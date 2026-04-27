---
name: gchat
description: Read Google Chat conversations using a remote Chrome DevTools headless instance, cache messages in SQLite, and output AI-summarized compact results. Use when the user asks to check chat messages, read recent Google Chat threads, get chat conversations, or prepare a daily briefing. Supports DMs, group chats, and thread views.
version: 4.0.0
author: Michael
tags: [gchat, google-chat, chrome, cdp, devtools, conversations, messages, chat, summarize, cache]
---

# GChat Skill

## When to Use
- User asks to check or read recent Google Chat messages
- User wants chat conversation summaries for daily briefing
- User needs to review Google Chat DMs or group chats
- User asks about recent chat activity or correspondence

Do NOT use for: sending messages (read-only), Gmail emails (use gmail skill), Slack/Teams.

## Usage

### Default - read last 3 days, up to 200 conversations
```bash
python /a0/usr/skills/gchat/scripts/gchat.py
```

### Custom time window and conversation limit
```bash
python /a0/usr/skills/gchat/scripts/gchat.py --days 14 --max-threads 20
```

### Force re-fetch and re-summarize everything
```bash
python /a0/usr/skills/gchat/scripts/gchat.py --force
```

### Focus on specific conversation
```bash
python /a0/usr/skills/gchat/scripts/gchat.py --focus-title "DevOps"
```

### Disable early-stop for full scan
```bash
python /a0/usr/skills/gchat/scripts/gchat.py --early-stop 0
```

### Fast report from cache (no browser needed)
```bash
python /a0/usr/skills/gchat/scripts/gchat.py --cached-only
```

### Filter output by minimum relevance score
```bash
python /a0/usr/skills/gchat/scripts/gchat.py --min-relevance 8
```

## Arguments
| Argument | Required | Default | Description |
|---|---|---|---|
| `--cdp-url` | No | `http://192.168.1.11:9223` | Chrome DevTools Protocol endpoint |
| `--days` | No | 3 (Wed-Sat), 4 (Sun), 5 (Mon-Tue) | Days to look back (auto-detects to always cover 3 weekdays) |
| `--max-threads` | No | 200 | Max conversations to process |
| `--max-scan` | No | 500 | Max feed items to scan (safety cap) |
| `--max-scroll` | No | 5 | Max scroll-up iterations per thread |
| `--max-expansion` | No | 5 | Max expansion rounds for collapsed messages |
| `--early-stop` | No | 3 | Stop fetching after N consecutive unchanged convos (0=disabled) |
| `--focus-title` | No | *(none)* | Substring filter for conversation titles |
| `--cached-only` | No | false | Output cached summaries from DB without browser (fast, for reports) |
| `--force` | No | false | Bypass change detection, re-fetch and re-summarize all |
| `--output` | No | `workdir/gchat-output.md` | Write results to file |
| `--min-relevance` | No | 7 | Minimum relevance score for output (1-10) |
| `--debug-dom` | No | false | Dump Home feed DOM to stderr and exit |
| `--llm-context-limit` | No | 100000 | Max characters for LLM context (picks newest items that fit) |

## Output

The output `.md` file is **only created after successful completion** of all fetching and summarization. If any error occurs before completion, no output file is created. This prevents AI agents from reading incomplete results.

Conversations are ordered chronologically (most recent first). Relevance scoring is used for filtering (via `--min-relevance`), not ordering.

Output format per conversation:
```
## [1/6] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Relevance: 8/10 | Mention: direct | Messages: 3 | Work Items: Project Light | People: Michael Bui, Alvin Choo | Labels: architecture-review, team-coordination
[AI-generated summary of conversation]
```

Progress and diagnostics go to stderr.

## Monitoring

The script writes log messages to stderr. Key markers to look for:

- **Job started:** `STARTED (days=..., since=..., user=...)` near the top with a recent timestamp
- **Fetching progress:** `[Fetching X/Y] conversation_name` - currently loading this conversation from GChat via browser
- **Summarizing progress:** `Summarizing [X/Y] conversation_name (N msgs, mention_type)` - AI is generating a summary
- **Done:** `Done [X/Y] resource_id rel=N` - summary complete for one conversation
- **Job completed:** `COMPLETED (N conversations, fetched=M)` at the end of the log
- **Job completed with errors:** `COMPLETED WITH ERRORS (N conversations, M error(s))` - run finished but some conversations failed AI summarization
- **Job failed:** `FAILED: error message` - fatal error

**Important:** The output file is only written after ALL summarization completes. Individual `Done` messages do not mean the output is ready. Wait for `COMPLETED` before reading the output file.

## Relevance Scoring

Each conversation summary includes a 1-10 relevance score from the AI:
- **Direct personal conversations** (DMs, @mentions, personal discussions): 7-10
- **Action-required automated** (access requests, approval requests): 6-8
- **Informational automated** (alerts, monitoring, reports): 5-7
- **Indirect** (user not directly involved): 3-5
- **No involvement**: 1-4

## Handling Results
- Output file is at `--output` path (default: `workdir/gchat-output.md`)
- Conversations are ordered chronologically (most recent first)
- Each block includes: conversation name, group ID, AI summary, relevance score, mention type, work items, people, labels
- Use `--min-relevance` to filter noise (default 7 excludes most automated alerts)
- Use `--cached-only` for fast re-reads without browser
