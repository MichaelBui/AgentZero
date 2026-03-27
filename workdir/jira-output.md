

## [1/58] [BCRS Compliance] Phase 2: Order Place & Returns/Refunds Process
Source: jira | Key: OMNI-1294 | Status: Technical Live (Done) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Winson Lim | Labels: bcrs | discovery---connected: NEDMT-2334 | polaris-work-item-link: DPD-225, DPD-225 | Last Updated: 2026-03-27T01:31:06.407280+00:00
**Ticket:** OMNI-1294 | **[BCRS Compliance] Phase 2: Order Place & Returns/Refunds Process**
**Status:** Technical Live (Done) | **Risk Level:** High | **Assignee:** Prajney Sribhashyam
**Reporter:** Winson Lim | **Priority:** High | **Type:** Idea

### Current Status
*   **Regulatory Context:** Singapore NEA mandates a $0.10 deposit on regulated beverages (150ml–3L). Compliance deadline: Labeling by April 1, 2026; Enforcement by July 1, 2026.
*   **Phase Progress:** Technical implementation is live. Focus has shifted from general UAT to validating specific logic for Returns, Pre-orders (Staff App/Cart Flow), MP SKU creation, Scan & Go, and Finance flows.
*   **Scope:** Digital and Food Services teams are onboarding in Phase 2. Effort spans 43 weeks across Procurement, SAP, Finance (CF), POS, and CPI teams.

### Scope & Functional Requirements
*   **Catalogue & Search:** BCRS SKUs must link to Deposit SKUs. Updates required for Algolia, Dynamic Yield, and DS Purchase History indices (P1/P0). New SKUs replace old ones in search feeds.
*   **MP Integration:** Creation of BCRS SKUs in Mirakl; sync to DBP (P0).
*   **Cart/Checkout/Scan & Go:** Deposit added as a separate charge on cart and checkout screens. Excluded from offer limits and Link points. SKU-level breakdown visibility remains under design discussion.
*   **Returns & Refunds:** Deposit amount must refund when the master BCRS SKU is returned (including if dropped during picking/packing). Logic requires business definition for non-return scenarios and partial multipack refunds (e.g., 1 of 6).
*   **Picker/TMS Apps:** Deposit SKUs excluded from picker view. Partial pick logic ($0.80 vs $1.00) requires immediate business confirmation.
*   **SAP Integration:** Orders posted only in "delivered" state with deposit as a distinct line item. Order State Management remains in OMS (no decoupling).

### Pending Actions & Ownership
1.  **Design Clarifications:** Finalize invoice design, SKU-level breakdown visibility (subtotal vs. separate charge), and "Deposit SKU return" policy for non-returned master SKUs. *Owner: Business/Finance/Digital.*
2.  **Partial Pick Logic:** Confirm calculation logic for partial picks in Picker/TMS apps. *Owner: Digital/Food Services.*
3.  **SAP Validation:** Validate refund/return flow mapping and ensure distinct deposit line items. *Owner: Finance/Prajney Sribhashyam.*

### Key Decisions & Assumptions
*   **Deposit Treatment:** Non-GST, treated as a separate charge; excluded from offer limits and Link points.
*   **SAP Strategy:** Orders passed to SAP only in "delivered" state with deposit as a separate line item. Order State Management remains in OMS.
*   **QC Food:** BCRS deposit inclusion logic for QC food services is currently excluded from scope regarding specific food processing rules.
*   **Success Criteria:** Targeting 100% accuracy in pricing, receipt breakdown, and POS integration by March 2026 to meet NEA labeling deadlines.

### Blockers & Risks
*   **Complexity:** Returns logic for multipacks and partial pick charges requires immediate business definition.
*   **Scope Exclusion:** SAP decoupling excluded; Order State Management stays in OMS.
*   **Impact:** Affects ~130 stores and 100% of shoppers purchasing regulated beverages post-April 2026.

### Linked Issues
*   **Polaris Work Item:** DPD-225
*   **Discovery - Connected:** NEDMT-2334


## [2/58] [Decoupling from SAP] Improve order orchestration with integration to WMS Middleware
Source: jira | Key: OMNI-1362 | Status: Paused (To Do) | Type: Idea | Priority: High | Assignee: Gopalakrishna Dhulipati | Reporter: Gopalakrishna Dhulipati | blocks: OMNI-1249, OMNI-1249 | polaris-work-item-link: DPD-184 | relates: OE-3209 | Last Updated: 2026-03-27T01:31:23.599726+00:00
**Ticket:** OMNI-1362: [Decoupling from SAP] Improve order orchestration with integration to WMS Middleware
**Current Status:** Paused (To Do) | **Type:** Idea | **Assignee:** Gopalakrishna Dhulipati | **Priority:** High

### 1. Strategic Context & Problem Definition
Decoupling SAP is a strategic initiative aimed at achieving financial compliance (specifically GST non-compliance for the Finance team) and optimizing fulfillment architecture. The primary prerequisite is integrating DBP with WMS Middleware. Currently, customer fulfillment experience relies heavily on SAP flows; this integration aims to resolve those dependencies.

### 2. Implementation & Validation Scope
*   **Integration Plan:** DBP will integrate with WMS Middleware, followed by the integration between WMS Middleware and TMS.
*   **UAT Scope:** Validation covers DBP-WMS Middleware flows and DBP-TMS flows.
*   **Validation Status:** Sufficient validation is required before roadmap prioritization. Previous historical context notes SIT completion (Dec 29–30, 2025) and UAT passing with WM6/SAP teams. However, the current status reflects a "Paused" state pending further validation of requirements against the new strategic definition.

### 3. Pending Actions & Ownership
*   **Requirement Clarification:** The team must determine if specific requirements (carton items, order types, Boys Brigade Donation posting) belong in the B2C current system or are deferred to "Project Light." Action owner: Gopalakrishna Dhulipati (checking with Fenny).
*   **Timeline Finalization:** Await confirmation on project dates from Sathya Murthy Karthik. A re-group meeting was historically scheduled for Jan 8, 2026; the current status remains "Paused" pending final timeline alignment.

