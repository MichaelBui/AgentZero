#!/usr/bin/env python3
"""
Gmail Skill - Fetch email threads via Chrome CDP, cache, and AI-summarize.

Single-file skill that:
1. Connects to remote Chrome via CDP, navigates Gmail search
2. Extracts threads via DOM scraping, caches messages in SQLite
3. Summarizes via LLM with relevance scoring, entity extraction, JSON output
4. Writes final output .md only after all summaries succeed

Usage:
  python gmail.py                          # defaults: 3-5 day lookback
  python gmail.py --days 7
  python gmail.py --cached-only            # output from DB, no browser
  python gmail.py --force                  # re-summarize (keeps cached content)
"""

import argparse
import json
import os
import queue as _queue
import re
import sqlite3
import sys
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional
from zoneinfo import ZoneInfo

import requests
from playwright.sync_api import sync_playwright, TimeoutError as PwTimeout

# ═════════════════════════════════════════════════════════════════════
# Configuration
# ═════════════════════════════════════════════════════════════════════

DEFAULT_CDP = os.environ.get("CDP_URL", "http://192.168.1.11:9223")
GMAIL_BASE = "https://mail.google.com"
GMAIL_USER_EMAIL = os.environ.get("GMAIL_USER_EMAIL", "michael.bui@fairpricegroup.sg")

DEFAULT_EXCLUDE = '["❌ ai-exclusion", "🪣 Bitbucket"]'

LITELLM_BASE = os.environ.get("LITELLM_BASE_URL", "https://llm.gigary.com/v1")
SUMMARIZE_MODEL = os.environ.get("SUMMARIZE_MODEL", "local/qwen3.5-35b-a3b:instruct-reasoning")
LITELLM_API_KEY = os.environ.get("API_KEY_OTHER", os.environ.get("LLAMA_TOKEN", ""))
SUMMARIZE_RETRIES = int(os.environ.get("SUMMARIZE_RETRIES", "3"))
SUMMARIZE_RETRY_INITIAL_SEC = float(os.environ.get("SUMMARIZE_RETRY_INITIAL_SEC", "30"))

_WORKDIR = Path(__file__).resolve().parents[3] / "workdir"
_DEFAULT_DB_PATH = Path(__file__).resolve().parent.parent / "data" / "gmail_cache.db"
DB_PATH = Path(os.environ.get("GMAIL_DB_PATH", str(_DEFAULT_DB_PATH)))
_USER_MD_PATH = Path(__file__).resolve().parents[3] / "User.md"

_TZ = ZoneInfo(os.environ.get("TZ", "Asia/Singapore"))

_RELEVANCE_FLOORS = {"direct": 7, "indirect": 5, "none": 1}
_WORD_HINTS = {"direct": 200, "indirect": 100, "none": 30}

_DB_OPEN_RETRIES = 3
_DB_RETRY_DELAY_S = 2


def _default_lookback_days() -> int:
    """3 weekdays coverage: 3 (Tue-Sat), 4 (Sun), 5 (Mon)."""
    weekday = datetime.now(_TZ).weekday()
    if weekday == 0:
        return 5
    if weekday == 6:
        return 4
    return 3


def _now_iso() -> str:
    return datetime.now(_TZ).isoformat()


def _ts() -> str:
    return datetime.now(_TZ).strftime("%Y-%m-%dT%H:%M:%S%z")


def log(*a, **kw):
    print(f"[{_ts()}]", *a, flush=True, **kw)


# ═════════════════════════════════════════════════════════════════════
# Text Cleaner
# ═════════════════════════════════════════════════════════════════════

_HTML_TAG_RE = re.compile(r"<[^>]+>")
_MULTI_NEWLINE_RE = re.compile(r"\n{3,}")
_MULTI_SPACE_RE = re.compile(r" {3,}")

_QUOTED_REPLY_PATTERNS = [
    re.compile(r"On .{10,80} wrote:\s*\n.*", re.DOTALL),
    re.compile(r"-{2,}\s*Forwarded message\s*-{2,}.*", re.DOTALL),
    re.compile(r"From:\s+.+\nSent:\s+.+\nTo:\s+.+\n(?:Cc:\s+.+\n)?Subject:\s+.+\n.*", re.DOTALL),
    re.compile(r"_{3,}\nFrom:\s+.+$.*", re.DOTALL | re.MULTILINE),
]

_SIGNATURE_PATTERNS = [
    re.compile(r"\n--\s*\n.*", re.DOTALL),
    re.compile(r"\n(?:Best regards|Kind regards|Regards|Thanks|Cheers|Sincerely|Warm regards),?\s*\n.*", re.DOTALL | re.IGNORECASE),
    re.compile(r"\nSent from my (?:iPhone|iPad|Galaxy|Android|device).*", re.DOTALL | re.IGNORECASE),
    re.compile(r"\nGet Outlook for (?:iOS|Android).*", re.DOTALL | re.IGNORECASE),
]

_FOOTER_NOISE_PATTERNS = [
    re.compile(r"This email and any (?:files|attachments) .{50,500}(?:privileged|confidential).*", re.DOTALL | re.IGNORECASE),
    re.compile(r"CONFIDENTIALITY NOTICE:.*", re.DOTALL | re.IGNORECASE),
    re.compile(r"If you(?:'re| are) not the intended recipient.*", re.DOTALL | re.IGNORECASE),
]


def clean_html(text: str) -> str:
    text = _HTML_TAG_RE.sub("", text)
    text = text.replace("&nbsp;", " ").replace("&amp;", "&")
    text = text.replace("&lt;", "<").replace("&gt;", ">")
    text = text.replace("&quot;", '"').replace("&#39;", "'")
    return text


def clean_email_body(text: str) -> str:
    if not text:
        return ""
    text = clean_html(text)
    for pat in _QUOTED_REPLY_PATTERNS:
        text = pat.sub("", text)
    for pat in _SIGNATURE_PATTERNS:
        text = pat.sub("", text)
    for pat in _FOOTER_NOISE_PATTERNS:
        text = pat.sub("", text)
    text = _MULTI_NEWLINE_RE.sub("\n\n", text)
    text = _MULTI_SPACE_RE.sub(" ", text)
    return text.strip()


