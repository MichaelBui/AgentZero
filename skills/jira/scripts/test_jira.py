#!/usr/bin/env python3
"""
BDD-style test-table unit tests for jira.py public API.

Uses pytest subtests fixture for verbose scenario output.
Run: make test          (quiet)
     make test-verbose  (shows each SUBPASSED scenario)

Pattern: one test function per public method, containing a test table
of (scenario, input, expected) tuples with descriptive scenario names
following "When {scenario} then {expected behavior}" format.
"""

import json
import os
import sqlite3
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from jira import (
    clean_jira_text,
    adf_to_text,
    open_db, SkillDB,
    SummaryResult, parse_llm_response,
    _build_system_prompt, _build_user_prompt, _load_user_context,
    _RELEVANCE_FLOORS, _WORD_HINTS, _default_lookback_days,
    format_issue, _extract_comments, _extract_links,
    _build_ticket_metadata, cache_issue,
    _build_view_jql,
    _format_summary_block, write_output,
    _Pipeline, _summarize_one, _call_llm, _request,
    get_auth_header, log, validate_env, main,
    summarize_resource, fetch_issues, fetch_filter_jql,
    resolve_view_to_jql, _get_cached_view_jql, _set_cached_view_jql,
)


# ═══════════════════════════════════════════════════════════════
# Fixtures
# ═══════════════════════════════════════════════════════════════

@pytest.fixture
def db():
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    os.unlink(path)
    d = open_db(path)
    yield d
    d.close()
    for s in ("", "-wal", "-shm"):
        p = path + s
        if os.path.exists(p):
            os.unlink(p)


def _make_db():
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    os.unlink(path)
    return open_db(path), path


def _cleanup_db(d, path):
    d.close()
    for s in ("", "-wal", "-shm"):
        p = path + s
        if os.path.exists(p):
            os.unlink(p)


def _sample_issue(**overrides):
    base = {
        "key": "DPD-1",
        "fields": {
            "summary": "Test Ticket",
            "description": {"type": "paragraph", "content": [{"type": "text", "text": "Desc"}]},
            "status": {"name": "Open", "statusCategory": {"name": "To Do"}},
            "assignee": {"displayName": "Michael Bui"},
            "reporter": {"displayName": "John Doe"},
            "priority": {"name": "High"},
            "issuetype": {"name": "Task"},
            "resolution": None,
            "components": [{"name": "Backend"}],
            "fixVersions": [{"name": "v1.0"}],
            "labels": ["important"],
            "duedate": "2026-06-01",
            "parent": None,
            "subtasks": [],
            "issuelinks": [],
            "comment": {"comments": []},
            "created": "2026-01-01T00:00:00+0800",
            "updated": "2026-01-05T00:00:00+0800",
        },
    }
    for k, v in overrides.items():
        if k in base["fields"]:
            base["fields"][k] = v
        else:
            base[k] = v
    return base


# ═══════════════════════════════════════════════════════════════
# clean_jira_text
# ═══════════════════════════════════════════════════════════════

def test_clean_jira_text(subtests):
    cases = [
        ("When input is None then returns empty string", None, ""),
        ("When input is empty then returns empty string", "", ""),
        ("When input is normal text then returns unchanged", "Hello world", "Hello world"),
        ("When input has leading/trailing whitespace then strips it", "  hello  ", "hello"),
        ("When input has multiple consecutive newlines then collapses to two", "A\n\n\n\n\nB", "A\n\nB"),
        ("When input has multiple consecutive spaces then collapses to one", "A     B", "A B"),
        ("When input has mixed noise then cleans all at once", "Important\n\n\n\n\n\nstuff   here", "Important\n\nstuff here"),
    ]
    for scenario, input_val, expected in cases:
        with subtests.test(msg=scenario):
            assert clean_jira_text(input_val) == expected


def test_clean_jira_text_strips_technical_dumps(subtests):
    nmap = "Some text\nPORT  STATE SERVICE\n22/tcp open ssh\n80/tcp open http\n443/tcp open https\n"
    nmap += "\n".join([f"line{i}" for i in range(50)])
    result = clean_jira_text(nmap)
    with subtests.test(msg="When input contains nmap output then replaces with placeholder"):
        assert "[...technical output removed...]" in result


# ═══════════════════════════════════════════════════════════════
# adf_to_text
# ═══════════════════════════════════════════════════════════════

def test_adf_to_text(subtests):
    cases = [
        ("When node is None then returns empty string", None, ""),
        ("When node is plain string then returns string", "hello", "hello"),
        ("When node is integer then returns empty string", 42, ""),
        ("When node is text type then returns text value", {"type": "text", "text": "hello"}, "hello"),
        ("When node is hardBreak then returns newline", {"type": "hardBreak"}, "\n"),
        ("When node is paragraph then returns text with trailing newline",
         {"type": "paragraph", "content": [{"type": "text", "text": "Hello"}]}, "Hello\n"),
        ("When node is empty paragraph then returns just newline", {"type": "paragraph", "content": []}, "\n"),
        ("When node is list then concatenates children",
         [{"type": "text", "text": "a"}, {"type": "text", "text": "b"}], "ab"),
        ("When node is unknown type then processes children recursively",
         {"type": "custom_widget", "content": [{"type": "text", "text": "x"}]}, "x"),
    ]
    for scenario, input_val, expected in cases:
        with subtests.test(msg=scenario):
            assert adf_to_text(input_val) == expected


def test_adf_to_text_nested_document(subtests):
    doc = {
        "type": "doc",
        "content": [
            {"type": "paragraph", "content": [{"type": "text", "text": "Line 1"}]},
            {"type": "paragraph", "content": [{"type": "text", "text": "Line 2"}]},
        ],
    }
    result = adf_to_text(doc)
    with subtests.test(msg="When doc has nested paragraphs then all content is present"):
        assert "Line 1" in result and "Line 2" in result


# ═══════════════════════════════════════════════════════════════
# open_db
# ═══════════════════════════════════════════════════════════════

def test_open_db(subtests):
    cases = [
        ("When opening fresh DB then creates all required tables",
         {"atomic_content", "resource_summary", "ticket_relationships"}),
    ]
    for scenario, expected_tables in cases:
        with subtests.test(msg=scenario):
            d, path = _make_db()
            try:
                tables = {row[0] for row in d._conn.execute(
                    "SELECT name FROM sqlite_master WHERE type='table'")}
                assert expected_tables.issubset(tables)
            finally:
                _cleanup_db(d, path)


def test_open_db_preserves_data_on_reopen(subtests):
    d, path = _make_db()
    d.upsert_atomic("jira", "K-1", "K-1", "A", "x", "2026-01-01", "2026-01-01")
    d.close()
    d2 = open_db(path)
    with subtests.test(msg="When reopening DB then existing data is preserved"):
        assert len(d2.get_atomic_for_resource("K-1")) == 1
    _cleanup_db(d2, path)


def test_open_db_migration_on_old_schema(subtests):
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    os.unlink(path)
    conn = sqlite3.connect(path)
    conn.execute("""CREATE TABLE resource_summary (
        resource_id TEXT PRIMARY KEY, source TEXT NOT NULL,
        title TEXT, summary TEXT, summarized_at TEXT, metadata TEXT DEFAULT '{}'
    )""")
    conn.execute("INSERT INTO resource_summary VALUES ('K-1','jira','T','S','2026-01-01','{}')")
    conn.commit()
    conn.close()

    d = open_db(path)
    cols = {row[1] for row in d._conn.execute("PRAGMA table_info(resource_summary)")}
    with subtests.test(msg="When opening old-schema DB then migration adds mention_type column"):
        assert "mention_type" in cols
        assert "estimated_relevance" in cols
        assert "final_relevance" in cols
    _cleanup_db(d, path)


# ═══════════════════════════════════════════════════════════════
# SkillDB.upsert_atomic
# ═══════════════════════════════════════════════════════════════

def test_upsert_atomic(subtests, db):
    cases = [
        ("When inserting new item then returns True",
         ("jira", "K-1", "K-1", "A", "C", "2026-01-01", "2026-01-01"), {}, True, None),
        ("When upserting same content then returns False",
         ("jira", "K-1", "K-1", "A", "C", "2026-01-01", "2026-01-01"), {}, False, None),
        ("When upserting changed content then returns True and stores new value",
         ("jira", "K-1", "K-1", "A", "V2", "2026-01-01", "2026-01-02"), {},
         True, lambda: assert_eq(db.get_atomic_for_resource("K-1")[0]["content"], "V2")),
        ("When upserting with metadata then stores JSON blob",
         ("jira", "K-M", "K-M", "A", "x", "2026-01-01", "2026-01-01"),
         {"metadata": {"assignee": "Michael Bui"}},
         True, lambda: assert_eq(
             json.loads(db.get_atomic_for_resource("K-M")[0]["metadata"])["assignee"],
             "Michael Bui")),
    ]
    for scenario, args, kwargs, expected_return, extra_check in cases:
        with subtests.test(msg=scenario):
            result = db.upsert_atomic(*args, **kwargs)
            assert result == expected_return
            if extra_check:
                extra_check()


def assert_eq(a, b):
    assert a == b


# ═══════════════════════════════════════════════════════════════
# SkillDB.get_atomic_for_resource
# ═══════════════════════════════════════════════════════════════

def test_get_atomic_for_resource(subtests, db):
    db.upsert_atomic("jira", "K-1", "c2", "A", "second", "2026-01-02", "2026-01-02")
    db.upsert_atomic("jira", "K-1", "c1", "A", "first", "2026-01-01", "2026-01-01")
    cases = [
        ("When resource has no items then returns empty list", "NONE", []),
        ("When resource has items then returns ordered by created_at", "K-1", ["first", "second"]),
    ]
    for scenario, resource_id, expected in cases:
        with subtests.test(msg=scenario):
            items = db.get_atomic_for_resource(resource_id)
            if isinstance(expected, list) and len(expected) > 0:
                assert [i["content"] for i in items] == expected
            else:
                assert items == expected


# ═══════════════════════════════════════════════════════════════
# SkillDB.get_latest_updated_at
# ═══════════════════════════════════════════════════════════════

