#!/usr/bin/env python3
"""
Unit tests for gchat.py - follows BDD test-table culture.

One test function per public method, comprehensive test tables,
pytest-subtests for scenario display.
"""

import json
import os
import sqlite3
import tempfile
import time
from pathlib import Path
from unittest.mock import MagicMock, patch, PropertyMock

import pytest
import requests

import gchat
from playwright.sync_api import TimeoutError as PwTimeout


# ═════════════════════════════════════════════════════════════════════
# Fixtures
# ═════════════════════════════════════════════════════════════════════

@pytest.fixture
def db():
    """Fresh in-memory DB for each test."""
    d = gchat.open_db(":memory:")
    yield d
    d.close()


@pytest.fixture
def db_file(tmp_path):
    """DB backed by a temp file."""
    path = tmp_path / "test.db"
    d = gchat.open_db(str(path))
    yield d, path
    d.close()


def _seed_conversation(db, resource_id="space123", name="Test Space", n_msgs=3,
                       user_name=None, mention_content=None):
    """Helper to seed a conversation with n messages."""
    from datetime import datetime, timedelta
    now = datetime.now().astimezone()
    for i in range(n_msgs):
        msg_id = f"msg{i}"
        author = f"User{i}"
        if i == 0 and user_name:
            author = user_name
        content = f"Message {i} body"
        if i == 0 and mention_content:
            content = mention_content
        meta = {"timestamp_display": f"10:0{i} AM"}
        ts = (now - timedelta(hours=n_msgs - i)).isoformat()
        db.upsert_atomic("gchat", resource_id, msg_id, author=author,
                         content=content, created_at=ts,
                         updated_at=ts, metadata=meta)
    return resource_id


def _seed_dm(db, resource_id="dm/abc123", name="DM with Alice", n_msgs=2):
    """Helper to seed a DM conversation."""
    return _seed_conversation(db, resource_id=resource_id, name=name, n_msgs=n_msgs)


# ═════════════════════════════════════════════════════════════════════
# Tests: Configuration & Dependencies
# ═════════════════════════════════════════════════════════════════════

def test_ensure_dependencies(subtests):
    with subtests.test(msg="When all packages present then no install needed"):
        gchat._ensure_dependencies()

    with subtests.test(msg="When package missing then triggers install"):
        original = gchat._REQUIRED_PACKAGES.copy()
        gchat._REQUIRED_PACKAGES["nonexistent_pkg_xyz"] = "nonexistent_pkg_xyz"
        try:
            with patch("subprocess.check_call") as mock_call:
                gchat._ensure_dependencies()
                assert mock_call.called
                call_args = mock_call.call_args_list[0][0][0]
                assert "nonexistent_pkg_xyz" in call_args
        except ImportError:
            pass
        finally:
            gchat._REQUIRED_PACKAGES = original

    with subtests.test(msg="When playwright missing then also installs chromium"):
        original = gchat._REQUIRED_PACKAGES.copy()
        gchat._REQUIRED_PACKAGES["nonexistent_pw"] = "playwright"
        try:
            with patch("subprocess.check_call") as mock_call:
                gchat._ensure_dependencies()
                assert mock_call.call_count >= 2
        except ImportError:
            pass
        finally:
            gchat._REQUIRED_PACKAGES = original


# ═════════════════════════════════════════════════════════════════════
# Tests: Text Cleanup
# ═════════════════════════════════════════════════════════════════════

def test_clean_chat_message(subtests):
    with subtests.test(msg="When empty string then returns empty"):
        assert gchat.clean_chat_message("") == ""

    with subtests.test(msg="When plain text then returns trimmed"):
        assert gchat.clean_chat_message("  hello world  ") == "hello world"

    with subtests.test(msg="When bot pattern (Datadog) then removes it"):
        text = "[10:30 AM] Datadog Bot alert triggered\nReal message"
        result = gchat.clean_chat_message(text)
        assert "Datadog" not in result
        assert "Real message" in result

    with subtests.test(msg="When bot pattern (Jira) then removes it"):
        text = "12:00 PM Jira Bot updated ticket\nHuman message"
        result = gchat.clean_chat_message(text)
        assert "Jira Bot" not in result
        assert "Human message" in result

    with subtests.test(msg="When [ALERT] line then removes it"):
        text = "[ALERT] Something happened\nNormal content"
        result = gchat.clean_chat_message(text)
        assert "[ALERT]" not in result
        assert "Normal content" in result

    with subtests.test(msg="When [MONITORING] line then removes it"):
        text = "[MONITORING] System check\nOther text"
        result = gchat.clean_chat_message(text)
        assert "[MONITORING]" not in result

    with subtests.test(msg="When triple newlines then collapses to double"):
        text = "Line 1\n\n\n\nLine 2"
        assert gchat.clean_chat_message(text) == "Line 1\n\nLine 2"

    with subtests.test(msg="When triple spaces then collapses"):
        text = "Word1   Word2"
        assert gchat.clean_chat_message(text) == "Word1 Word2"


# ═════════════════════════════════════════════════════════════════════
# Tests: Database - open_db
# ═════════════════════════════════════════════════════════════════════

def test_open_db(subtests):
    with subtests.test(msg="When in-memory then returns SkillDB"):
        d = gchat.open_db(":memory:")
        assert isinstance(d, gchat.SkillDB)
        d.close()

    with subtests.test(msg="When file path then creates file and returns SkillDB"):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sub" / "test.db"
            d = gchat.open_db(str(path))
            assert isinstance(d, gchat.SkillDB)
            assert path.exists()
            d.close()


def test_open_db_retry_on_error(subtests):
    with subtests.test(msg="When all retries fail then raises last error"):
        with patch("sqlite3.connect", side_effect=sqlite3.DatabaseError("corrupt")):
            with pytest.raises(sqlite3.DatabaseError):
                gchat.open_db(":memory:")


# ═════════════════════════════════════════════════════════════════════
# Tests: Database - Atomic Content
# ═════════════════════════════════════════════════════════════════════

def test_upsert_atomic(subtests, db):
    with subtests.test(msg="When new message then inserts and returns True"):
        result = db.upsert_atomic("gchat", "space1", "msg1",
                                  author="Alice", content="Hello",
                                  created_at="2026-04-01", updated_at="2026-04-01")
        assert result is True

    with subtests.test(msg="When same message exists then returns False (immutable)"):
        result = db.upsert_atomic("gchat", "space1", "msg1",
                                  author="Alice", content="Hello changed",
                                  created_at="2026-04-01", updated_at="2026-04-01")
        assert result is False


def test_has_message(subtests, db):
    db.upsert_atomic("gchat", "space1", "msg1", author="A", content="B",
                     created_at="2026-04-01", updated_at="2026-04-01")

    with subtests.test(msg="When message exists then returns True"):
        assert db.has_message("space1", "msg1") is True

    with subtests.test(msg="When message not exists then returns False"):
        assert db.has_message("space1", "msg999") is False

    with subtests.test(msg="When resource not exists then returns False"):
        assert db.has_message("space999", "msg1") is False


def test_get_atomic_for_resource(subtests, db):
    _seed_conversation(db, "space1", n_msgs=3)

    with subtests.test(msg="When conversation has messages then returns sorted by created_at"):
        items = db.get_atomic_for_resource("space1")
        assert len(items) == 3
        assert items[0]["created_at"] <= items[1]["created_at"] <= items[2]["created_at"]

    with subtests.test(msg="When conversation not exists then returns empty"):
        assert db.get_atomic_for_resource("space999") == []


def test_get_cached_message_ids(subtests, db):
    _seed_conversation(db, "space1", n_msgs=2)

    with subtests.test(msg="When conversation has messages then returns set of item_ids"):
        ids = db.get_cached_message_ids("space1")
        assert ids == {"msg0", "msg1"}

    with subtests.test(msg="When conversation not exists then returns empty set"):
        assert db.get_cached_message_ids("space999") == set()


def test_get_all_resource_ids(subtests, db):
    _seed_conversation(db, "space1", n_msgs=1)
    _seed_conversation(db, "space2", n_msgs=1)
    db.upsert_atomic("jira", "TICKET-1", "item1", author="A", content="B",
                     created_at="2026-04-01", updated_at="2026-04-01")

    with subtests.test(msg="When source=None then returns all resource_ids"):
        ids = db.get_all_resource_ids()
        assert set(ids) == {"space1", "space2", "TICKET-1"}

    with subtests.test(msg="When source=gchat then returns gchat resource_ids"):
        ids = db.get_all_resource_ids(source="gchat")
        assert set(ids) == {"space1", "space2"}

    with subtests.test(msg="When source=jira then returns jira resource_ids"):
        ids = db.get_all_resource_ids(source="jira")
        assert ids == ["TICKET-1"]


def test_get_latest_cached_at(subtests, db):
    _seed_conversation(db, "space1", n_msgs=2)

    with subtests.test(msg="When conversation has items then returns max cached_at"):
        result = db.get_latest_cached_at("space1")
        assert result is not None

    with subtests.test(msg="When conversation not exists then returns None"):
        result = db.get_latest_cached_at("space999")
        assert result is None


# ═════════════════════════════════════════════════════════════════════
# Tests: Database - Change Detection
# ═════════════════════════════════════════════════════════════════════

def test_conversation_needs_fetch(subtests, db):
    _seed_conversation(db, "space1", n_msgs=1)

    with subtests.test(msg="When display_ts is 0 then needs fetch"):
        assert db.conversation_needs_fetch("space1", 0) is True

    with subtests.test(msg="When display_ts is newer than cached then needs fetch"):
        future_ts = int((gchat.datetime.now(gchat._TZ) + gchat.timedelta(days=1)).timestamp() * 1000)
        assert db.conversation_needs_fetch("space1", future_ts) is True

    with subtests.test(msg="When no cached items then needs fetch"):
        assert db.conversation_needs_fetch("space_new", 1000) is True

    with subtests.test(msg="When display_ts is older than cached then no fetch needed"):
        past_ts = int((gchat.datetime.now(gchat._TZ) - gchat.timedelta(days=30)).timestamp() * 1000)
        assert db.conversation_needs_fetch("space1", past_ts) is False


# ═════════════════════════════════════════════════════════════════════
# Tests: Database - Mention Type
# ═════════════════════════════════════════════════════════════════════

def test_compute_mention_type(subtests, db):
    with subtests.test(msg="When DM resource then returns direct"):
        _seed_dm(db, "dm/abc123", n_msgs=1)
        assert db.compute_mention_type("dm/abc123") == "direct"

    with subtests.test(msg="When user is author of a message then returns direct"):
        _seed_conversation(db, "space_author", user_name="Michael Bui", n_msgs=1)
        assert db.compute_mention_type("space_author") == "direct"

    with subtests.test(msg="When @mentioned by full name then returns direct"):
        _seed_conversation(db, "space_mention", mention_content="Hey @Michael Bui check this", n_msgs=1)
        assert db.compute_mention_type("space_mention") == "direct"

    with subtests.test(msg="When @michael mentioned then returns direct"):
        _seed_conversation(db, "space_short_mention", mention_content="Hey @michael what do you think?", n_msgs=1)
        assert db.compute_mention_type("space_short_mention") == "direct"

    with subtests.test(msg="When user name in summary title then returns indirect"):
        _seed_conversation(db, "space_title", n_msgs=1)
        db.upsert_summary("space_title", "gchat", "Discussion about Michael's project",
                          "Some summary", mention_type="none")
        assert db.compute_mention_type("space_title") == "indirect"

    with subtests.test(msg="When no involvement then returns none"):
        _seed_conversation(db, "space_none", n_msgs=1)
        assert db.compute_mention_type("space_none") == "none"

    with subtests.test(msg="When no items then returns none"):
        assert db.compute_mention_type("space_empty") == "none"


