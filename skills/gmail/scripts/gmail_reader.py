#!/usr/bin/env python3
"""
Gmail Reader - extract email threads via CDP, cache, and summarize.

Connects to a remote Chrome instance, navigates Gmail search, extracts threads.
Caches each message in SQLite, summarizes at thread level via AI.
Streams output per thread: ## gmail/{thread_id}: {subject}

Usage:
  python gmail_reader.py
  python gmail_reader.py --days 7 --max-threads 10
  python gmail_reader.py --force
"""

import argparse
import json
import os
import queue as _queue
import sys
import threading
import time
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PwTimeout

from gmail_db import get_gmail_db, SkillDB
from gmail_cleaner import clean_email_body
from gmail_summarizer import summarize_resource

DEFAULT_CDP = "http://192.168.1.11:9223"
GMAIL_BASE = "https://mail.google.com"
DEFAULT_EXCLUDE = '["❌ ai-exclusion", "🪣 Bitbucket"]'
DEFAULT_PRIORITY = '["⚠️IMPORTANT", "❗️ ASAP  🏃‍♂️‍➡️", "🔜 Soon 🚶‍♂️‍➡️", "👀 KIV 🧘‍♂️", "📝 Noted"]'
_WORKDIR = Path(__file__).resolve().parents[3] / "workdir"
DB_PATH = Path(__file__).resolve().parent.parent / "data" / "gmail_cache.db"


_debug_file = sys.stderr
_output_file = sys.stdout


from datetime import datetime
from zoneinfo import ZoneInfo

_TZ = ZoneInfo(os.environ.get("TZ", "Asia/Singapore"))


def _ts() -> str:
    return datetime.now(_TZ).strftime("%Y-%m-%dT%H:%M:%S%z")


def eprint(*a, **kw):
    print(f"[{_ts()}]", *a, file=_debug_file, flush=True, **kw)


_HEARTBEAT_INTERVAL = int(os.environ.get("SKILL_HEARTBEAT_INTERVAL", "60"))


# ── Browser & Navigation ───────────────────────────────────────────

def connect_browser(cdp_url: str):
    eprint(f"Connecting to Chrome at {cdp_url}...")
    pw = sync_playwright().start()
    browser = pw.chromium.connect_over_cdp(cdp_url)
    eprint(f"Connected. Browser version: {browser.version}")
    contexts = browser.contexts
    context = contexts[0] if contexts else browser.new_context()
    pages = context.pages
    eprint(f"Found {len(pages)} open tab(s)")
    gmail_page = None
    for p in pages:
        if "mail.google.com" in p.url:
            gmail_page = p
            eprint("Reusing existing Gmail tab")
            break
    if not gmail_page:
        eprint("No Gmail tab found. Opening new tab...")
        gmail_page = context.new_page()
    return pw, browser, gmail_page


def navigate_to_search(page, days: int):
    search_url = f"{GMAIL_BASE}/mail/u/0/#search/newer_than%3A{days}d"
    eprint(f"Navigating to Gmail (last {days} days)...")
    page.goto(search_url, wait_until="domcontentloaded", timeout=30000)
    time.sleep(4)
    page.wait_for_selector('div[role="main"] tr[jscontroller]', timeout=15000)
    eprint("Gmail search results loaded.")


