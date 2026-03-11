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
SEL_USER_MSG = 'c-wiz[data-topic-id][data-is-user-topic="true"]'

# Reusable JS to find the right panel scroll container.
# GChat separates data layer (c-wiz[data-topic-id] with 0x0 dimensions) from
# the visible rendering layer. Walking up from messages hits the hidden layer.
# Instead, find the largest overflow-y:auto/scroll container in the right half.
FIND_PANEL_JS = """
function findPanel() {
    const mid = window.innerWidth / 3;
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
            feed.push({group_id: el.getAttribute("data-group-id") || "", display_ts: ts, name});
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


def wait_for_messages(page, old_ids, timeout_s=20):
    """Wait for new messages to appear in the right panel. Returns message count."""
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        time.sleep(2)
        try:
            r = page.evaluate(f"""() => {{
                const m = document.querySelectorAll("{SEL_MSG}");
                return {{
                    c: m.length,
                    ids: Array.from(m).slice(0, 5)
                        .map(x => x.getAttribute("data-topic-id")).filter(Boolean),
                }};
            }}""")
        except Exception:
            continue

        if r["c"] == 0:
            continue
        if not old_ids or not set(r["ids"]).issubset(old_ids):
            return r["c"]

    try:
        return page.evaluate(f'() => document.querySelectorAll("{SEL_MSG}").length')
    except Exception:
        return 0


def scroll_to_bottom(page):
    """Scroll right panel to the very bottom, handling 'Jump to bottom' button.

    GChat may jump to first unread message (far back in long threads).
    Retries scroll + 'Jump to bottom' clicks until truly at bottom.
    """
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
            const panel = findPanel();
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


def scroll_up(page, cutoff_ms, max_scrolls):
    """Scroll right panel up until oldest message reaches cutoff date."""
    for i in range(max_scrolls):
        oldest = page.evaluate(f"""() => {{
            const m = document.querySelectorAll("{SEL_MSG}");
            return m.length
                ? parseInt(m[0].getAttribute("data-local-sort-time-msec") || "0", 10)
                : 0;
        }}""")

        if oldest > 0 and oldest <= cutoff_ms:
            eprint(f"  Reached cutoff after {i} scroll(s)")
            return

        moved = page.evaluate(f"""() => {{
            {FIND_PANEL_JS}
            const panel = findPanel();
            if (!panel) return false;
            const before = panel.scrollTop;
            panel.scrollTop = Math.max(0, panel.scrollTop - 800);
            return panel.scrollTop !== before;
        }}""")

        if not moved:
            eprint(f"  Reached top after {i} scroll(s)")
            return

        time.sleep(1)

    eprint(f"  Hit scroll limit ({max_scrolls})")


def expand_collapsed_content(page, max_rounds=5):
    """Expand collapsed messages and 'Show more' buttons in the right panel.

    Targets:
    1. Collapsed message bars (aria-label='N collapsed message(s)') — these
       hide older replies in thread views and expand in-place when clicked.
    2. 'Show more'/'See more' buttons — truncated message content.

    Does NOT click 'N replies' headers — those are thread navigators.

    Uses Playwright mouse.click() (not JS .click()) because GChat's framework
    event handlers do not respond to synthetic JS click events.

    Retries expansion because collapsed messages may be lazy-loaded — clicking
    one collapse bar may reveal additional collapse bars for more hidden content.
    """
    before_count = page.evaluate(
        f'() => document.querySelectorAll("{SEL_MSG}").length'
    )
    total_clicked = 0

    for round_num in range(max_rounds):
        bars = page.evaluate(f"""() => {{
            {FIND_PANEL_JS}
            const panel = findPanel();
            const results = [];

            // Collapsed message bars
            for (const bar of document.querySelectorAll(
                "[role='button'][aria-label*='collapsed message']"
            )) {{
                const rect = bar.getBoundingClientRect();
                if (rect.width < 20 || rect.height < 5) continue;
                bar.scrollIntoView({{block: "center", behavior: "instant"}});
                const r2 = bar.getBoundingClientRect();
                results.push({{
                    x: Math.round(r2.left + r2.width / 2),
                    y: Math.round(r2.top + r2.height / 2),
                    label: bar.getAttribute("aria-label") || "",
                    type: "collapse",
                }});
            }}

            // 'Show more' / 'See more' buttons (by aria-label)
            if (panel) {{
                for (const btn of panel.querySelectorAll(
                    "button[aria-label*='how more'], [role='button'][aria-label*='how more'],"
                    + "button[aria-label*='ee more'], [role='button'][aria-label*='ee more']"
                )) {{
                    btn.scrollIntoView({{block: "center", behavior: "instant"}});
                    const r = btn.getBoundingClientRect();
                    if (r.width < 10 || r.height < 5) continue;
                    results.push({{
                        x: Math.round(r.left + r.width / 2),
                        y: Math.round(r.top + r.height / 2),
                        label: btn.getAttribute("aria-label") || btn.textContent.trim(),
                        type: "showmore",
                    }});
                }}

                // Fallback: match by text content for Show more/See more
                if (results.filter(r => r.type === "showmore").length === 0) {{
                    for (const btn of panel.querySelectorAll(
                        "button, [role='button'], span[role='button']"
                    )) {{
                        const t = btn.textContent.trim().toLowerCase();
                        if (t === "show more" || t === "see more") {{
                            btn.scrollIntoView({{block: "center", behavior: "instant"}});
                            const r = btn.getBoundingClientRect();
                            if (r.width < 10 || r.height < 5) continue;
                            results.push({{
                                x: Math.round(r.left + r.width / 2),
                                y: Math.round(r.top + r.height / 2),
                                label: t,
                                type: "showmore",
                            }});
                        }}
                    }}
                }}
            }}

            return results;
        }}""")

        if not bars:
            break

        for bar in bars:
            try:
                page.mouse.click(bar["x"], bar["y"])
                total_clicked += 1
                time.sleep(2)
            except Exception:
                pass

        time.sleep(1)

    if total_clicked:
        after_count = page.evaluate(
            f'() => document.querySelectorAll("{SEL_MSG}").length'
        )
        new_msgs = after_count - before_count
        eprint(f"  Expanded {total_clicked} bar(s) ({new_msgs} new messages)")


# --- Message Extraction ---


def extract_messages(page, cutoff_ms):
    """Extract messages from the right panel within date range.

    Walks all text nodes inside div[role='group']. Captures rich content,
    link URLs, bot/app sender, and quoted text.
    """
    return page.evaluate("""(cutoff) => {
        const containers = document.querySelectorAll(
            'c-wiz[data-topic-id][data-is-user-topic="true"]'
        );
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
                // but skip action/UI buttons by aria-label or CSS class
                for (const btn of grp.querySelectorAll("button, [role='button']")) {
                    const label = (btn.getAttribute("aria-label") || "").toLowerCase();
                    if (label.includes("reaction") || label.includes("reply") ||
                        label.includes("resolve") || label.includes("collapsed") ||
                        label.includes("show more") || label.includes("see more")) continue;

                    // Skip thread reply indicators and metadata by class
                    const bcls = btn.getAttribute("class") || "";
                    let isNoise = false;
                    for (const nc of NOISE_CLS) {
                        if (bcls.includes(nc)) { isNoise = true; break; }
                    }
                    if (isNoise) continue;

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
    }""", cutoff_ms)


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
        limit = min(len(feed), args.max_scan)

        eprint(f"\nProcessing (target: {args.max_threads}, "
               f"feed: {limit})...\n")

        for i in range(limit):
            if len(threads) >= args.max_threads:
                break

            gid = feed[i]["group_id"]
            dts = feed[i]["display_ts"]
            name = feed[i]["name"]

            eprint(f"[{len(threads) + 1}/{args.max_threads}] {name[:55]}...")

            old_ids = get_topic_ids(page)

            if not click_feed_item(page, gid, dts):
                scroll_feed_down(page)
                time.sleep(1)
                if not click_feed_item(page, gid, dts):
                    eprint("  SKIP: item not found in DOM")
                    skipped += 1
                    continue

            # Guardrail: left panel must still be visible.
            # If gone, we accidentally navigated away from 2-panel layout.
            time.sleep(1)
            if not left_panel_visible(page):
                eprint("  WARN: left panel gone — wrong click, returning to Home")
                go_home(page)
                skipped += 1
                continue

            msg_count = wait_for_messages(page, old_ids)
            if msg_count == 0:
                eprint("  SKIP: 0 messages loaded")
                go_home(page)
                skipped += 1
                continue

            eprint(f"  {msg_count} message container(s)")

            scroll_to_bottom(page)

            if args.max_scroll > 0:
                scroll_up(page, cutoff_ms, args.max_scroll)

            expand_collapsed_content(page, max_rounds=args.max_expansion)

            messages = extract_messages(page, cutoff_ms)
            eprint(f"  -> {len(messages)} message(s) within {args.days} day(s)")

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

        eprint(f"\nDone: {len(threads)} conversation(s), {skipped} skipped")

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
