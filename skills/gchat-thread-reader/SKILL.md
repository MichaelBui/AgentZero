---
name: gchat-thread-reader
description: Read Google Chat conversations using a remote Chrome DevTools headless instance. Use when the user asks to check chat messages, read recent Google Chat threads, get chat conversations, or review Google Chat activity. Connects to a running Chrome instance via CDP and extracts who said what and when from each conversation. Supports DMs and group chats.
version: 1.4.0
author: Michael
tags: [gchat, google-chat, chrome, cdp, devtools, conversations, messages, chat]
---

# Google Chat Thread Reader Skill

## When to Use
Use this skill when:
- User asks to check or read recent Google Chat messages
- User wants chat conversations (who said what, when)
- User needs to review Google Chat DMs or group chats
- User asks about recent chat activity or correspondence on Google Chat

Do NOT use for:
- Sending chat messages (this is read-only)
- Gmail emails (use gmail-thread-reader)
- Google Spaces threaded discussions (future support)
- Non-Google chat providers (Slack, Teams, etc.)

## Prerequisites
- A running Chrome/Chromium instance with remote debugging enabled
- The Chrome instance must have an active Google Chat session (already logged in)
- Google Chat must be in **2-panel view** (settings: "Right panel opens conversations")
- `playwright` Python package installed (`pip install playwright`)

## How It Works (Flow)
1. Navigate to `chat.google.com/app/home` (Home feed, sorted by recency)
2. Extract Home feed items (`span[role="listitem"]` with `data-group-id`)
3. Filter conversations with `data-display-timestamp` within `--days` cutoff
4. For each conversation (up to `--max-threads`):
   - Click the Home feed item to open in the **right panel** (2-panel view)
   - **Guardrail check**: verify left panel (Home feed) is still visible — if gone, the click navigated away from 2-panel layout and the item is skipped
   - Wait for message containers to load
   - **Scroll right panel to bottom** first (GChat may jump to first unread, which can be far back)
   - **Scroll right panel up** until the `--days` cutoff is reached
   - Expand collapsed "Show more"/"See more" sections (does NOT click "N replies" thread navigators)
   - Extract all messages within date range (sender, timestamp, body, quoted text)
5. Output all conversations as minified JSON to stdout

## Usage

### Basic — read last 3 days (default)
```bash
python /a0/usr/skills/gchat-thread-reader/scripts/gchat_thread_reader.py
```

### Read last 7 days, up to 10 conversations
```bash
python /a0/usr/skills/gchat-thread-reader/scripts/gchat_thread_reader.py --days 7 --max-threads 10
```

### Custom Chrome endpoint
```bash
python /a0/usr/skills/gchat-thread-reader/scripts/gchat_thread_reader.py --cdp-url http://192.168.1.11:9223 --days 5
```

### Debug DOM structure (when selectors break)
```bash
python /a0/usr/skills/gchat-thread-reader/scripts/gchat_thread_reader.py --debug-dom
```

## Arguments
| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--cdp-url` | No | `http://192.168.1.11:9223` | Chrome DevTools Protocol endpoint |
| `--days` | No | 3 | Number of days to look back |
| `--max-threads` | No | 20 | Max conversations to read |
| `--max-scan` | No | 100 | Max total Home feed items to scan. Safety cap |
| `--max-scroll` | No | 20 | Max scroll-up iterations per thread to load older messages |
| `--max-expansion` | No | 5 | Max expansion rounds for collapsed message bars (handles lazy loading) |
| `--focus-title` | No | *(none)* | Substring filter — only process conversations whose title contains this string (case-insensitive) |
| `--format` | No | `json` | Output format: `json` or `yaml` |
| `--debug-dom` | No | false | Dump Home feed DOM structure to stderr for selector debugging |

## Output
- **stdout:** Minified JSON (default) or YAML array of conversation objects (pipe-friendly)
- **stderr:** Progress info, connection status, diagnostics, errors

### Output fields per conversation
```json
{
  "name": "Nikhil Grover",
  "url": "https://chat.google.com/dm/xxxxx",
  "message_count": 20,
  "messages": [
    {
      "sender": "Nikhil Grover",
      "timestamp": "2:33 PM",
      "epoch_ms": 1773153237567,
      "body": "Message text content..."
    }
  ]
}
```

### Fields per message
| Field | Description |
|-------|-------------|
| `sender` | Sender name (person or "App Name, App" for bots) |
| `timestamp` | Display timestamp as shown in GChat UI |
| `epoch_ms` | Epoch milliseconds from `data-absolute-timestamp` (threads) or `data-local-sort-time-msec` (main conversations) |
| `body` | Full text body including rich content, URLs, monitor queries. Quoted text prefixed with `[quoted]`. Truncated at 5KB. |

## Notes
- Default Chrome endpoint: `192.168.1.11:9223` (Michael's homelab headless Chrome)
- The Chrome instance must already be logged into Google Chat
- **2-panel view required**: GChat must be configured for conversations to open in the right panel
- **Right panel scrolling**: The script scrolls the rightmost scrollable container (the conversation panel), NOT the Home feed panel
- **Left-panel guardrail**: After clicking a feed item, the script verifies the Home feed panel is still visible. If the click accidentally navigated away from the 2-panel layout (wrong element clicked), it returns to Home and skips the item
- **No thread navigation**: The script does NOT click "N replies" thread indicators — those navigate to a separate thread view. Only genuine "Show more"/"See more" buttons are expanded
- Google Chat's DOM is heavily obfuscated; use `--debug-dom` when selectors break after UI updates
- **Fail-loud:** If 0 feed items are found within date range, exits with code 2 and FATAL error
- **Scan safety cap:** `--max-scan` (default 100) limits total Home feed items examined
- **Scroll depth control:** `--max-scroll` (default 20) limits scroll-up iterations per thread. Use lower values (1-3) for quick scans, higher for full history
- Uses Playwright native clicks (not JS `.click()`) for reliable GChat framework interaction
- ~5-15s per conversation with `--max-scroll 1`, ~20-40s with high scroll depth
- Bot/app messages include full rich content (monitor tags, queries, URLs, button text)

## Files
- `scripts/gchat_thread_reader.py` — Main script
