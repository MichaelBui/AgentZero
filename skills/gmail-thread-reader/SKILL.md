---
name: gmail-thread-reader
description: Read Gmail email threads using a remote Chrome DevTools headless instance. Use when the user asks to check emails, read recent email threads, get email conversations, or review inbox messages. Connects to a running Chrome instance via CDP and extracts who said what and when from each thread. Supports label-based exclusion and priority tagging.
version: 1.2.0
author: Michael
tags: [gmail, email, chrome, cdp, devtools, inbox, threads, conversations]
---

# Gmail Thread Reader Skill

## When to Use
Use this skill when:
- User asks to check or read recent emails
- User wants email thread conversations (who said what, when)
- User needs to review inbox or specific email threads
- User asks about recent correspondence or email activity

Do NOT use for:
- Sending emails (this is read-only)
- Calendar events (use a calendar skill)
- Non-Gmail email providers

## Prerequisites
- A running Chrome/Chromium instance with remote debugging enabled
- The Chrome instance must have an active Gmail session (already logged in)
- `playwright` Python package installed (`pip install playwright`)

## Usage

### Basic — read last 3 days (default)
```bash
python /a0/usr/skills/gmail-thread-reader/scripts/gmail_thread_reader.py
```

### Read last 7 days, up to 10 threads
```bash
python /a0/usr/skills/gmail-thread-reader/scripts/gmail_thread_reader.py --days 7 --max-threads 10
```

### Custom Chrome endpoint
```bash
python /a0/usr/skills/gmail-thread-reader/scripts/gmail_thread_reader.py --cdp-url http://192.168.1.11:9223 --days 5
```

### Custom exclusion labels
```bash
python /a0/usr/skills/gmail-thread-reader/scripts/gmail_thread_reader.py --exclude-labels '["❌ ai-exclusion", "Promotions"]'
```

### Custom priority labels
```bash
python /a0/usr/skills/gmail-thread-reader/scripts/gmail_thread_reader.py --priority-labels '["⚠️IMPORTANT", "❗️ ASAP  🏃‍♂️‍➡️", "🔜 Soon 🚶‍♂️‍➡️"]'
```

## Arguments
| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--cdp-url` | No | `http://192.168.1.11:9223` | Chrome DevTools Protocol endpoint |
| `--days` | No | 3 | Number of days to look back |
| `--max-threads` | No | 20 | Max non-excluded threads to read |
| `--exclude-labels` | No | `["❌ ai-exclusion"]` | JSON array of labels to skip |
| `--priority-labels` | No | `["⚠️IMPORTANT", ...]` | JSON array of priority labels (highest first) |
| `--format` | No | `json` | Output format: `json` or `yaml` |

## Label-Based Filtering

### Exclusion Labels
Threads with any label in `--exclude-labels` are completely skipped. The `--max-threads` count only applies to non-excluded threads, so the script continues scanning until the target count is reached.

### Priority Labels
Each thread is tagged with its highest-matching priority label (first match from the priority list wins). Priority appears as a `priority` field in the output — `null` if no priority label matches.

**Default priority order (highest to lowest):**
1. `⚠️IMPORTANT`
2. `❗️ ASAP  🏃‍♂️‍➡️`
3. `🔜 Soon 🚶‍♂️‍➡️`
4. `👀 KIV 🧘‍♂️`
5. `📝 Noted`

## Output
- **stdout:** JSON (default) or YAML array of thread objects (pipe-friendly)
- **stderr:** Progress info, connection status, skip/exclusion logs, errors

### Output fields per thread
```json
{
  "subject": "Re: Project update",
  "thread_url": "https://mail.google.com/mail/u/0/#search/.../FMfcg...",
  "labels": ["Inbox", "⚠️IMPORTANT"],
  "priority": "⚠️IMPORTANT",
  "senders": [
    { "name": "Jane Doe", "email": "jane@example.com" }
  ],
  "last_date": "Mon, Mar 9, 2026, 3:30 PM",
  "messages": [
    {
      "from": "Jane Doe <jane@example.com>",
      "to": [
        { "name": "me", "email": "michael.bui@fairpricegroup.sg" },
        { "name": "Bob", "email": "bob@example.com" }
      ],
      "cc": [
        { "name": "Alice", "email": "alice@example.com" }
      ],
      "date": "Mar 9, 2026, 3:30 PM",
      "body": "Message text content..."
    }
  ]
}
```

### Fields per message
| Field | Description |
|-------|-------------|
| `from` | Sender name and email |
| `to` | List of To recipients (name + email) |
| `cc` | List of CC recipients (name + email, if header expanded) |
| `date` | Full date and time |
| `body` | Plain text body (images/attachments ignored, truncated at 5KB) |

## Notes
- Default Chrome endpoint: `192.168.1.11:9223` (Michael's homelab headless Chrome)
- The Chrome instance must already be logged into Gmail
- CC extraction requires Gmail's "show details" header to be expandable; falls back to empty list
- ~6-7 seconds per thread (navigation + extraction + back)
- See `scripts/gmail_thread_reader.py` for implementation details

## Files
- `scripts/gmail_thread_reader.py` — Main script
