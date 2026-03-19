---
name: gchat
description: Read Google Chat conversations using a remote Chrome DevTools headless instance, cache messages in SQLite, and output AI-summarized compact results. Use when the user asks to check chat messages, read recent Google Chat threads, get chat conversations, or prepare a daily briefing. Supports DMs, group chats, and thread views.
version: 3.0.0
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

## Prerequisites
- Running Chrome/Chromium instance with remote debugging at `192.168.1.11:9223`
- Active Google Chat session in Chrome (already logged in)
- Google Chat must be in **3-panel view** (nav left, feed middle, conversation right)
- `playwright` Python package installed
- `API_KEY_OTHER` or `LLAMA_TOKEN` environment variable set for LLM summarization

## Usage

### Default - read last 3 days, up to 200 conversations
```bash
python /a0/usr/skills/gchat/scripts/gchat_reader.py
```

### Custom time window and conversation limit
```bash
python /a0/usr/skills/gchat/scripts/gchat_reader.py --days 14 --max-threads 20
```

### Force re-fetch and re-summarize everything
```bash
python /a0/usr/skills/gchat/scripts/gchat_reader.py --force
```

### Focus on specific conversation
```bash
python /a0/usr/skills/gchat/scripts/gchat_reader.py --focus-title "DevOps"
```

### Disable early-stop for full scan
```bash
python /a0/usr/skills/gchat/scripts/gchat_reader.py --early-stop 0
```

### Fast report from cache (no browser needed)
```bash
python /a0/usr/skills/gchat/scripts/gchat_reader.py --cached-only
```

## Arguments
| Argument | Required | Default | Description |
|---|---|---|---|
| `--cdp-url` | No | `http://192.168.1.11:9223` | Chrome DevTools Protocol endpoint |
| `--days` | No | 3 | Days to look back |
| `--max-threads` | No | 200 | Max conversations to process |
| `--max-scan` | No | 500 | Max feed items to scan (safety cap) |
| `--max-scroll` | No | 5 | Max scroll-up iterations per thread |
| `--max-expansion` | No | 5 | Max expansion rounds for collapsed messages |
| `--early-stop` | No | 3 | Stop fetching after N consecutive unchanged convos; scan continues, output includes all (0=disabled) |
| `--focus-title` | No | *(none)* | Substring filter for conversation titles |
| `--cached-only` | No | false | Output cached summaries from DB without browser (fast, for reports) |
| `--force` | No | false | Bypass change detection, re-fetch and re-summarize all |
| `--output` | No | `workdir/gchat-output.md` | Write results to file (clean markdown for AI agents) |
| `--debug-log` | No | `workdir/gchat-debug.log` | Write debug/progress messages to file |
| `--debug-dom` | No | false | Dump Home feed DOM to stderr and exit |

## Environment Variables
| Variable | Required | Default | Purpose |
|---|---|---|---|
| `API_KEY_OTHER` / `LLAMA_TOKEN` | Yes | - | LiteLLM proxy auth (set via Terraform) |
| `LITELLM_BASE_URL` | No | `https://llm.gigary.com/v1` | LiteLLM proxy endpoint |
| `SUMMARIZE_MODEL` | No | `local/qwen3.5-35b-a3b:instruct-reasoning` | LLM model for summarization |
| `MAX_SUMMARY_WORDS` | No | `500` | Max words per summary |

## Output

Streams text blocks per conversation to stdout:
```
## gchat/dm/abc123: Nikhil Grover
Source: gchat | Group: dm/abc123 | Messages: 20 | Last Activity: 2026-03-15T12:30:00+08:00 | Last Updated: 2026-03-19T13:05:25+08:00
[AI-generated summary - main conversation, no topic_id]

## gchat/space/AAAALHoAh6U/e2Tne49XGSA: Feature flag management
Source: gchat | Group: space/AAAALHoAh6U/e2Tne49XGSA | Messages: 5 | Last Activity: 2026-03-15T10:00:00+08:00 | Last Updated: 2026-03-19T13:05:25+08:00
[AI-generated summary - thread-specific, resource_id = group_id/topic_id]
```

`Last Activity` is the feed's last message timestamp. `Last Updated` is when the AI summary was last generated/refreshed.

Progress and diagnostics go to stderr. Use `PYTHONUNBUFFERED=1 python3 -u` for real-time streaming to file.

## Monitoring

The script writes status markers to the debug log (`workdir/gchat-debug.log`). Use these to determine if the job is running correctly:

- **Job started:** Look for `STATUS: STARTED` near the **top** of the log with a **recent timestamp** (within the last 5 minutes). If you do NOT see this, the job has not executed properly — wait up to 5 minutes or treat it as failed.
- **Job completed:** Look for `STATUS: COMPLETED` or `STATUS: COMPLETED WITH ERRORS` near the **bottom** of the log. The script is only considered done when one of these markers appears. A run with only `STATUS: STARTED` but no completion marker is still in progress or failed.
- **Job completed with errors:** `STATUS: COMPLETED WITH ERRORS` means the run finished but some conversations failed AI summarization (transient API errors with retries exhausted). Most output is available; failed conversations are listed in the log.
- **Job failed:** Look for `STATUS: FAILED` in the log, which includes the error message.

Progress messages use explicit phase labels — **fetching and summarization are two distinct phases**:
- `[Fetching X/Y]` — currently fetching this conversation from GChat via browser; **summarization is still pending**
- `[Fetched X/Y]` — fetched and cached, queued for AI summarization
- `[Fetch skipped X/Y]` — skipped (unchanged timestamp or focus filter); still queued for summarization
- `[Fetch failed X/Y]` — error during fetch (DOM not found, panel lost, 0 messages); skipped
- `[Summarizing X/Y]` — AI is actively generating a summary for this conversation
- `[Summarized X/Y]` — summary complete and written to output

**Important:** Seeing `[Fetched 77/77]` does NOT mean the job is done. Wait for `STATUS: COMPLETED` at the bottom.

## Architecture
- Self-contained: all modules (DB, cleaner, summarizer) embedded in `scripts/`
- SQLite cache at `data/gchat_cache.db` (persistent across sessions)
- Output and debug logs written to `/a0/usr/workdir/` (transactional, per-session)
- `resource_id`: `{group_id}/{topic_id}` for thread-specific items, `{group_id}` for main conversations
- 3-panel layout navigation: nav (left), Home feed (middle), conversation (right)
- Change detection via `data-display-timestamp` comparison at feed level
- Progressive message collection handles virtual scrolling (dedup by data_id)
- Early-stop optimization: halts scanning after N consecutive unchanged conversations or cached messages during scroll
- AI summarization via LiteLLM proxy (configurable via `MAX_SUMMARY_WORDS` env var, default 500)
- See `_architecture.md` for detailed design with Mermaid diagrams

## Files
```
scripts/gchat_reader.py      - Main script (CDP + caching + summarization)
scripts/gchat_db.py          - SQLite database management
scripts/gchat_cleaner.py     - Chat message cleanup (deterministic)
scripts/gchat_summarizer.py  - LLM summarization via LiteLLM
data/gchat_cache.db          - SQLite cache (persistent, auto-created)
_architecture.md             - Detailed design documentation
# Transactional output written to /a0/usr/workdir/:
#   gchat-output.md          - Results output (overwritten each run)
#   gchat-debug.log          - Debug/progress log (overwritten each run)
```
