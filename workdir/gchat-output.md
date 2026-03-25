

## [1/64] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 16 | Last Activity: 2026-03-25T14:18:52.651000+00:00 | Last Updated: 2026-03-25T14:37:13.194311+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (Updated March 25, 14:18 UTC)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
Following the March 21 incident and critical surges on March 24, volatility persists into **March 25 between 05:58 and 14:18 UTC**. The issue has evolved from isolated latency to a synchronized instability loop. While some services recovered mid-afternoon (e.g., `gamification-api` at 14:00), new spikes in `engage-my-persona-api-go` errors and MyInfo latency emerged at **14:02–14:18 UTC**, indicating a recurring cycle rather than full resolution.

**Status Summary & Timeline (Extended Incident)**
*   **Service Error Rates (`engage-my-persona-api-go`):**
    *   Recurring high error alarms (>0.1%) triggered multiple times between **05:58–06:27 UTC**, **10:04 UTC**, and resurfaced at **14:02 UTC** (Peak: 0.105%) and **14:14 UTC** (0.107%).
    *   Monitor #92965074 shows alternating Trigger/Recovered states throughout the morning, with a final recovery observed at **14:12 UTC**.
*   **MyInfo & User Data Latency:**
    *   **`post_/new-myinfo/confirm`:** P90 spikes (>1.8s) observed at **06:00**, **06:24**, and **10:29 UTC**. A new spike detected at **14:08 UTC** (1.888s), recovering by **14:18 UTC**.
    *   **`put_/user/email`:** P90 latency spike (>2.5s) triggered at 10:20 UTC; no recent alerts reported for this endpoint in the new data.
*   **Frontend Gateway & Downstream Impact:**
    *   `frontend-gateway`: `orchid` recommendation failures (<99.9%) triggered at **10:04**, recovered, then re-triggered at **14:01 UTC** (99.655% success), recovering by **14:11 UTC**.
    *   `lyt-p13n-layout`: P99 latency spike (>1.8s) detected at 10:04 UTC; a new trigger occurred at **13:53 UTC** (2.009s), recovering by **14:01 UTC**.
    *   `gamification-api`: High error rate triggered at **13:50 UTC** (0.366%), recovered by **14:00 UTC**.
    *   `ef-android` (Compass): Android user linkpoints load failure (<99.9%) triggered at **13:54 UTC** (99.39% success), recovered by **13:57 UTC**.

**Pending Actions & Ownership**
*   **Investigate Recurring Latency Loops:** Immediate RCA required for the repeated spikes in `engage-my-persona-api-go` errors and MyInfo confirm latency observed between **14:02–14:18 UTC**. Owner: **Squad Dynamics/Journey**.
*   **Analyze Downstream Effects:** Investigate correlation between `gamification-api` error spike (13:50) and simultaneous latency in `lyt-p13n-layout` (13:53). Owner: **Squad Journey/Dynamics**.
*   **Frontend Gateway Stability:** Monitor intermittent `orchid` recommendation failures; note the recurrence at 14:01 UTC. Owner: **Squad Journey/Dynamics**.

**Decisions Made**
*   **Severity Maintenance:** Incident severity remains high due to the persistence of instability loops past midday, specifically the re-emergence of `engage-my-persona-api-go` errors and MyInfo latency at 14:08 UTC.
*   **Pattern Continuity:** Activity confirms a synchronized instability affecting core engagement flows (`gamification`, `MyInfo`) and downstream frontend components throughout the afternoon window.

**Key Dates & Follow-ups**
*   **Active Window:** March 24–25 (UTC+8). Recent critical activity: **13:50 – 14:18 UTC** (March 25).
*   **Reference Links (Updated):**
    *   `gamification-api` Error Monitor #92939290 (Peak: 0.366% @ 13:50)
    *   `lyt-p13n-layout` P99 Latency Monitor #20382854 (Triggered @ 13:53, Peak: 2.009s)
    *   MyInfo P90 Monitor #50879027 (New Spike: 1.888s @ 14:08)
    *   `orchid` Success Rate Monitor #17448311 (Re-triggered @ 14:01, Recovered @ 14:11)
    *   Android Linkpoints Monitor #63109467 (Triggered @ 13:54)


## [2/64] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/o4m2XO8j1K0 | Messages: 26 | Last Activity: 2026-03-25T14:17:11.526000+00:00 | Last Updated: 2026-03-25T14:37:34.545953+00:00
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


## [3/64] Video & Product Ads Working Group
Source: gchat | Group: space/AAQAeSWRtgQ/RZyBk6LBi14 | Messages: 10 | Last Activity: 2026-03-25T14:09:34.340000+00:00 | Last Updated: 2026-03-25T14:37:56.987677+00:00
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


## [4/64] Google Drive
Source: gchat | Group: dm/7d1XKcAAAAE | Messages: 4 | Last Activity: 2026-03-25T14:06:37.786000+00:00 | Last Updated: 2026-03-25T14:38:32.514566+00:00
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


## [5/64] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Messages: 25 | Last Activity: 2026-03-25T13:46:31.220000+00:00 | Last Updated: 2026-03-25T14:38:56.033305+00:00
**Daily Work Briefing: Nikhil Grover & Michael Bui**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator; confirmed fix for ranking issue, managing deployment request and stakeholder timeline updates.
*   **Michael Bui:** Technical Lead (Engineering); now available for immediate deep-dive via video meeting to finalize deployment decisions.
*   **Flora:** Frontend resource; raised a specific concern regarding the analytics payload that requires investigation.

**Main Topics**
1.  **Ad Delivery Inconsistency & Deployment Impact:**
    *   **Ranking Issue Status:** The erratic ranking orders on homepage swimlanes (ranks 4, 9, and 1) have been confirmed as **fixed**. Nikhil Grover requested immediate deployment to resolve the issue today.
    *   **Analytics Payload Concern:** Flora raised a new point regarding the analytics payload that requires further investigation before full confidence in the fix is achieved.

2.  **Deployment & Stakeholder Communication:**
    *   A video meeting was convened at **13:37 UTC** on March 25 to discuss deployment and stakeholder timelines.
    *   Deployment remains contingent on addressing Flora's analytics payload concern and securing technical consensus during the current session.

**Decisions Made & Status Updates**
*   **Deployment Readiness:** The core ranking anomaly is resolved; however, the path to deployment is paused pending review of the analytics payload issue raised by Flora.
*   **Investigation Pivot:** While the initial redirect to Norman/Flora for event details remains relevant regarding the root cause history, immediate focus has shifted to validating the analytics payload fix during the current video call.
*   **Meeting Status:** Michael Bui is now actively participating in a Google Meet session (link provided below) to replace the previously requested brief meeting at 04:01 UTC for finalizing stakeholder communications.

**Pending Actions & Owners**
*   **Analytics Payload Verification (Nikhil Grover/Flora):** Investigate Flora's concern regarding the analytics payload during the current video call to ensure no `Ad ID` or metadata gaps persist post-fix.
*   **Deployment Authorization:** Await final confirmation from Michael Bui and technical consensus reached in the video meeting to proceed with the requested "today" deployment.
*   **Stakeholder Timeline Update (Nikhil Grover):** Communicate deployment status and timeline to stakeholders immediately following the conclusion of the 13:37 UTC meeting.

**Key Dates & Deadlines**
*   **March 25, 2026:**
    *   **03:58 UTC:** Nikhil Grover confirmed the rank issue is fixed and requested deployment.
    *   **04:01 UTC:** Original request for a brief meeting with Michael Bui to finalize stakeholder timeline updates (superseded by current session).
    *   **13:37 UTC:** Video meeting initiated between Nikhil Grover and Michael Bui to address the analytics payload concern and deployment authorization.

**Historical Context Note**
Previous discussions established readiness for dynamic slots UAT with resolved `[1,3,3,5]` logic. Focus shifted to a critical ad delivery anomaly (Store ID mismatch) on March 19–20. On March 24, the narrative evolved: while OSMOS sync was confirmed as manual and the Store ID issue downgraded by Nikhil Grover as an edge case, Michael Bui maintained the need for further investigation. Later that afternoon, the scope expanded when Nikhil Grover identified a new critical failure in product ad placements on homepage swimlanes, characterized by random ranking orders (1, 4, 9) and missing `Ad ID` fields in Segment events. On March 25 morning, the situation progressed: Nikhil Grover confirmed the rank fix but introduced a potential blocker raised by Flora regarding analytics payloads. Consequently, while deployment is requested for today, the process is waiting on payload verification and technical consensus. The team has now transitioned from asynchronous delays to an active video discussion (13:37 UTC) to resolve these blockers.

**Meeting Link:**
*   **Google Meet:** https://meet.google.com/gwr-efmg-pfd?hs=146


## [6/64] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-03-25T13:42:25.572000+00:00 | Last Updated: 2026-03-25T14:39:32.617906+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Update)**
**Date:** March 25, 2026 (Afternoon)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 372

### Key Participants & Roles
*   **System/Tool:** Datadog App (Automated Monitoring)
*   **Notification Channel:** `@hangouts-ShoppingCartNotification`
*   **Ownership Teams:** `dpd-pricing`, `dpd-pricing-cart`.

### Main Topic
Instability in `frontend-gateway` continues to exhibit extreme high-frequency oscillation between trigger and recovery states. The issue has expanded to include significant latency spikes in `st-cart-prod` (S&G post cart), confirming a systemic failure affecting the full user journey (Read, Write, Cart Update, and Checkout). Activity persists through 13:42 UTC on March 25.

### Incident Timeline & Actions
**Previous Context:**
*   *Activity from March 20–09:59 UTC regarding `frontend-gateway` latency, wish list degradation, and checkout dips.*

**New Activity (March 25, UTC+0)**
*   **11:08–11:17 UTC:** `post /api/cart` P99 spiked to **3.006s** (>2.6s threshold) on `frontend-gateway`. Recovered to 0.83s (Monitor ID `21245713`).
*   **12:22–12:31 UTC:** Rapid oscillation detected across two services:
    *   `post /api/cart` P99 on `frontend-gateway` spiked to **4.099s** (Monitor ID `21245713`).
    *   `st-cart-prod` `post /cart` P99 spiked to **4.036s** (>2.6s threshold) before recovering to 1.0s (Monitor ID `22710473`).
*   **12:43–12:44 UTC:** `put_/api/product/_id_/wish-list` P90 on `frontend-gateway` spiked to **5.093s** (>5s threshold). Recovered to 1.302s (Monitor ID `21245706`).
*   **13:34–13:42 UTC:** `get_/api/wish-list/_id` P90 on `frontend-gateway` oscillated between triggering (>1.7s, max 1.775s) and recovering (min 1.282s). Four distinct trigger/recovery cycles observed within 8 minutes (Monitor ID `21245720`).

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** The failure pattern has intensified to include the core `st-cart-prod` service (`post /cart`) alongside existing `frontend-gateway` instability. The frequency of triggers (multiple per minute) confirms a systemic bottleneck in shared dependencies rather than isolated service failures.
*   **Scope:** Immediate correlation required between the 12:22 UTC double-trigger events on `frontend-gateway` and `st-cart-prod`. Investigate database contention, resource saturation, or shared dependency bottlenecks causing P99/P90 spikes across all cart operations.

### Decisions Made
*   **Priority Escalation:** Status remains **"Critical Incident"**. Activity extends from March 20 through at least March 25, 13:42 UTC, with no stabilization observed.
*   **Focus Shift:** Prioritize analysis of the new `st-cart-prod` latency vector (Event ID `8559375021152460907`) alongside recurring `frontend-gateway` oscillations.

### Key Dates & Follow-ups
*   **Critical Window:** Extended activity from March 20 through at least March 25, 13:42 UTC.
*   **Follow-up:** Analyze Event IDs `8559299856184365311` (Cart P99), `8559375021152460907` (S&G Cart P99), `8559395371467916598` (Wish List Put), and `8559446954781587639`/`8559449960637239140` (Wish List Get) to identify common failure vectors.

### References
*   **Active Monitors:** `21245713` (Cart P99 > 2.6s), `22710473` (S&G Cart P99 > 2.6s), `21245706` (Wish List Put P90 > 5s), `21245720` (Wish List Get P90 > 1.7s).
*   **Service Tags:** `service:frontend-gateway`, `service:st-cart-prod`, `team:dpd-pricing`, `tribe:pricing`.


## [7/64] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Messages: 17 | Last Activity: 2026-03-25T13:09:49.959000+00:00 | Last Updated: 2026-03-25T14:40:04.630065+00:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
Automated alerts for the production environment (`env:prod`) continue to show instability in Mirakl integration. Following escalations on March 24, new incidents were recorded later on **March 25**, confirming a persistent cycle of DBP fetch failures and API errors affecting `fni-order-create`.

**Incident Summary & Timeline (2026-03-15 to 2026-03-25)**
*   **Service:** `fni-order-create` (Mirakl Integration) – **Escalated Recurrence on Mar 25 (Afternoon)**
    *   **Pattern Continuation:** Instability spans March 17–25. A new incident window occurred midday **March 25**.
    *   **Afternoon Incident (Mar 25, ~13:04 UTC):** Two distinct P2 triggers initiated simultaneous alerts for "Exception Occurred At Mirakl Route" and "Error while calling APIs".
        *   Both monitors triggered at **13:04:40 UTC** (`Monitor ID: 17447918`) and **13:04:50 UTC** (`Monitor ID: 17447928`) respectively.
        *   Logs confirmed `>1` event match for both queries within a 5-minute window.
    *   **Recovery:** Monitors returned to normal by **13:09:40 UTC** and **13:09:49 UTC**. Total duration was approximately **5 minutes**.
    *   **Context:** This follows the morning cluster on Mar 25 (approx. 08:22 UTC) and four distinct error clusters recorded between 18:49–20:04 UTC on March 24.

