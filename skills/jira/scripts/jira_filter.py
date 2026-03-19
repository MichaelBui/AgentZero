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
    eprint, JIRA_BASE,
    add_common_args, setup_output_redirection, cleanup_files, run_cached_only,
    start_summarize_pipeline, finish_summarize_pipeline,
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
    parser.add_argument("--filter-id", required=not any(a in sys.argv for a in ["--cached-only"]),
                        default=None, help="Jira saved filter ID (numeric)")
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

        filter_name, jql = fetch_filter(args.filter_id, headers)
        issues, api_total = fetch_issues(jql, args.limit, args.offset, headers)
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
        eprint(f"STATUS: COMPLETED - Jira Filter pipeline finished successfully ({total} tickets)")
        eprint(f"{'='*60}")
    finally:
        db.close()
        cleanup_files()


if __name__ == "__main__":
    main()