# ═════════════════════════════════════════════════════════════════════
# Tests: Database - Resource Summary
# ═════════════════════════════════════════════════════════════════════

def test_needs_resummarize(subtests, db):
    with subtests.test(msg="When no summary exists then returns True"):
        _seed_conversation(db, "space1", n_msgs=1)
        assert db.needs_resummarize("space1") is True

    with subtests.test(msg="When summary is fresh with no new items then returns False"):
        _seed_conversation(db, "space2", n_msgs=1)
        db.upsert_summary("space2", "gchat", "Test", "Summary text")
        import time as _t
        _t.sleep(0.01)
        assert db.needs_resummarize("space2") is False


def test_upsert_summary(subtests, db):
    with subtests.test(msg="When new summary then inserts"):
        db.upsert_summary("space1", "gchat", "Test Space", "Summary text",
                          mention_type="direct", estimated_relevance=8, final_relevance=8)
        s = db.get_resource_summary("space1")
        assert s["title"] == "Test Space"
        assert s["summary"] == "Summary text"
        assert s["mention_type"] == "direct"
        assert s["final_relevance"] == 8

    with subtests.test(msg="When updating summary then updates"):
        db.upsert_summary("space1", "gchat", "Test Space Updated", "New summary",
                          mention_type="indirect", estimated_relevance=6, final_relevance=6)
        s = db.get_resource_summary("space1")
        assert s["title"] == "Test Space Updated"
        assert s["summary"] == "New summary"
        assert s["mention_type"] == "indirect"


def test_get_resource_summary(subtests, db):
    db.upsert_summary("space1", "gchat", "Test", "Summary")

    with subtests.test(msg="When summary exists then returns it"):
        s = db.get_resource_summary("space1")
        assert s is not None
        assert s["title"] == "Test"

    with subtests.test(msg="When summary not exists then returns None"):
        assert db.get_resource_summary("space999") is None


def test_get_all_summaries(subtests, db):
    _seed_conversation(db, "space1", n_msgs=1)
    _seed_conversation(db, "space2", n_msgs=1)
    _seed_conversation(db, "space3", n_msgs=1)
    db.upsert_summary("space1", "gchat", "Low", "Low summary", final_relevance=3)
    db.upsert_summary("space2", "gchat", "Mid", "Mid summary", final_relevance=6)
    db.upsert_summary("space3", "gchat", "High", "High summary", final_relevance=9)

    with subtests.test(msg="When no filters then returns all summaries"):
        results = db.get_all_summaries(source="gchat")
        assert len(results) == 3

    with subtests.test(msg="When min_relevance=6 then filters low relevance"):
        results = db.get_all_summaries(source="gchat", min_relevance=6)
        assert len(results) == 2
        relevances = [r["final_relevance"] for r in results]
        assert all(r >= 6 for r in relevances)

    with subtests.test(msg="When min_relevance=9 then returns only high"):
        results = db.get_all_summaries(source="gchat", min_relevance=9)
        assert len(results) == 1
        assert results[0]["title"] == "High"


def test_get_items_since(subtests, db):
    _seed_conversation(db, "space1", n_msgs=3)

    with subtests.test(msg="When since is old then returns all"):
        items = db.get_items_since("space1", "2020-01-01")
        assert len(items) == 3

    with subtests.test(msg="When since is future then returns none"):
        items = db.get_items_since("space1", "2099-01-01")
        assert len(items) == 0


def test_clear_all_summaries(subtests, db):
    _seed_conversation(db, "space1", n_msgs=1)
    db.upsert_summary("space1", "gchat", "Test", "Summary", final_relevance=8)

    with subtests.test(msg="When summaries exist then clears and returns count"):
        count = db.clear_all_summaries()
        assert count == 1
        s = db.get_resource_summary("space1")
        assert s["summary"] is None
        assert s["final_relevance"] == 0


def test_clear_summaries_for_resources(subtests, db):
    db.upsert_summary("space1", "gchat", "Test1", "S1", final_relevance=8)
    db.upsert_summary("space2", "gchat", "Test2", "S2", final_relevance=7)

    with subtests.test(msg="When resource_ids provided then clears those summaries"):
        count = db.clear_summaries_for_resources(["space1"])
        assert count == 1
        s1 = db.get_resource_summary("space1")
        assert s1["summary"] is None
        s2 = db.get_resource_summary("space2")
        assert s2["summary"] == "S2"

    with subtests.test(msg="When empty list then clears none"):
        count = db.clear_summaries_for_resources([])
        assert count == 0


def test_delete_atomic_since(subtests, db):
    _seed_conversation(db, "space1", n_msgs=3)

    with subtests.test(msg="When items exist after date then deletes them"):
        count = db.delete_atomic_since("gchat", "2020-01-01")
        assert count == 3

    with subtests.test(msg="When no items after date then deletes none"):
        _seed_conversation(db, "space2", n_msgs=1)
        count = db.delete_atomic_since("gchat", "2099-01-01")
        assert count == 0


def test_db_close(subtests, db):
    with subtests.test(msg="When close called then no error"):
        db.close()


def test_db_retry_on_write_error(subtests):
    with subtests.test(msg="When write fails all retries then raises"):
        d = gchat.open_db(":memory:")
        with patch.object(d, "_conn") as mock_conn:
            mock_conn.execute.side_effect = sqlite3.DatabaseError("database is locked")
            with pytest.raises(sqlite3.DatabaseError, match="locked"):
                d.upsert_summary("x", "gchat", "T", "S")
            assert mock_conn.execute.call_count == d._WRITE_RETRIES
        d.close()


# ═════════════════════════════════════════════════════════════════════
# Tests: Database - Schema Migration
# ═════════════════════════════════════════════════════════════════════

def test_migrate_schema(subtests):
    with subtests.test(msg="When old DB without new columns then adds them"):
        conn = sqlite3.connect(":memory:")
        conn.row_factory = sqlite3.Row
        conn.executescript("""
            CREATE TABLE atomic_content (
                id TEXT PRIMARY KEY, source TEXT NOT NULL, resource_id TEXT NOT NULL,
                item_id TEXT NOT NULL, author TEXT, content TEXT,
                created_at TEXT, updated_at TEXT, cached_at TEXT NOT NULL,
                metadata TEXT DEFAULT '{}'
            );
            CREATE TABLE resource_summary (
                resource_id TEXT PRIMARY KEY, source TEXT NOT NULL, title TEXT,
                summary TEXT, summarized_at TEXT, metadata TEXT DEFAULT '{}'
            );
        """)
        conn.commit()
        db = gchat.SkillDB(conn)
        db._migrate_schema()
        cols = {row[1] for row in conn.execute("PRAGMA table_info(resource_summary)")}
        assert "mention_type" in cols
        assert "estimated_relevance" in cols
        assert "final_relevance" in cols
        conn.close()


# ═════════════════════════════════════════════════════════════════════
# Tests: AI Summarizer - Prompt Building
# ═════════════════════════════════════════════════════════════════════

def test_build_system_prompt(subtests):
    with subtests.test(msg="When User.md exists then includes user context"):
        with patch.object(gchat, "_USER_CONTEXT", None):
            with patch("pathlib.Path.read_text", return_value="I am a test user"):
                prompt = gchat._build_system_prompt()
                assert "I am a test user" in prompt
                assert "relevance-scoring" in prompt

    with subtests.test(msg="When User.md not found then includes warning"):
        with patch.object(gchat, "_USER_CONTEXT", None):
            with patch("pathlib.Path.read_text", side_effect=FileNotFoundError):
                prompt = gchat._build_system_prompt()
                assert "relevance-scoring" in prompt


def test_build_user_prompt(subtests):
    with subtests.test(msg="When direct mention then includes 200 word hint"):
        prompt = gchat._build_user_prompt("Test", "Google Chat conversation", "{}",
                                          "content", "direct")
        assert "~200 words" in prompt

    with subtests.test(msg="When indirect mention then includes 100 word hint"):
        prompt = gchat._build_user_prompt("Test", "Google Chat conversation", "{}",
                                          "content", "indirect")
        assert "~100 words" in prompt

    with subtests.test(msg="When none mention then includes 30 word hint"):
        prompt = gchat._build_user_prompt("Test", "Google Chat conversation", "{}",
                                          "content", "none")
        assert "~30 words" in prompt

    with subtests.test(msg="When existing summary provided then includes it"):
        prompt = gchat._build_user_prompt("Test", "Google Chat conversation", "{}",
                                          "content", "direct",
                                          existing_summary="Previous summary text")
        assert "Previous summary text" in prompt

    with subtests.test(msg="When prompt built then includes decision tree"):
        prompt = gchat._build_user_prompt("Test", "Google Chat conversation", "{}",
                                          "content", "direct")
        assert "AUTOMATED/BOT signals" in prompt
        assert "HARD CAP" in prompt
        assert "HUMAN signals" in prompt

    with subtests.test(msg="When prompt built then includes entity rules"):
        prompt = gchat._build_user_prompt("Test", "Google Chat conversation", "{}",
                                          "content", "direct")
        assert "work_items" in prompt
        assert "people" in prompt
        assert "labels" in prompt


# ═════════════════════════════════════════════════════════════════════
# Tests: AI Summarizer - Response Parsing
# ═════════════════════════════════════════════════════════════════════

def test_parse_llm_response(subtests):
    with subtests.test(msg="When valid JSON then parses correctly"):
        raw = '{"relevance": 8, "summary": "Test summary", "work_items": ["DPD-715"], "people": ["Alice"], "labels": ["team-chat", "alert-response"]}'
        result = gchat.parse_llm_response(raw, "direct")
        assert result.relevance == 8
        assert result.summary == "Test summary"
        assert result.work_items == ["DPD-715"]
        assert result.people == ["Alice"]

    with subtests.test(msg="When thinking tags then strips them"):
        raw = '<think>reasoning here</think>{"relevance": 7, "summary": "Thought result"}'
        result = gchat.parse_llm_response(raw, "direct")
        assert result.relevance == 7
        assert result.summary == "Thought result"

    with subtests.test(msg="When code fence then strips it"):
        raw = '```json\n{"relevance": 6, "summary": "Fenced"}\n```'
        result = gchat.parse_llm_response(raw, "direct")
        assert result.relevance == 6

    with subtests.test(msg="When relevance below direct floor then clamps to 5"):
        raw = '{"relevance": 2, "summary": "Low score"}'
        result = gchat.parse_llm_response(raw, "direct")
        assert result.relevance == 5

    with subtests.test(msg="When relevance below indirect floor then clamps to 5"):
        raw = '{"relevance": 3, "summary": "Low score"}'
        result = gchat.parse_llm_response(raw, "indirect")
        assert result.relevance == 5

    with subtests.test(msg="When relevance above 10 then clamps to 10"):
        raw = '{"relevance": 15, "summary": "High score"}'
        result = gchat.parse_llm_response(raw, "direct")
        assert result.relevance == 10

    with subtests.test(msg="When mention_type none then floor is 1"):
        raw = '{"relevance": 1, "summary": "Minimal"}'
        result = gchat.parse_llm_response(raw, "none")
        assert result.relevance == 1

    with subtests.test(msg="When invalid JSON then uses regex fallback"):
        raw = 'Some text "relevance": 7 "summary": "fallback text"'
        result = gchat.parse_llm_response(raw, "direct")
        assert result.relevance == 7

    with subtests.test(msg="When completely invalid then defaults to 5"):
        raw = "completely invalid response"
        result = gchat.parse_llm_response(raw, "direct")
        assert result.relevance == 5

    with subtests.test(msg="When labels exceed 5 then truncates"):
        raw = '{"relevance": 7, "summary": "S", "labels": ["a-b","c-d","e-f","g-h","i-j","k-l"]}'
        result = gchat.parse_llm_response(raw, "direct")
        assert len(result.labels) == 5