def get_thread_list(page) -> list[dict]:
    """Extract thread listing data including legacy thread IDs from DOM."""
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

            // Extract legacy IDs from hidden spans
            let legacyThreadId = '';
            let legacyLastMsgId = '';
            const idSpans = tr.querySelectorAll('span[data-legacy-thread-id]');
            if (idSpans.length > 0) {
                legacyThreadId = idSpans[0].getAttribute('data-legacy-thread-id') || '';
            }
            const lastMsgSpans = tr.querySelectorAll('span[data-legacy-last-non-draft-message-id]');
            if (lastMsgSpans.length > 0) {
                legacyLastMsgId = lastMsgSpans[0].getAttribute('data-legacy-last-non-draft-message-id') || '';
            }

            const senderEls = tr.querySelectorAll('span[email]');
            const senders = [];
            const seen = new Set();
            for (const s of senderEls) {
                const email = s.getAttribute('email') || '';
                if (!seen.has(email)) {
                    seen.add(email);
                    senders.push({
                        name: s.getAttribute('name') || s.textContent.trim(),
                        email: email
                    });
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

            const snippetEl = tds[5].querySelector('span.y2');
            const snippet = snippetEl ? snippetEl.textContent.trim().replace(/^\\s*-\\s*/, '') : '';
            const dateSpan = tds[8].querySelector('span[title]');
            const date = dateSpan ? dateSpan.getAttribute('title') : tds[8].textContent.trim();
            const labelEls = tds[5].querySelectorAll('div.at');
            const labels = [];
            for (const l of labelEls) {
                labels.push(l.getAttribute('title') || l.textContent.trim());
            }

            threads.push({
                rowIndex: i,
                legacyThreadId: legacyThreadId,
                legacyLastMsgId: legacyLastMsgId,
                senders: senders,
                subject: subject,
                snippet: snippet.substring(0, 120),
                date: date,
                labels: labels
            });
        }
        return threads;
    }
    """)


def click_thread_row(page, row_index: int):
    page.evaluate("""
    (idx) => {
        const main = document.querySelector('div[role="main"]');
        const rows = main.querySelectorAll('tr[jscontroller]');
        if (rows[idx]) {
            const linkEl = rows[idx].querySelector('td.xY.a4W div[role="link"]');
            if (linkEl) linkEl.click();
            else rows[idx].click();
        }
    }
    """, row_index)


def wait_for_thread_view(page, timeout_ms: int = 15000) -> bool:
    try:
        page.wait_for_selector(
            '[data-message-id], div.adn, table.Bs, h2.hP',
            timeout=timeout_ms
        )
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
        eprint("  Clicked 'Expand all' button, waiting for messages to load...")
        msg_count = _wait_for_messages_stable(page)
        eprint(f"  {msg_count} message(s) loaded")
    page.evaluate("""
    () => {
        const detailBtns = document.querySelectorAll(
            'img[aria-label="Show details"], span.ajy, div.ajz'
        );
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
    """Extract all messages from thread view with legacy message IDs."""
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
                            const recipient = {
                                name: e.getAttribute('name') || e.textContent.trim(),
                                email: e.getAttribute('email') || ''
                            };
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
                    toList.push({
                        name: s.getAttribute('name') || s.textContent.trim(),
                        email: email
                    });
                }
            }

            let body = '';
            const bodySelectors = ['div.a3s.aiL', 'div.a3s', 'div[dir="ltr"]'];
            for (const sel of bodySelectors) {
                const bodyEl = container.querySelector(sel);
                if (bodyEl && bodyEl.textContent.trim().length > 5) {
                    body = bodyEl.innerText.trim();
                    break;
                }
            }
            if (!body) {
                const clone = container.cloneNode(true);
                const headers = clone.querySelectorAll('.gE, .gH, .gK, .gs');
                for (const h of headers) h.remove();
                body = clone.innerText ? clone.innerText.trim() : clone.textContent.trim();
            }
            body = body.replace(/\\n{3,}/g, '\\n\\n').trim();

            messages.push({
                legacy_message_id: legacyMsgId,
                from: sender,
                to: toList,
                cc: ccList,
                date: date,
                body: body
            });
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


def navigate_to_thread(page, thread_id: str) -> bool:
    """Navigate directly to a Gmail thread by its legacy thread ID."""
    url = f"{GMAIL_BASE}/mail/u/0/#all/{thread_id}"
    page.goto(url, wait_until="domcontentloaded", timeout=20000)
    time.sleep(2)
    return wait_for_thread_view(page)


