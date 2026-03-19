# Jira Skill - Architecture

> Combined skill replacing `jira-query-listing`, `jira-filter-listing`, and `jira-view-listing`.
> Self-contained - all dependencies (DB, cleaner, summarizer) are embedded in `scripts/`.

## High-Level Flow

```mermaid
flowchart TD
    A["1/ Entry Point Selection"] --> B{"Which mode?"}
    B -->|"--jql"| C["jira_query.py"]
    B -->|"--filter-id"| D["jira_filter.py"]
    B -->|"--viewId"| E["jira_view.py"]

    D --> D1["Resolve filter ID to JQL\nGET /rest/api/3/filter/{id}"]
    E --> E1["Resolve view to JQL\nGraphQL polarisView\n(24h file cache)"]

    C --> F["2/ Fetch Issues via REST API\nGET /rest/api/3/search/jql"]
    D1 --> F
    E1 --> F

    F --> G["3/ Timestamp Check\nCompare API updated_at\nvs cached updated_at"]
    G -->|"Unchanged"| G1["Skip issue entirely"]
    G -->|"Newer or new"| G2["Format Issue\nADF to text, clean,\nextract full metadata"]

    G2 --> H["4/ Cache in SQLite\nupsert_atomic per ticket + comment\nFull content, no truncation\nStore relationships"]

    H --> K["5/ AI Summarization\nOnly for changed tickets\nIncremental: existing summary + new items\n1000 tokens max (configurable)"]
    G1 --> L["Use cached summary"]
    K --> M["6/ Stream output\n## jira/{key}: {title}\n{metadata}\n{summary}\nFlush per ticket"]
    L --> M
```

## Data Model

```mermaid
erDiagram
    ATOMIC_CONTENT {
        text id PK "jira:{ticket_key}:{item_id}"
        text source "jira"
        text resource_id "DPD-645"
        text item_id "ticket key or comment ID"
        text author "Michael Bui"
        text content "Full cleaned text"
        text created_at "ISO timestamp"
        text updated_at "ISO timestamp from Jira"
        text cached_at "When we stored it"
        text metadata "JSON: status, priority, labels, etc"
    }

    RESOURCE_SUMMARY {
        text resource_id PK "DPD-645"
        text source "jira"
        text title "DPD-645: Ticket title"
        text summary "AI-generated summary"
        text summarized_at "When summary was generated"
        text metadata "JSON: full ticket metadata"
    }

    TICKET_RELATIONSHIPS {
        text source_key "DPD-645"
        text target_key "DPD-644"
        text relation_type "parent | child | blocks"
        text cached_at "When cached"
    }

    ATOMIC_CONTENT ||--o{ RESOURCE_SUMMARY : "summarized into"
    ATOMIC_CONTENT ||--o{ TICKET_RELATIONSHIPS : "has relationships"
```

## Change Detection Flow

```mermaid
flowchart TD
    A["Jira API returns issue listing\nwith updated_at timestamp"] --> B{"issue_needs_fetch:\nCompare API updated_at\nvs cached updated_at"}
    B -->|"Same timestamp"| C["Skip entirely\nNo format, no cache, no LLM"]
    B -->|"Newer or new"| D["format_issue:\nADF to text, clean,\nextract full metadata"]

    D --> E["cache_issue:\nupsert ticket body as atomic item\n(item_id = ticket key)"]
    E --> F["cache_issue:\nupsert each comment\n(item_id = comment ID)"]
    F --> G["Clear + rebuild relationships\nparent, child, blocks, etc"]

    G --> H{"needs_resummarize:\nsummarized_at < latest updated_at?"}
    H -->|"No"| I["Use cached summary"]
    H -->|"Yes"| J{"Existing summary?"}
    J -->|"Yes"| K["Incremental summarization:\nexisting summary + items since\nlast summarized_at"]
    J -->|"No"| L["Full summarization:\nall atomic items for resource"]
    K --> M["upsert_summary in DB"]
    L --> M
```

## Incremental Summarization

When a ticket has an existing summary and new/updated content, the system provides both to the LLM:
1. Retrieves the existing summary text
2. Fetches only atomic items with `updated_at > summarized_at`
3. Sends both to the LLM with an "update" prompt that preserves historical context

This ensures old content outside the current API fetch window is not lost.

With `--force`, all atomic items are re-fetched and the full content is re-summarized regardless of timestamps.

## Relationship Tracking