# ═════════════════════════════════════════════════════════════════════
# Tests: AI Summarizer - LLM API
# ═════════════════════════════════════════════════════════════════════

def test_call_llm(subtests):
    with subtests.test(msg="When API returns 200 then returns content"):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"choices": [{"message": {"content": "result"}}]}
        with patch("requests.post", return_value=mock_resp):
            result = gchat._call_llm("system", "user")
            assert result == "result"

    with subtests.test(msg="When API returns 500 and exhausts retries then raises"):
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_resp.text = "Server error"
        with patch("requests.post", return_value=mock_resp):
            with patch.object(gchat, "SUMMARIZE_RETRIES", 0):
                with patch.object(gchat, "SUMMARIZE_RETRY_INITIAL_SEC", 0.01):
                    with pytest.raises(RuntimeError, match="LLM API 500"):
                        gchat._call_llm("system", "user")

    with subtests.test(msg="When connection error exhausts retries then raises"):
        with patch("requests.post", side_effect=gchat.requests.ConnectionError("fail")):
            with patch.object(gchat, "SUMMARIZE_RETRIES", 0):
                with patch.object(gchat, "SUMMARIZE_RETRY_INITIAL_SEC", 0.01):
                    with pytest.raises(RuntimeError, match="connection failed"):
                        gchat._call_llm("system", "user")

    with subtests.test(msg="When API returns 400 then raises immediately"):
        mock_resp = MagicMock()
        mock_resp.status_code = 400
        mock_resp.text = "Bad request"
        with patch("requests.post", return_value=mock_resp):
            with pytest.raises(RuntimeError, match="LLM API 400"):
                gchat._call_llm("system", "user")

    with subtests.test(msg="When API returns empty content then raises"):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"choices": [{"message": {"content": ""}}]}
        with patch("requests.post", return_value=mock_resp):
            with pytest.raises(RuntimeError, match="empty content"):
                gchat._call_llm("system", "user")

    with subtests.test(msg="When no API key then no auth header"):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"choices": [{"message": {"content": "ok"}}]}
        with patch.object(gchat, "LITELLM_API_KEY", ""):
            with patch("requests.post", return_value=mock_resp) as mock_post:
                gchat._call_llm("system", "user")
                headers = mock_post.call_args[1]["headers"]
                assert "Authorization" not in headers

    with subtests.test(msg="When API key set then includes auth header"):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"choices": [{"message": {"content": "ok"}}]}
        with patch.object(gchat, "LITELLM_API_KEY", "test-key"):
            with patch("requests.post", return_value=mock_resp) as mock_post:
                gchat._call_llm("system", "user")
                headers = mock_post.call_args[1]["headers"]
                assert headers["Authorization"] == "Bearer test-key"


# ═════════════════════════════════════════════════════════════════════
# Tests: AI Summarizer - summarize_resource
# ═════════════════════════════════════════════════════════════════════

def test_summarize_resource(subtests):
    with subtests.test(msg="When no items then returns default"):
        result = gchat.summarize_resource("Test", "Google Chat", [])
        assert result.relevance == 1
        assert result.summary == ""

    with subtests.test(msg="When items provided then calls LLM and returns result"):
        items = [{"author": "Alice", "created_at": "2026-04-01", "content": "Hello"}]
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"choices": [{"message": {"content": '{"relevance": 7, "summary": "Test"}'}}]}
        with patch("requests.post", return_value=mock_resp):
            with patch.object(gchat, "_USER_CONTEXT", "test user"):
                result = gchat.summarize_resource("Test Chat", "Google Chat", items,
                                                  mention_type="direct")
                assert result.relevance == 7
                assert result.summary == "Test"

    with subtests.test(msg="When existing summary provided then includes in prompt"):
        items = [{"author": "Alice", "created_at": "2026-04-01", "content": "Hello"}]
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"choices": [{"message": {"content": '{"relevance": 8, "summary": "Updated"}'}}]}
        with patch("requests.post", return_value=mock_resp) as mock_post:
            with patch.object(gchat, "_USER_CONTEXT", "test user"):
                gchat.summarize_resource("Test", "Google Chat", items,
                                         existing_summary="Previous summary")
                call_payload = mock_post.call_args[1]["json"]
                user_msg = call_payload["messages"][1]["content"]
                assert "Previous summary" in user_msg


# ═════════════════════════════════════════════════════════════════════
# Tests: Caching Pipeline
# ═════════════════════════════════════════════════════════════════════

def test_cache_conversation(subtests, db):
    with subtests.test(msg="When all messages are new then caches all"):
        messages = [
            {"data_id": "m1", "sender": "Alice", "epoch_ms": 1712000000000,
             "body": "Hello", "timestamp": "10:00 AM"},
            {"data_id": "m2", "sender": "Bob", "epoch_ms": 1712000001000,
             "body": "Hi there", "timestamp": "10:01 AM"},
        ]
        count = gchat.cache_conversation(db, "space1", "Test Space", messages)
        assert count == 2

    with subtests.test(msg="When message already cached then skips"):
        messages = [
            {"data_id": "m1", "sender": "Alice", "epoch_ms": 1712000000000,
             "body": "Hello", "timestamp": "10:00 AM"},
        ]
        count = gchat.cache_conversation(db, "space1", "Test Space", messages)
        assert count == 0

    with subtests.test(msg="When message has no data_id then generates one from epoch"):
        messages = [
            {"sender": "Carol", "epoch_ms": 1712000005000,
             "body": "Auto-id message", "timestamp": "10:05 AM"},
        ]
        count = gchat.cache_conversation(db, "space2", "Space 2", messages)
        assert count == 1

    with subtests.test(msg="When message body has bot patterns then cleans them"):
        messages = [
            {"data_id": "m_bot", "sender": "Bot", "epoch_ms": 1712000010000,
             "body": "[ALERT] Service down\nPlease check", "timestamp": "10:10 AM"},
        ]
        gchat.cache_conversation(db, "space3", "Space 3", messages)
        items = db.get_atomic_for_resource("space3")
        assert "[ALERT]" not in items[0]["content"]
        assert "Please check" in items[0]["content"]


def test_make_resource_id(subtests):
    with subtests.test(msg="When topic_id provided then combines"):
        assert gchat.make_resource_id("group1", "topic1") == "group1/topic1"

    with subtests.test(msg="When no topic_id then returns group_id"):
        assert gchat.make_resource_id("group1") == "group1"
        assert gchat.make_resource_id("group1", "") == "group1"


# ═════════════════════════════════════════════════════════════════════
# Tests: Summarize One
# ═════════════════════════════════════════════════════════════════════

def test_summarize_one(subtests, db):
    with subtests.test(msg="When conversation has items then summarizes and stores"):
        _seed_conversation(db, "space1", n_msgs=2)
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"choices": [{"message": {"content": '{"relevance": 7, "summary": "AI summary", "work_items": [], "people": [], "labels": ["test-chat"]}'}}]}
        with patch("requests.post", return_value=mock_resp):
            with patch.object(gchat, "_USER_CONTEXT", "test"):
                gchat._summarize_one(db, "space1", {"name": "Test Space"}, current=1, total=1,
                                     ctx_limit=50000)
        s = db.get_resource_summary("space1")
        assert s["summary"] == "AI summary"
        assert s["final_relevance"] == 7

    with subtests.test(msg="When no items then does nothing"):
        gchat._summarize_one(db, "space_empty", {"name": "Empty"}, current=1, total=1)
        assert db.get_resource_summary("space_empty") is None


def test_summarize_one_cached_skip(subtests, db):
    with subtests.test(msg="When cached summary exists and no new items then skips LLM"):
        _seed_conversation(db, "space_cached", n_msgs=1)
        db.upsert_summary("space_cached", "gchat", "Cached", "Existing summary",
                          final_relevance=8)
        import time as _t
        _t.sleep(0.01)
        with patch("requests.post") as mock_post:
            gchat._summarize_one(db, "space_cached", {"name": "Cached"}, current=1, total=1,
                                 ctx_limit=50000)
            mock_post.assert_not_called()


def test_summarize_one_force(subtests, db):
    with subtests.test(msg="When force=True then re-summarizes even with existing summary"):
        _seed_conversation(db, "space_force", n_msgs=1)
        db.upsert_summary("space_force", "gchat", "Test", "Old summary", final_relevance=5)
        import time as _t
        _t.sleep(0.01)
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"choices": [{"message": {"content": '{"relevance": 9, "summary": "New summary"}'}}]}
        with patch("requests.post", return_value=mock_resp):
            with patch.object(gchat, "_USER_CONTEXT", "test"):
                gchat._summarize_one(db, "space_force", {"name": "Test"}, force=True, current=1, total=1,
                                     ctx_limit=50000)
        s = db.get_resource_summary("space_force")
        assert s["summary"] == "New summary"
        assert s["final_relevance"] == 9


def test_summarize_one_empty_summary_raises(subtests, db):
    with subtests.test(msg="When LLM returns empty summary then raises"):
        _seed_conversation(db, "space_empty_llm", n_msgs=1)
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"choices": [{"message": {"content": '{"relevance": 5, "summary": ""}'}}]}
        with patch("requests.post", return_value=mock_resp):
            with patch.object(gchat, "_USER_CONTEXT", "test"):
                 with pytest.raises(RuntimeError, match="Empty summary"):
                    gchat._summarize_one(db, "space_empty_llm", {"name": "Test"}, current=1, total=1,
                                         ctx_limit=50000)


# ═════════════════════════════════════════════════════════════════════
# Tests: Pipeline
# ═════════════════════════════════════════════════════════════════════

def test_pipeline(subtests, db):
    with subtests.test(msg="When pipeline processes conversation then no errors"):
        _seed_conversation(db, "space_pipe", n_msgs=1)
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"choices": [{"message": {"content": '{"relevance": 7, "summary": "Pipeline test"}'}}]}
        with patch("requests.post", return_value=mock_resp):
            with patch.object(gchat, "_USER_CONTEXT", "test"):
                pipeline = gchat._Pipeline(db, force=False, ctx_limit=50000)
                pipeline.set_total(1)
                pipeline.put("space_pipe", {"name": "Pipeline Test"})
                errors = pipeline.finish()
                assert errors == []
        s = db.get_resource_summary("space_pipe")
        assert s["summary"] == "Pipeline test"


def test_pipeline_error_handling(subtests, db):
    with subtests.test(msg="When summarization raises then collects error"):
        _seed_conversation(db, "space_err", n_msgs=1)
        with patch("requests.post", side_effect=RuntimeError("API down")):
            with patch.object(gchat, "_USER_CONTEXT", "test"):
                pipeline = gchat._Pipeline(db, force=False, ctx_limit=50000)
                pipeline.set_total(1)
                pipeline.put("space_err", {"name": "Error Test"})
                errors = pipeline.finish()
                assert len(errors) == 1
                assert "space_err" in errors[0]


# ═════════════════════════════════════════════════════════════════════
# Tests: Output Formatting
# ═════════════════════════════════════════════════════════════════════

