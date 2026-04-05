#!/usr/bin/env python3
"""
Jira Skill - Fetch, cache, and AI-summarize Jira tickets.

Single-file skill that:
1. Fetches tickets from saved filter, Polaris view, and/or raw JQL
2. Caches atomic content in SQLite with incremental change detection
3. Summarizes via LLM with relevance scoring, entity extraction, and JSON output
4. Writes final output .md only after all summaries succeed

Usage:
  python jira.py                                  # defaults: filter + view
  python jira.py --jql "project = DPD"
  python jira.py --filter-id 13811 --view-id 10489904
  python jira.py --cached-only                    # output from DB, no API
  python jira.py --force                          # re-fetch and re-summarize all
"""

import argparse
import base64
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

# ═════════════════════════════════════════════════════════════════════
# Configuration
# ═════════════════════════════════════════════════════════════════════

JIRA_BASE = "https://ntuclink.atlassian.net"
SEARCH_URL = f"{JIRA_BASE}/rest/api/3/search/jql"
FILTER_URL = f"{JIRA_BASE}/rest/api/3/filter"
GRAPHQL_URL = f"{JIRA_BASE}/gateway/api/graphql"
CLOUD_ID = "faa50733-0f7b-4288-901e-5e0e16334984"

DEFAULT_FIELDS = (
    "summary,description,status,parent,issuelinks,created,updated,comment,"
    "subtasks,assignee,priority,labels,duedate,reporter,issuetype,resolution,"
    "components,fixVersions"
)

_DEFAULT_FILTER_ID = os.environ.get("JIRA_DEFAULT_FILTER_ID", "13811")
_DEFAULT_VIEW_ID = os.environ.get("JIRA_DEFAULT_VIEW_ID", "10489904")

LITELLM_BASE = os.environ.get("LITELLM_BASE_URL", "https://llm.gigary.com/v1")
SUMMARIZE_MODEL = os.environ.get("SUMMARIZE_MODEL", "local/qwen3.5-35b-a3b:instruct-reasoning")
LITELLM_API_KEY = os.environ.get("API_KEY_OTHER", os.environ.get("LLAMA_TOKEN", ""))
SUMMARIZE_RETRIES = int(os.environ.get("SUMMARIZE_RETRIES", "3"))
SUMMARIZE_RETRY_INITIAL_SEC = float(os.environ.get("SUMMARIZE_RETRY_INITIAL_SEC", "30"))

_WORKDIR = Path(__file__).resolve().parents[3] / "workdir"
_DEFAULT_DB_PATH = Path(__file__).resolve().parent.parent / "data" / "jira_cache.db"
DB_PATH = Path(os.environ.get("JIRA_DB_PATH", str(_DEFAULT_DB_PATH)))
_USER_MD_PATH = Path(__file__).resolve().parents[3] / "User.md"

_TZ = ZoneInfo(os.environ.get("TZ", "Asia/Singapore"))

VIEW_CACHE_FILE = Path.home() / ".cache" / "jira_view_jql.json"
VIEW_CACHE_TTL = 86400

_RELEVANCE_FLOORS = {"direct": 7, "indirect": 5, "none": 1}
_WORD_HINTS = {"direct": 200, "indirect": 100, "none": 30}

_DB_OPEN_RETRIES = 3
_DB_RETRY_DELAY_S = 2


def _default_lookback_days() -> int:
    """Default 14-day lookback window for Jira tickets."""
    return 14


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
_TECHNICAL_DUMP_PATTERNS = [
    re.compile(r"(?:^|\n)(?:PORT\s+STATE.*\n(?:.*\n){3,50})", re.MULTILINE),
    re.compile(r"(?:^|\n)\$\s+(?:nmap|sslscan|curl|gsutil|gcloud)\s.*?(?=\n\$|\n\n\n|\Z)", re.DOTALL),
    re.compile(r"\{[^{}]*\"__metadata\"[^{}]*\{[^{}]*\}[^{}]*\}", re.DOTALL),
    re.compile(r"\{[^{}]*\"uri\":\s*\"http[^\"]+/sap/[^{}]+\}", re.DOTALL),
]


