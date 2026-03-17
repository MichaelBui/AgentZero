

## jira/OMNI-1163: Enable AI Personalisation Search Capability with Algolia
Source: jira | Key: OMNI-1163 | Status: Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Erica Lee | Reporter: Erica Lee | migration_parent: OMNI-653 | polaris-work-item-link: PRDM-12 | relates: PRDM-12, OMNI-1312
**Status Update: OMNI-1163 (Enable AI Personalisation Search Capability with Algolia)**

**Current State**
The initiative remains in the **Ideas** backlog but is marked as **Prioritised** (**High Priority**, Status: **To Do**), assigned to **Erica Lee**. While technically feasible and linked to migration parent **OMNI-653**, immediate implementation hinges on resolving specific technical constraints regarding event completeness. The project faces a critical dependency on confirming whether current "past purchase boosting" logic will be overridden by Algolia's AI if enabled "as-is," which could inadvertently hide previously purchased items.

**Problem & Opportunity**
Customers currently face generic search results that fail to reflect individual preferences, leading to inefficient discovery. Enabling AI personalization aims to dynamically adjust search and category listings based on browsing behavior and purchase history.
*   **Projected Impact:** A conservative 2% increase in Search Conversion Rate (CVR) is expected, driving a **$1.6M uplift** in Search GMV against a 2024 baseline of $81.7M. This also targets an increase in Overall Average Order Value (AOV).
*   **Validation:** Based on Algolia client data showing 4.5% CTR/CVR gains, FairPrice anticipates measurable improvements in search relevance and conversion.

**Key Decisions & Strategic Context**
1.  **Scope Management:** While this ticket focuses on Algolia AI, Google Search functionality was split into a separate ticket (**OMNI-1312**) to allow immediate A/B testing of that alternative, which showed strong preliminary results (resolving 21.6% zero-result queries).
2.  **Strategic Continuity:** Despite recent backlog movements, leadership affirmed on **2025-09-22** and again on **2026-01-19** that this is not wasted effort. It requires re-evaluation for low-risk activation once technical blockers are cleared.

**Pending Actions & Ownership**
*   **Re-validate with Algolia (Owner: Vivian Lim Yu Qian):** A meeting was scheduled for **Tuesday, 2026-03-18** to confirm specific event requirements from Algolia engineers.
    *   *Critical Technical Question:* Determine if the effort to modify past purchase data flows is "deadly critical" or if AI logic will override existing boosting without significant engineering intervention.
*   **Event Confirmation:** Verify that all required personalization events are live via CDP/Segment (work completed by Deloitte in Sprints 7 and 9).

**Key Dates & Dependencies**
*   **2026-03-18:** Re-validation meeting with Algolia.
*   **Dependencies:** The ticket cannot proceed until the search provider strategy is finalized post-POC and event completeness is confirmed.
*   **Blockers:** Uncertainty regarding the engineering effort to prevent AI logic from overriding past purchase data; confirmation that no additional tagging work is needed beyond Deloitte's delivery.

**Technical References**
*   **Provider:** Algolia (via CDP/Segment).
*   **Related Issues:** PRDM-12, OMNI-653 (migration_parent), OMNI-1312.


## jira/DPD-715: Dynamic ad slot configuration for Homepage swimlanes
Source: jira | Key: DPD-715 | Status: TESTING IN PREPRODUCTION (In Progress) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-17 | parent: DPD-710
**Ticket Summary: DPD-715 (Dynamic ad slot configuration for Homepage swimlanes)**
*Parent:* DPD-710 ([RMN] Activate product ads in Omni Home swimlanes)
*Assignee:* Michael Bui | *Reporter:* Nikhil Grover
*Priority:* High | *Status:* TESTING IN PREPRODUCTION (In Progress) | *Due Date:* 2026-03-17

**Current Status**
The story is in **TESTING IN PREPRODUCTION**. The feature allows dynamic control of ad placement and count via Split feature flags, enabling layout optimization for both Omni and OG Homepages without code changes or manual API updates. As of **2026-03-16T18:07:30**, mobile application issues have been resolved, and the ticket is officially ready for UAT.

**Pending Actions & Ownership**
*   **UAT Initiation:** Michael Bui has confirmed readiness for UAT; stakeholders should proceed with acceptance testing immediately.
*   **Omni Home Configuration Discrepancy:** As of **2026-03-16T16:54:01**, SplitIO changes (2, 5) successfully reflected in **OG Home** swimlanes but remain fixed at **(1, 3)** in **Omni Home** swimlanes. Michael Bui is investigating this discrepancy and coordinating with relevant team members to align Omni configurations before final deployment.

**Decisions Made & Acceptance Criteria**
*   **Dynamic API Requests:** When the flag is ON with configuration `[3, 5, 7]`, the system requests 3 ads rendering at positions 3, 5, and 7. Updating the Split config to `[2, 4, 6, 8, 10]` automatically triggers a request for 5 ads in new user sessions without deployment.
*   **Fallback Logic:** If the flag is OFF, the system defaults to slots `[1, 3]`, fetching 2 ads.
*   **Empty Configuration:** An empty Split array `[]` results in 0 ad requests; the page displays only organic products with no gaps.
*   **Supply Shortage Handling:** If configuration calls for 3 slots (e.g., `[3, 5, 7]`) but only 2 valid ads are returned, slots 3 and 5 fill with ads, while slot 7 renders organic content.
*   **Out-of-Bounds Handling:** Slot indices exceeding the available content range (e.g., index 20 in a 10-item swimlane) are ignored; only valid indices render.
*   **Stock Integrity:** The system strictly honors existing stock availability checks before requesting ads to prevent displaying out-of-stock items.

**Key Dates & Blockers**
*   **2026-03-10T12:29:37:** Ticket created and requirements defined by Nikhil Grover.
*   **2026-03-16T16:54:01:** Partial deployment observed (OG Home updated to 2,5; Omni Home lagging at 1,3).
*   **2026-03-16T18:07:30:** Mobile app issues resolved; status shifted to ready for UAT.
*   **2026-03-17:** Hard deadline for completion.
*   **Blocker/Constraint:** Omni Home swimlanes are not reflecting the latest Split configuration changes (fixed at 1,3), preventing full deployment success until resolved.


## jira/DPD-645: Improve event sync to prevent overage
Source: jira | Key: DPD-645 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-12 | Resolution: Done | blocks: DPD-273, DPD-273 | parent: DPD-644
**Ticket:** DPD-645: Improve event sync to prevent overage
**Status:** IN RELEASE QUEUE (Done) | **Priority:** High | **Resolution:** Done
**Assignee:** Michael Bui | **Reporter:** Nikhil Grover
**Parent:** DPD-644 ([RMN] Streamline event sync from Segment.io to OSMOS to resolve overage)
**Linked Issues:** Blocks DPD-273

### 1. Current Status/State
*   **Deployment Outcome:** The optimization change was deployed to PROD temporarily on **2026-03-15** between 8:00 PM and 11:00 PM local time.
*   **Immediate Result:** While no issues were detected after ~30 minutes, the deployment was reverted to version #56 at **23:02 on 2026-03-15**.
*   **Target Metric:** The acceptance criteria required a **50% reduction** in function execution time for transaction and product events. Michael Bui noted this is a tentative target due to variable computing durations, with the primary aim being minimizing function usage.

### 2. Pending Actions & Ownership
*   **Investigation Required:** Root cause analysis is needed regarding why the temporary deployment was reverted despite initial stability.
    *   **Owner:** Michael Bui (implied based on recent activity).
*   **Data Verification Plan:** If a new deployment window is scheduled, the following steps must be executed:
    *   Enable change in PROD for 3 hours on Sunday (tentative time 8 PM–11 PM).
    *   Verify data consistency between OSMOS and BigQuery against last 1-2 weeks of baseline data to ensure error rates are within threshold.
    *   If successful, enable permanently and observe closely for 1–2 days.
*   **Automation Gap:** A specific limitation was noted regarding E2E testing coverage; since the scenario involves UI interactions, it cannot be automated.
    *   **Owner:** Madhuri Nalamothu (confirmed in comment on 2026-03-16).

### 3. Key Decisions Made
*   **Reversion Decision:** The temporary PROD change enabled on March 15 was rolled back to version #56 by late evening that same day.
*   **Release Strategy:** A phased approach was agreed upon: UAT observation (2 weeks post-change) followed by a short-term PROD trial, then permanent enablement if stable.

### 4. Key Dates & Blockers
*   **Critical Dates:**
    *   **UAT Observation Period:** Started ~05/03/2026; observed for 2 weeks prior to the PROD attempt.
    *   **PROD Trial Window:** 15/03/2026 (8:00 PM – 11:00 PM).
    *   **Original Due Date:** 12/03/2026 (Ticket marked "Done" post-deadline due to deployment status).
*   **Blockers:** The temporary production failure/reversion prevents the immediate elimination of recurring monthly cost overages. No specific technical blocker was cited for the revert, only the action itself.

### 5. Technical References
*   **System Components:** Segment.io -> OSMOS PROD destination function -> BigQuery.
*   **Versions:** Reverted to version #56.
*   **Platforms Monitored:** IOS UAT, Android UAT (Statuses listed as open/blank in comments).
*   **Context:** Ticket created 2026-03-03; Automation limitation confirmed 2026-03-16.


