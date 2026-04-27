#!/usr/bin/env python3
"""
GChat Skill - Extract Google Chat conversations via CDP, cache, and AI-summarize.

Single-file skill that:
1. Connects to remote Chrome via CDP, navigates GChat Home feed (3-panel layout)
2. Extracts conversations with progressive message collection (virtual scroll aware)
3. Caches messages in SQLite with mention_type detection
4. Summarizes via LLM with relevance scoring, entity extraction, JSON output
5. Writes final output .md only after all summaries succeed

Usage:
  python gchat.py
  python gchat.py --days 7 --max-threads 10
  python gchat.py --cached-only
  python gchat.py --force
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

_REQUIRED_PACKAGES = {
    "requests": "requests",
    "playwright": "playwright",
}


def _ensure_dependencies():
    missing = []
    for import_name, pip_name in _REQUIRED_PACKAGES.items():
        try:
            __import__(import_name)
        except ImportError:
            missing.append(pip_name)
    if missing:
        import subprocess
        print(f"[gchat] Installing missing packages: {', '.join(missing)}", flush=True)
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--quiet"] + missing
        )
        if "playwright" in missing:
            subprocess.check_call(
                [sys.executable, "-m", "playwright", "install", "chromium"]
            )


_ensure_dependencies()

import requests  # noqa: E402
from playwright.sync_api import sync_playwright, TimeoutError as PwTimeout  # noqa: E402

# ═════════════════════════════════════════════════════════════════════
# Configuration
# ═════════════════════════════════════════════════════════════════════

DEFAULT_CDP = os.environ.get("CDP_URL", "http://192.168.1.11:9223")
GCHAT_URL = "https://chat.google.com/app/home"
GCHAT_USER_NAME = os.environ.get("GCHAT_USER_NAME", "Michael Bui")
GCHAT_USER_EMAIL = os.environ.get("GCHAT_USER_EMAIL", "michael.bui@fairpricegroup.sg")

LITELLM_BASE = os.environ.get("LITELLM_BASE_URL", "https://llm.gigary.com/v1")
SUMMARIZE_MODEL = os.environ.get("SUMMARIZE_MODEL", "local/qwen3.6-35b-a3b:thinking-general")
LITELLM_API_KEY = os.environ.get("API_KEY_OTHER", os.environ.get("LLAMA_TOKEN", ""))
SUMMARIZE_RETRIES = int(os.environ.get("SUMMARIZE_RETRIES", "3"))
SUMMARIZE_RETRY_INITIAL_SEC = float(os.environ.get("SUMMARIZE_RETRY_INITIAL_SEC", "30"))

_DEFAULT_CTX_LIMIT = int(os.environ.get("LLM_CONTEXT_LIMIT", "50000"))
_WORKDIR = Path(__file__).resolve().parents[3] / "workdir"
_DEFAULT_DB_PATH = Path(__file__).resolve().parent.parent / "data" / "gchat_cache.db"
DB_PATH = Path(os.environ.get("GCHAT_DB_PATH", str(_DEFAULT_DB_PATH)))
_USER_MD_PATH = Path(__file__).resolve().parents[3] / "User.md"

_TZ = ZoneInfo(os.environ.get("TZ", "Asia/Singapore"))

_RELEVANCE_FLOORS = {"direct": 5, "indirect": 5, "none": 1}
_WORD_HINTS = {"direct": 200, "indirect": 100, "none": 30}

_DB_OPEN_RETRIES = 3
_DB_RETRY_DELAY_S = 2

def _default_lookback_days() -> int:
    """Always cover 3 weekdays: 5 (Mon-Tue), 4 (Sun), 3 (Wed-Sat)."""
    weekday = datetime.now(_TZ).weekday()
    if weekday in (0, 1):
        return 5
    if weekday == 6:
        return 4
    return 3


SEL_FEED = 'span[role="listitem"][data-group-id][data-is-unread]'
SEL_MSG = "c-wiz[data-topic-id]"

FIND_PANEL_JS = """
function findPanel(topicId) {
    const mid = window.innerWidth / 3;
    if (topicId) {
        const match = document.querySelector(
            'c-wiz[data-topic-id="' + topicId + '"]'
        );
        if (match) {
            let el = match.parentElement;
            while (el && el !== document.body) {
                const s = getComputedStyle(el);
                if ((s.overflowY === "auto" || s.overflowY === "scroll")
                    && el.clientHeight > 100) {
                    const r = el.getBoundingClientRect();
                    if (r.width > 100 && r.left >= mid) return el;
                }
                el = el.parentElement;
            }
        }
    }
    let best = null, bestArea = 0;
    for (const el of document.getElementsByTagName("div")) {
        const s = getComputedStyle(el);
        if (s.overflowY !== "auto" && s.overflowY !== "scroll") continue;
        if (el.clientHeight < 100) continue;
        const r = el.getBoundingClientRect();
        if (r.left < mid || r.width < 100) continue;
        const a = r.width * r.height;
        if (a > bestArea) { bestArea = a; best = el; }
    }
    return best;
}
"""


# ═════════════════════════════════════════════════════════════════════
# Logging
# ═════════════════════════════════════════════════════════════════════

_LOG_LEVEL = os.environ.get("GCHAT_LOG_LEVEL", "INFO").upper()


def _ts() -> str:
    return datetime.now(_TZ).strftime("%Y-%m-%dT%H:%M:%S%z")


def log(*a, **kw):
    print(f"[{_ts()}]", *a, flush=True, **kw)


def debug(*a, **kw):
    if _LOG_LEVEL == "DEBUG":
        print(f"[{_ts()}] DEBUG:", *a, flush=True, **kw)


# ═════════════════════════════════════════════════════════════════════
# Text Cleanup
# ═════════════════════════════════════════════════════════════════════

_BOT_PATTERNS = [
    re.compile(
        r"^\[?\d{1,2}:\d{2}\s*(?:AM|PM)?\]?\s*"
        r"(?:Datadog|PagerDuty|Jira|GitHub|Bitbucket|Google Calendar|Meet)\s*"
        r"(?:Bot|App).*",
        re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(r"^\[ALERT\].*$", re.MULTILINE),
    re.compile(r"^\[MONITORING\].*$", re.MULTILINE),
]

_MULTI_NEWLINE_RE = re.compile(r"\n{3,}")
_MULTI_SPACE_RE = re.compile(r" {3,}")


def clean_chat_message(text: str) -> str:
    if not text:
        return ""
    for pat in _BOT_PATTERNS:
        text = pat.sub("", text)
    text = _MULTI_NEWLINE_RE.sub("\n\n", text)
    text = _MULTI_SPACE_RE.sub(" ", text)
    return text.strip()


# ═════════════════════════════════════════════════════════════════════
# Database Layer
# ═════════════════════════════════════════════════════════════════════

def _now_iso() -> str:
    return datetime.now(_TZ).isoformat()


def open_db(db_path: str | Path = DB_PATH) -> "SkillDB":
    db_path = Path(db_path)
    if str(db_path) != ":memory:":
        db_path.parent.mkdir(parents=True, exist_ok=True)

    last_err: Exception | None = None
    for attempt in range(_DB_OPEN_RETRIES):
        try:
            conn = sqlite3.connect(str(db_path), timeout=30, check_same_thread=False)
            conn.row_factory = sqlite3.Row
            conn.execute("PRAGMA journal_mode=DELETE")
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
        pk = f"gchat:{resource_id}:{item_id}"
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
                    "SELECT DISTINCT resource_id FROM atomic_content WHERE source=?",
                    (source,),
                ).fetchall()
            else:
                rows = self._conn.execute(
                    "SELECT DISTINCT resource_id FROM atomic_content"
                ).fetchall()
        return [r["resource_id"] for r in rows]

    # ── Change Detection ──

    def conversation_needs_fetch(self, group_id: str, display_ts_ms: int) -> bool:
        if display_ts_ms <= 0:
            return True
        ts_iso = datetime.fromtimestamp(display_ts_ms / 1000, tz=_TZ).isoformat()
        with self._lock:
            latest = self._conn.execute(
                "SELECT MAX(updated_at) as max_ts FROM atomic_content WHERE resource_id=?",
                (group_id,),
            ).fetchone()
        if not latest or not latest["max_ts"]:
            return True
        return ts_iso > latest["max_ts"]

    # ── Mention Type ──

    def compute_mention_type(self, resource_id: str) -> str:
        items = self.get_atomic_for_resource(resource_id)
        if not items:
            return "none"

        if resource_id.startswith("dm/"):
            return "direct"

        for item in items:
            author = (item.get("author") or "").strip()
            if author.lower() == GCHAT_USER_NAME.lower():
                return "direct"

            content = item.get("content") or ""
            if re.search(r"@" + re.escape(GCHAT_USER_NAME), content, re.IGNORECASE):
                return "direct"
            if re.search(r"@michael\b", content, re.IGNORECASE):
                return "direct"

        summary = self.get_resource_summary(resource_id)
        if summary:
            title = (summary.get("title") or "").lower()
            if "michael" in title:
                return "indirect"

        return "none"

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
                       COALESCE(ac_latest.last_updated, rs.summarized_at) AS sort_ts,
                       ac_latest.last_updated
                FROM resource_summary rs
                LEFT JOIN (
                    SELECT resource_id,
                           MAX(cached_at) AS max_cached,
                           MAX(updated_at) AS last_updated
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
                query += " AND COALESCE(ac_latest.last_updated, rs.summarized_at) >= ?"
                params.append(since)
            query += " ORDER BY sort_ts ASC"
            rows = self._conn.execute(query, params).fetchall()
        return [dict(r) for r in rows]

    def delete_atomic_since(self, source: str, since: str) -> int:
        def _do():
            cursor = self._conn.execute(
                "DELETE FROM atomic_content WHERE source=? AND cached_at >= ?",
                (source, since),
            )
            self._conn.commit()
            return cursor.rowcount
        return self._retry(_do)

    def clear_summaries_for_resources(self, resource_ids: list[str]) -> int:
        if not resource_ids:
            return 0
        def _do():
            placeholders = ",".join("?" for _ in resource_ids)
            cursor = self._conn.execute(
                f"UPDATE resource_summary SET summary=NULL, summarized_at=NULL, "
                f"mention_type='none', estimated_relevance=0, final_relevance=0 "
                f"WHERE resource_id IN ({placeholders})",
                resource_ids,
            )
            self._conn.commit()
            return cursor.rowcount
        return self._retry(_do)

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
        "  - direct: DM with user, user authored a message, or @mentioned by name",
        "  - indirect: group chat where user is a participant but not directly addressed",
        "  - none: no personal involvement detected",
        f"Metadata: {meta_json}",
    ]
    if existing_summary:
        parts.append(f"\nExisting summary (update with new content, preserve still-relevant context):\n{existing_summary}")
    parts.append(f"\nContent (chronological):\n{content}")
    parts.append(f"""
