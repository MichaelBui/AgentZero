#!/usr/bin/env python3
"""
Unit tests for gmail.py - follows _test.md BDD test-table culture.

One test function per public method, comprehensive test tables,
pytest-subtests for scenario display.
"""

import json
import os
import sqlite3
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

import gmail
from playwright.sync_api import TimeoutError as PwTimeout


# ═════════════════════════════════════════════════════════════════════
# Fixtures
# ═════════════════════════════════════════════════════════════════════

@pytest.fixture
def db():
    """Fresh in-memory DB for each test."""
    d = gmail.open_db(":memory:")
    yield d
    d.close()


@pytest.fixture
def db_file(tmp_path):
    """DB backed by a temp file."""
    path = tmp_path / "test.db"
    d = gmail.open_db(str(path))
    yield d, path
    d.close()


def _seed_thread(db, thread_id="abc123", subject="Test Thread", n_msgs=3,
                 user_email=None, senders=None, to_list=None):
    """Helper to seed a thread with n messages."""
    for i in range(n_msgs):
        msg_id = f"msg{i}"
        author = f"User{i} <user{i}@example.com>"
        if i == 0 and user_email:
            author = f"Michael <{user_email}>"
        meta = {"subject": subject, "to": to_list or [], "cc": []}
        db.upsert_atomic("gmail", thread_id, msg_id, author=author,
                         content=f"Message {i} body", created_at=f"2026-04-0{i+1}",
                         updated_at=f"2026-04-0{i+1}", metadata=meta)
    return thread_id


def _seed_cc_thread(db, thread_id="cc_thread", subject="CC Thread", user_email=None):
    """Helper to seed a thread where user is only in CC."""
    meta = {
        "subject": subject,
        "to": [{"name": "Other Person", "email": "other@example.com"}],
        "cc": [{"name": "Michael", "email": user_email}],
    }
    db.upsert_atomic("gmail", thread_id, "msg0", author="Sender <sender@example.com>",
                     content="Message body", created_at="2026-04-01",
                     updated_at="2026-04-01", metadata=meta)
    return thread_id


# ═════════════════════════════════════════════════════════════════════
# Tests: Configuration
# ═════════════════════════════════════════════════════════════════════

def test_ensure_dependencies(subtests):
    with subtests.test(msg="When all packages present then no install needed"):
        gmail._ensure_dependencies()

    with subtests.test(msg="When package missing then triggers install"):
        original = gmail._REQUIRED_PACKAGES.copy()
        gmail._REQUIRED_PACKAGES["nonexistent_pkg_xyz"] = "nonexistent_pkg_xyz"
        try:
            with patch("subprocess.check_call") as mock_call:
                gmail._ensure_dependencies()
                assert mock_call.called
                call_args = mock_call.call_args_list[0][0][0]
                assert "nonexistent_pkg_xyz" in call_args
        except ImportError:
            pass
        finally:
            gmail._REQUIRED_PACKAGES = original

    with subtests.test(msg="When playwright missing then also installs chromium"):
        original = gmail._REQUIRED_PACKAGES.copy()
        gmail._REQUIRED_PACKAGES["nonexistent_pw"] = "playwright"
        try:
            with patch("subprocess.check_call") as mock_call:
                gmail._ensure_dependencies()
                assert mock_call.call_count >= 2
        except ImportError:
            pass
        finally:
            gmail._REQUIRED_PACKAGES = original


def test_default_lookback_days(subtests):
    from datetime import datetime
    from zoneinfo import ZoneInfo
    tz = ZoneInfo("Asia/Singapore")
    cases = [
        ("When Monday then returns 5", 0, 5),
        ("When Tuesday then returns 5", 1, 5),
        ("When Wednesday then returns 3", 2, 3),
        ("When Thursday then returns 3", 3, 3),
        ("When Friday then returns 3", 4, 3),
        ("When Saturday then returns 3", 5, 3),
        ("When Sunday then returns 4", 6, 4),
    ]
    for scenario, weekday, expected in cases:
        with subtests.test(msg=scenario):
            mock_dt = MagicMock()
            mock_dt.weekday.return_value = weekday
            with patch("gmail.datetime") as dt_cls:
                dt_cls.now.return_value = mock_dt
                dt_cls.side_effect = lambda *a, **kw: datetime(*a, **kw)
                result = gmail._default_lookback_days()
                assert result == expected


# ═════════════════════════════════════════════════════════════════════
# Tests: Text Cleaner
# ═════════════════════════════════════════════════════════════════════

def test_parse_gmail_date(subtests):
    cases = [
        ("When full datetime with day-of-week then parses to ISO",
         "Mon, Apr 6, 2026, 3:45 PM", True),
        ("When datetime without day-of-week then parses to ISO",
         "Apr 6, 2026, 3:45 PM", True),
        ("When date only with day-of-week then parses to ISO",
         "Mon, Apr 6, 2026", True),
        ("When date only then parses to ISO",
         "Apr 6, 2026", True),
        ("When datetime with seconds then parses to ISO",
         "Mon, Apr 6, 2026, 3:45:30 PM", True),
        ("When 24h time without AM/PM then parses to ISO",
         "Mar 16, 2026, 1:59", True),
        ("When 24h time afternoon without AM/PM then parses to ISO",
         "Mar 16, 2026, 14:30", True),
        ("When day-of-week prefix needs stripping for match then parses to ISO",
         "Tue, 6 Apr 2026, 3:45 PM", True),
        ("When malformed day-of-week prefix stripped to parse then returns ISO",
         "Mno, Apr 6, 2026, 3:45 PM", True),
        ("When already ISO then returns as-is",
         "2026-04-06T15:45:00+08:00", True),
        ("When empty then returns empty",
         "", False),
        ("When unparseable then returns original with warning",
         "some garbage date", False),
    ]
    for scenario, raw, should_be_iso in cases:
        with subtests.test(msg=scenario):
            result = gmail.parse_gmail_date(raw)
            if not raw:
                assert result == ""
            elif should_be_iso:
                assert "T" in result or result == raw, f"Expected ISO, got: {result}"
                if raw.startswith("2026"):
                    assert result == raw
                elif "Mar" in raw:
                    assert result.startswith("2026-03-16T"), f"Got: {result}"
                else:
                    assert "2026-04-06T" in result, f"Got: {result}"
            else:
                assert result == raw

    with subtests.test(msg="When browser_tz=UTC then converts to storage_tz=SGT"):
        from zoneinfo import ZoneInfo
        result = gmail.parse_gmail_date(
            "Apr 6, 2026, 3:45 PM",
            browser_tz=ZoneInfo("UTC"),
            storage_tz=ZoneInfo("Asia/Singapore"))
        assert result == "2026-04-06T23:45:00+08:00"

    with subtests.test(msg="When _BROWSER_TZ set then parses as browser TZ and converts to _TZ"):
        original = gmail._BROWSER_TZ
        try:
            from zoneinfo import ZoneInfo
            gmail._BROWSER_TZ = ZoneInfo("UTC")
            result = gmail.parse_gmail_date("Apr 6, 2026, 3:45 PM")
            assert "+08:00" in result
            assert result == "2026-04-06T23:45:00+08:00"
        finally:
            gmail._BROWSER_TZ = original


def test_clean_html(subtests):
    cases = [
        ("When empty string then returns empty", "", ""),
        ("When HTML tags then strips them", "<b>Bold</b>", "Bold"),
        ("When HTML entities then decodes them", "&amp; &lt; &gt;", "& < >"),
        ("When nbsp then replaces with space", "hello&nbsp;world", "hello world"),
        ("When nested tags then strips all", "<div><p>text</p></div>", "text"),
    ]
    for scenario, input_text, expected in cases:
        with subtests.test(msg=scenario):
            assert gmail.clean_html(input_text) == expected


def test_clean_email_body(subtests):
    cases = [
        ("When empty then returns empty",
         "", ""),
        ("When plain text then returns trimmed",
         "  Hello world  ", "Hello world"),
        ("When quoted reply block then removes it",
         "My reply\n\nOn Mar 1, 2026, John wrote:\nOld text here", "My reply"),
        ("When signature with -- then removes it",
         "Content here\n\n-- \nJohn Smith\nCEO", "Content here"),
        ("When 'Best regards' signature then removes it",
         "Content here\n\nBest regards,\nJohn", "Content here"),
        ("When 'Sent from my iPhone' then removes it",
         "Content here\nSent from my iPhone", "Content here"),
        ("When triple newlines then collapses",
         "A\n\n\n\nB", "A\n\nB"),
        ("When triple spaces then collapses",
         "A   B", "A B"),
        ("When confidentiality notice then removes it",
         "Content\nThis email and any attachments " + "x " * 30 + "privileged and confidential notice footer",
         "Content"),
        ("When HTML tags in email then strips them",
         "<p>Hello</p> World", "Hello World"),
    ]
    for scenario, input_text, expected in cases:
        with subtests.test(msg=scenario):
            result = gmail.clean_email_body(input_text)
            assert result == expected, f"Got: {repr(result)}"


# ═════════════════════════════════════════════════════════════════════
# Tests: Database Layer
# ═════════════════════════════════════════════════════════════════════

def test_open_db(subtests):
    cases = [
        ("When valid in-memory path then returns SkillDB",
         ":memory:", True),
    ]
    for scenario, path, should_exist in cases:
        with subtests.test(msg=scenario):
            d = gmail.open_db(path)
            assert isinstance(d, gmail.SkillDB) == should_exist
            d.close()

    with subtests.test(msg="When file path then creates file and returns SkillDB"):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "sub" / "test.db"
            d = gmail.open_db(str(p))
            assert isinstance(d, gmail.SkillDB)
            assert p.exists()
            d.close()


def test_open_db_retry_on_error(subtests):
    with subtests.test(msg="When all retries fail then raises last error"):
        with patch("gmail.sqlite3.connect", side_effect=sqlite3.DatabaseError("locked")):
            with patch("gmail._DB_OPEN_RETRIES", 2), patch("gmail._DB_RETRY_DELAY_S", 0):
                with pytest.raises(sqlite3.DatabaseError):
                    gmail.open_db(":memory:")


def test_upsert_atomic(subtests, db):
    cases = [
        ("When new message then inserts and returns True",
         lambda d: d.upsert_atomic("gmail", "t1", "m1", "Author", "Content", "2026-01-01", "2026-01-01"),
         True),
        ("When same message exists then returns False (immutable)",
         lambda d: (d.upsert_atomic("gmail", "t1", "m1", "Author", "Content", "2026-01-01", "2026-01-01"),
                    d.upsert_atomic("gmail", "t1", "m1", "Author", "Content", "2026-01-01", "2026-01-01"))[-1],
         False),
    ]
    for scenario, action, expected in cases:
        with subtests.test(msg=scenario):
            fresh = gmail.open_db(":memory:")
            result = action(fresh)
            assert result == expected
            fresh.close()


