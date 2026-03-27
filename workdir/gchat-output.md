

## [1/30] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 17 | Last Activity: 2026-03-27T14:30:16.703000+00:00 | Last Updated: 2026-03-27T14:33:23.442422+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (Updated March 27, 14:30 UTC)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
Instability persists into the mid-afternoon of **March 27**, evolving from morning latency spikes to a cycle of intermittent high error rates and throughput degradation. While early-morning profile update latencies recovered, **13:47–14:30 UTC** saw recurring alerts for `engage-my-persona-api-go` (high errors, p90/p99 latency) alongside new reliability drops in `frontend-gateway` (Orchid service) and mobile linkpoints (`ef-android`, `ef-ios`).

**Status Summary & Timeline (Afternoon Surge)**
*   **Recurring Latency & Errors (`engage-my-persona-api-go`):**
    *   **13:47 UTC:** p99 for `post_/new-myinfo/confirm` recovered (Value: 1.031s).
    *   **13:52 UTC:** p90 for `patch_/user/profile` triggered (>1.8s, Value: 1.911s); Recovered at 13:55 UTC.
    *   **13:54–13:56 UTC:** High error rate detected (Peak: 0.103%); Recovered at 13:56 UTC.
    *   **14:14 UTC:** High error rate re-triggered (Value: 0.105%); Recovered at 14:29 UTC.
    *   **14:21 UTC:** p90 for `post_/new-myinfo/confirm` triggered (>1.8s, Value: 2.009s).
*   **Search Reliability (`frontend-gateway`):**
    *   **13:50–14:30 UTC:** Orchid service success rate dropped below 99.9% twice (Lowest: 99.796% @ 14:17). Both instances recovered by 14:30 UTC. Owner: **Squad Journey**.
*   **Mobile Linkpoint Degradation:**
    *   **Android (`ef-android`):** Success rate dropped to 99.495% (13:57) and 99.379% (14:28), recovering immediately each time. Owner: **Squad Compass**.
    *   **iOS (`ef-ios`):** New alert triggered at **14:30 UTC** with success rate at 98.592%. Owner: **Squad Compass**.

**Pending Actions & Ownership**
*   **Investigate `engage-my-persona-api-go` Instability:** Address recurring error spikes (peaking >0.1%) and latency regressions in profile updates (`patch_/user/profile`) and MyInfo confirmations. Owners: **Squad Dynamics**.
*   **Analyze Orchid Service Drops:** Investigate intermittent success rate fluctuations (<99.9%) affecting the recommender service. Owner: **Squad Journey**.
*   **Monitor Mobile Linkpoints:** Immediate attention required for iOS (`ef-ios`) degradation at 14:30 UTC and recurring Android issues. Owners: **Squads Compass, Dynamics**.

**Decisions Made**
*   **Severity Escalation:** Incident severity remains high due to the resurgence of `engage-my-persona-api-go` errors and the expansion of mobile linkpoint failures (iOS alert triggered).
*   **Pattern Continuity:** Issues have shifted from single-point latency spikes to cyclical throughput degradation across backend identity services and frontend recommendation engines, impacting user profile updates and search functionality.

**Key Dates & Follow-ups**
*   **Active Window:** March 24–27 (UTC). Recent critical activity: **09:51 – 14:30 UTC** (March 27).
*   **Reference Links (Updated):**
    *   `engage-my-persona-api-go` Error Monitor #92965074 (Peak: 0.105% @ 14:14)
    *   `frontend-gateway` Orchid Monitor #17448311 (Lowest: 99.796% @ 14:17)
    *   `ef-ios` Linkpoints Monitor #63109468 (Value: 98.592% @ 14:30)
    *   `engage-my-persona-api-go` MyInfo p90 Monitor #50879027 (Value: 2.009s @ 14:21)


## [2/30] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-03-27T14:27:05.366000+00:00 | Last Updated: 2026-03-27T14:34:05.541692+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Afternoon Update)**
**Date:** March 27, 2026 (Shift Extended)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 500

### Key Participants & Roles
*   **System/Tool:** Datadog App (Automated Monitoring)
*   **Notification Channel:** `@hangouts-ShoppingCartNotification`
*   **Ownership Teams:** `dpd-pricing`, `dpd-pricing-cart`.

### Main Topic
Instability persists in `frontend-gateway` and `st-cart-prod`. The incident has evolved into a high-frequency oscillation involving latency spikes on "Put Product ID to Wish List" and "Get Wish List," alongside intermittent success rate drops. A critical **SLO Error Budget Alert (P2)** has been triggered, indicating 70.165% of the 7-day error budget is consumed.

### Incident Timeline & Actions
**Previous Context:**
*   *Activity from March 20–March 27 UTC+09:49 regarding `frontend-gateway` latency and checkout dips.*

**New Activity (Afternoon Shift, March 27 UTC+0)**
*   **12:44–12:45 UTC:** Brief P90 "Get Wish List" spike (**1.978s**, threshold 1.7s); recovered at 12:45 UTC.
*   **13:10–13:20 UTC:** Severe Recurrence of "Put Product ID to Wish List":
    *   P99 Latency spiked to **9.324s** (Threshold 6.0s).
    *   Concurrent P90 spikes reached **5.173s** and **9.324s**. All recovered by 13:20 UTC.