def test_get_latest_updated_at(subtests, db):
    db.upsert_atomic("jira", "K-1", "c1", "A", "x", "2026-01-01", "2026-01-01")
    db.upsert_atomic("jira", "K-1", "c2", "A", "y", "2026-01-02", "2026-01-05")
    cases = [
        ("When resource does not exist then returns None", "NONE", None),
        ("When resource has items then returns latest updated_at", "K-1", "2026-01-05"),
    ]
    for scenario, rid, expected in cases:
        with subtests.test(msg=scenario):
            assert db.get_latest_updated_at(rid) == expected


# ═══════════════════════════════════════════════════════════════
# SkillDB.has_content_changed
# ═══════════════════════════════════════════════════════════════

def test_has_content_changed(subtests, db):
    db.upsert_atomic("jira", "K-1", "K-1", "A", "x", "2026-01-01", "2026-01-01")
    cases = [
        ("When resource is new then returns True (needs fetch)", "K-NEW", "2026-01-01", True),
        ("When timestamp matches cached then returns False (skip)", "K-1", "2026-01-01", False),
        ("When timestamp is newer than cached then returns True", "K-1", "2026-01-02", True),
    ]
    for scenario, rid, ts, expected in cases:
        with subtests.test(msg=scenario):
            assert db.has_content_changed(rid, ts) == expected


# ═══════════════════════════════════════════════════════════════
# SkillDB.get_all_resource_ids
# ═══════════════════════════════════════════════════════════════

def test_get_all_resource_ids(subtests, db):
    db.upsert_atomic("jira", "K-1", "K-1", "A", "x", "2026-01-01", "2026-01-01")
    db.upsert_atomic("jira", "K-2", "K-2", "A", "y", "2026-01-01", "2026-01-01")
    db.upsert_atomic("gmail", "T-1", "T-1", "A", "z", "2026-01-01", "2026-01-01")
    cases = [
        ("When no source filter then returns all resource IDs", None, {"K-1", "K-2", "T-1"}),
        ("When source=jira then returns only jira resource IDs", "jira", {"K-1", "K-2"}),
        ("When source=gmail then returns only gmail resource IDs", "gmail", {"T-1"}),
    ]
    for scenario, source, expected in cases:
        with subtests.test(msg=scenario):
            assert set(db.get_all_resource_ids(source=source)) == expected


# ═══════════════════════════════════════════════════════════════
# SkillDB.upsert_summary & get_resource_summary
# ═══════════════════════════════════════════════════════════════

def test_upsert_summary(subtests, db):
    cases = [
        ("When getting nonexistent summary then returns None",
         {"rid": "NOPE"},
         {"action": "get", "expected_summary": None}),
        ("When upserting basic summary then stores with defaults",
         {"rid": "K-1", "source": "jira", "title": "Title", "summary": "Summary text"},
         {"action": "upsert_get", "expected_summary": "Summary text",
          "expected_mention": "none", "expected_est_rel": 0, "expected_fin_rel": 0}),
        ("When upserting with relevance fields then stores correctly",
         {"rid": "K-2", "source": "jira", "title": "T", "summary": "S",
          "mention_type": "direct", "estimated_relevance": 8, "final_relevance": 8},
         {"action": "upsert_get", "expected_mention": "direct",
          "expected_est_rel": 8, "expected_fin_rel": 8}),
        ("When final_relevance not specified then defaults to estimated",
         {"rid": "K-3", "source": "jira", "title": "T", "summary": "S",
          "estimated_relevance": 7},
         {"action": "upsert_get", "expected_fin_rel": 7}),
        ("When upserting with metadata then stores JSON entities",
         {"rid": "K-4", "source": "jira", "title": "T", "summary": "S",
          "metadata": {"work_items": ["DPD-1"], "people": ["John"]}},
         {"action": "upsert_get", "expected_meta_keys": {"work_items": ["DPD-1"], "people": ["John"]}}),
        ("When updating existing summary then overwrites values",
         {"rid": "K-1", "source": "jira", "title": "T", "summary": "V2",
          "estimated_relevance": 9},
         {"action": "upsert_get", "expected_summary": "V2", "expected_est_rel": 9}),
    ]
    for scenario, upsert_args, checks in cases:
        with subtests.test(msg=scenario):
            if checks["action"] == "get":
                assert db.get_resource_summary(upsert_args["rid"]) is None
            else:
                rid = upsert_args.pop("rid")
                source = upsert_args.pop("source")
                title = upsert_args.pop("title")
                summary = upsert_args.pop("summary")
                db.upsert_summary(rid, source, title, summary, **upsert_args)
                s = db.get_resource_summary(rid)
                if "expected_summary" in checks:
                    assert s["summary"] == checks["expected_summary"]
                if "expected_mention" in checks:
                    assert s["mention_type"] == checks["expected_mention"]
                if "expected_est_rel" in checks:
                    assert s["estimated_relevance"] == checks["expected_est_rel"]
                if "expected_fin_rel" in checks:
                    assert s["final_relevance"] == checks["expected_fin_rel"]
                if "expected_meta_keys" in checks:
                    m = json.loads(s["metadata"])
                    for k, v in checks["expected_meta_keys"].items():
                        assert m[k] == v


# ═══════════════════════════════════════════════════════════════
# SkillDB.needs_resummarize
# ═══════════════════════════════════════════════════════════════

def test_needs_resummarize(subtests):
    cases = [
        ("When no summary exists then returns True",
         lambda d: d.upsert_atomic("jira", "K-1", "K-1", "A", "x", "2026-01-01", "2026-01-01"),
         True),
        ("When summary is up-to-date then returns False",
         lambda d: (d.upsert_atomic("jira", "K-1", "K-1", "A", "x", "2026-01-01", "2026-01-01"),
                    d.upsert_summary("K-1", "jira", "T", "S")),
         False),
        ("When new content added after summary then returns True",
         lambda d: (d.upsert_atomic("jira", "K-1", "K-1", "A", "x", "2026-01-01", "2026-01-01"),
                    d.upsert_summary("K-1", "jira", "T", "S"),
                    d.upsert_atomic("jira", "K-1", "c2", "A", "new", "2026-01-02", "2099-01-01")),
         True),
    ]
    for scenario, setup, expected in cases:
        with subtests.test(msg=scenario):
            d, path = _make_db()
            setup(d)
            assert d.needs_resummarize("K-1") == expected
            _cleanup_db(d, path)


# ═══════════════════════════════════════════════════════════════
# SkillDB.get_items_since
# ═══════════════════════════════════════════════════════════════

def test_get_items_since(subtests, db):
    db.upsert_atomic("jira", "K-1", "c1", "A", "old", "2026-01-01", "2026-01-01")
    db.upsert_atomic("jira", "K-1", "c2", "A", "new", "2026-01-05", "2026-01-05")
    cases = [
        ("When cutoff is before all items then returns all items", "K-1", "2025-01-01", 2),
        ("When cutoff is between items then returns only newer", "K-1", "2026-01-02", 1),
        ("When cutoff is after all items then returns none", "K-1", "2027-01-01", 0),
    ]
    for scenario, rid, since, expected_count in cases:
        with subtests.test(msg=scenario):
            assert len(db.get_items_since(rid, since)) == expected_count


# ═══════════════════════════════════════════════════════════════
# SkillDB.compute_mention_type
# ═══════════════════════════════════════════════════════════════

def test_compute_mention_type(subtests, db):
    cases = [
        ("When resource does not exist then returns 'none'", [], "none"),
        ("When user is assignee then returns 'direct'",
         [{"iid": "K-1", "author": "Reporter", "content": "C",
           "metadata": {"assignee": "Michael Bui"}}], "direct"),
        ("When user is reporter then returns 'direct'",
         [{"iid": "K-1", "author": "Someone", "content": "C",
           "metadata": {"reporter": "Michael Bui"}}], "direct"),
        ("When user is comment author then returns 'direct'",
         [{"iid": "c1", "author": "Michael Bui", "content": "Comment"}], "direct"),
        ("When user is @mentioned in content then returns 'direct'",
         [{"iid": "c1", "author": "Someone", "content": "Hey @michael bui check this"}], "direct"),
        ("When user name appears in content then returns 'direct'",
         [{"iid": "c1", "author": "Someone", "content": "Assigned to Michael Bui for review"}], "direct"),
        ("When user name is UPPERCASE then returns 'direct' (case insensitive)",
         [{"iid": "K-1", "author": "Someone", "content": "C",
           "metadata": {"assignee": "MICHAEL BUI"}}], "direct"),
        ("When only linked issues exist then returns 'indirect'",
         [{"iid": "K-1", "author": "Someone", "content": "C",
           "metadata": {"linked_issues": [{"type": "blocks", "key": "K-2"}]}}], "indirect"),
        ("When no user signals then returns 'none'",
         [{"iid": "K-1", "author": "Someone", "content": "Unrelated content"}], "none"),
    ]
    for idx, (scenario, items_data, expected) in enumerate(cases):
        with subtests.test(msg=scenario):
            rid = f"MT-{idx}"
            for item in items_data:
                db.upsert_atomic("jira", rid, item["iid"], item.get("author", "Unknown"),
                                 item["content"], "2026-01-01", "2026-01-01",
                                 metadata=item.get("metadata"))
            assert db.compute_mention_type(rid) == expected


def test_compute_mention_type_strongest_wins(subtests, db):
    with subtests.test(msg="When resource has both indirect and direct signals then strongest wins"):
        db.upsert_atomic("jira", "K-SW", "K-SW", "Someone", "Content", "2026-01-01", "2026-01-01",
                         metadata={"linked_issues": [{"type": "x", "key": "K-2"}]})
        db.upsert_atomic("jira", "K-SW", "c1", "Michael Bui", "My comment", "2026-01-02", "2026-01-02")
        assert db.compute_mention_type("K-SW") == "direct"


# ═══════════════════════════════════════════════════════════════
# SkillDB.get_all_summaries
# ═══════════════════════════════════════════════════════════════

