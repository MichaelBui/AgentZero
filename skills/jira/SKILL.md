---
name: jira
description: Fetch Jira tickets with SQLite caching and AI summarization. Supports three modes - raw JQL query, saved filter by ID, or Polaris view. Always outputs compact text summaries with source, key, metadata, and AI summary. Use when the user asks to search, list, or summarize Jira tickets by JQL, project, status, assignee, labels, sprint, filter, or board view.
version: 3.0.0
author: Michael
tags: [jira, jql, search, tickets, query, filter, view, polaris, backlog, sprint, ntuclink, summarize, cache]
---

# Jira Skill

Unified Jira skill replacing `jira-query-listing`, `jira-filter-listing`, and `jira-view-listing`. All modes share a single SQLite cache with incremental fetching, timestamp-based skip, relationship tracking, and AI summarization. Self-contained - no external shared modules.

## When to Use

| User Intent | Script |
|---|---|
| Any combination of JQL, filter, and/or view (preferred) | `jira_reader.py` |
| Search tickets by JQL only | `jira_query.py` |
| Fetch tickets from a saved Jira filter only | `jira_filter.py` |
| Fetch tickets from a Polaris/board view only | `jira_view.py` |

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
python /Volumes/Apps/AgentZero/usr/skills/jira/scripts/jira_query.py
python3 -c "import shutil; shutil.copyfile('/tmp/jira_cache.db', '/Volumes/Apps/AgentZero/usr/skills/jira/data/jira_cache.db')"
```

## Usage

### Unified reader (preferred)
```bash
python /a0/usr/skills/jira/scripts/jira_reader.py --jql 'project = DPD AND status = "In Progress"'
python /a0/usr/skills/jira/scripts/jira_reader.py --filter-id 13811
python /a0/usr/skills/jira/scripts/jira_reader.py --view-id 10489904
python /a0/usr/skills/jira/scripts/jira_reader.py --jql '...' --filter-id 13811 --view-id 10489904
python /a0/usr/skills/jira/scripts/jira_reader.py --cached-only
```

### Default - current user's active tickets
```bash
python /a0/usr/skills/jira/scripts/jira_reader.py
```

### Force full re-fetch and re-summarize
```bash
python /a0/usr/skills/jira/scripts/jira_reader.py --force
```

### Pagination
```bash
python /a0/usr/skills/jira/scripts/jira_reader.py --jql 'project = DPD' --limit 20 --offset 0
```

### Fast report from cache (no API calls needed)
```bash
python /a0/usr/skills/jira/scripts/jira_reader.py --cached-only
```

## Arguments (all scripts)

| Argument | Required | Default | Description |
|---|---|---|---|
| `--jql` | No (query) | currentUser() active tickets | JQL query string |
| `--filter-id` | Yes (filter) | - | Jira saved filter ID (numeric) |
| `--view-id` | Yes (view) | - | Polaris view ID (numeric) |
| `--limit` | No | 200 | Max tickets to return |
| `--offset` | No | 0 | Pagination offset |
| `--cached-only` | No | false | Output cached summaries from DB without API calls (fast, for reports) |
| `--force` | No | false | Skip timestamp checks, force full fetch + re-summarize |
| `--output` | No | `workdir/jira-output.md` | Write results to file (clean markdown for AI agents) |
| `--debug-log` | No | `workdir/jira-debug.log` | Write debug/progress messages to file |
| `--no-cache` | No (view) | false | Bypass JQL cache for view resolution |

## Output

Text blocks to stdout, one per ticket:

```
---
jira/DPD-645: Improve event sync to prevent overage
Source: jira | Key: DPD-645 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-12 | Resolution: Done | blocks: DPD-273 | parent: DPD-644 | Last Updated: 2026-03-19T13:05:25+08:00
[AI-generated summary: current status, decisions, pending actions, key dates, blockers]
---
```

`Last Updated` is the timestamp when the AI summary was last generated/refreshed.

Progress and diagnostics go to stderr.

## Monitoring

The script writes status markers to the debug log (`workdir/jira-debug.log`). Use these to determine if the job is running correctly:

- **Job started:** Look for `STATUS: STARTED` near the **top** of the log with a **recent timestamp** (within the last 5 minutes). If you do NOT see this, the job has not executed properly — wait up to 5 minutes or treat it as failed.
- **Job completed:** Look for `STATUS: COMPLETED` or `STATUS: COMPLETED WITH ERRORS` near the **bottom** of the log. The script is only considered done when one of these markers appears. A run with only `STATUS: STARTED` but no completion marker is still in progress or failed.
- **Job completed with errors:** `STATUS: COMPLETED WITH ERRORS` means the run finished but some tickets failed AI summarization (e.g. transient API errors). Those tickets will appear in the output with their cached or empty summary. The error list is shown in the log.
- **Job failed:** Look for `STATUS: FAILED` in the log, which includes the error message.

Progress messages use explicit phase labels — **fetching and summarization are two distinct phases**:
- `[Fetching X/Y]` — currently fetching ticket data from the Jira API; **summarization is still pending**
- `[Fetched X/Y]: unchanged - summarization pending` — cached, no new data; still pending summarization
- `[Fetched X/Y]: queued for summarization` — newly fetched and cached; queued for AI summarization
- `[Summarizing X/Y]` — AI is actively generating a summary for this ticket
- `[Summarized X/Y]` — summary complete and written to output

**Important:** Seeing `[Fetched 76/76]` does NOT mean the job is done. Wait for `STATUS: COMPLETED` at the bottom.

## Architecture
- SQLite cache at `data/jira_cache.db` (persistent across sessions)
- Output and debug logs written to `/a0/usr/workdir/` (transactional, per-session)
- Timestamp-based skip: compares API `updated` field vs cached - skips unchanged tickets entirely
- Full content preserved in cache (no truncation); AI summarization handles size reduction
- 500 word max per summary (configurable via `MAX_SUMMARY_WORDS` env var)
- Incremental summarization: existing summary + only new/changed items sent to LLM
- Relationship tracking (parent/child/linked tickets) in `ticket_relationships` table
- Rich metadata: status, issuetype, priority, assignee, reporter, resolution, duedate, labels, components, fix_versions
- See `_architecture.md` for detailed design with Mermaid diagrams

## Files
```
scripts/
  jira_reader.py      - Unified entry point: JQL + filter + view (preferred)
  jira_common.py      - Core: auth, ADF parsing, formatting, caching, summarization, output
  jira_db.py          - Self-contained SQLite DB (SkillDB class)
  jira_cleaner.py     - Self-contained text cleanup for Jira content
  jira_summarizer.py  - Self-contained LLM summarization via LiteLLM proxy
  jira_query.py       - Entry point: raw JQL query
  jira_filter.py      - Entry point: saved filter by ID
  jira_view.py        - Entry point: Polaris view by ID
data/
  jira_cache.db              - SQLite cache (persistent, auto-created)
_architecture.md             - Detailed design documentation
# Transactional output written to /a0/usr/workdir/:
#   jira-output.md           - Results output (overwritten each run)
#   jira-debug.log           - Debug/progress log (overwritten each run)
```