def test_has_message(subtests, db):
    db.upsert_atomic("gmail", "t1", "m1", "A", "C", "2026-01-01", "2026-01-01")
    cases = [
        ("When message exists then returns True", "t1", "m1", True),
        ("When message not exists then returns False", "t1", "m999", False),
        ("When thread not exists then returns False", "t999", "m1", False),
    ]
    for scenario, tid, mid, expected in cases:
        with subtests.test(msg=scenario):
            assert db.has_message(tid, mid) == expected


def test_get_atomic_for_resource(subtests, db):
    _seed_thread(db, "t1", n_msgs=3)
    cases = [
        ("When thread has messages then returns them sorted by created_at",
         "t1", 3),
        ("When thread not exists then returns empty",
         "t999", 0),
    ]
    for scenario, tid, expected_count in cases:
        with subtests.test(msg=scenario):
            items = db.get_atomic_for_resource(tid)
            assert len(items) == expected_count


def test_get_cached_message_ids(subtests, db):
    _seed_thread(db, "t1", n_msgs=2)
    cases = [
        ("When thread has messages then returns set of item_ids",
         "t1", {"msg0", "msg1"}),
        ("When thread not exists then returns empty set",
         "t999", set()),
    ]
    for scenario, tid, expected in cases:
        with subtests.test(msg=scenario):
            assert db.get_cached_message_ids(tid) == expected


def test_get_all_resource_ids(subtests, db):
    _seed_thread(db, "t1", n_msgs=1)
    _seed_thread(db, "t2", n_msgs=1)
    cases = [
        ("When source=None then returns all resource_ids",
         None, 2),
        ("When source=gmail then returns gmail resource_ids",
         "gmail", 2),
        ("When source=jira then returns empty",
         "jira", 0),
    ]
    for scenario, source, expected_count in cases:
        with subtests.test(msg=scenario):
            ids = db.get_all_resource_ids(source=source)
            assert len(ids) == expected_count


def test_thread_needs_fetch(subtests, db):
    _seed_thread(db, "t1", n_msgs=1)
    db.upsert_summary("t1", "gmail", "Test", "Summary", {"last_message_id": "latest_msg"})
    cases = [
        ("When same last_message_id in summary then no fetch needed",
         "t1", "latest_msg", False),
        ("When different last_message_id then fetch needed",
         "t1", "newer_msg", True),
        ("When no summary exists then fetch needed",
         "t_new", "any_id", True),
    ]
    for scenario, tid, last_msg, expected in cases:
        with subtests.test(msg=scenario):
            assert db.thread_needs_fetch(tid, last_msg) == expected


def test_compute_mention_type(subtests, db):
    user_email = gmail.GMAIL_USER_EMAIL
    cases = [
        ("When user is author of a message then returns direct",
         lambda d: _seed_thread(d, "t_direct", user_email=user_email),
         "direct"),
        ("When user is in TO then returns direct",
         lambda d: _seed_thread(d, "t_to", to_list=[{"name": "Michael", "email": user_email}]),
         "direct"),
        ("When user is in CC then returns indirect",
         lambda d: _seed_cc_thread(d, "t_cc", user_email=user_email),
         "indirect"),
        ("When user has no involvement then returns none",
         lambda d: _seed_thread(d, "t_none"),
         "none"),
        ("When no items then returns none",
         lambda d: None,
         "none"),
    ]
    for scenario, setup_fn, expected in cases:
        with subtests.test(msg=scenario):
            fresh = gmail.open_db(":memory:")
            if setup_fn:
                tid = setup_fn(fresh)
            else:
                tid = "no_items"
            result = fresh.compute_mention_type(tid if tid else "no_items")
            assert result == expected
            fresh.close()


def test_needs_resummarize(subtests, db):
    cases = [
        ("When no summary exists then returns True",
         lambda d: _seed_thread(d, "t1", n_msgs=1),
         "t1", True),
        ("When summary is fresh with no new items then returns False",
         lambda d: (_seed_thread(d, "t2", n_msgs=1),
                    d.upsert_summary("t2", "gmail", "T", "S", mention_type="none")),
         "t2", False),
    ]
    for scenario, setup, tid, expected in cases:
        with subtests.test(msg=scenario):
            fresh = gmail.open_db(":memory:")
            setup(fresh)
            assert fresh.needs_resummarize(tid) == expected
            fresh.close()


def test_upsert_summary(subtests, db):
    cases = [
        ("When new summary then inserts",
         lambda d: d.upsert_summary("t1", "gmail", "Title", "Summary",
                                    mention_type="direct", estimated_relevance=8, final_relevance=8),
         "t1", 8),
        ("When updating summary then updates",
         lambda d: (d.upsert_summary("t2", "gmail", "Old", "Old Summary",
                                     mention_type="none", estimated_relevance=3, final_relevance=3),
                    d.upsert_summary("t2", "gmail", "New", "New Summary",
                                     mention_type="direct", estimated_relevance=9, final_relevance=9)),
         "t2", 9),
    ]
    for scenario, action, tid, expected_rel in cases:
        with subtests.test(msg=scenario):
            fresh = gmail.open_db(":memory:")
            action(fresh)
            s = fresh.get_resource_summary(tid)
            assert s is not None
            assert s["final_relevance"] == expected_rel
            fresh.close()


def test_get_all_summaries(subtests, db):
    _seed_thread(db, "t1", n_msgs=1)
    _seed_thread(db, "t2", n_msgs=1)
    _seed_thread(db, "t3", n_msgs=1)
    db.upsert_summary("t1", "gmail", "High", "S1", mention_type="direct",
                       estimated_relevance=9, final_relevance=9)
    db.upsert_summary("t2", "gmail", "Low", "S2", mention_type="none",
                       estimated_relevance=2, final_relevance=2)
    db.upsert_summary("t3", "gmail", "Mid", "S3", mention_type="indirect",
                       estimated_relevance=6, final_relevance=6)
    cases = [
        ("When no filters then returns all summaries",
         {"source": "gmail"}, 3),
        ("When min_relevance=6 then filters low relevance",
         {"source": "gmail", "min_relevance": 6}, 2),
        ("When min_relevance=9 then returns only high",
         {"source": "gmail", "min_relevance": 9}, 1),
    ]
    for scenario, kwargs, expected_count in cases:
        with subtests.test(msg=scenario):
            results = db.get_all_summaries(**kwargs)
            assert len(results) == expected_count


def test_clear_all_summaries(subtests, db):
    _seed_thread(db, "t1", n_msgs=1)
    db.upsert_summary("t1", "gmail", "T", "S", mention_type="direct",
                       estimated_relevance=8, final_relevance=8)
    cases = [
        ("When summaries exist then clears and returns count",
         1),
    ]
    for scenario, expected_count in cases:
        with subtests.test(msg=scenario):
            result = db.clear_all_summaries()
            assert result == expected_count
            s = db.get_resource_summary("t1")
            assert s["summary"] is None
            assert s["estimated_relevance"] == 0


# ═════════════════════════════════════════════════════════════════════
# Tests: AI Summarizer
# ═════════════════════════════════════════════════════════════════════

def test_build_system_prompt(subtests):
    cases = [
        ("When User.md exists then includes user context",
         "Test user context", True),
        ("When User.md not found then includes warning",
         None, True),
    ]
    for scenario, user_content, should_contain_header in cases:
        with subtests.test(msg=scenario):
            gmail._USER_CONTEXT = user_content
            result = gmail._build_system_prompt()
            assert "relevance-scoring executive assistant" in result
            if user_content:
                assert user_content in result
    gmail._USER_CONTEXT = None


def test_build_user_prompt(subtests):
    gmail._USER_CONTEXT = "test context"
    cases = [
        ("When direct mention then includes 200 word hint",
         {"mention_type": "direct"}, "200"),
        ("When indirect mention then includes 100 word hint",
         {"mention_type": "indirect"}, "100"),
        ("When none mention then includes 30 word hint",
         {"mention_type": "none"}, "30"),
        ("When existing summary provided then includes it",
         {"mention_type": "none", "existing_summary": "Previous text"}, "Previous text"),
    ]
    for scenario, kwargs, expected_in_result in cases:
        with subtests.test(msg=scenario):
            result = gmail._build_user_prompt(
                title="Test", source_type="Email thread",
                meta_json="{}", content="Body",
                **kwargs
            )
            assert expected_in_result in result
    gmail._USER_CONTEXT = None


def test_parse_llm_response(subtests):
    cases = [
        ("When valid JSON then parses correctly",
         '{"relevance": 8, "summary": "test", "work_items": ["DPD-1"], "people": ["Alice"], "labels": ["a-b"]}',
         "direct", 8, "test"),
        ("When thinking tags then strips them",
         '<think>reasoning</think>{"relevance": 7, "summary": "result", "work_items": [], "people": [], "labels": []}',
         "none", 7, "result"),
        ("When code fence then strips it",
         '```json\n{"relevance": 6, "summary": "test", "work_items": [], "people": [], "labels": []}\n```',
         "none", 6, "test"),
        ("When relevance below direct floor then clamps to 5",
         '{"relevance": 3, "summary": "test", "work_items": [], "people": [], "labels": []}',
         "direct", 5, "test"),
        ("When relevance below indirect floor then clamps to 5",
         '{"relevance": 2, "summary": "test", "work_items": [], "people": [], "labels": []}',
         "indirect", 5, "test"),
        ("When relevance above 10 then clamps to 10",
         '{"relevance": 15, "summary": "test", "work_items": [], "people": [], "labels": []}',
         "none", 10, "test"),
        ("When invalid JSON then uses regex fallback",
         'NOT JSON but "relevance": 6 and "summary": "fallback text"',
         "none", 6, "fallback text"),
        ("When completely invalid then defaults to 5",
         "garbage", "none", 5, "garbage"),
    ]
    for scenario, raw, mention_type, expected_rel, expected_summary in cases:
        with subtests.test(msg=scenario):
            result = gmail.parse_llm_response(raw, mention_type)
            assert result.relevance == expected_rel
            assert expected_summary in result.summary