def test_get_all_summaries(subtests, db):
    db.upsert_atomic("jira", "K-1", "K-1", "A", "x", "2026-01-01", "2026-01-01")
    db.upsert_atomic("jira", "K-2", "K-2", "A", "x", "2026-01-03", "2026-01-03")
    db.upsert_atomic("gmail", "K-3", "K-3", "A", "x", "2026-01-02", "2026-01-02")
    db.upsert_summary("K-1", "jira", "T", "Low", estimated_relevance=3, final_relevance=3)
    db.upsert_summary("K-2", "jira", "T", "High", estimated_relevance=8, final_relevance=8)
    db.upsert_summary("K-3", "gmail", "T", "Gmail", estimated_relevance=9, final_relevance=9)

    cases = [
        ("When no filters then returns all", {}, 3, None),
        ("When min_relevance=5 then excludes low relevance", {"min_relevance": 5}, 2, None),
        ("When source=jira then returns only jira summaries", {"source": "jira"}, 2, None),
        ("When both filters then applies both", {"source": "jira", "min_relevance": 5}, 1, None),
        ("When since filter then excludes older resources", {"since": "2026-01-02"}, 2, None),
        ("When since filter with min_relevance then applies both",
         {"since": "2026-01-02", "min_relevance": 5}, 2, None),
        ("When results returned then ordered chronologically (oldest first)", {}, 3, ["K-1", "K-3", "K-2"]),
    ]
    for scenario, kwargs, expected_count, expected_order in cases:
        with subtests.test(msg=scenario):
            result = db.get_all_summaries(**kwargs)
            assert len(result) == expected_count
            if expected_order:
                assert [r["resource_id"] for r in result] == expected_order


# ═══════════════════════════════════════════════════════════════
# SkillDB.backfill_mention_types
# ═══════════════════════════════════════════════════════════════

def test_backfill_mention_types(subtests, db):
    db.upsert_atomic("jira", "K-1", "K-1", "Michael Bui", "x", "2026-01-01", "2026-01-01")
    db.upsert_atomic("jira", "K-2", "K-2", "Other", "y", "2026-01-01", "2026-01-01",
                      metadata={"linked_issues": [{"type": "x", "key": "K-3"}]})
    db.upsert_atomic("jira", "K-3", "K-3", "Other", "z", "2026-01-01", "2026-01-01")
    db.upsert_summary("K-1", "jira", "T1", "S1")
    db.upsert_summary("K-2", "jira", "T2", "S2")
    db.upsert_summary("K-3", "jira", "T3", "S3")
    counts = db.backfill_mention_types()

    cases = [
        ("When backfilling direct author then count=1 and mention_type=direct", "K-1", "direct", "direct"),
        ("When backfilling indirect linked then count=1 and mention_type=indirect", "K-2", "indirect", "indirect"),
        ("When backfilling no-signal then count=1 and mention_type=none", "K-3", "none", "none"),
    ]
    for scenario, rid, count_key, expected_mt in cases:
        with subtests.test(msg=scenario):
            assert counts.get(count_key, 0) == 1
            assert db.get_resource_summary(rid)["mention_type"] == expected_mt


# ═══════════════════════════════════════════════════════════════
# SkillDB.clear_all_summaries
# ═══════════════════════════════════════════════════════════════

def test_clear_all_summaries(subtests, db):
    db.upsert_summary("K-1", "jira", "T", "S", mention_type="direct",
                       estimated_relevance=8, final_relevance=8)
    count = db.clear_all_summaries()
    s = db.get_resource_summary("K-1")
    cases = [
        ("When clearing then returns count of cleared summaries", count, 1),
        ("When cleared then summary text is None", s["summary"], None),
        ("When cleared then estimated_relevance is 0", s["estimated_relevance"], 0),
        ("When cleared then mention_type is preserved", s["mention_type"], "direct"),
    ]
    for scenario, actual, expected in cases:
        with subtests.test(msg=scenario):
            assert actual == expected


# ═══════════════════════════════════════════════════════════════
# SkillDB.upsert_relationship / get_relationships / clear_relationships
# ═══════════════════════════════════════════════════════════════

def test_relationships(subtests):
    cases = [
        ("When upserting then retrievable from source side",
         lambda d: d.upsert_relationship("K-1", "K-2", "blocks"), "K-1", 1),
        ("When upserting then retrievable from target side (bidirectional)",
         lambda d: d.upsert_relationship("K-1", "K-2", "blocks"), "K-2", 1),
        ("When upserting duplicate then no duplicates",
         lambda d: (d.upsert_relationship("K-1", "K-2", "blocks"),
                    d.upsert_relationship("K-1", "K-2", "blocks")), "K-1", 1),
        ("When clearing then all removed for resource",
         lambda d: (d.upsert_relationship("K-1", "K-2", "blocks"),
                    d.upsert_relationship("K-1", "K-3", "relates-to"),
                    d.clear_relationships("K-1")), "K-1", 0),
    ]
    for scenario, setup, query_key, expected_count in cases:
        with subtests.test(msg=scenario):
            d, path = _make_db()
            setup(d)
            assert len(d.get_relationships(query_key)) == expected_count
            _cleanup_db(d, path)


# ═══════════════════════════════════════════════════════════════
# SkillDB.delete_resource
# ═══════════════════════════════════════════════════════════════

def test_delete_resource(subtests, db):
    db.upsert_atomic("jira", "K-1", "K-1", "A", "x", "2026-01-01", "2026-01-01")
    db.upsert_summary("K-1", "jira", "T", "S")
    db.upsert_relationship("K-1", "K-2", "blocks")
    db.delete_resource("K-1")

    cases = [
        ("When deleting resource then atomic content is removed",
         lambda: db.get_atomic_for_resource("K-1"), []),
        ("When deleting resource then summary is removed",
         lambda: db.get_resource_summary("K-1"), None),
        ("When deleting resource then relationships are removed",
         lambda: db.get_relationships("K-1"), []),
    ]
    for scenario, get_fn, expected in cases:
        with subtests.test(msg=scenario):
            assert get_fn() == expected


# ═══════════════════════════════════════════════════════════════
# parse_llm_response
# ═══════════════════════════════════════════════════════════════

def _valid_json(**overrides):
    base = {
        "relevance": 8, "summary": "DPD-715: Task assigned.",
        "work_items": ["DPD-715", "PR #649"], "people": ["Nikhil Grover"],
        "labels": ["pricing-migration", "code-review", "task-assignment", "pull-request", "backend-api"],
    }
    base.update(overrides)
    return json.dumps(base)


def test_parse_llm_response(subtests):
    valid = _valid_json()
    cases = [
        ("When response is valid JSON then parses all fields correctly",
         valid, "direct", {"relevance": 8, "work_items_len": 2, "people_len": 1, "labels_len": 5}),
        ("When response has <think> block then strips it and parses",
         f"<think>Let me analyze...</think>{valid}", "direct", {"relevance": 8}),
        ("When response has ```json fences then strips them and parses",
         f"```json\n{valid}\n```", "direct", {"relevance": 8}),
        ("When response has bare ``` fences then strips them and parses",
         f"```\n{valid}\n```", "direct", {"relevance": 8}),
        ("When response has both think block and fences then handles both",
         f"<think>hmm</think>```json\n{valid}\n```", "direct", {"relevance": 8}),
        ("When relevance below direct floor then clamps to 7",
         _valid_json(relevance=3), "direct", {"relevance": 7}),
        ("When relevance below indirect floor then clamps to 5",
         _valid_json(relevance=2), "indirect", {"relevance": 5}),
        ("When mention is 'none' and relevance=1 then no clamping",
         _valid_json(relevance=1), "none", {"relevance": 1}),
        ("When relevance exceeds 10 then clamps to 10",
         _valid_json(relevance=15), "none", {"relevance": 10}),
        ("When labels > 5 then truncates to 5",
         json.dumps({"relevance": 5, "summary": "x", "work_items": [], "people": [],
                     "labels": ["a-b", "c-d", "e-f", "g-h", "i-j", "k-l", "m-n"]}),
         "none", {"relevance": 5, "labels_len": 5}),
        ("When work_items and people keys missing then defaults to empty lists",
         json.dumps({"relevance": 5, "summary": "x", "labels": ["a-b"]}),
         "none", {"work_items_len": 0, "people_len": 0}),
    ]
    for scenario, raw, mention, checks in cases:
        with subtests.test(msg=scenario):
            r = parse_llm_response(raw, mention)
            for key, expected in checks.items():
                if key == "relevance":
                    assert r.relevance == expected
                elif key.endswith("_len"):
                    attr = key[:-4]
                    assert len(getattr(r, attr)) == expected


def test_parse_llm_response_regex_fallback(subtests):
    cases = [
        ("When JSON is invalid but has relevance regex then extracts it",
         'Not JSON but "relevance": 6 and "summary": "Fallback text"', "indirect", 6, "Fallback text"),
        ("When JSON is completely invalid then defaults to relevance=5",
         "Completely invalid text", "none", 5, None),
        ("When regex fallback with direct floor then clamps up",
         'Bad "relevance": 2', "direct", 7, None),
    ]
    for scenario, raw, mention, expected_rel, expected_summary in cases:
        with subtests.test(msg=scenario):
            r = parse_llm_response(raw, mention)
            assert r.relevance == expected_rel
            if expected_summary:
                assert expected_summary in r.summary


def test_summary_result_dataclass_defaults(subtests):
    sr = SummaryResult(relevance=8, summary="Test")
    with subtests.test(msg="When creating SummaryResult without optional fields then lists default to empty"):
        assert sr.work_items == []
        assert sr.people == []
        assert sr.labels == []


# ═══════════════════════════════════════════════════════════════
# _build_system_prompt & _build_user_prompt
# ═══════════════════════════════════════════════════════════════

def test_build_system_prompt(subtests):
    p = _build_system_prompt()
    with subtests.test(msg="When building system prompt then includes user context from User.md"):
        assert "Michael Bui" in p
        assert "relevance-scoring" in p


