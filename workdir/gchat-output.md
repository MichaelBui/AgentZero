

## [1/70] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 16 | Last Activity: 2026-03-29T02:24:00.511000+00:00 | Last Updated: 2026-03-29T02:34:03.704623+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (Updated March 29, 02:30 UTC)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
Instability persists into **March 29**, evolving from isolated backend latency to recurrent cyclical failures across Identity APIs, Recommendation services (Orchid), and Mobile App reliability. The issue profile now includes concurrent error spikes in `engage-my-persona-api-go` (Dynamics) and intermittent success rate drops for Orchid (Journey) alongside mobile cart errors (Compass).

**Status Summary & Timeline (March 28–29)**
*   **Identity API Instability (`engage-my-persona-api-go` / Squad Dynamics):**
    *   *Previous Session:* Recovered @ 21:59 UTC March 28.
    *   *New Activity (Mar 29):* Cyclical volatility resumed late night.
        *   **01:17:** Triggered (Recoveried); Metric value 0.091%.
        *   **02:06:** Triggered; Error rate 0.136% (Monitor #92965074).
        *   **02:23:** Triggered; Error rate 0.104%.
    *   *Current Status:* Unstable. Multiple triggers between 02:06 and 02:23 UTC. Monitor #92965074 active.
*   **Recommendation Services (`frontend-gateway` / Squad Journey):**
    *   *Orchid Service:* Recurring failures observed on Mar 29.
        *   **01:19:** Triggered (99.855% success); Recovered @ 01:32 UTC.
        *   **02:07:** Triggered (99.835% success); Recovered @ 02:20 UTC.
    *   *Boughtbought Service:* Last seen stable after 22:16 UTC Mar 28; no new alerts reported in this window.
*   **Mobile Reliability (`ef-ios` / `ef-android` / Squad Compass):**
    *   **iOS:** Intermittent "view user linkpoints" failures at **01:46** (99.18% success); Recovered @ 01:47 UTC.
    *   **Android:** Concurrent issues with "view user linkpoints" (**01:50**, 99.618%) and S&G cart errors (**02:19** >10 errors/5m). Both recovered by **02:23–02:24 UTC**.

**Pending Actions & Ownership**
*   **Investigate Identity API Recurrence:** Analyze the root cause of repeated high error rates in `engage-my-persona-api-go` (Peak 0.136% @ 02:06) and the specific `/user/profile/myinfo` endpoint failure at 02:05 UTC. Owner: **Squad Dynamics**.
*   **Analyze Orchid Intermittency:** Investigate why Orchid success rates dipped below 99.9% twice on March 29 (01:19, 02:07). Owner: **Squad Journey**.
*   **Review Mobile Cart Errors:** Correlate the Android S&G cart error spike at 02:19 with the concurrent Identity API latency. Owner: **Squad Compass**, **Squad Journey**.

**Decisions Made**
*   **Severity Escalation:** Incidents remain critical due to multi-squad, cross-platform recurrence (Backend + iOS + Android) within a single hour window on March 29.
*   **Pattern Continuity:** The ecosystem instability has shifted from "isolated spikes" to "sustained cyclical failures." Identity API errors are now occurring roughly every 30–45 minutes, accompanied by parallel drops in mobile and recommendation service reliability.

**Key Dates & Follow-ups**
*   **Active Window:** March 28–29 (UTC). Recent critical activity: **01:17 – 02:24 UTC**.
*   **Reference Links:**
    *   `engage-my-persona-api-go` Error Monitor #92965074 (Peak: 0.136% @ 02:06)
    *   `frontend-gateway` Orchid Monitor #17448311 (Lowest: 99.835% @ 02:07)
    *   `ef-android` Cart Errors Monitor #20382959 (Triggered @ 02:19)


## [2/70] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-03-29T02:17:25.343000+00:00 | Last Updated: 2026-03-29T02:34:43.588009+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Update)**
**Date:** March 29, 2026 (Early AM Shift)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 594

### Key Participants & Roles
*   **System/Tool:** Datadog App (Automated Monitoring)
*   **Notification Channel:** `@hangouts-ShoppingCartNotification`
*   **Ownership Teams:** `dpd-pricing`, `dpd-pricing-cart`.

### Main Topic
Instability persists in `frontend-gateway` and `st-cart-prod`. The incident has evolved into a high-frequency oscillation affecting Wish List operations, Cart API performance, and Checkout reliability. Critical **P2 SLO Error Budget Alert** status remains active with continued high consumption. Latency spikes now span PUT (Wish List), POST (Cart/Checkout), GET (Wish List/Cart), and success rate degradation.

### Incident Timeline & Actions
**Previous Context:**
*   *Activity from March 20–March 28 regarding `frontend-gateway` latency and checkout dips.*

**New Activity (Overnight Shift, March 29 UTC)**
*   **00:17–00:48 UTC:** Recurring failure of Cart success rates. Multiple triggers on Monitor `22710472`:
    *   00:17: Success rate dropped to **99.495%**.
    *   00:30: Success rate dropped to **99.627%**.
    *   00:48: Success rate dropped to **99.716%**.
    *   All instances recovered to 100.0% within ~10 minutes of triggering.
*   **00:18 UTC:** Checkout success rate triggered on Monitor `21245708`, dropping to **99.868%** before recovering at 00:28 UTC.
*   **01:03–02:17 UTC:** Intermittent latency spikes on `get /api/wish-list/_id` (`frontend-gateway`).
    *   01:03: P90 reached **2.171s** (Threshold: 1.7s). Recovered at 01:08 (1.52s).
    *   02:13: P90 reached **2.239s**. Recovered at 02:17 (1.451s).

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** The failure mode has expanded to a consistent oscillation pattern where success rates dip below 99.9% for Cart (Monitor `22710472`) and Checkout (Monitor `21245708`) in short bursts, often followed by rapid recovery. This suggests transient dependency exhaustion or load balancing issues rather than permanent code failure.
*   **Immediate Action Required:** Correlate trace data for the 00:17–02:17 UTC window. Specifically investigate Event IDs `8564443400027888473` (Cart success), `8564443674557369934` (Checkout success), and `8564489180175830165` (Wish List latency).

### Decisions Made
*   **Priority Escalation:** Status remains **"Critical Incident"**. Activity extends continuously from March 20 through at least 02:17 UTC on March 29.
*   **Focus Shift:** Analysis must now cover the rapid oscillation of success rates (dropping to ~99.5%) and latency spikes (>2s P90) occurring every ~1 hour. Correlate Monitor `22710472` (Cart Success) with Monitor `21245708` (Checkout Success) and Monitor `21245720` (Wish List Latency).
*   **Metric Update:** Confirmed rotating failure mode: Cart success rate dipped as low as 99.495% on March 29, while Checkout success dropped to 99.868%. Wish List GET P90 spiked to 2.239s.

### Key Dates & Follow-ups
*   **Critical Window:** Extended activity from March 20 through at least March 29, 02:17 UTC.
*   **Follow-up:** Immediate trace correlation for the overnight oscillation pattern (00:17–02:17 UTC) to determine if the root cause is environmental or traffic-based before shift handover.

### References
*   **Active Monitors:** `22710472` (Post Cart Success), `21245708` (Checkout Success), `21245720` (Wish List GET P90).
*   **Service Tags:** `service:frontend-gateway`, `service:st-cart-prod`, `team:dpd-pricing`.


## [3/70] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE/qsfGRIhmHp4 | Messages: 9 | Last Activity: 2026-03-29T02:13:44.614000+00:00 | Last Updated: 2026-03-29T02:35:00.963824+00:00
**Daily Work Briefing: Google Chat Summary**
**Resource:** Nikhil Grover
**Date:** March 28–29, 2026

**Key Participants & Roles**
*   **Nikhil Grover:** Product/Strategy lead; clarifies scope and evaluates technical complexity regarding service migration.
*   **Michael Bui:** Engineering lead; details routing architecture between legacy MPS (NodeJS) and the new RMN ad service (Golang).

**Main Topic**
Refined discussion on migrating request routing from legacy MPS services to the new RMN ad service. The focus shifted from video format handling to ensuring all traffic (including category, promotion, and search pages) routes correctly. The team assessed the risks of implementing dynamic slot logic in two locations versus a single unified location due to poor code quality in the existing NodeJS stack.

**Decisions Made & Technical Strategy**
*   **Migration Scope:** All requests from category, promotion, and search pages currently using old MPS services must be routed to the new RMN ad service (Golang).
*   **Implementation Approach:** Logic must be implemented in a single location within the new service. Implementing logic in two places is rejected due to higher complexity and risk, specifically citing that the existing NodeJS code lacks sufficient test coverage.
*   **Instrumentation:** New instrumentation requirements were raised but confirmed as necessary for the unified approach; however, no specific timeline impact was noted.

**Pending Actions & Ownership**
*   **Routing Migration:** Michael Bui must migrate all page types (including category, promotion, search) to send requests to the new RMN ad service. *Owner: Michael Bui.*
*   **SIT Completion:** Finalize System Integration Testing (SIT) by April 7–8, 2026. *Owner: Engineering Team.*
*   **UAT & Deployment:** Execute User Acceptance Testing immediately post-SIT to meet the production deadline. *Owner: Michael Bui/Engineering Team.*

**Key Dates & Deadlines**
*   **SIT Completion Target:** April 7 or 8, 2026.
*   **Production Deployment Target:** April 9, 2026 (contingent on SIT completion and assuming work proceeds after team members return).

**Summary Notes**
Michael Bui clarified that the migration is driven by the need to centralize dynamic slot logic in the new Golang-based RMN ad service, rather than just handling video formats. He noted that the legacy NodeJS MPS code has poor test coverage, making a dual-implementation approach too risky. Consequently, Nikhil Grover confirmed the plan to implement logic in one place. Bui assured that despite the necessary migration of category, promotion, and search pages, the April 9th production launch remains feasible provided SIT is completed by April 7–8. Grover sought confirmation that this timeline assumes work begins immediately upon team return.


## [4/70] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Messages: 16 | Last Activity: 2026-03-29T02:12:15.875000+00:00 | Last Updated: 2026-03-29T02:35:35.526088+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Mar 29, 02:15 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`.
*   **Escalations:** `@oncall-dpd-staff-excellence-pdm`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Retail Media.

**Main Topic**
**P3/P4 ALERTS (Mostly Recovered):** The `sku-store-attribute` job experienced intermittent low file counts (P3) between Mar 28 and Mar 29, now **recovered**. Concurrently, the `marketing-service` has shown multiple throughput anomalies (P4) on Mar 29, also **recovered**. The persistent critical error on `fp-search-indexer` remains active since Mar 18.

**Pending Actions & Ownership**
*   **Action:** **INVESTIGATE LOW FILE COUNT (`sku-store-attribute`):** [Status: RESOLVED] Address P3 alert for job processing < 6 files in 4h.
    *   **Owner:** Grocery Discovery Team.
    *   **Status:** **RECOVERED (01:21 UTC Mar 29).** Alert triggered at 22:06 and 00:54 UTC; recovered at 00:59 UTC. Monitor ID: `20382848`. Logs confirmed >6 events matched in the last 5h.
*   **Action:** **INVESTIGATE THROUGHPUT ANOMALY (`marketing-service`):** [Status: RESOLVED] Address P4 alert regarding abnormal throughput on `env:prod`.
    *   **Owner:** Retail Media Team (`@opsgenie-dpd-grocery-retail-media`) & Grocery Discovery.
    *   **Status:** **RECOVERED (02:12 UTC Mar 29).** Multiple triggers occurred between 00:18 and 01:21 UTC; final resolution at 02:12 UTC. Monitor ID: `17447110`.
*   **Action:** **PERSISTENT INVESTIGATION:** Address critical errors on `fp-search-indexer` (env: prod).
    *   **Owner:** Product Data Management On-Call.
    *   **Status:** Active since Mar 18; last re-triggered Mar 24, 16:29 UTC. No resolution achieved.

**Decisions Made**
*   The `sku-store-attribute` P3 alert (Monitor ID: `20382848`) is confirmed resolved at 00:59 UTC after log event counts normalized to >6.
*   The `marketing-service` throughput anomaly (Monitor ID: `17447110`) triggered three times on Mar 29 (00:18, 00:59, 01:21 UTC) but is now recovered at 02:12 UTC.
*   The `fp-search-indexer` failure continues to require critical focus by Product Data Management.

**Key Dates & Follow-ups (Mar 28–29, 2026)**
*   **Service: `sku-store-attribute` (P3 - Grocery Discovery) [RECOVERED]**
    *   *Latest Timeline:* Triggered Mar 28 (22:06 UTC); Re-triggered Mar 29 (00:54 UTC); Recovered Mar 29 (00:59 UTC).
    *   *Monitor Query:* `logs("service:fpon-catalogue-job-sku-store-attribute \"processed Files:\"").index("*").rollup("count").last("5h") < 6`
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/20382848)
*   **Service: `marketing-service` (P4 - Retail Media) [RECOVERED]**
    *   *Latest Timeline:* Triggered Mar 29 (00:18, 01:21 UTC); Recovered Mar 29 (00:59, 02:12 UTC).
    *   *Monitor Query:* `avg(last_4h):anomalies(sum:trace.http.request.hits{env:prod,service:marketing-service}...) >= 1`
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/17447110) | [K8s Console] | [Runbook]
*   **Service: `fp-search-indexer` (P2 - Product Data Management) [ACTIVE CRITICAL]**
    *   *Latest Timeline:* Active since Mar 18; re-triggered Mar 24, 16:29 UTC.

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c


## [5/70] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE/ghXHBY1ul1k | Messages: 6 | Last Activity: 2026-03-29T01:14:25.795000+00:00 | Last Updated: 2026-03-29T02:35:54.864658+00:00
**Daily Work Briefing: OSMOS Banner Logic & Slot Transition Strategy**

**Key Participants & Roles**
*   **Nikhil Grover:** Product/Technical Lead. Explained the interim nature of the "slot" field and confirmed logic for duplicate handling.
*   **Michael Bui:** Technical Stakeholder. Validated tracking object positioning logic and questioned the necessity of static slots in a dynamic environment.

**Main Topic**
Discussion refined the business logic for the optional "slot" field in OSMOS, clarifying its role as an interim transition mechanism until May 1, 2026. The conversation addressed edge-case handling for empty/null values and duplicate slot numbers, alongside the rationale for maintaining this field during the current sales cycle.

**Decisions Made & Clarified Logic**
1.  **Interim Purpose:** The "slot" field is strictly temporary. It remains necessary because paid campaigns are still sold by slot until **May 1, 2026**.
    *   *Scenario:* A campaign with a 2-impression cap on Omni Home will be replaced by a house banner once the limit is hit, resulting in sequences like `[1,1,null, null,null,2,null]`.
2.  **Post-Transition:** After May 1, the "slot" field will no longer be used; the system will transition to purely dynamic slots.
3.  **Duplicate Handling (First-Wins):** If a number exists in the field, the system retains only the **first** instance. Subsequent banners with the same slot value are dropped.
    *   *Input Example:* `[null, null, 2, null, null, 1, null, 1]`
    *   *Output Result:* `[null, null, 2, null, null, 1, null]` (The second banner with `slot = 1` is removed).
4.  **Default Behavior:** If the "slot" field is blank or null, the system takes **no action**; the banner remains in the sequence.

**Pending Actions & Ownership**
*   **Action:** Nikhil Grover to verify and implement control logic on the OSMOS side based on the confirmed "blank = no action" and "first-wins duplicate" rules.
    *   **Context:** While Michael raised questions about tracking object positioning, Nikhil confirmed the technical approach is acceptable given the interim strategy. Implementation remains the immediate next step.

**Key Dates & Follow-ups**
*   **Discussion Date:** March 28–29, 2026 (Session concluded with final clarifications on March 29 at 01:14 UTC).
*   **Critical Deadline:** **May 1, 2026**. On this date, the "slot" field logic will be deprecated as the system moves away from slot-based selling.

**Specific References & Context**
*   **System/Platform:** OSMOS.
*   **Data Constraints:** The field may contain numbers (e.g., 999), and sequences often include negatives, zeros, or duplicates during the transition period.
*   **Related Pages:** Omni home, OG Home, FP Pay.
*   **Tracking Logic:** Michael confirmed that while the logic is technically sound, the output sequence reflects the deduplication process (e.g., removing the second occurrence of slot `1`).


## [6/70] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Messages: 8 | Last Activity: 2026-03-29T00:47:23.112000+00:00 | Last Updated: 2026-03-29T02:36:44.362996+00:00
# Daily Work Briefing: #dd-fpg-watchdog-alert

### Key Participants & Roles
*   **Datadog App:** Automated monitoring system.
*   **@hangouts-dd-dpd-watchdog-alert:** Targeted notification channel.
*   *Note: Interactions remain purely automated.*

### Main Topic
The channel tracks **P3 [DPD Watchdog] infrastructure incidents** in Production. Logs show recurring transient issues (excluding `tcp_retrans_jump` and `full_disk_forecast`) aggregated by `story_key`. The alert consistently reads: "Datadog is unable to process your request."

### Incident Summary & Status Update
**Historical Resolved Incidents:**
1.  **Mar 05–17:** 11 distinct events triggered and recovered within the period.
2.  **Mar 18/19:** Incident `story_key`: `10aaf170-dac2-5fec-97bf-cfd442f8706b`. Duration ~5.6 hours. Status: **Resolved**.

**Previously Active Incidents (Now Resolved):**
*   **Mar 20, 2026:** Incident `story_key`: `2787bcd7-d59e-58f0-961a-8f578260cd84`. Duration ~4.4 hours. Status: **Resolved**.
*   **Mar 22, 2026:** Incident `story_key`: `08f5624a-14f1-50e5-9a4a-7418b3602953`. Duration ~3.4 hours. Status: **Resolved**.
*   **Mar 24–25, 2026:** Incident `story_key`: `de0cbb14-ade3-5de2-bfab-cbddd41da779` (~3h 51m). Status: **Resolved**.
*   **Mar 25, 2026:** Incident `story_key`: `978f6328-424c-53dd-83c8-6411c3aa2158`. Recovered at 12:09 UTC. Duration ~24 hours. Status: **Resolved**.
*   **Mar 26, 2026:** Incident `story_key`: `7b73b037-696a-5016-bca4-5c22e31b6245`. Duration ~3 hours 22 minutes. Status: **Resolved**.
*   **Mar 27, 2026:** Incident `story_key`: `f5d0894a-4a42-515d-985f-d06644833529`. Recovered at 17:37 UTC. Status: **Resolved**.

**Current Active/Resolved Sequence (Mar 28–29):**
*   **Incident 1 (Resolved, Mar 28):** Triggered March 28 at 03:26:22 UTC. Story Key: `8874d9ed-c1b1-5d8a-960b-85d280269164`. Recovered at 07:17:22 UTC. Duration ~3h 51m. Status: **[P3] Recovered**.
*   **Incident 2 (Resolved, Mar 29):** Triggered March 28 at 21:27:22 UTC. Story Key: `784f6ec6-03de-5cee-a4e5-9fa93fd78209`. **Recovered** on **March 29, 2026, at 00:47:23 UTC**. Status: **[P3] Recovered**.

### Pending Actions & Ownership
*   **Current Status:** The sequence is currently clear. Incident `784f6ec6...` has self-resolved approximately 3 hours after triggering. No immediate action required pending new triggers.
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Investigation Note:** The recurrence of the "Datadog is unable to process your request" message during the incident window suggests persistent pipeline degradation consistent with historical trends, though the latest event resolved within standard variance.

### Decisions Made
*   **Status:** No escalation triggered for the Mar 28/29 sequence; both incidents self-resolved.
*   **Protocol:** Escalation to SRE/Platform Engineering remains the protocol if a new trigger occurs with similar error messaging and resolution time exceeds 6 hours.