def navigate_to_page(page, days: int, page_num: int) -> bool:
    """Navigate to a specific page of Gmail search results using /pN URL parameter.
    Page 1 has no suffix; page 2+ uses /pN. Returns True if threads loaded."""
    if page_num <= 1:
        search_url = f"{GMAIL_BASE}/mail/u/0/#search/newer_than%3A{days}d"
    else:
        search_url = f"{GMAIL_BASE}/mail/u/0/#search/newer_than%3A{days}d/p{page_num}"
    eprint(f"Navigating to Gmail search (page {page_num}, last {days} days)...")
    page.goto(search_url, wait_until="domcontentloaded", timeout=30000)
    time.sleep(5)
    try:
        page.wait_for_selector('div[role="main"] tr[jscontroller]', timeout=20000)
        eprint("Gmail search results loaded.")
        return True
    except PwTimeout:
        eprint(f"  WARN: Page {page_num} did not load threads within timeout")
        return False


def match_priority(labels: list[str], priority_labels: list[str]) -> str | None:
    for pl in priority_labels:
        for label in labels:
            if pl.strip() == label.strip():
                return pl.strip()
    return None


# ── Caching ─────────────────────────────────────────────────────────

def cache_thread_messages(
    db: SkillDB, thread_id: str, subject: str, messages: list[dict],
    labels: list, priority: str | None
) -> int:
    """Cache each message in the thread. Returns count of new messages cached."""
    cached_ids = db.get_cached_message_ids(thread_id)
    new_count = 0

    for msg in messages:
        msg_id = msg.get("legacy_message_id", "")
        if not msg_id:
            continue
        if msg_id in cached_ids:
            continue

        body = clean_email_body(msg.get("body", ""))
        author = msg.get("from", "Unknown")
        date = msg.get("date", "")

        meta = {
            "to": msg.get("to", []),
            "cc": msg.get("cc", []),
            "subject": subject,
        }

        if db.upsert_atomic(
            "gmail", thread_id, msg_id,
            author=author, content=body,
            created_at=date, updated_at=date,
            metadata=meta,
        ):
            new_count += 1

    return new_count


# ── Output & Summarization ─────────────────────────────────────────

def _to_local_ts(iso_str: str) -> str:
    """Convert an ISO timestamp string to the configured local timezone."""
    if not iso_str:
        return iso_str
    try:
        dt = datetime.fromisoformat(iso_str)
        return dt.astimezone(_TZ).isoformat()
    except (ValueError, TypeError):
        return iso_str


def _print_output(thread_id: str, subject: str, summary_text: str,
                  labels: list, priority: str | None, senders: list, date: str,
                  summarized_at: str = "",
                  current: int = 0, total: int = 0):
    """Print a single thread's output in streaming format."""
    label_str = ", ".join(labels) if labels else "None"
    priority_str = priority or "None"
    sender_names = ", ".join(s.get("name", s.get("email", "")) for s in senders) if senders else "Unknown"
    updated_str = f" | Last Updated: {_to_local_ts(summarized_at)}" if summarized_at else ""

    numbering = f"[{current}/{total}] " if current and total else ""
    print(f"\n\n## {numbering}{subject}", file=_output_file, flush=True)
    print(
        f"Source: gmail | Thread: {thread_id} | Labels: {label_str} | "
        f"Priority: {priority_str} | Senders: {sender_names} | Last Date: {date}{updated_str}",
        file=_output_file, flush=True,
    )
    print(summary_text, file=_output_file, flush=True)


