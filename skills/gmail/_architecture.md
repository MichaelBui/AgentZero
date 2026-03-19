# Gmail Skill - Architecture

> Replaces `gmail-thread-reader`. Self-contained with SQLite caching, incremental fetching, and AI summarization.
> All dependencies (DB, cleaner, summarizer) are embedded in `scripts/`.

## High-Level Flow (Two-Phase Architecture)

```mermaid
flowchart TD
    A["1/ Connect to Chrome via CDP\nhttp://192.168.1.11:9223"] --> P1

    subgraph P1["Phase 1: Listing Scan"]
        B["Navigate to Gmail Search\nnewer_than:{days}d/p{page}"] --> C["Extract Thread Listing\nAll data available without clicking"]
        C --> D["For each non-excluded thread"]
        D --> D1{"Listing-Level Change Detection\nCompare data-legacy-last-non-draft-message-id\nvs cached last_message_id"}
        D1 -->|"Same ID"| SKIP["Mark as unchanged\n(will use cached summary)"]
        D1 -->|"Different or new"| FETCH["Add to fetch queue"]
        SKIP --> CHK{"Early stop?\nN consecutive cached"}
        FETCH --> CHK
        CHK -->|"Triggered"| SKIPALL["Skip fetching for remaining\nContinue scan, use cached data"]
        CHK -->|"No + more threads needed"| NP{"More pages?"}
        NP -->|"Yes"| B
    end

    subgraph P2["Phase 2: Detail Fetch"]
        F1["For each thread in fetch queue"] --> F2["Navigate directly to\n#all/{thread_id}"]
        F2 --> F3["Expand all messages\nExtract messages with data-legacy-message-id"]
        F3 --> F4["Deterministic cleanup\nStrip HTML, signatures, quoted replies"]
        F4 --> F5["Cache in SQLite\nupsert_atomic per message"]
    end

    subgraph P3["Phase 3: Summarize & Output"]
        S1["For each thread (all)"] --> S2{"needs_resummarize?"}
        S2 -->|"No"| S3["Use cached summary"]
        S2 -->|"Yes"| S4["Incremental LLM summarization\nExisting summary + new items\nMax 500 words"]
        S3 --> S5["Stream output immediately\n## gmail/{thread_id}: {subject}"]
        S4 --> S5
    end

    P1 --> P2
    P2 --> P3
```

### Why Two Phases?

1. **Phase 1 (Listing Scan)** collects all thread metadata by paginating through search results via URL (`/pN`). No threads are opened - only DOM attributes from listing rows.
2. **Phase 2 (Detail Fetch)** navigates directly to each thread URL (`#all/{thread_id}`) for content extraction. This avoids back-navigation issues and pagination state corruption.
3. **Phase 3 (Summarize)** processes all threads (cached + newly fetched) and streams output.

### Pagination

Gmail search results are paginated using URL hash suffix: `#search/newer_than%3A{days}d/p{page_num}`. Page 1 has no suffix; page 2+ uses `/pN`. Each page shows ~100 threads. The script navigates to successive pages until `max-threads` or `max-scan` is reached.

### Early Stop

Configurable via `--early-stop N` (default: 5, 0=disabled). When N consecutive threads are found unchanged in the DB, fetching stops but listing scan continues. All remaining threads are treated as unchanged and included in the output using cached data. This preserves the full response while skipping expensive detail fetches.

## Data Available at Thread Listing (Without Opening Thread)

All of the following are extracted from `<SPAN>` elements inside each `tr[jscontroller]` row:

