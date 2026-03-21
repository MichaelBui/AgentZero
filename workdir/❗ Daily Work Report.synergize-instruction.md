# Synthesis Instructions

You have just read the 3 source files (Jira, GChat, Gmail) and historical context. Now follow these steps exactly to produce the daily work report. Do NOT skip steps. Do NOT invent data. Do NOT produce vague summaries.

**Reference example:** Read `workdir/❗ Daily Work Report.example-v2.md` before writing. Match its structure, depth, cross-source synergization, and specificity exactly. Every section in your report must meet or exceed the quality bar set by v2.

---

## Step 1: Structured Pre-Analysis (think step by step using /think mode)

Before writing any report section, reason through the source data systematically. Use chain-of-thought reasoning to process each output file one at a time. For each item, classify it explicitly:

**A. Work stream grouping.** A "work stream" is a named project, initiative, or recurring process - NOT a ticket number or chat space. One work stream spans multiple sources (e.g., "BCRS Phase 2" may have Jira tickets, GChat threads, and emails). Group all related items under one work stream name.

**B. Classification per item.** For every source item, assign exactly one label:
- `ACTION` = Michael must personally do something (reply, approve, deploy, decide)
- `FOLLOW-UP` = Michael already acted; waiting on someone else
- `WORKSTREAM` = informational update, no action needed now
- `NOISE` = irrelevant or duplicate

**C. Cross-source correlation.** When the same topic appears in 2+ sources (Jira + GChat, Gmail + Jira, etc.), mark it as cross-source. These items are higher priority and must include all source references in the final output.

**D. Implied action detection.** Some items look informational but imply action:
- A question directed at Michael with no answer yet = `ACTION`
- A ticket blocked because Michael hasn't signed off = `ACTION`
- A team member waiting on Michael's input = `ACTION`
- A ticket Michael owns that is stalled = `FOLLOW-UP`
- An alert that auto-resolved = `WORKSTREAM`

**E. Priority assignment.**
- 🔴 Critical = deadline today or tomorrow, OR blocking someone else's work right now, OR executive-level request
- 🟡 Important = SLA risk this week, manager request, or team-level blocker
- 🟢 Low = no immediate deadline, can be batched

**F. Fact-check yourself.** Every claim in the report must trace back to a specific source item. Never infer or fabricate details. If a date, name, ticket key, or status appears in the report, it must exist verbatim in the source data.

---

## Step 2: Write the Executive Summary

**Timing:** Draft this paragraph AFTER completing all other sections (Steps 3-6), then place it at the top of the report, directly after the title and `---` separator.

Write 4-6 sentences of plain prose (NO tables, NO bullet points, NO headings). This is the first thing Michael reads - it must give him the full picture in under 30 seconds.

Cover ALL three of these in your sentences:
1. The 2-3 most important things happening today, with specific names, dates, and ticket keys
2. Current delivery state - what is on track, what is at risk, what is blocked
3. Any notable people dynamics, team wins, or concerns

Rules:
- No heading like "Executive Summary" - just start the prose directly after the `---`
- No "Single most important focus" box or call-out - end naturally
- Include specific timestamps, people names, and ticket references (like v2 example does)
- This summary must be dense with facts, not generic observations

---

## Step 3: Write Section 1 - My Action Items

**What belongs here:** Items where Michael must personally do something - reply, approve, deploy, provide info, attend, or decide.

**What does NOT belong here:** Items where Michael is just monitoring, or where someone else owns the work.

For each action item, write one table row in EXACTLY this format:

```
| Metadata | Details | Suggested Action |
|----------|---------|-----------------|
| **Priority:** 🔴/🟡/🟢<br>**Priority reason:** [1 sentence - why is this urgent or important?]<br>**Source:** [Jira / GChat / Gmail / Memory - be specific, e.g., "GChat (BCRS Firefighting Group)"]<br>**Date:** [When was this requested or when is it due?]<br>**From:** [Full name of the person who asked or created this] | **Context:** [3-5 sentences: (1) What is the situation? (2) What exactly is Michael asked to do? (3) What happens if Michael does not act? (4) Any deadline or dependency.]<br>**References:** [Exact ticket keys like DPD-715, or thread names, or resource_ids from the output files]<br>**Cross-source signals:** [List other sources where this topic appears, e.g., "GChat (3 threads), Jira (2 tickets)". If only one source, write "Single source."] | [1-2 sentences. Start with a verb. Name the person and the channel. E.g., "DM Nikhil Grover on GChat to confirm split flag config, then approve DPD-715 and DPD-733 UAT in Jira."] |
```

Sort rows by priority: all 🔴 first, then all 🟡, then all 🟢.

---

## Step 4: Write Section 2 - My Follow-Ups

**What belongs here:** Items where Michael has already asked for something and is waiting for someone else to respond or deliver. Michael has done his part; the ball is in someone else's court.

For each follow-up, write one table row in EXACTLY this format:

