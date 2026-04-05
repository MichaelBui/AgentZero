# Relevance-Scored Summarization Pipeline - Design Document

> Last reviewed: 2026-04-05

## Problem Statement

The daily work report aggregates content from Jira, Gmail, and GChat into a unified briefing. Current issues:
- **~537K tokens** across 958 summaries (Jira: 64, Gmail: 636, GChat: 258) - ~2x the Qwen 3.5 35B context window
- **~70-80% noise**: automated alerts (968 msgs from Shopping Cart Notification, 1295 from #dd-dpd-engage-alert), system emails (262 from dpd-rmn-alert, 83 from Opsgenie), calendar auto-responses
- **Slow inference**: large context causes long LLM processing times
- **No relevance signal**: all content treated equally regardless of user involvement

## Architecture

```
Fetch (cron) --> Cache atomic items --> Detect mention_type per atomic item
                                            |
                                            v
                                  Propagate STRONGEST mention_type to resource_summary
                                            |
                                            v
                                  Summarize (LLM) with:
                                    - response_format: {"type": "json_object"} (native JSON mode)
                                    - User.md as system context (~200 tokens)
                                    - mention_type as relevance hint
                                    - Relevance floors: direct>=7, indirect>=5
                                    - Output: {"relevance", "summary", "work_items", "people", "labels"}
                                            |
                                            v
                                  Store: estimated_relevance, final_relevance, entities (JSON)
                                            |
                                            v
                                  Daily Report: read from DB, filter by final_relevance >= threshold
                                  Cross-source linking: group by shared work_items/people/labels
```

## 1. mention_type Detection

### Principle

mention_type is about the **resource** (conversation/thread/ticket), not the summary. If ANY atomic item in a resource has a stronger signal, the whole resource inherits it.

**Propagation rule:** `resource.mention_type = max(all child atomic items)` where `direct > indirect > none`.

**User participation = direct mention.** If Michael replied/participated in any item, it signals active interest.

### Per-Source Detection Rules

#### Jira

| Signal | mention_type | Detection Method |
|---|---|---|
| assignee = 'Michael Bui' | direct | metadata.assignee field |
| reporter = 'Michael Bui' | direct | metadata.reporter field |
| Michael authored a comment | direct | atomic_content.author match |
| Comment text contains '@Michael' or 'Michael Bui' | direct | content text search |
| Linked to a ticket Michael owns | indirect | ticket_relationships cross-lookup |
| Everything else | none | default |

#### Gmail

| Signal | mention_type | Detection Method |
|---|---|---|
| `to` contains michael.bui@fairpricegroup.sg | direct | metadata.to list |
| Author IS Michael (he sent/replied) | direct | atomic_content.author match |
| `cc` contains Michael's email | indirect | metadata.cc list |
| Distribution list / no personal address | none | default |

#### GChat

| Signal | mention_type | Detection Method |
|---|---|---|
| resource_id starts with 'dm/' | direct | resource_id prefix |
| Michael authored a message | direct | atomic_content.author = 'Michael Bui' |
| Content contains '@Michael' (case-insensitive) | direct | content text search |
| Chat title includes 'Michael' in participants | indirect | resource_summary.title |
| Group chat, no participation, no @mention | none | default |

### Data Validation (from actual cache)

- GChat: Michael participated in 114/258 resources (44%)
- Gmail: Michael sent 225/1534 emails
- Jira: Michael authored 64/384 items

## 2. DB Schema Changes

On `resource_summary` table in all 3 DBs (jira_cache.db, gmail_cache.db, gchat_cache.db):

```sql
ALTER TABLE resource_summary ADD COLUMN mention_type TEXT DEFAULT 'none';
ALTER TABLE resource_summary ADD COLUMN estimated_relevance INTEGER DEFAULT 0;
ALTER TABLE resource_summary ADD COLUMN final_relevance INTEGER DEFAULT 0;
```

Total: 3 new columns for relevance scoring. Entity fields (work_items, people, labels) stored inside existing `metadata` JSON blob - no additional columns needed.

On `atomic_content` - NO schema change. mention_type stored inside existing `metadata` JSON blob per item.

## 3. Entity Extraction (Cross-Source Linking)

Each summarization extracts three entity categories for cross-source correlation:

### JSON Output Format

```json
{
  "relevance": 7,
  "summary": "DPD-715: Task assigned to Michael to use tagged-based pricing. Nikhil raised PR #649 on lt-strudel-api. Pending code review.",
  "work_items": ["DPD-715", "PR #649", "lt-strudel-api", "BCRS"],
  "people": ["Nikhil Grover"],
  "labels": ["pricing-migration", "code-review", "task-assignment", "pull-request", "backend-api"]
}
```

### Entity Categories

| Field | Content | Purpose |
|---|---|---|
| `work_items` | Jira ticket IDs (DPD-715), PR numbers (PR #649), project codenames (BCRS, RMN, BLIGHT), service names (lt-strudel-api, offer-service), git repositories (bitbucket.org/ntuclink/...) | Link same work item across Jira, email, and chat |
| `people` | Explicit person names ONLY (e.g., "Nikhil Grover", "Alvin Choo"). NO group names, team names, or distribution lists | Identify who specifically is involved |
| `labels` | 5 most relevant 2-word descriptive labels, AI-generated | Semantic linking when no shared IDs exist |

### Label Guidelines (for LLM prompt)

- Exactly 5 labels per resource
- Each label is exactly 2 words, lowercase, hyphenated (e.g., "pricing-migration", "code-review")
- Labels should be descriptive and suggestive of the topic/activity
- Prefer domain-specific terms over generic ones (e.g., "delivery-latency" over "performance-issue")

### Storage (Inside metadata JSON)

Entities are stored inside the existing `resource_summary.metadata` JSON blob:

```json
{
  "existing_key": "existing_value",
  "work_items": ["DPD-715", "PR #649", "lt-strudel-api"],
  "people": ["Nikhil Grover"],
  "labels": ["pricing-migration", "code-review", "task-assignment", "pull-request", "backend-api"]
}
```

**Rationale:** SQLite 3.9+ supports JSON operations (`json_extract`, `json_each`), and the primary filter is always `WHERE final_relevance >= N` (which uses a dedicated column). Entity lookups are secondary and done in Python after relevance filtering. Storing entities in metadata keeps the schema simpler and extensible - adding new entity types requires no ALTER TABLE.

### Cross-Source Linking (Report Assembly)

When building the daily report, group resources that share `work_items` or `people`:
```python
# Pseudo-code for report assembly
groups = defaultdict(list)
for resource in summaries:
    for item in resource.work_items:
        groups[item].append(resource)
    for person in resource.people:
        groups[person].append(resource)

# Feed each multi-source group to LLM for synthesis
for key, related_resources in groups.items():
    if len(related_resources) > 1 and sources_differ(related_resources):
        synthesize(key, related_resources)
```

Labels enable secondary grouping for items without shared IDs but related topics.

## 4. Structured JSON Output (Native JSON Mode)

The full chain supports `response_format: {"type": "json_object"}`:

| Layer | Support | Notes |
|---|---|---|
| Qwen 3.5 35B | Yes | Non-thinking mode only (our model uses :instruct-reasoning with enable_thinking=false) |
| llama.cpp | Yes | Supports response_format with json_object type natively |
| llama-swap | Pass-through | Does NOT strip response_format (only strips temperature, top_p, etc.) |
| LiteLLM | Pass-through | Passes response_format to custom_openai providers |

**Requirement:** Prompt MUST contain the word "JSON" (case-insensitive) for json_object mode.

**Fallback:** If JSON parsing fails, regex extraction: `"relevance"\s*:\s*(\d+)` + treat rest as summary.

## 5. Relevance Scoring

### Floors

| mention_type | Floor | Rationale |
|---|---|---|
| direct | 7 | Michael actively participated or was explicitly addressed |
| indirect | 5 | Michael is in the audience but not directly engaged |
| none | 1 | No personal involvement detected |

Enforced in BOTH the prompt (LLM instruction) AND code (safety net clamp).

### Production Incident Handling

Automated alerts (Opsgenie, Datadog, watchdog, notification channels) score LOW unless a human has manually replied in the thread. The LLM determines this from the content.

### Adaptive Summary Length

| Relevance | Max Words | Content Focus |
|---|---|---|
| 8-10 (High) | 200 | Full detail: actions, decisions, deadlines, people, context |
| 5-7 (Medium) | 100 | Key status updates and pending items |
| 1-4 (Low) | 30 | One-liner: what it is and whether action needed |

## 6. LLM Prompt

```
SYSTEM:
You are a relevance-scoring executive assistant. Score the relevance, summarize,
and extract entities from the content for the following user.

[--- User.md content (~200 tokens) ---]

USER:
Analyze this {source_type} resource and return a JSON response.

Resource: {title}
Mention Type: {mention_type}
  - direct: user is explicitly addressed, assigned, tagged, or has actively participated/replied
  - indirect: user is in recipient/participant list but not directly addressed
  - none: no personal involvement detected
Metadata: {meta_json}

Content (chronological):
{content}

Scoring rules:
- Refer to the user's "What Matters Most" section for scoring guidance
- RELEVANCE FLOOR: direct mention_type >= 7, indirect >= 5
- Automated system alerts/notifications: score LOW unless a human has manually replied
- Adapt summary length: relevance 8-10 = up to 200 words, 5-7 = up to 100 words, 1-4 = up to 30 words
- Keep all person names, ticket IDs, dates, and concrete next actions

Entity extraction rules:
- work_items: Extract Jira ticket IDs (e.g., DPD-715, OMNI-1191), PR numbers (e.g., PR #649), project codenames (e.g., BCRS, RMN, BLIGHT), service names (e.g., lt-strudel-api, offer-service), and git repository names. Empty list if none found.
- people: Extract ONLY explicit person names (e.g., "Nikhil Grover", "Alvin Choo"). Do NOT include group names, team names, or distribution lists. Empty list if none.
- labels: Generate exactly 5 descriptive 2-word labels (lowercase, hyphenated) that best characterize this resource's topic and activity. Prefer domain-specific terms over generic ones.

Return ONLY valid JSON:
{
  "relevance": <integer 1-10>,
  "summary": "<your summary>",
  "work_items": ["<id1>", "<id2>"],
  "people": ["<person-name1>", "<person-name2>"],
  "labels": ["<word-word>", "<word-word>", "<word-word>", "<word-word>", "<word-word>"]
}
```

## 7. Response Parser

```python
@dataclass
class SummaryResult:
    relevance: int
    summary: str
    work_items: list[str]
    people: list[str]
    labels: list[str]

def parse_llm_response(raw: str, mention_type: str) -> SummaryResult:
    # Strip <think> block if present
    if raw.startswith('<think>'):
        think_end = raw.find('</think>')
        if think_end != -1:
            raw = raw[think_end + 8:].strip()
    
    # Strip markdown code fences if present
    if raw.startswith('```'):
        raw = re.sub(r'^```\w*\n?', '', raw)
        raw = re.sub(r'\n?```$', '', raw)
    
    # Try JSON parse
    try:
        data = json.loads(raw)
        relevance = int(data['relevance'])
        summary = str(data['summary'])
        work_items = [str(x) for x in data.get('work_items', [])]
        people = [str(x) for x in data.get('people', [])]
        labels = [str(x) for x in data.get('labels', [])][:5]
    except (json.JSONDecodeError, KeyError, TypeError):
        # Fallback: regex extraction
        match = re.search(r'"relevance"\s*:\s*(\d+)', raw)
        relevance = int(match.group(1)) if match else 5
        summary = re.sub(r'\{[^}]*"relevance"[^}]*\}', '', raw).strip()
        if not summary:
            summary = raw
        work_items, people, labels = [], [], []
    
    # Enforce floor
    floor = {'direct': 7, 'indirect': 5, 'none': 1}.get(mention_type, 1)
    relevance = max(min(relevance, 10), floor)
    
    return SummaryResult(relevance, summary, work_items, people, labels)
```

## 8. Migration Plan (one-time)

1. Add 3 columns to `resource_summary` in all 3 DBs
2. Backfill `mention_type` for all existing resources by scanning child atomic items
3. Clear all existing summaries (set summary=NULL, estimated_relevance=0, final_relevance=0)
4. Re-run summarization on all resources with new prompt + JSON mode
5. Estimated time: ~4 hours for 958 resources at ~15s/call

## 9. Files to Modify

| File | Change | Est. Lines |
|---|---|---|
| gchat_db.py | Add 3 columns, mention_type propagation, entity storage | ~50 |
| Jira DB module | Same schema + mention detection + entity storage | ~50 |
| Gmail DB module | Same schema + mention detection + entity storage | ~50 |
| jira_summarizer.py | New prompt with entities, JSON output, response_format, User.md, parser | ~90 |
| GChat summarizer | Same prompt changes | ~90 |
| Gmail summarizer | Same prompt changes | ~90 |
| jira_reader.py | Add mention_type detection during fetch | ~30 |
| gchat_reader.py | Same fetch-time mention detection | ~30 |
| Gmail reader | Same fetch-time mention detection | ~30 |
| NEW: relevance_utils.py | Shared parser (SummaryResult), mention_type compute, prompt builder, entity merge | ~80 |
| **Total** | | **~590 lines** |

## 10. Design Decisions Log

| # | Decision | Rationale |
|---|---|---|
| 1 | mention_type on both atomic items (JSON) and resource_summary (column) | Strongest signal propagation; column enables fast SQL filtering |
| 2 | User participation/reply = direct mention | Active interest indicator across all sources |
| 3 | Relevance floor: direct=7, indirect=5, none=1 | Prompt + code enforcement prevents under-scoring |
| 4 | Production alerts: low unless human replied | Reduces noise from automated monitoring |
| 5 | Native JSON mode via response_format | Reliable structured output, no free-text parsing |
| 6 | Adaptive length: 200/100/30 words | Single-pass; reduces total output by ~60-70% |
| 7 | One-time full re-summarization on migration | Consistent scoring across all items |
| 8 | User.md as system context (~200 tokens) | Stable professional profile, rarely changes |
| 9 | final_relevance = estimated initially, user-adjustable | Enables human-in-the-loop correction |
| 10 | No batch ordering, no token budget guard | Keep it simple; trust the AI |
| 11 | Entity extraction (work_items, people, labels) in same LLM call | Zero extra cost; enables cross-source linking |
| 12 | AI-generated 2-word labels for semantic linking | Catches related content without shared IDs |
| 13 | Timeline summarization deferred to Phase 2 | Relevance filtering must stabilize first |
| 14 | work_items includes service names and git repos | Services and repos are work identifiers that appear across sources |
| 15 | people contains ONLY person names (no groups/teams) | Clean person-level linking; groups go in labels if needed |
| 16 | Entities stored inside metadata JSON (not dedicated columns) | Extensible without schema changes; primary filter is relevance column; SQLite JSON ops available for queries if needed |

## 11. Risk Matrix

| Risk | Severity | Mitigation |
|---|---|---|
| JSON parse failure | Medium | Regex fallback + logging |
| Score inconsistency across calls | Medium | Temperature controlled by llama-swap, rubric in prompt |
| False negative on critical group chat | High | LLM reads content + User.md guidance; mention_type is BOOST not GATE |
| Author name matching edge cases | Low | Use full name 'Michael Bui' and specific email |
| User.md staleness | Low | Generic/role-based; add 'last reviewed' date |
| Re-summarization time (~4h) | Low | One-time cost, acceptable |
| Label inconsistency across calls | Medium | LLM may generate different labels for similar content; labels are supplementary to work_items/people for linking |
| Entity extraction misses | Low | Primary linking is via work_items (deterministic IDs); labels are secondary |

## 12. Future Phases

### Phase 2: Timeline Summarization (after Phase 1 stabilizes)

- Daily digest: cron at end-of-day, combine resources with final_relevance >= 5
- Weekly rollup: combine 5-7 daily digests
- Monthly rollup: combine 4 weekly digests
- New `timeline_digest` table: `{period, date, summary, token_count}`

### Phase 3: Embedding-Based Semantic Linking (optional)

- Generate embeddings for each summary
- Store in vector DB for semantic similarity search
- Catches connections without shared IDs (e.g., "delivery performance" relates to "FFS latency")
