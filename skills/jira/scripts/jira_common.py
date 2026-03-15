"""
Shared Jira logic for all Jira skill entry points.

Provides: authentication, ADF parsing, issue formatting with full metadata,
caching via SQLite, incremental fetching, content cleanup, and AI summarization.
"""

import base64
import json
import os
import sys
import time
from pathlib import Path
from typing import Optional

import requests

from jira_db import get_jira_db as _get_jira_db, SkillDB
from jira_cleaner import clean_jira_text
from jira_summarizer import summarize_resource

JIRA_BASE = "https://ntuclink.atlassian.net"
SEARCH_URL = f"{JIRA_BASE}/rest/api/3/search/jql"
DEFAULT_FIELDS = (
    "summary,description,status,parent,issuelinks,created,updated,comment,"
    "subtasks,assignee,priority,labels,duedate,reporter,issuetype,resolution,"
    "components,fixVersions"
)

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "jira_cache.db"


def eprint(*a, **kw):
    print(*a, file=sys.stderr, **kw)


# ── Authentication ──────────────────────────────────────────────────

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


def get_auth_header(email: str, api_key: str) -> dict:
    token = base64.b64encode(f"{email}:{api_key}".encode()).decode()
    return {"Authorization": f"Basic {token}"}


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


# ── ADF Parsing ─────────────────────────────────────────────────────

def adf_to_text(node) -> str:
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


# ── Issue Fetching ──────────────────────────────────────────────────

def fetch_issues(jql: str, limit: int, offset: int, headers: dict,
                 fields: str = DEFAULT_FIELDS) -> tuple[list[dict], int]:
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
    total = max(total, len(issues))
    eprint(f"Found {total} total tickets, fetched {len(issues)}")
    return issues, total


# ── Issue Formatting ────────────────────────────────────────────────

def format_issue(issue: dict) -> dict:
    """Extract and clean essential fields from a raw Jira issue, including full metadata."""
    fields = issue.get("fields", {})
    description_raw = fields.get("description")
    description = (
        adf_to_text(description_raw).strip()
        if isinstance(description_raw, dict)
        else (description_raw or "")
    )
    description = clean_jira_text(description)

    status = fields.get("status", {})
    parent = fields.get("parent")
    subtasks = fields.get("subtasks", []) or []
    assignee = fields.get("assignee")
    reporter = fields.get("reporter")
    priority = fields.get("priority")
    issuetype = fields.get("issuetype")
    resolution = fields.get("resolution")
    components = fields.get("components", []) or []
    fix_versions = fields.get("fixVersions", []) or []

    comments_raw = fields.get("comment", {})
    comments = _extract_comments(comments_raw)
    links = _extract_links(fields.get("issuelinks"))

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
        "reporter": reporter.get("displayName") if reporter else None,
        "priority": priority.get("name") if priority else None,
        "issuetype": issuetype.get("name") if issuetype else None,
        "resolution": resolution.get("name") if resolution else None,
        "components": [c.get("name") for c in components if c.get("name")],
        "fix_versions": [v.get("name") for v in fix_versions if v.get("name")],
        "labels": fields.get("labels", []),
        "duedate": fields.get("duedate"),
        "parent": {
            "key": parent["key"],
            "summary": parent.get("fields", {}).get("summary"),
        } if parent else None,
        "subtasks": [
            {"key": s["key"], "summary": s.get("fields", {}).get("summary")}
            for s in subtasks
        ],
        "links": links,
        "created": fields.get("created"),
        "updated": fields.get("updated"),
        "comments": comments,
    }


def _extract_comments(comment_field: dict, max_comments: int = 10) -> list[dict]:
    comments = comment_field.get("comments", []) if comment_field else []
    sorted_comments = sorted(comments, key=lambda c: c.get("created", ""), reverse=True)
    result = []
    for c in sorted_comments[:max_comments]:
        body_raw = c.get("body")
        body_text = adf_to_text(body_raw) if isinstance(body_raw, dict) else (body_raw or "")
        body_text = clean_jira_text(body_text)
        result.append({
            "id": c.get("id"),
            "created": c.get("created"),
            "updated": c.get("updated"),
            "author": c.get("author", {}).get("displayName"),
            "body": body_text,
        })
    return result


