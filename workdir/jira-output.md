

## [1/57] Dynamic ad slot configuration for Homepage swimlanes
Source: jira | Key: DPD-715 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-17 | Resolution: Done | child: DPD-849 | parent: DPD-710 | Last Updated: 2026-03-30T21:30:46.670732+00:00
### Daily Briefing Summary: DPD-715 (Dynamic Ad Slot Configuration)

**Current Status:** **IN RELEASE QUEUE** (Resolution: Done). The story was created by Nikhil Grover on **2026-03-10** to enable dynamic ad placement via Split feature flags without code changes. It is technically complete, UAT signed off, and resolved.

**Key Decisions & Actions Taken:**
*   **Feature Flag Implementation:** Logic successfully implemented to control slot indices dynamically (e.g., `[3, 5, 7]` or `[2, 4, 6, 8, 10]`). Supports empty arrays for organic-only views and honors existing stock availability checks.
*   **Test Automation Status:** Confirmed by Milind Badame on **2026-03-30** that existing E2E tests cover static ad label positions in vertical and horizontal swimlanes. Runtime verification based on Split settings cannot be automated as labels are static; no immediate E2E updates are required unless specific new position verifications are manually requested.
*   **Environment Updates:** Verified SplitIO changes reflect correctly in OG Home & Mobile Apps. Omni Home slot positions now match configured values (e.g., `3, 5, 7`), resolving previous discrepancies where swimlanes were stuck at fixed positions `(1, 3)`.

**Critical New Findings (Post-Deployment):**
*   **Race Condition Identified:** On **2026-03-28**, Michael Bui identified a code defect where a shared variable (`share`) was overwritten during concurrent requests. This specific issue affected `pnct=1` functionality immediately post-deployment. While verified in UAT, it requires attention in production stability checks.

**Pending Actions & Ownership:**
*   **Immediate Monitoring:** Close monitoring of concurrent request stability is required across Omni and OG Homepages due to the shared variable race condition.
*   **Root Cause Analysis:** Verify if `share` variable logic requires a broader code review to prevent data integrity issues in high-concurrency scenarios not captured in UAT.
*   **E2E Maintenance:** No action required for E2E updates pending manual verification requests from stakeholders.

**Technical Context:**
*   **Logic:** API requests adapt dynamically to Split configuration counts (e.g., 6 slots = request 6 ads). Fallback defaults (`[1,3]`) apply when the flag is OFF.
*   **Resilience:** System handles Ad Supply Shortages by filling available slots with organic content and ignores indices exceeding swimlane length (e.g., index 20 in a 10-item list).

**Timeline Update:**
*   **2026-03-10:** Ticket created by Nikhil Grover defining acceptance criteria for dynamic API requests, fallback defaults, empty array handling, and stock constraints.
*   **2026-03-19:** UAT session conducted by Michael Bui.
*   **2026-03-25:** Nikhil Grover signed off on UAT; requested production config `3, 5, 7, 11, 13, 15`.
*   **2026-03-26:** Michael Bui deployed to Production; confirmed functionality.
*   **2026-03-28:** Michael Bui identified race condition regarding shared variable overwrites during concurrent requests (`pnct=1`).
*   **2026-03-30:** Milind Badame clarified E2E automation strategy; no test updates required for runtime Split verification.

**Blockers/Notes:**
*   **Resolution of Discrepancy:** The issue regarding fixed positions in Omni Home swimlanes has been resolved. Stakeholders confirmed slot positions now match SplitIO flag values.
*   **Dependencies:** Parent ticket DPD-710 ([RMN] Activate product ads in Omni Home swimlanes); Subtask DPD-849 ([BE] update layout-service dependency).

**Key Dates & Constraints:**
*   **Due Date:** 2026-03-17 (Deployment occurred post-due date on 2026-03-26).


## [2/57] Dynamic ad slots for vertical scroll on omni homepage
Source: jira | Key: DPD-733 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-17 | Resolution: Done | parent: DPD-710 | Last Updated: 2026-03-30T21:31:05.241607+00:00
**Daily Briefing Summary: DPD-733**

**1. Current Status & State**
*   **Ticket ID:** DPD-733 (Dynamic ad slots for vertical scroll on omni homepage)
*   **Status:** IN RELASE QUEUE (Resolution: Done).
*   **Parent Epic:** DPD-710 ("[RMN] Activate product ads in Omni Home swimlanes").
*   **Priority:** High.
*   **Type:** Story.
*   **Due Date:** March 17, 2026.
*   **Assignee:** Michael Bui.
*   **Reporter:** Nikhil Grover.

**2. Actions Pending & Ownership**
*   **Pending Action:** Deployment from the release queue to production is required.
*   **QA Scope Update:** Existing E2E tests verify static ad label positions for vertical and horizontal swimlanes. Automated runtime verification for Split on/off states is currently not feasible without specific position inputs. No E2E updates are required at this time unless manual position inputs are provided by the team.
*   **Owner:** Michael Bui (Assignee).
*   **Stakeholder/Reporter:** Nikhil Grover.
*   **QA Note:** Milind Badame confirmed that while static label verification exists, runtime verification for Split settings requires explicit input to update tests.

**3. Key Decisions & Technical Implementation**
The feature enables dynamic control of product ad placement and count via a Split feature flag, eliminating code changes or manual API updates based on the following acceptance criteria:

*   **Dynamic Logic:** With the feature flag ON and configuration set (e.g., `[3, 5, 7]`), the app requests N ads matching the array length and renders them at specific indices.
*   **Fallback Behavior:** If the feature flag is OFF but ads are enabled, the system defaults to slots `[1, 3]` (requesting 2 ads).
*   **Real-Time Updates:** Updating Split configuration (e.g., to `[2, 4, 6, 8, 10]`) in the dashboard immediately affects new user sessions without code deployment.
*   **Edge Case Handling:**
    *   **Empty Config:** If configured as `[]`, the system requests 0 ads; only organic content is displayed with no gaps.
    *   **Supply Shortage:** If the API returns fewer ads than requested (e.g., config asks for 3, API returns 2), valid slots fill first, and remaining slots display organic content.
    *   **Out-of-Bounds:** Indices exceeding the available content range are ignored; ads render only within the valid range.
*   **Constraints:** The system strictly honors existing stock availability checks; out-of-stock products cannot be served as ads.

**4. Key Dates & Deadlines**
*   **Due Date:** March 17, 2026.
*   **Last Activity:** 
    *   March 30, 2026: Milind Badame confirmed E2E automation scope (static verification only; no updates needed).
    *   March 10, 2026: Ticket status updated to "IN RELASE QUEUE".
*   **Blockers:** None reported; ticket is resolved and awaiting release deployment.


## [3/57] Transition to Impression-Based Inventory & Multi-Banner Delivery
Source: jira | Key: DPD-838 | Status: TO BE DEFINED (To Do) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | parent: DPD-385 | Last Updated: 2026-03-29T05:30:43.708501+00:00
**Daily Briefing Summary: DPD-838**

**Current Status**
Ticket **DPD-838**, titled "Transition to Impression-Based Inventory & Multi-Banner Delivery," is a **High** priority **Story** in the **"TO BE DEFINED"** (To Do) state. Assigned to **Michael Bui** and reported by **Nikhil Grover**, it remains unresolved with no due date set. It serves as an execution component for parent ticket **DPD-385**.
*   **Last Activity:** 2026-03-27 (Ticket creation/logged) and 2026-03-28T22:44:15+0800 (Questions raised).

**Pending Actions & Ownership**
The Product Manager/Ad Ops Lead must execute the migration from fixed-slot tenancy to an inventory-based model. However, assignment is currently in flux due to unresolved scope questions. **Michael Bui** has raised critical clarifications regarding the execution plan:
*   **Scope Clarification:** Michael Bui questioned if Category and Search pages (using the legacy MPS service) require immediate migration alongside new components (Omni/OG Home, FPPay), noting potential FE component changes and video support discrepancies.
*   **Blockers:** The "TO BE DEFINED" status reflects a need to finalize scope before development. Specific questions regarding OSMOS logic limits, position tracking, fallback behaviors, and API availability must be resolved by the reporter/PM before work can commence.

