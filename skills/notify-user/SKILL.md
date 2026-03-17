# Notify User Skill

## Description
Send notifications to the user via ntfy.sh service. This skill provides a simple way to push messages to the user's devices through the ntfy.sh notification system.

## Version
1.0.0

## Author
Agent Zero

## Tags
notification, alert, messaging, ntfy

## Usage

### Basic Usage
Use the provided Python script to send a notification message:

```bash
python /a0/usr/skills/notify-user/scripts/notify.py "Your message here"
```

### Parameters
| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `message` | Yes | — | The notification message to send |
| `--title` / `-t` | No | "Agent Zero Notification" | Title for the notification |
| `--priority` / `-p` | No | 3 | Priority level 1-5 |
| `--format` | No | `json` | Output format: `json` or `yaml` |

### Examples

1. Send a simple notification:
```bash
python /a0/usr/skills/notify-user/scripts/notify.py "Task completed successfully!"
```

2. Send a notification with custom title:
```bash
python /a0/usr/skills/notify-user/scripts/notify.py "Build finished" --title "Build Status"
```

3. Send a high-priority alert:
```bash
python /a0/usr/skills/notify-user/scripts/notify.py "Critical error detected!" --priority 5
```

## Configuration
The ntfy.sh endpoint is pre-configured to:
- URL: https://ntfy.sh/AgentZero-eHqWuKJQWSuKmXBE

## Procedures

### Sending a notification
1. Call the Python script with your message
2. The script will send an HTTP POST request to ntfy.sh
3. The notification will be delivered to all subscribed devices

## Files
- `scripts/notify.py` - Main notification script