def test_build_user_prompt(subtests):
    cases = [
        ("When mention_type=direct then word hint is ~200 words",
         "direct", None, ["~200 words"]),
        ("When mention_type=indirect then word hint is ~100 words",
         "indirect", None, ["~100 words"]),
        ("When mention_type=none then word hint is ~30 words",
         "none", None, ["~30 words"]),
        ("When prompt built then contains JSON instruction and relevance floor rules",
         "direct", None, ["JSON", "RELEVANCE FLOOR", "direct mention_type >= 7"]),
        ("When prompt built then contains entity extraction rules",
         "none", None, ["work_items", "people", "5 descriptive 2-word"]),
        ("When existing_summary provided then prompt includes it",
         "direct", "Previous text", ["Existing summary"]),
    ]
    for scenario, mention, existing, expected_substrings in cases:
        with subtests.test(msg=scenario):
            p = _build_user_prompt("T", "Jira", "{}", "c", mention, existing_summary=existing)
            for sub in expected_substrings:
                assert sub in p


def test_load_user_context(subtests):
    with subtests.test(msg="When loading user context then User.md content is returned"):
        assert "Michael Bui" in _load_user_context()


# ═══════════════════════════════════════════════════════════════
# format_issue
# ═══════════════════════════════════════════════════════════════

def test_format_issue(subtests):
    cases = [
        ("When issue has all fields then extracts them correctly",
         _sample_issue(),
         {"key": "DPD-1", "title": "Test Ticket", "assignee": "Michael Bui",
          "reporter": "John Doe", "priority": "High", "issuetype": "Task"}),
        ("When assignee is None then returns None",
         _sample_issue(assignee=None), {"assignee": None}),
        ("When issue has parent then extracts parent key",
         _sample_issue(parent={"key": "EPIC-1", "fields": {"summary": "Epic"}}),
         {"parent_key": "EPIC-1"}),
    ]
    for scenario, raw_issue, checks in cases:
        with subtests.test(msg=scenario):
            result = format_issue(raw_issue)
            for k, v in checks.items():
                if k == "parent_key":
                    assert result["parent"]["key"] == v
                else:
                    assert result[k] == v


def test_format_issue_comments(subtests):
    issue = _sample_issue(comment={
        "comments": [
            {"id": str(i), "created": f"2026-01-{i:02d}", "author": {"displayName": f"P{i}"}, "body": f"C{i}"}
            for i in range(1, 16)
        ]
    })
    result = format_issue(issue)
    with subtests.test(msg="When issue has >10 comments then only latest 10 are kept"):
        assert len(result["comments"]) == 10


def test_format_issue_links(subtests):
    issue = _sample_issue(issuelinks=[
        {"type": {"name": "Blocks"}, "outwardIssue": {"key": "DPD-2"}},
        {"type": {"name": "Relates"}, "inwardIssue": {"key": "DPD-3"}},
    ])
    result = format_issue(issue)
    with subtests.test(msg="When issue has issuelinks then both inward and outward are extracted"):
        assert len(result["links"]) == 2


# ═══════════════════════════════════════════════════════════════
# _build_ticket_metadata
# ═══════════════════════════════════════════════════════════════

def test_build_ticket_metadata(subtests):
    base = {
        "status": {"name": "Done", "category": "Done"},
        "assignee": "Michael", "reporter": "John", "priority": "High",
        "issuetype": "Task", "resolution": "Fixed", "duedate": "2026-06-01",
        "labels": ["x"], "components": ["BE"], "fix_versions": ["v1"],
        "parent": None, "subtasks": [], "links": [],
    }
    cases = [
        ("When issue has no parent then meta excludes parent_key",
         base, lambda m: "parent_key" not in m),
        ("When issue has parent then meta includes parent_key",
         {**base, "parent": {"key": "E-1", "summary": "Epic"}, "subtasks": [{"key": "S-1"}],
          "links": [{"type": "blocks", "key": "K-2"}]},
         lambda m: m["parent_key"] == "E-1" and m["subtask_keys"] == ["S-1"]
                    and m["linked_issues"][0]["key"] == "K-2"),
    ]
    for scenario, issue, check_fn in cases:
        with subtests.test(msg=scenario):
            assert check_fn(_build_ticket_metadata(issue))


# ═══════════════════════════════════════════════════════════════
# cache_issue
# ═══════════════════════════════════════════════════════════════

def test_cache_issue(subtests, db):
    base = {
        "key": "K-1", "title": "Test", "description": "Desc",
        "status": {"name": "Open", "category": "To Do"},
        "assignee": "Michael Bui", "reporter": "John", "priority": "High",
        "issuetype": "Task", "resolution": None, "labels": [], "components": [],
        "fix_versions": [], "duedate": None, "parent": None, "subtasks": [],
        "links": [], "created": "2026-01-01", "updated": "2026-01-01", "comments": [],
    }
    cases = [
        ("When caching without comments then 1 atomic item",
         {**base, "key": "K-1"}, "K-1", 1, None),
        ("When caching with 1 comment then 2 atomic items",
         {**base, "key": "K-2", "comments": [
             {"id": "c1", "created": "2026-01-02", "updated": "2026-01-02",
              "author": "Alice", "body": "Comment body"}]},
         "K-2", 2, None),
        ("When issue has parent then relationship stored",
         {**base, "key": "K-3", "parent": {"key": "EPIC-1", "summary": "Epic"}},
         "K-3", 1, "EPIC-1"),
    ]
    for scenario, issue_data, rid, expected_items, expected_rel_target in cases:
        with subtests.test(msg=scenario):
            cache_issue(db, issue_data)
            items = db.get_atomic_for_resource(rid)
            assert len(items) == expected_items
            if expected_rel_target:
                rels = db.get_relationships(rid)
                assert any(r["target_key"] == expected_rel_target for r in rels)


def test_cache_issue_all_optional_fields(subtests):
    d, path = _make_db()
    issue = {
        "key": "K-5", "title": "Full Issue", "description": "Desc here",
        "status": {"name": "Done", "category": "Done"},
        "assignee": "Michael Bui", "reporter": "John", "priority": "High",
        "issuetype": "Story", "resolution": "Fixed",
        "labels": ["critical", "backend"], "components": ["API", "DB"],
        "fix_versions": ["v2.0"], "duedate": "2026-06-01",
        "parent": {"key": "EPIC-1", "summary": "Epic"},
        "subtasks": [{"key": "K-5a", "summary": "Sub 1"}],
        "links": [{"type": "blocks", "key": "K-6"}],
        "created": "2026-01-01", "updated": "2026-01-05",
        "comments": [
            {"id": "c1", "created": "2026-01-02", "updated": "2026-01-02", "author": "Alice", "body": "Comment 1"},
            {"id": "c2", "created": "2026-01-03", "updated": "2026-01-03", "author": "Bob", "body": "Comment 2"},
        ],
    }
    cache_issue(d, issue)

    expected_substrings = [
        "Labels: critical, backend", "Components: API, DB", "Fix Versions: v2.0",
        "Parent: EPIC-1", "Subtask: K-5a", "Link (blocks): K-6",
        "Resolution: Fixed", "Due: 2026-06-01",
    ]
    with subtests.test(msg="When issue has all optional fields then caches them in content"):
        items = d.get_atomic_for_resource("K-5")
        assert len(items) == 3
        main_content = items[0]["content"]
        for sub in expected_substrings:
            assert sub in main_content

    with subtests.test(msg="When issue has parent/subtasks/links then relationships stored"):
        rels = d.get_relationships("K-5")
        types = {r["relation_type"] for r in rels}
        for t in ("parent", "child", "blocks"):
            assert t in types

    _cleanup_db(d, path)


# ═══════════════════════════════════════════════════════════════
# get_auth_header
# ═══════════════════════════════════════════════════════════════

def test_get_auth_header(subtests):
    header = get_auth_header("user@example.com", "mykey")
    with subtests.test(msg="When generating auth header then includes Authorization key"):
        assert "Authorization" in header
    with subtests.test(msg="When generating auth header then value is Basic auth"):
        assert header["Authorization"].startswith("Basic ")


# ═══════════════════════════════════════════════════════════════
# _build_view_jql
# ═══════════════════════════════════════════════════════════════

def test_build_view_jql(subtests):
    cases = [
        ("When no filters or sort then returns base JQL unchanged",
         ("project = DPD", [], [], None), "project = DPD"),
        ("When filter with single value then adds = clause",
         ("project = DPD", [{"field": {"jiraFieldKey": "status"}, "kind": "FIELD_IDENTITY",
           "values": [{"stringValue": "Done"}]}], [], None), "status = Done"),
        ("When filter is negation then adds != clause",
         ("project = DPD", [{"field": {"jiraFieldKey": "status"}, "kind": "NOT_FIELD_IDENTITY",
           "values": [{"stringValue": "Done"}]}], [], None), "status != Done"),
        ("When filter has multiple values then adds IN clause",
         ("project = DPD", [{"field": {"jiraFieldKey": "status"}, "kind": "FIELD_IDENTITY",
           "values": [{"stringValue": "Open"}, {"stringValue": "In Progress"}]}], [], None),
         "status in (Open, In Progress)"),
        ("When sort fields provided then adds ORDER BY",
         ("project = DPD", [], [{"field": {"jiraFieldKey": "updated"}, "order": "DESC"}], None),
         "ORDER BY updated DESC"),
        ("When sort_mode fallback used then generates ORDER BY from mode",
         ("project = DPD", [], [], "CREATED"), "ORDER BY created DESC"),
        ("When base has existing ORDER BY then strips and replaces",
         ("project = DPD ORDER BY rank ASC", [], [], "UPDATED"), "ORDER BY updated DESC"),
        ("When customfield then converts to cf[] syntax",
         ("project = DPD", [{"field": {"jiraFieldKey": "customfield_12345"}, "kind": "FIELD_IDENTITY",
           "values": [{"numericValue": 42}]}], [], None), "cf[12345] = 42"),
    ]
    for scenario, (base, filters, sort, mode), expected_substring in cases:
        with subtests.test(msg=scenario):
            assert expected_substring in _build_view_jql(base, filters, sort, mode)

    with subtests.test(msg="When base had ORDER BY then old sort is removed"):
        result = _build_view_jql("project = DPD ORDER BY rank ASC", [], [], "UPDATED")
        assert "rank ASC" not in result


