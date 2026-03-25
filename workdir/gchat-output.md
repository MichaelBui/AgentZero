

## [1/32] [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Messages: 2 | Last Activity: 2026-03-25T02:38:01.608000+00:00 | Last Updated: 2026-03-25T02:49:31.057756+00:00
**Daily Work Briefing: [Prod Support] Marketplace**

**Key Participants & Roles**
*   **Support/Operations:** Willie Tan, Iris Chang, Lalita Phichagonakasit, Charlene Tan, Jie Yi Tan, Ayton See, Amos Lam, Michelle Lim.
*   **Technical/Admin Team:** Dang Hung Cuong, Shiva Kumar Yalagunda Bas (Frequent recipients of access/access issues), Olivia -, Jill Ong, Greta Lee, Zaw Myo Htet, Angella Yeo, Cassandra Thoi, Gopalakrishna Dhulipati.

**Main Topics & Discussion Summary**
The conversation covers critical operational blockers regarding seller onboarding, order fulfillment discrepancies, system configuration errors, urgent promotion removal requests, and new order inquiries. New discussions include email notification failures and order status synchronization issues. Major themes include:

1.  **User Access & Notifications:**
    *   **Email Failure:** Michelle Lim (Mar 23) reported a seller/user did not receive Mirakl invitation emails for the "Frutrip Official Store," even after checking spam folders. The team needs to determine how to resend the invite to create a new user.
2.  **Order Status Discrepancies:** Cassandra Thoi (Mar 25) requested checks on two orders with conflicting statuses:
    *   Order #256055476: DBP shows "Completed," but Mirakl shows "Cancelled."
    *   Order #248407866: Cancelled by API.
3.  **Access Management:** Requests to grant "PickerApp" access for new/existing sellers (Meat Affair, Old Shanghai, BulkMartGo, PETS STATION HOLDING). Charlene Tan reported a new seller (Woah Group) encountering errors under the "Offers" section.
4.  **Sales Data & Reporting:** Issues with vendors (CoLab Apac, Old Shanghai) not receiving sales breakdown reports since inception.
5.  **Promotion & Pricing Conflicts:**
    *   **Urgent Removal Request:** Lalita Phichagonakasit (Mar 20) reported an incorrectly set up promotion for **Item ID: 90244361** requiring immediate removal to prevent financial loss.
    *   Conflicting promotions for "Falcon Galaxy Strong Garbage Bag" require one to be disabled.
    *   Discount prices not showing despite SKU publication.
