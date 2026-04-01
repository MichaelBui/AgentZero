

## [1/57] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 16 | Last Activity: 2026-03-31T22:28:00.561000+00:00 | Last Updated: 2026-03-31T22:33:59.393312+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (Updated March 31, ~22:30 UTC)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
Instability in the `engage-my-persona-api-go` service persists into the evening of March 31. Following earlier afternoon spikes, a new wave of errors, latency violations, and success rate drops emerged after **21:35 UTC**, affecting Identity, Gamification, Banner carousel, and Recommendation services (Orchid/Boughtbought).

**Status Summary & Timeline (March 31 Evening)**
*   **Identity API Instability (`engage-my-persona-api-go` / Squad Dynamics):**
    *   *Error Rate Cycles:* Triggered repeatedly between **21:35 UTC and 22:28 UTC**. Notable peaks: 0.116 (21:35), 0.105 (22:07), 0.111 (22:10), and 0.102 (22:28). Recovered briefly to <0.1 between incidents.
    *   *Latency Spikes:*
        *   `post_/new-myinfo/confirm`: P90 latency exceeded 1.8s at **22:10 UTC** (Metric: 0.987, indicating 98.7% of requests were slow).
        *   `post_/new-myinfo/oidc/token`: P90 latency exceeded 1.8s at **22:21 UTC** (Metric: 2.04). Recovered by 22:28 UTC.
*   **Gamification Service (`engage-gamification-api` / Squad Dynamics):**
    *   *Error Rate Spike:* Triggered at **21:43 UTC** with a critical metric value of **5.882**. Recovered by 21:53 UTC.
*   **App & Banner Availability (`marketing-personalisation` / Squad Compass):**
    *   *Banner Carousel Failures:* `post_/banner` success rate dropped below 99.9% at **21:38 UTC** (Metric: 100.0, likely noise/transient). Recovered immediately.
*   **Recommendation Services (`frontend-gateway` / Squad Journey):**
    *   *Boughtbought Failures:* Success rate dropped significantly to **85.714%** at **22:23 UTC**.
    *   *Orchid Failures:* Success rates dipped below 99.9% at **21:43 UTC** (Metric: 100.0) and again at **22:23 UTC** (Value: 99.312%).

**Pending Actions & Ownership**
*   **Investigate Identity API Correlation:** Analyze the recurrence of error spikes (21:35–22:28 UTC) against latency issues on `post_/new-myinfo/confirm` and `post_/new-myinfo/oidc/token`. Owner: **Squad Dynamics**.
*   **Diagnose Gamification Crash:** Investigate the severe 5.882 error rate spike at 21:43 UTC for `engage-gamification-api`. Owner: **Squad Dynamics**.
*   **Monitor Recommendation Degradation:** Address the critical Boughtbought failure (85.714%) and recurring Orchid issues observed at 22:23 UTC. Owner: **Squad Journey**.

**Decisions Made**
*   **Status Update:** Incident severity remains Critical due to continuous, cyclical failures across Identity, Gamification, and Recommendation services extending from the afternoon (09:58–14:20) through late evening (21:35–22:30).
*   **Pattern Confirmation:** The 21:35 UTC error spike in `engage-my-persona-api-go` and the severe 21:43 UTC gamification error confirm a persistent instability cycle affecting multiple squads simultaneously.

**Key Dates & Follow-ups**
*   **Active Window:** March 31, 21:35 – 22:30 UTC (Latest Critical Activity).
*   **Reference Links (Latest):**
    *   `engage-my-persona-api-go` Error Rate Monitor #92965074 (Triggered: 21:35, 22:07, 22:10, 22:28)
    *   `post_/new-myinfo/oidc/token` Latency Monitor #94562095 (Triggered: 22:21, Value: 2.04s)
    *   `gamification-api` Error Rate Monitor #92939290 (Triggered: 21:43, Value: 5.882)
    *   `frontend-gateway` Boughtbought Monitor #17448306 (Triggered: 22:23, Value: 85.714%)


## [2/57] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Messages: 16 | Last Activity: 2026-03-31T21:50:11.560000+00:00 | Last Updated: 2026-03-31T22:34:37.365886+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Mar 31, 21:50 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`, `@opsgenie-dpd-grocery-discovery`.
*   **Escalations:** `@oncall-dpd-staff-excellence-pdm`, `@hangouts-GT-Search-DatadogAlerts`, `@hangouts-GT-Discovery-DatadogAlerts`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Retail Media.

**Main Topic**
**P2 INCIDENT (RESOLVED):** Google PubSub backlog affecting pricing data in DBP via `sap-job-file-plu-subscription`.
*   **Current Status:** Resolved at 21:50 UTC after auto-recovery. No active P2 incidents remain for this service.
*   **Incident Timeline:**
    *   **Triggered:** Mar 31, 20:35 UTC (Oldest unacked message age: 5474s / ~1.5h).
    *   **Recovered:** Mar 31, 21:50 UTC (Metric value: 0.0).
*   **Monitor ID:** `91573506`.

**Resolved Incidents**
*   **`marketing-service`:** P2 high error rate triggered at 17:28 UTC (Metric: 4.5%) and resolved automatically at 17:38 UTC.
    *   *Query:* Error rate > 5% over 10m. Monitor ID `17447106`.
*   **`go-catalogue-service` (Latency):** P3 latency on `get_/product` triggered at 19:35 UTC (P90: 163ms) and resolved at 19:56 UTC.
    *   *Query:* P90 > 150ms over 15m. Monitor ID `17447976`.
*   **`go-catalogue-service` (Latency):** P3 latency on `get_/category/_id` recovered at 14:33 UTC after earlier spikes. Metric value normalized to 0.746s.
    *   *Query:* P90 > 2.0s over 20m. Monitor ID `17447967`.

**Pending Actions & Ownership**
*   **Action:** **MONITORING ONLY (`fp-search-indexer`):** [Status: ACTIVE/UNRESOLVED] Investigate P2 errors on `env:prod` (Triggered 07:29 UTC). No new status update in latest logs.
    *   **Owner:** Product Data Management (`team:dpd-staff-excellence-pdm`).
*   **Action:** **POST-INCIDENT REVIEW (`sap-job-file-plu-subscription`):** [Status: CLOSED] P2 PubSub backlog resolved without manual intervention mentioned in recovery log. Verify if root cause analysis is needed for the 1h+ delay.
    *   **Owner:** Product Data Management / Discovery Team.

**Decisions Made**
*   The `marketing-service` error rate spike was transient and self-resolving within 10 minutes.
*   The `sap-job-file-plu-subscription` backlog impacted pricing data integrity but recovered automatically at 21:50 UTC; no manual restart was required based on the recovery log.
*   Previous alerts for `sku-store-attribute`, `sku-global-attribute`, and earlier `go-catalogue-service` latency events remain closed with no further action required.