**Decisions Made & Technical Requirements**
The ticket defines specific acceptance criteria for the transition:
1.  **Unified Request Architecture:** For defined pages (Omni/OG/O2O Home, Search, Category, FP Pay), the system must send a single batch request to OSMOS for all 20 slots, including page-level metadata (User ID, page type/ID, category ID, search keyword).
2.  **Display Sequence Integrity:** Banners returned by OSMOS must be displayed in the exact sequence provided.
3.  **Endemic Prioritization Logic:** If a non-endemic banner occupies Position 1, the first endemic banner is boosted to Position 1 while maintaining relative order of subsequent banners. Logic for identifying "non-endemic" via the "Campaign type" field requires clarification (exact vs. substring match).
4.  **Duplicate Slot Handling:** If multiple banners share the same "Slot" parameter number, only the first instance is passed; duplicates are dropped. Clarification is needed on how OSMOS manages position values (e.g., `[-1,0,1,2,2,5,999]`).
5.  **Partial Response Management:** If fewer than 20 campaigns are configured, the system returns only available banners without empty responses.
6.  **Edge Cases:** Requirements for auto-play/auto-next logic (for videos), fallback handling if OSMOS returns no results or is inaccessible, and limits on OSMOS `pcnt` (currently unclear if limit remains at 10) require definition.

**Key Dates, Deadlines, & Blockers**
*   **Last Activity:** 2026-03-28T22:44:15+0800 (Michael Bui raised questions).
*   **Deadline:** None currently set (`duedate: null`).
*   **Blockers:** Pending answers to six specific technical queries from Michael Bui regarding legacy page scope, endemic identification logic, OSMOS `pcnt` limits, position tracking, video logic, and error handling.

**Stakeholders**
*   **Reporter:** Nikhil Grover
*   **Assignee:** Michael Bui


## [4/57] Suppress duplicate BCRS deposit posting via order metadata
Source: jira | Key: DPD-842 | Status: TESTING IN PREPRODUCTION (In Progress) | Type: Subtask | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | child: DPD-383 | parent: DPD-383 | work-item-split: DPD-807, DPD-807 | Last Updated: 2026-03-28T03:34:37.903686+00:00
**Daily Briefing Summary: DPD-842**

**Current Status**
The subtask **DPD-842** ("Suppress duplicate BCRS deposit posting via order metadata") is currently in the **"TESTING IN PREPRODUCTION"** phase, categorized as "In Progress." This high-priority subtask falls under parent ticket **DPD-383** ("Sales posting for BCRS deposit amount"). The work item was created as a split from linked issue **DPD-807**.

**Ownership and Actions**
*   **Owner:** Michael Bui (Assignee and Reporter).
*   **Pending Action:** No immediate pending actions are required; the testing phase has concluded with validation.
*   **Testing Execution:** Testing activities were conducted on **2026-03-28**. The status was updated to "TESTING IN PREPRODUCTION" at **02:57:42+0800**.

**Decisions Made**
*   **Validation Confirmed:** On **2026-03-28 at 03:02:22+0800**, it was confirmed that re-delivering an order will **not** send a duplicate BCRS deposit posting to SAP. This validation relies on the suppression logic utilizing order metadata.
*   **Data Capture:** To support this verification, the system state after BCRS posting was captured at **2026-03-28 03:00:02+0800**.

**Key Dates and Blockers**
*   **Timeline:** Key activities occurred on **2026-03-28**:
    *   **02:57:42+0800:** Ticket title confirmed as "Suppress duplicate BCRS deposit posting via order metadata"; Status set to "TESTING IN PREPRODUCTION".
    *   **03:00:02+0800:** Post-BCRS posting state captured.
    *   **03:02:22+0800:** Duplicate suppression logic validated successfully.
*   **Deadlines:** The ticket currently has **no assigned due date**.
*   **Blockers:** No blockers or resolution issues are currently listed.

**Technical References**
*   **Parent Issue:** DPD-383
*   **Linked Split:** DPD-807
*   **Target System:** SAP (specifically regarding BCRS deposit amounts).
*   **Resolution Logic:** The system suppresses duplicate postings by utilizing order metadata.


## [5/57] Charge BCRS deposit for re-delivery
Source: jira | Key: DPD-807 | Status: TO BE DEFINED (To Do) | Type: Story | Priority: High | Reporter: Prajney Sribhashyam | parent: DPD-225 | relates: DPD-383, DPD-383 | work-item-split: DPD-842, DPD-842 | Last Updated: 2026-03-28T03:34:59.700323+00:00
**Daily Briefing Summary: DPD-807 – Charge BCRS Deposit for Re-delivery**

**Current Status & State**
*   **Ticket ID:** DPD-807 (Story)
*   **Status:** TO BE DEFINED (Category: To Do)
*   **Priority:** High
*   **Parent Ticket:** DPD-225 ([BCRS] Inform customers on BCRS deposit during Order Placement & Returns/Refunds Process)
*   **Reporter:** Prajney Sribhashyam
*   **Assignee:** Unassigned.
*   **Linked Issues:** Relates to DPD-383; Work item split of DPD-842.
*   **Creation Date:** 2026-03-24 (Defined by Prajney Sribhashyam).
*   **Last Activity:** 2026-03-27T15:54:11+0800 (Inquiry regarding Backoffice Custom Fields ownership).

**Decisions Made & Scope Definition**
*   **Core Feature Logic:** As an Operations Manager, the system must apply BCRS deposit fees (e.g., €0.10/unit) to eligible items (plastic bottles, aluminum cans) in re-delivery orders. Non-eligible items (cardboard, produce) are excluded; no charge is applied. The fee appears as a separate line item.
*   **Refund/Credit Logic:** If the original deposit was refunded or cancelled, a new charge applies on re-delivery. Otherwise, duplicate charges are suppressed based on payment history verification.
*   **System Architecture Requirements:**
    *   **Order Service:** Must maintain metadata flag `Deposit posted to SAP`.
    *   **Deposit Sales Posting:** Updates this field to `true` only after the first successful posting; consumes this flag to suppress duplicate postings during re-deliveries.
    *   **RPA Component:** Responsible for charging BCRS deposits to the customer's original payment method and posting sales data.

**Pending Actions & Ownership**
*   **Custom Field Configuration (Urgent):** The `Deposit posted to SAP` field must be added as a custom field in the Config Service metadata via the Backoffice Production page.
    *   *Action:* Identify the owner managing this configuration page.
    *   *Inquiry:* On 2026-03-27, Wai Ching Chan requested clarification on who manages the "Custom Fields" page to facilitate inserting the metadata field.
    *   *Owner:* **Unassigned** (Awaiting identification).
*   **Technical Implementation:** Develop logic in "Deposit sales posting" to set `metadata.Deposit posted to SAP` correctly and implement filtering for BCRS-eligible items.
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

**Key Dates & Deadlines**
*   **Due Date:** Not defined.
*   **Blockers:** No assignee is currently linked to the ticket; development cannot commence until ownership is assigned and the Backoffice Custom Field configuration is resolved.


## [6/57] Sales posting for BCRS deposit amount
Source: jira | Key: DPD-383 | Status: IN RELASE QUEUE (Done) | Type: Story | Priority: High | Assignee: Michael Bui | Reporter: Prajney Sribhashyam | Due: 2026-02-18 | Resolution: Done | blocks: DPD-551, DPD-551 | child: DPD-590, DPD-842 | parent: DPD-225, DPD-590, DPD-842 | relates: DPD-807, DPD-807 | Last Updated: 2026-03-28T03:35:23.712588+00:00
**Ticket:** DPD-383 (Sales posting for BCRS deposit amount)
**Status:** Done | **Category:** In Release Queue | **Priority:** High
**Assignee:** Michael Bui | **Reporter:** Prajney Sribhashyam

**Current State & Key Decisions**
*   **Resolution:** Ticket resolved as **Done** with status "IN RELASE QUEUE". Original due date: 2026-02-18. Parent ticket: **DPD-225** ("[BCRS] Inform customers on BCRS deposit...").
*   **Core Objective:** DBP calculates BCRS deposits at the **order line level** (`deposit price × fulfilled quantity`) and aggregates totals for SAP posting (Order + SKU level). This applies to E-Comm, Marketplace, Returns/Refunds, Donations, and FOC items.
*   **Eligibility Logic:** System processes only **COMPLETED** orders. OFFLINE channels and RB PreOrders are acknowledged but ignored.
*   **Calculation Rules:** Deposit per line = (Deposit Price × Ordered Quantity). Aggregated total is the sum of all eligible lines. Quantities follow BRD rules for final fulfilled quantity.

