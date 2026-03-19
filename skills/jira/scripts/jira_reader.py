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
import os
import sys

from jira_common import (
    validate_env, get_auth_header, fetch_issues, format_issue,
    get_jira_db, issue_needs_fetch, cache_issue,
    eprint, add_common_args, setup_output_redirection, cleanup_files,
    run_cached_only, start_summarize_pipeline, finish_summarize_pipeline,
)
from jira_filter import fetch_filter
from jira_view import resolve_view_to_jql

_DEFAULT_FILTER_ID = os.environ.get("JIRA_DEFAULT_FILTER_ID", "13811")
_DEFAULT_VIEW_ID = os.environ.get("JIRA_DEFAULT_VIEW_ID", "10489904")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch Jira tickets from JQL, saved filter, and/or Polaris view"
    )
    parser.add_argument("--jql", default=None,
                        help="JQL query string")
    parser.add_argument("--filter-id", default=_DEFAULT_FILTER_ID,
                        help=f"Jira saved filter ID (default: {_DEFAULT_FILTER_ID}, override via JIRA_DEFAULT_FILTER_ID)")
    parser.add_argument("--view-id", default=_DEFAULT_VIEW_ID,
                        help=f"Numeric Polaris view ID (default: {_DEFAULT_VIEW_ID}, override via JIRA_DEFAULT_VIEW_ID)")
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

    print("[jira_reader] STARTED - fetching and summarizing Jira tickets. Do NOT interrupt or move on.", flush=True)

    try:
        if args.cached_only:
            run_cached_only(db)
            print(
                f"\n{'='*60}\n"
                f"[jira_reader] ALL DONE - output file is ready for use.\n"
                f"{'='*60}\n",
                flush=True,
            )
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

        pipeline = start_summarize_pipeline(db, force=args.force)
        seen_keys: set = set()
        unchanged_keys: list = []

        try:
            # First pass: collect all unique keys across all sources
            all_issues_by_source: list[tuple[str, list]] = []
            for source_label, jql in jql_sources:
                eprint(f"\n=== Source: {source_label} ===")
                eprint(f"JQL: {jql}")
                issues, total = fetch_issues(jql, args.limit, args.offset, headers)
                eprint(f"Fetched {len(issues)}/{total} issues from {source_label}")
                all_issues_by_source.append((source_label, issues))

            _pre_seen: set = set()
            total_unique = 0
            for _, issues in all_issues_by_source:
                for raw in issues:
                    k = raw.get("key", "")
                    if k and k not in _pre_seen:
                        _pre_seen.add(k)
                        total_unique += 1
            pipeline.set_total(total_unique)
            eprint(f"Total unique tickets to process: {total_unique} (force={args.force})")

            fetch_idx = 0
            for source_label, issues in all_issues_by_source:
                eprint(f"\n=== Processing: {source_label} ({len(issues)} issues) ===")
                for raw in issues:
                    key = raw.get("key", "")
                    if key in seen_keys:
                        eprint(f"  {key}: duplicate, skipping")
                        continue
                    seen_keys.add(key)
                    fetch_idx += 1

                    eprint(f"[Fetching {fetch_idx}/{total_unique}] {key} (summarization pending)")
                    print(f"[Fetching {fetch_idx}/{total_unique}] {key} (summarization pending)", flush=True)

                    api_updated = raw.get("fields", {}).get("updated", "")
                    if not args.force and not issue_needs_fetch(db, key, api_updated):
                        eprint(f"[Fetched {fetch_idx}/{total_unique}] {key}: unchanged - summarization pending")
                        unchanged_keys.append(key)
                        print(f"[Fetched {fetch_idx}/{total_unique}] {key}: unchanged (cached) - summarization pending", flush=True)
                        continue

                    issue = format_issue(raw)
                    cache_issue(db, issue)
                    eprint(f"[Fetched {fetch_idx}/{total_unique}] {key}: cached - queued for summarization")
                    pipeline.put(key)
                    print(f"[Fetched {fetch_idx}/{total_unique}] {key}: cached - queued for summarization (pipeline running)", flush=True)

            for key in unchanged_keys:
                pipeline.put(key)
        finally:
            _sum_errors = finish_summarize_pipeline(pipeline)

        if _sum_errors:
            eprint(f"{'='*60}")
            eprint(f"STATUS: COMPLETED WITH ERRORS - Jira Reader finished ({len(seen_keys)} unique tickets, {len(_sum_errors)} summarization error(s))")
            for err in _sum_errors:
                eprint(f"  ERROR: {err}")
            eprint(f"{'='*60}")
            print(
                f"\n{'='*60}\n"
                f"[jira_reader] COMPLETED WITH ERRORS - output file is ready but {len(_sum_errors)} ticket(s) may lack summaries.\n"
                f"Processed: {len(seen_keys)} unique tickets | Errors: {len(_sum_errors)}\n"
                f"{'='*60}\n",
                flush=True,
            )
        else:
            eprint(f"{'='*60}")
            eprint(f"STATUS: COMPLETED - Jira Reader pipeline finished successfully ({len(seen_keys)} unique tickets)")
            eprint(f"{'='*60}")
            print(
                f"\n{'='*60}\n"
                f"[jira_reader] ALL DONE - output file is ready for use.\n"
                f"Processed: {len(seen_keys)} unique tickets\n"
                f"{'='*60}\n",
                flush=True,
            )
    except Exception as e:
        eprint(f"{'='*60}")
        eprint(f"STATUS: FAILED - Jira Reader encountered an error: {e}")
        eprint(f"{'='*60}")
        print(f"\n[jira_reader] FAILED with error: {e}\n", flush=True)
        raise
    finally:
        db.close()
        cleanup_files()


if __name__ == "__main__":
    main()
