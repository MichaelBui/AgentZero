

## [1/52] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 16 | Last Activity: 2026-03-24T14:25:16.248000+00:00 | Last Updated: 2026-03-24T14:34:15.994169+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (Updated March 24, 14:30 UTC)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
Following the March 21 incident involving cyclic instability, volatility has persisted and evolved on **March 24 (UTC+8)**. The issue expanded from initial latency spikes to intermittent high error rates in `engage-my-persona-api-go` and `gamification-api`, alongside new degradations in `lt-gateway-app`. Alerts have continued intermittently throughout the morning and early afternoon, with a secondary surge occurring between **09:33 and 10:28 UTC** and recurring spikes observed from **13:19 to 14:25 UTC**.

**Status Summary & Timeline (Extended Incident)**
*   **MyInfo Confirmation Latency (`post_/new-myinfo/confirm`):**
    *   Persistent P90 spikes exceeding 1.8s continue. New peaks recorded at **13:19–10:24 UTC** and again at **14:24 UTC** (Metric: **1.911s**).
*   **Service Error Rates:**
    *   `engage-my-persona-api-go` shows recurring high error rate alarms (>0.1%) with triggered events at **13:19, 13:20, 13:24, 13:53, 14:06**, and **14:21**. Peak values reached **0.104% (13:24)** and **0.103% (13:20)**.
    *   `gamification-api` triggered critical high error rate alarms at **14:11** (Peak: **0.565%**) and **14:25** (Peak: **0.437%**), following the earlier 10:23 peak of 0.676%.
*   **Secondary Service Impact:**
    *   `lt-gateway-app` (`get_/rms/me/campaigns`) triggered a P99 latency alert (>1.8s) at **09:57** (Metric: 29.826s).
    *   `lyt-p13n-layout` (`post_/v1/scan-door/scratch-cards/claim`) triggered a P99 latency alert at **10:16** (Metric: 2.496s).
    *   Discount scheme loading success dropped below 99.9% at **13:36** (Value: 99.895%) and recovered by **13:39**.
    *   `frontend-gateway` (`get_/api/recommender/orchid`) success rate dropped to 99.885% at **13:37**, recovering by **14:11**.

**Pending Actions & Ownership**
*   **Investigate Recurring Spikes:** Prioritize analysis of `engage-my-persona-api-go` for the persistent error cycle (13:19–14:25) and sustained MyInfo latency. Owner: **Squad Dynamics**.
*   **Address Gamification Failures:** Address critical error rates in `gamification-api` (0.565% @ 14:11, 0.437% @ 14:25). Owner: **Squad Dynamics**.
*   **Correlate Multi-Service Degradation:** Investigate the correlation between late-morning/early-afternoon error spikes in `engage-my-persona-api-go` and success rate drops in `frontend-gateway` (Orchid requests) to determine if this is a systemic cascade. Owner: **Squad Dynamics/Journey**.

**Decisions Made**
*   **Pattern Shift:** The incident has evolved from isolated latency to a multi-service instability pattern involving error loops in `engage-my-persona-api-go` and `gamification-api`, plus intermittent success rate drops in `frontend-gateway`.
*   **Severity Escalation:** Recurring >0.5% error rates on `gamification-api` combined with sustained MyInfo latency require immediate root cause analysis for potential systemic resource exhaustion.

**Key Dates & Follow-ups**
*   **Active Window:** March 24 (UTC+8), extending from **06:49 – 14:30 UTC**.
*   **Reference Links (New):**
    *   Gamification Error Monitor #92939290 (Peak: 0.565% @ 14:11)
    *   MyInfo P90 Monitor #50879027 (Metric: 1.911s @ 14:24)
    *   Orchid Success Monitor #17448311 (Value: 99.885% @ 13:37)
    *   Discount Scheme Failed Monitor #50879029 (Value: 99.895% @ 13:36)


## [2/52] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Messages: 16 | Last Activity: 2026-03-24T14:23:19.146000+00:00 | Last Updated: 2026-03-24T14:34:39.062142+00:00
**Daily Work Briefing: Nikhil Grover & Michael Bui**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator; investigating new anomalies in product ad ranking and event data fidelity.
*   **Michael Bui:** Technical Lead (Engineering); previously assessing Store ID blockage, now required for immediate review of product event ranks.

**Main Topics**
1.  **Ad Delivery Inconsistency & Deployment Impact:**
    *   **Re-evaluation:** Michael Bui questioned if the Store ID mismatch (Store ID 17 vs. 165) blocks dynamic slot launch. Nikhil Grover characterized this as an edge case in multi-store scenarios, though Michael requested time to investigate further.
    *   **Historical Context:** The issue was previously unknown; ads failing on "See All" pages had been unaddressed for some time.

2.  **OSMOS Data Synchronization Inquiry:**
    *   **Mechanism Confirmed:** Updates are manual, not automated. Ram previously combined data from Michael and Calvin to facilitate updates. No automatic sync exists.

3.  **New Anomaly: Product Ad Rank & Event Fidelity (March 24):**
    *   **Ranking Disorder:** Nikhil Grover tested product events for new ad placements on homepage swimlanes. Segment data revealed erratic ranking orders: the first product showed rank 4, the second rank 9, and the third rank 1.
    *   **Missing Metadata:** Event logs are missing the `Ad ID` field entirely, which was previously present in event data.
    *   **Urgency:** Nikhil Grover emphasized there is "no reason" for ranks to be mixed up and requested a review of these findings early on March 25.

**Decisions Made**
*   **Launch Blockage Status Re-evaluated:** The Store ID issue remains classified as potentially not a hard block, pending Michael's deeper investigation.
*   **New Critical Issue Identified:** A separate critical anomaly exists regarding product ad ranking logic and missing `Ad ID` in events, halting confidence in the new placements regardless of the Store ID resolution.

**Pending Actions & Owners**
*   **Investigation of Block Status (Michael Bui):** Determine definitively if the Store ID mismatch prevents dynamic slot functionality. Nikhil Grover noted this requires more time to assess.
*   **Urgent Review of Ad Ranks (Michael Bui & Team):** Immediate analysis required for the erratic product ranks (4, 9, 1) and missing `Ad ID` in click events. Nikhil Grover requested this review by early March 25.
*   **Store List Refresh (Nikhil Grover):** Investigate how to refresh the current store list in OSMOS and verify if updates should strictly occur upon new store launches.

**Key Dates & Deadlines**
*   **March 24, 2026:** Session where Store ID issue was re-evaluated as an edge case; concurrently, Nikhil Grover discovered and reported severe anomalies in product ad ranks and missing event metadata via Segment.
*   **March 25, 2026 (Target):** Deadline for reviewing the new ranking and event data discrepancies as requested by Nikhil Grover.
*   **Original Launch Window (March 19–20):** Status remains suspended pending final determination regarding both the Store ID impact and the newly discovered ranking events.

**Historical Context Note**
Previous discussions established readiness for dynamic slots UAT with resolved `[1,3,3,5]` logic. The focus shifted to a critical ad delivery anomaly (Store ID mismatch) on March 19–20. On March 24, the narrative evolved: while OSMOS sync was confirmed as manual and the Store ID issue was downgraded by Nikhil Grover as an edge case, Michael Bui maintained the need for further investigation. Later that afternoon, the scope expanded significantly when Nikhil Grover identified a new critical failure in product ad placements on homepage swimlanes, characterized by random ranking orders (1, 4, 9) and missing `Ad ID` fields in Segment events.


## [3/52] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-03-24T14:04:26.600000+00:00 | Last Updated: 2026-03-24T14:35:17.032224+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Update)**
**Date:** March 24, 2026 (Afternoon)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 306

### Key Participants & Roles
*   **System/Tool:** Datadog App (Automated Monitoring)
*   **Notification Channel:** `@hangouts-ShoppingCartNotification`
*   **Ownership Teams:** `dpd-pricing`, `dpd-pricing-cart`.

### Main Topic
Instability persists in `frontend-gateway` across Wish List and Checkout operations. The system continues to exhibit high-frequency oscillation between trigger and recovery states. While P90/P99 latency spikes for Wish List operations have recently recovered, a new **P2 Alert** has triggered regarding checkout success rates (99.822%), confirming systemic degradation.

### Incident Timeline & Actions
**Previous Context:**
*   *See original summary for March 21 activity regarding `frontend-gateway` latency and initial cart spikes.*

**New Activity (March 24, UTC+0)**
*   **10:34–10:39 UTC:** Brief recovery of Wish List Write Latency. P90 dropped to 3.853s; P99 dropped to 3.853s.
*   **11:02–11:12 UTC:** **Checkout Success Rate Breach.** Monitor `21245708` triggered (Event ID `8557844181752745673`) with success rate at **99.822%**, immediately recovering to 100.0%.
*   **11:14–11:30 UTC:** Rapid oscillation on Read Operations:
    *   **11:14:** P90 `get_/api/wish-list/_id` triggered (Val: 1.802s). Recovered at 11:22 (Val: 1.15s).
    *   **11:20:** P99/P90 `get_/api/v2/shopping-list/guest` triggered (P99 Val: 4.295s, P90 Val: 4.295s). Recovered by 11:30.
*   **13:55–14:04 UTC:** Renewed latency spike on Wish List Read.
    *   **13:55:** P90 `get_/api/wish-list/_id` triggered (Val: 1.888s, Event ID `8558018529744820956`).
    *   **14:04:** Recovered to baseline (Val: 1.016s).

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** The pattern has expanded from write latency to include checkout success rate degradation (99.822%) and read latency instability.
*   **Scope:** Correlate the 11:02 Checkout breach with recent Wish List spikes. Investigate if shared dependency failures (database/caching) in `st-cart-prod` are driving cascading effects across write, read, and checkout endpoints.

### Decisions Made
*   **Priority Escalation:** Status remains **"Critical Incident"**. The recurrence of P2 alerts across Write, Read, and Checkout metrics indicates a systemic issue affecting the full cart lifecycle.
*   **Focus Shift:** Immediate analysis required for the 11:02 UTC checkout breach (Event ID `8557844181752745673`) combined with the persistent oscillation observed between 11:14 and 14:04.

### Key Dates & Follow-ups
*   **Critical Window:** Extended activity from March 20 through at least March 24, 14:04 UTC.
*   **Follow-up:** Investigate latest Event IDs `8558018529744820956` (P90 Wish List Read) and `8557844181752745673` (Checkout Success Rate).

**References:**
*   **Active Monitors:** `21245701` (P99 Write), `21245706` (P90 Write), `21245708` (Checkout Success), `21245720` (P90 Read Wish List), `21245718/21245721` (V2 Guest List).
*   **Service Tags:** `service:frontend-gateway`, `service:st-cart-prod`, `team:dpd-pricing`.


## [4/52] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Messages: 16 | Last Activity: 2026-03-24T13:09:49.596000+00:00 | Last Updated: 2026-03-24T14:35:52.466218+00:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
Automated alerts for the production environment (`env:prod`) continue to show instability in Mirakl integration and recurring latency issues extending from March 17 through March 24. The `fni-order-create` service exhibits a persistent cycle of DBP fetch failures, API errors, and route exceptions. Concurrently, `picklist-pregenerator` shows critical latency spikes on the night of March 20 and again on March 23.

**Incident Summary & Timeline (2026-03-15 to 2026-03-24)**
*   **Service:** `fni-order-create` (Mirakl Integration) – **Persistent Recurrence**
    *   **Pattern Continuation:** Instability spans March 17–24 with multiple recurrence windows.
    *   **March 23 Events:**
        *   06:46 UTC: Recovered "Failure occurred during fetching orders from DBP."
        *   06:49–13:09 UTC: Triggered and recovered "Exception Occurred At Mirakl Route" and "Error while calling APIs" around 13:04 UTC (duration ~5 mins).
    *   **March 24 Events:**
        *   13:04–13:09 UTC: Triggered and recovered "Exception Occurred At Mirakl Route" and "Error while calling APIs." Duration ~5 mins.
    *   *Note:* Confirms a continuous pattern of failures across six consecutive days (Mar 17–24).

*   **Service:** `seller` (`picklist-pregenerator`) – **Recurring Latency**
    *   **Cycle (Mar 20, 23:01:22 UTC):** P2 warning with metric value **3611.453s**.
    *   **Cycle (Mar 23, 23:01:22 UTC):** New P2 warning triggered at **23:01:22 UTC** with metric value **3607.424s** (Monitor ID `20383097`, tag `mkp-seller-job`).

*   **Service:** `fpon-seller-sap-picklist-reporter`
    *   **Status:** No new events reported in the current window (last event: Mar 20, 19:12 UTC P1).

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of expanded Mirakl integration instability affecting `fni-order-create`. The pattern now includes six distinct recurrence windows across six consecutive days (Mar 17–24), including recent events on Mar 23 and Mar 24.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Investigate root cause of extreme latency spikes in `picklist-pregenerator`. Cycles occurred on March 20 (3611s) and **March 23 (3607.424s)**. The recurrence suggests a systemic pipeline issue.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Review Monitor `29851723` logic for Apple Pay/Google Pay transactions. A test alert triggered and recovered on March 23 between 22:04 UTC and 22:42 UTC, indicating potential false positives or metric instability in payment processing monitoring.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Summary for Leadership**
Mirakl integration instability (`fni-order-create`) has persisted across six consecutive days (March 17–24), with new P2 events triggered and recovered on March 23 and March 24 at approximately 13:04 UTC, each lasting ~5 minutes. A critical recurring pattern of extreme latency emerged in `picklist-pregenerator`, with a spike recorded at **23:01:22 UTC on March 23** (metric value: 3607.424s), following the previous anomaly on March 20. Additionally, Monitor `29851723` for Apple Pay transactions generated multiple test alerts on March 23 evening requiring logic review. Urgent engineering review is required to address these systemic pipeline failures across Mirakl, SAP, and job processing logic.


## [5/52] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Messages: 3 | Last Activity: 2026-03-24T12:04:22.973000+00:00 | Last Updated: 2026-03-24T14:36:24.071237+00:00
# Daily Work Briefing: #dd-fpg-watchdog-alert

### Key Participants & Roles
*   **Datadog App:** Automated monitoring system.
*   **@hangouts-dd-dpd-watchdog-alert:** Targeted notification channel.
*   *Note: Interactions remain purely automated.*

### Main Topic
The channel tracks **P3 [DPD Watchdog] infrastructure incidents** in Production. Logs show recurring transient issues (excluding `tcp_retrans_jump` and `full_disk_forecast`) aggregated by `story_key` over a 30-minute window. The alert message consistently reads: "Datadog is unable to process your request."

### Incident Summary & Status Update
**Historical Resolved Incidents:**
1.  **Mar 05–17:** 11 distinct events triggered and recovered within the period.
2.  **Mar 18/19:** Incident `story_key`: `10aaf170-dac2-5fec-97bf-cfd442f8706b`. Duration ~5.6 hours. Status: **Resolved**.

**Newly Resolved Incidents:**
*   **Mar 20, 2026:** Incident `story_key`: `2787bcd7-d59e-58f0-961a-8f578260cd84`. Triggered 05:14 UTC, Recovered 09:37 UTC. Duration ~4.4 hours. Status: **Resolved**.
*   **Mar 22, 2026:** Incident `story_key`: `08f5624a-14f1-50e5-9a4a-7418b3602953`. Triggered Mar 22 20:14 UTC, Recovered Mar 22 23:36 UTC. Duration ~3.4 hours. Status: **Resolved**.

**Current Active Incidents:**
*   **Date/Time:** March 24, 2026, at 12:04 UTC.
*   **Incident ID (`story_key`):** `978f6328-424c-53dd-83c8-6411c3aa2158`.
*   **Status:** **[Triggered]** (Active).
*   **Alert Message:** "Datadog is unable to process your request."
*   **Severity:** P3.

### Pending Actions & Ownership
*   **Immediate Action:** Investigate the active trigger on March 24 (`story_key`: `978f6328-424c-53dd-83c8-6411c3aa2158`). The specific error message suggests a failure within the monitoring system's ingestion or processing pipeline.
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Investigation Note:** Recurrence is frequent (Mar 17, 18/19, 20, 21, and now Mar 24). The error "Datadog is unable to process your request" has persisted across all recent incidents, indicating a systemic issue with the watchdog mechanism rather than isolated infrastructure faults.

### Decisions Made
*   None recorded yet. Pending investigation into the persistent ingestion failure on March 24.

