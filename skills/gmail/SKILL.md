---
name: gmail
description: Read Gmail email threads using a remote Chrome DevTools headless instance, cache messages in SQLite, and output AI-summarized compact results. Use when the user asks to check emails, read recent threads, get email conversations, or prepare a daily briefing. Supports label-based exclusion and priority tagging.
version: 3.2.0
author: Michael
tags: [gmail, email, chrome, cdp, devtools, inbox, threads, conversations, summarize, cache]
---

# Gmail Skill

## When to Use
- User asks to check or read recent emails
- User wants email thread summaries for daily briefing
- User needs to review inbox or specific email threads
- User asks about recent correspondence or email activity

Do NOT use for: sending emails (read-only), calendar events, non-Gmail providers.

## Usage

### Default - read last 3 days, up to 200 threads
```bash
python /a0/usr/skills/gmail/scripts/gmail.py
```

### Custom time window and thread limit
```bash
python /a0/usr/skills/gmail/scripts/gmail.py --days 14 --max-threads 100
```

### Force re-fetch and re-summarize everything
```bash
python /a0/usr/skills/gmail/scripts/gmail.py --force
```

### Re-fetch threads since a specific date
```bash
python /a0/usr/skills/gmail/scripts/gmail.py --refetch-since 2026-04-01
```

### Disable early-stop for full scan
```bash
python /a0/usr/skills/gmail/scripts/gmail.py --early-stop 0
```

### Fast report from cache (no browser needed)
```bash
python /a0/usr/skills/gmail/scripts/gmail.py --cached-only
```

### Filter output by minimum relevance score
```bash
python /a0/usr/skills/gmail/scripts/gmail.py --min-relevance 8
```

## Arguments
| Argument | Required | Default | Description |
|---|---|---|---|
| `--cdp-url` | No | `http://192.168.1.11:9223` | Chrome DevTools Protocol endpoint |
| `--days` | No | 3 (Wed-Sat), 4 (Sun), 5 (Mon-Tue) | Days to look back (auto-detects to always cover 3 weekdays) |
| `--max-threads` | No | 200 | Max non-excluded threads to process |
| `--max-scan` | No | 500 | Max total threads to scan across all pages (safety cap) |
| `--early-stop` | No | 5 | Stop fetching after N consecutive cached threads (0=disabled) |
| `--min-relevance` | No | 7 | Minimum relevance score to include in output (1-10) |
| `--exclude-labels` | No | `["❌ ai-exclusion", ...]` | JSON array of labels to skip |
| `--cached-only` | No | false | Output cached summaries from DB without browser (fast, for reports) |
| `--force` | No | false | Bypass change detection, re-fetch and re-summarize all |
| `--refetch-since` | No | - | Re-fetch all threads cached on or after this date (YYYY-MM-DD) |
| `--output` | No | `workdir/gmail-output.md` | Write results to file |
| `--log-level` | No | INFO | Log level (DEBUG for diagnostics) |

## Output

The output `.md` file is **only created after successful completion** of all fetching and summarization. If any error occurs before completion, no output file is created. This prevents AI agents from reading incomplete results.

Threads are ordered chronologically (most recent first). Relevance scoring is used for filtering (via `--min-relevance`), not ordering.

Output format per thread:
```
## gmail/19ceb94ec915103d: Re: Project update
Source: gmail | Thread: 19ceb94ec915103d | Labels: Inbox, IMPORTANT | Senders: Jane Doe | Last Date: Mon, Mar 9, 2026, 3:30 PM | Last Updated: 2026-03-19T13:05:25+08:00
[AI-generated summary of thread]
```

`Last Updated` is the timestamp when the AI summary was last generated/refreshed.

Progress and diagnostics go to stderr.

## Monitoring

The script writes log messages to stderr. Key markers to look for:

- **Job started:** `STARTED (days=..., since=..., user=...)` near the top with a recent timestamp
- **Fetching progress:** `[Fetching X/Y] subject...` - currently loading this thread from Gmail via browser
- **Summarizing progress:** `Summarizing [X/Y] subject... (N msgs, mention_type)` - AI is generating a summary
- **Job completed:** `COMPLETED (N threads, fetched=M)` at the end of the log
- **Job completed with errors:** `COMPLETED WITH ERRORS (N threads, M error(s))` - run finished but some threads failed AI summarization
- **Job failed:** `FAILED: error message` - fatal error

**Important:** The output file is only written after ALL summarization completes. Individual `Summarizing` messages do not mean the output is ready. Wait for `COMPLETED` before reading the output file.

## Relevance Scoring

Each thread summary includes a 1-10 relevance score from the AI:
- **Direct personal emails** (human wrote to user): 7-10
- **Action-required automated** (access requests, calendar invites): 6-8
- **Informational automated** (reports, notifications): 5-7
- **Indirect** (user in CC): 5-7
- **No involvement**: 1-4

## Handling Results
- Output file is at `--output` path (default: `workdir/gmail-output.md`)
- Threads are ordered chronologically (most recent first)
- Each thread block includes: subject, labels, senders, AI summary, relevance score, mention type
- Use `--min-relevance` to filter noise (default 7 excludes most automated emails)
- Use `--cached-only` for fast re-reads without browser
