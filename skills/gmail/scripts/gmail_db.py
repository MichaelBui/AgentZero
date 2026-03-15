"""
SQLite cache for the Gmail skill.

Provides SkillDB class with CRUD for atomic content (email messages)
and resource summaries (thread summaries). Self-contained - no external dependencies.

Change detection uses data-legacy-last-non-draft-message-id comparison.
No ticket_relationships table (Gmail threads are flat).
"""

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def get_gmail_db(db_path: str | Path) -> "SkillDB":
    """Open or create the Gmail SQLite database."""
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path), timeout=10)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA busy_timeout=5000")
    conn.execute("PRAGMA foreign_keys=ON")
    db = SkillDB(conn)
    db._init_tables()
    return db


class SkillDB:
    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

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
        self._conn.commit()

    # ── Atomic Content ──────────────────────────────────────────────

    def upsert_atomic(
        self,
        source: str,
        resource_id: str,
        item_id: str,
        author: str,
        content: str,
        created_at: str,
        updated_at: str,
        metadata: Optional[dict] = None,
    ) -> bool:
        """Insert or update atomic content. Returns True if content is new or updated.
        For Gmail, emails are immutable so updates should not happen in practice."""
        pk = f"{source}:{resource_id}:{item_id}"
        meta_json = json.dumps(metadata or {}, separators=(",", ":"), ensure_ascii=False)

        existing = self._conn.execute(
            "SELECT updated_at FROM atomic_content WHERE id = ?", (pk,)
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

    def has_message(self, resource_id: str, item_id: str) -> bool:
        """Check if a specific message is already cached."""
        pk = f"gmail:{resource_id}:{item_id}"
        row = self._conn.execute(
            "SELECT 1 FROM atomic_content WHERE id = ?", (pk,)
        ).fetchone()
        return row is not None

    def get_atomic_for_resource(self, resource_id: str) -> list[dict]:
        rows = self._conn.execute(
            """SELECT * FROM atomic_content
               WHERE resource_id=? ORDER BY created_at ASC""",
            (resource_id,),
        ).fetchall()
        return [dict(r) for r in rows]

    def get_cached_message_ids(self, resource_id: str) -> set[str]:
        """Get set of item_ids already cached for a thread."""
        rows = self._conn.execute(
            "SELECT item_id FROM atomic_content WHERE resource_id=?",
            (resource_id,),
        ).fetchall()
        return {r["item_id"] for r in rows}

    def get_latest_updated_at(self, resource_id: str) -> Optional[str]:
        row = self._conn.execute(
            "SELECT MAX(updated_at) as max_ts FROM atomic_content WHERE resource_id=?",
            (resource_id,),
        ).fetchone()
        return row["max_ts"] if row else None

    def get_latest_cached_at(self, resource_id: str) -> Optional[str]:
        """Get the latest cached_at timestamp (ISO format) for a resource.
        Used for needs_resummarize since Gmail dates are not ISO format."""
        row = self._conn.execute(
            "SELECT MAX(cached_at) as max_ts FROM atomic_content WHERE resource_id=?",
            (resource_id,),
        ).fetchone()
        return row["max_ts"] if row else None

    def get_all_resource_ids(self, source: Optional[str] = None) -> list[str]:
        if source:
            rows = self._conn.execute(
                "SELECT DISTINCT resource_id FROM atomic_content WHERE source=?", (source,)
            ).fetchall()
        else:
            rows = self._conn.execute(
                "SELECT DISTINCT resource_id FROM atomic_content"
            ).fetchall()
        return [r["resource_id"] for r in rows]

    # ── Change Detection ─────────────────────────────────────────────

    def get_cached_last_message_id(self, resource_id: str) -> Optional[str]:
        """Get the last_message_id stored in resource_summary metadata.
        This is the data-legacy-last-non-draft-message-id from last fetch."""
        summary = self.get_resource_summary(resource_id)
        if not summary:
            return None
        meta = json.loads(summary.get("metadata", "{}"))
        return meta.get("last_message_id")

    def thread_needs_fetch(self, thread_id: str, listing_last_msg_id: str) -> bool:
        """Check if a thread needs fetching by comparing listing's
        data-legacy-last-non-draft-message-id against cached value."""
        cached = self.get_cached_last_message_id(thread_id)
        if cached is None:
            return True
        return listing_last_msg_id != cached

    # ── Resource Summary ────────────────────────────────────────────

    def get_resource_summary(self, resource_id: str) -> Optional[dict]:
        row = self._conn.execute(
            "SELECT * FROM resource_summary WHERE resource_id=?", (resource_id,)
        ).fetchone()
        return dict(row) if row else None

    def needs_resummarize(self, resource_id: str) -> bool:
        """Check if content has been added since last summarization.
        Uses cached_at (ISO) instead of updated_at (Gmail human-readable date)
        to ensure correct timestamp comparison."""
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
        """Get atomic items added after a given timestamp (for incremental summarization)."""
        rows = self._conn.execute(
            """SELECT * FROM atomic_content
               WHERE resource_id=? AND cached_at > ?
               ORDER BY created_at ASC""",
            (resource_id, since_timestamp),
        ).fetchall()
        return [dict(r) for r in rows]

    def upsert_summary(
        self,
        resource_id: str,
        source: str,
        title: str,
        summary: str,
        metadata: Optional[dict] = None,
    ) -> None:
        meta_json = json.dumps(metadata or {}, separators=(",", ":"), ensure_ascii=False)
        self._conn.execute(
            """INSERT INTO resource_summary
               (resource_id, source, title, summary, summarized_at, metadata)
               VALUES (?,?,?,?,?,?)
               ON CONFLICT(resource_id) DO UPDATE SET
                 source=excluded.source, title=excluded.title,
                 summary=excluded.summary,
                 summarized_at=excluded.summarized_at, metadata=excluded.metadata""",
            (resource_id, source, title, summary, _now_iso(), meta_json),
        )
        self._conn.commit()

    def get_all_summaries(self, source: Optional[str] = None) -> list[dict]:
        if source:
            rows = self._conn.execute(
                "SELECT * FROM resource_summary WHERE source=? ORDER BY summarized_at DESC",
                (source,),
            ).fetchall()
        else:
            rows = self._conn.execute(
                "SELECT * FROM resource_summary ORDER BY summarized_at DESC"
            ).fetchall()
        return [dict(r) for r in rows]

    # ── Cleanup ─────────────────────────────────────────────────────

    def delete_resource(self, resource_id: str) -> None:
        self._conn.execute(
            "DELETE FROM atomic_content WHERE resource_id=?", (resource_id,)
        )
        self._conn.execute(
            "DELETE FROM resource_summary WHERE resource_id=?", (resource_id,)
        )
        self._conn.commit()

    def close(self) -> None:
        self._conn.close()
