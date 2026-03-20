

## jira/OMNI-1191: [OSMOS only] Enable offsite ads integration with Meta on OSMOS
Source: jira | Key: OMNI-1191 | Status: Define (In Progress) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: RM-556 | Last Updated: 2026-03-20T14:44:56.988023+00:00
**Ticket:** OMNI-1191 | **Status:** Red (Blocked) | **Assignee:** Nikhil Grover | **Priority:** High | **Linked Issue:** RM-556

### Current State
The initiative to enable offsite ads integration with Meta on OSMOS remains blocked. While the solution design is defined and success criteria target $600k RMN Offsite revenue, development cannot proceed due to external dependencies. The project carries a high risk of missing the 2025 delivery window (~4-6 weeks development cycle required post-blocker removal).

### Blockers & Key Dates
*   **Primary Blocker:** Meta has not whitelisted specific campaigns required for API testing completion. This configuration update was delayed from October through January.
*   **Recent History:**
    *   **Oct 2025:** Configuration enabled by Meta; initial API testing began.
    *   **Nov 1, 2025:** Performance Marketing team confirmed correct config. Testing resumed but stalled waiting for campaign whitelisting.
    *   **Nov 28, 2025 - Jan 29, 2026:** Status remains blocked due to lack of response from Meta on whitelisting.
*   **Latest Update (Jan 22, 2026):** Testing of one use case is pending completion due to an error. Meta was asked to revert by the end of that week; no further update as of Jan 29.

### Pending Actions & Ownership
1.  **Finalize Whitelisting:** Meta must whitelist specific campaigns to allow OSMOS to complete API testing.
    *   *Owner:* Nikhil Grover (following up with Meta).
    *   *Escalation Path:* Business leadership and senior leads at Meta were previously engaged; escalation remains ongoing if no response is received.
2.  **Resolve Testing Error:** The error encountered in the current test case must be addressed by Meta to allow full testing completion.
3.  **Effort Estimation & Timeline:** Once testing is complete, OSMOS must confirm development effort and final timeline.
    *   *Owner:* OSMOS team (pending test completion).

### Decisions Made
*   **Validation Approach:** The idea was validated against a baseline of 7-8 offsite campaigns per month versus a target of $600k revenue.
*   **Escalation Strategy:** Upon multiple failed follow-ups in late October, the issue was escalated to senior leads at Meta and internal business stakeholders.

### Next Steps
Immediate focus is on securing Meta's response regarding campaign whitelisting to unblock API testing. Once OSMOS completes testing, they will provide a concrete effort estimate for the remaining development phase.


## jira/DPD-715: Dynamic ad slot configuration for Homepage swimlanes
Source: jira | Key: DPD-715 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-17 | Resolution: Done | parent: DPD-710 | Last Updated: 2026-03-20T14:45:22.796038+00:00
### Daily Briefing Summary: DPD-715 (Dynamic Ad Slot Configuration)

**Current Status:** **IN RELEASE QUEUE** (Resolution: Done). The story is technically complete and pending final deployment/approval.

**Key Decisions & Actions Taken:**
*   **Feature Flag Implementation:** Split configuration logic implemented to dynamically control ad slot indices (e.g., `[3, 5, 7]`) without code changes. Handles fallback defaults (`[1, 3]`), empty arrays (organic only), and out-of-bounds scenarios gracefully.
*   **Environment Updates (2026-03-16):**
    *   **OG Home:** Verified SplitIO change reflection in swimlanes.
    *   **Mobile Apps:** Confirmed fix for mobile-specific issues; ticket marked ready for UAT.
    *   **Omni Home:** Positions remain fixed at `(1, 3)` pending further investigation by Michael Bui (contacting stakeholders).

**Pending Actions & Ownership:**
*   **UAT Execution:** Conducted on **2026-03-19** by Michael Bui. Outcomes to be documented.
*   **Omni Home Discrepancy:** Investigate why Omni swimlanes are not reflecting the dynamic Split changes (currently stuck at fixed positions). Owner: **Michael Bui**.
*   **Final Release:** Move from "In Release Queue" to production deployment post-UAT sign-off.

**Key Dates & Constraints:**
*   **Due Date:** 2026-03-17 (Note: Status indicates completion past this date).
*   **Critical Constraint:** System must maintain existing stock availability checks; no out-of-stock products can be rendered as ads.
*   **Parent Ticket:** DPD-710 ([RMN] Activate product ads in Omni Home swimlanes).

**Technical Context:**
*   **Logic:** API requests adapt to Split configuration counts (e.g., 3 slots = request 3 ads). If Ad Supply is short, system fills available slots and renders organic content for gaps.
*   **Reporting:** Michael Bui reported successful UAT session completion on 2026-03-19.

**Blockers/Notes:**
*   Minor inconsistency remains in Omni Home swimlane rendering compared to OG Home; requires clarification with the referenced stakeholders before full sign-off.


## jira/DPD-733: Dynamic ad slots for vertical scroll on omni homepage
Source: jira | Key: DPD-733 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-17 | Resolution: Done | parent: DPD-710 | Last Updated: 2026-03-20T14:45:39.703781+00:00
**Daily Briefing Summary: DPD-733**

**1. Current Status & State**
*   **Ticket ID:** DPD-733 (Dynamic ad slots for vertical scroll on omni homepage)
*   **Status:** IN RELASE QUEUE (Parent status: Done).
*   **Resolution:** The story is completed and awaiting release deployment.
*   **Priority:** High.
*   **Type:** Story, part of parent epic DPD-710 ("[RMN] Activate product ads in Omni Home swimlanes").

**2. Actions Pending & Ownership**
*   **Pending Action:** Deployment to production is required from the release queue.
*   **Owner:** Michael Bui (Assignee).
*   **Stakeholder:** Nikhil Grover (Reporter).

**3. Key Decisions & Technical Implementation**
The feature enables dynamic control of product ad placement and count on the Omni Homepage vertical scroll via a Split feature flag, eliminating the need for code changes or manual API updates.
*   **Dynamic Logic:** The system requests ads based on configuration arrays (e.g., `[3, 5, 7]`). If enabled and configured to `[3, 5, 7]`, the app requests 3 ads and renders them at those specific indices.
*   **Fallback Behavior:** If the feature flag is OFF but ads are enabled, the system defaults to slots `[1, 3]` (requesting 2 ads).
*   **Real-Time Updates:** Updating Split configuration in the dashboard (e.g., to `[2, 4, 6, 8, 10]`) immediately affects new user sessions without code deployment.
*   **Edge Case Handling:**
    *   **Empty Config:** If configured as `[]`, the system requests 0 ads; only organic content is displayed.
    *   **Supply Shortage:** If fewer ads are returned than requested (e.g., config asks for 3, API returns 2), existing slots fill, and remaining slots display organic content.
    *   **Out-of-Bounds:** Indices exceeding available content range (e.g., index 20 with only 10 items) are ignored; valid ads render within the available range.
*   **Constraints:** The system strictly honors existing stock availability checks; out-of-stock products cannot be served as ads.

**4. Key Dates & Deadlines**
*   **Due Date:** March 17, 2026.
*   **Last Activity:** March 10, 2026 (Status update to "IN RELASE QUEUE").
*   **Blockers:** None reported; ticket is resolved and in the release queue.


## jira/DPD-734: Include swimlane name in the ad request for all Omni Home swimlanes
Source: jira | Key: DPD-734 | Status: TO BE DEFINED (To Do) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-17 | parent: DPD-710 | Last Updated: 2026-03-20T14:45:50.801862+00:00
**Daily Briefing Summary: DPD-734**

**Current Status:**
The ticket **DPD-734** is currently in the **TO BE DEFINED (To Do)** status. It is a High-priority Story assigned to **Michael Bui**, reported by **Nikhil Grover**. The issue is a sub-task of parent ticket **DPD-710** ("[RMN] Activate product ads in Omni Home swimlanes").

**Pending Actions & Ownership:**
*   **Action:** Implement technical logic to include the swimlane name in ad requests for all Omni Home swimlanes.
*   **Owner:** **Michael Bui**.
*   **Requirement Details:** When an enabled swimlane triggers an ad request to **OSMOS**, the system must pass the specific swimlane name as the `"Page_name"` parameter within the request payload. This is required to enable performance tracking and optimization at the individual swimlane level.

**Decisions Made:**
*   No technical decisions have been recorded yet; the ticket remains in the definition phase. The functional requirement (passing `Page_name`) is defined, but the implementation strategy has not been finalized by the assignee or team.

**Key Dates & Blockers:**
*   **Deadline:** March 17, 2026.
*   **Last Update:** March 10, 2026 (Initial ticket creation and status set to "To Do").
*   **Blockers:** None currently identified; the primary blocker is the transition from "To Be Defined" to active development by **Michael Bui**.

**Context:**
This story supports the broader initiative (**DPD-710**) to activate product ads in Omni Home swimlanes, specifically addressing the data visibility gap for Product Managers regarding ad request origins.


## jira/DPD-644: [RMN] Streamline event sync from Segment.io to OSMOS to resolve overage
Source: jira | Key: DPD-644 | Status: Done (Done) | Type: Epic | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-12 | Resolution: Done | parent: DPD-645 | polaris-work-item-link: OMNI-1418 | Last Updated: 2026-03-20T14:46:01.632729+00:00
**Daily Briefing: Jira Ticket DPD-644**

*   **Current Status:** The Epic is **Done**. Resolution status is confirmed as completed.
*   **Ownership & Pending Actions:** No actions are pending. The ticket was assigned to **Michael Bui**, who has successfully closed the work. **Nikhil Grover** reported and initiated the effort.
*   **Decisions Made:** The decision was executed to streamline the event synchronization pipeline from **Segment.io** directly to **OSMOS**. This architectural change was implemented specifically to resolve data ingestion overage costs associated with the previous setup.
*   **Key Dates & Deadlines:**
    *   **Due Date:** March 12, 2026 (Successfully met/navigated).
    *   **Last Activity Update:** March 3, 2026 (Status marked as Done).
*   **Technical References:**
    *   **Ticket ID:** DPD-644
    *   **Linked Work Item:** OMNI-1418 (Polaris work item link)
    *   **Priority:** High
    *   **Issue Type:** Epic

**Summary:**
The high-priority Epic **DPD-644**, titled "[RMN] Streamline event sync from Segment.io to OSMOS to resolve overage," has been formally resolved. Under the ownership of **Michael Bui**, the team successfully optimized the data flow between **Segment.io** and **OSMOS**. The primary objective was to eliminate unnecessary cost overages caused by inefficient syncing mechanisms. The work is complete as of March 3, 2026, ahead of the original due date of March 12, 2026. No blockers were recorded during this cycle.