```mermaid
flowchart TD
    subgraph "Example Ticket Hierarchy"
        P["DPD-644\nParent Epic"]
        T["DPD-645\nCurrent Ticket"]
        L1["DPD-273\nBlocked Ticket"]
        L2["OMNI-1418\nPolaris Link"]
    end

    P -->|"parent"| T
    T -->|"blocks"| L1
    P -->|"polaris-work-item-link"| L2

    subgraph "ticket_relationships table"
        R1["DPD-645 -> DPD-644 (parent)"]
        R2["DPD-645 -> DPD-273 (blocks)"]
        R3["DPD-644 -> OMNI-1418 (polaris-work-item-link)"]
    end
```

## Output Format

Each ticket is streamed to stdout as it becomes ready (from cache or after LLM returns). Tickets are NOT batched - output is flushed immediately per ticket:

```
## jira/{key}: {title}
Source: jira | Key: {key} | Status: {status} ({category}) | Type: {type} | Priority: {priority} | Assignee: {assignee} | Reporter: {reporter} | Due: {date} | {relationships}
{AI-generated summary - current status, decisions, pending actions, key dates}
```

- Title in the database is stored without the key prefix (clean title only)
- Use `PYTHONUNBUFFERED=1 python3 -u` for real-time streaming to file
- Progress and diagnostics are written to stderr

## File Structure

```
jira/
├── SKILL.md                  # Agent-facing documentation
├── _architecture.md          # This file (human-facing design)
├── data/
│   └── jira_cache.db         # SQLite (persistent, auto-created at runtime)
└── scripts/
    ├── jira_common.py        # Core: auth, ADF, format, cache, summarize, output
    ├── jira_db.py            # Self-contained SQLite DB (SkillDB class)
    ├── jira_cleaner.py       # Self-contained text cleanup for Jira content
    ├── jira_summarizer.py    # Self-contained LLM summarization via LiteLLM
    ├── jira_query.py         # Entry: --jql
    ├── jira_filter.py        # Entry: --filter-id (resolves JQL via REST)
    └── jira_view.py          # Entry: --viewId (resolves JQL via GraphQL)
# Transactional output → /a0/usr/workdir/jira-output.md, jira-debug.log
```

## Module Dependencies

```mermaid
flowchart TD
    JQ["jira_query.py"] --> JC["jira_common.py"]
    JF["jira_filter.py"] --> JC
    JV["jira_view.py"] --> JC

    JC --> DB["jira_db.py\nSkillDB class"]
    JC --> CL["jira_cleaner.py\nclean_jira_text"]
    JC --> SM["jira_summarizer.py\nLiteLLM proxy call"]

    DB --> SQ["SQLite3\n(stdlib)"]
    SM --> LL["LiteLLM Proxy\nhttps://llm.gigary.com/v1\nModel: local/qwen3.5-35b-a3b:instruct-reasoning"]
```

## Metadata Captured

| Field | Source | Stored In |
|---|---|---|
| status, status_category | fields.status | atomic metadata |
| assignee, reporter | fields.assignee/reporter.displayName | atomic metadata |
| priority | fields.priority.name | atomic metadata |
| issuetype | fields.issuetype.name | atomic metadata |
| resolution | fields.resolution.name | atomic metadata |
| duedate | fields.duedate | atomic metadata |
| labels | fields.labels | atomic metadata |
| components | fields.components[].name | atomic metadata |
| fix_versions | fields.fixVersions[].name | atomic metadata |
| parent_key | fields.parent.key | atomic metadata + relationships |
| subtask_keys | fields.subtasks[].key | atomic metadata + relationships |
| linked_issues | fields.issuelinks[].type + key | atomic metadata + relationships |

## Token Reduction Estimates

| Stage | Input | Output | Reduction |
|---|---|---|---|
| Raw Jira API response | ~86KB (~22K tokens) | - | - |
| Layer 1: Deterministic cleanup | 22K tokens | ~12K tokens | ~45% |
| Layer 2: Skip unchanged (re-run) | 12K tokens | 0 (cached) | 100% |
| Layer 3: AI summarization | 12K tokens | ~700 tokens (~500 words) | ~94% |
| **Total (first run)** | **22K tokens** | **~700 tokens** | **~97%** |
| **Total (re-run, no changes)** | **22K tokens** | **~0 processing** | **~100%** |

## Environment Variables

| Variable | Required | Default | Purpose |
|---|---|---|---|
| `JIRA_EMAIL` | Yes | - | Jira authentication email |
| `JIRA_API_KEY` | Yes | - | Jira API token |
| `LITELLM_API_KEY` / `API_KEY_OTHER` | Yes | - | LiteLLM proxy auth (set via Terraform) |
| `LITELLM_BASE_URL` | No | `https://llm.gigary.com/v1` | LiteLLM proxy endpoint |
| `SUMMARIZE_MODEL` | No | `local/qwen3.5-35b-a3b:instruct-reasoning` | LLM model for summarization |
| `MAX_SUMMARY_WORDS` | No | `500` | Max words per summary (in prompt) |
