---
name: gmail
description: Read Gmail email threads using a remote Chrome DevTools headless instance, cache messages in SQLite, and output AI-summarized compact results. Use when the user asks to check emails, read recent threads, get email conversations, or prepare a daily briefing. Supports label-based exclusion and priority tagging.
version: 3.0.0
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

## Prerequisites
- Running Chrome/Chromium instance with remote debugging at `192.168.1.11:9223`
- Active Gmail session in Chrome (already logged in)
- `playwright` Python package installed
- `API_KEY_OTHER` or `LLAMA_TOKEN` environment variable set for LLM summarization

## Usage

### Default - read last 3 days, up to 50 threads
```bash
python /a0/usr/skills/gmail/scripts/gmail_reader.py
```

### Custom time window and thread limit
```bash
python /a0/usr/skills/gmail/scripts/gmail_reader.py --days 14 --max-threads 50
```

### Force re-fetch and re-summarize everything
```bash
python /a0/usr/skills/gmail/scripts/gmail_reader.py --force
```

### Disable early-stop for full scan
```bash
python /a0/usr/skills/gmail/scripts/gmail_reader.py --early-stop 0
```

## Arguments
| Argument | Required | Default | Description |
|---|---|---|---|
| `--cdp-url` | No | `http://192.168.1.11:9223` | Chrome DevTools Protocol endpoint |
| `--days` | No | 3 | Days to look back |
| `--max-threads` | No | 50 | Max non-excluded threads to process |
| `--max-scan` | No | 100 | Max total threads to scan across all pages (safety cap) |
| `--early-stop` | No | 5 | Stop after N consecutive cached threads (0=disabled) |
| `--exclude-labels` | No | `["❌ ai-exclusion", ...]` | JSON array of labels to skip |
| `--priority-labels` | No | `["⚠️IMPORTANT", ...]` | JSON array of priority labels |
| `--force` | No | false | Bypass change detection, re-fetch and re-summarize all |

## Environment Variables
| Variable | Required | Default | Purpose |
|---|---|---|---|
| `API_KEY_OTHER` / `LLAMA_TOKEN` | Yes | - | LiteLLM proxy auth (set via Terraform) |
| `LITELLM_BASE_URL` | No | `https://llm.gigary.com/v1` | LiteLLM proxy endpoint |
| `SUMMARIZE_MODEL` | No | `local/qwen3.5-35b-a3b:instruct-reasoning` | LLM model for summarization |
| `MAX_SUMMARY_WORDS` | No | `500` | Max words per summary |

## Output

Streams text blocks per thread to stdout:
```
## gmail/19ceb94ec915103d: Re: Project update
Source: gmail | Thread: 19ceb94ec915103d | Labels: Inbox, IMPORTANT | Priority: IMPORTANT | Senders: Jane Doe | Last Date: Mon, Mar 9, 2026, 3:30 PM
[AI-generated summary of thread]
```

Progress and diagnostics go to stderr. Use `PYTHONUNBUFFERED=1 python3 -u` for real-time streaming to file.

## Architecture
- **Two-phase extraction**: Phase 1 scans listing pages (URL-based pagination via `/pN`), Phase 2 fetches details by direct thread URL navigation
- Self-contained: all modules (DB, cleaner, summarizer) embedded in `scripts/`
- SQLite cache at `data/gmail_cache.db` (per-message caching)
- Change detection via `data-legacy-last-non-draft-message-id` comparison at listing level
- Email bodies are immutable; only new messages in threads trigger re-caching
- Early-stop optimization: halts scanning after N consecutive cached threads
- AI summarization via LiteLLM proxy (configurable via `MAX_SUMMARY_WORDS` env var, default 500)
- See `_architecture.md` for detailed design with Mermaid diagrams

## Files
```
scripts/gmail_reader.py      - Main script (CDP + caching + summarization)
scripts/gmail_db.py          - SQLite database management
scripts/gmail_cleaner.py     - Email body cleanup (deterministic)
scripts/gmail_summarizer.py  - LLM summarization via LiteLLM
data/gmail_cache.db          - SQLite cache (auto-created)
_architecture.md             - Detailed design documentation
```
