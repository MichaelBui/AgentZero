#!/usr/bin/env python3
"""
BDD-style test-table unit tests for jira.py public API.

Pattern: one test function per public method, containing a test table
of (scenario, input, expected) tuples with descriptive scenario names
following "When {scenario} then {expected behavior}" format.

Run: make test
"""

import json
import os
import sqlite3
import sys
import tempfile
import unittest
from dataclasses import dataclass
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).resolve().parent))

from jira import (
    clean_jira_text,
    adf_to_text,
    open_db, SkillDB,
    SummaryResult, parse_llm_response,
    _build_system_prompt, _build_user_prompt, _load_user_context,
    _RELEVANCE_FLOORS, _WORD_HINTS,
    format_issue, _extract_comments, _extract_links,
    _build_ticket_metadata, cache_issue,
    _build_view_jql,
    _format_summary_block, write_output,
    _Pipeline,
    get_auth_header, log,
)


# ═══════════════════════════════════════════════════════════════
# Helpers
# ═══════════════════════════════════════════════════════════════

def _make_db():
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    os.unlink(path)
    return open_db(path), path


def _cleanup_db(db, path):
    db.close()
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

class TestCleanJiraText(unittest.TestCase):
    def test_clean_jira_text(self):
        cases = [
            ("When input is None then returns empty string",
             None, ""),
            ("When input is empty then returns empty string",
             "", ""),
            ("When input is normal text then returns unchanged",
             "Hello world", "Hello world"),
            ("When input has leading/trailing whitespace then strips it",
             "  hello  ", "hello"),
            ("When input has multiple consecutive newlines then collapses to two",
             "A\n\n\n\n\nB", "A\n\nB"),
            ("When input has multiple consecutive spaces then collapses to one",
             "A     B", "A B"),
            ("When input has mixed noise then cleans all at once",
             "Important\n\n\n\n\n\nstuff   here", "Important\n\nstuff here"),
        ]
        for scenario, input_val, expected in cases:
            with self.subTest(scenario=scenario):
                self.assertEqual(clean_jira_text(input_val), expected)

    def test_clean_jira_text_strips_technical_dumps(self):
        nmap = "Some text\nPORT  STATE SERVICE\n22/tcp open ssh\n80/tcp open http\n443/tcp open https\n"
        nmap += "\n".join([f"line{i}" for i in range(50)])
        result = clean_jira_text(nmap)
        self.assertIn("[...technical output removed...]", result,
                      "When input contains nmap output then replaces with placeholder")


# ═══════════════════════════════════════════════════════════════
# adf_to_text
# ═══════════════════════════════════════════════════════════════

class TestAdfToText(unittest.TestCase):
    def test_adf_to_text(self):
        cases = [
            ("When node is None then returns empty string",
             None, ""),
            ("When node is plain string then returns string",
             "hello", "hello"),
            ("When node is integer then returns empty string",
             42, ""),
            ("When node is text type then returns text value",
             {"type": "text", "text": "hello"}, "hello"),
            ("When node is hardBreak then returns newline",
             {"type": "hardBreak"}, "\n"),
            ("When node is paragraph then returns text with trailing newline",
             {"type": "paragraph", "content": [{"type": "text", "text": "Hello"}]}, "Hello\n"),
            ("When node is empty paragraph then returns just newline",
             {"type": "paragraph", "content": []}, "\n"),
            ("When node is list then concatenates children",
             [{"type": "text", "text": "a"}, {"type": "text", "text": "b"}], "ab"),
            ("When node is unknown type then processes children recursively",
             {"type": "custom_widget", "content": [{"type": "text", "text": "x"}]}, "x"),
        ]
        for scenario, input_val, expected in cases:
            with self.subTest(scenario=scenario):
                self.assertEqual(adf_to_text(input_val), expected)

    def test_adf_to_text_nested_document(self):
        doc = {
            "type": "doc",
            "content": [
                {"type": "paragraph", "content": [{"type": "text", "text": "Line 1"}]},
                {"type": "paragraph", "content": [{"type": "text", "text": "Line 2"}]},
            ],
        }
        result = adf_to_text(doc)
        self.assertIn("Line 1", result, "When doc has nested paragraphs then all content is present")
        self.assertIn("Line 2", result)


# ═══════════════════════════════════════════════════════════════
# open_db
# ═══════════════════════════════════════════════════════════════

class TestOpenDb(unittest.TestCase):
    def test_open_db(self):
        cases = [
            ("When opening fresh DB then creates all required tables",
             {"force": False}, {"atomic_content", "resource_summary", "ticket_relationships"}),
        ]
        for scenario, kwargs, expected_tables in cases:
            with self.subTest(scenario=scenario):
                db, path = _make_db()
                try:
                    tables = {row[0] for row in db._conn.execute(
                        "SELECT name FROM sqlite_master WHERE type='table'")}
                    self.assertTrue(expected_tables.issubset(tables))
                finally:
                    _cleanup_db(db, path)

    def test_open_db_preserves_data_on_reopen(self):
        db, path = _make_db()
        db.upsert_atomic("jira", "K-1", "K-1", "A", "x", "2026-01-01", "2026-01-01")
        db.close()
        db2 = open_db(path)
        items = db2.get_atomic_for_resource("K-1")
        self.assertEqual(len(items), 1,
                         "When reopening DB then existing data is preserved")
        _cleanup_db(db2, path)

    def test_open_db_migration_on_old_schema(self):
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

        db = open_db(path)
        cols = {row[1] for row in db._conn.execute("PRAGMA table_info(resource_summary)")}
        self.assertIn("mention_type", cols,
                      "When opening old-schema DB then migration adds mention_type column")
        self.assertIn("estimated_relevance", cols)
        self.assertIn("final_relevance", cols)
        _cleanup_db(db, path)


# ═══════════════════════════════════════════════════════════════
# SkillDB.upsert_atomic
# ═══════════════════════════════════════════════════════════════

