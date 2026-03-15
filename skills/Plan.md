# Context Reduction Architecture Plan

> **Goal:** Reduce token consumption from ~270K+ tokens to <30K tokens for daily briefing by caching atomic content in SQLite, skipping unchanged resources, and summarizing at the logical level via a lightweight AI model.

## Problem Statement

| Source | Raw Size | Est. Tokens | Main Bloat |
|--------|----------|-------------|------------|
| Gmail (3-5 days, 20 threads) | 217-432KB | 54-108K | Signatures, quoted replies, HTML noise |
| Google Chat (3-5 days, 20 convos) | 348KB | ~87K | Bot messages, monitoring alerts, repeated greetings |
| Jira (filter, 20-50 tickets) | 86KB | ~22K | Full descriptions with ACs, nmap/sslscan outputs in comments, SAP API responses |
| **Total** | **~1.1MB** | **~270K+** | Exceeds most context windows |

## Architecture Overview

```
┌──────────────────────────────────────────────────────────┐
│                    Data Source Layer                       │
│  Gmail CDP  │  GChat CDP  │  Jira REST API               │
└──────┬──────┴──────┬──────┴──────┬───────────────────────┘
       │             │             │
       ▼             ▼             ▼
┌──────────────────────────────────────────────────────────┐
│              Layer 1: Deterministic Cleanup                │
│  Strip HTML, signatures, quoted text, bot noise           │
│  Select only essential fields (ID, author, timestamp,     │
│  content). Truncate individual messages at 2KB.           │
│  ~40-60% token reduction. Zero LLM cost.                  │
└──────────────────────┬───────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────┐
│              Layer 2: SQLite Cache                         │
│  Store atomic content (individual messages/comments)      │
│  with metadata (IDs, timestamps, relationships).          │
│  On re-run: compare timestamps → skip unchanged.          │
│  Incremental fetch = zero re-download cost.               │
└──────────────────────┬───────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────┐
│         Layer 3: Per-Resource AI Summarization             │
│  For each logical resource (Jira ticket, GChat thread,    │
│  Gmail thread): collect all atomic content → send to      │
│  lightweight model → produce summary (max 5000 tokens).   │
│  Store summary in SQLite. Re-summarize only when          │
│  atomic content changes.                                  │
│  ~80-90% total token reduction.                           │
└──────────────────────┬───────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────┐
│              Output: Compact Summaries                     │
│  All resource summaries as minified JSON to stdout.       │
│  Ready for the reasoning model's daily briefing.          │
│  Target: <30K tokens total across all sources.            │
└──────────────────────────────────────────────────────────┘
```

## SQLite Schema

Database location: `~/.cache/agent_zero_skills.db`

### Table: `atomic_content`

Stores individual messages, comments, and content items.

| Column | Type | Description |
|--------|------|-------------|
| `id` | TEXT PK | Composite key: `{source}:{resource_id}:{item_id}` |
| `source` | TEXT | `jira`, `gmail`, `gchat` |
| `resource_id` | TEXT | Logical resource: Jira ticket key, Gmail thread URL, GChat group_id |
| `item_id` | TEXT | Atomic item: comment ID, message index, email message-id |
| `author` | TEXT | Person who created the content |
| `content` | TEXT | Cleaned text content (after Layer 1 cleanup) |
| `created_at` | TEXT | ISO timestamp when content was created |
| `updated_at` | TEXT | ISO timestamp when content was last updated |
| `cached_at` | TEXT | ISO timestamp when we cached this item |
| `metadata` | TEXT | JSON blob for source-specific metadata |

### Table: `resource_summary`

Stores AI-generated summaries at the logical resource level.

| Column | Type | Description |
|--------|------|-------------|
| `resource_id` | TEXT PK | Same as `atomic_content.resource_id` |
| `source` | TEXT | `jira`, `gmail`, `gchat` |
| `title` | TEXT | Resource title (ticket summary, email subject, chat name) |
| `summary` | TEXT | AI-generated summary (max ~5000 tokens) |
| `content_hash` | TEXT | SHA256 of all atomic content for this resource (for change detection) |
| `summarized_at` | TEXT | ISO timestamp when summary was generated |
| `metadata` | TEXT | JSON blob for source-specific metadata (status, priority, labels, etc.) |

### Table: `fetch_state`

Tracks the last fetch timestamp per source to enable incremental fetching.

| Column | Type | Description |
|--------|------|-------------|
| `source_key` | TEXT PK | e.g. `jira:filter:13811`, `gmail:last_5d`, `gchat:last_5d` |
| `last_fetch_at` | TEXT | ISO timestamp of last successful fetch |
| `metadata` | TEXT | JSON blob (e.g. list of resource_ids fetched) |

## Shared Modules

All shared code lives in `skills/_shared/`.

### `skills/_shared/db.py`

SQLite database management:
- `get_db()` - Get or create database connection
- `init_db()` - Create tables if not exist
- `upsert_atomic(source, resource_id, item_id, author, content, created_at, updated_at, metadata)` - Insert or update atomic content
- `get_atomic_for_resource(source, resource_id)` - Get all atomic items for a resource
- `get_resource_summary(resource_id)` - Get existing summary
- `upsert_summary(resource_id, source, title, summary, content_hash, metadata)` - Insert or update summary
- `get_all_summaries(source)` - Get all summaries for a source
- `get_fetch_state(source_key)` - Get last fetch timestamp
- `set_fetch_state(source_key, metadata)` - Update fetch state
- `get_resource_ids_for_source(source)` - List all known resource IDs