### 4. Key Decisions Made
*   **Strategic Alignment:** The initiative is now formally categorized as an Idea with High Priority to address GST compliance and fulfillment architecture.
*   **Rollout Scope:** Production rollout includes DBP-WMS Middleware and WMS-TMS integration.
*   **Status Shift:** The project has shifted from a "Delayed/Red" status to "Paused (To Do)" following the definition of new success criteria and scope.
    *   *Note:* Previous tentative dates (March/April 2026) are superseded by the current paused state until validation is complete.

### 5. Linked Issues & Context
*   **Blocks:** OMNI-1249
*   **Relates:** OE-3209
*   **Polaris Link:** DPD-184
*   **Risk Level:** High risk due to GST compliance requirements and the critical nature of SAP decoupling for financial operations.

### 6. Success Criteria
To prioritize this idea on the roadmap, specific metrics must be defined regarding:
*   Dimensions and metrics affected upon resolution.
*   Current baseline vs. expected outcome within a specified timeframe.
*(Note: Specific metric values were not provided in the new input; definition remains pending final validation).*


## [3/58] Sales posting for BCRS deposit amount
Source: jira | Key: DPD-383 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Prajney Sribhashyam | Due: 2026-02-18 | Resolution: Done | blocks: DPD-551, DPD-551 | child: DPD-590 | parent: DPD-225, DPD-590 | Last Updated: 2026-03-27T01:31:46.611260+00:00
**Ticket:** DPD-383 (Sales posting for BCRS deposit amount)
**Status:** Done | **Priority:** High
**Assignee:** Michael Bui | **Reporter:** Prajney Sribhashyam

**Current State & Key Decisions**
*   **Production Deployment Complete:** Deployed to PRD on 2026-03-26. Initial observations show no issues; however, actual SAP validation is pending the arrival of real BCRS orders in production.
*   **Development Scope:** DBP calculates deposits per order line (`deposit price × fulfilled quantity`) and aggregates them at the order level for SAP posting. This applies to E-Comm, Marketplace, Returns/Refunds, Donations, and FOC items.
*   **Eligibility Logic:** The system processes only **COMPLETED** orders. OFFLINE, RB PreOrder, and non-COMPLETED orders are acknowledged but ignored.
*   **Special Scenarios:**
    *   **Donation Orders:** Deposits calculated and posted using standard logic for BCRS-eligible items.
    *   **FOC Items:** Deposits calculated and posted if the master SKU is BCRS-eligible (identified via `freeItems` field).
*   **Duplicate Prevention:** A "delivery once" policy was enabled on GCP PubSub (2026-03-06) to prevent duplicate postings. SAP captures only the first valid posting.
*   **Technical Fixes:** CSRF token/cookie handling for SAP resolved 403 errors; failure detection logic distinguishes HTTP 201 success from internal business errors.

**Pending Actions & Ownership**
*   **Post-Deployment Monitoring:** Michael Bui is monitoring PRD for actual incoming BCRS orders to validate end-to-end SAP posting in a live environment.
*   **SAP Access:** Production SAP access for testing with live data is pending confirmation once real orders are observed.

**Key Dates & Timeline**
*   **2026-01-30:** Ticket created (High Priority). Requirements defined for E-Comm, Marketplace, Returns/Refunds, Donations, and FOC items. Title set to "Sales posting for BCRS deposit amount".
*   **2026-02-18:** Original due date passed; ticket resolved as Done. Resolution status updated to "Done" with category "IN RELASE QUEUE".
*   **2026-02-20:** `sapMaterialNumber` exposed via API (Resolves block DPD-551).
*   **2026-03-04:** Undocumented `freeItems` field identified for FOC logic.
*   **2026-03-06:** "Delivery once" policy enabled to prevent duplicates; verified against logs.
*   **2026-03-26:** Deployed to PRD by Michael Bui; observed and verified with no issues.

**Technical References & Data Points**
*   **Parent Ticket:** DPD-225 ([BCRS] Inform customers on BCRS deposit during Order Placement & Returns/Refunds Process)
*   **Subtask:** DPD-590 (Clean up archived proposals after PRD release)
*   **Blocking Issue (Resolved):** DPD-551 (PLU Processor)
*   **SAP Configuration Verified:** CompCode `FP10`, DocType `DR`, GL Account `4423` (Deposit), Customer `199997`.
*   **Reference Docs:** BRD DBP BCRS Requirement for Plan B, Sample deposit API, Order-v3 API.
*   **GCP PubSub Config:** Delivery once policy applied to avoid duplicate SAP postings.

**Blockers/Notes**
*   All technical blockers (SAP access in dev/test, material number availability) are cleared.
*   The only remaining dependency is the validation of real-world BCRS orders in Production post-deployment.


## [4/58] Charge BCRS deposit for re-delivery
Source: jira | Key: DPD-807 | Status: TO BE DEFINED (To Do) | Type: Story | Priority: High | Reporter: Prajney Sribhashyam | parent: DPD-225 | Last Updated: 2026-03-26T21:31:10.741743+00:00
**Daily Briefing Summary: DPD-807 – Charge BCRS Deposit for Re-delivery**

**Current Status & State**
*   **Ticket ID:** DPD-807 (Story)
*   **Status:** TO BE DEFINED (Category: To Do)
*   **Priority:** High
*   **Parent Ticket:** DPD-225 ([BCRS] Inform customers on BCRS deposit during Order Placement & Returns/Refunds Process)
*   **Reporter:** Prajney Sribhashyam
*   **Assignee:** None assigned as of 2026-03-24.

**Decisions Made & Scope Definition**
*   **Core Functionality (2026-03-24):** Defined feature to allow Operations Managers to apply BCRS deposits to eligible items (e.g., plastic bottles, aluminum cans) during re-delivery while excluding non-eligible items (cardboard, produce). Fees are calculated per unit (e.g., €0.10) and displayed as a separate line item.
*   **Duplicate Suppression Logic (2026-03-24):** The system must verify prior payment status before charging again. If a deposit was refunded or cancelled in the previous failed attempt, a new charge applies; otherwise, it is suppressed.
*   **Technical Implementation Strategy (2026-03-26):** A decision was made to utilize a `curl` PUT call to update the Order Service metadata flag `Deposit posted to SAP`. The "Deposit sales posting" service will:
    1.  Update this field to `true` upon completion of the first-time deposit sales posting.
    2.  Consume this field to suppress duplicate postings during subsequent re-delivery attempts.