**Key Dates & Follow-ups (Mar 31, 2026)**
*   **Service: `sap-job-file-plu-subscription` (P2 - Product Data Management) [RESOLVED]**
    *   *Latest Timeline:* Triggered 20:35 UTC; Recovered 21:50 UTC.
    *   *Details:* Oldest unacked message age exceeded 1.5 hours (5474s). Impact: Pricing data in DBP.
    *   *Links:* [Datadog](https://app.datadoghq.eu/monitors/91573506) | [PubSub](https://console.cloud.google.com/cloudpubsub/subscription/detail/sap-job-file-plu-subscription?project=fponprd) | [Runbook](https://ntuc.atlassian.net/wiki/spaces/SR/pages/2571632656/Restarting+service+via+deployment)
*   **Service: `go-catalogue-service` (P3 - Product Data Management) [RECOVERED]**
    *   *Latest Timeline:* P90 latency on `get_/product` resolved at 19:56 UTC.
    *   *Links:* [Datadog](https://app.datadoghq.eu/monitors/17447976) | [Runbook](https://ntuc.atlassian.net/wiki/spaces/DIS/pages/2646212686/Catalogue+Service)

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c


## [3/57] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-03-31T20:10:13.859000+00:00 | Last Updated: 2026-03-31T22:35:24.154886+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Update)**
**Date:** March 31, 2026 (Late Shift)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 804

### Key Participants & Roles
*   **System/Tool:** Datadog App (Automated Monitoring)
*   **Notification Channel:** `@hangouts-ShoppingCartNotification`
*   **Ownership Teams:** `dpd-pricing`, `dpd-pricing-cart`.

### Main Topic
Instability persists in `frontend-gateway` and `st-cart-prod`. While the critical latency spike on Wish List endpoints (`put /api/product/{_id}/wish-list`) recovers by 18:25 UTC, volatility has shifted to **Checkout** success rates and **Cart Update** availability. New incidents show recurring oscillation between triggered alerts and recoveries throughout the late afternoon and evening (17:55–20:10 UTC).

### Incident Timeline & Actions
**Previous Context:**
*   *Extended activity from March 20 through 14:30 UTC.*
*   *March 30, 21:57 UTC:* P2 Error Budget Alert triggered (94.9% consumed).

**New Activity (Late Afternoon – Evening March 31 UTC)**
*   **17:55–18:14 UTC:** Severe Checkout latency spike followed by recovery.
    *   `post /api/checkout`: P99 reached **20.242s** (threshold >3.0s). Recovered to 1.775s by 18:14 UTC.
*   **17:59–18:17 UTC:** Fluctuating availability on List operations.
    *   `get /api/v2/shopping-list`: Success rate dropped to **98.824%** (threshold <99.9%). Recovered by 18:09 UTC.
    *   `get /api/wish-list`: Success rate dropped to **99.864%**. Recovered by 18:17 UTC.
*   **18:07–18:25 UTC:** Cart Update volatility.
    *   `post /api/cart`: Success rate dipped to **99.783%** (threshold <99.9%). Recovered by 18:18 UTC.
*   **18:58–19:08 UTC:** Checkout success rate breach.
    *   `post /api/checkout`: Success rate fell to **99.722%**. Recovered by 19:08 UTC.
*   **20:00–20:10 UTC:** Latest Checkout success rate breach.
    *   `post /api/checkout`: Success rate dropped to **99.543%**. Recovered by 20:10 UTC.

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** Incident window extended through at least 20:10 UTC. The pattern has shifted from latency-dominant (Wish List) to success-rate dominant (Checkout/Cart).
*   **Immediate Action Required:** Investigate the correlation between the 17:55 UTC Checkout P99 spike (20.242s) and subsequent success rate dips (lowest 99.543% at 20:00 UTC). Review `frontend-gateway` resource utilization during these recurring 10-minute windows to rule out transient throttling or dependency failures.

### Decisions Made
*   **Priority Escalation:** Status remains **"Critical Incident"**. The system shows a distinct shift from latency anomalies to availability dips, with multiple new triggers occurring in the last hour alone.
*   **Focus Shift:** Analysis must prioritize `post /api/checkout` and `get /api/v2/shopping-list` monitors given their recurrence post-17:55 UTC. The previous 14:18 UTC Wish List spike is no longer the active trigger but remains part of the systemic instability profile.
*   **Metric Update:** Latest recorded Checkout P99 peak was **20.242s**. Lowest recorded success rate was **99.543%** (Checkout).

### Key Dates & Follow-ups
*   **Critical Window:** Extended activity from March 20 through at least March 31, 20:10 UTC.
*   **Follow-up:** Immediate trace correlation for the 17:55–20:10 UTC window to identify if `frontend-gateway` is consistently failing under load for Checkout and List endpoints.

### References
*   **Active Monitors:** `21245705` (Checkout P99), `21245735` (Shopping List Success Rate), `21245714` (Cart Update Success Rate), `21245708` (Checkout Success Rate).
*   **SLO Monitor:** `8567154411503835973` (Error Budget Alert).
*   **Service Tags:** `service:frontend-gateway`, `team:dpd-pricing`.


## [4/57] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Messages: 23 | Last Activity: 2026-03-31T17:45:04.488000+00:00 | Last Updated: 2026-03-31T22:36:02.594630+00:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
Production instability in the Mirakl and DBP integrations continues. A significant new incident cluster occurred on **March 31** between **17:39 UTC** and **17:45 UTC**, affecting `fni-order-create` with multiple P2 alerts related to database fetching and API errors. Concurrently, a separate test monitor triggered intermittently for Apple Pay transactions earlier in the afternoon. The `picklist-pregenerator` latency issue remains unresolved.

**Incident Summary & Timeline**
*   **Service: `fni-order-create` (Cluster of Errors) – Late Afternoon (Mar 31)**
    *   **Trigger Window:** A cluster of P2 alerts began at **17:39:46 UTC**:
        *   "Failure occurred during fetching orders from DBP" (`17447925`) triggered at **17:39:46 UTC**.
        *   "Error while calling APIs" (`17447928`) triggered at **17:39:49 UTC**.
        *   "Failure occurred during fetching orders" (`17447942`) triggered at **17:40:03 UTC**.
        *   "Exception Occurred At DBP Route" (`17447943`) triggered at **17:40:04 UTC**.
    *   **Recovery:** All four monitors returned to normal between **17:44:47 UTC** and **17:45:04 UTC**. Total duration: ~6 minutes.

*   **Service: Test Monitor (Apple Pay) – Mid-Afternoon (Mar 31)**
    *   **Trigger:** Monitor `29851723` (`formula("a / b").last("1h") > 0.5`) for group `@request.payment_method:APPLE_PAY` triggered at **16:41:45 UTC** and again at **16:51:45 UTC**.
    *   **Recovery:** Alerts cleared at **16:46:45 UTC** and **17:12:44 UTC**.

*   **Service: `picklist-pregenerator` (Latency Warning) – Late Evening (Mar 29 & Mar 30)**
    *   **Trigger:** P2 Warning "taking too long to complete." Triggered at 19:01 UTC on Mar 29 (**3609.523s**) and 23:01:23 UTC on Mar 30 (**3608.92s**).

*   **Service: `fpon-seller-sap-picklist-reporter` (P1 Incident) – Evening (Mar 27)**
    *   **Trigger:** P1 alert "SAP authentication failed" at 19:12:15 UTC. Recovered by 19:17:15 UTC.

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of the March 31 cluster affecting `fni-order-create` (Monitors `17447925`, `17447928`, `17447942`, `17447943`). Specifically analyze DBP fetching failures and API errors.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Investigate intermittent triggers for Monitor `29851723` regarding Apple Pay transaction ratios (`a/b > 0.5`).
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Address critical latency in `picklist-pregenerator`. Recurrence of >3,600s execution times indicates continuous systemic failure.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Analyze underlying causes for the P1 SAP authentication failure on `fpon-seller-sap-picklist-reporter` (Mar 27) to prevent recurrence.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Summary for Leadership**
Instability in the Mirakl and DBP integrations persists with a new activity cluster on **March 31**. Between **17:39:46 UTC** and **17:45:04 UTC**, `fni-order-create` triggered four distinct P2 alerts, including "Failure occurred during fetching orders from DBP" (`Monitor ID 17447925`) and "Exception Occurred At DBP Route" (`Monitor ID 17447943`). All issues resolved within approximately 6 minutes. Additionally, a test monitor for Apple Pay transactions triggered intermittently between **16:41 UTC** and **17:12 UTC**. Concurrently, the `picklist-pregenerator` service continues to exhibit critical latency, with execution times exceeding 3,600s logged on March 29 and 30. This indicates persistent systemic degradation across the `dpd-fulfilment` and `seller-experience` squads requiring urgent engineering review.


## [5/57] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/69o051rSqd4 | Messages: 12 | Last Activity: 2026-03-31T16:01:07.785000+00:00 | Last Updated: 2026-03-31T22:36:30.838076+00:00
**Daily Work Briefing: Digital Product Development (Leads Ecom/Omni)**

**Key Participants & Roles**
*   **Daryl Ng:** Initiator; previously tracking deployment status.
*   **Sneha Parab:** Technical lead/owner; confirmed completion of MP production deployment.
*   **Shiva:** Tester; concluded validation late yesterday evening (March 30).
*   **Alvin Choo:** Team member; coordinated BCRS focus and verified final status.

**Main Topic**
Discussion focused on the finalization of the BCRS deliverable, MP production deployment confirmation, and a subsequent query regarding flag configuration timing.

**Pending Actions & Ownership**
*   **Deploy Feature (MP):** **COMPLETED.** Sneha Parab deployed pending changes for MP to production as of 10:51 AM on March 31.
    *   **Owner:** Sneha Parab.
*   **BCRS Deliverable:** **CONFIRMED COMPLETE.** Alvin Choo verified the status at 10:49 AM, confirming "all okay," and subsequently celebrated the completion with the team.
*   **Feature Flags Configuration:** **PENDING/UNDETERMINED.** At 16:01 PM on March 31, Daryl Ng raised a question regarding whether flags were scheduled for enabling. No confirmation of scheduling or status was recorded in this update.
    *   **Owner:** To be determined (Query initiated by Daryl Ng).

**Decisions Made**
*   **Deployment Timing:** The deployment of MP changes to production was executed on March 31, 2026, following Shiva's successful testing (concluded March 30 evening).
*   **Daily Focus Priority:** The team successfully prioritized and completed all BCRS tasks by the end of the day.
*   **Flag Configuration Status:** No decision recorded; status remains pending verification as of 16:01 PM.

**Status Updates & Key Dates**
*   **Current Date:** March 31, 2026.
*   **BCRS Status:** Final deliverable confirmed ready and complete as of 10:49 AM. Alvin Choo expressed congratulations to the team at 11:02 AM.
*   **MP Deployment:** Successfully pushed to production by Sneha Parab at 10:51 AM.
*   **Critical Deadline:** Met; today (March 31) was the final day for BCRS deliverables and deployment activities.
*   **New Inquiry:** At 16:01 PM, Daryl Ng queried the scheduling status of feature flags to be enabled following the deployment.

**Reference Links**
*   Deployment Verification Link: `https://chat.google.com/room/AAQAX9iKYf0/CjKvfZ07Lb4/kIo2WYTccYY?cls=10`


## [6/57] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Messages: 6 | Last Activity: 2026-03-31T15:05:23.074000+00:00 | Last Updated: 2026-03-31T22:37:14.901332+00:00
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
2.  **Mar 18/19:** `10aaf170-dac2-5fec-97bf-cfd442f8706b`. (~5.6h). Status: **Resolved**.
3.  **Mar 20, 2026:** `2787bcd7-d59e-58f0-961a-8f578260cd84`. (~4.4h). Status: **Resolved**.
4.  **Mar 22, 2026:** `08f5624a-14f1-50e5-9a4a-7418b3602953`. (~3.4h). Status: **Resolved**.
5.  **Mar 24–25, 2026:** `de0cbb14-ade3-5de2-bfab-cbddd41da779`. (~3h 51m). Status: **Resolved**.
6.  **Mar 25, 2026:** `978f6328-424c-53dd-83c8-6411c3aa2158`. Recovered 12:09 UTC (~24h). Status: **Resolved**.
7.  **Mar 26, 2026:** `7b73b037-696a-5016-bca4-5c22e31b6245`. (~3h 22m). Status: **Resolved**.
8.  **Mar 27, 2026:** `f5d0894a-4a42-515d-985f-d06644833529`. Recovered 17:37 UTC. Status: **Resolved**.
9.  **Mar 28–30, 2026:** Multiple P3 incidents recovered (Keys: `8874d9ed...`, `784f6ec6...`, `acd815df...`).

**Recent Sequence Update:**
*   **Mar 31, 2026 (Trigger):** At 11:49:22 UTC, a new P3 incident triggered.
    *   **Story Key:** `0404fba2-a49b-51a3-a07f-1c4bb6b19362`.
    *   **Error Message:** "Datadog is unable to process your request."
*   **Mar 31, 2026 (Resolution):** At **15:05:23 UTC**, the incident `0404fba2-a49b-51a3-a07f-1c4bb6b19362` transitioned to **[P3] Recovered**.
    *   **Duration:** ~3 hours 16 minutes.
    *   **Status:** **Resolved**.

*Note: The previously triggered incident on Mar 31 has now self-resolved.*

### Pending Actions & Ownership
*   **Current Status:** Incident `0404fba2-a49b-51a3-a07f-1c4bb6b19362` is **Resolved** (Recovered at 15:05 UTC).
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Action Required:** None. Incident duration remained below the 6-hour escalation threshold. Continue standard surveillance for new triggers.

### Decisions Made
*   **Escalation Status:** No escalation required; incident resolved within expected window.
*   **Protocol:** Standard observation protocol confirmed effective for this sequence.

### Key Dates & Follow-ups
*   **Latest Event:** March 31, 2026 (Triggered 11:49 UTC → Recovered 15:05 UTC).
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Surveillance ongoing.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Datadog Monitor Link:** [View in Datadog](https://app.datadoghq.eu/monitors/17447511)
*   **Resolution Event Log:** https://app.datadoghq.eu/monitors/17447511?group=story_key%3A0404fba2-a49b-51a3-a07f-1c4bb6b19362

### Monitor Configuration
*   **Query:** `events("source:watchdog (story_category:infrastructure -story_type:(tcp_retrans_jump OR full_disk_forecast)) env:(PROD OR production OR prod)").rollup("count").by("story_key").last("30m") > 0`


## [7/57] BCRS ECOMM SAP POSTING
Source: gchat | Group: space/AAQA-ICuJRM | Last Activity: 2026-03-31T13:40:38.299000+00:00 | Last Updated: 2026-03-31T14:40:04.424440+00:00
**Daily Work Briefing: BCRS ECOMM SAP POSTING & Refunds UAT (Mar 31 Update)**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** UAT lead; coordinating validation.
*   **Tan Gay Lee:** Stakeholder rejecting sign-off due to GL entry errors in pre-order/S&G refunds.
*   **Lai Shu Hui:** Accounting participant; pending final test case closure for e-commerce returns.
*   **Sathya Murthy Karthik:** Confirmed 2 untested e-commerce cases remain; advocating for immediate sign-off.
*   **De Wei Tey:** Investigating production deployment status and requesting environment access.
*   **Onkar Bamane:** Confirmed "existing logic" handles B2C/B2B credit note variations.
*   **Wei Fen Ching:** Questioned discrepancies between B2C and B2B credit note designs.
*   **Yaxin Hao / Jianbin Huang:** Technical owners asked to check Store 420 UAT sales data.

**Main Topic**
UAT progress remains stalled due to GL entry discrepancies in Pre-order and Scan 'n Go (S&G) refunds, preventing final sign-off. Concurrently, De Wei Tey has raised deployment queries regarding the new BCRS CN API and requested critical access for testing environments. A separate query persists regarding visual discrepancies between B2C and B2B credit notes, confirmed by Onkar Bamane as resulting from existing system logic.

**Status of Issues & Updates**
*   **Sign-off Scope Adjustment:** Following alignment on Mar 26, S&G deposit refunds are excluded from "Returns & Refunds." A separate sign-off is now requested for E-Comm (API for Deposit Accounting, Marketplace SKU creation, Concess Sales Detail/Summary Reports).
*   **GL Entry Discrepancy:** Tan Gay Lee rejected the sign-off noting pre-order refunds fail to capture correct GL accounts. Pre-orders cancelled within 5 days follow 'Cancellation after delivery' via CS; POS-paid pre-order refunds occur at POS with cash.
*   **Credit Note Logic:** Wei Fen Ching queried why B2C credit notes differ from B2B designs. Onkar Bamane clarified this is due to existing logic, confirming two distinct RPA credit note designs (one for B2B, one for B2C).
*   **Environment Access & Deployment:** De Wei Tey raised a ticket on Mar 31 at 13:40 UTC to grant access to `FP_ROBOT_PER` in the PER environment. Additionally, De Wei Tey queried at 11:20 UTC whether the new BCRS CN API has been deployed to production.
*   **Testing Status:** Sathya Murthy Karthik highlighted two untested e-commerce cases pending validation. Prajney requested clarification from Tan regarding the GL issue, citing previous alignment that E-Comm test cases were otherwise fine.

**Pending Actions & Ownership**
1.  **Environment Access Grant:** Hendry Tionardi to grant `FP_ROBOT_PER` access in PER environment immediately as per De Wei Tey's ticket (Reply time: 5 mins ago). **(Owner: Hendry Tionardi)**.
2.  **Deployment Verification:** Confirm status of new BCRS CN API deployment to production. **(Owner: De Wei Tey / Technical Team)**.
3.  **GL Resolution:** Emergency call scheduled to resolve incorrect GL capture for pre-order refunds. **(Owner: Prajney Sribhashyam, Sathya Murthy Karthik)**.
4.  **Test Case Closure:** Lai Shu Hui must validate the remaining two untested e-commerce cases immediately. **(Owner: Lai Shu Hui)**.
5.  **Data Verification:** Check for unprocessed sales in Store 420 UAT. **(Owner: Yaxin Hao, Jianbin Huang)**.
6.  **Sign-off Execution:** Tan Gay Lee and Lai Shu Hui to provide separate E-Comm sign-off post-resolution. **(Owner: Tan Gay Lee, Lai Shu Hui)**.

**Decisions Made**
*   S&G deposit refund posting scope is excluded from the current "Returns & Refunds" sign-off; a distinct E-Comm sign-off is required.
*   RPA separate posting for deposit refunds is inadvisable; SAP recommends using Data 8 aggregation (aligned with sales/BCRS deposit methods).
*   Distinct RPA credit note designs exist for B2B and B2C, driven by pre-existing system logic.
*   Current UAT cannot proceed to final deployment until GL capture issues are addressed, pending test cases validated, and environment access/deployment queries resolved.

**Key Dates & Follow-ups**
*   **Mar 31, 13:40 UTC:** De Wei Tey raised a ticket for `FP_ROBOT_PER` access in PER; awaiting Hendry Tionardi's response.
*   **Mar 31, 11:20 UTC:** De Wei Tey queried BCRS CN API production deployment status.
*   **Mar 31:** Wei Fen Ching queried credit note discrepancies; Onkar Bamane confirmed existing logic with dual RPA designs for B2B/B2C.
*   **Mar 26, 07:54 AM:** Emergency Google Meet scheduled to resolve the sign-off blocker.

**Immediate Follow-up:** Attend the emergency video meeting to clarify GL handling for pre-order refunds, ensure Hendry Tionardi grants environment access ASAP, verify CN API deployment status, and confirm Lai Shu Hui completes the two outstanding e-commerce test cases urgently.


## [8/57] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY | Last Activity: 2026-03-31T13:10:28.838000+00:00 | Last Updated: 2026-03-31T14:41:43.048934+00:00
**Updated Briefing: BCRS Firefighting Group**
**Date:** March 31, 2026 (Latest activity: ~08:46 AM / New update @ 1:10 PM)
**Source:** Google Chat Space & Shared UAT Tracker (94 messages total)

### **Key Participants & Roles**
*   **Prajney Sribhashyam:** Project Lead/Test Coordinator.
*   **De Wei Tey / Michael Bui / Wai Ching Chan:** Finance/SAP, Re-delivery specialists, and Technical Integration.
*   **Dany Jacob / Eswarlal Rajesh / Sneha Parab:** Active test participants and finance coordinators.
*   **Alvin Choo:** Status reporting lead (monitoring Starship channel updates).
*   **Akash Gupta:** Mentioned stakeholder regarding Quick Buy deployment.
*   **New/Active Stakeholders:** Shiva Kumar Yalagunda Bas, Chee Hoe Leong, Tiong Siong Tee, Daryl Ng, Koklin Gan, Hang Chawin Tan.

### **Main Topics**
1.  **Quick Buy Deployment Confirmation (March 31, ~01:06 PM):** Prajney queried the production timeline for Quick Buy changes previously tested by GovTech. Wai Ching Chan confirmed deployment occurred "yesterday" (March 30). A brief exchange clarified that Prajney was already included in the notification loop; no further action required on this item.
2.  **Critical Feature Sign-Offs Confirmed (March 30):** Prajney confirmed sign-off for refunds across E-Comm and Scan & Go channels, completing critical features for the April 1 launch. Updated were CC'd to Koklin Gan.
3.  **RPA Production Verification Request (March 31, ~05:30 AM):** Prajney queried if RPA was in production. The message generated 10 replies and was viewed by 26 of 40 members, quoting De Wei Tey, Dany Jacob, Tiong Siong Tee, and Daryl Ng.
4.  **Legacy App Invoice Logic Query (March 31, ~06:55 AM):** Prajney raised a critical question regarding invoice reflection for customers on older app versions purchasing BCRS items, specifically asking if the invoice will reflect the BCRS deposit. This generated 10 replies and was viewed by 29 of 42 members.
    *   **Last Reply:** @Tiong Siong Tee and @Hang Chawin Tan (8:46 AM).
5.  **Linkage Investigation:** Shiva Kumar Yalagunda Bas flagged missing linkages on March 30 (~09:20 AM), requiring immediate investigation by Chee Hoe Leong.

### **Decisions & Updates**
*   **Quick Buy Status:** Resolved. Wai Ching Chan confirmed the GovTech Quick Buy integration was deployed to production on March 30; inclusion in communication loops is verified.
*   **Launch Readiness:** Refund sign-off solidifies readiness for the April 1 deadline. However, the legacy app invoice logic query introduces a potential risk regarding deposit reflection that requires resolution before launch.
*   **RPA Status Inquiry:** Focus remains on verifying live RPA execution in production immediately following sign-offs.

### **Pending Actions & Owners**
| Action Item | Owner(s) | Status/Context |
| :--- | :--- | :--- |
| **Clarify Legacy App Invoice Logic** | Tiong Siong Tee / Hang Chawin Tan | **Urgent:** Prajney queried invoice behavior for older app versions (06:55 AM); thread active with 10 replies. |
| **Verify RPA Production Status** | De Wei Tey / Team | **High Priority:** Prajney questioned production status at ~05:30 AM; requires immediate confirmation via existing thread. |
| **Resolve Missing Linkages** | Shiva Kumar Yalagunda Bas / Chee Hoe Leong | **Active:** Investigating linkage failures raised March 30; viewed by 18 of 39 members. |
| **Overall Status Update** | Prajney Sribhashyam / Team | **Pending:** Provide update to Alvin Choo regarding Starship channel changes, April 1 readiness, and current linkage/invoice issues. |

### **Key Dates & Deadlines**
*   **April 1:** Critical launch deadline; all critical features (including Refunds) signed off as of March 30.
*   **March 31 (Today):** Date of active RPA production verification request, legacy app invoice logic query, and Quick Buy deployment confirmation.
*   **March 30:** Date of refund sign-off, linkage issue flagging, and Quick Buy deployment to production.

### **Historical Context Retained**
*   Original SAP Deposit API development deadline of Feb 20 remains noted as missed/risked; current effort focuses on resolving specific re-delivery logic gaps via live testing.
*   Existing e-comm test accounts remain unusable for Pre-order staff app; new BCRS CF items and specific GWP SKUs are required.
*   Deposit SKU linking investigation continues due to failure to link post-publishing (now explicitly flagged by Shiva Kumar Yalagunda Bas).
*   Previous Re-delivery flow testing experienced audio issues on March 16; current Production effort aims to resolve logic gaps via grooming and live validation.


## [9/57] [Prod Support] Ecom FFS Ops
Source: gchat | Group: space/AAAAde_cYKA | Last Activity: 2026-03-31T12:25:23.666000+00:00 | Last Updated: 2026-03-31T14:48:18.462568+00:00
**Daily Work Briefing: [Prod Support] Ecom FFS Ops (Updated Mar 31)**

**Key Participants & Roles**
*   **Wai Ching Chan / Sampada Shukla:** Operations/Product Leads.
*   **TL HCBP FFS / TL - HGPT FFS:** Store Leads reporting picking queue blockages and SOH anomalies.
*   **Adrian Yap Chye Soon:** Technical Lead/Support (investigating data anomalies and dispatcher app failures).
*   **Akash Gupta:** DPD / Fulfilment / On Call.
*   **Yoongyoong Tan:** Reporting HCBP picking Q issues.
*   **Ler Whye Ling Angel:** Escalation point for "No picking Q."

**Main Topics**
1.  **Packlist & SOH Discrepancies (Expanded):** Ongoing investigation into critical `packed_qty` anomalies and Stock on Hand (SOH) NULL values across multiple sites.
    *   **New Critical Incident (Mar 31, ~12:25 PM):** TL - HGPT FFS reported bulk order issues at **HGPT** where SOH indicated **NULL**.
    *   **Ongoing Critical Incidents:**
        *   **Hyper Changi (Store ID 45) - Mar 29:** Order #22972590 showed `packed_qty` of 90,203,969 vs. `delivered_qty` of 2 ($19.95 MRP/$39.9).
        *   **VivoCity - Mar 26:** Orders #22912255/#22906879 with ~13M discrepancy.

2.  **Dispatcher App & Zone Scanning Failure (Mar 28):** Escalation regarding the dispatcher app's inability to scan new zones at **hvivo**.
    *   **Status:** Reported 01:45 AM Mar 28; Adrian Yap Chye Soon provided video evidence for review; technical investigation remains active.

3.  **HCBP Picking Queue Issues (Mar 27):** Escalated urgency regarding "No picking Q" blockage and T18 display failures.
    *   **Status:** Initial blockage reported 02:08 AM; escalated by Ler Whye Ling Angel at 02:52 AM; T18 data failure reported by TL HCBP FFS at 07:47 AM.

**Pending Actions & Ownership**
*   **Data Validation (Urgent - Mar 31):**
    *   *@Akash Gupta / On Call:* Immediate validation of SOH NULL values for bulk orders at **HGPT**.
    *   *@Wai Ching Chan @Sampada Shukla:* Prioritize review of the new HGPT anomaly alongside pending validations for Hyper Changi (Order #22972590), Sun Plaza, and VivoCity.
*   **Dispatcher App Investigation:**
    *   *@Adrian Yap Chye Soon / Technical Team:* Continue RCA on "unable to scan new zone" failure at hvivo based on video evidence.
*   **HCBP Queue Investigation:**
    *   *@Adrian Yap Chye Soon / @Gopalakrishna Dhulipati:* Monitor resolution of Mar 27 "No picking Q" and T18 display failures following escalations by Ler Whye Ling Angel.

**Decisions Made**
*   **App Release Strategy:** Picker App 10.4.0 rollout remains on hold pending resolution of critical data anomalies (Mar 18–31). Full rollout is contingent on stability post-fixes, specifically addressing:
    *   The newly discovered Mar 31 HGPT SOH NULL issue.
    *   The Mar 29 Hyper Changi anomaly (Order #22972590).
    *   The resolved/pending Mar 26 VivoCity alerts.
    *   The resolved/pending Mar 27 HCBP queue/T18 failures.
    *   The new dispatcher app zone scanning issue at hvivo.

**Key Dates & Deadlines**
*   **Immediate:** Validation of Mar 31 HGPT SOH NULLs and RCA for Mar 28 Dispatcher App failure at hvivo. Also urgent validation of Mar 29 Order #22972590.
*   **Pending:** Comprehensive RCA for recent anomalies across Sports Hub, VivoCity, Parkway, Changi, Sun Plaza, Hyper VivoCity, Hyper Changi, and the new HGPT site.

**Critical Alerts**
*   **Active Alert (Mar 31):** Bulk order SOH indicated **NULL** at **HGPT**. Requires immediate data validation by Ops.
*   **Active Alert (Mar 30/29):** Packlist quantity (`90M`) significantly exceeds delivered quantity at **Hyper Changi (Store ID 45)**.
*   **Secondary Active Alert (Mar 28):** Dispatcher app unable to scan new zone at **hvivo**. Video evidence available; requires technical check.
*   **Tertiary Active Alert (Mar 27):** HCBP "No picking Q" issue escalated by Ler Whye Ling Angel.


## [10/57] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/pA7_pZifIOE | Last Activity: 2026-03-31T09:45:55.026000+00:00 | Last Updated: 2026-03-31T10:40:35.111982+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Project Lead/Coordinator (orchestrating sign-offs and testing).
*   **De Wei Tey:** Technical Owner/RPA Lead (managing deployments, testing RPA logic, and production pushes).
*   **David Anura Cooray:** QA/Testing Lead (validating iOS/Android refund flows).
*   **Joey Ang Hui Xin:** Operations/Front-end Tester (executing live order placement and refund requests).
*   **Hendry Tionardi & Onkar Bamane:** Finance/System Integration (monitoring SAP postings and managing financial reversals).
*   **Dany Jacob, Koklin Gan, Yatlian Wee:** Stakeholders providing sign-offs or context.

**Main Topic**
Validation and production deployment of the RPA refund feature for **BCRS (Scan & Go)** ahead of the **1 April** critical deadline. The discussion focused on confirming sign-offs, testing specific SKUs on both iOS and Android, handling live environment data, and managing financial reversals for test transactions.

**Decisions Made**
1.  **Scope Adjustment:** Confirmed that **Scan & Go (S&G)** is already rolled out; focus shifted to verifying the RPA refund logic specifically for SNG/BCRS SKUs rather than OG (Original Game) first.
2.  **RPA Behavior Alignment:** Agreed that RPA will **not** perform BCRS posting for SNG. Consequently, De Wei Tey paused "auto-refund" temporarily to manually push BCRS refunds. This impacts refunds only, with no effect on First Response or other CS automated processes.
3.  **Testing Strategy:** Proceeded with live environment testing using real users (Joey Ang) and specific SKUs.

**Pending Actions & Ownership**
*   **Finance Reversal of Test Refund:** Finance must revert the test refund transaction generated during live testing.
    *   *Order ID:* `259017167` (iOS), `259018320` (Android), and `259022496` (Live Live Test).
    *   *Owner:* **Onkar Bamane** to inform Finance; **De Wei Tey** confirmed the RPA will refund these orders.
*   **SAP Monitoring:** Continued monitoring of SAP postings for test transactions.
    *   *Owner:* **Hendry Tionardi**.

**Key Dates & Deadlines**
*   **Critical Deadline:** **1 April 2026** (All sign-offs for critical features were required by this date; confirmed completed).
*   **Testing Execution Date:** **31 March 2026** (Live testing conducted between 06:26 and 07:32 UTC+8 equivalent timeframes).

**Specific References**
*   **Google Meet Link:** `https://meet.google.com/drg-exsc-rkj` (Production testing call).
*   **Impact Scope:** Only refunds are impacted by the temporary pause; CS automated processes remain unaffected.
*   **Environment:** Testing confirmed in the Live Environment at 07:19 UTC+8 equivalent.


## [11/57] RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU | Last Activity: 2026-03-31T09:41:14.829000+00:00 | Last Updated: 2026-03-31T10:41:12.435106+00:00
**Daily Briefing Summary: RMN Leadership Space (Updated Mar 31)**

**Key Participants & Roles**
*   **Bryan Choong:** Returned from eTail Asia; at Thomson Plaza. Prioritizing Q1 case studies, low-sodium project, and sampling solutions. Observed booth congestion. Preparing briefing points for Vipul's lunch with SPH CEO next week. Addressing digital screen slot requests.
*   **Vipul:** Meeting SPH CEO for lunch next week to discuss revenue, agreements, and strategic propositions.
*   **Pauline Tan:** Managing LinkedIn content/award repurposing; investigating sampling spend. Now leading "Product Launch Solution" inquiry (3 replies pending).
*   **Rajiv Kumar Singh:** Coordinating SOAC planning; shared DoorDash Ads benchmarks. Tasked with SPH radio insights and survey execution. Currently evaluating BCRS campaign digital screen placement options.
*   **Allen Umali:** Leading SignCloud cleanup; on MC. Requesting allocation for BCRS campaign on Digital Screens starting tomorrow (Apr 1).
*   **Serene Tan Si Lin & Raymond Kam:** Sourcing THPZ Australia Fair intelligence and coordinating SPH news broadcast surveys, respectively.
*   **Emerald:** Developing playbook for campaign assets in the app.

**Main Topics**
1.  **SPH Strategic Discussion (Next Week):** Bryan Choong is preparing briefing points for Vipul's upcoming lunch to address revenue performance, agreement timelines, and potential joint business plans.
2.  **In-Screen Reselling & Radio:** Focus on determining 2024/2025 revenue and 2026 YTD figures. Key discussion points include a previously declined offer, the official end date of the current reseller agreement (post-notice), and readiness to respond to potential Mediacorp-style propositions.
3.  **BCRS Campaign Activation:** A new campaign is scheduled from Apr 1 through Sep 30, 2026. Allen Umali requested a dedicated slot on Digital Screens starting tomorrow. Rajiv Kumar Singh has queried whether the campaign should utilize a *dedicated* slot or an *internal* slot to accommodate the launch "full swing."
4.  **SPH News Broadcast & Survey:** Raymond Kam to coordinate a joint customer survey with SPH regarding in-store news content.
5.  **Product Launch Solution:** Pauline Tan is actively managing a thread regarding product launch solutions with three replies received.

**Pending Actions & Owners**
*   **BCRS Campaign Slot Allocation:** Decide if the BCRS campaign (Apr 1–Sep 30) requires a dedicated Digital Screen slot or utilizes an internal slot based on capacity and impact. *Owner: Rajiv Kumar Singh, Bryan Choong.*
*   **SPH Revenue & Data Gathering:** Compile 2024/2025 revenue and 2026 YTD figures for both In-Screen Reselling and Radio. *Owner: Team (Bryan, Rajiv, Raymond).*
*   **Agreement Terms Analysis:** Identify the specific offer declined by SPH in reselling and confirm the official end date of the current agreement. *Owner: Bryan Choong.*
*   **Radio Strategy & Survey:** Verify if a joint business plan was submitted; confirm October agreement expiry; draft response for news broadcast updates; initiate customer survey planning with SPH. *Owner: Rajiv Kumar Singh, Raymond Kam.*
*   **Strategic Positioning:** Prepare a viewpoint for Vipul to counter potential Mediacorp-style propositions and outline any specific asks. *Owner: Bryan Choong.*
*   **Sampling Solution Investigation:** Obtain quotes from Grenadier and other agencies; analyze spend/traffic impact at THPZ. *Owners: Serene Tan Si Lin, Pauline Tan.*
*   **Product Launch Inquiry:** Resolve pending replies regarding product launch solutions. *Owner: Pauline Tan.*
*   **SignCloud Cleanup:** Complete manual removal of legacy screens (Urgent due to MC). *Status: Contact Allen via WhatsApp.*

**Decisions Made**
*   **SPH Engagement:** Proceed with Vipul's meeting; prepare data-driven responses for reselling and radio revenue discussions.
*   **Survey Execution:** Formalize plan to conduct customer survey on news broadcasts in collaboration with SPH.
*   **Sampling Strategy:** Accelerate solution development; verify Grenadier quotes and explore alternatives for THPZ model.

**Key Dates & Deadlines**
*   **Next Week (Apr):** Vipul lunch with SPH CEO.
*   **Apr 1 – Sep 30, 2026:** BCRS Campaign duration (launching tomorrow).
*   **Oct 2026:** Estimated end date for current In-Screen Radio agreement.
*   **Mar 31:** New briefing request generated; data compilation initiated.
*   **End of March:** Deadline to finalize SOAC targets.
*   **July:** Planned USA fair activation.


## [12/57] [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Last Activity: 2026-03-31T09:38:01.645000+00:00 | Last Updated: 2026-03-31T10:42:49.994417+00:00
**Daily Work Briefing: [Prod Support] Marketplace**

**Key Participants & Roles**
*   **Support/Operations:** Willie Tan, Iris Chang, Lalita Phichagonakasit, Charlene Tan, Jie Yi Tan, Ayton See, Amos Lam, Michelle Lim.
*   **Technical/Admin Team:** Dang Hung Cuong, Shiva Kumar Yalagunda Bas, Olivia -, Jill Ong, Greta Lee, Zaw Myo Htet, Angella Yeo, Cassandra Thoi, Gopalakrishna Dhulipati, Ee Ling Tan.
*   **New Reporter:** Muhammad Sufi Hakim Bin Safarudin.

**Main Topics & Discussion Summary**
Discussions continue to focus on operational blockers regarding seller onboarding, order fulfillment discrepancies, system configuration errors, and data visibility gaps. New reports from March 31 highlight sync failures, email distribution logic, and live site publishing issues. Major themes include:
1.  **Seller Account Sync Failure (New):** Michelle Lim reported (Mar 31, 07:48 UTC) that two new seller accounts failed to sync to DBP despite having allocated internal codes and no error messages.
    *   Operator Internal Codes: 32208, 32207.
2.  **Email Distribution Logic (New):** Iris Chang requested confirmation regarding Sales Breakdown Report delivery for DF vendors. The goal is to ensure `db-online-marketplace@ntucenterprise.sg` is automatically CC'd regardless of the "Report Emails" field status in Mirakl.
3.  **SKU Publishing Failure (New):** Charlene Tan flagged (Mar 31, ~09:09 UTC) that SKU 90248069 was published with an offer but remains offline on the website.
4.  **Picklist Generation Failures:** Muhammad Sufi Hakim Bin Safarudin reported critical incidents on Mar 30 regarding Order #258155683 (missing from Mar 25) and Postponed Order #256653797.
5.  **Data Visibility Gap:** Greta Lee (Mar 27) requested live dashboards for daily MP ordered quantities to bridge the gap between the 4 AM forecast cutoff and real-time volume.
6.  **PickerApp Barcode Errors:** Dang Hung Cuong is investigating a truncation issue for Pureen (SAP: 90247763), where `95561234717` is displayed instead of `9556123471735`. Greta Lee also flagged SKU 90244060 for Yumsay Foods as non-existent.
7.  **Access Management:** Access linkage for Seller ID 31435 was completed by Shiva Kumar Yalagunda Bas on Mar 27.

**Pending Actions & Ownership**
*   **Seller Sync Investigation (Urgent):** Tech team to investigate why DBP accounts 32208 and 32207 failed to sync despite valid internal codes (Michelle Lim, Mar 31).
*   **SKU Live Status:** Investigate why SKU 90248069 is not live on the website despite being published with an offer (Charlene Tan, Mar 31).
*   **Report Email Logic:** Confirm and implement automatic CC of `db-online-marketplace@ntucenterprise.sg` for all DF vendor Sales Breakdown Reports (Iris Chang, Mar 31; cc: Amos Lam, Michelle Lim, Jill Ong).
*   **Picklist Investigation:** Tech team to investigate failures for Order #258155683 and Postponed Order #256653797.
*   **Live Dashboard Request:** Configure dashboard for daily MP ordered quantities (Greta Lee, Mar 27).
*   **Truncated Barcode Investigation:** Dang Hung Cuong to investigate Pureen's barcode issue.
*   **PickerApp SKU Error:** Investigate why SKU 90244060 is flagged as non-existent.
*   **Urgent Promotion Removal:** Dang Hung Cuong and Gopalakrishna Dhulipati to remove incorrectly set up promotion for Item ID: 90244361 (Lalita Phichagonakasit, Mar 20).
*   **Order Status Investigation:** Check discrepancies for Order #256055476 and Order #248407866.
*   **Vendor Report Issues:** Investigate missing sales breakdown reports for CoLab Apac (NED-277148) and Old Shanghai (NED-277329).

**Decisions Made**
*   Dang Hung Cuong is prioritizing the removal of Item ID: 90244361, new picklist failures, Woah Group offers errors, Pureen barcode truncation, and DBP sync issues.
*   Dang Hung Cuong and Shiva Kumar Yalagunda Bas are assigned to investigate vendor picklist anomalies.
*   **Completed:** Access linkage for Seller ID 31435 was successfully executed by Shiva Kumar Yalagunda Bas on Mar 27, 11:29 UTC.

**Key Dates & Deadlines**
*   **2026-03-31:** Michelle Lim reported DBP sync failure for codes 32208 and 32207. Iris Chang raised Sales Breakdown Report email logic query. Charlene Tan reported SKU 90248069 not live.
*   **2026-03-30:** Muhammad Sufi Hakim Bin Safarudin reported picklist generation failures for Order #258155683 and Postponed Order #256653797.
*   **2026-03-27:** Greta Lee reported data visibility gap; Amos Lam requested access for Seller ID 31435 (completed). Lalita Phichagonakasit previously reported Pureen barcode truncation.
*   **2026-03-26:** Iris Chang requested sales report for UNICO Distribution Services; Greta Lee reported Yumsay Foods barcode issue; Ee Ling Tan queried picklist delivery.
*   **2026-03-25:** Cassandra Thoi requested checks on orders #256055476 and #248407866.
*   **2026-03-21:** Amos Lam reported vendor picklist failure due to public holiday opt-out status.


## [13/57] Web Chapter
Source: gchat | Group: space/AAAASzhKzV0/sfn1bAIlsOo | Last Activity: 2026-03-31T09:28:38.208000+00:00 | Last Updated: 2026-03-31T10:43:37.066856+00:00
**Daily Work Briefing: Web Chapter – Farewell Event & Departure Summary**

**Key Participants & Roles**
*   **Varun Chauhan:** Departing employee (7-year tenure with Fairprice Group), Web Chapter member, and acknowledged mentor. Last day: March 31, 2026.
*   **Flora Wo Ke:** Organizer of the farewell event; coordinated the meetup and photo session at L11 main gate.
*   **Alvin Choo, Wai Ching Chan, Jonathan Tanudjaja:** Team members offering final well-wishes and gratitude for support.
*   **Jazz Tong, Harry Akbar Ali Munir, Norman Goh, et al.:** Previous respondents acknowledging mentorship (from prior context).

**Event Timeline & Execution**
The farewell event ("Luckin with Varun") was held on **Tuesday, March 31, 2026**, preceding the scheduled departure time.
*   **06:56 AM:** Flora Wo Ke confirmed the venue choice ("Mama Mia?").
*   **07:05 AM:** The team gathered for a photo session at the **L11 main gate**.
*   **09:28 AM:** Varun Chauhan posted a final thank-you message, stating, "Thanks for the coffee. It was a pleasure working with you all," confirming the event concluded successfully with coffee consumption and group interaction.

**Key Participants' Contributions (New Data)**
Post-event messages from Alvin Choo ("All the best!!!"), Wai Ching Chan ("Farewell!"), and Jonathan Tanudjaja ("Thanks for your support all this time") highlight immediate team appreciation. Varun responded to Flora Wo Ke specifically, reinforcing the successful execution of the coffee meetup.

**Decisions Made & Outcomes**
*   **Event Execution:** The decision by Flora Wo Ke to host a "Luckin with Varun" coffee meetup was successfully executed.
*   **Photo Session:** A team photo was taken at the L11 main gate on the morning of March 31, 2026.

**Status Update & Pending Actions**
*   **Farewell Event Status:** **Completed.** The event occurred as planned between 06:56 AM and 09:28 AM. Varun's final message confirms attendance and satisfaction.
*   **LinkedIn Connection:** Varun previously shared his LinkedIn profile (https://www.linkedin.com/in/varunc1/) for continued networking; this remains a relevant contact point.
*   **Handover/Work Continuity:** No formal handover tasks were discussed in the chat thread. Prior to departure, Varun wished the team luck with upcoming sprints.

**Key Dates & Deadlines**
*   **Departure Date:** March 31, 2026 (Confirmed as last day).
*   **Event Duration:** Morning of March 31, 2026 (Approx. 07:00 AM – 09:30 AM).

No further pending actions regarding the farewell event remain open.


## [14/57] 📢 COM Notifications
Source: gchat | Group: space/AAAAu4WIubc | Last Activity: 2026-03-31T09:26:46.020000+00:00 | Last Updated: 2026-03-31T10:44:47.845751+00:00
**Daily Work Briefing: SonarCloud Quality Monitoring**

**Key Participants & Roles**
*   **gautam-ntuc**: Developer; responsible for `catalogue-job` commits.
*   **Shiva Kumar Yalagunda Bas**: Developer; authored recent `supplier-job` changes (PRs #439, #440).
*   **bitbucket-pipelines**: Automated CI/CD bot triggering merges and deployments.
*   **System/Webhook Bot**: Continues reporting recurring "Webhook Bot is unable to process your request" errors across all notifications.

**Main Topic**
Automated SonarCloud quality gate scans for `catalogue-job`, `fpon-sap-jobs`, `seller-proxy-service`, `supplier-job`, and `fni-product-license-alert`. The conversation tracks code coverage, pipeline retries, and the resolution of failing Quality Gates.

**Status Summary by App**
*   **`seller-proxy-service`**:
    *   **March 25**: PR-2330 recovered to PASSED (97.8% coverage); PR-2331 passed (100% coverage).
    *   **March 31, 06:34–07:06 UTC**: PR-2333 experienced volatility. Initial scans at 06:34 UTC (ver. `afc3a6f`, `91f6df0`) **FAILED** despite 100.0% new code coverage. Status recovered to **PASSED** by 07:06 UTC (ver. `91f6df0`) and confirmed at 07:09 UTC.
*   **`fni-product-license-alert`**:
    *   **March 31, 07:43–09:26 UTC**: PR-1478 passed with 94.4% new code coverage. Subsequent UAT scans (ver. `4dad14f`, `45be0f8`) also achieved **PASSED** status with identical coverage metrics.
*   **`supplier-job` (Shiva Kumar Yalagunda Bas)**: PRs #439/#440 scanned successfully on March 19 at 90.9% coverage; no new activity reported.

**Pending Actions & Ownership**
*   **System Error Investigation**: The "Webhook Bot is unable to process your request" error persists in every notification from March 5 through the latest scans on March 31 (including `seller-proxy-service` PR-2333 and `fni-product-license-alert` PR-1478). No specific owner assigned; requires immediate engineering attention.
*   **`fpon-sap-jobs` Unit Tests**: Discrepancy between 72.7% coverage and 0% unit test success requires review by the respective team.

**Decisions Made**
*   **March 31 Action**: Quality Gate failures for `seller-proxy-service` PR-2333 resolved via automated retries within minutes of the initial failures at 06:34 UTC. Pipelines successfully recovered the gate to **PASSED** status by 07:06 UTC despite 100% coverage metrics.
*   Recent merges in `supplier-job` and recovery scans for `seller-proxy-service` were accepted automatically following retries.

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
*   **March 31**: 
    *   **06:34 UTC**: `seller-proxy-service` PR-2333 failed (100.0% coverage).
    *   **07:06–07:09 UTC**: `seller-proxy-service` PR-2333 recovered to **PASSED**.
    *   **07:43–09:26 UTC**: `fni-product-license-alert` PR-1478 and UAT branches passed (94.4% coverage).


## [15/57] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/nGU0Rak5JT4 | Last Activity: 2026-03-31T08:46:25.117000+00:00 | Last Updated: 2026-03-31T10:47:16.173105+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Initiator of the inquiry regarding invoice logic for older app versions.
*   **Wai Ching Chan:** Provided technical clarification on backend logic and shared a UAT build link.
*   **Andin Eswarlal Rajesh:** Clarified UI vs. PDF generation mechanics; confirmed backend sourcing.
*   **Tiong Siong Tee:** Provided final confirmation regarding app version independence for invoices.
*   *Others mentioned:* Akash Gupta (referenced for PDF confirmation), Alvin Choo.

**Main Topic**
Discussion on whether BCRS deposit details will reflect in customer invoices when a purchase is made via an older application version. The debate focused on the divergence between mobile app UI receipts and backend-generated PDF invoices.

**Decisions Made**
*   **Invoice Content:** Invoices generated from the backend (PDF format) **will** reflect the BCRS deposit line item and total, regardless of the specific app version used for the purchase.
*   **UI Receipts:** Mobile app tax receipts may not display the deposit in the UI, but this does not affect the official PDF invoice generation.
*   **Version Dependency:** Tiong Siong Tee confirmed that invoice generation is not dependent on the app version; it relies on backend data.

**Pending Actions & Ownership**
*   **Verification Testing:** Prajney and the team were advised to download an older Android app build (UAT) from Bitrise to manually verify the invoice output.
    *   *Link:* `https://app.bitrise.io/app/fc15d1785f4e15d5/installable-artifacts/2c1ee233a6aa3e2d/public-install-page/ea74ab2d7b764eda3e2d`
    *   *Owner:* Prajney Sribhashyam (implied via request to "test to make sure").

**Key Dates & Timeline**
*   **Date:** March 31, 2026
*   **Discussion Window:** 06:55 UTC – 08:46 UTC.
*   **Status:** Discussion concluded at 07:37 UTC with Prajney acknowledging the clarification ("Got it"). Tiong Siong Tee provided a reinforcing note at 08:46 UTC.

**Summary of Resolution**
The team confirmed that while older app versions may lack UI visibility for BCRS deposits, the backend correctly adds these deposits to orders. Consequently, the generated PDF invoices will accurately display both the line item and the total amount including the deposit. Manual testing via an older UAT build is recommended to validate this behavior end-to-end.


## [16/57] SRE / Network / DBA / DevOps / Infra
Source: gchat | Group: space/AAAAYX-ew1s | Last Activity: 2026-03-31T08:22:29.168000+00:00 | Last Updated: 2026-03-31T10:48:08.077237+00:00
**Daily Work Briefing: SRE / Infrastructure Team**

**Key Participants & Roles**
*   **Natalya Kosenko:** Submitted new PR #12 (`infra-gcp-gen-ai-spark`) regarding service account rotation compliance; tagged @Himal Hewagamage, @Mohit Niranwal, and @Isuru Dilhan.
*   **Apurva Shingne:** Previously submitted Datadog PR #142 (GCD-8995); pending review by @Sneha Parab and @Nicholas Tan.
*   **Boning He:** Requested pricing workspace access via PR #722; pending review.
*   **Zheng Ming, Wai Ching Chan, Calvin Phan:** Reported connectivity/network issues (GCD-8941, GCD-8954, DSD-11066).
*   **Himal Hewagamage & Isuru Dilhan:** Primary reviewers/approvers for new gen-AI and Terraform requests.

**Main Topics**
1.  **Gen-AI Compliance & Service Accounts:** On **2026-03-31**, Natalya Kosenko submitted PR #12 to remove an unused service account key from `infra-gcp-gen-ai-spark` that had never been rotated, resolving a compliance issue.
2.  **Datadog Infrastructure & Compliance:** Ongoing review of `fp-datadog-eu` PRs (#135–#148). On **2026-03-27**, Apurva Shingne submitted new PR #142 (`infra-gcp-fpg-optimus`) linked to ticket GCD-8995.
3.  **Terraform & Workspaces:** Natalya Kosenko's previous Terraform PR #719 and Boning He's PR #722 (pricing workspace access) remain pending review alongside the new compliance fix. A failed Terraform plan (`run-CZVLtajJGbLVojLM`) and ticket GCD-8900 are active.
4.  **CI/CD Pipeline Failures:** Soni-BE golden pipeline clone failures persist; `lt-strudel-api-go` Go versioning conflicts (Go 1.25.8 vs `golangci-lint`) require resolution.
5.  **Cloud Networking:** AI agents in `us-central1` face internet connectivity issues (Ticket GCD-8941). Mohit Niranwal mandated non-prod testing prior to rollout.
6.  **Bastion Connectivity:** Wai Ching Chan's ticket GCD-8954 remains under investigation.
7.  **Database Subnet Request:** Calvin Phan requested CloudSQL subnets for SOT-SONI (Ticket DSD-11066); DBA coordination with @Himal Hewagamage is active.

**Pending Actions & Ownership**
*   **Review Gen-AI Compliance PR:**
    *   **PR #12:** Owned by **Natalya Kosenko**; requires immediate review by **@Himal Hewagamage**, **@Mohit Niranwal**, and **@Isuru Dilhan**.
*   **Review New Datadog & Terraform PRs:**
    *   **PR #142:** Owned by Apurva Shingne; tagged for review by @Sneha Parab, @Nicholas Tan.
    *   **PR #719** (Natalya) & **PR #722** (Boning): Pending review by @Isuru Dilhan and @Himal Hewagamage.
*   **Troubleshoot Pipeline Issues:** Investigate Soni-BE SSH keys (Kalana) and `lt-strudel-api-go` config conflicts (Lester).
*   **Infrastructure Strategy:** Finalize IaC implementation for Datadog log pipelines (Natalya; discussion with @Prabu Ramamurthy Selvaraj).
*   **Network & DBA Tickets:** Execute non-prod testing for Cloud NAT (GCD-8941); investigate Bastion issues (GCD-8954); review SOT-SONI subnet requirements (DSD-11066).

**Decisions Made**
*   **IaC Requirement:** Mandatory adoption of IaC for Datadog pipelines.
*   **Change Management:** Mohit Niranwal mandated non-prod testing for Cloud NAT changes before production deployment (regarding GCD-8941).
*   **Compliance Action:** Removal of unused, unrotated service account keys is confirmed via PR #12 to address compliance gaps.

**Key Dates & Follow-ups**
*   **2026-03-02 to 03-05:** Initial Datadog PR requests.
*   **2026-03-11 to 03-12:** Critical pipeline failures reported.
*   **2026-03-19:** GCD-8941 raised; Mohit Niranwal intervention regarding testing protocol.
*   **2026-03-20:** Bastion (GCD-8954) and DBA subnet (DSD-11066) tickets opened.
*   **2026-03-24:** PR #140 and #722 requested for review.
*   **2026-03-26:** Channel confirmation for Datadog submissions; @Andin Eswarlal Rajesh engaged.
*   **2026-03-27 (07:30 UTC):** Apurva Shingne submitted PR #142 and ticket GCD-8995.
*   **2026-03-31 (08:22 UTC):** Natalya Kosenko submitted PR #12 for service account key removal; tagged @Himal Hewagamage, @Mohit Niranwal, and @Isuru Dilhan.


## [17/57] QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs | Last Activity: 2026-03-31T08:09:13.351000+00:00 | Last Updated: 2026-03-31T10:48:33.877658+00:00
**Daily Work Briefing: QE <-> All Tribes** (Updated)

**Key Participants & Roles**
*   **Patrick Thun:** Lead/Coordination.
*   **Madhuri Nalamothu:** QA Lead/Test Execution.
*   **Milind Badame:** QA Engineer.
*   **Hang Chawin Tan:** DevOps/Backend Support.
*   **Daryl Ng / Michael Bui:** Dev/Product.
*   **Andin Eswarlal Rajesh:** Development.
*   **Oktavianer Diharja:** Pipeline Support.
*   *(Previous roles: Zaw Myo Htet, Tiong Siong Tee, Yangyu Wang, Pandi, Aman Saxena, Komal Ashokkumar Jain retained for historical context).*

**Main Topics & Discussion**
1.  **Pipeline Error (New - Critical):** On **31 Mar**, Hang Chawin Tan reported a pipeline failure in `dp-gifting-web`. *Status:* Active discussion involving @Madhuri Nalamothu, @Milind Badame, and @Oktavianer Diharja awaiting resolution.
2.  **BCRS Swimlane Management:** On **31 Mar**, Milind Badame queried if BCRS swimlanes can be disabled post-UAT completion. *Status:* Discussion ongoing with @Daryl Ng and @Andin Eswarlal Rajesh to determine cleanup protocols.
3.  **System-Wide Intermittent Failures:** On **30 Mar**, Milind Badame reported frequent HTTP 500 errors affecting order placement, cart, and PDP pages. *Status:* Active investigation for backend instability vs. testing impact.
4.  **Order Placement Failure ('Strong Tasty Brew'):** On **30 Mar**, Madhuri Nalamothu reported inability to place orders for non-FP product 'Strong Tasty Brew'. Discussion ongoing with @Piraba Nagkeeran.
5.  **MiniGames Blank Screen:** On **30 Mar**, Milind Badame reported a blank white screen when tapping the MiniGames tile as a guest user followed by login on lower Android versions. *Owner:* @Aman Saxena, Mobile Team.
6.  **DC Membership Subscription Issue:** On **30 Mar**, Madhuri Nalamothu confirmed subscription failures impact both new and existing users. *Owner:* @Kadar Sharif.
7.  **LinkPoints Regression Failure:** Reported on **27 Mar** regarding CLS Award Balance API `500` errors ("Transaction posting failed"). Status remains Critical/Blocked pending resolution with @Pandi.

**Pending Actions & Ownership**
*   **Pipeline Resolution:** Resolve `dp-gifting-web` pipeline error reported by @Hang Chawin Tan. *Owners:* @Madhuri Nalamothu, @Milind Badame, @Oktavianer Diharja. **(Highest Priority)**
*   **BCRS Cleanup Strategy:** Confirm feasibility of disabling BCRS swimlanes post-UAT and implement if approved. *Owners:* @Daryl Ng, @Andin Eswarlal Rajesh.
*   **System Stability Investigation:** Identify cause of widespread HTTP 500 errors on PDP/Cart/Order Placement (30 Mar). *Owner:* Dev Team / @Hang Chawin Tan.
*   **MiniGames Crash Fix:** Resolve blank screen issue on MiniGames tile for guest users/login flow. *Owner:* @Aman Saxena.
*   **DC Membership Fix:** Resolve subscription failures impacting all user segments. *Owner:* @Kadar Sharif. **(Critical)**

**Decisions Made**
*   System-wide errors on 30 Mar require immediate triage; potential testing activity suspected by Milind Badame but not yet confirmed as the root cause.
*   DC Membership issue escalated to @Kadar Sharif due to scope affecting existing users.
*   MiniGames blank screen investigation assigned to @Aman Saxena.

**Key Dates & Deadlines**
*   **31 Mar (Morning):** Pipeline error reported; BCRS swimlane query raised.
*   **30 Mar (Morning/Afternoon):** System-wide 500 errors, Cart issues, 'Strong Tasty Brew' failure, MiniGames blank screen, DC membership issue confirmed.
*   **27 Mar:** LinkPoints API failure and iOS SnG Flow loading stuck.
*   **26 Mar:** Express cart service fee discrepancy.


## [18/57] [BCRS]-SAP to POS & DBP Interface Deployment
Source: gchat | Group: space/AAQAeMC3qBk | Last Activity: 2026-03-31T07:04:54.234000+00:00 | Last Updated: 2026-03-31T10:49:34.229356+00:00
**Daily Work Briefing: [BCRS]-SAP to POS & DBP Interface Deployment**

**Key Participants & Roles**
*   **Onkar Bamane:** Deployment Lead/Coordinator.
*   **Michael Bui:** Deployer (Production OData/SAP).
*   **Hendry Tionardi:** Technical Advisor.
*   **Prajney Sribhashyam:** Process Owner/Test Coordinator.
*   **Daryl Ng:** Technical Advisor/Approver.
*   **Anthony Vaz:** Technical Contributor.
*   **Suwandi Cahyadi:** Recipient of API clarification inquiry.
*   **Sneha Parab:** Technical Contributor (Inventory Management).
*   **Olivia:** Resource for Inventory Support.
*   **Alvin Choo:** Stakeholder (Data Integrity/Integration).
*   **Others:** Wai Ching Chan, Kandasamy Magesh.

**Main Topic**
Transition from initial deployment execution to active post-deployment validation. A critical conflict has emerged regarding the creation of production inventory for BCRS testing. While Sneha Parab initially requested stock creation, technical reviews by Olivia and Onkar Bamane confirmed that SAP Production cannot hold test stock or SKU data via UD processes, as DBP back-office updates do not sync to IMS (Inventory Management System).

**Decisions Made & Status Update**
1.  **Deployment Execution:** Confirmed **DBP deployment proceeded first**, followed by SAP OData. Michael Bui successfully deployed to Production (PRD) on March 26, 2026.
2.  **Inventory Strategy Shift (Critical):** The requirement to add stock in SAP has been rejected.
    *   **Technical Constraints:** Olivia clarified that UD is for SKU data only; SAP cannot hold real test SKUs. Sneha Parab confirmed DBP back-office changes do not update IMS/stock sync from SAP.
    *   **Consensus Reached:** Onkar Bamane confirmed SAP does not depend on Stock On Hand (SOH) to process orders; the system can function with zero SOH.
3.  **Proposed Solutions:** Two options were presented by Sneha Parab and challenged by Alvin Choo:
    *   *Option A:* Add inventory directly in DBP only, complete testing, then reset (Alvin Choo noted this risks mocking data rather than testing true system integration).
    *   *Option B:* Ops team enables "unlimited stock" for specific test SKUs temporarily, requiring quick execution to disable afterward.
4.  **Database Integrity:** A debate arose regarding the risk of updating production data; Alvin Choo emphasized the need for correct data flow to validate system integration effectively.

**Pending Actions & Ownership**
*   **Finalize Inventory Method:** Decide between "Unlimited Stock" enablement (Ops team) or DBP-only inventory with a reset plan. *(Owner: Sneha Parab, Onkar Bamane, Alvin Choo)*
    *   *Context:* Must balance testing integrity vs. production data safety.
*   **API Clarification Response:** Provide definitive confirmation on `ZUD_DOWNLOAD` API calls (specifically regarding the exclusion of LB). *(Owner: Technical Team / Suwandi Cahyadi)*
    *   *Note:* Replies may be deferred until tomorrow during working hours.
*   **DBP Production Validation:** Monitor the "DBP Production Testing" thread for test results and anomalies. *(Owner: Prajney Sribhashyam)*
*   **Update Deployment Steps:** Continue adding specific deployment steps to the shared spreadsheet, specifically **MP Article creation** by Sneha Parab. *(Owner: Michael Bui, Sneha Parab)*
*   **Add Missing PICs:** Identify and add any missing Persons In Charge (PICs). *(Owner: Sneha Parab, Prajney Sribhashyam)*

**Key Dates & Deadlines**
*   **Deployment Window:** Friday, March 26, 2026 (Completed).
*   **Inventory Debate Date:** Monday, March 31, 2026 (In Progress).
*   **Expected Reply on API:** Tomorrow during working hours.

**References**
*   **Thread: DBP Production Testing:** https://chat.google.com/space/AAQAeMC3qBk
*   **Deployment Plan/Tracker:** https://docs.google.com/spreadsheets/d/1gvCjdXWB2BeWr7XgBQs0-zKeLxGi3OmX4ZrbY6pNMeQ/edit?gid=1022676232#gid=1022676232


## [19/57] RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Last Activity: 2026-03-31T07:04:40.405000+00:00 | Last Updated: 2026-03-31T10:49:58.474652+00:00
**Daily Work Briefing: Automated Test Results Summary (RMN Notification)**

**Key Participants & Roles**
*   **Collection Runner App:** Automated testing agent executing API suites.
*   **Webhook Bot:** Reporting mechanism; consistently returning "unable to process your request" on all notifications through March 31, 2026.
*   **Parties Involved:** System-generated notification log only.

**Main Topic/Discussion**
Automated nightly API test executions across `promo-service`, `marketing-personalization-service`, and `marketing-service` in the **staging** environment. Monitoring period spans March 12 through **March 31, 2026**. Execution windows occur at approximately 01:05 UTC (morning), 02:30/02:31 UTC (midnight), and **03:20/03:21 UTC** (early morning).

**Test Execution Status & Anomalies**
*   **`marketing-service` Stability Confirmation:** The streak of resolution extends through March 31.
    *   **March 31, 01:05 UTC:** Executed successfully with **53 API Tests Passed / 0 Failed / 0 Skipped** (Total Requests: 17).
    *   **Contract Tests:** 20 Passed / 0 Failed / 0 Skipped (Total Requests: 16).
    *   **Historical Context:** Recurring instability persisted from March 17 through early March 25. Temporary stabilization occurred on March 25; the morning failure streak broke on March 26. Stability confirmed for March 26–31.
*   **`promo-service`:** Confirmed stable on March 31 at **02:31 UTC**. The latest run showed **10 API Tests Passed / 0 Failed** and **6 Contract Tests Passed / 0 Failed** (Total Requests: 3 each). Stability confirmed for March 26–31.
*   **`marketing-personalization-service`:** New data confirms a successful run at **03:21 UTC on March 31**.
    *   **API Contract Tests:** 125 Passed / 0 Failed (Total Requests: 21).
    *   **API Tests:** 96 Passed / 0 Failed (Total Requests: 21).
    *   This confirms stability for March 31, extending the successful streak from March 27–31.

**Pending Actions & Ownership**
*   **Webhook Bot Remediation (High Priority):** The bot failed to process requests in every notification cycle from March 12 through the latest log on **March 31 at 07:04 UTC**. Immediate attention is required from DevOps or Automation Infrastructure.
*   **Verify `marketing-service` Stability:** Engineering must continue monitoring subsequent runs to confirm the resolution of early-morning flakiness observed between March 17–25 was permanent.

**Decisions Made**
*   No human decisions recorded; all entries are automated system outputs.

**Key Dates & Deadlines**
*   **Failure Window (Historical):** Instability noted on March 12, 13, and persistently from **March 17 through March 25**.
*   **Current Status:** Successful runs observed on March 26–31 across all three services.
    *   `marketing-service`: Passed at 01:05 UTC (March 31). Previous stable window noted March 26–30.
    *   `promo-service`: Passed at 02:30/02:31 UTC (March 26–31).
    *   `marketing-personalization-service`: Passed at 03:20/03:21 UTC (March 27–31).
*   **Monitoring Period:** Data covers runs from **March 12, 2026**, through **March 31, 2026**.

**Resource Info**
*   **Message Count:** Updated to reflect notifications through March 31.
*   **URL:** https://chat.google.com/space/AAQA85dw4So


## [20/57] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Last Activity: 2026-03-31T07:04:02.984000+00:00 | Last Updated: 2026-03-31T10:50:35.991907+00:00
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
1.  **Unit Price Calculation Compliance (New):** On Mar 31, Lester Santiago Soriano highlighted a government compliance requirement for Phase 2 unit price calculations. The current reliance on parsing the free-form `display_units` field (e.g., "20 x 320ml") is unscaleable due to complex formats like "3 x 64 per pack (CTN)."
    *   **Proposed Solution:** Ingest structured fields (`pack_size`, `pack_size_unit`, `pack_size_bundle`) from Mirakl/SAP into DBP for consumption by `website-service`.
    *   **Action:** Sneha Parab requested an initial effort assessment to map and flow these three fields.
2.  **B2B SKU Sync Clarification:** On Mar 30, Sneha Parab requested clarity on B2B SKU synchronization to WMS. Akash Gupta responded by 9:20 AM.
3.  **UAT Stock Sourcing Update:** Sneha Parab requested specific SKUs (128373, 13205552, etc.) be marked as unlimited stock in UAT for bulk order testing. Wai Ching Chan is handling the update (Mar 30).
4.  **BCRS Deposit Logic Failure:** On Mar 30, Wai Ching Chan reported missing deposit values during UAT checkout. Sundy Yaputra has been flagged to investigate this regression.
5.  **BCRS Epic Closure Urgency:** Sneha Parab continues to push for the closure of the BCRS epic (DPD-637 and DPD-807 remain in "Define" state). Inputs required from Akash Gupta, Michael Bui, and Andin Eswarlal Rajesh.
6.  **iOS Address Emoji Blocking Bug:** Wai Ching Chan reported on Mar 26 that customer addresses with emojis on iOS cause order time slot failures (Customer ID: 2022036). Logic validation is required during address add/edit.
7.  **Slot Date Discrepancy:** Shiva Kumar Yalagunda Bas reported a delivery slot mismatch (UI shows 25th, API indicates 23rd). Daryl Ng and Sundy Yaputra are resolving this.
8.  **Omni Home Split Flag Regression:** On Mar 31 at 02:27 UTC, Daryl Ng reported that Omni home swimlanes fail to follow the split flag, requesting ads based on older configurations or none due to backend default setting updates.

**Pending Actions & Ownership**
*   **Sundy Yaputra:** Investigate missing BCRS deposit values in UAT checkout (Reported by Wai Ching Chan, Mar 30).
*   **Wai Ching Chan:** Update specified SKUs to "unlimited stock" in UAT.
*   **Akash Gupta, Michael Bui, Andin Eswarlal Rajesh:** Provide immediate inputs on BCRS tickets **DPD-637** and **DPD-807**.
*   **Lester Santiago Soriano / Sneha Parab:** Assess effort required to map `pack_size`, `pack_size_unit`, and `pack_size_bundle` from Mirakl/SAP to DBP for `website-service`.
*   **Daryl Ng:** Review Michael Bui's PR #7 (`bcrs-deposit-posting`). Investigate Omni home split flag issue with Nikhil and Yangyu Wang.
*   **Wai Ching Chan, Gopalakrishna Dhulipati, Dang Hung Cuong:** Validate emoji blocking logic for iOS address entry (Customer ID: 2022036).
*   **Zaw Myo Htet:** Clarify pre-order payment redemption logic; execute UAT testing on offboarded Pinelabs split feature flag.
*   **All Engineers:** Mark production-deployed tickets as "Status = Done."

**Decisions Made**
*   **Unit Price Structure:** Move from parsing `display_units` to utilizing structured fields (`pack_size`, `pack_size_unit`, `pack_size_bundle`) for Phase 2 compliance.
*   **BCRS Epic Priority:** Immediate action required to close the BCRS epic; ticket status must be verified for DPD-637 and DPD-807.
*   **UAT Stock Critical:** Specific SKUs identified by Sneha Parab must be set to unlimited stock immediately.
*   **Deposit Logic Fix:** Focus remains on PR #7 review and investigating the UAT regression where deposit values are missing.

**Key Dates & Deadlines**
*   **Mar 30, 2026 (Yesterday):** B2B sync clarity requested; UAT stock updates required; BCRS deposit failure reported.
*   **Mar 31, 2026 (Today):** Unit price compliance discussion initiated by Lester Santiago Soriano; Omni home split flag regression reported. Sports Hub FFS store closure deadline active.

**Note on Historical Context:** Previous mentions of code review priorities for `layout-service` PR #362 are superseded by the urgent Strudel SDK deployment update (`go-platform-website`). The current focus includes investigating the UAT BCRS deposit regression, updating UAT stock levels, resolving slot date mismatches, closing the BCRS epic via tickets DPD-637 and DPD-807, debugging the Omni home split flag configuration, and assessing the effort for structured unit price field ingestion.


## [21/57] QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs/YgGvvuD2Ow8 | Last Activity: 2026-03-31T06:50:57.621000+00:00 | Last Updated: 2026-03-31T10:52:25.003908+00:00
**Daily Work Briefing: Ad Slot Configuration Changes (QE <-> All Tribes)**

**Key Participants & Roles**
*   **Michael Bui:** Initiator of the change; responsible for managing the change window, testing timeline, and subsequent reset.
*   **Komal Ashokkumar Jain:** Stakeholder managing impact analysis.
*   **Milind Badame:** Monitors UAT status and E2E test failures; initiated the latest follow-up.

**Main Topic**
Ongoing discussion regarding temporary modifications to ad slot positions in swimlanes. Existing User Acceptance Testing (UAT) scripts hardcoded to positions 1 and 3 are failing due to these changes. The system remains in its modified configuration pending final UAT completion and a reset to original positions.

**Decisions Made & Status Updates**
*   **Current Status:** As of March 31, UAT completion status is unconfirmed. E2E tests involving hardcoded positions 1 & 3 continue to fail.
*   **Protocol Update:** On March 25, the team agreed to ignore specific failing test cases temporarily. This protocol remains in effect pending Michael Bui's confirmation that testing is complete. No reset has occurred; the configuration remains active.

**Pending Actions & Ownership**
*   **UAT Finalization Confirmation:** Milind Badame initiated a new follow-up on March 31, explicitly asking Michael Bui if UAT is done. The team awaits this specific confirmation to determine the timeline for reverting ad slots.
*   **Execution Oversight:** Michael Bui retains full responsibility for executing the ad slot reset (back to positions 1 & 3) immediately upon confirming UAT completion. No new reset date has been established pending his response to the March 31 inquiry.

**Key Dates, Deadlines & Follow-ups**
*   **Original Start Date:** March 12, 2026 (Changes active "starting today").
*   **Original Scheduled End:** End of Next Week (March 19, 2026). *Status:* Deadline passed; testing remains incomplete.
*   **Previous Inquiry/Response:** March 24, 2026 at 08:44 UTC (Michael Bui stated UAT was "not fully completed yet").
*   **March 25 Acknowledgment:** Milind Badame confirmed ongoing E2E failures and agreed to ignore tests pending further updates.
*   **Latest Follow-up:** March 31, 2026 at 06:50 UTC (Milind Badame asked directly: "Hi, just a quick follow up, is the UAT done?").

**Summary of Chronology**
On March 12, 2026, Michael Bui initiated ad slot changes, warning that tests hardcoded for positions 1 and 3 would fail. While an initial End-of-Week (March 19) deadline was set, testing remained incomplete by March 24. On that date, Milind Badame queried the status; Michael Bui responded at 08:44 UTC confirming UAT was not finished.

On March 25, 2026, Milind Badame acknowledged the delay and noted persistent E2E failures, agreeing to ignore these specific test cases until a new update was provided. The configuration remained active with no reset scheduled.

On March 31, 2026 at 06:50 UTC, Milind Badame sent a direct follow-up message ("Hi, just a quick follow up, is the UAT done? @Michael Bui"). As of this timestamp, Michael Bui has not provided a confirmation that testing is complete. Consequently, the system remains in its modified state, E2E failures persist, and the reset protocol remains dormant pending Michael's response to the March 31 inquiry.


## [22/57] Yangyu Wang
Source: gchat | Group: dm/4Ut7xcAAAAE | Last Activity: 2026-03-31T06:35:17.544000+00:00 | Last Updated: 2026-03-31T10:53:31.169586+00:00
**Daily Work Briefing: Layout Service Deployment (PR #362) & Slot Issue Investigation Update**

**Key Participants & Roles**
*   **Yangyu Wang:** Initiator/Deployer. Investigated slot issues, deployed PR #362 for default slot testing, executed a rollback due to adverse effects, and subsequently reported the temporary fix was effective.
*   **Michael Bui:** Approver/Monitor. Validated safety initially; assisted in clarifying customer impact.
*   **Nikhil:** Suggested the initial testing approach via default slot updates.

**Main Topic**
Investigation into ads slots sent to OSMOS appearing as incorrect values (2 or 6 instead of defaults 1, 3). Initial deployment on March 30 intended to test updated default slots but caused swimlanes to stop taking ads, triggering an immediate rollback. Subsequent verification confirmed the temporary solution works.

**Decisions Made & Outcomes**
*   **Deployment Approval:** Michael Bui approved the initial `layout-service` deployment on March 24 as safe after clarifying it was distinct from a prior `website-service` error.
*   **Rollback Execution:** On March 30, following reports that swimlanes stopped accepting ads post-deployment, Yangyu executed an immediate rollback at ~13:43 UTC and requested Michael Bui's assistance for investigation.
*   **Resolution Update:** On March 31, Yangyu corrected the previous assessment, confirming that the temporary solution (changing default slots) **works**. Consequently, the incident is resolved, and no further investigation or rollback verification is required at this time.

**Actions & Ownership**
*   **Completed Actions:**
    *   **Deployment (March 24):** Executed by Yangyu Wang; acknowledged by Michael Bui.
    *   **Investigation & Rollback (March 30):** Yangyu deployed the default slot update, observed failure ("most swimlane no longer take ads"), and initiated a rollback.
    *   **Resolution Confirmation (March 31):** Yangyu issued a correction confirming the temporary fix is effective, negating the need for immediate further action.
*   **Pending Actions:**
    *   None. The pending verification by Nikhil regarding the failure status has been superseded by the confirmation that the solution works. Michael Bui's assistance in troubleshooting is no longer required as the issue is resolved.

**Key Dates, Deadlines & Timeline**
*   **2026-03-24 | 06:36 UTC:** Initial `layout-service` PR #362 deployment confirmed successful.
*   **2026-03-30 | 11:08 AM:** Michael Bui inquires about the specific issue behind Yangyu's PR regarding default slots.
*   **2026-03-30 | 11:10 AM:** Yangyu explains ads sent to OSMOS show values of 2 or 6 instead of defaults 1, 3; Nikhil suggests updating the default slot for testing.
*   **2026-03-30 | 11:17 AM:** Yangyu confirms deployment.
*   **2026-03-30 | ~01:42 PM (UTC):** Yangyu reports the change failed; most swimlanes no longer take ads.
*   **2026-03-30 | ~01:43 PM:** Yangyu executes rollback and requests Michael's help to investigate further.
*   **2026-03-31 | 06:35 UTC:** Yangyu issues a correction stating the temporary solution works, advising to disregard the previous failure reports.

**Summary of Event Flow**
On March 24, 2026, the initial deployment of `layout-service` PR #362 was successfully executed. On March 30, Yangyu deployed an update suggested by Nikhil to address OSMOS slot misalignment (showing values 2 or 6 instead of defaults 1 or 3). The deployment caused swimlanes to stop accepting ads, leading Yangyu to roll back the changes at ~13:43 UTC and request Michael Bui's assistance for troubleshooting. However, on March 31 at 06:35 UTC, Yangyu issued a correction confirming that the temporary solution of changing default slots **works**. The previous reports of failure are disregarded, resolving the incident without further action from Nikhil or Michael Bui regarding this specific slot issue.


## [23/57] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/XnO4XifIieI | Last Activity: 2026-03-31T06:33:43.472000+00:00 | Last Updated: 2026-03-31T10:54:00.753719+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Key Participants & Roles**
*   **Daryl Ng**: Reported an issue regarding homepage integration with the Split flag.
*   **Michael Bui**: Recipient of the initial report (CC'd).
*   **Yangyu Wang**: Resolved the reported issue and identified a temporary fix.
*   **Nikhil**: Source of the escalation to Daryl Ng.

**Main Topic/Discussion**
Investigation into why the Omni homepage swimlanes fail to adhere to the new Split flag configuration. Specifically, certain swimlanes continued requesting ad slots based on legacy configurations rather than the updated split logic. An attempted backend update to default settings inadvertently caused these swimlanes to cease requesting ads entirely.

**Pending Actions & Ownership**
*   **Action**: Submit a Pull Request (PR) implementing the identified temporary solution for the Split flag issue.
*   **Owner**: Yangyu Wang.
*   **Status**: In progress; PR submission is imminent ("soon").

**Decisions Made**
*   A temporary technical workaround was successfully identified by Yangyu Wang to bypass the backend configuration regression that halted ad requests. No permanent architectural decision has been finalized yet pending the PR review.

**Key Dates & Deadlines**
*   **Issue Reported**: March 31, 2026, at 02:27 UTC (Daryl Ng).
*   **Resolution Identified**: March 31, 2026, at 06:33 UTC (Yangyu Wang).
*   **Follow-up**: Submission of the PR for the temporary solution is expected shortly after the 06:33 UTC update.

**Reference Details**
*   **Space URL**: https://chat.google.com/space/AAQAUbi9szY
*   **Message Count**: 2


## [24/57] D&T Funtastic Team
Source: gchat | Group: space/AAQARGCS1Wk | Last Activity: 2026-03-31T06:21:03.514000+00:00 | Last Updated: 2026-03-31T06:41:51.668313+00:00
**Daily Work Briefing: D&T Funtastic Team (Google Chat)**

**Key Participants & Roles**
*   **Trina Boquiren:** Primary communicator/organizer. Coordinates Q1 All Hands, manages training registrations, and initiates new engagement initiatives (Power Breakfast, EDM voting).

**Main Topics**
1.  **Post-Event Follow-up:** Execution of Q1 All Hands wrap-up (photo collection).
2.  **AI Upskilling Initiative:** Coordination of the "Gemini Enterprise & NotebookLM" training session (March 19 completed/due).
3.  **International Food Day:** EDM design selection requiring team voting on shortlisted options.
4.  **D&T Power Breakfast:** Launch of a recurring monthly volunteer program to co-create engaging moments for the team.

**Actions Pending & Ownership**
*   **Action:** Vote for International Food Day eDM designs (select top 2).
    *   **Owner:** All team members.
    *   **Context:** Voting via reactions on image links provided by Trina. Deadline implied immediate.
*   **Action:** Sign up as volunteers for the D&T Power Breakfast series.
    *   **Owner:** Interested team members.
    *   **Requirement:** Select 4 available slots across recurring sessions (Last Thursday of every month).
    *   **First Session:** April 28, 9:00 AM – 10:30 AM at Lobby B Pantry.
    *   **Resource:** Sign-up sheet: https://docs.google.com/spreadsheets/d/1cGylUKJUbBoF3LU4ZQB2wzT59ETiSOKqf7HYUoznz74/edit?usp=sharing
*   **Action:** Upload photos taken during the Q1 All Hands to the designated album.
    *   **Owner:** All team members (specifically requested by Trina).
    *   **Link:** https://photos.app.goo.gl/yzn3e35tr4RRrrFT7
*   **Action:** Register for the Gemini Enterprise Training via the provided form.
    *   **Note:** Calendar acceptance does not guarantee entry; seats are limited. Registration is required separately. (March 19 event context).
    *   **Owner:** All team members.
    *   **Link:** https://forms.gle/p4dCU5rsmg5mrKh66

**Decisions Made**
*   **Q1 All Hands:** Protocol established for introducing the D&T 2026 FUNtastic Team (stand up and move to front when names are called).
*   **Gemini Training:** Session held on March 19, 2026. A certified Google Trainer was onsite at FP Hub L10 covering Prompt Engineering, NotebookLM, Agent Building, and live demos ("Polly" and "ITSM Service Request Agent").
*   **Power Breakfast:** Established as a recurring monthly event (Last Thursday) starting April 28 to foster team co-creation.
*   **EDM Design:** Selection method confirmed; the final design will be determined by majority vote on the shortlisted options.

**Key Dates & Timeline**
*   **March 6, 2026:** Initial RSVP reminder sent for Q1 All Hands.
*   **March 11-12, 2026:** Q1 All Hands held; photo collection link distributed.
*   **March 16, 2026:** Gemini Enterprise Training announced.
*   **March 19, 2026:** Gemini Enterprise & NotebookLM Exclusive Training (FP Hub L10).
*   **March 31, 2026:** Trina Boquiren opened voting for International Food Day eDMs and launched Power Breakfast volunteer sign-ups.
*   **April 28, 2026:** First D&T Power Breakfast session (9:00 AM – 10:30 AM, Lobby B Pantry).

**Summary of Flow**
Following the successful Q1 All Hands on March 12 and the subsequent AI upskilling training on March 19, Trina Boquiren has shifted focus to springtime team engagement. On March 31, she initiated a voting drive for International Food Day eDM designs (top 2 selection) and launched the "D&T Power Breakfast." This new recurring initiative, held monthly on the last Thursday starting April 28, seeks volunteers to co-create fun events at Lobby B Pantry. Trina provided a shared calendar and sign-up sheet to manage recurring volunteer slots, emphasizing the need for participants to commit to four sessions.


## [25/57] D&T Funtastic Team
Source: gchat | Group: space/AAQARGCS1Wk/5YZW6i2wniE | Last Activity: 2026-03-31T06:14:05.891000+00:00 | Last Updated: 2026-03-31T06:42:44.669332+00:00
**Daily Work Briefing: D&T Funtastic Team**

**Key Participants & Roles**
*   **Trina Boquiren:** Initiator and project lead for the International Food Day eDM design selection.
*   **Team (@all):** Stakeholders responsible for reviewing options and casting votes.

**Main Topic**
Selection of the final email design (eDM) for the upcoming **International Food Day**. Trina presented three shortlisted design concepts to gather team consensus on which best represents the event's spirit.

**Pending Actions & Ownership**
*   **Action:** Review the three provided design options and vote for the top two favorites using reaction emojis ("on" the images).
*   **Owner:** All team members.
*   **Context:** Voting is required to determine the final design choice based on collective preference.

**Decisions Made**
*   No final decision has been made yet; the process is currently in the voting phase. The final selection will be determined by the aggregate votes received from the team.

**Key Dates & Follow-ups**
*   **Event:** International Food Day (Upcoming).
*   **Discussion Date:** March 31, 2026.
*   **Initiation Time:** Votes were requested starting at 06:07 UTC on March 31, 2026.
*   **Next Step:** Completion of voting to finalize the design before the event date.

**Reference Data**
*   **Space URL:** https://chat.google.com/space/AAQARGCS1Wk
*   **Message Count:** 4
*   **Options Presented:** Option 1, Option 2, Option 3 (posted between 06:11 and 06:14 UTC).


## [26/57] Plan the activity for Power Breakfast - Mar 31
Source: gchat | Group: space/AAQAQ39saZQ | Last Activity: 2026-03-31T05:57:20.838000+00:00 | Last Updated: 2026-03-31T06:43:00.308210+00:00
**Daily Work Briefing: Power Breakfast Planning (Mar 31)**

**Key Participants & Roles**
*   **Trina Boquiren:** Meeting organizer, room booker, and event coordinator. She owns the planning spreadsheet ("DnT FUNtastic Calendar of Events 2026") and is soliciting volunteers.
*   **Aman Saxena:** Participant confirming meeting logistics (room location).
*   **Sirisha Turlapati:** Participant clarifying venue details.

**Main Topic**
Coordination for the upcoming "Power Breakfast" activity, specifically finalizing the venue and recruiting staff to help facilitate the event series starting in April 2026.

**Decisions Made**
*   **Venue Confirmed:** The meeting will be held in the **Mocha Room**.
    *   *Note:* Trina Boquiren clarified this after Aman Saxena asked about "room 11" and Sirisha Turlapati suggested "mocha." Trina confirmed the booking is secured there.

**Pending Actions & Ownership**
*   **Action:** Sign up to volunteer/help with the Power Breakfast series.
    *   **Owner:** All team members (specifically requested by Trina Boquiren).
    *   **Method:** Via the shared Google Sheet ("DnT FUNtastic Calendar of Events 2026").

**Key Dates & Deadlines**
*   **Meeting Date:** March 31, 2026 (Current conversation date/time: 05:32–05:57 UTC).
*   **First Power Breakfast Event:** April 28, 2026.
    *   **Time:** 9:00 AM – 10:30 AM.
    *   **Location:** Lobby B Pantry.
*   **Ongoing Schedule:** The event will occur on the **last Thursday of every month** for the remainder of 2026.

**References & Resources**
*   **Meeting Link:** https://chat.google.com/space/AAQAQ39saZQ
*   **Planning Document:** DnT FUNtastic Calendar of Events 2026 (Google Sheet) - Owner: Trina Boquiren.


## [27/57] FPG Everyone - General
Source: gchat | Group: space/AAAAjDYVcBU | Last Activity: 2026-03-31T05:49:13.221000+00:00 | Last Updated: 2026-03-31T06:43:39.449732+00:00
**Daily Work Briefing: FPG Everyone Chat Summary (Updated)**
**Date Range:** March 3 – April 1, 2026
**Source:** Google Chat (FPG Everyone - General)

### Key Participants & Roles
*   **Serene Kua Puay Leng:** Promotes daily product deals and lobangs.
*   *(Previous participants retained: Siti Nabilah, Jasmine Neo, Keith Lee, Melissa Lim, Maisy Heeng, Si Min Ng)*

### Main Topics
1.  **Digital Access Rollout:** Completed as of Mar 30. User guide distributed.
2.  **Media Collaboration – "Bowl of Love":** Final episodes featuring Tyler Ten, Tasha Low, and Xiang Yun are live (Mar 21 launch). Focuses on warmth/healing with fresh Malaysian pork. Platform: @mediacorp.re.dian TikTok.
3.  **Industry Recognition:** Lau Pa Sat's "Spin for your Huat" featured by Campaign Asia as a top CNY 2026 campaign alongside Nike and Apple.
4.  **FairPrice Heartland Hits Launch (Mar 27):** Community storytelling contest (#FPHeartlandHits, #FPNorthie, etc.). Incentive: $50 E-Vouchers + feature in final song. Deadline: April 5, 2026.
5.  **Unity Wellness Promotions:**
    *   **B1G1 Offer (Mar 26–29):** Zhaoyue Touw announced Buy 1 Get 1 Free on health/wellness essentials at Unity stores. Link: `https://go.fpg.sg/Unity-MarB1G1`.
    *   **Wellness Picks:** Highlighted products include Moom Health, Elastine, New Moon Bird's Nest, and Greenlife Derma.
6.  **New Brand Launch – Shabu Days (FPG Food Services):** First overseas brand launching April 3 at Hillion Mall. Hotel-inspired dining at heartland prices. IG/FB active.
7.  **Linkpoints Loyalty Promo ($0.99):** Updated redemption details (Mar 30) for FairPrice Maple Syrup Cashews and Myojo Bowl Noodles. Collection deadline: April 5, 2026.
8.  **New Product Promo – Delicato Sausages:** Serene Kua Puay Leng announced a deal on **Delicato Japanese-style sausages** (Flavours: Japanese Curry & Bonito Seaweed) at FairPrice.
    *   **Price:** $3.95/packet (U.P. $4.85).
    *   **Duration:** Promo valid until **April 15, 2026**.

### Pending Actions & Ownership
*   **Shorty Awards Voting (Owner: All Staff):** Vote daily via personal email for *Bridge to Equity* and *2025 End-Of-Year Unpacked*. Deadline: **April 8**.
*   **Linkpoints Redemption (Owner: All Staff):** Redeem $0.99 rewards. Collection deadline: **April 5, 2026**.
*   **Volunteer Engagement:** Sign up for upcoming opportunities via `https://forms.gle/UkyQDagmDy4mcY7K7`. "Willing Hearts Kitchen Crew" is fully booked as of Mar 27.
*   **Sensory Test Sign-ups:** Chapati screening form remains open (`https://forms.gle/DFYrahZcvhtcoJ9R7`). Frozen Snacks sign-up is closed.
*   **Delicato Sausage Trial (Owner: All Staff):** Staff encouraged to purchase Delicato sausages during the promo run through April 15 for an instant meal upgrade.

### Decisions Made
*   **Awards Campaign:** Mobilization approved for Shorty Awards voting.
*   **Wellness Extension:** Unity B1G1 offer extended (Mar 26–29).
*   **Loyalty Initiative:** $0.99 redemption launched with specific SKUs (Cashews/Myojo Noodles).
*   **Brand Expansion:** Shabu Days launch approved for April 3.
*   **Product Promotion:** Delicato sausage promo activated at FairPrice through April 15.

### Critical Dates & Deadlines
*   **March 26–29:** Unity B1G1 Promotion.
*   **April 3:** Shabu Days launch (Hillion Mall).
*   **April 5:** Heartland Hits contest closes; Linkpoints redemption collection ends.
*   **April 8:** Shorty Awards voting deadline.
*   **April 15:** Delicato Japanese-style sausage promo expires.


## [28/57] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw | Last Activity: 2026-03-31T04:38:59.393000+00:00 | Last Updated: 2026-03-31T06:52:08.030128+00:00
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
*   **Jazz Tong:** Incident Coordinator.
*   **Akash Gupta:** Support Lead.
*   **Vivian Lim Yu Qian:** Staff Verification Specialist.
*   **Mohammad Adyatma:** Team Member (Security).

**Main Topics & Discussions**
1.  **FPPay Production Issue:** On March 30, 2026 (09:11 UTC), Andin Eswarlal Rajesh reported FPPay banner images failing to load in production. Activity continues with 25+ replies.
2.  **Staff Verification Logic:** Vivian Lim Yu Qian queried app screens for staff verification during SKU purchases requiring force verification (e.g., milk powder). The team is validating compliance against existing protocols.
3.  **Incident Management Response:** Earlier on March 27, Jazz Tong raised an urgent query regarding a potential incident ("it is incident?"). The team mobilized support for the DPD Incidents channel involving Gopalakrishna Dhulipati, Akash Gupta, and Kyle Nguyen.
4.  **Infrastructure & Operations Risk:** Nicholas Tan flagged risks regarding Broadcom ending free Bitnami images, causing `kubectl` image tag failures and increased Time To Recovery (TTR) impacting the Golden Pipeline (GP).
5.  **Payment Service Issues:** Alvin Choo reported promo code redemption failures in FP Pay; confirmed that a change freeze has ended and feature releases are proceeding.
6.  **Mobile Quality Assurance:** Andin Eswarlal Rajesh previously identified an iOS FPPay bug where QR codes load without user login, escalated via file download.
7.  **Datadog Governance:** Natalya Kosenko reported unauthorized manual changes to Datadog On-Call teams (removals of Maxine, Arijit, Minu). Terraform manages this config; manual console edits are overwritten on the next run.
8.  **Strategic Planning & Tooling:** Winson Lim highlighted data centers as potential targets in modern warfare (Iran conflict context) to inform Disaster Recovery (DR) scenarios and noted Reforge joined Miro to bridge strategy and delivery gaps.
9.  **AI Engineering Learning:** On March 30, 2026 (23:25 UTC), Winson Lim shared a GitHub repository (`affaan-m/everything-claude-code`) as a resource for learning AI-first engineering patterns and reusable skills.
10. **Security Alert (NPM):** On March 31, 2026 (04:38 UTC), Mohammad Adyatma flagged the compromise of the `axios` npm package via `https://socket.dev/blog/axios-npm-package-compromised`. Immediate review of dependencies is required.
11. **Social Events:** Kyle Nguyen announced an upcoming DPD BBQ ("We come first"). Boning He and Gopalakrishna Dhulipati shared snacks; Maou Sheng Lee expressed sentiment regarding energy waste on March 18.

**Pending Actions & Owners**
*   **FPPay Image Team (Andin Eswarlal Rajesh, DevOps):** Investigate root cause of banner image loading failures in production and deploy fix. Priority: High.
*   **S&G Verification Team (Vivian Lim Yu Qian, Product/Dev Teams):** Investigate current S&G flows against the WIP verification logic document to confirm if forced staff verification screens exist for restricted SKUs like milk powder. Reference: `https://ntuclink.atlassian.net/wiki/spaces/SE/pages/1995997683/WIP+S+G+Verification+Flow`.
*   **Incident Response Team (Jazz Tong, Akash Gupta, Gopalakrishna Dhulipati, Kyle Nguyen):** Act as support guides for the active DPD Incidents channel; monitor and resolve incoming incident queries.
*   **GP Team (Nicholas Tan / Mohit Niranwal):** Investigate Bitnami image replacement strategy to resolve TTR issues and update Golden Pipeline dependencies.
*   **iOS/Dev Team (Tiong Siong Tee):** Re-verify the previously identified iOS FPPay QR code login bypass bug status.
*   **Security Team (Mohammad Adyatma, All Devs):** Audit all projects for `axios` dependency versions to mitigate risks associated with the reported npm package compromise. Reference: `https://socket.dev/blog/axios-npm-package-compromised`.
*   **Datadog Admins:** Anyone who manually altered Datadog Teams must submit a Pull Request to `https://bitbucket.org/ntuclink/fp-datadog-eu` instead of editing the console.

**Decisions Made**
*   No formal change freeze; feature releases are currently active (Alvin Choo).
*   Datadog team configurations must strictly follow Infrastructure as Code (Terraform) protocols; manual overrides are deprecated.
*   Miro's acquisition of Reforge is recognized as a strategic move to bridge product strategy and delivery gaps.
*   **New:** Active incident support protocol established for Jazz Tong, Akash Gupta, Gopalakrishna Dhulipati, and Kyle Nguyen on March 27, 2026.
*   **New:** Winson Lim endorsed the `affaan-m/everything-claude-code` repository as a key resource for AI-first engineering patterns and skill development.

**Key Dates & Follow-ups**
*   **Mar 31, 2026 (04:38 UTC):** Mohammad Adyatma flagged `axios` npm package compromise; security audit initiated.
*   **Mar 30, 2026 (23:25 UTC):** Winson Lim shared AI engineering resource repo.
*   **Mar 30, 2026 (09:11 UTC):** Andin Eswarlal Rajesh flagged FPPay banner image loading failure in prod; discussion ongoing (25+ replies).
*   **Mar 27, 2026 (03:03 UTC):** Jazz Tong flagged potential DPD incident; support team mobilized.
*   **Mar 27, 2026 (08:11 AM):** Vivian Lim Yu Qian raised S&G verification flow query; discussion concluded with 12 replies.
*   **Mar 26, 2026:** Winson Lim shared Reforge joining Miro.
*   **Mar 25, 2026:** Natalya Kosenko highlighted DPD alumni participation in a Google AI event.
*   **Mar 18, 2026:** Maou Sheng Lee noted sentiment regarding wasted energy.

**Social Notes**
*   Upcoming DPD BBQ announced by Kyle Nguyen ("We come first, see you!").


## [29/57] DPD x Platform Engineering
Source: gchat | Group: space/AAQAcjNXKpA | Last Activity: 2026-03-31T03:55:31.648000+00:00 | Last Updated: 2026-03-31T06:52:46.592174+00:00
**Daily Work Briefing: DPD x Platform Engineering**
*(Updated with March 31 SLO Error Budget Alerts & Redis Investigation)*

**Key Participants & Roles**
*   **Kyle Nguyen:** Infrastructure/Platform Engineering (Reviewer, Incident Triage, Redis Alert Lead).
*   **Daryl Ng:** Incident Analyst / Automation query responder.
*   **Gopalakrishna Dhulipati:** Addressed in new alert chain.
*   **Sneha Parab:** Addressed in new alert chain.
*   **Alvin Choo:** Team Lead; CC'd on high-urgency Redis alert.
*   **Sampada Shukla:** Reported SLO error budget alerts on March 31.
*   **Dodla Gopi Krishna:** Owner of Fulfillment/Pricing SLOs; addressed in new alert chain.
*   *(Other roles from previous briefing remain active).*

**Main Topics & Discussions**
1.  **High-Urgency Redis CPU Spike (March 30):** Kyle Nguyen reported a critical alert at ~03:00 AM UTC regarding the Redis instance `zs-fpon-prd-catalogue-service` in `asia-southeast1`. The instance hit nearly 100% CPU usage.
    *   *Investigation Status:* Verified latency spikes originating from `go-catalogue-service`. Latency has normalized, preventing escalation to a formal incident.
    *   *Action:* Kyle requested priority investigation for March 31 with specific focus on root cause analysis (RCA) for CPU saturation.
    *   *Participants:* Alert chain included Daryl Ng, Gopalakrishna Dhulipati, Sneha Parab, and Alvin Choo.

2.  **SLO Error Budget Alerts (March 31):** Sampada Shukla reported new SLO error budget alerts on March 31 at ~03:55 AM UTC. The alert notification references two specific SLO monitors (Datadoghq EU).
    *   *Status:* Alert acknowledged by Dodla Gopi Krishna; thread currently active with 4 replies and unread messages. This confirms ongoing degradation in the Fulfillment and Pricing tribes previously noted on March 25, now requiring immediate attention due to error budget consumption.

3.  **Historical Context (Retained):**
    *   *Critical Picking App & Backoffice Incident (March 23):* `SocketTimeoutExceptions` caused by GKE cluster (`jarvis-prod-ap-v2`) hard memory limits triggering forced pod evictions. Root cause identified as memory exhaustion between 15:22–15:39 SGT.
    *   *SLO Performance Degradation (March 25):* Dodla Gopi Krishna notified of initial error budget depletion in Fulfillment and Pricing tribes.
    *   *On-Call Restructuring & Security:* Debate continues on shifting on-call configuration from Terraform to Datadog UI (Akash Gupta proposal). Lester Soriano encountered `golangci-lint` version mismatch during vulnerability patching for `lt-strudel-api-go`.

**Pending Actions & Owners**
*   **Investigate Redis CPU Saturation:** Prioritize RCA for `zs-fpon-prd-catalogue-service` hitting 100% CPU. *(Owners: Daryl Ng, Gopalakrishna Dhulipati, Sneha Parab)*
*   **Address SLO Error Budget Alerts:** Resolve the current alert status and prevent further budget depletion for the two affected SLOs reported by Sampada Shukla. *(Owner: Dodla Gopi Krishna, relevant service owners)*
*   **Resolve Cluster Capacity Scaling:** Investigate why the cluster failed to scale out during peak traffic (March 23) and implement fixes for memory limits. *(Owners: Kyle Nguyen, Nicholas Tan)*
*   **Evaluate On-Call Tooling Strategy:** Assess Akash Gupta's proposal to use Datadog UI instead of Terraform for new on-call teams. *(Owner: Platform Engineering)*
*   **Restore Bastion Access:** Investigate PROD `asia-southeast1-c` Bastion inaccessibility. *(Owners: Nicholas Tan, Kyle Nguyen, Harry Akbar Ali Munir)*
*   **Review Infrastructure & Monitoring PRs:** Natalya Kosenko's PR `infra-gcp-fpg-titan/344` and Akash Gupta's PR #917 require reviews.
*   **Resolve Go Pipeline Error:** Reconcile `golangci-lint` version mismatch for Lester Soriano.

**Decisions Made**
*   *Tentative:* The team is debating whether to retain the Terraform-based change-freeze process or adopt direct Datadog UI management for on-call teams. No final decision recorded yet.
*   **QC Food Status:** Disabling confirmed on production (as of March 19). Resource scale-down planning initiated pending ES confirmation.

**Key Dates & Follow-ups**
*   **March 31, ~03:55 AM UTC:** Sampada Shukla reported SLO error budget alerts referencing two monitors; Dodla Gopi Krishna acknowledged.
*   **March 30, ~03:00 AM UTC:** High-urgency alert triggered for Redis instance `zs-fpon-prd-catalogue-service` CPU usage.
*   **March 25, 03:15 AM UTC:** Initial Fulfillment SLO degradation alert.
*   **March 23, 03:40–03:45 PM SGT:** Critical incident involving GKE memory exhaustion and pod evictions.


## [30/57] Web Chapter
Source: gchat | Group: space/AAAASzhKzV0 | Last Activity: 2026-03-31T03:21:06.049000+00:00 | Last Updated: 2026-03-31T06:53:43.559885+00:00
**Daily Work Briefing: Web Chapter (Updated)**

**Key Participants & Roles**
*   **Wai Ching Chan**: Reporter/Initiator.
*   **Madhuri Nalamothu**: Tagged assignee for investigation.
*   **Milind Badame**: Tagged assignee for investigation.
*   **Varun Chauhan**: Departing member (7-year tenure).

**Main Topic**
1.  **Technical Escalation**: Investigation into persistent failures of the **backoffice E2E TestSigma UAT**. Wai Ching Chan reported repeated execution failures requiring immediate review.
2.  **Team Transition**: Varun Chauhan announced his departure from Fairprice Group, marking his last day on March 31, 2026, after seven years of service.

**Pending Actions & Ownership**
*   **Action**: Investigate root cause of failing backoffice E2E tests in TestSigma UAT and resolve pipeline issues.
    *   **Owner**: Madhuri Nalamothu, Milind Badame.
    *   **Context**: The reporter has attempted runs multiple times without success. Varun's departure does not alter this immediate technical requirement; the team must proceed with the investigation to ensure sprint stability.

**Decisions Made**
*   No technical decisions were recorded regarding the test failures.
*   Acknowledgment of Varun Chauhan's exit and transition plan initiated via social connection (LinkedIn).

**Key Dates & Follow-ups**
*   **Issue Log**: March 30, 2026, at 02:15 UTC (Chat message sent by Wai Ching Chan).
*   **Departure Announcement**: March 31, 2026, at 03:21 UTC.
*   **Reference Links**:
    *   Pipeline Failure Log: `https://bitbucket.org/ntuclink/platform-admin/pipelines/results/13756/steps/{27e77363-8855-4cb3-84d2-1a4f33b6ae00}`
    *   TestSigma Run Details: `https://app.testsigma.com/ui/td/runs/247783`
    *   Varun Chauhan LinkedIn: `https://www.linkedin.com/in/varunc1/`
*   **Space URL**: `https://chat.google.com/space/AAAASzhKzV0`

**Summary**
On March 30, 2026, Wai Ching Chan flagged a critical stability issue with the backoffice E2E TestSigma UAT environment, citing repeated failures across multiple execution attempts. Madhuri Nalamothu and Milind Badame were assigned to analyze the specific Bitbucket pipeline logs and TestSigma run data provided to restore test stability immediately following sprint deadlines.

On March 31, 2026, Varun Chauhan announced his final day with Fairprice Group after a seven-year tenure. In a departure message received by the Web Chapter, Varun expressed gratitude for the collaborative environment and the accomplishments achieved over the past week. He shared his LinkedIn profile (`https://www.linkedin.com/in/varunc1/`) to maintain connections and encouraged the team regarding upcoming sprints. While Varun is no longer active in the group, his legacy of seven years remains part of the chapter's history. The technical investigation into the E2E test failures remains the primary operational priority for the remaining team members.


## [31/57] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/e4zfXRT2Pnk | Last Activity: 2026-03-31T02:35:25.919000+00:00 | Last Updated: 2026-03-31T06:54:12.501178+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Initiator of production testing; managing test data, UAT sheets, and confirming store selection.
*   **Sneha Parab:** Inventory/Store specialist; coordinating SKU enablement, Ops alignment, and defining return workflows.
*   **Andin Eswarlal Rajesh:** Tester; verifying platform compatibility (OG vs. Scango), identifying low-peak windows, and monitoring indexer status.
*   **Daryl Ng:** Advisor on system availability; confirmed 24-hour S&G (Store & Global) coverage.
*   **Wai Ching Chan:** Advisor on risks regarding shut-down stores during production testing.

**Main Topic**
Finalizing the execution plan for BCRS production testing, specifically confirming store selection, defining non-peak testing windows, and resolving technical blockers (SKU indexing and 404 errors).

**Decisions Made & Technical Clarifications**
*   **Store Selection:** Prajney confirmed **Parkway Parade** as the selected location for production testing. **Daryl Ng** clarified that **Yew Tee** is a viable alternative specifically for testing S&G (Scango) at midnight due to 24-hour operational coverage.
*   **Indexing Behavior:** Sneha clarified that enabling a SKU mid-run may cause it to be skipped in the current cycle, though appearance on the Product Listing Page (PLP) is not guaranteed. The indexer runs hourly at the 30th minute (excluding 2:30 AM and 3:30 AM). If a test starts at 12:00 AM, the last window to revert changes is **1:30 AM**.
*   **System Status:** Andin reported system downtime around 02:30 AM on March 31. Daryl Ng confirmed the system status and availability windows.

**Decisions Made (Existing & Updated)**
*   **Data Migration:** Prajney moved the "Firefighting BCRS" list to the **"BCRS UAT 2026"** spreadsheet; this remains the source of truth.
*   **Testing Scope:** Only specific SKUs created during the smoke test are currently available for production testing.
*   **Target Date Strategy:** Sneha proposed postponing full testing to **April 1** if compliance risks are too high, but the team is now pivoting to an immediate window on **March 31**.

**Pending Actions & Owners**
*   **Low-Peak Hour Identification:** Prajney requested clarification on exact non-peak hours. The previous proposal of a late-night window (10:30 PM) is secondary to defining daytime availability for dual OG/Scango testing, or utilizing Yew Tee for midnight S&G tests per Daryl Ng's input.
*   **System Verification:** Andin flagged a system issue at 02:30 AM; Daryl Ng has confirmed system status and S&G coverage windows.
*   **Return Process Definition:** Sneha must clarify how returns will be handled during the chosen testing window (late-night vs. daytime).
*   **SKU Enablement:** SKUs must be enabled both **in-store and globally** to resolve 404 errors. Sneha to coordinate with Operations to finalize this setup.
*   **Whitelist Request:** Prajney (`prajney.sribhashyam@fairpricegroup.sg`) requested whitelisting while business users collect production IDs.

**Key Dates & Deadlines**
*   **March 30, 2026:** Date of conversation and spreadsheet updates.
    *   Prajney confirmed **Parkway Parade** as the test site at 11:01 PM.
    *   Sneha joined an urgent meeting at 06:25.
*   **March 31, 2026 (Active):** 
    *   System downtime noted around 02:30 AM.
    *   Daryl Ng confirmed 24-hour S&G availability and suggested Yew Tee for midnight testing.
    *   Pending confirmation of low-peak hours for testing.
*   **April 1, 2026:** Backup date for full production testing if immediate execution on March 31 is deemed too risky.

**Technical Issues Noted**
*   **404 Errors:** Caused by SKUs not being enabled globally and in-store.
*   **System Stability:** Intermittent outages reported early morning (March 31); Daryl Ng confirmed S&G coverage is available 24 hours.
*   **Store Configuration:** Risks remain regarding using live stores for testing; no dummy postal codes exist to mitigate the risk of real customer orders.


## [32/57] [D&T] Discussion service account key decommission
Source: gchat | Group: space/AAQAHH3dAYc | Last Activity: 2026-03-31T02:32:57.666000+00:00 | Last Updated: 2026-03-31T06:54:37.155573+00:00
**Daily Work Briefing: [D&T] Service Account Key Decommission**

**Key Participants & Roles**
*   **Himal Hewagamage:** Project Lead/Owner. Confirmed key status, workflow, and Confluence resource availability; clarified Infra team ownership of rotation execution.
*   **Nicholas Tan:** D&T representative. Initially queried formal runbooks and proposed developer-led onboarding for DPD accounts before accepting Infra team management.
*   **Michael Bui:** Stakeholder seeking clarification on security compliance and prioritization (PRD/UAT).
*   **Kyle Nguyen:** Infrastructure team lead; maintains oversight while conducting independent reviews for Infra projects.
*   **Mohit Niranwal:** Provided specific security standards regarding key age and quantity.

**Main Topic**
A security hardening initiative to decommission duplicate, unused, or manually rotated GCP service account keys and migrate active accounts to an automated rotation policy. The scope covers the D&T domain (excluding defunct "dpd"). Focus includes clarifying the operational workflow: Infra will generate fresh JSON keys alongside existing ones, share via G Suite groups, and automate the removal of old keys upon confirmation.

**Pending Actions & Ownership**
*   **Runbook Distribution:** Himal Hewagamage to share the Confluence page containing formal rotation steps with Nicholas Tan.
    *   *Owner:* Himal Hewagamage.
*   **Service Account Onboarding:** Application teams (specifically D&T/DPD) are to request fresh key generation from Infra rather than managing it independently. Teams must provide G Suite group names for accounts using old keys.
    *   *Owner:* Nicholas Tan (coordination); Himal Hewagamage / Infra Team (Execution).
*   **Unused Account Identification:** Nicholas Tan and the D&T team must identify any unused service accounts to trigger immediate offboarding from automation and decommissioning.
    *   *Owner:* Nicholas Tan / Application Leads.
*   **Recurring Alignment:** Meetings scheduled every 4th week on Mondays.
    *   *Owner:* Himal Hewagamage.

**Decisions Made & Standards**
*   **Execution Ownership:** The Infrastructure team, not application developers, will manage the rotation workflow (provisioning new keys and deleting old ones) to ensure consistency across teams.
*   **Rotation Workflow Logic:**
    1.  Team confirms readiness.
    2.  Infra generates a fresh JSON key alongside the existing one.
    3.  New key is shared via the G Suite group.
    4.  Old keys are deleted from automation once confirmed.
*   **Unused Accounts:** Any identified unused SAs will be immediately offboarded and decommissioned.
*   **Defunct Services:** "dpd" remains confirmed as defunct and excluded from active usage, though the team requested fresh key provisioning for DPD accounts pending further clarification on their status.
*   **Security Standard:** Keys must not exceed 90 days old; ideally, only one active key per SA should exist within the automated rotation policy.

**Key Dates & References**
*   **Initiation Date:** March 16, 2026.
*   **Recent Discussion (New):** March 31, 2026, between 02:14 and 02:32 UTC.
    *   *Specific Update:* Confirmation that Infra will handle key generation; Himal to share Confluence runbook with Nicholas Tan.
*   **Primary Resource:** [GCP][Security] Service Account Key Rotation & Decommission Spreadsheet.
    *   URL: https://docs.google.com/spreadsheets/d/1mGBCTRQDcTs0z_w0LjVtywDCtFHZhZfWYIRGqcNglpQ/edit?gid=0#gid=0

**Next Steps**
Himal Hewagamage will provide the Confluence runbook to Nicholas Tan. The D&T team (led by Nicholas) will coordinate with developers to identify unused accounts and request new keys for active DPD accounts, acknowledging that Infra will execute the actual key generation and rotation. No further data is required from the Infra side beyond the standard onboarding process.


## [33/57] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4 | Last Activity: 2026-03-31T02:30:38.002000+00:00 | Last Updated: 2026-03-31T02:37:56.703503+00:00
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


## [34/57] @ecom-ops #standup - Mar 31
Source: gchat | Group: space/AAQA87ehICk | Last Activity: 2026-03-31T02:18:52.052000+00:00 | Last Updated: 2026-03-31T02:40:46.590921+00:00
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


## [35/57] Backend Chapter
Source: gchat | Group: space/AAAAHhDyHI4 | Last Activity: 2026-03-31T02:14:10.738000+00:00 | Last Updated: 2026-03-31T02:41:58.893653+00:00
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


## [36/57] @omni-ops #standup - Mar 31
Source: gchat | Group: space/AAQASmCjPX8 | Last Activity: 2026-03-31T02:06:29.467000+00:00 | Last Updated: 2026-03-31T02:43:21.927493+00:00
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


## [37/57] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/kc66iXHBUHA | Last Activity: 2026-03-31T01:49:00.428000+00:00 | Last Updated: 2026-03-31T02:44:29.834856+00:00
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


## [38/57] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Last Activity: 2026-03-31T01:44:43.295000+00:00 | Last Updated: 2026-03-31T02:47:04.013249+00:00
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


## [39/57] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Last Activity: 2026-03-31T00:03:09.218000+00:00 | Last Updated: 2026-03-31T02:49:12.843842+00:00
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


## [40/57] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Last Activity: 2026-03-30T23:07:07.982000+00:00 | Last Updated: 2026-03-31T02:50:15.582994+00:00
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


## [41/57] Digital Product Development {DPD}
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


## [42/57] BCRS Firefighting Group
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


## [43/57] BCRS Firefighting Group
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


## [44/57] PDM Notification
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


## [45/57] [Internal] (Ecom/Omni) Digital Product Development
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


## [46/57] [Leads] (Ecom/Omni) Digital Product Development
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


## [47/57] ❗ Important Email
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


## [48/57] @omni-ops #standup - Mar 30
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


## [49/57] Project Light Attack and Defence Leads
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


## [50/57] [Internal] (Ecom/Omni) Digital Product Development
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


## [51/57] DPD x DPM
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


## [52/57] Omni Fairmily
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


## [53/57] @ecom-ops #standup - Mar 30
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


## [54/57] Alvin Choo
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


## [55/57] RMN Incidents
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


## [56/57] DPD AI Guild
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


## [57/57] BCRS Firefighting Group
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
