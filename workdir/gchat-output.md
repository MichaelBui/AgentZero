

## [1/61] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/e4zfXRT2Pnk | Messages: 27 | Last Activity: 2026-03-30T06:29:47.609000+00:00 | Last Updated: 2026-03-30T06:37:06.937752+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Initiator of production testing; managing test data and UAT sheets.
*   **Sneha Parab:** Inventory/Store specialist; confirming store availability, SKU status, and coordinating with Ops.
*   **Andin Eswarlal Rajesh:** Tester; verifying product links and platform compatibility (OG vs. Scango).
*   **Wai Ching Chan:** Advisor on risks regarding shut-down stores during production testing.

**Main Topic**
Production testing strategy for BCRS, specifically addressing the lack of dummy stores/postal codes, SKU availability for smoke tests, and technical validation of product links in a live environment.

**Decisions Made**
*   **Data Migration:** Prajney moved the "Firefighting BCRS" list to the **"BCRS UAT 2026"** spreadsheet (specifically the two tabs mentioned) and added production test cases. This sheet is now the source of truth for testing.
*   **Testing Scope:** Confirmed that currently, only specific SKUs created during the smoke test are available for use in production testing.
*   **Target Date Proposal:** Sneha proposed postponing full production testing to **April 1** (when SKUs can be listed without compliance worries) if current risks are deemed too high. This is pending further review.

**Pending Actions & Owners**
*   **Whitelist Request:** Prajney requested his ID (`prajney.sribhashyam@fairpricegroup.sg`) to be whitelisted while business users collect production IDs. (Owner: Implicitly Ops/Admin, referenced in chat).
*   **SKU Enablement:** Sneha noted that SKUs must be enabled both **in-store and globally** to resolve 404 errors encountered by Prajney. The alignment with the Operations team for this setup is currently missing.
    *   *Action:* Sneha to coordinate Ops team setup.
*   **Platform Coverage:** Andin asked if testing should cover Scango and Preorder; confirmed only current available SKUs will be used, pending Ops alignment.

**Key Dates & Deadlines**
*   **March 30, 2026:** Date of conversation.
    *   Sneha joined an urgent meeting at 06:25 (local time context).
    *   Prajney updated the UAT spreadsheet on Mar 30.
*   **April 1, 2026:** Proposed date for testing to avoid non-compliance risks if immediate production testing is deemed too risky.

**Technical Issues Noted**
*   **404 Errors:** Prajney reported seeing 404 errors on product links; identified as caused by SKUs not being enabled globally and in-store.
*   **Store Configuration:** Risks exist regarding using shut-down FFS stores for testing (potential real customer orders). No dummy postal codes or stores currently exist for this purpose.


## [2/61] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 17 | Last Activity: 2026-03-30T06:28:52.575000+00:00 | Last Updated: 2026-03-30T06:37:51.742423+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (Updated March 30, ~06:32 UTC)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
Instability persists into the morning of **March 30**, extending from early hours (01:53–02:25 UTC) to a new wave between **06:01 and 06:31 UTC**. The issue profile has evolved into sustained cyclical failures affecting Identity APIs, Recommendation Services (Orchid), and Backend Latency. While some alerts recovered by mid-morning, intermittent latency spikes in `post_/new-myinfo/confirm` and error rate fluctuations in `engage-gamification-api` remain active.

**Status Summary & Timeline (March 28 – Mar 30, Early Morning)**
*   **Identity API Instability (`engage-my-persona-api-go` / Squad Dynamics):**
    *   *01:53 – 02:24 UTC:* Recurring high error rates (>0.1%) and latency spikes (P90 up to 2.239s) for `post_/new-myinfo/confirm` and `patch_/user/profile`.
    *   *06:01 – 06:31 UTC (New Activity):*
        *   **06:01:** Discount scheme load failure detected (Metric: 99.89% success). Recovered @ 06:19 UTC.
        *   **06:05:** Severe `put_/user/phone` failure (Metric: 83.333%). Recovered @ 06:21 UTC.
        *   **06:11 & 06:28:** Recurring P90 latency spikes (>1.8s) for `post_/new-myinfo/confirm` (Peak 2.112s @ 06:11; 1.948s @ 06:28).
        *   **06:31:** New P90 latency spike (>1.8s) for `put_/user/residential-address` (Metric: 2.07s).
*   **Gamification & Recommendation Services:**
    *   **Orchid/Boughtbought (`frontend-gateway` / Squad Journey):** Dip at **06:06 UTC** (97.917% success) recovered by **06:16–06:17 UTC**.
    *   **Gamification (`engage-gamification-api` / Squad Dynamics):** High error rate triggered @ 06:08 and again @ 06:17 (Peak 0.296%). Recovered @ 06:27 UTC.
*   **Layout Services:**
    *   `lyt-p13n-layout`: P99 latency spike (>1.8s) for `get_/v1/home` at **06:06 UTC** (Metric: 2.009s). Recovered @ 06:09 UTC.

**Pending Actions & Ownership**
*   **Investigate Identity API Recurrence:** Analyze repeated P90 latency spikes in `post_/new-myinfo/confirm` and `put_/user/residential-address` occurring between 06:11–06:31 UTC, alongside the earlier 02:07–02:25 window. Owner: **Squad Dynamics**.
*   **Address New Endpoint Failures:** Investigate sudden failure rates in `put_/user/phone` (06:05) and `get_/user/profile/myinfo` (06:01). Owner: **Squad Dynamics**.
*   **Correlate Gamification & Gateway Latency:** Review the intermittent error spikes in `engage-gamification-api` and Orchid service dips from 06:06–06:28 UTC. Owner: **Squad Journey**, **Squad Dynamics**.

**Decisions Made**
*   **Severity Escalation:** Incidents remain critical due to multi-squad recurrence extending from Mar 28 through morning of Mar 30 (latest activity 06:01 – 06:31 UTC).
*   **Pattern Continuity:** The ecosystem instability has solidified into a "sustained cyclical failure" model. New latency issues in residential address updates and phone number writes have joined existing Identity/Recommendation failures.

**Key Dates & Follow-ups**
*   **Active Window:** March 28–30 (UTC). Recent critical activity: **06:01 – 06:31 UTC**.
*   **Reference Links:**
    *   `get_/user/profile/myinfo` Monitor #50879029 (Latest Trigger: 06:01, Value 99.89%)
    *   `put_/user/phone` Monitor #17447668 (Latest Trigger: 06:05, Value 83.333%)
    *   `post_/new-myinfo/confirm` Latency Monitor #50879027 (Latest Trigger: 06:28, P90: 1.948s)
    *   `put_/user/residential-address` Monitor #17447643 (Latest Trigger: 06:31, P90: 2.07s)
    *   `engage-gamification-api` Error Rate Monitor #92939290 (Latest Trigger: 06:17, Value 0.296%)


## [3/61] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/rKtZEQsyOFI | Messages: 20 | Last Activity: 2026-03-30T06:11:55.755000+00:00 | Last Updated: 2026-03-30T06:38:10.067381+00:00
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


## [4/61] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/z2zSDKRl4Vc | Messages: 3 | Last Activity: 2026-03-30T06:06:48.755000+00:00 | Last Updated: 2026-03-30T06:38:28.447290+00:00
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


## [5/61] QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs | Messages: 3 | Last Activity: 2026-03-30T06:04:05.263000+00:00 | Last Updated: 2026-03-30T06:39:03.366336+00:00
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
*   **Others:** Piraba Nagkeeran, Andin Eswarlal Rajesh, **Kadar Sharif**.

**Main Topics & Discussion**
1.  **LinkPoints Regression Failure (Critical Update):** On **27 Mar**, Milind Badame reported a complete failure of all LinkPoints tests due to a `500` error at the CLS Award Balance API step: *"Transaction posting failed"*. *Status:* Critical/Blocked. Discussion ongoing with @Pandi.
2.  **iOS SnG Flow QR Loading Issue (New):** On **27 Mar**, Madhuri Nalamothu reported a random issue in iOS where scanning the QR code in the SnG Flow gets stuck on loading forever. Observed on iOS 15 and 17. *Status:* Investigating flakiness. *Owner:* @Pandi.
3.  **DC Membership Subscription Issue (Updated):** On **30 Mar**, Madhuri Nalamothu reported that DC membership subscription issues affect **both new and existing users**. Previously logged as a logic discrepancy, this is now confirmed as an active failure impacting the user base across the board. *Owner:* @Kadar Sharif.
4.  **Express Cart Service Fee Waiver:** Milind Badame reported service fees incorrectly waived in Express cart mode (Subtotal $37.87) on **26 Mar**. *Status:* Open/Investigating. *Owners:* @Daryl Ng, @Andin Eswarlal Rajesh.
5.  **Search Indexing Failure:** Critical failure where "Ninben Tsuyu No Moto Seasoning Soy Sauce - Triple Strength" (Hyper Changi) is invisible in search despite stock availability. *Status:* Urgent investigation needed. *Owners:* @Daryl Ng, @Yangyu Wang.
6.  **OmniHome Christmas Tiles Anomaly:** "Dressed up" Christmas tiles visible for FoodTakeaway on OmniHome in March. *Status:* Investigating visual consistency.
7.  **PreOrder Tile Permanency:** New PreOrder tile flagged on **25 Mar**; E2E test updates pending confirmation of permanency from Dev/Product.
8.  **LinkPay Receipt Banner Missing:** Android banner missing in LinkPay receipts; investigation requested with @Tiong Siong Tee.
9.  **E-Voucher Application Error:** `404 Invalid voucher` error reported by Milind Badame on **24 Mar**; backend logic failure. *Owner:* @Zaw Myo Htet.
10. **Cart Page Logic Flaw (Critical):** Komal Ashokkumar Jain reported cart items "stick" when switching to Express delivery, allowing ineligible orders for 1HD. Reported **20 Mar**.
11. **Android OTP Blank Screen:** Blank screen on Android v12 and below; investigation requested with @Tiong Siong Tee.

**Pending Actions & Ownership**
*   **LinkPoints API Resolution:** Investigate "Transaction posting failed" error at CLS Award Balance API immediately. *Owner: @Pandi, Dev Team.* **(High Priority)**
*   **iOS SnG Flow Loading:** Investigate random/stuck loading issue during QR scanning on iOS 15/17 in SnG Flow. *Owner: @Pandi, Mobile Team.* **(New High Priority)**
*   **DC Membership Fix:** Resolve subscription failures impacting **all users** (new and existing). *Owner: @Kadar Sharif.* **(Critical Update)**
*   **Express Cart Service Fee:** Verify why service fees are waived in Express cart mode. *Owners: @Daryl Ng, @Andin Eswarlal Rajesh.*
*   **Search Indexing Failure:** Resolve search failure for "Ninben Tsuyu No Moto Seasoning Soy Sauce - Triple Strength" at Hyper Changi. *Owners: @Daryl Ng, @Yangyu Wang.*
*   **PreOrder Tile Strategy:** Confirm if PreOrder tile is permanent to decide on E2E test updates. *Owner: @Daryl Ng / QA Team.*
*   **Cart Express Delivery Logic:** Resolve cart alignment and delivery mode eligibility logic. *Owners: Komal Ashokkumar Jain, Daryl Ng, Andin Eswarlal Rajesh.*
*   **LinkPay Receipt Banner & Android OTP:** Fix missing banner and blank screen issues. *Owner: @Tiong Siong Tee.*

**Decisions Made**
*   Ad slot changes proceed; known test impacts acknowledged.
*   No resolution yet on LinkPoints, iOS SnG Flow loading, Express cart service fee, Search indexing, Cart eligibility logic, or tile anomalies.
*   **DC Membership Issue:** Escalated to @Kadar Sharif for immediate investigation regarding the scope affecting existing users.

**Key Dates & Deadlines**
*   **5 Mar:** Load testing window (completed).
*   **16 Mar:** DC membership logic discrepancy logged.
*   **20 Mar:** Critical Express delivery bug flagged.
*   **24 Mar:** E-Voucher error and Android OTP issue raised.
*   **25 Mar:** OmniHome tiles, LinkPay receipts, Search indexing, PreOrder tile issues flagged.
*   **26 Mar:** Express cart service fee discrepancy reported.
*   **27 Mar:** LinkPoints API failure (02:47 UTC) and iOS SnG Flow issue observed.
*   **30 Mar:** DC membership subscription issue confirmed for existing users; discussion active with @Kadar Sharif (Last reply 5 min ago).


## [6/61] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-03-30T05:36:57.545000+00:00 | Last Updated: 2026-03-30T06:39:36.072819+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Update)**
**Date:** March 30, 2026 (Early Morning Shift)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 708

### Key Participants & Roles
*   **System/Tool:** Datadog App (Automated Monitoring)
*   **Notification Channel:** `@hangouts-ShoppingCartNotification`
*   **Ownership Teams:** `dpd-pricing`, `dpd-pricing-cart`.

### Main Topic
Instability persists in `frontend-gateway` and `st-cart-prod`. Following the critical cascade on March 29, activity extends through early morning hours (01:10–05:36 UTC). The failure mode continues to oscillate across **Checkout**, **Cart Update** (`post /api/cart`), and **Wish List** endpoints. A new degradation pattern is confirmed in `st-cart-prod` success rates, distinct from the persistent latency issues on `frontend-gateway`.

### Incident Timeline & Actions
**Previous Context:**
*   *Extended activity from March 20 through March 29.*

**New Activity (March 30 UTC)**
*   **01:10–05:26 UTC:** Continuous oscillation on Wish List endpoints (`get` and `put`). Notable P90/P99 spikes recorded at 01:14, 01:47, 02:03, and a severe surge at **04:12 UTC** (P99: **10.555s**; Monitor `21245701`).
*   **01:12–02:19 UTC:** Checkout success rate dipped to 99.87%, followed by a critical drop on `st-cart-prod` (Monitor `22710472`) to 99.611%.
*   **05:26–05:36 UTC:** New degradation detected on `st-cart-prod`. Monitor `22710472` triggered at 05:26 with a success rate of **99.719%** (Threshold <99.9%), recovering to 100.0% at 05:36.

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** The incident window has extended to March 30, 05:36 UTC. A second distinct degradation event on `st-cart-prod` success rates occurred at 05:26 UTC.
*   **Immediate Action Required:** Correlate trace data for the full morning cascade (01:10–05:36 UTC), specifically investigating the 04:12 UTC P99 spike (Event `8566128665676671583`) and the 05:26 UTC success rate drop (Event `8566204001990943787`).

### Decisions Made
*   **Priority Escalation:** Status remains **"Critical Incident"**. Activity is continuous from March 20 through at least 05:36 UTC on March 30.
*   **Focus Shift:** Analysis must prioritize `st-cart-prod` success rate degradation (Monitor `22710472`) alongside the severe latency oscillation on `frontend-gateway`.
*   **Metric Update:** Confirmed rotating failure mode: Cart Update P99 reached 10.555s; Checkout Success Rate dropped to 99.87%; Wish List GET P90 peaked at 2.009s; `st-cart-prod` success rate dropped to 99.611% and again to 99.719%.

### Key Dates & Follow-ups
*   **Critical Window:** Extended activity from March 20 through at least March 30, 05:36 UTC.
*   **Follow-up:** Immediate trace correlation for the early morning cascade to determine if root cause is environmental or traffic-based before shift handover.

### References
*   **Active Monitors:** `21245706` (Wish List PUT P90), `21245708` (Checkout Success Rate), `21245713` (Cart Update P99), `21245720` (Wish List GET P90), `22710472` (`st-cart-prod` Success Rate), `21245701` (Wish List PUT P99).
*   **Service Tags:** `service:frontend-gateway`, `service:st-cart-prod`, `team:dpd-pricing`.


## [7/61] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Messages: 16 | Last Activity: 2026-03-30T05:12:32.783000+00:00 | Last Updated: 2026-03-30T06:40:33.751281+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Mar 30, 05:12 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`.
*   **Escalations:** `@oncall-dpd-staff-excellence-pdm`, `@hangouts-GT-Search-DatadogAlerts`, `@hangouts-GT-Discovery-DatadogAlerts`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Retail Media.

**Main Topic**
**P3 INCIDENTS (RESOLVED):** Two transient incidents triggered on Mar 30 but have since recovered.
1.  **`frontend-gateway`:** Browse banner page success rate dropped below 99.9% at 04:38 UTC (Metric: 98.182%). Recovered at 04:48 UTC (Metric: 100.0%). Monitor ID `17448322`.
2.  **`go-catalogue-service`:** P3 latency alert for resource `get_/category/_id` triggered at 04:52 UTC (P90 Latency: 2656ms). Recovered at 05:12 UTC (P90 Latency: 883ms). Monitor ID `17447967`.

**Resolved Incidents:**
*   **`sku-store-attribute`:** Triggered Mar 30, 00:53 UTC; Recovered Mar 30, 01:01 UTC (Monitor ID `20382848`).
*   **`marketing-service`:** Throughput anomaly triggered Mar 30, 04:03 UTC (P4); Recovered Mar 30, 05:02 UTC (Monitor ID `17447110`). Previous P4 incident from Mar 29 also resolved.

**Pending Actions & Ownership**
*   **Action:** **INVESTIGATE CRITICAL ERRORS (`fp-search-indexer`):** [Status: ACTIVE] Address P2 alert for >0 errors on `env:prod`.
    *   **Owner:** Product Data Management On-Call.
    *   **Status:** **RE-TRIGGERED (Mar 29, 21:13 UTC).** Metric value reached 1.0. Active since Mar 18; no resolution achieved. Monitor ID: `17447691`.

**Decisions Made**
*   The `fp-search-indexer` incident remains the sole critical priority with trace errors at 100%. Immediate investigation of Datadog, K8s, and Runbooks is mandated.
*   Recent transient issues regarding `frontend-gateway` banner success rates and `go-catalogue-service` latency have self-corrected; no immediate action required, but monitoring continues for recurrence.
*   Throughput anomalies on `marketing-service` (04:03–05:02 UTC) have resolved automatically.

