"""
SQLite cache for the GChat skill.

Provides SkillDB class with CRUD for atomic content (chat messages)
and resource summaries (conversation summaries). Self-contained - no external dependencies.

Change detection uses data-display-timestamp comparison at feed level.
No edit detection in v1 - messages treated as insert-only.
"""

import json
import os
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Optional
from zoneinfo import ZoneInfo

_TZ = ZoneInfo(os.environ.get("TZ", "Asia/Singapore"))


def _now_iso() -> str:
    return datetime.now(_TZ).isoformat()


_DB_OPEN_RETRIES = 3
_DB_RETRY_DELAY_S = 2


def _remove_db_files(db_path: Path) -> None:
    """Remove the SQLite DB and its WAL/SHM companion files."""
    for suffix in ("", "-wal", "-shm"):
        p = db_path.parent / (db_path.name + suffix)
        if p.exists():
            p.unlink()


def get_gchat_db(db_path: str | Path, *, force: bool = False) -> "SkillDB":
    """Open or create the GChat SQLite database with retry on transient NFS errors.

    When force=True, deletes the existing DB (and WAL/SHM) before creating a fresh one.
    """
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    if force and db_path.exists():
        _remove_db_files(db_path)

    last_err: Exception | None = None
    for attempt in range(_DB_OPEN_RETRIES):
        try:
            conn = sqlite3.connect(str(db_path), timeout=30)
            conn.row_factory = sqlite3.Row
            try:
                conn.execute("PRAGMA journal_mode=WAL")
            except sqlite3.OperationalError:
                try:
                    conn.execute("PRAGMA journal_mode=DELETE")
                except sqlite3.OperationalError:
                    pass
            conn.execute("PRAGMA synchronous=NORMAL")
            conn.execute("PRAGMA busy_timeout=10000")
            conn.execute("PRAGMA foreign_keys=ON")
            db = SkillDB(conn)
            db._init_tables()
            return db
        except sqlite3.DatabaseError as exc:
            last_err = exc
            import time
            time.sleep(_DB_RETRY_DELAY_S * (attempt + 1))
    raise last_err  # type: ignore[misc]


class SkillDB:
    _WRITE_RETRIES = 3
    _WRITE_RETRY_DELAY_S = 1

    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    def _retry(self, fn):
        """Retry a DB write operation on transient errors (NFS, WAL contention)."""
        last_err: Exception | None = None
        for attempt in range(self._WRITE_RETRIES):
            try:
                return fn()
            except sqlite3.DatabaseError as exc:
                last_err = exc
                import time
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
        """Insert atomic content if not already cached. Returns True if new."""
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
        rows = self._conn.execute(
            "SELECT item_id FROM atomic_content WHERE resource_id=?",
            (resource_id,),
        ).fetchall()
        return {r["item_id"] for r in rows}

    def get_latest_cached_at(self, resource_id: str) -> Optional[str]:
        row = self._conn.execute(
            "SELECT MAX(cached_at) as max_ts FROM atomic_content WHERE resource_id=?",
            (resource_id,),
        ).fetchone()
        return row["max_ts"] if row else None

    # ── Change Detection ─────────────────────────────────────────────

    def conversation_needs_fetch(self, group_id: str, display_ts_ms: int) -> bool:
        """Check if a conversation needs fetching by comparing feed's
        data-display-timestamp (epoch_ms) against cached latest updated_at."""
        if display_ts_ms <= 0:
            return True
        ts_iso = datetime.fromtimestamp(display_ts_ms / 1000, tz=_TZ).isoformat()
        latest = self._conn.execute(
            "SELECT MAX(updated_at) as max_ts FROM atomic_content WHERE resource_id=?",
            (group_id,),
        ).fetchone()
        if not latest or not latest["max_ts"]:
            return True
        return ts_iso > latest["max_ts"]

    # ── Resource Summary ────────────────────────────────────────────

    def get_resource_summary(self, resource_id: str) -> Optional[dict]:
        row = self._conn.execute(
            "SELECT * FROM resource_summary WHERE resource_id=?", (resource_id,)
        ).fetchone()
        return dict(row) if row else None

    def needs_resummarize(self, resource_id: str) -> bool:
        """Check if new content has been cached since last summarization."""
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
        def _do():
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
        self._retry(_do)

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