## jira/DPD-645: Improve event sync to prevent overage
Source: jira | Key: DPD-645 | Status: Done (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-12 | Resolution: Done | blocks: DPD-273, DPD-273 | parent: DPD-644 | Last Updated: 2026-03-20T14:46:17.913487+00:00
**Jira Briefing: DPD-645 – Improve event sync to prevent overage**

**Current Status**
*   **State:** Done (Complete).
*   **Assignee:** Michael Bui.
*   **Reporter:** Nikhil Grover.
*   **Resolution:** The optimization has been successfully deployed and verified in Production. Daily function execution time was reduced from approximately 25 days to ~8 days, translating to an estimated reduction of ~12.2k hours/month (actual savings to be confirmed over the coming months).

**Key Decisions & Outcomes**
*   **Target Adjustment:** The initial acceptance criteria requested a 50% execution time reduction. Michael Bui clarified this was a tentative target due to variable computing duration; the team committed to minimizing function usage regardless of meeting the specific percentage.
*   **Deployment Strategy:** A phased rollout plan was approved:
    1.  UAT observation (data pattern comparison between OSMOS and BigQuery).
    2.  Temporary PRD deployment on Sunday, March 15, from 8 PM to 11 PM.
    3.  Verification of error rates against the last 1–2 weeks of data.
    4.  Permanent enablement if no issues were detected.
*   **Production Outcome:** The change was deployed temporarily on March 15 at 20:01. After ~30 minutes, no issues were observed. Although a temporary restoration to version #56 occurred at 23:02 (likely for maintenance or final validation), subsequent monitoring confirmed no abnormalities in PRD as of March 19. The solution is now considered stable and effective.

**Pending Actions & Ownership**
*   **Ongoing Monitoring:** While the immediate deployment is successful, continuous observation is required to confirm long-term cost savings.
    *   **Owner:** Michael Bui (Monitoring PRD stability).
*   **Final Validation:** Confirmation of the exact monthly reduction figures over the next few months.
    *   **Owner:** Michael Bui / Finance Team (implied via "Actual reduction will be observed").

**Key Dates & References**
*   **Ticket ID:** DPD-645 (Parent: DPD-644; Blocks: DPD-273).
*   **Due Date:** March 12, 2026 (Note: Ticket marked Done post-due date).
*   **Critical Milestones:**
    *   March 3: Initial status update and target discussion.
    *   March 5: UAT data pattern analysis completed.
    *   March 15: Temporary PRD deployment (20:01) and subsequent verification.
    *   March 19: Confirmation of no abnormalities and reported ~68% reduction in function time (~25d to ~8d).
*   **Technical References:** Segment.io, OSMOS PROD destination, BigQuery cross-checks, Function version #56.


## jira/OPCO-1940: FP VIPs encounter verification after S&G purchase for fewer reasons, vs other customers
Source: jira | Key: OPCO-1940 | Status: In release queue (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Ravi Goel | Resolution: Done | Labels: priority:improvement | blocks: OPCO-1956 | Last Updated: 2026-03-20T14:46:38.477862+00:00
### Executive Briefing: OPCO-1940 (FP VIP Verification Bypass)

**Current Status:**
The ticket is **On Hold**. While the development work is complete and UAT was signed off on **2026-02-02**, the feature has **not been released or enabled**. It remains in a "Done" state technically but is blocked pending business alignment. As confirmed by Michael Bui on **2026-03-16** following Vivian Lim Yu Qian's update, the deployment is paused due to required re-alignment on the business side regarding VIP identification logic.

**Pending Actions & Ownership:**
*   **Business Alignment (Owner: Business Side/CS):** Re-align on the definition of "VIP" status. The original implementation relied on a Split flag referencing an external tracking sheet; feedback from Winson indicates the system must instead rely directly on the backoffice tag applied to the customer account. This requires business confirmation before release.
*   **UAT Finalization (Owner: Michael Bui):** Await signed-off UAT results once alignment is resolved.
    *   *Note:* Initial UAT was completed by Calvin Phan and David Anura Cooray on **2026-01-29** and **2026-02-02**, confirming non-VIP behavior remains unchanged via targeted testing (VIP account 6873106, Non-VIP 6835530).
*   **Deployment (Owner: Michael Bui):** Execute release only after UAT sign-off and business alignment are confirmed.

**Key Decisions Made:**
1.  **Logic Shift:** The VIP identification source was re-evaluated. Instead of using a Split flag referencing an Excel sheet, the system must utilize the direct backoffice tag on the customer account to determine VIP status (Decision noted by Vivian Lim Yu Qian on **2026-03-16**).
2.  **Verification Logic:** Confirmed that VIPs bypass S&G verification for generic risk rules but **must still verify** for:
    *   Age-restricted items.
    *   Force-verification SKUs.
    *   High-priced items (price > HighRiskPrice threshold).
3.  **Monitoring Strategy:** Vivian Lim Yu Qian approved release pending the above, mandating specific Datadoghq monitoring post-deployment to track verification success/fail ratios and ensure no regression in non-VIP flows.

**Key Dates & Blockers:**
*   **2026-01-29:** UAT issues regarding Orange/Green banners resolved; testing concluded.
*   **2026-02-02:** Monitoring strategy defined (Datadoghq queries for `st-verification-service`).
*   **2026-03-16:** Ticket officially placed on hold pending business re-alignment.
*   **Blocker:** Business alignment on VIP identification methodology (Backoffice tag vs. Split flag/Sheet).
*   **Linked Issues:** Blocks **OPCO-1956**.

**Technical References:**
*   Feature controlled via Split (flag state and VIP list configuration).
*   Monitoring queries linked to `service:st-verification-service` for manual check counts.


## jira/DPD-700: Fix RMN pentest Low and optionally Info issues
Source: jira | Key: DPD-700 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Due: 2026-03-20 | Resolution: Done | Labels: priority:improvement | relates: DPD-591, DPD-591 | Last Updated: 2026-03-20T14:47:05.245530+00:00
**Daily Briefing: DPD-700 (Fix RMN Pentest Low/Info Issues)**

**Current Status:**
The ticket **DPD-700** is marked as **Done**. Remediation efforts for the RMN pentest findings on the `marketing-personalization-service` have been successfully deployed to both Preprod (`...uat.fairprice.com.sg`) and Production environments. The fixes were captured following a Terraform apply on March 9, 2026, at 22:25 SGT.

**Actions Completed:**
*   **Headers Deployed:** All missing security headers have been verified in both environments:
    *   `Strict-Transport-Security` (max-age=31536000)
    *   `Content-Security-Policy` (`default-src 'none'; frame-ancestors 'none'`)
    *   `Cache-Control` (`no-store`)
    *   `X-Content-Type-Options` (`nosniff`)
    *   `X-Frame-Options` (`DENY`)
    *   `Referrer-Policy` (`strict-origin-when-cross-origin`)
*   **Rate Limiting:** GCP Cloud Armor is now active, enforcing 200 requests per second (RPS) per IP address with a threshold of 12,000 req/60s. Exceeding limits returns HTTP 429.
*   **TLS Configuration:** Previous Low-severity findings regarding "Lucky Thirteen" attacks and Static Key Ciphers were already resolved via the new GCP SSL Policy ("RESTRICTED").

**Pending Actions & Ownership:**
*   **Unreferenced API Endpoints (Low):** The auditor noted unreferenced pages. This was accepted as a Health Check configuration rather than an active endpoint issue. No further action required.
*   **CORS Wildcard Origin (Info):** The current response still includes `access-control-allow-origin: *`.
    *   **Decision:** This is **Accepted** for the time being but flagged as requiring a future application-level change to enforce a strict whitelist of FairPrice domains.
    *   **Owner:** Application team (outside scope of this specific infrastructure chore).

**Key Dates & Deadlines:**
*   **Fix Deployment:** March 9, 2026.
*   **Ticket Due Date:** March 20, 2026.
*   **Resolution Status:** Completed prior to the deadline.

**Stakeholders & References:**
*   **Assignee/Reporter:** Michael Bui
*   **Related Ticket:** DPD-591 (Relates)
*   **Priority:** High
*   **Labels:** `priority:improvement`

**Summary:**
Infrastructure-side security hardening is complete. All Low and optional Info severity headers are active, and rate limiting is enforced. The only remaining item regarding CORS wildcards has been accepted as an application-level dependency and does not block this ticket's completion.


## jira/DPD-551: Capture SAP Material Number into catalogue service for SAP-related downstream usage
Source: jira | Key: DPD-551 | Status: Done (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done | blocks: DPD-383, DPD-383 | Last Updated: 2026-03-20T14:47:29.994165+00:00
**Daily Briefing Summary: DPD-551**

**Current Status:** **Done**
The story regarding the capture of SAP Material Numbers into the catalogue service is complete. Development, User Acceptance Testing (UAT), and Production deployment have been successfully executed.

**Key Actions & Ownership:**
*   **Development & Verification (Michael Bui):** Implemented logic to store SAP material numbers in product metadata fields. Verified functionality on UAT post-UD (Update). Deployed changes to Production on March 9, 2026, and verified with a UD for both RB and MP SKUs (specifically BCRS SKU).
*   **Production Enablement (Sneha Parab):** Created the `SAPMaterialNumber` field in the production environment on March 9, 2026.

**Decisions Made:**
*   Confirmed that the SAP material number must be stored as a specific product metadata field to resolve identification mismatches between the DPP platform and SAP systems.
*   Validated integration readiness by confirming downstream services can now utilize captured data for SAP-related logic.

**Key Dates & Milestones:**
*   **Feb 16, 2026:** Ticket created; scope defined (High Priority Story).
*   **Feb 19, 2026:** UAT verification completed successfully by Michael Bui.
*   **Mar 09, 2026:** Production field creation and deployment verified by Sneha Parab and Michael Bui.

**Pending Actions & Blockers:**
*   **No pending actions.** The ticket is resolved.
*   **Dependency Resolved:** This work was required to unblock issue **DPD-383**. No current blockers exist.

**Technical References:**
*   **Ticket ID:** DPD-551
*   **Blocked Issue:** DPD-383
*   **New Field:** `SAPMaterialNumber`
*   **Test Scope:** RB and MP SKUs (BCRS SKU verified).


## jira/DPD-631: Setup alerts for Advertima platform
Source: jira | Key: DPD-631 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done | Last Updated: 2026-03-20T14:47:42.666749+00:00
**Jira Ticket Briefing: DPD-631**

**Ticket Details:**
*   **ID:** DPD-631
*   **Title:** Setup alerts for Advertima platform
*   **Type/Category:** Chore (High Priority)
*   **Current Status:** Done
*   **Assignee/Reporter:** Michael Bui

**Status Summary:**
The task is fully completed. The alerting system for the Advertima platform has been successfully configured and operational as of March 9, 2026.

**Key Actions & Decisions:**
1.  **Alert Configuration:** Established an email distribution group to receive RMN (Rapid Monitoring Network) alerts specifically for the Advertima platform.
    *   *Decision:* Use an email group mechanism for alert ingestion.
    *   *Reference Update:* Noted update from Advertima regarding status on February 20, 2026, which preceded this configuration work.
2.  **Implementation:** Michael Bui completed the setup of the alerts within the system.

**Timeline & Milestones:**
*   **Creation:** Ticket opened and assigned to Michael Bui on February 27, 2026.
*   **Reference Update:** Advertima provided status context on February 20, 2026 (logged on Feb 27).
*   **Action Timestamps:**
    *   Feb 27, 2026: Configuration of the email group initiated.
    *   Mar 9, 2026: Confirmed completion; alerts are active ("The alert has been set up").

**Pending Actions & Ownership:**
*   None. All items within this ticket scope have been resolved. No pending tasks require ownership assignment.

**Blockers & Constraints:**
*   **Deadlines:** No specific due date was assigned to the ticket (`duedate: null`).
*   **Blockers:** None reported; the task progressed from initiation to completion without impediments.


## jira/DPD-591: Fix RMN pentest medium issues
Source: jira | Key: DPD-591 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Due: 2026-03-20 | Resolution: Done | Labels: priority:improvement | relates: RM-669, DPD-700, DPD-700 | Last Updated: 2026-03-20T14:47:54.792440+00:00
**Jira Ticket Summary: DPD-591**

**Current Status:** Done (Resolved)
*   **Assignee/Reporter:** Michael Bui
*   **Priority:** High
*   **Resolution:** Completed with verification.

**Key Actions & Decisions:**
*   **Security Remediation:** The ticket addressed seven medium-severity pentest findings related to TLS/SSL vulnerabilities, including SWEET32 (64-bit block ciphers), BEAST attack vectors, deprecated protocols (TLS 1.0/1.1), outdated cipher suites (DES, IDEA), "Lucky Thirteen" timing attacks, and static key ciphers lacking Forward Secrecy.
*   **Policy Implementation:** On **March 5, 2026**, Michael Bui implemented a `RESTRICTED` policy to mitigate the identified risks.
*   **Verification & Deployment:** The changes were deployed to Production (PRD) on **March 5, 2026**. Verification was performed via Nmap scan (`ssl-enum-ciphers`) against `marketing-personalization-service.fairprice.com.sg`.
    *   **Result:** TLSv1.2 is now enforced with `x25519` (128-bit) key exchange and SHA256WithRSAEncryption signatures. Legacy protocols and weak ciphers were successfully removed.
*   **Sign-off:** LGMS confirmed the remediation on March 5, 2026.

**Linked Issues & Dependencies:**
*   Relates to: `RM-669` and `DPD-700`.

**Key Dates & Deadlines:**
*   **Ticket Due Date:** March 20, 2026 (Note: Task completed well ahead of this deadline).
*   **Completion Date:** March 5, 2026.

**Pending Actions & Blockers:**
*   None. The ticket is closed with no outstanding blockers or pending actions identified in the log.


## jira/DPD-383: Sales posting for BCRS deposit amount
Source: jira | Key: DPD-383 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Prajney Sribhashyam | Due: 2026-02-18 | Resolution: Done | blocks: DPD-551, DPD-551 | child: DPD-590 | parent: DPD-225, DPD-590 | Last Updated: 2026-03-20T14:48:18.957493+00:00
**Ticket:** DPD-383 (Sales posting for BCRS deposit amount)
**Status:** IN RELASE QUEUE (Done) | **Priority:** High
**Assignee:** Michael Bui | **Reporter:** Prajney Sribhashyam

**Current State & Key Decisions**
*   **Development Complete:** The SAP Deposit Posting service is fully implemented to handle BCRS deposits for E-Comm, Marketplace, Return/Refund, Donation, and FOC (Free of Charge) items.
*   **Logic Confirmation:** Deposits are calculated per order line (`deposit price × fulfilled quantity`) and aggregated at the order level. Only orders with status **COMPLETED** are processed; OFFLINE, RB PreOrder, and non-COMPLETED orders are ignored.
*   **Duplicate Prevention Decision:** Due to GCP PubSub default behavior causing duplicate postings, Michael Bui enabled the "delivery once" policy on 2026-03-06. SAP successfully captures only the first valid posting.
*   **Technical Fixes:** CSRF token and cookie handling for SAP (403 resolution) was implemented. Failure detection logic was added to distinguish HTTP 201 success from internal business errors based on response content.

**Pending Actions & Ownership**
*   **Release Execution:** Ticket is in the "IN RELASE QUEUE." Michael Bui will execute or monitor the final release deployment.
*   **No Immediate Blockers:** The previous blockage (DPD-551 PLU Processor) was resolved on 2026-02-20 when `sapMaterialNumber` was added to the order-v3 gRPC API response.

**Key Dates & Timeline**
*   **2026-01-30:** Story created with High priority.
*   **2026-02-16:** SAP access requested; work paused pending DPD-551 resolution.
*   **2026-02-20:** `sapMaterialNumber` exposed in API; Development marked as complete (E2E blocked by SAP access).
*   **2026-02-23:** SAP connectivity verified; successful posting confirmed with reference doc `BKPFF 6500037303FP102027`.
*   **2026-03-04:** Discovered undocumented `freeItems` field for FOC logic.
*   **2026-03-06:** "Delivery once" policy enabled to prevent duplicates; verified against SAP logs.

**Technical References & Data Points**
*   **Parent Ticket:** DPD-225 ([BCRS] Inform customers on BCRS deposit...)
*   **Blocking Issue (Resolved):** DPD-551
*   **Subtask:** DPD-590 (Clean up archived proposals)
*   **SAP Configuration Verified:** CompCode `FP10`, DocType `DR`, GL Account `4423` (Deposit), Customer `199997`.
*   **Sample Success Log:** `MessageV2: "Document posted successfully: BKPFF 6500037303..."`
*   **GCP PubSub Config:** Delivery once policy applied to avoid duplicate SAP postings.

**Blockers/Notes**
*   All historical blockers (SAP access, material number availability) have been cleared. The system is currently in the release queue awaiting production deployment.


## jira/DPD-273: Take over Segment destination functions from OSMOS
Source: jira | Key: DPD-273 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done | blocks: DPD-645, DPD-645 | Last Updated: 2026-03-20T14:48:27.043939+00:00
**Status:** Done
**Ticket ID:** DPD-273
**Type:** Chore (High Priority)
**Assignee/Reporter:** Michael Bui

**Current State**
The task to take over Segment destination functions from OSMOS has been completed and resolved. The work involved migrating functionality previously managed by the OSMOS team.

**Key Actions & Timeline**
*   **2026-01-23:** Ticket created by Michael Bui to initiate the takeover.
*   **2026-01-23:** An IT Helpdesk ticket was referenced/logged in connection with this work.
*   **2026-02-14:** Work paused and placed on hold pending receipt of a specific Handover document from the OSMOS team.
*   **2026-03-06:** The required documentation was provided by Vipul (OSMOS), allowing the task to proceed and eventually reach completion.

**Decisions & Dependencies**
*   **Dependency:** Progress was explicitly blocked until the handover documentation from OSMOS was received.
*   **Blocking Relationship:** This ticket blocks **DPD-645**.

**Pending Actions**
None. The ticket resolution is marked as "Done." All immediate dependencies regarding the handover document have been satisfied.


## jira/DPD-590: Clean up archived proposals after PRD release
Source: jira | Key: DPD-590 | Status: TO BE DEFINED (To Do) | Type: Subtask | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Due: 2026-04-24 | child: DPD-383 | parent: DPD-383 | Last Updated: 2026-03-20T14:48:32.369189+00:00
**Daily Briefing Summary: DPD-590**

*   **Current Status:** The task is marked as **TO BE DEFINED (To Do)**. No work has commenced.
*   **Ownership & Pending Actions:** **Michael Bui** (Assignee/Reporter) owns the execution of this subtask. Pending actions include identifying and removing archived proposals from the repository to prevent future AI hallucinations.
*   **Decisions Made:** None recorded in the ticket history yet; the scope remains defined by the task title and description intent.
*   **Key Dates & Deadlines:** The due date is set for **2026-04-24**.
*   **Blockers/Context:** This subtask (**DPD-590**) supports the parent initiative **DPD-383** ("Sales posting for BCRS deposit amount"). It carries a **High** priority.


## jira/QE-1105: New project setup for BCRS deposit posting job "ntuclink_bcrs-deposit-posting"
Source: jira | Key: QE-1105 | Status: Done (Done) | Type: Chore | Priority: High | Reporter: Michael Bui | Resolution: Done | parent: QE-682 | Last Updated: 2026-03-20T14:48:41.349496+00:00
**Daily Briefing Summary: QE-1105**

**Status & State**
*   **Current Status:** Done (Resolution: Done).
*   **Ticket ID:** QE-1105.
*   **Parent Ticket:** QE-682 ("Sonar and other Adhoc support requests").
*   **Date of Completion Update:** 2026-02-19T10:20:37+0800.

**Ownership & Actions**
*   **Reporter:** Michael Bui.
*   **Assignee:** None (Unassigned).
*   **Pending Actions:** No pending actions; the ticket is closed.
*   **Team Ownership:** DPD Omni/Ecom team is responsible for the associated project context.

**Key Decisions & Configuration**
The following configuration was established and finalized during this Chore:
*   **Project Setup:** New SonarCloud project created with the identifier `ntuclink_bcrs-deposit-posting`.
*   **Repository:** Linked to `bcrs-deposit-posting` (specific URL not populated in ticket).
*   **Language Stack:** Golang.
*   **Quality Standards:** Configured to "Low Tolerance" Quality Gate.

**Dates, Deadlines & Blockers**
*   **Deadline:** None (`null`).
*   **Blockers:** None identified; the task is marked as complete.
*   **Priority:** High (as assigned by Michael Bui).

**Technical References**
*   **Job Name:** `ntuclink_bcrs-deposit-posting`.
*   **Platform:** SonarCloud.


## jira/DPD-519: [RMN] Unblock NTP connection for Advertima devices
Source: jira | Key: DPD-519 | Status: Done (Done) | Type: Chore | Priority: Medium | Assignee: Michael Bui | Reporter: Michael Bui | Resolution: Done | Last Updated: 2026-03-20T14:48:50.891725+00:00
**Daily Work Briefing Summary**

**Ticket ID:** DPD-519
**Title:** [RMN] Unblock NTP connection for Advertima devices
**Current Status:** Done (Resolution: Done)
**Assignee/Owner:** Michael Bui
**Reporter:** Michael Bui
**Priority:** Medium
**Issue Type:** Chore

**Status Overview**
The ticket is fully completed. The issue regarding the NTP connection for Advertima devices has been resolved. No further actions are pending, and there are no active blockers or upcoming deadlines associated with this item (Duedate: null).

**Key Dates & Timeline**
*   **2026-02-09T17:50:10.933+0800:** Ticket created by Michael Bui. Initial status set to "Done" at creation time, with the title and metadata captured.
*   **2026-02-14T11:10:36.331+0800:** Final confirmation provided by Michael Bui that the issue has been resolved.

**Decisions Made**
No formal decision-making meetings or strategic pivots were recorded for this ticket. The workflow indicates a direct execution path where the assigned engineer (Michael Bui) implemented the necessary changes to unblock the NTP connection, resulting in an immediate "Done" status upon creation and final confirmation five days later.

**Pending Actions**
None. All work defined in the scope of DPD-519 is complete.

**Technical References**
*   **Resource:** RMN (Regional/Main Network context implied)
*   **Target Device:** Advertima devices
*   **Action Required:** Unblock NTP (Network Time Protocol) connection
*   **Component/Version:** No specific fix versions or components listed in metadata.


## jira/DPD-221: New SKU Sync Optimisation
Source: jira | Key: DPD-221 | Status: Done (Done) | Type: Epic | Priority: High | Reporter: Michael Bui | Resolution: Done | parent: DPD-220 | Last Updated: 2026-03-20T14:48:58.534921+00:00
**Daily Briefing Summary: DPD-221 – New SKU Sync Optimisation**

*   **Current Status:** The Epic is marked as **Done**. Both the `status` and `resolution` fields indicate full completion.
*   **Pending Actions & Ownership:** There are **no pending actions**. The ticket has no assigned assignee (`assignee: null`), and since the status is "Done," no further ownership or execution is required for this item.
*   **Decisions Made:** The work scope defined under the "New SKU Sync Optimisation" title initiated by Michael Bui has been fully executed and resolved. No specific technical decisions are detailed in the provided log, but the final resolution confirms the optimisation initiative was concluded successfully.
*   **Key Dates & Blockers:**
    *   **Reporter:** Michael Bui.
    *   **Priority:** High.
    *   **Last Activity Date:** September 30, 2025 (10:16 AM +08:00).
    *   **Deadlines:** None (`duedate: null`).
    *   **Blockers:** No blockers identified.

**Summary:**
Epic DPD-221 is closed. Initiated and reported by Michael Bui with High priority, the "New SKU Sync Optimisation" project reached completion as of September 30, 2025. The item requires no further action or resource allocation.


## jira/NEDMT-2288: [CDP] Access Request from Retail Media
Source: jira | Key: NEDMT-2288 | Status: Done (Done) | Type: Task | Priority: Blocker | Assignee: Yadear Zhang | Reporter: Michael Bui | Resolution: Done | Last Updated: 2026-03-20T14:49:18.293034+00:00
**Daily Briefing Summary: Jira Ticket NEDMT-2288**

*   **Current Status:** The ticket is marked as **Done** with a resolution of "Done." Access has been successfully provisioned.
*   **Ownership & Actions:** The request was initiated by **Michael Bui**. **Yadear Zhang** executed the action on 2025-11-17 at 12:05 AM, confirming that Source Admin access was granted and notifying the reporter to verify. No further actions are pending; the ticket is closed.
*   **Decisions Made:** The team decided to grant **Source Admin** privileges in the **production environment** for user `vipul.gupta_fp@ntucguest.com`. This decision addressed a critical access gap where the user previously had visibility only into the UAT environment.
*   **Key Dates & Blockers:**
    *   **Priority:** Blocker (indicating high urgency).
    *   **Request Date/Time:** 2025-11-17 at 11:30 AM.
    *   **Resolution Time:** 2025-11-17 at 12:05 PM (Resolved within 35 minutes).
    *   **Ticket ID:** NEDMT-2288 | **Issue Type:** Task.

**Summary:** The Blocker access request for Retail Media was resolved immediately on November 17, 2025. Yadear Zhang granted the necessary production environment permissions to vipul.gupta_fp@ntucguest.com as requested by Michael Bui.


## jira/DPD-431: "Ad" product copy display not consistent at times
Source: jira | Key: DPD-431 | Status: TO BE DEFINED (To Do) | Type: Bug | Priority: Low | Reporter: Vivian Lim Yu Qian | Labels: priority:improvement | Last Updated: 2026-03-20T14:49:49.631570+00:00
**Jira Ticket Briefing: DPD-431**

**Issue Summary**
The "Ad" product copy display is inconsistent on PROD Android 7.20.0 (build 680.7f77). In some instances, the Ad label formatting disappears or blends with the product title font color, causing it to appear as part of the title rather than a distinct label. This occurs alongside other PLP ad SKUs displaying correctly.

**Current Status**
*   **State:** TO BE DEFINED (To Do)
*   **Type:** Bug (Label: `priority:improvement`)
*   **Priority:** Low
*   **Assignee:** None currently assigned.
*   **Reporter:** Vivian Lim Yu Qian

**Key Discussion Points & Decisions**
*   **Root Cause Analysis (2026-02-06):** Michael Bui identified the issue relates to product title labels/custom labels and noted that a fix for this specific behavior was discussed previously, though verification is required.
*   **Fix Availability (2026-02-06 11:31):** Andin Eswarlal Rajesh confirmed the bug was already resolved in code but failed to ship in the previous regular release. He referenced the original ticket for context.
*   **Decision Pending:** The team has not yet decided if this requires a hotfix, given its "Low" priority and the fact that the fix is already available in code.

**Pending Actions & Ownership**
*   **Hotfix Decision:** A decision is required on whether to deploy a hotfix for this issue (Owner: Unassigned/Team).
*   **Verification:** The previously discussed fix needs verification against current production behavior.

**Key Dates & References**
*   **2026-02-05 17:59:** Issue reported by Vivian Lim Yu Qian.
*   **2026-02-06 10:14:** Investigation by Michael Bui regarding label logic.
*   **2026-02-06 11:31:** Confirmation of fix existence by Andin Eswarlal Rajesh.
*   **Technical Reference:** PROD Android 7.20.0 (680.7f77).

**Blockers & Risks**
*   No active assignee; the ticket remains in "To Be Defined" status pending a decision on deployment strategy.
*   No hard deadline or due date currently set.


## jira/DPD-220: Automate sync of newly onboarded SKUs into OSMOS for faster activation
Source: jira | Key: DPD-220 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Resolution: Done | Labels: priority:improvement | parent: DPD-221 | Last Updated: 2026-03-20T14:50:10.397534+00:00
**Ticket:** DPD-220 | **Title:** Automate sync of newly onboarded SKUs into OSMOS for faster activation
**Parent:** DPD-221 (New SKU Sync Optimisation)
**Assignee:** Michael Bui | **Reporter:** Nikhil Grover
**Status:** IN RELASE QUEUE (Done) | **Priority:** High

### Current Status
The automation job is successfully generated in the pre-production GCS bucket (`gs://fpg-spotlight-osmos-preprod/sku-vendor-mapping/`). Files contain >500k rows matching PRD data, with hourly snapshots and Datadog logs confirming correct generation. The ticket remains pending formal UAT sign-off due to a lack of isolated testing environment; the source (BigQuery) contains only production data.

### Pending Actions & Ownership
*   **Action:** Proceed with Production Deployment.
    *   **Owner:** Michael Bui (Lead), Nikhil Grover (Final Approval).
    *   **Steps Required:** Create service account, request BigQuery/Osmos GCS access, deploy job, verify end-to-end functionality.
*   **Action:** Post-deployment Verification.
    *   **Owner:** Michael Bui.
    *   **Requirements:** Confirm generated file count (~500k SKUs) and compare against previous file to ensure match accuracy.

### Decisions Made
1.  **No UAT Environment:** Confirmed on 2026-01-22 that a dedicated UAT environment is impossible; testing must rely on production data integrity checks (SIT).
2.  **Risk Acceptance:** Nikhil Grover accepted the risk of proceeding to production without formal UAT sign-off on 2026-01-22, delegating the rollout call to Michael Bui.
3.  **Mitigation Strategy:** Risk of missing SKU mapping (products disappearing from campaigns) is mitigated by:
    *   Auto sanity check requiring >500k SKUs in the sync file.
    *   Manual post-deployment comparison with previous files.
    *   Hourly snapshot backups allowing immediate version rollback.

### Key Dates & Blockers
*   **2025-10-03:** Ticket created (Status: IN RELASE QUEUE).
*   **2025-12-18:** Pre-production file generation and content validation completed (>500k rows).
*   **2026-01-12:** Michael Bui flagged ticket as pending UAT for ~1 month.
*   **2026-01-22:** Final risk discussion; Grover delegates rollout approval to Bui.
*   **2026-01-26:** Michael Bui performed final verification check prior to PRD deployment request.
*   **Blocker:** None remaining on technical side; procedural sign-off was the constraint, now resolved by delegation.


## jira/QE-843: Mutation Testing Implementation - rmn-osmos-purchase-event-tracking
Source: jira | Key: QE-843 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Oktavianer Diharja | Reporter: Oktavianer Diharja | Resolution: Done | parent: QE-829 | Last Updated: 2026-03-20T14:50:24.826807+00:00
**Jira Ticket Briefing: QE-843**
**Title:** Mutation Testing Implementation - rmn-osmos-purchase-event-tracking
**Status Category:** Done
**Priority:** High
**Assignee/Reporter:** Oktavianer Diharja
**Parent Ticket:** QE-829 (Staff Excellence (Retail Media) QE Onboarding)

**Current Status**
The ticket is marked as **Done**. The work was completed in September 2025, despite the final log entry being timestamped January 26, 2026.

**Key Dates & Timeline**
*   **Aug 05, 2025:** Ticket created; identified as a Chore with High priority.
*   **Aug 07, 2025 (10:24):** Initial review revealed that while the repository (`rmn-osmos-purchase-event-tracking`) implements standard CI/CD, mutation testing was missing from Pull Requests. Status set to "On hold."
*   **Aug 07, 2025 (14:11):** Collaboration initiated; Oktavianer Diharja indicated help would be provided and tagged relevant parties (CC).
*   **Aug 13, 2025:** Task flagged for follow-up.
*   **Sep 2025:** Implementation completed (per final note).
*   **Jan 26, 2026:** Final status update confirming completion in September.

**Actions & Ownership**
*   **Pending Actions:** None. The ticket is resolved.
*   **Ownership:** Oktavianer Diharja owned the end-to-end execution and reporting.
*   **Collaboration:** Other team members were cc'd on Aug 07 to assist with adding mutation testing, though specific names of helpers are not recorded in the text provided.

**Decisions Made**
*   It was decided that the existing standard CI/CD implementation required an additional layer of mutation testing for Pull Requests.
*   The task was temporarily placed "On hold" on Aug 07 to facilitate synchronization and assistance before resuming work.

**Blockers & Notes**
*   **Initial Blocker:** Missing mutation testing configuration in the PR workflow as of early August 2025.
*   **Resolution Path:** Synchronization with stakeholders followed by implementation, resulting in completion by September 2025.


## jira/QE-842: Mutation Testing Implementation - rmn-osmos-product-feeder
Source: jira | Key: QE-842 | Status: Done (Done) | Type: Chore | Priority: High | Assignee: Oktavianer Diharja | Reporter: Oktavianer Diharja | Resolution: Done | parent: QE-829 | Last Updated: 2026-03-20T14:50:39.002843+00:00
**Jira Ticket Briefing: QE-842**

**Current Status**
*   **State:** Done / Resolved.
*   **Ticket:** QE-842 (Mutation Testing Implementation - rmn-osmos-product-feeder).
*   **Type/Priority:** Chore, High Priority.
*   **Assignee & Reporter:** Oktavianer Diharja.
*   **Parent Issue:** QE-829 (Staff Excellence (Retail Media) QE Onboarding).

**Key Timeline & History**
*   **Aug 05, 2025:** Ticket created to implement mutation testing for `rmn-osmos-product-feeder`.
*   **Aug 07, 2025 (10:08 AM):** Oktavianer identified that while the repository has standard CI/CD pipelines, mutation testing was missing from Pull Requests. Task placed on hold pending synchronization with relevant stakeholders.
*   **Aug 07, 2025 (02:12 PM):** Confirmation received to assist in adding the feature; relevant parties were notified (`cc`).
*   **Aug 13, 2025:** Task marked for follow-up.
*   **Jan 26, 2026:** Oktavianer updated the ticket status to "Done," noting implementation was completed in **September 2025**.

**Decisions Made**
*   It was confirmed that mutation testing needed to be integrated into the Pull Request workflow of the `rmn-osmos-product-feeder` repository.
*   The implementation was executed and closed, superseding the initial on-hold status from August 2025.

**Pending Actions & Ownership**
*   **No pending actions.** The ticket is resolved with a "Done" resolution.
*   **Ownership:** Fully owned by Oktavianer Diharja throughout the lifecycle.

**Blockers & Deadlines**
*   **Original Blocker (Aug 07):** Lack of mutation testing configuration in PRs required synchronization with other team members to proceed. This was resolved internally or via external coordination between August and September 2025.
*   **Deadlines:** No specific due date was set on the ticket (`duedate: null`).
*   **Implementation Window:** Confirmed completion occurred in **Sep 2025**.


## jira/DPD-1: Foundation Setups
Source: jira | Key: DPD-1 | Status: Done (Done) | Type: Epic | Priority: High | Reporter: Michael Bui | Resolution: Done | Last Updated: 2026-03-20T14:50:48.233153+00:00
**Daily Briefing Summary: DPD-1 – Foundation Setups**

**Current Status**
The epic **DPD-1: Foundation Setups**, reported by **Michael Bui** on **2026-01-14**, is officially closed. The status and resolution are both marked as **"Done"**. No assignee was designated for this task throughout its lifecycle.

**Pending Actions & Ownership**
There are no pending actions or outstanding items associated with this ticket. As the resolution is "Done," ownership of follow-up tasks has effectively transferred to subsequent workflows not visible in this specific record. The **High** priority item required by the reporter has been fulfilled.

**Decisions Made**
The primary decision recorded is the finalization and closure of the foundation setup phase. By marking the resolution as "Done" on **2026-01-14**, the team confirmed that all prerequisite activities defined under this High-priority Epic were completed to satisfaction prior to closing the ticket.

**Key Dates, Deadlines, & Blockers**
*   **Status Update Date:** 2026-01-14T14:25:32.150+0800 (Timestamp of final update).
*   **Scheduled Deadline:** None (The `duedate` field is null).
*   **Blockers:** No blockers were identified or recorded; the ticket closed without impediments.

**Technical References**
*   **Ticket ID:** DPD-1
*   **Type:** Epic
*   **Priority:** High


## jira/OMNI-1249: B2B Solution: Integration work
Source: jira | Key: OMNI-1249 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Erica Lee | Reporter: Fiona U | blocks: OMNI-1362, OMNI-1362 | discovery---connected: DPD-57 | migration_parent: PAY-7080 | polaris-work-item-link: DPD-682, PAY-7080, DPD-57 | Last Updated: 2026-03-20T14:51:11.260259+00:00
**Issue:** OMNI-1249 (B2B Solution: Integration work)
**Assignee:** Erica Lee | **Reporter:** Fiona U | **Status:** In Development (RED/AMBER) | **Priority:** High

### Current State & Impact
The B2B platform launch is currently **delayed to April 2026**. The project status fluctuated between RED and AMBER due to critical dependencies on external middleware and system integrations. The primary blocker remains the **WMS Middleware** readiness; specifically, the Go-Live date for Phase 2 (required for B2B finance/sales posting) is currently unconfirmed.

### Key Decisions & Strategic Shifts
*   **Integration Strategy:** Per Dennis, the solution will proceed with **Co-mall** on SAP (2025-12-09).
*   **Scope Adjustment:** Increased scope to include BCRS and Co-mall requirements necessitated a new sprint. No callouts from the Co-mall end are currently planned for the April timeline (2026-01-22).
*   **Architecture Clarification:**
    *   *Phase 1 (Mid-March):* DBP routes orders to PFC via SAP; SAP talks to PFC via middleware (As-Is Ecomm flow).
    *   *Phase 2:* DBP talks to PFC via Middleware. This phase is mandatory for B2B fulfillment and sales posting flows to function correctly.

### Pending Actions & Ownership
*   **WMS Middleware Status:** WMS team to walk through Phase 1 UAT plans. Confirmation needed on whether Go-Live includes Phase 2 (Critical). *Owner: WMS Team/Zi Ying Liow.*
*   **SAP Blueprint:** Pending review session with CC and Finance for sign-off (originally due 16 Jan; alignment required continues).
*   **UAT Execution:**
    *   Test case backbone creation deadline: **22 Feb**.
    *   SIT Window: **3 Mar – 6 Mar** (Ongoing as of 6 Mar).
    *   UAT Window: Planned for **23 March**.
    *   Socialization with business and Gopal scheduled for late Feb.
*   **Usability Refinements:** Feedback on B2B web/BO shared with Comall ("Project Light"); final requirements to be consolidated and sent to Comall.
*   **Critical Dependencies (Amber Status):**
    1.  **Decoupling First Mile:** Requires decision on decoupling PFC/First Mile training for MP apps prior to launch. Call scheduled for **11 March**.
    2.  **Forecasting & Reporting:** Alignment required on setup for sales order flow reporting.

### Key Dates & Deadlines
*   **WMS Phase 1 Go-Live:** Mid-March (Target).
*   **B2B Platform Go-Live:** April 2026 (Contingent on WMS Phase 2 readiness).
*   **UAT Testing:** Start date **23 March**.
*   **SAP Sign-off Review:** Originally 16 Jan; alignment still pending.

### Linked Issues & Context
*   **Blocks:** OMNI-1362
*   **Migration Parent:** PAY-7080
*   **Connected Discovery:** DPD-57, DPD-682
*   **Goal:** Scale GMV from $16M (2025) to $100M by 2030; reduce manual inquiries by 30%.


## jira/OMNI-1363: [Decoupling from SAP] Migrate CF apps to DBP to improve MP Consol fulfilment experience
Source: jira | Key: OMNI-1363 | Status: Paused (To Do) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Gopalakrishna Dhulipati | polaris-work-item-link: DST-2272, DPD-326, DPD-332, DPD-341, DST-2531, DPD-348 | Last Updated: 2026-03-20T14:51:38.924262+00:00
**Ticket:** OMNI-1363 | **Status:** Paused (Red/Delayed) | **Priority:** High
**Assignee:** Prajney Sribhashyam | **Reporter:** Gopalakrishna Dhulipati
**Linked Issues:** DST-2272, DPD-326, DPD-332, DPD-341, DST-2531, DPD-348

### Current State
The project to migrate CloudFoundry (CF) apps to DBP for MP Consolidate Fulfilment is **delayed**. While development on CF apps is complete and on track, the overall program status is Red due to dependencies on WMS Middleware. The business live date has been pushed from January 2026 to **1 April 2026**.

### Pending Actions & Ownership
*   **Timeline Confirmation:** Sathya Murthy Karthik requested an update on dates (3/11). Prajney Sribhashyam must confirm final rollout timelines with the PFC team following alignment sessions.
*   **Scope Adjustment:** Gopalakrishna Dhulipati removed Pricing scope (70 man days estimate) from this ticket; ensure Finance/Product teams are informed of the reduced scope.
*   **Change Management:** Prajney Sribhashyam previously documented Change Management & GTM, but final alignment with PFC and First Mile teams remains critical to clear risks identified in Dec 2025.

### Key Decisions Made
1.  **Live Date Shift:** Business live confirmed for **1 April 2026** (previously tentatively moved from Jan to March).
2.  **WMS Middleware Dependency:** Rollout is scheduled post-CNY due to WMS Middleware delays; this is the primary blocker.
3.  **Scope Reduction:** Ticket scope limited strictly to Fulfilment apps, excluding Pricing components.

### Critical Dates & Blockers
*   **Blocker:** WMS Middleware UAT and rollout (Post-CNY delay).
    *   WMS Middleware Production Live: **14 March 2026**
    *   DBP Order SAP Decoupling Production Live: **24 March 2026**
*   **Target Dates:**
    *   CF App Business Live: **1 April 2026** (Tech live confirmed for this date).
    *   Original UAT/Training Window: 5–9 Jan (Missed).
    *   Original Rollout Window: 12–16 Jan (Missed).
*   **Historical Data:** Contingency plan required due to historical data risk.

### Success Criteria & Impact
*   **Cost Reduction:** $170K annually ($170K -> $0).
*   **Performance:** Improve DOT% for CF sellers and enable earlier order pushes (4PM on D-1).
*   **Components involved:** First Mile Operations App, First Mile Dashboard, PFC Receiving App.


## jira/OMNI-1362: [Decoupling from SAP] Improve order orchestration with integration to WMS Middleware
Source: jira | Key: OMNI-1362 | Status: Paused (To Do) | Type: Idea | Priority: High | Assignee: Gopalakrishna Dhulipati | Reporter: Gopalakrishna Dhulipati | blocks: OMNI-1249, OMNI-1249 | polaris-work-item-link: DPD-184 | relates: OE-3209 | Last Updated: 2026-03-20T14:52:12.736574+00:00
**Ticket:** OMNI-1362: [Decoupling from SAP] Improve order orchestration with integration to WMS Middleware
**Current Status:** Red (Delayed) | **Type:** Idea | **Assignee:** Gopalakrishna Dhulipati

### 1. Current State
The program is experiencing significant delays due to the WMS Middleware rollout being pushed post-CNY. While DBP development for SAP decoupling components was initially on track, it is now blocked by the middleware timeline. SIT (System Integration Testing) between DBP OMS and WMS was completed Dec 29–30, 2025. However, additional scope was identified post-SIT requiring special logic for carton items, order types, and Boys Brigade Donation posting.

### 2. Pending Actions & Ownership
*   **Timeline Confirmation:** Sathya Murthy Karthik requested clarification on whether specific requirements must be implemented in the B2C current system or delayed until "Project Light." (Action: Check with Fenny).
*   **Date Updates:** Sathya Murthy Karthik is awaiting updates to confirm and finalize project dates.
*   **Re-group Meeting:** Scheduled for Jan 8, 2026 (historical context) to determine exact timelines; current status remains "Red" pending final confirmation of the March rollout.

### 3. Key Decisions Made
*   **Phased Rollout:** WMS Middleware team approved Phase 1 go-live initially set for Nov 17, but subsequent updates confirmed a shift to post-CNY deployment.
*   **Scope Change:** DBP required additional dev days (5 days) and specific logic implementations (carton items, order types, donation posting) discovered during/after SIT.
*   **Launch Prioritization:** CF App Business live is tentatively confirmed for April 1, 2026, while SAP decoupling requires synchronization with WMS Middleware production.

### 4. Key Dates & Blockers
*   **Blocker:** WMS Middleware UAT and rollout schedule delayed post-CNY (High Risk).
*   **SIT Completion:** Dec 29–30, 2025.
*   **WMS Middleware Production Live:** Tentatively scheduled for March 14, 2026.
*   **DBP Order SAP Decoupling Production Live:** Tentatively scheduled for March 24, 2026.
*   **CF App Business Live:** Confirmed for April 1, 2026.

### 5. Linked Issues & Context
*   **Blocks:** OMNI-1249
*   **Relates:** OE-3209; **Polaris Link:** DPD-184
*   **Validation:** UAT passed with WM6 and SAP teams. Next phase involves UAT with Business Users (E-Comm business, E-Comm operations, SAP).
*   **Risk Level:** High risk due to the post-CNY delay impacting the overall decoupling strategy required for financial compliance (GST) and fulfillment architecture.


## jira/OMNI-1294: [BCRS Compliance] Phase 2: Order Place & Returns/Refunds Processxa
Source: jira | Key: OMNI-1294 | Status: UAT (In Progress) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Winson Lim | Labels: bcrs | discovery---connected: NEDMT-2334 | polaris-work-item-link: DPD-225 | Last Updated: 2026-03-20T14:53:05.144660+00:00
**Ticket:** OMNI-1294 | **[BCRS Compliance] Phase 2: Order Place & Returns/Refunds Process**
**Status:** UAT (In Progress) | **Risk Level:** Low to Medium | **Assignee:** Prajney Sribhashyam
**Reporter:** Winson Lim | **Priority:** High

### Current Status
*   **Development:** Complete for Browse, PDP, Cart, Checkout, Order Details/History, and Sales Posting logic. Production deployment pending sign-off.
*   **UAT Progress (ETA: 20 Mar):** Active for Refunds, Pre-order Staff App, and MP SKU Creation (Seller Facing).
*   **Pending UAT:** SnG Returns (Ready ETA: 24 Mar; Target Complete: 26 Mar).
*   **Finance/CC Sign-off:** Completed for Invoice, Sales Posting, and Seller Reports. Production deployment pending.

### Pending Actions & Ownership
1.  **Production Deployment Coordination:** Finalize dates for Prod deployment of Finance flows (Sales Posting, Seller Reports) and Customer-facing flows after UAT completion. *Owner: Prajney Sribhashyam.*
2.  **UAT Execution:** Complete Refunds UAT by 26 Mar and Pre-order Staff App/Merchant SKU UAT by 20 Mar. *Owner: Testing Team/Prajney Sribhashyam.*
3.  **Finance Alignment:** Resolve OMS dependency for Seller Reports acceptance criteria. Clarify MP sales posting flows with Finance. *Owner: Prajney Sribhashyam/Finance Team.*
4.  **Data Approval:** Secure Category approval from PurSys for E-Comm SKU data updates (forms submitted by suppliers). *Owner: PurSys/Category Management.*

### Key Decisions Made
*   **Scope De-prioritization:** Personalization scope (swapping old/new SKUs in recommendations) removed to ensure the April 1 launch.
*   **Re-prioritization Strategy (Feb 12):** MP Seller listing prioritized for UAT week of Feb 23; Finance flows (Sales Posting, Invoice, Returns) scheduled for UAT starting Feb 26.
*   **Interim Solution:** Aligned on interim sales posting solution without full SAP decoupling to mitigate timeline risks.

### Key Dates & Deadlines
*   **Regulatory Milestones:** April 1, 2026 (Labeling); July 1, 2026 (Enforcement).
*   **Internal Target:** March 2026 for 100% compliance on pricing, receipts, and POS integration.
*   **UAT Completion Targets:** Mar 20 (Refunds/Pre-order/MP), Mar 24 (SnG Ready), Mar 26 (SnG Complete).

### Blockers & Risks
*   **High Risk Areas:** Invoice design changes, Returns & Refunds logic complexity, MP Seller listing.
*   **Major Issue:** In-store Pre-order flow requires resolution.
*   **Technical Dependency:** OMS dependency for finalizing Seller Reports acceptance criteria remains open.
*   **Linked Issues:** DPD-225 (Polaris), NEDMT-2334 (Discovery).


## jira/OMNI-1407: Improve seller catalogue compliance to align with FSQ expectations
Source: jira | Key: OMNI-1407 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Prajney Sribhashyam | polaris-work-item-link: DPD-100 | Last Updated: 2026-03-20T14:53:26.329514+00:00
**Jira Ticket Summary: OMNI-1407 – Improve Seller Catalogue Compliance (FSQ Alignment)**

**Current Status:**
The project is currently **In Development**. As of March 19, 2026, the start date remains unchanged. However, recent updates indicate a shift in the testing schedule due to pending Business Continuity and Risk Strategy (BCRS) work. The ticket is linked to Polaris item **DPD-100**.

**Key Dates & Deadlines:**
*   **SIT Start:** March 16, 2026.
*   **UAT Start:** March 17, 2026 (confirmed as the new target).
*   **Non-compliant SKU De-listing Deadline:** December 31 (Historical target; current focus is on system readiness).
*   **Previous Go-live Target:** February 6, 2026 (Deferred/Adjusted).

**Pending Actions & Ownership:**
*   **Update Stakeholders:** Communicate the new SIT/UAT timeline (March 16–17) to all stakeholders.
    *   *Owner:* Prajney Sribhashyam / Koklin Gan (per request on March 19).
*   **End Date Update:** Formalize and update the project end date based on current progress.
    *   *Owner:* Prajney Sribhashyam.
*   **Test Case Creation:** Develop comprehensive test cases for the compliance logic and data pipelines.
    *   *Owner:* Sathya Murthy Karthik.
*   **BCRS Work:** Complete necessary Business Continuity and Risk Strategy activities before finalizing the timeline.
    *   *Context:* Identified as a prerequisite causing the schedule adjustment.

**Decisions Made:**
*   The project start date remains consistent with previous plans, despite earlier discussions about potential delays.
*   SIT is confirmed for March 16, 2026, followed immediately by UAT on March 17, 2026.
*   **Impact Assessment:** Non-compliance carries a high risk of reputation damage and an estimated **$2.5M annual GMV loss** due to potential de-listing of ~25% of the assortment.

**Technical & Operational Context:**
The initiative automates compliance for Marketplace SKUs (e.g., HSA, Safety Mark, Halal) by implementing mandatory fields in **Mirakl** (License Code, Expiry Date). The system will enforce logic to:
1.  Trigger warnings 4 weeks and 1 week prior to expiry.
2.  Automatically disable/hide SKUs upon certification lapse.
3.  Sync SKU status between Mirakl and DBP.

The effort is estimated at **Small (30 person-days)**.


## jira/OMNI-1345: [MP Foundational] Sales Breakdown & Seller Payouts
Source: jira | Key: OMNI-1345 | Status: Paused (To Do) | Type: Idea | Priority: High | Assignee: Koklin Gan | Reporter: Prajney Sribhashyam | discovery---connected: OMNI-1178 | polaris-work-item-link: DST-2056, DST-2272, DST-2487, DPD-9 | Last Updated: 2026-03-20T14:53:46.889427+00:00
**Resource:** OMNI-1345: [MP Foundational] Sales Breakdown & Seller Payouts
**Current Status:** Paused (To Do) / Blocked since Jan 29, 2026; currently on hold as of Mar 17, 2026.

**Key Decisions**
*   **Project Hold (Mar 17):** MP Business advised a foundational change in the consolidated fulfilment business model is required due to compliance inputs and business license limitations. All work on sales breakdown reports & seller payouts is paused until these requirements are finalized.
*   **Scope Adjustment:** BCRS Compliance changes (qty, $) for Seller Report, Combined Sales Report, and Finance Concess Report have been cleared for the E-comm team. Voucher fixes, returns, refunds, and specific payout accuracy adjustments remain pending under Project Light.

**Pending Actions & Ownership**
*   **Finalize Business Requirements:** MP Leadership/Compliance to finalize consolidated fulfilment model requirements (Owner: Unspecified; Context: Prajney Sribhashyam).
*   **Report Alignment & Validation:** Runthrough of all reports (Sales Breakdown, Combined Sales, Finance Concess) with Jesslin Lim Bee Leng, Hwee Ping Lim, April Kok, and Wei Fen Ching.
    *   *Owner:* Prajney Sribhashyam, Koklin Gan.
*   **UAT Execution:** Execute User Acceptance Testing for the BCRS compliance changes.
    *   *Timeline:* Feb 23 to Jan 6 (Note: Date logic unclear in source text; likely typo, verify with team).
*   **Technical Reconciliation:** Resolve data mismatches between new BQ table (`mp_sales_breakdown`) and production reports for DF/CF.
    *   *Owner:* Sneha Parab, Data Analytics Team.

**Blockers & Dependencies**
*   **Compliance/Legal:** Business license limitations require a shift in the fulfilment model before financial reporting can proceed.
*   **Data Integrity:** Historical gaps identified between DBP finance reports and SAP regarding format and data alignment (identified Jan 29).
*   **Dependency:** Work on MP sales reports was previously placed on-hold pending SKU Compliance completion.

**Key Dates & Milestones**
*   **Original ETA (Rollout):** Jan 31, 2026 (shrink timeline attempted).
*   **Last Blocked Date:** Jan 29, 2026 (Finance reporting format alignment pending).
*   **Hold Confirmation:** Mar 17, 2026.
*   **Linked Issues:** OMNI-1178 (Discovery), DST-2056, DST-2272, DST-2487, DPD-9.

**Technical Notes**
*   Reports impacted: Seller Report (Dashboard), Combined Sales Report (Dashboard), Finance Report (DBP vs SAP mismatch).
*   Logical flow principle established for future designs: Order statement → Invoice → Sales Posting → Seller Reports → Seller Payouts. No re-calculation at any state; data must flow from confirmed previous states.


## jira/OMNI-1296: Enhanced Notification Preference Center for Multi-Channel Communication Management
Source: jira | Key: OMNI-1296 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Sip Khoon Tan | Reporter: Sip Khoon Tan | discovery---connected: CORE-304 | polaris-work-item-link: CORE-304 | Last Updated: 2026-03-20T14:54:02.607103+00:00
**Jira Ticket Summary: OMNI-1296 (Enhanced Notification Preference Center)**

**Current Status & State**
*   **Status:** In Development.
*   **Assignee/Owner:** Sip Khoon Tan (Reporter), Zi Ying Liow (Latest updates).
*   **Linked Issues:** CORE-304 (Discovery and Polaris work item).
*   **Scope:** Granular control for EDM (by business swimlane: Grocery, FP Super, FP Finest, etc.), Push Notification Service (PNS) types (transactional vs. marketing), and WhatsApp settings via a centralized interface.

**Pending Actions & Ownership**
*   **Integration Testing:** Martech team to link delivery ticket and execute integration testing between Salesforce (SFMC) and the mobile/web preference center. *Owner: Zi Ying Liow / Martech Team.*
*   **Backend Completion:** Finalize backend development by **20 February 2026**.
*   **UAT Execution:** Conduct User Acceptance Testing on **12–13 March 2026**.
*   **Go-Live Preparation:** Awaiting business direction to confirm mid-April launch.

**Key Decisions & Alignment**
*   **Stakeholder Coordination:** Collaboration confirmed with Xue Yin and William for SFMC preference center building (James Huang, 11/09).
*   **Timeline Re-alignment:** Previous "Technical live" target of Jan 7 shifted to backend completion by 20 Feb due to dependency on CCO and CRM alignment.
*   **Status Update:** Ticket status corrected to "In Development" per Sathya Murthy Karthik (11/20).

**Key Dates & Deadlines**
*   **20 Feb 2026:** Backend development completion.
*   **2 Mar 2026:** UAT readiness target.
*   **12–13 Mar 2026:** Scheduled UAT window.
*   **Mid-April 2026:** Target Go-Live (Pending business direction).

**Blockers & Rationale**
*   **Timeline Dependency:** Development timeline was revised due to pending alignment with CCO and CRM on specific timelines (18 Nov).
*   **Integration Gap:** Testing is currently halted pending the Martech team to link the delivery ticket for integration validation.

**Business Impact (Context)**
*   **Goal:** Reduce complete unsubscribe rates by 30% (EDM) to 50% (Preference Center specific), preventing an estimated $531.6k annual GMV loss ($57.6k from EDM, $474k from PNS).


## jira/OMNI-1423: [1HD] Pilot to customer launch readiness
Source: jira | Key: OMNI-1423 | Status: UAT (In Progress) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Prajney Sribhashyam | polaris-work-item-link: DPD-406 | Last Updated: 2026-03-20T14:54:15.901894+00:00
**Jira Ticket Summary: OMNI-1423 ([1HD] Pilot to customer launch readiness)**
**Status:** UAT (In Progress) | **Priority:** High | **Assignee:** Rajesh Dobariya | **Reporter:** Prajney Sribhashyam
**Linked Issue:** DPD-406

**Current State**
The project is targeting a **7th April launch**. Development has moved from initial UAT to production testing.
*   **UAT Status:** First round completed on 10 March; currently investigating bugs discovered during this phase.
*   **Production Testing:** Started on 18 March with the team identifying data issues regarding "bulk threshold." Root Cause (RC) analysis and fixes are ongoing as of 19 March.

**Pending Actions & Ownership**
*   **Rajesh Dobariya:** Investigating root cause of bulk threshold data issues; providing ETA updates by EOD 11 March (for UAT bugs); updating tech live and biz live dates.
*   **Team/Technical:** Fixing identified production testing bugs and data integrity issues.

**Key Decisions Made**
*   **MVP Scope Split (20 Feb):** To align with business requirements, the delivery was split into "now" and "later" phases. Non-blocker items were moved to a new epic on 27 February.
*   **Launch Schedule:** Confirmed on-track status for 7 April launch pending successful completion of remaining production rounds.

**Key Dates & Deadlines**
*   **18 March:** Production testing commenced.
*   **19 March:** Continuation of second round of production testing (internal).
*   **Week starting 24 March:** Second round of production testing scheduled with Business, Finance, and Ops stakeholders.
*   **31 March:** Third round (End-to-End) testing with 3PL (contingent on SOP alignment and driver availability).
*   **7 April:** Targeted customer launch date.
*   **19 Feb (Historical):** Deadline for MVP split decision.

**Blockers & Risks**
*   **Data Issues:** Current production test is hindered by bulk threshold data inconsistencies; root cause identification is pending.
*   **Dependencies:** 31 March E2E testing with 3PL depends on final alignment of SOPs with Ops and confirmed driver availability.


## jira/OMNI-1425: [1HD] Phase 2 - Build to enable scaling of 1 hour to 100 stores
Source: jira | Key: OMNI-1425 | Status: Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Rajesh Dobariya | polaris-work-item-link: DPD-627 | Last Updated: 2026-03-20T14:54:30.007620+00:00
**Jira Ticket Summary: OMNI-1425**
**Subject:** [1HD] Phase 2 - Build to enable scaling of 1 hour to 100 stores
**Assignee/Reporter:** Rajesh Dobariya | **Priority:** High | **Status:** To Do (Prioritised)

### Current Status
The ticket is currently in the "To Do" phase, marked as a Work In Progress (WIP). The initial scope defined includes 3PL integration, picker app enhancements, store creation processes, FFS store handling, and financial treatment. However, recent discussions have significantly narrowed the immediate scope.

### Key Decisions & Scope Changes
*   **Feature Removal:** It was decided during a discussion that adding a "delivery ticket" for the week starting 23rd March is **not required** for the launch (Update: 2026-02-27).
*   **JTBD Update:** Koklin Gan updated the Jobs To Be Done (JTBD) section on 2026-03-18 and requested updates to the remaining sections of the description.

### Pending Actions & Ownership
*   **Business Impact & Timeline:** Rajesh Dobariya is waiting for business stakeholders to provide specific data on the impact and timeline required for scaling from the current pilot to 100 stores. Once received, he will update the ticket accordingly (Status as of 2026-03-19).
*   **Solution Definition:** The actual scope and effort estimation cannot be finalized until the Solution design is defined and 3PL requirements are clarified.
*   **Description Completion:** Rajesh Dobariya must update the "Business Impact," "Product Metrics Impact," "Operational Processes," and "Business Rules" sections based on the clarified business inputs and revised JTBD.

### Key Dates & Blockers
*   **2026-03-19:** Last status update indicating dependency on external clarity.
*   **Blocker:** Lack of defined Solution design and 3PL requirements prevents accurate effort estimation and scope finalization.
*   **Dependency:** Requires input from business stakeholders regarding financial impact metrics (e.g., AOV increase, Perfect Order rates) to complete the ticket.

### Technical References & Linked Items
*   **Linked Issue:** DPD-627 (Polaris work item link).
*   **Context:** The initiative aims to eliminate manual order handling and reduce errors when scaling 1-hour delivery to 100 stores, though immediate launch requirements have been de-scoped.


## jira/OMNI-1414: Integrate personalized gamification challenge with FP app
Source: jira | Key: OMNI-1414 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: James Huang | polaris-work-item-link: DPD-297 | Last Updated: 2026-03-20T14:54:52.307387+00:00
**Ticket:** OMNI-1414 (Idea) | **Priority:** High | **Assignee:** Rajesh Dobariya | **Reporter:** James Huang
**Linked Issue:** DPD-297
**Current Status:** In Development / In Progress

### Current State
Backend development for the UntieNot gamification integration has commenced as of March 11, 2026. The project involves integrating a personalized challenge platform with the FP app to target DCC shoppers and marketers. The technical approach requires hashing Customer UID using SHA256 + salt ('s@veValue!') before passing it via URL webview (per Alvin Choo).

Total effort estimated at 3 man-weeks:
*   **Frontend:** 2 weeks across platforms (OMNI Homepage, Rewards page, PNW Banner, Popup, Voucher Wallet, Rewards Tile).
*   **Backend:** 1 week.

### Pending Actions & Ownership
*   **Technical Finalization:** Rajesh Dobariya must align/finalize the technical approach by February 20th (Note: Dates in log suggest this task may be retrospective or requires re-confirmation against current timeline).
*   **UAT Execution:** Scheduled for **March 27, 2026** (Rescheduled to prioritize "Project Light"). Owner: Rajesh Dobariya.
*   **Launch Planning:** Business live date is TBD pending issues identified by UntieNot. The team must communicate delivery dates to the CCO team for launch planning. Owner: Rajesh Dobariya/James Huang.

### Key Decisions & Estimates
*   **Data Handoff:** James Huang confirmed a mapping file of Customer UID to personalized challenge page URLs will be provided in the 1st week of February (estimated).
*   **Uplift Justification:** Despite initial skepticism regarding MVP uplift, James Huang reiterated the projection: $8M incremental GMV based on scaling from 938K DCC (pilot) to 1.7M DCC over 8 months, extrapolating from $400K/month baseline.
*   **Timeline Shift:** UAT moved from March 24th to March 27th; Technical Live rescheduled from March 30th to **April 2nd** (allowing a 1-week buffer for post-UAT fixes).

### Key Dates & Deadlines
*   **Feb 20, 2026:** Deadline to finalize technical approach.
*   **Mar 27, 2026:** Scheduled UAT start.
*   **Apr 2, 2026:** Target Technical Live date.
*   **TBD:** Business Live date (contingent on UntieNot feedback).

### Blockers & Risks
*   **Business Readiness:** Launch timeline is currently blocked by the "Business side" for finalizing the go-live date pending UntieNot issue identification.
*   **Prioritization:** UAT was rescheduled specifically to accommodate work on "Project Light," indicating resource contention or priority shifts.


## jira/OMNI-1420: Enable all 3P domain links to open in the in-app browser from banner redirection
Source: jira | Key: OMNI-1420 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-372 | Last Updated: 2026-03-20T14:55:09.351726+00:00
**Jira Ticket Summary: OMNI-1420**
**Subject:** Enable all 3P domain links to open in the in-app browser from banner redirection.
**Current Status:** In Development (In Progress) | **Assignee:** Nikhil Grover | **Priority:** High | **Linked Issue:** DPD-372

**Current State & Key Decisions**
*   **Problem:** Non-endemic campaigns currently require app updates for domain whitelisting, causing up to a 4-week lead time and slowing the RMN BD sales cycle. Target business impact is up to $500K in GMV.
*   **Security Decision (2026-02-11):** Cyber security rejected removing whitelisting entirely, citing other app use cases. The team aligned on a backend-managed solution where whitelists do not require app updates.
*   **Technical Constraint (2026-02-12):** Winson Lim clarified that "Split" (an experimental flagging platform) cannot be used for operational whitelisting. Sathya Murthy Karthik and Nikhil Grover confirmed the final solution architecture excludes Split.
*   **Resource Strategy:** Initially considered external resources, but business aligned on using internal resources after Accenture indicated a 7-8 week commitment time (2026-03-11).

**Pending Actions & Ownership**
*   **Front-end Development:** Nikhil Grover is awaiting the completion of "UntieNots" tasks before starting front-end work. Current ETA for start: Second half of the week of March 16, 2026.
*   **Resource Augmentation:** Business confirmation on resource augmentation was previously awaited (as of 2026-02-19); however, the decision to proceed with internal resources was confirmed on 2026-03-11.

**Key Dates & Blockers**
*   **Effort Estimate:** 2 man weeks total (1 week per platform).
*   **Blocker/Dependency:** The start of front-end work is blocked by the completion of "UntieNots." No other active blockers are noted as of March 11, 2026.

**Summary of Chronology**
*   *Jan 29:* Ticket created; initial proposal involved backend whitelisting but considered Split for implementation.
*   *Feb 11:* Cyber security ruled out removing whitelisting; backend-only solution approved.
*   *Feb 12:* Winson Lim rejected Split as a technical component; ROI updated by Sathya Murthy Karthik based on new estimates.
*   *Feb 13:* Danielle Lee requested assignee update; Nikhil Grover confirmed ownership transfer.
*   *Mar 11:* Accenture resource timeline (7-8 weeks) deemed too long; business aligned to use internal resources instead. Front-end start date set for the week of March 16 pending "UntieNots" completion.


## jira/OMNI-1429: Activate product ads on all Omni homepage swimlanes
Source: jira | Key: OMNI-1429 | Status: UAT (In Progress) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-710 | Last Updated: 2026-03-20T14:55:19.972732+00:00
**Jira Ticket Briefing: OMNI-1429**

**Current Status**
*   **State:** In Progress (UAT).
*   **Assignee:** Nikhil Grover.
*   **Type:** Idea (High Priority).
*   **Linked Issue:** DPD-710.

**Objective & Business Case**
The initiative aims to activate product ads in slots 3, 5, and 7 across all Omni homepage swimlanes (excluding the Past Purchase swimlane where ads currently only appear in slots 1 and 3). This allows the RMN/Products team to keep top slots for relevant products while maximizing monetization.
*   **Proposed Solution:** Configure product ad slots via Split; no app changes required.
*   **Estimated Effort:** 3–4 man days.
*   **Financial Impact:** Expected incremental revenue of $750K p.a.; projected $312K for 2026 (5-month impact).

**Pending Actions & Ownership**
*   **Action:** Update "new tech live" and "biz live" dates.
*   **Owner:** Nikhil Grover.
*   **Context:** Requested by Danielle Lee on March 17, 2026.

**Decisions Made**
*   Confirmed that the solution requires only configuration in Split to fetch ads based on slot counts and sequence products accordingly.
*   No changes required for operational processes, business rules, or go-to-market strategies.

**Key Dates & Blockers**
*   **Last Update:** March 17, 2026 (Request for date updates).
*   **Blockers/Dependencies:** None currently listed; awaiting the specific live dates from the assignee to finalize the timeline.


## jira/OMNI-1421: Transition from fixed-tenancy to impressions-based banner delivery model
Source: jira | Key: OMNI-1421 | Status: Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-385 | Last Updated: 2026-03-20T14:55:33.991315+00:00
**Jira Ticket Briefing: OMNI-1421**

**Current Status:** Prioritised / To Do (High Priority)
The initiative is an "Idea" type ticket aimed at transitioning the RMN banner delivery model from fixed tenancy to impressions-based allocation. As of March 11, the project is in a pre-development phase awaiting prerequisite work.

**Key Decisions & Strategy:**
*   **Model Shift:** Moving from per-week fixed slots to an impressions-based system (launching April 1).
*   **Financial Target:** Projected incremental revenue of **$900k p.a.** (based on freeing up 40% inventory and a 60% sell-through rate at $10 CPM).
*   **Prerequisites:** Implementation is contingent upon the completion of **OMNI-1429** (activation of product ads on Omni homepage swimlanes).

**Pending Actions & Ownership:**
*   **Nikhil Grover (Assignee/Reporter):** Currently finalizing the solution definition. Must complete this work to enable development.
    *   *Previous Deadline:* February 27 (missed/unmet in favor of dependency on OMNI-1429).
    *   *New Target:* Complete solution finalization and initiate execution by **March end**.
*   **Ad Ops & Platform Ops:** Required to align on Standard Operating Procedures (SOP) for the new impressions-based model.

**Key Dates & Deadlines:**
*   **Feb 27:** Original target for solution finalization (superseded).
*   **Mar 11:** Status update confirming dependency on OMNI-1429.
*   **March End:** Target completion date for the current phase/solution definition.
*   **April 1:** Expected launch window for updating packages to the impressions-based model.

**Dependencies & Blockers:**
*   **Primary Dependency:** Completion of ticket **OMNI-1429**. The team will not start work on OMNI-1421 until this activation is complete.
*   **Linked Issue:** Polaris work item link **DPD-385**.

**Business Impact Summary:**
The transition aims to solve low relevance and frequency capping issues in the current fixed-slot model. By shifting 70% of package budgets to product ads, the goal is to increase customer relevance, improve traffic efficiency (maximize dollars per traffic), and allow RMN BD users to sell more campaigns by maximizing exposed inventory.


## jira/OMNI-1416: FP Pay experience improvements to support new auto apply voucher at IPOS/KPOS 
Source: jira | Key: OMNI-1416 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Rajesh Dobariya | duplicate: CPR-4 | Last Updated: 2026-03-20T14:55:50.937082+00:00
**Jira Briefing: OMNI-1416 – FP Pay Experience Improvements (Auto-Apply Voucher)**

**Current Status:**
*   **State:** In Development / High Priority.
*   **Progress:** Core Product Team (Tiong Siong's team) has completed 67% of the work; it is tracked on the Core Product Roadmap, not OMNI capacity.
*   **Dependencies:** Pending API availability from Hengky's team for DSP integration to fetch vouchers in "browse-only" mode within FP Pay.

**Pending Actions & Owners:**
1.  **Effort Estimation & ETA:** The assignee (Rajesh Dobariya) needs to obtain the Estimated Time of Arrival (ETA) and effort estimation for remaining work from the Core Product team based on their roadmap priority.
2.  **API Delivery:** Hengky's team must provide the necessary APIs to enable FP Pay integration with DSP to surface in-store offers. This is a blocker for the "Interim" phase launch.
3.  **Alignment Meetings:** Rajesh Dobariya previously noted the need to align on the final FP Pay experience (RB & Kopitiam) with Koklin and Qiuyan for App Exco review.

**Decisions Made:**
*   **Architecture Shift:** FP Pay is transitioning from a redemption execution layer to purely a "discovery and visibility surface." POS systems (IPOS/KPOS) will become the single source of truth for offer logic, eligibility, and auto-application.
*   **Ticket Classification Clarification:** On [2026-03-17], it was confirmed that this delivery is owned by the Core Product Team. Since OMNI resources are not consuming capacity for the majority of the work, there is an open question regarding whether tracking via OMNI ticketing is strictly necessary, though the ticket remains active for coordination.
*   **Transition Strategy:** A phased approach (July–Sep 2026) is agreed upon to minimize disruption, shifting redemption authority from Offer Service to POS gradually.

**Key Dates & Blockers:**
*   **Target Launch (Interim):** July 2026 (requires DSP API integration and BE work completion).
*   **End State Target:** September 2026 onwards (POS handles all voucher types, including EVs/Bank vouchers; Offer Service retired).
*   **Blockers:**
    *   Pending API evaluation and delivery from Hengky's team.
    *   Alignment on IPOS timeline for fetching applicable vouchers based on user profiles from DSP.
*   **Related Issues:** Linked as a duplicate to `CPR-4`.

**Summary of Work Scope:**
The initiative addresses compliance risks (treating vouchers as payment methods) and poor UX (manual selection, friction). The solution involves Digital Center becoming the canonical offer engine. Currently, the "Interim" state requires FP Pay to fetch eligible offers from DSP for browsing only, while IPOS handles redemption logic.


## jira/OMNI-1300: GST Compliance Phase 2 - Refunds and return
Source: jira | Key: OMNI-1300 | Status: Define (In Progress) | Type: Idea | Priority: High | Assignee: Alvin Choo | Reporter: Sathya Murthy Karthik | Labels: GST | polaris-work-item-link: CORE-51, PAY-6725 | Last Updated: 2026-03-20T14:56:05.624316+00:00
**Jira Ticket Summary: OMNI-1300 (GST Compliance Phase 2)**

**Status Overview**
*   **Current State:** Define / In Progress.
*   **Assignee:** Alvin Choo.
*   **Priority:** High.
*   **Linked Issues:** CORE-51, PAY-6725.
*   **Context:** The project aims to resolve incorrect GST calculations in refund processing for FairPrice retail and marketplace orders (affecting ~5% of returns).

**Key Decisions Made**
*   **Strategic Split (Jan 2026):** Based on the Jan 5, 2026 discussion with the SAP Team:
    *   **Replatform:** Return and refund functionality is now scoped for the replatform initiative.
    *   **BCRS (Current System):** Will continue using the existing RPA-based refund process; OMNI-1300 focuses on refining this interim flow.
*   **Steerco Escalation:** On Mar 20, Koklin Gan flagged that as a critical compliance topic, it requires steering committee decision-making.

**Pending Actions & Owners**
1.  **Stakeholder Alignment:** Share the action plan for Corporate Control (CC) and Ecom Business to align on refund calculations. Owner: Aditi Rathi / Team.
2.  **RPA API Integration:** Meeting scheduled/confirmed with the RPA team (Dec 10, 2025 context) to share API documentation regarding refund simulation and order confirmation APIs.
3.  **Calculation Confirmation:** Finalize refund calculation logic with CC and Business stakeholders. Owner: Aditi Rathi (Targeted for W48/W49).

**Key Dates & Timeline**
*   **Nov 12, 2025:** Kick-off with development team completed.
*   **Dec 9-10, 2025:** Draft refund calculation ready; API documentation finalized; RPA team meeting scheduled.
*   **Jan 5, 2026:** SAP Team discussion held (established the Replatform vs. BRS split).
*   **Mar 20, 2026:** Topic flagged for Steerco review.

**Blockers & Risks**
*   **Compliance Risk:** Current manual GST adjustments cause errors and regulatory exposure.
*   **API Gaps:** RPA requires a "Refund simulation API" (to reply to customers) and an "Order+SKU refund confirmation API" prior to processing.
*   **Stakeholder Delays:** Previous meetings with Corporate Control, Business, and Finance were cancelled or delayed; alignment remains pending.


## jira/OMNI-1235: AI shopping assistant: An engaging experience for customers to build their shopping cart within seconds
Source: jira | Key: OMNI-1235 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Koklin Gan | Reporter: Koklin Gan | polaris-merge-work-item-link: OMNI-1237 | polaris-work-item-link: DPD-293 | Last Updated: 2026-03-20T14:56:23.953156+00:00
**Ticket:** OMNI-1235 (AI shopping assistant)
**Current Status:** Deprioritized to "Next" | **Priority:** High | **Assignee:** Koklin Gan
**Linked Issues:** OMNI-1237, DPD-293

### Current State & Decisions
*   **Deprioritization:** The initiative was moved to the "Next" queue on 2025-09-30 due to delays in defining business use cases.
*   **Re-evaluation:** On 2026-01-13, Vivian Lim Yu Qian confirmed design resource availability and requested reactivation for a discovery phase.
*   **Scope Definition (Jan 2026):** A "lean" effort estimation was established with specific constraints:
    *   **Timeline:** 8 weeks total (3 weeks Design, 3 weeks Web/Android App dev only, 2 weeks Backend).
    *   **Functionality:** System will display products but **cannot** add items directly to the cart; users must navigate to the Product Detail Page (PDP) to purchase.
    *   **Data Limitations:** No conversation history context will be passed between sessions.
    *   **Search Optimization:** Must pass Store ID to improve search relevance.

### Pending Actions & Ownership
*   **Trigger:** Initiate discovery phase now that design resources are confirmed (per Peter Talbot, 2026-01-13).
*   **Validation:** Koklin Gan previously noted a meeting with Trollee was held on 2025-08-13 to review capabilities (Demo link: `ai-agent-fpg.trollee.com/chat`). Further validation of business use cases is required before full development.
*   **Design & Dev:** Assign design and engineering resources based on the Jan 2026 estimation (Android/Web focus).

### Key Dates & History
*   **2025-04-16:** Idea created by Koklin Gan to solve inefficient search/scrolling.
*   **2025-08-05:** Conceptual complexity rated as 3; concerns raised regarding feature discoverability and search impact.
*   **2025-08-13:** Peter Talbot requested Product Requirements (PRD) and scalability plans for Omni Home/PDP/In-store. Koklin Gan scheduled Trollee meeting to scope.
*   **2025-09-03:** Target set: Close use cases by 09/09, PRD by 09/12, work start by 09/12.
*   **2025-09-11:** Delay reported; PRD deadline extended to 09/18.
*   **2025-09-30:** Ticket deprioritized.
*   **2026-01-13:** Effort estimation finalized (8 weeks lean scope); request to proceed with discovery.

### Blockers & Risks
*   **Scope Reduction:** The inability to add to cart directly and the lack of conversation context may impact user conversion metrics compared to the original vision.
*   **Platform Limitation:** Development is restricted to Web and Android only (iOS excluded in current estimate).
*   **PRD Status:** Business use cases were delayed in September; a finalized PRD linked to the Jan 2026 scope must be confirmed before engineering begins.


## jira/OMNI-1153: Enable WhatsApp Marketing Consent at Sign-Up Page and Preference Center to Unlock Better Engagement Opportunities
Source: jira | Key: OMNI-1153 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Ravi Goel | Reporter: Yadear Zhang | Labels: app-engagement | polaris-merge-work-item-link: OMNI-1152 | Last Updated: 2026-03-20T14:57:19.825725+00:00
**Jira Ticket Summary: OMNI-1153**
**Subject:** Enable WhatsApp Marketing Consent at Sign-Up Page and Preference Center

**Current Status**
The ticket is currently **In Development**. However, recent updates indicate the scope for this specific feature is being re-evaluated to align with a broader initiative. The current baseline involves adding WhatsApp consent options to the sign-up page and preference center to leverage high open rates (77% vs. 30-40% for email).

**Key Decisions Made**
*   **Scope Integration:** It was decided that enabling WhatsApp marketing consent should not be a standalone effort but must be integrated into the **"revamp of the login/signup experience"** (Linked Issue: **OMNI-1152**). This prevents duplicate work and aligns with the CCO initiative.
*   **Validation Path:** The feature relies on recent pilot data showing 77% transactional message open rates to justify marketing expansion.

**Pending Actions & Ownership**
*   **Final Scope Confirmation:** Danielle Lee noted the item was marked "require further discussion" and tasked the team with confirming inclusion in the onboarding revamp scope by March 6, 2025 (referenced as "close this tomorrow" in March logs). The latest instruction confirms it is now designated for OMNI-1152.
*   **Impact Analysis:** Koklin Gan was seeking an impact analysis prior to prioritization; this appears to be the gating factor before full commitment.
*   **Marketing Planning:** Nghi (Nghi) is responsible for planning WhatsApp marketing use cases and defining strategies to nudge customers into providing consent once the technical base is established.

**Timeline & Technical Estimates**
*   **Technical Effort:** Estimated at 2 weeks for backend, plus 1 week each for iOS, Android, and Web (Flora Wo Ke).
*   **Projected Outcome Goal:** Targeting ~89,000 user consents over 6 months based on 35,000 monthly sign-ups.

**Blockers & Risks**
*   **Dependency Conflict:** Initial concern raised by Ryne Cheow regarding potential clashes with the CCO login/signup revamp. Resolved via alignment to include WhatsApp consent within that larger scope.
*   **Technical Uncertainty:** Noted as level "1" early in the thread; currently being addressed through integration planning.

**Stakeholders & Metadata**
*   **Assignee:** Ravi Goel
*   **Reporter:** Yadear Zhang
*   **Key Contributors:** Ryne Cheow, Koklin Gan, Danielle Lee, Flora Wo Ke, Nghi (Marketing), SSO onboarding team.
*   **Linked Issues:** OMNI-1152 (Polaris merge work item).
*   **Priority:** High | **Labels:** app-engagement


## jira/OMNI-1246: Support the SIT/UAT/Beta/Cut Over for MyInfo and LEAP core system integration
Source: jira | Key: OMNI-1246 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Ryne Cheow | Reporter: James Huang | polaris-merge-work-item-link: OMNI-1169 | Last Updated: 2026-03-20T14:57:50.407407+00:00
**Daily Briefing Summary: OMNI-1246**

**Current Status**
*   **Ticket ID:** OMNI-1246
*   **State:** Backlog (To Do)
*   **Type:** Idea
*   **Priority:** High
*   **Reporter:** James Huang
*   **Assignee:** Ryne Cheow
*   **Linked Issue:** OMNI-1169 (Polaris merge work item link)

**Pending Actions & Ownership**
The following actions require execution to move this idea toward prioritization:
*   **Integration Planning:** Work with the LEAP team on the SIT/UAT/Beta/Cutover plan for necessary integration with the LEAP middleware. Owner: Ryne Cheow (and LEAP team).
*   **Quality Assurance:** Participate in test and validation activities. Owner: Ryne Cheow.
*   **Development:** Develop new onboarding journeys and force update journeys. Owner: Ryne Cheow.
*   **Defect Management:** Address bug fixes and the "SG 60" mechanic implementation. Owner: Ryne Cheow (and LEAP team).

**Decisions Made**
*   No formal decisions were recorded in the chronological log; the ticket currently represents a proposed scope rather than an approved execution plan.
*   The problem definition was validated by identifying CHAS large family customers and new/existing customers as key stakeholders requiring fast-track onboarding, profile validation, and invisible service disruption during backend changes (CDM/LMS).

**Key Dates, Deadlines, & Blockers**
*   **Target Metrics:** Increase customer data quality index from 29% to 80%; reduce checkout time for CHAS large family customers via automated POS discounts.
*   **Timeline/Blockers:** The "Assumptions" section notes an assumed timeline exists but no specific dates are provided in the ticket. Consequently, there is currently no fixed deadline or defined blocker preventing immediate planning, other than the need to finalize the integration plan with the LEAP team.

**Summary of Scope**
This initiative supports the MyInfo and LEAP core system integration across SIT, UAT, Beta, and Cutover phases. The goal is to enable SG 60 large family discounts for CHAS members, fast-track onboarding via MyInfo, and ensure system stability during backend updates.


## jira/OMNI-1361: Achieve 100% GST compliance for Ecom orders 
Source: jira | Key: OMNI-1361 | Status: Discovery (To Do) | Type: Idea | Priority: High | Assignee: Alvin Choo | Reporter: Gopalakrishna Dhulipati | polaris-work-item-link: PAY-6785 | Last Updated: 2026-03-20T14:58:07.295595+00:00
**Ticket:** OMNI-1361 (Achieve 100% GST compliance for Ecom orders)
**Assignee:** Alvin Choo | **Reporter:** Gopalakrishna Dhulipati | **Priority:** High
**Linked Issue:** PAY-6785 (Polaris work item link)

**Current Status**
*   **State:** Discovery (To Do).
*   **Strategic Direction:** Confirmed via discussion with the SAP Team on 05 Jan 2026. The "SAP Decoupling" initiative will be covered under a replatform project.
*   **Specific Logic Agreements:**
    *   **BCRS Deposit:** Will continue with existing SAP posting methods.
    *   **Post-BCRS Deposit (Per Order):** Switching to monthly aggregation for posting to SAP.

**Pending Actions & Ownership**
*   **Plan Alignment:** Alvin Choo must share the plan of action with Corporate Control and Ecom Biz for alignment.
*   **Finance Requirements:** Pending Finance team requirements for SAP-to-Finance aggregate posting (specifically data fields needed). This is owned by the SAP team (identified as an important piece in W48).
*   **Connector Decision:** Pending decision on whether to post via Comall Connector or directly to SAP. A chaser was sent on 27 Nov to Sophia (Comall); reply regarding the SAP connector (currently built under B2B project) is awaited.
*   **Mapping Confirmation:** Working with Finance to confirm GL Code mapping and Condition Type mapping.

**Key Decisions Made**
*   **Posting Strategy:** Finalized that DBP will hold all Price, Promo, and GST logic, while SAP will no longer carry business/financial logic (decoupling). SAP receives updates on order changes in the final state only.
*   **Replatforming Scope:** The decoupling architecture is now scoped to the replatform project rather than immediate execution within this specific ticket's current sprint scope.

**Dates, Deadlines & Blockers**
*   **09 Nov 2025 (W48):** New SAP posting approach aligned; Finance requirements identified as pending.
*   **16-22 Nov 2025 (W49):** Workshop planned to resolve open questions regarding DBP-to-SAP posting, GL mapping, and Condition Type mapping.
*   **27 Nov 2025:** Chaser sent to Sophia (Comall) for connector decision; reply still awaited.
*   **06 Dec 2025 (W51):** Ongoing discussions with SAP Team, PM, and Tech regarding the posting approach.
*   **05 Jan 2026:** Latest strategic alignment confirmed (Replatform vs. BCRS deposit logic).
*   **Blocker:** Decision on the technical method of posting (Comall Connector vs. Direct) is pending a response from Comall. Finance data requirements for aggregate posting remain outstanding.


## jira/OMNI-1227: FPG - Fraud detect and prevention 
Source: jira | Key: OMNI-1227 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Aditi Rathi | Reporter: Koklin Gan | discovery---connected: OMNI-1075, OMNI-1134 | polaris-merge-work-item-link: OMNI-1075 | Last Updated: 2026-03-20T14:58:25.942194+00:00
### Daily Briefing: OMNI-1227 (FPG - Fraud Detect & Prevention)

**Current Status:**
*   **Ticket State:** To Do / Soft Prioritized.
*   **Assignee:** Aditi Rathi (Owner).
*   **Project Context:** High-priority initiative stemming from the Risk team's "Fraud Detection and Prevention" project. Focuses on reducing financial/reputational risk via automated prevention at the order placement touchpoint, excluding onboarding journey changes (already addressed by Nov releases).

**Key Decisions & Progress:**
*   **Scope Definition:** Confirmed exclusion of onboarding changes; focus is strictly on **transactional surveillance**.
*   **Partial Implementation:**
    *   *Onboarding:* New/Manual/MyInfo onboarding released (Nov 5 & 24) to address voucher abuse via multiple accounts.
    *   *Vouchers:* Restriction of E-Voucher redemption for Marketplace items released Oct 7.
*   **Proposed Solution:** Build a Real-time Fraud Engine (DS-driven) with a Backoffice Control Portal.
    *   **Logic:** Score transactions as LOW (pass), MEDIUM (flag for review), or HIGH (block).
    *   **Effort Estimates:** DS/DE integration estimated at 8 weeks; DPD Fulfilment (orchestration + portal) at 4 weeks (1 BE, 3 FE).
*   **Risk Identified:** Integrating the fraud engine adds latency to the Order Placement SLO.

**Pending Actions & Ownership:**
*   **Technical Solution Proposal:** Aditi Rathi is meeting with DS and Tech teams (planned for week of Oct 8) to brainstorm options and present business alignment by **Oct 15**. *Note: Timeline checks indicate this target has passed; current status is "WIP".*
*   **Owner Transition:** Danielle Lee queried new ownership on Feb 13, 2026. Koklin Gan reaffirmed focus on transactional surveillance in March 2026.
*   **Resource/Feasibility Review (Critical):** Rajesh Dobariya requested assessment of feasibility within the "current app" vs. "Project Light." He asked to move this ticket out of the board if realizable timelines cannot be met due to resource constraints, to provide stakeholder visibility.

**Key Dates & Blockers:**
*   **2025-10-15:** Target for presenting potential tech options (Status: Likely missed/overdue).
*   **Current Blocker:** Unclear ownership status and lack of concrete timeline due to resource prioritization ("Project Light" constraints).
*   **Upcoming:** Need to resolve whether this moves to a separate backlog or remains active with adjusted expectations.

**Metrics & Impact (Baseline):**
*   **Risk:** 27 incidents (90 transactions) cancelled manually (Apr-Jul 2025); potential $100k annual voucher abuse loss.
*   **Ops Cost:** Currently consumes 4-6 hours/week across Ecom Business and CS teams for manual review. Automation aims to reduce this significantly.


## jira/OMNI-1208: Mirakl foundational work for scalability
Source: jira | Key: OMNI-1208 | Status: Discovery (To Do) | Type: Idea | Priority: High | Assignee: Koklin Gan | Reporter: Koklin Gan | blocks: DST-2247 | discovery---connected: OMNI-1178 | polaris-work-item-link: DST-2247, DPD-326, DPD-332, DST-2277, DPD-543, DST-2305 | Last Updated: 2026-03-20T14:58:43.544572+00:00
**Jira Ticket Briefing: OMNI-1208 (Mirakl Foundational Work)**

**Current Status**
The ticket **OMNI-1208** is currently in the **"Discovery"** phase with a status category of "To Do." However, per the latest comment on **April 30** by **Koklin Gan**, the epic is being retired ("killed") as it served only for parent visibility. Consequently, no active development or execution is planned under this specific ticket ID.

**Key Actions & Ownership (Historical)**
*   **Complexity Estimation:** Multiple requests were made by **Koklin Gan** between March 6 and April 12 to obtain complexity estimates from the engineering team.
    *   **Alvin Choo** provided initial estimates: "BE two backend" at 12 weeks (March 18), later updated to "4 weeks for Vouchers created in DBP should be calculated into Mirakl" if Option 1 is selected (April 7).
    *   **Gopalakrishna Dhulipati** provided a conflicting estimate of "2 BE x 20 weeks = 40 weeks" (March 23).
*   **User Story Input:** As noted by **Fiona U** on April 4, the team was pending user stories from **KL** and **Aditi**, with a target completion window of two weeks.

**Decisions Made**
*   **Project Termination:** The decisive action taken on **April 30** by **Koklin Gan** was to decommission the epic "OMNI-1208." This indicates that the foundational work outlined (financial recalculations, catalogue accuracy, Mirakl <> DBP <> SAP architecture) will not proceed under this specific initiative.

**Key Dates & Blockers**
*   **March 5:** Ticket created with high priority to address financial discrepancies and seller trust issues.
*   **March 18 – April 7:** Back-and-forth regarding backend complexity estimates (ranging from 4 to 40 weeks).
*   **April 4:** Update indicating pending deliverables from KL and Aditi were the immediate blocker for progress.
*   **April 30:** Final status update; project closed.

**Technical & Linkage Context**
*   **Primary Dependency:** Linked to **OMNI-1178**.
*   **Blocked Items:** Blocks **DST-2247** (also linked as a Polaris work item).
*   **Related Polaris Items:** DPD-326, DPD-332, DST-2277, DPD-543, DST-2305.
*   **Scope Issues Identified:** Incorrect billing/revenue collection from sellers due to gaps in refund, cancellation, dropoff, and voucher creation visibility; reliance on manual workarounds; need for a single source of truth for billing/sales orders.

**Summary**
Despite high priority and detailed problem definitions regarding financial integrity and scalability, the initiative was halted following estimation disputes and pending user story inputs from **KL** and **Aditi**. The ticket is now closed with no further action required on this specific Epic ID.


## jira/OMNI-1242: [Pre-order] 'Mark as Paid' for In-Store Preorders
Source: jira | Key: OMNI-1242 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Fiona U | Labels: Preorder | polaris-work-item-link: PA-330 | Last Updated: 2026-03-20T14:58:59.120852+00:00
**Jira Ticket Summary: OMNI-1242 [Pre-order] 'Mark as Paid' for In-Store Preorders**

**Current Status**
*   **State:** Backlog (To Do).
*   **Resolution:** The ticket is marked to be deleted; the initiative will be covered by a future "re-platform" effort.
*   **Assignee:** Rajesh Dobariya (initially assigned); Ravi Goel looped in on 2025-07-03.
*   **Priority:** High | **Type:** Idea.

**Key Decisions & Outcomes**
*   **Technical Approach:** The team defined a two-step automation flow: (1) POS publishes payments to PubSub; (2) DBP reads these events to 'Mark as Paid' on relevant orders. This requires the POS team to provide a dedicated PubSub topic (Confirmed by Prajney Sribhashyam on 2025-10-22).
*   **Project Scope:** Initial efforts to estimate effort and secure POS data files were conducted, but the specific request for an implementation plan was deferred until re-platforming.
*   **Business Impact:** The feature aims to eliminate manual payment status updates, thereby reducing Customer Service (CS) incidents, improving Perfect Order %, and preventing lost GMV ($11.96k observed in a reference period involving 146 unpaid orders).

**Pending Actions & Ownership**
*   **No immediate technical actions remain:** The ticket is closed for execution.
*   **Future Work:** This functionality will be addressed during the "re-platform" initiative (per 2026-01-15 update by Prajney Sribhashyam).

**Key Dates & Timeline**
*   **2025-04-30:** Ticket created by Fiona U.
*   **2025-06-24:** Danielle Lee noted potential 2-week effort but required POS example files for accurate estimation.
*   **2025-10-22:** Final technical plan documented (PubSub integration).
*   **2026-01-15:** Decision made to delete ticket and defer to re-platform.

**Blockers & Dependencies**
*   **Dependency:** Previous dependency on the POS team to provide a PubSub topic was identified but superseded by the decision to delay implementation.
*   **Data Gaps:** Initial delays were caused by missing example files from the POS team required for technical estimation (noted 2025-06-24).

**Linked References**
*   **Related Issue:** PA-330 (Polaris work item link).
*   **Key Personnel:** Fiona U, Rajesh Dobariya, Gopalakrishna Dhulipati, Danielle Lee, Qiuyan Tian, Ravi Goel, Prajney Sribhashyam.


## jira/OMNI-1334: Optimising Airway Bill Generation Experience for Seller
Source: jira | Key: OMNI-1334 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Prajney Sribhashyam | Last Updated: 2026-03-20T14:59:11.894061+00:00
**Daily Briefing Summary: OMNI-1334**

**Current Status:** **Deleted / Closed** (Previously "Backlog" -> Moved to Seller Experience Board).
The ticket is no longer active for the current roadmap. Prajney Sribhashyam confirmed on 2026-01-15 that this initiative will be covered in a future "re-platform" effort and explicitly instructed that the ticket can be deleted.

**Key Decisions & Actions:**
*   **Scope Correction (2025-07-21):** Koklin Gan queried if the work fell strictly within the Seller team's scope, suggesting it might not belong in the current board.
*   **Board Transfer (2025-07-22):** Prajney Sribhashyam confirmed ownership lies with the Seller team and moved OMNI-1334 to the "Seller Experience board," repurposing this specific ticket for a different initiative.
*   **Decommissioning (2026-01-15):** Prajney Sribhashyam decided to delete the ticket, as the requirements will be addressed during the upcoming system re-platform.

**Original Problem Definition (Context):**
The ticket originally proposed an "Idea" to allow FP Marketplace sellers to generate/print Airway Bills without triggering a carrier pickup (NJV) and to support multiple print generations. The goal was to prevent premature pickup triggers, reduce PPS errors at the MP seller's warehouse, and resolve current workflow struggles where generating bills inadvertently caused delivery issues.

**Key Dates:**
*   **2025-07-15:** Ticket created by Prajney Sribhashyam; Priority set to "High".
*   **2025-07-21:** Scope review discussion initiated by Koklin Gan.
*   **2025-07-22:** Ticket moved out of current board to Seller Experience Board.
*   **2026-01-15:** Final decision made to delete the ticket pending re-platform.

**Blockers & Dependencies:**
*   No technical blockers remain as the item is being retired.
*   The functionality is deprecated in favor of future re-platforming work.

**Ownership:**
*   **Original Assignee/Reporter:** Prajney Sribhashyam
*   **Reviewer:** Koklin Gan


## jira/OMNI-1389: [POC] Enabling PalmPay to allow quick checkout
Source: jira | Key: OMNI-1389 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Sathya Murthy Karthik | Reporter: Koklin Gan | Last Updated: 2026-03-20T14:59:18.610134+00:00
**Daily Briefing: OMNI-1389**

*   **Current Status:** The ticket is in the **Backlog** state (Category: **To Do**). It remains an active **Idea** with no resolution, fix versions, or assigned due date.
*   **Ownership & Pending Actions:** The task is assigned to **Sathya Murthy Karthik** for ownership of the "POC" (Proof of Concept) phase. No specific technical actions have been logged yet; the ticket awaits initiation of work from the assignee.
*   **Decisions Made:** No decisions or technical requirements were recorded in the chronological log. The entry serves as an initial proposal to enable PalmPay for quick checkout functionality.
*   **Key Dates & Blockers:**
    *   **Creation Date:** October 13, 2025 (16:38 UTC+08:00).
    *   **Deadlines:** None currently set (`duedate`: null).
    *   **Blockers:** None identified.
*   **Metadata Summary:**
    *   **Priority:** High
    *   **Reporter:** Koklin Gan
    *   **Labels/Components:** None assigned


## jira/OMNI-1390: Project Turbo to support new POS version
Source: jira | Key: OMNI-1390 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Sathya Murthy Karthik | Reporter: Koklin Gan | Last Updated: 2026-03-20T14:59:36.728250+00:00
**Daily Work Briefing: OMNI-1390**

*   **Current Status:** The ticket is currently in **Backlog (To Do)** status. However, the latest activity indicates it has been marked for archiving rather than active development.
*   **Pending Actions:** No immediate development or backlog actions are pending on this specific ticket due to the archiving decision. Ownership remains with **Sathya Murthy Karthik**, though the ticket is effectively closed for work.
*   **Decisions Made:** On **2026-01-29**, **Rajesh Dobariya** directed that the item be archived, citing that the requirement has already been captured elsewhere ("Archive this as its captured"). This supersedes the original "High" priority status assigned by reporter **Koklin Gan**.
*   **Key Dates & Deadlines:**
    *   **2025-10-13**: Ticket created/updated with initial details (Idea type, High Priority).
    *   **2026-01-29**: Archiving instruction issued.
    *   There are no assigned due dates or fix versions.

**Summary:**
The "Project Turbo to support new POS version" initiative (OMNI-1390) originated as a high-priority idea reported by **Koklin Gan**. While initially assigned to **Sathya Murthy Karthik**, the ticket was effectively paused and archived on **2026-01-29** by **Rajesh Dobariya**. The decision to archive confirms that the requirements have been documented in another location, rendering this specific backlog item redundant for active tracking.


## jira/OMNI-1353: Integrating Tencent's  Biometric Authentication (Palm Pay) solution with FPG App for member verification  
Source: jira | Key: OMNI-1353 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Aditi Rathi | Reporter: Gopal Singh | polaris-work-item-link: ENGM-2474 | Last Updated: 2026-03-20T15:00:49.870348+00:00
**Jira Ticket Briefing: OMNI-1353 (Tencent Palm Pay Integration)**

**Current Status**
The ticket is marked as **"Soft Prioritised" (To Do)** with **High** priority. However, the last activity indicates significant ambiguity regarding the project's viability and ownership. The work was initially scoped down to three stories in October 2025, but a critical review in February 2026 suggests potential stagnation.

**Key Decisions & Findings**
*   **Scope Reduction:** In Oct 2025, the scope was reduced to three specific stories (Koklin Gan).
*   **Technical Feasibility Assessment (Nov 4, 2025):** Ryne Cheow proposed that for a POC, no new engineering work may be required if:
    *   Linking/unlinking is handled via CDP.
    *   POS can write/retrieve Palm IDs per user record.
    *   Current payment APIs are reused.
*   **UX/Process Gaps Identified:** Sip Khoon Tan (Nov 4) and Sunny Lim (Nov 4) raised concerns that if the FPG app does not communicate account linkage, customers will be confused since the registration happens on a kiosk (Tencent device). Sunny Lim emphasized that users expect to see linkage status within the FPG app after scanning.
*   **Prototype:** Aadil Baggia delivered a working Figma prototype on Nov 20, 2025.
*   **Target Dates:** Initial rollout targeted for Oct 2025; Pilot in PDD Cheers store targeted for early Sep 2025 (Note: These dates appear to have been missed or the project delayed).

**Pending Actions & Ownership**
*   **Critical Decision Required:** Danielle Lee requested clarification on Feb 13, 2026: "Who is the new owner?" and whether work is still ongoing.
    *   **Owner:** Unassigned/Unclear (Current assignee remains Aditi Rathi).
    *   **Action:** Leadership must confirm if this initiative should continue or be closed.
*   **Technical Specification:** Sunny Lim requested API specifications on Nov 4, 2025, which have not been explicitly confirmed as delivered in the thread log.
*   **Effort Estimation:** While Sip Khoon Tan estimated "S size" complexity (conceptual level 2), no final engineering effort estimate was locked after Ryne Cheow's initial assessment that work might be zero for a POC.

**Blockers & Risks**
*   **Customer Experience Risk:** Significant risk identified regarding user confusion if account linkage is not visible within the FPG app (Sunny Lim).
*   **Adoption Risk:** Potential drop in Weekly Active Users (WAU) as customers may bypass the app entirely for palm payments, reducing engagement metrics.
*   **Timeline Missed:** Target rollout dates (Sep/Oct 2025) have passed without a clear status update, leading to the Feb 2026 inquiry about project closure.

**References**
*   Linked Item: ENGM-2474
*   Key Stakeholders: Aditi Rathi (Assignee), Gopal Singh (Reporter), Koklin Gan, Sip Khoon Tan, Ryne Cheow, Sunny Lim, Aadil Baggia, Danielle Lee, Sathya Murthy Karthik.


## jira/OMNI-1179: Compliance - Improving the Cart calculation logic 
Source: jira | Key: OMNI-1179 | Status: Paused (To Do) | Type: Idea | Priority: High | Assignee: Alvin Choo | Reporter: Alvin Choo | Labels: Foundation | polaris-work-item-link: CART-54 | Last Updated: 2026-03-20T15:21:34.934349+00:00
**Jira Ticket Briefing: OMNI-1179 (Compliance - Improving Cart Calculation Logic)**

**Current Status & State**
*   **Status:** Paused (Category: To Do).
*   **Priority:** High.
*   **Assignee/Reporter:** Alvin Choo.
*   **Type:** Idea | **Labels:** Foundation.
*   **Linked Issue:** CART-54 (Polaris work item).
*   **Context:** Proposed as a unified cart service to ensure pricing, promotion, and tax consistency across channels (Online, In-store, Scan & Go, Marketplace). Originally addressed customer frustration with calculation discrepancies and engineering struggles with fragmented logic.
*   **Scope Alignment:** Scope was reduced due to the upcoming app replatform to focus strictly on: 1) CRUD of core cart services, and 2) Cart calculation logic. Broader compliance/GST features were removed as redundant for the immediate future.

**Decisions Made**
1.  **Scope Reduction (Nov 27, 2025):** Finalized reduction to "CRUD of core cart services" and "Cart calculation," removing broader GST features in anticipation of the replatform. Moved to "Platform Health" category.
2.  **Validation Inquiry (Mar 19, 2026):** Sathya Murthy Karthik questioned if the reduced scope is necessary for the *current* application versus the future replatform.

**Pending Actions & Ownership**
*   **Urgent Decision Required:** Confirm whether to close or proceed with the ticket based on current app necessity.
    *   **Trigger:** Rajesh Dobariya (Mar 20, 2026) requested advice on closure.
    *   **Owner:** Alvin Choo / Sathya Murthy Karthik.
    *   **Deadline:** Immediate response required as of EOD March 20, 2026.

**Key Dates & Deadlines**
*   **Feb 24, 2025:** Initial Idea creation defining problem scope (pricing inconsistencies, fragmented architecture).
*   **Sept 26, 2025:** Scheduled GST meeting with CC and Finance regarding sales/drop-off calculations.
*   **Nov 27, 2025:** Scope reduction finalized; moved to Platform Health.
*   **Mar 19, 2026:** Inquiry raised regarding necessity for the current app vs. replatform.
*   **Mar 20, 2026 (Evening):** Rajesh Dobariya explicitly requested closure guidance from Alvin Choo.

**Blockers & Risks**
*   **Redundancy Risk:** The reduced scope (CRUD/Calculation) may be entirely superseded by the upcoming replatform, creating a risk of wasted effort if not validated immediately.
*   **Board Cleanup:** OMNI board visibility requires realistic timelines; this ticket blocks progress until a closure or re-scoping decision is made.

**Technical References**
*   **Linked Issue:** CART-54.
*   **Related Epics:** Shoppable grocery in Omni Home, GST project, Replatform (order splitting), Scan & Go splits, Marketplace scaling.
*   **Success Metrics (Original Proposal):** Improved cart-to-checkout price consistency, reduced checkout abandonment due to pricing errors, and decreased time to implement new pricing rules.


## jira/OMNI-1247: [OSMOS only] Integrate fit-for-purpose digital signage with OSMOS for in-store ad activation (merged into another ticket)
Source: jira | Key: OMNI-1247 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Yi Hao Tan | Reporter: Nikhil Grover | polaris-merge-work-item-link: OMNI-1400, OMNI-1400 | Last Updated: 2026-03-20T15:02:19.664289+00:00
**Daily Briefing Summary: OMNI-1247**

**Current Status**
The ticket is **Archived**. The content has been merged into a combined work item (OMNI-1400) as indicated by the title update and final comment. It was previously in "Backlog" status with "High" priority.

**Key Decisions Made**
*   **Integration Scope:** Projected to integrate fit-for-purpose digital signage with OSMOS specifically for in-store ad activation to solve fragmented CMS issues (currently 2 separate CMSs, some unconnected screens).
*   **Vendor Selection:** A Proof of Value exercise with **Advertima** is required; the final digital signage system will be selected post-exercise.
*   **Scope Consolidation:** The scope was determined to be better managed by merging this ticket into a combined work item (OMNI-1400), rendering OMNI-1247 redundant.

**Pending Actions & Ownership**
*   **Solution Design:** A workshop between FPG and OSMOS is scheduled for **27 Nov 2025** to define solution design and timelines. *Owner: TBD (Workshop participants)*.
*   **Proof of Value (PoV):** The PoV exercise with **Advertima** is expected to complete by the **end of Feb 2026**. Results are due in **March 2026**. *Owner: Team leading ROOH*.
*   **Next Steps Update:** A request was made on **19 Mar 2026** for an update on next steps.

**Key Dates & Deadlines**
*   **Solution Design Workshop:** 27 Nov 2025.
*   **PoV Completion:** End of Feb 2026.
*   **PoV Results:** March 2026.
*   **Ticket Archival/Porting:** Confirmed on 20 Mar 2026.

**Strategic Context & Metrics**
The initiative targets Retail Media GMV growth driven by in-store screens:
*   **2025 Goal:** $60K (300 screens).
*   **2026 Goal:** $1.4M (1,000 screens).
*   **2027 Goal:** $3M (1,000 screens).
Primary success metrics include Fill Rate, Cost Per Mille (CPM), and total ad slot volume.

**Assignee History**
Originally assigned to **Yi Hao Tan**, reassignment was noted on 19 Mar 2026 for the ROOH lead, before the ticket was ultimately archived by Yi Hao Tan following the merge into OMNI-1400.


## jira/OMNI-1391: Available to Promise 1.0 [MVP] - New Time-based Inventory logic
Source: jira | Key: OMNI-1391 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Sathya Murthy Karthik | Reporter: Prajney Sribhashyam | Last Updated: 2026-03-20T15:02:47.689694+00:00
**Jira Ticket Briefing: OMNI-1391**
**Topic:** Available to Promise (ATP) 1.0 [MVP] – New Time-based Inventory Logic
**Status:** Soft Prioritised (To Do) | **Priority:** High | **Type:** Idea
**Assignee:** Sathya Murthy Karthik | **Reporter:** Prajney Sribhashyam

**Current State & Context**
The FPG application currently utilizes a "Global Reservation Logic" that blocks all Stock on Hand (SOH) immediately upon order placement, regardless of the future delivery date. This causes false stock-outs, lost revenue, and high wastage (shrinkage) as near-expiry stock remains locked for future slots. The proposed MVP aims to implement time-based inventory logic specifically for **PFC** and **selected SKUs** to calculate availability based on 2-hour picking blocks over the next 7 days.

**Key Solution Components**
1.  **Replenishment Patterns:** Manual preset of SKU-level stock additions by timeslot (e.g., +200 qty arriving daily at 11 AM, ready for pick by 1 PM).
2.  **Picking Time Mapping:** Configurable mapping between delivery slots and inventory reference points (e.g., 8 AM delivery uses previous day 8 PM inventory).
3.  **New Logic Formula:** `SOH by timeslot for picking = Previous SOH + Preset Replenishment - Variance - Reservation`.
4.  **Indexer Workaround:** Applying "Unlimited SKU" logic to the Indexer for these SKUs to prevent search/PLP visibility issues due to outdated inventory counts.

**Pending Actions & Ownership**
*   **Effort Estimation:** Confirm if development effort is Small (S) or Extra Small (XS). *Action Owner:* Danielle Lee (Request dated 2025-11-04).
*   **Scope Alignment:** Finalize implementation scope and direction to prevent duplicated effort. *Action Owner:* Yi Hao Tan / HIVE & Middleware teams (Update cited 2026-03-19).

**Decisions & Status Updates**
*   As of **2026-03-19**, the implementation scope remains fluid. Active alignment is required with the HIVE and middleware teams before proceeding.
*   Scope is strictly limited to PFC and selected SKUs for this MVP stage.

**Key Dates, Constraints & Risks**
*   **Critical Limitation:** No system visibility exists for SKU expiry/write-off values or batch-level expiry data. This poses a risk of stock shortfall where customers can order items that are actually expired/unavailable in the warehouse.
*   **Business Impact Target:** Estimated $5.5M annual GMV improvement (conservative estimate excluding fresh penetration gains).
*   **Reference Documents:** BRD Document, Solution Discussion, Calculation Logic Google Sheet.

**Summary**
The initiative addresses significant inventory inefficiencies by shifting from static SOH checks to dynamic time-based availability. However, progress is currently paused pending technical alignment with the HIVE team to define the final scope and effort estimation. The solution relies heavily on manual operational inputs for replenishment patterns due to current system limitations regarding expiry data.


## jira/OMNI-1393: Enabling User Consent for customer data
Source: jira | Key: OMNI-1393 | Status: Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Zi Ying Liow | Reporter: Zi Ying Liow | Last Updated: 2026-03-20T15:03:22.292737+00:00
**Jira Briefing: OMNI-1393**

**Current Status**
The ticket **OMNI-1393** ("Enabling User Consent for customer data") has been resolved via closure. The work item was marked as **"Prioritised"** with a status of **"To Do"** and priority **"High"**. It was originally an Idea proposed by **Zi Ying Liow**.

**Decisions Made**
On **2025-11-04**, **Zi Ying Liow** merged this ticket into issue **OMNI-1394**. The directive was to remove OMNI-1393 from active tracking, consolidating the scope under the new ID.

**Pending Actions & Ownership**
With the merge decision finalized on **2025-11-04**, there are no further specific actions or ownership assignments remaining for ticket OMNI-1393. The initiative's execution is now governed by the merged ticket (OMNI-1394).

*Note: Prior to the merge, the following dependencies were identified:*
*   **Frontend Integration:** Requires integration with the Lifecycle Management System (**LMS**). Estimated effort: **XS**.
*   **Martech Team:** Required a **2-week** development window.

**Key Dates & Timeline**
*   **2025-10-23:** Ticket created and prioritized by **Zi Ying Liow**.
*   **2025-10-28:** Feasibility confirmed; Martech team timeline noted (2 weeks).
*   **2025-11-04:** Ticket merged into OMNI-1394 and closed.

**Business Context & Risks (Historical)**
The initiative aimed to implement an opt-in/out consent toggle within the preference center, sending data to **LMS** and storing it in **BigQuery (BQ)**.
*   **Revenue Impact:** Projected to safeguard **$500K** in existing revenue and unlock **$250K** incrementally.
*   **Use Cases Affected:** Offsite ads (non-FPG pages), self-served client ads using FPG 1st Party Data, dashboard monetization, and merging FPG/external Hashed 1st Party Data.
*   **Metrics Targets:** Expected AOV increase within 6 weeks and Perfect Order improvement within 3 months (specific baseline figures were placeholders).

**Summary**
Ticket OMNI-1393 is no longer active due to the merge into **OMNI-1394**. The original scope involved high-priority compliance and revenue enablement via user consent mechanisms, with initial technical dependencies identified for a 2-week Martech development cycle.


## jira/OMNI-1400: ROOH 2.0 - Sourcing and Implementation of best-in-class In-Store Ad booking, management, attribution platform
Source: jira | Key: OMNI-1400 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Yi Hao Tan | Reporter: Nikhil Grover | polaris-merge-work-item-link: OMNI-1247, OMNI-1247 | Last Updated: 2026-03-20T15:03:54.176010+00:00
**Daily Briefing Summary: OMNI-1400**

**Current Status & State**
*   **Ticket ID:** OMNI-1400 (ROOH 2.0)
*   **Issue Type:** Idea
*   **Priority:** High
*   **Status Category:** To Do (Soft Prioritised)
*   **Assignee:** Yi Hao Tan
*   **Reporter:** Nikhil Grover
*   **Linked Issue:** OMNI-1247 (Polaris merge work item link)

**Key Context & Problem Definition**
The initiative addresses the lack of performance benchmarks in current In-Store Retail Media (RMN) sales. Currently, campaigns are sold via 15-second ad slots without impression data, forcing BD teams to rely on manual email planning and physical proof-of-play photos. Operations rely on monday.com for booking management across two CMS platforms.
*   **Goal:** Transition from selling by "ad plays" to "impressions," establish baselines for footfall/impressions per screen/store, and enable demographic breakdowns (age, gender, segment) for advertisers.
*   **Financial Targets:** Projected Retail Media GMV growth from $60K (2025) to $3M (2027).

**Decisions Made**
*   **March 19, 2026:** Nikhil Grover reassigned ownership to the lead of ROOH.
*   **March 20, 2026:** Yi Hao Tan confirmed consolidating this work into a single ticket (OMNI-1400).

**Pending Actions & Ownership**
*   **Vendor Sourcing & Implementation:** Yi Hao Tan is responsible for sourcing and implementing a best-in-class platform for booking, management, and attribution.
*   **Requirement Refinement:** Detailed inputs on "Business Rules," "Operational Processes," "Business Plans," and specific "Product Metrics" (e.g., AOV increase targets) remain empty in the ticket description and require completion prior to vendor pitching.

**Dates & Deadlines**
*   **No Due Date:** The ticket currently has no assigned deadline.
*   **Historical Updates:** Last activity recorded on March 20, 2026.

**Blockers**
*   **Incomplete Documentation:** Critical sections for Business Plans, Operational Processes, and specific Product Metrics (AOV/Perfect Order targets) are not yet defined.
*   **Vendor Selection:** The "best-in-class" platform has not yet been selected or implemented; the ticket is still in the "Idea" phase.


## jira/OMNI-1405: [OSMOS Only] Streamline seller/brand onboarding on OSMOS
Source: jira | Key: OMNI-1405 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | Last Updated: 2026-03-20T15:04:19.359510+00:00
**Daily Briefing Summary: OMNI-1405**

**Current Status & State**
*   **Ticket:** OMNI-1405 [OSMOS Only] Streamline seller/brand onboarding on OSMOS.
*   **Status:** Backlog (Category: To Do).
*   **Type:** Idea | **Priority:** High.
*   **Assignee/Reporter:** Nikhil Grover.
*   **Context:** The current SKU tagging and advertiser account setup process takes 3 days, causing campaign launch delays for Ad Ops, Advertisers, RMN BD teams, and Category Managers.

**Key Problem & Proposed Solution**
*   **Problem:** Manual onboarding requires uploading advertiser CSVs to OSMOS, manually sharing vendor code-brand ID mappings (SLA: 3 days), marking SKUs as "advertisable" in DBP BackOffice, and manually adding vendor codes via BQ. Missing SKUs delay campaign starts and hurt advertiser experience.
*   **Proposed Solution:** Automate three specific DBP processes to sync with OSMOS:
    1.  SKU information updates.
    2.  Vendor code tagging to SKUs.
    3.  "Advertisable" flag setting based on internal guidelines.

**Pending Actions & Ownership**
*   **Primary Owner:** Nikhil Grover is assigned to advance this idea from the Backlog.
*   **Pending Work:** The ticket lacks defined metrics and operational plans. Specific actions required include:
    *   Defining exact financial impact (AOV increase targets).
    *   Setting Customer Experience metrics (Perfect Order % targets).
    *   Outlining Operational Processes, dependencies, and budget approvals.
    *   Finalizing Business Plans and Go-to-Market strategies.
    *   Documenting specific Business Rules/Logic exceptions.

**Decisions Made**
*   No formal decisions or approvals have been recorded yet; the ticket remains in the initial "Idea" proposal phase. The problem statement has been defined, but the solution details are currently high-level and require further specification to move out of Backlog.

**Key Dates & Blockers**
*   **Dates:** Ticket logged on 2025-11-06. No due date is set.
*   **Blockers:** The lack of quantified metrics (AOV, Perfect Order), undefined operational workflows, and missing business rules are preventing the transition from "Backlog" to active development or design phases.

**Technical Context**
*   **Systems Involved:** OSMOS, DBP BackOffice, SAP, BQ (BigQuery).
*   **Current Workflow:** CSV upload -> Vendor mapping (3-day SLA) -> SKU marking in DBP -> BQ data pull -> Hourly catalog sync.


## jira/OMNI-1428: [1hd] Phase 2 -  Scaling one hour delivery to more stores (TO REMOVE)
Source: jira | Key: OMNI-1428 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Rajesh Dobariya | polaris-work-item-link: DPD-627 | Last Updated: 2026-03-20T15:04:37.778860+00:00
**Daily Briefing Summary: OMNI-1428**

**Current Status**
The ticket **OMNI-1428** [1hd] Phase 2 - Scaling one hour delivery to more stores (TO REMOVE) is currently in the **Backlog** status. However, per the latest update on **2026-03-19**, this item has been marked for **archival**. It was merged with ticket **OMNI-1425**.

**Decisions Made**
*   **Archival & Consolidation**: On **2026-03-19**, the reporter/assignee determined that the scope of OMNI-1428 is being consolidated into work item **DPD-627** (linked via Polaris) and specifically merged with ticket **OMNI-1425**. No further independent action on OMNI-1428 is required.

**Pending Actions & Ownership**
*   **No Direct Actions**: Since the ticket is archived, there are no pending tasks assigned to this specific ID.
*   **Follow-up**: The owner of the merged initiative must be referenced in relation to **OMNI-1425**. Currently, **Rajesh Dobariya** remains listed as the Assignee and Reporter for OMNI-1428 until the merge is fully reflected in system workflows.

**Key Dates & Deadlines**
*   **Last Update**: 2026-03-19 (Archival decision).
*   **Original Proposal Date**: 2026-02-27.
*   **Deadlines**: None specified; the ticket has no due date.

**Technical References & Context**
*   **Ticket ID**: OMNI-1428 (Idea, High Priority).
*   **Linked Issue**: DPD-627 (Polaris work item link).
*   **Original Scope**: The initial description outlined a detailed template for defining an opportunity to allow shoppers to amend orders post-completion. It requested specific inputs on problem definition ("As a shopper..."), affected user segments, estimated volume, current workarounds, business impact (GMV/AOV), product metrics, operational dependencies, and go-to-market strategies.
*   **Resolution**: The content was deemed redundant or superseded by the merged ticket OMNI-1425.

**Summary**
The initiative to scale one-hour delivery to more stores via an order amendment feature (OMNI-1428) has been closed out and consolidated into **OMNI-1425**. The detailed requirement template provided in the original description is now subsumed under the merged ticket's scope. No immediate action is required on this specific record.


## jira/OMNI-1431: Blocking of specific postal code from allowing customer to select for delivery address
Source: jira | Key: OMNI-1431 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Koklin Gan | Reporter: Koklin Gan | Last Updated: 2026-03-20T15:04:53.480603+00:00
**Briefing Summary: OMNI-1431**

*   **Current Status:** The ticket is in the **Backlog (To Do)** state. It is classified as an **Idea** with **High** priority. No resolution, due date, or fix versions have been assigned yet.
*   **Ownership & Assignment:** Both the reporter and assignee are **Koklin Gan**. Recent activity on **2026-03-20T14:54:21.064+0800** shows **Sathya Murthy Karthik** confirmed adding this item to a list as requested.
*   **Pending Actions:** No immediate development actions are logged. The ticket currently contains a template description requiring the author (**Koklin Gan**) to complete specific sections before advancement: Opportunity/Problem definition, Solution Summary (user stories), Business Impact (GMV/Cost savings), Product Metrics Impact, Operational Processes, Business Plans, and detailed Business Rules/Logic.
*   **Decisions Made:** The primary decision recorded is the inclusion of this feature request into a prioritization or tracking list by **Sathya Murthy Karthik** on March 20, 2026.
*   **Key Dates & Blockers:**
    *   **Last Activity:** March 19, 2026 (Initial creation and status update).
    *   **Next Activity:** None scheduled; the ticket is blocked by the lack of completed solution details in the template fields.
*   **Technical Scope & Logic:**
    *   **Feature:** Block specific high-risk or restricted postal codes from customer selection during checkout or address entry to prevent fraud and operational costs.
    *   **Required Logic:**
        1.  Prevent checkouts for newly inputted postal codes on the module.
        2.  Prevent checkouts if a saved address matches a restricted postal code.
        3.  Ensure customers are blocked immediately at the checkout page if their existing postal code is on the restricted list.
    *   **Admin Capability:** Administrators must be able to add or remove codes from the restricted list via backoffice settings.
    *   **Compliance Context:** Aligns with a "Risk-Based Approach" for money laundering prevention regarding fraudulent clusters and sanctioned entities.


## jira/OMNI-1432: Adhere to alcohol act compliance 
Source: jira | Key: OMNI-1432 | Status: Backlog (To Do) | Type: Idea | Priority: High | Assignee: Koklin Gan | Reporter: Koklin Gan | Last Updated: 2026-03-20T15:05:10.155938+00:00
**Daily Briefing Summary: OMNI-1432**

**Current Status & State**
*   **Ticket ID:** OMNI-1432
*   **Title:** Adhere to alcohol act compliance
*   **Type/Status:** Idea / Backlog (To Do)
*   **Priority:** High
*   **Assignee & Reporter:** Koklin Gan
*   **Last Activity:** 2026-03-20T14:54:25.811+0800

**Pending Actions & Ownership**
*   **Content Completion (Owner: Koklin Gan):** The ticket description currently contains placeholder template fields that are unfilled. Koklin Gan must complete the following sections to advance the idea:
    *   Opportunity/Problem definition details.
    *   Business Impact (Financial metrics, GMV/AOV projections).
    *   Product Metrics Impact (Perfect Order targets with timelines).
    *   Operational Processes (Dependencies, vendor alignments).
    *   Business Plans (Go-to-market strategies).
*   **System Logic Definition:** The core requirement is defined but not yet operationalized:
    *   *Trigger:* Detection of alcohol-related SKUs in an order.
    *   *Action:* Automatically disable and hide the "Leave at Door" option during checkout/delivery preference stages.
    *   *Integration:* Delivery instructions must be transmitted to TMS (Transportation Management System).

**Decisions Made**
*   **Compliance Gap Identified:** A review of compliance guidelines flagged a specific gap regarding Liquor SKU handling that requires immediate feature development.
*   **Feature Scope Confirmed:** The requirement is strictly to mandate face-to-face interaction for alcohol deliveries, ensuring drivers never leave controlled substances unattended.

**Key Dates, Deadlines & Blockers**
*   **Creation Date:** 2026-03-19 (Initial ticket creation by Koklin Gan).
*   **Status Update Date:** 2026-03-20 (Sathya Murthy Karthik added the item to the list as requested).
*   **Deadlines:** None currently assigned (`duedate: null`).
*   **Blockers:** The ticket remains in "Backlog" status pending the completion of the detailed description fields by the assignee. No technical implementation has begun.

**Technical References**
*   **System Dependency:** TMS (for delivery instruction handoff).
*   **UI Logic:** Checkout and Delivery Preference stages logic modification.