def test_build_view_jql_project_rank_mode(subtests):
    with subtests.test(msg="When sort_mode is PROJECT_RANK then uses rank ASC"):
        assert "ORDER BY rank ASC" in _build_view_jql("project = DPD", [], [], "PROJECT_RANK")


def test_build_view_jql_empty_filter_values(subtests):
    filters = [{"field": {"jiraFieldKey": "status"}, "kind": "FIELD_IDENTITY", "values": []}]
    with subtests.test(msg="When filter has empty values then filter is skipped"):
        assert _build_view_jql("project = DPD", filters, [], None) == "project = DPD"


# ═══════════════════════════════════════════════════════════════
# _format_summary_block
# ═══════════════════════════════════════════════════════════════

def test_format_summary_block(subtests, db):
    cases = [
        ("When direct mention then shows Relevance and Mention",
         "K-R", {"mention_type": "direct", "estimated_relevance": 9, "final_relevance": 9},
         None, ["Relevance: 9/10", "Mention: direct"], []),
        ("When mention_type is 'none' then Mention label excluded",
         "K-N", {}, None, [], ["Mention:"]),
        ("When metadata has status/priority then shows them",
         "K-M", {"metadata": {"status": "Done", "status_category": "Done", "priority": "High"}},
         None, ["Status: Done (Done)", "Priority: High"], []),
        ("When relationships exist then shows them",
         "K-L", {}, lambda: db.upsert_relationship("K-L", "K-2", "blocks"),
         ["blocks: K-2"], []),
    ]
    for scenario, rid, kwargs, setup, expected_in, expected_not_in in cases:
        with subtests.test(msg=scenario):
            db.upsert_summary(rid, "jira", "Test", "S", **kwargs)
            if setup:
                setup()
            s = db.get_resource_summary(rid)
            block = _format_summary_block(db, rid, s, 1, 1)
            for sub in expected_in:
                assert sub in block
            for sub in expected_not_in:
                assert sub not in block


def test_format_summary_block_extended(subtests):
    d, path = _make_db()
    meta = {
        "status": "In Progress", "status_category": "In Progress",
        "issuetype": "Story", "priority": "Critical",
        "assignee": "Michael", "reporter": "John",
        "duedate": "2026-06-01", "resolution": "Unresolved",
        "labels": ["backend", "urgent"], "components": ["API"], "fix_versions": ["v2.0"],
    }
    d.upsert_summary("K-E", "jira", "Extended Test", "Summary",
                      metadata=meta, mention_type="indirect",
                      estimated_relevance=6, final_relevance=6)
    s = d.get_resource_summary("K-E")
    block = _format_summary_block(d, "K-E", s, 1, 5)

    cases = [
        ("When summary has labels then shows them", "Labels: backend, urgent"),
        ("When summary has components then shows them", "Components: API"),
        ("When summary has fix_versions then shows them", "Fix Versions: v2.0"),
        ("When summary has type then shows it", "Type: Story"),
        ("When summary has assignee then shows it", "Assignee: Michael"),
        ("When summary has reporter then shows it", "Reporter: John"),
        ("When summary has due date then shows it", "Due: 2026-06-01"),
        ("When summary has resolution then shows it", "Resolution: Unresolved"),
    ]
    for scenario, expected_str in cases:
        with subtests.test(msg=scenario):
            assert expected_str in block
    _cleanup_db(d, path)


# ═══════════════════════════════════════════════════════════════
# write_output
# ═══════════════════════════════════════════════════════════════

def test_write_output(subtests):
    cases = [
        ("When no summaries then creates empty file", False, "", []),
        ("When summaries exist then file contains summary and relevance", True, "Summary text", ["Relevance: 8/10"]),
    ]
    for scenario, setup_data, expected_content, extra_checks in cases:
        with subtests.test(msg=scenario):
            d, path = _make_db()
            if setup_data:
                d.upsert_atomic("jira", "K-1", "K-1", "A", "x", "2026-01-01", "2026-01-01")
                d.upsert_summary("K-1", "jira", "Test", "Summary text",
                                 estimated_relevance=8, final_relevance=8)
            output = Path(tempfile.mktemp(suffix=".md"))
            write_output(d, output)
            content = output.read_text()
            assert expected_content in content
            for check in extra_checks:
                assert check in content
            output.unlink()
            _cleanup_db(d, path)


def test_write_output_file_lifecycle(subtests):
    d, path = _make_db()
    output = Path(tempfile.mktemp(suffix=".md"))
    with subtests.test(msg="When output not yet written then file does not exist"):
        assert not output.exists()
    d.upsert_summary("K-1", "jira", "T", "S", estimated_relevance=5, final_relevance=5)
    write_output(d, output)
    with subtests.test(msg="When write_output called then file is created"):
        assert output.exists()
    output.unlink()
    _cleanup_db(d, path)


def test_write_output_multiple_items_filtering_and_ordering(subtests):
    d, path = _make_db()
    d.upsert_atomic("jira", "K-OLD", "K-OLD", "A", "old", "2025-12-01", "2025-12-01")
    d.upsert_atomic("jira", "K-MID", "K-MID", "A", "mid", "2026-01-15", "2026-01-15")
    d.upsert_atomic("jira", "K-NEW", "K-NEW", "A", "new", "2026-02-01", "2026-02-01")
    d.upsert_atomic("jira", "K-LOW", "K-LOW", "A", "low", "2026-01-20", "2026-01-20")
    d.upsert_summary("K-OLD", "jira", "Old Ticket", "Old summary", estimated_relevance=9, final_relevance=9)
    d.upsert_summary("K-MID", "jira", "Mid Ticket", "Mid summary", estimated_relevance=7, final_relevance=7)
    d.upsert_summary("K-NEW", "jira", "New Ticket", "New summary", estimated_relevance=8, final_relevance=8)
    d.upsert_summary("K-LOW", "jira", "Low Ticket", "Low summary", estimated_relevance=3, final_relevance=3)

    cases = [
        ("When min_relevance=6 then excludes K-LOW (rel=3)",
         {"min_relevance": 6, "since": None},
         {"present": ["Old summary", "Mid summary", "New summary"], "absent": ["Low summary"]}),
        ("When since=2026-01-01 then excludes K-OLD (2025-12-01)",
         {"min_relevance": 1, "since": "2026-01-01"},
         {"present": ["Mid summary", "New summary", "Low summary"], "absent": ["Old summary"]}),
        ("When both filters then only K-MID and K-NEW remain",
         {"min_relevance": 6, "since": "2026-01-01"},
         {"present": ["Mid summary", "New summary"], "absent": ["Old summary", "Low summary"]}),
        ("When no filters then all items included in chronological order (oldest first)",
         {"min_relevance": 1, "since": None},
         {"present": ["Old summary", "Mid summary", "New summary", "Low summary"], "absent": []}),
    ]
    for scenario, kwargs, checks in cases:
        with subtests.test(msg=scenario):
            output = Path(tempfile.mktemp(suffix=".md"))
            write_output(d, output, **kwargs)
            content = output.read_text()
            for s in checks["present"]:
                assert s in content
            for s in checks["absent"]:
                assert s not in content
            output.unlink()

    with subtests.test(msg="When output generated then oldest items appear first"):
        output = Path(tempfile.mktemp(suffix=".md"))
        write_output(d, output, min_relevance=1)
        content = output.read_text()
        assert content.index("Old summary") < content.index("Mid summary")
        assert content.index("Mid summary") < content.index("New summary")
        output.unlink()

    _cleanup_db(d, path)


# ═══════════════════════════════════════════════════════════════
# _Pipeline (with mocked LLM)
# ═══════════════════════════════════════════════════════════════

@patch("jira._call_llm")
def test_pipeline(mock_llm, subtests):
    cases = [
        ("When LLM succeeds then no errors and summary stored",
         json.dumps({"relevance": 8, "summary": "Test summary",
                     "work_items": ["K-1"], "people": ["Alice"],
                     "labels": ["a-b", "c-d", "e-f", "g-h", "i-j"]}),
         None, 0, 8),
        ("When LLM fails then error captured in errors list",
         None, RuntimeError("LLM down"), 1, None),
    ]
    for scenario, llm_return, llm_error, expected_errors, expected_rel in cases:
        with subtests.test(msg=scenario):
            d, path = _make_db()
            d.upsert_atomic("jira", "K-1", "K-1", "Reporter",
                            "Title: Test\nStatus: Open (To Do)",
                            "2026-01-01", "2026-01-01",
                            metadata={"status": "Open", "status_category": "To Do"})
            if llm_error:
                mock_llm.side_effect = llm_error
            else:
                mock_llm.side_effect = None
                mock_llm.return_value = llm_return
            pipeline = _Pipeline(d, force=True)
            pipeline.set_total(1)
            pipeline.put("K-1")
            errors = pipeline.finish()
            assert len(errors) == expected_errors
            if expected_rel is not None:
                s = d.get_resource_summary("K-1")
                assert s is not None
                assert s["estimated_relevance"] == expected_rel
            _cleanup_db(d, path)


# ═══════════════════════════════════════════════════════════════
# Relevance Constants
# ═══════════════════════════════════════════════════════════════

def test_relevance_floors(subtests):
    cases = [
        ("When mention is direct then floor is 7", "direct", 7),
        ("When mention is indirect then floor is 5", "indirect", 5),
        ("When mention is none then floor is 1", "none", 1),
    ]
    for scenario, key, expected in cases:
        with subtests.test(msg=scenario):
            assert _RELEVANCE_FLOORS[key] == expected


def test_word_hints(subtests):
    cases = [
        ("When mention is direct then hint is 200 words", "direct", 200),
        ("When mention is indirect then hint is 100 words", "indirect", 100),
        ("When mention is none then hint is 30 words", "none", 30),
    ]
    for scenario, key, expected in cases:
        with subtests.test(msg=scenario):
            assert _WORD_HINTS[key] == expected


# ═══════════════════════════════════════════════════════════════
# _default_lookback_days
# ═══════════════════════════════════════════════════════════════