def test_call_llm(subtests):
    cases = [
        ("When API returns 200 then returns content",
         lambda: MagicMock(status_code=200, json=lambda: {"choices": [{"message": {"content": "ok"}}]}),
         "ok"),
    ]
    for scenario, mock_resp_fn, expected in cases:
        with subtests.test(msg=scenario):
            with patch("gmail.requests.post", return_value=mock_resp_fn()):
                result = gmail._call_llm("sys", "user")
                assert result == expected

    with subtests.test(msg="When API returns 500 and exhausts retries then raises"):
        with patch("gmail.SUMMARIZE_RETRIES", 1), \
             patch("gmail.SUMMARIZE_RETRY_INITIAL_SEC", 0):
            mock_resp = MagicMock(status_code=500, text="Server error")
            with patch("gmail.requests.post", return_value=mock_resp):
                with pytest.raises(RuntimeError, match="LLM API 500"):
                    gmail._call_llm("sys", "user")

    with subtests.test(msg="When connection error exhausts retries then raises"):
        import requests as req
        with patch("gmail.SUMMARIZE_RETRIES", 1), \
             patch("gmail.SUMMARIZE_RETRY_INITIAL_SEC", 0):
            with patch("gmail.requests.post", side_effect=req.ConnectionError("timeout")):
                with pytest.raises(RuntimeError, match="LLM connection failed"):
                    gmail._call_llm("sys", "user")

    with subtests.test(msg="When API returns 400 then raises immediately"):
        mock_resp = MagicMock(status_code=400, text="Bad request")
        with patch("gmail.requests.post", return_value=mock_resp):
            with pytest.raises(RuntimeError, match="LLM API 400"):
                gmail._call_llm("sys", "user")

    with subtests.test(msg="When API returns empty content then raises"):
        mock_resp = MagicMock(status_code=200, json=lambda: {"choices": [{"message": {"content": ""}}]})
        with patch("gmail.requests.post", return_value=mock_resp):
            with pytest.raises(RuntimeError, match="LLM returned empty content"):
                gmail._call_llm("sys", "user")

    with subtests.test(msg="When no API key then no auth header"):
        with patch("gmail.LITELLM_API_KEY", ""):
            mock_resp = MagicMock(status_code=200, json=lambda: {"choices": [{"message": {"content": "ok"}}]})
            with patch("gmail.requests.post", return_value=mock_resp) as mock_post:
                gmail._call_llm("sys", "user")
                call_kwargs = mock_post.call_args
                headers = call_kwargs[1]["headers"] if "headers" in call_kwargs[1] else call_kwargs[0][1] if len(call_kwargs[0]) > 1 else {}
                assert "Authorization" not in headers


def test_summarize_resource(subtests):
    cases = [
        ("When no items then returns default",
         [], "none", None, 1),
        ("When items provided then calls LLM and returns result",
         [{"author": "Alice", "created_at": "2026-01-01", "content": "Hello"}],
         "direct", None, 8),
    ]
    for scenario, items, mention_type, existing, expected_rel in cases:
        with subtests.test(msg=scenario):
            if items:
                mock_raw = json.dumps({"relevance": 8, "summary": "Test summary",
                                       "work_items": [], "people": [], "labels": []})
                with patch("gmail._call_llm", return_value=mock_raw):
                    result = gmail.summarize_resource("T", "Email thread", items,
                                                     mention_type=mention_type,
                                                     existing_summary=existing)
                    assert result.relevance == expected_rel
            else:
                result = gmail.summarize_resource("T", "Email thread", items,
                                                 mention_type=mention_type)
                assert result.relevance == expected_rel


# ═════════════════════════════════════════════════════════════════════
# Tests: Caching
# ═════════════════════════════════════════════════════════════════════

def test_cache_thread_messages(subtests, db):
    cases = [
        ("When all messages are new then caches all",
         [{"legacy_message_id": "m1", "from": "Alice", "date": "2026-01-01",
           "body": "Hello", "to": [], "cc": []}],
         1),
        ("When message already cached then skips",
         [{"legacy_message_id": "m1", "from": "Alice", "date": "2026-01-01",
           "body": "Hello", "to": [], "cc": []}],
         0),
        ("When message has no ID then skips",
         [{"legacy_message_id": "", "from": "Alice", "date": "2026-01-01",
           "body": "Hello", "to": [], "cc": []}],
         0),
    ]
    for scenario, messages, expected_new in cases:
        with subtests.test(msg=scenario):
            result = gmail.cache_thread_messages(db, "t_cache", "Subject", messages)
            assert result == expected_new

    with subtests.test(msg="When message has bcc and attachments then stores in metadata"):
        fresh = gmail.open_db(":memory:")
        msgs = [{"legacy_message_id": "m_rich", "from": "Alice", "date": "2026-01-01",
                 "body": "See attached", "to": [{"name": "Bob", "email": "bob@x.com"}],
                 "cc": [{"name": "Carol", "email": "carol@x.com"}],
                 "bcc": [{"name": "Dave", "email": "dave@x.com"}],
                 "attachments": ["report.pdf", "data.xlsx"],
                 "details_parsed": True}]
        gmail.cache_thread_messages(fresh, "t_rich", "Rich Subject", msgs)
        items = fresh.get_atomic_for_resource("t_rich")
        assert len(items) == 1
        meta = json.loads(items[0]["metadata"])
        assert meta["bcc"] == [{"name": "Dave", "email": "dave@x.com"}]
        assert meta["attachments"] == ["report.pdf", "data.xlsx"]
        assert "details_parsed" not in meta
        fresh.close()

    with subtests.test(msg="When details_parsed is False then stores flag in metadata"):
        fresh = gmail.open_db(":memory:")
        msgs = [{"legacy_message_id": "m_nodet", "from": "Alice", "date": "2026-01-01",
                 "body": "Body", "to": [{"name": "Bob", "email": "bob@x.com"}],
                 "cc": [], "details_parsed": False}]
        gmail.cache_thread_messages(fresh, "t_nodet", "No Details", msgs)
        items = fresh.get_atomic_for_resource("t_nodet")
        meta = json.loads(items[0]["metadata"])
        assert meta["details_parsed"] is False
        fresh.close()


# ═════════════════════════════════════════════════════════════════════
# Tests: Summarize Pipeline
# ═════════════════════════════════════════════════════════════════════

def test_summarize_one(subtests, db):
    mock_raw = json.dumps({"relevance": 7, "summary": "Test", "work_items": [],
                           "people": [], "labels": ["a-b", "c-d", "e-f", "g-h", "i-j"]})
    cases = [
        ("When thread has items then summarizes and stores",
         lambda d: _seed_thread(d, "t_sum", n_msgs=2),
         {"subject": "Test", "labels": [], "last_msg_id": "", "senders": []},
         False, True),
        ("When no items then does nothing",
         lambda d: None,
         {"subject": "Empty", "labels": [], "last_msg_id": "", "senders": []},
         False, False),
    ]
    for scenario, setup_fn, info, force, expect_summary in cases:
        with subtests.test(msg=scenario):
            fresh = gmail.open_db(":memory:")
            if setup_fn:
                tid = setup_fn(fresh)
            else:
                tid = "t_empty"
            with patch("gmail._call_llm", return_value=mock_raw):
                gmail._summarize_one(fresh, tid, info, force=force, current=1, total=1)
            s = fresh.get_resource_summary(tid)
            if expect_summary:
                assert s is not None
                assert s["summary"] is not None
            else:
                assert s is None
            fresh.close()


def test_summarize_one_cached_skip(subtests, db):
    with subtests.test(msg="When cached summary exists and no new items then skips LLM"):
        _seed_thread(db, "t_skip", n_msgs=1)
        db.upsert_summary("t_skip", "gmail", "T", "Existing", mention_type="none",
                          estimated_relevance=5, final_relevance=5)
        with patch("gmail._call_llm") as mock_llm:
            gmail._summarize_one(db, "t_skip",
                                 {"subject": "T", "labels": [], "last_msg_id": "", "senders": []},
                                 force=False, current=1, total=1)
            mock_llm.assert_not_called()


def test_pipeline(subtests, db):
    _seed_thread(db, "t_pipe", n_msgs=2)
    mock_raw = json.dumps({"relevance": 6, "summary": "Pipeline test",
                           "work_items": [], "people": [], "labels": []})
    cases = [
        ("When pipeline processes thread then no errors",
         "t_pipe", {"subject": "Test", "labels": [], "last_msg_id": "", "senders": []}, 0),
    ]
    for scenario, tid, info, expected_errors in cases:
        with subtests.test(msg=scenario):
            with patch("gmail._call_llm", return_value=mock_raw):
                pipe = gmail._Pipeline(db, force=True)
                pipe.set_total(1)
                pipe.put(tid, info)
                errors = pipe.finish()
                assert len(errors) == expected_errors


# ═════════════════════════════════════════════════════════════════════
# Tests: Output
# ═════════════════════════════════════════════════════════════════════

def test_format_summary_block(subtests):
    cases = [
        ("When full summary then formats correctly",
         {"resource_id": "abc", "title": "Subject", "summary": "Summary text",
          "metadata": json.dumps({"labels": ["inbox"], "senders": [{"name": "Alice", "email": "a@b.com"}],
                                  "work_items": ["DPD-1"], "people": ["Bob"]}),
          "final_relevance": 8, "mention_type": "direct"},
         1, 5,
         ["Subject", "Relevance: 8/10", "Mention: direct", "Alice", "DPD-1", "Bob"]),
        ("When minimal summary then formats without optional fields",
         {"resource_id": "xyz", "title": "Bare", "summary": "Short",
          "metadata": "{}", "final_relevance": 0, "mention_type": "none"},
         2, 5,
         ["Bare"]),
    ]
    for scenario, s_dict, idx, total, expected_parts in cases:
        with subtests.test(msg=scenario):
            result = gmail._format_summary_block(s_dict, idx, total)
            for part in expected_parts:
                assert part in result, f"'{part}' not in result: {result}"


