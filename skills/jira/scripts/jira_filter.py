#!/usr/bin/env python3
"""
Jira Filter - fetch tickets from a saved Jira filter, cache, and summarize.

Resolves the filter's JQL via REST API, then fetches and summarizes issues.
Always outputs compact summaries (key IDs + metadata + AI summary).

Usage:
  python jira_filter.py --filter-id 12345
  python jira_filter.py --filter-id 12345 --force
"""

import argparse
import sys

from jira_common import (
    validate_env, get_auth_header, request_with_retry, fetch_issues,
    format_issue, get_jira_db, issue_needs_fetch, cache_issue,
    summarize_issues, eprint, JIRA_BASE,
)

FILTER_URL = f"{JIRA_BASE}/rest/api/3/filter"


def fetch_filter(filter_id: str, headers: dict) -> tuple[str, str]:
    """Resolve a saved filter by ID. Returns (filter_name, jql)."""
    url = f"{FILTER_URL}/{filter_id}"
    eprint(f"Resolving filter ID: {filter_id}...")
    resp = request_with_retry("GET", url, headers=headers)
    if resp.status_code != 200:
        eprint(f"ERROR: Filter API returned {resp.status_code}: {resp.text}")
        sys.exit(1)
    data = resp.json()
    name = data.get("name", "(unnamed)")
    jql = data.get("jql", "")
    if not jql:
        eprint(f"ERROR: Filter '{name}' has no JQL query.")
        sys.exit(1)
    eprint(f"Filter: {name}")
    eprint(f"JQL: {jql}")
    return name, jql


def main():
    parser = argparse.ArgumentParser(description="Fetch Jira tickets from a saved filter")
    parser.add_argument("--filter-id", required=True, help="Jira saved filter ID (numeric)")
    parser.add_argument("--limit", type=int, default=50, help="Max tickets (default: 50)")
    parser.add_argument("--offset", type=int, default=0, help="Pagination offset")
    parser.add_argument("--force", action="store_true", help="Skip timestamp checks, fetch and re-summarize everything")
    args = parser.parse_args()

    email, api_key = validate_env()
    headers = get_auth_header(email, api_key)
    db = get_jira_db()

    try:
        filter_name, jql = fetch_filter(args.filter_id, headers)
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
