#!/usr/bin/env python3
"""
Jira Polaris View Listing Tool
================================
Fetches tickets from a Jira Polaris View via two-step: GraphQL (view → JQL) + REST API (issues).
Output: JSON array to stdout. Progress/debug to stderr.

Architecture
------------
Step 1 — GraphQL: Resolve the complete JQL for a Polaris view.
  - `polarisView.jql` (scalar) provides the base JQL (project + issuetype + ORDER BY).
  - `polarisView.filter[]` provides additional UI-level filter conditions NOT in the scalar jql
    (e.g. Roadmap bucket field, Status filter). Each filter has `kind`, `field.jiraFieldKey`,
    and `values[].stringValue` (which are raw IDs for custom fields and status).
  - `polarisView.sortMode` provides fallback sort when `sort[]` is empty (e.g. PROJECT_RANK).
  - The complete JQL = base_jql (no ORDER BY) + AND filter conditions + ORDER BY from sort/sortMode.

Step 2 — REST: Fetch issues using the resolved JQL via `/rest/api/3/search/jql`.

JQL Caching
-----------
Resolving JQL via GraphQL is slow (~3s). Since Polaris view filters change rarely,
the resolved JQL is cached per viewId in a JSON file (~/.cache/jira_view_jql.json).
Cache TTL: 86400 seconds (24 hours). Bypass with --no-cache flag.

Custom Field JQL Mapping
------------------------
Polaris filter values use raw IDs (stringValue). In JQL:
  - `customfield_XXXXX` → `cf[XXXXX] in (id1, id2, ...)` — IDs work directly without name lookup.
  - `status` → `status in (id1, id2, ...)` — Jira accepts status IDs in JQL.
  - Standard fields (non-custom) use the field key directly.

Sort Mode Mapping
-----------------
  PROJECT_RANK → ORDER BY rank ASC
  CREATED      → ORDER BY created DESC
  UPDATED      → ORDER BY updated DESC
"""

import argparse
import base64
import json
import os
import sys
import time
from pathlib import Path

import requests

JIRA_BASE = "https://ntuclink.atlassian.net"
CLOUD_ID = "faa50733-0f7b-4288-901e-5e0e16334984"
GRAPHQL_URL = f"{JIRA_BASE}/gateway/api/graphql"
SEARCH_URL = f"{JIRA_BASE}/rest/api/3/search/jql"
CACHE_FILE = Path.home() / ".cache" / "jira_view_jql.json"
CACHE_TTL = 86400  # 24 hours in seconds


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def load_jql_cache() -> dict:
    """Load cached JQL entries from disk. Returns empty dict on any error."""
    try:
        if CACHE_FILE.exists():
            return json.loads(CACHE_FILE.read_text())
    except Exception:
        pass
    return {}


def get_cached_jql(view_id: str) -> str | None:
    """Return cached JQL for view_id if it exists and is within TTL, else None."""
    cache = load_jql_cache()
    entry = cache.get(view_id)
    if entry and (time.time() - entry.get("ts", 0)) < CACHE_TTL:
        eprint(f"Cache hit for view {view_id} (age: {int(time.time() - entry['ts'])}s)")
        return entry["jql"]
    return None


def set_cached_jql(view_id: str, jql: str) -> None:
    """Persist resolved JQL to disk cache with current timestamp."""
    try:
        CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        cache = load_jql_cache()
        cache[view_id] = {"jql": jql, "ts": time.time()}
        CACHE_FILE.write_text(json.dumps(cache, indent=2))
    except Exception as e:
        eprint(f"WARN: Failed to write JQL cache: {e}")


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


def resolve_view_to_jql(view_id: str, headers: dict, use_cache: bool = True) -> str:
    """Step 1: Query Polaris GraphQL API to resolve full JQL for a view.

    Uses disk cache (TTL: 24h) to skip the slow GraphQL call on repeat invocations.
    Pass use_cache=False (or --no-cache CLI flag) to force refresh.
    """
    if use_cache:
        cached = get_cached_jql(view_id)
        if cached:
            return cached

    ari = f"ari:cloud:jira:{CLOUD_ID}:view/{view_id}"
    query = """
    query GetPolarisViewJQL($viewId: ID!) {
      polarisView(id: $viewId) {
        jql
        userJql
        name
        sortMode
        sort {
          order
          field {
            jiraFieldKey
          }
        }
        filter {
          kind
          field {
            id
            jiraFieldKey
          }
          values {
            stringValue
            numericValue
            enumValue
            operator
          }
        }
      }
    }
    """
    payload = {"query": query, "variables": {"viewId": ari}}
    graphql_headers = {
        **headers,
        "Content-Type": "application/json",
        "x-experimentalapi": "polaris-v0",
    }
    eprint(f"Resolving view {view_id} via GraphQL...")
    resp = request_with_retry("POST", GRAPHQL_URL, headers=graphql_headers, json=payload)
    if resp.status_code != 200:
        eprint(f"ERROR: GraphQL returned {resp.status_code}: {resp.text}")
        sys.exit(1)
    data = resp.json()
    if "errors" in data:
        for err in data["errors"]:
            severity = err.get("extensions", {}).get("agg", {}).get("severity", "ERROR")
            if severity != "NORMAL":
                eprint(f"GraphQL error: {err.get('message')}")

    view = data.get("data", {}).get("polarisView")
    if not view:
        eprint(f"ERROR: View ID {view_id} not found.")
        sys.exit(1)

    eprint(f"View name: {view.get('name')}")

    base_jql = view.get("jql") or view.get("userJql")
    if not base_jql:
        eprint(f"ERROR: View {view_id} has no base JQL defined.")
        sys.exit(1)

    filters = view.get("filter") or []
    sort_fields = view.get("sort") or []
    sort_mode = view.get("sortMode")

    jql = build_jql_from_filters(base_jql, filters, sort_fields, sort_mode)
    eprint(f"Resolved JQL: {jql}")
    set_cached_jql(view_id, jql)
    return jql