def summarize_and_output(db: SkillDB, thread_info: dict):
    """Summarize a single thread and stream output immediately."""
    thread_id = thread_info["thread_id"]
    subject = thread_info["subject"]
    labels = thread_info.get("labels", [])
    priority = thread_info.get("priority")
    senders = thread_info.get("senders", [])
    date = thread_info.get("date", "")
    last_msg_id = thread_info.get("last_msg_id", "")
    current = thread_info.get("_sum_current", "?")
    total = thread_info.get("_sum_total", "?")
    current_int = current if isinstance(current, int) else 0
    total_int = total if isinstance(total, int) else 0
    sum_progress = f"[Summarizing {current}/{total}]"
    sum_done = f"[Summarized {current}/{total}]"

    if not db.needs_resummarize(thread_id):
        existing = db.get_resource_summary(thread_id)
        if existing:
            eprint(f"{sum_done} [{subject[:40]}]: using cached summary")
            _print_output(thread_id, subject, existing["summary"], labels, priority, senders, date,
                          summarized_at=existing.get("summarized_at", ""),
                          current=current_int, total=total_int)
            return

    items = db.get_atomic_for_resource(thread_id)
    if not items:
        eprint(f"{sum_done} [{subject[:40]}]: no cached messages, outputting metadata only")
        _print_output(thread_id, subject, "(Not yet fetched)", labels, priority, senders, date,
                      current=current_int, total=total_int)
        return

    existing_summary = db.get_resource_summary(thread_id)
    existing_text = existing_summary["summary"] if existing_summary else None

    if existing_text and existing_summary:
        prev_summarized_at = existing_summary.get("summarized_at", "")
        new_items = db.get_items_since(thread_id, prev_summarized_at) if prev_summarized_at else items
        if new_items:
            items_to_summarize = new_items
        else:
            items_to_summarize = items
    else:
        prev_summarized_at = ""
        items_to_summarize = items

    meta = {"labels": labels, "priority": priority, "last_message_id": last_msg_id}

    eprint(f"{sum_progress} [{subject[:40]}]: AI summarizing ({len(items_to_summarize)} messages)...")
    summary_text = summarize_resource(
        title=subject,
        source_type="Email thread",
        atomic_items=items_to_summarize,
        metadata=meta,
        existing_summary=existing_text,
    )

    if summary_text:
        db.upsert_summary(thread_id, "gmail", subject, summary_text, meta)
        saved = db.get_resource_summary(thread_id)
        new_summarized_at = saved.get("summarized_at", "") if saved else ""
        _print_output(thread_id, subject, summary_text, labels, priority, senders, date,
                      summarized_at=new_summarized_at,
                      current=current_int, total=total_int)
        eprint(f"{sum_done} [{subject[:40]}]: done")
    elif existing_text:
        _print_output(thread_id, subject, existing_text, labels, priority, senders, date,
                      summarized_at=prev_summarized_at,
                      current=current_int, total=total_int)


def _summarize_worker(q: "_queue.Queue", db_path: Path, error_event: threading.Event, results: list) -> None:
    """Background worker: process summarization queue one item at a time."""
    worker_db = get_gmail_db(db_path)
    current = 0
    try:
        while True:
            item = q.get()
            if item is None:
                q.task_done()
                break
            current += 1
            item["_sum_current"] = current
            try:
                summarize_and_output(worker_db, item)
            except Exception as exc:
                eprint(f"ERROR summarizing {item.get('thread_id', '?')}: {exc}")
                results.append(exc)
                error_event.set()
            finally:
                q.task_done()
    finally:
        worker_db.close()


