

## [1/31] You have no events scheduled today.
Source: gmail | Thread: 19d40c04e42da577 | Labels: Inbox, Updates | Priority: None | Senders: Google Calendar | Last Date: Mon, Mar 30, 2026, 9:57 PM | Last Updated: 2026-03-30T22:01:11.161185+00:00
**Daily Work Briefing Summary**

**Key Participants & Roles**
*   **Michael Bui** (michael.bui@fairpricegroup.sg): Primary recipient of the daily agenda notification; subscribed to the "Digital Business Tech Release/Changes" calendar.
*   **Google Calendar System**: Automated sender providing status updates on schedule availability.

**Main Topic/Request**
The email is an automated system notification confirming that the recipient's work schedule for the current day (Tuesday, March 31, 2026) contains no scheduled events. No manual request or discussion occurred in this thread; it serves purely as a status confirmation.

**Pending Actions & Ownership**
*   **No Pending Actions:** There are no tasks assigned, requests made, or follow-ups required based on this specific message.
*   **Ownership:** N/A (System-generated informational update).

**Decisions Made**
*   No decisions were recorded in this thread. The content reflects a static state of the calendar rather than an outcome of deliberation.

**Key Dates & Deadlines**
*   **Notification Date/Time:** March 30, 2026, at 9:57 PM.
*   **Relevant Day:** Tuesday, March 31, 2026 (Confirmed as having no scheduled events).
*   **Calendar Subscription:** Digital Business Tech Release/Changes.

**Specific References**
*   **Account Email:** michael.bui@fairpricegroup.sg
*   **Last Message ID:** 19d40c04e42da577
*   **Settings Link:** https://calendar.google.com/calendar/ (for modifying calendar subscription preferences).

**Conclusion**
The briefing confirms a clear schedule for Michael Bui on March 31, 2026. No immediate action is required unless the user wishes to modify their notification settings via the provided link.


## [2/31] How AI is actually changing developer productivity
Source: gmail | Thread: 19d4065007217075 | Labels: Inbox, Promotions | Priority: None | Senders: Team Atlassian | Last Date: Mon, Mar 30, 2026, 8:17 PM | Last Updated: 2026-03-30T22:01:23.426019+00:00
**Daily Briefing: AI Productivity Webinar Invitation**

**Key Participants & Roles**
*   **Sender:** Atlassian Team (team@eml.atlassian.com)
*   **Speaker 1:** Justin Reock, Deputy CTO at DX. Expert in developer experience and productivity with 20+ years of experience.
*   **Speaker 2:** Nathen Harvey, DORA Lead and Product Manager at Google Cloud. Leads the DORA team on software delivery metrics and co-author of influential reports including "97 Things Every Cloud Engineer Should Know."

**Main Topic & Request**
The email invites recipients to a free webinar titled **"Measuring AI's real impact on developers"** based on the 2025 DORA State of AI-Assisted Software Development report. The session aims to move beyond hype regarding "10x" productivity gains and discuss realistic metrics, benchmarking strategies, and prerequisites for scaling AI in engineering teams.

**Action Items & Ownership**
*   **Action:** Register for the webinar or sign up to receive the recording if unable to attend live.
    *   **Owner:** Recipient (implied need to save a spot).
    *   **Link:** "Save your spot" (CTA provided in original email).

**Decisions Made**
*   No internal decisions were made or recorded in this thread; this is an external invitation.

**Key Dates & Deadlines**
*   **Event Date:** April 23–24, 2026.
*   **Current Status:** Registration is open ("Limited spots available").
*   **Follow-up:** If the recipient cannot attend live, they are instructed to register anyway to receive a recording.

**Specific References**
*   **Report:** 2025 DORA State of AI-Assisted Software Development (140-page document).
*   **Topics Covered:** Realistic productivity gains, evaluation metrics, cross-team benchmarking, and leadership prerequisites for AI scale.
*   **Organization:** Atlassian Pty Ltd, 341 George Street, Sydney, NSW, 2000, Australia.


## [3/31] [JIRA] (DPD-715) Dynamic ad slot configuration for Homepage swimlanes
Source: gmail | Thread: 19cd82204175d296 | Labels: Inbox, Updates | Priority: None | Senders: Nikhil | Last Date: Mon, Mar 30, 2026, 11:15 AM | Last Updated: 2026-03-30T14:02:12.655099+00:00
**Daily Work Briefing: DPD-715 Dynamic Ad Slot Configuration (Race Condition Identified; E2E Testing Required)**

**Key Participants & Roles**
*   **Nikhil Grover:** Product Manager.
*   **Michael Bui:** Development Lead/Manager; executed deployment and identified post-deployment race condition.
*   **Milind Badame:** Assigned QA/Test lead for new verification steps.

**Main Topic/Request**
Development of a dynamic ad slot configuration system (Ticket: **DPD-715**) for Omni and OG Homepage swimlanes, enabling Product Managers to control ad placement indices via Split feature flags without code deployments.

**Decisions Made & Status Updates**
*   **Status Change:** The ticket remains in a critical state following the initial "Done" status on March 25, 2026. A race condition was identified post-launch rendering the `pnct=1` flag ineffective.
*   **Current State:** As of March 30, 2026 (11:15 AM), the ticket requires execution of an End-to-End (E2E) test to validate the fix before re-deployment. The status is effectively **"Ready for E2E Test."**
*   **Production Deployment:** Initial deployment occurred on March 25, 2026 (12:02 AM Singapore Time). UAT was signed off by Nikhil Grover at 10:11 PM Singapore Time on the same date with configuration `[3, 5, 7, 11, 13, 15]`.
*   **Critical Defect Identified:** On March 27, 2026 (03:38 AM Singapore Time), Michael Bui identified a race condition where the `share` variable is overwritten, impacting concurrent requests. This was verified in UAT with evidence provided via screenshot (`image-20260327-193706.png`).
*   **New Testing Requirement:** Milind Badame has explicitly marked the ticket as requiring E2E testing (`Requires_e2e_test: Yes`) to ensure the race condition is resolved across the full user flow prior to final closure.

**Pending Actions & Ownership**
*   **Immediate Action Required:** Execute comprehensive E2E tests on the UAT environment to validate that the `share` variable overwrite logic has been corrected and `pnct=1` functions correctly under load.
*   **Ownership:** Milind Badame is responsible for initiating and executing the E2E test suite. Michael Bui must ensure the codebase is updated with the fix prior to testing.
*   **Monitoring:** Post-deployment monitoring remains paused pending successful E2E validation and subsequent re-deployment.

**Key Dates & Deadlines**
*   **Start Date:** March 10, 2026
*   **UAT Sign-off (Initial):** March 25, 2026 (10:11 PM Singapore Time).
*   **Production Deployment (Initial):** March 25, 2026 (12:02 AM Singapore Time).
*   **Issue Discovery:** March 27, 2026 (03:38 AM Singapore Time).
*   **E2E Test Requirement Added:** March 30, 2026 (11:15 AM) via Jira update by Milind Badame.

**Reference Data**
*   **Ticket ID:** DPD-715
*   **Project:** (Ecom/Omni) DPD
*   **Last Message ID:** 19d3e750cb60c97c (Updated from previous 19d30d7ccd9ed15b)
*   **New Flag:** `Requires_e2e_test: Yes`
*   **Attachments:**
    *   `image-20260325-160055.png` (Visual confirmation of slot changes).
    *   `ScreenRecording_03-26-2026 00-15-50_1.MP4` (Initial post-deployment validation).
    *   `image-20260327-193706.png` (Evidence of race condition affecting `pnct=1`).

**Historical Context Retained**
*   Boundary handling logic remains valid: Configured indices exceeding available content range are ignored; only valid bounds render.
*   Stock integrity checks remain active: Out-of-stock items cannot be served as ads regardless of slot configuration.
*   Previous mobile app issues were resolved in the earlier UAT cycle and verified during initial deployment, though the current race condition represents a new code-level defect unrelated to previous mobile fixes.


## [4/31] [JIRA] (DPD-733) Dynamic ad slots for vertical scroll on omni homepage
Source: gmail | Thread: 19d01d9056f39bea | Labels: Inbox, Updates | Priority: None | Senders: Michael | Last Date: Mon, Mar 30, 2026, 11:15 AM | Last Updated: 2026-03-30T14:02:30.023255+00:00
**Daily Work Briefing: DPD-733 (Dynamic Ad Slots for Vertical Scroll)**

**Key Participants & Roles**
*   **Michael Bui:** Developer/Project Lead. Previously identified as the sole actor performing updates on this work item within the provided log.
*   **Milind Badame:** Jira System User. Recently updated the ticket status and testing requirements.

**Main Topic**
*   **Issue:** [DPD-733] Dynamic ad slots for vertical scroll on omni homepage (Ecom/Omni).
*   **Objective:** Implement dynamic advertising functionality for vertical scrolling on the Omni homepage.

**Status Timeline & Decisions**
The following status transitions and updates were executed:
1.  **Development & Testing Phase:** On March 18, 2026, at 12:37 AM Singapore Time, Michael Bui moved the item from "TO BE DEFINED" through "READY FOR DEVELOPMENT," to "IN DEVELOPMENT," and finally to **"Testing in Preproduction."**
2.  **Completion Decision (Initial):** On March 18, 2026, at 12:37 AM Singapore Time, Michael Bui marked the item as **Resolution: Done** and updated the status to **"IN RELASE QUEUE"** (retaining the source typo) while retaining pre-production testing context.
3.  **Updated Testing Requirement:** On March 30, 2026, at 11:15 AM Singapore Time, Milind Badame updated the ticket indicating that **End-to-End (E2E) Testing is Required ("Yes").** This update supersedes the previous indication of completion pending only release execution.

**Pending Actions & Ownership**
*   **Action:** Conduct required End-to-End (E2E) testing before finalizing the release to production. The item cannot proceed to live deployment until E2E validation is confirmed as "Yes."
*   **Owner:** Milind Badame flagged this requirement; however, specific assignees for the execution of this new test phase are not explicitly defined in the latest log entry.
*   **Next Step:** Execute E2E testing protocols. Upon successful completion, proceed with release deployment from the queue to production.