def build_jql_from_filters(base_jql: str, filters: list, sort_fields: list, sort_mode: str) -> str:
    """Combine base JQL with Polaris filter conditions and sort order.

    Strategy:
    - Strip ORDER BY from base_jql (Polaris sort takes precedence)
    - Append each filter as an AND condition using field IDs
    - Re-append ORDER BY from sort_fields or sort_mode
    """
    # Strip ORDER BY from base JQL (case-insensitive)
    order_idx = base_jql.upper().rfind(" ORDER BY ")
    base_without_order = base_jql[:order_idx].strip() if order_idx >= 0 else base_jql.strip()

    conditions = [base_without_order]

    for f in (filters or []):
        field_info = f.get("field") or {}
        jira_key = field_info.get("jiraFieldKey") or field_info.get("id")
        kind = f.get("kind", "FIELD_IDENTITY")
        values_raw = f.get("values") or []

        # Extract the non-null value from each value object
        resolved = []
        for v in values_raw:
            val = v.get("stringValue") or v.get("numericValue") or v.get("enumValue")
            if val is not None:
                resolved.append(str(val))

        if not jira_key or not resolved:
            eprint(f"WARN: Skipping filter — missing field or values: {f}")
            continue

        # Use cf[id] syntax for custom fields, plain key for system fields
        if jira_key.startswith("customfield_"):
            field_id = jira_key.split("_", 1)[1]
            jql_field = f"cf[{field_id}]"
        else:
            jql_field = jira_key

        negate = "NOT" in kind.upper()
        if len(resolved) == 1:
            op = "!=" if negate else "="
            conditions.append(f"{jql_field} {op} {resolved[0]}")
        else:
            op = "not in" if negate else "in"
            ids = ", ".join(resolved)
            conditions.append(f"{jql_field} {op} ({ids})")

    jql = " AND ".join(conditions)

    # Determine ORDER BY: explicit sort fields take priority, then sortMode
    order_parts = []
    for s in (sort_fields or []):
        field_info = s.get("field") or {}
        key = field_info.get("jiraFieldKey")
        order = s.get("order", "DESC").upper()
        if key:
            order_parts.append(f"{key} {order}")

    if not order_parts and sort_mode:
        mode = sort_mode.upper()
        if mode == "PROJECT_RANK":
            order_parts.append("rank ASC")
        elif mode == "CREATED":
            order_parts.append("created DESC")
        elif mode == "UPDATED":
            order_parts.append("updated DESC")
        # else: no recognized sort mode, omit ORDER BY

    if order_parts:
        jql += " ORDER BY " + ", ".join(order_parts)

    return jql


def fetch_issues(jql: str, limit: int, offset: int, headers: dict) -> list[dict]:
    """Step 2: Fetch issues via Jira REST API v3."""
    params = {
        "jql": jql,
        "maxResults": limit,
        "startAt": offset,
        "expand": "names,renderedFields,operations,changelog,links,comments",
        "fields": "summary,description,status,parent,issuelinks,created,updated,comment,subtasks",
    }
    eprint(f"Fetching issues (limit={limit}, offset={offset})...")
    resp = request_with_retry("GET", SEARCH_URL, headers=headers, params=params)
    if resp.status_code != 200:
        eprint(f"ERROR: Search API returned {resp.status_code}: {resp.text}")
        sys.exit(1)
    data = resp.json()
    total = data.get("total", 0)
    issues = data.get("issues", [])
    eprint(f"Found {total} total tickets, fetched {len(issues)}")
    return issues


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
    return {
        "key": issue.get("key"),
        "id": issue.get("id"),
        "title": fields.get("summary"),
        "description": description,
        "status": {
            "name": status.get("name"),
            "category": status.get("statusCategory", {}).get("name"),
        },
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
        print(json.dumps(data, separators=(",", ":"), ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description="Fetch Jira tickets from a Polaris View")
    parser.add_argument("--viewId", required=True, help="Numeric Polaris view ID")
    parser.add_argument("--format", choices=["json", "yaml"], default="json", help="Output format (default: json)")
    parser.add_argument("--limit", type=int, default=50, help="Max tickets (default: 50)")
    parser.add_argument("--offset", type=int, default=0, help="Pagination offset (default: 0)")
    parser.add_argument("--no-cache", action="store_true", help="Bypass JQL cache and re-resolve from GraphQL")
    args = parser.parse_args()

    email, api_key = validate_env()
    auth_headers = get_auth_header(email, api_key)

    jql = resolve_view_to_jql(args.viewId, auth_headers, use_cache=not args.no_cache)
    issues = fetch_issues(jql, args.limit, args.offset, auth_headers)
    formatted = [format_issue(issue) for issue in issues]

    output_data(formatted, args.format)


if __name__ == "__main__":
    main()
