

## [1/31] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 16 | Last Activity: 2026-03-29T14:26:53.042000+00:00 | Last Updated: 2026-03-29T14:33:10.840066+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (Updated March 29, ~14:30 UTC)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
Instability persists into the afternoon of **March 29**. The issue profile has evolved from cyclical failures to a sustained session of intermittent errors affecting Identity APIs, Recommendation Services (Orchid), and Mobile reliability. A new latency spike in Identity API confirmation endpoints was observed this afternoon alongside recurring success rate drops.

**Status Summary & Timeline (March 28–29, Afternoon)**
*   **Identity API Instability (`engage-my-persona-api-go` / Squad Dynamics):**
    *   *Afternoon Activity (13:28 – 14:26 UTC):* Recurring high error rates and latency spikes.
        *   **13:28:** Triggered (Error rate 0.103%); Recovered @ 14:06 UTC (Value 0.087%).
        *   **14:07 – 14:09:** Rapid recurrence of high error rates (Peak 0.104% @ 14:09). Recovered @ 14:09/14:10 UTC.
        *   **14:23:** P90 latency spike for `post_/new-myinfo/confirm` (1.859s); Recovered @ 14:26 UTC.
        *   **14:24:** Success rate drop for `get_/user/profile/myinfo` (99.639%).
    *   *Current Status:* Fluctuating. Recent activity between 13:28 and 14:26 UTC shows persistent volatility. Monitor #92965074 active.
*   **Gamification & Recommendation Services:**
    *   **Orchid Service (`frontend-gateway` / Squad Journey):** Cyclical failures observed late morning and early afternoon.
        *   **13:32 – 13:57:** Triggered (Success rate dropped to 99.865%); Recovered @ 13:57 UTC.
        *   **14:01:** Recovered.
        *   **14:26:** New trigger observed (Success rate 99.869%).
*   **Mobile Reliability:**
    *   **Android (`ef-android` / Squad Compass):** Recurring "view user linkpoints" failures.
        *   **13:57 – 14:01:** Triggered (Metric value ~99.265%); Recovered @ 14:01 UTC.
        *   **14:10 – 14:11:** New trigger observed (Metric value ~98.291%); Recovered @ 14:11 UTC.

**Pending Actions & Ownership**
*   **Investigate Identity API Recurrence:** Analyze repeated error rates (>0.1%) and latency spikes (P90 >1.8s) in `engage-my-persona-api-go` occurring between 13:28 and 14:26 UTC, including the specific `post_/new-myinfo/confirm` delay. Owner: **Squad Dynamics**.
*   **Analyze Orchid Intermittency:** Investigate recurring success rate dips for Orchid (latest at 14:26) correlating with Identity API instability. Owner: **Squad Journey**.
*   **Review Mobile Errors:** Correlate Android linkpoint failures (13:57, 14:10) with concurrent backend issues. Owner: **Squad Compass**, **Squad Dynamics**.

**Decisions Made**
*   **Severity Escalation:** Incidents remain critical due to multi-squad recurrence extending from early morning through the afternoon (latest activity 13:28 – 14:26 UTC).
*   **Pattern Continuity:** The ecosystem instability has shifted to a "sustained cyclical failure" model. New latency issues in `post_/new-myinfo/confirm` have joined existing Identity and recommendation service failures.

**Key Dates & Follow-ups**
*   **Active Window:** March 28–29 (UTC). Recent critical activity: **13:28 – 14:26 UTC**.
*   **Reference Links:**
    *   `engage-my-persona-api-go` Error Monitor #92965074 (Peak: 0.104% @ 14:09)
    *   `post_/new-myinfo/confirm` Latency Monitor #50879027 (P90: 1.859s @ 14:23)
    *   `get_/user/profile/myinfo` Success Rate Monitor #50879029 (Lowest: 99.639% @ 14:24)
    *   `frontend-gateway` Orchid Monitor #17448311 (Latest Trigger: 14:26, Value 99.869%)
    *   `ef-android` Linkpoints Monitor #63109467 (Latest Trigger: 14:10, Value 98.291%)


## [2/31] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Messages: 16 | Last Activity: 2026-03-29T14:17:11.803000+00:00 | Last Updated: 2026-03-29T14:33:52.324613+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Mar 29, 14:17 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`.
*   **Escalations:** `@oncall-dpd-staff-excellence-pdm`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Retail Media.

**Main Topic**
**P2 ALERTS (Resolved):** The `marketing-service` P2 error rate alert triggered at 14:07 UTC and recovered at 14:17 UTC on Mar 29. A separate P2 alert regarding the `frontend-gateway` browse banner page success rate previously triggered at 09:31 UTC and recovered at 09:41 UTC. The critical error on `fp-search-indexer` (Active since Mar 18) persists.

**Pending Actions & Ownership**
*   **Action:** **INVESTIGATE HIGH ERROR RATE (`marketing-service`):** [Status: RESOLVED] Address P2 alert for error rate > 5% on `env:prod`.
    *   **Owner:** Retail Media Team & Grocery Discovery.
    *   **Status:** **RECOVERED (14:17 UTC Mar 29).** Triggered at 14:07 UTC with a metric value of 0.014; recovered at 14:17 UTC reaching 0.0. Monitor ID: `17447106`.
*   **Action:** **INVESTIGATE LOW FILE COUNT (`sku-store-attribute`):** [Status: RESOLVED] Address P3 alert for job processing < 6 files in 4h.
    *   **Owner:** Grocery Discovery Team.
    *   **Status:** **RECOVERED (01:21 UTC Mar 29).** Monitor ID: `20382848`. Last confirmed recovery at 00:59 UTC.
*   **Action:** **INVESTIGATE LOW BANNER SUCCESS RATE (`frontend-gateway`):** [Status: RESOLVED] Address P2 alert for success rate < 99.9% on `env:prod`.
    *   **Owner:** Product Data Management Team (`team:dpd-staff-excellence-pdm`).
    *   **Status:** **RECOVERED (09:41 UTC Mar 29).** Triggered at 09:31 UTC with a metric value of 95.0%; recovered at 09:41 UTC reaching 100.0%. Monitor ID: `17448322`.
*   **Action:** **PERSISTENT INVESTIGATION:** Address critical errors on `fp-search-indexer` (env: prod).
    *   **Owner:** Product Data Management On-Call.
    *   **Status:** Active since Mar 18; no resolution achieved.

**Decisions Made**
*   The `marketing-service` P2 error rate alert (Monitor ID: `17447106`) is confirmed resolved at 14:17 UTC after the metric normalized to 0.0, well below the 0.05 threshold.
*   The incident window for `marketing-service` was brief (approx. 10 minutes), triggering with a peak error rate of 1.4% and resolving automatically.
*   The `frontend-gateway` browse banner alert (Monitor ID: `17448322`) is confirmed resolved following the earlier dip to 95.0% success rate.
*   The `fp-search-indexer` failure continues to require critical focus by Product Data Management.

**Key Dates & Follow-ups (Mar 28–29, 2026)**
*   **Service: `marketing-service` (P2 - Retail Media) [RECOVERED]**
    *   *Latest Timeline:* Triggered Mar 29 (14:07 UTC); Recovered Mar 29 (14:17 UTC).
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/17447106) | [K8s Overview](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview) | [Runbook](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book)
*   **Service: `sku-store-attribute` (P3 - Grocery Discovery) [RECOVERED]**
    *   *Latest Timeline:* Triggered Mar 28 (22:06 UTC); Re-triggered Mar 29 (00:54 UTC); Recovered Mar 29 (00:59 UTC).
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/20382848)
*   **Service: `frontend-gateway` (P2 - Product Data Management) [RECOVERED]**
    *   *Latest Timeline:* Triggered Mar 29 (09:31 UTC); Recovered Mar 29 (09:41 UTC).
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/17448322)
*   **Service: `fp-search-indexer` (P2 - Product Data Management) [ACTIVE CRITICAL]**
    *   *Latest Timeline:* Active since Mar 18; re-triggered Mar 24, 16:29 UTC.

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c


