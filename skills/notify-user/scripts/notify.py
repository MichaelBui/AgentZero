#!/usr/bin/env python3
"""
Notify User Script
Sends notifications via ntfy.sh service
"""

import argparse
import sys
try:
    import requests
except ImportError:
    print("Error: requests library not found. Install with: pip install requests")
    sys.exit(1)

# ntfy.sh endpoint
NTFY_URL = "https://ntfy.sh/AgentZero-eHqWuKJQWSuKmXBE"

def send_notification(message: str, title: str = "Agent Zero Notification", priority: int = 3) -> bool:
    """
    Send a notification via ntfy.sh
    
    Args:
        message: The notification message
        title: Title for the notification
        priority: Priority level (1-5)
    
    Returns:
        True if successful, False otherwise
    """
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
            print(f"✓ Notification sent successfully!")
            return True
        else:
            print(f"✗ Failed to send notification. Status: {response.status_code}")
            print(f"  Response: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        print("✗ Error: Request timed out")
        return False
    except requests.exceptions.ConnectionError:
        print("✗ Error: Could not connect to ntfy.sh")
        return False
    except Exception as e:
        print(f"✗ Error sending notification: {e}")
        return False

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
    
    args = parser.parse_args()
    
    success = send_notification(
        message=args.message,
        title=args.title,
        priority=args.priority
    )
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