**Technical Implementation & Acceptance Criteria**
*   **Order Status Handling:** The SAP Deposit Posting service processes orders only when status is `COMPLETED`. Non-COMPLETED messages are acknowledged but not processed.
*   **Channel Filtering:** Explicitly ignores OFFLINE channel orders and RB PreOrders.
*   **Special Scenarios:**
    *   **Donation Orders:** Deposits calculated using standard logic for BCRS-eligible items.
    *   **FOC Items:** Deposits calculated if the master SKU is BCRS-eligible, treated identically to non-FOC items.
*   **Duplicate Prevention:** Subtask **DPD-842** implements suppression via order metadata. A "delivery once" policy on GCP PubSub ensures SAP captures only the first valid posting.

**Pending Actions & Ownership**
*   **Validation:** Michael Bui is monitoring for actual incoming BCRS orders in Production to validate end-to-end SAP posting against live data.
*   **Dependencies:** Blocking issue **DPD-551** (PLU Processor) resolved by exposing `sapMaterialNumber` via API on 2026-02-20. Issue **DPD-807** remains relatable. Subtask **DPD-590** assigned for archiving proposals post-release.

**Key Dates & Timeline**
*   **2026-01-30:** Ticket created; title set to "Sales posting for BCRS deposit amount". Requirements defined for all use cases (E-Comm, Marketplace, Returns/Refunds). Subtask DPD-590 assigned. Status updated to "IN RELASE QUEUE".
*   **2026-02-18:** Original due date passed; ticket resolved as Done. Resolution category updated to "IN RELASE QUEUE".
*   **2026-02-20:** `sapMaterialNumber` exposed via API (Resolves block DPD-551).

**Technical References & Data Points**
*   **Subtasks:** DPD-590 (Clean up archived proposals), DPD-842 (Suppress duplicate posting).
*   **Linked Issues:** Blocks DPD-551; Relates DPD-807.
*   **SAP Configuration Verified:** CompCode `FP10`, DocType `DR`, GL Account `4423` (Deposit), Customer `199997`.
*   **API References:** BRD DBP BCRS Requirement for Plan B, Sample deposit API, Order-v3 API.
*   **Technical Fixes:** CSRF token/cookie handling resolved 403 errors; failure detection distinguishes HTTP 201 success from internal business errors.

**Blockers/Notes**
*   All technical blockers (SAP access in dev/test, material number availability) are cleared.
*   Validation of real-world BCRS orders in Production remains the final step before full operational confirmation.


## [7/57] [BCRS] Inform customers on BCRS deposit during Order Placement & Returns/Refunds Process
Source: jira | Key: DPD-225 | Status: IN DEVELOPMENT (In Progress) | Type: Epic | Priority: High | Reporter: Andin Eswarlal Rajesh | Due: 2026-03-26 | discovery---connected: NEDMT-2334 | parent: DPD-807, DPD-383 | polaris-work-item-link: OMNI-1294, OMNI-1294 | relates: DPD-26 | Last Updated: 2026-03-27T21:32:17.122631+00:00
**Daily Briefing: DPD-225 [BCRS] Inform customers on BCRS deposit during Order Placement & Returns/Refunds Process**

*   **Current Status:** IN DEVELOPMENT (High Priority Epic). Due date is **March 26, 2026**.
    *   *Context:* This initiative integrates Singapore's mandatory $0.10 refundable Beverage Container Return Scheme (BCRS) into core systems ahead of the scheme's official launch. While the title references customer notifications during order placement and returns/refunds, the strategic objective focuses on backend data integrity: flagging BCRS products in Mirakl, synchronizing flags to SAP, and updating sales reporting for accurate revenue tracking.

*   **Pending Actions & Ownership:**
    *   **Documentation Completion:** Critical gaps persist in the "Technical Documents" section; fields for Order Experience, Cart/Checkout, Product Catalogue, UAT Products, and Feature Flags remain empty. Action required: Technical Team must populate these to define UI elements and product lists.
    *   **Design Alignment:** The "Design" reference is currently blank. Specific UI elements (e.g., checkboxes/flags for Mirakl product creation) require formalization before development completion.
    *   **Synchronization Testing:** Verification of the automated sync process between Mirakl and SAP is required to ensure BCRS flags remain consistent across platforms.
    *   **Ownership:** Reported by **Andin Eswarlal Rajesh**. No assignee is currently listed.

*   **Key Decisions & Milestones:**
    *   **Scope Confirmation:** The project strictly defines three deliverables: (1) A new UI element (checkbox/flag) within the Mirakl product creation/update flow for BCRS products; (2) An automated synchronization process between Mirakl and SAP; and (3) Modifications to existing sales reporting to include dedicated fields/filters for BCRS tracking.
    *   **Strategic Value:** Deliverables ensure regulatory compliance (avoiding penalties), operational efficiency (reducing manual entry risks), financial accuracy (auditable BCRS revenue/fee calculations), and improved data integrity (single source of truth).
    *   **Sub-task Reference:** A related strategic sub-issue, **[BCRS] Marketplace products create and update**, was moved from the main ticket for reference.

*   **Key Dates & Blockers:**
    *   **Official Launch Context:** The scheme launches on an upcoming date (specific date TBD), serving as the hard compliance deadline.
    *   **Last Update:** January 22, 2026.
    *   **Blockers:** Missing design specifications and incomplete technical documentation are currently preventing full scope validation.

*   **Linked Issues:**
    *   **Polaris Work Item:** OMNI-1294
    *   **Related:** DPD-26
    *   **Connected Discovery:** NEDMT-2334


## [8/57] [RMN] Streamline event sync from Segment.io to OSMOS to resolve overage
Source: jira | Key: DPD-644 | Status: Done (Done) | Type: Epic | Priority: High | Assignee: Michael Bui | Reporter: Nikhil Grover | Due: 2026-03-12 | Resolution: Done | parent: DPD-645 | polaris-work-item-link: OMNI-1418 | Last Updated: 2026-03-27T21:32:29.917584+00:00
**Daily Briefing: Jira Ticket DPD-644**

*   **Current Status:** The Epic is officially **Done**. Resolution status is confirmed as completed effective March 3, 2026.
*   **Ownership & Pending Actions:** No actions are pending. The ticket was assigned to **Michael Bui**, who executed the work, and reported by **Nikhil Grover**. Both roles remain consistent with the final state of the record.
*   **Decisions Made:** The initiative focused on streamlining the event synchronization pipeline from **Segment.io** directly to **OSMOS**. This architectural adjustment was implemented specifically to resolve data ingestion overage costs associated with the previous configuration.
*   **Key Dates & Deadlines:**
    *   **Due Date:** March 12, 2026 (Deadline met).
    *   **Resolution Date:** March 3, 2026. The status was updated to "Done" at 14:07 UTC+08 on this date.
*   **Technical References:**
    *   **Ticket ID:** DPD-644
    *   **Linked Work Item:** OMNI-1418 (Polaris work item link)
    *   **Priority:** High
    *   **Issue Type:** Epic

**Summary:**
The high-priority Epic **DPD-644**, titled "[RMN] Streamline event sync from Segment.io to OSMOS to resolve overage," has been formally resolved. The work was assigned to **Michael Bui** and reported by **Nikhil Grover**. On March 3, 2026, at 14:07 UTC+08, the team successfully optimized the data flow between **Segment.io** and **OSMOS**, achieving a status of "Done" ahead of the scheduled due date of March 12, 2026. The primary objective was to eliminate unnecessary cost overages caused by inefficient syncing mechanisms, a decision executed as part of this high-priority initiative. No blockers were recorded during the execution cycle. The associated Polaris work item **OMNI-1418** remains linked to this epic for traceability.

The resolution status ("Done") and issue type (Epic) are confirmed in the latest system update. All metadata, including priority levels and assignee details, aligns with the final record.