# ── Main ────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Read Gmail email threads via CDP, cache, and summarize"
    )
    parser.add_argument("--cdp-url", default=DEFAULT_CDP,
                        help=f"Chrome DevTools endpoint (default: {DEFAULT_CDP})")
    parser.add_argument("--days", type=int, default=3,
                        help="Days to look back (default: 3)")
    parser.add_argument("--max-threads", type=int, default=200,
                        help="Max threads to read (default: 200)")
    parser.add_argument("--max-scan", type=int, default=500,
                        help="Max total threads to scan (default: 500)")
    parser.add_argument("--exclude-labels", default=DEFAULT_EXCLUDE,
                        help="JSON array of labels to exclude")
    parser.add_argument("--priority-labels", default=DEFAULT_PRIORITY,
                        help="JSON array of priority labels, highest first")
    parser.add_argument("--early-stop", type=int, default=5,
                        help="Stop after N consecutive cached/unchanged threads (default: 5, 0=disabled)")
    parser.add_argument("--cached-only", action="store_true",
                        help="Output cached summaries from DB without browser fetching (fast, for reports)")
    parser.add_argument("--force", action="store_true",
                        help="Bypass change detection, re-fetch and re-summarize all")
    parser.add_argument("--output", default=str(_WORKDIR / "gmail-output.md"),
                        help="Write results to this file (default: workdir/gmail-output.md)")
    parser.add_argument("--debug-log", default=str(_WORKDIR / "gmail-debug.log"),
                        help="Write debug messages to this file (default: workdir/gmail-debug.log)")
    args = parser.parse_args()

    global _output_file, _debug_file
    for p in (Path(args.output), Path(args.debug_log)):
        p.parent.mkdir(parents=True, exist_ok=True)
    _output_file = open(args.output, "w", encoding="utf-8", buffering=1)
    _debug_file = open(args.debug_log, "w", encoding="utf-8", buffering=1)
    eprint(f"{'='*60}")
    eprint(f"STATUS: STARTED - Gmail Reader")
    eprint(f"output={args.output}, debug={args.debug_log}")
    eprint(f"{'='*60}")

    print("[gmail_reader] STARTED - processing Gmail threads. Do NOT interrupt or move on - this takes 5-15 minutes.", flush=True)

    try:
        exclude_labels = json.loads(args.exclude_labels)
    except json.JSONDecodeError:
        eprint(f"ERROR: Invalid JSON for --exclude-labels: {args.exclude_labels}")
        sys.exit(1)
    try:
        priority_labels = json.loads(args.priority_labels)
    except json.JSONDecodeError:
        eprint(f"ERROR: Invalid JSON for --priority-labels: {args.priority_labels}")
        sys.exit(1)

    if args.force:
        eprint("--force: recreating database from scratch")
    db = get_gmail_db(DB_PATH, force=args.force)
    pw = browser = None

    if args.cached_only:
        try:
            summaries = db.get_all_summaries(source="gmail")
            total = len(summaries)
            eprint(f"Cached-only mode: {total} summaries from DB")
            for idx, s in enumerate(summaries, 1):
                meta = json.loads(s.get("metadata", "{}"))
                labels = meta.get("labels", [])
                priority = meta.get("priority")
                senders = []
                _print_output(
                    s["resource_id"], s.get("title", "(no subject)"),
                    s.get("summary", "(no summary)"),
                    labels, priority, senders, "",
                    summarized_at=s.get("summarized_at", ""),
                    current=idx, total=total,
                )
            eprint(f"{'='*60}")
            eprint(f"STATUS: COMPLETED - Gmail Reader (cached-only): {len(summaries)} summaries output")
            eprint(f"{'='*60}")
        finally:
            db.close()
            if _output_file and _output_file is not sys.stdout:
                _output_file.close()
            if _debug_file and _debug_file is not sys.stderr:
                _debug_file.close()
        return

    try:
        eprint(f"Connecting to browser at {args.cdp_url}...")
        pw, browser, page = connect_browser(args.cdp_url)
        eprint("Browser connected.")

        # ── Phase 1: Scan listing pages to collect thread metadata ──
        thread_infos = []
        threads_to_fetch = []
        seen_thread_ids = set()
        scanned = 0
        skipped_excluded = 0
        skipped_unchanged = 0
        consecutive_cached = 0
        early_stop_triggered = False
        page_num = 1

        eprint(f"\nPhase 1: Scanning listing (target: {args.max_threads}, "
               f"scan limit: {args.max_scan}, early-stop: {args.early_stop})...")

        while len(thread_infos) < args.max_threads and scanned < args.max_scan:
            if not navigate_to_page(page, args.days, page_num):
                if page_num == 1:
                    eprint("FATAL: 0 threads found - Gmail DOM selectors may need updating.")
                    sys.exit(2)
                eprint(f"  Page {page_num}: failed to load, stopping.")
                break

            thread_list = get_thread_list(page)
            if not thread_list:
                eprint(f"  Page {page_num}: no threads found, stopping.")
                break

            eprint(f"  Page {page_num}: {len(thread_list)} thread(s)")
            new_unique_on_page = 0

            for row in thread_list:
                if len(thread_infos) >= args.max_threads or scanned >= args.max_scan:
                    break

                thread_id = row.get("legacyThreadId", "")
                if not thread_id or thread_id in seen_thread_ids:
                    continue
                seen_thread_ids.add(thread_id)
                scanned += 1
                new_unique_on_page += 1

                labels = row.get("labels", [])
                subject = row.get("subject", "(no subject)")
                last_msg_id = row.get("legacyLastMsgId", "")

                should_exclude = any(
                    el.strip() in [l.strip() for l in labels]
                    for el in exclude_labels
                )
                if should_exclude:
                    eprint(f"  SKIP [{scanned}] {subject[:50]}... (excluded label)")
                    skipped_excluded += 1
                    continue

                priority = match_priority(labels, priority_labels)

                info = {
                    "thread_id": thread_id,
                    "subject": subject,
                    "labels": labels,
                    "priority": priority,
                    "senders": row.get("senders", []),
                    "date": row.get("date", ""),
                    "last_msg_id": last_msg_id,
                    "fetched": False,
                }

                if early_stop_triggered or (
                    not args.force and thread_id and not db.thread_needs_fetch(thread_id, last_msg_id)
                ):
                    eprint(f"  SKIP [{scanned}] {subject[:50]}... (unchanged)")
                    thread_infos.append(info)
                    skipped_unchanged += 1
                    if not early_stop_triggered:
                        consecutive_cached += 1
                        if args.early_stop > 0 and consecutive_cached >= args.early_stop:
                            eprint(f"\n  Early stop: {consecutive_cached} consecutive cached threads. "
                                   f"Skipping fetches, continuing scan...")
                            early_stop_triggered = True
                    continue

                consecutive_cached = 0
                thread_infos.append(info)
                threads_to_fetch.append(info)

            if len(thread_infos) >= args.max_threads or scanned >= args.max_scan:
                break
            if new_unique_on_page == 0:
                eprint(f"  Page {page_num}: all threads already seen, stopping.")
                break

            page_num += 1

        stop_reason = ""
        if early_stop_triggered:
            stop_reason = ", early-stopped"
        elif len(thread_infos) >= args.max_threads:
            stop_reason = ", reached max-threads"
        elif scanned >= args.max_scan:
            stop_reason = ", reached scan limit"

        eprint(f"\nPhase 1 complete: {len(thread_infos)} threads "
               f"(excluded: {skipped_excluded}, unchanged: {skipped_unchanged}, "
               f"to-fetch: {len(threads_to_fetch)}{stop_reason})")

        # ── Phase 2+3: Fetch and summarize in pipeline ──
        sum_q: _queue.Queue = _queue.Queue()
        fetched_ids: set = set()
        _sum_error_event = threading.Event()
        _sum_errors: list = []
        worker = threading.Thread(
            target=_summarize_worker, args=(sum_q, DB_PATH, _sum_error_event, _sum_errors), daemon=True,
        )
        worker.start()
        eprint(f"\nPhase 2: Fetching {len(threads_to_fetch)} thread(s) "
               f"(summarization pipelined in background)...")

        for idx, info in enumerate(threads_to_fetch, 1):
            thread_id = info["thread_id"]
            subject = info["subject"]
            last_msg_id = info.get("last_msg_id", "")
            priority = info.get("priority")
            labels = info.get("labels", [])
            priority_tag = f" [{priority}]" if priority else ""
            eprint(f"[Fetching {idx}/{len(threads_to_fetch)}] {subject[:55]}...{priority_tag} (summarization pending)")
            print(f"[Fetching {idx}/{len(threads_to_fetch)}] {subject}{priority_tag} (summarization pending)", flush=True)

            if not navigate_to_thread(page, thread_id):
                eprint(f"  WARN: Could not load thread {thread_id}, retrying...")
                time.sleep(2)
                if not navigate_to_thread(page, thread_id):
                    eprint(f"  WARN: Thread {thread_id} failed to load after retry, skipping.")
                    print(f"[Fetch failed {idx}/{len(threads_to_fetch)}] Thread {thread_id} - skipped after retry", flush=True)
                    continue

            thread_subject = get_thread_subject(page) or subject
            messages = extract_thread_messages(page)
            eprint(f"  -> {len(messages)} message(s)")

            new_count = cache_thread_messages(
                db, thread_id, thread_subject, messages, labels, priority
            )
            if new_count > 0:
                eprint(f"  -> {new_count} new message(s) cached")
            else:
                eprint(f"  -> all messages already cached")
            db.upsert_thread_meta(thread_id, last_msg_id)

            info["subject"] = thread_subject
            info["fetched"] = True
            info["_sum_total"] = len(thread_infos)
            fetched_ids.add(thread_id)
            sum_q.put(info)
            eprint(f"[Fetched {idx}/{len(threads_to_fetch)}] {thread_subject[:60]} - queued for summarization")
            print(f"[Fetched {idx}/{len(threads_to_fetch)}] {thread_subject[:60]} - queued for summarization (pipeline running)", flush=True)

        eprint(f"\nQueuing {len(thread_infos) - len(fetched_ids)} unchanged threads for summarization...")
        for info in thread_infos:
            if info["thread_id"] not in fetched_ids:
                info["_sum_total"] = len(thread_infos)
                sum_q.put(info)

        sum_q.put(None)
        worker.join()
        if _sum_errors:
            eprint(f"{'='*60}")
            eprint(f"STATUS: COMPLETED WITH ERRORS - Gmail Reader finished ({len(thread_infos)} threads, {len(_sum_errors)} summarization error(s))")
            for err in _sum_errors:
                eprint(f"  ERROR: {err}")
            eprint(f"{'='*60}")
            print(
                f"\n{'='*60}\n"
                f"[gmail_reader] DONE WITH ERRORS - {len(_sum_errors)} thread(s) failed summarization.\n"
                f"Check gmail-debug.log for details. Other {len(thread_infos) - len(_sum_errors)} threads completed.\n"
                f"{'='*60}\n",
                flush=True,
            )
        else:
            eprint(f"{'='*60}")
            eprint(f"STATUS: COMPLETED - Gmail Reader pipeline finished successfully ({len(thread_infos)} threads)")
            eprint(f"{'='*60}")
        print(
            f"\n{'='*60}\n"
            f"[gmail_reader] ALL DONE - output file is ready for use.\n"
            f"Fetched: {len(fetched_ids)} thread(s) | total scanned: {len(thread_infos)}\n"
            f"{'='*60}\n",
            flush=True,
        )

    except Exception as e:
        eprint(f"{'='*60}")
        eprint(f"STATUS: FAILED - Gmail Reader encountered an error: {e}")
        eprint(f"{'='*60}")
        import traceback
        traceback.print_exc(file=_debug_file)
        print(f"\n[gmail_reader] FAILED with error: {e}\n", flush=True)
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
        if _output_file and _output_file is not sys.stdout:
            _output_file.close()
        if _debug_file and _debug_file is not sys.stderr:
            _debug_file.close()


if __name__ == "__main__":
    main()
