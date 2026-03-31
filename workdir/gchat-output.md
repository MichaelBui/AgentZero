

## [1/44] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4 | Messages: 4 | Last Activity: 2026-03-31T02:30:38.002000+00:00 | Last Updated: 2026-03-31T02:37:56.703503+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Space Creator; Lead coordinating the briefing.
*   **Daryl Ng, Gopalakrishna Dhulipati, Tiong Siong Tee, Michael Bui, Akash Gupta:** Designated "Project Light Attack and Defence Leads".
*   **Hui Hui Voon:** Owner of the D&T Scope for Project Light Workshop document.
*   **Pauline Pong:** Owner of promotion conflict test case file.
*   **Jacob Yeo:** Edited CDTO Internal RFP requirements file on March 25, 2026.
*   **Sophia:** Contacted by Michael Bui regarding CoMall coordination (March 26).

**Main Topic**
Following the transition to active strategic planning ("Room 2") on March 24, the team is finalizing specific slide preparation within six "Spotlight Topics." While Alvin Choo initiated collaboration on **"RMN"** and **"Payment"** slides on March 24, a new flexibility protocol was established on March 25 allowing leads to attend other meetings (e.g., BCRS) if required. Concurrently, technical direction has shifted toward decoupling from SAP, with consensus that SAP should serve primarily for finance and sales records purposes.

On March 30, the discussion pivoted to data strategy. Alvin Choo proposed a "wild idea" to eliminate data migration entirely by keeping existing servers online and restricting user access to view only historical orders. The objective is to significantly reduce project risk and timeline. This proposal generated significant engagement with three replies recorded by 9:07 AM UTC on March 30.

On **March 31**, the team clarified the schedule for communicating leadership roles. Alvin Choo confirmed that team roles would be shared on **Thursday morning** (March 31 or April 1, depending on local timezone context). Additionally, it was noted that Gopalakrishna Dhulipati will return to active duties soon.

**Pending Actions & Ownership**
*   **Action:** Finalize content for "RMN" and "Payment" slides in the D&T Scope document.
    *   **Ownership:** Alvin Choo (initiated), Hui Hui Voon (Document Owner).
    *   **Status:** In progress; collaboration initiated March 24, ~9:32 AM UTC.
*   **Action:** Share designated team roles with the wider group.
    *   **Ownership:** Alvin Choo.
    *   **Status:** Scheduled for Thursday morning (March 31 query raised at 02:25 UTC; confirmed at 02:30 UTC).
*   **Action:** Review "Promotion Conflict Test Case_05.NOV.20" and summarize the file for Alvin Choo.
    *   **Ownership:** Michael Bui. Access was initially denied to Alvin Choo on March 25, 2:51 AM UTC.
*   **Action:** Review "[CDTO Internal] Project Light Requirements for RFP by MVP Scope.xlsx".
    *   **Ownership:** Gopalakrishna Dhulipati (Owner). Jacob Yeo edited this file on March 25, 2026. Alvin Choo shared the link on March 25, ~3:56 AM UTC for summary.
*   **Action:** Clarify backend API responsibilities with CoMall regarding personalization and orchestration.
    *   **Ownership:** Michael Bui (to note and document).
*   **Action:** Identify the owner managing data indexing to Algolia.
    *   **Ownership:** Daryl Ng raised this query on March 26, ~1:55 AM UTC; team response pending in chat space.
*   **Action:** Finalize the Attack/Defence team composition pending Dennis's confirmation following Alvin Choo's email.
    *   **Ownership:** Alvin Choo.
*   **Action:** Address technical clarifications raised by Tiong Siong Tee regarding Inventory visibility, Corporate Control alignment, and Product management portal structure (FP vs. Sellers).
    *   **Ownership:** Alvin Choo and Gopalakrishna Dhulipati.
*   **New Action:** Evaluate feasibility of the "no data migration" strategy proposed on March 30.
    *   **Ownership:** Team consensus needed; initiated by Alvin Choo (March 30, ~8:55 AM UTC).
*   **Action:** Confirm CoMall contract status and determine timing for creating a dedicated GChat space with CoMall teams.
    *   **Ownership:** Michael Bui (initiated inquiry on March 26); pending confirmation from Alvin Choo or Gopalakrishna Dhulipati regarding "grooming next week" vs. immediate kickoff.

**Decisions Made**
*   **Session Protocol:** Participants are encouraged to listen during live sessions; questions should be raised in the chat space.
*   **Meeting Flexibility:** Leads attending this project may prioritize other critical meetings (e.g., BCRS) if necessary, as confirmed by Alvin Choo on March 25.
*   **Platform Resilience:** Integration testing is a strict technical requirement prioritized from "Day 1."
*   **Governance Structure:** FPG cannot be treated merely as a standard seller due to governance conflicts; distinct data structures or models are required for FP vs. non-governance sellers (Clarified by Gopalakrishna Dhulipati).
*   **System Architecture:** SAP integration should be decoupled from core operational logic; it is designated strictly for finance and sales records purposes (Agreed by Tiong Siong Tee on March 25).
*   **Gamification:** Confirmed not part of the DSP scope.

**Key Dates & Follow-ups**
*   **Slide Collaboration Initiated:** March 24, 2026 (~9:32 AM UTC).
*   **"No Data Migration" Proposal:** March 30, 2026 (~8:55 AM UTC) – Alvin Choo suggested keeping servers up to view existing orders only to reduce risk; 3 replies recorded.
*   **SAP Decoupling Consensus:** March 25, 2026 (1:36 AM UTC).
*   **Meeting Flexibility Policy:** March 25, 2026 (1:31 AM UTC).
*   **RFP File Sharing & Review Request:** March 25, 2026 (~3:56 AM UTC).
*   **Test Case Identification:** March 25, 2026 (~2:46 AM UTC).
*   **Algolia Indexing Query:** March 26, 2026 (~1:55 AM UTC).
*   **CoMall Strategy Inquiry:** March 26, 2026 (14:39 UTC).
*   **Session Start ("Room 2"):** March 24, 2026 (1:02 AM UTC).
*   **Team Roles Communication:** Scheduled for Thursday morning (March 31, ~02:30 UTC); confirmed after Daryl Ng's inquiry at ~02:25 UTC. Gopalakrishna Dhulipati return noted March 31.


## [2/44] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/e4zfXRT2Pnk | Messages: 24 | Last Activity: 2026-03-31T02:30:32.841000+00:00 | Last Updated: 2026-03-31T02:38:20.325512+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Initiator of production testing; managing test data, UAT sheets, and confirming store selection.
*   **Sneha Parab:** Inventory/Store specialist; coordinating SKU enablement, Ops alignment, and defining return workflows.
*   **Andin Eswarlal Rajesh:** Tester; verifying platform compatibility (OG vs. Scango), identifying low-peak windows, and monitoring indexer status.
*   **Wai Ching Chan:** Advisor on risks regarding shut-down stores during production testing.

**Main Topic**
Finalizing the execution plan for BCRS production testing, specifically confirming store selection, defining non-peak testing windows, and resolving technical blockers (SKU indexing and 404 errors).

**Decisions Made & Technical Clarifications**
*   **Store Selection:** Prajney confirmed **Parkway Parade** as the selected location for production testing. This resolves the previous pending decision regarding store selection.
*   **Indexing Behavior:** Sneha clarified that enabling a SKU mid-run may cause it to be skipped in the current cycle, though appearance on the Product Listing Page (PLP) is not guaranteed. The indexer runs hourly at the 30th minute (excluding 2:30 AM and 3:30 AM). If a test starts at 12:00 AM, the last window to revert changes is **1:30 AM**.
*   **System Status:** Andin reported that the system was down ("Is back") around 02:30 AM on March 31 and requested verification from Daryl Ng.

**Decisions Made (Existing & Updated)**
*   **Data Migration:** Prajney moved the "Firefighting BCRS" list to the **"BCRS UAT 2026"** spreadsheet; this remains the source of truth.
*   **Testing Scope:** Only specific SKUs created during the smoke test are currently available for production testing.
*   **Target Date Strategy:** Sneha proposed postponing full testing to **April 1** if compliance risks are too high, but the team is now pivoting to an immediate window on **March 31**.

**Pending Actions & Owners**
*   **Low-Peak Hour Identification:** Prajney explicitly requested clarification on exact non-peak hours during the day from Sneha and Andin. The previous proposal of a late-night window (10:30 PM) is now secondary to defining daytime availability for dual OG/Scango testing.
*   **System Verification:** Andin has flagged a system issue at 02:30 AM; Daryl Ng is requested to verify current stability.
*   **Return Process Definition:** Sneha must still clarify how returns will be handled during the chosen testing window (whether late-night or daytime).
*   **SKU Enablement:** SKUs must be enabled both **in-store and globally** to resolve 404 errors. Sneha to coordinate with the Operations team to finalize this setup.
*   **Whitelist Request:** Prajney (`prajney.sribhashyam@fairpricegroup.sg`) requested whitelisting while business users collect production IDs.

**Key Dates & Deadlines**
*   **March 30, 2026:** Date of conversation and spreadsheet updates.
    *   Prajney confirmed **Parkway Parade** as the test site at 11:01 PM.
    *   Sneha joined an urgent meeting at 06:25.
*   **March 31, 2026 (Active):** 
    *   System downtime noted around 02:30 AM.
    *   Pending confirmation of low-peak hours for testing.
*   **April 1, 2026:** Backup date for full production testing if immediate execution on March 31 is deemed too risky.

**Technical Issues Noted**
*   **404 Errors:** Caused by SKUs not being enabled globally and in-store.
*   **System Stability:** Intermittent outages reported early morning (March 31).
*   **Store Configuration:** Risks remain regarding using live stores for testing; no dummy postal codes exist to mitigate the risk of real customer orders.


## [3/44] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-03-31T02:30:06.805000+00:00 | Last Updated: 2026-03-31T02:38:59.385800+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Update)**
**Date:** March 31, 2026 (Early Shift)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 749

### Key Participants & Roles
*   **System/Tool:** Datadog App (Automated Monitoring)
*   **Notification Channel:** `@hangouts-ShoppingCartNotification`
*   **Ownership Teams:** `dpd-pricing`, `dpd-pricing-cart`.

### Main Topic
Instability persists in `frontend-gateway` and `st-cart-prod`. Following the critical cascade on March 29, activity has extended through late evening (March 30) into early morning (March 31). Failure modes now include **Checkout**, **Cart Update** (`post /api/cart`), **Get Cart** (`get /api/cart`), and expanding latency in **Wish List** operations. The system previously triggered a critical SLO breach at 21:11 UTC on March 30; new alerts indicate continued volatility in Wish List P99/P90 latencies and brief success rate degradation on `post /cart`.

### Incident Timeline & Actions
**Previous Context:**
*   *Extended activity from March 20 through 10:28 UTC.*
*   *March 30, 21:57 UTC:* P2 Error Budget Alert triggered (94.9% consumed).

**New Activity (Late March 30 – Early March 31 UTC)**
*   **23:40–23:42 UTC:** Brief latency spike on `get /api/wish-list/_id` (P90: 1.948s). Recovered to 1.406s.
*   **00:48–01:05 UTC:** Significant latency on `put /api/product/{_id}/wish-list`. P90 peaked at **5.504s** (Trigger), followed by P99 reaching **6.04s**. System recovered to 2.239s within ~17 minutes.
*   **01:16–01:20 UTC:** Recurring oscillation on `get /api/wish-list/_id` (P90 > 1.7s). Triggered twice with values of **1.721s**, recovering to ~1.54s.
*   **01:45–01:55 UTC:** Success rate dip on `st-cart-prod`. `post /cart` availability dropped to **99.702%** (below 99.9% threshold). Recovered to 100.0% within 10 minutes.
*   **02:30 UTC:** Re-trigger of P99 latency on `put /api/product/{_id}/wish-list`. Metric reached **7.164s**.

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** The incident window has extended to March 31, 02:30 UTC. The system continues to experience rapid oscillation in Wish List endpoints and a new success rate breach on the Cart service.
*   **Immediate Action Required:** Prioritize root cause analysis for the `put /api/product/{_id}/wish-list` P99 spike (Event ID: `8567475535227362709`). Investigate the correlation between Wish List latency and the brief 99.7% success rate on `post /cart`.

### Decisions Made
*   **Priority Escalation:** Status remains **"Critical Incident"**. New triggers confirm that error budget depletion risks are accompanied by expanding endpoint volatility (Wish List) and availability drops.
*   **Focus Shift:** Analysis must explicitly correlate the 02:30 UTC P99 spike (7.164s) with the earlier 00:58 UTC event to identify if a persistent resource exhaustion or dependency issue is driving recurring latency in Wish List operations.
*   **Metric Update:** New peak P99 for `put /api/product/{_id}/wish-list` reached **7.164s**. Success rate on `post /cart` briefly dipped to 99.702%.

### Key Dates & Follow-ups
*   **Critical Window:** Extended activity from March 20 through at least March 31, 02:30 UTC.
*   **Follow-up:** Immediate trace correlation for the 00:48–02:30 UTC window to correlate the new `put /api/product/{_id}/wish-list` spikes with the success rate anomaly on `st-cart-prod`.

### References
*   **Active Monitors:** `21245720` (Wish List P90), `21245706` (Wish List Put P90), `21245701` (Wish List Put P99), `22710472` (`st-cart-prod` Success Rate).
*   **SLO Monitor:** `8567154411503835973` (Error Budget Alert).
*   **Service Tags:** `service:frontend-gateway`, `team:dpd-pricing`.


## [4/44] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Messages: 5 | Last Activity: 2026-03-31T02:27:45.320000+00:00 | Last Updated: 2026-03-31T02:39:36.714406+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Key Participants & Roles**
*   **Sneha Parab:** BCRS/Fees/Store Closure Impact Lead.
*   **Akash Gupta:** IMS availability/UAT stock sourcing, B2B SKU sync queries.
*   **Wai Ching Chan:** Order Service Deployment/Slot Logic Validation.
*   **Michael Bui:** BCRS Deposit Logic/SAP Integration/Publisher of PRs.
*   **Daryl Ng:** Backoffice/Order Management/Bug Reporting / Slot Logic validation.
*   **Andin Eswarlal Rajesh:** Frontend (iOS/Android) & BCRS UX queries / Amplitude tracking.
*   **Lester Santiago Soriano:** Backend Services Lead.
*   **Zaw Myo Htet:** Payment/Feature Flagging.
*   **Shiva Kumar Yalagunda Bas:** Slot discrepancy reporting.
*   **Gopalakrishna Dhulipati & Dang Hung Cuong:** Address emoji validation (New assignees).
*   **Nikhil:** Provided context on ad slot configuration to Daryl Ng.
*   **Yangyu Wang:** Tagged regarding split flag issues.

**Main Topics Discussed**
1.  **B2B SKU Sync Clarification:** On Mar 30, Sneha Parab requested clarity on B2B SKU synchronization to WMS and whether a dedicated service exists for this process. Akash Gupta provided the response by 9:20 AM.
2.  **UAT Stock Sourcing Update:** Sneha Parab requested specific SKUs (128373, 13205552, 11974812, 11725029, 10414784, 10467878, 11224253, 10293396, 13180286, 51532) be marked as unlimited stock in UAT to support bulk order testing. Wai Ching Chan is handling the update (Mar 30).
3.  **BCRS Deposit Logic Failure:** On Mar 30, Wai Ching Chan reported a sudden issue where BCRS deposit values are missing during checkout in UAT, affecting order placement. Sundy Yaputra has been flagged to investigate this regression.
4.  **BCRS Epic Closure Urgency:** Sneha Parab continues to push for the closure of the BCRS epic (tickets DPD-637 and DPD-807 remain in "Define" state). Inputs are still required from Akash Gupta, Michael Bui, and Andin Eswarlal Rajesh.
5.  **iOS Address Emoji Blocking Bug:** Wai Ching Chan reported on Mar 26 that customer addresses with emojis on iOS cause order time slot failures (Customer ID: 2022036). Logic validation is required during address add/edit.
6.  **Slot Date Discrepancy:** Shiva Kumar Yalagunda Bas reported a delivery slot mismatch (UI shows 25th, API indicates 23rd). Daryl Ng and Sundy Yaputra are resolving this.
7.  **Omni Home Split Flag Regression:** On Mar 31 at 02:27 UTC, Daryl Ng reported that Omni home swimlanes are failing to follow the split flag, requesting ad slots based on older configurations. Backend default setting updates inadvertently stopped swimlanes from requesting ads entirely. Investigation required regarding configuration logic.

**Pending Actions & Ownership**
*   **Sundy Yaputra:** Investigate the missing BCRS deposit value in UAT checkout causing order placement failures (Reported by Wai Ching Chan, Mar 30).
*   **Wai Ching Chan:** Update specified SKUs to "unlimited stock" in UAT for Sneha Parab's testing needs.
*   **Akash Gupta, Michael Bui, Andin Eswarlal Rajesh:** Provide immediate inputs on the status of BCRS tickets **DPD-637** and **DPD-807** to facilitate epic closure.
*   **Daryl Ng:** Review Michael Bui's PR #7 (`bcrs-deposit-posting`) to suppress deposit posting in the re-delivery journey. Investigate the Omni home split flag issue (reported Mar 31) with Nikhil and Yangyu Wang.
*   **Wai Ching Chan, Gopalakrishna Dhulipati, Dang Hung Cuong:** Validate and implement emoji blocking logic for iOS address entry/editing. Reference Customer ID: 2022036.
*   **Zaw Myo Htet:** Clarify pre-order payment redemption logic; execute UAT testing on offboarded Pinelabs split feature flag.
*   **All Engineers:** Mark all tickets deployed to production as "Status = Done."

**Decisions Made**
*   **BCRS Epic Priority:** Immediate action required to close the BCRS epic; ticket status must be verified for DPD-637 and DPD-807.
*   **UAT Stock Critical:** Specific SKUs identified by Sneha Parab must be set to unlimited stock immediately to enable testing.
*   **Status Protocol:** All engineers must update Jira ticket status to "Done" upon production deployment; pending items must be flagged in the chat thread.
*   **Deposit Logic Fix:** Focus remains on PR #7 review and investigating the UAT regression where deposit values are missing.
*   **Ad Slot Configuration:** The issue regarding split flag adherence for Omni home swimlanes requires immediate resolution to restore ad slot functionality without breaking backend defaults.

**Key Dates & Deadlines**
*   **Mar 30, 2026 (Yesterday):** Sneha Parab requested B2B sync clarity and UAT stock updates; Wai Ching Chan reported BCRS deposit failure in UAT. Responses required from Akash Gupta, Sundy Yaputra, and Wai Ching Chan.
*   **Mar 31, 2026 (Today):** Daryl Ng reported Omni home split flag regression via Nikhil. Sports Hub FFS store closure deadline active.

**Note on Historical Context:** Previous mentions of code review priorities for `layout-service` PR #362 are superseded by the urgent Strudel SDK deployment update (`go-platform-website`). The current focus includes investigating the UAT BCRS deposit regression, updating UAT stock levels, resolving slot date mismatches, closing the BCRS epic via tickets DPD-637 and DPD-807, and debugging the Omni home split flag configuration that prevents ad slot requests.


## [5/44] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 16 | Last Activity: 2026-03-31T02:25:19.610000+00:00 | Last Updated: 2026-03-31T02:40:15.798841+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (Updated March 31, ~02:30 UTC)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
Instability in the `engage-my-persona-api-go` service persists into early morning of **March 31**, extending a cycle observed late on March 30. New latency and error spikes have emerged between **02:00 and 02:25 UTC**, affecting both profile services (`post_/pwl/reverify`, `post_/new-myinfo/confirm`) and scanning features in `lyt-p13n-layout`. While individual alerts resolve quickly, the service remains in a state of intermittent failure.

