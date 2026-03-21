#!/usr/bin/env python3
"""
GChat Reader - extract Google Chat conversations via CDP, cache, and summarize.

Connects to a remote Chrome instance, navigates GChat Home feed, extracts
conversations with progressive message collection (virtual scrolling aware).
Caches each message in SQLite, summarizes at conversation level via AI.
Always outputs compact summaries (group_id + name + AI summary).

Usage:
  python gchat_reader.py
  python gchat_reader.py --days 7 --max-threads 10
  python gchat_reader.py --cdp-url http://192.168.1.11:9223
"""

import argparse
import json
import os
import queue as _queue
import sys
import threading
import time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

_TZ = ZoneInfo(os.environ.get("TZ", "Asia/Singapore"))
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PwTimeout

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gchat_db import get_gchat_db, SkillDB
from gchat_cleaner import clean_chat_message
from gchat_summarizer import summarize_resource

DEFAULT_CDP = "http://192.168.1.11:9223"
GCHAT_URL = "https://chat.google.com/app/home"
_WORKDIR = Path(__file__).resolve().parents[3] / "workdir"
DB_PATH = Path(__file__).resolve().parent.parent / "data" / "gchat_cache.db"

SEL_FEED = 'span[role="listitem"][data-group-id][data-is-unread]'
SEL_MSG = "c-wiz[data-topic-id]"