def clean_jira_text(text: str) -> str:
    if not text:
        return ""
    for pat in _TECHNICAL_DUMP_PATTERNS:
        text = pat.sub("\n[...technical output removed...]\n", text)
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
    _USER_NAME = "Michael Bui"
    _USER_EMAIL = "michael.bui@fairpricegroup.sg"

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

            CREATE TABLE IF NOT EXISTS ticket_relationships (
                source_key    TEXT NOT NULL,
                target_key    TEXT NOT NULL,
                relation_type TEXT NOT NULL,
                cached_at     TEXT NOT NULL,
                PRIMARY KEY (source_key, target_key, relation_type)
            );
            CREATE INDEX IF NOT EXISTS idx_rel_source
                ON ticket_relationships(source_key);
            CREATE INDEX IF NOT EXISTS idx_rel_target
                ON ticket_relationships(target_key);
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
                "SELECT updated_at FROM atomic_content WHERE id = ?", (pk,)
            ).fetchone()
            if existing:
                if existing["updated_at"] == updated_at:
                    return False
                self._conn.execute(
                    """UPDATE atomic_content SET author=?, content=?, created_at=?,
                       updated_at=?, cached_at=?, metadata=? WHERE id=?""",
                    (author, content, created_at, updated_at, _now_iso(), meta_json, pk),
                )
            else:
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

    def get_atomic_for_resource(self, resource_id: str) -> list[dict]:
        with self._lock:
            rows = self._conn.execute(
                "SELECT * FROM atomic_content WHERE resource_id=? ORDER BY created_at ASC",
                (resource_id,),
            ).fetchall()
        return [dict(r) for r in rows]

    def get_latest_updated_at(self, resource_id: str) -> Optional[str]:
        with self._lock:
            row = self._conn.execute(
                "SELECT MAX(updated_at) as max_ts FROM atomic_content WHERE resource_id=?",
                (resource_id,),
            ).fetchone()
        return row["max_ts"] if row else None

    def has_content_changed(self, resource_id: str, new_updated_at: str) -> bool:
        cached_ts = self.get_latest_updated_at(resource_id)
        if cached_ts is None:
            return True
        return new_updated_at > cached_ts

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

    # ── Resource Summary ──

    def get_resource_summary(self, resource_id: str) -> Optional[dict]:
        with self._lock:
            row = self._conn.execute(
                "SELECT * FROM resource_summary WHERE resource_id=?", (resource_id,)
            ).fetchone()
        return dict(row) if row else None

    def needs_resummarize(self, resource_id: str) -> bool:
        existing = self.get_resource_summary(resource_id)
        if not existing or not existing.get("summarized_at"):
            return True
        latest = self.get_latest_updated_at(resource_id)
        return bool(latest and latest > existing["summarized_at"])

    def get_items_since(self, resource_id: str, since: str) -> list[dict]:
        with self._lock:
            rows = self._conn.execute(
                "SELECT * FROM atomic_content WHERE resource_id=? AND updated_at > ? ORDER BY created_at ASC",
                (resource_id, since),
            ).fetchall()
        return [dict(r) for r in rows]

    def compute_mention_type(self, resource_id: str) -> str:
        user_lower = self._USER_NAME.lower()
        with self._lock:
            items = self._conn.execute(
                "SELECT author, content, metadata FROM atomic_content WHERE resource_id=?",
                (resource_id,),
            ).fetchall()
        strongest = "none"
        for item in items:
            author = (item["author"] or "").lower()
            content = (item["content"] or "").lower()
            meta = json.loads(item["metadata"] or "{}")
            assignee = (meta.get("assignee") or "").lower()
            reporter = (meta.get("reporter") or "").lower()
            if user_lower in assignee or user_lower in reporter:
                return "direct"
            if user_lower in author:
                return "direct"
            if f"@{user_lower}" in content or user_lower in content:
                return "direct"
            if strongest == "none" and meta.get("linked_issues"):
                strongest = "indirect"
        return strongest

    def upsert_summary(self, resource_id: str, source: str, title: str,
                       summary: str, metadata: Optional[dict] = None,
                       mention_type: Optional[str] = None,
                       estimated_relevance: int = 0,
                       final_relevance: Optional[int] = None) -> None:
        def _do():
            meta_json = json.dumps(metadata or {}, separators=(",", ":"), ensure_ascii=False)
            mt = mention_type or "none"
            fr = final_relevance if final_relevance is not None else estimated_relevance
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
                 mt, estimated_relevance, fr),
            )
            self._conn.commit()
        self._retry(_do)

    def get_all_summaries(self, source: Optional[str] = None,
                          min_relevance: Optional[int] = None,
                          since: Optional[str] = None) -> list[dict]:
        with self._lock:
            conditions, params = [], []
            if source:
                conditions.append("rs.source=?")
                params.append(source)
            if min_relevance is not None:
                conditions.append("rs.final_relevance >= ?")
                params.append(min_relevance)
            if since:
                conditions.append("COALESCE(ac_latest.max_updated, rs.summarized_at) >= ?")
                params.append(since)
            where = f" WHERE {' AND '.join(conditions)}" if conditions else ""
            rows = self._conn.execute(
                f"""SELECT rs.*, COALESCE(ac_latest.max_updated, rs.summarized_at) AS sort_ts
                    FROM resource_summary rs
                    LEFT JOIN (
                        SELECT resource_id, MAX(updated_at) AS max_updated
                        FROM atomic_content GROUP BY resource_id
                    ) ac_latest ON rs.resource_id = ac_latest.resource_id
                    {where}
                    ORDER BY sort_ts DESC""",
                params,
            ).fetchall()
        return [dict(r) for r in rows]

    def backfill_mention_types(self) -> dict[str, int]:
        counts: dict[str, int] = {"direct": 0, "indirect": 0, "none": 0}
        for rid in self.get_all_resource_ids():
            mt = self.compute_mention_type(rid)
            counts[mt] = counts.get(mt, 0) + 1
            def _update(rid=rid, mt=mt):
                self._conn.execute(
                    "UPDATE resource_summary SET mention_type=? WHERE resource_id=?", (mt, rid)
                )
                self._conn.commit()
            self._retry(_update)
        return counts

    def clear_all_summaries(self) -> int:
        def _do():
            cur = self._conn.execute(
                "UPDATE resource_summary SET summary=NULL, estimated_relevance=0, final_relevance=0, summarized_at=NULL"
            )
            self._conn.commit()
            return cur.rowcount
        return self._retry(_do)

    # ── Ticket Relationships ──

    def upsert_relationship(self, source_key: str, target_key: str, relation_type: str) -> None:
        def _do():
            self._conn.execute(
                """INSERT INTO ticket_relationships (source_key, target_key, relation_type, cached_at)
                   VALUES (?,?,?,?) ON CONFLICT(source_key, target_key, relation_type)
                   DO UPDATE SET cached_at=excluded.cached_at""",
                (source_key, target_key, relation_type, _now_iso()),
            )
            self._conn.commit()
        self._retry(_do)

    def get_relationships(self, ticket_key: str) -> list[dict]:
        with self._lock:
            rows = self._conn.execute(
                "SELECT * FROM ticket_relationships WHERE source_key=? OR target_key=? ORDER BY relation_type",
                (ticket_key, ticket_key),
            ).fetchall()
        return [dict(r) for r in rows]

    def clear_relationships(self, ticket_key: str) -> None:
        def _do():
            self._conn.execute("DELETE FROM ticket_relationships WHERE source_key=?", (ticket_key,))
            self._conn.commit()
        self._retry(_do)

    def delete_resource(self, resource_id: str) -> None:
        def _do():
            self._conn.execute("DELETE FROM atomic_content WHERE resource_id=?", (resource_id,))
            self._conn.execute("DELETE FROM resource_summary WHERE resource_id=?", (resource_id,))
            self._conn.execute(
                "DELETE FROM ticket_relationships WHERE source_key=? OR target_key=?",
                (resource_id, resource_id),
            )
            self._conn.commit()
        self._retry(_do)

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
        "  - direct: user is explicitly addressed, assigned, tagged, or has actively participated/replied",
        "  - indirect: user is in recipient/participant list but not directly addressed",
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
- Keep all person names, ticket IDs, dates, and concrete next actions