# ═════════════════════════════════════════════════════════════════════
# Database Layer
# ═════════════════════════════════════════════════════════════════════

def open_db(db_path: str | Path = DB_PATH) -> "SkillDB":
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    last_err: Exception | None = None
    for attempt in range(_DB_OPEN_RETRIES):
        try:
            conn = sqlite3.connect(str(db_path), timeout=30, check_same_thread=False)
            conn.row_factory = sqlite3.Row
            try:
                conn.execute("PRAGMA journal_mode=WAL")
            except sqlite3.OperationalError:
                try:
                    conn.execute("PRAGMA journal_mode=DELETE")
                except sqlite3.OperationalError:
                    pass
            conn.execute("PRAGMA foreign_keys=ON")
            conn.execute("PRAGMA busy_timeout=10000")
            db = SkillDB(conn)
            db._init_tables()
            return db
        except sqlite3.DatabaseError as exc:
            last_err = exc
            time.sleep(_DB_RETRY_DELAY_S * (attempt + 1))
    raise last_err  # type: ignore[misc]


class SkillDB:
    _WRITE_RETRIES = 3
    _WRITE_RETRY_DELAY_S = 1

    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn
        self._lock = threading.Lock()

    def _retry(self, fn):
        last_err: Exception | None = None
        for attempt in range(self._WRITE_RETRIES):
            try:
                with self._lock:
                    return fn()
            except sqlite3.DatabaseError as exc:
                last_err = exc
                time.sleep(self._WRITE_RETRY_DELAY_S * (attempt + 1))
        raise last_err  # type: ignore[misc]

    def _init_tables(self) -> None:
        self._conn.executescript("""
            CREATE TABLE IF NOT EXISTS atomic_content (
                id           TEXT PRIMARY KEY,
                source       TEXT NOT NULL,
                resource_id  TEXT NOT NULL,
                item_id      TEXT NOT NULL,
                author       TEXT,
                content      TEXT,
                created_at   TEXT,
                updated_at   TEXT,
                cached_at    TEXT NOT NULL,
                metadata     TEXT DEFAULT '{}'
            );
            CREATE INDEX IF NOT EXISTS idx_atomic_resource
                ON atomic_content(source, resource_id);
            CREATE INDEX IF NOT EXISTS idx_atomic_updated
                ON atomic_content(resource_id, updated_at);

            CREATE TABLE IF NOT EXISTS resource_summary (
                resource_id   TEXT PRIMARY KEY,
                source        TEXT NOT NULL,
                title         TEXT,
                summary       TEXT,
                summarized_at TEXT,
                metadata      TEXT DEFAULT '{}'
            );
            CREATE INDEX IF NOT EXISTS idx_summary_source
                ON resource_summary(source);
        """)
        self._migrate_schema()
        self._conn.commit()

    def _migrate_schema(self) -> None:
        existing = {
            row[1] for row in self._conn.execute("PRAGMA table_info(resource_summary)")
        }
        for col_name, col_def in [
            ("mention_type", "TEXT DEFAULT 'none'"),
            ("estimated_relevance", "INTEGER DEFAULT 0"),
            ("final_relevance", "INTEGER DEFAULT 0"),
        ]:
            if col_name not in existing:
                self._conn.execute(
                    f"ALTER TABLE resource_summary ADD COLUMN {col_name} {col_def}"
                )
        self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_summary_relevance ON resource_summary(final_relevance)"
        )

    # ── Atomic Content ──

    def upsert_atomic(self, source: str, resource_id: str, item_id: str,
                      author: str, content: str, created_at: str,
                      updated_at: str, metadata: Optional[dict] = None) -> bool:
        def _do():
            pk = f"{source}:{resource_id}:{item_id}"
            meta_json = json.dumps(metadata or {}, separators=(",", ":"), ensure_ascii=False)
            existing = self._conn.execute(
                "SELECT 1 FROM atomic_content WHERE id = ?", (pk,)
            ).fetchone()
            if existing:
                return False
            self._conn.execute(
                """INSERT INTO atomic_content
                   (id, source, resource_id, item_id, author, content,
                    created_at, updated_at, cached_at, metadata)
                   VALUES (?,?,?,?,?,?,?,?,?,?)""",
                (pk, source, resource_id, item_id, author, content,
                 created_at, updated_at, _now_iso(), meta_json),
            )
            self._conn.commit()
            return True
        return self._retry(_do)

    def has_message(self, resource_id: str, item_id: str) -> bool:
        pk = f"gmail:{resource_id}:{item_id}"
        with self._lock:
            row = self._conn.execute(
                "SELECT 1 FROM atomic_content WHERE id = ?", (pk,)
            ).fetchone()
        return row is not None

    def get_atomic_for_resource(self, resource_id: str) -> list[dict]:
        with self._lock:
            rows = self._conn.execute(
                "SELECT * FROM atomic_content WHERE resource_id=? ORDER BY created_at ASC",
                (resource_id,),
            ).fetchall()
        return [dict(r) for r in rows]

    def get_cached_message_ids(self, resource_id: str) -> set[str]:
        with self._lock:
            rows = self._conn.execute(
                "SELECT item_id FROM atomic_content WHERE resource_id=?",
                (resource_id,),
            ).fetchall()
        return {r["item_id"] for r in rows}

    def get_latest_cached_at(self, resource_id: str) -> Optional[str]:
        with self._lock:
            row = self._conn.execute(
                "SELECT MAX(cached_at) as max_ts FROM atomic_content WHERE resource_id=?",
                (resource_id,),
            ).fetchone()
        return row["max_ts"] if row else None

    def get_all_resource_ids(self, source: Optional[str] = None) -> list[str]:
        with self._lock:
            if source:
                rows = self._conn.execute(
                    "SELECT DISTINCT resource_id FROM atomic_content WHERE source=?", (source,)
                ).fetchall()
            else:
                rows = self._conn.execute(
                    "SELECT DISTINCT resource_id FROM atomic_content"
                ).fetchall()
        return [r["resource_id"] for r in rows]

    # ── Change Detection ──

    def get_thread_meta_last_message_id(self, thread_id: str) -> Optional[str]:
        with self._lock:
            row = self._conn.execute(
                "SELECT metadata FROM atomic_content WHERE resource_id=? ORDER BY cached_at DESC LIMIT 1",
                (thread_id,),
            ).fetchone()
        if not row:
            return None
        meta = json.loads(row["metadata"] or "{}")
        return meta.get("last_message_id")

    def upsert_thread_meta(self, thread_id: str, last_message_id: str) -> None:
        def _do():
            pk = f"gmail:{thread_id}:{last_message_id}"
            row = self._conn.execute(
                "SELECT metadata FROM atomic_content WHERE id = ?", (pk,)
            ).fetchone()
            if not row:
                return
            existing_meta = json.loads(row["metadata"] or "{}")
            if existing_meta.get("last_message_id") == last_message_id:
                return
            existing_meta["last_message_id"] = last_message_id
            self._conn.execute(
                "UPDATE atomic_content SET metadata=? WHERE id=?",
                (json.dumps(existing_meta, separators=(",", ":")), pk),
            )
            self._conn.commit()
        self._retry(_do)

    def thread_needs_fetch(self, thread_id: str, listing_last_msg_id: str) -> bool:
        summary = self.get_resource_summary(thread_id)
        if summary:
            meta = json.loads(summary.get("metadata", "{}"))
            cached = meta.get("last_message_id")
            if cached is not None:
                return listing_last_msg_id != cached
        cached_meta = self.get_thread_meta_last_message_id(thread_id)
        if cached_meta is not None:
            return listing_last_msg_id != cached_meta
        return True

    # ── Mention Type ──

    def compute_mention_type(self, resource_id: str) -> str:
        items = self.get_atomic_for_resource(resource_id)
        if not items:
            return "none"
        user_email = GMAIL_USER_EMAIL.lower()
        for item in items:
            author = (item.get("author") or "").lower()
            if user_email in author:
                return "direct"
        for item in items:
            meta = json.loads(item.get("metadata", "{}"))
            for recipient in meta.get("to", []):
                if isinstance(recipient, dict) and user_email == (recipient.get("email") or "").lower():
                    return "direct"
            for recipient in meta.get("cc", []):
                if isinstance(recipient, dict) and user_email == (recipient.get("email") or "").lower():
                    return "direct"
        return "indirect"

    # ── Resource Summary ──

    def get_resource_summary(self, resource_id: str) -> Optional[dict]:
        with self._lock:
            row = self._conn.execute(
                "SELECT * FROM resource_summary WHERE resource_id=?", (resource_id,)
            ).fetchone()
        return dict(row) if row else None

    def needs_resummarize(self, resource_id: str) -> bool:
        existing = self.get_resource_summary(resource_id)
        if not existing:
            return True
        summarized_at = existing.get("summarized_at")
        if not summarized_at:
            return True
        latest_cached = self.get_latest_cached_at(resource_id)
        if not latest_cached:
            return False
        return latest_cached > summarized_at

    def get_items_since(self, resource_id: str, since_timestamp: str) -> list[dict]:
        with self._lock:
            rows = self._conn.execute(
                """SELECT * FROM atomic_content
                   WHERE resource_id=? AND cached_at > ?
                   ORDER BY created_at ASC""",
                (resource_id, since_timestamp),
            ).fetchall()
        return [dict(r) for r in rows]

    def upsert_summary(self, resource_id: str, source: str, title: str,
                       summary: str, metadata: Optional[dict] = None,
                       mention_type: str = "none",
                       estimated_relevance: int = 0,
                       final_relevance: int = 0) -> None:
        def _do():
            meta_json = json.dumps(metadata or {}, separators=(",", ":"), ensure_ascii=False)
            self._conn.execute(
                """INSERT INTO resource_summary
                   (resource_id, source, title, summary, summarized_at, metadata,
                    mention_type, estimated_relevance, final_relevance)
                   VALUES (?,?,?,?,?,?,?,?,?)
                   ON CONFLICT(resource_id) DO UPDATE SET
                     source=excluded.source, title=excluded.title,
                     summary=excluded.summary, summarized_at=excluded.summarized_at,
                     metadata=excluded.metadata, mention_type=excluded.mention_type,
                     estimated_relevance=excluded.estimated_relevance,
                     final_relevance=excluded.final_relevance""",
                (resource_id, source, title, summary, _now_iso(), meta_json,
                 mention_type, estimated_relevance, final_relevance),
            )
            self._conn.commit()
        self._retry(_do)

    def get_all_summaries(self, source: Optional[str] = None,
                          min_relevance: int = 0,
                          since: Optional[str] = None) -> list[dict]:
        with self._lock:
            query = """
                SELECT rs.*,
                       COALESCE(ac_latest.max_cached, rs.summarized_at) AS sort_ts
                FROM resource_summary rs
                LEFT JOIN (
                    SELECT resource_id, MAX(cached_at) AS max_cached
                    FROM atomic_content GROUP BY resource_id
                ) ac_latest ON ac_latest.resource_id = rs.resource_id
                WHERE 1=1
            """
            params: list = []
            if source:
                query += " AND rs.source = ?"
                params.append(source)
            if min_relevance > 0:
                query += " AND rs.final_relevance >= ?"
                params.append(min_relevance)
            if since:
                query += " AND COALESCE(ac_latest.max_cached, rs.summarized_at) >= ?"
                params.append(since)
            query += " ORDER BY sort_ts DESC"
            rows = self._conn.execute(query, params).fetchall()
        return [dict(r) for r in rows]

    def clear_all_summaries(self) -> int:
        def _do():
            cursor = self._conn.execute(
                "UPDATE resource_summary SET summary=NULL, summarized_at=NULL, "
                "mention_type='none', estimated_relevance=0, final_relevance=0"
            )
            self._conn.commit()
            return cursor.rowcount
        return self._retry(_do)

    def close(self) -> None:
        self._conn.close()


