

## jira/RM-697: Web - OG Home - Testhas Offer swimlane - Ad label is missing for the first listed product
Source: jira | Key: RM-697 | Status: To Do (To Do) | Type: Bug | Priority: High | Assignee: Michael Bui | Reporter: Madhuri Nalamothu | Labels: found-in-e2e-automation, priority:health
**Executive Briefing Summary: RM-697**

**1. Current Status/State**
*   **Ticket ID:** RM-697
*   **Status:** To Do (Re-opened for verification)
*   **Type:** Bug | **Priority:** High | **Labels:** `found-in-e2e-automation`, `priority:health`
*   **Issue:** On the Web platform, the "Ad" label is missing from the first listed product within the "Testhas Offer swimlane" on the OG Home page. This issue is isolated to Web; iOS and Android versions function correctly.
*   **Environment Details:** Postcode `098619` required for reproduction.
*   **Evidence:** E2E automation result available at `https://app.testsigma.com/ui/td/test_case_results/16571301/step_results`.

**2. Pending Actions & Ownership**
*   **Action:** Re-verify the reported bug to confirm if the issue persists under current conditions.
*   **Owner:** Michael Bui (Assignee) requested verification assistance from the reporter/QE team on Jan 6.
*   **Latest Update:** On Jan 14, Michael Bui confirmed he verified the specific test account provided by the QE team and observed the ad displaying correctly ("I can see the ad is showing"). However, the ticket status remains "To Do," indicating the discrepancy between the original bug report and this verification requires further investigation or clarification before closure.

**3. Decisions Made**
*   **Platform Scope:** Confirmed the defect is specific to the Web interface; mobile platforms (iOS/Android) are not affected.
*   **Verification Protocol:** The team agreed to test with the specific valid credentials and postal code (`098619`) provided in the initial report.

**4. Key Dates & Blockers**
*   **05 Jan 2026 (15:13):** Issue reported by Madhuri Nalamothu. Ticket marked as High Priority Bug.
*   **06 Jan 2026 (11:19):** Michael Bui requested re-verification, noting he could see the ad at that time.
*   **14 Jan 2026 (15:28):** Michael Bui reported verification with the QE team's test account resulted in the ad appearing correctly.
*   **Blockers:** None currently listed; however, the "To Do" status persists despite recent successful verification attempts, suggesting a need to reconcile the automation failure (Jan 5) with manual success (Jan 14).

**Summary of Conflict:** A high-priority E2E automation failure on Jan 5 reported a missing Ad label. Subsequent manual checks by Michael Bui on Jan 6 and Jan 14 suggest the feature is working correctly when using the specified test account, creating a need to determine if this was a transient state, environment-specific issue, or an automation flake that requires re-investigation rather than immediate code fix.


