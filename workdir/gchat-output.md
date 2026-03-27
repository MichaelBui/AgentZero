

## [1/85] RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Messages: 24 | Last Activity: 2026-03-27T02:30:49.056000+00:00 | Last Updated: 2026-03-27T02:39:04.092790+00:00
**Daily Work Briefing: Automated Test Results Summary (RMN Notification)**

**Key Participants & Roles**
*   **Collection Runner App:** Automated testing agent executing API suites.
*   **Webhook Bot:** Reporting mechanism; consistently returning "unable to process your request" on all notifications through March 27, 2026.
*   **Parties Involved:** System-generated notification log only.

**Main Topic/Discussion**
Automated nightly API test executions across `promo-service`, `marketing-personalization-service`, and `marketing-service` in the **staging** environment. Monitoring period spans March 12 through **March 27, 2026**. Execution windows occur at approximately 01:05 UTC (morning), 02:30/02:31 UTC (midnight), and **03:20/03:21 UTC** (early morning).

**Test Execution Status & Anomalies**
*   **Stable Services:**
    *   `promo-service`: Confirmed stable on March 26 (02:31 UTC) and **March 27 at 02:30 UTC**. The latest run on March 27 showed **10 API Passed / 0 Failed** and **6 Contract Tests Passed / 0 Failed**.
    *   `marketing-personalization-service`: Stable execution continues through March 26 (03:21 UTC) with 96 API/126 Contract tests passing. No new logs reported for this service on March 27 in the provided feed, but stability is maintained from previous runs.
*   **`marketing-service` Stability Confirmation:**
    *   **Historical Context:** Recurring instability persisted from March 17 through early March 25 (characterized by exactly 2 failed API tests). A temporary stabilization occurred on March 25; the morning failure streak was broken on March 26.
    *   **Current Status (March 27):** The streak of resolution continues. At **01:05 UTC** on **March 27**, `marketing-service` executed successfully with **53 API Tests Passed / 0 Failed** and **20 Contract Tests Passed / 0 Failed**.
    *   **Total Requests:** March 27 run recorded 17 total API requests and 16 contract test requests, all passing.

**Pending Actions & Ownership**
*   **Webhook Bot Remediation (High Priority):** The bot failed to process requests in every notification cycle from March 12 through the latest log on **March 27 at 03:21 UTC**. Immediate attention is required from DevOps or Automation Infrastructure.
*   **Verify `marketing-service` Stability:** Engineering must continue monitoring subsequent runs to confirm the resolution of early-morning flakiness observed between March 17–25 was permanent.

**Decisions Made**
*   No human decisions recorded; all entries are automated system outputs.

**Key Dates & Deadlines**
*   **Failure Window (Historical):** Instability noted on March 12, 13, and persistently from **March 17 through March 25**.
*   **Current Status:** Successful runs observed on March 26 and **March 27**.
    *   `marketing-service`: Passed at 01:05 UTC (March 26 & 27).
    *   `promo-service`: Passed at 02:30/02:31 UTC (March 26 & 27).
*   **Monitoring Period:** Data covers runs from **March 12, 2026**, through **March 27, 2026**.

**Resource Info**
*   **Message Count:** 147 notifications logged in the space (updated from 141).
*   **URL:** https://chat.google.com/space/AAQA85dw4So


## [2/85] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/GjGHRIi5T-E | Messages: 9 | Last Activity: 2026-03-27T02:30:36.867000+00:00 | Last Updated: 2026-03-27T02:39:21.058378+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles:**
*   **Prajney Sribhashyam:** Requester of E2E production test; clarifies original plans for refunds/GI adjustments.
*   **Sneha Parab:** Provides status on MP order sync issues, revert actions, and impact analysis regarding DF reports.
*   **Andin Eswarlal Rajesh, Daryl Ng:** Tagged participants for the requested test (no direct input in this thread).

**Main Topic:**
Coordination of an End-to-End (E2E) production test scheduled for "today" (March 27, 2026), specifically addressing App Experience, Order Placing, and Order Posting. The discussion pivoted to address technical blockers regarding MP order sync issues observed overnight involving BCRS unit count and price information required for DF reports.

**Pending Actions & Owners:**
*   **Execute E2E Production Test:** Prajney initiated a request for the team (Andin, Daryl, Sneha) to perform testing today covering App Experience, Order Place, and Order Posting.
*   **Test Refunds Flow & GI Adjustment:** Prajney needs to determine the plan regarding refunds still in UAT and their integration with General Inventory (GI) adjustments.
*   **Clarify Reversal Process:** Alignment is required between Prajney and Adrian regarding the process for returning an order and processing stock reversal, previously discussed in the Deployment Planning Session with Onkar.
*   **Validate Sync Fix:** Sneha has a fix available for MP order sync but requires further testing before re-attempting deployment.

**Decisions Made:**
*   **Scope of Testing:** It was confirmed that Order Logging is part of the scope, though specific impact on seller reports (DF reports) depends on BCRS-eligible MP SKUs becoming available for ordering. Since this feature has not been deployed to production, immediate impact on active reporting is mitigated until eligible SKUs are live.
*   **Revert Status:** The team reverted the change causing MP order sync issues (BCRS unit count & price info) pending further testing of the available fix.

**Key Dates, Deadlines, and Follow-ups:**
*   **March 26, 2026 (22:11):** Prajney requested the E2E production test for "today."
*   **March 27, 2026 (01:17):** Sneha reported MP order sync issues and revert status.
*   **Wednesday (Prior to March 27):** Deployment Planning Session held where Order Reversal/Stock Reversal alignment was raised by Onkar and others.
*   **Immediate Follow-up:** A session is required between Prajney and Adrian to align on the refund/reversal workflow before re-deployment attempts.

