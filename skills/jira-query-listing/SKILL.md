---
name: jira-query-listing
description: Fetch Jira tickets using a raw JQL query. Use when the user asks to search for tickets by JQL, project, status, assignee, labels, sprint, or any Jira search criteria. Returns full issue details including hierarchy, links, and comments.
version: 1.1.0
author: Michael
tags: [jira, jql, search, tickets, query, backlog, sprint, ntuclink]
---

# Jira Query Listing Skill

## When to Use
Use this skill when:
- User asks to search or query Jira tickets using JQL
- User wants tickets filtered by project, status, assignee, label, sprint, etc.
- User provides a JQL string or describes search criteria that translate to JQL
- User wants to look up specific tickets by key (e.g., DPD-383)

Do NOT use for: fetching from Polaris views (use `jira-view-listing` instead), creating/updating tickets.

## Required Environment Variables
```
JIRA_EMAIL    — michael.bui@fairpricegroup.sg
JIRA_API_KEY  — loaded via `load_jira_api_key` in terminal (never log full value)
```

## Usage

### Basic — raw JQL query
```bash
python /a0/usr/skills/jira-query-listing/scripts/jira_query_listing.py --jql 'project = DPD AND status = "In Progress" ORDER BY updated DESC'
```

### Fetch specific ticket(s) by key
```bash
python /a0/usr/skills/jira-query-listing/scripts/jira_query_listing.py --jql 'key in (DPD-383, DPD-700)'
```

### With pagination
```bash
python /a0/usr/skills/jira-query-listing/scripts/jira_query_listing.py --jql 'project = DPD' --limit=20 --offset=0
```

### Custom fields selection
```bash
python /a0/usr/skills/jira-query-listing/scripts/jira_query_listing.py --jql 'project = DPD' --fields 'summary,status,assignee,priority,labels'
```

### Pipe to jq for filtering
```bash
python /a0/usr/skills/jira-query-listing/scripts/jira_query_listing.py --jql 'project = DPD' | jq '.[] | {key, title, status: .status.name}'
```

## Arguments
| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--jql` | Yes | — | JQL query string |
| `--limit` | No | 50 | Max tickets to return |
| `--offset` | No | 0 | Pagination offset |
| `--fields` | No | (all standard) | Comma-separated Jira field names |
| `--format` | No | `json` | Output format: `json` or `yaml` |

## Output
- **stdout:** JSON (default) or YAML array of issue objects (pipe-friendly)
- **stderr:** Progress info, API key validation, errors

### Output fields per ticket
```json
{
  "key": "DPD-383",
  "id": "12345",
  "title": "Ticket summary",
  "description": "Plain text extracted from ADF",
  "status": { "name": "In Progress", "category": "Indeterminate" },
  "assignee": "Jane Doe",
  "priority": "High",
  "labels": ["backend", "deposit"],
  "parent": { "key": "DPD-100", "summary": "Parent title" },
  "subtasks": [{ "key": "DPD-384", "summary": "Subtask title" }],
  "links": [{ "type": "blocks", "key": "DPD-500" }],
  "created": "2024-01-01T00:00:00.000+0000",
  "updated": "2024-01-15T00:00:00.000+0000",
  "comments": [
    {
      "created": "2024-01-10T00:00:00.000+0000",
      "author": "Jane Doe",
      "body": "Comment text"
    }
  ]
}
```

## Notes
- Jira instance: `ntuclink.atlassian.net`
- See `scripts/jira_query_listing.py` for implementation details.

## Files
- `scripts/jira_query_listing.py` — Main script