**Key Dates & Deadlines**
*   **Last Update:** March 30, 2026, at 11:15 AM (E2E requirement update).
*   **Previous Status Change:** March 18, 2026, at 12:37 AM Singapore Time.
*   **Current State:** Item is in the release queue but requires E2E verification before final production launch.

**Additional Notes**
*   The work item includes attachments over 100 KB accessible via the "View work item" link.
*   Notification settings for Jira Cloud mobile apps (Android/iOS) are referenced in system comments.


## [5/31] [JIRA] Milind Badame mentioned you on DPD-715
Source: gmail | Thread: 19d3e71cd098db63 | Labels: Inbox, Updates | Priority: None | Senders: Milind Badame (Jira) | Last Date: Mon, Mar 30, 2026, 11:12 AM | Last Updated: 2026-03-30T14:02:44.252586+00:00
**Daily Work Briefing: Email Thread Summary**

**Key Participants & Roles**
*   **Milind Badame:** Jira User / Test Lead (Represents the testing team).
*   **Michael Bui:** Recipient of the mention; Stakeholder for test requirements.
*   **System/JIRA Bot:** Automated notification sender.

**Main Topic/Request**
Discussion regarding end-to-end (E2E) automation strategies for Jira work item **DPD-715: "Dynamic ad slot configuration for Homepage swimlanes"** within the **(Ecom/Omni) DPD** project. The core issue involves verifying Ad label positions based on split/on/off settings versus static configurations.

**Decisions Made**
*   **Automation Scope:** It was determined that E2E automation updates are **not required** at this time ("No for now").
*   **Verification Method:** Runtime verification of labels based on split settings cannot be automated. Verification must remain **static**, which is already covered by existing tests for vertical and horizontal swimlanes.

**Pending Actions & Ownership**
*   **Action:** Review specific label positions to determine if additional static test updates are needed.
    *   **Owner:** Michael Bui (implied).
    *   **Trigger:** If Michael Bui identifies specific positions requiring verification, he must inform the testing team ("If required, You can let us know...").
