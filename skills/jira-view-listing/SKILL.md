---
name: jira-view-listing
description: Fetch Jira tickets from a Polaris View (Jira Product Discovery / Roadmaps). Use when the user asks about team initiatives, backlog items, roadmap tickets, sprint tasks, or anything in a specific Jira view. Resolves the view's dynamic JQL and returns full issue details including hierarchy, links, and comments.
version: 1.0.0
author: Michael
tags: [jira, polaris, roadmap, initiatives, backlog, tickets, product-discovery, ntuclink]
---

# Jira View Listing Skill

## When to Use
Use this skill when:
- User asks what tickets are in a Jira view, board, or roadmap
- User wants to review team initiatives, backlog, or sprint items
- User needs ticket hierarchy (parent/subtasks), links, or comments from Jira
- User references a Jira view ID or wants to see what's in a specific Polaris view

Do NOT use for: creating tickets, updating tickets, managing sprints — this skill is read-only.

## Required Environment Variables
```
JIRA_EMAIL    — your Jira login email (e.g., michael@ntuclink.com)
JIRA_API_KEY  — Jira API key (never log full value)
```

These must be set in the project's `secrets.env` or the global `secrets.env`.

## Usage

### Basic — fetch from a Polaris view
```bash
python /a0/usr/skills/jira-view-listing/scripts/jira_view_listing.py --viewId=10489904
```

### With pagination
```bash
python /a0/usr/skills/jira-view-listing/scripts/jira_view_listing.py --viewId=10489904 --limit=20 --offset=0
```

### Pipe to jq for filtering
```bash
python /a0/usr/skills/jira-view-listing/scripts/jira_view_listing.py --viewId=10489904 | jq '.[] | {key, title, status: .status.name}'
```

## Arguments
| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--viewId` | Yes | — | Numeric Polaris view ID |
| `--limit` | No | 50 | Max tickets to return |
| `--offset` | No | 0 | Pagination offset |
| `--no-cache` | No | false | Bypass 24h JQL cache, re-resolve from GraphQL |

## Output
- **stdout:** JSON array of issue objects (pipe-friendly)
- **stderr:** Progress info, API key validation, errors

### Output fields per ticket
```json
{
  "key": "OMNI-1",
  "id": "12345",
  "title": "Ticket summary",
  "description": "Plain text extracted from ADF",
  "status": { "name": "In Progress", "category": "Indeterminate" },
  "parent": { "key": "OMNI-0", "summary": "Parent title" },
  "subtasks": [{ "key": "OMNI-2", "summary": "Subtask title" }],
  "links": [{ "type": "blocks", "key": "OMNI-5" }],
  "created": "2024-01-01T00:00:00.000+0000",
  "updated": "2024-01-15T00:00:00.000+0000",
  "comments": [
    {
      "created": "2024-01-10T00:00:00.000+0000",
      "updated": "2024-01-10T00:00:00.000+0000",
      "author": "Jane Doe",
      "body": "Comment text"
    }
  ]
}
```

## Notes
- Jira instance: `ntuclink.atlassian.net`
- JQL is cached per view ID for 24 hours. Use `--no-cache` to force refresh.
- See `scripts/jira_view_listing.py` for implementation details.

## Files
- `scripts/jira_view_listing.py` — Main script