### Key Dates & Follow-ups
*   **Latest Event:** March 29, 2026, at 00:47:23 UTC (Recovery of `784f6ec6...`).
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Continue standard surveillance. The extended duration of the Mar 25 incident (~24h) remains a significant outlier requiring trend analysis alongside current activity.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Datadog Monitor Link:** [View in Datadog](https://app.datadoghq.eu/monitors/17447511)
*   **Latest Incident (Resolved):** https://app.datadoghq.eu/monitors/17447511?group=story_key%3A784f6ec6-03de-5cee-a4e5-9fa93fd78209&from_ts=1774744251000&to_ts=1774745451000&event_id=8564473089519635859

### Monitor Configuration
*   **Query:** `events("source:watchdog (story_category:infrastructure -story_type:(tcp_retrans_jump OR full_disk_forecast)) env:(PROD OR production OR prod)").rollup("count").by("story_key").last("30m") > 0`


## [7/70] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Messages: 3 | Last Activity: 2026-03-29T00:03:09.735000+00:00 | Last Updated: 2026-03-29T02:37:16.337434+00:00
**Daily Work Briefing Summary (Updated: March 29, 2026)**

**Main Topics & Discussions**
1.  **Programmatic Advertising (Advertima/TTD):** Focus remains on validating discrepancies for `advertima_ttd-fixed-price-test-1.5`. Ravi Singh confirmed receipt of raw BURLs; validation was targeted for Monday, March 17th. Yian Koh requested confirmation on deals `advertima_ttd-first-price-test` and `advertima_ttd-fixed-price-test-1`.
2.  **New Deal Setup:** Yasmina Tregan (Advertima) required an end-to-end test setup this week. Wei Phung to share live campaign details; Ravi Singh to execute setup, push to TradeDesk, and map segments before launch.
3.  **BCRS UAT & Finance Integration:** Progress on SAP document numbers, duplicate posting fixes via PubSub "exactly once" policy (PR #1033), and Bukit Timah Plaza pricing/display issues.
4.  **Event Sync Optimization (DPD-645):** Addressing the massive event overage (14M vs. normal 550k). PRD deployment plan set for Sunday, March 15.
5.  **Security & Compliance:** RMN Pentest fixes (DPD-700) deployed to Prod; Bitbucket App Passwords deprecated effective June 9, 2026.

**Status Update: Inbox & Communications**
*   **Inbox Status:** As of March 29, 2026, the workspace inbox is fully caught up across all categories (**Urgent Action Items**, **High-Volume Project Themes**, **Meeting Updates**, and **FYI**). No pending unread items require immediate attention. This status follows confirmations from daily summaries dated March 24 through March 28. The latest update from Workspace Studio confirms zero backlog in all sections, including Code Reviews and Project Updates.

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
*   **June 9, 2026:** Bitbucket App Password deprecation deadline.

**Note on New Content:** The daily summary from March 29, 2026, via Workspace Studio confirms the inbox remains clear of urgent action items across all categories. No changes to pending actions or decisions were required based on this update; historical context regarding project statuses and deadlines remains valid.


## [8/70] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Messages: 16 | Last Activity: 2026-03-28T23:01:22.756000+00:00 | Last Updated: 2026-03-29T02:37:47.927066+00:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
Production instability in the Mirakl integration continues into March 28, now extending to a **12-day streak (March 17–28)**. While midday clusters affected `fni-order-create` earlier today, critical latency issues in `picklist-pregenerator` persist late into the night of March 28, indicating sustained service degradation.

**Incident Summary & Timeline**
*   **Service: `fni-order-create` (Mirakl Integration) – Midday Cluster (Mar 28)**
    *   **Trigger Window:** Simultaneous P2 triggers at **11:32 UTC**.
        *   "Exception Occurred At Mirakl Route" triggered at **11:32:39 UTC** (Monitor ID `17447918`).
        *   "Error while calling API" triggered at **11:32:49 UTC** (Monitor ID `17447928`).
    *   **Recovery:** Monitors returned to normal by **11:37:40/50 UTC**. Duration: ~5 minutes.

*   **Service: `fpon-seller-sap-picklist-reporter` (P1 Incident) – Evening (Mar 27)**
    *   Triggered P1 alert "SAP authentication failed" at **19:12:15 UTC**.
    *   Recovered at **19:17:15 UTC**. Duration: ~5 minutes.

*   **Service: `picklist-pregenerator` (Latency Warning) – Late Evening (Mar 28)**
    *   **New Trigger:** P2 Warning "picklist-pregenerator is taking too long to complete" at **23:01:22 UTC**.
    *   **Metric Value:** **3609.298s** (Monitor ID `20383097`).
    *   **Context:** This confirms sustained performance degradation initially observed on March 27 (3608.98s at 23:01 UTC). The recurrence of values exceeding 3,600 seconds indicates a continuous systemic failure rather than an isolated spike.

*   **Service: `fpon-seller-mirakl-order-creation-alert` (Test Alert) – Evening (Mar 27)**
    *   Monitor `29851723` triggered at **19:15:44 UTC** and recovered at **19:16:45 UTC**. A second test cycle occurred from **19:22:44 UTC** to **20:13:45 UTC**.

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of the midday Mirakl instability affecting `fni-order-create` (Mar 28, 11:32 UTC).
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Analyze underlying causes for the P1 SAP authentication failure on `fpon-seller-sap-picklist-reporter` (Mar 27, 19:12 UTC) to prevent recurrence.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Address the critical latency in `picklist-pregenerator`. A second instance of >3,600s execution time occurred at **23:01:22 UTC** on March 28 (Monitor ID `20383097`). Immediate review required to resolve sustained slowness.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Verify logic for Monitor `29851723` following evening test alerts on March 27; ensure they do not mask production issues.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Summary for Leadership**
Mirakl integration instability has expanded to a **12-day streak (March 17–28)**. On **March 28**, a second cluster occurred at **11:32 UTC** affecting `fni-order-create`, triggering simultaneous "Exception Occurred At Mirakl Route" and "Error while calling API" alerts before recovering by **11:37 UTC**. Crucially, instability persisted late into the day; at **23:01:22 UTC**, the `picklist-pregenerator` service triggered a P2 warning with an execution time of **3609.298s** (Monitor ID `20383097`). This mirrors critical latency peaks from March 27, suggesting a continuous degradation pattern rather than isolated incidents. Combined with the earlier P1 SAP authentication failure on March 27 and the midday Mirakl errors, the system exhibits systemic instability requiring urgent engineering review to stabilize production across the `dpd-fulfilment` and `seller-experience` squads.


## [9/70] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE/fYk6XRzFjAo | Last Activity: 2026-03-28T15:55:03.891000+00:00 | Last Updated: 2026-03-28T22:37:26.809516+00:00
**Daily Work Briefing: Google Chat Summary (Nikhil Grover)**

**Key Participants & Roles**
*   **Nikhil Grover:** Resource/Owner of the operational workflow regarding carousel video approvals.
*   **Michael Bui:** Stakeholder requesting process clarification on ticketing instructions.

**Main Topic**
The discussion centers on **Ops controls approval** for video carousels, specifically addressing how many videos should be included in a final output and how this instruction must be communicated within the project ticket.

**Decisions Made**
*   **Video Count:** Ops controls will ensure that only **one video per carousel** is processed/approved.
*   **Process Requirement:** Tickets must explicitly state whether to drop any videos beyond the first one (2nd video onwards).

**Pending Actions & Owners**
*   **Action:** Ensure all future tickets clearly indicate if the 2nd and subsequent videos should be dropped.
    *   **Owner:** Implementation team/Nikhil Grover (confirmed via "Ok" response to Michael Bui's request).
*   **Action:** Apply the "one video per carousel" rule during ops approval.
    *   **Owner:** Ops controls team (as directed by Nikhil Grover).

**Key Dates & Timeline**
*   **Discussion Date:** March 28, 2026
*   **Timeline of Events:**
    *   15:35 UTC: Initial note regarding the "one video per carousel" rule.
    *   15:45 UTC: Michael Bui requested clear ticketing instructions regarding dropping extra videos.
    *   15:55 UTC: Nikhil Grover acknowledged and accepted the requirement to update ticket clarity.

**Summary of Conversation Flow**
Nikhil Grover initiated the thread by stating that Ops controls will enforce a limit of one video per carousel. Michael Bui immediately followed up (approx. 10 minutes later) to clarify that this decision must be explicitly written in the ticket, specifically asking for confirmation on whether to drop the 2nd video onwards. Nikhil Grover responded approximately 10 minutes after that request, confirming the instruction ("Ok").

**Reference**
*   **Resource:** Nikhil Grover
*   **Chat URL:** https://chat.google.com/dm/t3wf6EAAAAE


## [10/70] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE/AjRV8_d65w4 | Last Activity: 2026-03-28T15:52:39.199000+00:00 | Last Updated: 2026-03-28T22:38:11.036012+00:00
**Daily Work Briefing**
**Resource:** Nikhil Grover | **Date:** March 28, 2026

**Key Participants & Roles**
*   **Nikhil Grover:** Discussant; concerned with ticket ownership and finalizing the production timeline.
*   **Michael Bui:** Developer/Owner of current task; assessing feasibility of handover and weekend work.

**Main Topic**
Discussion regarding resource allocation for a specific development task, feasibility of meeting upcoming deadlines, and confirmation of the Production (PRD) deployment schedule.

**Decisions Made**
*   Michael Bui will retain ownership of the task rather than handing it to another developer due to tight constraints; he confirmed that while another person *could* work on it, they likely could not complete development within the next week.
*   The team agreed to proceed with a timeline targeting Production deployment between April 8 and April 9, pending successful UAT.

**Pending Actions & Ownership**
*   **Nikhil Grover:** Update the ticket tomorrow if answers are comprehensive; confirm alignment on the final PRD date (April 9).
*   **Michael Bui:** Work over the weekend to ensure SIT completion by April 7–8.
*   **Team/All:** Execute UAT immediately following SIT to enable deployment.

**Key Dates & Deadlines**
*   **March 29, 2026 (Tomorrow):** Nikhil Grover updates the ticket.
*   **April 7–8, 2026:** Earliest expected completion of System Integration Testing (SIT).
*   **April 8 or 9, 2026:** Targeted deployment to Production (PRD), contingent on fast UAT.
*   **April 9, 2026:** Confirmed current deadline for Production by Nikhil Grover.

**Context**
Nikhil initially proposed handing the task off if questions were answered comprehensively but pivoted after Michael noted development constraints. Michael committed to weekend work to bridge the gap between SIT and UAT, aiming to meet the April 9 PRD target.


## [11/70] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Last Activity: 2026-03-28T15:35:21.604000+00:00 | Last Updated: 2026-03-28T22:39:03.461378+00:00
**Daily Work Briefing: Nikhil Grover & Michael Bui (Updated)**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator; clarifying technical scope, OSMOS logic, and operational controls. Currently finalizing ticket updates for FE team coordination.
*   **Michael Bui:** Technical Lead (Engineering); identified race condition requiring UAT. Clarified implementation constraints regarding page-specific video support and slot sequencing.

**Main Topics & Technical Clarifications (Mar 28)**
1.  **Scope of Video Support & Page Logic:**
    *   Initial confusion arose regarding whether banner/video changes apply to Category/Search pages. Nikhil confirmed that while the logic change applies to all placements, **video content will only be served on Omni Home and FP Pay**. Other pages (Search, Category) route to the legacy MPS service which does not support video UI rendering.
    *   Michael noted this distinction was critical for his estimation; Nikhil clarified Ops controls approval to ensure one video per carousel, even if advertisers bid with videos.

2.  **OSMOS Logic & Slot Management:**
    *   **Endemic Identification:** Confirmed as a Boolean value ("Endemic" or "Non-endemic").
    *   **PCNT Limits:** OSMOS currently limits `pcnt` to 10; support for values >10 is expected by early April. Nikhil will confirm track on Monday.
    *   **Position/Slot Values:** The `position` field (e.g., -1, 0, 2, 999) is optional and used only to exclude multiple banners targeting the same slot from displaying simultaneously. Values like 999 are acceptable provided uniqueness per slot exists. This logic was previously documented in SOPs.
    *   **Fallback Behavior:** If no banners return or OSMOS API is inaccessible, the system returns nothing (banners collapse). Nikhil noted an incident will be created for API failures; Ops manages fallback scenarios.

3.  **Frontend Implementation:**
    *   Auto-play and auto-scroll logic remain frontend-managed; the backend only defines banner sequence.
    *   Michael requested explicit examples for slot values (-1, 0, 999) to ensure accurate FE updates. Nikhil agreed to clarify OSMOS-side controls in the ticket tomorrow.

**Decisions Made & Status Updates**
*   **Documentation:** Nikhil confirmed that if answers cover all technical queries, he will update ticket DPD-838 tomorrow and coordinate with Alvin for implementation details.
*   **Deployment Readiness:** Michael remains available for urgent evening deployments before his April 6th departure but requires clearer scope confirmation on slot logic to proceed confidently.
*   **Revenue Metrics:** Nikhil is still pending the afternoon update of specific numbers based on `pcnt` drops (originally noted as $1250/day).

**Pending Actions & Owners**
*   **Ticket Updates (Nikhil Grover):** Update DPD-838 with explicit slot value examples and OSMOS logic clarifications; coordinate with Alvin.
*   **Monday Confirmation (Nikhil Grover):** Verify the timeline for OSMOS `pcnt` limit expansion (>10) beyond early April estimates.
*   **Ops Approval (Operations Team):** Ensure strict adherence to one-video-per-carousel limits during campaign approval.

**Key Dates & Deadlines**
*   **March 28, 2026:** Technical scope clarified; Nikhil to update tickets tomorrow; Michael reviews slot logic examples.
*   **April 6–12, 2026:** Michael Bui's leave period (island with limited connectivity).

**Historical Context Note**
The conversation pivoted from parameter gaps to a confirmed technical defect: a race condition identified March 27 preventing `swimlane` and `page_name` rendering. While Nikhil initially cited a $1250/day impact, he clarified this includes the overall drop (excluding S$11.5K lost revenue from advertisers who stopped campaigns on March 17). On Mar 28 afternoon, Michael raised six critical questions regarding video scope, OSMOS logic, and slot sequencing. Nikhil clarified that video is restricted to Omni Home/FP Pay via Ops control, slot values are optional for uniqueness rather than sequencing, and PCNT limits >10 are expected by early April. Documentation updates are scheduled for Mar 29 in coordination with Alvin.


## [12/70] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE/4_UWzOKoxX0 | Last Activity: 2026-03-28T14:44:42.866000+00:00 | Last Updated: 2026-03-28T22:39:20.829035+00:00
**Daily Work Briefing: Google Chat Summary**
**Resource:** Nikhil Grover
**Date:** March 28, 2026
**Participants:** Michael Bui (Sender), Team/Recipient (Implicit)

**1. Key Participants & Roles**
*   **Michael Bui:** Engineer/Product Owner raising technical concerns regarding the video banner implementation and OSMOS integration. Acknowledges being occupied with packing but is actively clarifying scope and logic.

**2. Main Topic**
Clarification of requirements and technical constraints for the new video banner component rollout across Omni Home, OG Home, and FPPay, specifically focusing on:
*   Scope expansion to Category/Search pages (currently routing via the legacy MPS service).
*   Logic definitions for OSMOS integration (Campaign type matching, percentage limits, position tracking).
*   Edge case handling (API failures, auto-play/next logic).

**3. Pending Actions & Owners**
*   **Action:** Document clarifications and logic specifics in the associated ticket to maintain context.
    *   **Owner:** Michael Bui (stated intent: "I commented in the ticket as well").
*   **Action Required by Recipient/Nikhil Grover:** Address specific technical questions raised by Michael:
    1.  Confirm if Category/Search pages require mandatory video support changes or if they remain on the legacy MPS service.
    2.  Define explicit logic for identifying non-endemic banners via the `Campaign type` field (exact vs. substring match).
    3.  Clarify OSMOS support limits for `pcnt` > 10 and define expected handling when the limit is capped at 10.
    4.  Confirm ownership of position tracking values (e.g., `[-1, 0, 1, 2, 2, 5, 999]`)—specifically if OSMOS manages these or if they are passed differently.
    5.  Define logic for auto-play and auto-next scenarios involving multiple videos.
    6.  Establish fallback expectations if no banner is returned by OSMOS or the API becomes inaccessible.

**4. Decisions Made**
*   **Scope Acknowledgement:** Michael noted his initial estimation focused only on Omni Home, OG Home, and FPPay (supporting video). He flagged that Category/Search pages currently route to the old MPS service which does not support video in the UI. The decision on whether to mandate changes for these legacy pages is pending recipient confirmation.
*   **Documentation Strategy:** Michael decided to consolidate detailed clarifications directly into the project ticket rather than continuing the chat thread.

**5. Key Dates & Follow-ups**
*   **Timestamp:** March 28, 2026 (14:39 UTC – 14:44 UTC).
*   **Follow-up:** Immediate response required on the six open technical questions to unblock estimation and implementation planning.
*   **Context Link:** https://chat.google.com/dm/t3wf6EAAAAE


## [13/70] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/jIquLFJEGIc | Last Activity: 2026-03-28T06:25:47.465000+00:00 | Last Updated: 2026-03-28T10:25:55.877133+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Initiator; clarifies scope and coordinates UAT.
*   **Michael Bui:** Developer/Lead; delivered Jobs 1–3 in UAT; managing PRD deployment logistics while on leave.
*   **Wai Ching Chan & Daryl Ng:** Acknowledged contributors for the delivery of Jobs 1–3.
*   **De Wei Tey:** Clarification requester regarding use case scope.

**Main Topic**
Clarification and status update for the "Re-delivery" use case within BCRS, specifically addressing RPA work dependency and UAT sign-off for non-RPA backend logic (Jobs 1–3).

**Pending Actions & Owners**
*   **UAT Sign-off:** Obtain sign-off for Jobs 1–3 (Order service metadata maintenance, Deposit sales posting update, Duplicate suppression).
    *   *Owner:* Prajney Sribhashyam (to coordinate), with support from Michael Bui/Wai Ching Chan.
    *   *Context:* A separate Jira ticket (**DPD-842**) was created to isolate this work from RPA tasks (**DPD-807**).
*   **PRD Deployment:** Execute deployment for the non-RPA logic during late evening or night hours.
    *   *Owner:* Michael Bui (executing remotely due to connectivity constraints).
*   **RPA Grooming Session:** Pending confirmation from Wai Ching Chan and Michael Bui regarding the 'Re-delivery' use case; proposed by Prajney but not yet scheduled in this thread.

**Decisions Made**
*   **Scope Correction:** The team explicitly clarified that Jobs 1–3 relate to the **"Redelivery"** use case, specifically rejecting the suggestion that they address "pre-order and cancellation after delivery" scenarios.
*   **Scope Separation:** The team agreed to proceed with UAT for Jobs 1–3 independently, without dependency on concurrent RPA work.
*   **Deployment Timing:** Michael Bui will handle PRD deployment during off-peak hours (late evening/night) due to upcoming leave and unstable daytime connectivity while on islands.

**Key Dates & Follow-ups**
*   **Date of Conversation:** March 28, 2026.
*   **Next Milestone:** Michael Bui will assist with PRD deployment "next week" (specific timing subject to his connectivity).
*   **Follow-up:** Prajney Sribhashyam committed to providing a status update soon ("Let me give you an update soon").

**Relevant References**
*   **Jira Tickets:** DPD-807 (RPA/General), DPD-842 (Non-RPA UAT).
*   **Chat URL:** https://chat.google.com/space/AAQAgT-LpYY


## [14/70] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/jfuh2YauMzM | Last Activity: 2026-03-28T03:54:16.091000+00:00 | Last Updated: 2026-03-28T10:27:07.620021+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Michael Bui:** Developer responsible for root cause analysis, fix execution, and testing.
*   **Alvin Choo:** Primary recipient querying deployment status; provided flexibility on timing.
*   **Daryl Ng:** Team lead for `website-service`, coordinating code reviews.

**Main Topic**
Resolution of an RMN incident in the `website-service` module, focusing on UAT verification and finalizing the deployment window (Monday evening/night vs. Monday office hours).

**Pending Actions & Ownership**
*   **Regression Testing:** Michael Bui to manually verify that daily morning regression tests show no failures for other functionalities. [Owner: Michael Bui]
*   **Code Review:** Daryl Ng's team to review the PR submitted by Michael Bui. [Owner: Daryl Ng's Team]
*   **Production Deployment (Revised):** Scheduled for Monday evening/night, coordinated with a BCRS change. Alternatively, Alvin Choo has opened the option to deploy during Monday office hours if the team can assist. Final timing pending approval and coordination. [Owner: Michael Bui / Approver: Hui Hui]

**Decisions Made**
*   **UAT Verification Confirmed:** Testing on UAT is complete. The fix corrected the number of requested ads from a degraded value (1) to the correct count (6). Documented in Jira DPD-715 with screenshots.
*   **Risk Assessment:** Michael Bui assessed low risk, noting the root cause is specific to a single race-condition scenario involving one shared variable/object.
*   **Deployment Timing Flexibility:** The team agreed to delay deployment from the weekend (March 27–28) to Monday due to lower urgency compared to Nikhil's request. Alvin Choo confirmed acceptance of "Monday night" but explicitly stated an alternative: the team may deploy during Monday office hours if assistance is available.

**Key Dates & References**
*   **Incident Date/Time:** March 27, 2026 (14:50 UTC).
*   **UAT Confirmation Timestamp:** March 28, 2026 (03:08 UTC) – Michael Bui confirmed UAT success.
*   **New Deployment Discussion Timestamp:** March 28, 2026 (03:54 UTC) – Alvin Choo confirmed flexibility for Monday night or office hours.
*   **PR Link:** https://bitbucket.org/ntuclink/website-service/pull-requests/652/overview
*   **Jira Ticket:** DPD-715 (https://ntuclink.atlassian.net/browse/DPD-715) – Updated with UAT verification and timestamps.
*   **Service Scope:** `website-service`.

**Note on Previous Assumptions**
The previous assumption of a mandatory weekend deployment window has been superseded by the decision to wait until Monday. The specific timing for Monday is now flexible: either evening/night (bundled with BCRS) or during office hours, contingent on team availability.


## [15/70] [BCRS]-SAP to POS & DBP Interface Deployment
Source: gchat | Group: space/AAQAeMC3qBk | Last Activity: 2026-03-28T03:22:30.817000+00:00 | Last Updated: 2026-03-28T03:48:23.615469+00:00
**Daily Work Briefing: [BCRS]-SAP to POS & DBP Interface Deployment**

**Key Participants & Roles**
*   **Onkar Bamane:** Deployment Lead/Coordinator.
*   **Michael Bui:** Deployer (Production OData/SAP).
*   **Hendry Tionardi:** Technical Advisor.
*   **Prajney Sribhashyam:** Process Owner/Test Coordinator (Lead on DBP Testing).
*   **Daryl Ng:** Technical Advisor/Approver.
*   **Others:** Sneha Parab, Wai Ching Chan, Olivia, Kandasamy Magesh.

**Main Topic**
Transition from production deployment execution to post-deployment validation and testing. While the initial deployment was successful on March 26, 2026, active focus has now shifted to validating DBP functionality in Production.

**Decisions Made & Status Update**
1.  **Deployment Execution:** Confirmed that **DBP deployment proceeded first**, followed by SAP OData, as originally planned. Michael Bui successfully deployed to Production (PRD) on March 26, 2026.
2.  **New Testing Phase Initiated:** A dedicated thread titled **"DBP Production Testing"** has been established and is currently active.
    *   Status: The thread contains 3 replies with 3 unread messages as of the last check (approx. 11 minutes ago).
    *   Owner: Prajney Sribhashyam is leading this specific validation effort.
3.  **Risk Mitigation:** The initial validation that deploying DBP first poses no risk regarding BCRS deposit error logs remains valid during this testing phase.

**Pending Actions & Ownership**
*   **DBP Production Validation:** Monitor the "DBP Production Testing" thread for test results and anomalies. *(Owner: Prajney Sribhashyam)*
*   **Update Deployment Steps:** Team members must continue adding specific deployment steps to the shared spreadsheet. *(Owner: Michael Bui, Sneha Parab)*
    *   *Specific Note:* Sneha Parab is requested to update steps specifically regarding **MP Article creation**.
*   **Add Missing PICs:** Identify and add any missing Persons In Charge (PICs) not currently listed in the coordination group. *(Owner: Sneha Parab, Prajney Sribhashyam)*
*   **Redelivery Status:** Discuss the latest status on "redelivery" separately in the working group meeting; do not discuss in this chat. *(Owner: Prajney Sribhashyam)*
*   **Release Coordination:** The condition for an exceptional release is now moot as the standard deployment was completed successfully by Michael Bui.

**Key Dates & Deadlines**
*   **Deployment Window:** Friday, March 26, 2026 (Completed).
*   **Current Activity Date:** Testing updates noted on March 28, 2026.

**References**
*   **Thread: DBP Production Testing:** https://chat.google.com/space/AAQAeMC3qBk (Accessed within the chat space)
*   **Deployment Plan/Tracker (SAP-DBP Deployment Plan):** https://docs.google.com/spreadsheets/d/1gvCjdXWB2BeWr7XgBQs0-zKeLxGi3OmX4ZrbY6pNMeQ/edit?gid=1022676232#gid=1022676232
*   **Chat Space:** https://chat.google.com/space/AAQAeMC3qBk


## [16/70] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/GnLs4UnHRAI | Last Activity: 2026-03-28T03:06:46.472000+00:00 | Last Updated: 2026-03-28T03:49:53.983297+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Alvin Choo:** Requestor of status updates; responsible for disseminating information to stakeholders.
*   **Prajney Sribhashyam:** Subject matter expert providing technical details and coordination support.

**Main Topic**
Discussion regarding recent changes affecting the system, specifically noting concurrent updates observed in the "starship channel." The focus is on consolidating these changes into a comprehensive status update.

**Pending Actions & Ownership**
*   **Action:** Provide an overall update on recent changes to Alvin Choo.
    *   **Owner:** Prajney Sribhashyam (to be confirmed during a call).
*   **Action:** Schedule and conduct a quick call to ensure all necessary details are captured prior to the final update issuance.
    *   **Owner:** Both participants (initiated by Prajney).

**Decisions Made**
*   Prajney Sribhashyam agreed to facilitate a brief synchronous discussion ("quick call") rather than providing text-based details immediately, ensuring no critical information is missed before Alvin releases the status report.

**Key Dates & Follow-ups**
*   **Date of Conversation:** March 28, 2026.
*   **Timeframe:** Early morning (UTC) between 03:04 and 03:06.
*   **Follow-up Required:** Immediate scheduling of a call to finalize the content for Alvin's status update.
*   **Reference Channel:** "starship channel" (mentioned as having parallel updates).

**Resource Metadata**
*   **Group:** BCRS Firefighting Group
*   **Source URL:** https://chat.google.com/space/AAQAgT-LpYY


## [17/70] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY | Last Activity: 2026-03-28T03:04:56.114000+00:00 | Last Updated: 2026-03-28T03:50:15.426830+00:00
**Updated Briefing: BCRS Firefighting Group**
**Date:** March 28, 2026 (Latest activity: ~3:28 AM)
**Source:** Google Chat Space & Shared UAT Tracker (80 messages total)

### **Key Participants & Roles**
*   **Prajney Sribhashyam:** Project Lead/Test Coordinator.
*   **De Wei Tey / Michael Bui / Wai Ching Chan:** Finance/SAP, Re-delivery specialists, and Technical Integration.
*   **Dany Jacob / Eswarlal Rajesh / Sneha Parab:** Active test participants and finance coordinators.
*   **Alvin Choo:** Status reporting lead (monitoring Starship channel updates).

### **Main Topics**
1.  **UAT Readiness & RPA Mobilization:** Prajney Sribhashyam confirmed that Jobs 1 to 3 are ready in UAT as of March 28, pending confirmation on RPA work readiness. The focus has shifted to immediate grooming for the 'Re-delivery' use case (Jira DPD-807).
2.  **Re-delivery Use Case Definition (DPD-807):** A quick grooming session is required today to define workflows for:
    *   Order service maintaining 'Deposit posted to SAP' in metadata.
    *   Deposit sales posting updating this field upon first completion.
    *   Consumption of the field to suppress duplicate BCRS deposit postings.
    *   RPA charging the customer's original payment method and posting BCRS deposit sales.
3.  **Status Reporting:** Alvin Choo requested an overall status update following recent changes noted in the Starship channel, noting visibility for 10 of 39 members.

### **Decisions & Updates**
*   **Schedule Adjustment:** The timeline has shifted from March 26 (Michael Bui's departure/deployment day) to immediate action on March 28 following UAT readiness confirmation. Michael Bui and Wai Ching Chan are explicitly requested for assistance with the Re-delivery case.
*   **Testing Scope:** While previous E2E production testing was targeted for March 26, current priority is validating UAT Jobs 1-3 before proceeding to RPA execution.

### **Pending Actions & Owners**
| Action Item | Owner(s) | Status/Context |
| :--- | :--- | :--- |
| **Re-delivery Grooming Session (DPD-807)** | Prajney Sribhashyam / Michael Bui / Wai Ching Chan / De Wei Tey | **Urgent:** Schedule and execute "quick grooming" today to finalize metadata, sales posting, and RPA workflows. Last reply: 25 min ago. |
| **Overall Status Update** | Prajney Sribhashyam / Team | **Pending:** Provide comprehensive update to Alvin Choo regarding Starship channel changes and UAT progress. |
| **RPA Work Validation** | De Wei Tey / Wai Ching Chan | **Active:** Confirm readiness for RPA execution now that Jobs 1-3 are in UAT. |
| **UAT Job Verification** | Prajney Sribhashyam | **Completed:** Jobs 1 to 3 confirmed ready in UAT (March 28). |

### **Key Dates & Deadlines**
*   **March 28 (Today):** Target for Re-delivery grooming session and RPA readiness confirmation.
*   **Historical Deadline Note:** The original SAP Deposit API development deadline of Feb 20 remains noted as missed/risked; current focus is on resolving the specific re-delivery logic gaps.

### **Historical Context Retained**
*   Existing e-comm test accounts remain unusable for Pre-order staff app; new BCRS CF items and specific GWP SKUs required.
*   Deposit SKU linking investigation continues due to failure to link post-publishing.
*   Re-delivery flow testing previously experienced audio issues on March 16; current effort aims to resolve logic gaps via the grooming session.


## [18/70] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE/owFZqxoK4p8 | Last Activity: 2026-03-28T02:42:04.629000+00:00 | Last Updated: 2026-03-28T03:50:30.120558+00:00
**Daily Work Briefing**
**Resource:** Nikhil Grover
**Date Range:** March 27–28, 2026

**Key Participants & Roles**
*   **Nikhil Grover:** Lead/Stakeholder (Focus: Impact assessment, user story documentation for new app).
*   **Michael Bui:** Technical/Engineering (Focus: Root cause analysis of detection failure, proposed testing infrastructure fixes).

**Main Topic**
Discussion regarding a delayed detection of a system issue causing a financial impact of approximately **$1250 per day**. The conversation addresses why the issue was missed during previous testing phases and outlines necessary changes to the testing strategy in **Osmos** to prevent recurrence.

**Root Cause Analysis (Michael Bui)**
The issue could not be spotted earlier because it requires **multiple concurrent requests** to manifest. Current unit and E2E tests focus on individual requests, which typically ensure at least one ad is present, masking the logic degradation that occurs over time when multiple requests interact.

Previously, testing relied on hard-coded campaigns in Osmos covering multiple ad positions. However, these products went out of stock (OOS), and subsequent campaign changes caused missing ads in specific positions. To avoid false alarms, test scope was reduced to merely checking for the *presence* of an ad, which failed to detect this concurrency issue.

**Decisions Made**
No final decision on a deadline or immediate timeline was recorded. However, Michael Bui proposed two critical requirements to reliably catch these issues:
1.  Establish a campaign in Osmos that is **immutable**, stocked with abundant inventory intended to last indefinitely (virtually), eliminating OOS scenarios.
2.  Implement a specific process in Osmos to prevent this campaign from being modified or competed against by other campaigns.

**Pending Actions & Owners**
*   **Nikhil Grover:** Writing user stories for the new application to clarify requirements if needed; asked why the issue was not spotted earlier.
*   **Michael Bui (Action Required):** Implement the proposed immutable campaign strategy and process controls in Osmos to ensure reliable detection of multi-request issues.

**Key Dates & Follow-ups**
*   **2026-03-27 22:21 UTC:** Nikhil Grover noted the $1250/day impact and questioned Monday's availability.
*   **2026-03-28 02:37 UTC:** Michael Bui explained the technical difficulty of detection due to test scope limitations.
*   **2026-03-28 02:42 UTC:** Michael Bui detailed the historical context of OOS campaigns and proposed the fixed campaign solution.

**Urgency Note**
Nikhil Grover emphasized that "earlier we fix, the better" given the daily financial impact.


## [19/70] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/gZNwhpEiEY4 | Last Activity: 2026-03-28T02:23:26.710000+00:00 | Last Updated: 2026-03-28T02:35:26.007087+00:00
**Daily Work Briefing: Digital Product Development (Leads)**
**Resource:** [Leads] (Ecom/Omni) Digital Product Development
**Metadata:** { "message_count": 17, "url": "https://chat.google.com/space/AAQAN8mDauE" }
**Date of Discussion:** March 26–28, 2026

### **Key Participants & Roles**
*   **Daryl Ng:** Project Lead; confirmed changes are live in UAT.
*   **Michael Bui:** Developer for the BCRS deposit posting job; confirmed SIT success and verified functionality with a re-delivered order on March 28. Manages pipeline deployment coordination.
*   **Wai Ching:** Created necessary order custom field during UAT (March 26).
*   **Adrian:** Restricted from redelivery work between April 1–7 due to duplicate posting risks.
*   **Sneha Parab:** Validated discussion relevance against ticket DPD-807 on March 27.

### **Main Topic**
The discussion confirmed the successful completion of SIT for the BCRS deposit posting job. Michael Bui created new Jira ticket **DPD-842** to track this specific task, noting that the original **DPD-807** is now assigned to the RPA team. On March 28, Michael confirmed that changes are already in **UAT** and verified success by testing with a re-delivered order. The focus has shifted to initiating UAT for suppressing BCRS deposit posting in redelivery scenarios and finalizing PRD deployment via Bitbucket pipelines.

### **Decisions Made**
1.  **Ticket Reassignment:** Work tracked under DPD-807 is moved to **DPD-842** for the RPA team; current PR (PR #7) requires immediate review.
2.  **UAT Status:** Changes are confirmed live in UAT and verified via re-delivered order testing. Formal UAT kick-off for suppressing BCRS deposits in redelivery scenarios is pending final approval following PR merge.
3.  **Deployment Strategy:** A Bitbucket Pipeline (similar to result #67) is available to deploy master branch changes to PRD upon PR merge. If not urgent, deployment can be scheduled for next week during night hours due to Michael's daytime unavailability.

### **Pending Actions & Owners**
*   **PR Review:** Daryl Ng to review Pull Request #7: `https://bitbucket.org/ntuclink/bcrs-deposit-posting/pull-requests/7`.
*   **UAT Kick-off:** Team to formally start UAT for suppressing BCRS deposit posting in redelivery scenarios immediately after PR merge.
*   **PRD Pipeline Deployment:** Michael Bui to execute Bitbucket pipeline deployment to PRD (master branch) either urgently post-merge or next week at night, depending on urgency assessment by Daryl.

### **Key Dates & Deadlines**
*   **March 28, 2026 (02:23 UTC):** Michael Bui confirmed changes are in UAT and verified with a re-delivered order.
*   **Immediate:** PR #7 review required upon merge to proceed with deployment.
*   **Next Week (Night Time):** Fallback window for PRD deployment if not urgent.
*   **April 1 – April 7, 2026:** Critical window where Adrian must refrain from redelivery to prevent duplicate postings; SIT is concluded before this period begins.

**Reference Links:**
*   **New Ticket (SIT Tracking):** https://ntuclink.atlassian.net/browse/DPD-842
*   **Old Ticket (RPA Assignment):** https://ntuclink.atlassian.net/browse/DPD-807
*   **PR to Review:** https://bitbucket.org/ntuclink/bcrs-deposit-posting/pull-requests/7
*   **Example Pipeline:** https://bitbucket.org/ntuclink/bcrs-deposit-posting/pipelines/results/67


## [20/70] [Prod Support] Ecom FFS Ops
Source: gchat | Group: space/AAAAde_cYKA | Last Activity: 2026-03-28T01:45:21.232000+00:00 | Last Updated: 2026-03-28T02:35:54.742047+00:00
**Daily Work Briefing: [Prod Support] Ecom FFS Ops (Updated Mar 28)**

**Key Participants & Roles**
*   **Wai Ching Chan / Sampada Shukla:** Operations/Product Leads.
*   **TL HCBP FFS:** Store Lead reporting T18/T19 picking queue blockages and scan issues.
*   **Adrian Yap Chye Soon:** Technical Lead/Support (investigating data anomalies and dispatcher app failures).
*   **Akash Gupta:** DPD / Fulfilment / On Call.
*   **Yoongyoong Tan:** Reporting HCBP picking Q issues.
*   **Ler Whye Ling Angel:** Escalation point for "No picking Q."

**Main Topics**
1.  **Packlist Discrepancies & Validation:** Ongoing investigation into critical `packed_qty` anomalies (NULL values or massive mismatches vs. `delivered_qty`).
    *   **Critical Incident (Mar 26):** Akash Gupta identified two orders at **VivoCity (Store ID 170)** showing `packed_qty` > 13M against `delivered_qty` of <20.
        *   Order #22912255: `packed_qty` 13,165,999 vs. `delivered_qty` 12.
        *   Order #22906879: `packed_qty` 13,165,999 vs. `delivered_qty` 18.
    *   **Historical Context:** Incidents include Mar 25 Sun Plaza (Order #22898981) and prior anomalies at Hyper Sports Hub.

2.  **Dispatcher App & Zone Scanning Failure (Mar 28):** New escalation regarding the dispatcher app's inability to scan new zones.
    *   **01:45 AM Mar 28:** Adrian Yap Chye Soon reported that the dispatcher app is unable to scan the new zone at **hvivo** (High Vivo/Healthcare VivoCity context). A video demonstration was provided for review.

3.  **HCBP Picking Queue Issues (Mar 27):** Escalated urgency regarding "No picking Q" blockage and T18 display failures.
    *   **Timeline:** Initial blockage reported 02:08 AM; escalated by Ler Whye Ling Angel at 02:52 AM; T18 data failure reported by TL HCBP FFS at 07:47 AM with follow-up at 07:53 AM.

**Pending Actions & Ownership**
*   **Dispatcher App Investigation (Urgent - Mar 28):**
    *   *@Adrian Yap Chye Soon / Technical Team:* Investigate the "unable to scan new zone" failure at hvivo based on the video evidence provided by Adrian.
    *   *@Wai Ching Chan @Sampada Shukla:* Review the uploaded video and coordinate resolution for the dispatcher app issue.
*   **Critical Data Validation (Mar 26):**
    *   *@Akash Gupta / On Call:* Confirm massive `packed_qty` mismatches for Orders #22912255 and #22906879 at VivoCity. Sun Plaza validation remains pending.
*   **HCBP Queue Investigation (Mar 27):**
    *   *@Adrian Yap Chye Soon / @Gopalakrishna Dhulipati:* Continue monitoring the resolution of Mar 27 "No picking Q" and T18 display failures following escalated pings from Ler Whye Ling Angel and TL HCBP FFS.

**Decisions Made**
*   **App Release Strategy:** Picker App 10.4.0 rollout remains on hold pending resolution of critical data anomalies (Mar 18–27). Full rollout is contingent on stability post-fixes, specifically addressing the Mar 26 VivoCity alerts, the resolved Mar 27 HCBP queue/T18 failures, and the **new dispatcher app zone scanning issue at hvivo**.

**Key Dates & Deadlines**
*   **Immediate:** Validation of Mar 26 Orders #22912255/#22906879; Root cause analysis of Mar 28 Dispatcher App failure at hvivo.
*   **Pending:** RCA for recent `packed_qty` anomalies across Sports Hub, VivoCity, Parkway, Changi, Sun Plaza, Hyper VivoCity.

**Critical Alerts**
*   **Active Alert (Mar 28):** Dispatcher app unable to scan new zone at **hvivo**. Video evidence available; requires immediate technical check by @Adrian Yap Chye Soon and Ops leads.
*   **Secondary Active Alert (Mar 27):** HCBP "No picking Q" issue escalated by Ler Whye Ling Angel.
*   **Tertiary Active Alert (Mar 26):** Two orders at VivoCity showing `packed_qty` (~13M) >> `delivered_qty`.


## [21/70] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/z2zSDKRl4Vc | Last Activity: 2026-03-28T00:08:06.077000+00:00 | Last Updated: 2026-03-28T02:36:43.651556+00:00
**Daily Work Briefing: [Internal] (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Michael Bui:** Initiator/Requester (Submitted PR review request).
*   **Daryl Ng:** Review Lead/Scheduler (Requested peer reviews for upcoming work).
*   **Yangyu Wang, Lester Santiago Soriano, Sundy Yaputra, Zaw Myo Htet, Chee Hoe Leong:** Assigned reviewers.

**Main Topic/Discussion**
The conversation focuses on code review requirements for a specific Pull Request (PR) regarding the suppression of BCRS deposit posting within the re-delivery journey. Additionally, Daryl Ng initiated a schedule for peer reviews concerning work planned for the following week.

**Pending Actions & Ownership**
*   **Action:** Review PR #7 at `https://bitbucket.org/ntuclink/bcrs-deposit-posting/pull-requests/7` to suppress BCRS deposit posting in the re-delivery journey.
    *   **Owner:** @Daryl Ng (Explicitly requested by Michael Bui).
*   **Action:** Assist with upcoming review tasks for next week's deliverables.
    *   **Owners:** @Yangyu Wang, @Lester Santiago Soriano, @Sundy Yaputra, @Zaw Myo Htet, @Chee Hoe Leong (Assigned by Daryl Ng).

**Decisions Made**
*   No formal technical decisions or approvals were recorded in this snippet. The thread consists of a direct request for review and an administrative instruction to assign reviewers.

**Key Dates & Follow-ups**
*   **Initiation Date:** March 27, 2026 (19:33 UTC) – Michael Bui posted the PR link.
*   **Assignment Date:** March 28, 2026 (00:08 UTC) – Daryl Ng expanded the review list.
*   **Upcoming Deadline/Focus:** "Next week" – The specific tasks assigned to the five reviewers are targeted for this upcoming period.

**References**
*   **PR Link:** `https://bitbucket.org/ntuclink/bcrs-deposit-posting/pull-requests/7`
*   **Space URL:** `https://chat.google.com/space/AAQAUbi9szY`


## [22/70] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/rKtZEQsyOFI | Last Activity: 2026-03-27T20:20:12.120000+00:00 | Last Updated: 2026-03-27T22:37:56.202521+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Michael Bui:** Lead developer/technical contact; created initial Confluence documentation for RMN integration.
*   **Alvin Choo:** Decision maker (likely Technical Lead or Manager); requested draft prior to leave.
*   **Gopalakrishna Dhulipati:** Tagged participant (no direct action in this thread).

**Main Topic**
Coordination with the CoMall team regarding "Project Light Attack and Defence" kick-off, focusing on contract status, engagement timing, and finalizing Technical API Specifications (Tech Spec) for RMN pieces.

**Decisions Made**
1.  **Engagement Timing:** Do not connect with the CoMall team or create a Google Chat space immediately; wait until the official kick-off/grooming next week as they are not yet awarded.
2.  **Documentation Platform:** Use Confluence for API specifications (confirmed implemented).
3.  **Template Approach:** Initial drafts created immediately to ensure consistency across Payments, FP Pay, and Identity teams. Perfection is not required; content can be refined later.

**New Developments & Status Updates**
*   **Draft Completion:** Michael Bui has successfully created two Confluence documents today (March 27, 2026), fulfilling the request to draft before his upcoming leave.
    *   **Display (Banner/Video) Ads:** Documented as currently supported with minimal changes required for Project LIGHT.
        *   *Link:* https://ntuclink.atlassian.net/wiki/spaces/LIGHT/pages/3346989110/Finalizing+Display+Ads+Banner+Video
    *   **Dynamic Ads in PLP Content Cards:** Documented as not currently available; requires development for Project LIGHT.
        *   *Link:* https://ntuclink.atlassian.net/wiki/spaces/LIGHT/pages/3347120197/Draft+Dynamic+Ads+in+the+PLP+Content+Card
*   **Next Step:** Awaiting Alvin Choo's review of the document layout and content.

**Pending Actions & Ownership**
*   **Review Draft:** Alvin Choo to review the two new Confluence documents for format and content accuracy.
*   **CoMall Alignment:** Prepare standardization discussion for Payments, FP Pay, and Identity teams during next week's kick-off.

**Key Dates & Deadlines**
*   **Today (March 27, 2026):** Michael Bui completed Confluence draft templates.
*   **Next Week:** Scheduled kick-off/grooming session with CoMall.
*   **Upcoming:** Michael Bui is on leave soon; immediate drafting action has been prioritized and executed.

**Specific References**
*   Contract status: Unconfirmed/Awaited award.
*   Services involved: Payments, FP Pay, Identity.
*   Document format: Confluence draft (exportable to PDF if CoMall lacks access).
*   RMN Integration Scope: Display Ads (supported) and Dynamic Ads in PLP Content Cards (requires dev).


## [23/70] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Last Activity: 2026-03-27T19:33:53.868000+00:00 | Last Updated: 2026-03-27T22:39:14.506022+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Key Participants & Roles**
*   **Sneha Parab:** BCRS/Fees/Store Closure Impact Lead.
*   **Daryl Ng:** Backoffice/Order Management/Bug Reporting / Slot Logic validation.
*   **Michael Bui:** BCRS Deposit Logic/SAP Integration/Publisher of PRs.
*   **Wai Ching Chan:** Order Service Deployment/Slot Logic Validation.
*   **Andin Eswarlal Rajesh:** Frontend (iOS/Android) & BCRS UX queries / Amplitude tracking.
*   **Lester Santiago Soriano:** Backend Services Lead.
*   **Zaw Myo Htet:** Payment/Feature Flagging.
*   **Shiva Kumar Yalagunda Bas:** Slot discrepancy reporting.
*   **Gopalakrishna Dhulipati & Dang Hung Cuong:** Address emoji validation (New assignees).
*   **Akash Gupta:** IMS availability/UAT stock sourcing.

**Main Topics Discussed**
1.  **BCRS Epic Closure Urgency:** Sneha Parab flagged that the BCRS epic remains open with tickets in "Define" state, necessitating immediate status clarification to close the epic. Specific tickets identified: **DPD-637** and **DPD-807**. Inputs requested from Akash Gupta, Michael Bui, and Andin Eswarlal Rajesh (Mar 27).
2.  **BCRS Deposit Logic Update:** On Mar 27 at 19:33, Michael Bui published PR #7 (`bcrs-deposit-posting`) to suppress deposit posting during the re-delivery journey. Daryl Ng has been tagged for immediate code review. This action supports the critical duplicate deposit fixing efforts.
3.  **iOS Address Emoji Blocking Bug:** Wai Ching Chan reported on Mar 26 that customer addresses with emojis on iOS cause order time slot failures, requiring manual resolution (Customer ID: 2022036). Validation logic is required during address add/edit.
4.  **Website SDK Deployment (Strudel):** Lester deployed `go-platform-website` on Mar 19 to update the Strudel SDK for maximum voucher validation. Review via Bitbucket diff between v1.5.11 and v1.5.10 completed.
5.  **Pre-order Payment Logic & UAT:** Zaw initiated an inquiry on Mar 24 regarding pre-order flows (app payment vs. POS redemption) and requested peer review for the offline pre-order admin page (`https://admin-uat.fairprice.com.sg/in-store-preorder/offline`).
6.  **Slot Date Discrepancy:** Shiva reported a delivery slot mismatch (UI shows 25th, API indicates 23rd). Daryl Ng and Sundy Yaputra are resolving this.
7.  **UAT Stock Requirements:** Sneha requested high-stock SKUs for Zi Ying's bulk order testing; Wai Ching Chan and Akash Gupta tasked to check IMS availability.
8.  **Order Verification Bug (NED-278216):** Investigation continues into the Whitelisting API returning older contract data (identified by Andin).

**Pending Actions & Ownership**
*   **Daryl Ng:** Review Michael Bui's PR #7 to suppress BCRS deposit posting in the re-delivery journey.
*   **Akash Gupta, Michael Bui, Andin Eswarlal Rajesh:** Provide immediate inputs on the status of BCRS tickets **DPD-637** and **DPD-807** to facilitate epic closure (Sneha Parab).
*   **Wai Ching Chan, Gopalakrishna Dhulipati, Dang Hung Cuong:** Validate and implement emoji blocking logic for iOS address entry/editing to prevent order slot failures. Reference Customer ID: 2022036.
*   **Zaw Myo Htet:** Clarify pre-order payment redemption logic; execute UAT testing on offboarded Pinelabs split feature flag.
*   **Lester Santiago Soriano:** Assist with Whitelisting API contract issue (cc: Piraba Nagkeeran, Jonathan Tanudjaja). Deployment completed Mar 19.
*   **Daryl Ng & Sundy Yaputra:** Resolve delivery slot date mismatch (UI showing 25th vs API 23rd).
*   **All Engineers:** Mark all tickets deployed to production as "Status = Done." Highlight any pending deployments immediately (Sneha Parab).

**Decisions Made**
*   **BCRS Epic Priority:** Immediate action required to close the BCRS epic; ticket status must be verified for DPD-637 and DPD-807.
*   **Deposit Logic Fix:** Focus shifted to PR #7 review to suppress deposit posting in re-delivery flows, addressing critical duplicate posting risks.
*   **Status Protocol:** All engineers must update Jira ticket status to "Done" upon production deployment; pending items must be flagged in the chat thread.
*   **Deployment Approval:** PLU processor deployment approved pending UD alignment.
*   **Code Review Priority:** Focus remains on `go-platform-website` PR #1538 for Strudel SDK update, alongside the new BCRS deposit PR review and iOS emoji validation logic.

**Key Dates & Deadlines**
*   **Mar 27, 2026 (Today):** Sneha Parab initiated inquiry on BCRS epic closure; Michael Bui requested PR #7 review for deposit suppression. Responses required from Akash Gupta, Michael Bui, Andin Eswarlal Rajesh, and Daryl Ng.
*   **Mar 19, 2026:** Website deployment completed at 4:00 PM; UAT stock sourcing required immediately.
*   **Mar 24, 2026:** Zaw Myo Htet initiated inquiry regarding the offline pre-order admin page and pre-order payment logic.
*   **Mar 31, 2026:** Sports Hub FFS store closure deadline.

**Note on Historical Context:** Previous mentions of code review priorities for `layout-service` PR #362 and `website-service` PR #649 are superseded by the urgent Strudel SDK deployment update. The current focus includes reviewing the BCRS deposit suppression logic (PR #7), resolving slot date mismatches, pre-order payment logic queries, the iOS address emoji blocking issue, and closing the BCRS epic via tickets DPD-637 and DPD-807.


## [24/70] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Last Activity: 2026-03-27T14:50:23.456000+00:00 | Last Updated: 2026-03-27T22:40:29.012704+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Sneha Parab:** Lead/Manager; coordinating cross-team support, SAP/API integration blockers.
*   **Michael Bui:** Engineering/RMN Architect; identified root cause for the RMN incident and preparing UAT verification.
*   **Alvin Choo:** Leadership; addressing approval workflows for weekend deployments and release schedules.
*   **Daryl Ng:** Investigating store network ownership, Omni Home data discrepancies (currently away).
*   **Others Active:** Andin Eswarlal Rajesh, Olivia, Koklin, Zaw, Ravi.

**Main Topics & Updates**
1.  **RMN Incident Resolution:** Michael Bui identified the root cause for the RMN incident and is implementing a fix pending UAT verification. Immediate guidance is required on deployment protocols: if deploying over the weekend (Sat/Sun), the process involves sending an approval request to Hui Hui.
2.  **Search Performance Drop:** Investigation continues regarding the severe 60–70% impression decline since March 18/19. The RMN root cause fix may correlate with these symptoms; release timing remains contingent on this investigation and UAT success.
3.  **Epic Lifecycle Query (DPD-710):** Sneha Parab flagged a technical live date of March 19, 2026, for the Omni ticket. With Daryl Ng away, closure validation awaits Michael Bui's input on whether the epic is safe to close immediately.
4.  **SIT Timeline & Redelivery Risk:** Discussion continues on SIT delivery feasibility before April 6/7 contingent on Knowledge Transfer (KT). Adrian remains unavailable for redeliveries between April 1–7 due to duplicate posting risks without a completed handover.
5.  **Infrastructure Compliance:** Bitnami ending free Docker images mandates migration for `sonic_raptor` and `mkp-fairnex`.

**Pending Actions & Owners**
*   **RMN Deployment Approval:** Confirm weekend deployment process (send approval request to Hui Hui) following UAT verification of the fix. (Owner: Michael Bui; Coordination: Alvin Choo/Hui Hui)
*   **Epic Closure Validation:** Determine if DPD-710 can be closed given the March 19 live date discrepancy. (Owner: Michael Bui; Requestor: Sneha Parab)
*   **SIT Delivery Assessment:** Evaluate KT feasibility to complete SIT before April 6/7. (Owners: Michael Bui/Daryl Ng)
*   **Store Network Ownership:** Confirm scope under Data COE vs. Miguel's team regarding `Omni Home` store ID mismatch (OMNI-1157). (Owner: Daryl Ng/Michael Bui)
*   **SAP Timeline Resolution:** Resolve deposit SKU data integration blockers. (Owners: Sneha Parab/Alvin Choo/Gopalakrishna Dhulipati)
*   **RAW Forms Review:** Complete Risk Register review for DPD RAW forms; confirm handovers and renew expired forms by Tomorrow EOD. (Owner: All Leads/Sazali Bin Mohammed Ali's team)

**Decisions Made & Status Changes**
*   **RMN Fix Status:** Root cause identified; moving to UAT verification. Deployment timing (weekend vs. weekday) is currently being debated.
*   **Release Strategy:** Regular app release status remains pending the search performance investigation and RMN fix validation.
*   **Architecture Updates:** Michael Bui has updated current, future, and transition architecture diagrams.

**Key Dates & Deadlines**
*   **RAW Forms Review:** Due Tomorrow EOD.
*   **Adrian Redelivery Block:** Unavailable Apr 1–7 due to duplicate posting risks.
*   **SIT Target:** Potential delivery by April 6/7 contingent on KT success.
*   **Chee Hoe Support:** Effective end of March for Product Catalogue/MarTech scope.
*   **DPD-710 Live Date:** March 19, 2026 (Subject to validation).


## [25/70] #dpd-dba
Source: gchat | Group: space/AAAAMh7T8Y0 | Last Activity: 2026-03-27T12:55:22.022000+00:00 | Last Updated: 2026-03-27T14:35:13.606526+00:00
**Daily Work Briefing: #dpd-dba**

**Key Participants & Roles**
*   **Akash Gupta:** DBA Team Representative/Requestor.
*   **Wai Ching Chan:** Deployment Coordinator (Service Owner).
*   **Tiong Siong Tee:** Communication Initiator.
*   **Maou Sheng Lee:** Advisor (Requested owner involvement).
*   **Gopalakrishna Dhulipati:** Primary DBA Contact (Active on recent urgent tickets).
*   **Sampada Shukla, Hanafi Yakub, Dodla Gopi Krishna, Alvin Choo, Natalya Kosenko, Lester Santiago Soriano, Borja Adrian Dominguez:** DBA Team/Stakeholders.

**Main Topic**
The conversation focuses on executing multiple urgent Jira service tickets for production and pre-production database updates, including critical patches for order zone IDs and a new insertion request for pork product picking zones. Additionally, the team is investigating GKE Autopilot scale-down incidents impacting SLOs.

**Pending Actions & Owners**
*   **Execute DSD-11003 Ticket:**
    *   **Action:** Add `container_deposit` column to `order_service.order_items`.
    *   **Owner:** DBA Team (Akash Gupta).
    *   **Status:** Pending execution if not completed. Initial request made Mar 6; replies received from Sampada Shukla and Hanafi Yakub.
*   **Execute DSD-11124 Ticket (NEW):**
    *   **Action:** Insert new picking zone ("Pork products") into the picking service table for both Prod and Pre-prod environments.
    *   **Owner:** DBA Team (specifically tagged to @Gopalakrishna Dhulipati).
    *   **Status:** **APPROVED**. Submitted by Wai Ching Chan on Mar 27 at 12:55 UTC. Requires immediate execution.
*   **Approve URGENT Patch DSD-11122:**
    *   **Action:** Patch `orders` zone ID for non-COMPLETED/CANCELLED statuses.
    *   **Owner:** DBA Team (Requested by Wai Ching Chan, Mar 27 at 08:14 UTC). Tags @Gopalakrishna Dhulipati, @Alvin Choo, @Natalya Kosenko, @Akash Gupta.
    *   **Status:** Requires immediate approval.
*   **Approve URGENT Patch DSD-11119:**
    *   **Action:** Review and approve urgent patch for `orders` zone ID (general statuses).
    *   **Owner:** DBA Team (Requested by Wai Ching Chan, Mar 27 at 04:06 UTC). Tags @Gopalakrishna Dhulipati, @Alvin Choo, @Natalya Kosenko.
    *   **Status:** Requires owner approval and consultation with the DB owner per Maou Sheng Lee's guidance.
*   **Support Production Deployment & Monitoring:**
    *   **Action:** Standby for `order-service` deployment monitoring on `fpon`.
    *   **Owner:** Akash Gupta, Gopalakrishna Dhulipati.
    *   **Status:** Requested Mar 9; script details provided.
*   **Investigate SLO Impact & Proxy Scale-Down:**
    *   **Action:** Investigate "bad connection" errors caused by `sqlproxy-prod-ap` GKE Autopilot scale-downs.
    *   **Owner:** @Gopalakrishna Dhulipati, @Dodla Gopi Krishna.
    *   **Status:** Reported Mar 25; identified as critical SLO risk.

**Decisions Made**
*   `container_deposit` column (JSON, NULL default) to be added via transaction (`BEGIN...COMMIT`) for ticket DSD-11003.
*   Ticket DSD-11124 is **approved** and ready for execution in Prod and Pre-prod.
*   Future requests must explicitly name the specific DB owner (per Maou Sheng Lee).

**Key Dates & Updates**
*   **Mar 6, 2026 (01:48 UTC):** Initial request for DSD-11003.
*   **Mar 9, 2026 (04:36 UTC):** Deployment window scheduled for 11:00 PM; script shared.
*   **Mar 25, 2026 (05:52 UTC):** SLO impact report regarding GKE scale-downs.
*   **Mar 27, 2026 (03:12 UTC):** Advice to include DB owners in requests.
*   **Mar 27, 2026 (04:06 UTC):** Urgent ticket DSD-11119 submitted.
*   **Mar 27, 2026 (08:14 UTC):** Urgent ticket DSD-11122 submitted.
*   **Mar 27, 2026 (12:55 UTC):** **New:** Wai Ching Chan submits approved urgent ticket **DSD-11124** for "Pork products" insertion; @Gopalakrishna Dhulipati tagged.

**References**
*   **Jira Tickets:** `DSD-11003`, `DSD-11119` (Urgent), `DSD-11122` (Urgent), **New: `DSD-11124`** (Pork products, Approved).
*   **Database:** `fpon.order_service.order_items`, Picking service tables (Prod/Pre-prod).
*   **Affected Cluster:** `sqlproxy-prod-ap` (GKE Autopilot).


## [26/70] [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Last Activity: 2026-03-27T11:29:59.041000+00:00 | Last Updated: 2026-03-27T14:35:43.145971+00:00
**Daily Work Briefing: [Prod Support] Marketplace**

**Key Participants & Roles**
*   **Support/Operations:** Willie Tan, Iris Chang, Lalita Phichagonakasit, Charlene Tan, Jie Yi Tan, Ayton See, Amos Lam, Michelle Lim.
*   **Technical/Admin Team:** Dang Hung Cuong, Shiva Kumar Yalagunda Bas (Frequent recipients of access/access issues), Olivia -, Jill Ong, Greta Lee, Zaw Myo Htet, Angella Yeo, Cassandra Thoi, Gopalakrishna Dhulipati, Ee Ling Tan.

**Main Topics & Discussion Summary**
Discussions continue to focus on operational blockers regarding seller onboarding, order fulfillment discrepancies, system configuration errors, and data visibility gaps. Major themes include:
1.  **Data Visibility Gap:** Greta Lee (Mar 27, 08:51 UTC) requested live dashboards for daily MP ordered quantities for specific SKUs, citing a discrepancy between the current forecast cutoff (4 AM) and real-time high run-rate volume. She tagged Dang Hung Cuong, Shiva Kumar Yalagunda Bas, and Amos Lam.
2.  **PickerApp Barcode Errors:** Dang Hung Cuong is investigating a truncation issue for Pureen (SAP: 90247763), where the system displays `95561234717` instead of `9556123471735`. Greta Lee also flagged SKU 90244060 for Yumsay Foods as non-existent.
3.  **Access Management:** Amos Lam (Mar 27, 10:00 UTC) requested PickerApp access linkage for Seller ID 31435 (Nathalie Huang, nathalie.huang@alphico.com.sg), code `69c621405ddaee7f20b504ea`. **Status Update:** Shiva Kumar Yalagunda Bas confirmed completion of this request at 11:29 UTC on Mar 27.

**Pending Actions & Ownership**
*   **Live Dashboard Request:** Technical team to provide or configure a live dashboard for daily MP ordered quantities to bridge the 4 AM–current time gap (Greta Lee, Mar 27).
*   **Truncated Barcode Investigation:** Dang Hung Cuong to investigate Pureen's barcode truncation issue.
*   **PickerApp SKU Error:** Technical team to investigate why SKU 90244060 for Yumsay Foods is flagged as non-existent.
*   **Urgent Promotion Removal:** Dang Hung Cuong and Gopalakrishna Dhulipati to remove incorrectly set up promotion for Item ID: 90244361 (Lalita Phichagonakasit, Mar 20).
*   **Picklist Verification:** Dang Hung Cuong to confirm picklist delivery status for Sinhua Hock Kee Order #257719344.
*   **Order Status Investigation:** Team to check discrepancies for Order #256055476 and Order #248407866.
*   **Vendor Report Issues:** Investigate missing sales breakdown reports for CoLab Apac (NED-277148) and Old Shanghai (NED-277329).

**Decisions Made**
*   Dang Hung Cuong is prioritizing the removal of Item ID: 90244361, the new picklist failure issue raised by Amos Lam, the Woah Group offers error, and the current barcode truncation investigation for Pureen.
*   Dang Hung Cuong and Shiva Kumar Yalagunda Bas are assigned to investigate the vendor picklist anomaly.
*   **Completed:** Access linkage for Seller ID 31435 (Nathalie Huang) has been successfully executed by Shiva Kumar Yalagunda Bas on Mar 27, 11:29 UTC.

**Key Dates & Deadlines**
*   **2026-03-27 (Today):** Greta Lee reported data visibility gap; Dang Hung Cuong, Shiva Kumar Yalagunda Bas, and Amos Lam tagged. Amos Lam requested access for Seller ID 31435; **Shiva Kumar Yalagunda Bas completed the access grant at 11:29 UTC.** Lalita Phichagonakasit previously reported Pureen barcode truncation.
*   **2026-03-26:** Iris Chang requested sales report for UNICO Distribution Services; Greta Lee reported Yumsay Foods barcode issue; Ee Ling Tan queried picklist delivery.
*   **2026-03-25:** Cassandra Thoi requested checks on orders #256055476 and #248407866.
*   **2026-03-21:** Amos Lam reported vendor picklist failure due to public holiday opt-out status.


## [27/70] RMN Incidents
Source: gchat | Group: space/AAQAz11ATzY/f96GZlnokS4 | Last Activity: 2026-03-27T11:29:15.744000+00:00 | Last Updated: 2026-03-27T14:35:57.366604+00:00
**Daily Work Briefing: RMN Incidents Analysis**

**Key Participants & Roles**
*   **Rachit Sachdeva:** Analyst/Investigator. Initiated the review of March traffic trends and provided detailed data via email.
*   **Michael Bui:** Technical Investigator. Collaborating to validate Rachit's findings by cross-referencing captured request logs.
*   **Nikhil Grover & Rahul Jain:** Tagged for visibility; no substantive updates provided in this chat thread.

**Main Topic**
Investigation into a significant traffic trend observed between March 20–27, 2026. Rachit identified that requests with `f_pcnt` (product count) set to "1" dominated the volume:
*   **CATEGORY pages:** >90% of requests.
*   **SEARCH pages:** >98% of requests.

This configuration limits system responses to a single product impression per request. The discussion focuses on confirming whether recent changes were made to the product count filter configuration causing this anomaly.

**Pending Actions & Ownership**
*   **Action:** Review captured request logs (URL, headers) to validate if `f_pcnt=1` is due to a configuration change or upstream client behavior.
    *   **Owner:** Michael Bui (Status: In Progress/Confirmed receipt of data).
*   **Context for Action:** Rachit previously emailed full request details including URL and headers to Michael (with confidential data handled via DM/email) on March 27 at 10:53 AM.

**Decisions Made**
*   Both parties agreed that yesterday's (March 26) data samples would suffice for the initial technical validation.
*   Data transmission protocol was confirmed: Full requests to be shared, with any confidential elements sent via separate secure channels (DM/Email).

**Key Dates & Follow-ups**
*   **Analysis Period:** March 20–27, 2026.
*   **Discussion Date:** March 27, 2026.
*   **Data Provided:** Yesterday's logs (March 26) shared via email prior to 11:29 AM.
*   **Next Step:** Michael Bui is currently analyzing the received email data to determine if configuration changes occurred regarding product count filters.


## [28/70] RMN Incidents
Source: gchat | Group: space/AAQAz11ATzY | Last Activity: 2026-03-27T10:29:57.571000+00:00 | Last Updated: 2026-03-27T10:39:22.553372+00:00
**Daily Work Briefing: RMN Incidents (Updated)**

**Key Participants & Roles**
*   **Nikhil Grover:** Issue initiator; escalated urgency for resolution by EOD March 27th. Recently requested an update on the investigation status.
*   **Rachit Sachdeva:** Investigator; identified a systemic configuration issue regarding product count parameters. Currently preparing detailed data via email.
*   **Stakeholders (CC'd):** Shubhangi Agrawal, Michael Bui, Allen Umali, Rajiv Kumar Singh, Ravi Goel.
*   **New Involvement:** Rahul Jain (noted in update request).

**Main Topic**
Critical investigation into a 50% drop in product ad impressions and $11k revenue loss since March 17th. Initial hypotheses regarding paused campaigns were refuted by Nikhil, who noted single-SKU responses persist despite active advertisers. Rachit has now identified the root cause: a configuration anomaly where the `f_pcnt` parameter (requested product count) is set to 1 in over 90% of CATEGORY and 98% of SEARCH page requests, forcing single-product system responses regardless of available inventory.

**Critical Findings & Data**
*   **Root Cause Identified:** The issue is not supply-side pausing but a request parameter configuration. When `f_pcnt` equals 1, the system returns only one product per call.
    *   **CATEGORY Pages:** Requests with `f_pcnt`=1 consistently exceeded 90% (Mar 20–27).
    *   **SEARCH Pages:** Requests with `f_pcnt`=1 consistently exceeded 98% (Mar 20–27).
*   **Previous Context:** While Rachit initially noted 24 paused advertisers generating $11.5k revenue (Mar 1–17), this was insufficient to explain the single-SKU output observed in active campaigns (e.g., Ferrero, Colgate). The new data confirms the "single response" behavior is driven by the parameter count, not advertiser availability.

**Decisions Made**
*   **Root Cause Confirmation:** The issue has shifted from a supply-side analysis to a configuration review of product count filters (`f_pcnt`).
*   **Priority Status:** Elevated to immediate resolution; Nikhil requested an update on March 27th at 08:34 UTC.

**Pending Actions & Ownership**
*   **Action:** Investigate recent updates or changes to the configuration governing product count filters in requests.
    *   **Owner:** Team (Rachit Sachdeva to confirm with stakeholders).
*   **Action:** Distribute detailed data analysis regarding the March 20–27 trends for `f_pcnt`.
    *   **Owner:** Rachit Sachdeva (Email follow-up pending confirmation of findings).
*   **Action:** Resolve the configuration override to allow multi-SKU responses when multiple active campaigns exist.
    *   **Owner:** Engineering Team / Technical Owners.

**Key Dates & Deadlines**
*   **Incident Start Date:** March 17th (campaign pauses observed; impact noted).
*   **Latest Update:** March 27th, 2026 at 08:34 UTC (Nikhil follow-up); 10:29 UTC (Rachit root cause analysis).
*   **Data Window:** Mar 1–17 (Revenue baseline); Mar 20–27 (Current `f_pcnt` trend analysis).
*   **Deadline:** Resolution required by end of day on March 27th.

**Attachments Referenced**
*   `FPG _ Paused Advertisers (1).xlsx` (Shared by Rachit on Mar 26; reviewed by Nikhil on Mar 27).
*   **New Data:** Detailed analysis regarding `f_pcnt` trends for March 20–27 (to be sent via email by Rachit).


## [29/70] Team Starship
Source: gchat | Group: space/AAQAX9iKYf0 | Last Activity: 2026-03-27T09:35:05.122000+00:00 | Last Updated: 2026-03-27T10:41:50.003976+00:00
**Daily Work Briefing: Team Starship (Updated)**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Operations/Testing Lead.
*   **Danielle Lee:** Biz Ops/S&G Representative.
*   **Vivian Lim Yu Qian:** Product/Design Liaison.
*   **Alvin Choo:** Compliance Lead / Technical POC.
*   **Zi Ying Liow:** Frontend/Promotion Logic Inquiry.
*   **Sathya Murthy Karthik:** Shared Omni Roadmap update (March 2026).
*   **Nikhil Grover:** Compliance/PRD Liaison.

**Main Topics & Decisions**

1.  **BCRS Refunds Status (Critical Update)**
    *   **Status:** UAT complete for Customer App, Backend/Backoffice, MP Seller (Mirakl & DBP), and Preorder Staff App. Production deployment of DBP + SAP parts is confirmed.
    *   **Sign-off Timeline:** Corporate Control and Finance require first half of the day to finalize formalities; sign-off expected **EOD today**. Full UAT sign-off forms submitted for E-comm, Marketplace SKU Listing, and In-store Pre-order.
    *   **Open Non-Critical Items (Post-Launch):**
        *   **Re-delivery:** BCRS items currently cannot be re-delivered. Business holds off attempts until fix; ETA: Ready for UAT April 2, Deploy April 8.
        *   **FOC Deposit Charging:** Staff app unable to charge deposits on FOC items. Solution pending; ETA update by Monday.
        *   **B2B Quick Buy:** BCRS SKUs unavailable via quick buy. UAT in progress; Production ETA **April 3**.
    *   **Production Testing:** Smoke test scheduled for Friday (and weekend if necessary). Next production test planned for **Monday, April 30** post-deployment of refunds.
    *   **Issues:** Minor logging issue found on Marketplace orders during regression; fix deploying EOD.

2.  **Compliance & PRD Updates**
    *   **Regulatory Requirements:** Nikhil Grover shared Compliance perspective for Project Light (FPG App/BO/BE Replatform), specifically IAB standards on impression tracking (Requirement C4). Links provided in PRD documents.

3.  **Bug Report: App Icon Display (DPD-783)**
    *   **Issue:** Vivian reported Christmas theme regression.
    *   **Action:** Ticket created for urgent resolution ("asap"). Engineering Team/Andin Eswarlal Rajesh to revert.

4.  **New Request: Cart-Level Coupon Allocation**
    *   **Status:** Alvin Choo relayed Ryan's request to stop per-SKU cart-level coupon allocation for accurate GP calculation. Team determining if this fits "Project Light" list.

5.  **Frontend Tag Mapping & Performance Marketing**
    *   **Inquiry:** Zi Ying Liow seeks clarification on promotion method-to-tag mapping logic (pending technical verification).
    *   **Performance Marketing:** Alvin Choo requested an alias to the Performance Marketing team regarding a specific app change request looped in by Andin Eswarlal Rajesh.

6.  **OMNI Project Status**
    *   **Omni Roadmap:** PMs must submit deprioritized items from the "Jan 2026" roadmap by **EOD today (March 25)**.
    *   **OMNI-1345:** Indefinite hold due to foundational business model changes.

7.  **Operational Pilots**
    *   Operations piloting "picker app enhanced for CT58" on DT50S/DT66S models; Prajney emphasizes testing before store rollout.

8.  **CHAS Verification Flow**
    *   Auto-verification via MyInfo remains technically feasible but outside current "Light" scope. Vivian to verify assumptions with Serene.

9.  **Scan@Door: AI Personalisation**
    *   Daryl Ng proposed AI-based voucher issuance (vs. rule-based). Estimated BE impact: 2 weeks. Target go-live mid-April. Prioritization decision pending resource review.

**Pending Actions & Owners**

| Action Item | Owner | Deadline/Note |
| :--- | :--- | :--- |
| **Finalize:** BCRS Finance/Corp Control sign-off | Prajney / Finance | **EOD Today** |
| **Deploy:** Marketplace logging fix | Engineering Team | **EOD Today** |
| **Confirm:** App Icon revert (DPD-783) | Andin Eswarlal Rajesh / Eng | ASAP |
| **Clarify:** B2B Cybersource OTP flow applicability | Alvin Choo | As needed |
| **Submit:** Omni Roadmap deprioritization list | All PMs | **EOD Today (March 25)** |
| **Update:** OMNI-1282 status (De-prioritize) | Alvin Choo / Koklin Gan | Pending confirmation |
| **PAUSE:** OMNI-1345 requirements | All Stakeholders | Until business model finalized |
| **Clarify:** Cart-level coupon logic & Project Light inclusion | Alvin Choo / Ryan's team | Pending decision |
| **Prioritize:** Scan@Door AI Personalisation review | Danielle Lee, Daryl Ng, Tech Leads | Immediate |
| **Provide:** Performance Marketing alias contact | Alvin Choo / Andin Eswarlal Rajesh | Immediate |

**Key Dates & Follow-ups**

*   **Meeting Rescheduled:** Weekly Epics meeting postponed to **Wednesday, March 12 (tomorrow) at 11:00 AM**. Location: Level 12 Room 18 (or virtual/pantry).
*   **Reference Tickets:** SHOP-3779, OMNI-1099, DPD-100, **DPD-783**, OMNI-1345, OMNI-1282, OMNI-1421.


## [30/70] FPG Everyone - General
Source: gchat | Group: space/AAAAjDYVcBU | Last Activity: 2026-03-27T08:28:22.476000+00:00 | Last Updated: 2026-03-27T10:44:25.900406+00:00
**Daily Work Briefing: FPG Everyone Chat Summary (Updated)**
**Date Range:** March 3 – March 27, 2026
**Source:** Google Chat (FPG Everyone - General)

### Key Participants & Roles
*   **Siti Nabilah:** Day of Service Campaign Promoter.
*   **Jasmine Neo:** Senior Executive, E-Commerce (Ordering Management).
*   **Keith Lee:** Industry Trends Monitor.
*   **Melissa Lim:** Community Engagement Lead.
*   **Maisy Heeng:** FPG Food Services Brand Lead.

### Main Topics
1.  **Digital Access Rollout:** Schedule confirmed and executed (C-suite/HR/Finance on Mar 16; Customer/Marketing/E-Commerce on Mar 23; Remaining Hub staff by Mar 30). User guide distributed.
2.  **Media Collaboration – "Bowl of Love":** Final episodes featuring Tyler Ten, Tasha Low, and Xiang Yun are officially live following the March 21 launch. The story focuses on warmth and healing with fresh Malaysian pork.
    *   **Platform:** @mediacorp.re.dian TikTok (`https://vt.tiktok.com/ZSusN9b4n/`).
3.  **Industry Recognition:** Lau Pa Sat's "Spin for your Huat" campaign was featured by Campaign Asia as a top CNY campaign to watch in 2026, competing alongside global heavyweights like Nike and Apple.
    *   **Source:** `https://www.campaignasia.com/article/brands-launch-campaigns-celebrating-chinese-new-year-2026/n554u1b7maurkcmkwcd29mooi2`
4.  **FairPrice Heartland Hits Launch (Mar 27):** A new community storytelling contest launched to turn neighbourhood stories into music.
    *   **Mechanism:** Share FairPrice moments with store location and region hashtags (#FPNorthie, #FPEastie, #FPSouthie, #FPWestie) plus #FPHeartlandHits.
    *   **Incentives:** $50 E-Vouchers for winners; top stories featured in the final "Heartland Hit."
    *   **Region Reps:** Support leaders including @itsmydadera (South), @thesamdriscoll (East), @sarahhuangbenjamin (West), and @leeshuhadah (North).
    *   **Link:** `https://www.instagram.com/p/DWQMR9tIL_e/` | **Deadline:** April 5, 2026.
5.  **Unity Wellness Promotions:**
    *   **World Oral Health Day:** Offers extended through March 25 (Listerine, Colgate, Oral-B).
    *   **New B1G1 Promotion (Mar 26–29):** Zhaoyue Touw announced a "Buy 1 Get 1 FREE" on selected health and wellness essentials at Unity stores.
        *   **Link:** `https://go.fpg.sg/Unity-MarB1G1`
    *   **Wellness Picks:** Ariel Yap highlighted products including Moom Health Happy Hormones, Elastine Perfume De Shampoo/Conditioner, New Moon Bird's Nest Gift Set, and Greenlife Derma Youth Softgels.
        *   **Catalogue Link:** `https://go.fpg.sg/HABAFPG_WK4`
6.  **New Brand Launch – Shabu Days (FPG Food Services):** First overseas brand introduction launching April 3 at Hillion Mall. Concept focuses on hotel-inspired elevated dining at heartland prices.
    *   **Socials:** IG `https://www.instagram.com/shabu_days.sg/`, FB `https://www.facebook.com/ShabuDays.SG`.
7.  **Loyalty Promo (Chloe Ong):** A new redemption offer launched on March 27 with a price point of **$0.99** to reduce barriers for trial.
    *   **Link:** `https://go.link.sg/wexvmf`

### Pending Actions & Ownership
*   **Shorty Awards Voting (Owner: All Staff):** FPG has two campaigns shortlisted for the 18th Annual Shorty Awards under "Audience Honor."
    *   **Action:** Create a personal email account, vote daily from today until **April 8**, casting one vote per category per day.
*   **Volunteer Engagement (Owner: All Staff):** Siti Nabilah shared a "Volunteer Spotlight" featuring Jasmine Neo. Staff encouraged to sign up for upcoming opportunities.
    *   **Link:** `https://forms.gle/UkyQDagmDy4mcY7K7`
*   **Sensory Test Sign-ups (Owner: All Staff):** Chapati screening form remains open (`https://forms.gle/DFYrahZcvhtcoJ9R7`). Frozen Snacks sign-up is closed.
*   **Heartland Hits Participation:** Staff encouraged to submit stories and rally regional crew before April 5.
*   **New Redemption Action:** Staff encouraged to redeem the $0.99 offer immediately.

### Decisions Made
*   **Awards Campaign:** Strategic decision to mobilize staff for Shorty Awards voting until April 8.
*   **Wellness Extension:** Unity promotions extended with a new B1G1 offer (Mar 26–29).
*   **Service Event:** "Willing Hearts Kitchen Crew" spots are fully booked/closed as of late March 27 morning. Future opportunities remain open via the new sign-up link.
*   **New Loyalty Initiative:** Decision to launch a low-barrier ($0.99) redemption offer.
*   **Brand Expansion:** Approval and execution of Shabu Days launch (April 3) as FPG Food Services' first overseas brand.

### Critical Dates & Deadlines
*   **March 25:** World Oral Health Day offers expired.
*   **March 26–29:** Unity B1G1 Promotion on health/wellness essentials.
*   **April 3:** Shabu Days launch at Hillion Mall.
*   **April 5:** FairPrice Heartland Hits contest closes.
*   **April 8:** Shorty Awards voting deadline.


## [31/70] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/X0kOPw3Ylqk | Last Activity: 2026-03-27T07:51:27.333000+00:00 | Last Updated: 2026-03-27T10:48:03.618428+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Key Participants & Roles**
*   **Sneha Parab:** Initiator; aligning on epic closure status.
*   **Akash Gupta:** Contributor providing board assignment and clarification requests.
*   **Wai Ching Chan:** PM/Contributor confirming input provided and handoff details.
*   **Michael Bui:** Identified as the owner for pending work items.
*   **Andin Eswarlal Rajesh:** Tagged for inputs (no response recorded in snippet).

**Main Topic**
Closure of the **BCRS epic**. Sneha Parab raised concerns that specific tickets remain in the "define" state despite alignment at the weekly epics meeting, requesting clarification on ownership and completion status.

**Pending Actions & Ownership**
*   **DPD-637:** Akash Gupta identified this ticket belongs to the **core products (payment) board**. Status requires reassignment or validation by the relevant team.
*   **DPD-807:**
    *   **Wai Ching Chan:** Has already provided input; no further action required from them at this time.
    *   **Michael Bui:** Explicitly owns the remaining work for this ticket ("The rest for Michael to handle").

**Decisions Made**
*   **DPD-637 Ownership:** It was determined that invoices regarding this ticket should be managed under the core products (payment) board, not the current Digital Product Development scope.
*   **DPD-807 Status:** Work initiated by the PM is 50% complete (input provided by Wai Ching Chan); the remaining execution rests solely with Michael Bui.

**Key Dates & Follow-ups**
*   **Date:** March 27, 2026.
*   **Context:** Follow-up to the "weekly epics meeting."
*   **Target:** Immediate closure of the BCRS epic.
*   **Dependencies:** Resolution requires Michael Bui to complete DPD-807 and the team to address the board assignment for DPD-637.

**Reference Links**
*   **Jira Tickets:** [DPD-637](https://ntuclink.atlassian.net/browse/DPD-637), [DPD-807](https://ntuclink.atlassian.net/browse/DPD-807)
*   **Chat Room:** [Link to Room Discussion](https://chat.google.com/room/AAQAgT-LpYY/qtUOXlxVm80/qtUOXlxVm80?cls=10)


## [32/70] QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs | Last Activity: 2026-03-27T07:39:49.781000+00:00 | Last Updated: 2026-03-27T10:49:33.345223+00:00
**Daily Work Briefing: QE <-> All Tribes** (Updated)

**Key Participants & Roles**
*   **Patrick Thun:** Lead/Coordination.
*   **Madhuri Nalamothu:** QA Lead/Test Execution.
*   **Milind Badame:** QA Engineer.
*   **Hang Chawin Tan:** DevOps/Backend Support.
*   **Daryl Ng / Michael Bui:** Dev/Product.
*   **Komal Ashokkumar Jain:** Reported New Defect.
*   **Zaw Myo Htet:** Backend/Voucher Developer.
*   **Tiong Siong Tee:** Android Development.
*   **Yangyu Wang:** Search Logic Support.
*   **Pandi:** Recent responder regarding LinkPoints and iOS SnG Flow.
*   **Others:** Piraba Nagkeeran, Andin Eswarlal Rajesh.

**Main Topics & Discussion**
1.  **LinkPoints Regression Failure (Critical Update):** On **27 Mar**, Milind Badame reported a complete failure of all LinkPoints tests due to a `500` error at the CLS Award Balance API step: *"Transaction posting failed"*. *Status:* Critical/Blocked. Discussion ongoing with @Pandi (4 replies, last reply 4:49 AM).
2.  **iOS SnG Flow QR Loading Issue (New):** On **27 Mar**, Madhuri Nalamothu reported a random issue in iOS where scanning the QR code in the SnG Flow gets stuck on loading forever. The issue is reproducible manually but inconsistent, observed on iOS 15 and 17. *Status:* Investigating flakiness. *Owner:* @Pandi (5 replies, last reply 7:46 AM).
3.  **Express Cart Service Fee Waiver:** Milind Badame reported service fees incorrectly waived in Express cart mode (Subtotal $37.87) on **26 Mar**. *Status:* Open/Investigating. *Owners:* @Daryl Ng, @Andin Eswarlal Rajesh.
4.  **Search Indexing Failure:** Critical failure where "Ninben Tsuyu No Moto Seasoning Soy Sauce - Triple Strength" (Hyper Changi) is invisible in search despite stock availability. *Status:* Urgent investigation needed. *Owners:* @Daryl Ng, @Yangyu Wang.
5.  **OmniHome Christmas Tiles Anomaly:** "Dressed up" Christmas tiles visible for FoodTakeaway on OmniHome in March. *Status:* Investigating visual consistency.
6.  **PreOrder Tile Permanency:** New PreOrder tile flagged on **25 Mar**; E2E test updates pending confirmation of permanency from Dev/Product.
7.  **LinkPay Receipt Banner Missing:** Android banner missing in LinkPay receipts; investigation requested with @Tiong Siong Tee.
8.  **E-Voucher Application Error:** `404 Invalid voucher` error reported by Milind Badame on **24 Mar**; backend logic failure. *Owner:* @Zaw Myo Htet.
9.  **Cart Page Logic Flaw (Critical):** Komal Ashokkumar Jain reported cart items "stick" when switching to Express delivery, allowing ineligible orders for 1HD. Reported **20 Mar**.
10. **Android OTP Blank Screen:** Blank screen on Android v12 and below; investigation requested with @Tiong Siong Tee.
11. **Other Defects:** Missing `label` attribute for Postal Code **098619**; DC Membership Logic discrepancy (back office vs. UI); General UI alignment/navigation issues persist.

**Pending Actions & Ownership**
*   **LinkPoints API Resolution:** Investigate "Transaction posting failed" error at CLS Award Balance API immediately to unblock regression. *Owner: @Pandi, Dev Team.* **(High Priority)**
*   **iOS SnG Flow Loading:** Investigate random/stuck loading issue during QR scanning on iOS 15/17 in SnG Flow. *Owner: @Pandi, Mobile Team.* **(New High Priority)**
*   **Express Cart Service Fee:** Verify why service fees are waived in Express cart mode. *Owners: @Daryl Ng, @Andin Eswarlal Rajesh.*
*   **Search Indexing Failure:** Resolve search failure for "Ninben Tsuyu No Moto Seasoning Soy Sauce - Triple Strength" at Hyper Changi. *Owners: @Daryl Ng, @Yangyu Wang.*
*   **PreOrder Tile Strategy:** Confirm if PreOrder tile is permanent to decide on E2E test updates. *Owner: @Daryl Ng / QA Team.*
*   **Cart Express Delivery Logic:** Resolve cart alignment and delivery mode eligibility logic. *Owners: Komal Ashokkumar Jain, Daryl Ng, Andin Eswarlal Rajesh.*
*   **LinkPay Receipt Banner & Android OTP:** Fix missing banner and blank screen issues. *Owner: @Tiong Siong Tee.*

**Decisions Made**
*   Ad slot changes proceed; known test impacts acknowledged.
*   No resolution yet on LinkPoints (now critical), iOS SnG Flow loading, Express cart service fee, Search indexing, Cart eligibility logic, or tile anomalies; awaiting investigation results and Dev clarification.

**Key Dates & Deadlines**
*   **5 Mar:** Load testing window (completed).
*   **16 Mar:** DC membership logic discrepancy logged.
*   **20 Mar:** Critical Express delivery bug flagged.
*   **24 Mar:** E-Voucher error and Android OTP issue raised.
*   **25 Mar:** OmniHome tiles, LinkPay receipts, Search indexing, PreOrder tile issues flagged.
*   **26 Mar:** Express cart service fee discrepancy reported (active until 8:59 AM).
*   **27 Mar:** LinkPoints API failure reported at 02:47 UTC; discussion active until 4:49 AM. iOS SnG Flow issue observed today; discussion active until 7:46 AM.


## [33/70] SRE / Network / DBA / DevOps / Infra
Source: gchat | Group: space/AAAAYX-ew1s | Last Activity: 2026-03-27T07:30:29.958000+00:00 | Last Updated: 2026-03-27T10:50:06.498405+00:00
**Daily Work Briefing: SRE / Infrastructure Team**

**Key Participants & Roles**
*   **Apurva Shingne:** Requests review for PR #142 (`infra-gcp-fpg-optimus`) and ticket GCD-8995; tagged @Sneha Parab, @Nicholas Tan.
*   **Madhawa Mallika Arachchige:** Confirmed channel usage for Datadog PR submissions on 2026-03-26.
*   **Natalya Kosenko:** Submitted Terraform PR #719; strategic IaC discussions ongoing.
*   **Boning He:** Requested access to pricing workspaces via PR #722.
*   **Zheng Ming, Wai Ching Chan, Calvin Phan:** Reported connectivity/network issues (GCD-8941, GCD-8954, DSD-11066).
*   **Himal Hewagamage & Isuru Dilhan:** Primary reviewers/approvers.

**Main Topics**
1.  **Datadog Infrastructure & Compliance:** Ongoing review of `fp-datadog-eu` PRs (#135–#148). On **2026-03-27**, Apurva Shingne submitted new PR **#142** (`infra-gcp-fpg-optimus`) linked to ticket **GCD-8995**.
2.  **Terraform & Workspaces:** Natalya Kosenko's PR #719 and Boning He's PR #722 (pricing workspace access) are pending review. A failed Terraform plan (`run-CZVLtajJGbLVojLM`) and ticket GCD-8900 remain active.
3.  **CI/CD Pipeline Failures:** Soni-BE golden pipeline clone failures persist; `lt-strudel-api-go` Go versioning conflicts (Go 1.25.8 vs `golangci-lint`) require resolution.
4.  **Cloud Networking:** AI agents in `us-central1` face internet connectivity issues (Ticket GCD-8941). Mohit Niranwal mandated non-prod testing prior to rollout.
5.  **Bastion Connectivity:** Wai Ching Chan's ticket GCD-8954 remains under investigation.
6.  **Database Subnet Request:** Calvin Phan requested CloudSQL subnets for SOT-SONI (Ticket DSD-11066); DBA coordination with @Himal Hewagamage is active.

**Pending Actions & Ownership**
*   **Review New Datadog PRs:**
    *   **PR #142:** Owned by **Apurva Shingne**; tagged for review by **@Sneha Parab**, **@Nicholas Tan**.
    *   **PR #135, #137–#139, #140, #144, #147:** Managed by @Himal Hewagamage and @Isuru Dilhan. PR #140 is also tagged to @Maou Sheng Lee.
*   **Review Terraform PRs:**
    *   **PR #719** (Natalya) & **PR #722** (Boning): Pending review by @Isuru Dilhan and @Himal Hewagamage.
*   **Troubleshoot Pipeline Issues:** Investigate Soni-BE SSH keys (Kalana) and `lt-strudel-api-go` config conflicts (Lester).
*   **Infrastructure Strategy:** Finalize IaC implementation for Datadog log pipelines (Natalya; discussion with @Prabu Ramamurthy Selvaraj).
*   **Network & DBA Tickets:** Execute non-prod testing for Cloud NAT (GCD-8941); investigate Bastion issues (GCD-8954); review SOT-SONI subnet requirements (DSD-11066).

**Decisions Made**
*   **IaC Requirement:** Mandatory adoption of IaC for Datadog pipelines.
*   **Change Management:** Mohit Niranwal mandated non-prod testing for Cloud NAT changes before production deployment (regarding GCD-8941).

**Key Dates & Follow-ups**
*   **2026-03-02 to 03-05:** Initial Datadog PR requests.
*   **2026-03-11 to 03-12:** Critical pipeline failures reported.
*   **2026-03-19:** GCD-8941 raised; Mohit Niranwal intervention regarding testing protocol.
*   **2026-03-20:** Bastion (GCD-8954) and DBA subnet (DSD-11066) tickets opened.
*   **2026-03-24:** PR #140 and #722 requested for review.
*   **2026-03-26:** Channel confirmation for Datadog submissions; @Andin Eswarlal Rajesh engaged.
*   **2026-03-27 (07:30 UTC):** Apurva Shingne submitted PR #142 and ticket GCD-8995; requested review from @Sneha Parab and @Nicholas Tan.


## [34/70] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw | Last Activity: 2026-03-27T07:21:11.133000+00:00 | Last Updated: 2026-03-27T10:51:39.560169+00:00
**Daily Work Briefing: Digital Product Development (DPD)**

**Key Participants & Roles**
*   **Flora Wo Ke:** Team Lead.
*   **Alvin Choo:** Developer/QA.
*   **Nicholas Tan:** DevOps/Infrastructure.
*   **Tiong Siong Tee / Andin Eswarlal Rajesh:** QA/Engineering (iOS).
*   **Winson Lim:** Engineering Lead/Strategy.
*   **Natalya Kosenko:** DevOps/SRE.
*   **Boning He / Gopalakrishna Dhulipati:** Team Members.
*   **Kyle Nguyen:** Team Member.
*   **Maou Sheng Lee:** Team Member.
*   **Jazz Tong:** Incident Coordinator (New).
*   **Akash Gupta:** Support Lead (New).
*   **Vivian Lim Yu Qian:** Staff Verification Specialist (New).

**Main Topics & Discussions**
1.  **Staff Verification Logic (S&G Flows):** On March 27, 2026, Vivian Lim Yu Qian queried the existence of an app screen for staff verification during SKU purchases requiring force verification (e.g., milk powder), referencing age-restriction popup logic. The team is investigating compliance with existing verification protocols.
2.  **Incident Management Response:** Earlier on March 27, Jazz Tong raised an urgent query regarding a potential incident ("it is incident?"). The team mobilized support for the DPD Incidents channel involving Gopalakrishna Dhulipati, Akash Gupta, and Kyle Nguyen.
3.  **Infrastructure & Operations Risk:** Nicholas Tan flagged risks regarding Broadcom ending free Bitnami images, causing `kubectl` image tag failures and increased Time To Recovery (TTR) impacting the Golden Pipeline (GP).
4.  **Payment Service Issues:** Alvin Choo reported promo code redemption failures in FP Pay; confirmed that a change freeze has ended and feature releases are proceeding.
5.  **Mobile Quality Assurance:** Andin Eswarlal Rajesh identified an iOS FPPay bug where QR codes load without user login, escalated via file download.
6.  **Datadog Governance:** Natalya Kosenko reported unauthorized manual changes to Datadog On-Call teams (removals of Maxine, Arijit, Minu). Terraform manages this config; manual console edits are overwritten on the next run.
7.  **Strategic Planning:** Winson Lim highlighted data centers as potential targets in modern warfare (Iran conflict context) to inform Disaster Recovery (DR) scenarios.
8.  **Product Strategy & Tooling Expansion:** On March 26, Winson Lim noted Reforge joined Miro, signaling expansion into product strategy to close the gap between decision-making and delivery.
9.  **Social Events & Sentiment:** Kyle Nguyen announced an upcoming DPD BBQ with the sentiment "We come first." Maou Sheng Lee expressed a sentiment of feeling like energy is being wasted on March 18.

**Pending Actions & Owners**
*   **S&G Verification Team (Vivian Lim Yu Qian, Product/Dev Teams):** Investigate current S&G flows against the WIP verification logic document to confirm if forced staff verification screens exist for restricted SKUs like milk powder. Reference: `https://ntuclink.atlassian.net/wiki/spaces/SE/pages/1995997683/WIP+S+G+Verification+Flow`.
*   **Incident Response Team (Jazz Tong, Akash Gupta, Gopalakrishna Dhulipati, Kyle Nguyen):** Act as support guides for the active DPD Incidents channel; monitor and resolve incoming incident queries.
*   **GP Team (Nicholas Tan / Mohit Niranwal):** Investigate Bitnami image replacement strategy to resolve TTR issues and update Golden Pipeline dependencies.
*   **iOS/Dev Team (Tiong Siong Tee / Andin Eswarlal Rajesh):** Investigate the iOS FPPay QR code login bypass bug.
*   **Datadog Admins:** Anyone who manually altered Datadog Teams must submit a Pull Request to `https://bitbucket.org/ntuclink/fp-datadog-eu` instead of editing the console.

**Decisions Made**
*   No formal change freeze; feature releases are currently active (Alvin Choo).
*   Datadog team configurations must strictly follow Infrastructure as Code (Terraform) protocols; manual overrides are deprecated.
*   Miro's acquisition of Reforge is recognized as a strategic move to bridge product strategy and delivery gaps.
*   **New:** Active incident support protocol established for Jazz Tong, Akash Gupta, Gopalakrishna Dhulipati, and Kyle Nguyen on March 27, 2026.
*   **New:** Verification of S&G staff verification screens is pending; current logic requires validation against the WIP document.

**Key Dates & Follow-ups**
*   **Mar 27, 2026 (03:03 UTC):** Jazz Tong flagged potential DPD incident; support team mobilized.
*   **Mar 27, 2026 (08:11 AM):** Vivian Lim Yu Qian raised S&G verification flow query; discussion concluded with 12 replies.
*   **Mar 26, 2026:** Winson Lim shared Reforge joining Miro; potential impact on product strategy workflows identified.
*   **Mar 25, 2026:** Natalya Kosenko highlighted DPD alumni participation in a Google AI event.
*   **Mar 18, 2026:** Maou Sheng Lee noted sentiment regarding wasted energy.

**Social Notes**
*   Boning He and Gopalakrishna Dhulipati shared snacks (Chinese cookies with chicken gizzard/medicinal barley and Indian cookies) in pantry areas.
*   Upcoming DPD BBQ announced by Kyle Nguyen ("We come first, see you!").


## [35/70] [Prod Support] Offers
Source: gchat | Group: space/AAAAzZ3qkNU | Last Activity: 2026-03-27T06:17:14.551000+00:00 | Last Updated: 2026-03-27T06:40:11.493447+00:00
**Daily Work Briefing: [Prod Support] Offers**

**Key Participants & Roles**
*   **Willie Tan:** Reported initial issue (Mar 17) with offer visibility; escalated on Mar 26 regarding promo flow failure for specific SKUs.
*   **Angela Yeo:** Previously escalated discrepancy regarding incorrect promo display for SKU 13066243.
*   **Alvin Choo:** Previously flagged urgency and assigned owners for the initial case.
*   **Zaw Myo Htet & Daryl Ng:** Assigned to investigate both historical and new flow issues.
*   **Neo Seng Ka:** Investigating database segment configuration (Mar 27).

**Main Topic**
Investigation into production offer display errors involving two distinct but potentially related scenarios:
1.  **Historical Context (Mar 17–19):** Issues with Offer ID `sap offer 202603000112484` for **SKU 13066243**. The team confirmed "2 for $5.40" is the correct configuration, but it failed to display as expected while incorrect promotions were visible.
2.  **New Escalation (Mar 26):** Willie Tan reported that promos created in SAP are not flowing to FPON for a list of SKUs, despite these items *not* being on the promo blacklist. The specific SKUs provided were samples; a full investigation of the flow mechanism is required.
3.  **New Technical Query (Mar 27):** Neo Seng Ka raised a query regarding DBP segment configuration, specifically checking for segments involving "union + dcc" logic, noting no results found when searching for "union."

**Pending Actions & Ownership**
*   **Action 1:** Investigate why correct offers ("2 for $5.40") are not displaying or if incorrect offers are showing for historical cases (SKU 13066243).
*   **Action 2:** Investigate the root cause of promo flow failure from SAP to FPON for SKUs not on the blacklist, as reported by Willie Tan on March 26.
*   **Action 3 (New):** Clarify DBP segment logic regarding "union + dcc" configurations and confirm why no applicable segments were found in the database.
*   **Owners:** @Zaw Myo Htet, @Daryl Ng (assigned previously; applicable to all issues). @Neo Seng Ka is investigating the DBP configuration.
*   **Status:** Active/Urgent. The scope has expanded from a single SKU display error to a systemic flow issue affecting multiple SKUs. Debugging now includes database segment validation.

**Decisions Made**
No final technical fixes have been implemented yet. The team has established the expected outcome for historical cases: offers must display "2 for $5.40." For the new case, it is confirmed that SKUs in question should be eligible for promos (not blacklisted) but are failing to receive them from SAP. Neo Seng Ka's inquiry suggests a potential gap or misconfiguration in the DBP "union + dcc" segment logic which may be contributing to the flow failure.

**Key Dates & Deadlines**
*   **Initial Issue Reported:** March 17, 2026 (09:01 AM).
*   **Historical Escalation:** March 19, 2026 (10:04 AM and 12:35 PM).
*   **New Flow Issue Reported:** March 26, 2026 (02:24 AM UTC) by Willie Tan.
*   **DBP Query Raised:** March 27, 2026 (06:17 AM UTC) by Neo Seng Ka.
*   **Deadline:** Immediate resolution requested for both the display error and the new flow failure.

**Reference Links & IDs**
*   **Chat Space URL:** https://chat.google.com/space/AAAAzZ3qkNU
*   **Historical Offer ID:** `sap offer 202603000112484`
*   **Historical SKU:** 13066243
*   **New Case Scope:** Multiple SKUs (samples provided by Willie Tan) not under promo blacklist.
*   **System Components:** SAP (source), FPON (destination), DBP (segment logic).


## [36/70] Progress Check: Monitor & On-Call Team Alignment - Mar 27
Source: gchat | Group: space/AAQAuufxt5I | Last Activity: 2026-03-27T05:33:46.176000+00:00 | Last Updated: 2026-03-27T06:41:10.747636+00:00
**Daily Work Briefing: Progress Check – Monitor & On-Call Team Alignment (Mar 27)**

**1. Key Participants & Roles**
*   **Madhawa Mallika Arachchige:** Initiator of the meeting reminder; likely a team lead or coordinator for the alignment effort.
*   **@all (8 of 13 viewed):** The broader Monitor & On-Call team members.

**2. Main Topic/Discussion**
The conversation centered on a scheduled **meeting reminder** regarding "Monitor & On-Call Team Alignment." No detailed discussion content, technical updates, or problem-solving logs were recorded in the provided chat snippet; the primary activity was the dissemination of the meeting notification to the group.

**3. Pending Actions & Owners**
*   **Action:** Attend and participate in the alignment meeting.
    *   **Owner:** All team members (specifically the 8 who have viewed the message out of the total 13).
*   **Note:** No specific pre-meeting tasks or deliverables were assigned within this chat log.

**4. Decisions Made**
No formal decisions, votes, or strategic shifts were recorded in this single-message thread. The interaction serves as a logistical notification rather than a decision-making channel.

**5. Key Dates & Deadlines**
*   **Date:** March 27, 2026 (Specific time of message: 05:33:46 UTC).
*   **Event:** Monitor & On-Call Team Alignment Meeting.
    *   *Note:* The exact start time and duration of the meeting were not included in this specific reminder snippet.

**Summary Notes**
The provided data represents a single transactional message from Madhawa Mallika Arachchige intended to ensure team visibility for an upcoming alignment session. With 8 out of 13 recipients having viewed the message, attendance confirmation is pending. Further details regarding the meeting agenda or specific outcomes must be obtained directly from the meeting minutes or subsequent communications.

**Resource Link:** https://chat.google.com/space/AAQAuufxt5I
**Message Count:** 1


## [37/70] DPD Incidents
Source: gchat | Group: space/AAAAEsAEG84/bmd5TXQRY-w | Last Activity: 2026-03-27T04:54:45.718000+00:00 | Last Updated: 2026-03-27T06:41:31.016446+00:00
**Daily Work Briefing: DPD Incidents (HCBP Zone Issue)**

**Key Participants & Roles**
*   **Akash Gupta:** Technical Lead/Coordinator; identified root cause, managed DB fixes, and defined remediation steps.
*   **Owen Sng:** Operations Representative; flagged the anomaly regarding zone replacement despite standard KML upload procedures.
*   **Yap Chye Soon Adrian (Adrian):** Stakeholder; requested alignment meeting and verified order queue status post-fix.
*   **Ler Whye Ling Angel (Angel):** Initial reporter of missing picking orders for HCBP.
*   **Alvin Choo:** Team Lead; escalated issue to support room with Subject Matter Experts (SMEs).
*   **Gopalakrishna Dhulipati, Winson Lim:** Paged by Alvin for SME support.

**Main Topic**
Investigation and resolution of a critical incident where 820 orders for the HCBP store failed to appear in the picking queue due to a zone ID mismatch caused by an erroneous KML file upload.

**Root Cause Analysis**
The Changi zone (ID: 487) was deleted and replaced with a new zone (ID: 539). This occurred because the Ops team uploaded a KML file containing an extra trailing space in the name ("Changi " instead of "Changi"). The system interpreted this as a new location, invalidating existing orders linked to the old zone ID.

**Decisions Made**
*   **Immediate Mitigation:** Manual patching of affected orders via Database (DBA) ticket was executed to map them to the correct new zone.
*   **Process Validation:** The fix was verified by Adrian; pending orders are now in the picking queue following the scheduled 12:33 PM picklist generator run.

**Actions Pending & Ownership**
*   **Ops Team (Owen Sng, Alvin Choo):**
    1.  Maintain a backlog of zone upload files and validate against past uploads before production deployment.
    2.  Eliminate manual typing inputs when creating new KML files to prevent whitespace errors.
*   **DBP/Engineering Team (Akash Gupta):**
    1.  Implement an additional validation layer on the "update delivery area" API within the logistics-service to reject invalid KML formatting before processing.

**Key Dates, Deadlines & References**
*   **Incident Date:** March 27, 2026 (Timeline: 02:58 AM – 04:54 AM).
*   **Affected Volume:** 820 orders.
*   **Zone IDs:** Old Zone 487 replaced by New Zone 539.
*   **Ticket Reference:** DSD-11119 (NTU Enterprise Service Desk) – Used for DB patching; approved by Alvin Choo.
*   **Resolution Time:** Verified complete by 04:45 AM on March 27, 2026.
*   **Next Scheduled Run:** Picklist generator at 12:33 PM (March 27) to ensure pending orders are queued.
*   **Meeting Link:** https://meet.google.com/pib-buss-vqf (Call concluded).


## [38/70] Retail out of home (Digital Screens & CMS)
Source: gchat | Group: space/AAQAXn1ocmE | Last Activity: 2026-03-27T04:13:02.762000+00:00 | Last Updated: 2026-03-27T06:41:57.543576+00:00
**Daily Work Briefing: Retail Out of Home (Digital Screens & CMS)**

**Key Participants & Roles**
*   **Priscilla Chan Li Wei:** Inventory management (Samsung ADE/FilmScreen); Escalation workflow impact analysis.
*   **David Anura Cooray:** Technical operations; Lead on "EPT Blank Screen" investigation and **SWPZ** incident analysis.
*   **Fiona U:** Project Lead/Coordinator; driving Phase 1 closure and stakeholder alignment.
*   **Rajkumar Romendro & Allen Umali:** Subject matter experts for Retail Media inventory and Screen Loading (MPBS/VXT).
*   **Cheng Joo Wu:** Assigned to Action Items regarding SOPs, Indirect Procurement (IP), IFM integration, and Engie scope liaison.
*   **Serene Tan Si Lin:** Clarification on facility management scope boundaries.

**Main Topic**
The discussion centers on operationalizing **Retail Out of Home (RoOH) Phase 1**, focusing on hardware inventory verification, digital screen content loading, transitioning from Hypercare to Business As Usual (BAU), and finalizing SOPs. A critical update concerns the **IFM** announcement: it is now confirmed that IFM will encompass the current Engie scope of responsibilities (building equipment, soft services, aircons, freezers). Digital monitors remain excluded from this maintenance scope.

**New Critical Issues:**
1.  **EPT Blank Screen:** David Anura Cooray raised an urgent ticket requiring immediate technical investigation and potentially impacting screen connectivity workflows.
2.  **SWPZ Incident (ID: SWPZ):** A new high-priority thread identified by David Anura Cooray contains **14 replies** with the last update at **5:16 AM**. This requires immediate review alongside the EPT issue to assess potential systemic connectivity or loading failures.

**Pending Actions & Ownership**
*   **Sync Meeting Attendance:** Priscilla, Allen, Cheng, and Rajkumar must attend or assign a proxy to the sync scheduled for **Tuesday at 2:00 PM**.
    *   *Pre-meeting Review:*
        *   **SOPs (Gdoc & Gslide):** Resolve unresolved comments and perform consistency checks. Owners: Team (implied Priscilla/Cheng).
        *   **SLA Finalization:** Must be completed by next week for the Samsung SI meeting. Owner: Fiona U / Team.
        *   **Communication Channels:** Define escalation paths between stores and AdOps; identify chat groups to sunset. Owner: Team.
        *   **Indirect Procurement (IP):** Clarify IP's specific role before integrating them into the Retail Media Workflow. Owner: Cheng Joo Wu.
*   **Inventory Verification:** David Anura Cooray requested a master list of all digital screens under Retail Media; pending response from Allen Umali and Rajkumar Romendro.
    *   *Scope Update:* Inventory scope explicitly includes **PDD Gondola End Large TVs**.
*   **Issue Resolution (EPT & SWPZ):** David Anura Cooray must immediately investigate **"EPT Blank Screen"** occurrences and the **SWPZ** thread (14 replies, last updated 5:16 AM). This requires verification of CMS connectivity and screen status prior to the BAU transition.
*   **IFM Scope Liaison:** Cheng Joo Wu must approach the representative from RB for detailed Engie/IFM scope responsibilities.

**Decisions Made**
*   Transition from Hypercare to BAU is targeted for the week of **March 30, 2026**.
*   A pilot with Advertima is scheduled to end later this month (March 2026).
*   **IFM Scope Confirmation:** IFM will include the current Engie scope (building equipment/soft services); digital monitors are definitively **not** included. Escalation workflows for screen issues do not require IFM integration for monitor-specific faults.

**Key Dates & Deadlines**
*   **Tuesday (Current Week), 2:00 PM:** RoOH Phase 1 Sync Meeting.
*   **Next Week:** Finalize SLA for meeting with Samsung SI.
*   **Week of March 30, 2026:** Target transition to BAU (Store Training & Transition).
*   **Later this month:** End of Advertima pilot.

**Specific References**
*   **Files:** `NTUC Mac Serial number.xlsx` (Samsung inventory), Google Slides presentation on Indirect Procurement/Walkthroughs (`1FQrBgiiL69I_jsdy7W_aMTd1QApoT_Mn6A-IM25SUto`).
*   **Hardware/Systems:** Samsung screens (ADE, FilmScreen), **PDD Gondola End Large TVs**, MPBS - VXT Screen Loading, TAMHUB, FPHUB Digital Screen Content.
*   **Incident Logs:** EPT Blank Screen thread; **SWPZ** thread (14 replies, last updated 5:16 AM).


## [39/70] [Virtual] Smart Cart x RMN Catchup - Mar 27
Source: gchat | Group: space/AAQAGEaKjjo | Last Activity: 2026-03-27T03:54:49.241000+00:00 | Last Updated: 2026-03-27T06:42:41.424887+00:00
**Daily Work Briefing: Smart Cart x RMN Catchup (Mar 27)**

**Key Participants & Roles**
*   **Nikhil Grover:** Focuses on onsite (app and web) initiatives; previously managed retail out-of-home scope.
*   **Ching Hui Ng:** Meeting organizer/lead.
*   **Yi Hao:** New owner of the retail out-of-home scope (replacing Nikhil).

**Main Topic**
Discussion regarding the status, agenda, and necessity of a scheduled virtual meeting on "Smart Cart x RMN Catchup." The conversation confirmed a lack of immediate readiness for Smart Cart integration.

**Decisions Made**
*   **Meeting Cancellation:** Ching Hui Ng has officially cancelled the scheduled catch-up meeting for March 27.
*   **Strategic Pivot:** The team will prioritize "scale" efforts over the Smart Cart integration at this time.
*   **Stakeholder Alignment:** Future communications regarding retail out-of-home scope and Smart Cart will involve Yi Hao instead of Nikhil Grover.

**Pending Actions & Ownership**
*   **Action:** Re-liaise on the Smart Cart project when bandwidth permits.
    *   **Owner:** Ching Hui Ng (to coordinate with Yi Hao).
*   **Action:** Incorporate Yi Hao into future discussions regarding retail out-of-home scope.
    *   **Context:** Nikhil has handed over this specific scope to Yi Hao to accelerate progress while he focuses on onsite work.

**Key Dates & Follow-ups**
*   **Original Meeting Date:** March 27, 2026 (Cancelled).
*   **Next Step:** No specific date set; follow-up will occur once bandwidth allows.
*   **Contextual Note:** The decision to pause was driven by the absence of business requirements and an unidentified vendor for Smart Cart integration on the Osmos side.


## [40/70] DPD All Leads
Source: gchat | Group: space/AAAAQezbuRE/KePJESgRBP8 | Last Activity: 2026-03-27T03:09:22.595000+00:00 | Last Updated: 2026-03-27T06:44:57.953915+00:00
**Daily Work Briefing: DPD All Leads Chat Summary (Update)**

**Key Participants & Roles:**
*   **Vincent Wei Teck Lim:** Initiated inquiry; confirmed intent to create a new SDK key; acknowledged short notice.
*   **Jazz Tong:** Provided strategic direction; suggested reverse engineering code for iOS/Android SDKs and advised checking Harness FF SDK compatibility; noted Split API is still functional but migration is pending long-term harmonization.
*   **James Lai Li Hao:** Clarified terminology ("browser key" = client key); shared a legacy Confluence page regarding feature flags and environment guidelines.
*   **Flora Wo Ke:** Engaged in clarifying the request scope; noted familiarity with Jazz's suggestion on reverse engineering.
*   **Komal Ashokkumar Jain:** Highlighted critical time pressure (request received last evening, deadline earlier today morning).
*   **Winson Lim:** Acknowledged incoming external replies.

**Main Topic:**
Creation of a new Split SDK key for the "Everything Food" implementation on OneApp and validation of current vs. legacy integration methods following Split.io's partial migration to Harness.

**Decisions & Clarifications Made:**
*   **Terminology Update:** James Lai Li Hao clarified that the previously discussed "browser key" is synonymous with the "client key."
*   **Technical Path Forward:** Jazz Tong proposed using AI for reverse engineering existing code to generate new iOS/Android SDKs for OneApp as an immediate workaround.
*   **Legacy vs. Current State:** Jazz Tong confirmed Split.io API remains functional; however, a full migration to Harness FF SDK is ongoing and not yet complete.
*   **Documentation Alignment:** Vincent Wei Teck Lim confirmed the team is currently reviewing the shared Confluence page regarding client-side browser keys.

**Pending Actions & Ownership:**
*   **Urgent Resolution:** The team must resolve the new key generation by today morning, despite the short notice (received last evening).
*   **SDK Generation:** Vincent Wei Teck Lim to proceed with generating the key, potentially utilizing Jazz Tong's suggestion of reverse engineering code if standard methods are delayed.
*   **Harness Validation:** Komal Ashokkumar Jain and Jazz Tong to verify if the new Harness Feature Flag (FF) SDK is usable for this specific requirement.
*   **Documentation Review:** Team to finalize review of the Confluence page: *Split.io feature flags and environment guidelines*.
*   **Communication:** Vincent Wei Teck Lim apologized for the short notice and committed to minimizing such occurrences in the future.

**Key References & Dates:**
*   **Date of Discussion:** March 27, 2026 (01:43 – 03:09 UTC).
*   **Legacy Reference:** "Koklin" identified by Vincent and James as a potential original creator ("he is the bible").
*   **Resources Cited:**
    *   *Confluence Page:* https://ntuclink.atlassian.net/wiki/spaces/DPD/pages/2000585047/Split.io+feature+flags+and+environment+guideliens (Shared by James Lai Li Hao; referenced as "long lost" by OKTA).
    *   *Harness Developer Hub:* Before and After Guide: API for Split Admins.

**Status:** **Critical/Urgent**. The team has pivoted from historical investigation to immediate execution under tight time constraints. Jazz Tong's suggestion to use AI reverse engineering or verify Harness FF SDK compatibility serves as the primary alternative path while the standard key creation process is validated against the legacy Confluence documentation.


## [41/70] DPD Incidents
Source: gchat | Group: space/AAAAEsAEG84 | Last Activity: 2026-03-27T02:58:14.109000+00:00 | Last Updated: 2026-03-27T06:45:45.235596+00:00
**Daily Work Briefing: DPD Incidents – HCBP Picking Queue Issue**

**Key Participants & Roles**
*   **Ler Whye Ling Angel:** Initiator of the incident report; flagged a critical operational blocker.
*   **Gopalakrishna Dhulipati:** Key participant in the 17-reply thread discussing the issue (Role inferred as technical support or operations lead).
*   **Winson Lim:** Key participant in the 17-reply thread discussion (Role inferred as technical support or operations lead).

**Main Topic/Discussion**
The conversation centers on a system outage where **no orders are appearing in the picking queue for HCBP**. Angel flagged this issue at **2026-03-27T02:58:14.109Z**, stating, "Please assist as there is no order in the picking Q till now for HCBP." The thread generated significant engagement (17 replies) and concluded with a follow-up discussion at **04:54 AM**.

**Pending Actions & Ownership**
*   **Action:** Investigate and resolve the root cause of missing orders in the HCBP picking queue.
*   **Action:** Restore order flow to allow picking operations to proceed for HCBP.
*   **Ownership:** The issue was directed at **Gopalakrishna Dhulipati** and **Winson Lim** via tag, indicating they are responsible for troubleshooting and resolution.

**Decisions Made**
No explicit decisions or resolutions were recorded in the provided metadata snippet; however, the engagement of two specific team members indicates an active investigation into the queue failure is underway.

**Key Dates & Deadlines**
*   **Incident Reported:** 2026-03-27, 02:58:14 UTC.
*   **Last Activity:** 04:54 AM (Timezone not specified in snippet; assumed local to chat space).
*   **Thread Duration:** Approximately 2 hours of active discussion and reply activity.

**Contextual References**
*   **Resource Name:** DPD Incidents.
*   **Space URL:** https://chat.google.com/space/AAAAEsAEG84.
*   **Specific System Issue:** "No order in the picking Q" for HCBP.


## [42/70] DPD x DPM
Source: gchat | Group: space/AAQApzD7Im0 | Last Activity: 2026-03-27T02:51:56.638000+00:00 | Last Updated: 2026-03-27T06:46:35.745254+00:00
### Daily Work Briefing: DPD x DPM Collaboration Space (Updated)

**Key Participants & Roles**
*   **Daryl Ng:** Tech Lead; flagged CHAS calculation issues. Tagged regarding Gamification ownership, delivery logic, and urgent ticket status updates for the OMNI review.
*   **Rajesh Dobariya:** Inquired about Gamification data and "Normal" vs. "Express" display logic. Initiated "1HD Business testing." Recently flagged a discrepancy where tickets are ready for UAT (per Zaw) but show 0% completion status. Urged Daryl Ng to update ticket statuses by the afternoon OMNI review, noting Andin is on leave.
*   **Andin Eswarlal Rajesh:** Previously initiated "1HD Business testing" (March 25). Currently on leave; unable to update ticket statuses as of March 27.
*   **Vivian Lim Yu Qian:** Driving mandates (MTI price per piece) and SWA migration history.
*   **Zaw:** Credited with confirming tickets are ready for UAT.

**Main Topics**
1.  **Ticket Status Discrepancy (Critical):** Rajesh Dobariya identified a critical status mismatch on March 27. Tickets are reportedly "ready for UAT" according to Zaw, yet the system tracks them at **0% done**. Immediate correction is required before the afternoon OMNI review.
2.  **Delivery Text Logic:** Daryl Ng requested a breakdown of the *existing* logic for displaying "orange label" text on Omni and OG homepages (March 25). Last reply pending from Yangyu Wang & Zi Ying Liow as of March 25, 01:34 AM.
3.  **Gamification Data Requirements:** CRM team requires specific BigQuery data points for PNS automation. Needs confirmation on existing data or effort estimation for pushing new data.
4.  **Govt Mandate (MTI):** Implementation of "Price per Piece" info for 40+ categories in the current app MVP.
5.  **CHAS Calculation Bug:** UI discrepancy where cart-level discounts split at the sales order level affect CHAS calculations (`DPD-530`).
6.  **SWA Migration:** Investigation into reverting SWA ad serving from Publitas back to Wordpress (`DIS-585`).

**Pending Actions & Ownership**
*   **Ticket Status Update (Urgent):** Correct ticket status from 0% to "Ready for UAT" by the afternoon OMNI review on March 27. *Owner: Daryl Ng (Rajesh Dobariya requested; Andin on leave).*
*   **Orange Label Logic Clarification:** Share and document existing logic for Omni/OG homepages regarding text variables. *Owner: Daryl Ng.*
*   **Gamification Data Query:** Clarify ownership of Gamification features and provide BQ table/column names or confirm data push needs. *Owner: Daryl Ng.*
*   **Tech Lead Confirmation:** Determine lead ownership for Price per Piece expansion. *Owner: Vivian Lim Yu Qian / Team.*
*   **1HD Testing Follow-up:** Review the 8 replies regarding Andin's "1HD Business testing" initiation. *Owner: Rajesh Dobariya / Team.*

**Decisions Made**
*   No formal decisions recorded yet; however, a consensus exists that ticket statuses require immediate correction to reflect UAT readiness before the OMNI review. The intent to fix the CHAS bug via API update remains established. Implementation details for the "orange label" text are pending Daryl Ng's input.

**Key Dates & Deadlines**
*   **March 27, ~02:50 AM:** Rajesh Dobariya notes tickets are ready for UAT (per Zaw) but show 0% done; flags need for status update.
*   **March 27, ~03:02 AM:** Rajesh tags Daryl Ng to update statuses by the afternoon OMNI review, noting Andin is on leave.
*   **March 25, 06:59 AM:** Andin Eswarlal Rajesh initiates "1HD Business testing" discussion.
*   **March 25, 01:34 AM:** Daryl Ng requests clarification on orange label display logic.

**Reference Links**
*   Price Per Piece Wiki: `https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008175965/Price+Per+Piece+Multipack+in+Display+Unit`
*   CHAS Ticket: `DPD-530`
*   Sticky Header UI Ticket: `ENGM-2501`
*   SWA Migration Ticket: `DIS-585`


## [43/70] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/GjGHRIi5T-E | Last Activity: 2026-03-27T02:33:15.491000+00:00 | Last Updated: 2026-03-27T06:47:20.607035+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles:**
*   **Prajney Sribhashyam:** Requester of E2E production test; clarifies deployment urgency and adds @De Wei Tey to the refund discussion.
*   **Sneha Parab:** Reports on MP order sync issues, revert status, and identifies additional participants needed for refund/GI discussions.
*   **Andin Eswarlal Rajesh, Daryl Ng:** Tagged for testing; identified by Sneha as potential attendees for the refunds workflow discussion.
*   **De Wei Tey:** Newly added participant to the refund discussion thread.

**Main Topic:**
Coordination of an End-to-End (E2E) production test scheduled for March 27, 2026, covering App Experience, Order Placing, and Order Posting. The focus shifted from testing MP order sync fixes immediately to prioritizing a separate alignment session on refunds and GI adjustments, while ensuring the deployed fix addresses overnight BCRS unit count and price info issues in DF reports.

**Pending Actions & Owners:**
*   **Deploy Sync Fix:** Sneha has a tested fix for MP order sync (reverting the change causing errors). Prajney confirmed this is "not needed" for the current E2E test but instructed to get the fix deployed soon.
*   **Refunds & GI Alignment Session:** A specific discussion is required regarding refunds still in UAT and their integration with General Inventory (GI) adjustments. Sneha needs to confirm if @Daryl Ng requires additional attendees; Prajney confirmed adding @De Wei Tey to this call.
*   **Validate Reversal Process:** Alignment remains required between Prajney and Adrian regarding order return and stock reversal processes, previously raised in the Deployment Planning Session with Onkar.

**Decisions Made:**
*   **Test Scope Adjustment:** The MP order sync fix (BCRS unit count & price info) is excluded from the immediate E2E production test scope to avoid surprises on production, though it must be deployed soon.
*   **Deployment Strategy:** The team reverted the change causing nightly sync issues immediately. A separate deployment for the available fix will occur after further validation and alignment on refunds, rather than as part of the main test run.
*   **Meeting Expansion:** The refund discussion meeting will include @De Wei Tey in addition to existing stakeholders.

**Key Dates, Deadlines, and Follow-ups:**
*   **March 27, 2026 (01:17):** Sneha reported MP order sync issues and confirmed the revert.
*   **March 27, 2026 (02:31):** Prajney clarified that the fix is not needed for the current test but must be deployed soon.
*   **March 27, 2026 (02:32):** Sneha confirmed alignment needs to prevent production surprises and queried additional call attendees.
*   **March 27, 2026 (02:33):** Prajney added @De Wei Tey to the refund discussion thread.
*   **Immediate Follow-up:** Schedule a session between Prajney, Adrian, Daryl Ng, and De Wei Tey to align on the refund/reversal workflow before finalizing deployment attempts.

**Link:** [BCRS Firefighting Group Chat](https://chat.google.com/space/AAQAgT-LpYY)


## [44/70] @omni-ops #standup - Mar 27
Source: gchat | Group: space/AAQAz751zBQ | Last Activity: 2026-03-27T02:02:10.051000+00:00 | Last Updated: 2026-03-27T02:42:34.236887+00:00
**Daily Work Briefing: #standup Channel**
**Date:** March 27, 2026
**Source:** Google Chat (#omni-ops)

**1. Key Participants and Roles**
*   **Yangyu Wang:** Initiator of the standup check-in (Role inferred as team member or lead initiating daily sync).
*   **Audience/Participants:** "Viewed by 5 of 8" indicates an active channel presence, though specific roles for the other viewers are not explicitly stated in this log.

**2. Main Topic/Discussion**
The conversation consisted of a single query regarding the status or initiation of the daily standup meeting. No substantive project updates, blockers, or technical discussions were recorded in this snapshot.

**3. Pending Actions and Ownership**
*   **Action:** Commence the standup meeting.
    *   **Owner:** Unclear/Unassigned (The initiator, Yangyu Wang, asked "standup?" but did not assign a specific facilitator in this message).
    *   **Status:** Pending initiation based on the query.

**4. Decisions Made**
*   No formal decisions were recorded in this conversation log. The interaction remains an open inquiry.

**5. Key Dates, Deadlines, and Follow-ups**
*   **Event Date/Time:** March 27, 2026, at 02:02:10 UTC.
*   **Follow-up Required:** Confirmation of standup status or the start of the meeting itself to ensure the team sync proceeds as scheduled.

**Summary Note:** The log reflects a single timestamped message from Yangyu Wang prompting for the daily standup. Further details regarding project status, blockers, or outcomes are not available in this specific conversation excerpt.


## [45/70] [BCRS]-SAP to POS & DBP Interface Deployment
Source: gchat | Group: space/AAQAeMC3qBk/3a5kvSWZa-g | Last Activity: 2026-03-27T01:46:35.052000+00:00 | Last Updated: 2026-03-27T02:43:08.464635+00:00
### Daily Work Briefing: [BCRS]-SAP to POS & DBP Interface Deployment

**Key Participants & Roles**
*   **Michael Bui:** Execution lead; confirmed initial deployment success but noted no BCRS deposit data is currently available in PRD.
*   **Onkar Bamane:** Stakeholder/Coordinator; managing the smoke test strategy and liaising between SAP, DBP, and MP teams.
*   **Sneha Parab:** Point of contact for MP (Mirakl); coordinating testing schedules and stakeholder comms regarding deposit SKUs.
*   **Hendry Tionardi:** Technical analyst; identified the root cause as an empty database table awaiting data population on April 1st.
*   **Shiva Kumar Yalagunda Bas:** Reported initial failure to update SAP product names for specific MP SKUs.
*   **Olivia -:** Involved in downstream impact assessment regarding POS charging before April 1st.

**Main Topic**
Post-deployment monitoring of the **[BCRS]-SAP to POS & DBP Interface**. While the deployment itself was error-free, immediate issues arose regarding missing BCRS deposit data for MP SKUs, preventing successful product updates and linking. The focus shifted from general monitoring to troubleshooting a data availability gap between SAP production tables and downstream systems.

**Pending Actions & Owners**
*   **Smoke Test Setup:** Onkar Bamane will maintain one dummy SKU (for 1, 6, and 12 qty) temporarily for testing purposes; it will be removed post-test.
    *   *Owner:* Onkar Bamane
*   **MP SKU Creation Testing:** Sneha Parab to inform PIC availability on Mirakl to create a dummy SKU for the smoke test. A meeting is scheduled for March 27 at 11:00 UTC.
    *   *Owners:* Sneha Parab, Hendry Tionardi, Onkar Bamane
*   **Data Synchronization:** Wait for full BCRS deposit data to be maintained in SAP on the afternoon of March 31, 2026. MP BCRS SKU approval cannot proceed until then.
    *   *Owner:* Sneha Parab (to inform Cheryl & Amos)

**Decisions Made**
*   The initial deployment at 14:20 UTC on March 26 was successful; however, the system currently shows no deposit SKUs in SAP because the source table is empty.
*   The empty table state is expected to resolve on **April 1st**, when data population occurs.
*   A temporary workaround (maintaining a single test SKU) was approved by Onkar Bamane to allow smoke testing before full data availability.
*   MP BCRS SKU approval processes are paused pending the March 31 data maintenance window.

**Key Dates & Follow-ups**
*   **Deployment Date:** March 26, 2026, at 14:20 UTC.
*   **Data Availability Timeline:** Full data maintained on March 31 afternoon; table populates April 1.
*   **Smoke Test Meeting:** March 27, 2026, at 11:00 UTC (Google Meet link provided by Sneha Parab).
*   **Next Update:** Sneha Parab to confirm PIC availability for dummy SKU creation and provide alignment steps before the test meeting.

**Resource Reference**
*   **Chat URL:** https://chat.google.com/space/AAQAeMC3qBk


## [46/70] DPD All Leads
Source: gchat | Group: space/AAAAQezbuRE | Last Activity: 2026-03-27T01:43:42.350000+00:00 | Last Updated: 2026-03-27T02:43:31.929104+00:00
**Daily Work Briefing: DPD All Leads Space**

**Key Participants & Roles**
*   **Vincent Wei Teck Lim:** Lead (Inquired on CNY support migration; Investigating SDK key history).
*   **Natalya Kosenko:** Lead (Proposed Zendesk group update strategy).
*   **Alvin Choo:** Lead (Raised HR performance feedback protocol).
*   **Tan Nhu Duong:** Lead/Informant (Provided critical calibration rating visibility warning).
*   **Michael Bui:** Team Member/Analyst (Flagged data spike anomaly).
*   **Winson Lim:** Lead/New Inquiry (Raised food tile decommissioning concerns).
*   **Komal Ashokkumar Jain:** Identified as the likely owner of the split SDK key creation.

**Main Topics & Discussions**
1.  **CNY Support Transition (Mar 2):** Vincent raised the question of migrating on-call support from temporary resources to the core team as CNY support concludes.
2.  **Zendesk Group Management (Mar 4):** Natalya discussed updating Zendesk groups for Gomathi, proposing a centralized email notification rather than individual adhoc requests.
3.  **HR Performance Feedback & Reporting Lines (Mar 4–10):** Alvin requested guidance on inviting both old and new Reporting Officers (ROs) to 1-on-1 performance feedback sessions due to recent reporting line changes. Tan subsequently warned that former managers cannot see final calibrations; only the *new* RO sees the final rating.
4.  **Data Anomaly Investigation (Mar 16):** Michael identified a sudden spike in `popup_myinfo_unverified` events within Segment data specifically on March 13, seeking verification and contact points for resolution.
5.  **Food Tile & Service Decommissioning (Mar 20 – Mar 27):**
    *   On **Mar 20**, Winson Lim noted the discontinuation of the food tile due to recent events and raised concerns regarding associated service decommissioning.
    *   On **Mar 27**, Vincent Wei Teck Lim initiated an inquiry to identify the specific individual responsible for creating the split SDK key during the initial implementation of the "everything food" feature, tagging @all and receiving a response from Komal Ashokkumar Jain.

**Decisions Made**
*   None explicitly recorded as final decisions in the provided snippets. Discussions remain in inquiry or information-sharing phases regarding support migration, notification strategy, feedback protocols, data validation, service decommissioning, and SDK key history.

**Pending Actions & Owners**
*   **Confirm CNY Support Migration Plan:** Owner: TBD (Vincent initiated). Needs confirmation on whether to migrate to the core team.
*   **Finalize Zendesk Update Strategy:** Owner: Natalya/Kosenko. Decision needed on executing a centralized email vs. adhoc updates for Gomathi's group access.
*   **Verify Final Performance Ratings:** Action: Old ROs must consult new ROs before communicating final ratings to avoid discrepancies (e.g., Green+ vs. Gold). Owner: All Managers/Leads involved in feedback sessions.
*   **Investigate Segment Data Spike:** Owner: TBD/Michael Bui. Requires identifying the source of the `popup_myinfo_unverified` spike on 13/03 and verifying with the relevant team.
*   **Assess Food Tile & Service Decommissioning:** Owner: TBD (Winson Lim initiated). Needs strategic input on whether to proceed with decommissioning services linked to the food tile following its removal.
*   **Document Split SDK Key History:** Action: Verify Komal Ashokkumar Jain's involvement or identify the original creator of the split SDK key for "everything food" to aid in potential decommissioning or troubleshooting efforts. Owner: Vincent Wei Teck Lim (Lead inquiry).

**Key Dates & Deadlines**
*   **Mar 2, 2026:** CNY support close inquiry raised.
*   **Mar 4, 2026:** Zendesk update discussion; HR performance feedback month begins.
*   **Mar 13, 2026:** Date of the Segment data spike requiring investigation.
*   **March (Ongoing):** HR Performance Feedback Month (1-on-1s).
*   **Mar 20, 2026:** Winson Lim raised food tile and service decommissioning inquiry.
*   **Mar 27, 2026:** Vincent Wei Teck Lim inquired about the split SDK key creator; Komal Ashokkumar Jain replied to the thread.


## [47/70] [BCRS]-ECOM Flow Deployment - Mar 27
Source: gchat | Group: space/AAQAPK5pWxQ | Last Activity: 2026-03-26T16:11:02.982000+00:00 | Last Updated: 2026-03-27T02:57:53.151637+00:00
**Daily Work Briefing: [BCRS]-ECOM Flow Deployment**

**Key Participants & Roles**
*   **Shiva Kumar Yalagunda Bas:** Reported deployment failure status. (Note: Participant role inferred as technical lead or engineer based on monitoring activity).
*   **Unspecified Team Members:** 9 out of 11 participants viewed the conversation, indicating broad team visibility on the incident.

**Main Topic**
Investigation and reporting regarding a recurring failure in the **[BCRS]-ECOM Flow Deployment**. The discussion centers on a specific timestamp where the deployment process failed to complete successfully.

**Status & Actions Pending**
*   **Issue Confirmation:** A deployment failure was confirmed occurring at **12:05 am**.
*   **Owner:** **Shiva Kumar Yalagunda Bas** identified the failure but no further resolution steps or ownership for remediation is explicitly stated in the provided log.
*   **Next Steps:** Immediate dependency on root cause analysis to address why the flow fails at this specific time slot (12:05 am).

**Decisions Made**
*   No formal decisions, approvals, or strategic pivots were recorded in this 7-minute exchange. The interaction was limited to status reporting.

**Key Dates & Deadlines**
*   **Failure Timestamp:** **12:05 am** (Time of deployment failure).
*   **Report Date:** **March 26, 2026**.
    *   Failure reported at **16:06:24 UTC**.
    *   Message viewed by team at **16:11:02 UTC**.
*   **Reference Document:** "Resource: [BCRS]-ECOM Flow Deployment - Mar 27" (Note: The resource title suggests the deployment is targeted for or associated with March 27, while the incident occurred on March 26).

**Summary of Incident**
On March 26, 2026, Shiva Kumar Yalagunda Bas reported that the [BCRS]-ECOM Flow Deployment "still fails" specifically at **12:05 am**. The issue appears to be a recurring problem given the use of the word "still." The conversation was visible to the majority of the team (9/11 members) shortly after being posted. No resolution or corrective action plan is currently documented in this specific chat segment.


## [48/70] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4 | Last Activity: 2026-03-26T14:39:28.616000+00:00 | Last Updated: 2026-03-27T02:59:01.520039+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Space Creator; Lead coordinating the briefing.
*   **Daryl Ng, Gopalakrishna Dhulipati, Tiong Siong Tee, Michael Bui, Akash Gupta:** Designated "Project Light Attack and Defence Leads".
*   **Hui Hui Voon:** Owner of the D&T Scope for Project Light Workshop document.
*   **Pauline Pong:** Owner of promotion conflict test case file.
*   **Jacob Yeo:** Edited CDTO Internal RFP requirements file on March 25, 2026.
*   **Sophia:** Contacted by Michael Bui regarding CoMall coordination (March 26).

**Main Topic**
Following the transition to active strategic planning ("Room 2") on March 24, the team is finalizing specific slide preparation within six "Spotlight Topics." While Alvin Choo initiated collaboration on **"RMN"** and **"Payment"** slides on March 24, a new flexibility protocol was established on March 25 allowing leads to attend other meetings (e.g., BCRS) if required. Concurrently, technical direction has shifted toward decoupling from SAP, with consensus that SAP should serve primarily for finance and sales records purposes. New RFP documentation and promotion conflict testing cases have been identified for review. On March 26, the discussion expanded to data infrastructure specifics and CoMall integration strategy. Michael Bui reported a preliminary chat with Sophia on March 26 regarding early engagement with CoMall teams to kickstart development.

**Pending Actions & Ownership**
*   **Action:** Finalize content for "RMN" and "Payment" slides in the D&T Scope document.
    *   **Ownership:** Alvin Choo (initiated), Hui Hui Voon (Document Owner).
    *   **Status:** In progress; collaboration initiated March 24, ~9:32 AM UTC.
*   **Action:** Review "Promotion Conflict Test Case_05.NOV.20" and summarize the file for Alvin Choo.
    *   **Ownership:** Michael Bui (requested by Alvin Choo on March 25, ~2:46 AM UTC). Note: Access was initially denied to Alvin Choo on March 25, 2:51 AM UTC.
*   **Action:** Review "[CDTO Internal] Project Light Requirements for RFP by MVP Scope.xlsx".
    *   **Ownership:** Gopalakrishna Dhulipati (Owner). Jacob Yeo edited this file on March 25, 2026. Alvin Choo shared the link on March 25, ~3:56 AM UTC for summary.
*   **Action:** Clarify backend API responsibilities with CoMall regarding personalization and orchestration.
    *   **Ownership:** Michael Bui (to note and document).
*   **Action:** Identify the owner managing data indexing to Algolia.
    *   **Ownership:** Daryl Ng raised this query on March 26, ~1:55 AM UTC; team response pending in chat space (10 replies noted).
*   **Action:** Finalize the Attack/Defence team composition pending Dennis's confirmation following Alvin Choo's email.
    *   **Ownership:** Alvin Choo.
*   **Action:** Address technical clarifications raised by Tiong Siong Tee regarding Inventory visibility, Corporate Control alignment, and Product management portal structure (FP vs. Sellers).
    *   **Ownership:** Alvin Choo and Gopalakrishna Dhulipati.
*   **New Action:** Confirm CoMall contract status and determine timing for creating a dedicated GChat space with CoMall teams.
    *   **Ownership:** Michael Bui (initiated inquiry on March 26, ~14:39 UTC); pending confirmation from Alvin Choo or Gopalakrishna Dhulipati regarding "grooming next week" vs. immediate kickoff.

**Decisions Made**
*   **Session Protocol:** Participants are encouraged to listen during live sessions; questions should be raised in the chat space.
*   **Meeting Flexibility:** Leads attending this project may prioritize other critical meetings (e.g., BCRS) if necessary, as confirmed by Alvin Choo on March 25.
*   **Platform Resilience:** Integration testing is a strict technical requirement prioritized from "Day 1."
*   **Governance Structure:** FPG cannot be treated merely as a standard seller due to governance conflicts; distinct data structures or models are required for FP vs. non-governance sellers (Clarified by Gopalakrishna Dhulipati).
*   **System Architecture:** SAP integration should be decoupled from core operational logic; it is designated strictly for finance and sales records purposes (Agreed by Tiong Siong Tee on March 25, aligning with Rock's prior position).
*   **Gamification:** Confirmed not part of the DSP scope.

**Key Dates & Follow-ups**
*   **Slide Collaboration Initiated:** March 24, 2026 (~9:32 AM UTC) – Alvin Choo requested work on RMN and Payment slides.
*   **SAP Decoupling Consensus:** March 25, 2026 (1:36 AM UTC) – Tiong Siong Tee agreed to limit SAP usage to finance/sales records.
*   **Meeting Flexibility Policy:** March 25, 2026 (1:31 AM UTC) – Alvin Choo authorized attendance at other meetings like BCRS.
*   **RFP File Sharing & Review Request:** March 25, 2026 (~3:56 AM UTC) – Alvin Choo shared the "Project Light Requirements for RFP by MVP Scope" file.
*   **Test Case Identification:** March 25, 2026 (~2:46 AM UTC) – Michael Bui identified "Promotion Conflict Test Case_05.NOV.20" (Owner: Pauline Pong); Alvin Choo noted access issues at ~2:51 AM UTC.
*   **Algolia Indexing Query:** March 26, 2026 (~1:55 AM UTC) – Daryl Ng asked "who is managing the indexing of the data to Algolia?" with 10 replies recorded.
*   **CoMall Strategy Inquiry:** March 26, 2026 (14:39 UTC) – Michael Bui queried contract confirmation and GChat creation timing following a chat with Sophia; discussion currently active with 9 replies.
*   **Session Start ("Room 2"):** March 24, 2026 (1:02 AM UTC).
*   **Spotlight Topics List Published:** March 24, 2026 (3:14 AM UTC).
*   **Email Sent for Team Confirmation:** March 24, 2026 (3:51 AM UTC) by Alvin Choo.


## [49/70] GE Connect
Source: gchat | Group: space/AAQASkvSlwo | Last Activity: 2026-03-26T14:32:33.384000+00:00 | Last Updated: 2026-03-27T03:00:23.936000+00:00
**Daily Work Briefing: GE Connect – Polly Launch & Incident Report**

**Key Participants & Roles**
*   **Sip Khoon Tan:** Announcer/Presenter; introduced the AI agent "Polly."
*   **Oktavianer Diharja:** Identified a critical functional issue regarding agent routing.
*   **Sunny Lim:** Reported UI limitations in the NotebookLM studio interface.
*   **Team (GE FPG):** Primary audience and users experiencing reported incidents.

**Main Topic & Discussion**
The discussion centers on the launch of **Polly**, an AI agent for FPG Policy Assistance, alongside newly identified technical failures in both routing logic and user interface capabilities.
*   **Launch Overview:** Polly is designed to streamline policy inquiries via instant answers and source citations through the Workbench (`work.fpg.sg`).
*   **Incident Report 1 (Routing):** On March 26, 2026, Oktavianer Diharja reported a hallucination where the GE workflow incorrectly routed queries from the "Confluence agent" to the "Jira agent," yielding misleading responses.
*   **Incident Report 2 (UI/Feature Limitation):** Sunny Lim noted that the NotebookLM studio tab is restricted to only four types and lacks an "Infographic" option, limiting content creation capabilities.

**Decisions Made**
*   **Deployment Strategy:** Polly remains the primary interface for policy questions, though adoption is currently on hold pending fixes.
*   **Access Routing:** Access is routed through the Workbench (`work.fpg.sg`) and Vertex AI Search.
*   *Update:* Reliability of cross-agent routing (Confluence to Jira) is compromised. Additionally, the NotebookLM studio interface requires feature expansion to include Infographic generation.

**Pending Actions & Owners**
*   **Action:** Investigate routing logic error causing Confluence-to-Jira switch and misleading responses.
    *   **Owner:** Engineering/Development Team.
*   **Action:** Validate accuracy of Jira agent's response regarding Oktavianer Diharja's specific case.
    *   **Owner:** Technical Lead / SMEs.
*   **Action:** Investigate and resolve the missing "Infographic" option in NotebookLM studio to expand the four available types.
    *   **Owner:** Engineering/Development Team (NotebookLM Integration).
*   **Action:** Test functionality for both routing stability and UI completeness before full team reliance.
    *   **Owner:** All team members (pending resolution of bugs/features).

**Key Dates & Follow-ups**
*   **Original Launch Date:** March 20, 2026.
*   **Incident Report Date (Routing):** March 26, 2026 (11:56 AM UTC).
*   **UI Issue Reported:** March 26, 2026 (approx. 2:32 PM UTC per metadata timestamp).
*   **Last Reply Time:** 8:22 AM (Current thread activity); Latest UI discussion reply at 1:07 AM.
*   **Reference URL:** `https://chat.google.com/space/AAQASkvSlwo`
*   **Direct Access Links:**
    *   Polly Agent Link: `http://vertexaisearch.cloud.google.com/home/cid/7c7eb665-e9c4-4276-ab72-3269644e5a4b/r/agent/14958526149084864719/session/-?pli=1`
    *   Workbench Portal: `http://work.fpg.sg`

**Status**
The initiative is **active but interrupted by multiple critical incidents**. While launched on March 20, 2026, adoption is stalled due to a reported hallucination involving agent switching (Confluence to Jira) and misleading data. Furthermore, the NotebookLM studio interface has been flagged for having only four content types, specifically missing an "Infographic" option. The chat log indicates unresolved technical debt with 3 unread items and multiple replies regarding these specific issues. Full team adoption remains on hold until routing logic is corrected and the UI feature gap (Infographics) is addressed.


## [50/70] OMS x CS
Source: gchat | Group: space/AAAAUPoVWjI | Last Activity: 2026-03-26T13:32:52.621000+00:00 | Last Updated: 2026-03-26T14:38:08.188942+00:00
**Daily Work Briefing: OMS x CS Resources (Updated)**

**Key Participants & Roles**
*   **Sampada Shukla:** Customer Support (CS) agent.
*   **Wai Ching Chan:** CS representative flagging operational process gaps regarding customer profile merging.
*   **Raine Lee:** CS representative reporting notification delivery failures, including a new NPS feedback loop.
*   **Gomathi Panneerselvam & Gopalakrishna Dhulipati:** IT/Operations personnel involved in resolving reported issues.
*   **Binte Abdul Karim Kamilah:** CS agent escalating billing discrepancy inquiries from the GCEO channel.

**Main Topics**
1.  **Access Control:** Critical lockout of CS agent Sampada Shukla from Zendesk due to MFA/SMS 2FA failures (March 4). Resolution pending.
2.  **Process Integrity:** Recurring disruption caused by merging customer profiles without validating pending orders, leading to stalled workflows (Orders #255985725 and others).
3.  **System Reliability & Billing Discrepancies:**
    *   Historical failure of SMS/PNS delivery for Order #256547454 (March 12).
    *   Missing order confirmation emails for Orders #257969203, #257279251, and #256369211 (Ticket #4449487), linked to an NPS survey submission.
    *   **New Incident:** Customer complaint via GCEO regarding unjustified charges for drop-off items in Order #256906035. The invoice reflected a charge of $93.50 for Item 491697 (Haagen-Dazs Ice Cream - Strawberry, Qty 6), despite DBP logs and internal records confirming the item was marked as "drop off" and fully fulfilled.

**Pending Actions & Ownership**
*   **Reset MFA:** IT support must reset Sampada Shukla's Multi-Factor Authentication immediately to restore Zendesk access. (*Owner: IT Team*)
*   **Process Validation Protocol:** CS and Customer Data Management (CDM) teams need to implement a mandatory validation check for open/pending orders before executing customer profile merges. (*Owner: CS & CDM Teams*)
*   **Investigate Email Delivery Failure:** Verify backend logs for Ticket #4449487 to confirm successful dispatch of order confirmation emails for the three affected orders (#257969203, #257279251, #256369211). Compare against historical delivery metrics. (*Owner: Technical/Operations Team*)
*   **Investigate Notification Failure (Legacy):** Proceed with technical review for SMS/PNS triggers failing on Order #256547454 (Customer: btsoh268@gmail.com) as previously planned. (*Owner: Technical/Operations Team*)
*   **Investigate Billing Discrepancy:** Review Invoice vs. DBP Logs for Order #256906035 to explain the $93.50 charge on drop-off item 491697 and respond to the customer's GCEO request. (*Owner: Operations/Billing Team*)

**Decisions Made**
*   No formal decisions recorded in the chat log; however, **Wai Ching Chan** explicitly identified a systemic risk requiring a protocol change between CS and CDM to prevent future order processing blocks during profile merges.
*   **New Context:** The NPS survey submission for Ticket #4449487 elevates the email delivery issue from a routine check to a customer satisfaction concern requiring priority verification.
*   **Escalation Protocol:** Binte Abdul Karim Kamilah has escalated the billing anomaly in Order #256906035 due to its origin from a GCEO inquiry, necessitating immediate root cause analysis of the charge logic failure.

**Key Dates & References**
*   **March 4, 2026:** Sampada Shukla reported Zendesk lockout (SMS 2FA issue). Last reply recorded March 4 at 4:41 AM.
*   **March 7, 2026:** Customer profile UID `4815537039166279` merged into UID `216353592157999833`, stalling Order #255985725.
*   **March 9, 2026:** Wai Ching Chan escalated the merge issue at 6:13 AM. Last reply recorded Thursday at 11:11 AM.
    *   *Affected Order Link:* `https://admin.fairprice.com.sg/customer-support/sale-orders/255985725`
    *   *Customer Profile Link:* `https://admin.fairprice.com.sg/customer-support/customers/view/1067653`
*   **March 12, 2026:** Raine Lee reported SMS/PNS delivery failure for Order #256547454. Last reply recorded at 12:00 AM.
*   **March 24, 2026 (03:58 AM):** Raine Lee raised Ticket #4449487 regarding missing order confirmation emails for three recent orders (#257969203, #257279251, #256369211). Customer submitted NPS survey. Last reply recorded 5:13 AM.
*   **March 26, 2026 (13:32 UTC):** Binte Abdul Karim Kamilah raised Ticket #4446136 regarding the billing discrepancy for Order #256906035 ($93.50 charge on drop-off item 491697).


## [51/70] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/jG0L_VCljVA | Last Activity: 2026-03-26T13:02:30.327000+00:00 | Last Updated: 2026-03-26T14:38:22.568646+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Meeting/Channel Resource:** [Internal] Digital Product Development Space
**Date of Discussion:** March 26, 2026
**Reference Link:** https://admin.fairprice.com.sg/customer-support/customers/view/2022036

### 1. Key Participants & Roles
*   **Wai Ching Chan:** Issue reporter (Customer Support/Product). Identified the bug affecting order time slot changes for iOS users with emoji in addresses.
*   **Sneha Parab:** Service Owner verification. Currently determining ownership of the `address-service`.
*   **Michael Bui:** Product/Development inquiry. Questioned the technical root cause regarding emoji breaking the flow.
*   **Gopalakrishna Dhulipati & Dang Hung Cuong:** Tagged stakeholders for visibility.

### 2. Main Topic
Investigation into a bug where customer addresses containing **emoji icons** (specifically on iOS) prevent users from changing order time slots, requiring manual resolution in the admin panel. The discussion focuses on validating if emojis are currently blocked during address creation or editing and identifying the service responsible for this logic.

### 3. Pending Actions & Ownership
*   **Action:** Validate whether emoji icons block adding/editing addresses.
    *   **Owner:** To be determined (Immediate follow-up required).
*   **Action:** Identify the current owner of `address-service`.
    *   **Owner:** Sneha Parab (currently investigating).

### 4. Decisions Made
No final decisions or resolutions were reached during this conversation thread. The group is currently in the diagnostic and ownership identification phase.

### 5. Key Dates & Follow-ups
*   **Issue Date:** March 26, 2026.
    *   Initial report: 10:35 UTC (Wai Ching Chan).
    *   Service ownership check initiated: 11:10 UTC (Sneha Parab).
    *   Root cause inquiry raised: 13:02 UTC (Michael Bui).
*   **Follow-up Required:** Confirmation of `address-service` ownership and execution of the emoji validation test.

**Specific References:**
*   **Customer ID:** 2022036
*   **Platform Impact:** iOS users only (reported via admin link).
*   **Impact Scope:** Manual intervention required for order time slot changes.


## [52/70] RMN Incidents
Source: gchat | Group: space/AAQAz11ATzY/JzqdqNaNWpo | Last Activity: 2026-03-26T13:00:42.163000+00:00 | Last Updated: 2026-03-26T14:39:07.311447+00:00
**Daily Work Briefing: RMN Incidents**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator of the incident report; identified a critical product ad performance drop.
*   **Rachit Sachdeva:** Point of contact for internal investigation; confirmed issue acknowledgment.
*   **Michael Bui:** Stakeholder requesting timeline for the next status update.
*   **Other Stakeholders (CC'd):** Shubhangi Agrawal, Allen Umali, Rajiv Kumar Singh, Ravi Goel.

**Main Topic**
A high-priority incident regarding a **50% drop in product ad impressions** since March 17, 2026. The decline is isolated to search and category pages despite stable request/response trends. The root cause hypothesis suggests a reduction in the number of SKUs per response (dropping from 4–5 SKUs to a single product). This anomaly has resulted in an **$11k revenue loss** compared to the previous nine-day period.

**Pending Actions & Ownership**
*   **Action:** Investigate and confirm the hypothesis regarding SKU reduction per response.
*   **Owner:** Rachit Sachdeva (confirmed internal ticket raised).
*   **New Action:** Provide a timeline/status update on the investigation.
*   **Status:** In progress; awaiting next update from Rachit Sachdeva following Michael Bui's inquiry at 13:00 UTC on March 26, 2026.

**Decisions Made**
No final decisions or root cause confirmations were reached during this exchange. The discussion remains in the triage and hypothesis confirmation phase. A follow-up update is now explicitly requested by Michael Bui.

**Key Dates & Follow-ups**
*   **Incident Start Date:** March 17, 2026 (start of impression drop).
*   **Report Date:** March 26, 2026.
    *   Issue raised: 09:40 UTC by Nikhil Grover.
    *   Internal ticket raised: 09:42 UTC by Rachit Sachdeva.
    *   Follow-up request: 13:00 UTC by Michael Bui asking for the next update timeline.
*   **Data Window Cited:** Past 7 days (as of March 26).
*   **Follow-up Required:** Rachit Sachdeva to provide an update on the internal investigation status in response to Michael Bui's query.

**Resource Reference**
*   **Space/URL:** https://chat.google.com/space/AAQAz11ATzY


## [53/70] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE/S2k2gx19hOs | Last Activity: 2026-03-26T10:12:09.136000+00:00 | Last Updated: 2026-03-26T10:44:58.617361+00:00
**Daily Work Briefing: Google Chat Summary**

**Key Participants & Roles**
*   **Nikhil Grover:** Analyzing data trends; identifying risks; driving incident management.
*   **Michael Bui:** Seeking clarification on specific metrics and stakeholder status (OSMSO).

**Main Topic**
Discussion regarding a discrepancy in March 19th data, specifically concerning impression numbers versus the percentage of multi-product responses on the search page, and the decision to escalate a potential revenue-impacting drop.

**Pending Actions & Owners**
*   **Raise Incident:** Nikhil Grover intends to raise an incident immediately due to a significant drop in impressions with revenue implications. He believes waiting for OSMSO feedback is not viable given the impact. (Owner: Nikhil Grover)
*   **OSMSO Data Follow-up:** Both parties are awaiting confirmation from OSMSO regarding specific metrics. (Owner: Pending external response, but ownership lies with both to monitor).

**Decisions Made**
*   **Incident Escalation:** It was agreed that an incident should be raised immediately regarding the drop in impressions, despite missing data from OSMSO. Nikhil Grover explicitly stated, "I think important to raise incident now."
*   **Data Scope Clarification:** Confirmed that the "unchanged" numbers previously discussed referred strictly to the search page impression data for March 19th, which remains stable. The initial confusion arose because Michael Bui was referencing a different metric (percentage of responses containing 2+ products) or a different view (2 pages vs. 1 page).

**Key Dates & Context**
*   **March 19:** The specific date for the data anomaly in question.
*   **March 25:** Nikhil Grover posted "11 replies" (contextual marker).
*   **March 26, 04:27 UTC:** Michael Bui noted numbers for March 19 had been changed.
*   **March 26, 09:20 UTC:** Nikhil clarified that search page impressions for March 19 were actually unchanged and this was not supposed to change.
*   **March 26, 10:04–10:12 UTC:** Clarification regarding OSMSO data; confirmed OSMSO has not yet returned numbers for the "% of 2 or more products in the response."

**Summary Notes**
The conversation clarified that while impression numbers for the search page on March 19 are stable, there is a broader concern regarding dropped impressions impacting revenue. Consequently, the team prioritized raising an incident over waiting for OSMSO to provide specific multi-product response percentage data.


## [54/70] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/yjyq94srBMw | Last Activity: 2026-03-26T10:04:49.922000+00:00 | Last Updated: 2026-03-26T10:45:20.585139+00:00
**Daily Briefing: BCRS Firefighting Group (Re-delivery Use Case)**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Project Lead/Coordinator. Driving timeline clarification and dependency mapping.
*   **Michael Bui:** Developer (Sales Posting). Clarified parallel execution capabilities; noted upcoming leave.
*   **De Wei Tey:** RPA Engineer. Confirmed delivery readiness for UAT.
*   **Wai Ching Chan:** Developer (Order Service). Confirmed UAT status of metadata field.
*   **Koklin Gan:** Stakeholder/Manager. Raised concerns regarding April 1st deadlines and mitigation strategies.
*   **Daryl Ng:** Noted as a potential alternative resource for BCRS posting tasks.

**Main Topic**
Discussion focused on the **"Re-delivery" use case for BCRS (BCRS Firefighting Group)** to prevent duplicate deposit postings in SAP. The team addressed task dependencies, timelines, and mitigation strategies regarding an upcoming April 1st deadline. The initiative involves three core jobs: updating metadata flags, consuming those flags to suppress duplicates, and executing RPA charges.

**Decisions Made**
*   **Parallel Execution:** Michael Bui confirmed that the Sales Posting work (Item #2) has **no dependency** on the completion of the RPA deployment (Item #3); both can proceed in parallel.
*   **UAT Deadline Confirmed:** De Wei Tey confirmed the RPA solution will be ready for UAT testing by **April 1**.
*   **Compliance Status:** Prajney Sribhashyam clarified that while the fix is not mandatory for April 1st, it impacts all re-deliveries of orders containing BCRS SKUs.

**Pending Actions & Ownership**
*   **Update Jira Ticket (DPD-807):** Prajney Sribhashyam will update the ticket with finalized details and timelines after clarifying dependencies.
*   **Start Development:** De Wei Tey to begin work on RPA tasks immediately (starting tomorrow, March 27).
*   **SIT Planning:** Michael Bui previously indicated System Integration Testing (SIT) is likely scheduled for **April 6–7** (referred to as "06-07/4").

**Key Dates & Deadlines**
*   **March 27, 2026:** Target start date for RPA development tasks.
*   **April 1, 2026:** Deadline for RPA readiness (UAT testing).
*   **April 6–7, 2026:** Estimated window for SIT completion (per Michael Bui).

**Contextual Notes**
*   Michael Bui is going on leave the following week; immediate alignment was required to ensure handover or continuity.
*   Koklin Gan raised concerns about a potential gap between the April 1st requirement and the final timeline, suggesting mitigation via stopping BCRS SKU re-deliveries if necessary. Prajney noted that RPA completion is estimated at 3–5 days from the start date.


## [55/70] Backend Chapter
Source: gchat | Group: space/AAAAHhDyHI4 | Last Activity: 2026-03-26T09:57:03.534000+00:00 | Last Updated: 2026-03-26T10:45:48.624917+00:00
**Daily Work Briefing: Backend Chapter**

**Key Participants & Roles**
*   **Michael Bui:** Investigated GCP PubSub configuration.
*   **Nicholas Tan:** Flagged critical supply-chain security issues (Trivy/LiteLLM); paused pipelines; identified expired cluster certificates requiring immediate rotation.
*   **Lester Santiago Soriano:** Blocked on CI/CD pipeline errors after upgrading Go dependencies.
*   **Boon Seng Ong:** Investigated ESPv2 deployment failures.

**Main Topics**
1.  **Critical Supply-Chain Security Alert (March 26, Morning):** Nicholas Tan identified a "Trojanization" attack affecting Trivy, Checkmarx, and LiteLLM tools (source: Kaspersky blog).
    *   *Action:* Users with `trivy` CLI version `v0.69.4` must uninstall immediately. Users with `litellm` on local machines are instructed **not** to upgrade, as the binary is compromised.
2.  **CI/CD & Dependency Upgrade (March 12):** Lester Santiago Soriano upgraded `stdlib` to `v1.25.8`. The pipeline failed due to a version mismatch between the project target (Go 1.25.8) and the build agent's `golangci-lint` (compiled with Go 1.24).
    *   *Root Cause:* Requires update to the `dpd-backend-cicd` resource.
3.  **ESPv2 Deployment Failure (March 25):** Boon Seng Ong reported failures in `deploy-esp-image` due to invalid flags for `gcloud beta run deploy` and `update-traffic`. Suspects changes to the "golden pipeline."
4.  **Service Account Security Audit (March 16):** Nicholas Tan identified JSON keys embedded in Service Accounts (`pong-club-agent`, `vertex-client`) within `fpg-titan-preprod` requiring decomposition.
5.  **Cluster Certificate Expiry (March 26, 09:57 UTC):** Nicholas Tan flagged an urgent need to identify the owner of a specific cluster and rotate certificates immediately, warning that failure to do so will cause cluster failure ("go boom boom").

**Pending Actions & Ownership**
*   **Eradicate Compromised CLI Tools:** Immediately uninstall `trivy` v0.69.4 from all laptops; halt upgrades for `litellm`.
    *   *Owner:* **All Team Members**.
*   **Resolve CI/CD Pipeline Block (Go Version):** Update `dpd-backend-cicd` resource to support Go 1.25.8 or align linter version.
    *   *Owner:* **TBD** (Lester requested ownership).
*   **Investigate Golden Pipeline Breakage:** Determine changes causing `gcloud beta run deploy` failures for ESPv2.
    *   *Owner:* **Boon Seng Ong**.
*   **Service Account Cleanup:** Decompose identified SAs (`pong-club-agent`, `vertex-client`) in `fpg-titan-preprod`.
    *   *Owner:* **TBD** (Nicholas Tan flagged).
*   **Cluster Certificate Rotation:** Identify cluster owner and rotate certificates immediately to prevent outage.
    *   *Owner:* **TBD** (Nicholas Tan requested help).

**Decisions Made**
*   Pipelines for `infra-gcp-fpg-titan` remain disabled pending the resolution of Trivy CLI risks.
*   The team has been instructed to remove specific compromised tool versions locally; local development environments are now a security priority over CI/CD infrastructure.
*   Immediate attention is required to identify cluster owners for certificate rotation.

**Key Dates & Follow-ups**
*   **March 6, 2026:** Initial PubSub inquiry (Open).
*   **March 12, 2026:** Pipeline failure reported; escalation for CICD ownership required.
*   **March 16, 2026:** Security flag raised regarding `fpg-titan-preprod` SAs.
*   **March 25, 2026:** Critical deployment failure reported; investigation into golden pipeline changes initiated.
*   **March 26, 2026 (Morning):** Supply-chain attack confirmed; immediate local cleanup required.
*   **March 26, 2026 (09:57 UTC):** Urgent cluster certificate rotation identified as critical path item to prevent failure.


## [56/70] RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU | Last Activity: 2026-03-26T09:12:17.093000+00:00 | Last Updated: 2026-03-26T10:47:32.420567+00:00
**Daily Briefing Summary: RMN Leadership Space (Updated Mar 26)**

**Key Participants & Roles**
*   **Bryan Choong:** Returning from eTail Asia; prioritizing Q1 case study compilation and low-sodium project. Emphasized the need for a tracker on developing case studies.
*   **Pauline Tan:** Managing LinkedIn content (FPG ADvantage page) and award repurposing. Currently transitioning from award submissions to case study development.
*   **Rajiv Kumar Singh:** Coordinating SOAC planning; shared industry benchmark regarding DoorDash Ads sales lift measurement (+30% incrementality).
*   **Allen Umali:** Leading SignCloud cleanup and Advertima loop verification (Legacy hardware status remains active).

**Main Topics**
1.  **Case Study Development & Tracking:** With Q1 ending, Bryan Choong requested a tracker for developing case studies. Pauline Tan confirmed the HPB case study is in progress; she recently submitted long-form award entries for Drum APAC and Retail Asia Awards (Mar 26), which will be repurposed into shorter formats. She is also preparing an APB submission. Bryan directed immediate focus on building a "low sodium" case study while BD team explores other potential leads to avoid delays similar to HPB timelines.
2.  **Industry Benchmarking:** Rajiv Kumar Singh shared insights from DoorDash Ads, noting new sales lift measurement capabilities driving up to 30% incrementality for brands on average (Mar 26).
3.  **SignCloud Cleanup:** Legacy hardware cleanup continues; Allen Umali confirmed the full list is available for removal by Mar 28.

**Pending Actions & Owners**
*   **Case Study Tracker:** Establish and maintain a refreshed tracker of strong Q1 case studies. *Owner: Pauline Tan.*
*   **Low Sodium Case Study:** Accelerate development of this specific asset to prioritize immediate wins over long-cycle projects like HPB. *Owners: Bryan Choong, Pauline Tan.*
*   **HPB & APB Submissions:** Convert submitted award entries (Drum APAC, Retail Asia) into case study formats; prepare APB submission. *Owner: Pauline Tan.*
*   **SignCloud Cleanup:** Complete manual removal of legacy screens and resolve loop errors. *Owner: Allen Umali | Deadline: Mar 28.*
*   **Advertima SRA Renewal:** Secure new SRA for long-term partnership beyond April extended PoV. *Owners: Allen Umali, Alvin Choo.*
*   **SOAC Planning:** Finalize targets per CM, supplier, and category by end of March. *Owner: Rajiv Kumar Singh & Ryan.*

**Decisions Made**
*   **Case Study Priorities:** Immediate focus shifted to "low sodium" case study construction; HPB and APB efforts rely on repurposing recent award submissions rather than starting from scratch.
*   **Award Repurposing Strategy:** Long-form entries for Drum APAC and Retail Asia Awards (submitted Mar 26) will be adapted into concise case studies.
*   **SignCloud Resolution:** Manual purging of old screens confirmed, targeting completion this week.
*   **Industry Alignment:** Team to consider DoorDash's sales lift measurement benchmarks (+30% incrementality) for future campaign strategies.

**Key Dates & Deadlines**
*   **Mar 26:** Pauline Tan submitted award entries (Drum APAC, Retail Asia); Bryan Choong requested case study tracker and low-sodium focus; Rajiv shared DoorDash benchmark data.
*   **Mar 28 (Est.):** Completion of SignCloud manual cleanup.
*   **End of March:** Deadline to finalize SOAC targets.
*   **April End:** Current deadline for Advertima extended PoV operations.


## [57/70] BCRS Regroup - Open Item Planning - Mar 26
Source: gchat | Group: space/AAQAC8aeuag | Last Activity: 2026-03-26T08:53:37.675000+00:00 | Last Updated: 2026-03-26T10:47:43.346295+00:00
**Daily Work Briefing: BCRS Regroup – Open Item Planning (Mar 26)**

**Key Participants & Roles**
*   **Daryl Ng:** Initiator of the planning session; provides project status updates.
*   **Prajney Sribhashyam:** Facilitator/Owner of tracking documentation; coordinates stakeholder inclusion.
*   **Wai Ching Chan:** Active participant in the chat space (availability confirmed).

**Main Topic**
The discussion focuses on identifying open items for the "BCRS Regroup" and determining necessary leads and members required to address them, specifically within the context of Project Light.

**Pending Actions & Ownership**
*   **Action:** Populate the newly created tracking sheet with relevant leads and required members.
    *   **Owner:** Daryl Ng (Responding to Prajney's request at 05:07).
*   **Action:** Review and acknowledge the shared Google Chat room link for further discussion or documentation.
    *   **Owner:** Wai Ching Chan (Link viewed by 3 of 8 participants).

**Decisions Made**
*   No formal decisions were recorded in this chat log; the group agreed to utilize a shared sheet for tracking open items and leads.

**Key Dates, Deadlines & Follow-ups**
*   **Date:** March 26, 2026.
*   **Upcoming Meeting:** Project Light Backlog and Sprint Planning discussion scheduled from **4:00 PM – 5:00 PM**.
*   **Reference Links:**
    *   Master Sheet: Created by Prajney Sribhashyam (Time: 05:06).
    *   Chat Room Link: `https://chat.google.com/room/AAQAgT-LpYY/qtUOXlxVm80/o5O3fA1DeMA` (Shared at 08:53).


## [58/70] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/qtUOXlxVm80 | Last Activity: 2026-03-26T08:53:13.643000+00:00 | Last Updated: 2026-03-26T10:48:04.829699+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles:**
*   **Prajney Sribhashyam:** Initiator; confirmed Jira ticket updates (DPD-807) and clarified RPA ownership for deposit charging.
*   **Wai Ching Chan:** Implementing metadata in UAT config service; provided API examples (cURL/gRPC); identified need to contact a Config Service owner for production.
*   **Michael Bui:** Clarified that the metadata change prevents duplicates but does not handle the actual redelivery logic; requested effort estimates and assignment of the RPA task; noted upcoming leave starting next week.
*   **De Wei Tey:** Provided estimates for related tasks (Order Service maintenance and RPA).
*   **Sneha Parab:** Identified as a potential Config Service owner to approach for production metadata updates.

**Main Topic:**
Discussion regarding the **'Re-delivery' use case for BCRS** (Jira: DPD-807). The focus has shifted from general coordination to specific implementation details and ownership clarification. Key deliverables remain:
1.  **Config Service:** Wai Ching Chan is adding "Deposit posted to SAP" metadata to the UAT config service via Backoffice (`admin-uat.fairprice.com.sg`). Production requires a Config Service owner (Sneha Parab or similar).
2.  **Order Service:** Maintaining 'Deposit posted to SAP' in metadata; Wai Ching Chan provided specific cURL and gRPC call examples for UAT testing (`api.zs-uat.fairprice.com.sg/order-service/v3/deliveryOrders`).
3.  **Sales Posting:** Consumes the field to suppress duplicate BCRS deposit postings (Task 2 & 3 in Jira).
4.  **RPA Logic:** Specifically handles charging the BCRS deposit to the customer's original payment method (Point 4). Prajney clarified this is an RPA task, distinct from Michael's metadata changes.

**Actions Pending & Ownership:**
*   **Production Metadata Setup:** Wai Ching Chan and team must identify and approach the **Config Service owner** (Sneha Parab suggested) to add the field in production.
*   **Technical Implementation:** Wai Ching Chan will test UAT updates using provided API calls; development effort estimated at 1-2 days by Wai Ching/De Wei Tey.
*   **Timeline & SIT:** Michael Bui is on leave starting next week; earliest System Integration Testing (SIT) date is **April 6 or April 7, 2026**.
*   **Jira Updates:** Prajney confirmed Task 4 (RPA) has been assigned and added to the ticket.

**Decisions Made:**
*   The metadata field ("Deposit posted to SAP") will be implemented via the Config Service for UAT, with production handled by a designated service owner.
*   Michael Bui's changes specifically address duplicate prevention; the **RPA team** retains ownership of the redelivery charge logic.
*   SIT is scheduled for early April due to Michael Bui's leave schedule.

**Key Dates & Follow-ups:**
*   **Discussion Dates:** March 24, 2026 (Initial briefing); March 26, 2026 (Implementation details).
*   **Upcoming Leave/SIT Window:** Michael Bui leaves next week; SIT targeted for **April 6–7, 2026**.
*   **Reference Link:** https://ntuclink.atlassian.net/browse/DPD-807

**Technical References:**
*   UAT Config: `https://admin-uat.fairprice.com.sg/settings/extensions/18`
*   UAT Delivery Order Admin: `https://admin-uat.fairprice.com.sg/customer-support/delivery-orders/75588070`


## [59/70] [BCRS]-SAP to POS & DBP Interface Deployment
Source: gchat | Group: space/AAQAeMC3qBk/wHwvIxHWK_U | Last Activity: 2026-03-26T08:14:28.945000+00:00 | Last Updated: 2026-03-26T10:50:31.865720+00:00
**Daily Work Briefing: [BCRS]-SAP to POS & DBP Interface Deployment**

**Key Participants & Roles**
*   **Onkar Bamane:** Lead coordinator; requested documentation updates and confirmed team readiness.
*   **Michael Bui:** Contributor; added deployment steps to the tracking sheet.
*   **Sneha Parab:** Contributor and Planner; updated the sheet and confirmed resource availability for parallel deployments.
*   **Shiva Kumar Yalagunda Bas & Dang Hung Cuong:** Designated resources identified for MP (Mirakl) deployment support.

**Main Topic**
Coordination of documentation updates and resource allocation for the upcoming SAP to POS & DBP Interface Deployment, with specific focus on ensuring step-by-step procedures are recorded and team availability is confirmed.

**Pending Actions & Ownership**
*   **Review Documentation:** Onkar Bamane (via Sneha Parab) needs to verify if Michael Bui's added row contains all necessary details or requires further input.
*   **Standby Coordination:** Sneha Parab has flagged the need for three specific team members (including herself, Michael Bui, and potentially others) to be available for deployment, testing, and standby duties during the SAP deployment window.

**Decisions Made**
*   **Resource Allocation for MP Deployment:** It was confirmed that three individuals will support the MP deployment (combining DBP + Mirakl). This team will handle deployment, testing, and standby specifically while the SAP deployment is ongoing.
*   **Process Confirmation:** Onkar Bamane acknowledged the updates ("ok"), indicating acceptance of the current status of the sheet and the proposed resource plan.

**Key Dates & Follow-ups**
*   **Timeline Context:** All activities discussed occurred on **2026-03-26**, between **07:05 UTC** (initial request) and **08:14 UTC** (final confirmation).
*   **Immediate Follow-up:** Verification of the completeness of Michael Bui's entries in the shared sheet.
*   **Upcoming Event:** The SAP deployment window is imminent, requiring the designated team to be on standby.


## [60/70] BCRS ECOMM SAP POSTING
Source: gchat | Group: space/AAQA-ICuJRM | Last Activity: 2026-03-26T07:54:50.976000+00:00 | Last Updated: 2026-03-26T10:53:06.349496+00:00
**Daily Work Briefing: BCRS ECOMM SAP POSTING & Refunds UAT (Mar 26 Update)**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** UAT lead; coordinating validation and technical alignment.
*   **Tan Gay Lee:** Stakeholder rejecting current sign-off due to GL entry errors in pre-order/S&G refunds.
*   **Lai Shu Hui:** Accounting participant; pending final test case closure for e-commerce returns.
*   **Sathya Murthy Karthik:** Confirmed 2 untested e-commerce cases remain; advocating for immediate sign-off.
*   **Onkar Bamane:** Previously requested separate IT audit sign-off (now adjusted scope).
*   **Yaxin Hao / Jianbin Huang:** Technical owners asked to check Store 420 UAT sales data.

**Main Topic**
UAT progress is stalled due to GL entry discrepancies in Pre-order and Scan 'n Go (S&G) refunds, preventing final sign-off. While SAP recommends using the "Data 8" aggregation method for deposit refunds instead of RPA, Tan Gay Lee asserts that current refund entries are not captured in the correct GL accounts, rendering the E-Comm Returns & Refunds scope incomplete without these corrections.

**Status of Issues & Updates**
*   **Sign-off Scope Adjustment:** Following alignment on the call (Mar 26), S&G deposit refunds are excluded from the "Returns & Refunds" sign-off. A separate sign-off is now requested specifically for E-Comm. The scope covers: (1) API for Posting Deposit Accounting, (2) Marketplace SKU creation, (3) Concess Sales Detail Report, and (4) Concess Sales Summary Report.
*   **GL Entry Discrepancy:** Tan Gay Lee rejected the sign-off, noting that refunds for pre-orders paid online are processed manually but fail to capture the correct GL account. Pre-orders cancelled within 5 days follow 'Cancellation after delivery' via CS; POS-paid pre-order refunds occur at POS with cash.
*   **Testing Status:** Sathya Murthy Karthik highlighted two untested e-commerce cases pending validation (Pass/Fail) and urged immediate closure to prevent delays. Prajney Sribhashyam requested clarification from Tan regarding the GL issue, citing previous alignment that E-Comm test cases were fine.
*   **Technical Checks:** Prajney Sribhashyam asked Yaxin Hao and Jianbin Huang to verify unprocessed sales for Store 420 in UAT.

**Pending Actions & Ownership**
1.  **GL Resolution:** Tan Gay Lee requested an emergency call (Google Meet: `emh-uzhw-vtz`) with Prajney and Sathya to resolve the incorrect GL capture issue for pre-order refunds. **(Owner: Prajney Sribhashyam, Sathya Murthy Karthik)**.
2.  **Test Case Closure:** Lai Shu Hui must validate the remaining two untested e-commerce cases immediately to allow sign-off. **(Owner: Lai Shu Hui)**.
3.  **Data Verification:** Check for unprocessed sales in Store 420 UAT. **(Owner: Yaxin Hao, Jianbin Huang)**.
4.  **Sign-off Execution:** Tan Gay Lee and Lai Shu Hui to provide the separate E-Comm sign-off once GL issues are resolved and tests pass. **(Owner: Tan Gay Lee, Lai Shu Hui)**.

**Decisions Made**
*   S&G deposit refund posting scope is excluded from the current "Returns & Refunds" sign-off; a distinct E-Comm sign-off is required.
*   RPA separate posting for deposit refunds is deemed inadvisable; SAP recommends using Data 8 aggregation (aligned with sales/BCRS deposit methods).
*   Current UAT cannot proceed to final deployment until the incorrect GL capture for pre-order refunds is addressed and two pending e-commerce test cases are validated.

**Key Dates & Follow-ups**
*   **Mar 26, 07:51 AM:** Tan Gay Lee flagged incorrect GL entries for pre-order refunds.
*   **Mar 26, 07:54 AM:** Emergency Google Meet scheduled to resolve the sign-off blocker.
*   **Mar 26, 03:03 AM:** Technical request sent to check Store 420 UAT data.

**Immediate Follow-up:** Attend the emergency video meeting to clarify GL handling for pre-order refunds and ensure Lai Shu Hui completes the two outstanding e-commerce test cases urgently.


## [61/70] Project Light: Mobilization and Planning Workshop Day 3 - Mar 26
Source: gchat | Group: space/AAQAwOH7W8A | Last Activity: 2026-03-26T07:31:58.093000+00:00 | Last Updated: 2026-03-26T10:54:35.988273+00:00
**Daily Work Briefing: Project Light Mobilization Workshop (Day 3)**

**Key Participants & Roles**
*   **Jacob Yeo**: Primary communicator regarding agenda updates.
*   **Pandi**: Uploaded a new resource link on March 26.
*   **Recipients**: 18 total members of the "Project Light" Mobilization and Planning group; 10 have viewed the latest shared resource (FairPrice Rewards Catalogue Edit).

**Main Topic/Discussion**
The discussion continues to center on critical updates for **Day 3** of the Project Light Mobilization and Planning Workshop, scheduled for **March 26**. While Jacob Yeo previously notified the team of "latest changes" to the schedule without detailing specific content, a new communication thread initiated by **Pandi** at 07:31 AM UTC on March 26 introduced a direct link to the FairPrice Rewards Catalogue edit page. This suggests the "changes" or operational requirements may involve catalog management or rewards program adjustments relevant to the day's agenda.

**Pending Actions & Ownership**
*   **Action**: Review the updated project agenda and new resource links.
    *   **Owner**: All 18 workshop participants.
    *   **Status Update**: While 11 members viewed the previous agenda document, current engagement metrics show that **10 of 18** participants have now accessed the FairPrice catalogue link provided by Pandi.
    *   **Reference (Agenda)**: [Project Light Workshop Agenda](https://docs.google.com/spreadsheets/d/1ODEEFsP8mMxmUhYNuQ1norNCnWoIJwddZzUFqEUX-qw/edit?gid=1079702164#gid_1079702164).
    *   **Reference (New Resource)**: [FairPrice Rewards Catalogue Edit](https://admin.fairprice.com.sg/rewards/catalogue/edit/1049) (Linked by Pandi).
*   **Action**: Integrate FairPrice catalogue updates into Day 3 planning.
    *   **Owner**: All participants.
    *   **Context**: Jacob Yeo's request to "take note of the latest changes" is now complemented by the specific operational link shared by Pandi, requiring immediate review before the session begins.

**Decisions Made**
No formal strategic decisions were recorded in these exchanges. The communications serve as mandatory notifications for agenda modifications and the introduction of new external tooling (FairPrice admin interface) for the workshop day.

**Key Dates & Follow-ups**
*   **Initial Notification Date**: March 25, 2026 (10:35 AM UTC).
*   **Resource Update Date**: March 26, 2026 (07:31 AM UTC) by Pandi.
*   **Event Date**: March 26, 2026 (Day 3 of Mobilization and Planning Workshop).
*   **Follow-up Required**: Immediate review of both the Google Sheet agenda and the FairPrice catalogue link by all attendees prior to the start of Day 3.

**Summary Note**
Participants must access the linked resources immediately. While Jacob Yeo flagged schedule changes on March 25, Pandi has subsequently provided a specific operational link (FairPrice Rewards Catalogue Edit) on the morning of the event. Engagement is tracking at 10 views out of 18 for this new resource, indicating a need for further reminders to ensure all stakeholders are aligned with both the schedule and the catalog updates before the workshop commences.


## [62/70] [Postmortem] 300126 - P1 - Some customers charged full price - Mar 26
Source: gchat | Group: space/AAQACrrEY0I | Last Activity: 2026-03-26T07:11:32.324000+00:00 | Last Updated: 2026-03-26T10:54:48.749435+00:00
**Daily Work Briefing: Incident Post-Mortem Review**

**Key Participants & Roles**
*   **Zaw Myo Htet:** Meeting initiator; owner of the discussion thread.
*   **Nicholas Tan:** Initial attendee, unavailable for live meeting.
*   **Kyle Nguyen:** Active participant joining to support the session.
*   **Maou Sheng Lee:** Cited as a potential replacement for Nicholas Tan.
*   **Gopi:** Cited as a potential replacement for Nicholas Tan.

**Main Topic**
Review of Postmortem document **[300126 - P1 - Some customers charged full price]** (dated March 26, 2026). The incident involves a P1 severity issue where specific customers were incorrectly charged full pricing.

**Pending Actions & Ownership**
*   **Request for Additional Attendees:** Zaw Myo Htet requested representation from the RE (Requirements/Engineering) team to join the discussion at L11 Macchiato. **Owner:** Zaw Myo Htet / Organizers.
*   **Meeting Attendance Substitution:** Nicholas Tan delegated attendance to Maou Sheng Lee or Gopi due to conflicting priorities. **Owner:** Nicholas Tan (to confirm).

**Decisions Made**
*   No formal decisions regarding the root cause or resolution were recorded in this chat snippet; the session is currently in the coordination phase for attendees.

**Key Dates & Follow-ups**
*   **Date of Incident/Post-Mortem:** March 26, 2026.
*   **Meeting Time:** Approximately 07:03 UTC (March 26).
*   **Document Access:** Postmortem file shared at 07:11:32 UTC via Google Docs link: `https://docs.google.com/document/d/16aLYguYuUjoHHHd_UYVllHewHBtuejGgjH-ZiH0D3l8/edit?usp=sharing`.
*   **Next Steps:** Participants are expected to review the linked document prior to or during the meeting. Kyle Nguyen explicitly requested the file be shared (which was done).

**Summary Note**
The conversation focuses on logistical coordination for a post-incident review of a critical pricing error. While Nicholas Tan could not attend, Kyle Nguyen confirmed participation, and the necessary documentation has been distributed to the group. Awaiting confirmation of RE team attendance.


## [63/70] Backend Chapter
Source: gchat | Group: space/AAAAHhDyHI4/nKDrYLSLrhA | Last Activity: 2026-03-26T06:33:30.786000+00:00 | Last Updated: 2026-03-26T10:55:37.850722+00:00
**Daily Work Briefing: Backend Chapter Security Alert**

**Key Participants & Roles**
*   **Nicholas Tan:** Initiator/Security Lead. Issuing the security directive.
*   **Jazz Tong:** Team Member. Seeking clarification on verification commands.
*   **Michael Bui:** Team Member/Homelab User. Confirming status of local usage.

**Main Topic**
A critical security advisory regarding a compromised `trivy` CLI vulnerability (version v0.69.4) which impacts the `litellm` tool. The discussion focuses on immediate remediation steps and clarifying safety protocols for existing installations.

**Pending Actions & Ownership**
*   **Action:** Check local machine for `trivy` CLI installation using the command `whereis trivy`.
    *   **Owner:** All Backend Chapter team members (specifically prompted by Nicholas Tan).
*   **Action:** Verify `trivy` version via `trivy --version`.
    *   **Owner:** All Backend Chapter team members.
*   **Action:** Immediately remove `trivy` if version v0.69.4 is detected.
    *   **Owner:** Any user identified with the specific vulnerable version.
*   **Action:** Do **not** upgrade `litellm`. Maintain current pinned versions to avoid triggering the scanner vulnerability.
    *   **Owner:** All users running `litellm`.

**Decisions Made**
*   **Version Constraint:** Users must strictly avoid upgrading `litellm` due to its scanning by the compromised `trivy` instance.
*   **Remediation Threshold:** Removal of `trivy` is mandatory only if the specific version v0.69.4 is found; pinned versions (e.g., Michael Bui's v1.81.3) are considered safe and require no action.

**Key Dates & Follow-ups**
*   **Date:** March 26, 2026
*   **Time:** Alerts issued between 05:59 UTC and 06:33 UTC.
*   **Follow-up:** Immediate execution of version checks and removal procedures is requested ("soonest").

**Specific References**
*   **Tool:** `trivy` CLI (vulnerable at v0.69.4).
*   **Affected Tool:** `litellm`.
*   **Safe Configuration Note:** Michael Bui confirmed safety with `litellm` pinned to version 1.81.3.


## [64/70] Project Light: Mobilization and Planning Workshop Day 1 - Mar 24
Source: gchat | Group: space/AAQAA8d_pfI | Last Activity: 2026-03-26T06:29:23.835000+00:00 | Last Updated: 2026-03-26T10:56:05.605221+00:00
**Daily Work Briefing: Project Light – Mobilization & Planning Workshop (Day 1)**
**Date:** March 24, 2026 (Session concluded; new insights added Mar 26)
**Resource Link:** https://chat.google.com/space/AAQAA8d_pfI

**Key Participants & Roles**
*   **Jacob Yeo:** Meeting facilitator.
*   **Vivian Lim Yu Qian:** Presenter/UI Walkthrough; defined technical/action items.
*   **Tiong Siong Tee:** UX Lead; proposed agenda flow and requested Figma access.
*   **Cecilia Koo Hai Ling:** Design/UX Contributor; shared DoorDash, NTUC FairPrice, Lazada references; clarified SKU logic; provided RedMart video analysis; posted new campaign link.
*   **Christine Yap Ee Ling:** Internal Liaison; handling Figma link distribution.
*   **Rajesh Dobariya:** Stakeholder; reviewed delivery categorization references.
*   **Sophia Liao & Rock Shi:** Identified as audience for Cecilia's latest Flash Deal observations.

**Main Topic & Discussion Updates**
The team conducted a high-level UX walkthrough, significantly expanding reference analysis to include RedMart's current "mega campaign" (running for 2 days) and Lazada app mechanics:
*   **Voucher Logic Update:** Cecilia Koo Hai Ling shared a specific Lazada campaign link (`https://s.lazada.sg/s.3jBSs`), noting that **vouchers are tied to the campaign only**. This clarifies previous assumptions about standalone voucher usage.
    *   *Engagement:* The new link was viewed by 15 of 23 participants.
*   **RedMart Campaign Analysis:** Cecilia also shared a video demo (`Video_20260326_094235_087_1.mp4`, viewed by 13 of 23) reviewing critical components:
    1.  **Flash Deal Mechanics:** Clickable sections direct users back to the dedicated flash deal landing page.
    2.  **Label System:** RedMart displays multiple scrollable labels, including unclaimed vouchers.
    3.  Voucher center structure and gamification mechanics.
    4.  Promo mechanisms (claim, apply, stack, and nudge toward next tiers).
    5.  Social sharing features.
    6.  "Store-in-store" concepts (default views, dedicated flash deals, seller vouchers).
    7.  User journey flow: Homepage → Category → Search → Campaign → General Merchandise.
*   **Lazada & FairPrice References:** Reviewed DoorDash's first-time app open and NTUC FairPrice examples (SharkNinja Official Store, FP Unilever Tag). The Lazada "promo label" (dynamic seller section) and gamified "Help me click" mechanic were accepted as engagement drivers.
*   **Navigation & Filters:** Clarification remains needed on whether category page filters should be pre-configured ("dynamic") or retrieved dynamically.
*   **UI Clarity:** The toggle selection between "Scheduled" and "Quick" modes requires improved visual definition.
*   **Compliance:** Discussed potential separation of eGift cards from vouchers to meet compliance requirements.
*   **SKU Logic:** Clarified that when any SKU is clicked, it is displayed as the primary SKU in Slot 1.

**Decisions Made**
*   **Reference Alignment:** Agreed that DoorDash's categorization and Lazada/RedMart campaign mechanics (voucher stacking, gamification, store-in-store) are valid benchmarks for Project Light integration.
*   **Voucher Constraint:** Confirmed the finding that vouchers in the target reference campaigns are strictly tied to the specific campaign context.
*   **Specific Feature Validation:** Confirmed RedMart's clickable flash deal section behavior and scrollable label system as key UX patterns to analyze.
*   **Filter Logic:** No final consensus on filter behavior; pending technical solution discussion led by Vivian.
*   **Slot 1 Behavior:** Clarified that the clicked SKU populates Slot 1, establishing a baseline interaction pattern.

**Pending Actions & Owners**
1.  **Share Figma Link:** Christine Yap Ee Ling to send via separate internal chat (requested by Tiong Siong Tee).
2.  **Resolve Filter Logic:** Vivian Lim Yu Qian and the technical team to finalize category page filter behavior.
3.  **Refine UI Toggle:** Design team to address visual clarity for "Scheduled/Quick" toggle selection.
4.  **Compliance Review:** Determine if eGift cards must be standalone from vouchers given the new insight on campaign-tied vouchers.
5.  **Deep-Dive Analysis:** UX Lead (Tiong Siong Tee) to analyze RedMart's specific mechanics: clickable flash deal navigation, scrollable label system, voucher center, gamification logic, and store-in-store flows for Project Light integration.

**Key Dates & Follow-ups**
*   **Event:** Project Light Mobilization and Planning Workshop Day 1 (March 24, 2026).
*   **Status:** Session concluded; RedMart campaign materials and video shared via chat on March 26. New Lazada link (`s.3jBSs`) posted Mar 26.
*   **Next Step:** Internal distribution of Figma link by Christine Yap Ee Ling; UX team to evaluate RedMart's "mega campaign" mechanics for potential application in Project Light mega campaigns.


## [65/70] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/9UYvfToHPUM | Last Activity: 2026-03-26T05:55:01.238000+00:00 | Last Updated: 2026-03-26T10:56:16.131954+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Michael Bui:** Identified as the source of clarification regarding resource ownership.
*   **Daryl Ng:** Active participant seeking validation or confirmation on organizational structure; acknowledged the correction.
*   **Miguel:** Referenced as the current owner/responsible party for the "Leads" resource.

**Main Topic/Discussion**
The conversation focused on clarifying the organizational ownership and COE (Center of Excellence) alignment for the **"Leads"** resource within the Ecom/Omni Digital Product Development space. Specifically, participants debated whether the **Store Network** falls under the **Data COE** or if it remains under Miguel's purview.

**Decisions Made**
*   It was established that the specific "Leads" resource is currently **under Miguel**.
*   A counter-point was raised questioning if "store network" belongs to the Data COE, but no final structural change was confirmed in this thread; rather, a correction regarding the current owner (Miguel) was accepted.

**Pending Actions & Ownership**
*   **Clarification on Store Network Alignment:** The question of whether "Store Network" is technically under the **Data COE** remains an open point of inquiry raised by Michael Bui. No specific action item or deadline has been assigned yet in this chat log to resolve this structural query.

**Key Dates & Follow-ups**
*   **Conversation Date:** March 26, 2026 (UTC timestamps: 05:54 – 05:55).
*   **Next Steps:** Immediate follow-up required if the Data COE alignment for "Store Network" impacts current project resourcing.

**Contextual References**
*   **Space URL:** https://chat.google.com/space/AAQAN8mDauE
*   **Resource Name:** Leads (Ecom/Omni) Digital Product Development
*   **Total Messages:** 2


## [66/70] Data Tracking Working Group
Source: gchat | Group: space/AAAAkdI3Ijg | Last Activity: 2026-03-26T05:23:56.548000+00:00 | Last Updated: 2026-03-26T10:56:52.152320+00:00
**Daily Work Briefing: Data Tracking Working Group**

**1. Key Participants & Roles**
*   **Quan To Van:** Initiator of the communication thread; likely acting as a point of contact for segment-related inquiries.
*   **Nikhil Grover:** Active participant in the discussion (last reply mentioned).
*   **Patty Yuan:** Active participant in the discussion (last reply mentioned).
*   *Note:* The thread indicates 24 replies from other unnamed participants not listed in the provided summary snippet.

**2. Main Topic/Discussion**
The core subject of the conversation is establishing a communication channel for **"segment related request or question."** Quan To Van directed team members to utilize this specific Google Chat space/thread as the primary destination for such inquiries, implying a need to consolidate segment-related data tracking issues into one forum.

**3. Pending Actions & Ownership**
*   **Action:** Reach out via the designated channel (Google Chat space) for any new or existing segment-related requests.
*   **Ownership:** All team members requiring clarification on segments are responsible for directing questions here. Specific follow-up actions by Nikhil Grover and Patty Yuan regarding this directive were noted in the 24-reply thread but specific task assignments beyond "replying" are not detailed in the provided snippet.

**4. Decisions Made**
*   **Decision:** The Google Chat space (Resource: Data Tracking Working Group) has been designated as the official hub for handling segment-related questions. No alternative channels were mentioned; this thread is now the sole reference point for these topics.

**5. Key Dates, Deadlines, & Follow-ups**
*   **Date of Message:** March 26, 2026 (05:23:56 UTC).
*   **Last Activity:** Approximately 5 minutes ago relative to the briefing time.
*   **Thread Status:** High engagement with 24 unread replies at the time of notification.
*   **Next Steps:** Review the full thread history (available via URL) to identify specific resolutions or outstanding questions from Nikhil Grover, Patty Yuan, and other contributors before proceeding with segment tasks.

**Link to Full Context:** https://chat.google.com/space/AAAAkdI3Ijg


## [67/70] ❗ Important Email
Source: gchat | Group: space/AAQAUJW8HMo | Last Activity: 2026-03-26T05:08:22.340000+00:00 | Last Updated: 2026-03-26T10:57:52.628394+00:00
**Daily Work Briefing Summary (Updated)**

**Key Participants & Roles**
*   **Michael Bui (You):** Managing Osmos support, event RSVPs, FileVault compliance, performance feedback, Project Light coordination, and AI training follow-ups.
*   **Sip Khoon Tan (FPG AICOE) / Google AI Specialists:** Leading weekly Workbench Agentic AI sessions.
*   **Daryl Ng:** Declined "ACNxOsmos: Daily Cadence"; Organizer of new BCRS Regroup meeting; Key attendee for RMN discussion.
*   **Prajney Sribhashyam:** Lead for BCRS Refunds Warroom and organizer of "BCRS Regroup - Open Item Planning."
*   **Miguel Ho Xian Da (FairPrice):** Lead for OSMOS integration.
*   **Jazz Tong:** Head of Platform Engineering; on leave until Mar 23, 2026.
*   **Tong A. Yu / Lilibeth Villena (Accenture):** Proposing working sessions for integration architecture.

**Main Topics**
1.  **AI Training & Workbench Follow-up:**
    *   Weekly 30-min virtual support on building agents in Workbench (Gemini Enterprise).
    *   **Schedule:** Wednesdays, 2:00 PM – 2:30 PM SGT (Mar 25 – May 31, 2026).
    *   **Action:** RSVP required; submit questions via form prior to sessions.

2.  **BCRS - Refunds Issue Warroom & Regroup Updates:**
    *   **Warroom:** Scheduled for Thursday, March 19, 2026, 3:30 PM – 4:30 PM SGT. *Conflict with Project Light remains.*
    *   **New Meeting (Today):** "BCRS Regroup - Open Item Planning" scheduled for **Thursday, March 26, 2026, from 4:00 PM to 5:00 PM SGT**.
    *   **Organizer:** Prajney Sribhashyam.
    *   **Attendees:** Michael Bui (Required), Sathya Murthy Karthik (Required), Daryl Ng (Required), Akash Gupta (Required); Koklin Gan (Optional).

3.  **Project Light & RMN Integration:**
    *   **RMN Discussion:** Rescheduled for Thursday, March 26, 2026, from 2:00 PM – 3:00 PM SGT.
        *   *Attendees:* Michael Bui (Required), Rajiv Kumar Singh (Required), Bryan Choong (Optional).
    *   **Project Light:** Rescheduled to Mar 19, 4:00–5:00 PM SGT. *Conflict with BCRS Warroom remains.*

4.  **ACNxOsmos Daily Cadence Update:**
    *   Daryl Ng declined the Monday, March 30, 2026 (12:30 PM – 1:00 PM SGT) invitation due to reservist duty.

5.  **D&T Power Breakfast Planning:**
    *   New event by Trina Boquiren. Planning meeting: Tuesday, March 31, 2026, 1:30 PM – 2:00 PM SGT.

**Pending Actions & Ownership**
*   **BCRS Regroup RSVP (Michael Bui):** **Immediate Action Required.** Respond to the invitation for today (March 26), 4:00–5:00 PM SGT.
*   **AI Training RSVP:** Submit "Yes" to the weekly session series starting March 25; submit questions via form.
*   **RMN Meeting RSVP:** Confirm attendance for March 26, 2:00–3:00 PM SGT. *Note: This overlaps with your immediate requirement to join BCRS Regroup (4:00 PM).*
*   **Project Light/Warroom Conflict:** Resolve scheduling conflict between Project Light (Mar 19) and BCRS Warroom (Mar 19). Reply "Yes" to both or delegate.
*   **Performance Meeting RSVP:** Confirm attendance for Mar 18, 4:00 PM SGT.
*   **D&T Breakfast Planning RSVP:** Respond to Trina Boquiren's invitation for March 31.
*   **OSMOS Architecture:** Provide architectural details on SmartCarts and IPOS to finalize long-term integration strategy with Accenture.

**Decisions Made**
*   **RMN Integration Timeline:** Team agreed to prioritize a focused working session on March 26 for architecture definition after previous slots failed due to conflicts.
*   **OSMOS Capability:** Confirmed feasible short-term integration (video via CDN, image via FPG service); long-term decision pending Accenture recommendation.

**Critical Dates & Deadlines**
*   **Mar 18, 2026:** Performance Feedback Meeting.
*   **Mar 19, 2026:** BCRS Warroom (3:30 PM) & Project Light (4:00 PM). *Conflict.*
*   **Mar 25–May 31, 2026:** Weekly AI Workbench Sessions.
*   **Mar 26, 2026 (Today):**
    *   RMN Discussion with Accenture (2:00–3:00 PM SGT). Link: `https://meet.google.com/koe-uzer-xbd`.
    *   BCRS Regroup - Open Item Planning (4:00–5:00 PM SGT). Organizer: Prajney Sribhashyam.
*   **Mar 30, 2026:** ACNxOsmos Daily Cadence (Daryl Ng declined).
*   **Mar 31, 2026:** D&T Power Breakfast Planning Session; FileVault Final Deadline.


## [68/70] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/nO81EVARv7I | Last Activity: 2026-03-26T04:42:23.981000+00:00 | Last Updated: 2026-03-26T10:58:30.957470+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Dany Jacob:** Requestor; seeking expertise on BCRS item refunds (Scan n Go/Preorder) and API enhancements.
*   **Prajney Sribhashyam:** Technical Lead; clarifying SAP/Finance constraints regarding refund posting methods and coordinating alignment between DPD, SAP, and Finance teams.
*   **Akash Gupta:** Developer/Stakeholder; advocating for RPA-based flows based on prior agreements (Feb 16) and providing historical context/tickets.
*   **Daryl Ng:** Stakeholder; seeking clarification on specific Finance/SAP feedback regarding the current posting method.
*   **Wai Ching Chan, Amirul Amri, Gopalakrishna Dhulipati, Alvin Choo:** CC'd/involved parties.

**Main Topic**
Resolution of a discrepancy regarding refund posting for Scan n Go (SnG) and preorder items involving container deposits. The core conflict is between the existing **RPA email flow** (proposed by Akash/Dany) and the **SAP Finance requirement** that refund posting must route through **Data8** to ensure accurate Cost Centre (CC) and Profit Centre allocation.

**Decisions & Clarifications**
*   **Current State:** SAP/Finance feedback indicates the current RPA email flow for *posting* refunds is inaccurate regarding financial accounts, though it works for the initial payment reversal/refund trigger.
*   **Required Path:** Deposit refund posting must align with the SnG sales/deposit/posting flow via **Data8**. Data8 already has pre-configured accounts, whereas RPA requires complex manual configuration of CCs and Profit Centres.
*   **Historical Context (Akash):** An OMS enhancement was delivered to UAT on Feb 16, aligned with Finance and CC at that time. Prajney clarifies that while the email flow for refunds is accepted, the *posting* mechanism was never successfully validated via RPA until now.
*   **Action Required:** Teams must either justify why the current approach works or proceed with enhancing Data8 posting to include refund data.

**Pending Actions & Ownership**
*   **Estimate Creation:** Dany Jacob and Wai Ching Chan are requested (by Prajney) to provide a rough estimate for enhancing the `GET` API endpoint (and subsequent Data8 integration) to include container deposit information for refunds.
    *   *Ticket Reference:* DPD-529 (https://ntuclink.atlassian.net/browse/DPD-529).
*   **Documentation:** Akash Gupta shared a Google Sheet and ticket link regarding the RPA flow; further alignment on the Data8 enhancement is pending.

**Key Dates & References**
*   **Current Date:** March 26, 2026 (Conversation timestamped early morning UTC).
*   **Previous Milestone:** February 16, 2026 – OMS enhancement delivered to UAT; alignment with Finance/CC achieved.
*   **API Endpoint:** `https://api.zs-uat.fairprice.com.sg/order-service/order/{id}/returns` (Requesting container deposit inclusion).
*   **Documentation Links:**
    *   Google Sheet: `14tjv37bLbBBvVTJeE_qxkMSQ2h-ltXPbOpktaAilJww`
    *   Jira Ticket: DPD-529


## [69/70] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/h-WUXwPta8M | Last Activity: 2026-03-26T03:05:37.451000+00:00 | Last Updated: 2026-03-26T10:59:54.289976+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**
**Source:** Google Chat Space (13 messages) | **Date:** March 26, 2026

### Key Participants & Roles
*   **Daryl Ng:** Raises architectural queries regarding data indexing; confirms understanding of new governance updates.
*   **Michael Bui:** Initially suggests DSP handles Algolia integration; seeks clarification on system boundaries.
*   **Alvin Choo:** Corrects architecture scope (B2C backend, not DSP) and defines initial governance protocols.
*   **Gopalakrishna Dhulipati:** Provides context on the Distributed Service Platform (DSP); confirms EA design principles and clarifies project-level approval requirements.

### Main Topic/Discussion
The team discussed technical ownership of **Algolia data indexing** within the B2C ecosystem, clarified architectural distinctions between the core commerce engine (DSP) and channel-specific backends, and refined governance protocols regarding system unification.
*   **Clarification:** Algolia integration is specific to the **B2C backend**, not DSP. Each channel (B2C, B2B, POS) utilizes its own Frontend and Backend.
*   **Design Principle Update:** Gopalakrishna confirmed that while high-level design principles are approved by Enterprise Architecture (EA), specific implementation details for each backend require approval on a **per-project basis**.
*   **Unification Constraints:** Due to per-channel ownership (e.g., distinct Cart & Checkout systems for POS vs. Omni app), a unified cart cannot exist across channels without explicit EA intervention. Building a unified cart requires returning to EA for approval.

### Decisions Made
*   **Ownership Confirmed:** The **B2C backend** manages indexing of data to Algolia, not the DSP.
*   **Governance Rule (General):** Any changes affecting upstream and downstream systems require **KDD sign-off**.
*   **Project-Specific Governance:** Specific architectural implementations within each backend require approval for each individual project.
*   **Unification Protocol:** Creating a unified cart across POS and Omni app requires direct engagement with and approval from **EA**.

### Pending Actions & Owners
| Action Item | Owner/Responsible | Context |
| :--- | :--- | :--- |
| Provide a single "Source of Truth" architecture diagram (noting current diagrams may be outdated). | **Enterprise Architecture (EA)** | Requested by Gopalakrishna Dhulipati. |
| Discuss and finalize the data schema to support searching for vouchers, brands, etc., beyond just products. | **Daryl Ng** / Team | Identified as a prerequisite for Algolia functionality. |
| Re-engage EA if unified cart development is required across POS and Omni channels. | **Project Team** | Per new constraint: cannot have unified cart without EA approval. |

### Key Dates & Follow-ups
*   **March 26, 2026:** Conversation took place between 01:55 and 03:05 UTC.
*   **Immediate Follow-up:** EA to share the updated architectural diagram.
*   **Next Step:** Schedule a discussion on data schema expansion (Daryl Ng).

**Reference URL:** https://chat.google.com/space/AAQAsFyLso4


## [70/70] Nikhil, Soumya, Andin Eswarlal
Source: gchat | Group: space/AAQAw0jsPYU | Last Activity: 2026-03-26T02:44:38.290000+00:00 | Last Updated: 2026-03-26T11:00:12.720075+00:00
**Daily Work Briefing: Data Impact Fix & Release Plan**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator; verifying data impact, coordinating backfill strategy, and finalizing the release plan.
*   **Soumya Singh:** Engineering Lead; providing status on the fix timeline and confirming technical impact details.
*   **Andin Eswarlal Rajesh (Rajesh):** Engineering Resource; aligned with Soumya regarding the target build date.
*   **Michael Bui:** CC'd for informational purposes.

**Main Topic**
Discussion regarding a critical data root cause fix, specifically addressing the impact of turning off the "IAB FF" feature flag on banner view and click event metrics, and determining the timeline for the next release.

**Decisions Made**
1.  **Fix Prioritization:** The team agreed to prioritize the fix due to its data impact.
2.  **Target Build Date:** The fix is targeted for Friday's build. Rajesh has confirmed alignment with this schedule.
3.  **Technical Impact Confirmation:** It was confirmed that while turning off the IAB FF may affect screen names for banner view and click events, the total count of impressions (banner view events) will be correctly recorded once the flag is disabled on affected versions.
4.  **Release Strategy:** If no backfill data can be secured from the Data Engineering (DE) team, the team will proceed with a "timer release" instead.

**Pending Actions & Ownership**
*   **Backfill Verification:** Nikhil Grover to quickly check with the Data Engineering (DE) team regarding potential backfill options for the affected period. If DE cannot assist, the timer release plan proceeds.
    *   *Owner:* Nikhil Grover
*   **Build Execution:** Execute the fix in Friday's build.
    *   *Owner:* Soumya Singh / Andin Eswarlal Rajesh

**Key Dates & Deadlines**
*   **2026-03-26 (Current Date):** Discussion took place early morning (UTC).
*   **Friday, 2026-03-27:** Target date for the build containing the fix.
*   **Tomorrow's Release:** Nikhil referenced a "tomorrow's release" in his final message; however, Soumya explicitly stated the target is Friday's build. This discrepancy should be clarified if "tomorrow" refers to Saturday or if the timeline shifted. (Note: The chat log states "targetting this Friday's build" and Nikhil later says "ready for tomorrow's release," implying Friday is the immediate next day relative to the conversation timestamp).

**Summary of Discussion Flow**
Nikhil Grover requested prioritization of a fix requiring one day of work, asked about backfill resources, and sought confirmation on data impact. Soumya Singh confirmed the timeline (Friday build), admitted uncertainty regarding backfill sources, and validated Nikhil's understanding of the IAB FF flag impact. Nikhil concluded by deciding to consult DE for backfill support immediately but authorized proceeding with a timer release if that fails.
