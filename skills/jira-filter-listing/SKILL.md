---
name: jira-filter-listing
description: Fetch Jira tickets from a saved filter by filter ID. Use when the user asks to list tickets from a Jira filter, board filter, or references a filter number/ID. Resolves the filter's JQL and returns full issue details in JSON or YAML.
version: 1.1.0
author: Michael
tags: [jira, filter, saved-search, tickets, listing, board, ntuclink]
---

# Jira Filter Listing Skill

## When to Use
Use this skill when:
- User asks to list tickets from a Jira filter by ID (e.g., filter 13811)
- User wants a quick board-like table view of filter results
- User references a saved Jira filter or wants to see what's in a specific filter

Do NOT use for:
- Raw JQL queries (use `jira-query-listing` instead)
- Polaris views (use `jira-view-listing` instead)
- Creating/updating tickets or filters

## Required Environment Variables
```
JIRA_EMAIL    — michael.bui@fairpricegroup.sg
JIRA_API_KEY  — loaded via `load_jira_api_key` in terminal (never log full value)
```

## Usage

### Basic — fetch from a saved filter (JSON output, default)
```bash
python /a0/usr/skills/jira-filter-listing/scripts/jira_filter_listing.py --filter-id 13811
```

### YAML output
```bash
python /a0/usr/skills/jira-filter-listing/scripts/jira_filter_listing.py --filter-id 13811 --format yaml
```

### With pagination
```bash
python /a0/usr/skills/jira-filter-listing/scripts/jira_filter_listing.py --filter-id 13811 --limit 20 --offset 0
```

### Pipe to jq for filtering
```bash
python /a0/usr/skills/jira-filter-listing/scripts/jira_filter_listing.py --filter-id 13811 | jq '.[] | {key, title, status}'
```

## Arguments
| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--filter-id` | Yes | — | Jira saved filter ID (numeric) |
| `--format` | No | `json` | Output format: `json` or `yaml` |
| `--limit` | No | 50 | Max tickets to return |
| `--offset` | No | 0 | Pagination offset |

## Output
- **stdout:** JSON (default) or YAML array of issue objects (pipe-friendly)
- **stderr:** Progress info, API key validation, errors

Same structure as `jira-query-listing` output — full issue objects with hierarchy, links, and comments.

## Notes
- Jira instance: `ntuclink.atlassian.net`
- Filter endpoint: `GET /rest/api/3/filter/{id}` resolves the saved JQL, then executes it via search API.
- See `scripts/jira_filter_listing.py` for implementation details.

## Files
- `scripts/jira_filter_listing.py` — Main script