### `skills/_shared/summarizer.py`

AI summarization via LiteLLM proxy:
- `summarize_resource(title, atomic_items, existing_summary=None)` - Generate/update summary
- Uses `local/qwen3.5-35b-a3b:thinking-general` via `https://llm.gigary.com/v1`
- Max output: ~5000 tokens
- If existing summary exists and only new content added, uses anchored update prompt

### `skills/_shared/cleaner.py`

Deterministic text cleanup:
- `clean_email_body(text)` - Strip signatures, quoted text, HTML, excessive whitespace
- `clean_chat_message(text)` - Strip bot noise, monitoring tags, excessive URLs
- `clean_jira_text(text)` - Strip redundant technical outputs (nmap, curl, sslscan blocks)
- `truncate(text, max_chars=2000)` - Hard truncate with `[truncated]` marker

## Skill Modifications

### Common Pattern (all skills)

Each skill gains a new `--use-cache` flag (default: true) and `--summarize` flag (default: false):

```
python script.py [existing args] --use-cache --summarize
```

When `--summarize` is used, stdout outputs summaries instead of raw data.

### Flow per skill:

1. **Fetch resource list** (thread list, ticket list, feed items)
2. **For each resource:** Check SQLite for existing atomic content timestamps
3. **If resource has new content:** Fetch full details, clean, store atomic content
4. **If resource is unchanged:** Skip fetching (use cached data)
5. **If `--summarize`:** For each resource with new/changed content, run AI summarization
6. **Output:** Either raw cleaned data (default) or summaries (`--summarize`)

### Jira Skills (query, filter, view)

**Fields to keep per ticket:**
- `key`, `id` (identification)
- `title` (summary)
- `status.name`, `status.category`
- `assignee`, `priority`, `labels`, `duedate`
- `parent.key`, `parent.summary`
- `created`, `updated`
- `comments[]`: only `author`, `created`, `body` (cleaned, truncated at 2KB each)

**Fields to strip:**
- `description` body beyond 2KB (keep first 2KB)
- `subtasks` (rarely needed for daily briefing)
- `links` (rarely needed for daily briefing)
- Comment bodies: Strip nmap outputs, sslscan outputs, curl responses, JSON API responses >500 chars

**Atomic content:** Each comment is one atomic item. Ticket metadata (title, status, description) is also one atomic item.

**Resource ID:** Jira ticket key (e.g. `DPD-383`)

### Gmail Thread Reader

**Fields to keep per message:**
- `from` (sender)
- `date` (timestamp)
- `body` (cleaned, truncated at 2KB)

**Fields to strip:**
- `to`, `cc` (kept only in metadata JSON, not in main content)
- Email signatures (detected by common patterns: `--`, `Best regards`, `Sent from`)
- Quoted replies (lines starting with `>` or `On ... wrote:`)
- HTML artifacts

**Atomic content:** Each email message is one atomic item.
**Resource ID:** Gmail thread URL

### Google Chat Thread Reader

**Fields to keep per message:**
- `sender` (person name)
- `timestamp`, `epoch_ms`
- `body` (cleaned, truncated at 2KB)

**Fields to strip:**
- Bot/app messages that are purely monitoring (e.g., Datadog alerts, build notifications)
- `[quoted]` sections
- `[links]` sections (URLs stored in metadata, not content)
- Repeated greetings/acknowledgments under 10 chars

**Atomic content:** Each chat message is one atomic item.
**Resource ID:** GChat group_id or `dm/{id}`

## Summarization Prompt

```
You are a concise executive assistant. Summarize the following {source_type} content for a daily work briefing.

Resource: {title}
Metadata: {metadata_json}

Content (chronological):
{all_atomic_content}

Instructions:
- Identify: What is the current status/state?
- Identify: What actions are pending and who owns them?
- Identify: What decisions were made?
- Identify: Key dates, deadlines, blockers
- Keep all person names, ticket IDs, dates, and technical references
- Be factual and specific - do not generalize
- Maximum 800 words
```

## Implementation Order

1. `skills/_shared/db.py` - SQLite foundation
2. `skills/_shared/cleaner.py` - Text cleanup utilities
3. `skills/_shared/summarizer.py` - AI summarization
4. Modify `jira-filter-listing` (most-used for daily briefing)
5. Modify `jira-query-listing`
6. Modify `jira-view-listing`
7. Modify `gmail-thread-reader`
8. Modify `gchat-thread-reader`

## Expected Results

| Metric | Before | After | Reduction |
|--------|--------|-------|-----------|
| Gmail tokens | 54-108K | ~5K (summaries) | 90-95% |
| GChat tokens | ~87K | ~5K (summaries) | 94% |
| Jira tokens | ~22K | ~5K (summaries) | 77% |
| **Total** | **~270K+** | **~15-20K** | **~93%** |
| Fetch time (re-run) | 10-20 min | <2 min (incremental) | 80-90% |
| LLM cost per run | High (all in reasoning model) | Low (cheap summarization model) | ~70% |

## Dependencies

- `sqlite3` (Python stdlib)
- `hashlib` (Python stdlib)
- `requests` (already approved)
- LiteLLM proxy at `https://llm.gigary.com/v1` (already running)
- Summarization model: `local/qwen3.5-35b-a3b:thinking-general` (already configured as utility model)
