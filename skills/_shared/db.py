"""
Shared SQLite cache for Agent Zero skills.

Stores atomic content (messages, comments) and AI-generated summaries
at the logical resource level (Jira ticket, Gmail thread, GChat thread).
Enables incremental fetching by tracking timestamps.
"""

import hashlib
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

DB_PATH = Path.home() / ".cache" / "agent_zero_skills.db"

_conn: Optional[sqlite3.Connection] = None


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def get_db() -> sqlite3.Connection:
    global _conn
    if _conn is not None:
        return _conn
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    _conn = sqlite3.connect(str(DB_PATH), timeout=10)
    _conn.row_factory = sqlite3.Row
    _conn.execute("PRAGMA journal_mode=WAL")
    _conn.execute("PRAGMA foreign_keys=ON")
    init_db(_conn)
    return _conn


def init_db(conn: sqlite3.Connection) -> None:
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS atomic_content (
            id          TEXT PRIMARY KEY,
            source      TEXT NOT NULL,
            resource_id TEXT NOT NULL,
            item_id     TEXT NOT NULL,
            author      TEXT,
            content     TEXT,
            created_at  TEXT,
            updated_at  TEXT,
            cached_at   TEXT NOT NULL,
            metadata    TEXT DEFAULT '{}'
        );

        CREATE INDEX IF NOT EXISTS idx_atomic_resource
            ON atomic_content(source, resource_id);

        CREATE TABLE IF NOT EXISTS resource_summary (
            resource_id   TEXT PRIMARY KEY,
            source        TEXT NOT NULL,
            title         TEXT,
            summary       TEXT,
            content_hash  TEXT,
            summarized_at TEXT,
            metadata      TEXT DEFAULT '{}'
        );

        CREATE INDEX IF NOT EXISTS idx_summary_source
            ON resource_summary(source);

        CREATE TABLE IF NOT EXISTS fetch_state (
            source_key    TEXT PRIMARY KEY,
            last_fetch_at TEXT NOT NULL,
            metadata      TEXT DEFAULT '{}'
        );
    """)
    conn.commit()


def _make_id(source: str, resource_id: str, item_id: str) -> str:
    return f"{source}:{resource_id}:{item_id}"


def upsert_atomic(
    source: str,
    resource_id: str,
    item_id: str,
    author: str,
    content: str,
    created_at: str,
    updated_at: str,
    metadata: Optional[dict] = None,
) -> bool:
    """Insert or update an atomic content item. Returns True if content changed."""
    conn = get_db()
    pk = _make_id(source, resource_id, item_id)
    meta_json = json.dumps(metadata or {}, separators=(",", ":"), ensure_ascii=False)

    existing = conn.execute(
        "SELECT content, updated_at FROM atomic_content WHERE id = ?", (pk,)
    ).fetchone()

    if existing:
        if existing["content"] == content and existing["updated_at"] == updated_at:
            return False
        conn.execute(
            """UPDATE atomic_content
               SET author=?, content=?, created_at=?, updated_at=?, cached_at=?, metadata=?
               WHERE id=?""",
            (author, content, created_at, updated_at, _now_iso(), meta_json, pk),
        )
    else:
        conn.execute(
            """INSERT INTO atomic_content
               (id, source, resource_id, item_id, author, content, created_at, updated_at, cached_at, metadata)
               VALUES (?,?,?,?,?,?,?,?,?,?)""",
            (pk, source, resource_id, item_id, author, content, created_at, updated_at, _now_iso(), meta_json),
        )
    conn.commit()
    return True


def get_atomic_for_resource(source: str, resource_id: str) -> list[dict]:
    """Get all atomic items for a resource, ordered by created_at ASC."""
    conn = get_db()
    rows = conn.execute(
        """SELECT * FROM atomic_content
           WHERE source=? AND resource_id=?
           ORDER BY created_at ASC""",
        (source, resource_id),
    ).fetchall()
    return [dict(r) for r in rows]


def get_latest_updated_at(source: str, resource_id: str) -> Optional[str]:
    """Get the most recent updated_at timestamp for a resource's atomic content."""
    conn = get_db()
    row = conn.execute(
        """SELECT MAX(updated_at) as max_ts FROM atomic_content
           WHERE source=? AND resource_id=?""",
        (source, resource_id),
    ).fetchone()
    return row["max_ts"] if row else None


