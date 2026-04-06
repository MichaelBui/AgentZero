---
name: jira
description: Fetch Jira tickets with SQLite caching, AI-driven relevance scoring, and structured summarization. Supports raw JQL query, saved filter by ID, or Polaris view. Outputs relevance-scored markdown summaries with mention detection, entity extraction, and adaptive detail levels. Use when the user asks to search, list, or summarize Jira tickets.
version: 4.0.0
author: Michael
tags: [jira, jql, search, tickets, query, filter, view, polaris, backlog, sprint, ntuclink, summarize, cache, relevance]
---

# Jira Skill

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