def _extract_links(issuelinks: list) -> list[dict]:
    links = []
    for link in (issuelinks or []):
        link_type = link.get("type", {}).get("name", "relates to")
        if "inwardIssue" in link:
            links.append({"type": link_type, "key": link["inwardIssue"]["key"]})
        if "outwardIssue" in link:
            links.append({"type": link_type, "key": link["outwardIssue"]["key"]})
    return links


# ── Metadata Builder ────────────────────────────────────────────────

def _build_ticket_metadata(issue: dict) -> dict:
    """Build comprehensive metadata dict from a formatted issue."""
    meta = {
        "status": issue["status"]["name"],
        "status_category": issue["status"]["category"],
        "assignee": issue.get("assignee"),
        "reporter": issue.get("reporter"),
        "priority": issue.get("priority"),
        "issuetype": issue.get("issuetype"),
        "resolution": issue.get("resolution"),
        "duedate": issue.get("duedate"),
        "labels": issue.get("labels", []),
        "components": issue.get("components", []),
        "fix_versions": issue.get("fix_versions", []),
    }
    if issue.get("parent"):
        meta["parent_key"] = issue["parent"]["key"]
        meta["parent_summary"] = issue["parent"].get("summary")
    if issue.get("subtasks"):
        meta["subtask_keys"] = [s["key"] for s in issue["subtasks"]]
    if issue.get("links"):
        meta["linked_issues"] = [
            {"type": l["type"], "key": l["key"]} for l in issue["links"]
        ]
    return meta


# ── Caching ─────────────────────────────────────────────────────────

def get_jira_db() -> SkillDB:
    return _get_jira_db(DB_PATH)


def issue_needs_fetch(db: SkillDB, issue_key: str, api_updated: str) -> bool:
    """Check if an issue needs full processing based on timestamp from API listing."""
    return db.has_content_changed(issue_key, api_updated)


def cache_issue(db: SkillDB, issue: dict) -> bool:
    """Cache a formatted issue and its comments. Returns True if any content changed."""
    key = issue["key"]
    changed = False

    ticket_content_parts = [f"Title: {issue['title']}"]
    ticket_content_parts.append(f"Status: {issue['status']['name']} ({issue['status']['category']})")
    if issue.get("issuetype"):
        ticket_content_parts.append(f"Type: {issue['issuetype']}")
    if issue.get("assignee"):
        ticket_content_parts.append(f"Assignee: {issue['assignee']}")
    if issue.get("reporter"):
        ticket_content_parts.append(f"Reporter: {issue['reporter']}")
    if issue.get("priority"):
        ticket_content_parts.append(f"Priority: {issue['priority']}")
    if issue.get("resolution"):
        ticket_content_parts.append(f"Resolution: {issue['resolution']}")
    if issue.get("duedate"):
        ticket_content_parts.append(f"Due: {issue['duedate']}")
    if issue.get("labels"):
        ticket_content_parts.append(f"Labels: {', '.join(issue['labels'])}")
    if issue.get("components"):
        ticket_content_parts.append(f"Components: {', '.join(issue['components'])}")
    if issue.get("fix_versions"):
        ticket_content_parts.append(f"Fix Versions: {', '.join(issue['fix_versions'])}")
    if issue.get("parent"):
        ticket_content_parts.append(f"Parent: {issue['parent']['key']} - {issue['parent'].get('summary', '')}")
    if issue.get("subtasks"):
        for s in issue["subtasks"]:
            ticket_content_parts.append(f"Subtask: {s['key']} - {s.get('summary', '')}")
    if issue.get("links"):
        for l in issue["links"]:
            ticket_content_parts.append(f"Link ({l['type']}): {l['key']}")
    if issue.get("description"):
        ticket_content_parts.append(f"\nDescription:\n{issue['description']}")

    ticket_content = "\n".join(ticket_content_parts)
    meta = _build_ticket_metadata(issue)

    if db.upsert_atomic(
        "jira", key, key,
        author=issue.get("reporter") or issue.get("assignee") or "Unknown",
        content=ticket_content,
        created_at=issue.get("created", ""),
        updated_at=issue.get("updated", ""),
        metadata=meta,
    ):
        changed = True

    for comment in issue.get("comments", []):
        cid = comment.get("id") or comment.get("created", "")
        if db.upsert_atomic(
            "jira", key, str(cid),
            author=comment.get("author", "Unknown"),
            content=comment.get("body", ""),
            created_at=comment.get("created", ""),
            updated_at=comment.get("updated", comment.get("created", "")),
            metadata={"comment_id": cid},
        ):
            changed = True

    db.clear_relationships(key)
    if issue.get("parent"):
        db.upsert_relationship(key, issue["parent"]["key"], "parent")
    for sub in issue.get("subtasks", []):
        db.upsert_relationship(key, sub["key"], "child")
    for link in issue.get("links", []):
        db.upsert_relationship(key, link["key"], link["type"].lower().replace(" ", "-"))

    return changed


