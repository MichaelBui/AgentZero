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
import sys
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
DB_PATH = Path(__file__).resolve().parent.parent / "data" / "gmail_cache.db"


def eprint(*a, **kw):
    print(*a, file=sys.stderr, **kw)


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


def go_back_to_search(page):
    page.go_back(wait_until="domcontentloaded", timeout=15000)
    time.sleep(2)
    try:
        page.wait_for_selector('div[role="main"] tr[jscontroller]', timeout=10000)
    except PwTimeout:
        eprint("  WARN: Grid not found after back, waiting more...")
        time.sleep(3)


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

def _print_output(thread_id: str, subject: str, summary_text: str,
                  labels: list, priority: str | None, senders: list, date: str):
    """Print a single thread's output in streaming format."""
    label_str = ", ".join(labels) if labels else "None"
    priority_str = priority or "None"
    sender_names = ", ".join(s.get("name", s.get("email", "")) for s in senders) if senders else "Unknown"

    print(f"## gmail/{thread_id}: {subject}", flush=True)
    print(
        f"Source: gmail | Thread: {thread_id} | Labels: {label_str} | "
        f"Priority: {priority_str} | Senders: {sender_names} | Last Date: {date}",
        flush=True,
    )
    print(summary_text, flush=True)


def summarize_and_output(db: SkillDB, thread_info: dict):
    """Summarize a single thread and stream output immediately."""
    thread_id = thread_info["thread_id"]
    subject = thread_info["subject"]
    labels = thread_info.get("labels", [])
    priority = thread_info.get("priority")
    senders = thread_info.get("senders", [])
    date = thread_info.get("date", "")
    last_msg_id = thread_info.get("last_msg_id", "")

    if not db.needs_resummarize(thread_id):
        existing = db.get_resource_summary(thread_id)
        if existing:
            eprint(f"  [{subject[:40]}]: using cached summary")
            _print_output(thread_id, subject, existing["summary"], labels, priority, senders, date)
            return

    items = db.get_atomic_for_resource(thread_id)
    if not items:
        eprint(f"  [{subject[:40]}]: no cached messages, skipping summary")
        return

    existing_summary = db.get_resource_summary(thread_id)
    existing_text = existing_summary["summary"] if existing_summary else None

    if existing_text and existing_summary:
        summarized_at = existing_summary.get("summarized_at", "")
        new_items = db.get_items_since(thread_id, summarized_at) if summarized_at else items
        if new_items:
            items_to_summarize = new_items
        else:
            items_to_summarize = items
    else:
        items_to_summarize = items

    meta = {"labels": labels, "priority": priority, "last_message_id": last_msg_id}

    eprint(f"  [{subject[:40]}]: summarizing ({len(items_to_summarize)} messages)...")
    summary_text = summarize_resource(
        title=subject,
        source_type="Email thread",
        atomic_items=items_to_summarize,
        metadata=meta,
        existing_summary=existing_text,
    )

    if summary_text:
        db.upsert_summary(thread_id, "gmail", subject, summary_text, meta)
        _print_output(thread_id, subject, summary_text, labels, priority, senders, date)
    elif existing_text:
        _print_output(thread_id, subject, existing_text, labels, priority, senders, date)


