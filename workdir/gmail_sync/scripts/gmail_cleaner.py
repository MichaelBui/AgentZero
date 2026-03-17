"""
Deterministic text cleanup for Gmail email bodies.

Strips noise (HTML artifacts, quoted replies, email signatures,
excessive whitespace) to reduce token count before caching and summarization.
Full content preserved - no truncation.
"""

import re


_HTML_TAG_RE = re.compile(r"<[^>]+>")
_MULTI_NEWLINE_RE = re.compile(r"\n{3,}")
_MULTI_SPACE_RE = re.compile(r" {3,}")

_QUOTED_REPLY_PATTERNS = [
    re.compile(r"On .{10,80} wrote:\s*\n.*", re.DOTALL),
    re.compile(r"-{2,}\s*Forwarded message\s*-{2,}.*", re.DOTALL),
    re.compile(r"From:\s+.+\nSent:\s+.+\nTo:\s+.+\n(?:Cc:\s+.+\n)?Subject:\s+.+\n.*", re.DOTALL),
    re.compile(r"_{3,}\nFrom:\s+.+$.*", re.DOTALL | re.MULTILINE),
]

_SIGNATURE_PATTERNS = [
    re.compile(r"\n--\s*\n.*", re.DOTALL),
    re.compile(r"\n(?:Best regards|Kind regards|Regards|Thanks|Cheers|Sincerely|Warm regards),?\s*\n.*", re.DOTALL | re.IGNORECASE),
    re.compile(r"\nSent from my (?:iPhone|iPad|Galaxy|Android|device).*", re.DOTALL | re.IGNORECASE),
    re.compile(r"\nGet Outlook for (?:iOS|Android).*", re.DOTALL | re.IGNORECASE),
]

_FOOTER_NOISE_PATTERNS = [
    re.compile(r"This email and any (?:files|attachments) .{50,500}(?:privileged|confidential).*", re.DOTALL | re.IGNORECASE),
    re.compile(r"CONFIDENTIALITY NOTICE:.*", re.DOTALL | re.IGNORECASE),
    re.compile(r"If you(?:'re| are) not the intended recipient.*", re.DOTALL | re.IGNORECASE),
]


def clean_html(text: str) -> str:
    """Remove HTML tags and decode common entities."""
    text = _HTML_TAG_RE.sub("", text)
    text = text.replace("&nbsp;", " ").replace("&amp;", "&")
    text = text.replace("&lt;", "<").replace("&gt;", ">")
    text = text.replace("&quot;", '"').replace("&#39;", "'")
    return text


def clean_email_body(text: str) -> str:
    """Full cleanup pipeline for an email message body."""
    if not text:
        return ""
    text = clean_html(text)
    for pat in _QUOTED_REPLY_PATTERNS:
        text = pat.sub("", text)
    for pat in _SIGNATURE_PATTERNS:
        text = pat.sub("", text)
    for pat in _FOOTER_NOISE_PATTERNS:
        text = pat.sub("", text)
    text = _normalize_whitespace(text)
    return text.strip()


def _normalize_whitespace(text: str) -> str:
    text = _MULTI_NEWLINE_RE.sub("\n\n", text)
    text = _MULTI_SPACE_RE.sub(" ", text)
    return text
