#!/usr/bin/env python3
"""
Jira View - fetch tickets from a Polaris View, cache, and summarize.

Two-step: GraphQL (view -> JQL) + REST API (issues).
JQL caching with 24h TTL to skip slow GraphQL resolution on repeat calls.
Always outputs compact summaries (key IDs + metadata + AI summary).

Usage:
  python jira_view.py --viewId 12345
  python jira_view.py --viewId 12345 --force --no-cache
"""

import argparse
import json
import sys
import time
from pathlib import Path

from jira_common import (
    validate_env, get_auth_header, request_with_retry, fetch_issues,
    format_issue, get_jira_db, issue_needs_fetch, cache_issue,
    summarize_issues, eprint, JIRA_BASE,
)

CLOUD_ID = "faa50733-0f7b-4288-901e-5e0e16334984"
GRAPHQL_URL = f"{JIRA_BASE}/gateway/api/graphql"
CACHE_FILE = Path.home() / ".cache" / "jira_view_jql.json"
CACHE_TTL = 86400


def load_jql_cache() -> dict:
    try:
        if CACHE_FILE.exists():
            return json.loads(CACHE_FILE.read_text())
    except Exception:
        pass
    return {}


def get_cached_jql(view_id: str) -> str | None:
    cache = load_jql_cache()
    entry = cache.get(view_id)
    if entry and (time.time() - entry.get("ts", 0)) < CACHE_TTL:
        eprint(f"Cache hit for view {view_id} (age: {int(time.time() - entry['ts'])}s)")
        return entry["jql"]
    return None


def set_cached_jql(view_id: str, jql: str) -> None:
    try:
        CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        cache = load_jql_cache()
        cache[view_id] = {"jql": jql, "ts": time.time()}
        CACHE_FILE.write_text(json.dumps(cache, indent=2))
    except Exception as e:
        eprint(f"WARN: Failed to write JQL cache: {e}")


def build_jql_from_filters(base_jql: str, filters: list, sort_fields: list, sort_mode: str) -> str:
    order_idx = base_jql.upper().rfind(" ORDER BY ")
    base_without_order = base_jql[:order_idx].strip() if order_idx >= 0 else base_jql.strip()
    conditions = [base_without_order]

    for f in (filters or []):
        field_info = f.get("field") or {}
        jira_key = field_info.get("jiraFieldKey") or field_info.get("id")
        kind = f.get("kind", "FIELD_IDENTITY")
        values_raw = f.get("values") or []
        resolved = []
        for v in values_raw:
            val = v.get("stringValue") or v.get("numericValue") or v.get("enumValue")
            if val is not None:
                resolved.append(str(val))
        if not jira_key or not resolved:
            continue

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

    if order_parts:
        jql += " ORDER BY " + ", ".join(order_parts)

    return jql


def resolve_view_to_jql(view_id: str, headers: dict, use_cache: bool = True) -> str:
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
          field { jiraFieldKey }
        }
        filter {
          kind
          field { id jiraFieldKey }
          values { stringValue numericValue enumValue operator }
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

    jql = build_jql_from_filters(
        base_jql,
        view.get("filter") or [],
        view.get("sort") or [],
        view.get("sortMode"),
    )
    eprint(f"Resolved JQL: {jql}")
    set_cached_jql(view_id, jql)
    return jql


def main():
    parser = argparse.ArgumentParser(description="Fetch Jira tickets from a Polaris View")
    parser.add_argument("--viewId", required=True, help="Numeric Polaris view ID")
    parser.add_argument("--limit", type=int, default=50, help="Max tickets (default: 50)")
    parser.add_argument("--offset", type=int, default=0, help="Pagination offset")
    parser.add_argument("--no-cache", action="store_true", help="Bypass JQL cache and re-resolve from GraphQL")
    parser.add_argument("--force", action="store_true", help="Skip timestamp checks, fetch and re-summarize everything")
    args = parser.parse_args()

    email, api_key = validate_env()
    headers = get_auth_header(email, api_key)
    db = get_jira_db()

    try:
        jql = resolve_view_to_jql(args.viewId, headers, use_cache=not args.no_cache)
        issues, total = fetch_issues(jql, args.limit, args.offset, headers)
        eprint(f"Processing {len(issues)} issues... (force={args.force})")

        all_keys = []
        for raw in issues:
            key = raw.get("key", "")
            api_updated = raw.get("fields", {}).get("updated", "")
            all_keys.append(key)

            if not args.force and not issue_needs_fetch(db, key, api_updated):
                eprint(f"  {key}: unchanged (timestamp match), skipping")
                continue

            issue = format_issue(raw)
            cache_issue(db, issue)
            eprint(f"  {key}: fetched and cached")

        eprint(f"\nSummarizing {len(all_keys)} tickets...")
        summarize_issues(db, all_keys, force=args.force)
    finally:
        db.close()


if __name__ == "__main__":
    main()