## [9/57] [BCRS Compliance] Phase 2: Order Place & Returns/Refunds Process
Source: jira | Key: OMNI-1294 | Status: Technical Live (Done) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Winson Lim | Labels: bcrs | discovery---connected: NEDMT-2334 | polaris-work-item-link: DPD-225, DPD-225 | Last Updated: 2026-03-27T09:35:20.749795+00:00
**Ticket:** OMNI-1294 | **[BCRS Compliance] Phase 2: Order Place & Returns/Refunds Process**
**Status:** Technical Live (Done) | **Risk Level:** High | **Assignee:** Prajney Sribhashyam
**Reporter:** Winson Lim | **Priority:** High | **Type:** Idea

### Current Status
*   **Regulatory Context:** Singapore NEA mandates a $0.10 deposit on regulated beverages (150ml–3L). Compliance deadline: Labeling by April 1, 2026; Enforcement by July 1, 2026. Estimated effort spans 43 weeks across Procurement, SAP, Finance (CF), POS, and CPI teams.
*   **Phase Progress:** Technical implementation is live. Digital and Food Services teams are onboarding in Phase 2. Focus has shifted to validating specific logic for Returns, Pre-orders (Staff App/Cart Flow), MP SKU creation, Scan & Go, and Finance flows.
*   **Impact:** Affects ~130 FairPrice stores and 100% of shoppers purchasing regulated beverages post-April 2026.

### Scope & Functional Requirements
*   **Catalogue & Search:** New BCRS SKUs replace old ones in Algolia, Dynamic Yield, and DS Purchase History indices. Mirakl MP integration requires creating BCRS SKUs and syncing to DBP (P0).
*   **Cart/Checkout/Scan & Go:** Deposit added as a separate charge on cart and checkout screens. Excluded from offer limits and Link points. Total deposit displayed; SKU-level breakdown visibility remains under design discussion.
*   **Returns & Refunds:** Deposit amount refunds when the master BCRS SKU is returned (including drops during picking/packing). Logic requires business definition for non-return scenarios and partial multipack refunds (e.g., 1 of 6).
*   **Picker/TMS Apps:** Deposit SKUs excluded from picker view. Partial pick logic ($0.80 vs $1.00) requires immediate business confirmation.
*   **SAP Integration:** Orders posted only in "delivered" state with deposit as a distinct line item. Order State Management remains in OMS (no decoupling).
*   **QC Food:** BCRS deposit inclusion logic for QC food services is currently excluded from scope regarding specific food processing rules.

### Pending Actions & Ownership
1.  **Design Clarifications:** Finalize invoice design, SKU-level breakdown visibility (subtotal vs. separate charge), and "Deposit SKU return" policy for non-returned master SKUs. *Owner: Business/Finance/Digital.*
2.  **Partial Pick Logic:** Confirm calculation logic for partial picks in Picker/TMS apps. *Owner: Digital/Food Services.*
3.  **SAP Validation:** Validate refund/return flow mapping and ensure distinct deposit line items. *Owner: Finance/Prajney Sribhashyam.*

### Key Decisions & Assumptions
*   **Deposit Treatment:** Non-GST, treated as a separate charge; excluded from offer limits and Link points.
*   **SAP Strategy:** Orders passed to SAP only in "delivered" state with deposit as a separate line item. Order State Management remains in OMS.
*   **Success Criteria:** Targeting 100% accuracy in pricing, receipt breakdown, and POS integration by March 2026 to meet NEA labeling deadlines.

### Blockers & Risks
*   **Complexity:** Returns logic for multipacks and partial pick charges requires immediate business definition.
*   **Scope Exclusion:** SAP decoupling excluded; Order State Management stays in OMS.
*   **Impact:** Affects ~130 stores and 100% of shoppers purchasing regulated beverages post-April 2026.

### Linked Issues
*   **Polaris Work Item:** DPD-225
*   **Discovery - Connected:** NEDMT-2334


## [10/57] [OSMOS only] Enable offsite ads integration with Meta on OSMOS
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


## [11/57] Include swimlane name in the ad request for all Omni Home swimlanes
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


## [12/57] Improve event sync to prevent overage
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


## [13/57] FP VIPs encounter verification after S&G purchase for fewer reasons, vs other customers
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


## [14/57] Fix RMN pentest Low and optionally Info issues
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


## [15/57] Capture SAP Material Number into catalogue service for SAP-related downstream usage
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


## [16/57] Setup alerts for Advertima platform
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


## [17/57] Fix RMN pentest medium issues
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


## [18/57] Take over Segment destination functions from OSMOS
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


## [19/57] Clean up archived proposals after PRD release
Source: jira | Key: DPD-590 | Status: TO BE DEFINED (To Do) | Type: Subtask | Priority: High | Assignee: Michael Bui | Reporter: Michael Bui | Due: 2026-04-24 | child: DPD-383 | parent: DPD-383 | Last Updated: 2026-03-20T14:48:32.369189+00:00
**Daily Briefing Summary: DPD-590**

*   **Current Status:** The task is marked as **TO BE DEFINED (To Do)**. No work has commenced.
*   **Ownership & Pending Actions:** **Michael Bui** (Assignee/Reporter) owns the execution of this subtask. Pending actions include identifying and removing archived proposals from the repository to prevent future AI hallucinations.
*   **Decisions Made:** None recorded in the ticket history yet; the scope remains defined by the task title and description intent.
*   **Key Dates & Deadlines:** The due date is set for **2026-04-24**.
*   **Blockers/Context:** This subtask (**DPD-590**) supports the parent initiative **DPD-383** ("Sales posting for BCRS deposit amount"). It carries a **High** priority.


## [20/57] New project setup for BCRS deposit posting job "ntuclink_bcrs-deposit-posting"
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


## [21/57] [RMN] Unblock NTP connection for Advertima devices
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


## [22/57] New SKU Sync Optimisation
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


## [23/57] [CDP] Access Request from Retail Media
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


## [24/57] "Ad" product copy display not consistent at times
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


## [25/57] B2B Solution: Integration work
Source: jira | Key: OMNI-1249 | Status: In Development (In Progress) | Type: Idea | Priority: High | Assignee: Erica Lee | Reporter: Fiona U | blocks: OMNI-1362, OMNI-1362 | discovery---connected: DPD-57 | migration_parent: PAY-7080 | polaris-work-item-link: DPD-682, PAY-7080, DPD-57 | Last Updated: 2026-03-27T21:33:03.967304+00:00
**Issue:** OMNI-1249 (B2B Solution: Integration work)
**Assignee:** Erica Lee | **Reporter:** Fiona U | **Status:** In Development (In Progress/AMBER) | **Priority:** High

### Current State & Impact
The B2B platform launch is currently marked **AMBER** due to critical dependencies. The DSP launched successfully on **26 April 2026** (confirmed by Zi Ying Liow). However, the overall Go-Live remains delayed until **April 2026**, contingent on **WMS Phase 2** readiness. WMS Phase 2 is the primary blocker for B2B finance and sales posting flows, with a confirmed target date of **13 April**.

### Strategic Context & Problem Definition
The initiative addresses fragmented legacy processes where clients must switch to separate stores via the Postal Code Module (PCM) for Donation Drives or Corporate Employee Discounts (CED), reducing engagement. The solution centralizes procurement, credit management, and campaigns into a unified portal.
*   **Goal:** Scale GMV from $16M (2025) to $100M by 2030; reduce manual inquiries by 30%.
*   **Scope:** Includes Account Admins, Parent-Child structures, Donation Drives, and CED to replace fragmented legacy workflows.

### Key Decisions & Architecture
*   **Integration Strategy:** Proceed with **Co-mall** on SAP (Target: 2025-12-09).
*   **Architecture Flow:**
    *   *Phase 1:* DBP routes orders to PFC via SAP; SAP talks to PFC via middleware.
    *   *Phase 2 (Mandatory):* DBP communicates with PFC directly via Middleware, enabling B2B fulfillment and sales posting.
*   **Scope Adjustment:** Increased scope to include BCRS/Co-mall requirements necessitated a new sprint; no callouts from Co-mall are planned for the April timeline.

### Pending Actions & Operational Readiness
*   **WMS Phase 2 Go-Live:** Scheduled for **13 April**. *Owner: WMS Team/Zi Ying Liow.* This remains the primary blocker.
*   **SAP Blueprint:** Pending final review and sign-off with CC and Finance.
*   **UAT & Testing:** SIT Window completed (6 Mar); UAT window planned for 23 March.
*   **Training & Enablement:** Critical training required for Account Management, Finance (credit workflows), Operations (fulfilment SOPs), Marketing (campaigns), and Support (Zendesk/Refunds).