# ═════════════════════════════════════════════════════════════════════
# AI Summarizer
# ═════════════════════════════════════════════════════════════════════

@dataclass
class SummaryResult:
    relevance: int
    summary: str
    work_items: list[str] = field(default_factory=list)
    people: list[str] = field(default_factory=list)
    labels: list[str] = field(default_factory=list)


_USER_CONTEXT: Optional[str] = None


def _load_user_context() -> str:
    global _USER_CONTEXT
    if _USER_CONTEXT is not None:
        return _USER_CONTEXT
    try:
        _USER_CONTEXT = _USER_MD_PATH.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        log(f"WARNING: User.md not found at {_USER_MD_PATH}")
        _USER_CONTEXT = ""
    return _USER_CONTEXT


def _build_system_prompt() -> str:
    return f"""You are a relevance-scoring executive assistant. Score the relevance, summarize, and extract entities from the content for the following user.

{_load_user_context()}"""


def _build_user_prompt(title: str, source_type: str, meta_json: str,
                       content: str, mention_type: str,
                       existing_summary: Optional[str] = None) -> str:
    word_hint = _WORD_HINTS.get(mention_type, 30)
    parts = [
        f"Analyze this {source_type} resource and return a JSON response.",
        f"\nResource: {title}",
        f"Mention Type: {mention_type}",
        "  - direct: user is explicitly in TO/CC, or has replied/sent a message in this thread",
        "  - indirect: received via group/distribution list without direct address",
        "  - none: no personal involvement detected",
        f"Metadata: {meta_json}",
    ]
    if existing_summary:
        parts.append(f"\nExisting summary (update with new content, preserve still-relevant context):\n{existing_summary}")
    parts.append(f"\nContent (chronological):\n{content}")
    parts.append(f"""
Scoring rules:
- Refer to the user's "What Matters Most" section for scoring guidance
- RELEVANCE FLOOR: direct mention_type >= 7, indirect >= 5
- Automated system alerts/notifications: score LOW unless a human has manually replied
- Adapt summary length: relevance 8-10 = up to 200 words, 5-7 = up to 100 words, 1-4 = up to 30 words (hint: ~{word_hint} words)
- Keep all person names, dates, and concrete next actions

Entity extraction rules:
- work_items: Extract Jira ticket IDs (e.g., DPD-715), PR numbers (e.g., PR #649), project codenames (e.g., BCRS, RMN), service names, and git repository names. Empty list if none found.
- people: Extract ONLY explicit person names (e.g., "Nikhil Grover"). Do NOT include group names, team names, or distribution lists. Empty list if none.
- labels: Generate exactly 5 descriptive 2-word labels (lowercase, hyphenated) that best characterize this resource's topic and activity.

Return ONLY valid JSON:
{{"relevance": <integer 1-10>, "summary": "<your summary>", "work_items": ["<id1>"], "people": ["<person1>"], "labels": ["<word-word>", "<word-word>", "<word-word>", "<word-word>", "<word-word>"]}}""")
    return "\n".join(parts)