Relevance scoring - follow this decision tree step by step:

Step 1: Identify the message source. Is this a human conversation or automated/bot content?
  AUTOMATED/BOT signals: Datadog alerts, PagerDuty, Jira Bot, GitHub Bot, Google Calendar Bot, monitoring notifications, auto-generated summaries, Shopping Cart Notification, notification channels (#dd-, #alert-)
  HUMAN signals: messages composed by people, discussions, questions, decisions, feedback

Step 2: Apply the scoring rules based on source type AND mention_type:
  If mention_type is "none": score 1-4
  If mention_type is "indirect": score 5-7
  If mention_type is "direct" AND AUTOMATED/BOT:
    - ACTION-REQUIRED (alert needing response, access request, task assignment): score 6-7
    - INFORMATIONAL (status updates, monitoring alerts no action needed, daily reports): score 5-6
    - HARD CAP: automated/bot messages in DMs or group chats MUST NOT exceed 7
  If mention_type is "direct" AND HUMAN:
    - Minimum score 7 (human directly engaged with user = always at least medium-high relevance)
    - Use the user's "What Matters Most" to distinguish 7 vs 8 vs 9 vs 10

Step 3: Cross-check against the user's "What Matters Most" priorities.

Summary length: relevance 8-10 = up to 200 words, 5-7 = up to 100 words, 1-4 = up to 30 words (hint: ~{word_hint} words)
Keep all person names, dates, and concrete next actions

Entity extraction rules:
- work_items: Extract Jira ticket IDs (e.g., DPD-715), PR numbers (e.g., PR #649), project codenames (e.g., BCRS, RMN), service names, and git repository names. Empty list if none found.
- people: Extract ONLY explicit person names (e.g., "Nikhil Grover"). Do NOT include group names, team names, or bot names. Empty list if none.
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


def _filter_items_by_context(items: list[dict], ctx_limit: int,
                              title: str, mention_type: str,
                              metadata: Optional[dict]) -> list[dict]:
    """Pick items from newest to oldest that fit within the context budget.

    The budget accounts for the full LLM prompt: system prompt, user prompt
    headers, metadata, and the content block.
    """
    if not items or ctx_limit <= 0:
        return []

    system_prompt = _build_system_prompt()

    meta_json = json.dumps(metadata or {}, indent=2, ensure_ascii=False)

    word_hint = _WORD_HINTS.get(mention_type, 30)
    header = (
        f"Analyze this resource and return a JSON response.\n"
        f"Resource: {title}\n"
        f"Mention Type: {mention_type}\n"
        "  - direct: DM with user, user authored a message, or @mentioned by name\n"
        "  - indirect: group chat where user is a participant but not directly addressed\n"
        "  - none: no personal involvement detected\n"
        f"Metadata: {meta_json}\n\n"
        f"Content (chronological):\n"
    )

    fixed_overhead = len(system_prompt) + len(header)
    available = ctx_limit - fixed_overhead

    filtered = []
    for item in reversed(items):
        author = item.get("author", "Unknown")
        ts = item.get("created_at", "")
        text = item.get("content", "")
        if text:
            item_text = f"[{ts}] {author}: {text}"
        else:
            item_text = f"[{ts}] {author}: (empty)"
        item_size = len(item_text)
        if filtered:
            item_size += 4  # "\n---\n" separator before item
        if available < item_size:
            break
        filtered.append(item)
        available -= item_size

    filtered.reverse()
    return filtered


# ═════════════════════════════════════════════════════════════════════
# Browser & Navigation (CDP)
# ═════════════════════════════════════════════════════════════════════

def connect_browser(cdp_url):
    pw = sync_playwright().start()
    browser = pw.chromium.connect_over_cdp(cdp_url)
    ctx = browser.contexts[0] if browser.contexts else browser.new_context()
    page = next((p for p in ctx.pages if "chat.google.com" in p.url), None)
    if not page:
        page = ctx.new_page()
    else:
        log(f"Reusing tab: {page.url[:80]}")
    return pw, browser, page


def mark_conversation_unread(page) -> bool:
    """Mark the currently-open conversation as unread via the kebab (three-dot) header menu.

    Must be called while the conversation is still open (before go_home).
    The kebab button is in the conversation header bar at the top-right.
    """
    try:
        kebab = page.locator(
            'button[aria-label="More actions"], '
            'button[aria-label="More"], '
            'div[role="button"][aria-label="More actions"], '
            'div[role="button"][aria-label="More"]'
        )
        if kebab.count() == 0:
            return False
        kebab.first.click(timeout=3000)
        time.sleep(0.8)
        menu_items = page.locator(
            "[role='menuitem'], [role='menuitemradio']"
        )
        for i in range(menu_items.count()):
            text = (menu_items.nth(i).text_content() or "").lower().strip()
            if "mark" in text and "unread" in text:
                menu_items.nth(i).click()
                time.sleep(0.3)
                return True
        page.keyboard.press("Escape")
        return False
    except Exception:
        return False


def go_home(page):
    if "/app/home" not in page.url:
        page.goto(GCHAT_URL, wait_until="domcontentloaded", timeout=30000)
    time.sleep(4)
    try:
        page.wait_for_selector(SEL_FEED, timeout=15000)
    except PwTimeout:
        log("WARN: Home feed not loaded within 15s")


def _snapshot_feed_once(page, cutoff_ms):
    return page.evaluate("""({sel, cutoff}) => {
        const feed = [];
        for (const el of document.querySelectorAll(sel)) {
            const ts = parseInt(el.getAttribute("data-display-timestamp") || "0", 10);
            if (cutoff > 0 && ts < cutoff) continue;
            const ne = el.querySelector("div.Vb5pDe");
            let name = "";
            if (ne) for (const n of ne.childNodes) { if (n.nodeType === 3) name += n.textContent; }
            name = name.trim() || el.getAttribute("data-group-id") || "";
            feed.push({
                group_id: el.getAttribute("data-group-id") || "",
                topic_id: el.getAttribute("data-topic-id") || "",
                display_ts: ts,
                name,
                is_unread: el.getAttribute("data-is-unread") === "true",
            });
        }
        return feed;
    }""", {"sel": SEL_FEED, "cutoff": cutoff_ms})


def snapshot_feed(page, cutoff_ms, max_scrolls=30, stable_threshold=5):
    """Progressive feed scanner: scrolls down the left panel to load all items within the cutoff.

    GChat lazily loads feed items - a single scroll may not immediately produce new DOM elements.
    We scroll and wait up to `stable_threshold` consecutive rounds with no new items before stopping.
    """
    seen_keys: set[str] = set()
    feed: list[dict] = []
    stable_rounds = 0

    def _merge():
        items = _snapshot_feed_once(page, cutoff_ms)
        new_count = 0
        for item in items:
            key = f"{item['group_id']}|{item.get('topic_id', '')}|{item['display_ts']}"
            if key not in seen_keys:
                seen_keys.add(key)
                feed.append(item)
                new_count += 1
        return new_count

    _merge()
    debug(f"Feed initial: {len(feed)} items")

    for scroll in range(max_scrolls):
        scroll_feed_down(page)
        new_count = _merge()
        if new_count == 0:
            stable_rounds += 1
            if stable_rounds >= stable_threshold:
                debug(f"Feed scroll {scroll+1}: stable for {stable_threshold} rounds - done ({len(feed)} total)")
                break
        else:
            stable_rounds = 0
            debug(f"Feed scroll {scroll+1}: +{new_count} new ({len(feed)} total)")

    feed.sort(key=lambda x: x["display_ts"], reverse=True)
    return feed


def click_feed_item(page, gid, dts):
    found = page.evaluate("""({sel, gid, dts}) => {
        for (const el of document.querySelectorAll(sel)) {
            if (el.getAttribute("data-group-id") === gid &&
                parseInt(el.getAttribute("data-display-timestamp") || "0", 10) === dts) {
                el.scrollIntoView({block: "center", behavior: "instant"});
                return true;
            }
        }
        return false;
    }""", {"sel": SEL_FEED, "gid": gid, "dts": dts})
    if not found:
        return False
    time.sleep(0.5)
    loc = page.locator(f'{SEL_FEED}[data-group-id="{gid}"]')
    if loc.count() == 0:
        return False
    try:
        target = loc.first
        for i in range(loc.count()):
            if loc.nth(i).get_attribute("data-display-timestamp") == str(dts):
                target = loc.nth(i)
                break
        target.click(timeout=5000)
        time.sleep(2)
        return True
    except Exception as e:
        log(f"  WARN: click failed: {e}")
        return False


def scroll_feed_down(page):
    """Scroll the left feed panel down to trigger lazy-loading of older items."""
    page.evaluate("""() => {
        const items = document.querySelectorAll('span[role="listitem"][data-group-id]');
        if (!items.length) return;
        const last = items[items.length - 1];
        last.scrollIntoView({block: "end", behavior: "instant"});
    }""")
    time.sleep(2)


def left_panel_visible(page):
    try:
        return page.evaluate(f"() => document.querySelectorAll('{SEL_FEED}').length > 0")
    except Exception:
        return False


def get_topic_ids(page):
    try:
        return set(page.evaluate(
            f'() => Array.from(document.querySelectorAll("{SEL_MSG}"))'
            f'  .map(m => m.getAttribute("data-topic-id")).filter(Boolean)'
        ))
    except Exception:
        return set()


def _wait_for_thread(page, topic_id, timeout_s=20):
    sel = f'c-wiz[data-topic-id="{topic_id}"]'
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        time.sleep(2)
        try:
            count = page.evaluate("(s) => document.querySelectorAll(s).length", sel)
            if count > 0:
                return count
        except Exception:
            continue
    return 0


def wait_for_messages(page, old_ids, timeout_s=20, sel=SEL_MSG):
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        time.sleep(2)
        try:
            r = page.evaluate("""(s) => {
                const m = document.querySelectorAll(s);
                return {
                    c: m.length,
                    ids: Array.from(m).slice(0, 5)
                        .map(x => x.getAttribute("data-topic-id")).filter(Boolean),
                };
            }""", sel)
        except Exception:
            continue
        if r["c"] == 0:
            continue
        if not old_ids or not set(r["ids"]).issubset(old_ids):
            return r["c"]
    try:
        return page.evaluate("(s) => document.querySelectorAll(s).length", sel)
    except Exception:
        return 0


def scroll_to_bottom(page, topic_id=""):
    tid_js = json.dumps(topic_id)
    for attempt in range(8):
        jumped = page.evaluate("""() => {
            const btn = document.querySelector(
                "button[aria-label='Jump to bottom'], div[aria-label='Jump to bottom']"
            );
            if (btn && btn.getBoundingClientRect().height > 0) {
                btn.click(); return true;
            }
            return false;
        }""")
        if jumped:
            time.sleep(2)
            continue
        at_bottom = page.evaluate(f"""() => {{
            {FIND_PANEL_JS}
            const panel = findPanel({tid_js});
            if (!panel) return true;
            if (panel.scrollHeight <= panel.clientHeight + 10) return true;
            const wasBottom = panel.scrollTop + panel.clientHeight >= panel.scrollHeight - 20;
            if (!wasBottom) {{
                panel.scrollTop = panel.scrollHeight;
                return false;
            }}
            return true;
        }}""")
        if at_bottom:
            break
        time.sleep(1.5)
    time.sleep(1)


def extract_messages(page, cutoff_ms, topic_id=""):
    sel = f'c-wiz[data-topic-id="{topic_id}"]' if topic_id else SEL_MSG
    return page.evaluate("""({sel, cutoff, isThread}) => {
        const NOISE_CLS = [
            "FvYVyf", "njhDLd", "cPjwNc", "GOoeGd", "Lphf0c",
            "nzVtF", "ZTmjQb", "w692Zc", "TmhmK",
            "ne2Ple-oshW8e-V67aGc",
        ];
        function extractBody(grp) {
            const body = [];
            const quoted = [];
            const w = document.createTreeWalker(grp, NodeFilter.SHOW_TEXT, null, false);
            while (w.nextNode()) {
                const t = w.currentNode.textContent.trim();
                if (!t) continue;
                const p = w.currentNode.parentElement;
                if (!p) continue;
                const cls = p.getAttribute("class") || "";
                const role = p.getAttribute("role") || "";
                if (role === "tooltip" || role === "presentation") continue;
                if (p.closest("button, [role='button']")) continue;
                const rList = p.closest("[role='list']");
                if (rList && /reaction/i.test(rList.getAttribute("aria-label") || "")) continue;
                let skip = false;
                for (const nc of NOISE_CLS) { if (cls.includes(nc)) { skip = true; break; } }
                if (skip) continue;
                if (t.startsWith("press L to")) continue;
                cls.includes("J87oZd") ? quoted.push(t) : body.push(t);
            }
            for (const btn of grp.querySelectorAll("button, [role='button']")) {
                const label = (btn.getAttribute("aria-label") || "").toLowerCase();
                if (label.includes("reaction") || label.includes("reply") ||
                    label.includes("resolve") || label.includes("collapsed") ||
                    label.includes("show more") || label.includes("see more")) continue;
                const t = btn.textContent.trim();
                if (t && t.length > 2 && t.length < 80 && !body.includes(t)) body.push(t);
            }
            let text = body.join("\\n").trim();
            if (quoted.length) text += "\\n[quoted] " + quoted.join("\\n");
            const urls = [];
            for (const a of grp.querySelectorAll("a[href]")) {
                const h = a.getAttribute("href") || "";
                if (h && !h.startsWith("mailto:") && !h.startsWith("javascript:") && !text.includes(h))
                    urls.push(h);
            }
            if (urls.length) text += "\\n[links] " + [...new Set(urls)].join(" ");
            let imgCount = 0;
            for (const img of grp.querySelectorAll("img")) {
                const src = img.getAttribute("src") || "";
                if (src.includes("get_attachment_url") || src.includes("content_type=im"))
                    imgCount++;
            }
            if (imgCount > 0 && !text.trim())
                text = "[" + imgCount + " image" + (imgCount > 1 ? "s" : "") + " attached]";
            else if (imgCount > 0)
                text += "\\n[" + imgCount + " image" + (imgCount > 1 ? "s" : "") + " attached]";
            return text.replace(/\\n{3,}/g, "\\n\\n");
        }
        const out = [];
        if (isThread) {
            const containers = document.querySelectorAll(sel);
            for (const c of containers) {
                if (c.getAttribute("data-is-detailed-thread-view") !== "true") continue;
                for (const grp of c.querySelectorAll("div[role='group']")) {
                    const dataId = grp.getAttribute("data-id") || "";
                    const absEl = grp.querySelector("span[data-absolute-timestamp]");
                    const ms = absEl ? parseInt(absEl.getAttribute("data-absolute-timestamp") || "0", 10) : 0;
                    if (cutoff > 0 && ms > 0 && ms < cutoff) continue;
                    let sender = "";
                    const se = grp.querySelector("span[data-member-id][data-name]");
                    if (se) sender = se.getAttribute("data-name");
                    if (!sender) { const ns = grp.querySelector("span.nzVtF"); if (ns) sender = ns.textContent.trim(); }
                    const te = grp.querySelector("span.FvYVyf");
                    const displayTime = te ? te.textContent.trim() : "";
                    const text = extractBody(grp);
                    if (!text && !sender) continue;
                    out.push({ data_id: dataId, sender: sender || "Unknown", timestamp: displayTime, epoch_ms: ms, body: text });
                }
            }
        } else {
            for (const msg of document.querySelectorAll(sel)) {
                const dataId = msg.getAttribute("data-topic-id") || "";
                const ms = parseInt(msg.getAttribute("data-local-sort-time-msec") || "0", 10);
                if (cutoff > 0 && ms < cutoff) continue;
                let sender = "";
                const se = msg.querySelector("span[data-member-id][data-name]");
                if (se) sender = se.getAttribute("data-name");
                if (!sender) { const ns = msg.querySelector("span.nzVtF"); if (ns) sender = ns.textContent.trim(); }
                const te = msg.querySelector("span.FvYVyf");
                const displayTime = te ? te.textContent.trim() : "";
                const grp = msg.querySelector("div[role='group']");
                const text = grp ? extractBody(grp) : "";
                if (!text && !sender) continue;
                out.push({ data_id: dataId, sender: sender || "Unknown", timestamp: displayTime, epoch_ms: ms, body: text });
            }
        }
        return out;
    }""", {"sel": sel, "cutoff": cutoff_ms, "isThread": bool(topic_id)})


def scroll_and_expand(page, cutoff_ms, max_scrolls, max_expansion,
                      topic_id="", cached_ids=None, early_stop_n=0):
    scroll_count = 0
    expand_count = 0
    collected = {}
    tid_js = json.dumps(topic_id)
    is_thread = bool(topic_id)
    cached_ids = cached_ids or set()
    consecutive_cached = 0

    def _snapshot():
        nonlocal consecutive_cached
        new_found = False
        for msg in extract_messages(page, cutoff_ms, topic_id):
            key = msg.get("data_id") or f"{msg['epoch_ms']}_{msg['sender']}_{hash(msg['body'][:80])}"
            if key not in collected:
                collected[key] = msg
                if cached_ids and key in cached_ids:
                    consecutive_cached += 1
                else:
                    consecutive_cached = 0
                    new_found = True
        return new_found

    _snapshot()

    while True:
        if early_stop_n > 0 and consecutive_cached >= early_stop_n:
            log(f"  Scroll early-stop: {consecutive_cached} consecutive cached messages")
            break
        if is_thread:
            anchor = page.evaluate(f"""() => {{
                const sel = 'c-wiz[data-topic-id="{topic_id}"][data-is-detailed-thread-view="true"]';
                const c = document.querySelector(sel);
                if (!c) return null;
                const grps = c.querySelectorAll("div[role='group']");
                if (!grps.length) return null;
                const absEl = grps[0].querySelector("span[data-absolute-timestamp]");
                const ts = absEl ? parseInt(absEl.getAttribute("data-absolute-timestamp") || "0", 10) : 0;
                return {{ts: ts, grpCount: grps.length}};
            }}""")
        else:
            anchor = page.evaluate("""(s) => {
                const m = document.querySelectorAll(s);
                if (!m.length) return null;
                return {
                    ts: parseInt(m[0].getAttribute("data-local-sort-time-msec") || "0", 10),
                    tid: m[0].getAttribute("data-topic-id") || "",
                };
            }""", SEL_MSG)

        if not anchor:
            break
        if anchor["ts"] > 0 and anchor["ts"] <= cutoff_ms:
            log(f"  Reached cutoff after {scroll_count} scroll(s)")
            break

        if expand_count < max_expansion:
            bar = _find_one_expandable(page, topic_id)
            if bar:
                if is_thread:
                    before = anchor.get("grpCount", 0)
                else:
                    before = page.evaluate("(s) => document.querySelectorAll(s).length", SEL_MSG)
                try:
                    page.mouse.click(bar["x"], bar["y"])
                    expand_count += 1
                except Exception:
                    pass
                if is_thread:
                    sel_grp = f'c-wiz[data-topic-id="{topic_id}"][data-is-detailed-thread-view="true"] div[role="group"]'
                    _wait_for_dom_change(page, before, sel_grp)
                else:
                    _wait_for_dom_change(page, before, SEL_MSG)
                    if anchor.get("tid"):
                        _scroll_to_anchor(page, anchor["tid"])
                _snapshot()
                continue

        if scroll_count >= max_scrolls:
            log(f"  Hit scroll limit ({max_scrolls})")
            break

        moved = page.evaluate(f"""() => {{
            {FIND_PANEL_JS}
            const panel = findPanel({tid_js});
            if (!panel) return false;
            const before = panel.scrollTop;
            panel.scrollTop = Math.max(0, panel.scrollTop - 800);
            return panel.scrollTop !== before;
        }}""")

        if not moved:
            log(f"  Reached top after {scroll_count} scroll(s)")
            break

        scroll_count += 1
        time.sleep(1)
        _snapshot()

    if expand_count:
        log(f"  Expanded {expand_count} bar(s)")
    return sorted(collected.values(), key=lambda m: m["epoch_ms"])


def _wait_for_dom_change(page, before_count, sel=SEL_MSG, timeout=5):
    deadline = time.time() + timeout
    while time.time() < deadline:
        time.sleep(0.5)
        after = page.evaluate("(s) => document.querySelectorAll(s).length", sel)
        if after != before_count:
            return
    time.sleep(1)


def _scroll_to_anchor(page, topic_id):
    page.evaluate(f"""() => {{
        const el = document.querySelector('c-wiz[data-topic-id="{topic_id}"]');
        if (el) el.scrollIntoView({{block: "center", behavior: "instant"}});
    }}""")
    time.sleep(0.5)


def _find_one_expandable(page, topic_id=""):
    tid_js = json.dumps(topic_id)
    return page.evaluate(f"""() => {{
        {FIND_PANEL_JS}
        const panel = findPanel({tid_js});
        if (!panel) return null;
        for (const bar of panel.querySelectorAll(
            "[role='button'][aria-label*='collapsed message']"
        )) {{
            const rect = bar.getBoundingClientRect();
            if (rect.width < 20 || rect.height < 5) continue;
            bar.scrollIntoView({{block: "center", behavior: "instant"}});
            const r2 = bar.getBoundingClientRect();
            return {{
                x: Math.round(r2.left + r2.width / 2),
                y: Math.round(r2.top + r2.height / 2),
                label: bar.getAttribute("aria-label") || "",
            }};
        }}
        for (const btn of panel.querySelectorAll(
            "button, [role='button'], span[role='button']"
        )) {{
            const t = btn.textContent.trim().toLowerCase();
            if (!t.includes("show more") && !t.includes("see more")) continue;
            btn.scrollIntoView({{block: "center", behavior: "instant"}});
            const r = btn.getBoundingClientRect();
            if (r.width < 10 || r.height < 5) continue;
            return {{
                x: Math.round(r.left + r.width / 2),
                y: Math.round(r.top + r.height / 2),
                label: t,
            }};
        }}
        return null;
    }}""")


# ═════════════════════════════════════════════════════════════════════
# Caching & Summarization Pipeline
# ═════════════════════════════════════════════════════════════════════

def make_resource_id(group_id: str, topic_id: str = "") -> str:
    if topic_id:
        return f"{group_id}/{topic_id}"
    return group_id


def cache_conversation(db: SkillDB, resource_id: str, name: str,
                       messages: list[dict]) -> int:
    new_count = 0
    for msg in messages:
        data_id = msg.get("data_id") or f"{msg['epoch_ms']}_{hash(msg.get('sender', ''))}"
        body = clean_chat_message(msg.get("body", ""))
        author = msg.get("sender", "Unknown")
        epoch_ms = msg.get("epoch_ms", 0)
        ts_iso = datetime.fromtimestamp(epoch_ms / 1000, tz=_TZ).isoformat() if epoch_ms else ""

        meta = {"timestamp_display": msg.get("timestamp", "")}

        if db.upsert_atomic(
            "gchat", resource_id, data_id,
            author=author, content=body,
            created_at=ts_iso, updated_at=ts_iso,
            metadata=meta,
        ):
            new_count += 1

    return new_count


def _summarize_one(db: SkillDB, resource_id: str, convo_info: dict,
                   force: bool = False, current: int = 0, total: int = 0,
                   ctx_limit: int = _DEFAULT_CTX_LIMIT) -> None:
    name = convo_info.get("name", resource_id)

    if not force and not db.needs_resummarize(resource_id):
        existing = db.get_resource_summary(resource_id)
        if existing and existing.get("summary"):
            log(f"[{current}/{total}] {resource_id}: cached (rel={existing.get('final_relevance', '?')})")
            return

    existing_summary = db.get_resource_summary(resource_id)
    existing_text = existing_summary["summary"] if existing_summary else None
    summarized_at = existing_summary.get("summarized_at") if existing_summary else None

    if existing_text and summarized_at:
        items = db.get_items_since(resource_id, summarized_at)
        if not items:
            items = db.get_atomic_for_resource(resource_id)
    else:
        items = db.get_atomic_for_resource(resource_id)

    if not items:
        return

    mention_type = db.compute_mention_type(resource_id)
    all_items = db.get_atomic_for_resource(resource_id)
    meta = {"message_count": len(all_items), "url": convo_info.get("url", "")}

    items = _filter_items_by_context(items, ctx_limit, name, mention_type, meta)
    if not items:
        log(f"SKIP [{current}/{total}] {resource_id}: no items fit within context limit")
        return

    log(f"Summarizing [{current}/{total}] {name[:50]} ({len(items)} msgs, {mention_type}, ctx={ctx_limit})")

    result = summarize_resource(
        title=name, source_type="Google Chat conversation", atomic_items=items,
        metadata=meta, existing_summary=existing_text, mention_type=mention_type,
    )

    if not result.summary:
        raise RuntimeError(f"Empty summary for {resource_id}")

    enriched_meta = dict(meta)
    enriched_meta["work_items"] = result.work_items
    enriched_meta["people"] = result.people
    enriched_meta["labels"] = result.labels

    db.upsert_summary(
        resource_id, "gchat", name, result.summary, enriched_meta,
        mention_type=mention_type,
        estimated_relevance=result.relevance,
        final_relevance=result.relevance,
    )
    log(f"Done [{current}/{total}] {resource_id} rel={result.relevance}")


def _summarize_worker(q: "_queue.Queue", db: SkillDB, force: bool, errors: list,
                      ctx_limit: int = _DEFAULT_CTX_LIMIT) -> None:
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        resource_id, convo_info, current, total = item
        try:
            _summarize_one(db, resource_id, convo_info, force, current, total, ctx_limit=ctx_limit)
        except Exception as exc:
            log(f"ERROR summarizing {resource_id}: {exc}")
            errors.append(f"{resource_id}: {exc}")
        finally:
            q.task_done()


class _Pipeline:
    def __init__(self, db: SkillDB, force: bool, ctx_limit: int = _DEFAULT_CTX_LIMIT):
        self._q: _queue.Queue = _queue.Queue()
        self._errors: list = []
        self._counter = 0
        self._total = 0
        self._ctx_limit = ctx_limit
        self._thread = threading.Thread(
            target=_summarize_worker, args=(self._q, db, force, self._errors, ctx_limit), daemon=True
        )
        self._thread.start()

    def set_total(self, total: int) -> None:
        self._total = total

    def put(self, resource_id: str, convo_info: dict) -> None:
        self._counter += 1
        self._q.put((resource_id, convo_info, self._counter, self._total))

    def finish(self) -> list[str]:
        self._q.put(None)
        self._thread.join()
        return self._errors


# ═════════════════════════════════════════════════════════════════════
# Output Formatting
# ═════════════════════════════════════════════════════════════════════

def _format_summary_block(s: dict, idx: int, total: int) -> str:
    meta = json.loads(s.get("metadata", "{}"))
    title = s.get("title", "(unknown)")
    parts = ["Source: gchat", f"Group: {s['resource_id']}"]

    rel = s.get("final_relevance", s.get("estimated_relevance", 0))
    mt = s.get("mention_type", "none")
    if rel:
        parts.append(f"Relevance: {rel}/10")
    if mt and mt != "none":
        parts.append(f"Mention: {mt}")

    last_updated = s.get("last_updated")
    if last_updated:
        parts.append(f"Updated: {last_updated}")

    if meta.get("work_items"):
        parts.append(f"Work Items: {', '.join(meta['work_items'])}")
    if meta.get("people"):
        parts.append(f"People: {', '.join(meta['people'])}")

    labels = meta.get("labels", [])
    if labels:
        parts.append(f"Labels: {', '.join(labels)}")

    header = f"[{idx}/{total}] {title}"
    return f"\n\n## {header}\n{' | '.join(parts)}\n{s.get('summary', '')}"


def write_output(db: SkillDB, output_path: Path, min_relevance: int = 7,
                 since: Optional[str] = None) -> None:
    summaries = db.get_all_summaries(source="gchat", min_relevance=min_relevance, since=since)
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
    ap = argparse.ArgumentParser(
        description="GChat Skill - fetch, cache, and summarize Google Chat conversations"
    )
    ap.add_argument("--cdp-url", default=DEFAULT_CDP,
                    help=f"CDP endpoint (default: {DEFAULT_CDP})")
    ap.add_argument("--days", type=int, default=None,
                    help="Lookback days (default: 3 Wed-Sat, 4 Sun, 5 Mon-Tue)")
    ap.add_argument("--max-threads", type=int, default=200,
                    help="Max conversations to process (default: 200)")
    ap.add_argument("--max-scan", type=int, default=500,
                    help="Max feed items to scan (default: 500)")
    ap.add_argument("--max-scroll", type=int, default=5,
                    help="Max scroll-up iterations per thread (default: 5)")
    ap.add_argument("--max-expansion", type=int, default=5,
                    help="Max expansion rounds for collapsed messages (default: 5)")
    ap.add_argument("--early-stop", type=int, default=3,
                    help="Stop after N consecutive unchanged conversations (0=disabled, default: 3)")
    ap.add_argument("--focus-title", default="",
                    help="Only process conversations matching this title (case-insensitive)")
    ap.add_argument("--force", action="store_true",
                    help="Clear summaries and re-summarize (keeps cached content)")
    ap.add_argument("--cached-only", action="store_true",
                    help="Output cached summaries from DB without browser (fast, for reports)")
    ap.add_argument("--min-relevance", type=int, default=7,
                    help="Minimum relevance for output (default: 7)")
    ap.add_argument("--refetch-since", default=None,
                    help="Delete cached content since YYYY-MM-DD and re-fetch")
    ap.add_argument("--output", default=str(_WORKDIR / "gchat-output.md"),
                    help="Write results to this file (default: workdir/gchat-output.md)")
    ap.add_argument("--debug-dom", action="store_true",
                    help="Dump Home feed DOM to stderr and exit")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO"],
                    help="Log level (default: INFO)")
    ap.add_argument("--llm-context-limit", type=int, default=_DEFAULT_CTX_LIMIT,
                    help=f"Max characters for LLM context budget (default: {_DEFAULT_CTX_LIMIT})")
    args = ap.parse_args()

    global _LOG_LEVEL
    _LOG_LEVEL = args.log_level.upper()

    output_path = Path(args.output)
    days = args.days if args.days is not None else _default_lookback_days()
    since_dt = datetime.now(_TZ) - timedelta(days=days)
    since_iso = since_dt.strftime("%Y-%m-%d")

    cutoff_ms = int(since_dt.timestamp() * 1000)

    if output_path.exists():
        output_path.unlink()

    db = open_db()
    log(f"STARTED (days={days}, since={since_iso}, user={GCHAT_USER_NAME})")

    if args.refetch_since:
        try:
            refetch_dt = datetime.strptime(args.refetch_since, "%Y-%m-%d").replace(tzinfo=_TZ)
            refetch_iso = refetch_dt.isoformat()
            affected = db.get_all_resource_ids(source="gchat")
            deleted = db.delete_atomic_since("gchat", refetch_iso)
            cleared = db.clear_summaries_for_resources(affected)
            log(f"--refetch-since {args.refetch_since}: deleted {deleted} cached messages, "
                f"cleared {cleared} summaries")
        except ValueError:
            log(f"ERROR: invalid date format for --refetch-since: {args.refetch_since}")
            sys.exit(1)

    if args.force:
        count = db.clear_all_summaries()
        log(f"--force: cleared {count} summaries (cached content preserved)")

    pw = browser = None

    try:
        if args.cached_only:
            write_output(db, output_path, min_relevance=args.min_relevance, since=since_iso)
            log("COMPLETED (cached-only)")
            return

        if args.force:
            resource_ids = db.get_all_resource_ids(source="gchat")
            log(f"--force: re-summarizing {len(resource_ids)} cached conversations (no browser)")
            pipeline = _Pipeline(db, force=True, ctx_limit=args.llm_context_limit)
            pipeline.set_total(len(resource_ids))
            for rid in resource_ids:
                existing = db.get_resource_summary(rid)
                info = {"name": existing["title"] if existing else rid}
                pipeline.put(rid, info)
            errors = pipeline.finish()
            if errors:
                log(f"COMPLETED WITH ERRORS ({len(resource_ids)} conversations, {len(errors)} error(s))")
                for e in errors:
                    log(f"  ERROR: {e}")
                sys.exit(1)
            write_output(db, output_path, min_relevance=args.min_relevance, since=since_iso)
            log(f"COMPLETED --force ({len(resource_ids)} conversations)")
            return

        # ── Phase 1: Scan feed ──
        log(f"Connecting to browser at {args.cdp_url}...")
        pw, browser, page = connect_browser(args.cdp_url)

        go_home(page)

        if args.debug_dom:
            items = page.evaluate(f"""() => {{
                return Array.from(document.querySelectorAll('{SEL_FEED}')).slice(0, 10).map(el => ({{
                    gid: el.getAttribute("data-group-id"),
                    ts: el.getAttribute("data-display-timestamp"),
                    unread: el.getAttribute("data-is-unread"),
                    text: el.textContent.trim().substring(0, 150),
                }}));
            }}""")
            log(f"Feed items: {len(items)}")
            for it in items:
                log(f"  [{it['gid'][:30]}] ts={it['ts']} unread={it['unread']} {it['text'][:80]}")
            sys.exit(0)

        feed = snapshot_feed(page, cutoff_ms)
        log(f"Feed: {len(feed)} item(s) within {days} day(s)")
        if not feed:
            log("FATAL: 0 feed items - run --debug-dom to inspect.")
            sys.exit(2)

        convo_infos: list[dict] = []
        threads_to_fetch: list[dict] = []
        seen_ids: set[str] = set()
        scanned = 0
        skipped_focus = 0
        skipped_unchanged = 0
        consecutive_cached = 0
        early_stop_triggered = False
        limit = min(len(feed), args.max_scan)

        for i in range(limit):
            if len(convo_infos) >= args.max_threads:
                break

            gid = feed[i]["group_id"]
            dts = feed[i]["display_ts"]
            tid = feed[i].get("topic_id", "")
            name = feed[i]["name"]
            rid = make_resource_id(gid, tid)
            scanned += 1

            if rid in seen_ids:
                continue
            seen_ids.add(rid)

            is_focused = not args.focus_title or args.focus_title.lower() in name.lower()
            if not is_focused:
                skipped_focus += 1
                continue

            info = {
                "resource_id": rid, "name": name, "display_ts": dts,
                "url": f"https://chat.google.com/{gid}", "fetched": False,
                "group_id": gid, "topic_id": tid,
                "is_unread": feed[i].get("is_unread", False),
            }

            if early_stop_triggered or (
                not args.force and not db.conversation_needs_fetch(rid, dts)
            ):
                convo_infos.append(info)
                skipped_unchanged += 1
                if not early_stop_triggered:
                    consecutive_cached += 1
                    if args.early_stop > 0 and consecutive_cached >= args.early_stop:
                        log(f"  Early stop: {consecutive_cached} consecutive cached")
                        early_stop_triggered = True
                continue

            consecutive_cached = 0
            convo_infos.append(info)
            threads_to_fetch.append(info)

        unread_count = sum(1 for t in threads_to_fetch if t.get("is_unread"))
        log(f"Phase 1: {len(convo_infos)} conversations (focus-skip={skipped_focus}, "
            f"unchanged={skipped_unchanged}, to-fetch={len(threads_to_fetch)}, "
            f"unread={unread_count})")

        # ── Phase 2+3: Fetch and summarize in pipeline ──
        pipeline = _Pipeline(db, force=False, ctx_limit=args.llm_context_limit)
        pipeline.set_total(len(convo_infos))
        fetched_ids: set[str] = set()

        for idx, info in enumerate(threads_to_fetch, 1):
            rid = info["resource_id"]
            gid = info["group_id"]
            dts = info["display_ts"]
            tid = info.get("topic_id", "")
            name = info["name"]

            log(f"[Fetching {idx}/{len(threads_to_fetch)}] {name[:55]}")

            old_ids = get_topic_ids(page) if not tid else set()

            if not click_feed_item(page, gid, dts):
                scroll_feed_down(page)
                time.sleep(1)
                if not click_feed_item(page, gid, dts):
                    log("  SKIP: item not found in DOM")
                    continue

            time.sleep(1)
            if not left_panel_visible(page):
                log("  WARN: mid panel gone - returning to Home")
                go_home(page)
                continue

            if tid:
                msg_count = _wait_for_thread(page, tid)
            else:
                msg_count = wait_for_messages(page, old_ids)
            if msg_count == 0:
                log("  SKIP: 0 messages loaded")
                go_home(page)
                continue

            scroll_to_bottom(page, topic_id=tid)
            cached_ids = db.get_cached_message_ids(rid)
            messages = scroll_and_expand(
                page, cutoff_ms, args.max_scroll, args.max_expansion,
                topic_id=tid, cached_ids=cached_ids,
                early_stop_n=args.early_stop,
            )
            log(f"  -> {len(messages)} message(s)")

            if messages:
                new_count = cache_conversation(db, rid, name, messages)
                if new_count > 0:
                    log(f"  -> {new_count} new cached")
                info["fetched"] = True
                fetched_ids.add(rid)

            if info.get("is_unread", False):
                if mark_conversation_unread(page):
                    log("  -> restored unread status")
                else:
                    log("  WARN: could not restore unread status")

            if "/app/home" not in page.url:
                go_home(page)

            pipeline.put(rid, info)

        log(f"Phase 2: fetched {len(fetched_ids)}/{len(threads_to_fetch)} conversations")

        for info in convo_infos:
            if info["resource_id"] not in fetched_ids:
                pipeline.put(info["resource_id"], info)

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
        pw = browser = None

        if errors:
            log(f"COMPLETED WITH ERRORS ({len(convo_infos)} conversations, {len(errors)} error(s))")
            for e in errors:
                log(f"  ERROR: {e}")
            sys.exit(1)

        write_output(db, output_path, min_relevance=args.min_relevance, since=since_iso)
        log(f"COMPLETED ({len(convo_infos)} conversations, fetched={len(fetched_ids)})")

    except SystemExit:
        raise
    except Exception as e:
        log(f"FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        db.close()
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


if __name__ == "__main__":
    main()