## [3/31] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-03-29T12:27:06.962000+00:00 | Last Updated: 2026-03-29T14:34:42.054355+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Update)**
**Date:** March 29, 2026 (Mid-Morning Shift)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 630

### Key Participants & Roles
*   **System/Tool:** Datadog App (Automated Monitoring)
*   **Notification Channel:** `@hangouts-ShoppingCartNotification`
*   **Ownership Teams:** `dpd-pricing`, `dpd-pricing-cart`.

### Main Topic
Instability persists in `frontend-gateway` and `st-cart-prod`. The incident has evolved into a high-frequency oscillation. While the Shopping List P99 spike (10.72s) remains a historical peak, new critical failures have emerged on **Checkout** reliability (`post /api/checkout`) and recurring severe latency on **Wish List PUT** operations (`put /api/product/_id/wish-list`). The failure mode now spans GET, PUT, and Checkout endpoints with rapid P90/P99 oscillation.

### Incident Timeline & Actions
**Previous Context:**
*   *Activity from March 20–March 28 regarding `frontend-gateway` latency and checkout dips.*

**New Activity (Morning Shift, March 29 UTC)**
*   **06:41–07:32 UTC:** Recurring P90 oscillation on `get /api/wish-list/_id`. Peak P90 reached **1.888s**.
*   **08:11–08:21 UTC:** Severe latency on PUT operations (`put /api/product/_id/wish-list`). P99 triggered at **7.389s**; recovered to ~1.4s within 10 minutes.
*   **09:13–09:23 UTC:** Critical spike on `get /api/v2/shopping-list`. P99 triggered at **10.72s**. Recovered rapidly to **0.483s**.
*   **10:08–10:17 UTC:** Return of `get /api/wish-list/_id` instability. P90 triggered at **2.072s**.
*   **10:40–10:51 UTC (New):** Oscillation on `put /api/product/_id/wish-list`.
    *   P99 triggered at **6.231s** (10:40); recovered to 4.229s (10:51).
    *   P90 triggered at **5.856s** (10:45); recovered to 4.163s (10:50).
*   **11:00–11:10 UTC (New):** New failure on `post /api/checkout`.
    *   P99 triggered at **3.511s** (Threshold: 3.0s); recovered to 1.802s (11:10).
*   **12:15–12:27 UTC (New):** Recurring oscillation on `put /api/product/_id/wish-list`.
    *   P99 triggered at **6.328s** (12:15); recovered to 4.641s (12:27).
    *   P90 triggered multiple times, peaking at **6.231s** (12:24); recovered to 3.794s (12:20) and 4.163s (12:25).

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** The failure scope has expanded to include Checkout (P99 > 3s) alongside persistent PUT latency spikes (>6.3s). The pattern suggests transient resource exhaustion or load balancing issues affecting multiple distinct workflows simultaneously.
*   **Immediate Action Required:** Correlate trace data for the extended window (06:41–12:27 UTC). Investigate Event IDs `8565069685520819045` (10:40 P99), `8565089886996083923` (11:00 Checkout P99), and `8565165319347447763` (12:15 P99).

### Decisions Made
*   **Priority Escalation:** Status remains **"Critical Incident"**. Activity extends continuously from March 20 through at least 12:27 UTC on March 29.
*   **Focus Shift:** Analysis must now cover the Checkout endpoint failure (Monitor `21245705`) alongside established Wish List and Shopping List issues. Correlate Monitor `21245701` (PUT P99), `21245706` (PUT P90), and `21245734` (Shopping List P99).
*   **Metric Update:** Confirmed rotating failure mode: Checkout P99 spiked to 3.511s; PUT Wish List P99 reached 6.328s (12:15) and 7.389s (08:11); Shopping List P99 spiked to 10.72s.

### Key Dates & Follow-ups
*   **Critical Window:** Extended activity from March 20 through at least March 29, 12:27 UTC.
*   **Follow-up:** Immediate trace correlation for the morning oscillation pattern (06:41–12:27 UTC) to determine if the root cause is environmental or traffic-based before shift handover.

### References
*   **Active Monitors:** `21245701` (Wish List PUT P99), `21245706` (Wish List PUT P90), `21245705` (Checkout P99), `21245734` (Shopping List P99).
*   **Service Tags:** `service:frontend-gateway`, `service:st-cart-prod`, `team:dpd-pricing`.


## [4/31] RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU | Last Activity: 2026-03-29T04:32:47.890000+00:00 | Last Updated: 2026-03-29T06:34:38.708958+00:00
**Daily Briefing Summary: RMN Leadership Space (Updated Mar 29)**

**Key Participants & Roles**
*   **Bryan Choong:** Returned from eTail Asia; currently at Thomson Plaza for the ongoing Aussie fair. Prioritizing Q1 case study compilation, low-sodium project, and sampling solutions. Observed 6–7 sampling booths congesting physical traffic flow at the fair.
*   **Pauline Tan:** Managing LinkedIn content (FPG ADvantage page) and award repurposing. Transitioning from award submissions to case study development; tasked with investigating sampling booth spend via Serene.
*   **Rajiv Kumar Singh:** Coordinating SOAC planning; previously shared DoorDash Ads sales lift benchmarks (+30% incrementality).
*   **Allen Umali:** Leading SignCloud cleanup and Advertima loop verification (Legacy hardware status remains active).

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
*   **SignCloud Cleanup:** Complete manual removal of legacy screens and resolve loop errors. *Owner: Allen Umali | Status: Target completion Mar 28 (passed).*
*   **Advertima SRA Renewal:** Secure new SRA for long-term partnership beyond April extended PoV. *Owners: Allen Umali, Alvin Choo.*
*   **SOAC Planning:** Finalize targets per CM, supplier, and category by end of March. *Owner: Rajiv Kumar Singh & Ryan.*

**Decisions Made**
*   **Sampling Strategy:** Accelerate the sampling solution immediately; investigate high-traffic booth congestion at Thomson Plaza (Aussie fair).
*   **Case Study Priorities:** Immediate focus on "low sodium" case study; HPB/APB efforts to utilize repurposed award entries.
*   **SignCloud Resolution:** Manual purging of old screens confirmed, targeting completion by Mar 28.

**Key Dates & Deadlines**
*   **Mar 26:** Pauline Tan submitted award entries (Drum APAC, Retail Asia); Bryan requested case study tracker and low-sodium focus; Rajiv shared DoorDash benchmark data.
*   **Mar 28 (Est.):** Completion of SignCloud manual cleanup.
*   **Mar 29:** Bryan Choong observed sampling booth congestion at Thomson Plaza; directed investigation into spend/traffic impact.
*   **End of March:** Deadline to finalize SOAC targets.
*   **April End:** Current deadline for Advertima extended PoV operations.


## [5/31] RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Last Activity: 2026-03-29T03:21:06.166000+00:00 | Last Updated: 2026-03-29T06:35:32.884010+00:00
**Daily Work Briefing: Automated Test Results Summary (RMN Notification)**

**Key Participants & Roles**
*   **Collection Runner App:** Automated testing agent executing API suites.
*   **Webhook Bot:** Reporting mechanism; consistently returning "unable to process your request" on all notifications through March 29, 2026.
*   **Parties Involved:** System-generated notification log only.