def parse_llm_response(raw: str, mention_type: str) -> SummaryResult:
    if raw.startswith("<think>"):
        end = raw.find("</think>")
        if end != -1:
            raw = raw[end + 8:].strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```\w*\n?", "", raw)
        raw = re.sub(r"\n?```$", "", raw)
        raw = raw.strip()

    try:
        data = json.loads(raw)
        relevance = int(data["relevance"])
        summary = str(data["summary"])
        work_items = [str(x) for x in data.get("work_items", [])]
        people = [str(x) for x in data.get("people", [])]
        labels = [str(x) for x in data.get("labels", [])][:5]
    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        log(f"WARNING: JSON parse failed, using regex fallback. Raw: {raw[:200]}")
        m = re.search(r'"relevance"\s*:\s*(\d+)', raw)
        relevance = int(m.group(1)) if m else 5
        sm = re.search(r'"summary"\s*:\s*"((?:[^"\\]|\\.)*)"', raw)
        summary = sm.group(1) if sm else raw
        work_items, people, labels = [], [], []

    floor = _RELEVANCE_FLOORS.get(mention_type, 1)
    relevance = max(min(relevance, 10), floor)
    return SummaryResult(relevance, summary, work_items, people, labels)


def _call_llm(system_prompt: str, user_prompt: str) -> str:
    url = f"{LITELLM_BASE}/chat/completions"
    headers = {"Content-Type": "application/json"}
    if LITELLM_API_KEY:
        headers["Authorization"] = f"Bearer {LITELLM_API_KEY}"
    payload = {
        "model": SUMMARIZE_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.3,
        "response_format": {"type": "json_object"},
    }

    last_error: Optional[Exception] = None
    for attempt in range(1, SUMMARIZE_RETRIES + 2):
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=120)
        except requests.RequestException as exc:
            last_error = exc
            if attempt <= SUMMARIZE_RETRIES:
                wait = SUMMARIZE_RETRY_INITIAL_SEC * (2 ** (attempt - 1))
                log(f"  [retry {attempt}/{SUMMARIZE_RETRIES}] Connection error: {exc} - retrying in {wait:.0f}s")
                time.sleep(wait)
                continue
            raise RuntimeError(f"LLM connection failed after {SUMMARIZE_RETRIES} retries: {exc}") from exc

        if resp.status_code >= 500:
            last_error = RuntimeError(f"LLM API {resp.status_code}: {resp.text[:300]}")
            if attempt <= SUMMARIZE_RETRIES:
                wait = SUMMARIZE_RETRY_INITIAL_SEC * (2 ** (attempt - 1))
                log(f"  [retry {attempt}/{SUMMARIZE_RETRIES}] 5xx error - retrying in {wait:.0f}s")
                time.sleep(wait)
                continue
            raise last_error

        if resp.status_code != 200:
            raise RuntimeError(f"LLM API {resp.status_code}: {resp.text[:300]}")

        content = resp.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        if not content:
            raise RuntimeError("LLM returned empty content")
        return content.strip()

    raise RuntimeError(f"LLM failed after {SUMMARIZE_RETRIES} retries") from last_error