**Pending Actions & Ownership**
*   **Metadata Management:** Develop logic in "Deposit sales posting" to set `metadata.Deposit posted to SAP` to `true` only after the initial successful post.
    *   *Owner:* Unassigned (Reported by Prajney Sribhashyam).
*   **RPA Integration:** Configure RPA to charge the customer's original payment method and post BCRS deposit sales, consuming the metadata flag to prevent double-charging.
    *   *Owner:* Unassigned.
*   **Order Service Logic:** Implement filtering for BCRS-eligible items in re-delivery orders and logic to exclude non-eligible items from calculations.
    *   *Owner:* Unassigned.

**Technical References & Evidence**
*   **API Endpoint for Metadata Update:**
    `PUT https://api.zs-uat.fairprice.com.sg/order-service/v3/deliveryOrders/{deliveryOrderId}`
*   **Payload Structure (2026-03-26):**
    ```json
    {
      "metadata": {
        "Deposit posted to SAP": true
      },
      "updateAction": ["UPDATE_ACTION_UPDATE_METADATA"]
    }
    ```
*   **Test Case Reference:** Delivery Order ID `75588070` (URL: `https://admin-uat.fairprice.com.sg/customer-support/delivery-orders/75588070`).
*   **Execution Command:** Confirmed via Wai Ching Chan on 2026-03-26 using the specific curl command provided for testing.

**Key Dates & Deadlines**
*   **Last Activity:** 2026-03-26T16:49:44+0800 (Technical specification and command verification).
*   **Due Date:** Not defined.
*   **Blockers:** No assignee is currently linked to the ticket; development cannot commence until ownership is assigned.


## [5/58] Dynamic ad slot configuration for Homepage swimlanes
Source: jira | Key: DPD-715 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-17 | Resolution: Done | parent: DPD-710 | Last Updated: 2026-03-26T01:30:50.334691+00:00
### Daily Briefing Summary: DPD-715 (Dynamic Ad Slot Configuration)

**Current Status:** **IN RELEASE QUEUE** (Resolution: Done). The story is technically complete, UAT signed off, and deployed to production.

**Key Decisions & Actions Taken:**
*   **Feature Flag Implementation:** Split configuration logic successfully implemented to dynamically control ad slot indices without code changes. Supports dynamic density updates (e.g., changing from `[3, 5, 7]` to `[2, 4, 6, 8, 10]`) and handles empty arrays for organic-only views.
*   **Environment Updates:**
    *   **OG Home & Mobile Apps:** Verified SplitIO changes reflect correctly; mobile-specific issues resolved.
    *   **Omni Home:** Slot positions updated to configured values (e.g., `3, 5, 7`) following production deployment. The previous discrepancy regarding fixed positions at `(1, 3)` has been resolved.
*   **Production Deployment:** On **2026-03-26**, Michael Bui confirmed successful deployment to PRD with the specific slot configuration: `3, 5, 7, 11, 13, 15` as requested by Nikhil Grover on **2026-03-25**.

**Pending Actions & Ownership:**
*   **No Pending Actions:** The ticket is effectively closed pending standard monitoring. UAT was signed off on **2026-03-25**.
*   **Monitoring:** Verify post-deployment stability of the new slot configuration (`3, 5, 7, 11, 13, 15`) across Omni and OG Homepages.

**Key Dates & Constraints:**
*   **Due Date:** 2026-03-17 (Deployment occurred post-due date on 2026-03-26).
*   **Critical Constraint:** System continues to honor existing stock availability checks; no out-of-stock products are rendered as ads.
*   **Parent Ticket:** DPD-710 ([RMN] Activate product ads in Omni Home swimlanes).

**Technical Context:**
*   **Logic:** API requests adapt dynamically to Split configuration counts (e.g., 6 slots = request 6 ads).
*   **Resilience:** The system gracefully handles Ad Supply Shortages (filling available slots with organic content) and Out-of-Bounds scenarios (ignoring indices exceeding swimlane length, e.g., index 20 in a 10-item list).

**Blockers/Notes:**
*   **Resolution of Discrepancy:** The previously noted issue where Omni Home swimlanes were stuck at fixed positions has been resolved following the production deployment on 2026-03-26. Stakeholders confirmed slot positions now match the SplitIO flag values.

**Timeline Update:**
*   **2026-03-19:** UAT session conducted by Michael Bui.
*   **2026-03-25:** Nikhil Grover signed off on UAT and requested specific production config: `3, 5, 7, 11, 13, 15`.
*   **2026-03-26:** Michael Bui deployed to Production; confirmed functionality.
*   **2026-03-10:** Ticket created with initial acceptance criteria defining dynamic API requests, fallback defaults (`[1,3]`), and empty array handling.


## [6/58] [BCRS] Inform customers on BCRS deposit during Order Placement & Returns/Refunds Process
Source: jira | Key: DPD-225 | Status: IN DEVELOPMENT (In Progress) | Type: Epic | Priority: High | Reporter: Andin Eswarlal Rajesh | Due: 2026-02-23 | discovery---connected: NEDMT-2334 | parent: DPD-807, DPD-383 | polaris-work-item-link: OMNI-1294, OMNI-1294 | relates: DPD-26 | Last Updated: 2026-03-25T13:31:29.242246+00:00
**Daily Briefing: DPD-225 [BCRS] Inform customers on BCRS deposit during Order Placement & Returns/Refunds Process**

*   **Current Status:** IN DEVELOPMENT (High Priority Epic). Due date is February 23, 2026.
    *   *Note:* While the ticket title references customer notifications for deposits, the core description outlines a broader strategic initiative to integrate BCRS flags into Mirakl and SAP systems, including UI updates, automated synchronization, and sales reporting modifications.

*   **Pending Actions & Ownership:**
    *   **QE/E2E Testing:** Queuing stories from the referenced slide for End-to-End testing. Owner: QA Team (implied by "QE needs... to be picked up"). Action required: Review slide content against ticket requirements and add missing components.
    *   **Deployment Planning:** Finalizing deployment strategy and production smoke test plan. Owner: Prajney Sribhashyam.
    *   **Documentation:** Ensuring all technical documents for Order Experience, Cart/Checkout, Product Catalogue, UAT Products, and Feature Flags are complete (currently listed as empty in the description).