| Field | DOM Source | Example | Notes |
|---|---|---|---|
| `data-legacy-thread-id` | `span[data-legacy-thread-id]` | `19ceb94ec915103d` | **Stable thread ID (hex)** - our `resource_id` |
| `data-legacy-last-non-draft-message-id` | `span[data-legacy-last-non-draft-message-id]` | `19cf12e94c0556b8` | **Last message ID** - for change detection |
| subject | `span.bog` in `tds[5]` | Full subject text | Thread subject |
| senders | `span[email]` elements | Name + email pairs | All thread participants |
| labels | `div.at` elements | Inbox, custom labels | Gmail labels |
| date | `tds[8] span[title]` | `Sun, Mar 15, 2026, 11:08 AM` | Date of most recent message |
| snippet | `span.y2` in `tds[5]` | ~120 chars | Preview of latest message |

## Data Available Inside Thread (After Clicking)

| Field | DOM Source | Example | Notes |
|---|---|---|---|
| `data-legacy-thread-id` | `h2.hP[data-legacy-thread-id]` | `19ceb94ec915103d` | Same as listing (confirmation) |
| `data-legacy-message-id` | `div.adn[data-legacy-message-id]` | `19ceb94ec915103d` | **Per-message ID (hex)** - our `item_id` |
| subject | `h2.hP` text content | Full thread subject | |
| from (per message) | `span.gD[email]` | Name + email | Message sender |
| to, cc (per message) | `table.ajB` detail rows | Name + email lists | Recipients |
| date (per message) | `span.g3[title]` | `Mar 14, 2026, 9:02 AM` | Message timestamp |
| body (per message) | `div.a3s.aiL` or `div.a3s` | Full email body | Cleaned before caching |

## ID Conventions

All IDs use the **legacy hex format** for consistency (since listing-level data uses legacy format).

| Concept | Value | Example |
|---|---|---|
| `resource_id` | `data-legacy-thread-id` | `19ceb94ec915103d` |
| `item_id` | `data-legacy-message-id` | `19ceb94ec915103d` |
| Change detection key | `data-legacy-last-non-draft-message-id` | `19cf12e94c0556b8` |
| Composite key | `gmail:{resource_id}:{item_id}` | `gmail:19ceb94ec915103d:19ceb94ec915103d` |

Note: The first message in a thread shares the same legacy ID as the thread itself (thread_id == first_message_id).

## Data Model

```mermaid
erDiagram
    ATOMIC_CONTENT {
        text id PK "gmail:{thread_id}:{message_id}"
        text source "gmail"
        text resource_id "data-legacy-thread-id (hex)"
        text item_id "data-legacy-message-id (hex)"
        text author "Jane Doe jane@example.com"
        text content "Cleaned email body (full, no truncation)"
        text created_at "Email date from DOM"
        text updated_at "Same as created_at (emails immutable)"
        text cached_at "When we stored it"
        text metadata "JSON: subject, to, cc, labels, priority"
    }

    RESOURCE_SUMMARY {
        text resource_id PK "data-legacy-thread-id (hex)"
        text source "gmail"
        text title "Re: Project Update"
        text summary "AI-generated thread summary (max 500 words)"
        text summarized_at "When summary was generated"
        text metadata "JSON: labels, priority, senders, last_message_id"
    }

    ATOMIC_CONTENT ||--o{ RESOURCE_SUMMARY : "summarized into"
```

## Change Detection Flow

```mermaid
flowchart TD
    A["Thread in search listing\nExtract data-legacy-thread-id\nand data-legacy-last-non-draft-message-id"] --> B{"Thread exists in DB?"}
    B -->|"No"| C["NEW THREAD\nAdd to fetch queue"]
    B -->|"Yes"| D{"Compare listing's\ndata-legacy-last-non-draft-message-id\nvs cached last_message_id"}

    D -->|"Same"| E["LISTING-LEVEL SKIP\nNo new non-draft messages\nUse cached data in Phase 3"]
    D -->|"Different"| F["New messages exist\nAdd to fetch queue"]

    C --> G["Phase 2: Navigate to\n#all/{thread_id}\nExpand all messages"]
    F --> G

    G --> H{"For each message:\ndata-legacy-message-id\nin cached items?"}
    H -->|"Yes"| I["Skip (already cached)\nEmails are immutable"]
    H -->|"No"| J["Clean and cache\nnew message"]

    J --> K["Update last_message_id\nin resource metadata"]
    I --> K

    E --> L["Phase 3: Check needs_resummarize"]
    K --> L

    L -->|"No changes"| M["Use cached summary\nStream output"]
    L -->|"New items"| N["Incremental summarization\nExisting summary + new messages\nMax 500 words"]
    N --> O["Stream output\n## gmail/{thread_id}: {subject}"]
    M --> O
```

