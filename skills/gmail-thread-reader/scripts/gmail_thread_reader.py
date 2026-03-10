#!/usr/bin/env python3
"""
Gmail Thread Reader
===================
Connects to a remote Chrome instance via Chrome DevTools Protocol (CDP),
navigates Gmail, and extracts recent email thread conversations.

Features:
- Exclusion labels: skip threads with specific labels (e.g., "❌ ai-exclusion")
- Priority labels: tag threads with priority level based on label matching
- Full message extraction: from, to, cc, date, body, labels

Output: JSON array of thread objects to stdout.
Progress/debug: stderr.

Requires: playwright (pip install playwright)
"""

import argparse
import json
import sys
import time

from playwright.sync_api import sync_playwright, TimeoutError as PwTimeout


DEFAULT_CDP = "http://192.168.1.11:9223"
GMAIL_BASE = "https://mail.google.com"

DEFAULT_EXCLUDE = '["❌ ai-exclusion", "🪣 Bitbucket"]'
DEFAULT_PRIORITY = '["⚠️IMPORTANT", "❗️ ASAP  🏃‍♂️‍➡️", "🔜 Soon 🚶‍♂️‍➡️", "👀 KIV 🧘‍♂️", "📝 Noted"]'


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def connect_browser(cdp_url: str):
    """Connect to remote Chrome via CDP. Returns (playwright, browser, page)."""
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
            eprint(f"Reusing existing Gmail tab")
            break

    if not gmail_page:
        eprint("No Gmail tab found. Opening new tab...")
        gmail_page = context.new_page()

    return pw, browser, gmail_page


def navigate_to_search(page, days: int):
    """Navigate to Gmail search filtered to last N days."""
    search_url = f"{GMAIL_BASE}/mail/u/0/#search/newer_than%3A{days}d"
    eprint(f"Navigating to Gmail (last {days} days)...")
    page.goto(search_url, wait_until="domcontentloaded", timeout=30000)
    time.sleep(4)
    page.wait_for_selector('div[role="main"] tr[jscontroller]', timeout=15000)
    eprint("Gmail search results loaded.")


