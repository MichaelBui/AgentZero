# GChat Skill - Architecture

> Replaces `gchat-thread-reader`. Self-contained with SQLite caching, incremental fetching, and AI summarization.
> All dependencies (DB, cleaner, summarizer) are embedded in `scripts/`.

## High-Level Flow

```mermaid
flowchart TD
    A["1/ Connect to Chrome via CDP\nhttp://192.168.1.11:9223"] --> B["2/ Navigate to GChat Home\nchat.google.com/app/home"]
    B --> C["3/ Snapshot Home Feed\nFilter by date cutoff\nExtract group_id, topic_id,\nname, display_timestamp"]

    C --> D["4/ For Each Conversation"]
    D --> D1{"Change Detection\nCompare display_timestamp\nvs cached updated_at"}
    D1 -->|"Same or older"| SKIP["Skip opening conversation\n(use cached data in output)"]
    D1 -->|"Newer timestamp"| D2["Click feed item\nVerify 2-panel layout"]

    D2 --> D3["Scroll to bottom\nHandle Jump to bottom"]
    D3 --> D4["Scroll up + expand\nCollect messages progressively\nDedup by data_id"]
    D4 --> D5["Deterministic cleanup\nStrip bot noise\nFull content preserved"]
    D5 --> D6["Cache in SQLite\nupsert_atomic per message\nHash-based edit detection"]
    D6 --> D7["Return to Home feed"]

    SKIP --> E["5/ Summarize & Stream Output"]
    D7 --> E
    E --> E1{"needs_resummarize?\nNew/updated atomic items\nsince last summarization?"}
    E1 -->|"No"| E2["Use cached summary\nStream output immediately"]
    E1 -->|"Yes"| E3["Summarize via LLM\nIncremental: existing summary + new/changed items\nMax 500 words (configurable)"]
    E3 --> E4["Stream output immediately\n## gchat/{group_id}: {name}"]
    E2 --> E4
```

### Early Stop

Configurable via `--early-stop N` (default: 5, 0=disabled). When N consecutive conversations are found unchanged (timestamp match), scanning stops early. This significantly speeds up subsequent runs.

## Data Available in Home Feed (Without Opening Conversation)

| Field | DOM Source | Example | Notes |
|---|---|---|---|
| `data-group-id` | `span[role="listitem"][data-group-id]` | `dm/abc123` or `space/xyz789` | **Stable conversation ID** - our `resource_id` |
| `data-display-timestamp` | Same element | `1710513600000` (epoch_ms) | **Last activity timestamp** - for change detection |
| `data-topic-id` | Same element | `topic_id_string` | Thread/topic ID within conversation |
| `data-is-unread` | Same element | `true`/`false` | Unread indicator |
| name | `div.Vb5pDe` text nodes | `Nikhil Grover` | Conversation/person name |

## Data Available Inside Conversation (After Clicking)

| Field | DOM Source | Notes |
|---|---|---|
| `data-topic-id` | `c-wiz[data-topic-id]` | Thread container |
| `data-id` | `div[role="group"][data-id]` | **Per-message ID** - our `item_id` |
| sender | `span[data-member-id][data-name]` | Message author name |
| timestamp display | `span.FvYVyf` | Human-readable time |
| epoch_ms | `span[data-absolute-timestamp]` | Epoch milliseconds |
| body | Text walker on `div[role="group"]` | Extracted via TreeWalker, noise classes filtered |

## ID Conventions

| Concept | Value | Example |
|---|---|---|
| `resource_id` | `data-group-id` | `dm/abc123` or `space/xyz789` |
| `item_id` | `data-id` or `{epoch_ms}_{sender_hash}` | `message_id_123` or `1710513600000_42` |
| Change detection key | `data-display-timestamp` (epoch_ms) | `1710513600000` |
| Composite key | `gchat:{resource_id}:{item_id}` | `gchat:dm/abc123:message_id_123` |

## Data Model