*   **Service:** `seller` (`picklist-pregenerator`) – **Recurring Latency**
    *   **Cycle (Mar 20):** P2 warning with metric value **3611.453s**.
    *   **Cycle (Mar 23):** New P2 warning triggered at **23:01:22 UTC** with metric value **3607.424s** (Monitor ID `20383097`).
    *   **Latest Update (Mar 24, ~23:01 UTC):** A new P2 warning triggered for the same service detecting excessive completion time (metric value **3607.798s**, Monitor ID `20383097`).
    *   **Note:** No new latency alerts reported for March 25 in the provided feed; focus remains on Mirakl integration.

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of expanded Mirakl integration instability affecting `fni-order-create`. The pattern now includes multiple recurrence windows: Mar 17–23 history, four clusters on Mar 24, an early-morning cluster on Mar 25 (08:22 UTC), and a new midday cluster at **13:04 UTC**.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Investigate root cause of extreme latency spikes in `picklist-pregenerator`. Cycles occurred on March 20 (3611s), March 23 (3607s), and March 24 (3607.798s). Confirm if the Mar 25 morning window impacts job processing logic.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Review Monitor `29851723` logic for Apple Pay/Google Pay transactions following the March 23 test alert indicating potential false positives.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Summary for Leadership**
Mirakl integration instability (`fni-order-create`) has persisted across nine consecutive days (March 17–25). On March 25, the service exhibited two recurrence windows: one at **08:22 UTC** and a second at **13:04 UTC**. Both incidents triggered simultaneous P2 alerts for Mirakl route exceptions and API errors, resolving within roughly 5 minutes each. This follows four separate incident windows on March 24. Concurrently, `picklist-pregenerator` shows a continuous cycle of critical latency spikes on March 20 (3611s), March 23 (3607s), and March 24 (3607.798s). These systemic failures in Mirakl, SAP, and job processing logic require urgent engineering review to stabilize production performance.

**Resource:** fairnex-datadog-notification
**Metadata:** { "message_count": 126, "url": "https://chat.google.com/space/AAAA8dv5lp0" }


## [8/64] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Messages: 15 | Last Activity: 2026-03-25T13:00:32.436000+00:00 | Last Updated: 2026-03-25T14:40:38.025548+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Mar 25, 13:01 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-discovery`.
*   **Escalations:** `@hangouts-GT-Search-DatadogAlerts`, `@oncall-dpd-staff-excellence-pdm`, `@hangouts-GT-Discovery-DatadogAlerts`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Search Indexing.

**Main Topic**
**P3 ALERT (Flapping):** The `go-catalogue-service` exhibits severe latency instability on the `get_/category/_id` endpoint in production. Following spikes earlier today, the alert cycled between triggered and recovered states multiple times before stabilizing at 13:00 UTC.

**Pending Actions & Ownership**
*   **Action:** **RESOLVE LATENCY FLAPPING:** Address P90 latency spikes > 2000ms for `get_/category/_id`.
    *   **Owner:** Discovery Team (`@hangouts-GT-Discovery-DatadogAlerts`) & Product Data Management (`@opsgenie-dpd-staff-excellence-pdm`).
    *   **Status:** **RECOVERED (13:00 UTC).** The alert has cycled states on Mar 25 with the following sequence:
        *   Triggered 07:14 UTC, Recovered shortly after.
        *   Triggered 07:28 UTC (p90: 2.42s), Recovered 07:29 UTC.
        *   Triggered **08:38 UTC** (p90: 3.214s), Recovered 09:18 UTC.
        *   **Triggered 10:39 UTC** (p90: **2.794s**).
        *   **Recovered 13:00 UTC** (p90: **0.746s**).
    *   **Required Checks:** Review Datadog logs, inspect K8s deployment (`fpon-cluster/default/go-catalogue-service`), and consult Runbook.

*   **Action:** **PERSISTENT INVESTIGATION:** Address critical errors on `fp-search-indexer` (env: prod).
    *   **Owner:** Product Data Management On-Call (`@oncall-dpd-staff-excellence-pdm`).
    *   **Status:** Active since Mar 18. Last re-triggered Mar 24, 16:29 UTC. No resolution achieved.

*   **Action:** Monitor `sku-store-attribute` job stability.
    *   **Owner:** DPD Grocery Discovery Team (`@hangouts-dd-dpd-grocery-alert`).
    *   **Status:** Persistent instability observed Mar 23–24. Last recovery at 01:01 UTC Mar 24.

**Decisions Made**
*   `go-catalogue-service` latency on `get_/category/_id` has shown a final spike of **2.794s** (p90) at **10:39 UTC**, followed by recovery to **0.746s** (p90) at **13:00 UTC**. The alert is currently stable, but the frequency of flapping confirms a persistent underlying instability requiring root cause analysis.
*   `fp-search-indexer` failure remains persistent since Mar 18; root cause analysis is critical.
*   `sku-store-attribute` shows frequent oscillation; further investigation into job dependencies is needed.

