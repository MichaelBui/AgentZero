

## [1/38] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Messages: 3 | Last Activity: 2026-04-03T14:28:22.574000+00:00 | Last Updated: 2026-04-03T14:33:30.777846+00:00
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
2.  **Mar 18/19:** `10aaf170...` (~5.6h). Status: **Resolved**.
3.  **Mar 20, 2026:** `2787bcd7...` (~4.4h). Status: **Resolved**.
4.  **Mar 22, 2026:** `08f5624a...` (~3.4h). Status: **Resolved**.
5.  **Mar 24–25, 2026:** `de0cbb14...` (~3h 51m). Status: **Resolved**.
6.  **Mar 25, 2026:** `978f6328...`. Recovered 12:09 UTC (~24h). Status: **Resolved**.
7.  **Mar 26, 2026:** `7b73b037...` (~3h 22m). Status: **Resolved**.
8.  **Mar 27, 2026:** `f5d0894a...`. Recovered 17:37 UTC. Status: **Resolved**.
9.  **Mar 28–30, 2026:** Multiple P3 incidents recovered (Keys: `8874d9ed...`, `784f6ec6...`, `acd815df...`).
10. **Mar 31, 2026:** Incident `0404fba2...` triggered at 11:49 UTC and resolved at 15:05 UTC (~3h 16m). Status: **Resolved**.

**Recent Sequence Update (Apr 1–2):**
*   **Apr 1, 2026:** Three incidents (`c6d476e4...`, `f28ed3be...`, `ba9617bc...`) triggered and recovered within ~1h 19m to 3h 26m. All Status: **[P3] Recovered**.
*   **Apr 2, 2026:** Incident `fa62ae68...` triggered at 06:58:23 UTC and recovered at 10:52:23 UTC (~3h 54m). Status: **[P3] Recovered**.

**Current Active Incident (New):**
*   **Trigger Time:** Apr 3, 2026 at 14:28:22 UTC.
*   **Story Key:** `21a5a729-dfbb-5206-a97e-047fe5903e51`.
*   **Monitor Query:** `events("source:watchdog (story_category:infrastructure -story_type:(tcp_retrans_jump OR full_disk_forecast)) env:(PROD OR production OR prod)").rollup("count").by("story_key").last("30m") > 0`.
*   **Current Status:** **[P3] Triggered**.

### Pending Actions & Ownership
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Action Required:** No manual intervention required at this time. The incident is currently active with no duration data yet available for comparison against the established transient pattern (~3 hours). Continue standard surveillance.

### Decisions Made
*   **Escalation Status:** Pending; no escalation triggered as the incident just triggered on Apr 3, 2026.
*   **Protocol:** Maintain monitoring of `story_key:21a5a729-dfbb-5206-a97e-047fe5903e51`. If resolution does not occur within the typical 6-hour window, review for potential process anomalies.