*   **13:42–13:47 UTC:** Rapid Oscillation on "Get Wish List": P90 spiked to **1.918s** twice (triggered/recovered in <5 min each).
*   **13:47–13:57 UTC:** Success Rate Dip: "Get V2 Shopping List" dropped to **99.672%** (Threshold 99.9%); recovered at 13:57 UTC.
*   **14:26–14:27 UTC:** P90 "Get Wish List" spiked again (**1.747s**).
    *   **14:27 UTC:** **[P2] SLO Error Budget Alert**: 70.165% of the 7-day budget consumed.

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** The incident is now a multi-service oscillation. The SLO alert indicates an imminent breach risk if latency patterns continue. Success rate dips on checkout have occurred multiple times today (07:02, 08:56, 13:47).
*   **Immediate Action Required:** Correlate trace data for recent Event IDs `8562295722384480554` (P90 Get Wish List), `8562321581209029892` (P99 Put Latency), and `8562399127059707216` (SLO Budget). Investigate the root cause of the ~1-hour oscillation cycle affecting both frontend-gateway and st-cart-prod.

### Decisions Made
*   **Priority Escalation:** Status remains **"Critical Incident"** with added **P2 SLO Warning**. The pattern confirms active, recurring degradation across multiple services rather than isolated spikes. Activity extends from March 20 through at least 14:27 UTC with no sustained stabilization observed.
*   **Focus Shift:** Prioritize analysis of "Put Product ID to Wish List" and "Get Wish List" resources. Correlate Monitor `21245708` (Checkout Success) with Monitor `21245793` (SLO Budget Alert). Immediate stabilization is required to prevent SLO breach.

### Key Dates & Follow-ups
*   **Critical Window:** Extended activity from March 20 through at least March 27, 14:27 UTC.
*   **Follow-up:** Immediate trace correlation for the 13:10–14:27 UTC window to resolve recurring latency spikes and success rate drops before completing the shift.

### References
*   **Active Monitors:** `21245708` (Checkout Success), `22710472` (S&G Post Cart Success), `21245701/21245706` (Wish List Latency), `21245720` (Get Wish List P90), `21245735` (Shopping List Success), `21245793` (SLO Budget).
*   **Service Tags:** `service:frontend-gateway`, `service:st-cart-prod`, `team:dpd-pricing`.


## [3/30] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Messages: 3 | Last Activity: 2026-03-27T13:16:22.780000+00:00 | Last Updated: 2026-03-27T14:34:38.522597+00:00
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

**Newly Triggered Incident (Mar 27):**
*   **Trigger:** March 27, 2026, at 13:16 UTC.
*   **Story Key:** `f5d0894a-4a42-515d-985f-d06644833529`.
*   **Status:** **Active / Triggered**.
*   **Error Message:** "Datadog is unable to process your request."

### Pending Actions & Ownership
*   **Immediate Action:** A new P3 incident triggered on Mar 27. As the error message "Datadog is unable to process your request" persists, manual intervention via the Datadog UI is required if the alert does not self-clear within standard variance. The current duration has just begun; no escalation decision can be finalized yet.
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Investigation Note:** The persistent system error suggests potential pipeline degradation or Datadog processing issues, similar to historical trends. Continued trend analysis is warranted pending the resolution of this Mar 27 event.

### Decisions Made
*   **Status:** No escalation triggered yet for the Mar 27 incident as it is currently in the "Triggered" state.
*   **Protocol:** Continue active surveillance. If a new trigger occurs with similar error messaging and resolution time exceeds 6 hours, escalate immediately to SRE/Platform Engineering.