**Main Topic/Discussion**
Automated nightly API test executions across `promo-service`, `marketing-personalization-service`, and `marketing-service` in the **staging** environment. Monitoring period spans March 12 through **March 29, 2026**. Execution windows occur at approximately 01:05 UTC (morning), 02:30/02:31 UTC (midnight), and **03:20/03:21 UTC** (early morning).

**Test Execution Status & Anomalies**
*   **`marketing-service` Stability Confirmation:** The streak of resolution continues.
    *   **March 29, 01:05 UTC:** Executed successfully with **52 API Tests Passed / 0 Failed** and **20 Contract Tests Passed / 0 Failed**. (Total Requests: 17 API, 16 Contract).
    *   **Historical Context:** Recurring instability persisted from March 17 through early March 25. A temporary stabilization occurred on March 25; the morning failure streak was broken on March 26. Stability confirmed for March 26, 27, and 28 as previously noted.
*   **`promo-service`:** Confirmed stable on March 29 at **02:31 UTC**. The latest run showed **10 API Tests Passed / 0 Failed** and **6 Contract Tests Passed / 0 Failed**. (Total Requests: 3 each). Stability confirmed for March 26, 27, 28, and 29.
*   **`marketing-personalization-service`:** New data confirms a successful run at **03:21 UTC on March 29**.
    *   **API Contract Tests:** 125 Passed / 0 Failed (Total Requests: 21).
    *   **API Tests:** 96 Passed / 0 Failed (Total Requests: 21).
    *   This updates the previous status, confirming stability for March 29 in addition to runs on March 27 and 28.

**Pending Actions & Ownership**
*   **Webhook Bot Remediation (High Priority):** The bot failed to process requests in every notification cycle from March 12 through the latest log on **March 29 at 03:21 UTC**. Immediate attention is required from DevOps or Automation Infrastructure.
*   **Verify `marketing-service` Stability:** Engineering must continue monitoring subsequent runs to confirm the resolution of early-morning flakiness observed between March 17–25 was permanent.

**Decisions Made**
*   No human decisions recorded; all entries are automated system outputs.

**Key Dates & Deadlines**
*   **Failure Window (Historical):** Instability noted on March 12, 13, and persistently from **March 17 through March 25**.
*   **Current Status:** Successful runs observed on March 26, 27, 28, and **March 29** across all three services.
    *   `marketing-service`: Passed at 01:05 UTC (March 26–29).
    *   `promo-service`: Passed at 02:30/02:31 UTC (March 26–29).
    *   `marketing-personalization-service`: Passed at 03:20/03:21 UTC (March 27–29).
*   **Monitoring Period:** Data covers runs from **March 12, 2026**, through **March 29, 2026**.

**Resource Info**
*   **Message Count:** 168 notifications logged in the space.
*   **URL:** https://chat.google.com/space/AAQA85dw4So


## [6/31] Nikhil Grover
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


## [7/31] Nikhil Grover
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


## [8/31] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Last Activity: 2026-03-29T00:47:23.112000+00:00 | Last Updated: 2026-03-29T02:36:44.362996+00:00
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

**Current Active/Resolved Sequence (Mar 28–29):**
*   **Incident 1 (Resolved, Mar 28):** Triggered March 28 at 03:26:22 UTC. Story Key: `8874d9ed-c1b1-5d8a-960b-85d280269164`. Recovered at 07:17:22 UTC. Duration ~3h 51m. Status: **[P3] Recovered**.
*   **Incident 2 (Resolved, Mar 29):** Triggered March 28 at 21:27:22 UTC. Story Key: `784f6ec6-03de-5cee-a4e5-9fa93fd78209`. **Recovered** on **March 29, 2026, at 00:47:23 UTC**. Status: **[P3] Recovered**.

### Pending Actions & Ownership
*   **Current Status:** The sequence is currently clear. Incident `784f6ec6...` has self-resolved approximately 3 hours after triggering. No immediate action required pending new triggers.
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Investigation Note:** The recurrence of the "Datadog is unable to process your request" message during the incident window suggests persistent pipeline degradation consistent with historical trends, though the latest event resolved within standard variance.

### Decisions Made
*   **Status:** No escalation triggered for the Mar 28/29 sequence; both incidents self-resolved.
*   **Protocol:** Escalation to SRE/Platform Engineering remains the protocol if a new trigger occurs with similar error messaging and resolution time exceeds 6 hours.