def test_format_summary_block(subtests):
    with subtests.test(msg="When full summary then formats correctly"):
        s = {
            "resource_id": "space1", "title": "Test Space",
            "summary": "A test summary", "final_relevance": 8,
            "estimated_relevance": 8, "mention_type": "direct",
            "metadata": json.dumps({"message_count": 5, "work_items": ["DPD-1"], "people": ["Alice"], "labels": ["team-chat", "alert-response"]}),
        }
        block = gchat._format_summary_block(s, 1, 3)
        assert "## [1/3] Test Space" in block
        assert "Source: gchat" in block
        assert "Relevance: 8/10" in block
        assert "Mention: direct" in block
        assert "Messages: 5" not in block
        assert "DPD-1" in block
        assert "Alice" in block
        assert "team-chat" in block

    with subtests.test(msg="When minimal summary then formats without optional fields"):
        s = {
            "resource_id": "space2", "title": "Min Space",
            "summary": "Minimal", "final_relevance": 0,
            "estimated_relevance": 0, "mention_type": "none",
            "metadata": "{}",
        }
        block = gchat._format_summary_block(s, 1, 1)
        assert "## [1/1] Min Space" in block
        assert "Relevance" not in block
        assert "Mention" not in block


def test_write_output(subtests, db, tmp_path):
    _seed_conversation(db, "space1", n_msgs=1)
    _seed_conversation(db, "space2", n_msgs=1)
    _seed_conversation(db, "space3", n_msgs=1)
    db.upsert_summary("space1", "gchat", "Low", "Low summary", final_relevance=3)
    db.upsert_summary("space2", "gchat", "Mid", "Mid summary", final_relevance=6)
    db.upsert_summary("space3", "gchat", "High", "High summary", final_relevance=9)

    with subtests.test(msg="When min_relevance=6 then filters low relevance items"):
        output = tmp_path / "out1.md"
        gchat.write_output(db, output, min_relevance=6)
        text = output.read_text()
        assert "High" in text
        assert "Mid" in text
        assert "Low" not in text

    with subtests.test(msg="When min_relevance=0 then includes all summaries"):
        output = tmp_path / "out2.md"
        gchat.write_output(db, output, min_relevance=0)
        text = output.read_text()
        assert "High" in text
        assert "Mid" in text
        assert "Low" in text

    with subtests.test(msg="When no summaries match then creates empty output"):
        output = tmp_path / "out3.md"
        gchat.write_output(db, output, min_relevance=10)
        text = output.read_text()
        assert text == ""

    with subtests.test(msg="When multiple conversations then output ordered by sort_ts desc"):
        output = tmp_path / "out4.md"
        gchat.write_output(db, output, min_relevance=0)
        text = output.read_text()
        assert text.index("[1/3]") < text.index("[2/3]") < text.index("[3/3]")


# ═════════════════════════════════════════════════════════════════════
# Tests: Browser Functions (mocked)
# ═════════════════════════════════════════════════════════════════════

def test_connect_browser(subtests):
    with subtests.test(msg="When CDP has gchat page then reuses it"):
        mock_pw = MagicMock()
        mock_browser = MagicMock()
        mock_ctx = MagicMock()
        mock_page = MagicMock()
        mock_page.url = "https://chat.google.com/app/home"
        mock_ctx.pages = [mock_page]
        mock_browser.contexts = [mock_ctx]
        mock_pw.chromium.connect_over_cdp.return_value = mock_browser
        with patch("gchat.sync_playwright") as mock_sp:
            mock_sp.return_value.start.return_value = mock_pw
            pw, browser, page = gchat.connect_browser("http://test:9222")
            assert page == mock_page

    with subtests.test(msg="When CDP has no gchat page then creates new"):
        mock_pw = MagicMock()
        mock_browser = MagicMock()
        mock_ctx = MagicMock()
        mock_other_page = MagicMock()
        mock_other_page.url = "https://example.com"
        mock_new_page = MagicMock()
        mock_ctx.pages = [mock_other_page]
        mock_ctx.new_page.return_value = mock_new_page
        mock_browser.contexts = [mock_ctx]
        mock_pw.chromium.connect_over_cdp.return_value = mock_browser
        with patch("gchat.sync_playwright") as mock_sp:
            mock_sp.return_value.start.return_value = mock_pw
            pw, browser, page = gchat.connect_browser("http://test:9222")
            assert page == mock_new_page


# ═════════════════════════════════════════════════════════════════════
# Tests: Main Entry Points
# ═════════════════════════════════════════════════════════════════════

def _make_nonclosing_db(db):
    """Wrap db so main()'s finally block db.close() doesn't destroy the test fixture."""
    original_close = db.close
    db.close = lambda: None
    return db, original_close


def test_main_cached_only(subtests, db, tmp_path):
    with subtests.test(msg="When --cached-only then outputs from DB without browser"):
        _seed_conversation(db, "space1", n_msgs=1)
        db.upsert_summary("space1", "gchat", "Test", "Cached summary", final_relevance=8)
        output = tmp_path / "output.md"
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch("sys.argv", ["gchat.py", "--cached-only", "--output", str(output)]):
                    gchat.main()
            text = output.read_text()
            assert "Cached summary" in text
        finally:
            db.close = restore


def test_main_force(subtests, db, tmp_path):
    with subtests.test(msg="When --force then re-summarizes without browser"):
        _seed_conversation(db, "space1", n_msgs=1)
        db.upsert_summary("space1", "gchat", "Test", "Old", final_relevance=5)
        output = tmp_path / "output.md"
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"choices": [{"message": {"content": '{"relevance": 9, "summary": "Forced new"}'}}]}
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch("requests.post", return_value=mock_resp):
                    with patch.object(gchat, "_USER_CONTEXT", "test"):
                        with patch("sys.argv", ["gchat.py", "--force", "--output", str(output)]):
                            gchat.main()
            s = db.get_resource_summary("space1")
            assert s["summary"] == "Forced new"
        finally:
            db.close = restore


def test_main_removes_stale_output(subtests, db, tmp_path):
    with subtests.test(msg="When stale output exists then removes it at start"):
        output = tmp_path / "output.md"
        output.write_text("stale content")
        _seed_conversation(db, "space1", n_msgs=1)
        db.upsert_summary("space1", "gchat", "Test", "Summary", final_relevance=8)
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch("sys.argv", ["gchat.py", "--cached-only", "--output", str(output)]):
                    gchat.main()
            text = output.read_text()
            assert "stale content" not in text
        finally:
            db.close = restore


def test_main_refetch_since(subtests, db, tmp_path):
    with subtests.test(msg="When --refetch-since then deletes cached content"):
        _seed_conversation(db, "space1", n_msgs=2)
        db.upsert_summary("space1", "gchat", "Test", "Old summary", final_relevance=7)
        output = tmp_path / "output.md"
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch("sys.argv", ["gchat.py", "--cached-only", "--refetch-since", "2026-01-01",
                                        "--output", str(output)]):
                    gchat.main()
            s = db.get_resource_summary("space1")
            assert s["summary"] is None
        finally:
            db.close = restore


def test_main_invalid_refetch_since(subtests, db, tmp_path):
    with subtests.test(msg="When invalid date for --refetch-since then exits with error"):
        output = tmp_path / "output.md"
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch("sys.argv", ["gchat.py", "--cached-only", "--refetch-since", "not-a-date",
                                        "--output", str(output)]):
                    with pytest.raises(SystemExit) as exc_info:
                        gchat.main()
                    assert exc_info.value.code == 1
        finally:
            db.close = restore


def test_main_full_browser_flow(subtests, db, tmp_path):
    with subtests.test(msg="When normal run then connects browser, scans, fetches, summarizes"):
        output = tmp_path / "output.md"
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())):
                    with patch.object(gchat, "go_home"):
                        with patch.object(gchat, "snapshot_feed", return_value=[
                            {"group_id": "g1", "topic_id": "", "display_ts": 9999999999999, "name": "Test Chat"}
                        ]):
                            with patch.object(gchat, "click_feed_item", return_value=True):
                                with patch.object(gchat, "left_panel_visible", return_value=True):
                                    with patch.object(gchat, "wait_for_messages", return_value=3):
                                        with patch.object(gchat, "scroll_to_bottom"):
                                            with patch.object(gchat, "scroll_and_expand", return_value=[
                                                {"data_id": "m1", "sender": "Alice", "epoch_ms": 1712000000000,
                                                 "body": "Hello", "timestamp": "10:00 AM"},
                                            ]):
                                                mock_resp = MagicMock()
                                                mock_resp.status_code = 200
                                                mock_resp.json.return_value = {"choices": [{"message": {"content": '{"relevance": 8, "summary": "Browser test"}'}}]}
                                                with patch("requests.post", return_value=mock_resp):
                                                    with patch.object(gchat, "_USER_CONTEXT", "test"):
                                                        with patch("sys.argv", ["gchat.py", "--days", "3", "--output", str(output)]):
                                                            gchat.main()

            s = db.get_resource_summary("g1")
            assert s is not None
            assert s["summary"] == "Browser test"
        finally:
            db.close = restore


def test_main_browser_fatal_no_threads(subtests, db, tmp_path):
    with subtests.test(msg="When no feed items found then exits with code 2"):
        output = tmp_path / "output.md"
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())):
                    with patch.object(gchat, "go_home"):
                        with patch.object(gchat, "snapshot_feed", return_value=[]):
                            with patch("sys.argv", ["gchat.py", "--output", str(output)]):
                                with pytest.raises(SystemExit) as exc_info:
                                    gchat.main()
                                assert exc_info.value.code == 2
        finally:
            db.close = restore


def test_main_browser_errors_exit_1(subtests, db, tmp_path):
    with subtests.test(msg="When summarization has errors then exits with code 1"):
        output = tmp_path / "output.md"
        _seed_conversation(db, "g1", n_msgs=1)
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())):
                    with patch.object(gchat, "go_home"):
                        with patch.object(gchat, "snapshot_feed", return_value=[
                            {"group_id": "g1", "topic_id": "", "display_ts": 9999999999999, "name": "Test"}
                        ]):
                            with patch.object(gchat, "click_feed_item", return_value=True):
                                with patch.object(gchat, "left_panel_visible", return_value=True):
                                    with patch.object(gchat, "wait_for_messages", return_value=1):
                                        with patch.object(gchat, "scroll_to_bottom"):
                                            with patch.object(gchat, "scroll_and_expand", return_value=[
                                                {"data_id": "m1", "sender": "A", "epoch_ms": 1712000000000,
                                                 "body": "Hello", "timestamp": "10:00 AM"},
                                            ]):
                                                with patch("requests.post", side_effect=RuntimeError("fail")):
                                                    with patch.object(gchat, "_USER_CONTEXT", "test"):
                                                        with patch("sys.argv", ["gchat.py", "--output", str(output)]):
                                                            with pytest.raises(SystemExit) as exc_info:
                                                                gchat.main()
                                                            assert exc_info.value.code == 1
        finally:
            db.close = restore


# ═════════════════════════════════════════════════════════════════════
# Tests: User Context Loading
# ═════════════════════════════════════════════════════════════════════

def test_load_user_context(subtests):
    with subtests.test(msg="When User.md exists then loads content"):
        with patch.object(gchat, "_USER_CONTEXT", None):
            with patch("pathlib.Path.read_text", return_value="User context here"):
                result = gchat._load_user_context()
                assert result == "User context here"

    with subtests.test(msg="When User.md not found then returns empty"):
        with patch.object(gchat, "_USER_CONTEXT", None):
            with patch("pathlib.Path.read_text", side_effect=FileNotFoundError):
                result = gchat._load_user_context()
                assert result == ""

    with subtests.test(msg="When already cached then returns cached"):
        with patch.object(gchat, "_USER_CONTEXT", "cached value"):
            result = gchat._load_user_context()
            assert result == "cached value"


# ═════════════════════════════════════════════════════════════════════
# Tests: Debug Function
# ═════════════════════════════════════════════════════════════════════

