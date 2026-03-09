#!/usr/bin/env python3
"""
Jira Query Listing Tool
=======================
Fetches tickets from Jira using a raw JQL query via REST API v3.
Output: JSON array to stdout. Progress/debug to stderr.

Simpler than jira-view-listing: no GraphQL/Polaris resolution needed.
Takes JQL directly, returns fully formatted issue details.
"""

import argparse
import base64
import json
import os
import sys
import time

import requests

JIRA_BASE = "https://ntuclink.atlassian.net"
SEARCH_URL = f"{JIRA_BASE}/rest/api/3/search/jql"

DEFAULT_FIELDS = "summary,description,status,parent,issuelinks,created,updated,comment,subtasks,assignee,priority,labels"


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_auth_header(email: str, api_key: str) -> dict:
    token = base64.b64encode(f"{email}:{api_key}".encode()).decode()
    return {"Authorization": f"Basic {token}"}


def validate_env() -> tuple[str, str]:
    email = os.environ.get("JIRA_EMAIL")
    api_key = os.environ.get("JIRA_API_KEY")
    if not email:
        eprint("ERROR: Missing required env var: JIRA_EMAIL")
        sys.exit(1)
    if not api_key:
        eprint("ERROR: Missing required env var: JIRA_API_KEY")
        sys.exit(1)
    masked = f"{api_key[:3]}...{api_key[-3:]} (Length: {len(api_key)})"
    eprint(f"API Key detected: {masked}")
    eprint(f"Email: {email}")
    return email, api_key


def request_with_retry(method: str, url: str, max_retries: int = 3, **kwargs) -> requests.Response:
    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.request(method, url, timeout=30, **kwargs)
            if resp.status_code == 401:
                eprint("ERROR: Authentication failed. Check JIRA_EMAIL and JIRA_API_KEY.")
                sys.exit(1)
            if resp.status_code == 404:
                eprint(f"ERROR: Resource not found at {url}")
                sys.exit(1)
            return resp
        except requests.exceptions.Timeout:
            wait = 2 ** attempt
            eprint(f"Timeout on attempt {attempt}/{max_retries}. Retrying in {wait}s...")
            if attempt < max_retries:
                time.sleep(wait)
            else:
                eprint("ERROR: All retry attempts timed out.")
                sys.exit(1)
        except requests.exceptions.ConnectionError as e:
            eprint(f"ERROR: Connection error: {e}")
            sys.exit(1)


def fetch_issues(jql: str, limit: int, offset: int, fields: str, headers: dict) -> tuple[list[dict], int]:
    """Fetch issues via Jira REST API v3. Returns (issues, total)."""
    params = {
        "jql": jql,
        "maxResults": limit,
        "startAt": offset,
        "fields": fields,
    }
    eprint(f"JQL: {jql}")
    eprint(f"Fetching issues (limit={limit}, offset={offset})...")
    resp = request_with_retry("GET", SEARCH_URL, headers=headers, params=params)
    if resp.status_code == 400:
        error_messages = resp.json().get("errorMessages", [])
        eprint(f"ERROR: Invalid JQL — {'; '.join(error_messages)}")
        sys.exit(1)
    if resp.status_code != 200:
        eprint(f"ERROR: Search API returned {resp.status_code}: {resp.text}")
        sys.exit(1)
    data = resp.json()
    total = data.get("total", 0)
    issues = data.get("issues", [])
    eprint(f"Found {total} total tickets, fetched {len(issues)}")
    return issues, total


def adf_to_text(node) -> str:
    """Recursively extract plain text from Atlassian Document Format (ADF) JSON."""
    if node is None:
        return ""
    if isinstance(node, str):
        return node
    if isinstance(node, dict):
        node_type = node.get("type", "")
        if node_type == "text":
            return node.get("text", "")
        if node_type == "hardBreak":
            return "\n"
        content = node.get("content", [])
        text = "".join(adf_to_text(c) for c in content)
        if node_type in ("paragraph", "heading", "bulletList", "orderedList", "listItem", "blockquote"):
            return text + "\n"
        return text
    if isinstance(node, list):
        return "".join(adf_to_text(c) for c in node)
    return ""


def extract_comments(comment_field: dict, max_comments: int = 10) -> list[dict]:
    """Extract last N comments sorted by created date desc."""
    comments = comment_field.get("comments", []) if comment_field else []
    sorted_comments = sorted(comments, key=lambda c: c.get("created", ""), reverse=True)
    result = []
    for c in sorted_comments[:max_comments]:
        body_raw = c.get("body")
        body_text = adf_to_text(body_raw) if isinstance(body_raw, dict) else (body_raw or "")
        result.append({
            "created": c.get("created"),
            "updated": c.get("updated"),
            "author": c.get("author", {}).get("displayName"),
            "body": body_text.strip(),
        })
    return result


def extract_links(issuelinks: list) -> list[dict]:
    """Extract linked issues with type and key."""
    links = []
    for link in (issuelinks or []):
        link_type = link.get("type", {}).get("name", "relates to")
        if "inwardIssue" in link:
            links.append({"type": link_type, "key": link["inwardIssue"]["key"]})
        if "outwardIssue" in link:
            links.append({"type": link_type, "key": link["outwardIssue"]["key"]})
    return links


def format_issue(issue: dict) -> dict:
    fields = issue.get("fields", {})
    description_raw = fields.get("description")
    description = (
        adf_to_text(description_raw).strip()
        if isinstance(description_raw, dict)
        else (description_raw or "")
    )
    status = fields.get("status", {})
    parent = fields.get("parent")
    subtasks = fields.get("subtasks", []) or []
    assignee = fields.get("assignee")
    priority = fields.get("priority")

    return {
        "key": issue.get("key"),
        "id": issue.get("id"),
        "title": fields.get("summary"),
        "description": description,
        "status": {
            "name": status.get("name"),
            "category": status.get("statusCategory", {}).get("name"),
        },
        "assignee": assignee.get("displayName") if assignee else None,
        "priority": priority.get("name") if priority else None,
        "labels": fields.get("labels", []),
        "parent": {
            "key": parent["key"],
            "summary": parent.get("fields", {}).get("summary"),
        } if parent else None,
        "subtasks": [
            {"key": s["key"], "summary": s.get("fields", {}).get("summary")}
            for s in subtasks
        ],
        "links": extract_links(fields.get("issuelinks")),
        "created": fields.get("created"),
        "updated": fields.get("updated"),
        "comments": extract_comments(fields.get("comment")),
    }


def output_data(data, fmt: str = "json"):
    """Output data as JSON (default) or YAML to stdout."""
    if fmt == "yaml":
        import yaml
        print(yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False))
    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description="Fetch Jira tickets using a raw JQL query")
    parser.add_argument("--jql", required=True, help="JQL query string")
    parser.add_argument("--format", choices=["json", "yaml"], default="json", help="Output format (default: json)")
    parser.add_argument("--limit", type=int, default=50, help="Max tickets (default: 50)")
    parser.add_argument("--offset", type=int, default=0, help="Pagination offset (default: 0)")
    parser.add_argument("--fields", default=DEFAULT_FIELDS, help="Comma-separated Jira field names")
    args = parser.parse_args()

    email, api_key = validate_env()
    auth_headers = get_auth_header(email, api_key)

    issues, total = fetch_issues(args.jql, args.limit, args.offset, args.fields, auth_headers)
    formatted = [format_issue(issue) for issue in issues]

    output_data(formatted, args.format)


if __name__ == "__main__":
    main()
