#!/usr/bin/env python3
"""
Google Chat Thread Reader
=========================
Connects to a remote Chrome instance via Chrome DevTools Protocol (CDP),
navigates Google Chat Home view, and extracts recent chat conversations.

Flow:
1. Navigate to chat.google.com Home view
2. Snapshot Home feed items (sorted by recency)
3. Filter conversations with activity within --days
4. For each feed item:
   a. Scroll feed item into view, click to open in right panel
   b. Wait for conversation change (new topic IDs)
   c. Expand collapsed sections ("Show more")
   d. Scroll right panel to bottom, then up for date range
   e. Extract messages (sender, timestamp, body, links)
5. If 0 messages load, return to Home and retry/skip

Output: Minified JSON array to stdout. Progress/debug to stderr.

Requires: playwright (pip install playwright)
"""

import argparse
import json
import sys
import time
from datetime import datetime, timedelta, timezone

from playwright.sync_api import sync_playwright, TimeoutError as PwTimeout


DEFAULT_CDP = "http://192.168.1.11:9223"
GCHAT_URL = "https://chat.google.com/app/home"

HOME_FEED_ITEM = 'span[role="listitem"][data-group-id][data-is-unread]'
MSG_CONTAINER_ALL = "c-wiz[data-topic-id]"


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def connect_browser(cdp_url: str):
    eprint(f"Connecting to Chrome at {cdp_url}...")
    pw = sync_playwright().start()
    browser = pw.chromium.connect_over_cdp(cdp_url)
    eprint(f"Connected. Browser version: {browser.version}")

    contexts = browser.contexts
    context = contexts[0] if contexts else browser.new_context()
    pages = context.pages
    eprint(f"Found {len(pages)} open tab(s)")

    chat_page = None
    for p in pages:
        if "chat.google.com" in p.url:
            chat_page = p
            eprint(f"Reusing existing Google Chat tab: {p.url[:80]}")
            break

    if not chat_page:
        eprint("No Google Chat tab found. Opening new tab...")
        chat_page = context.new_page()

    return pw, browser, chat_page


def navigate_to_home(page):
    current = page.url
    if "/app/home" not in current:
        eprint("Navigating to Google Chat Home...")
        page.goto(GCHAT_URL, wait_until="domcontentloaded", timeout=30000)
    else:
        eprint(f"Already on Home view: {current[:80]}")

    time.sleep(4)

    try:
        page.wait_for_selector(HOME_FEED_ITEM, timeout=15000)
        eprint("Home feed loaded.")
    except PwTimeout:
        eprint("WARN: Home feed items not found within 15s.")


def snapshot_home_feed(page, cutoff_ms: int) -> list[dict]:
    """Take a snapshot of Home feed items with activity within cutoff.

    Stores display_ts and group_id for each item. The index is the DOM
    position at snapshot time; we re-locate items by group_id + display_ts
    when clicking to handle live feed changes.
    """
    return page.evaluate("""
    ({selector, cutoffMs}) => {
        const items = document.querySelectorAll(selector);
        const feed = [];

        for (let i = 0; i < items.length; i++) {
            const el = items[i];
            const groupId = el.getAttribute("data-group-id") || "";
            const displayTs = parseInt(el.getAttribute("data-display-timestamp") || "0", 10);

            if (cutoffMs > 0 && displayTs < cutoffMs) continue;

            const nameEl = el.querySelector("div.Vb5pDe");
            let name = "";
            if (nameEl) {
                for (const node of nameEl.childNodes) {
                    if (node.nodeType === 3) name += node.textContent;
                }
                name = name.trim();
            }
            if (!name) name = groupId;

            feed.push({
                group_id: groupId,
                display_ts: displayTs,
                name: name,
            });
        }

        return feed;
    }
    """, {"selector": HOME_FEED_ITEM, "cutoffMs": cutoff_ms})