def test_default_lookback_days(subtests):
    cases = [
        ("When called then always returns 14", 14),
    ]
    for scenario, expected in cases:
        with subtests.test(msg=scenario):
            assert _default_lookback_days() == expected


# ═══════════════════════════════════════════════════════════════
# log function
# ═══════════════════════════════════════════════════════════════

def test_log(subtests):
    import io
    with patch("sys.stdout", new_callable=io.StringIO) as mock_out:
        log("test message")
        output = mock_out.getvalue()
        with subtests.test(msg="When log is called then message appears on stdout"):
            assert "test message" in output
        with subtests.test(msg="When log is called then timestamp bracket is present"):
            assert "[" in output


# ═══════════════════════════════════════════════════════════════
# summarize_resource (with mocked LLM)
# ═══════════════════════════════════════════════════════════════

@patch("jira._call_llm")
def test_summarize_resource(mock_llm, subtests):
    mock_llm.return_value = json.dumps({
        "relevance": 9, "summary": "Critical bug fix needed",
        "work_items": ["DPD-100"], "people": ["Alice"],
        "labels": ["bug-fix", "critical-path", "api-error", "prod-issue", "urgent-deploy"],
    })
    items = [{"author": "Alice", "created_at": "2026-01-01", "content": "Bug description here"}]
    cases = [
        ("When items provided then calls LLM and returns structured result", items, "direct", 9),
        ("When mention_type is none then relevance floor is 1", items, "none", 9),
    ]
    for scenario, test_items, mention, expected_rel in cases:
        with subtests.test(msg=scenario):
            r = summarize_resource("DPD-100: Bug", "Jira ticket", test_items,
                                   metadata={"status": "Open"}, mention_type=mention)
            assert r.relevance == expected_rel
            assert "bug fix" in r.summary.lower()


def test_summarize_resource_empty_items(subtests):
    cases = [
        ("When no items and no existing summary then returns floor relevance with empty summary",
         "direct", None, 7, ""),
        ("When no items but existing summary then returns floor relevance with existing text",
         "indirect", "Prev text", 5, "Prev text"),
    ]
    for scenario, mention, existing, expected_rel, expected_summary in cases:
        with subtests.test(msg=scenario):
            r = summarize_resource("K-1", "Jira", [], mention_type=mention, existing_summary=existing)
            assert r.relevance == expected_rel
            assert r.summary == expected_summary


# ═══════════════════════════════════════════════════════════════
# _call_llm (mocked HTTP)
# ═══════════════════════════════════════════════════════════════

@patch("jira.requests.post")
def test_call_llm(mock_post, subtests):
    cases = [
        ("When API returns 200 then returns content",
         200, {"choices": [{"message": {"content": '{"relevance":5}'}}]}, '{"relevance":5}'),
    ]
    for scenario, status, resp_json, expected in cases:
        with subtests.test(msg=scenario):
            mock_resp = MagicMock()
            mock_resp.status_code = status
            mock_resp.json.return_value = resp_json
            mock_post.return_value = mock_resp
            assert _call_llm("sys", "user") == expected


@patch("jira.requests.post")
def test_call_llm_api_key_handling(mock_post, subtests):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"choices": [{"message": {"content": '{"r":1}'}}]}
    mock_post.return_value = mock_resp
    cases = [
        ("When LITELLM_API_KEY is empty then no Authorization header", "", False),
        ("When LITELLM_API_KEY is set then Authorization header included", "test-key-123", True),
    ]
    for scenario, api_key, expect_auth in cases:
        with subtests.test(msg=scenario):
            mock_post.reset_mock()
            with patch("jira.LITELLM_API_KEY", api_key):
                _call_llm("sys", "user")
            call_headers = mock_post.call_args[1]["headers"]
            if expect_auth:
                assert "Authorization" in call_headers
                assert call_headers["Authorization"] == f"Bearer {api_key}"
            else:
                assert "Authorization" not in call_headers


@patch("jira.requests.post")
@patch("jira.SUMMARIZE_RETRIES", 0)
def test_call_llm_errors(mock_post, subtests):
    cases = [
        ("When API returns 400 then raises RuntimeError", 400, "Bad request"),
        ("When API returns empty content then raises RuntimeError", 200, None),
    ]
    for scenario, status, text_or_none in cases:
        with subtests.test(msg=scenario):
            mock_resp = MagicMock()
            mock_resp.status_code = status
            mock_resp.text = text_or_none or ""
            if status == 200:
                mock_resp.json.return_value = {"choices": [{"message": {"content": ""}}]}
            mock_post.return_value = mock_resp
            with pytest.raises(RuntimeError):
                _call_llm("sys", "user")


@patch("jira.requests.post")
@patch("jira.SUMMARIZE_RETRIES", 1)
@patch("jira.SUMMARIZE_RETRY_INITIAL_SEC", 0.01)
def test_call_llm_retries_on_5xx(mock_post, subtests):
    err_resp = MagicMock(); err_resp.status_code = 503; err_resp.text = "Service Unavailable"
    ok_resp = MagicMock(); ok_resp.status_code = 200
    ok_resp.json.return_value = {"choices": [{"message": {"content": "ok"}}]}
    mock_post.side_effect = [err_resp, ok_resp]
    with subtests.test(msg="When first call returns 5xx then retries and succeeds on second attempt"):
        assert _call_llm("sys", "user") == "ok"


@patch("jira.requests.post")
@patch("jira.SUMMARIZE_RETRIES", 1)
@patch("jira.SUMMARIZE_RETRY_INITIAL_SEC", 0.01)
def test_call_llm_retries_on_connection_error(mock_post, subtests):
    import requests as req
    ok_resp = MagicMock(); ok_resp.status_code = 200
    ok_resp.json.return_value = {"choices": [{"message": {"content": "recovered"}}]}
    mock_post.side_effect = [req.ConnectionError("fail"), ok_resp]
    with subtests.test(msg="When connection error then retries and succeeds"):
        assert _call_llm("sys", "user") == "recovered"


@patch("jira.requests.post")
@patch("jira.SUMMARIZE_RETRIES", 1)
@patch("jira.SUMMARIZE_RETRY_INITIAL_SEC", 0.001)
def test_call_llm_exhausts_connection_retries(mock_post, subtests):
    import requests as req
    mock_post.side_effect = req.ConnectionError("persistent failure")
    with subtests.test(msg="When all connection retries exhausted then raises RuntimeError"):
        with pytest.raises(RuntimeError):
            _call_llm("sys", "user")


@patch("jira.requests.post")
@patch("jira.SUMMARIZE_RETRIES", 1)
@patch("jira.SUMMARIZE_RETRY_INITIAL_SEC", 0.001)
def test_call_llm_exhausts_5xx_retries(mock_post, subtests):
    err_resp = MagicMock(); err_resp.status_code = 503; err_resp.text = "Service Unavailable"
    mock_post.return_value = err_resp
    with subtests.test(msg="When all 5xx retries exhausted then raises RuntimeError"):
        with pytest.raises(RuntimeError):
            _call_llm("sys", "user")


# ═══════════════════════════════════════════════════════════════
# validate_env
# ═══════════════════════════════════════════════════════════════

@patch.dict(os.environ, {"JIRA_EMAIL": "a@b.com", "JIRA_API_KEY": "secret123"})
def test_validate_env_success(subtests):
    email, key = validate_env()
    with subtests.test(msg="When env vars set then returns email"):
        assert email == "a@b.com"
        assert key == "secret123"


def test_validate_env_missing(subtests):
    env_backup = {}
    for k in ("JIRA_EMAIL", "JIRA_API_KEY"):
        if k in os.environ:
            env_backup[k] = os.environ.pop(k)
    try:
        with subtests.test(msg="When env vars missing then exits"):
            with pytest.raises(SystemExit):
                validate_env()
    finally:
        os.environ.update(env_backup)


# ═══════════════════════════════════════════════════════════════
# _load_user_context edge case
# ═══════════════════════════════════════════════════════════════

@patch("jira._USER_MD_PATH", Path("/nonexistent/User.md"))
@patch("jira._USER_CONTEXT", None)
def test_load_user_context_missing_file(subtests):
    import jira
    original = jira._USER_CONTEXT
    jira._USER_CONTEXT = None
    try:
        with subtests.test(msg="When User.md does not exist then returns empty string"):
            assert _load_user_context() == ""
    finally:
        jira._USER_CONTEXT = original


# ═══════════════════════════════════════════════════════════════
# _summarize_one (with mocked LLM)
# ═══════════════════════════════════════════════════════════════

@patch("jira._call_llm")
def test_summarize_one(mock_llm, subtests):
    cases = [
        ("When new resource then stores summary with relevance",
         lambda: _setup_summarize_new(),
         json.dumps({"relevance": 8, "summary": "New summary",
                     "work_items": ["K-1"], "people": [],
                     "labels": ["a-b", "c-d", "e-f", "g-h", "i-j"]}),
         None, {"expected_rel": 8, "expected_summary_contains": "New summary"}),
        ("When already summarized and not stale then skips LLM",
         lambda: _setup_summarize_cached(),
         None, None, {"llm_not_called": True}),
        ("When LLM returns empty summary then raises RuntimeError",
         lambda: _setup_summarize_empty(),
         json.dumps({"relevance": 5, "summary": "", "work_items": [], "people": [], "labels": []}),
         None, {"raises": RuntimeError}),
        ("When new content added then re-summarizes incrementally",
         lambda: _setup_summarize_incremental(),
         json.dumps({"relevance": 9, "summary": "Updated summary with new info",
                     "work_items": [], "people": [],
                     "labels": ["a-b", "c-d", "e-f", "g-h", "i-j"]}),
         None, {"expected_rel": 9, "expected_summary_contains": "Updated summary"}),
        ("When no atomic items then no summary created",
         lambda: _setup_summarize_no_items(),
         None, None, {"expected_none": True}),
    ]
    for scenario, setup_fn, llm_return, llm_error, checks in cases:
        with subtests.test(msg=scenario):
            mock_llm.reset_mock()
            mock_llm.side_effect = None
            if llm_return:
                mock_llm.return_value = llm_return
            if llm_error:
                mock_llm.side_effect = llm_error
            d, path, key, force = setup_fn()
            try:
                if "raises" in checks:
                    with pytest.raises(checks["raises"]):
                        _summarize_one(d, key, force=force, current=1, total=1)
                else:
                    _summarize_one(d, key, force=force, current=1, total=1)
                    if checks.get("llm_not_called"):
                        mock_llm.assert_not_called()
                    elif checks.get("expected_none"):
                        assert d.get_resource_summary(key) is None
                    else:
                        s = d.get_resource_summary(key)
                        assert s is not None
                        if "expected_rel" in checks:
                            assert s["estimated_relevance"] == checks["expected_rel"]
                        if "expected_summary_contains" in checks:
                            assert checks["expected_summary_contains"] in s["summary"]
            finally:
                _cleanup_db(d, path)