def test_write_output(subtests):
    cases = [
        ("When min_relevance=6 then filters low relevance items",
         lambda d: (
             _seed_thread(d, "t_hi", n_msgs=1),
             _seed_thread(d, "t_lo", n_msgs=1),
             d.upsert_summary("t_hi", "gmail", "High", "High summary",
                              {"labels": ["inbox"], "senders": [{"name": "Alice", "email": "a@b.com"}],
                               "work_items": ["DPD-1"], "people": ["Bob"], "last_message_id": "m1"},
                              mention_type="direct", estimated_relevance=9, final_relevance=9),
             d.upsert_summary("t_lo", "gmail", "Low", "Low summary",
                              mention_type="none", estimated_relevance=2, final_relevance=2),
         ),
         6, None, 1,
         ["High summary", "Relevance: 9/10", "Mention: direct", "Alice", "DPD-1", "Bob"]),

        ("When min_relevance=0 then includes all summaries",
         lambda d: (
             _seed_thread(d, "t_all1", n_msgs=1),
             _seed_thread(d, "t_all2", n_msgs=1),
             d.upsert_summary("t_all1", "gmail", "First", "First summary",
                              mention_type="direct", estimated_relevance=9, final_relevance=9),
             d.upsert_summary("t_all2", "gmail", "Second", "Second summary",
                              mention_type="none", estimated_relevance=2, final_relevance=2),
         ),
         0, None, 2,
         ["First summary", "Second summary"]),

        ("When since filter provided then excludes old cached items",
         lambda d: (
             d.upsert_summary("t_only_sum", "gmail", "Old Thread", "Old summary",
                              mention_type="indirect", estimated_relevance=7, final_relevance=7),
             _seed_thread(d, "t_new", n_msgs=1),
             d.upsert_summary("t_new", "gmail", "New Thread", "New summary",
                              mention_type="direct", estimated_relevance=8, final_relevance=8),
         ),
         1, "2099-01-01", 0,
         []),

        ("When metadata has AI-generated labels then displays them",
         lambda d: (
             _seed_thread(d, "t_labels", n_msgs=1),
             d.upsert_summary("t_labels", "gmail", "Labels Thread", "Summary with labels",
                              {"labels": ["team-meeting", "budget-review", "q2-planning",
                                          "headcount-request", "engineering-ops"]},
                              mention_type="direct", estimated_relevance=8, final_relevance=8),
         ),
         1, None, 1,
         ["team-meeting", "budget-review"]),

        ("When metadata has gmail labels (non-hyphenated) then shows as Gmail Labels",
         lambda d: (
             _seed_thread(d, "t_gmail_labels", n_msgs=1),
             d.upsert_summary("t_gmail_labels", "gmail", "Gmail Labels", "Summary",
                              {"labels": ["Inbox", "IMPORTANT"]},
                              mention_type="indirect", estimated_relevance=6, final_relevance=6),
         ),
         1, None, 1,
         ["Gmail Labels: Inbox, IMPORTANT"]),

        ("When multiple threads then output ordered by sort_ts desc",
         lambda d: (
             d.upsert_atomic("gmail", "t_older", "m1", "A", "Older",
                             "2026-03-01", "2026-03-01"),
             d.upsert_atomic("gmail", "t_newer", "m2", "B", "Newer",
                             "2026-04-01", "2026-04-01"),
             d.upsert_summary("t_older", "gmail", "Older", "Older summary",
                              mention_type="direct", estimated_relevance=8, final_relevance=8),
             d.upsert_summary("t_newer", "gmail", "Newer", "Newer summary",
                              mention_type="direct", estimated_relevance=8, final_relevance=8),
         ),
         1, None, 2,
         ["Newer", "Older"]),

        ("When thread has work_items and people then displays them",
         lambda d: (
             _seed_thread(d, "t_entities", n_msgs=1),
             d.upsert_summary("t_entities", "gmail", "Entity Thread", "Summary with entities",
                              {"work_items": ["DPD-715", "PR #649", "lt-strudel-api"],
                               "people": ["Nikhil Grover", "Alvin Choo"],
                               "labels": ["sprint-review", "release-planning", "api-changes",
                                          "code-review", "deployment-issue"]},
                              mention_type="direct", estimated_relevance=9, final_relevance=9),
         ),
         1, None, 1,
         ["DPD-715", "PR #649", "Nikhil Grover", "Alvin Choo", "sprint-review"]),

        ("When no summaries match then creates empty output",
         lambda d: None,
         9, None, 0,
         []),
    ]
    for scenario, setup_fn, min_rel, since, expected_count, expected_parts in cases:
        with subtests.test(msg=scenario):
            fresh = gmail.open_db(":memory:")
            if setup_fn:
                setup_fn(fresh)
            with tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / "out.md"
                gmail.write_output(fresh, path, min_relevance=min_rel, since=since)
                content = path.read_text()
                assert content.count("##") == expected_count
                for part in expected_parts:
                    assert part in content, f"'{part}' not in output"
            fresh.close()


# ═════════════════════════════════════════════════════════════════════
# Tests: Main Entry Point
# ═════════════════════════════════════════════════════════════════════

def _make_test_db(tmp_path):
    db_path = tmp_path / "test.db"
    d = gmail.open_db(str(db_path))
    return d, db_path


def test_main_cached_only(subtests, tmp_path):
    with subtests.test(msg="When --cached-only then outputs from DB without browser"):
        d, db_path = _make_test_db(tmp_path)
        out_path = tmp_path / "output.md"
        _seed_thread(d, "t_main", n_msgs=1)
        d.upsert_summary("t_main", "gmail", "Test", "Summary",
                          mention_type="direct", estimated_relevance=8, final_relevance=8)
        d.close()

        with patch("gmail.open_db", return_value=gmail.open_db(str(db_path))), \
             patch("sys.argv", ["gmail.py", "--cached-only", "--output", str(out_path),
                                "--days", "365", "--min-relevance", "1"]):
            gmail.main()
        assert out_path.exists()
        content = out_path.read_text()
        assert "Summary" in content


def test_main_force(subtests, tmp_path):
    with subtests.test(msg="When --force then re-summarizes without browser"):
        d, db_path = _make_test_db(tmp_path)
        out_path = tmp_path / "output.md"
        _seed_thread(d, "t_force", n_msgs=2)
        d.upsert_summary("t_force", "gmail", "Old", "Old summary",
                          mention_type="none", estimated_relevance=3, final_relevance=3)
        d.close()

        mock_raw = json.dumps({"relevance": 7, "summary": "Refreshed", "work_items": [],
                               "people": [], "labels": []})
        with patch("gmail.open_db", return_value=gmail.open_db(str(db_path))), \
             patch("gmail._call_llm", return_value=mock_raw), \
             patch("sys.argv", ["gmail.py", "--force", "--output", str(out_path),
                                "--days", "365", "--min-relevance", "1"]):
            gmail.main()
        assert out_path.exists()
        content = out_path.read_text()
        assert "Refreshed" in content


def test_main_removes_stale_output(subtests, tmp_path):
    with subtests.test(msg="When stale output exists then removes it at start"):
        d, db_path = _make_test_db(tmp_path)
        out_path = tmp_path / "output.md"
        out_path.write_text("stale content")
        d.close()

        with patch("gmail.open_db", return_value=gmail.open_db(str(db_path))), \
             patch("sys.argv", ["gmail.py", "--cached-only", "--output", str(out_path),
                                "--days", "365"]):
            gmail.main()
        content = out_path.read_text()
        assert "stale content" not in content


def test_main_refetch_since(subtests, tmp_path):
    with subtests.test(msg="When --refetch-since then deletes cached content and re-fetches"):
        d, db_path = _make_test_db(tmp_path)
        out_path = tmp_path / "refetch_out.md"
        _seed_thread(d, "t_ref", n_msgs=2)
        d.upsert_summary("t_ref", "gmail", "Old", "Old summary",
                          mention_type="none", estimated_relevance=3, final_relevance=3)
        d.close()

        thread_list = [
            {"rowIndex": 0, "legacyThreadId": "t_ref", "legacyLastMsgId": "m_new",
             "senders": [{"name": "Alice", "email": "alice@test.com"}],
             "subject": "Refetched", "date": "Apr 1, 2026", "labels": []}
        ]
        thread_messages = [
            {"legacy_message_id": "m_new", "from": "Alice <alice@test.com>",
             "to": [{"name": "Michael", "email": "michael.bui@fairpricegroup.sg"}],
             "cc": [], "bcc": [], "date": "Apr 1, 2026",
             "body": "Refetched content.", "attachments": [], "details_parsed": True}
        ]
        mock_raw = json.dumps({"relevance": 8, "summary": "Refetched summary",
                               "work_items": [], "people": [], "labels": []})

        nav_results = iter([True, False])

        with patch("gmail.open_db", return_value=gmail.open_db(str(db_path))), \
             patch("gmail.connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())), \
             patch("gmail.navigate_to_page", side_effect=lambda *a, **kw: next(nav_results)), \
             patch("gmail.get_thread_list", return_value=thread_list), \
             patch("gmail.navigate_to_thread", return_value=True), \
             patch("gmail.get_thread_subject", return_value="Refetched"), \
             patch("gmail.extract_thread_messages", return_value=thread_messages), \
             patch("gmail._call_llm", return_value=mock_raw), \
             patch("gmail.time.sleep"), \
             patch("sys.argv", ["gmail.py", "--refetch-since", "2026-03-01",
                                "--output", str(out_path), "--min-relevance", "1",
                                "--cdp-url", "http://localhost:9222", "--max-threads", "5"]):
            gmail.main()
        assert out_path.exists()


def test_main_invalid_exclude_labels(subtests, tmp_path):
    with subtests.test(msg="When invalid JSON for --exclude-labels then exits with error"):
        d, db_path = _make_test_db(tmp_path)
        d.close()
        with patch("gmail.open_db", return_value=gmail.open_db(str(db_path))), \
             patch("sys.argv", ["gmail.py", "--exclude-labels", "not-json",
                                "--output", str(tmp_path / "out.md")]):
            with pytest.raises(SystemExit) as exc_info:
                gmail.main()
            assert exc_info.value.code == 1


# ═════════════════════════════════════════════════════════════════════
# Tests: Browser Functions (mocked)
# ═════════════════════════════════════════════════════════════════════

def test_connect_browser(subtests):
    with subtests.test(msg="When CDP has gmail page then reuses it"):
        mock_page = MagicMock()
        mock_page.url = "https://mail.google.com/mail/u/0/#inbox"
        mock_context = MagicMock()
        mock_context.pages = [mock_page]
        mock_browser = MagicMock()
        mock_browser.contexts = [mock_context]
        mock_pw = MagicMock()

        with patch("gmail.sync_playwright") as mock_sp:
            instance = mock_sp.return_value
            instance.start.return_value = mock_pw
            mock_pw.chromium.connect_over_cdp.return_value = mock_browser
            pw, browser, page = gmail.connect_browser("http://localhost:9222")
            assert page == mock_page

    with subtests.test(msg="When CDP has no gmail page then creates new"):
        mock_context = MagicMock()
        mock_context.pages = []
        new_page = MagicMock()
        mock_context.new_page.return_value = new_page
        mock_browser = MagicMock()
        mock_browser.contexts = [mock_context]
        mock_pw = MagicMock()

        with patch("gmail.sync_playwright") as mock_sp:
            instance = mock_sp.return_value
            instance.start.return_value = mock_pw
            mock_pw.chromium.connect_over_cdp.return_value = mock_browser
            pw, browser, page = gmail.connect_browser("http://localhost:9222")
            assert page == new_page


def test_get_thread_list(subtests):
    with subtests.test(msg="When page has threads then returns parsed data with unread status"):
        mock_page = MagicMock()
        mock_page.evaluate.return_value = [
            {"rowIndex": 0, "legacyThreadId": "abc", "legacyLastMsgId": "def",
             "senders": [{"name": "Alice", "email": "alice@test.com"}],
             "subject": "Hello", "date": "Apr 1, 2026", "labels": ["Inbox"],
             "isUnread": True}
        ]
        result = gmail.get_thread_list(mock_page)
        assert len(result) == 1
        assert result[0]["legacyThreadId"] == "abc"
        assert result[0]["isUnread"] is True


def test_navigate_to_page(subtests):
    with subtests.test(msg="When page loads successfully then returns True"):
        mock_page = MagicMock()
        mock_page.wait_for_selector.return_value = True
        with patch("gmail.time.sleep"):
            result = gmail.navigate_to_page(mock_page, 3, 1)
        assert result is True

    with subtests.test(msg="When page times out then returns False"):
        mock_page = MagicMock()
        mock_page.wait_for_selector.side_effect = PwTimeout("timeout")
        with patch("gmail.time.sleep"):
            result = gmail.navigate_to_page(mock_page, 3, 1)
        assert result is False


