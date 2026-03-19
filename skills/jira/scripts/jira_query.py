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

        issues, api_total = fetch_issues(args.jql, args.limit, args.offset, headers)
        total = len(issues)
        eprint(f"Processing {total}/{api_total} issues (force={args.force})")

        pipeline = start_summarize_pipeline(db, force=args.force)
        pipeline.set_total(total)
        unchanged_keys = []

        for idx, raw in enumerate(issues, 1):
            key = raw.get("key", "")
            api_updated = raw.get("fields", {}).get("updated", "")

            print(f"[Fetching {idx}/{total}] {key}", flush=True)
            if not args.force and not issue_needs_fetch(db, key, api_updated):
                eprint(f"  [{idx}/{total}] {key}: unchanged (timestamp match), skipping")
                unchanged_keys.append(key)
                print(f"[Fetched {idx}/{total}] {key}: unchanged (cached)", flush=True)
                continue

            issue = format_issue(raw)
            cache_issue(db, issue)
            eprint(f"  [{idx}/{total}] {key}: fetched and cached")
            pipeline.put(key)
            print(f"[Fetched {idx}/{total}] {key}: cached, queued for summarization", flush=True)

        for key in unchanged_keys:
            pipeline.put(key)

        finish_summarize_pipeline(pipeline)
        eprint(f"{'='*60}")
        eprint(f"STATUS: COMPLETED - Jira Query pipeline finished successfully ({total} tickets)")
        eprint(f"{'='*60}")
    finally:
        db.close()
        cleanup_files()


if __name__ == "__main__":
    main()