*   **Key Decisions & Milestones:**
    *   **Backend Approval:** Backend deployment sign-off has been granted. Documented on March 25, 2026, by Prajney Sribhashyam.
    *   **Scope Definition:** The project objective is confirmed to cover regulatory compliance for Singapore's BCRS ($0.10 refundable deposit), ensuring data integrity between Mirakl and SAP for revenue tracking.

*   **Key Dates & Blockers:**
    *   **Target Launch:** Official scheme launch date referenced as a deadline context (specific date not explicitly set in text, but ticket due is 2026-02-23).
    *   **Last Update:** March 25, 2026 (Backend sign-off).
    *   **Blockers/Dependencies:** Missing detailed documentation for UI elements ("Design -" is blank) and specific product lists for UAT. The ticket was previously split from a main ticket; ensure all sub-components regarding "Order Placement & Returns/Refunds Process" are explicitly covered in the current development stories.

*   **Linked Issues:**
    *   **Polaris Work Item:** OMNI-1294
    *   **Related:** DPD-26
    *   **Connected Discovery:** NEDMT-2334

*   **Reporter/Assignee:** Reported by Andin Eswarlal Rajesh. No assignee currently listed.


## [7/58] [OSMOS only] Enable offsite ads integration with Meta on OSMOS
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


## [8/58] Dynamic ad slots for vertical scroll on omni homepage
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


## [9/58] Include swimlane name in the ad request for all Omni Home swimlanes
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


## [10/58] [RMN] Streamline event sync from Segment.io to OSMOS to resolve overage
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


## [11/58] Improve event sync to prevent overage
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


## [12/58] FP VIPs encounter verification after S&G purchase for fewer reasons, vs other customers
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


## [13/58] Fix RMN pentest Low and optionally Info issues
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


## [14/58] Capture SAP Material Number into catalogue service for SAP-related downstream usage
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


## [15/58] Setup alerts for Advertima platform
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


## [16/58] Fix RMN pentest medium issues
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


## [17/58] Take over Segment destination functions from OSMOS
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


## [18/58] Clean up archived proposals after PRD release
Source: jira | Key: DPD-590 | Status: TO BE DEFINED (To Do) | Type: Subtask | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Due: 2026-04-24 | child: DPD-383 | parent: DPD-383 | Last Updated: 2026-03-20T14:48:32.369189+00:00
**Daily Briefing Summary: DPD-590**

*   **Current Status:** The task is marked as **TO BE DEFINED (To Do)**. No work has commenced.
*   **Ownership & Pending Actions:** **Michael Bui** (Assignee/Reporter) owns the execution of this subtask. Pending actions include identifying and removing archived proposals from the repository to prevent future AI hallucinations.
*   **Decisions Made:** None recorded in the ticket history yet; the scope remains defined by the task title and description intent.
*   **Key Dates & Deadlines:** The due date is set for **2026-04-24**.
*   **Blockers/Context:** This subtask (**DPD-590**) supports the parent initiative **DPD-383** ("Sales posting for BCRS deposit amount"). It carries a **High** priority.


## [19/58] New project setup for BCRS deposit posting job "ntuclink_bcrs-deposit-posting"
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


## [20/58] [RMN] Unblock NTP connection for Advertima devices
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


## [21/58] New SKU Sync Optimisation
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


## [22/58] [CDP] Access Request from Retail Media
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


## [23/58] "Ad" product copy display not consistent at times
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


## [24/58] Automate sync of newly onboarded SKUs into OSMOS for faster activation
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


## [25/58] Mutation Testing Implementation - rmn-osmos-purchase-event-tracking
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


## [26/58] Mutation Testing Implementation - rmn-osmos-product-feeder
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


## [27/58] B2B Solution: Integration work
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


## [28/58] [Decoupling from SAP] Migrate CF apps to DBP to improve MP Consol fulfilment experience
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


## [29/58] Improve seller catalogue compliance to align with FSQ expectations
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


## [30/58] [MP Foundational] Sales Breakdown & Seller Payouts
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


## [31/58] Enhanced Notification Preference Center for Multi-Channel Communication Management
Source: jira | Key: OMNI-1296 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Sip Khoon Tan | Reporter: Sip Khoon Tan | discovery---connected: CORE-304 | polaris-work-item-link: CORE-304 | Last Updated: 2026-03-26T21:31:55.209499+00:00
**Jira Ticket Summary: OMNI-1296 (Enhanced Notification Preference Center)**

**Current Status & State**
*   **Status:** In Development (In Progress).
*   **Type:** Idea.
*   **Priority:** High.
*   **Assignee/Owner:** Sip Khoon Tan (Reporter and Assignee).
*   **Linked Issues:** CORE-304 (Discovery - Connected; Polaris work item link).
*   **Last Update:** 26 Mar 2026, Zi Ying Liow confirmed updates.

**Scope & Solution Design**
A centralized interface enabling granular control over:
*   **EDM Subscriptions:** By business swimlane (Grocery, FP Super, FP Finest, FP Hyper, FP Online, Unity, Cheers, Kopitiam, FP Partners, FP B2B, Link Rewards). Includes an "Unsub all" logic.
*   **Frequency Management:** Daily, weekly, or monthly preferences.
*   **Push Notification Service (PNS):** Separate settings for transactional vs. marketing communications (e.g., app features, announcements).
*   **WhatsApp:** Dedicated communication settings management.

**Problem Definition & Business Impact**
The current binary unsubscribe mechanism causes total communication loss when a single channel is opted out, conflicting with the growing demand from business units for multi-channel engagement.
*   **EDM Goal:** Reduce complete unsub rate by 30% (from 72k to 50k annually). Prevents $57.6k GMV loss ($192k total opportunity lost based on $2.74 AOV per subscriber/year).
*   **PNS Goal:** Reduce device unsub rate by 30%. Prevents $474k GMV loss (Total PNS opportunity: $1.58M).
*   **Preference Center Specific:** Target to reduce complete unsub rate by 50% (from 50k to 25k annual center unsubscribes).
*   **Total Prevented Annual GMV Loss:** $531.6k (EDM + PNS).
*   **Operational Benefits:** Enhanced segmentation for Marketing Operations, improved preference data for Data Analytics, and reduced campaign waste through precise targeting.