**Key Dates & Follow-ups (Mar 29–30, 2026)**
*   **Service: `fp-search-indexer` (P2 - Product Data Management) [ACTIVE CRITICAL]**
    *   *Latest Timeline:* Active since Mar 18; Re-triggered Mar 29 (21:13 UTC).
    *   *Links:* [Datadog](https://app.datadoghq.eu/monitors/17447691) | [K8s](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/fp-search-indexer/overview) | [Runbook](https://ntuclink.atlassian.net/wiki/spaces/SR/pages/2001831558/Support+Run+book)
*   **Service: `sku-store-attribute` (P3 - Grocery Discovery) [RESOLVED]**
    *   *Latest Timeline:* Re-triggered Mar 30 (00:53 UTC); Recovered Mar 30 (01:01 UTC).
    *   *Links:* [Datadog](https://app.datadoghq.eu/monitors/20382848)
*   **Service: `marketing-service` (P4 - Retail Media) [RESOLVED]**
    *   *Latest Timeline:* Triggered Mar 30 (04:03 UTC); Recovered Mar 30 (05:02 UTC).
    *   *Links:* [Datadog](https://app.datadoghq.eu/monitors/17447110) | [K8s](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview) | [Runbook](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book)
*   **Service: `frontend-gateway` (P3 - Grocery Discovery) [RESOLVED]**
    *   *Latest Timeline:* Triggered Mar 30 (04:38 UTC); Recovered Mar 30 (04:48 UTC).
    *   *Links:* [Datadog](https://app.datadoghq.eu/monitors/17448322)
*   **Service: `go-catalogue-service` (P3 - Product Data Management) [RESOLVED]**
    *   *Latest Timeline:* Triggered Mar 30 (04:52 UTC); Recovered Mar 30 (05:12 UTC).
    *   *Links:* [Datadog](https://app.datadoghq.eu/monitors/17447967) | [K8s](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/go-catalogue-service/overview) | [Runbook](https://ntuc.atlassian.net/wiki/spaces/DIS/pages/2646212686/Catalogue+Service)

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c


## [8/61] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Messages: 8 | Last Activity: 2026-03-30T04:27:22.508000+00:00 | Last Updated: 2026-03-30T06:42:01.806493+00:00
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
*   **Mar 24–25, 2026:** Incident `story_key`: `de0cbb14-ade3-5de2-bfab-cbddd41da779` (~3h 51m). Status: **Resolved**.
*   **Mar 25, 2026:** Incident `story_key`: `978f6328-424c-53dd-83c8-6411c3aa2158`. Recovered at 12:09 UTC. Duration ~24 hours. Status: **Resolved**.
*   **Mar 26, 2026:** Incident `story_key`: `7b73b037-696a-5016-bca4-5c22e31b6245`. Duration ~3 hours 22 minutes. Status: **Resolved**.
*   **Mar 27, 2026:** Incident `story_key`: `f5d0894a-4a42-515d-985f-d06644833529`. Recovered at 17:37 UTC. Status: **Resolved**.

**Current Active/Resolved Sequence (Mar 28–30):**
*   **Incident 1 (Resolved, Mar 28):** Triggered March 28 at 03:26:22 UTC. Story Key: `8874d9ed-c1b1-5d8a-960b-85d280269164`. Recovered at 07:17:22 UTC. Status: **[P3] Recovered**.
*   **Incident 2 (Resolved, Mar 29):** Triggered March 28 at 21:27:22 UTC. Story Key: `784f6ec6-03de-5cee-a4e5-9fa93fd78209`. Recovered on **March 29, 2026, at 00:47:23 UTC**. Status: **[P3] Recovered**.
*   **Incident 3 (Active, Mar 30):** Triggered **March 30, 2026, at 04:27:22 UTC**. Story Key: `acd815df-528d-54a8-b915-069f6ae44fcc`.
    *   **Error Message:** "Datadog is unable to process your request."
    *   **Status:** **[P3] Triggered**.

### Pending Actions & Ownership
*   **Current Status:** A new incident (`acd815df...`) has triggered as of March 30, 2026. This follows the standard pattern of transient infrastructure degradation.
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Action Required:** Monitor duration against the 6-hour escalation threshold. If unresolved by ~10:27 UTC on March 30, escalate to SRE/Platform Engineering per protocol.

### Decisions Made
*   **Escalation Status:** No immediate escalation; incident is within standard variance window for this specific error profile ("unable to process your request").
*   **Protocol:** Escalation remains the protocol if resolution time exceeds 6 hours or if similar error messaging persists without self-resolution.

### Key Dates & Follow-ups
*   **Latest Event:** March 30, 2026, at 04:27:22 UTC (New Trigger).
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Continue standard surveillance. The recurrence of the "unable to process" message confirms persistent pipeline degradation trends. Note that the Mar 25 incident (~24h) remains a significant outlier for comparison against current duration.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Datadog Monitor Link:** [View in Datadog](https://app.datadoghq.eu/monitors/17447511)
*   **Latest Incident (Active):** https://app.datadoghq.eu/monitors/17447511?group=story_key%3Aacd815df-528d-54a8-b915-069f6ae44fcc&from_ts=1774843851000&to_ts=1774845051000&event_id=8566144087599989089

### Monitor Configuration
*   **Query:** `events("source:watchdog (story_category:infrastructure -story_type:(tcp_retrans_jump OR full_disk_forecast)) env:(PROD OR production OR prod)").rollup("count").by("story_key").last("30m") > 0`


## [9/61] FPG Everyone - General
Source: gchat | Group: space/AAAAjDYVcBU | Messages: 8 | Last Activity: 2026-03-30T03:49:03.207000+00:00 | Last Updated: 2026-03-30T06:43:43.043037+00:00
**Daily Work Briefing: FPG Everyone Chat Summary (Updated)**
**Date Range:** March 3 – March 30, 2026
**Source:** Google Chat (FPG Everyone - General)

### Key Participants & Roles
*   **Siti Nabilah:** Day of Service Campaign Promoter.
*   **Jasmine Neo:** Senior Executive, E-Commerce (Ordering Management).
*   **Keith Lee:** Industry Trends Monitor.
*   **Melissa Lim:** Community Engagement Lead.
*   **Maisy Heeng:** FPG Food Services Brand Lead.

### Main Topics
1.  **Digital Access Rollout:** Schedule confirmed and executed (C-suite/HR/Finance on Mar 16; Customer/Marketing/E-Commerce on Mar 23; Remaining Hub staff by Mar 30). User guide distributed.
2.  **Media Collaboration – "Bowl of Love":** Final episodes featuring Tyler Ten, Tasha Low, and Xiang Yun are officially live following the March 21 launch. The story focuses on warmth and healing with fresh Malaysian pork.
    *   **Platform:** @mediacorp.re.dian TikTok (`https://vt.tiktok.com/ZSusN9b4n/`).
3.  **Industry Recognition:** Lau Pa Sat's "Spin for your Huat" campaign was featured by Campaign Asia as a top CNY campaign to watch in 2026, competing alongside global heavyweights like Nike and Apple.
    *   **Source:** `https://www.campaignasia.com/article/brands-launch-campaigns-celebrating-chinese-new-year-2026/n554u1b7maurkcmkwcd29mooi2`
4.  **FairPrice Heartland Hits Launch (Mar 27):** A new community storytelling contest launched to turn neighbourhood stories into music.
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
*   **Linkpoints Redemption (Owner: All Staff):** Redeem $0.99 rewards immediately. Collection deadline is **April 5, 2026**.
    *   **Link:** `https://go.fpg.sg/ki0bdx`
*   **Shorty Awards Voting (Owner: All Staff):** FPG has two campaigns shortlisted for the 18th Annual Shorty Awards under "Audience Honor." Action: Create a personal email account, vote daily from today until **April 8**, casting one vote per category per day.
*   **Volunteer Engagement (Owner: All Staff):** Siti Nabilah shared a "Volunteer Spotlight" featuring Jasmine Neo. Staff encouraged to sign up for upcoming opportunities.
    *   **Link:** `https://forms.gle/UkyQDagmDy4mcY7K7`
*   **Sensory Test Sign-ups (Owner: All Staff):** Chapati screening form remains open (`https://forms.gle/DFYrahZcvhtcoJ9R7`). Frozen Snacks sign-up is closed.
*   **Heartland Hits Participation:** Staff encouraged to submit stories and rally regional crew before April 5.

### Decisions Made
*   **Awards Campaign:** Strategic decision to mobilize staff for Shorty Awards voting until April 8.
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


## [10/61] RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Messages: 36 | Last Activity: 2026-03-30T03:21:01.456000+00:00 | Last Updated: 2026-03-30T06:44:16.810694+00:00
**Daily Work Briefing: Automated Test Results Summary (RMN Notification)**

**Key Participants & Roles**
*   **Collection Runner App:** Automated testing agent executing API suites.
*   **Webhook Bot:** Reporting mechanism; consistently returning "unable to process your request" on all notifications through March 30, 2026.
*   **Parties Involved:** System-generated notification log only.

**Main Topic/Discussion**
Automated nightly API test executions across `promo-service`, `marketing-personalization-service`, and `marketing-service` in the **staging** environment. Monitoring period spans March 12 through **March 30, 2026**. Execution windows occur at approximately 01:05 UTC (morning), 02:30/02:31 UTC (midnight), and **03:20/03:21 UTC** (early morning).

**Test Execution Status & Anomalies**
*   **`marketing-service` Stability Confirmation:** The streak of resolution continues through March 30.
    *   **March 30, 01:05 UTC:** Executed successfully with **52 API Tests Passed / 0 Failed** and **20 Contract Tests Passed / 0 Failed**. (Total Requests: 17 API, 16 Contract).
    *   **Historical Context:** Recurring instability persisted from March 17 through early March 25. A temporary stabilization occurred on March 25; the morning failure streak was broken on March 26. Stability confirmed for March 26–30.
*   **`promo-service`:** Confirmed stable on March 30 at **02:31 UTC**. The latest run showed **10 API Tests Passed / 0 Failed** and **6 Contract Tests Passed / 0 Failed**. (Total Requests: 3 each). Stability confirmed for March 26–30.
*   **`marketing-personalization-service`:** New data confirms a successful run at **03:21 UTC on March 30**.
    *   **API Contract Tests:** 125 Passed / 0 Failed (Total Requests: 21).
    *   **API Tests:** 96 Passed / 0 Failed (Total Requests: 21).
    *   This updates the previous status, confirming stability for March 30 in addition to runs on March 27–29.

**Pending Actions & Ownership**
*   **Webhook Bot Remediation (High Priority):** The bot failed to process requests in every notification cycle from March 12 through the latest log on **March 30 at 03:21 UTC**. Immediate attention is required from DevOps or Automation Infrastructure.
*   **Verify `marketing-service` Stability:** Engineering must continue monitoring subsequent runs to confirm the resolution of early-morning flakiness observed between March 17–25 was permanent.

**Decisions Made**
*   No human decisions recorded; all entries are automated system outputs.

**Key Dates & Deadlines**
*   **Failure Window (Historical):** Instability noted on March 12, 13, and persistently from **March 17 through March 25**.
*   **Current Status:** Successful runs observed on March 26–30 across all three services.
    *   `marketing-service`: Passed at 01:05 UTC (March 26–30).
    *   `promo-service`: Passed at 02:30/02:31 UTC (March 26–30).
    *   `marketing-personalization-service`: Passed at 03:20/03:21 UTC (March 27–30).
*   **Monitoring Period:** Data covers runs from **March 12, 2026**, through **March 30, 2026**.

**Resource Info**
*   **Message Count:** 177 notifications logged in the space (Updated from 168).
*   **URL:** https://chat.google.com/space/AAQA85dw4So


## [11/61] @omni-ops #standup - Mar 30
Source: gchat | Group: space/AAQAPG9qdz4 | Messages: 6 | Last Activity: 2026-03-30T03:15:09.812000+00:00 | Last Updated: 2026-03-30T06:44:34.295102+00:00
**Daily Work Briefing: #standup (omni-ops)**
**Date:** March 30, 2026
**Channel:** Google Chat (#standup) | [Link](https://chat.google.com/space/AAQAPG9qdz4)

### **Key Participants & Roles**
*   **Daryl Ng:** Facilitator; initiated the meeting, followed up on attendance, and provided final confirmation.
*   **Yangyu Wang:** Participant; confirmed meeting status.
*   **Rohit Pahuja:** Presenter/Engineer; reported on completed tasks and upcoming plans.
*   **Sundy Yaputra:** Mentioned as an invitee.
*   **Hanafi & Sneha:** External colleagues referenced regarding task delegation.

### **Main Topic**
The team convened for the daily standup to address attendance issues and review technical updates from Rohit Pahuja. The discussion centered on the successful removal of redundant steps in the Backoffice deployment pipeline following the resolution of flaky tests, culminating in Daryl Ng's confirmation of the update.

### **Pending Actions & Ownership**
*   **Discuss Hanafi-related work:** Rohit Pahuja is scheduled to discuss this with Sneha today.
    *   *Context:* This discussion was necessitated because **Hanafi** is currently on leave.
*   **Assign task for deprecated pages:** Sneha will assign Rohit the specific task of removing deprecated pages from Backoffice.

### **Decisions Made**
*   No new technical decisions were recorded in this log. The conversation confirmed that all previously mentioned flaky test cases are now passing in a single run, validating the removal of the "Backoffice PR rerun step."
*   Daryl Ng verbally approved the update ("okay sounds good") at 03:15 UTC on March 30, finalizing the status discussion.

### **Key Dates & Follow-ups**
*   **March 30, 2026:** Rohit Pahuja missed the initial standup at 02:01 UTC due to another discussion. He provided his status update later that morning (approx. 02:28 UTC) after Daryl Ng requested updates regarding his absence.
*   **March 30, 2026 (03:15 UTC):** Daryl Ng confirmed the update with "okay sounds good."
*   **Today (March 30):** Rohit is to finalize discussions with Sneha and receive task assignments for the Backoffice cleanup.

### **Summary of Status**
Rohit Pahuja successfully submitted a Pull Request (PR) to remove the Backoffice PR rerun step, citing that all flaky tests are now stable in one run. Despite missing the initial sync due to conflicting meetings, Rohit communicated his progress and immediate schedule regarding Hanafi-related dependencies and Backoffice maintenance. The update was formally acknowledged by Daryl Ng at 03:15 UTC on March 30, confirming alignment with the team's objectives.


## [12/61] DPD x DPM
Source: gchat | Group: space/AAQApzD7Im0 | Messages: 3 | Last Activity: 2026-03-30T03:05:18.172000+00:00 | Last Updated: 2026-03-30T06:45:02.800302+00:00
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


## [13/61] Omni Fairmily
Source: gchat | Group: space/AAAAQuMQ3Bs | Messages: 1 | Last Activity: 2026-03-30T02:53:32.229000+00:00 | Last Updated: 2026-03-30T06:45:28.539649+00:00
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


## [14/61] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY | Messages: 6 | Last Activity: 2026-03-30T02:44:26.559000+00:00 | Last Updated: 2026-03-30T06:45:48.877489+00:00
**Updated Briefing: BCRS Firefighting Group**
**Date:** March 30, 2026 (Latest activity: ~02:44 AM)
**Source:** Google Chat Space & Shared UAT Tracker (81 messages total)

### **Key Participants & Roles**
*   **Prajney Sribhashyam:** Project Lead/Test Coordinator.
*   **De Wei Tey / Michael Bui / Wai Ching Chan:** Finance/SAP, Re-delivery specialists, and Technical Integration.
*   **Dany Jacob / Eswarlal Rajesh / Sneha Parab:** Active test participants and finance coordinators.
*   **Alvin Choo:** Status reporting lead (monitoring Starship channel updates).

### **Main Topics**
1.  **Production Testing Initiation:** Following UAT readiness, the group has shifted focus to **Production Testing**. A dedicated thread was opened on March 30 with 26 replies and active engagement from 25 of 39 members.
2.  **Re-delivery Use Case (DPD-807):** While initial grooming for this use case was scheduled for March 28, the immediate priority is now validating execution in Production. The workflow requires Order service to maintain 'Deposit posted to SAP' metadata and RPA to charge original payment methods while suppressing duplicate BCRS deposit postings.
3.  **Status Reporting:** Alvin Choo continues to monitor visibility (previously noted as 10 of 39 members; now 25 of 39 in the Production Testing thread) following recent Starship channel changes.

### **Decisions & Updates**
*   **Scope Shift:** The timeline has moved from March 28 UAT validation to immediate **Production Testing**. Michael Bui and Wai Ching Chan remain critical for assisting with the Re-delivery case logic during this phase.
*   **UAT Confirmation:** Jobs 1 to 3 were previously confirmed ready in UAT as of March 28, serving as the gateway to the current Production Testing phase.
*   **Thread Activity:** The "Production Testing" thread (March 30) indicates high engagement with 26 replies, suggesting active troubleshooting or execution is underway.

### **Pending Actions & Owners**
| Action Item | Owner(s) | Status/Context |
| :--- | :--- | :--- |
| **Execute Production Testing** | Prajney Sribhashyam / Team | **Active:** High-engagement thread opened March 30; 25 members viewing. Immediate focus on live environment validation. |
| **Re-delivery Logic Validation** | Michael Bui / Wai Ching Chan / De Wei Tey | **In Progress:** Transitioning from grooming (March 28) to executing the RPA and metadata workflow in Production. |
| **Overall Status Update** | Prajney Sribhashyam / Team | **Pending:** Provide comprehensive update to Alvin Choo regarding Starship channel changes and current Production Testing progress. |
| **RPA Work Validation** | De Wei Tey / Wai Ching Chan | **Active:** Confirm RPA execution success in Production now that jobs are live. |

### **Key Dates & Deadlines**
*   **March 30 (Today):** Current active date for Production Testing thread and RPA execution validation.
*   **Historical Note:** The original SAP Deposit API development deadline of Feb 20 remains noted as missed/risked; current effort focuses on resolving specific re-delivery logic gaps via live testing.

### **Historical Context Retained**
*   Existing e-comm test accounts remain unusable for Pre-order staff app; new BCRS CF items and specific GWP SKUs are required.
*   Deposit SKU linking investigation continues due to failure to link post-publishing.
*   Previous Re-delivery flow testing experienced audio issues on March 16; current Production effort aims to resolve logic gaps via the grooming session and live validation.


## [15/61] @ecom-ops #standup - Mar 30
Source: gchat | Group: space/AAQAqo-_GgY | Messages: 6 | Last Activity: 2026-03-30T02:40:55.376000+00:00 | Last Updated: 2026-03-30T06:46:04.789139+00:00
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


## [16/61] [Prod Support] Ecom FFS Ops
Source: gchat | Group: space/AAAAde_cYKA | Messages: 11 | Last Activity: 2026-03-30T02:40:20.597000+00:00 | Last Updated: 2026-03-30T06:46:30.058567+00:00
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


## [17/61] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/jfuh2YauMzM | Last Activity: 2026-03-30T02:15:27.555000+00:00 | Last Updated: 2026-03-30T02:39:32.004967+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Michael Bui:** Developer responsible for root cause analysis, PR merge, and post-deployment verification.
*   **Alvin Choo:** Primary recipient; coordinated immediate review and deployment execution.
*   **Daryl Ng:** Team lead for `website-service`; confirmed availability to review and deploy.

**Main Topic**
Immediate resolution of the RMN incident in the `website-service` module, shifting from a scheduled Monday deployment to an urgent same-day (March 30) production deployment following team availability confirmation.

**Pending Actions & Ownership**
*   **Post-Deployment Verification:** Michael Bui to verify that search and category pages display more than one ad (specifically slots 1, 4, 8, etc.) immediately after deployment. [Owner: Michael Bui]
*   **Deployment Execution:** Triggered via Bitbucket Pipelines; Alvin Choo/Daryl Ng to execute or monitor the live environment status. [Owner: Alvin Choo / Daryl Ng]

**Decisions Made**
*   **Deployment Timing Revised (Immediate):** The deployment window was advanced from "Monday evening/night" to **today, March 30, 2026**. This change occurred after Alvin Choo asked for immediate assistance and Daryl Ng confirmed availability ("Yeahhh!").
*   **PR Merge Confirmed:** Michael Bui has merged the Pull Request (PR). The PRD deployment pipeline is active at: `https://bitbucket.org/ntuclink/website-service/pipelines/results/3983`.
*   **Verification Criteria:** Upon completion of deployment, the team must ensure the fix resolves the ad count issue correctly on live pages.

**Key Dates & References**
*   **Incident Date/Time:** March 27, 2026 (14:50 UTC).
*   **UAT Confirmation Timestamp:** March 28, 2026 (03:08 UTC) – Michael Bui confirmed UAT success.
*   **Deployment Decision Timestamp:** March 30, 2026 (01:12–02:04 UTC) – Alvin Choo requested help; Daryl Ng agreed; deployment triggered.
*   **PR Link:** https://bitbucket.org/ntuclink/website-service/pull-requests/652/overview
*   **Pipeline Link:** https://bitbucket.org/ntuclink/website-service/pipelines/results/3983
*   **Jira Ticket:** DPD-715 (https://ntuclink.atlassian.net/browse/DPD-715)
*   **Service Scope:** `website-service`.

**Note on Previous Assumptions**
The previous plan to delay deployment until Monday evening or office hours has been superseded. Due to the urgency expressed by Alvin Choo and immediate availability from Daryl Ng's team, the PR was merged and the production deployment process initiated on March 30, 2026, in the early morning UTC timeframe. The team is now awaiting confirmation of successful live deployment before proceeding with final functional checks.


## [18/61] Web Chapter
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


## [19/61] Alvin Choo
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


## [20/61] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Last Activity: 2026-03-30T02:05:50.029000+00:00 | Last Updated: 2026-03-30T02:40:44.034266+00:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
Production instability in the Mirakl integration persists, extending the streak to **13 days (March 17–29)**. While late March 29 saw critical errors on `fni-offer` and `fni-order-create`, a new wave of alerts occurred early morning **March 30**. The `picklist-pregenerator` latency issue has re-triggered with sustained degradation.

**Incident Summary & Timeline**
*   **Service: `picklist-pregenerator` (Latency Warning) – Late Evening (Mar 29)**
    *   **Trigger:** P2 Warning "taking too long to complete" at **19:01 UTC** (approx.). Metric value: **3609.523s**. Monitor ID `20383097`. Confirms sustained degradation from March 27.

*   **Service: `fni-offer` (FairPrice Route) – Late Evening (Mar 29)**
    *   **Trigger:** P2 "Exception Occurred at FairPrice Route" at **21:14:01 UTC**.
    *   **Recovery:** Returned to normal by **21:18:57 UTC**. Duration: ~5 minutes.

*   **Service: `fni-order-create` (DBP/API Errors) – Late Evening (Mar 29)**
    *   **Trigger Window:** Simultaneous P2 triggers starting at **21:14:52 UTC** affecting DBP fetching and API calls.
    *   **Recovery:** All monitors returned to normal by **21:20:05 UTC**. Duration: ~5 minutes.

*   **Service: `fpon-seller-sap-picklist-reporter` (P1 Incident) – Evening (Mar 27)**
    *   Triggered P1 alert "SAP authentication failed" at **19:12:15 UTC**. Recovered by **19:17:15 UTC**.

*   **Service: `fni-order-create` (Mirakl Route) – Early Morning (Mar 30)**
    *   **Trigger Window:** New P2 triggers starting at **02:00:39 UTC**.
        *   "Exception Occurred At Mirakl Route" (Monitor ID `17447918`).
        *   "Error while calling APIs" (Monitor ID `17447928`).
    *   **Recovery:** Both monitors returned to normal by **02:05:50 UTC**. Duration: ~5 minutes.

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of the early morning Mar 30 cluster affecting `fni-order-create` (Mirakl Route and API errors).
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Analyze underlying causes for the P1 SAP authentication failure on `fpon-seller-sap-picklist-reporter` (Mar 27) to prevent recurrence.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Address critical latency in `picklist-pregenerator`. The recurrence of >3,600s execution times indicates continuous systemic failure requiring immediate review.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Summary for Leadership**
Instability in the Mirakl integration has extended to a **13-day streak (March 17–29)**. A new cluster occurred early morning **March 30**, where `fni-order-create` triggered "Exception Occurred At Mirakl Route" and "Error while calling APIs" at **02:00:39 UTC**. All issues resolved within approximately 5 minutes by **02:05:50 UTC**. This mirrors the late evening Mar 29 instability affecting `fni-offer` (FairPrice Route) and `fni-order-create`. Concurrently, the `picklist-pregenerator` service continues to exhibit critical latency (>3,600s), with a specific metric of **3609.523s** logged on Mar 29, indicating persistent systemic degradation across the `dpd-fulfilment` and `seller-experience` squads that requires urgent engineering review.


## [21/61] [Prod Support] Marketplace
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


## [22/61] RMN Incidents
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


## [23/61] DPD AI Guild
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


## [24/61] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Last Activity: 2026-03-30T01:05:31.724000+00:00 | Last Updated: 2026-03-30T02:42:22.305427+00:00
**Daily Work Briefing: Nikhil Grover & Michael Bui (Updated)**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator; clarifying technical scope, OSMOS logic, and operational controls. Currently coordinating incident fixes and ticket updates for FE team.
*   **Michael Bui:** Technical Lead (Engineering); identified race condition requiring UAT. Clarified implementation constraints regarding page-specific video support and slot sequencing.

**Main Topics & Technical Clarifications (Mar 28–30)**
1.  **Scope of Video Support & Page Logic:**
    *   Video content is restricted to Omni Home and FP Pay; Search/Category pages route to legacy MPS (no video UI). Ops controls ensure one video per carousel.
2.  **OSMOS Logic & Slot Management:**
    *   `pcnt` limit is currently 10; expansion >10 expected by early April.
    *   `position` field values (-1, 0, 999) are optional for slot uniqueness, not sequencing. Values like 999 are acceptable if unique per slot.
3.  **Incident Resolution & Deployment (New):**
    *   A race condition identified on March 27 prevents `swimlane` and `page_name` rendering. Nikhil Grover requested the specific incident fix details and deployment ownership on March 30, directing Michael Bui to clarify who is deploying the resolution.

**Decisions Made & Status Updates**
*   **Deployment Readiness:** Michael remains available for urgent evening deployments before his April 6th departure but requires clarity on slot logic and the current incident fix owner to proceed confidently.
*   **Ticket Coordination:** Nikhil confirmed he will update ticket DPD-838 with explicit slot value examples and OSMOS clarifications tomorrow (Mar 29) while coordinating with Alvin for implementation details.
*   **Revenue Metrics:** Pending afternoon update on specific numbers based on `pcnt` drops (originally noted as $1250/day).

**Pending Actions & Owners**
*   **Incident Fix Details (Nikhil Grover):** Obtain the specific incident fix and confirm the deployment owner for the race condition.
*   **Ticket Updates (Nikhil Grover):** Update DPD-838 with explicit slot value examples and OSMOS logic clarifications; coordinate with Alvin.
*   **Monday Confirmation (Nikhil Grover):** Verify the timeline for OSMOS `pcnt` limit expansion (>10).
*   **Ops Approval:** Ensure strict adherence to one-video-per-carousel limits during campaign approval.

**Key Dates & Deadlines**
*   **March 28, 2026:** Technical scope clarified; Nikhil to update tickets tomorrow; Michael reviews slot logic examples.
*   **March 30, 2026:** Nikhil inquired about incident fix ownership and deployment process.
*   **April 6–12, 2026:** Michael Bui's leave period (island with limited connectivity).

**Historical Context Note**
The conversation pivoted from parameter gaps to a confirmed technical defect: a race condition identified March 27 preventing `swimlane` and `page_name` rendering. While Nikhil initially cited a $1250/day impact, he clarified this includes the overall drop (excluding S$11.5K lost revenue from advertisers who stopped campaigns on March 17). On Mar 28 afternoon, Michael raised six critical questions regarding video scope, OSMOS logic, and slot sequencing. Nikhil clarified that video is restricted to Omni Home/FP Pay via Ops control, slot values are optional for uniqueness rather than sequencing, and PCNT limits >10 are expected by early April. On March 30, the focus shifted to operationalizing the fix for the race condition, with Nikhil requesting deployment ownership details from Michael. Documentation updates remain scheduled for Mar 29 in coordination with Alvin.


## [25/61] BCRS Firefighting Group
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


## [26/61] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Last Activity: 2026-03-30T00:40:24.961000+00:00 | Last Updated: 2026-03-30T02:43:46.201139+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Sneha Parab:** Lead/Manager; coordinating cross-team support, SAP/API integration blockers.
*   **Michael Bui:** Engineering/RMN Architect; identified root cause for the RMN incident and preparing UAT verification.
*   **Alvin Choo:** Leadership; addressing approval workflows for weekend deployments and release schedules.
*   **Daryl Ng:** Investigating store network ownership, Omni Home data discrepancies (currently away).
*   **Gopalakrishna Dhulipati:** On Child Care Leave until Wednesday (March 30–April 2). Will reach out individually if assistance is required to rep tasks.
*   **Others Active:** Andin Eswarlal Rajesh, Olivia, Koklin, Zaw, Ravi.

**Main Topics & Updates**
1.  **RMN Incident Resolution:** Michael Bui identified the root cause and is implementing a fix pending UAT verification. Immediate guidance required on deployment protocols: weekend (Sat/Sun) deployments require an approval request to Hui Hui.
2.  **Search Performance Drop:** Investigation continues regarding the severe 60–70% impression decline since March 18/19. The RMN root cause fix may correlate with these symptoms; release timing remains contingent on this investigation and UAT success.
3.  **Epic Lifecycle Query (DPD-710):** Sneha Parab flagged a technical live date of March 19, 2026, for the Omni ticket. With Daryl Ng away, closure validation awaits Michael Bui's input on whether the epic is safe to close immediately.
4.  **SIT Timeline & Redelivery Risk:** Discussion continues on SIT delivery feasibility before April 6/7 contingent on Knowledge Transfer (KT). Adrian remains unavailable for redeliveries between April 1–7 due to duplicate posting risks without a completed handover.
5.  **Infrastructure Compliance:** Bitnami ending free Docker images mandates migration for `sonic_raptor` and `mkp-fairnex`.
6.  **Resource Availability:** Gopalakrishna Dhulipati is currently on Child Care Leave until Wednesday, March 30.

**Pending Actions & Owners**
*   **RMN Deployment Approval:** Confirm weekend deployment process (send approval request to Hui Hui) following UAT verification of the fix. (Owner: Michael Bui; Coordination: Alvin Choo/Hui Hui)
*   **Epic Closure Validation:** Determine if DPD-710 can be closed given the March 19 live date discrepancy. (Owner: Michael Bui; Requestor: Sneha Parab)
*   **SIT Delivery Assessment:** Evaluate KT feasibility to complete SIT before April 6/7. (Owners: Michael Bui/Daryl Ng)
*   **Store Network Ownership:** Confirm scope under Data COE vs. Miguel's team regarding `Omni Home` store ID mismatch (OMNI-1157). (Owner: Daryl Ng/Michael Bui)
*   **SAP Timeline Resolution:** Resolve deposit SKU data integration blockers. *Note: Gopalakrishna Dhulipati is on leave until Wednesday; individual rep requests will be made if needed.* (Owners: Sneha Parab/Alvin Choo/Gopalakrishna Dhulipati)
*   **RAW Forms Review:** Complete Risk Register review for DPD RAW forms; confirm handovers and renew expired forms by Tomorrow EOD. (Owner: All Leads/Sazali Bin Mohammed Ali's team)

**Decisions Made & Status Changes**
*   **RMN Fix Status:** Root cause identified; moving to UAT verification. Deployment timing (weekend vs. weekday) is currently being debated.
*   **Release Strategy:** Regular app release status remains pending the search performance investigation and RMN fix validation.
*   **Architecture Updates:** Michael Bui has updated current, future, and transition architecture diagrams.
*   **Staffing Update:** Gopalakrishna Dhulipati is on Child Care Leave until Wednesday; active engagement for task reassignment will be initiated by him directly.

**Key Dates & Deadlines**
*   **RAW Forms Review:** Due Tomorrow EOD.
*   **Gopalakrishna Dhulipati Leave:** Until Wednesday, March 30 (Child Care Leave).
*   **Adrian Redelivery Block:** Unavailable Apr 1–7 due to duplicate posting risks.
*   **SIT Target:** Potential delivery by April 6/7 contingent on KT success.
*   **Chee Hoe Support:** Effective end of March for Product Catalogue/MarTech scope.
*   **DPD-710 Live Date:** March 19, 2026 (Subject to validation).


## [27/61] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Last Activity: 2026-03-30T00:03:09.786000+00:00 | Last Updated: 2026-03-30T02:44:30.044510+00:00
**Daily Work Briefing Summary (Updated: March 30, 2026)**

**Main Topics & Discussions**
1.  **Programmatic Advertising (Advertima/TTD):** Focus remains on validating discrepancies for `advertima_ttd-fixed-price-test-1.5`. Ravi Singh confirmed receipt of raw BURLs; validation was targeted for Monday, March 17th. Yian Koh requested confirmation on deals `advertima_ttd-first-price-test` and `advertima_ttd-fixed-price-test-1`.
2.  **New Deal Setup:** Yasmina Tregan (Advertima) required an end-to-end test setup this week. Wei Phung to share live campaign details; Ravi Singh to execute setup, push to TradeDesk, and map segments before launch.
3.  **BCRS UAT & Finance Integration:** Progress on SAP document numbers, duplicate posting fixes via PubSub "exactly once" policy (PR #1033), and Bukit Timah Plaza pricing/display issues.
4.  **Event Sync Optimization (DPD-645):** Addressing the massive event overage (14M vs. normal 550k). PRD deployment plan set for Sunday, March 15.
5.  **Security & Compliance:** RMN Pentest fixes (DPD-700) deployed to Prod; Bitbucket App Passwords deprecated effective June 9, 2026.

**Status Update: Inbox & Communications**
*   **Inbox Status:** As of March 30, 2026, the workspace inbox is fully caught up across all categories (**Urgent Action Items**, **High-Volume Project Themes**, **Meeting Updates**, and **FYI**). No pending unread items require immediate attention. This status follows confirmations from daily summaries dated March 24 through March 29. The latest update from Workspace Studio (March 30) confirms zero backlog in all sections, including Code Reviews and Project Updates.

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

**Note on New Content:** The daily summary from March 30, 2026, via Workspace Studio confirms the inbox remains clear of urgent action items across all categories. No changes to pending actions or decisions were required based on this update; historical context regarding project statuses and deadlines remains valid.


## [28/61] RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU | Last Activity: 2026-03-29T23:51:01.397000+00:00 | Last Updated: 2026-03-30T02:44:53.694272+00:00
**Daily Briefing Summary: RMN Leadership Space (Updated Mar 29)**

**Key Participants & Roles**
*   **Bryan Choong:** Returned from eTail Asia; currently at Thomson Plaza for the ongoing Aussie fair. Prioritizing Q1 case study compilation, low-sodium project, and sampling solutions. Observed 6–7 sampling booths congesting physical traffic flow.
*   **Pauline Tan:** Managing LinkedIn content (FPG ADvantage page) and award repurposing. Transitioning from award submissions to case study development; tasked with investigating sampling booth spend via Serene.
*   **Rajiv Kumar Singh:** Coordinating SOAC planning; previously shared DoorDash Ads sales lift benchmarks (+30% incrementality).
*   **Allen Umali:** Leading SignCloud cleanup and Advertima loop verification (Legacy hardware status remains active). Currently on Medical Certificate (MC) due to illness.

**Main Topics**
1.  **Sampling Solution Acceleration:** During the ongoing Aussie fair at Thomson Plaza, Bryan Choong observed 6–7 sampling booths significantly choking store physical traffic flow. He directed Pauline Tan to engage Serene for details on spend (FPG or supplier) and emphasized accelerating the "sampling solution" alongside new product launch solutions.
2.  **Case Study Development:** Immediate focus remains on the "low sodium" case study; HPB and APB efforts rely on repurposing recent award submissions submitted Mar 26 (Drum APAC, Retail Asia). A tracker for these studies is required.
3.  **Industry Benchmarking:** Rajiv Kumar Singh previously shared DoorDash Ads sales lift measurement capabilities driving up to 30% incrementality.
4.  **SignCloud Cleanup:** Legacy hardware cleanup continues; Allen Umali confirmed the full list was available for removal by Mar 28.

**Pending Actions & Owners**
*   **Sampling Solution Investigation:** Determine spend amounts (FPG/supplier) and traffic impact of sampling booths at the Aussie fair. *Owner: Pauline Tan (via Serene).*
*   **Sampling Solution Acceleration:** Develop and accelerate the sampling solution as part of new product launch strategy. *Owners: Bryan Choong, Pauline Tan.*
*   **Case Study Tracker:** Establish and maintain a refreshed tracker of strong Q1 case studies. *Owner: Pauline Tan.*
*   **Low Sodium Case Study:** Accelerate development to prioritize immediate wins. *Owners: Bryan Choong, Pauline Tan.*
*   **HPB & APB Submissions:** Convert submitted award entries into case study formats; prepare APB submission. *Owner: Pauline Tan.*
*   **SignCloud Cleanup:** Complete manual removal of legacy screens and resolve loop errors. *Owner: Allen Umali | Status: Target completion Mar 28 (passed); Currently on MC, urgent contact via WhatsApp.*
*   **Advertima SRA Renewal:** Secure new SRA for long-term partnership beyond April extended PoV. *Owners: Allen Umali, Alvin Choo.*
*   **SOAC Planning:** Finalize targets per CM, supplier, and category by end of March. *Owner: Rajiv Kumar Singh & Ryan.*

**Decisions Made**
*   **Sampling Strategy:** Accelerate the sampling solution immediately; investigate high-traffic booth congestion at Thomson Plaza (Aussie fair).
*   **Case Study Priorities:** Immediate focus on "low sodium" case study; HPB/APB efforts to utilize repurposed award entries.
*   **SignCloud Resolution:** Manual purging of old screens confirmed, targeting completion by Mar 28. Allen Umali notified team of illness and MC status; urgent matters to be handled via WhatsApp.

**Key Dates & Deadlines**
*   **Mar 26:** Pauline Tan submitted award entries (Drum APAC, Retail Asia); Bryan requested case study tracker and low-sodium focus; Rajiv shared DoorDash benchmark data.
*   **Mar 28 (Est.):** Completion of SignCloud manual cleanup.
*   **Mar 29:** Bryan Choong observed sampling booth congestion at Thomson Plaza; directed investigation into spend/traffic impact. Allen Umali reported illness and went on MC.
*   **End of March:** Deadline to finalize SOAC targets.
*   **April End:** Current deadline for Advertima extended PoV operations.


## [29/61] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE/qsfGRIhmHp4 | Last Activity: 2026-03-29T02:13:44.614000+00:00 | Last Updated: 2026-03-29T02:35:00.963824+00:00
**Daily Work Briefing: Google Chat Summary**
**Resource:** Nikhil Grover
**Date:** March 28–29, 2026

**Key Participants & Roles**
*   **Nikhil Grover:** Product/Strategy lead; clarifies scope and evaluates technical complexity regarding service migration.
*   **Michael Bui:** Engineering lead; details routing architecture between legacy MPS (NodeJS) and the new RMN ad service (Golang).

**Main Topic**
Refined discussion on migrating request routing from legacy MPS services to the new RMN ad service. The focus shifted from video format handling to ensuring all traffic (including category, promotion, and search pages) routes correctly. The team assessed the risks of implementing dynamic slot logic in two locations versus a single unified location due to poor code quality in the existing NodeJS stack.

**Decisions Made & Technical Strategy**
*   **Migration Scope:** All requests from category, promotion, and search pages currently using old MPS services must be routed to the new RMN ad service (Golang).
*   **Implementation Approach:** Logic must be implemented in a single location within the new service. Implementing logic in two places is rejected due to higher complexity and risk, specifically citing that the existing NodeJS code lacks sufficient test coverage.
*   **Instrumentation:** New instrumentation requirements were raised but confirmed as necessary for the unified approach; however, no specific timeline impact was noted.

**Pending Actions & Ownership**
*   **Routing Migration:** Michael Bui must migrate all page types (including category, promotion, search) to send requests to the new RMN ad service. *Owner: Michael Bui.*
*   **SIT Completion:** Finalize System Integration Testing (SIT) by April 7–8, 2026. *Owner: Engineering Team.*
*   **UAT & Deployment:** Execute User Acceptance Testing immediately post-SIT to meet the production deadline. *Owner: Michael Bui/Engineering Team.*

**Key Dates & Deadlines**
*   **SIT Completion Target:** April 7 or 8, 2026.
*   **Production Deployment Target:** April 9, 2026 (contingent on SIT completion and assuming work proceeds after team members return).

**Summary Notes**
Michael Bui clarified that the migration is driven by the need to centralize dynamic slot logic in the new Golang-based RMN ad service, rather than just handling video formats. He noted that the legacy NodeJS MPS code has poor test coverage, making a dual-implementation approach too risky. Consequently, Nikhil Grover confirmed the plan to implement logic in one place. Bui assured that despite the necessary migration of category, promotion, and search pages, the April 9th production launch remains feasible provided SIT is completed by April 7–8. Grover sought confirmation that this timeline assumes work begins immediately upon team return.


## [30/61] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE/ghXHBY1ul1k | Last Activity: 2026-03-29T01:14:25.795000+00:00 | Last Updated: 2026-03-29T02:35:54.864658+00:00
**Daily Work Briefing: OSMOS Banner Logic & Slot Transition Strategy**

**Key Participants & Roles**
*   **Nikhil Grover:** Product/Technical Lead. Explained the interim nature of the "slot" field and confirmed logic for duplicate handling.
*   **Michael Bui:** Technical Stakeholder. Validated tracking object positioning logic and questioned the necessity of static slots in a dynamic environment.

**Main Topic**
Discussion refined the business logic for the optional "slot" field in OSMOS, clarifying its role as an interim transition mechanism until May 1, 2026. The conversation addressed edge-case handling for empty/null values and duplicate slot numbers, alongside the rationale for maintaining this field during the current sales cycle.

**Decisions Made & Clarified Logic**
1.  **Interim Purpose:** The "slot" field is strictly temporary. It remains necessary because paid campaigns are still sold by slot until **May 1, 2026**.
    *   *Scenario:* A campaign with a 2-impression cap on Omni Home will be replaced by a house banner once the limit is hit, resulting in sequences like `[1,1,null, null,null,2,null]`.
2.  **Post-Transition:** After May 1, the "slot" field will no longer be used; the system will transition to purely dynamic slots.
3.  **Duplicate Handling (First-Wins):** If a number exists in the field, the system retains only the **first** instance. Subsequent banners with the same slot value are dropped.
    *   *Input Example:* `[null, null, 2, null, null, 1, null, 1]`
    *   *Output Result:* `[null, null, 2, null, null, 1, null]` (The second banner with `slot = 1` is removed).
4.  **Default Behavior:** If the "slot" field is blank or null, the system takes **no action**; the banner remains in the sequence.

**Pending Actions & Ownership**
*   **Action:** Nikhil Grover to verify and implement control logic on the OSMOS side based on the confirmed "blank = no action" and "first-wins duplicate" rules.
    *   **Context:** While Michael raised questions about tracking object positioning, Nikhil confirmed the technical approach is acceptable given the interim strategy. Implementation remains the immediate next step.

**Key Dates & Follow-ups**
*   **Discussion Date:** March 28–29, 2026 (Session concluded with final clarifications on March 29 at 01:14 UTC).
*   **Critical Deadline:** **May 1, 2026**. On this date, the "slot" field logic will be deprecated as the system moves away from slot-based selling.

**Specific References & Context**
*   **System/Platform:** OSMOS.
*   **Data Constraints:** The field may contain numbers (e.g., 999), and sequences often include negatives, zeros, or duplicates during the transition period.
*   **Related Pages:** Omni home, OG Home, FP Pay.
*   **Tracking Logic:** Michael confirmed that while the logic is technically sound, the output sequence reflects the deduplication process (e.g., removing the second occurrence of slot `1`).


## [31/61] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE/fYk6XRzFjAo | Last Activity: 2026-03-28T15:55:03.891000+00:00 | Last Updated: 2026-03-28T22:37:26.809516+00:00
**Daily Work Briefing: Google Chat Summary (Nikhil Grover)**

**Key Participants & Roles**
*   **Nikhil Grover:** Resource/Owner of the operational workflow regarding carousel video approvals.
*   **Michael Bui:** Stakeholder requesting process clarification on ticketing instructions.

**Main Topic**
The discussion centers on **Ops controls approval** for video carousels, specifically addressing how many videos should be included in a final output and how this instruction must be communicated within the project ticket.

**Decisions Made**
*   **Video Count:** Ops controls will ensure that only **one video per carousel** is processed/approved.
*   **Process Requirement:** Tickets must explicitly state whether to drop any videos beyond the first one (2nd video onwards).

**Pending Actions & Owners**
*   **Action:** Ensure all future tickets clearly indicate if the 2nd and subsequent videos should be dropped.
    *   **Owner:** Implementation team/Nikhil Grover (confirmed via "Ok" response to Michael Bui's request).
*   **Action:** Apply the "one video per carousel" rule during ops approval.
    *   **Owner:** Ops controls team (as directed by Nikhil Grover).

**Key Dates & Timeline**
*   **Discussion Date:** March 28, 2026
*   **Timeline of Events:**
    *   15:35 UTC: Initial note regarding the "one video per carousel" rule.
    *   15:45 UTC: Michael Bui requested clear ticketing instructions regarding dropping extra videos.
    *   15:55 UTC: Nikhil Grover acknowledged and accepted the requirement to update ticket clarity.

**Summary of Conversation Flow**
Nikhil Grover initiated the thread by stating that Ops controls will enforce a limit of one video per carousel. Michael Bui immediately followed up (approx. 10 minutes later) to clarify that this decision must be explicitly written in the ticket, specifically asking for confirmation on whether to drop the 2nd video onwards. Nikhil Grover responded approximately 10 minutes after that request, confirming the instruction ("Ok").

**Reference**
*   **Resource:** Nikhil Grover
*   **Chat URL:** https://chat.google.com/dm/t3wf6EAAAAE


## [32/61] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE/AjRV8_d65w4 | Last Activity: 2026-03-28T15:52:39.199000+00:00 | Last Updated: 2026-03-28T22:38:11.036012+00:00
**Daily Work Briefing**
**Resource:** Nikhil Grover | **Date:** March 28, 2026

**Key Participants & Roles**
*   **Nikhil Grover:** Discussant; concerned with ticket ownership and finalizing the production timeline.
*   **Michael Bui:** Developer/Owner of current task; assessing feasibility of handover and weekend work.

**Main Topic**
Discussion regarding resource allocation for a specific development task, feasibility of meeting upcoming deadlines, and confirmation of the Production (PRD) deployment schedule.

**Decisions Made**
*   Michael Bui will retain ownership of the task rather than handing it to another developer due to tight constraints; he confirmed that while another person *could* work on it, they likely could not complete development within the next week.
*   The team agreed to proceed with a timeline targeting Production deployment between April 8 and April 9, pending successful UAT.

**Pending Actions & Ownership**
*   **Nikhil Grover:** Update the ticket tomorrow if answers are comprehensive; confirm alignment on the final PRD date (April 9).
*   **Michael Bui:** Work over the weekend to ensure SIT completion by April 7–8.
*   **Team/All:** Execute UAT immediately following SIT to enable deployment.

**Key Dates & Deadlines**
*   **March 29, 2026 (Tomorrow):** Nikhil Grover updates the ticket.
*   **April 7–8, 2026:** Earliest expected completion of System Integration Testing (SIT).
*   **April 8 or 9, 2026:** Targeted deployment to Production (PRD), contingent on fast UAT.
*   **April 9, 2026:** Confirmed current deadline for Production by Nikhil Grover.

**Context**
Nikhil initially proposed handing the task off if questions were answered comprehensively but pivoted after Michael noted development constraints. Michael committed to weekend work to bridge the gap between SIT and UAT, aiming to meet the April 9 PRD target.


## [33/61] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE/4_UWzOKoxX0 | Last Activity: 2026-03-28T14:44:42.866000+00:00 | Last Updated: 2026-03-28T22:39:20.829035+00:00
**Daily Work Briefing: Google Chat Summary**
**Resource:** Nikhil Grover
**Date:** March 28, 2026
**Participants:** Michael Bui (Sender), Team/Recipient (Implicit)

**1. Key Participants & Roles**
*   **Michael Bui:** Engineer/Product Owner raising technical concerns regarding the video banner implementation and OSMOS integration. Acknowledges being occupied with packing but is actively clarifying scope and logic.

**2. Main Topic**
Clarification of requirements and technical constraints for the new video banner component rollout across Omni Home, OG Home, and FPPay, specifically focusing on:
*   Scope expansion to Category/Search pages (currently routing via the legacy MPS service).
*   Logic definitions for OSMOS integration (Campaign type matching, percentage limits, position tracking).
*   Edge case handling (API failures, auto-play/next logic).

**3. Pending Actions & Owners**
*   **Action:** Document clarifications and logic specifics in the associated ticket to maintain context.
    *   **Owner:** Michael Bui (stated intent: "I commented in the ticket as well").
*   **Action Required by Recipient/Nikhil Grover:** Address specific technical questions raised by Michael:
    1.  Confirm if Category/Search pages require mandatory video support changes or if they remain on the legacy MPS service.
    2.  Define explicit logic for identifying non-endemic banners via the `Campaign type` field (exact vs. substring match).
    3.  Clarify OSMOS support limits for `pcnt` > 10 and define expected handling when the limit is capped at 10.
    4.  Confirm ownership of position tracking values (e.g., `[-1, 0, 1, 2, 2, 5, 999]`)—specifically if OSMOS manages these or if they are passed differently.
    5.  Define logic for auto-play and auto-next scenarios involving multiple videos.
    6.  Establish fallback expectations if no banner is returned by OSMOS or the API becomes inaccessible.

**4. Decisions Made**
*   **Scope Acknowledgement:** Michael noted his initial estimation focused only on Omni Home, OG Home, and FPPay (supporting video). He flagged that Category/Search pages currently route to the old MPS service which does not support video in the UI. The decision on whether to mandate changes for these legacy pages is pending recipient confirmation.
*   **Documentation Strategy:** Michael decided to consolidate detailed clarifications directly into the project ticket rather than continuing the chat thread.

**5. Key Dates & Follow-ups**
*   **Timestamp:** March 28, 2026 (14:39 UTC – 14:44 UTC).
*   **Follow-up:** Immediate response required on the six open technical questions to unblock estimation and implementation planning.
*   **Context Link:** https://chat.google.com/dm/t3wf6EAAAAE


## [34/61] [BCRS]-SAP to POS & DBP Interface Deployment
Source: gchat | Group: space/AAQAeMC3qBk | Last Activity: 2026-03-28T03:22:30.817000+00:00 | Last Updated: 2026-03-28T03:48:23.615469+00:00
**Daily Work Briefing: [BCRS]-SAP to POS & DBP Interface Deployment**

**Key Participants & Roles**
*   **Onkar Bamane:** Deployment Lead/Coordinator.
*   **Michael Bui:** Deployer (Production OData/SAP).
*   **Hendry Tionardi:** Technical Advisor.
*   **Prajney Sribhashyam:** Process Owner/Test Coordinator (Lead on DBP Testing).
*   **Daryl Ng:** Technical Advisor/Approver.
*   **Others:** Sneha Parab, Wai Ching Chan, Olivia, Kandasamy Magesh.

**Main Topic**
Transition from production deployment execution to post-deployment validation and testing. While the initial deployment was successful on March 26, 2026, active focus has now shifted to validating DBP functionality in Production.

**Decisions Made & Status Update**
1.  **Deployment Execution:** Confirmed that **DBP deployment proceeded first**, followed by SAP OData, as originally planned. Michael Bui successfully deployed to Production (PRD) on March 26, 2026.
2.  **New Testing Phase Initiated:** A dedicated thread titled **"DBP Production Testing"** has been established and is currently active.
    *   Status: The thread contains 3 replies with 3 unread messages as of the last check (approx. 11 minutes ago).
    *   Owner: Prajney Sribhashyam is leading this specific validation effort.
3.  **Risk Mitigation:** The initial validation that deploying DBP first poses no risk regarding BCRS deposit error logs remains valid during this testing phase.

**Pending Actions & Ownership**
*   **DBP Production Validation:** Monitor the "DBP Production Testing" thread for test results and anomalies. *(Owner: Prajney Sribhashyam)*
*   **Update Deployment Steps:** Team members must continue adding specific deployment steps to the shared spreadsheet. *(Owner: Michael Bui, Sneha Parab)*
    *   *Specific Note:* Sneha Parab is requested to update steps specifically regarding **MP Article creation**.
*   **Add Missing PICs:** Identify and add any missing Persons In Charge (PICs) not currently listed in the coordination group. *(Owner: Sneha Parab, Prajney Sribhashyam)*
*   **Redelivery Status:** Discuss the latest status on "redelivery" separately in the working group meeting; do not discuss in this chat. *(Owner: Prajney Sribhashyam)*
*   **Release Coordination:** The condition for an exceptional release is now moot as the standard deployment was completed successfully by Michael Bui.

**Key Dates & Deadlines**
*   **Deployment Window:** Friday, March 26, 2026 (Completed).
*   **Current Activity Date:** Testing updates noted on March 28, 2026.

**References**
*   **Thread: DBP Production Testing:** https://chat.google.com/space/AAQAeMC3qBk (Accessed within the chat space)
*   **Deployment Plan/Tracker (SAP-DBP Deployment Plan):** https://docs.google.com/spreadsheets/d/1gvCjdXWB2BeWr7XgBQs0-zKeLxGi3OmX4ZrbY6pNMeQ/edit?gid=1022676232#gid=1022676232
*   **Chat Space:** https://chat.google.com/space/AAQAeMC3qBk


## [35/61] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/GnLs4UnHRAI | Last Activity: 2026-03-28T03:06:46.472000+00:00 | Last Updated: 2026-03-28T03:49:53.983297+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Alvin Choo:** Requestor of status updates; responsible for disseminating information to stakeholders.
*   **Prajney Sribhashyam:** Subject matter expert providing technical details and coordination support.

**Main Topic**
Discussion regarding recent changes affecting the system, specifically noting concurrent updates observed in the "starship channel." The focus is on consolidating these changes into a comprehensive status update.

**Pending Actions & Ownership**
*   **Action:** Provide an overall update on recent changes to Alvin Choo.
    *   **Owner:** Prajney Sribhashyam (to be confirmed during a call).
*   **Action:** Schedule and conduct a quick call to ensure all necessary details are captured prior to the final update issuance.
    *   **Owner:** Both participants (initiated by Prajney).

**Decisions Made**
*   Prajney Sribhashyam agreed to facilitate a brief synchronous discussion ("quick call") rather than providing text-based details immediately, ensuring no critical information is missed before Alvin releases the status report.

**Key Dates & Follow-ups**
*   **Date of Conversation:** March 28, 2026.
*   **Timeframe:** Early morning (UTC) between 03:04 and 03:06.
*   **Follow-up Required:** Immediate scheduling of a call to finalize the content for Alvin's status update.
*   **Reference Channel:** "starship channel" (mentioned as having parallel updates).

**Resource Metadata**
*   **Group:** BCRS Firefighting Group
*   **Source URL:** https://chat.google.com/space/AAQAgT-LpYY


## [36/61] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE/owFZqxoK4p8 | Last Activity: 2026-03-28T02:42:04.629000+00:00 | Last Updated: 2026-03-28T03:50:30.120558+00:00
**Daily Work Briefing**
**Resource:** Nikhil Grover
**Date Range:** March 27–28, 2026

**Key Participants & Roles**
*   **Nikhil Grover:** Lead/Stakeholder (Focus: Impact assessment, user story documentation for new app).
*   **Michael Bui:** Technical/Engineering (Focus: Root cause analysis of detection failure, proposed testing infrastructure fixes).

**Main Topic**
Discussion regarding a delayed detection of a system issue causing a financial impact of approximately **$1250 per day**. The conversation addresses why the issue was missed during previous testing phases and outlines necessary changes to the testing strategy in **Osmos** to prevent recurrence.

**Root Cause Analysis (Michael Bui)**
The issue could not be spotted earlier because it requires **multiple concurrent requests** to manifest. Current unit and E2E tests focus on individual requests, which typically ensure at least one ad is present, masking the logic degradation that occurs over time when multiple requests interact.

Previously, testing relied on hard-coded campaigns in Osmos covering multiple ad positions. However, these products went out of stock (OOS), and subsequent campaign changes caused missing ads in specific positions. To avoid false alarms, test scope was reduced to merely checking for the *presence* of an ad, which failed to detect this concurrency issue.

**Decisions Made**
No final decision on a deadline or immediate timeline was recorded. However, Michael Bui proposed two critical requirements to reliably catch these issues:
1.  Establish a campaign in Osmos that is **immutable**, stocked with abundant inventory intended to last indefinitely (virtually), eliminating OOS scenarios.
2.  Implement a specific process in Osmos to prevent this campaign from being modified or competed against by other campaigns.

**Pending Actions & Owners**
*   **Nikhil Grover:** Writing user stories for the new application to clarify requirements if needed; asked why the issue was not spotted earlier.
*   **Michael Bui (Action Required):** Implement the proposed immutable campaign strategy and process controls in Osmos to ensure reliable detection of multi-request issues.

**Key Dates & Follow-ups**
*   **2026-03-27 22:21 UTC:** Nikhil Grover noted the $1250/day impact and questioned Monday's availability.
*   **2026-03-28 02:37 UTC:** Michael Bui explained the technical difficulty of detection due to test scope limitations.
*   **2026-03-28 02:42 UTC:** Michael Bui detailed the historical context of OOS campaigns and proposed the fixed campaign solution.

**Urgency Note**
Nikhil Grover emphasized that "earlier we fix, the better" given the daily financial impact.


## [37/61] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/gZNwhpEiEY4 | Last Activity: 2026-03-28T02:23:26.710000+00:00 | Last Updated: 2026-03-28T02:35:26.007087+00:00
**Daily Work Briefing: Digital Product Development (Leads)**
**Resource:** [Leads] (Ecom/Omni) Digital Product Development
**Metadata:** { "message_count": 17, "url": "https://chat.google.com/space/AAQAN8mDauE" }
**Date of Discussion:** March 26–28, 2026

### **Key Participants & Roles**
*   **Daryl Ng:** Project Lead; confirmed changes are live in UAT.
*   **Michael Bui:** Developer for the BCRS deposit posting job; confirmed SIT success and verified functionality with a re-delivered order on March 28. Manages pipeline deployment coordination.
*   **Wai Ching:** Created necessary order custom field during UAT (March 26).
*   **Adrian:** Restricted from redelivery work between April 1–7 due to duplicate posting risks.
*   **Sneha Parab:** Validated discussion relevance against ticket DPD-807 on March 27.

### **Main Topic**
The discussion confirmed the successful completion of SIT for the BCRS deposit posting job. Michael Bui created new Jira ticket **DPD-842** to track this specific task, noting that the original **DPD-807** is now assigned to the RPA team. On March 28, Michael confirmed that changes are already in **UAT** and verified success by testing with a re-delivered order. The focus has shifted to initiating UAT for suppressing BCRS deposit posting in redelivery scenarios and finalizing PRD deployment via Bitbucket pipelines.

### **Decisions Made**
1.  **Ticket Reassignment:** Work tracked under DPD-807 is moved to **DPD-842** for the RPA team; current PR (PR #7) requires immediate review.
2.  **UAT Status:** Changes are confirmed live in UAT and verified via re-delivered order testing. Formal UAT kick-off for suppressing BCRS deposits in redelivery scenarios is pending final approval following PR merge.
3.  **Deployment Strategy:** A Bitbucket Pipeline (similar to result #67) is available to deploy master branch changes to PRD upon PR merge. If not urgent, deployment can be scheduled for next week during night hours due to Michael's daytime unavailability.

### **Pending Actions & Owners**
*   **PR Review:** Daryl Ng to review Pull Request #7: `https://bitbucket.org/ntuclink/bcrs-deposit-posting/pull-requests/7`.
*   **UAT Kick-off:** Team to formally start UAT for suppressing BCRS deposit posting in redelivery scenarios immediately after PR merge.
*   **PRD Pipeline Deployment:** Michael Bui to execute Bitbucket pipeline deployment to PRD (master branch) either urgently post-merge or next week at night, depending on urgency assessment by Daryl.

### **Key Dates & Deadlines**
*   **March 28, 2026 (02:23 UTC):** Michael Bui confirmed changes are in UAT and verified with a re-delivered order.
*   **Immediate:** PR #7 review required upon merge to proceed with deployment.
*   **Next Week (Night Time):** Fallback window for PRD deployment if not urgent.
*   **April 1 – April 7, 2026:** Critical window where Adrian must refrain from redelivery to prevent duplicate postings; SIT is concluded before this period begins.

**Reference Links:**
*   **New Ticket (SIT Tracking):** https://ntuclink.atlassian.net/browse/DPD-842
*   **Old Ticket (RPA Assignment):** https://ntuclink.atlassian.net/browse/DPD-807
*   **PR to Review:** https://bitbucket.org/ntuclink/bcrs-deposit-posting/pull-requests/7
*   **Example Pipeline:** https://bitbucket.org/ntuclink/bcrs-deposit-posting/pipelines/results/67


## [38/61] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Last Activity: 2026-03-27T19:33:53.868000+00:00 | Last Updated: 2026-03-27T22:39:14.506022+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Key Participants & Roles**
*   **Sneha Parab:** BCRS/Fees/Store Closure Impact Lead.
*   **Daryl Ng:** Backoffice/Order Management/Bug Reporting / Slot Logic validation.
*   **Michael Bui:** BCRS Deposit Logic/SAP Integration/Publisher of PRs.
*   **Wai Ching Chan:** Order Service Deployment/Slot Logic Validation.
*   **Andin Eswarlal Rajesh:** Frontend (iOS/Android) & BCRS UX queries / Amplitude tracking.
*   **Lester Santiago Soriano:** Backend Services Lead.
*   **Zaw Myo Htet:** Payment/Feature Flagging.
*   **Shiva Kumar Yalagunda Bas:** Slot discrepancy reporting.
*   **Gopalakrishna Dhulipati & Dang Hung Cuong:** Address emoji validation (New assignees).
*   **Akash Gupta:** IMS availability/UAT stock sourcing.

**Main Topics Discussed**
1.  **BCRS Epic Closure Urgency:** Sneha Parab flagged that the BCRS epic remains open with tickets in "Define" state, necessitating immediate status clarification to close the epic. Specific tickets identified: **DPD-637** and **DPD-807**. Inputs requested from Akash Gupta, Michael Bui, and Andin Eswarlal Rajesh (Mar 27).
2.  **BCRS Deposit Logic Update:** On Mar 27 at 19:33, Michael Bui published PR #7 (`bcrs-deposit-posting`) to suppress deposit posting during the re-delivery journey. Daryl Ng has been tagged for immediate code review. This action supports the critical duplicate deposit fixing efforts.
3.  **iOS Address Emoji Blocking Bug:** Wai Ching Chan reported on Mar 26 that customer addresses with emojis on iOS cause order time slot failures, requiring manual resolution (Customer ID: 2022036). Validation logic is required during address add/edit.
4.  **Website SDK Deployment (Strudel):** Lester deployed `go-platform-website` on Mar 19 to update the Strudel SDK for maximum voucher validation. Review via Bitbucket diff between v1.5.11 and v1.5.10 completed.
5.  **Pre-order Payment Logic & UAT:** Zaw initiated an inquiry on Mar 24 regarding pre-order flows (app payment vs. POS redemption) and requested peer review for the offline pre-order admin page (`https://admin-uat.fairprice.com.sg/in-store-preorder/offline`).
6.  **Slot Date Discrepancy:** Shiva reported a delivery slot mismatch (UI shows 25th, API indicates 23rd). Daryl Ng and Sundy Yaputra are resolving this.
7.  **UAT Stock Requirements:** Sneha requested high-stock SKUs for Zi Ying's bulk order testing; Wai Ching Chan and Akash Gupta tasked to check IMS availability.
8.  **Order Verification Bug (NED-278216):** Investigation continues into the Whitelisting API returning older contract data (identified by Andin).

**Pending Actions & Ownership**
*   **Daryl Ng:** Review Michael Bui's PR #7 to suppress BCRS deposit posting in the re-delivery journey.
*   **Akash Gupta, Michael Bui, Andin Eswarlal Rajesh:** Provide immediate inputs on the status of BCRS tickets **DPD-637** and **DPD-807** to facilitate epic closure (Sneha Parab).
*   **Wai Ching Chan, Gopalakrishna Dhulipati, Dang Hung Cuong:** Validate and implement emoji blocking logic for iOS address entry/editing to prevent order slot failures. Reference Customer ID: 2022036.
*   **Zaw Myo Htet:** Clarify pre-order payment redemption logic; execute UAT testing on offboarded Pinelabs split feature flag.
*   **Lester Santiago Soriano:** Assist with Whitelisting API contract issue (cc: Piraba Nagkeeran, Jonathan Tanudjaja). Deployment completed Mar 19.
*   **Daryl Ng & Sundy Yaputra:** Resolve delivery slot date mismatch (UI showing 25th vs API 23rd).
*   **All Engineers:** Mark all tickets deployed to production as "Status = Done." Highlight any pending deployments immediately (Sneha Parab).

**Decisions Made**
*   **BCRS Epic Priority:** Immediate action required to close the BCRS epic; ticket status must be verified for DPD-637 and DPD-807.
*   **Deposit Logic Fix:** Focus shifted to PR #7 review to suppress deposit posting in re-delivery flows, addressing critical duplicate posting risks.
*   **Status Protocol:** All engineers must update Jira ticket status to "Done" upon production deployment; pending items must be flagged in the chat thread.
*   **Deployment Approval:** PLU processor deployment approved pending UD alignment.
*   **Code Review Priority:** Focus remains on `go-platform-website` PR #1538 for Strudel SDK update, alongside the new BCRS deposit PR review and iOS emoji validation logic.

**Key Dates & Deadlines**
*   **Mar 27, 2026 (Today):** Sneha Parab initiated inquiry on BCRS epic closure; Michael Bui requested PR #7 review for deposit suppression. Responses required from Akash Gupta, Michael Bui, Andin Eswarlal Rajesh, and Daryl Ng.
*   **Mar 19, 2026:** Website deployment completed at 4:00 PM; UAT stock sourcing required immediately.
*   **Mar 24, 2026:** Zaw Myo Htet initiated inquiry regarding the offline pre-order admin page and pre-order payment logic.
*   **Mar 31, 2026:** Sports Hub FFS store closure deadline.

**Note on Historical Context:** Previous mentions of code review priorities for `layout-service` PR #362 and `website-service` PR #649 are superseded by the urgent Strudel SDK deployment update. The current focus includes reviewing the BCRS deposit suppression logic (PR #7), resolving slot date mismatches, pre-order payment logic queries, the iOS address emoji blocking issue, and closing the BCRS epic via tickets DPD-637 and DPD-807.


## [39/61] #dpd-dba
Source: gchat | Group: space/AAAAMh7T8Y0 | Last Activity: 2026-03-27T12:55:22.022000+00:00 | Last Updated: 2026-03-27T14:35:13.606526+00:00
**Daily Work Briefing: #dpd-dba**

**Key Participants & Roles**
*   **Akash Gupta:** DBA Team Representative/Requestor.
*   **Wai Ching Chan:** Deployment Coordinator (Service Owner).
*   **Tiong Siong Tee:** Communication Initiator.
*   **Maou Sheng Lee:** Advisor (Requested owner involvement).
*   **Gopalakrishna Dhulipati:** Primary DBA Contact (Active on recent urgent tickets).
*   **Sampada Shukla, Hanafi Yakub, Dodla Gopi Krishna, Alvin Choo, Natalya Kosenko, Lester Santiago Soriano, Borja Adrian Dominguez:** DBA Team/Stakeholders.

**Main Topic**
The conversation focuses on executing multiple urgent Jira service tickets for production and pre-production database updates, including critical patches for order zone IDs and a new insertion request for pork product picking zones. Additionally, the team is investigating GKE Autopilot scale-down incidents impacting SLOs.

**Pending Actions & Owners**
*   **Execute DSD-11003 Ticket:**
    *   **Action:** Add `container_deposit` column to `order_service.order_items`.
    *   **Owner:** DBA Team (Akash Gupta).
    *   **Status:** Pending execution if not completed. Initial request made Mar 6; replies received from Sampada Shukla and Hanafi Yakub.
*   **Execute DSD-11124 Ticket (NEW):**
    *   **Action:** Insert new picking zone ("Pork products") into the picking service table for both Prod and Pre-prod environments.
    *   **Owner:** DBA Team (specifically tagged to @Gopalakrishna Dhulipati).
    *   **Status:** **APPROVED**. Submitted by Wai Ching Chan on Mar 27 at 12:55 UTC. Requires immediate execution.
*   **Approve URGENT Patch DSD-11122:**
    *   **Action:** Patch `orders` zone ID for non-COMPLETED/CANCELLED statuses.
    *   **Owner:** DBA Team (Requested by Wai Ching Chan, Mar 27 at 08:14 UTC). Tags @Gopalakrishna Dhulipati, @Alvin Choo, @Natalya Kosenko, @Akash Gupta.
    *   **Status:** Requires immediate approval.
*   **Approve URGENT Patch DSD-11119:**
    *   **Action:** Review and approve urgent patch for `orders` zone ID (general statuses).
    *   **Owner:** DBA Team (Requested by Wai Ching Chan, Mar 27 at 04:06 UTC). Tags @Gopalakrishna Dhulipati, @Alvin Choo, @Natalya Kosenko.
    *   **Status:** Requires owner approval and consultation with the DB owner per Maou Sheng Lee's guidance.
*   **Support Production Deployment & Monitoring:**
    *   **Action:** Standby for `order-service` deployment monitoring on `fpon`.
    *   **Owner:** Akash Gupta, Gopalakrishna Dhulipati.
    *   **Status:** Requested Mar 9; script details provided.
*   **Investigate SLO Impact & Proxy Scale-Down:**
    *   **Action:** Investigate "bad connection" errors caused by `sqlproxy-prod-ap` GKE Autopilot scale-downs.
    *   **Owner:** @Gopalakrishna Dhulipati, @Dodla Gopi Krishna.
    *   **Status:** Reported Mar 25; identified as critical SLO risk.

**Decisions Made**
*   `container_deposit` column (JSON, NULL default) to be added via transaction (`BEGIN...COMMIT`) for ticket DSD-11003.
*   Ticket DSD-11124 is **approved** and ready for execution in Prod and Pre-prod.
*   Future requests must explicitly name the specific DB owner (per Maou Sheng Lee).

**Key Dates & Updates**
*   **Mar 6, 2026 (01:48 UTC):** Initial request for DSD-11003.
*   **Mar 9, 2026 (04:36 UTC):** Deployment window scheduled for 11:00 PM; script shared.
*   **Mar 25, 2026 (05:52 UTC):** SLO impact report regarding GKE scale-downs.
*   **Mar 27, 2026 (03:12 UTC):** Advice to include DB owners in requests.
*   **Mar 27, 2026 (04:06 UTC):** Urgent ticket DSD-11119 submitted.
*   **Mar 27, 2026 (08:14 UTC):** Urgent ticket DSD-11122 submitted.
*   **Mar 27, 2026 (12:55 UTC):** **New:** Wai Ching Chan submits approved urgent ticket **DSD-11124** for "Pork products" insertion; @Gopalakrishna Dhulipati tagged.

**References**
*   **Jira Tickets:** `DSD-11003`, `DSD-11119` (Urgent), `DSD-11122` (Urgent), **New: `DSD-11124`** (Pork products, Approved).
*   **Database:** `fpon.order_service.order_items`, Picking service tables (Prod/Pre-prod).
*   **Affected Cluster:** `sqlproxy-prod-ap` (GKE Autopilot).


## [40/61] RMN Incidents
Source: gchat | Group: space/AAQAz11ATzY/f96GZlnokS4 | Last Activity: 2026-03-27T11:29:15.744000+00:00 | Last Updated: 2026-03-27T14:35:57.366604+00:00
**Daily Work Briefing: RMN Incidents Analysis**

**Key Participants & Roles**
*   **Rachit Sachdeva:** Analyst/Investigator. Initiated the review of March traffic trends and provided detailed data via email.
*   **Michael Bui:** Technical Investigator. Collaborating to validate Rachit's findings by cross-referencing captured request logs.
*   **Nikhil Grover & Rahul Jain:** Tagged for visibility; no substantive updates provided in this chat thread.

**Main Topic**
Investigation into a significant traffic trend observed between March 20–27, 2026. Rachit identified that requests with `f_pcnt` (product count) set to "1" dominated the volume:
*   **CATEGORY pages:** >90% of requests.
*   **SEARCH pages:** >98% of requests.

This configuration limits system responses to a single product impression per request. The discussion focuses on confirming whether recent changes were made to the product count filter configuration causing this anomaly.

**Pending Actions & Ownership**
*   **Action:** Review captured request logs (URL, headers) to validate if `f_pcnt=1` is due to a configuration change or upstream client behavior.
    *   **Owner:** Michael Bui (Status: In Progress/Confirmed receipt of data).
*   **Context for Action:** Rachit previously emailed full request details including URL and headers to Michael (with confidential data handled via DM/email) on March 27 at 10:53 AM.

**Decisions Made**
*   Both parties agreed that yesterday's (March 26) data samples would suffice for the initial technical validation.
*   Data transmission protocol was confirmed: Full requests to be shared, with any confidential elements sent via separate secure channels (DM/Email).

**Key Dates & Follow-ups**
*   **Analysis Period:** March 20–27, 2026.
*   **Discussion Date:** March 27, 2026.
*   **Data Provided:** Yesterday's logs (March 26) shared via email prior to 11:29 AM.
*   **Next Step:** Michael Bui is currently analyzing the received email data to determine if configuration changes occurred regarding product count filters.


## [41/61] Team Starship
Source: gchat | Group: space/AAQAX9iKYf0 | Last Activity: 2026-03-27T09:35:05.122000+00:00 | Last Updated: 2026-03-27T10:41:50.003976+00:00
**Daily Work Briefing: Team Starship (Updated)**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Operations/Testing Lead.
*   **Danielle Lee:** Biz Ops/S&G Representative.
*   **Vivian Lim Yu Qian:** Product/Design Liaison.
*   **Alvin Choo:** Compliance Lead / Technical POC.
*   **Zi Ying Liow:** Frontend/Promotion Logic Inquiry.
*   **Sathya Murthy Karthik:** Shared Omni Roadmap update (March 2026).
*   **Nikhil Grover:** Compliance/PRD Liaison.

**Main Topics & Decisions**

1.  **BCRS Refunds Status (Critical Update)**
    *   **Status:** UAT complete for Customer App, Backend/Backoffice, MP Seller (Mirakl & DBP), and Preorder Staff App. Production deployment of DBP + SAP parts is confirmed.
    *   **Sign-off Timeline:** Corporate Control and Finance require first half of the day to finalize formalities; sign-off expected **EOD today**. Full UAT sign-off forms submitted for E-comm, Marketplace SKU Listing, and In-store Pre-order.
    *   **Open Non-Critical Items (Post-Launch):**
        *   **Re-delivery:** BCRS items currently cannot be re-delivered. Business holds off attempts until fix; ETA: Ready for UAT April 2, Deploy April 8.
        *   **FOC Deposit Charging:** Staff app unable to charge deposits on FOC items. Solution pending; ETA update by Monday.
        *   **B2B Quick Buy:** BCRS SKUs unavailable via quick buy. UAT in progress; Production ETA **April 3**.
    *   **Production Testing:** Smoke test scheduled for Friday (and weekend if necessary). Next production test planned for **Monday, April 30** post-deployment of refunds.
    *   **Issues:** Minor logging issue found on Marketplace orders during regression; fix deploying EOD.

2.  **Compliance & PRD Updates**
    *   **Regulatory Requirements:** Nikhil Grover shared Compliance perspective for Project Light (FPG App/BO/BE Replatform), specifically IAB standards on impression tracking (Requirement C4). Links provided in PRD documents.

3.  **Bug Report: App Icon Display (DPD-783)**
    *   **Issue:** Vivian reported Christmas theme regression.
    *   **Action:** Ticket created for urgent resolution ("asap"). Engineering Team/Andin Eswarlal Rajesh to revert.

4.  **New Request: Cart-Level Coupon Allocation**
    *   **Status:** Alvin Choo relayed Ryan's request to stop per-SKU cart-level coupon allocation for accurate GP calculation. Team determining if this fits "Project Light" list.

5.  **Frontend Tag Mapping & Performance Marketing**
    *   **Inquiry:** Zi Ying Liow seeks clarification on promotion method-to-tag mapping logic (pending technical verification).
    *   **Performance Marketing:** Alvin Choo requested an alias to the Performance Marketing team regarding a specific app change request looped in by Andin Eswarlal Rajesh.

6.  **OMNI Project Status**
    *   **Omni Roadmap:** PMs must submit deprioritized items from the "Jan 2026" roadmap by **EOD today (March 25)**.
    *   **OMNI-1345:** Indefinite hold due to foundational business model changes.

7.  **Operational Pilots**
    *   Operations piloting "picker app enhanced for CT58" on DT50S/DT66S models; Prajney emphasizes testing before store rollout.

8.  **CHAS Verification Flow**
    *   Auto-verification via MyInfo remains technically feasible but outside current "Light" scope. Vivian to verify assumptions with Serene.

9.  **Scan@Door: AI Personalisation**
    *   Daryl Ng proposed AI-based voucher issuance (vs. rule-based). Estimated BE impact: 2 weeks. Target go-live mid-April. Prioritization decision pending resource review.

**Pending Actions & Owners**

| Action Item | Owner | Deadline/Note |
| :--- | :--- | :--- |
| **Finalize:** BCRS Finance/Corp Control sign-off | Prajney / Finance | **EOD Today** |
| **Deploy:** Marketplace logging fix | Engineering Team | **EOD Today** |
| **Confirm:** App Icon revert (DPD-783) | Andin Eswarlal Rajesh / Eng | ASAP |
| **Clarify:** B2B Cybersource OTP flow applicability | Alvin Choo | As needed |
| **Submit:** Omni Roadmap deprioritization list | All PMs | **EOD Today (March 25)** |
| **Update:** OMNI-1282 status (De-prioritize) | Alvin Choo / Koklin Gan | Pending confirmation |
| **PAUSE:** OMNI-1345 requirements | All Stakeholders | Until business model finalized |
| **Clarify:** Cart-level coupon logic & Project Light inclusion | Alvin Choo / Ryan's team | Pending decision |
| **Prioritize:** Scan@Door AI Personalisation review | Danielle Lee, Daryl Ng, Tech Leads | Immediate |
| **Provide:** Performance Marketing alias contact | Alvin Choo / Andin Eswarlal Rajesh | Immediate |

**Key Dates & Follow-ups**

*   **Meeting Rescheduled:** Weekly Epics meeting postponed to **Wednesday, March 12 (tomorrow) at 11:00 AM**. Location: Level 12 Room 18 (or virtual/pantry).
*   **Reference Tickets:** SHOP-3779, OMNI-1099, DPD-100, **DPD-783**, OMNI-1345, OMNI-1282, OMNI-1421.


## [42/61] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/X0kOPw3Ylqk | Last Activity: 2026-03-27T07:51:27.333000+00:00 | Last Updated: 2026-03-27T10:48:03.618428+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Key Participants & Roles**
*   **Sneha Parab:** Initiator; aligning on epic closure status.
*   **Akash Gupta:** Contributor providing board assignment and clarification requests.
*   **Wai Ching Chan:** PM/Contributor confirming input provided and handoff details.
*   **Michael Bui:** Identified as the owner for pending work items.
*   **Andin Eswarlal Rajesh:** Tagged for inputs (no response recorded in snippet).

**Main Topic**
Closure of the **BCRS epic**. Sneha Parab raised concerns that specific tickets remain in the "define" state despite alignment at the weekly epics meeting, requesting clarification on ownership and completion status.

**Pending Actions & Ownership**
*   **DPD-637:** Akash Gupta identified this ticket belongs to the **core products (payment) board**. Status requires reassignment or validation by the relevant team.
*   **DPD-807:**
    *   **Wai Ching Chan:** Has already provided input; no further action required from them at this time.
    *   **Michael Bui:** Explicitly owns the remaining work for this ticket ("The rest for Michael to handle").

**Decisions Made**
*   **DPD-637 Ownership:** It was determined that invoices regarding this ticket should be managed under the core products (payment) board, not the current Digital Product Development scope.
*   **DPD-807 Status:** Work initiated by the PM is 50% complete (input provided by Wai Ching Chan); the remaining execution rests solely with Michael Bui.

**Key Dates & Follow-ups**
*   **Date:** March 27, 2026.
*   **Context:** Follow-up to the "weekly epics meeting."
*   **Target:** Immediate closure of the BCRS epic.
*   **Dependencies:** Resolution requires Michael Bui to complete DPD-807 and the team to address the board assignment for DPD-637.

**Reference Links**
*   **Jira Tickets:** [DPD-637](https://ntuclink.atlassian.net/browse/DPD-637), [DPD-807](https://ntuclink.atlassian.net/browse/DPD-807)
*   **Chat Room:** [Link to Room Discussion](https://chat.google.com/room/AAQAgT-LpYY/qtUOXlxVm80/qtUOXlxVm80?cls=10)


## [43/61] SRE / Network / DBA / DevOps / Infra
Source: gchat | Group: space/AAAAYX-ew1s | Last Activity: 2026-03-27T07:30:29.958000+00:00 | Last Updated: 2026-03-27T10:50:06.498405+00:00
**Daily Work Briefing: SRE / Infrastructure Team**

**Key Participants & Roles**
*   **Apurva Shingne:** Requests review for PR #142 (`infra-gcp-fpg-optimus`) and ticket GCD-8995; tagged @Sneha Parab, @Nicholas Tan.
*   **Madhawa Mallika Arachchige:** Confirmed channel usage for Datadog PR submissions on 2026-03-26.
*   **Natalya Kosenko:** Submitted Terraform PR #719; strategic IaC discussions ongoing.
*   **Boning He:** Requested access to pricing workspaces via PR #722.
*   **Zheng Ming, Wai Ching Chan, Calvin Phan:** Reported connectivity/network issues (GCD-8941, GCD-8954, DSD-11066).
*   **Himal Hewagamage & Isuru Dilhan:** Primary reviewers/approvers.

**Main Topics**
1.  **Datadog Infrastructure & Compliance:** Ongoing review of `fp-datadog-eu` PRs (#135–#148). On **2026-03-27**, Apurva Shingne submitted new PR **#142** (`infra-gcp-fpg-optimus`) linked to ticket **GCD-8995**.
2.  **Terraform & Workspaces:** Natalya Kosenko's PR #719 and Boning He's PR #722 (pricing workspace access) are pending review. A failed Terraform plan (`run-CZVLtajJGbLVojLM`) and ticket GCD-8900 remain active.
3.  **CI/CD Pipeline Failures:** Soni-BE golden pipeline clone failures persist; `lt-strudel-api-go` Go versioning conflicts (Go 1.25.8 vs `golangci-lint`) require resolution.
4.  **Cloud Networking:** AI agents in `us-central1` face internet connectivity issues (Ticket GCD-8941). Mohit Niranwal mandated non-prod testing prior to rollout.
5.  **Bastion Connectivity:** Wai Ching Chan's ticket GCD-8954 remains under investigation.
6.  **Database Subnet Request:** Calvin Phan requested CloudSQL subnets for SOT-SONI (Ticket DSD-11066); DBA coordination with @Himal Hewagamage is active.

**Pending Actions & Ownership**
*   **Review New Datadog PRs:**
    *   **PR #142:** Owned by **Apurva Shingne**; tagged for review by **@Sneha Parab**, **@Nicholas Tan**.
    *   **PR #135, #137–#139, #140, #144, #147:** Managed by @Himal Hewagamage and @Isuru Dilhan. PR #140 is also tagged to @Maou Sheng Lee.
*   **Review Terraform PRs:**
    *   **PR #719** (Natalya) & **PR #722** (Boning): Pending review by @Isuru Dilhan and @Himal Hewagamage.
*   **Troubleshoot Pipeline Issues:** Investigate Soni-BE SSH keys (Kalana) and `lt-strudel-api-go` config conflicts (Lester).
*   **Infrastructure Strategy:** Finalize IaC implementation for Datadog log pipelines (Natalya; discussion with @Prabu Ramamurthy Selvaraj).
*   **Network & DBA Tickets:** Execute non-prod testing for Cloud NAT (GCD-8941); investigate Bastion issues (GCD-8954); review SOT-SONI subnet requirements (DSD-11066).

**Decisions Made**
*   **IaC Requirement:** Mandatory adoption of IaC for Datadog pipelines.
*   **Change Management:** Mohit Niranwal mandated non-prod testing for Cloud NAT changes before production deployment (regarding GCD-8941).

**Key Dates & Follow-ups**
*   **2026-03-02 to 03-05:** Initial Datadog PR requests.
*   **2026-03-11 to 03-12:** Critical pipeline failures reported.
*   **2026-03-19:** GCD-8941 raised; Mohit Niranwal intervention regarding testing protocol.
*   **2026-03-20:** Bastion (GCD-8954) and DBA subnet (DSD-11066) tickets opened.
*   **2026-03-24:** PR #140 and #722 requested for review.
*   **2026-03-26:** Channel confirmation for Datadog submissions; @Andin Eswarlal Rajesh engaged.
*   **2026-03-27 (07:30 UTC):** Apurva Shingne submitted PR #142 and ticket GCD-8995; requested review from @Sneha Parab and @Nicholas Tan.


## [44/61] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw | Last Activity: 2026-03-27T07:21:11.133000+00:00 | Last Updated: 2026-03-27T10:51:39.560169+00:00
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
1.  **Staff Verification Logic (S&G Flows):** On March 27, 2026, Vivian Lim Yu Qian queried the existence of an app screen for staff verification during SKU purchases requiring force verification (e.g., milk powder), referencing age-restriction popup logic. The team is investigating compliance with existing verification protocols.
2.  **Incident Management Response:** Earlier on March 27, Jazz Tong raised an urgent query regarding a potential incident ("it is incident?"). The team mobilized support for the DPD Incidents channel involving Gopalakrishna Dhulipati, Akash Gupta, and Kyle Nguyen.
3.  **Infrastructure & Operations Risk:** Nicholas Tan flagged risks regarding Broadcom ending free Bitnami images, causing `kubectl` image tag failures and increased Time To Recovery (TTR) impacting the Golden Pipeline (GP).
4.  **Payment Service Issues:** Alvin Choo reported promo code redemption failures in FP Pay; confirmed that a change freeze has ended and feature releases are proceeding.
5.  **Mobile Quality Assurance:** Andin Eswarlal Rajesh identified an iOS FPPay bug where QR codes load without user login, escalated via file download.
6.  **Datadog Governance:** Natalya Kosenko reported unauthorized manual changes to Datadog On-Call teams (removals of Maxine, Arijit, Minu). Terraform manages this config; manual console edits are overwritten on the next run.
7.  **Strategic Planning:** Winson Lim highlighted data centers as potential targets in modern warfare (Iran conflict context) to inform Disaster Recovery (DR) scenarios.
8.  **Product Strategy & Tooling Expansion:** On March 26, Winson Lim noted Reforge joined Miro, signaling expansion into product strategy to close the gap between decision-making and delivery.
9.  **Social Events & Sentiment:** Kyle Nguyen announced an upcoming DPD BBQ with the sentiment "We come first." Maou Sheng Lee expressed a sentiment of feeling like energy is being wasted on March 18.

**Pending Actions & Owners**
*   **S&G Verification Team (Vivian Lim Yu Qian, Product/Dev Teams):** Investigate current S&G flows against the WIP verification logic document to confirm if forced staff verification screens exist for restricted SKUs like milk powder. Reference: `https://ntuclink.atlassian.net/wiki/spaces/SE/pages/1995997683/WIP+S+G+Verification+Flow`.
*   **Incident Response Team (Jazz Tong, Akash Gupta, Gopalakrishna Dhulipati, Kyle Nguyen):** Act as support guides for the active DPD Incidents channel; monitor and resolve incoming incident queries.
*   **GP Team (Nicholas Tan / Mohit Niranwal):** Investigate Bitnami image replacement strategy to resolve TTR issues and update Golden Pipeline dependencies.
*   **iOS/Dev Team (Tiong Siong Tee / Andin Eswarlal Rajesh):** Investigate the iOS FPPay QR code login bypass bug.
*   **Datadog Admins:** Anyone who manually altered Datadog Teams must submit a Pull Request to `https://bitbucket.org/ntuclink/fp-datadog-eu` instead of editing the console.

**Decisions Made**
*   No formal change freeze; feature releases are currently active (Alvin Choo).
*   Datadog team configurations must strictly follow Infrastructure as Code (Terraform) protocols; manual overrides are deprecated.
*   Miro's acquisition of Reforge is recognized as a strategic move to bridge product strategy and delivery gaps.
*   **New:** Active incident support protocol established for Jazz Tong, Akash Gupta, Gopalakrishna Dhulipati, and Kyle Nguyen on March 27, 2026.
*   **New:** Verification of S&G staff verification screens is pending; current logic requires validation against the WIP document.

**Key Dates & Follow-ups**
*   **Mar 27, 2026 (03:03 UTC):** Jazz Tong flagged potential DPD incident; support team mobilized.
*   **Mar 27, 2026 (08:11 AM):** Vivian Lim Yu Qian raised S&G verification flow query; discussion concluded with 12 replies.
*   **Mar 26, 2026:** Winson Lim shared Reforge joining Miro; potential impact on product strategy workflows identified.
*   **Mar 25, 2026:** Natalya Kosenko highlighted DPD alumni participation in a Google AI event.
*   **Mar 18, 2026:** Maou Sheng Lee noted sentiment regarding wasted energy.

**Social Notes**
*   Boning He and Gopalakrishna Dhulipati shared snacks (Chinese cookies with chicken gizzard/medicinal barley and Indian cookies) in pantry areas.
*   Upcoming DPD BBQ announced by Kyle Nguyen ("We come first, see you!").


## [45/61] [Prod Support] Offers
Source: gchat | Group: space/AAAAzZ3qkNU | Last Activity: 2026-03-27T06:17:14.551000+00:00 | Last Updated: 2026-03-27T06:40:11.493447+00:00
**Daily Work Briefing: [Prod Support] Offers**

**Key Participants & Roles**
*   **Willie Tan:** Reported initial issue (Mar 17) with offer visibility; escalated on Mar 26 regarding promo flow failure for specific SKUs.
*   **Angela Yeo:** Previously escalated discrepancy regarding incorrect promo display for SKU 13066243.
*   **Alvin Choo:** Previously flagged urgency and assigned owners for the initial case.
*   **Zaw Myo Htet & Daryl Ng:** Assigned to investigate both historical and new flow issues.
*   **Neo Seng Ka:** Investigating database segment configuration (Mar 27).

**Main Topic**
Investigation into production offer display errors involving two distinct but potentially related scenarios:
1.  **Historical Context (Mar 17–19):** Issues with Offer ID `sap offer 202603000112484` for **SKU 13066243**. The team confirmed "2 for $5.40" is the correct configuration, but it failed to display as expected while incorrect promotions were visible.
2.  **New Escalation (Mar 26):** Willie Tan reported that promos created in SAP are not flowing to FPON for a list of SKUs, despite these items *not* being on the promo blacklist. The specific SKUs provided were samples; a full investigation of the flow mechanism is required.
3.  **New Technical Query (Mar 27):** Neo Seng Ka raised a query regarding DBP segment configuration, specifically checking for segments involving "union + dcc" logic, noting no results found when searching for "union."

**Pending Actions & Ownership**
*   **Action 1:** Investigate why correct offers ("2 for $5.40") are not displaying or if incorrect offers are showing for historical cases (SKU 13066243).
*   **Action 2:** Investigate the root cause of promo flow failure from SAP to FPON for SKUs not on the blacklist, as reported by Willie Tan on March 26.
*   **Action 3 (New):** Clarify DBP segment logic regarding "union + dcc" configurations and confirm why no applicable segments were found in the database.
*   **Owners:** @Zaw Myo Htet, @Daryl Ng (assigned previously; applicable to all issues). @Neo Seng Ka is investigating the DBP configuration.
*   **Status:** Active/Urgent. The scope has expanded from a single SKU display error to a systemic flow issue affecting multiple SKUs. Debugging now includes database segment validation.

**Decisions Made**
No final technical fixes have been implemented yet. The team has established the expected outcome for historical cases: offers must display "2 for $5.40." For the new case, it is confirmed that SKUs in question should be eligible for promos (not blacklisted) but are failing to receive them from SAP. Neo Seng Ka's inquiry suggests a potential gap or misconfiguration in the DBP "union + dcc" segment logic which may be contributing to the flow failure.

**Key Dates & Deadlines**
*   **Initial Issue Reported:** March 17, 2026 (09:01 AM).
*   **Historical Escalation:** March 19, 2026 (10:04 AM and 12:35 PM).
*   **New Flow Issue Reported:** March 26, 2026 (02:24 AM UTC) by Willie Tan.
*   **DBP Query Raised:** March 27, 2026 (06:17 AM UTC) by Neo Seng Ka.
*   **Deadline:** Immediate resolution requested for both the display error and the new flow failure.

**Reference Links & IDs**
*   **Chat Space URL:** https://chat.google.com/space/AAAAzZ3qkNU
*   **Historical Offer ID:** `sap offer 202603000112484`
*   **Historical SKU:** 13066243
*   **New Case Scope:** Multiple SKUs (samples provided by Willie Tan) not under promo blacklist.
*   **System Components:** SAP (source), FPON (destination), DBP (segment logic).


## [46/61] Progress Check: Monitor & On-Call Team Alignment - Mar 27
Source: gchat | Group: space/AAQAuufxt5I | Last Activity: 2026-03-27T05:33:46.176000+00:00 | Last Updated: 2026-03-27T06:41:10.747636+00:00
**Daily Work Briefing: Progress Check – Monitor & On-Call Team Alignment (Mar 27)**

**1. Key Participants & Roles**
*   **Madhawa Mallika Arachchige:** Initiator of the meeting reminder; likely a team lead or coordinator for the alignment effort.
*   **@all (8 of 13 viewed):** The broader Monitor & On-Call team members.

**2. Main Topic/Discussion**
The conversation centered on a scheduled **meeting reminder** regarding "Monitor & On-Call Team Alignment." No detailed discussion content, technical updates, or problem-solving logs were recorded in the provided chat snippet; the primary activity was the dissemination of the meeting notification to the group.

**3. Pending Actions & Owners**
*   **Action:** Attend and participate in the alignment meeting.
    *   **Owner:** All team members (specifically the 8 who have viewed the message out of the total 13).
*   **Note:** No specific pre-meeting tasks or deliverables were assigned within this chat log.

**4. Decisions Made**
No formal decisions, votes, or strategic shifts were recorded in this single-message thread. The interaction serves as a logistical notification rather than a decision-making channel.

**5. Key Dates & Deadlines**
*   **Date:** March 27, 2026 (Specific time of message: 05:33:46 UTC).
*   **Event:** Monitor & On-Call Team Alignment Meeting.
    *   *Note:* The exact start time and duration of the meeting were not included in this specific reminder snippet.

**Summary Notes**
The provided data represents a single transactional message from Madhawa Mallika Arachchige intended to ensure team visibility for an upcoming alignment session. With 8 out of 13 recipients having viewed the message, attendance confirmation is pending. Further details regarding the meeting agenda or specific outcomes must be obtained directly from the meeting minutes or subsequent communications.

**Resource Link:** https://chat.google.com/space/AAQAuufxt5I
**Message Count:** 1


## [47/61] DPD Incidents
Source: gchat | Group: space/AAAAEsAEG84/bmd5TXQRY-w | Last Activity: 2026-03-27T04:54:45.718000+00:00 | Last Updated: 2026-03-27T06:41:31.016446+00:00
**Daily Work Briefing: DPD Incidents (HCBP Zone Issue)**

**Key Participants & Roles**
*   **Akash Gupta:** Technical Lead/Coordinator; identified root cause, managed DB fixes, and defined remediation steps.
*   **Owen Sng:** Operations Representative; flagged the anomaly regarding zone replacement despite standard KML upload procedures.
*   **Yap Chye Soon Adrian (Adrian):** Stakeholder; requested alignment meeting and verified order queue status post-fix.
*   **Ler Whye Ling Angel (Angel):** Initial reporter of missing picking orders for HCBP.
*   **Alvin Choo:** Team Lead; escalated issue to support room with Subject Matter Experts (SMEs).
*   **Gopalakrishna Dhulipati, Winson Lim:** Paged by Alvin for SME support.

**Main Topic**
Investigation and resolution of a critical incident where 820 orders for the HCBP store failed to appear in the picking queue due to a zone ID mismatch caused by an erroneous KML file upload.

**Root Cause Analysis**
The Changi zone (ID: 487) was deleted and replaced with a new zone (ID: 539). This occurred because the Ops team uploaded a KML file containing an extra trailing space in the name ("Changi " instead of "Changi"). The system interpreted this as a new location, invalidating existing orders linked to the old zone ID.

**Decisions Made**
*   **Immediate Mitigation:** Manual patching of affected orders via Database (DBA) ticket was executed to map them to the correct new zone.
*   **Process Validation:** The fix was verified by Adrian; pending orders are now in the picking queue following the scheduled 12:33 PM picklist generator run.

**Actions Pending & Ownership**
*   **Ops Team (Owen Sng, Alvin Choo):**
    1.  Maintain a backlog of zone upload files and validate against past uploads before production deployment.
    2.  Eliminate manual typing inputs when creating new KML files to prevent whitespace errors.
*   **DBP/Engineering Team (Akash Gupta):**
    1.  Implement an additional validation layer on the "update delivery area" API within the logistics-service to reject invalid KML formatting before processing.

**Key Dates, Deadlines & References**
*   **Incident Date:** March 27, 2026 (Timeline: 02:58 AM – 04:54 AM).
*   **Affected Volume:** 820 orders.
*   **Zone IDs:** Old Zone 487 replaced by New Zone 539.
*   **Ticket Reference:** DSD-11119 (NTU Enterprise Service Desk) – Used for DB patching; approved by Alvin Choo.
*   **Resolution Time:** Verified complete by 04:45 AM on March 27, 2026.
*   **Next Scheduled Run:** Picklist generator at 12:33 PM (March 27) to ensure pending orders are queued.
*   **Meeting Link:** https://meet.google.com/pib-buss-vqf (Call concluded).


## [48/61] Retail out of home (Digital Screens & CMS)
Source: gchat | Group: space/AAQAXn1ocmE | Last Activity: 2026-03-27T04:13:02.762000+00:00 | Last Updated: 2026-03-27T06:41:57.543576+00:00
**Daily Work Briefing: Retail Out of Home (Digital Screens & CMS)**

**Key Participants & Roles**
*   **Priscilla Chan Li Wei:** Inventory management (Samsung ADE/FilmScreen); Escalation workflow impact analysis.
*   **David Anura Cooray:** Technical operations; Lead on "EPT Blank Screen" investigation and **SWPZ** incident analysis.
*   **Fiona U:** Project Lead/Coordinator; driving Phase 1 closure and stakeholder alignment.
*   **Rajkumar Romendro & Allen Umali:** Subject matter experts for Retail Media inventory and Screen Loading (MPBS/VXT).
*   **Cheng Joo Wu:** Assigned to Action Items regarding SOPs, Indirect Procurement (IP), IFM integration, and Engie scope liaison.
*   **Serene Tan Si Lin:** Clarification on facility management scope boundaries.

**Main Topic**
The discussion centers on operationalizing **Retail Out of Home (RoOH) Phase 1**, focusing on hardware inventory verification, digital screen content loading, transitioning from Hypercare to Business As Usual (BAU), and finalizing SOPs. A critical update concerns the **IFM** announcement: it is now confirmed that IFM will encompass the current Engie scope of responsibilities (building equipment, soft services, aircons, freezers). Digital monitors remain excluded from this maintenance scope.

**New Critical Issues:**
1.  **EPT Blank Screen:** David Anura Cooray raised an urgent ticket requiring immediate technical investigation and potentially impacting screen connectivity workflows.
2.  **SWPZ Incident (ID: SWPZ):** A new high-priority thread identified by David Anura Cooray contains **14 replies** with the last update at **5:16 AM**. This requires immediate review alongside the EPT issue to assess potential systemic connectivity or loading failures.

**Pending Actions & Ownership**
*   **Sync Meeting Attendance:** Priscilla, Allen, Cheng, and Rajkumar must attend or assign a proxy to the sync scheduled for **Tuesday at 2:00 PM**.
    *   *Pre-meeting Review:*
        *   **SOPs (Gdoc & Gslide):** Resolve unresolved comments and perform consistency checks. Owners: Team (implied Priscilla/Cheng).
        *   **SLA Finalization:** Must be completed by next week for the Samsung SI meeting. Owner: Fiona U / Team.
        *   **Communication Channels:** Define escalation paths between stores and AdOps; identify chat groups to sunset. Owner: Team.
        *   **Indirect Procurement (IP):** Clarify IP's specific role before integrating them into the Retail Media Workflow. Owner: Cheng Joo Wu.
*   **Inventory Verification:** David Anura Cooray requested a master list of all digital screens under Retail Media; pending response from Allen Umali and Rajkumar Romendro.
    *   *Scope Update:* Inventory scope explicitly includes **PDD Gondola End Large TVs**.
*   **Issue Resolution (EPT & SWPZ):** David Anura Cooray must immediately investigate **"EPT Blank Screen"** occurrences and the **SWPZ** thread (14 replies, last updated 5:16 AM). This requires verification of CMS connectivity and screen status prior to the BAU transition.
*   **IFM Scope Liaison:** Cheng Joo Wu must approach the representative from RB for detailed Engie/IFM scope responsibilities.

**Decisions Made**
*   Transition from Hypercare to BAU is targeted for the week of **March 30, 2026**.
*   A pilot with Advertima is scheduled to end later this month (March 2026).
*   **IFM Scope Confirmation:** IFM will include the current Engie scope (building equipment/soft services); digital monitors are definitively **not** included. Escalation workflows for screen issues do not require IFM integration for monitor-specific faults.

**Key Dates & Deadlines**
*   **Tuesday (Current Week), 2:00 PM:** RoOH Phase 1 Sync Meeting.
*   **Next Week:** Finalize SLA for meeting with Samsung SI.
*   **Week of March 30, 2026:** Target transition to BAU (Store Training & Transition).
*   **Later this month:** End of Advertima pilot.

**Specific References**
*   **Files:** `NTUC Mac Serial number.xlsx` (Samsung inventory), Google Slides presentation on Indirect Procurement/Walkthroughs (`1FQrBgiiL69I_jsdy7W_aMTd1QApoT_Mn6A-IM25SUto`).
*   **Hardware/Systems:** Samsung screens (ADE, FilmScreen), **PDD Gondola End Large TVs**, MPBS - VXT Screen Loading, TAMHUB, FPHUB Digital Screen Content.
*   **Incident Logs:** EPT Blank Screen thread; **SWPZ** thread (14 replies, last updated 5:16 AM).


## [49/61] [Virtual] Smart Cart x RMN Catchup - Mar 27
Source: gchat | Group: space/AAQAGEaKjjo | Last Activity: 2026-03-27T03:54:49.241000+00:00 | Last Updated: 2026-03-27T06:42:41.424887+00:00
**Daily Work Briefing: Smart Cart x RMN Catchup (Mar 27)**

**Key Participants & Roles**
*   **Nikhil Grover:** Focuses on onsite (app and web) initiatives; previously managed retail out-of-home scope.
*   **Ching Hui Ng:** Meeting organizer/lead.
*   **Yi Hao:** New owner of the retail out-of-home scope (replacing Nikhil).

**Main Topic**
Discussion regarding the status, agenda, and necessity of a scheduled virtual meeting on "Smart Cart x RMN Catchup." The conversation confirmed a lack of immediate readiness for Smart Cart integration.

**Decisions Made**
*   **Meeting Cancellation:** Ching Hui Ng has officially cancelled the scheduled catch-up meeting for March 27.
*   **Strategic Pivot:** The team will prioritize "scale" efforts over the Smart Cart integration at this time.
*   **Stakeholder Alignment:** Future communications regarding retail out-of-home scope and Smart Cart will involve Yi Hao instead of Nikhil Grover.

**Pending Actions & Ownership**
*   **Action:** Re-liaise on the Smart Cart project when bandwidth permits.
    *   **Owner:** Ching Hui Ng (to coordinate with Yi Hao).
*   **Action:** Incorporate Yi Hao into future discussions regarding retail out-of-home scope.
    *   **Context:** Nikhil has handed over this specific scope to Yi Hao to accelerate progress while he focuses on onsite work.

**Key Dates & Follow-ups**
*   **Original Meeting Date:** March 27, 2026 (Cancelled).
*   **Next Step:** No specific date set; follow-up will occur once bandwidth allows.
*   **Contextual Note:** The decision to pause was driven by the absence of business requirements and an unidentified vendor for Smart Cart integration on the Osmos side.


## [50/61] DPD All Leads
Source: gchat | Group: space/AAAAQezbuRE/KePJESgRBP8 | Last Activity: 2026-03-27T03:09:22.595000+00:00 | Last Updated: 2026-03-27T06:44:57.953915+00:00
**Daily Work Briefing: DPD All Leads Chat Summary (Update)**

**Key Participants & Roles:**
*   **Vincent Wei Teck Lim:** Initiated inquiry; confirmed intent to create a new SDK key; acknowledged short notice.
*   **Jazz Tong:** Provided strategic direction; suggested reverse engineering code for iOS/Android SDKs and advised checking Harness FF SDK compatibility; noted Split API is still functional but migration is pending long-term harmonization.
*   **James Lai Li Hao:** Clarified terminology ("browser key" = client key); shared a legacy Confluence page regarding feature flags and environment guidelines.
*   **Flora Wo Ke:** Engaged in clarifying the request scope; noted familiarity with Jazz's suggestion on reverse engineering.
*   **Komal Ashokkumar Jain:** Highlighted critical time pressure (request received last evening, deadline earlier today morning).
*   **Winson Lim:** Acknowledged incoming external replies.

**Main Topic:**
Creation of a new Split SDK key for the "Everything Food" implementation on OneApp and validation of current vs. legacy integration methods following Split.io's partial migration to Harness.

**Decisions & Clarifications Made:**
*   **Terminology Update:** James Lai Li Hao clarified that the previously discussed "browser key" is synonymous with the "client key."
*   **Technical Path Forward:** Jazz Tong proposed using AI for reverse engineering existing code to generate new iOS/Android SDKs for OneApp as an immediate workaround.
*   **Legacy vs. Current State:** Jazz Tong confirmed Split.io API remains functional; however, a full migration to Harness FF SDK is ongoing and not yet complete.
*   **Documentation Alignment:** Vincent Wei Teck Lim confirmed the team is currently reviewing the shared Confluence page regarding client-side browser keys.

**Pending Actions & Ownership:**
*   **Urgent Resolution:** The team must resolve the new key generation by today morning, despite the short notice (received last evening).
*   **SDK Generation:** Vincent Wei Teck Lim to proceed with generating the key, potentially utilizing Jazz Tong's suggestion of reverse engineering code if standard methods are delayed.
*   **Harness Validation:** Komal Ashokkumar Jain and Jazz Tong to verify if the new Harness Feature Flag (FF) SDK is usable for this specific requirement.
*   **Documentation Review:** Team to finalize review of the Confluence page: *Split.io feature flags and environment guidelines*.
*   **Communication:** Vincent Wei Teck Lim apologized for the short notice and committed to minimizing such occurrences in the future.

**Key References & Dates:**
*   **Date of Discussion:** March 27, 2026 (01:43 – 03:09 UTC).
*   **Legacy Reference:** "Koklin" identified by Vincent and James as a potential original creator ("he is the bible").
*   **Resources Cited:**
    *   *Confluence Page:* https://ntuclink.atlassian.net/wiki/spaces/DPD/pages/2000585047/Split.io+feature+flags+and+environment+guideliens (Shared by James Lai Li Hao; referenced as "long lost" by OKTA).
    *   *Harness Developer Hub:* Before and After Guide: API for Split Admins.

**Status:** **Critical/Urgent**. The team has pivoted from historical investigation to immediate execution under tight time constraints. Jazz Tong's suggestion to use AI reverse engineering or verify Harness FF SDK compatibility serves as the primary alternative path while the standard key creation process is validated against the legacy Confluence documentation.


## [51/61] DPD Incidents
Source: gchat | Group: space/AAAAEsAEG84 | Last Activity: 2026-03-27T02:58:14.109000+00:00 | Last Updated: 2026-03-27T06:45:45.235596+00:00
**Daily Work Briefing: DPD Incidents – HCBP Picking Queue Issue**

**Key Participants & Roles**
*   **Ler Whye Ling Angel:** Initiator of the incident report; flagged a critical operational blocker.
*   **Gopalakrishna Dhulipati:** Key participant in the 17-reply thread discussing the issue (Role inferred as technical support or operations lead).
*   **Winson Lim:** Key participant in the 17-reply thread discussion (Role inferred as technical support or operations lead).

**Main Topic/Discussion**
The conversation centers on a system outage where **no orders are appearing in the picking queue for HCBP**. Angel flagged this issue at **2026-03-27T02:58:14.109Z**, stating, "Please assist as there is no order in the picking Q till now for HCBP." The thread generated significant engagement (17 replies) and concluded with a follow-up discussion at **04:54 AM**.

**Pending Actions & Ownership**
*   **Action:** Investigate and resolve the root cause of missing orders in the HCBP picking queue.
*   **Action:** Restore order flow to allow picking operations to proceed for HCBP.
*   **Ownership:** The issue was directed at **Gopalakrishna Dhulipati** and **Winson Lim** via tag, indicating they are responsible for troubleshooting and resolution.

**Decisions Made**
No explicit decisions or resolutions were recorded in the provided metadata snippet; however, the engagement of two specific team members indicates an active investigation into the queue failure is underway.

**Key Dates & Deadlines**
*   **Incident Reported:** 2026-03-27, 02:58:14 UTC.
*   **Last Activity:** 04:54 AM (Timezone not specified in snippet; assumed local to chat space).
*   **Thread Duration:** Approximately 2 hours of active discussion and reply activity.

**Contextual References**
*   **Resource Name:** DPD Incidents.
*   **Space URL:** https://chat.google.com/space/AAAAEsAEG84.
*   **Specific System Issue:** "No order in the picking Q" for HCBP.


## [52/61] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/GjGHRIi5T-E | Last Activity: 2026-03-27T02:33:15.491000+00:00 | Last Updated: 2026-03-27T06:47:20.607035+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles:**
*   **Prajney Sribhashyam:** Requester of E2E production test; clarifies deployment urgency and adds @De Wei Tey to the refund discussion.
*   **Sneha Parab:** Reports on MP order sync issues, revert status, and identifies additional participants needed for refund/GI discussions.
*   **Andin Eswarlal Rajesh, Daryl Ng:** Tagged for testing; identified by Sneha as potential attendees for the refunds workflow discussion.
*   **De Wei Tey:** Newly added participant to the refund discussion thread.

**Main Topic:**
Coordination of an End-to-End (E2E) production test scheduled for March 27, 2026, covering App Experience, Order Placing, and Order Posting. The focus shifted from testing MP order sync fixes immediately to prioritizing a separate alignment session on refunds and GI adjustments, while ensuring the deployed fix addresses overnight BCRS unit count and price info issues in DF reports.

**Pending Actions & Owners:**
*   **Deploy Sync Fix:** Sneha has a tested fix for MP order sync (reverting the change causing errors). Prajney confirmed this is "not needed" for the current E2E test but instructed to get the fix deployed soon.
*   **Refunds & GI Alignment Session:** A specific discussion is required regarding refunds still in UAT and their integration with General Inventory (GI) adjustments. Sneha needs to confirm if @Daryl Ng requires additional attendees; Prajney confirmed adding @De Wei Tey to this call.
*   **Validate Reversal Process:** Alignment remains required between Prajney and Adrian regarding order return and stock reversal processes, previously raised in the Deployment Planning Session with Onkar.

**Decisions Made:**
*   **Test Scope Adjustment:** The MP order sync fix (BCRS unit count & price info) is excluded from the immediate E2E production test scope to avoid surprises on production, though it must be deployed soon.
*   **Deployment Strategy:** The team reverted the change causing nightly sync issues immediately. A separate deployment for the available fix will occur after further validation and alignment on refunds, rather than as part of the main test run.
*   **Meeting Expansion:** The refund discussion meeting will include @De Wei Tey in addition to existing stakeholders.

**Key Dates, Deadlines, and Follow-ups:**
*   **March 27, 2026 (01:17):** Sneha reported MP order sync issues and confirmed the revert.
*   **March 27, 2026 (02:31):** Prajney clarified that the fix is not needed for the current test but must be deployed soon.
*   **March 27, 2026 (02:32):** Sneha confirmed alignment needs to prevent production surprises and queried additional call attendees.
*   **March 27, 2026 (02:33):** Prajney added @De Wei Tey to the refund discussion thread.
*   **Immediate Follow-up:** Schedule a session between Prajney, Adrian, Daryl Ng, and De Wei Tey to align on the refund/reversal workflow before finalizing deployment attempts.

**Link:** [BCRS Firefighting Group Chat](https://chat.google.com/space/AAQAgT-LpYY)


## [53/61] @omni-ops #standup - Mar 27
Source: gchat | Group: space/AAQAz751zBQ | Last Activity: 2026-03-27T02:02:10.051000+00:00 | Last Updated: 2026-03-27T02:42:34.236887+00:00
**Daily Work Briefing: #standup Channel**
**Date:** March 27, 2026
**Source:** Google Chat (#omni-ops)

**1. Key Participants and Roles**
*   **Yangyu Wang:** Initiator of the standup check-in (Role inferred as team member or lead initiating daily sync).
*   **Audience/Participants:** "Viewed by 5 of 8" indicates an active channel presence, though specific roles for the other viewers are not explicitly stated in this log.

**2. Main Topic/Discussion**
The conversation consisted of a single query regarding the status or initiation of the daily standup meeting. No substantive project updates, blockers, or technical discussions were recorded in this snapshot.

**3. Pending Actions and Ownership**
*   **Action:** Commence the standup meeting.
    *   **Owner:** Unclear/Unassigned (The initiator, Yangyu Wang, asked "standup?" but did not assign a specific facilitator in this message).
    *   **Status:** Pending initiation based on the query.

**4. Decisions Made**
*   No formal decisions were recorded in this conversation log. The interaction remains an open inquiry.

**5. Key Dates, Deadlines, and Follow-ups**
*   **Event Date/Time:** March 27, 2026, at 02:02:10 UTC.
*   **Follow-up Required:** Confirmation of standup status or the start of the meeting itself to ensure the team sync proceeds as scheduled.

**Summary Note:** The log reflects a single timestamped message from Yangyu Wang prompting for the daily standup. Further details regarding project status, blockers, or outcomes are not available in this specific conversation excerpt.


## [54/61] [BCRS]-SAP to POS & DBP Interface Deployment
Source: gchat | Group: space/AAQAeMC3qBk/3a5kvSWZa-g | Last Activity: 2026-03-27T01:46:35.052000+00:00 | Last Updated: 2026-03-27T02:43:08.464635+00:00
### Daily Work Briefing: [BCRS]-SAP to POS & DBP Interface Deployment

**Key Participants & Roles**
*   **Michael Bui:** Execution lead; confirmed initial deployment success but noted no BCRS deposit data is currently available in PRD.
*   **Onkar Bamane:** Stakeholder/Coordinator; managing the smoke test strategy and liaising between SAP, DBP, and MP teams.
*   **Sneha Parab:** Point of contact for MP (Mirakl); coordinating testing schedules and stakeholder comms regarding deposit SKUs.
*   **Hendry Tionardi:** Technical analyst; identified the root cause as an empty database table awaiting data population on April 1st.
*   **Shiva Kumar Yalagunda Bas:** Reported initial failure to update SAP product names for specific MP SKUs.
*   **Olivia -:** Involved in downstream impact assessment regarding POS charging before April 1st.

**Main Topic**
Post-deployment monitoring of the **[BCRS]-SAP to POS & DBP Interface**. While the deployment itself was error-free, immediate issues arose regarding missing BCRS deposit data for MP SKUs, preventing successful product updates and linking. The focus shifted from general monitoring to troubleshooting a data availability gap between SAP production tables and downstream systems.

**Pending Actions & Owners**
*   **Smoke Test Setup:** Onkar Bamane will maintain one dummy SKU (for 1, 6, and 12 qty) temporarily for testing purposes; it will be removed post-test.
    *   *Owner:* Onkar Bamane
*   **MP SKU Creation Testing:** Sneha Parab to inform PIC availability on Mirakl to create a dummy SKU for the smoke test. A meeting is scheduled for March 27 at 11:00 UTC.
    *   *Owners:* Sneha Parab, Hendry Tionardi, Onkar Bamane
*   **Data Synchronization:** Wait for full BCRS deposit data to be maintained in SAP on the afternoon of March 31, 2026. MP BCRS SKU approval cannot proceed until then.
    *   *Owner:* Sneha Parab (to inform Cheryl & Amos)

**Decisions Made**
*   The initial deployment at 14:20 UTC on March 26 was successful; however, the system currently shows no deposit SKUs in SAP because the source table is empty.
*   The empty table state is expected to resolve on **April 1st**, when data population occurs.
*   A temporary workaround (maintaining a single test SKU) was approved by Onkar Bamane to allow smoke testing before full data availability.
*   MP BCRS SKU approval processes are paused pending the March 31 data maintenance window.

**Key Dates & Follow-ups**
*   **Deployment Date:** March 26, 2026, at 14:20 UTC.
*   **Data Availability Timeline:** Full data maintained on March 31 afternoon; table populates April 1.
*   **Smoke Test Meeting:** March 27, 2026, at 11:00 UTC (Google Meet link provided by Sneha Parab).
*   **Next Update:** Sneha Parab to confirm PIC availability for dummy SKU creation and provide alignment steps before the test meeting.

**Resource Reference**
*   **Chat URL:** https://chat.google.com/space/AAQAeMC3qBk


## [55/61] DPD All Leads
Source: gchat | Group: space/AAAAQezbuRE | Last Activity: 2026-03-27T01:43:42.350000+00:00 | Last Updated: 2026-03-27T02:43:31.929104+00:00
**Daily Work Briefing: DPD All Leads Space**

**Key Participants & Roles**
*   **Vincent Wei Teck Lim:** Lead (Inquired on CNY support migration; Investigating SDK key history).
*   **Natalya Kosenko:** Lead (Proposed Zendesk group update strategy).
*   **Alvin Choo:** Lead (Raised HR performance feedback protocol).
*   **Tan Nhu Duong:** Lead/Informant (Provided critical calibration rating visibility warning).
*   **Michael Bui:** Team Member/Analyst (Flagged data spike anomaly).
*   **Winson Lim:** Lead/New Inquiry (Raised food tile decommissioning concerns).
*   **Komal Ashokkumar Jain:** Identified as the likely owner of the split SDK key creation.

**Main Topics & Discussions**
1.  **CNY Support Transition (Mar 2):** Vincent raised the question of migrating on-call support from temporary resources to the core team as CNY support concludes.
2.  **Zendesk Group Management (Mar 4):** Natalya discussed updating Zendesk groups for Gomathi, proposing a centralized email notification rather than individual adhoc requests.
3.  **HR Performance Feedback & Reporting Lines (Mar 4–10):** Alvin requested guidance on inviting both old and new Reporting Officers (ROs) to 1-on-1 performance feedback sessions due to recent reporting line changes. Tan subsequently warned that former managers cannot see final calibrations; only the *new* RO sees the final rating.
4.  **Data Anomaly Investigation (Mar 16):** Michael identified a sudden spike in `popup_myinfo_unverified` events within Segment data specifically on March 13, seeking verification and contact points for resolution.
5.  **Food Tile & Service Decommissioning (Mar 20 – Mar 27):**
    *   On **Mar 20**, Winson Lim noted the discontinuation of the food tile due to recent events and raised concerns regarding associated service decommissioning.
    *   On **Mar 27**, Vincent Wei Teck Lim initiated an inquiry to identify the specific individual responsible for creating the split SDK key during the initial implementation of the "everything food" feature, tagging @all and receiving a response from Komal Ashokkumar Jain.

**Decisions Made**
*   None explicitly recorded as final decisions in the provided snippets. Discussions remain in inquiry or information-sharing phases regarding support migration, notification strategy, feedback protocols, data validation, service decommissioning, and SDK key history.

**Pending Actions & Owners**
*   **Confirm CNY Support Migration Plan:** Owner: TBD (Vincent initiated). Needs confirmation on whether to migrate to the core team.
*   **Finalize Zendesk Update Strategy:** Owner: Natalya/Kosenko. Decision needed on executing a centralized email vs. adhoc updates for Gomathi's group access.
*   **Verify Final Performance Ratings:** Action: Old ROs must consult new ROs before communicating final ratings to avoid discrepancies (e.g., Green+ vs. Gold). Owner: All Managers/Leads involved in feedback sessions.
*   **Investigate Segment Data Spike:** Owner: TBD/Michael Bui. Requires identifying the source of the `popup_myinfo_unverified` spike on 13/03 and verifying with the relevant team.
*   **Assess Food Tile & Service Decommissioning:** Owner: TBD (Winson Lim initiated). Needs strategic input on whether to proceed with decommissioning services linked to the food tile following its removal.
*   **Document Split SDK Key History:** Action: Verify Komal Ashokkumar Jain's involvement or identify the original creator of the split SDK key for "everything food" to aid in potential decommissioning or troubleshooting efforts. Owner: Vincent Wei Teck Lim (Lead inquiry).

**Key Dates & Deadlines**
*   **Mar 2, 2026:** CNY support close inquiry raised.
*   **Mar 4, 2026:** Zendesk update discussion; HR performance feedback month begins.
*   **Mar 13, 2026:** Date of the Segment data spike requiring investigation.
*   **March (Ongoing):** HR Performance Feedback Month (1-on-1s).
*   **Mar 20, 2026:** Winson Lim raised food tile and service decommissioning inquiry.
*   **Mar 27, 2026:** Vincent Wei Teck Lim inquired about the split SDK key creator; Komal Ashokkumar Jain replied to the thread.


## [56/61] [BCRS]-ECOM Flow Deployment - Mar 27
Source: gchat | Group: space/AAQAPK5pWxQ | Last Activity: 2026-03-26T16:11:02.982000+00:00 | Last Updated: 2026-03-27T02:57:53.151637+00:00
**Daily Work Briefing: [BCRS]-ECOM Flow Deployment**

**Key Participants & Roles**
*   **Shiva Kumar Yalagunda Bas:** Reported deployment failure status. (Note: Participant role inferred as technical lead or engineer based on monitoring activity).
*   **Unspecified Team Members:** 9 out of 11 participants viewed the conversation, indicating broad team visibility on the incident.

**Main Topic**
Investigation and reporting regarding a recurring failure in the **[BCRS]-ECOM Flow Deployment**. The discussion centers on a specific timestamp where the deployment process failed to complete successfully.

**Status & Actions Pending**
*   **Issue Confirmation:** A deployment failure was confirmed occurring at **12:05 am**.
*   **Owner:** **Shiva Kumar Yalagunda Bas** identified the failure but no further resolution steps or ownership for remediation is explicitly stated in the provided log.
*   **Next Steps:** Immediate dependency on root cause analysis to address why the flow fails at this specific time slot (12:05 am).

**Decisions Made**
*   No formal decisions, approvals, or strategic pivots were recorded in this 7-minute exchange. The interaction was limited to status reporting.

**Key Dates & Deadlines**
*   **Failure Timestamp:** **12:05 am** (Time of deployment failure).
*   **Report Date:** **March 26, 2026**.
    *   Failure reported at **16:06:24 UTC**.
    *   Message viewed by team at **16:11:02 UTC**.
*   **Reference Document:** "Resource: [BCRS]-ECOM Flow Deployment - Mar 27" (Note: The resource title suggests the deployment is targeted for or associated with March 27, while the incident occurred on March 26).

**Summary of Incident**
On March 26, 2026, Shiva Kumar Yalagunda Bas reported that the [BCRS]-ECOM Flow Deployment "still fails" specifically at **12:05 am**. The issue appears to be a recurring problem given the use of the word "still." The conversation was visible to the majority of the team (9/11 members) shortly after being posted. No resolution or corrective action plan is currently documented in this specific chat segment.


## [57/61] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4 | Last Activity: 2026-03-26T14:39:28.616000+00:00 | Last Updated: 2026-03-27T02:59:01.520039+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Space Creator; Lead coordinating the briefing.
*   **Daryl Ng, Gopalakrishna Dhulipati, Tiong Siong Tee, Michael Bui, Akash Gupta:** Designated "Project Light Attack and Defence Leads".
*   **Hui Hui Voon:** Owner of the D&T Scope for Project Light Workshop document.
*   **Pauline Pong:** Owner of promotion conflict test case file.
*   **Jacob Yeo:** Edited CDTO Internal RFP requirements file on March 25, 2026.
*   **Sophia:** Contacted by Michael Bui regarding CoMall coordination (March 26).

**Main Topic**
Following the transition to active strategic planning ("Room 2") on March 24, the team is finalizing specific slide preparation within six "Spotlight Topics." While Alvin Choo initiated collaboration on **"RMN"** and **"Payment"** slides on March 24, a new flexibility protocol was established on March 25 allowing leads to attend other meetings (e.g., BCRS) if required. Concurrently, technical direction has shifted toward decoupling from SAP, with consensus that SAP should serve primarily for finance and sales records purposes. New RFP documentation and promotion conflict testing cases have been identified for review. On March 26, the discussion expanded to data infrastructure specifics and CoMall integration strategy. Michael Bui reported a preliminary chat with Sophia on March 26 regarding early engagement with CoMall teams to kickstart development.

**Pending Actions & Ownership**
*   **Action:** Finalize content for "RMN" and "Payment" slides in the D&T Scope document.
    *   **Ownership:** Alvin Choo (initiated), Hui Hui Voon (Document Owner).
    *   **Status:** In progress; collaboration initiated March 24, ~9:32 AM UTC.
*   **Action:** Review "Promotion Conflict Test Case_05.NOV.20" and summarize the file for Alvin Choo.
    *   **Ownership:** Michael Bui (requested by Alvin Choo on March 25, ~2:46 AM UTC). Note: Access was initially denied to Alvin Choo on March 25, 2:51 AM UTC.
*   **Action:** Review "[CDTO Internal] Project Light Requirements for RFP by MVP Scope.xlsx".
    *   **Ownership:** Gopalakrishna Dhulipati (Owner). Jacob Yeo edited this file on March 25, 2026. Alvin Choo shared the link on March 25, ~3:56 AM UTC for summary.
*   **Action:** Clarify backend API responsibilities with CoMall regarding personalization and orchestration.
    *   **Ownership:** Michael Bui (to note and document).
*   **Action:** Identify the owner managing data indexing to Algolia.
    *   **Ownership:** Daryl Ng raised this query on March 26, ~1:55 AM UTC; team response pending in chat space (10 replies noted).
*   **Action:** Finalize the Attack/Defence team composition pending Dennis's confirmation following Alvin Choo's email.
    *   **Ownership:** Alvin Choo.
*   **Action:** Address technical clarifications raised by Tiong Siong Tee regarding Inventory visibility, Corporate Control alignment, and Product management portal structure (FP vs. Sellers).
    *   **Ownership:** Alvin Choo and Gopalakrishna Dhulipati.
*   **New Action:** Confirm CoMall contract status and determine timing for creating a dedicated GChat space with CoMall teams.
    *   **Ownership:** Michael Bui (initiated inquiry on March 26, ~14:39 UTC); pending confirmation from Alvin Choo or Gopalakrishna Dhulipati regarding "grooming next week" vs. immediate kickoff.

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
*   **RFP File Sharing & Review Request:** March 25, 2026 (~3:56 AM UTC) – Alvin Choo shared the "Project Light Requirements for RFP by MVP Scope" file.
*   **Test Case Identification:** March 25, 2026 (~2:46 AM UTC) – Michael Bui identified "Promotion Conflict Test Case_05.NOV.20" (Owner: Pauline Pong); Alvin Choo noted access issues at ~2:51 AM UTC.
*   **Algolia Indexing Query:** March 26, 2026 (~1:55 AM UTC) – Daryl Ng asked "who is managing the indexing of the data to Algolia?" with 10 replies recorded.
*   **CoMall Strategy Inquiry:** March 26, 2026 (14:39 UTC) – Michael Bui queried contract confirmation and GChat creation timing following a chat with Sophia; discussion currently active with 9 replies.
*   **Session Start ("Room 2"):** March 24, 2026 (1:02 AM UTC).
*   **Spotlight Topics List Published:** March 24, 2026 (3:14 AM UTC).
*   **Email Sent for Team Confirmation:** March 24, 2026 (3:51 AM UTC) by Alvin Choo.


## [58/61] GE Connect
Source: gchat | Group: space/AAQASkvSlwo | Last Activity: 2026-03-26T14:32:33.384000+00:00 | Last Updated: 2026-03-27T03:00:23.936000+00:00
**Daily Work Briefing: GE Connect – Polly Launch & Incident Report**

**Key Participants & Roles**
*   **Sip Khoon Tan:** Announcer/Presenter; introduced the AI agent "Polly."
*   **Oktavianer Diharja:** Identified a critical functional issue regarding agent routing.
*   **Sunny Lim:** Reported UI limitations in the NotebookLM studio interface.
*   **Team (GE FPG):** Primary audience and users experiencing reported incidents.

**Main Topic & Discussion**
The discussion centers on the launch of **Polly**, an AI agent for FPG Policy Assistance, alongside newly identified technical failures in both routing logic and user interface capabilities.
*   **Launch Overview:** Polly is designed to streamline policy inquiries via instant answers and source citations through the Workbench (`work.fpg.sg`).
*   **Incident Report 1 (Routing):** On March 26, 2026, Oktavianer Diharja reported a hallucination where the GE workflow incorrectly routed queries from the "Confluence agent" to the "Jira agent," yielding misleading responses.
*   **Incident Report 2 (UI/Feature Limitation):** Sunny Lim noted that the NotebookLM studio tab is restricted to only four types and lacks an "Infographic" option, limiting content creation capabilities.

**Decisions Made**
*   **Deployment Strategy:** Polly remains the primary interface for policy questions, though adoption is currently on hold pending fixes.
*   **Access Routing:** Access is routed through the Workbench (`work.fpg.sg`) and Vertex AI Search.
*   *Update:* Reliability of cross-agent routing (Confluence to Jira) is compromised. Additionally, the NotebookLM studio interface requires feature expansion to include Infographic generation.

**Pending Actions & Owners**
*   **Action:** Investigate routing logic error causing Confluence-to-Jira switch and misleading responses.
    *   **Owner:** Engineering/Development Team.
*   **Action:** Validate accuracy of Jira agent's response regarding Oktavianer Diharja's specific case.
    *   **Owner:** Technical Lead / SMEs.
*   **Action:** Investigate and resolve the missing "Infographic" option in NotebookLM studio to expand the four available types.
    *   **Owner:** Engineering/Development Team (NotebookLM Integration).
*   **Action:** Test functionality for both routing stability and UI completeness before full team reliance.
    *   **Owner:** All team members (pending resolution of bugs/features).

**Key Dates & Follow-ups**
*   **Original Launch Date:** March 20, 2026.
*   **Incident Report Date (Routing):** March 26, 2026 (11:56 AM UTC).
*   **UI Issue Reported:** March 26, 2026 (approx. 2:32 PM UTC per metadata timestamp).
*   **Last Reply Time:** 8:22 AM (Current thread activity); Latest UI discussion reply at 1:07 AM.
*   **Reference URL:** `https://chat.google.com/space/AAQASkvSlwo`
*   **Direct Access Links:**
    *   Polly Agent Link: `http://vertexaisearch.cloud.google.com/home/cid/7c7eb665-e9c4-4276-ab72-3269644e5a4b/r/agent/14958526149084864719/session/-?pli=1`
    *   Workbench Portal: `http://work.fpg.sg`

**Status**
The initiative is **active but interrupted by multiple critical incidents**. While launched on March 20, 2026, adoption is stalled due to a reported hallucination involving agent switching (Confluence to Jira) and misleading data. Furthermore, the NotebookLM studio interface has been flagged for having only four content types, specifically missing an "Infographic" option. The chat log indicates unresolved technical debt with 3 unread items and multiple replies regarding these specific issues. Full team adoption remains on hold until routing logic is corrected and the UI feature gap (Infographics) is addressed.


## [59/61] OMS x CS
Source: gchat | Group: space/AAAAUPoVWjI | Last Activity: 2026-03-26T13:32:52.621000+00:00 | Last Updated: 2026-03-26T14:38:08.188942+00:00
**Daily Work Briefing: OMS x CS Resources (Updated)**

**Key Participants & Roles**
*   **Sampada Shukla:** Customer Support (CS) agent.
*   **Wai Ching Chan:** CS representative flagging operational process gaps regarding customer profile merging.
*   **Raine Lee:** CS representative reporting notification delivery failures, including a new NPS feedback loop.
*   **Gomathi Panneerselvam & Gopalakrishna Dhulipati:** IT/Operations personnel involved in resolving reported issues.
*   **Binte Abdul Karim Kamilah:** CS agent escalating billing discrepancy inquiries from the GCEO channel.

**Main Topics**
1.  **Access Control:** Critical lockout of CS agent Sampada Shukla from Zendesk due to MFA/SMS 2FA failures (March 4). Resolution pending.
2.  **Process Integrity:** Recurring disruption caused by merging customer profiles without validating pending orders, leading to stalled workflows (Orders #255985725 and others).
3.  **System Reliability & Billing Discrepancies:**
    *   Historical failure of SMS/PNS delivery for Order #256547454 (March 12).
    *   Missing order confirmation emails for Orders #257969203, #257279251, and #256369211 (Ticket #4449487), linked to an NPS survey submission.
    *   **New Incident:** Customer complaint via GCEO regarding unjustified charges for drop-off items in Order #256906035. The invoice reflected a charge of $93.50 for Item 491697 (Haagen-Dazs Ice Cream - Strawberry, Qty 6), despite DBP logs and internal records confirming the item was marked as "drop off" and fully fulfilled.

**Pending Actions & Ownership**
*   **Reset MFA:** IT support must reset Sampada Shukla's Multi-Factor Authentication immediately to restore Zendesk access. (*Owner: IT Team*)
*   **Process Validation Protocol:** CS and Customer Data Management (CDM) teams need to implement a mandatory validation check for open/pending orders before executing customer profile merges. (*Owner: CS & CDM Teams*)
*   **Investigate Email Delivery Failure:** Verify backend logs for Ticket #4449487 to confirm successful dispatch of order confirmation emails for the three affected orders (#257969203, #257279251, #256369211). Compare against historical delivery metrics. (*Owner: Technical/Operations Team*)
*   **Investigate Notification Failure (Legacy):** Proceed with technical review for SMS/PNS triggers failing on Order #256547454 (Customer: btsoh268@gmail.com) as previously planned. (*Owner: Technical/Operations Team*)
*   **Investigate Billing Discrepancy:** Review Invoice vs. DBP Logs for Order #256906035 to explain the $93.50 charge on drop-off item 491697 and respond to the customer's GCEO request. (*Owner: Operations/Billing Team*)

**Decisions Made**
*   No formal decisions recorded in the chat log; however, **Wai Ching Chan** explicitly identified a systemic risk requiring a protocol change between CS and CDM to prevent future order processing blocks during profile merges.
*   **New Context:** The NPS survey submission for Ticket #4449487 elevates the email delivery issue from a routine check to a customer satisfaction concern requiring priority verification.
*   **Escalation Protocol:** Binte Abdul Karim Kamilah has escalated the billing anomaly in Order #256906035 due to its origin from a GCEO inquiry, necessitating immediate root cause analysis of the charge logic failure.

**Key Dates & References**
*   **March 4, 2026:** Sampada Shukla reported Zendesk lockout (SMS 2FA issue). Last reply recorded March 4 at 4:41 AM.
*   **March 7, 2026:** Customer profile UID `4815537039166279` merged into UID `216353592157999833`, stalling Order #255985725.
*   **March 9, 2026:** Wai Ching Chan escalated the merge issue at 6:13 AM. Last reply recorded Thursday at 11:11 AM.
    *   *Affected Order Link:* `https://admin.fairprice.com.sg/customer-support/sale-orders/255985725`
    *   *Customer Profile Link:* `https://admin.fairprice.com.sg/customer-support/customers/view/1067653`
*   **March 12, 2026:** Raine Lee reported SMS/PNS delivery failure for Order #256547454. Last reply recorded at 12:00 AM.
*   **March 24, 2026 (03:58 AM):** Raine Lee raised Ticket #4449487 regarding missing order confirmation emails for three recent orders (#257969203, #257279251, #256369211). Customer submitted NPS survey. Last reply recorded 5:13 AM.
*   **March 26, 2026 (13:32 UTC):** Binte Abdul Karim Kamilah raised Ticket #4446136 regarding the billing discrepancy for Order #256906035 ($93.50 charge on drop-off item 491697).


## [60/61] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/jG0L_VCljVA | Last Activity: 2026-03-26T13:02:30.327000+00:00 | Last Updated: 2026-03-26T14:38:22.568646+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Meeting/Channel Resource:** [Internal] Digital Product Development Space
**Date of Discussion:** March 26, 2026
**Reference Link:** https://admin.fairprice.com.sg/customer-support/customers/view/2022036

### 1. Key Participants & Roles
*   **Wai Ching Chan:** Issue reporter (Customer Support/Product). Identified the bug affecting order time slot changes for iOS users with emoji in addresses.
*   **Sneha Parab:** Service Owner verification. Currently determining ownership of the `address-service`.
*   **Michael Bui:** Product/Development inquiry. Questioned the technical root cause regarding emoji breaking the flow.
*   **Gopalakrishna Dhulipati & Dang Hung Cuong:** Tagged stakeholders for visibility.

### 2. Main Topic
Investigation into a bug where customer addresses containing **emoji icons** (specifically on iOS) prevent users from changing order time slots, requiring manual resolution in the admin panel. The discussion focuses on validating if emojis are currently blocked during address creation or editing and identifying the service responsible for this logic.

### 3. Pending Actions & Ownership
*   **Action:** Validate whether emoji icons block adding/editing addresses.
    *   **Owner:** To be determined (Immediate follow-up required).
*   **Action:** Identify the current owner of `address-service`.
    *   **Owner:** Sneha Parab (currently investigating).

### 4. Decisions Made
No final decisions or resolutions were reached during this conversation thread. The group is currently in the diagnostic and ownership identification phase.

### 5. Key Dates & Follow-ups
*   **Issue Date:** March 26, 2026.
    *   Initial report: 10:35 UTC (Wai Ching Chan).
    *   Service ownership check initiated: 11:10 UTC (Sneha Parab).
    *   Root cause inquiry raised: 13:02 UTC (Michael Bui).
*   **Follow-up Required:** Confirmation of `address-service` ownership and execution of the emoji validation test.

**Specific References:**
*   **Customer ID:** 2022036
*   **Platform Impact:** iOS users only (reported via admin link).
*   **Impact Scope:** Manual intervention required for order time slot changes.


## [61/61] RMN Incidents
Source: gchat | Group: space/AAQAz11ATzY/JzqdqNaNWpo | Last Activity: 2026-03-26T13:00:42.163000+00:00 | Last Updated: 2026-03-26T14:39:07.311447+00:00
**Daily Work Briefing: RMN Incidents**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator of the incident report; identified a critical product ad performance drop.
*   **Rachit Sachdeva:** Point of contact for internal investigation; confirmed issue acknowledgment.
*   **Michael Bui:** Stakeholder requesting timeline for the next status update.
*   **Other Stakeholders (CC'd):** Shubhangi Agrawal, Allen Umali, Rajiv Kumar Singh, Ravi Goel.

**Main Topic**
A high-priority incident regarding a **50% drop in product ad impressions** since March 17, 2026. The decline is isolated to search and category pages despite stable request/response trends. The root cause hypothesis suggests a reduction in the number of SKUs per response (dropping from 4–5 SKUs to a single product). This anomaly has resulted in an **$11k revenue loss** compared to the previous nine-day period.

**Pending Actions & Ownership**
*   **Action:** Investigate and confirm the hypothesis regarding SKU reduction per response.
*   **Owner:** Rachit Sachdeva (confirmed internal ticket raised).
*   **New Action:** Provide a timeline/status update on the investigation.
*   **Status:** In progress; awaiting next update from Rachit Sachdeva following Michael Bui's inquiry at 13:00 UTC on March 26, 2026.

**Decisions Made**
No final decisions or root cause confirmations were reached during this exchange. The discussion remains in the triage and hypothesis confirmation phase. A follow-up update is now explicitly requested by Michael Bui.

**Key Dates & Follow-ups**
*   **Incident Start Date:** March 17, 2026 (start of impression drop).
*   **Report Date:** March 26, 2026.
    *   Issue raised: 09:40 UTC by Nikhil Grover.
    *   Internal ticket raised: 09:42 UTC by Rachit Sachdeva.
    *   Follow-up request: 13:00 UTC by Michael Bui asking for the next update timeline.
*   **Data Window Cited:** Past 7 days (as of March 26).
*   **Follow-up Required:** Rachit Sachdeva to provide an update on the internal investigation status in response to Michael Bui's query.

**Resource Reference**
*   **Space/URL:** https://chat.google.com/space/AAQAz11ATzY
