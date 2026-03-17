"""
Deterministic text cleanup for Jira content.

Strips noise (technical command outputs, large JSON dumps, HTML artifacts)
to reduce token count before caching and summarization. Zero LLM cost.
"""

import re


_HTML_TAG_RE = re.compile(r"<[^>]+>")
_MULTI_NEWLINE_RE = re.compile(r"\n{3,}")
_MULTI_SPACE_RE = re.compile(r" {3,}")

_TECHNICAL_DUMP_PATTERNS = [
    re.compile(r"(?:^|\n)(?:PORT\s+STATE.*\n(?:.*\n){3,50})", re.MULTILINE),
    re.compile(r"(?:^|\n)\$\s+(?:nmap|sslscan|curl|gsutil|gcloud)\s.*?(?=\n\$|\n\n\n|\Z)", re.DOTALL),
    re.compile(r"\{[^{}]*\"__metadata\"[^{}]*\{[^{}]*\}[^{}]*\}", re.DOTALL),
    re.compile(r"\{[^{}]*\"uri\":\s*\"http[^\"]+/sap/[^{}]+\}", re.DOTALL),
]


def clean_html(text: str) -> str:
    """Remove HTML tags and decode common entities."""
    text = _HTML_TAG_RE.sub("", text)
    text = text.replace("&nbsp;", " ").replace("&amp;", "&")
    text = text.replace("&lt;", "<").replace("&gt;", ">")
    text = text.replace("&quot;", '"').replace("&#39;", "'")
    return text


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