### Key Dates & Follow-ups
*   **Latest Event:** March 27, 2026, at 13:16 UTC (Triggered).
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Monitor for recurrence or resolution. The extended duration of the Mar 25 incident (~24h) remains a significant outlier requiring trend analysis.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Datadog Monitor Link:** [View in Datadog](https://app.datadoghq.eu/monitors/17447511)
*   **Latest Incident (Mar 27):** https://app.datadoghq.eu/monitors/17447511?group=story_key%3Af5d0894a-4a42-515d-985f-d06644833529

### Monitor Configuration
*   **Query:** `events("source:watchdog (story_category:infrastructure -story_type:(tcp_retrans_jump OR full_disk_forecast)) env:(PROD OR production OR prod)").rollup("count").by("story_key").last("30m") > 0`


## [4/30] #dpd-dba
Source: gchat | Group: space/AAAAMh7T8Y0 | Messages: 7 | Last Activity: 2026-03-27T12:55:22.022000+00:00 | Last Updated: 2026-03-27T14:35:13.606526+00:00
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


## [5/30] [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Messages: 7 | Last Activity: 2026-03-27T11:29:59.041000+00:00 | Last Updated: 2026-03-27T14:35:43.145971+00:00
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


## [6/30] RMN Incidents
Source: gchat | Group: space/AAQAz11ATzY/f96GZlnokS4 | Messages: 5 | Last Activity: 2026-03-27T11:29:15.744000+00:00 | Last Updated: 2026-03-27T14:35:57.366604+00:00
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


## [7/30] RMN Incidents
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


## [8/30] Team Starship
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


## [9/30] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Last Activity: 2026-03-27T09:11:50.345000+00:00 | Last Updated: 2026-03-27T10:42:18.378363+00:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
Production instability in Mirakl integration continues into **March 27**. While late-night cycles on March 26/27 previously showed ~5-minute durations, a new P2 incident cluster occurred on the morning of March 27 affecting `fni-order-create`, involving both "Exception Occurred At Mirakl Route" and "Error while calling API". Concurrently, `picklist-pregenerator` latency cycles remain critical.

**Incident Summary & Timeline**
*   **Service: `fni-order-create` (Mirakl Integration) – Morning Cluster (Mar 27)**
    *   **Trigger Window:** Simultaneous P2 triggers at **09:06 UTC** on March 27.
        *   "Exception Occurred At Mirakl Route" triggered at **09:06:39 UTC** (Monitor ID `17447918`).
        *   "Error while calling API" triggered at **09:06:49 UTC** (Monitor ID `17447928`).
    *   **Recovery:** Monitors returned to normal by **09:11 UTC**. Duration: ~5 minutes.

*   **Service: `fni-offer` (Mirakl Integration) – Historical Context**
    *   Instability persists from March 17–26, including the new "FairPrice Route" failure at **15:14 UTC** on March 26 and late-night clusters on Mar 26/27.

*   **Service: `seller` (`picklist-pregenerator`) – Recurring Latency**
    *   Critical latency cycles continue, peaking at **3603.203s** on March 26 (23:01 UTC) following peaks of **3657.213s** on March 25 and **3607.798s** on March 24.

*   **Service: `fpon-seller-mirakl-order-creation-alert` (Sync Issues)**
    *   Fluctuating P3 alerts for unsynced orders occurred on March 26 between 17:36 and 18:06 UTC.

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of expanded Mirakl integration instability affecting `fni-order-create`. The pattern now includes a new morning cluster on **March 27 (09:06–09:11 UTC)**, extending the history from March 17 through early March 27.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Investigate root cause of extreme latency spikes in `picklist-pregenerator`. The cycle remains critical with values exceeding 3600s on March 25 and 26.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Review Monitor `29851723` logic for Apple Pay/Google Pay transactions following the March 23 test alert.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Summary for Leadership**
Mirakl integration instability has persisted across ten consecutive days (March 17–27). On **March 27**, a new morning cluster occurred at **09:06 UTC** affecting `fni-order-create`, triggering simultaneous "Exception Occurred At Mirakl Route" and "Error while calling API" alerts before recovering by **09:11 UTC**. This follows previous systemic failures on March 26, including a distinct "FairPrice Route" failure at 15:14 UTC lasting ~5 minutes and an afternoon cluster affecting `fni-order-create` for over an hour. Concurrently, `picklist-pregenerator` exhibits continuous critical latency spikes, reaching **3603.203s** on March 26. These recurring patterns in Mirakl routing and job processing require urgent engineering review to stabilize production performance.


## [10/30] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Last Activity: 2026-03-27T08:37:20.035000+00:00 | Last Updated: 2026-03-27T10:42:53.649881+00:00
**Daily Work Briefing: Nikhil Grover & Michael Bui**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator; managing deployment requests and incident coordination. Verifying prod visibility in "Omni Home" and confirming `pcnt` parameters for Search/Category pages to prevent regression.
*   **Michael Bui:** Technical Lead (Engineering); deployed to PRD. Confirmed `pageType: OMNI_HOMEPAGE` in logs but noted no changes were made to include `swimlane` or `page_name` parameters yet. Verified no changes to `pcnt` for Search/Category pages.
*   **Flora:** Frontend resource; previously raised analytics payload concerns. Confirmed backend control for swim lanes historically resided with Yang Yu.

**Main Topics**
1.  **Post-Deployment Visibility & Parameter Gaps (Omni Home):**
    *   While the core ranking fix was deployed to PRD on March 25, visibility issues persist in "Omni Home." Nikhil observed only one ad in vertical scroll; Michael confirmed he has never seen ads there.
    *   **Log Analysis:** Michael verified logs for Customer UID `163692623655477837` show `pageType: OMNI_HOMEPAGE`. However, Nikhil noted the absence of the `page_name` parameter in the Osmos request and that the `swimlane name` was not included.
    *   **Code Status:** Michael confirmed no changes were made to include swim lane names or the `page_name` param yet.
    *   **Action:** Nikhil provided a sample Osmos URL (referencing Daryl's DPD-814 comment) for investigation; focus shifted to ensuring backend requests include both `swimlane` and `page_name`.

2.  **Incident Tracking Initiation:**
    *   On March 27 at 08:36 UTC, Michael Bui requested confirmation on whether an OSMOS support ticket had been created for the raised incident regarding missing parameters.
    *   Nikhil Grover confirmed no ticket existed and initiated the creation of the OSMOS support ticket immediately following this exchange.

3.  **Resource Constraints & Timeline Conflict:**
    *   **Impressions Delivery:** Nikhil requested starting tickets on March 26, but Michael declined due to travel preparations and a strict leave block starting April 6th.
    *   **Project Light Conflict:** The week of April 6th is "unprecedentedly tight" for Project Light. Michael estimates focusing until April 12th (UAT April 13–14, deploy April 15).
    *   **Timeline Clash:** Nikhil requires deployment by **April 9th**. He flagged that waiting until mid-April is not feasible as he can only manage a 1–2 day delay.

4.  **Regression Prevention (Search & Category Pages):**
    *   On March 27, Nikhil requested verification that `pcnt` settings for Search and Category pages remained at **6** following the Homepage changes.
    *   Michael confirmed he did not alter `pcnt` for these pages on his end and that Osmos receives parameters directly from their side, ensuring no side effects from homepage adjustments. Nikhil insisted on explicit confirmation to avoid potential incidents regarding regression.

**Decisions Made & Status Updates**
*   **Deployment Readiness:** PRD deployment is confirmed, but ads remain invisible in "Omni Home" pending backend parameter updates (`swimlane`, `page_name`) and swim lane activation.
*   **Incident Management:** An OSMOS support ticket has been initiated by Nikhil Grover to track the visibility incident (timestamped March 27).
*   **Regression Safety:** Confirmed on March 27 that `pcnt` for Search and Category pages remains at **6** with no side effects from the homepage deployment.
*   **Capacity Planning:** Michael Bui cannot start impressions tickets immediately due to Project Light constraints (April 6–12). A delivery window before April 9th is currently at risk.

**Pending Actions & Owners**
*   **OSMOS Ticket Creation (Nikhil Grover):** Complete the support ticket for the raised incident regarding missing parameters in Osmos requests.
*   **Parameter Implementation (Michael Bui):** Investigate why `page_name` is missing and implement changes to pass both `swimlane` and `page_name` to Osmos.
*   **Swim Lane Activation (Nikhil Grover/Team):** Continue coordinating with Yang Yu or third parties to enable remaining swim lanes in PRD for Omni Home.
*   **Impressions Delivery Scheduling (Nikhil Grover/Michael Bui):** Urgent negotiation required to find a delivery window before April 9th, despite Michael's unavailability until mid-April.

**Key Dates & Deadlines**
*   **March 26, 2026:** Verification of Omni Home ads; discovery of missing `page_name` and swim lane params in Osmos requests (UID: `163692623655477837`).
*   **March 27, 2026:** Confirmation that Search/Category `pcnt` remains at 6; initiation of OSMOS support ticket.
*   **April 9, 2026:** Critical deadline for delivery raised by Nikhil Grover.
*   **April 6–12, 2026:** Michael Bui's anticipated leave/travel and Project Light focus period.

**Historical Context Note**
While the initial focus was on resolving the March 25 ranking anomaly (confirmed fixed), the conversation pivoted to immediate post-deployment validation in "Omni Home." Despite successful PRD deployment, ads remain invisible due to missing backend parameters (`page_name`, `swimlane`) and potential swim lane configuration issues. On March 27 at 08:36 UTC, Michael Bui queried regarding incident tracking, prompting Nikhil Grover to initiate an OSMOS support ticket immediately. Simultaneously, a critical resource conflict emerged: Nikhil requires delivery by April 9th, but Michael is unavailable due to Project Light and travel until at least mid-April, creating a significant scheduling risk for upcoming impressions delivery tickets. On March 27, both parties confirmed the stability of Search/Category `pcnt` settings (6) following the homepage update.


## [11/30] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Last Activity: 2026-03-27T08:29:12.018000+00:00 | Last Updated: 2026-03-27T10:43:36.641675+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Mar 27, 08:30 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-discovery`, `@opsgenie-dpd-grocery-retail-media`.
*   **Escalations:** `@hangouts-GT-Search-DatadogAlerts`, `@oncall-dpd-staff-excellence-pdm`, `@hangouts-GT-Discovery-DatadogAlerts`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Search Indexing.

**Main Topic**
**P2 ALERT (High Error Rate):** The `marketing-service` experienced a high error rate in production on Mar 27. Concurrently, the `go-catalogue-service` exhibited recurring latency instability (`get_/category/_id` endpoint) and flapped again following a stable period on Mar 25.

**Pending Actions & Ownership**
*   **Action:** **RESOLVE HIGH ERROR RATE (`marketing-service`):** Address P2 error rate > 5% on `env:prod`.
    *   **Owner:** Retail Media Team (`@opsgenie-dpd-grocery-retail-media`).
    *   **Status:** **RECOVERED (08:29 UTC Mar 27).** Triggered at 08:19 UTC with a metric value of 0.01 (5% threshold exceeded); resolved by 08:29 UTC dropping to 0.0. Monitor ID: `17447106`.
    *   **Required Checks:** Review Datadog traces, inspect K8s deployment (`fpon-cluster/default/marketing-service`), and consult Runbook.
*   **Action:** **RESOLVE LATENCY FLAPPING (`go-catalogue-service`):** Address P90 latency spikes > 2000ms for `get_/category/_id`.
    *   **Owner:** Discovery Team (`@hangouts-GT-Discovery-DatadogAlerts`) & Product Data Management (`@opsgenie-dpd-staff-excellence-pdm`).
    *   **Status:** **RECOVERED (05:50 UTC Mar 27).** Triggered at 05:18 UTC with a p90 of 2.738s; resolved by 05:50 UTC dropping to 0.542s. Monitor ID: `17447967`.
    *   **Required Checks:** Review Datadog logs, inspect K8s deployment (`fpon-cluster/default/go-catalogue-service`), and consult Runbook.
*   **Action:** **RESOLVE ERROR RATE ANOMALY (`sku-global-attribute`):** Address P3 error rate > 0.1% in SKU Global attribute Job processing.
    *   **Owner:** Product Data Management (`@oncall-dpd-staff-excellence-pdm`) & Discovery Team (`@opsgenie-dpd-grocery-discovery`).
    *   **Status:** **RECOVERED (04:56 UTC Mar 27).** Triggered at 04:02 UTC with a metric value of 100.0%; resolved by 04:56 UTC dropping to 0.0%. Monitor ID: `91573503`.
    *   **Required Checks:** Review Datadog logs for `fpon-catalogue-job-sku-global-attribute`.
*   **Action:** **RESOLVE LATENCY FLAPPING (`get_/product`):** Address P90 latency spikes > 150ms.
    *   **Owner:** Discovery Team & Product Data Management.
    *   **Status:** Previously recovered at 19:27 UTC on Mar 25 (p90: 129ms). Monitor ID: `17447976`. No new activity reported in current cycle.
*   **Action:** **PERSISTENT INVESTIGATION:** Address critical errors on `fp-search-indexer` (env: prod).
    *   **Owner:** Product Data Management On-Call (`@oncall-dpd-staff-excellence-pdm`).
    *   **Status:** Active since Mar 18. Last re-triggered Mar 24, 16:29 UTC. No resolution achieved.

**Decisions Made**
*   The `marketing-service` triggered a P2 alert at 08:19 UTC (metric value: 0.01) and normalized by 08:29 UTC. This replaces the previous P4 throughput anomaly record for this service; no root cause analysis is required unless recurrence is observed.
*   The `sku-global-attribute` job critical processing failure at 04:02 UTC was resolved by 04:56 UTC.
*   Root cause analysis remains critical for the recurring `go-catalogue-service` monitor (ID: `17447967`) and the persistent `fp-search-indexer` failure since Mar 18.

**Key Dates & Follow-ups (Mar 16–27, 2026)**
*   **Service: `marketing-service` (P2 - Retail Media) [RESOLVED]**
    *   *Latest Timeline:* Triggered 08:19 UTC Mar 27 (error rate 0.01); Recovered 08:29 UTC. Monitor ID: `17447106`.
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/17447106) | [Runbook](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book).
*   **Service: `go-catalogue-service` (P3 - Discovery/Product Data) [FLAPPING]**
    *   *Latest Timeline:* Triggered 05:18 UTC Mar 27 (p90: 2.738s); Recovered 05:50 UTC. Monitor ID: `17447967`.
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/17447967) | [Runbook](https://ntuc.atlassian.net/wiki/spaces/DIS/pages/2646212686/Catalogue+Service).
*   **Service: `sku-global-attribute` (P3 - Product Data Management) [RESOLVED]**
    *   *Latest Timeline:* Triggered 04:02 UTC Mar 27; Recovered 04:56 UTC. Monitor ID: `91573503`.
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/91573503).
*   **Service: `fp-search-indexer` (P2 - Product Data Management) [ACTIVE CRITICAL]**
    *   *Latest Timeline:* Active since Mar 18; re-triggered Mar 24, 16:29 UTC.

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c