def _setup_summarize_new():
    d, path = _make_db()
    d.upsert_atomic("jira", "K-1", "K-1", "Reporter",
                    "Title: Test\nStatus: Open (To Do)",
                    "2026-01-01", "2026-01-01",
                    metadata={"status": "Open", "status_category": "To Do"})
    return d, path, "K-1", True

def _setup_summarize_cached():
    d, path = _make_db()
    d.upsert_atomic("jira", "K-1", "K-1", "A", "Title: T", "2026-01-01", "2026-01-01")
    d.upsert_summary("K-1", "jira", "T", "Existing", estimated_relevance=7, final_relevance=7)
    return d, path, "K-1", False

def _setup_summarize_empty():
    d, path = _make_db()
    d.upsert_atomic("jira", "K-1", "K-1", "A", "Title: T", "2026-01-01", "2026-01-01")
    return d, path, "K-1", True

def _setup_summarize_incremental():
    d, path = _make_db()
    d.upsert_atomic("jira", "K-1", "K-1", "A",
                    "Title: T\nStatus: Open (To Do)", "2026-01-01", "2026-01-01")
    d.upsert_summary("K-1", "jira", "T", "Old summary",
                     estimated_relevance=5, final_relevance=5)
    d.upsert_atomic("jira", "K-1", "c2", "B", "New comment", "2026-06-01", "2099-01-01")
    return d, path, "K-1", False

def _setup_summarize_no_items():
    d, path = _make_db()
    return d, path, "EMPTY-KEY", True


# ═══════════════════════════════════════════════════════════════
# _request (mocked HTTP)
# ═══════════════════════════════════════════════════════════════

@patch("jira.requests.request")
def test_request_success(mock_req, subtests):
    mock_resp = MagicMock(); mock_resp.status_code = 200
    mock_req.return_value = mock_resp
    with subtests.test(msg="When request succeeds then returns response"):
        assert _request("GET", "http://example.com").status_code == 200


@patch("jira.requests.request")
def test_request_auth_failure(mock_req, subtests):
    mock_resp = MagicMock(); mock_resp.status_code = 401
    mock_req.return_value = mock_resp
    with subtests.test(msg="When request returns 401 then exits"):
        with pytest.raises(SystemExit):
            _request("GET", "http://example.com")


@patch("jira.requests.request")
def test_request_not_found(mock_req, subtests):
    mock_resp = MagicMock(); mock_resp.status_code = 404
    mock_req.return_value = mock_resp
    with subtests.test(msg="When request returns 404 then exits"):
        with pytest.raises(SystemExit):
            _request("GET", "http://example.com")


@patch("jira.requests.request")
def test_request_timeout_retries(mock_req, subtests):
    import requests as req
    mock_req.side_effect = [req.exceptions.Timeout("t"), req.exceptions.Timeout("t"), req.exceptions.Timeout("t")]
    with subtests.test(msg="When request times out after retries then exits"):
        with pytest.raises(SystemExit):
            _request("GET", "http://example.com", retries=3)


@patch("jira.requests.request")
def test_request_connection_error(mock_req, subtests):
    import requests as req
    mock_req.side_effect = req.exceptions.ConnectionError("down")
    with subtests.test(msg="When connection error then exits"):
        with pytest.raises(SystemExit):
            _request("GET", "http://example.com")


# ═══════════════════════════════════════════════════════════════
# fetch_issues (mocked HTTP)
# ═══════════════════════════════════════════════════════════════

@patch("jira._request")
def test_fetch_issues(mock_req, subtests):
    cases = [
        ("When API returns issues then returns parsed list and total", {"issues": [{"key": "K-1"}], "total": 1}, 1, 1),
        ("When API returns empty then returns empty list", {"issues": [], "total": 0}, 0, 0),
    ]
    for scenario, resp_json, expected_len, expected_total in cases:
        with subtests.test(msg=scenario):
            mock_resp = MagicMock(); mock_resp.status_code = 200
            mock_resp.json.return_value = resp_json
            mock_req.return_value = mock_resp
            issues, total = fetch_issues("project=X", 10, 0, {})
            assert len(issues) == expected_len
            assert total == expected_total


@patch("jira._request")
def test_fetch_issues_errors(mock_req, subtests):
    cases = [
        ("When API returns 400 then exits with error", 400, {"errorMessages": ["Bad JQL"]}),
        ("When API returns 500 then exits with error", 500, {}),
    ]
    for scenario, status, resp_json in cases:
        with subtests.test(msg=scenario):
            mock_resp = MagicMock(); mock_resp.status_code = status
            mock_resp.json.return_value = resp_json
            mock_req.return_value = mock_resp
            with pytest.raises(SystemExit):
                fetch_issues("bad jql", 10, 0, {})


# ═══════════════════════════════════════════════════════════════
# fetch_filter_jql (mocked HTTP)
# ═══════════════════════════════════════════════════════════════

@patch("jira._request")
def test_fetch_filter_jql(mock_req, subtests):
    mock_resp = MagicMock(); mock_resp.status_code = 200
    mock_resp.json.return_value = {"name": "My Filter", "jql": "project = DPD"}
    mock_req.return_value = mock_resp
    name, jql = fetch_filter_jql("13811", {})
    with subtests.test(msg="When filter API succeeds then returns name"):
        assert name == "My Filter" and jql == "project = DPD"


@patch("jira._request")
def test_fetch_filter_jql_api_error(mock_req, subtests):
    mock_resp = MagicMock(); mock_resp.status_code = 403
    mock_req.return_value = mock_resp
    with subtests.test(msg="When filter API returns 403 then exits"):
        with pytest.raises(SystemExit):
            fetch_filter_jql("999", {})


@patch("jira._request")
def test_fetch_filter_jql_empty_jql(mock_req, subtests):
    mock_resp = MagicMock(); mock_resp.status_code = 200
    mock_resp.json.return_value = {"name": "Empty", "jql": ""}
    mock_req.return_value = mock_resp
    with subtests.test(msg="When filter has empty JQL then exits"):
        with pytest.raises(SystemExit):
            fetch_filter_jql("999", {})


# ═══════════════════════════════════════════════════════════════
# resolve_view_to_jql (mocked HTTP)
# ═══════════════════════════════════════════════════════════════

@patch("jira._request")
@patch("jira._get_cached_view_jql", return_value=None)
@patch("jira._set_cached_view_jql")
def test_resolve_view_to_jql_success(mock_set, mock_get, mock_req, subtests):
    mock_resp = MagicMock(); mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "data": {"polarisView": {
            "jql": "project = DPD", "userJql": None, "name": "Board",
            "sortMode": None, "sort": [], "filter": [],
        }}
    }
    mock_req.return_value = mock_resp
    with subtests.test(msg="When GraphQL returns view then extracts JQL"):
        assert resolve_view_to_jql("12345", {}, use_cache=False) == "project = DPD"


@patch("jira._get_cached_view_jql", return_value="cached = JQL")
def test_resolve_view_to_jql_cached(mock_get, subtests):
    with subtests.test(msg="When cache hit then returns cached JQL without API call"):
        assert resolve_view_to_jql("12345", {}, use_cache=True) == "cached = JQL"


@patch("jira._request")
@patch("jira._get_cached_view_jql", return_value=None)
def test_resolve_view_to_jql_not_found(mock_get, mock_req, subtests):
    mock_resp = MagicMock(); mock_resp.status_code = 200
    mock_resp.json.return_value = {"data": {"polarisView": None}}
    mock_req.return_value = mock_resp
    with subtests.test(msg="When view not found then exits"):
        with pytest.raises(SystemExit):
            resolve_view_to_jql("99999", {}, use_cache=False)


@patch("jira._request")
@patch("jira._get_cached_view_jql", return_value=None)
def test_resolve_view_to_jql_graphql_error(mock_get, mock_req, subtests):
    mock_resp = MagicMock(); mock_resp.status_code = 500
    mock_req.return_value = mock_resp
    with subtests.test(msg="When GraphQL returns 500 then exits"):
        with pytest.raises(SystemExit):
            resolve_view_to_jql("12345", {}, use_cache=False)


# ═══════════════════════════════════════════════════════════════
# View cache helpers
# ═══════════════════════════════════════════════════════════════

def test_view_cache_roundtrip(subtests, tmp_path):
    cache_file = tmp_path / "cache.json"
    with patch("jira.VIEW_CACHE_FILE", cache_file):
        _set_cached_view_jql("123", "project = X")
        with subtests.test(msg="When JQL is cached then get returns it"):
            assert _get_cached_view_jql("123") == "project = X"


def test_view_cache_miss(subtests):
    with patch("jira.VIEW_CACHE_FILE", Path("/nonexistent/cache.json")):
        with subtests.test(msg="When cache file does not exist then returns None"):
            assert _get_cached_view_jql("999") is None


def test_view_cache_corrupted_read(subtests, tmp_path):
    corrupt_file = tmp_path / "corrupt.json"
    corrupt_file.write_text("not valid json{{{")
    with patch("jira.VIEW_CACHE_FILE", corrupt_file):
        with subtests.test(msg="When cache file is corrupt then returns None gracefully"):
            assert _get_cached_view_jql("123") is None