**Pending Actions & Ownership**
*   **Timeline Alignment:** As of 26 Mar 2026, Sathya Murthy Karthik requested immediate date updates; Zi Ying Liow confirmed these changes. All previous hard deadlines (Feb 20, March 2, and March 12–13) are superseded by this re-alignment request.
*   **Integration Testing:** Martech team action required to link the delivery ticket for validation between Salesforce (SFMC) and the mobile/web preference center.

**Key Decisions & Alignment**
*   **Stakeholder Coordination:** Collaboration confirmed with Xue Yin and William for SFMC preference center building (James Huang, 11/09).
*   **Development Focus:** Backend finalization pending alignment on the new timeline post-26 Mar update.

**Blockers & Rationale**
*   **Timeline Dependency:** Development schedule is fluid due to the need for CCO and CRM alignment on specific dates following the 26 Mar request.
*   **Integration Gap:** Testing remains halted pending the Martech team to link the delivery ticket for integration validation.


## [32/58] [1HD] Phase 2 - Build to enable scaling of 1 hour to 100 stores
Source: jira | Key: OMNI-1425 | Status: Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Rajesh Dobariya | polaris-work-item-link: DPD-627 | Last Updated: 2026-03-26T13:33:43.667744+00:00
**Jira Ticket Summary: OMNI-1425**
**Subject:** [1HD] Phase 2 - Build to enable scaling of 1 hour to 100 stores
**Assignee/Reporter:** Rajesh Dobariya | **Priority:** High | **Status:** To Do (Prioritised)

### Current Status
The ticket remains an "Idea" type in the "To Do" phase. As of 2026-03-19, the description requires comprehensive population across all standard sections prior to pitching. While initial discussions refined requirements, the core Jira fields (Problem Definition, Goals, Solution Summary, etc.) remain incomplete pending business stakeholder input on user segments and volume impact.

### Key Decisions & Scope Definitions
*   **Core Objective:** Eliminate manual order handling and reduce human error when scaling 1-hour delivery (1HD) to 100 stores. The initiative will iterate based on discoveries from the Pilot trial.
*   **Functional Requirements:**
    *   **3PL Integration:** Push order details/location; receive last-mile updates and Proof of Delivery (POD). Vendor app must display live tracking outside the FPG app.
    *   **Picker App:** Enhancements for real-time new order notifications.
    *   **Store Operations:** Streamline store creation (inventory, assortment, time-slots, capacity) and handle 1HD in Financial Food Service (FFS) stores with specific accounting entries.
*   **User Story (Amendment):** As a shopper, when I complete an order and forget items, I want to amend my order to avoid multiple orders and delivery fees.

### Pending Actions & Ownership
Rajesh Dobariya must finalize the following sections based on stakeholder input:
*   **Problem Definition:** Identify specific user segments, estimated affected volume (% of total users), current workarounds (e.g., placing new orders), and problem severity.
*   **Business Impact & Metrics:** Define Annual GMV/Cost savings. Set targets for AOV increase ($X to $Y within 6 weeks) and Perfect Order rate improvement (X% to Y% in 3 months).
*   **Operational Logic Clarifications:**
    *   **Trigger Timing:** Clarify if the vendor is notified at order placement or packed status.
    *   **Data Scope:** Confirm required fields (Name, Address, Contact only?).
    *   **Completion Protocol:** Define how/when the vendor app notifies DBP upon completion and records POD.

### Key Dates & Blockers
*   **2026-03-19:** Last recorded status update; dependency remains on external clarity for financial metrics and operational rules.
*   **Blocker:** Incomplete solution design and undefined 3PL communication protocols prevent accurate effort estimation.
*   **Dependency:** Must resolve questions regarding vendor notification timing, data fields, and completion logic before pitching.

### Technical References & Linked Items
*   **Linked Issue:** DPD-627 (Polaris work item link).
*   **Context:** The initiative relies on an iterative approach based on Pilot trial discoveries.


## [33/58] Integrate personalized gamification challenge with FP app
Source: jira | Key: OMNI-1414 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: James Huang | polaris-work-item-link: DPD-297 | Last Updated: 2026-03-26T13:34:02.832548+00:00
**Ticket:** OMNI-1414 (Idea) | **Priority:** High | **Assignee:** Rajesh Dobariya | **Reporter:** James Huang
**Linked Issue:** DPD-297
**Current Status:** In Development / In Progress

### Current State
Backend development for the UntieNot gamification integration has commenced. As of Jan 7, 2026, the project integrates a personalized challenge platform with the FP app targeting 1.8M DCC shoppers and marketers. The solution addresses the need for behavior-based challenges that drive GMV through efficient campaign creation.

**Technical Approach:**
*   **Data Security:** Customer UID must be hashed using SHA256 + salt ('s@veValue!') before passing via URL webview (per Alvin Choo).
*   **Entry Points:** Frontend development required across OMNI Homepage, Rewards page, PNW Banner, Popup, Voucher Wallet, and Rewards Tile.

**Effort Estimate:** Total 3 man-weeks split between Backend (1 week) and Frontend (2 weeks).

### Business Impact & Metrics
*   **Financial Goal:** Projected $8M incremental GMV over 8 months. This scales from the 2023 UntieNot pilot ($400K/month baseline with 938K DCC, totaling ~$1.6M) to a target audience of 1.7M–1.8M DCC using category and format challenges for wider adoption.
*   **User Value:** Shoppers seek relevant milestones/rewards based on app, in-store, or eDM interactions; Marketers require efficient tools to launch high-participation campaigns.
*   **Key Metrics:** Challenge participation rate and completion rate (Customer Experience).

### Pending Actions & Ownership
*   **Data Handoff:** James Huang confirmed a mapping file (Customer UID to personalized challenge URLs) is required in the 1st week of February.
*   **Technical Finalization:** Rajesh Dobariya must align on the technical approach by Feb 20, 2026.
*   **UAT Execution:** Scheduled for March 27, 2026 (rescheduled to prioritize "Project Light"). Owner: Rajesh Dobariya.
*   **Launch Planning:** Business live date remains TBD pending UntieNot issue identification. Delivery dates must be communicated to the CCO team. Owners: Rajesh Dobariya/James Huang.

### Key Decisions & Estimates
*   **Solution Strategy:** Contracted UntieNot to run personalized gamification for all 1.8M DCC users; app team support is critical for entry point awareness.
*   **Timeline Shift:** UAT moved from March 24th to March 27th. Target Technical Live date adjusted to April 2, 2026 (providing a 1-week buffer for post-UAT fixes).