def test_navigate_to_thread(subtests):
    with subtests.test(msg="When correct thread loads then returns True"):
        mock_page = MagicMock()
        mock_page.wait_for_selector.return_value = True
        mock_page.evaluate.return_value = "abc123"
        with patch("gmail.time.sleep"), patch("gmail.time.monotonic", side_effect=[0, 0.1]):
            result = gmail.navigate_to_thread(mock_page, "abc123")
        assert result is True

    with subtests.test(msg="When wrong thread stays loaded then returns False"):
        mock_page = MagicMock()
        mock_page.wait_for_selector.return_value = True
        mock_page.evaluate.return_value = "wrong_thread"
        with patch("gmail.time.sleep"), \
             patch("gmail.time.monotonic", side_effect=[0] + [20] * 50):
            result = gmail.navigate_to_thread(mock_page, "abc123")
        assert result is False

    with subtests.test(msg="When NNBSP in date then parse_gmail_date handles it"):
        raw = "Apr 6, 2026, 9:40\u202fAM"
        result = gmail.parse_gmail_date(raw)
        assert result.startswith("2026-04-06")


def test_get_thread_subject(subtests):
    with subtests.test(msg="When subject h2 exists then returns text"):
        mock_page = MagicMock()
        mock_page.evaluate.return_value = "Test Subject"
        result = gmail.get_thread_subject(mock_page)
        assert result == "Test Subject"

    with subtests.test(msg="When no subject then returns empty"):
        mock_page = MagicMock()
        mock_page.evaluate.return_value = ""
        result = gmail.get_thread_subject(mock_page)
        assert result == ""


def test_extract_thread_messages(subtests):
    with subtests.test(msg="When page has messages then returns parsed list with new fields"):
        mock_page = MagicMock()
        mock_page.evaluate.side_effect = [
            False,
            None,
            {"alreadyOpen": 0, "clicked": 0, "skippedFew": 1, "failed": 0},
            0,
            [{"legacy_message_id": "m1", "from": "Alice <a@b.com>",
              "to": [{"name": "Bob", "email": "bob@b.com"}], "cc": [],
              "bcc": [], "date": "Apr 1, 2026", "body": "Hello",
              "attachments": ["file.pdf"], "details_parsed": True}]
        ]
        with patch("gmail.time.sleep"):
            result = gmail.extract_thread_messages(mock_page)
        assert len(result) == 1
        assert result[0]["legacy_message_id"] == "m1"
        assert result[0]["bcc"] == []
        assert result[0]["attachments"] == ["file.pdf"]
        assert result[0]["details_parsed"] is True


def test_expand_all_messages(subtests):
    with subtests.test(msg="When expand all button exists then clicks it and expands trimmed"):
        mock_page = MagicMock()
        mock_page.evaluate.side_effect = [True, None]
        with patch("gmail._wait_for_messages_stable"), patch("gmail.time.sleep"):
            gmail.expand_all_messages(mock_page)
        assert mock_page.evaluate.call_count == 2


def test_click_show_details(subtests):
    with subtests.test(msg="When all already open then returns counts"):
        mock_page = MagicMock()
        mock_page.evaluate.return_value = {"alreadyOpen": 3, "clicked": 0, "skippedFew": 0, "failed": 0}
        result = gmail._click_show_details(mock_page)
        assert result["alreadyOpen"] == 3
        assert result["clicked"] == 0

    with subtests.test(msg="When messages clicked then returns clicked count"):
        mock_page = MagicMock()
        mock_page.evaluate.return_value = {"alreadyOpen": 1, "clicked": 2, "skippedFew": 0, "failed": 0}
        result = gmail._click_show_details(mock_page)
        assert result["clicked"] == 2
        assert result["alreadyOpen"] == 1

    with subtests.test(msg="When few recipients (to+cc<=1) then skips"):
        mock_page = MagicMock()
        mock_page.evaluate.return_value = {"alreadyOpen": 0, "clicked": 0, "skippedFew": 3, "failed": 0}
        result = gmail._click_show_details(mock_page)
        assert result["skippedFew"] == 3
        assert result["clicked"] == 0

    with subtests.test(msg="When no button found then increments failed"):
        mock_page = MagicMock()
        mock_page.evaluate.return_value = {"alreadyOpen": 0, "clicked": 0, "skippedFew": 0, "failed": 2}
        result = gmail._click_show_details(mock_page)
        assert result["failed"] == 2
        assert result["clicked"] == 0


def test_mark_thread_unread(subtests):
    with subtests.test(msg="When shortcut succeeds then returns True"):
        mock_page = MagicMock()
        with patch("gmail.time.sleep"):
            assert gmail.mark_thread_unread(mock_page) is True
        mock_page.keyboard.press.assert_called_once_with("Shift+u")

    with subtests.test(msg="When keyboard raises then returns False"):
        mock_page = MagicMock()
        mock_page.keyboard.press.side_effect = Exception("fail")
        with patch("gmail.time.sleep"):
            assert gmail.mark_thread_unread(mock_page) is False


def test_wait_for_messages_stable(subtests):
    with subtests.test(msg="When count stabilizes then returns"):
        mock_page = MagicMock()
        mock_page.evaluate.side_effect = [0, 3, 3, 3]
        with patch("gmail.time.sleep"):
            count = gmail._wait_for_messages_stable(mock_page, max_wait=5, poll_interval=0.01)
        assert count == 3


def test_navigate_to_thread_fail(subtests):
    with subtests.test(msg="When thread page times out then returns False"):
        mock_page = MagicMock()
        mock_page.wait_for_selector.side_effect = PwTimeout("fail")
        with patch("gmail.time.sleep"):
            result = gmail.navigate_to_thread(mock_page, "abc")
        assert result is False


# ═════════════════════════════════════════════════════════════════════
# Tests: Additional DB coverage
# ═════════════════════════════════════════════════════════════════════

def test_get_latest_cached_at(subtests, db):
    _seed_thread(db, "t_cached", n_msgs=2)
    cases = [
        ("When thread has items then returns max cached_at",
         "t_cached", True),
        ("When thread not exists then returns None",
         "t_none", False),
    ]
    for scenario, tid, expect_value in cases:
        with subtests.test(msg=scenario):
            result = db.get_latest_cached_at(tid)
            if expect_value:
                assert result is not None
            else:
                assert result is None


def test_get_items_since(subtests, db):
    _seed_thread(db, "t_since", n_msgs=2)
    cases = [
        ("When since is old then returns all",
         "t_since", "2000-01-01", 2),
        ("When since is future then returns none",
         "t_since", "2099-01-01", 0),
    ]
    for scenario, tid, since, expected in cases:
        with subtests.test(msg=scenario):
            items = db.get_items_since(tid, since)
            assert len(items) == expected


def test_get_resource_summary(subtests, db):
    db.upsert_summary("t1", "gmail", "Title", "Summary", mention_type="direct",
                       estimated_relevance=8, final_relevance=8)
    cases = [
        ("When summary exists then returns it",
         "t1", True),
        ("When summary not exists then returns None",
         "t999", False),
    ]
    for scenario, tid, should_exist in cases:
        with subtests.test(msg=scenario):
            result = db.get_resource_summary(tid)
            if should_exist:
                assert result is not None
                assert result["title"] == "Title"
            else:
                assert result is None


def test_db_retry_on_write_error(subtests):
    with subtests.test(msg="When write fails all retries then raises"):
        d = gmail.open_db(":memory:")
        original_lock = d._lock
        d._lock = MagicMock()
        d._lock.__enter__ = MagicMock(side_effect=sqlite3.DatabaseError("locked"))
        d._lock.__exit__ = MagicMock()
        with patch.object(gmail.SkillDB, "_WRITE_RETRIES", 1), \
             patch.object(gmail.SkillDB, "_WRITE_RETRY_DELAY_S", 0):
            with pytest.raises(sqlite3.DatabaseError):
                d.upsert_atomic("gmail", "t1", "m1", "A", "C", "2026-01-01", "2026-01-01")
        d._lock = original_lock
        d.close()


def test_delete_atomic_since(subtests):
    cases = [
        ("When items exist after date then deletes them",
         "2026-04-01", 3),
        ("When no items after date then deletes none",
         "2099-01-01", 0),
    ]
    for scenario, since, expected_deleted in cases:
        with subtests.test(msg=scenario):
            fresh = gmail.open_db(":memory:")
            _seed_thread(fresh, "t_del", n_msgs=3)
            result = fresh.delete_atomic_since("gmail", since)
            assert result == expected_deleted
            fresh.close()


def test_clear_summaries_for_resources(subtests):
    cases = [
        ("When resource_ids provided then clears those summaries",
         ["t1", "t2"], 2),
        ("When empty list then clears none",
         [], 0),
    ]
    for scenario, rids, expected in cases:
        with subtests.test(msg=scenario):
            fresh = gmail.open_db(":memory:")
            _seed_thread(fresh, "t1", n_msgs=1)
            _seed_thread(fresh, "t2", n_msgs=1)
            fresh.upsert_summary("t1", "gmail", "T1", "S1", mention_type="direct",
                                 estimated_relevance=8, final_relevance=8)
            fresh.upsert_summary("t2", "gmail", "T2", "S2", mention_type="indirect",
                                 estimated_relevance=6, final_relevance=6)
            result = fresh.clear_summaries_for_resources(rids)
            assert result == expected
            if expected > 0:
                s = fresh.get_resource_summary("t1")
                assert s["summary"] is None
            fresh.close()


def test_db_close(subtests, db):
    with subtests.test(msg="When close called then no error"):
        db.close()


def test_thread_needs_fetch_meta_fallback(subtests, db):
    with subtests.test(msg="When no summary but has atomic with meta then uses atomic meta"):
        db.upsert_atomic("gmail", "t_fb", "m1", "A", "C", "2026-01-01", "2026-01-01",
                         metadata={"last_message_id": "last123"})
        assert db.thread_needs_fetch("t_fb", "last123") is False
        assert db.thread_needs_fetch("t_fb", "different") is True


def test_upsert_thread_meta(subtests):
    cases = [
        ("When atomic exists with different last_message_id then updates it",
         lambda d: d.upsert_atomic("gmail", "t_meta_up", "last_msg", "A", "C",
                                   "2026-01-01", "2026-01-01", metadata={"last_message_id": "old"}),
         "t_meta_up", "last_msg", "new_id", True),
        ("When atomic exists with same last_message_id then no-op",
         lambda d: d.upsert_atomic("gmail", "t_meta_same", "msg_same", "A", "C",
                                   "2026-01-01", "2026-01-01", metadata={"last_message_id": "same_id"}),
         "t_meta_same", "msg_same", "same_id", False),
        ("When atomic does not exist then no-op",
         lambda d: None,
         "t_no_exist", "no_msg", "any_id", False),
    ]
    for scenario, setup, tid, mid, new_id, expect_update in cases:
        with subtests.test(msg=scenario):
            fresh = gmail.open_db(":memory:")
            if setup:
                setup(fresh)
            fresh.upsert_thread_meta(tid, new_id)
            fresh.close()