def summarize_resource(title: str, source_type: str, atomic_items: list[dict],
                       metadata: Optional[dict] = None,
                       existing_summary: Optional[str] = None,
                       mention_type: str = "none") -> SummaryResult:
    if not atomic_items:
        return SummaryResult(1, existing_summary or "")

    content_parts = []
    for item in atomic_items:
        author = item.get("author", "Unknown")
        ts = item.get("created_at", "")
        text = item.get("content", "")
        if text:
            content_parts.append(f"[{ts}] {author}: {text}")

    content_block = "\n---\n".join(content_parts)
    meta_json = json.dumps(metadata or {}, indent=2, ensure_ascii=False)

    system_prompt = _build_system_prompt()
    user_prompt = _build_user_prompt(
        title, source_type, meta_json, content_block, mention_type, existing_summary
    )
    raw = _call_llm(system_prompt, user_prompt)
    return parse_llm_response(raw, mention_type)


# ═════════════════════════════════════════════════════════════════════
# Browser & Navigation (CDP)
# ═════════════════════════════════════════════════════════════════════

def connect_browser(cdp_url: str):
    pw = sync_playwright().start()
    browser = pw.chromium.connect_over_cdp(cdp_url)
    contexts = browser.contexts
    context = contexts[0] if contexts else browser.new_context()
    pages = context.pages
    gmail_page = None
    for p in pages:
        if "mail.google.com" in p.url:
            gmail_page = p
            break
    if not gmail_page:
        gmail_page = context.new_page()
    return pw, browser, gmail_page


def navigate_to_page(page, days: int, page_num: int) -> bool:
    if page_num <= 1:
        search_url = f"{GMAIL_BASE}/mail/u/0/#search/newer_than%3A{days}d"
    else:
        search_url = f"{GMAIL_BASE}/mail/u/0/#search/newer_than%3A{days}d/p{page_num}"
    page.goto(search_url, wait_until="domcontentloaded", timeout=30000)
    time.sleep(5)
    try:
        page.wait_for_selector('div[role="main"] tr[jscontroller]', timeout=20000)
        return True
    except PwTimeout:
        return False


def get_thread_list(page) -> list[dict]:
    return page.evaluate("""
    () => {
        const main = document.querySelector('div[role="main"]');
        if (!main) return [];
        const rows = main.querySelectorAll('tr[jscontroller]');
        const threads = [];
        for (let i = 0; i < rows.length; i++) {
            const tr = rows[i];
            const tds = tr.querySelectorAll('td');
            if (tds.length < 9) continue;
            let legacyThreadId = '';
            let legacyLastMsgId = '';
            const idSpans = tr.querySelectorAll('span[data-legacy-thread-id]');
            if (idSpans.length > 0) legacyThreadId = idSpans[0].getAttribute('data-legacy-thread-id') || '';
            const lastMsgSpans = tr.querySelectorAll('span[data-legacy-last-non-draft-message-id]');
            if (lastMsgSpans.length > 0) legacyLastMsgId = lastMsgSpans[0].getAttribute('data-legacy-last-non-draft-message-id') || '';
            const senderEls = tr.querySelectorAll('span[email]');
            const senders = [];
            const seen = new Set();
            for (const s of senderEls) {
                const email = s.getAttribute('email') || '';
                if (!seen.has(email)) {
                    seen.add(email);
                    senders.push({ name: s.getAttribute('name') || s.textContent.trim(), email: email });
                }
            }
            let subject = '';
            const bogSpan = tds[5].querySelector('span.bog');
            if (bogSpan) subject = bogSpan.textContent.trim();
            if (!subject) {
                let maxLen = 0;
                for (const s of tds[5].querySelectorAll('span')) {
                    const t = s.textContent.trim();
                    if (t.length > maxLen && t.length > 5) { maxLen = t.length; subject = t; }
                }
            }
            const dateSpan = tds[8].querySelector('span[title]');
            const date = dateSpan ? dateSpan.getAttribute('title') : tds[8].textContent.trim();
            const labelEls = tds[5].querySelectorAll('div.at');
            const labels = [];
            for (const l of labelEls) labels.push(l.getAttribute('title') || l.textContent.trim());
            threads.push({
                rowIndex: i, legacyThreadId, legacyLastMsgId,
                senders, subject, date, labels
            });
        }
        return threads;
    }
    """)


def navigate_to_thread(page, thread_id: str) -> bool:
    url = f"{GMAIL_BASE}/mail/u/0/#all/{thread_id}"
    page.goto(url, wait_until="domcontentloaded", timeout=20000)
    time.sleep(2)
    try:
        page.wait_for_selector('[data-message-id], div.adn, table.Bs, h2.hP', timeout=15000)
        time.sleep(1.5)
        return True
    except PwTimeout:
        return False


def _wait_for_messages_stable(page, max_wait: float = 30.0, poll_interval: float = 1.0):
    prev_count = 0
    stable_rounds = 0
    elapsed = 0.0
    while elapsed < max_wait:
        count = page.evaluate("() => document.querySelectorAll('[data-message-id]').length")
        if count == prev_count and count > 0:
            stable_rounds += 1
            if stable_rounds >= 2:
                return count
        else:
            stable_rounds = 0
        prev_count = count
        time.sleep(poll_interval)
        elapsed += poll_interval
    return prev_count


