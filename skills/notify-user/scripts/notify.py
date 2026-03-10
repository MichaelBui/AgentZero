#!/usr/bin/env python3
"""
Notify User Script
Sends notifications via ntfy.sh service
"""

import argparse
import json
import sys
try:
    import requests
except ImportError:
    print("Error: requests library not found. Install with: pip install requests", file=sys.stderr)
    sys.exit(1)

# ntfy.sh endpoint
NTFY_URL = "https://ntfy.sh/AgentZero-eHqWuKJQWSuKmXBE"

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def send_notification(message: str, title: str = "Agent Zero Notification", priority: int = 3) -> dict:
    """Send a notification via ntfy.sh. Returns result dict."""
    result = {"success": False, "title": title, "priority": priority, "message": message}
    try:
        headers = {
            "Title": title,
            "Priority": str(priority)
        }
        
        response = requests.post(
            NTFY_URL,
            data=message.encode('utf-8'),
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            eprint("Notification sent successfully")
            result["success"] = True
        else:
            result["error"] = f"HTTP {response.status_code}: {response.text}"
            eprint(f"Failed to send notification: {result['error']}")
            
    except requests.exceptions.Timeout:
        result["error"] = "Request timed out"
        eprint(result["error"])
    except requests.exceptions.ConnectionError:
        result["error"] = "Could not connect to ntfy.sh"
        eprint(result["error"])
    except Exception as e:
        result["error"] = str(e)
        eprint(f"Error: {e}")

    return result


def output_data(data, fmt: str = "json"):
    """Output data as JSON (default) or YAML to stdout."""
    if fmt == "yaml":
        import yaml
        print(yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False))
    else:
        print(json.dumps(data, separators=(",", ":"), ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(
        description="Send notifications via ntfy.sh"
    )
    parser.add_argument(
        "message",
        help="The notification message to send"
    )
    parser.add_argument(
        "--title", "-t",
        default="Agent Zero Notification",
        help="Title for the notification (default: 'Agent Zero Notification')"
    )
    parser.add_argument(
        "--priority", "-p",
        type=int,
        default=3,
        choices=[1, 2, 3, 4, 5],
        help="Priority level 1-5 (default: 3)"
    )
    parser.add_argument(
        "--format", choices=["json", "yaml"], default="json",
        help="Output format (default: json)"
    )
    
    args = parser.parse_args()
    
    result = send_notification(
        message=args.message,
        title=args.title,
        priority=args.priority
    )
    
    output_data(result, args.format)
    sys.exit(0 if result["success"] else 1)

if __name__ == "__main__":
    main()