## Email Immutability

Gmail messages are **immutable once sent** - body content never changes. Threads grow only by new replies. This simplifies our logic:
- If `data-legacy-last-non-draft-message-id` matches cached value -> no new messages -> skip entirely
- If it differs -> new messages added -> open thread, cache ONLY new messages
- Existing cached messages never need re-fetching or updating
- No need for `updated_at` comparison per message (unlike Jira where comments can be edited)

## Deterministic Cleanup Pipeline

```mermaid
flowchart TD
    A["Raw email body\nfrom Gmail DOM innerText"] --> B["Strip residual HTML tags\nDecode entities"]
    B --> C["Remove quoted replies\n'On ... wrote:' blocks"]
    C --> D["Remove email signatures\n'--', 'Best regards',\n'Sent from my iPhone', etc."]
    D --> E["Normalize whitespace\nCollapse triple+ newlines\nCollapse triple+ spaces"]
    E --> F["Cleaned body\nFull content preserved\n(no truncation)"]
```

## Output Format

Each thread is streamed to stdout immediately when its summary is ready:

```
## gmail/19ceb94ec915103d: Re: Project Update
Source: gmail | Thread: 19ceb94ec915103d | Labels: Inbox, IMPORTANT | Priority: IMPORTANT | Senders: Jane Doe, Bob Smith | Last Date: Sun, Mar 15, 2026, 11:08 AM
[AI-generated summary - participants, key decisions, action items, timeline, max 500 words]
```

- Each block streamed with `print(..., flush=True)`
- Use `PYTHONUNBUFFERED=1 python3 -u` for real-time streaming to file
- Progress and diagnostics go to stderr
- No `---` separators (saves tokens)

## File Structure

```
gmail/
├── SKILL.md                  # Agent-facing documentation
├── _architecture.md          # This file (human-facing design)
├── data/
│   └── gmail_cache.db        # SQLite (persistent, auto-created at runtime)
└── scripts/
    ├── gmail_reader.py       # Main script: CDP + listing + caching + output
    ├── gmail_db.py           # Self-contained SQLite DB management
    ├── gmail_cleaner.py      # Self-contained email body cleanup
    └── gmail_summarizer.py   # Self-contained LLM summarization via LiteLLM
# Transactional output → /a0/usr/workdir/gmail-output.md, gmail-debug.log
```

## Module Dependencies

```mermaid
flowchart TD
    GR["gmail_reader.py\n(main entry point)"] --> DB["gmail_db.py\nSkillDB: atomic_content\n+ resource_summary"]
    GR --> CL["gmail_cleaner.py\nclean_email_body()"]
    GR --> SM["gmail_summarizer.py\nsummarize_resource()"]
    GR --> PW["playwright\nChrome CDP connection"]

    DB --> SQ["SQLite3 (stdlib)"]
    SM --> LL["LiteLLM Proxy\nhttps://llm.gigary.com/v1\nModel: local/qwen3.5-35b-a3b:instruct-reasoning"]
    PW --> CH["Remote Chrome\n192.168.1.11:9223"]
```

## Arguments

