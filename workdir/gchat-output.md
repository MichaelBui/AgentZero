

## [1/24] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 16 | Last Activity: 2026-04-05T06:30:16.402000+00:00 | Last Updated: 2026-04-05T06:35:16.569053+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (Updated April 5, ~06:31 UTC)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
Cyclical instability persists from April 1 through the early morning of April 5 (~06:31 UTC). The incident remains active with recurring failures affecting Identity (`engage-my-persona-api-go`), Gamification, Orchid frontend services, and Android app linkpoints. While specific latency spikes have recovered, high error rates and intermittent success rate dips continue to trigger alerts across multiple squads, indicating widespread degradation in the Engage tribe's services.

**Status Summary & Timeline (Updated: ~06:31 UTC)**
*   **Identity API Instability (`squad:dynamics`):**
    *   *Error Rate:* High error rates (>0.1%) triggered repeatedly between 05:59 and 06:30 UTC, with values ranging from 0.101 to 0.108. Most recent triggers occurred at **05:59** (0.108), **06:03** (0.100), **06:21** (0.106), and **06:29** (0.101). All triggered alerts recovered shortly after within the 06:00–06:30 window.
    *   *Latency:* P90 latency spikes (>1.8s) on `post_/new-myinfo/confirm` triggered at **06:07 UTC** (Value: 1.544s in recovered state, indicating a prior spike), recovering by **06:08 UTC**.
*   **Orchid Frontend (`squad:journey`):**
    *   *Success Rate:* Intermittent dips (<99.9%) triggered at **01:43 UTC** (Value: 99.806%) and again at **06:30 UTC** (Value: 99.894%).
*   **Android App (`squad:compass`):**
    *   *Linkpoints:* Success rate dips (<99.9%) triggered at **01:15 UTC** (Value: 99.029%), **06:13 UTC** (Value: 99.747%), and **06:27 UTC** (Value: 99.692%). All subsequent triggers recovered shortly after.
*   **Gamification/LT Gateway (`squad:dynamics`):**
    *   *Latency:* P99 latency spikes (>1.8s) on `get_/rms/me/campaigns` triggered at **06:19 UTC** (Value: 1.978s), recovering by **06:26 UTC**.

**Pending Actions & Ownership**
*   **Investigate Identity Service Fluctuations:** Continue analyzing recurring high error rates (~0.1%) on `engage-my-persona-api-go`. The pattern shows frequent triggers and recoveries (e.g., 05:59–06:30 UTC). Owner: **Squad Dynamics**.
*   **Monitor Gamification API Spike:** Investigate the severe error rate spike (0.345) recorded on April 3 at 14:12 UTC for root cause analysis. Owner: **Squad Dynamics**.
*   **Track Android & Orchid Stability:** Monitor cyclical success rate dips in `ef-android` and `frontend-gateway`. Owner: **Squad Compass** and **Squad Journey**.

**Decisions Made**
*   **Status Update:** Incident severity remains Critical. The continuity of failures from April 1 through the April 5 morning window (latest activity ~06:31 UTC) confirms systemic instability affecting multiple squads simultaneously.
*   **Pattern Confirmation:** Recurrence involves Identity error rates hovering just above 0.1%, Orchid success dips, and Android linkpoint failures, indicating widespread degradation in the Engage tribe's services.

**Key Dates & Follow-ups**
*   **Active Window:** April 1, 09:58 – April 5, 06:31 UTC (Latest Activity).
*   **Reference Links (Latest):**
    *   `engage-my-persona-api-go` Error Rate Monitor #92965074 (Most Recent Trigger: 06:29 UTC, Value: 0.101)
    *   `frontend-gateway` (Orchid) Success Rate Monitor #17448311 (Latest Trigger: 06:30 UTC, Value: 99.894%)
    *   `ef-android` RUM Monitor #63109467 (Latest Trigger: 06:27 UTC, Value: 99.692%)
    *   `lt-gateway-app` P99 Latency Monitor #17447532 (Triggered: 06:19 UTC, Value: 1.978s)


## [3/24] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Messages: 8 | Last Activity: 2026-04-05T03:37:22.592000+00:00 | Last Updated: 2026-04-05T06:57:57.106775+00:00
# Daily Work Briefing: #dd-fpg-watchdog-alert

### Key Participants & Roles
*   **Datadog App:** Automated monitoring system.
*   **@hangouts-dd-dpd-watchdog-alert:** Targeted notification channel.
*   *Note: Interactions remain purely automated.*
*   **Monitor Tags:** `managed_by:datadog-sync`

### Main Topic
The channel tracks **P3 [DPD Watchdog] infrastructure incidents** in Production. Logs show recurring transient issues (excluding `tcp_retrans_jump` and `full_disk_forecast`) aggregated by `story_key`. The consistent alert message reads: "Datadog is unable to process your request."

### Incident Summary & Status Update
**Historical Resolved Incidents:**
*   **Mar 05–31, 2026:** Multiple incidents (e.g., Keys `10aaf170...`, `2787bcd7...`, `de0cbb14...`) resolved within typical transient windows. All Status: **Resolved**.
*   **Apr 1–2, 2026:** Incidents (`c6d476e4...`, `fa62ae68...`) triggered and recovered. All Status: **[P3] Recovered**.

**Active Incident Timeline (Updated):**
*   **Incident #1:** `story_key: 21a5a729-dfbb-5206-a97e-047fe5903e51`
    *   Triggered: Apr 3, 2026 at 14:28:22 UTC.
    *   **Recovered:** Apr 3, 2026 at 17:53:23 UTC (~3h 25m). Status: **[P3] Recovered**.
*   **Incident #2 (Resolved):** `story_key: 211807e9-ab64-599b-959a-7ce890e78c22`
    *   Triggered: Apr 4, 2026 at 17:04:22 UTC.
    *   **Recovered:** Apr 5, 2026 at 03:37:22 UTC (~10h 33m). Status: **[P3] Recovered**.
*   **Incident #3 (Resolved):** `story_key: f1f4de4a-77e2-55e6-9946-e28bfbb18621`
    *   Triggered: Apr 4, 2026 at 18:00:22 UTC.
    *   **Recovered:** Apr 5, 2026 at 03:37:22 UTC (~9h 37m). Status: **[P3] Recovered**.

### Pending Actions & Ownership
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Action Required:** No manual intervention required. Both incidents triggered on Apr 4 resolved simultaneously on Apr 5 at 03:37:22 UTC. Duration exceeded the typical ~3–4 hour window (~10 hours), but resolution is confirmed. Continue standard surveillance for new triggers.

### Decisions Made
*   **Escalation Status:** Closed/Resolved. The previous protocol to monitor for a 6-hour threshold was superseded by actual recovery at the ~10-hour mark. No escalation was triggered as incidents resolved autonomously.
*   **Protocol:** Maintain monitoring of `story_key` groups. If future incidents exceed 12 hours without resolution, review for potential process anomalies.