# ── Main ────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Read Gmail email threads via CDP, cache, and summarize"
    )
    parser.add_argument("--cdp-url", default=DEFAULT_CDP,
                        help=f"Chrome DevTools endpoint (default: {DEFAULT_CDP})")
    parser.add_argument("--days", type=int, default=3,
                        help="Days to look back (default: 3)")
    parser.add_argument("--max-threads", type=int, default=20,
                        help="Max threads to read (default: 20)")
    parser.add_argument("--max-scan", type=int, default=100,
                        help="Max total threads to scan (default: 100)")
    parser.add_argument("--exclude-labels", default=DEFAULT_EXCLUDE,
                        help="JSON array of labels to exclude")
    parser.add_argument("--priority-labels", default=DEFAULT_PRIORITY,
                        help="JSON array of priority labels, highest first")
    parser.add_argument("--force", action="store_true",
                        help="Bypass change detection, re-fetch and re-summarize all")
    args = parser.parse_args()

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

    db = get_gmail_db(DB_PATH)
    pw = browser = None

    try:
        pw, browser, page = connect_browser(args.cdp_url)
        navigate_to_search(page, args.days)

        thread_list = get_thread_list(page)
        eprint(f"Found {len(thread_list)} thread(s) in search results")
        if not thread_list:
            eprint("FATAL: 0 threads found - Gmail DOM selectors may need updating.")
            sys.exit(2)

        thread_infos = []
        total_rows = min(len(thread_list), args.max_scan)
        row_idx = 0
        skipped_excluded = 0
        skipped_unchanged = 0

        eprint(f"\nProcessing threads (target: {args.max_threads}, scan limit: {args.max_scan})...")

        while len(thread_infos) < args.max_threads and row_idx < total_rows:
            row = thread_list[row_idx]
            labels = row.get("labels", [])
            subject = row.get("subject", "(no subject)")
            thread_id = row.get("legacyThreadId", "")
            last_msg_id = row.get("legacyLastMsgId", "")

            should_exclude = any(
                el.strip() in [l.strip() for l in labels]
                for el in exclude_labels
            )
            if should_exclude:
                eprint(f"  SKIP [{row_idx+1}] {subject[:50]}... (excluded label)")
                row_idx += 1
                skipped_excluded += 1
                continue

            priority = match_priority(labels, priority_labels)

            if not args.force and thread_id and not db.thread_needs_fetch(thread_id, last_msg_id):
                eprint(f"  SKIP [{row_idx+1}] {subject[:50]}... (unchanged, last_msg_id match)")
                thread_infos.append({
                    "thread_id": thread_id,
                    "subject": subject,
                    "labels": labels,
                    "priority": priority,
                    "senders": row.get("senders", []),
                    "date": row.get("date", ""),
                    "last_msg_id": last_msg_id,
                    "fetched": False,
                })
                row_idx += 1
                skipped_unchanged += 1
                continue

            current_count = len(thread_infos) + 1
            priority_tag = f" [{priority}]" if priority else ""
            eprint(f"[{current_count}/{args.max_threads}] {subject[:55]}...{priority_tag}")

            click_thread_row(page, row["rowIndex"])
            if not wait_for_thread_view(page):
                eprint(f"  Retrying thread click...")
                go_back_to_search(page)
                time.sleep(1)
                updated = get_thread_list(page)
                if row_idx < len(updated):
                    thread_list = updated
                    total_rows = min(len(updated), args.max_scan)
                    click_thread_row(page, updated[row_idx]["rowIndex"])
                    if not wait_for_thread_view(page):
                        eprint(f"  WARN: Thread view did not load after retry, skipping...")
                        go_back_to_search(page)
                        row_idx += 1
                        continue

            thread_subject = get_thread_subject(page) or subject
            messages = extract_thread_messages(page)
            eprint(f"  -> {len(messages)} message(s)")

            new_count = cache_thread_messages(db, thread_id, thread_subject, messages, labels, priority)
            if new_count > 0:
                eprint(f"  -> {new_count} new message(s) cached")
            else:
                eprint(f"  -> all messages already cached")

            thread_infos.append({
                "thread_id": thread_id,
                "subject": thread_subject,
                "labels": labels,
                "priority": priority,
                "senders": row.get("senders", []),
                "date": row.get("date", ""),
                "last_msg_id": last_msg_id,
                "fetched": True,
            })

            go_back_to_search(page)
            row_idx += 1
            if len(thread_infos) < args.max_threads and row_idx < total_rows:
                updated = get_thread_list(page)
                if updated:
                    thread_list = updated
                    total_rows = min(len(updated), args.max_scan)

        eprint(f"\nProcessed: {len(thread_infos)} threads "
               f"(excluded: {skipped_excluded}, unchanged: {skipped_unchanged})")

        eprint(f"\nSummarizing and streaming output for {len(thread_infos)} threads...")
        for info in thread_infos:
            summarize_and_output(db, info)

    except Exception as e:
        eprint(f"ERROR: {e}")
        import traceback
        traceback.print_exc(file=sys.stderr)
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