| Argument | Default | Description |
|---|---|---|
| `--cdp-url` | `http://192.168.1.11:9223` | Chrome DevTools Protocol endpoint |
| `--days` | `3` | Days to look back |
| `--max-threads` | `50` | Max non-excluded threads to process |
| `--max-scan` | `100` | Max total threads to scan across all pages (safety cap) |
| `--early-stop` | `5` | Stop fetching after N consecutive cached threads; scan continues, output includes all (0=disabled) |
| `--exclude-labels` | `["❌ ai-exclusion", "🪣 Bitbucket"]` | JSON array of labels to skip |
| `--priority-labels` | `["⚠️IMPORTANT", ...]` | JSON array of priority labels (highest first) |
| `--cached-only` | `false` | Output cached summaries from DB without browser (fast, for reports) |
| `--force` | `false` | Bypass change detection, re-fetch and re-summarize all |
| `--output` | `workdir/gmail-output.md` | Write results to file (clean markdown for AI agents) |
| `--debug-log` | `workdir/gmail-debug.log` | Write debug/progress messages to file |

## Metadata Captured

| Field | Source | Stored In |
|---|---|---|
| thread_id (resource_id) | `data-legacy-thread-id` from listing | All tables |
| last_message_id | `data-legacy-last-non-draft-message-id` from listing | resource_summary metadata |
| message_id (item_id) | `data-legacy-message-id` from thread view | atomic_content |
| subject | `span.bog` at listing / `h2.hP` in thread | resource_summary title |
| senders | `span[email]` at listing | resource_summary metadata |
| labels | `div.at` at listing | atomic metadata + summary metadata |
| priority | Matched from priority_labels config | summary metadata |
| from, to, cc | Per-message headers in thread view | atomic metadata |
| date | Per-message `span.g3[title]` | atomic created_at/updated_at |
| snippet | `span.y2` at listing (~120 chars) | Not stored (full body cached instead) |

## Environment Variables

| Variable | Required | Default | Purpose |
|---|---|---|---|
| `API_KEY_OTHER` / `LLAMA_TOKEN` | Yes | - | LiteLLM proxy auth (set via Terraform, or LLAMA_TOKEN) |
| `LITELLM_BASE_URL` | No | `https://llm.gigary.com/v1` | LiteLLM proxy endpoint |
| `SUMMARIZE_MODEL` | No | `local/qwen3.5-35b-a3b:instruct-reasoning` | LLM model for summarization |
| `MAX_SUMMARY_WORDS` | No | `500` | Max words per summary (in prompt) |

## Token Reduction Estimates

| Stage | Input | Output | Reduction |
|---|---|---|---|
| Raw Gmail extraction (100 threads, 7 days) | ~500K-1MB (125-250K tokens) | - | - |
| Layer 1: Deterministic cleanup | 125-250K tokens | ~60-120K tokens | ~50% |
| Layer 2: Skip unchanged threads (re-run) | 60-120K tokens | 0 (cached) | 100% |
| Layer 3: AI summarization | 60-120K tokens | ~50K tokens (100 x 500 words) | ~60% |
| **Total (first run)** | **125-250K tokens** | **~50K tokens** | **~80%** |
| **Total (re-run, no changes)** | **125-250K tokens** | **~0 processing, ~50K cached output** | **~100%** |

Performance: First run ~37min (102 threads). Re-run with cache: ~2min (3 new threads out of 105).

## Key Differences from Jira Skill

| Aspect | Jira | Gmail |
|---|---|---|
| Data source | REST API | Chrome CDP (browser automation) |
| Resource ID | Ticket key (DPD-645) | `data-legacy-thread-id` (hex) |
| Item ID | Ticket key or comment ID | `data-legacy-message-id` (hex) |
| Content mutability | Mutable (comments can be edited) | **Immutable** (emails never change) |
| Listing-level ID | Available (ticket key in API) | Available (`data-legacy-thread-id`) |
| Change detection | `updated_at` timestamp comparison | `data-legacy-last-non-draft-message-id` comparison |
| Relationships | parent/child/blocks/linked tickets | None (flat thread structure) |
| Pagination | API `startAt` parameter | URL-based `/pN` hash suffix |
| Extraction strategy | Single-pass (API returns all) | Two-phase (listing scan + detail fetch) |
| Speed bottleneck | API rate limits | Browser navigation (~6-7s/thread) |