**Key Dates & Follow-ups (Mar 16–25, 2026)**
*   **Service: `go-catalogue-service` (P3 - Discovery/Product Data) [FLAPPING]**
    *   *Latest Timeline:* Alert cycled between Triggered and Recovered states from 07:14 to 13:00 UTC on Mar 25. Most recent spike at **10:39 UTC** (p90: 2.794s). Latest recovery at **13:00 UTC** (p90: 0.746s).
    *   *Monitor ID:* `17447967`.
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/17447967) | [K8s Console](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/go-catalogue-service/overview?project=fponprd).
*   **Service: `fp-search-indexer` (P2 - Product Data Management) [ACTIVE CRITICAL]**
    *   *Latest Timeline:* Active since Mar 18; re-triggered Mar 24, 16:29 UTC.
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/17447691) | [Runbook](https://ntuclink.atlassian.net/wiki/spaces/SR/pages/2001831558/Support+Run+book).
*   **Service: `sku-store-attribute` (P3 - Grocery Discovery) [FLAPPING]**
    *   *Latest Timeline:* Last recovery at 01:01 UTC Mar 24. Monitor ID: `20382848`.

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c


## [9/64] Sneha Parab
Source: gchat | Group: dm/50uphEAAAAE | Messages: 2 | Last Activity: 2026-03-25T12:22:51.489000+00:00 | Last Updated: 2026-03-25T14:40:50.812292+00:00
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


## [10/64] DPD AI Guild
Source: gchat | Group: space/AAQA5_B3lZQ/9rNMaZEmMZE | Messages: 6 | Last Activity: 2026-03-25T12:13:58.891000+00:00 | Last Updated: 2026-03-25T14:41:07.560589+00:00
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


## [11/64] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Messages: 6 | Last Activity: 2026-03-25T12:09:22.800000+00:00 | Last Updated: 2026-03-25T14:41:57.254460+00:00
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
*   **Mar 24–25, 2026:** Incident `story_key`: `de0cbb14-ade3-5de2-bfab-cbddd41da779`. Triggered Mar 24 at 22:45 UTC; Recovered Mar 25 at 02:36 UTC. Duration ~3h 51m. Status: **Resolved**.

**Newly Resolved Incident (Mar 25):**
*   **Date:** March 25, 2026.
*   **Time:** Recovered at 12:09 UTC.
*   **Story Key:** `978f6328-424c-53dd-83c8-6411c3aa2158`.
*   **Context:** Previously listed in the "Mar 24 (Old)" entry as triggered at 12:04 UTC. This new data confirms recovery on Mar 25 at 12:09 UTC, extending the duration to approximately 24 hours.
*   **Status:** **Resolved**.

### Pending Actions & Ownership
*   **Immediate Action:** The systemic error "Datadog is unable to process your request" persists across multiple `story_keys`. The recent incident (`978f6328...`) exhibited a significantly longer duration (~24 hours) compared to the Mar 20–25 average (~1.8h to ~3.9h). This deviation suggests potential persistent pipeline degradation rather than standard transient load spikes.
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Investigation Note:** The extended duration of the `story_key` `978f6328-424c-53dd-83c8-6411c3aa2158` (Mar 24–25) requires immediate scrutiny to distinguish between transient spikes and pipeline stability issues.

### Decisions Made
*   **Status:** No escalation triggered yet as the incident has resolved. However, the resolution time (~24h) exceeds the standard historical average (~3-5 hours).
*   **Protocol:** Continue active surveillance. If a new trigger occurs with similar error messaging and resolution time again exceeds recent norms (specifically >6 hours), escalate immediately to SRE/Platform Engineering.

### Key Dates & Follow-ups
*   **Latest Event:** March 25, 2026, at 12:09 UTC (Recovered).
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Monitor for recurrence. The extended duration of the Mar 25 incident is an outlier requiring trend analysis.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Datadog Monitor Link:** [View in Datadog](https://app.datadoghq.eu/monitors/17447511)
*   **Latest Incident (Mar 25 Resolved):** https://app.datadoghq.eu/monitors/17447511?group=story_key%3A978f6328-424c-53dd-83c8-6411c3aa2158&from_ts=1774439571000&to_ts=1774440771000&event_id=8559361398919485850

### Monitor Configuration
*   **Query:** `events("source:watchdog (story_category:infrastructure -story_type:(tcp_retrans_jump OR full_disk_forecast)) env:(PROD OR production OR prod)").rollup("count").by("story_key").last("30m") > 0`


## [12/64] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Messages: 5 | Last Activity: 2026-03-25T12:03:35.798000+00:00 | Last Updated: 2026-03-25T14:46:05.508073+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Sneha Parab:** Lead/Manager; coordinating cross-team support, SAP/API integration blockers, tooling requests, and subscription processes.
*   **Michael Bui:** Engineering/RMN Architect; managing architecture updates, infrastructure compliance, reporting Omni Home swimlane issues, and investigating search performance drops.
*   **Alvin Choo:** Leadership; addressing feedback loops, release schedules, epic queries, AI personalization prioritization, and recent traffic anomalies.
*   **Gopalakrishna Dhulipati:** Lead; overseeing risk registers, delivery approvals, service key rotation with SRE, and clarifying PIC for store purchase surveys.
*   **Others Active:** Daryl Ng (raised OMNI-1157), Andin Eswarlal Rajesh, Olivia, Koklin, Zaw, Ravi.

**Main Topics**
1.  **Critical Search Performance Drop:** Michael Bui flagged a severe decline in impressions on search and category pages (60–70%) since March 18/19. Immediate investigation required to identify if PRD deployments caused this regression. Action involves Daryl Ng, Andin Eswarlal Rajesh, and Alvin Choo.
2.  **SAP/Deposit SKU Integration Blocker:** Marketplace lacks deposit data for SAP API integration. Proposed manual UD failed MP Ops sign-off due to poor PM communication; Olivia rejected new technical solutions. Immediate action from SAP team required.
3.  **Requirement Clarity (BCRS):** Michael Bui flagged that "follow existing ones" is unacceptable acceptance criteria for BCRS deposit posting. Explicit UAT scenarios are required for Definition of Ready (DoR).
4.  **Infrastructure Compliance:** Bitnami ending free Docker images impacts `sonic_raptor` and `mkp-fairnex`. Migration is mandatory.
5.  **Service Key Rotation:** Gopalakrishna Dhulipati requested leads take ownership with the SRE team; discussion moved to a dedicated room.
6.  **B2B Testing Alignment:** Sneha Parab raised queries on finalized B2B testing procedures. Zaw requires guidance on producing MP SKUs specifically for B2B testing.
7.  **New Epic Inquiry (OMNI-1157):** Daryl Ng raised an item from the weekly epics. Ravi indicated this action should only be performed for the new app. Alvin Choo and Gopalakrishna Dhulipati were tagged to clarify status.
8.  **Omni Home Data Discrepancy:** Michael Bui reported a store ID mismatch between Omni Home swimlane and "See All" screen. Team identification remains under investigation (involving Daryl Ng).
9.  **Store Purchase Survey PIC:** Gopalakrishna Dhulipati initiated a query regarding the responsible party for the survey on products purchased at stores.
10. **Scan@Door AI Personalization:** Daryl Ng noted the project lacks PM involvement and requires BE changes; prioritization on the Omni board is under review by Alvin Choo.
11. **1HD Changes & Production Testing:** Andin Eswarlal Rajesh confirmed production testing with leadership is targeted for Friday or Monday. *Note: Search drop investigation may impact this timeline.*
12. **Tooling & Admin (New):** Sneha Parab queried Cursor subscription requests for unsponsored engineers and sought confirmation on current system owners (Discussions concluded March 25).

**Pending Actions & Owners**
*   **Search Performance Investigation:** Identify root cause of 60–70% impression drop since Mar 18/19; correlate with PRD deployments. (Owners: Michael Bui, Daryl Ng, Andin Eswarlal Rajesh, Alvin Choo)
*   **SAP Timeline Resolution:** Push SAP team to explore deposit SKU data solutions. (Owner: Sneha Parab/Alvin Choo/Gopalakrishna Dhulipati)
*   **B2B Testing Procedure:** Clarify MP SKU production alignment. (Owner: Gopalakrishna Dhulipati/Sneha Parab)
*   **Service Key Rotation:** Leads to take ownership with SRE. (Owner: All Leads/Gopalakrishna Dhulipati)
*   **OMNI-1157 Clarification:** Confirm scope applies only to the new app. (Owners: Alvin Choo/Gopalakrishna Dhulipati)
*   **BCRS Requirements:** Define explicit UAT scenarios with Koklin. (Owner: Alvin Choo/Gopalakrishna Dhulipati)
*   **Infrastructure Migration:** Address Bitnami Docker image end-of-life. (Owner: Engineering Team/Michael Bui)
*   **RAW Forms Review:** Review Risk Register for DPD RAW forms; confirm handovers and renew expired forms. Deadline: Tomorrow EOD. (Owner: All Leads/Sazali Bin Mohammed Ali's team)
*   **Survey PIC Identification:** Confirm responsible party for store purchase survey. (Owner: Gopalakrishna Dhulipati/All Leads)
*   **Scan@Door AI Prioritization:** Determine prioritization status on Omni board. (Owner: Daryl Ng/Alvin Choo)
*   **1HD Release Verification:** Confirm release status prior to production testing. (Owner: All Leads/Daryl Ng)
*   **Cursor Subscription & System Owners:** Finalize request mechanism and validate owner list following March 25 discussion. (Owner: Sneha Parab/IT Admin)

**Decisions Made**
*   **RMN Architecture:** Michael Bui updated current, future, and transition architecture diagrams.
*   **Townhall Coordination:** Team to meet Hui Hui post-townhall; no full Q&A scheduled.
*   **Release Status:** Questions remain regarding holding today's regular app release pending the search performance investigation.

**Key Dates & Deadlines**
*   **RAW Forms Review:** Due Tomorrow EOD.
*   **Townhall Meeting:** Today post-townhall session.
*   **Chee Hoe Support:** Effective end of March for Product Catalogue/MarTech scope.
*   **Bitnami Migration:** Ongoing (immediate action required).
*   **1HD Production Testing:** Targeted for this Friday or Monday.


## [13/64] Miguel Ho Xian Da
Source: gchat | Group: dm/0pYlUwAAAAE | Messages: 4 | Last Activity: 2026-03-25T11:39:55.713000+00:00 | Last Updated: 2026-03-25T14:46:17.874621+00:00
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


## [14/64] BCRS - UAT
Source: gchat | Group: space/AAQACfHCuNI | Messages: 2 | Last Activity: 2026-03-25T11:05:10.722000+00:00 | Last Updated: 2026-03-25T14:46:38.485586+00:00
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


## [15/64] Project Light: Mobilization and Planning Workshop Day 3 - Mar 26
Source: gchat | Group: space/AAQAwOH7W8A | Messages: 2 | Last Activity: 2026-03-25T10:35:12.694000+00:00 | Last Updated: 2026-03-25T14:46:53.765175+00:00
**Daily Work Briefing: Project Light Mobilization Workshop (Day 3)**

**Key Participants & Roles**
*   **Jacob Yeo**: Primary communicator regarding agenda updates.
*   **Recipients**: 18 total members of the "Project Light" Mobilization and Planning group; 11 have viewed the current agenda document.

**Main Topic/Discussion**
The discussion focuses on critical updates to the agenda for **Day 3** of the Project Light Mobilization and Planning Workshop, scheduled for **March 26**. Jacob Yeo notified the team that there are "latest changes" to tomorrow's schedule, though the specific content of these alterations was not detailed in the chat message itself.

**Pending Actions & Ownership**
*   **Action**: Review the updated agenda containing the latest changes.
    *   **Owner**: All 18 workshop participants (Status: 11 viewed).
    *   **Reference**: [Project Light Workshop Agenda](https://docs.google.com/spreadsheets/d/1ODEEFsP8mMxmUhYNuQ1norNCnWoIJwddZzUFqEUX-qw/edit?gid=1079702164#gid_1079702164) (Spreadsheet).
*   **Action**: Note the changes prior to the start of Day 3.
    *   **Owner**: All participants.
    *   **Context**: Jacob Yeo explicitly requested: "pls take note of the latest changes."

**Decisions Made**
No formal decisions were recorded in this specific chat exchange. The communication serves as a notification mechanism to alert stakeholders that the official agenda has been modified.

**Key Dates & Follow-ups**
*   **Notification Date**: March 25, 2026 (10:35 AM UTC).
*   **Event Date**: March 26, 2026 (Tomorrow relative to notification).
*   **Event Phase**: Day 3 of Mobilization and Planning Workshop.
*   **Follow-up Required**: Immediate review of the linked spreadsheet by all attendees before tomorrow's session.

**Summary Note**
Participants must access the linked Google Sheet immediately, as it contains the finalized agenda for March 26 with unlisted updates that were highlighted by Jacob Yeo.


## [16/64] BCRS Firefighting Group
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


## [17/64] RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU | Last Activity: 2026-03-25T10:11:05.086000+00:00 | Last Updated: 2026-03-25T10:40:24.138704+00:00
**Daily Briefing Summary: RMN Leadership Space (Updated Mar 25)**

**Key Participants & Roles**
*   **Bryan Choong:** Leadership; active oversight on SignCloud cleanup timeline. Currently attending eTail Asia. Emphasized maximizing ROI from event efforts and requested compilation of decks for future reuse.
*   **Allen Umali:** Addressed SRA/Advertima inquiries; leading SignCloud screen cleanup and loop verification.
*   **Rajiv Kumar Singh:** Coordinating SOAC planning and Advertima operations.
*   **Michael Bui:** Inquired about Advertima future clarity.
*   **Pauline Tan:** Active in LinkedIn content cadence and event coordination. Currently attending eTail Asia (as of 04:21 UTC, Mar 25).
*   *Note: Jaren Loy Xing Wei (Departing) remains as per previous context.*

**Main Topics**
1.  **Advertima Partnership Status:** Michael Bui questioned the future of Advertima operations, noting the current SRA covers only the Proof-of-Value (PoV) period. An extended PoV or long-term partnership requires a new Service Request Agreement (SRA). Rajiv Kumar Singh confirmed devices will operate under an extended PoV through end of April pending SRA formalization.
2.  **Advertima Technical Issues:** Reports identified consecutive playback errors in specific stores: an Energy Market Authority (EMA) ad ran three times consecutively, and a "Trust sign up" ad appeared erroneously. Allen Umali clarified that the affected screen is legacy hardware still on SignCloud undergoing manual cleanup; all other screens in the store follow the current play loop correctly.
3.  **SignCloud Cleanup:** Bryan Choong requested a timeline for removing old SignCloud screens. Allen Umali confirmed the full list is available and cleanup will be completed within this week (by Mar 28).

**Pending Actions & Owners**
*   **Advertima SRA Renewal:** Secure a new SRA for long-term Advertima partnership or extended PoV beyond April. *Owners: Allen Umali, Alvin Choo.*
*   **SignCloud Cleanup:** Complete manual removal of legacy screens and resolve loop errors (EMA/Trust ads). *Owner: Allen Umali | Deadline: End of this week (Mar 28).*
*   **Event Asset Compilation:** Compile event decks for future reuse to maximize ROI. *Owner: Pauline Tan.*
*   **Ad Suppression with Osmos:** Provide firm ETA to resolve weeks-old issue. *Owner: Team.*
*   **SOAC Planning:** Finalize targets per CM, supplier, and category by end of March. *Owner: Rajiv Kumar Singh & Ryan.*
*   **Brand/Non-Endemic Sales:** Continue rOOH sales efforts (endemic via JBP; non-endemic via WOG/govt campaigns) and prepare for HPB meeting. *Owner: Team.*
*   **LinkedIn Content Cadence:** Maintain 1–2 posts weekly starting Mar 9. Gather ideas/case studies from the team. *Owners: Pauline Tan & Team (Currently at eTail Asia).*

**Decisions Made**
*   **Advertima Continuity:** Confirmed extended PoV for Advertima devices through end of April pending SRA formalization.
*   **LinkedIn Launch:** "FPG ADvantage" page is live; frequency set at 1–2 times weekly.
*   **SignCloud Resolution:** Old screens are being manually purged; full list identified and cleanup targeted for completion this week.
*   **Strategic Focus:** Priorities during Bryan Choong's absence (and eTail Asia attendance) locked to SOAC targets, rOOH sales, and HPB prep.
*   **Knowledge Management:** Event decks will be standardized and compiled for future reuse to optimize operational efficiency.

**Key Dates & Deadlines**
*   **Mar 2:** Criteo/ChatGPT partnership analyzed; Jaren's departure announced.
*   **Mar 5:** FPG ADvantage LinkedIn page went live.
*   **Mar 9 – Mar 23:** Bryan Choong away from office (Re-engaged Mar 24 regarding SignCloud).
*   **Mar 19:** Advertima extended PoV confirmed for end of April; SRA update identified as necessary.
*   **Mar 25:** Pauline Tan and Bryan Choong attending eTail Asia; request issued to compile event decks.
*   **Mar 28 (Est.):** Completion of SignCloud manual cleanup.
*   **End of March:** Deadline to finalize SOAC targets per CM/supplier/category.
*   **April End:** Current deadline for Advertima extended PoV operations.
*   **Upcoming:** HPB meeting preparation required.


## [18/64] FP x Mirakl
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


## [19/64] [Leads] (Ecom/Omni) Digital Product Development
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


## [20/64] [Leads] (Ecom/Omni) Digital Product Development
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


## [21/64] FPG Everyone - General
Source: gchat | Group: space/AAAAjDYVcBU | Last Activity: 2026-03-25T08:08:27.885000+00:00 | Last Updated: 2026-03-25T10:44:18.786132+00:00
**Daily Work Briefing: FPG Everyone Chat Summary (Updated)**
**Date Range:** March 3 – March 21, 2026 (plus Mar 25 update)
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
*   **Siti Nabilah:** Day of Service Campaign Promoter (New context for Mar 25 update).

### Main Topics
1.  **Digital Access Rollout:** Schedule confirmed: Live (Facilities/Tech); Mar 16 (C-suite/HR/Finance); Mar 23 (Customer/Marketing/E-Commerce); Mar 30 (Remaining Hub staff). User guide distributed.
2.  **Media Collaboration – "Bowl of Love":** FairPrice launched a microdrama with Mediacorp featuring fresh pork from Malaysia, focusing on Mdm Gao and porridge.
    *   **Status:** Episodes 1–5 starring Tyler Ten were previously live. **Final episodes are now officially live** following the March 20 launch. The finale features Tyler Ten, Tasha Low, and Xiang Yun depicting a story of warmth and healing.
    *   **Platform:** @mediacorp.re.dian TikTok (`https://vt.tiktok.com/ZSusN9b4n/`).
3.  **Sensory Testing Panels:**
    *   **Frozen Snacks:** Evaluation conducted on March 18 & 19, 2026 (3 slots). Limited to 40 panelists. Mobile device submission required. Sign-up closed.
    *   **Chapati:** Screening form remains open.
    *   **Frozen Processed Food/Nuts:** Session status pending confirmation of overlap with Frozen Snacks dates.
4.  **Wellness Campaign – World Oral Health Day:** Ariel Yap promoted daily oral care routines ahead of the occasion, extending offers through March 25.
    *   **New Offer Details:** Up to 50% OFF essentials at Unity stores. Featured: Listerine Mouthwash (2 for $15.95), Colgate Charcoal Toothpaste (2 for $12.95), Colgate Gentle Gum Care Brushes (2 for $14.90), and Oral-B Vitality Electric Toothbrush ($48.10).
    *   **Offer Link:** https://go.fpg.sg/WOHD

### Pending Actions & Ownership
*   **Day of Service Registration (Owner: All Staff):** Final call issued by Siti Nabilah on March 25. Join the "Willing Hearts Kitchen Crew" on **March 27, 2026 (Friday)**, 1:00 PM – 5:00 PM at Joo Chiat Place to prep/cook/pack **3,000 meals**.
    *   **Urgency:** Only **20 spots left** remain.
    *   **Link:** `https://forms.gle/Y4B22gtUmU7SF42V6`
*   **Sensory Test Sign-ups (Owner: All Staff):** Chapati screening form remains open (`https://forms.gle/DFYrahZcvhtcoJ9R7`). Frozen Snacks sign-up is closed.
*   **Wellness Engagement:** Visit Unity stores for deals before Mar 25 or explore https://go.fpg.sg/WOHD.

### Critical Dates & Deadlines
*   **March 6:** End of Foaming Hand Soap offer (Completed).
*   **March 8:** International Women's Day Celebration (Completed).
*   **March 12:** Non-Halal Soup Sensory Evaluation (Completed).
*   **March 16–30:** Cardless access rollout phases.
*   **March 17:** Frozen Food/Nuts session (Status: Pending confirmation/overshadowed).
*   **March 18–19:** Frozen Snacks Sensory Evaluation (Completed).
*   **March 21:** "Bowl of Love" finale episodes live on TikTok.
*   **March 22:** FairPrice Walnuts with Cranberries redemption ends.
*   **March 25:** World Oral Health Day offers expire at Unity stores; Final call for Day of Service issued.
*   **March 27 (Friday):** Day of Service at Willing Hearts Kitchen (1:00 PM – 5:00 PM).

### Decisions Made
*   No formal strategic decisions recorded; focus remains on correcting Cardless Access communication, recruiting panelists for Frozen Snacks/Chapati testing, promoting the "Bowl of Love" microdrama collaboration (now complete with finale release), supporting World Oral Health Day initiatives via Unity stores (extended to Mar 25), and coordinating the March 27 Day of Service event.
*   **Updated:** Siti Nabilah has issued a final urgent call for the March 27 service, confirming only 20 spots remain for the "Kitchen Hero" mission at Joo Chiat Place.


## [22/64] [Internal] (Ecom/Omni) Digital Product Development
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


## [23/64] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Last Activity: 2026-03-25T07:55:26.595000+00:00 | Last Updated: 2026-03-25T10:45:03.850263+00:00
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

**Main Topics Discussed**
1.  **Website SDK Deployment (Strudel):** Lester deployed `go-platform-website` on Mar 19 to update the Strudel SDK for maximum voucher validation. Changes were reviewed via Bitbucket diff between v1.5.11 and v1.5.10.
2.  **Pre-order Payment Logic & UAT:** Zaw initiated an inquiry on Mar 24 regarding pre-order flows (app payment vs. POS redemption) and requested peer review for the offline pre-order admin page (`https://admin-uat.fairprice.com.sg/in-store-preorder/offline`).
3.  **Slot Date Discrepancy:** Shiva reported a delivery slot mismatch (UI shows 25th, API indicates 23rd). Daryl Ng and Sundy Yaputra are resolving this.
4.  **UAT Stock Requirements:** Sneha requested high-stock SKUs for Zi Ying's bulk order testing; Wai Ching Chan and Akash Gupta were tasked to check IMS availability.
5.  **Order Verification Bug (NED-278216):** Investigation continues into the Whitelisting API returning older contract data (identified by Andin).
6.  **BCRS Deposit & SAP Integration:** Critical duplicate deposit posting fix remains active (PR #6). Marketplace tickets are planned for release tomorrow in sync with SAP deployment.

**Pending Actions & Ownership**
*   **All Engineers:** Mark all tickets deployed to production as "Status = Done." Highlight any pending deployments in this chat thread immediately (Sneha Parab).
*   **Zaw Myo Htet:** Clarify pre-order payment redemption logic; execute UAT testing on offboarded Pinelabs split feature flag.
*   **Lester Santiago Soriano:** Assist with Whitelisting API contract issue (cc: Piraba Nagkeeran, Jonathan Tanudjaja). Deployment completed Mar 19.
*   **Wai Ching Chan & Akash Gupta:** Source high-stock SKUs from IMS for Zi Ying's bulk order testing and investigate UAT SKU `13023506` threshold settings.
*   **Daryl Ng & Sundy Yaputra:** Resolve delivery slot date mismatch (UI showing 25th vs API 23rd).
*   **Andin Eswarlal Rajesh:** Investigate iOS slot mapping error and assist with Amplitude event tracking flow inquiry.

**Decisions Made**
*   **Status Protocol:** All engineers must update Jira ticket status to "Done" upon production deployment; pending items must be flagged in the chat thread.
*   **Deployment Approval:** PLU processor deployment approved pending UD alignment.
*   **Code Review Priority:** Focus shifted to `go-platform-website` PR #1538 for the Strudel SDK update, superseding previous layout-service priorities. Current focus includes reviewing the new offline pre-order admin page.

**Key Dates & Deadlines**
*   **Mar 19, 2026:** Website deployment completed at 4:00 PM; UAT stock sourcing required immediately.
*   **Mar 24, 2026:** Zaw Myo Htet initiated inquiry regarding the offline pre-order admin page and pre-order payment logic.
*   **Mar 25, 2026 (Today):** Sneha Parab requested status updates on production deployments and highlighted open tickets via Jira filter ID: DPD-225 queue.
*   **Tomorrow:** Marketplace tickets release in sync with SAP deployment.
*   **Thursday:** D&T All Hands meeting.
*   **Mar 31, 2026:** Sports Hub FFS store closure deadline.

**Note on Historical Context:** Previous mentions of code review priorities for `layout-service` PR #362 and `website-service` PR #649 are superseded by the urgent Strudel SDK deployment update. The focus has now shifted to resolving slot date mismatches, pre-order payment logic queries, and the newly flagged offline pre-order admin page review. A new procedural requirement mandates immediate status updates for production tickets.


## [24/64] Project Light: Mobilization and Planning Workshop Day 1 - Mar 24
Source: gchat | Group: space/AAQAA8d_pfI | Last Activity: 2026-03-25T07:49:02.745000+00:00 | Last Updated: 2026-03-25T10:45:28.096914+00:00
**Daily Work Briefing: Project Light – Mobilization & Planning Workshop (Day 1)**
**Date:** March 24, 2026 (Session concluded; new insights added Mar 25)
**Resource Link:** https://chat.google.com/space/AAQAA8d_pfI

**Key Participants & Roles**
*   **Jacob Yeo:** Meeting facilitator.
*   **Vivian Lim Yu Qian:** Presenter/UI Walkthrough; defined technical/action items.
*   **Tiong Siong Tee:** UX Lead; proposed agenda flow and requested Figma access.
*   **Cecilia Koo Hai Ling:** Design/UX Contributor; shared DoorDash, NTUC FairPrice, Lazada references; clarified SKU logic and RedMart campaign details.
*   **Christine Yap Ee Ling:** Internal Liaison; handling Figma link distribution.
*   **Rajesh Dobariya:** Stakeholder; reviewed delivery categorization references.

**Main Topic & Discussion Updates**
The team conducted a high-level UX walkthrough and UI review, significantly expanding reference analysis to include RedMart's current "mega campaign" (running for 2 days) and Lazada app mechanics:
*   **RedMart Campaign Analysis:** Cecilia Koo Hai Ling shared screenshots and the Lazada campaign calendar link ([s.l.38p5B](https://s.lazada.sg/s.38p5B), viewed by 11 of 22). The team reviewed six critical components:
    1.  Voucher center structure.
    2.  Gamification mechanics.
    3.  Promo mechanisms (claim, apply, stack, and nudge toward next tiers).
    4.  Social sharing features.
    5.  "Store-in-store" concepts (default views, dedicated flash deals, seller vouchers).
    6.  User journey flow: Homepage → Category → Search → Campaign → General Merchandise.
*   **Lazada & FairPrice References:** Reviewed DoorDash's first-time app open and NTUC FairPrice examples (SharkNinja Official Store, FP Unilever Tag). The Lazada "promo label" (dynamic seller section) and gamified "Help me click" mechanic were accepted as engagement drivers.
*   **Navigation & Filters:** Clarification remains needed on whether category page filters should be pre-configured ("dynamic") or retrieved dynamically.
*   **UI Clarity:** The toggle selection between "Scheduled" and "Quick" modes requires improved visual definition.
*   **Compliance:** Discussed potential separation of eGift cards from vouchers to meet compliance requirements.
*   **SKU Logic:** Clarified that when any SKU is clicked, it is displayed as the primary SKU in Slot 1.

**Decisions Made**
*   **Reference Alignment:** Agreed that DoorDash's categorization and Lazada/RedMart campaign mechanics (voucher stacking, gamification, store-in-store) are valid benchmarks for Project Light integration.
*   **Filter Logic:** No final consensus on filter behavior; pending technical solution discussion led by Vivian.
*   **Slot 1 Behavior:** Clarified that the clicked SKU populates Slot 1, establishing a baseline interaction pattern.

**Pending Actions & Owners**
1.  **Share Figma Link:** Christine Yap Ee Ling to send via separate internal chat (requested by Tiong Siong Tee).
2.  **Resolve Filter Logic:** Vivian Lim Yu Qian and the technical team to finalize category page filter behavior.
3.  **Refine UI Toggle:** Design team to address visual clarity for "Scheduled/Quick" toggle selection.
4.  **Compliance Review:** Determine if eGift cards must be standalone from vouchers.
5.  **Deep-Dive Analysis:** UX Lead (Tiong Siong Tee) to analyze RedMart's voucher center, gamification, promo stacking logic, and store-in-store flows for Project Light integration.

**Key Dates & Follow-ups**
*   **Event:** Project Light Mobilization and Planning Workshop Day 1 (March 24, 2026).
*   **Status:** Session concluded; RedMart campaign materials and Lazada links shared via chat on March 25.
*   **Next Step:** Internal distribution of Figma link by Christine Yap Ee Ling; UX team to evaluate RedMart's "mega campaign" mechanics (voucher stacking, social sharing) for potential application in Project Light mega campaigns.


## [25/64] Project Light: Spotlight Topic - HIVE/Inventory - Mar 25
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


## [26/64] DPD x DPM
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


## [27/64] [Leads] (Ecom/Omni) Digital Product Development
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


## [28/64] QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs | Last Activity: 2026-03-25T06:55:46.464000+00:00 | Last Updated: 2026-03-25T10:46:55.210678+00:00
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
1.  **OmniHome Christmas Tiles Anomaly:** Milind Badame reported seeing "dressed up" Christmas tiles for FoodTakeaway on OmniHome despite the date being March. *Status:* Investigating visual consistency; 3 replies, last reply 3:13 AM.
2.  **PreOrder Tile Permanency (New):** On **25 Mar** at 06:55 UTC, Milind Badame flagged a new PreOrder tile in OmniHome and queried @Daryl Ng regarding its permanence to determine if E2E tests need updating as an entry point. *Status:* Awaiting clarification from Dev/Product.
3.  **LinkPay Receipt Banner Missing:** Observed on Android that the banner is missing in LinkPay receipts. Investigation requested with @Tiong Siong Tee. *Status:* New/Open (5 replies, last reply 4:45 AM).
4.  **Search Indexing Failure:** Madhuri Nalamothu reported a critical search failure where "Ninben Tsuyu No Moto Seasoning Soy Sauce - Triple Strength" is available with stock in the back office for store Hyper Changi but returns "We couldn't find anything that matches your search" when queried. *Status:* Urgent investigation needed. *Owners:* @Daryl Ng, @Yangyu Wang (21 replies).
5.  **E-Voucher Application Error:** Milind Badame reported a `404 Invalid voucher` error. Backend response indicates logic failure. *Status:* Open/Investigating with @Zaw Myo Htet.
6.  **LinkPoints Test Failure:** Tests remain disabled in regression; awaiting ETA on resolution from Dev Team (Michael Bui). *Status:* Blocked.
7.  **Postal Code Offer Label Missing:** Missing `label` attribute for the first product in "TestHasOffer swimlane" for Postal code **098619**.
8.  **QC Food Tile Removal Testing:** Daryl Ng confirmed testing is underway on the removal of QC (O2O) food tiles on the Omni home page.
9.  **Load Testing & Environment Stability:** Small-scale load test completed on **5 Mar, 11 AM–1 PM** (UAT LEAP env). Scale-down operations executed successfully.
10. **DC Membership Logic Discrepancy:** Critical inconsistency where users have `DC member` flags in back office but lack active plans/UI awards. Investigation ongoing.
11. **E2E Test Failures & UI Defects:**
    *   **Cart Page (Critical):** Komal Ashokkumar Jain reported a flaw where switching from Standard to Express delivery causes cart items to "stick," allowing orders with ineligible items for 1HD. Referenced by @Daryl Ng and @Andin Eswarlal Rajesh.
    *   **General UI:** Broken alignment on the third highlighted product; unidentified "view buttons"; iOS navigation issues persist (disappearing swimlanes, EVoucher errors, Express delivery label changes).
12. **Android OTP Blank Screen:** Milind Badame reported a blank screen issue for OTP on Android versions v12 and below. Investigation requested with @Tiong Siong Tee.

**Pending Actions & Ownership**
*   **PreOrder Tile Strategy:** Confirm if PreOrder tile is permanent to decide on E2E test updates. *Owner: @Daryl Ng / QA Team.*
*   **OmniHome Tile Anomaly:** Verify why Christmas tiles are visible in March. *Owner: QA Team / Dev.*
*   **LinkPay Receipt Banner:** Fix missing banner on Android receipts. *Owner: @Tiong Siong Tee.*
*   **Search Indexing Failure:** Resolve search failure for "Ninben Tsuyu No Moto Seasoning Soy Sauce - Triple Strength" at Hyper Changi. *Owners: @Daryl Ng, @Yangyu Wang.* (High Priority).
*   **E-Voucher Bug:** Investigate `404 Invalid voucher` error. *Owner: Milind Badame / @Zaw Myo Htet.*
*   **LinkPoints Fix Status:** Provide ETA for the LinkPoints fix. *Owner: Dev Team / Michael Bui.*
*   **Cart Express Delivery Bug:** Fix logic allowing ineligible items for 1HD when switching delivery modes. *Owners: Komal Ashokkumar Jain, Daryl Ng, Andin Eswarlal Rajesh.*
*   **Postal Code Label Debug:** Investigate missing `label` for Postal code 098619. *Owner: Milind Badame / Dev Team.*
*   **General Cart & Payment:** Resolve Cart alignment, view buttons, and payment failures. *Owners: Madhuri Nalamothu, Andin Eswarlal Rajesh, Dev Team.*
*   **Android OTP Blank Screen:** Investigate blank screen for Android v12 and lower. *Owner: @Tiong Siong Tee / Milind Badame.*

**Decisions Made**
*   Ad slot changes proceed; known test impacts acknowledged.
*   No decision yet on LinkPoints fix, Cart view buttons, Express delivery eligibility logic, E-Voucher application failure, Android OTP blank screen, Search indexing, tile anomalies, or the new PreOrder tile permanency; awaiting dev clarification and investigation results.

**Key Dates & Deadlines**
*   **5 Mar:** Load testing window (completed).
*   **16 Mar:** DC membership logic discrepancy logged.
*   **17 Mar:** UI defects reported on cart page (06:23–06:33 AM).
*   **18 Mar:** LinkPoints fix ETA required; Postal code 098619 issue flagged.
*   **20 Mar:** Critical Express delivery bug flagged by Komal Ashokkumar Jain at 11:05 UTC.
*   **24 Mar:** E-Voucher error reported by Milind Badame (02:39 UTC); Android OTP blank screen issue raised (08:05 UTC).
*   **25 Mar:** New issues flagged regarding OmniHome tiles, LinkPay receipts, Search indexing, and PreOrder tile permanency.


## [29/64] Project Light Attack and Defence Leads
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


## [30/64] Vera, Alvin, Ravi, Gopalakrishna
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


## [31/64] [Prod Support] Ecom FFS Ops
Source: gchat | Group: space/AAAAde_cYKA | Last Activity: 2026-03-25T06:13:38.538000+00:00 | Last Updated: 2026-03-25T06:44:50.334746+00:00
**Daily Work Briefing: [Prod Support] Ecom FFS Ops (Updated Mar 25)**

**Key Participants & Roles**
*   **Wai Ching Chan / Sampada Shukla:** Operations/Product Leads.
*   **TL HCBP FFS, TL - HGPT FFS, TLEPT FFS, Harry Akbar Ali Munir:** Store/Regional Team Leads reporting blockers.
*   **Adrian Yap Chye Soon:** Technical Lead/Support (investigating data anomalies).
*   **Akash Gupta:** DPD / Fulfilment / On Call (Source of new alerts and escalation point).

**Main Topics**
1.  **Packlist Discrepancies & Validation:** Ongoing investigation into critical `packed_qty` anomalies (NULL values or massive mismatches vs. `delivered_qty`).
    *   **New Critical Incident (Mar 25, ~6:00 AM):** Order #22898981 at Sun Plaza (Store ID 13) shows `packed_qty` of 12,710,651 vs. `delivered_qty` of 6. Reported by Akash Gupta to Adrian Yap Chye Soon.
    *   **Historical Context:** Previous Mar 23–24 incidents at Hyper Sports Hub and VivoCity remain active reference points alongside the new Mar 25 Sun Plaza alert.

**Pending Actions & Ownership**
*   **Critical Data Validation (Mar 25):**
    *   *@Yap Chye Soon Adrian:* Confirm massive `packed_qty` mismatch for Order #22898981 (Sun Plaza) immediately.
    *   *@Akash Gupta:* Continue monitoring DPD/Fulfilment alerts and tagging technical leads as requested in the 6:00 AM message.
*   **App Load Issues (Resolved):**
    *   **New Incident (Mar 25, 03:45 AM – 04:13 AM):** TL HCBP FFS reported "no order in picking q". The issue was confirmed active at 03:55 AM and escalated to On Call support via Wai Ching Chan. Status **Resolved** ("Its up now") by 04:13 AM.
    *   *Note:* This resolves the immediate HCBP blocking reported on Mar 23, though historical context of widespread load failures remains relevant for pattern analysis.

**Decisions Made**
*   **App Release Strategy:** Picker App 10.4.0 rollout remains on hold pending resolution of critical data anomalies (Mar 18–25). Full rollout is contingent on stability post-fixes, specifically addressing the new Mar 25 Sun Plaza alert and previous NULL quantity/mismatch incidents.

**Key Dates & Deadlines**
*   **Immediate:** Validation of Mar 25 Order #22898981 (Sun Plaza) and investigation into root causes for HCBP picking queue emptying (Mar 25).
*   **Pending:** Root cause analysis for all recent `packed_qty` anomalies across Sports Hub, VivoCity, Parkway, Changi, and Sun Plaza.

**Critical Alerts**
*   **New Alert (Mar 25, ~6:00 AM):** Order #22898981 at Sun Plaza shows `packed_qty` (12.7M) >> `delivered_qty` (6).
*   **Resolved Alert (Mar 25, 03:45–04:13 AM):** HCBP "no order in picking q" issue reported by TL HCBP FFS and resolved after On Call intervention.
*   **Previous Critical Alerts:** Mar 23 NULL quantity (Sports Hub), Mar 23 massive mismatch (VivoCity/Sports Hub), and Mar 24 massive mismatch (Sports Hub).


## [32/64] Alvin Choo
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


## [33/64] #dpd-dba
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


## [34/64] BCRS Firefighting Group
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


## [35/64] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY | Last Activity: 2026-03-25T05:19:40.447000+00:00 | Last Updated: 2026-03-25T06:47:56.448975+00:00
**Updated Briefing: BCRS Firefighting Group**
**Date:** March 25, 2026 (Latest activity: ~5:30 AM)
**Source:** Google Chat Space & Shared UAT Tracker (73 messages total)

### **Key Participants & Roles**
*   **Prajney Sribhashyam:** Project Lead/Test Coordinator.
*   **Sathya Murthy Karthik:** QA Lead (Scanning/Glitch focus).
*   **Michael Bui / Dany Jacob / De Wei Tey:** Finance/Data/Invoice specialists.
*   **Onkar Bamane:** Technical Integration/SAP Liaison.
*   **Alvin Choo:** Product/Release Manager.
*   **Hendry Tionardi, Shiva Kumar Yalagunda Bas, Andin Eswarlal Rajesh:** Technical Support & Development.
*   **Sneha Parab:** Stakeholder (SKU/Feature inquiries).
*   **Daryl Ng / Zaw Myo Htet:** Production deployment status liaison & Payment specialists.

### **Main Topics**
1.  **Payment Logic Clarification:** Prajney raised a critical query regarding whether "Hybrid pre-order" on the customer app can be paid using an "e-voucher." The thread generated six replies, with Zaw Myo Htet and Daryl Ng providing input by 5:30 AM.
2.  **Production Deployment Planning:** Prajney initiated a session for March 25 to secure sign-offs and plan production deployment, prioritizing attendance from Daryl Ng, Sneha Parab, Andin Eswarlal Rajesh, and Onkar Bamane.
3.  **UAT & Beta Testing Strategy:** Sathya requested clarification on the beta testing plan, specifically asking for tester assignments, specific SKUs to be tested, and detailed procedures.
4.  **Critical System Crash (Order #75577957):** Continuing from March 24; Sathya reports an inability to open Order #75577957 on mobile (repeated crashes) and a backend "order type unspecified" error blocking invoice generation.
5.  **Michael Bui's Departure:** Michael noted he has full-day meetings but emphasized his last day to deploy to Production is tomorrow (March 26). He requested meeting recordings and UAT sign-offs in Jira tickets, as he will be on leave next week.

### **Decisions & Updates**
*   **Payment Logic Inquiry:** Immediate clarification sought on e-voucher eligibility for Hybrid pre-orders; discussion active with Daryl Ng and Zaw Myo Htet.
*   **Deployment Priority:** Immediate planning session scheduled for March 25 to finalize production deployment and secure necessary sign-offs.
*   **Documentation Requirement:** Michael Bui mandated that UAT sign-offs must be explicitly indicated in Jira tickets before he departs next week.

### **Pending Actions & Owners**
| Action Item | Owner(s) | Status/Context |
| :--- | :--- | :--- |
| **Hybrid Pre-order Payment Logic** | Prajney Sribhashyam / Zaw Myo Htet / Daryl Ng | **High Priority (Mar 25, 5:30 AM):** Confirm if e-vouchers are allowed for Hybrid pre-orders on the customer app. Thread active with 6 replies. |
| **Production Deployment Session** | Prajney Sribhashyam / Onkar Bamane | **Urgent (Mar 25, 1:11 AM):** Session scheduled today to plan deployment and secure sign-offs. Attendance critical for Daryl Ng, Sneha Parab, Andin Eswarlal Rajesh. |
| **Beta Testing Plan Definition** | Sathya Murthy Karthik / Prajney Sribhashyam / Onkar Bamane | **High Priority (Mar 25, 1:13 AM):** Awaiting confirmation on tester list, specific SKUs for testing, and detailed beta procedures. Thread active with 11+ replies. |
| **Order #75577957 Crash Resolution** | Sathya Murthy Karthik / Technical Team | **Critical (Mar 24-25):** Mobile app crashes on order open; backoffice fails to generate invoice ("order type unspecified"). Follow-up requested by Sathya. |
| **Jira Sign-off & Meeting Recording** | Michael Bui / Team | **Urgent:** Michael requires UAT sign-offs recorded in Jira and meeting recordings before his final deployment day (Mar 26). |

### **Key Dates & Deadlines**
*   **March 24, 9:39 AM:** Critical crash reported on Order #75577957.
*   **March 25, Today:** Target for production deployment planning session and sign-off acquisition; active discussion on e-voucher payment logic.
*   **March 26 (Thu):** Last day for Michael Bui to deploy to Production; leave begins next week.

### **Historical Context Retained**
*   Existing e-comm test accounts deemed unusable for Pre-order staff app; new BCRS CF items and specific GWP SKUs required.
*   Original deadline for SAP Deposit API development was Feb 20 (missed/risk noted).
*   Re-delivery flow testing ongoing with audio issues reported on March 16 awaiting resolution.
*   Deposit SKU linking investigation ongoing due to failure to link post-publishing.


## [36/64] Team Starship
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


## [37/64] PFM x Events/UID Martech Issues
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


## [38/64] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw | Last Activity: 2026-03-25T04:50:17.652000+00:00 | Last Updated: 2026-03-25T06:49:22.397428+00:00
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
6.  **Social Events & Sentiment:** Kyle Nguyen previously announced an upcoming DPD BBQ with the sentiment "We come first." Maou Sheng Lee expressed a sentiment of feeling like energy is being wasted on March 18.
7.  **New: Alumni Engagement:** Natalya Kosenko noted DPD alumni participation in a Google AI event (March 25, 2026).

**Pending Actions & Owners**
*   **GP Team (Nicholas Tan / Mohit Niranwal):** Investigate Bitnami image replacement strategy to resolve TTR issues and update Golden Pipeline dependencies.
*   **iOS/Dev Team (Tiong Siong Tee / Andin Eswarlal Rajesh):** Investigate the iOS FPPay QR code login bypass bug.
*   **Datadog Admins:** Anyone who manually altered Datadog Teams must submit a Pull Request to `https://bitbucket.org/ntuclink/fp-datadog-eu` instead of editing the console to prevent configuration loss.

**Decisions Made**
*   No formal change freeze; feature releases are currently active (Alvin Choo).
*   Datadog team configurations must strictly follow Infrastructure as Code (Terraform) protocols; manual overrides are deprecated.

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

**Social Notes**
*   Boning He and Gopalakrishna Dhulipati shared snacks (Chinese cookies with chicken gizzard/medicinal barley and Indian cookies) in pantry areas.
*   Upcoming DPD BBQ announced by Kyle Nguyen ("We come first, see you!").


## [39/64] Product x RMN x Platform
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


## [40/64] BCRS Production Deployment Planning Session - Mar 25
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


## [41/64] BCRS Working Group - OMNI
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


## [42/64] BCRS Firefighting Group
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


## [43/64] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4 | Last Activity: 2026-03-25T03:56:53.657000+00:00 | Last Updated: 2026-03-25T06:52:19.788504+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Space Creator; Lead coordinating the briefing.
*   **Daryl Ng, Gopalakrishna Dhulipati, Tiong Siong Tee, Michael Bui, Akash Gupta:** Designated "Project Light Attack and Defence Leads".
*   **Hui Hui Voon:** Owner of the D&T Scope for Project Light Workshop document.
*   **Pauline Pong:** Owner of promotion conflict test case file.
*   **Jacob Yeo:** Edited CDTO Internal RFP requirements file on March 25, 2026.

**Main Topic**
Following the transition to active strategic planning ("Room 2") on March 24, the team is finalizing specific slide preparation within six "Spotlight Topics." While Alvin Choo initiated collaboration on **"RMN"** and **"Payment"** slides on March 24, a new flexibility protocol was established on March 25 allowing leads to attend other meetings (e.g., BCRS) if required. Concurrently, technical direction has shifted toward decoupling from SAP, with consensus that SAP should serve primarily for finance and sales records purposes. New RFP documentation and promotion conflict testing cases have been identified for review.

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
*   **Action:** Finalize the Attack/Defence team composition pending Dennis's confirmation following Alvin Choo's email.
    *   **Ownership:** Alvin Choo.
*   **Action:** Address technical clarifications raised by Tiong Siong Tee regarding Inventory visibility, Corporate Control alignment, and Product management portal structure (FP vs. Sellers).
    *   **Ownership:** Alvin Choo and Gopalakrishna Dhulipati.

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
*   **Session Start ("Room 2"):** March 24, 2026 (1:02 AM UTC).
*   **Spotlight Topics List Published:** March 24, 2026 (3:14 AM UTC).
*   **Email Sent for Team Confirmation:** March 24, 2026 (3:51 AM UTC) by Alvin Choo.


## [44/64] Theo Adi
Source: gchat | Group: dm/4g6tFSAAAAE | Last Activity: 2026-03-25T03:52:51.827000+00:00 | Last Updated: 2026-03-25T06:52:31.021540+00:00
**Daily Work Briefing**  
**Resource:** Theo Adi  
**Date:** March 25, 2026  
**Time Window:** 03:52 UTC  

**1. Key Participants & Roles**  
*   **Michael Bui:** Sender of the message; role not explicitly defined in context but acting as an information provider or system operator.  
*   **Theo Adi:** Subject resource (mentioned in metadata); recipient of this briefing summary.

**2. Main Topic/Discussion**  
The conversation consists of a single data transmission regarding a specific alphanumeric identifier: `NLPE-3ZEF-CWP4-LLLU-5MH3-HMAU`. No conversational context, questions, or explanatory text accompanied the code. The subject matter is strictly the relay of this unique tracking reference.

**3. Pending Actions & Ownership**  
*   **Action:** Review, validate, or act upon the identifier `NLPE-3ZEF-CWP4-LLLU-5MH3-HMAU`.  
*   **Owner:** Theo Adi (implied as the recipient of the data).  
*   **Status:** Pending initiation. No specific task instruction was attached to the message itself.

**4. Decisions Made**  
No decisions were recorded in this exchange. The interaction is a one-way notification of a code rather than a deliberative discussion resulting in an outcome.

**5. Key Dates, Deadlines, & Follow-ups**  
*   **Message Timestamp:** March 25, 2026, at 03:52:51 UTC.  
*   **Deadlines:** None specified within the message content.  
*   **Follow-ups:** No follow-up requests or next-step instructions were included in the single message from Michael Bui.

**Summary Note**  
The chat log contains only one entry. It serves as a direct handover of the reference code `NLPE-3ZEF-CWP4-LLLU-5MH3-HMAU` by Michael Bui to Theo Adi. Immediate attention is required to determine the operational significance of this code based on internal protocols, as no further context was provided in the chat interface.


## [45/64] Chee Keong Ng
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


## [46/64] 📢 COM Notifications
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


## [47/64] DPD x Platform Engineering
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


## [48/64] RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Last Activity: 2026-03-25T03:21:00.879000+00:00 | Last Updated: 2026-03-25T06:55:31.308505+00:00
**Daily Work Briefing: Automated Test Results Summary (RMN Notification)**

**Key Participants & Roles**
*   **Collection Runner App:** Automated testing agent executing API suites.
*   **Webhook Bot:** Reporting mechanism; consistently returning "unable to process your request" on all notifications.
*   **Parties Involved:** No human participants engaged; system-generated notification log.

**Main Topic/Discussion**
The conversation comprises automated notifications from the Collection Runner regarding nightly API test executions across `promo-service`, `marketing-personalization-service`, and `marketing-service` in the **staging** environment. Logs track "API Tests" and "API Contract Tests." The monitoring period spans March 12 through **March 25, 2026**, with execution windows at approximately 01:05 UTC, 02:30/02:31 UTC, and **03:20/03:21 UTC**.

**Test Execution Status & Anomalies**
*   **Stable Services:**
    *   `promo-service`: Confirmed stable on March 25 (02:30 UTC) with 10 Passed / 0 Failed API tests and 6 Passed / 0 Failed Contract tests. Stability continues from previous runs.
    *   `marketing-personalization-service`: **Updated Status:** The service executed successfully on **March 25, 2026, at 03:20 UTC**.
        *   **API Tests:** 96 Passed / 0 Failed (Total Requests: 21).
        *   **Contract Tests:** 126 Passed / 0 Failed (Total Requests: 21).
    *   Historical stability remains unbroken as of March 24. The service is now confirmed stable for the current day's final run.
*   **Persistent Failures (`marketing-service`):**
    *   The pattern of **recurring API test failures** persists on **March 25, 2026, at 01:05 UTC**, extending instability observed since March 17.
        *   **Mar 25 (01:05 UTC):** 51 Passed / **2 Failed** (API Tests). Contract tests remained stable (20 Passed / 0 Failed).
    *   The failure count remains consistent at exactly 2 API failures per run across the streak from March 17 through **March 25, 2026**.

**Pending Actions & Ownership**
*   **Investigate Persistent `marketing-service` Failures:** Root cause for the consistent 2 API test failures daily from March 17 through **March 25, 2026**, remains unaddressed. Engineering teams must review failure reports immediately given the five-day streak of recurrence.
*   **Webhook Bot Remediation:** The bot failed to process requests in every notification cycle from March 12 through the latest log on **March 25, 03:21 UTC**. Immediate attention is required from DevOps or Automation Infrastructure.

**Decisions Made**
*   No human decisions recorded; all entries are automated system outputs.

**Key Dates & Deadlines**
*   **Failure Window (Historical):** Instability noted on March 12 and 13.
*   **Current Failure Window:** The service has been failing consistently since **March 17, 2026**, continuing through **March 25, 2026**.
*   **Monitoring Period:** Data covers runs from **March 12, 2026**, through **March 25, 2026** (spanning execution windows at 01:05 UTC, 02:30/02:31 UTC, and **03:20/03:21 UTC**).
*   **Next Steps:** Immediate investigation into the `marketing-service` API flakiness and Webhook Bot connectivity issues.


## [49/64] QE <-> All Tribes
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


## [50/64] ❗ Important Email
Source: gchat | Group: space/AAQAUJW8HMo | Last Activity: 2026-03-25T02:54:31.598000+00:00 | Last Updated: 2026-03-25T06:56:55.973667+00:00
**Daily Work Briefing Summary (Updated)**

**Key Participants & Roles**
*   **Michael Bui (You):** Managing Osmos support, event RSVPs, FileVault compliance, performance feedback, Project Light coordination, and AI training follow-ups.
*   **Sip Khoon Tan (FPG AICOE) / Google AI Specialists:** Leading weekly Workbench Agentic AI sessions.
*   **Daryl Ng:** Declined "ACNxOsmos: Daily Cadence" due to reservist duty.
*   **Miguel Ho Xian Da (FairPrice):** Lead for OSMOS integration; organizer of RMN discussion with Accenture.
*   **Jazz Tong:** Head of Platform Engineering; on leave until Mar 23, 2026.
*   **Tong A. Yu / Lilibeth Villena (Accenture):** Proposing working sessions for integration architecture.

**Main Topics**
1.  **AI Training & Workbench Follow-up (New):**
    *   **Session:** Weekly 30-min virtual support on building agents in Workbench (Gemini Enterprise).
    *   **Schedule:** Every Wednesday, 2:00 PM – 2:30 PM SGT.
    *   **Duration:** March 25, 2026, to May 31, 2026.
    *   **Objective:** Guidance on agent building, Q&A, use case sharing, and exploring Gemini Enterprise/NotebookLM features.
    *   **Requirement:** RSVP required; submit questions in advance via the Question Submission Form. Log in at `work.fpg.sg` to explore tools prior to sessions.

2.  **Project Light & RMN Integration:**
    *   **Meeting Rescheduled:** Discussion with Accenture on RMN is now scheduled for **Thursday, March 26, 2026, from 2:00 PM – 3:00 PM SGT**. Attendees: Michael Bui, Rajiv Kumar Singh (Required), Bryan Choong (Optional).
    *   **Context:** FairPrice Group is scaling Smart Carts/Digital Price Cards/IPOS. Accenture proposed sessions Mar 16-20; March 26 was selected due to conflicts.
    *   **Project Light (Original):** Rescheduled to Mar 19, 4:00–5:00 PM SGT. *Conflict with BCRS Warroom remains.*

3.  **BCRS - Refunds Issue Warroom:**
    *   Scheduled for **Thursday, March 19, 2026, from 3:30 PM – 4:30 PM SGT** (Prajney Sribhashyam).
    *   **Conflict Alert:** Overlaps with Project Light meeting. Immediate resolution required.

4.  **ACNxOsmos Daily Cadence Update:**
    *   **Status:** Daryl Ng declined the Monday, March 30, 2026 (12:30 PM – 1:00 PM SGT) invitation due to reservist duty.

5.  **D&T Power Breakfast Planning:**
    *   New event announced by Trina Boquiren.
    *   **Planning Meeting:** Tuesday, March 31, 2026, from 1:30 PM – 2:00 PM SGT at FairPrice Hub-11-L11 Mocha (6) [TV] or Google Meet.

6.  **Performance Feedback:** Scheduled for Wednesday, Mar 18, 2026, at 4:00 PM SGT with Alvin Choo and Winson Lim.

**Pending Actions & Ownership**
*   **AI Training RSVP (Michael Bui):** Submit "Yes" to the weekly session series starting March 25; submit questions via the form before each Wednesday slot.
*   **RMN Meeting RSVP:** Confirm attendance for March 26, 2:00–3:00 PM SGT.
*   **Project Light/Warroom Conflict:** Resolve scheduling conflict between Project Light (Mar 19, 4:00 PM) and BCRS Warroom (Mar 19, 3:30 PM). Reply "Yes" to both invitations immediately or delegate.
*   **Performance Meeting RSVP:** Confirm attendance for Mar 18, 4:00 PM SGT.
*   **D&T Breakfast Planning RSVP:** Respond to Trina Boquiren's invitation for March 31.
*   **OSMOS Architecture:** Provide architectural details on SmartCarts and IPOS to finalize long-term integration strategy with Accenture.

**Decisions Made**
*   **RMN Integration Timeline:** Team agreed to prioritize a focused working session on March 26 for architecture definition after previous slots failed due to conflicts.
*   **OSMOS Capability:** Confirmed feasible short-term integration (video via CDN, image via FPG service); long-term decision pending Accenture recommendation on centralized CMS vs. API distribution.

**Critical Dates & Deadlines**
*   **Mar 18, 2026:** Performance Feedback Meeting.
*   **Mar 19, 2026:** BCRS Warroom (3:30 PM) & Project Light (4:00 PM). *Conflict.*
*   **Mar 25–May 31, 2026:** Weekly AI Workbench Sessions (Wednesdays, 2:00–2:30 PM SGT).
*   **Mar 26, 2026:** RMN Discussion with Accenture (2:00–3:00 PM SGT). Link: `https://meet.google.com/koe-uzer-xbd` | PIN: 583106441.
*   **Mar 30, 2026:** ACNxOsmos Daily Cadence (Daryl Ng declined).
*   **Mar 31, 2026:** D&T Power Breakfast Planning Session (1:30–2:00 PM); FileVault Final Deadline.


## [51/64] BCRS ECOMM SAP POSTING
Source: gchat | Group: space/AAQA-ICuJRM | Last Activity: 2026-03-25T02:45:52.280000+00:00 | Last Updated: 2026-03-25T06:57:33.973322+00:00
**Daily Work Briefing: BCRS ECOMM SAP POSTING & Refunds UAT (Mar 25 Update)**

**Key Participants & Roles**
*   **Wei Fen Ching:** Accounting verification lead.
*   **De Wei Tey:** Provided B2B credit note examples; confirmed refund status for order 75567408.
*   **Yap Chye Soon Adrian / Hendry Tionardi:** SAP/DBP technical owners handling invoice creation, GI processing, and system validation.
*   **Onkar Bamane / Prajney Sribhashyam:** Stakeholders managing UAT validation, coordination, and SAP finance queries.
*   **Lai Shu Hui:** Participant in upcoming resolution call.
*   **Tan Gay Lee:** Raised query regarding Pre-order return testing.

**Main Topic**
UAT testing for BCRS E-commerce involving Sales Posting to SAP (F420) and Refunds. Focus has shifted from initial invoice validation to resolving specific SAP posting discrepancies, generating missing invoices/GIs, and clarifying treatment for fully redeemed orders (Linkpoints/eVouchers). Immediate priority is addressing Finance's reporting anomalies regarding FPON orders via a scheduled technical discussion. New focus includes validating test results for manual and Scan 'n Go refunds with/without container returns.

**Status of Issues & Updates**
*   **Credit Note Verification:** On Mar 24, Wei Fen Ching flagged a credit note lacking BCRS deposit details (shared image), prompting review with Yap Chye Soon Adrian.
*   **Invoice & GI Generation:** De Wei Tey requested invoice generation for orders **#75578021** and **#75577802**. Hendry Tionardi confirmed the issue was resolved, noting invoices will auto-create within 15 minutes.
*   **Goods Issue (GI):** On Mar 24 at 05:43 AM, De Wei Tey requested assistance with GI for order **#75578449**; Hendry Tionardi confirmed completion ("Done").
*   **SAP Posting Anomaly:** Prajney Sribhashyam reported a critical query on Mar 24 at 04:42 AM. Finance highlighted that FPON orders fully redeemed via Linkpoints and eVouchers show no sales posting in SAP, despite DPD team confirmation of backend posting.
*   **New Test Cases Added (Mar 25):** Prajney Sribhashyam added four new test cases following yesterday's discussion:
    1.  Manual refund with return of container.
    2.  Manual refund without return of the container.
    3.  Scan 'n Go refund with return of container.
    4.  Scan 'n Go refund without return of the container.
*   **Testing Request:** Prajney Sribhashyam requested Wei Fen Ching and Lai Shu Hui to review test results in rows 28–37 of the "UAT Refunds (RPA, CS & Finance)" tab in the BCRS UAT 2026 spreadsheet.
*   **Pre-order Query:** Tan Gay Lee queried on Mar 25 regarding Pre-order return testing; response pending from Prajney Sribhashyam.

**Pending Actions & Ownership**
1.  **UAT Data Review:** Wei Fen Ching and Lai Shu Hui to review test results for rows 28–37 (Manual/Scan 'n Go refunds with/without container returns). **(Owner: Wei Fen Ching, Lai Shu Hui)**.
2.  **FPON Resolution Meeting:** Attend the scheduled call at 4:00 PM on Mar 24 to validate SAP treatment for fully redeemed orders. **(Owner: Onkar Bamane, Wei Fen Ching, Lai Shu Hui)**.
3.  **Verify Credit Note Details:** Investigate Wei Fen Ching's observation regarding the credit note missing BCRS deposit data. **(Owner: Yap Chye Soon Adrian / DBP Team)**.
4.  **Pre-order Clarification:** Address Tan Gay Lee's inquiry on Pre-order return testing status. **(Owner: Prajney Sribhashyam)**.
5.  **API Integration Confirmation:** De Wei Tey seeks confirmation on API connectivity between Zendesk and DBP used by Jimmy to pull information. **(Owner: Wai Ching Chan / Onkar Bamane)**.

**Decisions Made**
*   Confirmed that invoices for orders #75578021 and #75577802 are now processing automatically (15-min window).
*   Goods Issue for order #75578449 successfully completed by Hendry Tionardi.
*   Finance has identified a discrepancy in SAP posting logic for fully redeemed FPON orders requiring immediate technical validation via the 4:00 PM call.
*   Four new refund test scenarios (Manual/Scan 'n Go with/without container return) have been added to the UAT spreadsheet for review.

**Key Dates & Follow-ups**
*   **Mar 21:** Initiated BCRS deposit refund testing (Order #75570370).
*   **Mar 24, 00:55 UTC:** Wei Fen Ching flagged credit note without BCRS deposit.
*   **Mar 24, 03:43 UTC:** De Wei Tey requested invoices for orders #75578021 and #75577802.
*   **Mar 24, 03:46 UTC:** Hendry Tionardi confirmed issue resolution; auto-invoice generation confirmed.
*   **Mar 24, 04:42 UTC:** Prajney Sribhashyam raised query regarding FPON orders with no SAP sales posting despite DPD confirmation.
*   **Mar 24, 05:43 UTC:** GI requested for order #75578449; completed immediately.
*   **Mar 24, 07:40 UTC:** Scheduled Google Meet call at 16:00 (UTC) to resolve FPON posting anomaly.
*   **Mar 25, 00:17 UTC:** Prajney Sribhashyam shared updated test cases and requested review of rows 28–37.
*   **Mar 25, 02:45 UTC:** Tan Gay Lee inquired about Pre-order return testing.

**Immediate Follow-up:** Attend the 4:00 PM meeting with Onkar Bamane, Wei Fen Ching, and Lai Shu Hui to validate SAP treatment for fully redeemed FPON orders, confirm API data flow between Zendesk and DBP, and verify the BCRS deposit status on the flagged credit note. Concurrently, review new refund test cases in the UAT spreadsheet.


## [52/64] [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Last Activity: 2026-03-25T02:38:01.608000+00:00 | Last Updated: 2026-03-25T02:49:31.057756+00:00
**Daily Work Briefing: [Prod Support] Marketplace**

**Key Participants & Roles**
*   **Support/Operations:** Willie Tan, Iris Chang, Lalita Phichagonakasit, Charlene Tan, Jie Yi Tan, Ayton See, Amos Lam, Michelle Lim.
*   **Technical/Admin Team:** Dang Hung Cuong, Shiva Kumar Yalagunda Bas (Frequent recipients of access/access issues), Olivia -, Jill Ong, Greta Lee, Zaw Myo Htet, Angella Yeo, Cassandra Thoi, Gopalakrishna Dhulipati.

**Main Topics & Discussion Summary**
The conversation covers critical operational blockers regarding seller onboarding, order fulfillment discrepancies, system configuration errors, urgent promotion removal requests, and new order inquiries. New discussions include email notification failures and order status synchronization issues. Major themes include:

1.  **User Access & Notifications:**
    *   **Email Failure:** Michelle Lim (Mar 23) reported a seller/user did not receive Mirakl invitation emails for the "Frutrip Official Store," even after checking spam folders. The team needs to determine how to resend the invite to create a new user.
2.  **Order Status Discrepancies:** Cassandra Thoi (Mar 25) requested checks on two orders with conflicting statuses:
    *   Order #256055476: DBP shows "Completed," but Mirakl shows "Cancelled."
    *   Order #248407866: Cancelled by API.
3.  **Access Management:** Requests to grant "PickerApp" access for new/existing sellers (Meat Affair, Old Shanghai, BulkMartGo, PETS STATION HOLDING). Charlene Tan reported a new seller (Woah Group) encountering errors under the "Offers" section.
4.  **Sales Data & Reporting:** Issues with vendors (CoLab Apac, Old Shanghai) not receiving sales breakdown reports since inception.
5.  **Promotion & Pricing Conflicts:**
    *   **Urgent Removal Request:** Lalita Phichagonakasit (Mar 20) reported an incorrectly set up promotion for **Item ID: 90244361** requiring immediate removal to prevent financial loss.
    *   Conflicting promotions for "Falcon Galaxy Strong Garbage Bag" require one to be disabled.
    *   Discount prices not showing despite SKU publication.
6.  **Fulfillment & System Errors:**
    *   Delivery slot display discrepancy for seller "Funa Artistic Hampers & Gifts" (Mar 19): Mirakl shows 91h vs Frontend date; focus remains on a window duration issue showing 4 days instead of the expected 2 days.
    *   Missing items in PickerApp compared to email picklists (Atasco Dairy, Estalife).
    *   Orders completed without delivery by NJV (Order #246974265, #248270820).
    *   Seller description/image updates not triggering "Pending Verification" status.
7.  **New Listing & Logic Queries:**
    *   **Item Visibility:** Lalita Phichagonakasit reported SKU **13226899** failing to appear under postal code **762115** since March 14th.
    *   **Picklist Logic (New):** Amos Lam (Mar 21) raised a critical issue where a vendor who opted out of public holidays in December did not receive a pick list today. This requires immediate investigation into why the system failed to generate a list for an opt-out status.
8.  **SAP Configuration Inquiry:** Iris Chang queried the definition and data source of "Lead Time" within SAP T-code ZMP_VENDOR on Mar 18.
9.  **Order Status Inquiry:** Angela Yeo (Mar 21) raised a query regarding FFS orders for seller **Yumsay Food**, seeking technical team advice.

**Pending Actions & Ownership**
*   **Urgent Promotion Removal:** Dang Hung Cuong and Gopalakrishna Dhulipati to immediately remove incorrectly set up promotion for Item ID: 90244361 (Lalita Phichagonakasit request, Mar 20).
*   **Picklist Generation Failure:** Technical team (Dang Hung Cuong, Shiva Kumar Yalagunda Bas) to investigate why a vendor who opted out of public holidays in December did not receive a pick list today (Amos Lam, Mar 21).
*   **FFS Order Inquiry:** Technical team to investigate FFS order status for seller "Yumsay Food" (Angela Yeo, Mar 21).
*   **Order Status Investigation:** Dang Hung Cuong, Shiva Kumar Yalagunda Bas, and Amos Lam to check discrepancies for Order #256055476 (DBP vs. Mirakl) and Order #248407866 (API cancellation) (Cassandra Thoi, Mar 25).
*   **Resend User Invitation:** Technical team to investigate how to resend the Mirakl invitation email for the "Frutrip Official Store" user who did not receive it (Michelle Lim, Mar 23).
*   **Close DF SOF Order:** Willie Tan requested closure; tracking via DST-2578 (Owners: Dang Hung Cuong, Shiva Kumar Yalagunda Bas).
*   **Vendor Report Issues:** Investigate missing sales breakdown reports for CoLab Apac (NED-277148) and Old Shanghai (NED-277329).
*   **Access Grants:** Grant PickerApp access to Meat Affair, BulkMartGo, PETS STATION HOLDING, and others. Resolve Woah Group "Offers" error (Charlene Tan).
*   **Fulfillment Investigation:** Check why Estalife missing Final Picklist PFC; investigate delivery slot display for Funa Artistic Hampers & Gifts (4 days vs. 2 days expected); determine trigger for NJV non-delivery completions.
*   **System Logic & Listing Fixes:** Investigate missing SKU 13226899 listing for postcode 762115; clarify picklist generation logic for postponed orders. Resolve SAP ZMP_VENDOR Lead Time definition (Dang Hung Cuong/Amos Lam).

**Decisions Made**
*   Dang Hung Cuong is prioritizing the removal of Item ID: 90244361, the new picklist failure issue raised by Amos Lam, and the Woah Group offers error. Dang Hung Cuong and Shiva Kumar Yalagunda Bas are assigned to investigate the vendor picklist anomaly. Ayton See previously educated a seller on promotion setup rules after identifying a configuration error.

**Key Dates & Deadlines**
*   **2026-03-25 (Today):** Cassandra Thoi requested checks on orders #256055476 and #248407866. Previous urgent request to remove Item ID: 90244361 remains active from Mar 20.
*   **2026-03-23:** Michelle Lim reported Mirakl email notification failure for Frutrip Official Store user.
*   **2026-03-21 (Yesterday):** Angela Yeo requested advice on FFS orders for "Yumsay Food"; Amos Lam reported vendor picklist failure due to public holiday opt-out status.
*   **2026-03-19:** Jie Yi Tan reported Funa Artistic Hampers & Gifts delivery window discrepancy; discussion ongoing with 34 replies.
*   **2026-03-18:** Iris Chang inquired about SAP T-code ZMP_VENDOR "Lead Time" definition.
*   **2026-03-03:** DF SOF order request raised.
*   **December 2025 (Historical Context):** Vendor involved in Amos Lam's query opted out of public holidays.


## [53/64] Release - FPG Back Office (Mon-Thurs)
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


## [54/64] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/-3PHNWPnwGs | Last Activity: 2026-03-25T02:24:15.864000+00:00 | Last Updated: 2026-03-25T02:52:10.682336+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Sathya Murthy Karthik:** Initiator of the technical issue; reporting inability to access order data and generate invoices.
*   **Andin Eswarlal Rajesh:** Triage lead; coordinating the investigation and attempting to gather account details from Sathya.

**Main Topic**
Technical troubleshooting regarding Order #75577957. The user is unable to open the order on a mobile device (app crashing) and cannot generate an invoice via the backoffice due to an "order type unspecified" error.

**Status of Actions & Ownership**
*   **Action:** Investigate Order #75577957 access issues and invoice generation failure.
    *   **Owner:** Andin Eswarlal Rajesh (assigned initially in the thread).
    *   **Current Status:** **Resolved/Redirected.** Andin noted at 02:24 on March 25 that he located the issue details in a separate discussion thread ("Nvm saw the other thread"), ending the need for further inquiry within this specific chat space.

**Decisions Made**
*   No formal decisions were recorded in this specific chat log, as the discussion concluded with the realization that the relevant context existed elsewhere. The team determined that the issue requires follow-up in a different thread rather than continuing here.

**Key Dates & Deadlines**
*   **Issue Reported:** March 24, 2026 (09:39 UTC) by Sathya Murthy Karthik.
*   **Investigation Started:** March 25, 2026 (02:21 UTC) by Andin Eswarlal Rajesh.
*   **Thread Closed/Redirected:** March 25, 2026 (02:24 UTC).

**Summary for Follow-up**
The team should verify the status of Order #75577957 in the "other thread" referenced by Andin to ensure Sathya's invoice request and crash issue are fully resolved.


## [55/64] @omni-ops #standup - Mar 25
Source: gchat | Group: space/AAQANjGExUA | Last Activity: 2026-03-25T02:01:19.578000+00:00 | Last Updated: 2026-03-25T02:53:59.575617+00:00
**Daily Work Briefing: #standup Channel**
**Date:** March 25, 2026
**Channel:** @omni-ops #standup
**Source URL:** https://chat.google.com/space/AAQANjGExUA

### **Key Participants & Roles**
*   **Yangyu Wang:** Initiator of the standup check-in. (Specific role not explicitly defined in log, but active participant).
*   **Channel Audience:** 4 out of 7 members viewed the message; specific identities of other viewers are not listed.

### **Main Topic/Discussion**
The conversation consisted solely of a prompt by Yangyu Wang asking for the initiation or progress update of the daily standup meeting ("standup?"). No substantive discussion, status updates, or technical details were recorded in this log entry. The interaction appears to be an attempt to convene the team rather than a completed report.

### **Pending Actions & Ownership**
*   **Action:** Initiate/Conduct the daily standup meeting.
*   **Owner:** Team members (triggered by Yangyu Wang).
*   **Status:** Pending. The prompt indicates the session has not yet commenced or concluded, as no subsequent updates were recorded in this timeframe.

### **Decisions Made**
*   None. No decisions were reached or documented within the provided chat log.

### **Key Dates & Follow-ups**
*   **Timestamp:** March 25, 2026, at 02:01:19 UTC.
*   **Immediate Follow-up Required:** Team members need to respond to Yangyu Wang's prompt to begin the standup or provide a status update if the meeting was already underway but not logged.

### **Summary**
On March 25, 2026, at 02:01 UTC, Yangyu Wang posted a single inquiry in the #standup channel asking for the start of the daily standup. The message was viewed by four members of the seven-person team. No further content, status reports, blockers, or action items were generated in this specific log segment. The conversation remains open pending further input from the team to proceed with the standard daily briefing protocol.


## [56/64] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/OYprgYt5wxQ | Last Activity: 2026-03-25T01:40:23.024000+00:00 | Last Updated: 2026-03-25T02:54:42.036641+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Michael Bui:** Deployer/Developer (Last day to deploy to Production; leaving next week).
*   **Prajney Sribhashyam:** Stakeholder/Product Owner (Managing sign-off process and Epic tracking).
*   **Other Mentioned:** Daryl Ng, Sneha Parab, Andin Eswarlal Rajesh (Recipients of original deployment request); Onkar Bamane (Planned for deployment session).

**Main Topic**
Coordination regarding the final Production (PRD) deployment for the OMNI & DPD Epics, specifically addressing UAT sign-off procedures and Michael Bui's availability constraints.

**Decisions Made**
*   **Sign-Off Mechanism:** Sign-offs will be recorded at the overall OMNI & DPD Epic ticket level rather than on individual sub-tickets to ensure scalability.
*   **Documentation:** A specific sign-off form will be shared by Prajney Sribhashyam for reference.
*   **Deployment Timing:** Michael Bui confirmed he will process PRD deployment today (25/03) or latest by tomorrow (Thu 26/03).

**Pending Actions & Ownership**
1.  **Share Sign-Off Form:** Prajney Sribhashyam to distribute the sign-off document. (Owner: Prajney)
2.  **Update Jira Ticket:** Michael Bui to comment on his specific ticket referencing the Epic-level sign-off once received/processed. (Owner: Michael)
3.  **Meeting Recording:** The team must record the meeting since Michael cannot attend due to full-day meetings. (Owner: Team/Organizer)

**Key Dates & Deadlines**
*   **2026-03-25 (Wed):** Target for PRD deployment and sign-off processing.
*   **2026-03-26 (Thu, Tomorrow):** Absolute deadline for Michael Bui's final PRD deployment.
*   **Next Week:** Michael Bui is on leave; no further deployments expected from him after the 26th.

**Follow-Ups**
*   Michael Bui will follow up after his meetings.
*   A session with Onkar Bamane was identified as prioritized for deployment planning (status implied as active).


## [57/64] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/y11GNi2Z3Yo | Last Activity: 2026-03-25T01:35:06.555000+00:00 | Last Updated: 2026-03-25T02:55:43.362629+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Lead/Coordinator. Facilitates scheduling flexibility for team members regarding conflicting commitments.
*   **Daryl Ng:** Team Member/Lead. Confirms attendance for specific project sessions.

**Main Topic/Discussion**
The conversation focused on scheduling coordination between the "Project Light Attack and Defence" meeting and other mandatory engagements, specifically the BCRS (Business Continuity Risk Scenario?) meeting. Alvin Choo clarified that if team members have conflicting requirements (e.g., BCRS), they are authorized to attend those meetings instead of Project Light.

**Decisions Made**
*   **Attendance Priority:** No blanket attendance requirement was enforced for the Project Light meeting; flexibility is granted if other critical meetings (like BCRS) arise.
*   **Confirmed Schedule:** Daryl Ng confirmed his intention to prioritize and join the Project Light meeting scheduled for 10:30 AM on March 25, 2026.

**Pending Actions & Ownership**
*   **Action:** Attend the Project Light meeting at 10:30 AM.
    *   **Owner:** Daryl Ng
    *   **Status:** Confirmed/In Progress.

**Key Dates & Follow-ups**
*   **Date:** March 25, 2026 (Tuesday).
*   **Event Timing:** Project Light meeting at 10:30.
*   **Reference Context:** BCRS meeting (time not specified in chat).

**Metadata Reference**
*   **Space URL:** https://chat.google.com/space/AAQAsFyLso4
*   **Total Messages Reviewed:** 2


## [58/64] Backend Chapter
Source: gchat | Group: space/AAAAHhDyHI4 | Last Activity: 2026-03-25T01:29:26.022000+00:00 | Last Updated: 2026-03-25T02:56:29.408987+00:00
**Daily Work Briefing: Backend Chapter**

**Key Participants & Roles**
*   **Michael Bui:** Investigated GCP PubSub configuration for message delivery.
*   **Nicholas Tan:** Inquired about PubSub flags; flagged security concerns regarding Service Account (SA) keys in `fpg-titan-preprod`.
*   **Lester Santiago Soriano:** Blocked on CI/CD pipeline errors after upgrading Go dependencies; requested support.
*   **Maou Sheng Lee:** Suggested using AI tools to resolve Lester's issue.
*   **Boon Seng Ong:** Investigated deployment failures with `deploy-esp-image` for ESPv2, noting discrepancies between past success and current failures despite unchanged code or SDK versions.

**Main Topics**
1.  **GCP PubSub Configuration (March 6):** Michael Bui sought configuration flags for "at-most-once" delivery in GCP PubSub but found no samples. Nicholas Tan followed up, noting limited expertise. No resolution reached; discussion remains open regarding specific flag implementation.
2.  **CI/CD & Dependency Upgrade (March 12):** Lester Santiago Soriano upgraded `stdlib` to `v1.25.8` to address SonarQube vulnerability `GO-2026-4603`. The pipeline failed due to a version mismatch: the build agent's `golangci-lint` was compiled with Go 1.24, while the project targeted Go 1.25.8.
    *   *Root Cause Identified:* The error requires an update to the `dpd-backend-cicd` resource.
3.  **ESPv2 Deployment Failure (March 25):** Boon Seng Ong reported that redeploying ESPv2 via `deploy-esp-image` fails with `gcloud beta run deploy` errors, specifically: "expected a container image path" and invalid flag value for `--to-revisions`.
    *   *Investigation:* Code unchanged from 7 days prior; usage of an older `google/cloud-sdk:546.0.0-slim` image also failed. Boon suspects recent changes to the "golden pipeline."
    *   *Error Detail:* `gcloud run services update-traffic` rejected `--to-revisions [value=100]`, suggesting a syntax or parameter shift in the deployment logic.
4.  **Service Account Security Audit (March 16):** Nicholas Tan identified JSON keys embedded in Service Accounts (`pong-club-agent`, `vertex-client`) within the `fpg-titan-preprod` project. These accounts require decomposition due to security best practices.

**Pending Actions & Ownership**
*   **Resolve CI/CD Pipeline Block (Go Version):** Update `dpd-backend-cicd` resource configuration to support Go 1.25.8 or align linter version.
    *   *Owner:* **TBD** (Lester requested ownership; current owner unknown).
*   **Investigate Golden Pipeline Breakage:** Determine recent changes causing `gcloud beta run deploy` and `update-traffic` flag failures for ESPv2.
    *   *Owner:* **Boon Seng Ong** (to coordinate with pipeline maintainers).
*   **Service Account Cleanup:** Identify owners and decompose identified SAs (`pong-club-agent`, `vertex-client`) in `fpg-titan-preprod`.
    *   *Owner:* **TBD** (Nicholas Tan flagged this; ownership unknown).

**Decisions Made**
*   No formal decisions recorded. The team acknowledged the Go version mismatch requires a CICD resource update, identified the need to decompose specific Service Accounts, and flagged the golden pipeline as a potential root cause for recent deployment failures.

**Key Dates & Follow-ups**
*   **March 6, 2026:** Initial PubSub inquiry (Open).
*   **March 12, 2026:** Pipeline failure reported; escalation for CICD ownership required.
*   **March 16, 2026:** Security flag raised regarding `fpg-titan-preprod` SAs. Follow-up on SA ownership is critical.
*   **March 25, 2026:** Critical deployment failure reported; investigation into golden pipeline changes initiated.


## [59/64] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/hWcMUCKuAro | Last Activity: 2026-03-25T01:28:11.621000+00:00 | Last Updated: 2026-03-25T02:56:39.575679+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**1. Key Participants & Roles**
*   **Prajney Sribhashyam:** Initiator of the deployment session; coordinating sign-offs and logistics.
*   **Daryl Ng, Sneha Parab, Andin Eswarlal Rajesh, Onkar Bamane:** Tagged participants expected to prioritize the upcoming planning session.

**2. Main Topic/Discussion**
*   Preparation for an imminent production deployment.
*   The team is awaiting final sign-offs to proceed with this deployment today (March 25, 2026).
*   A dedicated coordination session is being organized to plan the execution of the deployment once approvals are secured.

**3. Pending Actions & Ownership**
*   **Action:** Attend and prioritize the planning session for production deployment.
    *   **Owner:** Daryl Ng, Sneha Parab, Andin Eswarlal Rajesh, Onkar Bamane.
    *   **Context:** Prajney Sribhashyam has explicitly requested these individuals to prioritize this meeting.

**4. Decisions Made**
*   **Logistics:** The planning session venue has been confirmed as **L11 Room 11**.
*   **Timeline:** The team expects to receive all necessary sign-offs for the production deployment on **March 25, 2026**.

**5. Key Dates & Deadlines**
*   **Date:** March 25, 2026 (Today).
    *   **Deadline/Expectation:** Receipt of all necessary sign-offs is expected today.
    *   **Event:** Production deployment planning session to be held later in the day at L11 Room 11.

**Reference Metrics**
*   **Resource Group:** BCRS Firefighting Group
*   **Space URL:** https://chat.google.com/space/AAQAgT-LpYY


## [60/64] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/T3AnJ6uPt5g | Last Activity: 2026-03-25T01:22:01.467000+00:00 | Last Updated: 2026-03-25T02:56:50.065565+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Initiator of the production deployment planning; has scheduling authority.
*   **Sneha Parab:** Participant providing availability constraints and conflict reporting.
*   **Onkar Bamane:** Identified participant in the thread (no specific action logged).
*   **Daryl:** Participant with conflicting schedule and travel plans.

**Main Topic**
Coordination and rescheduling of the "Production Deployment Planning Session" to accommodate team member availability.

**Decisions Made**
*   The production deployment planning session time has been officially moved from its original slot to **11:00 AM**.

**Pending Actions & Ownership**
*   **No specific pending action items** were generated in this conversation snippet. The primary request (scheduling) was resolved immediately.
*   *Note:* Prajney Sribhashyam indicated they would provide deployment details once the session began, but no new task was created for follow-up after the time change.

**Key Dates & Follow-ups**
*   **Date:** March 25, 2026.
*   **Meeting Time:** 11:00 AM (Confirmed).
*   **Conflicts Avoided:**
    *   Sneha Parab and Daryl have a conflicting meeting at 1:00 PM.
    *   Daryl is unavailable for the entire day due to attendance at the "Project Light session."

**Summary of Discussion Flow**
Prajney Sribhashyam announced an upcoming production deployment planning session. Onkar Bamane was tagged in a follow-up query regarding this announcement. Sneha Parab proposed moving the meeting to 11:00 AM to avoid a 1:00 PM clash and Daryl's unavailability due to the Project Light session. Prajney confirmed the change to 11:00 AM immediately, concluding the discussion with confirmation from Sneha.


## [61/64] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Last Activity: 2026-03-25T00:03:09.772000+00:00 | Last Updated: 2026-03-25T02:57:34.931039+00:00
**Daily Work Briefing Summary (Updated: March 25, 2026)**

**Key Participants & Roles**
*   **Michael Bui:** Primary recipient; responsible for code reviews, UAT support, and project ownership.
*   **Tan Gay Lee / Hendry Tionardi / Olivia:** Finance/UAT coordination (BCRS).
*   **Nikhil Grover / Ravi Singh / Yian Koh:** Programmatic advertising (Advertima/TTD) strategy and testing.
*   **Gautam Singh / Sundy Yaputra / Daryl Ng:** Development leads for Search Indexer, BCRS, and Platform fixes.
*   **James Lai / Mohammed Miran / Andin Eswarlal Rajesh:** iOS Chapter handover responsibilities.

**Main Topics & Discussions**
1.  **Programmatic Advertising (Advertima/TTD):** Focus remains on validating discrepancies for `advertima_ttd-fixed-price-test-1.5`. Ravi Singh confirmed receipt of raw BURLs; validation was targeted for Monday, March 17th. Yian Koh requested confirmation on deals `advertima_ttd-first-price-test` and `advertima_ttd-fixed-price-test-1`.
2.  **New Deal Setup:** Yasmina Tregan (Advertima) required an end-to-end test setup this week. Wei Phung to share live campaign details; Ravi Singh to execute setup, push to TradeDesk, and map segments before launch.
3.  **BCRS UAT & Finance Integration:** Progress on SAP document numbers, duplicate posting fixes via PubSub "exactly once" policy (PR #1033), and Bukit Timah Plaza pricing/display issues.
4.  **Event Sync Optimization (DPD-645):** Addressing the massive event overage (14M vs. normal 550k). PRD deployment plan set for Sunday, March 15.
5.  **Security & Compliance:** RMN Pentest fixes (DPD-700) deployed to Prod; Bitbucket App Passwords deprecated effective June 9, 2026.

**Status Update: Inbox & Communications**
*   **Inbox Status:** As of March 25, 2026, the workspace inbox is fully caught up across all categories (**Urgent Action Items**, **High-Volume/Project Themes**, **Meeting Updates**, and **FYI**). No pending unread items require immediate attention. This status was confirmed in daily summaries dated March 24 and March 25, 2026.

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

**Note on New Content:** Daily summaries received on March 24 and March 25, 2026, confirm the inbox remains clear of urgent action items, meeting updates, and FYI notices. No changes to pending actions or decisions were required based on these updates.


## [62/64] Ping Pong 🏓
Source: gchat | Group: space/AAQAnryjAA8/cFKeWJ-k288 | Last Activity: 2026-03-24T10:42:04.599000+00:00 | Last Updated: 2026-03-24T14:37:00.696439+00:00
**Daily Work Briefing: Ping Pong 🏓**

**Key Participants & Roles**
*   **Zaw Myo Htet:** Initiator of initial communication (Status inquiry).
*   **Michael Bui:** Respondent (Confirmed unavailability; currently in meeting).
*   **Karuna Kemmu:** New participant joining the thread later.

**Main Topic/Discussion**
The exchange began with Zaw Myo Htet initiating a status check ("Pong?") regarding Michael Bui's availability. Michael responded at 09:37 UTC indicating he was occupied with another meeting. Later, Karuna Kemmu entered the conversation to confirm presence. At 10:42:21 UTC, Karuna confirmed that four participants were now present in the space ("Four here now :)"). The primary theme remains availability scheduling for a session or interaction; no specific work deliverables or project tasks were discussed.

**Pending Actions & Ownership**
*   **Action:** Finalize rescheduling for the group interaction once Michael Bui is free.
    *   **Owner:** Karuna Kemmu / Zaw Myo Htet (Implicit coordination required).
    *   **Context:** While four people are currently available, Michael Bui remains in a meeting (confirmed at 10:39 UTC) and cannot join immediately.

**Decisions Made**
*   No concrete decisions were reached regarding the time or topic of the interaction due to Michael's continued unavailability. The group has effectively assembled, pending Michael's departure from his current meeting.

**Key Dates, Deadlines & Follow-ups**
*   **Interaction Date:** March 24, 2026.
*   **Timeline Updates:**
    *   09:36 UTC: Inquiry sent by Zaw Myo Htet.
    *   09:37 UTC: Michael Bui responds (still in meeting).
    *   10:38:50 UTC: Karuna Kemmu asks, "Anyone still there?"
    *   10:39:21 UTC: Michael Bui confirms, "Still in meeting."
    *   10:42:04 UTC: Karuna Kemmu reports, "Four here now :)."
*   **Next Steps:** Await Michael Bui's availability to proceed with the session.

**Resource Details**
*   **Space Name:** Ping Pong 🏓
*   **URL:** https://chat.google.com/space/AAQAnryjAA8
*   **Message Count:** 5


## [63/64] Ping Pong 🏓
Source: gchat | Group: space/AAQAnryjAA8 | Last Activity: 2026-03-24T09:36:20.806000+00:00 | Last Updated: 2026-03-24T10:38:10.266773+00:00
**Daily Work Briefing: Ping Pong Space (Resource ID: AAQAnryjAA8)**

**Key Participants & Roles**
*   **Michael Bui:** Initiator and coordinator. Created the space to facilitate scheduling for informal table tennis (PP/TT) play sessions.
*   **Karuna Kemmu:** Active participant sharing resources.
*   **Zaw Myo Htet:** Active participant initiating a direct query regarding play availability.

**Main Topic/Discussion**
The conversation centers on establishing a coordination channel for informal ping pong activities. Initial discussions focused on recruiting interested colleagues and confirming interest following Michael Bui's "Anyone?" inquiry. The dialogue recently shifted to specific resource sharing and immediate scheduling inquiries. Karuna Kemmu shared an Instagram Reel highlighting pricing tiers for jump rackets (€1–€370) titled "Power of the unsaid," suggesting a discussion on equipment costs or novelty items. Shortly thereafter, Zaw Myo Htet initiated a direct availability check with the message "Pong?"

**Pending Actions & Ownership**
*   **Action:** Respond to Zaw Myo Htet's inquiry ("Pong?") regarding immediate play availability.
    *   **Owner:** Michael Bui and interested team members.
    *   **Context:** Recent activity indicates a pending response to this direct query (last reply noted as 54 minutes prior to current snapshot).
*   **Action:** Expand group membership by identifying additional colleagues.
    *   **Owner:** Michael Bui.
    *   **Context:** Previously acknowledged as necessary to prevent missing potential participants ("I may miss some").

**Decisions Made**
No formal scheduling decisions or time slots were established in the initial phase. The only confirmed operational decision remains the creation of the dedicated Google Chat space for coordination.

**Key Dates & Follow-ups**
*   **Space Creation:** March 19, 2026, at 06:57 UTC (Michael Bui).
*   **Initial Inquiry:** March 19, 2026, at 09:29 UTC (Michael Bui asked "Anyone?").
*   **Resource Sharing:** March 22, 2026, at 12:44 UTC (Karuna Kemmu shared Instagram reel regarding racket pricing).
*   **Availability Check:** March 24, 2026, at 09:36 UTC (Zaw Myo Htet asked "Pong?").

**Reference Data**
*   **Space URL:** https://chat.google.com/space/AAQAnryjAA8
*   **Total Messages:** 6 (Updated from 4).


## [64/64] Soo Ngee Tong
Source: gchat | Group: dm/3L_55SAAAAE | Last Activity: 2026-03-24T08:25:52.255000+00:00 | Last Updated: 2026-03-24T10:40:51.586407+00:00
**Daily Work Briefing: Google Chat Summary**

**Key Participants & Roles**
*   **Michael Bui:** Initiator of the inquiry; demonstrates vigilance regarding cybersecurity threats.
*   **Soo Ngee Tong (Resource):** Subject Matter Expert/Approver; provided confirmation on email legitimacy and context for audit communications.

**Main Topic**
Verification of two emails received by Michael Bui regarding **"KPMG FY 2025 Audit - UAR Self-Review"** to confirm their authenticity and clarify differences between them. The discussion also highlighted potential phishing risks involving URL redirection via Google Classroom.

**Decisions Made**
*   Confirmed legitimacy: Both emails are authorized updates related to **IT audit issues**.
*   Clarification of content: The first email was an initial transmission without context; the second email contains full context and an uploaded video.
*   Risk acknowledgment: Michael Bui acknowledged the need for caution regarding external links, specifically citing the risk of Google Classroom URLs being used for phishing redirection.

**Pending Actions & Ownership**
*   **Action:** Review and process the second email (containing context and video) as instructed by Soo Ngee Tong.
    *   **Owner:** Michael Bui
*   **Action:** Maintain vigilance against potential URL-based phishing attempts while handling audit links.
    *   **Owner:** Michael Bui

**Key Dates & Follow-ups**
*   **Date of Conversation:** March 24, 2026 (Times: 08:23 AM – 08:25 AM UTC).
*   **Reference Project:** KPMG FY 2025 Audit - UAR Self-Review.
*   **Follow-up Status:** Immediate acknowledgment provided by Michael Bui ("Noted, thanks for your confirmation!"). No specific future deadline was set beyond the immediate processing of the confirmed emails.

**Resource Metadata**
*   **Participant:** Soo Ngee Tong
*   **Message Count:** 3
*   **Source URL:** https://chat.google.com/dm/3L_55SAAAAE