*   **Action:** Update E2E tests to include identified positions if requested.
    *   **Owner:** Milind Badame / Testing Team (conditional on Michael Bui's input).

**Key Dates & Follow-ups**
*   **Last Communication Date:** March 30, 2026, at 11:12 AM (Singapore Time).
*   **Work Item Reference:** DPD-715.
*   **Follow-up Status:** Pending. The testing team is waiting for Michael Bui to confirm if any specific positions need verification before proceeding with test updates. No immediate deadline was set, contingent on the user's input.

**Specific References**
*   **Jira Issue:** DPD-715
*   **Project:** (Ecom/Omni) DPD
*   **Feature:** Dynamic ad slot configuration for Homepage swimlanes
*   **Existing Coverage:** E2E tests currently verify Ad label positions for vertical and horizontal swimlanes.
*   **Constraint:** Labels cannot be verified at runtime based on split/on/off settings; verification must be static.


## [6/31] [JIRA] Milind Badame mentioned you on DPD-733
Source: gmail | Thread: 19d3e7152d3e2adf | Labels: Inbox, Updates | Priority: None | Senders: Milind Badame (Jira) | Last Date: Mon, Mar 30, 2026, 11:11 AM | Last Updated: 2026-03-30T14:02:55.060803+00:00
**Daily Work Briefing: JIRA Notification Summary**

**Key Participants & Roles:**
*   **Milind Badame:** System/Jira Tester or Developer (Sender). Provided status update on E2E automation feasibility.
*   **Michael Bui (You):** Recipient of the notification. Requested for input regarding test verification positions.

**Main Topic/Request:**
Discussion regarding **JIRA work item DPD-733** titled *"Dynamic ad slots for vertical scroll on omni homepage."* The focus is on the feasibility and scope of E2E automation for verifying Ad label positions within vertical and horizontal swimlanes, specifically concerning split/on-off settings.

**Decisions Made:**
1.  **Automation Limitation Confirmed:** It was established that runtime verification for label positions based on split/on-off settings cannot be automated at this time. Label verification must remain static.
2.  **E2E Update Status:** No immediate updates to the E2E test suite are required.

**Pending Actions & Ownership:**
*   **Action:** Provide specific label positions that require verification if additional testing is deemed necessary beyond the current static checks.
*   **Owner:** Michael Bui (You).
*   **Context:** Milind Badame has offered to update the tests accordingly should you provide these specific positions.

**Key Dates & References:**
*   **Date/Time:** March 30, 2026, at 11:11 AM (Sender noted as 7:11 PM Singapore Time).
*   **Work Item ID:** DPD-733.
*   **Project Context:** Ecom/Omni / DPD.
*   **Notification ID:** `19d3e7152d3e2adf`.

**Summary of Technical Stance:**
Milind confirmed existing E2E coverage for vertical and horizontal swimlanes verifies Ad label positions statically. Since runtime verification for dynamic split settings is not feasible, the current approach stands unless Michael Bui specifies alternative positions to be added to the test suite.


## [7/31] Opsgenie Alert: [Datadog] [P4] [Triggered] Service marketing-service has an abnormal change in throughput on env:prod
Source: gmail | Thread: 19d3bfcc25dc99ae | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Mon, Mar 30, 2026, 10:20 AM | Last Updated: 2026-03-30T14:03:21.700215+00:00
**Daily Work Briefing: Opsgenie Alert Summary (Updated)**

**1. Key Participants & Roles**
*   **System/Source:** Opsgenie (Notification Engine), Datadog (Monitoring Source).
*   **Alert Owner:** DPD Staff Excellence - Retail Media.
*   **Notify Channels:** `@hangouts-dd-dpd-grocery-alert` (Google Hangouts channel), `@opsgenie-dpd-grocery-retail-media` (Opsgenie responder group).
*   **Service Owner:** `marketing-service`.

**2. Main Topic/Request**
*   **Alert Type:** P4 Priority Alert regarding abnormal throughput changes in the production environment (`env:prod`).
*   **Specific Trigger:** 100% of `sum:trace.http.request.hits{env:prod,service:marketing-service}` values exceeded 3 deviations from predicted values over the last 15 minutes.
*   **Percent Anomalous:** 100.0%.
*   **Integration Details:** Source is Datadog via integration `dpd-grocery-retail-media-eu`.
*   **Request:** Immediate investigation of service health via provided Datadog APM links, Kubernetes (GCP) console, and Runbook documentation.

**3. Pending Actions & Ownership**
*   **Action:** Investigate throughput anomaly, review metrics graphs, and determine root cause for `marketing-service`.
*   **Owner:** DPD Staff Excellence - Retail Media (Assigned via Opsgenie responders).
*   **Required Resources:**
    *   Datadog APM: [Link to marketing-service operations](https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod)
    *   Kubernetes Console: [GCP Cluster Overview](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview?cloudshell=false&project=fponprd)
    *   Runbook: [Atlassian Wiki - marketing-service](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book)

**4. Decisions Made**
*   None recorded in this thread; the alert remains active and awaiting human intervention.

**5. Key Dates, Deadlines & Follow-ups**
*   **Alert Trigger Time:** Mar 30, 2026, at 11:44 PM UTC (Previous snapshot).
*   **Latest Status Update:** Mar 30, 2026, at 10:15 AM UTC (Newest notification received).
    *   *Note:* The "Last Updated" timestamp within the alert payload remains 2026-03-30 10:14:10 +0000.
*   **Notification Timestamps:**
    *   Initial Notification Received: Mar 30, 2026, at 6:15:12 PM (Local time noted in metadata as "Created At").
    *   Latest Status Update: Mar 30, 2026, at 10:15 AM UTC.
*   **Follow-up Required:** Immediate resolution or status update required by the Retail Media team to clear the P4 alert status.

**Technical Metadata**
*   **Monitor ID:** 17447110
*   **Event IDs:** 8565860058801546694 (Initial), 8566119760983702769 (Previous), 8566494225877288340 (Latest).
*   **Tags:** `env:prod`, `service:marketing-service`, `managed_by:datadog-sync`, `monitor`, `priority:p4`.
*   **Integration ID:** ff4c0851-ff71-4975-a76e-b9af95297a56-1774865712480 (TinyId: 139298).
*   **Alert Snapshot Link:** [Datadog Monitor Snapshot](https://app.datadoghq.eu/monitors/17447110?from_ts=1774864750000&to_ts=1774865950000&event_id=8566494225877288340&link_source=monitor_notif&link_monitor_id=17447110&link_event_id=8566494225877288340)
*   **Event URL:** https://app.datadoghq.eu/monitors/17447110


## [8/31] Indirect Procurement Q1 2026 Newsletter
Source: gmail | Thread: 19d3df93c2c73f8f | Labels: Inbox, Forums | Priority: None | Senders: 'Indirect Procureme. | Last Date: Mon, Mar 30, 2026, 9:00 AM | Last Updated: 2026-03-30T10:01:47.698304+00:00
**Executive Briefing: Indirect Procurement Q1 2026 Newsletter**

**Key Participants & Roles**
*   **Sender:** Project Buywell Team (via `grp_fpg_all@fairpricegroup.sg` and `project_buywell@fairpricegroup.sg`).
*   **Audience:** All FairPrice Group colleagues ("Colleagues").
*   **Stakeholders:** Indirect Procurement representatives, Finance team, Suppliers, and Subject Matter Experts (SMEs).

**Main Topic**
The newsletter outlines the final preparation phase for the "Project Buywell" indirect procurement system transition scheduled for Go-Live in Q1 2026. It introduces key features including the new **eInvoice module**, automated **Delegation of Authority (DOA)** streams, and clarifies usage boundaries between **Zycus eProc** and **MyClaims**.

**Pending Actions & Ownership**
*   **System Testing:** Users must prepare for User Acceptance Testing (UAT) and upcoming Key-User Testing/End-User Training sessions. *Owner: All Employees.*
*   **Training Compliance:** Employees must review feature spotlights to prepare for a mandatory quiz prior to Go-Live. Winners will receive prizes. *Owner: All Employees.*
*   **Process Adherence:** Users must stop using MyClaims for non-personal expenses and route such purchases to the correct dedicated systems (e.g., Zycus eProc for assets). *Owner: All Employees.*
*   **System Confirmation:** Recipients are requested to click a specific link (`https://forms.gle/D6whAz364PKpPznx5`) to confirm they have read the newsletter. *Owner: All Employees.*

**Decisions Made**
1.  **eInvoice Implementation:** Adoption of a digital-first eInvoice module to replace paper processing, enabling automated 3-way matching (PO, GR, Invoice) and real-time status tracking.
2.  **DOA Automation:** Approval streams will be automatically routed based on spend type:
    *   Standard Spend.
    *   Waiver Approval (Waiver of Competition/Tender).
    *   SME Approval (mandatory for technical exceptions like IT/Cybersecurity).
    *   Mobile approvals enabled for approvers.
3.  **Expense Policy Enforcement:** Strict prohibition on using credit card charge slips; only original itemized receipts are accepted. MyClaims is restricted strictly to personal expenses incurred while working.

**Key Dates & Deadlines**
*   **Newsletter Date:** March 30, 2026.
*   **Go-Live:** Imminent (Q1 2026 closure). A quiz will be administered immediately before Go-Live.
*   **Follow-up:** Training session emails are forthcoming; no specific dates provided yet.

**Specific References**
*   **Systems Mentioned:** Project Buywell, Zycus eProc, MyClaims, eInvoice module.
*   **Contact Email:** `project_buywell@fairpricegroup.sg`.
*   **Quiz Link:** Refer to "Ready for a Quiz?" section (link provided in original email).
*   **Sustainability Impact:** Digital invoicing cited as saving ~118 trees per 1M invoices and reducing carbon footprint by 63%.


## [9/31] [GCP] New Service Account Key Created - 5ef839aab5b8bfe27baf56b662a06e322aa14a8b
Source: gmail | Thread: 19d3dda3d1f0bd95 | Labels: Inbox, Forums | Priority: None | Senders: noreply-sre | Last Date: Mon, Mar 30, 2026, 8:26 AM | Last Updated: 2026-03-30T10:02:03.110799+00:00
**Daily Work Briefing: Service Account Notification**

**1. Key Participants & Roles**
*   **Sender:** `noreply-sre@ntucenterprise.sg` (System Automated Alert / SRE Team)
*   **Recipient Context:** The email targets the owner or administrator of the service account `fpon-224503/seller-analytics-service@fpon-224503.iam.gserviceaccount.com`. No specific human name is listed in the metadata, but the notification is directed at the entity responsible for this GCP resource.

**2. Main Topic/Request**
*   **Event:** Generation of a new Service Account Key.
*   **Key Identifier:** `5ef839aab5b8bfe27baf56b662a06e322aa14a8b`
*   **Resource:** GCP Service Account `fpon-224503/seller-analytics-service@fpon-224503.iam.gserviceaccount.com`.
*   **Action Required:** The recipient must download the new key via the provided link to ensure continuity of service access before the current credentials expire or are rotated.

**3. Pending Actions & Ownership**
*   **Action:** Download and securely store the new service account key `5ef839aab5b8bfe27baf56b662a06e322aa14a8b`.
*   **Owner:** The system administrator or developer responsible for the `seller-analytics-service` project.
*   **Urgency:** High; the key expires in 90 days, but immediate download is required to access it (as per standard security protocols for new keys).

**4. Decisions Made**
*   **System Decision:** A new key was automatically generated by the GCP system on March 30, 2026.
*   **Expiration Policy:** The new key is configured for a 90-day lifecycle.

**5. Key Dates & Deadlines**
*   **Creation Date/Time:** March 30, 2026, at 8:26 AM.
*   **Expiration Date:** June 28, 2026.
*   **Follow-up Required:** Immediate (Download). No specific follow-up meeting is noted in the thread; however, verification of successful deployment with the new key should occur prior to expiration.

**6. Metadata Context**
*   **Thread Labels:** Inbox, Forums.
*   **Priority:** Not set (null).
*   **Message ID:** `19d3dda3d1f0bd95`.


## [10/31] GCP Service Account Key clean UP
Source: gmail | Thread: 195892088be2d83b | Labels: Inbox | Priority: None | Senders: Mohit, Kyle, Himal | Last Date: Mon, Mar 30, 2026, 7:36 AM | Last Updated: 2026-03-30T10:02:27.546231+00:00
**Daily Work Briefing: GCP Service Account Key Cleanup (Updated)**

**1. Key Participants & Roles**
*   **Himal Hewagamage** (himal.hewagamage@fairpricegroup.sg): Initiator and Security Lead; followed up on March 30, 2026, regarding non-production remediation status.
*   **Kyle Nguyen**: Technical lead coordinating immediate cleanup; assigned Nicholas Tan to assist starting the week of March 30, 2026.
*   **Nicholas Tan**: New support resource added by Kyle Nguyen to assist with execution and tracking.
*   **Jazz Tong** (jazz_tong@fairpricegroup.sg): Previously identified as execution lead; role context remains relevant for scope verification.
*   **Mohit Niranwal** (mohit_niranwal@fairpricegroup.sg): Provided initial context on automated rotation gaps and legacy accounts.

**2. Main Topic/Request**
The team is addressing security risks associated with legacy GCP Service Account (SA) keys created between 2019–2024. Following the March 24, 2026, directive to remediate 56 keys in non-production environments, a status check on **March 30, 2026**, revealed no prior updates from Kyle's team. Consequently, work is now formally restarting with Nicholas Tan as support. Additionally, Himal confirmed the removal of old Datadog service account keys and updated the tracking sheet accordingly.

**3. Pending Actions & Owners**
*   **Immediate Remediation (Non-Prod)**: Kyle Nguyen and Nicholas Tan will commence execution for the 56 identified legacy keys starting the week of March 30, 2026.
*   **Progress Tracking**: Kyle Nguyen has added a "Status" column to the tracking sheet to monitor individual item progress; this is now the primary method for status reporting.
*   **Documentation Update**: Kyle must update the [GCP][Security] Service Account Key Rotation & Decommission document to reflect project owner information and current remediation status.
*   **Owner Verification**: Integration of Jazz Tong's previous task (tagging application owners) remains pending under Kyle's documentation responsibility.
*   **Onboarding Process**: For SAs without keys or those with outdated keys, the team will facilitate onboarding into the automated key rotation process via a specific Google Group.

**4. Decisions Made & Process Changes**
*   **Execution Strategy (Mar 30, 2026)**: The team confirmed that remediation for non-production environments will proceed immediately with expanded resources (Nicholas Tan).
*   **Data Hygiene**: Himal Hewagamage has proactively removed old Datadog service account keys and updated the central tracking sheet.
*   **Communication Channel**: A separate weekly communication channel remains the primary method for status updates regarding key decommissioning.
*   **Scope & Strategy**: The scope covers `cpd-dp`, `fpg-callisto`, `fpg-jarvis`, `fpg-optimus`, and `fponprd` environments. The strategy prioritizes enabling automated rotation for legacy accounts before decommissioning based on application utility.

**5. Key Dates & Follow-ups**
*   **Mar 10–24, 2026**: Initial requests, spreadsheet updates, meeting, and directive for immediate remediation of 56 keys issued by Himal.
*   **Mar 30, 2026 (4:11 AM)**: Himal requested a status update on non-production key removal, noting no response was received.
*   **Mar 30, 2026 (7:33 AM)**: Kyle confirmed the team will start work that week and added Nicholas Tan to support; tracking sheet updated with a new "Status" column.
*   **Mar 30, 2026 (7:36 AM)**: Himal confirmed removal of old Datadog keys and offered further support if clarification is needed.

**Links & References**
*   *Data Source*: https://docs.google.com/spreadsheets/d/1mGBCTRQDcTs0z_w0LjVtywDCtFHZhZfWYIRGqcNglpQ/edit?gid=0#gid=0 (Updated by Himal)
*   *Documentation*: [GCP][Security] Service Account Key Rotation & Decommission (To be updated by Kyle).


## [11/31] Notes: “ACNxOsmos: Daily Cadence” Mar 30, 2026
Source: gmail | Thread: 19d3d27b6670b367 | Labels: Inbox | Priority: None | Senders: Gemini | Last Date: Mon, Mar 30, 2026, 5:11 AM | Last Updated: 2026-03-30T10:02:40.918776+00:00
**Daily Briefing Summary: ACNxOsmos Daily Cadence (Mar 30, 2026)**

**Key Participants & Roles**
The meeting involved the broader team including **Nikhil Grover**, **Rachit Sachdeva**, and **Rahul Jain**. Coordination is required with external stakeholders: **Alan**, **Carly** (vendor-to-advertiser mapping), and **Gori** (Meta offsite). The meeting was facilitated via Google Meet, with notes auto-generated by Gemini.

**Main Topic & Requests**
The discussion focused on three core areas: Product Listing Ad (PLA) targeting timelines, catalog synchronization strategies, and event tracking for statistical rigor. A primary request involves securing GMV data splits and vendor mappings to support the PLA launch strategy.

**Decisions Made**
*   **PLA Launch Date:** The business has decided to push the PLA targeting launch to **June 1st**. The accelerated end-of-May timeline cannot be moved up further.
*   **Catalog Sync Method:** The API is confirmed acceptable for full and differential syncs (up to 150,000 products); differential updates are recommended for real-time changes. For Store Feed syncing, the team must use a cloud file via S3 or GCS bucket as no API exists for this process.
*   **Event Tracking:** Both server-to-server tracking (via Segment) and client-side tracking (via SDK) are mandated to ensure real-time updates for audience targeting.

**Pending Actions & Owners**
*   **Nikhil Grover:**
    *   Verify the ability to add brand links to the data dashboard.
    *   Draft a sales uplift measurement strategy document, including use cases and questions on statistical significance for small categories.
*   **Rachit Sachdeva:**
    *   Coordinate the GMV split data request and vendor mapping directly with Alan or (Alan and Carly).
*   **Rahul Jain:**
    *   Obtain the planned timeline for display sales uplift from stakeholders.
    *   Coordinate the meta offsite integration schedule with Gori.
    *   Draft and share the final meta offsite plan by **Wednesday**.
    *   Share the current store feed file structure and provide the last update date of the list.

**Key Dates & Deadlines**
*   **June 1, 2026:** Targeted launch date for PLA targeting.
*   **Wednesday (March 30, 2026):** Deadline to draft and share the final meta offsite plan.


## [12/31] Updated invitation: ACNxOsmos: Daily Cadence @ Mon Mar 30, 2026 12:30pm - 1pm (SGT) (Artharn Senrit)
Source: gmail | Thread: 19d3d2704cd5b3e2 | Labels: Inbox, Updates | Priority: None | Senders: me, Mail | Last Date: Mon, Mar 30, 2026, 5:11 AM | Last Updated: 2026-03-30T10:02:53.962537+00:00
**Daily Work Briefing: ACNxOsmos Daily Cadence Update**

**Key Participants & Roles**
*   **Organizer:** Michael Bui (FairPrice Group).
*   **Attendees:** Flora Wo Ke, Vipul Gupta, Barkha Kewalramani, Rahul Jain, Tiong Siong Tee, Daryl Ng, John Henji Mantaring, Artharn Senrit, Nikhil Grover, Aman Khatri, Tanul Mehta (Onlinesales/Accenture), Satish Pamidimarthi, Shravan Kankaria, Siddharth Aklujkar, Rachit Sachdeva.
*   **Optional Guest:** Ravi Goel.

**Main Topic/Request**
Update regarding the "ACNxOsmos: Daily Cadence" meeting scheduled for Monday, March 30, 2026. The organizer notified attendees of changes to the event's attachments and confirmed the connection details remain active via Google Meet. A specific project document, **"FPG Project Plan 2905025,"** is attached to the invitation.

**Pending Actions & Ownership**
*   **Action:** Investigate failed RSVP delivery for Artharn Senrit.
    *   **Context:** An automated bounce message indicates that an email sent to `artharn.senrit_fp@ntucguest.com` was undeliverable ("Address not found").
    *   **Owner:** Michael Bui (Organizer) or the system administrator managing the guest list.
*   **Action:** Verify correct email address for Artharn Senrit's RSVP to ensure attendance confirmation is recorded.

**Decisions Made**
*   No substantive changes to the meeting agenda, time, or location were made; only attachment metadata was updated.
*   The meeting link (`meet.google.com/xbb-jnwp-okc`) and US phone dial-in details remain valid.

**Key Dates, Deadlines & Follow-ups**
*   **Meeting Date/Time:** Monday, March 30, 2026, at 12:30 PM – 1:00 PM (SGT).
*   **Reference Project:** FPG Project Plan 2905025.
*   **Immediate Follow-up:** Resolve the delivery failure for `artharn.senrit_fp@ntucguest.com` prior to the meeting start time to confirm Artharn Senrit's participation status.


## [13/31] Delivery Status Notification (Failure)
Source: gmail | Thread: 19d3d2708a9e7707 | Labels: Inbox, Updates | Priority: None | Senders: Mail Delivery Subsy. | Last Date: Mon, Mar 30, 2026, 5:11 AM | Last Updated: 2026-03-30T10:03:03.593283+00:00
**Daily Work Briefing: Delivery Failure Notification**

**Key Participants & Roles**
*   **Sender:** [Not Specified in Thread] (Initiated the email).
*   **Recipient:** tanul.mehta@accenture.com.
*   **System Actor:** Mail Delivery Subsystem (<mailer-daemon@googlemail.com>) via Google Workspace, which generated the failure report.

**Main Topic/Request**
The thread documents a failed email delivery attempt to `tanul.mehta@accenture.com`. The system explicitly reported that the message could not be delivered because the recipient's address was "not found."

**Pending Actions & Ownership**
*   **Action:** Investigate and correct the recipient email address or verify if `tanul.mehta@accenture.com` is still active within Accenture.
*   **Owner:** The original sender of the undelivered message (identity not specified in this thread).
*   **Next Steps:** Attempt delivery to an alternative valid address for Tanul Mehta or contact IT support to resolve the "User Unknown" status.

**Decisions Made**
No decisions were made within this automated notification thread, as it is a system-generated error report rather than a discussion forum.

**Key Dates & Deadlines**
*   **Failure Date:** March 30, 2026, at 5:11 AM.
*   **Error Code:** 550 5.1.1 User Unknown.
*   **Message ID Reference:** `19d3d2708a9e7707`.

**Status Summary**
The email thread is a "Delivery Status Notification (Failure)." The remote server rejected the message immediately upon receipt, citing that the user account does not exist or cannot receive mail. No further communication occurred between human parties regarding this specific incident in this log.


## [14/31] Updated invitation: ACNxOsmos: Daily Cadence @ Mon Mar 30, 2026 12:30pm - 1pm (SGT) (artharn.senrit@accenture.com)
Source: gmail | Thread: 19d3d2705bad27bc | Labels: None | Priority: None | Senders: me | Last Date: Mon, Mar 30, 2026, 5:11 AM | Last Updated: 2026-03-30T10:03:18.530020+00:00
**Daily Work Briefing: ACNxOsmos Daily Cadence**

**Key Participants & Roles**
*   **Organizer:** Michael Bui (FairPrice Group)
*   **Attendees:** Flora Wo Ke, Vipul Gupta, Barkha Kewalramani, Rahul Jain, Tiong Siong Tee, Daryl Ng, John Henji Mantaring, Artharn Senrit, Nikhil Grover, Aman Khatri, Tanul Mehta, Tanish Nevatia, Nabhey Samant, Shubhangi Agrawal, Siddharth Aklujkar, Rachit Sachdeva, Satish Pamidimarthi, Shravan Kankaria.
*   **Optional Attendee:** Ravi Goel.
*   **Representatives:** Accenture team (Artharn Senrit, Tanul Mehta, Satish Pamidimarthi) and Onlinesales.ai team (Vipul Gupta, Barkha Kewalramani, Rahul Jain, etc.).

**Main Topic & Request**
*   **Event:** "ACNxOsmos: Daily Cadence" meeting.
*   **Action Taken:** Organizers updated the invitation to include attachments and confirmed Google Meet/phone dial-in details for participation.
*   **Subject Matter Review:** The attached document **"FPG Project Plan 2905025"** is the primary agenda item for discussion.

**Pending Actions & Ownership**
*   **No specific new action items identified in this notification.**
*   **Implied Action:** All attendees are expected to review the "FPG Project Plan 2905025" prior to the meeting start time.
*   **RSVP Status:** The system indicates an interest from `artharn.senrit@accenture.com` (marked "Yes").

**Decisions Made**
*   **Meeting Logistics Confirmed:** The meeting will proceed as scheduled on **Monday, March 30, 2026**, from **12:30 PM to 1:00 PM SGT**.
*   **Access Method:** Participants are directed to use the Google Meet link (`meet.google.com/xbb-jnwp-okc`) or phone dial-in (US: +1 321-609-5234, PIN: 867832275).

**Key Dates & Follow-ups**
*   **Meeting Date:** March 30, 2026.
*   **Time:** 12:30 PM – 1:00 PM (Singapore Standard Time).
*   **Reference Document:** "FPG Project Plan 2905025" (Attached to the calendar invite).
*   **Next Steps:** Attendees must join the call at the scheduled time; no further updates were generated in this specific thread after the attachment update.


## [15/31] Updated invitation: ACNxOsmos: Daily Cadence @ Mon Mar 30, 2026 12:30pm - 1pm (SGT) (satish.pamidimarthi@accenture.com)
Source: gmail | Thread: 19d3d2704da5cee1 | Labels: None | Priority: None | Senders: me | Last Date: Mon, Mar 30, 2026, 5:11 AM | Last Updated: 2026-03-30T10:03:34.236697+00:00
**Daily Work Briefing: ACNxOsmos Daily Cadence Update**

**1. Key Participants & Roles**
*   **Organizer:** Michael Bui (FairPrice Group)
*   **Primary Attendees:** Flora Wo Ke, Vipul Gupta, Barkha Kewalramani, Rahul Jain, Tiong Siong Tee, Daryl Ng, John Henji Mantaring, Artharn Senrit, Nikhil Grover, Aman Khatri, Tanul Mehta, Tanish Nevatia, Nabhey Samant, Shubhangi Agrawal, Siddharth Aklujkar, Rachit Sachdeva, Shravan Kankaria.
*   **Accenture Representatives:** Satish Pamidimarthi (User), Artharn Senrit, Tanul Mehta.
*   **Optional Guest:** Ravi Goel.

**2. Main Topic/Request**
This is an updated calendar invitation for the **"ACNxOsmos: Daily Cadence"** meeting. The primary change noted in the thread was an update to the event attachments. The session focuses on project execution and alignment regarding the **FPG Project Plan**.

**3. Pending Actions & Ownership**
*   **Action:** Review updated attachment "CHANGED Notes by Gemini" (Project Plan Ref: FPG Project Plan 2905025).
    *   **Owner:** All attendees, specifically Satish Pamidimarthi, to ensure alignment with the latest notes.
*   **Action:** Confirm attendance status via Google Calendar.
    *   **Owner:** Satish Pamidimarthi (Current RSVP status: Pending response required; "Yes" is an option).

**4. Decisions Made**
*   **Meeting Logistics Confirmed:** The meeting time and location remain fixed for Monday, March 30, 2026, from 12:30 PM to 1:00 PM (SGT).
*   **Access Method:** Meeting will be conducted via Google Meet.

**5. Key Dates & Follow-ups**
*   **Meeting Date:** Monday, March 30, 2026.
*   **Time:** 12:30 PM – 1:00 PM Singapore Standard Time (SGT).
*   **Join Details:**
    *   **Google Meet Link:** `meet.google.com/xbb-jnwp-okc`
    *   **Phone Access (US):** +1 321-609-5234 | PIN: 867832275.
*   **Document Reference:** FPG Project Plan 2905025.

**Summary Statement:**
The ACNxOsmos Daily Cadence is scheduled for March 30, 2026. The organizer has updated the meeting invitation to include revised notes regarding the "FPG Project Plan 2905025." Satish Pamidimarthi and other attendees must review the updated attachment prior to the call and confirm their RSVP status on Google Calendar.


## [16/31] Updated invitation: ACNxOsmos: Daily Cadence @ Mon Mar 30, 2026 12:30pm - 1pm (SGT) (tanul.mehta@accenture.com)
Source: gmail | Thread: 19d3d27045b94fad | Labels: None | Priority: None | Senders: me | Last Date: Mon, Mar 30, 2026, 5:11 AM | Last Updated: 2026-03-30T10:03:48.724482+00:00
**Daily Work Briefing: Daily Cadence Update**

**1. Key Participants & Roles**
*   **Organizer:** Michael Bui (FairPrice Group)
*   **Primary Attendees (FPG/Onlinesales/Accenture):** Flora Wo Ke, Vipul Gupta, Barkha Kewalramani, Rahul Jain, Tiong Siong Tee, Daryl Ng, John Henji Mantaring, Artharn Senrit, Nikhil Grover, Aman Khatri, Tanul Mehta (Accenture), Tanish Nevatia, Nabhey Samant, Shubhangi Agrawal, Siddharth Aklujkar, Rachit Sachdeva, Shravan Kankaria.
*   **Optional Attendee:** Ravi Goel.

**2. Main Topic & Request**
*   **Event:** "ACNxOsmos: Daily Cadence" (Project Plan Ref: FPG Project Plan 2905025).
*   **Purpose:** Scheduled daily status sync for the FairPrice Group project.
*   **Update Notification:** The event details were updated on March 30, 2026, at 5:11 AM SGT by Michael Bui to include specific attachments.

**3. Pending Actions & Owners**
*   **RSVP Confirmation:** Tanul Mehta (tanul.mehta@accenture.com) must confirm attendance status via the Google Calendar link ("Yes", "No", or "Maybe").
*   **Meeting Participation:** All listed guests are required to join using the provided meeting credentials.

**4. Decisions Made**
*   **Schedule Confirmation:** The meeting is confirmed for Monday, March 30, 2026, from 12:30 PM to 1:00 PM (Singapore Standard Time).
*   **Attachments Added:** The "FPG Project Plan 2905025" document was attached to the invitation.

**5. Key Dates & Logistics**
*   **Date:** Monday, March 30, 2026.
*   **Time:** 12:30 PM – 1:00 PM (SGT).
*   **Meeting Link:** `meet.google.com/xbb-jnwp-okc`
*   **Phone Access:**
    *   US Toll-free: +1 321-609-5234
    *   PIN: 867832275

**Summary for Action:** Ensure the "FPG Project Plan 2905025" is reviewed prior to the 12:30 PM SGT cadence on March 30, 2026. Tanul Mehta and other attendees should verify their calendar availability immediately.


## [17/31] Scale to 30+ Channels: Join our Webinar | CrescoData x Neto by Maropost
Source: gmail | Thread: 19d3cd7dffa3af84 | Labels: Inbox, Promotions, Risky (by Trend Micro) | Priority: None | Senders: CrescoData | Last Date: Mon, Mar 30, 2026, 3:44 AM | Last Updated: 2026-03-30T10:04:25.258285+00:00
**Daily Work Briefing: Webinar Invitation Summary**

**Key Participants & Roles**
*   **Sender:** CrescoData (Marketing Team), representing the event organizer.
*   **Recipient:** Internal Inbox (User).
*   **Partnership/Hosts:** Neto by Maropost and CrescoData.
*   **Contact for Sales:** sales@crescodata.com.

**Main Topic & Request**
CrescoData is promoting an execution-focused webinar designed to help eCommerce brands scale marketplace presence in 2026. The session addresses operational readiness, specifically focusing on migrating from legacy apps and reducing manual data mapping.
*   **Core Value Proposition:** Scaling to over 30+ marketplaces without complexity.
*   **Specific Focus Areas:**
    *   Expanding to 30+ marketplaces confidently.
    *   Migrating infrastructure for scalability.
    *   Reducing manual catalogue and inventory management.
    *   Reviewing marketplace trends specific to Australia and New Zealand.

**Pending Actions & Ownership**
*   **Action:** Register for the webinar via the provided link ("Register for the Webinar Here").
*   **Ownership:** Pending user decision/registration.
*   **Optional Action:** Reach out via email at sales@crescodata.com if additional connection is desired prior to the event.

**Decisions Made**
*   No internal decisions were recorded in this thread; this is an incoming promotional notification.

**Key Dates & Deadlines**
*   **Event Date:** Tuesday, 31 March 2026.
*   **Event Time:** 1:00 PM AEDT / 2:00 PM AEST (Note: Current date in email is March 30, 2026; event is scheduled for the following day).
*   **Session Content:** Includes live Q&A.

**Metadata & Technical Notes**
*   **Email Priority:** Not flagged as high priority by system.
*   **Security Status:** Flagged as **"Risky (by Trend Micro)"**. Caution advised when clicking external links or providing data.
*   **Sender Address:** marketing@crescodata.com.
*   **Company Address:** 38 Beach Road, #23-11 South Beach Tower, Singapore 189766.


## [18/31] [Action Required] Service Account Key Expiring, Renewal Required - f792e978ec1ae926be65e78b9b0ee4256ac146b7
Source: gmail | Thread: 19d3cb2f9f8dffd9 | Labels: Inbox, Forums | Priority: None | Senders: noreply-sre | Last Date: Mon, Mar 30, 2026, 3:04 AM | Last Updated: 2026-03-30T10:04:38.856988+00:00
**Daily Work Briefing: Service Account Key Expiration Alert**

**Key Participants & Roles**
*   **noreply-sre@ntucenterprise.sg (NTU Centreprise SRE Team):** System administrator issuing automated alerts for infrastructure maintenance.
*   **Service Owner (Recipient of email):** The system owner responsible for the service account `fponprd/fpon-gcs-sign-url@fponprd.iam.gserviceaccount.com`. Role is not explicitly named but requires immediate technical intervention.

**Main Topic/Request**
Automated notification regarding the impending expiration of a Google Cloud Platform (GCP) service account key (`f792e978ec1ae926be65e78b9b0ee4256ac146b7`). The SRE team has pre-generated a replacement key and is instructing the recipient to rotate it before validity expires to prevent authentication failures.

**Pending Actions & Ownership**
*   **Action:** Download the new service account key (to be sent in a separate email) and replace the existing key (`f792e978ec1ae926be65e78b9b0ee4256ac146b7`) within the target system.
*   **Ownership:** Service Owner / Engineering Team managing `fponprd/fpon-gcs-sign-url`.
*   **Conditional Action:** If the key is deemed stale and no longer needed, the Service Owner must raise a formal SRE request to permanently remove it instead of renewing.

**Decisions Made**
*   No new decisions were made in this thread; this is an advisory alert requiring execution by the recipient. The system has already decided to generate a replacement key for distribution.

**Key Dates & Deadlines**
*   **Alert Issued:** March 30, 2026, at 3:04 AM.
*   **Expiration Deadline:** April 29, 2026. The current key becomes invalid after this date.
*   **Follow-up:** A separate email containing the new service account key will be sent "shortly" after March 30, 2026.

**Specific References**
*   **Key ID:** `f792e978ec1ae926be65e78b9b0ee4256ac146b7`
*   **Service Account Email:** `fponprd/fpon-gcs-sign-url@fponprd.iam.gserviceaccount.com`
*   **Project/Environment Context:** `fponprd` (Production).


## [19/31] [Dashboard Report] Retail Media - DD Dashboard | Mon 30 Mar 11:00AM +08
Source: gmail | Thread: 19d3cb250094e16f | Labels: Inbox, Updates | Priority: None | Senders: Datadog HQ | Last Date: Mon, Mar 30, 2026, 3:03 AM | Last Updated: 2026-03-30T10:04:49.647379+00:00
**Daily Work Briefing: Retail Media Dashboard Update**

**1. Key Participants & Roles**
*   **Michael:** Recipient of the report; implied owner of the "Retail Media" dashboard monitoring workflow (Role: Analyst/Stakeholder).
*   **Team Datadog / Datadog HQ:** Sender and automated system source. Role: Reporting/Operations provider.

**2. Main Topic & Request**
*   **Topic:** Automated delivery of historical performance data for the "Retail Media - DD Dashboard."
*   **Request:** Notification that a report containing the last 3 days of dashboard data has been attached to the email for review and monitoring purposes.

**3. Pending Actions & Ownership**
*   **Action:** Review the attached `[Dashboard Report] Retail Media - DD Dashboard` file (dated Mon 30 Mar).
*   **Ownership:** Michael.
*   **Context:** The report covers data from March 27, 2026, through March 30, 2026. No explicit follow-up action was requested in the email body beyond "Happy monitoring."

**4. Decisions Made**
*   None recorded in this thread. This is an informational update/automated delivery notification.

**5. Key Dates & Deadlines**
*   **Report Date:** Monday, March 30, 2026.
*   **Timestamp Sent:** 11:00 AM +08 (Local time).
*   **Data Scope:** Past 3 days relative to the report date (March 27–30, 2026).
*   **Organization Reference:** Datadog Inc., New York, NY.

**6. Specific References & Metadata**
*   **Subject/Asset:** `Retail Media - DD Dashboard`
*   **Email ID:** `19d3cb250094e16f` (Last Message)
*   **Sender Address:** `no-reply@dtdg.eu`
*   **Labels:** Inbox, Updates


## [20/31] Michael, here’s Google’s 2026 security blueprint.
Source: gmail | Thread: 19d3ca9cd752098c | Labels: Inbox, Updates | Priority: None | Senders: Google Cloud | Last Date: Mon, Mar 30, 2026, 2:54 AM | Last Updated: 2026-03-30T10:05:02.220231+00:00
**Daily Work Briefing: Security Talks 2026 Event**

**Key Participants & Roles**
*   **Michael:** Internal recipient; target audience for the briefing.
*   **Google Cloud Team:** Sender and organizer of the virtual event.
*   **Security Experts:** Panelists presenting internal Google security strategies (roles unspecified in text).

**Main Topic/Request**
Invitation to register for "Security Talks 2026: How Google Does It," a virtual event hosted by Google Cloud on April 8, 2026. The session details how Google leverages AI Agents to transform SecOps and offers a blueprint for implementing similar security best practices (including Zero Trust, threat modeling, and automated TDIR workflows) at Michael's organization.

**Pending Actions & Ownership**
*   **Action:** Register/Save spot for the event.
    *   **Owner:** Michael (Immediate).
*   **Action:** Attend live or access on-demand recording if unable to attend.
    *   **Owner:** Michael.

**Decisions Made**
No internal decisions were made within this thread; it is a notification and invitation from an external vendor/partner.

**Key Dates, Deadlines & Follow-ups**
*   **Event Date:** April 8, 2026.
*   **Time:** 11:30 AM – 1:30 PM GMT+8.
*   **Location:** Online (Virtual).
*   **Contextual Reference:** JAPAC 2025 Cyber Attack Aftermath review included in agenda.
*   **Follow-up:** On-demand access will be provided if the live session is missed.

**Event Agenda Highlights**
1.  JAPAC 2025 Cyber Attack Aftermath & 2026 Recommendations.
2.  Google's Forecast on the AI Revolution in Threats and Defense.
3.  Adversarial Misuse of AI (Internal threat group insights).
4.  Proactive Security via Threat Modeling, Red Teaming, and Vulnerability Management.
5.  Blueprint for Modern Threat Detection and Cloud Forensics.
6.  Zero Trust at hyperscale (securing 190,000+ Google Workspace users).

**Metadata Note**
*   **Labels:** Inbox, Updates.
*   **Last Message ID:** 19d3ca9cd752098c.


## [21/31] The Account Holder for your team has changed.
Source: gmail | Thread: 19d3ca5865ca2f70 | Labels: Inbox, Updates | Priority: None | Senders: Apple Developer | Last Date: Mon, Mar 30, 2026, 2:49 AM | Last Updated: 2026-03-30T10:05:11.967103+00:00
**Daily Work Briefing: Apple Developer Account Update**

**Key Participants & Roles**
*   **Sender:** Apple Developer Relations Team (`developer@email.apple.com`) – Issued service notification.
*   **Recipient (Internal):** Michael – Current user receiving the notification.
*   **New Account Holder:** Mohammed Miran – Replaced as the primary account holder for the team.

**Main Topic & Request**
Apple has officially transferred Account Holder authority for **NTUC Fairprice Co-operative Limited**. The organization must now direct all inquiries regarding legal agreements, contracts, app submissions, and program membership renewals to the new Account Holder, Mohammed Miran.

**Pending Actions & Ownership**
*   **Action:** Update internal records and inform relevant stakeholders (legal, development, operations) of the change in authority.
    *   **Owner:** Internal Team / Michael (implied owner to disseminate info).
*   **Action:** Redirect any future correspondence or requests regarding account management to Mohammed Miran.
    *   **Owner:** All team members interacting with Apple Developer services.

**Decisions Made**
*   No new decisions were made by the internal team; this is an administrative update initiated by Apple confirming the change in leadership for the developer program membership effective immediately ("As of today").

**Key Dates & Follow-ups**
*   **Effective Date:** March 30, 2026.
*   **Notification Sent:** March 30, 2026, at 2:49 AM.
*   **Follow-up Required:** None immediately from Apple's side; the team must acknowledge the change to ensure future processes (renewals/submissions) are not delayed.

**Specific References**
*   **Organization:** NTUC Fairprice Co-operative Limited
*   **Message ID:** 19d3ca5865ca2f70
*   **Service Provider:** Apple Inc.


## [22/31] NTUC Enterprise-2025 Web Service Penetration Testing for RMN APIs
Source: gmail | Thread: 19abde329ef69594 | Labels: Inbox, ⚠️IMPORTANT | Priority: ⚠️IMPORTANT | Senders: Ong, Jazz, me | Last Date: Mon, Mar 30, 2026, 2:08 AM | Last Updated: 2026-03-30T10:05:31.762367+00:00
**Subject:** Update: NTUC Enterprise-2025 RMN API Pen Test – Final Report PDF & Milestone Acknowledgement Follow-up

**Key Participants & Roles:**
*   **Michael Bui (FairPrice Group):** Client/Project Owner. Confirmed technical resolution on Mar 25, 2026; requested Jazz Tong's assistance for document acknowledgement.
*   **Ong Xiao Cong (LGMS):** Vendor Lead. Executed retest, delivered final report via secure link on Mar 24, 2026, and followed up on Mar 30, 2026, regarding queries, PDF conversion, and the signed Milestone Acknowledgement (MA) form.
*   **Jazz Tong (FairPrice Group):** Internal Stakeholder. Assisting Michael Bui with document acknowledgement processes.

**Main Topic/Request:**
Follow-up on post-assessment results to address team queries, convert findings to a formal PDF report, and secure the signed Milestone Acknowledgement (MA) form for LGMS internal auditing.

**Decisions Made:**
*   **Testing Scope:** Confirmed for UAT only; permissions granted for Create/Update/Delete in UAT.
*   **CORS Finding:** Deprioritized as "Informational" due to low ROI; identified as the sole remaining item in the final report.
*   **Reporting Format:** Pending conversion of results into a formal PDF format upon confirmation that no further queries exist from the client team.

**Pending Actions & Ownership:**
*   **[Owner: Ong Xiao Cong / LGMS]** Awaiting response regarding any outstanding queries and the signed MA form; prepared to generate final PDF report upon confirmation. *Action Date: Mar 30, 2026.*
*   **[Owner: Michael Bui / FairPrice Group]** Review attached MA form for signatures and confirm if there are any technical queries from the team regarding the March 24 deliverables.
*   **[Owner: Jazz Tong / FairPrice Group]** Assist Michael Bui with signing and submitting the MA form immediately upon receipt.

**Key Dates & Deadlines:**
*   **Mar 16, 2026:** Retest Window (Completed).
*   **Mar 24, 2026:** Final report delivered via secure link.
*   **Mar 25, 2026:** Michael Bui confirmed zero critical/high findings and resolved medium/low issues.
*   **Mar 31, 2026:** Secure link expiration deadline for accessing deliverables.
*   **Mar 30, 2026 (Mon), 2:08 AM:** Ong Xiao Cong sent follow-up email requesting query confirmation and the signed MA form.

**Status Summary:**
The retest concluded successfully on March 16, 2026. On March 24, LGMS delivered the final report via a secure link (https://lgms.online/s/Dpaizwt5cwaZTZW). Michael Bui confirmed on **March 25** that all critical/high findings are resolved, with only one CORS item remaining as "Informational."

On **March 30, 2026**, LGMS initiated a follow-up to:
1. Confirm if the client team has any queries regarding the shared results.
2. Proceed with generating the final report in PDF format pending confirmation of no issues.
3. Request the return of the attached Milestone Acknowledgement (MA) form for internal auditing purposes.

The project remains in the **Post-Delivery Review** phase, transitioning toward administrative closure. While technical sign-off is effectively complete, formal closure awaits the signed MA form and final PDF deliverable generation. The secure link used for initial delivery expires on March 31, 2026; however, the follow-up communication occurred prior to this expiration.


## [23/31] [Bitbucket]  Pipeline for master failed on 22b106d (ntuclink/website-service)
Source: gmail | Thread: 19d3c707df3654ae | Labels: Inbox, Updates | Priority: None | Senders: Bitbucket | Last Date: Mon, Mar 30, 2026, 1:51 AM | Last Updated: 2026-03-30T02:01:21.231015+00:00
**Daily Work Briefing: Bitbucket Pipeline Failure**

**1. Key Participants & Roles**
*   **Michael Bui**: Developer/Contributor (Committed code `22b106d`).
*   **Lester Santiago Soriano**: Approver of Pull Request #652.
*   **Zaw Myo Htet**: Approver of Pull Request #652.
*   **Bitbucket System**: Automated notification source (failed pipeline trigger).

**2. Main Topic/Request**
The `master` branch pipeline for the `ntuclink/website-service` repository on Bitbucket has failed immediately following a merge. The failure is attributed to test execution results in commit `22b106d`.
*   **Merge Context**: Pull Request #652 (Ticket: DPD-715), titled "Fix shared position map mutation in ReorderProductsAds".

**3. Pending Actions & Ownership**
*   **Action**: Investigate and resolve the pipeline failure where 0 out of 1,153 tests passed (interpreted as 1,153 tests failed based on standard CI failure reporting context).
*   **Owner**: Michael Bui (as the committer) or the development team responsible for `website-service`. No specific assignment is mentioned in the thread; ownership defaults to the author of the failing commit.

**4. Decisions Made**
*   The code change defined in DPD-715 was merged into the `master` branch despite subsequent pipeline failure, indicating the merge occurred before the full test suite validation or the CI gate failed post-merge.

**5. Key Dates, Deadlines & Follow-ups**
*   **Date/Time of Failure**: March 30, 2026, at 1:51 AM.
*   **Duration of Pipeline Run**: 6 minutes and 40 seconds.
*   **Commit Hash**: `22b106d`.
*   **Follow-up Required**: Immediate review of the test results to identify the cause of the mutation failure in `ReorderProductsAds` before further deployments.

**Summary**
The automated pipeline for `ntuclink/website-service` failed on March 30, 2026 (1:51 AM), halting progress on `master`. The failure occurred after Michael Bui merged PR #652 (DPD-715) approved by Lester Santiago Soriano and Zaw Myo Htet. The pipeline reported a critical test failure rate (0/1153 tests passed). Immediate investigation is required to address the shared position map mutation issue introduced in this commit.


## [24/31] Re: [Bitbucket] Pull request #652: DPD-715: Fix shared position map mutation in ReorderProductsAds (ntuclink/website-service)
Source: gmail | Thread: 19d3c5101edbc5b5 | Labels: Inbox, Updates | Priority: None | Senders: Zaw | Last Date: Mon, Mar 30, 2026, 1:46 AM | Last Updated: 2026-03-30T02:01:36.593132+00:00
**Daily Work Briefing: Pull Request #652 (DPD-715)**

**Key Participants & Roles**
*   **Zaw Myo Htet:** Reviewer/Approver.
*   **Lester Santiago Soriano:** Reviewer/Approver.
*   **Daryl Ng:** Reviewer/Approver.
*   **ntuclink/website-service:** Repository owner of the pull request.

**Main Topic/Request**
Review and approval of Pull Request #652 regarding ticket **DPD-715**. The PR addresses a technical defect titled "Fix shared position map mutation in ReorderProductsAds."

**Decisions Made**
Three separate approvals were recorded for this specific pull request:
1.  **Zaw Myo Htet** approved the changes on March 30, 2026, at 1:17 AM.
2.  **Lester Santiago Soriano** approved the changes on March 30, 2026, at 1:24 AM.
3.  **Daryl Ng** approved the changes on March 30, 2026, at 1:46 AM.

All three reviewers have officially signified approval for the code changes associated with DPD-715.

**Actions Pending & Ownership**
*   **Merge Action:** While approvals are secured, the specific action of merging the pull request is not explicitly detailed in this email thread as completed. The PR remains in a state where it has received necessary approvals.
*   **Ownership:** The merge responsibility typically falls to the repository maintainers or the original author (not listed in these approval notifications), though no specific owner was assigned a pending task in this text.

**Key Dates & Deadlines**
*   **March 30, 2026, 1:17 AM:** First approval received (Zaw Myo Htet).
*   **March 30, 2026, 1:24 AM:** Second approval received (Lester Santiago Soriano).
*   **March 30, 2026, 1:46 AM:** Third approval received (Daryl Ng).
*   **No deadlines or follow-up dates** are specified in the provided content.

**Summary Status**
The pull request #652 for DPD-715 has successfully secured three approvals within a 29-minute window on March 30, 2026. The technical issue regarding shared position map mutation in `ReorderProductsAds` has been validated by Zaw Myo Htet, Lester Santiago Soriano, and Daryl Ng.


## [25/31] You have no events scheduled today.
Source: gmail | Thread: 19d3b6b347f5f06b | Labels: Inbox, Updates | Priority: None | Senders: Google Calendar | Last Date: Sun, Mar 29, 2026, 9:06 PM | Last Updated: 2026-03-29T22:04:31.516241+00:00
**Daily Work Briefing Summary**

**Key Participants & Roles**
*   **Michael Bui**: Account holder (michael.bui@fairpricegroup.sg).
*   **Google Calendar System**: Automated notification sender.

**Main Topic/Request**
*   Automated delivery of a "daily agenda" notification confirming the absence of scheduled events for the specified date. This communication is triggered by subscription to the **"Digital Business Tech Release/Changes"** calendar.

**Pending Actions & Ownership**
*   **No actions pending.** The email explicitly states there are no events scheduled, and no tasks require attention or ownership as of this briefing.

**Decisions Made**
*   None recorded in this thread. This is an informational status update only.

**Key Dates, Deadlines, & Follow-ups**
*   **Notification Sent**: March 29, 2026, at 9:06 PM.
*   **Relevant Date**: Monday, March 30, 2026 (No events scheduled).
*   **Follow-up**: None required based on current content.
*   **Account Configuration**: If agenda settings need modification regarding which calendars are monitored, the user must log in to `https://calendar.google.com/calendar/`.

**Additional Metadata**
*   **Labels**: Inbox, Updates.
*   **Priority**: Unspecified (null).
*   **Last Message ID**: 19d3b6b347f5f06b.


## [26/31] Opsgenie Alert: [Datadog] [P2] [Triggered] Marketing Service Gateway Error
Source: gmail | Thread: 19d3ae5eb3b0090e | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Sun, Mar 29, 2026, 6:45 PM | Last Updated: 2026-03-29T22:04:50.307013+00:00
**Daily Work Briefing: Marketing Service Gateway Incident**

**1. Key Participants & Roles**
*   **System:** Opsgenie (Alerting System) receiving data from Datadog.
*   **Affected Team:** DPD Staff Excellence - Retail Media (`@opsgenie-dpd-grocery-retail-media`).
*   **Integration Source:** `dpd-grocery-retail-media-eu` (Datadog).

**2. Main Topic/Request**
An automated P2 alert triggered due to a production error spike in the Marketing Gateway service. The service is responsible for banners, video ads, and authentication.
*   **Error Volume:** >1,000 log events matched within the last 5 minutes.
*   **Monitored Query:** `service:martech-personalization-service-api-gateway env:prod status:error`.

**3. Pending Actions & Ownership**
*   **Action:** Investigate and resolve the high volume of error logs in the production environment for the Martech Personalization Service API Gateway.
*   **Owner:** DPD Staff Excellence - Retail Media (as designated responders).
*   **Reference Links:**
    *   Datadog Monitor: https://app.datadoghq.eu/monitors/65699796

**4. Decisions Made**
No manual decisions recorded in this thread; the alert was automated by system monitoring rules without human intervention noted in the log history.

**5. Key Dates & Timeline**
*   **Alert Trigger Time:** March 29, 2026, at 18:39:36 UTC (Last Updated).
*   **Notification Timestamps (Opsgenie):**
    *   Mar 29, 2026, 6:40 PM
    *   Mar 29, 2026, 6:42 PM
    *   Mar 29, 2026, 6:45 PM
*   **System Creation Timestamp:** Mar 30, 2026, at 2:40:37 AM (Note: This appears to be a system generation timestamp distinct from the alert trigger time).
*   **Alert ID:** `71c276fd-1010-4578-b555-effd2bb881a3-1774809637590` (TinyId: 139261).
*   **Last Message ID:** `19d3aea79f9a34bb`.

**Status Summary:** The alert has been generated and routed to the Retail Media team three times within a 5-minute window. No resolution or status update comments are present in the provided thread log. Immediate investigation is required by the assigned team.


## [27/31] Opsgenie Alert: [Datadog] [P2] [Warn] Service marketing-service has a high error rate on env:prod
Source: gmail | Thread: 19d35a661786941f | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Sun, Mar 29, 2026, 2:12 PM | Last Updated: 2026-03-29T22:05:24.977305+00:00
**Daily Work Briefing: Opsgenie Alert Summary (Updated)**

**Key Participants & Roles**
*   **System/Integration:** Opsgenie (Alerting) and Datadog (Monitoring Source).
*   **Responders/Owner:** DPD Staff Excellence - Retail Media.
*   **Notification Channels:** `@hangouts-dd-dpd-grocery-alert` (Google Hangouts) and `@opsgenie-dpd-grocery-retail-media`.

**Main Topic & Request**
An automated P2 warning alert remains active for the production environment (`env:prod`) regarding the `marketing-service`. The system detects a high HTTP error rate where the ratio of errors to total hits exceeds the 5% threshold (trigger condition: `> 0.05`). Despite recent metric improvements, the alert continues to trigger P2 notifications.

**Alert Details**
*   **Service:** `marketing-service`
*   **Environment:** Production (`prod`)
*   **Triggered Metric:** Error Rate over the last 10 minutes.
*   **Query:** `sum(last_10m):( sum:trace.http.request.errors{env:prod,service:marketing-service}.as_count()/sum:trace.http.request.hits{env:prod,service:marketing-service}.as_count() ) > 0.05`
*   **Threshold vs. Actual:** Threshold > 0.05; Current Metric Value: 0.014 (Latest update).
    *   *Note:* Previous values ranged from 0.044 to 0.011. The metric has stabilized at 0.014, yet the P2 alert persists.
*   **Alert ID/Event ID:** `2876abed-d7c2-442b-b7be-247333e4f4b5-1774793229072` / Event ID `8565278154849940428`.
*   **Monitor URL:** https://app.datadoghq.eu/monitors/17447106
*   **Snapshot Link:** https://app.datadoghq.eu/monitors/17447106?from_ts=1774792266000&to_ts=1774793466000&event_id=8565278154849940428
*   **Datadog Tags:** `env:prod`, `service:marketing-service`, `managed_by:datadog-sync`, `monitor`, `priority:p2`.

**Pending Actions & Ownership**
*   **Action:** Immediate investigation required to resolve why the P2 alert persists despite metric values (0.014) falling below the 5% threshold. Review recent alerts for recurrence and confirm if this is a false positive or intermittent issue.
*   **Owner:** DPD Staff Excellence - Retail Media.
*   **Required Checks (as per runbook):**
    1.  Review Datadog APM resources: [Datadog Link](https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod)
    2.  Review Kubernetes deployment status: [GCP K8s Link](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview?cloudshell=false&project=fponprd)
    3.  Consult the official Runbook: [Atlassian Wiki Link](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book)

**Decisions Made**
No human decisions were recorded in this thread; all entries are automated system notifications. The alert remains active as of Mar 29, 2026, at 14:06 UTC (Local time approx. 2:07 PM).

**Key Dates & Timeline**
*   **Latest Alert Update:** Mar 29, 2026, at 14:06:06 +0000 (Metric Value: 0.014).
*   **Notification Sent:** Mar 29, 2026, at 10:07:09 PM UTC (Created At), with subsequent identical notifications logged at 2:07 PM, 2:09 PM, and 2:12 PM local time.
*   **Previous Activity:** Earlier alerts on Mar 28, 2026, showed a metric value of 0.044.

**Status Note**
The alert status remains "Warn" (P2) for the production environment. Although the current metric value (0.014 or 1.4%) is significantly below the 5% threshold (>0.05), the system continues to generate P2 notifications. Immediate investigation per the provided links and runbook is required to determine why the alert persists despite improved metrics and to rule out intermittent issues.


## [28/31] [Action Required] Service Account Key Expiring, Renewal Required - a36a1c8b456f387db4ba32e73f8a243479423bf0
Source: gmail | Thread: 19d38b3c9f3ad7ec | Labels: Inbox, Forums | Priority: None | Senders: noreply-sre | Last Date: Sun, Mar 29, 2026, 8:26 AM | Last Updated: 2026-03-29T10:01:34.356027+00:00
**Daily Work Briefing: Service Account Key Expiration Notice**

*   **Key Participants & Roles:**
    *   **Sender:** `noreply-sre@ntucenterprise.sg` (SRE Team/Notification System).
    *   **Recipient:** The service account owner responsible for the `fpon-224503/seller-analytics-service`.

*   **Main Topic/Request:**
    *   Notification that the service account key `a36a1c8b456f387db4ba32e73f8a243479423bf0` for the account `fpon-224503/seller-analytics-service@fpon-224503.iam.gserviceaccount.com` is scheduled to expire.
    *   Immediate instruction to rotate this key before expiration to prevent authentication failures and service disruption.

*   **Pending Actions & Ownership:**
    *   **Action:** Download the newly issued service account key (sent separately) and replace the existing key in the target system.
    *   **Owner:** The ticket owner/service account administrator.
    *   **Alternative Action:** If the key is determined to be stale, a SRE request must be raised to permanently remove it.

*   **Decisions Made:**
    *   None recorded in this thread; this is an automated notification requiring recipient action.

*   **Key Dates & Deadlines:**
    *   **Notification Date:** March 29, 2026 (8:26 AM).
    *   **Expiration Deadline:** April 28, 2026. The key becomes invalid after this date.
    *   **Follow-up:** Await the separate email containing the new service account credentials to initiate rotation immediately upon receipt.


## [29/31] [Dashboard Report] Retail Media - DD Dashboard | Sun 29 Mar 11:00AM +08
Source: gmail | Thread: 19d378a961f79e91 | Labels: Inbox, Updates | Priority: None | Senders: Datadog HQ | Last Date: Sun, Mar 29, 2026, 3:02 AM | Last Updated: 2026-03-29T06:01:45.068609+00:00
**Daily Work Briefing: Retail Media Datadog Dashboard Update**

**Key Participants & Roles**
*   **Datadog HQ (no-reply@dtdg.eu):** Service Provider/Sender. Automated sender on behalf of the "Team Datadog."
*   **Michael:** Recipient (Internal Stakeholder/Client). Primary point of contact for the report delivery.

**Main Topic & Request**
Delivery of the **"Retail Media - DD Dashboard"** report containing data aggregated over the past three days leading up to March 29, 2026. The email serves as a notification that the attachment is available for review and monitoring purposes.

**Pending Actions & Ownership**
*   **Action:** Review the attached dashboard report (containing 3 days of historical data).
*   **Owner:** Michael.
*   **Status:** Awaiting receipt/acknowledgment or internal analysis by Michael. No further action from Datadog HQ is required at this stage.

**Decisions Made**
None recorded in this thread. The communication is a standard automated delivery notification without explicit decision-making logs.

**Key Dates & Deadlines**
*   **Report Generation Date:** Sunday, March 29, 2026 (11:00 AM +08).
*   **Data Range:** Past 3 days relative to the report generation date.
*   **Sent Timestamp:** March 29, 2026, at 3:02 AM (Timezone not specified in body, but server timestamp indicates early morning UTC/Europe likely given "HQ <no-reply@dtdg.eu>").

**Specific References & Metadata**
*   **Report Title:** Retail Media - DD Dashboard.
*   **Sender Email:** no-reply@dtdg.eu.
*   **Last Message ID:** 19d378a961f79e91.
*   **Labels:** Inbox, Updates.
*   **Datadog HQ Address:** 620 8th Avenue, 45th Floor, New York, NY 10018.
*   **Recipient Name:** Michael.

**Summary for Executive Review**
The automated system from Datadog HQ successfully delivered the latest Retail Media performance report to Michael on March 29, 2026. The content covers a 72-hour window ending at the time of generation. No follow-up requests or escalations were initiated by the sender; the ball is now in Michael's court to analyze the metrics.


## [30/31] Opsgenie Alert: [Datadog] [P4] [Triggered] Service marketing-service has an abnormal change in throughput on env:prod
Source: gmail | Thread: 19d36f49cbc748cd | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Sun, Mar 29, 2026, 1:26 AM | Last Updated: 2026-03-29T02:01:05.109307+00:00
**Daily Work Briefing: Opsgenie Alert Summary**

**1. Key Participants & Roles**
*   **System:** Opsgenie (Alerting System) and Datadog (Monitoring Source).
*   **Notification Targets:**
    *   `@hangouts-dd-dpd-grocery-alert` (Hangouts Group: Operations/Incident Response).
    *   `@opsgenie-dpd-grocery-retail-media` (Opsgenie Team Channel).
*   **Assigned Responders:** DPD Staff Excellence - Retail Media.

**2. Main Topic & Request**
*   **Subject:** Abnormal throughput change detected in the `marketing-service` production environment (`env:prod`).
*   **Alert Type:** P4 Priority Anomaly Detection.
*   **Trigger Condition:** 100% of trace HTTP request hit values deviated by more than 3 standard deviations from predicted values over a 15-minute window.
*   **Requested Actions:** Immediate investigation via provided links to Datadog APM, Google Kubernetes Engine (GKE) deployment overview, and the specific Runbook.

**3. Pending Actions & Ownership**
*   **Action:** Investigate service throughput anomaly using supplied monitoring links.
*   **Owner:** DPD Staff Excellence - Retail Media (Assigned via Opsgenie responder group).
*   **Reference Links Provided:**
    *   Datadog APM: `marketing-service` operations.
    *   Kubernetes Console: `asia-southeast1/fpon-cluster/default/marketing-service`.
    *   Runbook: `NTUCLink - marketing-service Run book`.

**4. Decisions Made**
*   No human decisions or mitigations recorded in this thread yet; the content consists entirely of automated system alerts indicating an ongoing, unresolved issue.

**5. Key Dates & Timeline**
*   **March 29, 2026, 12:18 AM (UTC):** Initial alert triggered. Last Updated: 00:17:10 +0000. Created At: 08:18:13 AM (System timestamp).
*   **March 29, 2026, 12:23 AM (UTC):** Duplicate alert received (Last Updated same as initial).
*   **March 29, 2026, 1:21 AM (UTC):** Alert updated/retriggered. Last Updated: 01:20:10 +0000. Created At: 09:21:12 AM (System timestamp).
*   **March 29, 2026, 1:26 AM (UTC):** Duplicate of the 1:21 AM alert received.

**Status:** Alert remains active with repeated notifications indicating no resolution or acknowledgment has been logged in this thread.


## [31/31] [RAW Overdue] Expired Risk Acceptance & Waiver Form
Source: gmail | Thread: 19d371d74be27bd7 | Labels: Inbox | Priority: None | Senders: cyberrisk.automation | Last Date: Sun, Mar 29, 2026, 1:02 AM | Last Updated: 2026-03-29T02:01:22.713174+00:00
**Daily Briefing: Resource [RAW Overdue] Expired Risk Acceptance & Waiver Form**

**Key Participants & Roles**
*   **Cyber Risk Team / Automation System:** Sender of the reminder; responsible for monitoring expiry and reviewing remediation evidence. Contact: `cyberRisk@ntucenterprise.sg`.
*   **Technology Governance and Compliance Team:** Recipient for form sharing to ensure correct completion prior to sign-off. Contact: `techgrc@ntucenterprise.sg`.
*   **Requestor (Entity Owner):** The individual responsible for raising the new RAW request, completing Section A, and securing approvals. Currently unspecified in thread but is the target audience of this alert.

**Main Topic/Request**
The system has detected an expired Risk Acceptance & Waiver (RAW) form for the asset **Signcloud Saas User access management** (Entity: FPG-Fairprice). The original waiver expired on **May 15, 2025**, due to a lack of user access management by the respective business owner. The requestor must either provide evidence of remediation or submit a new RAW form immediately.

**Pending Actions & Ownership**
*   **Action:** Determine if residual risks have been remediated.
    *   *If Yes:* Provide evidence to `cyberRisk@ntucenterprise.sg` for closure review.
    *   *If No:* Initiate a new RAW request via Gsuite immediately. This action is owned by the **Requestor**.
*   **Action:** If submitting a new form, complete Section A of the template and share it with `cyberRisk@ntucenterprise.sg` for pre-submission review and with `techgrc@ntucenterprise.sg`. Ownership: **Requestor**.
*   **Action:** Obtain sign-offs on Google Docs (full names or initials) accompanied by specific comments stating "Approved" or "Signed". Ownership: **Approvers**.
*   **Ownership Note:** The automation system will continue sending reminders until the new RAW is approved.

**Decisions Made**
No decisions were made in this thread; it serves as a notification of non-compliance and an instruction to act. The process requires all interactions and approvals to occur strictly within Google Docs (via Gsuite), not via email downloads.

**Key Dates & Deadlines**
*   **Current Date:** March 29, 2026.
*   **Original Expiry Date:** May 15, 2025.
*   **Status:** Overdue (expired ~1 year ago).
*   **Follow-up:** Continuous reminders will be sent until a new form is approved. Immediate action is required to stop the cycle.

**Specific References**
*   **RAW ID:** RAW-20240306_01-v1.0
*   **Email Address (Sender):** `cyberrisk.automation@fairpricegroup.sg`
*   **Email Address (Remediation/Review):** `cyberRisk@ntucenterprise.sg`
*   **Email Address (Governance):** `techgrc@ntucenterprise.sg`