### Key Dates & Deadlines
*   **Feb 20, 2026:** Deadline to finalize technical approach.
*   **Mar 27, 2026:** Scheduled UAT start.
*   **Apr 2, 2026:** Target Technical Live date.
*   **TBD:** Business Live date (contingent on UntieNot feedback).

### Blockers & Risks
*   **Business Readiness:** Launch timeline blocked by the "Business side" finalizing go-live dates pending UntieNot issue identification.
*   **Prioritization:** UAT rescheduling indicates resource contention with "Project Light."


## [34/58] Enable all 3P domain links to open in the in-app browser from banner redirection
Source: jira | Key: OMNI-1420 | Status: UAT (In Progress) | Type: Idea | Priority: High | Assignee: Nikhil Grover | Reporter: Nikhil Grover | polaris-work-item-link: DPD-372 | Last Updated: 2026-03-26T21:32:13.502770+00:00
**Jira Ticket Summary: OMNI-1420**
**Subject:** Enable all 3P domain links to open in the in-app browser from banner redirection.
**Current Status:** UAT (In Progress) | **Assignee:** Nikhil Grover | **Priority:** High | **Linked Issue:** DPD-372

**Problem & Business Impact**
*   **Problem:** Non-endemic 3P advertisers require users to visit campaign pages on the advertiser's domain. Current whitelisting requires an app update, creating a lead time of up to 4 weeks. This significantly slows the RMN BD sales cycle and revenue generation.
*   **Goal:** Enable non-endemic campaigns on the in-app browser without requiring an app update.
*   **Impact:** Potential to capture up to $500K in GMV from lead generation and non-endemic campaigns. Expected financial impact: AOV increase within 6 weeks; Customer experience (Perfect Order) improvement within 3 months.

**Solution & Technical Decisions**
*   **Final Solution:** Create a split config to host whitelisted domain names and update the banner component to check destination links against this Split, directing traffic to the in-app browser. This aligns with the backoffice-managed whitelist approach approved by Cyber Security (Feb 11) after rejecting total removal of whitelisting.
*   **Rejected Solutions:**
    *   Removing whitelisting entirely: Rejected by Cyber Security on 2026-02-11 due to other app use cases.
    *   Note: While the original description proposed Split, internal alignment confirmed using backend-managed whitelisting without app updates as the primary strategy.

**Resource & Timeline**
*   **Effort Estimate:** 2 man weeks total (1 week per platform).
*   **Resource Strategy:** Initially considered external resources via Accenture, but rejected on 2026-03-11 due to a 7-8 week commitment time. The business aligned to use internal resources instead.
*   **Current State:** Nikhil Grover is awaiting completion of "UntieNots" tasks before starting front-end work. Start date targeted for the second half of the week of March 16, 2026.

**Pending Actions & Ownership**
*   **Front-end Development:** Awaiting "UntieNots" completion to begin implementation. No other active blockers noted as of March 11, 2026.
*   **Reporting:** Status updated to UAT (In Progress) with Nikhil Grover confirmed as both reporter and assignee.

**Summary of Chronology**
*   *Jan 29:* Ticket created by Nikhil Grover; initial description proposed using Split for whitelisting.
*   *Feb 11:* Cyber Security ruled out removing whitelisting; backend-only solution approved.
*   *Feb 12:* Winson Lim rejected Split as a technical component; ROI updated by Sathya Murthy Karthik.
*   *Mar 11:* Accenture timeline deemed too long; decision made to utilize internal resources. Front-end start date set for week of March 16 pending "UntieNots."


## [35/58] Transition from fixed-tenancy to impressions-based banner delivery model
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


## [36/58] [Pilot] - 1 to 1 Personalised vouchers for scan at door 
Source: jira | Key: OMNI-1427 | Status: Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Rajesh Dobariya | polaris-work-item-link: DPD-824 | Last Updated: 2026-03-26T13:34:22.964564+00:00
**Daily Briefing Summary: OMNI-1427**

**Ticket Overview**
*   **ID:** OMNI-1427 ([Pilot] - 1 to 1 Personalised vouchers for scan at door)
*   **Link:** DPD-824 (Polaris work item)
*   **Status:** Prioritised / To Do
*   **Priority:** High
*   **Assignee/Reporter:** Rajesh Dobariya
*   **Issue Type:** Idea

**Current State & Decisions Made**
The initiative remains in the "To Do" phase, aiming to replace manual, rule-based voucher issuance with AI-driven 1-to-1 personalization via LEAP. Key governance and logic updates confirmed:
1.  **RMN Priority:** Users eligible for RMN vouchers (based on scan sequence/segmentation) receive them exclusively during active campaigns, overriding test/control status. The OMNI team retains sole authority over RMN campaign timing and traffic priority.
2.  **Segmentation:** Control and Test groups are defined by the CCO team based on specific segments.
3.  **Issuance Logic:** Upon QR scan:
    *   **Test Group:** Qualifies for BAU vouchers? Receives LEAP AI suggestions. Otherwise, follows rule engine.
    *   **Control/Non-Qualifiers:** Receive standard rule-engine configured vouchers.

**Business Impact & Metrics (Validated)**
New calculations from Rachel Chan (2026-03-26) validate financial and operational gains:
*   **Financial Impact:** Projected **$3.5M incremental GMV/year**.
    *   *Basis:* Scales a 28-day CNY model ($146k/month for 150k users) to 300k Scan MAU.
    *   *Drivers:* Assumes 6.5% blended redemption, 50% improvement in redemption rates, $26 incremental spend per member, and a 5% upspend stretch factor.
*   **Cost Avoidance:** Estimated **48,000 man-hours saved/year** (refined from previous estimates).
    *   *Basis:* Automating voucher creation scales from ~27 manual combinations to 3,000+ AI-generated vouchers (100x increase).
    *   *Calculation:* 40 hours per campaign × 100 scale factor × 12 months.

**Proposed Solution Logic**
The system differentiates issuance at QR scan:
*   **Test Group:** Receives LEAP AI suggestions if they qualify for BAU vouchers.
*   **Control/Non-Qualifiers:** Receive standard rule-engine configured vouchers.