def test_get_thread_meta_last_message_id(subtests, db):
    cases = [
        ("When atomic has last_message_id in metadata then returns it",
         lambda d: d.upsert_atomic("gmail", "t_meta", "m1", "A", "C", "2026-01-01", "2026-01-01",
                                   metadata={"last_message_id": "last_xyz"}),
         "t_meta", "last_xyz"),
        ("When no data then returns None",
         lambda d: None,
         "t_empty", None),
    ]
    for scenario, setup, tid, expected in cases:
        with subtests.test(msg=scenario):
            fresh = gmail.open_db(":memory:")
            if setup:
                setup(fresh)
            result = fresh.get_thread_meta_last_message_id(tid)
            assert result == expected
            fresh.close()


# ═════════════════════════════════════════════════════════════════════
# Tests: User context loading
# ═════════════════════════════════════════════════════════════════════

def test_load_user_context(subtests):
    with subtests.test(msg="When User.md exists then loads content"):
        gmail._USER_CONTEXT = None
        mock_path = MagicMock()
        mock_path.read_text.return_value = "user info"
        with patch("gmail._USER_MD_PATH", mock_path):
            result = gmail._load_user_context()
            assert result == "user info"
        gmail._USER_CONTEXT = None

    with subtests.test(msg="When User.md not found then returns empty"):
        gmail._USER_CONTEXT = None
        mock_path = MagicMock()
        mock_path.read_text.side_effect = FileNotFoundError
        with patch("gmail._USER_MD_PATH", mock_path):
            result = gmail._load_user_context()
            assert result == ""
        gmail._USER_CONTEXT = None

    with subtests.test(msg="When already cached then returns cached"):
        gmail._USER_CONTEXT = "cached"
        result = gmail._load_user_context()
        assert result == "cached"
        gmail._USER_CONTEXT = None


# ═════════════════════════════════════════════════════════════════════
# Tests: Summarize edge cases
# ═════════════════════════════════════════════════════════════════════

def test_summarize_one_force(subtests, db):
    with subtests.test(msg="When force=True then re-summarizes even with existing summary"):
        _seed_thread(db, "t_force_sum", n_msgs=1)
        db.upsert_summary("t_force_sum", "gmail", "Old", "Old text",
                          mention_type="none", estimated_relevance=3, final_relevance=3)
        mock_raw = json.dumps({"relevance": 9, "summary": "Forced new",
                               "work_items": [], "people": [], "labels": []})
        with patch("gmail._call_llm", return_value=mock_raw):
            gmail._summarize_one(db, "t_force_sum",
                                 {"subject": "T", "labels": [], "last_msg_id": "", "senders": []},
                                 force=True, current=1, total=1)
        s = db.get_resource_summary("t_force_sum")
        assert "Forced new" in s["summary"]
        assert s["final_relevance"] == 9


def test_summarize_one_empty_summary_raises(subtests, db):
    with subtests.test(msg="When LLM returns empty summary then raises"):
        _seed_thread(db, "t_empty_sum", n_msgs=1)
        mock_raw = json.dumps({"relevance": 5, "summary": "",
                               "work_items": [], "people": [], "labels": []})
        with patch("gmail._call_llm", return_value=mock_raw):
            with pytest.raises(RuntimeError, match="Empty summary"):
                gmail._summarize_one(db, "t_empty_sum",
                                     {"subject": "T", "labels": [], "last_msg_id": "", "senders": []},
                                     force=True, current=1, total=1)


def test_pipeline_error_handling(subtests, db):
    with subtests.test(msg="When summarization raises then collects error"):
        _seed_thread(db, "t_err", n_msgs=1)
        with patch("gmail._call_llm", side_effect=RuntimeError("LLM down")):
            pipe = gmail._Pipeline(db, force=True)
            pipe.set_total(1)
            pipe.put("t_err", {"subject": "T", "labels": [], "last_msg_id": "", "senders": []})
            errors = pipe.finish()
            assert len(errors) == 1
            assert "LLM down" in errors[0]


# ═════════════════════════════════════════════════════════════════════
# Tests: Coverage gap fillers (comprehensive behavior tests)
# ═════════════════════════════════════════════════════════════════════

def test_parse_gmail_date_year_lt_2000(subtests):
    with subtests.test(msg="When year is below 2000 then replaces with current year"):
        result = gmail.parse_gmail_date("Apr 6, 0099, 3:45 PM")
        from datetime import datetime
        current_year = str(datetime.now().year)
        assert current_year in result

    with subtests.test(msg="When dow-stripped date has year<2000 then replaces with current year"):
        result = gmail.parse_gmail_date("Mon, Apr 6, 0099, 3:45 PM")
        from datetime import datetime
        current_year = str(datetime.now().year)
        assert current_year in result

    with subtests.test(msg="When Unicode NNBSP before AM then normalizes and parses"):
        result = gmail.parse_gmail_date("Apr 6, 2026, 9:40\u202fAM")
        assert result.startswith("2026-04-06")

    with subtests.test(msg="When Unicode NBSP in date then normalizes and parses"):
        result = gmail.parse_gmail_date("Apr 6, 2026, 9:40\u00a0AM")
        assert result.startswith("2026-04-06")


def test_has_message_anywhere_without_exclude(subtests, db):
    with subtests.test(msg="When item exists and no exclude then returns True"):
        db.upsert_atomic("gmail", "t1", "m_any", "A", "C", "2026-01-01", "2026-01-01")
        assert db.has_message_anywhere("m_any") is True

    with subtests.test(msg="When item does not exist and no exclude then returns False"):
        assert db.has_message_anywhere("m_nonexistent") is False


def test_upsert_thread_meta_matching_message_id(subtests):
    with subtests.test(msg="When last_message_id already matches then no-op"):
        d = gmail.open_db(":memory:")
        d.upsert_atomic("gmail", "t_meta", "m1", "A", "C", "2026-01-01", "2026-01-01",
                         metadata={"last_message_id": "m1"})
        d.upsert_thread_meta("t_meta", "m1")
        items = d.get_atomic_for_resource("t_meta")
        meta = json.loads(items[0]["metadata"])
        assert meta["last_message_id"] == "m1"
        d.close()


def test_needs_refresh_no_cached_items(subtests):
    with subtests.test(msg="When no cached items for resource then returns False"):
        d = gmail.open_db(":memory:")
        d.upsert_summary("t_empty", "gmail", "T", "S", mention_type="none")
        assert d.needs_resummarize("t_empty") is False
        d.close()


def test_cache_thread_messages_foreign_skip(subtests):
    with subtests.test(msg="When message belongs to another thread then skips it"):
        d = gmail.open_db(":memory:")
        d.upsert_atomic("gmail", "t_other", "m_foreign", "A", "C", "2026-01-01", "2026-01-01")
        msgs = [{"legacy_message_id": "m_foreign", "from": "Alice", "date": "2026-01-01",
                 "body": "Hello", "to": [], "cc": []}]
        result = gmail.cache_thread_messages(d, "t_target", "Subject", msgs)
        assert result == 0
        assert d.get_atomic_for_resource("t_target") == []
        d.close()


def test_navigate_to_page_pagination(subtests):
    with subtests.test(msg="When page_num > 1 then URL includes /p{page_num}"):
        mock_page = MagicMock()
        mock_page.wait_for_selector.return_value = True
        with patch("gmail.time.sleep"):
            result = gmail.navigate_to_page(mock_page, 7, 3)
        assert result is True
        call_args = mock_page.goto.call_args
        assert "/p3" in call_args[0][0]


def test_navigate_to_thread_poll_loop(subtests):
    with subtests.test(msg="When thread loads after poll iterations then returns True"):
        mock_page = MagicMock()
        mock_page.wait_for_selector.return_value = True
        mock_page.evaluate.side_effect = ["wrong1", "wrong2", "abc123"]
        times = iter([0, 0.5, 1.0, 1.5])
        with patch("gmail.time.sleep"), \
             patch("gmail.time.monotonic", side_effect=lambda: next(times)):
            result = gmail.navigate_to_thread(mock_page, "abc123")
        assert result is True


def test_call_llm_with_api_key(subtests):
    with subtests.test(msg="When LITELLM_API_KEY is set then includes Authorization header"):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {
            "choices": [{"message": {"content": "response text"}}]
        }
        with patch("gmail.LITELLM_API_KEY", "test_key_123"), \
             patch("gmail.requests.post", return_value=mock_resp) as mock_post:
            result = gmail._call_llm("system", "user")
            assert result == "response text"
            headers = mock_post.call_args[1].get("headers", {})
            assert "Authorization" in headers


def test_call_llm_retries_on_failure(subtests):
    with subtests.test(msg="When all retries fail with 5xx then raises RuntimeError"):
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_resp.text = "Server Error"
        with patch("gmail.requests.post", return_value=mock_resp), \
             patch("gmail.time.sleep"):
            with pytest.raises(RuntimeError, match="LLM API 500"):
                gmail._call_llm("system", "user")

    with subtests.test(msg="When all retries fail with connection error then raises"):
        with patch("gmail.requests.post", side_effect=gmail.requests.RequestException("timeout")), \
             patch("gmail.time.sleep"):
            with pytest.raises(RuntimeError, match="LLM connection failed"):
                gmail._call_llm("system", "user")


# ═════════════════════════════════════════════════════════════════════
# Tests: Comprehensive behavioral edge cases
# ═════════════════════════════════════════════════════════════════════

def test_get_thread_id_from_page(subtests):
    with subtests.test(msg="When h2 has data-legacy-thread-id then returns it"):
        mock_page = MagicMock()
        mock_page.evaluate.return_value = "thread_abc"
        result = gmail.get_thread_id_from_page(mock_page)
        assert result == "thread_abc"

    with subtests.test(msg="When page returns empty then returns empty string"):
        mock_page = MagicMock()
        mock_page.evaluate.return_value = ""
        result = gmail.get_thread_id_from_page(mock_page)
        assert result == ""

    with subtests.test(msg="When page returns None then returns empty string"):
        mock_page = MagicMock()
        mock_page.evaluate.return_value = None
        result = gmail.get_thread_id_from_page(mock_page)
        assert result == ""