**Link:** [BCRS Firefighting Group Chat](https://chat.google.com/space/AAQAgT-LpYY)


## [3/85] DPD All Leads
Source: gchat | Group: space/AAAAQezbuRE/KePJESgRBP8 | Messages: 15 | Last Activity: 2026-03-27T02:30:35.525000+00:00 | Last Updated: 2026-03-27T02:39:37.397841+00:00
**Daily Work Briefing: DPD All Leads Chat Summary**

**Key Participants & Roles:**
*   **Vincent Wei Teck Lim:** Initiated inquiry regarding SDK key creation; leads current troubleshooting effort.
*   **James Lai Li Hao:** Provided technical resources (Split.io docs, Harness guide) and identified potential historical contributors.
*   **Winson Lim:** Clarified context (OneApp internal users) and directed focus to Harness documentation.
*   **Komal Ashokkumar Jain:** Noted team uncertainty but confirmed scope is for internal OneApp users only.
*   **Daryl Ng, Koklin (Steve Dao?), Winson Lim, Jazz Tong (tagged):** Identified as potential historical contributors or secondary contacts.

**Main Topic:**
Investigation into the original creator of the "split SDK key" for the "Everything Food" implementation and determining the current correct procedure to generate new keys following Split.io's integration with Harness.

**Decisions Made:**
*   **Methodology Shift:** The team agreed that legacy documentation is obsolete due to Split.io's integration with Harness.
*   **Action Plan:** Proceed using Harness-specific documentation rather than trial-and-error or old Split.io guides.
*   **Scope Confirmation:** The new key generation is confirmed for internal users on the "OneApp" platform.

**Pending Actions & Ownership:**
*   **Review Documentation:** James Lai Li Hao and Winson Lim have provided links to the *Before and After Guide: API for Split Admins* (Harness Developer Hub) and standard Split.io API documentation.
*   **Further Inquiry:** Vincent Wei Teck Lim will proceed with trial/error or follow up on the new process based on Harness docs.
*   **External Support:** If internal resolution fails, contact support@split.io as suggested in the provided links.
*   **Team Tagging:** Winson Lim tagged **Jazz Tong** (likely for further guidance or ownership), though no specific reply from Jazz is recorded in this thread.

**Key References & Dates:**
*   **Date of Discussion:** March 27, 2026 (01:43 – 02:30 UTC).
*   **Legacy Reference:** "Koklin" identified by Vincent and James as a potential original creator ("he is the bible").
*   **Technical Context:** Split.io has integrated with Harness; old API methods are no longer applicable.
*   **Resources Cited:**
    *   *Create-an-api-key:* https://docs.split.io/reference/create-an-api-key (Noted as potentially outdated).
    *   *Before and After Guide: API for Split Admins:* https://help.split.io/hc/en-us/articles/34773611130893-Before-and-After-Guide-API-for-Split-Admins.

**Status:** Active troubleshooting; team has pivoted from historical investigation to current Harness-based implementation guidance.


## [4/85] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-03-27T02:28:18.688000+00:00 | Last Updated: 2026-03-27T02:40:16.634092+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Late Night Update)**
**Date:** March 26–27, 2026 (Day Shift Extended)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 452

### Key Participants & Roles
*   **System/Tool:** Datadog App (Automated Monitoring)
*   **Notification Channel:** `@hangouts-ShoppingCartNotification`
*   **Ownership Teams:** `dpd-pricing`, `dpd-pricing-cart`.

### Main Topic
Instability persists in `frontend-gateway` and `st-cart-prod`. The incident has evolved from morning oscillation to sustained latency spikes, success rate failures, and a critical SLO error budget breach. Activity extends through 02:28 UTC on March 27.

### Incident Timeline & Actions
**Previous Context:**
*   *Activity from March 20–March 25 regarding `frontend-gateway` latency and checkout dips.*

**New Activity (Late Night Shift, March 26–27 UTC+0)**
*   **19:51 UTC:** [Recovered] P99 of "Get Cart" request (<1.8s threshold) after brief spike.
*   **21:25–21:32 UTC:** Severe latency in "Put Product ID to Wish List". P99 reached **8.365s** (threshold 6.0s); recovered at 21:32 UTC.
*   **23:41–23:43 UTC:** Brief "Put Product ID to Wish List" P90 spike (**5.254s**) recovered immediately.
*   **March 27, 00:04–00:05 UTC:** "Get Wish List by ID" P90 spiked to **1.948s** (threshold 1.7s); recovered at 00:05 UTC.
*   **01:25–01:35 UTC:** Cart success rate dropped to **99.574%** (Monitor `22710472`); recovered to 100% within 10 minutes.
*   **02:22–02:28 UTC:** Clustered latency events:
    *   "Get Wish List by ID" P99 spiked to **3.101s** (threshold 3.1s).
    *   **Critical Alert:** SLO Error Budget consumed **70.18%** of 7-day target, triggering a P2 Warn status (`Event ID: 8561671325753487283`).
    *   "Post Cart" and "Cart Update" P99 both spiked to ~**4.0s–4.1s** (threshold 2.6s).

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** The incident is now a **multi-vector availability degradation with active SLO burn**. Data confirms sustained success rate failures (<99.9%) alternating with extreme tail latencies (>8s P99) across write (Cart/Wish List) and read paths.
*   **Immediate Action Required:** Address the P2 Error Budget Alert (`Event ID: 8561671325753487283`) immediately to prevent SLA breach resolution timeout. Correlate recent latency spikes with Event IDs `8561612743642084453`, `8561669672158835357`, and `8561675516265438726`.

### Decisions Made
*   **Priority Escalation:** Status remains **"Critical Incident"** with added urgency due to the P2 Error Budget alert. Activity extends from March 20 through at least March 27, 02:28 UTC. No stabilization observed; failure modes have diversified to include SLO budget consumption.
*   **Focus Shift:** Prioritize analysis of Event IDs `8561612743642084453` (Cart Success Rate) and the cluster of latency events starting at 02:22 UTC (`8561669672158835357`, `8561674171692352711`) to identify the common root cause causing the error budget burn.

### Key Dates & Follow-ups
*   **Critical Window:** Extended activity from March 20 through at least March 27, 02:28 UTC.
*   **Follow-up:** Immediate correlation of trace data for the 01:25–02:28 UTC window to resolve the SLO budget burn before completing the shift.

### References
*   **Active Monitors:** `22710472` (Cart Success Rate), `21245701/21245706` (Wish List Latency), `21245720/21245725` (Wish List Get Latency), `22710473/21245713` (Cart Update Latency).
*   **Service Tags:** `service:frontend-gateway`, `service:st-cart-prod`, `team:dpd-pricing`.


## [5/85] FPG Everyone - General
Source: gchat | Group: space/AAAAjDYVcBU | Messages: 6 | Last Activity: 2026-03-27T02:26:28.408000+00:00 | Last Updated: 2026-03-27T02:40:46.300145+00:00
**Daily Work Briefing: FPG Everyone Chat Summary (Updated)**
**Date Range:** March 3 – March 27, 2026
**Source:** Google Chat (FPG Everyone - General)

### Key Participants & Roles
*   **Maisy Heeng:** Marketing/Product Announcement Lead.
*   **Mary Pereira:** Mediacorp Microdrama Collaboration Lead.
*   **Jolene Lim:** Own Brands Team (FairPrice Foaming Hand Soap).
*   **Eva Wang, Siew Mei Chu, Ng Zhuang Shu:** OB Sensory Team.
*   **Zhaoyue Touw & Ariel Yap:** Unity/Wellness Campaign Lead.
*   **Cheryl Tan:** NTUC Women and Family Event Coordinator.
*   **Kara Pua & Chloe Ong:** Loyalty/Rewards Coordination.
*   **Pauline Tan:** FPG ADvantage LinkedIn Page Launch Lead.
*   **Vincent Phua:** Digital & Technology Announcement (Cardless Access).
*   **Jenna Poh:** Day of Service Coordinator.
*   **Siti Nabilah:** Day of Service Campaign Promoter.
*   **Si Min Ng:** Award Campaign Coordinator.

### Main Topics
1.  **Digital Access Rollout:** Schedule confirmed and executed (C-suite/HR/Finance on Mar 16; Customer/Marketing/E-Commerce on Mar 23; Remaining Hub staff by Mar 30). User guide distributed.
2.  **Media Collaboration – "Bowl of Love":** Final episodes featuring Tyler Ten, Tasha Low, and Xiang Yun are officially live following the March 21 launch. The story focuses on warmth and healing with fresh Malaysian pork.
    *   **Platform:** @mediacorp.re.dian TikTok (`https://vt.tiktok.com/ZSusN9b4n/`).
3.  **Unity Wellness Promotions:**
    *   **World Oral Health Day:** Offers extended through March 25 (Listerine, Colgate, Oral-B).
    *   **New B1G1 Promotion (Mar 26–29):** Zhaoyue Touw announced a 4-day "Buy 1 Get 1 FREE" on selected health and wellness essentials at Unity stores.
        *   **Link:** `https://go.fpg.sg/Unity-MarB1G1`
    *   **Wellness Picks:** Ariel Yap highlighted specific products including Moom Health Happy Hormones, Elastine Perfume De Shampoo/Conditioner, New Moon Bird's Nest Gift Set, and Greenlife Derma Youth Softgels.
        *   **Catalogue Link:** `https://go.fpg.sg/HABAFPG_WK4`
4.  **Loyalty Promo (Chloe Ong):** A new redemption offer launched on March 27 with a price point of **$0.99** to reduce barriers for trial.
    *   **Link:** `https://go.link.sg/wexvmf`

### Pending Actions & Ownership
*   **Shorty Awards Voting (Owner: All Staff):** FPG has two campaigns shortlisted for the 18th Annual Shorty Awards under "Audience Honor."
    *   **Campaigns:** "Bridge to Equity" (Integrated) and "2025 End-Of-Year Unpacked" (Local).
    *   **Action:** Create a personal email account, vote daily from today until **April 8**, casting one vote per category per day.
    *   **Links:** `https://shortyawards.com/vote/` and specific campaign links provided by Si Min Ng.
*   **Day of Service Registration (Owner: All Staff):** Final call issued by Siti Nabilah for the "Willing Hearts Kitchen Crew" on **March 27, 2026 (Friday)**, 1:00 PM – 5:00 PM at Joo Chiat Place.
    *   **Status:** Event is currently underway; spots appear fully booked or closed as of late March 27 morning.
*   **Sensory Test Sign-ups (Owner: All Staff):** Chapati screening form remains open (`https://forms.gle/DFYrahZcvhtcoJ9R7`). Frozen Snacks sign-up is closed.
*   **New Redemption Action:** Staff encouraged to redeem the $0.99 offer via the link provided by Chloe Ong immediately.

### Decisions Made
*   **Awards Campaign:** Strategic decision to mobilize staff for the Shorty Awards "Audience Honor" category, emphasizing personal email usage and daily voting until April 8.
*   **Wellness Extension:** Unity promotions extended with a new B1G1 offer (Mar 26–29) following the World Oral Health Day campaign.
*   **Service Event:** Final recruitment for March 27 service event confirmed; event date has passed/is ongoing.
*   **New Loyalty Initiative:** Decision to launch a low-barrier ($0.99) redemption offer to drive trial and customer engagement.

### Critical Dates & Deadlines
*   **March 25:** World Oral Health Day offers expired.
*   **March 26–29:** Unity B1G1 Promotion on health/wellness essentials.
*   **March 27 (Friday):** Day of Service at Willing Hearts Kitchen (Event Date).
*   **April 8:** Shorty Awards voting deadline.


## [6/85] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Messages: 50 | Last Activity: 2026-03-27T02:24:25.968000+00:00 | Last Updated: 2026-03-27T02:41:17.260930+00:00
**Daily Work Briefing: Nikhil Grover & Michael Bui**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator; confirmed ranking fix, managing deployment requests. Investigated prod visibility in "Omni Home" and verified `pcnt` parameters for Search/Category pages to prevent regression.
*   **Michael Bui:** Technical Lead (Engineering); deployed to PRD. Confirmed `pageType: OMNI_HOMEPAGE` in logs but noted no changes were made to include `swimlane` or `page_name` parameters yet. Verified no changes to `pcnt` for Search/Category pages.
*   **Flora:** Frontend resource; previously raised analytics payload concerns. Confirmed backend control for swim lanes historically resided with Yang Yu.

**Main Topics**
1.  **Post-Deployment Visibility & Parameter Gaps (Omni Home):**
    *   While the core ranking fix was deployed to PRD on March 25, visibility issues persist in "Omni Home." Nikhil observed only one ad in vertical scroll; Michael confirmed he has never seen ads there.
    *   **Log Analysis:** Michael verified logs for Customer UID `163692623655477837` show `pageType: OMNI_HOMEPAGE`. However, Nikhil noted the absence of the `page_name` parameter in the Osmos request and that the `swimlane name` was not included.
    *   **Code Status:** Michael confirmed no changes were made to include swim lane names or the `page_name` param yet.
    *   **Action:** Nikhil provided a sample Osmos URL (referencing Daryl's DPD-814 comment) for investigation; focus shifted to ensuring backend requests include both `swimlane` and `page_name`.

2.  **Resource Constraints & Timeline Conflict:**
    *   **Impressions Delivery:** Nikhil requested starting tickets on March 26, but Michael declined due to travel preparations and a strict leave block starting April 6th.
    *   **Project Light Conflict:** The week of April 6th is "unprecedentedly tight" for Project Light. Michael estimates focusing until April 12th (UAT April 13–14, deploy April 15).
    *   **Timeline Clash:** Nikhil requires deployment by **April 9th**. He flagged that waiting until mid-April is not feasible as he can only manage a 1–2 day delay.

3.  **Regression Prevention (Search & Category Pages):**
    *   On March 27, Nikhil requested verification that `pcnt` settings for Search and Category pages remained at **6** following the Homepage changes.
    *   Michael confirmed he did not alter `pcnt` for these pages on his end and that Osmos receives parameters directly from their side, ensuring no side effects from homepage adjustments. Nikhil insisted on explicit confirmation to avoid potential incidents regarding regression.

**Decisions Made & Status Updates**
*   **Deployment Readiness:** PRD deployment is confirmed, but ads remain invisible in "Omni Home" pending backend parameter updates (`swimlane`, `page_name`) and swim lane activation.
*   **Regression Safety:** Confirmed on March 27 that `pcnt` for Search and Category pages remains at **6** with no side effects from the homepage deployment.
*   **Capacity Planning:** Michael Bui cannot start impressions tickets immediately due to Project Light constraints (April 6–12). A delivery window before April 9th is currently at risk.

**Pending Actions & Owners**
*   **Parameter Implementation (Michael Bui):** Investigate why `page_name` is missing and implement changes to pass both `swimlane` and `page_name` to Osmos.
*   **Swim Lane Activation (Nikhil Grover/Team):** Continue coordinating with Yang Yu or third parties to enable remaining swim lanes in PRD for Omni Home.
*   **Impressions Delivery Scheduling (Nikhil Grover/Michael Bui):** Urgent negotiation required to find a delivery window before April 9th, despite Michael's unavailability until mid-April.

**Key Dates & Deadlines**
*   **March 26, 2026:** Verification of Omni Home ads; discovery of missing `page_name` and swim lane params in Osmos requests (UID: `163692623655477837`).
*   **March 27, 2026:** Confirmation that Search/Category `pcnt` remains at 6; verification of no regression from homepage changes.
*   **April 9, 2026:** Critical deadline for delivery raised by Nikhil Grover.
*   **April 6–12, 2026:** Michael Bui's anticipated leave/travel and Project Light focus period.

**Historical Context Note**
While the initial focus was on resolving the March 25 ranking anomaly (confirmed fixed), the conversation pivoted to immediate post-deployment validation in "Omni Home." Despite successful PRD deployment, ads remain invisible due to missing backend parameters (`page_name`, `swimlane`) and potential swim lane configuration issues. Simultaneously, a critical resource conflict emerged: Nikhil requires delivery by April 9th, but Michael is unavailable due to Project Light and travel until at least mid-April, creating a significant scheduling risk for upcoming impressions delivery tickets. On March 27, both parties confirmed the stability of Search/Category `pcnt` settings (6) following the homepage update.


## [7/85] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 16 | Last Activity: 2026-03-27T02:18:33.550000+00:00 | Last Updated: 2026-03-27T02:41:56.286899+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (Updated March 27, 02:18 UTC)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
Instability persists into the early morning of **March 27**, characterized by recurring oscillating error rates in `engage-my-persona-api-go` and intermittent latency spikes. The issue has expanded to include failures in `ef-android`, degraded success rates for `orchid` requests, and latency issues in `lyt-p13n-layout`, indicating a widening backend impact across core APIs and mobile clients.

**Status Summary & Timeline (Early Morning Volatility)**
*   **Service Error Rates (`engage-my-persona-api-go`):**
    *   Recurring high error alarms (>0.1%) triggered at **01:23 UTC** (Peak: 0.101%), **01:38 UTC** (Peak: 0.111%). Recoveries observed intermittently between triggers.
    *   Status remains active as of the latest log.
*   **Latency Spikes (`lyt-p13n-layout`):**
    *   `get_/v1/scan-door/store`: P99 Latency (>1.8s) triggered repeatedly at **01:58 UTC** (Peak: 2.009s), recovered, then re-triggered at **02:11 UTC** (Peak: 2.009s). Recovered by **02:13 UTC**.
*   **New Service Degradation:**
    *   `ef-android` (Compass): Success rate dropped to 99.156% at **02:17 UTC**, recovering by **02:18 UTC**.
    *   `frontend-gateway` (Journey): `orchid` request success rate dropped to 99.778% at **01:24 UTC** (Recovered @ 01:34 UTC).
    *   `engage-my-persona-api-go`: `get_/user/profile/myinfo` success rate dropped to 99.881% at **01:40 UTC** (Recovered @ 01:50 UTC).

**Pending Actions & Ownership**
*   **Investigate Recurring Error Loops:** Immediate RCA required for the oscillating error rates in `engage-my-persona-api-go` continuing into March 27 early morning (01:23–02:18 UTC). Owner: **Squad Dynamics**.
*   **Analyze Cross-Service Correlation:** Investigate the newly triggered failures in `ef-android`, `orchid`, and `scan-door/store` alongside persona API errors. Owner: **Squads Compass, Journey, Dynamics**.
*   **Monitor Latency & Success Rates:** Continue monitoring `get_/v1/scan-door/store` P99 latency and `orchid` success rates following recent triggers. Owner: **Squad Journey**.

**Decisions Made**
*   **Severity Maintenance:** Incident severity remains high due to continuous re-emergence of instability across March 26 afternoon and March 27 early morning windows, now explicitly affecting mobile clients (`ef-android`) and new frontend services.
*   **Pattern Continuity:** Activity confirms a persistent issue affecting `engage-my-persona-api-go` error rates, expanding to downstream impacts on feed loading, user profile success rates, and Android view linkpoints.

**Key Dates & Follow-ups**
*   **Active Window:** March 24–27 (UTC). Recent critical activity: **01:23 – 02:18 UTC** (March 27).
*   **Reference Links (Updated):**
    *   `engage-my-persona-api-go` Error Monitor #92965074 (Peak: 0.111% @ 01:38)
    *   `get_/v1/scan-door/store` P99 Latency Monitor #20382854 (Peak: 2.009s @ 01:58 & 02:11)
    *   `orchid` Success Rate Monitor #17448311 (Value: 99.778% @ 01:24)
    *   `get_/user/profile/myinfo` Success Rate Monitor #50879029 (Value: 99.881% @ 01:40)
    *   `ef-android` Linkpoints Monitor #63109467 (Value: 99.156% @ 02:17)


## [8/85] [Prod Support] Ecom FFS Ops
Source: gchat | Group: space/AAAAde_cYKA | Messages: 9 | Last Activity: 2026-03-27T02:14:08.393000+00:00 | Last Updated: 2026-03-27T02:42:24.028540+00:00
**Daily Work Briefing: [Prod Support] Ecom FFS Ops (Updated Mar 27)**

**Key Participants & Roles**
*   **Wai Ching Chan / Sampada Shukla:** Operations/Product Leads.
*   **TL HCBP FFS, TL - HGPT FFS, TLEPT FFS, Harry Akbar Ali Munir:** Store/Regional Team Leads reporting blockers.
*   **Adrian Yap Chye Soon:** Technical Lead/Support (investigating data anomalies).
*   **Akash Gupta:** DPD / Fulfilment / On Call (Source of new alerts and escalation point).
*   **Yoongyoong Tan:** Reporting specific HCBP picking Q issues.

**Main Topics**
1.  **Packlist Discrepancies & Validation:** Ongoing investigation into critical `packed_qty` anomalies (NULL values or massive mismatches vs. `delivered_qty`).
    *   **New Critical Incident (Mar 26):** Akash Gupta identified two orders at **VivoCity (Store ID 170)** showing `packed_qty` > 13M against `delivered_qty` of <20.
        *   Order #22912255: `packed_qty` 13,165,999 vs. `delivered_qty` 12.
        *   Order #22906879: `packed_qty` 13,165,999 vs. `delivered_qty` 18.
    *   **Historical Context:** Previous incidents remain active reference points, including the Mar 25 Sun Plaza alert (Order #22898981) and Mar 23–24 anomalies at Hyper Sports Hub and VivoCity.
2.  **HCBP Picking Queue Issues (Mar 27):** A new blockage reported regarding "No picking Q" for HCBP.
    *   **Timeline:** Reported by TL HCBP FFS on Mar 27, 02:08 AM; followed by a specific request from Yoongyoong Tan at 02:14 AM to check the HCBP picking queue status.

**Pending Actions & Ownership**
*   **Critical Data Validation (Mar 26):**
    *   *@Yap Chye Soon Adrian:* Immediately confirm massive `packed_qty` mismatches for Order #22912255 and #22906879 at VivoCity as requested by Akash Gupta.
    *   *@Akash Gupta:* Continue monitoring DPD/Fulfilment alerts. Note that Sun Plaza (Mar 25) validation remains pending alongside new VivoCity findings.
*   **HCBP Queue Investigation (New - Mar 27):**
    *   *@Adrian Yap Chye Soon / On Call Team:* Investigate the "No picking Q" status for HCBP reported by TL HCBP FFS and Yoongyoong Tan on Mar 27.
    *   *Status Update:* The previously resolved Mar 25 HCBP "no order in picking q" incident is no longer active; however, a new instance has emerged requiring immediate attention.

**Decisions Made**
*   **App Release Strategy:** Picker App 10.4.0 rollout remains on hold pending resolution of critical data anomalies (Mar 18–27). Full rollout is contingent on stability post-fixes, specifically addressing the Mar 26 VivoCity alerts and the new Mar 27 HCBP queue issues.

**Key Dates & Deadlines**
*   **Immediate:** Validation of Mar 26 Orders #22912255 and #22906879 (VivoCity); Investigation of Mar 27 HCBP Picking Q status.
*   **Pending:** Root cause analysis for all recent `packed_qty` anomalies across Sports Hub, VivoCity, Parkway, Changi, Sun Plaza, Hyper VivoCity, and the new HCBP queue failures.

**Critical Alerts**
*   **Active Alert (Mar 27):** "No picking Q" issue at HCBP reported by TL HCBP FFS and Yoongyoong Tan; requires immediate technical check.
*   **New Alert (Mar 26):** Two orders at VivoCity (Store ID 170) showing `packed_qty` (~13M) >> `delivered_qty`. Orders #22912255 and #22906879 require immediate technical confirmation.
*   **Resolved Alert (Mar 25, 03:45–04:13 AM):** Previous HCBP "no order in picking q" issue resolved after On Call intervention (superseded by Mar 27 report).
*   **Previous Critical Alerts:** Mar 25 Sun Plaza massive mismatch; Mar 23 NULL quantity (Sports Hub) and massive mismatch (VivoCity/Sports Hub); Mar 24 massive mismatch (Sports Hub).


## [9/85] @omni-ops #standup - Mar 27
Source: gchat | Group: space/AAQAz751zBQ | Messages: 1 | Last Activity: 2026-03-27T02:02:10.051000+00:00 | Last Updated: 2026-03-27T02:42:34.236887+00:00
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


## [10/85] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/rKtZEQsyOFI | Messages: 10 | Last Activity: 2026-03-27T01:58:46.079000+00:00 | Last Updated: 2026-03-27T02:42:47.198032+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Michael Bui:** Lead developer/technical contact; drafting API specifications.
*   **Alvin Choo:** Decision maker (likely Technical Lead or Manager); defining scope and process.
*   **Gopalakrishna Dhulipati:** Tagged participant (no direct action in this thread).

**Main Topic**
Coordination with the CoMall team regarding the "Project Light Attack and Defence" kick-off, specifically focusing on contract status, engagement timing, and standardizing Technical API Specifications (Tech Spec) for RMN pieces.

**Decisions Made**
1.  **Engagement Timing:** Do not connect with the CoMall team or create a Google Chat space immediately; wait until the official kick-off/grooming next week as they are not yet awarded.
2.  **Documentation Platform:** Use Confluence for the API specification template (preferred over GDoc).
3.  **Template Approach:** Create an initial draft immediately to ensure all teams (Payments, FP Pay, Identity) follow a consistent format; perfection is not required at this stage.

**Pending Actions & Ownership**
*   **Draft API Spec Template:** Michael Bui must create a draft version of the RMN piece of API spec template today.
    *   *Note:* This follows his immediate priority to handle "BCRS redelivery" changes first.
*   **Review & Finalize:** Alvin Choo and the team will review the draft later today to align on the format.

**Key Dates & Deadlines**
*   **Today (March 27, 2026):** Michael Bui to send the Confluence draft template version.
*   **Next Week:** Scheduled kick-off/grooming session with CoMall.
*   **Upcoming:** Michael Bui is on leave soon; action item prioritized before departure.

**Specific References**
*   Contract status: Unconfirmed/Awaited award.
*   Services involved: Payments, FP Pay, Identity.
*   Document format: Confluence draft (exportable to PDF if CoMall lacks access).


## [11/85] [BCRS]-SAP to POS & DBP Interface Deployment
Source: gchat | Group: space/AAQAeMC3qBk/3a5kvSWZa-g | Messages: 63 | Last Activity: 2026-03-27T01:46:35.052000+00:00 | Last Updated: 2026-03-27T02:43:08.464635+00:00
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


## [12/85] DPD All Leads
Source: gchat | Group: space/AAAAQezbuRE | Messages: 1 | Last Activity: 2026-03-27T01:43:42.350000+00:00 | Last Updated: 2026-03-27T02:43:31.929104+00:00
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


## [13/85] RMN Incidents
Source: gchat | Group: space/AAQAz11ATzY | Messages: 4 | Last Activity: 2026-03-27T01:12:12.669000+00:00 | Last Updated: 2026-03-27T02:44:24.079587+00:00
**Daily Work Briefing: RMN Incidents (Updated)**

**Key Participants & Roles**
*   **Nikhil Grover:** Issue initiator; challenged the correlation between paused campaigns and SKU reduction, citing active advertisers in key categories. Demanded immediate resolution.
*   **Rachit Sachdeva:** Investigator; previously provided data on 24 paused advertisers generating $11.5k revenue (Mar 1–17). Currently tasked with reviewing root cause of single-SKU returns despite active inventory.
*   **Stakeholders (CC'd):** Shubhangi Agrawal, Michael Bui, Allen Umali, Rajiv Kumar Singh, Ravi Goel.

**Main Topic**
Critical investigation into a 50% drop in product ad impressions and $11k revenue loss since March 17th. While Rachit identified 24 paused advertisers as a potential cause, Nikhil has refuted this as the primary driver for single-SKU responses, noting that multiple active campaigns (e.g., Ferrero, DKSH-Mars, Mondelez in "chocolate"; Colgate, Haleon in "toothpaste") are still yielding only one product per response.

**Critical Findings & Data**
*   **Observation:** Product ad impressions dropped 50% starting March 17th; search and category pages primarily affected.
*   **Revenue Impact:** $11k decrease compared to the previous 9-day period.
*   **Supply-Side Context (Rachit):** 24 advertisers stopped campaigns after March 17th, accounting for S$11.5k revenue (Mar 1–17).
*   **Rebuttal on SKU Count (Nikhil):** Despite the paused cohort, sufficient campaigns remain active to support multi-SKU responses (typically 4–5 SKUs).
    *   **Example "Chocolate":** Active campaigns from Ferrero, DKSH - Mars Wrigley, and Mondelez still result in a single response.
    *   **Example "Toothpaste":** Active campaigns from Colgate and Haleon result in only one product.

**Decisions Made**
*   The hypothesis that paused campaigns are the sole cause of SKU reduction has been challenged. The issue is now identified as a technical or logic failure where single-SKU responses persist despite multiple active advertisers being available.
*   **Priority Status:** Elevated to immediate resolution; Nikhil requested the issue be resolved within the day (March 27th).

**Pending Actions & Ownership**
*   **Action:** Investigate why single responses are generated when multiple campaigns from top advertisers (e.g., Ferrero, Colgate) are active.
    *   **Owner:** Rachit Sachdeva and Engineering Team (implied by "review this on priority").
*   **Action:** Validate the logic governing SKU selection per response across all categories to ensure it aligns with available active campaigns.
    *   **Owner:** Team (specifically requested confirmation from Shubhangi Agrawal and Rachit Sachdeva).

**Key Dates & Deadlines**
*   **Incident Start Date:** March 17th (campaign pauses observed; impact noted).
*   **Latest Update:** March 26th, 2026 at 09:40–10:22 UTC (initial data sharing); March 27th, 01:12 UTC (Nikhil's rebuttal and urgency escalation).
*   **Data Window:** Past 7 days for SKU trends; Mar 1–17 for revenue baseline.
*   **Deadline:** Resolution required by end of day on March 27th due to significant business impact.

**Attachments Referenced**
*   `FPG _ Paused Advertisers (1).xlsx` (Shared by Rachit on Mar 26; acknowledged and reviewed by Nikhil on Mar 27).


## [14/85] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Messages: 16 | Last Activity: 2026-03-27T01:04:09.560000+00:00 | Last Updated: 2026-03-27T02:51:46.689917+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Mar 27, 01:15 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-discovery`, `@opsgenie-dpd-grocery-retail-media`.
*   **Escalations:** `@hangouts-GT-Search-DatadogAlerts`, `@oncall-dpd-staff-excellence-pdm`, `@hangouts-GT-Discovery-DatadogAlerts`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Search Indexing.

**Main Topic**
**P3 ALERT (Flapping):** The `go-catalogue-service` exhibits recurring latency instability in production. Following a stable period on Mar 25, the `get_/category/_id` endpoint flapped on **Mar 26**. Additionally, the `marketing-service` experienced throughput anomalies late evening March 26/early March 27, and the `sku-store-attribute` job showed low file processing counts.

**Pending Actions & Ownership**
*   **Action:** **MONITOR LATENCY FLAPPING (`go-catalogue-service`):** Address P90 latency spikes > 2000ms for `get_/category/_id`.
    *   **Owner:** Discovery Team (`@hangouts-GT-Discovery-DatadogAlerts`) & Product Data Management (`@opsgenie-dpd-staff-excellence-pdm`).
    *   **Status:** **RECOVERED (07:13 UTC Mar 26).** The alert cycled states on Mar 26 between 04:31 and 04:32 UTC, with p90 spiking to 3.027s before dropping to 0.575s.
    *   **Required Checks:** Review Datadog logs, inspect K8s deployment (`fpon-cluster/default/go-catalogue-service`), and consult Runbook.
*   **Action:** **RESOLVE LOW FILE PROCESSING (`sku-store-attribute`):** Address job processing < 6 files in the last 4 hours.
    *   **Owner:** Discovery Team (`@opsgenie-dpd-grocery-discovery`).
    *   **Status:** **RECOVERED (01:04 UTC Mar 27).** Triggered at 22:04 UTC on Mar 26; resolved when file count reached ≥6. Monitor ID: `20382848`.
*   **Action:** **INVESTIGATE THROUGHPUT ANOMALY (`marketing-service`):** Address abnormal throughput (P4) where hits deviated >3x from predicted values.
    *   **Owner:** Retail Media Team (`@opsgenie-dpd-grocery-retail-media`).
    *   **Status:** **RECOVERED (00:52 UTC Mar 27).** Triggered at 23:53 UTC on Mar 26; recovered at 00:52 UTC. Duration approx. 1 hour. Monitor ID: `17447110`.
*   **Action:** **RESOLVE LATENCY FLAPPING (`get_/product`):** Address P90 latency spikes > 150ms for `get_/product`.
    *   **Owner:** Discovery Team & Product Data Management.
    *   **Status:** Previously recovered at 19:27 UTC on Mar 25 (p90: 129ms). Monitor ID: `17447976`. No new activity reported in current cycle.
*   **Action:** **PERSISTENT INVESTIGATION:** Address critical errors on `fp-search-indexer` (env: prod).
    *   **Owner:** Product Data Management On-Call (`@oncall-dpd-staff-excellence-pdm`).
    *   **Status:** Active since Mar 18. Last re-triggered Mar 24, 16:29 UTC. No resolution achieved.

**Decisions Made**
*   The `sku-store-attribute` job experienced a processing delay (triggered <6 files in 5h) late on Mar 26 but normalized by early morning Mar 27.
*   The `marketing-service` anomaly showed 100% anomalous values for the monitoring window before returning to baseline. No root cause analysis required unless recurrence is observed.
*   Root cause analysis remains critical for the recurring `go-catalogue-service` monitor (ID: `17447967`) and the persistent `fp-search-indexer` failure since Mar 18.

**Key Dates & Follow-ups (Mar 16–27, 2026)**
*   **Service: `go-catalogue-service` (P3 - Discovery/Product Data) [FLAPPING]**
    *   *Latest Timeline:* Triggered 04:31 UTC Mar 26 (p90: 3.027s); Recovered 04:32 UTC. Stable after 13:00 UTC on Mar 25.
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/17447967) | [Runbook](https://ntuc.atlassian.net/wiki/spaces/DIS/pages/2646212686/Catalogue+Service).
*   **Service: `sku-store-attribute` (P3 - Grocery Discovery) [RESOLVED]**
    *   *Latest Timeline:* Triggered 22:04 UTC Mar 26; Recovered 01:04 UTC Mar 27. Monitor ID: `20382848`.
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/20382848).
*   **Service: `marketing-service` (P4 - Retail Media) [RESOLVED]**
    *   *Latest Timeline:* Triggered 23:53 UTC Mar 26; Recovered 00:52 UTC Mar 27. Monitor ID: `17447110`.
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/17447110) | [Runbook](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book).
*   **Service: `fp-search-indexer` (P2 - Product Data Management) [ACTIVE CRITICAL]**
    *   *Latest Timeline:* Active since Mar 18; re-triggered Mar 24, 16:29 UTC.

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c


## [15/85] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Messages: 16 | Last Activity: 2026-03-27T00:04:15.761000+00:00 | Last Updated: 2026-03-27T02:53:38.547729+00:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
Production instability persists in Mirakl integration and seller job processing, extending from March 17 through the early hours of **March 27**. Activity on March 26 shifted from early morning clusters to an afternoon cluster involving a new "FairPrice" route. Concurrently, `picklist-pregenerator` latency cycles continue into late March 26.

**Incident Summary & Timeline**
*   **Service: `fni-offer` (Mirakl Integration) – Afternoon Cluster (Mar 26)**
    *   **New Route Failure:** Triggered at **15:14 UTC** on Mar 26 with "Exception Occurred at FairPrice Route" (Monitor ID `17447935`). Recovered by **15:19 UTC**. Duration: ~5 minutes.
    *   **Pattern Continuation:** Instability spans March 17–26, including late-night clusters on Mar 25/26.

*   **Service: `fni-order-create` (Mirakl Integration) – Afternoon Cluster (Mar 26)**
    *   **Incident Window (~16:55 UTC):** Simultaneous P2 triggers for "Exception Occurred At Mirakl Route" and "Error occurred in FairNex".
        *   Triggered at **16:55:39 UTC** (Monitor ID `17447918`) and **16:55:56 UTC** (Monitor ID `17447934`).
    *   **Recovery:** Monitors returned to normal by **18:09 UTC**. Duration: ~1 hour 14 minutes.

*   **Service: `fpon-seller-mirakl-order-creation-alert` (Sync Issues)**
    *   **Fluctuating Sync Alerts:** P3 alerts for "There are unsynced orders from DBP to Mirakl" triggered at **17:36 UTC** and **18:01 UTC**, recovering at **17:46 UTC** and **18:06 UTC**.

*   **Service: `seller` (`picklist-pregenerator`) – Recurring Latency**
    *   **Latest Update (Mar 26, ~23:01 UTC):** A P2 warning triggered with metric value **3603.203s** (Monitor ID `20383097`), following previous peaks on March 25 (3657.213s) and March 24 (3607.798s).

*   **Service: `fni-offer` – Late Night Cluster (Mar 26/27)**
    *   **Incident Window (~23:58 UTC):** Simultaneous P2 triggers for "Error while calling API" and "Exception Occurred at Mirakl Route".
        *   Triggered at **23:58:40 UTC** (Monitor ID `17447919`) and **23:59:14 UTC** (Monitor ID `17447953`).
    *   **Recovery:** Monitors recovered by **00:03 UTC** and **00:04 UTC** on March 27. Duration: ~5 minutes.

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of expanded Mirakl integration instability affecting `fni-order-create` and `fni-offer`. The pattern now includes recurrence windows on Mar 17–26 history, clusters in the afternoon/evening of Mar 25/26, a new early-morning cluster at **00:12 UTC** on March 26, and a distinct **FairPrice Route** failure at **15:14 UTC**.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Investigate root cause of extreme latency spikes in `picklist-pregenerator`. The cycle peaked at **3657.213s** on March 25 and remained critical at **3603.203s** on March 26 (23:01 UTC).
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Review Monitor `29851723` logic for Apple Pay/Google Pay transactions following the March 23 test alert indicating potential false positives.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Summary for Leadership**
Mirakl integration instability has persisted across ten consecutive days (March 17–27). On March 26, the service exhibited a new failure mode ("FairPrice Route" exception at **15:14 UTC**) and a significant afternoon cluster affecting `fni-order-create` lasting over an hour. Late-night cycles on Mar 26/27 continued the pattern of simultaneous API/Mirakl route errors with ~5-minute durations. Concurrently, `picklist-pregenerator` shows a continuous cycle of critical latency spikes, reaching **3603.203s** on March 26 (23:01 UTC). These systemic failures in Mirakl and job processing logic require urgent engineering review to stabilize production performance.


## [16/85] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Messages: 2 | Last Activity: 2026-03-27T00:03:14.835000+00:00 | Last Updated: 2026-03-27T02:55:17.287407+00:00
**Daily Work Briefing Summary (Updated: March 27, 2026)**

**Main Topics & Discussions**
1.  **Programmatic Advertising (Advertima/TTD):** Focus remains on validating discrepancies for `advertima_ttd-fixed-price-test-1.5`. Ravi Singh confirmed receipt of raw BURLs; validation was targeted for Monday, March 17th. Yian Koh requested confirmation on deals `advertima_ttd-first-price-test` and `advertima_ttd-fixed-price-test-1`.
2.  **New Deal Setup:** Yasmina Tregan (Advertima) required an end-to-end test setup this week. Wei Phung to share live campaign details; Ravi Singh to execute setup, push to TradeDesk, and map segments before launch.
3.  **BCRS UAT & Finance Integration:** Progress on SAP document numbers, duplicate posting fixes via PubSub "exactly once" policy (PR #1033), and Bukit Timah Plaza pricing/display issues.
4.  **Event Sync Optimization (DPD-645):** Addressing the massive event overage (14M vs. normal 550k). PRD deployment plan set for Sunday, March 15.
5.  **Security & Compliance:** RMN Pentest fixes (DPD-700) deployed to Prod; Bitbucket App Passwords deprecated effective June 9, 2026.

**Status Update: Inbox & Communications**
*   **Inbox Status:** As of March 27, 2026, the workspace inbox is fully caught up across all categories (**Urgent Action Items**, **Thematic Project Updates**, **Meeting Updates**, and **FYI**). No pending unread items require immediate attention. This status follows confirmations from daily summaries dated March 24, 25, 26, and now March 27, 2026.

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

**Note on New Content:** Daily summaries received on March 27, 2026, confirm the inbox remains clear of urgent action items across all categories. No changes to pending actions or decisions were required based on this update.


## [17/85] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY | Messages: 7 | Last Activity: 2026-03-26T22:11:31.300000+00:00 | Last Updated: 2026-03-27T02:56:48.887602+00:00
**Updated Briefing: BCRS Firefighting Group**
**Date:** March 26, 2026 (Latest activity: ~10:04 PM)
**Source:** Google Chat Space & Shared UAT Tracker (78 messages total)

### **Key Participants & Roles**
*   **Prajney Sribhashyam:** Project Lead/Test Coordinator.
*   **Dany Jacob:** Finance/Data/Invoice specialist (Refund logic).
*   **Sathya Murthy Karthik:** QA Lead.
*   **Michael Bui / De Wei Tey:** Finance/SAP & Deposit specialists.
*   **Wai Ching Chan / Akash Gupta:** Technical Integration (API/Metadata).
*   **Daryl Ng / Zaw Myo Htet:** Production deployment & Payment specialists.
*   **Eswarlal Rajesh / Sneha Parab:** Active test participants.

### **Main Topics**
1.  **BCRS Refund Logic Enhancement (High Priority):** Dany Jacob requested expertise on BCRS item refunds for "Scan n Go" and pre-orders. The API `GET .../order/75583137/returns` must be enhanced to include container deposit information.
2.  **E2E Production Testing Initiative:** Prajney Sribhashyam initiated a request for immediate End-to-End (E2E) production testing today, focusing on: (1) App Experience, (2) Order placement, and (3) Order posting. This discussion has generated significant engagement (12 replies) with active participation from Eswarlal Rajesh, Daryl Ng, and Sneha Parab.
3.  **Deposit API & Metadata Implementation:** Technical tasks for Re-delivery use case (Jira DPD-807) remain critical: Order service to maintain 'Deposit posted to SAP' in metadata; Sales posting to consume this field to suppress duplicates; RPA to charge/post deposit sales.
4.  **Production Deployment Planning:** Focus remains on resolving critical refund logic errors and executing production tests before Michael Bui's final deployment day on March 26.

### **Decisions & Updates**
*   **Test Mobilization:** A new directive has been issued to execute E2E production testing today covering the full order lifecycle (App -> Order Place -> Order Posting).
*   **API Enhancement Scope:** Consensus remains to modify the Order Service API to include container deposit details for refunds, with rough estimates requested from Akash Gupta and Wai Ching Chan.
*   **Timeline Shift:** The schedule is now driven by immediate execution of refund logic fixes and production validation before Michael Bui's departure on March 26.

### **Pending Actions & Owners**
| Action Item | Owner(s) | Status/Context |
| :--- | :--- | :--- |
| **E2E Production Test Execution** | Prajney Sribhashyam / Eswarlal Rajesh / Daryl Ng / Sneha Parab | **Active (Today):** Conduct App Experience, Order Place, and Order Posting tests. Last reply: 4 mins ago. |
| **API Deposit Data Enhancement** | Akash Gupta / Wai Ching Chan | **Urgent:** Provide rough estimate for adding container deposit info to `order/returns` API endpoint. |
| **Re-delivery Grooming Session** | Michael Bui / Wai Ching Chan / De Wei Tey | **Immediate:** Schedule "quick grooming" (DPD-807) to define metadata, sales posting, and RPA charge workflows. |
| **Urgent Refund Coordination** | Prajney Sribhashyam / Dany Jacob / Daryl Ng | **Active:** Previously joined Google Meet (bgg-fuft-uzq) to accelerate SnG refund logic. |

### **Key Dates & Deadlines**
*   **March 26 (Today):** Target to finalize API estimates, execute urgent callouts for refund logic, and complete E2E production testing before Michael Bui's final deployment day.
*   **March 26:** Last day for Michael Bui to deploy to Production; departure begins next week.

### **Historical Context Retained**
*   Existing e-comm test accounts deemed unusable for Pre-order staff app; new BCRS CF items and specific GWP SKUs required.
*   Original deadline for SAP Deposit API development was Feb 20 (missed/risk noted).
*   Re-delivery flow testing ongoing with audio issues reported on March 16 awaiting resolution.
*   Deposit SKU linking investigation ongoing due to failure to link post-publishing.


## [18/85] [BCRS]-ECOM Flow Deployment - Mar 27
Source: gchat | Group: space/AAQAPK5pWxQ | Messages: 2 | Last Activity: 2026-03-26T16:11:02.982000+00:00 | Last Updated: 2026-03-27T02:57:53.151637+00:00
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


## [19/85] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4 | Messages: 6 | Last Activity: 2026-03-26T14:39:28.616000+00:00 | Last Updated: 2026-03-27T02:59:01.520039+00:00
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


## [20/85] GE Connect
Source: gchat | Group: space/AAQASkvSlwo | Messages: 2 | Last Activity: 2026-03-26T14:32:33.384000+00:00 | Last Updated: 2026-03-27T03:00:23.936000+00:00
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


## [21/85] [BCRS]-SAP to POS & DBP Interface Deployment
Source: gchat | Group: space/AAQAeMC3qBk | Last Activity: 2026-03-26T14:20:19.441000+00:00 | Last Updated: 2026-03-26T14:36:23.796880+00:00
**Daily Work Briefing: [BCRS]-SAP to POS & DBP Interface Deployment**

**Key Participants & Roles**
*   **Onkar Bamane:** Deployment Lead/Coordinator.
*   **Michael Bui:** Deployer (Production OData/SAP).
*   **Hendry Tionardi:** Technical Advisor.
*   **Prajney Sribhashyam:** Process Owner/Test Coordinator.
*   **Daryl Ng:** Technical Advisor/Approver.
*   **Others:** Sneha Parab, Wai Ching Chan, Olivia, Kandasamy Magesh (Deployed team members).

**Main Topic**
Coordination and execution of the ECOM flow deployment ([BCRS]-SAP to POS & DBP Interface). The primary focus has shifted from pre-deployment planning to post-execution validation following a successful production deployment by Michael Bui.

**Decisions Made & Status Update**
1.  **Deployment Execution:** Confirmed that **DBP deployment proceeded first**, followed by SAP OData, as originally planned.
2.  **Status Change:** **Michael Bui successfully deployed to Production (PRD)** on March 26, 2026.
    *   *Notification:* Deployment confirmed via chat with CC: Onkar Bamane, Hendry Tionardi, Daryl Ng, and Prajney Sribhashyam.
3.  **Risk Mitigation:** The initial validation that deploying DBP first posed no risk regarding BCRS deposit error logs remains valid.

**Pending Actions & Ownership**
*   **Update Deployment Steps:** Team members must continue adding specific deployment steps to the shared spreadsheet. *(Owner: Michael Bui, Sneha Parab)*
    *   *Specific Note:* Sneha Parab is requested to update steps specifically regarding **MP Article creation**.
*   **Add Missing PICs:** Identify and add any missing Persons In Charge (PICs) not currently listed in the coordination group. *(Owner: Sneha Parab, Prajney Sribhashyam)*
*   **Redelivery Status:** Discuss the latest status on "redelivery" separately in the working group meeting; do not discuss in this chat. *(Owner: Prajney Sribhashyam)*
*   **Release Coordination:** The condition for an exceptional release is now moot as the standard deployment was completed successfully by Michael Bui.

**Key Dates & Deadlines**
*   **Deployment Window:** Friday, March 26, 2026 (Completed).
*   **Missed Opportunity Context:** The previous concern regarding Michael Bui's availability for the following Friday and upcoming leave is resolved as his final opportunity was utilized successfully tonight.

**References**
*   **Deployment Plan/Tracker (SAP-DBP Deployment Plan):** https://docs.google.com/spreadsheets/d/1gvCjdXWB2BeWr7XgBQs0-zKeLxGi3OmX4ZrbY6pNMeQ/edit?gid=1022676232#gid=1022676232
*   **Chat Space:** https://chat.google.com/space/AAQAeMC3qBk


## [22/85] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/gZNwhpEiEY4 | Last Activity: 2026-03-26T13:41:16.749000+00:00 | Last Updated: 2026-03-26T14:37:34.007200+00:00
**Daily Work Briefing: Digital Product Development (Leads)**
**Resource:** [Leads] (Ecom/Omni) Digital Product Development
**Date of Discussion:** March 26, 2026

### **Key Participants & Roles**
*   **Daryl Ng:** Project Lead/Manager; coordinating timelines, risk mitigation, and resource allocation.
*   **Michael Bui:** Developer responsible for the BCRS deposit posting job; managing specs, unit tests, and SIT delivery.
*   **Sundy:** Development resource assigned to assist Michael Bui with PRD tasks (arranged by Daryl).
*   **Onkar:** Deployment engineer scheduled to deploy other services at midnight.
*   **Wai Ching:** Created the necessary order custom field during UAT today.
*   **Adrian:** Developer currently restricted from redelivery work between April 1–7 due to duplicate posting risks.

### **Main Topic**
Discussion focused on mitigating delivery risks for the BCRS deposit posting job changes. The team addressed potential delays in SIT (System Integration Testing) and duplicate postings if Adrian continues redeliveries between April 1–7. Michael expressed frustration regarding late UAT sign-offs but confirmed that comprehensive documentation and unit tests are available to facilitate Knowledge Transfer (KT) if needed.

### **Decisions Made**
1.  **Immediate Deployment:** Daryl approved the deployment of all currently ready changes, including the BCRS deposit posting job, scheduled for tonight at 10:00 PM or midnight.
2.  **Resource Allocation:** Sundy has been assigned to assist Michael Bui with specific PRD tasks (creating order custom fields and pipeline deployment).
3.  **Risk Mitigation:** The team agreed to proceed with available changes rather than waiting for a full KT, acknowledging that SIT could potentially be completed tomorrow if progress holds.

### **Pending Actions & Owners**
*   **Deploy BCRS Job:** Michael Bui to execute the Bitbucket pipeline deployment tonight (confirmed by Daryl).
    *   *Context:* Onkar is also deploying at midnight; coordination required to avoid conflicts or ensure sequencing.
*   **Create Order Custom Field:** Sundy to create the field that Wai Ching defined in UAT today.
*   **Pipeline Deployment Assistance:** Sundy to update on PRD pipeline deployment requirements after receiving instructions from Michael Bui.
*   **SIT Status Update:** Michael Bui to provide a status update by tomorrow End of Day (EOD) confirming if SIT is complete or if further actions are required.

### **Key Dates & Deadlines**
*   **March 26, 2026:** Deployment scheduled for tonight (10:00 PM / Midnight).
*   **Tomorrow (EOD):** Deadline for Michael Bui to report SIT completion status.
*   **April 1 – April 7, 2026:** Critical window where Adrian must refrain from redelivery to prevent duplicate postings; SIT is targeted to conclude before this period begins.

**Reference Links:**
*   Specs Repository: https://bitbucket.org/ntuclink/bcrs-deposit-posting/src/main/openspec/specs/


## [23/85] OMS x CS
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


## [24/85] [Internal] (Ecom/Omni) Digital Product Development
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


## [25/85] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Last Activity: 2026-03-26T13:02:01.119000+00:00 | Last Updated: 2026-03-26T14:38:51.682624+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Sneha Parab:** Lead/Manager; coordinating cross-team support, SAP/API integration blockers, tooling requests.
*   **Michael Bui:** Engineering/RMN Architect; managing architecture updates, infrastructure compliance, investigating search performance drops, and assessing SIT timelines.
*   **Alvin Choo:** Leadership; addressing feedback loops, release schedules, AI personalization prioritization, and traffic anomalies.
*   **Daryl Ng:** Investigating store network ownership, Omni Home data discrepancies, and SIT delivery timelines for redelivery changes.
*   **Others Active:** Andin Eswarlal Rajesh, Olivia, Koklin, Zaw, Ravi.

**Main Topics & Updates**
1.  **Critical Search Performance Drop:** Michael Bui flagged a severe decline in impressions (60–70%) on search/category pages since March 18/19. Investigation is ongoing to correlate with PRD deployments.
2.  **SIT Timeline & Redelivery Risk:** Daryl Ng queried the feasibility of SIT delivery before April 6/7 if Knowledge Transfer (KT) occurs. Michael Bui highlighted that between April 1–7, Adrian cannot perform redeliveries due to risks of duplicate postings without a completed handover.
3.  **Store Network Ownership Clarification:** Daryl Ng queried on March 26 regarding "store network" ownership under Data COE vs. Miguel's team. Investigation focus shifted for the `Omni Home` store ID mismatch (OMNI-1157 related).
4.  **SAP/Deposit SKU Integration Blocker:** Marketplace lacks deposit data for SAP API integration. Olivia rejected new technical solutions following poor PM communication regarding manual UD attempts. Immediate action required from the SAP team.
5.  **Requirement Clarity (BCRS):** Michael Bui flagged that "follow existing ones" is unacceptable acceptance criteria for BCRS deposit posting. Explicit UAT scenarios are required for Definition of Ready (DoR).
6.  **Infrastructure Compliance:** Bitnami ending free Docker images impacts `sonic_raptor` and `mkp-fairnex`. Migration is mandatory.
7.  **1HD Changes & Production Testing:** Andin Eswarlal Rajesh confirmed production testing with leadership is targeted for Friday or Monday, though the search drop investigation (and potential release hold) may impact this timeline.

**Pending Actions & Owners**
*   **Search Performance Investigation:** Identify root cause of impression drop since Mar 18/19; correlate with PRD deployments. (Owners: Michael Bui, Daryl Ng, Andin Eswarlal Rajesh, Alvin Choo)
*   **SIT Delivery Assessment:** Determine if KT allows SIT completion before April 6/7 to avoid duplicate posting risks during Adrian's unavailability (Apr 1–7). (Owner: Michael Bui/Daryl Ng)
*   **Store Network Ownership:** Confirm if store network is under Data COE or Miguel's team. (Owner: Daryl Ng/Michael Bui)
*   **SAP Timeline Resolution:** Push SAP team to explore deposit SKU data solutions. (Owner: Sneha Parab/Alvin Choo/Gopalakrishna Dhulipati)
*   **OMNI-1157 Clarification:** Confirm scope applies only to the new app and clarify Data COE ownership. (Owners: Alvin Choo/Gopalakrishna Dhulipati/Daryl Ng)
*   **BCRS Requirements:** Define explicit UAT scenarios with Koklin. (Owner: Alvin Choo/Gopalakrishna Dhulipati)
*   **Infrastructure Migration:** Address Bitnami Docker image end-of-life. (Owner: Engineering Team/Michael Bui)
*   **RAW Forms Review:** Review Risk Register for DPD RAW forms; confirm handovers and renew expired forms. Deadline: Tomorrow EOD. (Owner: All Leads/Sazali Bin Mohammed Ali's team)
*   **Scan@Door AI Prioritization:** Determine prioritization status on Omni board. (Owner: Daryl Ng/Alvin Choo)
*   **1HD Release Verification:** Confirm release status prior to production testing. (Owner: All Leads/Daryl Ng)

**Decisions Made**
*   **RMN Architecture:** Michael Bui updated current, future, and transition architecture diagrams.
*   **Townhall Coordination:** Team to meet Hui Hui post-townhall; no full Q&A scheduled.
*   **Release Status:** Questions remain regarding holding today's regular app release pending the search performance investigation.

**Key Dates & Deadlines**
*   **RAW Forms Review:** Due Tomorrow EOD.
*   **Townhall Meeting:** Today post-townhall session.
*   **Adrian Redelivery Block:** Adrian unavailable for redelivery Apr 1–7 due to duplicate posting risks.
*   **SIT Target:** Potential delivery by April 6/7 contingent on KT success.
*   **Chee Hoe Support:** Effective end of March for Product Catalogue/MarTech scope.
*   **1HD Production Testing:** Targeted for this Friday or Monday.


## [26/85] RMN Incidents
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


## [27/85] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Last Activity: 2026-03-26T10:35:38.422000+00:00 | Last Updated: 2026-03-26T14:39:37.680963+00:00
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
*   **Gopalakrishna Dhulipati & Dang Hung Cuong:** New assignees for address emoji validation.

**Main Topics Discussed**
1.  **iOS Address Emoji Blocking Bug:** Wai Ching Chan reported on Mar 26 that customer addresses containing emojis on iOS devices cause order time slot changes to fail, requiring manual resolution. The issue affects the `customer-support` admin view (Customer ID: 2022036). Validation logic for emoji blocking during address add/edit is required.
2.  **Website SDK Deployment (Strudel):** Lester deployed `go-platform-website` on Mar 19 to update the Strudel SDK for maximum voucher validation. Changes were reviewed via Bitbucket diff between v1.5.11 and v1.5.10.
3.  **Pre-order Payment Logic & UAT:** Zaw initiated an inquiry on Mar 24 regarding pre-order flows (app payment vs. POS redemption) and requested peer review for the offline pre-order admin page (`https://admin-uat.fairprice.com.sg/in-store-preorder/offline`).
4.  **Slot Date Discrepancy:** Shiva reported a delivery slot mismatch (UI shows 25th, API indicates 23rd). Daryl Ng and Sundy Yaputra are resolving this.
5.  **UAT Stock Requirements:** Sneha requested high-stock SKUs for Zi Ying's bulk order testing; Wai Ching Chan and Akash Gupta were tasked to check IMS availability.
6.  **Order Verification Bug (NED-278216):** Investigation continues into the Whitelisting API returning older contract data (identified by Andin).
7.  **BCRS Deposit & SAP Integration:** Critical duplicate deposit posting fix remains active (PR #6). Marketplace tickets are planned for release tomorrow in sync with SAP deployment.

**Pending Actions & Ownership**
*   **All Engineers:** Mark all tickets deployed to production as "Status = Done." Highlight any pending deployments immediately (Sneha Parab).
*   **Wai Ching Chan, Gopalakrishna Dhulipati, Dang Hung Cuong:** Validate and implement emoji blocking logic for iOS address entry/editing to prevent order slot failures. Reference Customer ID: 2022036.
*   **Zaw Myo Htet:** Clarify pre-order payment redemption logic; execute UAT testing on offboarded Pinelabs split feature flag.
*   **Lester Santiago Soriano:** Assist with Whitelisting API contract issue (cc: Piraba Nagkeeran, Jonathan Tanudjaja). Deployment completed Mar 19.
*   **Wai Ching Chan & Akash Gupta:** Source high-stock SKUs from IMS for Zi Ying's bulk order testing and investigate UAT SKU `13023506` threshold settings.
*   **Daryl Ng & Sundy Yaputra:** Resolve delivery slot date mismatch (UI showing 25th vs API 23rd).
*   **Andin Eswarlal Rajesh:** Investigate iOS slot mapping error and assist with Amplitude event tracking flow inquiry.

**Decisions Made**
*   **Status Protocol:** All engineers must update Jira ticket status to "Done" upon production deployment; pending items must be flagged in the chat thread.
*   **Deployment Approval:** PLU processor deployment approved pending UD alignment.
*   **Code Review Priority:** Focus shifted to `go-platform-website` PR #1538 for the Strudel SDK update, superseding previous layout-service priorities. Current focus includes reviewing the new offline pre-order admin page and addressing iOS emoji validation.

**Key Dates & Deadlines**
*   **Mar 19, 2026:** Website deployment completed at 4:00 PM; UAT stock sourcing required immediately.
*   **Mar 24, 2026:** Zaw Myo Htet initiated inquiry regarding the offline pre-order admin page and pre-order payment logic.
*   **Mar 25, 2026 (Yesterday):** Sneha Parab requested status updates on production deployments and highlighted open tickets via Jira filter ID: DPD-225 queue.
*   **Mar 26, 2026 (Today):** Wai Ching Chan flagged the iOS address emoji bug; peer review initiated for Gopalakrishna Dhulipati and Dang Hung Cuong.
*   **Tomorrow:** Marketplace tickets release in sync with SAP deployment.
*   **Thursday:** D&T All Hands meeting.
*   **Mar 31, 2026:** Sports Hub FFS store closure deadline.

**Note on Historical Context:** Previous mentions of code review priorities for `layout-service` PR #362 and `website-service` PR #649 are superseded by the urgent Strudel SDK deployment update. The focus has now shifted to resolving slot date mismatches, pre-order payment logic queries, and the newly flagged iOS address emoji blocking issue on customer view 2022036. A new procedural requirement mandates immediate status updates for production tickets.


## [28/85] [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Last Activity: 2026-03-26T10:31:33.408000+00:00 | Last Updated: 2026-03-26T14:40:10.250016+00:00
**Daily Work Briefing: [Prod Support] Marketplace**

**Key Participants & Roles**
*   **Support/Operations:** Willie Tan, Iris Chang, Lalita Phichagonakasit, Charlene Tan, Jie Yi Tan, Ayton See, Amos Lam, Michelle Lim.
*   **Technical/Admin Team:** Dang Hung Cuong, Shiva Kumar Yalagunda Bas (Frequent recipients of access/access issues), Olivia -, Jill Ong, Greta Lee, Zaw Myo Htet, Angella Yeo, Cassandra Thoi, Gopalakrishna Dhulipati, Ee Ling Tan.

**Main Topics & Discussion Summary**
The conversation covers critical operational blockers regarding seller onboarding, order fulfillment discrepancies, system configuration errors, urgent promotion removal requests, and new order inquiries. New discussions include sales report generation requests, PickerApp barcode scanning failures, and picklist confirmation for specific B2B orders. Major themes include:

1.  **Sales Data & Reporting:**
    *   Iris Chang (Mar 26) requested the Jan–Dec 2023 Sales breakdown report for **UNICO Distribution Services Pte Ltd (31933)**. A Jira ticket has been raised (NED-281073).
2.  **PickerApp & Scanning Errors:**
    *   Greta Lee (Mar 26) reported that seller **Yumsay Foods** cannot scan SKU **90244060** (Barcode: 8881300862060); the system returns an error stating "SKU barcode does not exist."
3.  **Picklist Verification:**
    *   Ee Ling Tan (Mar 26) requested confirmation on whether seller **SINHUA HOCK KEE TRADING** will receive a picklist tomorrow for Order #257719344 (SKU: 90022072, Qty: 105, Delivery: Mar 31).

**Pending Actions & Ownership**
*   **Sales Report Request:** Provide Jan–Dec 2023 sales breakdown for UNICO Distribution Services (NED-281073) (Iris Chang, Mar 26).
*   **PickerApp Barcode Issue:** Technical team (Dang Hung Cuong, Shiva Kumar Yalagunda Bas, Angela Yeo) to investigate why SKU 90244060 for Yumsay Foods is flagged as non-existent in PickerApp.
*   **Picklist Confirmation:** Dang Hung Cuong to confirm picklist delivery status for Sinhua Hock Kee Order #257719344 (Ee Ling Tan, Mar 26).
*   **Urgent Promotion Removal:** Dang Hung Cuong and Gopalakrishna Dhulipati to immediately remove incorrectly set up promotion for Item ID: 90244361 (Lalita Phichagonakasit request, Mar 20).
*   **Order Status Investigation:** Dang Hung Cuong, Shiva Kumar Yalagunda Bas, and Amos Lam to check discrepancies for Order #256055476 (DBP vs. Mirakl) and Order #248407866 (API cancellation) (Cassandra Thoi, Mar 25).
*   **Resend User Invitation:** Technical team to investigate how to resend the Mirakl invitation email for the "Frutrip Official Store" user who did not receive it (Michelle Lim, Mar 23).
*   **Picklist Generation Failure:** Technical team to investigate why a vendor who opted out of public holidays in December did not receive a pick list today (Amos Lam, Mar 21).
*   **FFS Order Inquiry:** Technical team to investigate FFS order status for seller "Yumsay Food" (Angela Yeo, Mar 21).
*   **Vendor Report Issues:** Investigate missing sales breakdown reports for CoLab Apac (NED-277148) and Old Shanghai (NED-277329).
*   **Access Grants:** Grant PickerApp access to Meat Affair, BulkMartGo, PETS STATION HOLDING, and others. Resolve Woah Group "Offers" error (Charlene Tan).

**Decisions Made**
*   Dang Hung Cuong is prioritizing the removal of Item ID: 90244361, the new picklist failure issue raised by Amos Lam, and the Woah Group offers error. Dang Hung Cuong and Shiva Kumar Yalagunda Bas are assigned to investigate the vendor picklist anomaly. Ayton See previously educated a seller on promotion setup rules after identifying a configuration error.

**Key Dates & Deadlines**
*   **2026-03-26 (Today):** Iris Chang requested sales report for UNICO Distribution Services; Greta Lee reported Yumsay Foods barcode issue; Ee Ling Tan queried picklist delivery for Sinhua Hock Kee. Previous urgent request to remove Item ID: 90244361 remains active from Mar 20.
*   **2026-03-25:** Cassandra Thoi requested checks on orders #256055476 and #248407866.
*   **2026-03-23:** Michelle Lim reported Mirakl email notification failure for Frutrip Official Store user.
*   **2026-03-21:** Angela Yeo requested advice on FFS orders for "Yumsay Food"; Amos Lam reported vendor picklist failure due to public holiday opt-out status.
*   **2026-03-19:** Jie Yi Tan reported Funa Artistic Hampers & Gifts delivery window discrepancy; discussion ongoing with 34 replies.
*   **2026-03-18:** Iris Chang inquired about SAP T-code ZMP_VENDOR "Lead Time" definition.


## [29/85] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE/S2k2gx19hOs | Last Activity: 2026-03-26T10:12:09.136000+00:00 | Last Updated: 2026-03-26T10:44:58.617361+00:00
**Daily Work Briefing: Google Chat Summary**

**Key Participants & Roles**
*   **Nikhil Grover:** Analyzing data trends; identifying risks; driving incident management.
*   **Michael Bui:** Seeking clarification on specific metrics and stakeholder status (OSMSO).

**Main Topic**
Discussion regarding a discrepancy in March 19th data, specifically concerning impression numbers versus the percentage of multi-product responses on the search page, and the decision to escalate a potential revenue-impacting drop.

**Pending Actions & Owners**
*   **Raise Incident:** Nikhil Grover intends to raise an incident immediately due to a significant drop in impressions with revenue implications. He believes waiting for OSMSO feedback is not viable given the impact. (Owner: Nikhil Grover)
*   **OSMSO Data Follow-up:** Both parties are awaiting confirmation from OSMSO regarding specific metrics. (Owner: Pending external response, but ownership lies with both to monitor).

**Decisions Made**
*   **Incident Escalation:** It was agreed that an incident should be raised immediately regarding the drop in impressions, despite missing data from OSMSO. Nikhil Grover explicitly stated, "I think important to raise incident now."
*   **Data Scope Clarification:** Confirmed that the "unchanged" numbers previously discussed referred strictly to the search page impression data for March 19th, which remains stable. The initial confusion arose because Michael Bui was referencing a different metric (percentage of responses containing 2+ products) or a different view (2 pages vs. 1 page).

**Key Dates & Context**
*   **March 19:** The specific date for the data anomaly in question.
*   **March 25:** Nikhil Grover posted "11 replies" (contextual marker).
*   **March 26, 04:27 UTC:** Michael Bui noted numbers for March 19 had been changed.
*   **March 26, 09:20 UTC:** Nikhil clarified that search page impressions for March 19 were actually unchanged and this was not supposed to change.
*   **March 26, 10:04–10:12 UTC:** Clarification regarding OSMSO data; confirmed OSMSO has not yet returned numbers for the "% of 2 or more products in the response."

**Summary Notes**
The conversation clarified that while impression numbers for the search page on March 19 are stable, there is a broader concern regarding dropped impressions impacting revenue. Consequently, the team prioritized raising an incident over waiting for OSMSO to provide specific multi-product response percentage data.


## [30/85] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/yjyq94srBMw | Last Activity: 2026-03-26T10:04:49.922000+00:00 | Last Updated: 2026-03-26T10:45:20.585139+00:00
**Daily Briefing: BCRS Firefighting Group (Re-delivery Use Case)**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Project Lead/Coordinator. Driving timeline clarification and dependency mapping.
*   **Michael Bui:** Developer (Sales Posting). Clarified parallel execution capabilities; noted upcoming leave.
*   **De Wei Tey:** RPA Engineer. Confirmed delivery readiness for UAT.
*   **Wai Ching Chan:** Developer (Order Service). Confirmed UAT status of metadata field.
*   **Koklin Gan:** Stakeholder/Manager. Raised concerns regarding April 1st deadlines and mitigation strategies.
*   **Daryl Ng:** Noted as a potential alternative resource for BCRS posting tasks.

**Main Topic**
Discussion focused on the **"Re-delivery" use case for BCRS (BCRS Firefighting Group)** to prevent duplicate deposit postings in SAP. The team addressed task dependencies, timelines, and mitigation strategies regarding an upcoming April 1st deadline. The initiative involves three core jobs: updating metadata flags, consuming those flags to suppress duplicates, and executing RPA charges.

**Decisions Made**
*   **Parallel Execution:** Michael Bui confirmed that the Sales Posting work (Item #2) has **no dependency** on the completion of the RPA deployment (Item #3); both can proceed in parallel.
*   **UAT Deadline Confirmed:** De Wei Tey confirmed the RPA solution will be ready for UAT testing by **April 1**.
*   **Compliance Status:** Prajney Sribhashyam clarified that while the fix is not mandatory for April 1st, it impacts all re-deliveries of orders containing BCRS SKUs.

**Pending Actions & Ownership**
*   **Update Jira Ticket (DPD-807):** Prajney Sribhashyam will update the ticket with finalized details and timelines after clarifying dependencies.
*   **Start Development:** De Wei Tey to begin work on RPA tasks immediately (starting tomorrow, March 27).
*   **SIT Planning:** Michael Bui previously indicated System Integration Testing (SIT) is likely scheduled for **April 6–7** (referred to as "06-07/4").

**Key Dates & Deadlines**
*   **March 27, 2026:** Target start date for RPA development tasks.
*   **April 1, 2026:** Deadline for RPA readiness (UAT testing).
*   **April 6–7, 2026:** Estimated window for SIT completion (per Michael Bui).

**Contextual Notes**
*   Michael Bui is going on leave the following week; immediate alignment was required to ensure handover or continuity.
*   Koklin Gan raised concerns about a potential gap between the April 1st requirement and the final timeline, suggesting mitigation via stopping BCRS SKU re-deliveries if necessary. Prajney noted that RPA completion is estimated at 3–5 days from the start date.


## [31/85] Backend Chapter
Source: gchat | Group: space/AAAAHhDyHI4 | Last Activity: 2026-03-26T09:57:03.534000+00:00 | Last Updated: 2026-03-26T10:45:48.624917+00:00
**Daily Work Briefing: Backend Chapter**

**Key Participants & Roles**
*   **Michael Bui:** Investigated GCP PubSub configuration.
*   **Nicholas Tan:** Flagged critical supply-chain security issues (Trivy/LiteLLM); paused pipelines; identified expired cluster certificates requiring immediate rotation.
*   **Lester Santiago Soriano:** Blocked on CI/CD pipeline errors after upgrading Go dependencies.
*   **Boon Seng Ong:** Investigated ESPv2 deployment failures.

**Main Topics**
1.  **Critical Supply-Chain Security Alert (March 26, Morning):** Nicholas Tan identified a "Trojanization" attack affecting Trivy, Checkmarx, and LiteLLM tools (source: Kaspersky blog).
    *   *Action:* Users with `trivy` CLI version `v0.69.4` must uninstall immediately. Users with `litellm` on local machines are instructed **not** to upgrade, as the binary is compromised.
2.  **CI/CD & Dependency Upgrade (March 12):** Lester Santiago Soriano upgraded `stdlib` to `v1.25.8`. The pipeline failed due to a version mismatch between the project target (Go 1.25.8) and the build agent's `golangci-lint` (compiled with Go 1.24).
    *   *Root Cause:* Requires update to the `dpd-backend-cicd` resource.
3.  **ESPv2 Deployment Failure (March 25):** Boon Seng Ong reported failures in `deploy-esp-image` due to invalid flags for `gcloud beta run deploy` and `update-traffic`. Suspects changes to the "golden pipeline."
4.  **Service Account Security Audit (March 16):** Nicholas Tan identified JSON keys embedded in Service Accounts (`pong-club-agent`, `vertex-client`) within `fpg-titan-preprod` requiring decomposition.
5.  **Cluster Certificate Expiry (March 26, 09:57 UTC):** Nicholas Tan flagged an urgent need to identify the owner of a specific cluster and rotate certificates immediately, warning that failure to do so will cause cluster failure ("go boom boom").

**Pending Actions & Ownership**
*   **Eradicate Compromised CLI Tools:** Immediately uninstall `trivy` v0.69.4 from all laptops; halt upgrades for `litellm`.
    *   *Owner:* **All Team Members**.
*   **Resolve CI/CD Pipeline Block (Go Version):** Update `dpd-backend-cicd` resource to support Go 1.25.8 or align linter version.
    *   *Owner:* **TBD** (Lester requested ownership).
*   **Investigate Golden Pipeline Breakage:** Determine changes causing `gcloud beta run deploy` failures for ESPv2.
    *   *Owner:* **Boon Seng Ong**.
*   **Service Account Cleanup:** Decompose identified SAs (`pong-club-agent`, `vertex-client`) in `fpg-titan-preprod`.
    *   *Owner:* **TBD** (Nicholas Tan flagged).
*   **Cluster Certificate Rotation:** Identify cluster owner and rotate certificates immediately to prevent outage.
    *   *Owner:* **TBD** (Nicholas Tan requested help).

**Decisions Made**
*   Pipelines for `infra-gcp-fpg-titan` remain disabled pending the resolution of Trivy CLI risks.
*   The team has been instructed to remove specific compromised tool versions locally; local development environments are now a security priority over CI/CD infrastructure.
*   Immediate attention is required to identify cluster owners for certificate rotation.

**Key Dates & Follow-ups**
*   **March 6, 2026:** Initial PubSub inquiry (Open).
*   **March 12, 2026:** Pipeline failure reported; escalation for CICD ownership required.
*   **March 16, 2026:** Security flag raised regarding `fpg-titan-preprod` SAs.
*   **March 25, 2026:** Critical deployment failure reported; investigation into golden pipeline changes initiated.
*   **March 26, 2026 (Morning):** Supply-chain attack confirmed; immediate local cleanup required.
*   **March 26, 2026 (09:57 UTC):** Urgent cluster certificate rotation identified as critical path item to prevent failure.


## [32/85] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Last Activity: 2026-03-26T09:37:22.662000+00:00 | Last Updated: 2026-03-26T10:46:30.885483+00:00
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

**Newly Resolved Incident (Mar 26):**
*   **Trigger:** March 26, 2026, at 06:15 UTC.
*   **Recovery:** March 26, 2026, at 09:37 UTC.
*   **Story Key:** `7b73b037-696a-5016-bca4-5c22e31b6245`.
*   **Duration:** ~3 hours 22 minutes.
*   **Status:** **Resolved**.

### Pending Actions & Ownership
*   **Immediate Action:** The systemic error "Datadog is unable to process your request" persists across all incidents. The new incident (Mar 26) lasted ~3.4 hours, aligning closer to the historical average than the outlier Mar 25 incident (~24h). No immediate escalation required for this specific event.
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Investigation Note:** While the Mar 26 duration is within normal variance, the persistent error message and the previous Mar 25 outlier warrant continued trend analysis to rule out pipeline degradation.

### Decisions Made
*   **Status:** No escalation triggered for the Mar 26 incident as it resolved within standard norms (<6 hours).
*   **Protocol:** Continue active surveillance. If a new trigger occurs with similar error messaging and resolution time exceeds 6 hours, escalate immediately to SRE/Platform Engineering.

### Key Dates & Follow-ups
*   **Latest Event:** March 26, 2026, at 09:37 UTC (Recovered).
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Monitor for recurrence. The extended duration of the Mar 25 incident remains an outlier requiring trend analysis.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Datadog Monitor Link:** [View in Datadog](https://app.datadoghq.eu/monitors/17447511)
*   **Latest Incident (Mar 26):** https://app.datadoghq.eu/monitors/17447511?group=story_key%3A7b73b037-696a-5016-bca4-5c22e31b6245

### Monitor Configuration
*   **Query:** `events("source:watchdog (story_category:infrastructure -story_type:(tcp_retrans_jump OR full_disk_forecast)) env:(PROD OR production OR prod)").rollup("count").by("story_key").last("30m") > 0`


## [33/85] RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU | Last Activity: 2026-03-26T09:12:17.093000+00:00 | Last Updated: 2026-03-26T10:47:32.420567+00:00
**Daily Briefing Summary: RMN Leadership Space (Updated Mar 26)**

**Key Participants & Roles**
*   **Bryan Choong:** Returning from eTail Asia; prioritizing Q1 case study compilation and low-sodium project. Emphasized the need for a tracker on developing case studies.
*   **Pauline Tan:** Managing LinkedIn content (FPG ADvantage page) and award repurposing. Currently transitioning from award submissions to case study development.
*   **Rajiv Kumar Singh:** Coordinating SOAC planning; shared industry benchmark regarding DoorDash Ads sales lift measurement (+30% incrementality).
*   **Allen Umali:** Leading SignCloud cleanup and Advertima loop verification (Legacy hardware status remains active).

**Main Topics**
1.  **Case Study Development & Tracking:** With Q1 ending, Bryan Choong requested a tracker for developing case studies. Pauline Tan confirmed the HPB case study is in progress; she recently submitted long-form award entries for Drum APAC and Retail Asia Awards (Mar 26), which will be repurposed into shorter formats. She is also preparing an APB submission. Bryan directed immediate focus on building a "low sodium" case study while BD team explores other potential leads to avoid delays similar to HPB timelines.
2.  **Industry Benchmarking:** Rajiv Kumar Singh shared insights from DoorDash Ads, noting new sales lift measurement capabilities driving up to 30% incrementality for brands on average (Mar 26).
3.  **SignCloud Cleanup:** Legacy hardware cleanup continues; Allen Umali confirmed the full list is available for removal by Mar 28.

**Pending Actions & Owners**
*   **Case Study Tracker:** Establish and maintain a refreshed tracker of strong Q1 case studies. *Owner: Pauline Tan.*
*   **Low Sodium Case Study:** Accelerate development of this specific asset to prioritize immediate wins over long-cycle projects like HPB. *Owners: Bryan Choong, Pauline Tan.*
*   **HPB & APB Submissions:** Convert submitted award entries (Drum APAC, Retail Asia) into case study formats; prepare APB submission. *Owner: Pauline Tan.*
*   **SignCloud Cleanup:** Complete manual removal of legacy screens and resolve loop errors. *Owner: Allen Umali | Deadline: Mar 28.*
*   **Advertima SRA Renewal:** Secure new SRA for long-term partnership beyond April extended PoV. *Owners: Allen Umali, Alvin Choo.*
*   **SOAC Planning:** Finalize targets per CM, supplier, and category by end of March. *Owner: Rajiv Kumar Singh & Ryan.*

**Decisions Made**
*   **Case Study Priorities:** Immediate focus shifted to "low sodium" case study construction; HPB and APB efforts rely on repurposing recent award submissions rather than starting from scratch.
*   **Award Repurposing Strategy:** Long-form entries for Drum APAC and Retail Asia Awards (submitted Mar 26) will be adapted into concise case studies.
*   **SignCloud Resolution:** Manual purging of old screens confirmed, targeting completion this week.
*   **Industry Alignment:** Team to consider DoorDash's sales lift measurement benchmarks (+30% incrementality) for future campaign strategies.

**Key Dates & Deadlines**
*   **Mar 26:** Pauline Tan submitted award entries (Drum APAC, Retail Asia); Bryan Choong requested case study tracker and low-sodium focus; Rajiv shared DoorDash benchmark data.
*   **Mar 28 (Est.):** Completion of SignCloud manual cleanup.
*   **End of March:** Deadline to finalize SOAC targets.
*   **April End:** Current deadline for Advertima extended PoV operations.


## [34/85] BCRS Regroup - Open Item Planning - Mar 26
Source: gchat | Group: space/AAQAC8aeuag | Last Activity: 2026-03-26T08:53:37.675000+00:00 | Last Updated: 2026-03-26T10:47:43.346295+00:00
**Daily Work Briefing: BCRS Regroup – Open Item Planning (Mar 26)**

**Key Participants & Roles**
*   **Daryl Ng:** Initiator of the planning session; provides project status updates.
*   **Prajney Sribhashyam:** Facilitator/Owner of tracking documentation; coordinates stakeholder inclusion.
*   **Wai Ching Chan:** Active participant in the chat space (availability confirmed).

**Main Topic**
The discussion focuses on identifying open items for the "BCRS Regroup" and determining necessary leads and members required to address them, specifically within the context of Project Light.

**Pending Actions & Ownership**
*   **Action:** Populate the newly created tracking sheet with relevant leads and required members.
    *   **Owner:** Daryl Ng (Responding to Prajney's request at 05:07).
*   **Action:** Review and acknowledge the shared Google Chat room link for further discussion or documentation.
    *   **Owner:** Wai Ching Chan (Link viewed by 3 of 8 participants).

**Decisions Made**
*   No formal decisions were recorded in this chat log; the group agreed to utilize a shared sheet for tracking open items and leads.

**Key Dates, Deadlines & Follow-ups**
*   **Date:** March 26, 2026.
*   **Upcoming Meeting:** Project Light Backlog and Sprint Planning discussion scheduled from **4:00 PM – 5:00 PM**.
*   **Reference Links:**
    *   Master Sheet: Created by Prajney Sribhashyam (Time: 05:06).
    *   Chat Room Link: `https://chat.google.com/room/AAQAgT-LpYY/qtUOXlxVm80/o5O3fA1DeMA` (Shared at 08:53).


## [35/85] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/qtUOXlxVm80 | Last Activity: 2026-03-26T08:53:13.643000+00:00 | Last Updated: 2026-03-26T10:48:04.829699+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles:**
*   **Prajney Sribhashyam:** Initiator; confirmed Jira ticket updates (DPD-807) and clarified RPA ownership for deposit charging.
*   **Wai Ching Chan:** Implementing metadata in UAT config service; provided API examples (cURL/gRPC); identified need to contact a Config Service owner for production.
*   **Michael Bui:** Clarified that the metadata change prevents duplicates but does not handle the actual redelivery logic; requested effort estimates and assignment of the RPA task; noted upcoming leave starting next week.
*   **De Wei Tey:** Provided estimates for related tasks (Order Service maintenance and RPA).
*   **Sneha Parab:** Identified as a potential Config Service owner to approach for production metadata updates.

**Main Topic:**
Discussion regarding the **'Re-delivery' use case for BCRS** (Jira: DPD-807). The focus has shifted from general coordination to specific implementation details and ownership clarification. Key deliverables remain:
1.  **Config Service:** Wai Ching Chan is adding "Deposit posted to SAP" metadata to the UAT config service via Backoffice (`admin-uat.fairprice.com.sg`). Production requires a Config Service owner (Sneha Parab or similar).
2.  **Order Service:** Maintaining 'Deposit posted to SAP' in metadata; Wai Ching Chan provided specific cURL and gRPC call examples for UAT testing (`api.zs-uat.fairprice.com.sg/order-service/v3/deliveryOrders`).
3.  **Sales Posting:** Consumes the field to suppress duplicate BCRS deposit postings (Task 2 & 3 in Jira).
4.  **RPA Logic:** Specifically handles charging the BCRS deposit to the customer's original payment method (Point 4). Prajney clarified this is an RPA task, distinct from Michael's metadata changes.

**Actions Pending & Ownership:**
*   **Production Metadata Setup:** Wai Ching Chan and team must identify and approach the **Config Service owner** (Sneha Parab suggested) to add the field in production.
*   **Technical Implementation:** Wai Ching Chan will test UAT updates using provided API calls; development effort estimated at 1-2 days by Wai Ching/De Wei Tey.
*   **Timeline & SIT:** Michael Bui is on leave starting next week; earliest System Integration Testing (SIT) date is **April 6 or April 7, 2026**.
*   **Jira Updates:** Prajney confirmed Task 4 (RPA) has been assigned and added to the ticket.

**Decisions Made:**
*   The metadata field ("Deposit posted to SAP") will be implemented via the Config Service for UAT, with production handled by a designated service owner.
*   Michael Bui's changes specifically address duplicate prevention; the **RPA team** retains ownership of the redelivery charge logic.
*   SIT is scheduled for early April due to Michael Bui's leave schedule.

**Key Dates & Follow-ups:**
*   **Discussion Dates:** March 24, 2026 (Initial briefing); March 26, 2026 (Implementation details).
*   **Upcoming Leave/SIT Window:** Michael Bui leaves next week; SIT targeted for **April 6–7, 2026**.
*   **Reference Link:** https://ntuclink.atlassian.net/browse/DPD-807

**Technical References:**
*   UAT Config: `https://admin-uat.fairprice.com.sg/settings/extensions/18`
*   UAT Delivery Order Admin: `https://admin-uat.fairprice.com.sg/customer-support/delivery-orders/75588070`


## [36/85] [BCRS]-SAP to POS & DBP Interface Deployment
Source: gchat | Group: space/AAQAeMC3qBk/wHwvIxHWK_U | Last Activity: 2026-03-26T08:14:28.945000+00:00 | Last Updated: 2026-03-26T10:50:31.865720+00:00
**Daily Work Briefing: [BCRS]-SAP to POS & DBP Interface Deployment**

**Key Participants & Roles**
*   **Onkar Bamane:** Lead coordinator; requested documentation updates and confirmed team readiness.
*   **Michael Bui:** Contributor; added deployment steps to the tracking sheet.
*   **Sneha Parab:** Contributor and Planner; updated the sheet and confirmed resource availability for parallel deployments.
*   **Shiva Kumar Yalagunda Bas & Dang Hung Cuong:** Designated resources identified for MP (Mirakl) deployment support.

**Main Topic**
Coordination of documentation updates and resource allocation for the upcoming SAP to POS & DBP Interface Deployment, with specific focus on ensuring step-by-step procedures are recorded and team availability is confirmed.

**Pending Actions & Ownership**
*   **Review Documentation:** Onkar Bamane (via Sneha Parab) needs to verify if Michael Bui's added row contains all necessary details or requires further input.
*   **Standby Coordination:** Sneha Parab has flagged the need for three specific team members (including herself, Michael Bui, and potentially others) to be available for deployment, testing, and standby duties during the SAP deployment window.

**Decisions Made**
*   **Resource Allocation for MP Deployment:** It was confirmed that three individuals will support the MP deployment (combining DBP + Mirakl). This team will handle deployment, testing, and standby specifically while the SAP deployment is ongoing.
*   **Process Confirmation:** Onkar Bamane acknowledged the updates ("ok"), indicating acceptance of the current status of the sheet and the proposed resource plan.

**Key Dates & Follow-ups**
*   **Timeline Context:** All activities discussed occurred on **2026-03-26**, between **07:05 UTC** (initial request) and **08:14 UTC** (final confirmation).
*   **Immediate Follow-up:** Verification of the completeness of Michael Bui's entries in the shared sheet.
*   **Upcoming Event:** The SAP deployment window is imminent, requiring the designated team to be on standby.


## [37/85] SRE / Network / DBA / DevOps / Infra
Source: gchat | Group: space/AAAAYX-ew1s | Last Activity: 2026-03-26T08:10:20.971000+00:00 | Last Updated: 2026-03-26T10:52:16.313378+00:00
**Daily Work Briefing: SRE / Infrastructure Team**

**Key Participants & Roles**
*   **Madhawa Mallika Arachchige:** Requests PR reviews/merges for Datadog configurations; confirmed channel usage on **2026-03-26**.
*   **Natalya Kosenko:** Raises IaC strategy questions, requests Terraform support, and submits compliance-related PRs.
*   **Kalana Thejitha:** Reports pipeline failures in new projects (Soni-BE).
*   **Lester Santiago Soriano:** Reports Go versioning conflicts in CI/CD pipelines.
*   **Boning He:** Requests access to pricing Terraform workspaces via PR #722.
*   **Dodla Gopi Krishna:** Requests Terraform review.
*   **Zheng Ming:** Reported US-Central1 internet connectivity failure for AI agents; opened ticket GCD-8941.
*   **Wai Ching Chan:** Reports bastion connectivity issues affecting team operations; raised ticket GCD-8954.
*   **Calvin Phan:** Raised request for CloudSQL subnets for project SOT-SONI creation; ticket DSD-11066.
*   **Himal Hewagamage & Isuru Dilhan:** Primary reviewers/approvers for PRs and incident support.
*   **Mohit Niranwal, Andin Eswarlal Rajesh:** Tagged stakeholders/reviewers.

**Main Topics**
1.  **Datadog Infrastructure & Compliance:** Multiple requests to review/merge PRs (#135–#148) related to `fp-datadog-eu`. On **2026-03-26**, Madhawa Mallika Arachchige confirmed the submission channel for new PRs. Strategic discussion regarding IaC for Datadog log pipelines and RBAC enforcement continues.
2.  **Terraform & Workspaces Management:** New PR **#719** submitted by Natalya Kosenko. Previous requests included PR #716. A failed Terraform plan (`run-CZVLtajJGbLVojLM`) and ticket GCD-8900 remain active.
3.  **CI/CD Pipeline Failures:**
    *   **Soni-BE:** `golden pipeline` clone step failing on new projects; SSH key status questioned.
    *   **lt-strudel-api-go:** Build failure after upgrading Go to `1.25.8`; `golangci-lint` conflict noted.
4.  **Cloud Networking (New):** AI agents in `us-central1` mothership subnets cannot connect to the internet. Zheng Ming raised ticket **GCD-8941** for Cloud NAT.
5.  **Bastion Connectivity:** Wai Ching Chan reported bastion connectivity issues affecting team operations; raised ticket **GCD-8954**.
6.  **Database Subnet Request (New):** Calvin Phan requested subnets for CloudSQL to support the **SOT-SONI** project creation. Ticket **DSD-11066** opened. DBA team is coordinating with @Himal Hewagamage regarding this request.

**Pending Actions & Ownership**
*   **Merge/Review Datadog PRs:**
    *   PR #135, #137–#139 (`fp-datadog-eu`): Owned by @Himal Hewagamage and @Isuru Dilhan.
    *   PR #140 (`gcp-fpg-optimus`) & new submissions: New request from **Madhawa Mallika Arachchige** (via channel confirmation); tagged for review by @Nicholas Tan, @Maou Sheng Lee, and now **@Andin Eswarlal Rajesh**.
    *   PR #144 & #147 (`fp-datadog-eu`): Owned by @Isuru Dilhan and @Himal Hewagamage.
*   **Merge/Review Terraform PRs:**
    *   PR **#719** (`tfe-workspaces`) (Natalya Kosenko) & **PR #722** (Boning He): Review pending with @Isuru Dilhan and @Himal Hewagamage. PR #722 is for Boning's access to pricing Terraform workspaces.
*   **Troubleshoot Pipeline Issues:**
    *   Soni-BE Golden Pipeline clone failure: Investigate SSH key/environment (Kalana).
    *   `lt-strudel-api-go` Go version mismatch: Resolve `golangci-lint` config vs. target Go version conflict (Lester).
*   **Infrastructure Strategy:** Evaluate IaC implementation for Datadog log pipelines (Natalya; discussion ongoing with @Prabu Ramamurthy Selvaraj).
*   **Terraform Support:** Investigate failed run `run-CZVLtajJGbLVojLM` and ticket GCD-8900.
*   **Cloud NAT Provisioning:** Review Cloud NAT request for `us-central1`. **@Mohit Niranwal** requested testing in non-prod first before full rollout (regarding GCD-8941). @Himal Hewagamage, @Tan Nhu Duong, and @Andin Eswarlal Rajesh are cc'd.
*   **Bastion Connectivity:** Investigate issue affecting Wai Ching Chan's team. Ticket **GCD-8954** raised; @Nicholas Tan, @Gopalakrishna Dhulipati, and @Akash Gupta notified.
*   **DBA Subnet Request:** Review CloudSQL subnet requirements for SOT-SONI project (Calvin Phan). @Himal Hewagamage is engaged via ticket DSD-11066.

**Decisions Made**
*   **IaC Requirement:** Clear requirement established for IaC adoption for Datadog pipelines to ensure auditability.
*   **Change Management Protocol:** Mohit Niranwal mandated testing new Cloud NAT configurations in non-production environments prior to production deployment (regarding GCD-8941).

**Key Dates & Follow-ups**
*   **2026-03-02 to 03-05:** Multiple PR requests from Madhawa.
*   **2026-03-11 to 03-12:** Critical pipeline failures reported by Kalana and Lester.
*   **2026-03-13:** Datadog strategy discussion initiated; Terraform plan failure reported.
*   **2026-03-16:** Service desk ticket GCD-8900 opened; PR #147, #148 (`fp-datadog-eu`), and #719 (`tfe-workspaces`) requested by Natalya Kosenko.
*   **2026-03-19:** Zheng Ming reported connectivity failure for AI agents; raised ticket GCD-8941. Mohit Niranwal intervened regarding non-prod testing.
*   **2026-03-20:** Wai Ching Chan reported bastion connectivity issues (GCD-8954). Calvin Phan requested CloudSQL subnets for SOT-SONI project (DSD-11066); @Himal Hewagamage replied.
*   **2026-03-24:** Himal Hewagamage requested review of PR #140 (`gcp-fpg-optimus`) tagged to @Nicholas Tan and @Maou Sheng Lee. Boning He requested review of PR #722, tagged to @Isuru Dilhan and @Himal Hewagamage.
*   **2026-03-26:** Madhawa Mallika Arachchige confirmed the submission channel for Datadog PRs; @Andin Eswarlal Rajesh engaged in conversation regarding these requests.


## [38/85] BCRS ECOMM SAP POSTING
Source: gchat | Group: space/AAQA-ICuJRM | Last Activity: 2026-03-26T07:54:50.976000+00:00 | Last Updated: 2026-03-26T10:53:06.349496+00:00
**Daily Work Briefing: BCRS ECOMM SAP POSTING & Refunds UAT (Mar 26 Update)**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** UAT lead; coordinating validation and technical alignment.
*   **Tan Gay Lee:** Stakeholder rejecting current sign-off due to GL entry errors in pre-order/S&G refunds.
*   **Lai Shu Hui:** Accounting participant; pending final test case closure for e-commerce returns.
*   **Sathya Murthy Karthik:** Confirmed 2 untested e-commerce cases remain; advocating for immediate sign-off.
*   **Onkar Bamane:** Previously requested separate IT audit sign-off (now adjusted scope).
*   **Yaxin Hao / Jianbin Huang:** Technical owners asked to check Store 420 UAT sales data.

**Main Topic**
UAT progress is stalled due to GL entry discrepancies in Pre-order and Scan 'n Go (S&G) refunds, preventing final sign-off. While SAP recommends using the "Data 8" aggregation method for deposit refunds instead of RPA, Tan Gay Lee asserts that current refund entries are not captured in the correct GL accounts, rendering the E-Comm Returns & Refunds scope incomplete without these corrections.

**Status of Issues & Updates**
*   **Sign-off Scope Adjustment:** Following alignment on the call (Mar 26), S&G deposit refunds are excluded from the "Returns & Refunds" sign-off. A separate sign-off is now requested specifically for E-Comm. The scope covers: (1) API for Posting Deposit Accounting, (2) Marketplace SKU creation, (3) Concess Sales Detail Report, and (4) Concess Sales Summary Report.
*   **GL Entry Discrepancy:** Tan Gay Lee rejected the sign-off, noting that refunds for pre-orders paid online are processed manually but fail to capture the correct GL account. Pre-orders cancelled within 5 days follow 'Cancellation after delivery' via CS; POS-paid pre-order refunds occur at POS with cash.
*   **Testing Status:** Sathya Murthy Karthik highlighted two untested e-commerce cases pending validation (Pass/Fail) and urged immediate closure to prevent delays. Prajney Sribhashyam requested clarification from Tan regarding the GL issue, citing previous alignment that E-Comm test cases were fine.
*   **Technical Checks:** Prajney Sribhashyam asked Yaxin Hao and Jianbin Huang to verify unprocessed sales for Store 420 in UAT.

**Pending Actions & Ownership**
1.  **GL Resolution:** Tan Gay Lee requested an emergency call (Google Meet: `emh-uzhw-vtz`) with Prajney and Sathya to resolve the incorrect GL capture issue for pre-order refunds. **(Owner: Prajney Sribhashyam, Sathya Murthy Karthik)**.
2.  **Test Case Closure:** Lai Shu Hui must validate the remaining two untested e-commerce cases immediately to allow sign-off. **(Owner: Lai Shu Hui)**.
3.  **Data Verification:** Check for unprocessed sales in Store 420 UAT. **(Owner: Yaxin Hao, Jianbin Huang)**.
4.  **Sign-off Execution:** Tan Gay Lee and Lai Shu Hui to provide the separate E-Comm sign-off once GL issues are resolved and tests pass. **(Owner: Tan Gay Lee, Lai Shu Hui)**.

**Decisions Made**
*   S&G deposit refund posting scope is excluded from the current "Returns & Refunds" sign-off; a distinct E-Comm sign-off is required.
*   RPA separate posting for deposit refunds is deemed inadvisable; SAP recommends using Data 8 aggregation (aligned with sales/BCRS deposit methods).
*   Current UAT cannot proceed to final deployment until the incorrect GL capture for pre-order refunds is addressed and two pending e-commerce test cases are validated.

**Key Dates & Follow-ups**
*   **Mar 26, 07:51 AM:** Tan Gay Lee flagged incorrect GL entries for pre-order refunds.
*   **Mar 26, 07:54 AM:** Emergency Google Meet scheduled to resolve the sign-off blocker.
*   **Mar 26, 03:03 AM:** Technical request sent to check Store 420 UAT data.

**Immediate Follow-up:** Attend the emergency video meeting to clarify GL handling for pre-order refunds and ensure Lai Shu Hui completes the two outstanding e-commerce test cases urgently.


## [39/85] Project Light: Mobilization and Planning Workshop Day 3 - Mar 26
Source: gchat | Group: space/AAQAwOH7W8A | Last Activity: 2026-03-26T07:31:58.093000+00:00 | Last Updated: 2026-03-26T10:54:35.988273+00:00
**Daily Work Briefing: Project Light Mobilization Workshop (Day 3)**

**Key Participants & Roles**
*   **Jacob Yeo**: Primary communicator regarding agenda updates.
*   **Pandi**: Uploaded a new resource link on March 26.
*   **Recipients**: 18 total members of the "Project Light" Mobilization and Planning group; 10 have viewed the latest shared resource (FairPrice Rewards Catalogue Edit).

**Main Topic/Discussion**
The discussion continues to center on critical updates for **Day 3** of the Project Light Mobilization and Planning Workshop, scheduled for **March 26**. While Jacob Yeo previously notified the team of "latest changes" to the schedule without detailing specific content, a new communication thread initiated by **Pandi** at 07:31 AM UTC on March 26 introduced a direct link to the FairPrice Rewards Catalogue edit page. This suggests the "changes" or operational requirements may involve catalog management or rewards program adjustments relevant to the day's agenda.

**Pending Actions & Ownership**
*   **Action**: Review the updated project agenda and new resource links.
    *   **Owner**: All 18 workshop participants.
    *   **Status Update**: While 11 members viewed the previous agenda document, current engagement metrics show that **10 of 18** participants have now accessed the FairPrice catalogue link provided by Pandi.
    *   **Reference (Agenda)**: [Project Light Workshop Agenda](https://docs.google.com/spreadsheets/d/1ODEEFsP8mMxmUhYNuQ1norNCnWoIJwddZzUFqEUX-qw/edit?gid=1079702164#gid_1079702164).
    *   **Reference (New Resource)**: [FairPrice Rewards Catalogue Edit](https://admin.fairprice.com.sg/rewards/catalogue/edit/1049) (Linked by Pandi).
*   **Action**: Integrate FairPrice catalogue updates into Day 3 planning.
    *   **Owner**: All participants.
    *   **Context**: Jacob Yeo's request to "take note of the latest changes" is now complemented by the specific operational link shared by Pandi, requiring immediate review before the session begins.

**Decisions Made**
No formal strategic decisions were recorded in these exchanges. The communications serve as mandatory notifications for agenda modifications and the introduction of new external tooling (FairPrice admin interface) for the workshop day.

**Key Dates & Follow-ups**
*   **Initial Notification Date**: March 25, 2026 (10:35 AM UTC).
*   **Resource Update Date**: March 26, 2026 (07:31 AM UTC) by Pandi.
*   **Event Date**: March 26, 2026 (Day 3 of Mobilization and Planning Workshop).
*   **Follow-up Required**: Immediate review of both the Google Sheet agenda and the FairPrice catalogue link by all attendees prior to the start of Day 3.

**Summary Note**
Participants must access the linked resources immediately. While Jacob Yeo flagged schedule changes on March 25, Pandi has subsequently provided a specific operational link (FairPrice Rewards Catalogue Edit) on the morning of the event. Engagement is tracking at 10 views out of 18 for this new resource, indicating a need for further reminders to ensure all stakeholders are aligned with both the schedule and the catalog updates before the workshop commences.


## [40/85] [Postmortem] 300126 - P1 - Some customers charged full price - Mar 26
Source: gchat | Group: space/AAQACrrEY0I | Last Activity: 2026-03-26T07:11:32.324000+00:00 | Last Updated: 2026-03-26T10:54:48.749435+00:00
**Daily Work Briefing: Incident Post-Mortem Review**

**Key Participants & Roles**
*   **Zaw Myo Htet:** Meeting initiator; owner of the discussion thread.
*   **Nicholas Tan:** Initial attendee, unavailable for live meeting.
*   **Kyle Nguyen:** Active participant joining to support the session.
*   **Maou Sheng Lee:** Cited as a potential replacement for Nicholas Tan.
*   **Gopi:** Cited as a potential replacement for Nicholas Tan.

**Main Topic**
Review of Postmortem document **[300126 - P1 - Some customers charged full price]** (dated March 26, 2026). The incident involves a P1 severity issue where specific customers were incorrectly charged full pricing.

**Pending Actions & Ownership**
*   **Request for Additional Attendees:** Zaw Myo Htet requested representation from the RE (Requirements/Engineering) team to join the discussion at L11 Macchiato. **Owner:** Zaw Myo Htet / Organizers.
*   **Meeting Attendance Substitution:** Nicholas Tan delegated attendance to Maou Sheng Lee or Gopi due to conflicting priorities. **Owner:** Nicholas Tan (to confirm).

**Decisions Made**
*   No formal decisions regarding the root cause or resolution were recorded in this chat snippet; the session is currently in the coordination phase for attendees.

**Key Dates & Follow-ups**
*   **Date of Incident/Post-Mortem:** March 26, 2026.
*   **Meeting Time:** Approximately 07:03 UTC (March 26).
*   **Document Access:** Postmortem file shared at 07:11:32 UTC via Google Docs link: `https://docs.google.com/document/d/16aLYguYuUjoHHHd_UYVllHewHBtuejGgjH-ZiH0D3l8/edit?usp=sharing`.
*   **Next Steps:** Participants are expected to review the linked document prior to or during the meeting. Kyle Nguyen explicitly requested the file be shared (which was done).

**Summary Note**
The conversation focuses on logistical coordination for a post-incident review of a critical pricing error. While Nicholas Tan could not attend, Kyle Nguyen confirmed participation, and the necessary documentation has been distributed to the group. Awaiting confirmation of RE team attendance.


## [41/85] Backend Chapter
Source: gchat | Group: space/AAAAHhDyHI4/nKDrYLSLrhA | Last Activity: 2026-03-26T06:33:30.786000+00:00 | Last Updated: 2026-03-26T10:55:37.850722+00:00
**Daily Work Briefing: Backend Chapter Security Alert**

**Key Participants & Roles**
*   **Nicholas Tan:** Initiator/Security Lead. Issuing the security directive.
*   **Jazz Tong:** Team Member. Seeking clarification on verification commands.
*   **Michael Bui:** Team Member/Homelab User. Confirming status of local usage.

**Main Topic**
A critical security advisory regarding a compromised `trivy` CLI vulnerability (version v0.69.4) which impacts the `litellm` tool. The discussion focuses on immediate remediation steps and clarifying safety protocols for existing installations.

**Pending Actions & Ownership**
*   **Action:** Check local machine for `trivy` CLI installation using the command `whereis trivy`.
    *   **Owner:** All Backend Chapter team members (specifically prompted by Nicholas Tan).
*   **Action:** Verify `trivy` version via `trivy --version`.
    *   **Owner:** All Backend Chapter team members.
*   **Action:** Immediately remove `trivy` if version v0.69.4 is detected.
    *   **Owner:** Any user identified with the specific vulnerable version.
*   **Action:** Do **not** upgrade `litellm`. Maintain current pinned versions to avoid triggering the scanner vulnerability.
    *   **Owner:** All users running `litellm`.

**Decisions Made**
*   **Version Constraint:** Users must strictly avoid upgrading `litellm` due to its scanning by the compromised `trivy` instance.
*   **Remediation Threshold:** Removal of `trivy` is mandatory only if the specific version v0.69.4 is found; pinned versions (e.g., Michael Bui's v1.81.3) are considered safe and require no action.

**Key Dates & Follow-ups**
*   **Date:** March 26, 2026
*   **Time:** Alerts issued between 05:59 UTC and 06:33 UTC.
*   **Follow-up:** Immediate execution of version checks and removal procedures is requested ("soonest").

**Specific References**
*   **Tool:** `trivy` CLI (vulnerable at v0.69.4).
*   **Affected Tool:** `litellm`.
*   **Safe Configuration Note:** Michael Bui confirmed safety with `litellm` pinned to version 1.81.3.


## [42/85] Project Light: Mobilization and Planning Workshop Day 1 - Mar 24
Source: gchat | Group: space/AAQAA8d_pfI | Last Activity: 2026-03-26T06:29:23.835000+00:00 | Last Updated: 2026-03-26T10:56:05.605221+00:00
**Daily Work Briefing: Project Light – Mobilization & Planning Workshop (Day 1)**
**Date:** March 24, 2026 (Session concluded; new insights added Mar 26)
**Resource Link:** https://chat.google.com/space/AAQAA8d_pfI

**Key Participants & Roles**
*   **Jacob Yeo:** Meeting facilitator.
*   **Vivian Lim Yu Qian:** Presenter/UI Walkthrough; defined technical/action items.
*   **Tiong Siong Tee:** UX Lead; proposed agenda flow and requested Figma access.
*   **Cecilia Koo Hai Ling:** Design/UX Contributor; shared DoorDash, NTUC FairPrice, Lazada references; clarified SKU logic; provided RedMart video analysis; posted new campaign link.
*   **Christine Yap Ee Ling:** Internal Liaison; handling Figma link distribution.
*   **Rajesh Dobariya:** Stakeholder; reviewed delivery categorization references.
*   **Sophia Liao & Rock Shi:** Identified as audience for Cecilia's latest Flash Deal observations.

**Main Topic & Discussion Updates**
The team conducted a high-level UX walkthrough, significantly expanding reference analysis to include RedMart's current "mega campaign" (running for 2 days) and Lazada app mechanics:
*   **Voucher Logic Update:** Cecilia Koo Hai Ling shared a specific Lazada campaign link (`https://s.lazada.sg/s.3jBSs`), noting that **vouchers are tied to the campaign only**. This clarifies previous assumptions about standalone voucher usage.
    *   *Engagement:* The new link was viewed by 15 of 23 participants.
*   **RedMart Campaign Analysis:** Cecilia also shared a video demo (`Video_20260326_094235_087_1.mp4`, viewed by 13 of 23) reviewing critical components:
    1.  **Flash Deal Mechanics:** Clickable sections direct users back to the dedicated flash deal landing page.
    2.  **Label System:** RedMart displays multiple scrollable labels, including unclaimed vouchers.
    3.  Voucher center structure and gamification mechanics.
    4.  Promo mechanisms (claim, apply, stack, and nudge toward next tiers).
    5.  Social sharing features.
    6.  "Store-in-store" concepts (default views, dedicated flash deals, seller vouchers).
    7.  User journey flow: Homepage → Category → Search → Campaign → General Merchandise.
*   **Lazada & FairPrice References:** Reviewed DoorDash's first-time app open and NTUC FairPrice examples (SharkNinja Official Store, FP Unilever Tag). The Lazada "promo label" (dynamic seller section) and gamified "Help me click" mechanic were accepted as engagement drivers.
*   **Navigation & Filters:** Clarification remains needed on whether category page filters should be pre-configured ("dynamic") or retrieved dynamically.
*   **UI Clarity:** The toggle selection between "Scheduled" and "Quick" modes requires improved visual definition.
*   **Compliance:** Discussed potential separation of eGift cards from vouchers to meet compliance requirements.
*   **SKU Logic:** Clarified that when any SKU is clicked, it is displayed as the primary SKU in Slot 1.

**Decisions Made**
*   **Reference Alignment:** Agreed that DoorDash's categorization and Lazada/RedMart campaign mechanics (voucher stacking, gamification, store-in-store) are valid benchmarks for Project Light integration.
*   **Voucher Constraint:** Confirmed the finding that vouchers in the target reference campaigns are strictly tied to the specific campaign context.
*   **Specific Feature Validation:** Confirmed RedMart's clickable flash deal section behavior and scrollable label system as key UX patterns to analyze.
*   **Filter Logic:** No final consensus on filter behavior; pending technical solution discussion led by Vivian.
*   **Slot 1 Behavior:** Clarified that the clicked SKU populates Slot 1, establishing a baseline interaction pattern.

**Pending Actions & Owners**
1.  **Share Figma Link:** Christine Yap Ee Ling to send via separate internal chat (requested by Tiong Siong Tee).
2.  **Resolve Filter Logic:** Vivian Lim Yu Qian and the technical team to finalize category page filter behavior.
3.  **Refine UI Toggle:** Design team to address visual clarity for "Scheduled/Quick" toggle selection.
4.  **Compliance Review:** Determine if eGift cards must be standalone from vouchers given the new insight on campaign-tied vouchers.
5.  **Deep-Dive Analysis:** UX Lead (Tiong Siong Tee) to analyze RedMart's specific mechanics: clickable flash deal navigation, scrollable label system, voucher center, gamification logic, and store-in-store flows for Project Light integration.

**Key Dates & Follow-ups**
*   **Event:** Project Light Mobilization and Planning Workshop Day 1 (March 24, 2026).
*   **Status:** Session concluded; RedMart campaign materials and video shared via chat on March 26. New Lazada link (`s.3jBSs`) posted Mar 26.
*   **Next Step:** Internal distribution of Figma link by Christine Yap Ee Ling; UX team to evaluate RedMart's "mega campaign" mechanics for potential application in Project Light mega campaigns.


## [43/85] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/9UYvfToHPUM | Last Activity: 2026-03-26T05:55:01.238000+00:00 | Last Updated: 2026-03-26T10:56:16.131954+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Michael Bui:** Identified as the source of clarification regarding resource ownership.
*   **Daryl Ng:** Active participant seeking validation or confirmation on organizational structure; acknowledged the correction.
*   **Miguel:** Referenced as the current owner/responsible party for the "Leads" resource.

**Main Topic/Discussion**
The conversation focused on clarifying the organizational ownership and COE (Center of Excellence) alignment for the **"Leads"** resource within the Ecom/Omni Digital Product Development space. Specifically, participants debated whether the **Store Network** falls under the **Data COE** or if it remains under Miguel's purview.

**Decisions Made**
*   It was established that the specific "Leads" resource is currently **under Miguel**.
*   A counter-point was raised questioning if "store network" belongs to the Data COE, but no final structural change was confirmed in this thread; rather, a correction regarding the current owner (Miguel) was accepted.

**Pending Actions & Ownership**
*   **Clarification on Store Network Alignment:** The question of whether "Store Network" is technically under the **Data COE** remains an open point of inquiry raised by Michael Bui. No specific action item or deadline has been assigned yet in this chat log to resolve this structural query.

**Key Dates & Follow-ups**
*   **Conversation Date:** March 26, 2026 (UTC timestamps: 05:54 – 05:55).
*   **Next Steps:** Immediate follow-up required if the Data COE alignment for "Store Network" impacts current project resourcing.

**Contextual References**
*   **Space URL:** https://chat.google.com/space/AAQAN8mDauE
*   **Resource Name:** Leads (Ecom/Omni) Digital Product Development
*   **Total Messages:** 2


## [44/85] Data Tracking Working Group
Source: gchat | Group: space/AAAAkdI3Ijg | Last Activity: 2026-03-26T05:23:56.548000+00:00 | Last Updated: 2026-03-26T10:56:52.152320+00:00
**Daily Work Briefing: Data Tracking Working Group**

**1. Key Participants & Roles**
*   **Quan To Van:** Initiator of the communication thread; likely acting as a point of contact for segment-related inquiries.
*   **Nikhil Grover:** Active participant in the discussion (last reply mentioned).
*   **Patty Yuan:** Active participant in the discussion (last reply mentioned).
*   *Note:* The thread indicates 24 replies from other unnamed participants not listed in the provided summary snippet.

**2. Main Topic/Discussion**
The core subject of the conversation is establishing a communication channel for **"segment related request or question."** Quan To Van directed team members to utilize this specific Google Chat space/thread as the primary destination for such inquiries, implying a need to consolidate segment-related data tracking issues into one forum.

**3. Pending Actions & Ownership**
*   **Action:** Reach out via the designated channel (Google Chat space) for any new or existing segment-related requests.
*   **Ownership:** All team members requiring clarification on segments are responsible for directing questions here. Specific follow-up actions by Nikhil Grover and Patty Yuan regarding this directive were noted in the 24-reply thread but specific task assignments beyond "replying" are not detailed in the provided snippet.

**4. Decisions Made**
*   **Decision:** The Google Chat space (Resource: Data Tracking Working Group) has been designated as the official hub for handling segment-related questions. No alternative channels were mentioned; this thread is now the sole reference point for these topics.

**5. Key Dates, Deadlines, & Follow-ups**
*   **Date of Message:** March 26, 2026 (05:23:56 UTC).
*   **Last Activity:** Approximately 5 minutes ago relative to the briefing time.
*   **Thread Status:** High engagement with 24 unread replies at the time of notification.
*   **Next Steps:** Review the full thread history (available via URL) to identify specific resolutions or outstanding questions from Nikhil Grover, Patty Yuan, and other contributors before proceeding with segment tasks.

**Link to Full Context:** https://chat.google.com/space/AAAAkdI3Ijg


## [45/85] ❗ Important Email
Source: gchat | Group: space/AAQAUJW8HMo | Last Activity: 2026-03-26T05:08:22.340000+00:00 | Last Updated: 2026-03-26T10:57:52.628394+00:00
**Daily Work Briefing Summary (Updated)**

**Key Participants & Roles**
*   **Michael Bui (You):** Managing Osmos support, event RSVPs, FileVault compliance, performance feedback, Project Light coordination, and AI training follow-ups.
*   **Sip Khoon Tan (FPG AICOE) / Google AI Specialists:** Leading weekly Workbench Agentic AI sessions.
*   **Daryl Ng:** Declined "ACNxOsmos: Daily Cadence"; Organizer of new BCRS Regroup meeting; Key attendee for RMN discussion.
*   **Prajney Sribhashyam:** Lead for BCRS Refunds Warroom and organizer of "BCRS Regroup - Open Item Planning."
*   **Miguel Ho Xian Da (FairPrice):** Lead for OSMOS integration.
*   **Jazz Tong:** Head of Platform Engineering; on leave until Mar 23, 2026.
*   **Tong A. Yu / Lilibeth Villena (Accenture):** Proposing working sessions for integration architecture.

**Main Topics**
1.  **AI Training & Workbench Follow-up:**
    *   Weekly 30-min virtual support on building agents in Workbench (Gemini Enterprise).
    *   **Schedule:** Wednesdays, 2:00 PM – 2:30 PM SGT (Mar 25 – May 31, 2026).
    *   **Action:** RSVP required; submit questions via form prior to sessions.

2.  **BCRS - Refunds Issue Warroom & Regroup Updates:**
    *   **Warroom:** Scheduled for Thursday, March 19, 2026, 3:30 PM – 4:30 PM SGT. *Conflict with Project Light remains.*
    *   **New Meeting (Today):** "BCRS Regroup - Open Item Planning" scheduled for **Thursday, March 26, 2026, from 4:00 PM to 5:00 PM SGT**.
    *   **Organizer:** Prajney Sribhashyam.
    *   **Attendees:** Michael Bui (Required), Sathya Murthy Karthik (Required), Daryl Ng (Required), Akash Gupta (Required); Koklin Gan (Optional).

3.  **Project Light & RMN Integration:**
    *   **RMN Discussion:** Rescheduled for Thursday, March 26, 2026, from 2:00 PM – 3:00 PM SGT.
        *   *Attendees:* Michael Bui (Required), Rajiv Kumar Singh (Required), Bryan Choong (Optional).
    *   **Project Light:** Rescheduled to Mar 19, 4:00–5:00 PM SGT. *Conflict with BCRS Warroom remains.*

4.  **ACNxOsmos Daily Cadence Update:**
    *   Daryl Ng declined the Monday, March 30, 2026 (12:30 PM – 1:00 PM SGT) invitation due to reservist duty.

5.  **D&T Power Breakfast Planning:**
    *   New event by Trina Boquiren. Planning meeting: Tuesday, March 31, 2026, 1:30 PM – 2:00 PM SGT.

**Pending Actions & Ownership**
*   **BCRS Regroup RSVP (Michael Bui):** **Immediate Action Required.** Respond to the invitation for today (March 26), 4:00–5:00 PM SGT.
*   **AI Training RSVP:** Submit "Yes" to the weekly session series starting March 25; submit questions via form.
*   **RMN Meeting RSVP:** Confirm attendance for March 26, 2:00–3:00 PM SGT. *Note: This overlaps with your immediate requirement to join BCRS Regroup (4:00 PM).*
*   **Project Light/Warroom Conflict:** Resolve scheduling conflict between Project Light (Mar 19) and BCRS Warroom (Mar 19). Reply "Yes" to both or delegate.
*   **Performance Meeting RSVP:** Confirm attendance for Mar 18, 4:00 PM SGT.
*   **D&T Breakfast Planning RSVP:** Respond to Trina Boquiren's invitation for March 31.
*   **OSMOS Architecture:** Provide architectural details on SmartCarts and IPOS to finalize long-term integration strategy with Accenture.

**Decisions Made**
*   **RMN Integration Timeline:** Team agreed to prioritize a focused working session on March 26 for architecture definition after previous slots failed due to conflicts.
*   **OSMOS Capability:** Confirmed feasible short-term integration (video via CDN, image via FPG service); long-term decision pending Accenture recommendation.

**Critical Dates & Deadlines**
*   **Mar 18, 2026:** Performance Feedback Meeting.
*   **Mar 19, 2026:** BCRS Warroom (3:30 PM) & Project Light (4:00 PM). *Conflict.*
*   **Mar 25–May 31, 2026:** Weekly AI Workbench Sessions.
*   **Mar 26, 2026 (Today):**
    *   RMN Discussion with Accenture (2:00–3:00 PM SGT). Link: `https://meet.google.com/koe-uzer-xbd`.
    *   BCRS Regroup - Open Item Planning (4:00–5:00 PM SGT). Organizer: Prajney Sribhashyam.
*   **Mar 30, 2026:** ACNxOsmos Daily Cadence (Daryl Ng declined).
*   **Mar 31, 2026:** D&T Power Breakfast Planning Session; FileVault Final Deadline.


## [46/85] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/nO81EVARv7I | Last Activity: 2026-03-26T04:42:23.981000+00:00 | Last Updated: 2026-03-26T10:58:30.957470+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Dany Jacob:** Requestor; seeking expertise on BCRS item refunds (Scan n Go/Preorder) and API enhancements.
*   **Prajney Sribhashyam:** Technical Lead; clarifying SAP/Finance constraints regarding refund posting methods and coordinating alignment between DPD, SAP, and Finance teams.
*   **Akash Gupta:** Developer/Stakeholder; advocating for RPA-based flows based on prior agreements (Feb 16) and providing historical context/tickets.
*   **Daryl Ng:** Stakeholder; seeking clarification on specific Finance/SAP feedback regarding the current posting method.
*   **Wai Ching Chan, Amirul Amri, Gopalakrishna Dhulipati, Alvin Choo:** CC'd/involved parties.

**Main Topic**
Resolution of a discrepancy regarding refund posting for Scan n Go (SnG) and preorder items involving container deposits. The core conflict is between the existing **RPA email flow** (proposed by Akash/Dany) and the **SAP Finance requirement** that refund posting must route through **Data8** to ensure accurate Cost Centre (CC) and Profit Centre allocation.

**Decisions & Clarifications**
*   **Current State:** SAP/Finance feedback indicates the current RPA email flow for *posting* refunds is inaccurate regarding financial accounts, though it works for the initial payment reversal/refund trigger.
*   **Required Path:** Deposit refund posting must align with the SnG sales/deposit/posting flow via **Data8**. Data8 already has pre-configured accounts, whereas RPA requires complex manual configuration of CCs and Profit Centres.
*   **Historical Context (Akash):** An OMS enhancement was delivered to UAT on Feb 16, aligned with Finance and CC at that time. Prajney clarifies that while the email flow for refunds is accepted, the *posting* mechanism was never successfully validated via RPA until now.
*   **Action Required:** Teams must either justify why the current approach works or proceed with enhancing Data8 posting to include refund data.

**Pending Actions & Ownership**
*   **Estimate Creation:** Dany Jacob and Wai Ching Chan are requested (by Prajney) to provide a rough estimate for enhancing the `GET` API endpoint (and subsequent Data8 integration) to include container deposit information for refunds.
    *   *Ticket Reference:* DPD-529 (https://ntuclink.atlassian.net/browse/DPD-529).
*   **Documentation:** Akash Gupta shared a Google Sheet and ticket link regarding the RPA flow; further alignment on the Data8 enhancement is pending.

**Key Dates & References**
*   **Current Date:** March 26, 2026 (Conversation timestamped early morning UTC).
*   **Previous Milestone:** February 16, 2026 – OMS enhancement delivered to UAT; alignment with Finance/CC achieved.
*   **API Endpoint:** `https://api.zs-uat.fairprice.com.sg/order-service/order/{id}/returns` (Requesting container deposit inclusion).
*   **Documentation Links:**
    *   Google Sheet: `14tjv37bLbBBvVTJeE_qxkMSQ2h-ltXPbOpktaAilJww`
    *   Jira Ticket: DPD-529


## [47/85] QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs | Last Activity: 2026-03-26T04:29:47.058000+00:00 | Last Updated: 2026-03-26T10:59:13.167688+00:00
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
*   **Others:** Piraba Nagkeeran, Andin Eswarlal Rajesh.

**Main Topics & Discussion**
1.  **Express Cart Service Fee Waiver (New):** On **26 Mar**, Milind Badame reported that for the Express cart, service fees are being incorrectly waived off with a subtotal of $37.87. *Status:* Open/Investigating. *Owners:* @Daryl Ng, @Andin Eswarlal Rajesh (7 replies, last reply 8:59 AM).
2.  **OmniHome Christmas Tiles Anomaly:** Milind Badame reported seeing "dressed up" Christmas tiles for FoodTakeaway on OmniHome despite the date being March. *Status:* Investigating visual consistency; 3 replies, last reply 3:13 AM.
3.  **PreOrder Tile Permanency (New):** On **25 Mar** at 06:55 UTC, Milind Badame flagged a new PreOrder tile in OmniHome and queried @Daryl Ng regarding its permanence to determine if E2E tests need updating as an entry point. *Status:* Awaiting clarification from Dev/Product.
4.  **LinkPay Receipt Banner Missing:** Observed on Android that the banner is missing in LinkPay receipts. Investigation requested with @Tiong Siong Tee. *Status:* New/Open (5 replies, last reply 4:45 AM).
5.  **Search Indexing Failure:** Madhuri Nalamothu reported a critical search failure where "Ninben Tsuyu No Moto Seasoning Soy Sauce - Triple Strength" is available with stock in the back office for store Hyper Changi but returns "We couldn't find anything that matches your search" when queried. *Status:* Urgent investigation needed. *Owners:* @Daryl Ng, @Yangyu Wang (21 replies).
6.  **E-Voucher Application Error:** Milind Badame reported a `404 Invalid voucher` error. Backend response indicates logic failure. *Status:* Open/Investigating with @Zaw Myo Htet.
7.  **LinkPoints Test Failure:** Tests remain disabled in regression; awaiting ETA on resolution from Dev Team (Michael Bui). *Status:* Blocked.
8.  **Postal Code Offer Label Missing:** Missing `label` attribute for the first product in "TestHasOffer swimlane" for Postal code **098619**.
9.  **QC Food Tile Removal Testing:** Daryl Ng confirmed testing is underway on the removal of QC (O2O) food tiles on the Omni home page.
10. **Load Testing & Environment Stability:** Small-scale load test completed on **5 Mar, 11 AM–1 PM** (UAT LEAP env). Scale-down operations executed successfully.
11. **DC Membership Logic Discrepancy:** Critical inconsistency where users have `DC member` flags in back office but lack active plans/UI awards. Investigation ongoing.
12. **E2E Test Failures & UI Defects:**
    *   **Cart Page (Critical):** Komal Ashokkumar Jain reported a flaw where switching from Standard to Express delivery causes cart items to "stick," allowing orders with ineligible items for 1HD. Referenced by @Daryl Ng and @Andin Eswarlal Rajesh.
    *   **General UI:** Broken alignment on the third highlighted product; unidentified "view buttons"; iOS navigation issues persist (disappearing swimlanes, EVoucher errors, Express delivery label changes).
13. **Android OTP Blank Screen:** Milind Badame reported a blank screen issue for OTP on Android versions v12 and below. Investigation requested with @Tiong Siong Tee.

**Pending Actions & Ownership**
*   **Express Cart Service Fee:** Verify why service fees are waived in Express cart mode (Subtotal $37.87). *Owners: @Daryl Ng, @Andin Eswarlal Rajesh.* (New High Priority).
*   **PreOrder Tile Strategy:** Confirm if PreOrder tile is permanent to decide on E2E test updates. *Owner: @Daryl Ng / QA Team.*
*   **OmniHome Tile Anomaly:** Verify why Christmas tiles are visible in March. *Owner: QA Team / Dev.*
*   **LinkPay Receipt Banner:** Fix missing banner on Android receipts. *Owner: @Tiong Siong Tee.*
*   **Search Indexing Failure:** Resolve search failure for "Ninben Tsuyu No Moto Seasoning Soy Sauce - Triple Strength" at Hyper Changi. *Owners: @Daryl Ng, @Yangyu Wang.* (High Priority).
*   **E-Voucher Bug:** Investigate `404 Invalid voucher` error. *Owner: Milind Badame / @Zaw Myo Htet.*
*   **LinkPoints Fix Status:** Provide ETA for the LinkPoints fix. *Owner: Dev Team / Michael Bui.*
*   **Cart Express Delivery Logic:** Resolve Cart alignment, view buttons, and delivery mode eligibility logic. *Owners: Komal Ashokkumar Jain, Daryl Ng, Andin Eswarlal Rajesh.*
*   **Postal Code Label Debug:** Investigate missing `label` for Postal code 098619. *Owner: Milind Badame / Dev Team.*
*   **Android OTP Blank Screen:** Investigate blank screen for Android v12 and lower. *Owner: @Tiong Siong Tee / Milind Badame.*

**Decisions Made**
*   Ad slot changes proceed; known test impacts acknowledged.
*   No decision yet on LinkPoints fix, Cart view buttons, Express delivery eligibility logic, E-Voucher application failure, Android OTP blank screen, Search indexing, tile anomalies, the new PreOrder tile permanency, or the Express cart service fee waiver; awaiting dev clarification and investigation results.

**Key Dates & Deadlines**
*   **5 Mar:** Load testing window (completed).
*   **16 Mar:** DC membership logic discrepancy logged.
*   **17 Mar:** UI defects reported on cart page (06:23–06:33 AM).
*   **18 Mar:** LinkPoints fix ETA required; Postal code 098619 issue flagged.
*   **20 Mar:** Critical Express delivery bug flagged by Komal Ashokkumar Jain at 11:05 UTC.
*   **24 Mar:** E-Voucher error reported by Milind Badame (02:39 UTC); Android OTP blank screen issue raised (08:05 UTC).
*   **25 Mar:** New issues flagged regarding OmniHome tiles, LinkPay receipts, Search indexing, and PreOrder tile permanency.
*   **26 Mar:** Express cart service fee discrepancy reported by Milind Badame at 04:29 AM; discussion active until 8:59 AM.


## [48/85] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/h-WUXwPta8M | Last Activity: 2026-03-26T03:05:37.451000+00:00 | Last Updated: 2026-03-26T10:59:54.289976+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**
**Source:** Google Chat Space (13 messages) | **Date:** March 26, 2026

### Key Participants & Roles
*   **Daryl Ng:** Raises architectural queries regarding data indexing; confirms understanding of new governance updates.
*   **Michael Bui:** Initially suggests DSP handles Algolia integration; seeks clarification on system boundaries.
*   **Alvin Choo:** Corrects architecture scope (B2C backend, not DSP) and defines initial governance protocols.
*   **Gopalakrishna Dhulipati:** Provides context on the Distributed Service Platform (DSP); confirms EA design principles and clarifies project-level approval requirements.

### Main Topic/Discussion
The team discussed technical ownership of **Algolia data indexing** within the B2C ecosystem, clarified architectural distinctions between the core commerce engine (DSP) and channel-specific backends, and refined governance protocols regarding system unification.
*   **Clarification:** Algolia integration is specific to the **B2C backend**, not DSP. Each channel (B2C, B2B, POS) utilizes its own Frontend and Backend.
*   **Design Principle Update:** Gopalakrishna confirmed that while high-level design principles are approved by Enterprise Architecture (EA), specific implementation details for each backend require approval on a **per-project basis**.
*   **Unification Constraints:** Due to per-channel ownership (e.g., distinct Cart & Checkout systems for POS vs. Omni app), a unified cart cannot exist across channels without explicit EA intervention. Building a unified cart requires returning to EA for approval.

### Decisions Made
*   **Ownership Confirmed:** The **B2C backend** manages indexing of data to Algolia, not the DSP.
*   **Governance Rule (General):** Any changes affecting upstream and downstream systems require **KDD sign-off**.
*   **Project-Specific Governance:** Specific architectural implementations within each backend require approval for each individual project.
*   **Unification Protocol:** Creating a unified cart across POS and Omni app requires direct engagement with and approval from **EA**.

### Pending Actions & Owners
| Action Item | Owner/Responsible | Context |
| :--- | :--- | :--- |
| Provide a single "Source of Truth" architecture diagram (noting current diagrams may be outdated). | **Enterprise Architecture (EA)** | Requested by Gopalakrishna Dhulipati. |
| Discuss and finalize the data schema to support searching for vouchers, brands, etc., beyond just products. | **Daryl Ng** / Team | Identified as a prerequisite for Algolia functionality. |
| Re-engage EA if unified cart development is required across POS and Omni channels. | **Project Team** | Per new constraint: cannot have unified cart without EA approval. |

### Key Dates & Follow-ups
*   **March 26, 2026:** Conversation took place between 01:55 and 03:05 UTC.
*   **Immediate Follow-up:** EA to share the updated architectural diagram.
*   **Next Step:** Schedule a discussion on data schema expansion (Daryl Ng).

**Reference URL:** https://chat.google.com/space/AAQAsFyLso4


## [49/85] Nikhil, Soumya, Andin Eswarlal
Source: gchat | Group: space/AAQAw0jsPYU | Last Activity: 2026-03-26T02:44:38.290000+00:00 | Last Updated: 2026-03-26T11:00:12.720075+00:00
**Daily Work Briefing: Data Impact Fix & Release Plan**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator; verifying data impact, coordinating backfill strategy, and finalizing the release plan.
*   **Soumya Singh:** Engineering Lead; providing status on the fix timeline and confirming technical impact details.
*   **Andin Eswarlal Rajesh (Rajesh):** Engineering Resource; aligned with Soumya regarding the target build date.
*   **Michael Bui:** CC'd for informational purposes.

**Main Topic**
Discussion regarding a critical data root cause fix, specifically addressing the impact of turning off the "IAB FF" feature flag on banner view and click event metrics, and determining the timeline for the next release.

**Decisions Made**
1.  **Fix Prioritization:** The team agreed to prioritize the fix due to its data impact.
2.  **Target Build Date:** The fix is targeted for Friday's build. Rajesh has confirmed alignment with this schedule.
3.  **Technical Impact Confirmation:** It was confirmed that while turning off the IAB FF may affect screen names for banner view and click events, the total count of impressions (banner view events) will be correctly recorded once the flag is disabled on affected versions.
4.  **Release Strategy:** If no backfill data can be secured from the Data Engineering (DE) team, the team will proceed with a "timer release" instead.

**Pending Actions & Ownership**
*   **Backfill Verification:** Nikhil Grover to quickly check with the Data Engineering (DE) team regarding potential backfill options for the affected period. If DE cannot assist, the timer release plan proceeds.
    *   *Owner:* Nikhil Grover
*   **Build Execution:** Execute the fix in Friday's build.
    *   *Owner:* Soumya Singh / Andin Eswarlal Rajesh

**Key Dates & Deadlines**
*   **2026-03-26 (Current Date):** Discussion took place early morning (UTC).
*   **Friday, 2026-03-27:** Target date for the build containing the fix.
*   **Tomorrow's Release:** Nikhil referenced a "tomorrow's release" in his final message; however, Soumya explicitly stated the target is Friday's build. This discrepancy should be clarified if "tomorrow" refers to Saturday or if the timeline shifted. (Note: The chat log states "targetting this Friday's build" and Nikhil later says "ready for tomorrow's release," implying Friday is the immediate next day relative to the conversation timestamp).

**Summary of Discussion Flow**
Nikhil Grover requested prioritization of a fix requiring one day of work, asked about backfill resources, and sought confirmation on data impact. Soumya Singh confirmed the timeline (Friday build), admitted uncertainty regarding backfill sources, and validated Nikhil's understanding of the IAB FF flag impact. Nikhil concluded by deciding to consult DE for backfill support immediately but authorized proceeding with a timer release if that fails.


## [50/85] Vivian Lim Yu Qian
Source: gchat | Group: dm/k9UsaIAAAAE | Last Activity: 2026-03-26T02:26:26.730000+00:00 | Last Updated: 2026-03-26T02:37:46.276536+00:00
**Daily Work Briefing: Google Chat Summary**

**Key Participants & Roles**
*   **Michael Bui:** Proposer of user experience issue; likely Product Manager or Stakeholder.
*   **Vivian Lim Yu Qian (Resource):** Technical lead or implementer responding to the inquiry.
*   **Ravi:** Third-party mentioned by Michael Bui as part of a prior discussion.

**Main Topic**
Discussion regarding the user experience (UX) potential for confusion on the **search banner** feature, specifically concerning ambiguous keywords like **"Apple."** The core concern is ensuring visual consistency between the banner imagery and the subsequent product list results.

**Pending Actions & Ownership**
*   **Action:** Clarify which specific technical component or module within the search interface Michael Bui is referring to regarding the "search banner" discrepancy.
*   **Owner:** Vivian Lim Yu Qian (to clarify scope) / Michael Bui (to provide further details once identified).

**Decisions Made**
No final decisions were reached in this conversation thread. The exchange consists of an issue report followed by a clarification request.

**Key Dates & Follow-ups**
*   **Date:** March 26, 2026.
*   **Follow-up Required:** Michael Bui must specify the exact UI component (e.g., banner logic, filtering algorithm, or rendering layer) to proceed with addressing the "Apple" keyword confusion scenario (where banners show phones but lists show fruit).

**Detailed Context**
Michael Bui reported a discussion with Ravi highlighting a UX inconsistency. When users search for ambiguous terms like "Apple," the current implementation may display a banner featuring "Apple phones" while the product list below displays only fruits, causing customer confusion. Vivian Lim Yu Qian responded by requesting clarification on which specific component of the search banner system is being referenced to facilitate further investigation.


## [51/85] [Prod Support] Offers
Source: gchat | Group: space/AAAAzZ3qkNU | Last Activity: 2026-03-26T02:24:26.546000+00:00 | Last Updated: 2026-03-26T02:38:47.731630+00:00
**Daily Work Briefing: [Prod Support] Offers**

**Key Participants & Roles**
*   **Willie Tan:** Reported initial issue (Mar 17) with offer visibility; escalated on Mar 26 regarding promo flow failure for specific SKUs.
*   **Angela Yeo:** Previously escalated discrepancy regarding incorrect promo display for SKU 13066243.
*   **Alvin Choo:** Previously flagged urgency and assigned owners for the initial case.
*   **Zaw Myo Htet & Daryl Ng:** Previously tagged as owners; now required to investigate the new flow issue.

**Main Topic**
Investigation into production offer display errors involving two distinct but potentially related scenarios:
1.  **Historical Context (Mar 17–19):** Issues with Offer ID `sap offer 202603000112484` for **SKU 13066243**. The team confirmed "2 for $5.40" is the correct configuration, but it failed to display as expected while incorrect promotions were visible.
2.  **New Escalation (Mar 26):** Willie Tan reported that promos created in SAP are not flowing to FPON for a list of SKUs, despite these items *not* being on the promo blacklist. The specific SKUs provided were samples; a full investigation of the flow mechanism is required.

**Pending Actions & Ownership**
*   **Action 1:** Investigate why correct offers ("2 for $5.40") are not displaying or if incorrect offers are showing for historical cases (SKU 13066243).
*   **Action 2:** Investigate the root cause of promo flow failure from SAP to FPON for SKUs not on the blacklist, as reported by Willie Tan on March 26.
*   **Owners:** @Zaw Myo Htet, @Daryl Ng (assigned by Alvin Choo previously; applicable to both current issues).
*   **Status:** Active/Urgent. The scope has expanded from a single SKU display error to a systemic flow issue affecting multiple SKUs as of March 26, 02:24 AM UTC.

**Decisions Made**
No final technical fixes have been implemented yet. The team has established the expected outcome for historical cases: offers must display "2 for $5.40." For the new case, it is confirmed that SKUs in question should be eligible for promos (not blacklisted) but are failing to receive them from SAP.

**Key Dates & Deadlines**
*   **Initial Issue Reported:** March 17, 2026 (09:01 AM).
*   **Historical Escalation:** March 19, 2026 (10:04 AM and 12:35 PM).
*   **New Flow Issue Reported:** March 26, 2026 (02:24 AM UTC) by Willie Tan.
*   **Deadline:** Immediate resolution requested for both the display error and the new flow failure.

**Reference Links & IDs**
*   **Chat Space URL:** https://chat.google.com/space/AAAAzZ3qkNU
*   **Historical Offer ID:** `sap offer 202603000112484`
*   **Historical SKU:** 13066243
*   **New Case Scope:** Multiple SKUs (samples provided by Willie Tan) not under promo blacklist.
*   **System Components:** SAP (source), FPON (destination).


## [52/85] Theo Adi
Source: gchat | Group: dm/4g6tFSAAAAE | Last Activity: 2026-03-26T02:22:57.015000+00:00 | Last Updated: 2026-03-26T02:39:50.181161+00:00
**Daily Work Briefing**  
**Resource:** Theo Adi  
**Date:** March 26, 2026  
**Time Window:** 01:59 – 02:23 UTC  

**1. Key Participants & Roles**  
*   **Michael Bui:** Manager/Supervisor; currently in an important meeting.
*   **Theo Adi:** Subject resource; initiates request to discuss a "big fix."

**2. Main Topic/Discussion**  
The exchange shifts from a previous one-way data relay (March 25) regarding the identifier `NLPE-3ZEF-CWP4-LLLU-5MH3-HMAU` to an active coordination between Theo Adi and Michael Bui.
*   **Theo Adi's Request:** Initiates contact ("hi morning boss") to request Michael Bui's immediate attention to "check your big fix."
*   **Michael Bui's Response:** Confirms availability during a short break from a critical meeting.
*   **Scheduling Negotiation:** Michael Bui inquires about the duration of the check due to the importance of his current meeting. Theo Adi confirms the session will take **15 minutes**.

**3. Pending Actions & Ownership**  
*   **Action:** Conduct a 15-minute review/check of the "big fix" (potentially related to previous identifier `NLPE-3ZEF-CWP4-LLLU-5MH3-HMAU` or a separate operational issue).
*   **Owner:** Michael Bui (to perform the check) and Theo Adi (to facilitate the discussion).
*   **Status:** Scheduled. The meeting is tentatively set for the short break following 02:22 UTC, pending Michael Bui's availability.

**4. Decisions Made**  
*   **Agreed Duration:** The review session is confirmed to last approximately 15 minutes.
*   **Timing:** Meeting to occur during Michael Bui's next scheduled break from his current important meeting.

**5. Key Dates, Deadlines, & Follow-ups**  
*   **Original Message Timestamp (March 25):** 03:52 UTC (Single data transmission of `NLPE-3ZEF-CWP4-LLLU-5MH3-HMAU`).
*   **New Coordination Timestamp:** March 26, 2026.
    *   Request Initiated: 01:59:04 UTC.
    *   Meeting Break Confirmation: 01:59:49 UTC.
    *   Duration Confirmation: 02:22:57 UTC.
*   **Next Step:** Michael Bui to initiate the check during his break after 02:23 UTC.

**Summary Note**  
The interaction has evolved from a passive data handover on March 25 into an active operational request on March 26. Theo Adi requires immediate assistance from Michael Bui to review a "big fix." Despite Michael Bui being in a critical meeting, a 15-minute window for this review was successfully negotiated and confirmed by Theo Adi at 02:22 UTC. The session is pending execution during the next available break. Historical context regarding `NLPE-3ZEF-CWP4-LLLU-5MH3-HMAU` remains relevant as a potential subject of this "big fix" review, though the current conversation focuses on scheduling rather than the code itself.


## [53/85] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw | Last Activity: 2026-03-26T01:59:19.364000+00:00 | Last Updated: 2026-03-26T02:40:49.419947+00:00
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

**Main Topics & Discussions**
1.  **Infrastructure & Operations Risk:** Nicholas Tan previously flagged operational risks regarding Broadcom ending free Bitnami images, causing `kubectl` image tag failures and increased Time To Recovery (TTR). The issue impacts the Golden Pipeline (GP).
2.  **Payment Service Issues:** Alvin Choo reported promo code redemption failures in FP Pay; confirmed that a change freeze has ended and feature releases are proceeding.
3.  **Mobile Quality Assurance:** Andin Eswarlal Rajesh identified an iOS FPPay bug where QR codes load without user login, escalated via file download.
4.  **Datadog Governance:** Natalya Kosenko reported unauthorized manual changes to Datadog On-Call teams (removals of Maxine, Arijit, Minu). Terraform manages this config; manual console edits are overwritten on the next run.
5.  **Strategic Planning:** Winson Lim highlighted data centers as potential targets in modern warfare (Iran conflict context) to inform Disaster Recovery (DR) scenarios.
6.  **Product Strategy & Tooling Expansion:** On March 26, 2026, Winson Lim noted that Reforge joined Miro. This acquisition signals Miro's expansion into product strategy, aiming to close the gap between decision-making and delivery for modern product teams.
7.  **Social Events & Sentiment:** Kyle Nguyen previously announced an upcoming DPD BBQ with the sentiment "We come first." Maou Sheng Lee expressed a sentiment of feeling like energy is being wasted on March 18.
8.  **Alumni Engagement:** Natalya Kosenko noted DPD alumni participation in a Google AI event (March 25, 2026).

**Pending Actions & Owners**
*   **GP Team (Nicholas Tan / Mohit Niranwal):** Investigate Bitnami image replacement strategy to resolve TTR issues and update Golden Pipeline dependencies.
*   **iOS/Dev Team (Tiong Siong Tee / Andin Eswarlal Rajesh):** Investigate the iOS FPPay QR code login bypass bug.
*   **Datadog Admins:** Anyone who manually altered Datadog Teams must submit a Pull Request to `https://bitbucket.org/ntuclink/fp-datadog-eu` instead of editing the console to prevent configuration loss.
*   **Product Strategy Team (Winson Lim / Product Folks):** Evaluate Miro's strategic expansion and Reforge integration opportunities to optimize decision-to-delivery workflows.

**Decisions Made**
*   No formal change freeze; feature releases are currently active (Alvin Choo).
*   Datadog team configurations must strictly follow Infrastructure as Code (Terraform) protocols; manual overrides are deprecated.
*   Miro's acquisition of Reforge is recognized as a strategic move to bridge product strategy and delivery gaps.

**Key Dates & Follow-ups**
*   **Mar 3, 2026:** Project status noted as "one step behind."
*   **Mar 7, 2026:** FP Pay promo code issue raised; change freeze lifted same day.
*   **Mar 9, 2026:** BCRS discussion and Meta AI news shared.
*   **Mar 10, 2026:** iOS bug discovered.
*   **Mar 12, 2026:** "BB incident" query raised; Data center DR scenario discussed.
*   **Mar 13, 2026:** Datadog governance warning issued.
*   **Mar 17, 2026:** DPD BBQ announcement made by Kyle Nguyen; Wai Ching Chan engaged with Vincent Wei Teck Lim regarding the event (Last Reply: 12:15 PM).
*   **Mar 18, 2026:** Maou Sheng Lee noted sentiment regarding wasted energy.
*   **Mar 25, 2026:** Natalya Kosenko highlighted DPD alumni participation in a Google AI event.
*   **Mar 26, 2026:** Winson Lim shared Reforge joining Miro; potential impact on product strategy workflows identified.

**Social Notes**
*   Boning He and Gopalakrishna Dhulipati shared snacks (Chinese cookies with chicken gizzard/medicinal barley and Indian cookies) in pantry areas.
*   Upcoming DPD BBQ announced by Kyle Nguyen ("We come first, see you!").


## [54/85] [BCRS]-SAP to POS & DBP Interface Deployment
Source: gchat | Group: space/AAQAeMC3qBk/0rSvmSBcJD0 | Last Activity: 2026-03-26T01:49:57.562000+00:00 | Last Updated: 2026-03-26T02:41:37.316381+00:00
**Daily Work Briefing: [BCRS]-SAP to POS & DBP Interface Deployment**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Initiator; coordinating deployment sequence.
*   **Yangyu Wang:** Technical lead (DBP); confirmed changes deployed.
*   **Sneha Parab:** Operations liaison; managing communications to Catalog Ops & MP Ops.
*   **Daryl Ng:** Deployment lead; assessing risk regarding midnight release.
*   **Michael Bui:** Verification lead; monitoring post-deployment status.
*   **Onkar Bamane:** Release engineer; executing the deployment window.

**Main Topic**
Confirmation of deployment sequence for the [BCRS]-SAP to POS & DBP Interface update, specifically verifying that the **DBP** component proceeds before the SAP changes. The discussion focused on establishing a maintenance window where MP SKU creation is suspended to mitigate risk during the transition.

**Decisions Made**
1.  **Deployment Sequence:** Confirmed that **DBP will go first**, followed by SAP changes.
2.  **Maintenance Window:** Catalog Ops and MP Ops will be instructed not to approve any SKUs starting **10:00 PM today (March 26, 2026)** until the deployment is verified.
3.  **Risk Assessment:** Daryl Ng confirmed no known risks prevent proceeding with this schedule, contingent on Onkar's midnight release plan.

**Pending Actions & Owners**
*   **Send Operational Communications:** Sneha Parab will notify Catalog Ops and MP Ops of the 10:00 PM SKU approval freeze and the deployment window details. *Owner: Sneha Parab.*
*   **Execute Release:** Onkar Bamane to deploy changes between **00:10 AM and 01:30 AM**. *Owner: Onkar Bamane.*
*   **Monitor & Verify:** Michael Bui will observe system status post-deployment (approx. 12:00 AM – 1:00 AM) to confirm successful deployment of SAP changes and identify any issues. *Owner: Michael Bui.*

**Key Dates, Deadlines & Follow-ups**
*   **March 26, 2026 @ 10:00 PM:** Deadline for Catalog Ops/MP Ops to stop approving SKUs.
*   **March 27, 2026 @ 00:10 AM – 01:30 AM:** Scheduled deployment window.
*   **March 27, 2026 @ ~12:00 AM – 1:00 AM:** Verification period for SAP changes.

**Reference**
*   Chat URL: https://chat.google.com/space/AAQAeMC3qBk


## [55/85] BCRS Production Deployment Planning Session - Mar 25
Source: gchat | Group: space/AAQAjVLsLrE | Last Activity: 2026-03-25T04:31:31.177000+00:00 | Last Updated: 2026-03-25T06:50:18.131240+00:00
**Daily Work Briefing: BCRS Production Deployment Planning (Mar 25)**

**Key Participants & Roles**
*   **Sneha Parab:** Meeting organizer/facilitator; confirmed location (L11, Room 11) and verified SKUs.
*   **Yang Yu:** Co-organizer (present at location).
*   **Sathya Murthy Karthik:** Attendee (joined late).
*   **Sundy Yaputra:** Contributor; provided status on deployed features.
*   **Michael Bui:** Requester of API access confirmation.
*   **Onkar Bamane:** Responsible for verifying API access requests and checking ticket status.
*   **Prajney Sribhashyam:** IT Support/Ticket Owner; created the access request ticket (NED-275153).

**Main Topic**
Coordination of the BCRS Production Deployment planning session, specifically focusing on confirming room availability, verifying current production deployment status, and resolving pending API access requirements for the production environment.

**Pending Actions & Owners**
*   **Verify Access Request Status:** Onkar Bamane has acknowledged a ticket exists and is currently checking its status to confirm if API access on Production (PRD) is ready.
*   **Join Meeting:** Sathya Murthy Karthik indicated he would join at 11:10 (timezone implied as local/UTC relative to context). Sundy Yaputra noted potential inability to attend but provided updates asynchronously.

**Decisions Made**
*   No formal strategic decisions were recorded in this thread; the discussion focused on status verification and logistical coordination.
*   It was confirmed that specific components are already live: Cart, Shopping List, Wishlist, and Amplitude "order completed" events for BCRS are deployed to production.

**Key Dates & References**
*   **Meeting Date:** March 25, 2026.
*   **Location:** L11 Room 11.
*   **Ticket Reference:** NED-275153 (Jira Service Desk portal).
*   **SKU Verification Data Provided by Sneha Parab:**
    *   *Non BCRS:* SKU 13278877 / Barcode 8888030317266.
    *   *BCRS Items:* SKUs 13280984, 12714758, 12714881 with corresponding barcodes and deposit SKUs (13285192, 13285203, 13285197).
*   **Deployment Timeline:** Amplitude events deployed yesterday (March 24, 2026 context); other features currently in prod.


## [56/85] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/o4m2XO8j1K0 | Last Activity: 2026-03-25T14:17:11.526000+00:00 | Last Updated: 2026-03-25T14:37:34.545953+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Michael Bui:** Initiator of the incident report; investigating search/category page impression drops.
*   **Daryl Ng:** Platform Ops/Frontend lead; verifying deployment history, traffic metrics, and Amplitude data.
*   **Andin Eswarlal Rajesh:** Team lead (likely Segment/Omni); cross-functional investigation and root cause analysis.
*   **Nikhil:** External/Allied team contact (Campaigns/Feature Flags) assisting with data comparison.
*   **Alvin Choo:** Copied on the initial alert; no direct contribution noted in this thread.

**Main Topic**
Investigation into a significant 60–70% drop in ad impressions on Search and Category pages since March 18–19, 2026. The team is determining if recent PRD deployments or operational changes caused the discrepancy between tracked requests and reported impressions.

**Status & Findings**
*   **Symptoms:** Impressions dropped significantly starting March 18/19. Traffic to pages remained stable; Amplitude data shows no drop in category page activity.
*   **Troubleshooting Results:**
    *   No related PRD deployments occurred on the affected dates for Search/Category pages.
    *   Platform Ops disabled swimlanes on Omni & OG Home (March 18–20), but this does not affect Search/Category tracking.
    *   OSMOS confirmed no drop in ad requests; MPS service shows no drop in tracking requests.
    *   **Root Cause Hypothesis:** Michael Bui and Nikhil identified that the number of responses containing "2 or more products" significantly reduced. This reduction is likely causing the impression drop, as impressions are tracked when an ad product card appears in the viewport (IAN standards).
*   **Related Issue:** Andin Eswarlal Rajesh noted a separate banner impression drop on the Omni Home page for Segment was caused by an IAB banner fix issue (previously identified) affecting iOS only.

**Pending Actions & Owners**
1.  **Cross-check with OSMOS:** Verify if the reduced response count (2+ products) is causing the SDK to fail sending impressions. *Owner: Michael Bui.*
2.  **Platform Breakdown:** Analyze data breakdown by platform (iOS vs. others) to confirm if the issue mirrors the iOS-only Segment banner problem. *Owner: Michael Bui & Andin Eswarlal Rajesh.*
3.  **Campaign/FF Audit:** Check with Nikhil regarding any campaigns or Feature Flags turned off on March 18/19. *Owner: Andin Eswarlal Rajesh (initiated).*

**Decisions Made**
*   The issue does not stem from platform traffic drops, Ad request failures, or direct PRD deployments targeting Search/Category logic during the specific window.
*   The investigation has pivoted to data structure changes (reduced multi-product responses) rather than infrastructure outages.

**Key Dates & Follow-ups**
*   **Incident Window:** March 18–19, 2026.
*   **Follow-up Date:** Investigation to continue "tomorrow" (March 26, 2026) regarding the potential link between the Segment banner fix issue and the current Search/Category drop.
*   **Next Update:** Michael Bui provided an interim update on March 25 at 14:17 regarding the response count analysis.


## [57/85] Video & Product Ads Working Group
Source: gchat | Group: space/AAQAeSWRtgQ/RZyBk6LBi14 | Last Activity: 2026-03-25T14:09:34.340000+00:00 | Last Updated: 2026-03-25T14:37:56.987677+00:00
**Daily Work Briefing: Video & Product Ads Working Group**
*Source: Google Chat (36 messages)*
*Date Range: March 17, 2026 – March 25, 2026 (UTC)*

### **Key Participants**
*   **Michael Bui:** Raised initial technical queries on API usage and feature flags; currently attending a full-day workshop.
*   **Norman Goh:** Validated assumptions regarding UAT rank issues; confirmed deployment to production; noted he is no longer part of the omni home experience team.
*   **Nikhil Grover:** Reported initial UAT discrepancies regarding event "rank"; requested verification post-production deployment.
*   **Flora Wo Ke:** Identified root cause: analytics payload generation occurred in the backend, rendering frontend Split.IO manipulations ineffective without backend config access; clarified team ownership changes.
*   **Others Involved:** Daryl Ng, Yangyu Wang (PR reviewers); Andin Eswarlal Rajesh.

### **Main Topic**
Discussion centered on the API strategy for **vertical scrolling product ads**, which evolved into resolving an incident involving incorrect event "rank" reporting in UAT after dynamic ad slot updates. The conversation concluded with the successful deployment of the fix to production and a request for final verification.

### **Decisions Made & Technical Clarifications**
*   **API Strategy (March 17):** Confirmed that vertical scrolling uses the same endpoint as "product swimlanes" with dynamic positioning values, not hardcoded. Split.IO logic resides entirely within the `marketing-service`.
*   **Root Cause of Rank Issue (March 25):** Incorrect ranks occurred because the analytics payload is built in the backend. Frontend manipulation via Split.IO was insufficient; the backend must retrieve the Split config to recalculate positions dynamically.
*   **Fix Implementation:** Norman Goh confirmed the fix utilizes dynamic calculation logic with no hardcoded values.

### **Pending Actions & Ownership**
*   **PR Status:** Pull Request #209 for `engage-content-orchestration-go` is submitted for review and approval by Daryl Ng and Yangyu Wang (requested on March 25).
*   **Production Verification (Critical):** Norman Goh (March 25, 14:09 UTC) confirmed the fix has been deployed to the **production environment**. He formally requested Nikhil Grover to verify the deployment in production.

### **Key Dates & Follow-ups**
*   **2026-03-17:** Initial strategy meeting regarding API endpoints and Split.IO architecture.
*   **2026-03-25 01:33 UTC:** Nikhil Grover reported rank discrepancies in UAT; Michael Bui unavailable due to workshop.
*   **2026-03-25 03:56 UTC:** Flora Wo Ke clarified backend retrieval of Split config is mandatory; Norman Goh confirmed leaving the omni home team.
*   **2026-03-25 04:11 UTC:** Norman Goh confirmed the fix uses dynamic calculation logic.
*   **2026-03-25 05:28 UTC:** PR #209 submitted for review and deployment.
*   **2026-03-25T14:09:34+00:00:** Norman Goh announced the fix is deployed to production and requested verification from Nikhil Grover.

### **Status Update**
The technical root cause has been resolved, and the dynamic position fix has been successfully **deployed to the production environment**. The immediate pending action is for Nikhil Grover to verify correct rank reporting in production scenarios (both "ad applied" and "non-ad"). While PR #209 remains pending final review by Daryl Ng and Yangyu Wang, the functional deployment to production allows for live validation. Future Split.IO changes affecting ad slots require backend integration to regenerate analytics payloads correctly.


## [58/85] Google Drive
Source: gchat | Group: dm/7d1XKcAAAAE | Last Activity: 2026-03-25T14:06:37.786000+00:00 | Last Updated: 2026-03-25T14:38:32.514566+00:00
**Daily Work Briefing Summary (Updated)**

**Key Participants & Roles:**
*   **Nikhil Grover (FairPriceGroup):** Repeatedly encountering "Google Drive unable to process your request" errors when sharing ads analytics and cadence notes. Previously attempted to share "Programmatic Ads tracking events."
*   **Sujit Jha (Onlinesales.ai):** Attempted to share "Ads tracking events"; file access failed due to recipient blocking.
*   **Michael Bui (Business/Stakeholder):** Blocked Sujit Jha's document; previously flagged as a blocked user in Drive incidents.
*   **Jacob Yeo (FairPriceGroup):** Encountered Drive processing errors while sharing the "Project Light: Mobilization & Planning Workshop" deck.
*   **Tan Gay Lee (Finance):** Driving UAT financial validation requiring SAP document numbers.
*   **Hendry Tionardi (Operations/IT):** Managing technical clarifications on POS/SAP integration.

**Main Topics:**
1.  **Google Drive Processing Failures:** A persistent system-wide or permission-based issue is preventing file sharing across FairPriceGroup domains.
    *   **March 18–19:** Nikhil Grover failed to share "Programmatic Ads tracking events" and gain Editor access to "ACNxOsmos: Daily Cadence."
    *   **March 23 (16:32):** Jacob Yeo attempted to share the "Project Light: Mobilization & Planning Workshop" presentation; request failed with a Drive processing error.
    *   **March 25 (14:00–14:06):** Nikhil Grover made three consecutive attempts to share specific Product Ads Analytics files (Baby-Child-Toys and Beauty/Oral-Care categories) for dates 20260304 and 20260325. All requests failed with the same "Google Drive is unable to process your request" error.
2.  **Ads Tracking Data Sharing & Access Issues:** Continued failures in sharing tracking event documents between FairPriceGroup and Onlinesales.ai domains, compounded by system processing errors.
    *   **March 18:** Sujit Jha's share failed due to Michael Bui blocking `sujit.jha@onlinesales.ai`.

**Pending Actions & Owners:**
*   **UAT SAP Document Update:** Hendry Tionardi and the BCRS team must update Column J with valid SAP document numbers immediately. Finance cannot proceed without this data. *(Note: Original deadline was March 10; current date is now March 25, requiring urgent resolution).*
*   **Scan & Go Flow Confirmation:** Hendry Tionardi requested **Onkar Bamane** to confirm if the "Scan and Go" flow posts sales data as an aggregate invoice to SAP rather than individual receipts.
*   **Drive Infrastructure Resolution:** IT support must investigate the recurring "Google Drive unable to process your request" errors affecting Jacob Yeo, Nikhil Grover, and others across multiple document types (Project Light, Ads Analytics, Cadence notes).
*   **Ads Tracking Resolution:** Michael Bui or Nikhil Grover must resolve access permissions for tracking documents (OSMOS source) with Finance/Operations.

**Decisions Made:**
*   **RMN Incident Impact:** Confirmed there is **no financial revenue impact**.
*   **Postmortem Template:** Michael Bui confirmed that breaking down the Executive Summary follows the approved **v2 postmortem template**.

**Key Dates & Deadlines:**
*   **March 6, 2026:** Initial request for SAP document numbers issued.
*   **March 10, 2026 (Original Deadline):** Finance required SAP document numbers in BCRS UAT spreadsheet (Missed).
*   **March 18–19, 2026:** Failed attempts to share Ads tracking files and Cadence notes by Sujit Jha and Nikhil Grover.
*   **March 23, 2026 (16:32):** Jacob Yeo failed to share "Project Light" workshop deck due to Drive error.
*   **March 25, 2026 (14:00–14:06):** Multiple failures by Nikhil Grover to share Product Ads Analytics files for Baby and Beauty categories.

**References:**
*   **BCRS UAT 2026 Spreadsheet:** [Link](https://docs.google.com/spreadsheets/d/1o6oklFTFyzpT490vQ4x8IKc00vdL41pl9hUAaQgg-ns/edit)
*   **RMN Incident Report (v2 Template):** [Link](https://docs.google.com/document/d/1XiN0diQicup7ujoCWWKdD3Hvp8J0OJD5LPOfnthegyE/edit)
*   **ACNxOsmos Daily Cadence (Access Failed):** [Link](https://docs.google.com/document/d/1LWKTTxcCJxIS12EkIvJmyXFNfjHXCF5ZYu2v5Vg4r9o/edit?usp=drive-dynamite&userstoinvite=nikhil.grover@fairpricegroup.sg&role=writer&ts=69bb8e22)
*   **Project Light Presentation (Failed Share):** [Link](https://docs.google.com/presentation/d/1iRcOI4v06WBUIERjlncMpkRre7z_jUkBl1J76fuzIso/edit?usp=drive-dynamite&ts=69c16b08)
*   **Product Ads Analytics (Failed Shares):** [Baby/Toys Link](https://docs.google.com/document/d/1_LkZAkPEP5jNy1mkJDc9JzrpTG0PrDWZ8V2YVcmp2KA0/edit), [Beauty Link](https://docs.google.com/document/d/1_DirQKHwYEkq2eOyfYkt0wcNj2jg2G_lOkvxghKIAj0/edit) (Note: Actual links for March 25 files not provided in source text, but file names recorded).


## [59/85] Sneha Parab
Source: gchat | Group: dm/50uphEAAAAE | Last Activity: 2026-03-25T12:22:51.489000+00:00 | Last Updated: 2026-03-25T14:40:50.812292+00:00
**Daily Work Briefing: Google Chat Summary**
**Resource:** Sneha Parab
**Date of Conversation:** March 25, 2026 (09:34 UTC)

**Key Participants & Roles**
*   **Sneha Parab:** Initiator of the query; verified tool status.
*   **Michael Bui:** Respondent who confirmed the operational history and contract status regarding "Citrus Ad."

**Main Topic/Discussion**
The conversation focused on validating the operational status of the marketing platform **"Citrus Ad."** Sneha Parab sought confirmation that the resource was no longer in use. Michael Bui provided a definitive affirmative response, clarifying that the vendor's contract was officially terminated last May (2025).

**Pending Actions & Ownership**
*   **Action:** None currently pending. The inquiry has been fully resolved with Michael's confirmation.
*   **Status Change:** The requirement for verification is complete. No further follow-up regarding this specific query is necessary until new information arises.

**Decisions Made**
*   **Confirmation of Termination:** It was confirmed that the "Citrus Ad" contract was terminated last May, rendering the tool no longer in use as of March 25, 2026. This settles the operational status inquiry raised by Sneha Parab.

**Key Dates & Follow-ups**
*   **Inquiry Sent:** March 25, 2026, at 09:34 UTC (Sneha Parab).
*   **Confirmation Received:** March 25, 2026, at 12:22:51 UTC (Michael Bui).
*   **Historical Context:** Contract termination occurred last May.

**Summary**
On March 25, 2026, Sneha Parab initiated a check-in to verify if "Citrus Ad" was no longer in use. Michael Bui responded at 12:22 UTC the same day, confirming that their contract was terminated last May. The thread has successfully concluded with this confirmation. All pending actions regarding the status of "Citrus Ad" have been resolved; the team may proceed with any necessary resource reallocations or workflow adjustments based on the confirmed deprecation of the tool.


## [60/85] DPD AI Guild
Source: gchat | Group: space/AAQA5_B3lZQ/9rNMaZEmMZE | Last Activity: 2026-03-25T12:13:58.891000+00:00 | Last Updated: 2026-03-25T14:41:07.560589+00:00
**Daily Work Briefing: DPD AI Guild**
**Resource:** Google Chat Space (URL: https://chat.google.com/space/AAQA5_B3lZQ)
**Date Range:** March 24 – 25, 2026

**Key Participants & Roles**
*   **Nicholas Tan:** Contributor; initiated the discussion by sharing industry news.
*   **Dodla Gopi Krishna:** Participant; provided commentary on leadership implications.
*   **Tan Nhu Duong:** Participant; questioned future development strategies regarding open source.
*   **Michael Bui:** Contributor; highlighted a parallel initiative by Y Combinator CEO Garry Tan and raised the question of open-sourcing.

**Main Topic**
The discussion initially centered on *The Independent*'s report (March 24) detailing Mark Zuckerberg's deployment of an "AI CEO" at Meta, characterized by Nicholas Tan as "tokenmaxxing." The group debated operational implications, including potential leadership redundancy and the tool's future availability. On March 25, Michael Bui expanded the scope by introducing a comparable project: Garry Tan (CEO of Y Combinator) has built a similar initiative hosted at `https://github.com/garrytan/gstack`.

**Decisions Made**
No formal decisions were made during this exchange. The conversation remained speculative regarding future corporate actions by Meta and Y Combinator.

**Pending Actions & Ownership**
*   **None:** No specific action items, tasks, or ownership assignments were generated from this chat thread. However, the community remains curious about the timeline for potential open-sourcing of both the Meta and Garry Tan's respective tools.

**Key Dates & Follow-ups**
*   **March 24, 2026 (06:57:45 UTC):** Nicholas Tan shared *The Independent* article regarding Mark Zuckerberg's AI CEO.
*   **March 24, 2026 (06:59:45 – 07:12:30 UTC):** Follow-up commentary regarding Meta leadership redundancy and open-source potential.
*   **March 25, 2026 (12:13:58 UTC):** Michael Bui shared the GitHub link to Garry Tan's project (`gstack`) and queried its future open-sourcing status.

**Summary of Conversation Flow**
The discussion began on March 24 with Nicholas Tan sharing a report that Mark Zuckerberg has deployed an "AI CEO" at Meta. Dodla Gopi Krishna interpreted this as a signal that Zuckerberg might be redundant or face layoffs, while Tan Nhu Duong questioned when the technology would be open-sourced. Nicholas Tan concluded the initial thread by labeling the trend "tokenmaxxing."

The conversation continued on March 25 when Michael Bui noted that Garry Tan (CEO of Y Combinator) has built a similar tool available at `https://github.com/garrytan/gstack`. Bui echoed the previous sentiment regarding availability, asking specifically when this project would be open-sourced, reinforcing the group's interest in the transparency and accessibility of these AI leadership tools.


## [61/85] Miguel Ho Xian Da
Source: gchat | Group: dm/0pYlUwAAAAE | Last Activity: 2026-03-25T11:39:55.713000+00:00 | Last Updated: 2026-03-25T14:46:17.874621+00:00
**Daily Work Briefing**
**Source:** Google Chat (Miguel Ho Xian Da)
**Date:** March 25, 2026

**1. Key Participants & Roles**
*   **Michael Bui:** Issue reporter; identified a potential security vulnerability regarding the "MyApp" feature.
*   **Miguel Ho Xian Da:** Technical authority/Developer; confirmed system behavior and provided design rationale.

**2. Main Topic**
Discussion regarding a perceived security risk where office doors can be opened via the "MyApp" feature without requiring user authentication (login) on the device.

**3. Decisions Made**
*   **Confirmation:** The ability to open doors without logging in is an **intended design**, not a bug or security breach.
*   **Rationale Established:** Access logic mirrors physical key card functionality. Since losing a mobile phone is statistically less likely than losing a physical key card, the system prioritizes convenience and availability over mandatory re-authentication for the app.

**4. Actions Pending & Ownership**
*   **Status:** None. The matter was resolved within the conversation (Michael accepted the explanation).
*   **Next Steps:** No further action required at this time.

**5. Key Dates & References**
*   **Conversation Start:** March 25, 2026, 11:36:03 UTC
*   **Resources Referenced:** "MyApp" feature; physical key cards.
*   **Chat URL:** https://chat.google.com/dm/0pYlUwAAAAE

**Summary**
Michael Bui reported that the MyApp allows door access without login, flagging it as a potential security issue. Miguel Ho Xian Da clarified this is intentional design to ensure accessibility in case of lost physical cards, noting higher probability of card loss compared to phone loss. Michael confirmed understanding and accepted the explanation.


## [62/85] BCRS - UAT
Source: gchat | Group: space/AAQACfHCuNI | Last Activity: 2026-03-25T11:05:10.722000+00:00 | Last Updated: 2026-03-25T14:46:38.485586+00:00
**BCRS UAT Daily Briefing Summary (Updated: 25 Mar 2026)**

**Key Participants & Roles**
*   **Sathya Murthy Karthik:** UAT Lead/Coordinator (Provided status update as of 25 Mar).
*   **CS Team:** Completed testing for Returns & Refunds; currently retesting failed Scan & Go cases.
*   **Finance Team:** Reviewing test case statuses; alignment achieved except for Row 30.

**Main Topic**
Status update as of 25 Mar 2026 at 7:00 PM. MP SKU Listing and In-store Pre-order testing have concluded with sign-offs obtained. Focus has shifted to retesting failed Scan & Go cases within the Returns & Refunds module, pending final status updates from Finance.

**Pending Actions & Owners**
*   **Returns & Refunds / Scan & Go:** Failed test cases (specifically Scan & Go) are currently being retested by CS and RPA teams.
    *   *Owner:* S&G/CS Team.
*   **Finance Testing Status Update:** Alignment for failed cases is complete except for Row 30. Finance Team must update statuses for 9 failed and 8 pending cases, including the outstanding Row 30 item.
    *   *Owner:* Finance Team.

**Decisions Made & Clarifications**
*   **MP SKU Listing:** Testing concluded; sign-off officially completed (updated from "due today" to "done").
*   **In-store Pre-order:** Testing concluded; sign-off completed ahead of the scheduled 25 Mar deadline.
*   **Returns & Refunds:** Scope now includes retesting of failed Scan & Go cases following initial CS testing results.

**Status Snapshot (as of 25 Mar, 7:00 PM)**
*   **MP SKU Listing:**
    *   **Status:** Completed with Sign-off.
*   **In-store Pre-order:**
    *   **Status:** Completed with Sign-off.
*   **Returns & Refunds / Scan & Go:**
    *   **CS Testing:** 22 Passed, 0 Pending, 5 Failed (All related to Scan & Go; currently being retested).
    *   **Finance Testing:** 10 Passed, 8 Pending, 9 Failed.
        *   *Note:* Alignment for failed cases is done, pending status update on Row 30.

**Key Dates & Deadlines**
*   **25 Mar 2026 (Tue):** Current reporting time; MP SKU and In-store Pre-order sign-offs completed today.
*   **Previous:** 24 Mar 2026 (Mon).

**Historical Context**
*   **MP SKU Listing:** Previously pending sign-off on 24 Mar; now fully concluded with success.
*   **In-store Pre-order:** Previously delayed to 25 Mar due to FOC alignment issues; testing and sign-off are now complete.
*   **Returns & Refunds:** Scope expanded to include Scan & Go. Previous counts (26 Passed, 8 Failed) have been superseded by new CS data (22 Passed, 5 Failed for Scan & Go) indicating a shift in the test cycle toward retesting. Finance pending cases increased from 11 to 13 total (involving Row 30).


## [63/85] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/d1FwEozsGcU | Last Activity: 2026-03-25T10:13:21.909000+00:00 | Last Updated: 2026-03-25T10:39:57.012370+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Sathya Murthy Karthik:** Reported initial mobile crash; provided test credentials (`sng_learningjourney+3@fairprice.com.sg`) and screenshots of the refunded order.
*   **Daryl Ng:** Escalated issue to engineering/support; questioned root cause ("why is the date wrong?").
*   **Wai Ching Chan:** Investigated order details, confirmed system-wide impact (reproduced on own account #75582027), tested on Android (no issue), and coordinated physical debugging meeting.
*   **Piraba Nagkeeran:** Reproduced the crash on iOS; identified root cause as a loop iterating over zero quantity items in the API response.
*   **Andin Eswarlal Rajesh:** Reviewed refund display logic; assigned code fix responsibility to Piraba.

**Main Topic**
Troubleshooting Order #75577957, which crashes on iOS devices upon loading due to a backend data anomaly where delivered/refunded item quantities are recorded as **0**. Initial hypotheses regarding a "1 AD" date error were corrected; the crash is caused by code attempting to loop over zero items (`for _ in 0...serverCartItem.cartQuantity - 1`).

**Pending Actions & Ownership**
*   **Action:** Deploy code fix for the iOS loop crash (handling zero quantity items).
    *   **Owner:** Piraba Nagkeeran
    *   **Status:** Fixed in UAT build; pending deployment.
    *   **Reference Build:** v7.26.0 (51173) released EOD 2026-03-25, including fixes for DPD-822 and DPD-823.
*   **Action:** Verify fix on iOS device using the provided test account.
    *   **Owner:** Sathya Murthy Karthik (Tester) & Team
*   **Action:** Determine if Android requires similar handling despite currently working as expected.
    *   **Owner:** Andin Eswarlal Rajesh / Wai Ching Chan

**Decisions Made**
*   The root cause was confirmed to be the **zero quantity** field in refunded items, not a historical date error ("1 AD").
*   Android clients do not currently crash on this data (likely due to different rendering logic), but iOS requires a code patch.
*   UAT build 7.26.0 is ready for testing the reported issues by EOD 2026-03-25.

**Key Dates, Deadlines & Follow-ups**
*   **Order ID:** 75577957 (Refunded item count: 0)
*   **Recreated Issue Order:** #75582027 (Confirmed same date/quantity issue).
*   **Timeline:** Incident reported 01:50 UTC; UAT build released 10:13 UTC on 2026-03-25.
*   **Follow-up Required:** Validate the new UAT build resolves the crash for Sathya Murthy Karthik's iOS device.

**References**
*   Admin-UAT Order Log: `https://admin-uat.fairprice.com.sg/customer-support/delivery-orders/order-log/75577957`
*   Jira Tickets: DPD-822, DPD-823 (NTUCLink)


## [64/85] FP x Mirakl
Source: gchat | Group: space/AAAAhWLveDE | Last Activity: 2026-03-25T09:26:19.161000+00:00 | Last Updated: 2026-03-25T10:41:26.258531+00:00
**Daily Work Briefing: FP x Mirakl Integration**

**Key Participants & Roles**
*   **Dang Hung Cuong:** Initiated the initial discussion regarding API rate limiting constraints.
*   **Jill Ong:** Raised a new query on March 25, 2026, regarding seller status creation.
*   **Intrepid (External Integrator):** Third-party partner requesting an increase in API thresholds due to bottlenecks while serving multiple sellers.
*   **Cheryl Jones & LyLy Lim:** Tagged for visibility and action on both the rate limit inquiry and the new seller status query.

**Main Topic**
The thread addresses two distinct technical inquiries regarding the Mirakl platform:
1.  **API Rate Limiting:** Intrepid requested an increase in the current limit of one check per minute, which is hindering multi-seller operations. The team investigated feasibility but had not finalized a decision as of March 17.
2.  **Seller Status Configuration:** As of March 25, Jill Ong queried whether additional seller statuses can be created within Mirakl to accommodate specific needs. Both inquiries require investigation and technical validation.

**Pending Actions & Ownership**
*   **Action A:** Evaluate and respond to Intrepid's request to increase the API rate limiter threshold (currently 1/minute).
    *   **Owner:** Cheryl Jones, LyLy Lim (assigned for feasibility review).
*   **Action B:** Investigate technical feasibility of creating additional seller statuses in Mirakl.
    *   **Owner:** Cheryl Jones, LyLy Lim (tagged by Jill Ong for response).

**Decisions Made**
*   No final decisions were recorded regarding the API rate limit increase or the seller status configuration. Both items remain active inquiries requiring investigation and technical confirmation rather than resolved directives.

**Key Dates & Follow-ups**
*   **Original Inquiry:** March 17, 2026 (06:16 UTC) – API Rate Limit discussion initiated by Dang Hung Cuong. Last activity recorded at 06:40 AM on the same day.
*   **New Inquiry:** March 25, 2026 (09:26 UTC) – Jill Ong raised question regarding additional seller status creation.
*   **Thread Status:** Active with multiple replies across different dates; requires follow-up on both technical constraints and configuration possibilities.
*   **Next Steps:** Review technical feasibility for increasing the API rate limit AND confirm capabilities for creating new seller statuses in Mirakl before coordinating responses to Intrepid and Jill Ong.

**Specific References**
*   **Integrator:** Intrepid.
*   **Current Limit:** Once per minute for checking APIs.
*   **New Query Topic:** Creation of additional seller status in Mirakl.
*   **Platform:** Mirakl API.
*   **Source URL:** https://chat.google.com/space/AAAAhWLveDE


## [65/85] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/BviHwkT97xU | Last Activity: 2026-03-25T09:10:08.322000+00:00 | Last Updated: 2026-03-25T10:42:11.936410+00:00
**Daily Work Briefing: Digital Product Development (Leads) Group**

**Key Participants & Roles**
*   **Sneha Parab:** Initiating inquiry regarding system ownership; coordinating with Sazali.
*   **Daryl Ng:** Providing clarification on current and past system owner assignments.
*   **Sazali:** The individual currently managing the tagging activity for which assistance is requested (mentioned by Sneha).
*   **James & Pandi:** Identified as potential names to tag for "loyalty" ownership.
*   **CCO:** Referenced as an existing owner for loyalty initiatives.

**Main Topic**
The conversation focuses on validating and correcting the list of **system owners** for specific digital product domains: Gifting, EV (Electric Vehicles), and Loyalty within the Ecom/Omni channel. The discussion arose from a request by Sazali to correctly tag system owners during an active data activity.

**Pending Actions & Ownership**
*   **Action:** Tagging system owners for "Loyalty."
    *   **Context:** Sneha requires specific names to tag based on the confirmation that James and Pandi are likely the correct contacts, rather than just "CCO" generally.
    *   **Owner:** Implicitly Sazali (who requested help) or Daryl Ng (who provided the candidate names), pending final confirmation from Sneha to proceed with tagging.

**Decisions Made**
*   **Gifting & EV Ownership:** Confirmed that **Daryl Ng** is the system owner for both "gifting" and "EV."
*   **Loyalty Ownership Status:** Clarified that while "CCO" was previously associated, specific individuals (**James and Pandi**) are likely the correct contacts to tag moving forward.

**Key Dates & Follow-ups**
*   **Date of Discussion:** March 25, 2026 (09:06 – 09:10 UTC).
*   **Next Steps:** Sneha needs to finalize the tagging list with James and Pandi for the Loyalty domain. No specific deadline was set in this thread, but the activity is currently underway.

**References**
*   **Space URL:** https://chat.google.com/space/AAQAN8mDauE
*   **Message Count:** 5


## [66/85] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/23aNS8tE76g | Last Activity: 2026-03-25T08:59:56.409000+00:00 | Last Updated: 2026-03-25T10:43:02.349904+00:00
**Daily Work Briefing: Digital Product Development (Leads)**
**Resource:** [Leads] (Ecom/Omni) Digital Product Development
**Date Range:** March 25, 2026

### Key Participants & Roles
*   **Sneha Parab:** Initiator of the inquiry regarding engineer software access.
*   **Daryl Ng:** Provided information on budget allocation and request channels.
*   **Michael Bui:** Expressed personal need for the subscription.
*   **Gopalakrishna Dhulipati:** Tagged as the point of contact for handling requests (Owner: Pending Action).

### Main Topic
Discussion regarding the process to secure sponsored **Cursor subscriptions** for engineers who do not currently have organization-sponsored licenses. The team confirmed that a budget exists for this purpose and identified the correct internal channel for submission.

### Decisions Made
*   It was confirmed that a specific budget is allocated for Cursor subscriptions.
*   The approved method to request these subscriptions is through **Jazz**.
*   Reference was made to "Winson" as the source of this guidance regarding Jazz and budget availability.

### Pending Actions & Ownership
*   **Action:** Submit requests for Cursor subscriptions via Jazz.
    *   **Owner:** Sneha Parab (confirmed intent to reach out) and Michael Bui (needs access).
*   **Action:** Process/approve the incoming subscription requests.
    *   **Owner:** Gopalakrishna Dhulipati (tagged explicitly by both Sneha Parab and Michael Bui).

### Key Dates & Follow-ups
*   **March 25, 2026, 08:38:** Daryl Ng clarified the Jazz process.
*   **March 25, 2026, 08:53:** Sneha Parab indicated she would follow up ("back to you on this") and tagged Gopalakrishna Dhulipati.
*   **March 25, 2026, 08:59:** Michael Bui reiterated the need for access and also tagged Gopalakrishna Dhulipati.
*   **Next Step:** Follow-up required from the team once Sneha Parab submits requests to Jazz or upon confirmation from Gopalakrishna Dhulipati regarding the intake of these requests.

**Metadata Reference:**
*   Message Count: 6
*   Chat URL: https://chat.google.com/space/AAQAN8mDauE


## [67/85] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/VjNIGhgr76c | Last Activity: 2026-03-25T07:57:46.777000+00:00 | Last Updated: 2026-03-25T10:44:37.022858+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Key Participants & Roles**
*   **Sneha Parab:** Initiator of the request; coordinating BCRS status and deployment planning.
*   **Engineers:** Target audience for the status update request.
*   **Daryl Ng:** Carbon copy recipient.
*   **Andin Eswarlal Rajesh:** Carbon copy recipient.

**Main Topic**
Urgent alignment on Jira ticket statuses within the Digital Product Development space to ensure accurate tracking of deployments and prevent blockers in the release queue. Sneha highlighted that many tickets lack assignees due to Frontend (FE) and Backend (BE) subtasks, complicating status updates.

**Pending Actions & Ownership**
*   **Update Ticket Status:** All engineers must mark tickets deployed to production as **"Done"**.
    *   *Owner:* All Engineers.
*   **Highlight Pending Deployments:** Any deployments currently pending must be explicitly highlighted in this chat thread.
    *   *Owner:* All Engineers.
*   **Resolve Subtask Blockers:** Address specific subtasks (e.g., FE/BE) that are keeping parent stories in the "In Release Queue" status. Sneha provided **DPD-79** as an example where one subtask remains in the queue, preventing the main story from moving forward.
    *   *Owner:* All Engineers.

**Decisions Made**
*   No formal project decisions were recorded; however, a protocol was established requiring immediate status updates to allow for contingency planning.
*   Immediate action is required today so that tomorrow can be utilized to plan for any missed deployments.

**Key Dates & Deadlines**
*   **Date of Communication:** March 25, 2026 (07:55 AM UTC).
*   **Action Deadline:** Today (March 25, 2026) via the end of the day to facilitate planning.
*   **Upcoming Release:** Marketplace tickets are planned for release tomorrow in sync with the SAP deployment.

**References & Links**
*   **Jira Filter for Open Tickets:** [View Link](https://ntuclink.atlassian.net/jira/software/projects/DPD/issues?jql=project+%3D+DPD%0Aand+parent+%3D+DPD-225%0Aand+status+IN+%28%22IN+RELASE+QUEUE%22%2C+%22TESTING+IN+PREPRODUCTION%22%2C+%22IN+DEVELOPMENT%22%29%0AORDER+BY+assignee+ASC%2C+status+ASC%2C+created+DESC&atlOrigin=eyJpIjoibDoxZGJlMzZkNjBjNDY3MmIxMzYwZmMyYTgzZDg4ZWEiLCJwIjoiaiJ9) (Statuses: "IN RELASE QUEUE", "TESTING IN PREPRODUCTION", "IN DEVELOPMENT").
*   **Example Issue:** [DPD-79](https://ntuclink.atlassian.net/browse/DPD-79).


## [68/85] Project Light: Spotlight Topic - HIVE/Inventory - Mar 25
Source: gchat | Group: space/AAQACrAwhoI | Last Activity: 2026-03-25T07:28:24.185000+00:00 | Last Updated: 2026-03-25T10:45:39.058153+00:00
**Daily Work Briefing: Project Light – HIVE/Inventory Session**

**Key Participants & Roles**
*   **Jacob Yeo:** Session Organizer/Coordinator (Confirmed via reminder message).
*   **Attendees:** Total of 14 participants viewed the initial notification out of a projected group of 23. Specific roles for other attendees were not detailed in the provided text.

**Main Topic/Discussion**
The conversation focused on logistical confirmation for an upcoming "Spotlight Topic" session regarding **HIVE/Inventory**. The primary objective was to ensure all participants are aware of the specific physical location for the meeting to prevent attendance issues.

**Pending Actions & Ownership**
*   **Action:** Attendees must proceed to the designated room at the scheduled time.
    *   **Owner:** All 23 group members (implied).
*   **Action:** Jacob Yeo has completed the notification duty; no further explicit action items were assigned in this specific thread segment.

**Decisions Made**
*   **Location Confirmation:** The session location was finalized as **Level 10, Training Room 2**. This decision was communicated to the group on March 25, 2026.

**Key Dates & Deadlines**
*   **Event Date:** March 25, 2026 (Today).
*   **Notification Time:** 07:28:24 UTC.
*   **Follow-up:** The meeting is scheduled to commence immediately following the notification window; no future follow-up meetings were mentioned in this snippet.

**Summary**
Jacob Yeo issued a logistical reminder for the Project Light "HIVE/Inventory" Spotlight Topic session held on March 25, 2026. The critical update was the venue assignment: **Lvl 10 Training Room 2**. This message reached 14 of the 23 expected participants prior to the briefing time. No other discussion points or action items were recorded in this specific log entry.


## [69/85] DPD x DPM
Source: gchat | Group: space/AAQApzD7Im0 | Last Activity: 2026-03-25T06:59:20.731000+00:00 | Last Updated: 2026-03-25T10:46:06.958900+00:00
### Daily Work Briefing: DPD x DPM Collaboration Space

**Key Participants & Roles**
*   **Daryl Ng:** Tech Lead; flagged CHAS calculation issues. Tagged regarding Gamification ownership and delivery logic inquiries. Requested breakdown of existing orange label display logic on Omni and OG homepages.
*   **Vivian Lim Yu Qian:** Initiator of topics; driving mandates (MTI price per piece) and feature rollouts. Investigating SWA migration history.
*   **Rajesh Dobariya & Andin Eswarlal Rajesh:** Inquired about Gamification data requirements for CRM PNS automation. Previously asked to clarify display logic for "Normal" vs. "Express" delivery. **Andin** has initiated "1HD Business testing" with 8 replies.
*   **Sneha Parab:** Tagged regarding Tech Lead ownership transition and SWA/Wordpress vs. Publitas inquiry.
*   **Yangyu Wang & Zi Ying Liow:** Tagged in the latest thread regarding orange label display logic clarification; last reply pending as of March 25, 01:34 AM.

**Main Topics**
1.  **Delivery Text Logic (Updated):** Daryl Ng explicitly requests a breakdown of the *existing* logic for displaying the "orange label" text on both Omni and OG homepages to support required updates. This follows Rajesh Dobariya's earlier inquiry about "Normal Delivery" logic for Express updates.
2.  **Gamification Data Requirements:** CRM team requires specific BigQuery (BQ) data points for PNS automation. Needs confirmation on existing data points or effort estimation for pushing new data. Previous ownership attributed to Nhu/Jack's team.
3.  **Govt Mandate (MTI):** Implementation of "Price per Piece" info for 40+ categories in the current app MVP.
4.  **CHAS Calculation Bug:** UI discrepancy where cart-level discounts split at the sales order level affect CHAS calculations (Ticket: `DPD-530`).
5.  **SWA Migration:** Investigation into reverting SWA ad serving from Publitas back to Wordpress (`DIS-585`) and associated effort estimation.
6.  **1HD Business Testing:** Andin Eswarlal Rajesh initiated a discussion on "1HD Business testing" (March 25, 06:59 AM) with 8 replies; currently active with 8 unread messages.

**Pending Actions & Ownership**
*   **Orange Label Logic Clarification:** Share and document the existing logic for showing orange labels on Omni and OG homepages (specifically regarding text variables). *Owner: Daryl Ng (to share details).*
*   **Gamification Data Query:** Clarify current ownership of Gamification features and provide BQ table/column names or confirm data push needs. *Owner: Daryl Ng (to clarify).*
*   **Tech Lead Confirmation:** Determine if Daryl Ng is still the lead for Price per Piece expansion or identify the correct owner. *Owner: Vivian Lim Yu Qian / Team.*
*   **CHAS Issue Analysis:** Explain the cart-level discount splitting issue to enable an API fix. *Owners: Prajney Sribhashyam, Wai Ching Chan.*
*   **SWA Revert Analysis:** Assess effort required to revert SWA ad serving from Publitas back to Wordpress. *Owners: Sneha Parab, Arijit Mondal.*
*   **1HD Testing Follow-up:** Review the 8 replies regarding Andin's "1HD Business testing" initiation. *Owner: Rajesh Dobariya / Team.*

**Decisions Made**
*   No formal decisions recorded; the thread contains active requests for clarification and execution. The intent to fix the CHAS bug via an API update remains established. The feasibility of reverting SWA ads is under investigation. The specific implementation details for the "orange label" text on Omni/OG homepages are pending Daryl Ng's input based on his March 25 request. The status of "1HD Business testing" initiated by Andin Eswarlal Rajesh is currently active and requires review.

**Key Dates & Deadlines**
*   **March 11:** Space creation; Vivian's inquiry on Price per Piece.
*   **March 12:** Daryl flags CHAS calculation issue (`DPD-530`).
*   **March 16:** Request to complete 100% Android rollout for Search on Omni home and Sticky Header UI. Vivian initiates SWA inquiry. Rajesh inquires about "Normal Delivery" logic.
*   **March 24, 07:39 AM:** Vivian initiates inquiry regarding SWA `DIS-585`.
*   **March 25, 01:34 AM:** Daryl Ng requests clarification on the existing orange label display logic for Omni and OG homepages. Last reply pending from Yangyu Wang/Zi Ying Liow.
*   **March 25, 06:59 AM:** Andin Eswarlal Rajesh initiates "1HD Business testing" discussion (8 replies).

**Reference Links**
*   Price Per Piece Wiki: `https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008175965/Price+Per+Piece+Multipack+in+Display+Unit`
*   CHAS Ticket: `DPD-530`
*   Sticky Header UI Ticket: `ENGM-2501`
*   SWA Migration Ticket: `DIS-585`


## [70/85] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/GZUDEA5Z4tU | Last Activity: 2026-03-25T06:58:52.624000+00:00 | Last Updated: 2026-03-25T10:46:20.574093+00:00
**Daily Work Briefing: DPD x DPM Release & Bosses' Testing Session**

**Key Participants & Roles**
*   **Daryl Ng:** Initiator of testing logistics; coordinating with Rajesh on the session schedule and rollout expectations.
*   **Andin Eswarlal Rajesh:** Developer/Lead responsible for app store submissions, bug status, and managing the release pipeline.
*   **Rajesh:** Stakeholder organizing a production testing session ("with the bosses"); target dates are Friday or Monday.

**Main Topic**
Status update on the "1HD" release changes for Digital Product Development (DPD) and planning logistics for a high-level production testing session organized by Rajesh. The discussion centers on the feasibility of ensuring 100% user rollout prior to the meeting, given App Store staged rollout constraints.

**Decisions Made**
*   **Release Scope:** All changes except one specific iOS bug (tracked as DPD-740) have been submitted to the App Store and Google Play Store. The fix for the iOS bug is scheduled for inclusion in this week's release.
*   **Testing Strategy:** A production build containing all current changes will be provided for testing, rather than relying on TestFlight (which Daryl noted would be difficult for stakeholders to install).
*   **Communication Protocol:** If a 100% rollout cannot be guaranteed before the session, Rajesh must be informed immediately.

**Pending Actions & Ownership**
*   **Initiate Coordination Meeting:** Andin Eswarlal Rajesh will start a conversation regarding the testing plan and potential rollout delays. (Owner: Andin)
*   **Session Alignment:** Daryl to coordinate with Rajesh regarding the "DPD x DPM" approach discussed face-to-face earlier, ensuring alignment on how to handle stakeholders if the rollout is incomplete. (Owner: Daryl Ng)

**Key Dates & Deadlines**
*   **March 25, 2026:** Current date of conversation; iOS bug fix scheduled for this week's release.
*   **Friday or Monday (Target):** Rajesh's target dates to conduct production testing with the bosses. The session is confirmed for **Monday**.
*   **Immediate Follow-up:** Preparation must be completed before the Monday session to assess if a full rollout is achievable.

**Specific References**
*   **Jira Ticket:** DPD-740 (iOS bug status).
*   **Project Code:** 1HD release; DPD x DPM initiative.
*   **Platform Constraints:** App Store staged rollout limitations prevent guaranteed instant availability for all users even if published immediately.


## [71/85] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/77DpGxXYs38 | Last Activity: 2026-03-25T06:41:02.860000+00:00 | Last Updated: 2026-03-25T10:47:15.166447+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Initiator; defines scope, timing, data requirements, diagram formatting, and slide content.
*   **Tiong Siong Tee:** Clarifies technical scope (Payment/FPPay) and presentation depth.
*   **Michael Bui:** Validates strategic purpose; drafts RMN flow diagrams; raises questions on long-term maintenance and B2B applicability.
*   **Hui Hui Voon:** Identified as the owner of the "D&T Scope for Project Light Workshop."

**Main Topic**
Preparation of presentation slides for the **Project Light Workshop**, focusing on:
1.  **Spotlight Topic 5: RMN** (Scheduled for today, March 25, 4:45 PM – 5:45 PM).
2.  **Spotlight Topic 2: Payment** (Scheduled for Thursday, March 26, 1:00 PM slot).

**Decisions Made & New Directives**
*   **RMN Diagram Status:** Michael Bui has successfully converted the draft RMN flows to **Sequence Diagram format**.
*   **New Development Model:** For new development on RMN, capacity will be allocated separately and aligned with the **RMN team**.
*   **Ad Service Scope Clarification:** Alvin Choo raised a critical "To-Be" state question regarding the **AD service**. It must be clarified if the team intends to maintain this service for non-Light usage (e.g., in-store screens) post-launch. Michael Bui reiterated that adding this to the slides requires confirmation on whether the team is expected to continue supporting it for these scenarios.
*   **Labeling Conventions:** The orchestrator service involved in these flows should be explicitly labeled as **"B2C backend"** and potentially applicable to **B2B** contexts.
*   **New Slide Requirement (Direct from Alvin Choo):** Add one additional slide detailing the **data flow from B2C backend to OSMOS**.

**Pending Actions & Ownership**
*   **Finalize RMN Diagrams & Slides (Michael Bui/Alvin Choo):**
    *   Ensure the newly converted sequence diagrams have clean arrows and clear dependencies.
    *   Label the orchestrator service as "B2C backend."
    *   Resolve the AD service scope question: Confirm if support for non-Light usage (in-store screens) is required post-launch before finalizing slides.
    *   **Update:** Incorporate the new slide regarding the data flow from B2C backend to OSMOS as requested by Alvin Choo.
*   **Clarify Future Maintenance (Michael Bui/Team):**
    *   Define the post-launch strategy regarding RMN changes and CoMall development contracts, specifically noting the new alignment with the RMN team for capacity allocation.
*   **Prepare Slides:**
    *   **RMN Slide:** Due prior to today's 4:45 PM slot (incorporating sequence diagrams, AD service clarification, and the new B2C-to-OSMOS data flow).
    *   **Payment Slide:** Due prior to Thursday, March 26, at 1:00 PM.

**Key Dates & Deadlines**
*   **Today (March 25, 2026):**
    *   **Time:** 4:45 PM – 5:45 PM.
    *   **Event:** Spotlight Topic 5: RMN presentation.
*   **Thursday (March 26, 2026):**
    *   **Time:** 1:00 PM – 2:00 PM.
    *   **Event:** Spotlight Topic 2: Payment presentation.

**Resources Referenced**
*   Google Docs Presentation: `D&T Scope for Project Light Workshop`.


## [72/85] Vera, Alvin, Ravi, Gopalakrishna
Source: gchat | Group: space/AAQAp2kBxiM | Last Activity: 2026-03-25T06:32:09.861000+00:00 | Last Updated: 2026-03-25T10:47:31.497296+00:00
**Daily Work Briefing: Business Invitation Letter Coordination**

**Key Participants & Roles**
*   **Alvin Choo:** Coordinator; initiated document requests, flagged date errors, coordinated with "Rock" for updates.
*   **Vera Wijaya:** Stakeholder; provided specific visa duration requirements and followed up on delivery status.
*   **Gopalakrishna Dhulipati:** Document Provider; uploaded final invitation letters for multiple recipients.
*   **Michael Bui:** Recipient (via @mention); received documents submitted by Gopalakrishna for review.
*   **Rock:** External party; requested to update dates on invitation letters (status: pending).

**Main Topic**
Coordination and revision of Chinese Business Visa Invitation Letters for Vera Wijaya, Ravi Goel, Dhulipati Gopalakrishna, and Bui Le Minh. The discussion focused on correcting date discrepancies to align with visa validity requirements (>6 months) and ensuring timely delivery.

**Decisions Made**
*   **Visa Duration:** Agreed that invitation dates must cover a period allowing for >6-month multi-entry visas.
    *   *Initial proposal:* 1 May 2026 – 31 Oct 2026.
    *   *Final agreed duration:* 1 April 2026 – 30 November 2026 (Multi-entry).
*   **Submission Process:** Confirmed that the "Express" option would be used for submission to expedite processing.

**Pending Actions & Ownership**
*   **Update Invitation Dates:** Rock must update the invitation letters to reflect the new date range (1 Apr – 30 Nov 2026).
    *   *Owner:* Alvin Choo (confirmed he asked Rock to do this).
*   **Preliminary Review & Submission:** Documents submitted with "Express" option are pending results.
    *   *Status:* Submitted by Gopalakrishna; awaiting result (1-3 working days) and actual submission (2-4 working days).
    *   *Owner:* Michael Bui (to check status/results).

**Key Dates & Deadlines**
*   **Mar 24, 07:28:** Vera specified the required date range (1 Apr – 30 Nov 2026).
*   **Mar 25, 02:00:** Vera requested updated letters by "today" (Mar 25).
*   **Mar 25, 05:28:** Gopalakrishna uploaded final PDFs for Bui Le Minh, Vera Wijaya, and Ravi Goel.
*   **Upcoming Deadline:** Preliminary review result expected within **1-3 working days** of submission (approx. Mar 26–27). Actual submission processing time is **2-4 working days**.

**Follow-ups Required**
*   Confirm if Rock has successfully updated the dates on the original drafts before finalizing the new batch.
*   Monitor Michael Bui's "Express" submission status for results within the 1-3 day window.


## [73/85] Alvin Choo
Source: gchat | Group: dm/zmMZpgAAAAE | Last Activity: 2026-03-25T05:57:40.052000+00:00 | Last Updated: 2026-03-25T06:45:14.365580+00:00
**Daily Work Briefing: RMN & Postmortem Updates (Updated)**
**Resource:** Alvin Choo (Lead/Manager) | **Participant:** Michael Bui (Domain Expert, Backend Dev)
**Date Range:** March 3 – March 24, 2026

### **Key Participants & Roles**
*   **Alvin Choo:** Leads coordination for RMN postmortem reports, travel logistics, and securing business invitation letters from CoMall. Contact: +65 9351 0653.
*   **Michael Bui:** Domain expert responsible for backend implementation; currently on leave until April 2, with a public holiday on April 3.

### **Main Topics**
1.  **Wuhan Travel & Visa Processing:** Departure confirmed for **April 6, 2026**. Michael requires a multi-entry visa (valid 6mth or 1yr) applied for at least one month in advance. Alvin is securing an invitation letter from CoMall to expedite the application.
2.  **RMN Postmortem & Incident Review:** Finalizing report for BCRS completion; addressing "Overage on transaction sync" and transition to impressions-based model.
3.  **Technical Implementation:** Backend work for RMN tickets; integration with Advertima (Grassfish CMS) and Vijaykumar (PDA owner). GLMS re-testing initiated after Pentest fixes (DPD-591).

### **Decisions Made**
*   **Visa Strategy:** Visa Type M (Business & Trade) confirmed. Michael is on leave next week; Alvin advised checking with Gopal and Ravi regarding their self-processing methods while waiting for the invitation letter.
*   **Contact Exchange:** On March 25, Alvin provided his mobile number (**93510653**) to facilitate direct communication during the visa process.
*   **Document Requirements:** Michael provided personal details (Vietnam Passport P00241735, DOB: 1986-09-22) to facilitate the visa application form.
*   **Workshop Deliverables:** Michael will prepare "as-is" and "to-be" design plans rather than full slides; Alvin confirmed existing documents need alignment only.
*   **Ticket Prioritization:** OMNI-1282 (SAP invoice) deprioritized; OMNI-1191 and OMNI-1247 remain active but OSMOS-focused.

### **Pending Actions & Ownership**
| Action Item | Owner | Details/Context |
| :--- | :--- | :--- |
| **Visa Application** | Michael Bui | Apply for multi-entry Type M visa immediately upon receiving invitation letter; submit online verification today if possible. Use Alvin's number (93510653) for coordination. |
| **Invitation Letter** | Alvin Choo | Secure business letter from CoMall to speed up Michael's visa process. |
| **Workshop Prep (Design)** | Michael Bui | Create docs detailing "as-is" vs. "to-be" integration flows; note: On leave until April 2, PH on April 3. |
| **Postmortem Review** | Alvin Choo | Final review after PDA impact verification (Vijay) and Advertima POV status inclusion. |
| **GLMS Re-testing** | Michael Bui | RMN APIs fixed for Pentest issues; GLMS instructed to re-test upon return from leave. |

### **Key Dates & Milestones**
*   **March 24/25:** Departure set for April 6. Alvin requested invitation letter today; Michael advised on visa processing timeline (1 month lead time). Contact details exchanged on March 25.
*   **April 2:** End of Michael's current leave period.
*   **April 3:** Public Holiday in Singapore.
*   **April 6:** Confirmed departure date for Wuhan, China.
*   **End of March:** PM25 rating meeting (Alvin) to be scheduled; Winson invited.
*   **End of Q1 2026:** Advertima POV pilot period concludes.


## [74/85] #dpd-dba
Source: gchat | Group: space/AAAAMh7T8Y0 | Last Activity: 2026-03-25T05:52:14.208000+00:00 | Last Updated: 2026-03-25T06:46:01.002094+00:00
**Daily Work Briefing: #dpd-dba**

**Key Participants & Roles**
*   **Akash Gupta:** DBA Team Representative/Requestor.
*   **Wai Ching Chan:** Deployment Coordinator (Service Owner).
*   **Tiong Siong Tee:** Communication Initiator.
*   **Sampada Shukla, Hanafi Yakub, Gopalakrishna Dhulipati, Dodla Gopi Krishna:** DBA Team Members (CC'd for support/monitoring/response to incidents).
*   **Lester Santiago Soriano:** Tagged recipient by Tiong Siong Tee.

**Main Topic**
The conversation covers two primary items: the execution of a specific Jira service ticket and coordination for a production deployment involving a database schema migration. Additionally, a new high-priority incident regarding GKE Autopilot scale-downs impacting Service Level Objectives (SLOs) has been identified.

**Pending Actions & Owners**
*   **Execute DSD-11003 Ticket:**
    *   **Action:** Run the request associated with ticket `DSD-11003`.
    *   **Owner:** DBA Team (specifically requested to Akash Gupta).
    *   **Status:** Initial request made on Mar 6; replies were received from Sampada Shukla and Hanafi Yakub. Ticket remains pending execution if not already completed.
*   **Support Production Deployment & Monitoring:**
    *   **Action:** Standby and monitor the `fpon` database during the deployment of `order-service`.
    *   **Owner:** DBA Team (specifically requested to Akash Gupta and Gopalakrishna Dhulipati).
    *   **Status:** Requested on Mar 9; migration script details provided.
*   **Investigate SLO Impact & Proxy Scale-Down:**
    *   **Action:** Investigate "bad connection" errors caused by GKE Autopilot cluster-autoscaler performing automatic scale-downs of the `sqlproxy-prod-ap` node.
    *   **Owner:** DBA Team (specifically requested to @Gopalakrishna Dhulipati and @Dodla Gopi Krishna).
    *   **Status:** Reported by Akash Gupta on Mar 25; identified as a contributing factor impacting SLOs across services.

**Decisions Made**
*   A new column named `container_deposit` of type `json` with a default value of `NULL` will be added to the `order_service.order_items` table in the `fpon` database.
*   The operation is confirmed to be wrapped in a transaction (`BEGIN...COMMIT`).
*   **New:** The issue regarding proxy scale-downs requires immediate attention from the DBA team to mitigate SLO degradation.

**Key Dates, Deadlines & Follow-ups**
*   **Mar 6, 2026 (01:48 UTC):** Initial request for ticket `DSD-11003` made by Akash Gupta.
*   **Mar 9, 2026 (04:36 UTC):** Deployment window scheduled for **11:00 PM** on this date (local time context implied as deployment was announced). Migration script details shared.
*   **Mar 12, 2026 (05:34 UTC):** Tiong Siong Tee sent a reply specifically tagging @Lester Santiago Soriano.
*   **Mar 25, 2026 (05:52 UTC):** Akash Gupta reported GKE Autopilot scale-down incidents affecting the `sqlproxy-prod-ap` cluster, causing "bad connection" errors impacting SLOs.

**References**
*   **Jira Ticket:** `DSD-11003` (URL: https://ntucenterprise.atlassian.net/servicedesk/customer/portal/1459/DSD-11003)
*   **Database/Table:** `fpon.order_service.order_items`
*   **Migration Command:** `ALTER TABLE order_items ADD COLUMN container_deposit json DEFAULT NULL;`
*   **Datadog Log Query:** https://app.datadoghq.eu/logs?query=%22driver%3A%20bad%20connection%22&agg_m=count&agg_m_source=base&agg_t=count&cols=host%2Cservice&fromUser=true&messageDisplay=inline&refresh_mode=paused&storage=hot&stream_sort=desc&viz=stream&from_ts=1774365188232&to_ts=1774374564976&live=false
*   **Affected Cluster:** `sqlproxy-prod-ap` (GKE Autopilot)


## [75/85] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/BVkgpZZxX1g | Last Activity: 2026-03-25T05:30:16.605000+00:00 | Last Updated: 2026-03-25T06:46:10.312998+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Initiator of the inquiry; seeking confirmation on payment policy.
*   **Zaw Myo Htet:** Clarified terminology regarding "Hybrid pre-order."
*   **Daryl Ng:** Provided definitive answer and referenced Terms & Conditions (T&C).

**Main Topic**
Discussion focused on whether e-vouchers can be used to pay for "Hybrid pre-orders" (defined as in-store pre-orders initiated via the customer app) within the customer application.

**Decisions Made**
*   **Policy Confirmation:** E-vouchers are **not allowed** for Hybrid pre-orders paid via the customer app.
*   **Basis of Decision:** This restriction is explicitly stated in the Terms & Conditions (T&C) of the e-voucher.

**Pending Actions**
*   **Status:** None. The inquiry was resolved within the chat thread; no new tasks or ownership assignments were generated. Prajney Sribhashyam confirmed his alignment with Daryl Ng's statement after verification.

**Key Dates & Follow-ups**
*   **Date of Discussion:** March 25, 2026 (UTC).
*   **Timeline:** Conversation occurred between 05:19 UTC and 05:30 UTC.
*   **Follow-up Required:** No immediate follow-up actions identified as the matter was confirmed by referencing existing documentation (T&C).

**Reference Data**
*   **Resource:** BCRS Firefighting Group
*   **Chat URL:** https://chat.google.com/space/AAQAgT-LpYY


## [76/85] Team Starship
Source: gchat | Group: space/AAQAX9iKYf0 | Last Activity: 2026-03-25T05:16:29.121000+00:00 | Last Updated: 2026-03-25T06:48:28.343114+00:00
**Daily Work Briefing: Team Starship (Updated)**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Operations/Testing Lead.
*   **Danielle Lee:** Biz Ops/S&G Representative.
*   **Vivian Lim Yu Qian:** Product/Design Liaison.
*   **Alvin Choo:** Compliance Lead / Technical POC.
*   **Zi Ying Liow:** Frontend/Promotion Logic Inquiry.
*   **Sathya Murthy Karthik:** Shared Omni Roadmap update (March 2026).

**Main Topics & Decisions**

1.  **BCRS Refunds Testing Status (Critical Update)**
    *   **Status:** UAT Sign-off received for Customer App, Backend/Backoffice, MP Seller, and Preorder Staff Application.
    *   **New Inquiry:** Danielle Lee raised a Category Manager query regarding **Pre-order via App** using **FP e-gift vouchers**. Prajney to confirm feasibility as payment method.
    *   **Payment Gateway (New):** Zi Ying Liow inquired about **Cybersource OTP handling** for B2B orders > threshold. Alvin Choo confirmed Cybersource integration behavior; pending confirmation on whether OTP flow applies automatically to the new B2B platform upon integration.

2.  **Bug Report: App Icon Display (DPD-783)**
    *   **Issue:** Vivian reported a regression where the app icon displays a Christmas theme instead of the default.
    *   **Action:** Bug ticket **DPD-783** created for urgent resolution ("asap").

3.  **New Request: Cart-Level Coupon Allocation (GP Calculation)**
    *   **Request:** Alvin Choo relayed a request from Ryan to stop considering cart-level coupon allocation per SKU.
    *   **Objective:** Ensure accurate Gross Profit (GP) calculation for products.
    *   **Decision/Pending:** The team is currently determining whether to park this requirement in the "Project Light" list.

4.  **Frontend Tag Mapping Inquiry**
    *   **Inquiry:** Zi Ying Liow sought clarification on mapping logic between promotion methods and frontend tags. No resolution documented yet; requires technical verification.

5.  **OMNI Project Status & Compliance**
    *   **Omni Roadmap Review:** PMs must review the "Omni Roadmap Consolidated from Jan 2026." A list of items to deprioritize is required by **EOD today (March 25)**.
    *   **OMNI-1345 (Sales Breakdown):** MP Business has instructed an indefinite **hold** due to foundational changes in the consolidated fulfilment business model. No further work until requirements are finalized.

6.  **Operational Pilots**
    *   Operations continues piloting the "picker app enhanced for CT58" on newer models (DT50S, DT66S). Prajney emphasized testing new models before store rollout.

7.  **CHAS Verification Flow**
    *   Auto-verification via MyInfo remains technically feasible but outside current "Light" scope. Vivian to verify technical assumptions with Serene.

8.  **Scan@Door: AI Personalisation Discussion**
    *   **Context:** Daryl Ng initiated a discussion regarding Scan@Door personalization using AI to issue personalized vouchers, shifting from rule-based logic.
    *   **Impact:** Requires Backend (BE) changes estimated at **2 weeks**.
    *   **Timeline:** Targeted go-live is mid-April.
    *   **Decision Pending:** The team must determine if this requirement should be prioritized given the development timeline and resource constraints.

**Pending Actions & Owners**

| Action Item | Owner | Deadline/Note |
| :--- | :--- | :--- |
| **Urgent Fix:** Revert app icon display (DPD-783) | Engineering Team / Andin Eswarlal Rajesh | ASAP |
| Finalize Returns & Refunds sign-off; Confirm Production Deploy time | Prajney Sribhashyam / Finance/Corp Control | **EOD Today** |
| **Confirm:** Pre-order via App with FP e-gift voucher validity | Prajney Sribhashyam | Immediate |
| **Clarify:** B2B Cybersource OTP flow applicability | Alvin Choo | As needed |
| Submit list of items to deprioritize from Jan 2026 Omni Roadmap | All PMs | **EOD Today (March 25)** |
| Update OMNI-1282 status (De-prioritize) | Alvin Choo / Koklin Gan | Pending confirmation |
| **PAUSE** work on OMNI-1345 requirements | All Stakeholders | Until business model is finalized |
| **Clarify:** Cart-level coupon allocation logic & Project Light inclusion | Alvin Choo / Ryan's team | Pending decision |
| Prioritize Scan@Door AI Personalisation (BE impact assessment) | Danielle Lee, Daryl Ng, Tech Leads | Immediate review required |

**Key Dates & Follow-ups**

*   **Meeting Rescheduled:** Weekly Epics meeting postponed to **Wednesday, March 12 (tomorrow) at 11:00 AM**.
    *   **Location:** Level 12 Room 18 (subject to availability; virtual or pantry table as backup).
    *   **Agenda:** BCRS work progress review, capacity planning, and Scan@Door prioritization decision.
*   **Reference Tickets:** SHOP-3779, OMNI-1099, DPD-100, **DPD-783**, OMNI-1345, OMNI-1282, OMNI-1421.


## [77/85] PFM x Events/UID Martech Issues
Source: gchat | Group: space/AAAAwg3yipA | Last Activity: 2026-03-25T05:07:07.446000+00:00 | Last Updated: 2026-03-25T06:48:57.546064+00:00
**Daily Work Briefing: PFM x Events/UID Martech Issues**

**Key Participants & Roles**
*   **Nicole Lim (PFM):** Initiator of access requests, incident reports, automation validation, and new GMC integration review.
*   **Sneha Parab:** Primary technical contact for access issues, event incidents, exclusion list validation, and the new Google Merchant Centre (GMC) query.
*   **James Huang:** Tagged regarding missing events, Exclusion List ownership, and the urgent GMC integration impact assessment.

**Main Topic & Discussion**
1.  **Google Merchant Centre (GMC) Integration Urgency:** Nicole Lim received an email on March 25 regarding mandatory updates to the BigQuery (BQ) Merchant exports for multi-channel products by March 26. The update involves new guidelines to accurately manage products sold online and in-store. It is currently unclear if PFM currently utilizes this specific integration, requiring immediate review of impact (@James Huang, @Sneha Parab).
2.  **Performance Marketing Exclusion List:** A `category_l3` was added on March 19 for self-service exclusion of SKUs/categories from the DB catalogue. Nicole Lim requested validation that the associated automated job runs correctly, noting uncertainty regarding ownership/handover since Tze Hsien's departure.
3.  **Critical Incident: Missing Events:** A data integrity issue occurred on **March 11**, where zero events were sent to all platforms. This was flagged by Nicole Lim on **March 12** as a potential upstream change.
4.  **Martech AI Chatbot Access:** Ticket **NEDMT-2346** created for Stephanie and the MA team.

**Pending Actions & Owners**
*   **Action:** Review GMC integration guidelines to confirm current usage of BQ Merchant exports for multi-channel products and assess impact of mandatory updates due tomorrow (March 26).
    *   **Owner:** James Huang, Sneha Parab.
    *   **Context:** Urgent review required to determine if existing workflows need modification per new guidelines.
*   **Action:** Validate the automated job run for the Performance Marketing Exclusion List following the March 19 `category_l3` update.
    *   **Owner:** Sneha Parab, James Huang.
    *   **Context:** Confirm operational status and process ownership.
*   **Action:** Investigate root cause of missing events sent on March 11 (0 events to all platforms).
    *   **Owner:** Sneha Parab, James Huang, respective teams.
    *   **Context:** Requires confirmation on upstream changes causing the data gap.
*   **Action:** Process access request for Martech AI Chatbot (Ticket NEDMT-2346).
    *   **Owner:** Technical team (assigned to Sneha Parab).

**Decisions Made**
*   No final resolution on the root cause of the March 11 missing events or the status of the Exclusion List automation.
*   GMC integration impact is currently under investigation; no decision on necessary changes has been made yet due to uncertainty regarding current usage.
*   Access request for Martech AI Chatbot remains pending completion.

**Key Dates & Follow-ups**
*   **March 10, 2026:** Ticket NEDMT-2346 created.
*   **March 11, 2026 (UTC):** Incident date; zero events sent to platforms.
*   **March 12, 2026:** Missing event issue reported and escalated. Last reply at 02:22 AM UTC.
*   **March 19, 2026:** New exclusion category added; automation validation requested. Last reply at 12:07 PM UTC (Local Time).
*   **March 25, 2026 (UTC):** Nicole Lim flagged the GMC/BQ export update requirement with a deadline of March 26.
*   **Immediate Follow-up:** Confirm current BQ Merchant export usage and required changes by end of day March 25 to meet March 26 deadline.

**Reference Links**
*   Ticket: https://ntuclink.atlassian.net/browse/NEDMT-2346
*   Chat Space: https://chat.google.com/space/AAAAwg3yipA
*   GMC Guidelines Link: https://c.gle/AEJ26quJGD9DVmYiNGnScfpBBpoylAdgJAnFit2TyMiMZomv798vYjjlwXztTsSXK4FW9J71NdhKCiqrmtIHJpny6GmDLa6BWTySjPRgV4TdpPUJZu5XyiO16zwaMqjjKS4GpQcDKi4nNjj9STc2LY0y5NtaljD33QTUVJ2CknAJKuB5II4RTboxmNzYy3ZqkRLEDDFg6QV85Be906X0H2fAiTOKbcerli6R-aq-Co4
*   Confluence Ref: https://ntuclink.atlassian.net/wiki/spaces/CMT/pages/2674622589/Exclusion+Inclusion+Self-service+System


## [78/85] Product x RMN x Platform
Source: gchat | Group: space/AAQAR16KXqc | Last Activity: 2026-03-25T04:39:11.591000+00:00 | Last Updated: 2026-03-25T06:49:45.065008+00:00
**Daily Work Briefing: Product x RMN x Platform**

**Key Participants**
*   **Christopher Yong:** Product/Business Lead.
*   **Rajiv Kumar Singh:** Ad Operations/Strategy.
*   **Sanjana Sanjana:** Analytics/Measurement (GA tracking for sponsored vs. organic impressions).
*   **Nikhil Grover:** Product Engineering (in-store data lead).
*   **Vivian Lim Yu Qian:** Data Science/Ecom Search Lead.
*   **Ravi Goel:** Source of FPG app user data and in-store transaction breakdowns.
*   **Cecilia Koo Hai Ling, Ryan Ho:** Stakeholders (CC'd on recent updates).

**Main Topics Discussed**
1.  **In-Store Data Requirements (Nestle Deal):** Christopher Yong initially requested an average percentage breakdown of DCC vs. non-DCC in-store payments. Ravi Goel previously provided December 2025 GMV data noting ~41% of grocery business was checked out via app/digital loyalty, which Christopher deemed <50%.
    *   **Updated Insight:** On March 19 at 17:40, Christopher Yong shared critical analysis showing approximately **70% of sales** and **60% of transactions** in-store are attributable to members. This metric significantly improves the data scale for the Nestle pitch compared to the initial GMV percentage.
2.  **Banner UX Standardization:** Nikhil Grover proposed standardizing banner auto-scroll timers from 5 to 3 seconds, approved pending beta testing with CTR variance within 10% of baseline.
    *   **Status Update (March 26):** Product ads on Omni homepage swimlanes have passed UAT successfully. Business Go-live is scheduled for Thursday, March 26. Changes will be deployed tomorrow to make ads live.
3.  **Ecom Search Analysis:** Post-launch review showed stable RMN revenue (~$300/week uplift) but no significant new customer acquisition or conversion uplift despite increased search traffic.

**Decisions Made**
*   **Banner Timer Change:** Standardization to a 3-second auto-scroll timer approved, conditional on successful beta testing (CTR within 10% of baseline).
*   **Data Validation for Nestle:** The initial concern regarding low DCC activity is resolved by the new member-centric metrics. Christopher Yong confirmed that member data provides the necessary scale for the deal without requiring further transaction-level digging for percentage validation.
*   **Omni Homepage Ad Deployment:** UAT passed; deployment to live ads on aligned slots (3, 5, 7, 11, 13, 15) is proceeding as scheduled for March 26.

**Pending Actions & Ownership**
*   **Finalize Nestle Pitch Materials:** Christopher Yong will utilize the new 70% sales/60% transaction member data to finalize the Nestle engagement strategy. No further deep-dive into transaction-level DCC percentages is required at this stage.
*   **Provide User Metrics:** Christopher Yong still awaits weekly/monthly active FPG app user data from Ravi Goel (distinct from the in-store member data).
*   **Monitor Banner Beta Performance:** Product team to track impressions and CTR during the phased rollout (currently 20% on March 16–19; scaling to 50% by March 19) for the timer change. Proceed only if CTR variance stays within 10% of baseline.
*   **GA Tracking Implementation:** Sanjana Sanjana to finalize tracking for Sponsored vs. Organic Product Impressions.

**Key Dates & Deadlines**
*   **March 16 (Mon):** Banner beta test began on iOS v7.24.0 and Android v7.22.1; Ecom Search rollout scheduled for Android.
*   **March 16–19:** Banner phased rollout at 20% user volume.
*   **March 19:** Banner scale-up to 50% of users. Christopher Yong shared the updated in-store member data (70% sales, 60% transactions) at 17:40 on this date.
*   **March 23:** Banner full (100%) rollout scheduled for timer standardization.
*   **March 26 (Thu):** Business Go-live for Product ads on Omni homepage swimlanes; changes to be deployed today/tomorrow depending on timezone execution.


## [79/85] BCRS Working Group - OMNI
Source: gchat | Group: space/AAQAkrn0niY | Last Activity: 2026-03-25T04:18:10.154000+00:00 | Last Updated: 2026-03-25T06:51:12.776414+00:00
**Daily Work Briefing: BCRS Working Group – OMNI**
**Source:** Google Chat (BCRS Working Group) & Jira
**Date Range:** March 5, 2026 – March 25, 2026

### Key Participants & Roles
*   **Teri Ong Qiu Mei:** Raised a critical security concern regarding "Scan & Go" inventory integrity.
*   **Prajney Sribhashyam:** Assigned to address the Scan & Go SKU substitution query and co-owner of FOC UAT resolution.
*   **Daryl Ng, Seokhwee Poh, Sathya Murthy Karthik:** Continued roles in UAT testing and POS logic resolution.
*   **Sip Khoon Tan, Piraba Nagkeeran:** Continuing work on iOS asset updates.
*   **Onkar Bamane:** Leading BCRS ECOM UAT sign-off requests.
*   **Lai Shu Hui, Wei Fen Ching, Jesslin Lim Bee Leng:** Targeted for ECOM UAT sign-off.

### Main Topics
**1. Scan & Go Inventory Integrity (Priority)**
Teri Ong Qiu Mei raised a specific concern regarding the "Scan & Go" feature: preventing customers from scanning barcode labels of old SKUs while physically removing new SKUs to avoid the 10-cent charge. This highlights a vulnerability in item verification logic between digital and physical inventory during self-service checkout. Prajney Sribhashyam is assigned to investigate this substitution mechanism.

**2. POS & Pre-order FOC Logic**
*Continued:* Investigation into POS failures regarding Free of Charge (FOC) SKUs with $0 RSP. Confirmed that standard POS interfaces cannot process $0 items directly; workflows require excluding items from scanning or applying 100% discounts on SAP-defined promo sets.

**3. iOS Asset Update**
*Continued:* Piraba Nagkeeran identified an outdated "snowman" default icon in the iOS repository (Jira ticket **DPD-657**). Sip Khoon Tan has been engaged to provide the correct asset.

**4. BCRS ECOM UAT Sign-off (New)**
Onkar Bamane initiated a request for sign-off on BCRS ECOM UAT. Relevant stakeholders (**Lai Shu Hui, Wei Fen Ching, Jesslin Lim Bee Leng**) have been tagged. Onkar has also shared the "Deploy BCRS Enhancements related to ECOM Process" document (Google Doc: `179m3aUNLXWz_4lKbT7-VBhOv11bCuQVr`) for review.

### Decisions Made & Process Updates
*   **POS Limitation Confirmed:** POS systems cannot accept $0 RSP for FOC SKUs via standard interface. In-store pre-orders must exclude scanning or use discount logic on promo sets.
*   **Scan & Go Query Open:** The specific mechanism to prevent SKU substitution has been flagged as a priority concern by Teri Ong Qiu Mei and assigned to Prajney Sribhashyam for immediate technical review.
*   **ECOM UAT Initiated:** Onkar Bamane formally requested sign-off for BCRS ECOM UAT, directing the document `Deploy BCRS Enhancements related to ECOM Process.docx` to relevant approvers.

### Pending Actions & Owners
*   **Action:** Investigate and resolve the "Scan & Go" SKU substitution vulnerability (Old vs. New SKUs).
    *   **Owner:** Prajney Sribhashyam.
    *   **Context:** Prevent loss of 10-cent charges due to barcode mismatch.
*   **Action:** Provide sign-off for BCRS ECOM UAT and review enhancement deployment docs.
    *   **Owners:** Lai Shu Hui, Wei Fen Ching, Jesslin Lim Bee Leng.
    *   **Requestor:** Onkar Bamane.
*   **Action:** Follow up on the specific Pre-order FOC process and resolve the UAT discrepancy.
    *   **Owner:** Sathya Murthy Karthik (Support: Prajney Sribhashyam).
*   **Action:** Provide the default icon asset to resolve the iOS repository discrepancy.
    *   **Owner:** Sip Khoon Tan.

### Key Dates & Deadlines
*   **March 5–17, 2026:** Initial threads on "Offline preorder receipt," UAT findings, and FOC logic clarification.
*   **March 13, 2026 (02:33 AM):** Daryl Ng reported UAT issues regarding missing BCRS deposits for FOC SKUs.
    *   *References:* PDA Receipt (`1G4t5GYI6iTsabjuNHHqEDqbMlDB6ImZr`), POS Receipt (`1hqtxOUysbUNtTT7CW48RPXZ6dEfN-2Dc`).
*   **March 13, 2026 (05:17 AM):** Sathya acknowledged findings and initiated action.
*   **March 17, 2026 (09:45 AM):** Piraba flagged outdated iOS icon via Jira ticket **DPD-657**.
*   **March 24, 2026 (03:17 AM):** Teri Ong Qiu Mei raised the "Scan & Go" SKU substitution query.
*   **March 25, 2026 (04:17 AM – 04:18 AM):** Onkar Bamane requested ECOM UAT sign-off and shared the deployment guide.

### Summary of Findings
While previous discussions confirmed POS limitations on $0 RSP items and established SOPs for in-store pre-orders, a new critical risk has emerged regarding "Scan & Go" operations. Teri Ong Qiu Mei identified that current controls may allow customers to scan old SKUs while taking new ones to evade the 10-cent fee; Prajney Sribhashyam is investigating this specific substitution logic. Concurrently, the ECOM UAT process has moved forward with Onkar Bamane requesting sign-off from Lai Shu Hui, Wei Fen Ching, and Jesslin Lim Bee Leng based on the shared enhancement document. The iOS asset update (Jira **DPD-657**) remains an active but secondary item.


## [80/85] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/qx4BVM7nI60 | Last Activity: 2026-03-25T02:49:25.303000+00:00 | Last Updated: 2026-03-25T06:51:30.795620+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Lead/Coordinator (Overseeing war room creation and sign-off).
*   **Zaw Myo Htet:** Backend/Data Specialist (Validated SAP-DBP sync logic).
*   **Jonathan Tanudjaja:** Frontend Developer (Resolved UI discount bug; deployed fix to UAT).
*   **Andin Eswarlal Rajesh:** Frontend Lead (Confirmed root cause analysis and BO display alignment).
*   **Daryl Ng:** Stakeholder (Monitoring synchronization status).
*   **Sathya Murthy Karthik:** New participant requested for re-testing assistance by Jonathan.

**Main Topic**
Urgent resolution of high-priority "Staff App" issues, specifically the PWP UI bug where offers/discounts failed to display. While initial discussions on March 24 focused on debugging and logging tickets, the focus has now shifted to verification of the deployed fix with expanded testing support.

**Decisions & Findings**
*   **Data Sync (ZOTO):** Confirmed earlier that production data syncs between SAP and DBP are functioning correctly; no backend issue exists.
*   **Root Cause (PWP/UI):** Identified as a legacy implementation flaw where the Frontend incorrectly calculated discounts by selecting only the "first item" in an array. No recent pricing logic changes were made.
*   **Implementation Status:** Jonathan Tanudjaja has completed the fix for ticket **DPD-811**. The code is live in the **UAT** environment as of early morning March 25 (02:17 UTC).

**Pending Actions & Ownership**
1.  **Collaborative Re-testing:** @Jonathan Tanudjaja has explicitly requested assistance from **@Sathya Murthy Karthik** to aid in re-testing the fix on UAT.
2.  **Re-verify Fix (Urgent):** @Prajney Sribhashyam remains responsible for final re-verification of discount display functionality and securing stakeholder sign-off.
3.  **Final Sign-off:** Pending successful UAT verification, the "war room" meeting scheduled for late March 24 will now serve to finalize closures.
4.  **Ticket Closure:** Once re-verification is confirmed by Prajney (and Sathya), ticket **DPD-811** will be marked as resolved.

**Timeline & Deadlines**
*   **Date:** March 25, 2026.
*   **Previous Estimate:** Jonathan initially estimated a 1–2 day effort window.
*   **Current Status:** Fix deployed to UAT as of early morning March 25 (02:17 UTC). Re-testing phase initiated with additional support from Sathya Murthy Karthik.
*   **Immediate Goal:** Complete re-verification in UAT to close the Staff App issue immediately.

**Archived Context**
*   *Original Ticket Creation:* Ticket **DPD-811** was logged on March 24 to address the display logic error.
*   *Root Cause Clarification:* Andin Eswarlal Rajesh confirmed that the "after paid" implementation aligns with BO displays and final invoices, validating the fix approach.
*   *Note:* A message deleted by its author at 04:10 UTC on March 25 has been excluded from active findings as it contains no actionable data.


## [81/85] Chee Keong Ng
Source: gchat | Group: dm/_6kv2MAAAAE | Last Activity: 2026-03-25T03:39:13.286000+00:00 | Last Updated: 2026-03-25T06:52:41.751007+00:00
**Daily Work Briefing: FileVault Encryption Coordination**

**Key Participants & Roles**
*   **Michael Bui:** Requestor/Employee (Requires FileVault encryption setup).
*   **Chee Keong Ng:** IT Support Coordinator/Administrator.
*   **Adi:** Technician at Level 15 Geek Squad who will perform the task.

**Main Topic**
Coordination of a Macbook FileVault encryption appointment for Michael Bui, necessitated by a full-day meeting schedule tomorrow (March 26, 2026). The discussion focused on rescheduling the time slot and providing specific location instructions.

**Decisions Made**
*   **Time Slot:** Michael will attend after 14:00 (avoiding the 13:00–14:00 window).
*   **Location & Contact:** Michael is directed to proceed directly to L15 Geek Squad upon arrival and request assistance from Adi.
*   **Process Specification:** Michael must explicitly state the requirement to "enable Macbook Filevault" when meeting Adi.

**Pending Actions & Ownership**
*   **Action:** Attend Geek Squad for encryption setup today (March 25, 2026) after 14:00.
    *   **Owner:** Michael Bui.
*   **Action:** Perform FileVault enablement on Michael's Macbook.
    *   **Owner:** Adi (via L15 Geek Squad).

**Key Dates & Follow-ups**
*   **Appointment Date:** Today, March 25, 2026.
*   **Time Constraint:** Avoid the 13:00–14:00 slot; arrival required after 14:00.
*   **Estimated Duration:** Chee Keong Ng confirmed the process takes approximately 10 minutes.
*   **Next Step (Contextual):** Michael previously noted an original appointment scheduled for tomorrow (March 26, 2026) was cancelled/rescheduled to today due to his full-day meeting.


## [82/85] 📢 COM Notifications
Source: gchat | Group: space/AAAAu4WIubc | Last Activity: 2026-03-25T03:30:24.297000+00:00 | Last Updated: 2026-03-25T06:53:12.271257+00:00
**Daily Work Briefing: SonarCloud Quality Monitoring**

**Key Participants & Roles**
*   **gautam-ntuc**: Developer; responsible for `catalogue-job` commits.
*   **Shiva Kumar Yalagunda Bas**: Developer; authored recent `supplier-job` changes (PRs #439, #440).
*   **bitbucket-pipelines**: Automated CI/CD bot triggering merges and deployments.
*   **System/Webhook Bot**: Continues reporting recurring "Webhook Bot is unable to process your request" errors across all notifications.

**Main Topic**
Automated SonarCloud quality gate scans for `catalogue-job`, `fpon-sap-jobs`, `seller-proxy-service`, `supplier-job`, and `fni-product-license-alert`. The conversation tracks code coverage, pipeline retries, and the resolution of failing Quality Gates.

**Status Summary by App**
*   **`catalogue-job` (gautam-ntuc)**: Addressed temporary logic to skip SKUs not in DBP. Coverage fluctuated previously but stabilized via refactoring.
*   **`fpon-sap-jobs`**: Deployed to UAT on March 9. Coverage at 72.7%; Unit Test Success reported at 0%.
*   **`supplier-job` (Shiva Kumar Yalagunda Bas)**:
    *   **March 19, 08:28–09:10 UTC**: Two scans for PR #439 and PR #440 (`feature/cutoff_uat`) completed successfully with **90.9%** new code coverage. Status remained **OPEN**.
*   **`seller-proxy-service` (PR-2306 & PR-2330/2331)**:
    *   **March 19–20**: Volatility observed with multiple failure/recovery cycles (details omitted for brevity; previously resolved via retry).
    *   **March 25, 02:50 UTC**: PR-2330 (ver. `7f365a4`) **FAILED** with **97.8%** new code coverage.
    *   **March 25, 03:15 UTC**: PR-2331 (ver. `decab7c`) scanned successfully with **100.0%** coverage (**PASSED**).
    *   **March 25, 03:20–03:30 UTC**: Subsequent scans for PR-2330 recovered. Status updated to **PASSED** by 03:20 UTC (ver. `7f365a4`) and confirmed again at 03:30 UTC (ver. `7746f01`), maintaining **97.8%** coverage.
*   **`fni-product-license-alert`**: Scans on March 20 (PR-1433 and PR-1450) achieved **PASSED** status with 94.4% new code coverage.

**Pending Actions & Ownership**
*   **System Error Investigation**: The "Webhook Bot is unable to process your request" error persists in every notification from March 5 through the latest scans on March 25 (including `supplier-job`, `seller-proxy-service` PR-2330/2331). No specific owner assigned; requires immediate engineering attention.
*   **`fpon-sap-jobs` Unit Tests**: Discrepancy between 72.7% coverage and 0% unit test success requires review by the respective team.

**Decisions Made**
*   Recent merges in `supplier-job` (PRs #439, #440) and recovery scans for `seller-proxy-service` were accepted automatically following retries.
*   **March 25 Action**: Quality Gate failures for `seller-proxy-service` PR-2330 resolved via automated retries within minutes of the initial failure at 02:50 UTC. No manual interventions recorded; pipelines successfully recovered the gate to **PASSED** status by 03:20 UTC.

**Key Dates & Timeline**
*   **March 5**: Initial scan failures in `catalogue-job`.
*   **March 9**: UAT deployment for `fpon-sap-jobs`; initial failure for `seller-proxy-service` PR-2318.
*   **March 12**: `seller-proxy-service` first passed after persistent failures; coverage stabilized above 95%.
*   **March 16 & 20**: Successful scans for `fni-product-license-alert` (PRs #1433, #1450) with 94.4% coverage.
*   **March 19**: 
    *   `supplier-job` PRs #439/#440 scanned successfully at 90.9% coverage.
    *   `seller-proxy-service` PR-2306 showed multiple failure/recovery cycles (failures at 13:38, 08:40; passes at 08:45, 09:11).
*   **March 20**: `seller-proxy-service` PR-2306 failed again at 04:58 UTC (91.8% coverage) but passed immediately at 05:00 UTC.
*   **March 25**: 
    *   **02:50 UTC**: `seller-proxy-service` PR-2330 failed (97.8% coverage).
    *   **03:15 UTC**: `seller-proxy-service` PR-2331 passed (100.0% coverage).
    *   **03:20–03:30 UTC**: `seller-proxy-service` PR-2330 recovered to **PASSED** status with 97.8% coverage.


## [83/85] DPD x Platform Engineering
Source: gchat | Group: space/AAQAcjNXKpA | Last Activity: 2026-03-25T03:27:46.240000+00:00 | Last Updated: 2026-03-25T06:54:40.768434+00:00
**Daily Work Briefing: DPD x Platform Engineering**
*(Updated with March 25, 2026 SLO Alerts & PR Review)*

**Key Participants & Roles**
*   **Madhawa Mallika Arachchige:** On-call restructuring lead.
*   **Alvin Choo:** Team Lead/Organizational structure owner.
*   **Michael Bui:** Stakeholder for RMN on-call grouping.
*   **Kyle Nguyen:** Infrastructure/Platform Engineering (Reviewer, Incident Triage).
*   **Sampada Shukla:** Reliability Engineer (Incident lead for Picking App).
*   **Wai Ching Chan:** Operations/On-call liaison.
*   **Daryl Ng:** Incident Analyst / Automation query responder.
*   **Akash Gupta:** User reporting Bastion access failure; proposing IaC policy change; PR reviewer requestor.
*   **Nicholas Tan, Harry Akbar Ali Munir:** Engaged in Bastion and Cluster capacity investigations.
*   **Dodla Gopi Krishna:** SLO performance monitoring lead.
*   **Tiong Siong Tee:** Stakeholder for Pricing SLO degradation.

**Main Topics & Discussions**
1.  **Critical Picking App & Backoffice Incident (March 23):** Sampada Shukla reported significant issues starting at 03:40 PM SGT on March 23. Operations observed `SocketTimeoutExceptions` on Android and `Connection Resets` on the Web between 03:40–03:45 PM SGT.
    *   *Root Cause Analysis:* GKE logs indicate the cluster (`jarvis-prod-ap-v2`) reached hard memory limits at 15:22 SGT (0/6 nodes available). At 15:39 SGT, Kubernetes initiated forced pod evictions of `picking-service` pods due to extreme memory pressure.
    *   *Impact:* Forceful eviction severed active network sockets, causing the observed timeouts and resets.
    *   *Context:* This follows a previous March 9 incident involving load balancer churn; current findings point to cluster capacity scaling limits rather than LB updates.
2.  **SLO Performance Degradation (March 25):** Dodla Gopi Krishna notified the team of SLO degradation over the last month affecting two tribes:
    *   **Fulfillment Tribe:** Error budget remaining is critically low (Datadog Dashboard `3hw-j87-f9j`).
    *   **Pricing Tribe:** Alert regarding `dept:dpd tribe:pricing` error budget status.
    *   *Discussion:* Daryl Ng queried if these notifications were automated; Akash Gupta acknowledged the alerts and noted they require attention.
3.  **On-Call Restructuring Methodology Debate:** Akash Gupta proposed shifting new on-call configuration from Terraform (IaC) to direct Datadog UI management to facilitate manual overrides and reduce PR overhead. The team is reviewing this proposal against the strict two-PR Terraform process.
4.  **Security & Dependency Updates:** Lester Soriano upgraded `lt-strudel-api-go` for vulnerability `GO-2026-4603` but encountered pipeline failures due to a `golangci-lint` version mismatch (v1.24 build vs v1.25.8 target).
5.  **Security & Infrastructure:** Akash Gupta reported Bastion unavailability in PROD (`asia-southeast1-c`). Natalya Kosenko flagged potential manual deletion of Datadog resources causing Terraform drift.

**Pending Actions & Owners**
*   **Resolve Cluster Capacity Scaling:** Investigate why the cluster failed to scale out during peak traffic (03:40 PM SGT) and implement fixes for memory limits. *(Owners: Kyle Nguyen, Nicholas Tan)*
*   **Investigate SLO Degradation:** Address error budget consumption in Fulfillment and Pricing tribes. *(Owner: Dodla Gopi Krishna, relevant service owners)*
*   **Evaluate On-Call Tooling Strategy:** Assess Akash Gupta's proposal to use Datadog UI instead of Terraform for new on-call teams. *(Owner: Platform Engineering)*
*   **Restore Bastion Access:** Investigate PROD `asia-southeast1-c` Bastion inaccessibility affecting order republishing. *(Owners: Nicholas Tan, Kyle Nguyen, Harry Akbar Ali Munir)*
*   **Resolve Go Pipeline Error:** Reconcile `golangci-lint` version mismatch for Lester Soriano.
*   **Review Infrastructure PR:** Natalya Kosenko's PR `infra-gcp-fpg-titan/344` requires review from Kyle, Nicholas, Madhawa, and Dodla Gopi Krishna.
*   **Review Monitoring PR:** Akash Gupta requests reviews for PR #917 (`dpd-datadog-monitoring`) to change p90 cancel noncritical alert threshold; rationale is that critical alerts already exist on p99. *(Owners: Madhawa Mallika Arachchige, Dodla Gopi Krishna)*
*   **Plan Resource Scale-Down:** Daryl Ng to coordinate with Kyle Nguyen, Maou Sheng Lee, and Alvin Choo regarding QC Food resource reduction pending ES confirmation.

**Decisions Made**
*   *Tentative:* The team is debating whether to retain the Terraform-based change-freeze process or adopt direct Datadog UI management for on-call teams. No final decision recorded yet.
*   **QC Food Status:** Disabling confirmed on production (as of March 19). Resource scale-down planning initiated pending ES confirmation.

**Key Dates & Follow-ups**
*   **March 25, 03:15 AM UTC:** Dodla Gopi Krishna alerted on Fulfillment SLO degradation.
*   **March 25, 03:16 AM UTC:** Alert raised on Pricing Tribe SLO performance.
*   **March 25, 03:27 AM UTC:** Akash Gupta submitted PR #917 for review regarding p90 cancel monitoring changes.
*   **March 23, 03:40–03:45 PM SGT:** Critical incident involving `SocketTimeoutExceptions` and `Connection Resets` due to GKE memory exhaustion.
*   **March 16, 08:58 UTC:** Akash Gupta submitted proposal to replace Terraform with Datadog UI.
*   **March 19, 11:47 AM SGT:** Daryl Ng confirmed QC Food tile disabled on production.


## [84/85] QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs/YgGvvuD2Ow8 | Last Activity: 2026-03-25T03:19:09.666000+00:00 | Last Updated: 2026-03-25T06:56:20.482439+00:00
**Daily Work Briefing: Ad Slot Configuration Changes (QE <-> All Tribes)**

**Key Participants & Roles**
*   **Michael Bui:** Initiator of the change; responsible for managing the change window and subsequent reset.
*   **Komal Ashokkumar Jain:** Stakeholder managing testing timeline and impact analysis.
*   **Milind Badame:** Notified stakeholder monitoring UAT status and E2E test failures.

**Main Topic**
Discussion regarding temporary modifications to ad slot positions in swimlanes, specifically the impact on User Acceptance Testing (UAT) scripts hardcoded to positions 1 and 3.

**Decisions Made & Status Updates**
*   Ad slots were reconfigured temporarily during the testing phase, causing existing UAT tests tied to positions 1 & 3 to fail.
*   The system remains in its modified configuration pending final UAT completion; it has not yet reverted to original positions (1 & 3).
*   **Current Status:** As of March 25, E2E tests involving the hardcoded positions continue to fail. Milind Badame confirmed that these specific test cases will be ignored until the next update is provided by Michael Bui.

**Pending Actions & Ownership**
*   **UAT Completion Confirmation:** Following Michael Bui's March 24 confirmation that testing was "not fully completed yet," Milind Badame acknowledged this on March 25, noting persistent E2E failures. The team has agreed to skip these failing tests temporarily rather than halting progress.
*   **Execution Oversight:** Michael Bui retains responsibility for managing the extended change window and executing the ad slot reset (back to positions 1 & 3) immediately upon UAT finalization. No new reset date has been established pending further updates.

**Key Dates, Deadlines & Follow-ups**
*   **Original Start Date:** March 12, 2026 (Changes active "starting today").
*   **Query Date:** March 24, 2026 (Milind Badame asked if UAT was completed).
*   **Response Date/Timestamp:** March 24, 2026 at 08:44 UTC (Michael Bui replied: "It's not fully completed yet").
*   **Acknowledgment Date:** March 25, 2026 at 03:19 UTC (Milind Badame confirmed receiving the update and noted ongoing E2E failures).
*   **Scheduled End Date (Original):** End of Next Week (March 19, 2026). *Note:* This deadline has passed; testing remains incomplete.

**Summary of Chronology**
On March 12, 2026, Michael Bui informed the group that ad slot changes were underway, warning that UAT tests hardcoded for positions 1 and 3 would fail. Komal Ashokkumar Jain inquired about the End Time (ETA), with Michael confirming the activity would conclude by "next week EOW."

On March 24, 2026, Milind Badame initiated a follow-up asking if UAT was completed. Contrary to expectations, Michael Bui responded at 08:44 UTC stating, "It's not fully completed yet." Consequently, the original end date of March 19 is superseded by the ongoing status.

On March 25, 2026, Milind Badame acknowledged Michael's update via chat. He confirmed that E2E failures persist in those specific slots and stated explicitly: "We are still seeing failures in those E2E, so we will continue to ignore those until your next update." The ad slot configuration remains active in its modified state, with the reset protocol dormant pending a final confirmation from Michael Bui.


## [85/85] Release - FPG Back Office (Mon-Thurs)
Source: gchat | Group: space/AAAAoJgpZBM | Last Activity: 2026-03-25T02:33:49.818000+00:00 | Last Updated: 2026-03-25T02:51:23.397379+00:00
**Daily Work Briefing: FPG Back Office Releases**

**Key Participants & Roles**
*   **Rohit Pahuja:** Primary communicator; responsible for announcing scheduled releases and providing release note links.
*   **Jonathan Tanudjaja:** Confirmed as the executor for the v8.37.1 release.

**Main Topic**
The conversation focuses on confirmed software deployment schedules for the **Back Office** system, covering versions **v8.35.0**, **v8.36.0**, **v8.37.0**, and the newly announced urgent release of **v8.37.1**. These messages notify the team of upcoming maintenance windows aligned with the FPG Back Office (Mon-Thurs) resource schedule.

**Pending Actions & Ownership**
*   **Action:** Monitor the Back Office system during release execution for all scheduled versions.
    *   **Owner:** Team (implied by "Hi team" notifications).
*   **Action:** Review specific release notes for version updates and change logs.
    *   **Owner:** Team members referencing provided links.
*   **New Action:** Execute the deployment of version **v8.37.1** today.
    *   **Owner:** Jonathan Tanudjaja.

**Decisions Made**
No new strategic decisions were made; messages confirm four existing scheduled deployment plans:
1.  Deployment of **Backoffice_v8.35.0**.
2.  Deployment of **Backoffice_v8.36.0**.
3.  Deployment of **Backoffice_v8.37.0** (Previously announced for March 24).
4.  **Deployment of Backoffice_v8.37.1** (Newly confirmed and initiated by Jonathan Tanudjaja on March 25, 2026).

**Key Dates, Deadlines, & Follow-ups**
*   **Release 1:**
    *   **Version:** Backoffice_v8.35.0
    *   **Announced:** March 9, 2026, at 05:11 UTC.
    *   **Scheduled Execution:** Approximately 1:20 PM on March 9, 2026.
    *   **Reference:** [Backoffice_v8.35.0 Release Notes](https://ntuclink.atlassian.net/wiki/spaces/SE/pages/3290431602/Backoffice_v8.35.0)
*   **Release 2:**
    *   **Version:** Backoffice_v8.36.0
    *   **Announced:** March 12, 2026, at 13:44 UTC.
    *   **Scheduled Execution:** Same day (March 12, 2026).
    *   **Reference:** [Backoffice_v8.36.0 Release Notes](https://ntuclink.atlassian.net/wiki/spaces/SE/pages/3304423425/Backoffice_v8.36.0)
*   **Release 3:**
    *   **Version:** Backoffice_v8.37.0
    *   **Announced:** March 24, 2026, at 02:17 UTC.
    *   **Scheduled Execution:** Same day (March 24, 2026).
    *   **Reference:** [Backoffice_v8.37.0 Release Notes](https://ntuclink.atlassian.net/wiki/spaces/SE/pages/3334537232/Backoffice_v8.37.0)
*   **Release 4 (New):**
    *   **Version:** Backoffice_v8.37.1
    *   **Announced:** March 25, 2026, at 02:33 UTC.
    *   **Scheduled Execution:** Today (March 25, 2026) by Jonathan Tanudjaja.
    *   **Reference:** [Backoffice_v8.37.1 Release Notes](https://ntuclink.atlassian.net/wiki/spaces/SE/pages/3340828673/Backoffice_v8.37.1)

**Contextual Notes**
*   These updates align with the resource schedule for **FPG Back Office (Mon-Thurs)**.
*   The v8.37.1 release represents an immediate follow-up to the v8.37.0 cycle, initiated within 24 hours of the previous announcement.
