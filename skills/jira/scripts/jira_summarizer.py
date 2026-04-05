"""
AI summarization for Jira tickets via LiteLLM proxy.

Generates relevance-scored, structured JSON summaries with entity extraction
using native JSON mode (response_format). Self-contained - no shared modules.
"""

import json
import os
import re
import sys
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional

import requests

LITELLM_BASE = os.environ.get("LITELLM_BASE_URL", "https://llm.gigary.com/v1")
SUMMARIZE_MODEL = os.environ.get("SUMMARIZE_MODEL", "local/qwen3.5-35b-a3b:instruct-reasoning")
LITELLM_API_KEY = os.environ.get("API_KEY_OTHER", os.environ.get("LLAMA_TOKEN", ""))
SUMMARIZE_RETRIES = int(os.environ.get("SUMMARIZE_RETRIES", "3"))
SUMMARIZE_RETRY_INITIAL_SEC = float(os.environ.get("SUMMARIZE_RETRY_INITIAL_SEC", "30"))

_USER_MD_PATH = Path(__file__).resolve().parents[3] / "User.md"
_USER_CONTEXT: Optional[str] = None

_RELEVANCE_FLOORS = {"direct": 7, "indirect": 5, "none": 1}
_WORD_HINTS = {"direct": 200, "indirect": 100, "none": 30}


def eprint(*a, **kw):
    print(*a, file=sys.stderr, **kw)


def word_limit_for_relevance(relevance: int) -> int:
    """Return max word count for a given relevance score."""
    if relevance >= 8:
        return 200
    if relevance >= 5:
        return 100
    return 30


# ── Data Model ───────────────────────────────────────────────────────


@dataclass
class SummaryResult:
    relevance: int
    summary: str
    work_items: list[str] = field(default_factory=list)
    people: list[str] = field(default_factory=list)
    labels: list[str] = field(default_factory=list)


# ── User Context ─────────────────────────────────────────────────────


def _load_user_context() -> str:
    global _USER_CONTEXT
    if _USER_CONTEXT is not None:
        return _USER_CONTEXT
    try:
        _USER_CONTEXT = _USER_MD_PATH.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        eprint(f"WARNING: User.md not found at {_USER_MD_PATH}, using empty context")
        _USER_CONTEXT = ""
    return _USER_CONTEXT


# ── Prompt Building ──────────────────────────────────────────────────


def _word_limit(mention_type: str) -> int:
    """Hint max words to LLM based on expected relevance for this mention type."""
    return _WORD_HINTS.get(mention_type, 30)


def _build_system_prompt() -> str:
    user_ctx = _load_user_context()
    return f"""You are a relevance-scoring executive assistant. Score the relevance, summarize, and extract entities from the content for the following user.

{user_ctx}"""


def _build_user_prompt(
    title: str,
    source_type: str,
    meta_json: str,
    content: str,
    mention_type: str,
    existing_summary: Optional[str] = None,
) -> str:
    word_hint = _word_limit(mention_type)

    parts = [
        f"Analyze this {source_type} resource and return a JSON response.",
        f"\nResource: {title}",
        f"Mention Type: {mention_type}",
        "  - direct: user is explicitly addressed, assigned, tagged, or has actively participated/replied",
        "  - indirect: user is in recipient/participant list but not directly addressed",
        "  - none: no personal involvement detected",
        f"Metadata: {meta_json}",
    ]

    if existing_summary:
        parts.append(f"\nExisting summary (update with new content, preserve still-relevant context):\n{existing_summary}")

    parts.append(f"\nContent (chronological):\n{content}")

    parts.append(f"""
Scoring rules:
- Refer to the user's "What Matters Most" section for scoring guidance
- RELEVANCE FLOOR: direct mention_type >= 7, indirect >= 5
- Automated system alerts/notifications: score LOW unless a human has manually replied
- Adapt summary length: relevance 8-10 = up to 200 words, 5-7 = up to 100 words, 1-4 = up to 30 words (hint: ~{word_hint} words)
- Keep all person names, ticket IDs, dates, and concrete next actions

Entity extraction rules:
- work_items: Extract Jira ticket IDs (e.g., DPD-715, OMNI-1191), PR numbers (e.g., PR #649), project codenames (e.g., BCRS, RMN, BLIGHT), service names (e.g., lt-strudel-api, offer-service), and git repository names. Empty list if none found.
- people: Extract ONLY explicit person names (e.g., "Nikhil Grover", "Alvin Choo"). Do NOT include group names, team names, or distribution lists. Empty list if none.
- labels: Generate exactly 5 descriptive 2-word labels (lowercase, hyphenated) that best characterize this resource's topic and activity. Prefer domain-specific terms over generic ones.

Return ONLY valid JSON:
{{"relevance": <integer 1-10>, "summary": "<your summary>", "work_items": ["<id1>", "<id2>"], "people": ["<person1>", "<person2>"], "labels": ["<word-word>", "<word-word>", "<word-word>", "<word-word>", "<word-word>"]}}""")

    return "\n".join(parts)


