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

### Default - read last 3 days, up to 50 conversations
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

## Arguments
| Argument | Required | Default | Description |
|---|---|---|---|
| `--cdp-url` | No | `http://192.168.1.11:9223` | Chrome DevTools Protocol endpoint |
| `--days` | No | 3 | Days to look back |
| `--max-threads` | No | 50 | Max conversations to process |
| `--max-scan` | No | 100 | Max feed items to scan (safety cap) |
| `--max-scroll` | No | 5 | Max scroll-up iterations per thread |
| `--max-expansion` | No | 5 | Max expansion rounds for collapsed messages |
| `--early-stop` | No | 3 | Stop after N consecutive unchanged convos or cached messages (0=disabled) |
| `--focus-title` | No | *(none)* | Substring filter for conversation titles |
| `--force` | No | false | Bypass change detection, re-fetch and re-summarize all |
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
Source: gchat | Group: dm/abc123 | Messages: 20 | Last Activity: 2026-03-15T12:30:00+00:00
[AI-generated summary - main conversation, no topic_id]

## gchat/space/AAAALHoAh6U/e2Tne49XGSA: Feature flag management
Source: gchat | Group: space/AAAALHoAh6U/e2Tne49XGSA | Messages: 5 | Last Activity: 2026-03-15T10:00:00+00:00
[AI-generated summary - thread-specific, resource_id = group_id/topic_id]
```

Progress and diagnostics go to stderr. Use `PYTHONUNBUFFERED=1 python3 -u` for real-time streaming to file.

## Architecture
- Self-contained: all modules (DB, cleaner, summarizer) embedded in `scripts/`
- SQLite cache at `data/gchat_cache.db` (per-message caching)
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
data/gchat_cache.db          - SQLite cache (auto-created)
_architecture.md             - Detailed design documentation
```
