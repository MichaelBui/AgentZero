"""
Deterministic text cleanup for Agent Zero skills.

Strips noise (signatures, HTML, quoted text, bot messages, technical dumps)
to reduce token count before caching or summarization. Zero LLM cost.
"""

import re


_SIG_PATTERNS = [
    r"\n--\s*\n.*",
    r"\nBest regards[\s\S]*",
    r"\nKind regards[\s\S]*",
    r"\nRegards[\s,]*\n[\s\S]*",
    r"\nCheers[\s,]*\n[\s\S]*",
    r"\nThanks[\s,]*\n[A-Z][\s\S]{0,200}$",
    r"\nSent from my [\w\s]+[\s\S]*",
    r"\nGet Outlook for [\w\s]+[\s\S]*",
]
_SIG_RE = re.compile("|".join(_SIG_PATTERNS), re.IGNORECASE)

_QUOTED_REPLY_RE = re.compile(
    r"(?:^|\n)On .{10,120} wrote:\s*\n[\s\S]*", re.MULTILINE
)
_QUOTED_LINE_RE = re.compile(r"(^>.*\n?)+", re.MULTILINE)

_HTML_TAG_RE = re.compile(r"<[^>]+>")
_MULTI_NEWLINE_RE = re.compile(r"\n{3,}")
_MULTI_SPACE_RE = re.compile(r" {3,}")

_TECHNICAL_DUMP_PATTERNS = [
    re.compile(r"(?:^|\n)(?:PORT\s+STATE.*\n(?:.*\n){3,50})", re.MULTILINE),
    re.compile(r"(?:^|\n)\$\s+(?:nmap|sslscan|curl|gsutil|gcloud)\s.*?(?=\n\$|\n\n\n|\Z)", re.DOTALL),
    re.compile(r"\{[^{}]*\"__metadata\"[^{}]*\{[^{}]*\}[^{}]*\}", re.DOTALL),
    re.compile(r"\{[^{}]*\"uri\":\s*\"http[^\"]+/sap/[^{}]+\}", re.DOTALL),
]

_BOT_PATTERNS = [
    re.compile(r"^\[?\d{1,2}:\d{2}\s*(?:AM|PM)?\]?\s*(?:Datadog|PagerDuty|Jira|GitHub|Bitbucket)\s*(?:Bot|App).*", re.IGNORECASE | re.MULTILINE),
]


def clean_html(text: str) -> str:
    """Remove HTML tags and decode common entities."""
    text = _HTML_TAG_RE.sub("", text)
    text = text.replace("&nbsp;", " ").replace("&amp;", "&")
    text = text.replace("&lt;", "<").replace("&gt;", ">")
    text = text.replace("&quot;", '"').replace("&#39;", "'")
    return text


def clean_email_body(text: str) -> str:
    """Strip signatures, quoted replies, HTML artifacts from email body."""
    if not text:
        return ""
    text = clean_html(text)
    text = _QUOTED_REPLY_RE.sub("\n[...quoted reply removed...]", text)
    text = _QUOTED_LINE_RE.sub("", text)
    text = _SIG_RE.sub("", text)
    text = _normalize_whitespace(text)
    return text.strip()


def clean_chat_message(text: str) -> str:
    """Strip bot noise and monitoring tags from chat messages."""
    if not text:
        return ""
    for pat in _BOT_PATTERNS:
        text = pat.sub("", text)
    text = _normalize_whitespace(text)
    return text.strip()


def clean_jira_text(text: str) -> str:
    """Strip technical command outputs and large JSON dumps from Jira content."""
    if not text:
        return ""
    for pat in _TECHNICAL_DUMP_PATTERNS:
        text = pat.sub("\n[...technical output removed...]\n", text)
    text = _normalize_whitespace(text)
    return text.strip()


def _normalize_whitespace(text: str) -> str:
    text = _MULTI_NEWLINE_RE.sub("\n\n", text)
    text = _MULTI_SPACE_RE.sub(" ", text)
    return text


def truncate(text: str, max_chars: int = 2000) -> str:
    """Hard truncate text with marker. Preserves word boundaries when possible."""
    if not text or len(text) <= max_chars:
        return text
    cut = text[:max_chars]
    last_space = cut.rfind(" ", max_chars - 100, max_chars)
    if last_space > 0:
        cut = cut[:last_space]
    return cut + " [truncated]"