def test_view_cache_write_to_readonly(subtests):
    with patch("jira.VIEW_CACHE_FILE", Path("/nonexistent/deep/dir/cache.json")):
        with subtests.test(msg="When writing to readonly path then no error"):
            _set_cached_view_jql("123", "project = X")


def test_view_cache_write_existing_file(subtests, tmp_path):
    cache_file = tmp_path / "existing.json"
    cache_file.write_text('{"old": {"jql": "OLD", "ts": 0}}')
    with patch("jira.VIEW_CACHE_FILE", cache_file):
        _set_cached_view_jql("new_id", "project = NEW")
        with subtests.test(msg="When cache file exists then appends new entry"):
            assert _get_cached_view_jql("new_id") == "project = NEW"


# ═══════════════════════════════════════════════════════════════
# main() function (integration with mocked externals)
# ═══════════════════════════════════════════════════════════════

def _make_main_db():
    fd, db_path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    os.unlink(db_path)
    return db_path

def _cleanup_main(output_path, db_path):
    if output_path.exists():
        output_path.unlink()
    for s in ("", "-wal", "-shm"):
        p = db_path + s
        if os.path.exists(p):
            os.unlink(p)


@patch("jira.resolve_view_to_jql", return_value="project = DPD")
@patch("jira.fetch_filter_jql", return_value=("My Filter", "project = DPD"))
@patch("jira.fetch_issues", return_value=([_sample_issue()], 1))
@patch("jira.validate_env", return_value=("a@b.com", "key"))
@patch("jira._call_llm")
def test_main_full_flow(mock_llm, mock_env, mock_fetch, mock_filter, mock_view, subtests):
    mock_llm.return_value = json.dumps({
        "relevance": 8, "summary": "Main test summary",
        "work_items": ["DPD-1"], "people": ["John"],
        "labels": ["a-b", "c-d", "e-f", "g-h", "i-j"],
    })
    output_path = Path(tempfile.mktemp(suffix=".md"))
    db_path = _make_main_db()
    _real_open_db = open_db
    def _patched(**kwargs):
        return _real_open_db(db_path, **kwargs)
    try:
        with patch("sys.argv", ["jira.py", "--output", str(output_path), "--days", "365"]), \
             patch("jira.open_db", side_effect=_patched):
            main()
        with subtests.test(msg="When main completes successfully then output file is created"):
            assert output_path.exists()
            assert "Main test summary" in output_path.read_text()
    finally:
        _cleanup_main(output_path, db_path)


@patch("jira.validate_env", return_value=("a@b.com", "key"))
@patch("jira.fetch_filter_jql", return_value=("F", "p = X"))
@patch("jira.resolve_view_to_jql", return_value="p = X")
@patch("jira.fetch_issues", return_value=([], 0))
def test_main_no_issues(mock_fetch, mock_view, mock_filter, mock_env, subtests):
    output_path = Path(tempfile.mktemp(suffix=".md"))
    db_path = _make_main_db()
    _real_open_db = open_db
    def _patched(**kwargs):
        return _real_open_db(db_path, **kwargs)
    try:
        with patch("sys.argv", ["jira.py", "--output", str(output_path), "--days", "365"]), \
             patch("jira.open_db", side_effect=_patched):
            main()
        with subtests.test(msg="When no issues found then output file still created (empty)"):
            assert output_path.exists()
    finally:
        _cleanup_main(output_path, db_path)


@patch("jira._call_llm")
def test_main_force_resummarizes_without_fetch(mock_llm, subtests):
    mock_llm.return_value = json.dumps({
        "relevance": 7, "summary": "Force re-summary",
        "work_items": ["K-1"], "people": ["Alice"],
        "labels": ["a-b", "c-d", "e-f", "g-h", "i-j"],
    })
    output_path = Path(tempfile.mktemp(suffix=".md"))
    db_path = _make_main_db()
    _real_open_db = open_db
    def _patched(**kwargs):
        return _real_open_db(db_path, **kwargs)
    try:
        d = open_db(db_path)
        d.upsert_atomic("jira", "K-1", "K-1", "Alice", "content", "2026-01-01", "2026-01-01")
        d.upsert_summary("K-1", "jira", "Title", "Old summary", estimated_relevance=5, final_relevance=5)
        d.close()
        with patch("sys.argv", ["jira.py", "--output", str(output_path), "--force", "--days", "365"]), \
             patch("jira.open_db", side_effect=_patched), \
             patch("jira.validate_env") as mock_env:
            main()
            mock_env.assert_not_called()
        with subtests.test(msg="When --force then output created from re-summarized cached data"):
            assert output_path.exists()
            assert "Force re-summary" in output_path.read_text()
    finally:
        _cleanup_main(output_path, db_path)


def test_main_cached_only(subtests):
    output_path = Path(tempfile.mktemp(suffix=".md"))
    db_path = _make_main_db()
    try:
        d = open_db(db_path)
        d.upsert_atomic("jira", "K-1", "K-1", "A", "x", "2026-01-01", "2026-01-01")
        d.upsert_summary("K-1", "jira", "T", "Cached summary", estimated_relevance=7, final_relevance=7)
        d.close()
        _real_open_db = open_db
        def _patched(**kwargs):
            return _real_open_db(db_path, **kwargs)
        with patch("sys.argv", ["jira.py", "--cached-only", "--output", str(output_path), "--days", "365"]), \
             patch("jira.open_db", side_effect=_patched):
            main()
        with subtests.test(msg="When --cached-only then output is generated from DB without API calls"):
            assert output_path.exists()
            assert "Cached summary" in output_path.read_text()
    finally:
        _cleanup_main(output_path, db_path)


def test_main_deletes_stale_output(subtests):
    output_path = Path(tempfile.mktemp(suffix=".md"))
    db_path = _make_main_db()
    output_path.write_text("STALE")
    try:
        d = open_db(db_path); d.close()
        _real_open_db = open_db
        def _patched(**kwargs):
            return _real_open_db(db_path, **kwargs)
        with patch("sys.argv", ["jira.py", "--cached-only", "--output", str(output_path), "--days", "365"]), \
             patch("jira.open_db", side_effect=_patched):
            main()
        with subtests.test(msg="When stale output exists then it is replaced"):
            assert "STALE" not in output_path.read_text()
    finally:
        _cleanup_main(output_path, db_path)


def test_main_jql_argument(subtests):
    output_path = Path(tempfile.mktemp(suffix=".md"))
    db_path = _make_main_db()
    _real_open_db = open_db
    def _patched(**kwargs):
        return _real_open_db(db_path, **kwargs)
    try:
        with patch("sys.argv", ["jira.py", "--jql", "project=X", "--filter-id", "",
                                "--view-id", "", "--output", str(output_path), "--days", "365"]), \
             patch("jira.open_db", side_effect=_patched), \
             patch("jira.validate_env", return_value=("a@b.com", "key")), \
             patch("jira.fetch_issues", return_value=([], 0)):
            main()
        with subtests.test(msg="When --jql provided then runs with JQL source"):
            assert output_path.exists()
    finally:
        _cleanup_main(output_path, db_path)


def test_main_no_sources(subtests):
    output_path = Path(tempfile.mktemp(suffix=".md"))
    db_path = _make_main_db()
    _real_open_db = open_db
    def _patched(**kwargs):
        return _real_open_db(db_path, **kwargs)
    try:
        with patch("sys.argv", ["jira.py", "--filter-id", "", "--view-id", "",
                                "--output", str(output_path), "--days", "365"]), \
             patch("jira.open_db", side_effect=_patched), \
             patch("jira.validate_env", return_value=("a@b.com", "key")):
            main()
        with subtests.test(msg="When no sources provided then no output file created"):
            assert not output_path.exists()
    finally:
        _cleanup_main(output_path, db_path)


@patch("jira.resolve_view_to_jql", return_value="project = DPD")
@patch("jira.fetch_filter_jql", return_value=("My Filter", "project = DPD"))
@patch("jira.fetch_issues")
@patch("jira.validate_env", return_value=("a@b.com", "key"))
@patch("jira._call_llm")
def test_main_unchanged_tickets(mock_llm, mock_env, mock_fetch, mock_filter, mock_view, subtests):
    mock_llm.return_value = json.dumps({
        "relevance": 7, "summary": "Unchanged summary",
        "work_items": ["K-1"], "people": ["Alice"],
        "labels": ["a-b", "c-d", "e-f", "g-h", "i-j"],
    })
    output_path = Path(tempfile.mktemp(suffix=".md"))
    db_path = _make_main_db()
    _real_open_db = open_db
    def _patched(**kwargs):
        return _real_open_db(db_path, **kwargs)
    try:
        d = open_db(db_path)
        d.upsert_atomic("jira", "K-1", "K-1", "Alice", "content", "2026-01-01", "2026-01-01")
        d.upsert_summary("K-1", "jira", "Title", "Old", estimated_relevance=5, final_relevance=5)
        d.close()
        mock_fetch.return_value = ([{
            "key": "K-1",
            "fields": {"summary": "Title", "updated": "2026-01-01T00:00:00.000+0000"},
        }], 1)
        with patch("sys.argv", ["jira.py", "--output", str(output_path), "--days", "365"]), \
             patch("jira.open_db", side_effect=_patched):
            main()
        with subtests.test(msg="When ticket unchanged then still included in output via pipeline"):
            assert output_path.exists()
    finally:
        _cleanup_main(output_path, db_path)


@patch("jira.validate_env", side_effect=RuntimeError("No env"))
def test_main_exception_handler(mock_env, subtests):
    output_path = Path(tempfile.mktemp(suffix=".md"))
    db_path = _make_main_db()
    _real_open_db = open_db
    def _patched(**kwargs):
        return _real_open_db(db_path, **kwargs)
    try:
        with patch("sys.argv", ["jira.py", "--output", str(output_path), "--days", "365"]), \
             patch("jira.open_db", side_effect=_patched):
            with pytest.raises(RuntimeError):
                main()
        with subtests.test(msg="When main fails with exception then no output file created"):
            assert not output_path.exists()
    finally:
        _cleanup_main(output_path, db_path)