### Business Impact Metrics
*   **GMV Growth:** +25% within 12 months; 75% YoY growth thereafter.
*   **Volume:** Order count increase from 62K to 333K by 2030; Active users from 8.2K to 17K.
*   **AOV:** Projected rise from $257 to $300.

### Critical Dependencies (Amber Status)
1.  **WMS Phase 2 Readiness:** Without the Go-Live on **13 April**, B2B finance/sales posting cannot function.
2.  **System Integration:** Requires alignment across SAP/DBP (catalogue, offers, pricing, invoicing), Segment (analytics), and Zendesk (support).

### Linked Issues & Context
*   **Blocks:** OMNI-1362
*   **Migration Parent:** PAY-7080
*   **Connected Discovery:** DPD-57, DPD-682
*   **Related Work Item:** DPD-682 (Polaris link)

**Key Dates:**
*   **DSP Launch:** Completed 26 April.
*   **WMS Phase 2 Go-Live:** Planned 13 April.
*   **B2B Platform Go-Live:** Contingent on WMS Phase 2; Targeted April 2026.


## [26/57] [Decoupling from SAP] Migrate CF apps to DBP to improve MP Consol fulfilment experience
Source: jira | Key: OMNI-1363 | Status: UAT (In Progress) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Gopalakrishna Dhulipati | polaris-work-item-link: DST-2272, DPD-326, DPD-332, DPD-341, DST-2531, DPD-348 | Last Updated: 2026-03-27T21:33:22.858463+00:00
**Ticket:** OMNI-1363 | **Status:** UAT (In Progress) | **Priority:** High
**Assignee:** Prajney Sribhashyam | **Reporter:** Gopalakrishna Dhulipati
**Linked Issues:** DST-2272, DPD-326, DPD-332, DPD-341, DST-2531, DPD-348

### Current State
The project to migrate CloudFoundry (CF) apps to DBP for MP Consolidate Fulfilment has transitioned from a paused state to **UAT**. Development work is complete. Per the latest program update by Prajney Sribhashyam (March 27, 2026), UAT is confirmed to start next week with a kick-off session scheduled specifically for **Monday, March 30, 2026**, commencing that same week.

### Pending Actions & Ownership
*   **UAT Execution:** Prajney Sribhashyam must oversee the UAT launch and manage the kick-off session on March 30, 2026.
*   **Training Material:** Product and Tech teams are responsible for creating training materials as part of the rollout plan.
*   **Contingency Planning:** A contingency plan is actively being developed to address historical data risks identified during migration.
*   **Change Management:** Operations must ensure zero downtime; deployment will be managed via device updates. Final alignment with PFC and First Mile teams remains critical.

### Key Decisions Made
1.  **UAT Schedule Confirmed:** UAT has been rescheduled for the week of **March 30, 2026** (previously planned for Jan 5–9, 2026). Kick-off set for Monday, March 30.
2.  **Scope & Components:** Strictly limited to Fulfilment apps: First Mile Operations App, First Mile Dashboard, and PFC Receiving App. Pricing components were excluded.
3.  **Deployment Method:** Rollout will be managed by device updates to ensure no disruption to Operations.

### Critical Dates & Blockers
*   **Upcoming Milestones:**
    *   UAT Kick-off: **March 30, 2026** (Monday).
    *   UAT Window: Week of **March 30, 2026**.
    *   *Note:* The original rollout target of Jan 12–16, 2026, has been superseded by the new UAT timeline.
*   **Historical Context:** The initial Jan 5–9 UAT and Jan 12–16 Rollout windows were missed; current focus is on the March 30 execution.
*   **Dependencies:** WMS Middleware remains a historical dependency factor, though immediate focus is DBP/UAT execution.

### Success Criteria & Impact
*   **Cost Reduction:** Annual savings of **$170K** (reducing CF costs from $170K to $0).
*   **Performance:** Improved DOT% for CF sellers and enabling earlier order pushes (4PM on D-1) compared to the previous baseline.
*   **Target Audience:** MP Consolidate Fulfilment Sellers and DPD developers.

### Technical Context
*   **Objective:** Decouple from SAP by migrating CF apps to DBP to resolve enhancement dependencies.
*   **Risk:** Historical data integrity requires a specific contingency plan currently in development.


## [27/57] [Decoupling from SAP] Improve order orchestration with integration to WMS Middleware
Source: jira | Key: OMNI-1362 | Status: Paused (To Do) | Type: Idea | Priority: High | Assignee: Gopalakrishna Dhulipati | Reporter: Gopalakrishna Dhulipati | blocks: OMNI-1249, OMNI-1249 | polaris-work-item-link: DPD-184 | relates: OE-3209 | Last Updated: 2026-03-27T21:33:37.168535+00:00
**Ticket:** OMNI-1362: [Decoupling from SAP] Improve order orchestration with integration to WMS Middleware
**Current Status:** Paused (To Do) | **Type:** Idea | **Assignee/Reporter:** Gopalakrishna Dhulipati | **Priority:** High

### 1. Strategic Context & Problem Definition
Decoupling SAP is a strategic initiative driven by the Finance team's need to resolve GST non-compliance and optimize fulfillment architecture, which currently suffers from high dependency on SAP flows. Integration with WMS Middleware is the critical prerequisite for this change.

### 2. Implementation & Validation Scope
*   **Integration Plan:** DBP will integrate with WMS Middleware, followed by integration between WMS Middleware and TMS.
*   **UAT Scope:** Validation covers DBP-WMS Middleware flows and DBP-TMS flows.
*   **Production Rollout:** Includes DBP-WMS Middleware and WMS-TMS integration.
*   **Current Progress (as of 2026-03-27):**
    *   **B2B:** Currently in UAT.
    *   **B2C:** Pending pitch to leadership; Priority and dates remain pending confirmation.

### 3. Pending Actions & Ownership
*   **Leadership Alignment:** The B2C scope must be pitched to leadership; priority and specific dates are currently pending confirmation.
*   **Success Criteria Definition:** Specific metrics (dimensions and values) defining the current baseline vs. expected outcome remain undefined. This is a mandatory requirement before roadmap prioritization can occur.

### 4. Key Decisions & Context
*   **Strategic Alignment:** The initiative remains an "Idea" with High Priority to address GST compliance and fulfillment architecture.
*   **Validation Status:** Sufficient validation is required prior to prioritizing on the roadmap. While historical SIT completion was noted (Dec 29–30, 2025) with passing results from WM6/SAP teams, the project remains "Paused" pending final validation of requirements and leadership alignment for B2C.
*   **Linked Issues:**
    *   **Blocks:** OMNI-1249
    *   **Relates:** OE-3209
    *   **Polaris Link:** DPD-184

### 5. Success Criteria Requirements
To be prioritized, the following must be defined:
*   **Metrics:** Which dimensions and metrics will improve upon resolution (primary metric to be highlighted).
*   **Baseline & Outcome:** Current baseline vs. expected outcome values and the target timeline for improvement.


## [28/57] Improve seller catalogue compliance to align with FSQ expectations
Source: jira | Key: OMNI-1407 | Status: UAT (In Progress) | Type: Idea | Priority: High | Assignee: Prajney Sribhashyam | Reporter: Prajney Sribhashyam | polaris-work-item-link: DPD-100 | Last Updated: 2026-03-27T21:33:56.328482+00:00
**Jira Ticket Summary: OMNI-1407 – Improve Seller Catalogue Compliance (FSQ Alignment)**

**Current Status:**
The project is currently **In Progress (UAT)**. This **High Priority Idea** is assigned to and reported by **Prajney Sribhashyam**, linked to Polaris work item **DPD-100**. The initiative aims to automate compliance checks for Marketplace SKUs, ensuring buyers can verify certifications (HSA, Safety Mark, Halal, Organic) prior to purchase.

**Goal & Business Impact:**
The objective is to eliminate reliance on missing or offline manual checks by enforcing digital verification of licenses and certificate expiry dates.
*   **Risk:** Current non-compliance poses a high reputation risk and an estimated **$2.5M annual GMV loss** due to the potential de-listing of ~25% of the assortment.
*   **Target:** Achieve 100% compliance with FSQ standards by **December 31**, ensuring all non-compliant SKUs are disabled by this date.

