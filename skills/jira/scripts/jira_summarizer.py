"""
AI summarization for Jira tickets via LiteLLM proxy.

Generates concise summaries of Jira tickets using a lightweight model
to reduce tokens for downstream reasoning.
"""

import json
import os
import sys
from typing import Optional

import requests

LITELLM_BASE = os.environ.get("LITELLM_BASE_URL", "https://llm.gigary.com/v1")
SUMMARIZE_MODEL = os.environ.get("SUMMARIZE_MODEL", "local/qwen3.5-35b-a3b:instruct-reasoning")
LITELLM_API_KEY = os.environ.get("API_KEY_OTHER", os.environ.get("LLAMA_TOKEN", ""))
MAX_SUMMARY_WORDS = int(os.environ.get("MAX_SUMMARY_WORDS", "500"))


def eprint(*a, **kw):
    print(*a, file=sys.stderr, **kw)


def summarize_resource(
    title: str,
    source_type: str,
    atomic_items: list[dict],
    metadata: Optional[dict] = None,
    existing_summary: Optional[str] = None,
) -> str:
    """Generate a summary for a logical resource from its atomic content.

    If existing_summary is provided, uses an anchored update approach
    to extend the existing summary with new content, preserving historical context.
    """
    if not atomic_items:
        return existing_summary or ""

    content_parts = []
    for item in atomic_items:
        author = item.get("author", "Unknown")
        ts = item.get("created_at", "")
        text = item.get("content", "")
        if text:
            content_parts.append(f"[{ts}] {author}: {text}")

    content_block = "\n---\n".join(content_parts)
    meta_json = json.dumps(metadata or {}, indent=2, ensure_ascii=False)

    if existing_summary:
        prompt = _build_update_prompt(title, source_type, meta_json, existing_summary, content_block)
    else:
        prompt = _build_full_prompt(title, source_type, meta_json, content_block)

    return _call_llm(prompt)


def _build_full_prompt(title: str, source_type: str, meta_json: str, content: str) -> str:
    return f"""You are a concise executive assistant. Summarize the following {source_type} content for a daily work briefing.

Resource: {title}
Metadata: {meta_json}

Content (chronological):
{content}

Instructions:
- Identify: What is the current status/state?
- Identify: What actions are pending and who owns them?
- Identify: What decisions were made?
- Identify: Key dates, deadlines, blockers
- Keep all person names, ticket IDs, dates, and technical references
- Be factual and specific - do not generalize
- Maximum {MAX_SUMMARY_WORDS} words"""


def _build_update_prompt(
    title: str, source_type: str, meta_json: str, existing: str, new_content: str
) -> str:
    return f"""You are a concise executive assistant. Update the existing summary with new information.

Resource: {title}
Metadata: {meta_json}

Existing summary:
{existing}

New content to incorporate:
{new_content}

Instructions:
- Merge the new information into the existing summary
- Update status, pending actions, and decisions based on new content
- Remove outdated information that is contradicted by new content
- Keep all person names, ticket IDs, dates, and technical references
- Preserve historical context from the existing summary that is still relevant
- Be factual and specific - do not generalize
- Maximum {MAX_SUMMARY_WORDS} words"""


def _call_llm(prompt: str) -> str:
    """Call LiteLLM proxy for summarization."""
    url = f"{LITELLM_BASE}/chat/completions"
    headers = {"Content-Type": "application/json"}
    if LITELLM_API_KEY:
        headers["Authorization"] = f"Bearer {LITELLM_API_KEY}"

    payload = {
        "model": SUMMARIZE_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
    }

    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=120)
        if resp.status_code != 200:
            eprint(f"WARN: Summarization API returned {resp.status_code}: {resp.text[:200]}")
            return ""
        data = resp.json()
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        if content.startswith("<think>"):
            think_end = content.find("</think>")
            if think_end != -1:
                content = content[think_end + len("</think>"):].strip()
        return content.strip()
    except requests.exceptions.Timeout:
        eprint("WARN: Summarization request timed out (120s)")
        return ""
    except Exception as e:
        eprint(f"WARN: Summarization failed: {e}")
        return ""