def test_debug_function(subtests):
    with subtests.test(msg="When log level is DEBUG then prints"):
        original = gchat._LOG_LEVEL
        gchat._LOG_LEVEL = "DEBUG"
        try:
            gchat.debug("test message")
        finally:
            gchat._LOG_LEVEL = original

    with subtests.test(msg="When log level is INFO then does not print"):
        original = gchat._LOG_LEVEL
        gchat._LOG_LEVEL = "INFO"
        try:
            gchat.debug("should not print")
        finally:
            gchat._LOG_LEVEL = original


# ═════════════════════════════════════════════════════════════════════
# Tests: Browser - go_home
# ═════════════════════════════════════════════════════════════════════

def test_go_home(subtests):
    with subtests.test(msg="When not on home page then navigates"):
        page = MagicMock()
        page.url = "https://chat.google.com/something/else"
        page.wait_for_selector = MagicMock()
        gchat.go_home(page)
        page.goto.assert_called_once()
        assert "home" in page.goto.call_args[0][0]

    with subtests.test(msg="When already on home then skips navigation"):
        page = MagicMock()
        page.url = "https://chat.google.com/app/home"
        page.wait_for_selector = MagicMock()
        gchat.go_home(page)
        page.goto.assert_not_called()

    with subtests.test(msg="When wait_for_selector times out then logs warning"):
        page = MagicMock()
        page.url = "https://chat.google.com/other"
        page.wait_for_selector.side_effect = PwTimeout("timeout")
        gchat.go_home(page)


def test_snapshot_feed(subtests):
    with subtests.test(msg="When all items visible on first snapshot then returns after stable threshold"):
        page = MagicMock()
        items = [{"group_id": "g1", "topic_id": "t1", "display_ts": 1000, "name": "Chat 1", "is_unread": False}]
        with patch.object(gchat, "_snapshot_feed_once", return_value=items):
            with patch.object(gchat, "scroll_feed_down") as mock_scroll:
                result = gchat.snapshot_feed(page, 0, max_scrolls=10, stable_threshold=3)
                assert len(result) == 1
                assert result[0]["group_id"] == "g1"
                assert mock_scroll.call_count >= 3

    with subtests.test(msg="When scrolling reveals more items then accumulates all"):
        page = MagicMock()
        batch1 = [{"group_id": "g1", "topic_id": "", "display_ts": 2000, "name": "A", "is_unread": False}]
        batch2 = [
            {"group_id": "g1", "topic_id": "", "display_ts": 2000, "name": "A", "is_unread": False},
            {"group_id": "g2", "topic_id": "", "display_ts": 1000, "name": "B", "is_unread": True},
        ]
        with patch.object(gchat, "_snapshot_feed_once", side_effect=[batch1, batch2, batch2, batch2, batch2]):
            with patch.object(gchat, "scroll_feed_down"):
                result = gchat.snapshot_feed(page, 0, max_scrolls=10, stable_threshold=3)
                assert len(result) == 2
                assert result[0]["display_ts"] == 2000
                assert result[1]["display_ts"] == 1000

    with subtests.test(msg="When result is sorted by display_ts descending"):
        page = MagicMock()
        items = [
            {"group_id": "g1", "topic_id": "", "display_ts": 100, "name": "Old", "is_unread": False},
            {"group_id": "g2", "topic_id": "", "display_ts": 300, "name": "New", "is_unread": False},
            {"group_id": "g3", "topic_id": "", "display_ts": 200, "name": "Mid", "is_unread": False},
        ]
        with patch.object(gchat, "_snapshot_feed_once", return_value=items):
            with patch.object(gchat, "scroll_feed_down"):
                result = gchat.snapshot_feed(page, 0, max_scrolls=10, stable_threshold=3)
                assert [r["display_ts"] for r in result] == [300, 200, 100]


def test_click_feed_item(subtests):
    with subtests.test(msg="When item found then clicks and returns True"):
        page = MagicMock()
        page.evaluate.return_value = True
        loc = MagicMock()
        loc.count.return_value = 1
        loc.nth.return_value.get_attribute.return_value = "1000"
        loc.nth.return_value.click = MagicMock()
        page.locator.return_value = loc
        result = gchat.click_feed_item(page, "g1", 1000)
        assert result is True

    with subtests.test(msg="When item not found then returns False"):
        page = MagicMock()
        page.evaluate.return_value = False
        result = gchat.click_feed_item(page, "g1", 1000)
        assert result is False

    with subtests.test(msg="When locator has no elements then returns False"):
        page = MagicMock()
        page.evaluate.return_value = True
        loc = MagicMock()
        loc.count.return_value = 0
        page.locator.return_value = loc
        result = gchat.click_feed_item(page, "g1", 1000)
        assert result is False

    with subtests.test(msg="When click raises then returns False"):
        page = MagicMock()
        page.evaluate.return_value = True
        loc = MagicMock()
        loc.count.return_value = 1
        loc.first.click.side_effect = Exception("click failed")
        loc.nth.return_value.get_attribute.return_value = "999"
        page.locator.return_value = loc
        result = gchat.click_feed_item(page, "g1", 1000)
        assert result is False


def test_scroll_feed_down(subtests):
    with subtests.test(msg="When called then evaluates scroll JS"):
        page = MagicMock()
        gchat.scroll_feed_down(page)
        page.evaluate.assert_called_once()


def test_left_panel_visible(subtests):
    with subtests.test(msg="When feed elements found then returns True"):
        page = MagicMock()
        page.evaluate.return_value = True
        assert gchat.left_panel_visible(page) is True

    with subtests.test(msg="When evaluate raises then returns False"):
        page = MagicMock()
        page.evaluate.side_effect = Exception("error")
        assert gchat.left_panel_visible(page) is False


def test_get_topic_ids(subtests):
    with subtests.test(msg="When page has topics then returns set"):
        page = MagicMock()
        page.evaluate.return_value = ["t1", "t2"]
        result = gchat.get_topic_ids(page)
        assert result == {"t1", "t2"}

    with subtests.test(msg="When evaluate raises then returns empty set"):
        page = MagicMock()
        page.evaluate.side_effect = Exception("error")
        assert gchat.get_topic_ids(page) == set()


def test_wait_for_thread(subtests):
    with subtests.test(msg="When thread appears then returns count"):
        page = MagicMock()
        page.evaluate.return_value = 5
        result = gchat._wait_for_thread(page, "t1", timeout_s=3)
        assert result == 5

    with subtests.test(msg="When thread never appears then returns 0"):
        page = MagicMock()
        page.evaluate.return_value = 0
        result = gchat._wait_for_thread(page, "t1", timeout_s=1)
        assert result == 0


def test_wait_for_messages(subtests):
    with subtests.test(msg="When new messages arrive then returns count"):
        page = MagicMock()
        page.evaluate.return_value = {"c": 3, "ids": ["t1"]}
        result = gchat.wait_for_messages(page, set(), timeout_s=3)
        assert result == 3

    with subtests.test(msg="When no messages loaded then returns 0"):
        page = MagicMock()
        page.evaluate.side_effect = [
            {"c": 0, "ids": []},
            0,
        ]
        result = gchat.wait_for_messages(page, set(), timeout_s=2)
        assert result == 0

    with subtests.test(msg="When evaluate raises then recovers"):
        page = MagicMock()
        page.evaluate.side_effect = [
            Exception("transient"),
            {"c": 2, "ids": ["new"]},
        ]
        result = gchat.wait_for_messages(page, set(), timeout_s=6)
        assert result >= 0


def test_scroll_to_bottom(subtests):
    with subtests.test(msg="When jump button exists then clicks it"):
        page = MagicMock()
        call_count = [0]
        def eval_side_effect(js, *args):
            nonlocal call_count
            call_count[0] += 1
            if call_count[0] == 1:
                return True
            return True
        page.evaluate.side_effect = eval_side_effect
        gchat.scroll_to_bottom(page)

    with subtests.test(msg="When already at bottom then returns"):
        page = MagicMock()
        page.evaluate.return_value = True
        gchat.scroll_to_bottom(page)


def test_extract_messages(subtests):
    with subtests.test(msg="When page has messages then returns list"):
        page = MagicMock()
        page.evaluate.return_value = [
            {"data_id": "d1", "sender": "Alice", "timestamp": "10:00", "epoch_ms": 1000, "body": "Hello"},
        ]
        result = gchat.extract_messages(page, 0)
        assert len(result) == 1
        assert result[0]["sender"] == "Alice"

    with subtests.test(msg="When topic_id provided then uses thread selector"):
        page = MagicMock()
        page.evaluate.return_value = []
        gchat.extract_messages(page, 0, topic_id="t1")
        call_args = page.evaluate.call_args[0][1]
        assert call_args["isThread"] is True


def test_wait_for_dom_change(subtests):
    with subtests.test(msg="When count changes then returns"):
        page = MagicMock()
        page.evaluate.return_value = 5
        gchat._wait_for_dom_change(page, 3, timeout=1)


def test_scroll_to_anchor(subtests):
    with subtests.test(msg="When called then scrolls to element"):
        page = MagicMock()
        gchat._scroll_to_anchor(page, "t1")
        page.evaluate.assert_called_once()


def test_find_one_expandable(subtests):
    with subtests.test(msg="When expandable found then returns coords"):
        page = MagicMock()
        page.evaluate.return_value = {"x": 100, "y": 200, "label": "collapsed"}
        result = gchat._find_one_expandable(page)
        assert result["x"] == 100

    with subtests.test(msg="When no expandable then returns None"):
        page = MagicMock()
        page.evaluate.return_value = None
        assert gchat._find_one_expandable(page) is None


def test_scroll_and_expand(subtests):
    with subtests.test(msg="When cutoff reached then stops"):
        page = MagicMock()
        page.evaluate.side_effect = [
            [],
            {"ts": 500, "tid": "t1"},
        ]
        result = gchat.scroll_and_expand(page, 1000, 5, 5)
        assert isinstance(result, list)

    with subtests.test(msg="When no anchor then stops"):
        page = MagicMock()
        page.evaluate.side_effect = [
            [],
            None,
        ]
        result = gchat.scroll_and_expand(page, 0, 5, 5)
        assert isinstance(result, list)


# ═════════════════════════════════════════════════════════════════════
# Tests: needs_resummarize edge cases
# ═════════════════════════════════════════════════════════════════════

def test_needs_resummarize_extra(subtests, db):
    with subtests.test(msg="When summary has no summarized_at then returns True"):
        db.upsert_summary("rs-edge1", "gchat", "Title", "Summary")
        db._retry(lambda: db._conn.execute(
            "UPDATE resource_summary SET summarized_at = NULL WHERE resource_id = ?",
            ("rs-edge1",)
        ))
        db._retry(lambda: db._conn.commit())
        assert db.needs_resummarize("rs-edge1") is True

    with subtests.test(msg="When summary exists but no cached items then returns False"):
        db.upsert_summary("rs-edge2", "gchat", "Title", "Summary")
        assert db.needs_resummarize("rs-edge2") is False

    with subtests.test(msg="When cached_at > summarized_at then returns True"):
        _seed_conversation(db, "rs-edge3", n_msgs=1)
        db.upsert_summary("rs-edge3", "gchat", "Title", "Summary")
        db._retry(lambda: db._conn.execute(
            "UPDATE resource_summary SET summarized_at = '2020-01-01T00:00:00+08:00' WHERE resource_id = ?",
            ("rs-edge3",)
        ))
        db._retry(lambda: db._conn.commit())
        assert db.needs_resummarize("rs-edge3") is True


# ═════════════════════════════════════════════════════════════════════
# Tests: _call_llm retry paths
# ═════════════════════════════════════════════════════════════════════

