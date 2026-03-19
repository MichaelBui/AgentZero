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
Source: jira | Key: DPD-645 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-12 | Resolution: Done | blocks: DPD-273 | parent: DPD-644
[AI-generated summary: current status, decisions, pending actions, key dates, blockers]
---
```

Progress and diagnostics go to stderr.

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