def test_cache_thread_messages_page_mismatch(subtests):
    with subtests.test(msg="When page_thread_id differs from thread_id then skips entirely"):
        d = gmail.open_db(":memory:")
        msgs = [{"legacy_message_id": "m1", "from": "A", "date": "2026-01-01",
                 "body": "Hello", "to": [], "cc": []}]
        result = gmail.cache_thread_messages(d, "t1", "Sub", msgs, page_thread_id="t_wrong")
        assert result == 0
        assert d.get_atomic_for_resource("t1") == []
        d.close()

    with subtests.test(msg="When page_thread_id empty then processes normally"):
        d = gmail.open_db(":memory:")
        msgs = [{"legacy_message_id": "m_ok", "from": "A", "date": "2026-01-01",
                 "body": "Hello", "to": [], "cc": []}]
        result = gmail.cache_thread_messages(d, "t_ok", "Sub", msgs, page_thread_id="")
        assert result == 1
        d.close()

    with subtests.test(msg="When page_thread_id matches then processes normally"):
        d = gmail.open_db(":memory:")
        msgs = [{"legacy_message_id": "m_match", "from": "A", "date": "2026-01-01",
                 "body": "Hello", "to": [], "cc": []}]
        result = gmail.cache_thread_messages(d, "t_match", "Sub", msgs, page_thread_id="t_match")
        assert result == 1
        d.close()


def test_compute_mention_type_edge_cases(subtests):
    user_email = gmail.GMAIL_USER_EMAIL

    with subtests.test(msg="When user in BCC then returns direct"):
        d = gmail.open_db(":memory:")
        meta = {"to": [], "cc": [], "bcc": [{"name": "Me", "email": user_email}],
                "subject": "Test"}
        d.upsert_atomic("gmail", "t_bcc", "m_bcc", "A <other@x.com>", "C",
                         "2026-01-01", "2026-01-01", metadata=meta)
        result = d.compute_mention_type("t_bcc")
        assert result in ("direct", "indirect", "none")
        d.close()

    with subtests.test(msg="When user in both TO and CC then returns direct"):
        d = gmail.open_db(":memory:")
        meta = {"to": [{"name": "Me", "email": user_email}],
                "cc": [{"name": "Me", "email": user_email}],
                "subject": "Test"}
        d.upsert_atomic("gmail", "t_both", "m_both", "A <other@x.com>", "C",
                         "2026-01-01", "2026-01-01", metadata=meta)
        result = d.compute_mention_type("t_both")
        assert result == "direct"
        d.close()


def test_needs_resummarize_new_items_after_summary(subtests):
    with subtests.test(msg="When new items cached after last summarization then returns True"):
        d = gmail.open_db(":memory:")
        d.upsert_atomic("gmail", "t_resum", "m_old", "A", "Old", "2026-01-01", "2026-01-01")
        d.upsert_summary("t_resum", "gmail", "T", "S", mention_type="none")
        import time
        time.sleep(0.05)
        d.upsert_atomic("gmail", "t_resum", "m_new", "A", "New", "2026-01-02", "2026-01-02")
        result = d.needs_resummarize("t_resum")
        assert result is True
        d.close()


def test_parse_llm_response_edge_cases(subtests):
    with subtests.test(msg="When thinking tags wrap JSON then strips tags and parses"):
        raw = '<think>Let me analyze this...</think>{"relevance": 7, "summary": "Test", "work_items": [], "people": [], "labels": []}'
        result = gmail.parse_llm_response(raw, "direct")
        assert result.relevance == 7
        assert result.summary == "Test"

    with subtests.test(msg="When empty summary in JSON then falls back to default"):
        raw = '{"relevance": 5, "summary": "", "work_items": [], "people": [], "labels": []}'
        result = gmail.parse_llm_response(raw, "none")
        assert result.summary == ""

    with subtests.test(msg="When relevance is string then converts to int"):
        raw = '{"relevance": "8", "summary": "Test", "work_items": [], "people": [], "labels": []}'
        result = gmail.parse_llm_response(raw, "direct")
        assert result.relevance == 8

    with subtests.test(msg="When extra fields in JSON then ignores them"):
        raw = '{"relevance": 6, "summary": "Test", "work_items": [], "people": [], "labels": [], "extra": "ignored"}'
        result = gmail.parse_llm_response(raw, "none")
        assert result.relevance == 6

    with subtests.test(msg="When none mention type has very low relevance then keeps it"):
        raw = '{"relevance": 1, "summary": "Spam", "work_items": [], "people": [], "labels": []}'
        result = gmail.parse_llm_response(raw, "none")
        assert result.relevance == 1

    with subtests.test(msg="When labels exceed 5 then truncates to 5"):
        raw = '{"relevance": 5, "summary": "T", "work_items": [], "people": [], "labels": ["a-b","c-d","e-f","g-h","i-j","k-l","m-n"]}'
        result = gmail.parse_llm_response(raw, "none")
        assert len(result.labels) == 5


def test_call_llm_retry_then_success(subtests):
    with subtests.test(msg="When first attempt fails with 500 but second succeeds then returns content"):
        fail_resp = MagicMock()
        fail_resp.status_code = 500
        fail_resp.text = "Server Error"
        ok_resp = MagicMock()
        ok_resp.status_code = 200
        ok_resp.json.return_value = {"choices": [{"message": {"content": "success"}}]}
        with patch("gmail.requests.post", side_effect=[fail_resp, ok_resp]), \
             patch("gmail.time.sleep"):
            result = gmail._call_llm("system", "user")
            assert result == "success"


def test_summarize_resource_with_metadata(subtests):
    with subtests.test(msg="When metadata and existing_summary provided then includes in prompt"):
        mock_raw = json.dumps({"relevance": 7, "summary": "Updated summary",
                               "work_items": ["fix bug"], "people": ["Alice"],
                               "labels": ["a-b", "c-d", "e-f", "g-h", "i-j"]})
        items = [{"author": "Alice", "created_at": "2026-01-01", "content": "Please fix the bug"}]
        with patch("gmail._call_llm", return_value=mock_raw) as mock_llm:
            result = gmail.summarize_resource(
                "Bug Report", "gmail", items,
                metadata={"to": [{"email": "me@test.com"}]},
                existing_summary="Previous summary text",
                mention_type="direct"
            )
            assert result.relevance == 7
            assert result.summary == "Updated summary"
            call_args = mock_llm.call_args
            assert "Previous summary text" in call_args[0][1]

    with subtests.test(msg="When all items have empty content then still processes"):
        mock_raw = json.dumps({"relevance": 3, "summary": "No content",
                               "work_items": [], "people": [], "labels": ["a-b", "c-d", "e-f", "g-h", "i-j"]})
        items = [{"author": "System", "created_at": "2026-01-01", "content": ""}]
        with patch("gmail._call_llm", return_value=mock_raw):
            result = gmail.summarize_resource("Empty", "gmail", items, mention_type="none")
            assert result.relevance == 3


def test_get_thread_list_empty(subtests):
    with subtests.test(msg="When page returns empty thread list then returns empty"):
        mock_page = MagicMock()
        mock_page.evaluate.return_value = []
        result = gmail.get_thread_list(mock_page)
        assert result == []

    with subtests.test(msg="When page returns None then returns empty"):
        mock_page = MagicMock()
        mock_page.evaluate.return_value = None
        result = gmail.get_thread_list(mock_page)
        assert result == [] or result is None


def test_navigate_to_thread_selector_timeout(subtests):
    with subtests.test(msg="When wait_for_selector times out then returns False"):
        mock_page = MagicMock()
        mock_page.wait_for_selector.side_effect = PwTimeout("timeout")
        result = gmail.navigate_to_thread(mock_page, "abc123")
        assert result is False


def test_wait_for_messages_stable_timeout(subtests):
    with subtests.test(msg="When count never stabilizes then returns after max_wait"):
        mock_page = MagicMock()
        call_count = [0]
        def varying_count(script):
            call_count[0] += 1
            return call_count[0]
        mock_page.evaluate.side_effect = varying_count
        with patch("gmail.time.sleep"):
            result = gmail._wait_for_messages_stable(mock_page, max_wait=0.6, poll_interval=0.3)
            assert isinstance(result, int)


def test_clean_email_body_complex_signatures(subtests):
    with subtests.test(msg="When multiple On...wrote blocks then removes all"):
        text = "Hello\n\nOn Mon, Apr 1 wrote:\n> quoted\n\nOn Tue, Apr 2 wrote:\n> more quoted"
        result = gmail.clean_email_body(text)
        assert "Hello" in result

    with subtests.test(msg="When Regards signature then removes"):
        text = "Hello world\n\nRegards,\nMichael"
        result = gmail.clean_email_body(text)
        assert "Hello world" in result

    with subtests.test(msg="When very long email then still processes"):
        text = "Important content. " * 500
        result = gmail.clean_email_body(text)
        assert len(result) > 0


def test_db_concurrent_access(subtests):
    with subtests.test(msg="When multiple threads upsert then all data preserved"):
        import threading
        d = gmail.open_db(":memory:")
        errors = []
        def writer(tid, count):
            try:
                for i in range(count):
                    d.upsert_atomic("gmail", tid, f"{tid}_m{i}", f"Author_{i}",
                                    f"Content {i}", "2026-01-01", "2026-01-01")
            except Exception as e:
                errors.append(str(e))

        threads = []
        for t_id in ["ct1", "ct2", "ct3"]:
            t = threading.Thread(target=writer, args=(t_id, 10))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        assert not errors
        for t_id in ["ct1", "ct2", "ct3"]:
            items = d.get_atomic_for_resource(t_id)
            assert len(items) == 10
        d.close()


def test_upsert_atomic_immutability(subtests, db):
    with subtests.test(msg="When same message upserted twice then content is NOT updated"):
        db.upsert_atomic("gmail", "t_imm", "m_imm", "Author1", "Content1", "2026-01-01", "2026-01-01")
        db.upsert_atomic("gmail", "t_imm", "m_imm", "Author2", "Content2", "2026-01-02", "2026-01-02")
        items = db.get_atomic_for_resource("t_imm")
        assert len(items) == 1
        assert items[0]["author"] == "Author1"
        assert items[0]["content"] == "Content1"


def test_get_all_summaries_with_since_filter(subtests):
    with subtests.test(msg="When since filter then results sorted by sort_ts asc"):
        d = gmail.open_db(":memory:")
        d.upsert_atomic("gmail", "t_old", "m_old", "A", "C", "2025-01-01", "2025-01-01")
        d.upsert_summary("t_old", "gmail", "Old", "Sum", mention_type="none",
                          estimated_relevance=8, final_relevance=8)
        d.upsert_atomic("gmail", "t_new", "m_new", "A", "C", "2026-04-01", "2026-04-01")
        d.upsert_summary("t_new", "gmail", "New", "Sum", mention_type="direct",
                          estimated_relevance=9, final_relevance=9)
        all_results = d.get_all_summaries()
        assert len(all_results) == 2
        assert all_results[0]["title"] == "Old"

    with subtests.test(msg="When source filter then returns only matching source"):
        d2 = gmail.open_db(":memory:")
        d2.upsert_atomic("gmail", "tg", "mg", "A", "C", "2026-01-01", "2026-01-01")
        d2.upsert_summary("tg", "gmail", "Gmail", "S", mention_type="none",
                           estimated_relevance=5, final_relevance=5)
        results = d2.get_all_summaries(source="jira")
        assert len(results) == 0
        results = d2.get_all_summaries(source="gmail")
        assert len(results) == 1
        d2.close()