def scroll_home_feed_to_item(page, group_id: str, display_ts: int) -> bool:
    """Find a Home feed item by group_id+display_ts, scroll into view, click.

    Uses page.evaluate only to scroll into view, then Playwright's native
    .click() for real mouse event dispatch (JS .click() doesn't trigger
    GChat's framework event handlers reliably).
    """
    try:
        page.evaluate("""
        ({selector, groupId, displayTs}) => {
            const items = document.querySelectorAll(selector);
            for (const item of items) {
                const gid = item.getAttribute("data-group-id") || "";
                const ts = parseInt(item.getAttribute("data-display-timestamp") || "0", 10);
                if (gid === groupId && ts === displayTs) {
                    item.scrollIntoView({block: "center", behavior: "instant"});
                    return true;
                }
            }
            return false;
        }
        """, {"selector": HOME_FEED_ITEM, "groupId": group_id, "displayTs": display_ts})
    except Exception:
        return False

    time.sleep(0.5)

    selector = f'{HOME_FEED_ITEM}[data-group-id="{group_id}"]'
    try:
        loc = page.locator(selector)
        if loc.count() == 0:
            return False
        if loc.count() == 1:
            loc.click(timeout=5000)
        else:
            for idx in range(loc.count()):
                ts_attr = loc.nth(idx).get_attribute("data-display-timestamp")
                if ts_attr and int(ts_attr) == display_ts:
                    loc.nth(idx).click(timeout=5000)
                    break
            else:
                loc.first.click(timeout=5000)
        time.sleep(2)
        return True
    except Exception as e:
        eprint(f"  WARN: click error: {e}")
        time.sleep(3)
        return "/app/home" not in page.url or True


def scroll_home_panel_down(page):
    """Scroll the Home feed panel down to reveal more items."""
    page.evaluate("""
    () => {
        const items = document.querySelectorAll('span[role="listitem"][data-group-id]');
        if (items.length === 0) return;
        const container = items[0].closest("div");
        let el = container;
        while (el && el !== document.body) {
            if (el.scrollHeight > el.clientHeight + 50 && el.clientHeight > 200) {
                el.scrollTop += 400;
                return;
            }
            el = el.parentElement;
        }
    }
    """)
    time.sleep(1)


def get_current_topic_ids(page) -> set:
    try:
        ids = page.evaluate(f"""
        () => {{
            const msgs = document.querySelectorAll("{MSG_CONTAINER_ALL}");
            return Array.from(msgs).map(m => m.getAttribute("data-topic-id")).filter(Boolean);
        }}
        """)
        return set(ids)
    except Exception:
        return set()


