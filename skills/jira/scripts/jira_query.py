#!/usr/bin/env python3
"""
Jira Query - fetch tickets using a raw JQL query, cache, and summarize.

Default JQL fetches the current user's active tickets.
Always outputs compact summaries (key IDs + metadata + AI summary).

Usage:
  python jira_query.py
  python jira_query.py --jql "project = DPD AND status != Done"
  python jira_query.py --force
"""

import argparse
import sys

from jira_common import (
    validate_env, get_auth_header, fetch_issues, format_issue,
    get_jira_db, issue_needs_fetch, cache_issue, summarize_issues,
    eprint,
)

DEFAULT_JQL = 'assignee = currentUser() AND status != Done ORDER BY updated DESC'


def main():
    parser = argparse.ArgumentParser(description="Fetch Jira tickets using a raw JQL query")
    parser.add_argument("--jql", default=DEFAULT_JQL, help="JQL query (default: current user's active tickets)")
    parser.add_argument("--limit", type=int, default=50, help="Max tickets (default: 50)")
    parser.add_argument("--offset", type=int, default=0, help="Pagination offset")
    parser.add_argument("--force", action="store_true", help="Skip timestamp checks, fetch and re-summarize everything")
    args = parser.parse_args()

    email, api_key = validate_env()
    headers = get_auth_header(email, api_key)
    db = get_jira_db()

    try:
        issues, total = fetch_issues(args.jql, args.limit, args.offset, headers)
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
