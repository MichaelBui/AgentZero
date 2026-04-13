# LifeLog - Architecture Design

> Standalone personal knowledge retrieval API. Sensors push raw data; the server does all intelligence. Self-hosted on Strix Halo homelab.

## System Architecture

```mermaid
flowchart TD
    subgraph Sensors["Sensors"]
        S1["A0 hooks / n8n cron / any HTTP client"]
    end
    subgraph API["LifeLog API (Python/FastAPI)"]
        H["Handlers: /v1/ingest, /v1/query, /v1/job/*"]
        W["Ingest Worker (async background task)"]
        SVC["Services: Ingest, Query, Embed, Job"]
        REPO["Repos: ChunkRepo, TaskRepo, ResourceRepo, LLMRepo, QueueRepo"]
    end
    subgraph Infra["Infrastructure"]
        PG["PG17 VectorChord :5434"]
        RD["Redis 7.4 :6379"]
        LLM["LiteLLM :4000 -> llama-swap :8080"]
    end
    S1 -->|"POST multipart"| H
    H --> RD
    RD -->|"Redis Streams\nlifelog:ingest"| W --> SVC --> REPO
    REPO --> PG & RD & LLM
    H -->|"sync query"| SVC
```

**Key decisions:** Single container (API + worker). Clean Architecture (Handler -> Service -> Repository -> Model). Redis Streams for async ingestion. 1024d embeddings via Matryoshka truncation. No auth (internal network only).

## Models

| Model | Purpose | Native Dim | Used Dim |
|---|---|---|---|
| **Qwen3-Embedding-4B** (Q8_0) | Embedding | 2560 | 1024 (MRL truncation in app code) |
| **Qwen3-Reranker-4B** (Q8_0, VooDisss) | Re-ranking | - | - |
| Qwen3.5-35B | LLM (summary, tasks, chunking, context) | - | - |

## Data Model

```mermaid
erDiagram
    resources ||--o{ atomic_items : contains
    resources ||--o{ resource_tasks : linked
    tasks ||--o{ resource_tasks : linked
    tasks ||--o{ task_relationships : "source or target"
    atomic_items ||--o{ chunks : "chunked into"

    resources {
        uuid id PK
        text source "google_chat gmail jira agent_zero file"
        text external_id UK
        text name
        text summary "LLM-generated"
        uuid last_processed_item_id
        jsonb metadata
    }
    atomic_items {
        uuid id PK
        uuid resource_id FK
        text external_id
        text content
        text content_hash UK "SHA256 dedup"
        timestamptz source_ts
        jsonb metadata "sender, thread_id, labels, etc"
    }
    chunks {
        uuid id PK
        uuid resource_id FK
        text enriched_content "context + content"
        vector_1024 embedding
        tsvector tsv
        boolean is_full "TRUE if >= 300 tokens"
        int2 chunk_index
    }
    tasks {
        uuid id PK
        text title
        text description
        text status "pending/in_progress/blocked/done"
        text status_source "auto or manual"
        text priority
        int2 accuracy "-5 worst to 5 best, default 0"
        int2 relevancy "-5 worst to 5 best, default 0"
        text_arr labels
        vector_1024 embedding
        tsvector tsv
        jsonb metadata "assignee, due_date, project, etc"
    }
    resource_tasks {
        uuid resource_id FK
        uuid task_id FK
    }
    task_relationships {
        uuid source_task_id FK
        uuid target_task_id FK
        text relationship_type "blocks/parent_of/duplicate_of/related_to"
    }
```

**n:n resources-tasks:** A task can span multiple resources (same action in email + chat). **Directional relationships:** `blocks` means source prevents target; inverse derived in code (no `blocked_by` row).

## API Endpoints

| Method | Path | Purpose | Response |
|---|---|---|---|
| `POST` | `/v1/ingest` | Multipart: JSON metadata + optional files (PDF/DOCX) | `202` (queued) |
| `POST` | `/v1/query` | Hybrid search (chunks + tasks) | `200` |
| `POST` | `/v1/job/gchat` | Trigger Google Chat sync (n8n cron) | `202` |
| `POST` | `/v1/job/gmail` | Trigger Gmail sync (n8n cron) | `202` |
| `POST` | `/v1/job/jira` | Trigger Jira sync (n8n cron) | `202` |
| `GET` | `/health` | Liveness check | `200` |

## Ingestion Pipeline

**Order matters (dependencies):** Persist -> Summary -> Tasks -> Chunk -> Context -> Embed -> Store

```mermaid
sequenceDiagram
    participant S as Sensor
    participant A as API
    participant Q as Redis Streams
    participant W as Worker
    participant L as LLM
    participant P as PG17

    S->>A: POST /v1/ingest
    A->>Q: XADD (no validation, capture first)
    A-->>S: 202

    Q->>W: XREADGROUP BLOCK 5000
    W->>P: Upsert resource + items (dedup content_hash)
    W->>L: Resource summary (full resource)
    W->>L: Task extraction (full resource + existing tasks)
    W->>W: Adaptive chunking (buffer + semantic split + overlap)
    W->>L: Contextual retrieval (summary + per-chunk context)
    W->>L: Embed chunks + tasks (1024d)
    W->>P: Store all
    W->>Q: XACK
```

**Worker:** Single asyncio background task. `XREADGROUP` blocking read, 1 message at a time. Unacked messages redeliver after 5 min. DLQ after 3 failures. Idempotent via content_hash.

