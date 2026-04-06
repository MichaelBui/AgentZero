

## [1/30] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Messages: 1 | Last Activity: 2026-04-06T02:34:20.549000+00:00 | Last Updated: 2026-04-06T02:42:42.388605+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Sneha Parab:** Lead/Manager; coordinating cross-team support, SAP/API integration blockers. Recently queried B2B user blocking logic for migrated customers.
*   **Michael Bui:** Engineering/RMN Architect; identified root cause for RMN incident and preparing UAT verification. Seeking alignment on opening the "Project Light" Confluence space widely.
*   **Daryl Ng:** Investigating store network ownership and Omni Home data discrepancies. Flagged Linkpoints eligibility issue (April 1). Inquired about learning budget (Sundy's course) and S&G Store Enabling SOP adherence. Currently replying to B2B blocking use case discussion.
*   **Alvin Choo:** Leadership; addressing approval workflows for weekend deployments. Consulted regarding Sundy's training budget inquiry and Project Light alignment.
*   **Gopalakrishna Dhulipati:** On Child Care Leave until Wednesday (April 2). Will reach out individually if assistance is required to rep tasks.

**Main Topics & Updates**
1.  **RMN Incident & Deployment Status:** Michael Bui identified the root cause and implemented a fix. Daryl Ng confirmed active inquiry regarding deployment status on March 31 (01:44 UTC). Immediate guidance remains required on weekend (Sat/Sun) deployment protocols, requiring an approval request to Hui Hui.
2.  **Project Light Confluence Access (New):** On April 6 at 02:34 UTC, Michael Bui requested guidance from Alvin Choo and Gopalakrishna Dhulipati regarding whether the "Project Light" Confluence space (`https://ntuclink.atlassian.net/wiki/spaces/LIGHT/overview`) should be opened widely or aligned internally first.
3.  **Linkpoints Eligibility Issue:** On April 1 at 03:13 UTC, Daryl Ng flagged that Wei Sing's team enabled "Linkpoints eligible" in SAP, but it remains disabled in DBP. Investigation is underway.
4.  **Search Performance Drop:** Investigation continues regarding the severe 60–70% impression decline since March 18/19. The RMN root cause fix may correlate with these symptoms; release timing remains contingent on this investigation and UAT success.

**Pending Actions & Owners**
*   **Project Light Access Decision:** Determine if the Confluence space should be opened widely or aligned internally first. (Owner: Alvin Choo/Gopalakrishna Dhulipati; Coordinator: Michael Bui)
*   **RMN Deployment Verification:** Confirm if the fix has been deployed following Daryl Ng's inquiry and proceed with UAT verification. Send approval request to Hui Hui for weekend deployment if applicable. (Owner: Michael Bui; Coordination: Alvin Choo/Hui Hui/Daryl Ng)
*   **Linkpoints Investigation:** Verify why "Linkpoints eligible" is disabled in DBP despite SAP enablement by Wei Sing's team. Follow up with Daryl Ng/Sneha Parab. (Owner: To be assigned/Wei Sing's team; Coordination: Sneha Parab/Daryl Ng)
*   **B2B Logic Feasibility:** Evaluate technical possibility of blocking migrated users from B2B orders based on identification logic. (Owner: Engineering Team; Discussion Owner: Daryl Ng/Sneha Parab)
*   **SOP Adherence Confirmation:** Clarify current status of the S&G Store Enabling SOP to address Daryl Ng's query. (Owner: To be assigned; Coordination: Sneha Parab/Daryl Ng)
*   **Training Budget Check:** Confirm availability of learning budget for Sundy's course request. (Owner: Alvin Choo/Sundeep's team lead)
*   **Epic Closure Validation:** Determine if DPD-710 can be closed given the March 19 live date discrepancy. (Owner: Michael Bui; Requestor: Sneha Parab)
*   **SIT Delivery Assessment:** Evaluate KT feasibility to complete SIT before April 6/7. (Owners: Michael Bui/Daryl Ng)
*   **Store Network Ownership:** Confirm scope under Data COE vs. Miguel's team regarding `Omni Home` store ID mismatch (OMNI-1157). (Owner: Daryl Ng/Michael Bui)
*   **SAP Timeline Resolution:** Resolve deposit SKU data integration blockers. *Note: Gopalakrishna Dhulipati is on leave until Wednesday; individual rep requests will be made if needed.* (Owners: Sneha Parab/Alvin Choo/Gopalakrishna Dhulipati)
*   **RAW Forms Review:** Complete Risk Register review for DPD RAW forms; confirm handovers and renew expired forms by Tomorrow EOD. (Owner: All Leads/Sazali Bin Mohammed Ali's team)

**Decisions Made & Status Changes**
*   **RMN Deployment Inquiry:** Daryl Ng raised a query on March 31 regarding the deployment status of the RMN fix, indicating active monitoring of the release phase.
*   **Linkpoints Discrepancy (New):** SAP enablement by Wei Sing's team does not reflect in DBP status; root cause analysis required.
*   **Release Strategy:** Regular app release status remains pending the search performance investigation and confirmation of the current deployment status (per Daryl Ng's check).
*   **Architecture Updates:** Michael Bui has updated current, future, and transition architecture diagrams.
*   **Confluence Access Request (New):** Awaiting leadership decision on Project Light space visibility as of April 6.
*   **Staffing Update:** Gopalakrishna Dhulipati is on Child Care Leave until Wednesday; active engagement for task reassignment will be initiated by him directly.

**Key Dates & Deadlines**
*   **RAW Forms Review:** Due Tomorrow EOD.
*   **Gopalakrishna Dhulipati Leave:** Until Wednesday, April 2 (Child Care Leave).
*   **Adrian Redelivery Block:** Unavailable Apr 1–7 due to duplicate posting risks.
*   **SIT Target:** Potential delivery by April 6/7 contingent on KT success.
*   **Chee Hoe Support:** Effective end of March for Product Catalogue/MarTech scope.
*   **DPD-710 Live Date:** March 19, 2026 (Subject to validation).


## [2/30] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 17 | Last Activity: 2026-04-06T02:32:57.314000+00:00 | Last Updated: 2026-04-06T02:43:16.150825+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (Updated April 6, ~02:35 UTC)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
Cyclical instability continues from April 1 through early morning on April 6. The incident remains active with a sharp increase in frequency overnight (April 5 ~22:30 to April 6 ~02:35 UTC). Failures now affect Identity (`engage-my-persona-api-go`), Orchid frontend, and newly impacted Gamification services, alongside persistent latency spikes in identity update endpoints.

**Status Summary & Timeline (Updated: ~02:35 UTC)**
*   **Identity API Instability (`squad:dynamics`):**
    *   *Error Rate:* Recurring high error rates (>0.1%) triggered frequently between 01:25 and 02:35 UTC. Notable triggers occurred at **01:35** (0.102%), **01:42** (0.104%), **02:01** (0.121%), and **02:26** (0.101%).
    *   *Latency:* P90 latency for `patch_/user/profile` spiked to **1.948s** (threshold >1.8s) at **02:09 UTC**. P90 latency for `post_/new-myinfo/confirm` breached threshold (**1.802s**) at **02:32 UTC**. Previous spikes noted at 21:42 UTC (phone update).
*   **Orchid Frontend (`squad:journey`):**
    *   *Success Rate:* Intermittent dips (<99.9%) triggered repeatedly between 01:25 and 02:35 UTC. Recent values include **01:42** (99.679%) and **02:26** (99.875%).
*   **Gamification Service (`squad:dynamics`):**
    *   *Error Rate:* New instability detected with a high error rate trigger at **02:15 UTC** (Value: 0.917%), resolving by 02:25 UTC.
*   **Android App (`squad:compass`):**
    *   No new triggers reported in the latest window; stability remains consistent since last alert on April 5 at 13:54 UTC.

**Pending Actions & Ownership**
*   **Investigate Identity Service Fluctuations:** Analyze rapid recurrence of error rates (~0.1–0.12%) and latency spikes on `engage-my-persona-api-go` (specifically profile updates and MyInfo confirmations). Owner: **Squad Dynamics**.
*   **Monitor Orchid Stability:** Investigate recurring success rate dips for `frontend-gateway`. Owner: **Squad Journey**.
*   **Investigate Gamification Errors:** Analyze the cause of the 0.917% error spike on `gamification-api` at 02:15 UTC to prevent recurrence. Owner: **Squad Dynamics**.

**Decisions Made**
*   **Status Update:** Incident severity remains Critical. The timeline has extended into April 6 with intensified activity in the last two hours, characterized by a "burst" pattern of alerts across multiple services.
*   **Pattern Confirmation:** Error rate triggers for `engage-my-persona-api-go` are now occurring every ~5–10 minutes (vs. 15–20 mins previously), and latency thresholds have shifted from phone updates to profile/MyInfo endpoints.

**Key Dates & Follow-ups**
*   **Active Window:** April 1, 09:58 – April 6, ~02:35 UTC (Latest Activity).
*   **Reference Links (Latest):**
    *   `gamification-api` Error Rate Monitor #92939290 (Triggered: 02:15 UTC, Value: 0.917)
    *   `engage-my-persona-api-go` P90 Latency Monitor #17447638 (Triggered: 02:09 UTC, Value: 1.948s)
    *   `frontend-gateway` Orchid Success Rate Monitor #17448311 (Latest Trigger: 02:26 UTC, Value: 99.875%)


## [3/30] RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Messages: 36 | Last Activity: 2026-04-06T02:30:42.402000+00:00 | Last Updated: 2026-04-06T02:43:50.227294+00:00
**Daily Work Briefing: Automated Test Results Summary (RMN Notification)**

**Key Participants & Roles**
*   **Collection Runner App:** Automated testing agent executing API suites.
*   **Webhook Bot:** Reporting mechanism; consistently returning "unable to process your request" on all notifications from March 12 through April 6, 2026.
*   **Parties Involved:** System-generated notification log only.

**Main Topic/Discussion**
Automated nightly API test executions across `promo-service`, `marketing-personalization-service`, and `marketing-service` in the **staging** environment. Monitoring period spans March 12 through **April 6, 2026**. Execution windows occur at approximately 01:05 UTC (morning), 02:31 UTC (midnight), and **03:21 UTC** (early morning).

**Test Execution Status & Anomalies**
*   **`marketing-service`:** Regression confirmed.
    *   **April 6, 01:05 UTC:** Contract tests passed (20 Passed / 0 Failed); API Tests failed with **3 failures** (44 Passed). This confirms a persistent instability issue extending the problematic window previously seen March 17–25 and April 2–3. The service has now failed on consecutive mornings at 01:05 UTC (April 3, 4, 5, and 6).
*   **`promo-service`:** Confirmed stable on **April 6 at 02:30:42 UTC**.
    *   **[API Contract Tests]:** 6 Passed / 0 Failed / 0 Skipped (Total Requests: 3).
    *   **[API Tests]:** 10 Passed / 0 Failed / 0 Skipped.
*   **`marketing-personalization-service`:** No log recorded for April 6 execution window at 03:21 UTC in the latest feed; previous runs (April 5) were stable.

**Pending Actions & Ownership**
*   **Webhook Bot Remediation (High Priority):** The bot failed to process requests in every notification cycle from March 12 through the latest log on **April 6**. Immediate attention is required from DevOps or Automation Infrastructure to resolve the persistent "unable to process" error.
*   **Investigate `marketing-service` Regression:** Engineering must analyze the root cause of the recurring API test failures (3 failures) observed on April 4, 5, and **6** at 01:05 UTC. The issue persists without resolution, indicating a critical systemic or code regression.

**Decisions Made**
*   No human decisions recorded; all entries are automated system outputs.

**Key Dates & Deadlines**
*   **Failure Window (Historical):** Instability noted March 12–13 and persistently from **March 17 through March 25**. Recent recurrence began April 2, continuing through **April 6**.
*   **Current Status:** Continuous failure in `marketing-service` API tests on April 4, 5, and 6. Other services remain stable for the latest check.
    *   `marketing-service`: Failed API tests at 01:05 UTC on April 4, 5, and 6.
    *   `promo-service`: Passed at 02:30 UTC on April 6.
*   **Monitoring Period:** Data covers runs from **March 12, 2026**, through **April 6, 2026**.

**Resource Info**
*   **Message Count:** Updated to reflect notifications through April 6 (Total: 243).
*   **URL:** https://chat.google.com/space/AAQA85dw4So


## [4/30] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/8zAYSPGGpFE | Messages: 3 | Last Activity: 2026-04-06T02:30:12.149000+00:00 | Last Updated: 2026-04-06T02:44:10.769723+00:00
**Daily Work Briefing: Project Light Documentation**
**Channel:** [Internal] (Ecom/Omni) Digital Product Development
**Date:** April 6, 2026
**Link:** https://chat.google.com/space/AAQAUbi9szY

**Key Participants & Roles**
*   **Akash Gupta:** Initiator; responsible for engineering documentation space setup and maintenance.
*   **Michael Bui:** Notified stakeholder regarding link updates (specifically tagged in conversation).

**Main Topic**
Establishment and configuration of the centralized Confluence space for "Project Light" to serve as the single source of truth for Design, API Specifications, and Integration documentation.

**Decisions Made**
*   **Platform Consolidation:** The engineering team will utilize the dedicated Confluence space at `https://ntuclink.atlassian.net/wiki/spaces/LIGHT/overview` exclusively for all Project Light technical documentation (Design/API Spec/Integration docs).
*   **Link Verification:** Akash Gupta identified an initial URL error, updated the reference, and confirmed the correct link on the same day.

**Pending Actions & Ownership**
*   **Adoption of New Space:** The engineering team must transition all relevant Project Light documentation to the new Confluence space. *Owner: Engineering Team.*
*   **Link Awareness:** Michael Bui was explicitly notified of the updated URL to ensure immediate access to the correct resources. *Owner: Akash Gupta (Notification sent); Michael Bui (Acknowledgement expected).*

**Key Dates & Follow-ups**
*   **April 6, 2026 @ 02:24 UTC:** Initial announcement made by Akash Gupta regarding the new space creation.
*   **April 6, 2026 @ 02:30 UTC:** Link corrected and re-posted; Michael Bui tagged for awareness.

**Summary of Activity**
Akash Gupta initiated the documentation workflow for Project Light by creating a dedicated Confluence space. Upon realizing the initial link required adjustment, he immediately updated the URL and ensured Michael Bui was notified to prevent access issues. The channel is now active for technical specification storage, pending team adoption.


## [5/30] Akash Gupta
Source: gchat | Group: dm/4lXABkAAAAE | Messages: 6 | Last Activity: 2026-04-06T02:28:59.242000+00:00 | Last Updated: 2026-04-06T02:44:26.798749+00:00
**Daily Work Briefing: Project Light Space Migration**

**Key Participants & Roles**
*   **Michael Bui:** Initiator of the space migration; managing access permissions.
*   **Akash Gupta:** Recipient of the new workspace invitation; owner of the temporary chat room used for transition.

**Main Topic**
Discussion regarding the creation and onboarding process for a dedicated Jira Confluence space for "Project Light," including troubleshooting access issues and determining the communication channel for ongoing collaboration.

**Decisions Made**
*   **Workspace Migration:** The team agreed to shift all Project Light discussions from the current Google Chat thread to a new, specific Atlassian Confluence space (`https://ntuclink.atlassian.net/wiki/spaces/LIGHT/overview`).
*   **Access Resolution:** Michael Bui granted Akash Gupta immediate access rights after an initial failure.
*   **Channel Cleanup:** It was decided that the temporary Google Chat room created by Akash for this transition should be deleted to prevent wide publication before it is ready.

**Pending Actions & Ownership**
1.  **Delete Temporary Room:** Michael Bui requested the deletion of the Google Chat room (`https://chat.google.com/room/AAQAUbi9szY/8zAYSPGGpFE/8zAYSPGGpFE?cls=10`). *Owner: Akash Gupta* (implied by context "can comment in my thread to use this space instead" followed by Michael's request to delete it, though Michael also stated he wasn't sure if they wanted to publish it widely).
2.  **Adopt New Wiki:** Both participants are expected to utilize the new Confluence overview page for future Project Light documentation and comments.

**Key Dates & Follow-ups**
*   **Date:** April 6, 2026 (UTC timestamps provided: 02:26 – 02:28).
*   **Context Note:** The conversation occurred during early morning hours (UTC), suggesting work spanning time zones.

**Specific References**
*   **New Space URL:** `https://ntuclink.atlassian.net/wiki/spaces/LIGHT/overview`
*   **Old/Temporary Room URL:** `https://chat.google.com/room/AAQAUbi9szY/8zAYSPGGpFE/8zAYSPGGpFE?cls=10`
*   **Project Name:** Project Light


## [6/30] @ecom-ops #standup - Apr 6
Source: gchat | Group: space/AAQAZZrQINg | Messages: 1 | Last Activity: 2026-04-06T02:27:23.735000+00:00 | Last Updated: 2026-04-06T02:44:36.279725+00:00
**Daily Work Briefing: @ecom-ops #standup (Apr 6)**

**Key Participants & Roles**
*   **Gautam Singh:** Team Member/Operator (Context suggests involvement in operations or data management).
*   *Note: The channel includes 8 total members, but only Gautam Singh posted.*

**Main Topic/Discussion**
*   Update regarding Gautam Singh's availability and schedule for a specific task involving "Data migration DSM."

**Pending Actions & Ownership**
*   **Action:** Leave the current meeting or disconnect from the channel.
*   **Owner:** Gautam Singh.
*   **Timing:** 10:30 (Timezone not specified in source, assumed local or UTC based on message timestamp).
*   **Context:** The departure is specifically to attend to "Data migration DSM."

**Decisions Made**
*   No formal decisions were recorded; the message serves as a status update regarding attendance.

**Key Dates & Deadlines**
*   **Date:** April 6, 2026.
*   **Time:** Message posted at 02:27:23 UTC. Planned departure at 10:30.
*   **Follow-up:** None explicitly stated; the action is a departure rather than a scheduled follow-up meeting.

**Summary of Conversation Flow**
Gautam Singh initiated the conversation by stating his intention to drop off from the chat/meeting at 10:30 AM on April 6, 2026, to focus on "Data migration DSM." The post was viewed by one other member out of eight channel participants. No further responses or questions were recorded in this log.


## [7/30] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Messages: 6 | Last Activity: 2026-04-06T02:24:01.244000+00:00 | Last Updated: 2026-04-06T02:45:13.890230+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Key Participants & Roles**
*   **Sneha Parab:** BCRS/Fees/Store Closure Impact Lead.
*   **Akash Gupta:** IMS availability/UAT stock sourcing, B2B SKU sync queries, DBP access coordination.
*   **Wai Ching Chan:** Order Service Deployment/Slot Logic Validation / UAT Stock updates.
*   **Michael Bui:** BCRS Deposit Logic/SAP Integration/Publisher of PRs.
*   **Daryl Ng:** Backoffice/Order Management/Bug Reporting / Slot Logic validation / SOH Sourcing / DBP/Jira inquiries.
*   **Andin Eswarlal Rajesh:** Frontend (iOS/Android) & BCRS UX queries / Amplitude tracking.
*   **Lester Santiago Soriano:** Backend Services Lead.
*   **Zaw Myo Htet:** Payment/Feature Flagging / Pre-order Voucher Logic.
*   **Shiva Kumar Yalagunda Bas:** Slot discrepancy reporting.
*   **Gopalakrishna Dhulipati & Dang Hung Cuong:** Address emoji validation.
*   **Alvin Choo:** Announced annual planning meeting for Apr 2, 9:30 AM.
*   **Yangyu Wang:** Tagged regarding split flag issues; reported iOS Instore page issue.

**Main Topics Discussed**
1.  **DBP Access & Documentation (New):** On Apr 6 at 01:36 UTC, Daryl Ng requested the Jira link to raise DBP access tickets. Later that day, Akash Gupta established a new Confluence engineering space for "Project Light" (`https://ntuclink.atlassian.net/wiki/spaces/LIGHT/overview`) for Design/API Spec/Integration docs.
2.  **API Source Identification (New):** On Apr 6 at 01:41 UTC, Daryl Ng queried the origin of a specific API endpoint requiring further investigation by the backend team.
3.  **HPWP Serviceable Area Routing Issue:** On Apr 2 at 08:10 UTC, Daryl Ng reported Parkway postal codes routing incorrectly to HCBP instead of HPWP. Akash Gupta and Wai Ching Chan have been tagged for access verification and investigation.
4.  **Unit Price Calculation Compliance:** On Mar 31, Lester highlighted a government compliance requirement for Phase 2 unit price calculations. Current reliance on parsing `display_units` is unscaleable. Proposed solution involves ingesting structured fields (`pack_size`, etc.) from Mirakl/SAP into DBP. Sneha Parab requested an effort assessment.
5.  **iOS Instore Page Regression:** On Apr 1 at 04:14 UTC, Yangyu Wang reported a functional issue on the iOS instore page (Android unaffected). Andin Eswarlal Rajesh is investigating.
6.  **BCRS Stock Sourcing for Sign-off:** On Apr 2 at 02:54 AM, Daryl Ng requested adding Stock on Hand (SOH) for product ID `1152196` in "1HD" store (Store ID: 768). Wai Ching Chan is handling this for Finance sign-off.
7.  **Pre-order Voucher Payment Logic:** On Apr 2 at 03:14 AM, Zaw Myo Htet queried app voucher charging logic for in-store pickups. Wai Ching Chan is addressing queries on sales and voucher cost posting.
8.  **BCRS Deposit Logic Failure:** On Mar 30, Wai Ching Chan reported missing deposit values during UAT checkout. Sundy Yaputra is investigating this regression.
9.  **Slot Date Discrepancy:** Shiva Kumar Yalagunda Bas reported a delivery slot mismatch (UI shows 25th, API indicates 23rd). Daryl Ng and Sundy Yaputra are resolving this.
10. **Omni Home Split Flag Regression:** On Mar 31 at 02:27 UTC, Daryl Ng reported that Omni home swimlanes fail to follow the split flag due to backend default setting updates.

**Pending Actions & Ownership**
*   **Daryl Ng:** Follow up on DBP access request and identify the source API for recent queries (New).
*   **Akash Gupta:** Coordinate DBP access requests; maintain Project Light Confluence space; verify HPWP serviceable area data.
*   **Wai Ching Chan:** Add SOH for product `1152196` in store 768; Update specific SKUs to "unlimited stock" in UAT; Clarify pre-order voucher posting logic.
*   **Sundy Yaputra:** Investigate missing BCRS deposit values in UAT checkout and resolve slot date mismatch (UI vs API).
*   **Akash Gupta, Michael Bui, Andin Eswarlal Rajesh:** Provide immediate inputs on BCRS tickets DPD-637 and DPD-807 to close the epic.
*   **Lester Santiago Soriano / Sneha Parab:** Assess effort for mapping structured unit price fields from Mirakl/SAP.
*   **Andin Eswarlal Rajesh:** Investigate iOS instore page regression reported by Yangyu Wang.
*   **Daryl Ng:** Review Michael Bui's PR #7 (`bcrs-deposit-posting`) and investigate Omni home split flag issue with Nikhil and Yangyu Wang.

**Decisions Made**
*   **Unit Price Structure:** Move from parsing `display_units` to utilizing structured fields for Phase 2 compliance.
*   **BCRS Epic Priority:** Immediate action required to close the BCRS epic; ticket status must be verified for DPD-637 and DPD-807.
*   **UAT Stock Critical:** Specific SKUs identified by Sneha Parab must be set to unlimited stock immediately. Product `1152196` requires SOH in store 768.
*   **iOS Issue:** Investigation initiated into iOS-specific instore page failure.
*   **Documentation Standard:** All Design/API Spec/Integration docs for Project Light are now centralized on the new Confluence space (Akash Gupta).

**Key Dates & Deadlines**
*   **Mar 30, 2026:** B2B sync clarity requested; UAT stock updates required; BCRS deposit failure reported.
*   **Mar 31, 2026:** Unit price compliance discussion initiated; Omni home split flag regression reported.
*   **Apr 2, 2026 (Today):** Annual planning meeting scheduled for 9:30 AM (Host: Alvin Choo); HPWP routing issue flagged at 08:10 UTC.
*   **Apr 6, 2026:** DBP access query and API source identification raised (New).

**Note on Historical Context:** Previous mentions of code review priorities for `layout-service` PR #362 are superseded by the urgent Strudel SDK deployment update (`go-platform-website`). Current focus includes investigating UAT BCRS deposit regression, updating UAT stock levels, resolving slot date mismatches, closing the BCRS epic via tickets DPD-637 and DPD-807, debugging the Omni home split flag configuration, assessing structured unit price field ingestion, troubleshooting the new iOS instore page regression, clarifying pre-order voucher payment posting logic, verifying HPWP serviceable area routing, and establishing Project Light documentation standards.


## [8/30] Jacob, Sathya, Daryl, Tiong Siong, ...
Source: gchat | Group: space/AAQA-bdVPoA | Messages: 1 | Last Activity: 2026-04-06T02:23:00.218000+00:00 | Last Updated: 2026-04-06T02:45:32.546673+00:00
**Daily Work Briefing: Project Light Leave Planning (Updated)**

**Key Participants & Roles**
*   **Sathya Murthy Karthik:** Requester/Owner of the "Omni Leave Plans" spreadsheet; driving data collection and follow-up.
*   **Michael Bui, Daryl Ng, Tiong Siong Tee, Akash Gupta:** Team members requested to submit leave plans.

**Main Topic**
Collection of individual leave plans extending through October 2026. While a central Google Sheet was established for long-term tracking, team feedback indicates accurate planning beyond one month is difficult due to standard travel booking cycles (1–1.5 months in advance).

**Pending Actions & Ownership**
*   **Action:** Input all known leave dates into the "Omni Leave Plans" spreadsheet.
    *   **Scope Nuance:** Akash Gupta has noted that planning beyond one month is not feasible; he will update plans 1–1.5 months prior to travel.
*   **Owner:** All tagged team members (**Michael Bui, Daryl Ng, Tiong Siong Tee, Akash Gupta**).
*   **Status Update:**
    *   **Sathya Murthy Karthik:** Issued a new follow-up on April 6, 2026, at 02:23 UTC. Requested all team members to share updated leave plans (current date through October) by **EOD today**. The message was viewed by 2 of the 5 recipients.
    *   **Akash Gupta:** Previously confirmed no major leave for the next month and inability to commit to a full October 2026 schedule due to planning horizons; will provide updates closer to dates.
    *   **Michael Bui:** Confirmed leave for late March (~1 week).
    *   **Daryl Ng:** Provided initial coverage dates (Reservist duties on 30 March PM; 22–30 April) but noted long-term plans are unavailable. Committed to securing team coverage during absences.
    *   **Tiong Siong Tee:** Confirmed no long-term leave plan yet, pending update on specific leaves.

**Decisions Made**
*   A centralized Google Sheet has been designated as the single source of truth for Project Light leave planning.
*   **Revised Expectation:** While data "till Oct" is requested, participants (specifically Akash) clarified that accurate input is limited to ~1 month in advance, with long-term dates being tentative or unavailable. The April 6 request reinforces the need for immediate updates within this realistic window.

**Key Dates & Deadlines**
*   **March 18, 2026:** Initial deadline for known leave plans; Akash Gupta provided access at 03:53 UTC on this date.
*   **April 6, 2026 (02:23 UTC):** New follow-up issued by Sathya Murthy Karthik.
    *   **Deadline:** EOD today (April 6, 2026) for updated leave plans covering "now till Oct."
*   **Future Coverage Data:**
    *   Late March (~1 week): Michael Bui's confirmed leave.
    *   March 30 (PM): Daryl Ng's reservist duty.
    *   April 22–30: Daryl Ng's reservist duty.

**Reference**
*   **Document:** Omni Leave Plans (Project Light)
*   **Link:** https://docs.google.com/spreadsheets/d/1BuohjrUTREwWgj_4JNLUnu4d2c-a4VPEPWrvJJks_eo/edit?gid=0#gid=0


## [9/30] @omni-ops #standup - Apr 6
Source: gchat | Group: space/AAQAoCXidLg | Messages: 5 | Last Activity: 2026-04-06T02:19:51.797000+00:00 | Last Updated: 2026-04-06T02:45:44.775114+00:00
**Daily Work Briefing: @omni-ops #standup (April 6)**

**Key Participants & Roles**
*   **Yangyu Wang:** Standup organizer; active responder to resource requests.
*   **Daryl Ng:** Requester for immediate assistance; identified a support gap.
*   **Oktavianer Diharja:** Tagged by Yangyu Wang (likely intended as the primary responder).

**Main Topic**
The discussion centered on an urgent need for personnel support regarding a specific operational issue, triggered during the morning standup session. The thread highlights a resource bottleneck where Daryl Ng required immediate help to address a task or incident.

**Pending Actions & Ownership**
*   **Action:** Investigate and assist with the issue detailed in the shared link (Room ID: `AAQAUbi9szY/Sy2uCKMi2yc/8ApCpT-V6Ho`).
    *   **Owner:** Yangyu Wang.
    *   **Status:** Acknowledged ("Yes, checking"). Viewed by 3 of 8 participants as of the last update.

**Decisions Made**
*   No formal decisions were recorded in this specific thread. The conversation remains in an execution phase where a team member (Wang) has agreed to investigate the request raised by Daryl Ng.

**Key Dates, Deadlines, & Follow-ups**
*   **Date:** April 6, 2026.
*   **Timeline:**
    *   Standup initiated: ~02:00 UTC.
    *   Initial tag of Oktavianer Diharja: ~02:03 UTC.
    *   Resource request posted by Daryl Ng: ~02:08 UTC.
    *   Follow-up request to Yangyu Wang: ~02:19 UTC.
    *   Commitment to action: ~02:19 UTC (Wang confirmed checking).
*   **Follow-up:** Pending resolution from Yangyu Wang after reviewing the linked chat room.

**References & Links**
*   Space URL: https://chat.google.com/space/AAQAoCXidLg
*   Specific Chat Room Link cited for assistance: https://chat.google.com/room/AAQAUbi9szY/Sy2uCKMi2yc/8ApCpT-V6Ho?cls=10


## [10/30] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/YLE78JhUjDM | Messages: 16 | Last Activity: 2026-04-06T02:17:43.910000+00:00 | Last Updated: 2026-04-06T02:45:58.781153+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**
**Date:** April 6, 2026
**Channel:** [Internal] (Ecom/Omni) Digital Product Development

### Key Participants & Roles
*   **Daryl Ng:** Initiator; coordinating DBP access requests for the Ad Ops team.
*   **Michael Bui:** Provided updated Jira service desk link.
*   **Rohit Pahuja:** Subject Matter Expert (SME); clarified permissions and provided ticket reference.
*   **Hanafi Yakub:** SME; confirmed existing access logic regarding App Home vs. Whitelist Domain pages.

### Main Topic
Discussion focused on resolving technical requirements to grant the Ad Ops team access to the **Back Office DBP** system, specifically concerning the **Domain Whitelisting Module**. The team needed a valid Jira link and specific permission values to raise a service request.

### Decisions Made
1.  **Service Request Channel:** Confirmed that Ad Ops must use the General Service Request portal (Link provided by Michael Bui).
2.  **Permission Logic:** Determined that access to the "Whitelist Domain" page requires the same permissions as the "App Home" page. Hanafi Yakub confirmed that any user with App Home access can access the Whitelist Domain page without additional specific permission values.

### Pending Actions & Owners
*   **Raise Service Request:** Daryl Ng must submit a request using the ticket ID provided by Rohit Pahuja (**DSD-11065**) to grant Ad Ops DBP access.
    *   *Reference Link:* https://ntucenterprise.atlassian.net/servicedesk/customer/portal/8 (General Service Request) or specific ticket: https://ntucenterprise.atlassian.net/servicedesk/customer/portal/1459/DSD-11065?created=true
    *   *Required Permission Value:* **"App Home / Whitelist Domain"**

### Key Dates & References
*   **Date:** April 6, 2026 (All timestamps recorded between 01:36 and 02:17 UTC).
*   **Ticket ID:** DSD-11065.
*   **Service Desk URLs:**
    *   General Request: `https://ntucenterprise.atlassian.net/servicedesk/customer/portal/8`
    *   Specific Ticket: `https://ntucenterprise.atlassian.net/servicedesk/customer/portal/1459/DSD-11065?created=true`
*   **Target System:** Back Office DBP (Digital Product Development).


## [11/30] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw/mrSGCifSoS8 | Messages: 6 | Last Activity: 2026-04-06T02:01:17.646000+00:00 | Last Updated: 2026-04-06T02:46:13.366919+00:00
**Daily Work Briefing: Digital Product Development (DPD)**

**Key Participants & Roles**
*   **Natalya Kosenko:** Raised the initial cost optimization query regarding unactionable logging services.
*   **Vincent Wei Teck Lim:** Provided preliminary attribution to tablet/retail sectors and shared a Datadog query link.
*   **Jazz Tong:** Investigated potential source (Comall team new ingestion logs) and tagged Kyle Nguyen.
*   **Michael Bui:** Identified specific environment names (`fpg-retail-pos-prod`, `doriscluster`) and queried project ownership (Nova).
*   **Kyle Nguyen:** Escalated the matter to Maou Sheng Lee via direct mention.

**Main Topic**
Investigation into high Datadog logging costs (thousands of USD incurred last week) attributed to services named "be", "fe", and "N/A," which appear to lack actionable data. The discussion focuses on identifying service ownership, project affiliation, and the root cause of the data ingestion.

**Pending Actions & Ownership**
*   **Action:** Provide clarification on ownership and context for the specific logging services (`fpg-retail-pos-prod`, `doriscluster`).
    *   **Owner:** Maou Sheng Lee (tagged by Kyle Nguyen).
*   **Action:** Verify if these services belong to Project Nova.
    *   **Owner:** Unassigned (Question raised by Michael Bui, awaiting input from ownership team).

**Decisions Made**
No formal decisions were reached in this thread. The conversation concluded with the identification of potential service environments and the escalation of the issue to a senior stakeholder for clarification.

**Key Dates & Follow-ups**
*   **Date:** April 6, 2026.
*   **Incident Period:** Last week (relative to April 6).
*   **Follow-up:** Awaiting response from Maou Sheng Lee regarding the cost and ownership of the identified logs.

**Specific References**
*   **Services:** "be", "fe", "N/A".
*   **Environment/Cluster:** `fpg-retail-pos-prod`, `doriscluster`.
*   **Potential Project:** Nova.
*   **Potential Team:** Comall team.
*   **Datadog URL:** https://app.datadoghq.eu/logs?query=service%3Abe&agg_m=count&agg_m_source=base&agg_t=count&cols=trace_id%2Cservice%2Cmessage&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=asc&viz=stream&from_ts=1772846477849&to_ts=1775438477849&live=true
*   **Space URL:** https://chat.google.com/space/AAAAx50IkHw


## [12/30] Digital Signage - Network and StoreTech
Source: gchat | Group: space/AAAA1BqTEzo | Messages: 3 | Last Activity: 2026-04-06T01:57:41.266000+00:00 | Last Updated: 2026-04-06T02:46:36.606408+00:00
**Daily Work Briefing: Digital Signage Network Migration**

**Key Participants & Roles**
*   **Seng Shwu Shyan:** Requester (Initiator of SDWAN migration).
*   **Calvin Phan:** Technical Point of Contact / Escalation Owner.
*   **Daryl Ng:** Service Desk Ticket Owner (NED-195890).
*   **Steven Ng Teck Leong:** Technical Support/Network Administrator (Original context).
*   **Delwyn:** SignBox Vendor Representative (+65 8338 7829).

**Main Topic**
Migration of StoreTech digital signage from static IP configurations to DHCP as part of the transition to SDWAN. This supersedes previous discussions regarding specific static IP ranges (10.19.77.x) and MAC whitelisting for new provisioning, specifically for stores undergoing this network overhaul.

**Decisions Made & Status Updates**
*   **Migration Strategy:** All digital signage TVs in the affected stores must switch from Static IP to DHCP configuration.
*   **Scope of Affected Stores:** HJPT, HAMK, HPWP, CQ.
*   **Ownership Change:** Technical execution is no longer handled by internal Network Admins (Steven Ng Teck Leong) but delegated to the external vendor, SignBox.
*   **Contextual Note:** Inquiry raised regarding current usage of "Vxt" technology on TVs in these stores; awaiting response from Daryl Ng and Allen Umali.

**Pending Actions & Ownership**
*   **Action 1:** Update digital signage IP settings (Static to DHCP) for stores HJPT, HAMK, HPWP, and CQ.
    *   **Owner:** Delwyn / SignBox Team.
    *   **Contact:** +65 8338 7829.
*   **Action 2:** Confirm if TVs in the affected stores are currently using Vxt technology.
    *   **Owner:** Daryl Ng, Allen Umali.
    *   **Context:** Provided as FYI to Seng Shwu Shyan by Calvin Phan.
*   **Action 3 (Resolved):** Determine connection method for ticket NED-195890.
    *   **Status:** This specific ticket requirement is now superseded by the broader SDWAN migration directive if the store falls under the affected list.

**Key Dates & References**
*   **Original Discussion Date:** March 18, 2026 (Ticket NED-195890 context).
*   **New Migration Request Date:** April 6, 2026 (01:48 – 01:57 UTC).
*   **Ticket Reference:** [NED-195890](https://ntucenterprise.atlassian.net/servicedesk/customer/portal/8/NED-195890?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0Z3QiOiJhbm9ueW1vdXMtbGluayIsInFzaCI6IjViOThmMWY0MWUwZmZmNjI3NTliZjBjZTE2OGI1ZmRkNTE1MWY1NWFmY2NlMTVhYjI2MmJiY2I1ZWIxZGEwMWYiLCJpc3MiOiJzZXJ2aWNlZGVzay1qd3QtdG9rZW4taXNzdWVyIiwiY29udGV4dCI6eyJ1c2VyIjoiMTA2MDUiLCJpc3N1ZSI6Ik5FRC0xOTU4OTAifSwiZXhwIjoxNzc2MjE0MzgzLCJpYXQiOjE3NzM3OTUxODN9.lVNBoVHVpF4WMA1KrZH_5yMV1o-Ruw77n_9mCSWJCgI)
*   **Space URL:** https://chat.google.com/space/AAAA1BqTEzo

**Note on Outdated Information**
Static IP ranges (**10.19.77.66–10.19.77.78**) and MAC address whitelisting requirements previously detailed are no longer applicable for the stores listed (HJPT, HAMK, HPWP, CQ) as they are transitioning to DHCP via SDWAN.


## [13/30] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-04-06T01:56:25.536000+00:00 | Last Updated: 2026-04-06T02:47:08.885913+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Update)**
**Date:** April 3–6, 2026 (Shift Continuation)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 1032

### Main Topic
Systemic instability persists into the early hours of April 6th. The incident has evolved into a **high-frequency cyclic volatility pattern**, characterized by rapid trigger/recovery cycles across Wish List read and write operations. New alerts confirm repeated P90 latency spikes on `get /api/wish-list/{_id}` and severe Write operation degradation (`put /api/product/{_id}/wish-list`), with peak latencies surpassing previous records.

### Incident Timeline & Actions
**Historical Context:**
*   *Extended activity from March 20 through late March 31.*
*   *April 2–3:* Critical burst affecting Cart/Checkout and S&G success rates (recovered by end of April 3).

**Latest Activity (Apr 5 Late Evening – Apr 6 Early Morning)**
The cyclic pattern intensified with tighter intervals between spikes:

*   **17:00 – 17:24 UTC (Previous):** P99/P90 spikes on Write operations peaked at 6.629s and 5.336s respectively.
*   **23:42 – 00:07 UTC (Apr 5/6):** Rapid cycle of Write latency.
    *   **Peak:** `put /api/product/{_id}/wish-list` Monitor (`21245701`) hit **9.039s** P99 at 00:34 UTC on Apr 6.
    *   **Secondary Peak:** 6.838s P99 at 00:06 UTC; 7.505s P90 at 00:07 UTC.
*   **00:30 – 01:56 UTC (Apr 6):** Recurring Read latency on `get /api/wish-list/{_id}`.
    *   Triggers occurred at **00:30** (Value: 2.205s) and **01:55** (Value: 1.747s), with rapid recoveries within 6–9 minutes of each trigger.
*   **01:37 – 01:46 UTC:** Another Write spike triggered at 01:37 (6.04s P99), recovering by 01:46.

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** Incidence frequency has increased, with latency spikes occurring every ~30–50 minutes across both Read and Write endpoints. The severity of the P99 spike on Apr 6 (9.039s) indicates escalating systemic stress compared to previous cycles.
*   **Immediate Action Required:**
    *   Correlate the new cyclic windows (23:42, 00:06, 00:30, 00:34, 01:37, 01:55 UTC) with deployment cycles or batch jobs immediately.
    *   Investigate `put /api/product/{_id}/wish-list` (Monitors `21245701`, `21245706`) where P99 reached **9.039s**.
    *   Monitor `get /api/wish-list/{_id}` (Monitor `21245720`) for continued instability.

### Decisions Made
*   **Priority Status:** Maintained at **"Critical Incident"**. The escalation in peak latency values (new max 9.039s) and the tight cyclic nature confirm a broad, worsening systemic issue.
*   **Focus Shift:** Triage explicitly targets the **high-frequency recurrence** of degradation in both read and write operations within the Wish List service.
*   **Metric Update (Session Peak):**
    *   `put /api/product/{_id}/wish-list` P99 High: **9.039s** (00:34 UTC, Apr 6).
    *   `get /api/wish-list/{_id}` P90 High: **2.205s** (00:30 UTC, Apr 6).

### References
*   **Active Monitors:** `21245720` (Wish List Read P90), `21245701` (Wish List Write P99), `21245706` (Wish List Write P90).
*   **Service Tags:** `service:frontend-gateway`, `team:dpd-pricing`.


## [14/30] DPD x Platform Engineering
Source: gchat | Group: space/AAQAcjNXKpA | Messages: 3 | Last Activity: 2026-04-06T01:51:41.910000+00:00 | Last Updated: 2026-04-06T02:48:06.402853+00:00
**Daily Work Briefing: DPD x Platform Engineering**
*(Updated with April 6 Split.io Secret Request & Ongoing Incident Status)*

**Key Participants & Roles**
*   **Kyle Nguyen:** Infrastructure/Platform Engineering (Reviewer, Incident Triage).
*   **Daryl Ng:** Incident Analyst.
*   **Gopalakrishna Dhulipati:** Addressed in new P1 incident; involved in Redis RCA.
*   **Sneha Parab:** Involved in Redis RCA.
*   **Alvin Choo:** Team Lead; escalated regarding April 2 P1 incident.
*   **Sampada Shukla:** Reported SLO alerts March 31; validated April 1 alerts.
*   **Dodla Gopi Krishna:** Owner of Fulfillment/Pricing SLOs.
*   **Maou Sheng Lee:** Initiated inquiry on April 2 regarding P1 incident status.
*   **Jazz Tong:** Provided Terraform run link for `infra-gcp-fpon-prod`.
*   **Tayza Htoon:** Requested Split.io secret upload (April 6).
*   **Tiong Siong Tee:** Last respondent to the April 6 request.

**Main Topics & Discussions**
1.  **P1 Incident: IR-49 "Picking list not available" (April 2):** Maou Sheng Lee flagged the incident as "Active" and breaching group policy at ~03:36 UTC on April 2, requesting status updates. The alert was directed to Alvin Choo and Gopalakrishna Dhulipati.
    *   *Status:* Incident remains Active P1; requires immediate resolution validation.

2.  **Split.io API Key Secret Update (April 6):** Tayza Htoon requested the upload of the latest pre-prod/UAT and production Split.io API keys (`engage-split-io-api-key`) to projects `fpg-engage-preprod` and `fpg-engage-prod`. The request specified alignment with existing configurations in `fpo-platform-preprod` and `fpo-platform-production`, referencing Secret Manager links.
    *   *Status:* Request posted; last reply received from **Tiong Siong Tee** 34 minutes ago (as of briefing time).

3.  **Get Serviceable Area Journey Alert (April 1):** Dodla Gopi Krishna queried SLO V2 alert validation (~02:55 PM local time).
    *   *Status:* Thread active with ongoing verification by Sampada Shukla, Wai Ching Chan, and Akash Gupta.

4.  **High-Urgency Redis CPU Spike (March 30):** Kyle Nguyen reported `zs-fpon-prd-catalogue-service` hitting ~100% CPU in `asia-southeast1`.
    *   *Investigation Status:* Latency spikes from `go-catalogue-service` verified; latency normalized. No formal incident escalation required.

5.  **SLO Error Budget Alerts (March 31):** Sampada Shukla reported alerts regarding Fulfillment and Pricing tribes.
    *   *Status:* Acknowledged by Dodla Gopi Krishna; ongoing degradation in error budget consumption remains a concern.

**Pending Actions & Owners**
*   **Resolve P1 Incident IR-49:** Determine current status of "Picking list not available" breach. *(Owners: Alvin Choo, Gopalakrishna Dhulipati, Maou Sheng Lee)*
*   **Upload Split.io Secrets:** Execute upload of `engage-split-io-api-key` to `fpg-engage-preprod` and `fpg-engage-prod`. *(Owner: Tayza Htoon / Execution pending response from Tiong Siong Tee)*
*   **Validate Get Serviceable Area Alert:** Confirm accuracy of April 1 SLO V2 alert. *(Owners: Sampada Shukla, Wai Ching Chan, Akash Gupta)*
*   **Investigate Redis CPU Saturation:** Prioritize RCA for March 30 event. *(Owners: Daryl Ng, Gopalakrishna Dhulipati, Sneha Parab)*
*   **Address SLO Error Budget Alerts:** Prevent further depletion for Fulfillment and Pricing SLOs. *(Owner: Dodla Gopi Krishna)*
*   **Resolve Cluster Capacity Scaling & Bastion Access:** Investigate March 23 memory limit failures and PROD `asia-southeast1-c` inaccessibility. *(Owners: Kyle Nguyen, Nicholas Tan, Harry Akbar Ali Munir)*

**Decisions Made**
*   *Tentative:* Debate continues on Terraform-based change-freeze vs. direct Datadog UI management for on-call teams.
*   **QC Food Status:** Disabling confirmed on production (as of March 19); resource scale-down planning initiated pending ES confirmation.

**Key Dates & Follow-ups**
*   **April 6, ~01:51 UTC:** Tayza Htoon requested Split.io secret updates; last reply from Tiong Siong Tee recorded 34 minutes ago.
*   **April 2, ~03:36 UTC:** Maou Sheng Lee queried P1 incident IR-49 status; active breach noted.
*   **April 2, ~04:22 UTC:** Jazz Tong posted Terraform run `run-g4Lg24A7Y21cJzPQ`.
*   **April 1, ~05:16 AM:** Last reply recorded in SLO validation thread.
*   **March 31, ~03:55 UTC:** Sampada Shukla reported SLO error budget alerts.
*   **March 30, ~03:00 UTC:** Redis CPU spike triggered; latency normalized.


## [15/30] PDM Notification
Source: gchat | Group: space/AAAAnyFGr84 | Messages: 12 | Last Activity: 2026-04-06T01:36:32.425000+00:00 | Last Updated: 2026-04-06T02:48:49.924313+00:00
**Daily Work Briefing: PDM Notification Summary (Updated)**

**Key Participants & Roles**
*   **Gchat Notification / API Bot (Collection Runner):** Automated system generating test reports.
*   **Webhook Bot:** System component responsible for processing requests; currently failing to render/deliver links despite successful test execution.

**Main Topic**
Automated API contract and functional tests for the `gt-catalogue-service` in the Staging environment executed successfully but failed to generate final notifications due to a persistent Webhook Bot error. The system returns "Webhook Bot is unable to process your request" immediately following summary data, blocking access to detailed reports. This issue persists despite varying test outcomes between runs.

**Pending Actions & Ownership**
*   **Action:** Investigate the specific failure point in the Webhook Bot rendering logic. Prioritize verifying if the failure count discrepancy (now showing 1 failed contract test) aligns with raw Collection Runner data. Resolve the post-execution delivery issue to enable full report visibility.
*   **Owner:** Engineering/DevOps Team (responsible for the notification pipeline).
*   **Context:** New logs from April 6, 2026, confirm a third execution window where tests passed but reporting failed. The error remains a systemic post-processing block.

**Decisions Made**
None recorded; priority remains on repairing the Webhook Bot's rendering capability. No code modifications to service logic are required as failures (if any) are isolated to the notification layer.

**Key Dates & Follow-ups**
*   **Historical Background:** March 18 and March 30, 2026 – Previous incidents with zero execution.
*   **Most Recent Failures/Issues:**
    *   **April 2, 2026 (Two runs):** Run 1 showed 1 API failure; Run 2 showed 2 API failures.
    *   **April 6, 2026 (Run at 01:36 UTC):**
        *   **[API Contract Tests]:** 188 Total Requests, 349 Passed, **1 Failed**, 13 Skipped.
        *   **[API Tests]:** 398 Total Requests, 678 Passed, **0 Failed**, 91 Skipped.
*   **Environment:** Staging.
*   **Service:** `gt-catalogue-service`.
*   **Immediate Follow-up Required:** Correlate the new "1 Failed" contract test count from April 6 against raw data to confirm if the failure is genuine or if the error message previously masked results in earlier runs. Resolve Webhook Bot rendering errors to restore visibility.

**Status Summary**
The automated run summary indicates a critical failure in the *reporting layer*, not the test execution pipeline itself. Unlike previous incidents on March 30 where Total Requests were zero, recent runs (April 2 and April 6) show successful completion with varying outcomes:

*   **April 2 Runs:** Showed API failures (1 and 2 respectively).
*   **April 6 Run (01:36 UTC):** Shows a regression in Contract Tests (**1 Failed** out of 188 requests), while API Tests remained clean.

Despite these results, the Gchat Notification app explicitly states: "Webhook Bot is unable to process your request" for all runs. This confirms a systemic issue where the notification pipeline blocks finalization or display, even though the underlying Collection Runner executed cases. The presence of failed tests in the April 6 Contract Test run suggests potential instability that was previously obscured by earlier assumptions of total execution success. Immediate technical troubleshooting of the Webhook Bot's post-execution logic is required to restore full visibility into test outcomes and accurate failure reporting.


## [16/30] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw | Messages: 3 | Last Activity: 2026-04-06T01:16:29.841000+00:00 | Last Updated: 2026-04-06T02:50:38.658795+00:00
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
1.  **Datadog Cost Optimization:** On April 6, 2026 (01:16 UTC), Natalya Kosenko flagged high costs ($3k+) for services named "be", "fe", and "N/A" in Datadog logs, noting low actionable value. The thread currently has 5 replies with activity from 38 minutes ago.
2.  **System Design Learning:** Winson Lim shared a resource for system design patterns (`https://github.com/VoltAgent/awesome-design-md`) on April 4, 2026 (07:46 UTC). Discussion remains active with updates as of yesterday at 11:23 AM.
3.  **FPPay Production Issue:** On March 30, 2026 (09:11 UTC), Andin Eswarlal Rajesh reported FPPay banner images failing to load in production. Activity continues with 25+ replies.
4.  **Staff Verification Logic:** Vivian Lim Yu Qian queried app screens for staff verification during SKU purchases requiring force verification (e.g., milk powder). The team is validating compliance against existing protocols.
5.  **Incident Management Response:** Earlier on March 27, Jazz Tong raised an urgent query regarding a potential incident ("it is incident?"). The team mobilized support for the DPD Incidents channel involving Gopalakrishna Dhulipati, Akash Gupta, and Kyle Nguyen.
6.  **Infrastructure & Operations Risk:** Nicholas Tan flagged risks regarding Broadcom ending free Bitnami images, causing `kubectl` image tag failures and increased Time To Recovery (TTR) impacting the Golden Pipeline (GP).
7.  **Payment Service Issues:** Alvin Choo reported promo code redemption failures in FP Pay; confirmed that a change freeze has ended and feature releases are proceeding.
8.  **Mobile Quality Assurance:** Andin Eswarlal Rajesh previously identified an iOS FPPay bug where QR codes load without user login, escalated via file download.
9.  **Datadog Governance (Updated):** Natalya Kosenko previously reported unauthorized manual changes to Datadog On-Call teams; Terraform manages this config, overwriting manual console edits on the next run. *New Context:* Current focus has shifted to cost optimization for "be", "fe", and "N/A" services due to wasteful logging.
10. **Strategic Planning & Tooling:** Winson Lim highlighted data centers as potential targets in modern warfare (Iran conflict context) to inform Disaster Recovery (DR) scenarios and noted Reforge joined Miro to bridge strategy and delivery gaps.
11. **AI Engineering Learning:** On March 30, 2026 (23:25 UTC), Winson Lim shared a GitHub repository (`affaan-m/everything-claude-code`) as a resource for learning AI-first engineering patterns.
12. **Security Alert (NPM):** On March 31, 2026 (04:38 UTC), Mohammad Adyatma flagged the compromise of the `axios` npm package via `https://socket.dev/blog/axios-npm-package-compromised`. Immediate review of dependencies is required.
13. **Bonus Communication:** On April 1, 2026 (13:51 UTC), Wai Ching Chan initiated a discussion regarding "FPG Bonus" with 2 replies. A YouTube link was shared in the thread.
14. **Social Events:** Kyle Nguyen announced an upcoming DPD BBQ ("We come first"). Boning He and Gopalakrishna Dhulipati shared snacks; Maou Sheng Lee expressed sentiment regarding energy waste on March 18.
15. **Employee Code of Conduct Update:** On April 2, 2026 (10:02 UTC), Alvin Choo circulated a critical update to the Employee Code of Conduct via NTUC Enterprise Mail, urging all staff to review for doubts.

**Pending Actions & Owners**
*   **Datadog Cost Audit (Natalya Kosenko):** Identify ownership and enable/disable logging for services "be", "fe", and "N/A" to resolve $3k+ wasteful costs. Priority: High.
*   **FPPay Image Team (Andin Eswarlal Rajesh, DevOps):** Investigate root cause of banner image loading failures in production and deploy fix.
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
*   Datadog team configurations must strictly follow Infrastructure as Code (Terraform) protocols; manual overrides are deprecated. *New:* Unactionable logging for "be", "fe", and "N/A" services requires immediate cost review by Natalya Kosenko.
*   Miro's acquisition of Reforge is recognized as a strategic move to bridge product strategy and delivery gaps.
*   Active incident support protocol established for Jazz Tong, Akash Gupta, Gopalakrishna Dhulipati, and Kyle Nguyen on March 27, 2026.
*   Winson Lim endorsed the `affaan-m/everything-claude-code` repository as a key resource for AI-first engineering patterns (March 30). **Updated:** Winson Lim also identified `VoltAgent/awesome-design-md` as a primary reference for system design architecture (April 4).
*   Mandatory review of updated Employee Code of Conduct (April 2, 2026) initiated by Alvin Choo; staff must clarify doubts with management.

**Key Dates & Follow-ups**
*   **Apr 6, 2026 (01:16 UTC):** Natalya Kosenko flagged high Datadog costs for "be", "fe", and "N/A" services; discussion ongoing (5 replies).
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


## [17/30] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Messages: 8 | Last Activity: 2026-04-06T01:14:56.547000+00:00 | Last Updated: 2026-04-06T02:51:22.397568+00:00
**Daily Work Briefing: Nikhil Grover & Michael Bui (Updated)**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator; coordinating incident fixes, ticket updates for the FE team, and RMN project preparation. Currently on a meeting block until 11:00 with additional sessions involving Rajiv.
*   **Michael Bui:** Technical Lead (Engineering); currently initiating integration documentation for CoMall teams.

**Main Topics & Recent Developments (Mar 28 – Apr 06)**
1.  **Integration Documentation & OSMOS Clarification (Apr 06):**
    *   On April 6 at 01:12 UTC, Michael requested an urgent catch-up to discuss integration documents for the CoMall teams and clarify OSMOS capabilities regarding UI design requirements for RMN.
    *   **Correction:** Nikhil confirmed that "OSMOS is not a final thing" but has prepared his own integration docs which were already reviewed with OSMOS. He intends to share these with Michael.
2.  **Meeting Scheduling (Apr 06):**
    *   Due to prior commitments until 11:00, Nikhil proposed rescheduling the catch-up from "early today" to lunchtime.
    *   Michael agreed and requested a WhatsApp call to save time.

**Decisions Made & Status Updates**
*   **Communication Channel:** Agreed to conduct the upcoming discussion via WhatsApp for efficiency.
*   **OSMOS Status:** Clarified that OSMOS is not finalized, while Nikhil's parallel integration documents have undergone internal review with OSMOS and will be shared.
*   **RMN Focus:** Michael specifically seeks to clarify RMN capabilities based on new UI design requirements during the agreed discussion.
*   **Previous Timeline Adjustment:** The previously planned "morning of April 3" meeting was superseded by the immediate request for an April 6 catch-up.

**Pending Actions & Owners**
*   **RMN & OSMOS Catch-up (Michael Bui & Nikhil Grover):** Conduct a WhatsApp call at lunchtime on April 6 to discuss RMN capabilities, UI design requirements, and share integration documents.
*   **Document Sharing (Nikhil Grover):** Share the reviewed integration documents with Michael following the lunch discussion.
*   **Incident Resolution:** The homepage ad race condition remains unresolved; operational focus has shifted temporarily to documentation and RMN alignment while Michael prepares for his leave.

**Key Dates & Deadlines**
*   **April 6, 2026 (01:12 UTC):** Michael requests urgent catch-up regarding CoMall integration docs.
*   **April 6, 2026 (Post-11:00):** Scheduled lunchtime catch-up via WhatsApp.
*   **April 6–12, 2026:** Michael Bui's leave period (island with limited connectivity).

**Historical Context Note**
The conversation originally focused on technical scope regarding video content restrictions and OSMOS `pcnt` limits, later shifting to a critical homepage ad race condition identified March 27. Priorities expanded on April 2 to include RMN discussions within Project Light before Michael's departure. On April 6, amidst preparation for integration documentation for CoMall teams, the focus has refined to clarifying OSMOS capabilities against specific UI design requirements for RMN. While Nikhil noted OSMOS is not final, he confirmed his own integration docs were reviewed with them and will be shared. The immediate operational priority remains resolving these RMN queries before Michael's leave begins on April 6.


## [18/30] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Messages: 17 | Last Activity: 2026-04-06T00:59:09.516000+00:00 | Last Updated: 2026-04-06T02:52:00.621964+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Apr 6, 01:00 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`.
*   **Escalations:** `@oncall-dpd-staff-excellence-pdm`, `@hangouts-GT-Search-DatadogAlerts`, `@hangouts-GT-Discovery-DatadogAlerts`, `@opsgenie-dpd-grocery-discovery`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Retail Media.

**Main Topic**
**P2 INCIDENT (ACTIVE):** High error rate in `fp-search-indexer`.
**P3 INCIDENT (FLUCTUATING):** Intermittent low processed files for `sku-store-attribute` job. Status oscillated between Triggered and Recovered on Apr 6, indicating unstable job processing behavior rather than a stable resolution.

**Active Incidents (Apr 5–6)**
1.  **P2 High Error Rate (`fp-search-indexer`)** [Status: TRIGGERED]
    *   *Timeline:* Triggered Apr 5, 07:23 UTC.
    *   *Metric:* `trace.http.request.errors` > 0.0 in last 1m (Value: 1.0).
    *   *Severity:* Critical ("We don't allow any error").
    *   *Action:* Immediate investigation of Datadog, K8s (`asia-southeast1/fpon-cluster/default/fp-search-indexer`), and Runbook execution remains pending.

2.  **P3 Low Processed Files (`sku-store-attribute`)** [Status: FLUCTUATING / UNSTABLE]
    *   *Timeline:* Initial trigger Apr 5, ~22:07 UTC. Recent activity on Apr 6 shows rapid state changes.
    *   *Recent Events (Apr 6):*
        *   00:44 UTC: **Recovered** (>6 files matched).
        *   00:54 UTC: **Triggered** (<6 files matched in last 5h).
        *   00:59 UTC: **Recovered** (>6 files matched).
    *   *Metric Query:* `logs("service:fpon-catalogue-job-sku-store-attribute \"processed Files:\"").index("*").rollup("count").last("5h") < 6`.
    *   *Scope:* Service tagged `team:dpd-grocery-discovery`, monitored by Datadog.

**Resolved Incidents (Historical)**
*   **P2:** `marketing-service` high error rate (Apr 3) – Resolved.
*   **Historical Anomalies:** Issues with `fpon-catalogue-job-sku-global-attribute`, `go-catalogue-service`, and previous `marketing-service` throughput issues remain resolved.

**Decisions & Pending Actions**
*   **Immediate Action (P2):** Execute Runbook for `fp-search-indexer`. Investigate K8s deployment and logs immediately.
*   **Investigation Focus (P3):** Due to the "Triggered" status at 00:54 UTC on Apr 6, the issue is not fully resolved.
    *   Analyze the root cause of intermittent file processing drops between 00:44 and 00:59 UTC.
    *   Check job logs for transient errors/warnings during low-count windows.
    *   Verify dependency stability (inputs/storage) to prevent recurring triggers.
*   **Notification:** Alert routed to `@hangouts-dd-dpd-grocery-alert`. Escalate to Discovery team if the "Triggered" state persists beyond the next cycle.

**Key Dates & Follow-ups (Apr 2–6, 2026)**
*   **P2 (Active):** `fp-search-indexer` errors (Triggered: Apr 5, 07:23 UTC).
*   **P3 (Fluctuating):** `sku-store-attribute` low files (Last Trigger: Apr 6, 00:54 UTC; Last Recovery: Apr 6, 00:59 UTC).
*   **P2 (Resolved):** `marketing-service` high error rate (Apr 3).

**Reference Links:**
*   **P2 Monitor (`fp-search-indexer` Errors):** https://app.datadoghq.eu/monitors/17447691
*   **P3 Monitor (`sku-store-attribute` Low Files):** https://app.datadoghq.eu/monitors/20382848
*   **Runbook (`fp-search-indexer`):** https://ntuclink.atlassian.net/wiki/spaces/SR/pages/2001831558/Support+Run+book
*   **APM Resource:** https://app.datadoghq.eu/apm/services/fp-search-indexer/operations/http.request/resources?env=prod
*   **K8s Deployment:** https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/fp-search-indexer/overview
*   **Datadog Space:** https://chat.google.com/space/AAAAtxQjB7c


## [19/30] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Messages: 4 | Last Activity: 2026-04-06T00:03:10.002000+00:00 | Last Updated: 2026-04-06T02:52:26.122162+00:00
**Daily Work Briefing Summary (Updated: April 6, 2026)**

**Main Topics & Discussions**
1.  **Programmatic Advertising:** Focus remains on validating discrepancies for `advertima_ttd-fixed-price-test-1.5`. Ravi Singh confirmed receipt of raw BURLs; validation was targeted for Monday, March 17th (historical context). Yian Koh requested confirmation on deals `advertima_ttd-first-price-test` and `advertima_ttd-fixed-price-test-1`.
2.  **New Deal Setup:** Yasmina Tregan (Advertima) requires an end-to-end test setup this week. Wei Phung to share live campaign details; Ravi Singh to execute setup, push to TradeDesk, and map segments before launch.
3.  **BCRS UAT & Finance Integration:** Progress continues on SAP document numbers, duplicate posting fixes via PubSub "exactly once" policy (PR #1033), and Bukit Timah Plaza pricing/display issues.
4.  **Event Sync Optimization (DPD-645):** Addressing the massive event overage (14M vs. normal 550k). PRD deployment plan set for Sunday, March 15 (historical context).
5.  **Security & Compliance:** RMN Pentest fixes (DPD-700) deployed to Prod; Bitbucket App Passwords deprecated effective June 9, 2026.

**Status Update: Inbox & Communications**
*   **Inbox Status:** As of April 6, 2026 (00:03 UTC), the workspace inbox is fully caught up across all categories (**Urgent Action Items**, **Project Updates & Reviews**, **Meeting Updates**, and **FYI**). No pending unread items require immediate attention. This status follows confirmations from daily summaries dated March 24 through April 5. The latest update from Workspace Studio (April 6) confirms zero backlog in all sections, maintaining the trend of cleared Code Reviews and Project Updates established on April 3–5.

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
*   **April 1–6, 2026:** Daily inbox reviews completed; no new urgent items identified across any category (**Urgent Action Items**, **Project Updates & Reviews**, **Meeting Updates**, **FYI**).
*   **June 9, 2026:** Bitbucket App Password deprecation deadline.

**Note on New Content:** The Workspace Studio summary from April 6 (00:03 UTC) confirms the inbox remains clear across all categories, including "Project Updates & Reviews." No new urgent actions or decisions were required; historical project statuses and deadlines remain valid.


## [20/30] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Messages: 16 | Last Activity: 2026-04-05T23:01:22.032000+00:00 | Last Updated: 2026-04-06T02:52:54.303259+00:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
On April 5, a second transient P2 incident cluster involving the `fni-order-create` service occurred between 19:32 and 19:59 UTC, following an earlier morning event. New error patterns emerged in `fni-offer` (FairPrice Route) during this window. Critical latency in `picklist-pregenerator` persists through April 5 evening (April 3–6), with execution times consistently exceeding 3,610s. The P1 SAP authentication failure from April 3 remains resolved.

**Incident Summary & Timeline**
*   **Service: `fni-order-create` (P2 Error Cluster) – April 5 Evening**
    *   **Trigger:** A second cluster triggered at **19:32:39 UTC** with "Exception Occurred At Mirakl Route" (Monitor 17447918). Concurrent triggers included `fni-offer` exceptions at **19:27:56 UTC**.
    *   **Recovery:** All evening monitors recovered by **19:59:49 UTC** (Duration: ~27 minutes).
    *   **Context:** A secondary burst occurred between 19:54–19:59 UTC involving "Failure occurred during fetching orders," "Exception Occurred At DBP Route," and "Error while calling APIs." This mirrors morning instability, indicating recurring systemic integration failure.

*   **Service: `fni-offer` (Transient P2 Error) – April 5 Evening**
    *   **Trigger:** "Exception Occurred at FairPrice Route" triggered at **19:27:56 UTC**.
    *   **Recovery:** Monitor recovered by **19:32:56 UTC** (~5 minutes).

*   **Service: `picklist-pregenerator` (Latency Warning) – Ongoing**
    *   **Status:** Critical latency persists. A new warning triggered on **April 5 at 23:01:22 UTC** with a metric value of **3,611.352s**.
    *   **Triggers:** Pattern continues without resolution across April 3, 4, and 5 evening cycles.
    *   **Monitor ID:** 20383097 (Tagged: `service:seller`, `team:dpd-fulfilment`, `env:prod`).

*   **Service: `fpon-seller-sap-picklist-reporter`**
    *   **Status:** Resolved as of April 3 evening. No new P1 alerts reported on April 4 or 5.

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of the second transient `fni-order-create` cluster (19:27–19:59 UTC) and new `fni-offer` FairPrice exceptions. Focus remains on Mirakl, DBP, and API route stability following four consecutive days of instability (April 1–5).
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Address critical latency in `picklist-pregenerator`. The failure at **23:01 UTC** confirms execution times remain above 3,610s. Immediate architectural review is required.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Summary for Leadership**
On April 5, the system experienced two transient P2 clusters in `fni-order-create`: a morning event (08:29–08:34 UTC) and an evening event (19:27–19:59 UTC). The evening incident introduced new "FairPrice Route" exceptions in `fni-offer` alongside persistent DBP and Mirakl route failures. This marks a continuation of systemic integration instability affecting order creation for four consecutive days. Simultaneously, the critical latency crisis in `picklist-pregenerator` remains unresolved; a new alert at **23:01 UTC** recorded a duration of **3,611.352s**. Urgent engineering review is required to address recurring multi-burst order processing failures and resolve seller experience workflow degradation.


## [21/30] Michael Bui
Source: gchat | Group: space/AAAADYH5KAQ | Last Activity: 2026-04-05T17:47:25.758000+00:00 | Last Updated: 2026-04-05T22:35:18.551689+00:00
**Daily Work Briefing: Google Chat Summary**
**Resource:** Michael Bui
**Date:** April 5, 2026
**Link:** https://chat.google.com/space/AAAADYH5KAQ

**Key Participants & Roles**
*   **Michael Bui:** Identified as the primary contributor discussing script functionality and AI inference performance. (Role inferred: Developer or Technical Lead).

**Main Topic/Discussion**
The discussion focused on a specific bug regarding a scripting process involving AI inference. Michael Bui highlighted that the current script fails to log summarization progress. He noted that this omission creates significant confusion for users when the AI inference duration is lengthy, as there is no visual or textual feedback indicating the system's status during processing.

**Pending Actions & Ownership**
*   **Action:** Update the script to include logging functionality for summarization progress.
*   **Owner:** Unspecified in the provided transcript (requires assignment).
*   **Context:** The fix is necessary to prevent user confusion during long-running AI inference tasks.

**Decisions Made**
No formal decisions or approvals were recorded in this single-message thread. The content represents an issue identification and a stated requirement rather than a resolved decision.

**Key Dates & Follow-ups**
*   **Observation Date:** April 5, 2026, at 17:47 UTC.
*   **Follow-up Required:** Implementation of progress logging to resolve the identified confusion during AI inference. No specific deadline was attached to this message.

**Summary Notes**
The primary concern is user experience and observability within the automation workflow. Without progress logs, stakeholders cannot distinguish between a stalled process and one actively processing long-form AI tasks. Immediate attention is recommended to add these logging mechanisms to the script referenced by Michael Bui.


## [22/30] [Prod Support] Ecom FFS Ops
Source: gchat | Group: space/AAAAde_cYKA | Last Activity: 2026-04-03T08:16:40.717000+00:00 | Last Updated: 2026-04-05T14:35:18.127421+00:00
**Daily Work Briefing: [Prod Support] Ecom FFS Ops (Updated Apr 5)**

**Key Participants & Roles**
*   **Wai Ching Chan / Sampada Shukla:** Operations/Product Leads.
*   **Tok Hong Siang:** TL - TSENGFFS.
*   **Adrian Yap Chye Soon:** Technical Lead/Support.
*   **Akash Gupta:** DPD / Fulfilment / On Call.
*   *(New Inquiry):* **TL HPWP FFS** (Invoked for Order #23032024).

**Main Topics**
1.  **Packlist & SOH Discrepancies (Expanded):** Ongoing investigation into critical `packed_qty` anomalies and Stock on Hand (SOH) NULL values across multiple sites.
    *   **Critical Incident (Apr 3, ~08:16 AM):** Wai Ching Chan flagged a discrepancy at **Hyper Parkway (Store ID 186)**. Order #23032024 shows `packed_qty` of **10,932,725** vs. `delivered_qty` of **3**. Data indicates significant price impact (MRP null).
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

**System Logs**
*   **Apr 5, ~10:40 UTC:** Message deleted by its author. No impact on current operational status or investigation priorities.


## [23/30] DPD AI Guild
Source: gchat | Group: space/AAQA5_B3lZQ | Last Activity: 2026-04-05T08:38:36.182000+00:00 | Last Updated: 2026-04-05T14:35:41.201317+00:00
### Daily Work Briefing: DPD AI Guild

**1. Key Participants & Roles**
*   **Michael Bui:** Research/Technical Lead – Introduced Mistral Small 4; reinforced the principle of precise instruction following.
*   **Zaw Myo Htet:** Technical Strategy/Engineering – Proposed optimization strategy and cost reduction via quantization.
*   **Nicholas Tan:** Strategic Monitor – Highlighted industry trends, critiqued consumer Copilot terms, and assessed mobile hardware constraints.
*   **Oktavianer Diharja:** Engineering Support – Suggested Go utility libraries for skill management.

**2. Main Topic**
The discussion focuses on leveraging **Mistral Small 4** to optimize local knowledge handling via quantization (Unsloth), reducing RAG dependency. This is contextualized by Meta's "AI CEO" automation shift and recent hardware constraints with **Gemma4**. On April 5, Michael Bui emphasized the critical operational necessity of models that execute instructions precisely without deviation or hallucination.

**3. Pending Actions & Ownership**
*   **Action:** Evaluate feasibility of replacing heavy RAG pipelines with quantized open-weight models to reduce costs.
    *   **Owner:** Zaw Myo Htet
    *   **Context:** Requires technical assessment based on Unsloth documentation and precision testing.
*   **Action:** Investigate integration of Mistral Small 4's specific architecture (MoE, 119B total/6B active parameters) into current workflows.
    *   **Owner:** TBD (Team-wide).
*   **Action:** Analyze implications of Meta's "AI CEO" model and Michael Bui's directive on instruction fidelity for the autonomous agent roadmap.
    *   **Owner:** Nicholas Tan / Team
    *   **Context:** Assess if high-level executive automation and strict command execution patterns are applicable to DPD workflows.
*   **Action:** Evaluate constraints and thermal side-effects of deploying mobile-native models like Gemma4 for external/cold-weather field operations.
    *   **Owner:** Nicholas Tan / Engineering Team
    *   **Context:** Investigate if "hand warmer" behavior indicates power inefficiency unsuitable for reliable DPD agent deployment in cold environments.
*   **Action:** Analyze implications of Microsoft Copilot Terms of Service to define risk boundaries for internal AI usage.
    *   **Owner:** Nicholas Tan
    *   **Context:** Determine why consumer tools are unsuitable compared to custom autonomous agent stacks.

**4. Decisions Made**
*   **Strategic Alignment:** The team acknowledges that while Mistral Small 4 offers cost benefits via quantization, the industry is moving toward high-level autonomous agents. Future initiatives must balance model efficiency with strict instruction compliance (per Michael Bui) and agentic autonomy.
*   **Risk Assessment:** Nicholas Tan concluded consumer-grade copilots are "toys not for work" due to legal liabilities. The team agreed to avoid them for production, prioritizing custom or governed enterprise models that ensure precise execution.
*   **Hardware Reality Check:** Current mobile AI (e.g., Gemma4) suffers from thermal inefficiencies in cold climates, rendering standard consumer phones unreliable for field-deployable agents requiring consistent compute performance.
*   **Tooling Consideration:** The `samber/cc-skills-golang` library is flagged for skill management integration pending review by Oktavianer Diharja.

**5. Key Dates & References**
*   **2026-03-17:** Michael Bui announced **Mistral Small 4** (MoE, 119B/6B params, 256k context, Vision).
*   **2026-03-19:** Zaw Myo Htet suggested using **Unsloth** for quantization.
*   **2026-03-24:** Nicholas Tan shared info on Mark Zuckerberg's AI CEO bot.
*   **2026-03-30:** Oktavianer Diharja recommended `cc-skills-golang`.
*   **2026-04-02:** Nicholas Tan flagged Microsoft Copilot Terms of Service as "toy not for work."
*   **2026-04-04:** Nicholas Tan noted Gemma4's thermal inefficiency in cold climates.
*   **2026-04-05T08:38:36:** Michael Bui reinforced the core requirement: **"When AI do exactly what we tell them to do."**

**Thread Status:** Active (Last reply noted recently relative to briefing generation).


## [24/30] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Last Activity: 2026-04-05T03:37:22.592000+00:00 | Last Updated: 2026-04-05T06:57:57.106775+00:00
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


## [25/30] Digital Product Development {DPD}
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


## [26/30] Nikhil, Nicole Soh, Yap Chye Soon, Anwar, ...
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


## [27/30] 📢 COM Notifications
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


## [28/30] [Prod Support] Marketplace
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


## [29/30] QE <-> All Tribes
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


## [30/30] Digital Product Development {DPD}
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