**Technical & Solution Overview:**
The solution enhances **Mirakl** SKU creation forms to enforce mandatory fields for License Code and Expiry Date based on Level 3 (L3) categories.
*   **Fields & Logic:** Mandatory fields (License Code, Expiry Date) will dynamically appear based on L3 category selection (e.g., Safety Mark). The expiry date uses calendar-based selection to prevent format errors. An "exempted with a reason" field is available for non-required cases. Logic retrofits existing certificates (Halal, Organic).
*   **Automation:** A data pipeline extracts license codes and dates. Automated notifications alert sellers ~4 weeks and 1 week prior to expiry. Upon lapse, SKUs automatically disable/hide, with status synced between Mirakl and DBP.
*   **Reapproval Workflow:** When a seller updates an expiring certificate, the SKU status shifts to "pending verification" for reapproval before reactivation. The system supports both single and mass uploads (templates) for new and existing SKUs.

**Pending Actions & Ownership:**
*   **UAT Execution:** Complete User Acceptance Testing currently in progress.
    *   *Owner:* Prajney Sribhashyam.
*   **Data Preparation:** Marketplace teams must source necessary certifications from sellers to upload to Mirakl. A definitive list of compliance requirements per L3 category serves as the source of truth.
    *   *Owner:* Marketplace Team & Category Leads.
*   **Operational Setup:** Establish weekly data extraction processes and configure automated alerts for sellers and Category Managers (CM).
    *   *Owner:* Technical Implementation / Marketplace Team.

**Decisions Made:**
*   **System Logic:** Mandatory fields are dynamic based on L3 category; exemptions require a reason field. All components must be filled before pitching SKUs.
*   **De-listing Deadline:** The December 31 hard target remains for disabling non-compliant SKUs.
*   **Process Shift:** Transition from unreliable offline checks to a digital, automated workflow where Mirakl maintains license/expiry data post-implementation.

**Operational Context:**
The effort is estimated at **Small (30 person-days)**. Current activities focus on creating Mirakl data fields, finalizing extraction logic, and ensuring business teams source compliance data to meet the December milestone. The solution covers specific licenses (HSA, Safety Mark, Vector Control, NEA, IMDA) and certifications (Halal, Organic).


## [29/57] [MP Foundational] Sales Breakdown & Seller Payouts
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


## [30/57] Enhanced Notification Preference Center for Multi-Channel Communication Management
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


## [31/57] [1HD] Phase 2 - Build to enable scaling of 1 hour to 100 stores
Source: jira | Key: OMNI-1425 | Status: Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Rajesh Dobariya | polaris-work-item-link: DPD-627 | Last Updated: 2026-03-27T13:32:56.725003+00:00
**Jira Ticket Summary: OMNI-1425**
**Subject:** [1HD] Phase 2 - Build to enable scaling of 1 hour to 100 stores
**Assignee/Reporter:** Rajesh Dobariya | **Priority:** High | **Status:** To Do (Prioritised)

### Current Status
As of the latest update on **2026-03-27**, no new progress has been reported since the previous check-in. The ticket remains an "Idea" in the "To Do" phase. Per recent guidance, all standard sections (Problem Definition, Goals, Solution Summary, Business Impact, etc.) must be fully populated before pitching. While initial requirements were refined, core fields remain incomplete pending stakeholder input on user segments and volume impact.

### Key Decisions & Scope Definitions
*   **Core Objective:** Eliminate manual order handling and reduce human error to scale 1-hour delivery (1HD) to 100 stores. The initiative will iterate based on findings from the Pilot trial.
*   **Functional Requirements:**
    *   **3PL Integration:** Push order details/location; receive last-mile updates and Proof of Delivery (POD). Vendor apps must display live tracking outside the FPG app.
    *   **Picker App:** Enhancements for real-time new order notifications.
    *   **Store Operations:** Streamline store creation (inventory, assortment, time-slots, capacity) and handle 1HD in Financial Food Service (FFS) stores with specific accounting entries.
*   **User Story (Amendment):** As a shopper, when I complete an order and forget items, I want to amend my order to avoid multiple orders and delivery fees.

### Pending Actions & Ownership
Rajesh Dobariya must finalize the following sections based on stakeholder input before pitching:
*   **Problem Definition:** Identify specific user segments, estimated affected volume (% of total users), current workarounds (e.g., placing new orders), and problem severity.
*   **Business Impact & Metrics:** Define Annual GMV/Cost savings. Set targets for AOV increase ($X to $Y within 6 weeks) and Perfect Order rate improvement (X% to Y% in 3 months).
*   **Operational Logic Clarifications:**
    *   **Trigger Timing:** Clarify if the vendor is notified at order placement or packed status.
    *   **Data Scope:** Confirm required fields (Name, Address, Contact only?).
    *   **Completion Protocol:** Define how/when the vendor app notifies DBP upon completion and records POD.

### Key Dates & Blockers
*   **2026-03-19:** Last recorded status update indicating dependency on external clarity for financial metrics and operational rules.
*   **2026-03-27:** No new updates reported; work remains stalled pending required documentation completion.
*   **Blocker:** Incomplete solution design and undefined 3PL communication protocols prevent accurate effort estimation.
*   **Dependency:** Must resolve questions regarding vendor notification timing, data fields, and completion logic before pitching.

### Technical References & Linked Items
*   **Linked Issue:** DPD-627 (Polaris work item link).
*   **Context:** The initiative relies on an iterative approach based on Pilot trial discoveries.


## [32/57] Integrate personalized gamification challenge with FP app
Source: jira | Key: OMNI-1414 | Status: UAT (In Progress) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: James Huang | polaris-work-item-link: DPD-297 | Last Updated: 2026-03-27T13:33:16.219196+00:00
**Ticket:** OMNI-1414 (Idea) | **Priority:** High | **Assignee:** Rajesh Dobariya | **Reporter:** James Huang
**Linked Issue:** DPD-297
**Current Status:** UAT (In Progress) / Dev Completed

### Current State
Backend and Frontend development for the UntieNot gamification integration is **completed**. The solution integrates a personalized challenge system with the FP app, targeting 1.8M DCC shoppers and marketers. It addresses behavior-based challenges to drive GMV through efficient campaign creation.

**Technical Approach:**
*   **Data Security:** Customer UID must be hashed using SHA256 + salt ('s@veValue!') before passing via URL webview (per Alvin Choo).
*   **Entry Points:** Frontend implementation required across OMNI Homepage, Rewards page, PNW Banner, Popup, Voucher Wallet, and Rewards Tile.
*   **Operational Logic:** All solution components must be fully filled prior to pitching; challenges require relevance to user app/in-store/eDM interactions.

**Effort Estimate:** Total 3 man-weeks (Backend: 1 week, Frontend: 2 weeks).

### Business Impact & Metrics
*   **Financial Goal:** Projected $8M incremental GMV over 8 months. This scales from the 2023 UntieNot pilot ($400K/month baseline with 938K DCC, totaling ~$1.6M) to a target audience of 1.7M–1.8M DCC using category and format challenges for wider adoption.
*   **User Value:** Shoppers seek relevant milestones/rewards based on app, in-store, or eDM interactions; Marketers require efficient tools to launch high-participation campaigns ("do more with less").
*   **Key Metrics:** Challenge participation rate and completion rate (Customer Experience).

### Pending Actions & Ownership
*   **UAT Execution:** Rescheduled to **March 31, 2026**, due to prioritization of "Project Light." Owner: Rajesh Dobariya.
*   **Technical Finalization:** Completed as of Jan 7, 2026; Dev is closed.
*   **Launch Planning:** Business live date remains TBD (targeting April) pending UntieNot feedback and business confirmation. Owners: Rajesh Dobariya/James Huang.

### Key Decisions & Estimates
*   **Solution Strategy:** Contracted UntieNot to run personalized gamification for all 1.8M DCC users; app team support is critical for entry point awareness.
*   **Timeline Shift:** UAT moved from March 27th to **March 31st**. Target Technical Live date adjusted to **April 7, 2026** (providing a 1-week buffer from UAT completion for post-UAT fixes).

### Key Dates & Deadlines
*   **Feb 20, 2026:** Deadline to finalize technical approach (Completed).
*   **Mar 31, 2026:** Rescheduled UAT start.
*   **Apr 7, 2026:** Target Technical Live date.
*   **TBD (April):** Business Live date (contingent on UntieNot feedback and business readiness).

