

## jira/OMNI-1191: [OSMOS only] Enable offsite ads integration with Meta on OSMOS
Source: jira | Key: OMNI-1191 | Status: Define (In Progress) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: RM-556 | Last Updated: 2026-03-19T12:35:56.248550+08:00
**Ticket:** OMNI-1191 (Idea: [OSMOS only] Enable offsite ads integration with Meta on OSMOS)
**Assignee:** Nikhil Grover | **Priority:** High | **Current Status:** Define / In Progress

**Problem Definition & Success Criteria**
The current workflow requires manual setup of campaigns in Meta/TTD and limits ad creation solely to FairPrice handles. This restricts advertisers from running ads on their own accounts, hindering campaign success and traffic maximization.
*   **Goal:** Enable RMN Ad Ops to manage onsite/offsite channels on a single platform; allow advertisers to run ads on personal accounts alongside FairPrice handles.
*   **Key Metrics:** Target $600k increase in RMN Offsite revenue; baseline of 7-8 offsite campaigns/month.

**Current State & Blockers**
The project is stalled awaiting external dependencies from Meta. While API documentation was received, critical configuration updates and campaign whitelisting remain incomplete. Testing of the first use case is pending due to a reported error escalated to Meta on 2026-01-22.
*   **Blocker:** No update from Meta on campaign whitelisting or configuration as of 2026-01-29.
*   **Risk:** Delivery within 2025 is at high risk; ~4–6 weeks of development time remains after API testing completion.

**Pending Actions & Ownership**
*   **Meta (External):** Enable specific campaign whitelisting; resolve API testing errors; provide firm ETAs. Owner: External vendor, currently unresponsive.
*   **Bryan:** Escalation to senior Meta leads initiated on 2025-10-08 and again on 2026-01-22 to unblock configuration and whitelisting.
*   **Nikhil Grover:** Ongoing follow-ups with Meta; coordination with OSMOS post-testing. Validating assumptions regarding user impact (estimated % of users affected).
*   **Performance Marketing Team:** Confirmed correct config enabled (2025-11-05).
*   **OSMOS Team:** Awaiting whitelisting to complete API testing; pending confirmation of effort estimate and timeline upon resolution.

**Key Decisions & Context**
*   **Solution Path:** Integration requires updated Meta Ads account configuration, specific campaign whitelisting, and OSMOS development (estimated 4–6 weeks once enabled).
*   **Impact:** Targeting $600k RMN Offsite revenue increase; baseline of 7-8 offsite campaigns/month.
*   **Escalation Path:** Due to lack of response from Meta standard channels, issues have been escalated to senior Meta leads and internal business stakeholders (11/11).

**Key Dates & Blockers**
*   **2025-02-27:** Ticket created with status "Define / In Progress"; linked to Polaris work item RM-556.
*   **2025-10-22:** Status marked Red due to lack of Meta configuration update.
*   **2025-11-05:** Performance Marketing confirmed config enabled; OSMOS target ETA for testing completion was 14 Nov (missed).
*   **2026-01-22:** Testing error escalated to Meta with expectation of response by week-end.
*   **2026-01-29:** No further updates; blocked status continues.

**Linked Issues:** RM-556


## jira/DPD-715: Dynamic ad slot configuration for Homepage swimlanes
Source: jira | Key: DPD-715 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-17 | Resolution: Done | parent: DPD-710 | Last Updated: 2026-03-19T04:15:48.930329+00:00
**Ticket Summary: DPD-715 (Dynamic ad slot configuration for Homepage swimlanes)**
*Parent:* DPD-710 ([RMN] Activate product ads in Omni Home swimlanes)
*Assignee:* Michael Bui | *Reporter:* Nikhil Grover
*Priority:* High | *Status:* **DONE** (In Release Queue) | *Due Date:* 2026-03-17

**Current Status**
The story is marked as **DONE** and resides in the **Release Queue**. The feature enables dynamic control of ad placement and count via Split feature flags for both Omni and OG Homepages, removing dependencies on code changes. While initial deployment discrepancies were observed on 2026-03-16 (where OG Home updated to slots [2,5] but Omni lagged at [1,3]), the resolution is recorded as "Done," indicating alignment has been achieved.

**Pending Actions & Ownership**
*   **UAT Completion:** Michael Bui conducted a UAT session on **2026-03-19T00:46:38+0800**, confirming the solution meets all acceptance criteria and marking the ticket as resolved.
*   **Release Execution:** The ticket is pending final deployment validation in the release queue. No further development actions are required.

**Decisions Made & Acceptance Criteria**
The following behaviors were validated against the requirements:
*   **Dynamic API Requests:** With the flag ON and config `[3, 5, 7]`, the system requests exactly 3 ads rendering at positions 3, 5, and 7. Updating Split config to `[2, 4, 6, 8, 10]` triggers a request for 5 ads in new user sessions without deployment.
*   **Fallback Logic:** If the flag is OFF, the system defaults to slots `[1, 3]`, fetching 2 ads.
*   **Empty Configuration:** An empty Split array `[]` results in 0 ad requests; the page displays only organic products with no gaps.
*   **Supply Shortage Handling:** If configuration calls for 3 slots (e.g., `[3, 5, 7]`) but only 2 valid ads are returned, slots 3 and 5 fill with ads, while slot 7 renders organic content.
*   **Out-of-Bounds Handling:** Slot indices exceeding the available content range (e.g., index 20 in a 10-item swimlane) are ignored; only valid indices render.
*   **Stock Integrity:** The system strictly honors existing stock availability checks before requesting ads to prevent displaying out-of-stock items.

**Key Dates & History**
*   **2026-03-10T12:29:37+0800:** Ticket created by Nikhil Grover (Title: Dynamic ad slot configuration for Homepage swimlanes) defining requirements for dynamic placement via Split flags.
*   **2026-03-16T16:54:01+0800:** Partial deployment observed; OG Home updated to 2,5 while Omni Home lagged at 1,3. Coordination initiated to resolve the discrepancy.
*   **2026-03-16T18:07:30+0800:** Mobile application issues resolved; ticket initially marked ready for UAT.
*   **2026-03-19T00:46:38+0800:** Michael Bui conducted UAT session, confirming readiness and marking resolution as "Done."

**Blockers & Constraints**
*   *Resolved:* The Omni Home swimlane configuration discrepancy (previously fixed at 1,3) has been addressed to allow full deployment.
*   *Constraint:* Integration with existing stock logic remains a hard constraint; no out-of-stock products may be displayed as ads.


## jira/DPD-733: Dynamic ad slots for vertical scroll on omni homepage
Source: jira | Key: DPD-733 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-17 | Resolution: Done | parent: DPD-710 | Last Updated: 2026-03-19T04:16:05.107518+00:00
**Daily Briefing Summary: DPD-733**

**Current Status & State**
*   **Ticket:** DPD-733 (Dynamic ad slots for vertical scroll on omni homepage)
*   **Status:** IN RELASE QUEUE (Category: Done, Resolution: Done). Development is complete; the feature is awaiting release.
*   **Parent Ticket:** DPD-710 ([RMN] Activate product ads in Omni Home swimlanes).

**Ownership & Pending Actions**
*   **Assignee:** Michael Bui (Development owner).
*   **Reporter:** Nikhil Grover (Stakeholder/Requester).
*   **Pending Action:** Release deployment. The feature is ready for production rollout with no further development or testing required.

**Key Decisions & Technical Scope**
The story implements a Split feature flag to enable dynamic control of ad placement and count on the Omni homepage vertical scroll without code changes or manual API updates. Key logic decisions derived from acceptance criteria include:
*   **Dynamic Configuration:** When enabled, the system requests ads based on the dashboard-defined slot array (e.g., `[3, 5, 7]`), rendering them at specific indices.
*   **Fallback Logic:** If the feature flag is OFF but ads are enabled, the system defaults to slots `[1, 3]`, requesting 2 ads.
*   **Dynamic Density:** Changes to the Split configuration (e.g., updating from `[3, 5, 7]` to `[2, 4, 6, 8, 10]`) are instantly reflected in new user sessions, requesting a corresponding number of ads without redeployment.
*   **Empty Configuration:** An empty array `[]` results in zero ad requests; the vertical scroll displays only organic content with no gaps or placeholders.
*   **Supply Shortage Handling:** If the Ad API returns fewer ads than requested (e.g., requesting 3 but receiving 2), slots are filled sequentially (e.g., slots 3 and 5), and remaining slots render organic content rather than leaving gaps.
*   **Out-of-Bounds Handling:** Invalid indices beyond available content length (e.g., index 20 with only 10 items) are ignored; rendering is capped by actual content availability.
*   **Stock Integrity:** The system strictly honors existing stock availability checks prior to API requests; out-of-stock products will not be shown as ads.

**Key Dates & Deadlines**
*   **Due Date:** March 17, 2026.
*   **Last Update:** March 10, 2026 (Status transitioned to "IN RELASE QUEUE").

**Blockers**
None identified. The ticket indicates successful completion pending release execution.


## jira/DPD-734: Include swimlane name in the ad request for all Omni Home swimlanes
Source: jira | Key: DPD-734 | Status: TO BE DEFINED (To Do) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-17 | parent: DPD-710 | Last Updated: 2026-03-19T04:16:16.283770+00:00
**Daily Briefing Summary: DPD-734**

*   **Current Status**: The ticket remains in **"TO BE DEFINED"** (Status Category: To Do). As a Story assigned by Reporter Nikhil Grover, the requirement is now explicitly defined with clear acceptance criteria. No development has commenced as of March 10, 2026.
*   **Ownership & Action Items**:
    *   **Assignee**: Michael Bui is responsible for executing the story.
    *   **Pending Action**: Implement logic to pass the swimlane name as the `Page_name` parameter in all ad requests sent to OSMOS for Omni Home swimlanes where ads are enabled, specifically adhering to the defined acceptance criteria.
*   **Decisions Made & Requirements**:
    *   **User Story**: "As a Product Manager, I want to know which ad requests originated from which swimlanes and their corresponding responses So that I can track and optimise the performance on a swimlane level."
    *   **Functional Requirement**: When an ad request is triggered from a swimlane enabled for ads, the system must include the `Page_name` parameter in the OSMOS request containing the name of that specific swimlane.
*   **Key Dates & Deadlines**:
    *   **Due Date**: March 17, 2026 (High Priority).
    *   **Parent Epic**: DPD-710 ("[RMN] Activate product ads in Omni Home swimlanes").
*   **Technical Context**:
    *   **Objective**: Enable granular performance tracking and optimization at the specific swimlane level.
    *   **Integration Point**: OSMOS ad request service.
    *   **Target Parameter**: `Page_name`.

This briefing reflects the transition of DPD-734 from a placeholder to a defined requirement, maintaining the original timeline and ownership structure while incorporating the explicit "As-Product Manager" narrative and acceptance criteria.


## jira/DPD-644: [RMN] Streamline event sync from Segment.io to OSMOS to resolve overage
Source: jira | Key: DPD-644 | Status: Done (Done) | Type: Epic | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-12 | Resolution: Done | parent: DPD-645 | polaris-work-item-link: OMNI-1418, OMNI-1418 | Last Updated: 2026-03-19T12:46:02.643253+08:00
### Daily Briefing Summary: DPD-644

**Current Status**
*   **Ticket:** DPD-644 ([RMN] Streamline event sync from Segment.io to OSMOS to resolve overage)
*   **Type:** Epic (High Priority)
*   **State:** `Done` / `Resolution: Done`. The work is officially completed.
*   **Owner:** Michael Bui (Assignee).

**Pending Actions & Ownership**
*   **Status Update:** No further actions are required; the ticket status and resolution have both been set to "Done."
*   **Responsibility:** Michael Bui has successfully executed the scope, strategy, and execution plan for streamlining event synchronization.
*   **External Dependency:** The task remains linked to Polaris work item **OMNI-1418**.

**Decisions Made**
*   The primary objective of resolving "overage" issues through process streamlining has been achieved, confirmed by the `Done` resolution status.
*   Technical and strategic decisions were finalized during the execution phase, superseding any prior planning states.

**Key Dates & Blockers**
*   **Due Date:** March 12, 2026.
*   **Latest Activity:** Ticket creation recorded on March 3, 2026, at 14:07 UTC+8 by Nikhil Grover (Reporter). The status was updated to `Done` immediately upon or following creation in the log entry.
*   **Blockers:** None; the `Done` status indicates successful completion without open blockers.

**Technical Context**
*   **Source System:** Segment.io
*   **Target System:** OSMOS
*   **Objective:** Optimize data flow to resolve financial overages associated with current sync volumes.

**Historical Note**
*   Previous tracking indicated the work was in a `TO BE DEFINED` state awaiting initiation. This status has been superseded by the current `Done` resolution, confirming that the definition phase and subsequent execution were successfully concluded between creation and the due date. The log confirms the ticket transitioned directly to completion with the title and metadata finalized on March 3, 2026.