**Pending Actions & Ownership**
To proceed to pitch, the following must be finalized (as of 2026-03-26):
*   **Documentation:** Ensure all components (Problem Definition, Goal, Business Plans, Operational Processes) are filled before pitching.
*   **Methodology Validation:** Confirm calculation assumptions for redemption rates and upspend stretch factors as requested by Rajesh Dobariya.
*   **Operational Planning:** Define workflows for automating voucher creation at scale and vendor alignment with LEAP.

**Key Dates & Blockers**
*   **Deadlines:** None set (Duedate: null).
*   **Blockers:** Ticket is ready to proceed pending final documentation completeness; placeholders previously flagged as blockers have been resolved by the attached calculation methodology.


## [37/58] FP Pay experience improvements to support new auto apply voucher at IPOS/KPOS 
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


## [38/58] GST Compliance Phase 2 - Refunds and return
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


## [39/58] AI shopping assistant: An engaging experience for customers to build their shopping cart within seconds
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


## [40/58] Enable WhatsApp Marketing Consent at Sign-Up Page and Preference Center to Unlock Better Engagement Opportunities
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


## [41/58] Support the SIT/UAT/Beta/Cut Over for MyInfo and LEAP core system integration
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


## [42/58] Achieve 100% GST compliance for Ecom orders 
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


## [43/58] FPG - Fraud detect and prevention 
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


## [44/58] Mirakl foundational work for scalability
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


## [45/58] [Pre-order] 'Mark as Paid' for In-Store Preorders
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


## [46/58] Optimising Airway Bill Generation Experience for Seller
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


## [47/58] [POC] Enabling PalmPay to allow quick checkout
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


## [48/58] Project Turbo to support new POS version
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


## [49/58] Integrating Tencent's  Biometric Authentication (Palm Pay) solution with FPG App for member verification  
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


## [50/58] Compliance - Improving the Cart calculation logic 
Source: jira | Key: OMNI-1179 | Status: Paused (To Do) | Type: Idea | Priority: High | Assignee: Alvin Choo | Reporter: Alvin Choo | Labels: Foundation | polaris-work-item-link: CART-54 | Last Updated: 2026-03-24T13:31:02.520794+00:00
**Jira Ticket Briefing: OMNI-1179 (Compliance - Improving Cart Calculation Logic)**

**Current Status & State**
*   **Status:** Paused (Category: To Do).
*   **Priority:** High.
*   **Assignee/Reporter:** Alvin Choo.
*   **Type:** Idea | **Labels:** Foundation.
*   **Linked Issue:** CART-54 (Polaris work item).
*   **Context:** Addresses customer frustration regarding pricing, promotion, and tax discrepancies across Online, In-store, Scan & Go, and Marketplace channels. The goal is a unified cart service to support scalability, GST compliance, and accurate order splitting.

**Decisions Made & Scope Alignment**
1.  **Initial Definition (Feb 24, 2025):** Defined problem scope targeting "X%" developer time on investigation and "Z" feature parity gaps. Success metrics include improved checkout conversion and reduced pricing rule implementation time.
2.  **Scope Reduction:** Aligned with the upcoming app replatform ("Project Light"). Scope strictly limited to:
    *   CRUD of core cart services.
    *   Cart calculation logic.
3.  **Removal & Reinstatement (Mar 24, 2026):**
    *   **10:32:** Rajesh Dobariya confirmed the ticket could be removed and addressed in "Project Light."
    *   **10:33:** Sathya Murthy Karthik executed the removal.
    *   **11:28:** Rajesh Dobariya instructed to reinstate the ticket, noting it is a compliance topic requiring Steer Co discussion.
    *   **11:31:** Sathya Murthy Karthik reinstated the ticket.

**Pending Actions & Ownership**
*   **Steer Co Discussion Required:** The ticket must be reviewed at the Steering Committee to validate if the reduced scope (Core Cart/Calculation) is necessary prior to the replatform, rather than deferring entirely to Project Light.
    *   **Owner:** Alvin Choo / Sathya Murthy Karthik / Rajesh Dobariya.
    *   **Status Update:** Active; reinstated after brief removal.

**Key Dates & Deadlines**
*   **Feb 24, 2025 (16:53):** Idea creation with detailed problem definition, success criteria, and assumptions established.
*   **Mar 24, 2026 (Morning):** Temporary removal and subsequent reinstatement confirmed by Rajesh Dobariya for Steer Co review.

**Blockers & Risks**
*   **Redundancy Risk:** Scope may be superseded by the "Project Light" replatform or order splitting initiatives.
*   **Compliance Urgency:** Despite scope reduction, GST and calculation consistency remain critical compliance requirements mandating Steer Co validation.
*   **Board Cleanup:** Ticket movement (remove/add) temporarily impacted board flow; now stabilized pending decision.

**Technical References & Metrics**
*   **Linked Issue:** CART-54.
*   **Related Epics:** Shoppable grocery in Omni Home, GST project, Replatform (Order splitting), Scan & Go splits, Marketplace scaling.
*   **User Impact:** X% of developer time allocated to cart investigation; Z feature parity gaps across channels; A% of marketplace transactions require custom calculations.
*   **Success Metrics:** Improved Cart-to-checkout price consistency (Baseline: X%, Expected: Y%), reduced checkout abandonment due to pricing errors, and decreased time to implement new pricing rules (Baseline: X weeks).


## [51/58] [OSMOS only] Integrate fit-for-purpose digital signage with OSMOS for in-store ad activation (merged into another ticket)
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


## [52/58] Available to Promise 1.0 [MVP] - New Time-based Inventory logic
Source: jira | Key: OMNI-1391 | Status: Discovery (To Do) | Type: Idea | Priority: High | Assignee: Yi Hao Tan | Reporter: Prajney Sribhashyam | Last Updated: 2026-03-26T21:32:35.809265+00:00
**Jira Ticket Briefing: OMNI-1391**
**Topic:** Available to Promise (ATP) 1.0 [MVP] – New Time-based Inventory Logic
**Status:** Discovery (To Do) | **Priority:** High | **Type:** Idea
**Assignee:** Yi Hao Tan | **Reporter:** Prajney Sribhashyam

**Current State & Context**
The FPG application currently utilizes "Global Reservation Logic," blocking all Stock on Hand (SOH) immediately upon order placement regardless of the delivery date. This causes false stock-outs, lost revenue, and high wastage as near-expiry stock remains locked for future slots. The MVP aims to implement time-based inventory logic strictly for **PFC** and **selected SKUs**, calculating availability in 2-hour picking blocks over the next 7 days.