6.  **Fulfillment & System Errors:**
    *   Delivery slot display discrepancy for seller "Funa Artistic Hampers & Gifts" (Mar 19): Mirakl shows 91h vs Frontend date; focus remains on a window duration issue showing 4 days instead of the expected 2 days.
    *   Missing items in PickerApp compared to email picklists (Atasco Dairy, Estalife).
    *   Orders completed without delivery by NJV (Order #246974265, #248270820).
    *   Seller description/image updates not triggering "Pending Verification" status.
7.  **New Listing & Logic Queries:**
    *   **Item Visibility:** Lalita Phichagonakasit reported SKU **13226899** failing to appear under postal code **762115** since March 14th.
    *   **Picklist Logic (New):** Amos Lam (Mar 21) raised a critical issue where a vendor who opted out of public holidays in December did not receive a pick list today. This requires immediate investigation into why the system failed to generate a list for an opt-out status.
8.  **SAP Configuration Inquiry:** Iris Chang queried the definition and data source of "Lead Time" within SAP T-code ZMP_VENDOR on Mar 18.
9.  **Order Status Inquiry:** Angela Yeo (Mar 21) raised a query regarding FFS orders for seller **Yumsay Food**, seeking technical team advice.

**Pending Actions & Ownership**
*   **Urgent Promotion Removal:** Dang Hung Cuong and Gopalakrishna Dhulipati to immediately remove incorrectly set up promotion for Item ID: 90244361 (Lalita Phichagonakasit request, Mar 20).
*   **Picklist Generation Failure:** Technical team (Dang Hung Cuong, Shiva Kumar Yalagunda Bas) to investigate why a vendor who opted out of public holidays in December did not receive a pick list today (Amos Lam, Mar 21).
*   **FFS Order Inquiry:** Technical team to investigate FFS order status for seller "Yumsay Food" (Angela Yeo, Mar 21).
*   **Order Status Investigation:** Dang Hung Cuong, Shiva Kumar Yalagunda Bas, and Amos Lam to check discrepancies for Order #256055476 (DBP vs. Mirakl) and Order #248407866 (API cancellation) (Cassandra Thoi, Mar 25).
*   **Resend User Invitation:** Technical team to investigate how to resend the Mirakl invitation email for the "Frutrip Official Store" user who did not receive it (Michelle Lim, Mar 23).
*   **Close DF SOF Order:** Willie Tan requested closure; tracking via DST-2578 (Owners: Dang Hung Cuong, Shiva Kumar Yalagunda Bas).
*   **Vendor Report Issues:** Investigate missing sales breakdown reports for CoLab Apac (NED-277148) and Old Shanghai (NED-277329).
*   **Access Grants:** Grant PickerApp access to Meat Affair, BulkMartGo, PETS STATION HOLDING, and others. Resolve Woah Group "Offers" error (Charlene Tan).
*   **Fulfillment Investigation:** Check why Estalife missing Final Picklist PFC; investigate delivery slot display for Funa Artistic Hampers & Gifts (4 days vs. 2 days expected); determine trigger for NJV non-delivery completions.
*   **System Logic & Listing Fixes:** Investigate missing SKU 13226899 listing for postcode 762115; clarify picklist generation logic for postponed orders. Resolve SAP ZMP_VENDOR Lead Time definition (Dang Hung Cuong/Amos Lam).

**Decisions Made**
*   Dang Hung Cuong is prioritizing the removal of Item ID: 90244361, the new picklist failure issue raised by Amos Lam, and the Woah Group offers error. Dang Hung Cuong and Shiva Kumar Yalagunda Bas are assigned to investigate the vendor picklist anomaly. Ayton See previously educated a seller on promotion setup rules after identifying a configuration error.

**Key Dates & Deadlines**
*   **2026-03-25 (Today):** Cassandra Thoi requested checks on orders #256055476 and #248407866. Previous urgent request to remove Item ID: 90244361 remains active from Mar 20.
*   **2026-03-23:** Michelle Lim reported Mirakl email notification failure for Frutrip Official Store user.
*   **2026-03-21 (Yesterday):** Angela Yeo requested advice on FFS orders for "Yumsay Food"; Amos Lam reported vendor picklist failure due to public holiday opt-out status.
*   **2026-03-19:** Jie Yi Tan reported Funa Artistic Hampers & Gifts delivery window discrepancy; discussion ongoing with 34 replies.
*   **2026-03-18:** Iris Chang inquired about SAP T-code ZMP_VENDOR "Lead Time" definition.
*   **2026-03-03:** DF SOF order request raised.
*   **December 2025 (Historical Context):** Vendor involved in Amos Lam's query opted out of public holidays.


## [2/32] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/77DpGxXYs38 | Messages: 18 | Last Activity: 2026-03-25T02:37:37.553000+00:00 | Last Updated: 2026-03-25T02:49:50.132673+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Initiator; defines scope, timing, data requirements, and diagram formatting.
*   **Tiong Siong Tee:** Clarifies technical scope (Payment/FPPay) and presentation depth.
*   **Michael Bui:** Validates strategic purpose; drafts RMN flow diagrams; raises questions on long-term maintenance and B2B applicability.
*   **Hui Hui Voon:** Identified as the owner of the "D&T Scope for Project Light Workshop."

**Main Topic**
Preparation of presentation slides for the **Project Light Workshop**, focusing on:
1.  **Spotlight Topic 5: RMN** (Scheduled for today, March 25, 4:45 PM – 5:45 PM).
2.  **Spotlight Topic 2: Payment** (Scheduled for Thursday, March 26, 1:00 PM slot).

**Decisions Made & New Directives**
*   **Diagram Format:** Michael Bui's draft of basic RMN flows (initially a data flow diagram) must be converted to a **Sequence Diagram format** due to messy arrows in the previous version.
*   **Labeling Conventions:** The orchestrator service involved in these flows should be explicitly labeled as **"B2C backend"** and potentially applicable to **B2B** contexts.
*   **Scope Clarification (Ad Service):** Alvin Choo raised a critical "To-Be" state question regarding the **AD service**. It must be clarified if the team intends to maintain this service for non-Light usage (e.g., in-store screens) post-launch.
*   **Strategic Alignment:** Content is intended to enable CoMall to build solutions; however, Michael Bui questioned the future maintenance strategy: Will development contracts with CoMall continue after launch given RMN's expected high change frequency?

**Pending Actions & Ownership**
*   **Revise RMN Diagrams (Michael Bui):**
    *   Convert draft to **Sequence Diagram format**.
    *   Ensure arrows are clean and dependencies are clear.
    *   Label the orchestrator service as "B2C backend."
    *   Clarify the status of the AD service for non-Light scenarios.
*   **Clarify Future Maintenance (Michael Bui/Team):**
    *   Define the post-launch strategy regarding RMN changes and CoMall development contracts.
*   **Prepare Slides:**
    *   **RMN Slide:** Due prior to today's 4:45 PM slot.
    *   **Payment Slide:** Due prior to Thursday, March 26, at 1:00 PM.

**Key Dates & Deadlines**
*   **Today (March 25, 2026):**
    *   **Time:** 4:45 PM – 5:45 PM.
    *   **Event:** Spotlight Topic 5: RMN presentation.
*   **Thursday (March 26, 2026):**
    *   **Time:** 1:00 PM – 2:00 PM.
    *   **Event:** Spotlight Topic 2: Payment presentation.

**Resources Referenced**
*   Google Docs Presentation: `D&T Scope for Project Light Workshop`.


## [3/32] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Messages: 5 | Last Activity: 2026-03-25T02:36:22.439000+00:00 | Last Updated: 2026-03-25T02:50:21.370457+00:00
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
*   **Mar 24, 2026 (Old):** Incident `story_key`: `978f6328-424c-53dd-83c8-6411c3aa2158`. Triggered at 12:04 UTC. Status: **Resolved**.

**Recent Resolved Incidents:**
*   **Mar 24, 2026 (Afternoon):** Incident `story_key`: `d59141a3-b4b0-588d-a1c7-a7056988d5be`. Duration ~1h 51m. Status: **Resolved**.
*   **Mar 24–25, 2026:** Incident `story_key`: `de0cbb14-ade3-5de2-bfab-cbddd41da779`.
    *   **Triggered:** March 24, 2026, at 22:45 UTC.
    *   **Recovered:** March 25, 2026, at 02:36 UTC.
    *   **Duration:** ~3 hours 51 minutes.
    *   **Status:** **Resolved**.

### Pending Actions & Ownership
*   **Immediate Action:** The recurrence of the "Datadog is unable to process your request" error persists across multiple `story_keys` within a short window (Mar 24–25). While resolution times vary (~1.8h to ~3.9h), the systemic nature suggests ongoing issues with the Datadog ingestion/processing pipeline rather than isolated infrastructure faults.
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Investigation Note:** High frequency of triggers (Mar 24–25) requires continued scrutiny to distinguish between transient load spikes and persistent pipeline degradation.

### Decisions Made
*   No new escalations required yet; the latest incident resolved within standard historical averages (~3-5 hours). Continue monitoring for patterns where resolution time exceeds recent norms or fails to recover.

### Key Dates & Follow-ups
*   **Latest Event:** March 25, 2026, at 02:36 UTC (Recovered).
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Maintain active surveillance. If a new trigger occurs with similar error messaging and resolution time exceeds recent averages or if transient recovery fails, escalate to SRE/Platform Engineering.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Datadog Monitor Link:** [View in Datadog](https://app.datadoghq.eu/monitors/17447511)
*   **Latest Incident (Mar 24–25 Resolved):** https://app.datadoghq.eu/monitors/17447511?group=story_key%3Ade0cbb14-ade3-5de2-bfab-cbddd41da779&from_ts=1774405191000&to_ts=1774406391000&event_id=8558784591982850463

### Monitor Configuration
*   **Query:** `events("source:watchdog (story_category:infrastructure -story_type:(tcp_retrans_jump OR full_disk_forecast)) env:(PROD OR production OR prod)").rollup("count").by("story_key").last("30m") > 0`


## [4/32] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 16 | Last Activity: 2026-03-25T02:34:52.602000+00:00 | Last Updated: 2026-03-25T02:50:57.377883+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (Updated March 25, 02:34 UTC)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
Following the March 21 incident, volatility persists. After a critical surge in `gamification-api` on March 24 (UTC+8), activity shifted to **March 25 between 02:00 and 02:34 UTC**. The primary issue is now recurring high error rates in `engage-my-persona-api-go` (peaks ~0.1%) coupled with significant latency spikes in the MyInfo confirmation endpoint (`post_/new-myinfo/confirm`), reaching P99 of **2.656s**.

**Status Summary & Timeline (Extended Incident)**
*   **MyInfo Confirmation Latency (`post_/new-myinfo/confirm`):**
    *   Recurring spikes observed on March 25: P90 reached **2.656s** at **02:24 UTC** and P99 hit **2.656s** (Monitor #50879037). Metrics recovered by **02:31 UTC** (P99: 1.802s) and **02:34 UTC** (P90: 1.15s).
*   **Service Error Rates (`engage-my-persona-api-go`):**
    *   Recurring high error rate alarms (>0.1%) triggered multiple times between **02:00 and 02:30 UTC**. Peak values recorded at **02:00** (0.108%), **02:17** (0.102%), **02:19** (0.105%), and **02:26** (0.107%).
    *   Monitor #92965074 shows alternating Trigger/Recovered states throughout this window.
*   **Secondary Service Impact:**
    *   `frontend-gateway` (`orchid` requests) triggered latency alerts at **02:03**, **02:13**, and resolved by **02:24**.
    *   Manual signup success rate dropped below 99.9% at **02:03 UTC** (Monitor #93210650).

**Pending Actions & Ownership**
*   **Investigate MyInfo Latency:** Immediate RCA required for `post_/new-myinfo/confirm` P99 spike to **2.656s** at **02:24 UTC**. Owner: **Squad Dynamics**.
*   **Analyze Error Loops:** Investigate the persistent cycle in `engage-my-persona-api-go` (multiple triggers between 02:00–02:30) and its correlation with MyInfo latency. Owner: **Squad Dynamics**.
*   **Correlate Systemic Impact:** Determine if frontend gateway (`orchid`) issues are linked to the persona API errors. Owner: **Squad Journey/Dynamics**.

**Decisions Made**
*   **Severity Escalation:** Incident severity remains high due to the transition from isolated latency (March 24) to a complex loop involving both error rates and critical latency thresholds on March 25.
*   **Pattern Shift:** Activity has evolved into synchronized instability affecting `engage-my-persona-api-go` error handling, MyInfo response times, and downstream frontend recommendations simultaneously.

**Key Dates & Follow-ups**
*   **Active Window:** March 24–25 (UTC+8). Recent critical activity: **02:00 – 02:34 UTC** (March 25).
*   **Reference Links (New):**
    *   MyInfo P90 Monitor #50879027 (Peak: **2.656s @ 02:24**)
    *   MyInfo P99 Monitor #50879037 (Peak: **2.656s @ 02:24**)
    *   Engage Persona API Error Monitor #92965074 (Max Peak: **0.108% @ 02:00**)
    *   Frontend Gateway Orchid Monitor #17448311 (Peak: **99.883% success @ 02:13**)
    *   Manual Signup Success Monitor #93210650 (Triggered @ 02:03)


## [5/32] Release - FPG Back Office (Mon-Thurs)
Source: gchat | Group: space/AAAAoJgpZBM | Messages: 2 | Last Activity: 2026-03-25T02:33:49.818000+00:00 | Last Updated: 2026-03-25T02:51:23.397379+00:00
**Daily Work Briefing: FPG Back Office Releases**

**Key Participants & Roles**
*   **Rohit Pahuja:** Primary communicator; responsible for announcing scheduled releases and providing release note links.
*   **Jonathan Tanudjaja:** Confirmed as the executor for the v8.37.1 release.

**Main Topic**
The conversation focuses on confirmed software deployment schedules for the **Back Office** system, covering versions **v8.35.0**, **v8.36.0**, **v8.37.0**, and the newly announced urgent release of **v8.37.1**. These messages notify the team of upcoming maintenance windows aligned with the FPG Back Office (Mon-Thurs) resource schedule.

**Pending Actions & Ownership**
*   **Action:** Monitor the Back Office system during release execution for all scheduled versions.
    *   **Owner:** Team (implied by "Hi team" notifications).
*   **Action:** Review specific release notes for version updates and change logs.
    *   **Owner:** Team members referencing provided links.
*   **New Action:** Execute the deployment of version **v8.37.1** today.
    *   **Owner:** Jonathan Tanudjaja.

**Decisions Made**
No new strategic decisions were made; messages confirm four existing scheduled deployment plans:
1.  Deployment of **Backoffice_v8.35.0**.
2.  Deployment of **Backoffice_v8.36.0**.
3.  Deployment of **Backoffice_v8.37.0** (Previously announced for March 24).
4.  **Deployment of Backoffice_v8.37.1** (Newly confirmed and initiated by Jonathan Tanudjaja on March 25, 2026).

**Key Dates, Deadlines, & Follow-ups**
*   **Release 1:**
    *   **Version:** Backoffice_v8.35.0
    *   **Announced:** March 9, 2026, at 05:11 UTC.
    *   **Scheduled Execution:** Approximately 1:20 PM on March 9, 2026.
    *   **Reference:** [Backoffice_v8.35.0 Release Notes](https://ntuclink.atlassian.net/wiki/spaces/SE/pages/3290431602/Backoffice_v8.35.0)
*   **Release 2:**
    *   **Version:** Backoffice_v8.36.0
    *   **Announced:** March 12, 2026, at 13:44 UTC.
    *   **Scheduled Execution:** Same day (March 12, 2026).
    *   **Reference:** [Backoffice_v8.36.0 Release Notes](https://ntuclink.atlassian.net/wiki/spaces/SE/pages/3304423425/Backoffice_v8.36.0)
*   **Release 3:**
    *   **Version:** Backoffice_v8.37.0
    *   **Announced:** March 24, 2026, at 02:17 UTC.
    *   **Scheduled Execution:** Same day (March 24, 2026).
    *   **Reference:** [Backoffice_v8.37.0 Release Notes](https://ntuclink.atlassian.net/wiki/spaces/SE/pages/3334537232/Backoffice_v8.37.0)
*   **Release 4 (New):**
    *   **Version:** Backoffice_v8.37.1
    *   **Announced:** March 25, 2026, at 02:33 UTC.
    *   **Scheduled Execution:** Today (March 25, 2026) by Jonathan Tanudjaja.
    *   **Reference:** [Backoffice_v8.37.1 Release Notes](https://ntuclink.atlassian.net/wiki/spaces/SE/pages/3340828673/Backoffice_v8.37.1)

**Contextual Notes**
*   These updates align with the resource schedule for **FPG Back Office (Mon-Thurs)**.
*   The v8.37.1 release represents an immediate follow-up to the v8.37.0 cycle, initiated within 24 hours of the previous announcement.


## [6/32] RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Messages: 18 | Last Activity: 2026-03-25T02:30:47.572000+00:00 | Last Updated: 2026-03-25T02:51:45.629748+00:00
**Daily Work Briefing: Automated Test Results Summary (RMN Notification)**

**Key Participants & Roles**
*   **Collection Runner App:** Automated testing agent executing API suites.
*   **Webhook Bot:** Reporting mechanism; consistently returning "unable to process your request" on all notifications.
*   **Parties Involved:** No human participants engaged; system-generated notification log.

**Main Topic/Discussion**
The conversation comprises automated notifications from the Collection Runner regarding nightly API test executions across `promo-service`, `marketing-personalization-service`, and `marketing-service` in the **staging** environment. Logs track "API Tests" and "API Contract Tests." The monitoring period has extended from March 12 through **March 25, 2026**, with execution windows at approximately 01:05 UTC, 02:30/02:31 UTC, and 03:20/03:21 UTC.

**Test Execution Status & Anomalies**
*   **Stable Services:**
    *   `promo-service`: Confirmed stable on March 25 (02:30 UTC) with 10 Passed / 0 Failed API tests and 6 Passed / 0 Failed Contract tests. Stability continues from previous runs on March 24 and earlier dates.
    *   `marketing-personalization-service`: Previously confirmed stable through **March 24, 2026**. No new reports were generated for this service in the latest batch (post-March 25 01:05 UTC), but historical stability remains unbroken as of March 24.
*   **Persistent Failures (`marketing-service`):**
    *   The pattern of **recurring API test failures** persists on **March 25, 2026, at 01:05 UTC**, extending the instability observed since March 17.
        *   **Mar 25 (01:05 UTC):** 51 Passed / **2 Failed** (API Tests). Total requests were 17. Contract tests remained stable (20 Passed / 0 Failed) with 16 total requests.
    *   The failure count remains consistent at exactly 2 API failures per run across the streak from March 17 through **March 25, 2026**.

**Pending Actions & Ownership**
*   **Investigate Persistent `marketing-service` Failures:** The root cause for the consistent 2 API test failures observed daily from March 17 through **March 25, 2026**, remains unaddressed. Engineering teams must review failure reports immediately given the five-day streak of recurrence in the current monitoring window.
*   **Webhook Bot Remediation:** The bot failed to process requests in every notification cycle from March 12 through **March 25, 01:05 UTC** (including the latest log). Immediate attention is required from DevOps or Automation Infrastructure.

**Decisions Made**
*   No human decisions recorded; all entries are automated system outputs.

**Key Dates & Deadlines**
*   **Failure Window (Historical):** Instability noted on March 12 and 13.
*   **Current Failure Window:** The service has been failing consistently since **March 17, 2026**, continuing through **March 25, 2026**.
*   **Monitoring Period:** Data covers runs from **March 12, 2026**, through **March 25, 2026** (spanning execution windows at 01:05 UTC, 02:30/02:31 UTC, and 03:20/03:21 UTC).
*   **Next Steps:** Immediate investigation into the `marketing-service` API flakiness and Webhook Bot connectivity issues.


## [7/32] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/d1FwEozsGcU | Messages: 12 | Last Activity: 2026-03-25T02:26:46.451000+00:00 | Last Updated: 2026-03-25T02:51:58.588608+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Sathya Murthy Karthik:** Reported initial technical issue (cannot open order/invoice on mobile; backoffice error "order type unspecified").
*   **Daryl Ng:** Escalated the issue to engineering/support, provided direct link to Order #75577957.
*   **Wai Ching Chan:** Investigated the specific order details and confirmed the root cause (date discrepancy).
*   **Prajney Sribhashyam:** Identified the root cause: The order date was set incorrectly (1 AD).
*   **Sneha Parab & Andin Eswarlal Rajesh:** Tagged for initial assistance; status not updated in this thread.

**Main Topic**
Troubleshooting Order #75577957, which failed to generate an invoice and crashed on mobile devices due to a backend data error regarding the order date (recorded as "1 AD").

**Pending Actions & Ownership**
*   **Action:** Fix the date record for Order #75577957 in the system.
    *   **Owner:** Wai Ching Chan
    *   **Status:** In progress ("Will need to check and fix").
*   **Action:** Verify if a new order can be successfully placed after the fix is applied.
    *   **Owner:** To be confirmed (likely Sathya Murthy Karthik or requester).

**Decisions Made**
*   Confirmed that the system failure was caused by an invalid historical date ("1 AD") rather than a code crash or user error.

**Key Dates, Deadlines & Follow-ups**
*   **Order ID:** 75577957
*   **Issue Date:** 2026-03-25 (Timeline: 01:50 – 02:26 UTC)
*   **Follow-up Required:** Immediate resolution of the date field for Order #75577957 to enable invoice generation and order placement.

**References**
*   Admin-UAT Link: `https://admin-uat.fairprice.com.sg/customer-support/delivery-orders/75577957`


## [8/32] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/-3PHNWPnwGs | Messages: 4 | Last Activity: 2026-03-25T02:24:15.864000+00:00 | Last Updated: 2026-03-25T02:52:10.682336+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Sathya Murthy Karthik:** Initiator of the technical issue; reporting inability to access order data and generate invoices.
*   **Andin Eswarlal Rajesh:** Triage lead; coordinating the investigation and attempting to gather account details from Sathya.

**Main Topic**
Technical troubleshooting regarding Order #75577957. The user is unable to open the order on a mobile device (app crashing) and cannot generate an invoice via the backoffice due to an "order type unspecified" error.

**Status of Actions & Ownership**
*   **Action:** Investigate Order #75577957 access issues and invoice generation failure.
    *   **Owner:** Andin Eswarlal Rajesh (assigned initially in the thread).
    *   **Current Status:** **Resolved/Redirected.** Andin noted at 02:24 on March 25 that he located the issue details in a separate discussion thread ("Nvm saw the other thread"), ending the need for further inquiry within this specific chat space.

**Decisions Made**
*   No formal decisions were recorded in this specific chat log, as the discussion concluded with the realization that the relevant context existed elsewhere. The team determined that the issue requires follow-up in a different thread rather than continuing here.

**Key Dates & Deadlines**
*   **Issue Reported:** March 24, 2026 (09:39 UTC) by Sathya Murthy Karthik.
*   **Investigation Started:** March 25, 2026 (02:21 UTC) by Andin Eswarlal Rajesh.
*   **Thread Closed/Redirected:** March 25, 2026 (02:24 UTC).

**Summary for Follow-up**
The team should verify the status of Order #75577957 in the "other thread" referenced by Andin to ensure Sathya's invoice request and crash issue are fully resolved.


## [9/32] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-03-25T02:20:57.946000+00:00 | Last Updated: 2026-03-25T02:52:50.432670+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Update)**
**Date:** March 25, 2026 (Morning)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 338

### Key Participants & Roles
*   **System/Tool:** Datadog App (Automated Monitoring)
*   **Notification Channel:** `@hangouts-ShoppingCartNotification`
*   **Ownership Teams:** `dpd-pricing`, `dpd-pricing-cart`.

### Main Topic
Instability in `frontend-gateway` has evolved from intermittent spikes to a recurring pattern of rapid oscillation between trigger and recovery states. The issue now encompasses widespread degradation across **Read** (Wish List, Cart), **Write** (Wish List updates), and **Checkout Success Rates**, with recent activity extending into the early hours of March 25.

### Incident Timeline & Actions
**Previous Context:**
*   *Activity from March 21–14:04 UTC regarding `frontend-gateway` latency and initial cart spikes.*

**New Activity (March 24, UTC+0 - March 25, UTC+0)**
*   **18:02–18:13 UTC:** Cascade of errors affecting multiple endpoints. V2 Shopping List success rate dropped to 97.778%, Put Wish List to 95.0%, and Checkout P99 spiked to 3.794s. Recovered by 18:13 UTC.
*   **18:49–20:15 UTC:** Recurring failures on Checkout success rates (dropping to 99.696% and 99.517%) and Get Cart P99 latency (2.072s). Recovered by 20:24 UTC.
*   **22:00–22:10 UTC:** Checkout success rate dropped to 99.698%. Recovered at 22:10 UTC.
*   **23:13–23:14 UTC (Mar 24):** P90 of `get wish list by id` spiked to 1.721s. Recovered immediately (1.016s).
*   **23:33–23:34 UTC (Mar 24):** P99 of `post /api/cart` spiked to 6.427s. Recovered immediately (0.78s).
*   **23:35–23:45 UTC (Mar 24):** Checkout success rate dropped to 99.85%. Recovered at 100.0% by 23:45 UTC.
*   **00:06–00:17 UTC (Mar 25):** Checkout success rate dropped to 99.876%. Recovered at 99.946% by 00:17 UTC.
*   **01:14–01:31 UTC (Mar 25):** Significant latency spikes on `put /api/product/_id_/wish-list` (P99: 6.945s, P90: 5.419s). Concurrent Checkout success rate dropped to 99.887%. All metrics recovered by 01:31 UTC.
*   **02:10–02:20 UTC (Mar 25):** `st-cart-prod` `post /cart` success rate dropped to 99.679%. Recovered at 100.0% by 02:20 UTC.

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** The failure pattern has expanded to include write operations on Wish List updates (P99 > 6s) and backend success rate drops in `st-cart-prod`. The frequency of triggers indicates a systemic, recurring issue affecting the full lifecycle.
*   **Scope:** Immediate correlation required between the 01:14 UTC Write failure (Wish List update) and subsequent Checkout failures. Investigate shared dependencies in `st-cart-prod` for cascading root causes.

### Decisions Made
*   **Priority Escalation:** Status remains **"Critical Incident"**. The activity window has extended from March 20 through at least March 25, 02:20 UTC, with no stabilization observed.
*   **Focus Shift:** Prioritize investigation into the high-impact Wish List write latency (Event IDs `8558701726293837406`, `8558701800419189339`) and the persistent Checkout success rate degradation.

### Key Dates & Follow-ups
*   **Critical Window:** Extended activity from March 20 through at least March 25, 02:20 UTC.
*   **Follow-up:** Analyze Event IDs `8558701726293837406`, `8558758953391603245`, and others to identify common failure vectors across frontend and cart services.

**References:**
*   **Active Monitors:** `21245720` (Wish List P90), `21245713` (Cart P99), `21245708` (Checkout Success), `21245701` (Wish List Put P99), `22710472` (st-cart-prod success).
*   **Service Tags:** `service:frontend-gateway`, `service:st-cart-prod`, `team:dpd-pricing`.


## [10/32] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/qx4BVM7nI60 | Messages: 22 | Last Activity: 2026-03-25T02:17:26.242000+00:00 | Last Updated: 2026-03-25T02:53:06.259360+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Lead/Coordinator (Overseeing war room creation and sign-off).
*   **Zaw Myo Htet:** Backend/Data Specialist (Validated SAP-DBP sync logic).
*   **Jonathan Tanudjaja:** Frontend Developer (Resolved UI discount bug; deployed fix to UAT).
*   **Andin Eswarlal Rajesh:** Frontend Lead (Confirmed root cause analysis).
*   **Daryl Ng:** Stakeholder (Monitoring synchronization status).

**Main Topic**
Urgent resolution of high-priority "Staff App" issues, specifically the PWP UI bug where offers/discounts failed to display. While initial discussions on March 24 focused on debugging and logging tickets, the focus has now shifted to verification of the deployed fix.

**Decisions & Findings**
*   **Data Sync (ZOTO):** Confirmed earlier that production data syncs between SAP and DBP are functioning correctly; no backend issue exists.
*   **Root Cause (PWP/UI):** Identified as a legacy implementation flaw where the Frontend incorrectly calculated discounts by selecting only the "first item" in an array. No recent pricing logic changes were made.
*   **Implementation Status:** Jonathan Tanudjaja has completed the fix for ticket **DPD-811**. The code is now live in the **UAT** environment and requires re-verification.

**Pending Actions & Ownership**
1.  **Re-verify Fix (Urgent):** @Prajney Sribhashyam to re-verify the discount display functionality on UAT following Jonathan's deployment update.
2.  **Final Sign-off:** Pending successful UAT verification, the "war room" meeting scheduled for late March 24 will now serve to finalize closures and secure stakeholder sign-off.
3.  **Ticket Closure:** Once re-verification is confirmed by Prajney, ticket **DPD-811** will be marked as resolved.

**Timeline & Deadlines**
*   **Date:** March 25, 2026 (Update based on new message timestamp).
*   **Previous Estimate:** Jonathan initially estimated a 1–2 day effort window.
*   **Current Status:** Fix deployed to UAT as of early morning March 25 (02:17 UTC).
*   **Immediate Goal:** Complete re-verification in UAT to close the Staff App issue immediately.

**Archived Context**
*   *Original Ticket Creation:* Ticket **DPD-811** was logged on March 24 to address the display logic error.
*   *Root Cause Clarification:* Andin Eswarlal Rajesh confirmed that the "after paid" implementation aligns with BO displays and final invoices, validating the fix approach.


## [11/32] Team Starship
Source: gchat | Group: space/AAQAX9iKYf0 | Messages: 4 | Last Activity: 2026-03-25T02:08:01.557000+00:00 | Last Updated: 2026-03-25T02:53:39.085996+00:00
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
    *   **Status:** UAT Sign-off received for Customer App, Backend/Backoffice, MP Seller (Mirakl & DBP), and Preorder Staff Application.
    *   **Open Item:** Returns & refunds remain the only open item, with an updated ETA of **EOD today**.
    *   **Alignment:** Corporate Control and Finance clarified scope for BCRS and "Project Light." Formal sign-off expected by EOD to complete finance formalities.
    *   **Deployment:** Production deployment (DBP backend & SAP) tentatively scheduled for **Thursday, 12:00 AM** (confirmation by 12:00 PM today). Smoke testing planned for Friday (and weekend if needed).

2.  **Bug Report: App Icon Display (DPD-783)**
    *   **Issue:** Vivian reported a regression where the app icon displays a Christmas theme instead of the default.
    *   **Action:** Bug ticket **DPD-783** created for urgent resolution ("asap").

3.  **New Request: Cart-Level Coupon Allocation (GP Calculation)**
    *   **Request:** Alvin Choo relayed a request from Ryan to stop considering cart-level coupon allocation per SKU.
    *   **Objective:** Ensure accurate Gross Profit (GP) calculation for products.
    *   **Decision/Pending:** The team is currently determining whether to park this requirement in the "Project Light" list.

4.  **Frontend Tag Mapping Inquiry**
    *   **Inquiry:** Zi Ying Liow sought clarification on mapping logic between promotion methods and frontend tags. No resolution documented yet; requires technical verification.

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

**Pending Actions & Owners**

| Action Item | Owner | Deadline/Note |
| :--- | :--- | :--- |
| **Urgent Fix:** Revert app icon display (DPD-783) | Engineering Team / Andin Eswarlal Rajesh | ASAP |
| Finalize Returns & Refunds sign-off; Confirm Production Deploy time | Prajney Sribhashyam / Finance/Corp Control | **EOD Today** |
| Submit list of items to deprioritize from Jan 2026 Omni Roadmap | All PMs | **EOD Tomorrow (March 25)** |
| Update OMNI-1282 status (De-prioritize) | Alvin Choo / Koklin Gan | Pending confirmation |
| **PAUSE** work on OMNI-1345 requirements | All Stakeholders | Until business model is finalized |
| **Clarify:** Cart-level coupon allocation logic & Project Light inclusion | Alvin Choo / Ryan's team | Pending decision |
| **Investigate:** Promotion method to frontend tag mapping | Zi Ying Liow / Tech Team | As needed |
| Prioritize Scan@Door AI Personalisation (BE impact assessment) | Danielle Lee, Daryl Ng, Tech Leads | Immediate review required |

**Key Dates & Follow-ups**

*   **Meeting Rescheduled:** Weekly Epics meeting postponed to **Wednesday, March 12 (tomorrow) at 11:00 AM**.
    *   **Location:** Level 12 Room 18 (subject to availability; virtual or pantry table as backup).
    *   **Agenda:** BCRS work progress review, capacity planning, and Scan@Door prioritization decision.
*   **Reference Tickets:** SHOP-3779, OMNI-1099, DPD-100, **DPD-783**, OMNI-1345, OMNI-1282, OMNI-1421.


## [12/32] @omni-ops #standup - Mar 25
Source: gchat | Group: space/AAQANjGExUA | Messages: 1 | Last Activity: 2026-03-25T02:01:19.578000+00:00 | Last Updated: 2026-03-25T02:53:59.575617+00:00
**Daily Work Briefing: #standup Channel**
**Date:** March 25, 2026
**Channel:** @omni-ops #standup
**Source URL:** https://chat.google.com/space/AAQANjGExUA

### **Key Participants & Roles**
*   **Yangyu Wang:** Initiator of the standup check-in. (Specific role not explicitly defined in log, but active participant).
*   **Channel Audience:** 4 out of 7 members viewed the message; specific identities of other viewers are not listed.

### **Main Topic/Discussion**
The conversation consisted solely of a prompt by Yangyu Wang asking for the initiation or progress update of the daily standup meeting ("standup?"). No substantive discussion, status updates, or technical details were recorded in this log entry. The interaction appears to be an attempt to convene the team rather than a completed report.

### **Pending Actions & Ownership**
*   **Action:** Initiate/Conduct the daily standup meeting.
*   **Owner:** Team members (triggered by Yangyu Wang).
*   **Status:** Pending. The prompt indicates the session has not yet commenced or concluded, as no subsequent updates were recorded in this timeframe.

### **Decisions Made**
*   None. No decisions were reached or documented within the provided chat log.

### **Key Dates & Follow-ups**
*   **Timestamp:** March 25, 2026, at 02:01:19 UTC.
*   **Immediate Follow-up Required:** Team members need to respond to Yangyu Wang's prompt to begin the standup or provide a status update if the meeting was already underway but not logged.

### **Summary**
On March 25, 2026, at 02:01 UTC, Yangyu Wang posted a single inquiry in the #standup channel asking for the start of the daily standup. The message was viewed by four members of the seven-person team. No further content, status reports, blockers, or action items were generated in this specific log segment. The conversation remains open pending further input from the team to proceed with the standard daily briefing protocol.


## [13/32] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY | Messages: 15 | Last Activity: 2026-03-25T01:50:27.110000+00:00 | Last Updated: 2026-03-25T02:54:28.599765+00:00
**Updated Briefing: BCRS Firefighting Group**
**Date:** March 25, 2026 (Latest activity: ~1:40 AM)
**Source:** Google Chat Space & Shared UAT Tracker (71 messages total)

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
1.  **Production Deployment Planning:** Prajney initiated a session for March 25 to secure sign-offs and plan production deployment, prioritizing attendance from Daryl Ng, Sneha Parab, Andin Eswarlal Rajesh, and Onkar Bamane.
2.  **UAT & Beta Testing Strategy:** Sathya requested clarification on the beta testing plan, specifically asking for tester assignments, specific SKUs to be tested, and detailed procedures.
3.  **Critical System Crash (Order #75577957):** Continuing from March 24; Sathya reports an inability to open Order #75577957 on mobile (repeated crashes) and a backend "order type unspecified" error blocking invoice generation.
4.  **Michael Bui's Departure:** Michael noted he has full-day meetings but emphasized his last day to deploy to Production is tomorrow (March 26). He requested meeting recordings and UAT sign-offs in Jira tickets, as he will be on leave next week.

### **Decisions & Updates**
*   **Deployment Priority:** Immediate planning session scheduled for March 25 to finalize production deployment and secure necessary sign-offs.
*   **Documentation Requirement:** Michael Bui mandated that UAT sign-offs must be explicitly indicated in Jira tickets before he departs next week.
*   **Meeting Protocol:** Requests made to record the deployment planning session for absentees.

### **Pending Actions & Owners**
| Action Item | Owner(s) | Status/Context |
| :--- | :--- | :--- |
| **Production Deployment Session** | Prajney Sribhashyam / Onkar Bamane | **Urgent (Mar 25, 1:11 AM):** Session scheduled today to plan deployment and secure sign-offs. Attendance critical for Daryl Ng, Sneha Parab, Andin Eswarlal Rajesh. |
| **Beta Testing Plan Definition** | Sathya Murthy Karthik / Prajney Sribhashyam / Onkar Bamane | **High Priority (Mar 25, 1:13 AM):** Awaiting confirmation on tester list, specific SKUs for testing, and detailed beta procedures. Thread active with 11+ replies. |
| **Order #75577957 Crash Resolution** | Sathya Murthy Karthik / Technical Team | **Critical (Mar 24-25):** Mobile app crashes on order open; backoffice fails to generate invoice ("order type unspecified"). Follow-up requested by Sathya. |
| **Jira Sign-off & Meeting Recording** | Michael Bui / Team | **Urgent:** Michael requires UAT sign-offs recorded in Jira and meeting recordings before his final deployment day (Mar 26). |

### **Key Dates & Deadlines**
*   **March 24, 9:39 AM:** Critical crash reported on Order #75577957.
*   **March 25, Today:** Target for production deployment planning session and sign-off acquisition.
*   **March 26 (Thu):** Last day for Michael Bui to deploy to Production; leave begins next week.

### **Historical Context Retained**
*   Existing e-comm test accounts deemed unusable for Pre-order staff app; new BCRS CF items and specific GWP SKUs required.
*   Original deadline for SAP Deposit API development was Feb 20 (missed/risk noted).
*   Re-delivery flow testing ongoing with audio issues reported on March 16 awaiting resolution.
*   Deposit SKU linking investigation ongoing due to failure to link post-publishing.


## [14/32] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/OYprgYt5wxQ | Messages: 7 | Last Activity: 2026-03-25T01:40:23.024000+00:00 | Last Updated: 2026-03-25T02:54:42.036641+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Michael Bui:** Deployer/Developer (Last day to deploy to Production; leaving next week).
*   **Prajney Sribhashyam:** Stakeholder/Product Owner (Managing sign-off process and Epic tracking).
*   **Other Mentioned:** Daryl Ng, Sneha Parab, Andin Eswarlal Rajesh (Recipients of original deployment request); Onkar Bamane (Planned for deployment session).

**Main Topic**
Coordination regarding the final Production (PRD) deployment for the OMNI & DPD Epics, specifically addressing UAT sign-off procedures and Michael Bui's availability constraints.

**Decisions Made**
*   **Sign-Off Mechanism:** Sign-offs will be recorded at the overall OMNI & DPD Epic ticket level rather than on individual sub-tickets to ensure scalability.
*   **Documentation:** A specific sign-off form will be shared by Prajney Sribhashyam for reference.
*   **Deployment Timing:** Michael Bui confirmed he will process PRD deployment today (25/03) or latest by tomorrow (Thu 26/03).

**Pending Actions & Ownership**
1.  **Share Sign-Off Form:** Prajney Sribhashyam to distribute the sign-off document. (Owner: Prajney)
2.  **Update Jira Ticket:** Michael Bui to comment on his specific ticket referencing the Epic-level sign-off once received/processed. (Owner: Michael)
3.  **Meeting Recording:** The team must record the meeting since Michael cannot attend due to full-day meetings. (Owner: Team/Organizer)

**Key Dates & Deadlines**
*   **2026-03-25 (Wed):** Target for PRD deployment and sign-off processing.
*   **2026-03-26 (Thu, Tomorrow):** Absolute deadline for Michael Bui's final PRD deployment.
*   **Next Week:** Michael Bui is on leave; no further deployments expected from him after the 26th.

**Follow-Ups**
*   Michael Bui will follow up after his meetings.
*   A session with Onkar Bamane was identified as prioritized for deployment planning (status implied as active).


## [15/32] Project Light: Mobilization and Planning Workshop Day 1 - Mar 24
Source: gchat | Group: space/AAQAA8d_pfI | Messages: 18 | Last Activity: 2026-03-25T01:36:57.479000+00:00 | Last Updated: 2026-03-25T02:55:02.863531+00:00
**Daily Work Briefing: Project Light – Mobilization & Planning Workshop (Day 1)**
**Date:** March 24, 2026 (Session concluded; new insights added Mar 25)
**Resource Link:** https://chat.google.com/space/AAQAA8d_pfI

**Key Participants & Roles**
*   **Jacob Yeo:** Meeting facilitator.
*   **Vivian Lim Yu Qian:** Presenter/UI Walkthrough; defined technical/action items.
*   **Tiong Siong Tee:** UX Lead; proposed agenda flow and requested Figma access.
*   **Cecilia Koo Hai Ling:** Design/UX Contributor; shared DoorDash, NTUC FairPrice, and Lazada references.
*   **Christine Yap Ee Ling:** Internal Liaison; handling Figma link distribution.
*   **Rajesh Dobariya:** Stakeholder; reviewed delivery categorization references.

**Main Topic & Discussion Updates**
The team conducted a high-level UX walkthrough and UI review, expanding reference analysis to include local competitors:
*   **Navigation & Filters:** Clarification remains needed on whether category page filters should be pre-configured ("dynamic") or retrieved dynamically.
*   **UI Clarity:** The toggle selection between "Scheduled" and "Quick" modes requires improved visual definition.
*   **Compliance:** Discussed potential separation of eGift cards from vouchers to meet compliance requirements.
*   **Reference Analysis (Updated):**
    *   **DoorDash & FairPrice:** Reviewed DoorDash's first-time app open for categorization inspiration. Cecilia shared NTUC FairPrice examples (SharkNinja Official Store, FP Unilever Tag) for local context. The FairPrice tag link was viewed by 15 of 21 participants initially.
    *   **Lazada Dynamic Labels:** Cecilia noted that Lazada's "promo label" within the seller section is dynamic, specifically designed to nudge users toward higher tiers.
    *   **Gamification Strategy:** Cecilia highlighted a Lazada mega campaign example where a gamified "Help me click, get your own $3 reward" mechanic drives daily traffic. Users can help once per day; every three helps yields $3 to offset the cart. This link was viewed by 14 of 21 participants: https://s.lazada.sg/s.381Dg

**Decisions Made**
*   **Reference Alignment:** Agreed that DoorDash's categorization approach is valid (confirmed by Rajesh). Lazada examples regarding dynamic promo labeling and gamified traffic drivers were accepted as supplementary data for engagement strategies.
*   **Filter Logic:** No final consensus on filter behavior (dynamic vs. pre-configured); pending technical solution discussion led by Vivian.

**Pending Actions & Owners**
1.  **Share Figma Link:** Christine Yap Ee Ling to send via separate internal chat (requested by Tiong Siong Tee).
2.  **Resolve Filter Logic:** Vivian Lim Yu Qian and the technical team to finalize category page filter behavior.
3.  **Refine UI Toggle:** Design team to address visual clarity for "Scheduled/Quick" toggle selection.
4.  **Compliance Review:** Determine if eGift cards must be standalone from vouchers.
5.  **Analyze Local Benchmarks:** UX Lead (Tiong Siong Tee) to review FairPrice links and the new Lazada gamification/promo label patterns for Project Light integration.

**Key Dates & Follow-ups**
*   **Event:** Project Light Mobilization and Planning Workshop Day 1 (March 24, 2026).
*   **Status:** Session concluded; materials and new references shared via chat on March 25.
*   **Next Step:** Internal distribution of Figma link by Christine Yap Ee Ling; UX team to analyze Lazada gamification mechanics for potential application in mega campaigns.


## [16/32] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4 | Messages: 31 | Last Activity: 2026-03-25T01:36:07.165000+00:00 | Last Updated: 2026-03-25T02:55:33.794202+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Space Creator; Lead coordinating the briefing.
*   **Daryl Ng, Gopalakrishna Dhulipati, Tiong Siong Tee, Michael Bui, Akash Gupta:** Designated "Project Light Attack and Defence Leads".
*   **Hui Hui Voon:** Owner of the D&T Scope for Project Light Workshop document.

**Main Topic**
Following the transition to active strategic planning ("Room 2") on March 24, the team is finalizing specific slide preparation within six "Spotlight Topics." While Alvin Choo initiated collaboration on **"RMN"** and **"Payment"** slides on March 24, a new flexibility protocol was established on March 25 allowing leads to attend other meetings (e.g., BCRS) if required. Concurrently, technical direction has shifted toward decoupling from SAP, with consensus that SAP should serve primarily for finance and sales records purposes.

**Pending Actions & Ownership**
*   **Action:** Finalize content for "RMN" and "Payment" slides in the D&T Scope document.
    *   **Ownership:** Alvin Choo (initiated), Hui Hui Voon (Document Owner).
    *   **Status:** In progress; collaboration initiated March 24, ~9:32 AM UTC.
*   **Action:** Clarify backend API responsibilities with CoMall regarding personalization and orchestration.
    *   **Ownership:** Michael Bui (to note and document).
*   **Action:** Finalize the Attack/Defence team composition pending Dennis's confirmation following Alvin Choo's email.
    *   **Ownership:** Alvin Choo.
*   **Action:** Address technical clarifications raised by Tiong Siong Tee regarding Inventory visibility, Corporate Control alignment, and Product management portal structure (FP vs. Sellers).
    *   **Ownership:** Alvin Choo and Gopalakrishna Dhulipati.

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
*   **Session Start ("Room 2"):** March 24, 2026 (1:02 AM UTC).
*   **Spotlight Topics List Published:** March 24, 2026 (3:14 AM UTC).
*   **Email Sent for Team Confirmation:** March 24, 2026 (3:51 AM UTC) by Alvin Choo.

**Summary of Activity Log**
*   **March 23, 4:27 PM:** Michael Bui shared a customer journey diagram.
*   **March 24, 1:02 AM:** Alvin announced the start of "Room 2" sessions.
*   **March 24, 3:14 AM:** Alvin defined six spotlight topics (Inventory, Payment, Loyalty, Backoffice, RMN, AI).
*   **March 24, 3:51 AM:** Daryl Ng inquired about team assignments; Alvin confirmed emails sent to Dennis.
*   **March 24, 6:28 AM:** Tiong Siong Tee questioned the product management portal structure (FP vs. Sellers); flagged for "Backoffice" discussion.
*   **March 24, 7:38 AM:** Gopalakrishna Dhulipati rejected treating FPG as a standard seller due to governance conflicts.
*   **March 24, ~9:32 AM:** Alvin Choo directed the team to work on "RMN" and "Payment" slides within the D&T Scope document shared by Hui Hui Voon.
*   **March 25, 1:31 AM:** Alvin Choo informed leads they are free to attend other meetings like BCRS if required.
*   **March 25, 1:36 AM:** Tiong Siong Tee agreed with Rock that SAP should be decoupled, serving only for finance and sales records.

**Space URL:** https://chat.google.com/space/AAQAsFyLso4


## [17/32] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/y11GNi2Z3Yo | Messages: 2 | Last Activity: 2026-03-25T01:35:06.555000+00:00 | Last Updated: 2026-03-25T02:55:43.362629+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Lead/Coordinator. Facilitates scheduling flexibility for team members regarding conflicting commitments.
*   **Daryl Ng:** Team Member/Lead. Confirms attendance for specific project sessions.

**Main Topic/Discussion**
The conversation focused on scheduling coordination between the "Project Light Attack and Defence" meeting and other mandatory engagements, specifically the BCRS (Business Continuity Risk Scenario?) meeting. Alvin Choo clarified that if team members have conflicting requirements (e.g., BCRS), they are authorized to attend those meetings instead of Project Light.

**Decisions Made**
*   **Attendance Priority:** No blanket attendance requirement was enforced for the Project Light meeting; flexibility is granted if other critical meetings (like BCRS) arise.
*   **Confirmed Schedule:** Daryl Ng confirmed his intention to prioritize and join the Project Light meeting scheduled for 10:30 AM on March 25, 2026.

**Pending Actions & Ownership**
*   **Action:** Attend the Project Light meeting at 10:30 AM.
    *   **Owner:** Daryl Ng
    *   **Status:** Confirmed/In Progress.

**Key Dates & Follow-ups**
*   **Date:** March 25, 2026 (Tuesday).
*   **Event Timing:** Project Light meeting at 10:30.
*   **Reference Context:** BCRS meeting (time not specified in chat).

**Metadata Reference**
*   **Space URL:** https://chat.google.com/space/AAQAsFyLso4
*   **Total Messages Reviewed:** 2


## [18/32] DPD x DPM
Source: gchat | Group: space/AAQApzD7Im0 | Messages: 2 | Last Activity: 2026-03-25T01:34:37.458000+00:00 | Last Updated: 2026-03-25T02:56:07.676627+00:00
### Daily Work Briefing: DPD x DPM Collaboration Space

**Key Participants & Roles**
*   **Daryl Ng:** Tech Lead; flagged CHAS calculation issues. Tagged regarding Gamification ownership and delivery logic inquiries. Directly requested breakdown of existing orange label display logic on Omni and OG homepages.
*   **Vivian Lim Yu Qian:** Initiator of topics; driving mandates (MTI price per piece) and feature rollouts. Investigating SWA migration history.
*   **Rajesh Dobariya:** Inquired about Gamification data requirements for CRM PNS automation. Previously asked to clarify display logic for "Normal" vs. "Express" delivery text changes.
*   **Sneha Parab:** Tagged regarding Tech Lead ownership transition and SWA/Wordpress vs. Publitas inquiry.
*   **Yangyu Wang & Zi Ying Liow:** Tagged in the latest thread regarding orange label display logic clarification.

**Main Topics**
1.  **Delivery Text Logic (Updated):** Daryl Ng explicitly requests a breakdown of the *existing* logic for displaying the "orange label" text on both Omni and OG homepages to support required updates. This follows Rajesh Dobariya's earlier inquiry about "Normal Delivery" logic for Express updates.
2.  **Gamification Data Requirements:** CRM team requires specific BigQuery (BQ) data points for PNS automation. Needs confirmation on existing data points or effort estimation for pushing new data. Previous ownership attributed to Nhu/Jack's team.
3.  **Govt Mandate (MTI):** Implementation of "Price per Piece" info for 40+ categories in the current app MVP.
4.  **CHAS Calculation Bug:** UI discrepancy where cart-level discounts split at the sales order level affect CHAS calculations (Ticket: `DPD-530`).
5.  **SWA Migration:** Investigation into reverting SWA ad serving from Publitas back to Wordpress (`DIS-585`) and associated effort estimation.

**Pending Actions & Ownership**
*   **Orange Label Logic Clarification:** Share and document the existing logic for showing orange labels on Omni and OG homepages (specifically regarding text variables). *Owner: Daryl Ng (to share details).*
*   **Gamification Data Query:** Clarify current ownership of Gamification features and provide BQ table/column names or confirm data push needs. *Owner: Daryl Ng (to clarify).*
*   **Tech Lead Confirmation:** Determine if Daryl Ng is still the lead for Price per Piece expansion or identify the correct owner. *Owner: Vivian Lim Yu Qian / Team.*
*   **CHAS Issue Analysis:** Explain the cart-level discount splitting issue to enable an API fix. *Owners: Prajney Sribhashyam, Wai Ching Chan.*
*   **SWA Revert Analysis:** Assess effort required to revert SWA ad serving from Publitas back to Wordpress. *Owners: Sneha Parab, Arijit Mondal.*

**Decisions Made**
*   No formal decisions recorded; the thread contains active requests for clarification and execution. The intent to fix the CHAS bug via an API update remains established. The feasibility of reverting SWA ads is under investigation. The specific implementation details for the "orange label" text on Omni/OG homepages are now pending Daryl Ng's input based on his March 25 request.

**Key Dates & Deadlines**
*   **March 11:** Space creation; Vivian's inquiry on Price per Piece.
*   **March 12:** Daryl flags CHAS calculation issue (`DPD-530`).
*   **March 16:** Request to complete 100% Android rollout for Search on Omni home and Sticky Header UI. Vivian initiates SWA inquiry. Rajesh inquires about "Normal Delivery" logic.
*   **March 24, 07:39 AM:** Vivian initiates inquiry regarding SWA `DIS-585`.
*   **March 25, 01:34 AM:** Daryl Ng requests clarification on the existing orange label display logic for Omni and OG homepages. Last reply pending from Yangyu Wang/Zi Ying Liow.

**Reference Links**
*   Price Per Piece Wiki: `https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008175965/Price+Per+Piece+Multipack+in+Display+Unit`
*   CHAS Ticket: `DPD-530`
*   Sticky Header UI Ticket: `ENGM-2501`
*   SWA Migration Ticket: `DIS-585`


## [19/32] Backend Chapter
Source: gchat | Group: space/AAAAHhDyHI4 | Messages: 1 | Last Activity: 2026-03-25T01:29:26.022000+00:00 | Last Updated: 2026-03-25T02:56:29.408987+00:00
**Daily Work Briefing: Backend Chapter**

**Key Participants & Roles**
*   **Michael Bui:** Investigated GCP PubSub configuration for message delivery.
*   **Nicholas Tan:** Inquired about PubSub flags; flagged security concerns regarding Service Account (SA) keys in `fpg-titan-preprod`.
*   **Lester Santiago Soriano:** Blocked on CI/CD pipeline errors after upgrading Go dependencies; requested support.
*   **Maou Sheng Lee:** Suggested using AI tools to resolve Lester's issue.
*   **Boon Seng Ong:** Investigated deployment failures with `deploy-esp-image` for ESPv2, noting discrepancies between past success and current failures despite unchanged code or SDK versions.

**Main Topics**
1.  **GCP PubSub Configuration (March 6):** Michael Bui sought configuration flags for "at-most-once" delivery in GCP PubSub but found no samples. Nicholas Tan followed up, noting limited expertise. No resolution reached; discussion remains open regarding specific flag implementation.
2.  **CI/CD & Dependency Upgrade (March 12):** Lester Santiago Soriano upgraded `stdlib` to `v1.25.8` to address SonarQube vulnerability `GO-2026-4603`. The pipeline failed due to a version mismatch: the build agent's `golangci-lint` was compiled with Go 1.24, while the project targeted Go 1.25.8.
    *   *Root Cause Identified:* The error requires an update to the `dpd-backend-cicd` resource.
3.  **ESPv2 Deployment Failure (March 25):** Boon Seng Ong reported that redeploying ESPv2 via `deploy-esp-image` fails with `gcloud beta run deploy` errors, specifically: "expected a container image path" and invalid flag value for `--to-revisions`.
    *   *Investigation:* Code unchanged from 7 days prior; usage of an older `google/cloud-sdk:546.0.0-slim` image also failed. Boon suspects recent changes to the "golden pipeline."
    *   *Error Detail:* `gcloud run services update-traffic` rejected `--to-revisions [value=100]`, suggesting a syntax or parameter shift in the deployment logic.
4.  **Service Account Security Audit (March 16):** Nicholas Tan identified JSON keys embedded in Service Accounts (`pong-club-agent`, `vertex-client`) within the `fpg-titan-preprod` project. These accounts require decomposition due to security best practices.

**Pending Actions & Ownership**
*   **Resolve CI/CD Pipeline Block (Go Version):** Update `dpd-backend-cicd` resource configuration to support Go 1.25.8 or align linter version.
    *   *Owner:* **TBD** (Lester requested ownership; current owner unknown).
*   **Investigate Golden Pipeline Breakage:** Determine recent changes causing `gcloud beta run deploy` and `update-traffic` flag failures for ESPv2.
    *   *Owner:* **Boon Seng Ong** (to coordinate with pipeline maintainers).
*   **Service Account Cleanup:** Identify owners and decompose identified SAs (`pong-club-agent`, `vertex-client`) in `fpg-titan-preprod`.
    *   *Owner:* **TBD** (Nicholas Tan flagged this; ownership unknown).

**Decisions Made**
*   No formal decisions recorded. The team acknowledged the Go version mismatch requires a CICD resource update, identified the need to decompose specific Service Accounts, and flagged the golden pipeline as a potential root cause for recent deployment failures.

**Key Dates & Follow-ups**
*   **March 6, 2026:** Initial PubSub inquiry (Open).
*   **March 12, 2026:** Pipeline failure reported; escalation for CICD ownership required.
*   **March 16, 2026:** Security flag raised regarding `fpg-titan-preprod` SAs. Follow-up on SA ownership is critical.
*   **March 25, 2026:** Critical deployment failure reported; investigation into golden pipeline changes initiated.


## [20/32] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/hWcMUCKuAro | Messages: 2 | Last Activity: 2026-03-25T01:28:11.621000+00:00 | Last Updated: 2026-03-25T02:56:39.575679+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**1. Key Participants & Roles**
*   **Prajney Sribhashyam:** Initiator of the deployment session; coordinating sign-offs and logistics.
*   **Daryl Ng, Sneha Parab, Andin Eswarlal Rajesh, Onkar Bamane:** Tagged participants expected to prioritize the upcoming planning session.

**2. Main Topic/Discussion**
*   Preparation for an imminent production deployment.
*   The team is awaiting final sign-offs to proceed with this deployment today (March 25, 2026).
*   A dedicated coordination session is being organized to plan the execution of the deployment once approvals are secured.

**3. Pending Actions & Ownership**
*   **Action:** Attend and prioritize the planning session for production deployment.
    *   **Owner:** Daryl Ng, Sneha Parab, Andin Eswarlal Rajesh, Onkar Bamane.
    *   **Context:** Prajney Sribhashyam has explicitly requested these individuals to prioritize this meeting.

**4. Decisions Made**
*   **Logistics:** The planning session venue has been confirmed as **L11 Room 11**.
*   **Timeline:** The team expects to receive all necessary sign-offs for the production deployment on **March 25, 2026**.

**5. Key Dates & Deadlines**
*   **Date:** March 25, 2026 (Today).
    *   **Deadline/Expectation:** Receipt of all necessary sign-offs is expected today.
    *   **Event:** Production deployment planning session to be held later in the day at L11 Room 11.

**Reference Metrics**
*   **Resource Group:** BCRS Firefighting Group
*   **Space URL:** https://chat.google.com/space/AAQAgT-LpYY


## [21/32] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/T3AnJ6uPt5g | Messages: 4 | Last Activity: 2026-03-25T01:22:01.467000+00:00 | Last Updated: 2026-03-25T02:56:50.065565+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Initiator of the production deployment planning; has scheduling authority.
*   **Sneha Parab:** Participant providing availability constraints and conflict reporting.
*   **Onkar Bamane:** Identified participant in the thread (no specific action logged).
*   **Daryl:** Participant with conflicting schedule and travel plans.

**Main Topic**
Coordination and rescheduling of the "Production Deployment Planning Session" to accommodate team member availability.

**Decisions Made**
*   The production deployment planning session time has been officially moved from its original slot to **11:00 AM**.

**Pending Actions & Ownership**
*   **No specific pending action items** were generated in this conversation snippet. The primary request (scheduling) was resolved immediately.
*   *Note:* Prajney Sribhashyam indicated they would provide deployment details once the session began, but no new task was created for follow-up after the time change.

**Key Dates & Follow-ups**
*   **Date:** March 25, 2026.
*   **Meeting Time:** 11:00 AM (Confirmed).
*   **Conflicts Avoided:**
    *   Sneha Parab and Daryl have a conflicting meeting at 1:00 PM.
    *   Daryl is unavailable for the entire day due to attendance at the "Project Light session."

**Summary of Discussion Flow**
Prajney Sribhashyam announced an upcoming production deployment planning session. Onkar Bamane was tagged in a follow-up query regarding this announcement. Sneha Parab proposed moving the meeting to 11:00 AM to avoid a 1:00 PM clash and Daryl's unavailability due to the Project Light session. Prajney confirmed the change to 11:00 AM immediately, concluding the discussion with confirmation from Sneha.


## [22/32] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Messages: 18 | Last Activity: 2026-03-25T01:06:41.222000+00:00 | Last Updated: 2026-03-25T02:57:08.246445+00:00
**Daily Work Briefing: Nikhil Grover & Michael Bui**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator; reporting anomalies in product ad ranking and event data fidelity.
*   **Michael Bui:** Technical Lead (Engineering); unavailable for immediate deep-dive due to illness and meetings.
*   **Norman & Flora:** Designated resources for Frontend (FE) investigation per Michael's instruction.

**Main Topics**
1.  **Ad Delivery Inconsistency & Deployment Impact:**
    *   **Store ID Status:** Re-evaluated as a potential edge case by Nikhil Grover, though Michael Bui previously requested further investigation into Store ID 17 vs. 165 mismatches blocking dynamic slots.
    *   **OSMOS Data Sync:** Confirmed as manual; no automatic sync exists. Ram previously facilitated updates combining data from Michael and Calvin.

2.  **Critical Anomaly: Product Ad Rank & Event Fidelity (March 24):**
    *   **Ranking Disorder:** Segment data revealed erratic ranking orders on homepage swimlanes (ranks 4, 9, and 1).
    *   **Missing Metadata:** Event logs are missing the `Ad ID` field entirely.

**Decisions Made & Status Updates**
*   **Investigation Path Shifted:** Due to Michael Bui's unavailability, the investigation into wrong event details has been redirected from him to the Frontend team (Norman and Flora).
*   **LLM/Metadata Review:** Nikhil Grover is tasked with checking what data is sent from FE apps regarding the missing `Ad ID` and rank issues.

**Pending Actions & Owners**
*   **Frontend Data Verification (Nikhil Grover):** Check specific payloads sent from FE applications to diagnose the missing `Ad ID` and ranking anomalies.
*   **Availability Constraint (Michael Bui):** Michael is in full-day meetings this week and may not respond quickly; he previously cited a bad headache on March 24 as a reason for delay.
*   **Store List Refresh (Nikhil Grover):** Investigate OSMOS store list refresh logic and verify if updates should occur strictly upon new store launches.

**Key Dates & Deadlines**
*   **March 25, 2026:** Nikhil Grover sent a follow-up at 01:04 UTC requesting information availability; Michael responded at 01:06 UTC regarding his schedule and redirecting the query to Norman and Flora.
*   **Original Launch Window (March 19–20):** Status remains suspended pending resolution of Store ID impact and the newly discovered ranking events.

**Historical Context Note**
Previous discussions established readiness for dynamic slots UAT with resolved `[1,3,3,5]` logic. Focus shifted to a critical ad delivery anomaly (Store ID mismatch) on March 19–20. On March 24, the narrative evolved: while OSMOS sync was confirmed as manual and the Store ID issue downgraded by Nikhil Grover as an edge case, Michael Bui maintained the need for further investigation. Later that afternoon, the scope expanded when Nikhil Grover identified a new critical failure in product ad placements on homepage swimlanes, characterized by random ranking orders (1, 4, 9) and missing `Ad ID` fields in Segment events. On March 25, Michael Bui's inability to investigate immediately due to health and meetings necessitated a pivot to checking FE app data directly.


## [23/32] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Messages: 2 | Last Activity: 2026-03-25T00:03:09.772000+00:00 | Last Updated: 2026-03-25T02:57:34.931039+00:00
**Daily Work Briefing Summary (Updated: March 25, 2026)**

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
*   **Inbox Status:** As of March 25, 2026, the workspace inbox is fully caught up across all categories (**Urgent Action Items**, **High-Volume/Project Themes**, **Meeting Updates**, and **FYI**). No pending unread items require immediate attention. This status was confirmed in daily summaries dated March 24 and March 25, 2026.

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

**Note on New Content:** Daily summaries received on March 24 and March 25, 2026, confirm the inbox remains clear of urgent action items, meeting updates, and FYI notices. No changes to pending actions or decisions were required based on these updates.


## [24/32] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Messages: 16 | Last Activity: 2026-03-24T23:01:22.839000+00:00 | Last Updated: 2026-03-25T02:58:02.818250+00:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
Automated alerts for the production environment (`env:prod`) continue to show instability in Mirakl integration and recurring latency issues extending from March 17 through March 24. The `fni-order-create` service exhibits a persistent cycle of DBP fetch failures, API errors, and route exceptions, with a notable escalation on **March 24**. Concurrently, `picklist-pregenerator` shows critical latency spikes recorded previously and updated today.

**Incident Summary & Timeline (2026-03-15 to 2026-03-24)**
*   **Service:** `fni-order-create` (Mirakl Integration) – **Escalated Recurrence on Mar 24**
    *   **Pattern Continuation:** Instability spans March 17–24. A new intensive burst occurred on **March 24**.
    *   **Morning Incident (Mar 24, ~13:04 UTC):** Previously noted triggers and recoveries for "Exception Occurred At Mirakl Route" and "Error while calling APIs" (~5 mins).
    *   **Evening Incident (Mar 24, 18:49–20:04 UTC):** Four distinct error types triggered in rapid succession:
        *   *Window 1:* 18:49–18:55 UTC. Triggered "Failure occurred during fetching orders from DBP", "Error while calling APIs", "Failure occurred during fetching orders", and "Exception Occurred At DBP Route". All recovered by 18:55 UTC (duration ~6 mins).
        *   *Window 2:* 19:59–20:04 UTC. Identical error set triggered again. Recovered by 20:04 UTC (duration ~5 mins).

*   **Service:** `seller` (`picklist-pregenerator`) – **Recurring Latency**
    *   **Cycle (Mar 20):** P2 warning with metric value **3611.453s**.
    *   **Cycle (Mar 23):** New P2 warning triggered at **23:01:22 UTC** with metric value **3607.424s** (Monitor ID `20383097`).
    *   **Latest Update (Mar 24, ~23:01 UTC):** A new P2 warning triggered for the same service (`picklist-pregenerator`) detecting excessive completion time. The metric value recorded was **3607.798s**. Monitor ID `20383097` confirms this is a recurring pattern within the `seller-experience` tribe.

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of expanded Mirakl integration instability affecting `fni-order-create`. The pattern now includes multiple recurrence windows on March 24 alone (two distinct clusters at ~13:00 and ~19:00 UTC), alongside the Mar 17–23 history.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Investigate root cause of extreme latency spikes in `picklist-pregenerator`. Cycles occurred on March 20, March 23 (3607.424s), and **March 24 (3607.798s)**. The recurrence confirms a persistent issue with job processing completion times exceeding 3600s.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Review Monitor `29851723` logic for Apple Pay/Google Pay transactions following the March 23 test alert indicating potential false positives.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Summary for Leadership**
Mirakl integration instability (`fni-order-create`) has persisted across eight consecutive days (March 17–24). On March 24, the service exhibited a severe escalation with **four separate incident windows**, including two major clusters at ~13:04 UTC and ~19:00 UTC. Each evening cluster involved simultaneous triggers of DBP fetch failures, API errors, and route exceptions, resolving within 5–6 minutes. Concurrently, `picklist-pregenerator` shows a continuous cycle of critical latency spikes on March 20 (3611s), March 23 (3607s), and **March 24 (3607.798s)**. These systemic failures in Mirakl, SAP, and job processing logic require urgent engineering review to stabilize production performance.

**Resource:** fairnex-datadog-notification
**Metadata:** { "message_count": 118, "url": "https://chat.google.com/space/AAAA8dv5lp0" }


## [25/32] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Last Activity: 2026-03-24T16:29:57.301000+00:00 | Last Updated: 2026-03-24T22:42:03.965742+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Mar 24, 16:30 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-discovery`.
*   **Escalations:** `@hangouts-GT-Search-DatadogAlerts`, `@oncall-dpd-staff-excellence-pdm`, `@hangouts-GT-Discovery-DatadogAlerts`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Search Indexing.

**Main Topic**
**CRITICAL ALERT (P2):** The `fp-search-indexer` service remains in a **P2 Error State** on production. Despite transient recoveries noted previously, the service has re-triggered as P2 multiple times since Mar 18, most recently on Mar 24 at 16:29 UTC.

**Pending Actions & Ownership**
*   **Action:** **URGENT INVESTIGATION:** Address critical errors on `fp-search-indexer` (env: prod).
    *   **Owner:** Product Data Management On-Call (`@oncall-dpd-staff-excellence-pdm`).
    *   **Status:** Active since Mar 18. Re-triggered Mar 23, 01:46 UTC and again on **Mar 24, 16:29 UTC**. No resolution achieved.
    *   **Required Checks:** Review Datadog logs (`trace.http.request.errors`), inspect K8s deployment (`fpon-cluster/default/fp-search-indexer`), consult Runbook (Jira SR-2001831558).

*   **Action:** Investigate `go-catalogue-service` latency flapping.
    *   **Owner:** Discovery Team (`@hangouts-GT-Discovery-DatadogAlerts`).
    *   **Status:** Flapping pattern observed on Mar 23. Triggered at 07:42 UTC, recovered 12:43 UTC, triggered again 13:06 UTC, and recovered at 14:09 UTC (P90 dropped to 0.149s). Monitor ID `17447968`.

*   **Action:** Monitor `sku-store-attribute` job stability.
    *   **Owner:** DPD Grocery Discovery Team (`@hangouts-dd-dpd-grocery-alert`).
    *   **Status:** Persistent instability observed Mar 23–24. Multiple trigger/recovery cycles occurred between Mar 23, 01:03 UTC and Mar 24, 01:01 UTC due to <6 processed files (Monitor ID `20382848`).

*   **Action:** Investigate SAP Data Sync volume anomalies.
    *   **Owner:** Product Data Management Team (`@opsgenie-dpd-grocery-discovery`).
    *   **Status:** Triggered Mar 20, 01:01 UTC (P3). Alerts indicate >2000 files received/stored daily for `fpon-sap-jobs-file-parser`. No recent updates noted.

**Decisions Made**
*   The `fp-search-indexer` failure is confirmed persistent and recurrent; previous "resolved" statuses were temporary or invalid. Immediate root cause analysis is required.
*   `go-catalogue-service` latency issues exhibit a flapping pattern (trigger/recover cycles) over a short window on Mar 23, requiring correlation with traffic volumes.
*   `sku-store-attribute` shows frequent oscillation between alert and recovery states; further investigation into job dependencies is needed to stop the loop.

**Key Dates & Follow-ups (Mar 16–24, 2026)**
*   **Service: `fp-search-indexer` (P2 - Product Data Management) [ACTIVE CRITICAL]**
    *   *Latest Timeline:* Active since Mar 18; re-triggered **Mar 23, 01:46 UTC** and **Mar 24, 16:29 UTC**.
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/17447691) | [Runbook](https://ntuclink.atlassian.net/wiki/spaces/SR/pages/2001831558/Support+Run+book).
*   **Service: `go-catalogue-service` (P3 - Discovery) [FLAPPING]**
    *   *Issue:* P90 latency > 500ms on `get_/search`.
    *   *Latest Timeline:* Last resolved at Mar 23, 14:09 UTC. Monitor ID: `17447968`.
*   **Service: `sku-store-attribute` (P3 - Grocery Discovery) [FLAPPING]**
    *   *Issue:* <6 processed files in 4h.
    *   *Latest Timeline:* Multiple trigger/recovery cycles observed Mar 23–24, with the last recovery at 01:01 UTC Mar 24. Monitor ID: `20382848`.
*   **Service: `fpon-sap-jobs-file-parser` (P3 - Product Data Management)**
    *   *Issue:* Excessive file volume (>2000/day). Triggered Mar 20, 01:01 UTC.

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c


## [26/32] BCRS - UAT
Source: gchat | Group: space/AAQACfHCuNI | Last Activity: 2026-03-24T11:44:49.961000+00:00 | Last Updated: 2026-03-24T14:36:46.741885+00:00
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


## [27/32] Ping Pong 🏓
Source: gchat | Group: space/AAQAnryjAA8/cFKeWJ-k288 | Last Activity: 2026-03-24T10:42:04.599000+00:00 | Last Updated: 2026-03-24T14:37:00.696439+00:00
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


## [28/32] Ping Pong 🏓
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


## [29/32] QE <-> All Tribes
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


## [30/32] DPD x Platform Engineering
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


## [31/32] Soo Ngee Tong
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


## [32/32] QE <-> All Tribes
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