**Status Summary & Timeline (March 30 Late Evening – March 31 Early Morning)**
*   **Identity API Instability (`engage-my-persona-api-go` / Squad Dynamics):**
    *   *New Activity (02:00–02:25 UTC):* High error rates triggered repeatedly, peaking at **0.109** (02:14). Latency spikes observed on `post_/pwl/reverify` (P99: 3.101s at 02:00) and `post_/new-myinfo/confirm` (P90: 2.346s at 02:08).
    *   *Correlation:* Errors coincided with latency surges on user data verification endpoints before recovering to sub-threshold levels by 02:11–02:25 UTC.
*   **Scanning & Layout Services (`lyt-p13n-layout` / Squad Journey):**
    *   *New Activity (02:00–02:25 UTC):* Latency spikes in `get_/v1/scan-door/nearest` (P99 > 1.8s) and `get_/v1/scan-door/store` (P99: 2.009s at 02:22).
    *   *Availability:* Success rate for `post_/v1/scan-door/scratch-cards/claim` dropped to **98.039%** (< 99.9% threshold) at 02:23 UTC.
*   **Gamification & Recommendation (`frontend-gateway` / Squad Journey):**
    *   *New Activity:* Orchid request success rate dipped to **99.865%** (02:21 UTC). Other services like `boughtbought` recovered by 02:06 UTC.

**Pending Actions & Ownership**
*   **Investigate Early Morning Latency/Errors:** Analyze the correlation between `post_/pwl/reverify` latency spikes (3.1s) and error rate surges in `engage-my-persona-api-go`. Owner: **Squad Dynamics**.
*   **Assess Scanning Service Health:** Investigate success rate drops (<99.9%) for scratch card claims and store page latency in `lyt-p13n-layout`. Owner: **Squad Journey**.
*   **Pattern Continuity Review:** Determine if the 02:00–02:25 UTC window represents a new daily cycle or an extension of the March 30 evening instability. Owner: **Squad Dynamics**, **Squad Journey**.

**Decisions Made**
*   **Severity Escalation:** Incident status remains critical due to sustained cyclical recurrence across three distinct timeframes (Morning/Afternoon Mar 30, Evening Mar 30, Early Morning Mar 31). The failure model now explicitly includes the 02:00–02:25 UTC window.
*   **Cross-Squad Impact:** New latency and availability issues in `lyt-p13n-layout` (Journey) have joined the persistent errors in `engage-my-persona-api-go` (Dynamics), suggesting potential shared dependency or load correlation.

**Key Dates & Follow-ups**
*   **Active Window:** March 28–31 (UTC). Recent critical activity: **02:00 – 02:25 UTC**.
*   **Reference Links (Latest):**
    *   `engage-my-persona-api-go` Error Rate Monitor #92965074 (Latest Trigger: 02:14, Value: 0.109)
    *   `post_/pwl/reverify` Latency Monitor #17447618 (Latest Trigger: 02:00, P99: 3.101s)
    *   `post_/new-myinfo/confirm` Latency Monitor #50879027 (Latest Trigger: 02:08, P90: 2.346s)
    *   `lyt-p13n-layout` Success Rate Monitor #20382861 (Triggered: 02:23, Value: 98.039%)


## [6/44] @ecom-ops #standup - Mar 31
Source: gchat | Group: space/AAQA87ehICk | Messages: 4 | Last Activity: 2026-03-31T02:18:52.052000+00:00 | Last Updated: 2026-03-31T02:40:46.590921+00:00
**Daily Work Briefing: @ecom-ops #standup (Mar 31)**

**Key Participants & Roles**
*   **Sneha Parab:** Lead/Coordinator for the standup session.

**Main Topic/Discussion**
The conversation centered on logistical coordination to initiate the daily standup meeting. Sneha announced a brief delay while concluding an ongoing discussion and subsequently instructed the team to join the online session.

**Pending Actions & Ownership**
*   **Action:** Join the online standup meeting.
    *   **Owner:** All Team Members (Target audience: 5 of 8 viewed).
    *   **Context:** Initiated by Sneha Parab at 02:18:45 UTC.

**Decisions Made**
*   The team agreed to proceed with the standup via an online platform rather than in-person or text-only coordination.

**Key Dates, Deadlines & Follow-ups**
*   **Meeting Date:** March 31, 2026.
*   **Time Reference:** Session commenced/coordinated around 02:17–02:18 UTC.
*   **Specific Reference:** Sneha Parab joined from location/device identifier "L12" at 02:18:52 UTC.

**Summary of Events**
*   **02:17:29:** Sneha requested a few minutes before joining the standup.
*   **02:17:32:** She clarified she was in the middle of a discussion.
*   **02:18:45:** She notified the group to join online.
*   **02:18:52:** She confirmed her availability from "L12."

**Resource Link**
https://chat.google.com/space/AAQA87ehICk


## [7/44] Backend Chapter
Source: gchat | Group: space/AAAAHhDyHI4 | Messages: 1 | Last Activity: 2026-03-31T02:14:10.738000+00:00 | Last Updated: 2026-03-31T02:41:58.893653+00:00
**Daily Work Briefing: Backend Chapter**

**Key Participants & Roles**
*   **Michael Bui:** Investigated GCP PubSub configuration.
*   **Nicholas Tan:** Flagged critical security issues; identified ownership for Service Accounts (SAs).
*   **Lester Santiago Soriano:** Blocked on CI/CD pipeline errors after upgrading Go dependencies.
*   **Boon Seng Ong:** Investigated ESPv2 deployment failures.
*   **Himal Hewagamage:** Identified as the new owner for `fpg-titan-preprod` Service Account Key Rotation and Decommission tasks.

**Main Topics**
1.  **Critical Supply-Chain Security Alert (March 26, Morning):** Nicholas Tan identified a "Trojanization" attack affecting Trivy, Checkmarx, and LiteLLM tools (source: Kaspersky blog).
    *   *Action:* Users with `trivy` CLI version `v0.69.4` must uninstall immediately. Users with `litellm` on local machines are instructed **not** to upgrade.
2.  **CI/CD & Dependency Upgrade (March 12):** Lester Santiago Soriano upgraded `stdlib` to `v1.25.8`. The pipeline failed due to a version mismatch between the project target (Go 1.25.8) and the build agent's `golangci-lint` (compiled with Go 1.24).
    *   *Root Cause:* Requires update to the `dpd-backend-cicd` resource.
3.  **ESPv2 Deployment Failure (March 25):** Boon Seng Ong reported failures in `deploy-esp-image` due to invalid flags for `gcloud beta run deploy` and `update-traffic`. Suspects changes to the "golden pipeline."
4.  **Service Account Security Audit & Rotation (March 16 / March 31):** Nicholas Tan initially flagged JSON keys embedded in SAs (`pong-club-agent`, `vertex-client`) within `fpg-titan-preprod` requiring decomposition. On **March 31, 2026**, the ownership for this specific rotation and decommission task was assigned to **Himal Hewagamage**.
5.  **Cluster Certificate Expiry (March 26, 09:57 UTC):** Nicholas Tan flagged an urgent need to identify the owner of a specific cluster and rotate certificates immediately, warning that failure to do so will cause cluster failure ("go boom boom").

**Pending Actions & Ownership**
*   **Eradicate Compromised CLI Tools:** Immediately uninstall `trivy` v0.69.4 from all laptops; halt upgrades for `litellm`.
    *   *Owner:* **All Team Members**.
*   **Resolve CI/CD Pipeline Block (Go Version):** Update `dpd-backend-cicd` resource to support Go 1.25.8 or align linter version.
    *   *Owner:* **TBD** (Lester Santiago Soriano requested ownership).
*   **Investigate Golden Pipeline Breakage:** Determine changes causing `gcloud beta run deploy` failures for ESPv2.
    *   *Owner:* **Boon Seng Ong**.
*   **Service Account Key Rotation & Decommission:** Decompose identified SAs (`pong-club-agent`, `vertex-client`) in `fpg-titan-preprod`.
    *   *Owner:* **Himal Hewagamage** (Assigned March 31, 2026).
*   **Cluster Certificate Rotation:** Identify cluster owner and rotate certificates immediately to prevent outage.
    *   *Owner:* **TBD** (Nicholas Tan requested help).

**Decisions Made**
*   Pipelines for `infra-gcp-fpg-titan` remain disabled pending the resolution of Trivy CLI risks.
*   The team has been instructed to remove specific compromised tool versions locally; local development environments are now a security priority over CI/CD infrastructure.
*   Ownership of Service Account Key Rotation tasks has been formally assigned to Himal Hewagamage.

**Key Dates & Follow-ups**
*   **March 6, 2026:** Initial PubSub inquiry (Open).
*   **March 12, 2026:** Pipeline failure reported; escalation for CICD ownership required.
*   **March 16, 2026:** Security flag raised regarding `fpg-titan-preprod` SAs.
*   **March 25, 2026:** Critical deployment failure reported; investigation into golden pipeline changes initiated.
*   **March 26, 2026 (Morning):** Supply-chain attack confirmed; immediate local cleanup required.
*   **March 26, 2026 (09:57 UTC):** Urgent cluster certificate rotation identified as critical path item to prevent failure.
*   **March 31, 2026:** Service Account ownership assigned to Himal Hewagamage for rotation and decommissioning.


## [8/44] RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU | Messages: 7 | Last Activity: 2026-03-31T02:10:02.318000+00:00 | Last Updated: 2026-03-31T02:42:47.241700+00:00
**Daily Briefing Summary: RMN Leadership Space (Updated Mar 31)**

**Key Participants & Roles**
*   **Bryan Choong:** Returned from eTail Asia; currently at Thomson Plaza. Prioritizing Q1 case studies, low-sodium project, and sampling solutions. Observed booth congestion. Preparing briefing points for Vipul's lunch with SPH CEO next week.
*   **Vipul:** Meeting SPH CEO for lunch next week to discuss revenue, agreements, and strategic propositions.
*   **Pauline Tan:** Managing LinkedIn content and award repurposing; investigating sampling spend.
*   **Rajiv Kumar Singh:** Coordinating SOAC planning; previously shared DoorDash Ads benchmarks. Also tasked with providing SPH radio insights regarding news broadcasts and customer surveys.
*   **Allen Umali:** Leading SignCloud cleanup; currently on Medical Certificate (MC).
*   **Serene Tan Si Lin:** Sourced THPZ Australia Fair intelligence; liaising on booth specifics.
*   **Emerald:** Assigned to develop a playbook for campaign assets in the app.
*   **Raymond Kam:** Tasked with providing insights on SPH news broadcasts and coordinating customer survey execution.

**Main Topics**
1.  **SPH Strategic Discussion (Next Week):** Bryan Choong is preparing briefing points for Vipul's upcoming lunch with the SPH CEO to address revenue performance, agreement timelines, and potential joint business plans.
2.  **In-Screen Reselling:** Focus on determining 2024/2025 revenue and 2026 YTD figures from SPH. Key discussion points include a previously declined offer, the official end date of the current reseller agreement (post-notice), and readiness to respond to potential Mediacorp-style propositions.
3.  **In-Screen Radio:** Reviewing 2024/2025 revenue and 2026 YTD data. Agenda includes verifying if SPH returned with a growth plan, confirming the October agreement end date, and discussing updates on news broadcasts within stores.
4.  **SPH News Broadcast & Survey:** Raymond Kam to coordinate a joint customer survey with SPH regarding in-store news content.

**Pending Actions & Owners**
*   **SPH Revenue & Data Gathering:** Compile 2024/2025 revenue and 2026 YTD figures for both In-Screen Reselling and Radio. *Owner: Team (Bryan, Rajiv, Raymond).*
*   **Agreement Terms Analysis:** Identify the specific offer declined by SPH in reselling and confirm the official end date of the current agreement. *Owner: Bryan Choong.*
*   **Radio Strategy & Survey:** Verify if a joint business plan was submitted; confirm October agreement expiry; draft response for news broadcast updates; initiate customer survey planning with SPH. *Owner: Rajiv Kumar Singh, Raymond Kam.*
*   **Strategic Positioning:** Prepare a viewpoint for Vipul to counter potential Mediacorp-style propositions and outline any specific asks. *Owner: Bryan Choong.*
*   **Sampling Solution Investigation:** Obtain quotes from Grenadier and other agencies; analyze spend/traffic impact at THPZ. *Owners: Serene Tan Si Lin, Pauline Tan.*
*   **SignCloud Cleanup:** Complete manual removal of legacy screens (Urgent due to MC). *Status: Contact Allen via WhatsApp.*

**Decisions Made**
*   **SPH Engagement:** Proceed with Vipul's meeting; prepare data-driven responses for reselling and radio revenue discussions.
*   **Survey Execution:** Formalize plan to conduct customer survey on news broadcasts in collaboration with SPH.
*   **Sampling Strategy:** Accelerate solution development; verify Grenadier quotes and explore alternatives for THPZ model.

**Key Dates & Deadlines**
*   **Next Week (Apr):** Vipul lunch with SPH CEO.
*   **Oct 2026:** Estimated end date for current In-Screen Radio agreement.
*   **Mar 31:** New briefing request generated; data compilation initiated.
*   **End of March:** Deadline to finalize SOAC targets.
*   **July:** Planned USA fair activation.


## [9/44] @omni-ops #standup - Mar 31
Source: gchat | Group: space/AAQASmCjPX8 | Messages: 1 | Last Activity: 2026-03-31T02:06:29.467000+00:00 | Last Updated: 2026-03-31T02:43:21.927493+00:00
**Daily Work Briefing: @omni-ops #standup**
**Date:** March 31, 2026
**Source:** Google Chat (Resource ID: DPD-385)

**Key Participants & Roles**
*   **Daryl Ng:** Primary contributor; identified the issue/task via a link.
*   **Chee Hoe Leong:** Tagged for attention/action; viewed by 7 others total (5 of 8 participants saw this specific message).

**Main Topic/Discussion**
The conversation centers on a single item: the tracking or review of task **DPD-385**. No verbal discussion, debate, or elaboration occurred in this snapshot. The sole activity was Daryl Ng sharing the link to the Jira ticket (`https://ntuclink.atlassian.net/browse/DPD-385`) and explicitly tagging Chee Hoe Leong.

**Pending Actions & Ownership**
*   **Action:** Review or address task DPD-385.
*   **Owner:** @Chee Hoe Leong (indicated by the direct tag).
*   **Context:** The action is implied as a request for review, status update, or assignment based on the "Viewed by" metric showing high visibility among the team.

**Decisions Made**
No formal decisions were recorded in this specific exchange. The interaction serves as an information dissemination point regarding the existence and location of task DPD-385.

**Key Dates & Deadlines**
*   **Timestamp:** March 31, 2026, at 02:06:29 UTC.
*   **Task Reference:** DPD-385 (NTU CLINK Jira instance).
*   **Follow-up:** Pending response or action from @Chee Hoe Leong; no specific deadline was set in the message body.

**Summary**
The update is a single-point notification regarding task DPD-385. Daryl Ng has flagged this ticket for Chee Hoe Leong. The high visibility (5 of 8 viewers) suggests team awareness, but active engagement from the tagged individual is required to progress.


## [10/44] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/69o051rSqd4 | Messages: 5 | Last Activity: 2026-03-31T01:50:22.202000+00:00 | Last Updated: 2026-03-31T02:43:52.655851+00:00
**Daily Work Briefing: Digital Product Development (Leads Ecom/Omni)**

**Key Participants & Roles**
*   **Daryl Ng:** Initiator; verifying deployment status and tracking pending items.
*   **Sneha Parab:** Technical lead/owner; managing the deployment schedule based on testing outcomes.
*   **Shiva:** Tester; currently validating the specific build (status noted as of yesterday evening).
*   **Alvin Choo:** Team member; coordinating focus for the upcoming deadline regarding BCRS.

**Main Topic**
Discussion centers on the deployment status of a digital product feature and immediate resource allocation for the day, specifically balancing new deployments against an urgent year-end deliverable (BCRS).

**Pending Actions & Ownership**
*   **Deploy Feature:** Pending finalization based on testing results.
    *   **Owner:** Sneha Parab.
    *   **Context:** Deployment is scheduled for today once Shiva's testing concludes successfully.
*   **Address Pending Item:** A second item flagged by Daryl Ng requires attention.
    *   **Owner:** Alvin Choo (acknowledged).

**Decisions Made**
*   **Deployment Timing:** Confirmed that the deployment will occur "today," contingent upon the completion of Shiva's testing (which concluded late yesterday evening).
*   **Daily Focus Priority:** The team decided to fully prioritize BCRS tasks for the remainder of the day, delaying other non-urgent activities.

**Key Dates & Deadlines**
*   **Current Date:** March 31, 2026.
*   **Testing Status:** Shiva was testing until yesterday evening (March 30).
*   **Deployment Window:** Scheduled for March 31, 2026.
*   **Critical Deadline:** Today is the final day for BCRS deliverables.

**Reference Links**
*   Deployment Verification Link: `https://chat.google.com/room/AAQAX9iKYf0/CjKvfZ07Lb4/kIo2WYTccYY?cls=10`


## [11/44] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/kc66iXHBUHA | Messages: 6 | Last Activity: 2026-03-31T01:49:00.428000+00:00 | Last Updated: 2026-03-31T02:44:29.834856+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Initiator of the discussion; proposed a strategic pivot to mitigate project risks.
*   **Tiong Siong Tee:** Technical lead/consultant; raised critical functional queries regarding data scope, business logic, and legacy order structures.
*   **Daryl Ng:** Workshop participant; reinforced the preference for avoiding full migration by citing existing constraints on new app history retention.

**Main Topic/Discussion**
The team discussed a strategy to eliminate full historical data migration for Project Light Attack and Defence to reduce risk and timeline. Alvin Choo proposed retaining the legacy server in an active state, restricting user access to viewing existing orders only. Daryl Ng supported this approach, noting that during a previous workshop, it was established that the new app will only retain **3 months of history**. Consequently, he advocated using this 3-month window as a baseline to avoid migrating older data entirely.

Daryl Ng suggested a UI solution where users see order history with a specific button for "existing orders." However, clarification is required on scope: while historical past purchases might remain in the legacy app, **all open orders must be synced** to the new system. Tiong Siong Tee raised technical edge cases regarding whether "past purchases" exist in a separate dataset outside the standard order list and clarified business rules for refunds on legacy orders within the old application environment.

**Pending Actions & Ownership**
*   **Clarify Data Structure:** Determine if "past purchases" are stored in a separate dataset from current orders to assess feasibility of the read-only view. *(Owner: Unassigned/Team)*
*   **Define Refund Logic:** Establish whether refunds on legacy app orders should be blocked or supported under the proposed no-migration scenario. *(Owner: Unassigned/Team)*
*   **Confirm Sync Scope:** Verify that all "open orders" are identified for migration to the new system, distinguishing them from the 3-month history baseline and older past purchases. *(Owner: Unassigned/Team)*

**Decisions Made**
No final architectural decision was reached. However, a consensus leans toward a hybrid approach:
1.  **Avoid full migration:** Rely on the existing constraint that the new app only holds 3 months of history.
2.  **Legacy Read-Only Mode:** Retain the legacy server for viewing older past purchases and processing specific legacy scenarios.
3.  **Mandatory Sync:** All open orders must be migrated to the new system regardless of the read-only strategy for historical data.