```mermaid
erDiagram
    ATOMIC_CONTENT {
        text id PK "gchat:{group_id}:{data_id}"
        text source "gchat"
        text resource_id "data-group-id (conversation ID)"
        text item_id "data-id or epoch_sender fallback"
        text author "Nikhil Grover"
        text content "Cleaned message body (full, no truncation)"
        text created_at "ISO from epoch_ms"
        text updated_at "ISO from epoch_ms"
        text cached_at "When we stored it"
        text metadata "JSON: timestamp_display"
    }

    RESOURCE_SUMMARY {
        text resource_id PK "data-group-id"
        text source "gchat"
        text title "Conversation name"
        text summary "AI-generated summary (max 500 words)"
        text summarized_at "When summary was generated"
        text metadata "JSON: message_count, url"
    }

    ATOMIC_CONTENT ||--o{ RESOURCE_SUMMARY : "summarized into"
```

## Change Detection Flow

Change detection uses the `data-display-timestamp` from the feed to determine if a conversation has new activity since last cache:

```mermaid
flowchart TD
    A["Feed item in Home feed\nExtract data-group-id\nand data-display-timestamp"] --> B{"Compare display_timestamp\nvs latest cached updated_at"}
    B -->|"Same or older"| C["FEED-LEVEL SKIP\nNo new activity\nDo not open conversation"]
    B -->|"Newer"| D["Open conversation\nExtract all messages"]

    D --> E{"For each message:\ndata-id in cache?"}
    E -->|"No"| F["NEW MESSAGE\nClean and cache"]
    E -->|"Yes"| G["Skip (already cached)"]

    F --> H["Mark conversation changed"]

    C --> K["Check needs_resummarize"]
    G --> K
    H --> K

    K -->|"No changes"| L["Use cached summary\nStream output"]
    K -->|"New items"| M["Incremental summarization\nExisting summary + new messages\nMax 500 words"]
    M --> N["Stream output\n## gchat/{group_id}: {name}"]
    L --> N
```

Note: GChat messages can technically be edited after sending, but edit detection is **not implemented** in v1. Messages are treated as insert-only (like Gmail). If a conversation's `display_timestamp` increases, all messages are extracted and new ones are cached.

## GChat DOM Navigation (3-Panel Layout)

```mermaid
flowchart TD
    subgraph "3-Panel Layout"
        LP["Left Panel\nNavigation sidebar\nSpaces, DMs, etc."]
        MP["Middle Panel\nHome Feed (newsfeed)\nspan role=listitem\nThread listing"]
        RP["Right Panel\nConversation View\nc-wiz data-topic-id\nThread content"]
    end

    A["Click feed item\nin Middle Panel"] --> B{"Middle panel\nstill visible?"}
    B -->|"Yes"| C["Correct: 3-panel mode\nContent loaded in Right Panel\nProceed with extraction"]
    B -->|"No"| D["Wrong click: navigated away\nReturn to Home, skip item"]

    C --> E["Scroll Right Panel to bottom\nHandle Jump to bottom button"]
    E --> F["Scroll up progressively\nCollect messages at each step\nDedup by data_id"]
    F --> G{"Reached date cutoff\nor scroll limit?"}
    G -->|"No"| H["Expand collapsed bars\nShow more / See more"]
    H --> F
    G -->|"Yes"| I["Return sorted messages\nby epoch_ms"]
```

## Progressive Message Collection

GChat uses **virtual scrolling** - only messages near the viewport exist in the DOM at any time. Messages are collected progressively by scrolling and deduplicating:

1. Scroll to bottom of conversation
2. Extract all visible messages, dedup by `data_id`
3. Scroll up 800px, extract again, dedup
4. Repeat until date cutoff reached or scroll limit hit
5. Expand any collapsed message bars, extract again
6. Return all collected messages sorted by `epoch_ms`

## Deterministic Cleanup Pipeline

```mermaid
flowchart TD
    A["Raw message body\nfrom GChat DOM TreeWalker"] --> B["Filter noise CSS classes\nFvYVyf, njhDLd, cPjwNc, etc."]
    B --> C["Remove bot patterns\nAlert tags, monitoring noise\nAutomated notifications"]
    C --> D["Normalize whitespace\nCollapse triple+ newlines\nCollapse triple+ spaces"]
    D --> E["Cleaned body\nFull content preserved\n(no truncation)"]
```

## Output Format

Each conversation is streamed to stdout immediately when its summary is ready:

```
## gchat/dm/abc123: Nikhil Grover
Source: gchat | Group: dm/abc123 | Messages: 20 | Last Activity: 2026-03-15T12:30:00+00:00
[AI-generated summary - participants, key decisions, action items, max 500 words]
```

