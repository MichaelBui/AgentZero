#!/usr/bin/env python3
"""
Google Chat Thread Reader — extracts recent conversations via CDP.

Flow:
1. Navigate to chat.google.com Home view
2. Snapshot Home feed items within date range
3. For each item: click → verify right panel → scroll → extract messages
4. Output JSON to stdout, progress to stderr

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

SEL_FEED = 'span[role="listitem"][data-group-id][data-is-unread]'
SEL_MSG = "c-wiz[data-topic-id]"

# Reusable JS to find the right panel scroll container.
# When topicId is provided, finds the scroll container holding elements with
# that topic ID (the thread panel, which overlays the main conversation).
# Otherwise falls back to the largest scrollable container in the right half.
FIND_PANEL_JS = """
function findPanel(topicId) {
    const mid = window.innerWidth / 3;

    // If we have a topic ID, find the scroll container holding that thread
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

    // Fallback: largest scrollable container in the right half
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


def eprint(*a, **kw):
    print(*a, file=sys.stderr, **kw)


# --- Browser & Navigation ---


def connect_browser(cdp_url):
    eprint(f"Connecting to Chrome at {cdp_url}...")
    pw = sync_playwright().start()
    browser = pw.chromium.connect_over_cdp(cdp_url)
    ctx = browser.contexts[0] if browser.contexts else browser.new_context()
    eprint(f"Connected ({browser.version}), {len(ctx.pages)} tab(s)")

    page = next((p for p in ctx.pages if "chat.google.com" in p.url), None)
    if not page:
        eprint("Opening new Google Chat tab...")
        page = ctx.new_page()
    else:
        eprint(f"Reusing tab: {page.url[:80]}")

    return pw, browser, page


def go_home(page):
    if "/app/home" not in page.url:
        page.goto(GCHAT_URL, wait_until="domcontentloaded", timeout=30000)
    time.sleep(4)
    try:
        page.wait_for_selector(SEL_FEED, timeout=15000)
    except PwTimeout:
        eprint("WARN: Home feed not loaded within 15s")


# --- Home Feed ---


def snapshot_feed(page, cutoff_ms):
    """Snapshot Home feed items with activity within cutoff."""
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
            });
        }
        return feed;
    }""", {"sel": SEL_FEED, "cutoff": cutoff_ms})


def click_feed_item(page, gid, dts):
    """Scroll a Home feed item into view and click it. Returns True on success."""
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
        eprint(f"  WARN: click failed: {e}")
        return False


def scroll_feed_down(page):
    """Scroll the Home feed panel down to reveal more items."""
    page.evaluate("""() => {
        const items = document.querySelectorAll('span[role="listitem"][data-group-id]');
        if (!items.length) return;
        let el = items[0].closest("div");
        while (el && el !== document.body) {
            if (el.scrollHeight > el.clientHeight + 50 && el.clientHeight > 200) {
                el.scrollTop += 400; return;
            }
            el = el.parentElement;
        }
    }""")
    time.sleep(1)


# --- Right Panel ---


def left_panel_visible(page):
    """Guardrail: verify Home feed (left panel) is still in the DOM.

    If False after clicking a feed item, the click accidentally navigated
    away from the 2-panel layout — the wrong element was clicked.
    """
    try:
        return page.evaluate(f"() => document.querySelectorAll('{SEL_FEED}').length > 0")
    except Exception:
        return False


def get_topic_ids(page):
    """Get current message topic IDs for detecting conversation changes."""
    try:
        return set(page.evaluate(
            f'() => Array.from(document.querySelectorAll("{SEL_MSG}"))'
            f'  .map(m => m.getAttribute("data-topic-id")).filter(Boolean)'
        ))
    except Exception:
        return set()


def _wait_for_thread(page, topic_id, timeout_s=20):
    """Wait for thread messages to appear after clicking a thread feed item.

    GChat loads the thread panel directly when clicking a thread-specific
    feed item (one with data-topic-id). We just wait for the messages
    to appear in the DOM.
    """
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
    """Wait for new messages to appear in the right panel. Returns message count."""
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
    """Scroll right panel to the very bottom, handling 'Jump to bottom' button.

    GChat may jump to first unread message (far back in long threads).
    Retries scroll + 'Jump to bottom' clicks until truly at bottom.
    """
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


def scroll_and_expand(page, cutoff_ms, max_scrolls, max_expansion, topic_id=""):
    """Interleaved scroll-up + expansion with progressive message collection.

    GChat uses virtual scrolling — only messages near the viewport exist in the
    DOM. Collecting once at the end would miss messages we scrolled past. So we
    collect at every scroll/expand step and merge by (epoch_ms, sender) key.

    When topic_id is set, scopes extraction to that thread only.

    Returns the accumulated list of messages sorted chronologically.
    """
    scroll_count = 0
    expand_count = 0
    collected = {}
    tid_js = json.dumps(topic_id)
    msg_sel = f'{SEL_MSG}[data-topic-id="{topic_id}"]' if topic_id else SEL_MSG

    def _snapshot():
        for msg in extract_messages(page, cutoff_ms, topic_id):
            key = f"{msg['epoch_ms']}_{msg['sender']}"
            if key not in collected:
                collected[key] = msg

    _snapshot()

    while True:
        anchor = page.evaluate("""(s) => {
            const m = document.querySelectorAll(s);
            if (!m.length) return null;
            return {
                ts: parseInt(m[0].getAttribute("data-local-sort-time-msec") || "0", 10),
                tid: m[0].getAttribute("data-topic-id") || "",
            };
        }""", msg_sel)

        if not anchor:
            break

        if anchor["ts"] > 0 and anchor["ts"] <= cutoff_ms:
            eprint(f"  Reached cutoff after {scroll_count} scroll(s)")
            break

        if expand_count < max_expansion:
            bar = _find_one_expandable(page, topic_id)
            if bar:
                before = page.evaluate(
                    "(s) => document.querySelectorAll(s).length", msg_sel
                )
                try:
                    page.mouse.click(bar["x"], bar["y"])
                    expand_count += 1
                except Exception:
                    pass

                _wait_for_dom_change(page, before, msg_sel)

                if anchor["tid"]:
                    _scroll_to_anchor(page, anchor["tid"])
                _snapshot()
                continue

        if scroll_count >= max_scrolls:
            eprint(f"  Hit scroll limit ({max_scrolls})")
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
            eprint(f"  Reached top after {scroll_count} scroll(s)")
            break

        scroll_count += 1
        time.sleep(1)
        _snapshot()

    if expand_count:
        eprint(f"  Expanded {expand_count} bar(s)")

    return sorted(collected.values(), key=lambda m: m["epoch_ms"])


def _wait_for_dom_change(page, before_count, sel=SEL_MSG, timeout=5):
    """Poll until DOM container count changes after expansion, or timeout."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        time.sleep(0.5)
        after = page.evaluate(
            "(s) => document.querySelectorAll(s).length", sel
        )
        if after != before_count:
            return
    time.sleep(1)