**Key Dates & Follow-ups**
*   **Discussion Date (Original):** March 30, 2026 (08:55 – 09:07 UTC).
*   **Updated Discussion:** March 31, 2026 (01:47 – 01:49 UTC).
*   **Next Steps:** Address the specific questions regarding past purchase data location and refund policies. Confirm that "open orders" are prioritized for migration while older data remains on the legacy server.

**Reference Links**
*   Conversation URL: https://chat.google.com/space/AAQAsFyLso4
*   Message Count: 6


## [12/44] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Messages: 16 | Last Activity: 2026-03-31T01:46:40.122000+00:00 | Last Updated: 2026-03-31T02:45:50.334033+00:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
Production instability in the Mirakl integration persists, extending a streak to **13 days (March 17–29)** with continued incidents into **March 30 and March 31**. While late March 29 saw critical errors on `fni-offer` and `fni-order-create`, a new cluster occurred early morning **March 31** (UTC). The `picklist-pregenerator` latency issue remains unresolved, with alerts triggering across multiple days.

**Incident Summary & Timeline**
*   **Service: `picklist-pregenerator` (Latency Warning) – Late Evening (Mar 29)**
    *   **Trigger:** P2 Warning "taking too long to complete" at **19:01 UTC**. Metric value: **3609.523s** (Monitor ID `20383097`). Confirms sustained degradation from March 27.

*   **Service: `fni-offer` (FairPrice Route) – Late Evening (Mar 29)**
    *   **Trigger:** P2 "Exception Occurred at FairPrice Route" at **21:14:01 UTC**.
    *   **Recovery:** Returned to normal by **21:18:57 UTC** (~5 mins).

*   **Service: `fpon-seller-sap-picklist-reporter` (P1 Incident) – Evening (Mar 27)**
    *   Triggered P1 alert "SAP authentication failed" at **19:12:15 UTC**. Recovered by **19:17:15 UTC**.

*   **Service: `picklist-pregenerator` (Latency Warning) – Late Evening (Mar 30)**
    *   **Trigger:** P2 Warning "taking too long to complete" at **23:01:23 UTC** (UTC+8 context implied by timestamp sequence). Metric value: **3608.92**. Monitor ID `20383097`.

*   **Service: `fni-order-create` (Cluster of Errors) – Early Morning (Mar 31)**
    *   **Trigger Window:** A cluster of P2 alerts began at **01:40:50 UTC**:
        *   "Error while calling APIs" (Monitor ID `17447928`).
        *   "Exception Occurred At Mirakl Route" (Monitor ID `17447918`) triggered at **01:41:39 UTC**.
    *   **Recovery:** Both monitors returned to normal between **01:45:49 UTC** and **01:46:40 UTC**. Duration: ~5 minutes.

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of the March 31 cluster affecting `fni-order-create` (Mirakl Route and API errors).
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Address critical latency in `picklist-pregenerator`. Recurrence of >3,600s execution times was logged on both Mar 29 (3609.523s) and Mar 30 (3608.92), indicating continuous systemic failure requiring immediate review.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Analyze underlying causes for the P1 SAP authentication failure on `fpon-seller-sap-picklist-reporter` (Mar 27) to prevent recurrence.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Summary for Leadership**
Instability in the Mirakl integration has extended beyond the initial 13-day streak (March 17–29) with new activity on **March 30 and March 31**. A significant cluster occurred early morning **March 31 at 01:40:50 UTC**, where `fni-order-create` triggered two distinct P2 alerts covering "Exception Occurred At Mirakl Route" and "Error while calling APIs." All issues resolved by **01:46:40 UTC** within approximately 5 minutes. Concurrently, the `picklist-pregenerator` service continues to exhibit critical latency, with a metric of **3608.92** logged on March 30 following the previous 3609.523s reading, indicating persistent systemic degradation across the `dpd-fulfilment` and `seller-experience` squads that requires urgent engineering review.


## [13/44] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Messages: 2 | Last Activity: 2026-03-31T01:44:43.295000+00:00 | Last Updated: 2026-03-31T02:47:04.013249+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Sneha Parab:** Lead/Manager; coordinating cross-team support, SAP/API integration blockers.
*   **Michael Bui:** Engineering/RMN Architect; identified root cause for the RMN incident and preparing UAT verification.
*   **Alvin Choo:** Leadership; addressing approval workflows for weekend deployments.
*   **Daryl Ng:** Investigating store network ownership and Omni Home data discrepancies. Recently engaged in chat regarding deployment status (March 31, 01:44 UTC).
*   **Gopalakrishna Dhulipati:** On Child Care Leave until Wednesday (April 2). Will reach out individually if assistance is required to rep tasks.
*   **Others Active:** Andin Eswarlal Rajesh, Olivia, Koklin, Zaw, Ravi.

**Main Topics & Updates**
1.  **RMN Incident & Deployment Status:** Michael Bui identified the root cause and implemented a fix. Daryl Ng confirmed active inquiry regarding deployment status on March 31 (01:44 UTC), asking "this is deployed?". Immediate guidance remains required on weekend (Sat/Sun) deployment protocols, requiring an approval request to Hui Hui.
2.  **Search Performance Drop:** Investigation continues regarding the severe 60–70% impression decline since March 18/19. The RMN root cause fix may correlate with these symptoms; release timing remains contingent on this investigation and UAT success.
3.  **Epic Lifecycle Query (DPD-710):** Sneha Parab flagged a technical live date of March 19, 2026, for the Omni ticket. Closure validation awaits Michael Bui's input given Daryl Ng's recent activity on deployment queries.
4.  **SIT Timeline & Redelivery Risk:** Discussion continues on SIT delivery feasibility before April 6/7 contingent on Knowledge Transfer (KT). Adrian remains unavailable for redeliveries between April 1–7 due to duplicate posting risks without a completed handover.
5.  **Infrastructure Compliance:** Bitnami ending free Docker images mandates migration for `sonic_raptor` and `mkp-fairnex`.
6.  **Resource Availability:** Gopalakrishna Dhulipati is currently on Child Care Leave until Wednesday, April 2.