# ── Response Parser ──────────────────────────────────────────────────


def parse_llm_response(raw: str, mention_type: str) -> SummaryResult:
    """Parse LLM JSON response with fallback to regex extraction."""
    if raw.startswith("<think>"):
        think_end = raw.find("</think>")
        if think_end != -1:
            raw = raw[think_end + 8:].strip()

    if raw.startswith("```"):
        raw = re.sub(r"^```\w*\n?", "", raw)
        raw = re.sub(r"\n?```$", "", raw)
        raw = raw.strip()

    try:
        data = json.loads(raw)
        relevance = int(data["relevance"])
        summary = str(data["summary"])
        work_items = [str(x) for x in data.get("work_items", [])]
        people = [str(x) for x in data.get("people", [])]
        labels = [str(x) for x in data.get("labels", [])][:5]
    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        eprint(f"WARNING: JSON parse failed, using regex fallback. Raw: {raw[:200]}")
        match = re.search(r'"relevance"\s*:\s*(\d+)', raw)
        relevance = int(match.group(1)) if match else 5
        summary_match = re.search(r'"summary"\s*:\s*"((?:[^"\\]|\\.)*)"', raw)
        summary = summary_match.group(1) if summary_match else raw
        work_items, people, labels = [], [], []

    floor = _RELEVANCE_FLOORS.get(mention_type, 1)
    relevance = max(min(relevance, 10), floor)

    return SummaryResult(relevance, summary, work_items, people, labels)


# ── LLM Call ─────────────────────────────────────────────────────────


def _call_llm(system_prompt: str, user_prompt: str) -> str:
    """Call LiteLLM proxy with native JSON mode and exponential backoff."""
    url = f"{LITELLM_BASE}/chat/completions"
    headers = {"Content-Type": "application/json"}
    if LITELLM_API_KEY:
        headers["Authorization"] = f"Bearer {LITELLM_API_KEY}"

    payload = {
        "model": SUMMARIZE_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.3,
        "response_format": {"type": "json_object"},
    }

    last_error: Optional[Exception] = None
    for attempt in range(1, SUMMARIZE_RETRIES + 2):
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=120)
        except requests.RequestException as exc:
            last_error = exc
            if attempt <= SUMMARIZE_RETRIES:
                wait = SUMMARIZE_RETRY_INITIAL_SEC * (2 ** (attempt - 1))
                eprint(f"  [retry {attempt}/{SUMMARIZE_RETRIES}] Connection error: {exc} - retrying in {wait:.0f}s")
                time.sleep(wait)
                continue
            raise RuntimeError(f"Summarization connection failed after {SUMMARIZE_RETRIES} retries: {exc}") from exc

        if resp.status_code >= 500:
            last_error = RuntimeError(f"Summarization API returned {resp.status_code}: {resp.text[:300]}")
            if attempt <= SUMMARIZE_RETRIES:
                wait = SUMMARIZE_RETRY_INITIAL_SEC * (2 ** (attempt - 1))
                eprint(f"  [retry {attempt}/{SUMMARIZE_RETRIES}] 5xx error ({resp.status_code}) - retrying in {wait:.0f}s")
                time.sleep(wait)
                continue
            raise last_error

        if resp.status_code != 200:
            raise RuntimeError(f"Summarization API returned {resp.status_code}: {resp.text[:300]}")

        data = resp.json()
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        if not content:
            raise RuntimeError(f"Summarization API returned empty content")
        return content.strip()

    raise RuntimeError(f"Summarization failed after {SUMMARIZE_RETRIES} retries") from last_error


# ── Public API ───────────────────────────────────────────────────────


def summarize_resource(
    title: str,
    source_type: str,
    atomic_items: list[dict],
    metadata: Optional[dict] = None,
    existing_summary: Optional[str] = None,
    mention_type: str = "none",
) -> SummaryResult:
    """Summarize a Jira ticket and return structured result with relevance score.

    Returns a SummaryResult with relevance, summary text, and extracted entities.
    """
    if not atomic_items:
        return SummaryResult(
            relevance=_RELEVANCE_FLOORS.get(mention_type, 1),
            summary=existing_summary or "",
        )

    content_parts = []
    for item in atomic_items:
        author = item.get("author", "Unknown")
        ts = item.get("created_at", "")
        text = item.get("content", "")
        if text:
            content_parts.append(f"[{ts}] {author}: {text}")

    content_block = "\n---\n".join(content_parts)
    meta_json = json.dumps(metadata or {}, indent=2, ensure_ascii=False)

    system_prompt = _build_system_prompt()
    user_prompt = _build_user_prompt(
        title, source_type, meta_json, content_block,
        mention_type, existing_summary,
    )

    raw = _call_llm(system_prompt, user_prompt)
    return parse_llm_response(raw, mention_type)
