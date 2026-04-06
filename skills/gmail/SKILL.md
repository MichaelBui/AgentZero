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

### Disable early-stop for full scan
```bash
python /a0/usr/skills/gmail/scripts/gmail.py --early-stop 0
```

### Fast report from cache (no browser needed)
```bash
python /a0/usr/skills/gmail/scripts/gmail.py --cached-only
```

## Arguments
| Argument | Required | Default | Description |
|---|---|---|---|
| `--cdp-url` | No | `http://192.168.1.11:9223` | Chrome DevTools Protocol endpoint |
| `--days` | No | 3 | Days to look back |
| `--max-threads` | No | 200 | Max non-excluded threads to process |
| `--max-scan` | No | 500 | Max total threads to scan across all pages (safety cap) |
| `--early-stop` | No | 5 | Stop fetching after N consecutive cached threads; scan continues, output includes all (0=disabled) |
| `--min-relevance` | No | 7 | Minimum relevance score to include in output (1-10) |
| `--exclude-labels` | No | `["❌ ai-exclusion", ...]` | JSON array of labels to skip |
| `--priority-labels` | No | `["⚠️IMPORTANT", ...]` | JSON array of priority labels |
| `--cached-only` | No | false | Output cached summaries from DB without browser (fast, for reports) |
| `--force` | No | false | Bypass change detection, re-fetch and re-summarize all |
| `--refetch-since` | No | - | Re-fetch all threads cached on or after this date (YYYY-MM-DD) |
| `--output` | No | `workdir/gmail-output.md` | Write results to file (clean markdown for AI agents) |
| `--debug-log` | No | `workdir/gmail-debug.log` | Write debug/progress messages to file |

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
Source: gmail | Thread: 19ceb94ec915103d | Labels: Inbox, IMPORTANT | Priority: IMPORTANT | Senders: Jane Doe | Last Date: Mon, Mar 9, 2026, 3:30 PM | Last Updated: 2026-03-19T13:05:25+08:00
[AI-generated summary of thread]
```

`Last Updated` is the timestamp when the AI summary was last generated/refreshed.

Progress and diagnostics go to stderr. Use `PYTHONUNBUFFERED=1 python3 -u` for real-time streaming to file.

## Monitoring

The script writes status markers to the debug log (`workdir/gmail-debug.log`). Use these to determine if the job is running correctly:

- **Job started:** Look for `STATUS: STARTED` near the **top** of the log with a **recent timestamp** (within the last 5 minutes). If you do NOT see this, the job has not executed properly — wait up to 5 minutes or treat it as failed.
- **Job completed:** Look for `STATUS: COMPLETED` or `STATUS: COMPLETED WITH ERRORS` near the **bottom** of the log. The script is only considered done when one of these markers appears. A run with only `STATUS: STARTED` but no completion marker is still in progress or failed.
- **Job completed with errors:** `STATUS: COMPLETED WITH ERRORS` means the run finished but some threads failed AI summarization (transient API errors with retries exhausted). Most output is available; failed threads are listed in the log.
- **Job failed:** Look for `STATUS: FAILED` in the log, which includes the error message.

Progress messages use explicit phase labels — **fetching and summarization are two distinct phases**:
- `[Fetching X/Y]` — currently fetching this thread from Gmail via browser; **summarization is still pending**
- `[Fetched X/Y]` — fetched and cached, queued for AI summarization
- `[Fetch failed X/Y]` — thread could not be loaded (skipped, does not block other threads)
- `[Summarizing X/Y]` — AI is actively generating a summary for this thread
- `[Summarized X/Y]` — summary complete and written to output

**Important:** Seeing `[Fetched 128/128]` does NOT mean the job is done. Wait for `STATUS: COMPLETED` at the bottom.

## Architecture
- **Single-file design**: All logic (DB, cleaner, summarizer, CDP) in `scripts/gmail.py`
- **Two-phase extraction**: Phase 1 scans listing pages (URL-based pagination via `/pN`), Phase 2 fetches details by direct thread URL navigation
- **SPA race condition handling**: Active polling for correct `data-legacy-thread-id` after navigation, with 3-tier retry strategy
- SQLite cache at `data/gmail_cache.db` (persistent across sessions, thread-safe with `threading.Lock`)
- Output and debug logs written to `/a0/usr/workdir/` (transactional, per-session)
- Change detection via `data-legacy-last-non-draft-message-id` comparison at listing level
- Email bodies are immutable; only new messages in threads trigger re-caching
- Early-stop optimization: halts scanning after N consecutive cached threads
- **3-tier relevance scoring**: PERSONAL (7-10), ACTION-REQUIRED (6-8), INFORMATIONAL (5-7)
- AI summarization via LiteLLM proxy (configurable via `MAX_SUMMARY_WORDS` env var, default 500)
- **Cross-thread leakage prevention**: `has_message_anywhere()` guards against SPA DOM residue
- **Unicode date normalization**: Handles `\u202f` and other Unicode whitespace in Gmail dates
- See `_architecture.md` for detailed design with Mermaid diagrams and 25-point integrity checklist

## Files
```
scripts/gmail.py             - Single-file entry point (CDP + DB + cleaner + summarizer + output)
scripts/test_gmail.py        - Comprehensive test suite (90 tests, 212 subtests, 95% coverage)
Makefile                     - Test/coverage targets (make test, make coverage)
data/gmail_cache.db          - SQLite cache (persistent, auto-created)
_architecture.md             - Detailed design documentation
SKILL.md                     - This file (agent-facing)
# Transactional output written to /a0/usr/workdir/:
#   gmail-output.md          - Results output (overwritten each run)
#   gmail-debug.log          - Debug/progress log (overwritten each run)
```