- Each block streamed with `print(..., flush=True)`
- Use `PYTHONUNBUFFERED=1 python3 -u` for real-time streaming to file
- Progress and diagnostics go to stderr
- No `---` separators (saves tokens)

## File Structure

```
gchat/
├── SKILL.md                  # Agent-facing documentation
├── _architecture.md          # This file (human-facing design)
├── data/
│   ├── .gitignore            # Excludes *.db from git
│   └── gchat_cache.db        # SQLite (auto-created at runtime)
└── scripts/
    ├── gchat_reader.py       # Main script: CDP + feed + caching + output
    ├── gchat_db.py           # Self-contained SQLite DB management
    ├── gchat_cleaner.py      # Self-contained chat message cleanup
    └── gchat_summarizer.py   # Self-contained LLM summarization via LiteLLM
```

## Module Dependencies

```mermaid
flowchart TD
    GR["gchat_reader.py\n(main entry point)"] --> DB["gchat_db.py\nSkillDB: atomic_content\n+ resource_summary"]
    GR --> CL["gchat_cleaner.py\nclean_chat_message()"]
    GR --> SM["gchat_summarizer.py\nsummarize_resource()"]
    GR --> PW["playwright\nChrome CDP connection"]

    DB --> SQ["SQLite3 (stdlib)"]
    SM --> LL["LiteLLM Proxy\nhttps://llm.gigary.com/v1\nModel: local/qwen3.5-35b-a3b:instruct-reasoning"]
    PW --> CH["Remote Chrome\n192.168.1.11:9223"]
```

## Arguments

| Argument | Default | Description |
|---|---|---|
| `--cdp-url` | `http://192.168.1.11:9223` | Chrome DevTools Protocol endpoint |
| `--days` | `7` | Days to look back |
| `--max-threads` | `50` | Max conversations to process |
| `--max-scan` | `100` | Max feed items to scan (safety cap) |
| `--max-scroll` | `20` | Max scroll-up iterations per conversation |
| `--max-expansion` | `5` | Max expansion rounds for collapsed messages |
| `--early-stop` | `5` | Stop after N consecutive unchanged conversations (0=disabled) |
| `--focus-title` | *(none)* | Substring filter for conversation titles |
| `--force` | `false` | Bypass change detection, re-fetch and re-summarize all |
| `--debug-dom` | `false` | Dump Home feed DOM to stderr and exit |

## Metadata Captured

| Field | Source | Stored In |
|---|---|---|
| group_id (resource_id) | `data-group-id` from feed | All tables |
| display_timestamp | `data-display-timestamp` from feed | Change detection |
| data_id (item_id) | `data-id` from message `div[role="group"]` | atomic_content |
| sender | `span[data-member-id][data-name]` | atomic_content author |
| timestamp | `span.FvYVyf` display text | atomic metadata |
| epoch_ms | `span[data-absolute-timestamp]` | atomic created_at/updated_at |
| conversation name | `div.Vb5pDe` text nodes | resource_summary title |

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
| Raw GChat extraction (50 convos, 7 days) | ~500KB (~125K tokens) | - | - |
| Layer 1: Deterministic cleanup | 125K tokens | ~60K tokens | ~50% |
| Layer 2: Skip unchanged convos (re-run) | 60K tokens | 0 (cached) | 100% |
| Layer 3: AI summarization | 60K tokens | ~25K tokens (50 x 500 words) | ~60% |
| **Total (first run)** | **~125K tokens** | **~25K tokens** | **~80%** |
| **Total (re-run, no changes)** | **~125K tokens** | **~0 processing, ~25K cached output** | **~100%** |

## Key Differences from Gmail Skill

| Aspect | Gmail | GChat |
|---|---|---|
| Data source | Chrome CDP (browser) | Chrome CDP (browser) |
| Resource ID | `data-legacy-thread-id` (hex) | `data-group-id` (path like `dm/abc`) |
| Item ID | `data-legacy-message-id` (hex) | `data-id` or epoch+sender fallback |
| Content mutability | **Immutable** (emails never change) | Mutable (edit detection skipped in v1) |
| Change detection | `last-non-draft-message-id` comparison | `display_timestamp` comparison |
| Pagination | URL-based `/pN` across search pages | Feed scroll (single-page virtual list) |
| Layout | Single-pane thread view | 3-panel (nav left, feed middle, conversation right) |
| Message loading | All visible after expand | Virtual scrolling (progressive collection) |