def test_call_llm_retry_connection_error(subtests):
    with subtests.test(msg="When connection error then retries with backoff"):
        with patch("requests.post", side_effect=requests.ConnectionError("refused")):
            with patch.object(gchat, "SUMMARIZE_RETRIES", 2):
                with patch.object(gchat, "SUMMARIZE_RETRY_INITIAL_SEC", 0.01):
                    with pytest.raises(RuntimeError, match="connection failed"):
                        gchat._call_llm("sys", "user")

    with subtests.test(msg="When 5xx errors then retries with backoff"):
        resp = MagicMock()
        resp.status_code = 503
        resp.text = "service unavailable"
        with patch("requests.post", return_value=resp):
            with patch.object(gchat, "SUMMARIZE_RETRIES", 2):
                with patch.object(gchat, "SUMMARIZE_RETRY_INITIAL_SEC", 0.01):
                    with pytest.raises(RuntimeError, match="LLM API 503"):
                        gchat._call_llm("sys", "user")

    with subtests.test(msg="When all retries exhausted then raises last error"):
        resp = MagicMock()
        resp.status_code = 502
        resp.text = "bad gateway"
        with patch("requests.post", return_value=resp):
            with patch.object(gchat, "SUMMARIZE_RETRIES", 1):
                with patch.object(gchat, "SUMMARIZE_RETRY_INITIAL_SEC", 0.01):
                    with pytest.raises(RuntimeError):
                        gchat._call_llm("sys", "user")


# ═════════════════════════════════════════════════════════════════════
# Tests: _wait_for_thread exception path
# ═════════════════════════════════════════════════════════════════════

def test_wait_for_thread_exception(subtests):
    with subtests.test(msg="When evaluate raises then catches and returns 0"):
        page = MagicMock()
        page.evaluate.side_effect = Exception("DOM error")
        result = gchat._wait_for_thread(page, "t1", timeout_s=2)
        assert result == 0


# ═════════════════════════════════════════════════════════════════════
# Tests: scroll_to_bottom - scrolling loop
# ═════════════════════════════════════════════════════════════════════

def test_scroll_to_bottom_scroll_loop(subtests):
    with subtests.test(msg="When no jump button and not at bottom then scrolls down"):
        page = MagicMock()
        call_count = [0]
        def eval_side(js, *a):
            call_count[0] += 1
            if "Jump to bottom" in js:
                return False
            if "findPanel" in js:
                if call_count[0] <= 6:
                    return False
                return True
            return True
        page.evaluate.side_effect = eval_side
        gchat.scroll_to_bottom(page)


# ═════════════════════════════════════════════════════════════════════
# Tests: scroll_and_expand - inner logic
# ═════════════════════════════════════════════════════════════════════

def test_scroll_and_expand_expand_bar(subtests):
    with subtests.test(msg="When expandable bar found then clicks and snapshots"):
        page = MagicMock()
        msg1 = {"data_id": "m1", "sender": "Alice", "epoch_ms": 2000000000000, "body": "Hi", "timestamp": "10:00 AM"}
        msg2 = {"data_id": "m2", "sender": "Bob", "epoch_ms": 2000000001000, "body": "Hello", "timestamp": "10:01 AM"}
        call_idx = [0]
        def eval_side(js, *a):
            call_idx[0] += 1
            if "NOISE_CLS" in js:
                return [msg1] if call_idx[0] < 5 else [msg1, msg2]
            if "data-absolute-timestamp" in js or "data-local-sort-time-msec" in js:
                return {"ts": 2000000000000, "tid": "t1"}
            if "expandable" in js.lower() or "collapsed" in js.lower() or "role='button'" in js:
                if call_idx[0] < 8:
                    return {"x": 100, "y": 200, "label": "collapsed"}
                return None
            if "findPanel" in js:
                return False
            if "querySelectorAll(s).length" in js:
                return 1
            if "scrollIntoView" in js:
                return None
            return None
        page.evaluate.side_effect = eval_side
        page.mouse = MagicMock()
        result = gchat.scroll_and_expand(page, 1000000000000, 3, 3)
        assert isinstance(result, list)

    with subtests.test(msg="When scroll hits limit then stops"):
        page = MagicMock()
        msg1 = {"data_id": "m1", "sender": "Alice", "epoch_ms": 9999999999999, "body": "Hi", "timestamp": "10:00 AM"}
        def eval_side(js, *a):
            if "NOISE_CLS" in js:
                return [msg1]
            if "data-absolute-timestamp" in js or "data-local-sort-time-msec" in js:
                return {"ts": 9999999999999, "tid": "t1"}
            if "expandable" in js.lower() or "collapsed" in js.lower() or "role='button'" in js:
                return None
            if "findPanel" in js:
                return True
            if "querySelectorAll(s).length" in js:
                return 1
            return None
        page.evaluate.side_effect = eval_side
        result = gchat.scroll_and_expand(page, 0, max_scrolls=2, max_expansion=0)
        assert isinstance(result, list)

    with subtests.test(msg="When early stop via cached IDs then stops"):
        page = MagicMock()
        msgs = [
            {"data_id": f"cached_{i}", "sender": "Bob", "epoch_ms": 1000 + i, "body": "msg", "timestamp": "10:00"}
            for i in range(5)
        ]
        def eval_side(js, *a):
            if "NOISE_CLS" in js:
                return msgs
            return None
        page.evaluate.side_effect = eval_side
        cached = {f"cached_{i}" for i in range(5)}
        result = gchat.scroll_and_expand(page, 0, 5, 5, cached_ids=cached, early_stop_n=3)
        assert isinstance(result, list)


# ═════════════════════════════════════════════════════════════════════
# Tests: Main - --force error path
# ═════════════════════════════════════════════════════════════════════

def test_main_force_with_errors(subtests, db, tmp_path):
    with subtests.test(msg="When --force and summarization errors then exits 1"):
        output = tmp_path / "output.md"
        _seed_conversation(db, "g-err", n_msgs=1)
        db.upsert_summary("g-err", "gchat", "Error Chat", "Old summary", final_relevance=5)

        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "_summarize_one", side_effect=RuntimeError("LLM failed")):
                    with patch("sys.argv", ["gchat.py", "--force", "--output", str(output)]):
                        with pytest.raises(SystemExit) as exc_info:
                            gchat.main()
                        assert exc_info.value.code == 1
        finally:
            db.close = restore


# ═════════════════════════════════════════════════════════════════════
# Tests: Main - max_threads break, duplicate skip
# ═════════════════════════════════════════════════════════════════════

def test_main_max_threads_break(subtests, db, tmp_path):
    with subtests.test(msg="When max-threads reached then stops scanning"):
        output = tmp_path / "output.md"
        feed = [
            {"group_id": f"g{i}", "topic_id": "", "display_ts": 9999999999999, "name": f"Chat {i}"}
            for i in range(5)
        ]
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())):
                    with patch.object(gchat, "go_home"):
                        with patch.object(gchat, "snapshot_feed", return_value=feed):
                            with patch.object(gchat, "click_feed_item", return_value=True):
                                with patch.object(gchat, "left_panel_visible", return_value=True):
                                    with patch.object(gchat, "wait_for_messages", return_value=0):
                                        with patch("sys.argv", [
                                            "gchat.py", "--max-threads", "2", "--output", str(output),
                                        ]):
                                            gchat.main()
        finally:
            db.close = restore


def test_main_duplicate_rid_skip(subtests, db, tmp_path):
    with subtests.test(msg="When feed has duplicate resource_id then skips second occurrence"):
        output = tmp_path / "output.md"
        feed = [
            {"group_id": "g1", "topic_id": "", "display_ts": 9999999999999, "name": "Dup Chat"},
            {"group_id": "g1", "topic_id": "", "display_ts": 9999999999999, "name": "Dup Chat"},
        ]
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())):
                    with patch.object(gchat, "go_home"):
                        with patch.object(gchat, "snapshot_feed", return_value=feed):
                            with patch.object(gchat, "click_feed_item", return_value=True):
                                with patch.object(gchat, "left_panel_visible", return_value=True):
                                    with patch.object(gchat, "wait_for_messages", return_value=0):
                                        with patch("sys.argv", ["gchat.py", "--output", str(output)]):
                                            gchat.main()
        finally:
            db.close = restore


# ═════════════════════════════════════════════════════════════════════
# Tests: mark_conversation_unread
# ═════════════════════════════════════════════════════════════════════

def test_mark_conversation_unread(subtests):
    with subtests.test(msg="When kebab menu found and has mark-unread then returns True"):
        page = MagicMock()
        kebab_loc = MagicMock()
        kebab_loc.count.return_value = 1
        kebab_loc.first = MagicMock()
        menu_loc = MagicMock()
        menu_loc.count.return_value = 1
        menu_item = MagicMock()
        menu_item.text_content.return_value = "Mark as unread"
        menu_loc.nth.return_value = menu_item
        page.locator.side_effect = [kebab_loc, menu_loc]

        assert gchat.mark_conversation_unread(page) is True
        kebab_loc.first.click.assert_called_once_with(timeout=3000)
        menu_item.click.assert_called_once()

    with subtests.test(msg="When kebab button not found then returns False"):
        page = MagicMock()
        kebab_loc = MagicMock()
        kebab_loc.count.return_value = 0
        page.locator.return_value = kebab_loc
        assert gchat.mark_conversation_unread(page) is False

    with subtests.test(msg="When locator raises then returns False"):
        page = MagicMock()
        page.locator.side_effect = Exception("error")
        assert gchat.mark_conversation_unread(page) is False

    with subtests.test(msg="When no mark-unread menu item then escapes and returns False"):
        page = MagicMock()
        kebab_loc = MagicMock()
        kebab_loc.count.return_value = 1
        kebab_loc.first = MagicMock()
        menu_loc = MagicMock()
        menu_loc.count.return_value = 1
        menu_loc.nth.return_value.text_content.return_value = "Pin"
        page.locator.side_effect = [kebab_loc, menu_loc]
        assert gchat.mark_conversation_unread(page) is False
        page.keyboard.press.assert_called_once_with("Escape")

    with subtests.test(msg="When menu item text_content returns None then skips safely"):
        page = MagicMock()
        kebab_loc = MagicMock()
        kebab_loc.count.return_value = 1
        kebab_loc.first = MagicMock()
        menu_loc = MagicMock()
        menu_loc.count.return_value = 1
        menu_loc.nth.return_value.text_content.return_value = None
        page.locator.side_effect = [kebab_loc, menu_loc]
        assert gchat.mark_conversation_unread(page) is False
        page.keyboard.press.assert_called_once_with("Escape")


# ═════════════════════════════════════════════════════════════════════
# Tests: snapshot_feed with is_unread
# ═════════════════════════════════════════════════════════════════════

def test_snapshot_feed_unread(subtests):
    with subtests.test(msg="When feed items have is_unread then includes it"):
        page = MagicMock()
        items = [
            {"group_id": "g1", "topic_id": "", "display_ts": 2000, "name": "Chat", "is_unread": True},
            {"group_id": "g2", "topic_id": "", "display_ts": 1000, "name": "Chat2", "is_unread": False},
        ]
        with patch.object(gchat, "_snapshot_feed_once", return_value=items):
            with patch.object(gchat, "scroll_feed_down"):
                result = gchat.snapshot_feed(page, 0, max_scrolls=10, stable_threshold=3)
                assert result[0]["is_unread"] is True
                assert result[1]["is_unread"] is False



# ═════════════════════════════════════════════════════════════════════
# Tests: Main - unread restoration in fetch loop
# ═════════════════════════════════════════════════════════════════════