## [12/30] FPG Everyone - General
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


## [13/30] [Prod Support] Ecom FFS Ops
Source: gchat | Group: space/AAAAde_cYKA | Last Activity: 2026-03-27T07:53:37.579000+00:00 | Last Updated: 2026-03-27T10:47:31.668760+00:00
**Daily Work Briefing: [Prod Support] Ecom FFS Ops (Updated Mar 27)**

**Key Participants & Roles**
*   **Wai Ching Chan / Sampada Shukla:** Operations/Product Leads.
*   **TL HCBP FFS:** Store Lead reporting T18/T19 picking queue blockages.
*   **Adrian Yap Chye Soon:** Technical Lead/Support (investigating data anomalies).
*   **Akash Gupta:** DPD / Fulfilment / On Call (Source of new alerts and escalation point).
*   **Yoongyoong Tan:** Reporting specific HCBP picking Q issues.
*   **Ler Whye Ling Angel:** Urgent escalation for HCBP "No picking Q."

**Main Topics**
1.  **Packlist Discrepancies & Validation:** Ongoing investigation into critical `packed_qty` anomalies (NULL values or massive mismatches vs. `delivered_qty`).
    *   **Critical Incident (Mar 26):** Akash Gupta identified two orders at **VivoCity (Store ID 170)** showing `packed_qty` > 13M against `delivered_qty` of <20.
        *   Order #22912255: `packed_qty` 13,165,999 vs. `delivered_qty` 12.
        *   Order #22906879: `packed_qty` 13,165,999 vs. `delivered_qty` 18.
    *   **Historical Context:** Incidents remain active references, including Mar 25 Sun Plaza (Order #22898981) and prior anomalies at Hyper Sports Hub and VivoCity.

2.  **HCBP Picking Queue Issues (Mar 27):** Escalated urgency regarding "No picking Q" blockage and T18 display failures.
    *   **Timeline & Escalation:**
        *   **02:08 AM:** TL HCBP FFS reported the initial blockage.
        *   **02:14 AM:** Yoongyoong Tan requested status check on HCBP picking queue.
        *   **02:52 AM:** Ler Whye Ling Angel escalated "No picking Q" with urgency ("please assist asap"), tagging @Akash Gupta and @Gopalakrishna Dhulipati.
        *   **07:47 AM (New):** TL HCBP FFS requested immediate checks regarding T18 not showing data in the chat.
        *   **07:53 AM (New):** TL HCBP FFS followed up asking, "anyone looking into it?" regarding the T18 issue.

**Pending Actions & Ownership**
*   **Critical Data Validation (Mar 26):**
    *   *@Yap Chye Soon Adrian:* Confirm massive `packed_qty` mismatches for Orders #22912255 and #22906879 at VivoCity.
    *   *@Akash Gupta:* Continue monitoring DPD/Fulfilment alerts; Sun Plaza validation remains pending.
*   **HCBP Queue Investigation (Urgent - Mar 27):**
    *   *@Adrian Yap Chye Soon / On Call Team / @Gopalakrishna Dhulipati:* Immediately investigate the "No picking Q" status and T18 display failure for HCBP following escalated pings from Ler Whye Ling Angel and TL HCBP FFS.
    *   *Context:* While the Mar 25 incident is resolved, the new Mar 27 instance (T18 not showing) requires immediate intervention per the latest chat activity at 07:47 AM and 07:53 AM.

**Decisions Made**
*   **App Release Strategy:** Picker App 10.4.0 rollout remains on hold pending resolution of critical data anomalies (Mar 18–27). Full rollout is contingent on stability post-fixes, specifically addressing the Mar 26 VivoCity alerts and the urgent Mar 27 HCBP queue/T18 failures.

**Key Dates & Deadlines**
*   **Immediate:** Validation of Mar 26 Orders #22912255/#22906879; Root cause analysis of Mar 27 HCBP "No picking Q" and T18 display issues (Escalated by Ler Whye Ling Angel and TL HCBP FFS).
*   **Pending:** RCA for recent `packed_qty` anomalies across Sports Hub, VivoCity, Parkway, Changi, Sun Plaza, Hyper VivoCity.

**Critical Alerts**
*   **Active Alert (Mar 27):** T18 not showing data reported by TL HCBP FFS at 07:47 AM; follow-up ping sent at 07:53 AM. Urgent technical check required for @Akash Gupta and @Gopalakrishna Dhulipati.
*   **Secondary Active Alert (Mar 27, 02:52 AM):** HCBP "No picking Q" issue escalated by Ler Whye Ling Angel; urgent technical check required.
*   **New Alert (Mar 26):** Two orders at VivoCity (Store ID 170) showing `packed_qty` (~13M) >> `delivered_qty`. Orders #22912255 and #22906879 require confirmation.


## [14/30] [Internal] (Ecom/Omni) Digital Product Development
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


## [15/30] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Last Activity: 2026-03-27T07:42:47.450000+00:00 | Last Updated: 2026-03-27T10:48:58.701639+00:00
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
2.  **iOS Address Emoji Blocking Bug:** Wai Ching Chan reported on Mar 26 that customer addresses with emojis on iOS cause order time slot failures, requiring manual resolution (Customer ID: 2022036). Validation logic is required during address add/edit.
3.  **Website SDK Deployment (Strudel):** Lester deployed `go-platform-website` on Mar 19 to update the Strudel SDK for maximum voucher validation. Review via Bitbucket diff between v1.5.11 and v1.5.10 completed.
4.  **Pre-order Payment Logic & UAT:** Zaw initiated an inquiry on Mar 24 regarding pre-order flows (app payment vs. POS redemption) and requested peer review for the offline pre-order admin page (`https://admin-uat.fairprice.com.sg/in-store-preorder/offline`).
5.  **Slot Date Discrepancy:** Shiva reported a delivery slot mismatch (UI shows 25th, API indicates 23rd). Daryl Ng and Sundy Yaputra are resolving this.
6.  **UAT Stock Requirements:** Sneha requested high-stock SKUs for Zi Ying's bulk order testing; Wai Ching Chan and Akash Gupta tasked to check IMS availability.
7.  **Order Verification Bug (NED-278216):** Investigation continues into the Whitelisting API returning older contract data (identified by Andin).
8.  **BCRS Deposit & SAP Integration:** Critical duplicate deposit posting fix remains active (PR #6). Marketplace tickets planned for release in sync with SAP deployment.

**Pending Actions & Ownership**
*   **Akash Gupta, Michael Bui, Andin Eswarlal Rajesh:** Provide immediate inputs on the status of BCRS tickets **DPD-637** and **DPD-807** to facilitate epic closure (Sneha Parab).
*   **Wai Ching Chan, Gopalakrishna Dhulipati, Dang Hung Cuong:** Validate and implement emoji blocking logic for iOS address entry/editing to prevent order slot failures. Reference Customer ID: 2022036.
*   **Zaw Myo Htet:** Clarify pre-order payment redemption logic; execute UAT testing on offboarded Pinelabs split feature flag.
*   **Lester Santiago Soriano:** Assist with Whitelisting API contract issue (cc: Piraba Nagkeeran, Jonathan Tanudjaja). Deployment completed Mar 19.
*   **Daryl Ng & Sundy Yaputra:** Resolve delivery slot date mismatch (UI showing 25th vs API 23rd).
*   **All Engineers:** Mark all tickets deployed to production as "Status = Done." Highlight any pending deployments immediately (Sneha Parab).

**Decisions Made**
*   **BCRS Epic Priority:** Immediate action required to close the BCRS epic; ticket status must be verified for DPD-637 and DPD-807.
*   **Status Protocol:** All engineers must update Jira ticket status to "Done" upon production deployment; pending items must be flagged in the chat thread.
*   **Deployment Approval:** PLU processor deployment approved pending UD alignment.
*   **Code Review Priority:** Focus shifted to `go-platform-website` PR #1538 for the Strudel SDK update, superseding previous layout-service priorities. Current focus includes reviewing the new offline pre-order admin page and addressing iOS emoji validation.

**Key Dates & Deadlines**
*   **Mar 27, 2026 (Today):** Sneha Parab initiated inquiry on BCRS epic closure; responses required from Akash Gupta, Michael Bui, and Andin Eswarlal Rajesh.
*   **Mar 19, 2026:** Website deployment completed at 4:00 PM; UAT stock sourcing required immediately.
*   **Mar 24, 2026:** Zaw Myo Htet initiated inquiry regarding the offline pre-order admin page and pre-order payment logic.
*   **Mar 31, 2026:** Sports Hub FFS store closure deadline.

**Note on Historical Context:** Previous mentions of code review priorities for `layout-service` PR #362 and `website-service` PR #649 are superseded by the urgent Strudel SDK deployment update. The focus has now shifted to resolving slot date mismatches, pre-order payment logic queries, the newly flagged iOS address emoji blocking issue, and the critical requirement to close the BCRS epic by clarifying the status of tickets DPD-637 and DPD-807.


## [16/30] QE <-> All Tribes
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


## [17/30] SRE / Network / DBA / DevOps / Infra
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


## [18/30] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/gZNwhpEiEY4 | Last Activity: 2026-03-27T07:29:54.158000+00:00 | Last Updated: 2026-03-27T10:50:30.069664+00:00
**Daily Work Briefing: Digital Product Development (Leads)**
**Resource:** [Leads] (Ecom/Omni) Digital Product Development
**Date of Discussion:** March 26, 2026 (Updated with follow-up on March 27)

### **Key Participants & Roles**
*   **Daryl Ng:** Project Lead/Manager; coordinating timelines, risk mitigation, and resource allocation.
*   **Michael Bui:** Developer responsible for the BCRS deposit posting job; managing specs, unit tests, and SIT delivery.
*   **Sundy:** Development resource assigned to assist Michael Bui with PRD tasks (arranged by Daryl).
*   **Onkar:** Deployment engineer scheduled to deploy other services at midnight.
*   **Wai Ching:** Created the necessary order custom field during UAT today.
*   **Adrian:** Developer currently restricted from redelivery work between April 1–7 due to duplicate posting risks.
*   **Sneha Parab:** Validated discussion relevance against ticket DPD-807 on March 27, 2026.

### **Main Topic**
Discussion focused on mitigating delivery risks for the BCRS deposit posting job changes. The team addressed potential delays in SIT (System Integration Testing) and duplicate postings if Adrian continues redeliveries between April 1–7. Michael expressed frustration regarding late UAT sign-offs but confirmed that comprehensive documentation and unit tests are available to facilitate Knowledge Transfer (KT) if needed. **Sneha Parab queried the link between this discussion and ticket DPD-807 on March 27.**

### **Decisions Made**
1.  **Immediate Deployment:** Daryl approved the deployment of all currently ready changes, including the BCRS deposit posting job, scheduled for tonight at 10:00 PM or midnight.
2.  **Resource Allocation:** Sundy has been assigned to assist Michael Bui with specific PRD tasks (creating order custom fields and pipeline deployment).
3.  **Risk Mitigation:** The team agreed to proceed with available changes rather than waiting for a full KT, acknowledging that SIT could potentially be completed tomorrow if progress holds.

### **Pending Actions & Owners**
*   **Deploy BCRS Job:** Michael Bui to execute the Bitbucket pipeline deployment tonight (confirmed by Daryl).
    *   *Context:* Onkar is also deploying at midnight; coordination required to avoid conflicts or ensure sequencing.
*   **Create Order Custom Field:** Sundy to create the field that Wai Ching defined in UAT today.
*   **Pipeline Deployment Assistance:** Sundy to update on PRD pipeline deployment requirements after receiving instructions from Michael Bui.
*   **SIT Status Update:** Michael Bui to provide a status update by tomorrow End of Day (EOD) confirming if SIT is complete or if further actions are required.

### **Key Dates & Deadlines**
*   **March 26, 2026:** Deployment scheduled for tonight (10:00 PM / Midnight).
*   **March 27, 2026:** Sneha Parab verified relevance to ticket DPD-807.
*   **Tomorrow (EOD):** Deadline for Michael Bui to report SIT completion status.
*   **April 1 – April 7, 2026:** Critical window where Adrian must refrain from redelivery to prevent duplicate postings; SIT is targeted to conclude before this period begins.

**Reference Links:**
*   **Ticket:** https://ntuclink.atlassian.net/browse/DPD-807
*   Specs Repository: https://bitbucket.org/ntuclink/bcrs-deposit-posting/src/main/openspec/specs/


## [19/30] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Last Activity: 2026-03-27T07:24:23.785000+00:00 | Last Updated: 2026-03-27T10:51:04.514692+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Sneha Parab:** Lead/Manager; coordinating cross-team support, SAP/API integration blockers, and epic lifecycle management.
*   **Michael Bui:** Engineering/RMN Architect; managing architecture updates, infrastructure compliance, investigating search performance drops, and assessing SIT timelines.
*   **Alvin Choo:** Leadership; addressing feedback loops, release schedules, AI personalization prioritization, and traffic anomalies.
*   **Daryl Ng:** Investigating store network ownership, Omni Home data discrepancies, and SIT delivery timelines for redelivery changes (currently away).
*   **Others Active:** Andin Eswarlal Rajesh, Olivia, Koklin, Zaw, Ravi.

**Main Topics & Updates**
1.  **Epic Lifecycle Query (DPD-710):** Sneha Parab flagged that the Omni ticket for this epic shows a technical live date of March 19, 2026. With Daryl Ng away, she queried if the epic is safe to close immediately pending Michael Bui's input.
2.  **Critical Search Performance Drop:** Michael Bui flagged a severe decline in impressions (60–70%) on search/category pages since March 18/19. Investigation is ongoing to correlate with PRD deployments, potentially delaying the release indicated as live on March 19.
3.  **SIT Timeline & Redelivery Risk:** Daryl Ng queried the feasibility of SIT delivery before April 6/7 if Knowledge Transfer (KT) occurs. Michael Bui highlighted that between April 1–7, Adrian cannot perform redeliveries due to risks of duplicate postings without a completed handover.
4.  **Store Network Ownership Clarification:** Daryl Ng queried on March 26 regarding "store network" ownership under Data COE vs. Miguel's team. Investigation focus shifted for the `Omni Home` store ID mismatch (OMNI-1157 related).
5.  **SAP/Deposit SKU Integration Blocker:** Marketplace lacks deposit data for SAP API integration. Olivia rejected new technical solutions following poor PM communication regarding manual UD attempts. Immediate action required from the SAP team.
6.  **Requirement Clarity (BCRS):** Michael Bui flagged that "follow existing ones" is unacceptable acceptance criteria for BCRS deposit posting. Explicit UAT scenarios are required for Definition of Ready (DoR).
7.  **Infrastructure Compliance:** Bitnami ending free Docker images impacts `sonic_raptor` and `mkp-fairnex`. Migration is mandatory.
8.  **1HD Changes & Production Testing:** Andin Eswarlal Rajesh confirmed production testing with leadership is targeted for Friday or Monday, though the search drop investigation (and potential release hold) may impact this timeline.

**Pending Actions & Owners**
*   **Epic Closure Validation:** Determine if DPD-710 can be closed given the March 19 live date discrepancy and Daryl's absence. (Owner: Michael Bui; Requestor: Sneha Parab)
*   **Search Performance Investigation:** Identify root cause of impression drop since Mar 18/19; correlate with PRD deployments. (Owners: Michael Bui, Daryl Ng, Andin Eswarlal Rajesh, Alvin Choo)
*   **SIT Delivery Assessment:** Determine if KT allows SIT completion before April 6/7 to avoid duplicate posting risks during Adrian's unavailability (Apr 1–7). (Owner: Michael Bui/Daryl Ng)
*   **Store Network Ownership:** Confirm if store network is under Data COE or Miguel's team. (Owner: Daryl Ng/Michael Bui)
*   **SAP Timeline Resolution:** Push SAP team to explore deposit SKU data solutions. (Owner: Sneha Parab/Alvin Choo/Gopalakrishna Dhulipati)
*   **OMNI-1157 Clarification:** Confirm scope applies only to the new app and clarify Data COE ownership. (Owners: Alvin Choo/Gopalakrishna Dhulipati/Daryl Ng)
*   **BCRS Requirements:** Define explicit UAT scenarios with Koklin. (Owner: Alvin Choo/Gopalakrishna Dhulipati)
*   **Infrastructure Migration:** Address Bitnami Docker image end-of-life. (Owner: Engineering Team/Michael Bui)
*   **RAW Forms Review:** Review Risk Register for DPD RAW forms; confirm handovers and renew expired forms. Deadline: Tomorrow EOD. (Owner: All Leads/Sazali Bin Mohammed Ali's team)
*   **Scan@Door AI Prioritization:** Determine prioritization status on Omni board. (Owner: Daryl Ng/Alvin Choo)
*   **1HD Release Verification:** Confirm release status prior to production testing. (Owner: All Leads/Daryl Ng)

**Decisions Made**
*   **RMN Architecture:** Michael Bui updated current, future, and transition architecture diagrams.
*   **Townhall Coordination:** Team to meet Hui Hui post-townhall; no full Q&A scheduled.
*   **Release Status:** Questions remain regarding holding today's regular app release pending the search performance investigation and clarification on DPD-710 closure.

**Key Dates & Deadlines**
*   **DPD-710 Live Date:** March 19, 2026 (Subject to validation).
*   **RAW Forms Review:** Due Tomorrow EOD.
*   **Townhall Meeting:** Today post-townhall session.
*   **Adrian Redelivery Block:** Adrian unavailable for redelivery Apr 1–7 due to duplicate posting risks.
*   **SIT Target:** Potential delivery by April 6/7 contingent on KT success.
*   **Chee Hoe Support:** Effective end of March for Product Catalogue/MarTech scope.
*   **1HD Production Testing:** Targeted for this Friday or Monday.


## [20/30] Digital Product Development {DPD}
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


## [21/30] [Prod Support] Offers
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


## [22/30] Progress Check: Monitor & On-Call Team Alignment - Mar 27
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


## [23/30] DPD Incidents
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


## [24/30] Retail out of home (Digital Screens & CMS)
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


## [25/30] [Virtual] Smart Cart x RMN Catchup - Mar 27
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


## [26/30] RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Last Activity: 2026-03-27T03:20:59.446000+00:00 | Last Updated: 2026-03-27T06:44:37.636413+00:00
**Daily Work Briefing: Automated Test Results Summary (RMN Notification)**

**Key Participants & Roles**
*   **Collection Runner App:** Automated testing agent executing API suites.
*   **Webhook Bot:** Reporting mechanism; consistently returning "unable to process your request" on all notifications through March 27, 2026.
*   **Parties Involved:** System-generated notification log only.

**Main Topic/Discussion**
Automated nightly API test executions across `promo-service`, `marketing-personalization-service`, and `marketing-service` in the **staging** environment. Monitoring period spans March 12 through **March 27, 2026**. Execution windows occur at approximately 01:05 UTC (morning), 02:30/02:31 UTC (midnight), and **03:20/03:21 UTC** (early morning).

**Test Execution Status & Anomalies**
*   **`marketing-personalization-service` Update:** New logs confirm a stable run at **03:20 UTC on March 27**.
    *   **API Contract Tests:** 125 Passed / 0 Failed / 0 Skipped (Total Requests: 21).
    *   **API Tests:** 96 Passed / 0 Failed / 0 Skipped (Total Requests: 21).
*   **`promo-service`:** Confirmed stable on March 26 (02:31 UTC) and **March 27 at 02:30 UTC**. The latest run on March 27 showed **10 API Passed / 0 Failed** and **6 Contract Tests Passed / 0 Failed**.
*   **`marketing-service` Stability Confirmation:**
    *   **Historical Context:** Recurring instability persisted from March 17 through early March 25 (characterized by exactly 2 failed API tests). A temporary stabilization occurred on March 25; the morning failure streak was broken on March 26.
    *   **Current Status (March 27):** The streak of resolution continues. At **01:05 UTC** on **March 27**, `marketing-service` executed successfully with **53 API Tests Passed / 0 Failed** and **20 Contract Tests Passed / 0 Failed**.
    *   **Total Requests:** March 27 run recorded 17 total API requests and 16 contract test requests, all passing.

**Pending Actions & Ownership**
*   **Webhook Bot Remediation (High Priority):** The bot failed to process requests in every notification cycle from March 12 through the latest log on **March 27 at 03:21 UTC**. Immediate attention is required from DevOps or Automation Infrastructure.
*   **Verify `marketing-service` Stability:** Engineering must continue monitoring subsequent runs to confirm the resolution of early-morning flakiness observed between March 17–25 was permanent.

**Decisions Made**
*   No human decisions recorded; all entries are automated system outputs.

**Key Dates & Deadlines**
*   **Failure Window (Historical):** Instability noted on March 12, 13, and persistently from **March 17 through March 25**.
*   **Current Status:** Successful runs observed on March 26 and **March 27**.
    *   `marketing-service`: Passed at 01:05 UTC (March 26 & 27).
    *   `promo-service`: Passed at 02:30/02:31 UTC (March 26 & 27).
    *   `marketing-personalization-service`: Passed at 03:20 UTC (March 27).
*   **Monitoring Period:** Data covers runs from **March 12, 2026**, through **March 27, 2026**.

**Resource Info**
*   **Message Count:** 150 notifications logged in the space.
*   **URL:** https://chat.google.com/space/AAQA85dw4So


## [27/30] DPD All Leads
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


## [28/30] DPD Incidents
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


## [29/30] DPD x DPM
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


## [30/30] BCRS Firefighting Group
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