**Key Solution Components**
1.  **Replenishment Patterns:** Manual preset of SKU-level stock additions by timeslot (e.g., +200 qty arriving daily at 11 AM, ready for pick by 1 PM after buffer).
2.  **Picking Time Mapping:** Configurable mapping between delivery slots and inventory reference points (e.g., 8 AM delivery uses previous day 8 PM inventory).
3.  **New Logic Formula:** `SOH by timeslot = Previous SOH + Preset Replenishment - Variance - Reservation`.
4.  **Indexer Workaround:** Applying "Unlimited SKU" logic to the Indexer for these SKUs to prevent search/PLP visibility issues from outdated counts.

**Pending Actions & Ownership**
*   **Fresh/Van Sales Strategy:** Finalize hybrid approach. Tech team proposed "Mother DC SOH" for Ambient SKUs; however, Business Team confirmed this fails for Fresh/Van SKUs (pork, eggs, bread) due to short shelf life. *Action Owner:* Yi Hao Tan / Business Team.
*   **Effort Estimation:** Confirm development effort size (Small vs. Extra Small). *Action Owner:* Danielle Lee.

**Decisions & Status Updates**
*   **Scope Conflict Resolution (2026-03-26):** During the 3:30 PM meeting, the Tech team (HIVE/Inventory) suggested using "Mother DC SOH" derived values for Ambient SKUs due to higher volume visibility. However, the Business Team reiterated on 2026-03-26 that this is insufficient for Fresh/Van SKUs with short shelf lives.
*   **Strategic Alignment:** The initiative will proceed with a hybrid model: "Mother DC SOH" for Ambient SKUs and manual "Daily Presets" for Fresh/Van SKUs to address critical pain points immediately.
*   **Scope:** Strictly PFC only for this stage; selected SKUs only.

**Key Dates, Constraints & Risks**
*   **Critical Limitation:** No system visibility for SKU expiry/write-off values or batch-level data. Risk remains where customers order items that are actually expired/unavailable in the warehouse.
*   **Business Impact Target:** Estimated $5.5M annual GMV improvement (conservative, excluding fresh penetration gains).
*   **Reference Documents:** BRD Document, Solution Discussion, Calculation Logic Google Sheet.

**Summary**
Progress remains in Discovery pending final technical alignment on inventory referencing. Following the 2026-03-26 meeting, a hybrid approach was agreed upon: utilizing "Mother DC SOH" for Ambient SKUs while retaining manual "Daily Presets" for Fresh/Van categories to prevent stock-outs and wastage. The initiative is scoped strictly to PFC and selected SKUs to rapidly reduce shrinkage and improve Sales-weighted Availability (SWA).


## [53/58] Enabling User Consent for customer data
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


## [54/58] ROOH 2.0 - Sourcing and Implementation of best-in-class In-Store Ad booking, management, attribution platform
Source: jira | Key: OMNI-1400 | Status: Discovery (To Do) | Type: Idea | Priority: High | Assignee: Yi Hao Tan | Reporter: Nikhil Grover | polaris-merge-work-item-link: OMNI-1247, OMNI-1247 | Last Updated: 2026-03-26T21:32:53.974685+00:00
**Daily Briefing Summary: OMNI-1400**

**Current Status & State**
*   **Ticket ID:** OMNI-1400 (ROOH 2.0)
*   **Issue Type:** Idea
*   **Priority:** High
*   **Status Category:** To Do (Discovery)
*   **Assignee:** Yi Hao Tan
*   **Reporter:** Nikhil Grover
*   **Linked Issue:** OMNI-1247 (Polaris merge work item link)

**Key Context & Problem Definition**
The initiative addresses the lack of performance benchmarks in current In-Store Retail Media (RMN). Currently, campaigns sell 15-second ad slots without impression data, forcing BD teams into manual email planning and requiring physical proof-of-play photos. Operations rely on monday.com for booking across two CMS platforms.
*   **Problem:** Ad Ops and RMN BD lack visibility into shopper views per screen/store, hindering media planning and campaign optimization.
*   **Goal:** Transition from selling "ad plays" to "impressions," establish baselines for footfall/impressions per screen/store, and enable demographic breakdowns (age, gender, segment).
*   **Financial Targets:** Projected Retail Media GMV growth from $60K (2025) to $1.4M (2026), reaching $3M (2027). Estimated annual revenue potential is ~$2m.

**Decisions Made**
*   **March 19, 2026:** Nikhil Grover reassigned ownership to the ROOH lead.
*   **March 20, 2026:** Yi Hao Tan confirmed consolidating work into OMNI-1400.

**Pending Actions & Ownership**
*   **Vendor Sourcing & Implementation:** Yi Hao Tan is responsible for sourcing/implementing a best-in-class platform for booking, management, and attribution.
*   **Documentation Completion (Critical):** The ticket description mandates filling all components before vendor pitching. Key missing sections include:
    *   **Business Impact:** Define annual GMV/Income/Cost savings.
    *   **Product Metrics:** Specify AOV increase targets ($X to $Y in 6 weeks) and Perfect Order improvement targets (X% to Y% in 3 months). Establish baselines for impressions, footfall, fill rate, and CPM.
    *   **Operational Processes & Business Plans:** Outline workflows, budget approvals, and go-to-market strategies.
    *   **Business Rules/Logic:** Define system behaviors and dependencies.

**Dates & Deadlines**
*   **No Due Date:** The ticket currently has no assigned deadline.
*   **Historical Updates:** Last activity recorded on March 20, 2026; new content added November 4, 2025.

**Blockers**
*   **Incomplete Documentation:** Critical sections for Business Plans, Operational Processes, specific Product Metrics (AOV/Perfect Order), and Business Rules are undefined. Pitching cannot proceed until these are completed.
*   **Vendor Selection:** The "best-in-class" platform has not yet been selected or implemented; the ticket remains in the "Idea" phase.


## [55/58] [OSMOS Only] Streamline seller/brand onboarding on OSMOS
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


## [56/58] [1hd] Phase 2 -  Scaling one hour delivery to more stores (TO REMOVE)
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


## [57/58] Blocking of specific postal code from allowing customer to select for delivery address
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


## [58/58] Adhere to alcohol act compliance 
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