class TestUpsertAtomic(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_upsert_atomic(self):
        cases = [
            ("When inserting new item then returns True",
             {"source": "jira", "rid": "K-1", "iid": "K-1", "author": "A",
              "content": "C", "created": "2026-01-01", "updated": "2026-01-01"},
             True),
        ]
        for scenario, args, expected in cases:
            with self.subTest(scenario=scenario):
                result = self.db.upsert_atomic(
                    args["source"], args["rid"], args["iid"],
                    args["author"], args["content"],
                    args["created"], args["updated"])
                self.assertEqual(result, expected)

        with self.subTest(scenario="When upserting same content then returns False"):
            result = self.db.upsert_atomic("jira", "K-1", "K-1", "A", "C", "2026-01-01", "2026-01-01")
            self.assertFalse(result)

        with self.subTest(scenario="When upserting changed content then returns True and stores new value"):
            self.db.upsert_atomic("jira", "K-1", "K-1", "A", "V2", "2026-01-01", "2026-01-02")
            items = self.db.get_atomic_for_resource("K-1")
            self.assertEqual(items[0]["content"], "V2")

        with self.subTest(scenario="When upserting with metadata then stores JSON blob"):
            self.db.upsert_atomic("jira", "K-2", "K-2", "A", "x", "2026-01-01", "2026-01-01",
                                  metadata={"assignee": "Michael Bui"})
            items = self.db.get_atomic_for_resource("K-2")
            meta = json.loads(items[0]["metadata"])
            self.assertEqual(meta["assignee"], "Michael Bui")


# ═══════════════════════════════════════════════════════════════
# SkillDB.get_atomic_for_resource
# ═══════════════════════════════════════════════════════════════

class TestGetAtomicForResource(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_get_atomic_for_resource(self):
        with self.subTest(scenario="When resource has no items then returns empty list"):
            self.assertEqual(self.db.get_atomic_for_resource("NONE"), [])

        self.db.upsert_atomic("jira", "K-1", "c2", "A", "second", "2026-01-02", "2026-01-02")
        self.db.upsert_atomic("jira", "K-1", "c1", "A", "first", "2026-01-01", "2026-01-01")

        with self.subTest(scenario="When resource has items then returns them ordered by created_at"):
            items = self.db.get_atomic_for_resource("K-1")
            self.assertEqual(items[0]["content"], "first")
            self.assertEqual(items[1]["content"], "second")


# ═══════════════════════════════════════════════════════════════
# SkillDB.get_latest_updated_at
# ═══════════════════════════════════════════════════════════════

class TestGetLatestUpdatedAt(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_get_latest_updated_at(self):
        cases = [
            ("When resource does not exist then returns None",
             "NONE", None),
        ]
        for scenario, rid, expected in cases:
            with self.subTest(scenario=scenario):
                self.assertEqual(self.db.get_latest_updated_at(rid), expected)

        self.db.upsert_atomic("jira", "K-1", "c1", "A", "x", "2026-01-01", "2026-01-01")
        self.db.upsert_atomic("jira", "K-1", "c2", "A", "y", "2026-01-02", "2026-01-05")

        with self.subTest(scenario="When resource has items then returns latest updated_at"):
            self.assertEqual(self.db.get_latest_updated_at("K-1"), "2026-01-05")


# ═══════════════════════════════════════════════════════════════
# SkillDB.has_content_changed
# ═══════════════════════════════════════════════════════════════

class TestHasContentChanged(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_has_content_changed(self):
        cases = [
            ("When resource is new then returns True (needs fetch)",
             "K-NEW", "2026-01-01", True),
        ]
        for scenario, rid, ts, expected in cases:
            with self.subTest(scenario=scenario):
                self.assertEqual(self.db.has_content_changed(rid, ts), expected)

        self.db.upsert_atomic("jira", "K-1", "K-1", "A", "x", "2026-01-01", "2026-01-01")

        with self.subTest(scenario="When timestamp matches cached then returns False (skip)"):
            self.assertFalse(self.db.has_content_changed("K-1", "2026-01-01"))

        with self.subTest(scenario="When timestamp is newer than cached then returns True"):
            self.assertTrue(self.db.has_content_changed("K-1", "2026-01-02"))


# ═══════════════════════════════════════════════════════════════
# SkillDB.get_all_resource_ids
# ═══════════════════════════════════════════════════════════════

class TestGetAllResourceIds(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_get_all_resource_ids(self):
        self.db.upsert_atomic("jira", "K-1", "K-1", "A", "x", "2026-01-01", "2026-01-01")
        self.db.upsert_atomic("jira", "K-2", "K-2", "A", "y", "2026-01-01", "2026-01-01")
        self.db.upsert_atomic("gmail", "T-1", "T-1", "A", "z", "2026-01-01", "2026-01-01")

        cases = [
            ("When no source filter then returns all resource IDs",
             None, {"K-1", "K-2", "T-1"}),
            ("When source=jira then returns only jira resource IDs",
             "jira", {"K-1", "K-2"}),
            ("When source=gmail then returns only gmail resource IDs",
             "gmail", {"T-1"}),
        ]
        for scenario, source, expected in cases:
            with self.subTest(scenario=scenario):
                result = set(self.db.get_all_resource_ids(source=source))
                self.assertEqual(result, expected)


# ═══════════════════════════════════════════════════════════════
# SkillDB.upsert_summary & get_resource_summary
# ═══════════════════════════════════════════════════════════════

class TestUpsertAndGetSummary(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_upsert_summary(self):
        with self.subTest(scenario="When getting nonexistent summary then returns None"):
            self.assertIsNone(self.db.get_resource_summary("NOPE"))

        with self.subTest(scenario="When upserting basic summary then stores with defaults"):
            self.db.upsert_summary("K-1", "jira", "Title", "Summary text")
            s = self.db.get_resource_summary("K-1")
            self.assertEqual(s["summary"], "Summary text")
            self.assertEqual(s["mention_type"], "none")
            self.assertEqual(s["estimated_relevance"], 0)
            self.assertEqual(s["final_relevance"], 0)

        with self.subTest(scenario="When upserting with relevance fields then stores them correctly"):
            self.db.upsert_summary("K-2", "jira", "T", "S",
                                   mention_type="direct", estimated_relevance=8, final_relevance=8)
            s = self.db.get_resource_summary("K-2")
            self.assertEqual(s["mention_type"], "direct")
            self.assertEqual(s["estimated_relevance"], 8)
            self.assertEqual(s["final_relevance"], 8)

        with self.subTest(scenario="When final_relevance not specified then defaults to estimated_relevance"):
            self.db.upsert_summary("K-3", "jira", "T", "S", estimated_relevance=7)
            s = self.db.get_resource_summary("K-3")
            self.assertEqual(s["final_relevance"], 7)

        with self.subTest(scenario="When upserting with metadata then stores JSON entities"):
            meta = {"work_items": ["DPD-1"], "people": ["John"], "labels": ["a-b", "c-d"]}
            self.db.upsert_summary("K-4", "jira", "T", "S", metadata=meta)
            s = self.db.get_resource_summary("K-4")
            m = json.loads(s["metadata"])
            self.assertEqual(m["work_items"], ["DPD-1"])
            self.assertEqual(m["people"], ["John"])

        with self.subTest(scenario="When updating existing summary then overwrites values"):
            self.db.upsert_summary("K-1", "jira", "T", "V2", estimated_relevance=9)
            s = self.db.get_resource_summary("K-1")
            self.assertEqual(s["summary"], "V2")
            self.assertEqual(s["estimated_relevance"], 9)


# ═══════════════════════════════════════════════════════════════
# SkillDB.needs_resummarize
# ═══════════════════════════════════════════════════════════════

class TestNeedsResummarize(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_needs_resummarize(self):
        self.db.upsert_atomic("jira", "K-1", "K-1", "A", "x", "2026-01-01", "2026-01-01")

        cases_before_summary = [
            ("When no summary exists then returns True",
             "K-1", True),
        ]
        for scenario, rid, expected in cases_before_summary:
            with self.subTest(scenario=scenario):
                self.assertEqual(self.db.needs_resummarize(rid), expected)

        self.db.upsert_summary("K-1", "jira", "T", "S")

        with self.subTest(scenario="When summary is up-to-date then returns False"):
            self.assertFalse(self.db.needs_resummarize("K-1"))

        self.db.upsert_atomic("jira", "K-1", "c2", "A", "new", "2026-01-02", "2099-01-01")

        with self.subTest(scenario="When new atomic content added after summary then returns True"):
            self.assertTrue(self.db.needs_resummarize("K-1"))


# ═══════════════════════════════════════════════════════════════
# SkillDB.get_items_since
# ═══════════════════════════════════════════════════════════════

class TestGetItemsSince(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_get_items_since(self):
        self.db.upsert_atomic("jira", "K-1", "c1", "A", "old", "2026-01-01", "2026-01-01")
        self.db.upsert_atomic("jira", "K-1", "c2", "A", "new", "2026-01-05", "2026-01-05")

        cases = [
            ("When cutoff is before all items then returns all items",
             "K-1", "2025-01-01", 2),
            ("When cutoff is between items then returns only newer",
             "K-1", "2026-01-02", 1),
            ("When cutoff is after all items then returns none",
             "K-1", "2027-01-01", 0),
        ]
        for scenario, rid, since, expected_count in cases:
            with self.subTest(scenario=scenario):
                items = self.db.get_items_since(rid, since)
                self.assertEqual(len(items), expected_count)


# ═══════════════════════════════════════════════════════════════
# SkillDB.compute_mention_type
# ═══════════════════════════════════════════════════════════════

class TestComputeMentionType(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_compute_mention_type(self):
        cases = [
            ("When resource does not exist then returns 'none'",
             [], "none"),
            ("When user is assignee then returns 'direct'",
             [{"iid": "K-1", "author": "Reporter", "content": "C",
               "metadata": {"assignee": "Michael Bui"}}],
             "direct"),
            ("When user is reporter then returns 'direct'",
             [{"iid": "K-1", "author": "Someone", "content": "C",
               "metadata": {"reporter": "Michael Bui"}}],
             "direct"),
            ("When user is comment author then returns 'direct'",
             [{"iid": "c1", "author": "Michael Bui", "content": "Comment"}],
             "direct"),
            ("When user is @mentioned in content then returns 'direct'",
             [{"iid": "c1", "author": "Someone", "content": "Hey @michael bui check this"}],
             "direct"),
            ("When user name appears in content then returns 'direct'",
             [{"iid": "c1", "author": "Someone", "content": "Assigned to Michael Bui for review"}],
             "direct"),
            ("When user name is UPPERCASE then returns 'direct' (case insensitive)",
             [{"iid": "K-1", "author": "Someone", "content": "C",
               "metadata": {"assignee": "MICHAEL BUI"}}],
             "direct"),
            ("When only linked issues exist then returns 'indirect'",
             [{"iid": "K-1", "author": "Someone", "content": "C",
               "metadata": {"linked_issues": [{"type": "blocks", "key": "K-2"}]}}],
             "indirect"),
            ("When no user signals then returns 'none'",
             [{"iid": "K-1", "author": "Someone", "content": "Unrelated content"}],
             "none"),
        ]

        for idx, (scenario, items_data, expected) in enumerate(cases):
            with self.subTest(scenario=scenario):
                rid = f"MT-{idx}"
                for item in items_data:
                    self.db.upsert_atomic(
                        "jira", rid, item["iid"], item.get("author", "Unknown"),
                        item["content"], "2026-01-01", "2026-01-01",
                        metadata=item.get("metadata"))
                self.assertEqual(self.db.compute_mention_type(rid), expected)

    def test_compute_mention_type_strongest_wins(self):
        self.db.upsert_atomic("jira", "K-SW", "K-SW", "Someone", "Content", "2026-01-01", "2026-01-01",
                              metadata={"linked_issues": [{"type": "x", "key": "K-2"}]})
        self.db.upsert_atomic("jira", "K-SW", "c1", "Michael Bui", "My comment", "2026-01-02", "2026-01-02")
        self.assertEqual(self.db.compute_mention_type("K-SW"), "direct",
                         "When resource has both indirect and direct signals then strongest wins")


# ═══════════════════════════════════════════════════════════════
# SkillDB.get_all_summaries
# ═══════════════════════════════════════════════════════════════

class TestGetAllSummaries(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_get_all_summaries(self):
        self.db.upsert_summary("K-1", "jira", "T", "Low", estimated_relevance=3, final_relevance=3)
        self.db.upsert_summary("K-2", "jira", "T", "High", estimated_relevance=8, final_relevance=8)
        self.db.upsert_summary("K-3", "gmail", "T", "Gmail", estimated_relevance=9, final_relevance=9)

        cases = [
            ("When no filters then returns all sorted by final_relevance desc",
             {}, 3),
            ("When min_relevance=5 then excludes low relevance",
             {"min_relevance": 5}, 2),
            ("When source=jira then returns only jira summaries",
             {"source": "jira"}, 2),
            ("When both filters then applies both",
             {"source": "jira", "min_relevance": 5}, 1),
        ]
        for scenario, kwargs, expected_count in cases:
            with self.subTest(scenario=scenario):
                result = self.db.get_all_summaries(**kwargs)
                self.assertEqual(len(result), expected_count)

        with self.subTest(scenario="When results returned then ordered by final_relevance descending"):
            all_s = self.db.get_all_summaries()
            self.assertEqual(all_s[0]["resource_id"], "K-3")
            self.assertEqual(all_s[1]["resource_id"], "K-2")


# ═══════════════════════════════════════════════════════════════
# SkillDB.backfill_mention_types
# ═══════════════════════════════════════════════════════════════

class TestBackfillMentionTypes(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_backfill_mention_types(self):
        self.db.upsert_atomic("jira", "K-1", "K-1", "Michael Bui", "x", "2026-01-01", "2026-01-01")
        self.db.upsert_atomic("jira", "K-2", "K-2", "Other", "y", "2026-01-01", "2026-01-01",
                              metadata={"linked_issues": [{"type": "x", "key": "K-3"}]})
        self.db.upsert_atomic("jira", "K-3", "K-3", "Other", "z", "2026-01-01", "2026-01-01")
        self.db.upsert_summary("K-1", "jira", "T1", "S1")
        self.db.upsert_summary("K-2", "jira", "T2", "S2")
        self.db.upsert_summary("K-3", "jira", "T3", "S3")

        counts = self.db.backfill_mention_types()

        with self.subTest(scenario="When backfilling then counts each mention_type correctly"):
            self.assertEqual(counts["direct"], 1)
            self.assertEqual(counts["indirect"], 1)
            self.assertEqual(counts["none"], 1)

        with self.subTest(scenario="When backfilled then summaries have correct mention_type"):
            self.assertEqual(self.db.get_resource_summary("K-1")["mention_type"], "direct")
            self.assertEqual(self.db.get_resource_summary("K-2")["mention_type"], "indirect")


# ═══════════════════════════════════════════════════════════════
# SkillDB.clear_all_summaries
# ═══════════════════════════════════════════════════════════════

class TestClearAllSummaries(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_clear_all_summaries(self):
        self.db.upsert_summary("K-1", "jira", "T", "S", mention_type="direct",
                               estimated_relevance=8, final_relevance=8)
        count = self.db.clear_all_summaries()

        with self.subTest(scenario="When clearing then returns count of cleared summaries"):
            self.assertEqual(count, 1)

        with self.subTest(scenario="When cleared then summary text is None but mention_type preserved"):
            s = self.db.get_resource_summary("K-1")
            self.assertIsNone(s["summary"])
            self.assertEqual(s["estimated_relevance"], 0)
            self.assertEqual(s["mention_type"], "direct")


# ═══════════════════════════════════════════════════════════════
# SkillDB.upsert_relationship / get_relationships / clear_relationships
# ═══════════════════════════════════════════════════════════════

class TestRelationships(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_relationships(self):
        with self.subTest(scenario="When upserting relationship then it is retrievable"):
            self.db.upsert_relationship("K-1", "K-2", "blocks")
            rels = self.db.get_relationships("K-1")
            self.assertEqual(len(rels), 1)
            self.assertEqual(rels[0]["target_key"], "K-2")

        with self.subTest(scenario="When querying from target side then relationship is bidirectional"):
            rels = self.db.get_relationships("K-2")
            self.assertEqual(len(rels), 1)

        with self.subTest(scenario="When upserting same relationship twice then no duplicates"):
            self.db.upsert_relationship("K-1", "K-2", "blocks")
            rels = self.db.get_relationships("K-1")
            self.assertEqual(len(rels), 1)

        with self.subTest(scenario="When clearing relationships then all removed for that resource"):
            self.db.upsert_relationship("K-1", "K-3", "relates-to")
            self.db.clear_relationships("K-1")
            self.assertEqual(self.db.get_relationships("K-1"), [])


# ═══════════════════════════════════════════════════════════════
# SkillDB.delete_resource
# ═══════════════════════════════════════════════════════════════

class TestDeleteResource(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_delete_resource(self):
        self.db.upsert_atomic("jira", "K-1", "K-1", "A", "x", "2026-01-01", "2026-01-01")
        self.db.upsert_summary("K-1", "jira", "T", "S")
        self.db.upsert_relationship("K-1", "K-2", "blocks")
        self.db.delete_resource("K-1")

        with self.subTest(scenario="When deleting resource then atomic content is removed"):
            self.assertEqual(self.db.get_atomic_for_resource("K-1"), [])

        with self.subTest(scenario="When deleting resource then summary is removed"):
            self.assertIsNone(self.db.get_resource_summary("K-1"))

        with self.subTest(scenario="When deleting resource then relationships are removed"):
            self.assertEqual(self.db.get_relationships("K-1"), [])


# ═══════════════════════════════════════════════════════════════
# parse_llm_response
# ═══════════════════════════════════════════════════════════════

class TestParseLlmResponse(unittest.TestCase):
    def _valid_json(self, **overrides):
        base = {
            "relevance": 8, "summary": "DPD-715: Task assigned.",
            "work_items": ["DPD-715", "PR #649"], "people": ["Nikhil Grover"],
            "labels": ["pricing-migration", "code-review", "task-assignment", "pull-request", "backend-api"],
        }
        base.update(overrides)
        return json.dumps(base)

    def test_parse_llm_response(self):
        valid = self._valid_json()
        cases = [
            ("When response is valid JSON then parses all fields correctly",
             valid, "direct",
             {"relevance": 8, "work_items_len": 2, "people_len": 1, "labels_len": 5}),
            ("When response has <think> block then strips it and parses",
             f"<think>Let me analyze...</think>{valid}", "direct",
             {"relevance": 8}),
            ("When response has ```json fences then strips them and parses",
             f"```json\n{valid}\n```", "direct",
             {"relevance": 8}),
            ("When response has bare ``` fences then strips them and parses",
             f"```\n{valid}\n```", "direct",
             {"relevance": 8}),
            ("When response has both think block and fences then handles both",
             f"<think>hmm</think>```json\n{valid}\n```", "direct",
             {"relevance": 8}),
            ("When relevance below direct floor then clamps to 7",
             self._valid_json(relevance=3), "direct",
             {"relevance": 7}),
            ("When relevance below indirect floor then clamps to 5",
             self._valid_json(relevance=2), "indirect",
             {"relevance": 5}),
            ("When mention is 'none' and relevance=1 then no clamping",
             self._valid_json(relevance=1), "none",
             {"relevance": 1}),
            ("When relevance exceeds 10 then clamps to 10",
             self._valid_json(relevance=15), "none",
             {"relevance": 10}),
            ("When labels > 5 then truncates to 5",
             json.dumps({"relevance": 5, "summary": "x", "work_items": [], "people": [],
                         "labels": ["a-b", "c-d", "e-f", "g-h", "i-j", "k-l", "m-n"]}), "none",
             {"relevance": 5, "labels_len": 5}),
            ("When work_items and people keys missing then defaults to empty lists",
             json.dumps({"relevance": 5, "summary": "x", "labels": ["a-b"]}), "none",
             {"work_items_len": 0, "people_len": 0}),
        ]
        for scenario, raw, mention, checks in cases:
            with self.subTest(scenario=scenario):
                r = parse_llm_response(raw, mention)
                for key, expected in checks.items():
                    if key == "relevance":
                        self.assertEqual(r.relevance, expected)
                    elif key.endswith("_len"):
                        attr = key[:-4]
                        self.assertEqual(len(getattr(r, attr)), expected)

    def test_parse_llm_response_regex_fallback(self):
        cases = [
            ("When JSON is invalid but has relevance regex then extracts it",
             'Not JSON but "relevance": 6 and "summary": "Fallback text"', "indirect",
             6, "Fallback text"),
            ("When JSON is completely invalid then defaults to relevance=5",
             "Completely invalid text", "none",
             5, None),
            ("When regex fallback with direct floor then clamps up",
             'Bad "relevance": 2', "direct",
             7, None),
        ]
        for scenario, raw, mention, expected_rel, expected_summary in cases:
            with self.subTest(scenario=scenario):
                r = parse_llm_response(raw, mention)
                self.assertEqual(r.relevance, expected_rel)
                if expected_summary:
                    self.assertIn(expected_summary, r.summary)

    def test_summary_result_dataclass_defaults(self):
        sr = SummaryResult(relevance=8, summary="Test")
        self.assertEqual(sr.work_items, [],
                         "When creating SummaryResult without optional fields then lists default to empty")
        self.assertEqual(sr.people, [])
        self.assertEqual(sr.labels, [])


# ═══════════════════════════════════════════════════════════════
# _build_system_prompt & _build_user_prompt
# ═══════════════════════════════════════════════════════════════

class TestPromptBuilders(unittest.TestCase):
    def test_build_system_prompt(self):
        p = _build_system_prompt()
        self.assertIn("Michael Bui", p,
                      "When building system prompt then includes user context from User.md")
        self.assertIn("relevance-scoring", p)

    def test_build_user_prompt(self):
        cases = [
            ("When mention_type=direct then word hint is ~200 words",
             "direct", "~200 words"),
            ("When mention_type=indirect then word hint is ~100 words",
             "indirect", "~100 words"),
            ("When mention_type=none then word hint is ~30 words",
             "none", "~30 words"),
        ]
        for scenario, mention, expected_hint in cases:
            with self.subTest(scenario=scenario):
                p = _build_user_prompt("T", "Jira", "{}", "c", mention)
                self.assertIn(expected_hint, p)

        with self.subTest(scenario="When prompt built then contains JSON instruction"):
            p = _build_user_prompt("T", "Jira", "{}", "c", "direct")
            self.assertIn("JSON", p)

        with self.subTest(scenario="When prompt built then contains relevance floor rules"):
            p = _build_user_prompt("T", "Jira", "{}", "c", "direct")
            self.assertIn("RELEVANCE FLOOR", p)
            self.assertIn("direct mention_type >= 7", p)

        with self.subTest(scenario="When prompt built then contains entity extraction rules"):
            p = _build_user_prompt("T", "Jira", "{}", "c", "none")
            self.assertIn("work_items", p)
            self.assertIn("people", p)
            self.assertIn("5 descriptive 2-word", p)

        with self.subTest(scenario="When existing_summary provided then prompt includes it"):
            p = _build_user_prompt("T", "Jira", "{}", "c", "direct", existing_summary="Previous text")
            self.assertIn("Existing summary", p)
            self.assertIn("Previous text", p)

    def test_load_user_context(self):
        ctx = _load_user_context()
        self.assertIn("Michael Bui", ctx,
                      "When loading user context then User.md content is returned")


# ═══════════════════════════════════════════════════════════════
# format_issue
# ═══════════════════════════════════════════════════════════════

class TestFormatIssue(unittest.TestCase):
    def test_format_issue(self):
        cases = [
            ("When issue has all fields then extracts them correctly",
             _sample_issue(),
             {"key": "DPD-1", "title": "Test Ticket", "assignee": "Michael Bui",
              "reporter": "John Doe", "priority": "High", "issuetype": "Task"}),
            ("When assignee is None then returns None",
             _sample_issue(assignee=None),
             {"assignee": None}),
            ("When issue has parent then extracts parent key",
             _sample_issue(parent={"key": "EPIC-1", "fields": {"summary": "Epic"}}),
             {"parent_key": "EPIC-1"}),
        ]
        for scenario, raw_issue, checks in cases:
            with self.subTest(scenario=scenario):
                result = format_issue(raw_issue)
                for k, v in checks.items():
                    if k == "parent_key":
                        self.assertEqual(result["parent"]["key"], v)
                    else:
                        self.assertEqual(result[k], v)

    def test_format_issue_comments(self):
        issue = _sample_issue(comment={
            "comments": [
                {"id": str(i), "created": f"2026-01-{i:02d}", "author": {"displayName": f"P{i}"}, "body": f"C{i}"}
                for i in range(1, 16)
            ]
        })
        result = format_issue(issue)
        self.assertEqual(len(result["comments"]), 10,
                         "When issue has >10 comments then only latest 10 are kept")

    def test_format_issue_links(self):
        issue = _sample_issue(issuelinks=[
            {"type": {"name": "Blocks"}, "outwardIssue": {"key": "DPD-2"}},
            {"type": {"name": "Relates"}, "inwardIssue": {"key": "DPD-3"}},
        ])
        result = format_issue(issue)
        self.assertEqual(len(result["links"]), 2,
                         "When issue has issuelinks then both inward and outward are extracted")


# ═══════════════════════════════════════════════════════════════
# _build_ticket_metadata
# ═══════════════════════════════════════════════════════════════

class TestBuildTicketMetadata(unittest.TestCase):
    def test_build_ticket_metadata(self):
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
            with self.subTest(scenario=scenario):
                meta = _build_ticket_metadata(issue)
                self.assertTrue(check_fn(meta))


# ═══════════════════════════════════════════════════════════════
# cache_issue
# ═══════════════════════════════════════════════════════════════

class TestCacheIssue(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_cache_issue(self):
        issue_data = {
            "key": "K-1", "title": "Test", "description": "Desc",
            "status": {"name": "Open", "category": "To Do"},
            "assignee": "Michael Bui", "reporter": "John", "priority": "High",
            "issuetype": "Task", "resolution": None, "labels": [], "components": [],
            "fix_versions": [], "duedate": None, "parent": None, "subtasks": [],
            "links": [], "created": "2026-01-01", "updated": "2026-01-01", "comments": [],
        }

        with self.subTest(scenario="When caching issue without comments then creates 1 atomic item"):
            cache_issue(self.db, issue_data)
            items = self.db.get_atomic_for_resource("K-1")
            self.assertEqual(len(items), 1)
            self.assertIn("Title: Test", items[0]["content"])

        with self.subTest(scenario="When caching issue with comments then creates 1+N atomic items"):
            issue_with_comments = dict(issue_data)
            issue_with_comments["key"] = "K-2"
            issue_with_comments["comments"] = [
                {"id": "c1", "created": "2026-01-02", "updated": "2026-01-02",
                 "author": "Alice", "body": "Comment body"}
            ]
            cache_issue(self.db, issue_with_comments)
            items = self.db.get_atomic_for_resource("K-2")
            self.assertEqual(len(items), 2)

        with self.subTest(scenario="When issue has parent then relationship is stored"):
            parent_issue = dict(issue_data)
            parent_issue["key"] = "K-3"
            parent_issue["parent"] = {"key": "EPIC-1", "summary": "Epic"}
            cache_issue(self.db, parent_issue)
            rels = self.db.get_relationships("K-3")
            self.assertTrue(any(r["target_key"] == "EPIC-1" for r in rels))


# ═══════════════════════════════════════════════════════════════
# get_auth_header
# ═══════════════════════════════════════════════════════════════

class TestGetAuthHeader(unittest.TestCase):
    def test_get_auth_header(self):
        header = get_auth_header("user@example.com", "mykey")
        self.assertIn("Authorization", header,
                      "When generating auth header then includes Authorization key")
        self.assertTrue(header["Authorization"].startswith("Basic "),
                        "When generating auth header then value is Basic auth")


# ═══════════════════════════════════════════════════════════════
# _build_view_jql
# ═══════════════════════════════════════════════════════════════

class TestBuildViewJql(unittest.TestCase):
    def test_build_view_jql(self):
        cases = [
            ("When no filters or sort then returns base JQL unchanged",
             ("project = DPD", [], [], None),
             "project = DPD"),
            ("When filter with single value then adds = clause",
             ("project = DPD",
              [{"field": {"jiraFieldKey": "status"}, "kind": "FIELD_IDENTITY",
                "values": [{"stringValue": "Done"}]}], [], None),
             "status = Done"),
            ("When filter is negation then adds != clause",
             ("project = DPD",
              [{"field": {"jiraFieldKey": "status"}, "kind": "NOT_FIELD_IDENTITY",
                "values": [{"stringValue": "Done"}]}], [], None),
             "status != Done"),
            ("When filter has multiple values then adds IN clause",
             ("project = DPD",
              [{"field": {"jiraFieldKey": "status"}, "kind": "FIELD_IDENTITY",
                "values": [{"stringValue": "Open"}, {"stringValue": "In Progress"}]}], [], None),
             "status in (Open, In Progress)"),
            ("When sort fields provided then adds ORDER BY",
             ("project = DPD", [],
              [{"field": {"jiraFieldKey": "updated"}, "order": "DESC"}], None),
             "ORDER BY updated DESC"),
            ("When sort_mode fallback used then generates ORDER BY from mode",
             ("project = DPD", [], [], "CREATED"),
             "ORDER BY created DESC"),
            ("When base has existing ORDER BY then strips and replaces",
             ("project = DPD ORDER BY rank ASC", [], [], "UPDATED"),
             "ORDER BY updated DESC"),
            ("When customfield then converts to cf[] syntax",
             ("project = DPD",
              [{"field": {"jiraFieldKey": "customfield_12345"}, "kind": "FIELD_IDENTITY",
                "values": [{"numericValue": 42}]}], [], None),
             "cf[12345] = 42"),
        ]
        for scenario, (base, filters, sort, mode), expected_substring in cases:
            with self.subTest(scenario=scenario):
                result = _build_view_jql(base, filters, sort, mode)
                self.assertIn(expected_substring, result)

        with self.subTest(scenario="When base had ORDER BY then old sort is removed"):
            result = _build_view_jql("project = DPD ORDER BY rank ASC", [], [], "UPDATED")
            self.assertNotIn("rank ASC", result)


# ═══════════════════════════════════════════════════════════════
# _format_summary_block
# ═══════════════════════════════════════════════════════════════

class TestFormatSummaryBlock(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_format_summary_block(self):
        cases = [
            ("When summary has relevance then block includes 'Relevance: N/10'",
             {"mention_type": "direct", "estimated_relevance": 9, "final_relevance": 9},
             "Relevance: 9/10"),
            ("When mention_type is 'none' then block excludes Mention label",
             {},
             None),
            ("When summary has relationships then block includes them",
             {},
             None),
        ]

        self.db.upsert_summary("K-R", "jira", "Test", "Summary",
                               mention_type="direct", estimated_relevance=9, final_relevance=9)
        s = self.db.get_resource_summary("K-R")
        block = _format_summary_block(self.db, "K-R", s, 1, 1)

        with self.subTest(scenario="When summary has direct mention then shows Relevance and Mention"):
            self.assertIn("Relevance: 9/10", block)
            self.assertIn("Mention: direct", block)

        self.db.upsert_summary("K-N", "jira", "Test", "Summary")
        s2 = self.db.get_resource_summary("K-N")
        block2 = _format_summary_block(self.db, "K-N", s2, 1, 1)

        with self.subTest(scenario="When mention_type is 'none' then Mention label is excluded"):
            self.assertNotIn("Mention:", block2)

        self.db.upsert_summary("K-M", "jira", "Test", "S",
                               metadata={"status": "Done", "status_category": "Done", "priority": "High"})
        s3 = self.db.get_resource_summary("K-M")
        block3 = _format_summary_block(self.db, "K-M", s3, 1, 1)

        with self.subTest(scenario="When summary has metadata then shows Status and Priority"):
            self.assertIn("Status: Done (Done)", block3)
            self.assertIn("Priority: High", block3)

        self.db.upsert_summary("K-L", "jira", "Test", "S")
        self.db.upsert_relationship("K-L", "K-2", "blocks")
        s4 = self.db.get_resource_summary("K-L")
        block4 = _format_summary_block(self.db, "K-L", s4, 1, 1)

        with self.subTest(scenario="When summary has relationships then shows them"):
            self.assertIn("blocks: K-2", block4)


# ═══════════════════════════════════════════════════════════════
# write_output
# ═══════════════════════════════════════════════════════════════

class TestWriteOutput(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()
        self.output = Path(tempfile.mktemp(suffix=".md"))

    def tearDown(self):
        _cleanup_db(self.db, self.path)
        if self.output.exists():
            self.output.unlink()

    def test_write_output(self):
        with self.subTest(scenario="When no summaries then creates empty file"):
            write_output(self.db, self.output)
            self.assertTrue(self.output.exists())
            self.assertEqual(self.output.read_text(), "")

        self.output.unlink()
        self.db.upsert_summary("K-1", "jira", "Test", "Summary text",
                               estimated_relevance=8, final_relevance=8)

        with self.subTest(scenario="When summaries exist then file contains summary content"):
            write_output(self.db, self.output)
            content = self.output.read_text()
            self.assertIn("Summary text", content)
            self.assertIn("Relevance: 8/10", content)

    def test_write_output_file_lifecycle(self):
        self.assertFalse(self.output.exists(),
                         "When output not yet written then file does not exist")
        self.db.upsert_summary("K-1", "jira", "T", "S", estimated_relevance=5, final_relevance=5)
        write_output(self.db, self.output)
        self.assertTrue(self.output.exists(),
                        "When write_output called then file is created")


# ═══════════════════════════════════════════════════════════════
# _Pipeline (with mocked LLM)
# ═══════════════════════════════════════════════════════════════

class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    @patch("jira._call_llm")
    def test_pipeline(self, mock_llm):
        mock_llm.return_value = json.dumps({
            "relevance": 8, "summary": "Test summary",
            "work_items": ["K-1"], "people": ["Alice"],
            "labels": ["a-b", "c-d", "e-f", "g-h", "i-j"],
        })
        self.db.upsert_atomic("jira", "K-1", "K-1", "Reporter",
                              "Title: Test\nStatus: Open (To Do)",
                              "2026-01-01", "2026-01-01",
                              metadata={"status": "Open", "status_category": "To Do"})

        pipeline = _Pipeline(self.db, force=True)
        pipeline.set_total(1)
        pipeline.put("K-1")
        errors = pipeline.finish()

        with self.subTest(scenario="When pipeline processes successfully then no errors returned"):
            self.assertEqual(errors, [])

        with self.subTest(scenario="When pipeline completes then summary is stored in DB"):
            s = self.db.get_resource_summary("K-1")
            self.assertIsNotNone(s)
            self.assertEqual(s["estimated_relevance"], 8)

    @patch("jira._call_llm")
    def test_pipeline_error_handling(self, mock_llm):
        mock_llm.side_effect = RuntimeError("LLM down")
        self.db.upsert_atomic("jira", "K-1", "K-1", "A", "Title: Test", "2026-01-01", "2026-01-01")

        pipeline = _Pipeline(self.db, force=True)
        pipeline.set_total(1)
        pipeline.put("K-1")
        errors = pipeline.finish()

        with self.subTest(scenario="When LLM fails then error is captured in errors list"):
            self.assertEqual(len(errors), 1)
            self.assertIn("K-1", errors[0])


# ═══════════════════════════════════════════════════════════════
# Relevance Constants
# ═══════════════════════════════════════════════════════════════

class TestRelevanceConstants(unittest.TestCase):
    def test_relevance_floors(self):
        cases = [
            ("When mention is direct then floor is 7", "direct", 7),
            ("When mention is indirect then floor is 5", "indirect", 5),
            ("When mention is none then floor is 1", "none", 1),
        ]
        for scenario, key, expected in cases:
            with self.subTest(scenario=scenario):
                self.assertEqual(_RELEVANCE_FLOORS[key], expected)

    def test_word_hints(self):
        cases = [
            ("When mention is direct then hint is 200 words", "direct", 200),
            ("When mention is indirect then hint is 100 words", "indirect", 100),
            ("When mention is none then hint is 30 words", "none", 30),
        ]
        for scenario, key, expected in cases:
            with self.subTest(scenario=scenario):
                self.assertEqual(_WORD_HINTS[key], expected)


# ═══════════════════════════════════════════════════════════════
# log function
# ═══════════════════════════════════════════════════════════════

class TestLog(unittest.TestCase):
    def test_log(self):
        import io
        from unittest.mock import patch
        with patch("sys.stdout", new_callable=io.StringIO) as mock_out:
            log("test message")
            output = mock_out.getvalue()
            self.assertIn("test message", output,
                          "When log is called then message appears on stdout")
            self.assertIn("[", output,
                          "When log is called then timestamp bracket is present")


# ═══════════════════════════════════════════════════════════════
# summarize_resource (with mocked LLM)
# ═══════════════════════════════════════════════════════════════

from jira import summarize_resource

class TestSummarizeResource(unittest.TestCase):
    @patch("jira._call_llm")
    def test_summarize_resource(self, mock_llm):
        mock_llm.return_value = json.dumps({
            "relevance": 9, "summary": "Critical bug fix needed",
            "work_items": ["DPD-100"], "people": ["Alice"],
            "labels": ["bug-fix", "critical-path", "api-error", "prod-issue", "urgent-deploy"],
        })
        items = [{"author": "Alice", "created_at": "2026-01-01", "content": "Bug description here"}]

        cases = [
            ("When items provided then calls LLM and returns structured result",
             items, "direct", 9),
            ("When mention_type is none then relevance floor is 1",
             items, "none", 9),
        ]
        for scenario, test_items, mention, expected_rel in cases:
            with self.subTest(scenario=scenario):
                r = summarize_resource("DPD-100: Bug", "Jira ticket", test_items,
                                       metadata={"status": "Open"}, mention_type=mention)
                self.assertEqual(r.relevance, expected_rel)
                self.assertIn("bug fix", r.summary.lower())

    def test_summarize_resource_empty_items(self):
        cases = [
            ("When no items and no existing summary then returns floor relevance with empty summary",
             "direct", None, 7, ""),
            ("When no items but existing summary then returns floor relevance with existing text",
             "indirect", "Prev text", 5, "Prev text"),
        ]
        for scenario, mention, existing, expected_rel, expected_summary in cases:
            with self.subTest(scenario=scenario):
                r = summarize_resource("K-1", "Jira", [], mention_type=mention,
                                       existing_summary=existing)
                self.assertEqual(r.relevance, expected_rel)
                self.assertEqual(r.summary, expected_summary)


# ═══════════════════════════════════════════════════════════════
# _call_llm (mocked HTTP)
# ═══════════════════════════════════════════════════════════════

from jira import _call_llm

class TestCallLlm(unittest.TestCase):
    @patch("jira.requests.post")
    def test_call_llm(self, mock_post):
        cases = [
            ("When API returns 200 then returns content",
             200, {"choices": [{"message": {"content": '{"relevance":5}'}}]}, '{"relevance":5}'),
        ]
        for scenario, status, resp_json, expected in cases:
            with self.subTest(scenario=scenario):
                mock_resp = MagicMock()
                mock_resp.status_code = status
                mock_resp.json.return_value = resp_json
                mock_post.return_value = mock_resp
                result = _call_llm("sys", "user")
                self.assertEqual(result, expected)

    @patch("jira.requests.post")
    @patch("jira.SUMMARIZE_RETRIES", 0)
    def test_call_llm_errors(self, mock_post):
        cases = [
            ("When API returns 400 then raises RuntimeError",
             400, "Bad request"),
            ("When API returns empty content then raises RuntimeError",
             200, None),
        ]
        for scenario, status, text_or_none in cases:
            with self.subTest(scenario=scenario):
                mock_resp = MagicMock()
                mock_resp.status_code = status
                mock_resp.text = text_or_none or ""
                if status == 200:
                    mock_resp.json.return_value = {"choices": [{"message": {"content": ""}}]}
                mock_post.return_value = mock_resp
                with self.assertRaises(RuntimeError):
                    _call_llm("sys", "user")

    @patch("jira.requests.post")
    @patch("jira.SUMMARIZE_RETRIES", 1)
    @patch("jira.SUMMARIZE_RETRY_INITIAL_SEC", 0.01)
    def test_call_llm_retries_on_5xx(self, mock_post):
        err_resp = MagicMock()
        err_resp.status_code = 503
        err_resp.text = "Service Unavailable"
        ok_resp = MagicMock()
        ok_resp.status_code = 200
        ok_resp.json.return_value = {"choices": [{"message": {"content": "ok"}}]}
        mock_post.side_effect = [err_resp, ok_resp]

        result = _call_llm("sys", "user")
        self.assertEqual(result, "ok",
                         "When first call returns 5xx then retries and succeeds on second attempt")

    @patch("jira.requests.post")
    @patch("jira.SUMMARIZE_RETRIES", 1)
    @patch("jira.SUMMARIZE_RETRY_INITIAL_SEC", 0.01)
    def test_call_llm_retries_on_connection_error(self, mock_post):
        import requests as req
        ok_resp = MagicMock()
        ok_resp.status_code = 200
        ok_resp.json.return_value = {"choices": [{"message": {"content": "recovered"}}]}
        mock_post.side_effect = [req.ConnectionError("fail"), ok_resp]

        result = _call_llm("sys", "user")
        self.assertEqual(result, "recovered",
                         "When connection error then retries and succeeds")


# ═══════════════════════════════════════════════════════════════
# validate_env
# ═══════════════════════════════════════════════════════════════

from jira import validate_env

class TestValidateEnv(unittest.TestCase):
    @patch.dict(os.environ, {"JIRA_EMAIL": "a@b.com", "JIRA_API_KEY": "secret123"})
    def test_validate_env_success(self):
        email, key = validate_env()
        self.assertEqual(email, "a@b.com",
                         "When env vars set then returns email")
        self.assertEqual(key, "secret123")

    @patch.dict(os.environ, {}, clear=True)
    def test_validate_env_missing(self):
        env_backup = {}
        for k in ("JIRA_EMAIL", "JIRA_API_KEY"):
            if k in os.environ:
                env_backup[k] = os.environ.pop(k)
        try:
            with self.assertRaises(SystemExit):
                validate_env()
        finally:
            os.environ.update(env_backup)


# ═══════════════════════════════════════════════════════════════
# cache_issue extended branches
# ═══════════════════════════════════════════════════════════════

class TestCacheIssueExtended(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_cache_issue_all_optional_fields(self):
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
                {"id": "c1", "created": "2026-01-02", "updated": "2026-01-02",
                 "author": "Alice", "body": "Comment 1"},
                {"id": "c2", "created": "2026-01-03", "updated": "2026-01-03",
                 "author": "Bob", "body": "Comment 2"},
            ],
        }
        changed = cache_issue(self.db, issue)

        with self.subTest(scenario="When issue has all optional fields then caches them in content"):
            self.assertTrue(changed)
            items = self.db.get_atomic_for_resource("K-5")
            self.assertEqual(len(items), 3)
            main_content = items[0]["content"]
            self.assertIn("Labels: critical, backend", main_content)
            self.assertIn("Components: API, DB", main_content)
            self.assertIn("Fix Versions: v2.0", main_content)
            self.assertIn("Parent: EPIC-1", main_content)
            self.assertIn("Subtask: K-5a", main_content)
            self.assertIn("Link (blocks): K-6", main_content)
            self.assertIn("Resolution: Fixed", main_content)
            self.assertIn("Due: 2026-06-01", main_content)

        with self.subTest(scenario="When issue has parent/subtasks/links then relationships stored"):
            rels = self.db.get_relationships("K-5")
            types = {r["relation_type"] for r in rels}
            self.assertIn("parent", types)
            self.assertIn("child", types)
            self.assertIn("blocks", types)


# ═══════════════════════════════════════════════════════════════
# _format_summary_block extended branches
# ═══════════════════════════════════════════════════════════════

class TestFormatSummaryBlockExtended(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    def test_format_summary_block_extended(self):
        meta = {
            "status": "In Progress", "status_category": "In Progress",
            "issuetype": "Story", "priority": "Critical",
            "assignee": "Michael", "reporter": "John",
            "duedate": "2026-06-01", "resolution": "Unresolved",
            "labels": ["backend", "urgent"],
            "components": ["API"],
            "fix_versions": ["v2.0"],
        }
        self.db.upsert_summary("K-E", "jira", "Extended Test", "Summary",
                               metadata=meta, mention_type="indirect",
                               estimated_relevance=6, final_relevance=6)
        s = self.db.get_resource_summary("K-E")
        block = _format_summary_block(self.db, "K-E", s, 1, 5)

        with self.subTest(scenario="When summary has labels then shows them"):
            self.assertIn("Labels: backend, urgent", block)

        with self.subTest(scenario="When summary has components then shows them"):
            self.assertIn("Components: API", block)

        with self.subTest(scenario="When summary has fix_versions then shows them"):
            self.assertIn("Fix Versions: v2.0", block)

        with self.subTest(scenario="When summary has all metadata fields then shows them all"):
            self.assertIn("Type: Story", block)
            self.assertIn("Assignee: Michael", block)
            self.assertIn("Reporter: John", block)
            self.assertIn("Due: 2026-06-01", block)
            self.assertIn("Resolution: Unresolved", block)


# ═══════════════════════════════════════════════════════════════
# _load_user_context edge case
# ═══════════════════════════════════════════════════════════════

class TestLoadUserContextEdge(unittest.TestCase):
    @patch("jira._USER_MD_PATH", Path("/nonexistent/User.md"))
    @patch("jira._USER_CONTEXT", None)
    def test_load_user_context_missing_file(self):
        import jira
        original = jira._USER_CONTEXT
        jira._USER_CONTEXT = None
        try:
            result = _load_user_context()
            self.assertEqual(result, "",
                             "When User.md does not exist then returns empty string")
        finally:
            jira._USER_CONTEXT = original


# ═══════════════════════════════════════════════════════════════
# _summarize_one (with mocked LLM)
# ═══════════════════════════════════════════════════════════════

from jira import _summarize_one

class TestSummarizeOne(unittest.TestCase):
    def setUp(self):
        self.db, self.path = _make_db()

    def tearDown(self):
        _cleanup_db(self.db, self.path)

    @patch("jira._call_llm")
    def test_summarize_one_new_resource(self, mock_llm):
        mock_llm.return_value = json.dumps({
            "relevance": 8, "summary": "New summary",
            "work_items": ["K-1"], "people": [], "labels": ["a-b", "c-d", "e-f", "g-h", "i-j"]
        })
        self.db.upsert_atomic("jira", "K-1", "K-1", "Reporter",
                              "Title: Test\nStatus: Open (To Do)",
                              "2026-01-01", "2026-01-01",
                              metadata={"status": "Open", "status_category": "To Do"})

        _summarize_one(self.db, "K-1", force=True, current=1, total=1)
        s = self.db.get_resource_summary("K-1")

        with self.subTest(scenario="When summarizing new resource then stores summary with relevance"):
            self.assertIsNotNone(s)
            self.assertEqual(s["estimated_relevance"], 8)
            self.assertIn("New summary", s["summary"])

    @patch("jira._call_llm")
    def test_summarize_one_cached_skip(self, mock_llm):
        self.db.upsert_atomic("jira", "K-1", "K-1", "A", "Title: T", "2026-01-01", "2026-01-01")
        self.db.upsert_summary("K-1", "jira", "T", "Existing",
                               estimated_relevance=7, final_relevance=7)

        _summarize_one(self.db, "K-1", force=False, current=1, total=1)

        with self.subTest(scenario="When resource already summarized and not stale then skips LLM call"):
            mock_llm.assert_not_called()

    @patch("jira._call_llm")
    def test_summarize_one_empty_summary_raises(self, mock_llm):
        mock_llm.return_value = json.dumps({
            "relevance": 5, "summary": "", "work_items": [], "people": [], "labels": []
        })
        self.db.upsert_atomic("jira", "K-1", "K-1", "A", "Title: T", "2026-01-01", "2026-01-01")

        with self.subTest(scenario="When LLM returns empty summary then raises RuntimeError"):
            with self.assertRaises(RuntimeError):
                _summarize_one(self.db, "K-1", force=True, current=1, total=1)

    @patch("jira._call_llm")
    def test_summarize_one_incremental(self, mock_llm):
        mock_llm.return_value = json.dumps({
            "relevance": 9, "summary": "Updated summary with new info",
            "work_items": [], "people": [], "labels": ["a-b", "c-d", "e-f", "g-h", "i-j"]
        })
        self.db.upsert_atomic("jira", "K-1", "K-1", "A",
                              "Title: T\nStatus: Open (To Do)", "2026-01-01", "2026-01-01")
        self.db.upsert_summary("K-1", "jira", "T", "Old summary",
                               estimated_relevance=5, final_relevance=5)
        self.db.upsert_atomic("jira", "K-1", "c2", "B", "New comment", "2026-06-01", "2099-01-01")

        _summarize_one(self.db, "K-1", force=False, current=1, total=1)
        s = self.db.get_resource_summary("K-1")

        with self.subTest(scenario="When resource has new content then re-summarizes with updated data"):
            self.assertEqual(s["estimated_relevance"], 9)
            self.assertIn("Updated summary", s["summary"])

    def test_summarize_one_no_items(self):
        _summarize_one(self.db, "EMPTY-KEY", force=True, current=1, total=1)
        s = self.db.get_resource_summary("EMPTY-KEY")
        self.assertIsNone(s,
                          "When resource has no atomic items then no summary is created")


# ═══════════════════════════════════════════════════════════════
# View JQL builder edge cases
# ═══════════════════════════════════════════════════════════════

class TestBuildViewJqlEdge(unittest.TestCase):
    def test_build_view_jql_project_rank_mode(self):
        result = _build_view_jql("project = DPD", [], [], "PROJECT_RANK")
        self.assertIn("ORDER BY rank ASC", result,
                      "When sort_mode is PROJECT_RANK then uses rank ASC")

    def test_build_view_jql_empty_filter_values(self):
        filters = [{"field": {"jiraFieldKey": "status"}, "kind": "FIELD_IDENTITY", "values": []}]
        result = _build_view_jql("project = DPD", filters, [], None)
        self.assertEqual(result, "project = DPD",
                         "When filter has empty values then filter is skipped")


# ═══════════════════════════════════════════════════════════════
# _request (mocked HTTP)
# ═══════════════════════════════════════════════════════════════

from jira import _request

class TestRequestFunction(unittest.TestCase):
    @patch("jira.requests.request")
    def test_request_success(self, mock_req):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_req.return_value = mock_resp
        resp = _request("GET", "http://example.com")
        self.assertEqual(resp.status_code, 200,
                         "When request succeeds then returns response")

    @patch("jira.requests.request")
    def test_request_auth_failure(self, mock_req):
        mock_resp = MagicMock()
        mock_resp.status_code = 401
        mock_req.return_value = mock_resp
        with self.assertRaises(SystemExit):
            _request("GET", "http://example.com")

    @patch("jira.requests.request")
    def test_request_not_found(self, mock_req):
        mock_resp = MagicMock()
        mock_resp.status_code = 404
        mock_req.return_value = mock_resp
        with self.assertRaises(SystemExit):
            _request("GET", "http://example.com")

    @patch("jira.requests.request")
    def test_request_timeout_retries(self, mock_req):
        import requests as req
        mock_req.side_effect = [req.exceptions.Timeout("timeout"), req.exceptions.Timeout("timeout"), req.exceptions.Timeout("timeout")]
        with self.assertRaises(SystemExit):
            _request("GET", "http://example.com", retries=3)

    @patch("jira.requests.request")
    def test_request_connection_error(self, mock_req):
        import requests as req
        mock_req.side_effect = req.exceptions.ConnectionError("down")
        with self.assertRaises(SystemExit):
            _request("GET", "http://example.com")


# ═══════════════════════════════════════════════════════════════
# fetch_issues (mocked HTTP)
# ═══════════════════════════════════════════════════════════════

from jira import fetch_issues

class TestFetchIssues(unittest.TestCase):
    @patch("jira._request")
    def test_fetch_issues(self, mock_req):
        cases = [
            ("When API returns issues then returns parsed list and total",
             200, {"issues": [{"key": "K-1"}], "total": 1}, 1, 1),
            ("When API returns empty then returns empty list",
             200, {"issues": [], "total": 0}, 0, 0),
        ]
        for scenario, status, resp_json, expected_len, expected_total in cases:
            with self.subTest(scenario=scenario):
                mock_resp = MagicMock()
                mock_resp.status_code = status
                mock_resp.json.return_value = resp_json
                mock_req.return_value = mock_resp
                issues, total = fetch_issues("project=X", 10, 0, {})
                self.assertEqual(len(issues), expected_len)
                self.assertEqual(total, expected_total)

    @patch("jira._request")
    def test_fetch_issues_errors(self, mock_req):
        cases = [
            ("When API returns 400 then exits with error",
             400, {"errorMessages": ["Bad JQL"]}),
            ("When API returns 500 then exits with error",
             500, {}),
        ]
        for scenario, status, resp_json in cases:
            with self.subTest(scenario=scenario):
                mock_resp = MagicMock()
                mock_resp.status_code = status
                mock_resp.json.return_value = resp_json
                mock_req.return_value = mock_resp
                with self.assertRaises(SystemExit):
                    fetch_issues("bad jql", 10, 0, {})


# ═══════════════════════════════════════════════════════════════
# fetch_filter_jql (mocked HTTP)
# ═══════════════════════════════════════════════════════════════

from jira import fetch_filter_jql

class TestFetchFilterJql(unittest.TestCase):
    @patch("jira._request")
    def test_fetch_filter_jql(self, mock_req):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"name": "My Filter", "jql": "project = DPD"}
        mock_req.return_value = mock_resp
        name, jql = fetch_filter_jql("13811", {})
        self.assertEqual(name, "My Filter",
                         "When filter API succeeds then returns name")
        self.assertEqual(jql, "project = DPD")

    @patch("jira._request")
    def test_fetch_filter_jql_api_error(self, mock_req):
        mock_resp = MagicMock()
        mock_resp.status_code = 403
        mock_req.return_value = mock_resp
        with self.assertRaises(SystemExit):
            fetch_filter_jql("999", {})

    @patch("jira._request")
    def test_fetch_filter_jql_empty_jql(self, mock_req):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"name": "Empty", "jql": ""}
        mock_req.return_value = mock_resp
        with self.assertRaises(SystemExit):
            fetch_filter_jql("999", {})


# ═══════════════════════════════════════════════════════════════
# resolve_view_to_jql (mocked HTTP)
# ═══════════════════════════════════════════════════════════════

from jira import resolve_view_to_jql, _get_cached_view_jql, _set_cached_view_jql

class TestResolveViewToJql(unittest.TestCase):
    @patch("jira._request")
    @patch("jira._get_cached_view_jql", return_value=None)
    @patch("jira._set_cached_view_jql")
    def test_resolve_view_to_jql_success(self, mock_set, mock_get, mock_req):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {
            "data": {"polarisView": {
                "jql": "project = DPD", "userJql": None, "name": "Board",
                "sortMode": None, "sort": [], "filter": [],
            }}
        }
        mock_req.return_value = mock_resp
        jql = resolve_view_to_jql("12345", {}, use_cache=False)
        self.assertEqual(jql, "project = DPD",
                         "When GraphQL returns view then extracts JQL")

    @patch("jira._get_cached_view_jql", return_value="cached = JQL")
    def test_resolve_view_to_jql_cached(self, mock_get):
        jql = resolve_view_to_jql("12345", {}, use_cache=True)
        self.assertEqual(jql, "cached = JQL",
                         "When cache hit then returns cached JQL without API call")

    @patch("jira._request")
    @patch("jira._get_cached_view_jql", return_value=None)
    def test_resolve_view_to_jql_not_found(self, mock_get, mock_req):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"data": {"polarisView": None}}
        mock_req.return_value = mock_resp
        with self.assertRaises(SystemExit):
            resolve_view_to_jql("99999", {}, use_cache=False)

    @patch("jira._request")
    @patch("jira._get_cached_view_jql", return_value=None)
    def test_resolve_view_to_jql_graphql_error(self, mock_get, mock_req):
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_req.return_value = mock_resp
        with self.assertRaises(SystemExit):
            resolve_view_to_jql("12345", {}, use_cache=False)


# ═══════════════════════════════════════════════════════════════
# View cache helpers
# ═══════════════════════════════════════════════════════════════

class TestViewCache(unittest.TestCase):
    def setUp(self):
        self.cache_dir = tempfile.mkdtemp()
        self.cache_file = Path(self.cache_dir) / "test_view_cache.json"

    def tearDown(self):
        import shutil
        shutil.rmtree(self.cache_dir, ignore_errors=True)

    @patch("jira.VIEW_CACHE_FILE")
    def test_view_cache_roundtrip(self, mock_path):
        mock_path.__class__ = Path
        with patch("jira.VIEW_CACHE_FILE", self.cache_file):
            _set_cached_view_jql("123", "project = X")
            result = _get_cached_view_jql("123")
            self.assertEqual(result, "project = X",
                             "When JQL is cached then get returns it")

    @patch("jira.VIEW_CACHE_FILE", Path("/nonexistent/cache.json"))
    def test_view_cache_miss(self):
        result = _get_cached_view_jql("999")
        self.assertIsNone(result,
                          "When cache file does not exist then returns None")


# ═══════════════════════════════════════════════════════════════
# main() function (integration with mocked externals)
# ═══════════════════════════════════════════════════════════════

from jira import main

class TestMain(unittest.TestCase):
    def _make_main_db(self):
        fd, db_path = tempfile.mkstemp(suffix=".db")
        os.close(fd)
        os.unlink(db_path)
        return db_path

    def _cleanup_main(self, output_path, db_path):
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
    def test_main_full_flow(self, mock_llm, mock_env, mock_fetch, mock_filter, mock_view):
        mock_llm.return_value = json.dumps({
            "relevance": 8, "summary": "Main test summary",
            "work_items": ["DPD-1"], "people": ["John"],
            "labels": ["a-b", "c-d", "e-f", "g-h", "i-j"],
        })
        output_path = Path(tempfile.mktemp(suffix=".md"))
        db_path = self._make_main_db()

        _real_open_db = open_db
        def _patched(**kwargs):
            return _real_open_db(db_path, **kwargs)

        try:
            with patch("sys.argv", ["jira.py", "--output", str(output_path), "--force"]), \
                 patch("jira.open_db", side_effect=_patched):
                main()
            self.assertTrue(output_path.exists(),
                            "When main completes successfully then output file is created")
            self.assertIn("Main test summary", output_path.read_text())
        finally:
            self._cleanup_main(output_path, db_path)

    @patch("jira.validate_env", return_value=("a@b.com", "key"))
    @patch("jira.fetch_filter_jql", return_value=("F", "p = X"))
    @patch("jira.resolve_view_to_jql", return_value="p = X")
    @patch("jira.fetch_issues", return_value=([], 0))
    def test_main_no_issues(self, mock_fetch, mock_view, mock_filter, mock_env):
        output_path = Path(tempfile.mktemp(suffix=".md"))
        db_path = self._make_main_db()

        _real_open_db = open_db
        def _patched(**kwargs):
            return _real_open_db(db_path, **kwargs)

        try:
            with patch("sys.argv", ["jira.py", "--output", str(output_path), "--force"]), \
                 patch("jira.open_db", side_effect=_patched):
                main()
            self.assertTrue(output_path.exists(),
                            "When no issues found then output file still created (empty)")
        finally:
            self._cleanup_main(output_path, db_path)

    def test_main_cached_only(self):
        output_path = Path(tempfile.mktemp(suffix=".md"))
        db_path = self._make_main_db()
        try:
            db = open_db(db_path)
            db.upsert_summary("K-1", "jira", "T", "Cached summary",
                              estimated_relevance=7, final_relevance=7)
            db.close()

            _real_open_db = open_db
            def _patched(**kwargs):
                return _real_open_db(db_path, **kwargs)

            with patch("sys.argv", ["jira.py", "--cached-only", "--output", str(output_path)]), \
                 patch("jira.open_db", side_effect=_patched):
                main()
            self.assertTrue(output_path.exists(),
                            "When --cached-only then output is generated from DB without API calls")
            self.assertIn("Cached summary", output_path.read_text())
        finally:
            self._cleanup_main(output_path, db_path)

    def test_main_deletes_stale_output(self):
        output_path = Path(tempfile.mktemp(suffix=".md"))
        db_path = self._make_main_db()
        output_path.write_text("STALE")
        try:
            db = open_db(db_path)
            db.close()

            _real_open_db = open_db
            def _patched(**kwargs):
                return _real_open_db(db_path, **kwargs)

            with patch("sys.argv", ["jira.py", "--cached-only", "--output", str(output_path)]), \
                 patch("jira.open_db", side_effect=_patched):
                main()
            content = output_path.read_text()
            self.assertNotIn("STALE", content,
                             "When stale output exists then it is replaced")
        finally:
            self._cleanup_main(output_path, db_path)


if __name__ == "__main__":
    unittest.main(verbosity=2)


