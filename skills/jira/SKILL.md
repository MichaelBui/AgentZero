---
name: jira
description: Fetch Jira tickets with SQLite caching, AI-driven relevance scoring, and structured summarization. Supports raw JQL query, saved filter by ID, or Polaris view. Outputs relevance-scored markdown summaries with mention detection, entity extraction, and adaptive detail levels. Use when the user asks to search, list, or summarize Jira tickets.
version: 4.0.0
author: Michael
tags: [jira, jql, search, tickets, query, filter, view, polaris, backlog, sprint, ntuclink, summarize, cache, relevance]
---

# Jira Skill

## When to Use
- User asks to search, list, or summarize Jira tickets
- User wants ticket summaries for daily briefing
- User needs to review active tickets, sprint backlogs, or saved filters
- User asks about recent Jira activity or ticket status

Do NOT use for: creating/updating tickets, fetching non-NTUC Jira instances.

## Usage

### Default - current user's active tickets
```bash
python /a0/usr/skills/jira/scripts/jira.py
```

### Fetch from saved filter and/or Polaris view
```bash
python /a0/usr/skills/jira/scripts/jira.py --filter-id 13811 --view-id 10489904
```

### Search tickets by JQL
```bash
python /a0/usr/skills/jira/scripts/jira.py --jql 'project = DPD AND status = "In Progress"'
```

### Any combination of JQL, filter, and view
```bash
python /a0/usr/skills/jira/scripts/jira.py --jql '...' --filter-id N --view-id N
```

### Force re-fetch and re-summarize everything
```bash
python /a0/usr/skills/jira/scripts/jira.py --force
```

### Fast report from cache (no API calls)
```bash
python /a0/usr/skills/jira/scripts/jira.py --cached-only
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

Tickets are ordered chronologically (most recently updated first). Relevance scoring is used for filtering, not ordering.

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

## Monitoring

The script writes progress to stdout. Key markers to look for:

- **Fetching progress:** `[Fetching X/Y]` - currently loading tickets from Jira API
- **Summarizing progress:** `Summarizing [X/Y]` - AI is generating a summary for a ticket
- **Job completed:** `COMPLETED (N tickets, fetched=M)` at the end
- **Job completed with errors:** `COMPLETED WITH ERRORS (N tickets, M error(s))` - run finished but some tickets failed AI summarization
- **Job failed:** `FAILED: error message` - fatal error

**Important:** The output file is only written after ALL summarization completes. Wait for `COMPLETED` before reading the output file.

## Relevance Scoring

Each ticket summary includes a 1-10 relevance score from the AI, guided by:
- `User.md` context (professional role, domain expertise, priorities)
- `mention_type` detection (direct/indirect/none)
- Relevance floors: direct >= 7, indirect >= 5, none >= 1
- Adaptive summary length: direct ~200 words, indirect ~100 words, none ~30 words

## Mention Type Detection

Automatically classifies each resource as `direct`, `indirect`, or `none`:
- **Direct**: assignee, reporter, author of comment, @mentioned, user participation (replied)
- **Indirect**: linked issues, same epic, watcher
- **None**: no user signal detected
- Strongest signal wins at resource level (1 direct mention in 20 comments = direct)

## Handling Results
- Output file is at `--output` path (default: `workdir/jira-output.md`)
- Tickets are ordered chronologically (most recently updated first)
- Each ticket block includes: key, status, priority, assignee, AI summary, relevance score, mention type, work items, people, labels, relationships
- Use `--cached-only` for fast re-reads without API calls