def expand_all_messages(page):
    expanded = page.evaluate("""
    () => {
        const btn = document.querySelector('button[aria-label="Expand all"]');
        if (btn) { btn.click(); return true; }
        return false;
    }
    """)
    if expanded:
        _wait_for_messages_stable(page)
    page.evaluate("""
    () => {
        const detailBtns = document.querySelectorAll('img[aria-label="Show details"], span.ajy, div.ajz');
        for (const btn of detailBtns) { try { btn.click(); } catch(e) {} }
    }
    """)
    time.sleep(1)
    page.evaluate("""
    () => {
        const trimmers = document.querySelectorAll('[aria-label="Show trimmed content"]');
        for (const el of trimmers) { try { el.click(); } catch(e) {} }
    }
    """)
    time.sleep(0.5)


def extract_thread_messages(page) -> list[dict]:
    expand_all_messages(page)
    return page.evaluate("""
    () => {
        const messages = [];
        const msgContainers = document.querySelectorAll('[data-message-id]');
        for (const container of msgContainers) {
            const legacyMsgId = container.getAttribute('data-legacy-message-id') || '';
            const fromEl = container.querySelector('span.gD[email]');
            let sender = 'Unknown';
            if (fromEl) {
                const name = fromEl.getAttribute('name') || fromEl.textContent.trim();
                const email = fromEl.getAttribute('email') || '';
                sender = email ? name + ' <' + email + '>' : name;
            }
            let date = '';
            const dateEl = container.querySelector('span.g3[title]');
            if (dateEl) date = dateEl.getAttribute('title') || dateEl.textContent.trim();
            if (!date) {
                const fallbackDate = container.querySelectorAll('span[title]');
                for (const d of fallbackDate) {
                    const title = d.getAttribute('title') || '';
                    if (title.match(/\\d{1,2},?\\s*\\d{4}/)) { date = title; break; }
                }
            }
            const allEmailSpans = container.querySelectorAll('span[email]');
            const fromEmail = fromEl ? fromEl.getAttribute('email') : '';
            const toList = [];
            const ccList = [];
            const detailTable = container.querySelector('table.ajB');
            if (detailTable) {
                const dtRows = detailTable.querySelectorAll('tr');
                for (const row of dtRows) {
                    const label = row.querySelector('td.aGb');
                    const value = row.querySelector('td.ajA');
                    if (label && value) {
                        const labelText = label.textContent.trim().toLowerCase();
                        const emailEls = value.querySelectorAll('span[email]');
                        for (const e of emailEls) {
                            const recipient = { name: e.getAttribute('name') || e.textContent.trim(), email: e.getAttribute('email') || '' };
                            if (labelText.startsWith('to')) toList.push(recipient);
                            else if (labelText.startsWith('cc')) ccList.push(recipient);
                        }
                    }
                }
            }
            if (toList.length === 0 && ccList.length === 0) {
                let foundFrom = false;
                for (const s of allEmailSpans) {
                    const email = s.getAttribute('email') || '';
                    if (email === fromEmail && !foundFrom) { foundFrom = true; continue; }
                    toList.push({ name: s.getAttribute('name') || s.textContent.trim(), email: email });
                }
            }
            let body = '';
            const bodySelectors = ['div.a3s.aiL', 'div.a3s', 'div[dir="ltr"]'];
            for (const sel of bodySelectors) {
                const bodyEl = container.querySelector(sel);
                if (bodyEl && bodyEl.textContent.trim().length > 5) { body = bodyEl.innerText.trim(); break; }
            }
            if (!body) {
                const clone = container.cloneNode(true);
                const headers = clone.querySelectorAll('.gE, .gH, .gK, .gs');
                for (const h of headers) h.remove();
                body = clone.innerText ? clone.innerText.trim() : clone.textContent.trim();
            }
            body = body.replace(/\\n{3,}/g, '\\n\\n').trim();
            messages.push({ legacy_message_id: legacyMsgId, from: sender, to: toList, cc: ccList, date: date, body: body });
        }
        return messages;
    }
    """)


def get_thread_subject(page) -> str:
    return page.evaluate("""
    () => {
        const h2 = document.querySelector('div[role="main"] h2.hP');
        if (h2) return h2.textContent.trim();
        const h2Alt = document.querySelector('div[role="main"] h2');
        if (h2Alt) return h2Alt.textContent.trim();
        return '';
    }
    """) or ""


# ═════════════════════════════════════════════════════════════════════
# Caching & Summarization Pipeline
# ═════════════════════════════════════════════════════════════════════

def cache_thread_messages(db: SkillDB, thread_id: str, subject: str,
                          messages: list[dict]) -> int:
    cached_ids = db.get_cached_message_ids(thread_id)
    new_count = 0
    for msg in messages:
        msg_id = msg.get("legacy_message_id", "")
        if not msg_id or msg_id in cached_ids:
            continue
        body = clean_email_body(msg.get("body", ""))
        author = msg.get("from", "Unknown")
        date = msg.get("date", "")
        meta = {"to": msg.get("to", []), "cc": msg.get("cc", []), "subject": subject}
        if db.upsert_atomic("gmail", thread_id, msg_id, author=author,
                            content=body, created_at=date, updated_at=date,
                            metadata=meta):
            new_count += 1
    return new_count


