---
name: jira
description: Fetch Jira tickets with SQLite caching, AI-driven relevance scoring, and structured summarization. Supports raw JQL query, saved filter by ID, or Polaris view. Outputs relevance-scored markdown summaries with mention detection, entity extraction, and adaptive detail levels. Use when the user asks to search, list, or summarize Jira tickets.
version: 4.0.0
author: Michael
tags: [jira, jql, search, tickets, query, filter, view, polaris, backlog, sprint, ntuclink, summarize, cache, relevance]
---

# Jira Skill

Single-file Jira skill (`jira.py`) with SQLite caching, incremental fetching, AI-driven relevance scoring, entity extraction, and adaptive summarization. Replaces all previous multi-file scripts. Self-contained - no external shared modules.

## When to Use

| User Intent | Command |
|---|---|
| Any combination of JQL, filter, and/or view | `python jira.py --jql '...' --filter-id N --view-id N` |
| Search tickets by JQL only | `python jira.py --jql '...'` |
| Fetch tickets from a saved Jira filter | `python jira.py --filter-id N` |
| Fetch tickets from a Polaris/board view | `python jira.py --view-id N` |
| Default: current user's active tickets | `python jira.py` |
| Fast report from cache (no API calls) | `python jira.py --cached-only` |
| Force full re-fetch and re-summarize | `python jira.py --force` |

Do NOT use for: creating/updating tickets, fetching non-NTUC Jira instances.

## Required Environment Variables
```
JIRA_EMAIL    - michael.bui@fairpricegroup.sg
JIRA_API_KEY  - loaded via secrets (never log full value)
API_KEY_OTHER - LiteLLM proxy authentication (set via Terraform, or LLAMA_TOKEN)
JIRA_DB_PATH  - (optional) Override SQLite DB path. Use when running from host Mac
                (NFS mount: /Volumes/Apps/...) since WAL mode fails on NFS.
                Set to a local path e.g. /tmp/jira_cache.db, copy the DB there
                first, then copy back after the run.
```

## Running from Host Mac (NFS workaround)
SQLite WAL mode is incompatible with NFS. When running outside Docker (host Mac),
copy the DB to /tmp first, set JIRA_DB_PATH, run, then sync back:
```bash
python3 -c "import shutil; shutil.copyfile('/Volumes/Apps/AgentZero/usr/skills/jira/data/jira_cache.db', '/tmp/jira_cache.db')"
export JIRA_DB_PATH=/tmp/jira_cache.db
python /Volumes/Apps/AgentZero/usr/skills/jira/scripts/jira.py
python3 -c "import shutil; shutil.copyfile('/tmp/jira_cache.db', '/Volumes/Apps/AgentZero/usr/skills/jira/data/jira_cache.db')"
```

## Arguments

| Argument | Required | Default | Description |
|---|---|---|---|
| `--jql` | No | currentUser() active tickets | JQL query string |
| `--filter-id` | No | - | Jira saved filter ID (numeric) |
| `--view-id` | No | - | Polaris view ID (numeric) |
| `--limit` | No | 200 | Max tickets to return |
| `--offset` | No | 0 | Pagination offset |
| `--cached-only` | No | false | Output cached summaries from DB without API calls |
| `--force` | No | false | Skip timestamp checks, force full fetch + re-summarize |
| `--output` | No | `workdir/jira-output.md` | Write results to file |
| `--no-cache` | No | false | Bypass JQL cache for view resolution |

## Output

The output `.md` file is **only created after successful completion** of all fetching and summarization. If any error occurs, no file is created. This prevents AI agents from reading incomplete results.

Progress and diagnostics go to **stdout** (no separate log file).

Output format per ticket:
```
---
[1/N] jira/DPD-645: Improve event sync to prevent overage
Relevance: 8/10 | Mention: direct
Source: jira | Key: DPD-645 | Status: IN RELEASE QUEUE (Done) | Priority: High | Assignee: Michael Bui
Work Items: DPD-645, DPD-273 | People: Nikhil Grover | Labels: event-sync, pricing-pipeline
blocks: DPD-273 | parent: DPD-644 | Last Updated: 2026-03-19T13:05:25+08:00
[AI summary with adaptive length based on relevance]
---
```

## Key Features

### Relevance Scoring (AI-driven)
Each ticket summary includes a 1-10 relevance score from the AI, guided by:
- `User.md` context (professional role, domain expertise, priorities)
- `mention_type` detection (direct/indirect/none)
- Relevance floors: direct >= 7, indirect >= 5, none >= 1
- Adaptive summary length: direct ~200 words, indirect ~100 words, none ~30 words

### Mention Type Detection
Automatically classifies each resource as `direct`, `indirect`, or `none`:
- **Direct**: assignee, reporter, author of comment, @mentioned, user participation (replied)
- **Indirect**: linked issues, same epic, watcher
- **None**: no user signal detected
- Strongest signal wins at resource level (1 direct mention in 20 comments = direct)

### Entity Extraction
AI extracts structured entities alongside the summary (stored in metadata JSON):
- `work_items`: Jira ticket IDs, PR numbers, project codenames, service names, git repos
- `people`: Explicit person names only (no groups, teams, distribution lists)
- `labels`: Exactly 5 AI-generated 2-word descriptive labels (lowercase, hyphenated)

### JSON Structured Output from LLM
Uses Qwen 3.5 native `response_format={"type": "json_object"}` for reliable structured responses. Regex fallback parser handles edge cases (think blocks, code fences).

## Architecture

### Database Schema
SQLite cache at `data/jira_cache.db` with three tables:
- `atomic_content`: Individual items (ticket descriptions, comments) with metadata JSON
- `resource_summary`: Per-resource summaries with `mention_type`, `estimated_relevance`, `final_relevance`, and metadata JSON (work_items, people, labels)
- `ticket_relationships`: Parent/child/linked ticket relationships

### Processing Pipeline
1. **Fetch**: Jira API -> format issues -> cache atomic content (timestamp-based skip for unchanged)
2. **Summarize** (concurrent thread): For new/changed resources, compute mention_type, call LLM with relevance-scoring prompt, parse JSON response, upsert summary with entities
3. **Output**: Only after all items complete, write sorted markdown to file

## Files
```
scripts/
  jira.py           - Single consolidated script (all logic)
  test_jira.py      - Comprehensive unit tests (126 tests)
data/
  jira_cache.db     - SQLite cache (persistent, auto-created)
_architecture.md    - Detailed design documentation
```

## Testing
```bash
cd /Volumes/Apps/AgentZero/usr/skills/jira/scripts
python test_jira.py
```
126 tests covering: text cleaning, ADF parsing, DB schema/migration/CRUD, mention type detection, relevance filtering, LLM response parsing (valid JSON, fallbacks, floor/ceiling), issue formatting, metadata building, caching, output formatting, pipeline (mocked LLM), and integration with real DB.
