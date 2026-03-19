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
    get_jira_db, issue_needs_fetch, cache_issue,
    eprint, add_common_args, setup_output_redirection, cleanup_files, run_cached_only,
    start_summarize_pipeline, finish_summarize_pipeline,
)

DEFAULT_JQL = 'assignee = currentUser() AND status != Done ORDER BY updated DESC'


def main():
    parser = argparse.ArgumentParser(description="Fetch Jira tickets using a raw JQL query")
    parser.add_argument("--jql", default=DEFAULT_JQL, help="JQL query (default: current user's active tickets)")
    parser.add_argument("--limit", type=int, default=200, help="Max tickets (default: 200)")
    parser.add_argument("--offset", type=int, default=0, help="Pagination offset")
    parser.add_argument("--force", action="store_true", help="Skip timestamp checks, fetch and re-summarize everything")
    add_common_args(parser)
    args = parser.parse_args()

    setup_output_redirection(args)
    db = get_jira_db(force=args.force)

    try:
        if args.cached_only:
            run_cached_only(db)
            return

        email, api_key = validate_env()
        headers = get_auth_header(email, api_key)

        issues, total = fetch_issues(args.jql, args.limit, args.offset, headers)
        eprint(f"Processing {len(issues)} issues... (force={args.force})")

        sum_q, worker = start_summarize_pipeline(db, force=args.force)
        unchanged_keys = []

        for raw in issues:
            key = raw.get("key", "")
            api_updated = raw.get("fields", {}).get("updated", "")

            if not args.force and not issue_needs_fetch(db, key, api_updated):
                eprint(f"  {key}: unchanged (timestamp match), skipping")
                unchanged_keys.append(key)
                continue

            issue = format_issue(raw)
            cache_issue(db, issue)
            eprint(f"  {key}: fetched and cached")
            sum_q.put(key)

        for key in unchanged_keys:
            sum_q.put(key)

        finish_summarize_pipeline(sum_q, worker)
        eprint(f"{'='*60}")
        eprint(f"STATUS: COMPLETED - Jira Query pipeline finished successfully")
        eprint(f"{'='*60}")
    finally:
        db.close()
        cleanup_files()


if __name__ == "__main__":
    main()