### Blockers & Risks
*   **Business Readiness:** Launch timeline blocked by the "Business side" finalizing go-live dates pending UntieNot issue identification.
*   **Prioritization:** UAT rescheduling indicates resource contention with "Project Light."


## [33/57] Transition from fixed-tenancy to impressions-based banner delivery model
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


## [34/57] [Pilot] - 1 to 1 Personalised vouchers for scan at door 
Source: jira | Key: OMNI-1427 | Status: Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Rajesh Dobariya | Reporter: Rajesh Dobariya | polaris-work-item-link: DPD-824 | Last Updated: 2026-03-27T21:34:13.777566+00:00
**Daily Briefing Summary: OMNI-1427**

**Ticket Overview**
*   **ID:** OMNI-1427 ([Pilot] - 1 to 1 Personalised vouchers for scan at door)
*   **Link:** DPD-824 (Polaris work item)
*   **Status:** Ready for development
*   **Priority:** High
*   **Assignee/Reporter:** Rajesh Dobariya
*   **Issue Type:** Idea

**Current State & Decisions Made**
The initiative is officially "Ready for development" as of March 27th. Key governance and logic updates confirmed during the description phase:
1.  **RMN Governance:** During active RMN campaigns, users eligible based on scan sequence/segmentation receive RMN vouchers exclusively, overriding test/control status. The OMNI team retains sole authority over RMN campaign timing (sequence/priority).
2.  **Segmentation:** Control and Test groups are defined by the CCO team based on specific segments.
3.  **Issuance Logic:** Upon QR scan:
    *   **Test Group:** If qualifying for BAU vouchers AND in the Test group, receives LEAP AI suggestions.
    *   **Control/Non-qualifiers:** Receive standard rule-engine configured vouchers.

**Business Impact & Metrics**
*   **Financial Impact:** Total incremental GMV per monthly campaign confirmed at **$145,762** ($127,650 + $19,012).
*   **Effort:** Estimated development effort is **2 weeks**.

**Operational Planning & Timeline**
*   **Engineering:** Tickets shared with engineers; grooming session scheduled for **March 31st**.
*   **Start Date:** Development expected to commence in the **first week of April**, running in parallel (confirmed by Daryl).
*   **Note:** Additional dates will be populated immediately following the March 31st grooming session.

**Proposed Solution Logic**
The system addresses rule complexity at store/campaign levels to optimize spending and ROI for multiple sponsors while ensuring customer engagement freshness.
*   **As a [user]**, **When** scanning the QR code, **I want** to receive LEAP AI-suggested vouchers (if qualifying for BAU and in the Test group) or standard rule-engine vouchers (Control/Non-qualifiers), **So I can** maintain relevance, freshness, and ROI without manual rule updates.

**Pending Actions & Ownership**
*   **Documentation:** Ensure all pitch components are completed prior to submission: Problem Definition, Goal, Business Plans, Operational Processes, and Metrics Impact.
*   **Methodology Validation:** Confirm calculation assumptions for redemption rates and upspend stretch factors as requested by Rajesh Dobariya.
*   **Planning:** Finalize remaining project dates immediately following the March 31st grooming session.

**Key Dates & Blockers**
*   **Deadlines:** Development start: First week of April. Grooming: March 31st.
*   **Blockers:** None. Ticket is ready for development pending final documentation completeness.


## [35/57] FP Pay experience improvements to support new auto apply voucher at IPOS/KPOS 
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


## [36/57] GST Compliance Phase 2 - Refunds and return
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


## [37/57] AI shopping assistant: An engaging experience for customers to build their shopping cart within seconds
Source: jira | Key: OMNI-1235 | Status: Soft Prioritised (To Do) | Type: Idea | Priority: High | Assignee: Koklin Gan | Reporter: Koklin Gan | polaris-merge-work-item-link: OMNI-1237 | polaris-work-item-link: DPD-293 | Last Updated: 2026-03-27T21:34:37.812433+00:00
**Ticket:** OMNI-1235 (AI shopping assistant: An engaging experience for customers to build their shopping cart within seconds)
**Current Status:** Soft Prioritised (To Do) | **Priority:** High | **Assignee/Reporter:** Koklin Gan
**Linked Issues:** OMNI-1237, DPD-293

### Problem & Vision
*   **Problem:** Current AI reliance on intent-based search and manual scrolling creates friction for users with broad/contextual needs (e.g., "cook a healthy dinner"). High-intent users rely on precise keywords; discovery-mode users browse categories inefficiently. This causes frustration, drop-off, lower Conversion Rates (CR), missed Average Order Value (AOV) opportunities, and increased Customer Support queries regarding findability.
*   **Vision:** Integrate an AI-powered conversational assistant acting as a personal shopping expert to guide users from intent to purchase via natural language interaction.
*   **Success Metrics:** Increased CR by reducing friction; Higher AOV via intelligent up-selling/cross-selling; Enhanced Engagement/Loyalty through personalized experiences.

### Current State & Decisions
*   **Status Update:** The ticket remains "Soft Prioritised" (To Do). It was created on 2025-04-16 by Koklin Gan with High priority and is currently re-evaluated for roadmap inclusion.
*   **Business Planning (Mar 2026):** On 2026-03-27, Vivian Lim Yu Qian confirmed she will formulate necessary business plans to secure prioritization during the week of March 30. This supersedes earlier assumptions regarding a completed discovery phase in Jan 2026.
*   **Scope Constraints (Historical Context):** Previous estimates (Jan 2026) proposed an "lean" scope due to resource constraints:
    *   **Timeline:** 8 weeks total (3 Design, 3 Web/Android Dev, 2 Backend).
    *   **Functionality:** System displays products but **cannot** add items directly to cart; users must navigate to the Product Detail Page (PDP) to purchase.
    *   **Data Limitations:** No conversation history context between sessions.
    *   **Search Optimization:** Must pass Store ID for relevance.
    *   **Platform:** Restricted to Web and Android only (iOS excluded).

### Pending Actions & Ownership
*   **Business Plan Formulation:** Vivian Lim Yu Qian is leading the creation of business plans required to move this ticket from "To Do" to an active roadmap item (Target: Week of 2026-03-30).
*   **Validation Required:** Sufficient validation is a prerequisite for prioritization. While Koklin Gan noted a Trollee meeting on 2025-08-13 (Demo: `ai-agent-fpg.trollee.com/chat`), a finalized PRD linked to current scope must be confirmed alongside data insights or deck references.
*   **Resource Allocation:** Design and engineering resources remain pending the finalization of the business plan.

### Key Dates & History
*   **2025-04-16:** Idea created by Koklin Gan; initially soft prioritized with High priority.
*   **2025-08-05:** Conceptual complexity rated as 3; concerns raised on discoverability.
*   **2025-08-13:** Peter Talbot requested PRD; Trollee meeting held for scoping.
*   **2025-09-30:** Ticket was previously deprioritized to "Next" due to use case delays (Status now superseded by Mar 2026 re-evaluation).
*   **2026-01-13:** Vivian Lim Yu Qian confirmed design availability; Jan 2026 lean scope finalized.
*   **2026-03-27:** Vivian Lim Yu Qian assigned to formulate business plans for prioritization (Week of Mar 30).

### Blockers & Risks
*   **Scope vs. Vision Gap:** The inability to add items directly to cart and lack of conversation context may hinder the original vision of building a cart "within seconds."
*   **Prioritization Dependency:** Progress is blocked pending the business plans required to officially prioritize the ticket for development.
*   **Platform Limitations:** iOS support remains excluded in current estimates.


## [38/57] Enable WhatsApp Marketing Consent at Sign-Up Page and Preference Center to Unlock Better Engagement Opportunities
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


## [39/57] Support the SIT/UAT/Beta/Cut Over for MyInfo and LEAP core system integration
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


## [40/57] Achieve 100% GST compliance for Ecom orders 
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


## [41/57] FPG - Fraud detect and prevention 
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


## [42/57] Mirakl foundational work for scalability
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


## [43/57] [Pre-order] 'Mark as Paid' for In-Store Preorders
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


## [44/57] Optimising Airway Bill Generation Experience for Seller
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


## [45/57] [POC] Enabling PalmPay to allow quick checkout
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