def _summarize_one(db: SkillDB, thread_id: str, thread_info: dict,
                   force: bool = False, current: int = 0, total: int = 0) -> None:
    subject = thread_info.get("subject", thread_id)

    if not force and not db.needs_resummarize(thread_id):
        existing = db.get_resource_summary(thread_id)
        if existing and existing.get("summary"):
            log(f"[{current}/{total}] {thread_id}: cached (rel={existing.get('final_relevance', '?')})")
            return

    existing_summary = db.get_resource_summary(thread_id)
    existing_text = existing_summary["summary"] if existing_summary else None
    summarized_at = existing_summary.get("summarized_at") if existing_summary else None

    if existing_text and summarized_at:
        items = db.get_items_since(thread_id, summarized_at)
        if not items:
            items = db.get_atomic_for_resource(thread_id)
    else:
        items = db.get_atomic_for_resource(thread_id)

    if not items:
        return

    mention_type = db.compute_mention_type(thread_id)
    labels_from_thread = thread_info.get("labels", [])
    meta = {"labels": labels_from_thread, "last_message_id": thread_info.get("last_msg_id", "")}

    log(f"Summarizing [{current}/{total}] {subject[:50]} ({len(items)} msgs, {mention_type})")

    result = summarize_resource(
        title=subject, source_type="Email thread", atomic_items=items,
        metadata=meta, existing_summary=existing_text, mention_type=mention_type,
    )

    if not result.summary:
        raise RuntimeError(f"Empty summary for {thread_id}")

    enriched_meta = dict(meta)
    enriched_meta["work_items"] = result.work_items
    enriched_meta["people"] = result.people
    enriched_meta["labels"] = result.labels

    senders = thread_info.get("senders", [])
    if senders:
        enriched_meta["senders"] = senders

    db.upsert_summary(
        thread_id, "gmail", subject, result.summary, enriched_meta,
        mention_type=mention_type,
        estimated_relevance=result.relevance,
        final_relevance=result.relevance,
    )
    log(f"Done [{current}/{total}] {thread_id} rel={result.relevance}")


def _summarize_worker(q: "_queue.Queue", db: SkillDB, force: bool, errors: list) -> None:
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        thread_id, thread_info, current, total = item
        try:
            _summarize_one(db, thread_id, thread_info, force, current, total)
        except Exception as exc:
            log(f"ERROR summarizing {thread_id}: {exc}")
            errors.append(f"{thread_id}: {exc}")
        finally:
            q.task_done()


class _Pipeline:
    def __init__(self, db: SkillDB, force: bool):
        self._q: _queue.Queue = _queue.Queue()
        self._errors: list = []
        self._counter = 0
        self._total = 0
        self._thread = threading.Thread(
            target=_summarize_worker, args=(self._q, db, force, self._errors), daemon=True
        )
        self._thread.start()

    def set_total(self, total: int) -> None:
        self._total = total

    def put(self, thread_id: str, thread_info: dict) -> None:
        self._counter += 1
        self._q.put((thread_id, thread_info, self._counter, self._total))

    def finish(self) -> list[str]:
        self._q.put(None)
        self._thread.join()
        return self._errors


# ═════════════════════════════════════════════════════════════════════
# Output Formatting
# ═════════════════════════════════════════════════════════════════════

def _format_summary_block(s: dict, idx: int, total: int) -> str:
    meta = json.loads(s.get("metadata", "{}"))
    title = s.get("title", "(no subject)")
    parts = [f"Source: gmail", f"Thread: {s['resource_id']}"]

    rel = s.get("final_relevance", s.get("estimated_relevance", 0))
    mt = s.get("mention_type", "none")
    if rel:
        parts.append(f"Relevance: {rel}/10")
    if mt and mt != "none":
        parts.append(f"Mention: {mt}")

    labels = meta.get("labels", [])
    if isinstance(labels, list) and labels and isinstance(labels[0], str) and "-" in labels[0]:
        parts.append(f"Labels: {', '.join(labels)}")
    elif isinstance(labels, list) and labels:
        parts.append(f"Gmail Labels: {', '.join(str(l) for l in labels)}")

    senders = meta.get("senders", [])
    if senders:
        sender_names = ", ".join(s.get("name", s.get("email", "")) for s in senders if isinstance(s, dict))
        if sender_names:
            parts.append(f"Senders: {sender_names}")

    if meta.get("work_items"):
        parts.append(f"Work Items: {', '.join(meta['work_items'])}")
    if meta.get("people"):
        parts.append(f"People: {', '.join(meta['people'])}")

    header = f"[{idx}/{total}] {title}"
    return f"\n\n## {header}\n{' | '.join(parts)}\n{s.get('summary', '')}"


def write_output(db: SkillDB, output_path: Path, min_relevance: int = 6,
                 since: Optional[str] = None) -> None:
    summaries = db.get_all_summaries(source="gmail", min_relevance=min_relevance, since=since)
    total = len(summaries)
    lines = []
    for idx, s in enumerate(summaries, 1):
        lines.append(_format_summary_block(s, idx, total))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("".join(lines), encoding="utf-8")
    log(f"Output: {output_path} ({total} summaries, min_relevance={min_relevance})")