def summarize_issues(db: SkillDB, ticket_keys: list[str], force: bool = False) -> None:
    """Summarize tickets and print each output block immediately when ready.
    Uses incremental approach: existing summary + only new/changed items.
    If force=True, re-summarizes all tickets regardless of cache."""
    for key in ticket_keys:
        if not force and not db.needs_resummarize(key):
            existing = db.get_resource_summary(key)
            if existing:
                _print_output(db, key, existing)
                eprint(f"  {key}: using cached summary")
            continue

        existing_summary = db.get_resource_summary(key)
        existing_text = existing_summary["summary"] if existing_summary else None
        summarized_at = existing_summary.get("summarized_at") if existing_summary else None

        if existing_text and summarized_at:
            items = db.get_items_since(key, summarized_at)
            if not items:
                items = db.get_atomic_for_resource(key)
        else:
            items = db.get_atomic_for_resource(key)

        if not items:
            if existing_summary:
                _print_output(db, key, existing_summary)
            continue

        ticket_item = next(
            (i for i in db.get_atomic_for_resource(key) if i["item_id"] == key), None
        )
        title = ""
        meta = {}
        if ticket_item:
            meta = json.loads(ticket_item.get("metadata", "{}"))
            content_lines = ticket_item.get("content", "").split("\n")
            for line in content_lines:
                if line.startswith("Title: "):
                    title = line[7:]
                    break

        eprint(f"  {key}: summarizing ({len(items)} items, existing_summary={'yes' if existing_text else 'no'})...")
        summary_text = summarize_resource(
            title=f"{key}: {title}" if title else key,
            source_type="Jira ticket",
            atomic_items=items,
            metadata=meta,
            existing_summary=existing_text,
        )

        if summary_text:
            db.upsert_summary(key, "jira", title or key, summary_text, meta)
            _print_output(db, key, db.get_resource_summary(key))
        elif existing_summary:
            _print_output(db, key, existing_summary)


def _print_output(db: SkillDB, key: str, summary_row: dict) -> None:
    """Print text output block immediately and flush stdout."""
    meta = json.loads(summary_row.get("metadata", "{}"))
    title = summary_row.get("title", "")

    meta_parts = ["Source: jira", f"Key: {key}"]
    if meta.get("status"):
        cat = f" ({meta['status_category']})" if meta.get("status_category") else ""
        meta_parts.append(f"Status: {meta['status']}{cat}")
    if meta.get("issuetype"):
        meta_parts.append(f"Type: {meta['issuetype']}")
    if meta.get("priority"):
        meta_parts.append(f"Priority: {meta['priority']}")
    if meta.get("assignee"):
        meta_parts.append(f"Assignee: {meta['assignee']}")
    if meta.get("reporter"):
        meta_parts.append(f"Reporter: {meta['reporter']}")
    if meta.get("duedate"):
        meta_parts.append(f"Due: {meta['duedate']}")
    if meta.get("resolution"):
        meta_parts.append(f"Resolution: {meta['resolution']}")
    if meta.get("labels"):
        meta_parts.append(f"Labels: {', '.join(meta['labels'])}")
    if meta.get("components"):
        meta_parts.append(f"Components: {', '.join(meta['components'])}")
    if meta.get("fix_versions"):
        meta_parts.append(f"Fix Versions: {', '.join(meta['fix_versions'])}")

    rels = db.get_relationships(key)
    if rels:
        grouped = {}
        for r in rels:
            rtype = r["relation_type"]
            target = r["target_key"] if r["source_key"] == key else r["source_key"]
            grouped.setdefault(rtype, []).append(target)
        for rtype, targets in grouped.items():
            meta_parts.append(f"{rtype}: {', '.join(targets)}")

    metadata_block = " | ".join(meta_parts)
    summary = summary_row.get("summary", "")

    header = f"jira/{key}: {title}" if title else f"jira/{key}"
    print(f"## {header}\n{metadata_block}\n{summary}\n", flush=True)
