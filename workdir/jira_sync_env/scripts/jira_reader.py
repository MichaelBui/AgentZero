#!/usr/bin/env python3
"""
Jira Reader - unified entry point for fetching Jira tickets.

Accepts --jql, --filter-id, and/or --view-id. Processes all provided sources
sequentially, deduplicates by ticket key, then summarizes via AI.

Usage:
  python jira_reader.py --jql "project = DPD AND status != Done"
  python jira_reader.py --filter-id 13811
  python jira_reader.py --view-id 10489904 --jql "..."
  python jira_reader.py --filter-id 13811 --view-id 10489904
  python jira_reader.py --cached-only
"""

import argparse
import sys

from jira_common import (
    validate_env, get_auth_header, fetch_issues, format_issue,
    get_jira_db, issue_needs_fetch, cache_issue,
    eprint, add_common_args, setup_output_redirection, cleanup_files,
    run_cached_only, start_summarize_pipeline, finish_summarize_pipeline,
)
from jira_filter import fetch_filter
from jira_view import resolve_view_to_jql

def main():
    parser = argparse.ArgumentParser(
        description="Fetch Jira tickets from JQL, saved filter, and/or Polaris view"
    )
    parser.add_argument("--jql", default=None,
                        help="JQL query string")
    parser.add_argument("--filter-id", default=None,
                        help="Jira saved filter ID (numeric)")
    parser.add_argument("--view-id", default=None,
                        help="Numeric Polaris view ID")
    parser.add_argument("--limit", type=int, default=200,
                        help="Max tickets per source (default: 200)")
    parser.add_argument("--offset", type=int, default=0,
                        help="Pagination offset")
    parser.add_argument("--no-cache", action="store_true",
                        help="Bypass JQL cache for view resolution")
    parser.add_argument("--force", action="store_true",
                        help="Skip timestamp checks, fetch and re-summarize everything")
    add_common_args(parser)
    args = parser.parse_args()

    setup_output_redirection(args)
    if args.force:
        eprint("--force: recreating database from scratch")
    db = get_jira_db(force=args.force)

    try:
        if args.cached_only:
            run_cached_only(db)
            return

        email, api_key = validate_env()
        headers = get_auth_header(email, api_key)

        jql_sources: list[tuple[str, str]] = []

        if args.filter_id:
            filter_name, filter_jql = fetch_filter(args.filter_id, headers)
            jql_sources.append((f"filter:{args.filter_id} ({filter_name})", filter_jql))

        if args.view_id:
            view_jql = resolve_view_to_jql(args.view_id, headers, use_cache=not args.no_cache)
            jql_sources.append((f"view:{args.view_id}", view_jql))

        if args.jql:
            jql_sources.append(("jql", args.jql))

        if not jql_sources:
            eprint("No source provided (--jql, --filter-id, or --view-id required). Nothing to do.")
            return

        sum_q, worker = start_summarize_pipeline(db, force=args.force)
        seen_keys: set = set()
        unchanged_keys: list = []

        try:
            for source_label, jql in jql_sources:
                eprint(f"\n=== Source: {source_label} ===")
                eprint(f"JQL: {jql}")
                issues, total = fetch_issues(jql, args.limit, args.offset, headers)
                eprint(f"Processing {len(issues)} issues (total: {total}, force={args.force})...")

                for raw in issues:
                    key = raw.get("key", "")
                    if key in seen_keys:
                        eprint(f"  {key}: duplicate, skipping")
                        continue
                    seen_keys.add(key)

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
        finally:
            finish_summarize_pipeline(sum_q, worker)

        eprint(f"\nPipeline complete. {len(seen_keys)} unique tickets processed.")
    finally:
        db.close()
        cleanup_files()


if __name__ == "__main__":
    main()