# ═════════════════════════════════════════════════════════════════════
# Main Entry Point
# ═════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Gmail Skill - fetch, cache, and summarize email threads")
    parser.add_argument("--cdp-url", default=DEFAULT_CDP, help=f"Chrome DevTools endpoint (default: {DEFAULT_CDP})")
    parser.add_argument("--days", type=int, default=None,
                        help="Lookback days (default: 3 Tue-Sat, 4 Sun, 5 Mon)")
    parser.add_argument("--max-threads", type=int, default=200, help="Max threads to read (default: 200)")
    parser.add_argument("--max-scan", type=int, default=500, help="Max total threads to scan (default: 500)")
    parser.add_argument("--exclude-labels", default=DEFAULT_EXCLUDE, help="JSON array of labels to exclude")
    parser.add_argument("--early-stop", type=int, default=5,
                        help="Stop after N consecutive cached threads (default: 5, 0=disabled)")
    parser.add_argument("--cached-only", action="store_true", help="Output from DB only, no browser or summarization")
    parser.add_argument("--force", action="store_true", help="Clear summaries and re-summarize (keeps cached content)")
    parser.add_argument("--min-relevance", type=int, default=6, help="Minimum relevance for output (default: 6)")
    parser.add_argument("--output", default=str(_WORKDIR / "gmail-output.md"), help="Output .md path")
    args = parser.parse_args()

    output_path = Path(args.output)
    days = args.days if args.days is not None else _default_lookback_days()
    since_dt = datetime.now(_TZ) - timedelta(days=days)
    since_iso = since_dt.strftime("%Y-%m-%d")

    if output_path.exists():
        output_path.unlink()

    db = open_db()
    log(f"STARTED (days={days}, since={since_iso}, user={GMAIL_USER_EMAIL})")

    if args.force:
        count = db.clear_all_summaries()
        log(f"--force: cleared {count} summaries (cached content preserved)")

    try:
        exclude_labels = json.loads(args.exclude_labels)
    except json.JSONDecodeError:
        log(f"ERROR: Invalid JSON for --exclude-labels: {args.exclude_labels}")
        sys.exit(1)

    try:
        if args.cached_only:
            write_output(db, output_path, min_relevance=args.min_relevance, since=since_iso)
            log("COMPLETED (cached-only)")
            return

        if args.force:
            resource_ids = db.get_all_resource_ids(source="gmail")
            log(f"--force: re-summarizing {len(resource_ids)} cached threads (no browser)")
            pipeline = _Pipeline(db, force=True)
            pipeline.set_total(len(resource_ids))
            for rid in resource_ids:
                existing = db.get_resource_summary(rid)
                info = {"subject": existing["title"] if existing else rid, "labels": [], "senders": []}
                pipeline.put(rid, info)
            errors = pipeline.finish()
            if errors:
                log(f"COMPLETED WITH ERRORS ({len(resource_ids)} threads, {len(errors)} error(s))")
                for e in errors:
                    log(f"  ERROR: {e}")
                sys.exit(1)
            write_output(db, output_path, min_relevance=args.min_relevance, since=since_iso)
            log(f"COMPLETED --force ({len(resource_ids)} threads)")
            return

        # ── Phase 1: Scan listing pages ──
        log(f"Connecting to browser at {args.cdp_url}...")
        pw, browser, page = connect_browser(args.cdp_url)
        log("Browser connected.")

        thread_infos: list[dict] = []
        threads_to_fetch: list[dict] = []
        seen_ids: set[str] = set()
        scanned = 0
        skipped_excluded = 0
        skipped_unchanged = 0
        consecutive_cached = 0
        early_stop_triggered = False
        page_num = 1

        while len(thread_infos) < args.max_threads and scanned < args.max_scan:
            if not navigate_to_page(page, days, page_num):
                if page_num == 1:
                    log("FATAL: 0 threads found")
                    sys.exit(2)
                break

            thread_list = get_thread_list(page)
            if not thread_list:
                break

            log(f"  Page {page_num}: {len(thread_list)} thread(s)")

            for row in thread_list:
                if len(thread_infos) >= args.max_threads or scanned >= args.max_scan:
                    break

                thread_id = row.get("legacyThreadId", "")
                if not thread_id or thread_id in seen_ids:
                    continue
                seen_ids.add(thread_id)
                scanned += 1

                labels = row.get("labels", [])
                subject = row.get("subject", "(no subject)")
                last_msg_id = row.get("legacyLastMsgId", "")

                should_exclude = any(el.strip() in [l.strip() for l in labels] for el in exclude_labels)
                if should_exclude:
                    skipped_excluded += 1
                    continue

                info = {
                    "thread_id": thread_id, "subject": subject, "labels": labels,
                    "senders": row.get("senders", []), "date": row.get("date", ""),
                    "last_msg_id": last_msg_id, "fetched": False,
                }

                if early_stop_triggered or (not db.thread_needs_fetch(thread_id, last_msg_id)):
                    thread_infos.append(info)
                    skipped_unchanged += 1
                    if not early_stop_triggered:
                        consecutive_cached += 1
                        if args.early_stop > 0 and consecutive_cached >= args.early_stop:
                            log(f"  Early stop: {consecutive_cached} consecutive cached")
                            early_stop_triggered = True
                    continue

                consecutive_cached = 0
                thread_infos.append(info)
                threads_to_fetch.append(info)

            if len(thread_infos) >= args.max_threads or scanned >= args.max_scan:
                break
            page_num += 1

        log(f"Phase 1: {len(thread_infos)} threads (excluded={skipped_excluded}, "
            f"unchanged={skipped_unchanged}, to-fetch={len(threads_to_fetch)})")

        # ── Phase 2+3: Fetch and summarize in pipeline ──
        pipeline = _Pipeline(db, force=False)
        pipeline.set_total(len(thread_infos))
        fetched_ids: set[str] = set()

        for idx, info in enumerate(threads_to_fetch, 1):
            thread_id = info["thread_id"]
            subject = info["subject"]
            last_msg_id = info.get("last_msg_id", "")
            log(f"[Fetching {idx}/{len(threads_to_fetch)}] {subject[:55]}")

            if not navigate_to_thread(page, thread_id):
                time.sleep(2)
                if not navigate_to_thread(page, thread_id):
                    log(f"  WARN: {thread_id} failed to load, skipping")
                    continue

            thread_subject = get_thread_subject(page) or subject
            messages = extract_thread_messages(page)

            new_count = cache_thread_messages(db, thread_id, thread_subject, messages)
            if new_count > 0:
                log(f"  -> {new_count} new message(s) cached")
            db.upsert_thread_meta(thread_id, last_msg_id)

            info["subject"] = thread_subject
            info["fetched"] = True
            fetched_ids.add(thread_id)
            pipeline.put(thread_id, info)

        for info in thread_infos:
            if info["thread_id"] not in fetched_ids:
                pipeline.put(info["thread_id"], info)

        errors = pipeline.finish()

        if browser:
            try:
                browser.close()
            except Exception:
                pass
        if pw:
            try:
                pw.stop()
            except Exception:
                pass

        if errors:
            log(f"COMPLETED WITH ERRORS ({len(thread_infos)} threads, {len(errors)} error(s))")
            for e in errors:
                log(f"  ERROR: {e}")
            sys.exit(1)

        write_output(db, output_path, min_relevance=args.min_relevance, since=since_iso)
        log(f"COMPLETED ({len(thread_infos)} threads, fetched={len(fetched_ids)})")

    except SystemExit:
        raise
    except Exception as e:
        log(f"FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        db.close()


if __name__ == "__main__":
    main()