```
| Metadata | Details | Suggested Action |
|----------|---------|-----------------|
| **Priority:** 🔴/🟡/🟢<br>**Priority reason:** [1 sentence]<br>**Source:** [Jira / GChat / Gmail - be specific]<br>**Since:** [Date Michael last asked or sent the request]<br>**Days Waiting:** [Calculate: today's date minus the "Since" date]<br>**Waiting On:** [Full name + their role/team] | **Context:** [3-4 sentences: (1) What is pending? (2) Why does it matter? (3) What breaks if this stays unresolved?]<br>**References:** [Exact ticket keys or thread names]<br>**Cross-source signals:** [Other sources or "Single source."] | [Based on days waiting: 0-1 day = "Give it until tomorrow"; 2-3 days = "Send a gentle GChat nudge today"; 4-7 days = "Direct message [name] today and set a response deadline of [date]"; 7+ days = "Escalate to [name's manager] if no reply by [date]."] |
```

Sort rows by priority: all 🔴 first, then 🟡, then 🟢.

---

## Step 5: Write Section 3 - Work Stream Summaries

**What belongs here:** Everything that did NOT become an action item or follow-up, grouped by the work streams you identified in Step 1. Also include context for action items and follow-ups (e.g., the full BCRS situation, not just the specific action).

For each work stream, write this block:

```
### [Work Stream Name] - **[Status: On Track / At Risk / Blocked / Completed / Paused]**

- **What's happening:** [3-5 sentences: What is the current state? What progress happened recently? What decisions were made? What is pending?]
- **Key people:** [List named individuals and their role in this stream. E.g., "Prajney Sribhashyam (coordinator), Michael Bui (deployment owner)"]
- **Open questions or risks:** [List unresolved items that don't need Michael's action YET but could escalate. Number them: (1), (2), (3).]
- **Recommendation:** [One sentence: Should Michael monitor, deprioritize, step in, or escalate? Be specific.]
```

Order: Most active or highest-risk work streams first. Paused or stable ones last.

Skip any work stream with zero activity in the last reporting period.

---

## Step 6: Write Section 4 - Patterns and Observations

Write 3-5 bullet points. Each bullet must:
- Span at least 2 work streams or 2 sources (this is a cross-cutting observation, not a per-item note)
- Be specific - name the people, tickets, or patterns involved
- Sound like a trusted advisor's private notes, not a corporate status update

Good examples of patterns:
- A person or team that consistently delays responses across multiple threads
- A risk that is affecting multiple work streams simultaneously
- A team win worth acknowledging
- A process gap that keeps causing the same problem
- A coverage gap because someone is on leave

Bad examples (too vague, do NOT write these):
- "Communication could be improved"
- "Some tickets are delayed"
- "The team is busy"

---

## Step 7: Final Assembly

Put the sections together in this order:

```
# ❗ Daily Work Report - [Day of week], [Month DD, YYYY]

---

[Executive summary prose - 4-6 sentences, no heading, no bullet points]

---

## 🔴 My Action Items (Pending My Action)

[Section 1 table]

---

## 🟡 My Follow-Ups (Waiting on Others)

[Section 2 table]

---

## 📊 Work Streams

[Section 3 blocks]

---

## 💡 Patterns and Observations

[Section 4 bullets]

---

**Quick Stats:** [X] action items | [Y] follow-ups | [Z] work streams | [W] patterns/observations | Sources: [n_memory] memory items, [n_jira] Jira tickets, [n_gchat] chats, [n_gmail] emails
```

Rules:
- Use EXACTLY the section headers and emoji shown above
- Never use vague language like "investigate issue" or "look into this" - always name WHO does WHAT
- If a section has no items, write: "None identified in the reporting period."
- Quick Stats counts: action items = table rows in Section 1, follow-ups = table rows in Section 2, work streams = Section 3 blocks, patterns = Section 4 bullets. Source counts = total items read from each output file (the `Total` number from the `[N/Total]` heading)

---

## Output and Save

⚠️ **You MUST output the complete report in your response AND save it to a file. The response content and the file content must be identical.**

1. **Write the complete report in your response** - every section, every table row, every bullet point. Do NOT summarize or abbreviate.
2. **Save to file:** `workdir/❗ Daily Work Report {YYYY-MM-DD}.md` (overwrite if exists)
3. **Quality gate:** Before saving, compare your report against `workdir/❗ Daily Work Report.example-v2.md`. Your report must match v2's level of:
   - Cross-source synergization (same topic referenced across Jira + GChat + Gmail)
   - Specificity (exact names, timestamps, ticket keys, not vague references)
   - Depth (3-5 sentence contexts, not 1-2 sentence summaries)
   - Detail density (the more actionable details, the better)

## Truthfulness and Accuracy

- Every fact (date, name, ticket key, status, metric) must be traceable to a specific source item
- Never fabricate or infer details not present in the source data
- If uncertain about a detail, say "unconfirmed" rather than guessing
- Use exact quotes and references from source files when citing decisions or requests

## Error Handling

- If any source file was missing or empty, note it in the report header
- Never silently skip data - always report what succeeded and what failed