## jira/RM-693: [Retail Media OSMOS] Missing Unicharm SKU
Source: jira | Key: RM-693 | Status: Cancelled (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Pamela Koh | Due: 2025-12-15 | Resolution: Done | Labels: priority:health, priority:improvement | relates: RM-694, RM-694
**Ticket Summary: RM-693 [Retail Media OSMOS] Missing Unicharm SKU**

*   **Current Status:** Cancelled (Resolution: Done).
    *   The ticket was initially raised to address two missing SKUs under vendor "DKSH Unicharm" (Code: 52513, Brand ID: 9909) in the OSMOS system.
*   **Key Actions & Findings:**
    *   **Initiation (Dec 11):** Reporter Pamela Koh flagged missing SKUs `13086873` and `13085255`.
    *   **Investigation (Dec 17):** Assignee Michael Bui verified via terminal commands (`grep`) that both products exist in the sync files (`fpg-...jsonl`).
        *   Confirmed data presence: Both SKUs are active ("ENABLED"), indexed, and mapped to vendor code `52513` in the `sku-vendor-mapping.tsv`.
        *   Found product details (e.g., "MamyPoko Air Fit Diapers") with associated tags and stock visibility.
    *   **Resolution Path:** Michael Bui requested the OSMOS support ticket number from Pamela Koh to investigate why these products were previously rejected by OSMOS despite being present in the source sync files.
*   **Decisions Made:** The issue was resolved internally by confirming data availability, but the root cause of the rejection remains under investigation pending external support validation. Consequently, the Jira ticket was marked as Cancelled/Done without a code fix, likely due to the finding that the data *is* present.
*   **Pending Actions:** None explicitly stated in the final comment, though the initial comment indicated a need for an OSMOS support ticket reference to proceed with backend rejection analysis.
*   **Ownership:**
    *   Assignee: Michael Bui (Investigation lead).
    *   Reporter: Pamela Koh (Initial flagger).
*   **Key Dates & Reference IDs:**
    *   Ticket Created/Status Update: 2025-12-11.
    *   Investigation Comment: 2025-12-17.
    *   Due Date: 2025-12-15 (Note: Actual work occurred after the due date).
    *   Linked Issue: RM-694 (Relates).
    *   Technical References: `fpg-01KCND9AXZN39ZPVMARVMCMWNG-20251217_134219.jsonl`, `sku-vendor-mapping-20251119.tsv`.


## jira/RM-694: [Retail Media OSMOS] Missing Nino Nana SKU
Source: jira | Key: RM-694 | Status: Cancelled (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Pamela Koh | Due: 2025-12-19 | Resolution: Done | Labels: priority:health, priority:improvement | relates: RM-693, RM-693
**Jira Ticket Briefing: RM-694 [Retail Media OSMOS] Missing Nino Nana SKU**

**Current Status:** Cancelled / Done (Resolved)
*   **Assignee:** Michael Bui
*   **Reporter:** Pamela Koh
*   **Priority:** High
*   **Resolution:** The issue was identified as a configuration error in AdOps, not a data sync failure.

**Key Findings & Decisions**
1.  **Root Cause Identified:** On 2025-12-19, Michael Bui confirmed the root cause was incorrect brand-vendor mapping sent to OSMOS by AdOps (tickets RM-693 and RM-694 share this issue), rather than missing data in sync files.
2.  **Data Verification:** On 2025-12-17, Michael Bui verified that 60 SKUs requested for "Nino Nana" (Vendor Code: 32139, Brand ID: 34945) exist in both the sync files (`fpg-*.jsonl`) and the vendor mapping file (`sku-vendor-mapping-20251119.tsv`).
3.  **Data Anomalies:** Two SKUs (90228729, 90228800) were found duplicated in the source Excel list provided by the reporter.
4.  **OSMS Support Context:** The specific SKUs were flagged as "unavailable" in Nino Nana within OSMOS but existed in the Platform Ops account.

**Action Items & Ownership**
*   **Past Actions (Completed):**
    *   Investigated SKU presence in sync files and mapping tables (Michael Bui).
    *   Escalated to OSMOS support to investigate why 60 products were rejected (Pamela Koh).
*   **Pending Actions:** None. The ticket is closed with a root cause analysis provided for future reference.

**Key Dates & References**
*   **Ticket Opened/Cancelled:** 2025-12-16 to 2025-12-19 (Due date: 2025-12-19).
*   **Investigation Date:** 2025-12-17 (SKU verification completed).
*   **OSMS Support Ticket:** #107110 and #11274 (Monetize Admin project type).
*   **Linked Issues:** Relates to RM-693.
*   **Technical References:**
    *   Vendor: Nino Nana (Code: 32139, Brand ID: 34945).
    *   Files analyzed: `fpg-01KCNCTZ26F5WP5DTYA95KM6C2-20251217_133428.jsonl`, `fpg-01KCNCTVVY2DPA23W24RC6QV8Y-20251217_133425.jsonl`.
    *   Mapping file: `../sku-vendor-mapping-20251119.tsv`.
*   **Blockers:** Resolved by identifying the AdOps mapping error.


## jira/RM-613: Update Opsgenie Notification Rules
Source: jira | Key: RM-613 | Status: Cancelled (Done) | Type: Ops | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done
**Daily Briefing Summary: RM-613**

*   **Ticket ID:** RM-613
*   **Title:** Update Opsgenie Notification Rules
*   **Status:** Cancelled (Category: Done)
*   **Priority:** High
*   **Owner/Assignee:** Michael Bui
*   **Reporter:** Michael Bui
*   **Type:** Ops

**Current Status & Resolution**
The ticket was marked as **Cancelled** with a resolution of **Done**. The work is considered complete in terms of administrative closure, though no technical changes were implemented.

**Key Technical Reference**
The scope involved attempting to update notification rules at the following URL: `https://fairprice.app.opsgenie.com/settings/user/notification`. The objective was blocked because the interface currently lacks an option to modify these specific rules.

**Action Items & Ownership**
*   **Pending Actions:** None. As the ticket is resolved/cancelled, there are no outstanding tasks assigned to Michael Bui or other parties regarding this specific request.
*   **Ownership:** The issue was self-reported and closed by Michael Bui without escalation or reassignment.

**Decisions Made**
The decision to cancel was made because the required functionality (updating notification rules) does not exist within the current Opsgenie user settings interface. No alternative workarounds or configuration changes were applied; the request is effectively moot due to platform limitations.

**Dates & Blockers**
*   **Recorded Date:** 2025-09-10 (Ticket status update logged at 10:27:16).
*   **Deadline:** None originally assigned (`duedate` null).
*   **Blocker:** Platform limitation; the "Update" option is unavailable in the target URL path.

**Summary for Executive Review**
Michael Bui reported a High priority request to update Opsgenie notification rules but was unable to proceed due to missing UI options at the specified endpoint. Rather than finding a workaround, the ticket was immediately cancelled and marked Done on 2025-09-10. No further action is required from the operations team for this specific item.


## jira/BED-67: Secret management via CI/CD pipeline with Google Secret Manager (GSM)
Source: jira | Key: BED-67 | Status: In Production (Done) | Type: Idea | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui
**Daily Briefing Summary: Resource BED-67**

**Current Status & State**
*   **Ticket:** BED-67 (Secret management via CI/CD pipeline with Google Secret Manager).
*   **Status:** In Production (Done).
*   **Type:** Idea | **Priority:** High.
*   **Assignee/Reporter:** Michael Bui.

**Key Technical Implementation**
The solution establishes two distinct Bitbucket pipelines to manage secrets: `preprod_secrets` for the preproduction environment and `prod_secrets` for production. The system utilizes an auto-detection mechanism for variables prefixed with `ENV_SECRET_`. It parses these variables to inject them into Google Secret Manager (GSM); the prefix is removed, and the remainder becomes the GSM secret key, while the variable value becomes the secret payload.
*   *Example:* Variable `ENV_SECRET_DB_PASSWORD` creates a GSM entry named `db-password`.

**Decisions Made & Ownership**
1.  **Architecture Decision:** Secrets are to be managed and injected directly by Bitbucket repositories using the defined pipeline structure.
2.  **Ownership:** Michael Bui owns the implementation, documentation, and execution of this initiative.
3.  **Documentation:** Final instructions for operating this system were documented on October 12, 2025.

**Timeline & Key Dates**
*   **Initiation:** September 24, 2025 (Ticket creation and scope definition).
*   **Validation:** September 29, 2025 (Sample run conducted).
*   **Completion/Documentation:** October 12, 2025 (Final documentation published; Status marked "In Production").

**Pending Actions & Blockers**
*   **Pending Actions:** None. The ticket resolution is null, and the status confirms the work is done and in production.
*   **Blockers:** No blockers reported.


## jira/RM-665: Omni Homepage product ads shown as "TPA" on OSMOS dashboard
Source: jira | Key: RM-665 | Status: Cancelled (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Resolution: Done | Labels: priority:health | parent: RM-459
**Jira Ticket Briefing: RM-665**

**Current Status & State**
*   **Ticket ID:** RM-665 (Parent: RM-459)
*   **Status:** Cancelled / Done.
*   **Resolution:** Completed.
*   **Priority:** High.
*   **Labels:** `priority:health`.

**Decisions & Outcomes**
*   **Decision:** The ticket was cancelled and marked as "Done," indicating the issue regarding Omni homepage product ads displaying incorrectly on the OSMOS dashboard has been addressed or deemed resolved without further action required by this specific story.
*   **Issue Context:** Previously, Omni homepage ads were incorrectly categorized under "TPA" instead of the distinct "Omni home" page type. The requirement was to separate this inventory from "OG Home."

**Ownership & Actions**
*   **Assignee:** Michael Bui (owned the implementation).
*   **Reporter:** Nikhil Grover (identified the need as an RMN PM).
*   **Pending Actions:** None. The ticket is closed with a resolution of "Done."

**Key Dates & Blockers**
*   **Tracking Date:** 2025-10-14T14:43:25+08:00 (Status update recorded).
*   **Due Date:** None set.
*   **Blockers:** No active blockers listed; the item is resolved/cancelled.

**Technical Summary**
The objective was to ensure OSMOS dashboard metrics correctly distinguish between "Omni home" and "OG home" page types for product ads. The acceptance criteria required that ads on the Omni homepage be recorded as "Omni home" rather than "TPA," and ads on OG homepages remain distinct. This work is now concluded under the umbrella of Production Issues (RM-459).


## jira/RM-689: Limit product ads to 30% of search results
Source: jira | Key: RM-689 | Status: To Do (To Do) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Labels: priority:improvement
**Daily Briefing: Jira Ticket RM-689**

*   **Current Status:** The ticket is in the **"To Do"** state. No development work has commenced, and there is no resolution date set.
*   **Pending Actions & Ownership:** Implementation of the feature to limit product ads requires execution by **Michael Bui**. The requirement stems from an observation by reporter **Nikhil Grover** regarding poor user experience on low-result searches.
*   **Decisions Made:** No technical or design decisions have been recorded yet in the chronological log; this is a new high-priority improvement story initiated to address ad saturation.
*   **Key Dates & Blockers:**
    *   **Created/Logged:** November 18, 2025, at 14:45 UTC+8.
    *   **Deadline:** None assigned (`null`).
    *   **Blockers:** None identified in the current ticket metadata.

**Summary of Requirements:**
The story addresses an issue where sponsored products currently dominate search results on low-volume queries within the FPG app and website, negatively impacting customer experience. The specific acceptance criteria mandate that for any product search, sponsored results must not exceed **30%** of the total returned results (sponsored + organic). This is tagged as a `priority:improvement` with a **High** priority level.


## jira/RM-684: Banner ads cannot be targeted by platform (Android/iOS)
Source: jira | Key: RM-684 | Status: To Do (To Do) | Type: Bug | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Labels: priority:health | parent: RM-459
**Daily Briefing Summary: RM-684**

**Ticket Overview**
*   **ID:** RM-684
*   **Title:** Banner ads cannot be targeted by platform (Android/iOS)
*   **Type/Status:** Bug / To Do
*   **Priority:** High (Label: `priority:health`)
*   **Parent Epic:** RM-459 (Production Issues)

**Current State & Issue Identification**
The ticket reports a functional defect where banner ad targeting fails based on device platform. Specifically, **Ad requests originating from Android devices do not include the platform identifier in the request payload**. Consequently, logical rules designed to target ads by platform (Android/iOS/Web/mWeb) are non-functional for Android traffic.

**Ownership & Pending Actions**
*   **Assignee:** Michael Bui is currently responsible for resolving this issue.
*   **Reporter:** Nikhil Grover identified and logged the defect on 2025-10-23.
*   **Pending Action:** No specific technical resolution steps are detailed in the current log; however, as the status remains "To Do," Michael Bui must investigate why Android ad requests omit platform data and implement a fix to ensure platform parameters are included in all requests.

**Decisions & Dates**
*   **Decisions Made:** None recorded in the chronological logs provided. The ticket has been logged but no solution strategy or engineering decision has been documented yet.
*   **Key Dates:**
    *   Date Logged: 2025-10-23T17:45:18.768+0800
    *   Due Date: None set (null).

**Blockers & Risks**
*   **Primary Blocker:** The absence of platform data in the request prevents any platform-specific ad targeting logic from executing for Android users.
*   **Risk Level:** High priority, categorized under `priority:health`, indicating this impacts core production functionality and user experience regarding ad delivery.

**Technical References**
*   **Affected Platforms:** Android (specifically noted as failing), iOS, Web, mWeb (expected targets).
*   **Component Failure:** Ad request payload construction for Android.


## jira/ID-5062: Optimise product page query
Source: jira | Key: ID-5062 | Status: Released (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Tan Nhu Duong | Resolution: Done | Labels: priority:health | parent: ID-5060
**Ticket Summary: ID-5062 (Optimise product page query)**

**Current Status & State**
*   **Status:** Released / Done.
*   **Deployed:** Changes are live in Production (PRD) as of Oct 13, 2025, but the feature flag `be_layout_r4u_response_cache` is currently **OFF**.
*   **Observations:** Following deployment on Oct 13, Redis memory usage decreased immediately despite the flag being off. Post-deployment metrics (Oct 17) show a reduction in Algolia search calls after 5 PM when traffic was rolled out to 100%.

**Pending Actions & Ownership**
*   **Action:** Enable the `be_layout_r4u_response_cache` feature flag for a small percentage of traffic first.
    *   **Owner:** Tan Nhu Duong (implied based on initial request context).
    *   **Deadline:** Immediate (to validate cost reduction and minimize risk).
*   **Configuration Check:** Ensure Split.io user segments are configured to use `customerID`. Segments using `customerUID` will not function correctly.
    *   **Owner:** Michael Bui / Platform Team.

**Decisions Made**
1.  **Scope Expansion:** Cache key logic extended beyond `customerId/storeId` to include `RecType` and `pageNumber` (e.g., `R4U_RESP:{customerID}:{storeID}:{recommendationType}:{pageNumber}`).
2.  **Exclusion Logic:** Caching will be excluded if the request requires product ads.
3.  **Rollout Strategy:** Adopt a phased rollout starting with low traffic percentage before enabling 100% to mitigate risk.
4.  **Feature Flagging:** Implementation controlled via Split.io flag `be_layout_r4u_response_cache` (Default: OFF).

**Key Dates & Technical References**
*   **2025-09-25:** Ticket created; requirement defined (reduce Algolia costs for "Recommended For You").
*   **2025-10-06:** Cache key structure finalized; Split.io flag creation requested.
*   **2025-10-07:** Implementation details documented; exclusion of product ads decided.
*   **2025-10-13:** Code deployed to PRD (Flag OFF). Redis memory usage dropped unexpectedly.
*   **2025-10-17:** Performance data confirmed showing Algolia call reduction post-deployment.
*   **Technical Configs:**
    *   Cache TTL: 1 hour (configurable via `R4U_RESP_TTL` env variable).
    *   Parent Ticket: ID-5060 ([Platform Health] Optimising Algolia usage for cost reduction).
    *   References: Datadog trace URL and GCP Memorystore console link provided in comments.

**Blockers/Notes**
*   None currently active; awaiting traffic ramp-up to fully validate cost savings against the initial unexpected Redis memory drop.


## jira/RM-677: Raise RAW request to proceed with vendor evaluation trial without SRA
Source: jira | Key: RM-677 | Status: Cancelled (Done) | Type: Ops | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Resolution: Done
**Daily Briefing Summary: RM-677**

*   **Current Status:** The ticket is **Cancelled** with a resolution status of **Done**. No further work is required.
*   **Pending Actions:** None. All associated tasks have been closed out as the request was cancelled.
*   **Key Decisions:** The decision to proceed with raising a RAW (Request for Approval/Work) for a vendor evaluation trial without an SRA (Security Risk Assessment) was made but subsequently rescinded, leading to the cancellation of this specific ticket.
*   **Ownership & Timeline:**
    *   **Ticket ID:** RM-677
    *   **Assignee:** Michael Bui
    *   **Reporter:** Nikhil Grover
    *   **Priority:** High
    *   **Issue Type:** Ops
    *   **Key Date:** The ticket was formally marked as Cancelled/Done on **2025-10-17** at 17:16:09 (UTC+08).
*   **Blockers/Constraints:** There were no explicit blockers noted in the chronological log; the cancellation implies a change in strategy or requirement alignment that removed the need for this specific RAW request.


## jira/RM-674: Investigate the logs usage of martech-ad-event-sub
Source: jira | Key: RM-674 | Status: To Do (To Do) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Maou Sheng Lee | Labels: priority:health, priority:improvement
**Daily Briefing Summary: RM-674**

**Ticket:** RM-674 – Investigate the logs usage of *martech-ad-event-sub*  
**Status:** To Do | **Priority:** High | **Type:** Chore  
**Assignee:** Michael Bui | **Reporter:** Maou Sheng Lee  
**Labels:** `priority:health`, `priority:improvement`

**Objective:**
Investigate current log usage patterns for the *martech-ad-event-sub* service within Datadog Logs (DPD Datadog Log Management). The goal is to establish a clear understanding of the current state, pending actions, and ownership across the logging infrastructure.

**Required Analysis & Deliverables:**
1.  **Current Status Assessment:** Determine the existing operational state of logs for *martech-ad-event-sub*.
2.  **Action & Ownership Mapping:** Identify all pending tasks related to this investigation and assign specific owners to each.
3.  **Decision Log:** Document any decisions made regarding log ingestion, retention, or analysis strategies during the review.
4.  **Timeline & Blockers:** Pinpoint key dates, deadlines (currently none set), and identify any technical or operational blockers preventing progress.

**Technical Context:**
*   **Log Source:** DPD Datadog Log Management – *martech-ad-event-sub*.
*   **Access Point:** Datadog Logs viewer (DD Logs pattern).

**Next Steps for Assignee (Michael Bui):**
*   Access the Datadog Logs viewer immediately.
*   Execute a gap analysis against the "Instructions" listed above to generate a status report.
*   Note: No due date has been assigned; however, the High priority and health labels suggest immediate attention is required upon task initiation.

**Key Dates:** None currently defined in ticket metadata.  
**Resolution Status:** Open (null).


## jira/PRDM-29: [Postmortem] Prevent the Search Indexer cronjob from being evicted due to GKE Auto-Scaling events
Source: jira | Key: PRDM-29 | Status: Completed (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Due: 2025-04-03 | Resolution: Done | Labels: Postmortem, sprint2 | parent: PRDM-32 | problem/incident: PRDM-469
**Daily Briefing Summary: PRDM-29**

**Current Status**
*   **State:** Completed (Done).
*   **Resolution:** The Postmortem action item to prevent Search Indexer eviction has been successfully implemented.

**Key Actions & Ownership**
*   **Action:** Implementation of a PodDisruptionBudget (PDB) named `fp-search-indexer-pdb` with `minAvailable: 1`. This ensures the Search Indexer remains available during GKE auto-scaling events, node maintenance, and cluster upgrades to reduce MTTR.
*   **Execution:** Created in UAT on 2025-04-02 at 16:00; deployed to PRD on 2025-04-02 at 16:22.
*   **Verification:** Search functionality confirmed as normal on 2025-04-02 at 17:19.
*   **Owner:** Michael Bui (Assignee/Reporter).

**Decisions Made**
*   **Mitigation Strategy:** Adopted a PodDisruptionBudget approach rather than other scaling configurations to specifically address pod eviction during node under-utilization (detected after 15 minutes of low usage), directly addressing the root cause identified in incident PRDM-469.

**Key Dates, Deadlines & Context**
*   **Incident Reference:** Linked Problem/Incident ticket **PRDM-469**.
*   **Parent Epic:** Part of **PRDM-32** (Search Indexer Issues).
*   **Reminders:** A deadline reminder was issued by Sneha Parab on 2025-04-01 regarding the due date.
*   **Original Due Date:** 2025-04-03 (Ticket closed prior to this date).
*   **Labels:** Postmortem, sprint2.

**Blockers/Outstanding Issues**
*   None. The ticket is resolved with no pending actions.


## jira/RM-630: Onboard DiffMind Code Review AI to RMN Repos
Source: jira | Key: RM-630 | Status: To Do (To Do) | Type: Ops | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui
**Daily Briefing Summary: RM-630**

**Current Status**
The ticket **RM-630** ("Onboard DiffMind Code Review AI to RMN Repos") is currently in the **"To Do"** status. It is classified as a **High** priority **Ops** issue.

**Ownership & Pending Actions**
*   **Owner:** Michael Bui (Assignee and Reporter).
*   **Pending Action:** The ticket contains an empty "PR" (Pull Request) field dated **2025-10-12**, indicating the code submission or review artifact has not yet been attached. The primary pending step is to finalize and link the PR for this onboarding task.

**Decisions Made**
*   **Action Taken:** A repository webhook for DiffMind was successfully configured as of **2025-10-12** (entry timestamp 21:13:18). This confirms the infrastructure integration point is active, pending the code PR to trigger the review logic.

**Key Dates & Deadlines**
*   **Last Activity:** **2025-10-12**.
*   **Deadline:** No due date (null) is currently set on the ticket.
*   **Blockers:** None explicitly listed; however, the lack of a linked PR since Oct 12 suggests a process pause awaiting code submission.


## jira/RM-645: Documentation of SKU mapping sync
Source: jira | Key: RM-645 | Status: To Do (To Do) | Type: Ops | Priority: High | Assignee: Michael Bui | Reporter: John Henji Mantaring | discovery---connected: RM-634
**Briefing Summary: RM-645 Documentation of SKU mapping sync**

*   **Current Status:** The ticket is in **"To Do"** status with a **High** priority. It is classified as an **Ops** task.
*   **Ownership:**
    *   **Assignee:** Michael Bui (responsible for execution).
    *   **Reporter:** John Henji Mantaring.
*   **Dependencies & Context:** This task is linked as a **"Discovery - Connected"** issue to ticket **RM-634**. Documentation of the SKU mapping sync process is pending validation based on findings from that discovery phase.
*   **Pending Actions:**
    *   Michael Bui must author the documentation detailing the current status and state of the SKU mapping sync.
    *   John Henji Mantaring requires this output for review and validation (as noted in comments dated 2025-10-03).
*   **Decisions & Deadlines:** No specific decisions or due dates have been recorded in the metadata or timeline as of the latest entry. The task remains unassigned a completion target.
*   **Key Dates:**
    *   Issue Creation/Update: 2025-10-01 (Initial status set).
    *   Review Request: 2025-10-03T15:21:07+0800 (John Henji Mantaring requested documentation for review).

**Executive Note:** Immediate attention is required from Michael Bui to draft the documentation, as this is a High-priority Ops task dependent on the linked discovery work. No blockers are currently listed.


## jira/RM-644: Documentation of secondary category targeting
Source: jira | Key: RM-644 | Status: To Do (To Do) | Type: Ops | Priority: High | Assignee: Michael Bui | Reporter: John Henji Mantaring
**Daily Briefing Summary: RM-644**

*   **Current Status:** The ticket is in **"To Do"** status. Although a draft Confluence document was created on October 2, the overall task remains unstarted or awaiting finalization.
*   **Ownership & Pending Actions:**
    *   **Owner:** Michael Bui (Assignee).
    *   **Reporter:** John Henji Mantaring.
    *   **Pending Action:** The draft Confluence document requires review and approval. Following the update on October 3 regarding hierarchy sync options, the final documentation needs to be completed based on these inputs.
*   **Decisions Made:** On **October 3**, the reporter specified that for secondary categories, two distinct options were defined for **secondary category hierarchy sync**.
*   **Key Dates & Blockers:**
    *   **Ticket ID:** RM-644.
    *   **Priority:** High.
    *   **Timeline:**
        *   Created: October 1, 2025 (Title defined).
        *   Draft Submitted: October 2, 2025.
        *   Technical Update: October 3, 2025.
    *   **Deadlines/Blockers:** No due date is currently set on the ticket. There are no explicit blockers noted in the log; work appears to be pending review of the technical options for hierarchy sync.


## jira/RM-628: Video UX Testing
Source: jira | Key: RM-628 | Status: Cancelled (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done | Labels: priority:health, priority:improvement | parent: RM-446 | relates: RM-546
**Daily Briefing Summary: RM-628 Video UX Testing**

*   **Current Status:** The ticket is **Cancelled** with a resolution status of **Done**. No further work is required on this specific item by the current team.
*   **Pending Actions & Ownership:** Since the testing scope was identified as outside the RMN team's domain, the ownership has shifted to other stakeholders. Michael Bui (Reporter/Assignee) indicated that follow-up coordination is needed with unspecified teams ("check with [Name] and [Name]") to address the UX requirements. Specific owners for the handover were not named in the log.
*   **Decisions Made:** It was decided on **October 3, 2025**, to cancel this chore because the required "Video UX Testing" falls outside the RMN team's scope of responsibility. The work is effectively closed with a resolution of "Done."
*   **Key Dates & Blockers:**
    *   **Original Creation/Update:** September 17, 2025 (Title and metadata established).
    *   **Cancellation Date:** October 3, 2025.
    *   **Blocker/Scope Issue:** The primary driver for cancellation was the misalignment of scope; the task was deemed a UX-related activity rather than an RMN deliverable. There is no technical blocker, but rather a process/scope clarification.
*   **Ticket Metadata & References:**
    *   **Ticket ID:** RM-628 (Type: Chore, Priority: High).
    *   **Parent Epic:** RM-446 ("Video Ads").
    *   **Related Issue:** RM-546 (Linked as "Relates").
    *   **Person Involved:** Michael Bui.
    *   **Labels:** `priority:health`, `priority:improvement`.


## jira/PRDM-7: Allow staff to update images multiple times a day 
Source: jira | Key: PRDM-7 | Status: To Do (To Do) | Type: Story | Priority: Medium | Assignee: Michael Bui | Reporter: Michael Bui | Labels: priority:improvement | parent: PRDM-9
**Jira Ticket Brief: PRDM-7**

**Current Status**
*   **Status:** To Do (Deprioritized).
*   **Previous State:** The ticket was stuck in the QA and merge process.
*   **Resolution Decision:** As of 2024-12-11, the solution is deemed untested and too risky to release during the current change freeze. It has been deprioritized with plans to revisit a long-term solution in Q1 2025.

**Key Decisions Made**
*   **Deprioritization:** Sneha Parab decided on 2024-12-11 to pause this task immediately due to the change freeze and lack of testing.
*   **Future Planning:** The team agreed to defer implementation until Q1 2025.

**Pending Actions & Ownership**
*   **No Immediate Action Required:** With the ticket marked as deprioritized, there are no active development or QA tasks assigned for the current sprint.
*   **Re-evaluation Owner:** Michael Bui (Assignee) will likely re-engage upon the return to Q1 2025 planning cycles.

**Key Dates & Deadlines**
*   **Original Context:** Important for upcoming CNY campaigns (historical urgency noted by reporter).
*   **Last Update:** 2024-12-11T10:30:31.180+0800 (Deprioritization decision).
*   **Next Scheduled Review:** Q1 2025 (Long-term solution planning).

**Blockers & Context**
*   **Technical Limitation:** Current system only reflects image updates once daily, causing delays in fixing wrong images and preventing efficient flash campaign execution.
*   **Business Impact:** The limitation risks customer confusion regarding expired campaigns and reduced visibility for new promotions.
*   **Risk Factor:** Recent testing was insufficient to validate the solution against the risk of a change freeze release.

**Ticket Metadata Summary**
*   **Parent Ticket:** PRDM-9 ([Discover] Re-architecture of Image upload flow).
*   **Issue Type:** Story.
*   **Priority:** Medium (Label: `priority:improvement`).
*   **Assignee/Reporter:** Michael Bui.
*   **Comment History:** Moved back to "To Do" by Sneha Parab on 2024-11-25 due to merge process delays; deprioritized by Sneha Parab on 2024-12-11.


## jira/RM-612: RMN Architecture for ad delivery & tracking standardization
Source: jira | Key: RM-612 | Status: To Do (To Do) | Type: Ops | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui
**Daily Briefing Summary: RM-612**

*   **Current Status:** The ticket is in the **"To Do"** state. No work has commenced yet.
*   **Ownership & Pending Actions:**
    *   **Owner:** Michael Bui (Assignee and Reporter).
    *   **Pending Action:** Initiate work on defining the **RMN Architecture** to standardize ad delivery and tracking processes.
*   **Decisions Made:** None. The ticket was created with no prior discussion notes or resolution steps recorded in the chronological log.
*   **Key Dates, Deadlines, & Blockers:**
    *   **Priority:** High.
    *   **Due Date:** None assigned (null).
    *   **Blockers:** None identified currently.
    *   **Issue Type:** Ops.

**Technical Context:**
The scope involves establishing a standardized architecture for RMN regarding ad delivery mechanisms and tracking protocols. The ticket creation timestamp was noted as **2025-09-09T15:19:20.696+0800**. No components, labels, or fix versions are currently associated with the ticket.


## jira/RM-639: To discover the dependencies and estimate complexity
Source: jira | Key: RM-639 | Status: To Do (To Do) | Type: Ops | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | parent: RM-635
**Daily Briefing Summary: RM-639**

*   **Current Status:** The ticket is in the **"To Do"** state. No work has commenced, as indicated by a null resolution and no status changes since creation.
*   **Pending Actions & Ownership:**
    *   **Action:** Discover dependencies and estimate complexity for "Default and Generic Search Targeting."
    *   **Owner:** Michael Bui (Assignee and Reporter).
    *   **Context:** This task is a sub-issue of parent ticket **RM-635** ("Default and Generic Search Targeting").
*   **Decisions Made:** No decisions have been recorded in the chronological log. The entry serves as an initial creation or assignment to determine scope and effort.
*   **Key Dates & Blockers:**
    *   **Priority:** High.
    *   **Issue Type:** Ops.
    *   **Deadline:** None assigned (Duedate is null).
    *   **Blockers:** None explicitly identified in the log; however, the task remains unstarted pending execution by the assignee.
*   **Technical References:** Ticket ID **RM-639**, Parent Key **RM-635**.


## jira/BED-56: Create a standard repo template
Source: jira | Key: BED-56 | Status: Accepted (In Progress) | Type: Idea | Priority: High | Assignee: Michael Bui | Reporter: Zheng Ming New
**Jira Ticket Briefing: BED-56**

**Current Status/State**
*   **Ticket ID:** BED-56 (Idea)
*   **Status:** Accepted / In Progress
*   **Priority:** High
*   **Assignee:** Michael Bui
*   **Reporter:** Zheng Ming New
*   **Strategic Goal:** To reduce cognitive load when switching between repositories and improve consistency across all backend services by standardizing repo structures.

**Key Decisions & Updates**
*   A decision was made to proceed with creating a standard repository template for backend services (created 2025-03-28).
*   **Reference Document:** On 2025-09-29, Michael Bui updated the ticket with a link to the "Backend Chapter Standards" documentation: `https://ntuclink.atlassian.net/wiki/spaces/DPD/pages/2000584867/Backend+Chapter+Standards`.

**Pending Actions & Ownership**
*   **Owner:** Michael Bui
*   **Action:** Execute the creation of the standard repo template based on the established standards. The specific steps to finalize and deploy this template are currently underway (Status: In Progress).

**Key Dates, Deadlines, & Blockers**
*   **Last Update:** 2025-09-29T16:55:43+0800
*   **Original Creation/Update:** 2025-03-28T09:51:27+0800
*   **Due Date:** None set (null)
*   **Blockers:** No blockers identified in the current log.


## jira/RM-632: Pentest for Video Ads API
Source: jira | Key: RM-632 | Status: Cancelled (Done) | Type: Ops | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done
**Daily Briefing Summary: RM-632 (Pentest for Video Ads API)**

*   **Current Status:** The ticket is **Cancelled** with a final resolution of **Done**. It was reclassified under the "Ops" issue type.
*   **Decision Made:** The scheduled penetration test was deferred pending architectural changes. Per advice from **Winson**, testing should be postponed to align with the closure of **RMN development**. This ensures a comprehensive pentest covers all **RMN APIs** simultaneously rather than isolating the Video Ads API.
*   **Pending Actions:** None currently assigned to this specific ticket as it is marked Done. The strategic action now rests on waiting for **RMN development** to reach closure before initiating the unified security assessment.
*   **Ownership:**
    *   **Reporter & Assignee:** Michael Bui
    *   **Advisory Input:** Winson (regarding deferral strategy)
*   **Key Dates & Blockers:**
    *   **Cancellation Date:** 2025-09-29 (11:44 AM).
    *   **Original Priority:** High.
    *   **Blocker/Dependency:** Completion of RMN development closure. No specific new deadline has been set for the rescheduled pentest; the original due date remains null.

**Summary:** The high-priority security assessment for the Video Ads API (RM-632) initiated by Michael Bui was cancelled on September 29, 2025. The decision to delay was made to optimize scope by bundling this effort with a broader pentest for all RMN APIs once development is finalized.


## jira/RM-337: SSL-enabled fairprice-sg.onlinesales.ai
Source: jira | Key: RM-337 | Status: Cancelled (Done) | Type: Subtask | Priority: High | Assignee: Michael Bui | Reporter: Fadilah Iskander | Due: 2025-04-08 | Resolution: Done | Labels: priority:strategic | child: RM-336 | parent: RM-336
**Daily Briefing Summary: RM-337**

**Ticket Status & Decision**
*   **Status:** Cancelled (Resolution: Done)
*   **Decision:** The SSL configuration task for `fairprice-sg.onlinesales.ai` within the OSMOS whitelabelling initiative has been formally cancelled and closed. No further action is required on this specific subtask.

**Key Details**
*   **Parent Initiative:** RM-336 - [OSMOS] Whitelabelling Domain
*   **Priority:** High (Label: `priority:strategic`)
*   **Assignee:** Michael Bui
*   **Reporter:** Fadilah Iskander
*   **Original Deadline:** 2025-04-08

**Technical Context & Scope**
The original scope involved enabling SSL for the proposed production domains:
1.  `pulse.ads.fairpricegroup.com.sg`
2.  `ad-ops.fairpricegroup.com.sg`
3.  `ads.fairpricegroup.com.sg`

**Action Items & Ownership**
*   **Pending Actions:** None. The ticket is marked "Done" with a status of "Cancelled."
*   **Owner Responsibility:** Michael Bui's assignment on this subtask is complete per the cancellation resolution recorded by reporter Fadilah Iskander.

**Timeline & Blockers**
*   **Last Activity:** 2025-04-07 (Cancellation and closure).
*   **Blockers:** None identified in the metadata; the task was terminated before the deadline.


## jira/RM-336: [OSMOS] Whitelabelling Domain
Source: jira | Key: RM-336 | Status: To Do (To Do) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Fadilah Iskander | Labels: priority:roadmap | child: RM-337, RM-338, RM-339, RM-340 | parent: RM-593, RM-337
**Executive Briefing Summary: RM-336 [OSMOS] Whitelabelling Domain**

**Current Status**
*   **Ticket State:** To Do (Currently Paused).
*   **Parent Epic:** RM-593 (Whitelabel OSMOS platform to FPG RMN brand identity).
*   **Priority:** High.
*   **Assignee:** Michael Bui.
*   **Reporter:** Fadilah Iskander.

**Pending Actions & Ownership**
1.  **Business Decision Required:** A decision on the rollout strategy for new hostnames is needed to unblock progress.
    *   *Owner:* Business Stakeholders / Leadership (implied by "business decision").
2.  **Asset Collection (Fairprice Group):**
    *   **Logo:** High-resolution variations (.svg, .png, or .jpg) with max dimensions 60px height x 250px width. Must include light and dark background versions.
    *   **Brand Color:** Primary brand hex code (e.g., #636cff).
    *   **Sender Email:** A verified email address for platform communications (recipient must click verification link).
    *   *Owner:* Fadilah Iskander / Fairprice Group Representatives.
3.  **Technical Configuration (Michael Bui):**
    *   Provide exact OSMOS hostname for the CNAME record mapping.
    *   Obtain and process SSL certificates (`.key`, `.crt`, `.pem`) for the target domain (`ads.fairpricegroup.com.sg` or equivalent).
    *   *Note:* Domain mapping requires DNS CNAME to `<publisherdomain>.onlinesales.ai` with 60-minute TTL.

**Decisions Made & Technical Requirements**
*   **Domain Strategy:** The white-labeled Advertiser Platform must be accessed via a custom domain (e.g., `ads.fairpricegroup.com.sg`) that is SSL-enabled.
*   **CNAME Requirement:** The publisher must map their custom domain to the OSMOS hostname provided by Michael Bui.
*   **SSL Requirements:** Three specific files per certificate (`*.key`, `*.crt`, `*.pem`) are required for secure connections.

**Key Dates, Deadlines & Blockers**
*   **Last Update:** 2025-08-18 (Michael Bui noted the ticket is paused).
*   **Estimated Processing Time:** 1–2 weeks once assets and decisions are confirmed (per 2025-04-07 comment by Michael Bui).
*   **Subtasks Linked:** RM-337, RM-338, RM-339, RM-340.
*   **Primary Blocker:** Waiting for a business decision regarding the rollout of new hostnames. No further technical work can proceed until this strategic direction is confirmed.


## jira/RM-589: OSMOS product being advertised when set-up is not done
Source: jira | Key: RM-589 | Status: To Do (To Do) | Type: Ops | Priority: High | Assignee: Michael Bui | Reporter: Pamela Koh
**Daily Briefing Summary: Ticket RM-589**

*   **Current Status:** The ticket is currently in **"To Do"** status with a **"High"** priority classification. It is categorized as an "Ops" issue type and remains unresolved.
*   **Pending Actions & Ownership:**
    *   **Action Required:** Investigate the root cause of why the OSMOS product (specifically `cp-hot-wings-1kg`, URL: `https://www.fairprice.com.sg/product/cp-hot-wings-1kg-13149007`) is actively being advertised despite the ad ops team not completing the necessary setup.
    *   **Owner:** **Michael Bui** (Assignee) is responsible for executing this investigation.
*   **Decisions Made:** No decisions have been recorded yet as the ticket has not progressed beyond the "To Do" stage. The reporter, **Pamela Koh**, has raised the issue requesting a technical check but no resolution strategy has been formally approved or initiated.
*   **Key Dates & Blockers:**
    *   **Reported Date:** September 4, 2025 (14:33 SGT).
    *   **Deadline:** None assigned (`null`).
    *   **Blockers:** No specific blockers are currently listed; however, the discrepancy between advertised status and setup completion is an active operational issue requiring immediate attention due to its high priority.


## jira/PRDM-31: Configurable Product Discrepancy flow in DBP
Source: jira | Key: PRDM-31 | Status: To Do (To Do) | Type: Chore | Priority: Medium | Assignee: Michael Bui | Reporter: Ram Datchnamoorthy | Labels: Postmortem-LongTerm, priority:health
**Daily Briefing Summary: PRDM-31**

**Current Status & State**
*   **Ticket ID:** PRDM-31
*   **Issue Type:** Chore (Configurable Product Discrepancy flow in DBP)
*   **Status:** To Do (No work initiated yet).
*   **Priority:** Medium.
*   **Labels:** Postmortem-LongTerm, priority:health.

**Ownership & Pending Actions**
*   **Assignee:** Michael Bui is responsible for execution.
*   **Reporter:** Ram Datchnamoorthy.
*   **Pending Deliverables:**
    1.  Implement a configurable discrepancy threshold in the DBP Portal (Default: 10%).
    2.  Develop an approval workflow to replace the current total block; if discrepancies exceed the threshold, execution pauses for manual override rather than failing entirely.
    3.  Integrate Datadog alerting to notify stakeholders when discrepancies approach the defined threshold.
    4.  Establish an audit log mechanism to track all approval or denial actions regarding index switches.

**Decisions Made**
*   **Strategy Shift:** The team decided against blocking the entire index switch upon detecting discrepancies. Instead, the flow will now allow for controlled execution based on a configurable percentage threshold.
*   **Oversight Model:** Business oversight is maintained via an approval workflow requiring authorized users to explicitly proceed, pause, or investigate before changes are applied.

**Key Dates, Deadlines & Blockers**
*   **Deadlines:** No due date has been assigned (null).
*   **Dependencies:** Implementation requires coordination with the DBP Portal team for the approval workflow and the Search Indexer team for configurable discrepancy handling logic.
*   **Blockers:** None currently identified; ticket is in "To Do" status awaiting assignment to development.


## jira/RM-341: [BE] New Product Handling in Product Feed
Source: jira | Key: RM-341 | Status: To Do (To Do) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Fadilah Iskander | parent: RM-250
**Daily Briefing Summary: RM-341**

**Current Status**
*   **Ticket:** RM-341 ([BE] New Product Handling in Product Feed)
*   **State:** To Do (Story type, High Priority).
*   **Parent Epic:** RM-250 (Platform health).
*   **Reporter:** Fadilah Iskander.

**Pending Actions & Ownership**
*   **Action:** Implement backend logic to include vendor code and product data within the Product Feed.
*   **Owner:** Michael Bui (Assignee).
*   **Deadline:** None currently assigned (Due Date: null).

**Decisions Made**
*   No technical or business decisions are recorded in the current ticket content. The scope is defined strictly by the requirement to integrate vendor codes and product data.

**Key Dates & Blockers**
*   **Last Activity:** 2025-04-08T20:17:23.129+0800 (Initial creation/ticket update).
*   **Blockers:** None identified in the current log.
*   **Dependencies:** Linked to parent ticket RM-250; no specific version fixes or components are assigned yet.

**Technical Context**
*   **Component Focus:** Backend (BE) development regarding Product Feed enhancements.
*   **Specific Data Points:** Vendor code and product data inclusion.


## jira/PRDM-130: SLO migration as per new team names
Source: jira | Key: PRDM-130 | Status: Cancelled (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Sneha Parab | Resolution: Done
**Jira Ticket Briefing: PRDM-130**

**Current Status**
*   **State:** Cancelled (Marked as Done).
*   **Ticket ID:** PRDM-130.
*   **Type/Priority:** Chore / High.

**Key Decisions & Actions Taken**
*   **SLO Migration Scope:** The ticket was created to migrate specific SLOs from the *Grocery-Discovery* service to align with new team tagging conventions, specifically targeting the "Engage Tribe."
*   **Targeted SLOs for Migration:**
    1.  Marketplace Category Management Journey
    2.  Marketplace Product Management Journey
    3.  Marketplace Brand Management Journey
    4.  Food product listing journey
    5.  Browse banner page journey
*   **Additional Requirement:** The task included verifying if other SLOs intended for the Engage Tribe lacked Pull Requests (PRs); missing PRs were to be raised and approved by the team.

**Pending Actions & Ownership**
*   **Execution Status:** No specific technical work (migration or PR creation) appears completed in the timeline, as the ticket was subsequently cancelled based on priority shifts.
*   **Dependency Note:** Reporter Sneha Parab added a critical instruction on 2025-04-28 regarding a "Follow up thread with RE team." Assignee Michael Bui is instructed to take note of this context before proceeding if work resumes.

**Key Dates & Timeline**
*   **2025-04-08:** Ticket created by Sneha Parab; SLO list defined.
*   **2025-04-22:** Sneha Parab noted execution is deferred pending priority assessment ("Will be done after based on priority").
*   **2025-04-28:** Final update linking the ticket to an ongoing thread with the RE team; status updated to Cancelled/Done.

**Blockers & Constraints**
*   **Priority Deferral:** Work was halted pending further prioritization decisions.
*   **Timeline:** No fixed due date was set.
*   **Communication Gap:** The cancellation suggests a shift in strategy or priority, requiring alignment with the RE team (per the 04-28 note) before any potential reactivation.

**Assignee/Reporter**
*   **Assignee:** Michael Bui
*   **Reporter:** Sneha Parab


## jira/PRDM-162: Disable DY swimlanes 15 mins to assess impact on homepage SLO
Source: jira | Key: PRDM-162 | Status: Cancelled (Done) | Type: Chore | Priority: Medium | Assignee: Michael Bui | Reporter: Sneha Parab | Resolution: Done
**Jira Ticket Brief: PRDM-162**

**Current Status:** Cancelled (Resolved as Done). The task to disable DY swimlanes has been closed. No further action is required on this specific ticket.

**Key Decisions & Outcomes:**
*   **Objective Assessment:** Sneha Parab requested a 15-minute test to assess the impact of "DY" latency on homepage SLO by disabling specific feature flags.
*   **Scope Confirmation:** Michael Bui confirmed testing 7 active DY feature flags (fe_gt_rec_bs, fe_gt_rec_wfp, fe_gt_rec_r4u, and others) while leaving 4 other flags (fe_gt_rec_ws, fe_gt_rec_tag, etc.) untouched as they have no impact.
*   **Timing Plan:** Michael Bui proposed conducting the test on **April 15th at approximately 2:00 PM – 3:00 PM**, citing lower post-lunch traffic and immediate developer availability to handle issues.

**Pending Actions & Owners:**
*   **None.** The ticket is marked as "Cancelled/Done," indicating the planned execution did not proceed or was superseded. The specific test window proposed for April 15th at 2–3 PM was never finalized in comments, and no date/time was confirmed by the reporter (Sneha Parab) prior to closure.

**Key Dates & References:**
*   **Ticket ID:** PRDM-162
*   **Reporter:** Sneha Parab
*   **Assignee:** Michael Bui
*   **Original Proposal Date:** April 14, 2025 (17:36)
*   **Clarification/Query:** April 14, 2025 (18:18 – Erica Lee asked for timing; Sneha clarified scope on 18:44).
*   **Proposed Execution Date:** April 15, 2025 (Estimated 2–3 PM).

**Technical Details:**
*   **Feature Flags to Disable:** `fe_gt_rec_bs` (Best Seller), `fe_gt_rec_wfp` (Fresh Picks), `fe_gt_rec_r4u` (Recommended for You).
*   **Feature Flags Excluded:** `fe_gt_rec_ws`, `fe_gt_rec_tag`, `fe_gt_rec_fbt`, `fe_gt_rec_category`, `fe_gt_rec_ne`, `fe_gt_rec_wtyl`, `fe_gt_rec_whn`, `fe_gt_rec_pdbn`.

**Blockers/Note:**
The ticket status is "Cancelled" despite being marked "Done." There is no record of the actual execution or SLO impact data in this thread. The planned window on April 15 was only proposed by Michael Bui and requires confirmation to proceed if the test is re-initiated.