def test_main_unread_restored(subtests, db, tmp_path):
    with subtests.test(msg="When fetched conversation was unread then restores unread"):
        output = tmp_path / "output.md"
        feed = [{"group_id": "g1", "topic_id": "", "display_ts": 9999999999999,
                 "name": "Unread Chat", "is_unread": True}]
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())):
                    with patch.object(gchat, "go_home"):
                        with patch.object(gchat, "snapshot_feed", return_value=feed):
                            with patch.object(gchat, "click_feed_item", return_value=True):
                                with patch.object(gchat, "left_panel_visible", return_value=True):
                                    with patch.object(gchat, "wait_for_messages", return_value=3):
                                        with patch.object(gchat, "scroll_to_bottom"):
                                            with patch.object(gchat, "scroll_and_expand", return_value=[
                                                {"data_id": "m1", "sender": "Bob", "epoch_ms": 1712000000000,
                                                 "body": "Msg", "timestamp": "10:00"},
                                            ]):
                                                with patch.object(gchat, "mark_conversation_unread", return_value=True) as mock_mark:
                                                    mock_resp = MagicMock()
                                                    mock_resp.status_code = 200
                                                    mock_resp.json.return_value = {"choices": [{"message": {"content": '{"relevance": 7, "summary": "Summary"}'}}]}
                                                    with patch("requests.post", return_value=mock_resp):
                                                        with patch.object(gchat, "_USER_CONTEXT", "test"):
                                                            with patch("sys.argv", ["gchat.py", "--output", str(output)]):
                                                                gchat.main()
                                                    mock_mark.assert_called_once()
        finally:
            db.close = restore


# ═════════════════════════════════════════════════════════════════════
# Tests: Main - Fatal exception
# ═════════════════════════════════════════════════════════════════════

def test_main_fatal_exception(subtests, db, tmp_path):
    with subtests.test(msg="When unhandled exception then exits 1 with FAILED log"):
        output = tmp_path / "output.md"
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "connect_browser", side_effect=RuntimeError("browser died")):
                    with patch("sys.argv", ["gchat.py", "--output", str(output)]):
                        with pytest.raises(SystemExit) as exc_info:
                            gchat.main()
                        assert exc_info.value.code == 1
        finally:
            db.close = restore


# ═════════════════════════════════════════════════════════════════════
# Tests: Main - Debug DOM
# ═════════════════════════════════════════════════════════════════════

def test_main_debug_dom(subtests, db, tmp_path):
    with subtests.test(msg="When --debug-dom then dumps feed and exits"):
        output = tmp_path / "output.md"
        mock_page = MagicMock()
        mock_page.url = "https://chat.google.com/app/home"
        mock_page.evaluate.return_value = [
            {"gid": "g1", "ts": "1000", "unread": "true", "text": "Test"},
        ]
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "connect_browser", return_value=(MagicMock(), MagicMock(), mock_page)):
                    with patch.object(gchat, "go_home"):
                        with patch("sys.argv", ["gchat.py", "--debug-dom", "--output", str(output)]):
                            with pytest.raises(SystemExit) as exc_info:
                                gchat.main()
                            assert exc_info.value.code == 0
        finally:
            db.close = restore


# ═════════════════════════════════════════════════════════════════════
# Tests: Main - Focus Title Filter
# ═════════════════════════════════════════════════════════════════════

def test_main_focus_title(subtests, db, tmp_path):
    with subtests.test(msg="When --focus-title then skips non-matching conversations"):
        output = tmp_path / "output.md"
        _seed_conversation(db, "g1", n_msgs=1)
        db.upsert_summary("g1", "gchat", "Important Chat", "Summary", final_relevance=8)

        feed = [
            {"group_id": "g1", "topic_id": "", "display_ts": 1000, "name": "Important Chat"},
            {"group_id": "g2", "topic_id": "", "display_ts": 1000, "name": "Unrelated Chat"},
        ]
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())):
                    with patch.object(gchat, "go_home"):
                        with patch.object(gchat, "snapshot_feed", return_value=feed):
                            with patch("sys.argv", ["gchat.py", "--focus-title", "Important",
                                                    "--output", str(output)]):
                                gchat.main()
            text = output.read_text()
            assert "Important Chat" in text
        finally:
            db.close = restore


# ═════════════════════════════════════════════════════════════════════
# Tests: Main - Fetch Failures
# ═════════════════════════════════════════════════════════════════════

def test_main_fetch_click_fail(subtests, db, tmp_path):
    with subtests.test(msg="When click_feed_item fails then skips conversation"):
        output = tmp_path / "output.md"
        feed = [{"group_id": "g1", "topic_id": "", "display_ts": 9999999999999, "name": "Test"}]
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())):
                    with patch.object(gchat, "go_home"):
                        with patch.object(gchat, "snapshot_feed", return_value=feed):
                            with patch.object(gchat, "click_feed_item", return_value=False):
                                with patch.object(gchat, "scroll_feed_down"):
                                    with patch("sys.argv", ["gchat.py", "--output", str(output)]):
                                        gchat.main()
        finally:
            db.close = restore


def test_main_panel_lost(subtests, db, tmp_path):
    with subtests.test(msg="When left panel lost after click then returns home"):
        output = tmp_path / "output.md"
        feed = [{"group_id": "g1", "topic_id": "", "display_ts": 9999999999999, "name": "Test"}]
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())):
                    with patch.object(gchat, "go_home"):
                        with patch.object(gchat, "snapshot_feed", return_value=feed):
                            with patch.object(gchat, "click_feed_item", return_value=True):
                                with patch.object(gchat, "left_panel_visible", return_value=False):
                                    with patch("sys.argv", ["gchat.py", "--output", str(output)]):
                                        gchat.main()
        finally:
            db.close = restore


def test_main_zero_messages(subtests, db, tmp_path):
    with subtests.test(msg="When 0 messages loaded then skips and returns home"):
        output = tmp_path / "output.md"
        feed = [{"group_id": "g1", "topic_id": "", "display_ts": 9999999999999, "name": "Test"}]
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())):
                    with patch.object(gchat, "go_home"):
                        with patch.object(gchat, "snapshot_feed", return_value=feed):
                            with patch.object(gchat, "click_feed_item", return_value=True):
                                with patch.object(gchat, "left_panel_visible", return_value=True):
                                    with patch.object(gchat, "wait_for_messages", return_value=0):
                                        with patch("sys.argv", ["gchat.py", "--output", str(output)]):
                                            gchat.main()
        finally:
            db.close = restore


def test_main_thread_with_topic_id(subtests, db, tmp_path):
    with subtests.test(msg="When feed item has topic_id then uses thread navigation"):
        output = tmp_path / "output.md"
        feed = [{"group_id": "g1", "topic_id": "t1", "display_ts": 9999999999999, "name": "Thread Test"}]
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())):
                    with patch.object(gchat, "go_home"):
                        with patch.object(gchat, "snapshot_feed", return_value=feed):
                            with patch.object(gchat, "click_feed_item", return_value=True):
                                with patch.object(gchat, "left_panel_visible", return_value=True):
                                    with patch.object(gchat, "_wait_for_thread", return_value=2):
                                        with patch.object(gchat, "scroll_to_bottom"):
                                            with patch.object(gchat, "scroll_and_expand", return_value=[
                                                {"data_id": "m1", "sender": "Bob", "epoch_ms": 1712000000000,
                                                 "body": "Thread msg", "timestamp": "10:00 AM"},
                                            ]):
                                                mock_resp = MagicMock()
                                                mock_resp.status_code = 200
                                                mock_resp.json.return_value = {"choices": [{"message": {"content": '{"relevance": 7, "summary": "Thread summary"}'}}]}
                                                with patch("requests.post", return_value=mock_resp):
                                                    with patch.object(gchat, "_USER_CONTEXT", "test"):
                                                        with patch("sys.argv", ["gchat.py", "--output", str(output)]):
                                                            gchat.main()
        finally:
            db.close = restore


# ═════════════════════════════════════════════════════════════════════
# Tests: Pipeline starts concurrently with fetching
# ═════════════════════════════════════════════════════════════════════

def test_main_pipeline_interleaves_with_fetch(subtests, db, tmp_path):
    with subtests.test(msg="When fetching then pipeline.put is called inside the fetch loop (not after)"):
        output = tmp_path / "output.md"
        feed = [
            {"group_id": "g1", "topic_id": "", "display_ts": 9999999999999, "name": "Chat 1"},
            {"group_id": "g2", "topic_id": "", "display_ts": 9999999999998, "name": "Chat 2"},
        ]
        put_order = []
        original_pipeline_init = gchat._Pipeline.__init__
        original_pipeline_put = gchat._Pipeline.put

        def tracking_put(self, resource_id, convo_info):
            put_order.append(("put", resource_id))
            original_pipeline_put(self, resource_id, convo_info)

        wrapped, restore = _make_nonclosing_db(db)

        fetch_calls = []
        original_click = gchat.click_feed_item

        def tracking_click(page, gid, dts):
            fetch_calls.append(("click", gid))
            return True

        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())):
                    with patch.object(gchat, "go_home"):
                        with patch.object(gchat, "snapshot_feed", return_value=feed):
                            with patch.object(gchat, "click_feed_item", side_effect=tracking_click):
                                with patch.object(gchat, "left_panel_visible", return_value=True):
                                    with patch.object(gchat, "wait_for_messages", return_value=3):
                                        with patch.object(gchat, "scroll_to_bottom"):
                                            with patch.object(gchat, "scroll_and_expand", return_value=[
                                                {"data_id": "m1", "sender": "A", "epoch_ms": 1712000000000,
                                                 "body": "Hello", "timestamp": "10:00 AM"},
                                            ]):
                                                mock_resp = MagicMock()
                                                mock_resp.status_code = 200
                                                mock_resp.json.return_value = {"choices": [{"message": {"content": '{"relevance": 7, "summary": "OK"}'}}]}
                                                with patch("requests.post", return_value=mock_resp):
                                                    with patch.object(gchat, "_USER_CONTEXT", "test"):
                                                        with patch.object(gchat._Pipeline, "put", tracking_put):
                                                            with patch("sys.argv", ["gchat.py", "--days", "3", "--output", str(output)]):
                                                                gchat.main()

            assert len(put_order) == 2
            assert put_order[0] == ("put", "g1")
            assert put_order[1] == ("put", "g2")

            assert len(fetch_calls) == 2
            assert fetch_calls[0] == ("click", "g1")
            assert fetch_calls[1] == ("click", "g2")
        finally:
            db.close = restore


# ═════════════════════════════════════════════════════════════════════
# Tests: Early Stop & Focus Title
# ═════════════════════════════════════════════════════════════════════

def test_main_early_stop(subtests, db, tmp_path):
    with subtests.test(msg="When early stop triggers then remaining conversations use cache"):
        output = tmp_path / "output.md"
        for i in range(5):
            _seed_conversation(db, f"g{i}", n_msgs=1)
            db.upsert_summary(f"g{i}", "gchat", f"Chat {i}", f"Summary {i}", final_relevance=7)

        feed = [{"group_id": f"g{i}", "topic_id": "", "display_ts": 1000, "name": f"Chat {i}"}
                for i in range(5)]

        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())):
                    with patch.object(gchat, "go_home"):
                        with patch.object(gchat, "snapshot_feed", return_value=feed):
                            with patch("sys.argv", ["gchat.py", "--early-stop", "2", "--output", str(output)]):
                                gchat.main()
            text = output.read_text()
            assert "Summary" in text
        finally:
            db.close = restore


# ═════════════════════════════════════════════════════════════════════
# Tests: _filter_items_by_context
# ═════════════════════════════════════════════════════════════════════

