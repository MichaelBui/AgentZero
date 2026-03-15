"""
SQLite cache for the Jira skill.

Provides SkillDB class with CRUD for atomic content, summaries,
and ticket relationships. Self-contained - no external dependencies.

Change detection uses updated_at timestamps only.
"""

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def get_jira_db(db_path: str | Path) -> "SkillDB":
    """Open or create the Jira SQLite database."""
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path), timeout=10)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
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
        """Insert or update atomic content. Returns True if content is new or updated."""
        pk = f"{source}:{resource_id}:{item_id}"
        meta_json = json.dumps(metadata or {}, separators=(",", ":"), ensure_ascii=False)

        existing = self._conn.execute(
            "SELECT updated_at FROM atomic_content WHERE id = ?", (pk,)
        ).fetchone()

        if existing:
            if existing["updated_at"] == updated_at:
                return False
            self._conn.execute(
                """UPDATE atomic_content
                   SET author=?, content=?, created_at=?,
                       updated_at=?, cached_at=?, metadata=?
                   WHERE id=?""",
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

    def get_atomic_for_resource(self, resource_id: str) -> list[dict]:
        rows = self._conn.execute(
            """SELECT * FROM atomic_content
               WHERE resource_id=? ORDER BY created_at ASC""",
            (resource_id,),
        ).fetchall()
        return [dict(r) for r in rows]

    def get_latest_updated_at(self, resource_id: str) -> Optional[str]:
        row = self._conn.execute(
            "SELECT MAX(updated_at) as max_ts FROM atomic_content WHERE resource_id=?",
            (resource_id,),
        ).fetchone()
        return row["max_ts"] if row else None

    def has_content_changed(self, resource_id: str, new_updated_at: str) -> bool:
        """Check if a resource has newer content than what we cached (timestamp comparison)."""
        cached_ts = self.get_latest_updated_at(resource_id)
        if cached_ts is None:
            return True
        return new_updated_at > cached_ts

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

    # ── Resource Summary ────────────────────────────────────────────

    def get_resource_summary(self, resource_id: str) -> Optional[dict]:
        row = self._conn.execute(
            "SELECT * FROM resource_summary WHERE resource_id=?", (resource_id,)
        ).fetchone()
        return dict(row) if row else None

    def needs_resummarize(self, resource_id: str) -> bool:
        """Check if content has been updated since last summarization."""
        existing = self.get_resource_summary(resource_id)
        if not existing:
            return True
        summarized_at = existing.get("summarized_at")
        if not summarized_at:
            return True
        latest_updated = self.get_latest_updated_at(resource_id)
        if not latest_updated:
            return False
        return latest_updated > summarized_at

    def get_items_since(self, resource_id: str, since_timestamp: str) -> list[dict]:
        """Get atomic items updated after a given timestamp (for incremental summarization)."""
        rows = self._conn.execute(
            """SELECT * FROM atomic_content
               WHERE resource_id=? AND updated_at > ?
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

    # ── Ticket Relationships ────────────────────────────────────────

    def upsert_relationship(
        self, source_key: str, target_key: str, relation_type: str
    ) -> None:
        self._conn.execute(
            """INSERT INTO ticket_relationships
               (source_key, target_key, relation_type, cached_at)
               VALUES (?,?,?,?)
               ON CONFLICT(source_key, target_key, relation_type) DO UPDATE SET
                 cached_at=excluded.cached_at""",
            (source_key, target_key, relation_type, _now_iso()),
        )
        self._conn.commit()

    def get_relationships(self, ticket_key: str) -> list[dict]:
        rows = self._conn.execute(
            """SELECT * FROM ticket_relationships
               WHERE source_key=? OR target_key=?
               ORDER BY relation_type""",
            (ticket_key, ticket_key),
        ).fetchall()
        return [dict(r) for r in rows]

    def clear_relationships(self, ticket_key: str) -> None:
        self._conn.execute(
            "DELETE FROM ticket_relationships WHERE source_key=?", (ticket_key,)
        )
        self._conn.commit()

    # ── Cleanup ─────────────────────────────────────────────────────

    def delete_resource(self, resource_id: str) -> None:
        self._conn.execute(
            "DELETE FROM atomic_content WHERE resource_id=?", (resource_id,)
        )
        self._conn.execute(
            "DELETE FROM resource_summary WHERE resource_id=?", (resource_id,)
        )
        self._conn.execute(
            "DELETE FROM ticket_relationships WHERE source_key=? OR target_key=?",
            (resource_id, resource_id),
        )
        self._conn.commit()

    def close(self) -> None:
        self._conn.close()