## jira/DPD-645: Improve event sync to prevent overage
Source: jira | Key: DPD-645 | Status: Done (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-12 | Resolution: Done | blocks: DPD-273, DPD-273 | parent: DPD-644 | Last Updated: 2026-03-19T12:46:18.668408+08:00
**Ticket:** DPD-645: Improve event sync to prevent overage
**Status:** Done | **Priority:** High | **Resolution:** Done
**Assignee:** Michael Bui | **Reporter:** Nikhil Grover
**Parent:** DPD-644 ([RMN] Streamline event sync from Segment.io to OSMOS to resolve overage)
**Linked Issues:** Blocks DPD-273

### 1. Current Status & Context
*   **Objective:** Optimize the OSMOS PROD destination function in Segment to eliminate recurring monthly cost overages caused by excessive execution times (Transaction and Product events).
*   **Acceptance Criteria:** The function must complete syncing at least **50% faster** than baseline.
*   **Outcome Confirmation:** As of March 19, 2026, no abnormalities were observed in PROD. The optimization is deemed successful.
    *   **Performance Gain:** Daily function time reduced from ~25 days to ~8 days.
    *   **Impact:** This represents a reduction of approximately **12,200 hours/month** of function time. Actual cost savings will be realized over the coming months.
*   **Testing Limitations:** Verification relies on monitoring execution logs and daily totals rather than UI interactions, as E2E testing cannot cover this backend scenario.

### 2. Pending Actions & Ownership
*   **Monitoring:** Continued observation is required to validate the long-term impact of the time reduction on monthly billing cycles.
    *   **Owner:** Michael Bui.
*   **Verification Strategy:** No further immediate deployment windows are required as the target optimization has been confirmed stable in PROD since March 19.

### 3. Key Decisions Made
*   **Resolution Status:** The ticket is marked "Done" as the acceptance criteria were met. The execution time reduction achieved (~68%, from ~25d to ~8d) significantly exceeds the required 50% target.
*   **Versioning:** Optimization was successfully implemented beyond version #56 (original target).

### 4. Key Dates & Blockers
*   **Critical Dates:**
    *   **Ticket Creation/Title Update:** 2026-03-03.
    *   **Original Due Date:** 2026-03-12 (Completed post-deadline).
    *   **Stability Confirmation:** 2026-03-19 (Michael Bui confirmed no abnormality in PROD).
*   **Blockers:** No current blockers.

### 5. Technical References
*   **System Architecture:** Segment.io -> OSMOS PROD destination function -> BigQuery.
*   **Platforms Monitored:** IOS UAT, Android UAT; PROD monitoring confirmed via daily function duration logs.


## jira/OPCO-1940: FP VIPs encounter verification after S&G purchase for fewer reasons, vs other customers
Source: jira | Key: OPCO-1940 | Status: In release queue (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Ravi Goel | Resolution: Done | Labels: priority:improvement | blocks: OPCO-1956 | Last Updated: 2026-03-16T13:53:56.498248+00:00
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


## jira/DPD-700: Fix RMN pentest Low and optionally Info issues
Source: jira | Key: DPD-700 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Due: 2026-03-20 | Resolution: Done | Labels: priority:improvement | relates: DPD-591, DPD-591 | Last Updated: 2026-03-16T13:54:30.994239+00:00
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
Source: jira | Key: DPD-551 | Status: Done (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done | blocks: DPD-383, DPD-383 | Last Updated: 2026-03-16T13:54:46.201998+00:00
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
Source: jira | Key: DPD-631 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done | Last Updated: 2026-03-16T13:55:00.004759+00:00
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
Source: jira | Key: DPD-591 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Due: 2026-03-20 | Resolution: Done | Labels: priority:improvement | relates: RM-669, DPD-700, DPD-700 | Last Updated: 2026-03-16T13:55:19.972142+00:00
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
Source: jira | Key: DPD-383 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Prajney Sribhashyam | Due: 2026-02-18 | Resolution: Done | blocks: DPD-551, DPD-551 | child: DPD-590 | parent: DPD-225, DPD-590 | Last Updated: 2026-03-16T13:55:51.618831+00:00
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
Source: jira | Key: DPD-273 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done | blocks: DPD-645, DPD-645 | Last Updated: 2026-03-16T13:56:05.264554+00:00
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
Source: jira | Key: DPD-590 | Status: TO BE DEFINED (To Do) | Type: Subtask | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Due: 2026-04-24 | child: DPD-383 | parent: DPD-383 | Last Updated: 2026-03-16T13:56:16.301010+00:00
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
Source: jira | Key: QE-1105 | Status: Done (Done) | Type: Chore | Priority: High | Reporter: Michael Bui | Resolution: Done | parent: QE-682 | Last Updated: 2026-03-16T13:56:30.864010+00:00
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
Source: jira | Key: DPD-519 | Status: Done (Done) | Type: Chore | Priority: Medium | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done | Last Updated: 2026-03-16T13:56:41.380591+00:00
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
Source: jira | Key: DPD-221 | Status: Done (Done) | Type: Epic | Priority: High | Reporter: Michael Bui | Resolution: Done | parent: DPD-220 | Last Updated: 2026-03-16T13:56:53.623919+00:00
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
Source: jira | Key: NEDMT-2288 | Status: Done (Done) | Type: Task | Priority: Blocker | Assignee: Yadear Zhang | Reporter: Michael Bui | Resolution: Done | Last Updated: 2026-03-16T13:57:06.074600+00:00
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
Source: jira | Key: DPD-431 | Status: TO BE DEFINED (To Do) | Type: Bug | Priority: Low | Reporter: Vivian Lim Yu Qian | Labels: priority:improvement | Last Updated: 2026-03-16T13:57:22.026679+00:00
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


## jira/DPD-220: Automate sync of newly onboarded SKUs into OSMOS for faster activation
Source: jira | Key: DPD-220 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Resolution: Done | Labels: priority:improvement | parent: DPD-221 | Last Updated: 2026-03-16T13:58:03.447777+00:00
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
Source: jira | Key: QE-843 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Oktavianer Diharja | Reporter: Oktavianer Diharja | Resolution: Done | parent: QE-829 | Last Updated: 2026-03-16T13:58:18.324710+00:00
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
Source: jira | Key: QE-842 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Oktavianer Diharja | Reporter: Oktavianer Diharja | Resolution: Done | parent: QE-829 | Last Updated: 2026-03-16T13:58:31.545590+00:00
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
Source: jira | Key: DPD-1 | Status: Done (Done) | Type: Epic | Priority: High | Reporter: Michael Bui | Resolution: Done | parent: DPD-7, DPD-6 | Last Updated: 2026-03-16T13:58:41.195509+00:00
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
Source: jira | Key: DPD-7 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Daryl Ng | Reporter: Michael Bui | Resolution: Done | Labels: priority:operations | parent: DPD-1 | Last Updated: 2026-03-16T13:58:50.931419+00:00
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
Source: jira | Key: DPD-6 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done | Labels: priority:operations | parent: DPD-1 | Last Updated: 2026-03-16T13:58:57.988441+00:00
**Daily Briefing Summary: DPD-6**

*   **Current Status:** The ticket is marked as **Done**. All work associated with this item has been completed.
*   **Actions Pending:** There are no pending actions or ownership transfers required for this specific ticket. The assignee and reporter, **Michael Bui**, have finalized the task.
*   **Decisions Made:** The scope was defined as configuring ticket types and transitions within the system. This configuration has been successfully implemented and resolved.
*   **Key Dates & Deadlines:** No due date was assigned to this item. The final status update occurred on **2026-01-15**. There are no reported blockers preventing completion.

**Ticket Metadata Context:**
This task (**DPD-6**) is categorized as a **Chore** with **High** priority and carries the label `priority:operations`. It serves as a sub-task for the parent initiative **DPD-1 (Foundation Setups)**. The work was executed entirely by **Michael Bui**.


## jira/DPD-8: [RMN] Renew guest account for RMN contractor
Source: jira | Key: DPD-8 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done | Labels: priority:operations | Last Updated: 2026-03-16T13:59:09.562553+00:00
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
Source: jira | Key: OMNI-1297 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Ram Datchnamoorthy | polaris-work-item-link: PRDM-239 | Last Updated: 2026-03-16T13:59:29.124478+00:00
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


## jira/OMNI-1249: B2B Solution: Integration work
Source: jira | Key: OMNI-1249 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Erica Lee | Reporter: Fiona U | blocks: OMNI-1362, OMNI-1362 | discovery---connected: DPD-57 | migration_parent: PAY-7080 | polaris-work-item-link: DPD-682, PAY-7080, DPD-57 | Last Updated: 2026-03-17T17:48:19.327891+00:00
**Ticket Summary: OMNI-1249 (B2B Solution: Integration Work)**
**Assignee:** Erica Lee | **Reporter:** Fiona U | **Status:** In Development (In Progress) | **Priority:** High | **Type:** Idea

### Current Status & Strategic Context
The project is **In Development**, focusing on integrating new B2B capabilities to scale GMV from $16M (2025) to $100M by 2030. While historical context noted critical delays pushing the MVP Go-Live to April 2026, the primary focus is now enabling **Co-mall** on SAP and Phase 2 of the WMS Middleware go-live.

### Key Features & Scope
The initiative addresses gaps in current B2B solutions (limited discounting, no subscription pricing) by introducing:
*   **Parent-Child Account Structures:** Enforce corporate policies across departments with configurable credit limits and payment modes.
*   **Donation Drives & Corporate Employee Discounts (CED):** Replace fragmented PCM routing with unified portal campaigns for SKUs/EDMs.
*   **Advanced Workflows:** Unified management for quotations, bulk orders, credit approvals, and invoicing.

**Business Impact:** Targeting 30% reduction in manual inquiries within 12 months and a 200% increase in new business customers by 24 months.

### Key Decisions & Technical Direction
*   **SAP Strategy:** Proceed with **"Co-mall"** on SAP pending blueprint sign-off. The launch relies on **Phase 2** of WMS Middleware to enable full B2B billing/document flows (Phase 1 only routes orders to PFC).
*   **Architecture:** Integration required with SAP, DBP, Segment, and Zendesk for catalogues, pricing, analytics, and support workflows.

### Pending Actions & Owners
*   **WMS Middleware Confirmation (Critical):** Confirm if mid-March go-live includes **Phase 2** functionality. Status remains "not confirmed." Owner: **Zi Ying Liow / WMS Team**.
*   **SAP Blueprint Sign-off:** Review session scheduled for January 16, 2026. Owner: **CC & Finance**.
*   **UAT Execution:** Test cases to be finalized by Feb 22; inputs gathered Feb 23–25; business socialization Feb 26–27. UAT testing scheduled for mid-March (previously noted March 3). Owner: **Zi Ying Liow / Comall**.
*   **Training & Enablement:** Cross-functional training required for Account Management (onboarding/parent-child), Finance (credit matrix), Operations (bulk orders), and Support (Zendesk workflows).
*   **Dependency Resolution (March 11):** Resolve status on decoupling First Mile training and Forecasting/Reporting alignment. Owner: **Zi Ying Liow / Stakeholders**.

### Key Dates & Deadlines
*   **January 16, 2026:** SAP Blueprint Sign-off review.
*   **Mid-March (2026):** Target WMS Middleware Phase 1 Go-Live; re-evaluate Phase 2 readiness.
*   **March 2026:** UAT execution (dates updated to mid-March).
*   **March 11, 2026:** Call to resolve Forecasting/Reporting and First Mile decoupling.
*   **April 2026 (Tentative):** B2B Platform Go-Live.

### Blockers & Risks
*   **WMS Middleware Readiness:** Lack of confirmed Phase 2 go-live remains the single biggest blocker for April launch.
*   **SAP Blueprint Sign-off:** Delays in Jan 16 review directly impact development timelines.
*   **Integration Complexity:** Dependencies on SAP/DBP/Zendesk alignment may strain resources given the new scope (BCRS, Co-mall).

**Linked Issues:** DPD-682, OMNI-1362 (Blocks), PAY-7080, DPD-57.


## jira/OMNI-1363: [Decoupling from SAP] Migrate CF apps to DBP to improve MP Consol fulfilment experience
Source: jira | Key: OMNI-1363 | Status: Paused (To Do) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Gopalakrishna Dhulipati | polaris-work-item-link: DST-2272, DPD-326, DPD-332, DPD-341, DST-2531, DPD-348 | Last Updated: 2026-03-18T21:36:33.991412+00:00
**Ticket:** OMNI-1363 | [Decoupling from SAP] Migrate CF apps to DBP to improve MP Consol fulfilment experience
**Assignee:** Prajney Sribhashyam | **Reporter:** Gopalakrishna Dhulipati | **Priority:** High | **Status:** Paused (To Do) | **Type:** Idea
**Linked Issues:** DST-2272, DPD-326, DPD-332, DPD-341, DST-2531, DPD-348

### Current Status
*   **Overall State:** Paused/Delayed. Development scope was refined in March 2026 to exclude "Pricing" components (removing a 70 man-day estimate).
*   **Business Context:** Problem involves $170K annual Cloud Foundry costs and enhancement dependencies for MP Consolidate Fulfilment Sellers and DPD developers.
*   **Risk Level:** High risk regarding historical data risk; contingency plan is in development.

### Pending Actions & Ownership
*   **Data Contingency:** Complete development of the contingency plan for historical data at risk during migration.
*   **Training:** Product & Tech teams must create training materials prior to rollout.
*   **Alignment:** Confirm final alignment with PFC & First Mile teams regarding device-managed rollout to ensure zero operational disruption.

### Key Decisions Made
*   **Scope Definition (2026-03-18):** Ticket scope strictly limited to Fulfilment apps; Pricing component removed from effort estimates.
*   **Rollout Strategy:** Managed by device to prevent downtime for Operations.
*   **Technical Go-Live (Original Baseline):**
    *   UAT & Training: 5–9 Jan.
    *   Rollout Window: Start date 12–16 Jan.
    *   *Note:* These dates were superseded by WMS Middleware delays shifting the live to April 2026 in prior updates, but the scope reduction remains valid for the current paused state.

### Key Dates, Deadlines & Blockers
*   **Blocker:** WMS Middleware dependency previously delayed live from Jan to March/April; current status is Paused pending re-alignment.
*   **Scope Change:** Pricing component (70 man days) removed from ticket scope as of 2026-03-18.

### Success Criteria & Scope
*   **Goal:** Reduce annual Cloud Foundry costs by $170K (Baseline: $170K -> $0) and improve DOT% for CF sellers.
*   **Operational Improvement:** Enable earlier order pushing to CF apps (4PM on D-1).
*   **Components for Rollout:**
    *   First Mile Operations App
    *   First Mile Dashboard
    *   PFC Receiving App


## jira/OMNI-1362: [Decoupling from SAP] Improve order orchestration with integration to WMS Middleware
Source: jira | Key: OMNI-1362 | Status: Paused (To Do) | Type: Idea | Priority: High | Assignee: Gopalakrishna Dhulipati | Reporter: Gopalakrishna Dhulipati | blocks: OMNI-1249, OMNI-1249 | polaris-work-item-link: DPD-184 | relates: OE-3209 | Last Updated: 2026-03-18T21:37:49.266559+00:00
**Jira Ticket Summary: OMNI-1362**
**Topic:** [Decoupling from SAP] Improve order orchestration with integration to WMS Middleware
**Current Status:** **Paused (To Do)** | Priority: High | Assignee: Gopalakrishna Dhulipati | Reporter: Gopalakrishna Dhulipati | Type: Idea

### 1. Current State & Context
As of **September 11, 2025**, this initiative remains an **Idea** in a **Paused (To Do)** state. The primary objective is to decouple from SAP to resolve GST non-compliance risks for the Finance team and reduce dependency on SAP flows that negatively impact customer fulfillment experiences.

*   **Primary Drivers:**
    *   **Finance Team:** Resolving GST non-compliance.
    *   **Customers:** Reducing fulfillment experience dependencies on SAP flows.
*   **Linked Issues:** Blocks OMNI-1249; Relates to OE-3209 and DPD-184 (Polaris work item link).

### 2. Implementation Plan & Scope
The strategic approach involves a specific integration sequence:
1.  **DBP** integrates with **WMS Middleware**.
2.  Subsequent integration between **WMS Middleware** and **TMS**.

**UAT Scope:**
*   DBP - WMS Middleware Flows
*   DBP - TMS Flows

### 3. Pending Actions & Ownership
To transition from "Paused" to active roadmap prioritization, the following mandatory steps are required:
*   **Define Success Criteria:** Specific dimensions and metrics must be established; this is a prerequisite for prioritization. Currently, these fields in the idea template are undefined.
    *   *Required Data:* Definition of specific dimensions/metrics, current baseline vs. expected outcome, and target timeline.
*   **Validation:** Sufficient validation must be conducted to justify moving this Idea onto the roadmap.
    *   *Owner:* Gopalakrishna Dhulipati (Reported/Assigned) and Product/Finance Stakeholders.

### 4. Decisions Made
*   **Status Classification:** The ticket is formally categorized as an "Idea" rather than a completed development task, overriding previous execution timelines.
*   **Problem Definition:** Confirmed that the primary problem is GST non-compliance for Finance and fulfillment dependency on SAP flows. Integration with WMS Middleware is identified as the primary prerequisite.

### 5. Critical Blockers & Dependencies
*   **Primary Blocker:** The absence of defined success criteria (dimensions/metrics) prevents roadmap prioritization.
*   **Dependencies:**
    *   Blocks: OMNI-1249
    *   Relates: OE-3209, DPD-184

*(Summary updated to reflect the "Paused" status and "Idea" type as of 2025-09-11. Historical execution dates (e.g., Dec SIT completion, March/April 2026 production) have been removed as they contradict the current re-platformed strategic state.)*


## jira/OMNI-1294: [BCRS Compliance] Phase 2: Order Place & Returns/Refunds Processxa
Source: jira | Key: OMNI-1294 | Status: UAT (In Progress) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Winson Lim | Labels: bcrs | discovery---connected: NEDMT-2334 | polaris-work-item-link: DPD-225 | Last Updated: 2026-03-19T12:36:39.180186+08:00
**Ticket:** OMNI-1294 | **Status:** UAT (In Progress) | **Priority:** High | **Assignee:** Prajney Sribhashyam | **Reporter:** Winson Lim
**Linked Issues:** DPD-225, NEDMT-2334

### Current State
The initiative is in the User Acceptance Testing (UAT) phase for Phase 2 (Order Place & Returns/Refunds Process). As of **March 19**, program risk has shifted from "High" to **Medium**. The system requires linked deposit SKUs ($0.10) across POS, SAP, and Mirakl to ensure regulatory compliance with Singapore's BCRS enforcement by July 1, 2026 (labelling deadline: April 1, 2026).

### Key Decisions & Strategic Shifts
*   **Risk Update (Mar 19):** Program risk downgraded from High to Medium.
*   **Scope Confirmation:** Phase 2 includes Digital and Food Services teams. Scope explicitly excludes SAP Decoupling order flow (state management remains in OMS; SAP receives orders only in end state).
*   **Finance Alignment:** Invoice design, Sales Posting, and Seller Reports have received sign-off from Finance and Corporate Control (CC). Deployment to production is pending.
*   **Deposit Logic:** Deposits are treated as separate line items, excluded from offer limits/loyalty points, and not GST-applicable. Deposit SKUs must be nested under subtotal or displayed as a separate charge on receipts/cart.

### Pending Actions & Owners
*   **UAT Completion (Refunds):** Target completion scheduled for **March 26**. Pre-order Staff App MP SKU creation UAT ETA: **March 20**.
*   **SnG Refunds:** Development in progress; UAT ready by **March 24**, with target complete date of **March 26**.
*   **Production Testing:** Tech live for Browse, PDP, Cart, Checkout, Order Details/History pending final production test.
*   **Partial Pick Logic:** Clarification needed on partial deposit charging logic (e.g., if 8 of 10 items in a pack are picked).
*   **Pre-Order Digital Flow:** Confirmation required on whether digital teams are involved in pre-order receiving.

### Blockers & Risks
*   **Refunds Complexity:** Business discussion needed regarding refunding deposits for damaged/expired products and partial refunds for multipack SKUs (e.g., refunding 1 deposit item from a pack of 6).
*   **Technical Validation:** While Finance sign-off is complete, final production deployment remains pending.

### Critical Dates & Deadlines
*   **UAT Completion:** March 26, 2026 (Refunds/Pre-order).
*   **Regulatory Milestones:** Product labelling by April 1, 2026; Enforcement by July 1, 2026.
*   **Financial Compliance Target:** 100% of BCRS beverage SKUs with accurate deposit pricing by March 2026.

### Technical Context
The solution mandates the creation of linked deposit SKUs for all regulated beverages (150ml–3L) in Mirakl and DBP. Key flows include:
*   **Catalogue:** Replacing old SKUs with BCRS SKUs in Algolia, Dynamic Yield, and Purchase History indices.
*   **Checkout/POS:** Displaying deposit as a separate charge; excluding deposit SKUs from picker/TMS apps to avoid operator confusion.
*   **Returns:** Ensuring master SKU returns trigger corresponding deposit refunds in SAP and OMS.


## jira/OMNI-1407: Improve seller catalogue compliance to align with FSQ expectations
Source: jira | Key: OMNI-1407 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Prajney Sribhashyam | polaris-work-item-link: DPD-100 | Last Updated: 2026-03-19T12:36:59.501940+08:00
**Jira Briefing: OMNI-1407 – Improve Seller Catalogue Compliance (FSQ Alignment)**

**Current Status**
*   **State:** In Development (In Progress).
*   **Type:** Idea.
*   **Priority:** High.
*   **Assignee/Reporter:** Prajney Sribhashyam.
*   **Linked Issue:** DPD-100.
*   **Progress Indicator:** On Track.

**Key Decisions & Estimates**
*   **Scope:** Implementation of mandatory "License Code" and "Expiry Date" fields on the Mirakl SKU creation form, triggered by Level 3 (L3) categories (e.g., Safety Mark, Halal, Organic). Supports single and mass upload templates. Includes exemption logic with an explanation field for non-required cases.
*   **Automation Logic:** System to send expiry warnings at 4 weeks and 1 week prior; automatic SKU disabling/hiding upon certificate expiry with status consistency between Mirakl and DBP.
*   **Reapproval Process:** Updated certificates trigger a "pending verification" status for reapproval; successful updates reactivate the label in the catalogue.
*   **Sizing:** Finalized as **Small** (estimated at **30 people-days**) per Prajney Sribhashyam's update on Dec 3.
*   **Business Impact:** Addresses high risk of $2.5M annual GMV loss from de-listing (approx. 25% of assortment). Goal is 100% FSQ compliance and shopper transparency.
*   **Scope Details:** Covers HSA, Safety Mark, Vector Control, NEA, and IMDA registrations; Halal and Organic certifications. Requires retrofitting expiry functionality for existing certificates lacking this data.

**Upcoming Dates & Deadlines**
*   **March 31, 2025:** Deadline to disable non-compliant SKUs (Original target). *Note: End date pending update as of Mar 19.*
*   **March 16, 2026:** Scheduled start for System Integration Testing (SIT). Koklin Gan raised concerns regarding BCRS work requirements affecting this date.
*   **March 17, 2026:** Scheduled start for User Acceptance Testing (UAT).

**Pending Actions & Ownership**
*   **Timeline Confirmation:** Prajney Sribhashyam confirmed the start date remains unchanged (Mar 16) but will update the end date. Immediate stakeholder communication is required regarding the revised March timeline and BCRS impact.
*   **Testing Planning:** Sathya Murthy Karthik requires a stakeholder update confirming the new schedule and test case creation.
*   **Data Preparation:** Marketplace team to source certifications for Mirakl upload and conduct weekly data extractions for validation. A "Source of Truth" working sheet must be finalized per L3 category.
*   **Operational Setup:** Teams must establish the alert pipeline (4 weeks/1 week) and define the manual processing workflow for license code/date extraction.

**Technical References**
*   **Platform:** Mirakl SKU creation form, DBP synchronization.
*   **Fields:** Mandatory inputs for license code and calendar-based expiry dates; exemption logic with explanation field required for non-required cases.
*   **Retrofitting:** Expiry functionality must be retrofitted for existing certificates (Halal, Organic) currently lacking this data.


## jira/OMNI-1345: [MP Foundational] Sales Breakdown & Seller Payouts
Source: jira | Key: OMNI-1345 | Status: Paused (To Do) | Type: Idea | Priority: High | Assignee: Koklin Gan | Reporter: Prajney Sribhashyam | discovery---connected: OMNI-1178 | polaris-work-item-link: DST-2056, DST-2272, DST-2487, DPD-9 | Last Updated: 2026-03-19T12:37:18.608631+08:00
**Ticket:** OMNI-1345 [MP Foundational] Sales Breakdown & Seller Payouts
**Assignee:** Koklin Gan | **Reporter:** Prajney Sribhashyam | **Priority:** High | **Type:** Idea
**Current Status:** Paused (To Do). Initiative is on hold pending the finalization of foundational business model changes driven by compliance inputs.

### 1. Problem Definition & Impact
The initiative addresses critical gaps in sales order data where key transactions—including dropoffs, refunds, cancellations, and voucher applications—are not captured or reflected accurately. This causes discrepancies between reported and actual figures, impacting financial accuracy and seller payouts.
*   **Current Workaround:** Manual interventions are currently used to check the "seller report" issue seller-by-seller. These methods have significant gaps and lack 100% accuracy.
*   **Impact:** All MP sellers face improper charging for refunds, cancellations, and returns in downstream financial systems.

### 2. Completed Milestones & Technical Validation
The following steps have been completed:
*   **Milestone 1:** Migrated CF sellers to the new app and completed cutover (Done - Nov 30).
    *   *Technical Detail:* Sellers moved to seller app to measure "picked by seller" → FFS.
*   **Milestone 2:** Validated enhanced 'Sales Breakdown Report' (Done - Jan 5; Business signed off).
    *   *Technical Details:* 'Put-away' Qty fetched from WMS DB for PFC; Finance alignment on 'Sales Order Breakdown' completed.
    *   *Validation:* DA team generated the report based on aligned requirements. A limited set of sellers was validated to measure disputes and NPS.

### 3. Scope Changes & Decisions
*   **Out of Scope (Deferred):** "Returns & refunds flow" alignment across RB & MP, and alignment with finance on SOA seller reports, are marked out of scope for this phase (deferred to "Project Light").
*   **Rollout Timeline:** The original ETA was Jan 24. This was updated to Jan 31 while working on shrinking the timeline. Despite previous authorization for UAT, the entire initiative is now paused pending new requirements.

### 4. Pending Actions & Blockers
*   **Primary Blocker:** Awaiting finalization of requirements for the foundational change in the consolidated fulfillment business model due to compliance inputs (business license limitations).
*   **Next Steps:** No technical or rollout actions can proceed until new business rules are defined. The team must wait for revised specifications before re-initiating data generation or UAT.

### 5. Key Dates & Technical References
*   **Status Date:** March 17, 2026 (Pause decision recorded).
*   **Success Criteria:** Improved Seller NPS and Full Compliance alignment.
*   **Linked Issues:** OMNI-1178 (Discovery), DST-2056, DST-2272, DST-2487, DPD-9.
*   **Data Sources:** BigQuery table `mp_sales_breakdown`.
*   **Tools/Reports:** Looker Studio, SAP, DBP; Affected reports include Seller Report, Combined Sales Report, and Finance Concess Report.


## jira/OMNI-1296: Enhanced Notification Preference Center for Multi-Channel Communication Management
Source: jira | Key: OMNI-1296 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Sip Khoon Tan | Reporter: Sip Khoon Tan | discovery---connected: CORE-304 | polaris-work-item-link: CORE-304 | Last Updated: 2026-03-17T17:50:09.005383+00:00
**Jira Ticket Briefing: OMNI-1296**
**Topic:** Enhanced Notification Preference Center for Multi-Channel Communication Management
**Current Status:** In Development (High Priority) | **Type:** Idea
**Assignee/Reporter:** Sip Khoon Tan; **Links:** CORE-304 (Discovery - Connected / Polaris work item link).

### 1. Current State & Progress
The project addresses the limitation of binary unsubscribe mechanisms which cause total communication loss upon opting out from a single channel. The solution replaces this with a granular, centralized preference center for EDMs, Push Notification Services (PNS), and WhatsApp across specific business swimlanes.
*   **Functional Scope:** Customers can now control subscriptions by business unit, set frequency (daily/weekly/monthly), and manage transactional vs. marketing PNS settings separately.
*   **Business Swimlanes Supported:** Grocery, FP Super, FP Finest, FP Hyper, FP Online, Unity, Cheers, Kopitiam, FP Partners, FP B2B, and Link Rewards.
*   **Timeline Context:** While the status is "In Development," historical planning previously indicated backend completion by Feb 20, 2026, and UAT in March 2026. The specific implementation dates from prior drafts conflicting with the current "Idea" type status should be treated as preliminary targets pending final alignment.

### 2. Pending Actions & Ownership
*   **Development & Integration:** Finalize development of the centralized interface integrating with Salesforce Marketing Cloud (SFMC) and mobile apps/web notification centers. Primary ownership: Sip Khoon Tan, Xue Yin, William.
*   **PNS Segmentation:** Complete integration to segment PNS based on type (app features, announcements, transactional, marketing). Owner: Martech team.
*   **Business Alignment:** Finalize go-live coordination pending business direction and CCO/CRM timeline alignment (Zi Ying Liow).

### 3. Decisions Made
*   **Granular Control Strategy:** Confirmed that customers must be able to select specific content types rather than a global "unsubscribe all" only, reducing churn.
*   **Financial Targets:** Validated goals to reduce complete unsubscribe rates by 30% initially (EDM: 72k → 50k unsub/year; PNS: device rate -30%).
*   **Long-term Metric:** Target a 50% reduction in annual preference center unsubscribes (reducing from 50k to 25k annually).

### 4. Business Impact & Metrics
*   **Financial Goal:** Prevent total annual GMV loss of **$531.6k**.
    *   **EDM Impact:** Current loss $192k/year (6,000 unsub/month). Target prevention: **$57.6k**.
    *   **PNS Impact:** Current loss $1.58M/year. Target prevention: **$474k**.
*   **Operational Benefits:** Enhanced segmentation for Marketing Operations, improved data analytics for personalization, and reduced campaign waste through precise audience targeting.
*   **Scalability:** Architecture supports future communication channels and additional business swimlanes.

### 5. Key Dates & Blockers
*   **Current Status:** In Development (In Progress).
*   **Dependency:** Integration with Salesforce Marketing Cloud remains a critical path item for Martech team execution.
*   **Risk:** Timeline alignment with CCO and CRM is required to confirm the final delivery window, previously targeted around mid-April 2026 but subject to change given the "Idea" classification adjustments.


## jira/OMNI-1423: [1HD] Pilot to customer launch readiness
Source: jira | Key: OMNI-1423 | Status: UAT (In Progress) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Prajney Sribhashyam | polaris-work-item-link: DPD-406 | Last Updated: 2026-03-19T12:37:37.502764+08:00
### Daily Briefing: OMNI-1423 [1HD] Pilot to Customer Launch Readiness

**Current Status**
*   **Status:** UAT (In Progress / Green).
*   **Date/Time Reference:** Current update as of **March 19, 2026**.
*   **Progress:** Production testing commenced on March 18. The team is actively resolving data issues related to "bulk threshold." While a root cause (RC) is being identified for these bugs, the overall status remains Green.

**Pending Actions & Ownership**
*   **Owner:** Rajesh Dobariya (Assignee).
*   **Reporter:** Prajney Sribhashyam.
*   **Action Items:**
    *   Tech team to identify root causes and fix bulk threshold data issues.
    *   Continue production testing on March 19, 2026.
    *   Schedule Second Round of Production Testing (Business, Finance, Ops) for the week starting **March 24**.
    *   Schedule Third Round (E2E with 3PL) for **March 31**, contingent on SOP alignment and driver availability.
    *   Update technical and business "live" dates pending final confirmation.

**Key Decisions Made**
*   **Scope Splitting:** On **February 20, 2026**, stakeholders aligned on MVP "must-haves," splitting delivery into two phases.
*   **Item Movement:** On **February 27, 2026**, non-blocker items were moved to a new epic to streamline focus.
*   **Launch Target:** As of March 19, the project is on track for a **April 7** launch.

**Key Dates, Deadlines & Blockers**
*   **Upcoming Milestones:**
    *   **March 18–19:** Ongoing production testing.
    *   **Week of March 24:** Second round of production testing (Stakeholders).
    *   **March 31:** Third round of E2E testing with 3PL.
    *   **April 7:** Target customer launch date.
*   **Blockers/Dependencies:** Active investigation into bulk threshold data issues continues to impact immediate progress but is not currently derailing the April 7 target, assuming SOPs align for the March 31 test.

**Technical & Contextual References**
*   **Linked Issue:** DPD-406 (Polaris work item link).
*   **Project Goal:** Ensure the FairPrice app and backend are ready for customer launch of express delivery service:
    *   **Shoppers:** Seamless discovery, cart, checkout, and receipt without planning horizon.
    *   **Pickers:** Task completion within X-minute SLA to prevent delays.
    *   **Business Managers:** Accurate financial attribution for issues and sales.
*   **Product Metrics Targets:**
    *   **Financial:** Increase AOV from $X to $Y within 6 weeks.
    *   **Customer Experience:** Increase Perfect Order rate from X% to Y% in 3 months.
*   **Priority:** High.
*   **Type:** Idea.


## jira/OMNI-1425: [1HD] Phase 2 - Build to enable scaling of 1 hour to 100 stores
Source: jira | Key: OMNI-1425 | Status: Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Rajesh Dobariya | polaris-work-item-link: DPD-627 | Last Updated: 2026-03-19T12:37:57.942603+08:00
**Jira Briefing: OMNI-1425 – Phase 2 Build to Scale 1 Hour Delivery (1HD) to 100 Stores**

**Current Status**
*   **Ticket ID:** OMNI-1425 | **Linked Issue:** DPD-627
*   **Status Category:** To Do (Marked "Prioritised")
*   **Priority:** High
*   **Type:** Idea
*   **Assignee/Reporter:** Rajesh Dobariya
*   **Latest Update:** 2026-03-19 (WIP: Awaiting business impact/timeline for scaling; effort depends on undefined solution and 3PL requirements).

**Core Objective & Scope**
Scale 1HD from 1 to 100 stores via 3PL integration. Key functional components include:
*   **Integration:** Push order details (Name, Address, Contact No) to vendor's last-mile app for live tracking and Proof of Delivery (POD).
*   **App Enhancements:** Picker app updates for real-time new order notifications; simplified store creation (inventory, assortment, time-slot, capacity).
*   **FFS Operations:** Handling 1HD in FFS stores with defined financial treatment (accounting entries) and pilot trial iteration.

**Pending Logic Decisions (Clarification Required)**
*   **Notification Trigger:** Clarify if vendor is notified at "order placement" or "upon packed status."
*   **Data Fields:** Confirm if transfer is limited to Name, Address, and Contact No only.
*   **Completion Protocol:** Define mechanism/timing for vendor app to notify DBP upon order completion.

**Pending Actions & Ownership (Updated)**
*   **Documentation Gaps (Owner: Rajesh Dobariya):** All components must be filled before pitching.
    *   **Problem Definition:** Articulate specific pain point using JTBD format (As a shopper, when I forget items post-order, I want to amend/add items so I can avoid multiple fees).
    *   **User Impact Analysis:** Define affected segments, estimated volume (% or number), and current manual workarounds.
    *   **Business Impact:** Quantify annual GMV/Income/Cost savings. Current draft notes: "Eliminate manual order handling, reduce human error risk, ensure faster fulfillment."
*   **Metrics Targets:**
    *   **Financial:** Increase AOV from $X to $Y within 6 weeks.
    *   **Customer Experience:** Improve Perfect Order rate from X% to Y% in 3 months.
    *   **Operational:** Track Order Processing Time, Delivery Status Sync Accuracy, and Operational Errors.

**Blockers & Dependencies**
*   **Missing Business Data:** Awaiting business impact and timeline for scaling from the business team (as of 2026-03-19).
*   **Definition Gaps:** Actual scope and effort estimation are blocked until the Solution is defined and 3PL requirements are clarified.
*   **Operational Dependencies:** Requires vendor alignment, budget approvals for financial treatment, and internal workflow definition.

**Key Dates & Deadlines**
*   **Status Set to Prioritised:** 2026-02-11
*   **JTBD Update Request:** 2026-03-18 (Koklin Gan requested updates).
*   **Current Status:** WIP as of 2026-03-19.


## jira/OMNI-1414: Integrate personalized gamification challenge with FP app
Source: jira | Key: OMNI-1414 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: James Huang | polaris-work-item-link: DPD-297 | Last Updated: 2026-03-19T12:38:21.202186+08:00
**Jira Briefing: OMNI-1414 – Integrate Personalized Gamification Challenge with FP App**

**Current Status**
*   **Status:** In Development (In Progress).
*   **Assignee:** Rajesh Dobariya.
*   **Reporter:** James Huang.
*   **Type:** Idea / High Priority.
*   **Linked Issue:** DPD-297.
*   **Progress:** Backend work commenced March 11. UAT rescheduled to **March 24, 2026** (previously March 23). Technical live date confirmed for **March 30, 2026**, allowing a one-week buffer for post-UAT fixes. Business live date remains TBD, pending issue identification from UntieNot.

**Key Decisions & Requirements**
*   **Technical Architecture:** Customer UID must be hashed using `sha256 + salt ('s@veValue!')` before passing to the webview URL (Decision by Alvin Choo, Jan 30).
*   **Platform Integration:** Contracted "UntieNot" platform for personalized gamification targeting ~1.8M DCC customers. App team must build entry points across Split PNW banner, Rewards page, OMNI Popup, Homepage Banner, Voucher Wallet Banner, and Rewards Tile.
*   **User & Marketing Logic:**
    *   *Shoppers:* Participate in challenges relevant to their app/in-store/EDM browsing behavior to earn rewards.
    *   *Marketers:* Create efficient campaigns to drive sales metrics with higher participation rates.
*   **Effort Estimate:** 3 man-weeks total (2 weeks Frontend + 1 week Backend) confirmed by Rajesh on March 6.
*   **Data Prerequisite:** App team requires a mapping file of customer UID to personalized challenge page URLs. Target delivery was the 1st week of February; BE work commenced March 11 pending alignment.

**Pending Actions & Ownership**
*   **UAT Execution:** Complete User Acceptance Testing by March 24 (Rajesh Dobariya).
*   **Go-Live Confirmation:** Confirm Business Live date with stakeholders post-UAT to finalize launch planning (Owner: Rajesh Dobariya/James Huang).
*   **Data Alignment:** Resolve status of the customer UID mapping file relative to the delayed BE start date and upcoming UAT.

**Key Dates & Timeline**
*   **UAT Date:** March 24, 2026.
*   **Technical Live:** March 30, 2026.
*   **Business Live:** TBD (Pending stakeholder confirmation and UntieNot issue review).
*   **Historical Context:** Initial tentative launch projected for March 2026; data handover target was the 1st week of February.

**Business Context & Impact**
*   **Goal:** Integrate "UntieNot" personalized gamification to drive sales and engagement for 1.8M DCC customers via category and format challenges.
*   **Impact Estimate:** Leveraging a 2023 pilot ($395K/month incremental GMV on ~938K DCC), the initiative projects $8M incremental GMV over 8 months by scaling to ~1.7M DCC with broader challenge formats.
    *   *Calculation:* $1.6M (pilot equivalent) + ($800K x 8 months for doubled audience) = $8M total projection.
*   **Metrics:** Primary focus on Challenge participation and completion rates, impacting Financial Impact and Customer Experience dimensions.

**Blockers/Notes**
*   The discrepancy between the "1st week of February" data target and the March 11 BE start date requires resolution to ensure mapping files are ready for UAT by March 24.
*   Business live date remains unconfirmed; final coordination is critical before the March 30 technical go-live, contingent on resolving any issues identified from UntieNot during UAT.


## jira/OMNI-1420: Enable all 3P domain links to open in the in-app browser from banner redirection
Source: jira | Key: OMNI-1420 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-372 | Last Updated: 2026-03-16T14:03:58.139756+00:00
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
Source: jira | Key: OMNI-1429 | Status: UAT (In Progress) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-710 | Last Updated: 2026-03-19T12:38:39.429015+08:00
**Daily Briefing: OMNI-1429 – Activate Product Ads on Omni Homepage Swimlanes**

**Current Status**
*   **State:** UAT (In Progress).
*   **Priority:** High.
*   **Type:** Idea.
*   **Assigned To/Reporter:** Nikhil Grover.
*   **Related Work Item:** DPD-710 (Polaris work item link).

**Pending Actions & Ownership**
*   **Implementation:** Nikhil Grover is configuring product ad slots via Split to enable dynamic testing of placements [3, 5, and 7].
*   **Technical Scope:** The solution involves setting ad slots in Split, fetching ads based on configured counts, and sequencing products for the frontend. No new app deployment or code changes are required (Effort: 3-4 man days).
*   **Business Logic Update:** As of March 17, "new tech live" and "biz live" dates remain pending confirmation per Danielle Lee's request. All components must be finalized before pitching.
*   **Target Scope:** Ads will activate in slots 3, 5, and 7 across all Omni homepage swimlanes and Vertical Scroll. Previously, ads were limited to slots 1 and 3 within the Past Purchase swimlane only.

**Key Decisions Made**
*   **Strategic Shift:** To maximize monetization while preserving highly relevant products in top slots (1 & 2), ads are pushed to lower-visibility positions (3, 5, and 7). This addresses the current limitation where ads were absent from non-Past Purchase swimlanes.
*   **Configurability:** The RMN Product Manager can now test different placements via Split rather than hard-coding logic. This supports future planning for Project Light.
*   **Operational Impact:** No changes required to existing operational processes, business rules, or go-to-market strategies ("No change").

**Key Dates & Deadlines**
*   **Status Date:** Current status reflects updates as of March 4, 2026 (UAT entry).
*   **Launch Timeline:** Pending confirmation of "tech live" and "biz live" dates per recent request.
*   **Revenue Projections:**
    *   **Annual Goal:** $750K p.a. incremental revenue (GMV/Income).
    *   **2026 Projection:** $312K expected based on a 5-month rollout window post-launch.

**Blockers & Dependencies**
*   **Dependencies:** None identified; the initiative relies on existing mechanisms with no external dependencies.
*   **Stakeholders:** RMN and Products teams face the current limitation of ads not appearing in non-Past Purchase swimlanes, impacting monetization potential.

**Business Impact & Metrics**
*   **Goal:** Maximize monetization from the Omni homepage by utilizing available inventory beyond the first two slots without compromising product relevance.
*   **Metrics:** Expected outcomes include increased ad impressions (from x to y) and clicks (from x to y). Specific numerical values are defined in the problem statement but were not detailed in the source text.


## jira/OMNI-1421: Transition from fixed-tenancy to impressions-based banner delivery model
Source: jira | Key: OMNI-1421 | Status: Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-385 | Last Updated: 2026-03-19T12:38:59.155775+08:00
**Ticket:** OMNI-1421 | **Priority:** High | **Type:** Idea | **Assignee/Reporter:** Nikhil Grover | **Status:** Prioritised (To Do)

### Current Status
The project to transition from a fixed-tenancy model to an impressions-based banner delivery model is in the "Prioritised" phase. The assignee, Nikhil Grover, is finalizing the solution design. This initiative is contingent on the completion of **OMNI-1429** (activation of product ads on Omni homepage swimlanes) and the alignment of Ad Ops and Platform Ops on new SOPs.

### Problem Definition & Opportunity
*   **Current State:** FPG runs display campaigns on fixed slots per week.
    *   **Issue:** All users see identical content, leading to irrelevant exposure and excessive frequency caps that limit campaign variety.
    *   **Impact:** The RMN team is restricted by limited slot availability; Platform/Ecomm cannot deliver personalized content at the right time.
*   **Proposed Solution:** Transition to an impressions-based model where banner sequences are personalized to consumers, maximizing traffic efficiency via frequency capping and relevance.

### Business Impact & Logic
*   **Financial Target:** Projected annual incremental revenue of **$900k**.
    *   **Assumptions:** Current package fill rate is ~60%. Transitioning 70% of package budgets to Product Ads frees up 40% of inventory (12.4m monthly impressions).
    *   **Calculation:** Freed-up inventory at $10 CPM yields $1.5M potential. At a 60% sell-through rate, this results in $900k annual revenue ($124k/month).
*   **Operational Goal:** Enable RMN BD users to run campaigns on an impressions basis to maximize advertiser exposure and sales volume.

### Pending Actions & Ownership
*   **Solution Finalization:** Nikhil Grover must complete the technical definition, ensuring all pitch components (problem statement, goal, metrics) are documented.
    *   **Target Completion:** By March 31, 2026.
*   **Operational Alignment:** Ad Ops and Platform Ops must align on Standard Operating Procedures (SOP) for the new model.
*   **Go-to-Market Preparation:** Update RMN packages to reflect the transition, targeting a start date of April 1, 2026.

### Key Dates & Deadlines
*   **Feb 27, 2026:** Original target for solution finalization (updated).
*   **March 31, 2026:** Revised ETA for completion of OMNI-1421.
*   **April 1, 2026:** Target start date for the new model implementation.
*   **Blocker:** Project cannot commence until **OMNI-1429** is activated.

### Success Metrics (Target)
*   **Financial:** AOV will increase within 6 weeks.
*   **Customer Experience:** Perfect Order rate will increase within 3 months.

### Key Decisions & Dependencies
*   **Strategic Shift:** Moving from a ~60% package fill rate to utilizing freed-up inventory at $10 CPM.
*   **Linked Issue:** Polaris work item **DPD-385**.


## jira/OMNI-1416: FP Pay experience improvements to support new auto apply voucher at IPOS/KPOS 
Source: jira | Key: OMNI-1416 | Status: Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Rajesh Dobariya | Last Updated: 2026-03-17T17:55:42.143767+00:00
**Jira Ticket Summary: OMNI-1416**
**Title:** FP Pay experience improvements to support new auto apply voucher at IPOS/KPOS
**Status:** Prioritised (To Do) | **Priority:** High | **Assignee:** Rajesh Dobariya | **Reporter:** Rajesh Dobariya

**Current State & Strategic Shift**
The initiative addresses compliance risks and UX friction by shifting offer redemption authority from the Offer Service to POS systems (IPOS, KPOS). FP Pay will transition from an execution layer to a "discovery surface" only.
*   **Problem Statement:** Current compliance issues treat vouchers as payment methods; poor UX forces manual selection or "apply all," causing checkout friction and lower utilisation due to lack of cart context in FP Pay.
*   **Architecture Shift:** Digital Center becomes the Single Source of Truth for offers (creation, logic, application). IPOS will fetch eligible offers in real-time and auto-apply them during checkout.
*   **Target UX:** Users scan QR at POS; system identifies user, fetches offers from Digital Center, and auto-applies savings without manual selection.

**Transition & End State**
*   **Interim Phase (July – Sep 2026):** Offer Service continues handling Bank vouchers and EVs due to existing dependencies not yet supported by POS. IPOS handles other in-store offers. FP Pay acts as browse-only for interim offers. Goal: Minimise disruption while shifting redemption authority.
*   **End State (Sep 2026+):** Offer Service is decommissioned. POS becomes the single redemption engine for EVs, Bank vouchers, and all promotional offers. Digital Center owns logic; FP Pay acts purely as discovery/engagement.

**Pending Actions & Ownership**
1.  **Scope Confirmation:** Rajesh Dobariya must double-confirm if this ticket requires tracking given that remaining work is performed by the Core Product Team (Tiong Siong's team) and does not consume OMNI capacity ([2026-03-17]).
2.  **Effort Estimation:** Clarify total effort required for the initiative following Danielle Lee's query regarding resource allocation ([2026-03-17]).
3.  **FS Team Alignment:** Follow up with FS team on final FP Pay experience timeline and effort estimation (Action: [2026-02-19]).
4.  **Executive Alignment:** Align FP Pay experience (RB & Kopitiam) with Koklin and Qiuyan for App Exco review (Action: [2026-02-19]).

**Decisions & Technical Constraints**
*   **Dependency:** App adoption depends on BE completion of DSP integration to fetch vouchers, required before the July launch.
*   **IPOS Coordination:** Align with IPOS on fetching applicable vouchers from DSP based on user profiles.
*   **Blockers:** Pending confirmation on whether OMNI capacity is needed for this work (Core Product Team handling execution).

**Key Dates & Deadlines**
*   **Target Launch Window:** July – September 2026.
*   **Production Go-Live:** Deadline undefined; clarification requested from Sathya Murthy Karthik ([2026-03-11]).

**Notes**
*   Alignment deck and Figma links are referenced but not attached in current summary.
*   Business impact metrics (AOV increase, Perfect Order improvements) remain to be defined.


## jira/OMNI-1163: Enable AI Personalisation Search Capability with Algolia
Source: jira | Key: OMNI-1163 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Erica Lee | Reporter: Erica Lee | migration_parent: OMNI-653 | polaris-work-item-link: PRDM-12 | relates: PRDM-12, OMNI-1312 | Last Updated: 2026-03-19T12:39:17.044864+08:00
**Status Update: OMNI-1163 (Enable AI Personalisation Search Capability with Algolia)**

**Current State**
The initiative remains in the **Ideas** backlog with a **High Priority** and status **To Do**. The ticket is assigned to and reported by **Erica Lee**, relating to migration parent **OMNI-653** and related work items **PRDM-12** and **OMNI-1312**. Progress remains halted due to technical assessment findings regarding upstream data integrations.

**Problem & Opportunity**
FairPrice customers face generic search results that ignore individual preferences (e.g., dietary restrictions, brand loyalty), causing inefficient discovery and potential abandonment. The goal is to dynamically adjust search, promotion, and category listings based on browsing behavior and purchase history.
*   **Projected Impact:** A conservative 2% increase in Search Conversion Rate (CVR) is expected, driving a **$1.6M uplift** in Search GMV against a 2024 baseline of $81.7M, alongside an increase in Overall Average Order Value (AOV).
*   **Validation:** Assumptions are based on Algolia client data showing a 4.5% CTR/CVR gain; FairPrice anticipates measurable improvements with the conservative 2% CVR estimate.

**Key Decisions & Strategic Context**
1.  **Scope Management:** Google Search functionality remains in a separate ticket (**OMNI-1312**) to allow immediate A/B testing, while this ticket focuses on Algolia AI.
2.  **Integration Strategy Shift:** Technical assessment confirms existing integrations are incomplete. The strategy has shifted from minor tweaks to planning optimal integrations via the **Light** platform to resolve upstream data gaps.

**Pending Actions & Ownership**
*   **Platform Migration Planning (Owner: Vivian Lim Yu Qian):** Plan for optimal data integrations via the **Light** platform.
    *   *Critical Technical Findings:*
        1.  **Event Tracking Gaps:** Significant issues identified in frontend-to-Segment flows. Web events frequently miss critical product info, and Android "Product Clicked" events often fail to trigger. AI personalization cannot proceed until these upstream tracking issues are resolved.
        2.  **Logic Refactoring:** Algolia requires a fundamental change to how past purchase items are returned in search results to ensure compatibility with AI logic, requiring significant engineering effort.

**Key Dates & Blockers**
*   **Blockers:** The ticket is blocked by incomplete event tracking (Android/Web) to Segment and the requirement for significant engineering refactoring of past purchase data flows. Progress on Algolia implementation is contingent upon resolving these upstream issues and executing the migration to Light.

**Technical References**
*   **Provider:** Algolia (via CDP/Segment) -> Transitioning to **Light**.
*   **Related Issues:** PRDM-12, OMNI-653 (migration_parent), OMNI-1312.


## jira/OMNI-1419: [Shopbeyond] - Capture all scan events coming from scanning Shop beyond QR code.
Source: jira | Key: OMNI-1419 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Rajesh Dobariya | Last Updated: 2026-03-19T12:39:34.459355+08:00
**Daily Briefing Summary: OMNI-1419 [Shopbeyond] Scan Event Capture**

**Current Status**
*   **State:** Soft Prioritised (To Do).
*   **Type:** Idea.
*   **Assignee/Reporter:** Rajesh Dobariya.
*   **Priority:** High.
*   **Context:** The ticket addresses a critical gap where GMV attribution for Shopbeyond is inaccurate due to reliance on generic GA events with keyword-based page paths rather than dedicated scan events.

**Key Decisions Made**
1.  **Roadmap Removal (2026-03-19):** Rajesh Dobariya aligned with business leadership that the feature will **not be implemented in the current app**.
    *   *Rationale:* Given existing workarounds and resource constraints, the item is being removed from the roadmap entirely. This supersedes the previous 2026-03-16 decision to prioritize the 1HD launch over Shopbeyond tracking; the project is now paused indefinitely.
2.  **Technical Scope (Original Requirement):** The original intent was to trigger a single dedicated Segment event for all Shopbeyond QR scans (internal scanner vs. external mobile camera) with UTM parameters captured at the event level.

**Pending Actions & Ownership**
*   **Action:** Remove OMNI-1419 from the product roadmap.
    *   **Owner:** Rajesh Dobariya / Business Leadership.
    *   **Status:** Completed (Decision recorded 2026-03-19).
*   **Action:** Continue utilizing generic GA proxy events for mobile camera scans until a future solution is defined.
    *   **Owner:** Analytics Team.
*   **Action:** Await potential re-evaluation if resource constraints ease or business needs shift.

**Key Dates, Deadlines & Blockers**
*   **Business Logic Rule:** Any DF order placed within 7 days of scanning a Shopbeyond QR code must be attributed to Shopbeyond GMV (Note: Current implementation does not support this accurately).
*   **Blocker/Constraint:** Resource constraints and the availability of temporary workarounds have led to the project's removal from the current roadmap. No hard deadline exists (Due Date: null).
*   **Reference Link:** Alignment discussion recorded at `https://chat.google.com/room/AAAA9x55r9A/kvcr2p7K8Wg/kvcr2p7K8Wg?cls=10`.

**Impact Assessment**
*   **Business Impact:** Accurate GMV attribution for Shopbeyond remains blocked; the business accepts inaccurate data temporarily due to resource limitations.
*   **Product Metrics:** NA.
*   **Historical Context:** On 2026-01-23, the requirement was formally defined as non-negotiable for accurate attribution, highlighting the critical nature of the problem even though execution is currently halted.


## jira/OMNI-1300: GST Compliance Phase 2 - Refunds and return
Source: jira | Key: OMNI-1300 | Status: Define (In Progress) | Type: Idea | Priority: High | Assignee: Alvin Choo | Reporter: Sathya Murthy Karthik | Labels: GST | polaris-work-item-link: CORE-51, PAY-6725 | Last Updated: 2026-03-19T12:39:54.549623+08:00
**Jira Briefing: OMNI-1300 (GST Compliance Phase 2 - Refunds and Returns)**

**Current Status:** In Progress (Status Category) / Define (Workflow Status). The project is an **Idea** with High priority, focusing on automating GST-compliant refunds for e-commerce and marketplace orders to eliminate manual calculation errors.

**Problem Definition & Scope:**
*   **Business Impact:** Approximately 5% of orders involve returns; current manual tracking leads to incorrect GST calculations in both FairPrice retail and marketplace scenarios. This creates regulatory risk and inefficiencies for E-commerce Operations and Finance Teams.
*   **Target Outcome:** Reduce incorrect GST calculation delta from baseline X% to 0%, eliminating manual adjustments and regulatory exposure.

**Strategic Decisions & Technical Approach:**
*   **Replatform Strategy (Confirmed 5 Jan 2026):** Full "Return and Refund" functionality will be delivered via the upcoming SAP Replatform, not within OMNI-1300's immediate scope.
*   **Interim Solution:** OMNI-1300 focuses on an interim RPA-driven workflow for BCRS pending the Replatform.
*   **Workflow Architecture:**
    *   **Customer Initiation:** Online requests submitted via App to Zendesk; In-store requests directed to a "to-be" refund system.
    *   **Processing Logic:** RPA and Zendesk filter requests based on business rules before sending to the "to-be" refund system (DPD).
    *   **System Integration:** The "to-be" system must generate credit notes, ensure tax-compliant GST calculations, and update downstream systems (SAP, Mirakl, DBP) before notifying RPA to close tickets.
*   **API Requirements:** On 29 Sept (W39), the team identified two critical APIs needed for RPA: "Refund simulation" (pre-confirmation info) and an API to verify if an order+SKU has already been refunded.

**Pending Actions & Ownership:**
*   **Aditi Rathi:**
    *   Share action plan with Corporate Control (CC) and Ecom Business for alignment.
    *   Coordinate final refund calculation meetings with CC and Business.
    *   Confirm API response specifications with PM/Tech teams.
*   **Stakeholders (CC, Finance, Business):**
    *   Attend workshop to align on open items and refund calculations.
    *   Review first draft of Refund Calculations (completed 27 Nov) for sign-off.

**Key Dates & Deadlines:**
*   **10 Dec 2025:** Scheduled meeting with RPA team to share API documentation (Status: Confirmed/Ready).
*   **TBD:** Final alignment meetings with CC and Ecom Business regarding refund calculations.
*   **3 Oct 2025:** Historical deadline for closing comments (superseded by current timeline).

**Blockers & Risks:**
*   **Stakeholder Alignment:** Previous meetings with CC, Business, and Finance were cancelled on 29 Sept; a workshop planned for 10 Oct is pending follow-up. Final alignment is required to proceed.
*   **API Readiness:** RPA logic cannot be finalized until the refund simulation and confirmation APIs are documented (Documentation ready as of 9 Dec).

**Linked Issues:** CORE-51, PAY-6725.
**Assignee:** Alvin Choo | **Reporter:** Sathya Murthy Karthik


## jira/OMNI-1394: [RMN-OFFSITE] - Acquire Customer consent
Source: jira | Key: OMNI-1394 | Status: For Pitching (To Do) | Type: Idea | Priority: High | Assignee: Zi Ying Liow | Reporter: Ravi Goel | polaris-work-item-link: ID-5183 | Last Updated: 2026-03-16T14:05:52.416818+00:00
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
Source: jira | Key: OMNI-1235 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Koklin Gan | Reporter: Koklin Gan | polaris-merge-work-item-link: OMNI-1237 | polaris-work-item-link: DPD-293 | Last Updated: 2026-03-16T14:06:10.335978+00:00
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
Source: jira | Key: OMNI-1153 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Ravi Goel | Reporter: Yadear Zhang | Labels: app-engagement | polaris-merge-work-item-link: OMNI-1152 | Last Updated: 2026-03-16T14:06:28.360123+00:00
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
Source: jira | Key: OMNI-1246 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Ryne Cheow | Reporter: James Huang | polaris-merge-work-item-link: OMNI-1169 | Last Updated: 2026-03-16T14:06:41.531690+00:00
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
Source: jira | Key: OMNI-1361 | Status: Discovery (To Do) | Type: Idea | Priority: High | Assignee: Alvin Choo | Reporter: Gopalakrishna Dhulipati | polaris-work-item-link: PAY-6785 | Last Updated: 2026-03-16T14:06:59.162499+00:00
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
Source: jira | Key: OMNI-1227 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Aditi Rathi | Reporter: Koklin Gan | discovery---connected: OMNI-1075, OMNI-1134 | polaris-merge-work-item-link: OMNI-1075 | Last Updated: 2026-03-17T17:59:18.606661+00:00
**Jira Briefing Summary: OMNI-1227 (FPG - Fraud detect and prevention)**

**Current Status:** Soft Prioritised / To Do. The initiative remains stalled awaiting ownership assignment and business alignment on a real-time fraud engine.

**Key Decisions & Progress:**
*   **Scope Definition:** Focused strictly on Order Management touchpoints to enable transactional surveillance. Explicitly excludes "Onboarding journey changes" (handled separately in Nov 2025).
*   **Mitigation Actions Taken:** E-Voucher redemption for Marketplace items was restricted starting Oct 7, 2025 (phased rollout) as an interim compliance measure.
*   **Proposed Solution:** Implementation of a real-time Fraud Engine (ML/Rule-based) integrated with OMS.
    *   **Logic:** Score transactions as LOW (auto-pass), MEDIUM (flag for review), or HIGH (instant block).
    *   **Backoffice Portal:** Required for CS/Business to approve/reject flags, whitelist customers, and generate reports.
*   **Effort Estimates (High):**
    *   **DS Team:** 8 weeks (building engine/rules).
    *   **DE Team:** TBD (connecting DS-OMS endpoints).
    *   **DPD Fulfilment:** 4 weeks (orchestrating journey & building backoffice; requires 1 BE, 3 FE).

**Pending Actions & Ownership:**
*   **Ownership Transfer:** Status remains unassigned. Danielle Lee flagged on Feb 13, 2026: "Who will be the new owner for this ticket?" Aditi Rathi (Assignee) is still targeted to present tech options but lacks active engagement since Dec 2025.
*   **Strategic Focus Update:** On March 17, 2026, Koklin Gan clarified the scope must focus strictly on **"transactional surveillance."**
*   **Technical Proposal:** Aditi Rathi targets presenting potential tech options and securing business alignment by Oct 15 (original target); this date is now obsolete due to inactivity.
*   **Brainstorming Session:** Planned meetings with DS and Tech teams to finalize the "To-Be" solution are pending.

**Key Dates & Blockers:**
*   **Last Update:** March 17, 2026 (Scope refinement by Koklin Gan) / Feb 13, 2026 (Ownership query).
*   **Historical Deadlines Missed:** Oct 15, 2025 (Alignment); Dec 2, 2025 (AOP update request).
*   **Blockers:**
    *   Lack of designated ticket owner since Feb 2026.
    *   Unresolved SLO impact regarding order placement latency from routing all transactions through the engine.
    *   Need for explicit business alignment on high-effort engine vs. current manual RPA processes.

**Context & Problem Statement:**
*   **Linked Issues:** OMNI-1075 (Discovery), OMNI-1134 (Discovery).
*   **Risk Profile:** Driven by the Risk team (Larry Pee). Risks include Voucher Abuse ($100k annual potential loss), Stolen Card usage (~3,200 alerts/year), and Account Takeover.
    *   *Stats:* 27 incidents with 90 transactions cancelled manually between April-July 2025. $0 financial liability so far due to Liability Shift ($200 threshold), but high reputational risk exists for chargebacks under this threshold.
*   **Current Process:** Relies on a manual RPA mechanic generating ~1 alert/day and seller notifications. Requires 2-3 hours/week per team (Ecom Business + CS) for investigation, call confirmation, and cancellation.
*   **Goal:** Automate prevention before fulfillment to reduce operational overhead and eliminate chargeback risks.


## jira/OMNI-1208: Mirakl foundational work for scalability
Source: jira | Key: OMNI-1208 | Status: Discovery (To Do) | Type: Idea | Priority: High | Assignee: Koklin Gan | Reporter: Koklin Gan | blocks: DST-2247 | discovery---connected: OMNI-1178 | polaris-work-item-link: DST-2247, DPD-326, DPD-332, DST-2277, DPD-543, DST-2305 | Last Updated: 2026-03-16T14:07:37.295043+00:00
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
Source: jira | Key: OMNI-1242 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Fiona U | Labels: Preorder | polaris-work-item-link: PA-330 | Last Updated: 2026-03-16T14:07:55.395230+00:00
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
Source: jira | Key: OMNI-1282 | Status: Define (In Progress) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-296 | Last Updated: 2026-03-16T14:08:10.793594+00:00
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
Source: jira | Key: OMNI-1334 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Prajney Sribhashyam | Last Updated: 2026-03-16T14:08:26.609544+00:00
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
Source: jira | Key: OMNI-1234 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Koklin Gan | Reporter: Koklin Gan | polaris-work-item-link: DPD-543 | Last Updated: 2026-03-19T12:40:10.679982+08:00
**Daily Briefing Summary: OMNI-1234 (White Label Invoice Generation for MP)**

**Current Status & State**
*   **Ticket Status:** Backlog (To Do); Issue Type: Idea.
*   **Priority:** High.
*   **Assignee/Reporter:** Koklin Gan.
*   **Linked Issues:** Polaris work item link **DPD-543**.

**Key Decisions & Strategic Shifts**
*   **Problem Definition (2025-04-16):** Established that current invoices branded under FairPrice (FP) for seller-fulfilled orders cause customer confusion and misrepresent the seller's brand. The objective is to enable white-labeling where the Seller is the issuing entity to support a true marketplace experience.
*   **Approach Confirmation:** No re-evaluation regarding B2B/B2C deferral was noted in the new input; the focus remains on enabling the feature via one of two technical paths, contingent on GST compliance.

**Technical Context & Blockers**
*   **Core Problem:** Brand misrepresentation for seller-fulfilled orders under the current FP branding.
*   **Solution Options Discussed:**
    *   *Option 1 (DBP):* Generate white-label invoices on DBP. Requires completion of GST compliance and data flow integration of seller information (name, info, logo) into DBP.
    *   *Option 2 (Mirakl):* Generate white-label invoices on Mirakl. Requires completion of GST compliance and streamlining sales data flow to Mirakl for configuration.
*   **Primary Blocker:** GST compliance must be completed before either solution path can proceed.

**Pending Actions & Ownership**
1.  **GST Compliance Completion:** Prerequisite for both DBP and Mirakl generation options.
    *   *Owner:* Koklin Gan (Reporter/Assignee).
2.  **Data Flow Integration:**
    *   For Option 1: Ensure seller info flows into DBP.
    *   For Option 2: Streamline sales data flow to Mirakl.
3.  **Implementation Planning:** Define specific design and configuration steps based on the selected path (DBP vs. Mirakl).

**Key Dates & Deadlines**
*   **16 Apr 2025:** Ticket creation and problem definition logged by Koklin Gan.
*   *(Note: Previous dates regarding Finance alignment in Sep/Oct 2025 have been removed as the new content reflects an earlier stage of project initiation without those specific historical milestones).*

**Summary of Immediate Next Steps**
Proceed with finalizing the technical path (DBP vs. Mirakl) pending GST compliance completion, as verified by Koklin Gan in the initial problem definition.


## jira/OMNI-1250: Customer Account Merging & Deduplication via LEAP middleware
Source: jira | Key: OMNI-1250 | Status: Discovery (To Do) | Type: Idea | Priority: High | Assignee: Ryne Cheow | Reporter: James Huang | polaris-work-item-link: CPR-86 | Last Updated: 2026-03-19T12:40:29.283398+08:00
**Ticket Summary: OMNI-1250 (Customer Account Merging & Deduplication via LEAP)**

**Current Status**
*   **Status:** Discovery (To Do) | **Priority:** High | **Assignee:** Ryne Cheow
*   **Latest Update (2026-03-19):** Sathya Murthy Karthik confirmed during weekly epics that this initiative is being **removed from the roadmap**.

**Problem Definition & Baseline**
*   **Objective:** Consolidate 1.5M+ duplicate customer records (reducing active records from 3.6M to 2.1M) caused by fragmented sign-ups (email vs. phone).
*   **User Pain Point:** Returning shoppers face fragmented loyalty points, vouchers, and order history with no in-app self-service merge option; currently forced to contact support.
*   **Business Impact:** Inaccurate member counts, ineffective governance for rewards/fraud prevention, and operational inefficiencies with partners (Trust/Union).
*   **Success Metrics:** Reduction of active records, lower reconciliation incidents with Trust/Union, and fewer support tickets regarding lost points.

**Strategic Context & Decisions**
*   **Original Scope:** Initially proposed an in-app merge flow via LEAP middleware within "Project Light" (New App) to secure user consent for merging accounts.
    *   *Reference:* Linked Polaris item **CPR-86**.
*   **Scope Refinement (2025-08-20):** Ravi Goel previously proposed splitting tracks into "New-New Customers" (Singpass-based) and "Existing Customers" (requiring creative impact testing).
*   **Timeline Adjustment (2025-06-13):** Merging was excluded from the LEAP September launch, planned for post-stabilization.
*   **Key Assumption:** The solution relies on the new LEAP Middleware's capability to handle complex logic at scale and successful integration of offers/order history without data loss.

**Pending Actions & Ownership**
*   **Roadmap Removal:** No further execution or prioritization is required as the item has been officially removed from the roadmap (Update: 2026-03-19).
*   **Archival:** Maintain historical record of the "Project Light" integration plan and CDM cutover dependencies for reference only.

**Historical Context (Retained)**
*   **Technical Baseline:** 3.6M active records currently exist; partial backend solution ("Project Marvel") exists but lacks in-app consent flows.
*   **Dependencies:** Previously dependent on production cutover to the new Customer Data Model (CDM).

**Key Dates & Deadlines**
*   **12-Month Goal:** Target reduction from 3.6M to 2.1M records (now cancelled due to roadmap removal).
*   **2025-09 (September):** LEAP launch where merge functionality was explicitly excluded.
*   **2026-03-19:** Decision made to remove OMNI-1250 from the roadmap.


## jira/OMNI-1157: Adopting the CDM Golden Record in the FPG App (and Phase out FPOn ID)
Source: jira | Key: OMNI-1157 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Ryne Cheow | Reporter: James Huang | Labels: Q2-2025, new_LMS | polaris-merge-work-item-link: OMNI-1174 | polaris-work-item-link: DPD-544 | Last Updated: 2026-03-19T12:40:50.510306+08:00
**Jira Ticket Summary: OMNI-1157**

**Current Status:**
**Removed from Roadmap**. Originally a High Priority **Idea** in the Backlog assigned to **Ryne Cheow** and reported by **James Huang**, this ticket was officially deprecated on **March 19, 2026**. As confirmed by **Daryl Ng**, the scope of adopting the CDM Golden Record is now designated for the "new app," rendering this specific ticket obsolete. It is linked to Polaris work item **DPD-544** and merge item **OMNI-1174**.

**Problem & Scope:**
The initiative aimed to resolve data fragmentation impacting ~4.28M active users (FairPrice Online/DCC: ~1.6M; Link Rewards: ~2.5M; JWC: ~180K). The goal was to replace legacy IDs (Linkpass, FPOn) with a CDM Golden Record to enable seamless cross-service experiences and accurate analytics.
*   **Baseline:** 0% CDM UID Adoption Rate in FPG App.
*   **Target:** 100% adoption for QR codes and platform services by Q2 2026, consolidating over 2.5M profiles.

**Proposed Technical Strategy (Historical):**
The project outlined six user stories:
1.  Embed CDM UID in Core Platform (DBP & DPD services).
2.  Profile synchronization via the FPG App.
3.  Analytics SDK integration for behavior tracking.
4.  QR Code refactoring to embed CDM UID.
5.  Phase-out of legacy IDs from codebases.
6.  Salesforce Marketing Cloud (SFMC) SDK updates using LEAP Middleware APIs.

**Validation & Assumptions:**
Work was aligned with the "Project LEAP Architectural Blueprint." Key assumptions included the stability of the foundational CDM platform ("GoldenUser" table) and the availability of LEAP Middleware APIs for UID formatting and service integration.

**Decisions Made:**
*   **Architectural Shift (March 19, 2026):** Confirmation received that CDM adoption belongs in the "new app." Consequently, this ticket has been removed from the roadmap to prevent resource misallocation on legacy architecture tasks.
*   **Risk Mitigation (Historical):** Prior to deprecation, a critical query raised by **Fiona U** on May 6 flagged potential timeline spillover into Q3 due to effort estimates exceeding the initial Q2-2025 label, contradicting the Q2 2026 delivery target. This schedule conflict was superseded by the decision to pivot scope to the new application.

**Key Dates & Blockers:**
*   **Timeline Target (Original):** Q2 2026 for 100% adoption.
*   **Deactivation Date:** March 19, 2026.
*   **Labels:** Q2-2025, new_LMS (Note: These labels now reflect the historical context of a cancelled initiative rather than current active planning).

**Summary:**
The project to adopt the CDM Golden Record in the legacy FPG App has been terminated. While the technical strategy was well-defined with multiple tribe estimates and aligned with Project LEAP, the strategic decision to execute this unification within the "new app" (confirmed by **Daryl Ng**) renders OMNI-1157 obsolete. No further action is required on this ticket.


## jira/OMNI-1389: [POC] Enabling PalmPay to allow quick checkout
Source: jira | Key: OMNI-1389 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Sathya Murthy Karthik | Reporter: Koklin Gan | Last Updated: 2026-03-16T14:09:28.771964+00:00
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
Source: jira | Key: OMNI-1390 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Sathya Murthy Karthik | Reporter: Koklin Gan | Last Updated: 2026-03-16T14:09:41.314413+00:00
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
Source: jira | Key: OMNI-1353 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Aditi Rathi | Reporter: Gopal Singh | polaris-work-item-link: ENGM-2474 | Last Updated: 2026-03-16T14:10:01.460354+00:00
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
Source: jira | Key: OMNI-1179 | Status: Paused (To Do) | Type: Idea | Priority: High | Assignee: Alvin Choo | Reporter: Alvin Choo | Labels: Foundation | polaris-work-item-link: CART-54 | Last Updated: 2026-03-19T12:41:22.546504+08:00
**Jira Ticket Briefing: OMNI-1179 – Compliance: Improving Cart Calculation Logic**

**Current Status**
*   **State:** Paused (Category: To Do).
*   **Type:** Idea.
*   **Priority:** High.
*   **Assignee/Reporter:** Alvin Choo.
*   **Labels:** Foundation.
*   **Linked Issues:** CART-54.

**Context & Problem Definition**
The initiative aims to resolve inconsistencies in pricing, promotions, and tax (GST) calculations across channels (online, in-store, Scan & Go, marketplace). Currently, the fragmented architecture causes checkout discrepancies, manual GST adjustments by Finance, and high engineering maintenance costs. Success metrics include improved cart-to-checkout consistency, reduced abandonment due to pricing errors, and faster implementation of new pricing rules.

**Key Decisions & Scope Changes**
*   **Scope Reduction (2025-11-27):** Aligned with the App Replatform strategy, the scope was narrowed to exclude complex "Sales and drop-off calculations." The remaining deliverables are strictly:
    1.  CRUD operations for core cart services.
    2.  Basic Cart calculation logic.
*   **Category Shift:** Aditi Rathi (2025-11-27) confirmed reclassification to **Platform Health** due to the reduced scope and alignment with replatforming.
*   **Dependency Confirmation:** The project contributes to "Shoppable grocery in Omni Home," "GST project," "Replatform - splitting of orders/transactions," "Scan & Go splits," and "Scaling of marketplace."

**Pending Actions & Ownership**
*   **Requirement Validation (New):** Sathya Murthy Karthik raised a critical query on **2026-03-19**: Determine if this ticket is still required for the *current app*, given the replatform pivot. This status check supersedes previous discussions regarding September 2025 GST meetings or October resourcing concerns.
*   **Resourcing & Timeline:** No formal resolution exists on resource allocation or the feasibility of a December delivery goal, as raised by Winson Lim (2025-10-22). With the new validation check in March 2026, the previous "Pending ETA" for remaining calculation logic remains unresolved.

**Key Dates & Blockers**
*   **Last Update:** 2026-03-19 (New validation request by Sathya Murthy Karthik).
*   **Previous Development Status:** WIP as of Week 38 (Sept 2025) and Week 35 (Aug/Sept 2025).
*   **Blockers:**
    *   **Critical Uncertainty:** Pending confirmation from Sathya Murthy Karthik regarding the necessity of this work for the current app versus the replatform.
    *   Lack of clear ETA for remaining calculation logic post-scope reduction.
    *   Unresolved resourcing constraints raised by Winson Lim regarding year-end delivery.

**Summary for Briefing**
OMNI-1179 was originally a High Priority Idea to unify cart logic for GST compliance and cross-channel consistency. Scope was significantly reduced on 2025-11-27 to focus only on CRUD services and basic calculations, shifting the category to "Platform Health" in alignment with the App Replatform. While development was WIP through September 2025, the project faces a critical juncture following Sathya Murthy Karthik's **March 19, 2026** inquiry: whether this work is required for the *current app*. Previous concerns regarding resourcing and December delivery deadlines remain open. The pending validation on the necessity of this ticket effectively pauses further action until the "App Replatform" strategy clarifies requirements for existing systems.


## jira/OMNI-1247: [OSMOS only] Integrate fit-for-purpose digital signage with OSMOS for in-store ad activation
Source: jira | Key: OMNI-1247 | Status: Define (In Progress) | Type: Idea | Priority: High | Assignee: Yi Hao Tan | Reporter: Nikhil Grover | Last Updated: 2026-03-19T12:41:44.684906+08:00
**Jira Ticket Briefing: OMNI-1247**

**Current Status**
*   **Ticket:** OMNI-1247 [OSMOS only] Integrate fit-for-purpose digital signage with OSMOS for in-store ad activation.
*   **State:** Define (In Progress).
*   **Type:** Idea | **Priority:** High.
*   **Owner/Assignee:** Yi Hao Tan (Reassigned 2026-03-19 as ROOH lead).
*   **Reporter:** Nikhil Grover.

**Key Context & Opportunity**
The project addresses the fragmentation of current digital screen management (two CMS systems for FP and FS screens, plus disconnected screens) and the inability to advertise on in-store digital displays despite 90% of transactions occurring there. Currently, campaigns are planned via email and managed across two CMSs, requiring manual proof-of-play (physical photos).
*   **Goal:** Consolidate campaign booking, viewing, and management within OSMOS to allow advertisers to influence shoppers at the point of purchase.
*   **Retail Media GMV Targets:** 2025: $60K; 2026: $1.4M; 2027: $3M.
*   **Success Metrics:** Fill rate, Cost per 1000 ad slots (CPM), total ad slot volume, and monetized slot percentage.

**Decisions Made & Validation Strategy**
*   **Validation Method:** A Proof of Value (PoV) exercise with vendor **Advertima** is required before roadmap prioritization.
*   **Assumptions:** Data insights regarding assumptions need to be fully documented and validated.
*   **Reassignment Context:** Ticket reassigned on 2026-03-19 to Yi Hao Tan (ROOH lead) following a request from Nikhil Grover.

**Pending Actions & Owners**
1.  **Define Next Steps:** Sathya Murthy Karthik requested an update on next steps for this ticket (as of 2026-03-19). This remains the immediate priority for the new assignee, Yi Hao Tan.
2.  **Execute PoV Exercise:** Oversight of the Proof of Value assessment with Advertima is required to validate the digital signage system.
    *   *Note:* Previous dates (End of Feb 2026 / March 2026) are now superseded by the current "Define" status and the latest reassignment in March 2026; specific revised timelines for the PoV must be established during the immediate next steps.
3.  **Solution Design:** A joint workshop between FPG and OSMOS teams is required to finalize the solution design, contingent on the validation strategy update.

**Key Dates & Deadlines**
*   **Latest Update:** 2026-03-19 (Reassignment and request for next steps).
*   **PoV Completion:** To be defined based on updated roadmap prioritization.
*   **PoV Results Reporting:** To be defined post-PoV execution.

**Blockers/Notes**
*   No specific technical blockers reported; the project is currently in the definition and validation phase.
*   The manual nature of current proof-of-play processes highlights the urgency for automation.
*   Historical context regarding the "Nov 27" workshop date is no longer applicable given the March 2026 reassignment and status update; new timelines must be set.


## jira/OMNI-1391: Available to Promise 1.0 [MVP] - New Time-based Inventory logic
Source: jira | Key: OMNI-1391 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Sathya Murthy Karthik | Reporter: Prajney Sribhashyam | Last Updated: 2026-03-19T12:43:02.452559+08:00
**Ticket:** OMNI-1391 | **Title:** Available to Promise 1.0 [MVP] - New Time-based Inventory logic
**Status:** Soft Prioritised (To Do) | **Type:** Idea | **Priority:** High
**Assignee:** Sathya Murthy Karthik | **Reporter:** Prajney Sribhashyam

**Current State & Problem Definition**
The FPG application relies on a "Global Reservation Logic" that blocks all Stock on Hand (SOH) immediately upon order placement, regardless of the future delivery date. This causes:
*   **False Stock Outs:** Items marked unavailable despite sufficient stock for the specific delivery window (e.g., 24–48 hours ahead).
*   **Premature Reservation & Wastage:** Stock near expiry remains "Reserved" for future slots, preventing immediate sale to reduce shrinkage.
*   **Operational Inefficiency:** Manual intervention required to "cheat" the system and release stock.
**Impact:** Impacts 2.4% of impressions on average (up to 8.9% pre-CNY); estimated annual GMV loss ~$5M with a target recovery of $5.5M.

**Proposed Solution & Scope**
*MVP Scope:* Strictly PFC items and selected SKUs only.
*   **Replenishment Patterns:** Manual presetting of SKU-level addition patterns by timeslot (e.g., +200 qty arriving 11am, +2hr buffer = available 1pm).
*   **Slot Mapping:** Configurable mapping linking delivery slots to specific inventory reference points (e.g., 8am slot uses previous day's 8pm stock).
*   **Forward-Looking Logic:** Toggle calculation for SKUs using: *SOH by timeslot = Previous SOH + Preset Replenishment - Variance - Reservation*. Calculations occur in 2-hour blocks for the next 7 days.
*   **Indexer Workaround:** Apply "Unlimited SKU" logic to prevent PLP disappearance due to outdated counts.
**Known Limitations:** No system visibility on batch-level expiry/write-offs; risk of stock shortfall if unlogged write-offs occur.

**Key Metrics & Goals**
*   **Goals:** Increase Sales-weighted Availability (SWA), Add-to-Cart (ATC), Average Order Value (AOV), and E2E conversion while reducing shrinkage.
*   **Target Audience:** Customers planning deliveries days in advance for essential items.

**Pending Actions & Ownership**
*   **Action:** Monitor alignment with HIVE/middleware teams to prevent duplicated effort; confirm effort estimation (S or XS) remains required.
*   **Owner:** Sathya Murthy Karthik.
*   **Context:** Prajney updated metadata on 2025-10-15. Danielle Lee requested effort confirmation on 2025-11-04. As of 2026-03-19, Yi Hao Tan confirmed implementation scope and direction remain fluid pending alignment with the HIVE team.

**Decisions & Strategy**
*   **Strategy:** Proceed with a controlled pilot for PFC/Selected SKUs to validate GMV improvement. Full deployment depends on successful ATP validation.
*   **Current State:** Implementation scope is fluid; development must align with the HIVE/middleware team roadmap.
*   **Reference Materials:** BRD Document, Solution Discussion, Calculation logic Google Sheet available.

**Dates & Blockers**
*   **Last Activity:** 2026-03-19 (Yi Hao Tan: Scope alignment update).
*   **Blocker:** Pending "S/XS" effort estimation and finalization of scope alignment with HIVE team.
*   **Deadlines:** No due date; timeline dependent on effort confirmation and middleware alignment.


## jira/OMNI-1393: Enabling User Consent for customer data
Source: jira | Key: OMNI-1393 | Status: Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Zi Ying Liow | Reporter: Zi Ying Liow | Last Updated: 2026-03-16T14:11:09.309451+00:00
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
Source: jira | Key: OMNI-1395 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Koklin Gan | Reporter: Sip Khoon Tan | polaris-work-item-link: CART-191 | Last Updated: 2026-03-19T12:43:19.330328+08:00
**Daily Briefing Summary: OMNI-1395 – Improving the Empty Shopping Cart Experience**

**Current Status/State**
*   **Ticket ID:** OMNI-1395 (Idea, Priority: High)
*   **Status:** Backlog (Category: To Do)
*   **Assignee:** Koklin Gan (Updated by Sathya Murthi Karthik on 2026-03-19)
*   **Reporter:** Sip Khoon Tan
*   **Linked Issue:** CART-191 (Polaris work item link)

**Pending Actions & Ownership**
*   **Section Completion:** Populate "Operational Processes," "Business Plans," and "Business Rules/Logic" sections before pitching.
    *   *Owner:* Sip Khoon Tan (Initial instruction on 2025-10-30).
*   **Asset Integration:** Add delivery ticket and Figma link to the main description as requested.
    *   *Owner:* Sip Khoon Tan (Requested on 2025-10-31; links provided by Peter Talbot on 2025-10-31 but pending integration).

**Decisions Made & Scope Confirmation**
*   **Feature Scope:** Confirmed inclusion of personalized product recommendations (sourced from browsing history, purchase history, or trending items) and a "1-click Add to Cart" capability directly on the empty cart page.
*   **Strategic Goal:** Shift navigation from a "dead-end" model ("Start Shopping" button) to an engagement model to increase impressions, ATC actions, and reduce exit rates for 40K Weekly Active Users (WAUs).
*   **Projected Impact:** Targeting an 80k increase in total product impressions, reducing exit rates, and achieving TBD percentage uplifts in ATC rate and CTR.

**Key Dates & Blockers**
*   **Timeline:** No due date assigned yet.
*   **Blockers/Dependencies:** Ticket cannot advance out of Backlog until content sections (Operational Processes, Business Plans, Rules) are finalized.
*   **Recent Activity Log:**
    *   2025-10-30T16:57: Initial ticket creation by Sip Khoon Tan; problem definition and solution summary drafted.
    *   2025-10-31T09:48: Request for delivery/Figma links made; Peter Talbot provided links later that day.
    *   2026-03-19T11:34: Ownership updated by Sathya Murthi Karthik.

**Note on Metrics:**
The user base is confirmed as **40K Weekly Active Users (WAUs)**, not Monthly Active Users, based on the original ticket description drafted in October 2025.


## jira/OMNI-1398: Extend offsite ad placement to Google 
Source: jira | Key: OMNI-1398 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | Last Updated: 2026-03-19T12:43:36.569926+08:00
**Daily Briefing Summary: OMNI-1398**

**Current Status**
*   **Ticket ID:** OMNI-1398
*   **Title:** Extend offsite ad placement to Google
*   **Status:** Backlog (To Do) — *Pending Deprioritization Sign-off*
*   **Type:** Idea
*   **Priority:** High (Historical) / *Pending Official Update*
*   **Assignee/Reporter:** Nikhil Grover

**Pending Actions & Ownership**
*   **Owner:** Nikhil Grover.
*   **Critical Update:** As of March 19, 2026, the assignee has flagged this initiative as "not a current priority for the business." A formal sign-off to deprioritize is currently required.
*   **Completion Requirements (Pre-Deprioritization):** The original requirement to fully populate the ticket before pitching remains valid if the project were to proceed. Key missing sections include:
    *   **Problem Definition:** Needs specific user story templates for FPG RMN sales teams leveraging 1st party data, as well as quantification of affected users (estimated count/% and severity).
    *   **Goals & Metrics:** Incremental RMN revenue remains "TBC." Product metrics (AOV targets, Perfect Order rates) and business logic are undefined.
    *   **Operational Planning:** No details on budget approvals, Google vendor alignment, or go-to-market strategies exist.

**Decisions Made**
*   **Context:** The initiative aims to shift from a single-channel Meta offering to a multi-channel approach including Google to capture additional offsite spend.
*   **New Decision (2026-03-19):** Nikhil Grover has determined the project is not a current business priority and initiated the process for official sign-off to deprioritize.
*   **Historical Context:** The ticket serves as an initial idea capture originally dated November 4, 2025.

**Key Dates & Blockers**
*   **Deadlines:** No due date assigned (`null`).
*   **Blockers:**
    *   Primary: Lack of official sign-off to deprioritize following the March 19, 2026 review.
    *   Secondary (if active): Missing business case data (Problem Definition, Impact Quantification, Metrics).
*   **Context:** Current ad offering is limited to Meta; this initiative targets FPG RMN Business Development and Performance Marketing teams.

**Technical & Reference Notes**
*   The ticket outlines a requirement for sales teams to utilize First Party Data for advertiser acquisition on the Google platform.
*   Proposed Success Metrics: Number of advertisers booking offsite campaigns and total Google offsite campaign volume.
*   **Timeline:** Initial draft created 2025-11-04; Priority status review conducted 2026-03-19.


## jira/OMNI-1399: Extend offsite ad placement to Tiktok
Source: jira | Key: OMNI-1399 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | Last Updated: 2026-03-19T12:43:53.056004+08:00
**Daily Briefing Summary: OMNI-1399**

**Ticket Overview**
*   **ID:** OMNI-1399
*   **Title:** Extend offsite ad placement to Tiktok
*   **Status:** Backlog (To Do) | **Priority:** High (Pending Deprioritization)
*   **Assignee/Reporter:** Nikhil Grover
*   **Type:** Idea

**Current State & Key Dates**
As of **2025-11-04**, the initiative was defined as a strategy to expand FPG's offsite ad capabilities from Meta-only to include TikTok, leveraging first-party data. The ticket remains in the **Backlog** phase with no assigned due date. However, on **2026-03-19**, Nikhil Grover flagged that this is not currently a business priority and initiated the process for official sign-off to deprioritize.

**Proposal Details & Requirements**
Prior to any potential pitch or advancement, the following components must be formalized:
*   **Problem Definition:**
    *   *Shopper:* Amend orders/avoid multiple deliveries after forgetting items.
    *   *FPG RMN Sales Team:* Leverage first-party data to capture additional offsite spend (currently limited to Meta).
*   **Impact Analysis:** Requires estimated user volume and severity assessment for FPG Business Development and Performance Marketing teams.
*   **Goal Quantification:** Incremental RMN revenue is currently marked TBC pending business case finalization.
*   **Metrics Setup:** Needs baseline vs. target definitions for:
    *   Financial Impact (AOV increase timeline).
    *   Customer Experience (Perfect Order rates).
    *   Campaign Volume (Advertisers and campaigns booked on TikTok).
*   **Operational & GTM Planning:** Requires vendor alignment, budget approvals, internal workflows, and go-to-market strategies.

**Decisions Made**
*   **Strategic Direction:** The core goal was identified as shifting from "Meta-only" to offering TikTok as an offsite channel.
*   **Priority Status Change:** As of **2026-03-19**, the ticket is awaiting official sign-off to be **deprioritized** due to a lack of current business priority. No final decisions on implementation or resource allocation have been recorded, as the initiative has effectively stalled pending this formal status change.

**Blockers & Constraints**
*   **Strategic Alignment:** The primary blocker is now the decision to deprioritize; no further work should proceed without official sign-off.
*   **Data Gaps:** Specific revenue targets and AOV improvement metrics remain undefined.
*   **Operational Readiness:** Vendor alignments, budget approvals, and internal workflows for TikTok integration have not been initiated.


## jira/OMNI-1400: Integrate camera/sensor module to track store footfall and impressions on in-store digital screens
Source: jira | Key: OMNI-1400 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Yi Hao Tan | Reporter: Nikhil Grover | Last Updated: 2026-03-19T12:44:09.876912+08:00
**Daily Briefing Summary: OMNI-1400**

**Current Status**
*   **Ticket:** OMNI-1400
*   **Type:** Idea (Backlog / To Do)
*   **Priority:** High
*   **Status Category:** Ready for execution planning.
*   **Last Updated:** 2026-03-19

**Key Context & Problem**
The RMN BD team currently sells in-store digital ad slots by unit (15-second plays) without performance benchmarks regarding actual shopper view counts. This lack of data creates friction in media planning and reporting, making it difficult to demonstrate campaign impact. The objective is to transition from selling "ad units" to selling based on "impressions."

**Proposed Solution**
Integrate camera/sensor modules to track store footfall and screen impressions. This provides advertisers/RMN BD users with:
*   Total shopper view counts per store and time slot.
*   Demographic breakdowns (age, gender, customer segment).
*   Performance baselines for future campaign planning.

**Action Items & Ownership**
*   **Primary Owner:** Yi Hao Tan (Reassigned on 2026-03-19; previously Nikhil Grover)
*   **Reporter:** Nikhil Grover
*   **Pending Actions:**
    *   Finalize component inputs required before pitching the solution to stakeholders.
    *   Define specific operational dependencies, vendor alignments, and budget approvals for camera/sensor integration.
    *   Establish technical baselines for impression and footfall tracking at the screen/store level.

**Decisions & Metrics**
*   **Decision:** The ticket is currently in the ideation/backlog phase, awaiting full problem definition validation. No formal execution decisions recorded yet.
*   **Target Metric:** Transition from ad-play sales to impressions-based sales; establish baselines on impressions and footfall at the screen/store level.
*   **Financial Impact:** Potential revenue of ~$2m/year for in-store RMN.
*   **Product Goal:** Enable forecasting for campaign planning and performance benchmarking.

**Dates, Deadlines & Blockers**
*   **Due Date:** None set (Backlog status).
*   **Blockers:** The ticket notes "Ensure all components are filled in before pitching," indicating that the current lack of detailed problem definition and operational process documentation is preventing progression to development or sales rollout. No technical blockers identified yet as this remains an idea stage.

**Historical Context & Updates**
*   **2025-11-04:** Initial ticket creation by Nikhil Grover; defined the user story for RMN BD users to track impressions and demographic breakdowns.
*   **2026-03-19:** Ticket reassigned to Yi Hao Tan, who is noted as leading ROOH (Retail Owned Outdoor).


## jira/OMNI-1402: Support 'default search' ad format in the search bar through OSMOS
Source: jira | Key: OMNI-1402 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-3, DPD-299 | Last Updated: 2026-03-19T12:44:26.103393+08:00
**Daily Briefing: OMNI-1402 Support 'default search' ad format in the search bar through OSMOS**

*   **Current Status:** The ticket is an **Idea** with a status of **"Soft Prioritised"** and category **"To Do"**. It holds a **High** priority.
*   **Ownership:** Assigned to and reported by **Nikhil Grover**.
*   **Linked Work Items:** Connected to Polaris items **DPD-3** and **DPD-299**.

**Problem & Goal**
Ad Ops users currently must manually set up the 'default search' ad format via Platform Ops in DBP Backoffice, as OSMOS lacks native support. Consequently, the RMN BD team and advertisers receive no performance reports for this specific format within FPG RMN campaigns, creating a fragmented experience. The objective is to enable centralized booking of all package ad formats (including default search) directly within OSMOS, ensuring timely post-campaign reporting for all assets in a single location.

**Key Dates & Deadlines**
*   **Creation Date:** 2025-11-04
*   **Last Update:** 2026-03-19
*   **Due Date:** None set (null).

**Pending Actions**
The ticket structure now contains a defined problem statement and goal, but critical planning sections remain incomplete. Pending actions include:
1.  Completing empty templates for "Solution Summary," "Business Impact," "Product Metrics Impact," "Operational Processes," and "Business Plans."
2.  Quantifying business impact (GMV, income) and defining product metrics (e.g., AOV increase from $X to $Y within 6 weeks; Perfect Order rates).
3.  Establishing baseline impression and click-through rate metrics for default search.
4.  Finalizing operational dependencies and Go-to-market strategies.

**Decisions & Blockers**
*   **Decisions:** On **2026-03-19**, it was decided that the initiative requires no approval for external resources at this time; work will be picked up once resources become available. The ticket is now considered "ready" pending resource availability.
*   **Blockers/Dependencies:** Execution is currently contingent on resource availability rather than requirement definition. While the conceptual gap and user story ("As Ad Ops user...") are defined, development or configuration has not commenced.

**Historical Context**
The initiative originated from the need to bridge workflow gaps between Ad Ops and OSMOS capabilities. The initial creation focused on addressing the lack of reporting for default search formats in FPG RMN campaigns.


## jira/OMNI-1403: Support 'generic/suggested search' ad format in the search bar through OSMOS
Source: jira | Key: OMNI-1403 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-3, DPD-299 | Last Updated: 2026-03-19T12:44:44.372588+08:00
**Daily Briefing: OMNI-1403 – Generic/Suggested Search Ad Format via OSMOS**

*   **Current Status:** The ticket remains in the **"To Do"** stage with a status of **"Soft Prioritised."** It is classified as an **Idea** (High Priority).
*   **Ownership & Assignee:** **Nikhil Grover** serves as both reporter and assignee.
*   **Pending Actions:** While the description outlines the problem statement, critical sections remain empty or require specific data:
    *   **Solution Summary:** The "As a... So I can..." format is currently placeholder text.
    *   **Business Impact:** No annual GMV, income, cost savings, or avoidance figures provided.
    *   **Product Metrics:** Baseline impressions and CTR for generic search are not established; specific targets (e.g., AOV increase) are missing placeholders ($X to $Y).
    *   **Operational & Business Plans:** Key actions, workflows, go-to-market strategies, and engagement tactics are undefined.
    *   **Business Rules:** No logic or system behaviors have been defined yet.
    *   The core pending action is finalizing these sections to enable "Centralised booking" and "Timely post-campaign reporting."
*   **Decisions Made:**
    *   On **2026-03-19**, it was confirmed that there is **no approval for external resources**. Work will be picked up only when internal resources become available.
    *   The ticket has been marked as **"Tickets ready"** pending resource availability, indicating the conceptual scope (problem definition and goals) is understood but execution requires further detailing.
*   **Key Dates & Blockers:**
    *   **Created:** 2025-11-04.
    *   **Deadlines:** None assigned (`duedate: null`).
    *   **Blockers:** The initiative is blocked by the lack of finalized solution logic, business impact data, and approved external resources.
*   **Dependencies & Links:**
    *   Linked to Polaris work items: **DPD-3** and **DPD-299**.
    *   **Context:** Currently, Ad Ops must manually set up this ad format via Platform Ops in DBP Backoffice. The RMN BD team and Advertisers receive no performance reports for generic search on FPG RMN, creating a poor experience. The goal is to allow booking of all campaign assets (including generic search) in one place.

**Summary:** OMNI-1403 is a high-priority conceptual request owned by Nikhil Grover to integrate 'generic/suggested search' ad formats into OSMOS. While the problem statement and goals are defined, the solution summary, business impact metrics, operational plans, and logic rules remain incomplete. Crucially, as of 2026-03-19, the project is paused regarding external resource allocation; it will proceed once internal resources are available. The ticket requires completion of the missing data sections to move from "To Do" to implementation.


## jira/OMNI-1404: Support 'brand deal feature' ad format on category pages through OSMOS
Source: jira | Key: OMNI-1404 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-5, DPD-299 | Last Updated: 2026-03-19T12:45:01.257851+08:00
**Daily Briefing Summary: OMNI-1404**

*   **Current Status:** The ticket remains a **High Priority** "Idea" in the **"To Do"** state with a "Soft Prioritised" label. As of **2026-03-19**, Nikhil Grover confirmed that the tickets are ready for execution, though approval for external resources was denied; work will commence only when internal resources become available.
*   **Ownership & Assignee:** Reported by and assigned to **Nikhil Grover**.
*   **Core Objective:** Enable the booking of 'brand deal feature' ad formats on category pages via **OSMOS** to replace manual setup in **DBP Backoffice**. The goal is centralized booking for all package ad formats and timely post-campaign reporting within OSMOS.
*   **Business Problem & Impact:**
    *   **Ad Ops:** Currently forced to rely on Platform Ops in DBP Backoffice to set up the format, creating workflow inefficiencies.
    *   **RMN BD Team & Advertisers:** Lack of performance reporting results in a poor experience for campaigns on FPG RMN.
    *   **Goals:** Achieve centralized booking and reporting across all ad formats included in packages.
*   **Linked Work Items:** Linked to Polaris work items **DPD-5** and **DPD-299**.
*   **Pending Actions & Decisions:**
    *   **Documentation:** The specific "Solution Summary," "Business Impact" (GMV/Income/Cost), "Product Metrics Impact" (AOV, Perfect Order), "Operational Processes," "Business Plans," and "Business Rules" sections remain empty. These must be populated before the initiative can be pitched or developed.
    *   **Metrics:** Baseline impressions and click-through rates for the brand deal feature must still be established to define future success metrics (e.g., AOV increase within 6 weeks, Perfect Order improvement in 3 months).
    *   **Resource Constraint:** Development is contingent on resource availability due to the lack of approval for external resources.
*   **Timeline & Blockers:**
    *   **Last Update:** 2026-03-19T11:34:21.191+0800 (Nikhil Grover).
    *   **Previous Context:** The ticket was last noted as stalled at the planning stage on 2025-11-04 due to incomplete documentation.
    *   **Blockers:** Primary blocker is the absence of completed description fields required for formal pitching and the lack of approved external resources.

**Action Required:** Nikhil Grover must finalize the missing descriptive sections (Solution, Metrics, Operational Plans, Business Rules) and secure necessary internal resource allocation to move this from a "Ready" state to active development.


## jira/OMNI-1405: [OSMOS Only] Streamline seller/brand onboarding on OSMOS
Source: jira | Key: OMNI-1405 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | Last Updated: 2026-03-16T14:13:04.666230+00:00
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
Source: jira | Key: OMNI-1417 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-2, DPD-299 | Last Updated: 2026-03-19T12:45:15.416794+08:00
**Jira Briefing: OMNI-1417 – Support Omni Pop-up Booking and Reporting through OSMOS**

*   **Current Status:** The ticket remains an **Idea** in the **"To Do"** state, categorized as "Soft Prioritised" with a **High** priority. It was created on **2026-01-14**.
*   **Ownership & Action Items:** **Nikhil Grover** (Assignee and Reporter) owns this initiative. As of **2026-03-19**, the ticket is confirmed as "ready," but execution is paused pending resource availability; specifically, there is **no approval for external resources**. Pending actions involve finalizing standard template sections (Solution Summary, Business Impact, Product Metrics Impact, Operational Processes, Business Plans, and Business Rules/Logic) prior to formal pitching. The core requirement remains enabling platform Ops users to configure Omni Pop Up formats via OSMOS, eliminating the current dependency on DBP.
*   **Decisions Made:** No technical or business decisions have been finalized regarding implementation scope. The primary decision noted is the resource constraint: work will only commence when internal resources become available. The ticket now serves as a formal problem definition articulated by Nikhil Grover on 2026-01-14, specifically defining the user story: "As Ops user, I want to be able to book all display formats including Omni Pop Up through OSMOS so that I can book, track and report all campaign asset performance in a single place."
*   **Key Dates & Blockers:** There are **no due dates** assigned. The primary blocker is the lack of approved external resources required to execute the initiative. Additionally, the solution remains incomplete as critical template sections (Business Impact, Metrics, Rules, etc.) still require definition before the "To Do" status can transition to active execution.
*   **Dependencies:** This initiative links to Polaris work items **DPD-2** and **DPD-299**.
*   **Objective Summary:**
    *   **Problem:** Platform Ops must currently set up pop-up formats via DBP while other banners are handled through OSMOS, creating fragmentation.
    *   **Goal:** Achieve centralized booking of all display formats on OSMOS.
    *   **Expected Outcomes:** Simplified reporting via the OSMOS dashboard and improved governance, specifically enabling user-level frequency capping.


## jira/OMNI-1426: [Phase 2] - Improve GP of product by removing offers for specific SKUs
Source: jira | Key: OMNI-1426 | Status: For Pitching (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Rajesh Dobariya | Last Updated: 2026-03-19T12:45:32.261543+08:00
**Daily Work Briefing: OMNI-1426**

**Ticket Overview**
*   **ID:** OMNI-1426
*   **Title:** [Phase 2] - Improve GP of product by removing offers for specific SKUs
*   **Status:** For Pitching (Category: To Do)
*   **Type:** Idea
*   **Priority:** High
*   **Assignee/Reporter:** Rajesh Dobariya

**Current Status & State**
The ticket remains in the "For Pitching" phase. As of March 19, 2026, Rajesh Dobariya explicitly stated: **"Waiting for business impact before pitching."** The current system logic only prevents *new* offers from SAP for blacklisted SKUs after the blacklist date; it fails to deactivate *existing* active offers. Consequently, discounts continue applying to these SKUs until they expire automatically, negatively impacting Gross Profit (GP).

**Pending Actions & Ownership**
Rajesh Dobariya must complete the "Pitching" requirements before the idea can proceed. The description explicitly mandates ensuring all components are filled in before pitching. Critical missing data includes:
1.  **Problem Definition:** Quantify the affected user base (estimated number or %), their segment, severity, and current manual workarounds. The ticket requires a specific "As a... I want..." problem statement focusing on ignoring SAP offers for specific SKUs to improve GP.
2.  **Business Impact:** Provide concrete estimates for annual GMV/Income/Cost savings or avoidance (currently missing).
3.  **Product Metrics:** Define targets for Financial Impact (e.g., AOV increase from $X to $Y within 6 weeks) and Customer Experience (e.g., Perfect Order increase).
4.  **Operational & Business Plans:** Outline dependencies, budget approvals, go-to-market strategies, and system logic rules (e.g., skipping offer creation for blacklisted SKUs and disabling existing offers).

**Decisions Made**
No final development decisions have been recorded yet. The current consensus identifies the need for a backoffice feature allowing the upload of SKU blacklists to exclude new SAP offers and disable existing ones. However, advancement is paused pending the quantification of business impact.

**Key Dates & Blockers**
*   **Created/Last Updated:** 2026-02-26T09:49:17.889+0800 (Initial); 2026-03-19T11:29:17.673+0800 (Status update).
*   **Deadline:** None currently assigned (null).
*   **Blocker:** The ticket is stalled because the "Business Impact" section remains incomplete. Rajesh Dobariya cannot proceed with the pitch without providing annual GMV/Income/Cost savings estimates and specific product metric targets.


## jira/OMNI-1428: [1hd] Phase 2 -  Scaling one hour delivery to more stores (TO REMOVE)
Source: jira | Key: OMNI-1428 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Rajesh Dobariya | polaris-work-item-link: DPD-627 | Last Updated: 2026-03-19T12:45:48.983429+08:00
**Jira Ticket Summary: OMNI-1428**
**Subject:** [1hd] Phase 2 - Scaling one hour delivery to more stores (TO REMOVE)

**Current Status & State**
*   **Status:** Closed/Archived (Previously Backlog)
*   **Resolution:** Merged with OMNI-1425
*   **Type:** Idea
*   **Priority:** High
*   **Associate Work Item:** DPD-627 (Polaris work item link)
*   **Owner/Reporter/Assignee:** Rajesh Dobariya
*   **Date of Record:** 2026-02-27
*   **Archive Date:** 2026-03-19T08:59:09.890+0800

**Ownership & Pending Actions**
*   **Status Update:** On March 19, 2026, Rajesh Dobariya archived this ticket as merged with **OMNI-1425**.
*   **Previous State (Feb 27):** The ticket was initially a placeholder requiring the completion of a standardized description template before pitching. Required fields included Opportunity/Problem Definition, Goal & Solution Summary, Business Impact, Product Metrics Impact, Operational Processes, Business Plans, and Business Rules/Logic.
*   **Current Action:** No further action required on OMNI-1428 as it has been superseded by the merged ticket (OMNI-1425).

**Decisions Made**
*   **Initiative Status:** The initiative to scale one-hour delivery is no longer being tracked under this ID. Execution and scope definition have been consolidated into **OMNI-1425**.
*   **Template Requirement:** While the standardized description template was drafted for OMNI-1428 on 2026-02-27, it was never populated because the ticket was subsequently merged prior to moving to active development.

**Key Dates & Blockers**
*   **Original Creation:** 2026-02-27T12:22:08.201+0800
*   **Archive/Resolution:** 2026-03-19T08:59:09.890+0800
*   **Blocker Resolution:** The previous blocker (incomplete description) is resolved by the merger of this ticket with OMNI-1425, effectively closing the scope for tracking under OMNI-1428.
*   **Deadlines:** No due date was assigned prior to archival.

**Technical References**
*   **Ticket ID:** OMNI-1428 (Archived)
*   **Linked Issue:** DPD-627
*   **Merged Into:** OMNI-1425