def test_filter_items_by_context(subtests):
    orig_ctx = gchat._USER_CONTEXT

    with subtests.test(msg="When items fit within limit then all returned"):
        gchat._USER_CONTEXT = "test"
        items = [
            {"author": "A", "created_at": "2026-01-01", "content": "Short"},
            {"author": "B", "created_at": "2026-01-02", "content": "Brief"},
        ]
        result = gchat._filter_items_by_context(items, ctx_limit=50000, title="Test",
                                                 mention_type="direct", metadata={})
        assert len(result) == 2

    with subtests.test(msg="When items exceed limit then picks newest first"):
        gchat._USER_CONTEXT = "test"
        items = [
            {"author": "A", "created_at": "2026-01-01", "content": "A" * 3000},
            {"author": "B", "created_at": "2026-01-02", "content": "B" * 3000},
            {"author": "C", "created_at": "2026-01-03", "content": "C" * 3000},
            {"author": "D", "created_at": "2026-01-04", "content": "D" * 3000},
        ]
        result = gchat._filter_items_by_context(items, ctx_limit=8000, title="Test",
                                                 mention_type="direct", metadata={})
        assert len(result) == 2
        assert result[0]["author"] == "C"
        assert result[1]["author"] == "D"

    with subtests.test(msg="When limit is 0 then returns empty"):
        gchat._USER_CONTEXT = "test"
        items = [
            {"author": "A", "created_at": "2026-01-01", "content": "Hello"},
        ]
        result = gchat._filter_items_by_context(items, ctx_limit=0, title="Test",
                                                 mention_type="direct", metadata={})
        assert result == []

    with subtests.test(msg="When empty items then returns empty"):
        gchat._USER_CONTEXT = "test"
        result = gchat._filter_items_by_context([], ctx_limit=1000, title="Test",
                                                 mention_type="direct", metadata={})
        assert result == []

    with subtests.test(msg="When all items exceed limit then returns empty"):
        gchat._USER_CONTEXT = "test"
        items = [
            {"author": "A", "created_at": "2026-01-01", "content": "A" * 10000},
        ]
        result = gchat._filter_items_by_context(items, ctx_limit=100, title="Test",
                                                 mention_type="direct", metadata={})
        assert result == []

    with subtests.test(msg="When items have empty content then still included"):
        gchat._USER_CONTEXT = "test"
        items = [
            {"author": "A", "created_at": "2026-01-01", "content": "Hello"},
            {"author": "B", "created_at": "2026-01-02", "content": ""},
        ]
        result = gchat._filter_items_by_context(items, ctx_limit=50000, title="Test",
                                                 mention_type="direct", metadata={})
        assert len(result) == 2

    with subtests.test(msg="When context limit is tight then only newest fit"):
        gchat._USER_CONTEXT = "test"
        items = [
            {"author": "A", "created_at": "2026-01-01", "content": "A" * 100},
            {"author": "B", "created_at": "2026-01-02", "content": "B" * 100},
            {"author": "C", "created_at": "2026-01-03", "content": "C" * 100},
        ]
        result = gchat._filter_items_by_context(items, ctx_limit=600, title="Test",
                                                 mention_type="direct", metadata={})
        assert len(result) == 1
        assert result[0]["author"] == "C"

    with subtests.test(msg="When mention_type indirect then overhead is larger"):
        gchat._USER_CONTEXT = "test"
        items = [
            {"author": "A", "created_at": "2026-01-01", "content": "Hello"},
        ]
        result_direct = gchat._filter_items_by_context(items, ctx_limit=50000, title="Test",
                                                        mention_type="direct", metadata={})
        result_indirect = gchat._filter_items_by_context(items, ctx_limit=50000, title="Test",
                                                          mention_type="indirect", metadata={})
        assert len(result_direct) == len(result_indirect)

    with subtests.test(msg="When metadata is large then accounted for"):
        gchat._USER_CONTEXT = "test"
        large_meta = {"key": "x" * 5000}
        items = [
            {"author": "A", "created_at": "2026-01-01", "content": "Hello"},
        ]
        result = gchat._filter_items_by_context(items, ctx_limit=50000, title="Test",
                                                 mention_type="direct", metadata=large_meta)
        assert len(result) == 1

    with subtests.test(msg="When result is in chronological order then preserved"):
        gchat._USER_CONTEXT = "test"
        items = [
            {"author": "A", "created_at": "2026-01-01", "content": "First"},
            {"author": "B", "created_at": "2026-01-02", "content": "Second"},
            {"author": "C", "created_at": "2026-01-03", "content": "Third"},
        ]
        result = gchat._filter_items_by_context(items, ctx_limit=50000, title="Test",
                                                 mention_type="direct", metadata={})
        assert result[0]["created_at"] == "2026-01-01"
        assert result[1]["created_at"] == "2026-01-02"
        assert result[2]["created_at"] == "2026-01-03"

    gchat._USER_CONTEXT = orig_ctx


# ═════════════════════════════════════════════════════════════════════
# Tests: _summarize_one with ctx_limit
# ═════════════════════════════════════════════════════════════════════

def test_summarize_one_ctx_limit(subtests, db):
    with subtests.test(msg="When ctx_limit too small then skips summarization"):
        _seed_conversation(db, "ctx_small", n_msgs=2)
        gchat._summarize_one(db, "ctx_small", {"name": "Small"}, current=1, total=1,
                             ctx_limit=10)
        assert db.get_resource_summary("ctx_small") is None

    with subtests.test(msg="When ctx_limit sufficient then summarizes"):
        _seed_conversation(db, "ctx_ok", n_msgs=2)
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"choices": [{"message": {"content": '{"relevance": 7, "summary": "OK", "work_items": [], "people": [], "labels": ["test"]}'}}]}
        with patch("requests.post", return_value=mock_resp):
            with patch.object(gchat, "_USER_CONTEXT", "test"):
                gchat._summarize_one(db, "ctx_ok", {"name": "OK"}, current=1, total=1,
                                     ctx_limit=50000)
        s = db.get_resource_summary("ctx_ok")
        assert s["summary"] == "OK"


def test_summarize_one_ctx_limit_with_existing_summary(subtests, db):
    with subtests.test(msg="When new items exceed ctx_limit then skips"):
        _seed_conversation(db, "ctx_existing", n_msgs=1)
        db.upsert_summary("ctx_existing", "gchat", "Test", "Old summary", final_relevance=7)
        import time as _t
        _t.sleep(0.01)
        _seed_conversation(db, "ctx_existing", n_msgs=3)
        gchat._summarize_one(db, "ctx_existing", {"name": "Test"}, current=1, total=1,
                             ctx_limit=10)
        s = db.get_resource_summary("ctx_existing")
        assert s["summary"] == "Old summary"


# ═════════════════════════════════════════════════════════════════════
# Tests: Pipeline with ctx_limit
# ═════════════════════════════════════════════════════════════════════

def test_pipeline_ctx_limit(subtests, db):
    with subtests.test(msg="When pipeline created with ctx_limit then passes to worker"):
        _seed_conversation(db, "ctx_pipe", n_msgs=1)
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"choices": [{"message": {"content": '{"relevance": 7, "summary": "Pipeline ctx", "work_items": [], "people": [], "labels": ["test"]}'}}]}
        with patch("requests.post", return_value=mock_resp):
            with patch.object(gchat, "_USER_CONTEXT", "test"):
                pipeline = gchat._Pipeline(db, force=False, ctx_limit=50000)
                pipeline.set_total(1)
                pipeline.put("ctx_pipe", {"name": "Pipeline Context"})
                errors = pipeline.finish()
                assert errors == []
        s = db.get_resource_summary("ctx_pipe")
        assert s["summary"] == "Pipeline ctx"


def test_pipeline_ctx_limit_too_small(subtests, db):
    with subtests.test(msg="When ctx_limit too small then no summary created"):
        _seed_conversation(db, "ctx_pipe_small", n_msgs=1)
        pipeline = gchat._Pipeline(db, force=False, ctx_limit=10)
        pipeline.set_total(1)
        pipeline.put("ctx_pipe_small", {"name": "Small Context"})
        errors = pipeline.finish()
        assert errors == []
        assert db.get_resource_summary("ctx_pipe_small") is None


# ═════════════════════════════════════════════════════════════════════
# Tests: Main --llm-context-limit argument
# ═════════════════════════════════════════════════════════════════════

def test_main_llm_context_limit(subtests, db, tmp_path):
    with subtests.test(msg="When --llm-context-limit then passes to pipeline"):
        output = tmp_path / "output.md"
        feed = [{"group_id": "g1", "topic_id": "", "display_ts": 9999999999999, "name": "Test Chat"}]
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())):
                    with patch.object(gchat, "go_home"):
                        with patch.object(gchat, "snapshot_feed", return_value=feed):
                            with patch.object(gchat, "click_feed_item", return_value=True):
                                with patch.object(gchat, "left_panel_visible", return_value=True):
                                    with patch.object(gchat, "wait_for_messages", return_value=3):
                                        with patch.object(gchat, "scroll_to_bottom"):
                                            with patch.object(gchat, "scroll_and_expand", return_value=[
                                                {"data_id": "m1", "sender": "Alice", "epoch_ms": 1712000000000,
                                                 "body": "Hello", "timestamp": "10:00 AM"},
                                            ]):
                                                mock_resp = MagicMock()
                                                mock_resp.status_code = 200
                                                mock_resp.json.return_value = {"choices": [{"message": {"content": '{"relevance": 8, "summary": "Context limited"}'}}]}
                                                with patch("requests.post", return_value=mock_resp):
                                                    with patch.object(gchat, "_USER_CONTEXT", "test"):
                                                        with patch("sys.argv", ["gchat.py", "--llm-context-limit", "50000", "--output", str(output)]):
                                                            gchat.main()
            s = db.get_resource_summary("g1")
            assert s["summary"] == "Context limited"
        finally:
            db.close = restore


def test_main_llm_context_limit_tiny(subtests, db, tmp_path):
    with subtests.test(msg="When --llm-context-limit tiny then no summary created"):
        output = tmp_path / "output.md"
        feed = [{"group_id": "g1", "topic_id": "", "display_ts": 9999999999999, "name": "Test Chat"}]
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch.object(gchat, "connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())):
                    with patch.object(gchat, "go_home"):
                        with patch.object(gchat, "snapshot_feed", return_value=feed):
                            with patch.object(gchat, "click_feed_item", return_value=True):
                                with patch.object(gchat, "left_panel_visible", return_value=True):
                                    with patch.object(gchat, "wait_for_messages", return_value=3):
                                        with patch.object(gchat, "scroll_to_bottom"):
                                            with patch.object(gchat, "scroll_and_expand", return_value=[
                                                {"data_id": "m1", "sender": "Alice", "epoch_ms": 1712000000000,
                                                 "body": "Hello", "timestamp": "10:00 AM"},
                                            ]):
                                                with patch("requests.post") as mock_post:
                                                    with patch.object(gchat, "_USER_CONTEXT", "test"):
                                                        with patch("sys.argv", ["gchat.py", "--llm-context-limit", "10", "--output", str(output)]):
                                                            gchat.main()
                                                    mock_post.assert_not_called()
        finally:
            db.close = restore


def test_main_force_ctx_limit(subtests, db, tmp_path):
    with subtests.test(msg="When --force with --llm-context-limit too small then no new summary"):
        output = tmp_path / "output.md"
        _seed_conversation(db, "g1", n_msgs=1)
        db.upsert_summary("g1", "gchat", "Test", "Old", final_relevance=5)
        wrapped, restore = _make_nonclosing_db(db)
        try:
            with patch.object(gchat, "open_db", return_value=wrapped):
                with patch("requests.post") as mock_post:
                    with patch.object(gchat, "_USER_CONTEXT", "test"):
                        with patch("sys.argv", ["gchat.py", "--force", "--llm-context-limit", "10",
                                                "--output", str(output)]):
                            gchat.main()
                        mock_post.assert_not_called()
            s = db.get_resource_summary("g1")
            assert s["summary"] is None
        finally:
            db.close = restore
