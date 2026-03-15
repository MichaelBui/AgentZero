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
| Search tickets by JQL, project, status, assignee, labels, sprint | `jira_query.py` |
| Fetch tickets from a saved Jira filter (by numeric ID) | `jira_filter.py` |
| Fetch tickets from a Polaris/board view (by numeric view ID) | `jira_view.py` |

Do NOT use for: creating/updating tickets, fetching non-NTUC Jira instances.

## Required Environment Variables
```
JIRA_EMAIL    - michael.bui@fairpricegroup.sg
JIRA_API_KEY  - loaded via secrets (never log full value)
API_KEY_OTHER - LiteLLM proxy authentication (set via Terraform, or LITELLM_API_KEY)
```

## Usage

### Default - current user's active tickets
```bash
python /a0/usr/skills/jira/scripts/jira_query.py
```

### Query by JQL
```bash
python /a0/usr/skills/jira/scripts/jira_query.py --jql 'project = DPD AND status = "In Progress"'
```

### Fetch from a saved filter
```bash
python /a0/usr/skills/jira/scripts/jira_filter.py --filter-id 13811
```

### Fetch from a Polaris view
```bash
python /a0/usr/skills/jira/scripts/jira_view.py --viewId 10489904
```

### Force full re-fetch and re-summarize
```bash
python /a0/usr/skills/jira/scripts/jira_query.py --force
```

### Pagination
```bash
python /a0/usr/skills/jira/scripts/jira_query.py --jql 'project = DPD' --limit 20 --offset 0
```

## Arguments (all scripts)

| Argument | Required | Default | Description |
|---|---|---|---|
| `--jql` | No (query) | currentUser() active tickets | JQL query string |
| `--filter-id` | Yes (filter) | - | Jira saved filter ID (numeric) |
| `--viewId` | Yes (view) | - | Polaris view ID (numeric) |
| `--limit` | No | 50 | Max tickets to return |
| `--offset` | No | 0 | Pagination offset |
| `--force` | No | false | Skip timestamp checks, force full fetch + re-summarize |
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
- SQLite cache at `data/jira_cache.db` (per-ticket + per-comment caching)
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
  jira_common.py      - Core: auth, ADF parsing, formatting, caching, summarization, output
  jira_db.py          - Self-contained SQLite DB (SkillDB class)
  jira_cleaner.py     - Self-contained text cleanup for Jira content
  jira_summarizer.py  - Self-contained LLM summarization via LiteLLM proxy
  jira_query.py       - Entry point: raw JQL query
  jira_filter.py      - Entry point: saved filter by ID
  jira_view.py        - Entry point: Polaris view by ID
data/
  jira_cache.db       - SQLite cache (auto-created)
_architecture.md      - Detailed design documentation
```
