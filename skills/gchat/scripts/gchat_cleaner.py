"""
Deterministic text cleanup for the GChat skill.

Strips bot noise, monitoring tags, and normalizes whitespace
to reduce token count before caching or summarization. Zero LLM cost.
"""

import re

_BOT_PATTERNS = [
    re.compile(
        r"^\[?\d{1,2}:\d{2}\s*(?:AM|PM)?\]?\s*"
        r"(?:Datadog|PagerDuty|Jira|GitHub|Bitbucket|Google Calendar|Meet)\s*"
        r"(?:Bot|App).*",
        re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(r"^\[ALERT\].*$", re.MULTILINE),
    re.compile(r"^\[MONITORING\].*$", re.MULTILINE),
]

_MULTI_NEWLINE_RE = re.compile(r"\n{3,}")
_MULTI_SPACE_RE = re.compile(r" {3,}")


def clean_chat_message(text: str) -> str:
    """Strip bot noise and monitoring tags from chat messages."""
    if not text:
        return ""
    for pat in _BOT_PATTERNS:
        text = pat.sub("", text)
    text = _MULTI_NEWLINE_RE.sub("\n\n", text)
    text = _MULTI_SPACE_RE.sub(" ", text)
    return text.strip()