def compute_content_hash(source: str, resource_id: str) -> str:
    """Compute SHA256 hash of all atomic content for change detection."""
    items = get_atomic_for_resource(source, resource_id)
    blob = "|".join(f"{i['item_id']}:{i['content']}:{i['updated_at']}" for i in items)
    return hashlib.sha256(blob.encode()).hexdigest()


def get_resource_summary(resource_id: str) -> Optional[dict]:
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM resource_summary WHERE resource_id=?", (resource_id,)
    ).fetchone()
    return dict(row) if row else None


def upsert_summary(
    resource_id: str,
    source: str,
    title: str,
    summary: str,
    content_hash: str,
    metadata: Optional[dict] = None,
) -> None:
    conn = get_db()
    meta_json = json.dumps(metadata or {}, separators=(",", ":"), ensure_ascii=False)
    conn.execute(
        """INSERT INTO resource_summary
           (resource_id, source, title, summary, content_hash, summarized_at, metadata)
           VALUES (?,?,?,?,?,?,?)
           ON CONFLICT(resource_id) DO UPDATE SET
             source=excluded.source,
             title=excluded.title,
             summary=excluded.summary,
             content_hash=excluded.content_hash,
             summarized_at=excluded.summarized_at,
             metadata=excluded.metadata""",
        (resource_id, source, title, summary, content_hash, _now_iso(), meta_json),
    )
    conn.commit()


def get_all_summaries(source: str) -> list[dict]:
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM resource_summary WHERE source=? ORDER BY summarized_at DESC",
        (source,),
    ).fetchall()
    return [dict(r) for r in rows]


def needs_resummarize(resource_id: str, source: str) -> bool:
    """Check if a resource needs re-summarization (content changed since last summary)."""
    existing = get_resource_summary(resource_id)
    if not existing:
        return True
    current_hash = compute_content_hash(source, resource_id)
    return current_hash != existing.get("content_hash")


def get_fetch_state(source_key: str) -> Optional[dict]:
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM fetch_state WHERE source_key=?", (source_key,)
    ).fetchone()
    return dict(row) if row else None


def set_fetch_state(source_key: str, metadata: Optional[dict] = None) -> None:
    conn = get_db()
    meta_json = json.dumps(metadata or {}, separators=(",", ":"), ensure_ascii=False)
    conn.execute(
        """INSERT INTO fetch_state (source_key, last_fetch_at, metadata)
           VALUES (?,?,?)
           ON CONFLICT(source_key) DO UPDATE SET
             last_fetch_at=excluded.last_fetch_at,
             metadata=excluded.metadata""",
        (source_key, _now_iso(), meta_json),
    )
    conn.commit()


def get_resource_ids_for_source(source: str) -> list[str]:
    conn = get_db()
    rows = conn.execute(
        "SELECT DISTINCT resource_id FROM atomic_content WHERE source=?", (source,)
    ).fetchall()
    return [r["resource_id"] for r in rows]


def delete_resource(source: str, resource_id: str) -> None:
    """Remove all atomic content and summary for a resource."""
    conn = get_db()
    conn.execute(
        "DELETE FROM atomic_content WHERE source=? AND resource_id=?",
        (source, resource_id),
    )
    conn.execute("DELETE FROM resource_summary WHERE resource_id=?", (resource_id,))
    conn.commit()


def close_db() -> None:
    global _conn
    if _conn:
        _conn.close()
        _conn = None