## Adaptive Chunking

Data: Google Chat avg 108 tokens/msg, Gmail avg 220 tokens/email. Most items are SHORT.

| Param | Value | Why |
|---|---|---|
| MIN_CHUNK | 300 tokens | Below this, embedding quality degrades |
| MAX_CHUNK | 500 tokens | Above this, semantic precision drops |
| OVERLAP | 20% | Context preservation across boundaries |

**Algorithm:**
1. Find `is_full=FALSE` chunk for resource -> delete it, put its items back in buffer
2. Add new items to buffer
3. For each item: if > MAX_CHUNK, LLM semantic split into 300-500 segments. Otherwise accumulate in buffer, emit as chunk when buffer >= MIN_CHUNK
4. Trailing chunk gets `is_full=FALSE`
5. Apply 20% overlap between adjacent chunks (prepend last 20% of previous chunk)
6. Prepend resource summary + LLM context per chunk

**Incremental ingestion:** Only new atomic items processed. Unfull trailing chunk is reopened (deleted + re-chunked with new items). Full chunks are immutable.

## Retrieval Pipeline

Every query searches BOTH chunks and tasks in parallel (always-on dual search, ~215ms overhead for tasks).

All top-N values are configurable via settings (defaults shown):

1. Embed query (1024d, shared)
2. Parallel: Chunk hybrid (dense top 50 + BM25 top 50 -> RRF) | Task hybrid (top 20 + 20 -> RRF)
3. Re-rank: chunks top 50 -> 20, tasks top 20 -> 20
4. Lost-in-Middle reorder chunks
5. Task relevance threshold filter (accuracy >= 0, relevancy >= 0)
6. Compose: separate sections (Context / Tasks)

## Scheduling

| Source | Trigger | Frequency |
|---|---|---|
| Google Chat | n8n -> `POST /v1/job/gchat` | Every 5 min |
| Gmail | n8n -> `POST /v1/job/gmail` | Every 15 min |
| Jira | n8n -> `POST /v1/job/jira` | Every 1 hour |
| Agent Zero | `monologue_end` hook -> `POST /v1/ingest` | Event-driven |

Job endpoints run source-specific sync logic internally (fetch from APIs using stored credentials), push to Redis Streams, return `202` immediately.

## Task Model

- Extracted from **full resource** (not chunks) - 1 LLM call per resource
- Tasks n:n with resources (junction table)
- Full re-extraction when new items arrive (LLM sees all items + existing tasks)
- Auto-status advances only (pending -> in_progress -> done, never regresses)
- `status_source = 'manual'` overrides are NEVER touched by auto-update
- Dedup: cosine > 0.85 + BM25 title match -> update; else create
- Labels: KIV, important, done, irrelevant, follow-up, custom (`project:X`)

## Techniques

**Phase 1 (ADOPT):** Contextual Retrieval (-67% failures), Semantic Chunking (+9% recall), Adaptive Chunking (is_full), Resource Summary, Task Extraction, Hybrid Search (+10-30% MRR), Re-Ranking (+15-40% NDCG@10), Always-On Dual Search, Lost-in-Middle, Matryoshka 1024d

**Phase 2 (EVALUATE):** HyDE, Multi-Query Expansion, Reverse HyDE, Parent Document Retrieval - triggered by recall < 0.7

**Phase 3+ (DEFER):** Late Chunking, ColBERT, RAPTOR, Knowledge Graph, LLM Query Classification

## Storage (1024d)

| Scale | Total |
|---|---|
| Current (5.5K docs) | ~126 MB |
| 10x | ~1.3 GB |
| 100x | ~12.5 GB |

## Phases

| Phase | Scope | Status |
|---|---|---|
| 0: Infrastructure | PG17, Qwen3 4B models, LiteLLM | **COMPLETE** |
| 1: Foundation | API server, schema, worker, first job | **COMPLETE** |
| 2: Sensors | gchat/gmail/jira jobs + n8n | **COMPLETE** |
| 3: Agent Integration | A0 search tool, task labels | Pending |
| 4: Quality | 50 test queries, tune, Phase 2 techniques | Pending |
| 5: Expansion | Confluence, PDF/DOCX, Cursor MCP | Pending |

## References

| Source | Link |
|---|---|
| Contextual Retrieval | [Anthropic 2024](https://www.anthropic.com/news/contextual-retrieval) |
| Semantic Chunking | [ScienceDirect 2025](https://www.sciencedirect.com/science/article/pii/S0950705125019343) |
| Hybrid + Re-Ranking | [NVIDIA 2026](https://developer.nvidia.com/blog/enhancing-rag-pipelines-with-re-ranking/) |
| Chunking Best Practices | [Firecrawl 2026](https://www.firecrawl.dev/blog/best-chunking-strategies-rag) |
| Lost-in-Middle | [Redis 2026](https://redis.io/blog/10-techniques-to-improve-rag-accuracy/) |
| Always-On Dual Search | [ScienceDirect 2026](https://www.sciencedirect.com/science/article/pii/S0278612526001020) |
| Qwen3-Embedding-4B GGUF | [HuggingFace](https://huggingface.co/Qwen/Qwen3-Embedding-4B-GGUF) |
| Qwen3-Reranker-4B GGUF | [VooDisss](https://huggingface.co/VooDisss/Qwen3-Reranker-4B-GGUF-llama_cpp) |