## [46/57] Project Turbo to support new POS version
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


## [47/57] Integrating Tencent's  Biometric Authentication (Palm Pay) solution with FPG App for member verification  
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


## [48/57] Compliance - Improving the Cart calculation logic 
Source: jira | Key: OMNI-1179 | Status: Paused (To Do) | Type: Idea | Priority: High | Assignee: Alvin Choo | Reporter: Alvin Choo | Labels: Foundation | polaris-work-item-link: CART-54 | Last Updated: 2026-03-27T21:35:01.115799+00:00
**Jira Ticket Briefing: OMNI-1179 (Compliance - Improving Cart Calculation Logic)**

**Current Status & State**
*   **Status:** Paused (Category: To Do).
*   **Priority:** High | **Type:** Idea.
*   **Assignee/Reporter:** Alvin Choo.
*   **Labels:** Foundation.
*   **Linked Issue:** CART-54 (Polaris work item).
*   **Context:** Addresses customer frustration regarding pricing, promotion, and tax discrepancies across Online, In-store, Scan & Go, and Marketplace channels. The goal is a unified cart service to support scalability, GST compliance, and accurate order splitting.

**Decisions Made & Scope Alignment**
1.  **Initial Definition (Feb 24, 2025):** Ticket created with detailed problem statements targeting "X%" developer time on investigation, "Z" feature parity gaps, and "A%" marketplace transactions requiring custom calculations. Success metrics established include improved checkout conversion and reduced pricing rule implementation time.
2.  **Scope Reduction:** Aligned with the upcoming app replatform ("Project Light"). Scope strictly limited to:
    *   CRUD of core cart services.
    *   Cart calculation logic only.
3.  **Architecture Assumptions:** Validated that a modular, scalable architecture will enable faster business model expansion (Marketplace, Scan & Go) and reduce technical debt from fragmented patchwork fixes.

**Pending Actions & Ownership**
*   **Steer Co Discussion Required:** Validation is needed at the Steering Committee to confirm if the reduced scope (Core Cart/Calculation) is necessary prior to the replatform, rather than deferring entirely to Project Light.
    *   **Owner:** Alvin Choo / Sathya Murthy Karthik / Rajesh Dobariya.
*   **Data Validation Gap:** Assumptions regarding unified architecture improving consistency and reducing technical debt require further data validation before roadmap prioritization.

**Key Dates & Deadlines**
*   **Feb 24, 2025 (16:53):** Idea creation with detailed problem definition, success criteria, and assumptions established by Alvin Choo.
*   **Mar 24, 2026:** Temporary removal and reinstatement confirmed by Rajesh Dobariya for Steer Co review (Context retained from historical record).

**Blockers & Risks**
*   **Redundancy Risk:** Scope may be superseded by the "Project Light" replatform or order splitting initiatives.
*   **Compliance Urgency:** Manual tax handling and fragmented logic create potential GST compliance risks requiring Steer Co validation.
*   **Board Cleanup:** Ticket movement (remove/add) previously impacted board flow; now stabilized pending decision.

**Technical References & Metrics**
*   **Linked Issue:** CART-54.
*   **Related Epics:** Shoppable grocery in Omni Home, GST project, Replatform (Order splitting), Scan & Go splits, Marketplace scaling.
*   **User Impact:** X% of developer time allocated to cart investigation; Z feature parity gaps across channels; A% of marketplace transactions require custom calculations due to supplier complexities.
*   **Success Metrics:**
    *   *Customer Experience:* Cart-to-checkout price consistency (Baseline: X%, Expected: Y%).
    *   *Conversion:* Reduction in abandonment due to pricing errors (Baseline: X%, Expected: Y%).
    *   *Technical:* Time to implement new pricing rules (Baseline: X weeks, Expected: Y weeks).
    *   *Engagement:* Weekly Active Users (WAU) contribution via improved consistency.

**Problem Definition & Validation**
*   **Customer Pain Points:** Shoppers face inconsistent final prices across platforms (checkout vs. order summary), leading to checkout abandonment.
*   **Engineering Challenges:** Current fragmented system requires manual GST adjustments and custom builds for each business case, increasing maintenance costs. Finance teams currently perform manual GST calculations, raising operational overhead.
*   **Data Insights:** Y% of abandoned carts occur due to perceived pricing discrepancies; competitive benchmarks show unified systems yield higher completion rates.
*   **Assumptions Requiring Validation:** A modular architecture will accelerate expansion (Marketplace, Scan & Go) and reduce technical debt from fragmented patchwork fixes.


## [49/57] [OSMOS only] Integrate fit-for-purpose digital signage with OSMOS for in-store ad activation (merged into another ticket)
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


## [50/57] Available to Promise 1.0 [MVP] - New Time-based Inventory logic
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


## [51/57] Enabling User Consent for customer data
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


## [52/57] ROOH 2.0 - Sourcing and Implementation of best-in-class In-Store Ad booking, management, attribution platform
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


## [53/57] [OSMOS Only] Streamline seller/brand onboarding on OSMOS
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


## [54/57] [1hd] Phase 2 -  Scaling one hour delivery to more stores (TO REMOVE)
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


## [55/57] Blocking of specific postal code from allowing customer to select for delivery address
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


## [56/57] Adhere to alcohol act compliance 
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


## [57/57] Compliance - Display price per piece (unit pricing) for selected products
Source: jira | Key: OMNI-1433 | Status: For Pitching (To Do) | Type: Idea | Priority: High | Assignee: Vivian Lim Yu Qian | Reporter: Vivian Lim Yu Qian | polaris-merge-work-item-link: OMNI-508 | polaris-work-item-link: DPD-818 | Last Updated: 2026-03-27T21:35:17.574945+00:00
**Daily Briefing Summary: OMNI-1433 – Unit Pricing Compliance**

*   **Current Status:** "For Pitching" (Category: To Do). The ticket remains an Idea awaiting pitch approval before development execution.
*   **Owner:** Vivian Lim Yu Qian (Assignee & Reporter).
*   **Priority:** High.
*   **Linked Items:** OMNI-508 (Polaris merge work item link), DPD-818 (Polaris work item link).

**Context & Drivers**
Mandated by the Ministry of Trade and Industry (MTI) and the Competition and Consumer Commission of Singapore (CCCS), this initiative extends Phase 2 of the unit pricing program. Following the September 2025 implementation for brick-and-mortar stores, Phase 2 expands requirements to e-commerce players including Amazon, Redmart, and Pandamart. FPG must deploy unit pricing displays on the FPON web and apps to enable shoppers to easily compare prices across products without manual calculation.

**Scope & Requirements**
*   **Mandated Categories:** Minimum of 47 product categories with standardized units of measurement.
*   **Logic Implementation:** Unit pricing formulas must replicate in-store Electronic Shelf Label (ESL) display logic, utilizing SAP UOM and EA Measure.
*   **Data Scope:** Includes Multi-Pack (MKP) items. Specific handling is required for online-only carton SKUs to amend SAP data.

**Business Impact & Metrics**
*   **Primary Goal:** Regulatory compliance with government mandates; secondary goals include competitive positioning, customer trust, and GMV uplift.
*   **Financial Projection:** Estimated annual GMV impact of $800K, driven by a 1.5% increase in Add-to-Cart (ATC) for multipack items.
    *   *Calculation:* ($60M quarterly OG Revenue × 4 quarters) × 30% purchase chance × 75% affected SKUs × 1.5% ATC uplift.

**Operational Processes & Actions**
*   **Data Cleansing:** Critical prerequisite involving mapping SAP classes to DBP categories to identify the number of affected SKUs and ensuring catalogue data cleanliness.
*   **Seller Operations:** Requires explicit communication with sellers to clean up multipack and carton pack sizes, ensuring consistency with SAP UOM and EA Measure requirements.
*   **Catalogue Management:** Specific focus on amending online-only carton SKU data in SAP.

**Timeline & Blockers**
*   **Deadlines:** No specific due date listed; rollout is driven by government timelines following the September 2025 Phase 1 completion for physical stores.
*   **Blockers:** Data cleanliness and accurate SKU mapping are prerequisites before implementation can proceed.

**Next Steps**
Vivian Lim Yu Qian to advance the item from "For Pitching" status to initiate execution of data mapping (SAP class to DBP categories) and seller communication tasks regarding pack size consistency.