## jira/OPCO-1940: FP VIPs encounter verification after S&G purchase for fewer reasons, vs other customers
Source: jira | Key: OPCO-1940 | Status: In release queue (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Ravi Goel | Resolution: Done | Labels: priority:improvement | blocks: OPCO-1956
**Jira Ticket Summary: OPCO-1940**

**Current Status**
The ticket is marked **"In release queue"** with a status of "Done" technically, but the feature remains **unreleased and on hold**. While UAT was concluded by David Anura Cooray on 2026-02-02, implementation has been paused pending business re-alignment.

**Key Decisions & Technical Context**
*   **Feature Logic:** VIP users (identified via CS Backoffice tags, not the initial Split sheet approach) now bypass S&G verification for generic risk rules, retaining verification only for: Age-restricted items, Force-verification SKUs, and High-priced items (>HighRiskPrice threshold).
*   **Non-VIP Safety:** Confirmed that non-VIP behavior remains unchanged. Vivian Lim Yu Qian verified no regression testing was performed; instead, UAT compared specific VIP (ID: 6873106) vs. Non-VIP (ID: 6835530) accounts to ensure stability.
*   **Monitoring Strategy:** Post-deployment monitoring will track "Total verification success/fail" ratios and the "Verification fail rate per total sessions" (baseline ~8-9%) via Datadog logs to detect anomalies, noting potential CNY seasonality fluctuations.
*   **Architecture Change:** Following feedback from Winson, VIP identification logic was updated to rely on customer account tags in Backoffice rather than a static Split flag referencing an Excel sheet.

**Pending Actions & Ownership**
*   **Business Re-alignment:** Vivian Lim Yu Qian (3/16) requested further business alignment before the feature can go live. This is currently the primary blocker.
*   **UAT Sign-off:** Michael Bui (3/15-3/16) confirmed UAT sign-off is pending finalization alongside the business alignment.
*   **Deployment:** Michael Bui will deploy and release the feature once UAT is signed off and business alignment is complete.

**Key Dates & Blockers**
*   **2026-02-02:** UAT concluded; Vivian gave approval to proceed to release pending monitoring setup.
*   **2026-03-15/16:** Michael Bui followed up on testing status. Vivian confirmed the feature is **not yet released** and placed the ticket on hold due to required business re-alignment.
*   **Blocker:** Pending business-side re-alignment regarding VIP identification logic implementation.

**Related Issues**
*   Blocks: **OPCO-1956**
*   Reporter: Ravi Goel | Assignee: Michael Bui


## jira/DPD-644: [RMN] Streamline event sync from Segment.io to OSMOS to resolve overage
Source: jira | Key: DPD-644 | Status: TO BE DEFINED (To Do) | Type: Epic | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-12 | parent: DPD-645 | polaris-work-item-link: OMNI-1418, OMNI-1418
### Daily Briefing Summary: DPD-644

**Current Status**
*   **Ticket:** DPD-644 ([RMN] Streamline event sync from Segment.io to OSMOS to resolve overage)
*   **Type:** Epic (High Priority)
*   **State:** `TO BE DEFINED` / `To Do`. The work has not commenced.
*   **Owner:** Michael Bui (Assignee).

**Pending Actions & Ownership**
*   **Action Required:** Define the scope, strategy, and execution plan for streamlining the event synchronization process between Segment.io and OSMOS to eliminate cost overages.
*   **Responsibility:** Michael Bui is responsible for initiating this definition phase.
*   **External Dependency:** The task is linked to Polaris work item **OMNI-1418**, which may require coordination or alignment prior to execution.

**Decisions Made**
*   No technical or strategic decisions have been recorded yet, as the status remains `TO BE DEFINED`. The primary objective identified is resolving "overage" issues through process streamlining.

**Key Dates & Blockers**
*   **Due Date:** March 12, 2026.
*   **Latest Activity:** Ticket creation/review noted on March 3, 2026, at 14:07 UTC+8 by Nikhil Grover (Reporter).
*   **Blockers:** None explicitly listed in the current log; however, the `TO BE DEFINED` status indicates a lack of immediate technical direction or resource allocation plan.

**Technical Context**
*   **Source System:** Segment.io
*   **Target System:** OSMOS
*   **Objective:** Optimize data flow to resolve financial overages associated with current sync volumes.


## jira/DPD-700: Fix RMN pentest Low and optionally Info issues
Source: jira | Key: DPD-700 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Due: 2026-03-20 | Resolution: Done | Labels: priority:improvement | relates: DPD-591, DPD-591
**Jira Ticket:** DPD-700 | **Resource:** RMN Pentest Remediation (Low/Info)
**Status:** Done | **Assignee:** Michael Bui | **Priority:** High | **Related:** DPD-591

### Current Status
The ticket is marked as **Done**. Security hardening for the Marketing Personalization Service (`marketing-personalization-service`) has been successfully deployed to both Preprod and Production environments (FairPrice domains) on **March 9, 2026**, following a Terraform apply.

### Actions Completed / Resolved
The following Low and Informational severity findings have been implemented:
*   **Rate Limiting:** GCP Cloud Armor configured with a limit of **200 requests per second (rps) per IP** (12,000 req/60s), returning HTTP 429 on exceed.
*   **HSTS:** `Strict-Transport-Security: max-age=31536000` enforced globally via GCP Load Balancer.
*   **Security Headers Added:**
    *   `Cache-Control: no-store` (Prevents caching of sensitive responses).
    *   `Content-Security-Policy: default-src 'none'; frame-ancestors 'none'`.
    *   `X-Content-Type-Options: nosniff`.
    *   `X-Frame-Options: DENY`.
    *   `Referrer-Policy: strict-origin-when-cross-origin`.
*   **TLS Fixes:** Previously resolved Lucky Thirteen and Static Key Cipher vulnerabilities via the "RESTRICTED" GCP SSL Policy.

### Pending Actions & Ownership
*   **Unreferenced Page Discovery (Low):** Status is **Accepted**. The team identified endpoints as a Health Check; no further action required currently.
*   **CORS Wildcard Origin (Info):** Status is **Accepted** but flagged for future remediation. The current `access-control-allow-origin: *` setting persists because it must be configured at the application level (Cloud Run code), not via Cloud Armor or Load Balancer configuration. Ownership remains with the application development team to enforce a strict whitelist of trusted FairPrice domains.

### Decisions Made
*   **TLS Policy:** Confirmed adoption of "RESTRICTED" GCP SSL Policy (CBC ciphers disabled, only forward-secret ciphers allowed) as sufficient for mitigating timing side-channel attacks and static key issues.
*   **CORS Strategy:** Accepted that the CORS wildcard cannot be removed immediately via infrastructure changes; an application code change is required. This was marked as "Accepted" rather than "Open."

### Key Dates & Blockers
*   **Deployment Date:** March 9, 2026 (14:25 SGT).
*   **Original Due Date:** March 20, 2026 (Ticket completed ahead of schedule).
*   **Blockers:** None. All infrastructure-level fixes are live in both environments.


## jira/DPD-551: Capture SAP Material Number into catalogue service for SAP-related downstream usage
Source: jira | Key: DPD-551 | Status: Done (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done | blocks: DPD-383, DPD-383
**Jira Ticket Briefing: DPD-551**

**Current Status:**
*   **Status:** Done (Resolved).
*   **Action:** The SAP Material Number is now successfully captured and stored in the DPP/DBP platform product metadata field.
*   **Verification:** Verified in UAT post-UD; Production deployment completed on 2026-03-09 with successful verification for both RB and MP SKUs.

**Ownership & Actions Pending:**
*   **No pending actions.** The ticket is fully closed.
*   **Primary Owner:** Michael Bui (Assignee, Reporter, Deployer).
*   **Support:** Sneha Parab confirmed the creation of the `SAPMaterialNumber` field in Production on 2026-03-09.

**Key Decisions & Technical Implementation:**
*   **Objective:** Capture SAP material numbers to resolve identification mismatches between SAP and DPP, enabling downstream integration logic.
*   **Implementation:** Added a specific product metadata field (`SAPMaterialNumber`) to store the data during UD (Update/Ingestion) processes.
*   **Scope:** Applies to both RB (Retail/B2C) and MP (Marketplace) SKUs.

**Key Dates & Dependencies:**
*   **2026-02-16:** Ticket created/highlighted as a High Priority Story.
*   **2026-02-19:** UAT verification completed; `SAPMaterialNumber` capture confirmed post-UD.
*   **2026-03-09 (11:09):** Production field `SAPMaterialNumber` created by Sneha Parab.
*   **2026-03-09 (14:59):** Deployment to PRD completed and verified by Michael Bui for BCRS SKU.

**Blockers/Dependencies:**
*   **Blocks Issue:** DPD-383 (This story unblocks downstream usage in DPD-383).


## jira/DPD-631: Setup alerts for Advertima platform
Source: jira | Key: DPD-631 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done
**Daily Briefing Summary: DPD-631 (Setup alerts for Advertima platform)**

*   **Current Status:** The ticket is **Done**. All implementation work has been completed.
*   **Owner & Assignment:** Assigned to and executed by **Michael Bui** (who also reported the issue). No further ownership or pending actions exist for this specific task.
*   **Key Decisions & Actions Taken:**
    *   Established an email group specifically designed to receive RMN alerts for the Advertima platform.
    *   Successfully configured and activated the alert system. Confirmation of setup was logged on **2026-03-09**.
    *   Reviewed update from Advertima dated **2026-02-20** as part of the prerequisite context.
*   **Key Dates & Timeline:**
    *   **Ticket Creation/High Priority Start:** 2026-02-27 (18:42 UTC+8).
    *   **Advertima Update Received:** 2026-02-20.
    *   **Email Group Creation:** 2026-02-27.
    *   **Final Setup Confirmation:** 2026-03-09 (12:05 UTC+8).
*   **Blockers & Deadlines:** No blockers identified; the ticket had no specific due date, and it was resolved within a two-week window from creation to completion.

**Summary:** The high-priority chore task **DPD-631** has been fully closed. **Michael Bui** successfully set up alerts for the Advertima platform, including the creation of a dedicated email group for RMN notifications, with final verification on March 9th.


## jira/DPD-591: Fix RMN pentest medium issues
Source: jira | Key: DPD-591 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Due: 2026-03-20 | Resolution: Done | Labels: priority:improvement | relates: RM-669, DPD-700, DPD-700
**Jira Ticket Summary: DPD-591**

**Status & Ownership**
*   **Current State:** Done (Completed).
*   **Assignee/Reporter:** Michael Bui.
*   **Ticket Type:** Chore (Priority: High).
*   **Resolution Date:** March 5, 2026.
*   **Linked Issues:** Relates to RM-669 and DPD-700.

**Action Taken**
Michael Bui resolved high-priority medium-severity security vulnerabilities identified during the RMN penetration test on the `marketing-personalization-service`. Actions included:
1.  **Policy Update:** Added a RESTRICTED policy on March 5, 2026, to mitigate specific TLS/SSL vulnerabilities, including SWEET32, BEAST, "Lucky Thirteen," and weak cipher suites (DES, IDEA, Static Key Ciphers).
2.  **Protocol Hardening:** Disabled deprecated protocols (TLS 1.0, TLS 1.1) and enforced Forward Secrecy.

**Verification & Results**
*   **Deployment Date:** March 5, 2026.
*   **Environment:** Production (`PRD`).
*   **Service:** `marketing-personalization-service.fairprice.com.sg`.
*   **Validation Method:** Executed Nmap scan (`nmap -sT --script ssl-enum-ciphers -p 443`).
*   **Outcome:** Confirmed by LGMS. The server now supports only TLSv1.2 with 128-bit x25519 encryption and a 2048-bit RSA key (SHA256WithRSAEncryption). All legacy ciphers and deprecated protocols were successfully removed.

**Key Dates & Deadlines**
*   **Action Completed:** March 5, 2026.
*   **Original Due Date:** March 20, 2026 (Completed ahead of schedule).
*   **Certificate Validity:** Feb 17, 2026 – May 18, 2026.

**Pending Actions & Decisions**
*   **No pending actions.** The ticket is fully resolved and verified.
*   **Decisions Made:** Deprecated legacy cryptographic standards (DES, IDEA, TLS 1.0/1.1) were permanently disabled in favor of modern, secure configurations.


## jira/DPD-383: Sales posting for BCRS deposit amount
Source: jira | Key: DPD-383 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Prajney Sribhashyam | Due: 2026-02-18 | Resolution: Done | blocks: DPD-551, DPD-551 | child: DPD-590 | parent: DPD-225, DPD-590
**Ticket Summary: DPD-383 – Sales Posting for BCRS Deposit Amount**

**Current Status:** IN RELEASE QUEUE (Resolved/Done)
**Assignee:** Michael Bui
**Reporter:** Prajney Sribhashyam
**Priority:** High
**Parent:** DPD-225 ([BCRS] Inform customers on BCRS deposit...)
**Due Date:** 2026-02-18 (Note: Ticket resolved after this date)

**Key Achievements & Decisions**
*   **Development Complete:** Implementation of SAP Deposit Posting service successfully calculates and posts BCRS deposits collected at the order line level. Logic covers E-Comm, Marketplace, Returns/Refunds, Donation orders, and FOC (Free of Charge) items.
*   **Dependency Resolution:** Previously blocked by **DPD-551** (PLU Processor). Michael Bui updated the `order-v3` gRPC API on 2026-02-20 to return `sapMaterialNumber`, unblocking this ticket.
*   **SAP Integration Confirmed:** First successful posting confirmed on 2026-02-23 (Doc Type: DR, Ref Doc No: 75471306). SAP successfully recorded the deposit (e.g., Account GL 4423, Customer 199997).
*   **Critical Fixes Implemented:**
    *   **CSRF Handling:** Updated logic to handle SAP CSRF tokens and cookies to resolve HTTP 403 errors. Added specific failure detection logic beyond standard HTTP codes.
    *   **Duplicate Posting Prevention:** Identified that GCP PubSub default behavior caused duplicate postings. Enabled "delivery once" policy on 2026-03-06 to ensure idempotency.
    *   **FOC Logic Update:** Discovered `freeItems` field in order data (not in original specs) and adapted logic to calculate deposits for FOC items correctly.

**Blockers & Risks**
*   **Historical Blocker:** SAP Access Request was submitted on 2026-02-16; development remained paused until connection instructions were provided on 2026-02-23.
*   **Current State:** All major blockers (SAP access, API updates, duplicate handling) are resolved. The ticket is marked as "Done" and queued for release.

**Pending Actions**
*   **None identified within this ticket.** The implementation is complete and tested against 5 continuous orders.

**Key Dates & References**
*   **2026-01-30:** Ticket opened with high priority.
*   **2026-02-16:** SAP access request submitted; development paused due to block on DPD-551.
*   **2026-02-20:** `order-v3` gRPC API updated (ref: Michael Bui).
*   **2026-02-23:** First successful BCRS deposit posted to SAP; connection instructions shared via Google Chat.
*   **2026-03-04:** Discovery of `freeItems` field affecting FOC logic.
*   **2026-03-06:** GCP PubSub "delivery once" policy enabled to prevent duplicates.

**Technical References**
*   **SAP API Response Logs:** Detailed JSON logs provided on 2026-02-23 showing successful (Doc No: 6500037303) and error scenarios (missing customer name).
*   **Subtask:** DPD-590 (Clean up archived proposals after PRD release).
*   **Linked Issues:** Blocks DPD-551.


## jira/DPD-273: Take over Segment destination functions from OSMOS
Source: jira | Key: DPD-273 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done | blocks: DPD-645, DPD-645
**Jira Ticket Summary: DPD-273**
**Ticket:** DPD-273: Take over Segment destination functions from OSMOS
**Status:** Done
**Assignee/Reporter:** Michael Bui
**Priority:** High
**Type:** Chore

**Current Status & Outcome**
The task to take over Segment destination functions has been marked **Done**. The work was completed pending the receipt of a handover document from the OSMOS team.

**Key Timeline & Events**
*   **2026-01-23:** Ticket created by Michael Bui. Associated with IT Helpdesk and linked as blocking issue DPD-645.
*   **2026-02-14:** Work placed on hold pending the handover document from Vipul (OSMOS).
*   **2026-03-06:** Handover document provided by Vipul, allowing the task to proceed and eventually reach a "Done" resolution.

**Action Items & Ownership**
*   **Primary Owner:** Michael Bui executed the takeover functions.
*   **External Dependency:** Vipul (OSMOS) was responsible for providing the necessary handover documentation.
*   **Blocking Issue:** Resolution of DPD-273 is linked to blocking issue **DPD-645**.

**Decisions & Dependencies**
*   It was decided that the takeover could not proceed until the OSMOS team provided specific documentation.
*   The task remains dependent on the completion of linked issue **DPD-645**, which it blocks.

**Technical References**
*   **Source System:** OSMOS
*   **Target System:** Segment destination functions
*   **Related Issues:** DPD-273 (current), DPD-645 (blocker).


## jira/DPD-590: Clean up archived proposals after PRD release
Source: jira | Key: DPD-590 | Status: TO BE DEFINED (To Do) | Type: Subtask | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Due: 2026-04-24 | child: DPD-383 | parent: DPD-383
**Jira Ticket Briefing: DPD-590**

**Current Status & State**
*   **Ticket ID:** DPD-590 (Subtask of parent ticket **DPD-383**: "Sales posting for BCRS deposit amount").
*   **Status Category:** To Do.
*   **Formal Status:** TO BE DEFINED.
*   **Priority:** High.

**Ownership & Pending Actions**
*   **Assignee/Reporter:** Michael Bui is the single owner of this task.
*   **Pending Action:** Identify archived proposals within the repository and execute a cleanup to empty the archive folder.
*   **Objective:** Remove stale data to prevent future AI hallucinations during processing.

**Decisions Made**
*   No technical implementation decisions have been recorded yet; the status remains "TO BE DEFINED." The scope is strictly limited to cleaning the archive folder post-**PRD release**.

**Key Dates & Deadlines**
*   **Due Date:** April 24, 2026.
*   **Last Activity:** February 23, 2026 (Ticket creation and initial definition by Michael Bui).

**Blockers & Dependencies**
*   Execution is contingent upon the completion of the parent task (**DPD-383**) or its associated PRD release phase, as indicated by the ticket title "Clean up archived proposals **after PRD release**."


## jira/QE-1105: New project setup for BCRS deposit posting job "ntuclink_bcrs-deposit-posting"
Source: jira | Key: QE-1105 | Status: Done (Done) | Type: Chore | Priority: High | Reporter: Michael Bui | Resolution: Done | parent: QE-682
**Jira Ticket Summary: QE-1105**

**Current Status**
*   **State:** Done (Resolution: Done).
*   **Ticket ID:** QE-1105.
*   **Priority:** High.
*   **Type:** Chore.
*   **Reporter:** Michael Bui.
*   **Assignee:** None currently assigned.

**Key Technical Context & Decisions**
*   **Project Setup:** Completed configuration for the SonarCloud project `ntuclink_bcrs-deposit-posting`.
*   **Source Repository:** `bcrs-deposit-posting` (Repository link not populated).
*   **Language:** Golang.
*   **Quality Gate:** Configured with "Low Tolerance".
*   **Team Ownership:** DPD Omni/Ecom.
*   **Parent Task:** Part of epic QE-682 ("Sonar and other Adhoc support requests").

**Actions & Ownership**
*   **Pending Actions:** None. The ticket is fully resolved as a setup chore.
*   **Ownership:** No active assignee; the task was initiated and closed by Michael Bui.

**Timeline & Blockers**
*   **Last Activity Date:** February 19, 2026 (10:20 AM +0800).
*   **Deadlines:** None specified (`duedate` is null).
*   **Blockers:** None identified; the setup has been successfully completed.

**Summary for Briefing**
The high-priority chore QE-1105 regarding the new project setup for the BCRS deposit posting job is complete. Michael Bui established the SonarCloud integration for the Golang repository `bcrs-deposit-posting` under the DPD Omni/Ecom team, applying a low-tolerance quality gate. This work satisfies requirements under parent ticket QE-682. No further actions or assignments are required for this specific item.


## jira/DPD-519: [RMN] Unblock NTP connection for Advertima devices
Source: jira | Key: DPD-519 | Status: Done (Done) | Type: Chore | Priority: Medium | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done
**Daily Work Briefing Summary: DPD-519**

*   **Current Status:** Done. The ticket has been fully resolved with no outstanding work required.
*   **Pending Actions & Ownership:** None. All tasks are complete.
    *   **Owner:** Michael Bui (Assignee/Reporter).
*   **Decisions Made:**
    *   No specific technical decisions or architectural changes were documented in the ticket comments; however, the resolution confirms that the NTP connection for Advertima devices has been successfully unblocked as requested in the title.
*   **Key Dates & Deadlines:**
    *   **Ticket Creation:** February 9, 2026, at 17:50 (UTC+8).
    *   **Resolution Date:** February 14, 2026, at 11:10 (UTC+8).
    *   **Deadline:** None specified; resolved five days after creation.
*   **Blockers:** No blockers identified post-resolution.

**Ticket Details**
*   **ID:** DPD-519
*   **Type:** Chore
*   **Priority:** Medium
*   **Title:** [RMN] Unblock NTP connection for Advertima devices


## jira/DPD-221: New SKU Sync Optimisation
Source: jira | Key: DPD-221 | Status: Done (Done) | Type: Epic | Priority: High | Reporter: Michael Bui | Resolution: Done | parent: DPD-220
**Daily Briefing Summary: DPD-221**

**Status & State**
*   **Ticket ID:** DPD-221
*   **Title:** New SKU Sync Optimisation
*   **Type:** Epic
*   **Current Status:** Done (Resolution: Done)
*   **Priority:** High
*   **Reporter:** Michael Bui

**Pending Actions & Ownership**
*   **Actions Pending:** None. The ticket is fully resolved.
*   **Assignee:** Currently unassigned (`null`), indicating no immediate owner for follow-up tasks as the work is complete.

**Decisions Made**
*   No specific decision log entries were recorded in the provided chronological content; however, the "Done" status confirms the team has concluded all activities related to the SKU Sync Optimisation scope defined under this Epic.

**Key Dates, Deadlines & Blockers**
*   **Last Activity Date:** 2025-09-30 (10:16 AM UTC+8) – Status updated to Done by Reporter Michael Bui.
*   **Deadlines:** No specific due date was set (`null`).
*   **Blockers:** None identified; the ticket resolution confirms successful completion without impediments.

**Summary**
The "New SKU Sync Optimisation" Epic (DPD-221), initiated by Michael Bui, is now officially marked as Done with a High priority level. The work was finalized on September 30, 2025. There are no outstanding actions, assigned owners, or scheduled deadlines associated with this ticket at this time.


## jira/NEDMT-2288: [CDP] Access Request from Retail Media
Source: jira | Key: NEDMT-2288 | Status: Done (Done) | Type: Task | Priority: Blocker | Assignee: Yadear Zhang | Reporter: Michael Bui | Resolution: Done
**Daily Briefing Summary: NEDMT-2288**

*   **Current Status:** The ticket **[CDP] Access Request from Retail Media** is marked as **Done**. The issue has been resolved with the resolution status set to "Done."
*   **Actions Pending:** No actions are pending. The assignee, **Yadear Zhang**, confirmed at 12:05 AM on November 17, 2025 (local time), that access has been granted and requested verification from the reporter.
*   **Decisions Made:** It was decided to grant **Source Admin** access in the production environment for user **vipul.gupta_fp@ntucguest.com**, as they previously held only UAT environment permissions.
*   **Key Dates & Blockers:**
    *   **Ticket ID:** NEDMT-2288
    *   **Priority:** Blocker
    *   **Request Date:** November 17, 2025 (11:30 AM)
    *   **Resolution Date:** November 17, 2025 (12:05 PM)
    *   **Blocker Status:** Resolved. The blocker was a missing production access level for the specified user.

**Stakeholders & Details:**
*   **Reporter:** Michael Bui
*   **Assignee:** Yadear Zhang
*   **User Receiving Access:** vipul.gupta_fp@ntucguest.com
*   **Environment:** Production (previously restricted to UAT only).


## jira/DPD-431: "Ad" product copy display not consistent at times
Source: jira | Key: DPD-431 | Status: TO BE DEFINED (To Do) | Type: Bug | Priority: Low | Reporter: Vivian Lim Yu Qian | Labels: priority:improvement
### Daily Briefing Summary: DPD-431

**Current Status & State**
*   **Ticket ID:** DPD-431 ("Ad" product copy display not consistent at times)
*   **Status Category:** To Do (Status: TO BE DEFINED)
*   **Type/Severity:** Bug, Priority Low. Label: `priority:improvement`.
*   **Issue Description:** In PROD Android 7.20.0 (680.7f77), "Ad" product copy occasionally displays with font colors that make it appear as part of the product title. The expected behavior is consistent formatting across the same PLP.
*   **Technical Context:** The issue appears related to the display/disappearance of the label/custom label within the product title.

**Pending Actions & Ownership**
*   **Owner:** Unassigned (Assignee: null).
*   **Action Required:** Verification and decision on release strategy for a fix that is technically complete but not yet deployed.
*   **Key Discussion Points:**
    *   **Michael Bui** noted the issue relates to label visibility, referencing a prior discussion where a fix was identified but requires verification.
    *   **Andin Eswarlal Rajesh** clarified that the bug is already fixed in code but was omitted from the previous regular release cycle. He raised the question of whether a hotfix is required.

**Decisions Made**
*   No final decision has been reached regarding deployment strategy (regular release vs. hotfix). The ticket remains in "TO BE DEFINED" status awaiting this determination.

**Key Dates & Blockers**
*   **Reported:** 2026-02-05 by Vivian Lim Yu Qian.
*   **Last Update:** 2026-02-06 (Discussions by Michael Bui and Andin Eswarlal Rajesh).
*   **Blockers:** None technical; the blocker is administrative/decisional pending a release plan for the existing fix.
*   **Due Date:** None set.

**Next Steps**
*   Assignee needs to be identified.
*   Stakeholders must decide if a hotfix is necessary or if the fix will wait for the next regular release.


## jira/OMNI-1191: [OSMOS only] Enable offsite ads integration with Meta on OSMOS
Source: jira | Key: OMNI-1191 | Status: Define (In Progress) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: RM-556
**Ticket:** OMNI-1191 (Idea: [OSMOS only] Enable offsite ads integration with Meta on OSMOS)
**Assignee:** Nikhil Grover | **Priority:** High | **Current Status:** Red / Blocked

**Current State**
The project is currently stalled awaiting external dependencies from Meta. While API documentation was received in October, critical configuration updates and campaign whitelisting remain incomplete. Testing of the first use case is pending completion due to a reported error escalated to Meta on 2026-01-22.

**Pending Actions & Ownership**
*   **Meta (External):** Enable specific campaign whitelisting; resolve API testing errors; provide firm ETAs. Owner: External vendor, currently unresponsive.
*   **Bryan:** Escalation to senior Meta leads initiated on 2025-10-08 and again on 2026-01-22 to unblock configuration and whitelisting.
*   **Nikhil Grover:** Ongoing follow-ups with Meta; coordination with OSMOS post-testing.
*   **Performance Marketing Team:** Confirmed correct config enabled (2025-11-05).
*   **OSMOS Team:** Awaiting whitelisting to complete API testing; pending confirmation of effort estimate and timeline upon resolution.

**Key Decisions & Context**
*   **Solution Path:** Integration requires updated Meta Ads account configuration, specific campaign whitelisting, and OSMOS development (estimated 4–6 weeks once enabled).
*   **Impact:** Targeting $600k RMN Offsite revenue increase; baseline of 7-8 offsite campaigns/month.
*   **Escalation Path:** Due to lack of response from Meta standard channels, issues have been escalated to senior Meta leads and internal business stakeholders (11/11).

**Key Dates & Blockers**
*   **Blocker:** No update from Meta on campaign whitelisting or configuration as of 2026-01-29.
*   **Critical Risk:** Delivery within 2025 is at high risk; ~4–6 weeks of development time remains after API testing completion.
*   **Recent Milestones:**
    *   2025-10-22: Status marked Red due to lack of Meta configuration update.
    *   2025-11-05: Performance Marketing confirmed config enabled; OSMOS target ETA for testing completion was 14 Nov (missed).
    *   2026-01-22: Testing error escalated to Meta with expectation of response by week-end.
    *   2026-01-29: No further updates; blocked status continues.

**Linked Issues:** RM-556


## jira/DPD-220: Automate sync of newly onboarded SKUs into OSMOS for faster activation
Source: jira | Key: DPD-220 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Resolution: Done | Labels: priority:improvement | parent: DPD-221
### Jira Briefing Summary: DPD-220

**1. Current Status**
*   **Ticket State:** `IN RELEASE QUEUE` (Resolved as Done).
*   **Parent Ticket:** DPD-221 (New SKU Sync Optimisation).
*   **Context:** The automation to sync newly onboarded SKUs into OSMOS is technically complete and verified in the pre-production GCS bucket (`gs://fpg-spotlight-osmos-preprod/`). Files contain >500k rows matching PRD data.

**2. Pending Actions & Ownership**
*   **Action:** Approve final Production Deployment (PRD) rollout.
    *   **Owner:** Team Lead / Decision Maker (Michael Bui has requested approval; Nikhil Grover delegated the decision).
*   **Action:** Execute production deployment steps:
    1.  Create service account.
    2.  Request BigQuery access.
    3.  Request Osmos GCS bucket access.
    4.  Deploy job and verify end-to-end functionality.
    *   **Owner:** Michael Bui.
*   **Action:** Post-deployment verification:
    *   Verify file generation matches previous snapshots (approx. 500k rows).
    *   Confirm no SKU mapping gaps exist.
    *   **Owner:** Michael Bui.

**3. Decisions Made**
*   **UAT Waiver:** Formal User Acceptance Testing was deemed impossible because the data source is BigQuery containing only live production data; it cannot be modified for testing.
*   **Risk Mitigation Strategy:** Proceeding to production without UAT sign-off based on:
    *   Automated sanity check (file count >500k).
    *   Manual historical comparison during SIT confirming ~500k matches.
    *   Availability of timestamped snapshots for immediate rollback if errors occur.
*   **Final Decision:** Nikhil Grover (Jan 22, 15:02) delegated the rollout decision to Michael Bui due to the inability to perform UAT.

**4. Key Dates & Blockers**
*   **Blocker:** Lack of isolated UAT environment (resolved via waiver).
*   **Timeline Events:**
    *   *Dec 18, 2025:* Pre-prod files generated and verified (>500k rows).
    *   *Jan 12, 2026:* Michael Bui flagged ticket pending UAT for one month.
    *   *Jan 22, 2026:* Risk analysis completed; decision made to proceed without UAT.
    *   *Jan 26, 2026:* Final pre-deployment verification of hourly file generation and logging completed by Michael Bui.

**5. Technical References**
*   **Bucket:** `gs://fpg-spotlight-osmos-preprod/sku-vendor-mapping/`
*   **Data Source:** BigQuery (Production only).
*   **Quality Gate:** File size >500k rows; Match rate ~500k rows vs. previous snapshot.
*   **Safety Mechanism:** Hourly snapshots with timestamps for rollback capability.


## jira/QE-843: Mutation Testing Implementation - rmn-osmos-purchase-event-tracking
Source: jira | Key: QE-843 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Oktavianer Diharja | Reporter: Oktavianer Diharja | Resolution: Done | parent: QE-829
**Jira Ticket Briefing: QE-843**

**Current Status**
*   **Status:** Done / Resolution: Done.
*   **Context:** The ticket addresses the implementation of mutation testing for the `rmn-osmos-purchase-event-tracking` repository, originally identified as a gap in standard CI/CD practices during PR reviews.
*   **Completion Note:** Work was marked as "Done" on 2026-01-26 by Oktavianer Diharja, with a retrospective note confirming completion occurred in September 2025.

**Actions Pending & Ownership**
*   **No pending actions.** The ticket is fully resolved.
*   **Previous Owner:** Oktavianer Diharja (Assignee/Reporter).
*   **Historical Blocker Action:** On 2025-08-07, the assignee placed the task on hold to sync with an unspecified party regarding PR implementation; a colleague was subsequently tagged (`cc`) to assist.

**Decisions Made**
*   **Implementation Path:** Mutation testing tools were added to the repository's CI/CD pipeline to cover Pull Requests.
*   **Timeline Adjustment:** Despite initial gaps noted in August 2025 and follow-up reminders in January 2026, the task was retrospectively confirmed as completed in September 2025.

**Key Dates & Blockers**
*   **Ticket Created:** 2025-08-05 (Title: Mutation Testing Implementation - rmn-osmos-purchase-event-tracking).
*   **Gap Identified:** 2025-08-07 – Assignee noted missing mutation testing in PRs.
*   **Temporary Hold:** 2025-08-07 – Task paused pending synchronization with a team member.
*   **Follow-up Requested:** 2025-08-13 – Assigned "to be followed up."
*   **Retrospective Completion:** 2026-01-26 – Ticket marked Done with confirmation of September 2025 delivery.
*   **Parent Context:** Part of parent ticket **QE-829** ("Staff Excellence (Retail Media) QE Onboarding").

**Technical References**
*   **Repository:** `rmn-osmos-purchase-event-tracking`
*   **CI/CD Focus:** Pull Request pipelines.
*   **Priority:** High.
*   **Issue Type:** Chore.


## jira/QE-842: Mutation Testing Implementation - rmn-osmos-product-feeder
Source: jira | Key: QE-842 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Oktavianer Diharja | Reporter: Oktavianer Diharja | Resolution: Done | parent: QE-829
**Ticket Summary: QE-842 - Mutation Testing Implementation (rmn-osmos-product-feeder)**

*   **Current Status:** **Done**. The ticket was resolved on January 26, 2026.
*   **Owner & Assignment:** Assigned and reported by **Oktavianer Diharja** (QE Onboarding). Priority: High. Type: Chore. Parent Ticket: **QE-829** (Staff Excellence (Retail Media) QE Onboarding).

**Key Actions & Timeline**
1.  **Initial Assessment (Aug 7, 2025):** Oktavianer Diharja identified that while the `rmn-osmos-product-feeder` repository implements a standard CI/CD pipeline, mutation testing is not currently configured for Pull Requests. The task was initially placed "on hold" pending synchronization with relevant stakeholders.
2.  **Collaboration (Aug 7, 2025):** Oktavianer Diharja engaged with another team member (noted as "cc") to facilitate the addition of mutation testing.
3.  **Follow-up Request (Aug 13, 2025):** A request was made to ensure the implementation is followed up on.
4.  **Final Resolution (Jan 26, 2026):** The assignee confirmed the task as complete, noting in the comment that the actual work was finished in **September 2025**.

**Decisions Made**
*   It was decided to implement mutation testing within the existing CI/CD pipeline for Pull Requests in the `rmn-osmos-product-feeder` repository.
*   The implementation was executed and completed in September 2025, despite the ticket remaining open until January 2026.

**Pending Actions & Blockers**
*   **No pending actions.** The status is "Done."
*   **Blockers:** Initial delay occurred due to a lack of synchronization regarding implementation details (recorded on Aug 7). This was resolved via team coordination.

**Technical References**
*   **Repo:** `rmn-osmos-product-feeder`
*   **Focus Area:** Mutation Testing for Pull Requests within the CI/CD pipeline.


## jira/DPD-1: Foundation Setups
Source: jira | Key: DPD-1 | Status: Done (Done) | Type: Epic | Priority: High | Reporter: Michael Bui | Resolution: Done | parent: DPD-7, DPD-6
**Daily Briefing: Jira Ticket DPD-1 (Foundation Setups)**

*   **Current Status:** The Epic **DPD-1: Foundation Setups** is marked as **Done**. Both the `status` and `resolution` fields confirm completion. The work associated with this ticket is closed.
*   **Ownership & Pending Actions:** There are no pending actions for this ticket. The **assignee** field is null, indicating that execution was completed without a specific long-term owner assigned post-completion or was handled as a team effort. The ticket was reported by **Michael Bui**.
*   **Decisions Made:** No active decisions remain to be made regarding the scope of "Foundation Setups" as the item has reached its final resolution state. The high-priority nature of this foundational work has been addressed and finalized.
*   **Key Dates & Blockers:**
    *   **Priority:** High (as reported by Michael Bui).
    *   **Deadline:** No due date was set (`duedate` is null).
    *   **Last Activity:** The ticket status was updated to "Done" on **2026-01-14** at 14:25:32 (UTC+8).
    *   **Blockers:** None identified; the ticket resolution confirms successful closure.

**Summary:**
The high-priority Epic **DPD-1: Foundation Setups**, reported by **Michael Bui**, is fully resolved and closed as of January 14, 2026. No further actions or ownership assignments are required for this specific item.


## jira/DPD-7: Create new email groups
Source: jira | Key: DPD-7 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Daryl Ng | Reporter: Michael Bui | Resolution: Done | Labels: priority:operations | parent: DPD-1
**Daily Briefing Summary: DPD-7**

**Ticket Status & Ownership**
*   **Current State:** Done (Resolution: Done).
*   **Assignee:** Daryl Ng.
*   **Reporter:** Michael Bui.
*   **Priority:** High.
*   **Type:** Chore / Operations.
*   **Parent Epic:** DPD-1 (Foundation Setups).

**Key Actions Completed**
Daryl Ng successfully created the following new email groups on **2026-01-15**:
1.  **dpd-ecom:** Configured for Sneha's team.
2.  **dpd-omni:** Configured for Daryl, Michael, and Rajesh's teams.

**Decisions Made**
Michael Bui defined the specific membership scope for both groups during ticket creation to align with operational needs:
*   The `dpd-ecom` channel was restricted exclusively to Sneha's team.
*   The `dpd-omni` channel was established as a cross-functional group including Daryl, Michael, and Rajesh.

**Pending Items & Blockers**
*   **Pending Actions:** None. All setup tasks are complete.
*   **Blockers:** None identified.
*   **Deadlines:** No due date was set; the task was completed immediately upon creation (Jan 15).

**Technical References**
*   Ticket ID: DPD-7
*   Parent Key: DPD-1
*   Labels: `priority:operations`


## jira/DPD-6: Configure ticket types and transition
Source: jira | Key: DPD-6 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done | Labels: priority:operations | parent: DPD-1
**Daily Briefing Summary: DPD-6**

*   **Current Status:** The ticket is marked as **Done**. All work associated with this item has been completed.
*   **Actions Pending:** There are no pending actions or ownership transfers required for this specific ticket. The assignee and reporter, **Michael Bui**, have finalized the task.
*   **Decisions Made:** The scope was defined as configuring ticket types and transitions within the system. This configuration has been successfully implemented and resolved.
*   **Key Dates & Deadlines:** No due date was assigned to this item. The final status update occurred on **2026-01-15**. There are no reported blockers preventing completion.

**Ticket Metadata Context:**
This task (**DPD-6**) is categorized as a **Chore** with **High** priority and carries the label `priority:operations`. It serves as a sub-task for the parent initiative **DPD-1 (Foundation Setups)**. The work was executed entirely by **Michael Bui**.


## jira/DPD-8: [RMN] Renew guest account for RMN contractor
Source: jira | Key: DPD-8 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done | Labels: priority:operations
**Daily Briefing Summary: DPD-8**

*   **Current Status:** Done. The task has been completed with a resolution of "Done."
*   **Pending Actions & Ownership:** None. All actions described in the ticket history are closed.
    *   *Note:* While an IT Helpdesk ticket was created, no specific ID or follow-up action is listed as pending within this record; the creation itself marks the completion of the workflow for this Jira issue.
*   **Decisions Made:**
    *   The renewal request for guest account `rafat.qayum_ne@ntucguest.com` was approved by Michael Bui on 2026-01-15 at 13:51 (+0800).
    *   An IT Helpdesk ticket was officially created to execute the renewal immediately following approval.
*   **Key Dates & Blockers:**
    *   **Ticket Created/Completed:** 2026-01-15 (All activities occurred between 13:23 and 14:03 on this date).
    *   **Blockers:** None identified.
    *   **Deadline:** No due date (`null`) was set for this Chore; the High priority label indicates urgency, which was addressed within the same day.

**Details:**
*   **Resource ID:** DPD-8
*   **Title:** [RMN] Renew guest account for RMN contractor
*   **Assignee/Reporter:** Michael Bui
*   **Priority:** High
*   **Type:** Chore (Operations)
*   **Target Account:** `rafat.qayum_ne@ntucguest.com`
*   **Timeline:**
    *   13:23: Ticket opened and status set to Done.
    *   13:51: Approval recorded.
    *   14:03: IT Helpdesk ticket creation confirmed.


## jira/OMNI-1297: Near Real-time Inventory Indexing for FFS to Decrease OOS Impressions on Search
Source: jira | Key: OMNI-1297 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Ram Datchnamoorthy | polaris-work-item-link: PRDM-239
**Resource:** OMNI-1297: Near Real-time Inventory Indexing (NRTI) for FFS to Decrease OOS Impressions on Search
**Assignee:** Prajney Sribhashyam | **Reporter:** Ram Datchnamoorthy | **Priority:** High | **Status:** Backlog / Deprioritized

### Current Status
The initiative has been **deprioritized** and removed from the pre-holiday "must-have" list. The decision stems from a comparison between NRTI and an alternative "Available to Promise" (ATP) initiative. While NRTI offers a higher estimated annual GMV impact (~$1.5M), it requires a "Medium to Large" effort, whereas ATP offers $1M–$1.25M GMV impact with "Small" effort.

Concurrently, engineering feedback confirmed that the current NRTI solution might not survive the upcoming re-platform unless significant work is done now. However, as of Oct 28, 2025, it was agreed to deprioritize NRTI in favor of ATP for immediate execution.

**Final Directive (Jan 19, 2026):** The functionality will be covered within the broader **re-platform** scope rather than as a standalone initiative.

### Key Decisions
*   **Deprioritization:** NRTI removed from pre-holiday delivery targets (Oct 28, 2025).
*   **Replacement:** "Available to Promise" (linked issue: PRDM-239) will take priority over NRTI.
*   **Re-platform Strategy:** NRTI requirements are now slated for inclusion in the future re-platform rather than immediate development.

### Pending Actions & Ownership
*   **Ownership:** Prajney Sribhashyam (Lead), with support from Qiuyan Tian and Ryne Cheow during evaluation phases.
*   **Pending:** No active development tasks remain on this ticket as it is deferred to the re-platform. The group previously convened on Oct 21, 2025, to make the priority decision.

### Key Dates & Deadlines
*   **Oct 16, 2025:** Deadline for t-shirt sizing and solution viability assessment (identified as "Medium" effort).
*   **Oct 21, 2025:** Target date for re-grouping to decide between NRTI vs. ATP.
*   **Oct 28, 2025:** Final decision made to deprioritize NRTI in favor of ATP.
*   **Jan 19, 2026:** Confirmation that the solution will be handled via re-platform.

### Blockers & Technical Context
*   **Relevance to Re-platform:** Initial concerns existed that this solution would not survive the re-platform (Oct 14). Later confirmation (Oct 17) suggested potential reusability, but the effort vs. ROI calculation drove the deprioritization.
*   **Impact Metrics:** The initiative originally targeted reducing Out-of-Stock (OOS) impressions on search, with a GMV impact estimate of $1.72M during peak periods (e.g., CNY).
*   **Linked Issue:** PRDM-239 (Polaris work item link) regarding Available to Promise evaluation.


## jira/OMNI-1339: Integration of Pine Labs API to replace the current e-Voucher platform
Source: jira | Key: OMNI-1339 | Status: UAT (In Progress) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Jia Xuan Tan | Labels: gifting | polaris-work-item-link: PRO-2419, DPD-226
**Jira Ticket Briefing: OMNI-1339**
**Subject:** Integration of Pine Labs API to replace current e-Voucher platform
**Current Status:** In Progress (UAT phase; previously marked Technical Live)
**Assignee:** Rajesh Dobariya | **Reporter:** Jia Xuan Tan

### **Current Status & State**
The initial development scope from the OMNI side was completed and pushed to production with feature flags off. However, the project reverted to "In-Development" following performance issues identified by the CCO team requiring additional work. While a specific bug reported during UAT was fixed and communicated to the Pine Labs (PL) team on Feb 12, the launch is currently stalled. The ticket remains open awaiting final sign-offs and compliance resolution.

### **Pending Actions & Ownership**
*   **DPD Performance/Load Testing Sign-off:** CCO team (James) must secure DPD sign-off. This was originally due Feb 6 but remains pending with no confirmed date as of March 11. Owner: **CCO Team (James)**.
*   **Data Migration Audit:** Currently in progress. Ownership unspecified, tracked by OMNI/CCO alignment.
*   **Compliance Items:** CCO team needs to address compliance-related blockers causing the launch delay. Owner: **CCO Team**.
*   **Follow-up:** Rajesh Dobariya to follow up on the status of DPD sign-off and performance testing results.

### **Decisions Made**
*   **Scope Change:** Original scope completed; new Epic required for additional CCO-driven work (performance optimization). A new delivery ticket was added with a dev completion ETA of Dec 30.
*   **Go-Live Timeline Shifts:**
    *   Initially targeted for end-Sept, then pushed to Jan 2026, then postponed to post-CNY (Feb/March 2026).
    *   Current target Go-Live date set for **March 30, 2026**.
*   **Mitigation:** A follow-up discussion was scheduled between James and Sisir on Nov 17 to determine go/no-go status; however, subsequent delays occurred.

### **Key Dates, Deadlines & Blockers**
*   **Test Completion (UAT):** Scheduled for Jan 30 (per timeline shared by Sisir).
*   **DPD Sign-off:** Originally targeted Feb 6; currently delayed with no new date.
*   **Launch Target:** March 30, 2026.
*   **Primary Blocker:** Compliance-related work required by the CCO team; delays in DPD performance testing sign-off. No new launch date communicated as of March 11.

### **Technical & Business Context**
*   **Linked Issues:** PRO-2419, DPD-226.
*   **Integration Scope:** Replacing `https://www.gift.fairprice.com.sg/` with Pine Labs platform. Requires migration of e-Voucher data and 7+ API integrations (Strudel SDK update).
*   **Business Impact:** $158m value; targets efficiency, fraud control, and scalability for the Gifting team (12 staff).
*   **Performance Testing:** PL team was instructed to share results by Jan 9; full timeline includes DPD sign-off on Feb 6.


## jira/OMNI-1249: B2B Solution: Integration work
Source: jira | Key: OMNI-1249 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Erica Lee | Reporter: Fiona U | blocks: OMNI-1362, OMNI-1362 | discovery---connected: DPD-57 | migration_parent: PAY-7080 | polaris-work-item-link: DPD-682, PAY-7080, DPD-57
**Ticket Summary: OMNI-1249 (B2B Solution: Integration Work)**
**Assignee:** Erica Lee | **Reporter:** Fiona U | **Status:** RED (In Development) | **Priority:** High

### Current Status & State
The project is currently **RED**, indicating critical delays. The B2B platform MVP Go-Live has been pushed from the original timeline to **April 2026**. Progress is heavily constrained by the readiness of the WMS Middleware and SAP integration. While SIT (System Integration Testing) concluded between March 2–6, UAT is now scheduled for mid-to-late March (originally planned for March 23).

### Key Decisions & Strategic Direction
*   **SAP Strategy:** Per Dennis's advice (Dec 9, 2025), the team will proceed with **"Co-mall"** on SAP.
*   **Technical Architecture:** The launch relies on **Phase 2** of the WMS Middleware go-live to enable B2B fulfillment and sales posting flows to SAP. Phase 1 (mid-March) only routes orders to PFC via SAP but does not support full B2B billing/document flows.
*   **Scope Adjustment:** Due to increased scope including **BCRS** and Co-mall requirements, a new sprint was tentatively added. No callouts from the Comall end are expected for the April planning immediately.

### Pending Actions & Owners
*   **WMS Middleware Confirmation (Critical):** The WMS team must confirm if the mid-March go-live includes **Phase 2** functionality required for finance and sales posting. Current status is "not confirmed." Owner: **Zi Ying Liow / WMS Team**.
*   **SAP Blueprint Sign-off:** Pending review session with CC and Finance scheduled for January 16, 2026. Delays here directly impact SAP development. Owner: **CC & Finance**.
*   **UAT Execution:** UAT test cases to be finalized by Feb 22; inputs gathered Feb 23–25; business socialization Feb 26–27. Comall UAT testing scheduled for March 3 (updated context suggests mid-March). Owner: **Zi Ying Liow / Comall**.
*   **Usability Refinements:** Feedback on B2B web and Back-Office usability consolidated and shared with Comall for "Project Light." Final requirements to be sent to Comall. Owner: **Internal Alignment Team / Comall**.
*   **Dependency Resolution (March 11):** Two specific dependencies require immediate attention:
    1.  **Decoupling First Mile:** Confirmation needed on whether PFC and First Mile training for MP apps can be decoupled from the B2B launch. Owner: **Zi Ying Liow**.
    2.  **Forecasting & Reporting:** Alignment required on setup for sales order flow forecasting/reporting. Call scheduled March 11. Owner: **Relevant Business Stakeholders**.

### Key Dates & Deadlines
*   **Mid-March (2026):** Target WMS Middleware Phase 1 Go-Live (and potential re-evaluation of Phase 2 readiness).
*   **March 3, 2026:** UAT testing with Comall.
*   **March 11, 2026:** Call to resolve Forecasting/Reporting alignment and First Mile decoupling status.
*   **April 2026 (Tentative):** B2B Platform Go-Live.

### Blockers & Risks
*   **WMS Middleware Readiness:** No confirmed go-live date for Phase 2; this is the single biggest blocker preventing April launch.
*   **SAP Blueprint Sign-off:** Any delay in the Jan 16 sign-off (historical context) or subsequent reviews impacts development timelines.
*   **Scope Creep:** Inclusion of BCRS and Co-mall integration necessitated a new sprint, potentially straining resources for the April deadline.

**Linked Issues:** DPD-682, OMNI-1362 (Blocks), PAY-7080, DPD-57.


## jira/OMNI-1363: [Decoupling from SAP] Migrate CF apps to DBP to improve MP Consol fulfilment experience
Source: jira | Key: OMNI-1363 | Status: Paused (To Do) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Gopalakrishna Dhulipati | polaris-work-item-link: DST-2272, DPD-326, DPD-332, DPD-341, DST-2531, DPD-348
**Ticket:** OMNI-1363 | [Decoupling from SAP] Migrate CF apps to DBP to improve MP Consol fulfilment experience
**Assignee:** Prajney Sribhashyam | **Reporter:** Gopalakrishna Dhulipati | **Priority:** High | **Status:** Paused (To Do)
**Linked Issues:** DST-2272, DPD-326, DPD-332, DPD-341, DST-2531, DPD-348

### Current Status
*   **Overall State:** Delayed (Red).
*   **Development Progress:** CF app development is complete. SAP de-coupling components are in progress but delayed due to WMS Middleware dependencies.
*   **WMS Middleware:** Production live scheduled for 14 March; UAT and rollout tentatively scheduled post-CNY.
*   **Risk Level:** High risk regarding business live date due to WMS Middleware delays.

### Pending Actions & Ownership
*   **Date Confirmation:** Update ticket with exact timelines post-realignment meeting (Action: Team, referenced by Sathya Murthy Karthik on 2026-03-11).
*   **Stakeholder Communication:** Confirm and communicate UAT/Rollout timelines to the PFC team following alignment sessions.
*   **Alignment:** Pending final alignment with PFC & First Mile teams (originally planned for week of 8 Dec, later impacted by WMS delays).

### Key Decisions Made
*   **Business Live Date:** Confirmed for **1 April 2026** (previously tentative Jan/Feb/March dates).
*   **Technical Go-Live:**
    *   WMS Middleware Production: 14 March 2026.
    *   DBP Order SAP Decoupling Production: 24 March 2026.
    *   CF App Tech Live: 1 April 2026.
*   **Rollout Strategy:** Managed by device to ensure no operational disruption; contingency plan for historical data risk is in development.

### Key Dates, Deadlines & Blockers
*   **Blocker:** WMS Middleware dependency (Delay shifting live from Jan to March/April).
*   **14 March 2026:** WMS Middleware Production Live.
*   **24 March 2026:** DBP Order SAP Decoupling Production Live.
*   **1 April 2026:** CF App Business Live (Confirmed).
*   **Historical Context:** Original target was Jan 2026; dev on track mid-Nov 2025, but WMS middleware Phase 1 go-live moved to post-CNY.

### Success Criteria & Scope
*   **Goal:** Eliminate $170K annual Cloud Foundry cost and improve DOT% for CF sellers.
*   **Components:** First Mile Operations App, First Mile Dashboard, PFC Receiving App.


## jira/OMNI-1362: [Decoupling from SAP] Improve order orchestration with integration to WMS Middleware
Source: jira | Key: OMNI-1362 | Status: Paused (To Do) | Type: Idea | Priority: High | Assignee: Gopalakrishna Dhulipati | Reporter: Gopalakrishna Dhulipati | blocks: OMNI-1249, OMNI-1249 | polaris-work-item-link: DPD-184 | relates: OE-3209
**Jira Ticket Summary: OMNI-1362**
**Topic:** Improve order orchestration with integration to WMS Middleware (Decoupling from SAP)
**Current Status:** **Red (Delayed)** | Priority: High | Assignee: Gopalakrishna Dhulipati / Prajney Sribhashyam

### 1. Current State & Context
The project aims to decouple SAP for financial compliance (GST) and improve fulfillment architecture by integrating DBP with WMS Middleware. While development for specific components (CF apps, SIT completed Dec 29-30) is on track or complete, the overall program status is **Red** due to delays in the upstream WMS Middleware rollout.

*   **WMS Middleware UAT:** Passed validation by WM6 and SAP teams.
*   **DBP Development:** SIT completed; however, additional scope was identified (special logic for carton items, order type logic, Boys Brigade Donation posting), adding 5 dev days.
*   **Risk Level:** High risk regarding post-CNY scheduling impacts the entire timeline.

### 2. Key Dates & Deadlines
*   **WMS Middleware Production Live:** Tentatively scheduled for **14 March 2026**.
*   **DBP Order SAP Decoupling Production Live:** Targeted for **24 March 2026**.
*   **CF App Business Live:** Confirmed for **1 April 2026**.
*   **Previous Milestones Missed:** Original tentative go-live (Nov 17, 2025) and UAT timelines were delayed due to the CNY period and WMS dependency.

### 3. Pending Actions & Ownership
*   **Timeline Confirmation:** A re-group meeting was scheduled on Jan 8 to finalize exact WMS Middleware launch dates; current target is March 14, 2026.
    *   *Owner:* Prajney Sribhashyam (Program Management).
*   **Scope Clarification (B2C vs. Project Light):** Must determine if specific B2C system work needs immediate execution or can be deferred to "Project Light."
    *   *Action:* Check with Fenny regarding the requirement scope.
    *   *Owner:* Sathya Murthy Karthik.
*   **Date Updates:** Tickets requires updated timeline documentation following recent delays.
    *   *Owner:* Prajney Sribhashyam / Sathya Murthy Karthik.

### 4. Decisions Made
*   **Rollout Strategy:** WMS Middleware rollout has been broken down into phases (Phase 1 approved).
*   **Scheduling Shift:** Business live dates have been pushed from late November/December 2025 to March/April 2026 due to CNY constraints and WMS dependency.
*   **Scope Adjustment:** Additional development work identified during SIT (carton logic, donation posting) is being accepted, necessitating a new ETA for DBP dev completion (pushed from Dec 15 to Dec 19).

### 5. Critical Blockers & Dependencies
*   **Primary Blocker:** WMS Middleware Production readiness and final rollout schedule post-CNY. Until this is confirmed as "Green," dependent SAP decoupling components cannot proceed to UAT with consumers.
*   **Linked Issues:**
    *   Blocks: OMNI-1249
    *   Relates: OE-3209, DPD-184


## jira/OMNI-1294: [BCRS Compliance] Phase 2: Order Place & Returns/Refunds Processxa
Source: jira | Key: OMNI-1294 | Status: UAT (In Progress) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Winson Lim | Labels: bcrs | discovery---connected: NEDMT-2334 | polaris-work-item-link: DPD-225
**Ticket:** OMNI-1294 | **Status:** UAT (In Progress) | **Priority:** High | **Assignee:** Prajney Sribhashyam | **Reporter:** Winson Lim
**Linked Issues:** DPD-225, NEDMT-2334

### Current State
The initiative is in the User Acceptance Testing (UAT) phase for Phase 2 (Order Place & Returns/Refunds Process). Recent updates on **Feb 12** classify the program risk as **Medium**, shifting from "At Risk" due to re-prioritization. Development is ongoing, with a target completion of **February 28**.

### Key Decisions & Strategic Shifts
*   **Re-Prioritization (Feb 12):** MP Seller listing moved to high priority to ensure customer-facing flows are ready for UAT in the week of **Feb 23**. Finance-related flows (sales posting, seller reports, invoice changes, returns/refunds) are scheduled for UAT starting **Feb 26**.
*   **Scope Reduction:** Personalization scope (swapping old SKUs with new SKUs in recommendations) has been de-prioritized to meet the April 1 launch deadline.
*   **Sales Posting Alignment:** The solution is aligned and approved by Corporate Control (CC). MP sales posting alignment with Finance is complete. An interim solution for SAP decoupling was agreed upon with Finance & SAP teams.

### Pending Actions & Owners
*   **OMS Dependency:** Resolution required regarding the dependency on OMS for seller reports (Owner: Unspecified/Team).
*   **E-Comm SKU Approval:** Category approval pending from PurSys for supplier-submitted forms regarding e-comm only SKUs.
*   **In-store Pre-order:** Identified as a "Major Issue" with unresolved blockers (Owner: Prajney Sribhashyam).
*   **Acceptance Criteria:** Clarity needed on Sales Posting and SnG (Scan & Go) Sales Posting criteria.
*   **Timeline Update:** Sathya Murthy Karthik requested date updates as of March 11.

### Critical Dates & Deadlines
*   **Dev Complete Target:** February 28, 2026.
*   **UAT (Customer Facing):** Week of Feb 23, 2026.
*   **UAT (Finance/Backend):** Starting Feb 26, 2026.
*   **SIT Complete Target:** February 28, 2026 (per working committee feedback).
*   **Regulatory Milestones:** Product labelling by April 1, 2026; Enforcement by July 1, 2026.

### Blockers & Risks
*   **High Risk Areas:** Invoice changes, Returns & Refunds logic, and MP Seller listing (prior to Feb 12).
*   **Major Issue:** In-store Pre-order functionality remains unresolved.
*   **Risk Factors:** OMS dependency for seller reports; pending Category approval for e-comm SKU data updates.

### Technical Context
The system requires linked deposit SKUs for BCRS items ($0.10 deposit) across POS, SAP, and Mirakl (MP). Deposits must be treated as separate line items in SAP and excluded from offer limits/loyalty points.


## jira/OMNI-1344: [BCRS Compliance] Phase 3: Product Discovery & Buying Experience
Source: jira | Key: OMNI-1344 | Status: UAT (In Progress) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Prajney Sribhashyam | Labels: bcrs | discovery---connected: NEDMT-2334 | polaris-work-item-link: DPD-117
**Daily Briefing Summary: OMNI-1344 [BCRS Compliance] Phase 3**

**Current Status:** UAT (In Progress). The project is currently **At Risk** regarding the timeline, with a shift from "On Track." Personalisation scope has been de-prioritized for the April 1 launch.

**Key Decisions & Scope Changes:**
*   **Personalisation De-prioritization:** Feedback from the working committee confirmed that swapping old SKUs with new SKUs in recommendations is **not a must-have** for the April 1 compliance launch.
*   **Scope Adjustment:** Focus remains on core deposit pricing, PDP/PLP visibility, and POS integration.

**Action Items & Ownership:**
*   **Timeline Alignment (Owner: Prajney Sribhashyam):** Schedule business stakeholder alignment to confirm the pull-back of the timeline for Feb 28 SIT completion.
*   **Status Update (Owner: Sathya Murthy Karthik):** Urgent request issued on March 11 to update ticket dates to reflect current progress.
*   **Program Planning:** Prajney Sribhashyam is coordinating with unspecified teams to finalize the development, testing, and change management timeline.
*   **Design Clarification (Owner: Prajney Sribhashyam):** Addressing Vivian Lim Yu Qian's query regarding PDP visibility; deposit indications on PLP must be mirrored on Product Detail Pages.

**Critical Dates & Deadlines:**
*   **Dev Completion Target:** February 28, 2026 (Current target despite "At Risk" status).
*   **SIT Complete Target:** February 28, 2026.
*   **Regulatory Milestones:** April 1, 2026 (Product labelling enforcement); July 1, 2026 (Full compliance enforcement).
*   **Goal Date:** March 2026 for 100% accurate deposit pricing and receipt breakdowns.

**Blockers & Risks:**
*   **Timeline Pressure:** The project is "At Risk" due to the need to pull back the timeline to meet the Feb 28 SIT deadline while managing stakeholder expectations.
*   **Ownership Ambiguity:** Pending confirmation on customer discovery ownership and bandwidth allocation following the new DPD structure (as noted Jan 8).
*   **Stakeholder Alignment:** Business alignment meeting was pending as of Feb 5; immediate rescheduling is required to mitigate risk.

**Technical & Compliance Context:**
*   **Linked Issues:** DPD-117, NEDMT-2334.
*   **Compliance Driver:** Singapore NEA-mandated Beverage Container Return Scheme (BCRS). Requires $0.10 deposit handling for ~130 stores and 100% of regulated beverage SKUs.
*   **System Impact:** Requires SAP enhancements, new SKU flags, barcode updates, and POS/procurement integration by April 2026. Deposit is GST-exempt and must be treated separately in flows.


## jira/OMNI-1407: Improve seller catalogue compliance to align with FSQ expectations
Source: jira | Key: OMNI-1407 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Prajney Sribhashyam | polaris-work-item-link: DPD-100
**Jira Briefing: OMNI-1407 – Improve Seller Catalogue Compliance (FSQ Alignment)**

**Current Status**
*   **State:** In Development (In Progress).
*   **Progress Indicator:** Green (On Track).
*   **Assignee:** Prajney Sribhashyam.
*   **Linked Issue:** DPD-100.

**Key Decisions & Estimates**
*   **Scope:** Implementation of mandatory "License Code" and "Expiry Date" fields on Mirakl, automatically triggered by Level 3 (L3) categories (e.g., Safety Mark, Halal).
*   **Automation Logic:** System to send expiry warnings at 4 weeks and 1 week prior; automatic SKU disabling upon certificate expiry.
*   **Sizing:** Finalized as **Small** (estimated at **30 people-days**) per Prajney Sribhashyam's update on Dec 3, correcting an earlier "T-shirt sizing" comment by Sathya Murthy Karthik.
*   **Business Impact:** Addresses high risk of $2.5M annual GMV loss from de-listing; goal is 100% FSQ compliance.

**Upcoming Dates & Deadlines**
*   **March 16, 2026:** Scheduled start for System Integration Testing (SIT).
*   **March 17, 2026:** Scheduled start for User Acceptance Testing (UAT).
*   **December 31, 2025:** Original deadline to disable non-compliant SKUs (Note: Current timeline extends into March 2026 for SIT/UAT).

**Pending Actions & Ownership**
*   **SIT/UAT Planning:** Sathya Murthy Karthik requested an update to stakeholders regarding the new March schedule and confirmation of test case creation.
*   **Stakeholder Communication:** Stakeholders must be notified of the revised timeline (March 16/17 start dates) per Sathya's request on March 11, 2026.
*   **Data Preparation:** Marketplace team to continue sourcing certifications for upload to Mirakl and conduct weekly data extractions for validation.
*   **Walkthroughs:** MP & Catalog teams conducted a walkthrough on the preceding Monday (referenced in Feb 5 update).

**Technical References**
*   **Platform:** Mirakl SKU creation form, DBP synchronization.
*   **Fields:** Mandatory inputs for license code and calendar-based expiry dates; exemption logic with explanation field required.


## jira/OMNI-1345: [MP Foundational] Sales Breakdown & Seller Payouts
Source: jira | Key: OMNI-1345 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Koklin Gan | Reporter: Prajney Sribhashyam | discovery---connected: OMNI-1178 | polaris-work-item-link: DST-2056, DST-2272, DST-2487, DPD-9
**Ticket:** OMNI-1345 [MP Foundational] Sales Breakdown & Seller Payouts
**Assignee:** Koklin Gan | **Reporter:** Prajney Sribhashyam | **Priority:** High
**Current Status:** Blocked (Previously Yellow/At Risk; now formally blocked)

### 1. Current State
The initiative aims to resolve financial data gaps regarding dropoffs, refunds, cancellations, and voucher applications to ensure accurate sales breakdowns and seller payouts. While the "Sales Breakdown Report" was initially validated with business stakeholders (Milestone 2 completed Jan 5), the full rollout is currently **blocked**.

Recent investigations by Sneha Parab revealed critical data mismatches between the new BigQuery table (`mp_sales_breakdown`) and existing production reports, specifically affecting the Finance report. The team determined that changes to seller reports must be synchronized with SKU Compliance (BCRS) before proceeding. Consequently, work on MP sales reports has been placed on hold pending BCRS completion.

### 2. Pending Actions & Ownership
*   **Finance Alignment:** Prajney Sribhashyam is finalizing alignment with Finance and Corporate Control regarding the finance reporting format and discrepancies between DBP vs. SAP data sources. Target closure for this alignment: **Jan 31** (Note: This date appears to have passed; current status indicates the block remains active).
*   **BCRS Compliance Execution:** The E-commerce team is authorized to proceed with changes required for BCRS compliance (BCRS quantity and value) across three reports: Seller Report, Combined Sales Report, and Finance Concess Report.
*   **Report Walkthrough/UAT:** Prajney Sribhashyam and Koklin Gan must conduct a runthrough of all reports with Jesslin Lim Bee Leng, Hwee Ping Lim, April Kok, and Wei Fen Ching.
    *   **UAT Timeline:** Feb 23 – Jan 6 (Note: Date likely typo for Feb 6 or Mar 6; strictly as recorded).
*   **Data Validation:** Sneha Parab's team continues to investigate discrepancies in the `mp_sales_breakdown` table pending validation from the DA and Product teams.

### 3. Key Decisions Made
*   **Scope Segmentation:** "Returns & refunds flow" alignment across RB & MP, and Sales Order Account (SOA) seller report alignment with finance were marked **Out of Scope** for this phase. These are deferred to "Project Light."
*   **Financial Principle:** A new logical flow was established for all financial statements: *Order Statement → Invoice → Sales Posting → Seller Reports → Seller Payouts*. No entries are to be re-calculated at any state; they must flow based on confirmations from previous states.
*   **Immediate Scope Change:** E-comm team can proceed with BCRS compliance changes immediately, but MP-specific sales breakdown fixes (payout accuracy) are blocked until after BCRS is complete.

### 4. Key Dates, Deadlines & Blockers
*   **Blocker:** Pending alignment on finance reporting format and data gaps between DBP vs. SAP reports. Full rollout of the enhanced Sales Breakdown Report is stalled.
*   **Linked Issues:** OMNI-1178 (Discovery), DST-2056, DST-2272, DST-2487, DPD-9.
*   **Prior Milestones:**
    *   Seller app migration: Done (Nov 30).
    *   Report validation: Done (Jan 5).
*   **Upcoming/Urgent:** BCRS compliance changes; UAT for all reports is scheduled to commence **Feb 23**.

### 5. Technical References
*   **New Data Source:** `mp_sales_breakdown` (BigQuery table).
*   **Reports Affected:** Seller Report, Combined Sales Report, Finance Concess Report.
*   **Tools:** Looker Studio (triggering reports), SAP, DBP.


## jira/OMNI-1296: Enhanced Notification Preference Center for Multi-Channel Communication Management
Source: jira | Key: OMNI-1296 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Sip Khoon Tan | Reporter: Sip Khoon Tan | discovery---connected: CORE-304 | polaris-work-item-link: CORE-304
**Jira Ticket Briefing: OMNI-1296**
**Topic:** Enhanced Notification Preference Center for Multi-Channel Communication Management
**Current Status:** In Development (High Priority)
**Assignee:** Sip Khoon Tan (Lead/Reporter); Implementation leads: Xue Yin, William.

### 1. Current State & Progress
The project aims to replace binary unsubscribe mechanisms with a granular preference center controlling EDMs, Push Notification Services (PNS), and WhatsApp across specific business swimlanes (e.g., Grocery, FP Finest, Unity, Cheers).
*   **Development Status:** Backend development is scheduled for completion by February 20, 2026. UAT is ready starting March 2, 2026.
*   **Recent Updates:** On March 11, 2026, the ticket status was amended to "In Development" following backend completion requests (Sathya Murthy Karthik).

### 2. Pending Actions & Ownership
*   **Integration Testing:** Martech team must link tickets for integration testing with Salesforce Marketing Cloud (SFMC). Owner: Xue Yin, William.
*   **UAT Execution:** User Acceptance Testing scheduled for March 12–13, 2026.
*   **Go-Live Coordination:** Finalize go-live date pending business direction. Target window: Mid-April 2026.
*   **Timeline Alignment:** Previously noted as pending alignment with CCO and CRM on timelines (Zi Ying Liow).

### 3. Decisions Made
*   **Stakeholder Engagement:** Identified Xue Yin and William as the primary contacts for building the SFMC preference center (James Huang, Sept 9).
*   **Status Tracking:** Confirmed need to link delivery tickets to accurately reflect status vs. Idea stage (Peter Talbot, Aug 27).

### 4. Key Dates & Blockers
*   **Backend Completion:** Feb 20, 2026.
*   **UAT Window:** March 12–13, 2026.
*   **Target Go-Live:** Mid-April 2026 (contingent on business direction).
*   **Technical Live (Previous Plan):** Jan 7 (Updated/Deferred to mid-April post-UAT).
*   **Blocker/Dependency:** Pending Martech link for integration testing and final business approval for the April go-live.

### 5. Business Impact & Metrics
*   **Financial Goal:** Prevent $531.6k annual GMV loss ($57.6k from EDM + $474k from PNS unsubscribes) by reducing complete unsubscribe rates by 30% initially, with a long-term target of 50%.
*   **Scope:** Supports Business Units including Grocery, FP Super/Finest/Hyper/Online, Unity, Cheers, Kopitiam, FP Partners, FP B2B, and Link Rewards.


## jira/OMNI-1425: [1HD] - Integration with 3PL vendor to push order details.
Source: jira | Key: OMNI-1425 | Status: Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Rajesh Dobariya
**Jira Briefing: OMNI-1425 – Integration with 3PL vendor to push order details**

**Current Status**
*   **Ticket ID:** OMNI-1425
*   **Status Category:** To Do (Marked as "Prioritised")
*   **Priority:** High
*   **Type:** Idea
*   **Assignee/Reporter:** Rajesh Dobariya
*   **Current State:** The initiative, originally scoped to integrate order details and live tracking with a 3PL vendor's last-mile app, has been deemed unnecessary for the immediate launch scope.

**Decisions Made**
*   **Scope Removal:** Following a discussion (chat room reference: `https://chat.google.com/room/AAAA9x55r9A/kvcr2p7K8Wg/xvwoJWehBTQ?cls=10`), it was confirmed on **2026-02-27** that the 3PL integration is **not required for the launch**.
*   **Initial Scope Definition:** The original description outlined features including pushing order details (Name, Address, Contact No) to the vendor app at a specific stage (order placement vs. packed status), live tracking visibility outside the FPG app, and Proof of Delivery recording.

**Pending Actions & Ownership**
*   **Action:** Update ticket documentation or close the "Idea" given the scope removal for launch.
*   **Owner:** Rajesh Dobariya (Assignee).
*   **Context:** While the specific integration is off for launch, the ticket remains in "To Do" status with no formal resolution yet filed to reflect this decision.

**Key Dates & Deadlines**
*   **Original Plan:** Add delivery ticket in the week starting **2026-03-23**.
*   **Decision Date:** 2026-02-27 (Integration confirmed as not required for launch).

**Blockers/Notes**
*   No technical blockers exist; the feature was deprioritized based on business requirements.
*   Previous planning questions regarding notification timing, data fields, and DBP notifications remain unaddressed due to scope cancellation.


## jira/OMNI-1423: [1HD] Pilot to customer launch readiness
Source: jira | Key: OMNI-1423 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Prajney Sribhashyam | polaris-work-item-link: DPD-406
### Daily Briefing: OMNI-1423 [1HD] Pilot to Customer Launch Readiness

**Current Status**
*   **Status:** In Development (In Progress).
*   **Date/Time Reference:** Current update as of 2026-03-11.
*   **Progress:** First round of User Acceptance Testing (UAT) was completed on **March 10, 2026**. The team is currently addressing bugs discovered during this UAT cycle.

**Pending Actions & Ownership**
*   **Owner:** Rajesh Dobariya.
*   **Action Items:**
    *   Investigate root causes for defects identified in the March 10 UAT round.
    *   Provide updated Estimated Time of Arrival (ETA) for resolving new items by **today, March 11, 2026, EOD**.

**Key Decisions Made**
*   **Scope Splitting:** On **February 20, 2026**, a decision was made to align with business stakeholders on MVP "must-haves" and split the delivery ticket into two phases (now vs. later).
*   **Item Movement:** On **February 27, 2026**, Rajesh Dobariya moved non-blocker items to a new epic to streamline the current focus.

**Key Dates, Deadlines & Blockers**
*   **Upcoming Deadline:** ETA update required by EOD on March 11, 2026.
*   **Completed Milestone:** UAT Round 1 (March 10, 2026).
*   **Blocker/Dependency:** Active investigation into the root cause of UAT bugs is currently delaying further progress.

**Technical & Contextual References**
*   **Linked Issue:** DPD-406 (Polaris work item link).
*   **Project Goal:** Enable seamless express delivery (discover, add to cart, checkout, receive) for shoppers; ensure picking within SLA for pickers; and ensure accurate financial attribution for business managers.
*   **Metrics Targets:** Product metrics aim to increase AOV from $X to $Y within 6 weeks and Perfect Order rate from X% to Y% in 3 months.
*   **Priority:** High.


## jira/OMNI-1414: Integrate personalized gamification challenge with FP app
Source: jira | Key: OMNI-1414 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: James Huang | polaris-work-item-link: DPD-297
**Jira Briefing: OMNI-1414 – Integrate Personalized Gamification Challenge with FP App**

**Current Status**
*   **Status:** In Development.
*   **Assignee:** Rajesh Dobariya (confirmed as of March 6).
*   **Type:** Idea / High Priority.
*   **Linked Issue:** DPD-297.
*   **Progress:** Backend (BE) work commenced as of March 11.

**Key Decisions & Requirements**
*   **Technical Architecture:** Customer UID must be hashed using `sha256 + salt ('s@veValue!')` before passing to the webview URL (Decision by Alvin Choo, Jan 30).
*   **Data Prerequisite:** The App team requires a mapping file of customer UID to personalized challenge page URLs. Target delivery for this data is the **1st week of February** (per James Huang, Jan 16); however, BE work started March 11 pending final alignment.
*   **Effort Estimate:** 3 man-weeks total (2 weeks Frontend across platforms + 1 week Backend) confirmed by Rajesh on March 6.

**Pending Actions & Ownership**
*   **Technical Alignment:** Finalize technical approach and confirm data mapping readiness by **Feb 20** (Rajesh Dobariya, Jan 19). *Note: Current date is post-January; status update needed on Feb 20 milestone.*
*   **Uplift Data:** Provide more realistic GMV uplift expectations for a 3-6 month MVP timeline to aid prioritization. Rajesh requested this on Jan 27; James provided the $8M long-term projection on Jan 24 but did not specify the immediate MVP figure (James Huang).
*   **Stakeholder Communication:** Communicate the final delivery date to the CCO team for launch planning (Rajesh Dobariya, March 6).

**Key Dates & Timeline**
*   **Tentative Launch:** March 2026 (James Huang, Jan 16). *Note: Initial comment suggested "after CNY," later refined to March.*
*   **Data Handover Target:** 1st week of February (James Huang, Jan 16).
*   **Technical Alignment Deadline:** Feb 20 (Rajesh Dobariya, Jan 19).
*   **BE Start Date:** March 11 (Rajesh Dobariya).

**Business Context & Impact**
*   **Goal:** Integrate "UntieNot" personalized gamification for 1.8M DCC customers to drive sales and engagement.
*   **Impact Estimate:** Projected $8M incremental GMV over 8 months (scaled from $395K/month pilot).
*   **Touchpoints Requiring Changes:** Split PNW banner on OMNI HP, PNW Banner in Rewards page, OMNI Popup, OMNI Homepage Banner, Voucher Wallet Banner, and Rewards Tile.

**Blockers/Notes**
*   Discrepancy between the stated "1st week of Feb" data delivery target and the March 11 BE start date requires clarification to ensure no delays occur due to missing mapping files.


## jira/OMNI-1418: Overage on transaction sync from Segment to OSMOS
Source: jira | Key: OMNI-1418 | Status: UAT (In Progress) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-644, DPD-644
**Jira Brief: OMNI-1418 – Overage on Transaction Sync (Segment to OSMOS)**

**Current Status**
*   **State:** UAT (In Progress).
*   **Priority:** High.
*   **Assignee/Reporter:** Nikhil Grover.
*   **Type:** Idea.
*   **Linked Issue:** DPD-644.

**Problem & Impact**
The current implementation of the transaction sync function from Segment to OSMOS causes usage overage, costing the organization **$4k per month**. Transactions are synced to attribute GMV to OSMOS campaigns; however, the existing logic is inefficient. The goal is to streamline this sync function to eliminate these costs.

**Key Dates & Deadlines**
*   **Timeline Alignment:** Resource availability and timeline alignment occurred on **2026-02-19**.
*   **UAT Completion ETA:** **2026-03-11**.
*   **Deployment:** As this is a backend-only change, no change management or additional workflows are required to deploy to production.

**Actions Pending & Ownership**
*   **Owner:** Nikhil Grover.
*   **Pending Action:** Complete UAT testing and deployment by the ETA of March 11.
*   **Status Check:** Work is currently in the final stage (UAT) following resource alignment.

**Decisions Made**
*   Confirmed that the initiative addresses a financial cost avoidance of $4k/month.
*   Determined that the solution is backend-only, requiring no external vendor alignments, budget approvals for launch, or user communication tactics.

**Blockers & Dependencies**
*   No active blockers identified in the latest update (2026-03-11).
*   The ticket references a "Solution Summary" marked as TBC in the original description; however, progress to UAT implies a technical solution has been defined and is now being validated.

**Summary for Daily Briefing**
Nikhil Grover is leading the finalization of OMNI-1418 to resolve a $4k/month cost overage in Segment-to-OSMOS transaction syncing. The work, linked to DPD-644, has moved from resource alignment (Feb 19) into UAT. Testing is scheduled for completion on March 11. Upon successful UAT, the backend change will be deployed immediately with no additional operational overhead required.


## jira/OMNI-1420: Enable all 3P domain links to open in the in-app browser from banner redirection
Source: jira | Key: OMNI-1420 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-372
**Jira Ticket Briefing: OMNI-1420**

**Current Status**
*   **State:** In Development (In Progress).
*   **Assignee:** Nikhil Grover.
*   **Priority:** High.
*   **Linked Issue:** DPD-372 (Polaris work item link).
*   **Context:** The initiative aims to enable non-endemic 3rd party campaign links to open in the in-app browser via banner redirection, eliminating the need for app updates required by current whitelisting processes. This reduces lead time from up to 4 weeks to near real-time.

**Key Decisions Made**
*   **Security Constraint:** Cybersecurity advised against removing whitelisting entirely due to other internal use cases.
*   **Solution Architecture:** Aligned on a backoffice/backend-managed solution (hosting whitelisted domain names) rather than "removing" whitelisting or using the "Split" flagging/experimental platform (per Winson Lim's intervention).
*   **Resource Strategy:** Despite Accenture requiring a 7-8 week commitment for external resources, the business aligned to utilize internal resources to maintain the original timeline.
*   **Effort Estimate:** Validated at 2 man weeks total (1 week per platform).

**Pending Actions & Ownership**
*   **Resource Augmentation Confirmation:** Awaiting final confirmation from the business regarding resource allocation. Owner: Nikhil Grover (as of March 19 update).
*   **Frontend Development Start:** Work is scheduled to commence after the "UntieNots" initiative is completed.
    *   **Target Start Date:** Second half of the week of **March 16**.
    *   **Owner:** Nikhil Grover (Assignee).

**Timeline & Blockers**
*   **Critical Deadline/ETA:** Frontend work starts second half of the week of March 16.
*   **Blocker/Dependency:** Progress is gated on the completion of the "UntieNots" project.
*   **Historical Context:**
    *   *Jan 29:* Initial proposal with 4-week lead time problem definition.
    *   *Feb 11:* Cybersecurity feedback received; solution pivoted to backoffice management.
    *   *Feb 12:* ROI updated by Sathya Murthy Karthik; Split platform usage rejected by Winson Lim.
    *   *Feb 13:* Assignee confirmed as Nikhil Grover.

**Business & Product Impact**
*   **Goal:** Close deals and launch campaigns with minimal lead time for the RMN BD team.
*   **Financial Impact:** Potential to generate up to **$500K** in annual GMV from lead generation and non-endemic campaigns.
*   **Metric Targets:** Expected AOV increase and Perfect Order improvement within 6 weeks to 3 months respectively (specific X/Y figures pending final definition).


## jira/OMNI-1429: Activate product ads on all Omni homepage swimlanes
Source: jira | Key: OMNI-1429 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-710
**Daily Briefing: OMNI-1429 – Activate Product Ads on Omni Homepage Swimlanes**

**Current Status**
*   **State:** In Development (In Progress).
*   **Priority:** High.
*   **Type:** Idea.
*   **Assigned To:** Nikhil Grover (also Reporter).
*   **Related Work Item:** DPD-710 (Polaris work item link).

**Pending Actions & Ownership**
*   **Implementation:** Nikhil Grover is currently developing the feature to configure product ad slots via Split.
*   **Technical Scope:** The team must implement logic to set ad slots in Split, fetch ads based on configured slot counts, and sequence products for the frontend. This change requires no new app deployment.
*   **Target Slots:** Ads will be activated in slots 3, 5, and 7 across all Omni home swimlanes and Vertical Scroll (previously limited to slots 1 and 3 only within the Past Purchase swimlane).

**Key Decisions Made**
*   **Strategic Shift:** To maximize monetization while keeping highly relevant products in the top two slots (1 & 2), ads will be pushed to lower-visibility positions (3, 5, and 7) across all swimlanes.
*   **Configurability:** The solution enables the RMN Product Manager to test different placements via Split rather than hard-coding, supporting future planning for Project Light.

**Key Dates & Deadlines**
*   **No Hard Deadline:** The ticket currently has no due date set.
*   **Impact Timeline:** Based on a 5-month rollout window post-launch, expected incremental revenue is projected at $312K (part of a larger $750K p.a. goal).

**Blockers & Dependencies**
*   **Dependencies:** None identified; operational processes and business rules remain unchanged ("No change").
*   **Effort Estimate:** 3-4 man days.
*   **Status Check:** No blockers currently reported; work is actively progressing in development.


## jira/OMNI-1421: Transition from fixed-tenancy to impressions-based banner delivery model
Source: jira | Key: OMNI-1421 | Status: Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-385
**Ticket:** OMNI-1421 | **Priority:** High | **Type:** Idea | **Assignee/Reporter:** Nikhil Grover | **Status:** Prioritised (To Do)

### Current Status
The project to transition from a fixed-tenancy model to an impressions-based banner delivery model is in the "Prioritised" phase. The assignee, Nikhil Grover, is currently finalizing the solution design. This initiative is contingent on the completion of **OMNI-1429** (activation of product ads on Omni homepage swimlanes).

### Pending Actions & Ownership
*   **Solution Finalization:** Nikhil Grover must complete the technical and logical definition of the new model.
    *   **Target Completion:** By March 31, 2026.
*   **Operational Alignment:** Ad Ops and Platform Ops must align on Standard Operating Procedures (SOP) for the new impressions-based model.
*   **Go-to-Market Preparation:** Update RMN packages to reflect the transition to the impressions-based model, targeting a start date of April 1, 2026.

### Key Decisions & Business Logic
*   **Problem Statement:** The current fixed-slot approach wastes inventory by showing irrelevant content repeatedly and limits sales slots for the RMN team.
*   **Strategic Shift:** Transitioning 70% of package budgets to Product Ads (impressions-based) aims to increase traffic efficiency through frequency capping and personalization.
*   **Financial Impact:** Projected annual incremental revenue of **$900k** (based on $1.49M potential and a 60% sell-through rate). This assumes moving from a ~60% package fill rate to utilizing freed-up inventory at $10 CPM.
*   **Dependencies:** Linked to Polaris work item **DPD-385**.

### Key Dates & Deadlines
*   **Feb 27, 2026:** Original target for solution finalization (updated).
*   **March 31, 2026:** Revised ETA for completion of OMNI-1421.
*   **April 1, 2026:** Target start date for the new model implementation.
*   **Blocker:** The project cannot commence until **OMNI-1429** is activated.

### Success Metrics (Target)
*   **Financial:** AOV increase within 6 weeks.
*   **Customer Experience:** Perfect Order rate increase within 3 months.


## jira/OMNI-1416: FP Pay experience improvements to support new auto apply voucher at IPOS/KPOS 
Source: jira | Key: OMNI-1416 | Status: Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Rajesh Dobariya
**Jira Ticket Summary: OMNI-1416**
**Title:** FP Pay experience improvements to support new auto apply voucher at IPOS/KPOS
**Status:** Prioritised (To Do) | **Priority:** High | **Assignee:** Rajesh Dobariya

**Current State**
The initiative aims to resolve compliance risks and UX friction by shifting offer redemption authority from the Offer Service to POS systems (IPOS, KPOS). FP Pay will transition from an execution layer to a "discovery surface" only.
*   **Architecture Shift:** Digital Center becomes the Single Source of Truth for offers. IPOS will fetch eligible offers in real-time and auto-apply them during checkout.
*   **Progress:** Backend (BE) work to enable voucher selection configuration is complete under an existing Core Product Roadmap epic and is ready for release.

**Pending Actions & Ownership**
1.  **FS Team Alignment:** Rajesh Dobariya must follow up with the FS team regarding their timeline to finalize the FP Pay experience and provide final effort estimation (Action: [2026-02-12]).
2.  **Executive Alignment:** Share and align the new FP Pay experience (RB & Kopitiam) with Koklin and Qiuyan for the App Exco review (Action: [2026-02-19]).
3.  **Effort Estimation:** Provide specific effort estimates for remaining work, specifically the DSP integration required to fetch vouchers in "browse-only" mode before launch (Action: [2026-02-19], [2026-03-11]).
4.  **IPOS Coordination:** Align with IPOS on when they will start fetching applicable vouchers based on user profiles from DSP to configure FP Pay accordingly.

**Decisions & Technical Constraints**
*   **Interim Phase (July – Sep 2026):** Offer Service continues handling Bank vouchers and EVs; IPOS handles other in-store offers. FP Pay acts as browse-only for these interim offers.
*   **End State (Sep 2026+):** Offer Service is decommissioned. POS becomes the single redemption engine for all voucher types (including GC 2.0).
*   **Dependency:** App adoption depends on BE completion of DSP integration to fetch vouchers, required before the July launch.

**Key Dates & Deadlines**
*   **Target Launch Window:** July – September 2026.
*   **Production Go-Live:** Deadline undefined; clarification requested from Sathya Murthy Karthik ([2026-03-11]) regarding specific go-live dates and requirements.

**Blockers**
*   Pending confirmation on production timeline from stakeholders.
*   Dependent on IPOS integration readiness to fetch vouchers from DSP.


## jira/OMNI-1419: [Shopbeyond] - Capture all scan events coming from scanning Shop beyond QR code.
Source: jira | Key: OMNI-1419 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Rajesh Dobariya
**Daily Briefing Summary: OMNI-1419 [Shopbeyond] Scan Event Capture**

**Current Status**
*   **State:** Soft Prioritised (To Do).
*   **Type:** Idea.
*   **Assignee:** Rajesh Dobariya.
*   **Context:** The ticket addresses a critical gap where GMV attribution for Shopbeyond is currently inaccurate due to reliance on generic GA events with keyword-based page paths instead of dedicated scan events.

**Key Decisions Made**
1.  **Priority Realignment (2026-03-16):** Rajesh Dobariya aligned with Jasper that the **1HD launch takes precedence** over Shopbeyond tracking.
    *   *Rationale:* Prioritizing Shopbeyond would delay the 1HD launch by approximately 3–4 weeks due to app adoption timelines, despite the tracking effort being only 2–3 days per platform.
2.  **Technical Scope (2026-02-19):** Aligned requirement is to send a single dedicated event for all Shopbeyond QR scans regardless of entry point (internal in-app scanner vs. external mobile camera). This event must include UTM parameters at the event level.

**Pending Actions & Ownership**
*   **Action:** Implement dedicated Segment scan event triggering for both internal and external camera modes, ensuring UTM parameters are captured at the event level.
    *   **Owner:** Rajesh Dobariya (Development Execution).
    *   **Estimated Effort:** 3 days per platform (confirmed by Andin Eswarlal).
*   **Action:** Update dashboards to reflect the new event tracking logic once implemented.
    *   **Owner:** Unspecified in ticket (implied Analytics/BI team).
*   **Action:** Finalize alignment on priority trade-offs between 1HD and Shopbeyond if scope changes again.
    *   **Owner:** Rajesh Dobariya / Jasper.

**Key Dates, Deadlines & Blockers**
*   **Business Logic Rule:** Any DF order placed within 7 days of scanning a Shopbeyond QR code must be attributed to Shopbeyond GMV.
*   **Blocker/Constraint:** No hard deadline exists (Due Date: null). Implementation is currently deprioritized pending the completion of the 1HD launch.
*   **Reference Link:** Alignment discussion recorded at `https://chat.google.com/room/AAAA9x55r9A/kvcr2p7K8Wg/kvcr2p7K8Wg?cls=10`.

**Impact Assessment**
*   **Business Impact:** Accurate GMV attribution for Shopbeyond is currently blocked; current workaround yields inaccurate data.
*   **Product Metrics:** NA.


## jira/OMNI-1300: GST Compliance Phase 2 - Refunds and return
Source: jira | Key: OMNI-1300 | Status: Define (In Progress) | Type: Idea | Priority: High | Assignee: Alvin Choo | Reporter: Sathya Murthy Karthik | Labels: GST | polaris-work-item-link: CORE-51, PAY-6725
**Jira Briefing: OMNI-1300 (GST Compliance Phase 2 - Refunds and Returns)**

**Current Status:** In Progress (Status Category) / Define (Workflow Status). The project is currently in the definition phase, split between a new Replatform initiative for general returns/refunds and an interim RPA solution for BCRS.

**Key Decisions & Strategic Shifts:**
*   **Replatform Strategy:** A decision made on 5 Jan 2026 with the SAP Team confirmed that "Return and Refund" functionality will be fully covered in the upcoming Replatform, not within OMNI-1300's immediate scope.
*   **Interim Solution:** For BCRS specifically, the team will continue the current refund process via RPA while awaiting the Replatform.
*   **RPA Requirements:** On 29 Sept (W39), it was determined that the RPA requires two specific APIs: one for "Refund simulation" to provide customers with pre-confirmation information, and another to verify if an order+SKU has already been refunded.

**Pending Actions & Ownership:**
*   **Aditi Rathi:**
    *   Share the plan of action with Corporate Control (CC) and Ecom Business for alignment.
    *   Coordinate final refund calculation alignment meetings with CC and Business (dates TBD).
    *   Confirm API response specifications with PM/Tech teams.
*   **Stakeholders (CC, Finance, Business):**
    *   Attend pending workshop to align on open items and refund calculations.
    *   Review the first draft of Refund Calculations (completed 27 Nov) for final sign-off.

**Key Dates & Deadlines:**
*   **10 Dec 2025:** Scheduled meeting with RPA team to share API documentation (Status: Confirmed/Ready).
*   **TBD:** Final alignment meetings with Corporate Control and Ecom Business regarding refund calculations.
*   **3 Oct 2025:** Deadline for closing all open comments (historical reference; currently superseded by new timeline).

**Blockers & Risks:**
*   **Stakeholder Alignment:** Previous meetings with CC, Business, and Finance were cancelled on 29 Sept; a workshop was planned for 10 Oct but pending follow-up. Final alignment is required to proceed.
*   **API Readiness:** RPA cannot finalize processing logic until the refund simulation API and confirmation API are documented and agreed upon (Documentation ready as of 9 Dec).

**Linked Issues:** CORE-51, PAY-6725.
**Assignee:** Alvin Choo | **Reporter:** Sathya Murthy Karthik.


## jira/OMNI-1394: [RMN-OFFSITE] - Acquire Customer consent
Source: jira | Key: OMNI-1394 | Status: For Pitching (To Do) | Type: Idea | Priority: High | Assignee: Zi Ying Liow | Reporter: Ravi Goel | polaris-work-item-link: ID-5183
**Jira Briefing: OMNI-1394 [RMN-OFFSITE] - Acquire Customer consent**

**Current Status**
*   **State:** "For Pitching" (Category: To Do).
*   **Priority:** High.
*   **Type:** Idea.
*   **Assignee:** Zi Ying Liow.
*   **Reporter:** Ravi Goel.
*   **Linked Issue:** Polaris work item link ID-5183.
*   **Recent Update (2026-03-11):** Sathya Murthy Karthik flagged that this ticket is **not prioritized** in the new setup and requested further details/updates before a cut-off date was established.

**Key Decisions & Context**
*   **Compliance Risk:** Existing T&Cs do not reflect data sharing with 3rd parties (e.g., Meta), hindering Retail Media use cases like offsite ads, dashboard monetization, and Hashed Data merging.
*   **Scope Changes:** The original scope was expanded on 2026-01-07 to include a customer acknowledgment popup for consent preferences.
*   **Estimated Effort (S):** Total timeline of 3 weeks: 1 week Web + 2 weeks iOS + 2 weeks Android + 3 weeks Backend.

**Pending Actions & Ownership**
1.  **Legal Approval:** Content for the new consent popup must be cleared with Legal (originally estimated mid-Jan, currently pending).
2.  **Requirement Definition:** Owner (Zi Ying Liow) or relevant stakeholders must provide further details to satisfy Sathya Murthy Karthik's request regarding prioritization and status updates.
3.  **Implementation Planning:** Once reprioritized, work involves updating Privacy Notice wording with Legal and adding a "Apps, social media and other digital platforms" opt-in checkbox.

**Key Dates & Blockers**
*   **2026-01-07:** Ticket paused pending CNY and Legal approval for popup content.
*   **2026-02-09:** Effort estimation (3 weeks) documented by Zi Ying Liow.
*   **2026-03-11:** Latest blocker identified: Lack of prioritization in the current setup; Sathya Murthy Karthik has requested updates before a cut-off date.
*   **CNY 2026:** Previously noted as a pause period (now passed).

**Technical References**
*   **New Field:** Label required for identifying opt-in users.
*   **Consent Mechanism:** Checkbox update including "Email, SMS, Telephone calls, Apps/social media/digital platforms."


## jira/OMNI-1235: AI shopping assistant: An engaging experience for customers to build their shopping cart within seconds
Source: jira | Key: OMNI-1235 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Koklin Gan | Reporter: Koklin Gan | polaris-merge-work-item-link: OMNI-1237 | polaris-work-item-link: DPD-293
**Ticket:** OMNI-1235 (AI shopping assistant)  
**Current Status:** Deprioritised to "Next" (Status Category: To Do). Priority remains High.  
**Assignee:** Koklin Gan.

### Key Decisions & Outcomes
*   **Scope Definition:** Recent estimation (Jan 13, 2026) confirmed a "lean" scope: the AI agent can display products but cannot add items directly to the cart; users must navigate to the Product Detail Page (PDP). It supports passing store IDs for search but does not persist conversation context.
*   **Resource Availability:** On Oct 6, 2025, Peter Talbot confirmed design resources are available for a discovery phase.
*   **Technical Direction:** Koklin Gan noted an intention to adopt FPG brand guidelines and align with Trollee AI capabilities (Demo: `https://ai-agent-fpg.trollee.com/chat`).

### Pending Actions & Ownership
*   **Product Requirements (PRD):** Originally due Sept 12, delayed to Sept 18. As of Sept 30, Koklin Gan reported "business use case and prd building in progress." This remains the critical path blocker for development.
*   **Discovery Phase:** Peter Talbot proposed initiating the discovery phase given available design resources on Oct 6, pending a decision to pick up the ticket from its "Next" status.

### Key Dates & Timeline History
*   **Aug 13, 2025:** Meeting with Trollee scheduled to define scope and capabilities.
*   **Sept 9-12, 2025:** Original target dates for business use cases and PRD translation (missed).
*   **Sept 18, 2025:** Revised deadline for PRD readiness (missed).
*   **Sept 30, 2025:** Ticket officially deprioritised to "Next."
*   **Jan 13, 2026:** Latest effort estimation provided by Vivian Lim Yu Qian: 3 weeks design, 3 weeks web (Android only), 2 weeks backend.

### Blockers & Considerations
*   **Complexity:** Sip Khoon Tan flagged "Conceptual Complexity 3" regarding feature discoverability and preventing negative impacts on existing search experiences.
*   **Requirements Clarity:** Peter Talbot previously requested clear business impact metrics, scaling strategy (Omni home vs. PDP), and specific service coverage before prioritization could proceed.
*   **Linked Issues:** Linked to OMNI-1237 (Polaris merge) and DPD-293.

### Metrics & Validation
*   **Goals:** Increase Conversion Rate (CR), Average Order Value (AOV) via up-selling, and customer loyalty.
*   **Current Baseline:** No specific baseline data or expected outcome timeline defined in the ticket yet.


## jira/OMNI-1153: Enable WhatsApp Marketing Consent at Sign-Up Page and Preference Center to Unlock Better Engagement Opportunities
Source: jira | Key: OMNI-1153 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Ravi Goel | Reporter: Yadear Zhang | Labels: app-engagement | polaris-merge-work-item-link: OMNI-1152
**Ticket:** OMNI-1153 (Idea) – Enable WhatsApp Marketing Consent at Sign-Up Page and Preference Center
**Assignee:** Ravi Goel | **Reporter:** Yadear Zhang | **Priority:** High
**Current Status:** In Development (In Progress) / On Hold pending integration scope

**Key Decisions & Strategy Shifts**
*   **Integration Scope Change:** Initial plan to implement consent at sign-up independently has been superseded. The feature will now be consolidated into the broader "CCO" (Customer Concierge/Onboarding) login/signup revamp to avoid duplicate work.
*   **Dependency:** This ticket is officially linked as a requirement within **OMNI-1152** (New Onboarding Scope). Implementation of OMNI-1153 will occur when the onboarding revamp scope in OMNI-1152 is finalized.
*   **Validation:** The business case relies on WhatsApp's 77% open rate (vs. email's 30-40%) and a projected target of collecting ~89,000 consents over 6 months based on 35k monthly sign-ups.

**Pending Actions & Ownership**
*   **Scope Finalization:** Product team must confirm the inclusion of WhatsApp consent in the OMNI-1152 revamp scope. (Status: "Further discussion" noted by Danielle Lee; target to close tomorrow, per March 10 comments).
*   **Impact Analysis:** Koklin Gan is currently gathering impact analysis for prioritization confirmation.
*   **Implementation Planning:** Once consent collection is enabled, **Nghi** is tasked with planning marketing campaigns and defining nudges to drive customer opt-in rates.

**Estimated Timeline & Resources**
*   **Effort Estimate (Flora Wo Ke - March 20):** Backend (2 weeks), iOS (1 week), Android (1 week), Web (1 week). Total estimated engineering effort: ~5 weeks.
*   **Current Date:** Post-June 30, 2025 (Last update confirms direction to OMNI-1152).

**Blockers & Risks**
*   **Technical Uncertainty:** Marked as "1" by Ryne Cheow due to potential conflicts with the CCO login revamp.
*   **Timing Dependency:** Development cannot commence until the broader OMNI-1152 onboarding revamp scope is defined and approved, delaying immediate execution despite the "In Development" status label.

**Summary**
The project aims to unify transactional and marketing consents in Salesforce to leverage WhatsApp for growth. Following technical reviews regarding the CCO login revamp, **OMNI-1153** has been deprioritized as a standalone task and folded into the larger **OMNI-1152** initiative. The next critical milestone is finalizing the OMNI-1152 scope to include this requirement, after which estimated engineering work (5 weeks total) can proceed.


## jira/OMNI-1246: Support the SIT/UAT/Beta/Cut Over for MyInfo and LEAP core system integration
Source: jira | Key: OMNI-1246 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Ryne Cheow | Reporter: James Huang | polaris-merge-work-item-link: OMNI-1169
**Jira Ticket Briefing: OMNI-1246**

**Current Status**
*   **Status:** Backlog (Category: To Do)
*   **Type:** Idea
*   **Priority:** High
*   **Assignee:** Ryne Cheow
*   **Reporter:** James Huang
*   **Related Item:** OMNI-1169

**Pending Actions & Ownership**
Ryne Cheow is responsible for the following pending tasks to support the MyInfo and LEAP core system integration:
*   Collaborate with the LEAP team to finalize plans for SIT, UAT, Beta, and Cut Over phases.
*   Address necessary integrations with LEAP middleware.
*   Execute bug fixes related to the "SG 60" mechanic.
*   Conduct test and validation activities.
*   Develop new onboarding journeys and force update flows (triggered via MyInfo pop-ups).

**Decisions Made**
No final decisions were recorded in this ticket; it currently serves as a high-priority idea requiring further validation before roadmap prioritization. The scope assumes the integration will enable:
1.  SG 60 large family discounts for CHAS status holders with >3 kids.
2.  Fast-track onboarding for FPG using MyInfo.
3.  Profile validation via forced updates.
4.  Zero service disruption during backend CDM/LMS changes.

**Key Dates, Deadlines & Metrics**
*   **Timeline:** No specific due date assigned; an assumed timeline exists but is not detailed in the ticket.
*   **Success Metrics (Current Baseline vs. Target):**
    *   *Customer Data Quality Index:* Increase from 29% to 80% validated profiles.
    *   *Checkout Speed:* Reduce minutes for CHAS large family customers via automated POS discounts.
*   **Target Audience:** CHAS large family customers and new/existing shoppers.

**Blockers/Notes**
*   The ticket is currently in the "Backlog" state, indicating readiness for resource allocation but not yet active development.
*   Success criteria require sufficient validation before moving to the roadmap.


## jira/OMNI-1361: Achieve 100% GST compliance for Ecom orders 
Source: jira | Key: OMNI-1361 | Status: Discovery (To Do) | Type: Idea | Priority: High | Assignee: Alvin Choo | Reporter: Gopalakrishna Dhulipati | polaris-work-item-link: PAY-6785
**Jira Ticket Summary: OMNI-1361 (Achieve 100% GST Compliance for Ecom Orders)**

**Current Status**
*   **State:** Discovery / To Do.
*   **Context:** The project aims to decouple Sales/GST calculation logic from SAP, establishing DBP as the single source of truth to eliminate data discrepancies and ensure IRAS compliance.
*   **Latest Update (06 Jan 2026):** A technical decision was reached during a discussion with the SAP Team on 05 Jan 2026:
    *   **SAP Decoupling:** Will be addressed as part of the broader "replatform" initiative.
    *   **BCRS Deposit:** Will continue using existing SAP posting methods.
    *   **Post-BCRS Deposit:** Orders will be posted to SAP on a monthly basis rather than per order.

**Key Decisions Made**
*   **Posting Strategy:** Confirmed that for BCRS deposits, the legacy SAP posting method persists. Post-deposit, aggregation to monthly posting to SAP is approved.
*   **Replatform Scope:** The full decoupling of business logic (Price, Promo, GST) from SAP is deferred to the replatform project timeline.

**Pending Actions & Ownership**
*   **Action:** Share a formal plan of action with Corporate Control and Ecom Business teams for alignment.
    *   **Owner:** Aditi Rathi (implied based on update frequency and content).
*   **Previous Pending Items (Status Unclear/Resolved by Decision):**
    *   Confirmation of GL Code mapping + Condition Type mapping with the Finance team.
    *   Decision between posting via Comall Connector vs. direct SAP posting (Sophia from Comall was chaser on 27 Nov; specific outcome is not explicitly noted in the latest update, though a new monthly approach was decided).

**Key Dates & Blockers**
*   **06 Jan 2026:** Latest discussion held with SAP Team.
*   **05 Jan 2026:** Decision point regarding BCRS and post-BCRS deposit posting logic.
*   **Blocker/Dependency:** The project is currently waiting on alignment from Corporate Control and Ecom Business teams regarding the new action plan following the decoupling deferral to replatform.

**Technical References & Metadata**
*   **Ticket ID:** OMNI-1361
*   **Linked Issue:** PAY-6785 (Polaris work item link)
*   **Assignee:** Alvin Choo
*   **Reporter:** Gopalakrishna Dhulipati
*   **Priority:** High
*   **Success Criteria:** 100% GST compliance as per IRAS.
*   **System Logic Shift:** DBP to carry Price, Promo, and GST logic; SAP restricted from carrying business/financial logic (subject to replatform scope).


## jira/OMNI-1227: FPG - Fraud detect and prevention 
Source: jira | Key: OMNI-1227 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Aditi Rathi | Reporter: Koklin Gan | discovery---connected: OMNI-1075, OMNI-1134 | polaris-merge-work-item-link: OMNI-1075
**Jira Briefing Summary: OMNI-1227 (FPG - Fraud detect and prevention)**

**Current Status:** Soft Prioritised / To Do. The initiative is stalled awaiting ownership assignment and business alignment on a new fraud engine solution.

**Key Decisions & Progress:**
*   **Scope Definition:** Finalized to exclude "Onboarding journey changes" (OMNI-1227). Focus remains strictly on Order Management touchpoints.
    *   *Note:* Onboarding fixes were addressed via separate releases: Manual Onboarding (5 Nov 2025) and MyInfo Onboarding (24 Nov 2025).
*   **Mitigation Actions Taken:** E-Voucher redemption for Marketplace items was restricted starting Oct 7, 2025 (phased rollout).
*   **Proposed Solution:** A real-time Fraud Engine (ML or Rule-based) integrated with the OMS.
    *   **Logic:** Score transactions as LOW (auto-pass), MEDIUM (flag for review), or HIGH (instant block).
    *   **Backoffice Portal:** Required for CS/Business to approve/reject flags and whitelist customers.
*   **Effort Estimates (High):**
    *   **DS Team:** 8 weeks (building engine/rules).
    *   **DE Team:** TBD (connecting DS-OMS endpoints).
    *   **DPD Fulfilment:** 4 weeks (orchestrating journey & building backoffice; requires 1 BE, 3 FE).
*   **Critical Constraint:** Routing all transactions through the fraud engine impacts Order Placement SLO (latency).

**Pending Actions & Ownership:**
*   **Ownership Transfer:** Danielle Lee flagged on Feb 13, 2026: "Who will be the new owner for this ticket?" Currently unassigned.
*   **Technical Proposal Presentation:** Aditi Rathi targets presenting potential tech options and securing business alignment by **Oct 15** (original target). This remains pending due to lack of active ownership since Dec 2025.
*   **Brainstorming Session:** Aditi planned meetings with DS and Tech teams to finalize the "To-Be" solution; status is unclear given the recent inactivity.

**Key Dates & Blockers:**
*   **Last Update:** Feb 13, 2026 (Danielle Lee requesting owner).
*   **Historical Deadlines Missed:** Oct 15, 2025 (Alignment target); Dec 2, 2025 (Qiuyan Tian requested AOP update).
*   **Blockers:**
    *   Lack of a designated ticket owner since Feb 2026.
    *   Need for explicit business alignment on the proposed high-effort fraud engine vs. current manual processes.
    *   Unresolved SLO impact regarding order placement latency.

**Context:**
*   **Linked Issues:** OMNI-1075 (Discovery), OMNI-1134 (Discovery).
*   **Problem Statement:** High financial/reputational risk from voucher abuse ($100k potential loss) and stolen card usage (~3,200 alerts/year currently processed manually via RPA).
*   **Goal:** Reduce manual review time (currently 2-3 hrs/week per team) and eliminate chargeback risks.


## jira/OMNI-1208: Mirakl foundational work for scalability
Source: jira | Key: OMNI-1208 | Status: Discovery (To Do) | Type: Idea | Priority: High | Assignee: Koklin Gan | Reporter: Koklin Gan | blocks: DST-2247 | discovery---connected: OMNI-1178 | polaris-work-item-link: DST-2247, DPD-326, DPD-332, DST-2277, DPD-543, DST-2305
**Ticket:** OMNI-1208 (Mirakl foundational work for scalability)
**Status:** Discovery / To Do (Inception Phase)
**Assignee:** Koklin Gan

**Current State & Decision**
The ticket is being closed ("To kill this epic") to remove parent visibility, as the scope is now covered by connected child tasks. The original high-priority idea focused on resolving critical financial discrepancies in the Mirakl marketplace ecosystem (incorrect billing, catalogue accuracy, offer integrity) that forced manual workarounds and eroded seller trust.

**Key Dependencies & Linked Issues**
*   **Connected:** OMNI-1178
*   **Blocked By / Blocks:** DST-2247
*   **Polaris Links:** DPD-326, DPD-332, DST-2277, DPD-543, DST-2305

**Timeline & Effort Estimates**
*   **Initial Estimate (Mar 18):** Alvin Choo estimated 12 weeks for two backend engineers.
*   **Revised Estimate (Mar 23):** Gopalakrishna Dhulipati revised to 40 weeks total (2 BE x 20 weeks).
*   **Voucher Logic Update (Apr 7):** Alvin Choo updated the estimate for "Vouchers created in DBP calculated into Mirakl" to 4 weeks if Option 1 is selected.

**Pending Actions & Owners**
*   **User Stories:** Fiona U noted on Apr 2 that user stories from **KL** and **Aditi** were pending completion, with a target of the following two weeks. As the ticket was closed on Apr 30 without confirmed delivery dates, these stories remain critical for the underlying work.
*   **Complexity Validation:** Koklin Gan repeatedly requested complexity estimates between Mar 6 and Mar 12 to support prioritization.

**Key Dates & Blockers**
*   **Mar 5:** Ticket created with "High" priority.
*   **Apr 4:** Status update flagged pending user stories.
*   **Apr 30:** Final action by Koklin Gan closed the ticket, indicating the initiative is being managed via its connected child items rather than this parent epic.

**Technical Scope (Original)**
The work aimed to establish Mirakl as the single source of truth for billing and sales orders, including:
1.  Migrating CWF leftovers and CF transporter apps to Mirakl/DBP.
2.  Decoupling from SAP/CF and handling refunds/cancellations/vouchers in upstream systems.
3.  Enabling white-label invoices sent directly to consumers under the seller entity.
4.  Assessing scalability of the Mirakl <> DBP <> SAP architecture.


## jira/OMNI-1242: [Pre-order] 'Mark as Paid' for In-Store Preorders
Source: jira | Key: OMNI-1242 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Fiona U | Labels: Preorder | polaris-work-item-link: PA-330
**Jira Ticket Summary: OMNI-1242**

**Current Status**
*   **Status:** Backlog (To Do) / Idea
*   **Priority:** High
*   **Assignee:** Rajesh Dobariya
*   **Reporter:** Fiona U
*   **Linked Issue:** PA-330

**Decision Made**
On **2026-01-15**, Prajney Sribhashyam determined this feature is no longer required for immediate implementation. The ticket was marked for deletion as the functionality ("Mark as Paid" automation) will be covered during the upcoming **re-platform**. This decision supersedes previous technical designs involving a PubSub integration between the POS system and DBP (Decided on **2025-10-22**).

**Key Dates & Timeline**
*   **Idea Created:** 2025-04-30 (Fiona U)
*   **Discovery/Clarification:** 2025-06-24 (Danielle Lee noted effort <10 days pending POS file; Qiuyan Tian requested pitch slides on 2025-07-02).
*   **POS Integration Plan Drafted:** ETA 4 Aug (2025-07-27, Prajney Sribhashyam) – Pending POS team dependency.
*   **Technical Approach Defined:** 2025-10-22 – Proposed two-step automation: (1) POS publishes to PubSub; (2) DBP reads and updates orders.
*   **Final Resolution:** 2026-01-15 – Feature deprioritized for re-platform.

**Pending Actions & Ownership**
*   **Action:** None pending on this specific ticket due to the "delete/covers by re-platform" decision.
*   **Ownership Transition:** On **2025-07-03**, Ravi Goel looped in a new owner (name redacted in log) to manage this post-checkout topic, but subsequent updates remained with Prajney Sribhashyam until the final cancellation.

**Blockers & Dependencies**
*   **Technical Dependency:** Prior to cancellation, implementation relied on the POS team providing a specific PubSub topic for payment data (Identified 2025-10-22).
*   **Information Gap:** Early discussions highlighted missing details regarding manual transaction ID/amount entry sources and lack of pitch slides (Danielle Lee, Qiuyan Tian - June/July 2025).

**Impact Metrics (If Implemented)**
*   **Goal:** Increase Perfect Order %, reduce CS incidents regarding unpaid/cancelled pre-orders, and improve DOT %.
*   **Risk Mitigation:** Avoided $11.96k GMV loss observed in the previous Christmas campaign due to 146 unpaid orders not flowing into bulk PO flows (Data cited by Fiona U on 2025-05-29).


## jira/OMNI-1282: Automate advertiser invoicing via OSMOS
Source: jira | Key: OMNI-1282 | Status: Define (In Progress) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-296
**Ticket Summary: OMNI-1282 (Automate advertiser invoicing via OSMOS)**

**Current Status**
*   **State:** Define (In Progress).
*   **Priority:** High.
*   **Owner/Assignee:** Nikhil Grover.
*   **Context:** Linked to Polaris work item **DPD-296**. The ticket is currently **not prioritized** for immediate execution despite high priority classification.

**Key Decisions & Validation**
*   **Business Alignment:** On Tuesday, January 27, 2026, a change in the billing process was aligned between RMN, Finance, and AR.
*   **Solution Review:** The proposed solution design has been reviewed with business stakeholders.
*   **Stakeholder Query:** Alvin Choo queried on March 13, 2026, regarding prioritization status given the "Define" state.
*   **Final Decision (March 16, 2026):** Nikhil Grover confirmed the initiative is de-prioritized pending further alignment.

**Pending Actions & Ownership**
*   **Primary Blocker:** Pending final alignment with the **Finance team**. While initial process changes were agreed upon with RMN and AR, Finance alignment remains outstanding.
*   **Next Steps:** Once Finance alignment is secured, requirements will be finalized for solution complexity assessment and design (originally targeted ETA February 6, 2026).

**Timeline & Dates**
*   **Jan 15, 2026:** Nikhil Grover noted finalizing solution design for effort estimation.
*   **Jan 27, 2026:** Billing process change aligned between RMN, Finance, and AR.
*   **Feb 6, 2026 (Target):** Original ETA for finalizing requirements for complexity assessment/design.
*   **March 13, 2026:** Status query raised by Alvin Choo.
*   **March 16, 2026:** Confirmation of de-prioritization status provided.

**Summary**
The initiative to automate advertiser invoicing via OSMOS (OMNI-1282) is stalled in the "Define" phase. Although process alignment occurred on January 27, 2026, and a solution review was completed, the project is currently on hold due to pending final approval from the Finance team. No new dates have been set for resumption.


## jira/OMNI-1334: Optimising Airway Bill Generation Experience for Seller
Source: jira | Key: OMNI-1334 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Prajney Sribhashyam
**Daily Briefing Summary: OMNI-1334**

**Current Status:**
The ticket **OMNI-1334** ("Optimising Airway Bill Generation Experience for Seller") is currently in the **Backlog** status with **To Do** categorization. The issue type is an **Idea** and was assigned to **Prajney Sribhashyam**.

**Decisions Made:**
*   **Board Reallocation (2025-07-22):** Following a query from **Koklin Gan** regarding team ownership, **Prajney Sribhashyam** confirmed the initiative falls exclusively within the Seller team's scope. Consequently, the ticket was moved to the **Seller Experience board**, and Prajney intended to repurpose this specific ticket for another initiative.
*   **Architectural Decision (2026-01-15):** **Prajney Sribhashyam** determined that the functionality described in OMNI-1334 would be covered by a broader "re-platform" effort rather than being built as a standalone feature. The decision was made to mark the ticket for deletion.

**Pending Actions:**
*   **Ticket Retraction:** No active development actions are pending; the instruction from 2026 is to delete the ticket since the scope will be absorbed by the re-platform initiative.
*   **Ownership:** **Prajney Sribhashyam** remains the assignee and reporter responsible for executing the deletion/archival process.

**Key Dates & Timeline:**
*   **Initial Creation/Post:** 2025-07-15 (Idea defined).
*   **Scope Clarification:** 2025-07-21 (Query raised by Koklin Gan).
*   **Board Move Decision:** 2025-07-22.
*   **Final Disposition:** 2026-01-15 (Decision to delete/defer to re-platform).

**Blockers & Context:**
*   **Original Problem:** Sellers were unable to generate Airway Bills without triggering a carrier pickup, leading to fulfillment errors and delivery issues. The current system lacks multi-generation capability for misplaced documents.
*   **Strategic Blocker:** The solution is no longer being pursued as an independent initiative due to the imminent "re-platform" strategy, rendering this specific backlog item obsolete.

**Technical/Metadata References:**
*   **Ticket ID:** OMNI-1334
*   **Priority:** High
*   **Components/Labels/Fix Versions:** None specified.


## jira/OMNI-1234: [MP Foundational] White label invoice generation for MP 
Source: jira | Key: OMNI-1234 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Koklin Gan | Reporter: Koklin Gan | polaris-work-item-link: DPD-543
**Daily Briefing Summary: OMNI-1234 (White Label Invoice Generation for MP)**

**Current Status & State**
*   **Ticket Status:** Backlog (To Do); Issue Type: Idea.
*   **Priority:** High.
*   **Assignee/Reporter:** Koklin Gan.
*   **Progression:** The item has moved from initial definition to product discovery and recent alignment with Finance. It is currently in a "discussing/approval pending" phase.

**Key Decisions & Strategic Shifts**
*   **Scope Re-evaluation (2025-09-17):** Prajney Sribhashyam noted that unless required for B2B, the feature is not critical for B2C and could potentially be deferred to a future replatforming.
*   **B2B Alignment Needed (2025-09-19):** Ying Ying Ting flagged an immediate dependency on the B2B platform timeline. If white-label invoices are needed for B2B, MP invoicing is proposed as an alternative if not aligned by a specific date.
*   **Approach Confirmation (2025-09-24):** Finalizing the approach with a target definition date of **7 Nov 2025**.

**Pending Actions & Ownership**
1.  **Finance Compliance Approval:** Pending approval from Finance regarding compliance standards and GST requirements.
    *   *Owner:* Prajney Sribhashyam (Discussion initiated 2025-10-22).
2.  **Target Timeline Confirmation:** Finalizing the release date post-Finance alignment to ensure B2B platform synchronization.
    *   *Owner:* Prajney Sribhashyam / Ying Ying Ting.
3.  **Release Date Input:** Initial request for an estimated release date (logged by Fiona U on 2025-04-29).

**Key Dates & Deadlines**
*   **7 Nov 2025:** Target date to finalize the approach and define specific dates.
*   **17 Sep 2025:** Scheduled for "Final alignment" (Context: B2B vs. B2C prioritization discussion).

**Technical Context & Blockers**
*   **Core Problem:** Current invoices are branded under FairPrice (FP) even for seller-fulfilled orders, causing brand confusion and misrepresentation. The goal is to enable white-labeling where the Seller is the issuing entity.
*   **Solution Options Discussed:**
    *   *Option 1:* Generate on DBP (Requires GST compliance, data flow of seller info/logo).
    *   *Option 2:* Generate on Mirakl (Requires GST compliance, streamlining sales data flow).
*   **Primary Blocker:** GST compliance completion and Finance approval are prerequisites for either solution path.
*   **Linked Issues:** Polaris work item link **DPD-543**.

**Summary of Immediate Next Steps**
Await outcome of Finance discussion led by Prajney Sribhashyam regarding GST/compliance standards to confirm if the 7 Nov target date remains viable and how it aligns with the B2B platform launch.


## jira/OMNI-1250: Customer Account Merging & Deduplication via LEAP middleware
Source: jira | Key: OMNI-1250 | Status: Discovery (To Do) | Type: Idea | Priority: High | Assignee: Ryne Cheow | Reporter: James Huang | polaris-work-item-link: CPR-86
**Ticket Summary: OMNI-1250 (Customer Account Merging & Deduplication via LEAP)**

**Current Status**
*   **Status:** Discovery (To Do) | **Priority:** High | **Assignee:** Ryne Cheow
*   **Context:** The project aims to resolve 1.5M+ duplicate customer records (reducing active records from 3.6M to 2.1M within 12 months) by implementing an in-app merge flow via the LEAP middleware.
*   **Latest Update (2026-02-09):** Confirmed that no urgent features are required for the *current* app version.

**Key Decisions & Strategic Shifts**
*   **Launch Timeline:** Aligned with James Huang on 2025-06-13; merging is **not** included in the LEAP September launch. Execution will begin only after the new system stabilizes.
*   **Scope Refinement (2025-08-20):** Ravi Goel proposed splitting the scope into two distinct tracks:
    1.  *New-New Customers:* Handling matches based on Singpass and parameters already in scope.
    2.  *Existing Customers:* Requires testing creative impact methods and re-prioritization.
*   **Implementation Path (2026-02-09):** Vera Wijaya confirmed the account merge journey will be included specifically in **"Project Light"** (the new app) to secure customer consent, rather than as a backend-only solution.

**Pending Actions & Ownership**
*   **Prioritization Review:** The team must review and prioritize the "Existing Customers" merge approach as suggested by Ravi Goel.
    *   *Owner:* Ryne Cheow (implied via assignee role) / Product Team.
*   **"Project Light" Integration:** Ensure the consent-to-merge journey is engineered into the new app build for Project Light.
    *   *Reference:* Linked to Polaris item **CPR-86**.

**Key Dates & Deadlines**
*   **2025-09 (September):** Targeted launch of LEAP; merge functionality explicitly excluded from this date.
*   **Post-Stabilization:** Merge operations for existing customers may commence after new system stabilization (date TBD).
*   **12-Month Goal:** Full launch impact expected to reduce active records to 2.1M.

**Technical & Operational Context**
*   **Middleware:** LEAP middleware is assumed capable of handling complex match-and-merge logic at scale.
*   **Data Baseline:** 3.6M active records currently, driven by fragmented sign-ups (email vs. phone).
*   **Dependencies:** Project Light development and the production cutover to the new Customer Data Model (CDM) are prerequisites for execution.


## jira/OMNI-1157: Adopting the CDM Golden Record in the FPG App (and Phase out FPOn ID)
Source: jira | Key: OMNI-1157 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Ryne Cheow | Reporter: James Huang | Labels: Q2-2025, new_LMS | polaris-merge-work-item-link: OMNI-1174 | polaris-work-item-link: DPD-544
**Jira Ticket Summary: OMNI-1157**

**Current Status:**
Backlog (To Do). This is a High Priority **Idea** ticket reported by **James Huang** and assigned to **Ryne Cheow**. It is linked to Polaris work item **DPD-544** and merge item **OMNI-1174**. The initiative aims to adopt the CDM Golden Record in the FPG App, phase out legacy IDs (Linkpass, FPOn), and unify data across ~4.28M active users.

**Key Actions & Ownership:**
*   **Technical Strategy:** Implement 6 user stories covering platform core updates, profile synchronization, analytics SDK integration, QR code refactoring, Salesforce Marketing Cloud (SFMC) SDK updates, and legacy ID deprecation.
*   **Effort Estimation:** Multiple tribes have submitted estimates for the "Engage" area:
    *   **Ryne Cheow:** 2 BE x 4 weeks + 2 Mobile x 2 weeks = 12 manweeks.
    *   **Alvin Choo:** 2 BE x 5 weeks each (Cart and Offers).
    *   **Gopalakrishna Dhulipati:** 1 BE x 2 weeks + 2 Mobile x 1 week + 1 Web x 1 week = 5 weeks.
    *   **Ram Datchnamoorthy:** 1 BE x 4 weeks.
*   **Validation:** Work aligns with the "Project LEAP Architectural Blueprint." Assumptions confirm the foundational CDM platform and LEAP Middleware APIs are stable/available.

**Decisions Made:**
No formal approval decision recorded yet; the ticket remains in the backlog pending resource allocation and scheduling confirmation based on the submitted estimates.

**Key Dates, Deadlines & Blockers:**
*   **Timeline Target:** Goal is to increase CDM UID Adoption Rate from 0% to 100% by **Q2 2026**.
*   **Critical Query (Blocker/Risk):** On **May 6**, **Fiona U** flagged that the current estimated timeline indicates a potential spillover into **Q3**, contradicting the Q2-2025 label and potentially impacting the Q2 2026 delivery target.
*   **Labels:** Q2-2025, new_LMS.

**Summary:**
The project requires consensus on total estimated effort versus the Q2 2026 deadline. The discrepancy noted by Fiona U regarding a potential schedule shift to Q3 must be resolved before moving from Backlog to active execution.


## jira/OMNI-1389: [POC] Enabling PalmPay to allow quick checkout
Source: jira | Key: OMNI-1389 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Sathya Murthy Karthik | Reporter: Koklin Gan
**Daily Briefing Summary: OMNI-1389**

*   **Current Status:** The ticket is in the **Backlog** state with a status category of **To Do**. It is classified as an **Idea** type.
*   **Ownership & Pending Actions:** The item is assigned to **Sathya Murthy Karthik**, who owns the next steps. No specific technical tasks or development actions have been logged yet; the ticket remains in a pre-implementation planning phase.
*   **Decisions Made:** There are no recorded decisions, discussions, or resolutions within the chronological log. The entry consists solely of the initial creation and metadata assignment.
*   **Key Dates & Blockers:**
    *   **Priority:** High.
    *   **Created/Logged Date:** 2025-10-13 (Entry timestamp: 16:38:10 UTC+08).
    *   **Deadline:** None set (Duedate is null).
    *   **Blockers:** None identified in the current log.

**Summary of Content:**
The initiative, titled "[POC] Enabling PalmPay to allow quick checkout," was reported by **Koklin Gan**. The objective involves a Proof of Concept (POC) to integrate PalmPay support for streamlined checkout processes. As of the last update on 2025-10-13, the ticket has not progressed beyond the backlog stage. No fix versions or components have been assigned, and no labels are currently applied.


## jira/OMNI-1390: Project Turbo to support new POS version
Source: jira | Key: OMNI-1390 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Sathya Murthy Karthik | Reporter: Koklin Gan
**Jira Briefing: OMNI-1390 (Project Turbo POS Support)**

*   **Current Status:** The ticket is in the **Backlog** state (**To Do**). Although classified as an "Idea" with **High** priority, it was formally **archived on 2026-01-29**.
*   **Pending Actions & Ownership:** No immediate actions are pending. The task requires no further development or assignment because the decision was made to cease active work on this specific entry.
    *   **Assignee:** Sathya Murthy Karthik (No longer active on this ticket).
    *   **Reporter:** Koklin Gan (Original author of the idea).
*   **Decisions Made:** On **2026-01-29**, Rajesh Dobariya reviewed the item and determined that the requirement was already sufficiently captured elsewhere. Consequently, the ticket was archived to prevent duplication or unnecessary backlog clutter.
*   **Key Dates & Deadlines:**
    *   **Original Entry:** 2025-10-13 (Title: Project Turbo to support new POS version).
    *   **Archive Date:** 2026-01-29.
    *   **Due Date:** None assigned; the ticket is now closed in terms of active workflow.
*   **Blockers/Notes:** The primary "blocker" was effectively bypassed by the decision to archive, indicating the scope has been either absorbed into another initiative or deemed complete via other means. No technical blockers are listed as the item never progressed beyond the Idea stage.

**Summary for Briefing:**
The high-priority idea **OMNI-1390** regarding "Project Turbo to support new POS version" is currently inactive. Following an initial entry on 2025-10-13 by Koklin Gan, the ticket was archived by Rajesh Dobariya on 2026-01-29. The rationale was that the requirement is already captured; therefore, no further action is required from assignee Sathya Murthy Karthik.


## jira/OMNI-1353: Integrating Tencent's  Biometric Authentication (Palm Pay) solution with FPG App for member verification  
Source: jira | Key: OMNI-1353 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Aditi Rathi | Reporter: Gopal Singh | polaris-work-item-link: ENGM-2474
**Jira Ticket Summary: OMNI-1353 – Tencent Palm Pay Integration (FPG App)**

**Current Status & State**
*   **Status:** To Do / Soft Prioritised.
*   **Issue Type:** Idea.
*   **Assignee:** Aditi Rathi (Original); ownership currently unclear as requested by Danielle Lee on 2026-02-13.
*   **Context:** The project aims to integrate Tencent's Palm Pay biometric authentication into the FPG App for member verification at Punggol Digital District (PDD) Cheers stores. This is a Phase 1 Pilot targeting Oct 2025 rollout. It allows customers to bypass QR scanning by hovering their palm at POS, but does **not** enable direct payment via palm; it verifies membership to trigger existing FPG payment flows.

**Key Decisions & Discussions**
*   **Scope Reduction:** On 2025-10-29, Koklin Gan scoped the work down to "3 stories."
*   **Effort Estimation:** Sip Khoon Tan estimated conceptual complexity of 2 (Low) and effort as "S" size. Ryne Cheow noted that if using CDP for linking/unlinking and reusing existing payment APIs with no POS experience changes, engineering work might be negligible ("no work here").
*   **UX & Linkage Concerns:** Sunny Lim flagged a poor customer experience if account linkage isn't visible in the FPG app (since kiosk screens are used). He requested API specs. Sip Khoon Tan questioned if the Palm Pay flow is customizable to display FPG linkage details or if email notifications are sufficient.
*   **Risk Identified:** Higher adoption of Palm Pay may reduce Weekly Active Users (WAU) for FP Pay users, as transactions move away from the app interface.

**Pending Actions & Ownership**
1.  **Ownership Clarification:** Danielle Lee (2026-02-13) requested confirmation on the new owner and whether work is ongoing or if the ticket should be closed.
2.  **API Specification:** Sunny Lim and Sip Khoon Tan require specific API specs to determine if FPG account linkage visibility can be customized within the Palm Pay flow.
3.  **Estimation Confirmation:** Koklin Gan (2025-11-03) requested final effort estimates after initial discussions; these need finalization before scaling beyond POC.
4.  **Stakeholder Alignment:** Discussion required on how to handle deregistration and linkage visibility given the kiosk-based registration process.

**Key Dates & References**
*   **Target Rollout (POC):** Oct 2025 (Original plan); Pilot in PDD Cheers early Sep 2025.
*   **Linked Issue:** ENGM-2474 (Polaris work item).
*   **Prototype Reference:** Aadil Baggia shared a working Figma file on 2025-11-20.
*   **Critical Review Date:** 2026-02-13 (Status check by Danielle Lee).

**Blockers**
*   Lack of current API specifications for Palm Pay-FPG linkage communication.
*   Uncertainty regarding the customer experience flow for account linking/unlinking on external kiosks vs. the FPG app.


## jira/OMNI-1179: Compliance - Improving the Cart calculation logic 
Source: jira | Key: OMNI-1179 | Status: Paused (To Do) | Type: Idea | Priority: High | Assignee: Alvin Choo | Reporter: Alvin Choo | Labels: Foundation | polaris-work-item-link: CART-54
**Jira Ticket Briefing: OMNI-1179 – Compliance: Improving Cart Calculation Logic**

**Current Status**
*   **State:** Paused (Category: To Do).
*   **Priority:** High.
*   **Assignee/Reporter:** Alvin Choo.
*   **Linked Issues:** CART-54.
*   **Context:** Originally an "Idea" to unify cart logic for GST compliance and cross-channel consistency. Due to upcoming app replatforming, the scope was significantly reduced on 2025-11-27 by Alvin Choo and Aditi Rathi.

**Key Decisions & Scope Changes**
*   **Scope Reduction (2025-11-27):** The epic's scope was narrowed to exclude complex "Sales and drop-off calculations" and focus strictly on:
    1.  CRUD operations for core cart services.
    2.  Basic Cart calculation logic.
*   **Category Shift:** Aditi Rathi (2025-11-27) confirmed the ticket should be moved to the **Platform Health** category given the reduced scope and alignment with the upcoming replatform.

**Pending Actions & Ownership**
*   **GST Calculation Logic Discussion:** Scheduled for **September 26, 2025**, at a GST meeting with CC and Finance (Status update by Aditi Rathi on 2025-09-23). *Note: This date is in the past relative to current progress; pending status remains.*
*   **Sales & Drop-off Calculations:** Identified as "Pending" in updates from August and September 2025. However, these were explicitly carved out during the November scope reduction. The specific ETA for remaining calculation logic is currently undefined ("Pending ETA").
*   **Resourcing Confirmation:** Winson Lim (2025-10-22) raised concerns regarding resourcing constraints and delivery before year-end (Dec). No formal resolution on resource allocation or Dec deadline feasibility has been recorded in the recent comments.

**Key Dates & Blockers**
*   **Last Update:** 2025-11-27 (Scope reduction finalized).
*   **Previous Development Status:** WIP as of Week 38 (Sept 2025) and Week 35 (Aug/Sept 2025).
*   **Blockers:**
    *   Lack of clear ETA for the remaining calculation logic post-scope reduction.
    *   Unresolved resourcing constraints raised by Winson Lim regarding year-end delivery.
    *   Dependency on the "App Replatform" strategy, which necessitated cutting the original scope.

**Summary for Briefing**
The OMNI-1179 project has been deprioritized as a "High Priority Idea" and reclassified as "Platform Health." The team pivoted away from full cart calculation logic (specifically sales/drop-off) to focus on CRUD services and basic calculations in anticipation of the app replatform. While development was WIP through September 2025, the November scope cut leaves open questions regarding the timeline for the remaining basic calculation work and whether the December delivery goal is still viable given resourcing concerns raised in October.


## jira/OMNI-1247: [OSMOS only] Integrate fit-for-purpose digital signage with OSMOS for in-store ad activation
Source: jira | Key: OMNI-1247 | Status: Define (In Progress) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover
**Jira Ticket Briefing: OMNI-1247**

**Current Status**
*   **Ticket:** OMNI-1247 [OSMOS only] Integrate fit-for-purpose digital signage with OSMOS for in-store ad activation.
*   **State:** Define (In Progress).
*   **Type:** Idea | **Priority:** High.
*   **Owner:** Nikhil Grover (Assignee/Reporter).

**Key Context & Opportunity**
The project addresses the fragmentation of current digital screen management (two CMS systems for FP and FS screens, plus disconnected screens) and the inability to advertise on in-store digital displays despite 90% of transactions occurring there. The goal is to consolidate campaign booking, viewing, and management within OSMOS.
*   **Projected Impact:** Retail media GMV target set at $60K (2025), $1.4M (2026), and $3M (2027). Success metrics include Fill rate, Cost per 1000 ad slots (CPM), and total ad slot volume.

**Decisions Made**
*   **Validation Strategy:** A Proof of Value (PoV) exercise with vendor **Advertima** has been selected as the primary validation method for the digital signage system.
*   **Solution Design Approach:** A joint workshop between FPG and OSMOS teams is required to finalize solution design.

**Pending Actions & Owners**
1.  **Execute PoV Exercise:** Nikhil Grover to oversee the Proof of Value assessment with Advertima.
    *   *Target Completion:* End of February 2026.
    *   *Results Expected:* March 2026.
2.  **Conduct Solution Design Workshop:** Schedule and run the FPG x OSMOS workshop.
    *   *Target Date:* November 27 (Year implied as 2025 based on chronology, though ticket shows future dates; context suggests upcoming).
3.  **Define Timelines:** Finalize project timelines immediately following the solution design discussion.

**Key Dates & Deadlines**
*   **Solution Design Workshop:** Nov 27.
*   **PoV Completion:** End of Feb 2026.
*   **PoV Results Reporting:** March 2026.

**Blockers/Notes**
*   No specific blockers reported; the project is currently in the definition and validation phase prior to roadmap prioritization.
*   Assumptions regarding data insights are yet to be fully documented in the ticket.


## jira/OMNI-1391: Available to Promise 1.0 [MVP] - Reservations against Future Inventory
Source: jira | Key: OMNI-1391 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Sathya Murthy Karthik | Reporter: Prajney Sribhashyam
**Ticket:** OMNI-1391 | **Title:** Available to Promise 1.0 [MVP] - Reservations against Future Inventory
**Status:** Soft Prioritised (To Do) | **Type:** Idea | **Priority:** High
**Assignee:** Sathya Murthy Karthik | **Reporter:** Prajney Sribhashyam

**Current State**
The initiative addresses the inability to sell future inventory, causing underselling of high-demand, frequently replenished items and cart abandonment. The proposed MVP allows customers to add currently Out-of-Stock (OOS) items to their cart if restocked before their delivery slot.

**Key Metrics & Impact**
*   **Problem Scale:** OOS impacts 2.4% of impressions during non-peak periods, rising to 5.4% annually (peaking at 8.9% pre-CNY).
*   **Financial Loss:** Estimated annual GMV loss due to OOS is ~$5M. The projected recovery from this solution is $1M–$1.25M.
*   **Goals:** Increase Add-to-Cart (ATC), Average Order Value (AOV), and end-to-end conversion by enabling reservations against replenishment data.

**Proposed Solution & Pilot (Phase 1)**
Sathya Murthy Karthik is tasked with piloting the concept on:
*   **Selection:** 10–15 SKUs (Highest OOS %, daily replenishment, direct supplier).
*   **Location:** 2–3 target stores.
*   **Logic:** During peak slots (6 PM–10 PM), display an additional X% of the next day's replenishment as available. The replenishment team and product manager will experiment with variable "X" values to assess business implications.

**Pending Actions & Ownership**
*   **Action:** Confirm effort estimation (S or XS) for the proposed solution.
*   **Owner:** Sathya Murthy Karthik (per assignment).
*   **Context:** Requested by Danielle Lee on 2025-11-04 to validate feasibility before proceeding.

**Decisions Made**
*   **Strategy:** Proceed with a controlled pilot rather than full deployment, focusing on validating conversion/GMV improvement and operational overhead (space constraints).
*   **Future Options:** Post-pilot evaluation will determine whether to evolve flows via increased store replenishment for T8/T10 slots or explore store-to-store transfers.

**Dates & Blockers**
*   **Last Activity:** 2025-11-04 (Danielle Lee requested effort confirmation).
*   **Blocker:** Pending "S/XS" effort estimation from the assignee to determine next steps.
*   **Deadlines:** No due date currently set; pilot timeline dependent on effort confirmation and subsequent planning.


## jira/OMNI-1393: Enabling User Consent for customer data
Source: jira | Key: OMNI-1393 | Status: Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Zi Ying Liow | Reporter: Zi Ying Liow
**Daily Briefing: OMNI-1393 (Enabling User Consent for Customer Data)**

**Current Status**
*   **Ticket ID:** OMNI-1393
*   **State:** Closed/Merged. This ticket is no longer active and has been merged into **OMNI-1394**.
*   **Original Priority:** High
*   **Assignee/Reporter:** Zi Ying Liow
*   **Issue Type:** Idea

**Key Decisions & Actions Taken**
*   **Decision (2025-11-04):** The scope of OMNI-1393 was merged into ticket **OMNI-1394**. The instruction was explicitly to "remove this ticket" from the active backlog.
*   **Technical Assessment (2025-10-28):** Front-end integration with the Lifecycle Management System (LMS) was estimated as effort XS.
*   **Dependency Identified:** The Martech team requires a 2-week development window to complete the integration.

**Strategic Context & Business Impact**
The original initiative aimed to implement an opt-in/out consent toggle in the preference center to capture user data preferences, sending them to LMS and BigQuery (BQ) for compliance and tracking.
*   **Problem:** Lack of opt-in consent hindered Retail Media use cases including offsite ads, self-served client campaigns using FPG 1st Party Data, dashboard monetization, and merging FPG with external hashed data.
*   **Financial Impact:** Projected to safeguard ~$500K in existing revenue and unlock at least $250K in incremental revenue.
*   **Metrics Goals:** Targeted AOV increase within 6 weeks and Perfect Order metric improvement within 3 months.

**Pending Items & Blockers**
*   **No active pending items** on OMNI-1393 as it has been superseded by OMNI-1394.
*   **Timeline Reference:** Original assessment noted a 2-week development requirement for Martech (as of 2025-10-28).

**Technical References & Dates**
*   **System Components:** LMS, BigQuery (BQ), Preference Center.
*   **Action Date:** Merged on 2025-11-04T10:00:17.128+0800.
*   **Estimation Date:** Development effort confirmed on 2025-10-28T16:59:48.689+0800.


## jira/OMNI-1395: Improving the Empty Shopping Cart Experience
Source: jira | Key: OMNI-1395 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Koklin Gan | Reporter: Sip Khoon Tan | polaris-work-item-link: CART-191
**Daily Briefing Summary: OMNI-1395 – Improving the Empty Shopping Cart Experience**

**Current Status/State**
*   **Ticket ID:** OMNI-1395 (Idea, Priority: High)
*   **Status:** Backlog (Category: To Do)
*   **Assignee:** Koklin Gan
*   **Reporter:** Sip Khoon Tan
*   **Linked Issue:** CART-191 (Polaris work item link)

**Pending Actions & Ownership**
*   **Data Correction:** Update the user metric from "40K monthly active users" to "40K weekly active users (WAUs)" in the ticket description.
    *   *Owner:* Sip Khoon Tan (Requested by Peter Talbot on 2025-10-31T12:51).
*   **Asset Integration:** Add delivery ticket and Figma link to the main description.
    *   *Owner:* Sip Khoon Tan (Requested on 2025-10-31T09:48).
*   **Completeness Check:** Ensure all required sections ("Operational Processes," "Business Plans," "Business Rules/Logic") are populated with specific details to finalize the pitch.
    *   *Owner:* Sip Khoon Tan (Initial instruction on 2025-10-30T16:57).

**Decisions Made**
*   **Feature Scope:** Confirmed inclusion of personalized product recommendations (based on browsing, purchase history, or trending items) and a "1-click Add to Cart" capability directly on the empty cart page.
*   **Strategic Goal:** Shift from a "dead-end" navigation model ("Start Shopping" button) to an engagement model aimed at increasing impressions, ATC actions, and reducing exit rates for 40K WAUs.

**Key Dates & Blockers**
*   **Timeline:** No due date assigned yet.
*   **Blockers/Dependencies:** None currently identified other than the pending content updates (metric correction and asset links) required to move the ticket out of Backlog.
*   **Recent Activity Log:**
    *   2025-10-30T16:57: Initial ticket creation and problem definition drafted.
    *   2025-10-31T09:25: Peter Talbot provided refined Opportunity/Problem text.
    *   2025-10-31T09:48: Sip Khoon Tan confirmed updates and requested delivery/Figma links.
    *   2025-10-31T09:53: Peter Talbot provided requested links (content pending integration).
    *   2025-10-31T12:51: Correction identified regarding Weekly vs. Monthly active users.


## jira/OMNI-1398: Extend offsite ad placement to Google 
Source: jira | Key: OMNI-1398 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover
**Daily Briefing Summary: OMNI-1398**

**Current Status**
*   **Ticket ID:** OMNI-1398
*   **Title:** Extend offsite ad placement to Google
*   **Status:** Backlog (To Do)
*   **Type:** Idea
*   **Priority:** High
*   **Assignee/Reporter:** Nikhil Grover

**Pending Actions & Ownership**
*   **Owner:** Nikhil Grover is responsible for completing the full ticket description to enable progression from "Backlog."
*   **Required Completions:** The current draft lacks specific data and definitions required for a formal business case:
    *   **Problem Definition:** Needs completion of standard user story templates (As a... When... I want...) specifically detailing the FPG RMN sales team's need to leverage 1st party data.
    *   **Impact Quantification:** Estimated number of affected users/customers and current problem severity are missing.
    *   **Goals & Metrics:** Incremental RMN revenue is currently "TBC (pending business case)." Specific Product Metrics (AOV targets, Perfect Order rates) and Business Rules/Logic are undefined.
    *   **Operational Planning:** No details on budget approvals, vendor alignments with Google, or go-to-market strategies.

**Decisions Made**
*   None recorded in the chronological log. The entry serves as an initial idea capture noting the strategic shift from current single-channel (Meta) offering to a multi-channel approach including Google.

**Key Dates & Blockers**
*   **Deadlines:** No due date assigned (`null`).
*   **Blockers:** The ticket cannot move forward in the workflow or be prioritized for development until Nikhil Grover populates the missing sections (Problem Definition, Business Impact, Metrics, and Operational Plans).
*   **Context:** Current ad offering is limited to Meta; this initiative aims to capture additional offsite spend via Google.

**Technical & Reference Notes**
*   The ticket outlines a requirement for FPG RMN sales teams to utilize First Party Data for advertiser acquisition on the Google platform.
*   Success metrics will include the number of advertisers booking offsite campaigns and total Google offsite campaign volume.


## jira/OMNI-1399: Extend offsite ad placement to Tiktok
Source: jira | Key: OMNI-1399 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover
**Daily Briefing Summary: OMNI-1399**

**Ticket Overview**
*   **ID:** OMNI-1399
*   **Title:** Extend offsite ad placement to Tiktok
*   **Status:** Backlog (To Do) | **Priority:** High
*   **Assignee/Reporter:** Nikhil Grover
*   **Type:** Idea

**Current State & Key Dates**
The ticket is currently in the **Backlog** phase with no assigned due date. As of **2025-11-04**, the initiative aims to expand FPG's offsite ad capabilities from Meta-only to include TikTok, leveraging first-party data to capture additional advertiser spend.

**Pending Actions & Ownership**
Nikhil Grover must complete the following documentation and business case components before the idea can advance:
1.  **Problem Definition:** Formalize user stories for both shoppers (order amendment) and the FPG RMN sales team (Tiktok channel offering).
2.  **Impact Analysis:** Estimate affected user volume and define problem severity for the FPG Business Development and Performance Marketing teams.
3.  **Goal Quantification:** Define specific incremental RMN revenue figures (currently marked TBC pending business case).
4.  **Metrics Setup:** Establish baseline vs. target metrics for:
    *   Financial Impact (AOV increase timeline).
    *   Customer Experience (Perfect Order rates).
    *   Campaign Volume (Number of advertisers and TikTok offsite campaigns booked).
5.  **Operational & GTM Planning:** Outline vendor alignment, budget approvals, internal workflows, and go-to-market strategies for launch and user acquisition.

**Decisions Made**
No final decisions on implementation or resource allocation have been recorded yet; the ticket serves as a placeholder to structure the business case. The core strategic direction identified is the shift from "We only offer ads on Meta currently" to "Offer Tiktok as an offsite channel."

**Blockers & Constraints**
*   **Data Gap:** Specific revenue targets and AOV improvement metrics are not yet defined.
*   **Operational Readiness:** Vendor alignments and budget approvals for TikTok integration have not been initiated.
*   **Timeline:** No deadlines have been set, potentially delaying the assessment of FPG's first-party data leverage capabilities on new channels.


## jira/OMNI-1400: Integrate camera/sensor module to track store footfall and impressions on in-store digital screens
Source: jira | Key: OMNI-1400 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover
**Daily Briefing Summary: OMNI-1400**

**Current Status**
*   **Ticket:** OMNI-1400
*   **Type:** Idea (Backlog / To Do)
*   **Priority:** High
*   **Status Category:** Ready for execution planning.

**Key Context & Problem**
The RMN BD team currently sells in-store digital ad slots by unit (15-second plays) without performance benchmarks. This creates friction in media planning and reporting, as there is no data on how many shoppers actually viewed the ads. The goal is to transition from selling "ad units" to selling based on "impressions" to unlock an estimated **$2m annual RMN revenue**.

**Proposed Solution**
Integrate camera/sensor modules to track store footfall and screen impressions. This will provide advertisers/RMN BD users with:
*   Total shopper view counts per store and time slot.
*   Demographic breakdowns (age, gender, customer segment).
*   Performance baselines for future campaign planning.

**Action Items & Ownership**
*   **Primary Owner:** Nikhil Grover (Assignee/Reporter)
*   **Pending Actions:**
    *   Finalize component inputs required before pitching the solution to stakeholders.
    *   Define specific operational dependencies, vendor alignments, and budget approvals for camera/sensor integration.
    *   Establish technical baselines for impression and footfall tracking at the screen/store level.

**Decisions & Metrics**
*   **Decision:** No formal decisions recorded yet; currently in the ideation/backlog phase awaiting full problem definition validation.
*   **Target Metric:** Transition from ad-play sales to impressions-based sales.
*   **Financial Impact:** Potential revenue of ~$2m/year.
*   **Product Goal:** Establish impression baselines and enable forecasting for campaign planning.

**Dates, Deadlines & Blockers**
*   **Due Date:** None set (Backlog status).
*   **Blockers:** The ticket notes "Ensure all components are filled in before pitching," indicating that the current lack of detailed problem definition and operational process documentation is preventing progression to development or sales rollout. No technical blockers identified yet, as this remains an idea stage.


## jira/OMNI-1402: Support 'default search' ad format in the search bar through OSMOS
Source: jira | Key: OMNI-1402 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-3, DPD-299
**Daily Briefing: OMNI-1402 Support 'default search' ad format in the search bar through OSMOS**

*   **Current Status:** The ticket is an **Idea** with a status of **"Soft Prioritised"** and category **"To Do"**. It holds a **High** priority.
*   **Ownership:** Assigned to and reported by **Nikhil Grover**.
*   **Linked Work Items:** Connected to Polaris items **DPD-3** and **DPD-299**.

**Problem & Goal**
The current process requires Ad Ops users to manually set up the 'default search' ad format via Platform Ops in DBP Backoffice, as OSMOS does not yet support it. This creates a fragmentation issue where the RMN BD team and advertisers receive no performance reports for this specific format within FPG RMN campaigns. The objective is to enable centralized booking and timely post-campaign reporting for all package ad formats (including default search) directly within OSMOS.

**Key Dates & Deadlines**
*   **Creation Date:** 2025-11-04
*   **Due Date:** None set (null).

**Pending Actions**
The ticket is currently in a conceptual drafting phase. The description indicates that standard templates for "Solution Summary," "Business Impact," "Product Metrics Impact," "Operational Processes," and "Business Rules/ Logic" are present but **empty**. Pending actions include:
1.  Defining the specific solution summary (User story format).
2.  Quantifying business impact (GMV, income, or cost savings) and product metrics (e.g., AOV increase, Perfect Order rates).
3.  Establishing baseline impression and click-through rate metrics for default search.
4.  Outlining operational dependencies, budget approvals, and Go-to-market strategies.

**Decisions & Blockers**
*   **Decisions:** No formal decisions have been recorded in the chronological log other than the initial creation of the ticket to address the gap between Ad Ops workflows and OSMOS capabilities.
*   **Blockers/Dependencies:** The initiative is blocked by the lack of finalized requirements and impact data. The current "To Do" status suggests no development or configuration work has commenced.


## jira/OMNI-1403: Support 'generic/suggested search' ad format in the search bar through OSMOS
Source: jira | Key: OMNI-1403 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-3, DPD-299
**Daily Briefing: OMNI-1403 – Generic/Suggested Search Ad Format via OSMOS**

*   **Current Status:** The ticket is in the **"To Do"** stage with a status of **"Soft Prioritised."** It is classified as an **Idea** rather than a finalized implementation plan.
*   **Ownership & Assignee:** **Nikhil Grover** serves as both the reporter and assignee.
*   **Pending Actions:** The description outlines a problem statement but lacks a defined solution summary, business impact metrics, operational processes, or specific logic rules. These sections currently require content to be filled in before development can proceed. The core pending action is finalizing the proposal details to enable "Centralised booking" and "Timely post-campaign reporting" on OSMOS.
*   **Decisions Made:** No technical decisions or approvals have been recorded yet; the ticket remains a conceptual request to address operational gaps where Ad Ops currently must set up this ad format via Platform Ops in DBP Backoffice.
*   **Key Dates & Blockers:**
    *   **Created:** 2025-11-04.
    *   **Deadlines:** None assigned (`duedate: null`).
    *   **Blockers:** The initiative is blocked by the lack of a finalized solution summary, business impact data (GMV/income/savings), and defined product metrics.
*   **Dependencies & Links:**
    *   Linked to Polaris work items: **DPD-3** and **DPD-299**.
    *   **Priority:** High.
    *   **Context:** Currently, the RMN BD team and Advertisers receive no performance reports for this format on FPG RMN, creating a poor experience. The goal is to allow booking of all campaign assets (including generic search) in one place to track performance effectively.

**Summary:** OMNI-1403 is a high-priority conceptual request owned by Nikhil Grover to integrate 'generic/suggested search' ad formats into OSMOS, eliminating the need for manual DBP Backoffice setup and enabling unified reporting. The ticket requires completion of the solution summary, business impact analysis, and operational logic sections before moving from "To Do."


## jira/OMNI-1404: Support 'brand deal feature' ad format on category pages through OSMOS
Source: jira | Key: OMNI-1404 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-5, DPD-299
**Daily Briefing Summary: OMNI-1404**

*   **Current Status:** The ticket is classified as a **High Priority** "Idea" currently in the **"To Do"** state (Status Category). It holds a "Soft Prioritised" label. No resolution has been assigned, and no due date exists.
*   **Ownership & Assignee:** The ticket was reported by and is assigned to **Nikhil Grover**.
*   **Core Objective:** Enable the booking of 'brand deal feature' ad formats on category pages via the **OSMOS** platform. Currently, Ad Ops must manually set up this format via Platform Ops in the **DBP Backoffice**, preventing centralized management and tracking.
*   **Business Problem & Impact:**
    *   **Ad Ops:** Inefficient workflow requiring manual DBP Backoffice setup.
    *   **RMN BD Team & Advertisers:** Lack of performance reporting for this ad format, resulting in a poor experience for campaigns on FPG RMN.
    *   **Goals:** Centralized booking for all package ad formats and timely post-campaign reporting within OSMOS.
*   **Linked Work Items:** This initiative is linked to Polaris work items **DPD-5** and **DPD-299**.
*   **Pending Actions & Decisions:**
    *   The "Solution Summary," "Business Impact" (GMV/Income/Cost), "Product Metrics Impact" (specifically AOV and Perfect Order metrics), "Operational Processes," "Business Plans," and "Business Rules" sections in the description are currently empty and require completion.
    *   Baseline impressions and click-through rates for the brand deal feature must be established.
    *   No formal decisions have been recorded yet; the ticket is awaiting detailed planning to move from Idea to execution.
*   **Timeline & Blockers:**
    *   **Last Update:** 2025-11-04T13:13:06.573+0800.
    *   **Deadlines:** None currently set.
    *   **Blockers:** The initiative is stalled at the planning stage due to incomplete documentation in the description fields (Solution, Metrics, Operational Plans).

**Action Required:** Nikhil Grover must populate the missing sections with specific metrics, operational dependencies, and go-to-market strategies to facilitate development movement.


## jira/OMNI-1405: [OSMOS Only] Streamline seller/brand onboarding on OSMOS
Source: jira | Key: OMNI-1405 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover
**Daily Briefing Summary: OMNI-1405**

**Current Status & State**
*   **Ticket ID:** OMNI-1405
*   **Status:** Backlog (To Do) / Idea
*   **Priority:** High
*   **Scope:** OSMOS platform only.
*   **Context:** The current seller/brand onboarding process is manual and slow, taking 3 days for vendor code-brand ID mapping. This causes SKU tagging delays, missed campaign start opportunities, and poor advertiser experiences.

**Pending Actions & Ownership**
*   **Owner:** Nikhil Grover (Assignee & Reporter).
*   **Required Actions:**
    *   Define specific technical specifications to automate SKU information updates in DBP for OSMOS sync.
    *   Automate vendor code tagging to SKUs within DBP.
    *   Implement automation for "advertisable" flag setting based on internal guidelines.
    *   Populate missing quantitative metrics (Business Impact, Product Metrics, Operational Processes) currently listed as placeholders or null in the ticket description.

**Decisions Made**
*   No implementation decisions have been made yet; the ticket remains an idea defining a problem and proposed high-level solutions.
*   Targeted improvement: Streamline SKU onboarding to accelerate activation.

**Key Dates, Deadlines & Blockers**
*   **Dates:** Ticket created/updated 2025-11-06. No due date set.
*   **Blockers:** The ticket is in "Backlog" status awaiting specification completion and metric definition before moving to development.

**Technical References & Impact Goals**
*   **Systems Involved:** OSMOS, DBP (BackOffice), SAP, BQ (BigQuery).
*   **Current Workflow Bottleneck:** Ad Ops uploads CSVs; manual vendor code sharing required; 3-day SLA for mapping; SKU tagging relies on hourly catalog sync.
*   **Proposed Outcomes:**
    *   Increase AOV from $X to $Y within 6 weeks.
    *   Increase Perfect Order rate from X% to Y% in 3 months.
*   **Stakeholders Affected:** Ad Ops, Advertisers, RMN BD team, and Category Managers.


## jira/OMNI-1417: Support Omni pop-up booking and reporting through OSMOS
Source: jira | Key: OMNI-1417 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-2, DPD-299
**Jira Briefing: OMNI-1417 – Support Omni Pop-up Booking and Reporting through OSMOS**

*   **Current Status:** The ticket is an **Idea** currently in the **"To Do"** state, categorized as "Soft Prioritised" with a **High** priority. It was created on **2026-01-14**.
*   **Ownership & Action Items:** **Nikhil Grover** (Assignee and Reporter) owns this initiative. Pending actions involve completing the standard template sections which are currently empty: *Solution Summary, Business Impact, Product Metrics Impact, Operational Processes, Business Plans,* and *Business Rules/ Logic*. The core requirement is to enable platform Ops users to configure Omni Pop Up formats via OSMOS, eliminating the current dependency on DBP for this specific format.
*   **Decisions Made:** No technical or business decisions have been finalized yet; the ticket currently serves as a formal problem definition and goal articulation rather than an active development task.
*   **Key Dates & Blockers:** There are **no due dates** assigned. The primary blocker is the lack of defined solution logic, metrics, and operational plans required to move from "To Do" to execution.
*   **Dependencies:** This initiative links to Polaris work items **DPD-2** and **DPD-299**.
*   **Objective Summary:**
    *   **Problem:** Platform Ops currently must set up pop-up formats via DBP, while other banners are handled through OSMOS.
    *   **Goal:** Achieve centralized booking for all display formats on OSMOS to enable unified tracking, reporting, and improved governance (specifically user-level frequency capping).
    *   **Expected Outcomes:** Simplified reporting via the OSMOS dashboard and a single place for campaign asset performance.


## jira/OMNI-1426: [Phase 2] - Improve GP of product by removing offers for specific SKUs
Source: jira | Key: OMNI-1426 | Status: For Pitching (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Rajesh Dobariya
**Daily Work Briefing: OMNI-1426**

**Ticket Overview**
*   **ID:** OMNI-1426
*   **Title:** [Phase 2] - Improve GP of product by removing offers for specific SKUs
*   **Status:** For Pitching (Category: To Do)
*   **Type:** Idea
*   **Priority:** High
*   **Assignee/Reporter:** Rajesh Dobariya

**Current Status & State**
The ticket is currently in the "For Pitching" phase, awaiting a structured proposal. The current system logic only prevents *new* offers from SAP for blacklisted SKUs post-blacklisting date; it fails to deactivate *existing* active offers. Consequently, discounts continue applying to these SKUs until they expire automatically, negatively impacting Gross Profit (GP).

**Pending Actions & Ownership**
Rajesh Dobariya must complete the "Pitching" requirements before the idea can proceed. Specific gaps in the description include:
1.  **Problem Definition:** Quantify the affected user base (estimated number or %), their segment, and the severity of the issue regarding current manual workarounds.
2.  **Business Impact:** Provide concrete estimates for annual GMV/Income/Cost savings.
3.  **Product Metrics:** Define specific targets (e.g., AOV increase from $X to $Y within 6 weeks).
4.  **Operational & Business Plans:** Outline necessary dependencies, budget approvals, and go-to-market strategies.

**Decisions Made**
No final decisions have been recorded yet. The current consensus identifies the need for a backoffice feature allowing the upload of SKU blacklists to exclude both new SAP offers and disable existing ones.

**Key Dates & Blockers**
*   **Created/Last Updated:** 2026-02-26T09:49:17.889+0800
*   **Deadline:** None currently assigned (null).
*   **Blocker:** The ticket cannot advance to development or implementation until the proposal includes the missing quantitative business and metric data outlined above.


## jira/OMNI-1428: [1hd] Phase 2 -  Scaling one hour delivery to more stores
Source: jira | Key: OMNI-1428 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Rajesh Dobariya | polaris-work-item-link: DPD-627
**Jira Ticket Summary: OMNI-1428**
**Subject:** Phase 2 - Scaling one hour delivery to more stores

**Current Status & State**
*   **Status:** Backlog (To Do)
*   **Type:** Idea
*   **Priority:** High
*   **Associated Work Item:** DPD-627 (Polaris work item link)
*   **Date of Record:** 2026-02-27

**Ownership & Pending Actions**
*   **Owner:** Rajesh Dobariya (Assignee/Reporter).
*   **Pending Action:** The ticket is currently an unpopulated "Idea" template. Rajesh Dobariya must complete the full description before this can be pitched or moved to active development. Required sections include:
    *   **Problem Definition:** Specific user context (shoppers forgetting items) and impact metrics (affected user count, current workarounds).
    *   **Goals & Solution Summary:** High-level feature description addressing order amendments.
    *   **Impact Analysis:** Annual GMV/Income projections and specific product metrics (e.g., AOV increase targets within 6 weeks; Perfect Order rate targets within 3 months).
    *   **Operational & Business Plans:** Budget approvals, vendor alignments, go-to-market strategies, and user retention tactics.
    *   **Business Rules:** System logic and dependencies required for the feature.

**Decisions Made**
*   None recorded. The ticket is currently in the "Backlog" state awaiting initial content generation to define the scope of scaling one-hour delivery to additional stores.

**Key Dates & Blockers**
*   **Deadlines:** No due date assigned (null).
*   **Blockers:** The initiative cannot proceed to execution until the description fields are populated with the required problem definition, metrics, and operational plans.

**Technical References**
*   Ticket ID: OMNI-1428
*   Linked Issue: DPD-627