def _scroll_to_anchor(page, topic_id):
    """Scroll the anchor message back into view after expansion (free, not counted)."""
    page.evaluate(f"""() => {{
        const el = document.querySelector('c-wiz[data-topic-id="{topic_id}"]');
        if (el) el.scrollIntoView({{block: "center", behavior: "instant"}});
    }}""")
    time.sleep(0.5)


def _find_one_expandable(page, topic_id=""):
    """Find one collapse bar or 'Show more' button to click. Returns coords or None."""
    tid_js = json.dumps(topic_id)
    return page.evaluate(f"""() => {{
        {FIND_PANEL_JS}
        const panel = findPanel({tid_js});

        if (!panel) return null;

        // Collapsed message bars within the active panel
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

        // 'Show more' / 'See more' buttons within the active panel
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


# --- Message Extraction ---


def extract_messages(page, cutoff_ms, topic_id=""):
    """Extract messages from the right panel within date range.

    When topic_id is set, only extracts from containers matching that topic.
    Walks all text nodes inside div[role='group']. Captures rich content,
    link URLs, bot/app sender, and quoted text.
    """
    sel = f'{SEL_MSG}[data-topic-id="{topic_id}"]' if topic_id else SEL_MSG
    return page.evaluate("""({sel, cutoff}) => {
        const containers = document.querySelectorAll(sel);
        const out = [];

        // UI chrome classes: timestamp, sender name, quote attribution.
        const NOISE_CLS = [
            "FvYVyf", "njhDLd", "cPjwNc", "GOoeGd", "Lphf0c",
            "nzVtF", "ZTmjQb", "w692Zc", "TmhmK",
            "ne2Ple-oshW8e-V67aGc",
        ];

        for (const msg of containers) {
            const ms = parseInt(
                msg.getAttribute("data-local-sort-time-msec") || "0", 10
            );
            if (cutoff > 0 && ms < cutoff) continue;

            let sender = "";
            const se = msg.querySelector("span[data-member-id][data-name]");
            if (se) sender = se.getAttribute("data-name");
            if (!sender) {
                const ns = msg.querySelector("span.nzVtF");
                if (ns) sender = ns.textContent.trim();
            }

            let displayTime = "";
            const te = msg.querySelector("span.FvYVyf");
            if (te) displayTime = te.textContent.trim();

            const grp = msg.querySelector("div[role='group']");
            const body = [];
            const quoted = [];

            if (grp) {
                const w = document.createTreeWalker(
                    grp, NodeFilter.SHOW_TEXT, null, false
                );
                while (w.nextNode()) {
                    const t = w.currentNode.textContent.trim();
                    if (!t) continue;
                    const p = w.currentNode.parentElement;
                    if (!p) continue;

                    const cls = p.getAttribute("class") || "";
                    const role = p.getAttribute("role") || "";

                    // Structural filter: skip non-content elements by role
                    if (role === "tooltip" || role === "presentation") continue;

                    // Structural filter: skip text inside buttons/clickable
                    // elements (reactions, actions, thread indicators).
                    // These are captured separately in the button loop below.
                    if (p.closest("button, [role='button']")) continue;

                    // Structural filter: skip text inside reaction lists
                    const rList = p.closest("[role='list']");
                    if (rList && /reaction/i.test(
                        rList.getAttribute("aria-label") || "")) continue;

                    // Skip known UI chrome classes (timestamps, sender names)
                    let skip = false;
                    for (const nc of NOISE_CLS) {
                        if (cls.includes(nc)) { skip = true; break; }
                    }
                    if (skip) continue;

                    // Skip accessibility hints
                    if (t.startsWith("press L to")) continue;

                    cls.includes("J87oZd") ? quoted.push(t) : body.push(t);
                }

                // Capture meaningful button text (e.g. "Join video meeting")
                // but skip action/UI buttons by aria-label
                for (const btn of grp.querySelectorAll("button, [role='button']")) {
                    const label = (btn.getAttribute("aria-label") || "").toLowerCase();
                    if (label.includes("reaction") || label.includes("reply") ||
                        label.includes("resolve") || label.includes("collapsed") ||
                        label.includes("show more") || label.includes("see more")) continue;

                    const t = btn.textContent.trim();
                    if (t && t.length > 2 && t.length < 80 && !body.includes(t)) {
                        body.push(t);
                    }
                }
            }

            let text = body.join("\\n").trim();
            if (quoted.length) text += "\\n[quoted] " + quoted.join("\\n");

            if (grp) {
                const urls = [];
                for (const a of grp.querySelectorAll("a[href]")) {
                    const h = a.getAttribute("href") || "";
                    if (h && !h.startsWith("mailto:") &&
                        !h.startsWith("javascript:") && !text.includes(h)) {
                        urls.push(h);
                    }
                }
                if (urls.length) {
                    text += "\\n[links] " + [...new Set(urls)].join(" ");
                }
            }

            if (text.length > 5000) {
                text = text.substring(0, 5000) + "... [truncated]";
            }
            text = text.replace(/\\n{3,}/g, "\\n\\n");

            if (!text && !sender) continue;

            out.push({
                sender: sender || "Unknown",
                timestamp: displayTime,
                epoch_ms: ms,
                body: text,
            });
        }

        return out;
    }""", {"sel": sel, "cutoff": cutoff_ms})


# --- Debug ---


def debug_dom(page):
    eprint(f"\n=== DEBUG DOM === URL: {page.url}")
    items = page.evaluate(f"""() => {{
        return Array.from(document.querySelectorAll('{SEL_FEED}')).slice(0, 10).map(el => ({{
            gid: el.getAttribute("data-group-id"),
            ts: el.getAttribute("data-display-timestamp"),
            unread: el.getAttribute("data-is-unread"),
            text: el.textContent.trim().substring(0, 150),
        }}));
    }}""")
    eprint(f"Feed items: {len(items)}")
    for it in items:
        eprint(f"  [{it['gid'][:30]}] ts={it['ts']} unread={it['unread']} "
               f"{it['text'][:80]}")
    eprint("=== END ===\n")


# --- Main ---


def main():
    ap = argparse.ArgumentParser(
        description="Read Google Chat conversations via Chrome DevTools Protocol"
    )
    ap.add_argument("--cdp-url", default=DEFAULT_CDP,
                    help=f"CDP endpoint (default: {DEFAULT_CDP})")
    ap.add_argument("--days", type=int, default=3,
                    help="Days to look back (default: 3)")
    ap.add_argument("--max-threads", type=int, default=20,
                    help="Max conversations to read (default: 20)")
    ap.add_argument("--max-scan", type=int, default=100,
                    help="Max feed items to scan (default: 100)")
    ap.add_argument("--max-scroll", type=int, default=20,
                    help="Max scroll-up iterations per thread (default: 20)")
    ap.add_argument("--max-expansion", type=int, default=5,
                    help="Max expansion rounds for collapsed messages (default: 5)")
    ap.add_argument("--format", choices=["json", "yaml"], default="json",
                    help="Output format (default: json)")
    ap.add_argument("--focus-title", default="",
                    help="Only process threads matching this title (others skipped but counted)")
    ap.add_argument("--debug-dom", action="store_true",
                    help="Dump Home feed DOM to stderr and exit")
    args = ap.parse_args()

    cutoff_ms = int(
        (datetime.now(timezone.utc) - timedelta(days=args.days)).timestamp() * 1000
    )

    pw = browser = None
    try:
        pw, browser, page = connect_browser(args.cdp_url)
        go_home(page)

        if args.debug_dom:
            debug_dom(page)
            sys.exit(0)

        feed = snapshot_feed(page, cutoff_ms)
        eprint(f"Feed: {len(feed)} item(s) within {args.days} day(s)")

        if not feed:
            eprint("FATAL: 0 feed items — run --debug-dom to inspect.")
            sys.exit(2)

        threads = []
        skipped = 0
        attempted = 0
        limit = min(len(feed), args.max_scan)

        eprint(f"\nProcessing (target: {args.max_threads}, "
               f"feed: {limit})...\n")

        for i in range(limit):
            if args.focus_title:
                if attempted >= args.max_threads:
                    break
            else:
                if len(threads) >= args.max_threads:
                    break

            gid = feed[i]["group_id"]
            dts = feed[i]["display_ts"]
            tid = feed[i].get("topic_id", "")
            name = feed[i]["name"]
            attempted += 1

            is_focused = not args.focus_title or args.focus_title.lower() in name.lower()
            eprint(f"[{attempted}/{limit}] {name[:55]}...")

            if not is_focused:
                eprint("  SKIP: not matching --focus-title")
                skipped += 1
                continue

            old_ids = get_topic_ids(page)

            if not click_feed_item(page, gid, dts):
                scroll_feed_down(page)
                time.sleep(1)
                if not click_feed_item(page, gid, dts):
                    eprint("  SKIP: item not found in DOM")
                    skipped += 1
                    continue

            time.sleep(1)
            if not left_panel_visible(page):
                eprint("  WARN: left panel gone — wrong click, returning to Home")
                go_home(page)
                skipped += 1
                continue

            if tid:
                msg_count = _wait_for_thread(page, tid)
            else:
                msg_count = wait_for_messages(page, old_ids)
            if msg_count == 0:
                eprint("  SKIP: 0 messages loaded")
                go_home(page)
                skipped += 1
                continue

            eprint(f"  {msg_count} message container(s)"
                   + (f" (thread: {tid[:15]})" if tid else ""))

            scroll_to_bottom(page, topic_id=tid)
            messages = scroll_and_expand(
                page, cutoff_ms, args.max_scroll, args.max_expansion,
                topic_id=tid,
            )
            eprint(f"  -> {len(messages)} message(s) within {args.days} day(s)")

            if args.focus_title and messages:
                eprint(f"\n  --- Collected messages for \"{name}\" ---")
                for idx, m in enumerate(messages, 1):
                    eprint(f"  [{idx}] {m['timestamp']} | {m['sender']}: "
                           f"{m['body'][:120]}")
                eprint(f"  --- End ({len(messages)} total) ---\n")

            if messages:
                threads.append({
                    "name": name,
                    "url": f"https://chat.google.com/{gid}",
                    "message_count": len(messages),
                    "messages": messages,
                })
            else:
                eprint("  SKIP: no messages in date range")
                skipped += 1

            if "/app/home" not in page.url:
                eprint("  Returning to Home...")
                go_home(page)

        eprint(f"\nDone: {len(threads)} conversation(s) from {attempted} "
               f"attempted, {skipped} skipped")

        if args.format == "yaml":
            import yaml
            print(yaml.dump(threads, default_flow_style=False,
                            allow_unicode=True, sort_keys=False))
        else:
            print(json.dumps(threads, separators=(",", ":"),
                             ensure_ascii=False))

    except Exception as e:
        eprint(f"ERROR: {e}")
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
    finally:
        try:
            if browser:
                browser.close()
        except Exception:
            pass
        try:
            if pw:
                pw.stop()
        except Exception:
            pass


if __name__ == "__main__":
    main()
