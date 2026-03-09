# Agent Skills — Authoring Guide

Instructions for AI agents creating or modifying skills in this directory. Every skill must follow these conventions to ensure consistency, discoverability, and reliable integration with Agent Zero.

## Directory Structure

```
skills/
├── AGENTS.md              ← This file
├── {skill-name}/
│   ├── SKILL.md           ← Skill definition (required)
│   └── scripts/
│       └── {script}.py    ← Executable Python script(s)
```

**Naming:** kebab-case for directories (`gmail-thread-reader`), snake_case for Python files (`gmail_thread_reader.py`).

## SKILL.md Format

Every skill must have a `SKILL.md` with YAML frontmatter and structured sections.

### Required Frontmatter

```yaml
---
name: skill-name
description: >-
  One-paragraph description using exact phrases a user would say to trigger this skill.
  Discoverability depends entirely on this text — vague descriptions mean the skill never loads.
version: 1.0.0
author: Michael
tags: [tag1, tag2, tag3]
---
```

**Description rules:**
- Write as if answering: "What would the user say when they need this?"
- Include synonyms and action verbs (`fetch`, `list`, `read`, `check`, `search`, `query`)
- Mention the data source explicitly (`Jira`, `Gmail`, `git`, `ntfy.sh`)

### Required Sections

| Section | Purpose |
|---------|---------|
| When to Use / When NOT to Use | Clear scope boundaries to avoid misuse |
| Prerequisites / Required Environment Variables | What must be set up before running |
| Usage (with examples) | Copy-paste-ready `bash` commands |
| Arguments (table) | All CLI arguments with Required, Default, Description |
| Output | What goes to stdout vs stderr, example JSON structure |
| Notes | Implementation details, limitations, performance characteristics |
| Files | List of files in the skill directory |

## Python Script Conventions

### Output Rules (Critical)

**All scripts must support `--format json|yaml` with `json` as default.** No table, markdown, or plain text output to stdout.

```python
def output_data(data, fmt: str = "json"):
    """Output data as JSON (default) or YAML to stdout."""
    if fmt == "yaml":
        import yaml
        print(yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False))
    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))
```

Add the argument:

```python
parser.add_argument(
    "--format", choices=["json", "yaml"], default="json",
    help="Output format (default: json)"
)
```

### Stream Separation

| Stream | Content |
|--------|---------|
| **stdout** | Structured data only (JSON/YAML). This is what downstream consumers parse. |
| **stderr** | Progress info, debug logs, connection status, warnings, errors. |

Use `eprint()` for all human-readable messages:

```python
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
```

### Script Template

```python
#!/usr/bin/env python3
"""
{Skill Name}
{'=' * len(skill_name)}
One-line description of what this script does.

Output: JSON/YAML to stdout. Progress/debug to stderr.
Requires: {dependencies}
"""

import argparse
import json
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def output_data(data, fmt: str = "json"):
    if fmt == "yaml":
        import yaml
        print(yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False))
    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description="...")
    # ... add arguments ...
    parser.add_argument("--format", choices=["json", "yaml"], default="json",
                        help="Output format (default: json)")
    args = parser.parse_args()

    # ... skill logic ...

    output_data(result, args.format)


if __name__ == "__main__":
    main()
```

### Authentication & Secrets

- Use environment variables for credentials (`JIRA_EMAIL`, `JIRA_API_KEY`)
- Validate early with clear error messages to stderr
- Mask secrets in logs: show only first 3 and last 3 characters

```python
masked = f"{api_key[:3]}...{api_key[-3:]} (Length: {len(api_key)})"
eprint(f"API Key detected: {masked}")
```

- **Never** hardcode secrets in scripts
- **Never** print full secret values

### Error Handling

- Use `sys.exit(1)` with a clear error message to stderr on fatal errors
- Implement retry with exponential backoff for network calls
- Distinguish between retryable (network timeout) and permanent (401, 404) errors

```python
def request_with_retry(method, url, max_retries=3, **kwargs):
    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.request(method, url, timeout=30, **kwargs)
            if resp.status_code == 401:
                eprint("ERROR: Authentication failed.")
                sys.exit(1)
            return resp
        except requests.exceptions.Timeout:
            if attempt < max_retries:
                time.sleep(2 ** attempt)
            else:
                eprint("ERROR: All retry attempts timed out.")
                sys.exit(1)
```

### Dependencies

- **Standard library preferred** (`json`, `argparse`, `sys`, `time`, `os`, `base64`)
- **Approved external packages:** `requests`, `pyyaml`, `playwright`
- Import optional dependencies inside functions to fail gracefully:

```python
def output_data(data, fmt="json"):
    if fmt == "yaml":
        import yaml  # Only imported when yaml format is requested
        ...
```

### Argparse Conventions

- Use `--kebab-case` for argument names
- Always provide `default` and `help` for optional arguments
- Use `choices` for enum-like arguments
- Required arguments use `required=True`

## Skill Categories

| Category | Pattern | Examples |
|----------|---------|---------|
| **Data Fetching** | Connect → Query → Format → Output | jira-query-listing, gmail-thread-reader |
| **Action** | Validate → Execute → Report Result | notify-user, git-backup |

Data fetching skills return arrays of objects. Action skills return a result object with a `success` boolean.

## Testing Checklist

Before marking a skill complete:

1. `python script.py --help` renders correctly
2. `python script.py [args] --format json` produces valid JSON
3. `python script.py [args] --format yaml` produces valid YAML
4. stderr contains progress info, stdout contains only structured data
5. Error cases produce clear messages and `sys.exit(1)`
6. Secrets are masked in all log output
7. SKILL.md arguments table matches actual `argparse` definitions

## Do

- Keep scripts self-contained (one file per skill when possible)
- Use `argparse` for all parameters — no positional-only hacks
- Log progress to stderr so stdout stays clean for piping
- Make scripts executable (`chmod +x`)
- Version bump in SKILL.md frontmatter on every change

## Don't

- Output tables, markdown, or plain text to stdout
- Hardcode credentials or API keys
- Print full secret values anywhere
- Use `print()` for progress — use `eprint()` (stderr)
- Create deep directory hierarchies — keep it flat: `SKILL.md` + `scripts/`
- Silently swallow errors — fail loudly with context