def get_thread_list(page) -> list[dict]:
    """Extract thread summary rows with labels from Gmail search results."""
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

            // Sender from span[email] (deduplicated)
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

            // Subject from span.bog
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

            // Snippet
            const snippetEl = tds[5].querySelector('span.y2');
            const snippet = snippetEl ? snippetEl.textContent.trim().replace(/^\\s*-\\s*/, '') : '';

            // Date from td[8]
            const dateSpan = tds[8].querySelector('span[title]');
            const date = dateSpan ? dateSpan.getAttribute('title') : tds[8].textContent.trim();

            // Labels from div.at[title] in td[5]
            const labelEls = tds[5].querySelectorAll('div.at');
            const labels = [];
            for (const l of labelEls) {
                labels.push(l.getAttribute('title') || l.textContent.trim());
            }

            threads.push({
                rowIndex: i,
                senders,
                subject,
                snippet: snippet.substring(0, 120),
                date,
                labels,
            });
        }
        return threads;
    }
    """)


def click_thread_row(page, row_index: int):
    """Click on a thread row to open the thread."""
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
    """Wait for thread view to load. Returns True if loaded."""
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
    """Poll until the number of visible [data-message-id] elements stabilizes."""
    prev_count = 0
    stable_rounds = 0
    elapsed = 0.0
    while elapsed < max_wait:
        count = page.evaluate(
            "() => document.querySelectorAll('[data-message-id]').length"
        )
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
    """Expand ALL messages using Gmail's built-in 'Expand all' button, then
    reveal To/CC details and trimmed quoted content for each message."""

    # Step 1: Click Gmail's "Expand all" toolbar button if present
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
    else:
        eprint("  No 'Expand all' button (single-message thread)")

    # Step 2: Click "show details" arrows to reveal To/CC for each message
    page.evaluate("""
    () => {
        const detailBtns = document.querySelectorAll(
            'img[aria-label="Show details"], span.ajy, div.ajz'
        );
        for (const btn of detailBtns) { try { btn.click(); } catch(e) {} }
    }
    """)
    time.sleep(1)

    # Step 3: Expand trimmed/quoted content
    page.evaluate("""
    () => {
        const trimmers = document.querySelectorAll('[aria-label="Show trimmed content"]');
        for (const el of trimmers) { try { el.click(); } catch(e) {} }
    }
    """)
    time.sleep(0.5)


def extract_thread_messages(page) -> list[dict]:
    """Extract all messages from the currently open thread view."""
    expand_all_messages(page)

    return page.evaluate("""
    () => {
        const messages = [];
        const msgContainers = document.querySelectorAll('[data-message-id]');

        for (const container of msgContainers) {
            // --- From ---
            const fromEl = container.querySelector('span.gD[email]');
            let sender = 'Unknown';
            if (fromEl) {
                const name = fromEl.getAttribute('name') || fromEl.textContent.trim();
                const email = fromEl.getAttribute('email') || '';
                sender = email ? name + ' <' + email + '>' : name;
            }

            // --- Date ---
            let date = '';
            const dateEl = container.querySelector('span.g3[title]');
            if (dateEl) {
                date = dateEl.getAttribute('title') || dateEl.textContent.trim();
            }
            if (!date) {
                const fallbackDate = container.querySelectorAll('span[title]');
                for (const d of fallbackDate) {
                    const title = d.getAttribute('title') || '';
                    if (title.match(/\\d{1,2},?\\s*\\d{4}/)) { date = title; break; }
                }
            }

            // --- To / CC ---
            // Collect all email spans; first span.gD is "from", rest are recipients
            const allEmailSpans = container.querySelectorAll('span[email]');
            const fromEmail = fromEl ? fromEl.getAttribute('email') : '';
            const toList = [];
            const ccList = [];
            let foundFrom = false;

            // Strategy: look for explicit "to"/"cc" header rows in expanded view
            const headerRows = container.querySelectorAll('tr.acZ td, div.ajw');
            let inCcSection = false;

            // Check for expanded header with "to:" and "cc:" labels
            const expandedTo = container.querySelectorAll('span.g2');
            const expandedHeaders = container.querySelectorAll('td.gF');

            // Parse the "show details" expanded area if available
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

            // Fallback: if expanded detail not available, collect from span[email]
            if (toList.length === 0 && ccList.length === 0) {
                for (const s of allEmailSpans) {
                    const email = s.getAttribute('email') || '';
                    if (email === fromEmail && !foundFrom) { foundFrom = true; continue; }
                    toList.push({
                        name: s.getAttribute('name') || s.textContent.trim(),
                        email: email
                    });
                }
            }

            // --- Body ---
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
            if (body.length > 5000) body = body.substring(0, 5000) + '... [truncated]';

            messages.push({
                from: sender,
                to: toList,
                cc: ccList,
                date: date,
                body: body,
            });
        }

        // Fallback for different thread structures
        if (messages.length === 0) {
            const msgBlocks = document.querySelectorAll('div.gs');
            for (const block of msgBlocks) {
                const fromEl = block.querySelector('span.gD[email], span[email]');
                const dateEl = block.querySelector('span.g3[title], span[title]');
                const bodyEl = block.querySelector('div.a3s, div[dir="ltr"]');

                if (fromEl || bodyEl) {
                    let sender = 'Unknown';
                    if (fromEl) {
                        sender = (fromEl.getAttribute('name') || fromEl.textContent.trim()) +
                                 ' <' + (fromEl.getAttribute('email') || '') + '>';
                    }
                    messages.push({
                        from: sender,
                        to: [],
                        cc: [],
                        date: dateEl ? (dateEl.getAttribute('title') || dateEl.textContent.trim()) : '',
                        body: bodyEl ? bodyEl.innerText.trim().substring(0, 5000) : '',
                    });
                }
            }
        }

        return messages;
    }
    """)


def get_thread_subject(page) -> str:
    """Extract the subject line from the currently open thread."""
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
    """Navigate back to the search results list."""
    page.go_back(wait_until="domcontentloaded", timeout=15000)
    time.sleep(2)
    try:
        page.wait_for_selector('div[role="main"] tr[jscontroller]', timeout=10000)
    except PwTimeout:
        eprint("  WARN: Grid not found after back, waiting more...")
        time.sleep(3)


def match_priority(labels: list[str], priority_labels: list[str]) -> str | None:
    """Return the highest-priority label that matches, or None."""
    for pl in priority_labels:
        for label in labels:
            if pl.strip() == label.strip():
                return pl.strip()
    return None


def read_threads(page, thread_list: list[dict], max_threads: int,
                 exclude_labels: list[str], priority_labels: list[str]) -> list[dict]:
    """Open each non-excluded thread via click and extract its messages."""
    threads = []
    total_rows = len(thread_list)
    row_idx = 0
    skipped = 0

    eprint(f"\nProcessing threads (target: {max_threads}, total rows: {total_rows})...")
    eprint(f"Exclude labels: {exclude_labels}")
    eprint(f"Priority labels: {priority_labels}\n")

    while len(threads) < max_threads and row_idx < total_rows:
        row = thread_list[row_idx]
        labels = row.get("labels", [])
        subject = row.get("subject", "(no subject)")

        # Check exclusion labels
        should_exclude = any(
            el.strip() in [l.strip() for l in labels]
            for el in exclude_labels
        )

        if should_exclude:
            eprint(f"  SKIP [{row_idx+1}] {subject[:50]}... (excluded label)")
            row_idx += 1
            skipped += 1
            continue

        priority = match_priority(labels, priority_labels)
        current_count = len(threads) + 1
        priority_tag = f" [{priority}]" if priority else ""
        eprint(f"[{current_count}/{max_threads}] {subject[:55]}...{priority_tag}")

        click_thread_row(page, row["rowIndex"])

        if not wait_for_thread_view(page):
            eprint(f"  Retrying thread click...")
            go_back_to_search(page)
            time.sleep(1)
            updated = get_thread_list(page)
            if row_idx < len(updated):
                thread_list = updated
                click_thread_row(page, updated[row_idx]["rowIndex"])
                if not wait_for_thread_view(page):
                    eprint(f"  WARN: Thread view did not load after retry, skipping...")
                    go_back_to_search(page)
                    row_idx += 1
                    continue

        thread_url = page.url
        thread_subject = get_thread_subject(page) or subject
        messages = extract_thread_messages(page)
        eprint(f"  -> {len(messages)} message(s)")

        threads.append({
            "subject": thread_subject,
            "thread_url": thread_url,
            "labels": labels,
            "priority": priority,
            "senders": row.get("senders", []),
            "last_date": row.get("date", ""),
            "messages": messages,
        })

        go_back_to_search(page)

        # Re-fetch list after back navigation (indices may shift)
        row_idx += 1
        if len(threads) < max_threads and row_idx < total_rows:
            updated = get_thread_list(page)
            if len(updated) > 0:
                thread_list = updated
                total_rows = len(updated)

    eprint(f"\nProcessed: {len(threads)} threads, skipped: {skipped} (excluded)")
    return threads


def main():
    parser = argparse.ArgumentParser(
        description="Read Gmail email threads via remote Chrome DevTools Protocol"
    )
    parser.add_argument(
        "--cdp-url", default=DEFAULT_CDP,
        help=f"Chrome DevTools Protocol endpoint (default: {DEFAULT_CDP})"
    )
    parser.add_argument(
        "--days", type=int, default=3,
        help="Number of days to look back (default: 3)"
    )
    parser.add_argument(
        "--max-threads", type=int, default=20,
        help="Max number of threads to read, excluding filtered threads (default: 20)"
    )
    parser.add_argument(
        "--exclude-labels", default=DEFAULT_EXCLUDE,
        help=f"JSON array of labels to exclude (default: {DEFAULT_EXCLUDE})"
    )
    parser.add_argument(
        "--priority-labels", default=DEFAULT_PRIORITY,
        help="JSON array of priority labels, highest first"
    )
    parser.add_argument(
        "--format", choices=["json", "yaml"], default="json",
        help="Output format (default: json)"
    )
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

    pw = None
    browser = None
    try:
        pw, browser, page = connect_browser(args.cdp_url)
        navigate_to_search(page, args.days)

        thread_list = get_thread_list(page)
        eprint(f"Found {len(thread_list)} thread(s) in search results")

        if not thread_list:
            eprint("No email threads found.")
            print("[]")
            return

        threads = read_threads(page, thread_list, args.max_threads,
                               exclude_labels, priority_labels)

        eprint(f"\nDone. Extracted {len(threads)} thread(s).")
        if args.format == "yaml":
            import yaml
            print(yaml.dump(threads, default_flow_style=False, allow_unicode=True, sort_keys=False))
        else:
            print(json.dumps(threads, indent=2, ensure_ascii=False))

    except Exception as e:
        eprint(f"ERROR: {e}")
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
    finally:
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