### Key Dates & Follow-ups
*   **Latest Event:** March 24, 2026, at 12:04 UTC (New Trigger).
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Monitor for recovery. If resolution exceeds the recent average (~3-4 hours) or if the error persists, escalate to SRE/Platform Engineering to investigate Datadog ingestion pipelines.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Datadog Monitor Link:** [View in Datadog](https://app.datadoghq.eu/monitors/17447511)
*   **Active Incident (Mar 24):** https://app.datadoghq.eu/monitors/17447511?group=story_key%3A978f6328-424c-53dd-83c8-6411c3aa2158&from_ts=1774352871000&to_ts=1774354071000&event_id=8557906816914739721

### Monitor Configuration
*   **Query:** `events("source:watchdog (story_category:infrastructure -story_type:(tcp_retrans_jump OR full_disk_forecast)) env:(PROD OR production OR prod)").rollup("count").by("story_key").last("30m") > 0`


## [6/52] BCRS - UAT
Source: gchat | Group: space/AAQACfHCuNI | Messages: 1 | Last Activity: 2026-03-24T11:44:49.961000+00:00 | Last Updated: 2026-03-24T14:36:46.741885+00:00
**BCRS UAT Daily Briefing Summary (Updated: 24 Mar 2026)**

**Key Participants & Roles**
*   **Sathya Murthy Karthik:** UAT Lead/Coordinator (Provided status update as of 24 Mar).
*   **Finance Team:** Currently reviewing failed test cases for Returns & Refunds and In-store Pre-order; pending sign-off actions.
*   **CS & RPA Teams:** Completed testing for Returns & Refunds and Scan & Go; reporting passed/pending counts.

**Main Topic**
Status update as of 24 Mar 2026 at 7:30 PM covering MP SKU Listing, In-store Pre-order, and Returns & Refunds. While MP SKU Listing is fully tested with sign-off due today (24 Mar), critical alignment issues regarding BCRS eligible FOC items in In-store Pre-order require a separate retest and sign-off by 25 Mar. Finance Team review remains the primary bottleneck for finalizing Returns & Refunds.

**Pending Actions & Owners**
*   **Returns & Refunds (OG):** CS and RPA testing completed; Finance team must review failed cases and update statuses. Re-delivery requires separate testing/sign-off. Scan & Go test cases added, completed by RPA/CS; pending Finance review.
    *   *Owner:* Finance Team.
*   **In-store Pre-order:** 1 failed test case (FOC) identified. Business alignment required for handling BCRS eligible FOC items before retest and separate sign-off.
    *   *Owner:* S&G/Testing Team; Sign-off by 25 Mar 2026.
*   **Marketplace SKU Listing:** Testing concluded; no failures.
    *   *Owner:* Finance Team (Sign-off due 24 Mar).
*   **Finance Testing:** Alignment on failed cases completed; Finance Team to update status of 8 failed and 11 pending cases.

**Decisions Made & Clarifications**
*   **MP SKU Listing:** Sign-off scheduled for completion by 24 Mar 2026 (Monday).
*   **In-store Pre-order:** Sign-off rescheduled to 25 Mar 2026 (Tuesday) due to FOC item alignment requirements.
*   **Returns & Refunds:** Development and internal testing (CS/RPA) complete; sign-off pending Finance review of failures and Scan & Go cases.

**Status Snapshot (as of 24 Mar, 7:30 PM)**
*   **MP SKU Listing:**
    *   **Passed:** 65 | **Pending:** 0 | **Failed:** 0
*   **In-store Pre-order:**
    *   **Passed:** 20 | **Pending:** 0 | **Failed:** 1 (FOC item alignment required).
*   **Returns & Refunds / Scan & Go:**
    *   **CS Testing:** 26 Passed, 1 Pending, 1 Failed (Re-delivery).
    *   **Finance Testing:** 9 Passed, 11 Pending, 8 Failed.

**Key Dates & Deadlines**
*   **24 Mar 2026 (Mon):** MP SKU Listing sign-off deadline; Current reporting time (7:30 PM).
*   **25 Mar 2026 (Tue):** Scheduled retest and sign-off for In-store Pre-order.
*   **20 Mar 2026:** Previous status date.

**Historical Context**
*   MP SKU Listing testing was not present in previous updates; now concluded with full pass rate.
*   In-store Pre-order failures dropped from 4 (on 23 Mar) to 1, but a new business alignment issue regarding FOC items necessitates the delay to 25 Mar.
*   Returns & Refunds testing scope expanded to include Scan & Go cases, now completed by CS and RPA.


## [7/52] Ping Pong 🏓
Source: gchat | Group: space/AAQAnryjAA8/cFKeWJ-k288 | Messages: 5 | Last Activity: 2026-03-24T10:42:04.599000+00:00 | Last Updated: 2026-03-24T14:37:00.696439+00:00
**Daily Work Briefing: Ping Pong 🏓**

**Key Participants & Roles**
*   **Zaw Myo Htet:** Initiator of initial communication (Status inquiry).
*   **Michael Bui:** Respondent (Confirmed unavailability; currently in meeting).
*   **Karuna Kemmu:** New participant joining the thread later.

**Main Topic/Discussion**
The exchange began with Zaw Myo Htet initiating a status check ("Pong?") regarding Michael Bui's availability. Michael responded at 09:37 UTC indicating he was occupied with another meeting. Later, Karuna Kemmu entered the conversation to confirm presence. At 10:42:21 UTC, Karuna confirmed that four participants were now present in the space ("Four here now :)"). The primary theme remains availability scheduling for a session or interaction; no specific work deliverables or project tasks were discussed.

**Pending Actions & Ownership**
*   **Action:** Finalize rescheduling for the group interaction once Michael Bui is free.
    *   **Owner:** Karuna Kemmu / Zaw Myo Htet (Implicit coordination required).
    *   **Context:** While four people are currently available, Michael Bui remains in a meeting (confirmed at 10:39 UTC) and cannot join immediately.

**Decisions Made**
*   No concrete decisions were reached regarding the time or topic of the interaction due to Michael's continued unavailability. The group has effectively assembled, pending Michael's departure from his current meeting.

**Key Dates, Deadlines & Follow-ups**
*   **Interaction Date:** March 24, 2026.
*   **Timeline Updates:**
    *   09:36 UTC: Inquiry sent by Zaw Myo Htet.
    *   09:37 UTC: Michael Bui responds (still in meeting).
    *   10:38:50 UTC: Karuna Kemmu asks, "Anyone still there?"
    *   10:39:21 UTC: Michael Bui confirms, "Still in meeting."
    *   10:42:04 UTC: Karuna Kemmu reports, "Four here now :)."
*   **Next Steps:** Await Michael Bui's availability to proceed with the session.

**Resource Details**
*   **Space Name:** Ping Pong 🏓
*   **URL:** https://chat.google.com/space/AAQAnryjAA8
*   **Message Count:** 5


## [8/52] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY | Last Activity: 2026-03-24T09:39:52.319000+00:00 | Last Updated: 2026-03-24T10:37:27.372784+00:00
**Updated Briefing: BCRS Firefighting Group**
**Date:** March 24, 2026 (Latest activity: 9:39 AM)
**Source:** Google Chat Space & Shared UAT Tracker (66 messages total)

### **Key Participants & Roles**
*   **Prajney Sribhashyam:** Project Lead/Test Coordinator.
*   **Sathya Murthy Karthik:** QA Lead (Scanning/Glitch focus).
*   **Michael Bui / Dany Jacob / De Wei Tey:** Finance/Data/Invoice specialists.
*   **Onkar Bamane:** Technical Integration/SAP Liaison.
*   **Alvin Choo:** Product/Release Manager.
*   **Hendry Tionardi, Shiva Kumar Yalagunda Bas, Andin Eswarlal Rajesh:** Technical Support & Development.
*   **Sneha Parab:** Stakeholder (SKU/Feature inquiries).
*   **Daryl Ng:** Production deployment status liaison.

### **Main Topics**
1.  **Critical System Crash (Order #75577957):** Sathya Murthy Karthik reports an inability to open Order #75577957 on mobile devices; the app crashes repeatedly. Backend access also fails with an "order type unspecified" error, preventing invoice generation.
2.  **Re-delivery Use Case & SAP Integration:** Immediate grooming session requested for 'Re-delivery' logic (Ticket: DPD-807) involving order service metadata and RPA charging logic.
3.  **Scan & Go (SnG) Fraud Prevention:** Investigation into blocking multiplication functions for BCRS SKUs to prevent deposit fee evasion.
4.  **Deposit Refund Display Logic:** Previous report (7:50 AM) noted deposits refunded but not struck out on receipts; new crash issues compound visibility problems.
5.  **Staff App Priority:** Prajney designated Staff App issues as high priority for closure today.

### **Decisions Made**
*   **Mobile Release:** Proceeded with mobile release on March 6 (Confirmed by Alvin Choo).
*   **Linkpoints Logic:** Confirmed Linkpoints issued for BCRS SKUs, but *not* for Deposit items.
*   **Invoice Formatting:** Issue with missing minus signs (Order #75502500) redeployed on March 13; cache clearing instructed.
*   **Staff App Urgency:** Staff App defects prioritized for resolution by end of day, March 24.

### **Pending Actions & Owners**
| Action Item | Owner(s) | Status/Context |
| :--- | :--- | :--- |
| **Order #75577957 Crash Resolution** | Sathya Murthy Karthik / Technical Team | **Critical (Mar 24, 9:39 AM):** Mobile app crashes when opening order; backoffice returns "order type unspecified." Invoice generation blocked. Immediate investigation required. |
| **'Re-delivery' Grooming Session** | Prajney Sribhashyam / Michael Bui / De Wei Tey | **High Priority (Mar 24, 2:34 AM):** Schedule session today for DPD-807. Focus: Order service metadata and RPA charging logic. Thread active with 4 replies. |
| **Scan & Go Glitch Resolution** | Sathya Murthy Karthik / Daryl Ng / Team | **Critical (Mar 24, 5:17 AM):** Investigation into SnG glitch preventing SKU substitution fraud. Discussion on multiplication block feasibility. Thread active with 17+ replies. |
| **Staff App Closure** | Prajney Sribhashyam / Zaw Myo Htet / Daryl Ng | **Urgent (Mar 24, 5:28 AM):** All Staff App issues to be closed today. Thread active with 24 unread replies. |
| **Refund Negative Balance & Strike-out Logic** | Sathya Murthy Karthik / Team | **Active (Mar 24, 7:50 AM):** Critical refund scenarios identified regarding negative cart totals and missing strike-outs on deposits. |

### **Key Dates & Deadlines**
*   **March 6:** Mobile release executed.
*   **March 13:** Invoice format redeployed.
*   **March 24 (Morning):** Target for Staff App resolution and 'Re-delivery' grooming session.
*   **March 24 (9:39 AM):** Critical system crash reported on Order #75577957 requiring immediate triage.

### **Historical Context Retained**
*   Existing e-comm test accounts deemed unusable for Pre-order staff app; new BCRS CF items and specific GWP SKUs (e.g., Coca-Cola Zero) required.
*   Original deadline for SAP Deposit API development was Feb 20 (missed/risk noted).
*   Re-delivery flow testing ongoing with audio issues reported on March 16 awaiting resolution.
*   Deposit SKU linking investigation ongoing due to failure to link post-publishing.


## [9/52] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/77DpGxXYs38 | Last Activity: 2026-03-24T09:37:08.747000+00:00 | Last Updated: 2026-03-24T10:37:54.229096+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Initiator; defines scope, timing, and data requirements for workshop slides.
*   **Tiong Siong Tee:** Clarifies technical scope (Payment/FPPay) and presentation depth (high-level flow vs. tech details).
*   **Michael Bui:** Validates the strategic purpose of the deliverable (enabling CoMall to build solutions).
*   **Hui Hui Voon:** Identified as the owner of the "D&T Scope for Project Light Workshop."

**Main Topic**
Preparation of presentation slides for the **Project Light Workshop**, specifically focusing on two Spotlight Topics:
1.  **Spotlight Topic 2: Payment** (Scheduled for Thursday, 09:34 AM slot).
2.  **Spotlight Topic 5: RMN** (Scheduled for tomorrow, 04:45 PM – 05:45 PM).

**Decisions Made**
*   **Scope:** The data flow diagrams must cover both **Payment** and **FPPay**.
*   **Data Source:** Use the latest available versions of existing diagrams.
*   **Strategic Alignment:** The content is intended to enable **CoMall** to understand requirements for building solutions under Project Light.

**Pending Actions & Ownership**
*   **Create/Update Data Flow Diagrams:**
    *   **Scope:** Payment and FPPay.
    *   **Requirement:** Must be the latest versions available.
    *   **Owner:** Team (Assigned by Alvin Choo; Tiong Siong Tee to clarify specific depth).
*   **Prepare Slides for Workshop:**
    *   **RMN Slide:** Due prior to tomorrow's 4:45 PM slot.
    *   **Payment Slide:** Due prior to Thursday's 1:00 PM slot.
    *   **Owner:** Alvin Choo (Lead) and assigned team members.

**Key Dates & Deadlines**
*   **Tomorrow (Date inferred as March 25, 2026):**
    *   **Time:** 4:45 PM – 5:45 PM.
    *   **Event:** Spotlight Topic 2: Payment presentation preparation.
*   **Thursday (March 26, 2026):**
    *   **Time:** 1:00 PM – 2:00 PM.
    *   **Event:** Spotlight Topic 5: RMN presentation preparation.

**Resources Referenced**
*   Google Docs Presentation: `D&T Scope for Project Light Workshop` (URL provided in chat).


## [10/52] Ping Pong 🏓
Source: gchat | Group: space/AAQAnryjAA8 | Last Activity: 2026-03-24T09:36:20.806000+00:00 | Last Updated: 2026-03-24T10:38:10.266773+00:00
**Daily Work Briefing: Ping Pong Space (Resource ID: AAQAnryjAA8)**

**Key Participants & Roles**
*   **Michael Bui:** Initiator and coordinator. Created the space to facilitate scheduling for informal table tennis (PP/TT) play sessions.
*   **Karuna Kemmu:** Active participant sharing resources.
*   **Zaw Myo Htet:** Active participant initiating a direct query regarding play availability.

**Main Topic/Discussion**
The conversation centers on establishing a coordination channel for informal ping pong activities. Initial discussions focused on recruiting interested colleagues and confirming interest following Michael Bui's "Anyone?" inquiry. The dialogue recently shifted to specific resource sharing and immediate scheduling inquiries. Karuna Kemmu shared an Instagram Reel highlighting pricing tiers for jump rackets (€1–€370) titled "Power of the unsaid," suggesting a discussion on equipment costs or novelty items. Shortly thereafter, Zaw Myo Htet initiated a direct availability check with the message "Pong?"

**Pending Actions & Ownership**
*   **Action:** Respond to Zaw Myo Htet's inquiry ("Pong?") regarding immediate play availability.
    *   **Owner:** Michael Bui and interested team members.
    *   **Context:** Recent activity indicates a pending response to this direct query (last reply noted as 54 minutes prior to current snapshot).
*   **Action:** Expand group membership by identifying additional colleagues.
    *   **Owner:** Michael Bui.
    *   **Context:** Previously acknowledged as necessary to prevent missing potential participants ("I may miss some").

**Decisions Made**
No formal scheduling decisions or time slots were established in the initial phase. The only confirmed operational decision remains the creation of the dedicated Google Chat space for coordination.

**Key Dates & Follow-ups**
*   **Space Creation:** March 19, 2026, at 06:57 UTC (Michael Bui).
*   **Initial Inquiry:** March 19, 2026, at 09:29 UTC (Michael Bui asked "Anyone?").
*   **Resource Sharing:** March 22, 2026, at 12:44 UTC (Karuna Kemmu shared Instagram reel regarding racket pricing).
*   **Availability Check:** March 24, 2026, at 09:36 UTC (Zaw Myo Htet asked "Pong?").

**Reference Data**
*   **Space URL:** https://chat.google.com/space/AAQAnryjAA8
*   **Total Messages:** 6 (Updated from 4).


## [11/52] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4 | Last Activity: 2026-03-24T09:32:02.160000+00:00 | Last Updated: 2026-03-24T10:38:34.166797+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Space Creator; Lead coordinating the briefing.
*   **Daryl Ng, Gopalakrishna Dhulipati, Tiong Siong Tee, Michael Bui, Akash Gupta:** Designated "Project Light Attack and Defence Leads".
*   **Hui Hui Voon:** Owner of the D&T Scope for Project Light Workshop document.

**Main Topic**
Following the transition to active strategic planning ("Room 2") on March 24, the team has moved from high-level definition to specific slide preparation. Alvin Choo initiated immediate collaboration on **"RMN"** and **"Payment"** slides via a shared Google Presentation (D&T Scope for Project Light Workshop). The focus remains on six "Spotlight Topics," with active work now directed at the content within these areas.

**Pending Actions & Ownership**
*   **Action:** Finalize content for "RMN" and "Payment" slides in the D&T Scope document.
    *   **Ownership:** Alvin Choo (initiated), Hui Hui Voon (Document Owner).
    *   **Status:** In progress; specific file shared March 24, ~9:32 AM UTC.
*   **Action:** Clarify backend API responsibilities with CoMall regarding personalization and orchestration.
    *   **Ownership:** Michael Bui (to note and document).
*   **Action:** Finalize the Attack/Defence team composition pending Dennis's confirmation following Alvin Choo's email.
    *   **Ownership:** Alvin Choo.
*   **Action:** Address technical clarifications raised by Tiong Siong Tee regarding Inventory visibility, Corporate Control alignment, and Product management portal structure (FP vs. Sellers).
    *   **Ownership:** Alvin Choo and Gopalakrishna Dhulipati.

**Decisions Made**
*   **Session Protocol:** Participants are encouraged to listen during live sessions; questions should be raised in the chat space.
*   **Platform Resilience:** Integration testing is a strict technical requirement prioritized from "Day 1."
*   **Governance Structure:** FPG cannot be treated merely as a standard seller due to governance conflicts; distinct data structures or models are required for FP vs. non-governance sellers (Clarified by Gopalakrishna Dhulipati).
*   **Gamification:** Confirmed not part of the DSP scope.

**Key Dates & Follow-ups**
*   **Slide Collaboration Initiated:** March 24, 2026 (~9:32 AM UTC) – Alvin Choo requested work on RMN and Payment slides in the D&T Scope document.
*   **Diagram Shared:** March 23, 2026 (4:27 PM UTC) by Michael Bui.
*   **Session Start ("Room 2"):** March 24, 2026 (1:02 AM UTC).
*   **Spotlight Topics List Published:** March 24, 2026 (3:14 AM UTC).
*   **Email Sent for Team Confirmation:** March 24, 2026 (3:51 AM UTC) by Alvin Choo.
*   **Space URL:** https://chat.google.com/space/AAQAsFyLso4

**Summary of Activity Log**
*   **March 23, 4:27 PM:** Michael Bui shared a customer journey diagram to facilitate upcoming sessions.
*   **March 24, 1:02 AM:** Alvin announced the start of "Room 2" sessions.
*   **March 24, 3:14 AM:** Alvin defined six spotlight topics (Inventory, Payment, Loyalty, Backoffice, RMN, AI).
*   **March 24, 3:51 AM:** Daryl Ng inquired about team assignments; Alvin confirmed emails sent to Dennis.
*   **March 24, 6:28 AM:** Tiong Siong Tee questioned the product management portal structure (FP vs. Sellers); Alvin flagged for "Backoffice" discussion.
*   **March 24, 7:38 AM:** Gopalakrishna Dhulipati rejected treating FPG as a standard seller due to governance conflicts.
*   **March 24, ~9:32 AM:** Alvin Choo directed the team to work on "RMN" and "Payment" slides within the D&T Scope document shared by Hui Hui Voon.


## [12/52] Project Light: Mobilization and Planning Workshop Day 1 - Mar 24
Source: gchat | Group: space/AAQAA8d_pfI | Last Activity: 2026-03-24T09:23:41.504000+00:00 | Last Updated: 2026-03-24T10:38:53.329555+00:00
**Daily Work Briefing: Project Light – Mobilization & Planning Workshop (Day 1)**
**Date:** March 24, 2026
**Resource Link:** https://chat.google.com/space/AAQAA8d_pfI

**Key Participants & Roles**
*   **Jacob Yeo:** Meeting facilitator; coordinated participant dial-in.
*   **Vivian Lim Yu Qian:** Presenter; led UI Walkthrough Demo and defined technical/action items.
*   **Tiong Siong Tee:** UX Lead; proposed agenda flow (High-level UX first) and requested Figma access.
*   **Cecilia Koo Hai Ling:** Design/UX Contributor; shared DoorDash references, UI assets, and **NTUC FairPrice category/store examples**.
*   **Christine Yap Ee Ling:** Internal Liaison; handling internal distribution of the Figma link.
*   **Rajesh Dobariya:** Stakeholder; reviewed references regarding delivery categorization.

**Main Topic/Discussion**
The team conducted a high-level User Experience (UX) walkthrough and UI review for Project Light, expanding reference analysis to include local competitors:
*   **Navigation & Filters:** Clarification on whether filters on category pages should be pre-configured ("dynamic") or retrieved dynamically.
*   **UI Clarity:** Identified that the toggle selection between "Scheduled" and "Quick" modes is not currently obvious in the current design.
*   **Compliance:** Discussed the potential need to separate eGift cards from vouchers to meet compliance requirements.
*   **Reference Analysis:** Reviewed DoorDash's first-time app open screen for UX inspiration regarding delivery categorization (brands, categories). Additionally, Cecilia Koo Hai Ling shared specific NTUC FairPrice examples to illustrate store/category structures:
    *   *SharkNinja Official Store:* https://www.fairprice.com.sg/category/sharkninja-official-store
    *   *FP Unilever Tag:* https://www.fairprice.com.sg/tag/fp-unilever
*   **Engagement:** The FairPrice tag link was viewed by 15 of 21 participants.

**Decisions Made**
*   **Filter Logic:** No final consensus recorded; the solution requires a decision on filter behavior (dynamic vs. pre-configured) pending the "solution/integration" discussion mentioned by Vivian.
*   **Reference Alignment:** Agreed that DoorDash's approach to breaking down delivery into categories and brands serves as a valid reference (confirmed by Rajesh). The FairPrice examples were accepted as supplementary data for local context.

**Pending Actions & Owners**
1.  **Share Figma Link:** Christine Yap Ee Ling will send the Figma link via a separate internal chat in response to Tiong Siong Tee's request.
2.  **Resolve Filter Logic:** Vivian Lim Yu Qian (and the technical team) must finalize the decision on category page filter behavior (dynamic vs. pre-configured).
3.  **Refine UI Toggle:** The design team must address the lack of visual clarity for the "Scheduled/Quick" toggle selection.
4.  **Compliance Review:** Determine if eGift cards must be standalone from vouchers.
5.  **Analyze Local Benchmarks:** UX Lead (Tiong Siong Tee) to review the shared FairPrice links (SharkNinja store and Unilever tag) for specific categorization patterns relevant to Project Light.

**Key Dates & Follow-ups**
*   **Event:** Project Light Mobilization and Planning Workshop Day 1 (March 24, 2026).
*   **Status:** Session concluded; materials shared via chat.
*   **Next Step:** Internal distribution of Figma link by Christine Yap Ee Ling.


## [13/52] QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs/YgGvvuD2Ow8 | Last Activity: 2026-03-24T08:44:20.923000+00:00 | Last Updated: 2026-03-24T10:39:28.740279+00:00
**Daily Work Briefing: Ad Slot Configuration Changes (QE <-> All Tribes)**

**Key Participants & Roles**
*   **Michael Bui:** Initiator of the change; responsible for managing the change window and subsequent reset.
*   **Komal Ashokkumar Jain:** Stakeholder managing testing timeline and impact analysis.
*   **Milind Badame:** Notified stakeholder who followed up on UAT status.

**Main Topic**
Discussion regarding temporary modifications to ad slot positions in swimlanes, specifically the impact on User Acceptance Testing (UAT) scripts hardcoded to positions 1 and 3.

**Decisions Made**
*   Ad slots were reconfigured temporarily during the testing phase, causing existing UAT tests tied to positions 1 & 3 to fail.
*   The system is scheduled to revert to the original configuration (positions 1 & 3) immediately upon conclusion of UAT.
*   **Status Update:** Testing did not conclude as originally anticipated by the March 19 deadline; Michael Bui confirmed on March 24 that work was "not fully completed yet."

**Pending Actions & Ownership**
*   **UAT Completion Confirmation:** Milind Badame queried Michael Bui regarding UAT status on March 24. Michael responded that testing is ongoing and not yet complete. The reset protocol remains dormant until full completion is confirmed.
*   **Execution Oversight:** Michael Bui retains responsibility for managing the extended change window and executing the ad slot reset (back to positions 1 & 3) immediately after UAT concludes.

**Key Dates, Deadlines & Follow-ups**
*   **Original Start Date:** March 12, 2026 (Changes active "starting today").
*   **Query Date:** March 24, 2026 (Milind Badame asked if UAT was completed).
*   **Response Date/Timestamp:** March 24, 2026 at 08:44 UTC (Michael Bui replied: "It's not fully completed yet").
*   **Scheduled End Date (Original):** End of Next Week (March 19, 2026). *Note: This deadline passed without completion.*
*   **Follow-up:** Post-UAT reset to default positions (1 & 3) required upon final confirmation.

**Summary of Chronology**
On March 12, 2026, Michael Bui informed the group that ad slot changes were underway, warning that UAT tests hardcoded for positions 1 and 3 would fail. Komal Ashokkumar Jain inquired about the End Time (ETA), with Michael confirming the activity would conclude by "next week EOW." Komal subsequently clarified the active window (March 12 through next EOW) and notified Milind Badame and Madhuri Nalamothu of this status update.

On March 24, 2026, Milind Badame initiated a follow-up by asking Michael Bui directly: "Hi is the UAT done?" Contrary to the expectation that testing might have finished prior to or on the original deadline (March 19), Michael Bui responded at 08:44 UTC stating, "It's not fully completed yet." Consequently, the original end date of March 19 is superseded by the ongoing status. The ad slot configuration remains in its modified state pending final UAT sign-off and a subsequent reset request from Michael Bui.


## [14/52] Team Starship
Source: gchat | Group: space/AAQAX9iKYf0 | Last Activity: 2026-03-24T08:39:23.981000+00:00 | Last Updated: 2026-03-24T10:40:00.498424+00:00
**Daily Work Briefing: Team Starship (Updated)**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Operations/Testing Lead.
*   **Danielle Lee:** Biz Ops/S&G Representative.
*   **Vivian Lim Yu Qian:** Product/Design Liaison.
*   **Alvin Choo:** Compliance Lead / Technical POC.
*   **Zi Ying Liow:** Frontend/Promotion Logic Inquiry.
*   **Sathya Murthy Karthik:** Shared Omni Roadmap update (March 2026).
*   **Daryl Ng, Qiuyan Tian, Ravi Goel:** New contributors to Scan@Door AI discussion.

**Main Topics & Decisions**

1.  **BCRS Refunds Testing Status (Critical Update)**
    *   **Status:** Prajney reported 9 out of 18 test cases failed.
    *   **Breakdown:** 6 unrelated UAT-only issues; 3 show inconsistencies between DBP/RPA and SAP records.
    *   **Action:** Prajney is collaborating with the RPA team to resolve SAP/DBP inconsistency immediately. Target closure remains today (March 24), though spillover risk persists into tomorrow morning.

2.  **Bug Report: App Icon Display (DPD-783)**
    *   **Issue:** Vivian reported a regression where the app icon displays a Christmas theme instead of the default.
    *   **Action:** Bug ticket **DPD-783** created for urgent resolution ("asap").

3.  **New Request: Cart-Level Coupon Allocation (GP Calculation)**
    *   **Request:** Alvin Choo relayed a request from Ryan to stop considering cart-level coupon allocation per SKU.
    *   **Objective:** Ensure accurate Gross Profit (GP) calculation for products.
    *   **Decision/Pending:** The team is currently determining whether to park this requirement in the "Project Light" list.

4.  **Frontend Tag Mapping Inquiry**
    *   **Inquiry:** Zi Ying Liow sought clarification on the mapping logic between promotion methods and frontend tags. No resolution documented yet; requires technical verification.

5.  **OMNI Project Status & Compliance**
    *   **Omni Roadmap Review:** PMs must review the "Omni Roadmap Consolidated from Jan 2026." A list of items to deprioritize is required by **EOD tomorrow (March 25)**.
    *   **OMNI-1345 (Sales Breakdown):** MP Business has instructed an indefinite **hold** due to foundational changes in the consolidated fulfilment business model. No further work until requirements are finalized.
    *   **OMNI-1282:** Status remains de-prioritized; ticket requires formal change from "Define."

6.  **Operational Pilots**
    *   Operations continues piloting the "picker app enhanced for CT58" on newer models (DT50S, DT66S). Prajney emphasized testing new models before store rollout.

7.  **CHAS Verification Flow**
    *   Auto-verification via MyInfo remains technically feasible but outside current "Light" scope. Vivian to verify technical assumptions with Serene.

8.  **Scan@Door: AI Personalisation Discussion (New)**
    *   **Context:** Daryl Ng initiated a discussion regarding Scan@Door personalization using AI to issue personalized vouchers, shifting from rule-based logic.
    *   **Impact:** Requires Backend (BE) changes estimated at **2 weeks**.
    *   **Timeline:** Targeted go-live is mid-April.
    *   **Decision Pending:** The team must determine if this requirement should be prioritized given the development timeline and resource constraints.
    *   **Stakeholders:** Daryl Ng, Danielle Lee, Qiuyan Tian, Vivian Lim Yu Qian, Alvin Choo, Ravi Goel (6 unread replies as of 9:09 AM).

**Pending Actions & Owners**

| Action Item | Owner | Deadline/Note |
| :--- | :--- | :--- |
| **Urgent Fix:** Revert app icon display (DPD-783) | Engineering Team / Andin Eswarlal Rajesh | ASAP |
| Resolve DBP/RPA & SAP inconsistency (BCRS Refunds) | Prajney Sribhashyam / RPA Team | Risk of spillover to Tomorrow AM |
| Submit list of items to deprioritize from Jan 2026 Omni Roadmap | All PMs | **EOD Tomorrow (March 25)** |
| Update OMNI-1282 status (De-prioritize) | Alvin Choo / Koklin Gan | Pending confirmation |
| **PAUSE** work on OMNI-1345 requirements | All Stakeholders | Until business model is finalized |
| **Clarify:** Cart-level coupon allocation logic & Project Light inclusion | Alvin Choo / Ryan's team | Pending decision |
| **Investigate:** Promotion method to frontend tag mapping | Zi Ying Liow / Tech Team | As needed |
| Prioritize Scan@Door AI Personalisation (BE impact assessment) | Danielle Lee, Daryl Ng, Tech Leads | Immediate review required |
| Prepare for BCRS progress review & capacity planning | Danielle Lee | See Meeting Below |

**Key Dates & Follow-ups**

*   **Meeting Rescheduled:** Weekly Epics meeting postponed to **Wednesday, March 12 (tomorrow) at 11:00 AM**. *Note: Date context suggests this refers to the upcoming Wednesday relative to current briefing.*
    *   **Location:** Level 12 Room 18 (subject to availability; virtual or pantry table as backup).
    *   **Agenda:** BCRS work progress review, capacity planning, and Scan@Door prioritization decision.
*   **Reference Tickets:** SHOP-3779, OMNI-1099, DPD-100, **DPD-783**, OMNI-1345, OMNI-1282, OMNI-1421.


## [15/52] DPD x Platform Engineering
Source: gchat | Group: space/AAQAcjNXKpA | Last Activity: 2026-03-24T08:36:08.434000+00:00 | Last Updated: 2026-03-24T10:40:28.445224+00:00
**Daily Work Briefing: DPD x Platform Engineering**

**Key Participants & Roles**
*   **Madhawa Mallika Arachchige:** On-call team restructuring lead.
*   **Alvin Choo:** Team Lead/Organizational structure owner.
*   **Michael Bui:** Stakeholder for RMN on-call grouping.
*   **Kyle Nguyen:** Infrastructure/Platform Engineering (Reviewer, Incident Triage).
*   **Sampada Shukla:** Reliability Engineer (Incident lead for Picking App).
*   **Wai Ching Chan:** Operations/On-call liaison.
*   **Daryl Ng:** Incident Analyst.
*   **Akash Gupta:** User reporting Bastion access failure; proposing IaC policy change for on-call.
*   **Nicholas Tan, Harry Akbar Ali Munir:** Engaged in Bastion and Cluster capacity investigations.

**Main Topics & Discussions**
1.  **Critical Picking App & Backoffice Incident (March 23):** Sampada Shukla reported significant issues starting at 03:40 PM SGT on March 23. Operations observed `SocketTimeoutExceptions` on Android and `Connection Resets` on the Web between 03:40–03:45 PM SGT.
    *   *Root Cause Analysis:* GKE logs indicate the cluster (`jarvis-prod-ap-v2`) reached hard memory limits at 15:22 SGT (0/6 nodes available). At 15:39 SGT, Kubernetes initiated forced pod evictions of `picking-service` pods due to extreme memory pressure.
    *   *Impact:* Forceful eviction severed active network sockets, causing the observed timeouts and resets.
    *   *Context:* This follows a previous March 9 incident involving load balancer churn; current findings point to cluster capacity scaling limits rather than LB updates.
2.  **On-Call Restructuring Methodology Debate:** Akash Gupta proposed shifting new on-call configuration from Terraform (IaC) to direct Datadog UI management to facilitate manual overrides and reduce PR overhead. The team is reviewing this proposal against the strict two-PR Terraform process.
3.  **Security & Dependency Updates:** Lester Soriano upgraded `lt-strudel-api-go` for vulnerability `GO-2026-4603` but encountered pipeline failures due to a `golangci-lint` version mismatch (v1.24 build vs v1.25.8 target).
4.  **Security & Infrastructure:** Akash Gupta reported Bastion unavailability in PROD (`asia-southeast1-c`). Natalya Kosenko flagged potential manual deletion of Datadog resources causing Terraform drift.

**Pending Actions & Owners**
*   **Resolve Cluster Capacity Scaling:** Investigate why the cluster failed to scale out during peak traffic (03:40 PM SGT) and implement fixes for memory limits. *(Owners: Kyle Nguyen, Nicholas Tan)*
*   **Evaluate On-Call Tooling Strategy:** Assess Akash Gupta's proposal to use Datadog UI instead of Terraform for new on-call teams. *(Owner: Platform Engineering)*
*   **Restore Bastion Access:** Investigate PROD `asia-southeast1-c` Bastion inaccessibility affecting order republishing. *(Owners: Nicholas Tan, Kyle Nguyen, Harry Akbar Ali Munir)*
*   **Resolve Go Pipeline Error:** Reconcile `golangci-lint` version mismatch for Lester Soriano.
*   **Review Infrastructure PR:** Natalya Kosenko's PR `infra-gcp-fpg-titan/344` requires review from Kyle, Nicholas, Madhawa, and Dodla Gopi Krishna.
*   **Plan Resource Scale-Down:** Daryl Ng to coordinate with Kyle Nguyen, Maou Sheng Lee, and Alvin Choo regarding QC Food resource reduction pending ES confirmation.

**Decisions Made**
*   *Tentative:* The team is debating whether to retain the Terraform-based change-freeze process or adopt direct Datadog UI management for on-call teams. No final decision recorded yet.
*   **QC Food Status:** Disabling confirmed on production (as of March 19). Resource scale-down planning initiated pending ES confirmation.

**Key Dates & Follow-ups**
*   **March 23, 03:40–03:45 PM SGT:** Critical incident involving `SocketTimeoutExceptions` and `Connection Resets` due to GKE memory exhaustion and pod evictions.
*   **March 16, 08:58 UTC:** Akash Gupta submitted proposal to replace Terraform with Datadog UI.
*   **March 19, 11:47 AM SGT:** Daryl Ng confirmed QC Food tile disabled on production.
*   **March 13:** Previous critical incident regarding Picking App 502 errors (now superseded by capacity findings).


## [16/52] Soo Ngee Tong
Source: gchat | Group: dm/3L_55SAAAAE | Last Activity: 2026-03-24T08:25:52.255000+00:00 | Last Updated: 2026-03-24T10:40:51.586407+00:00
**Daily Work Briefing: Google Chat Summary**

**Key Participants & Roles**
*   **Michael Bui:** Initiator of the inquiry; demonstrates vigilance regarding cybersecurity threats.
*   **Soo Ngee Tong (Resource):** Subject Matter Expert/Approver; provided confirmation on email legitimacy and context for audit communications.

**Main Topic**
Verification of two emails received by Michael Bui regarding **"KPMG FY 2025 Audit - UAR Self-Review"** to confirm their authenticity and clarify differences between them. The discussion also highlighted potential phishing risks involving URL redirection via Google Classroom.

**Decisions Made**
*   Confirmed legitimacy: Both emails are authorized updates related to **IT audit issues**.
*   Clarification of content: The first email was an initial transmission without context; the second email contains full context and an uploaded video.
*   Risk acknowledgment: Michael Bui acknowledged the need for caution regarding external links, specifically citing the risk of Google Classroom URLs being used for phishing redirection.

**Pending Actions & Ownership**
*   **Action:** Review and process the second email (containing context and video) as instructed by Soo Ngee Tong.
    *   **Owner:** Michael Bui
*   **Action:** Maintain vigilance against potential URL-based phishing attempts while handling audit links.
    *   **Owner:** Michael Bui

**Key Dates & Follow-ups**
*   **Date of Conversation:** March 24, 2026 (Times: 08:23 AM – 08:25 AM UTC).
*   **Reference Project:** KPMG FY 2025 Audit - UAR Self-Review.
*   **Follow-up Status:** Immediate acknowledgment provided by Michael Bui ("Noted, thanks for your confirmation!"). No specific future deadline was set beyond the immediate processing of the confirmed emails.

**Resource Metadata**
*   **Participant:** Soo Ngee Tong
*   **Message Count:** 3
*   **Source URL:** https://chat.google.com/dm/3L_55SAAAAE


## [17/52] QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs | Last Activity: 2026-03-24T08:05:57.413000+00:00 | Last Updated: 2026-03-24T10:41:20.877951+00:00
**Daily Work Briefing: QE <-> All Tribes** (Updated)

**Key Participants & Roles**
*   **Patrick Thun:** Lead/Coordination.
*   **Madhuri Nalamothu:** QA Lead/Test Execution.
*   **Milind Badame:** QA Engineer.
*   **Hang Chawin Tan:** DevOps/Backend Support.
*   **Daryl Ng / Michael Bui:** Dev/Product.
*   **Komal Ashokkumar Jain:** Reported New Defect.
*   **Zaw Myo Htet:** Backend/Voucher Developer (New).
*   **Tiong Siong Tee:** Involved in OTP/Android investigation.
*   **Others:** Dany Jacob, Piraba Nagkeeran, Yangyu Wang, Andin Eswarlal Rajesh.

**Main Topics & Discussion**
1.  **E-Voucher Application Error (Critical):** Milind Badame reported a `404 Invalid voucher` error during testing. Backend response indicates logic failure. Investigation initiated with @Zaw Myo Htet. *Status:* Open/Investigating.
2.  **LinkPoints Test Failure:** Tests remain disabled in regression; awaiting ETA on resolution from Dev Team (Michael Bui). *Status:* Blocked.
3.  **Postal Code Offer Label Missing:** Milind Badame reported a missing `label` attribute for the first product in "TestHasOffer swimlane" for Postal code **098619**. Requires investigation.
4.  **QC Food Tile Removal Testing:** Daryl Ng confirmed testing is underway on the removal of QC (O2O) food tiles on the Omni home page.
5.  **Load Testing & Environment Stability:** Small-scale load test completed on **5 Mar, 11 AM–1 PM** (UAT LEAP env). Scale-down operations executed successfully.
6.  **DC Membership Logic Discrepancy:** Critical inconsistency where users have `DC member` flags in back office but lack active plans/UI awards. Investigation ongoing regarding award logic and payment errors for new DC trial members.
7.  **E2E Test Failures & UI Defects:**
    *   **Cart Page (Critical):** Komal Ashokkumar Jain reported a critical flaw where switching from Standard to Express delivery causes cart items to "stick," allowing users to place orders with ineligible items for 1HD. Referenced by @Daryl Ng and @Andin Eswarlal Rajesh.
    *   **General UI:** Broken alignment on the third highlighted product; unidentified "view buttons" require clarification (Refs: Andin Eswarlal Rajesh). iOS navigation issues persist, including disappearing swimlanes, EVoucher errors, Express delivery label changes ("Get in 1Hr"), and 1-hour filter chip failures.
8.  **Android OTP Blank Screen (New):** Milind Badame reported a blank screen issue for OTP on Android versions v12 and below. Investigation requested with @Tiong Siong Tee. *Status:* New/Open (7 replies, last reply 9:16 AM).

**Pending Actions & Ownership**
*   **E-Voucher Bug:** Investigate `404 Invalid voucher` error causing application failure. *Owner: Milind Badame / @Zaw Myo Htet.* (High Priority).
*   **LinkPoints Fix Status:** Provide ETA for the LinkPoints fix to re-enable tests. *Owner: Dev Team / Michael Bui.*
*   **Postal Code Label Debug:** Investigate missing `label` for Postal code 098619 in TestHasOffer swimlane. *Owner: Milind Badame / Dev Team.*
*   **Cart Express Delivery Bug (New):** Investigate and fix logic allowing ineligible items for 1HD when switching delivery modes. *Owners: Komal Ashokkumar Jain, Daryl Ng, Andin Eswarlal Rajesh.*
*   **General Cart & Payment:** Resolve Cart alignment, view buttons, and payment failures for new DC trial members. *Owners: Milind Badame, Andin Eswarlal Rajesh, Madhuri Nalamothu, Dev Team.*
*   **QC Removal Testing:** Monitor progress of QC (O2O) food tile removal on Omni home. *Owner: Daryl Ng / QA Team.*
*   **Android OTP Blank Screen (New):** Investigate blank screen for Android v12 and lower versions. *Owner: @Tiong Siong Tee / Milind Badame.*

**Decisions Made**
*   Ad slot changes proceed; known test impacts acknowledged.
*   No decision yet on LinkPoints fix, Cart view buttons, Express delivery eligibility logic, E-Voucher application failure, or Android OTP blank screen; awaiting dev clarification and investigation results.

**Key Dates & Deadlines**
*   **5 Mar:** Load testing window (completed).
*   **16 Mar:** DC membership logic discrepancy logged.
*   **17 Mar:** UI defects reported on cart page (06:23–06:33 AM).
*   **18 Mar:** LinkPoints fix ETA required; Postal code 098619 issue flagged.
*   **20 Mar:** Critical Express delivery bug flagged by Komal Ashokkumar Jain at 11:05 UTC.
*   **24 Mar:** E-Voucher error reported by Milind Badame (02:39 UTC); Android OTP blank screen issue raised (08:05 UTC).


## [18/52] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/52Irp8aqAi4 | Last Activity: 2026-03-24T08:03:55.714000+00:00 | Last Updated: 2026-03-24T08:07:48.504983+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Daryl Ng:** Initiator of the discussion regarding resource allocation and backend requirements.
*   **Alvin Choo:** Confirmed prioritization decisions and directed communication channels for planning.

**Main Topic**
Discussion centered on the lack of a Product Manager (PM) currently assigned to the **Scan@Door AI personalisation** feature and the subsequent need for Backend (BE) changes. The core objective was determining how to prioritize this work within the Omni board given the technical requirements.

**Decisions Made**
*   The Scan@Door AI personalisation initiative requires immediate prioritization on the **Omni board**.
*   This confirmation followed Daryl's query regarding the absence of a PM and the necessity for BE modifications.

**Pending Actions & Ownership**
*   **Action:** Post the prioritization update to the **"Team Starship"** channel.
    *   **Owner:** Alvin Choo (implied via instruction "can share this").
*   **Action:** Solicit the specific implementation plan from Team Starship.
    *   **Owner:** Alvin Choo (instruction: "ask what is the plan").

**Key Dates, Deadlines & Estimates**
*   **Estimated Duration:** 2 weeks (attributed specifically to Backend development).
*   **Timestamp of Discussion:** March 24, 2026.
    *   Initial query: 08:00:29 UTC
    *   Confirmation and directives: 08:03:20 – 08:03:55 UTC

**Summary Context**
The conversation confirms that while the Scan@Door AI personalisation feature currently lacks PM involvement, it necessitates Backend engineering changes. Alvin Choo validated Daryl Ng's assessment that this must be prioritized on the Omni board. Consequently, the team is instructed to communicate this status and request a formal plan from Team Starship within their designated channel. The estimated timeline for the required BE work is two weeks.


## [19/52] ❗ Important Email
Source: gchat | Group: space/AAQAUJW8HMo | Last Activity: 2026-03-24T08:00:35.319000+00:00 | Last Updated: 2026-03-24T08:09:28.578855+00:00
**Daily Work Briefing Summary (Updated)**

**Key Participants & Roles**
*   **Michael Bui (You):** Managing Osmos support, event RSVPs, FileVault compliance, performance feedback, and Project Light coordination.
*   **Miguel Ho Xian Da (FairPrice):** Lead requesting OSMOS integration; organizer of the RMN discussion with Accenture.
*   **Jazz Tong:** Head of Platform Engineering; on leave until Mar 23, 2026.
*   **Tong A. Yu / Lilibeth Villena (Accenture):** Proposing working sessions and sharing availability for integration architecture.

**Main Topics**
1.  **Project Light & RMN Integration:**
    *   **Meeting Rescheduled:** [Placeholder] Discussion with Accenture on RMN is now scheduled for **Thursday, March 26, 2026, from 2:00 PM – 3:00 PM SGT**. Attendees: Michael Bui, Rajiv Kumar Singh (Required), Bryan Choong (Optional).
    *   **Context:** FairPrice Group is scaling Smart Carts/Digital Price Cards/IPOS. Current disparate CMSs require a decision on centralized vs. short-term integration. Accenture proposed 30-min sessions in the week of Mar 16-20; due to conflicts, March 26 was selected.
    *   **Project Light (Original):** Previously rescheduled to Mar 19, 4:00–5:00 PM SGT. *Note: This creates a conflict with the BCRS Warroom.*
2.  **BCRS - Refunds Issue Warroom:**
    *   Scheduled for **Thursday, March 19, 2026, from 3:30 PM – 4:30 PM SGT** (Prajney Sribhashyam).
    *   **Conflict Alert:** Overlaps with Project Light meeting. Immediate resolution required to attend both or delegate.
3.  **D&T Power Breakfast Planning:**
    *   New event "D&T Power Breakfast" announced by Trina Boquiren.
    *   **Planning Meeting:** Tuesday, March 31, 2026, from 1:30 PM – 2:00 PM SGT at FairPrice Hub-11-L11 Mocha (6) [TV] or Google Meet. Objective: Brainstorm engaging activities.
4.  **Performance Feedback:** Scheduled for Wednesday, Mar 18, 2026, at 4:00 PM SGT with Alvin Choo and Winson Lim.

**Pending Actions & Ownership**
*   **RMN Meeting RSVP (Michael Bui):** Submit "Yes" to Miguel Ho's invitation for March 26, 2:00–3:00 PM SGT.
*   **Project Light/Warroom Conflict:** Resolve scheduling conflict between Project Light (Mar 19, 4:00 PM) and BCRS Warroom (Mar 19, 3:30 PM). Reply "Yes" to both invitations immediately.
*   **Performance Meeting RSVP:** Confirm attendance for Mar 18, 4:00 PM SGT.
*   **D&T Breakfast Planning RSVP:** Respond to Trina Boquiren's invitation for March 31 planning session.
*   **OSMOS Architecture:** Provide architectural details on SmartCarts and IPOS to finalize long-term integration strategy with Accenture.

**Decisions Made**
*   **RMN Integration Timeline:** Team agreed to prioritize a focused working session on March 26 for architecture definition after previous slots (Mar 19-20) failed due to conflicts.
*   **OSMOS Capability:** Confirmed feasible short-term integration (video via CDN, image via FPG service); long-term decision pending Accenture recommendation on centralized CMS vs. API distribution.

**Critical Dates & Deadlines**
*   **Mar 18, 2026:** Performance Feedback Meeting.
*   **Mar 19, 2026:** BCRS Warroom (3:30 PM) & Project Light (4:00 PM). *Conflict.*
*   **Mar 26, 2026:** RMN Discussion with Accenture (2:00–3:00 PM SGT). Link: `https://meet.google.com/koe-uzer-xbd` | PIN: 583106441.
*   **Mar 31, 2026:** D&T Power Breakfast Planning Session (1:30–2:00 PM); FileVault Final Deadline.


## [20/52] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Last Activity: 2026-03-24T08:00:29.011000+00:00 | Last Updated: 2026-03-24T08:09:59.962550+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Sneha Parab:** Lead/Manager; coordinating cross-team support, SAP/API integration blockers.
*   **Michael Bui:** Engineering/RMN Architect; managing architecture updates, infrastructure compliance, and reporting Omni Home swimlane issues.
*   **Alvin Choo:** Leadership; addressing feedback loops, release schedules, epic queries, and AI personalization prioritization.
*   **Gopalakrishna Dhulipati:** Lead; overseeing risk registers, delivery approvals, service key rotation with SRE, and clarifying PIC for store purchase surveys.
*   **Others Active:** Daryl Ng (raised recent inquiry), Andin Eswarlal Rajesh, Olivia, Koklin, Zaw.

**Main Topics**
1.  **SAP/Deposit SKU Integration Blocker:** Marketplace lacks deposit data for SAP API integration. Proposed manual UD failed MP Ops sign-off due to poor PM communication; Olivia rejected new technical solutions. Immediate action from SAP team required.
2.  **Requirement Clarity (BCRS):** Michael Bui flagged that "follow existing ones" is unacceptable acceptance criteria for BCRS deposit posting. Explicit UAT scenarios are required for Definition of Ready (DoR).
3.  **Infrastructure Compliance:** Bitnami ending free Docker images impacts `sonic_raptor` and `mkp-fairnex`. Migration is mandatory.
4.  **Service Key Rotation:** Gopalakrishna Dhulipati requested leads take ownership with the SRE team; discussion moved to a dedicated room.
5.  **B2B Testing Alignment:** Sneha Parab raised queries on finalized B2B testing procedures. Zaw requires guidance on producing MP SKUs specifically for B2B testing.
6.  **New Epic Inquiry (OMNI-1157):** Daryl Ng raised an item from the weekly epics (Jira link: OMNI-1157). Ravi indicated this action should only be performed for the new app. Alvin Choo and Gopalakrishna Dhulipati were tagged to clarify status.
7.  **Omni Home Data Discrepancy:** Michael Bui reported an issue where the swimlane in Omni Home sends a different store ID compared to the "See All" screen. The specific team to check/fix this is currently under investigation (involving Daryl Ng).
8.  **Store Purchase Survey PIC:** Gopalakrishna Dhulipati initiated a query regarding the responsible person-in-charge (PIC) for the survey on products purchased at stores; discussion remains open with multiple replies.
9.  **Scan@Door AI Personalization (New):** Daryl Ng noted the Scan@Door AI personalization project currently lacks PM involvement. With required Backend (BE) changes, he queried if this must be prioritized on the Omni board. The topic is under active review by Alvin Choo.

**Pending Actions & Owners**
*   **OMNI-1157 Clarification:** Confirm if the item applies solely to the new app as per Ravi's feedback; coordinate with Daryl Ng. (Owners: Alvin Choo/Gopalakrishna Dhulipati)
*   **Service Key Rotation:** Leads to take ownership of rotation with SRE. Review details in dedicated room. (Owner: All Leads / Gopalakrishna Dhulipati)
*   **B2B Testing Procedure:** Clarify process for producing MP SKUs and confirm alignment status. Response required from Gopalakrishna Dhulipati regarding Zaw's inquiry. (Owner: Sneha Parab/Gopalakrishna Dhulipati)
*   **SAP Timeline Resolution:** Push SAP team to explore deposit SKU data solutions; provide timeline. (Owner: Sneha Parab/Alvin Choo/Gopalakrishna Dhulipati)
*   **BCRS Requirements:** Define explicit UAT scenarios with Koklin. (Owner: Alvin Choo/Gopalakrishna Dhulipati)
*   **Infrastructure Migration:** Address Bitnami Docker image end-of-life. (Owner: Engineering Team/Michael Bui)
*   **RAW Forms Review:** Review Risk Register for DPD RAW forms; confirm handovers and renew expired forms. Deadline: Tomorrow EOD. (Owner: All Leads/Sazali Bin Mohammed Ali's team)
*   **Omni Home Store ID Bug:** Identify the correct team to resolve the store ID mismatch between Omni Home swimlane and "See All" screen. (Owner: Michael Bui/Daryl Ng)
*   **Survey PIC Identification:** Confirm the responsible party for the product purchased at store survey. (Owner: Gopalakrishna Dhulipati/All Leads)
*   **Scan@Door AI Prioritization:** Determine prioritization status on the Omni board given the lack of PM and required BE changes. Response pending from Alvin Choo. (Owner: Daryl Ng/Alvin Choo)

**Decisions Made**
*   **RMN Architecture:** Michael Bui updated current, future, and transition architecture diagrams.
*   **Townhall Coordination:** Team to meet Hui Hui post-townhall; no full Q&A scheduled.
*   **Release Status:** Questions remain regarding holding today's regular app release (pending confirmation).

**Key Dates & Deadlines**
*   **RAW Forms Review:** Due Tomorrow EOD.
*   **Townhall Meeting:** Today post-townhall session.
*   **Chee Hoe Support:** Effective end of March for Product Catalogue/MarTech scope.
*   **Bitnami Migration:** Ongoing (immediate action required).


## [21/52] Ching Hui Ng
Source: gchat | Group: dm/1vXYPsAAAAE | Last Activity: 2026-03-24T07:58:29.672000+00:00 | Last Updated: 2026-03-24T08:10:16.060302+00:00
**Daily Work Briefing: Google Chat Summary**

**Resource:** Ching Hui Ng
**Date of Conversation:** March 24, 2026 (Updates to existing context from March 20)

### Key Participants & Roles
*   **Ching Hui Ng:** Initiator; focused on the integration roadmap for Osmo screens and Smart Cart collaboration.
*   **Michael Bui:** Respondent; shifted focus to technical feasibility and proposed adding Nikhil for roadmap discussions.

### Main Topic
Discussion regarding the technical integration between **Osmo** and **Smart Cart**, specifically determining the roadmap for integrating screens on Osmos and how Smart Cart fits into that strategy.

### Pending Actions & Ownership
*   **Action:** Finalize meeting scheduling (Originally proposed for Friday, March 27).
    *   **Status:** Meeting was initially tentatively set for Friday after 2:30 PM but was subsequently **postponed** by Ching Hui Ng.
    *   **Owner:** Both parties to reschedule.
*   **Action:** Prepare content for the rescheduled session.
    *   **Owner:** Ching Hui Ng (to provide roadmap details).
    *   **Owner:** Michael Bui (to prepare on technical feasibility).

### Decisions Made
*   **Meeting Format:** Confirmed as an online session (in-person declined due to workshops).
*   **Attendance Adjustment:** Michael Bui requested that **Nikhil** be added to the meeting to address the roadmap, while Michael will focus specifically on technical feasibility.
*   **Scheduling Outcome:** The proposed slot of "Friday after 2:30 PM" was mutually acknowledged as open but ultimately postponed for a future date.

### Key Dates & Follow-ups
*   **Conversation Date:** March 24, 2026 (07:52 – 07:58 UTC).
*   **Previous Constraints:** Michael Bui remains unavailable before 2:30 PM on Fridays due to full-day workshops next week; on leave the following week (March 30–April 3).
*   **Current Status:** The meeting originally tentatively booked for Friday, March 27, has been postponed. A new time must be agreed upon after Michael's leave or during a future open window.

### Action Required
1.  **Ching Hui Ng** to propose a new specific date/time once the Friday slot is cleared, noting that Nikhil needs to be included for roadmap discussions.
2.  **Ching Hui Ng** to prepare details regarding the Osmo screen integration roadmap and Smart Cart involvement.
3.  **Michael Bui** to await the rescheduled invitation and prepare technical feasibility inputs.


## [22/52] BCRS ECOMM SAP POSTING
Source: gchat | Group: space/AAQA-ICuJRM | Last Activity: 2026-03-24T07:40:19.421000+00:00 | Last Updated: 2026-03-24T08:11:41.329825+00:00
**Daily Work Briefing: BCRS ECOMM SAP POSTING & Refunds UAT (Mar 24 Update)**

**Key Participants & Roles**
*   **Wei Fen Ching:** Accounting verification lead.
*   **De Wei Tey:** Provided B2B credit note examples; confirmed refund status for order 75567408.
*   **Yap Chye Soon Adrian / Hendry Tionardi:** SAP/DBP technical owners handling invoice creation, GI processing, and system validation.
*   **Onkar Bamane / Prajney Sribhashyam:** Stakeholders managing UAT validation, coordination, and SAP finance queries.
*   **Lai Shu Hui:** Participant in upcoming resolution call.

**Main Topic**
UAT testing for BCRS E-commerce involving Sales Posting to SAP (F420) and Refunds. Focus has shifted from initial invoice validation to resolving specific SAP posting discrepancies, generating missing invoices/GIs, and clarifying treatment for fully redeemed orders (Linkpoints/eVouchers). Immediate priority is addressing Finance's reporting anomalies regarding FPON orders via a scheduled technical discussion.

**Status of Issues & Updates**
*   **Credit Note Verification:** On Mar 24, Wei Fen Ching flagged a credit note lacking BCRS deposit details (shared image), prompting review with Yap Chye Soon Adrian.
*   **Invoice & GI Generation:** De Wei Tey requested invoice generation for orders **#75578021** and **#75577802**. Hendry Tionardi confirmed the issue was resolved, noting invoices will auto-create within 15 minutes.
*   **Goods Issue (GI):** On Mar 24 at 05:43 AM, De Wei Tey requested assistance with GI for order **#75578449**; Hendry Tionardi confirmed completion ("Done").
*   **SAP Posting Anomaly:** Prajney Sribhashyam reported a critical query on Mar 24 at 04:42 AM. Finance highlighted that FPON orders fully redeemed via Linkpoints and eVouchers show no sales posting in SAP, despite DPD team confirmation of backend posting.
*   **Meeting Scheduled:** On Mar 24 at 07:40 UTC, Prajney Sribhashyam scheduled a Google Meet call for **4:00 PM** to discuss the FPON posting discrepancy. Attendees include @Onkar Bamane, @Wei Fen Ching, and @Lai Shu Hui (Link: https://meet.google.com/mkx-oxib-fpk).

**Pending Actions & Ownership**
1.  **FPON Resolution Meeting:** Attend the scheduled call at 4:00 PM to validate SAP treatment for fully redeemed orders. **(Owner: Onkar Bamane, Wei Fen Ching, Lai Shu Hui)**.
2.  **Verify Credit Note Details:** Investigate Wei Fen Ching's observation regarding the credit note missing BCRS deposit data. **(Owner: Yap Chye Soon Adrian / DBP Team)**.
3.  **API Integration Confirmation:** De Wei Tey seeks confirmation on API connectivity between Zendesk and DBP used by Jimmy to pull information. **(Owner: Wai Ching Chan / Onkar Bamane)**.

**Decisions Made**
*   Confirmed that invoices for orders #75578021 and #75577802 are now processing automatically (15-min window).
*   Goods Issue for order #75578449 successfully completed by Hendry Tionardi.
*   Finance has identified a discrepancy in SAP posting logic for fully redeemed FPON orders requiring immediate technical validation via the 4:00 PM call.

**Key Dates & Follow-ups**
*   **Mar 21:** Initiated BCRS deposit refund testing (Order #75570370).
*   **Mar 24, 00:55 UTC:** Wei Fen Ching flagged credit note without BCRS deposit.
*   **Mar 24, 03:43 UTC:** De Wei Tey requested invoices for orders #75578021 and #75577802.
*   **Mar 24, 03:46 UTC:** Hendry Tionardi confirmed issue resolution; auto-invoice generation confirmed.
*   **Mar 24, 04:42 UTC:** Prajney Sribhashyam raised query regarding FPON orders with no SAP sales posting despite DPD confirmation.
*   **Mar 24, 05:43 UTC:** GI requested for order #75578449; completed immediately.
*   **Mar 24, 07:40 UTC:** Scheduled Google Meet call at 16:00 (UTC) to resolve FPON posting anomaly.

**Immediate Follow-up:** Attend the 4:00 PM meeting with Onkar Bamane, Wei Fen Ching, and Lai Shu Hui to validate the SAP treatment for fully redeemed FPON orders, confirm API data flow between Zendesk and DBP, and verify the BCRS deposit status on the flagged credit note.


## [23/52] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/71IimpFl3FE | Last Activity: 2026-03-24T07:35:40.019000+00:00 | Last Updated: 2026-03-24T08:11:55.570481+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Sathya Murthy Karthik:** Reported a financial discrepancy regarding cart totals after a specific refund scenario.
*   **Daryl Ng:** Escalated the issue and requested assistance to investigate the reported anomaly.
*   **Wai Ching Chan:** Identified as the primary owner for investigating the reported issue (tagged by Daryl Ng); provided root cause analysis.

**Main Topic**
The discussion concerns a negative monetary value appearing in a shopping cart total under specific conditions:
1.  The cart was fully paid via a promo code.
2.  A BCRS deposit was simultaneously paid by credit card.
3.  A refund was subsequently issued for the BCRS item only, causing the refund amount to exceed the remaining final pay amount.

**Root Cause Analysis & Resolution**
*   **Findings:** Wai Ching Chan confirmed that the negative $ amount is due to refunded items' values exceeding the final payment amount.
*   **Classification:** This behavior is identified as **existing system logic**, not a defect. It occurs when a cart is fully paid by a promo code, even without BCRS deposits involved.
*   **Status:** The issue has been resolved and closed; no further investigation or root cause analysis of a bug is required.

**Pending Actions & Ownership**
*   **Action:** None (Investigation complete; behavior confirmed as intended).
*   **Owner:** N/A (Issue resolved by Wai Ching Chan's finding).

**Decisions Made**
*   It was determined that the negative cart total is expected system behavior for scenarios involving full promo code payments followed by partial refunds that exceed the remaining balance. No code changes or logic updates are required.

**Key Dates & Follow-ups**
*   **Incident Reported:** March 24, 2026, at 07:31 UTC (Sathya Murthy Karthik).
*   **Escalation Requested:** March 24, 2026, at 07:32 UTC (Daryl Ng).
*   **Root Cause Identified:** March 24, 2026, at 07:35 UTC (Wai Ching Chan).
*   **Next Steps:** None required. The matter is closed based on the existing behavior confirmation.

**Source Reference**
*   **Space:** BCRS Firefighting Group
*   **Link:** https://chat.google.com/space/AAQAgT-LpYY


## [24/52] DPD AI Guild
Source: gchat | Group: space/AAQA5_B3lZQ/9rNMaZEmMZE | Last Activity: 2026-03-24T07:12:30.805000+00:00 | Last Updated: 2026-03-24T07:45:56.644409+00:00
**Daily Work Briefing: DPD AI Guild**
**Resource:** Google Chat Space (URL: https://chat.google.com/space/AAQA5_B3lZQ)
**Date:** March 24, 2026

**Key Participants & Roles**
*   **Nicholas Tan:** Contributor; initiated the discussion by sharing industry news.
*   **Dodla Gopi Krishna:** Participant; provided commentary on leadership implications.
*   **Tan Nhu Duong:** Participant; questioned future development strategies regarding open source.

**Main Topic**
Discussion centered on a recent report from *The Independent* (shared by Tan) detailing Mark Zuckerberg's deployment of an "AI CEO" to assist in running Meta. The group debated the operational implications, including potential leadership redundancy and the possibility of the tool being open-sourced. Nicholas Tan characterized the trend as "tokenmaxxing."

**Decisions Made**
No formal decisions were made during this exchange. The conversation remained speculative regarding future corporate actions by Meta.

**Pending Actions & Ownership**
*   **None:** No action items, tasks, or ownership assignments were generated from this chat thread.

**Key Dates & Follow-ups**
*   **March 24, 2026 (06:57:45 UTC):** Nicholas Tan shared the link to *The Independent* article titled "Mark Zuckerberg builds AI CEO to help him run Meta."
*   **March 24, 2026 (06:59:45 – 07:12:30 UTC):** Follow-up commentary regarding Mark Zuckerberg's potential redundancy and the tool's future availability.

**Summary of Conversation Flow**
The discussion began with Nicholas Tan providing a link to an article about Meta's new AI CEO initiative. Dodla Gopi Krishna immediately interpreted this as a sign that Mark Zuckerberg might no longer need to serve as CEO, jokingly predicting he could be laid off soon. Tan Nhu Duong shifted the focus to development strategy, asking when (or if) the technology would be open-sourced. Nicholas Tan concluded the thread with the term "Tokenmaxxing," implying the move is driven by hype or token accumulation rather than pure operational efficiency.


## [25/52] SRE / Network / DBA / DevOps / Infra
Source: gchat | Group: space/AAAAYX-ew1s | Last Activity: 2026-03-24T06:58:54.051000+00:00 | Last Updated: 2026-03-24T07:46:36.686461+00:00
**Daily Work Briefing: SRE / Infrastructure Team**

**Key Participants & Roles**
*   **Madhawa Mallika Arachchige:** Requests PR reviews/merges for Datadog configurations.
*   **Natalya Kosenko:** Raises IaC strategy questions, requests Terraform support, and submits compliance-related PRs.
*   **Kalana Thejitha:** Reports pipeline failures in new projects (Soni-BE).
*   **Lester Santiago Soriano:** Reports Go versioning conflicts in CI/CD pipelines.
*   **Boning He:** Requests access to pricing Terraform workspaces via PR #722.
*   **Dodla Gopi Krishna:** Requests Terraform review.
*   **Zheng Ming:** Reported US-Central1 internet connectivity failure for AI agents; opened ticket GCD-8941.
*   **Wai Ching Chan:** Reports bastion connectivity issues affecting team operations; raised ticket GCD-8954.
*   **Calvin Phan:** Raised request for CloudSQL subnets for project SOT-SONI creation; ticket DSD-11066.
*   **Himal Hewagamage & Isuru Dilhan:** Primary reviewers/approvers for PRs and incident support.
*   **Mohit Niranwal:** Stages non-production verification for infrastructure changes.
*   **Tan Nhu Duong, Kyle Nguyen, Maou Sheng Lee, Nicholas Tan:** Tagged stakeholders/reviewers.

**Main Topics**
1.  **Datadog Infrastructure & Compliance:** Multiple requests to review/merge PRs (#135–#148) related to `fp-datadog-eu`. Strategic discussion regarding IaC for Datadog log pipelines and RBAC enforcement continues.
2.  **Terraform & Workspaces Management:** New PR **#719** submitted by Natalya Kosenko. Previous requests included PR #716. A failed Terraform plan (`run-CZVLtajJGbLVojLM`) and ticket GCD-8900 remain active.
3.  **CI/CD Pipeline Failures:**
    *   **Soni-BE:** `golden pipeline` clone step failing on new projects; SSH key status questioned.
    *   **lt-strudel-api-go:** Build failure after upgrading Go to `1.25.8`; `golangci-lint` conflict noted.
4.  **Cloud Networking (New):** AI agents in `us-central1` mothership subnets cannot connect to the internet. Zheng Ming raised ticket **GCD-8941** for Cloud NAT.
5.  **Bastion Connectivity:** Wai Ching Chan reported bastion connectivity issues affecting team operations; raised ticket **GCD-8954**.
6.  **Database Subnet Request (New):** Calvin Phan requested subnets for CloudSQL to support the **SOT-SONI** project creation. Ticket **DSD-11066** opened. DBA team is coordinating with @Himal Hewagamage regarding this request.

**Pending Actions & Ownership**
*   **Merge/Review Datadog PRs:**
    *   PR #135, #137–#139 (`fp-datadog-eu`): Owned by @Himal Hewagamage and @Isuru Dilhan.
    *   PR #140 (`gcp-fpg-optimus`): New request from **Himal Hewagamage**; tagged for review by @Nicholas Tan and @Maou Sheng Lee.
    *   PR #144 & #147 (`fp-datadog-eu`): Owned by @Isuru Dilhan and @Himal Hewagamage.
*   **Merge/Review Terraform PRs:**
    *   PR **#719** (`tfe-workspaces`) (Natalya Kosenko) & **PR #722** (Boning He): Review pending with @Isuru Dilhan and @Himal Hewagamage. PR #722 is for Boning's access to pricing Terraform workspaces.
*   **Troubleshoot Pipeline Issues:**
    *   Soni-BE Golden Pipeline clone failure: Investigate SSH key/environment (Kalana).
    *   `lt-strudel-api-go` Go version mismatch: Resolve `golangci-lint` config vs. target Go version conflict (Lester).
*   **Infrastructure Strategy:** Evaluate IaC implementation for Datadog log pipelines (Natalya; discussion ongoing with @Prabu Ramamurthy Selvaraj).
*   **Terraform Support:** Investigate failed run `run-CZVLtajJGbLVojLM` and ticket GCD-8900.
*   **Cloud NAT Provisioning:** Review Cloud NAT request for `us-central1`. **@Mohit Niranwal** requested testing in non-prod first before full rollout (regarding GCD-8941). @Himal Hewagamage and @Tan Nhu Duong are cc'd on ticket GCD-8941.
*   **Bastion Connectivity:** Investigate issue affecting Wai Ching Chan's team. Ticket **GCD-8954** raised; @Nicholas Tan, @Gopalakrishna Dhulipati, and @Akash Gupta notified.
*   **DBA Subnet Request:** Review CloudSQL subnet requirements for SOT-SONI project (Calvin Phan). @Himal Hewagamage is engaged via ticket DSD-11066.

**Decisions Made**
*   **IaC Requirement:** Clear requirement established for IaC adoption for Datadog pipelines to ensure auditability.
*   **Change Management Protocol:** Mohit Niranwal mandated testing new Cloud NAT configurations in non-production environments prior to production deployment (regarding GCD-8941).

**Key Dates & Follow-ups**
*   **2026-03-02 to 03-05:** Multiple PR requests from Madhawa.
*   **2026-03-11 to 03-12:** Critical pipeline failures reported by Kalana and Lester.
*   **2026-03-13:** Datadog strategy discussion initiated; Terraform plan failure reported.
*   **2026-03-16:** Service desk ticket GCD-8900 opened; PR #147, #148 (`fp-datadog-eu`), and #719 (`tfe-workspaces`) requested by Natalya Kosenko.
*   **2026-03-19:** Zheng Ming reported connectivity failure for AI agents; raised ticket GCD-8941 for Cloud NAT provisioning in `us-central1`. Mohit Niranwal intervened regarding non-prod testing.
*   **2026-03-20:** Wai Ching Chan reported bastion connectivity issues (GCD-8954). Calvin Phan requested CloudSQL subnets for SOT-SONI project (DSD-11066); @Himal Hewagamage replied.
*   **2026-03-24:** Himal Hewagamage requested review of PR #140 (`gcp-fpg-optimus`) tagged to @Nicholas Tan and @Maou Sheng Lee. Boning He requested review of PR #722 for workspace access, tagged to @Isuru Dilhan and @Himal Hewagamage.


## [26/52] DPD AI Guild
Source: gchat | Group: space/AAQA5_B3lZQ | Last Activity: 2026-03-24T06:57:45.762000+00:00 | Last Updated: 2026-03-24T07:46:54.634160+00:00
### Daily Work Briefing: DPD AI Guild

**1. Key Participants & Roles**
*   **Michael Bui:** Research/Technical Lead – Introduced the new model release.
*   **Zaw Myo Htet:** Technical Strategy/Engineering – Proposed optimization strategy and cost reduction.
*   **Nicholas Tan:** Strategic Monitor – Highlighted industry trends regarding AI executive automation (Meta).

**2. Main Topic**
The discussion centered on leveraging **Mistral Small 4** to optimize local knowledge handling via quantization (Unsloth) to reduce RAG dependency. This technical deep-dive was contextualized by recent market movements, specifically Meta's deployment of an "AI CEO" agent for executive operations, signaling a broader industry shift toward autonomous AI governance.

**3. Pending Actions & Ownership**
*   **Action:** Evaluate feasibility of replacing heavy RAG pipelines with quantized open-weight models to reduce costs.
    *   **Owner:** Zaw Myo Htet
    *   **Context:** Requires further technical assessment based on Unsloth documentation.
*   **Action:** Investigate integration of Mistral Small 4's specific architecture (MoE, 119B total/6B active parameters) into current workflows.
    *   **Owner:** TBD (Team-wide due to recent announcement).
*   **Action:** Analyze the implications of Meta's "AI CEO" model on our autonomous agent roadmap.
    *   **Owner:** Nicholas Tan / Team
    *   **Context:** Assess if similar high-level executive automation patterns are applicable to DPD workflows given the efficiency gains in large-scale operations.

**4. Decisions Made**
*   **Strategic Alignment:** The team acknowledged that while Mistral Small 4 offers specific architectural benefits for cost reduction, the broader industry (exemplified by Meta) is moving toward high-level autonomous agents. This suggests future DPD AI initiatives should balance model quantization with agent-based autonomy.
*   **No immediate formal decisions** were recorded regarding the technical implementation of Mistral Small 4; the conversation remains in the exploration phase pending Zaw Myo Htet's feasibility study.

**5. Key Dates & References**
*   **2026-03-17:** Michael Bui announced the release of **Mistral Small 4**.
    *   *Specs:* MoE Architecture, 119B total parameters (6B active), 256k context window, Vision capability.
    *   *Reference:* https://mistral.ai/news/mistral-small-4
*   **2026-03-19:** Zaw Myo Htet suggested utilizing **Unsloth** for quantization to make open-weight models more cost-effective and reduce RAG reliance.
    *   *Reference:* https://unsloth.ai/docs
*   **2026-03-24:** Nicholas Tan shared an article detailing Mark Zuckerberg's launch of an AI CEO bot to manage Meta operations.
    *   *Source:* The Independent (*Mark Zuckerberg builds AI CEO to help him run Meta*).
    *   *Relevance:* Highlights the maturity of agentic workflows for executive-level tasks, providing a benchmark for DPD's long-term automation goals.
*   **Thread Status:** Active (Last reply noted 22 minutes ago relative to briefing generation).


## [27/52] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/qx4BVM7nI60 | Last Activity: 2026-03-24T06:49:52.694000+00:00 | Last Updated: 2026-03-24T07:47:11.431016+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Lead/Coordinator (Prioritizing Staff App issues, creating war room).
*   **Zaw Myo Htet:** Backend/Data Specialist (Investigating SAP-DBP syncs, validating data logic).
*   **Daryl Ng:** Stakeholder (Checking data synchronization status).
*   **Jonathan Tanudjaja:** Frontend Developer (Diagnosing UI discount display issues, logging tickets).
*   **Andin Eswarlal Rajesh:** Frontend Lead (Reviewing root cause and ticket details).

**Main Topic**
Urgent resolution of high-priority "Staff App" issues to secure sign-off. The discussion focused on two specific areas: a ZOTO data synchronization issue between SAP and DBP, and a PWP UI bug where offers/discounts were not displaying correctly despite correct backend logic.

**Decisions & Findings**
*   **Data Sync (ZOTO):** Confirmed by Zaw Myo Htet that production data syncs between SAP and DBP are functioning correctly; no backend sync issue exists. The test case was successful.
*   **Root Cause (PWP/UI):** Jonathan Tanudjaja identified the bug as a legacy implementation flaw where the Frontend (FE) incorrectly determines discounts by taking only the "first item" in an array, rather than handling multiple items correctly. Andin Eswarlal Rajesh confirmed no recent pricing calculation changes were made; the issue is purely display logic.
*   **Resolution Strategy:** The team agreed to log a specific ticket for the FE fix rather than delaying for a war room meeting immediately.

**Pending Actions & Ownership**
1.  **Log Ticket (Completed):** Jonathan Tanudjaja logged ticket **DPD-811** regarding the discount display issue.
2.  **Share Root Cause Analysis:** Andin Eswarlal Rajesh requested a detailed explanation of the correct logic for picking discounts; Zaw Myo Htet confirmed the "after paid" implementation aligns with BO display and final invoices.
3.  **Provide Fix Estimate:** Jonathan Tanudjaja estimated **1-2 days** effort to resolve the issue.
4.  **Visibility Check:** All discussion threads were consolidated into the main chat room (per Prajney's instruction) to ensure visibility, moving away from separate private threads.

**Timeline & Deadlines**
*   **Date:** March 24, 2026.
*   **Immediate Goal:** Close all Staff App issues today.
*   **Planned Activity:** Creation of a "war room" in the second half of the day to finalize closures.
*   **Follow-up:** Zaw Myo Htet requested an estimation for the fix (completed by Jonathan). No specific hard deadline was set for the 1-2 day fix window, but the goal is immediate closure.


## [28/52] [Prod Support] Ecom FFS Ops
Source: gchat | Group: space/AAAAde_cYKA | Last Activity: 2026-03-24T06:48:45.930000+00:00 | Last Updated: 2026-03-24T07:47:41.890541+00:00
**Daily Work Briefing: [Prod Support] Ecom FFS Ops**

**Key Participants & Roles**
*   **Wai Ching Chan / Sampada Shukla:** Operations/Product Leads.
*   **TL HCBP FFS, TL - HGPT FFS, TLEPT FFS, Harry Akbar Ali Munir:** Store/Regional Team Leads reporting blockers.
*   **Adrian Yap Chye Soon:** Technical Lead/Support (investigating data anomalies and app downtime).
*   **Akash Gupta:** DPD / Fulfilment / On Call (Source of new alerts).

**Main Topics**
1.  **Packlist Discrepancies & Validation:** Ongoing investigation into critical `packed_qty` anomalies (NULL values or massive mismatches vs. `delivered_qty`).
    *   **New Critical Incident (Mar 23):** Order #22841624 at Hyper Sports Hub (Store ID 17) shows status `RECEIVED` but `packed_quantity` is NULL. Delivery date: Mar 23, 2026. Reported by Akash Gupta to Adrian Yap Chye Soon.
    *   **New Critical Incident (Mar 24):** Orders #22903190 and #22900975 at Hyper Sports Hub (Store ID 17) show `packed_qty` > 13 million vs. `delivered_qty` of 1. Reported by Akash Gupta to Adrian Yap Chye Soon.
    *   **New Critical Incident (Mar 23):** Order #22894000 at Hyper VivoCity (Store ID 170) shows `packed_qty` ~10.8M vs. `delivered_qty` of 2. Reported by Akash Gupta to Adrian Yap Chye Soon.
    *   **Historical Context:** Previous Mar 21 incident at Hyper Changi and Mar 19 anomaly at Hyper Parkway (Order #22862214) remain reference points alongside the new Mar 23–24 Sports Hub/VivoCity alerts.

**Pending Actions & Ownership**
*   **Critical Data Validation (Mar 23–24):**
    *   *@Yap Chye Soon Adrian:* Confirm NULL `packed_quantity` for Order #22841624 (Hyper Sports Hub) and investigate massive mismatches in Orders #22903190, #22900975 (Sports Hub) and #22894000 (VivoCity).
    *   **Root Cause Analysis:** Adrian Yap Chye Soon to determine the root cause of the short downtime affecting backoffice and picking apps reported on Mar 23.
*   **App Load Issues (Resolved):**
    *   Multiple stores (HSPH, HCBP, PGOASIS, Taiseng, TSENG) reported inability to load DBP/picking phones on Mar 23 morning; status confirmed "now ok" by respective TLs.
*   **Order Validation (Packlist Discrepancies):**
    *   *TL HSPH FFS:* Confirm packlists for Orders #22738044, #22754559, #22780412 and assist with Order #22894000 (unable to change date/time).
    *   *TL HPWP FFS:* Investigate discrepancy in Order #22781194.
    *   *Adrian Yap Chye Soon:* Review packlist NULL issue for Order #22789688 (Orchid Country Club).
*   **System Fixes:**
    *   *TL HCBP FFS:* Request IT assistance to check pending status for T10 orders (bulk/general/fresh) and resolve stuck "pending" status issues.

**Decisions Made**
*   **App Release Strategy:** Picker App 10.4.0 rollout remains on hold pending resolution of critical data anomalies (Mar 18–24). Full rollout contingent on stability post-fixes, specifically addressing the new Mar 23 NULL quantity alerts and the resolved but investigated app load downtime.

**Key Dates & Deadlines**
*   **Immediate:** Validation of Mar 23–24 incidents at Hyper Sports Hub and VivoCity; investigation into Mar 19 anomaly at Hyper Parkway.
*   **Pending:** Root cause analysis for Mar 23 app loading issues and pending status checks for HCBP T10 orders.

**Critical Alerts**
*   **New Alert (Mar 24, 6:02 AM):** Two orders at Hyper Sports Hub show `packed_qty` > 13M vs. 1 delivered.
*   **New Alert (Mar 23, 12:57 PM):** Order #22841624 at Hyper Sports Hub shows NULL `packed_quantity`.
*   **New Alert (Mar 23, 4:01 AM):** Order #22894000 at Hyper VivoCity shows massive data mismatch.
*   **Resolved Alert:** Widespread picking phone/DBP load failure across HSPH, HCBP, PGOASIS, Taiseng, and TSENG resolved by 7:57 AM on Mar 23.


## [29/52] Yangyu Wang
Source: gchat | Group: dm/4Ut7xcAAAAE | Last Activity: 2026-03-24T06:40:09.931000+00:00 | Last Updated: 2026-03-24T07:47:59.161849+00:00
**Daily Work Briefing: Layout Service Deployment (PR #362)**

**Key Participants & Roles**
*   **Yangyu Wang:** Initiator/Deployer (Requesting approval, executing deployment).
*   **Michael Bui:** Approver/Monitor (Validating safety, offering oversight).

**Main Topic**
Discussion regarding the safety and scheduling of a production deployment for the `layout-service` (Pull Request #362). The conversation clarified a misunderstanding where Michael initially confused this update with a previous `website-service` deployment.

**Decisions Made**
*   **Safety Approval:** Michael Bui confirmed the changes are safe to deploy at 2:00 PM local time once Yangyu confirms the correct service context.
*   **Clarification:** The target PR is for `layout-service`, distinct from a prior `website-service` deployment discussed in error.

**Actions & Ownership**
*   **Completed Action:** Deployment execution.
    *   **Owner:** Yangyu Wang
    *   **Status:** Confirmed deployed at 06:36:12 UTC on 2026-03-24.
*   **Pending Action:** Monitoring post-deployment stability.
    *   **Owner:** Michael Bui
    *   **Trigger:** Completed upon Yangyu's "Deployed" notification.

**Key Dates, Deadlines & Timeline**
*   **2026-03-18 | 06:59 UTC:** Previous deployment of a different service (historical context).
*   **2026-03-24 | 02:19 AM:** Yangyu asks for approval to deploy at 2:00 PM local time.
*   **2026-03-24 | 03:02 AM:** Michael expresses confusion regarding a potential prior deployment of the same changes.
*   **2026-03-24 | 03:15 AM:** Yangyu clarifies the PR is for `layout-service`, not `website-service`. Michael confirms approval ("For me it's ok") and requests pre-deployment notification to monitor the system.
*   **2026-03-24 | 06:36 UTC:** Yangyu executes the deployment.
*   **2026-03-24 | 06:40 UTC:** Michael acknowledges receipt and thanks Yangyu.

**Summary of Event Flow**
On March 24, 2026, Yangyu Wang initiated a request to deploy `layout-service` Pull Request #362 at 2:00 PM local time. Michael Bui initially queried if the changes were already deployed from the previous week. Yangyu clarified that the prior discussion referred to `website-service`, confirming this new PR was for `layout-service`. Michael approved the move, requested a ping before execution to monitor the system, and confirmed safety. Yangyu notified "Deployed" at 06:36:12 UTC on March 24, which Michael acknowledged one minute later at 06:40:09 UTC. The deployment was successfully completed with no further pending actions.


## [30/52] Gopalakrishna Dhulipati
Source: gchat | Group: dm/5Y7kGgAAAAE | Last Activity: 2026-03-24T06:32:01.720000+00:00 | Last Updated: 2026-03-24T07:48:11.827161+00:00
**Daily Work Briefing: China Visa Application Coordination**

**Key Participants & Roles**
*   **Michael Bui:** Initiator of the query; currently on leave next week.
*   **Gopalakrishna Dhulipati (Resource):** Primary contact for visa logistics in China; responsible for gathering documentation.

**Main Topic**
Discussion regarding the status and timeline of applying for a Visa to China, specifically focusing on the necessity of an invitation letter and the feasibility of third-party collection upon approval given Michael's upcoming leave.

**Pending Actions & Owners**
*   **Obtain Business Invitation Letter:** Owner: **Gopalakrishna Dhulipati**. (Status: Currently in progress; not yet applied).
*   **Submit Visa Application In-Person:** Owner: **Michael Bui**. (Decision made that submission must remain personal; collection can be delegated).
*   **Monitor Visa Production Status:** Owner: **Michael Bui**. (Tracking potential completion by Friday, March 27, 2026).

**Decisions Made**
*   Collection of the approved passport at the China Visa Application Service Center (CVASC) is confirmed as allowed for a third party.
*   Submission of the application itself must be performed in-person by Michael Bui and cannot be delegated to Gopalakrishna Dhulipati.

**Key Dates & Deadlines**
*   **2026-03-24:** Conversation took place (timestamps: 05:52 – 06:32 UTC).
*   **Next Week:** Michael Bui is on leave.
*   **Friday, 2026-03-27:** Target date for Michael to determine if the visa will be ready for collection. (Note: Status deemed "unlikely" by end of discussion).

**Summary**
Michael inquired about his China Visa application status. Gopal confirmed he has not yet applied and is currently securing a business invitation letter. Due to Michael's leave schedule next week, they discussed whether Gopal could collect the visa on his behalf. It was clarified that while submission requires Michael's physical presence, collection at CVASC can be handled by an authorized third party. Michael plans to check if the visa will be ready by Friday; however, he anticipates it may not be completed in time for immediate collection before or during his leave week. Gopal acknowledged this timeline update.


## [31/52] Alvin Choo
Source: gchat | Group: dm/zmMZpgAAAAE | Last Activity: 2026-03-24T06:05:09.086000+00:00 | Last Updated: 2026-03-24T08:12:15.187601+00:00
**Daily Work Briefing: RMN & Postmortem Updates (Updated)**
**Resource:** Alvin Choo (Lead/Manager) | **Participant:** Michael Bui (Domain Expert, Backend Dev)
**Date Range:** March 3 – March 24, 2026

### **Key Participants & Roles**
*   **Alvin Choo:** Leads coordination for RMN postmortem reports, travel logistics, and securing business invitation letters from CoMall.
*   **Michael Bui:** Domain expert responsible for backend implementation; currently on leave until April 2, with a public holiday on April 3.

### **Main Topics**
1.  **Wuhan Travel & Visa Processing:** Departure confirmed for **April 6, 2026**. Michael requires a multi-entry visa (valid 6mth or 1yr) applied for at least one month in advance. Alvin is securing an invitation letter from CoMall to expedite the application.
2.  **RMN Postmortem & Incident Review:** Finalizing report for BCRS completion; addressing "Overage on transaction sync" and transition to impressions-based model.
3.  **Technical Implementation:** Backend work for RMN tickets; integration with Advertima (Grassfish CMS) and Vijaykumar (PDA owner). GLMS re-testing initiated after Pentest fixes (DPD-591).

### **Decisions Made**
*   **Visa Strategy:** Visa Type M (Business & Trade) confirmed. Michael is on leave next week; Alvin advised checking with Gopal and Ravi regarding their self-processing methods while waiting for the invitation letter.
*   **Document Requirements:** Michael provided personal details (Vietnam Passport P00241735, DOB: 1986-09-22) to facilitate the visa application form.
*   **Workshop Deliverables:** Michael will prepare "as-is" and "to-be" design plans rather than full slides; Alvin confirmed existing documents need alignment only.
*   **Ticket Prioritization:** OMNI-1282 (SAP invoice) deprioritized; OMNI-1191 and OMNI-1247 remain active but OSMOS-focused.

### **Pending Actions & Ownership**
| Action Item | Owner | Details/Context |
| :--- | :--- | :--- |
| **Visa Application** | Michael Bui | Apply for multi-entry Type M visa immediately upon receiving invitation letter; submit online verification today if possible. |
| **Invitation Letter** | Alvin Choo | Secure business letter from CoMall to speed up Michael's visa process. |
| **Workshop Prep (Design)** | Michael Bui | Create docs detailing "as-is" vs. "to-be" integration flows; note: On leave until April 2, PH on April 3. |
| **Postmortem Review** | Alvin Choo | Final review after PDA impact verification (Vijay) and Advertima POV status inclusion. |
| **GLMS Re-testing** | Michael Bui | RMN APIs fixed for Pentest issues; GLMS instructed to re-test upon return from leave. |

### **Key Dates & Milestones**
*   **March 24:** Departure set for April 6. Alvin requested invitation letter today; Michael advised on visa processing timeline (1 month lead time).
*   **April 2:** End of Michael's current leave period.
*   **April 3:** Public Holiday in Singapore.
*   **April 6:** Confirmed departure date for Wuhan, China.
*   **End of March:** PM25 rating meeting (Alvin) to be scheduled; Winson invited.
*   **End of Q1 2026:** Advertima POV pilot period concludes.


## [32/52] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Last Activity: 2026-03-24T05:35:17.186000+00:00 | Last Updated: 2026-03-24T08:12:46.997646+00:00
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

**Main Topics Discussed**
1.  **Website SDK Deployment (Strudel):** Lester Santiago Soriano deployed `go-platform-website` on Mar 19 at 4:00 PM to update the Strudel SDK for maximum voucher amount validation. Changes were reviewed via Bitbucket diff between v1.5.11 and v1.5.10.
2.  **Pre-order Payment Logic & UAT Page:** Zaw Myo Htet raised a critical inquiry regarding pre-order flows (specifically app payment vs. POS redemption) on Mar 24. He subsequently requested peer review for the offline pre-order admin page (`https://admin-uat.fairprice.com.sg/in-store-preorder/offline`) at 05:38 AM, noting 8 replies and 8 unread messages in the thread.
3.  **Slot Date Discrepancy:** Shiva Kumar Yalagunda Bas reported a delivery slot mismatch where the UI shows the 25th while the API indicates the 23rd. Daryl Ng and Sundy Yaputra remain involved in resolving this.
4.  **UAT Stock Requirements:** Sneha Parab requested high-stock SKUs for bulk order testing by Zi Ying. Wai Ching Chan and Akash Gupta were tasked to check IMS availability.
5.  **Order Verification Bug (NED-278216):** Investigation continues into the Whitelisting API returning older contract data (identified by Andin).
6.  **BCRS Deposit & SAP Integration:** Critical duplicate deposit posting fix remains active (PR #6).

**Pending Actions & Ownership**
*   **Zaw Myo Htet:** Clarify pre-order payment redemption logic; execute UAT testing on offboarded Pinelabs split feature flag; provide peer review for the offline pre-order admin page.
*   **Lester Santiago Soriano:** Assist with Whitelisting API contract issue (cc: Piraba Nagkeeran, Jonathan Tanudjaja). Deployment completed Mar 19.
*   **Wai Ching Chan & Akash Gupta:** Source high-stock SKUs from IMS for Zi Ying's bulk order testing and investigate UAT SKU `13023506` threshold settings.
*   **Daryl Ng & Sundy Yaputra:** Resolve delivery slot date mismatch (UI showing 25th vs API 23rd).
*   **Andin Eswarlal Rajesh:** Investigate iOS slot mapping error and assist with Amplitude event tracking flow inquiry.

**Decisions Made**
*   **Deployment Approval:** PLU processor deployment approved pending UD alignment (per prior briefing).
*   **Code Review Priority:** Focus shifted to `go-platform-website` PR #1538 for the Strudel SDK update, superseding previous layout-service priorities. Current focus includes reviewing the new offline pre-order admin page.

**Key Dates & Deadlines**
*   **Mar 19, 2026:** Website deployment completed at 4:00 PM; UAT stock sourcing required immediately.
*   **Mar 24, 2026 (Today):** Zaw Myo Htet initiated inquiry regarding the offline pre-order admin page and pre-order payment logic.
*   **Thursday:** D&T All Hands meeting.
*   **Mar 31, 2026:** Sports Hub FFS store closure deadline.
*   **Ongoing:** Slot logic validation, Amplitude tracking investigation, and NED-278216 resolution.

**Note on Historical Context:** Previous mentions of code review priorities for `layout-service` PR #362 and `website-service` PR #649 are superseded by the urgent Strudel SDK deployment update. The focus has now shifted to resolving slot date mismatches, pre-order payment logic queries, and the newly flagged offline pre-order admin page review.


## [33/52] Sazali Bin Mohammed Ali
Source: gchat | Group: dm/y2r5GMAAAAE | Last Activity: 2026-03-24T05:29:40.582000+00:00 | Last Updated: 2026-03-24T08:13:19.645516+00:00
**Daily Work Briefing: Sazali Bin Mohammed Ali / Michael Bui**

**Key Participants & Roles**
*   **Sazali Bin Mohammed Ali:** Provides technical guidance from the Security Risk Assessment (SRA) perspective.
*   **Michael Bui:** Project lead; managing stakeholder communication and operational logistics regarding expiration dates.

**Main Topic**
Discussion regarding a new request for an SRA assessment for "Advertima" (specifically referenced in email thread: `rfc822msgid:<airmail-04ca1d17-c830-466b-9d97-391b2f05d2eb@google.com>`). The conversation focuses on the scope of expanding the Proof of Concept (POC) and managing setup expiration dates.

**Decisions Made**
*   **Scope Expansion:** Sazali confirmed that from the SRA perspective, Michael may proceed with expanding the POC.
*   **Assessment Basis:** It was noted that the initial assessment was conducted strictly from a technological standpoint.

**Pending Actions & Ownership**
1.  **Email Reply:** Michael Bui is tasked with replying to the email thread regarding this request.
    *   *Owner:* Michael Bui
2.  **Expiry Extension Verification:** Michael Bui will coordinate with relevant teams to ensure expiration dates are extended for specific setups (e.g., connectivity, account credentials).
    *   *Owner:* Michael Bui
3.  **Technical Team Consultation:** Any setup-specific expirations must be verified directly with the necessary technical teams before finalizing extensions.
    *   *Owner:* Michael Bui (with input from necessary teams)

**Key Dates & Follow-ups**
*   **2026-03-24 05:17:58 UTC:** Sazali provided initial guidance on the POC expansion and technical constraints.
*   **2026-03-24 05:29:40 UTC:** Michael Bui acknowledged the instructions and defined the immediate next steps (email reply and expiry check).
*   **Reference Links:**
    *   Google Chat: `https://chat.google.com/dm/y2r5GMAAAAE`
    *   Email Thread: `https://mail.google.com/mail/#search/rfc822msgid%3A%3Cairmail-04ca1d17-c830-466b-9d97-391b2f05d2eb%40google.com%3E?oor=true`


## [34/52] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/keeadQjwypw | Last Activity: 2026-03-24T05:17:31.016000+00:00 | Last Updated: 2026-03-24T08:13:37.685453+00:00
### Daily Work Briefing: BCRS Firefighting Group

**Key Participants & Roles**
*   **Sathya Murthy Karthik:** Issue reporter; provided initial bug details and order reference.
*   **Daryl Ng:** Initial triage lead; clarified context (Tax Receipt vs. Payment page) and escalated to engineering.
*   **Andin Eswarlal Rajesh:** Engineering lead; coordinated investigation, requested testing validation, and assigned ticketing workflow.
*   **Piraba Nagkeeran:** Engineer/Developer; reproduced the bug, implemented a fix, conducted regression testing, and will raise documentation.

**Main Topic**
Investigation and resolution of a "scan & go" glitch related to tax receipts occurring after order verification. The issue was distinct from previous B2B payment page issues.

**Key Timeline & Events**
*   **2026-03-24 03:43:** Sathya reported the scan & go glitch.
*   **2026-03-24 03:50–04:11:** Team clarified the issue scope (Tax Receipt) and requested specific order details from Sathya.
*   **2026-03-24 04:00:** Sathya provided UAT delivery order link (`delivery-orders/75577957`).
*   **2026-03-24 04:11–04:22:** Piraba investigated the pre-verification and post-verification states, confirming reproducibility after verification.
*   **2026-03-24 04:50:** Piraba confirmed the fix and announced an upcoming PR/new build.

**Decisions Made**
1.  **Fix Confirmation:** The glitch is resolved in the current development branch (PR pending).
2.  **Testing Scope:** Regression testing must cover both "verified" and "unverified" user statuses to ensure no other flows are broken.
3.  **Documentation Protocol:** A formal bug ticket must be created containing proof of the fix; Andin will assign this to the correct epic.

**Pending Actions & Ownership**
*   **Raise PR & Share Build:** Owned by **Piraba Nagkeeran**. Status: In progress immediately following the fix confirmation (04:50).
*   **Regression Testing:** Owned by **Piraba Nagkeeran**. Scope includes testing verified and unverified flows to prevent regression.
*   **Create Bug Ticket:** Owned by **Andin Eswarlal Rajesh** (or Piraba upon request, as per instruction "Create a bug ticket"). The ticket must include proof of the fix.
*   **Ticket Assignment:** Owned by **Andin Eswarlal Rajesh**. He will move the ticket to the appropriate epic once created.

**Critical References**
*   **Order URL:** `https://admin-uat.fairprice.com.sg/customer-support/delivery-orders/75577957`
*   **Issue Type:** Scan & Go glitch (Tax Receipt).
*   **System Context:** UAT environment (`admin-uat.fairprice.com.sg`).


## [35/52] OMS x CS
Source: gchat | Group: space/AAAAUPoVWjI | Last Activity: 2026-03-24T03:58:40.279000+00:00 | Last Updated: 2026-03-24T08:14:20.570159+00:00
**Daily Work Briefing: OMS x CS Resources (Updated)**

**Key Participants & Roles**
*   **Sampada Shukla:** Customer Support (CS) agent.
*   **Wai Ching Chan:** CS representative flagging operational process gaps regarding customer profile merging.
*   **Raine Lee:** CS representative reporting notification delivery failures, including a new NPS feedback loop.
*   **Gomathi Panneerselvam & Gopalakrishna Dhulipati:** IT/Operations personnel involved in resolving reported issues.

**Main Topics**
1.  **Access Control:** Critical lockout of CS agent Sampada Shukla from Zendesk due to MFA/SMS 2FA failures (March 4). Resolution pending.
2.  **Process Integrity:** Recurring disruption caused by merging customer profiles without validating pending orders, leading to stalled workflows (Orders #255985725 and others).
3.  **System Reliability:** 
    *   Historical failure of SMS/PNS delivery for Order #256547454 (March 12).
    *   **New Incident:** Customer reported missing order confirmation emails for Orders #257969203, #257279251, and #256369211. Despite OPS inbox visibility, the customer confirmed emails were not received in spam/junk folders. This issue is linked to Ticket #4449487 and an associated NPS survey submission.

**Pending Actions & Ownership**
*   **Reset MFA:** IT support must reset Sampada Shukla's Multi-Factor Authentication immediately to restore Zendesk access. (*Owner: IT Team*)
*   **Process Validation Protocol:** CS and Customer Data Management (CDM) teams need to implement a mandatory validation check for open/pending orders before executing customer profile merges. (*Owner: CS & CDM Teams*)
*   **Investigate Email Delivery Failure:** Verify backend logs for Ticket #4449487 to confirm successful dispatch of order confirmation emails for the three affected orders (#257969203, #257279251, #256369211). Compare against historical delivery metrics. (*Owner: Technical/Operations Team*)
*   **Investigate Notification Failure (Legacy):** Proceed with technical review for SMS/PNS triggers failing on Order #256547454 (Customer: btsoh268@gmail.com) as previously planned. (*Owner: Technical/Operations Team*)

**Decisions Made**
*   No formal decisions recorded in the chat log; however, **Wai Ching Chan** explicitly identified a systemic risk requiring a protocol change between CS and CDM to prevent future order processing blocks during profile merges.
*   **New Context:** The NPS survey submission for Ticket #4449487 elevates the email delivery issue from a routine check to a customer satisfaction concern requiring priority verification.

**Key Dates & References**
*   **March 4, 2026:** Sampada Shukla reported Zendesk lockout (SMS 2FA issue). Last reply recorded March 4 at 4:41 AM.
*   **March 7, 2026:** Customer profile UID `4815537039166279` merged into UID `216353592157999833`, stalling Order #255985725.
*   **March 9, 2026:** Wai Ching Chan escalated the merge issue at 6:13 AM. Last reply recorded Thursday at 11:11 AM.
    *   *Affected Order Link:* `https://admin.fairprice.com.sg/customer-support/sale-orders/255985725`
    *   *Customer Profile Link:* `https://admin.fairprice.com.sg/customer-support/customers/view/1067653`
*   **March 12, 2026:** Raine Lee reported SMS/PNS delivery failure for Order #256547454. Last reply recorded at 12:00 AM.
*   **March 24, 2026 (03:58 AM):** Raine Lee raised Ticket #4449487 regarding missing order confirmation emails for three recent orders (#257969203, #257279251, #256369211). Customer submitted NPS survey. Last reply recorded 5:13 AM.


## [36/52] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/U9X5v7rY7Kw | Last Activity: 2026-03-24T03:46:32.408000+00:00 | Last Updated: 2026-03-24T08:15:02.128056+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants**
*   **Prajney Sribhashyam:** Initiator of the query; represents Store Operations perspective.
*   **Daryl Ng:** Technical lead providing feasibility analysis and system limitations.
*   **Michael Bui:** Contributor clarifying fraud classification regarding barcode consistency.

**Main Topic**
Discussion on preventing revenue leakage in the "Scan & Go" feature caused by customers scanning old SKUs (lower price) while taking new SKUs (higher price), specifically within the BCRS context where cashiers are blocked from using multiplication functions. The group also evaluated technical guardrails to prevent quantity inflation via the (+) button or duplicate QR scanning without physical item verification.

**Discussion Highlights & Decisions**
*   **Technical Feasibility:** Daryl Ng confirmed that preventing a customer from scanning an old barcode while taking a new one is **not technically possible** at the system level, as barcodes are not unique identifiers for specific physical instances. This scenario is classified by the team as **pilferage**.
*   **Fraud Context:** Michael Bui noted that this behavior falls under general fraud; customers could scan any item and take a different one regardless of the BCRS context.
*   **Quantity Inflation Guardrails:** Prajney requested blocking the ability to add quantity via the (+) button without multiple scans. Daryl Ng verified that today, users **can** tap the (+) button to increment quantity for BCRS SKUs.
*   **Configuration Limits:** Regarding a proposal to require mandatory verification (e.g., "X times") for specific items:
    *   The request to configure "X" (specifically setting X=1 for all BCRS items) is **not currently possible**.
    *   Existing configuration logic for mandatory verification exists only for **alcohol** categories.
*   **Operational Strategy:** Since technical prevention of SKU swapping is impossible, the team aligned that the solution must rely on **aligned Standard Operating Procedures (SOPs)** in-store rather than software blocking.

**Pending Actions & Ownership**
*   **Action:** Implement SOP alignment to mitigate pilferage risk since system-level blocking is unavailable.
    *   **Owner:** Store Operations Team (implied via Prajney's initial request).
*   **Action:** Investigate potential configuration updates for quantity verification limits.
    *   **Status:** No immediate action; confirmed not configurable currently outside of alcohol categories.

**Key Dates & References**
*   **Date:** March 24, 2026 (03:33 – 03:46 UTC).
*   **Resource:** BCRS Firefighting Group.
*   **URL:** https://chat.google.com/space/AAQAgT-LpYY


## [37/52] RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU | Last Activity: 2026-03-24T03:26:50.240000+00:00 | Last Updated: 2026-03-24T08:15:23.003544+00:00
**Daily Briefing Summary: RMN Leadership Space (Updated Mar 24)**

**Key Participants & Roles**
*   **Bryan Choong:** Leadership; active oversight on SignCloud cleanup timeline.
*   **Allen Umali:** Addressed SRA/Advertima inquiries; leading SignCloud screen cleanup and loop verification.
*   **Rajiv Kumar Singh:** Coordinating SOAC planning and Advertima operations.
*   **Michael Bui:** Inquired about Advertima future clarity.
*   *Note: Jaren Loy Xing Wei (Departing), Pauline Tan, Christopher Yong remain as per previous context.*

**Main Topics**
1.  **Advertima Partnership Status:** Michael Bui questioned the future of Advertima operations, noting the current SRA covers only the Proof-of-Value (PoV) period. An extended PoV or long-term partnership requires a new Service Request Agreement (SRA). Rajiv Kumar Singh confirmed devices will operate under an extended PoV through end of April pending SRA formalization.
2.  **Advertima Technical Issues:** Reports identified consecutive playback errors in specific stores: an Energy Market Authority (EMA) ad ran three times consecutively, and a "Trust sign up" ad appeared erroneously. Allen Umali clarified that the affected screen is legacy hardware still on SignCloud undergoing manual cleanup; all other screens in the store follow the current play loop correctly.
3.  **SignCloud Cleanup:** Bryan Choong requested a timeline for removing old SignCloud screens. Allen Umali confirmed the full list is available and cleanup will be completed within this week (by Mar 28).

**Pending Actions & Owners**
*   **Advertima SRA Renewal:** Secure a new SRA for long-term Advertima partnership or extended PoV beyond April. *Owners: Allen Umali, Alvin Choo.*
*   **SignCloud Cleanup:** Complete manual removal of legacy screens and resolve loop errors (EMA/Trust ads). *Owner: Allen Umali | Deadline: End of this week (Mar 28).*
*   **Ad Suppression with Osmos:** Provide firm ETA to resolve weeks-old issue. *Owner: Team.*
*   **SOAC Planning:** Finalize targets per CM, supplier, and category by end of March. *Owner: Rajiv Kumar Singh & Ryan.*
*   **Brand/Non-Endemic Sales:** Continue rOOH sales efforts (endemic via JBP; non-endemic via WOG/govt campaigns) and prepare for HPB meeting. *Owner: Team.*
*   **LinkedIn Content Cadence:** Maintain 1–2 posts weekly starting Mar 9. Gather ideas/case studies from the team. *Owner: Pauline Tan & Team.*

**Decisions Made**
*   **Advertima Continuity:** Confirmed extended PoV for Advertima devices through end of April pending SRA formalization.
*   **LinkedIn Launch:** "FPG ADvantage" page is live; frequency set at 1–2 times weekly.
*   **SignCloud Resolution:** Old screens are being manually purged; full list identified and cleanup targeted for completion this week.
*   **Strategic Focus:** Priorities during Bryan's absence locked to SOAC targets, rOOH sales, and HPB prep.

**Key Dates & Deadlines**
*   **Mar 2:** Criteo/ChatGPT partnership analyzed; Jaren's departure announced.
*   **Mar 5:** FPG ADvantage LinkedIn page went live.
*   **Mar 9 – Mar 23:** Bryan Choong away from office (Note: Re-engaged Mar 24 regarding SignCloud).
*   **Mar 19:** Advertima extended PoV confirmed for end of April; SRA update identified as necessary.
*   **Mar 28 (Est.):** Completion of SignCloud manual cleanup.
*   **End of March:** Deadline to finalize SOAC targets per CM/supplier/category.
*   **April End:** Current deadline for Advertima extended PoV operations.
*   **Upcoming:** HPB meeting preparation required.


## [38/52] RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Last Activity: 2026-03-24T03:21:05.781000+00:00 | Last Updated: 2026-03-24T08:15:45.340990+00:00
**Daily Work Briefing: Automated Test Results Summary (RMN Notification)**

**Key Participants & Roles**
*   **Collection Runner App:** Automated testing agent executing API suites.
*   **Webhook Bot:** Reporting mechanism; consistently returning "unable to process your request" on all notifications.
*   **Parties Involved:** No human participants engaged; system-generated notification log.

**Main Topic/Discussion**
The conversation comprises automated notifications from the Collection Runner regarding nightly API test executions across `promo-service`, `marketing-personalization-service`, and `marketing-service` in the **staging** environment. Logs track "API Tests" and "API Contract Tests." The monitoring period has extended from March 12 through **March 24, 2026**, with execution windows at approximately 01:05 UTC, 02:30/02:31 UTC, and 03:20/03:21 UTC.

**Test Execution Status & Anomalies**
*   **Stable Services:**
    *   `promo-service`: Confirmed stable on March 23 (02:30 UTC) with 10 Passed / 0 Failed API tests and 6 Passed / 0 Failed Contract tests (3 Total Requests). Also stable on March 24 (02:31 UTC).
    *   `marketing-personalization-service`: New data from **March 23, 2026, at 03:21 UTC** confirms stability with zero failures (96 Passed API / 126 Passed Contract). Stability continues through **March 24, 2026, at 03:21 UTC**.
*   **Persistent Failures (`marketing-service`):**
    *   The pattern of **2 recurring API test failures per run** persists on **March 23 and March 24, 2026**, extending the instability observed since March 17.
        *   **Mar 23 (01:05 UTC):** 50 Passed / **2 Failed** (API Tests). Contract tests remained stable (20 Passed / 0 Failed).
        *   **Mar 24 (01:05 UTC):** 50 Passed / **2 Failed** (API Tests). Contract tests remained stable (20 Passed / 0 Failed).
    *   Total requests for API tests remain consistent at 17 per run.

**Pending Actions & Ownership**
*   **Investigate Persistent `marketing-service` Failures:** The root cause for the consistent 2 API test failures observed daily from March 17 through **March 24, 2026**, remains unaddressed. Engineering teams must review failure reports immediately given the four-day streak of recurrence in the current monitoring window.
*   **Webhook Bot Remediation:** The bot failed to process requests in every notification cycle from March 12 through at least **March 24, 01:05 UTC** (including the latest log). Immediate attention is required from DevOps or Automation Infrastructure.

**Decisions Made**
*   No human decisions recorded; all entries are automated system outputs.

**Key Dates & Deadlines**
*   **Failure Window (Historical):** Instability noted on March 12 and 13.
*   **Current Failure Window:** The service has been failing consistently since **March 17, 2026**, continuing through **March 24, 2026**.
*   **Monitoring Period:** Data covers runs from **March 12, 2026**, through **March 24, 2026** (spanning execution windows at 01:05 UTC, 02:30/02:31 UTC, and 03:20/03:21 UTC).
*   **Next Steps:** Immediate investigation into the `marketing-service` API flakiness and Webhook Bot connectivity issues.


## [39/52] BCRS Working Group - OMNI
Source: gchat | Group: space/AAQAkrn0niY | Last Activity: 2026-03-24T03:17:09.481000+00:00 | Last Updated: 2026-03-24T08:16:11.244496+00:00
**Daily Work Briefing: BCRS Working Group – OMNI**
**Source:** Google Chat (BCRS Working Group) & Jira
**Date Range:** March 5, 2026 – March 24, 2026

### Key Participants & Roles
*   **Teri Ong Qiu Mei:** Raised a critical security concern regarding "Scan & Go" inventory integrity.
*   **Prajney Sribhashyam:** Assigned to address the Scan & Go SKU substitution query; previously noted for follow-up on FOC processes.
*   **Daryl Ng, Seokhwee Poh, Sathya Murthy Karthik:** Continue roles regarding UAT testing and POS logic resolution from prior dates.
*   **Sip Khoon Tan, Piraba Nagkeeran:** Continuing work on iOS asset updates.

### Main Topics
**1. Scan & Go Inventory Integrity (New)**
Teri Ong Qiu Mei raised a specific concern regarding the "Scan & Go" feature: preventing customers from scanning barcode labels of old SKUs while physically removing new SKUs from shelves to avoid paying the associated 10-cent charge. This highlights a potential vulnerability in item verification logic between digital and physical inventory during self-service checkout.

**2. POS & Pre-order FOC Logic**
*Continued from March 5–17:* Investigation into POS failures regarding Free of Charge (FOC) SKUs with $0 RSP. Confirmed that standard POS interfaces cannot process $0 items directly; workflows require either excluding items from scanning or applying 100% discounts on SAP-defined promo sets.

**3. iOS Asset Update**
*Continued:* Piraba Nagkeeran identified an outdated "snowman" default icon in the iOS repository (Jira ticket **DPD-657**). Sip Khoon Tan has been engaged to provide the correct asset.

### Decisions Made & Process Updates
*   **POS Limitation Confirmed:** POS systems cannot accept $0 RSP for FOC SKUs via standard interface. In-store pre-orders must exclude scanning or use discount logic on promo sets.
*   **Scan & Go Query Open:** The specific mechanism to prevent SKU substitution (scanning old, taking new) in the Scan & Go flow has been flagged as a priority concern by Teri Ong Qiu Mei but requires immediate technical review.

### Pending Actions & Owners
*   **Action:** Investigate and resolve the "Scan & Go" SKU substitution vulnerability (Old vs. New SKUs).
    *   **Owner:** Prajney Sribhashyam (assigned to address Teri's query).
    *   **Context:** Prevent loss of 10-cent charges due to barcode mismatch.
*   **Action:** Follow up on the specific Pre-order FOC process and resolve the UAT discrepancy.
    *   **Owner:** Sathya Murthy Karthik.
    *   **Support:** Prajney Sribhashyam (co-owner).
*   **Action:** Provide the default icon asset to resolve the iOS repository discrepancy.
    *   **Owner:** Sip Khoon Tan.

### Key Dates & Deadlines
*   **March 5–17, 2026:** Initial threads on "Offline preorder receipt," UAT findings, and FOC logic clarification.
*   **March 13, 2026 (02:33 AM):** Daryl Ng reported UAT issues regarding missing BCRS deposits for FOC SKUs.
    *   *References:* PDA Receipt (`1G4t5GYI6iTsabjuNHHqEDqbMlDB6ImZr`), POS Receipt (`1hqtxOUysbUNtTT7CW48RPXZ6dEfN-2Dc`).
*   **March 13, 2026 (05:17 AM):** Sathya acknowledged findings and initiated action.
*   **March 17, 2026 (09:45 AM):** Piraba flagged outdated iOS icon via Jira ticket **DPD-657**. Last reply recorded at 04:58 AM on March 17.
*   **March 24, 2026 (03:17 AM):** Teri Ong Qiu Mei raised the "Scan & Go" SKU substitution query regarding the 10-cent charge discrepancy. Thread currently has 4 replies with Prajney Sribhashyam tagged for response.

### Summary of Findings
While previous discussions confirmed POS limitations on $0 RSP items and established SOPs for in-store pre-orders, a new critical risk has emerged regarding "Scan & Go" operations. Teri Ong Qiu Mei identified that current controls may allow customers to scan old SKUs while taking new ones to evade the 10-cent fee. Prajney Sribhashyam is now tasked with investigating this specific substitution logic. Concurrently, the iOS asset update (Jira **DPD-657**) and FOC UAT resolution remain active but secondary to the immediate Scan & Go security concern.


## [40/52] DPD x DPM
Source: gchat | Group: space/AAQApzD7Im0 | Last Activity: 2026-03-24T03:11:18.407000+00:00 | Last Updated: 2026-03-24T08:16:38.630342+00:00
### Daily Work Briefing: DPD x DPM Collaboration Space

**Key Participants & Roles**
*   **Daryl Ng:** Tech Lead; flagged CHAS calculation issues. Tagged regarding Gamification ownership and new delivery logic inquiry.
*   **Vivian Lim Yu Qian:** Initiator of topics; driving mandates (MTI price per piece) and feature rollouts. Investigating SWA migration history.
*   **Rajesh Dobariya:** Inquired about Gamification data requirements for CRM PNS automation. Recently asked to clarify display logic for "Normal" vs. "Express" delivery text changes.
*   **Sneha Parab:** Tagged regarding Tech Lead ownership transition and SWA/Wordpress vs. Publitas inquiry.

**Main Topics**
1.  **Delivery Text Logic (New):** Rajesh Dobariya requests clarification on the current display logic for "Normal Delivery" to facilitate a text change required for "Express Delivery." Awaiting Daryl Ng's response regarding implementation details.
2.  **Gamification Data Requirements:** CRM team requires specific data points in BigQuery (BQ) for PNS automation targeting. Needs confirmation on: (a) existence of data points, and (b) BQ table/column details if already pushed; otherwise, effort to push new data. Previous ownership attributed to Nhu/Jack's team.
3.  **Govt Mandate (MTI):** Implementation of "Price per Piece" info for 40+ categories in the current app MVP.
4.  **CHAS Calculation Bug:** UI discrepancy where cart-level discounts split at the sales order level affect CHAS calculations (Ticket: `DPD-530`).
5.  **Algolia Analytics:** Discussion on event tracking and a scheduled call.
6.  **Feature Rollout:** Enabling "Search on Omni home" with sticky header UI for Android users via feature flags.
7.  **SWA Migration (New):** Investigation into reverting SWA ad serving from Publitas back to Wordpress (`DIS-585`) and associated effort estimation.

**Pending Actions & Ownership**
*   **Delivery Logic Clarification:** Confirm current "Normal Delivery" display logic to enable text updates for "Express Delivery." *Owner: Daryl Ng (to clarify).*
*   **Gamification Data Query:** Clarify current ownership of Gamification features and provide BQ table/column names or confirm if data needs pushing for CRM automation. *Owner: Daryl Ng (to clarify).*
*   **Tech Lead Confirmation:** Determine if Daryl Ng is still the lead for the Price per Piece expansion or identify the correct owner (Loop in Sneha Parab). *Owner: Vivian Lim Yu Qian / Team.*
*   **CHAS Issue Analysis:** Explain the cart-level discount splitting issue to enable an API fix. *Owners: Prajney Sribhashyam, Wai Ching Chan.*
*   **Algolia Meeting:** Attend call at 11:00 AM (March 16) regarding agenda and required attendees (FE/BE). *Owner: Team (Decided by Vivian).*
*   **Android Rollout:** Enable "Search on Omni home" feature for 100% of Android users today. Ensure sticky header UI (`ENGM-2501`) is active and provide the minimum build number. *Owner: Andin Eswarlal Rajesh.*
*   **SWA Revert Analysis (New):** Assess effort required to revert SWA ad serving from Publitas back to Wordpress as per pre-Publitas state. *Owners: Sneha Parab, Arijit Mondal.*

**Decisions Made**
*   No formal decisions recorded in the log; the thread contains requests for confirmation and execution. The intent to fix the CHAS bug via an API update was established. The feasibility of reverting SWA ads is currently under investigation. Gamification data pipeline status and Delivery text logic are pending clarification from Daryl Ng.

**Key Dates & Deadlines**
*   **March 11:** Space creation; Vivian's inquiry on Price per Piece.
*   **March 12:** Daryl flags CHAS calculation issue (`DPD-530`).
*   **March 16 (Today):**
    *   **08:00 AM:** Algolia call scheduled (Vivian requested attendance).
    *   **Today:** Request to complete 100% Android rollout for Search on Omni home and Sticky Header UI.
    *   **07:39 AM:** Vivian initiates inquiry regarding SWA `DIS-585` migration history.
    *   **06:00 AM (March 24):** Rajesh Dobariya inquires about "Normal Delivery" logic to support Express delivery text updates. Last reply from Daryl Ng pending.

**Reference Links**
*   Price Per Piece Wiki: `https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008175965/Price+Per+Piece+Multipack+in+Display+Unit`
*   CHAS Ticket: `DPD-530`
*   Sticky Header UI Ticket: `ENGM-2501`
*   Harness Split Definition: Provided in Vivian's March 16 message.
*   SWA Migration Ticket: `DIS-585` (SWA Publitas <> Wordpress)


## [41/52] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/qtUOXlxVm80 | Last Activity: 2026-03-24T02:57:52.219000+00:00 | Last Updated: 2026-03-24T08:16:50.439979+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles:**
*   **Prajney Sribhashyam:** Initiator of the discussion; coordinating grooming sessions for the 'Re-delivery' use case.
*   **Wai Ching Chan:** Responded affirmatively to schedule a session.
*   **Michael Bui:** Identified as unavailable due to full meeting schedules; requested delegation.
*   **De Wei Tey:** Tagged in coordination requests (availability not explicitly confirmed in this thread).

**Main Topic:**
Discussion regarding the **'Re-delivery' use case for BCRS** (Jira: DPD-807). The group is reviewing necessary technical adjustments to prevent duplicate deposit postings. Key deliverables include:
1.  **Order Service:** Maintaining 'Deposit posted to SAP' in metadata.
2.  **Sales Posting:** Consuming the above field to suppress duplicate BCRS deposit postings.
3.  **RPA Logic:** Charging the BCRS deposit to the customer's original payment method.

**Actions Pending & Ownership:**
*   **Schedule Grooming Session:** Prajney Sribhashyam is coordinating availability for a quick grooming session.
    *   *Status:* Partially confirmed (Wai Ching Chan agreed). Michael Bui declined immediate attendance due to schedule conflicts.
*   **Proceed with Technical Discussion:** Wai Ching Chan and De Wei Tey are expected to proceed with the session without Michael Bui, utilizing recorded meetings for his review later.

**Decisions Made:**
*   Due to Michael Bui's full meeting schedule on Tuesday, Wednesday, and Thursday, the group will **proceed with the grooming session immediately** involving available members (Prajney, Wai Ching, De Wei).
*   Michael Bui will **review recorded meetings** from this session at a later date rather than attending live.

**Key Dates & Follow-ups:**
*   **Date of Discussion:** March 24, 2026.
*   **Relevant Meeting Blocks for Michael Bui:** Tuesday, Wednesday, and Thursday (following the discussion date).
*   **Reference Link:** https://ntuclink.atlassian.net/browse/DPD-807


## [42/52] Tiong Siong Tee
Source: gchat | Group: dm/700U4cAAAAE | Last Activity: 2026-03-24T02:57:18.291000+00:00 | Last Updated: 2026-03-24T08:17:02.251394+00:00
**Daily Work Briefing: Project Light (PRD Discussion)**

**Key Participants & Roles**
*   **Tiong Siong Tee:** Requester/Participant seeking documentation access.
*   **Michael Bui:** Responder providing document access; identified as the link sharer for this session.
*   **Sathya Murthi Karthik:** Document Owner (listed in metadata of the shared file).
*   **Vera Wijaya:** Editor (last edited the PRD on Mar 24, 2026).

**Main Topic**
Access and retrieval of the **[V2] PRD - Project Light: FPG App/BO/BE Replatform**. Tiong Siong Tee was unable to locate the file independently and requested a share from Michael Bui.

**Pending Actions & Ownership**
*   **None.** The request initiated by Tiong Siong Tee was immediately fulfilled by Michael Bui, and confirmation of receipt was provided by Tiong Siong Tee. No further action items are currently pending in this thread.

**Decisions Made**
*   No formal decisions were made; the conversation resulted solely in the successful distribution of a document link.

**Key Dates & Timeline**
*   **March 24, 2026 (02:21 UTC):** Tiong Siong Tee requested the PRD.
*   **March 24, 2026 (02:56 UTC):** Michael Bui shared the Google Docs link and confirmed the document title and owner.
*   **March 24, 2026 (02:57 UTC):** Tiong Siong Tee acknowledged receipt.
*   **Last Edited:** March 24, 2026 by Vera Wijaya.

**Specific References**
*   **Document Title:** [V2] PRD - Project Light: FPG App/BO/BE Replatform
*   **Document URL:** https://docs.google.com/document/d/1Z1kMCH5RGeeAPEABiWYprtpoujvsMVRCXInVlgahBNc/edit?tab=t.653xa9d75b02
*   **Resource Link:** https://chat.google.com/dm/700U4cAAAAE


## [43/52] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/j3nM7DjQY4I | Last Activity: 2026-03-24T02:56:08.517000+00:00 | Last Updated: 2026-03-24T08:17:20.187845+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Tiong Siong Tee:** Technical lead/architect; focused on bundle IDs, rollback feasibility, and data synchronization logic.
*   **Michael Bui:** Developer/Analyst; clarifying migration metrics and user behavior implications.
*   **Alvin Choo:** Project Lead/Stakeholder; driving the strategic timeline, scope (app + seller), and contingency planning.
*   **Gopalakrishna Dhulipati:** Technical Architect; defining versioning strategy (v70 vs. v71) and stack architecture.
*   **Daryl Ng:** Engineer; proposing technical solutions for data migration and risk mitigation.

**Main Topic**
Discussion regarding the migration strategy from the existing app to "Project Light" (v71). The team debated the feasibility of a single bundle ID, the necessity of rolling back in case of failure, and the timeline for decommissioning the old stack (v70) while maintaining service continuity.

**Key Decisions & Clarifications**
*   **Bundle ID Strategy:** Confirmed to be the **same bundle ID** for both versions, despite initial speculation otherwise. This complicates differentiation between users on the old vs. new app.
*   **Architecture:** v70 will operate on the legacy DBP stack with hotfixes in production. v71 is the new "Light" app running on a new DSP stack, initially deployed via a beta track to specific locations (e.g., postal codes).
*   **Rollback Risk:** Because there is no soft rollback mechanism for a shared bundle ID, any failure requires reverting to the old version entirely. This eliminates the ability to simply "switch back" without disrupting data integrity across engines.
*   **Data Sync:** Acknowledged that robust bi-directional or asynchronous data synchronization between the two engines (v70 and v71) is critical for a smooth transition and potential rollback scenarios.

**Pending Actions & Owners**
*   **Define Data Migration Plan:** Execute a one-way async migration from old to new platform for transactional data while preparing contingency sync-back mechanisms. *(Owner: Daryl Ng / Engineering Team)*
*   **Contingency Planning:** Formalize "Plan B" regarding rollback scenarios, acknowledging that this is a secondary plan but must be prepared if the main GTM (Go-To-Market) fails. *(Owner: Alvin Choo)*
*   **Data Migration Track Alignment:** Ensure the data migration development track starts simultaneously with the app build for v71. *(Owner: Gopalakrishna Dhulipati)*

**Key Dates & Deadlines**
*   **Migration Window:** The maximum duration allowed for running both apps in parallel is **4 weeks**. (Note: A previous mention of a "2-month" parallel run was raised by Michael Bui but appears to be a point of clarification rather than the final agreed constraint, which Alvin Choo capped at 4 weeks).
*   **Discussion Date:** March 24, 2026.

**Summary of Concerns**
The team views the migration as "very challenging" and "scary" due to the lack of a soft rollback capability with a shared bundle ID. The primary risk is data inconsistency if services must be cut over quickly within the 4-week window while maintaining full seller and transactional integrity.


## [44/52] Release - FPG Back Office (Mon-Thurs)
Source: gchat | Group: space/AAAAoJgpZBM | Last Activity: 2026-03-24T02:17:11.193000+00:00 | Last Updated: 2026-03-24T08:18:03.238389+00:00
**Daily Work Briefing: FPG Back Office Releases**

**Key Participants & Roles**
*   **Rohit Pahuja:** Primary communicator; responsible for announcing scheduled releases and providing release note links.

**Main Topic**
The conversation focuses on confirmed software deployment schedules for the **Back Office** system, specifically targeting versions **v8.35.0**, **v8.36.0**, and the newly announced **v8.37.0**. These informational messages serve to notify the team of upcoming maintenance windows aligned with the FPG Back Office (Mon-Thurs) resource schedule.

**Pending Actions & Ownership**
*   **Action:** Monitor the Back Office system during release execution for all scheduled versions.
    *   **Owner:** Team (implied by "Hi team" notifications).
*   **Action:** Review specific release notes for version updates and change logs.
    *   **Owner:** Team members referencing the provided links.

**Decisions Made**
No new strategic decisions were made; messages confirm three existing scheduled deployment plans:
1.  Deployment of **Backoffice_v8.35.0**.
2.  Deployment of **Backoffice_v8.36.0**.
3.  Deployment of **Backoffice_v8.37.0** (Newly confirmed).

**Key Dates, Deadlines, & Follow-ups**
*   **Release 1:**
    *   **Version:** Backoffice_v8.35.0
    *   **Announced:** March 9, 2026, at 05:11 UTC (05:11 AM).
    *   **Scheduled Execution:** Approximately 1:20 PM on March 9, 2026.
    *   **Reference:** [Backoffice_v8.35.0 Release Notes](https://ntuclink.atlassian.net/wiki/spaces/SE/pages/3290431602/Backoffice_v8.35.0)
*   **Release 2:**
    *   **Version:** Backoffice_v8.36.0
    *   **Announced:** March 12, 2026, at 13:44 UTC (1:44 PM).
    *   **Scheduled Execution:** Same day (March 12, 2026).
    *   **Reference:** [Backoffice_v8.36.0 Release Notes](https://ntuclink.atlassian.net/wiki/spaces/SE/pages/3304423425/Backoffice_v8.36.0)
*   **Release 3 (New):**
    *   **Version:** Backoffice_v8.37.0
    *   **Announced:** March 24, 2026, at 02:17 UTC (02:17 AM).
    *   **Scheduled Execution:** Same day (March 24, 2026) relative to announcement.
    *   **Reference:** [Backoffice_v8.37.0 Release Notes](https://ntuclink.atlassian.net/wiki/spaces/SE/pages/3334537232/Backoffice_v8.37.0)

**Contextual Notes**
*   These updates align with the resource schedule for **FPG Back Office (Mon-Thurs)**.
*   The conversation log indicates replies were received to announcements, though specific reply content is not detailed in this summary.


## [47/52] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/YnGsH8DqBGs | Last Activity: 2026-03-24T01:04:16.482000+00:00 | Last Updated: 2026-03-20T15:42:59.594021+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Michael Bui:** Raises strategic questions regarding fulfillment models, cart unification, and AI architecture.
*   **Daryl Ng:** Directs the inquiry to existing project documentation ("Workbench").
*   **Gopalakrishna Dhulipati:** Provides definitive technical clarification on "Project Hive" concepts and operational strategy.
*   **Tiong Siong Tee:** Validates the concept and summarizes the operational shift.

**Main Topic**
Discussion regarding the strategic implications of **Project Hive**, specifically focusing on:
1.  Changes to fulfillment models (Store vs. Hive).
2.  Potential for cart unification across channels.
3.  AI/Agentic architecture centralization vs. decentralization.

**Decisions & Clarifications**
*   **Hive Definition:** Project Hive is defined as a **sortation center**, not an inventory holding location. It does not store stock like traditional stores or DCs.
*   **Fulfillment Flow:** Orders will be placed directly to Distribution Centers (DCs) similar to how stores order from DCs. The DC sends picklists/product batches to the four Hives across Singapore. Hives then break down orders at the individual level, sort them, and dispatch to customers.
*   **Strategic Shift:** This is a multi-year journey transitioning from "fulfillment from store" to "fulfillment from Hive."
*   **Quick Commerce:** Initial decision indicates **no** quick commerce operations will originate directly from Hives; express delivery will likely remain fulfilled from stores during this transition.

**Pending Actions & Ownership**
*   **Review Project Documentation:** Michael Bui is advised by Daryl Ng to consult the "Workbench" on Project Hive for detailed specifications regarding fulfillment changes and inventory logic.
    *   *Owner:* Michael Bui (implied via suggestion).
*   **Cart Unification Strategy:** The question of a unified cart across Online, Offline, and O2O channels remains open pending further architectural planning, as no confirmation was provided in this thread.

**Key Dates & References**
*   **Date:** March 20, 2026 (Conversation timeline: 00:24 – 12:18 UTC).
*   **Project Reference:** Project Hive (Sortation Centre initiative).
*   **Location Scope:** Singapore (SG) – Four Hives planned.
*   **URL:** https://chat.google.com/space/AAQAsFyLso4


## [48/52] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Last Activity: 2026-03-24T01:01:09.513000+00:00 | Last Updated: 2026-03-21T02:08:46.969727+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Mar 21, 09:30 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-discovery`.
*   **Escalations:** `@hangouts-GT-Search-DatadogAlerts`, `@oncall-dpd-staff-excellence-pdm`, `@hangouts-GT-Discovery-DatadogAlerts`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Search Indexing, QC Layout Service, SAP Data Sync, Catalogue Service.

**Main Topic**
**CRITICAL ALERT (P2):** The `fp-search-indexer` service remains in a **P2 Error State** on production. New transient alerts have triggered and resolved; however, the unresolved P2 error state from Mar 18 persists as the highest priority.

**Pending Actions & Ownership**
*   **Action:** **URGENT INVESTIGATION:** Address critical errors on `fp-search-indexer` (env: prod).
    *   **Owner:** Product Data Management On-Call (`@oncall-dpd-staff-excellence-pdm`).
    *   **Status:** Active since Mar 18; re-triggered Mar 19, 15:35 UTC. No resolution achieved.
    *   **Required Checks:** Review Datadog logs, inspect K8s deployment (`fpon-cluster/default/fp-search-indexer`), consult Runbook (Jira SR-2001831558).

*   **Action:** Investigate `qc-layout-service` latency spikes.
    *   **Owner:** Product Data Management Team (`@hangouts-dd-dpd-grocery-alert`).
    *   **Status:** Triggered Mar 20, 00:24 UTC (P99 > 1.8s @ 2.381s; P90 > 1.1s). No recovery status noted in logs yet.
    *   **Context:** High latency on food product listing requests (`get_/v1/pages/plp`).

*   **Action:** Monitor `sku-store-attribute` job stability.
    *   **Owner:** DPD Grocery Discovery Team (`@hangouts-dd-dpd-grocery-alert`).
    *   **Status:** Triggered Mar 20, 00:59 UTC (<6 files in 4h); **Recovered** at Mar 21, 00:59 UTC. Monitor for recurrence of low file counts.

*   **Action:** Investigate SAP Data Sync volume anomalies.
    *   **Owner:** Product Data Management Team (`@opsgenie-dpd-grocery-discovery`).
    *   **Status:** Triggered Mar 20, 01:01 UTC (P3). Alerts indicate >2000 files received/stored per day for `fpon-sap-jobs-file-parser`.

*   **Action:** Monitor `go-catalogue-service` latency.
    *   **Owner:** Discovery Team (`@hangouts-GT-Discovery-DatadogAlerts`).
    *   **Status:** Triggered Mar 20, 08:51 UTC (P90 > 2.0s @ 4.005s); **Recovered** at Mar 20, 09:27 UTC (Value: 0.675s).

**Decisions Made**
*   The `fp-search-indexer` failure is confirmed persistent; previous "resolved" status was invalid.
*   Transient P3 issues (`sku-store-attribute`, `go-catalogue-service`) have self-resolved but require continued monitoring for flapping patterns.
*   New latency alerts on `qc-layout-service` and volume spikes in SAP ingestion are active and require immediate log review.

**Key Dates & Follow-ups (Mar 16–21, 2026)**
*   **Service: `fp-search-indexer` (P2 - Product Data Management) [ACTIVE CRITICAL]**
    *   *Latest Timeline:* Active since Mar 18; re-triggered Mar 19, 15:35 UTC.
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/17447691) | [Runbook](https://ntuclink.atlassian.net/wiki/spaces/SR/pages/2001831558/Support+Run+book).
*   **Service: `qc-layout-service` (P3 - Product Data Management) [ACTIVE]**
    *   *Issue:* PLP request latency (P99 > 1.8s, P90 > 1.1s).
    *   *Latest Timeline:* Triggered **Mar 20, 00:24 UTC**.
    *   *Links:* [Monitor 20382947](https://app.datadoghq.eu/monitors/20382947) | [Monitor 20382948](https://app.datadoghq.eu/monitors/20382948).
*   **Service: `sku-store-attribute` (P3 - Grocery Discovery)**
    *   *Status:* **Recovered** Mar 21, 00:59 UTC following a re-trigger at 00:54 UTC on the same day due to <6 processed files. Monitor ID: `20382848`.
*   **Service: `fpon-sap-jobs-file-parser` (P3 - Product Data Management) [ACTIVE]**
    *   *Issue:* Excessive file volume (>2000/day).
    *   *Latest Timeline:* Triggered **Mar 20, 01:01 UTC**. Monitors `92102475` (Received) & `92102474` (Stored).
*   **Service: `go-catalogue-service` (P3 - Discovery)**
    *   *Status:* **Recovered** Mar 20, 09:27 UTC following latency spike at 08:51 UTC. Monitor ID: `17447967`.

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c


## [49/52] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Last Activity: 2026-03-24T00:03:09.059000+00:00 | Last Updated: 2026-03-21T02:10:08.620197+00:00
**Daily Work Briefing Summary (Updated: March 21, 2026)**

**Key Participants & Roles**
*   **Michael Bui:** Primary recipient; responsible for code reviews, UAT support, and project ownership.
*   **Tan Gay Lee / Hendry Tionardi / Olivia:** Finance/UAT coordination (BCRS).
*   **Nikhil Grover / Ravi Singh / Yian Koh:** Programmatic advertising (Advertima/TTD) strategy and testing.
*   **Gautam Singh / Sundy Yaputra / Daryl Ng:** Development leads for Search Indexer, BCRS, and Platform fixes.
*   **James Lai / Mohammed Miran / Andin Eswarlal Rajesh:** iOS Chapter handover responsibilities.

**Main Topics & Discussions**
1.  **Programmatic Advertising (Advertima/TTD):** Focus remains on validating discrepancies for `advertima_ttd-fixed-price-test-1.5`. Ravi Singh confirmed receipt of raw BURLs; validation was targeted for Monday, March 17th. Yian Koh requested confirmation on deals `advertima_ttd-first-price-test` and `advertima_ttd-fixed-price-test-1`.
2.  **New Deal Setup:** Yasmina Tregan (Advertima) required an end-to-end test setup this week. Wei Phung to share live campaign details; Ravi Singh to execute setup, push to TradeDesk, and map segments before launch.
3.  **BCRS UAT & Finance Integration:** Progress on SAP document numbers, duplicate posting fixes via PubSub "exactly once" policy (PR #1033), and Bukit Timah Plaza pricing/display issues.
4.  **Event Sync Optimization (DPD-645):** Addressing the massive event overage (14M vs. normal 550k). PRD deployment plan set for Sunday, March 15.
5.  **Security & Compliance:** RMN Pentest fixes (DPD-700) deployed to Prod; Bitbucket App Passwords deprecated effective June 9, 2026.

**Status Update: Inbox & Communications**
*   **Inbox Status:** As of March 21, 2026, the workspace inbox is fully caught up across all categories (**Urgent Action Items**, **High-Volume/Project Themes**, **Meeting Updates**, and **FYI**). No pending unread items require immediate attention.

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

**Note on New Content:** The latest system notification confirms the inbox remains clear of urgent action items, project themes, meeting updates, and FYI notices as of March 21, 2026. No changes to pending actions or decisions were required based on this update.


## [50/52] Google Drive
Source: gchat | Group: dm/7d1XKcAAAAE | Last Activity: 2026-03-23T16:32:09.857000+00:00 | Last Updated: 2026-03-19T06:25:24.600564+00:00
**Daily Work Briefing Summary (Updated)**

**Key Participants & Roles:**
*   **Nikhil Grover (FairPriceGroup):** Attempted to access "ACNxOsmos: Daily Cadence" notes; encountered Drive processing errors. Previously attempted to share "Programmatic Ads tracking events."
*   **Sujit Jha (Onlinesales.ai):** Attempted to share "Ads tracking events"; file access failed due to recipient blocking.
*   **Michael Bui (Business/Stakeholder):** Blocked Sujit Jha's document; previously flagged as a blocked user in Drive incidents.
*   **Tan Gay Lee (Finance):** Driving UAT financial validation requiring SAP document numbers.
*   **Hendry Tionardi (Operations/IT):** Managing technical clarifications on POS/SAP integration.

**Main Topics:**
1.  **BCRS UAT 2026 Financial Validation:** Finance requires SAP document numbers to verify end-to-end posting. Queries remain regarding discrepancies in document counts (3 documents for a $45.90 order) and missing BCRS documents affecting Row 4 and 5 validation.
2.  **Ads Tracking Data Sharing & Access Issues:** Continued failures in sharing tracking event documents between FairPriceGroup and Onlinesales.ai domains.
    *   **March 18:** Sujit Jha's "Ads tracking events" shared failed due to Michael Bui blocking `sujit.jha@onlinesales.ai`.
    *   **March 18:** Nikhil Grover's "Programmatic Ads tracking events - Source OSMOS" share failed with a Google Drive processing error.
    *   **March 19 (13:48 GMT+08):** Nikhil Grover requested Editor access to the document **"ACNxOsmos: Daily Cadence - 2026/03/16"** but received a "Google Drive is unable to process your request" error.

**Pending Actions & Owners:**
*   **UAT SAP Document Update:** Hendry Tionardi and the BCRS team must update Column J with valid SAP document numbers immediately. Finance cannot proceed without this data. *(Note: Original deadline was March 10; current date is now March 19, requiring urgent resolution).*
*   **Scan & Go Flow Confirmation:** Hendry Tionardi requested **Onkar Bamane** to confirm if the "Scan and Go" flow posts sales data as an aggregate invoice to SAP rather than individual receipts.
*   **Ads Tracking Resolution:** Michael Bui or Nikhil Grover must resolve access permissions for tracking documents (OSMOS source) with Finance/Operations, given persistent blockages and processing errors between domains.

**Decisions Made:**
*   **RMN Incident Impact:** Confirmed there is **no financial revenue impact**.
*   **Postmortem Template:** Michael Bui confirmed that breaking down the Executive Summary follows the approved **v2 postmortem template**.

**Key Dates & Deadlines:**
*   **March 6, 2026:** Initial request for SAP document numbers issued.
*   **March 10, 2026 (Original Deadline):** Finance required SAP document numbers in BCRS UAT spreadsheet (Missed).
*   **March 12, 2026:** D&T Q1 All Hands meeting.
*   **March 18, 2026:** Failed attempts to share Ads tracking files by Sujit Jha and Nikhil Grover.
*   **March 19, 2026 (13:48):** Nikhil Grover failed to gain Editor access to "ACNxOsmos" notes due to Drive processing error.

**References:**
*   **BCRS UAT 2026 Spreadsheet:** [Link](https://docs.google.com/spreadsheets/d/1o6oklFTFyzpT490vQ4x8IKc00vdL41pl9hUAaQgg-ns/edit)
*   **RMN Incident Report (v2 Template):** [Link](https://docs.google.com/document/d/1XiN0diQicup7ujoCWWKdD3Hvp8J0OJD5LPOfnthegyE/edit)
*   **Postmortem v2 Template:** [Link](https://docs.google.com/document/d/1ZntG-Ggb1NI7WLUa2uLb6u5RX9VxYUefUT364OWOJhI/edit)
*   **ACNxOsmos Daily Cadence (Access Failed):** [Link](https://docs.google.com/document/d/1LWKTTxcCJxIS12EkIvJmyXFNfjHXCF5ZYu2v5Vg4r9o/edit?usp=drive-dynamite&userstoinvite=nikhil.grover@fairpricegroup.sg&role=writer&ts=69bb8e22)
*   **Ads Tracking Events (Failed Share):** [Sujit Jha Link](https://docs.google.com/document/d/1LkZAkPEP5jNy1mkJDc9JzrpTG0PrDWZ8V2YVcmp2KA0/edit) | **Blocker:** Michael Bui.
*   **Programmatic Ads Tracking (Failed Share):** [Nikhil Grover Link](https://docs.google.com/document/d/1_DirQKHwYEkq2eOyfYkt0wcNj2jg2G_lOkvxghKIAj0/edit)


## [51/52] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw | Last Activity: 2026-03-23T04:12:50.830000+00:00 | Last Updated: 2026-03-18T22:37:50.842992+00:00
**Daily Work Briefing: Digital Product Development (DPD)**

**Key Participants & Roles**
*   **Flora Wo Ke:** Team Lead (Project Status, Incident Response).
*   **Alvin Choo:** Developer/QA (Feature Release, Payment Services).
*   **Nicholas Tan:** DevOps/Infrastructure (Golden Pipeline, Container Risks).
*   **Tiong Siong Tee / Andin Eswarlal Rajesh:** QA/Engineering (iOS Bug Reporting).
*   **Winson Lim:** Engineering Lead/Strategy (Disaster Recovery Scenarios, UX Trends).
*   **Natalya Kosenko:** DevOps/SRE (Datadog Infrastructure as Code Governance).
*   **Boning He / Gopalakrishna Dhulipati:** Team Members (Social/Culture).
*   **Kyle Nguyen:** Team Member (Event Coordination).
*   **Maou Sheng Lee:** Team Member.

**Main Topics & Discussions**
1.  **Infrastructure & Operations Risk:** Nicholas Tan flagged an operational risk regarding Broadcom ending free Bitnami images, causing `kubectl` image tag failures and increased Time To Recovery (TTR) during service resuscitation. The issue impacts the Golden Pipeline (GP).
2.  **Payment Service Issues:** Alvin Choo reported that promo codes failed to redeem in FP Pay. Later confirmed that a change freeze has ended and feature releases are proceeding.
3.  **Mobile Quality Assurance:** Andin Eswarlal Rajesh identified a bug on iOS FPPay where QR codes load correctly without user login. The issue was escalated via file download.
4.  **Datadog Governance:** Natalya Kosenko reported unauthorized manual changes to Datadog On-Call teams (removals of Maxine, Arijit, Minu). She emphasized that Terraform manages this config; manual console edits are overwritten on the next run.
5.  **Strategic Planning:** Winson Lim highlighted data centers as potential targets in modern warfare (Iran conflict context) to inform Disaster Recovery (DR) scenarios.
6.  **Social Events & Sentiment:** Kyle Nguyen announced an upcoming DPD BBQ with the sentiment "We come first." Wai Ching Chan responded positively, tagging Vincent Wei Teck Lim regarding event details. Maou Sheng Lee expressed a sentiment of feeling like energy is being wasted on March 18.
7.  **Social Notes:** Boning He and Gopalakrishna Dhulipati shared snacks (Chinese cookies with chicken gizzard/medicinal barley and Indian cookies) in pantry areas.

**Pending Actions & Owners**
*   **GP Team (Nicholas Tan / Mohit Niranwal):** Investigate Bitnami image replacement strategy to resolve TTR issues and update Golden Pipeline dependencies.
*   **iOS/Dev Team (Tiong Siong Tee / Andin Eswarlal Rajesh):** Investigate the iOS FPPay QR code login bypass bug.
*   **Datadog Admins:** Anyone who manually altered Datadog Teams must submit a Pull Request to `https://bitbucket.org/ntuclink/fp-datadog-eu` instead of editing the console to prevent configuration loss.

**Decisions Made**
*   No formal change freeze; feature releases are currently active (Alvin Choo).
*   Datadog team configurations must strictly follow Infrastructure as Code (Terraform) protocols; manual overrides are deprecated.

**Key Dates & Follow-ups**
*   **Mar 3, 2026:** Project status noted as "one step behind."
*   **Mar 7, 2026:** FP Pay promo code issue raised; change freeze lifted same day.
*   **Mar 9, 2026:** BCRS discussion and Meta AI news shared.
*   **Mar 10, 2026:** iOS bug discovered.
*   **Mar 12, 2026:** "BB incident" query raised; Data center DR scenario discussed.
*   **Mar 13, 2026:** Datadog governance warning issued.
*   **Mar 17, 2026:** DPD BBQ announcement made by Kyle Nguyen; Wai Ching Chan engaged with Vincent Wei Teck Lim regarding the event (Last Reply: 12:15 PM).
*   **Mar 18, 2026:** Maou Sheng Lee noted sentiment regarding wasted energy.

**Social Notes**
*   Boning He and Gopalakrishna Dhulipati shared snacks in pantry areas.
*   Upcoming DPD BBQ announced by Kyle Nguyen ("We come first, see you!").


## [52/52] [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Last Activity: 2026-03-23T03:09:51.747000+00:00 | Last Updated: 2026-03-21T05:00:39.207120+00:00
**Daily Work Briefing: [Prod Support] Marketplace**

**Key Participants & Roles**
*   **Support/Operations:** Willie Tan, Iris Chang, Lalita Phichagonakasit, Charlene Tan, Jie Yi Tan, Ayton See, Amos Lam.
*   **Technical/Admin Team:** Dang Hung Cuong, Shiva Kumar Yalagunda Bas (Frequent recipients of access/access issues), Olivia -, Jill Ong, Greta Lee, Zaw Myo Htet, Angella Yeo, Cassandra Thoi, Gopalakrishna Dhulipati.

**Main Topics & Discussion Summary**
The conversation covers critical operational blockers regarding seller onboarding, order fulfillment discrepancies, system configuration errors, urgent promotion removal requests, and new order inquiries. Major themes include:

1.  **Access Management:** Requests to grant "PickerApp" access for new/existing sellers (Meat Affair, Old Shanghai, BulkMartGo, PETS STATION HOLDING). Charlene Tan reported a new seller (Woah Group) encountering errors under the "Offers" section.
2.  **Sales Data & Reporting:** Issues with vendors (CoLab Apac, Old Shanghai) not receiving sales breakdown reports since inception.
3.  **Promotion & Pricing Conflicts:**
    *   **Urgent Removal Request:** Lalita Phichagonakasit (Mar 20) reported an incorrectly set up promotion for **Item ID: 90244361** requiring immediate removal from the backend to prevent financial loss. This follows previous reports of stuck frontend states and expired promotions lingering on Mirakl.
    *   Conflicting promotions for "Falcon Galaxy Strong Garbage Bag" require one to be disabled.
    *   Discount prices not showing despite SKU publication.
4.  **Fulfillment & System Errors:**
    *   Delivery slot display discrepancy for seller "Funa Artistic Hampers & Gifts" (Mar 19): Mirakl shows 91h vs Frontend date; focus remains on a window duration issue showing 4 days instead of the expected 2 days.
    *   Missing items in PickerApp compared to email picklists (Atasco Dairy, Estalife).
    *   Orders completed without delivery by NJV (Order #246974265, #248270820).
    *   Seller description/image updates not triggering "Pending Verification" status.
5.  **New Listing & Logic Queries:**
    *   **Item Visibility:** Lalita Phichagonakasit reported SKU **13226899** failing to appear under postal code **762115** since March 14th, despite prior online availability.
    *   **Picklist Logic (New):** Amos Lam (Mar 21) raised a critical issue where a vendor who opted out of public holidays in December did not receive a pick list today. This requires immediate investigation into why the system failed to generate a list for an opt-out status.
6.  **SAP Configuration Inquiry:** Iris Chang queried the definition and data source of "Lead Time" within SAP T-code ZMP_VENDOR on Mar 18.
7.  **Order Status Inquiry (New):** Angela Yeo (Mar 21) raised a query regarding FFS orders for seller **Yumsay Food**, seeking technical team advice.

**Pending Actions & Ownership**
*   **Urgent Promotion Removal:** Dang Hung Cuong and Gopalakrishna Dhulipati to immediately remove incorrectly set up promotion for Item ID: 90244361 (Lalita Phichagonakasit request, Mar 20).
*   **Picklist Generation Failure (New):** Technical team (Dang Hung Cuong, Shiva Kumar Yalagunda Bas) to investigate why a vendor who opted out of public holidays in December did not receive a pick list today (Amos Lam, Mar 21).
*   **FFS Order Inquiry:** Technical team to investigate FFS order status for seller "Yumsay Food" (Angela Yeo, Mar 21).
*   **Close DF SOF Order:** Willie Tan requested closure; tracking via DST-2578 (Owners: Dang Hung Cuong, Shiva Kumar Yalagunda Bas).
*   **Vendor Report Issues:** Investigate missing sales breakdown reports for CoLab Apac (NED-277148) and Old Shanghai (NED-277329).
*   **Access Grants:** Grant PickerApp access to Meat Affair, BulkMartGo, PETS STATION HOLDING, and others. Resolve Woah Group "Offers" error (Charlene Tan).
*   **Fulfillment Investigation:** Check why Estalife missing Final Picklist PFC; investigate delivery slot display for Funa Artistic Hampers & Gifts (4 days vs 2 days expected); determine trigger for NJV non-delivery completions.
*   **System Logic & Listing Fixes:** Investigate missing SKU 13226899 listing for postcode 762115; clarify picklist generation logic for postponed orders. Resolve SAP ZMP_VENDOR Lead Time definition (Dang Hung Cuong/Amos Lam).

**Decisions Made**
*   Dang Hung Cuong is prioritizing the removal of Item ID: 90244361, the new picklist failure issue raised by Amos Lam, and the Woah Group offers error. Dang Hung Cuong and Shiva Kumar Yalagunda Bas are assigned to investigate the vendor picklist anomaly. Ayton See previously educated a seller on promotion setup rules after identifying a configuration error.

**Key Dates & Deadlines**
*   **2026-03-21 (Today):** Angela Yeo requested advice on FFS orders for "Yumsay Food" (Last reply 3 min ago). Amos Lam reported the vendor picklist failure due to public holiday opt-out status. Previous urgent request to remove Item ID: 90244361 remains active from Mar 20.
*   **2026-03-19 (Yesterday):** Jie Yi Tan reported Funa Artistic Hampers & Gifts delivery window discrepancy; discussion ongoing with 34 replies.
*   **2026-03-18:** Iris Chang inquired about SAP T-code ZMP_VENDOR "Lead Time" definition.
*   **2026-03-03:** DF SOF order request raised.
*   **December 2025 (Historical Context):** Vendor involved in Amos Lam's query opted out of public holidays.