### Key Dates & Follow-ups
*   **Latest Event:** Recovery notification received Apr 5, 2026 at 03:37:22 UTC for both active incident keys.
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Monitor `@hangouts-dd-dpd-watchdog-alert` for subsequent alerts.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Monitor Query:** `events("source:watchdog (story_category:infrastructure -story_type:(tcp_retrans_jump OR full_disk_forecast)) env:(PROD OR production OR prod)").rollup("count").by("story_key").last("30m") > 0`
*   **Recovery Links (Apr 5):**
    *   Key `211807e9...`: [View](https://app.datadoghq.eu/monitors/17447511?group=story_key%3A211807e9-ab64-599b-959a-7ce890e78c22&from_ts=1775359251000&to_ts=1775360451000&event_id=8574791062233039453)
    *   Key `f1f4de4a...`: [View](https://app.datadoghq.eu/monitors/17447511?group=story_key%3Af1f4de4a-77e2-55e6-9946-e28bfbb18621&from_ts=1775359251000&to_ts=1775360451000&event_id=8574791062203702124)


## [4/24] RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Messages: 27 | Last Activity: 2026-04-05T03:20:42.015000+00:00 | Last Updated: 2026-04-05T06:59:03.617895+00:00
**Daily Work Briefing: Automated Test Results Summary (RMN Notification)**

**Key Participants & Roles**
*   **Collection Runner App:** Automated testing agent executing API suites.
*   **Webhook Bot:** Reporting mechanism; consistently returning "unable to process your request" on all notifications from March 12 through April 5, 2026.
*   **Parties Involved:** System-generated notification log only.

**Main Topic/Discussion**
Automated nightly API test executions across `promo-service`, `marketing-personalization-service`, and `marketing-service` in the **staging** environment. Monitoring period spans March 12 through **April 5, 2026**. Execution windows occur at approximately 01:05 UTC (morning), 02:31 UTC (midnight), and **03:21 UTC** (early morning).

**Test Execution Status & Anomalies**
*   **`marketing-service`:** Regression confirmed.
    *   **April 5, 01:05 UTC:** Contract tests passed (20 Passed / 0 Failed); API Tests failed with **3 failures** (44 Passed). This confirms a persistent instability issue extending the problematic window previously seen March 17–25 and April 2–3. The service has now failed on consecutive mornings at 01:05 UTC (April 3, 4, and 5).
*   **`promo-service`:** Confirmed stable on **April 5 at 02:31:20 UTC**.
    *   **[API Contract Tests]:** 6 Passed / 0 Failed / 0 Skipped (Total Requests: 3).
    *   **[API Tests]:** 10 Passed / 0 Failed / 0 Skipped.
*   **`marketing-personalization-service`:** Confirmed stable on **April 5 at 03:20:42 UTC**.
    *   **[API Contract Tests]:** 125 Passed / 0 Failed / 0 Skipped (Total Requests: 21).
    *   **[API Tests]:** 96 Passed / 0 Failed / 0 Skipped.

**Pending Actions & Ownership**
*   **Webhook Bot Remediation (High Priority):** The bot failed to process requests in every notification cycle from March 12 through the latest log on **April 5**. Immediate attention is required from DevOps or Automation Infrastructure to resolve the persistent "unable to process" error.
*   **Investigate `marketing-service` Regression:** Engineering must analyze the root cause of the recurring API test failures (3 failures) observed on April 4 and **April 5** at 01:05 UTC. The issue persists without resolution, indicating a critical systemic or code regression.

**Decisions Made**
*   No human decisions recorded; all entries are automated system outputs.

**Key Dates & Deadlines**
*   **Failure Window (Historical):** Instability noted March 12–13 and persistently from **March 17 through March 25**. Recent recurrence began April 2, continuing through **April 5**.
*   **Current Status:** Continuous failure in `marketing-service` API tests on April 4 and 5. Other services remain stable.
    *   `marketing-service`: Failed API tests at 01:05 UTC on both April 4 and April 5.
    *   `promo-service`: Passed at 02:31 UTC on April 5 (previously noted as April 4).
    *   `marketing-personalization-service`: Fully successful run recorded at 03:20 UTC on April 5 (previously noted as April 4).
*   **Monitoring Period:** Data covers runs from **March 12, 2026**, through **April 5, 2026**.

**Resource Info**
*   **Message Count:** Updated to reflect notifications through April 5 (Total: 237).
*   **URL:** https://chat.google.com/space/AAQA85dw4So


## [5/24] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Last Activity: 2026-04-05T01:03:10.245000+00:00 | Last Updated: 2026-04-05T01:58:13.599183+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Apr 5, 01:03 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`.
*   **Escalations:** `@oncall-dpd-staff-excellence-pdm`, `@hangouts-GT-Search-DatadogAlerts`, `@hangouts-GT-Discovery-DatadogAlerts`, `@opsgenie-dpd-grocery-discovery`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Retail Media.

**Main Topic**
**P2 INCIDENT (RESOLVED):** Recurring transient high error rate in `marketing-service`.
**Ongoing P3 ANOMALY:** Intermittent "Low Processed Files" alerts for `sku-store-attribute` job on Apr 4–5.
*   **Current Status:** All recent `marketing-service` alerts are stable/recovered. The `sku-store-attribute` job shows recurring transient failures requiring continued monitoring; no open P2 incidents remain.

**Resolved Incidents (Apr 3)**
*   **Alert:** **P2 High Error Rate (`marketing-service`)** [Status: RECOVERED]
    *   *Timeline & Metrics:*
        *   **16:26 UTC:** Triggered (0.014) → Recovered 16:50 UTC.
        *   **17:35–17:51 UTC:** Fluctuating triggers (Peak: 0.073 at 17:41 UTC; Low: 0.039) → Recovered 17:51 UTC.
    *   *Detail:* Error rate threshold (>5%) breached multiple times within a short window. All instances resolved automatically with metrics dropping to 0.0%.

**Resolved Incidents (Apr 4–5)**
*   **Alert:** **P3 Low Processed Files (`sku-store-attribute`)** [Status: RECOVERED]
    *   *Incident 1:* Triggered Apr 4, 22:10 UTC; Recovered Apr 5, 00:21 UTC.
    *   *Incident 2:* Triggered Apr 5, 00:37 UTC; Recovered Apr 5, 01:03 UTC.
    *   *Detail:* Job processed <6 files in the last 4 hours (Log query threshold). Both instances self-corrected within ~2 hours.

**Resolved Incidents (Apr 2)**
*   Historical anomalies for `fpon-catalogue-job-sku-global-attribute`, `go-catalogue-service` (latency), `marketing-service` (throughput), and the first `sku-store-attribute` event remain resolved.

**Decisions Made**
*   **`marketing-service`:** The error rate on Apr 3 exhibits a clear pattern of transient spikes (peaks at 17:41 UTC reaching 7.3%). No manual intervention was required; monitoring confirms stabilization after each spike.
*   **`sku-store-attribute`:** Recurring low-file-count events on Apr 4 and 5 suggest intermittent job slowness or batch delays rather than permanent failure, as recovery is automatic.
*   **Action:** Continue standard monitoring. No immediate runbook execution or escalation to PDM team required unless recurrence patterns intensify or fail to self-correct within 2 hours.

**Key Dates & Follow-ups (Apr 2–5, 2026)**
*   **P2 (Resolved):** `marketing-service` high error rate (Multiple triggers: Apr 3, 16:26–17:51 UTC).
*   **P3 (Resolved/Recurring):** `sku-store-attribute` low files (Triggers: Apr 4 22:10, Apr 5 00:37; all recovered).
*   **Observation:** Both services demonstrate self-healing behaviors without manual intervention.

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c
*   **Monitor (`marketing-service` High Error Rate):** https://app.datadoghq.eu/monitors/17447106
*   **Monitor (`sku-store-attribute` Low Files):** https://app.datadoghq.eu/monitors/20382848
*   **APM Resource:** https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod
*   **K8s Deployment:** https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview
*   **Runbook:** https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book


## [6/24] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Last Activity: 2026-04-05T00:03:08.414000+00:00 | Last Updated: 2026-04-05T01:58:40.864051+00:00
**Daily Work Briefing Summary (Updated: April 5, 2026)**

**Main Topics & Discussions**
1.  **Programmatic Advertising:** Focus remains on validating discrepancies for `advertima_ttd-fixed-price-test-1.5`. Ravi Singh confirmed receipt of raw BURLs; validation was targeted for Monday, March 17th. Yian Koh requested confirmation on deals `advertima_ttd-first-price-test` and `advertima_ttd-fixed-price-test-1`.
2.  **New Deal Setup:** Yasmina Tregan (Advertima) requires an end-to-end test setup this week. Wei Phung to share live campaign details; Ravi Singh to execute setup, push to TradeDesk, and map segments before launch.
3.  **BCRS UAT & Finance Integration:** Progress continues on SAP document numbers, duplicate posting fixes via PubSub "exactly once" policy (PR #1033), and Bukit Timah Plaza pricing/display issues.
4.  **Event Sync Optimization (DPD-645):** Addressing the massive event overage (14M vs. normal 550k). PRD deployment plan set for Sunday, March 15.
5.  **Security & Compliance:** RMN Pentest fixes (DPD-700) deployed to Prod; Bitbucket App Passwords deprecated effective June 9, 2026.

**Status Update: Inbox & Communications**
*   **Inbox Status:** As of April 5, 2026 (00:03 UTC), the workspace inbox is fully caught up across all categories (**Urgent Action Items**, **Meeting Updates**, and **FYI**). No pending unread items require immediate attention. This status follows confirmations from daily summaries dated March 24 through April 5. The latest updates from Workspace Studio (April 3, April 4, and April 5) confirm zero backlog in all sections, including Code Reviews and Project Updates.

**Pending Actions & Owners**
*   **BCRS UAT SAP Docs:** Update Column J in Google Sheet for Finance finalization. *Owner: Michael Bui / Hendry Tionardi*.
*   **Bitbucket Security:** Generate scoped API tokens to replace deprecated App Passwords by June 9, 2026. *Owner: All Devs*.
*   **Event Overload Investigation:** Investigate the 14M event spike in the audience pipeline. *Owner: Michael Bui*.
*   **TTD Discrepancy Confirmation:** Ravi Singh to confirm discrepancies on raw BURLs; Yian Koh to validate other deals. *Owner: Ravi Singh / Yian Koh*.
*   **New Deal Setup:** Wei Phung to share details; Ravi Singh to execute. *Owner: Ravi Singh / Wei Phung*.

**Decisions Made**
*   **SLO Monitoring:** Merged PRs #882, #884, and #891 for night-time mute schedules and on-call configurations.
*   **Ad Strategy:** FPG to use "Native" creative formats for TTD carousel; OSMOS SDK restricted to tracking only. End-to-end test required before live launch.
*   **Release Schedule:** FairPrice Website v10.57.0 release canceled; RMN Pentest fixes (DPD-700) confirmed fixed in Prod.

**Key Dates & Deadlines**
*   **March 3, 2026:** Retail Media TV catch-up meeting.
*   **March 5, 2026:** Raya Scan visuals live; v10.57.0 release canceled.
*   **March 9, 2026:** D&T Q1 All Hands RSVP deadline.
*   **March 11, 2026 (12 AM):** RDCS database upgrade maintenance.
*   **March 15, 2026 (8–11 PM):** Tentative PRD rollout for DPD-645 event sync fix.
*   **March 17, 2026:** Deadline for TTD discrepancy confirmation.
*   **March 31, 2026:** FY2025 Performance Closeout deadline (MyHR).
*   **April 1, 2026:** Daily inbox review completed; no new urgent items identified.
*   **April 2, 2026:** Daily inbox review completed; no new urgent items identified across any category.
*   **April 3, 2026:** Daily inbox review completed via Workspace Studio; all categories confirmed clear of backlog.
*   **April 4, 2026:** Daily inbox review completed; Urgent Action Items and High-Volume Themes confirmed clear.
*   **April 5, 2026:** Daily inbox review completed; no new urgent items identified across any category.
*   **June 9, 2026:** Bitbucket App Password deprecation deadline.

**Note on New Content:** Updates from Workspace Studio dated April 4 and April 5 (00:03 UTC) confirm the inbox remains clear of urgent action items across all categories (**Urgent Action Items**, **High-Volume Themes**, **Meeting Updates**, **FYI**). No changes to pending actions or decisions were required based on these updates; historical context regarding project statuses and deadlines remains valid.


## [7/24] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Last Activity: 2026-04-04T23:01:23.161000+00:00 | Last Updated: 2026-04-05T01:59:04.472140+00:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
On April 3, a new P1 incident involving SAP authentication failures impacted the `fpon-seller-sap-picklist-reporter` service. Concurrently, critical latency in `picklist-pregenerator` persists across multiple days (April 3 and April 4). The recurring connectivity clusters affecting `fni-order-create` remain unresolved since the April 3 morning window.

**Incident Summary & Timeline**
*   **Service: `fpon-seller-sap-picklist-reporter` (P1 Authentication Failure) – April 3 Evening**
    *   **Trigger:** SAP authentication failed at **19:12:15 UTC**. Monitor query: `env:prod service:fpon-seller-sap-picklist-reporter "SAP API authentication failed"`.
    *   **Recovery:** Alert resolved at **19:17:15 UTC** (Duration: ~5 minutes).
    *   **Monitor ID:** 58101314.

*   **Service: `picklist-pregenerator` (Latency Warning) – Ongoing**
    *   **Status:** Critical latency persists with execution times consistently exceeding 3,610s.
    *   **Triggers:**
        *   April 3 at 23:01:22 UTC (Metric: 3612.223s).
        *   April 4 at 23:01:23 UTC (Metric: 3611.565s).
    *   **Monitor ID:** 20383097.

*   **Service: `fni-order-create` (Historical Cluster) – April 3 Morning**
    *   **Context:** A cluster of errors occurred between **05:42:40 UTC** and **05:47:49 UTC**. Monitors 17447918 ("Exception Occurred At Mirakl Route") and 17447928 ("Error while calling APIs") triggered.
    *   **Status:** Pattern mirrors instability on April 1 and April 2; recurrence indicates a systemic integration failure with Mirakl/DBP.

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of the SAP authentication failures in `fpon-seller-sap-picklist-reporter`. While resolved, the P1 severity warrants review to prevent recurrence.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Address critical latency in `picklist-pregenerator`. Execution times remain above 3,610s on April 3 and April 4 (Monitor ID 20383097). Immediate architectural review is required to prevent further degradation.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Investigate the root cause of the three-day cluster affecting `fni-order-create` (Apr 1–3). Focus on Mirakl route exceptions and API errors.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Summary for Leadership**
On April 3, the system experienced two distinct critical events: a transient P1 SAP authentication failure in `fpon-seller-sap-picklist-reporter` (resolved in ~5 minutes) and a persistent latency crisis in `picklist-pregenerator`. The latter shows no recovery, with execution times exceeding 3,610s on both April 3 and April 4. Additionally, connectivity issues affecting `fni-order-create` have persisted for three consecutive days (April 1–3), driven by Mirakl/DBP integration failures. Urgent engineering review is required to address the recurring order processing failures and resolve the critical latency in seller experience workflows which has now spanned multiple 24-hour cycles.


## [8/24] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw/vpSecvgp02o | Last Activity: 2026-04-04T11:23:12.639000+00:00 | Last Updated: 2026-04-05T01:59:59.866708+00:00
**Daily Work Briefing: Digital Product Development (DPD)**

**Key Participants & Roles**
*   **Winson Lim:** Shared a new design resource.
*   **Amit Giri:** Provided commentary on the proposed methodology.
*   **Michael Bui:** Expressed interest and acknowledged sharing; previously seeking this resource.

**Main Topic/Discussion**
The team discussed a new approach to system design centered around Markdown (MD). Winson Lim introduced a GitHub repository (`https://github.com/VoltAgent/awesome-design-md`) as a "new way to design system." Amit Giri characterized the shift as "MD-fying everything," suggesting a broader organizational move toward Markdown-based documentation and workflows. Michael Bui confirmed this resource was previously sought after by him.

**Pending Actions & Ownership**
*   **Action:** Review and adopt the new Markdown-based design system methodology.
    *   **Owner:** Unassigned (Shared by Winson Lim; requested by Michael Bui).
    *   **Context:** No specific task ticket or deadline was assigned in the chat.

**Decisions Made**
*   No formal decisions were recorded. The conversation indicates a consensus on the utility of the resource, but no binding mandate to replace existing systems was established during this exchange.

**Key Dates & Follow-ups**
*   **2026-04-04 07:46 UTC:** Winson Lim posted the link to `awesome-design-md`.
*   **2026-04-04 09:48 UTC:** Amit Giri confirmed the "MD-fying" trend.
*   **2026-04-04 11:23 UTC:** Michael Bui thanked Winson and shared his prior search for this specific tool.

**Resource Reference**
*   **Link:** https://github.com/VoltAgent/awesome-design-md
*   **Space URL:** https://chat.google.com/space/AAAAx50IkHw


## [9/24] Nikhil, Nicole Soh, Yap Chye Soon, Anwar, Owen, ...
Source: gchat | Group: space/AAAAJ8ygRqY | Last Activity: 2026-04-04T09:44:57.766000+00:00 | Last Updated: 2026-04-05T02:00:11.617019+00:00
**Daily Work Briefing: Google Chat Summary**

**1. Key Participants & Roles**
*   **Yap Chye Soon Adrian**: Primary contributor in the logged segment; identified as a viewer of shared content (7 of 13 participants viewed).
*   **Gopalakrishna Dhulipati**: Tagged by Yap Chye Soon Adrian, indicating direct relevance to the message or required attention.
*   **Other Resources Mentioned (Context Only)**: Nikhil, Nicole Soh, Anwar, Owen (No specific actions recorded for these individuals in the provided log).

**2. Main Topic/Discussion**
The conversation segment is minimal and does not contain an active discussion thread. The sole recorded action involves Yap Chye Soon Adrian viewing a shared item (likely a document or link) within the space and simultaneously tagging Gopalakrishna Dhulipati. The specific subject matter of the viewed item is not detailed in the provided text, only that it was accessed by 7 out of 13 total members.

**3. Pending Actions & Ownership**
*   **Action**: Acknowledge or respond to the tag/view notification from Yap Chye Soon Adrian regarding the shared content.
*   **Owner**: Gopalakrishna Dhulipati (indicated by the `@` mention).

**4. Decisions Made**
No formal decisions were recorded in this specific 2-message log segment. The interaction reflects a status update or notification of content consumption rather than a resolution or strategic choice.

**5. Key Dates, Deadlines, & Follow-ups**
*   **Date/Time**: April 4, 2026, at 09:44:57 (UTC).
*   **Follow-up Required**: Immediate attention to the tag from Yap Chye Soon Adrian is implied by the direct mention.
*   **Space URL**: https://chat.google.com/space/AAAAJ8ygRqY

**Summary Note**
The provided log represents a high-level notification event rather than a substantive debate. The critical takeaway for Gopalakrishna Dhulipati is to review the content viewed by Yap Chye Soon Adrian and determine if further engagement or action is required from his end. No other participants in the resource list (Nikhil, Nicole Soh, Anwar, Owen) are referenced in this specific timestamped exchange.


## [10/24] 📢 COM Notifications
Source: gchat | Group: space/AAAAu4WIubc | Last Activity: 2026-04-04T09:22:30.861000+00:00 | Last Updated: 2026-04-05T02:01:14.328151+00:00
**Daily Work Briefing: SonarCloud Quality Monitoring**

**Key Participants & Roles**
*   **gautam-ntuc**: Developer; responsible for `catalogue-service` (PR-535) and `catalogue-job` commits.
*   **Shiva Kumar Yalagunda Bas**: Developer; previously authored `supplier-job` changes.
*   **bitbucket-pipelines**: Automated CI/CD bot triggering merges and deployments.
*   **System/Webhook Bot**: Continues reporting recurring "Webhook Bot is unable to process your request" errors across all notifications, including new scans on April 4.

**Main Topic**
Automated SonarCloud quality gate scans for `catalogue-service`, `seller-picklist-reporter`, and other services. The conversation tracks code coverage anomalies (specifically 0% coverage despite PASSED gates), pipeline volatility, and persistent system notification errors.

**Status Summary by App**
*   **`fni-product-license-alert`**:
    *   **April 2**: PR-1433 passed scans with 94.4% coverage; PR-1483 passed with **0%** new code coverage (anomaly).
*   **`catalogue-service`**:
    *   **April 2**: PR-535 opened by gautam-ntuc; Status **OPEN**, 95.9% new code coverage.
*   **`seller-picklist-reporter`**:
    *   **April 4 (09:22 UTC)**: PR-2335 scanned (ver. `76047ac`) with **Medium Tolerance**. Quality Gate Status: **PASSED**. However, recorded **0%** Coverage on New Code. This mirrors anomalies seen in April 1 (`PR-1479`), April 2 (`PR-1483`), and persists despite the bot error message.
*   **`supplier-job`**: No new activity reported; previous scans on March 19 remain last recorded success.

**Pending Actions & Ownership**
*   **System Error Investigation**: The "Webhook Bot is unable to process your request" error persists in every notification from March 5 through April 4 (including `catalogue-service` PR-535, `fni-product-license-alert` PR-1483, and `seller-picklist-reporter` PR-2335). No specific owner assigned; requires immediate engineering attention.
*   **0% Coverage Anomaly Pattern**: A third instance of a **PASSED** Quality Gate with **0%** new code coverage occurred in `seller-picklist-reporter` PR-2335 on April 4. Following previous incidents (PR-1479, PR-1483), this suggests a systemic issue with tolerance settings or data reporting integrity rather than isolated failures.
*   **`catalogue-service` Monitoring**: PR-535 is currently OPEN; teams should monitor for potential failure/recovery cycles similar to previous `seller-proxy-service` incidents.

**Decisions Made**
*   **April 2 Action**: `fni-product-license-alert` PR-1433 scans consistently recovered and passed immediately despite volatility in previous days' logs. The system accepted the merge logic automatically.
*   Recent merges in `supplier-job` and recovery scans for `seller-proxy-service` remain valid historical context, though current focus has shifted to identifying patterns across `catalogue-service`, `fni-product-license-alert`, and `seller-picklist-reporter`.

**Key Dates & Timeline**
*   **April 1**: 
    *   **03:51 UTC**: `fni-product-license-alert` PR-1479 PASSED with 0% coverage.
    *   **03:52–04:22 UTC**: `seller-proxy-service` PR-2334 failed/recovered cycle.
*   **April 2**: 
    *   **03:14 – 06:27 UTC**: Multiple PASSED scans for `fni-product-license-alert` PR-1433 at 94.4% coverage.
    *   **05:21 – 05:25 UTC**: `catalogue-service` PR-535 opened by gautam-ntuc (OPEN, 95.9% coverage).
    *   **06:29 UTC**: `fni-product-license-alert` PR-1483 PASSED with **0%** new code coverage.
*   **April 4**: 
    *   **09:22 UTC**: `seller-picklist-reporter` PR-2335 PASSED (ver. `76047ac`) with **0%** new code coverage; associated webhook error persists.


## [11/24] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw | Last Activity: 2026-04-04T07:46:28.110000+00:00 | Last Updated: 2026-04-05T02:02:22.987531+00:00
**Daily Work Briefing: Digital Product Development (DPD)**

**Key Participants & Roles**
*   **Flora Wo Ke:** Team Lead.
*   **Winson Lim:** Engineering Lead/Strategy.
*   **Alvin Choo:** Developer/QA.
*   **Nicholas Tan:** DevOps/Infrastructure.
*   **Tiong Siong Tee / Andin Eswarlal Rajesh:** QA/Engineering (iOS).
*   **Natalya Kosenko:** DevOps/SRE.
*   **Boning He / Gopalakrishna Dhulipati:** Team Members.
*   **Kyle Nguyen:** Team Member.
*   **Maou Sheng Lee:** Team Member.
*   **Jazz Tong:** Incident Coordinator.
*   **Akash Gupta:** Support Lead.
*   **Vivian Lim Yu Qian:** Staff Verification Specialist.
*   **Mohammad Adyatma:** Team Member (Security).
*   **Wai Ching Chan:** Team Member.

**Main Topics & Discussions**
1.  **System Design Learning:** On April 4, 2026 (07:46 UTC), Winson Lim shared a new resource for system design patterns (`https://github.com/VoltAgent/awesome-design-md`). The thread has generated 2 replies as of yesterday at 11:23 AM.
2.  **FPPay Production Issue:** On March 30, 2026 (09:11 UTC), Andin Eswarlal Rajesh reported FPPay banner images failing to load in production. Activity continues with 25+ replies.
3.  **Staff Verification Logic:** Vivian Lim Yu Qian queried app screens for staff verification during SKU purchases requiring force verification (e.g., milk powder). The team is validating compliance against existing protocols.
4.  **Incident Management Response:** Earlier on March 27, Jazz Tong raised an urgent query regarding a potential incident ("it is incident?"). The team mobilized support for the DPD Incidents channel involving Gopalakrishna Dhulipati, Akash Gupta, and Kyle Nguyen.
5.  **Infrastructure & Operations Risk:** Nicholas Tan flagged risks regarding Broadcom ending free Bitnami images, causing `kubectl` image tag failures and increased Time To Recovery (TTR) impacting the Golden Pipeline (GP).
6.  **Payment Service Issues:** Alvin Choo reported promo code redemption failures in FP Pay; confirmed that a change freeze has ended and feature releases are proceeding.
7.  **Mobile Quality Assurance:** Andin Eswarlal Rajesh previously identified an iOS FPPay bug where QR codes load without user login, escalated via file download.
8.  **Datadog Governance:** Natalya Kosenko reported unauthorized manual changes to Datadog On-Call teams (removals of Maxine, Arijit, Minu). Terraform manages this config; manual console edits are overwritten on the next run.
9.  **Strategic Planning & Tooling:** Winson Lim highlighted data centers as potential targets in modern warfare (Iran conflict context) to inform Disaster Recovery (DR) scenarios and noted Reforge joined Miro to bridge strategy and delivery gaps.
10. **AI Engineering Learning:** On March 30, 2026 (23:25 UTC), Winson Lim shared a GitHub repository (`affaan-m/everything-claude-code`) as a resource for learning AI-first engineering patterns.
11. **Security Alert (NPM):** On March 31, 2026 (04:38 UTC), Mohammad Adyatma flagged the compromise of the `axios` npm package via `https://socket.dev/blog/axios-npm-package-compromised`. Immediate review of dependencies is required.
12. **Bonus Communication:** On April 1, 2026 (13:51 UTC), Wai Ching Chan initiated a discussion regarding "FPG Bonus" with 2 replies. A YouTube link was shared in the thread.
13. **Social Events:** Kyle Nguyen announced an upcoming DPD BBQ ("We come first"). Boning He and Gopalakrishna Dhulipati shared snacks; Maou Sheng Lee expressed sentiment regarding energy waste on March 18.
14. **Employee Code of Conduct Update:** On April 2, 2026 (10:02 UTC), Alvin Choo circulated a critical update to the Employee Code of Conduct via NTUC Enterprise Mail, urging all staff to review for doubts.

**Pending Actions & Owners**
*   **FPPay Image Team (Andin Eswarlal Rajesh, DevOps):** Investigate root cause of banner image loading failures in production and deploy fix. Priority: High.
*   **System Design Review (Winson Lim / All Engineers):** Explore the `VoltAgent/awesome-design-md` repository shared on April 4 for potential application of new system design methodologies.
*   **S&G Verification Team (Vivian Lim Yu Qian, Product/Dev Teams):** Investigate current S&G flows against the WIP verification logic document to confirm if forced staff verification screens exist for restricted SKUs like milk powder.
*   **Incident Response Team (Jazz Tong, Akash Gupta, Gopalakrishna Dhulipati, Kyle Nguyen):** Act as support guides for the active DPD Incidents channel; monitor and resolve incoming incident queries.
*   **GP Team (Nicholas Tan / Mohit Niranwal):** Investigate Bitnami image replacement strategy to resolve TTR issues and update Golden Pipeline dependencies.
*   **iOS/Dev Team (Tiong Siong Tee):** Re-verify the previously identified iOS FPPay QR code login bypass bug status.
*   **Security Team (Mohammad Adyatma, All Devs):** Audit all projects for `axios` dependency versions to mitigate risks associated with the reported npm package compromise.
*   **FPG Bonus Discussion (Wai Ching Chan):** Review details regarding FPG bonus distribution and linked content.
*   **All Staff:** Review the "Important Updates to the Employee Code of Conduct" PDF shared by Alvin Choo on April 2; raise any doubts immediately.

**Decisions Made**
*   No formal change freeze; feature releases are currently active (Alvin Choo).
*   Datadog team configurations must strictly follow Infrastructure as Code (Terraform) protocols; manual overrides are deprecated.
*   Miro's acquisition of Reforge is recognized as a strategic move to bridge product strategy and delivery gaps.
*   Active incident support protocol established for Jazz Tong, Akash Gupta, Gopalakrishna Dhulipati, and Kyle Nguyen on March 27, 2026.
*   Winson Lim endorsed the `affaan-m/everything-claude-code` repository as a key resource for AI-first engineering patterns (March 30). **Updated:** Winson Lim also identified `VoltAgent/awesome-design-md` as a primary reference for system design architecture (April 4).
*   Mandatory review of updated Employee Code of Conduct (April 2, 2026) initiated by Alvin Choo; staff must clarify doubts with management.

**Key Dates & Follow-ups**
*   **Apr 4, 2026 (07:46 UTC):** Winson Lim shared system design resource (`VoltAgent/awesome-design-md`); discussion active since yesterday at 11:23 AM.
*   **Apr 2, 2026 (10:02 UTC):** Alvin Choo distributed critical Employee Code of Conduct updates.
*   **Apr 1, 2026 (13:51 UTC):** Wai Ching Chan initiated FPG Bonus discussion; video shared.
*   **Mar 31, 2026 (04:38 UTC):** Mohammad Adyatma flagged `axios` npm package compromise; security audit initiated.
*   **Mar 30, 2026 (23:25 UTC):** Winson Lim shared AI engineering resource repo.
*   **Mar 30, 2026 (09:11 UTC):** Andin Eswarlal Rajesh flagged FPPay banner image loading failure in prod; discussion ongoing (25+ replies).
*   **Mar 27, 2026 (03:03 UTC):** Jazz Tong flagged potential DPD incident; support team mobilized.
*   **Mar 27, 2026 (08:11 AM):** Vivian Lim Yu Qian raised S&G verification flow query; discussion concluded with 12 replies.

**Social Notes**
*   Upcoming DPD BBQ announced by Kyle Nguyen ("We come first, see you!").


## [12/24] [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Last Activity: 2026-04-04T07:18:01.061000+00:00 | Last Updated: 2026-04-05T02:03:16.241440+00:00
**Daily Work Briefing: [Prod Support] Marketplace**

**Key Participants & Roles**
*   **Support/Operations:** Willie Tan, Iris Chang, Lalita Phichagonakasit, Charlene Tan, Jie Yi Tan, Ayton See, Amos Lam, Michelle Lim.
*   **Technical/Admin Team:** Dang Hung Cuong, Shiva Kumar Yalagunda Bas, Olivia -, Jill Ong, Greta Lee, Zaw Myo Htet, Angella Yeo, Cassandra Thoi, Gopalakrishna Dhulipati, Ee Ling Tan, Sneha Parab.
*   **New Reporter:** Muhammad Sufi Hakim Bin Safarudin.

**Main Topics & Discussion Summary**
Discussions continue to focus on operational blockers regarding seller onboarding, order fulfillment discrepancies, system configuration errors, and data visibility gaps. New reports from April 1 highlight critical platform performance issues (lag), DBP barcode conflicts, and delivery window synchronization failures. On April 2, queries arose regarding picker app historical data, specific seller app issues, and image identification problems. **On April 4, a new fulfillment error was reported by Aw's Market involving incorrect temperature labeling on FFS packlists.**

1.  **FFS Packlist Temperature Error (New):** On April 4 at 07:18 UTC, Jing Ying Foo reported that Aw's Market received an FFS packlist with ambient QR codes instead of chilled ones. The vendor typically handles either chilled or frozen SKUs and requested clarification/assistance.
2.  **Transporter App Performance:** Anwar Nur Amalina reported (Apr 1) severe lag and job loading failures in the Transporter Inform app.
3.  **DBP Barcode Duplicate/NotFound Error:** Charlene Tan flagged (Apr 1) a barcode unable to be found in DBP despite appearing as a duplicate entry. Dang Hung Cuong was tagged for investigation.
4.  **Delivery Window Synchronization:** Jie Yi Tan reported (Apr 1) that the delivery window configuration failed for seller "Funa Artistic Hampers & Gifts" (displaying 3 days instead of configured 5). Dang Hung Cuong was tagged.
5.  **Seller Account Sync Failure:** Michelle Lim reported (Mar 31) that two new seller accounts failed to sync to DBP despite allocated internal codes and no error messages (Codes: 32208, 32207).
6.  **Image Identification Query:** On Apr 2, Charlene Tan queried the team regarding how to identify specific image problems.

**Pending Actions & Ownership**
*   **FFS Packlist Correction:** Investigation into why Aw's Market FFS packlist displayed ambient QR instead of chilled status; immediate clarification requested (Jing Ying Foo, Apr 4).
*   **Transporter App Investigation:** Technical team to investigate lag and job loading failures (Anwar Nur Amalina, Apr 1).
*   **DBP Barcode Discrepancy:** Dang Hung Cuong to investigate why a specific barcode cannot be found in DBP while showing as a duplicate (Charlene Tan, Apr 1).
*   **Delivery Window Fix:** Dang Hung Cuong to resolve the delivery window sync issue for "Funa Artistic Hampers & Gifts" (Jie Yi Tan, Apr 1).
*   **Seller Sync Investigation:** Tech team to investigate why DBP accounts 32208 and 32207 failed to sync (Michelle Lim, Mar 31).
*   **Report Email Logic:** Confirm and implement automatic CC of `db-online-marketplace@ntucenterprise.sg` for all DF vendor Sales Breakdown Reports (Iris Chang, Mar 31; cc: Amos Lam, Michelle Lim, Jill Ong).
*   **SKU Live Status:** Investigate why SKU 90248069 is not live on the website despite being published with an offer (Charlene Tan, Mar 31).
*   **Picker App Functionality:** Dang Hung Cuong and Amos Lam to clarify picker app history viewing capabilities for sellers (Iris Chang, Apr 2).

**Decisions Made**
*   Dang Hung Cuong is prioritizing the removal of Item ID: 90244361, new picklist failures, Woah Group offers errors, Pureen barcode truncation, DBP sync issues, Transporter app lag, and delivery window failures.
*   Dang Hung Cuong and Shiva Kumar Yalagunda Bas are assigned to investigate vendor picklist anomalies.
*   **Clarification:** Storage type assignments for GLS-related scanning issues (previously reported Apr 2 regarding Toh Thye San/Aw's Market) are confirmed as non-technical; the operational workaround is applying alternate PA labels immediately. *(Note: The April 4 report concerns a separate temperature QR code discrepancy).*
*   **Completed:** Access linkage for Seller ID 31435 was successfully executed by Shiva Kumar Yalagunda Bas on Mar 27, 11:29 UTC.

**Key Dates & Deadlines**
*   **2026-04-04:** Jing Ying Foo reported Aw's Market FFS packlist error (ambient vs. chilled QR). Thread generated 66 replies; last reply Yesterday at 4:15 PM.
*   **2026-04-02:** Jing Ying Foo raised a "similar issue from Aw's Market" regarding Toh Thye San storage type; Amos Lam escalated urgent fulfillment risk (cc: Sneha Parab, Shiva Kumar Yalagunda Bas); Charlene Tan clarified GLS storage logic and advised on PA label workaround. Iris Chang queried picker app history functionality.
*   **2026-04-01:** Anwar Nur Amalina reported Transporter app lag; Charlene Tan flagged DBP barcode conflicts; Jie Yi Tan reported delivery window sync failure for "Funa Artistic Hampers & Gifts."
*   **2026-03-31:** Michelle Lim reported DBP sync failure for codes 32208 and 32207. Iris Chang raised Sales Breakdown Report email logic query. Charlene Tan reported SKU 90248069 not live.
*   **2026-03-30:** Muhammad Sufi Hakim Bin Safarudin reported picklist generation failures for Order #258155683 and Postponed Order #256653797.


## [13/24] DPD AI Guild
Source: gchat | Group: space/AAQA5_B3lZQ | Last Activity: 2026-04-04T02:02:36.582000+00:00 | Last Updated: 2026-04-05T02:03:48.171213+00:00
### Daily Work Briefing: DPD AI Guild

**1. Key Participants & Roles**
*   **Michael Bui:** Research/Technical Lead – Introduced the new model release.
*   **Zaw Myo Htet:** Technical Strategy/Engineering – Proposed optimization strategy and cost reduction.
*   **Nicholas Tan:** Strategic Monitor – Highlighted industry trends regarding AI executive automation (Meta), critiqued consumer Copilot terms of service, and provided recent hardware context on mobile AI.
*   **Oktavianer Diharja:** Engineering Support – Suggested relevant Go skill utility libraries.

**2. Main Topic**
The discussion centered on leveraging **Mistral Small 4** to optimize local knowledge handling via quantization (Unsloth) to reduce RAG dependency, contextualized by Meta's "AI CEO" automation shift. On March 30, the conversation broadened to include engineering tooling (`samber/cc-skills-golang`). On April 2, Nicholas Tan introduced a critical risk assessment regarding consumer-grade AI assistants, citing Microsoft's restrictive Terms of Service. On April 4, the scope expanded to hardware integration constraints, specifically noting **Gemma4** availability on mobile phones and its non-functional thermal utility in cold climates.

**3. Pending Actions & Ownership**
*   **Action:** Evaluate feasibility of replacing heavy RAG pipelines with quantized open-weight models to reduce costs.
    *   **Owner:** Zaw Myo Htet
    *   **Context:** Requires further technical assessment based on Unsloth documentation.
*   **Action:** Investigate integration of Mistral Small 4's specific architecture (MoE, 119B total/6B active parameters) into current workflows.
    *   **Owner:** TBD (Team-wide due to recent announcement).
*   **Action:** Analyze the implications of Meta's "AI CEO" model on our autonomous agent roadmap.
    *   **Owner:** Nicholas Tan / Team
    *   **Context:** Assess if similar high-level executive automation patterns are applicable to DPD workflows given the efficiency gains in large-scale operations.
*   **Action (New):** Evaluate constraints and thermal side-effects of deploying mobile-native models like Gemma4 for external/cold-weather field operations.
    *   **Owner:** Nicholas Tan / Engineering Team
    *   **Context:** Investigate if "hand warmer" behavior indicates power inefficiency or hardware limitations unsuitable for reliable DPD agent deployment in cold environments.
*   **Action (Existing):** Analyze the implications of Microsoft Copilot Terms of Service to define risk boundaries for internal AI usage.
    *   **Owner:** Nicholas Tan
    *   **Context:** Analyze the "toy" designation and liability clauses to determine why consumer tools are unsuitable for DPD work compared to our proposed autonomous agent stack.

**4. Decisions Made**
*   **Strategic Alignment:** The team acknowledged that while Mistral Small 4 offers specific architectural benefits for cost reduction, the broader industry (exemplified by Meta) is moving toward high-level autonomous agents. This suggests future DPD AI initiatives should balance model quantization with agent-based autonomy.
*   **Risk Assessment:** Nicholas Tan concluded that consumer-grade copilots are "toys not for work" due to restrictive legal frameworks and liability fears evident in Microsoft's Terms of Service. The team agreed to avoid relying on such tools for production workflows, reinforcing the need for custom-built solutions or strictly governed enterprise models.
*   **Hardware Reality Check:** Recent observations regarding **Gemma4** indicate that current mobile-integrated AI may suffer from significant thermal inefficiencies (serving as a "hand warmer" rather than performing compute tasks) in cold climates. This suggests immediate hardware integration hurdles for field-deployable agents relying on standard consumer-grade phones.
*   **Tooling Consideration:** The `samber/cc-skills-golang` library has been flagged for potential use in standardizing skill management for Go-integrated agents, pending technical review by Oktavianer Diharja.

**5. Key Dates & References**
*   **2026-03-17:** Michael Bui announced the release of **Mistral Small 4**.
    *   *Specs:* MoE Architecture, 119B total parameters (6B active), 256k context window, Vision capability.
*   **2026-03-19:** Zaw Myo Htet suggested utilizing **Unsloth** for quantization to make open-weight models more cost-effective and reduce RAG reliance.
*   **2026-03-24:** Nicholas Tan shared an article detailing Mark Zuckerberg's launch of an AI CEO bot to manage Meta operations.
    *   *Relevance:* Highlights the maturity of agentic workflows for executive-level tasks.
*   **2026-03-30:** Oktavianer Diharja recommended the `cc-skills-golang` library for potential skill management integration.
*   **2026-04-02T01:28:01:** Nicholas Tan flagged Microsoft Copilot Terms of Service, labeling it a "toy not for work" due to liability concerns.
    *   *Reference:* https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/termsofuse
*   **2026-04-04T02:02:36:** Nicholas Tan noted **Gemma4** is now native to phones but highlighted its thermal inefficiency in cold climates (double as a hand warmer).

**Thread Status:** Active (Last reply noted recently relative to briefing generation).


## [14/24] QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs | Last Activity: 2026-04-03T09:49:31.896000+00:00 | Last Updated: 2026-04-03T10:34:26.752010+00:00
**Daily Work Briefing: QE <-> All Tribes** (Updated)

**Key Participants & Roles**
*   **Patrick Thun:** Lead/Coordination.
*   **Madhuri Nalamothu:** QA Lead/Test Execution.
*   **Milind Badame:** QA Engineer.
*   **Hang Chawin Tan:** DevOps/Backend Support.
*   **Daryl Ng / Michael Bui:** Dev/Product.
*   **Andin Eswarlal Rajesh:** Development.
*   **Oktavianer Diharja:** Pipeline Support.
*   *(Previous roles: Zaw Myo Htet, Tiong Siong Tee, Yangyu Wang, Pandi, Aman Saxena, Komal Ashokkumar Jain retained for historical context).*

**Main Topics & Discussion**
1.  **LEAP Pipeline Error (Critical/New):** On **2026-04-03**, Patrick Thun reported a `sonar cloud` code analysis failure in the LEAP pipeline affecting `*_test.go` files. *Status:* Active request for assistance; awaiting resolution from DevOps/Dev team.
2.  **DC Membership Subscription & Enrollment (Critical/Escalated):** On **2026-04-02**, Milind Badame confirmed regression failures in DC membership tests (enrollment, promote/demote) due to "Unable to Process Payment" and backend blockage. *Status:* Escalated; awaiting investigation from @Daryl Ng and @Andin Eswarlal Rajesh.
3.  **iOS SnG Flow List Update Bug:** On **2026-04-02**, Madhuri Nalamothu reported that item additions to "My List" via PDP do not update the count on iOS. *Status:* Video evidence shared; discussion ongoing with @Piraba Nagkeeran and @Andin Eswarlal Rajesh.
4.  **iOS Express Delivery UI Issue:** On **2026-04-02**, Madhuri Nalamothu observed clear display issues with "Add to Cart" text on iOS PLP for specific products (e.g., Milo Chocolate Malt). *Status:* Notified @Piraba Nagkeeran.
5.  **BackOffice Domain Validation Gap:** On **2026-04-01**, Milind Badame identified that BackOffice accepts full invalid domains. *Status:* Awaiting investigation from @Daryl Ng.
6.  **Tile Customization - PreOrder:** On **2026-04-01**, Milind Badame inquired about enabling "PreOrder" functionality on tiles. *Status:* Pending response from @Daryl Ng.
7.  **Express Delivery Service Fee Logic:** On **1 Apr**, Milind Badame reported fees are not waived when amounts exceed $30. *Status:* Awaiting investigation by @Daryl Ng.
8.  **Unlimited Product API Error:** On **1 Apr**, Milind Badame queried behavior for increasing counts of unlimited products in BackOffice. *Status:* Under review with @Wai Ching Chan and @Andin Eswarlal Rajesh.
9.  **JWC & Express Delivery Timeouts:** On **1 Apr**, Milind Badame flagged E2E failures due to store timings; requested 24x7 configuration in UAT. *Status:* Pending advice from @Andin Eswarlal Rajesh and @Daryl Ng.
10. **Pipeline Error (Historical):** On **31 Mar**, Hang Chawin Tan reported a failure in `dp-gifting-web`. *Status:* Previously active discussion involving @Madhuri Nalamothu, @Milind Badame, and @Oktavianer Diharja awaiting resolution.
11. **BCRS Swimlane Management:** On **31 Mar**, Milind Badame queried disabling swimlanes post-UAT. *Status:* Discussion ongoing with @Daryl Ng and @Andin Eswarlal Rajesh.
12. **System-Wide Intermittent Failures:** On **30 Mar**, Milind Badame reported HTTP 500 errors affecting order placement, cart, and PDP pages. *Status:* Active investigation for backend instability vs. testing impact.
13. **Order Placement Failure ('Strong Tasty Brew'):** On **30 Mar**, Madhuri Nalamothu reported inability to place orders for non-FP product 'Strong Tasty Brew'. Discussion ongoing with @Piraba Nagkeeran.
14. **MiniGames Blank Screen:** On **30 Mar**, Milind Badame reported a blank white screen on MiniGames tile tap (guest login) on lower Android versions. *Owner:* @Aman Saxena, Mobile Team.
15. **LinkPoints Regression Failure:** Reported on **27 Mar** regarding CLS Award Balance API `500` errors. Status remains Critical/Blocked pending resolution with @Pandi.

**Pending Actions & Ownership**
*   **LEAP Pipeline Resolution:** Resolve SonarCloud analysis failure in `*_test.go`. *Owners:* @Patrick Thun (Reporter), DevOps/Dev Team. **(Highest Priority)**
*   **DC Membership Payment Fix:** Resolve "Unable to Process Payment" errors blocking new enrollments and promote/demote tests. *Owners:* @Daryl Ng, @Andin Eswarlal Rajesh.
*   **iOS SnG List Update Fix:** Investigate count update failure in iOS PDP My List flow. *Owners:* @Piraba Nagkeeran, @Andin Eswarlal Rajesh.
*   **BackOffice Validation Fix:** Investigate and prevent invalid domain entries in BackOffice. *Owner:* @Daryl Ng.

**Decisions Made**
*   DC Membership payment failures are confirmed as a regression blocking new user enrollment and require immediate escalation to Dev.
*   iOS SnG flow "My List" count update failure is validated via video; mobile team engagement initiated.
*   System-wide errors on 30 Mar require immediate triage; potential testing activity suspected but not yet confirmed as root cause.

**Key Dates & Deadlines**
*   **2026-04-03 09:49:** LEAP pipeline SonarCloud error reported by @Patrick Thun.
*   **2026-04-02 06:15:** iOS Express Delivery UI issue reported by @Madhuri Nalamothu.
*   **2026-04-02 03:09:** iOS SnG "My List" update bug reported; video shared.
*   **2026-04-02 04:48 - 05:13:** Escalation regarding DC membership payment failures and backend enrollment blockage.


## [15/24] [Prod Support] Ecom FFS Ops
Source: gchat | Group: space/AAAAde_cYKA | Last Activity: 2026-04-03T08:16:40.717000+00:00 | Last Updated: 2026-04-03T10:35:39.118240+00:00
**Daily Work Briefing: [Prod Support] Ecom FFS Ops (Updated Apr 3)**

**Key Participants & Roles**
*   **Wai Ching Chan / Sampada Shukla:** Operations/Product Leads.
*   **Tok Hong Siang:** TL - TSENGFFS.
*   **Adrian Yap Chye Soon:** Technical Lead/Support.
*   **Akash Gupta:** DPD / Fulfilment / On Call.
*   *(New Inquiry):* **TL HPWP FFS** (Invoked for Order #23032024).

**Main Topics**
1.  **Packlist & SOH Discrepancies (Expanded):** Ongoing investigation into critical `packed_qty` anomalies and Stock on Hand (SOH) NULL values across multiple sites.
    *   **New Critical Incident (Apr 3, ~08:16 AM):** Wai Ching Chan flagged a discrepancy at **Hyper Parkway (Store ID 186)**. Order #23032024 shows `packed_qty` of **10,932,725** vs. `delivered_qty` of **3**.
        *   *Data Context:* Preferred date Apr 3; SKU details indicate significant price impact (MRP null, Price Impact 23.4).
    *   **Resolution Update:** Tok Hong Siang confirmed the previous Tai Seng (Store ID 231) discrepancy (Order #23009418: `packed_qty` 369,076 vs. `delivered_qty` 2) was due to Out of Stock (OOS) and drop-off on Apr 3 at 04:26 AM.
    *   **Ongoing Critical Incidents:**
        *   **Hyper Changi (Store ID 45) - Apr 2:** Order #23013763 shows Packlist status `RECEIVED` but `packed_quantity` is `NULL`.
        *   **Hyper Changi (Store ID 45) - Mar 29:** Order #22972590 showed `packed_qty` of 90,203,969 vs. `delivered_qty` of 2.

2.  **Dispatcher App & Zone Scanning Failure (Mar 28):** Escalation regarding the dispatcher app's inability to scan new zones at **hvivo**.
    *   **Status:** Reported 01:45 AM Mar 28; Adrian Yap Chye Soon provided video evidence for review; technical investigation remains active.

3.  **HCBP Picking Queue Issues (Mar 27):** Escalated urgency regarding "No picking Q" blockage and T18 display failures.
    *   **Status:** Initial blockage reported 02:08 AM; escalated by Ler Whye Ling Angel at 02:52 AM; T18 data failure reported by TL HCBP FFS at 07:47 AM.

**Pending Actions & Ownership**
*   **Data Validation (Urgent - Apr 3):**
    *   *@TL HPWP FFS:* Immediate investigation into Order #23032024 (Hyper Parkway) where `packed_qty` exceeds `delivered_qty`.
    *   *@Adrian Yap Chye Soon:* Immediate investigation into Order #23013763 (Hyper Changi) where Packlist status is `RECEIVED` but `packed_quantity` is `NULL`.
    *   *@Tok Hong Siang / TL - TSENGFFS:* Monitor Tai Seng discrepancy; no action required if OOS logic holds.
    *   *@Akash Gupta / On Call:* Continue validation of SOH NULL values for bulk orders at **HGPT** (Mar 31 incident).
    *   *@Wai Ching Chan @Sampada Shukla:* Prioritize review of Hyper Parkway and Hyper Changi anomalies alongside pending validations for Sun Plaza, VivoCity, and HGPT.

**Decisions Made**
*   **App Release Strategy:** Picker App 10.4.0 rollout remains on hold pending resolution of critical data anomalies (Mar 18–Apr 3). Full rollout is contingent on stability post-fixes, specifically addressing:
    *   The newly discovered Apr 3 Hyper Parkway `packed_qty` anomaly (Order #23032024).
    *   The Apr 2 Hyper Changi `packed_quantity` NULL issue (Order #23013763).
    *   The Mar 31 HGPT SOH NULL issue.
    *   The Mar 29 Hyper Changi anomaly (Order #22972590).
    *   *(Note: Apr 3 Tai Seng discrepancy attributed to OOS; requires monitoring but not a data anomaly fix).*

**Critical Alerts**
*   **Active Alert (Apr 3):** Packlist quantity (`10,932,725`) significantly exceeds delivered quantity (`3`) at **Hyper Parkway (Order #23032024)**. Status: Under investigation by TL HPWP FFS.
*   **Active Alert (Apr 3):** Packlist quantity (`369,076`) exceeds delivered quantity (`2`) at **Tai Seng (Order #23009418)**. Status: Confirmed OOS/Drop-off.
*   **Active Alert (Apr 2):** Packlist status `RECEIVED` but `packed_quantity` is `NULL` at **Hyper Changi (Order #23013763)**.
*   **Active Alert (Mar 31):** Bulk order SOH indicated **NULL** at **HGPT**.
*   **Secondary Active Alert (Mar 28):** Dispatcher app unable to scan new zone at **hvivo**.


## [16/24] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw/GnX6VGfkaJk | Last Activity: 2026-04-03T04:32:06.459000+00:00 | Last Updated: 2026-04-03T06:36:02.710134+00:00
**Daily Work Briefing: Digital Product Development (DPD)**
**Source:** Google Chat Space | **Date Range:** April 2 – April 3, 2026
**Link:** https://chat.google.com/space/AAAAx50IkHw

### Key Participants & Roles
*   **Alvin Choo:** Initiator of the update regarding the Employee Code of Conduct.
*   **Michael Bui:** Clarified specific restrictions on data storage and AI tools.
*   **Winson Lim:** Seeker of official policy documentation; referenced Polly (work.fpg.sg).
*   **Maou Sheng Lee:** Front Office representative highlighting current non-compliant tool usage.
*   **Tan Nhu Duong:** Confirmed document availability but raised policy gaps regarding specific AI approvals.

### Main Topic
The discussion centers on mandatory updates to the Employee Code of Conduct regarding AI platform usage and data security. While a directive was issued prohibiting unapproved tools, recent verification reveals discrepancies between verbal directives and the written policy text.

### Decisions Made & Clarifications
1.  **Initial Directive:** Only **Gemini** was verbally confirmed as the approved tool for company-related items.
2.  **Policy Contradiction Identified:** Tan Nhu Duong (April 3, 04:24) noted that the updated PDF policy document does not explicitly mention which AI platform is approved, creating ambiguity against the verbal "Gemini-only" rule.
3.  **Document Access Confirmed:** The latest Code of Conduct is available on **Polly** at `work.fpg.sg` (Confirmed by Tan Nhu Duong, April 3, 04:21).

### Pending Actions & Ownership
*   **Action:** Identify the definitive source for the approved AI tool designation.
    *   **Owner:** Unassigned (Requested by Tan Nhu Duong on April 3).
    *   **Context:** The written policy lacks specific approval details, necessitating a follow-up to clarify the "Gemini-only" status.
*   **Action:** Resolve discrepancy regarding Front Office usage of **Claude Code**.
    *   **Owner:** Unassigned (Issue raised by Maou Sheng Lee; contradicts verbal Gemini rule).
*   **Action:** Review and acknowledge the attached PDF: *"NTUC Enterprise Mail - Important Updates to the Employee Code of Conduct.pdf"*.
    *   **Owner:** All team members.

### Key Dates & Follow-ups
*   **April 2, 2026 (10:02):** Initial announcement regarding new Code of Conduct updates.
*   **April 2, 2026 (11:30):** Verbal confirmation that only Gemini is permitted for company items.
*   **April 3, 2026 (04:21):** Confirmation that the policy is live on Polly (`work.fpg.sg`).
*   **April 3, 2026 (04:24):** Observation that the written policy text omits specific approved AI tool mentions.
*   **Immediate:** Team members are to raise questions regarding the gap between verbal directives and written policy immediately.

### Summary
The DPD team was initially informed of strict new AI governance rules effective April 2, with a directive stating **Gemini** is the sole approved platform. However, on April 3, Tan Nhu Duong confirmed that while the updated Code of Conduct is accessible via Polly (`work.fpg.sg`), the document text itself does not explicitly list the approved AI tool. This has created an ambiguity between the verbal "Gemini-only" instruction and the written policy. Consequently, a new action item requires identifying the authoritative source for the approved tool designation. Additionally, the conflict regarding the Front Office's use of **Claude Code** remains unresolved pending official clarification.


## [17/24] Digital & Tech - General
Source: gchat | Group: space/AAAAP63CaPo | Last Activity: 2026-04-03T03:52:45.781000+00:00 | Last Updated: 2026-04-03T06:37:02.555295+00:00
**Daily Work Briefing: Digital & Tech (D&T) General**

**Key Participants & Roles**
*   **Trina Boquiren:** Event Coordinator / Team Lead.
*   **Miguel Ho Xian Da:** Developer (iPOS UI, bug reporting).
*   **Ivan Cheow:** Product Owner/Developer (MyApp iOS optimization).
*   **Tan Peng:** Staff Member.
*   **Ching Hui Ng:** Project Lead (Smart Cart Pilot).
*   **Sip Khoon Tan:** Training Coordinator.
*   **Flora Wo Ke:** Staff Member reporting lost items.
*   **Dennis Seah:** Guidance provider for Digital Office Access.
*   **James Lai Li Hao & Mohammed Miran:** iOS/Android support.
*   **Cory Meilany:** Communications design and digital display coordination.

**Main Topics & Updates**
1.  **Digital Office Access Launch:** Successfully deployed to all FP Hub colleagues earlier in the week (Good Friday, April 3). The system has recorded approximately **400 active users**. This initiative received positive feedback for its ease of use and user experience.
2.  **MyApp iOS Update:** Previously released optimized door access featuring Lock Screen Widget, Tap Method, and In-App Method. The app must run in the background for scanning; Miguel Ho Xian Da handles bug reports.
3.  **Smart Cart Pilot:** Launched at **Punggol Oasis Terraces** (681 Punggol Drive, #B1-01). Features include attachable Smart Cart Tablets and integration with **Super** format colleagues and **Pricer** ESLs for LED blinking.
4.  **AI Training:** "Workbench Hands-on Training" on Gemini Enterprise & NotebookLM is scheduled for **Thursday, 19 March** (2:00 PM – 5:00 PM) at FP Hub L10. Virtual options available; alternative dates are 8 or 9 April.

**Pending Actions & Ownership**
*   **Lost Items – AirPods Pro:** Flora Wo Ke requests notification if anyone found an **AirPods Pro (2nd Gen) with case** on **L11**. The item was likely left in the office last week. *Owner: Staff who find item / Security.*
*   **Lost Items – Meeting Room 18:** Report lost phone/wallet previously noted for Tan Peng/Security.
*(Note: RSVP deadlines for March events have passed; no new actions required for All Hands or AI Training).

**Decisions Made**
*   Approved launch of Smart Cart pilot at Punggol Oasis Terraces with attachable tablets and ESL integration.
*   Confirmed iOS door access optimization requires the app to run in the background for widget functionality.
*   **Digital Office Access:** Confirmed successful rollout across FP Hub with high adoption (400 users).

**Key Dates & Deadlines**
*   **12 March 2026:** D&T All Hands (Completed/Past).
*   **19 March 2026:** Gemini Enterprise & NotebookLM Training (Past).
*   **8 or 9 April 2026:** Alternative dates for AI training.
*   **3 April 2026:** Digital Office Access launched and active at FP Hub.

**Historical Context**
The transition to digital access marks a significant milestone in the "Tech made easy" initiative, driven by cross-functional collaboration between D&T, HR, and operations teams.


## [18/24] Alvin, Gopalakrishna
Source: gchat | Group: space/AAQAMGrBBNE | Last Activity: 2026-04-03T03:56:30.110000+00:00 | Last Updated: 2026-04-03T06:37:21.071532+00:00
**Daily Work Briefing: Google Chat Summary (Updated)**

**Resource:** Alvin Choo, Gopalakrishna Dhulipati
**Metadata:** 6 messages | https://chat.google.com/space/AAQAMGrBBNE

**Key Participants & Roles**
*   **Alvin Choo:** Executive providing final guidance and expanding the scope of the warning.
*   **Gopalakrishna Dhulipati:** Compliance officer who flagged the initial violation regarding data privacy.
*   **Michael Bui:** Employee whose LinkedIn post triggered the discussion; identified as having shared metrics.
*   **Fiona:** Third party mentioned in the conversation who previously shared numbers and was instructed to remove them.

**Main Topic**
The discussion addresses a violation of the **Employee Code of Conduct** concerning the sharing of confidential **RMN metrics** on social media. While Gopalakrishna initially flagged Michael Bui's post for containing competitor-usable data, Alvin Choo subsequently reinforced that business metrics are sensitive and must not be shared generally.

**Actions & Ownership**
*   **Action:** Immediate removal of confidential RMN metrics from the LinkedIn post.
    *   **Owner:** Michael Bui (Completed).
*   **Action:** Broad dissemination of a compliance reminder regarding business metrics sensitivity to all employees.
    *   **Owner:** Alvin Choo (Implicit directive issued at 03:56:30 UTC); Gopalakrishna and Michael expected to assist in reinforcing this message.
*   **Action:** Monitoring social media activity for potential data leaks.
    *   **Owner:** All employees, with specific emphasis on caution regarding engagement (liking/resharing).

**Decisions Made**
*   **Strict Enforcement:** The organization maintains a "strict" stance on information security, extending beyond direct posting to include any interaction with confidential data.
*   **Expanded Scope:** Following Alvin Choo's directive at 03:56:30 UTC, the warning is no longer limited to Michael Bui but applies universally; all personnel are reminded that "business metrics is sensitive."

**Key Dates & Follow-ups**
*   **Date of Incident/Discussion:** April 3, 2026.
    *   *Initial Flag:* 01:27:15 UTC (Gopalakrishna alert).
    *   *Acknowledgment & Removal:* 02:06:54 UTC (Michael Bui confirms re-use of numbers and removal).
    *   *Further Guidance:* 02:10:41 UTC – 02:12:39 UTC (Discussion on strictness and future caution).
    *   *Final Directive:* **03:56:30 UTC** (Alvin Choo instructed to remind all personnel regarding the sensitivity of business metrics).
*   **Follow-up Status:** The specific removal action for Michael Bui is complete. A new organizational-wide reminder has been initiated by Alvin Choo to prevent future occurrences across the workforce. No pending action items remain for Michael Bui personally, but the conversation now serves as a broader policy enforcement alert for all staff.

**Resource Reference**
*   **Chat URL:** https://chat.google.com/space/AAQAMGrBBNE


## [19/24] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Last Activity: 2026-04-02T14:36:56.701000+00:00 | Last Updated: 2026-04-02T22:37:27.483091+00:00
**Daily Work Briefing: Nikhil Grover & Michael Bui (Updated)**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator; coordinating incident fixes, ticket updates for the FE team, and RMN project preparation.
*   **Michael Bui:** Technical Lead (Engineering); currently on leave (April 6–12) but available for urgent clarifications before departure.

**Main Topics & Recent Developments (Mar 28 – Apr 02)**
1.  **Homepage Ad Race Condition (Critical):**
    *   A race condition identified March 27 remains unresolved regarding intermittent homepage ad rendering (symptoms: 2 ads with old slots or 6 ads with new slots).
    *   **Status:** Persisted through Mar 30 night despite slot alignment troubleshooting. Escalated to Michael Bui during his vacation planning phase.
2.  **Topic Pivot: RMN & Project Light (Apr 02):**
    *   On April 2, Michael requested a call to clarify details regarding **RMN** within **Project Light**.
    *   Motivation: Michael aims to finalize clarifications to prepare for his upcoming long weekend before leaving on April 6.

**Decisions Made & Status Updates**
*   **Meeting Scheduling:** A synchronous discussion was initially proposed for the afternoon of April 2. Nikhil declined due to personal obligations, suggesting a reschedule to "tomorrow (April 3)" or Monday instead. Michael confirmed availability for the following day ("Tmr") upon Nikhil's awakening.
*   **Deployment Readiness:** The pending resolution of the homepage ad race condition continues to delay deployment readiness.
*   **Ticket Coordination:** Scheduled update for DPD-838 with slot value examples and OSMOS logic remains a priority, coordinated with Alvin (originally scheduled Mar 29).

**Pending Actions & Owners**
*   **RMN Clarification Call (Michael Bui & Nikhil Grover):** Reschedule the catchup regarding RMN in Project Light. Michael intends to hold this discussion early on April 3 ("Tmr") or Monday to facilitate his weekend preparation.
*   **Incident Resolution (Michael Bui):** Review the intermittent homepage ad issue reported by Yangyu/Nikhil; address slot sequencing failures.
*   **Ticket Updates (Nikhil Grover):** Proceed with updating DPD-838 and coordinating with Alvin.
*   **Timeline Verification (Nikhil Grover):** Confirm the timeline for OSMOS `pcnt` limit expansion (>10), expected by early April.

**Key Dates & Deadlines**
*   **March 27, 2026:** Race condition identified.
*   **April 2, 2026 (14:35 UTC):** Michael clarified intent to resolve RMN/Project Light questions before his leave; availability set for the following morning.
*   **April 6–12, 2026:** Michael Bui's leave period (island with limited connectivity).

**Historical Context Note**
The conversation initially focused on technical scope: video content restricted to Omni Home/FP Pay, OSMOS `pcnt` limits set at 10 (expansion expected early April), and slot values being optional for uniqueness. On March 30, the focus shifted to a critical incident where intermittent rendering persisted despite troubleshooting. By April 2, with Michael's departure approaching, priorities expanded to include **RMN** discussions within **Project Light**. While Nikhil initially cited a $1,250/day impact (clarified as part of overall drops excluding specific advertiser campaign losses), the immediate operational focus remains on resolving the ad race condition and clearing RMN queries before April 6.


## [20/24] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/yI8UlY4--fY | Last Activity: 2026-04-02T11:07:37.842000+00:00 | Last Updated: 2026-04-02T22:37:59.836478+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Lead/Manager (Assigns deliverables, validates scope).
*   **Michael Bui:** RMN Specialist/Tech Lead (Responsible for planning and alignment on RMN scenarios).
*   **Nikhil:** Business Stakeholder (Subject matter expert for ads in PLP and OSMOS).
*   **Rock:** Team Member/Peer (Assumed scope of work regarding RMN).

**Main Topic**
Clarification of "homework" deliverables due early next week (targeting April 7, 2026) across Defense and Attack streams. A specific discussion arose regarding the ownership and scoping of the **RMN (Real-time Media Network)** work required for the new ads product.

**Pending Actions & Ownership**
*   **Michael Bui:**
    *   Align with Nikhil on "ads in PLP" and business requirements for running RMN with OSMOS for complex scenarios.
    *   Produce a plan and timeline based on this alignment.
    *   Provide an estimate to Alvin Choo (and Rock) confirming the team is undertaking the work.
*   **Team (Defense Stream):**
    *   Firm up support model details: SLOs, on-call schedules, and Zendesk integration.
    *   Create an overview plan for data migration.
    *   Develop a later-stage app transition plan.
*   **Team (Attack Stream):**
    *   Deliver a workable UAT version of the Identity SDK for user sessions.
    *   Draft the Core Payment tech document.
    *   Plan integration tests to clarify all integration points.

**Decisions Made**
*   The scope for RMN is confirmed as requiring business alignment with Nikhil before final planning can proceed.
*   It was clarified that internal leadership (Alvin and Rock) assumes the team will execute the RMN work; therefore, a formal estimate and plan are now mandatory deliverables from Michael Bui.

**Key Dates & Deadlines**
*   **Target Delivery:** Early next week (Week commencing April 6, 2026).
*   **Reference Date:** Conversation took place on April 2, 2026.

**Follow-ups Required**
*   Michael Bui to initiate alignment with Nikhil immediately upon returning from the EA sharing session mentioned by Alvin Choo.


## [21/24] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4 | Last Activity: 2026-04-02T11:02:51.709000+00:00 | Last Updated: 2026-04-02T22:38:39.808939+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Space Creator; Lead coordinating the briefing.
*   **Daryl Ng, Gopalakrishna Dhulipati, Tiong Siong Tee, Michael Bui, Akash Gupta:** Designated "Project Light Attack and Defence Leads".
*   **Tiong Siong Tee:** Invited to calls by Alvin (confirmed April 1).

**Main Topic**
Following the transition to active strategic planning ("Room 2") on March 24, the team is executing a split strategy between "Attack" (feature development) and "Defense" (operational stability). While collaboration on **"RMN"** and **"Payment"** slides began March 24, technical direction remains focused on decoupling from SAP. On **April 2**, Alvin Choo assigned specific homework tasks to be aimed for completion early next week, shifting focus toward concrete deliverables rather than just slide preparation.

**Pending Actions & Ownership**
*   **Action (Defense): Firm up the support model.**
    *   **Scope:** Define Support Level Objectives (SLOs), on-call rotation, and Zendesk integration.
    *   **Ownership:** Defense Team/Alvin Choo.
    *   **Status:** Assigned April 2, 11:02 AM UTC; target completion early next week.
*   **Action (Defense): Create an overview plan for data migration.**
    *   **Context:** Follows the "No Data Migration" strategy proposed by Alvin Choo on March 30 to reduce risk.
    *   **Ownership:** Engineering Team.
    *   **Status:** Assigned April 2, 11:02 AM UTC; target completion early next week.
*   **Action (Defense): Develop app transition plan.**
    *   **Status:** Can be deferred until later; high-priority overview required first.
*   **Action (Attack): Produce a workable UAT version of the Identity SDK for user sessions.**
    *   **Ownership:** Engineering Team.
    *   **Status:** Assigned April 2, 11:02 AM UTC.
*   **Action (Attack): Finalize Core Payment technical document.**
    *   **Ownership:** Daryl Ng / Engineering Team.
    *   **Status:** Assigned April 2, 11:02 AM UTC.
*   **Action (Attack): Plan RMN work to achieve the new ads product.**
    *   **Ownership:** RMN Leads.
    *   **Status:** Assigned April 2, 11:02 AM UTC.
*   **Action (Attack): Initiate integration testing strategy.**
    *   **Goal:** Clarify all integration points and establish a clear plan.
    *   **Ownership:** Daryl Ng / Engineering Team.
    *   **Status:** Assigned April 2, 11:02 AM UTC.

**Previous Pending Actions (Re-evaluated)**
*   **Action:** Evaluate technical feasibility of adding a "Data8" layer between DSP and SAP.
    *   **Status:** Risk raised by Tiong Siong Tee on April 2, 06:31 AM UTC regarding reconciliation issues with Caltran/Data8. This remains under review pending the new data migration overview plan.
*   **Action:** Provide updated organizational chart to Daryl Ng.
    *   **Status:** Requested at 07:01 AM UTC on April 2; replies received from Alvin Choo.

**Decisions Made & Shifts**
*   **Workstream Split:** Deliberate separation into "Attack" (product features, SDK, payments) and "Defense" (SLOs, support, migration strategy).
*   **Timeline:** New deliverables targeted for early next week following the April 2 briefing.
*   **System Architecture:** SAP integration remains decoupled from core operational logic; designated strictly for finance and sales records.

**Key Dates & Follow-ups**
*   **April 2, 11:02 AM UTC:** Alvin Choo assigned specific "homework" tasks (Defense support model, migration overview, Attack SDK UAT, Payment docs, RMN plan, Integration test strategy).
*   **April 2, 07:01 AM UTC:** Daryl Ng requested org chart; replies received.
*   **April 2, 06:31 AM UTC:** Tiong Siong Tee queried Data8/SAP reconciliation risks.
*   **March 30:** "No Data Migration" strategy proposed by Alvin Choo.


## [22/24] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/jPGy0nmdYfc | Last Activity: 2026-04-02T10:50:51.840000+00:00 | Last Updated: 2026-04-02T22:40:47.648949+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Daryl Ng:** Lead requesting clarification on team composition.
*   **Alvin Choo:** Participant providing the updated organizational documentation.
*   **Tiong Siong Tee:** Participant offering context regarding information retention.

**Main Topic**
Discussion centered on resolving memory overload regarding specific personnel assignments within Daryl Ng's team. The conversation shifted from a status inquiry to the successful delivery of required documentation to verify the current roster.

**Pending Actions & Ownership**
*   **Action:** No pending actions; the request for the organization chart has been fulfilled.
*   **Owner:** Alvin Choo (Completed).
*   **Status:** Resolved. Alvin Choo provided the updated organization chart containing team member details, addressing Daryl Ng's query.

**Decisions Made**
No formal strategic decisions were recorded; however, a resolution was reached regarding the immediate need for verification. The team agreed to rely on the newly provided external documentation from Alvin Choo rather than internal recall to ensure accuracy of the roster.

**Key Dates & Follow-ups**
*   **Date:** April 2, 2026 (07:01 – 07:02 UTC).
*   **Follow-up Required:** None at this time. The immediate query regarding team composition has been addressed.

**Contextual Notes**
The conversation highlighted a temporary information gap where internal recall was insufficient for verifying team roles. This gap was bridged by Alvin Choo's provision of the updated organization chart, shifting the workflow from "pending verification" to "information confirmed." The interaction underscores the necessity of centralized documentation for Project Light Attack and Defence Leads to prevent future roster confusion.

**Metadata Reference**
*   **Source:** Project Light Attack and Defence Leads
*   **Message Count:** 4
*   **URL:** https://chat.google.com/space/AAQAsFyLso4


## [23/24] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/9KYZsmc-670 | Last Activity: 2026-04-02T10:02:11.714000+00:00 | Last Updated: 2026-04-02T10:46:03.489055+00:00
**Daily Work Briefing: S&G Store Enablement Discussion (Updated)**

**Key Participants & Roles**
*   **Daryl Ng:** Digital Product Development (Inquiry lead, capacity planning).
*   **Sneha Parab:** Digital Product Development / SME (Process owner, technical implementation).
*   **David:** Action Owner (Ticket submission/assignment).
*   **Hanafi:** Ticket Processor.

**Main Topic**
Assessment of effort and timeline for a temporary "Pop-up S&G" store setup at Jewel. Discussion focused on verifying SOPs, identifying dependencies, and finalizing the request workflow.

**Decisions Made**
*   **Documentation:** The previously cited SOP is outdated. The team agreed to utilize Hanafi's automated process, referencing version 3.0 of the store setup doc or the new Jira form.
*   **Workflow Confirmation:** While SAP handles master data downloads directly to GCS, DPD must still create the store in DBP and coordinate with the DE team for search/browse data flow upon receiving Stock on Hand (SOH).
*   **Timeline Estimate:** End-to-end lead time is estimated at approximately 2 weeks.

**Pending Actions & Ownership**
1.  **Submit Request Ticket:**
    *   **Owner:** David.
    *   **Status:** **Completed.** The request was submitted via the new Jira form to accommodate the team's workload starting next week.
    *   **Reference Form:** https://ntuclink.atlassian.net/jira/core/projects/STOR/form/577
2.  **Ticket Assignment:**
    *   **Owner:** David / Daryl Ng.
    *   **Action:** **Completed.** As of April 2, 2026, the ticket has been assigned to **Hanafi** for processing.
    *   **Update:** This action supersedes previous pending assignments; no further assignment is required at this stage.
3.  **Stakeholder Coordination:**
    *   **Owner:** Daryl Ng / Brendon.
    *   **Action:** Confirm with Brendon regarding awareness of this specific request and ensure proper handover if he is not the originator.

**Key Dates & Follow-ups**
*   **Event Timeline:** The pop-up store event is likely to occur approximately 3 weeks from April 1, 2026.
*   **Current Date:** April 2, 2026.
*   **Capacity Check:** Request submission was prioritized immediately to prevent delays given the team's increased workload starting next week.

**Reference Links**
*   Outdated SOP: https://ntuclink.atlassian.net/wiki/spaces/SE/pages/1995999558/S+G+Store+Enabling+-+SOP
*   Current Setup Doc (v3.0): https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008160308/Store+setup+doc+v3.0


## [24/24] RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU/PYIHH8s-2LQ | Last Activity: 2026-04-02T09:54:24.246000+00:00 | Last Updated: 2026-04-02T10:46:21.723634+00:00
**Daily Work Briefing: RMN Leadership Space**

**Key Participants & Roles**
*   **Bryan Choong:** Team Leader/Sender of directive.
*   **Allen Umali:** Team Member/Respondent (completed initial task).
*   **Christopher Yong:** Team Member (inquired and confirmed compliance).
*   **Rajiv:** Subject matter contact (initiated the request).
*   **Wendi:** Team member whose acknowledgement was shared by Christopher.
*   **Wilson:** Source of relevant message on MT chat.
*   **@all:** The broader team audience addressed in the message.

**Main Topic**
The conversation concerns urgent updates to the **Employee Code of Conduct**. Leadership is emphasizing a shift in compliance posture and mindset, requiring explicit acknowledgement from all team members regarding these new updates.

**Pending Actions & Ownership**
*   **Action:** Review HR email and Wilson's MT chat message for Code of Conduct updates; provide explicit acknowledgement.
*   **Owner:** Team members (specifically those who missed the initial notification).
*   **Status Update:** Christopher Yong confirmed completion ("Done") at 09:45 UTC on April 2, 2026, by sharing Wendi's acknowledgement.

**Decisions Made**
No new policy decisions were made. The discussion clarified that the directive originated from Rajiv and was disseminated via a specific HR email and a message from Wilson on MT chat. Immediate, explicit acknowledgement is required to satisfy organizational compliance protocols.

**Key Dates & Deadlines**
*   **Date:** April 2, 2026.
*   **Deadlines:**
    *   Initial deadline: "Within the day" (set at 02:37 UTC).
    *   Allen Umali confirmed completion: 03:42 UTC.
    *   Christopher Yong confirmed completion: 09:45 UTC.

**Summary of Flow**
1.  **02:37 UTC:** Bryan Choong notified the team that Rajiv initiated a request for explicit acknowledgement regarding Employee Code of Conduct updates, noting only one response was received. He set a deadline for the same day.
2.  **03:42 UTC:** Allen Umali confirmed completion ("Done").
3.  **09:16 UTC:** Christopher Yong apologized for missing the initial notification and asked if the request was via email, quoting Bryan's original instruction.
4.  **09:17 UTC:** Bryan Choong confirmed it was via email and directed the team to check Wilson's message on MT chat alongside the HR email.
5.  **09:45 UTC:** Christopher Yong confirmed he had read the email and Code of Conduct, sharing Wendi's acknowledgement as proof of completion.

**Reference Data**
*   **Space URL:** https://chat.google.com/space/AAAAQQGZSZU
*   **Sources:** HR Email (Code of Conduct updates), Wilson's message on MT chat.