**Pending Actions & Owners**
*   **RMN Deployment Verification:** Confirm if the fix has been deployed following Daryl Ng's inquiry and proceed with UAT verification. Send approval request to Hui Hui for weekend deployment if applicable. (Owner: Michael Bui; Coordination: Alvin Choo/Hui Hui/Daryl Ng)
*   **Epic Closure Validation:** Determine if DPD-710 can be closed given the March 19 live date discrepancy. (Owner: Michael Bui; Requestor: Sneha Parab)
*   **SIT Delivery Assessment:** Evaluate KT feasibility to complete SIT before April 6/7. (Owners: Michael Bui/Daryl Ng)
*   **Store Network Ownership:** Confirm scope under Data COE vs. Miguel's team regarding `Omni Home` store ID mismatch (OMNI-1157). (Owner: Daryl Ng/Michael Bui)
*   **SAP Timeline Resolution:** Resolve deposit SKU data integration blockers. *Note: Gopalakrishna Dhulipati is on leave until Wednesday; individual rep requests will be made if needed.* (Owners: Sneha Parab/Alvin Choo/Gopalakrishna Dhulipati)
*   **RAW Forms Review:** Complete Risk Register review for DPD RAW forms; confirm handovers and renew expired forms by Tomorrow EOD. (Owner: All Leads/Sazali Bin Mohammed Ali's team)

**Decisions Made & Status Changes**
*   **RMN Deployment Inquiry:** Daryl Ng raised a query on March 31 regarding the deployment status of the RMN fix, indicating active monitoring of the release phase.
*   **Release Strategy:** Regular app release status remains pending the search performance investigation and confirmation of the current deployment status (per Daryl Ng's check).
*   **Architecture Updates:** Michael Bui has updated current, future, and transition architecture diagrams.
*   **Staffing Update:** Gopalakrishna Dhulipati is on Child Care Leave until Wednesday; active engagement for task reassignment will be initiated by him directly.

**Key Dates & Deadlines**
*   **RAW Forms Review:** Due Tomorrow EOD.
*   **Gopalakrishna Dhulipati Leave:** Until Wednesday, April 2 (Child Care Leave).
*   **Adrian Redelivery Block:** Unavailable Apr 1–7 due to duplicate posting risks.
*   **SIT Target:** Potential delivery by April 6/7 contingent on KT success.
*   **Chee Hoe Support:** Effective end of March for Product Catalogue/MarTech scope.
*   **DPD-710 Live Date:** March 19, 2026 (Subject to validation).


## [14/44] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Messages: 16 | Last Activity: 2026-03-31T01:05:09.335000+00:00 | Last Updated: 2026-03-31T02:48:17.869590+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Mar 31, 01:10 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`.
*   **Escalations:** `@oncall-dpd-staff-excellence-pdm`, `@hangouts-GT-Search-DatadogAlerts`, `@hangouts-GT-Discovery-DatadogAlerts`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Retail Media.

**Main Topic**
**P3 INCIDENT (RECOVERED):** Intermittent low file count on `sku-store-attribute` job.
*   **Current Status:** Recovered at 01:05 UTC following a triggering event at 00:37 UTC.
*   **Incident Timeline:**
    *   Triggered: Mar 30, 22:09 UTC (Resolved earlier today).
    *   Triggered: Mar 31, 00:37 UTC (Metric < 6 files in last 5h).
    *   Recovered: Mar 31, 01:05 UTC (Metric > 6 files in last 5h).
*   **Monitor ID:** `20382848` | **Query:** `logs("service:fpon-catalogue-job-sku-store-attribute \"processed Files:\"").index("*").rollup("count").last("5h") < 6`.

**Resolved Incidents**
*   **`marketing-service`:** P4 throughput anomaly recovered at 10:53 UTC (Mar 30). Monitor ID `17447110`.
*   **`go-catalogue-service`:** P2 error count recovered at 16:40 UTC (Mar 30). Monitor ID `17447762`.
    *   *Note:* No new activity regarding the long-standing P3 latency alert since Mar 30.

**Pending Actions & Ownership**
*   **Action:** **POST-MORTEM / VERIFICATION (`sku-store-attribute`):** [Status: CLOSED/VERIFIED] The recent P3 alert (Mar 31, 00:37–01:05 UTC) has resolved automatically. No immediate investigation required unless recurrence occurs.
    *   **Owner:** DPD Grocery Discovery Team (`team:dpd-grocery-discovery`).
    *   **Context:** Monitor indicates normal processing (>6 files). Previous manual checks for errors/warnings remain valid historical context.
*   **Action:** **RE-VERIFY `fp-search-indexer`:** [Status: INACTIVE] Re-check status of Monitor ID `17447691` (active since Mar 18) against current Datadog state to confirm resolution.

**Decisions Made**
*   The intermittent low file count issue on `sku-store-attribute` is resolved; no further immediate action required for the alert triggered at 00:37 UTC.
*   Continue monitoring the job for recurrence of the pattern observed between Mar 30, 22:09 and Mar 31, 01:05 UTC.

**Key Dates & Follow-ups (Mar 31, 2026)**
*   **Service: `sku-store-attribute` (P3 - Grocery Discovery) [RECOVERED]**
    *   *Latest Timeline:*
        *   Triggered: Mar 31, 00:37 UTC.
        *   Recovered: Mar 31, 01:05 UTC.
        *   Previous incident resolved earlier today (Mar 30, ~22:10).
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/20382848) | [Job Logs](https://app.datadoghq.eu/logs?query=service%3Afpon-catalogue-job-sku-store-attribute+%22processed+Files%3A%22)
*   **Service: `marketing-service` (P4 - Retail Media) [RESOLVED]**
    *   *Latest Timeline:* Recovered Mar 30, 10:53 UTC.
    *   *Links:* [Datadog](https://app.datadoghq.eu/monitors/17447110) | [K8s](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview) | [Runbook](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book)
*   **Service: `go-catalogue-service` (P2 - Product Data Management) [RESOLVED]**
    *   *Latest Timeline:* Recovered Mar 30, 16:40 UTC.
    *   *Links:* [Datadog](https://app.datadoghq.eu/monitors/17447762) | [K8s](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/go-catalogue-service/overview) | [Runbook](https://ntuc.atlassian.net/wiki/spaces/DIS/pages/2646212686/Catalogue+Service)

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c


## [15/44] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Messages: 2 | Last Activity: 2026-03-31T00:03:09.218000+00:00 | Last Updated: 2026-03-31T02:49:12.843842+00:00
**Daily Work Briefing Summary (Updated: March 31, 2026)**

**Main Topics & Discussions**
1.  **Programmatic Advertising (Advertima/TTD):** Focus remains on validating discrepancies for `advertima_ttd-fixed-price-test-1.5`. Ravi Singh confirmed receipt of raw BURLs; validation was targeted for Monday, March 17th. Yian Koh requested confirmation on deals `advertima_ttd-first-price-test` and `advertima_ttd-fixed-price-test-1`.
2.  **New Deal Setup:** Yasmina Tregan (Advertima) required an end-to-end test setup this week. Wei Phung to share live campaign details; Ravi Singh to execute setup, push to TradeDesk, and map segments before launch.
3.  **BCRS UAT & Finance Integration:** Progress on SAP document numbers, duplicate posting fixes via PubSub "exactly once" policy (PR #1033), and Bukit Timah Plaza pricing/display issues.
4.  **Event Sync Optimization (DPD-645):** Addressing the massive event overage (14M vs. normal 550k). PRD deployment plan set for Sunday, March 15.
5.  **Security & Compliance:** RMN Pentest fixes (DPD-700) deployed to Prod; Bitbucket App Passwords deprecated effective June 9, 2026.

**Status Update: Inbox & Communications**
*   **Inbox Status:** As of March 31, 2026 (00:03 UTC), the workspace inbox is fully caught up across all categories (**Urgent Action Items**, **Thematic Project Updates**, **Meeting Updates**, and **FYI**). No pending unread items require immediate attention. This status follows confirmations from daily summaries dated March 24 through March 30. The latest update from Workspace Studio confirms zero backlog in all sections, including Code Reviews and Project Updates.

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

**Note on New Content:** The daily summary from March 31, 2026, via Workspace Studio confirms the inbox remains clear of urgent action items across all categories, including Thematic Project Updates. No changes to pending actions or decisions were required based on this update; historical context regarding project statuses and deadlines remains valid.


## [16/44] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw | Messages: 2 | Last Activity: 2026-03-30T23:25:30.295000+00:00 | Last Updated: 2026-03-31T02:49:51.137261+00:00
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
1.  **FPPay Production Issue:** On March 30, 2026 (09:11 UTC), Andin Eswarlal Rajesh reported that FPPay banner images are failing to load in production. Activity continues with 25+ replies as of 11 minutes ago.
2.  **Staff Verification Logic:** Vivian Lim Yu Qian queried app screens for staff verification during SKU purchases requiring force verification (e.g., milk powder). The team is validating compliance against existing protocols.
3.  **Incident Management Response:** Earlier on March 27, Jazz Tong raised an urgent query regarding a potential incident ("it is incident?"). The team mobilized support for the DPD Incidents channel involving Gopalakrishna Dhulipati, Akash Gupta, and Kyle Nguyen.
4.  **Infrastructure & Operations Risk:** Nicholas Tan flagged risks regarding Broadcom ending free Bitnami images, causing `kubectl` image tag failures and increased Time To Recovery (TTR) impacting the Golden Pipeline (GP).
5.  **Payment Service Issues:** Alvin Choo reported promo code redemption failures in FP Pay; confirmed that a change freeze has ended and feature releases are proceeding.
6.  **Mobile Quality Assurance:** Andin Eswarlal Rajesh previously identified an iOS FPPay bug where QR codes load without user login, escalated via file download.
7.  **Datadog Governance:** Natalya Kosenko reported unauthorized manual changes to Datadog On-Call teams (removals of Maxine, Arijit, Minu). Terraform manages this config; manual console edits are overwritten on the next run.
8.  **Strategic Planning & Tooling:** Winson Lim highlighted data centers as potential targets in modern warfare (Iran conflict context) to inform Disaster Recovery (DR) scenarios and noted Reforge joined Miro to bridge strategy and delivery gaps.
9.  **AI Engineering Learning:** On March 30, 2026 (23:25 UTC), Winson Lim shared a GitHub repository (`affaan-m/everything-claude-code`) as a resource for learning AI-first engineering patterns and reusable skills.
10. **Social Events:** Kyle Nguyen announced an upcoming DPD BBQ ("We come first"). Boning He and Gopalakrishna Dhulipati shared snacks; Maou Sheng Lee expressed sentiment regarding energy waste on March 18.

**Pending Actions & Owners**
*   **FPPay Image Team (Andin Eswarlal Rajesh, DevOps):** Investigate root cause of banner image loading failures in production and deploy fix. Priority: High.
*   **S&G Verification Team (Vivian Lim Yu Qian, Product/Dev Teams):** Investigate current S&G flows against the WIP verification logic document to confirm if forced staff verification screens exist for restricted SKUs like milk powder. Reference: `https://ntuclink.atlassian.net/wiki/spaces/SE/pages/1995997683/WIP+S+G+Verification+Flow`.
*   **Incident Response Team (Jazz Tong, Akash Gupta, Gopalakrishna Dhulipati, Kyle Nguyen):** Act as support guides for the active DPD Incidents channel; monitor and resolve incoming incident queries.
*   **GP Team (Nicholas Tan / Mohit Niranwal):** Investigate Bitnami image replacement strategy to resolve TTR issues and update Golden Pipeline dependencies.
*   **iOS/Dev Team (Tiong Siong Tee):** Re-verify the previously identified iOS FPPay QR code login bypass bug status.
*   **Datadog Admins:** Anyone who manually altered Datadog Teams must submit a Pull Request to `https://bitbucket.org/ntuclink/fp-datadog-eu` instead of editing the console.

**Decisions Made**
*   No formal change freeze; feature releases are currently active (Alvin Choo).
*   Datadog team configurations must strictly follow Infrastructure as Code (Terraform) protocols; manual overrides are deprecated.
*   Miro's acquisition of Reforge is recognized as a strategic move to bridge product strategy and delivery gaps.
*   **New:** Active incident support protocol established for Jazz Tong, Akash Gupta, Gopalakrishna Dhulipati, and Kyle Nguyen on March 27, 2026.
*   **New:** Winson Lim endorsed the `affaan-m/everything-claude-code` repository as a key resource for AI-first engineering patterns and skill development.

**Key Dates & Follow-ups**
*   **Mar 30, 2026 (23:25 UTC):** Winson Lim shared AI engineering resource repo.
*   **Mar 30, 2026 (09:11 UTC):** Andin Eswarlal Rajesh flagged FPPay banner image loading failure in prod; discussion ongoing (25+ replies).
*   **Mar 27, 2026 (03:03 UTC):** Jazz Tong flagged potential DPD incident; support team mobilized.
*   **Mar 27, 2026 (08:11 AM):** Vivian Lim Yu Qian raised S&G verification flow query; discussion concluded with 12 replies.
*   **Mar 26, 2026:** Winson Lim shared Reforge joining Miro.
*   **Mar 25, 2026:** Natalya Kosenko highlighted DPD alumni participation in a Google AI event.
*   **Mar 18, 2026:** Maou Sheng Lee noted sentiment regarding wasted energy.

**Social Notes**
*   Upcoming DPD BBQ announced by Kyle Nguyen ("We come first, see you!").


## [17/44] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Messages: 2 | Last Activity: 2026-03-30T23:07:07.982000+00:00 | Last Updated: 2026-03-31T02:50:15.582994+00:00
**Daily Work Briefing: Nikhil Grover & Michael Bui (Updated)**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator; coordinating incident fixes and ticket updates for the FE team. Recently escalated unresolved homepage ad issues to Michael Bui during his vacation period.
*   **Michael Bui:** Technical Lead (Engineering); currently on leave (April 6–12) but reached out regarding urgent deployment constraints.

**Main Topics & Technical Clarifications (Mar 28–30)**
1.  **Scope of Video Support & Page Logic:**
    *   Video content restricted to Omni Home and FP Pay; Search/Category pages route to legacy MPS. Ops controls ensure one video per carousel.
2.  **OSMOS Logic & Slot Management:**
    *   `pcnt` limit is currently 10; expansion expected by early April.
    *   `position` field values (-1, 0, 999) are optional for slot uniqueness, not sequencing.
3.  **Critical Incident Update (Mar 30 Night):**
    *   A race condition identified on March 27 remains unresolved regarding homepage ads.
    *   **Symptoms:** Intermittent response showing either 2 ads with old slots or 6 ads with new slots in swim lanes.
    *   **Troubleshooting:** Changing default slots to be identical resulted in ads appearing only in the "past purchase" swim lane.
    *   **Escalation:** Yangyu contacted Michael Bui on March 30 night; Nikhil Grover reiterated the issue is still active and requested urgent review despite Michael's vacation status.

**Decisions Made & Status Updates**
*   **Deployment Readiness:** Delayed pending resolution of the ongoing homepage ad race condition. Michael remains available for urgent evening deployments before his April 6th departure but requires immediate clarity on this specific defect.
*   **Ticket Coordination:** Nikhil confirmed he will update ticket DPD-838 with explicit slot value examples and OSMOS clarifications (scheduled Mar 29) while coordinating with Alvin.

**Pending Actions & Owners**
*   **Incident Resolution (Michael Bui):** Review the intermittent homepage ad issue reported by Yangyu/Nikhil; address slot sequencing failures causing partial renders or incorrect counts.
*   **Incident Fix Details (Nikhil Grover):** Continue tracking deployment ownership for the race condition fix while awaiting Michael's diagnosis.
*   **Ticket Updates (Nikhil Grover):** Proceed with updating DPD-838 with slot value examples and OSMOS logic; coordinate with Alvin.
*   **Monday Confirmation (Nikhil Grover):** Verify timeline for OSMOS `pcnt` limit expansion (>10).

**Key Dates & Deadlines**
*   **March 28, 2026:** Technical scope clarified.
*   **March 30, 2026:** Nikhil inquired about incident ownership; escalated unresolved ad rendering issue to Michael Bui at 23:07 UTC.
*   **April 6–12, 2026:** Michael Bui's leave period (island with limited connectivity).

**Historical Context Note**
The conversation pivoted from parameter gaps to a confirmed technical defect: a race condition identified March 27 preventing `swimlane` and `page_name` rendering. While Nikhil initially cited a $1250/day impact, he clarified this includes the overall drop (excluding S$11.5K lost revenue from advertisers who stopped campaigns on March 17). On Mar 28 afternoon, Michael raised six critical questions regarding video scope, OSMOS logic, and slot sequencing. Nikhil clarified that video is restricted to Omni Home/FP Pay via Ops control, slot values are optional for uniqueness rather than sequencing, and PCNT limits >10 are expected by early April. On March 30, the focus shifted to operationalizing the fix; however, by late night (23:07 UTC), Nikhil reported that despite Yangyu's prior outreach, the issue persists with intermittent rendering of 2 or 6 ads and failed slot sequencing when default slots were aligned. Documentation updates remain scheduled for Mar 29 in coordination with Alvin.


## [18/44] DPD x Platform Engineering
Source: gchat | Group: space/AAQAcjNXKpA | Last Activity: 2026-03-30T20:24:40.092000+00:00 | Last Updated: 2026-03-30T22:37:04.018145+00:00
**Daily Work Briefing: DPD x Platform Engineering**
*(Updated with March 26–30, 2026 High-Urgency Redis Alert & PR Reviews)*

**Key Participants & Roles**
*   **Kyle Nguyen:** Infrastructure/Platform Engineering (Reviewer, Incident Triage, Redis Alert Lead).
*   **Daryl Ng:** Incident Analyst / Automation query responder.
*   **Gopalakrishna Dhulipati:** Addressed in new alert chain.
*   **Sneha Parab:** Addressed in new alert chain.
*   **Alvin Choo:** Team Lead; CC'd on high-urgency Redis alert.
*   *(Other roles from previous briefing remain active).*

**Main Topics & Discussions**
1.  **High-Urgency Redis CPU Spike (March 30):** Kyle Nguyen reported a critical alert at ~03:00 AM UTC regarding the Redis instance `zs-fpon-prd-catalogue-service` in `asia-southeast1`. The instance hit nearly 100% CPU usage.
    *   *Investigation Status:* Verified latency spikes originating from `go-catalogue-service`. Latency has since normalized, preventing escalation to a formal incident.
    *   *Action:* Kyle requested priority investigation for the following day (March 31) with specific focus on root cause analysis for CPU saturation.
    *   *Participants:* Alert chain included Daryl Ng, Gopalakrishna Dhulipati, Sneha Parab, and Alvin Choo.

2.  **Critical Picking App & Backoffice Incident (March 23):** [Historical Context Retained] Sampada Shukla reported `SocketTimeoutExceptions` on Android and `Connection Resets` on Web between 03:40–03:45 PM SGT. Root cause identified as GKE cluster (`jarvis-prod-ap-v2`) hard memory limits triggering forced pod evictions at 15:22–15:39 SGT.

3.  **SLO Performance Degradation (March 25):** [Historical Context Retained] Dodla Gopi Krishna notified of error budget depletion in Fulfillment and Pricing tribes. Akash Gupta acknowledged alerts requiring attention.

4.  **On-Call Restructuring & Security:** [Historical Context Retained] Debate continues on shifting on-call configuration from Terraform to Datadog UI (Akash Gupta proposal). Lester Soriano encountered `golangci-lint` version mismatch during vulnerability patching for `lt-strudel-api-go`.

**Pending Actions & Owners**
*   **Investigate Redis CPU Saturation:** Prioritize root cause analysis for `zs-fpon-prd-catalogue-service` hitting 100% CPU on March 30. *(Owners: Daryl Ng, Gopalakrishna Dhulipati, Sneha Parab)*
*   **Resolve Cluster Capacity Scaling:** Investigate why the cluster failed to scale out during peak traffic (March 23) and implement fixes for memory limits. *(Owners: Kyle Nguyen, Nicholas Tan)*
*   **Investigate SLO Degradation:** Address error budget consumption in Fulfillment and Pricing tribes. *(Owner: Dodla Gopi Krishna, relevant service owners)*
*   **Evaluate On-Call Tooling Strategy:** Assess Akash Gupta's proposal to use Datadog UI instead of Terraform for new on-call teams. *(Owner: Platform Engineering)*
*   **Restore Bastion Access:** Investigate PROD `asia-southeast1-c` Bastion inaccessibility. *(Owners: Nicholas Tan, Kyle Nguyen, Harry Akbar Ali Munir)*
*   **Review Infrastructure & Monitoring PRs:** Natalya Kosenko's PR `infra-gcp-fpg-titan/344` and Akash Gupta's PR #917 require reviews from Kyle, Nicholas, Madhawa, and Dodla Gopi Krishna.
*   **Resolve Go Pipeline Error:** Reconcile `golangci-lint` version mismatch for Lester Soriano.

**Decisions Made**
*   *Tentative:* The team is debating whether to retain the Terraform-based change-freeze process or adopt direct Datadog UI management for on-call teams. No final decision recorded yet.
*   **QC Food Status:** Disabling confirmed on production (as of March 19). Resource scale-down planning initiated pending ES confirmation.

**Key Dates & Follow-ups**
*   **March 30, ~03:00 AM UTC:** High-urgency alert triggered for Redis instance `zs-fpon-prd-catalogue-service` CPU usage; latency spike verified from `go-catalogue-service`.
*   **March 30, 20:24 PM UTC (Local):** Kyle Nguyen issued priority investigation request citing the Redis incident.
*   **March 25, 03:15 AM UTC:** Fulfillment SLO degradation alert.
*   **March 23, 03:40–03:45 PM SGT:** Critical incident involving GKE memory exhaustion and pod evictions.


## [19/44] Yangyu Wang
Source: gchat | Group: dm/4Ut7xcAAAAE | Last Activity: 2026-03-30T13:42:38.232000+00:00 | Last Updated: 2026-03-30T22:37:31.073449+00:00
**Daily Work Briefing: Layout Service Deployment (PR #362) & Slot Issue Investigation**

**Key Participants & Roles**
*   **Yangyu Wang:** Initiator/Deployer. Investigated slot issues, deployed PR #362 for default slot testing, and executed a rollback due to adverse effects.
*   **Michael Bui:** Approver/Monitor. Validated safety initially; later assisted in clarifying the customer impact of the slot issue.

**Main Topic**
Initial discussion regarding the safety and scheduling of `layout-service` PR #362 (March 24), followed by a follow-up investigation on March 30 concerning ads slots sent to OSMOS appearing as incorrect values (2 or 6 instead of default 1, 3). The deployment intended to test updated default slots but resulted in swimlanes no longer taking ads.

**Decisions Made & Outcomes**
*   **Deployment Approval:** Michael Bui approved the initial `layout-service` deployment on March 24 as safe after clarifying it was distinct from a prior `website-service` error.
*   **Investigation Scope Clarified:** It was confirmed that the slot issue is separate from broken banner images (which relate to orchestrator and payment issues) and that the Marketing service PR addresses Nikhil's separate concern.
*   **Rollback Decision:** Following deployment on March 30, Yangyu observed that most swimlanes stopped taking ads. Consequently, a rollback was executed immediately after reporting the failure at 13:42 UTC.

**Actions & Ownership**
*   **Completed Actions:**
    *   **Deployment (March 24):** Executed by Yangyu Wang at 06:36:12 UTC; acknowledged by Michael Bui.
    *   **Investigation & Rollback (March 30):** Yangyu deployed the default slot update to test a fix for OSMOS slot misalignment, determined it failed ("Doesnt seems to work"), and initiated a rollback.
*   **Pending Actions:**
    *   **Verification:** Nikhil is expected to verify if the temporary resolution holds upon his return (March 30, ~17:46 UTC).
    *   **Support Request:** Yangyu requested Michael Bui's assistance in investigating the issue after the rollback.

**Key Dates, Deadlines & Timeline**
*   **2026-03-24 | 06:36 UTC:** Initial `layout-service` PR #362 deployment confirmed successful.
*   **2026-03-30 | 11:08 AM:** Michael Bui inquires about the specific issue behind Yangyu's PR regarding default slots.
*   **2026-03-30 | 11:10 AM:** Yangyu explains ads sent to OSMOS show values of 2 or 6 (from split) instead of defaults 1, 3, potentially due to a bug. Nikhil suggested updating the default slot for testing.
*   **2026-03-30 | 11:15 AM:** Yangyu clarifies that broken banner images discussed previously are related to orchestrator/payment issues, not this PR.
*   **2026-03-30 | 11:17 AM:** Yangyu confirms deployment; Nikhil pending verification upon returning home.
*   **2026-03-30 | 01:42 PM (UTC):** Yangyu reports the change failed; most swimlanes no longer take ads.
*   **2026-03-30 | ~01:43 PM:** Yangyu executes rollback and requests Michael's help to investigate further.

**Summary of Event Flow**
On March 24, 2026, the initial deployment of `layout-service` PR #362 was successfully executed after clarifying it targeted a different service than previously discussed. However, on March 30, Yangyu initiated a follow-up deployment to address an issue where ads slots sent to OSMOS were incorrectly displaying as 2 or 6 instead of the default 1 or 3, per Nikhil's suggestion. While clarifying that broken banner images were unrelated (stemming from orchestrator/payment issues), Yangyu deployed the change at ~11:17 AM UTC. By 01:42 PM UTC, it was determined the update failed, causing swimlanes to stop accepting ads. Yangyu immediately rolled back the changes and requested Michael Bui's assistance in troubleshooting the incident while Nikhil prepares to verify the situation later that afternoon.


## [20/44] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw/o99Edo1Fa-E | Last Activity: 2026-03-30T11:25:58.368000+00:00 | Last Updated: 2026-03-30T22:38:28.409668+00:00
**Daily Work Briefing: Digital Product Development (FPPay)**

**Key Participants & Roles**
*   **Andin Eswarlal Rajesh:** Issue Reporter (Frontend/Mobile).
*   **Tiong Siong Tee:** Lead Investigator/Coordinator.
*   **Jeet Gandhi:** Backend Engineer (Osmos API).
*   **Nikhil Grover:** Stakeholder confirming production timeline; currently on leave.
*   **Michael Bui:** Key Owner (Orchestrator); unavailable due to reservist duties.
*   **Daryl Ng, Alvin Choo, Yangyu Wang:** Backup engineers assisting with investigation.
*   **Raymond:** End-user reporter (mentioned).

**Main Topic**
Investigation and resolution of a production incident where FPPay promotional banners failed to load on iOS devices for five days. The issue was traced to an empty data response (`"groups": []`) from the Osmos API following a recent orchestrator deployment.

**Decisions Made**
*   **Root Cause Identified:** A deployment in the "orchestrator" service 5 days ago caused the API to return success status but with no banner groups.
*   **Resolution Action:** Yangyu Wang initiated an immediate rollback of the orchestrator deployment at 10:13 AM.
*   **Validation:** Tiong Siong Tee confirmed the banners were restored ("its back") at 10:25 AM.

**Pending Actions & Owners**
| Action Item | Owner | Status/Notes |
| :--- | :--- | :--- |
| **Post-incident analysis:** Investigate root cause of the orchestrator deployment failure. | Yangyu Wang | Will analyze after rollback; initial investigation concluded. |
| **Datadog Check:** Review error logs for the specific feed URL to confirm post-fix stability. | Alvin Choo / Yangyu Wang | Status: **Completed**. Alvin Choo acknowledged completion (11:25 AM). |
| **Process Improvement:** Implement a quick banner verification step immediately following future orchestrator deployments. | Team (Proposed by Tiong Siong Tee) | Pending agreement/implementation. |

**Key Dates & References**
*   **Date of Incident Start:** Approx. March 25, 2026 (Reported as "last 5 days").
*   **Current Date of Briefing:** March 30, 2026.
*   **Critical Timestamps:**
    *   09:11 AM: Issue reported by Andin Eswarlal Rajesh.
    *   09:37 AM: Jeet Gandhi confirmed empty API response (`groups: []`).
    *   10:13 AM: Yangyu Wang initiated rollback.
    *   10:25 AM: Service restored.
    *   **11:25 AM:** Alvin Choo acknowledged completion of monitoring tasks ("thank").
*   **Specific Technical References:**
    *   **Feature Flag:** `pmt_linkpay_osmos_banner` (Suggested for disabling by Tiong Siong Tee).
    *   **API Endpoint:** `https://website-api.omni.fairprice.com.sg/api/v1/feed/create`.
    *   **Page ID:** `fppay_receipt`.
*   **Unavailable Personnel:** Michael Bui and Nikhil Grover are currently on leave/reservist duties.


## [21/44] [BCRS]-SAP to POS & DBP Interface Deployment
Source: gchat | Group: space/AAQAeMC3qBk | Last Activity: 2026-03-30T11:22:50.407000+00:00 | Last Updated: 2026-03-30T22:38:53.544232+00:00
**Daily Work Briefing: [BCRS]-SAP to POS & DBP Interface Deployment**

**Key Participants & Roles**
*   **Onkar Bamane:** Deployment Lead/Coordinator.
*   **Michael Bui:** Deployer (Production OData/SAP).
*   **Hendry Tionardi:** Technical Advisor.
*   **Prajney Sribhashyam:** Process Owner/Test Coordinator (Lead on DBP Testing).
*   **Daryl Ng:** Technical Advisor/Approver.
*   **Anthony Vaz:** Technical Contributor.
*   **Suwandi Cahyadi:** Recipient of API clarification inquiry.
*   **Others:** Sneha Parab, Wai Ching Chan, Olivia, Kandasamy Magesh.

**Main Topic**
Transition from production deployment execution to post-deployment validation and testing. While the initial deployment was successful on March 26, 2026, active focus has shifted to validating DBP functionality in Production and clarifying API call behaviors for Lite POS & Umanned.

**Decisions Made & Status Update**
1.  **Deployment Execution:** Confirmed that **DBP deployment proceeded first**, followed by SAP OData, as originally planned. Michael Bui successfully deployed to Production (PRD) on March 26, 2026.
2.  **New Testing Phase Initiated:** A dedicated thread titled **"DBP Production Testing"** has been established and is currently active.
    *   Status: The thread contains 3 replies with 3 unread messages as of the last check (approx. 11 minutes ago).
    *   Owner: Prajney Sribhashyam is leading this specific validation effort.
3.  **Risk Mitigation:** The initial validation that deploying DBP first poses no risk regarding BCRS deposit error logs remains valid during this testing phase.
4.  **API Clarification (ZUD_DOWNLOAD):** A query was raised on March 30, 2026, by Anthony Vaz regarding the `ZUD_DOWNLOAD` interface for Lite POS & Umanned. The question confirmed whether internal calls are limited strictly to **PLU and Promotion APIs**, excluding **LB** (likely Loyalty Balance or similar).
    *   *Status:* Awaiting confirmation from Suwandi Cahyadi.

**Pending Actions & Ownership**
*   **API Clarification Response:** Provide definitive confirmation on `ZUD_DOWNLOAD` API calls (specifically regarding the exclusion of LB) to Anthony Vaz and acknowledge Suwandi Cahyadi's input. *(Owner: Technical Team / Suwandi Cahyadi)*
*   **Reply Timing:** Acknowledge that replies regarding the API clarification may be deferred until tomorrow during working hours if immediate confirmation is unavailable. *(Owner: Anthony Vaz/Suwandi Cahyadi)*
*   **DBP Production Validation:** Monitor the "DBP Production Testing" thread for test results and anomalies. *(Owner: Prajney Sribhashyam)*
*   **Update Deployment Steps:** Team members must continue adding specific deployment steps to the shared spreadsheet. *(Owner: Michael Bui, Sneha Parab)*
    *   *Specific Note:* Sneha Parab is requested to update steps specifically regarding **MP Article creation**.
*   **Add Missing PICs:** Identify and add any missing Persons In Charge (PICs) not currently listed in the coordination group. *(Owner: Sneha Parab, Prajney Sribhashyam)*
*   **Redelivery Status:** Discuss the latest status on "redelivery" separately in the working group meeting; do not discuss in this chat. *(Owner: Prajney Sribhashyam)*

**Key Dates & Deadlines**
*   **Deployment Window:** Friday, March 26, 2026 (Completed).
*   **API Inquiry Date:** Sunday, March 30, 2026 (In Progress).
*   **Expected Reply:** Tomorrow during working hours.

**References**
*   **Thread: DBP Production Testing:** https://chat.google.com/space/AAQAeMC3qBk (Accessed within the chat space)
*   **Deployment Plan/Tracker (SAP-DBP Deployment Plan):** https://docs.google.com/spreadsheets/d/1gvCjdXWB2BeWr7XgBQs0-zKeLxGi3OmX4ZrbY6pNMeQ/edit?gid=1022676232#gid=1022676232
*   **Chat Space:** https://chat.google.com/space/AAQAeMC3qBk


## [22/44] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/s5qex98NRD8 | Last Activity: 2026-03-30T11:02:33.403000+00:00 | Last Updated: 2026-03-30T22:39:14.429959+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Project Lead/Coordinator (provided SKU references, managed deployment constraints).
*   **De Wei Tey:** E-Commerce Refund Owner (inquired about testing SKUs and postal codes; clarified Help Centre integration details).
*   **Dany Jacob:** Scan & Go Refund Owner.
*   **Tiong Siong Tee:** QA/Testing Lead.
*   **Sathya Murthy Karthik:** Edited the "BCRS UAT 2026" file referenced during the discussion.

**Main Topic**
Coordination of final sign-offs and production deployment for critical refund features, specifically addressing testing constraints regarding BCRS SKUs and Help Centre enhancements required for the April 1st launch.

**Decisions Made**
*   **Deployment Status:** BCRS refund changes were successfully deployed to production by Dany Jacob on March 30, 2026 (09:06).
*   **Testing Strategy Adjustment:** Due to restricted production testing environments where orders cannot be completed, Prajney Sribhashyam recommended finding an alternative method to unblock deployment validation rather than attempting live refund tests immediately.
*   **Help Centre Integration:** De Wei Tey confirmed that Help Centre enhancements are complete; the external consultant successfully integrated BCRS data into the Zendesk app, allowing CS agents to view detailed order info (items, qty, prices, SKUs) without accessing DBP.

**Pending Actions**
*   **De Wei Tey:** Must identify a viable method for testing refunds given that production ordering is restricted. Prajney noted it is impossible to test full refund flows if orders cannot be placed; the team aims to attempt this tomorrow morning (March 31) if access opens.
*   **Tiong Siong Tee:** Requires resolution on ticket **CORE-384**, a pending issue from last Friday's testing cycle regarding the refund flow.

**Key Dates & Deadlines**
*   **April 1, 2026:** Critical deadline for feature availability.
*   **March 30, 2026 (10:39):** Prajney confirmed SKUs are available on the "Production Test Planning" tab of the BCRS UAT spreadsheet.
*   **March 30, 2026 (10:52-10:54):** Prajney clarified that specific features/permissions were not yet enabled for testing and suggested deferring attempts to the following morning.

**Summary of Conversation Flow**
Prajney Sribhashyam initiated the session confirming sign-offs for E-Commerce and Scan & Go refunds are secured for the April 1 deadline. When De Wei Tey requested BCRS SKUs for Singapore (SNG) and OG testing, Prajney directed them to the "Production Test Planning" tab in the shared spreadsheet but immediately noted that production ordering was restricted ("We can try it tomorrow morning").

De Wei Tey asked for specific postal codes, prompting Prajney to reiterate that features were not enabled yet. The discussion shifted to deployment constraints: Prajney highlighted the inability to place orders for refund testing and requested details on the release process. De Wei Tey clarified that the Help Centre enhancement (completed by an external consultant) now allows CS agents to view BCRS data via Zendesk, eliminating the need for DBP lookups, but confirmed that placing and refunding an order is still technically required for validation. Prajney concluded by advising a search for alternative unblocking methods due to these strict production limitations.


## [23/44] QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs | Last Activity: 2026-03-30T09:55:41.924000+00:00 | Last Updated: 2026-03-30T10:45:49.561642+00:00
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
*   **Aman Saxena:** Responding to MiniGames issue.
*   **Others:** Piraba Nagkeeran, Andin Eswarlal Rajesh, Kadar Sharif.

**Main Topics & Discussion**
1.  **System-Wide Intermittent Failures (Critical/New):** On **30 Mar**, Milind Badame reported frequent intermittent errors (HTTP 500: "Some unexpected error has occurred") affecting order placement, cart, and PDP pages. *Status:* Active investigation for potential testing impact or backend instability.
2.  **Order Placement Failure ('Strong Tasty Brew'):** On **30 Mar**, Madhuri Nalamothu reported inability to place orders for non-FP product 'Strong Tasty Brew'. Discussion ongoing with @Piraba Nagkeeran.
3.  **Cart Navigation Errors:** On **30 Mar**, intermittent errors observed when navigating to the cart, confirmed by Milind and Madhuri. *Status:* Investigating root cause alongside system-wide issues.
4.  **MiniGames Blank Screen (New):** On **30 Mar**, Milind Badame reported a blank white screen when tapping the MiniGames tile as a guest user followed by login. Observed on lower Android versions. *Owner:* @Aman Saxena, Mobile Team. *(Note: Supersedes previous "Android OTP" report for this specific symptom).*
5.  **DC Membership Subscription Issue:** On **30 Mar**, Madhuri Nalamothu confirmed subscription failures impact **both new and existing users**. Previously logged as a logic discrepancy; now confirmed active failure. *Owner:* @Kadar Sharif.
6.  **LinkPoints Regression Failure:** Reported on **27 Mar** regarding CLS Award Balance API `500` errors ("Transaction posting failed"). Status remains Critical/Blocked pending resolution with @Pandi.
7.  **Express Cart Service Fee Waiver:** Reported **26 Mar**; service fees incorrectly waived in Express mode. *Owners:* @Daryl Ng, @Andin Eswarlal Rajesh.
8.  **Search Indexing Failure:** "Ninben Tsuyu No Moto Seasoning Soy Sauce" invisible at Hyper Changi despite stock. *Status:* Urgent investigation with @Daryl Ng, @Yangyu Wang.
9.  **Automation Query (DPD-618):** On **30 Mar**, Milind Badame raised a logic concern regarding BackOffice domain management: currently only "disable" exists; E2E tests would cause list bloat without a delete API option. *Owner:* @Daryl Ng.
10. **Other Active Items:** iOS SnG Flow QR loading stuck (Madhuri, 27 Mar); OmniHome Christmas tiles anomaly; Cart Page Logic Flaw allowing ineligible orders (Komal, 20 Mar).

**Pending Actions & Ownership**
*   **System Stability Investigation:** Identify cause of widespread HTTP 500 errors on PDP/Cart/Order Placement. *Owner:* Dev Team / @Hang Chawin Tan. **(Highest Priority)**
*   **MiniGames Crash Fix:** Resolve blank screen issue on MiniGames tile for guest users/login flow on lower Android versions. *Owner:* @Aman Saxena.
*   **'Strong Tasty Brew' Order Failure:** Investigate why non-FP products fail to place orders. *Owner:* Dev Team / QA.
*   **DC Membership Fix:** Resolve subscription failures impacting all user segments. *Owner:* @Kadar Sharif. **(Critical)**
*   **LinkPoints API Resolution:** Address CLS Award Balance API `500` errors. *Owner:* @Pandi.
*   **Automation Logic (DPD-618):** Determine if a delete API or alternative method is required for domain management in E2E tests to prevent list bloat. *Owner:* @Daryl Ng.
*   **Express Cart & Search:** Resolve service fee waiver and search indexing failures. *Owners:* @Daryl Ng, Team leads.

**Decisions Made**
*   System-wide errors on 30 Mar require immediate triage; potential testing activity suspected by Milind Badame but not yet confirmed as the root cause.
*   DC Membership issue escalated to @Kadar Sharif due to scope affecting existing users.
*   MiniGames blank screen investigation assigned to @Aman Saxena, replacing previous attribution for this specific symptom.

**Key Dates & Deadlines**
*   **30 Mar (Morning):** System-wide 500 errors, Cart issues, and 'Strong Tasty Brew' failure reported.
*   **30 Mar (Afternoon):** MiniGames blank screen reported; DPD-618 automation query raised; DC membership issue confirmed for existing users.
*   **27 Mar:** LinkPoints API failure and iOS SnG Flow loading stuck.
*   **26 Mar:** Express cart service fee discrepancy.
*   **25 Mar:** OmniHome tiles, Search indexing, PreOrder tile flagged.
*   **24 Mar:** E-Voucher error.
*   **20 Mar:** Critical Express delivery logic bug flagged.


## [24/44] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/2L6h0-TbEpY | Last Activity: 2026-03-30T09:24:45.442000+00:00 | Last Updated: 2026-03-30T10:46:34.956301+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Shiva Kumar Yalagunda Bas:** Raised initial concern regarding missing linkages; subsequently identified the root cause of the outage.
*   **Chee Hoe Leong:** Tagged by Shiva to investigate the linkage issue (reply thread initiated).

**Main Topic/Discussion**
Investigation into a connectivity or integration failure where specific system "linkages" were absent. The discussion focused on diagnosing the cause of this interruption and confirming the current status of the affected service.

**Pending Actions & Ownership**
*   **Action:** Verify why linkages are missing (initially requested).
    *   **Owner:** Chee Hoe Leong (via @mention).
    *   **Status:** Implicitly resolved by Shiva's follow-up indicating a self-correction of the root cause. No further action is explicitly required from Chee in this thread, as the issue was attributed to an external service outage rather than a configuration error requiring immediate manual intervention.

**Decisions Made**
*   **Root Cause Identified:** The absence of linkages was determined to be caused by the `gt-catalogue-service` being out of service.
*   **Status Confirmation:** It was confirmed that the `gt-catalogue-service` is now operational ("Now seems OK"), resolving the linkage issue.

**Key Dates & Follow-ups**
*   **Issue Reported:** March 30, 2026, at 09:20 UTC (Shiva Kumar Yalagunda Bas).
*   **Resolution Identified:** March 30, 2026, at 09:24 UTC (Shiva Kumar Yalagunda Bas).
*   **Follow-up Required:** None explicitly stated in the conversation; monitoring is advised to ensure stability.

**Contextual References**
*   **Space/Group:** BCRS Firefighting Group.
*   **Affected Component:** `gt-catalogue-service`.
*   **Issue Type:** Missing linkages due to service unavailability.


## [25/44] PDM Notification
Source: gchat | Group: space/AAAAnyFGr84 | Last Activity: 2026-03-30T09:22:44.338000+00:00 | Last Updated: 2026-03-30T10:46:49.406644+00:00
**Daily Work Briefing: PDM Notification Summary (Updated)**

**Key Participants & Roles**
*   **Gchat Notification / API Bot (Collection Runner):** Automated system generating test reports.
*   **Webhook Bot:** System component responsible for processing requests; currently experiencing a critical failure preventing execution.

**Main Topic**
Automated API contract and functional tests for the `gt-catalogue-service` in the Staging environment failed to execute due to a backend processing error. The system returned zero results because the Webhook Bot could not process the trigger, blocking all test suites before completion.

**Pending Actions & Ownership**
*   **Action:** Investigate and resolve the "Webhook Bot is unable to process your request" error affecting both `[API Tests]` and `[API Contract Tests]`.
*   **Owner:** Engineering/DevOps Team (responsible for the notification pipeline).
*   **Context:** Two separate test suites returned 0 Total Requests, 0 Passed, 0 Failed, and 0 Skipped results. The failure is attributed to the execution block rather than service logic or code defects.

**Decisions Made**
None recorded; current outcomes indicate a technical infrastructure failure requiring troubleshooting of the CI/CD notification mechanism rather than business decisions or code modifications.

**Key Dates & Follow-ups**
*   **Initial Incident Date:** March 18, 2026 (03:57 UTC) – *Historical record of previous pipeline failures.*
*   **Most Recent Failure:** March 30, 2026 (09:22:43 UTC).
*   **Environment:** Staging.
*   **Service:** `gt-catalogue-service`.
*   **Immediate Follow-up Required:** Review and restore the Webhook Bot functionality before re-triggering tests on the Collection Runner.

**Status Summary**
The automated run summary indicates a critical failure in the test execution pipeline itself, not the `gt-catalogue-service` being tested. Both reports generated at 09:22 UTC on March 30, 2026, explicitly state "Webhook Bot is unable to process your request." Consequently, no actual test cases were run or evaluated (Total Request: 0). This confirms a recurring systemic issue where the notification pipeline blocks execution. No manual intervention or code changes were discussed; immediate technical troubleshooting of the Webhook Bot and the associated Gchat Notification app integration is required to restore functionality.


## [26/44] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY | Last Activity: 2026-03-30T09:20:34.406000+00:00 | Last Updated: 2026-03-30T10:47:12.482480+00:00
**Updated Briefing: BCRS Firefighting Group**
**Date:** March 30, 2026 (Latest activity: ~09:24 AM)
**Source:** Google Chat Space & Shared UAT Tracker (84 messages total)

### **Key Participants & Roles**
*   **Prajney Sribhashyam:** Project Lead/Test Coordinator.
*   **De Wei Tey / Michael Bui / Wai Ching Chan:** Finance/SAP, Re-delivery specialists, and Technical Integration.
*   **Dany Jacob / Eswarlal Rajesh / Sneha Parab:** Active test participants and finance coordinators.
*   **Alvin Choo:** Status reporting lead (monitoring Starship channel updates).
*   **New Mentioned Stakeholders:** Shiva Kumar Yalagunda Bas, Chee Hoe Leong, Tiong Siong Tee, Daryl Ng, Koklin Gan.

### **Main Topics**
1.  **Feature Sign-Offs Achieved:** Prajney Sribhashyam confirmed sign-off for refunds across E-Comm and Scan & Go channels (March 30, ~08:29 AM). This completes all critical feature sign-offs required for the April 1 launch.
2.  **GovTech Quick Buy Testing:** Alvin Choo reported successful testing of GovTech integration for "Quick Buy" functionality (March 30, ~09:16 AM).
3.  **Linkage Investigation:** Shiva Kumar Yalagunda Bas flagged an issue regarding missing linkages on March 30 (~09:20 AM), requiring immediate investigation by Chee Hoe Leong and others.

### **Decisions & Updates**
*   **Production Testing Status:** While the timeline previously shifted to Production Testing, the confirmed sign-offs for refunds (E-Comm & Scan & Go) finalize critical path requirements for the April 1 deadline.
*   **Scope Expansion:** GovTech testing is now explicitly confirmed as successful for Quick Buy, adding to the previously noted Re-delivery and Deposit validation efforts.
*   **Thread Activity:** The "Production Testing" thread remains active (26 replies), but new threads have emerged regarding specific linkage failures and GovTech validation.

### **Pending Actions & Owners**
| Action Item | Owner(s) | Status/Context |
| :--- | :--- | :--- |
| **Resolve Missing Linkages** | Shiva Kumar Yalagunda Bas / Chee Hoe Leong | **Active:** Investigating why no linkages exist; raised March 30, ~09:20 AM. Viewed by 18 of 39 members. |
| **Execute Production Testing** | Prajney Sribhashyam / Team | **Active:** High-engagement thread opened March 30; focus remains on live environment validation despite new sign-offs. |
| **Re-delivery Logic Validation** | Michael Bui / Wai Ching Chan / De Wei Tey | **In Progress:** Transitioning from grooming to executing RPA and metadata workflow in Production. |
| **Overall Status Update** | Prajney Sribhashyam / Team | **Pending:** Provide comprehensive update to Alvin Choo regarding Starship channel changes, April 1 readiness, and current linkage issues. |
| **RPA Work Validation** | De Wei Tey / Wai Ching Chan | **Active:** Confirm RPA execution success in Production now that jobs are live. |

### **Key Dates & Deadlines**
*   **April 1:** Critical launch deadline; all critical features (including Refunds) signed off as of March 30.
*   **March 30 (Today):** Current active date for Production Testing, GovTech validation, and linkage investigation.

### **Historical Context Retained**
*   Original SAP Deposit API development deadline of Feb 20 remains noted as missed/risked; current effort focuses on resolving specific re-delivery logic gaps via live testing.
*   Existing e-comm test accounts remain unusable for Pre-order staff app; new BCRS CF items and specific GWP SKUs are required.
*   Deposit SKU linking investigation continues due to failure to link post-publishing (now explicitly flagged by Shiva Kumar Yalagunda Bas).
*   Previous Re-delivery flow testing experienced audio issues on March 16; current Production effort aims to resolve logic gaps via grooming and live validation.


## [27/44] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/jG0L_VCljVA | Last Activity: 2026-03-30T08:37:16.576000+00:00 | Last Updated: 2026-03-30T10:49:32.026228+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Meeting/Channel Resource:** [Internal] Digital Product Development Space
**Date of Discussion:** March 26, 2026 – Updated Status as of March 30, 2026
**Reference Link:** https://chat.google.com/space/AAQAUbi9szY

### 1. Key Participants & Roles
*   **Wai Ching Chan:** Issue reporter; provided the root cause analysis regarding database schema limitations.
*   **Michael Bui:** Product/Development inquiry; questioned why emojis break the flow (now answered).
*   **Sneha Parab:** Service Owner verification. Previously investigating `address-service` ownership; investigation context remains relevant but technical root cause is now identified in `order service`.
*   **Gopalakrishna Dhulipati & Dang Hung Cuong:** Tagged stakeholders for visibility.

### 2. Main Topic
Investigation into a bug where customer addresses containing **emoji icons** on iOS prevent order time slot changes. The root cause has been confirmed: when the **order service** attempts to save the changed address value to the database, the operation fails because existing schema columns do not support emoji characters.

### 3. Pending Actions & Ownership
*   **Action:** Execute database schema migration to upgrade columns from `utf8mb3_general_ci` to `utf8mb4_bin` to support emoji characters.
    *   **Owner:** To be assigned (Technical fix required based on Error 3988).
*   **Action:** Verify if the `address-service` logic needs updating in conjunction with the database fix, though the immediate blocker is the order service's save operation.
    *   **Owner:** Sneha Parab / Development Team.

### 4. Decisions Made & Technical Findings
*   **Root Cause Confirmed:** The issue is not a validation block at the application layer but a database schema incompatibility.
*   **Error Details:** The system logs indicate `Error 3988 (HY000): Conversion from collation utf8mb3_general_ci into utf8mb4_bin impossible for parameter`.
*   **Impact Scope:** iOS users entering emojis in addresses cannot save changes via the order service, forcing manual admin resolution.

### 5. Key Dates & Follow-ups
*   **March 26, 2026:** Initial report (10:35 UTC) and diagnostic discussion regarding emoji validation logic.
*   **March 30, 2026:** Root cause identified by Wai Ching Chan at 08:37 UTC. Confirmation that the `order service` fails during save due to collation mismatch (`utf8mb3_general_ci` vs `utf8mb4_bin`).

**Specific References:**
*   **Customer ID:** 2022036
*   **Platform Impact:** iOS users (specifically where emojis are entered in addresses).
*   **Technical Error:** `Error 3988` during address save operation in the order service.


## [28/44] FPG Everyone - General
Source: gchat | Group: space/AAAAjDYVcBU | Last Activity: 2026-03-30T08:33:58.244000+00:00 | Last Updated: 2026-03-30T10:50:12.140445+00:00
**Daily Work Briefing: FPG Everyone Chat Summary (Updated)**
**Date Range:** March 3 – March 30, 2026
**Source:** Google Chat (FPG Everyone - General)

### Key Participants & Roles
*   **Siti Nabilah:** Day of Service Campaign Promoter.
*   **Jasmine Neo:** Senior Executive, E-Commerce (Ordering Management).
*   **Keith Lee:** Industry Trends Monitor.
*   **Melissa Lim:** Community Engagement Lead.
*   **Maisy Heeng:** FPG Food Services Brand Lead.
*   **Si Min Ng:** Shorty Awards Campaign Coordinator.

### Main Topics
1.  **Digital Access Rollout:** Schedule confirmed and executed (C-suite/HR/Finance on Mar 16; Customer/Marketing/E-Commerce on Mar 23; Remaining Hub staff by Mar 30). User guide distributed.
2.  **Media Collaboration – "Bowl of Love":** Final episodes featuring Tyler Ten, Tasha Low, and Xiang Yun are officially live following the March 21 launch. The story focuses on warmth and healing with fresh Malaysian pork.
    *   **Platform:** @mediacorp.re.dian TikTok (`https://vt.tiktok.com/ZSusN9b4n/`).
3.  **Industry Recognition:** Lau Pa Sat's "Spin for your Huat" campaign was featured by Campaign Asia as a top CNY campaign to watch in 2026, competing alongside global heavyweights like Nike and Apple.
    *   **Source:** `https://www.campaignasia.com/article/brands-launch-campaigns-celebrating-chinese-new-year-2026/n554u1b7maurkcmkwcd29mooi2`
4.  **FairPrice Heartland Hits Launch (Mar 27):** Community storytelling contest launched to turn neighbourhood stories into music.
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
7.  **Linkpoints Loyalty Promo ($0.99):** Updated redemption details announced by Kara Pua on March 30. Offers include FairPrice Maple Syrup Cashews (100g) and Myojo Bowl Noodles Chicken (79g).
    *   **Availability:** Limited stocks; redeem early via the FairPrice Group app. Collect at Cheers or FairPrice Xpress (excluding Changi Airport and unmanned stores).

### Pending Actions & Ownership
*   **Shorty Awards Voting (Owner: All Staff):** Two FPG campaigns are shortlisted for the 18th Annual Shorty Awards "Audience Honor." Action: Create a personal email account, vote daily until **April 8** (one vote per category/day).
    *   **Campaigns:** *Bridge to Equity: Automating Savings via Myinfo* (Integrated) and *2025 End-Of-Year Unpacked* (Local).
    *   **Vote Links:** `https://shortyawards.com/18th/bridge-to-equity-automating-savings-via-myinfo`, `https://shortyawards.com/18th/2025-end-of-year-unpacked`, and `https://shortyawards.com/vote/`.
*   **Linkpoints Redemption (Owner: All Staff):** Redeem $0.99 rewards immediately. Collection deadline is **April 5, 2026**.
    *   **Link:** `https://go.fpg.sg/ki0bdx`
*   **Volunteer Engagement (Owner: All Staff):** Siti Nabilah shared a "Volunteer Spotlight" featuring Jasmine Neo. Staff encouraged to sign up for upcoming opportunities.
    *   **Link:** `https://forms.gle/UkyQDagmDy4mcY7K7`
*   **Sensory Test Sign-ups (Owner: All Staff):** Chapati screening form remains open (`https://forms.gle/DFYrahZcvhtcoJ9R7`). Frozen Snacks sign-up is closed.
*   **Heartland Hits Participation:** Staff encouraged to submit stories and rally regional crew before April 5.

### Decisions Made
*   **Awards Campaign:** Strategic decision to mobilize staff for Shorty Awards voting until April 8, utilizing personal emails to support *Bridge to Equity* and *2025 End-Of-Year Unpacked*.
*   **Wellness Extension:** Unity promotions extended with a new B1G1 offer (Mar 26–29).
*   **Service Event:** "Willing Hearts Kitchen Crew" spots are fully booked/closed as of late March 27 morning. Future opportunities remain open via the new sign-up link.
*   **Loyalty Initiative:** Decision to launch a low-barrier ($0.99) redemption offer, specifically updated with specific product SKUs (Cashews/Myojo Noodles) and collection points.
*   **Brand Expansion:** Approval and execution of Shabu Days launch (April 3) as FPG Food Services' first overseas brand.

### Critical Dates & Deadlines
*   **March 25:** World Oral Health Day offers expired.
*   **March 26–29:** Unity B1G1 Promotion on health/wellness essentials.
*   **April 3:** Shabu Days launch at Hillion Mall.
*   **April 5:** FairPrice Heartland Hits contest closes; Linkpoints redemption collection ends.
*   **April 8:** Shorty Awards voting deadline.


## [29/44] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/jfuh2YauMzM | Last Activity: 2026-03-30T08:28:46.862000+00:00 | Last Updated: 2026-03-30T10:50:31.909867+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Michael Bui:** Developer responsible for root cause analysis, PR merge, and post-deployment verification.
*   **Alvin Choo:** Primary recipient; coordinated immediate review and deployment execution.
*   **Daryl Ng:** Team lead for `website-service`; confirmed availability to review, deployed the update, and provided final confirmation.

**Main Topic**
Immediate resolution of the RMN incident in the `website-service` module. The scheduled Monday deployment was advanced to an urgent same-day production release on March 30, 2026. Following successful execution, Daryl Ng confirmed the deployment is live as of early morning UTC.

**Pending Actions & Ownership**
*   **Post-Deployment Verification:** Michael Bui to verify that search and category pages display more than one ad (specifically slots 1, 4, 8, etc.) immediately after deployment to confirm functional success. [Owner: Michael Bui]
*   **Status Monitoring:** Deployment is confirmed complete; Alvin Choo and Daryl Ng to monitor live environment stability during peak traffic.

**Decisions Made & Status Updates**
*   **Deployment Timing Revised (Immediate):** The window was advanced from "Monday evening" to **today, March 30, 2026**, following urgent requests by Alvin Choo and confirmation of availability by Daryl Ng.
*   **PR Merge Confirmed:** Michael Bui merged the Pull Request. The PRD pipeline is active.
*   **Deployment Completed:** As of **March 30, 2026 (08:28 UTC)**, Daryl Ng confirmed via chat: "It is deployed." This supersedes the previous status of "awaiting confirmation."
*   **Verification Criteria:** The team must now focus on validating that the fix resolves the ad count issue correctly on live pages.

**Key Dates & References**
*   **Incident Date/Time:** March 27, 2026 (14:50 UTC).
*   **UAT Confirmation Timestamp:** March 28, 2026 (03:08 UTC) – Michael Bui confirmed UAT success.
*   **Deployment Decision & Execution:** March 30, 2026 (01:12–02:04 UTC) – Request made; pipeline triggered.
*   **Deployment Confirmation Timestamp:** March 30, 2026 (08:28 UTC) – Daryl Ng confirmed live deployment.
*   **PR Link:** https://bitbucket.org/ntuclink/website-service/pull-requests/652/overview
*   **Pipeline Link:** https://bitbucket.org/ntuclink/website-service/pipelines/results/3983
*   **Jira Ticket:** DPD-715 (https://ntuclink.atlassian.net/browse/DPD-715)
*   **Service Scope:** `website-service`.

**Note on Progress**
The previous plan to delay deployment until Monday evening has been superseded. The team successfully transitioned to an immediate release strategy on March 30, 2026. With Daryl Ng's confirmation at 08:28 UTC that the code is deployed, the execution phase is complete. The current operational focus has shifted entirely from deployment logistics to functional validation by Michael Bui to ensure ad slots are rendering correctly in production.


## [30/44] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Last Activity: 2026-03-30T07:47:22.425000+00:00 | Last Updated: 2026-03-30T10:51:39.523720+00:00
# Daily Work Briefing: #dd-fpg-watchdog-alert

### Key Participants & Roles
*   **Datadog App:** Automated monitoring system.
*   **@hangouts-dd-dpd-watchdog-alert:** Targeted notification channel.
*   *Note: Interactions remain purely automated.*
*   **Monitor Tags:** `managed_by:datadog-sync`

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
*   **Mar 27, 2026:** Incident `story_key`: `f5d0894a-4a42-515d-985f-d06644833529`. Recovered at 17:37 UTC. Status: **Resolved**.

**Current Active/Resolved Sequence (Mar 28–30):**
*   **Incident 1 (Resolved, Mar 28):** Triggered March 28 at 03:26:22 UTC. Story Key: `8874d9ed-c1b1-5d8a-960b-85d280269164`. Recovered at 07:17:22 UTC. Status: **[P3] Recovered**.
*   **Incident 2 (Resolved, Mar 29):** Triggered March 28 at 21:27:22 UTC. Story Key: `784f6ec6-03de-5cee-a4e5-9fa93fd78209`. Recovered on **March 29, 2026, at 00:47:23 UTC**. Status: **[P3] Recovered**.
*   **Incident 3 (Resolved, Mar 30):** Triggered **March 30, 2026, at 04:27:22 UTC**. Story Key: `acd815df-528d-54a8-b915-069f6ae44fcc`.
    *   **Resolution Time:** March 30, 2026, at 07:47:22 UTC.
    *   **Duration:** ~3 hours 20 minutes.
    *   **Status:** **[P3] Recovered**.

### Pending Actions & Ownership
*   **Current Status:** The incident associated with `story_key: acd815df-528d-54a8-b915-069f6ae44fcc` has been automatically resolved. No further action is required at this time.
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Action Required:** Continue standard surveillance for the next cycle.

### Decisions Made
*   **Escalation Status:** Resolved without escalation. The incident duration (3h 20m) remained well within the 6-hour threshold.
*   **Protocol:** Escalation remains the protocol if resolution time exceeds 6 hours or if similar error messaging persists without self-resolution.

### Key Dates & Follow-ups
*   **Latest Event:** March 30, 2026, at 07:47:22 UTC (Recovered).
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Maintain standard surveillance. The successful resolution confirms the transient nature of the "unable to process" error profile for this story key.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Datadog Monitor Link:** [View in Datadog](https://app.datadoghq.eu/monitors/17447511)
*   **Latest Incident (Resolved):** https://app.datadoghq.eu/monitors/17447511?group=story_key%3Aacd815df-528d-54a8-b915-069f6ae44fcc&from_ts=1774855851000&to_ts=1774857051000&event_id=8566345413277227331

### Monitor Configuration
*   **Query:** `events("source:watchdog (story_category:infrastructure -story_type:(tcp_retrans_jump OR full_disk_forecast)) env:(PROD OR production OR prod)").rollup("count").by("story_key").last("30m") > 0`


## [31/44] ❗ Important Email
Source: gchat | Group: space/AAQAUJW8HMo | Last Activity: 2026-03-30T07:33:54.938000+00:00 | Last Updated: 2026-03-30T10:52:25.144620+00:00
**Daily Work Briefing Summary (Updated)**

**Key Participants & Roles**
*   **Michael Bui (You):** Managing Osmos support, event RSVPs, FileVault compliance, performance feedback, Project Light coordination, AI training follow-ups, and GCP Service Account security compliance.
*   **Kyle Nguyen / Nicholas Tan:** Leading the immediate remediation of legacy GCP Service Account (SA) keys; Kyle's team starts removal activities week of Mar 30.
*   **Himal Hewagamage:** Previous initiator of cleanup requests; clarified legacy SAs created 2019–2020 for testing. Shared Datadog SA list and coordination links.
*   **Miguel Ho Xian Da (FairPrice):** Lead for OSMOS integration.
*   **Jazz Tong (Head of Platform Eng):** On leave until Mar 23, 2026; tasked with identifying the appropriate contact person for SA key decommissioning coordination.

**Main Topics**
1.  **GCP Security & Service Account Decommissioning:**
    *   **Objective:** Clean up legacy GCP SA keys that were never rotated or exceed two active keys. Immediate focus on non-production (56 keys identified) and automated rotation for all accounts.
    *   **Timeline:** Kyle Nguyen's team begins remediation week of March 30, 2026.
    *   **Action:** Review the spreadsheet to indicate consent for including specific SAs in the automated key rotation process.
    *   **Resources:**
        *   Sheet: `https://docs.google.com/spreadsheets/d/1mGBCTRQDcTs0z_w0LjVtywDCtFHZhZfWYIRGqcNglpQ/edit` (Legacy SAs)
        *   Sheet: `https://docs.google.com/spreadsheets/d/1DdBymxBMXjV0zBO-TAyLUBV2viFUnChntZ2YssHaR9c/edit` (Working document)

2.  **AI Training & Workbench Follow-up:**
    *   Weekly 30-min virtual support on building agents in Workbench (Gemini Enterprise).
    *   **Schedule:** Wednesdays, 2:00 PM – 2:30 PM SGT (Mar 25 – May 31, 2026).
    *   **Action:** RSVP required; submit questions via form prior to sessions.

3.  **BCRS - Refunds Issue Warroom & Regroup Updates:**
    *   **Warroom:** Scheduled for Thursday, March 19, 2026, 3:30 PM – 4:30 PM SGT. *Conflict with Project Light remains.*
    *   **New Meeting (Today):** "BCRS Regroup - Open Item Planning" scheduled for **Thursday, March 26, 2026, from 4:00 PM to 5:00 PM SGT**.
    *   **Organizer:** Prajney Sribhashyam.

4.  **Project Light & RMN Integration:**
    *   **RMN Discussion:** Rescheduled for Thursday, March 26, 2026, from 2:00 PM – 3:00 PM SGT.
        *   *Attendees:* Michael Bui (Required), Rajiv Kumar Singh (Required), Bryan Choong (Optional).
    *   **Project Light:** Rescheduled to Mar 19, 4:00–5:00 PM SGT.

**Pending Actions & Ownership**
*   **GCP Security Consent (Michael Bui):** **Immediate Action Required.** Review the legacy SA spreadsheet and indicate consent for automated key rotation.
*   **BCRS Regroup RSVP (Michael Bui):** Respond to today's (March 26) invitation, 4:00–5:00 PM SGT.
*   **AI Training RSVP:** Submit "Yes" to the weekly session series starting March 25.
*   **RMN Meeting RSVP:** Confirm attendance for March 26, 2:00–3:00 PM SGT. *Note: This overlaps with your BCRS Regroup requirement (4:00 PM).*
*   **OSMOS Architecture:** Provide architectural details on SmartCarts and IPOS to finalize integration strategy with Accenture.

**Decisions Made**
*   **RMN Integration Timeline:** Team agreed to prioritize a focused working session on March 26 for architecture definition.
*   **GCP Remediation Priority:** Highest priority is the security cleanup of legacy keys; Kyle Nguyen's team committed to starting non-production removal week of Mar 30, with Nicholas Tan supporting. A dedicated Google Group will be created for weekly status updates.

**Critical Dates & Deadlines**
*   **Mar 18, 2026:** Performance Feedback Meeting.
*   **Mar 19, 2026:** BCRS Warroom (3:30 PM) & Project Light (4:00 PM). *Conflict.*
*   **Mar 25–May 31, 2026:** Weekly AI Workbench Sessions.
*   **Mar 26, 2026 (Today):** RMN Discussion (2:00–3:00 PM SGT); BCRS Regroup (4:00–5:00 PM SGT).
*   **Mar 30, 2026:** GCP Key Removal activities begin; ACNxOsmos Daily Cadence (Daryl Ng declined).
*   **Mar 31, 2026:** D&T Power Breakfast Planning Session; FileVault Final Deadline.


## [32/44] @omni-ops #standup - Mar 30
Source: gchat | Group: space/AAQAPG9qdz4 | Last Activity: 2026-03-30T07:17:57.497000+00:00 | Last Updated: 2026-03-30T10:52:58.362704+00:00
**Daily Work Briefing: #standup (omni-ops)**
**Date:** March 30, 2026
**Channel:** Google Chat (#standup) | [Link](https://chat.google.com/space/AAQAPG9qdz4)

### **Key Participants & Roles**
*   **Daryl Ng:** Facilitator; confirmed updates and provided final approval.
*   **Yangyu Wang:** Participant; confirmed meeting status.
*   **Rohit Pahuja:** Engineer; reported on completed deployment pipeline tasks and Backoffice maintenance.
*   **Sundy Yaputra:** Invitee (mentioned).
*   **Hanafi & Sneha:** External colleagues referenced regarding task delegation.
*   **Lester Santiago Soriano:** Reviewed a new Pull Request.

### **Main Topic**
The team addressed attendance issues and reviewed technical updates regarding the Backoffice deployment pipeline, specifically the removal of redundant rerun steps following flaky test resolution. Additionally, Rohit Pahuja's completed PR was discussed, and a new review request for an Omni Layout component was introduced later in the day.

### **Pending Actions & Ownership**
*   **Hanafi-related work:** Rohit Pahuja is scheduled to discuss this with Sneha today due to Hanafi's leave.
*   **Backoffice deprecated pages:** Sneha will assign Rohit the task of removing these pages.
*   **Pull Request Review (PR #658):** Lester Santiago Soriano has reviewed and requested a review for the Omni Layout PR at [Bitbucket](https://bitbucket.org/ntuclink/p13n-omni-layout/pull-requests/658). The link indicates 4 of 8 required reviewers have viewed it.

### **Decisions Made**
*   **Deployment Pipeline Update:** Daryl Ng verbally approved the removal of the "Backoffice PR rerun step" at 03:15 UTC, confirming that all previously flaky test cases now pass in a single run.
*   **New Review Workflow:** The team acknowledged the active review cycle for PR #658 initiated by Lester Santiago Soriano.

### **Key Dates & Follow-ups**
*   **March 30, 2026 (02:01 UTC):** Rohit Pahuja missed the initial standup due to conflicting meetings but provided his status update later that morning (approx. 02:28 UTC) after Daryl Ng requested attendance confirmation.
*   **March 30, 2026 (03:15 UTC):** Daryl Ng confirmed the deployment pipeline update with "okay sounds good."
*   **March 30, 2026 (07:17 UTC):** Lester Santiago Soriano posted a link for PR #658 requesting review; the status shows partial reviewer engagement.

### **Summary of Status**
Rohit Pahuja successfully submitted a Pull Request to remove the Backoffice PR rerun step, validating that flaky tests are now stable in one run. Despite missing the initial sync at 02:01 UTC, Rohit communicated his progress regarding Hanafi-related dependencies and Backoffice maintenance, which were formally acknowledged by Daryl Ng at 03:15 UTC. Later in the day (07:17 UTC), the team received a new task from Lester Santiago Soriano to review PR #658 for the Omni Layout project. Rohit remains scheduled to finalize discussions with Sneha regarding Hanafi's tasks and receive specific assignments for Backoffice cleanup today.


## [33/44] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/rKtZEQsyOFI | Last Activity: 2026-03-30T06:11:55.755000+00:00 | Last Updated: 2026-03-30T06:38:10.067381+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Michael Bui:** Lead developer/technical contact; created initial Confluence documentation for RMN integration.
*   **Alvin Choo:** Decision maker (Technical Lead/Manager); approved draft templates for vendor use.
*   **Tiong Siong Tee:** Technical reviewer; provided feedback on documentation format.

**Main Topic**
Finalization of API specification templates for the CoMall team, specifically regarding "Project Light Attack and Defence" RMN integration for Identity and Payments services.

**Decisions Made**
1.  **Template Approval:** Alvin Choo approved the Confluence drafts created by Michael Bui as the standard template to be shared with the vendor for Identity and Payments API integrations.
2.  **Documentation Scope:** Confirmed that documentation will focus strictly on **"To-Be"** state specifications (future APIs). The requirement to document "As-Is" existing states was removed; no As-Is documentation is required.
3.  **Ad Service Retention:** Confirmed by Alvin Choo that the Ad service will be retained, and CoMall does not need to implement a retail media micro-service.

**New Developments & Status Updates**
*   **Review Cycle (March 30, 2026):** Tiong Siong Tee reviewed the approved drafts and provided two initial feedback points regarding format:
    *   Clarifying responsibility boundaries between teams.
    *   Defining "As-Is" vs. "To-Be" states.
*   **Resolution:** Alvin Choo clarified that only **"To-Be"** APIs need to be documented, resolving the first point. The team agreed to focus solely on future specifications.
*   **Efficiency Strategy:** Alvin Choo proposed utilizing AI tools to streamline the documentation process for these templates.

**Pending Actions & Ownership**
*   **Refine Responsibility Matrix:** Tiong Siong Tee and Alvin Choo must determine a clear format to indicate which parts of the integration are CoMall's responsibility versus internal responsibilities (addressing the second comment point).
*   **Vendor Handoff:** Distribute the finalized "To-Be" templates to CoMall.

**Key Dates & Deadlines**
*   **March 27, 2026:** Michael Bui completed initial Confluence draft templates.
*   **March 30, 2026:** Alvin Choo approved drafts; Tiong Siong Tee provided format feedback; consensus reached on "To-Be" only approach.
*   **Next Week:** Scheduled kick-off/grooming session with CoMall.

**Specific References**
*   **Services Involved:** Identity and Payments (APIs).
*   **Ad Services:** Display Ads (Banner/Video) supported; Dynamic Ads in PLP Content Cards require development. Ad service is retained by the organization.
*   **Document Format:** Confluence draft templates (exportable to PDF if required); future focus on "To-Be" specifications only.


## [34/44] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/z2zSDKRl4Vc | Last Activity: 2026-03-30T06:06:48.755000+00:00 | Last Updated: 2026-03-30T06:38:28.447290+00:00
**Daily Work Briefing: [Internal] (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Michael Bui:** Initiator/Requester.
*   **Daryl Ng:** Review Lead/Scheduler.
*   **Yangyu Wang, Lester Santiago Soriano, Sundy Yaputra, Zaw Myo Htet, Chee Hoe Leong:** Assigned reviewers.

**Main Topic/Discussion**
The discussion involves multiple code review requests. Initial focus was on suppressing BCRS deposit posting within the re-delivery journey (PR #7). Subsequently, a schedule for peer reviews regarding next week's deliverables was established by Daryl Ng. On March 30, Lester Santiago Soriano directly requested team review for a new Pull Request concerning P13N Omni layout updates.

**Pending Actions & Ownership**
*   **Action:** Review PR #7 (`https://bitbucket.org/ntuclink/bcrs-deposit-posting/pull-requests/7`) to suppress BCRS deposit posting in the re-delivery journey.
    *   **Owner:** @Daryl Ng (Requested by Michael Bui).
*   **Action:** Review PR #658 (`https://bitbucket.org/ntuclink/p13n-omni-layout/pull-requests/658`) for P13N Omni layout updates.
    *   **Owner:** Assigned Team (Requested by @Lester Santiago Soriano).
*   **Action:** Assist with upcoming review tasks for next week's deliverables.
    *   **Owners:** @Yangyu Wang, @Sundy Yaputra, @Zaw Myo Htet, @Chee Hoe Leong (Assigned by Daryl Ng; scope expanded to include PR #658).

**Decisions Made**
*   No formal technical approvals were recorded. The thread represents a series of direct review requests and administrative assignments for workload distribution across the upcoming week.

**Key Dates & Follow-ups**
*   **Initiation Date:** March 27, 2026 (19:33 UTC) – Michael Bui posted PR #7 link.
*   **Assignment Date:** March 28, 2026 (00:08 UTC) – Daryl Ng expanded the review list for next week's tasks.
*   **New Request Date:** March 30, 2026 (06:06 UTC) – Lester Santiago Soriano posted PR #658 link and requested reviews.
*   **Upcoming Deadline/Focus:** "Next week" – Tasks assigned to the team target this period.

**References**
*   **PR Links:**
    *   `https://bitbucket.org/ntuclink/bcrs-deposit-posting/pull-requests/7` (BCRS Deposit Posting)
    *   `https://bitbucket.org/ntuclink/p13n-omni-layout/pull-requests/658` (P13N Omni Layout)
*   **Space URL:** `https://chat.google.com/space/AAQAUbi9szY`


## [35/44] DPD x DPM
Source: gchat | Group: space/AAQApzD7Im0 | Last Activity: 2026-03-30T03:05:18.172000+00:00 | Last Updated: 2026-03-30T06:45:02.800302+00:00
### Daily Work Briefing: DPD x DPM Collaboration Space (Updated)

**Key Participants & Roles**
*   **Daryl Ng:** Tech Lead; flagged CHAS calculation issues. Tagged regarding Gamification ownership, delivery logic, and urgent ticket status updates for the OMNI review.
*   **Rajesh Dobariya:** Inquired about Gamification data and "Normal" vs. "Express" display logic. Initiated "1HD Business testing." Recently flagged a discrepancy where tickets are ready for UAT (per Zaw) but show 0% completion status. Urged Daryl Ng to update ticket statuses by the afternoon OMNI review, noting Andin is on leave.
*   **Andin Eswarlal Rajesh:** Previously initiated "1HD Business testing" (March 25). Currently on leave as of March 27; however, posted new updates regarding "Dynamic Whitelisting UAT" on March 30.
*   **Vivian Lim Yu Qian:** Driving mandates (MTI price per piece) and SWA migration history.
*   **Zaw:** Credited with confirming tickets are ready for UAT.

**Main Topics**
1.  **Dynamic Whitelisting UAT:** Andin Eswarlal Rajesh initiated a new discussion on "Dynamic Whitelisting UAT" on March 30, following previous leave status. This replaces the earlier focus solely on 1HD testing.
2.  **Ticket Status Discrepancy (Resolved/Critical):** Rajesh Dobariya identified a critical mismatch on March 27 where tickets were "ready for UAT" per Zaw but tracked at 0%. Immediate correction was flagged before the afternoon OMNI review.
3.  **Delivery Text Logic:** Daryl Ng requested a breakdown of the *existing* logic for displaying "orange label" text on Omni and OG homepages (March 25). Last reply pending from Yangyu Wang & Zi Ying Liow as of March 25, 01:34 AM.
4.  **Gamification Data Requirements:** CRM team requires specific BigQuery data points for PNS automation. Needs confirmation on existing data or effort estimation for pushing new data.
5.  **Govt Mandate (MTI):** Implementation of "Price per Piece" info for 40+ categories in the current app MVP.
6.  **CHAS Calculation Bug:** UI discrepancy where cart-level discounts split at the sales order level affect CHAS calculations (`DPD-530`).
7.  **SWA Migration:** Investigation into reverting SWA ad serving from Publitas back to Wordpress (`DIS-585`).

**Pending Actions & Ownership**
*   **Ticket Status Update:** Correct ticket status from 0% to "Ready for UAT" (Action flagged March 27). *Owner: Daryl Ng.*
*   **Dynamic Whitelisting Review:** Follow up on Andin's new "Dynamic Whitelisting UAT" discussion initiated March 30. *Owner: Team/Rajesh Dobariya.*
*   **Orange Label Logic Clarification:** Share and document existing logic for Omni/OG homepages regarding text variables. *Owner: Daryl Ng.*
*   **Gamification Data Query:** Clarify ownership of Gamification features and provide BQ table/column names or confirm data push needs. *Owner: Daryl Ng.*
*   **Tech Lead Confirmation:** Determine lead ownership for Price per Piece expansion. *Owner: Vivian Lim Yu Qian / Team.*

**Decisions Made**
*   Consensus remains that ticket statuses require immediate correction to reflect UAT readiness before the OMNI review. The intent to fix the CHAS bug via API update is established. Implementation details for the "orange label" text are pending Daryl Ng's input. New UAT scope (Dynamic Whitelisting) has been opened by Andin.

**Key Dates & Deadlines**
*   **March 30, ~03:05 AM:** Andin Eswarlal Rajesh posts regarding "Dynamic Whitelisting UAT" with 2 replies; last reply noted at 3:45 AM.
*   **March 27, ~03:02 AM:** Rajesh Dobariya tags Daryl Ng to update statuses by the afternoon OMNI review, noting Andin is on leave.
*   **March 27, ~02:50 AM:** Rajesh notes tickets are ready for UAT (per Zaw) but show 0% done; flags need for status update.
*   **March 25, 06:59 AM:** Andin initiates "1HD Business testing" discussion.

**Reference Links**
*   Price Per Piece Wiki: `https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008175965/Price+Per+Piece+Multipack+in+Display+Unit`
*   CHAS Ticket: `DPD-530`
*   Sticky Header UI Ticket: `ENGM-2501`
*   SWA Migration Ticket: `DIS-585`


## [36/44] Omni Fairmily
Source: gchat | Group: space/AAAAQuMQ3Bs | Last Activity: 2026-03-30T02:53:32.229000+00:00 | Last Updated: 2026-03-30T06:45:28.539649+00:00
**Daily Work Briefing Summary: Omni Fairmily Space**

**Key Participants & Roles**
*   **Pauline Tan:** Announced FPG ADvantage LinkedIn launch; highlighted team's showcase at the FairPrice Partners' Excellence Awards. Recently represented FPG ADvantage at eTail Asia 2026 to discuss retail media capabilities and shopper engagement. Acknowledges cross-functional contributors: Rajiv Kumar Singh, Christopher Yong, Wendi Koh, Karlie Sia, Allen Umali, Pamela Koh, Serene Tan Si Lin, Neo Seng Ka, Bryan Choong, and Sriharsh.
*   **Fiona U:** Organized group lunch orders; confirmed food distribution.
*   **Christine Yap Ee Ling:** Lead for Project Light user research; coordinating participant recruitment.
*   **Jacob Yeo:** Edited previous lunch order messages (Meta-data note).

**Main Topic/Discussion**
The conversation covers four distinct activities:
1.  **Marketing & Brand Presence:** Following the official FPG ADvantage LinkedIn launch, Pauline Tan reported on the team's showcase at the FairPrice Partners' Excellence Awards. Additionally, she represented FPG ADvantage at eTail Asia 2026, sharing how the initiative strengthens retail media capabilities to capture shopper attention and enhance brand interactions across in-store and digital touchpoints. The event facilitated connections with regional brands, agencies, and partners.
2.  **Business Development:** A call for referrals was issued to connect potential brands or partners interested in FPG ADvantage opportunities via `sales.fpgadvantage@fairpricegroup.sg`.
3.  **Team Logistics:** Coordination of a group lunch order for "Heybo," collected at L12 main pantry.
4.  **User Research Recruitment:** Urgent request to recruit non-staff participants (friends/family) for usability testing on the FPG App ("Project Light").

**Pending Actions & Ownership**
*   **Social Media Engagement:** Follow, like, and share the FPG ADvantage LinkedIn page. *Owner: All Team Members.*
*   **Business Development Referrals:** Connect brands or partners keen to explore opportunities with FPG ADvantage via email. *Owner: All Team Members.*
*   **Recruitment Referral:** Forward the provided WhatsApp/Telegram template to trusted social circles to find eligible participants. *Owner: All Team Members (as requested by Christine).*
*   **Participant Booking:** Prospective participants must book slots via the provided calendar link. Confirmation of slots will be handled by Sriharsh or Christine after booking.

**Decisions Made**
*   **Lunch Logistics:** Group order finalized for Heybo with a collection ETA of 12:00 PM on March 10, 2026. Food is currently available at L12 main pantry. *(Note: The original deadline was 10:30 AM).*
*   **Research Incentives:** Confirmed token amounts ($10 for online/Google Meet, $20 for in-person at FairPrice Hub/Joo Koon/L12).

**Key Dates & Deadlines**
*   **March 9, 2026 (09:33 AM):** FPG ADvantage LinkedIn page launch announcement.
*   **March 10, 2026:**
    *   Order deadline: 10:30 AM.
    *   Lunch collection ETA: 12:00 PM.
    *   Food arrival confirmed by 04:02 AM on March 10.
*   **March 17, 2026 (08:04 AM):** Post-event report issued regarding the FairPrice Partners' Excellence Awards showcase.
*   **March 16, 2026 (02:05 AM):** User research recruitment request issued.
*   **Recent Event:** eTail Asia 2026 (Post-event reporting ongoing). Read more at: `https://www.fpgadvantage.com.sg/customers-research-insights/navigating-the-future-of-retail-media-fpg-advantage-at-etail-asia-2026/`
*   **Upcoming Research Sessions:** March 25–27, 2026 (Wednesday to Friday). Available slots are 12:00 PM and 1:15 PM.
*   **Confirmation Timeline:** Sriharsh or Christine will confirm booked slots within 2 working days.

**Participant Eligibility Criteria (Project Light)**
Participants must be non-FPG staff, aged 25+, fluent in English, currently use the FPG App, have ordered online grocery delivery in the past 3 months, and manage household grocery shopping. They must not have participated in a FairPrice customer interview in the last 6 months.


## [37/44] @ecom-ops #standup - Mar 30
Source: gchat | Group: space/AAQAqo-_GgY | Last Activity: 2026-03-30T02:40:55.376000+00:00 | Last Updated: 2026-03-30T06:46:04.789139+00:00
**Daily Work Briefing: @ecom-ops #standup (Mar 30)**

**Key Participants & Roles**
*   **Sneha Parab**: Standup facilitator; initiated the session call.
*   **Dang Hung Cuong**: Technical lead/architect; identified memory issues and defined test scope.
*   **Hanafi Yakub**: Provided documentation link for Store Closure Workflow SOP.
*   **Shiva Kumar Yalagunda Bas**: Provided technical clarification on data synchronization logic and operational review requirements.

**Main Topic/Discussion**
The discussion focused on the scope of an upcoming load test for the order synchronization system, specifically addressing a previous Out of Memory (OOM) error. The team debated whether to isolate the "CM51" component or test the entire order sync process. Additionally, there was a brief technical clarification regarding the latency and operational workflow of seller profile changes within the master data. Hanafi Yakub shared the **Store Closure Workflow SOP Guide** (NTUCLink) as a reference for operational procedures.

**Decisions Made**
*   **Test Scope**: Dang Hung Cuong directed that the load test must cover the **whole order sync** process, explicitly rejecting a test limited only to "CM51."
*   **Documentation Reference**: The team referenced Hanafi Yakub's shared SOP guide regarding store closure workflows.

**Pending Actions & Owners**
*   *Execute Load Test*: Conduct a load test on the entire order sync workflow (not just CM51). **Owner**: Implied engineering team (likely Dang Hung Cuong's direct reports or Shiva Kumar Yalagunda Bas based on context).
*   *Operational Review Protocol*: No new action item assigned yet, but the constraint that "seller changing won't be reflected in master immediately" without an ops team review was established as a system behavior.
*   *SOP Alignment*: Team members (5 of 8 viewed) have accessed Hanafi Yakub's Store Closure Workflow SOP; further integration into testing or operations is pending discussion.

**Key Dates, Deadlines & Follow-ups**
*   **Date**: March 30, 2026 (Standup session).
*   **Reference Case**: Previous OOM failure occurred during a full process test (specific date not cited, but referenced as "last time").
*   **Next Steps**: The team needs to execute the broader load test strategy defined by Dang Hung Cuong and align with the Store Closure SOP.

**Specific References & Technical Notes**
*   **System Issue**: Out of Memory (OOM) error previously encountered during full process testing.
*   **Component Mentioned**: CM51 (excluded from current test scope).
*   **Data Sync Behavior**: Seller profile changes do not reflect in the master database immediately; they require a review by the operations team before propagation.
*   **Documentation Link**: [Store Closure Workflow - SOP GUIDE](https://ntuclink.atlassian.net/wiki/spaces/SE/pages/1995997811/Store+Closure+Workflow+-+SOP+GUIDE) (Shared by Hanafi Yakub).


## [38/44] [Prod Support] Ecom FFS Ops
Source: gchat | Group: space/AAAAde_cYKA | Last Activity: 2026-03-30T02:40:20.597000+00:00 | Last Updated: 2026-03-30T06:46:30.058567+00:00
**Daily Work Briefing: [Prod Support] Ecom FFS Ops (Updated Mar 30)**

**Key Participants & Roles**
*   **Wai Ching Chan / Sampada Shukla:** Operations/Product Leads.
*   **TL HCBP FFS:** Store Lead reporting T18/T19 picking queue blockages and scan issues.
*   **Adrian Yap Chye Soon:** Technical Lead/Support (investigating data anomalies and dispatcher app failures).
*   **Akash Gupta:** DPD / Fulfilment / On Call.
*   **Yoongyoong Tan:** Reporting HCBP picking Q issues.
*   **Ler Whye Ling Angel:** Escalation point for "No picking Q."

**Main Topics**
1.  **Packlist Discrepancies & Validation (Expanded):** Ongoing investigation into critical `packed_qty` anomalies (NULL values or massive mismatches vs. `delivered_qty`).
    *   **New Critical Incident (Mar 29):** Sampada Shukla flagged a severe anomaly at **Hyper Changi (Store ID 45)**.
        *   Order #22972590: `packed_qty` **90,203,969** vs. `delivered_qty` **2**. Price impact noted ($19.95 MRP/$39.9).
    *   **Previous Incidents:** Includes Mar 26 VivoCity (Orders #22912255/#22906879 with ~13M discrepancy), Mar 25 Sun Plaza, and prior anomalies at Hyper Sports Hub.

2.  **Dispatcher App & Zone Scanning Failure (Mar 28):** Escalation regarding the dispatcher app's inability to scan new zones.
    *   **Timeline:** Reported 01:45 AM Mar 28 at **hvivo**. Adrian Yap Chye Soon provided video evidence for review; technical investigation remains active.

3.  **HCBP Picking Queue Issues (Mar 27):** Escalated urgency regarding "No picking Q" blockage and T18 display failures.
    *   **Timeline:** Initial blockage reported 02:08 AM; escalated by Ler Whye Ling Angel at 02:52 AM; T18 data failure reported by TL HCBP FFS at 07:47 AM.

**Pending Actions & Ownership**
*   **Data Validation (Urgent - Mar 30):**
    *   *@Akash Gupta / On Call:* Immediate validation of the massive `packed_qty` mismatch for Order #22972590 at Hyper Changi.
    *   *@Wai Ching Chan @Sampada Shukla:* Prioritize review of this new anomaly alongside pending Sun Plaza and previous VivoCity validations.
*   **Dispatcher App Investigation (Mar 28):**
    *   *@Adrian Yap Chye Soon / Technical Team:* Continue RCA on the "unable to scan new zone" failure at hvivo based on video evidence.
*   **HCBP Queue Investigation (Mar 27):**
    *   *@Adrian Yap Chye Soon / @Gopalakrishna Dhulipati:* Monitor resolution of Mar 27 "No picking Q" and T18 display failures following escalations by Ler Whye Ling Angel.

**Decisions Made**
*   **App Release Strategy:** Picker App 10.4.0 rollout remains on hold pending resolution of critical data anomalies (Mar 18–30). Full rollout is contingent on stability post-fixes, specifically addressing:
    *   The newly discovered Mar 29 Hyper Changi anomaly (Order #22972590).
    *   The resolved/pending Mar 26 VivoCity alerts.
    *   The resolved Mar 27 HCBP queue/T18 failures.
    *   The new dispatcher app zone scanning issue at hvivo.

**Key Dates & Deadlines**
*   **Immediate:** Validation of Mar 29 Order #22972590 and RCA for Mar 28 Dispatcher App failure at hvivo.
*   **Pending:** Comprehensive RCA for recent `packed_qty` anomalies across Sports Hub, VivoCity, Parkway, Changi, Sun Plaza, Hyper VivoCity, and the new Hyper Changi site.

**Critical Alerts**
*   **Active Alert (Mar 30):** Packlist quantity (`90M`) significantly exceeds delivered quantity at **Hyper Changi (Store ID 45)**. Requires immediate data validation by Ops.
*   **Secondary Active Alert (Mar 28):** Dispatcher app unable to scan new zone at **hvivo**. Video evidence available; requires technical check.
*   **Tertiary Active Alert (Mar 27):** HCBP "No picking Q" issue escalated by Ler Whye Ling Angel.


## [39/44] Web Chapter
Source: gchat | Group: space/AAAASzhKzV0 | Last Activity: 2026-03-30T02:15:26.223000+00:00 | Last Updated: 2026-03-30T02:39:44.232298+00:00
**Daily Work Briefing: Web Chapter**

**Key Participants & Roles**
*   **Wai Ching Chan**: Reporter/Initiator (identified recurring issue with backoffice E2E tests).
*   **Madhuri Nalamothu**: Tagged assignee for investigation.
*   **Milind Badame**: Tagged assignee for investigation.

**Main Topic**
Investigation into persistent failures of the **backoffice E2E TestSigma UAT**. Wai Ching Chan reported that tests have failed across multiple execution attempts, requiring immediate technical review.

**Pending Actions & Ownership**
*   **Action**: Investigate root cause of failing backoffice E2E tests in TestSigma UAT and resolve pipeline issues.
    *   **Owner**: Madhuri Nalamothu, Milind Badame.
    *   **Context**: The reporter has attempted runs multiple times without success.

**Decisions Made**
*   No decisions were recorded in this log; the conversation is an initial escalation request for assistance.

**Key Dates & Follow-ups**
*   **Timestamp**: March 30, 2026, at 02:15 UTC (Chat message sent).
*   **Reference Links**:
    *   Pipeline Failure Log: `https://bitbucket.org/ntuclink/platform-admin/pipelines/results/13756/steps/{27e77363-8855-4cb3-84d2-1a4f33b6ae00}`
    *   TestSigma Run Details: `https://app.testsigma.com/ui/td/runs/247783`
*   **Space URL**: `https://chat.google.com/space/AAAASzhKzV0`

**Summary**
Wai Ching Chan flagged a critical stability issue with the backoffice E2E TestSigma UAT environment on March 30, 2026. The reporter noted repeated failures and requested direct support from Madhuri Nalamothu and Milind Badame to review the provided Bitbucket pipeline logs and TestSigma run data. Immediate attention is required to analyze these specific runs and restore test stability.


## [40/44] Alvin Choo
Source: gchat | Group: dm/zmMZpgAAAAE | Last Activity: 2026-03-30T02:14:07.739000+00:00 | Last Updated: 2026-03-30T02:40:07.029434+00:00
**Daily Work Briefing: RMN & Postmortem Updates (Updated)**
**Resource:** Alvin Choo (Lead/Manager) | **Participant:** Michael Bui (Domain Expert, Backend Dev)
**Date Range:** March 3 – March 24, 2026 + March 30 Discussion

### **Key Participants & Roles**
*   **Alvin Choo:** Leads coordination for RMN postmortem reports, travel logistics, and visa invitations. Contact: +65 9351 0653.
*   **Michael Bui:** Domain expert responsible for backend implementation; currently on leave until April 2 (Public Holiday April 3).

### **Main Topics**
1.  **Wuhan Travel & Visa Processing:** Departure confirmed for **April 6, 2026**. Michael requires a multi-entry Type M visa applied for one month in advance. Alvin is securing an invitation letter from CoMall.
2.  **RMN Postmortem & Incident Review:** Finalizing report for BCRS completion; addressing "Overage on transaction sync" and transition to impressions-based model.
3.  **Technical Implementation & Task Redistribution:** Discussion regarding a 5-man-day ticket in collaboration with Nikhil (created last Friday). Alvin identified Michael's weekend work requirement as a risk. Concluded that the task can be reassigned to another Backend Engineer from Daryl's team, though Michael will remain available for logic verification and complex dependency clarifications rather than formal Knowledge Transfer (KT).

### **Decisions Made**
*   **Task Reassignment:** Alvin will assign the Nikhil ticket to a Backend Engineer from Daryl's team. The original 5-man-day estimate applied only to Michael; others may require more time due to complexity (multiple service dependencies).
*   **Support Model:** No formal KT session is required as AI can assist in logic derivation. However, Michael will verify logic and clarify complex parts during development if needed.
*   **Visa Strategy:** Visa Type M confirmed. Alvin advised checking with Gopal and Ravi regarding self-processing methods while waiting for the invitation letter.
*   **Contact Exchange:** On March 25, Alvin provided his mobile number (**93510653**) for direct coordination.
*   **Workshop Deliverables:** Michael will prepare "as-is" and "to-be" design plans rather than full slides; existing documents need alignment only.

### **Pending Actions & Ownership**
| Action Item | Owner | Details/Context |
| :--- | :--- | :--- |
| **Ticket Reassignment** | Alvin Choo | Assign Nikhil ticket to a BE from Daryl's team; allow them to self-learn logic with Michael available for verification. |
| **Visa Application** | Michael Bui | Apply for multi-entry Type M visa immediately upon receiving invitation letter. Use Alvin's number (93510653) for coordination. |
| **Invitation Letter** | Alvin Choo | Secure business letter from CoMall to expedite the visa process. |
| **Workshop Prep (Design)** | Michael Bui | Create docs detailing "as-is" vs. "to-be" flows; note: On leave until April 2, PH on April 3. |
| **Postmortem Review** | Alvin Choo | Final review after PDA impact verification (Vijay) and Advertima POV status inclusion. |

### **Key Dates & Milestones**
*   **March 30:** Discussion held regarding Nikhil ticket redistribution and de-risking Michael's workload.
*   **April 2:** End of Michael's current leave period.
*   **April 3:** Public Holiday in Singapore.
*   **April 6:** Confirmed departure date for Wuhan, China.
*   **April 7-8:** Target UAT readiness by Michael (if needed) to meet Nikhil's April 9 PRD deployment timeline.
*   **End of Q1 2026:** Advertima POV pilot period concludes.


## [41/44] [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Last Activity: 2026-03-30T01:46:28.163000+00:00 | Last Updated: 2026-03-30T02:41:16.411324+00:00
**Daily Work Briefing: [Prod Support] Marketplace**

**Key Participants & Roles**
*   **Support/Operations:** Willie Tan, Iris Chang, Lalita Phichagonakasit, Charlene Tan, Jie Yi Tan, Ayton See, Amos Lam, Michelle Lim.
*   **Technical/Admin Team:** Dang Hung Cuong, Shiva Kumar Yalagunda Bas (Frequent recipients of access/access issues), Olivia -, Jill Ong, Greta Lee, Zaw Myo Htet, Angella Yeo, Cassandra Thoi, Gopalakrishna Dhulipati, Ee Ling Tan.
*   **New Reporter:** Muhammad Sufi Hakim Bin Safarudin.

**Main Topics & Discussion Summary**
Discussions continue to focus on operational blockers regarding seller onboarding, order fulfillment discrepancies, system configuration errors, and data visibility gaps. Recent reports highlight critical picklist generation failures affecting specific orders. Major themes include:
1.  **Picklist Generation Failures (New):** Muhammad Sufi Hakim Bin Safarudin reported two critical incidents on Mar 30:
    *   No picklist was generated for Order #258155683 despite activity on Mar 25.
    *   Picklists are not being generated for Postponed Order #256653797.
2.  **Data Visibility Gap:** Greta Lee (Mar 27, 08:51 UTC) requested live dashboards for daily MP ordered quantities for specific SKUs, citing a discrepancy between the current forecast cutoff (4 AM) and real-time high run-rate volume. She tagged Dang Hung Cuong, Shiva Kumar Yalagunda Bas, and Amos Lam.
3.  **PickerApp Barcode Errors:** Dang Hung Cuong is investigating a truncation issue for Pureen (SAP: 90247763), where the system displays `95561234717` instead of `9556123471735`. Greta Lee also flagged SKU 90244060 for Yumsay Foods as non-existent.
4.  **Access Management:** Amos Lam (Mar 27, 10:00 UTC) requested PickerApp access linkage for Seller ID 31435. Shiva Kumar Yalagunda Bas confirmed completion at 11:29 UTC on Mar 27.

**Pending Actions & Ownership**
*   **Picklist Investigation (Urgent):** Technical team to investigate why picklists failed for Order #258155683 (Mar 25 activity) and Postponed Order #256653797, reported by Muhammad Sufi Hakim Bin Safarudin.
*   **Live Dashboard Request:** Technical team to provide or configure a live dashboard for daily MP ordered quantities to bridge the 4 AM–current time gap (Greta Lee, Mar 27).
*   **Truncated Barcode Investigation:** Dang Hung Cuong to investigate Pureen's barcode truncation issue.
*   **PickerApp SKU Error:** Technical team to investigate why SKU 90244060 for Yumsay Foods is flagged as non-existent.
*   **Urgent Promotion Removal:** Dang Hung Cuong and Gopalakrishna Dhulipati to remove incorrectly set up promotion for Item ID: 90244361 (Lalita Phichagonakasit, Mar 20).
*   **Order Status Investigation:** Team to check discrepancies for Order #256055476 and Order #248407866.
*   **Vendor Report Issues:** Investigate missing sales breakdown reports for CoLab Apac (NED-277148) and Old Shanghai (NED-277329).

**Decisions Made**
*   Dang Hung Cuong is prioritizing the removal of Item ID: 90244361, the new picklist failure issues raised by Muhammad Sufi Hakim Bin Safarudin, the Woah Group offers error, and the current barcode truncation investigation for Pureen.
*   Dang Hung Cuong and Shiva Kumar Yalagunda Bas are assigned to investigate vendor picklist anomalies (including recent failures).
*   **Completed:** Access linkage for Seller ID 31435 (Nathalie Huang) was successfully executed by Shiva Kumar Yalagunda Bas on Mar 27, 11:29 UTC.

**Key Dates & Deadlines**
*   **2026-03-30:** Muhammad Sufi Hakim Bin Safarudin reported picklist generation failures for Order #258155683 (missing from Mar 25) and Postponed Order #256653797.
*   **2026-03-27:** Greta Lee reported data visibility gap; Dang Hung Cuong, Shiva Kumar Yalagunda Bas, and Amos Lam tagged. Amos Lam requested access for Seller ID 31435; completed by Shiva Kumar. Lalita Phichagonakasit previously reported Pureen barcode truncation.
*   **2026-03-26:** Iris Chang requested sales report for UNICO Distribution Services; Greta Lee reported Yumsay Foods barcode issue; Ee Ling Tan queried picklist delivery.
*   **2026-03-25:** Cassandra Thoi requested checks on orders #256055476 and #248407866.
*   **2026-03-21:** Amos Lam reported vendor picklist failure due to public holiday opt-out status.


## [42/44] RMN Incidents
Source: gchat | Group: space/AAQAz11ATzY | Last Activity: 2026-03-30T01:15:17.707000+00:00 | Last Updated: 2026-03-30T02:41:35.551227+00:00
**Daily Work Briefing: RMN Incidents (Updated)**

**Key Participants & Roles**
*   **Nikhil Grover:** Issue initiator; successfully identified root cause with team. Confirmed fix deployment on March 30th.
*   **Rachit Sachdeva:** Investigator; provided data confirming the `f_pcnt` configuration anomaly.
*   **Stakeholders (CC'd):** Shubhangi Agrawal, Michael Bui, Allen Umali, Rajiv Kumar Singh, Ravi Goel, **Alvin Choo**.
*   **New Involvement:** Rahul Jain (noted in previous update).

**Main Topic**
Investigation into a 50% drop in product ad impressions and $11k revenue loss since March 17th. The issue was initially suspected to be supply-side pausing but was refuted by Nikhil. Rachit identified the root cause as a configuration anomaly where the `f_pcnt` parameter (requested product count) was set to 1 in over 90% of CATEGORY and 98% of SEARCH page requests, forcing single-product system responses. **Status Update:** The root cause has been confirmed, and the fix is being deployed on March 30th.

**Critical Findings & Data**
*   **Root Cause Confirmed:** A configuration error set `f_pcnt`=1, limiting system responses to one product regardless of inventory.
    *   **CATEGORY Pages:** Requests with `f_pcnt`=1 exceeded 90% (Mar 20–27).
    *   **SEARCH Pages:** Requests with `f_pcnt`=1 exceeded 98% (Mar 20–27).
*   **Context:** While Rachit initially noted 24 paused advertisers generating $11.5k revenue (Mar 1–17), this did not explain the single-SKU output in active campaigns (e.g., Ferrero, Colgate). The `f_pcnt` parameter was the definitive driver.

**Decisions Made**
*   **Resolution Path:** Confirmed the issue is a configuration override rather than supply-side pausing.
*   **Action Executed:** Fix deployment initiated on March 30th by the engineering team based on Nikhil's confirmation.

**Pending Actions & Ownership**
*   **Action:** Monitor system performance following the fix push to ensure multi-SKU responses are restored.
    *   **Owner:** Engineering Team / Technical Owners.
*   **Action:** Verify resolution of single-SKU behavior for active campaigns (e.g., Ferrero, Colgate).
    *   **Owner:** Nikhil Grover, Rachit Sachdeva.

**Key Dates & Deadlines**
*   **Incident Start Date:** March 17th.
*   **Latest Update:** March 30th, 2026 (Fix pushed by team).
*   **Previous Milestones:** March 27th update request; March 27th root cause analysis.
*   **Data Window:** Mar 1–17 (Revenue baseline); Mar 20–27 (Anomaly trend).

**Attachments Referenced**
*   `FPG _ Paused Advertisers (1).xlsx` (Shared by Rachit on Mar 26; reviewed by Nikhil on Mar 27).
*   **New Status:** Fix deployment confirmed via chat update on March 30th.


## [43/44] DPD AI Guild
Source: gchat | Group: space/AAQA5_B3lZQ | Last Activity: 2026-03-30T01:14:44.773000+00:00 | Last Updated: 2026-03-30T02:42:00.029536+00:00
### Daily Work Briefing: DPD AI Guild

**1. Key Participants & Roles**
*   **Michael Bui:** Research/Technical Lead – Introduced the new model release.
*   **Zaw Myo Htet:** Technical Strategy/Engineering – Proposed optimization strategy and cost reduction.
*   **Nicholas Tan:** Strategic Monitor – Highlighted industry trends regarding AI executive automation (Meta).
*   **Oktavianer Diharja:** Engineering Support – Suggested relevant Go skill utility libraries.

**2. Main Topic**
The discussion centered on leveraging **Mistral Small 4** to optimize local knowledge handling via quantization (Unsloth) to reduce RAG dependency, contextualized by Meta's "AI CEO" automation shift. On March 30, the conversation broadened to include engineering tooling, specifically evaluating Go-based skill management libraries that could support future agent implementation.

**3. Pending Actions & Ownership**
*   **Action:** Evaluate feasibility of replacing heavy RAG pipelines with quantized open-weight models to reduce costs.
    *   **Owner:** Zaw Myo Htet
    *   **Context:** Requires further technical assessment based on Unsloth documentation.
*   **Action:** Investigate integration of Mistral Small 4's specific architecture (MoE, 119B total/6B active parameters) into current workflows.
    *   **Owner:** TBD (Team-wide due to recent announcement).
*   **Action:** Analyze the implications of Meta's "AI CEO" model on our autonomous agent roadmap.
    *   **Owner:** Nicholas Tan / Team
    *   **Context:** Assess if similar high-level executive automation patterns are applicable to DPD workflows given the efficiency gains in large-scale operations.
*   **Action (New):** Evaluate utility of `samber/cc-skills-golang` for managing AI agent skills or context within Go-based infrastructure.
    *   **Owner:** Oktavianer Diharja / Engineering Team
    *   **Context:** Review GitHub repository at https://github.com/samber/cc-skills-golang/blob/main/README.md to determine applicability for skill orchestration in the proposed autonomous agent stack.

**4. Decisions Made**
*   **Strategic Alignment:** The team acknowledged that while Mistral Small 4 offers specific architectural benefits for cost reduction, the broader industry (exemplified by Meta) is moving toward high-level autonomous agents. This suggests future DPD AI initiatives should balance model quantization with agent-based autonomy.
*   **Tooling Consideration:** The `samber/cc-skills-golang` library has been flagged for potential use in standardizing skill management for Go-integrated agents, pending technical review by Oktavianer Diharja.
*   **No immediate formal decisions** were recorded regarding the technical implementation of Mistral Small 4; the conversation remains in the exploration phase pending Zaw Myo Htet's feasibility study.

**5. Key Dates & References**
*   **2026-03-17:** Michael Bui announced the release of **Mistral Small 4**.
    *   *Specs:* MoE Architecture, 119B total parameters (6B active), 256k context window, Vision capability.
    *   *Reference:* https://mistral.ai/news/mistral-small-4
*   **2026-03-19:** Zaw Myo Htet suggested utilizing **Unsloth** for quantization to make open-weight models more cost-effective and reduce RAG reliance.
    *   *Reference:* https://unsloth.ai/docs
*   **2026-03-24:** Nicholas Tan shared an article detailing Mark Zuckerberg's launch of an AI CEO bot to manage Meta operations.
    *   *Source:* The Independent (*Mark Zuckerberg builds AI CEO to help him run Meta*).
    *   *Relevance:* Highlights the maturity of agentic workflows for executive-level tasks, providing a benchmark for DPD's long-term automation goals.
*   **2026-03-30:** Oktavianer Diharja recommended the `cc-skills-golang` library for potential skill management integration.
    *   *Reference:* https://github.com/samber/cc-skills-golang/blob/main/README.md
*   **Thread Status:** Active (Last reply noted 22 minutes ago relative to briefing generation).


## [44/44] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/jIquLFJEGIc | Last Activity: 2026-03-30T00:48:49.801000+00:00 | Last Updated: 2026-03-30T02:43:12.741573+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Initiator; coordinator for UAT and status verification.
*   **Michael Bui:** Developer/Lead; delivered Jobs 1–3 in UAT; managing PRD deployment logistics while on leave.
*   **Wai Ching Chan & Daryl Ng:** Acknowledged contributors for the delivery of Jobs 1–3.
*   **De Wei Tey:** Clarification requester regarding use case scope; provided status confirmation.

**Main Topic**
Status verification and UAT scheduling for the "Re-delivery" use case within BCRS, specifically confirming progress on non-RPA backend logic (Jobs 1–3) and BCRS item posting re-delivery.

**Pending Actions & Owners**
*   **UAT Execution:** Conduct User Acceptance Testing for Jobs 1–3 (Order service metadata maintenance, Deposit sales posting update, Duplicate suppression).
    *   *Owner:* Team execution; confirmed by De Wei Tey.
    *   *Timeline:* Scheduled for **Wednesday**.
    *   *Context:* A separate Jira ticket (**DPD-842**) isolates this work from RPA tasks (**DPD-807**).
*   **PRD Deployment:** Execute deployment for non-RPA logic during late evening or night hours.
    *   *Owner:* Michael Bui (executing remotely due to connectivity constraints).
    *   *Timeline:* "Next week" (specific timing subject to connectivity).

**Decisions Made**
*   **Scope Clarification:** The team explicitly clarified that Jobs 1–3 relate to the **"Re-delivery"** use case, specifically rejecting suggestions regarding "pre-order and cancellation after delivery" scenarios.
*   **Status Confirmation:** On March 29, Prajney Sribhashyam queried if the team was on track for BCRS posting re-delivery. De Wei Tey confirmed on March 30 that the project is **"On track"** for Wednesday UAT.
*   **Scope Separation:** The team agreed to proceed with UAT for Jobs 1–3 independently, without dependency on concurrent RPA work.
*   **Deployment Timing:** Michael Bui will handle PRD deployment during off-peak hours (late evening/night) due to upcoming leave and unstable daytime connectivity while on islands.

**Key Dates & Follow-ups**
*   **Conversation Date:** March 28, 2026 (Initial Briefing); March 29–30, 2026 (Status Updates).
*   **Immediate Milestone:** Wednesday UAT for Re-delivery logic.
*   **Future Milestone:** PRD Deployment "next week."

**Relevant References**
*   **Jira Tickets:** DPD-807 (RPA/General), DPD-842 (Non-RPA UAT).
*   **Chat URL:** https://chat.google.com/space/AAQAgT-LpYY