FIND_PANEL_JS = """
function findPanel(topicId) {
    const mid = window.innerWidth / 3;
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


_debug_file = sys.stderr
_output_file = sys.stdout


def _ts() -> str:
    return datetime.now(_TZ).strftime("%Y-%m-%dT%H:%M:%S%z")


def eprint(*a, **kw):
    print(f"[{_ts()}]", *a, file=_debug_file, flush=True, **kw)


_HEARTBEAT_INTERVAL = int(os.environ.get("SKILL_HEARTBEAT_INTERVAL", "60"))


def get_db(*, force: bool = False) -> SkillDB:
    return get_gchat_db(DB_PATH, force=force)


# ── Browser & Navigation ───────────────────────────────────────────

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


def snapshot_feed(page, cutoff_ms):
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


def left_panel_visible(page):
    try:
        return page.evaluate(f"() => document.querySelectorAll('{SEL_FEED}').length > 0")
    except Exception:
        return False


def get_topic_ids(page):
    try:
        return set(page.evaluate(
            f'() => Array.from(document.querySelectorAll("{SEL_MSG}"))'
            f'  .map(m => m.getAttribute("data-topic-id")).filter(Boolean)'
        ))
    except Exception:
        return set()


def _wait_for_thread(page, topic_id, timeout_s=20):
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


def extract_messages(page, cutoff_ms, topic_id=""):
    sel = f'c-wiz[data-topic-id="{topic_id}"]' if topic_id else SEL_MSG
    return page.evaluate("""({sel, cutoff, isThread}) => {
        const NOISE_CLS = [
            "FvYVyf", "njhDLd", "cPjwNc", "GOoeGd", "Lphf0c",
            "nzVtF", "ZTmjQb", "w692Zc", "TmhmK",
            "ne2Ple-oshW8e-V67aGc",
        ];
        function extractBody(grp) {
            const body = [];
            const quoted = [];
            const w = document.createTreeWalker(grp, NodeFilter.SHOW_TEXT, null, false);
            while (w.nextNode()) {
                const t = w.currentNode.textContent.trim();
                if (!t) continue;
                const p = w.currentNode.parentElement;
                if (!p) continue;
                const cls = p.getAttribute("class") || "";
                const role = p.getAttribute("role") || "";
                if (role === "tooltip" || role === "presentation") continue;
                if (p.closest("button, [role='button']")) continue;
                const rList = p.closest("[role='list']");
                if (rList && /reaction/i.test(rList.getAttribute("aria-label") || "")) continue;
                let skip = false;
                for (const nc of NOISE_CLS) { if (cls.includes(nc)) { skip = true; break; } }
                if (skip) continue;
                if (t.startsWith("press L to")) continue;
                cls.includes("J87oZd") ? quoted.push(t) : body.push(t);
            }
            for (const btn of grp.querySelectorAll("button, [role='button']")) {
                const label = (btn.getAttribute("aria-label") || "").toLowerCase();
                if (label.includes("reaction") || label.includes("reply") ||
                    label.includes("resolve") || label.includes("collapsed") ||
                    label.includes("show more") || label.includes("see more")) continue;
                const t = btn.textContent.trim();
                if (t && t.length > 2 && t.length < 80 && !body.includes(t)) body.push(t);
            }
            let text = body.join("\\n").trim();
            if (quoted.length) text += "\\n[quoted] " + quoted.join("\\n");
            const urls = [];
            for (const a of grp.querySelectorAll("a[href]")) {
                const h = a.getAttribute("href") || "";
                if (h && !h.startsWith("mailto:") && !h.startsWith("javascript:") && !text.includes(h))
                    urls.push(h);
            }
            if (urls.length) text += "\\n[links] " + [...new Set(urls)].join(" ");
            return text.replace(/\\n{3,}/g, "\\n\\n");
        }
        const out = [];
        if (isThread) {
            const containers = document.querySelectorAll(sel);
            for (const c of containers) {
                if (c.getAttribute("data-is-detailed-thread-view") !== "true") continue;
                for (const grp of c.querySelectorAll("div[role='group']")) {
                    const dataId = grp.getAttribute("data-id") || "";
                    const absEl = grp.querySelector("span[data-absolute-timestamp]");
                    const ms = absEl ? parseInt(absEl.getAttribute("data-absolute-timestamp") || "0", 10) : 0;
                    if (cutoff > 0 && ms > 0 && ms < cutoff) continue;
                    let sender = "";
                    const se = grp.querySelector("span[data-member-id][data-name]");
                    if (se) sender = se.getAttribute("data-name");
                    if (!sender) { const ns = grp.querySelector("span.nzVtF"); if (ns) sender = ns.textContent.trim(); }
                    const te = grp.querySelector("span.FvYVyf");
                    const displayTime = te ? te.textContent.trim() : "";
                    const text = extractBody(grp);
                    if (!text && !sender) continue;
                    out.push({ data_id: dataId, sender: sender || "Unknown", timestamp: displayTime, epoch_ms: ms, body: text });
                }
            }
        } else {
            for (const msg of document.querySelectorAll(sel)) {
                const dataId = msg.getAttribute("data-topic-id") || "";
                const ms = parseInt(msg.getAttribute("data-local-sort-time-msec") || "0", 10);
                if (cutoff > 0 && ms < cutoff) continue;
                let sender = "";
                const se = msg.querySelector("span[data-member-id][data-name]");
                if (se) sender = se.getAttribute("data-name");
                if (!sender) { const ns = msg.querySelector("span.nzVtF"); if (ns) sender = ns.textContent.trim(); }
                const te = msg.querySelector("span.FvYVyf");
                const displayTime = te ? te.textContent.trim() : "";
                const grp = msg.querySelector("div[role='group']");
                const text = grp ? extractBody(grp) : "";
                if (!text && !sender) continue;
                out.push({ data_id: dataId, sender: sender || "Unknown", timestamp: displayTime, epoch_ms: ms, body: text });
            }
        }
        return out;
    }""", {"sel": sel, "cutoff": cutoff_ms, "isThread": bool(topic_id)})


def scroll_and_expand(page, cutoff_ms, max_scrolls, max_expansion,
                      topic_id="", cached_ids=None, early_stop_n=0):
    scroll_count = 0
    expand_count = 0
    collected = {}
    tid_js = json.dumps(topic_id)
    is_thread = bool(topic_id)
    cached_ids = cached_ids or set()
    consecutive_cached = 0

    def _snapshot():
        nonlocal consecutive_cached
        new_found = False
        for msg in extract_messages(page, cutoff_ms, topic_id):
            key = msg.get("data_id") or f"{msg['epoch_ms']}_{msg['sender']}_{hash(msg['body'][:80])}"
            if key not in collected:
                collected[key] = msg
                if cached_ids and key in cached_ids:
                    consecutive_cached += 1
                else:
                    consecutive_cached = 0
                    new_found = True
        return new_found

    _snapshot()

    while True:
        if early_stop_n > 0 and consecutive_cached >= early_stop_n:
            eprint(f"  Scroll early-stop: {consecutive_cached} consecutive cached messages")
            break
        if is_thread:
            anchor = page.evaluate(f"""() => {{
                const sel = 'c-wiz[data-topic-id="{topic_id}"][data-is-detailed-thread-view="true"]';
                const c = document.querySelector(sel);
                if (!c) return null;
                const grps = c.querySelectorAll("div[role='group']");
                if (!grps.length) return null;
                const absEl = grps[0].querySelector("span[data-absolute-timestamp]");
                const ts = absEl ? parseInt(absEl.getAttribute("data-absolute-timestamp") || "0", 10) : 0;
                return {{ts: ts, grpCount: grps.length}};
            }}""")
        else:
            anchor = page.evaluate("""(s) => {
                const m = document.querySelectorAll(s);
                if (!m.length) return null;
                return {
                    ts: parseInt(m[0].getAttribute("data-local-sort-time-msec") || "0", 10),
                    tid: m[0].getAttribute("data-topic-id") || "",
                };
            }""", SEL_MSG)

        if not anchor:
            break
        if anchor["ts"] > 0 and anchor["ts"] <= cutoff_ms:
            eprint(f"  Reached cutoff after {scroll_count} scroll(s)")
            break

        if expand_count < max_expansion:
            bar = _find_one_expandable(page, topic_id)
            if bar:
                if is_thread:
                    before = anchor.get("grpCount", 0)
                else:
                    before = page.evaluate("(s) => document.querySelectorAll(s).length", SEL_MSG)
                try:
                    page.mouse.click(bar["x"], bar["y"])
                    expand_count += 1
                except Exception:
                    pass
                if is_thread:
                    sel_grp = f'c-wiz[data-topic-id="{topic_id}"][data-is-detailed-thread-view="true"] div[role="group"]'
                    _wait_for_dom_change(page, before, sel_grp)
                else:
                    _wait_for_dom_change(page, before, SEL_MSG)
                    if anchor.get("tid"):
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
    deadline = time.time() + timeout
    while time.time() < deadline:
        time.sleep(0.5)
        after = page.evaluate("(s) => document.querySelectorAll(s).length", sel)
        if after != before_count:
            return
    time.sleep(1)


def _scroll_to_anchor(page, topic_id):
    page.evaluate(f"""() => {{
        const el = document.querySelector('c-wiz[data-topic-id="{topic_id}"]');
        if (el) el.scrollIntoView({{block: "center", behavior: "instant"}});
    }}""")
    time.sleep(0.5)


def _find_one_expandable(page, topic_id=""):
    tid_js = json.dumps(topic_id)
    return page.evaluate(f"""() => {{
        {FIND_PANEL_JS}
        const panel = findPanel({tid_js});
        if (!panel) return null;
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


# ── Caching ─────────────────────────────────────────────────────────

def make_resource_id(group_id: str, topic_id: str = "") -> str:
    """Build resource_id: {group_id}/{topic_id} if topic_id present, else {group_id}."""
    if topic_id:
        return f"{group_id}/{topic_id}"
    return group_id


def conversation_needs_fetch(db: SkillDB, resource_id: str, display_ts: int) -> bool:
    """Check if a conversation needs re-fetching based on display_timestamp."""
    return db.conversation_needs_fetch(resource_id, display_ts)


def cache_conversation(db: SkillDB, resource_id: str, name: str,
                       messages: list[dict]) -> int:
    """Cache each message in the conversation. Returns count of newly cached messages."""
    new_count = 0
    for msg in messages:
        data_id = msg.get("data_id") or f"{msg['epoch_ms']}_{hash(msg.get('sender', ''))}"
        body = clean_chat_message(msg.get("body", ""))
        author = msg.get("sender", "Unknown")
        epoch_ms = msg.get("epoch_ms", 0)
        ts_iso = datetime.fromtimestamp(epoch_ms / 1000, tz=_TZ).isoformat() if epoch_ms else ""

        meta = {"timestamp_display": msg.get("timestamp", "")}

        if db.upsert_atomic(
            "gchat", resource_id, data_id,
            author=author, content=body,
            created_at=ts_iso, updated_at=ts_iso,
            metadata=meta,
        ):
            new_count += 1

    return new_count


def summarize_and_output(db: SkillDB, info: dict) -> None:
    """Summarize a single conversation and stream output immediately."""
    resource_id = info["resource_id"]
    name = info["name"]
    current = info.get("_sum_current", "?")
    total = info.get("_sum_total", "?")
    sum_progress = f"[Summarizing {current}/{total}]"
    sum_done = f"[Summarized {current}/{total}]"

    if not db.needs_resummarize(resource_id):
        existing = db.get_resource_summary(resource_id)
        if existing:
            eprint(f"{sum_done} [{name[:40]}]: using cached summary")
            _print_output(resource_id, name, existing["summary"], info,
                          summarized_at=existing.get("summarized_at", ""))
            return
        return

    existing_summary = db.get_resource_summary(resource_id)
    existing_text = existing_summary["summary"] if existing_summary else None
    prev_summarized_at = existing_summary.get("summarized_at", "") if existing_summary else ""

    if existing_text and existing_summary:
        items = db.get_items_since(resource_id, prev_summarized_at)
        if not items:
            items = db.get_atomic_for_resource(resource_id)
    else:
        items = db.get_atomic_for_resource(resource_id)

    if not items and existing_text:
        _print_output(resource_id, name, existing_text, info,
                      summarized_at=prev_summarized_at)
        return
    if not items:
        return

    all_items = db.get_atomic_for_resource(resource_id)
    meta = {"message_count": len(all_items), "url": info.get("url", "")}

    eprint(f"{sum_progress} [{name[:40]}]: AI summarizing ({len(items)} messages)...")
    summary_text = summarize_resource(
        title=name,
        source_type="Google Chat conversation",
        atomic_items=items,
        metadata=meta,
        existing_summary=existing_text,
    )

    if summary_text:
        db.upsert_summary(resource_id, "gchat", name, summary_text, meta)
        saved = db.get_resource_summary(resource_id)
        new_summarized_at = saved.get("summarized_at", "") if saved else ""
        _print_output(resource_id, name, summary_text, info,
                      summarized_at=new_summarized_at)
        eprint(f"{sum_done} [{name[:40]}]: done")
    elif existing_text:
        _print_output(resource_id, name, existing_text, info,
                      summarized_at=prev_summarized_at)


def _to_local_ts(iso_str: str) -> str:
    """Convert an ISO timestamp string to the configured local timezone."""
    if not iso_str:
        return iso_str
    try:
        dt = datetime.fromisoformat(iso_str)
        return dt.astimezone(_TZ).isoformat()
    except (ValueError, TypeError):
        return iso_str


def _print_output(resource_id: str, name: str, summary: str, info: dict,
                  summarized_at: str = "") -> None:
    """Stream a single conversation block to stdout."""
    display_ts = info.get("display_ts", 0)
    ts_str = ""
    if display_ts:
        ts_str = datetime.fromtimestamp(display_ts / 1000, tz=_TZ).isoformat()

    items_count = info.get("message_count", "")
    current = info.get("_sum_current", "")
    total = info.get("_sum_total", "")
    meta_parts = [
        f"Source: gchat",
        f"Group: {resource_id}",
    ]
    if items_count:
        meta_parts.append(f"Messages: {items_count}")
    if ts_str:
        meta_parts.append(f"Last Activity: {_to_local_ts(ts_str)}")
    if summarized_at:
        meta_parts.append(f"Last Updated: {_to_local_ts(summarized_at)}")

    numbering = f"[{current}/{total}] " if current and total else ""
    print(f"\n\n## {numbering}{name}", file=_output_file, flush=True)
    print(" | ".join(meta_parts), file=_output_file, flush=True)
    print(summary, file=_output_file, flush=True)


def _summarize_worker(q: "_queue.Queue", db_path: Path, error_event: threading.Event, results: list) -> None:
    """Background worker: process summarization queue one item at a time."""
    worker_db = get_gchat_db(db_path)
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
                eprint(f"ERROR summarizing {item.get('resource_id', '?')}: {exc}")
                results.append(exc)
                error_event.set()
            finally:
                q.task_done()
    finally:
        worker_db.close()


# ── Main ────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(
        description="Read Google Chat conversations via CDP, cache, and summarize"
    )
    ap.add_argument("--cdp-url", default=DEFAULT_CDP,
                    help=f"CDP endpoint (default: {DEFAULT_CDP})")
    ap.add_argument("--days", type=int, default=3,
                    help="Days to look back (default: 3)")
    ap.add_argument("--max-threads", type=int, default=200,
                    help="Max conversations to process (default: 200)")
    ap.add_argument("--max-scan", type=int, default=500,
                    help="Max feed items to scan (default: 500)")
    ap.add_argument("--max-scroll", type=int, default=5,
                    help="Max scroll-up iterations per thread (default: 5)")
    ap.add_argument("--max-expansion", type=int, default=5,
                    help="Max expansion rounds for collapsed messages (default: 5)")
    ap.add_argument("--early-stop", type=int, default=3,
                    help="Stop after N consecutive unchanged conversations (0=disabled, default: 3)")
    ap.add_argument("--focus-title", default="",
                    help="Only process conversations matching this title (case-insensitive)")
    ap.add_argument("--force", action="store_true",
                    help="Bypass change detection, re-fetch and re-summarize all")
    ap.add_argument("--cached-only", action="store_true",
                    help="Output cached summaries from DB without browser fetching (fast, for reports)")
    ap.add_argument("--output", default=str(_WORKDIR / "gchat-output.md"),
                    help="Write results to this file (default: workdir/gchat-output.md)")
    ap.add_argument("--debug-log", default=str(_WORKDIR / "gchat-debug.log"),
                    help="Write debug messages to this file (default: workdir/gchat-debug.log)")
    ap.add_argument("--debug-dom", action="store_true",
                    help="Dump Home feed DOM to stderr and exit")
    args = ap.parse_args()

    global _output_file, _debug_file
    for p in (Path(args.output), Path(args.debug_log)):
        p.parent.mkdir(parents=True, exist_ok=True)
    _output_file = open(args.output, "w", encoding="utf-8", buffering=1)
    _debug_file = open(args.debug_log, "w", encoding="utf-8", buffering=1)
    eprint(f"{'='*60}")
    eprint(f"STATUS: STARTED - GChat Reader")
    eprint(f"output={args.output}, debug={args.debug_log}")
    eprint(f"{'='*60}")

    print("[gchat_reader] STARTED - processing Google Chat conversations. Do NOT interrupt or move on - this takes 5-15 minutes.", flush=True)

    cutoff_ms = int(
        (datetime.now(_TZ) - timedelta(days=args.days)).timestamp() * 1000
    )

    if args.force:
        eprint("--force: recreating database from scratch")
    db = get_db(force=args.force)
    pw = browser = None

    if args.cached_only:
        try:
            summaries = db.get_all_summaries(source="gchat")
            total = len(summaries)
            eprint(f"Cached-only mode: {total} summaries from DB")
            for idx, s in enumerate(summaries, 1):
                meta = json.loads(s.get("metadata", "{}"))
                info = {
                    "display_ts": 0,
                    "url": "",
                    "message_count": meta.get("message_count", ""),
                    "_sum_current": idx,
                    "_sum_total": total,
                }
                _print_output(
                    s["resource_id"], s.get("title", "(unknown)"),
                    s.get("summary", "(no summary)"), info,
                    summarized_at=s.get("summarized_at", ""),
                )
            eprint(f"{'='*60}")
            eprint(f"STATUS: COMPLETED - GChat Reader (cached-only): {len(summaries)} summaries output")
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
        go_home(page)

        if args.debug_dom:
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
                eprint(f"  [{it['gid'][:30]}] ts={it['ts']} unread={it['unread']} {it['text'][:80]}")
            eprint("=== END ===\n")
            sys.exit(0)

        feed = snapshot_feed(page, cutoff_ms)
        eprint(f"Feed: {len(feed)} item(s) within {args.days} day(s)")
        if not feed:
            eprint("FATAL: 0 feed items - run --debug-dom to inspect.")
            sys.exit(2)

        convo_infos = []
        skipped_focus = 0
        skipped_unchanged = 0
        skipped_error = 0
        attempted = 0
        consecutive_cached = 0
        early_stop_triggered = False
        limit = min(len(feed), args.max_scan)
        fetched_ids: set = set()

        sum_q: _queue.Queue = _queue.Queue()
        _sum_error_event = threading.Event()
        _sum_errors: list = []
        worker = threading.Thread(
            target=_summarize_worker, args=(sum_q, DB_PATH, _sum_error_event, _sum_errors), daemon=True,
        )
        worker.start()

        eprint(f"\nProcessing (target: {args.max_threads}, feed: {limit}, "
               f"early-stop: {args.early_stop})...\n")

        for i in range(limit):
            if len(convo_infos) >= args.max_threads:
                break

            gid = feed[i]["group_id"]
            dts = feed[i]["display_ts"]
            tid = feed[i].get("topic_id", "")
            name = feed[i]["name"]
            rid = make_resource_id(gid, tid)
            attempted += 1

            is_focused = not args.focus_title or args.focus_title.lower() in name.lower()
            eprint(f"[Fetching {attempted}/{limit}] {name[:55]}... (summarization pending)")
            print(f"[Fetching {attempted}/{limit}] {name} (summarization pending)", flush=True)

            if not is_focused:
                eprint(f"[Fetch skipped {attempted}/{limit}] {name[:55]} - not matching focus filter")
                skipped_focus += 1
                print(f"[Fetch skipped {attempted}/{limit}] {name} - not matching focus filter", flush=True)
                continue

            if early_stop_triggered or (
                not args.force and not conversation_needs_fetch(db, rid, dts)
            ):
                eprint(f"[Fetch skipped {attempted}/{limit}] {name[:55]} - unchanged (summarization pending)")
                convo_infos.append({
                    "resource_id": rid, "name": name, "display_ts": dts,
                    "url": f"https://chat.google.com/{gid}", "fetched": False,
                })
                skipped_unchanged += 1
                if not early_stop_triggered:
                    consecutive_cached += 1
                    if args.early_stop > 0 and consecutive_cached >= args.early_stop:
                        eprint(f"\n  Early stop: {consecutive_cached} consecutive cached conversations. "
                               f"Skipping fetches, continuing scan...")
                        early_stop_triggered = True
                print(f"[Fetch skipped {attempted}/{limit}] {name} - unchanged (summarization pending)", flush=True)
                continue

            consecutive_cached = 0
            old_ids = get_topic_ids(page) if not tid else set()

            if not click_feed_item(page, gid, dts):
                scroll_feed_down(page)
                time.sleep(1)
                if not click_feed_item(page, gid, dts):
                    eprint("  SKIP: item not found in DOM")
                    skipped_error += 1
                    print(f"[Fetch failed {attempted}/{limit}] {name} - item not found in DOM", flush=True)
                    continue

            time.sleep(1)
            if not left_panel_visible(page):
                eprint("  WARN: mid panel gone - wrong click, returning to Home")
                go_home(page)
                skipped_error += 1
                print(f"[Fetch failed {attempted}/{limit}] {name} - panel lost, returned to Home", flush=True)
                continue

            if tid:
                msg_count = _wait_for_thread(page, tid)
            else:
                msg_count = wait_for_messages(page, old_ids)
            if msg_count == 0:
                eprint("  SKIP: 0 messages loaded")
                go_home(page)
                skipped_error += 1
                print(f"[Fetch failed {attempted}/{limit}] {name} - 0 messages loaded", flush=True)
                continue

            eprint(f"  {msg_count} message container(s)"
                   + (f" (thread: {tid[:15]})" if tid else ""))

            scroll_to_bottom(page, topic_id=tid)
            cached_ids = db.get_cached_message_ids(rid)
            messages = scroll_and_expand(
                page, cutoff_ms, args.max_scroll, args.max_expansion,
                topic_id=tid, cached_ids=cached_ids,
                early_stop_n=args.early_stop,
            )
            eprint(f"  -> {len(messages)} message(s) within {args.days} day(s)")

            if messages:
                new_count = cache_conversation(db, rid, name, messages)
                if new_count > 0:
                    eprint(f"  -> {new_count} new message(s) cached")
                else:
                    eprint(f"  -> all messages already cached")

                info_item = {
                    "resource_id": rid, "name": name, "display_ts": dts,
                    "url": f"https://chat.google.com/{gid}", "fetched": True,
                    "message_count": len(messages),
                }
                convo_infos.append(info_item)
                fetched_ids.add(rid)
            else:
                eprint("  SKIP: no messages in date range")
                skipped_error += 1

            if "/app/home" not in page.url:
                eprint("  Returning to Home...")
                go_home(page)
            eprint(f"[Fetched {attempted}/{limit}] {name[:55]} - queued for summarization")
            print(f"[Fetched {attempted}/{limit}] {name} - queued for summarization (pipeline running)", flush=True)

        stop_reason = ""
        if early_stop_triggered:
            stop_reason = ", early-stopped"
        elif len(convo_infos) >= args.max_threads:
            stop_reason = ", reached max-threads"

        eprint(f"\nFetch done: {len(convo_infos)} conversation(s) from {attempted} "
               f"attempted (unchanged: {skipped_unchanged}, focus-skip: {skipped_focus}, "
               f"errors: {skipped_error}{stop_reason})")

        total_to_summarize = len(convo_infos)
        eprint(f"\nQueuing {total_to_summarize} conversations for summarization ({len(fetched_ids)} fetched, {total_to_summarize - len(fetched_ids)} unchanged)...")
        for info in convo_infos:
            info["_sum_total"] = total_to_summarize
            sum_q.put(info)

        sum_q.put(None)
        worker.join()
        if _sum_errors:
            eprint(f"{'='*60}")
            eprint(f"STATUS: COMPLETED WITH ERRORS - GChat Reader finished ({len(convo_infos)} conversations, {len(_sum_errors)} summarization error(s))")
            for err in _sum_errors:
                eprint(f"  ERROR: {err}")
            eprint(f"{'='*60}")
            print(
                f"\n{'='*60}\n"
                f"[gchat_reader] DONE WITH ERRORS - {len(_sum_errors)} conversation(s) failed summarization.\n"
                f"Check gchat-debug.log for details. Other {len(convo_infos) - len(_sum_errors)} conversations completed.\n"
                f"{'='*60}\n",
                flush=True,
            )
        else:
            eprint(f"{'='*60}")
            eprint(f"STATUS: COMPLETED - GChat Reader pipeline finished successfully ({len(convo_infos)} conversations)")
            eprint(f"{'='*60}")
        print(
            f"\n{'='*60}\n"
            f"[gchat_reader] ALL DONE - output file is ready for use.\n"
            f"Fetched: {len(convo_infos)} conversation(s) | attempted: {attempted}\n"
            f"{'='*60}\n",
            flush=True,
        )

    except Exception as e:
        eprint(f"{'='*60}")
        eprint(f"STATUS: FAILED - GChat Reader encountered an error: {e}")
        eprint(f"{'='*60}")
        import traceback
        traceback.print_exc(file=_debug_file)
        print(f"\n[gchat_reader] FAILED with error: {e}\n", flush=True)
        sys.exit(1)
    finally:
        db.close()
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
        if _output_file and _output_file is not sys.stdout:
            _output_file.close()
        if _debug_file and _debug_file is not sys.stderr:
            _debug_file.close()


if __name__ == "__main__":
    main()