Entity extraction rules:
- work_items: Extract Jira ticket IDs (e.g., DPD-715, OMNI-1191), PR numbers (e.g., PR #649), project codenames (e.g., BCRS, RMN, BLIGHT), service names (e.g., lt-strudel-api, offer-service), and git repository names. Empty list if none found.
- people: Extract ONLY explicit person names (e.g., "Nikhil Grover", "Alvin Choo"). Do NOT include group names, team names, or distribution lists. Empty list if none.
- labels: Generate exactly 5 descriptive 2-word labels (lowercase, hyphenated) that best characterize this resource's topic and activity. Prefer domain-specific terms over generic ones.

Return ONLY valid JSON:
{{"relevance": <integer 1-10>, "summary": "<your summary>", "work_items": ["<id1>", "<id2>"], "people": ["<person1>", "<person2>"], "labels": ["<word-word>", "<word-word>", "<word-word>", "<word-word>", "<word-word>"]}}""")
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
        return SummaryResult(
            relevance=_RELEVANCE_FLOORS.get(mention_type, 1),
            summary=existing_summary or "",
        )
    content_parts = []
    for item in atomic_items:
        author = item.get("author", "Unknown")
        ts = item.get("created_at", "")
        text = item.get("content", "")
        if text:
            content_parts.append(f"[{ts}] {author}: {text}")

    raw = _call_llm(
        _build_system_prompt(),
        _build_user_prompt(
            title, source_type,
            json.dumps(metadata or {}, indent=2, ensure_ascii=False),
            "\n---\n".join(content_parts),
            mention_type, existing_summary,
        ),
    )
    return parse_llm_response(raw, mention_type)


# ═════════════════════════════════════════════════════════════════════
# Jira API Layer
# ═════════════════════════════════════════════════════════════════════

def validate_env() -> tuple[str, str]:
    email = os.environ.get("JIRA_EMAIL")
    api_key = os.environ.get("JIRA_API_KEY")
    if not email or not api_key:
        log("ERROR: Missing JIRA_EMAIL or JIRA_API_KEY")
        sys.exit(1)
    log(f"Auth: {email}")
    return email, api_key


def get_auth_header(email: str, api_key: str) -> dict:
    token = base64.b64encode(f"{email}:{api_key}".encode()).decode()
    return {"Authorization": f"Basic {token}"}


def _request(method: str, url: str, retries: int = 3, **kwargs) -> requests.Response:
    for attempt in range(1, retries + 1):
        try:
            resp = requests.request(method, url, timeout=30, **kwargs)
            if resp.status_code == 401:
                log("ERROR: Authentication failed")
                sys.exit(1)
            if resp.status_code == 404:
                log(f"ERROR: Not found: {url}")
                sys.exit(1)
            return resp
        except requests.exceptions.Timeout:
            if attempt < retries:
                time.sleep(2 ** attempt)
            else:
                log("ERROR: All retries timed out")
                sys.exit(1)
        except requests.exceptions.ConnectionError as e:
            log(f"ERROR: Connection error: {e}")
            sys.exit(1)
    sys.exit(1)  # unreachable


# ── ADF Parsing ──

def adf_to_text(node) -> str:
    if node is None:
        return ""
    if isinstance(node, str):
        return node
    if isinstance(node, dict):
        ntype = node.get("type", "")
        if ntype == "text":
            return node.get("text", "")
        if ntype == "hardBreak":
            return "\n"
        text = "".join(adf_to_text(c) for c in node.get("content", []))
        if ntype in ("paragraph", "heading", "bulletList", "orderedList", "listItem", "blockquote"):
            return text + "\n"
        return text
    if isinstance(node, list):
        return "".join(adf_to_text(c) for c in node)
    return ""


# ── Issue Fetching & Formatting ──

def fetch_issues(jql: str, limit: int, offset: int, headers: dict) -> tuple[list[dict], int]:
    params = {"jql": jql, "maxResults": limit, "startAt": offset, "fields": DEFAULT_FIELDS}
    resp = _request("GET", SEARCH_URL, headers=headers, params=params)
    if resp.status_code == 400:
        log(f"ERROR: Invalid JQL: {resp.json().get('errorMessages', [])}")
        sys.exit(1)
    if resp.status_code != 200:
        log(f"ERROR: Search API {resp.status_code}")
        sys.exit(1)
    data = resp.json()
    issues = data.get("issues", [])
    total = max(data.get("total", 0), len(issues))
    return issues, total


def format_issue(issue: dict) -> dict:
    fields = issue.get("fields", {})
    desc_raw = fields.get("description")
    description = adf_to_text(desc_raw).strip() if isinstance(desc_raw, dict) else (desc_raw or "")
    description = clean_jira_text(description)

    status = fields.get("status", {})
    parent = fields.get("parent")
    subtasks = fields.get("subtasks", []) or []
    assignee = fields.get("assignee")
    reporter = fields.get("reporter")
    priority = fields.get("priority")
    issuetype = fields.get("issuetype")
    resolution = fields.get("resolution")
    components = fields.get("components", []) or []
    fix_versions = fields.get("fixVersions", []) or []

    comments = _extract_comments(fields.get("comment", {}))
    links = _extract_links(fields.get("issuelinks"))

    return {
        "key": issue.get("key"),
        "title": fields.get("summary"),
        "description": description,
        "status": {"name": status.get("name"), "category": status.get("statusCategory", {}).get("name")},
        "assignee": assignee.get("displayName") if assignee else None,
        "reporter": reporter.get("displayName") if reporter else None,
        "priority": priority.get("name") if priority else None,
        "issuetype": issuetype.get("name") if issuetype else None,
        "resolution": resolution.get("name") if resolution else None,
        "components": [c.get("name") for c in components if c.get("name")],
        "fix_versions": [v.get("name") for v in fix_versions if v.get("name")],
        "labels": fields.get("labels", []),
        "duedate": fields.get("duedate"),
        "parent": {"key": parent["key"], "summary": parent.get("fields", {}).get("summary")} if parent else None,
        "subtasks": [{"key": s["key"], "summary": s.get("fields", {}).get("summary")} for s in subtasks],
        "links": links,
        "created": fields.get("created"),
        "updated": fields.get("updated"),
        "comments": comments,
    }


def _extract_comments(comment_field: dict, max_comments: int = 10) -> list[dict]:
    comments = comment_field.get("comments", []) if comment_field else []
    sorted_c = sorted(comments, key=lambda c: c.get("created", ""), reverse=True)
    result = []
    for c in sorted_c[:max_comments]:
        body_raw = c.get("body")
        body = adf_to_text(body_raw) if isinstance(body_raw, dict) else (body_raw or "")
        result.append({
            "id": c.get("id"),
            "created": c.get("created"),
            "updated": c.get("updated"),
            "author": c.get("author", {}).get("displayName"),
            "body": clean_jira_text(body),
        })
    return result


def _extract_links(issuelinks: list) -> list[dict]:
    links = []
    for link in (issuelinks or []):
        ltype = link.get("type", {}).get("name", "relates to")
        if "inwardIssue" in link:
            links.append({"type": ltype, "key": link["inwardIssue"]["key"]})
        if "outwardIssue" in link:
            links.append({"type": ltype, "key": link["outwardIssue"]["key"]})
    return links


def _build_ticket_metadata(issue: dict) -> dict:
    meta = {
        "status": issue["status"]["name"],
        "status_category": issue["status"]["category"],
        "assignee": issue.get("assignee"),
        "reporter": issue.get("reporter"),
        "priority": issue.get("priority"),
        "issuetype": issue.get("issuetype"),
        "resolution": issue.get("resolution"),
        "duedate": issue.get("duedate"),
        "labels": issue.get("labels", []),
        "components": issue.get("components", []),
        "fix_versions": issue.get("fix_versions", []),
    }
    if issue.get("parent"):
        meta["parent_key"] = issue["parent"]["key"]
        meta["parent_summary"] = issue["parent"].get("summary")
    if issue.get("subtasks"):
        meta["subtask_keys"] = [s["key"] for s in issue["subtasks"]]
    if issue.get("links"):
        meta["linked_issues"] = [{"type": l["type"], "key": l["key"]} for l in issue["links"]]
    return meta


def cache_issue(db: SkillDB, issue: dict) -> bool:
    key = issue["key"]
    changed = False
    parts = [f"Title: {issue['title']}"]
    parts.append(f"Status: {issue['status']['name']} ({issue['status']['category']})")
    for field_name, prefix in [
        ("issuetype", "Type"), ("assignee", "Assignee"), ("reporter", "Reporter"),
        ("priority", "Priority"), ("resolution", "Resolution"), ("duedate", "Due"),
    ]:
        if issue.get(field_name):
            parts.append(f"{prefix}: {issue[field_name]}")
    if issue.get("labels"):
        parts.append(f"Labels: {', '.join(issue['labels'])}")
    if issue.get("components"):
        parts.append(f"Components: {', '.join(issue['components'])}")
    if issue.get("fix_versions"):
        parts.append(f"Fix Versions: {', '.join(issue['fix_versions'])}")
    if issue.get("parent"):
        parts.append(f"Parent: {issue['parent']['key']} - {issue['parent'].get('summary', '')}")
    for s in issue.get("subtasks", []):
        parts.append(f"Subtask: {s['key']} - {s.get('summary', '')}")
    for l in issue.get("links", []):
        parts.append(f"Link ({l['type']}): {l['key']}")
    if issue.get("description"):
        parts.append(f"\nDescription:\n{issue['description']}")

    meta = _build_ticket_metadata(issue)
    if db.upsert_atomic(
        "jira", key, key,
        author=issue.get("reporter") or issue.get("assignee") or "Unknown",
        content="\n".join(parts),
        created_at=issue.get("created", ""),
        updated_at=issue.get("updated", ""),
        metadata=meta,
    ):
        changed = True

    for comment in issue.get("comments", []):
        cid = comment.get("id") or comment.get("created", "")
        if db.upsert_atomic(
            "jira", key, str(cid),
            author=comment.get("author", "Unknown"),
            content=comment.get("body", ""),
            created_at=comment.get("created", ""),
            updated_at=comment.get("updated", comment.get("created", "")),
            metadata={"comment_id": cid},
        ):
            changed = True

    db.clear_relationships(key)
    if issue.get("parent"):
        db.upsert_relationship(key, issue["parent"]["key"], "parent")
    for sub in issue.get("subtasks", []):
        db.upsert_relationship(key, sub["key"], "child")
    for link in issue.get("links", []):
        db.upsert_relationship(key, link["key"], link["type"].lower().replace(" ", "-"))
    return changed


# ═════════════════════════════════════════════════════════════════════
# Source Resolvers
# ═════════════════════════════════════════════════════════════════════

def fetch_filter_jql(filter_id: str, headers: dict) -> tuple[str, str]:
    resp = _request("GET", f"{FILTER_URL}/{filter_id}", headers=headers)
    if resp.status_code != 200:
        log(f"ERROR: Filter API {resp.status_code}")
        sys.exit(1)
    data = resp.json()
    name = data.get("name", "(unnamed)")
    jql = data.get("jql", "")
    if not jql:
        log(f"ERROR: Filter '{name}' has no JQL")
        sys.exit(1)
    return name, jql


def _get_cached_view_jql(view_id: str) -> Optional[str]:
    try:
        if VIEW_CACHE_FILE.exists():
            cache = json.loads(VIEW_CACHE_FILE.read_text())
            entry = cache.get(view_id)
            if entry and (time.time() - entry.get("ts", 0)) < VIEW_CACHE_TTL:
                return entry["jql"]
    except Exception:
        pass
    return None


def _set_cached_view_jql(view_id: str, jql: str) -> None:
    try:
        VIEW_CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        cache = {}
        if VIEW_CACHE_FILE.exists():
            cache = json.loads(VIEW_CACHE_FILE.read_text())
        cache[view_id] = {"jql": jql, "ts": time.time()}
        VIEW_CACHE_FILE.write_text(json.dumps(cache, indent=2))
    except Exception:
        pass


def resolve_view_to_jql(view_id: str, headers: dict, use_cache: bool = True) -> str:
    if use_cache:
        cached = _get_cached_view_jql(view_id)
        if cached:
            log(f"View {view_id}: using cached JQL")
            return cached

    ari = f"ari:cloud:jira:{CLOUD_ID}:view/{view_id}"
    query = """
    query GetPolarisViewJQL($viewId: ID!) {
      polarisView(id: $viewId) {
        jql userJql name sortMode
        sort { order field { jiraFieldKey } }
        filter { kind field { id jiraFieldKey } values { stringValue numericValue enumValue operator } }
      }
    }
    """
    gql_headers = {**headers, "Content-Type": "application/json", "x-experimentalapi": "polaris-v0"}
    resp = _request("POST", GRAPHQL_URL, headers=gql_headers, json={"query": query, "variables": {"viewId": ari}})
    if resp.status_code != 200:
        log(f"ERROR: GraphQL {resp.status_code}")
        sys.exit(1)

    view = resp.json().get("data", {}).get("polarisView")
    if not view:
        log(f"ERROR: View {view_id} not found")
        sys.exit(1)

    base_jql = view.get("jql") or view.get("userJql")
    if not base_jql:
        log(f"ERROR: View {view_id} has no JQL")
        sys.exit(1)

    jql = _build_view_jql(base_jql, view.get("filter") or [], view.get("sort") or [], view.get("sortMode"))
    _set_cached_view_jql(view_id, jql)
    return jql


def _build_view_jql(base_jql: str, filters: list, sort_fields: list, sort_mode: str) -> str:
    order_idx = base_jql.upper().rfind(" ORDER BY ")
    base = base_jql[:order_idx].strip() if order_idx >= 0 else base_jql.strip()
    conditions = [base]

    for f in (filters or []):
        field_info = f.get("field") or {}
        jira_key = field_info.get("jiraFieldKey") or field_info.get("id")
        values_raw = f.get("values") or []
        resolved = []
        for v in values_raw:
            val = v.get("stringValue") or v.get("numericValue") or v.get("enumValue")
            if val is not None:
                resolved.append(str(val))
        if not jira_key or not resolved:
            continue
        jql_field = f"cf[{jira_key.split('_', 1)[1]}]" if jira_key.startswith("customfield_") else jira_key
        negate = "NOT" in (f.get("kind", "")).upper()
        if len(resolved) == 1:
            conditions.append(f"{jql_field} {'!=' if negate else '='} {resolved[0]}")
        else:
            op = "not in" if negate else "in"
            conditions.append(f"{jql_field} {op} ({', '.join(resolved)})")

    jql = " AND ".join(conditions)

    order_parts = []
    for s in (sort_fields or []):
        key = (s.get("field") or {}).get("jiraFieldKey")
        if key:
            order_parts.append(f"{key} {s.get('order', 'DESC').upper()}")
    if not order_parts and sort_mode:
        mode = sort_mode.upper()
        if mode == "PROJECT_RANK":
            order_parts.append("rank ASC")
        elif mode == "CREATED":
            order_parts.append("created DESC")
        elif mode == "UPDATED":
            order_parts.append("updated DESC")
    if order_parts:
        jql += " ORDER BY " + ", ".join(order_parts)
    return jql


# ═════════════════════════════════════════════════════════════════════
# Summarization Pipeline
# ═════════════════════════════════════════════════════════════════════

def _summarize_one(db: SkillDB, key: str, force: bool = False,
                   current: int = 0, total: int = 0) -> None:
    if not force and not db.needs_resummarize(key):
        existing = db.get_resource_summary(key)
        if existing and existing.get("summary"):
            log(f"[{current}/{total}] {key}: cached summary (relevance={existing.get('final_relevance', '?')})")
            return

    existing_summary = db.get_resource_summary(key)
    existing_text = existing_summary["summary"] if existing_summary else None
    summarized_at = existing_summary.get("summarized_at") if existing_summary else None

    if existing_text and summarized_at:
        items = db.get_items_since(key, summarized_at)
        if not items:
            items = db.get_atomic_for_resource(key)
    else:
        items = db.get_atomic_for_resource(key)

    if not items:
        return

    ticket_item = next(
        (i for i in db.get_atomic_for_resource(key) if i["item_id"] == key), None
    )
    title, meta = "", {}
    if ticket_item:
        meta = json.loads(ticket_item.get("metadata", "{}"))
        for line in ticket_item.get("content", "").split("\n"):
            if line.startswith("Title: "):
                title = line[7:]
                break

    mention_type = db.compute_mention_type(key)
    log(f"Summarizing [{current}/{total}] {key} ({len(items)} items, {mention_type})")

    result = summarize_resource(
        title=f"{key}: {title}" if title else key,
        source_type="Jira ticket",
        atomic_items=items,
        metadata=meta,
        existing_summary=existing_text,
        mention_type=mention_type,
    )

    if not result.summary:
        raise RuntimeError(f"Empty summary for {key}")

    enriched_meta = dict(meta)
    enriched_meta["work_items"] = result.work_items
    enriched_meta["people"] = result.people
    enriched_meta["labels"] = result.labels

    db.upsert_summary(
        key, "jira", title or key, result.summary, enriched_meta,
        mention_type=mention_type,
        estimated_relevance=result.relevance,
        final_relevance=result.relevance,
    )
    log(f"Done [{current}/{total}] {key} rel={result.relevance}")


def _summarize_worker(q: "_queue.Queue", db: SkillDB, force: bool, errors: list) -> None:
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        key, current, total = item
        try:
            _summarize_one(db, key, force, current, total)
        except Exception as exc:
            log(f"ERROR summarizing {key}: {exc}")
            errors.append(f"{key}: {exc}")
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

    def put(self, key: str) -> None:
        self._counter += 1
        self._q.put((key, self._counter, self._total))

    def finish(self) -> list[str]:
        self._q.put(None)
        self._thread.join()
        return self._errors


# ═════════════════════════════════════════════════════════════════════
# Output Formatting
# ═════════════════════════════════════════════════════════════════════

def _format_summary_block(db: SkillDB, key: str, s: dict, idx: int, total: int) -> str:
    meta = json.loads(s.get("metadata", "{}"))
    title = s.get("title", "")
    parts = ["Source: jira", f"Key: {key}"]

    rel = s.get("final_relevance", s.get("estimated_relevance", 0))
    mt = s.get("mention_type", "none")
    if rel:
        parts.append(f"Relevance: {rel}/10")
    if mt and mt != "none":
        parts.append(f"Mention: {mt}")

    for field_name, label in [
        ("status", "Status"), ("issuetype", "Type"), ("priority", "Priority"),
        ("assignee", "Assignee"), ("reporter", "Reporter"),
        ("duedate", "Due"), ("resolution", "Resolution"),
    ]:
        val = meta.get(field_name)
        if val:
            if field_name == "status" and meta.get("status_category"):
                val = f"{val} ({meta['status_category']})"
            parts.append(f"{label}: {val}")
    if meta.get("labels"):
        parts.append(f"Labels: {', '.join(meta['labels'])}")
    if meta.get("components"):
        parts.append(f"Components: {', '.join(meta['components'])}")
    if meta.get("fix_versions"):
        parts.append(f"Fix Versions: {', '.join(meta['fix_versions'])}")

    rels = db.get_relationships(key)
    if rels:
        grouped: dict[str, list[str]] = {}
        for r in rels:
            rtype = r["relation_type"]
            target = r["target_key"] if r["source_key"] == key else r["source_key"]
            grouped.setdefault(rtype, []).append(target)
        for rtype, targets in grouped.items():
            parts.append(f"{rtype}: {', '.join(targets)}")

    header = f"[{idx}/{total}] {title}" if title else f"[{idx}/{total}] {key}"
    return f"\n\n## {header}\n{' | '.join(parts)}\n{s.get('summary', '')}"


def write_output(db: SkillDB, output_path: Path, min_relevance: int = 6,
                  since: Optional[str] = None) -> None:
    summaries = db.get_all_summaries(source="jira", min_relevance=min_relevance, since=since)
    total = len(summaries)
    lines = []
    for idx, s in enumerate(summaries, 1):
        lines.append(_format_summary_block(db, s["resource_id"], s, idx, total))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("".join(lines), encoding="utf-8")
    log(f"Output: {output_path} ({total} summaries, min_relevance={min_relevance})")


# ═════════════════════════════════════════════════════════════════════
# Main Entry Point
# ═════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Jira Skill - fetch, cache, and summarize tickets")
    parser.add_argument("--jql", default=None, help="Raw JQL query")
    parser.add_argument("--filter-id", default=_DEFAULT_FILTER_ID, help="Saved filter ID")
    parser.add_argument("--view-id", default=_DEFAULT_VIEW_ID, help="Polaris view ID")
    parser.add_argument("--limit", type=int, default=200, help="Max tickets per source")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--no-cache", action="store_true", help="Bypass view JQL cache")
    parser.add_argument("--days", type=int, default=None,
                        help="Lookback days (default: 14)")
    parser.add_argument("--force", action="store_true", help="Clear summaries and re-summarize (keeps cached content)")
    parser.add_argument("--cached-only", action="store_true", help="Output from DB only, no API calls or summarization")
    parser.add_argument("--min-relevance", type=int, default=6, help="Minimum relevance to include in output (default: 6)")
    parser.add_argument("--output", default=str(_WORKDIR / "jira-output.md"), help="Output .md path")
    args = parser.parse_args()

    output_path = Path(args.output)
    days = args.days if args.days is not None else _default_lookback_days()
    since_dt = datetime.now(_TZ) - timedelta(days=days)
    since_iso = since_dt.strftime("%Y-%m-%d")

    # Ensure no stale output exists while script is running
    if output_path.exists():
        output_path.unlink()

    db = open_db()

    log(f"STARTED (days={days}, since={since_iso})")

    if args.force:
        count = db.clear_all_summaries()
        log(f"--force: cleared {count} summaries (cached content preserved)")

    try:
        if args.cached_only:
            write_output(db, output_path, min_relevance=args.min_relevance, since=since_iso)
            log("COMPLETED (cached-only)")
            return

        if args.force:
            resource_ids = db.get_all_resource_ids()
            log(f"--force: re-summarizing {len(resource_ids)} cached resources (no API fetch)")
            pipeline = _Pipeline(db, force=True)
            pipeline.set_total(len(resource_ids))
            for key in resource_ids:
                pipeline.put(key)
            errors = pipeline.finish()
            if errors:
                log(f"COMPLETED WITH ERRORS ({len(resource_ids)} resources, {len(errors)} error(s))")
                for e in errors:
                    log(f"  ERROR: {e}")
                sys.exit(1)
            write_output(db, output_path, min_relevance=args.min_relevance, since=since_iso)
            log(f"COMPLETED --force ({len(resource_ids)} resources)")
            return

        email, api_key = validate_env()
        headers = get_auth_header(email, api_key)

        jql_sources: list[tuple[str, str]] = []
        if args.filter_id:
            name, jql = fetch_filter_jql(args.filter_id, headers)
            jql_sources.append((f"filter:{args.filter_id} ({name})", jql))
        if args.view_id:
            jql = resolve_view_to_jql(args.view_id, headers, use_cache=not args.no_cache)
            jql_sources.append((f"view:{args.view_id}", jql))
        if args.jql:
            jql_sources.append(("jql", args.jql))

        if not jql_sources:
            log("No sources provided. Use --filter-id, --view-id, or --jql.")
            return

        all_issues: list[tuple[str, list]] = []
        for label, jql in jql_sources:
            issues, total = fetch_issues(jql, args.limit, args.offset, headers)
            log(f"Fetched {len(issues)}/{total} from {label}")
            all_issues.append((label, issues))

        seen: set[str] = set()
        unique_count = 0
        skipped_old = 0
        for _, issues in all_issues:
            for raw in issues:
                k = raw.get("key", "")
                if not k or k in seen:
                    continue
                seen.add(k)
                api_updated = raw.get("fields", {}).get("updated", "")
                if api_updated and api_updated[:10] < since_iso:
                    skipped_old += 1
                    continue
                unique_count += 1

        pipeline = _Pipeline(db, force=False)
        pipeline.set_total(unique_count)
        seen.clear()
        unchanged: list[str] = []
        changed_count = 0

        for _, issues in all_issues:
            for raw in issues:
                key = raw.get("key", "")
                if key in seen:
                    continue
                seen.add(key)

                api_updated = raw.get("fields", {}).get("updated", "")
                if api_updated and api_updated[:10] < since_iso:
                    continue

                if not db.has_content_changed(key, api_updated):
                    unchanged.append(key)
                    continue

                issue = format_issue(raw)
                cache_issue(db, issue)
                changed_count += 1
                pipeline.put(key)

        log(f"Tickets: {unique_count} recent, {changed_count} changed, {len(unchanged)} cached, {skipped_old} older than {since_iso}")

        for key in unchanged:
            pipeline.put(key)

        errors = pipeline.finish()

        if errors:
            log(f"COMPLETED WITH ERRORS ({len(seen)} tickets, {len(errors)} error(s))")
            for e in errors:
                log(f"  ERROR: {e}")
            sys.exit(1)

        write_output(db, output_path, min_relevance=args.min_relevance, since=since_iso)
        log(f"COMPLETED ({len(seen)} tickets)")

    except Exception as e:
        log(f"FAILED: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