### Key Dates & Follow-ups
*   **Latest Event:** March 29, 2026, at 00:47:23 UTC (Recovery of `784f6ec6...`).
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Continue standard surveillance. The extended duration of the Mar 25 incident (~24h) remains a significant outlier requiring trend analysis alongside current activity.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Datadog Monitor Link:** [View in Datadog](https://app.datadoghq.eu/monitors/17447511)
*   **Latest Incident (Resolved):** https://app.datadoghq.eu/monitors/17447511?group=story_key%3A784f6ec6-03de-5cee-a4e5-9fa93fd78209&from_ts=1774744251000&to_ts=1774745451000&event_id=8564473089519635859

### Monitor Configuration
*   **Query:** `events("source:watchdog (story_category:infrastructure -story_type:(tcp_retrans_jump OR full_disk_forecast)) env:(PROD OR production OR prod)").rollup("count").by("story_key").last("30m") > 0`


## [9/31] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Last Activity: 2026-03-29T00:03:09.735000+00:00 | Last Updated: 2026-03-29T02:37:16.337434+00:00
**Daily Work Briefing Summary (Updated: March 29, 2026)**

**Main Topics & Discussions**
1.  **Programmatic Advertising (Advertima/TTD):** Focus remains on validating discrepancies for `advertima_ttd-fixed-price-test-1.5`. Ravi Singh confirmed receipt of raw BURLs; validation was targeted for Monday, March 17th. Yian Koh requested confirmation on deals `advertima_ttd-first-price-test` and `advertima_ttd-fixed-price-test-1`.
2.  **New Deal Setup:** Yasmina Tregan (Advertima) required an end-to-end test setup this week. Wei Phung to share live campaign details; Ravi Singh to execute setup, push to TradeDesk, and map segments before launch.
3.  **BCRS UAT & Finance Integration:** Progress on SAP document numbers, duplicate posting fixes via PubSub "exactly once" policy (PR #1033), and Bukit Timah Plaza pricing/display issues.
4.  **Event Sync Optimization (DPD-645):** Addressing the massive event overage (14M vs. normal 550k). PRD deployment plan set for Sunday, March 15.
5.  **Security & Compliance:** RMN Pentest fixes (DPD-700) deployed to Prod; Bitbucket App Passwords deprecated effective June 9, 2026.

**Status Update: Inbox & Communications**
*   **Inbox Status:** As of March 29, 2026, the workspace inbox is fully caught up across all categories (**Urgent Action Items**, **High-Volume Project Themes**, **Meeting Updates**, and **FYI**). No pending unread items require immediate attention. This status follows confirmations from daily summaries dated March 24 through March 28. The latest update from Workspace Studio confirms zero backlog in all sections, including Code Reviews and Project Updates.

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

**Note on New Content:** The daily summary from March 29, 2026, via Workspace Studio confirms the inbox remains clear of urgent action items across all categories. No changes to pending actions or decisions were required based on this update; historical context regarding project statuses and deadlines remains valid.


## [10/31] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Last Activity: 2026-03-28T23:01:22.756000+00:00 | Last Updated: 2026-03-29T02:37:47.927066+00:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
Production instability in the Mirakl integration continues into March 28, now extending to a **12-day streak (March 17–28)**. While midday clusters affected `fni-order-create` earlier today, critical latency issues in `picklist-pregenerator` persist late into the night of March 28, indicating sustained service degradation.

**Incident Summary & Timeline**
*   **Service: `fni-order-create` (Mirakl Integration) – Midday Cluster (Mar 28)**
    *   **Trigger Window:** Simultaneous P2 triggers at **11:32 UTC**.
        *   "Exception Occurred At Mirakl Route" triggered at **11:32:39 UTC** (Monitor ID `17447918`).
        *   "Error while calling API" triggered at **11:32:49 UTC** (Monitor ID `17447928`).
    *   **Recovery:** Monitors returned to normal by **11:37:40/50 UTC**. Duration: ~5 minutes.

*   **Service: `fpon-seller-sap-picklist-reporter` (P1 Incident) – Evening (Mar 27)**
    *   Triggered P1 alert "SAP authentication failed" at **19:12:15 UTC**.
    *   Recovered at **19:17:15 UTC**. Duration: ~5 minutes.

*   **Service: `picklist-pregenerator` (Latency Warning) – Late Evening (Mar 28)**
    *   **New Trigger:** P2 Warning "picklist-pregenerator is taking too long to complete" at **23:01:22 UTC**.
    *   **Metric Value:** **3609.298s** (Monitor ID `20383097`).
    *   **Context:** This confirms sustained performance degradation initially observed on March 27 (3608.98s at 23:01 UTC). The recurrence of values exceeding 3,600 seconds indicates a continuous systemic failure rather than an isolated spike.

*   **Service: `fpon-seller-mirakl-order-creation-alert` (Test Alert) – Evening (Mar 27)**
    *   Monitor `29851723` triggered at **19:15:44 UTC** and recovered at **19:16:45 UTC**. A second test cycle occurred from **19:22:44 UTC** to **20:13:45 UTC**.

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of the midday Mirakl instability affecting `fni-order-create` (Mar 28, 11:32 UTC).
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Analyze underlying causes for the P1 SAP authentication failure on `fpon-seller-sap-picklist-reporter` (Mar 27, 19:12 UTC) to prevent recurrence.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Address the critical latency in `picklist-pregenerator`. A second instance of >3,600s execution time occurred at **23:01:22 UTC** on March 28 (Monitor ID `20383097`). Immediate review required to resolve sustained slowness.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Verify logic for Monitor `29851723` following evening test alerts on March 27; ensure they do not mask production issues.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Summary for Leadership**
Mirakl integration instability has expanded to a **12-day streak (March 17–28)**. On **March 28**, a second cluster occurred at **11:32 UTC** affecting `fni-order-create`, triggering simultaneous "Exception Occurred At Mirakl Route" and "Error while calling API" alerts before recovering by **11:37 UTC**. Crucially, instability persisted late into the day; at **23:01:22 UTC**, the `picklist-pregenerator` service triggered a P2 warning with an execution time of **3609.298s** (Monitor ID `20383097`). This mirrors critical latency peaks from March 27, suggesting a continuous degradation pattern rather than isolated incidents. Combined with the earlier P1 SAP authentication failure on March 27 and the midday Mirakl errors, the system exhibits systemic instability requiring urgent engineering review to stabilize production across the `dpd-fulfilment` and `seller-experience` squads.


## [11/31] Nikhil Grover
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


## [12/31] Nikhil Grover
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


## [13/31] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Last Activity: 2026-03-28T15:35:21.604000+00:00 | Last Updated: 2026-03-28T22:39:03.461378+00:00
**Daily Work Briefing: Nikhil Grover & Michael Bui (Updated)**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator; clarifying technical scope, OSMOS logic, and operational controls. Currently finalizing ticket updates for FE team coordination.
*   **Michael Bui:** Technical Lead (Engineering); identified race condition requiring UAT. Clarified implementation constraints regarding page-specific video support and slot sequencing.

**Main Topics & Technical Clarifications (Mar 28)**
1.  **Scope of Video Support & Page Logic:**
    *   Initial confusion arose regarding whether banner/video changes apply to Category/Search pages. Nikhil confirmed that while the logic change applies to all placements, **video content will only be served on Omni Home and FP Pay**. Other pages (Search, Category) route to the legacy MPS service which does not support video UI rendering.
    *   Michael noted this distinction was critical for his estimation; Nikhil clarified Ops controls approval to ensure one video per carousel, even if advertisers bid with videos.

2.  **OSMOS Logic & Slot Management:**
    *   **Endemic Identification:** Confirmed as a Boolean value ("Endemic" or "Non-endemic").
    *   **PCNT Limits:** OSMOS currently limits `pcnt` to 10; support for values >10 is expected by early April. Nikhil will confirm track on Monday.
    *   **Position/Slot Values:** The `position` field (e.g., -1, 0, 2, 999) is optional and used only to exclude multiple banners targeting the same slot from displaying simultaneously. Values like 999 are acceptable provided uniqueness per slot exists. This logic was previously documented in SOPs.
    *   **Fallback Behavior:** If no banners return or OSMOS API is inaccessible, the system returns nothing (banners collapse). Nikhil noted an incident will be created for API failures; Ops manages fallback scenarios.

3.  **Frontend Implementation:**
    *   Auto-play and auto-scroll logic remain frontend-managed; the backend only defines banner sequence.
    *   Michael requested explicit examples for slot values (-1, 0, 999) to ensure accurate FE updates. Nikhil agreed to clarify OSMOS-side controls in the ticket tomorrow.

**Decisions Made & Status Updates**
*   **Documentation:** Nikhil confirmed that if answers cover all technical queries, he will update ticket DPD-838 tomorrow and coordinate with Alvin for implementation details.
*   **Deployment Readiness:** Michael remains available for urgent evening deployments before his April 6th departure but requires clearer scope confirmation on slot logic to proceed confidently.
*   **Revenue Metrics:** Nikhil is still pending the afternoon update of specific numbers based on `pcnt` drops (originally noted as $1250/day).

**Pending Actions & Owners**
*   **Ticket Updates (Nikhil Grover):** Update DPD-838 with explicit slot value examples and OSMOS logic clarifications; coordinate with Alvin.
*   **Monday Confirmation (Nikhil Grover):** Verify the timeline for OSMOS `pcnt` limit expansion (>10) beyond early April estimates.
*   **Ops Approval (Operations Team):** Ensure strict adherence to one-video-per-carousel limits during campaign approval.

**Key Dates & Deadlines**
*   **March 28, 2026:** Technical scope clarified; Nikhil to update tickets tomorrow; Michael reviews slot logic examples.
*   **April 6–12, 2026:** Michael Bui's leave period (island with limited connectivity).

**Historical Context Note**
The conversation pivoted from parameter gaps to a confirmed technical defect: a race condition identified March 27 preventing `swimlane` and `page_name` rendering. While Nikhil initially cited a $1250/day impact, he clarified this includes the overall drop (excluding S$11.5K lost revenue from advertisers who stopped campaigns on March 17). On Mar 28 afternoon, Michael raised six critical questions regarding video scope, OSMOS logic, and slot sequencing. Nikhil clarified that video is restricted to Omni Home/FP Pay via Ops control, slot values are optional for uniqueness rather than sequencing, and PCNT limits >10 are expected by early April. Documentation updates are scheduled for Mar 29 in coordination with Alvin.


## [14/31] Nikhil Grover
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


## [15/31] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/jIquLFJEGIc | Last Activity: 2026-03-28T06:25:47.465000+00:00 | Last Updated: 2026-03-28T10:25:55.877133+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Initiator; clarifies scope and coordinates UAT.
*   **Michael Bui:** Developer/Lead; delivered Jobs 1–3 in UAT; managing PRD deployment logistics while on leave.
*   **Wai Ching Chan & Daryl Ng:** Acknowledged contributors for the delivery of Jobs 1–3.
*   **De Wei Tey:** Clarification requester regarding use case scope.

**Main Topic**
Clarification and status update for the "Re-delivery" use case within BCRS, specifically addressing RPA work dependency and UAT sign-off for non-RPA backend logic (Jobs 1–3).

**Pending Actions & Owners**
*   **UAT Sign-off:** Obtain sign-off for Jobs 1–3 (Order service metadata maintenance, Deposit sales posting update, Duplicate suppression).
    *   *Owner:* Prajney Sribhashyam (to coordinate), with support from Michael Bui/Wai Ching Chan.
    *   *Context:* A separate Jira ticket (**DPD-842**) was created to isolate this work from RPA tasks (**DPD-807**).
*   **PRD Deployment:** Execute deployment for the non-RPA logic during late evening or night hours.
    *   *Owner:* Michael Bui (executing remotely due to connectivity constraints).
*   **RPA Grooming Session:** Pending confirmation from Wai Ching Chan and Michael Bui regarding the 'Re-delivery' use case; proposed by Prajney but not yet scheduled in this thread.

**Decisions Made**
*   **Scope Correction:** The team explicitly clarified that Jobs 1–3 relate to the **"Redelivery"** use case, specifically rejecting the suggestion that they address "pre-order and cancellation after delivery" scenarios.
*   **Scope Separation:** The team agreed to proceed with UAT for Jobs 1–3 independently, without dependency on concurrent RPA work.
*   **Deployment Timing:** Michael Bui will handle PRD deployment during off-peak hours (late evening/night) due to upcoming leave and unstable daytime connectivity while on islands.

**Key Dates & Follow-ups**
*   **Date of Conversation:** March 28, 2026.
*   **Next Milestone:** Michael Bui will assist with PRD deployment "next week" (specific timing subject to his connectivity).
*   **Follow-up:** Prajney Sribhashyam committed to providing a status update soon ("Let me give you an update soon").

**Relevant References**
*   **Jira Tickets:** DPD-807 (RPA/General), DPD-842 (Non-RPA UAT).
*   **Chat URL:** https://chat.google.com/space/AAQAgT-LpYY


## [16/31] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/jfuh2YauMzM | Last Activity: 2026-03-28T03:54:16.091000+00:00 | Last Updated: 2026-03-28T10:27:07.620021+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Michael Bui:** Developer responsible for root cause analysis, fix execution, and testing.
*   **Alvin Choo:** Primary recipient querying deployment status; provided flexibility on timing.
*   **Daryl Ng:** Team lead for `website-service`, coordinating code reviews.

**Main Topic**
Resolution of an RMN incident in the `website-service` module, focusing on UAT verification and finalizing the deployment window (Monday evening/night vs. Monday office hours).

**Pending Actions & Ownership**
*   **Regression Testing:** Michael Bui to manually verify that daily morning regression tests show no failures for other functionalities. [Owner: Michael Bui]
*   **Code Review:** Daryl Ng's team to review the PR submitted by Michael Bui. [Owner: Daryl Ng's Team]
*   **Production Deployment (Revised):** Scheduled for Monday evening/night, coordinated with a BCRS change. Alternatively, Alvin Choo has opened the option to deploy during Monday office hours if the team can assist. Final timing pending approval and coordination. [Owner: Michael Bui / Approver: Hui Hui]

**Decisions Made**
*   **UAT Verification Confirmed:** Testing on UAT is complete. The fix corrected the number of requested ads from a degraded value (1) to the correct count (6). Documented in Jira DPD-715 with screenshots.
*   **Risk Assessment:** Michael Bui assessed low risk, noting the root cause is specific to a single race-condition scenario involving one shared variable/object.
*   **Deployment Timing Flexibility:** The team agreed to delay deployment from the weekend (March 27–28) to Monday due to lower urgency compared to Nikhil's request. Alvin Choo confirmed acceptance of "Monday night" but explicitly stated an alternative: the team may deploy during Monday office hours if assistance is available.

**Key Dates & References**
*   **Incident Date/Time:** March 27, 2026 (14:50 UTC).
*   **UAT Confirmation Timestamp:** March 28, 2026 (03:08 UTC) – Michael Bui confirmed UAT success.
*   **New Deployment Discussion Timestamp:** March 28, 2026 (03:54 UTC) – Alvin Choo confirmed flexibility for Monday night or office hours.
*   **PR Link:** https://bitbucket.org/ntuclink/website-service/pull-requests/652/overview
*   **Jira Ticket:** DPD-715 (https://ntuclink.atlassian.net/browse/DPD-715) – Updated with UAT verification and timestamps.
*   **Service Scope:** `website-service`.

**Note on Previous Assumptions**
The previous assumption of a mandatory weekend deployment window has been superseded by the decision to wait until Monday. The specific timing for Monday is now flexible: either evening/night (bundled with BCRS) or during office hours, contingent on team availability.


## [17/31] [BCRS]-SAP to POS & DBP Interface Deployment
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


## [18/31] BCRS Firefighting Group
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


## [19/31] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY | Last Activity: 2026-03-28T03:04:56.114000+00:00 | Last Updated: 2026-03-28T03:50:15.426830+00:00
**Updated Briefing: BCRS Firefighting Group**
**Date:** March 28, 2026 (Latest activity: ~3:28 AM)
**Source:** Google Chat Space & Shared UAT Tracker (80 messages total)

### **Key Participants & Roles**
*   **Prajney Sribhashyam:** Project Lead/Test Coordinator.
*   **De Wei Tey / Michael Bui / Wai Ching Chan:** Finance/SAP, Re-delivery specialists, and Technical Integration.
*   **Dany Jacob / Eswarlal Rajesh / Sneha Parab:** Active test participants and finance coordinators.
*   **Alvin Choo:** Status reporting lead (monitoring Starship channel updates).

### **Main Topics**
1.  **UAT Readiness & RPA Mobilization:** Prajney Sribhashyam confirmed that Jobs 1 to 3 are ready in UAT as of March 28, pending confirmation on RPA work readiness. The focus has shifted to immediate grooming for the 'Re-delivery' use case (Jira DPD-807).
2.  **Re-delivery Use Case Definition (DPD-807):** A quick grooming session is required today to define workflows for:
    *   Order service maintaining 'Deposit posted to SAP' in metadata.
    *   Deposit sales posting updating this field upon first completion.
    *   Consumption of the field to suppress duplicate BCRS deposit postings.
    *   RPA charging the customer's original payment method and posting BCRS deposit sales.
3.  **Status Reporting:** Alvin Choo requested an overall status update following recent changes noted in the Starship channel, noting visibility for 10 of 39 members.

### **Decisions & Updates**
*   **Schedule Adjustment:** The timeline has shifted from March 26 (Michael Bui's departure/deployment day) to immediate action on March 28 following UAT readiness confirmation. Michael Bui and Wai Ching Chan are explicitly requested for assistance with the Re-delivery case.
*   **Testing Scope:** While previous E2E production testing was targeted for March 26, current priority is validating UAT Jobs 1-3 before proceeding to RPA execution.

### **Pending Actions & Owners**
| Action Item | Owner(s) | Status/Context |
| :--- | :--- | :--- |
| **Re-delivery Grooming Session (DPD-807)** | Prajney Sribhashyam / Michael Bui / Wai Ching Chan / De Wei Tey | **Urgent:** Schedule and execute "quick grooming" today to finalize metadata, sales posting, and RPA workflows. Last reply: 25 min ago. |
| **Overall Status Update** | Prajney Sribhashyam / Team | **Pending:** Provide comprehensive update to Alvin Choo regarding Starship channel changes and UAT progress. |
| **RPA Work Validation** | De Wei Tey / Wai Ching Chan | **Active:** Confirm readiness for RPA execution now that Jobs 1-3 are in UAT. |
| **UAT Job Verification** | Prajney Sribhashyam | **Completed:** Jobs 1 to 3 confirmed ready in UAT (March 28). |

### **Key Dates & Deadlines**
*   **March 28 (Today):** Target for Re-delivery grooming session and RPA readiness confirmation.
*   **Historical Deadline Note:** The original SAP Deposit API development deadline of Feb 20 remains noted as missed/risked; current focus is on resolving the specific re-delivery logic gaps.

### **Historical Context Retained**
*   Existing e-comm test accounts remain unusable for Pre-order staff app; new BCRS CF items and specific GWP SKUs required.
*   Deposit SKU linking investigation continues due to failure to link post-publishing.
*   Re-delivery flow testing previously experienced audio issues on March 16; current effort aims to resolve logic gaps via the grooming session.


## [20/31] Nikhil Grover
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


## [21/31] [Leads] (Ecom/Omni) Digital Product Development
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


## [22/31] [Prod Support] Ecom FFS Ops
Source: gchat | Group: space/AAAAde_cYKA | Last Activity: 2026-03-28T01:45:21.232000+00:00 | Last Updated: 2026-03-28T02:35:54.742047+00:00
**Daily Work Briefing: [Prod Support] Ecom FFS Ops (Updated Mar 28)**

**Key Participants & Roles**
*   **Wai Ching Chan / Sampada Shukla:** Operations/Product Leads.
*   **TL HCBP FFS:** Store Lead reporting T18/T19 picking queue blockages and scan issues.
*   **Adrian Yap Chye Soon:** Technical Lead/Support (investigating data anomalies and dispatcher app failures).
*   **Akash Gupta:** DPD / Fulfilment / On Call.
*   **Yoongyoong Tan:** Reporting HCBP picking Q issues.
*   **Ler Whye Ling Angel:** Escalation point for "No picking Q."

**Main Topics**
1.  **Packlist Discrepancies & Validation:** Ongoing investigation into critical `packed_qty` anomalies (NULL values or massive mismatches vs. `delivered_qty`).
    *   **Critical Incident (Mar 26):** Akash Gupta identified two orders at **VivoCity (Store ID 170)** showing `packed_qty` > 13M against `delivered_qty` of <20.
        *   Order #22912255: `packed_qty` 13,165,999 vs. `delivered_qty` 12.
        *   Order #22906879: `packed_qty` 13,165,999 vs. `delivered_qty` 18.
    *   **Historical Context:** Incidents include Mar 25 Sun Plaza (Order #22898981) and prior anomalies at Hyper Sports Hub.

2.  **Dispatcher App & Zone Scanning Failure (Mar 28):** New escalation regarding the dispatcher app's inability to scan new zones.
    *   **01:45 AM Mar 28:** Adrian Yap Chye Soon reported that the dispatcher app is unable to scan the new zone at **hvivo** (High Vivo/Healthcare VivoCity context). A video demonstration was provided for review.

3.  **HCBP Picking Queue Issues (Mar 27):** Escalated urgency regarding "No picking Q" blockage and T18 display failures.
    *   **Timeline:** Initial blockage reported 02:08 AM; escalated by Ler Whye Ling Angel at 02:52 AM; T18 data failure reported by TL HCBP FFS at 07:47 AM with follow-up at 07:53 AM.

**Pending Actions & Ownership**
*   **Dispatcher App Investigation (Urgent - Mar 28):**
    *   *@Adrian Yap Chye Soon / Technical Team:* Investigate the "unable to scan new zone" failure at hvivo based on the video evidence provided by Adrian.
    *   *@Wai Ching Chan @Sampada Shukla:* Review the uploaded video and coordinate resolution for the dispatcher app issue.
*   **Critical Data Validation (Mar 26):**
    *   *@Akash Gupta / On Call:* Confirm massive `packed_qty` mismatches for Orders #22912255 and #22906879 at VivoCity. Sun Plaza validation remains pending.
*   **HCBP Queue Investigation (Mar 27):**
    *   *@Adrian Yap Chye Soon / @Gopalakrishna Dhulipati:* Continue monitoring the resolution of Mar 27 "No picking Q" and T18 display failures following escalated pings from Ler Whye Ling Angel and TL HCBP FFS.

**Decisions Made**
*   **App Release Strategy:** Picker App 10.4.0 rollout remains on hold pending resolution of critical data anomalies (Mar 18–27). Full rollout is contingent on stability post-fixes, specifically addressing the Mar 26 VivoCity alerts, the resolved Mar 27 HCBP queue/T18 failures, and the **new dispatcher app zone scanning issue at hvivo**.

**Key Dates & Deadlines**
*   **Immediate:** Validation of Mar 26 Orders #22912255/#22906879; Root cause analysis of Mar 28 Dispatcher App failure at hvivo.
*   **Pending:** RCA for recent `packed_qty` anomalies across Sports Hub, VivoCity, Parkway, Changi, Sun Plaza, Hyper VivoCity.

**Critical Alerts**
*   **Active Alert (Mar 28):** Dispatcher app unable to scan new zone at **hvivo**. Video evidence available; requires immediate technical check by @Adrian Yap Chye Soon and Ops leads.
*   **Secondary Active Alert (Mar 27):** HCBP "No picking Q" issue escalated by Ler Whye Ling Angel.
*   **Tertiary Active Alert (Mar 26):** Two orders at VivoCity showing `packed_qty` (~13M) >> `delivered_qty`.


## [23/31] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/z2zSDKRl4Vc | Last Activity: 2026-03-28T00:08:06.077000+00:00 | Last Updated: 2026-03-28T02:36:43.651556+00:00
**Daily Work Briefing: [Internal] (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Michael Bui:** Initiator/Requester (Submitted PR review request).
*   **Daryl Ng:** Review Lead/Scheduler (Requested peer reviews for upcoming work).
*   **Yangyu Wang, Lester Santiago Soriano, Sundy Yaputra, Zaw Myo Htet, Chee Hoe Leong:** Assigned reviewers.

**Main Topic/Discussion**
The conversation focuses on code review requirements for a specific Pull Request (PR) regarding the suppression of BCRS deposit posting within the re-delivery journey. Additionally, Daryl Ng initiated a schedule for peer reviews concerning work planned for the following week.

**Pending Actions & Ownership**
*   **Action:** Review PR #7 at `https://bitbucket.org/ntuclink/bcrs-deposit-posting/pull-requests/7` to suppress BCRS deposit posting in the re-delivery journey.
    *   **Owner:** @Daryl Ng (Explicitly requested by Michael Bui).
*   **Action:** Assist with upcoming review tasks for next week's deliverables.
    *   **Owners:** @Yangyu Wang, @Lester Santiago Soriano, @Sundy Yaputra, @Zaw Myo Htet, @Chee Hoe Leong (Assigned by Daryl Ng).

**Decisions Made**
*   No formal technical decisions or approvals were recorded in this snippet. The thread consists of a direct request for review and an administrative instruction to assign reviewers.

**Key Dates & Follow-ups**
*   **Initiation Date:** March 27, 2026 (19:33 UTC) – Michael Bui posted the PR link.
*   **Assignment Date:** March 28, 2026 (00:08 UTC) – Daryl Ng expanded the review list.
*   **Upcoming Deadline/Focus:** "Next week" – The specific tasks assigned to the five reviewers are targeted for this upcoming period.

**References**
*   **PR Link:** `https://bitbucket.org/ntuclink/bcrs-deposit-posting/pull-requests/7`
*   **Space URL:** `https://chat.google.com/space/AAQAUbi9szY`


## [24/31] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/rKtZEQsyOFI | Last Activity: 2026-03-27T20:20:12.120000+00:00 | Last Updated: 2026-03-27T22:37:56.202521+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Michael Bui:** Lead developer/technical contact; created initial Confluence documentation for RMN integration.
*   **Alvin Choo:** Decision maker (likely Technical Lead or Manager); requested draft prior to leave.
*   **Gopalakrishna Dhulipati:** Tagged participant (no direct action in this thread).

**Main Topic**
Coordination with the CoMall team regarding "Project Light Attack and Defence" kick-off, focusing on contract status, engagement timing, and finalizing Technical API Specifications (Tech Spec) for RMN pieces.

**Decisions Made**
1.  **Engagement Timing:** Do not connect with the CoMall team or create a Google Chat space immediately; wait until the official kick-off/grooming next week as they are not yet awarded.
2.  **Documentation Platform:** Use Confluence for API specifications (confirmed implemented).
3.  **Template Approach:** Initial drafts created immediately to ensure consistency across Payments, FP Pay, and Identity teams. Perfection is not required; content can be refined later.

**New Developments & Status Updates**
*   **Draft Completion:** Michael Bui has successfully created two Confluence documents today (March 27, 2026), fulfilling the request to draft before his upcoming leave.
    *   **Display (Banner/Video) Ads:** Documented as currently supported with minimal changes required for Project LIGHT.
        *   *Link:* https://ntuclink.atlassian.net/wiki/spaces/LIGHT/pages/3346989110/Finalizing+Display+Ads+Banner+Video
    *   **Dynamic Ads in PLP Content Cards:** Documented as not currently available; requires development for Project LIGHT.
        *   *Link:* https://ntuclink.atlassian.net/wiki/spaces/LIGHT/pages/3347120197/Draft+Dynamic+Ads+in+the+PLP+Content+Card
*   **Next Step:** Awaiting Alvin Choo's review of the document layout and content.

**Pending Actions & Ownership**
*   **Review Draft:** Alvin Choo to review the two new Confluence documents for format and content accuracy.
*   **CoMall Alignment:** Prepare standardization discussion for Payments, FP Pay, and Identity teams during next week's kick-off.

**Key Dates & Deadlines**
*   **Today (March 27, 2026):** Michael Bui completed Confluence draft templates.
*   **Next Week:** Scheduled kick-off/grooming session with CoMall.
*   **Upcoming:** Michael Bui is on leave soon; immediate drafting action has been prioritized and executed.

**Specific References**
*   Contract status: Unconfirmed/Awaited award.
*   Services involved: Payments, FP Pay, Identity.
*   Document format: Confluence draft (exportable to PDF if CoMall lacks access).
*   RMN Integration Scope: Display Ads (supported) and Dynamic Ads in PLP Content Cards (requires dev).


## [25/31] [Internal] (Ecom/Omni) Digital Product Development
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


## [26/31] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Last Activity: 2026-03-27T14:50:23.456000+00:00 | Last Updated: 2026-03-27T22:40:29.012704+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Sneha Parab:** Lead/Manager; coordinating cross-team support, SAP/API integration blockers.
*   **Michael Bui:** Engineering/RMN Architect; identified root cause for the RMN incident and preparing UAT verification.
*   **Alvin Choo:** Leadership; addressing approval workflows for weekend deployments and release schedules.
*   **Daryl Ng:** Investigating store network ownership, Omni Home data discrepancies (currently away).
*   **Others Active:** Andin Eswarlal Rajesh, Olivia, Koklin, Zaw, Ravi.

**Main Topics & Updates**
1.  **RMN Incident Resolution:** Michael Bui identified the root cause for the RMN incident and is implementing a fix pending UAT verification. Immediate guidance is required on deployment protocols: if deploying over the weekend (Sat/Sun), the process involves sending an approval request to Hui Hui.
2.  **Search Performance Drop:** Investigation continues regarding the severe 60–70% impression decline since March 18/19. The RMN root cause fix may correlate with these symptoms; release timing remains contingent on this investigation and UAT success.
3.  **Epic Lifecycle Query (DPD-710):** Sneha Parab flagged a technical live date of March 19, 2026, for the Omni ticket. With Daryl Ng away, closure validation awaits Michael Bui's input on whether the epic is safe to close immediately.
4.  **SIT Timeline & Redelivery Risk:** Discussion continues on SIT delivery feasibility before April 6/7 contingent on Knowledge Transfer (KT). Adrian remains unavailable for redeliveries between April 1–7 due to duplicate posting risks without a completed handover.
5.  **Infrastructure Compliance:** Bitnami ending free Docker images mandates migration for `sonic_raptor` and `mkp-fairnex`.

**Pending Actions & Owners**
*   **RMN Deployment Approval:** Confirm weekend deployment process (send approval request to Hui Hui) following UAT verification of the fix. (Owner: Michael Bui; Coordination: Alvin Choo/Hui Hui)
*   **Epic Closure Validation:** Determine if DPD-710 can be closed given the March 19 live date discrepancy. (Owner: Michael Bui; Requestor: Sneha Parab)
*   **SIT Delivery Assessment:** Evaluate KT feasibility to complete SIT before April 6/7. (Owners: Michael Bui/Daryl Ng)
*   **Store Network Ownership:** Confirm scope under Data COE vs. Miguel's team regarding `Omni Home` store ID mismatch (OMNI-1157). (Owner: Daryl Ng/Michael Bui)
*   **SAP Timeline Resolution:** Resolve deposit SKU data integration blockers. (Owners: Sneha Parab/Alvin Choo/Gopalakrishna Dhulipati)
*   **RAW Forms Review:** Complete Risk Register review for DPD RAW forms; confirm handovers and renew expired forms by Tomorrow EOD. (Owner: All Leads/Sazali Bin Mohammed Ali's team)

**Decisions Made & Status Changes**
*   **RMN Fix Status:** Root cause identified; moving to UAT verification. Deployment timing (weekend vs. weekday) is currently being debated.
*   **Release Strategy:** Regular app release status remains pending the search performance investigation and RMN fix validation.
*   **Architecture Updates:** Michael Bui has updated current, future, and transition architecture diagrams.

**Key Dates & Deadlines**
*   **RAW Forms Review:** Due Tomorrow EOD.
*   **Adrian Redelivery Block:** Unavailable Apr 1–7 due to duplicate posting risks.
*   **SIT Target:** Potential delivery by April 6/7 contingent on KT success.
*   **Chee Hoe Support:** Effective end of March for Product Catalogue/MarTech scope.
*   **DPD-710 Live Date:** March 19, 2026 (Subject to validation).


## [27/31] #dpd-dba
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


## [28/31] [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Last Activity: 2026-03-27T11:29:59.041000+00:00 | Last Updated: 2026-03-27T14:35:43.145971+00:00
**Daily Work Briefing: [Prod Support] Marketplace**

**Key Participants & Roles**
*   **Support/Operations:** Willie Tan, Iris Chang, Lalita Phichagonakasit, Charlene Tan, Jie Yi Tan, Ayton See, Amos Lam, Michelle Lim.
*   **Technical/Admin Team:** Dang Hung Cuong, Shiva Kumar Yalagunda Bas (Frequent recipients of access/access issues), Olivia -, Jill Ong, Greta Lee, Zaw Myo Htet, Angella Yeo, Cassandra Thoi, Gopalakrishna Dhulipati, Ee Ling Tan.

**Main Topics & Discussion Summary**
Discussions continue to focus on operational blockers regarding seller onboarding, order fulfillment discrepancies, system configuration errors, and data visibility gaps. Major themes include:
1.  **Data Visibility Gap:** Greta Lee (Mar 27, 08:51 UTC) requested live dashboards for daily MP ordered quantities for specific SKUs, citing a discrepancy between the current forecast cutoff (4 AM) and real-time high run-rate volume. She tagged Dang Hung Cuong, Shiva Kumar Yalagunda Bas, and Amos Lam.
2.  **PickerApp Barcode Errors:** Dang Hung Cuong is investigating a truncation issue for Pureen (SAP: 90247763), where the system displays `95561234717` instead of `9556123471735`. Greta Lee also flagged SKU 90244060 for Yumsay Foods as non-existent.
3.  **Access Management:** Amos Lam (Mar 27, 10:00 UTC) requested PickerApp access linkage for Seller ID 31435 (Nathalie Huang, nathalie.huang@alphico.com.sg), code `69c621405ddaee7f20b504ea`. **Status Update:** Shiva Kumar Yalagunda Bas confirmed completion of this request at 11:29 UTC on Mar 27.

**Pending Actions & Ownership**
*   **Live Dashboard Request:** Technical team to provide or configure a live dashboard for daily MP ordered quantities to bridge the 4 AM–current time gap (Greta Lee, Mar 27).
*   **Truncated Barcode Investigation:** Dang Hung Cuong to investigate Pureen's barcode truncation issue.
*   **PickerApp SKU Error:** Technical team to investigate why SKU 90244060 for Yumsay Foods is flagged as non-existent.
*   **Urgent Promotion Removal:** Dang Hung Cuong and Gopalakrishna Dhulipati to remove incorrectly set up promotion for Item ID: 90244361 (Lalita Phichagonakasit, Mar 20).
*   **Picklist Verification:** Dang Hung Cuong to confirm picklist delivery status for Sinhua Hock Kee Order #257719344.
*   **Order Status Investigation:** Team to check discrepancies for Order #256055476 and Order #248407866.
*   **Vendor Report Issues:** Investigate missing sales breakdown reports for CoLab Apac (NED-277148) and Old Shanghai (NED-277329).

**Decisions Made**
*   Dang Hung Cuong is prioritizing the removal of Item ID: 90244361, the new picklist failure issue raised by Amos Lam, the Woah Group offers error, and the current barcode truncation investigation for Pureen.
*   Dang Hung Cuong and Shiva Kumar Yalagunda Bas are assigned to investigate the vendor picklist anomaly.
*   **Completed:** Access linkage for Seller ID 31435 (Nathalie Huang) has been successfully executed by Shiva Kumar Yalagunda Bas on Mar 27, 11:29 UTC.

**Key Dates & Deadlines**
*   **2026-03-27 (Today):** Greta Lee reported data visibility gap; Dang Hung Cuong, Shiva Kumar Yalagunda Bas, and Amos Lam tagged. Amos Lam requested access for Seller ID 31435; **Shiva Kumar Yalagunda Bas completed the access grant at 11:29 UTC.** Lalita Phichagonakasit previously reported Pureen barcode truncation.
*   **2026-03-26:** Iris Chang requested sales report for UNICO Distribution Services; Greta Lee reported Yumsay Foods barcode issue; Ee Ling Tan queried picklist delivery.
*   **2026-03-25:** Cassandra Thoi requested checks on orders #256055476 and #248407866.
*   **2026-03-21:** Amos Lam reported vendor picklist failure due to public holiday opt-out status.


## [29/31] RMN Incidents
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


## [30/31] RMN Incidents
Source: gchat | Group: space/AAQAz11ATzY | Last Activity: 2026-03-27T10:29:57.571000+00:00 | Last Updated: 2026-03-27T10:39:22.553372+00:00
**Daily Work Briefing: RMN Incidents (Updated)**

**Key Participants & Roles**
*   **Nikhil Grover:** Issue initiator; escalated urgency for resolution by EOD March 27th. Recently requested an update on the investigation status.
*   **Rachit Sachdeva:** Investigator; identified a systemic configuration issue regarding product count parameters. Currently preparing detailed data via email.
*   **Stakeholders (CC'd):** Shubhangi Agrawal, Michael Bui, Allen Umali, Rajiv Kumar Singh, Ravi Goel.
*   **New Involvement:** Rahul Jain (noted in update request).

**Main Topic**
Critical investigation into a 50% drop in product ad impressions and $11k revenue loss since March 17th. Initial hypotheses regarding paused campaigns were refuted by Nikhil, who noted single-SKU responses persist despite active advertisers. Rachit has now identified the root cause: a configuration anomaly where the `f_pcnt` parameter (requested product count) is set to 1 in over 90% of CATEGORY and 98% of SEARCH page requests, forcing single-product system responses regardless of available inventory.

**Critical Findings & Data**
*   **Root Cause Identified:** The issue is not supply-side pausing but a request parameter configuration. When `f_pcnt` equals 1, the system returns only one product per call.
    *   **CATEGORY Pages:** Requests with `f_pcnt`=1 consistently exceeded 90% (Mar 20–27).
    *   **SEARCH Pages:** Requests with `f_pcnt`=1 consistently exceeded 98% (Mar 20–27).
*   **Previous Context:** While Rachit initially noted 24 paused advertisers generating $11.5k revenue (Mar 1–17), this was insufficient to explain the single-SKU output observed in active campaigns (e.g., Ferrero, Colgate). The new data confirms the "single response" behavior is driven by the parameter count, not advertiser availability.

**Decisions Made**
*   **Root Cause Confirmation:** The issue has shifted from a supply-side analysis to a configuration review of product count filters (`f_pcnt`).
*   **Priority Status:** Elevated to immediate resolution; Nikhil requested an update on March 27th at 08:34 UTC.

**Pending Actions & Ownership**
*   **Action:** Investigate recent updates or changes to the configuration governing product count filters in requests.
    *   **Owner:** Team (Rachit Sachdeva to confirm with stakeholders).
*   **Action:** Distribute detailed data analysis regarding the March 20–27 trends for `f_pcnt`.
    *   **Owner:** Rachit Sachdeva (Email follow-up pending confirmation of findings).
*   **Action:** Resolve the configuration override to allow multi-SKU responses when multiple active campaigns exist.
    *   **Owner:** Engineering Team / Technical Owners.

**Key Dates & Deadlines**
*   **Incident Start Date:** March 17th (campaign pauses observed; impact noted).
*   **Latest Update:** March 27th, 2026 at 08:34 UTC (Nikhil follow-up); 10:29 UTC (Rachit root cause analysis).
*   **Data Window:** Mar 1–17 (Revenue baseline); Mar 20–27 (Current `f_pcnt` trend analysis).
*   **Deadline:** Resolution required by end of day on March 27th.

**Attachments Referenced**
*   `FPG _ Paused Advertisers (1).xlsx` (Shared by Rachit on Mar 26; reviewed by Nikhil on Mar 27).
*   **New Data:** Detailed analysis regarding `f_pcnt` trends for March 20–27 (to be sent via email by Rachit).


## [31/31] Team Starship
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