def wait_for_conversation_change(page, old_topic_ids: set, timeout_s: int = 30) -> int:
    """Wait until new topic IDs appear (conversation changed) or messages load.

    Handles page navigation (context destruction) by waiting for the page
    to stabilize and then checking for message containers.
    """
    for attempt in range(timeout_s // 2):
        time.sleep(2)
        try:
            current = page.evaluate(f"""
            () => {{
                const msgs = document.querySelectorAll("{MSG_CONTAINER_ALL}");
                return {{
                    count: msgs.length,
                    ids: Array.from(msgs).slice(0, 5).map(m => m.getAttribute("data-topic-id")).filter(Boolean),
                }};
            }}
            """)
        except Exception:
            time.sleep(2)
            continue

        count = current["count"]
        new_ids = set(current["ids"])

        if count == 0:
            continue

        if not old_topic_ids:
            return count

        if new_ids and not new_ids.issubset(old_topic_ids):
            return count

    try:
        return page.evaluate(f'() => document.querySelectorAll("{MSG_CONTAINER_ALL}").length')
    except Exception:
        return 0


# --- Right panel scrolling (ancestor-of-message approach) ---

SCROLL_BOTTOM_JS = """
() => {
    const msg = document.querySelector("c-wiz[data-topic-id]");
    if (!msg) return false;
    let el = msg.parentElement;
    while (el && el !== document.body) {
        if (el.scrollHeight > el.clientHeight + 50 && el.clientHeight > 100) {
            el.scrollTop = el.scrollHeight;
            return true;
        }
        el = el.parentElement;
    }
    return false;
}
"""

SCROLL_UP_JS = """
() => {
    const msg = document.querySelector("c-wiz[data-topic-id]");
    if (!msg) return false;
    let el = msg.parentElement;
    while (el && el !== document.body) {
        if (el.scrollHeight > el.clientHeight + 50 && el.clientHeight > 100) {
            const before = el.scrollTop;
            el.scrollTop = Math.max(0, el.scrollTop - 800);
            return el.scrollTop !== before;
        }
        el = el.parentElement;
    }
    return false;
}
"""


def scroll_to_bottom(page):
    page.evaluate(SCROLL_BOTTOM_JS)
    time.sleep(1.5)


def scroll_up_for_date_range(page, cutoff_ms: int, max_scrolls: int = 20):
    for i in range(max_scrolls):
        oldest_ms = page.evaluate(f"""
        () => {{
            const msgs = document.querySelectorAll("{MSG_CONTAINER_ALL}");
            if (msgs.length === 0) return 0;
            return parseInt(msgs[0].getAttribute("data-local-sort-time-msec") || "0", 10);
        }}
        """)

        if oldest_ms > 0 and oldest_ms <= cutoff_ms:
            eprint(f"  Reached cutoff date after {i} scroll(s)")
            return

        scrolled = page.evaluate(SCROLL_UP_JS)

        if not scrolled:
            eprint(f"  Reached top after {i} scroll(s)")
            return

        time.sleep(1)

    eprint(f"  Stopped scrolling after {max_scrolls} scrolls")


# --- Message extraction ---

def expand_collapsed_sections(page):
    """Click all 'Show more' buttons in the right panel to reveal hidden content."""
    page.evaluate("""
    () => {
        const buttons = document.querySelectorAll("button, [role='button'], span[role='button']");
        for (const btn of buttons) {
            const t = btn.textContent.trim().toLowerCase();
            if (t === "show more" || t === "see more") {
                try { btn.click(); } catch(e) {}
            }
        }
    }
    """)
    time.sleep(0.5)


def expand_thread_replies(page):
    """Click all collapsed 'N replies' bars in the right panel to expand them in-place.

    GChat threads show 'N replies' as a horizontal bar/divider between the
    parent message and its replies. Clicking this bar expands the replies
    inline (accordion-style) — no navigation occurs. After expansion, new
    c-wiz[data-topic-id] message containers appear in the DOM and will be
    captured by extract_messages.

    Scoped to the right panel via the message scroll container. Uses
    page.mouse.click() on button center coordinates to avoid accidentally
    clicking elements in the Home feed panel.
    """
    before_count = page.evaluate(f'() => document.querySelectorAll("{MSG_CONTAINER_ALL}").length')

    buttons = page.evaluate("""
    () => {
        const msgContainer = document.querySelector("c-wiz[data-topic-id]");
        if (!msgContainer) return [];

        let scrollParent = msgContainer.parentElement;
        while (scrollParent && scrollParent !== document.body) {
            if (scrollParent.scrollHeight > scrollParent.clientHeight + 50 &&
                scrollParent.clientHeight > 100) break;
            scrollParent = scrollParent.parentElement;
        }
        if (!scrollParent || scrollParent === document.body) return [];

        const results = [];
        const candidates = scrollParent.querySelectorAll("[role='button'], button");
        for (const el of candidates) {
            const t = el.textContent.trim();
            if (/[0-9]+ repl(y|ies)/i.test(t) && t.length < 100) {
                const rect = el.getBoundingClientRect();
                if (rect.width > 20 && rect.height > 10) {
                    el.scrollIntoView({block: "center", behavior: "instant"});
                    const r2 = el.getBoundingClientRect();
                    results.push({
                        x: Math.round(r2.left + r2.width / 2),
                        y: Math.round(r2.top + r2.height / 2),
                        text: t.substring(0, 60),
                    });
                }
            }
        }
        return results;
    }
    """)

    if not buttons:
        return

    clicked = 0
    max_expand = 5
    for btn in buttons[:max_expand]:
        try:
            page.mouse.click(btn["x"], btn["y"])
            clicked += 1
            time.sleep(1.5)
        except Exception:
            pass

    if clicked > 0:
        time.sleep(1)
        after_count = page.evaluate(f'() => document.querySelectorAll("{MSG_CONTAINER_ALL}").length')
        new_msgs = after_count - before_count
        eprint(f"  Expanded {clicked} reply bar(s) ({new_msgs} new messages)")


def extract_messages(page, cutoff_ms: int) -> list[dict]:
    """Extract messages from the right panel within the date range.

    Walks ALL text nodes inside div[role='group']. Also captures:
    - Rich content: card text, monitor queries, document comments
    - Link URLs: all <a href> not already in body
    - Bot/app sender via span.nzVtF fallback
    - Handles 'Show more' pre-expanded content
    """
    return page.evaluate("""
    (cutoffMs) => {
        const containers = document.querySelectorAll('c-wiz[data-topic-id][data-is-user-topic="true"]');
        const messages = [];

        const NOISE_CLASSES = [
            "FvYVyf", "njhDLd", "cPjwNc", "GOoeGd", "Lphf0c",
            "nzVtF", "ZTmjQb", "w692Zc", "TmhmK",
            "ne2Ple-oshW8e-V67aGc",
        ];
        const NOISE_TEXTS = [
            "End Quote", "Quoted", "Sent by",
            "Add reaction", "Show more", "See more",
        ];

        for (const msg of containers) {
            const sortTimeMs = parseInt(msg.getAttribute("data-local-sort-time-msec") || "0", 10);
            if (cutoffMs > 0 && sortTimeMs < cutoffMs) continue;

            let sender = "";
            const senderEl = msg.querySelector("span[data-member-id][data-name]");
            if (senderEl) sender = senderEl.getAttribute("data-name");
            if (!sender) {
                const nameSpan = msg.querySelector("span.nzVtF");
                if (nameSpan) sender = nameSpan.textContent.trim();
            }

            let displayTime = "";
            const timeEl = msg.querySelector("span.FvYVyf");
            if (timeEl) displayTime = timeEl.textContent.trim();

            const group = msg.querySelector("div[role='group']");
            const bodyParts = [];
            const quotedParts = [];

            if (group) {
                const walker = document.createTreeWalker(group, NodeFilter.SHOW_TEXT, null, false);
                while (walker.nextNode()) {
                    const t = walker.currentNode.textContent.trim();
                    if (!t) continue;

                    const parent = walker.currentNode.parentElement;
                    if (!parent) continue;

                    const cls = parent.getAttribute("class") || "";
                    const role = parent.getAttribute("role") || "";

                    if (role === "tooltip" || role === "presentation") continue;

                    let isNoise = false;
                    for (const nc of NOISE_CLASSES) {
                        if (cls.includes(nc)) { isNoise = true; break; }
                    }
                    if (isNoise) continue;

                    for (const nt of NOISE_TEXTS) {
                        if (t === nt || t.startsWith("press L to")) { isNoise = true; break; }
                    }
                    if (isNoise) continue;

                    if (cls.includes("J87oZd")) {
                        quotedParts.push(t);
                    } else {
                        bodyParts.push(t);
                    }
                }

                // Also capture text from buttons that contain useful action text
                const buttons = group.querySelectorAll("button, [role='button']");
                for (const btn of buttons) {
                    const t = btn.textContent.trim();
                    if (t && t.length > 2 && t.length < 80) {
                        const lower = t.toLowerCase();
                        if (lower === "reply" || lower === "add reaction" ||
                            lower === "show more" || lower === "see more" ||
                            lower === "resolve") continue;
                        if (!bodyParts.includes(t)) bodyParts.push(t);
                    }
                }
            }

            let body = bodyParts.join("\\n").trim();
            if (quotedParts.length > 0) {
                body += "\\n[quoted] " + quotedParts.join("\\n");
            }

            if (group) {
                const anchors = group.querySelectorAll("a[href]");
                const urls = [];
                for (const a of anchors) {
                    const href = a.getAttribute("href") || "";
                    if (href && !href.startsWith("mailto:") && !href.startsWith("javascript:") && !body.includes(href)) {
                        urls.push(href);
                    }
                }
                if (urls.length > 0) {
                    body += "\\n[links] " + [...new Set(urls)].join(" ");
                }
            }

            if (body.length > 5000) body = body.substring(0, 5000) + "... [truncated]";
            body = body.replace(/\\n{3,}/g, "\\n\\n");

            if (!body && !sender) continue;

            messages.push({
                sender: sender || "Unknown",
                timestamp: displayTime,
                epoch_ms: sortTimeMs,
                body: body,
            });
        }

        return messages;
    }
    """, cutoff_ms)


def debug_dom(page):
    eprint("\n=== DEBUG DOM ===")
    eprint(f"URL: {page.url}")

    items = page.evaluate("""
    (selector) => {
        const items = document.querySelectorAll(selector);
        const result = [];
        for (let i = 0; i < Math.min(10, items.length); i++) {
            const el = items[i];
            result.push({
                group_id: el.getAttribute("data-group-id"),
                display_ts: el.getAttribute("data-display-timestamp"),
                is_unread: el.getAttribute("data-is-unread"),
                text: el.textContent.trim().substring(0, 150),
            });
        }
        return result;
    }
    """, HOME_FEED_ITEM)

    eprint(f"Home feed items: {len(items)}")
    for item in items:
        eprint(f"  [{item['group_id'][:30]}] ts={item['display_ts']} unread={item['is_unread']} {item['text'][:80]}")
    eprint("=== END DEBUG ===\n")


def main():
    parser = argparse.ArgumentParser(
        description="Read Google Chat conversations via remote Chrome DevTools Protocol"
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
        help="Max conversations to read (default: 20)"
    )
    parser.add_argument(
        "--max-scan", type=int, default=100,
        help="Max Home feed items to scan. Safety cap (default: 100)"
    )
    parser.add_argument(
        "--max-scroll", type=int, default=20,
        help="Max scroll-up iterations per thread to load older messages (default: 20)"
    )
    parser.add_argument(
        "--format", choices=["json", "yaml"], default="json",
        help="Output format (default: json)"
    )
    parser.add_argument(
        "--debug-dom", action="store_true",
        help="Dump Home feed DOM to stderr and exit"
    )
    args = parser.parse_args()

    cutoff_dt = datetime.now(timezone.utc) - timedelta(days=args.days)
    cutoff_ms = int(cutoff_dt.timestamp() * 1000)

    pw = None
    browser = None
    try:
        pw, browser, page = connect_browser(args.cdp_url)
        navigate_to_home(page)

        if args.debug_dom:
            debug_dom(page)
            sys.exit(0)

        feed = snapshot_home_feed(page, cutoff_ms)
        eprint(f"Snapshot: {len(feed)} feed item(s) within last {args.days} day(s)")

        if not feed:
            eprint("FATAL: 0 Home feed items found — DOM parsing issue. "
                   "Run with --debug-dom to inspect.")
            sys.exit(2)

        threads = []
        scan_limit = min(len(feed), args.max_scan)
        skipped = 0

        eprint(f"\nProcessing (target: {args.max_threads}, feed items: {scan_limit})...\n")

        for i in range(scan_limit):
            if len(threads) >= args.max_threads:
                break

            item = feed[i]
            name = item["name"]
            gid = item["group_id"]
            dts = item["display_ts"]
            current_count = len(threads) + 1
            conv_url = f"https://chat.google.com/{gid}"
            eprint(f"[{current_count}/{args.max_threads}] {name[:55]}...")

            old_ids = get_current_topic_ids(page)

            clicked = scroll_home_feed_to_item(page, gid, dts)
            if not clicked:
                scroll_home_panel_down(page)
                time.sleep(1)
                clicked = scroll_home_feed_to_item(page, gid, dts)

            if not clicked:
                eprint(f"  WARN: Feed item not found in DOM, skipping")
                skipped += 1
                continue

            msg_count = wait_for_conversation_change(page, old_ids, timeout_s=20)

            if msg_count == 0:
                eprint(f"  WARN: 0 messages loaded — returning to Home to retry")
                navigate_to_home(page)
                skipped += 1
                continue

            eprint(f"  {msg_count} message container(s) loaded")

            expand_collapsed_sections(page)
            expand_thread_replies(page)

            if args.max_scroll > 0:
                scroll_to_bottom(page)
                scroll_up_for_date_range(page, cutoff_ms, max_scrolls=args.max_scroll)
                expand_thread_replies(page)

            expand_collapsed_sections(page)

            conv_name = name or gid
            messages = extract_messages(page, cutoff_ms)
            eprint(f"  -> {len(messages)} message(s) within last {args.days} day(s)")

            if messages:
                threads.append({
                    "name": conv_name,
                    "url": conv_url,
                    "message_count": len(messages),
                    "messages": messages,
                })
            else:
                eprint(f"  SKIP: No messages within date range")
                skipped += 1

            if "/app/home" not in page.url:
                eprint("  Returning to Home view...")
                navigate_to_home(page)

        eprint(f"\nDone. Extracted {len(threads)} conversation(s), skipped: {skipped}")

        if args.format == "yaml":
            import yaml
            print(yaml.dump(threads, default_flow_style=False, allow_unicode=True, sort_keys=False))
        else:
            print(json.dumps(threads, separators=(",", ":"), ensure_ascii=False))

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