### Key Dates & Follow-ups
*   **Latest Event:** Triggered Apr 3, 2026 at 14:28:22 UTC.
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Monitor for recovery notification in the `@hangouts-dd-dpd-watchdog-alert` channel.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Datadog Monitor Link:** [View in Datadog](https://app.datadoghq.eu/monitors/17447511?group=story_key%3A21a5a729-dfbb-5206-a97e-047fe5903e51&from_ts=1775225511000&to_ts=1775226711000&event_id=8572547283262036621)
*   **Recovery Log:** Pending (Current event `story_key:21a5a729-dfbb-5206-a97e-047fe5903e51`).


## [2/38] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 16 | Last Activity: 2026-04-03T14:28:00.570000+00:00 | Last Updated: 2026-04-03T14:34:06.983151+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (Updated April 3, ~14:28 UTC)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
Cyclical instability continues from the April 1 onset into the early afternoon of April 3 (09:53–14:28 UTC). While some latency spikes in Identity services have recovered, high error rates persist across Identity (`engage-my-persona-api-go`) and Gamification (`engage-gamification-api`). Orchid success rates show intermittent drops. The overall incident remains active with recurring failures affecting multiple squads.

**Status Summary & Timeline (Updated: ~14:28 UTC)**
*   **Identity API Instability (`squad:dynamics`):**
    *   *Latency:* P90 latency spikes (>1.8s) on `post_/new-myinfo/confirm` triggered at 13:42 UTC (Value: 1.802s), recovering by 14:45 UTC (Value: 1.15s).
    *   *Error Rate:* High error rates (>0.1%) triggered repeatedly throughout the afternoon, specifically at **13:41 UTC** (0.094), **14:01 UTC** (0.105), and **14:19 UTC** (0.100). Latest recovery recorded at 14:28 UTC (Value: 0.096).
*   **Gamification API (`squad:dynamics`):**
    *   *Error Rate:* Significant spike triggered at **14:12 UTC** with a value of **0.345**, the highest recorded in this session, before recovering at 14:22 UTC.
*   **Recommendation & Frontend Services (`squad:journey`):**
    *   *Orchid Failures:* Success rate dips (<99.9%) triggered at **14:16 UTC** (Value: 99.881%), recovering by 14:20 UTC (Value: 99.935%).
*   **Scratch Card Claim:** No new triggers reported in `lyt-p13n-layout` since the morning session; stability remains a monitoring focus.

**Pending Actions & Ownership**
*   **Investigate Identity Service Fluctuations:** Continue analyzing recurring high error rates (~0.1%) and intermittent latency spikes on `engage-my-persona-api-go`. Owner: **Squad Dynamics**.
*   **Monitor Gamification API Spike:** Investigate the severe error rate spike (0.345) at 14:12 UTC for root cause analysis. Owner: **Squad Dynamics**.
*   **Track Orchid Stability:** Monitor cyclical success rate dips in `frontend-gateway` (Orchid). Owner: **Squad Journey**.

**Decisions Made**
*   **Status Update:** Incident severity remains Critical due to continuous, cyclical failures extending from April 1 through the current afternoon window. The Gamification API error rate spike at 14:12 UTC represents a significant degradation compared to earlier metrics.
*   **Pattern Confirmation:** Recurrence of high error rates in Identity and Gamification APIs, coupled with intermittent success rate drops in Orchid, confirms systemic instability affecting multiple squads simultaneously.

**Key Dates & Follow-ups**
*   **Active Window:** April 1, 09:58 – April 3, 14:28 UTC (Latest Activity).
*   **Reference Links (Latest):**
    *   `gamification-api` Error Rate Monitor #92939290 (Triggered: 14:12 UTC, Value: 0.345)
    *   `engage-my-persona-api-go` Latency Monitor #50879027 (Triggered: 13:42 UTC, Value: 1.802s)
    *   `frontend-gateway` (Orchid) Success Rate Monitor #17448311 (Latest Trigger: 14:16 UTC)


## [3/38] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Messages: 16 | Last Activity: 2026-04-03T12:47:14.708000+00:00 | Last Updated: 2026-04-03T14:34:45.574576+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Apr 3, 12:47 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`.
*   **Escalations:** `@oncall-dpd-staff-excellence-pdm`, `@hangouts-GT-Search-DatadogAlerts`, `@hangouts-GT-Discovery-DatadogAlerts`, `@opsgenie-dpd-grocery-discovery`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Retail Media.

**Main Topic**
**P2 INCIDENT (RESOLVED):** Intermittent high error rate in `marketing-service` and transient Sanity Check failures in `fp-search-indexer`.
*   **Current Status:** All alerts resolved as of 12:47 UTC. The active P2 alert for `marketing-service` is stable; the Search Indexer sanity check has recovered. No open incidents remain.

**Resolved Incidents (Apr 3)**
*   **Alert:** **P2 High Error Rate (`marketing-service`)** [Status: RECOVERED]
    *   *Timeline & Metrics:*
        *   Triggered 07:29 UTC (Peak: 1.6%); Recovered 07:39 UTC.
        *   Triggered 11:25 UTC (Value: 0.021); Recovered 11:35 UTC.
        *   Triggered 12:18 UTC (Value: 0.01); Recovered 12:28 UTC.
        *   Triggered 12:29 UTC (Value: 0.012); Recovered 12:39 UTC.
    *   *Detail:* Error rate exceeded threshold of 5% on multiple occasions within a short window. All instances resolved automatically with metric dropping to 0.0%.
*   **Alert:** **P2 Sanity Check Failure (`fp-search-indexer`)** [Status: RECOVERED]
    *   *Timeline:* Triggered 11:47 UTC; Recovered 12:47 UTC (Duration: ~60 mins).
    *   *Detail:* Log query `logs("env:prod service:fp-search-indexer 'failed sanity checks'")` detected events > 0 in the last 1h. Resolved when event count dropped to 0.

**Resolved Incidents (Apr 2)**
*   **`fpon-catalogue-job-sku-global-attribute` (Error Rate):** P3 anomaly triggered at 20:02 UTC; recovered at 20:19 UTC. [Status: Resolved]
*   **`go-catalogue-service` (Latency):** P3 anomaly triggered at 03:24 UTC; recovered at 03:33 UTC. [Status: Resolved]
*   **`marketing-service` (Throughput):** P4 anomaly triggered at 01:29 UTC; recovered at 02:21 UTC. [Status: Resolved]
*   **`sku-store-attribute` (Low Files):** P3 anomaly triggered Apr 2 at 22:05 UTC; recovered Apr 3 at 01:05 UTC. [Status: Resolved]

**Decisions Made**
*   The `marketing-service` high error rate on Apr 3 exhibited a pattern of transient spikes (multiple triggers between 07:29 and 12:39) but recovered automatically without manual intervention each time.
*   The `fp-search-indexer` sanity check failure was self-correcting within one hour.
*   No further immediate action is required for `marketing-service` or `fp-search-indexer`; monitoring confirms stabilization.

**Key Dates & Follow-ups (Apr 2–3, 2026)**
*   **P2 (Resolved):** `marketing-service` high error rate (Multiple triggers: 07:29, 11:25, 12:18, 12:29 UTC; all recovered).
*   **P2 (Resolved):** `fp-search-indexer` sanity check failure (Triggered 11:47 UTC; Recovered 12:47 UTC).
*   **P3/P4:** Historical transient anomalies from Apr 2 remain resolved.

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c
*   **Monitor (`marketing-service` High Error Rate):** https://app.datadoghq.eu/monitors/17447106
*   **Monitor (`fp-search-indexer` Sanity Checks):** https://app.datadoghq.eu/monitors/21866653
*   **APM Resource:** https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod
*   **K8s Deployment:** https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview
*   **Runbook:** https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book


## [4/38] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-04-03T12:26:58.224000+00:00 | Last Updated: 2026-04-03T14:35:24.605293+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Update)**
**Date:** April 3, 2026 (Mid-Morning Shift)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 968

### Main Topic
System instability persists on April 3rd. Following an SLO breach at 04:21 UTC and cyclic degradation in the late morning, **Checkout** and **S&G Cart** success rates dropped below thresholds between 11:00 and 12:26 UTC. While some metrics recovered to baseline by 12:26 UTC, the incident scope has expanded from latency spikes to include transactional reliability issues in Checkout and S&G post-cart operations.

### Incident Timeline & Actions
**Historical Context:**
*   *Extended activity from March 20 through late March 31.*
*   *April 2 (04:55 – 06:26 UTC):* Critical burst affecting Cart/Checkout; recovered by 06:26 UTC.

**Latest Activity (Apr 3 Early Morning)**
*   **00:05 – 00:09 UTC:** Guest Shopping List P90 spiked to 2.242s.
*   **00:48 – 00:57 UTC:** Wish List writes P99 reached 6.135s.
*   **04:21 UTC:** **[Critical]** Error Budget Alert triggered on `slo_pricing_cart_get_wish_list_id`. 70.182% of 7-day budget consumed.
*   **04:57 – 05:06 UTC:** Wish List writes P99 spiked again to 7.862s.

**New Activity (Apr 3 Late Morning & Noon)**
*   **06:57 – 07:38 UTC:** Cyclic degradation on `put /api/product/{_id}/wish-list` (Monitor ID 21245701). Peak P99: 6.945s.
*   **08:08 – 08:23 UTC:** Continued cyclic instability on Wish List writes (P99 triggered at 6.231s).
*   **08:16 – 08:18 UTC:** P90 degradation on `put /api/product/{_id}/wish-list` (Monitor ID 21245706); value reached 5.336s.
*   **09:43 – 09:45 UTC:** P90 degradation on `get /api/wish-list/{_id}` (Monitor ID 21245720); value reached 1.831s.

**New Alerts & Recoveries (Apr 3 Mid-Day)**
*   **11:03 – 11:13 UTC:** **[New]** Checkout success rate dropped below 99.9% (Value: 99.886%). Triggered Monitor ID `21245708` (`post /api/checkout`). Recovered at 11:13 UTC.
*   **12:07 – 12:18 UTC:** **[New]** Wish List write P90 degraded again (Value: 5.015s). Triggered Monitor ID `21245706`. Recovered at 12:18 UTC.
*   **12:16 – 12:26 UTC:** **[New]** S&G Cart success rate dropped below 99.9% (Value: 99.885%). Triggered Monitor ID `22710472` (`post /cart`). Recovered at 12:26 UTC with 100.0% success.

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** The incident scope has widened to include Checkout (`post /api/checkout`) and S&G Cart (`post /cart`) reliability, in addition to Wish List latency. While mid-morning success rate issues have temporarily recovered, the recurrence of P90 write degradation at 12:07 UTC indicates persistent systemic volatility.
*   **Immediate Action Required:**
    *   Investigate the correlation between the earlier checkout/S&G success drops (11:03 & 12:16) and the ongoing Wish List latency patterns.
    *   Monitor `post /api/checkout` and `post /cart` closely for re-occurrence of <99.9% success rates.
    *   Continue prioritizing stabilization of `put /api/product/{_id}/wish-list` (Monitor 21245706) despite the recent recovery at 12:18 UTC.

### Decisions Made
*   **Priority Status:** Maintained at **"Critical Incident"**. The emergence of success rate failures in Checkout and S&G Cart, alongside cyclic latency, confirms a broad systemic issue rather than isolated network noise.
*   **Focus Shift:** Triage now explicitly targets the **transactional reliability** (Checkout/S&G) and **write performance** (Wish List P90/P99) across the full shift.
*   **Metric Update (Session Peak):**
    *   `post /api/checkout` Success Rate Low: **99.886%** (11:03 UTC).
    *   `put /api/product/{_id}/wish-list` P90 High: **5.015s** (12:07 UTC).

### References
*   **Active Monitors:** `21245708` (Checkout Success Rate), `22710472` (S&G Cart Success Rate), `21245706` (Wish List Write P90 - *Recurring*), `21245701` (Wish List Write P99).
*   **Service Tags:** `service:frontend-gateway`, `service:st-cart-prod`, `team:dpd-pricing`.


## [5/38] QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs | Last Activity: 2026-04-03T09:49:31.896000+00:00 | Last Updated: 2026-04-03T10:34:26.752010+00:00
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
1.  **LEAP Pipeline Error (Critical/New):** On **2026-04-03**, Patrick Thun reported a `sonar cloud` code analysis failure in the LEAP pipeline affecting `*_test.go` files. *Status:* Active request for assistance; awaiting resolution from DevOps/Dev team.
2.  **DC Membership Subscription & Enrollment (Critical/Escalated):** On **2026-04-02**, Milind Badame confirmed regression failures in DC membership tests (enrollment, promote/demote) due to "Unable to Process Payment" and backend blockage. *Status:* Escalated; awaiting investigation from @Daryl Ng and @Andin Eswarlal Rajesh.
3.  **iOS SnG Flow List Update Bug:** On **2026-04-02**, Madhuri Nalamothu reported that item additions to "My List" via PDP do not update the count on iOS. *Status:* Video evidence shared; discussion ongoing with @Piraba Nagkeeran and @Andin Eswarlal Rajesh.
4.  **iOS Express Delivery UI Issue:** On **2026-04-02**, Madhuri Nalamothu observed clear display issues with "Add to Cart" text on iOS PLP for specific products (e.g., Milo Chocolate Malt). *Status:* Notified @Piraba Nagkeeran.
5.  **BackOffice Domain Validation Gap:** On **2026-04-01**, Milind Badame identified that BackOffice accepts full invalid domains. *Status:* Awaiting investigation from @Daryl Ng.
6.  **Tile Customization - PreOrder:** On **2026-04-01**, Milind Badame inquired about enabling "PreOrder" functionality on tiles. *Status:* Pending response from @Daryl Ng.
7.  **Express Delivery Service Fee Logic:** On **1 Apr**, Milind Badame reported fees are not waived when amounts exceed $30. *Status:* Awaiting investigation by @Daryl Ng.
8.  **Unlimited Product API Error:** On **1 Apr**, Milind Badame queried behavior for increasing counts of unlimited products in BackOffice. *Status:* Under review with @Wai Ching Chan and @Andin Eswarlal Rajesh.
9.  **JWC & Express Delivery Timeouts:** On **1 Apr**, Milind Badame flagged E2E failures due to store timings; requested 24x7 configuration in UAT. *Status:* Pending advice from @Andin Eswarlal Rajesh and @Daryl Ng.
10. **Pipeline Error (Historical):** On **31 Mar**, Hang Chawin Tan reported a failure in `dp-gifting-web`. *Status:* Previously active discussion involving @Madhuri Nalamothu, @Milind Badame, and @Oktavianer Diharja awaiting resolution.
11. **BCRS Swimlane Management:** On **31 Mar**, Milind Badame queried disabling swimlanes post-UAT. *Status:* Discussion ongoing with @Daryl Ng and @Andin Eswarlal Rajesh.
12. **System-Wide Intermittent Failures:** On **30 Mar**, Milind Badame reported HTTP 500 errors affecting order placement, cart, and PDP pages. *Status:* Active investigation for backend instability vs. testing impact.
13. **Order Placement Failure ('Strong Tasty Brew'):** On **30 Mar**, Madhuri Nalamothu reported inability to place orders for non-FP product 'Strong Tasty Brew'. Discussion ongoing with @Piraba Nagkeeran.
14. **MiniGames Blank Screen:** On **30 Mar**, Milind Badame reported a blank white screen on MiniGames tile tap (guest login) on lower Android versions. *Owner:* @Aman Saxena, Mobile Team.
15. **LinkPoints Regression Failure:** Reported on **27 Mar** regarding CLS Award Balance API `500` errors. Status remains Critical/Blocked pending resolution with @Pandi.

**Pending Actions & Ownership**
*   **LEAP Pipeline Resolution:** Resolve SonarCloud analysis failure in `*_test.go`. *Owners:* @Patrick Thun (Reporter), DevOps/Dev Team. **(Highest Priority)**
*   **DC Membership Payment Fix:** Resolve "Unable to Process Payment" errors blocking new enrollments and promote/demote tests. *Owners:* @Daryl Ng, @Andin Eswarlal Rajesh.
*   **iOS SnG List Update Fix:** Investigate count update failure in iOS PDP My List flow. *Owners:* @Piraba Nagkeeran, @Andin Eswarlal Rajesh.
*   **BackOffice Validation Fix:** Investigate and prevent invalid domain entries in BackOffice. *Owner:* @Daryl Ng.

**Decisions Made**
*   DC Membership payment failures are confirmed as a regression blocking new user enrollment and require immediate escalation to Dev.
*   iOS SnG flow "My List" count update failure is validated via video; mobile team engagement initiated.
*   System-wide errors on 30 Mar require immediate triage; potential testing activity suspected but not yet confirmed as root cause.

**Key Dates & Deadlines**
*   **2026-04-03 09:49:** LEAP pipeline SonarCloud error reported by @Patrick Thun.
*   **2026-04-02 06:15:** iOS Express Delivery UI issue reported by @Madhuri Nalamothu.
*   **2026-04-02 03:09:** iOS SnG "My List" update bug reported; video shared.
*   **2026-04-02 04:48 - 05:13:** Escalation regarding DC membership payment failures and backend enrollment blockage.


## [6/38] [Prod Support] Ecom FFS Ops
Source: gchat | Group: space/AAAAde_cYKA | Last Activity: 2026-04-03T08:16:40.717000+00:00 | Last Updated: 2026-04-03T10:35:39.118240+00:00
**Daily Work Briefing: [Prod Support] Ecom FFS Ops (Updated Apr 3)**

**Key Participants & Roles**
*   **Wai Ching Chan / Sampada Shukla:** Operations/Product Leads.
*   **Tok Hong Siang:** TL - TSENGFFS.
*   **Adrian Yap Chye Soon:** Technical Lead/Support.
*   **Akash Gupta:** DPD / Fulfilment / On Call.
*   *(New Inquiry):* **TL HPWP FFS** (Invoked for Order #23032024).

**Main Topics**
1.  **Packlist & SOH Discrepancies (Expanded):** Ongoing investigation into critical `packed_qty` anomalies and Stock on Hand (SOH) NULL values across multiple sites.
    *   **New Critical Incident (Apr 3, ~08:16 AM):** Wai Ching Chan flagged a discrepancy at **Hyper Parkway (Store ID 186)**. Order #23032024 shows `packed_qty` of **10,932,725** vs. `delivered_qty` of **3**.
        *   *Data Context:* Preferred date Apr 3; SKU details indicate significant price impact (MRP null, Price Impact 23.4).
    *   **Resolution Update:** Tok Hong Siang confirmed the previous Tai Seng (Store ID 231) discrepancy (Order #23009418: `packed_qty` 369,076 vs. `delivered_qty` 2) was due to Out of Stock (OOS) and drop-off on Apr 3 at 04:26 AM.
    *   **Ongoing Critical Incidents:**
        *   **Hyper Changi (Store ID 45) - Apr 2:** Order #23013763 shows Packlist status `RECEIVED` but `packed_quantity` is `NULL`.
        *   **Hyper Changi (Store ID 45) - Mar 29:** Order #22972590 showed `packed_qty` of 90,203,969 vs. `delivered_qty` of 2.

2.  **Dispatcher App & Zone Scanning Failure (Mar 28):** Escalation regarding the dispatcher app's inability to scan new zones at **hvivo**.
    *   **Status:** Reported 01:45 AM Mar 28; Adrian Yap Chye Soon provided video evidence for review; technical investigation remains active.

3.  **HCBP Picking Queue Issues (Mar 27):** Escalated urgency regarding "No picking Q" blockage and T18 display failures.
    *   **Status:** Initial blockage reported 02:08 AM; escalated by Ler Whye Ling Angel at 02:52 AM; T18 data failure reported by TL HCBP FFS at 07:47 AM.

**Pending Actions & Ownership**
*   **Data Validation (Urgent - Apr 3):**
    *   *@TL HPWP FFS:* Immediate investigation into Order #23032024 (Hyper Parkway) where `packed_qty` exceeds `delivered_qty`.
    *   *@Adrian Yap Chye Soon:* Immediate investigation into Order #23013763 (Hyper Changi) where Packlist status is `RECEIVED` but `packed_quantity` is `NULL`.
    *   *@Tok Hong Siang / TL - TSENGFFS:* Monitor Tai Seng discrepancy; no action required if OOS logic holds.
    *   *@Akash Gupta / On Call:* Continue validation of SOH NULL values for bulk orders at **HGPT** (Mar 31 incident).
    *   *@Wai Ching Chan @Sampada Shukla:* Prioritize review of Hyper Parkway and Hyper Changi anomalies alongside pending validations for Sun Plaza, VivoCity, and HGPT.

**Decisions Made**
*   **App Release Strategy:** Picker App 10.4.0 rollout remains on hold pending resolution of critical data anomalies (Mar 18–Apr 3). Full rollout is contingent on stability post-fixes, specifically addressing:
    *   The newly discovered Apr 3 Hyper Parkway `packed_qty` anomaly (Order #23032024).
    *   The Apr 2 Hyper Changi `packed_quantity` NULL issue (Order #23013763).
    *   The Mar 31 HGPT SOH NULL issue.
    *   The Mar 29 Hyper Changi anomaly (Order #22972590).
    *   *(Note: Apr 3 Tai Seng discrepancy attributed to OOS; requires monitoring but not a data anomaly fix).*

**Critical Alerts**
*   **Active Alert (Apr 3):** Packlist quantity (`10,932,725`) significantly exceeds delivered quantity (`3`) at **Hyper Parkway (Order #23032024)**. Status: Under investigation by TL HPWP FFS.
*   **Active Alert (Apr 3):** Packlist quantity (`369,076`) exceeds delivered quantity (`2`) at **Tai Seng (Order #23009418)**. Status: Confirmed OOS/Drop-off.
*   **Active Alert (Apr 2):** Packlist status `RECEIVED` but `packed_quantity` is `NULL` at **Hyper Changi (Order #23013763)**.
*   **Active Alert (Mar 31):** Bulk order SOH indicated **NULL** at **HGPT**.
*   **Secondary Active Alert (Mar 28):** Dispatcher app unable to scan new zone at **hvivo**.


## [7/38] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Last Activity: 2026-04-03T05:47:49.970000+00:00 | Last Updated: 2026-04-03T06:35:40.134420+00:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
A third consecutive cluster of connectivity issues affecting `fni-order-create` occurred on **April 3**, mirroring instability observed on April 1 and April 2 regarding Mirakl/DBP integrations. Concurrently, the `picklist-pregenerator` continues to exhibit recurring critical latency with no improvement in execution times exceeding 3,600s.

**Incident Summary & Timeline**
*   **Service: `fni-order-create` (Cluster of Errors) – April 3 Morning**
    *   **Trigger Window:** Alerts began at **05:42:40 UTC**:
        *   "Exception Occurred At Mirakl Route" (`Monitor ID 17447918`) triggered at **05:42:40 UTC**.
        *   "Error while calling APIs" (`Monitor ID 17447928`) triggered at **05:42:49 UTC**.
    *   **Recovery:** All monitors returned to normal between **05:47:39 UTC** and **05:47:49 UTC**. Total duration: ~6 minutes.

*   **Service: `picklist-pregenerator` (Latency Warning) – Ongoing**
    *   **Status:** The streak of execution times exceeding 3,610s persists through the April 2 evening window and into April 3. No new specific trigger timestamp is provided for April 3 in this update, but the systemic failure pattern remains active.

*   **Historical Context**
    *   **April 1 & 2:** Similar clusters affecting `fni-order-create` resolved within ~6–8 minutes each.
    *   **Apple Pay:** Monitor `29851723` triggered on Apr 2 (04:56 UTC) and recovered by 05:12 UTC; no new activity reported.

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of the April 3 cluster affecting `fni-order-create`. Focus on Mirakl route exceptions (`Monitor ID 17447918`) and API errors (`Monitor ID 17447928`). The recurrence across three consecutive days (Apr 1, Apr 2, Apr 3) strongly indicates a systemic integration failure with Mirakl/DBP.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Address critical latency in `picklist-pregenerator`. Continuous execution times above 3,610s require immediate architectural review to prevent further degradation.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Summary for Leadership**
Instability in Mirakl/DBP integrations has persisted for a third consecutive day, triggering a cluster of two P2 alerts on `fni-order-create` between **05:42:40 UTC** and **05:47:49 UTC** on **April 3**. This follows nearly identical resolution windows on April 1 and April 2. The root cause remains unresolved, with specific errors now identified as "Exception Occurred At Mirakl Route" (Monitor ID `17447918`) alongside persistent API call failures. Concurrently, the `picklist-pregenerator` shows no recovery; execution times remain consistently above 3,610s. Urgent engineering review is required to break this three-day cycle of order processing failures and address the critical latency in seller experience workflows.


## [8/38] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw/GnX6VGfkaJk | Last Activity: 2026-04-03T04:32:06.459000+00:00 | Last Updated: 2026-04-03T06:36:02.710134+00:00
**Daily Work Briefing: Digital Product Development (DPD)**
**Source:** Google Chat Space | **Date Range:** April 2 – April 3, 2026
**Link:** https://chat.google.com/space/AAAAx50IkHw

### Key Participants & Roles
*   **Alvin Choo:** Initiator of the update regarding the Employee Code of Conduct.
*   **Michael Bui:** Clarified specific restrictions on data storage and AI tools.
*   **Winson Lim:** Seeker of official policy documentation; referenced Polly (work.fpg.sg).
*   **Maou Sheng Lee:** Front Office representative highlighting current non-compliant tool usage.
*   **Tan Nhu Duong:** Confirmed document availability but raised policy gaps regarding specific AI approvals.

### Main Topic
The discussion centers on mandatory updates to the Employee Code of Conduct regarding AI platform usage and data security. While a directive was issued prohibiting unapproved tools, recent verification reveals discrepancies between verbal directives and the written policy text.

### Decisions Made & Clarifications
1.  **Initial Directive:** Only **Gemini** was verbally confirmed as the approved tool for company-related items.
2.  **Policy Contradiction Identified:** Tan Nhu Duong (April 3, 04:24) noted that the updated PDF policy document does not explicitly mention which AI platform is approved, creating ambiguity against the verbal "Gemini-only" rule.
3.  **Document Access Confirmed:** The latest Code of Conduct is available on **Polly** at `work.fpg.sg` (Confirmed by Tan Nhu Duong, April 3, 04:21).

### Pending Actions & Ownership
*   **Action:** Identify the definitive source for the approved AI tool designation.
    *   **Owner:** Unassigned (Requested by Tan Nhu Duong on April 3).
    *   **Context:** The written policy lacks specific approval details, necessitating a follow-up to clarify the "Gemini-only" status.
*   **Action:** Resolve discrepancy regarding Front Office usage of **Claude Code**.
    *   **Owner:** Unassigned (Issue raised by Maou Sheng Lee; contradicts verbal Gemini rule).
*   **Action:** Review and acknowledge the attached PDF: *"NTUC Enterprise Mail - Important Updates to the Employee Code of Conduct.pdf"*.
    *   **Owner:** All team members.

### Key Dates & Follow-ups
*   **April 2, 2026 (10:02):** Initial announcement regarding new Code of Conduct updates.
*   **April 2, 2026 (11:30):** Verbal confirmation that only Gemini is permitted for company items.
*   **April 3, 2026 (04:21):** Confirmation that the policy is live on Polly (`work.fpg.sg`).
*   **April 3, 2026 (04:24):** Observation that the written policy text omits specific approved AI tool mentions.
*   **Immediate:** Team members are to raise questions regarding the gap between verbal directives and written policy immediately.

### Summary
The DPD team was initially informed of strict new AI governance rules effective April 2, with a directive stating **Gemini** is the sole approved platform. However, on April 3, Tan Nhu Duong confirmed that while the updated Code of Conduct is accessible via Polly (`work.fpg.sg`), the document text itself does not explicitly list the approved AI tool. This has created an ambiguity between the verbal "Gemini-only" instruction and the written policy. Consequently, a new action item requires identifying the authoritative source for the approved tool designation. Additionally, the conflict regarding the Front Office's use of **Claude Code** remains unresolved pending official clarification.


## [9/38] Digital & Tech - General
Source: gchat | Group: space/AAAAP63CaPo | Last Activity: 2026-04-03T03:52:45.781000+00:00 | Last Updated: 2026-04-03T06:37:02.555295+00:00
**Daily Work Briefing: Digital & Tech (D&T) General**

**Key Participants & Roles**
*   **Trina Boquiren:** Event Coordinator / Team Lead.
*   **Miguel Ho Xian Da:** Developer (iPOS UI, bug reporting).
*   **Ivan Cheow:** Product Owner/Developer (MyApp iOS optimization).
*   **Tan Peng:** Staff Member.
*   **Ching Hui Ng:** Project Lead (Smart Cart Pilot).
*   **Sip Khoon Tan:** Training Coordinator.
*   **Flora Wo Ke:** Staff Member reporting lost items.
*   **Dennis Seah:** Guidance provider for Digital Office Access.
*   **James Lai Li Hao & Mohammed Miran:** iOS/Android support.
*   **Cory Meilany:** Communications design and digital display coordination.

**Main Topics & Updates**
1.  **Digital Office Access Launch:** Successfully deployed to all FP Hub colleagues earlier in the week (Good Friday, April 3). The system has recorded approximately **400 active users**. This initiative received positive feedback for its ease of use and user experience.
2.  **MyApp iOS Update:** Previously released optimized door access featuring Lock Screen Widget, Tap Method, and In-App Method. The app must run in the background for scanning; Miguel Ho Xian Da handles bug reports.
3.  **Smart Cart Pilot:** Launched at **Punggol Oasis Terraces** (681 Punggol Drive, #B1-01). Features include attachable Smart Cart Tablets and integration with **Super** format colleagues and **Pricer** ESLs for LED blinking.
4.  **AI Training:** "Workbench Hands-on Training" on Gemini Enterprise & NotebookLM is scheduled for **Thursday, 19 March** (2:00 PM – 5:00 PM) at FP Hub L10. Virtual options available; alternative dates are 8 or 9 April.

**Pending Actions & Ownership**
*   **Lost Items – AirPods Pro:** Flora Wo Ke requests notification if anyone found an **AirPods Pro (2nd Gen) with case** on **L11**. The item was likely left in the office last week. *Owner: Staff who find item / Security.*
*   **Lost Items – Meeting Room 18:** Report lost phone/wallet previously noted for Tan Peng/Security.
*(Note: RSVP deadlines for March events have passed; no new actions required for All Hands or AI Training).

**Decisions Made**
*   Approved launch of Smart Cart pilot at Punggol Oasis Terraces with attachable tablets and ESL integration.
*   Confirmed iOS door access optimization requires the app to run in the background for widget functionality.
*   **Digital Office Access:** Confirmed successful rollout across FP Hub with high adoption (400 users).

**Key Dates & Deadlines**
*   **12 March 2026:** D&T All Hands (Completed/Past).
*   **19 March 2026:** Gemini Enterprise & NotebookLM Training (Past).
*   **8 or 9 April 2026:** Alternative dates for AI training.
*   **3 April 2026:** Digital Office Access launched and active at FP Hub.

**Historical Context**
The transition to digital access marks a significant milestone in the "Tech made easy" initiative, driven by cross-functional collaboration between D&T, HR, and operations teams.


## [10/38] Alvin, Gopalakrishna
Source: gchat | Group: space/AAQAMGrBBNE | Last Activity: 2026-04-03T03:56:30.110000+00:00 | Last Updated: 2026-04-03T06:37:21.071532+00:00
**Daily Work Briefing: Google Chat Summary (Updated)**

**Resource:** Alvin Choo, Gopalakrishna Dhulipati
**Metadata:** 6 messages | https://chat.google.com/space/AAQAMGrBBNE

**Key Participants & Roles**
*   **Alvin Choo:** Executive providing final guidance and expanding the scope of the warning.
*   **Gopalakrishna Dhulipati:** Compliance officer who flagged the initial violation regarding data privacy.
*   **Michael Bui:** Employee whose LinkedIn post triggered the discussion; identified as having shared metrics.
*   **Fiona:** Third party mentioned in the conversation who previously shared numbers and was instructed to remove them.

**Main Topic**
The discussion addresses a violation of the **Employee Code of Conduct** concerning the sharing of confidential **RMN metrics** on social media. While Gopalakrishna initially flagged Michael Bui's post for containing competitor-usable data, Alvin Choo subsequently reinforced that business metrics are sensitive and must not be shared generally.

**Actions & Ownership**
*   **Action:** Immediate removal of confidential RMN metrics from the LinkedIn post.
    *   **Owner:** Michael Bui (Completed).
*   **Action:** Broad dissemination of a compliance reminder regarding business metrics sensitivity to all employees.
    *   **Owner:** Alvin Choo (Implicit directive issued at 03:56:30 UTC); Gopalakrishna and Michael expected to assist in reinforcing this message.
*   **Action:** Monitoring social media activity for potential data leaks.
    *   **Owner:** All employees, with specific emphasis on caution regarding engagement (liking/resharing).

**Decisions Made**
*   **Strict Enforcement:** The organization maintains a "strict" stance on information security, extending beyond direct posting to include any interaction with confidential data.
*   **Expanded Scope:** Following Alvin Choo's directive at 03:56:30 UTC, the warning is no longer limited to Michael Bui but applies universally; all personnel are reminded that "business metrics is sensitive."

**Key Dates & Follow-ups**
*   **Date of Incident/Discussion:** April 3, 2026.
    *   *Initial Flag:* 01:27:15 UTC (Gopalakrishna alert).
    *   *Acknowledgment & Removal:* 02:06:54 UTC (Michael Bui confirms re-use of numbers and removal).
    *   *Further Guidance:* 02:10:41 UTC – 02:12:39 UTC (Discussion on strictness and future caution).
    *   *Final Directive:* **03:56:30 UTC** (Alvin Choo instructed to remind all personnel regarding the sensitivity of business metrics).
*   **Follow-up Status:** The specific removal action for Michael Bui is complete. A new organizational-wide reminder has been initiated by Alvin Choo to prevent future occurrences across the workforce. No pending action items remain for Michael Bui personally, but the conversation now serves as a broader policy enforcement alert for all staff.

**Resource Reference**
*   **Chat URL:** https://chat.google.com/space/AAQAMGrBBNE


## [11/38] RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Last Activity: 2026-04-03T03:20:50.261000+00:00 | Last Updated: 2026-04-03T06:37:42.669846+00:00
**Daily Work Briefing: Automated Test Results Summary (RMN Notification)**

**Key Participants & Roles**
*   **Collection Runner App:** Automated testing agent executing API suites.
*   **Webhook Bot:** Reporting mechanism; consistently returning "unable to process your request" on all notifications through April 3, 2026.
*   **Parties Involved:** System-generated notification log only.

**Main Topic/Discussion**
Automated nightly API test executions across `promo-service`, `marketing-personalization-service`, and `marketing-service` in the **staging** environment. Monitoring period spans March 12 through **April 3, 2026**. Execution windows occur at approximately 01:05 UTC (morning), 02:31 UTC (midnight), and **03:21 UTC** (early morning).

**Test Execution Status & Anomalies**
*   **`marketing-service`:** Regression confirmed.
    *   **April 3, 01:05 UTC:** Mixed results. API Contract Tests passed (20 Passed / 0 Failed), but API Tests failed (44 Passed / **3 Failed**).
    *   **Historical Context:** While stability was confirmed March 26–April 2, failures on April 2 and April 3 indicate a return to instability patterns similar to the March 17–25 window.
*   **`promo-service`:** Confirmed stable on April 3 at **02:31 UTC**.
    *   **API Contract Tests:** 6 Passed / 0 Failed.
    *   **API Tests:** 10 Passed / 0 Failed.
    *   Stability confirmed for March 26–April 3.
*   **`marketing-personalization-service`:** Confirmed stable on April 3 at **03:21 UTC**.
    *   **[API Contract Tests]:** 125 Passed / 0 Failed / 0 Skipped (Total Requests: 21).
    *   **[API Tests]:** 96 Passed / 0 Failed / 0 Skipped (Total Requests: 21).

**Pending Actions & Ownership**
*   **Webhook Bot Remediation (High Priority):** The bot failed to process requests in every notification cycle from March 12 through the latest log on **April 3 at 03:21 UTC**. Immediate attention is required from DevOps or Automation Infrastructure.
*   **Investigate `marketing-service` Regression:** Engineering must analyze the root cause of the 3 API test failures observed on April 3, 01:05 UTC (following similar failures on April 2), following a period of apparent instability.

**Decisions Made**
*   No human decisions recorded; all entries are automated system outputs.

**Key Dates & Deadlines**
*   **Failure Window (Historical):** Instability noted March 12–13 and persistently from **March 17 through March 25**.
*   **Current Status:** Mixed results on April 3.
    *   `marketing-service`: Failed API tests at 01:05 UTC.
    *   `promo-service`: Passed at 02:31 UTC.
    *   `marketing-personalization-service`: Fully successful run recorded at 03:21 UTC (125/96 passed).
*   **Monitoring Period:** Data covers runs from **March 12, 2026**, through **April 3, 2026**.

**Resource Info**
*   **Message Count:** Updated to reflect notifications through April 3.
*   **URL:** https://chat.google.com/space/AAQA85dw4So


## [12/38] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Last Activity: 2026-04-03T00:03:09.022000+00:00 | Last Updated: 2026-04-03T02:35:51.727770+00:00
**Daily Work Briefing Summary (Updated: April 3, 2026)**

**Main Topics & Discussions**
1.  **Programmatic Advertising:** Focus remains on validating discrepancies for `advertima_ttd-fixed-price-test-1.5`. Ravi Singh confirmed receipt of raw BURLs; validation was targeted for Monday, March 17th. Yian Koh requested confirmation on deals `advertima_ttd-first-price-test` and `advertima_ttd-fixed-price-test-1`.
2.  **New Deal Setup:** Yasmina Tregan (Advertima) requires an end-to-end test setup this week. Wei Phung to share live campaign details; Ravi Singh to execute setup, push to TradeDesk, and map segments before launch.
3.  **BCRS UAT & Finance Integration:** Progress continues on SAP document numbers, duplicate posting fixes via PubSub "exactly once" policy (PR #1033), and Bukit Timah Plaza pricing/display issues.
4.  **Event Sync Optimization (DPD-645):** Addressing the massive event overage (14M vs. normal 550k). PRD deployment plan set for Sunday, March 15.
5.  **Security & Compliance:** RMN Pentest fixes (DPD-700) deployed to Prod; Bitbucket App Passwords deprecated effective June 9, 2026.

**Status Update: Inbox & Communications**
*   **Inbox Status:** As of April 3, 2026 (00:03 UTC), the workspace inbox is fully caught up across all categories (**Urgent Action Items**, **Meeting Updates**, and **FYI**). No pending unread items require immediate attention. This status follows confirmations from daily summaries dated March 24 through April 2. The latest update from Workspace Studio confirms zero backlog in all sections, including Code Reviews and Project Updates.

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
*   **April 1, 2026:** Daily inbox review completed; no new urgent items identified.
*   **April 2, 2026:** Daily inbox review completed; no new urgent items identified across any category.
*   **April 3, 2026:** Daily inbox review completed via Workspace Studio; all categories (**Urgent Action Items**, **Thematic Groupings & Digests**, **Meeting Updates**, **FYI**) confirmed clear of backlog.
*   **June 9, 2026:** Bitbucket App Password deprecation deadline.

**Note on New Content:** The daily summary from April 3, 2026 (00:03 UTC), via Workspace Studio confirms the inbox remains clear of urgent action items across all categories. No changes to pending actions or decisions were required based on this update; historical context regarding project statuses and deadlines remains valid.


## [13/38] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Last Activity: 2026-04-02T14:36:56.701000+00:00 | Last Updated: 2026-04-02T22:37:27.483091+00:00
**Daily Work Briefing: Nikhil Grover & Michael Bui (Updated)**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator; coordinating incident fixes, ticket updates for the FE team, and RMN project preparation.
*   **Michael Bui:** Technical Lead (Engineering); currently on leave (April 6–12) but available for urgent clarifications before departure.

**Main Topics & Recent Developments (Mar 28 – Apr 02)**
1.  **Homepage Ad Race Condition (Critical):**
    *   A race condition identified March 27 remains unresolved regarding intermittent homepage ad rendering (symptoms: 2 ads with old slots or 6 ads with new slots).
    *   **Status:** Persisted through Mar 30 night despite slot alignment troubleshooting. Escalated to Michael Bui during his vacation planning phase.
2.  **Topic Pivot: RMN & Project Light (Apr 02):**
    *   On April 2, Michael requested a call to clarify details regarding **RMN** within **Project Light**.
    *   Motivation: Michael aims to finalize clarifications to prepare for his upcoming long weekend before leaving on April 6.

**Decisions Made & Status Updates**
*   **Meeting Scheduling:** A synchronous discussion was initially proposed for the afternoon of April 2. Nikhil declined due to personal obligations, suggesting a reschedule to "tomorrow (April 3)" or Monday instead. Michael confirmed availability for the following day ("Tmr") upon Nikhil's awakening.
*   **Deployment Readiness:** The pending resolution of the homepage ad race condition continues to delay deployment readiness.
*   **Ticket Coordination:** Scheduled update for DPD-838 with slot value examples and OSMOS logic remains a priority, coordinated with Alvin (originally scheduled Mar 29).

**Pending Actions & Owners**
*   **RMN Clarification Call (Michael Bui & Nikhil Grover):** Reschedule the catchup regarding RMN in Project Light. Michael intends to hold this discussion early on April 3 ("Tmr") or Monday to facilitate his weekend preparation.
*   **Incident Resolution (Michael Bui):** Review the intermittent homepage ad issue reported by Yangyu/Nikhil; address slot sequencing failures.
*   **Ticket Updates (Nikhil Grover):** Proceed with updating DPD-838 and coordinating with Alvin.
*   **Timeline Verification (Nikhil Grover):** Confirm the timeline for OSMOS `pcnt` limit expansion (>10), expected by early April.

**Key Dates & Deadlines**
*   **March 27, 2026:** Race condition identified.
*   **April 2, 2026 (14:35 UTC):** Michael clarified intent to resolve RMN/Project Light questions before his leave; availability set for the following morning.
*   **April 6–12, 2026:** Michael Bui's leave period (island with limited connectivity).

**Historical Context Note**
The conversation initially focused on technical scope: video content restricted to Omni Home/FP Pay, OSMOS `pcnt` limits set at 10 (expansion expected early April), and slot values being optional for uniqueness. On March 30, the focus shifted to a critical incident where intermittent rendering persisted despite troubleshooting. By April 2, with Michael's departure approaching, priorities expanded to include **RMN** discussions within **Project Light**. While Nikhil initially cited a $1,250/day impact (clarified as part of overall drops excluding specific advertiser campaign losses), the immediate operational focus remains on resolving the ad race condition and clearing RMN queries before April 6.


## [14/38] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/yI8UlY4--fY | Last Activity: 2026-04-02T11:07:37.842000+00:00 | Last Updated: 2026-04-02T22:37:59.836478+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Lead/Manager (Assigns deliverables, validates scope).
*   **Michael Bui:** RMN Specialist/Tech Lead (Responsible for planning and alignment on RMN scenarios).
*   **Nikhil:** Business Stakeholder (Subject matter expert for ads in PLP and OSMOS).
*   **Rock:** Team Member/Peer (Assumed scope of work regarding RMN).

**Main Topic**
Clarification of "homework" deliverables due early next week (targeting April 7, 2026) across Defense and Attack streams. A specific discussion arose regarding the ownership and scoping of the **RMN (Real-time Media Network)** work required for the new ads product.

**Pending Actions & Ownership**
*   **Michael Bui:**
    *   Align with Nikhil on "ads in PLP" and business requirements for running RMN with OSMOS for complex scenarios.
    *   Produce a plan and timeline based on this alignment.
    *   Provide an estimate to Alvin Choo (and Rock) confirming the team is undertaking the work.
*   **Team (Defense Stream):**
    *   Firm up support model details: SLOs, on-call schedules, and Zendesk integration.
    *   Create an overview plan for data migration.
    *   Develop a later-stage app transition plan.
*   **Team (Attack Stream):**
    *   Deliver a workable UAT version of the Identity SDK for user sessions.
    *   Draft the Core Payment tech document.
    *   Plan integration tests to clarify all integration points.

**Decisions Made**
*   The scope for RMN is confirmed as requiring business alignment with Nikhil before final planning can proceed.
*   It was clarified that internal leadership (Alvin and Rock) assumes the team will execute the RMN work; therefore, a formal estimate and plan are now mandatory deliverables from Michael Bui.

**Key Dates & Deadlines**
*   **Target Delivery:** Early next week (Week commencing April 6, 2026).
*   **Reference Date:** Conversation took place on April 2, 2026.

**Follow-ups Required**
*   Michael Bui to initiate alignment with Nikhil immediately upon returning from the EA sharing session mentioned by Alvin Choo.


## [15/38] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4 | Last Activity: 2026-04-02T11:02:51.709000+00:00 | Last Updated: 2026-04-02T22:38:39.808939+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Space Creator; Lead coordinating the briefing.
*   **Daryl Ng, Gopalakrishna Dhulipati, Tiong Siong Tee, Michael Bui, Akash Gupta:** Designated "Project Light Attack and Defence Leads".
*   **Tiong Siong Tee:** Invited to calls by Alvin (confirmed April 1).

**Main Topic**
Following the transition to active strategic planning ("Room 2") on March 24, the team is executing a split strategy between "Attack" (feature development) and "Defense" (operational stability). While collaboration on **"RMN"** and **"Payment"** slides began March 24, technical direction remains focused on decoupling from SAP. On **April 2**, Alvin Choo assigned specific homework tasks to be aimed for completion early next week, shifting focus toward concrete deliverables rather than just slide preparation.

**Pending Actions & Ownership**
*   **Action (Defense): Firm up the support model.**
    *   **Scope:** Define Support Level Objectives (SLOs), on-call rotation, and Zendesk integration.
    *   **Ownership:** Defense Team/Alvin Choo.
    *   **Status:** Assigned April 2, 11:02 AM UTC; target completion early next week.
*   **Action (Defense): Create an overview plan for data migration.**
    *   **Context:** Follows the "No Data Migration" strategy proposed by Alvin Choo on March 30 to reduce risk.
    *   **Ownership:** Engineering Team.
    *   **Status:** Assigned April 2, 11:02 AM UTC; target completion early next week.
*   **Action (Defense): Develop app transition plan.**
    *   **Status:** Can be deferred until later; high-priority overview required first.
*   **Action (Attack): Produce a workable UAT version of the Identity SDK for user sessions.**
    *   **Ownership:** Engineering Team.
    *   **Status:** Assigned April 2, 11:02 AM UTC.
*   **Action (Attack): Finalize Core Payment technical document.**
    *   **Ownership:** Daryl Ng / Engineering Team.
    *   **Status:** Assigned April 2, 11:02 AM UTC.
*   **Action (Attack): Plan RMN work to achieve the new ads product.**
    *   **Ownership:** RMN Leads.
    *   **Status:** Assigned April 2, 11:02 AM UTC.
*   **Action (Attack): Initiate integration testing strategy.**
    *   **Goal:** Clarify all integration points and establish a clear plan.
    *   **Ownership:** Daryl Ng / Engineering Team.
    *   **Status:** Assigned April 2, 11:02 AM UTC.

**Previous Pending Actions (Re-evaluated)**
*   **Action:** Evaluate technical feasibility of adding a "Data8" layer between DSP and SAP.
    *   **Status:** Risk raised by Tiong Siong Tee on April 2, 06:31 AM UTC regarding reconciliation issues with Caltran/Data8. This remains under review pending the new data migration overview plan.
*   **Action:** Provide updated organizational chart to Daryl Ng.
    *   **Status:** Requested at 07:01 AM UTC on April 2; replies received from Alvin Choo.

**Decisions Made & Shifts**
*   **Workstream Split:** Deliberate separation into "Attack" (product features, SDK, payments) and "Defense" (SLOs, support, migration strategy).
*   **Timeline:** New deliverables targeted for early next week following the April 2 briefing.
*   **System Architecture:** SAP integration remains decoupled from core operational logic; designated strictly for finance and sales records.

**Key Dates & Follow-ups**
*   **April 2, 11:02 AM UTC:** Alvin Choo assigned specific "homework" tasks (Defense support model, migration overview, Attack SDK UAT, Payment docs, RMN plan, Integration test strategy).
*   **April 2, 07:01 AM UTC:** Daryl Ng requested org chart; replies received.
*   **April 2, 06:31 AM UTC:** Tiong Siong Tee queried Data8/SAP reconciliation risks.
*   **March 30:** "No Data Migration" strategy proposed by Alvin Choo.


## [16/38] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/jPGy0nmdYfc | Last Activity: 2026-04-02T10:50:51.840000+00:00 | Last Updated: 2026-04-02T22:40:47.648949+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Daryl Ng:** Lead requesting clarification on team composition.
*   **Alvin Choo:** Participant providing the updated organizational documentation.
*   **Tiong Siong Tee:** Participant offering context regarding information retention.

**Main Topic**
Discussion centered on resolving memory overload regarding specific personnel assignments within Daryl Ng's team. The conversation shifted from a status inquiry to the successful delivery of required documentation to verify the current roster.

**Pending Actions & Ownership**
*   **Action:** No pending actions; the request for the organization chart has been fulfilled.
*   **Owner:** Alvin Choo (Completed).
*   **Status:** Resolved. Alvin Choo provided the updated organization chart containing team member details, addressing Daryl Ng's query.

**Decisions Made**
No formal strategic decisions were recorded; however, a resolution was reached regarding the immediate need for verification. The team agreed to rely on the newly provided external documentation from Alvin Choo rather than internal recall to ensure accuracy of the roster.

**Key Dates & Follow-ups**
*   **Date:** April 2, 2026 (07:01 – 07:02 UTC).
*   **Follow-up Required:** None at this time. The immediate query regarding team composition has been addressed.

**Contextual Notes**
The conversation highlighted a temporary information gap where internal recall was insufficient for verifying team roles. This gap was bridged by Alvin Choo's provision of the updated organization chart, shifting the workflow from "pending verification" to "information confirmed." The interaction underscores the necessity of centralized documentation for Project Light Attack and Defence Leads to prevent future roster confusion.

**Metadata Reference**
*   **Source:** Project Light Attack and Defence Leads
*   **Message Count:** 4
*   **URL:** https://chat.google.com/space/AAQAsFyLso4


## [17/38] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw | Last Activity: 2026-04-02T10:02:59.061000+00:00 | Last Updated: 2026-04-02T10:45:45.714635+00:00
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
*   **Wai Ching Chan:** Team Member.

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
11. **Bonus Communication:** On April 1, 2026 (13:51 UTC), Wai Ching Chan initiated a discussion regarding "FPG Bonus" with 2 replies. A YouTube link (`https://youtu.be/dQw4w9WgXcQ?si=xUc5b9AlRJE4gCah`) was shared in the thread.
12. **Social Events:** Kyle Nguyen announced an upcoming DPD BBQ ("We come first"). Boning He and Gopalakrishna Dhulipati shared snacks; Maou Sheng Lee expressed sentiment regarding energy waste on March 18.
13. **Employee Code of Conduct Update:** On April 2, 2026 (10:02 UTC), Alvin Choo circulated a critical update to the Employee Code of Conduct via NTUC Enterprise Mail (`Important Updates to the Employee Code of Conduct.pdf`), urging all staff to review for doubts.

**Pending Actions & Owners**
*   **FPPay Image Team (Andin Eswarlal Rajesh, DevOps):** Investigate root cause of banner image loading failures in production and deploy fix. Priority: High.
*   **S&G Verification Team (Vivian Lim Yu Qian, Product/Dev Teams):** Investigate current S&G flows against the WIP verification logic document to confirm if forced staff verification screens exist for restricted SKUs like milk powder. Reference: `https://ntuclink.atlassian.net/wiki/spaces/SE/pages/1995997683/WIP+S+G+Verification+Flow`.
*   **Incident Response Team (Jazz Tong, Akash Gupta, Gopalakrishna Dhulipati, Kyle Nguyen):** Act as support guides for the active DPD Incidents channel; monitor and resolve incoming incident queries.
*   **GP Team (Nicholas Tan / Mohit Niranwal):** Investigate Bitnami image replacement strategy to resolve TTR issues and update Golden Pipeline dependencies.
*   **iOS/Dev Team (Tiong Siong Tee):** Re-verify the previously identified iOS FPPay QR code login bypass bug status.
*   **Security Team (Mohammad Adyatma, All Devs):** Audit all projects for `axios` dependency versions to mitigate risks associated with the reported npm package compromise. Reference: `https://socket.dev/blog/axios-npm-package-compromised`.
*   **FPG Bonus Discussion (Wai Ching Chan):** Review details regarding FPG bonus distribution and linked content.
*   **All Staff:** Review the "Important Updates to the Employee Code of Conduct" PDF shared by Alvin Choo on April 2, 2026; raise any doubts immediately.

**Decisions Made**
*   No formal change freeze; feature releases are currently active (Alvin Choo).
*   Datadog team configurations must strictly follow Infrastructure as Code (Terraform) protocols; manual overrides are deprecated.
*   Miro's acquisition of Reforge is recognized as a strategic move to bridge product strategy and delivery gaps.
*   **New:** Active incident support protocol established for Jazz Tong, Akash Gupta, Gopalakrishna Dhulipati, and Kyle Nguyen on March 27, 2026.
*   **New:** Winson Lim endorsed the `affaan-m/everything-claude-code` repository as a key resource for AI-first engineering patterns and skill development.
*   **New:** Mandatory review of updated Employee Code of Conduct (April 2, 2026) initiated by Alvin Choo; staff must clarify doubts with management.

**Key Dates & Follow-ups**
*   **Apr 2, 2026 (10:02 UTC):** Alvin Choo distributed critical Employee Code of Conduct updates.
*   **Apr 1, 2026 (13:51 UTC):** Wai Ching Chan initiated FPG Bonus discussion; video shared.
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


## [18/38] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/9KYZsmc-670 | Last Activity: 2026-04-02T10:02:11.714000+00:00 | Last Updated: 2026-04-02T10:46:03.489055+00:00
**Daily Work Briefing: S&G Store Enablement Discussion (Updated)**

**Key Participants & Roles**
*   **Daryl Ng:** Digital Product Development (Inquiry lead, capacity planning).
*   **Sneha Parab:** Digital Product Development / SME (Process owner, technical implementation).
*   **David:** Action Owner (Ticket submission/assignment).
*   **Hanafi:** Ticket Processor.

**Main Topic**
Assessment of effort and timeline for a temporary "Pop-up S&G" store setup at Jewel. Discussion focused on verifying SOPs, identifying dependencies, and finalizing the request workflow.

**Decisions Made**
*   **Documentation:** The previously cited SOP is outdated. The team agreed to utilize Hanafi's automated process, referencing version 3.0 of the store setup doc or the new Jira form.
*   **Workflow Confirmation:** While SAP handles master data downloads directly to GCS, DPD must still create the store in DBP and coordinate with the DE team for search/browse data flow upon receiving Stock on Hand (SOH).
*   **Timeline Estimate:** End-to-end lead time is estimated at approximately 2 weeks.

**Pending Actions & Ownership**
1.  **Submit Request Ticket:**
    *   **Owner:** David.
    *   **Status:** **Completed.** The request was submitted via the new Jira form to accommodate the team's workload starting next week.
    *   **Reference Form:** https://ntuclink.atlassian.net/jira/core/projects/STOR/form/577
2.  **Ticket Assignment:**
    *   **Owner:** David / Daryl Ng.
    *   **Action:** **Completed.** As of April 2, 2026, the ticket has been assigned to **Hanafi** for processing.
    *   **Update:** This action supersedes previous pending assignments; no further assignment is required at this stage.
3.  **Stakeholder Coordination:**
    *   **Owner:** Daryl Ng / Brendon.
    *   **Action:** Confirm with Brendon regarding awareness of this specific request and ensure proper handover if he is not the originator.

**Key Dates & Follow-ups**
*   **Event Timeline:** The pop-up store event is likely to occur approximately 3 weeks from April 1, 2026.
*   **Current Date:** April 2, 2026.
*   **Capacity Check:** Request submission was prioritized immediately to prevent delays given the team's increased workload starting next week.

**Reference Links**
*   Outdated SOP: https://ntuclink.atlassian.net/wiki/spaces/SE/pages/1995999558/S+G+Store+Enabling+-+SOP
*   Current Setup Doc (v3.0): https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008160308/Store+setup+doc+v3.0


## [19/38] RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU/PYIHH8s-2LQ | Last Activity: 2026-04-02T09:54:24.246000+00:00 | Last Updated: 2026-04-02T10:46:21.723634+00:00
**Daily Work Briefing: RMN Leadership Space**

**Key Participants & Roles**
*   **Bryan Choong:** Team Leader/Sender of directive.
*   **Allen Umali:** Team Member/Respondent (completed initial task).
*   **Christopher Yong:** Team Member (inquired and confirmed compliance).
*   **Rajiv:** Subject matter contact (initiated the request).
*   **Wendi:** Team member whose acknowledgement was shared by Christopher.
*   **Wilson:** Source of relevant message on MT chat.
*   **@all:** The broader team audience addressed in the message.

**Main Topic**
The conversation concerns urgent updates to the **Employee Code of Conduct**. Leadership is emphasizing a shift in compliance posture and mindset, requiring explicit acknowledgement from all team members regarding these new updates.

**Pending Actions & Ownership**
*   **Action:** Review HR email and Wilson's MT chat message for Code of Conduct updates; provide explicit acknowledgement.
*   **Owner:** Team members (specifically those who missed the initial notification).
*   **Status Update:** Christopher Yong confirmed completion ("Done") at 09:45 UTC on April 2, 2026, by sharing Wendi's acknowledgement.

**Decisions Made**
No new policy decisions were made. The discussion clarified that the directive originated from Rajiv and was disseminated via a specific HR email and a message from Wilson on MT chat. Immediate, explicit acknowledgement is required to satisfy organizational compliance protocols.

**Key Dates & Deadlines**
*   **Date:** April 2, 2026.
*   **Deadlines:**
    *   Initial deadline: "Within the day" (set at 02:37 UTC).
    *   Allen Umali confirmed completion: 03:42 UTC.
    *   Christopher Yong confirmed completion: 09:45 UTC.

**Summary of Flow**
1.  **02:37 UTC:** Bryan Choong notified the team that Rajiv initiated a request for explicit acknowledgement regarding Employee Code of Conduct updates, noting only one response was received. He set a deadline for the same day.
2.  **03:42 UTC:** Allen Umali confirmed completion ("Done").
3.  **09:16 UTC:** Christopher Yong apologized for missing the initial notification and asked if the request was via email, quoting Bryan's original instruction.
4.  **09:17 UTC:** Bryan Choong confirmed it was via email and directed the team to check Wilson's message on MT chat alongside the HR email.
5.  **09:45 UTC:** Christopher Yong confirmed he had read the email and Code of Conduct, sharing Wendi's acknowledgement as proof of completion.

**Reference Data**
*   **Space URL:** https://chat.google.com/space/AAAAQQGZSZU
*   **Sources:** HR Email (Code of Conduct updates), Wilson's message on MT chat.


## [20/38] FPG Everyone - General
Source: gchat | Group: space/AAAAjDYVcBU | Last Activity: 2026-04-02T09:09:29.579000+00:00 | Last Updated: 2026-04-02T10:47:42.929754+00:00
**Daily Work Briefing: FPG Everyone Chat Summary (Updated)**
**Date Range:** March 3 – April 2, 2026
**Source:** Google Chat (FPG Everyone - General)

### Key Participants & Roles
*   **Serene Kua Puay Leng:** Promotes daily product deals and lobangs.
*   *(Previous participants retained: Siti Nabilah, Jasmine Neo, Keith Lee, Melissa Lim, Maisy Heeng, Si Min Ng)*

### Main Topics
1.  **Digital Access Rollout:** Completed as of Mar 30; user guide distributed.
2.  **Media Collaboration – "Bowl of Love":** Final episodes featuring Tyler Ten, Tasha Low, and Xiang Yun are live (Mar 21 launch). Focuses on warmth/healing with fresh Malaysian pork via @mediacorp.re.dian TikTok.
3.  **Industry Recognition:** Lau Pa Sat's "Spin for your Huat" featured by Campaign Asia as a top CNY 2026 campaign alongside Nike and Apple.
4.  **FairPrice Heartland Hits Launch (Mar 27):** Community storytelling contest (#FPHeartlandHits, #FPNorthie). Incentive: $50 E-Vouchers + song feature. Deadline: April 5, 2026.
5.  **Unity Wellness Promotions:** B1G1 offer on health/wellness (Mar 26–29) at Unity stores. Featured brands include Moom Health and Elastine.
6.  **Kopitiam Food Hall & Shabu Days Launch (Apr 3):** Confirmed launch of the brand-new Kopitiam Food Hall at Hillion Mall tomorrow (April 3). Features 25 F&B stalls, 14 halal-certified options, and the debut of **Shabu Days** ("Your Personal Shabu Treat Ritual"). Opening weekend includes live performances and exclusive swag.
7.  **Linkpoints Loyalty Promo ($0.99):** Redemption active for FairPrice Maple Syrup Cashews and Myojo Bowl Noodles. Collection deadline: April 5, 2026.
8.  **New Product Promo – Delicato Sausages:** Deal on Japanese-style sausages (Curry & Bonito Seaweed) at $3.95/packet until April 15, 2026.
9.  **Promotional Launch – KitKat F1 Pack (Apr 1):** Darren Goh announced the "Ready, Set, Break!" campaign. Exclusive to FairPrice, Cheers, and FairPrice Online. Price: $29.95; Contents: 2 KitKat 10s Sharebags + 1 KitKat & F1 Flask.

### Pending Actions & Ownership
*   **Shorty Awards Voting (Owner: All Staff):** Vote daily for *Bridge to Equity* and *2025 End-Of-Year Unpacked*. Deadline: **April 8**.
*   **Linkpoints Redemption (Owner: All Staff):** Redeem $0.99 rewards. Collection deadline: **April 5, 2026**.
*   **Easter Outreach @ Sunlove Abode (Owner: All Staff):** Join "Protein Pledge" Day of Service on **Thursday, April 9** (10:30 AM – 12:30 PM). Activities include Easter Bingo, serving buffet lunch to seniors, and egg distribution. Sign up here: `https://forms.gle/Y4B22gtUmU7SF42V6`.
*   **Volunteer Engagement:** Sign up via `https://forms.gle/UkyQDagmDy4mcY7K7`. "Willing Hearts Kitchen Crew" is fully booked.
*   **Sensory Test Sign-ups:** Chapati screening form open (`https://forms.gle/DFYrahZcvhtcoJ9R7`). Frozen Snacks sign-up closed.
*   **Delicato Sausage Trial (Owner: All Staff):** Encouraged purchase during promo through April 15 for instant meal upgrade.

### Decisions Made
*   **Awards Campaign:** Mobilization approved for Shorty Awards voting.
*   **Wellness Extension:** Unity B1G1 offer extended (Mar 26–29).
*   **Loyalty Initiative:** $0.99 redemption launched with specific SKUs.
*   **Brand Expansion:** Kopitiam Food Hall and Shabu Days launch confirmed for April 3 at Hillion Mall.
*   **Product Promotion:** Delicato sausage promo activated through April 15.
*   **Promotional Campaign:** KitKat F1 Flask Pack activation approved for exclusive retail distribution starting April 1, 2026.

### Critical Dates & Deadlines
*   **April 3:** Kopitiam Food Hall & Shabu Days launch (Hillion Mall).
*   **April 5:** Heartland Hits contest closes; Linkpoints redemption collection ends.
*   **April 8:** Shorty Awards voting deadline.
*   **April 9:** Easter Day of Service at Sunlove Abode (10:30 AM – 12:30 PM).
*   **April 15:** Delicato Japanese-style sausage promo expires.


## [21/38] ❗ Important Email
Source: gchat | Group: space/AAQAUJW8HMo | Last Activity: 2026-04-02T09:00:39.963000+00:00 | Last Updated: 2026-04-02T10:48:14.972706+00:00
**Daily Work Briefing Summary (Updated)**

**Key Participants & Roles**
*   **Michael Bui (You):** Managing Osmos support, event RSVPs, FileVault compliance, performance feedback, Project Light coordination, AI training follow-ups, GCP Service Account security, D&T Power Breakfast engagement, and Internal Talent Marketplace exploration.
*   **HR / FairPrice Group:** Expanded the Internal Talent Marketplace to include Corporate/HQ Non-Executive and Frontline Executive staff.
*   **TPA (ta@fairpricegroup.sg):** Point of contact for Internal Mobility programme queries.

**Main Topics**
1.  **GCP Security & Service Account Decommissioning:**
    *   **Objective:** Clean up legacy keys; focus on non-production (56 keys) and automated rotation.
    *   **Timeline:** Kyle Nguyen's team begins remediation week of March 30, 2026.

2.  **AI Training & Agentic Evolution Contest:**
    *   **Weekly Support:** Google AI Specialists hosting Wednesdays, 2:00–2:30 PM SGT (Mar 25 – May 31, 2026).
    *   **Contest:** Launched by FPG AI CoE & Google. Submissions due **April 25, 2026**.

3.  **DPD AI Guild Committee Monthly Meeting:**
    *   **Status:** Recurring first Tuesday, 10:00–10:50 AM SGT. Organizer: Michael Bui.
    *   **Location:** FairPrice Hub-11-L11 Room 10 (6) + Google Meet (`zhj-udzb-apd`).
    *   **Note:** Jazz Tong has declined the recurring invitation.

4.  **DPD, Core Product & Picking Teams Meeting:**
    *   **Event:** Thursday, April 2, 2026, 9:30–11:00 AM SGT (FairPrice Hub-13-L13 Heritage Room + Meet `mgv-sdor-ejt`).

5.  **D&T Power Breakfasts:**
    *   **Upcoming Event:** Tuesday, April 28, 2026, 9:00–10:30 AM SGT (Hub Level 11 Lobby B). Monthly on last Thursday hosted by Trina Boquiren.

6.  **BCRS & Project Light:**
    *   **Events:** RMN Discussion (Mar 26, 2:00 PM) and BCRS Regroup (Mar 26, 4:00 PM). Scheduling conflict noted.

7.  **Internal Talent Marketplace Expansion (New):**
    *   **Announcement:** Expanded April 2, 2026, to include Corporate/HQ Non-Executive and Frontline Executive staff.
    *   **Eligibility:** Min tenure of 2 years (Grade S/D) or 3 years (Grade C+); Green rating in last 2–3 years; no PIP/disciplinary actions in last 2–3 years. New role grade must match current grade.

**Pending Actions & Ownership**
*   **GCP Security Consent (Michael Bui):** Review legacy SA spreadsheet and indicate consent for automated rotation immediately.
*   **DPD/Core Product/Picking Meeting RSVP (Michael Bui):** Respond to April 2 invitation.
*   **Agentic Evolution Contest (Michael Bui):** Submit entry by **April 25, 2026**.
*   **Power Breakfast RSVP (Michael Bui):** Confirm "Yes" by **April 24** for April 28 event.
*   **BCRS & RMN Meetings (Michael Bui):** Confirm attendance for March 26 sessions; note conflict between 2:00 PM and 4:00 PM slots.
*   **Internal Talent Marketplace Exploration (Michael Bui):** View step-by-step guide and explore opportunities on the [myTalentHub portal]. Contact `ta@fairpricegroup.sg` for clarifications.

**Decisions Made**
*   **Agentic Evolution Contest:** Winners receive Google gear; focus on eliminating toil.
*   **Internal Mobility:** Greater cross-functional mobility encouraged between HQ and Frontline staff.
*   **GCP Remediation Priority:** Legacy key cleanup is highest priority; weekly status updates to follow via dedicated Google Group.

**Critical Dates & Deadlines**
*   **Mar 18, 2026:** Performance Feedback Meeting.
*   **Mar 25–May 31, 2026:** Weekly AI Workbench Sessions (Wednesdays).
*   **Mar 26, 2026:** RMN Discussion (2:00 PM) & BCRS Regroup (4:00 PM).
*   **Mar 30, 2026:** GCP Key Removal activities begin.
*   **Apr 2, 2026:** DPD/Core Product/Picking Joint Meeting; Internal Talent Marketplace officially expanded.
*   **Apr 24, 2026:** Deadline to RSVP for D&T Power Breakfast.
*   **Apr 25, 2026:** Agentic Evolution Contest Submission & FileVault Final Deadline.
*   **Apr 28, 2026:** D&T Power Breakfast (9:00 AM SGT).


## [22/38] SRE / Network / DBA / DevOps / Infra
Source: gchat | Group: space/AAAAYX-ew1s | Last Activity: 2026-04-02T08:46:52.272000+00:00 | Last Updated: 2026-04-02T10:49:28.019378+00:00
**Daily Work Briefing: SRE / Infrastructure Team**

**Key Participants & Roles**
*   **Kalana Thejitha:** Escalated CloudSQL PSC connectivity block (GCD-9015). Investigating DNS resolution failures for `soni-be` Cloud Run to `soni-preprod` CloudSQL. Requesting guidance on Private Zone configuration in `store-of-tmrw-nonprod-vpc`. Tagged @Saranga Colambage, @Kim Tong Ng, @Isuru Dilhan.
*   **Natalya Kosenko:** Submitted PR #12 (`infra-gcp-gen-ai-spark`) for service account rotation; pending review.
*   **Apurva Shingne:** Datadog PR #142 (GCD-8995) pending review by @Sneha Parab and @Nicholas Tan.
*   **Boning He:** Pricing workspace access PR #722 pending.
*   **Amit Giri:** Submitted Datadog permission change PR #152 (`fp-datadog-eu`) on 2026-04-01.
*   **Tayza Htoon:** Requested approval for Terraform workspace access PR #725; tagged @Himal Hewagamage and @Tiong Siong Tee.
*   **Zheng Ming, Wai Ching Chan, Calvin Phan:** Previously reported connectivity/network issues (GCD-8941, GCD-8954, DSD-11066).
*   **Himal Hewagamage & Isuru Dilhan:** Primary reviewers/approvers.

**Main Topics**
1.  **Gen-AI Compliance:** Natalya Kosenko submitted PR #12 on 2026-03-31 to remove an unused service account key from `infra-gcp-gen-ai-spark`.
2.  **Datadog Infrastructure:** Ongoing review of `fp-datadog-eu` PRs (#135–#152). Amit Giri submitted PR #152 on 2026-04-01. Apurva Shingne's PR #142 remains pending.
3.  **Terraform & Workspaces:** Natalya's PR #719, Boning He's PR #722, and Tayza Htoon's PR #725 remain pending review. A failed Terraform plan (`run-CZVLtajJGbLVojLM`) and ticket GCD-8900 are active.
4.  **CI/CD Pipeline Failures:** Soni-BE golden pipeline clone failures persist; `lt-strudel-api-go` Go versioning conflicts require resolution.
5.  **Critical CloudSQL Block (GCD-9015):** Kalana Thejitha reports a multi-day UAT block for `soni-be` Cloud Run (revision: `soni-be-00033-zjj`). Direct egress via PSC failed; DNS name `29eed2f7aa61.3fqp9bm8nzyts.asia-southeast1.sql.goog.` resolves but maps to no IP. Investigation required on `store-of-tmrw-nonprod-vpc` Private Zone configuration.
6.  **Cloud Networking:** AI agents in `us-central1` face internet connectivity issues (Ticket GCD-8941). Mohit Niranwal mandated non-prod testing prior to rollout.
7.  **Bastion Connectivity:** Wai Ching Chan's ticket GCD-8954 remains under investigation.

**Pending Actions & Ownership**
*   **Resolve CloudSQL DNS/PSC Block (GCD-9015):** Owned by @Saranga Colambage, @Kim Tong Ng, @Isuru Dilhan, and @Kalana Thejitha. Action: Create/update Private Zone in `store-of-tmrw-nonprod-vpc` to map the PSC DNS name to the correct IP for the Cloud Run backend.
*   **Review Datadog PR #152:** Owned by Amit Giri; requires immediate review by @Kyle Nguyen, @Himal Hewagamage, @Isuru Dilhan, and @Mohit Niranwal.
*   **Approve Terraform Workspace PRs:**
    *   **PR #725:** Owned by Tayza Htoon; requires approval from @Himal Hewagamage and @Tiong Siong Tee.
    *   **PR #12 (Gen-AI):** Owned by Natalya Kosenko; tagged for review by @Himal, @Mohit, and @Isuru.
    *   **PR #719 & #722:** Pending review by @Isuru Dilhan and @Himal Hewagamage.
*   **Review Datadog PR #142:** Owned by Apurva Shingne; tagged for review by @Sneha Parab, @Nicholas Tan.
*   **Troubleshoot Pipeline Issues:** Investigate Soni-BE SSH keys (Kalana) and `lt-strudel-api-go` config conflicts (Lester).

**Decisions Made**
*   **IaC Requirement:** Mandatory adoption of IaC for Datadog pipelines.
*   **Change Management:** Mohit Niranwal mandated non-prod testing for Cloud NAT changes before production deployment (GCD-8941).
*   **Compliance Action:** Removal of unused, unrotated service account keys is confirmed via PR #12 to address compliance gaps.

**Key Dates & Follow-ups**
*   **2026-03-31 (08:22 UTC):** Natalya Kosenko submitted PR #12 for service account key removal.
*   **2026-04-01 (06:58 UTC):** Amit Giri requested review and merge of Datadog PR #152.
*   **2026-04-01 (07:36–07:38 AM):** Tayza Htoon requested approval for Terraform PR #725.
*   **2026-04-02 (03:38 UTC):** Kalana Thejitha escalated GCD-9015, noting a multi-day UAT block and proposing VPC Connector as a solution.
*   **2026-04-02 (08:46 UTC):** Kalana Thejitha updated status on GCD-9015, identifying the root cause as likely DNS/Private Zone misconfiguration in `store-of-tmrw-nonprod-vpc` for PSC connections.


## [23/38] PDM Notification
Source: gchat | Group: space/AAAAnyFGr84 | Last Activity: 2026-04-02T08:38:30.160000+00:00 | Last Updated: 2026-04-02T10:49:50.790346+00:00
**Daily Work Briefing: PDM Notification Summary (Updated)**

**Key Participants & Roles**
*   **Gchat Notification / API Bot (Collection Runner):** Automated system generating test reports.
*   **Webhook Bot:** System component responsible for processing requests; currently failing to render/deliver links despite successful test execution.

**Main Topic**
Automated API contract and functional tests for the `gt-catalogue-service` in the Staging environment executed successfully but failed to generate final notifications due to a persistent Webhook Bot error. The system returns "Webhook Bot is unable to process your request" immediately following summary data, blocking access to detailed reports.

**Pending Actions & Ownership**
*   **Action:** Investigate the specific failure point in the Webhook Bot rendering logic. Prioritize verifying if the failure count discrepancy (1 vs 2 failed tests) aligns with raw Collection Runner data. Resolve the post-execution delivery issue to enable full report visibility.
*   **Owner:** Engineering/DevOps Team (responsible for the notification pipeline).
*   **Context:** New logs from April 2, 2026, confirm two separate execution windows where tests passed but reporting failed. The error is a systemic post-processing block, not a test execution failure.

**Decisions Made**
None recorded; priority remains on repairing the Webhook Bot's rendering capability. No code modifications to service logic are required as failures (if any) are isolated to the notification layer.

**Key Dates & Follow-ups**
*   **Historical Background:** March 18 and March 30, 2026 – Previous incidents with zero execution.
*   **Most Recent Failures/Issues:** April 2, 2026 (Two distinct runs):
    *   **Run 1 (05:38 UTC):** [API Tests] showed 1 Failed; [Contract Tests] showed 0 Failed.
    *   **Run 2 (08:38 UTC):** [API Tests] showed 2 Failed; [Contract Tests] showed 0 Failed.
*   **Environment:** Staging.
*   **Service:** `gt-catalogue-service`.
*   **Immediate Follow-up Required:** Correlate the "1 Failed" (Run 1) and "2 Failed" (Run 2) counts against raw data to determine if test stability is degrading or if the error message is masking variable results. Resolve Webhook Bot rendering errors to restore visibility.

**Status Summary**
The automated run summary indicates a critical failure in the *reporting layer*, not the test execution pipeline itself. Unlike previous incidents on March 30 where Total Requests were zero, April 2 runs show successful completion with varying test outcomes:

*   **Run 1 (07:26 UTC):**
    *   **[API Tests]:** 398 Total Requests, 677 Passed, **1 Failed**, 91 Skipped.
    *   **[API Contract Tests]:** 188 Total Requests, 350 Passed, 0 Failed, 13 Skipped.
*   **Run 2 (08:38 UTC):**
    *   **[API Tests]:** 398 Total Requests, 676 Passed, **2 Failed**, 91 Skipped.
    *   **[API Contract Tests]:** 188 Total Requests, 350 Passed, 0 Failed, 13 Skipped.

Despite these results, the Gchat Notification app explicitly states: "Webhook Bot is unable to process your request" for all runs. This confirms a systemic issue where the notification pipeline blocks finalization or display, even though the underlying Collection Runner executed cases. The presence of failed tests in the second run suggests potential instability that was previously obscured by earlier assumptions of total execution success. Immediate technical troubleshooting of the Webhook Bot's post-execution logic is required to restore full visibility into test outcomes and accurate failure reporting.


## [24/38] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Last Activity: 2026-04-02T08:10:34.920000+00:00 | Last Updated: 2026-04-02T10:50:24.961177+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Key Participants & Roles**
*   **Sneha Parab:** BCRS/Fees/Store Closure Impact Lead.
*   **Akash Gupta:** IMS availability/UAT stock sourcing, B2B SKU sync queries.
*   **Wai Ching Chan:** Order Service Deployment/Slot Logic Validation / UAT Stock updates.
*   **Michael Bui:** BCRS Deposit Logic/SAP Integration/Publisher of PRs.
*   **Daryl Ng:** Backoffice/Order Management/Bug Reporting / Slot Logic validation / SOH Sourcing.
*   **Andin Eswarlal Rajesh:** Frontend (iOS/Android) & BCRS UX queries / Amplitude tracking.
*   **Lester Santiago Soriano:** Backend Services Lead.
*   **Zaw Myo Htet:** Payment/Feature Flagging / Pre-order Voucher Logic.
*   **Shiva Kumar Yalagunda Bas:** Slot discrepancy reporting.
*   **Gopalakrishna Dhulipati & Dang Hung Cuong:** Address emoji validation.
*   **Alvin Choo:** Announced annual planning meeting for Apr 2, 9:30 AM.
*   **Yangyu Wang:** Tagged regarding split flag issues; reported iOS Instore page issue.

**Main Topics Discussed**
1.  **HPWP Serviceable Area Routing Issue (New):** On Apr 2 at 08:10 UTC, Daryl Ng reported that Parkway postal codes are incorrectly routing to HCBP instead of HPWP in the serviceable area logic. Akash Gupta and Wai Ching Chan have been tagged for access verification and investigation.
2.  **Unit Price Calculation Compliance:** On Mar 31, Lester highlighted a government compliance requirement for Phase 2 unit price calculations. Current reliance on parsing `display_units` is unscaleable. Proposed solution involves ingesting structured fields (`pack_size`, etc.) from Mirakl/SAP into DBP. Sneha Parab requested an effort assessment.
3.  **iOS Instore Page Regression:** On Apr 1 at 04:14 UTC, Yangyu Wang reported a functional issue on the iOS instore page (Android unaffected). Andin Eswarlal Rajesh is investigating.
4.  **BCRS Stock Sourcing for Sign-off:** On Apr 2 at 02:54 AM, Daryl Ng requested adding Stock on Hand (SOH) for product ID `1152196` in "1HD" store (Store ID: 768). Wai Ching Chan is handling this for Finance sign-off.
5.  **Pre-order Voucher Payment Logic:** On Apr 2 at 03:14 AM, Zaw Myo Htet queried app voucher charging logic for in-store pickups. Wai Ching Chan is addressing queries on sales and voucher cost posting.
6.  **BCRS Deposit Logic Failure:** On Mar 30, Wai Ching Chan reported missing deposit values during UAT checkout. Sundy Yaputra is investigating this regression.
7.  **Slot Date Discrepancy:** Shiva Kumar Yalagunda Bas reported a delivery slot mismatch (UI shows 25th, API indicates 23rd). Daryl Ng and Sundy Yaputra are resolving this.
8.  **Omni Home Split Flag Regression:** On Mar 31 at 02:27 UTC, Daryl Ng reported that Omni home swimlanes fail to follow the split flag due to backend default setting updates.

**Pending Actions & Ownership**
*   **Akash Gupta & Wai Ching Chan:** Verify access to HPWP serviceable area data and investigate Parkway postal code routing to HCBP (New).
*   **Wai Ching Chan:** Add SOH for product `1152196` in store 768; Update specific SKUs to "unlimited stock" in UAT; Clarify pre-order voucher posting logic.
*   **Sundy Yaputra:** Investigate missing BCRS deposit values in UAT checkout and resolve slot date mismatch (UI vs API).
*   **Akash Gupta, Michael Bui, Andin Eswarlal Rajesh:** Provide immediate inputs on BCRS tickets DPD-637 and DPD-807 to close the epic.
*   **Lester Santiago Soriano / Sneha Parab:** Assess effort for mapping structured unit price fields from Mirakl/SAP.
*   **Andin Eswarlal Rajesh:** Investigate iOS instore page regression reported by Yangyu Wang.
*   **Daryl Ng:** Review Michael Bui's PR #7 (`bcrs-deposit-posting`) and investigate Omni home split flag issue with Nikhil and Yangyu Wang.

**Decisions Made**
*   **Unit Price Structure:** Move from parsing `display_units` to utilizing structured fields for Phase 2 compliance.
*   **BCRS Epic Priority:** Immediate action required to close the BCRS epic; ticket status must be verified for DPD-637 and DPD-807.
*   **UAT Stock Critical:** Specific SKUs identified by Sneha Parab must be set to unlimited stock immediately. Product `1152196` requires SOH in store 768.
*   **iOS Issue:** Investigation initiated into iOS-specific instore page failure.

**Key Dates & Deadlines**
*   **Mar 30, 2026:** B2B sync clarity requested; UAT stock updates required; BCRS deposit failure reported.
*   **Mar 31, 2026:** Unit price compliance discussion initiated; Omni home split flag regression reported.
*   **Apr 2, 2026 (Today):** Annual planning meeting scheduled for 9:30 AM (Host: Alvin Choo); HPWP routing issue flagged at 08:10 UTC.

**Note on Historical Context:** Previous mentions of code review priorities for `layout-service` PR #362 are superseded by the urgent Strudel SDK deployment update (`go-platform-website`). Current focus includes investigating UAT BCRS deposit regression, updating UAT stock levels, resolving slot date mismatches, closing the BCRS epic via tickets DPD-637 and DPD-807, debugging the Omni home split flag configuration, assessing structured unit price field ingestion, troubleshooting the new iOS instore page regression, clarifying pre-order voucher payment posting logic, and verifying HPWP serviceable area routing.


## [25/38] [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Last Activity: 2026-04-02T08:10:29.847000+00:00 | Last Updated: 2026-04-02T10:51:18.467929+00:00
**Daily Work Briefing: [Prod Support] Marketplace**

**Key Participants & Roles**
*   **Support/Operations:** Willie Tan, Iris Chang, Lalita Phichagonakasit, Charlene Tan, Jie Yi Tan, Ayton See, Amos Lam, Michelle Lim.
*   **Technical/Admin Team:** Dang Hung Cuong, Shiva Kumar Yalagunda Bas, Olivia -, Jill Ong, Greta Lee, Zaw Myo Htet, Angella Yeo, Cassandra Thoi, Gopalakrishna Dhulipati, Ee Ling Tan, Sneha Parab.
*   **New Reporter:** Muhammad Sufi Hakim Bin Safarudin.

**Main Topics & Discussion Summary**
Discussions continue to focus on operational blockers regarding seller onboarding, order fulfillment discrepancies, system configuration errors, and data visibility gaps. New reports from April 1 highlight critical platform performance issues (lag), DBP barcode conflicts, and delivery window synchronization failures. Additionally, queries arose on April 2 regarding picker app historical data, specific seller app issues, and image identification problems.

1.  **Transporter App Performance:** Anwar Nur Amalina reported (Apr 1) severe lag and job loading failures in the Transporter Inform app.
2.  **DBP Barcode Duplicate/NotFound Error:** Charlene Tan flagged (Apr 1) a barcode unable to be found in DBP despite appearing as a duplicate entry. Dang Hung Cuong was tagged for investigation.
3.  **Delivery Window Synchronization:** Jie Yi Tan reported (Apr 1) that the delivery window configuration failed for seller "Funa Artistic Hampers & Gifts" (displaying 3 days instead of configured 5). Dang Hung Cuong was tagged.
4.  **Seller Account Sync Failure:** Michelle Lim reported (Mar 31) that two new seller accounts failed to sync to DBP despite allocated internal codes and no error messages (Codes: 32208, 32207).
5.  **Image Identification Query (New):** On Apr 2, Charlene Tan queried the team regarding how to identify specific image problems. The discussion involved multiple replies by early afternoon.
6.  **Picklist Investigation:** Tech team is investigating failures for Order #258155683 and Postponed Order #256653797 (reported Apr 30).

**Pending Actions & Ownership**
*   **Transporter App Investigation:** Technical team to investigate lag and job loading failures (Anwar Nur Amalina, Apr 1).
*   **DBP Barcode Discrepancy:** Dang Hung Cuong to investigate why a specific barcode cannot be found in DBP while showing as a duplicate (Charlene Tan, Apr 1).
*   **Delivery Window Fix:** Dang Hung Cuong to resolve the delivery window sync issue for "Funa Artistic Hampers & Gifts" (Jie Yi Tan, Apr 1).
*   **Seller Sync Investigation:** Tech team to investigate why DBP accounts 32208 and 32207 failed to sync (Michelle Lim, Mar 31).
*   **Report Email Logic:** Confirm and implement automatic CC of `db-online-marketplace@ntucenterprise.sg` for all DF vendor Sales Breakdown Reports (Iris Chang, Mar 31; cc: Amos Lam, Michelle Lim, Jill Ong).
*   **SKU Live Status:** Investigate why SKU 90248069 is not live on the website despite being published with an offer (Charlene Tan, Mar 31).
*   **Picker App Functionality:** Dang Hung Cuong and Amos Lam to clarify picker app history viewing capabilities for sellers (Iris Chang, Apr 2).
*   **Toh Thye San Issue / Urgent Fulfillment Block:** Jing Ying Foo raised a "similar issue from Aw's Market" on Apr 2 at 07:02 UTC. Amos Lam escalated this urgently to Dang Hung Cuong, Shiva Kumar Yalagunda Bas, and Sneha Parab at 07:04 UTC due to potential fulfillment impacts. Charlene Tan (Apr 2, 15:06) clarified that storage type assignments are managed by GLS, not tech; the immediate fix is using an alternative PA label to scan orders before end-of-day cutoffs.
*   **Image Problem Analysis:** Team to determine root cause of image identification issues raised by Charlene Tan (Apr 2).

**Decisions Made**
*   Dang Hung Cuong is prioritizing the removal of Item ID: 90244361, new picklist failures, Woah Group offers errors, Pureen barcode truncation, DBP sync issues, Transporter app lag, and delivery window failures.
*   Dang Hung Cuong and Shiva Kumar Yalagunda Bas are assigned to investigate vendor picklist anomalies.
*   **Clarification:** Storage type assignments for GLS-related scanning issues are confirmed as non-technical; the operational workaround is applying alternate PA labels immediately.
*   **Completed:** Access linkage for Seller ID 31435 was successfully executed by Shiva Kumar Yalagunda Bas on Mar 27, 11:29 UTC.

**Key Dates & Deadlines**
*   **2026-04-02:** Jing Ying Foo raised "Aw's Market" issue; Amos Lam escalated urgent fulfillment risk request (cc: Sneha Parab, Shiva Kumar Yalagunda Bas); Charlene Tan clarified GLS storage logic and advised on PA label workaround. Iris Chang queried picker app history functionality; Charlene Tan initiated image problem discussion.
*   **2026-04-01:** Anwar Nur Amalina reported Transporter app lag; Charlene Tan flagged DBP barcode conflicts; Jie Yi Tan reported delivery window sync failure for "Funa Artistic Hampers & Gifts."
*   **2026-03-31:** Michelle Lim reported DBP sync failure for codes 32208 and 32207. Iris Chang raised Sales Breakdown Report email logic query. Charlene Tan reported SKU 90248069 not live.
*   **2026-03-30:** Muhammad Sufi Hakim Bin Safarudin reported picklist generation failures for Order #258155683 and Postponed Order #256653797.


## [26/38] [Prod Support] Onsite/Search/Browsing
Source: gchat | Group: space/AAAA8Ot7GRg | Last Activity: 2026-04-02T07:22:12.112000+00:00 | Last Updated: 2026-04-02T10:51:47.408401+00:00
**Daily Work Briefing: [Prod Support] Onsite/Search/Browsing**

**Key Participants & Roles**
*   **Terence Cheah:** Investigating Amplitude tracking anomalies (March) and recently flagged potential bot activity on specific search terms.
*   **Lalita Phichagonakasit:** Originally raised issues regarding SKU `13226899` visibility and reordering (March).
*   **Emerald Sia:** Reported a critical outage where Preorder SKUs failed to appear despite going live at 09:00; noted removal of comms due to the issue.
*   **Tiffany Teo:** New report regarding Promo SKU `13279469` not reflected in HPWP (Home Page Widget Platform).

**Main Topics**
The discussion has expanded from historical anomalies to four active operational incidents:
1.  **Preorder Visibility Outage (Critical):** Preorder SKUs are not displaying on the site or via deep link (`fairprice://preorder/campaign`) despite a scheduled 09:00 go-live. Emerald Sia confirmed all communications were halted due to this failure.
2.  **Search Traffic Anomalies:** Terence Cheah identified suspicious "dirty traffic" on two specific terms: `Nescafe concentrate` (new, high volume) and `Bio-home capsule` (elevated volume with zero post-click interactions).
3.  **HPWP Display Failure (New):** Tiffany Teo reported that Promo SKU `13279469` is not appearing in the Home Page Widget Platform as of April 2, 2026, at 07:22 UTC+00:00.
4.  **Historical Context:** Ongoing investigation into Amplitude tracking gaps (March 10+) and SKU `13226899` visibility for postal code `762115`.

**Pending Actions & Ownership**
*   **Action A (Preorder/Engineering):** Immediate root cause analysis of why Preorder SKUs are invisible at go-live.
    *   *Owner:* Unassigned (Engineering/Product).
    *   *Context:* Critical business impact; comms already removed by Emerald Sia.
*   **Action B (HPWP/Product):** Investigate and resolve visibility failure for Promo SKU `13279469` in HPWP.
    *   *Owner:* Unassigned (Product/Engineering).
    *   *Context:* High priority; reported by Tiffany Teo with 12 replies awaiting resolution.
*   **Action C (Search/Safety):** Investigate bot activity on `Nescafe concentrate` and `Bio-home capsule`. Verify traffic sources and click-through behavior anomalies.
    *   *Owner:* Unassigned (Security/Search teams).
    *   *Context:* High volume/zero conversion suggests malicious or broken traffic.
*   **Action D (Analytics):** Continue investigation into Amplitude event gaps (March 10+) and backend deployment impact. (Status unchanged from March report).
*   **Action E (Product/Search):** Re-evaluate SKU `13226899` visibility for postal code `762115`.

**Decisions Made**
No formal resolutions recorded. The Preorder issue has triggered an immediate halt to marketing communications. A message regarding potential bot activity remains under investigation. An "Unknown User" sent a deleted message at 03:37 UTC+00:00 on April 2, 2026, adding no new actionable data.

**Key Dates & Follow-ups**
*   **Preorder Failure Date:** April 2, 2026 (Failed to launch at 09:00 local time).
*   **HPWP Report Time:** April 2, 2026, 07:22 UTC+00:00.
*   **Search Anomaly Report:** April 2, 2026, 03:35 UTC+00:00.
*   **Amplitude Gap Start:** March 10, 2026.
*   **Thread Activity:** Last confirmed reply recorded on April 2, 2026 (Emerald Sia and Terence Cheah). Thread shows 36 unread replies to the Preorder alert; HPWP thread has 12 unread replies.

**Specific References**
*   **Resource Tag:** `#Amplitude-discussions` | `#Preorder-Outage` | `#Search-Traffic-Spoofing` | `#HPWP-Display-Issue`
*   **Analytics URL:** https://app.amplitude.com/analytics/fairprice/chart/y69ylkn/edit/r76iv7h7
*   **Metric Affected:** "order checkout for online grocery completed"
*   **Product IDs (Historical):** `13226899`
*   **New Product ID:** `13279469` (Promo SKU)
*   **Affected Postal Code:** `762115`
*   **Search Terms Flagged:** `Nescafe concentrate`, `Bio-home capsule`
*   **Preorder Deep Link:** `fairprice://preorder/campaign`


## [27/38] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/KTy1--6dEUY | Last Activity: 2026-04-02T06:31:43.183000+00:00 | Last Updated: 2026-04-02T10:53:46.148589+00:00
### Daily Work Briefing: Project Light Attack and Defence Leads

**Key Participants & Roles**
*   **Tiong Siong Tee:** Raised a technical concern regarding data layer architecture and historical reconciliation risks.
*   **Gopalakrishna Dhulipati:** Provided immediate directive to escalate the identified risk.

**Main Topic/Discussion**
The discussion focused on the architectural implications of inserting a `data8` layer between the DSP and SAP systems within Project Light Attack and Defence Leads. Tiong Siong Tee queried whether this addition would introduce increased reconciliation issues, citing historical precedents from the `fppay` project where similar integrations with `caltran` or `data8` frequently encountered problems.

**Pending Actions & Ownership**
*   **Action:** Raise the concern regarding potential `data8` reconciliation issues immediately.
*   **Owner:** Tiong Siong Tee (inferred from Gopalakrishna's directive "you should raise it now" addressed to the proposer).
*   **Context:** The escalation must address the risk of introducing new reconciliation failures between DSP and SAP via the proposed `data8` layer, referencing past `fppay` experience.

**Decisions Made**
No technical decision regarding the architecture has been finalized yet. The only outcome was an administrative directive to escalate the issue for review or formal discussion immediately rather than delaying it.

**Key Dates & Follow-ups**
*   **Date of Discussion:** April 2, 2026 (UTC) at 06:31 UTC.
*   **Immediate Next Step:** The concern must be raised "now" (relative to the chat timestamp of 06:31:43).
*   **Reference Data:** `fppay` project history involving `caltran` and `data8`.

**Resource Metadata**
*   **Space URL:** https://chat.google.com/space/AAQAsFyLso4
*   **Total Messages:** 2


## [28/38] 📢 COM Notifications
Source: gchat | Group: space/AAAAu4WIubc | Last Activity: 2026-04-02T06:29:56.703000+00:00 | Last Updated: 2026-04-02T06:38:09.262656+00:00
**Daily Work Briefing: SonarCloud Quality Monitoring**

**Key Participants & Roles**
*   **gautam-ntuc**: Developer; responsible for `catalogue-service` (PR-535) and `catalogue-job` commits.
*   **Shiva Kumar Yalagunda Bas**: Developer; previously authored `supplier-job` changes.
*   **bitbucket-pipelines**: Automated CI/CD bot triggering merges and deployments.
*   **System/Webhook Bot**: Continues reporting recurring "Webhook Bot is unable to process your request" errors across all notifications, including new scans on April 2.

**Main Topic**
Automated SonarCloud quality gate scans for `catalogue-service`, `fni-product-license-alert`, and other services. The conversation tracks code coverage, pipeline volatility, the resolution of failing Quality Gates, and persistent system notification errors.

**Status Summary by App**
*   **`fni-product-license-alert`**:
    *   **April 2 (03:14–06:29 UTC)**: PR-1433 underwent multiple scans (ver. `1242b0a`, `3212fc0`, `770f1f6`, `d5a9f8a`), all **PASSED** with 94.4% new code coverage.
    *   **April 2 (06:29 UTC)**: PR-1483 scanned and **PASSED**, but recorded **0%** Coverage on New Code. This mirrors a previous anomaly seen in PR-1479 on April 1.
*   **`catalogue-service`**:
    *   **April 2 (05:21–05:25 UTC)**: gautam-ntuc opened PR-535 (`feature/rebase/PRDM-513-make-deposit-sku-data-available`). Status is currently **OPEN** with **95.9%** new code coverage.
*   **`supplier-job`**: No new activity reported; previous scans on March 19 remain the last recorded success.

**Pending Actions & Ownership**
*   **System Error Investigation**: The "Webhook Bot is unable to process your request" error persists in every notification from March 5 through April 2 (including `catalogue-service` PR-535 and `fni-product-license-alert` PR-1483). No specific owner assigned; requires immediate engineering attention.
*   **`fni-product-license-alert` Coverage Anomaly**: A second instance of a **PASSED** Quality Gate with **0%** new code coverage occurred in PR-1483 on April 2. This contradicts typical gate logic (following the PR-1479 incident on April 1) and requires investigation into tolerance settings or data reporting integrity.
*   **`catalogue-service` Monitoring**: PR-535 is currently OPEN; teams should monitor for potential failure/recovery cycles similar to previous `seller-proxy-service` incidents.

**Decisions Made**
*   **April 2 Action**: `fni-product-license-alert` PR-1433 scans consistently recovered and passed immediately despite volatility in previous days' logs. The system accepted the merge logic automatically.
*   Recent merges in `supplier-job` and recovery scans for `seller-proxy-service` remain valid historical context, though current focus has shifted to `catalogue-service`.

**Key Dates & Timeline**
*   **April 1**: 
    *   **03:51 UTC**: `fni-product-license-alert` PR-1479 PASSED with 0% coverage.
    *   **03:52–04:22 UTC**: `seller-proxy-service` PR-2334 failed/recovered cycle.
*   **April 2**: 
    *   **03:14 – 06:27 UTC**: Multiple PASSED scans for `fni-product-license-alert` PR-1433 at 94.4% coverage.
    *   **05:21 – 05:25 UTC**: `catalogue-service` PR-535 opened by gautam-ntuc (OPEN, 95.9% coverage).
    *   **06:29 UTC**: `fni-product-license-alert` PR-1483 PASSED with **0%** new code coverage.


## [29/38] Alvin Choo
Source: gchat | Group: dm/zmMZpgAAAAE | Last Activity: 2026-04-02T05:15:22.777000+00:00 | Last Updated: 2026-04-02T06:41:57.055186+00:00
**Daily Work Briefing: RMN & Postmortem Updates (Updated)**
**Resource:** Alvin Choo (Lead/Manager) | **Participant:** Michael Bui (Domain Expert, Backend Dev)
**Date Range:** March 3 – April 2, 2026 + Upcoming Planning

### **Key Participants & Roles**
*   **Alvin Choo:** Leads coordination for RMN postmortem reports, travel logistics, and visa invitations. Contact: +65 9351 0653.
*   **Michael Bui:** Domain expert responsible for backend implementation; returned to Singapore on April 2 after leave (ended April 2).

### **Main Topics**
1.  **Wuhan Travel & Visa Processing:** Departure confirmed for **April 6, 2026**. Michael requires a multi-entry Type M visa applied for one month in advance. Alvin is securing an invitation letter from CoMall.
2.  **RMN Postmortem & Incident Review:** Finalizing report for BCRS completion; addressing "Overage on transaction sync" and transition to impressions-based model.
3.  **Technical Implementation & Prioritization:** Michael has returned and identified the project timeline as "very tight and challenging." He requested immediate focus areas from Alvin to utilize his upcoming long weekend for preparation.

### **Decisions Made**
*   **Task Reassignment:** The Nikhil ticket (5-man-day) is assigned to a Backend Engineer from Daryl's team. Michael will remain available for logic verification but no formal KT session is required.
*   **Support Model:** AI assists in logic derivation; Michael clarifies complex dependencies during development if needed.
*   **Visa Strategy:** Visa Type M confirmed. Alvin advised checking with Gopal and Ravi regarding self-processing methods while waiting for the invitation letter.
*   **Strategic Focus (New):** Michael to prioritize critical path items immediately upon return to mitigate tight timeline risks. Specific focus areas to be defined by Alvin.
*   **Contact Exchange:** On March 25, Alvin provided his mobile number (**93510653**) for direct coordination.

### **Pending Actions & Ownership**
| Action Item | Owner | Details/Context |
| :--- | :--- | :--- |
| **Focus Direction** | Alvin Choo | Communicate specific priority tasks to Michael immediately so he can prepare during his long weekend. |
| **Ticket Reassignment** | Alvin Choo | Assign Nikhil ticket to a BE from Daryl's team; allow self-learning with Michael support. |
| **Visa Application** | Michael Bui | Apply for multi-entry Type M visa immediately upon receiving invitation letter. Use Alvin's number (93510653). |
| **Invitation Letter** | Alvin Choo | Secure business letter from CoMall to expedite the visa process. |
| **Workshop Prep (Design)** | Michael Bui | Create docs detailing "as-is" vs. "to-be" flows; note: Returned April 2, targeting long weekend prep. |
| **Postmortem Review** | Alvin Choo | Final review after PDA impact verification (Vijay) and Advertima POV status inclusion. |

### **Key Dates & Milestones**
*   **April 2:** Michael returned to Singapore; leave period ended.
*   **April 3:** Public Holiday in Singapore.
*   **Upcoming Long Weekend:** Critical preparation window for Michael regarding tight project timeline.
*   **April 6:** Confirmed departure date for Wuhan, China.
*   **April 9:** Target PRD deployment deadline (Nikhil's requirement); UAT readiness targeted for April 7-8 if needed.
*   **End of Q1 2026:** Advertima POV pilot period concludes.


## [30/38] DPD x Platform Engineering
Source: gchat | Group: space/AAQAcjNXKpA | Last Activity: 2026-04-02T04:22:24.431000+00:00 | Last Updated: 2026-04-02T06:43:37.697132+00:00
**Daily Work Briefing: DPD x Platform Engineering**
*(Updated with April 2 P1 Incident IR-49 & Terraform Execution)*

**Key Participants & Roles**
*   **Kyle Nguyen:** Infrastructure/Platform Engineering (Reviewer, Incident Triage).
*   **Daryl Ng:** Incident Analyst.
*   **Gopalakrishna Dhulipati:** Addressed in new P1 incident; involved in Redis RCA.
*   **Sneha Parab:** Involved in Redis RCA.
*   **Alvin Choo:** Team Lead; escalated regarding April 2 P1 incident.
*   **Sampada Shukla:** Reported SLO alerts March 31; validated April 1 alerts.
*   **Dodla Gopi Krishna:** Owner of Fulfillment/Pricing SLOs; queried April 1 "Get serviceable area" journey.
*   **Maou Sheng Lee:** Initiated inquiry on April 2 regarding P1 incident status.
*   **Jazz Tong:** Provided Terraform run link for `infra-gcp-fpon-prod`.

**Main Topics & Discussions**
1.  **P1 Incident: IR-49 "Picking list not available" (April 2):** Maou Sheng Lee flagged the incident as "Active" and breaching group policy at ~03:36 UTC on April 2, requesting status updates and follow-up owners. The alert was directed to Alvin Choo and Gopalakrishna Dhulipati.
    *   *Status:* Incident remains Active P1; requires immediate resolution validation.

2.  **Terraform Execution (April 2):** Jazz Tong shared a Terraform run link (`run-g4Lg24A7Y21cJzPQ`) for the `infra-gcp-fpon-prod` workspace at ~04:22 UTC.
    *   *Status:* One reply received; last activity recorded shortly after.

3.  **Get Serviceable Area Journey Alert (April 1):** Dodla Gopi Krishna queried SLO V2 alert validation (~02:55 PM local time).
    *   *Status:* Thread active with ongoing verification by Sampada Shukla, Wai Ching Chan, and Akash Gupta.

4.  **High-Urgency Redis CPU Spike (March 30):** Kyle Nguyen reported `zs-fpon-prd-catalogue-service` hitting ~100% CPU in `asia-southeast1`.
    *   *Investigation Status:* Latency spikes from `go-catalogue-service` verified; latency normalized. No formal incident escalation required.

5.  **SLO Error Budget Alerts (March 31):** Sampada Shukla reported alerts regarding Fulfillment and Pricing tribes.
    *   *Status:* Acknowledged by Dodla Gopi Krishna; ongoing degradation in error budget consumption remains a concern.

**Pending Actions & Owners**
*   **Resolve P1 Incident IR-49:** Determine current status of "Picking list not available" breach and assign follow-up owner. *(Owners: Alvin Choo, Gopalakrishna Dhulipati, Maou Sheng Lee)*
*   **Validate Get Serviceable Area Alert:** Confirm accuracy of April 1 SLO V2 alert. *(Owners: Sampada Shukla, Wai Ching Chan, Akash Gupta)*
*   **Investigate Redis CPU Saturation:** Prioritize RCA for March 30 event. *(Owners: Daryl Ng, Gopalakrishna Dhulipati, Sneha Parab)*
*   **Address SLO Error Budget Alerts:** Prevent further depletion for Fulfillment and Pricing SLOs. *(Owner: Dodla Gopi Krishna)*
*   **Resolve Cluster Capacity Scaling:** Investigate March 23 memory limit failures. *(Owners: Kyle Nguyen, Nicholas Tan)*
*   **Restore Bastion Access:** Investigate PROD `asia-southeast1-c` inaccessibility. *(Owners: Nicholas Tan, Kyle Nguyen, Harry Akbar Ali Munir)*

**Decisions Made**
*   *Tentative:* Debate continues on Terraform-based change-freeze vs. direct Datadog UI management for on-call teams.
*   **QC Food Status:** Disabling confirmed on production (as of March 19); resource scale-down planning initiated pending ES confirmation.

**Key Dates & Follow-ups**
*   **April 2, ~03:36 UTC:** Maou Sheng Lee queried P1 incident IR-49 status; active breach noted.
*   **April 2, ~04:22 UTC:** Jazz Tong posted Terraform run `run-g4Lg24A7Y21cJzPQ`.
*   **April 1, ~05:16 AM:** Last reply recorded in SLO validation thread (8 unread messages).
*   **March 31, ~03:55 UTC:** Sampada Shukla reported SLO error budget alerts.
*   **March 30, ~03:00 UTC:** Redis CPU spike triggered; latency normalized.


## [31/38] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/8-Q3gLE8QP8 | Last Activity: 2026-04-02T03:58:51.220000+00:00 | Last Updated: 2026-04-02T06:43:59.904629+00:00
**Daily Briefing Update: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Lead/Coordinator.
*   **Andin Eswarlal Rajesh:** App Adoption Data.
*   **Onkar Bamane:** SKU/Data Operations.
*   **Gautam Singh:** Technical/Database Verification.
*   **Sneha Parab:** Data Enrichment & Stakeholder Management.
*   **Daryl Ng:** App Adoption.

**Main Topic**
Continued focus on the BCRS POS cutover, specifically SKU enrichment execution and database linkage validation. The group addressed the immediate execution of the SKU enrichment script for downloaded SKUs and confirmed resolution of specific missing linkage issues (SKUs 13280733, 13280736).

**Pending Actions & Owners**
*   **Gautam Singh:** Execute the SKU enrichment script for downloaded SKUs. Status: Assigned for execution by 14:00 on April 2, 2026 (confirmed via separate chat).
*   **Sneha Parab:** Await Gautam's update and request sharing of the Service Request (SR) draft for approval. Identify any blockers to proceeding with enrichment.
*   **Onkar Bamane:** Continue investigation into why 10 specific SKUs (13280794, 13280852, 13280864, 13281403, 13281448, 13281453, 13281688, 13281689, 13281710, 13281712) are not created in the DBP system. Confirm if data can be sent to FPON for the 361 SKUs with barcodes.
*   **Sneha Parab:** Obtain access to "BCRS - POS Cutover Plan.xlsx" and inform Jonathan Ho & Cheryl Ho upon completion of enrichment actions.
*   **Andin Eswarlal Rajesh / Daryl Ng:** Update app adoption numbers on the dashboard once current lag resolves (data reflects March 28).

**Decisions Made**
*   **Enrichment Execution:** Gautam Singh has confirmed readiness to execute the SKU enrichment script for downloaded SKUs today. The process is scheduled for completion by 14:00 on April 2, 2026.
*   **SR Approval Protocol:** Sneha Parab requires the SR from Gautam Singh prior to approval to ensure no blockers exist before proceeding.
*   **Technical Clarification:** SKUs **13280733** and **13280736** are confirmed as external to FPON scope; they should not exist in the internal database. This issue is closed.

**Key Data Points & Dates**
*   **Data Status (as of March 28):** Android adoption 75.6%; iOS adoption 86.38%.
*   **SKU Discrepancy:** Out of 837 newly created SKUs, barcodes exist for only 361. In the DBP system: Unique SKUs listed (361), Present in system (351), Active deposit linkages (349).
*   **Timeline Context:** Download scheduled for April 1, 2026. New discussion regarding script execution occurred on April 2, 2026 (03:56 – 03:58 UTC). Previous discussions spanned March 31 to April 1, 2026.

**Historical Context**
Previous actions regarding the 10 missing SKUs remain active pending investigation. The adoption timeline remains ~2 months to reach >95%, with growth slowing significantly after 85%. Gautam Singh has acknowledged the clarification regarding external SKUs in previous interactions.


## [32/38] [Prod Support] Offers
Source: gchat | Group: space/AAAAzZ3qkNU | Last Activity: 2026-04-02T03:48:03.820000+00:00 | Last Updated: 2026-04-02T06:44:29.176547+00:00
**Daily Work Briefing: [Prod Support] Offers**

**Key Participants & Roles**
*   **Willie Tan:** Reported initial issue (Mar 17) with offer visibility; escalated on Mar 26 regarding promo flow failure for specific SKUs.
*   **Angela Yeo:** Previously escalated discrepancy regarding incorrect promo display for SKU 13066243.
*   **Alvin Choo:** Previously flagged urgency and assigned owners for the initial case.
*   **Zaw Myo Htet & Daryl Ng:** Assigned to investigate both historical, new flow, and recent voucher issues.
*   **Neo Seng Ka:** Investigating database segment configuration (Mar 27).
*   **Tiffany Teo:** Raised query regarding [Drinks] Tier 1 - 4.4 Campaign [Unico] (Apr 2–8, 2026).
*   **Karen Chia:** Reported missing HPB voucher for customer e-wallet ticket #4446847; requested Zaw Myo Htet's assistance.

**Main Topic**
Investigation into production offer display errors and voucher availability spanning three distinct scenarios:
1.  **Historical Context (Mar 17–19):** Issues with Offer ID `sap offer 202603000112484` for **SKU 13066243**. The team confirmed "2 for $5.40" is the correct configuration, but it failed to display as expected while incorrect promotions were visible.
2.  **New Escalation (Mar 26):** Willie Tan reported that promos created in SAP are not flowing to FPON for a list of SKUs, despite items *not* being on the promo blacklist. A full investigation of the flow mechanism is required.
3.  **DBP Configuration Query (Mar 27):** Neo Seng Ka raised a query regarding DBP segment configuration ("union + dcc" logic), noting no results found when searching for "union."
4.  **Recent Voucher Issue (Apr 2):** Karen Chia reported a customer could not locate an HPB voucher in their e-wallet despite it being active and unexpired. This aligns with the broader flow/display investigation regarding SAP-to-FPON delivery.

**Pending Actions & Ownership**
*   **Action 1:** Investigate why correct offers ("2 for $5.40") are not displaying or if incorrect offers are showing for historical cases (SKU 13066243).
*   **Action 2:** Investigate the root cause of promo flow failure from SAP to FPON for SKUs not on the blacklist (Willie Tan, Mar 26).
*   **Action 3 (New):** Clarify DBP segment logic regarding "union + dcc" configurations and confirm why no applicable segments were found in the database.
*   **Action 4 (New):** Investigate missing HPB voucher for customer ticket #4446847; verify if the campaign logic or e-wallet sync is at fault.
*   **Owners:** @Zaw Myo Htet, @Daryl Ng (assigned to all issues). @Neo Seng Ka (DBP config). @Karen Chia/Willie Tan/Customer context for voucher case.
*   **Status:** Active/Urgent. Scope has expanded from single SKU display errors and DBP logic gaps to a systemic flow issue affecting multiple SKUs and live customer vouchers.

**Decisions Made**
No final technical fixes have been implemented yet. The team established the expected outcome for historical cases: offers must display "2 for $5.40." For the new SAP-to-FPON case, it is confirmed that affected SKUs should be eligible but are failing to receive promos. Neo Seng Ka's inquiry suggests a potential gap in DBP "union + dcc" segment logic contributing to flow failures. The HPB voucher incident (ticket #4446847) requires immediate validation of the campaign delivery mechanism for the [Drinks] Tier 1 - 4.4 Campaign period.

**Key Dates & Deadlines**
*   **Initial Issue Reported:** March 17, 2026 (09:01 AM).
*   **New Flow Issue Reported:** March 26, 2026 (02:24 AM UTC) by Willie Tan.
*   **DBP Query Raised:** March 27, 2026 (06:17 AM UTC) by Neo Seng Ka.
*   **New Voucher Report:** April 2, 2026 (approx. 4:00 AM UTC) regarding ticket #4446847.
*   **Campaign Period:** [Drinks] Tier 1 - 4.4 Campaign runs Apr 2–8, 2026.
*   **Deadline:** Immediate resolution requested for all display errors and voucher availability issues.

**Reference Links & IDs**
*   **Chat Space URL:** https://chat.google.com/space/AAAAzZ3qkNU
*   **Historical Offer ID:** `sap offer 202603000112484`
*   **Historical SKU:** 13066243
*   **Customer Ticket:** #4446847 (HPB Voucher issue)
*   **System Components:** SAP, FPON, DBP.


## [33/38] #dpd-dba
Source: gchat | Group: space/AAAAMh7T8Y0 | Last Activity: 2026-04-02T03:42:02.739000+00:00 | Last Updated: 2026-04-02T06:46:05.151650+00:00
**Daily Work Briefing: #dpd-dba (Updated)**

**Key Participants & Roles**
*   **Akash Gupta:** DBA Team Representative/Requestor.
*   **Wai Ching Chan:** Deployment Coordinator (Service Owner).
*   **Tiong Siong Tee:** Communication Initiator.
*   **Maou Sheng Lee:** Advisor.
*   **Gopalakrishna Dhulipati:** Primary DBA Contact (Active on recent urgent tickets and new incident).
*   **Saranga Colambage, Kim Tong Ng:** New responders to the password update request.
*   **Sampada Shukla, Hanafi Yakub, Dodla Gopi Krishna, Alvin Choo, Natalya Kosenko, Lester Santiago Soriano, Borja Adrian Dominguez:** DBA Team/Stakeholders.

**Main Topic**
The conversation covers executing critical Jira service tickets for production/pre-production updates (order zone IDs, picking zones) and investigating GKE Autopilot scale-down incidents. **New Focus:** An urgent incident regarding the WMS Integration deployment failure in Production due to a database password mismatch, requiring immediate secret rotation.

**Pending Actions & Owners**
*   **Fix Prod DB Secret (NEW URGENT):**
    *   **Action:** Update database password/secret for `wms-integration-app-user` in Cloud SQL Proxy to resolve "Access denied" errors.
    *   **Context:** WMS Integration deployment failed with Error 1045; incident referenced as follow-up to DSD-10589.
    *   **Owner:** DBA Team (Tagged: @Gopalakrishna Dhulipati, @Saranga Colambage, @Kim Tong Ng).
    *   **Status:** **Active Incident.** Reported Apr 2, 2026 at 03:42 UTC. Requires immediate secret rotation in `fpg-jarvis-prod`.
*   **Execute DSD-11124 Ticket (Pork Products):**
    *   **Action:** Insert new picking zone ("Pork products") into the picking service table for Prod and Pre-prod.
    *   **Owner:** DBA Team (@Gopalakrishna Dhulipati).
    *   **Status:** **APPROVED**. Submitted Mar 27 at 12:55 UTC; requires immediate execution.
*   **Approve URGENT Patch DSD-11122 & DSD-11119:**
    *   **Action:** Patch `orders` zone ID for specific statuses (non-COMPLETED/CANCELLED and general).
    *   **Owner:** DBA Team (@Gopalakrishna Dhulipati, @Alvin Choo, @Natalya Kosenko, @Akash Gupta).
    *   **Status:** Requires immediate approval; requested Mar 27.
*   **Execute DSD-11003 Ticket:**
    *   **Action:** Add `container_deposit` column to `order_service.order_items`.
    *   **Owner:** DBA Team (Akash Gupta).
    *   **Status:** Pending execution if not completed; initial request Mar 6.
*   **Investigate SLO Impact & Proxy Scale-Down:**
    *   **Action:** Investigate "bad connection" errors caused by `sqlproxy-prod-ap` GKE Autopilot scale-downs.
    *   **Owner:** @Gopalakrishna Dhulipati, @Dodla Gopi Krishna.
    *   **Status:** Reported Mar 25; critical SLO risk.

**Decisions Made**
*   `container_deposit` column (JSON, NULL default) to be added via transaction for DSD-11003.
*   Ticket DSD-11124 is approved and ready for execution.
*   Future requests must explicitly name the specific DB owner (per Maou Sheng Lee).
*   **New Decision:** Secret rotation for `wms-integration-app-user` is prioritized over standard deployment windows due to active production failure.

**Key Dates & Updates**
*   **Mar 6, 2026 (01:48 UTC):** Initial request for DSD-11003.
*   **Mar 9, 2026 (04:36 UTC):** Deployment window scheduled; script shared.
*   **Mar 25, 2026 (05:52 UTC):** SLO impact report regarding GKE scale-downs.
*   **Mar 27, 2026 (03:12–12:55 UTC):** Series of urgent tickets submitted and approved (DSD-11119, DSD-11122, DSD-11124).
*   **Apr 2, 2026 (03:42 UTC):** **New:** Akash Gupta reports WMS deployment failure in Prod due to DB password error; flags incident for immediate fix.

**References**
*   **Jira Tickets:** `DSD-11003`, `DSD-11119` (Urgent), `DSD-11122` (Urgent), `DSD-11124` (Approved), **New: DSD-10589** (Preceding incident context).
*   **Database:** `fpon.order_service.order_items`, Picking service tables, Cloud SQL (`wms-integration-app-user`).
*   **Affected Cluster:** `sqlproxy-prod-ap` (GKE Autopilot), `fpg-jarvis-prod`.
*   **Error Log:** Panic: "failed to ping database: Error 1045 (28000): Access denied for user 'wms-integration-app-user'".


## [34/38] RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU | Last Activity: 2026-04-02T02:37:49.662000+00:00 | Last Updated: 2026-04-01T06:45:51.125189+00:00
**Daily Briefing Summary: RMN Leadership Space (Updated Apr 1)**

**Key Participants & Roles**
*   **Bryan Choong:** Confirmed commitment to Saurabh regarding the **May 1 timeline** for delivering PLA Targeting and Uplift measurement. Disseminated an article from *The Drum* (Zitcha/Troy Townsend) on moving beyond ROAS in commerce media. Continuing preparation for Vipul's lunch with SPH CEO.
*   **Vipul:** Meeting SPH CEO next week to discuss revenue, agreements, and strategic propositions.
*   **Pauline Tan:** Leading "Product Launch Solution" inquiry (3 replies pending); investigating sampling spend.
*   **Rajiv Kumar Singh:** Coordinating SOAC planning; evaluating BCRS campaign digital screen placement options (dedicated vs. internal). Tasked with SPH radio insights and survey execution.
*   **Allen Umali:** Leading SignCloud cleanup; on MC. Requested allocation for BCRS campaign on Digital Screens starting today (Apr 1).
*   **Serene Tan Si Lin & Raymond Kam:** Sourcing THPZ Australia Fair intelligence and coordinating SPH news broadcast surveys, respectively.
*   **Emerald:** Developing playbook for campaign assets in the app.

**Main Topics**
1.  **PLA Targeting & Uplift Measurement:** Bryan Choong secured a verbal commitment from Saurabh to deliver PLA Targeting and Uplift measurement by **May 1**. Previous discussions concluded with a clear message that future conversations will focus solely on this timeline adherence.
2.  **BCRS Campaign Activation:** The BCRS campaign runs from Apr 1–Sep 30, 2026. Allen Umali requested a dedicated Digital Screen slot starting today (Apr 1). Rajiv Kumar Singh is evaluating whether to use a dedicated or internal slot based on launch capacity.
3.  **SPH Strategic Discussion:** Bryan Choong prepares briefing points for Vipul's upcoming lunch to address revenue performance, agreement timelines, and potential joint business plans. Key data points include 2024/2025 revenue and 2026 YTD figures for In-Screen Reselling and Radio.
4.  **Market Intelligence:** Shared *The Drum* analysis by Zitcha's Troy Townsend on the shift from ROAS to broader commerce media value.

**Pending Actions & Owners**
*   **PLA Targeting Delivery:** Ensure Saurabh meets the **May 1** commitment for PLA Targeting and Uplift measurement. *Owner: Bryan Choong.*
*   **BCRS Campaign Slot Allocation:** Decide if the BCRS campaign requires a dedicated Digital Screen slot or utilizes an internal slot. *Owner: Rajiv Kumar Singh, Bryan Choong.*
*   **SPH Revenue & Data Gathering:** Compile 2024/2025 revenue and 2026 YTD figures for In-Screen Reselling and Radio. *Owner: Team (Bryan, Rajiv, Raymond).*
*   **Agreement Terms Analysis:** Identify the specific offer declined by SPH in reselling and confirm the official end date of the current agreement (estimated Oct 2026). *Owner: Bryan Choong.*
*   **Radio Strategy & Survey:** Draft response for news broadcast updates; initiate customer survey planning with SPH. *Owner: Rajiv Kumar Singh, Raymond Kam.*
*   **Sampling Solution Investigation:** Obtain quotes from Grenadier and other agencies; analyze spend/traffic impact at THPZ. *Owners: Serene Tan Si Lin, Pauline Tan.*

**Decisions Made**
*   **SLA Enforcement:** Bryan Choong has established a hard deadline (May 1) for PLA Targeting delivery with Saurabh, limiting future discussions to commitment tracking.
*   **Survey Execution:** Formalize plan to conduct customer survey on news broadcasts in collaboration with SPH.
*   **Sampling Strategy:** Accelerate solution development; verify Grenadier quotes and explore alternatives for THPZ model.

**Key Dates & Deadlines**
*   **May 1, 2026:** Commitment deadline for PLA Targeting and Uplift measurement delivery (Saurabh).
*   **Next Week (Apr):** Vipul lunch with SPH CEO.
*   **Apr 1 – Sep 30, 2026:** BCRS Campaign duration (launching today).
*   **Oct 2026:** Estimated end date for current In-Screen Radio agreement.
*   **End of March:** Deadline to finalize SOAC targets.


## [35/38] D&T Funtastic Team
Source: gchat | Group: space/AAQARGCS1Wk/5YZW6i2wniE | Last Activity: 2026-04-02T02:07:15.235000+00:00 | Last Updated: 2026-04-02T02:37:32.835999+00:00
**Daily Work Briefing: D&T Funtastic Team**

**Key Participants & Roles**
*   **Trina Boquiren:** Initiator, project lead for the International Food Day eDM design selection. Recently issued an urgent deadline for voting and confirmed she will finalize and send out the event invite immediately upon closing votes.
*   **Team (@all):** Stakeholders responsible for reviewing options and casting votes.

**Main Topic**
Selection of the final email design (eDM) for the upcoming **International Food Day**. Trina presented three shortlisted design concepts to gather team consensus. The process has shifted from general voting requests to a strict deadline-driven selection.

**Pending Actions & Ownership**
*   **Action:** Submit votes for the top design options by **12:00 PM (local time) on April 2, 2026**.
*   **Owner:** All team members.
*   **Context:** Trina Boquiren sent a direct message at 02:07 UTC on April 2, 2026, stating: "Send in your votes by 12pm today as I'll be sending out the invite this afternoon." Immediate participation is required to finalize the design before the invitation dispatch.

**Decisions Made**
*   The final decision remains pending and is contingent upon votes received by the 12:00 PM deadline on April 2, 2026. Once the deadline passes and Trina confirms receipt of votes, she will proceed to send out the official event invite that afternoon.

**Key Dates & Follow-ups**
*   **Event:** International Food Day (Upcoming).
*   **Discussion Timeline:**
    *   **March 31, 2026:** Initial design posting occurred between 06:11 and 06:14 UTC; voting requested at 06:07 UTC.
    *   **April 1, 2026 (09:17 UTC):** Trina Boquiren issued a follow-up reminder to the @all channel urging immediate participation.
    *   **April 2, 2026 (02:07 UTC):** Trina Boquiren set a hard deadline of **12:00 PM today** for vote submission, linking completion directly to the afternoon distribution of event invites.
*   **Next Step:** Team members must vote before 12:00 PM on April 2. Post-deadline action is the dispatching of the final invite by Trina.

**Reference Data**
*   **Space URL:** https://chat.google.com/space/AAQARGCS1Wk
*   **Message Count:** 6 (Updated to reflect new reminder).
*   **Options Presented:** Option 1, Option 2, Option 3.


## [36/38] DPD AI Guild
Source: gchat | Group: space/AAQA5_B3lZQ/DIiDn7sJXrg | Last Activity: 2026-04-02T01:50:07.450000+00:00 | Last Updated: 2026-04-02T02:37:45.530915+00:00
**Daily Work Briefing: DPD AI Guild Chat Summary**

**Key Participants & Roles**
*   **Nicholas Tan:** Contributor; expresses skepticism regarding Microsoft Copilot's enterprise viability and legal posture.
*   **Maou Sheng Lee:** Contributor; agrees with critiques of corporate messaging and hypocrisy in AI usage terms.
*   *Note: No formal roles (e.g., Lead, Manager) are explicitly defined in the provided log.*

**Main Topic/Discussion**
The group discussed the legitimacy and safety of using **Microsoft Copilot** for work purposes, specifically analyzing its Terms of Service (TOS).
*   **Nicholas Tan** shared a link to the Microsoft Copilot TOS for individuals, characterizing the document's tone as overly cautious ("afraid") regarding potential AI errors. He labeled the tool a "toy" unsuitable for professional use and criticized Microsoft as a company that merely "piggybacked on OpenAI."
*   **Maou Sheng Lee** concurred, highlighting the contradiction in capitalists promoting public use of these tools while simultaneously shifting liability to users ("at own risks"). They described the corporate messaging as containing "never ending contradicting words."

**Pending Actions & Ownership**
*   **None identified.** The conversation is purely analytical and critical; no tasks, research assignments, or follow-up actions were assigned.

**Decisions Made**
*   **No formal decisions** were recorded in this thread. The participants collectively expressed a negative sentiment regarding the readiness of Microsoft Copilot for production work, but this remains an opinion rather than a ratified team decision.

**Key Dates & References**
*   **Date:** April 2, 2026 (Timestamps: 01:28 AM – 01:50 AM UTC).
*   **Resource Link:** https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/termsofuse
*   **Space URL:** https://chat.google.com/space/AAQA5_B3lZQ

**Summary Note**
The discussion reflects individual sentiment regarding AI tool maturity and legal risk mitigation strategies rather than operational coordination. No immediate action items require attention for the daily workflow.


## [37/38] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/1UILrDfoupI | Last Activity: 2026-04-02T01:31:46.818000+00:00 | Last Updated: 2026-04-02T02:38:23.365143+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Resource:** [Leads] (Ecom/Omni) Digital Product Development
**Date of Discussion:** April 1–2, 2026
**Participants:** Sneha Parab, Daryl Ng, Gopalakrishna Dhulipati, Andin Eswarlal Rajesh

**Key Participants & Roles**
*   **Sneha Parab:** Product/Functional Lead driving migration strategy and operational workflows.
*   **Daryl Ng:** Technical Lead providing feasibility assessments.
*   **Gopalakrishna Dhulipati:** Contributor offering account suspension strategy for specific segments.
*   **Andin Eswarlal Rajesh:** Stakeholder identified for UI/UX roadmap prioritization.

**Main Topic**
Strategies to prevent migrated customers from placing orders in the legacy B2B platform while retaining B2C access, and defining migration workflows for dual-channel users.

**Discussion Summary & Decisions**
*   **Initial Technical Feasibility (April 1):** Sneha Parab queried if selective blocking of B2B order placement was possible. Daryl Ng initially indicated full user blocking was technically infeasible due to shared login systems for B2C access.
*   **Risk Assessment:** Sneha Parab noted that removing payment methods is ineffective for customers using credit terms or gateways like "GE Biz" and "QuickBuy." The consensus shifted toward operational workarounds rather than strict technical blocking.
*   **New Strategy: Account Suspension (April 2):** Gopalakrishna Dhulipati proposed suspending accounts for users who do not place B2C orders. He noted that the initial migrated cohort consists primarily of schools, making this approach "safe to suspend."
*   **Data Verification:** Sneha Parab agreed to validate the number of customers who do not place B2C orders to determine the viability of suspension during gradual migration.
*   **Alternative Workflows (April 2):** If suspension is not feasible for specific users, Gopalakrishna outlined two options:
    1.  Alert Business and Operations teams to manually cancel legacy orders or redirect customers.
    2.  Enhance the current DBP system to support this logic (requiring roadmap prioritization).
*   **UX Intervention:** Sneha Parab announced a plan to implement a popup on the legacy B2B platform for migrated users, informing them to use the new portal with a CTA redirecting to the new site.

**Pending Actions & Ownership**
*   **Action:** Analyze and provide a list of customers who do not place B2C orders to assess suspension feasibility.
    *   **Owner:** Sneha Parab
*   **Action:** Prioritize roadmap efforts for two potential solutions:
    1.  Enhancing the DBP system to support migration logic.
    2.  Implementing the legacy portal popup with redirect CTA.
    *   **Owner:** Sneha Parab (aligned with Andin Eswarlal Rajesh)
*   **Action:** Prepare effort estimates for the DBP enhancement and roadmap submission.

**Key Dates & Follow-ups**
*   **Initial Discussion:** April 1, 2026.
*   **Strategy Update:** April 2, 2026 (Suspension proposal and UX popup planning).
*   **Next Milestone:** Immediate verification of the non-B2C customer list to finalize the migration approach for school accounts.

**Reference URLs**
*   Chat Space: https://chat.google.com/space/AAQAN8mDauE


## [38/38] DPD AI Guild
Source: gchat | Group: space/AAQA5_B3lZQ | Last Activity: 2026-04-02T01:28:01.028000+00:00 | Last Updated: 2026-04-02T02:38:56.895981+00:00
### Daily Work Briefing: DPD AI Guild

**1. Key Participants & Roles**
*   **Michael Bui:** Research/Technical Lead – Introduced the new model release.
*   **Zaw Myo Htet:** Technical Strategy/Engineering – Proposed optimization strategy and cost reduction.
*   **Nicholas Tan:** Strategic Monitor – Highlighted industry trends regarding AI executive automation (Meta) and recently critiqued consumer Copilot terms of service.
*   **Oktavianer Diharja:** Engineering Support – Suggested relevant Go skill utility libraries.

**2. Main Topic**
The discussion centered on leveraging **Mistral Small 4** to optimize local knowledge handling via quantization (Unsloth) to reduce RAG dependency, contextualized by Meta's "AI CEO" automation shift. On March 30, the conversation broadened to include engineering tooling (`samber/cc-skills-golang`). On April 2, Nicholas Tan introduced a critical risk assessment regarding consumer-grade AI assistants, citing Microsoft's restrictive Terms of Service as evidence of liability concerns in production environments.

**3. Pending Actions & Ownership**
*   **Action:** Evaluate feasibility of replacing heavy RAG pipelines with quantized open-weight models to reduce costs.
    *   **Owner:** Zaw Myo Htet
    *   **Context:** Requires further technical assessment based on Unsloth documentation.
*   **Action:** Investigate integration of Mistral Small 4's specific architecture (MoE, 119B total/6B active parameters) into current workflows.
    *   **Owner:** TBD (Team-wide due to recent announcement).
*   **Action:** Analyze the implications of Meta's "AI CEO" model on our autonomous agent roadmap.
    *   **Owner:** Nicholas Tan / Team
    *   **Context:** Assess if similar high-level executive automation patterns are applicable to DPD workflows given the efficiency gains in large-scale operations.
*   **Action (New):** Review Microsoft Copilot Terms of Service to define risk boundaries for internal AI usage.
    *   **Owner:** Nicholas Tan
    *   **Context:** Analyze the "toy" designation and liability clauses (https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/termsofuse) to determine why consumer tools are unsuitable for DPD work compared to our proposed autonomous agent stack.
*   **Action (Existing):** Evaluate utility of `samber/cc-skills-golang` for managing AI agent skills or context within Go-based infrastructure.
    *   **Owner:** Oktavianer Diharja / Engineering Team

**4. Decisions Made**
*   **Strategic Alignment:** The team acknowledged that while Mistral Small 4 offers specific architectural benefits for cost reduction, the broader industry (exemplified by Meta) is moving toward high-level autonomous agents. This suggests future DPD AI initiatives should balance model quantization with agent-based autonomy.
*   **Risk Assessment:** Nicholas Tan concluded that consumer-grade copilots are "toys not for work" due to restrictive legal frameworks and liability fears evident in Microsoft's Terms of Service. The team agreed to avoid relying on such tools for production workflows, reinforcing the need for custom-built solutions or strictly governed enterprise models.
*   **Tooling Consideration:** The `samber/cc-skills-golang` library has been flagged for potential use in standardizing skill management for Go-integrated agents, pending technical review by Oktavianer Diharja.

**5. Key Dates & References**
*   **2026-03-17:** Michael Bui announced the release of **Mistral Small 4**.
    *   *Specs:* MoE Architecture, 119B total parameters (6B active), 256k context window, Vision capability.
*   **2026-03-19:** Zaw Myo Htet suggested utilizing **Unsloth** for quantization to make open-weight models more cost-effective and reduce RAG reliance.
*   **2026-03-24:** Nicholas Tan shared an article detailing Mark Zuckerberg's launch of an AI CEO bot to manage Meta operations.
    *   *Relevance:* Highlights the maturity of agentic workflows for executive-level tasks.
*   **2026-03-30:** Oktavianer Diharja recommended the `cc-skills-golang` library for potential skill management integration.
*   **2026-04-02T01:28:01:** Nicholas Tan flagged Microsoft Copilot Terms of Service, labeling it a "toy not for work" due to liability concerns.
    *   *Reference:* https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/termsofuse

**Thread Status:** Active (Last reply noted 43 minutes ago relative to briefing generation).