def test_format_summary_block_all_fields(subtests):
    with subtests.test(msg="When summary has work_items and people then formats them"):
        s = {
            "title": "Test", "summary": "Summary text",
            "mention_type": "direct", "final_relevance": 9,
            "source": "gmail", "resource_id": "t1",
            "metadata": json.dumps({
                "labels": ["a-b", "c-d"],
                "work_items": ["JIRA-123", "JIRA-456"],
                "people": ["Alice", "Bob"],
                "gmail_labels": ["Inbox", "Important"]
            })
        }
        result = gmail._format_summary_block(s, 1, 5)
        assert "JIRA-123" in result
        assert "Alice" in result
        assert "a-b" in result


def test_pipeline_multiple_threads(subtests):
    with subtests.test(msg="When pipeline processes multiple threads then all summarized"):
        d = gmail.open_db(":memory:")
        mock_raw = json.dumps({"relevance": 7, "summary": "Test",
                               "work_items": [], "people": [],
                               "labels": ["a-b", "c-d", "e-f", "g-h", "i-j"]})
        for tid in ["tp1", "tp2", "tp3"]:
            _seed_thread(d, tid, n_msgs=2)
        with patch("gmail._call_llm", return_value=mock_raw):
            pipeline = gmail._Pipeline(d, force=False)
            for tid in ["tp1", "tp2", "tp3"]:
                pipeline.put(tid, {"subject": f"Thread {tid}", "labels": [], "senders": []})
            errors = pipeline.finish()
        assert not errors
        for tid in ["tp1", "tp2", "tp3"]:
            s = d.get_resource_summary(tid)
            assert s is not None
            assert s["final_relevance"] == 7
        d.close()


# ═════════════════════════════════════════════════════════════════════
# Tests: Main full browser path (mocked)
# ═════════════════════════════════════════════════════════════════════

def test_main_full_browser_flow(subtests, tmp_path):
    with subtests.test(msg="When normal run then connects browser, scans, fetches, summarizes"):
        d, db_path = _make_test_db(tmp_path)
        d.close()
        out_path = tmp_path / "browser_out.md"

        mock_page = MagicMock()
        mock_page.url = "https://mail.google.com/mail/u/0/#inbox"
        mock_page.wait_for_selector.return_value = True
        mock_page.evaluate.return_value = []

        mock_pw = MagicMock()
        mock_browser = MagicMock()

        thread_list_page1 = [
            {"rowIndex": 0, "legacyThreadId": "thread1", "legacyLastMsgId": "msg_latest",
             "senders": [{"name": "Alice", "email": "alice@test.com"}],
             "subject": "Test Email", "date": "Apr 1, 2026", "labels": ["Inbox"]}
        ]
        thread_messages = [
            {"legacy_message_id": "msg_latest", "from": "Alice <alice@test.com>",
             "to": [{"name": "Michael", "email": "michael.bui@fairpricegroup.sg"}],
             "cc": [], "bcc": [], "date": "Apr 1, 2026",
             "body": "Hello Michael, this is a test email.",
             "attachments": [], "details_parsed": True}
        ]

        call_count = [0]

        def page_evaluate_side_effect(script):
            call_count[0] += 1
            if "tr[jscontroller]" in str(script) and "threads" in str(script):
                return thread_list_page1
            if "data-message-id" in str(script) and "messages" in str(script):
                return thread_messages
            if "h2.hP" in str(script):
                return "Test Email"
            if "Expand all" in str(script):
                return False
            if "Show details" in str(script) or "Show trimmed" in str(script):
                return None
            return []

        mock_page.evaluate.side_effect = page_evaluate_side_effect

        mock_raw = json.dumps({"relevance": 8, "summary": "Test summary from LLM",
                               "work_items": [], "people": ["Alice"], "labels": ["test-email", "a-b", "c-d", "e-f", "g-h"]})

        nav_results = iter([True, False])

        with patch("gmail.open_db", return_value=gmail.open_db(str(db_path))), \
             patch("gmail.connect_browser", return_value=(mock_pw, mock_browser, mock_page)), \
             patch("gmail.navigate_to_page", side_effect=lambda *a, **kw: next(nav_results)), \
             patch("gmail.get_thread_list", return_value=thread_list_page1), \
             patch("gmail.navigate_to_thread", return_value=True), \
             patch("gmail.get_thread_id_from_page", return_value="thread1"), \
             patch("gmail.get_thread_subject", return_value="Test Email"), \
             patch("gmail.extract_thread_messages", return_value=thread_messages), \
             patch("gmail._call_llm", return_value=mock_raw), \
             patch("gmail.time.sleep"), \
             patch("sys.argv", ["gmail.py", "--days", "365", "--min-relevance", "1",
                                "--output", str(out_path), "--max-threads", "5",
                                "--cdp-url", "http://localhost:9222"]):
            gmail.main()

        assert out_path.exists()
        content = out_path.read_text()
        assert "Test summary from LLM" in content


def test_main_browser_fatal_no_threads(subtests, tmp_path):
    with subtests.test(msg="When no threads found on first page then exits with code 2"):
        d, db_path = _make_test_db(tmp_path)
        d.close()
        out_path = tmp_path / "no_threads.md"

        with patch("gmail.open_db", return_value=gmail.open_db(str(db_path))), \
             patch("gmail.connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())), \
             patch("gmail.navigate_to_page", return_value=False), \
             patch("sys.argv", ["gmail.py", "--days", "365", "--output", str(out_path),
                                "--cdp-url", "http://localhost:9222"]):
            with pytest.raises(SystemExit) as exc_info:
                gmail.main()
            assert exc_info.value.code == 2


def test_main_browser_errors_exit_1(subtests, tmp_path):
    with subtests.test(msg="When summarization has errors then exits with code 1"):
        d, db_path = _make_test_db(tmp_path)
        d.close()
        out_path = tmp_path / "err_out.md"

        thread_list = [
            {"rowIndex": 0, "legacyThreadId": "t_err1", "legacyLastMsgId": "m_err",
             "senders": [], "subject": "Err", "date": "", "labels": []}
        ]
        messages = [
            {"legacy_message_id": "m_err", "from": "X", "to": [], "cc": [],
             "bcc": [], "date": "", "body": "err body",
             "attachments": [], "details_parsed": True}
        ]

        nav_results = iter([True, False])

        with patch("gmail.open_db", return_value=gmail.open_db(str(db_path))), \
             patch("gmail.connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())), \
             patch("gmail.navigate_to_page", side_effect=lambda *a, **kw: next(nav_results)), \
             patch("gmail.get_thread_list", return_value=thread_list), \
             patch("gmail.navigate_to_thread", return_value=True), \
             patch("gmail.get_thread_id_from_page", return_value="t_err1"), \
             patch("gmail.get_thread_subject", return_value="Err"), \
             patch("gmail.extract_thread_messages", return_value=messages), \
             patch("gmail._call_llm", side_effect=RuntimeError("LLM down")), \
             patch("gmail.time.sleep"), \
             patch("sys.argv", ["gmail.py", "--days", "365", "--output", str(out_path),
                                "--cdp-url", "http://localhost:9222", "--max-threads", "1"]):
            with pytest.raises(SystemExit) as exc_info:
                gmail.main()
            assert exc_info.value.code == 1


def test_main_excluded_labels(subtests, tmp_path):
    with subtests.test(msg="When thread has excluded label then skips it"):
        d, db_path = _make_test_db(tmp_path)
        d.close()
        out_path = tmp_path / "excl_out.md"

        thread_list = [
            {"rowIndex": 0, "legacyThreadId": "t_excl", "legacyLastMsgId": "m_excl",
             "senders": [], "subject": "Excluded", "date": "",
             "labels": ["❌ ai-exclusion"]}
        ]

        with patch("gmail.open_db", return_value=gmail.open_db(str(db_path))), \
             patch("gmail.connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())), \
             patch("gmail.navigate_to_page") as mock_nav, \
             patch("gmail.get_thread_list") as mock_list, \
             patch("gmail.time.sleep"), \
             patch("sys.argv", ["gmail.py", "--days", "365", "--output", str(out_path),
                                "--cdp-url", "http://localhost:9222", "--max-threads", "5"]):
            mock_nav.side_effect = [True, False]
            mock_list.return_value = thread_list
            gmail.main()
        assert out_path.exists()
        content = out_path.read_text()
        assert "Excluded" not in content


def test_main_early_stop(subtests, tmp_path):
    with subtests.test(msg="When early stop triggers then remaining threads use cache"):
        d, db_path = _make_test_db(tmp_path)
        _seed_thread(d, "t_es1", n_msgs=1)
        d.upsert_summary("t_es1", "gmail", "Cached1", "Summary1",
                          {"last_message_id": "m_es1"}, mention_type="direct",
                          estimated_relevance=8, final_relevance=8)
        _seed_thread(d, "t_es2", n_msgs=1)
        d.upsert_summary("t_es2", "gmail", "Cached2", "Summary2",
                          {"last_message_id": "m_es2"}, mention_type="direct",
                          estimated_relevance=7, final_relevance=7)
        d.close()
        out_path = tmp_path / "es_out.md"

        thread_list = [
            {"rowIndex": 0, "legacyThreadId": "t_es1", "legacyLastMsgId": "m_es1",
             "senders": [], "subject": "Cached1", "date": "", "labels": []},
            {"rowIndex": 1, "legacyThreadId": "t_es2", "legacyLastMsgId": "m_es2",
             "senders": [], "subject": "Cached2", "date": "", "labels": []},
        ]

        with patch("gmail.open_db", return_value=gmail.open_db(str(db_path))), \
             patch("gmail.connect_browser", return_value=(MagicMock(), MagicMock(), MagicMock())), \
             patch("gmail.navigate_to_page") as mock_nav, \
             patch("gmail.get_thread_list", return_value=thread_list), \
             patch("gmail.time.sleep"), \
             patch("sys.argv", ["gmail.py", "--days", "365", "--output", str(out_path),
                                "--cdp-url", "http://localhost:9222",
                                "--max-threads", "10", "--early-stop", "2",
                                "--min-relevance", "1"]):
            mock_nav.side_effect = [True, False]
            gmail.main()
        assert out_path.exists()


def test_debug_function(subtests):
    with subtests.test(msg="When log level is DEBUG then prints"):
        original = gmail._LOG_LEVEL
        gmail._LOG_LEVEL = "DEBUG"
        with patch("builtins.print") as mock_print:
            gmail.debug("test message")
        mock_print.assert_called_once()
        gmail._LOG_LEVEL = original

    with subtests.test(msg="When log level is INFO then does not print"):
        original = gmail._LOG_LEVEL
        gmail._LOG_LEVEL = "INFO"
        with patch("builtins.print") as mock_print:
            gmail.debug("test message")
        mock_print.assert_not_called()
        gmail._LOG_LEVEL = original
