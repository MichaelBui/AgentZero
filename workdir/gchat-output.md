

## [1/30] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 16 | Last Activity: 2026-03-21T14:28:26.107000+00:00 | Last Updated: 2026-03-21T14:34:01.660860+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (March 21 Update)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
Service volatility persisted from the morning of March 21 (UTC+8) well into the afternoon. Following initial instability starting at **06:16 UTC**, a secondary wave emerged at **07:33 UTC**. The incident escalated into prolonged cyclic instability from **08:47 to 10:31 UTC**. Additional anomalies were detected between **13:57 and 14:28 UTC**, affecting `lt-gateway-app`, `frontend-gateway`, and `lyt-p13n-layout`.

**Status Summary & Timeline**
*   **06:16 – 10:31 UTC (Initial Prolonged Instability):**
    *   **Persona API Volatility:** `engage-my-persona-api-go` triggered high error rates (>0.1%) cyclically between 08:50 and 10:30 UTC.
    *   **Android Linkpoints:** `ef-android` view user linkpoint failures occurred at 08:47 (99.103% success) and 10:21 (99.283%). Owner: **Squad Compass**.
    *   **MyInfo Latency:** P90 latency spikes (>2s) detected at 09:56 and 10:02.

*   **13:57 – 14:28 UTC (Afternoon Recurrence):**
    *   **Campaign Request Latency:** `lt-gateway-app` (`get_/rms/me/campaigns`) P90 latency spiked to **1.282s** at **13:57**, recovering by 13:58. Owner: **Squad Dynamics**.
    *   **Persona API & Gamification Recurrence:** `engage-my-persona-api-go` error rates exceeded 0.1% again at **13:59**, **14:02**, and **14:07** (peaking at 0.108%). Concurrently, `gamification-api` triggered a high error rate alarm at **14:07** (Metric: 0.658%), recovering by 14:17. Owner: **Squad Dynamics**.
    *   **Frontend Gateway Latency:** `frontend-gateway` (`get_/api/layout/home/v2`) P99 latency exceeded 1.8s at **14:01** (Metric: 1.802), recovering by 14:02. Owner: **Squad Journey**.
    *   **Scratch Card Claims:** `lyt-p13n-layout` (`post_/v1/scan-door/scratch-cards/claim`) success rates dropped below 99.9% at **14:11** (98.182%) and again at **14:28** (97.561%). Owner: **Squad Journey**.

**Pending Actions & Ownership**
*   **Investigate `engage-my-persona-api-go` Cyclic Errors:** Address recurring high error rate triggers (>0.1%) observed in both the morning and afternoon sessions, including the peak at 14:28 (0.108%). Owner: **Squad Dynamics**.
*   **Resolve Gamification & Scratch Card Failures:** Investigate `gamification-api` spike (0.658% errors) and recurring success rate drops in scratch card claims (<97.6%) at 14:28. Owner: **Squad Dynamics** / **Squad Journey**.
*   **Analyze Frontend & Gateway Latency:** Review P90 latency spikes for campaign requests (1.282s) and P99 home page v2 latency (1.802s). Owner: **Squad Dynamics** / **Squad Journey**.

**Decisions Made**
The incident pattern has evolved from isolated incidents to a systemic, multi-service "sawtooth" instability spanning over eight hours with two distinct waves:
1.  **Cross-Service Dependency Failure:** Correlation persists between `engage-my-persona-api-go` errors and failures in `gamification-api`, `lt-gateway-app`, and `lyt-p13n-layout`, suggesting shared backend contention or resource exhaustion affecting both API layers and frontend RUM.
2.  **Broad Latency Threshold Breach:** Services beyond MyInfo (Campaigns, Home Page V2) are exhibiting critical latency degradation (>1.8s P99), indicating potential infrastructure-wide threading issues distinct from the initial error rate spikes.

**Key Dates & Follow-ups**
*   **Active Window:** March 21 (UTC+8), with persistent volatility extending through at least **14:28 UTC**.
*   **Reference Links:**
    *   Campaign Latency Monitor #17447551 (P90 spike: 1.282s)
    *   Gamification Error Monitor #92939290 (Peak error: 0.658%)
    *   Scratch Card Claims Monitor #20382861 (Lowest success: 97.561%)
    *   Frontend Home Page Monitor #17448327 (P99 spike: 1.802s)


## [2/30] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 32 | Last Activity: 2026-03-21T13:34:31.035000+00:00 | Last Updated: 2026-03-21T14:34:44.390647+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Update)**
**Date:** March 21, 2026 (Afternoon)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 250 (Updated from 234)

### Key Participants & Roles
*   **System/Tool:** Datadog App (Automated Monitoring)
*   **Notification Channel:** `@hangouts-ShoppingCartNotification`
*   **Ownership Teams:** `dpd-pricing`, `dpd-pricing-cart`.

### Main Topic
Instability in `frontend-gateway` and `st-cart-prod` persists. The situation is critical due to recurring latency spikes on Wish List writes/reads and new SLO failure alerts on Cart updates (`post_/cart`). The **P2 Error Budget Alert** remains active, with the 7-day budget now at **70.086%** consumed (updated from 94.99% historical context; current alerts indicate sustained burning).

### Incident Timeline & Actions
**Morning History (Context)**
*   *See original summary for 03:01–10:26 UTC+8 activity regarding `frontend-gateway` latency and initial cart spikes.*

**Mid-Day Escalation (New Activity)**
*   **11:13 UTC:** Monitor `22710472` triggered. Cart success rate dropped to **99.823%** (< 99.9% threshold). Recovered at 11:23 (Value: 100.0%).
*   **11:16 UTC:** **P2 Error Budget Alert** fired (`slo_pricing_sng_post_cart`).
*   **12:10–12:18 UTC:** Rapid oscillation on Cart success rate:
    *   Triggered at 12:10 (Value: 99.9%), Recovered at 12:15 (Value: 99.902%).
    *   Re-triggered at 12:16 (Value: 99.896%), Recovered at 12:18 (Value: 100.0%).
*   **13:00 UTC:** `frontend-gateway` P90 latency on `put_/api/product/_id/wish-list` exceeded 5s (Value: 5.336s). Recovered at 13:03.
*   **13:24–13:34 UTC:** Concurrent Spike Cluster:
    *   **Wish List Reads:** P99 on `get_/api/wish-list/_id` exceeded 3.1s (Value: 3.15s). Recovered at 13:34.
    *   **Wish List Writes:** P99 on `put_/api/product/_id/wish-list` exceeded 6s (Value: 7.389s). Recovered at 13:29.
    *   **Read Jitter:** P90 on `get_...` exceeded 1.7s (Value: 1.775s). Recovered at 13:28.

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** **P2 Error Budget Alert** triggered again at 11:16 and 12:13 UTC. The pattern of rapid trigger/recovery cycles (12:10–12:18) confirms auto-healing is insufficient.
*   **Scope:** Investigation must correlate Event ID `8553648825556588478` (latest 13:34 recovery) with the 11:13 and 12:10 Cart success rate drops. Determine if `st-cart-prod` failures are driving the `frontend-gateway` latency cascade observed at 13:00–13:34.

### Decisions Made
*   **Priority Escalation:** Status remains **"Critical Incident"**. The recurrence of P2 Error Budget Alerts (Monitor ID `21245796`) and sub-99.9% success rates on Cart updates indicates a systemic degradation, not isolated latency.
*   **Focus Shift:** Immediate analysis required for the 13:00–13:34 window to identify if shared dependency failures (e.g., database or caching layers) are causing simultaneous degradation across `st-cart-prod`, Wish List writes, and reads.

### Key Dates & Follow-ups
*   **Critical Window:** Extended activity from March 20, 17:45 UTC through at least March 21, 13:34 UTC.
*   **Follow-up:** Investigate the latest Event ID `8553648825556588478` and correlate with the Cart SLO failure events (Event IDs `8553509591075940205`, `8553566967588704768`).

**References:**
*   **Active Monitors:** `22710472` (Cart Success Rate), `21245796` (SLO Error Budget), `21245701/21245706` (Write Latency), `21245720/21245725` (Read Latency).
*   **Service Tags:** `service:frontend-gateway`, `service:st-cart-prod`, `team:dpd-pricing`.


## [3/30] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Messages: 3 | Last Activity: 2026-03-21T13:14:22.650000+00:00 | Last Updated: 2026-03-21T14:35:21.625451+00:00
# Daily Work Briefing: #dd-fpg-watchdog-alert

### Key Participants & Roles
*   **Datadog App:** Automated monitoring system.
*   **@hangouts-dd-dpd-watchdog-alert:** Targeted notification channel.
*   *Note: Interactions remain purely automated.*

### Main Topic
The channel tracks **P3 [DPD Watchdog] infrastructure incidents** in Production. Logs show recurring transient issues (excluding `tcp_retrans_jump` and `full_disk_forecast`) aggregated by `story_key` over a 30-minute window.

### Incident Summary & Status Update
**Historical Resolved Incidents:**
1.  **Mar 05–17:** 11 distinct events triggered and recovered within the period (e.g., Mar 16 duration ~3h, Mar 17 Afternoon duration ~4h). Full list remains consistent with previous records.
2.  **Mar 18/19:** Incident `story_key`: `10aaf170-dac2-5fec-97bf-cfd442f8706b`. Triggered Mar 18 22:14 UTC, Recovered Mar 19 ~03:37 UTC. Duration ~5.6 hours. Status: **Resolved**.

**New Incident Resolved:**
*   **Date:** March 20, 2026.
*   **Incident ID (`story_key`):** `2787bcd7-d59e-58f0-961a-8f578260cd84`.
*   **Triggered:** Mar 20, 05:14 UTC.
*   **Recovered:** Mar 20, 09:37 UTC.
*   **Status:** **Resolved**.
*   **Duration:** ~4.4 hours (consistent with historical averages).

**Current Status Update (New):**
*   **Date/Time:** March 21, 2026, at 13:14 UTC.
*   **Incident ID (`story_key`):** `41621369-8f6a-58df-b6a8-5e7c89d60ae6`.
*   **Status:** **[Triggered]** (Active).
*   **Alert Message:** "Datadog is unable to process your request."
*   **Severity:** P3.

### Pending Actions & Ownership
*   **Immediate Action:** Investigate the active trigger on March 21 (`story_key`: `41621369-8f6a-58df-b6a8-5e7c89d60ae6`). The specific error message "Datadog is unable to process your request" suggests a potential ingestion or processing failure within the monitoring system itself, rather than just an infrastructure alert.
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Investigation Note:** Recurrence continues (Mar 17, Mar 18/19, Mar 20, and now Mar 21). The latest trigger occurs shortly after the previous resolution window. The error message requires immediate verification to ensure the watchdog mechanism is functioning correctly.

### Decisions Made
*   None recorded yet. Pending investigation into the "unable to process" error on March 21.

### Key Dates & Follow-ups
*   **Latest Event:** March 21, 2026, at 13:14 UTC (New Trigger).
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Monitor for recovery. If the error persists or resolution times exceed averages, escalate to SRE/Platform Engineering to investigate Datadog ingestion pipelines.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Datadog Monitor Link:** [View in Datadog](https://app.datadoghq.eu/monitors/17447511)
*   **New Incident (Mar 20):** https://app.datadoghq.eu/monitors/17447511?group=story_key%3A2787bcd7-d59e-58f0-961a-8f578260cd84&from_ts=1773982671000&to_ts=1773983871000&event_id=8551695889001406368
*   **Recovered Link (Mar 20):** https://app.datadoghq.eu/monitors/17447511?group=story_key%3A2787bcd7-d59e-58f0-961a-8f578260cd84&from_ts=1773998451000&to_ts=1773999651000&event_id=8551960641901155525
*   **Active Incident (Mar 21):** https://app.datadoghq.eu/monitors/17447511?group=story_key%3A41621369-8f6a-58df-b6a8-5e7c89d60ae6&from_ts=1774097871000&to_ts=1774099071000&event_id=8553628622588111192

### Monitor Configuration
*   **Query:** `events("source:watchdog (story_category:infrastructure -story_type:(tcp_retrans_jump OR full_disk_forecast)) env:(PROD OR production OR prod)").rollup("count").by("story_key").last("30m") > 0`


## [4/30] [Prod Support] Ecom FFS Ops
Source: gchat | Group: space/AAAAde_cYKA | Messages: 2 | Last Activity: 2026-03-21T12:57:19.993000+00:00 | Last Updated: 2026-03-21T14:35:54.510594+00:00
**Daily Work Briefing: [Prod Support] Ecom FFS Ops**

**Key Participants & Roles**
*   **Wai Ching Chan / Sampada Shukla:** Operations/Product Leads.
*   **TL HCBP FFS, TL - HGPT FFS, TLEPT FFS, Harry Akbar Ali Munir:** Store/Regional Team Leads reporting blockers.
*   **Adrian Yap Chye Soon:** Technical Lead/Support (investigating data anomalies).
*   **Akash Gupta:** DPD / Fulfilment / On Call (Source of new alert).

**Main Topics**
1.  **Packlist Discrepancies & Validation:** Ongoing investigation into orders with critical `packed_qty` anomalies (NULL values or massive mismatches vs. `delivered_qty`).
    *   **New Critical Incident (Mar 21):** Order #22870202 at Hyper Changi (Store ID 45) shows status `RECEIVED` but `packed_quantity` is NULL. Delivery date: Mar 21, 2026, 10:00 AM. Reported by Akash Gupta to Adrian Yap Chye Soon.
    *   **Re-Confirmed Incident (Mar 21):** Order #22839804 at Hyper Sports Hub (Store ID 17) confirmed with NULL `packed_quantity` despite `RECEIVED` status. Prior noted delivery date was Mar 20; current check confirms ongoing issue. Reported by Harry Akbar Ali Munir.
    *   **New Critical Incident (Mar 19):** Order #22862214 at Hyper Parkway (Store ID 186) shows `packed_qty` of 13,053,078 vs. `delivered_qty` of 1. Reported by Harry Akbar Ali Munir; flagged for TL HPWP FFS investigation.
    *   **Historical Context:** Previous Mar 18 incident at Hyper Hougang (Order #22828448) and Mar 14 incident at Orchid Country Club remain reference points.

**Pending Actions & Ownership**
*   **Critical Data Validation (New - Mar 21):**
    *   *@Yap Chye Soon Adrian:* Confirm NULL `packed_quantity` for Order #22870202 (Hyper Changi) and re-verify Order #22839804 (Hyper Sports Hub). Immediate response required from Akash Gupta's query.
    *   **Investigation Required:** Check Order #22862214 (Hyper Parkway) where `packed_qty` vastly exceeds `delivered_qty`.
*   **Critical Order Validation (Historical):**
    *   *TL - HGPT FFS:* Continue investigation into Order #22828448 (Hyper Hougang).
    *   *Adrian Yap Chye Soon:* Review packlist NULL issue for Order #22789688 (Orchid Country Club).
*   **Order Validation (Packlist Discrepancies):**
    *   *TL HSPH FFS:* Confirm packlists for Orders #22738044, #22754559, #22780412.
    *   *TL OCCL2 FFS:* Double-confirm Orders #22756415 and #22752129 (Mar 11).
    *   *TL HPWP FFS:* Confirm packlist for Order #22786748; investigate discrepancy in Order #22781194.
*   **System Fixes:**
    *   *TL HCBP FFS:* Resolve Order #256307387 stuck in "pending" status.

**Decisions Made**
*   **App Release Strategy:** Picker App 10.4.0 rollout remains on hold pending resolution of critical data anomalies (Mar 18–21). Full rollout contingent on stability post-fixes, specifically addressing the new Mar 21 NULL quantity alerts.

**Key Dates & Deadlines**
*   **Immediate:** Validation of Mar 21 incidents at Hyper Changi and Hyper Sports Hub; investigation into Mar 19 anomaly at Hyper Parkway.
*   **Pending:** Re-evaluation of Picker App 10.4.0 release timeline once data integrity is restored across all reported stores (HSPH, HPWP, HC).

**Critical Alerts**
*   **New Alert (Mar 21, 12:57 PM):** Two critical anomalies detected today. Akash Gupta flagged Order #22870202 (Hyper Changi) with NULL `packed_quantity` and `RECEIVED` status, requesting immediate confirmation from Adrian Yap Chye Soon.
*   **Ongoing Alert:** Persistent NULL `packed_qty` issues across Hyper Sports Hub and Hyper Changi; massive data mismatch at Hyper Parkway (13M+ packed vs 1 delivered).


## [5/30] FPG Everyone - General
Source: gchat | Group: space/AAAAjDYVcBU | Messages: 3 | Last Activity: 2026-03-21T12:24:53.064000+00:00 | Last Updated: 2026-03-21T14:36:33.526137+00:00
**Daily Work Briefing: FPG Everyone Chat Summary (Updated)**
**Date Range:** March 3 – March 21, 2026
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
*   **Day of Service Registration (Owner: All Staff):** Join the "Willing Hearts Kitchen Crew" on March 27, 2026 (1:00 PM – 5:00 PM) to help prep/pack 3,000 meals. Only 20 spots available. Register at `https://forms.gle/Y4B22gtUmU7SF42V6`.
*   **Sensory Test Sign-ups (Owner: All Staff):** Chapati screening form remains open (`https://forms.gle/DFYrahZcvhtcoJ9R7`). Frozen Snacks sign-up is closed.
*   **Wellness Engagement:** Visit Unity stores for deals before Mar 25 or explore https://go.fpg.sg/WOHD.
*   **Social Engagement:** Watch the "Bowl of Love" finale on TikTok (`https://vt.tiktok.com/ZSusN9b4n/`) to see the conclusion featuring fresh pork from Malaysia.

### Critical Dates & Deadlines
*   **March 6:** End of Foaming Hand Soap offer (Completed).
*   **March 8:** International Women's Day Celebration (Completed).
*   **March 12:** Non-Halal Soup Sensory Evaluation (Completed).
*   **March 16–30:** Cardless access rollout phases.
*   **March 17:** Frozen Food/Nuts session (Status: Pending confirmation/overshadowed).
*   **March 18–19:** Frozen Snacks Sensory Evaluation (Completed).
*   **March 21:** "Bowl of Love" finale episodes live on TikTok.
*   **March 22:** FairPrice Walnuts with Cranberries redemption ends.
*   **March 25:** World Oral Health Day offers expire at Unity stores.
*   **March 27 (Friday):** Day of Service at Willing Hearts Kitchen.

### Decisions Made
*   No formal strategic decisions recorded; focus remains on correcting Cardless Access communication, recruiting panelists for Frozen Snacks/Chapati testing, promoting the "Bowl of Love" microdrama collaboration (now complete with finale release), supporting World Oral Health Day initiatives via Unity stores (extended to Mar 25), and coordinating the March 27 Day of Service event.


## [6/30] [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Last Activity: 2026-03-21T04:32:34.437000+00:00 | Last Updated: 2026-03-21T05:00:39.207120+00:00
**Daily Work Briefing: [Prod Support] Marketplace**

**Key Participants & Roles**
*   **Support/Operations:** Willie Tan, Iris Chang, Lalita Phichagonakasit, Charlene Tan, Jie Yi Tan, Ayton See, Amos Lam.
*   **Technical/Admin Team:** Dang Hung Cuong, Shiva Kumar Yalagunda Bas (Frequent recipients of access/access issues), Olivia -, Jill Ong, Greta Lee, Zaw Myo Htet, Angella Yeo, Cassandra Thoi, Gopalakrishna Dhulipati.

**Main Topics & Discussion Summary**
The conversation covers critical operational blockers regarding seller onboarding, order fulfillment discrepancies, system configuration errors, urgent promotion removal requests, and new order inquiries. Major themes include:

1.  **Access Management:** Requests to grant "PickerApp" access for new/existing sellers (Meat Affair, Old Shanghai, BulkMartGo, PETS STATION HOLDING). Charlene Tan reported a new seller (Woah Group) encountering errors under the "Offers" section.
2.  **Sales Data & Reporting:** Issues with vendors (CoLab Apac, Old Shanghai) not receiving sales breakdown reports since inception.
3.  **Promotion & Pricing Conflicts:**
    *   **Urgent Removal Request:** Lalita Phichagonakasit (Mar 20) reported an incorrectly set up promotion for **Item ID: 90244361** requiring immediate removal from the backend to prevent financial loss. This follows previous reports of stuck frontend states and expired promotions lingering on Mirakl.
    *   Conflicting promotions for "Falcon Galaxy Strong Garbage Bag" require one to be disabled.
    *   Discount prices not showing despite SKU publication.
4.  **Fulfillment & System Errors:**
    *   Delivery slot display discrepancy for seller "Funa Artistic Hampers & Gifts" (Mar 19): Mirakl shows 91h vs Frontend date; focus remains on a window duration issue showing 4 days instead of the expected 2 days.
    *   Missing items in PickerApp compared to email picklists (Atasco Dairy, Estalife).
    *   Orders completed without delivery by NJV (Order #246974265, #248270820).
    *   Seller description/image updates not triggering "Pending Verification" status.
5.  **New Listing & Logic Queries:**
    *   **Item Visibility:** Lalita Phichagonakasit reported SKU **13226899** failing to appear under postal code **762115** since March 14th, despite prior online availability.
    *   **Picklist Logic (New):** Amos Lam (Mar 21) raised a critical issue where a vendor who opted out of public holidays in December did not receive a pick list today. This requires immediate investigation into why the system failed to generate a list for an opt-out status.
6.  **SAP Configuration Inquiry:** Iris Chang queried the definition and data source of "Lead Time" within SAP T-code ZMP_VENDOR on Mar 18.
7.  **Order Status Inquiry (New):** Angela Yeo (Mar 21) raised a query regarding FFS orders for seller **Yumsay Food**, seeking technical team advice.

**Pending Actions & Ownership**
*   **Urgent Promotion Removal:** Dang Hung Cuong and Gopalakrishna Dhulipati to immediately remove incorrectly set up promotion for Item ID: 90244361 (Lalita Phichagonakasit request, Mar 20).
*   **Picklist Generation Failure (New):** Technical team (Dang Hung Cuong, Shiva Kumar Yalagunda Bas) to investigate why a vendor who opted out of public holidays in December did not receive a pick list today (Amos Lam, Mar 21).
*   **FFS Order Inquiry:** Technical team to investigate FFS order status for seller "Yumsay Food" (Angela Yeo, Mar 21).
*   **Close DF SOF Order:** Willie Tan requested closure; tracking via DST-2578 (Owners: Dang Hung Cuong, Shiva Kumar Yalagunda Bas).
*   **Vendor Report Issues:** Investigate missing sales breakdown reports for CoLab Apac (NED-277148) and Old Shanghai (NED-277329).
*   **Access Grants:** Grant PickerApp access to Meat Affair, BulkMartGo, PETS STATION HOLDING, and others. Resolve Woah Group "Offers" error (Charlene Tan).
*   **Fulfillment Investigation:** Check why Estalife missing Final Picklist PFC; investigate delivery slot display for Funa Artistic Hampers & Gifts (4 days vs 2 days expected); determine trigger for NJV non-delivery completions.
*   **System Logic & Listing Fixes:** Investigate missing SKU 13226899 listing for postcode 762115; clarify picklist generation logic for postponed orders. Resolve SAP ZMP_VENDOR Lead Time definition (Dang Hung Cuong/Amos Lam).

**Decisions Made**
*   Dang Hung Cuong is prioritizing the removal of Item ID: 90244361, the new picklist failure issue raised by Amos Lam, and the Woah Group offers error. Dang Hung Cuong and Shiva Kumar Yalagunda Bas are assigned to investigate the vendor picklist anomaly. Ayton See previously educated a seller on promotion setup rules after identifying a configuration error.

**Key Dates & Deadlines**
*   **2026-03-21 (Today):** Angela Yeo requested advice on FFS orders for "Yumsay Food" (Last reply 3 min ago). Amos Lam reported the vendor picklist failure due to public holiday opt-out status. Previous urgent request to remove Item ID: 90244361 remains active from Mar 20.
*   **2026-03-19 (Yesterday):** Jie Yi Tan reported Funa Artistic Hampers & Gifts delivery window discrepancy; discussion ongoing with 34 replies.
*   **2026-03-18:** Iris Chang inquired about SAP T-code ZMP_VENDOR "Lead Time" definition.
*   **2026-03-03:** DF SOF order request raised.
*   **December 2025 (Historical Context):** Vendor involved in Amos Lam's query opted out of public holidays.


## [7/30] BCRS ECOMM SAP POSTING
Source: gchat | Group: space/AAQA-ICuJRM | Last Activity: 2026-03-21T04:14:49.285000+00:00 | Last Updated: 2026-03-21T05:01:17.257876+00:00
**Daily Work Briefing: BCRS ECOMM SAP POSTING & Refunds UAT (Mar 21 Update)**

**Key Participants & Roles**
*   **Dany Jacob:** Project Lead/Coordinator.
*   **Yaxin Hao / Jianbin Huang (DBP Team):** Technical owners for SAP data processing and uploads.
*   **Hendry Tionardi / Michael Bui / Tan Gay Lee:** Finance/UAT testers verifying order postings.
*   **Onkar Bamane / Prajney Sribhashyam:** Stakeholders managing UAT validation, coordination (PSR/Data8), and environment access.
*   **Wei Fen Ching:** Accounting verification lead.
*   **Lai Shu Hui:** Requester for Blackoffice/Zendesk UAT access; review of test cases and sign-off.
*   **Pazhanisamy Harish Prabhu:** IT Ops providing Zendesk sandbox credentials.
*   **Sathya Murthy Karthik:** Coordinated invoice updates, testing closure, and Refunds UAT sign-off.
*   **De Wei Tey:** Provided B2B credit note examples and confirmed refund status for order 75567408.

**Main Topic**
UAT testing for BCRS E-commerce involving Sales Posting to SAP (F420) and Refunds UAT. Focus has shifted from initial invoice validation to finalizing end-to-end refund scenarios, including specific deposit refunds and pending test cases requested by Lai Shu Hui. Attention is now turning toward the next phase of BCRS Deposit posting UAT.

**Status of Issues & Updates**
*   **Refunds Testing (Mar 21):** On March 21, Prajney Sribhashyam placed order **#75570370** under the `daryl.ng+bcrs2@fairpricegroup.sg` account to test a specific refund flow. This scenario covers auto-refunds (<$20) involving BCRS deposits where no container or SKU return is required.
*   **Test Case Review:** Lai Shu Hui acknowledged requests for time to review existing cases and reiterated the need for two additional scenarios: 1) Refund of item + cart discount, and 2) Customer refund via CS without a return bottle.
*   **SAP Finance Changes:** Onkar Bamane noted that upon completion of the BCRS Deposit posting UAT sign-off, SAP Finance has identified required changes that need deployment.

**Pending Actions & Ownership**
1.  **New Refund Scenario Execution:** Test the refund flow for order #75570370 (BCRS deposit, auto-refund < $20, no return) as requested by Prajney Sribhashyam. **(Owner: Testing Team / Onkar Bamane)**.
2.  **Additional Test Cases:** Sathya Murthy Karthik/Prajney Sribhashyam to provide the two specific scenarios requested by Lai Shu Hui: (1) Refund of item and cart discount, and (2) CS refund handling without a return bottle. **(Owner: Sathya Murthy Karthik / Prajney Sribhashyam)**.
3.  **Test Case Review:** Lai Shu Hui to finalize review and sign-off pending the provision of new test cases. **(Owner: Lai Shu Hui / Finance Team)**.
4.  **SAP Deployment Prep:** Prepare for SAP Finance changes required post-Deposit UAT sign-off. **(Owner: Onkar Bamane / DBP Team)**.

**Decisions Made**
*   Confirmed that end-to-end testing is mandatory before Finance can sign off.
*   B2C credit notes are generated in SAP but typically not printed; sample document 0900169572 was previously identified for validation.
*   **New:** A specific test case for BCRS deposit auto-refunds (Order #75570370) has been initiated to cover the < $20 threshold without return requirements.
*   Target to finish current testing by 5:30 PM on March 20 remains as context; new activities are scheduled for March 21.

**Key Dates & Follow-ups**
*   **Mar 9:** Manual file upload completed.
*   **Mar 20 (15:00 PM):** Lai Shu Hui requested time to review and asked for two specific additional test cases.
*   **Mar 21 (03:53 UTC):** Prajney Sribhashyam initiated testing on order #75570370 for BCRS deposit refund flow.
*   **Mar 21 (04:14 UTC):** Onkar Bamane flagged upcoming SAP Finance changes contingent on Deposit UAT sign-off.

**Immediate Follow-up:** Execute the new deposit refund test for order #75570370, provide the two additional test cases to Lai Shu Hui for review, and coordinate the deployment of SAP Finance changes once Deposit UAT is signed off.


## [8/30] RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Last Activity: 2026-03-21T03:20:45.163000+00:00 | Last Updated: 2026-03-21T05:02:23.239497+00:00
**Daily Work Briefing: Automated Test Results Summary (RMN Notification)**

**Key Participants & Roles**
*   **Collection Runner App:** Automated testing agent executing API suites.
*   **Webhook Bot:** Reporting mechanism; consistently returning "unable to process your request" on all notifications.
*   **Parties Involved:** No human participants engaged; system-generated notification log.

**Main Topic/Discussion**
The conversation comprises automated notifications from the Collection Runner regarding nightly API test executions across `promo-service`, `marketing-personalization-service`, and `marketing-service` in the **staging** environment. Logs track "API Tests" and "API Contract Tests." New entries cover a run on **March 21, 2026**, at **03:20 UTC**, extending the monitoring period previously ending late March (01:05/02:31 UTC).

**Test Execution Status & Anomalies**
*   **Stable Services:**
    *   `promo-service`: Previously confirmed stable on March 21 at 02:31 UTC.
    *   `marketing-personalization-service`: New data from **March 21, 2026, at 03:20 UTC** confirms stability with zero failures.
        *   **API Tests:** 96 Passed / 0 Failed / 0 Skipped (Total Requests: 21).
        *   **Contract Tests:** 126 Passed / 0 Failed / 0 Skipped (Total Requests: 21).
*   **Persistent Failures (`marketing-service`):**
    *   The pattern of **2 recurring API test failures per run** persists on **March 21, 2026**.
    *   **Recurring Failures:** Observed on every run from March 17 through **March 21**:
        *   **Mar 21 (01:05 UTC):** 50 Passed / **2 Failed** (API Tests). Total Requests: 17.
        *   Previous dates (Mar 17–20): Consistently showed 50–51 Passed / **2 Failed**.
    *   **Contract Tests:** `marketing-service` contract tests remain stable with a 100% pass rate on March 21 at 01:05 UTC (**20 Passed / 0 Failed / 0 Skipped**).

**Pending Actions & Ownership**
*   **Investigate Persistent `marketing-service` Failures:** The root cause for the consistent 2 API test failures observed daily from March 17 through **March 21, 2026**, remains unaddressed. Engineering teams must review failure reports immediately.
*   **Webhook Bot Remediation:** The bot failed to process requests in every notification cycle from March 12 through at least **March 21, 03:20 UTC** (including the latest log). Immediate attention is required from DevOps or Automation Infrastructure.

**Decisions Made**
*   No human decisions recorded; all entries are automated system outputs.

**Key Dates & Deadlines**
*   **Failure Window (Historical):** Instability noted on March 12 and 13.
*   **Current Failure Window:** The service has been failing consistently since **March 17, 2026**, continuing through **March 21, 2026**.
*   **Monitoring Period:** Data covers runs from **March 12, 2026**, through **March 21, 2026** (spanning 01:05 UTC, 02:31 UTC, and 03:20 UTC execution windows).
*   **Next Steps:** Immediate investigation into the `marketing-service` API flakiness and Webhook Bot connectivity issues.


## [9/30] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Last Activity: 2026-03-21T00:59:10.091000+00:00 | Last Updated: 2026-03-21T02:08:46.969727+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Mar 21, 09:30 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-discovery`.
*   **Escalations:** `@hangouts-GT-Search-DatadogAlerts`, `@oncall-dpd-staff-excellence-pdm`, `@hangouts-GT-Discovery-DatadogAlerts`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Search Indexing, QC Layout Service, SAP Data Sync, Catalogue Service.

**Main Topic**
**CRITICAL ALERT (P2):** The `fp-search-indexer` service remains in a **P2 Error State** on production. New transient alerts have triggered and resolved; however, the unresolved P2 error state from Mar 18 persists as the highest priority.

**Pending Actions & Ownership**
*   **Action:** **URGENT INVESTIGATION:** Address critical errors on `fp-search-indexer` (env: prod).
    *   **Owner:** Product Data Management On-Call (`@oncall-dpd-staff-excellence-pdm`).
    *   **Status:** Active since Mar 18; re-triggered Mar 19, 15:35 UTC. No resolution achieved.
    *   **Required Checks:** Review Datadog logs, inspect K8s deployment (`fpon-cluster/default/fp-search-indexer`), consult Runbook (Jira SR-2001831558).

*   **Action:** Investigate `qc-layout-service` latency spikes.
    *   **Owner:** Product Data Management Team (`@hangouts-dd-dpd-grocery-alert`).
    *   **Status:** Triggered Mar 20, 00:24 UTC (P99 > 1.8s @ 2.381s; P90 > 1.1s). No recovery status noted in logs yet.
    *   **Context:** High latency on food product listing requests (`get_/v1/pages/plp`).

*   **Action:** Monitor `sku-store-attribute` job stability.
    *   **Owner:** DPD Grocery Discovery Team (`@hangouts-dd-dpd-grocery-alert`).
    *   **Status:** Triggered Mar 20, 00:59 UTC (<6 files in 4h); **Recovered** at Mar 21, 00:59 UTC. Monitor for recurrence of low file counts.

*   **Action:** Investigate SAP Data Sync volume anomalies.
    *   **Owner:** Product Data Management Team (`@opsgenie-dpd-grocery-discovery`).
    *   **Status:** Triggered Mar 20, 01:01 UTC (P3). Alerts indicate >2000 files received/stored per day for `fpon-sap-jobs-file-parser`.

*   **Action:** Monitor `go-catalogue-service` latency.
    *   **Owner:** Discovery Team (`@hangouts-GT-Discovery-DatadogAlerts`).
    *   **Status:** Triggered Mar 20, 08:51 UTC (P90 > 2.0s @ 4.005s); **Recovered** at Mar 20, 09:27 UTC (Value: 0.675s).

**Decisions Made**
*   The `fp-search-indexer` failure is confirmed persistent; previous "resolved" status was invalid.
*   Transient P3 issues (`sku-store-attribute`, `go-catalogue-service`) have self-resolved but require continued monitoring for flapping patterns.
*   New latency alerts on `qc-layout-service` and volume spikes in SAP ingestion are active and require immediate log review.

**Key Dates & Follow-ups (Mar 16–21, 2026)**
*   **Service: `fp-search-indexer` (P2 - Product Data Management) [ACTIVE CRITICAL]**
    *   *Latest Timeline:* Active since Mar 18; re-triggered Mar 19, 15:35 UTC.
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/17447691) | [Runbook](https://ntuclink.atlassian.net/wiki/spaces/SR/pages/2001831558/Support+Run+book).
*   **Service: `qc-layout-service` (P3 - Product Data Management) [ACTIVE]**
    *   *Issue:* PLP request latency (P99 > 1.8s, P90 > 1.1s).
    *   *Latest Timeline:* Triggered **Mar 20, 00:24 UTC**.
    *   *Links:* [Monitor 20382947](https://app.datadoghq.eu/monitors/20382947) | [Monitor 20382948](https://app.datadoghq.eu/monitors/20382948).
*   **Service: `sku-store-attribute` (P3 - Grocery Discovery)**
    *   *Status:* **Recovered** Mar 21, 00:59 UTC following a re-trigger at 00:54 UTC on the same day due to <6 processed files. Monitor ID: `20382848`.
*   **Service: `fpon-sap-jobs-file-parser` (P3 - Product Data Management) [ACTIVE]**
    *   *Issue:* Excessive file volume (>2000/day).
    *   *Latest Timeline:* Triggered **Mar 20, 01:01 UTC**. Monitors `92102475` (Received) & `92102474` (Stored).
*   **Service: `go-catalogue-service` (P3 - Discovery)**
    *   *Status:* **Recovered** Mar 20, 09:27 UTC following latency spike at 08:51 UTC. Monitor ID: `17447967`.

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c


## [10/30] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Last Activity: 2026-03-21T00:03:09.011000+00:00 | Last Updated: 2026-03-21T02:10:08.620197+00:00
**Daily Work Briefing Summary (Updated: March 21, 2026)**

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
*   **Inbox Status:** As of March 21, 2026, the workspace inbox is fully caught up across all categories (**Urgent Action Items**, **High-Volume/Project Themes**, **Meeting Updates**, and **FYI**). No pending unread items require immediate attention.

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

**Note on New Content:** The latest system notification confirms the inbox remains clear of urgent action items, project themes, meeting updates, and FYI notices as of March 21, 2026. No changes to pending actions or decisions were required based on this update.


## [11/30] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Last Activity: 2026-03-20T23:01:22.301000+00:00 | Last Updated: 2026-03-21T02:11:15.168399+00:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
The conversation comprises automated Datadog alerts for the production environment (`env:prod`). Instability in Mirakl integration has extended from March 17 through mid-day on March 20. A recurring latency spike was detected in the `picklist-pregenerator` service on the night of March 17, early morning March 19, and again at **23:01 UTC on March 20**. All new alerts triggered today (March 20) were automatically recovered.

**Incident Summary & Timeline (2026-03-15 to 2026-03-20)**
*   **Service:** `fni-order-create` (Mirakl Integration) – **Recurring Pattern Continuation**
    *   **Cycle G (Mar 19, 09:42–09:49 UTC):** Triggered multiple P2 alerts including "Exception Occurred At Mirakl Route," "Error while calling APIs," and "Failure occurred during fetching orders." Resolved by 09:49 UTC (~7 mins).
    *   **Cycle H (Mar 20, 08:42–08:47 UTC):** Triggered at 08:42 UTC with "Exception Occurred At Mirakl Route" and "Error while calling APIs." Recovered by 08:47 UTC (~5 mins).
    *   **Note:** Confirms a persistent recurrence of Mirakl integration failures across March 17, 18, 19, and 20.

*   **Service:** `fpon-seller-sap-picklist-reporter` – **Authentication Failure**
    *   **Cycle (Mar 20, 19:12–19:17 UTC):** Triggered P1 alert "SAP authentication failed on picklist job." Log query matched `env:prod service:fpon-seller-sap-picklist-reporter "SAP API authentication failed"`.
    *   **Resolution:** Alert recovered at 19:17 UTC (~5 mins duration).

*   **Service:** `seller` (`picklist-pregenerator`) – **Recurring Latency**
    *   **Cycle (Mar 17, 23:01):** Triggered with P2 warning. Metric value: 3604.897s. Recovered subsequently.
    *   **Cycle (Mar 19, 07:01):** Triggered at 07:01:23 UTC with P2 warning regarding completion time. Metric value: 3605.054s. Status recovered by subsequent monitoring cycles.
    *   **Cycle (Mar 20, 23:01:22 UTC):** Triggered at **23:01:22 UTC** with P2 warning. **Metric value: 3611.453s**. Monitor ID `20383097` linked to dashboard tag `mkp-seller-job`.

*   **Service:** `fni-offer`
    *   Historical incidents from March 15–17 remain noted. No new events reported in the current window.

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of expanded Mirakl integration instability affecting `fni-order-create`. The pattern now includes four distinct recurrence windows across four consecutive days (Mar 17–20).
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Investigate root cause of SAP authentication failures in `fpon-seller-sap-picklist-reporter`. A P1 event occurred on March 20 at 19:12 UTC, indicating potential credential or connectivity issues specific to the SAP picklist job.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Investigate root cause of extreme latency spikes in `picklist-pregenerator`. Cycles occurred on March 17 (3604s), March 19 (3605s), and **March 20 (3611.453s)**.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Review Monitor `29851723` logic for Apple Pay/Google Pay transactions following the March 16 spike and resolve the test alert triggered on March 20 at 06:12 UTC regarding Google Pay metrics (resolved by 06:13 UTC).
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Summary for Leadership**
Mirakl integration instability has persisted across March 17–20, with a P2 event at 08:42 UTC on March 20 resolving in 5 minutes. A new critical pattern emerged on March 20 at 19:12 UTC where the `fpon-seller-sap-picklist-reporter` service experienced a P1 SAP authentication failure for approximately 5 minutes before automatic recovery. Concurrently, `picklist-pregenerator` exhibited a critical performance anomaly at **23:01:22 UTC on March 20** with a metric value of **3611.453s**. These recurring patterns across Mirakl, SAP, and job processing logic require urgent engineering review to address systemic pipeline issues.


## [12/30] BCRS - UAT
Source: gchat | Group: space/AAQACfHCuNI | Last Activity: 2026-03-20T13:18:36.396000+00:00 | Last Updated: 2026-03-20T15:41:34.903215+00:00
**BCRS UAT Daily Briefing Summary (Updated: 20 Mar 2026)**

**Key Participants & Roles**
*   **Sathya Murthy Karthik:** UAT Lead/Coordinator (Provided status update as of 20 Mar).
*   **Finance Team:** Reviewing failed test cases; providing sign-off pending internal review.
*   **S&G Team:** Completed development for Returns & Refunds; currently conducting internal testing.

**Main Topic**
Progress tracking on OG Returns & Refunds, In-store Pre-order, CS Testing, and Finance Testing as of 20 Mar 2026 at 9:30 PM. While S&G development is complete and CS/Finance testing figures remain stable, critical blockers in In-store Pre-order (POS charging issues) have shifted the retest timeline to 24 Mar. Sign-off for OG Returns & Refunds remains pending due to Finance Team review of failed cases.

**Pending Actions & Owners**
*   **Returns & Refunds (OG):** Development complete; internal testing initiated.
    *   *Specific Action:* Finance Team must review and mark previously failed test cases, then provide sign-off. Owner: Finance Team.
*   **In-store Pre-order:** 4 test cases still failing due to BCRS FOC POS charging issue (down from 15). Retest scheduled for 24 Mar; sign-off planned for the same day. Owner: S&G Team / Testing Team.
*   **Finance Testing:** 9 test cases failed. Finance Team to review and update status. Owner: Finance Team.

**Decisions Made & Clarifications**
*   **Sign-off Timeline:** OG Returns & Refunds sign-off is pending Finance Team review of failures. In-store Pre-order sign-off is now scheduled for 24 Mar 2026 (Tuesday).
*   **Status Updates:** S&G development for Returns & Refunds is officially complete. CS testing has resolved its single pending item (Manual cancellation) with the result now recorded as a pass or failure update in progress.

**Status Snapshot (as of 20 Mar, 9:30 PM)**
*   **OG Returns & Refunds:** Development done; internal testing started. Sign-off pending Finance review.
*   **CS Testing:**
    *   **Passed:** 17
    *   **Pending:** 0
    *   **Failed:** 1 (Re-delivery).
*   **Finance Testing:**
    *   **Passed:** 9
    *   **Pending:** 0
    *   **Failed:** 9 (Awaiting Finance review and update).
*   **In-store Pre-order:**
    *   **Passed:** 17
    *   **Pending:** 0
    *   **Failed:** 4 (Down from 15; retest planned for 24 Mar).

**Key Dates & Deadlines**
*   **9 Mar 2026:** Feature Flag turned off for production.
*   **18 Mar 2026:** Previous status reporting date.
*   **19 Mar 2026:** Previously planned sign-off (delayed).
*   **20 Mar 2026:** Current status reporting date (9:30 PM).
*   **24 Mar 2026 (Tue):** Scheduled retest and sign-off for In-store Pre-order.

**Historical Context**
*   Previous updates noted delays due to POS charging issues in In-store Pre-order; current data confirms progress with failures reduced from 15 to 4.
*   OG Returns & Refunds development, previously ongoing on 18 Mar, is now confirmed complete as of 20 Mar.


## [13/30] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/fN7jxS6RotE | Last Activity: 2026-03-20T12:33:53.106000+00:00 | Last Updated: 2026-03-20T15:42:20.707438+00:00
**Daily Work Briefing: BCRS Firefighting Group (Updated)**

**1. Key Participants & Roles**
*   **Prajney Sribhashyam:** Inquiry lead; responsible for confirming UAT readiness and risk management.
*   **De Wei Tey:** Technical confirmation owner; responsible for delivery status updates.
*   **Sathya Murthy Karthik:** Notified recipient regarding testing availability.

**2. Main Topic**
Verification of User Acceptance Testing (UAT) readiness for the "SnG refunds" feature, specifically addressing scheduling conflicts with public holidays and confirming internal testing capabilities.

**3. Decisions Made & Status Updates**
*   **Initial Request:** Prajney requested De Wei Tey to attempt a 23 March morning release, noting that internal testing could proceed on the holiday (19 Mar).
*   **Decision to Re-evaluate:** De Wei Tey declined an immediate confirmation for 23 March, stating they would provide an update by noon the following day (20 Mar) (19 Mar).
*   **Final Confirmation:** On 20 March at 12:26 PM, De Wei Tey confirmed that **"SnG is ready for testing."**
*   **Outcome:** The requirement to shift the deadline to 24 March was superseded by the successful confirmation of readiness for 23 March.

**4. Pending Actions & Ownership**
*   **Action:** None currently identified as pending regarding UAT readiness.
    *   De Wei Tey fulfilled the commitment to update Prajney by noon on 20 March.
    *   Sathya Murthy Karthik acknowledged the readiness notification (20 Mar).

**5. Key Dates & Deadlines**
*   **Request Date:** 19 March 2026, 10:26 AM – Request for 23 March morning availability.
*   **Commitment Deadline:** 20 March 2026, 12:00 PM (Noon) – De Wei Tey promised to update by this time.
*   **Readiness Confirmation:** 20 March 2026, 12:26 PM – SnG confirmed ready for testing.
*   **Acknowledgement:** 20 March 2026, 12:33 PM – Sathya Murthy Karthik confirmed receipt.

**Summary of Discussion Flow**
On 19 March at 10:26 AM, Prajney Sribhashyam asked De Wei Tey if a 23 March morning release was still possible, as internal testing could occur on the holiday. Instead of immediately confirming or rejecting, De Wei Tey deferred the decision, promising an update by noon on 20 March.

On 20 March at 12:26 PM, De Wei Tey confirmed that "SnG is ready for testing." Prajney thanked them and subsequently tagged Sathya Murthy Karthik to notify him of the readiness (12:33 PM). Sathya acknowledged the update. The previous discussion regarding a delay to 24 March due to holiday constraints was resolved in favor of proceeding with the original target date upon confirmation of readiness.

**Reference Resources**
*   **Group:** BCRS Firefighting Group
*   **Chat URL:** https://chat.google.com/space/AAQAgT-LpYY


## [14/30] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/YnGsH8DqBGs | Last Activity: 2026-03-20T12:18:50.538000+00:00 | Last Updated: 2026-03-20T15:42:59.594021+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Michael Bui:** Raises strategic questions regarding fulfillment models, cart unification, and AI architecture.
*   **Daryl Ng:** Directs the inquiry to existing project documentation ("Workbench").
*   **Gopalakrishna Dhulipati:** Provides definitive technical clarification on "Project Hive" concepts and operational strategy.
*   **Tiong Siong Tee:** Validates the concept and summarizes the operational shift.

**Main Topic**
Discussion regarding the strategic implications of **Project Hive**, specifically focusing on:
1.  Changes to fulfillment models (Store vs. Hive).
2.  Potential for cart unification across channels.
3.  AI/Agentic architecture centralization vs. decentralization.

**Decisions & Clarifications**
*   **Hive Definition:** Project Hive is defined as a **sortation center**, not an inventory holding location. It does not store stock like traditional stores or DCs.
*   **Fulfillment Flow:** Orders will be placed directly to Distribution Centers (DCs) similar to how stores order from DCs. The DC sends picklists/product batches to the four Hives across Singapore. Hives then break down orders at the individual level, sort them, and dispatch to customers.
*   **Strategic Shift:** This is a multi-year journey transitioning from "fulfillment from store" to "fulfillment from Hive."
*   **Quick Commerce:** Initial decision indicates **no** quick commerce operations will originate directly from Hives; express delivery will likely remain fulfilled from stores during this transition.

**Pending Actions & Ownership**
*   **Review Project Documentation:** Michael Bui is advised by Daryl Ng to consult the "Workbench" on Project Hive for detailed specifications regarding fulfillment changes and inventory logic.
    *   *Owner:* Michael Bui (implied via suggestion).
*   **Cart Unification Strategy:** The question of a unified cart across Online, Offline, and O2O channels remains open pending further architectural planning, as no confirmation was provided in this thread.

**Key Dates & References**
*   **Date:** March 20, 2026 (Conversation timeline: 00:24 – 12:18 UTC).
*   **Project Reference:** Project Hive (Sortation Centre initiative).
*   **Location Scope:** Singapore (SG) – Four Hives planned.
*   **URL:** https://chat.google.com/space/AAQAsFyLso4


## [15/30] Jacob, Alvin, Sathya, Daryl, ...
Source: gchat | Group: space/AAQARrKvd_Y | Last Activity: 2026-03-20T12:08:15.636000+00:00 | Last Updated: 2026-03-20T15:43:31.419470+00:00
**Daily Work Briefing: Workshop Catering Coordination**

**Key Participants & Roles**
*   **Sathya Murthy Karthik:** Meeting organizer/catering lead. Responsible for collecting dietary data and finalizing the lunch order.
*   **Gopalakrishna Dhulipati:** DPD leads representative. Submitted initial dietary information on behalf of the team based on available knowledge.
*   **Tiong Siong Tee:** Team member acknowledging Gopalakrishna's contribution.
*   **Hui Hui:** Identified as a participant with an unknown dietary status; requires direct follow-up.

**Main Topic**
Collection of dietary restrictions to arrange catering for the upcoming workshop lunch scheduled for next week (Tuesday). The data is being aggregated in a Google Sheet titled "Dietary Requirements."

**Pending Actions & Ownership**
1.  **Verify Hui Hui's Dietary Needs:** Sathya Murthy Karthik will personally check with Hui Hui to confirm her specific requirements, as Gopalakrishna Dhulipati indicated he was unaware of them.
2.  **Finalize Spreadsheet Entries:** Ensure all DPD leads' dietary information is accurate (currently marked by Gopalakrishna as "based on knowledge" pending verification).

**Decisions Made**
*   The team agreed to use the shared Google Sheet for data collection.
*   Gopalakrishna Dhulipati was authorized to fill in the sheet on behalf of the DPD leads based on his current knowledge, with an invitation for others to correct inaccuracies.

**Key Dates & Deadlines**
*   **Meeting Date:** Next Tuesday (Workshop lunch).
*   **Submission Deadline:** Today at 1:15 PM local time (approx. 04:30 UTC + offset based on message timestamp context, though strictly noted as "by 1:15 PM today" in chat).
*   **Reference Timestamps:** Activity occurred between March 20, 2026, 04:29 AM and 12:08 PM.

**Summary of Status**
The deadline for dietary submissions has passed (or is imminent) at 1:15 PM today. While the DPD leads have been covered provisionally by Gopalakrishna Dhulipati, a specific gap remains regarding Hui Hui's requirements, which Sathya is actively addressing to ensure accurate catering arrangements.


## [16/30] QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs | Last Activity: 2026-03-20T11:05:52.385000+00:00 | Last Updated: 2026-03-20T15:45:39.538220+00:00
**Daily Work Briefing: QE <-> All Tribes** (Updated)

**Key Participants & Roles**
*   **Patrick Thun:** Lead/Coordination.
*   **Madhuri Nalamothu:** QA Lead/Test Execution.
*   **Milind Badame:** QA Engineer.
*   **Hang Chawin Tan:** DevOps/Backend Support.
*   **Daryl Ng / Michael Bui:** Dev/Product.
*   **Komal Ashokkumar Jain:** Reported New Defect.
*   **Others:** Dany Jacob, Piraba Nagkeeran, Yangyu Wang, Andin Eswarlal Rajesh.

**Main Topics & Discussion**
1.  **LinkPoints Test Failure:** Tests remain disabled in regression; awaiting ETA on resolution from Dev Team (Michael Bui). *Status:* Blocked.
2.  **Postal Code Offer Label Missing:** Milind Badame reported a missing `label` attribute for the first product in "TestHasOffer swimlane" for Postal code **098619**. Requires investigation.
3.  **QC Food Tile Removal Testing:** Daryl Ng confirmed testing is underway on the removal of QC (O2O) food tiles on the Omni home page.
4.  **Load Testing & Environment Stability:** Small-scale load test completed on **5 Mar, 11 AM–1 PM** (UAT LEAP env). Scale-down operations executed successfully.
5.  **DC Membership Logic Discrepancy:** Critical inconsistency where users have `DC member` flags in back office but lack active plans/UI awards. Investigation ongoing regarding award logic and payment errors for new DC trial members.
6.  **E2E Test Failures & UI Defects:**
    *   **Cart Page (Critical):** Komal Ashokkumar Jain reported a critical flaw where switching from Standard to Express delivery causes cart items to "stick," allowing users to place orders with ineligible items for 1HD (One Hour Delivery). Referenced by @Daryl Ng and @Andin Eswarlal Rajesh.
    *   **General UI:** Broken alignment on the third highlighted product; unidentified "view buttons" require clarification (Refs: Andin Eswarlal Rajesh). iOS navigation issues persist, including disappearing swimlanes, EVoucher errors, Express delivery label changes ("Get in 1Hr"), and 1-hour filter chip failures.

**Pending Actions & Ownership**
*   **LinkPoints Fix Status:** Provide ETA for the LinkPoints fix to re-enable tests. *Owner: Dev Team / Michael Bui.* (High Priority).
*   **Postal Code Label Debug:** Investigate missing `label` for Postal code 098619 in TestHasOffer swimlane. *Owner: Milind Badame / Dev Team.*
*   **SonarCloud Fix:** Change `invoice-service` New Code baseline from "Specific version" to "Previous version". *Owner: Hang Chawin Tan / Project Admins.*
*   **Cart Express Delivery Bug (New):** Investigate and fix logic allowing ineligible items for 1HD when switching delivery modes. *Owners: Komal Ashokkumar Jain, Daryl Ng, Andin Eswarlal Rajesh.*
*   **General Cart & Payment:** Resolve Cart alignment, view buttons, and payment failures for new DC trial members. *Owners: Milind Badame, Andin Eswarlal Rajesh, Madhuri Nalamothu, Dev Team.*
*   **QC Removal Testing:** Monitor progress of QC (O2O) food tile removal on Omni home. *Owner: Daryl Ng / QA Team.*

**Decisions Made**
*   Ad slot changes proceed; known test impacts acknowledged.
*   No decision yet on LinkPoints fix, Cart view buttons, or Express delivery eligibility logic; awaiting dev clarification and investigation results.

**Key Dates & Deadlines**
*   **5 Mar:** Load testing window (completed).
*   **16 Mar:** DC membership logic discrepancy logged.
*   **17 Mar:** UI defects reported on cart page (06:23–06:33 AM).
*   **18 Mar:** LinkPoints fix ETA required; Postal code 098619 issue flagged.
*   **20 Mar (Today):** Critical Express delivery bug flagged by Komal Ashokkumar Jain at 11:05 UTC.


## [17/30] Ching Hui Ng
Source: gchat | Group: dm/1vXYPsAAAAE | Last Activity: 2026-03-20T09:13:18.208000+00:00 | Last Updated: 2026-03-20T15:48:33.524022+00:00
**Daily Work Briefing: Google Chat Summary**

**Resource:** Ching Hui Ng
**Date of Conversation:** March 20, 2026

### Key Participants & Roles
*   **Ching Hui Ng:** Initiator; inquiring about integration capabilities.
*   **Michael Bui:** Respondent; confirmed schedule constraints and proposed alternative timing.

### Main Topic
Discussion regarding the technical integration between **Osmo** and **Smart Cart**, specifically Ching Hui Ng's need for a quick catch-up to understand how the teams can collaborate on this integration.

### Pending Actions & Ownership
*   **Action:** Schedule an online meeting to discuss Osmo and Smart Cart integration.
    *   **Owner:** Both parties (to confirm availability).
    *   **Proposed Slots:** Monday or Friday of next week (week commencing March 23, 2026).

### Decisions Made
*   No immediate decision on the meeting date was finalized during this exchange.
*   Michael Bui declined a physical in-person meeting for next week due to full-day workshops but agreed to an online session.
*   The scope of the discussion remains focused on "integration with Osmo" and collaboration with "Smart Cart."

### Key Dates & Follow-ups
*   **Conversation Date:** March 20, 2026 (08:30 – 09:13 UTC).
*   **Michael's Availability Constraints:**
    *   **Next Week (March 23–27):** Fully occupied by full-day workshops; unavailable for in-person meetings.
    *   **Week After Next (March 30–April 3):** On leave.
*   **Target Follow-up Window:** Monday or Friday of next week (specifically within the week of March 23, 2026).

### Action Required
Ching Hui Ng to propose a specific time on either Monday or Friday of next week to finalize the online catch-up before Michael's leave the subsequent week.


## [18/30] Andin Eswarlal Rajesh
Source: gchat | Group: dm/pTMl_AAAAAE | Last Activity: 2026-03-20T09:11:42.530000+00:00 | Last Updated: 2026-03-20T15:49:05.015204+00:00
**Daily Work Briefing: Google Chat Summary**
**Resource:** Andin Eswarlal Rajesh
**Date of Conversation:** March 20, 2026

### **Key Participants & Roles**
*   **Andin Eswarlal Rajesh:** Initiator of the discussion; owner of the "ads issue" resolution and liaison with Nikhil.
*   **Michael Bui:** Recipient of initial outreach; attendee of the scheduled meeting; creator of the diagnostic diagram.
*   **Nikhil:** Third-party stakeholder briefed by Andin regarding the issue (role inferred as technical or operational owner).

### **Main Topic**
Discussion centered on resolving a specific **"ads issue."** The conversation involved scheduling an immediate video call to address this matter, followed by updates on internal communication with Nikhil and the preparation of a visual aid for clarity.

### **Actions & Ownership**
*   **Andin Eswarlal Rajesh:** Explained the ads issue details to **Nikhil**. Andin explicitly stated: "Let him comeback."
    *   *Status:* Pending response from Nikhil.
*   **Michael Bui:** Created a diagram to clarify the situation (sent at 09:11).
    *   *Status:* Completed; awaiting review or further discussion based on the new visual aid.

### **Decisions Made**
*   **Communication Protocol:** The issue was deemed complex enough to require a video call rather than text-only resolution.
*   **Information Handoff:** Andin determined that Nikhil needed to be briefed directly before proceeding, effectively passing the immediate explanatory burden to him.

### **Timeline & Follow-ups**
*   **07:48 UTC:** Michael Bui was tagged; Andin requested a call regarding the ads issue.
*   **07:59 UTC:** Michael Bui joined a Google Meet session (`https://meet.google.com/czz-sdbo-fhd`) and waited for ~10–15 minutes. No attendance from Andin is recorded in the chat log during this window.
*   **08:58 UTC:** Andin re-engaged, confirming he had explained the issue to Nikhil and was waiting for a response. A message was subsequently deleted by its author (timestamp 09:11 context implies subsequent silence or edit).
*   **09:11 UTC:** Michael Bui acknowledged Andin's help and provided a diagram to visualize the situation.

**Pending Follow-up:** The thread indicates an active wait state for **Nikhil** to "come back" (respond/proceed) after Andin's briefing, while Michael awaits review of the newly created diagram. No specific deadline was set in the chat log.


## [19/30] ❗ Important Email
Source: gchat | Group: space/AAQAUJW8HMo | Last Activity: 2026-03-20T09:08:51.688000+00:00 | Last Updated: 2026-03-20T15:50:12.794985+00:00
**Daily Work Briefing Summary (Updated)**

**Key Participants & Roles**
*   **Michael Bui (You):** Managing Osmos support, event RSVPs, FileVault compliance, performance feedback, Project Light coordination, and BCRS Refunds issue.
*   **Alvin Choo:** Organizer of "1 on 1 with michael" meeting; organizer of "[Placeholder] Project Light."
*   **Prajney Sribhashyam:** Organizer of the BCRS - Refunds Issue Warroom.
*   **Daryl Ng (FairPrice):** Required attendee for both Project Light and BCRS meetings.
*   **Miguel Ho Xian Da (FairPrice):** Lead requesting OSMOS integration.
*   **Jazz Tong:** Head of Platform Engineering; on leave until Mar 23, 2026.

**Main Topics**
1.  **Performance Feedback & Project Light:**
    *   **Feedback Session:** Scheduled for Wednesday, Mar 18, 2026, at 4:00 PM SGT with Alvin Choo and Winson Lim.
    *   **Project Light:** **TIME UPDATE**: Meeting rescheduled from 5:00–6:00 PM to **Thursday, March 19, 2026, from 4:00 PM – 5:00 PM SGT**. Location remains FairPrice Hub-11-L11 Cappuccino (10) [Google Meet]. Attendees include Tiong Siong Tee, Akash Gupta, Daryl Ng, and Gopalakrishna Dhulipati.
2.  **BCRS - Refunds Issue Warroom:**
    *   Scheduled for **Thursday, March 19, 2026, from 3:30 PM – 4:30 PM SGT** (scheduled by Prajney Sribhashyam).
    *   **Required Attendees:** Michael Bui, Daryl Ng, Wai Ching Chan, Sathya Murthy Karthik, and De Wei Tey. Optional guest: Pazhanisamy Harish Prabhu.
    *   Access via Google Meet link or PIN 991171272.
3.  **OSMOS Retail Media Integration:** FairPrice Group scaling Smart Carts/Digital Price Card requires CMS consolidation. Accenture (Tong A. Yu) and Miguel Ho to prioritize a working session next week for architecture definition.
4.  **Internal Talent Marketplace:** HR introduced "MyCareer Portal" for internal mobility. Eligibility: Grade D (2 yrs tenure), Grade C+ (3 yrs tenure); requires Green rating in last 2–3 years and no disciplinary actions.
5.  **DPD Team BBQ:** Celebratory dinner for Mar 17, 2026 (6:00 PM – 9:00 PM) at BBQ Box, Jurong Point. Meet Lobby A at 5:45 PM.

**Pending Actions & Ownership**
*   **Project Light RSVP (Michael Bui):** **CRITICAL**: Reply to Alvin Choo's updated invitation immediately confirming attendance for the new time slot (**Mar 19, 4:00 PM SGT**).
*   **BCRS Warroom RSVP (Michael Bui):** Reply "Yes" to Prajney Sribhashyam's invitation for Mar 19, 3:30–4:30 PM. Note: This overlaps with the Project Light meeting time; immediate attention required to resolve scheduling conflict.
*   **Performance Meeting RSVP:** Confirm attendance for Mar 18, 4:00 PM SGT.
*   **OSMOS Coordination:** Await timeslots from Miguel Ho to schedule working session.
*   **FileVault Encryption:** Register via calendar ASAP. Book appointment with Geek Squad (FP Hub Level 15) for Mar 28 deadline (Final: Mar 31). Bring MacBook; backup files to Google Drive.

**Decisions Made**
*   **OSMOS Capability:** Confirmed feasible short-term integration contingent on SmartCart/IPOS architecture details.
*   **Working Session:** Prioritized for the week following March 12.
*   **Internal Mobility:** Guidelines established for internal transfers via MyCareer Portal; direct queries to `ta@fairpricegroup.sg`.

**Critical Dates & Deadlines**
*   **Mar 16, 2026 (EOD):** RSVP deadline for DPD BBQ.
*   **Mar 18, 2026 (4:00 PM):** Performance Feedback Meeting.
*   **Mar 19, 2026 (3:30–4:30 PM):** BCRS Refunds Warroom.
*   **Mar 19, 2026 (4:00–5:00 PM):** Project Light meeting (**UPDATED**). *Conflict Alert:* Overlaps with Warroom start time.
*   **Mar 23, 2026:** Jazz Tong returns from holiday; OSMOS/Platform Engineering support resumes.
*   **Mar 24, 2026:** Bryan Choong returns.
*   **Mar 28 & Mar 31, 2026:** FileVault deadlines.


## [20/30] Video & Product Ads Working Group
Source: gchat | Group: space/AAQAeSWRtgQ/zGVhQ12TPVI | Last Activity: 2026-03-20T09:05:34.354000+00:00 | Last Updated: 2026-03-20T15:50:38.053859+00:00
**Daily Work Briefing: Video & Product Ads Working Group**

**Date:** March 20, 2026
**Source:** Google Chat Space (https://chat.google.com/space/AAQAeSWRtgQ)

**Key Participants & Roles**
*   **Michael Bui:** Primary contributor; provided technical analysis and documentation regarding store ID discrepancies.
*   **Nikhil Grover:** Tagged participant for review of the explanation.
*   **Andin Eswarlal Rajesh:** Tagged participant for review of the explanation.

**Main Topic**
Discussion regarding the discrepancy in Store IDs observed between the "Omni Home swimlane" and the "See all" pages within the application logic.

**Key Decisions & Findings**
*   **Root Cause Identified:** The variation in Store IDs is expected behavior, not a defect. It occurs because users interact with different devices and different stores simultaneously.
*   **Scenario Specificity:** This specific scenario does not represent normal user behavior. It only manifests when there is a change in the store or postal code.
*   **Impact Assessment:** Due to the rarity of the triggering condition (store/postal code changes), the frequency of these occurrences is expected to be low.

**Pending Actions & Ownership**
*   No new action items were assigned during this exchange. The discussion concluded with Michael Bui providing a sequence diagram and rationale to clarify the behavior for stakeholders Nikhil Grover and Andin Eswarlal Rajesh.

**Key Dates & Follow-ups**
*   **Latest Activity:** March 20, 2026 (09:04 AM – 09:05 AM UTC).
*   **Follow-up Status:** The sequence diagram created by Michael Bui serves as the primary reference for understanding this behavior; no further immediate follow-up is indicated in the chat log.


## [21/30] Video & Product Ads Working Group
Source: gchat | Group: space/AAQAeSWRtgQ | Last Activity: 2026-03-20T09:04:20.531000+00:00 | Last Updated: 2026-03-20T15:51:20.835679+00:00
**Daily Work Briefing: Video & Product Ads Working Group**

**Key Participants & Roles:**
*   **Michael Bui:** Initiator of technical inquiries; recently clarified store ID discrepancies in Omni Home.
*   **Nikhil Grover:** Noted as having unread messages previously; now active on swimlane data sources and finalizing the "See all" page explanation.
*   **Norman Goh & Flora Wo Ke:** Action Owners for previous API/positioning investigation.
*   **Daryl Ng, Andin Eswarlal Rajesh:** Recently tagged regarding swimlane logic and store ID sequences.

**Main Topic Shift:**
The discussion has expanded from a specific data inconsistency (frontend position vs. backend return) to broader architectural questions regarding **Omni Home swimlane data sources** and **store ID handling**.

**New Technical Inquiries & Updates:**
1.  **Data Source Clarification (March 19, 2026):** Nikhil Grover requested confirmation on which OG home swimlanes are powered by **DS** versus **Algolia**, specifically tagging Daryl Ng for input.
2.  **Store ID Logic (March 20, 2026):** Michael Bui addressed discrepancies between Omni Home swimlane and "See all" pages. He confirmed with the team that these differences are expected behavior due to users operating on different devices and stores. A sequence diagram was created to document this logic for Nikhil Grover and Andin Eswarlal Rajesh.

**Technical Evidence (Historical Context):**
*   **Ad ID:** `bc47...` | Service Return: Position `2` (Product ID: `11714485`)
*   **Ad ID:** `30d1...` | Service Return: Position `5` (Product ID: `11714258`)
*   *Note:* While the positioning discrepancy (observed 1,3 vs. reported 2,5) remains a technical baseline, current focus has shifted to swimlane architecture and store ID mapping.

**Pending Actions & Ownership:**
*   **Action 1 (Data Sources):** Confirm which OG home swimlanes utilize DS and which utilize Algolia.
    *   **Owner:** Daryl Ng (requested by Nikhil Grover).
*   **Action 2 (Store ID Logic):** Review the newly created sequence diagram explaining store ID differences between Omni Home and "See all" pages.
    *   **Participants:** Michael Bui, Nikhil Grover, Andin Eswarlal Rajesh.
*   **Action 3 (API/Scrolling):** Clarify API source for vertical scrolling and position derivation logic.
    *   **Owner:** Norman Goh and Flora Wo Ke.

**Decisions Made:**
*   Confirmed that store ID differences between Omni Home swimlanes and "See all" pages are **expected behavior**, driven by multi-device and multi-store user contexts. This was visualized via a new sequence diagram shared on March 20, 2026.

**Key Dates & Follow-ups:**
*   **Discussion Start:** March 16, 2026 (Original positioning inquiry).
*   **Latest Activity:** March 20, 2026, 09:04 AM UTC (Michael Bui's sequence diagram update) with a reply at 09:05 AM.
*   **Thread Volume:** Current context includes replies from Michael, Nikhil, Daryl, and Andin regarding the new topics.

**Reference Links:**
*   Space URL: `https://chat.google.com/space/AAQAeSWRtgQ`


## [22/30] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/HuH1xrx7Fvc | Last Activity: 2026-03-20T07:51:20.449000+00:00 | Last Updated: 2026-03-20T15:53:30.782457+00:00
**Daily Work Briefing: Digital Product Development (Leads/Omni)**

**Key Participants & Roles**
*   **Michael Bui:** Reporter of the technical discrepancy; currently coordinating backend investigation.
*   **Andin Eswarlal Rajesh:** Investigator/Owner assigned to diagnose and debug the Store ID inconsistency.
*   **Ravi:** Original observer who noticed the store ID mismatch while browsing.
*   **Nikhil Grover:** Identified as the owner for "Ads bug" context (mentioned in logs).

**Main Topic**
Investigation of a data inconsistency in Omni Home where the swimlane sends a different Store ID compared to the "See All" screen. Michael Bui identified that the "See all" page requests Store ID **165**, while the Omni swimlane request returns Store ID **17**.

**Pending Actions & Ownership**
*   **Provide API Samples:** Michael Bui requested one sample API request for the swimlane and one for the "See All" page to analyze data structure and flow.
    *   *Status:* Pending (Requested 2026-03-20).
*   **Debug & Connect:** Andin Eswarlal Rajesh initiated a direct connection with Michael Bui to debug the issue live.
    *   *Owner:* Andin Eswarlal Rajesh
    *   *Update:* DM sent at 07:51 AM on March 20, 2026; meeting scheduled.
*   **Backend Analysis:** Michael Bui will independently assess backend (BE) options while the Store ID consistency is being fixed by Andin.
    *   *Owner:* Michael Bui

**Decisions Made**
*   **Collaborative Debugging:** The team shifted from a log-only review to a live debugging session between Michael and Andin.
*   **Parallel Workstreams:** While Andin resolves the Store ID consistency, Michael will explore potential backend-side mitigations or fixes.
*   **No Immediate Fix Deployed:** Investigation continues before any patch is implemented.

**Key Dates & Follow-ups**
*   **Date Reported:** March 19, 2026
*   **Timeline:**
    *   09:19 AM (Mar 19): Issue raised by Michael Bui.
    *   09:50 AM (Mar 19): Clarification that Ravi is the observer (not triggered by postal code change).
    *   10:01 AM (Mar 19): Andin Eswarlal Rajesh confirmed ownership of the investigation.
    *   01:41 AM (Mar 20): Michael Bui requested specific API samples and noted BE-side analysis.
    *   07:51 AM (Mar 20): Andin Eswarlal Rajesh sent a DM to Michael Bui to schedule a debug session.
*   **Next Steps:** Await results of the live debugging session scheduled between Andin and Michael.

**Reference Links**
*   **Discussion Space:** https://chat.google.com/space/AAQAN8mDauE
*   **API Logs Document:** [View Here](https://docs.google.com/document/d/1a-G0Vp4jJtxE7RO9plx-ZfOUIO0ZWcFvDqJGXYDr1xE/edit?tab=t.0)


## [23/30] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Last Activity: 2026-03-20T07:29:53.715000+00:00 | Last Updated: 2026-03-20T15:54:22.666968+00:00
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
1.  **Website SDK Deployment (Strudel):** Lester Santiago Soriano announced a deployment of `go-platform-website` scheduled for today, Mar 19, at **4:00 PM**. This release updates the Strudel SDK to validate maximum voucher amounts per transaction. Changes are under review via Bitbucket diff between v1.5.11 and v1.5.10.
2.  **Pre-order Payment Logic:** Zaw Myo Htet raised a critical inquiry regarding pre-order flows: if a user with a pre-order QR code chooses the app payment method at a POS machine, does the order redeem as "pre-order" or "pay via app (offline)"? Investigation is ongoing.
3.  **Slot Date Discrepancy:** Shiva Kumar Yalagunda Bas reported a delivery slot mismatch where the UI shows the 25th while the API indicates the 23rd. Daryl Ng and Sundy Yaputra are involved in resolving this.
4.  **UAT Stock Requirements:** Sneha Parab requested 1-2 SKUs with high stock volumes for bulk order testing by Zi Ying. Wai Ching Chan and Akash Gupta were tasked to check IMS and provide availability.
5.  **Order Verification Bug (NED-278216):** Investigation continues into the Whitelisting API returning older contract data (identified by Andin). Team members are reviewing this issue.
6.  **BCRS Deposit & SAP Integration:** Critical duplicate deposit posting fix remains active (PR #6).

**Pending Actions & Ownership**
*   **Lester Santiago Soriano:** Proceed with `go-platform-website` deployment today at 4:00 PM. Assist with Whitelisting API contract issue (cc: Piraba Nagkeeran, Jonathan Tanudjaja).
*   **Wai Ching Chan & Akash Gupta:** Source high-stock SKUs from IMS for Zi Ying's bulk order testing. Investigate UAT SKU `13023506` threshold settings.
*   **Daryl Ng & Sundy Yaputra:** Resolve delivery slot date mismatch (UI showing 25th vs API 23rd).
*   **Zaw Myo Htet:** Clarify pre-order payment redemption logic and execute UAT testing on offboarded Pinelabs split feature flag.
*   **Andin Eswarlal Rajesh:** Investigate iOS slot mapping error and assist with Amplitude event tracking flow inquiry.

**Decisions Made**
*   **Deployment Approval:** PLU processor deployment approved pending UD alignment (per prior briefing).
*   **Code Review Priority:** Focus shifted to `go-platform-website` PR #1538 for the Strudel SDK update, superseding previous layout-service priorities.

**Key Dates & Deadlines**
*   **Mar 19, 2026 (Today):** Website deployment at 4:00 PM; UAT stock sourcing required immediately.
*   **Thursday:** D&T All Hands meeting.
*   **Mar 31, 2026:** Sports Hub FFS store closure deadline.
*   **Ongoing:** Slot logic validation, Amplitude tracking investigation, and NED-278216 resolution.

**Note on Historical Context:** Previous mentions of code review priorities for `layout-service` PR #362 and `website-service` PR #649 are superseded by the urgent Strudel SDK deployment update. The focus has now shifted to resolving slot date mismatches and pre-order payment logic queries.


## [24/30] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4 | Last Activity: 2026-03-20T07:23:49.182000+00:00 | Last Updated: 2026-03-20T15:55:14.727503+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Space Creator; Lead coordinating the briefing.
*   **Daryl Ng, Gopalakrishna Dhulipati, Tiong Siong Tee, Michael Bui, Akash Gupta:** Designated "Project Light Attack and Defence Leads".
*   **Note:** On March 20, Daryl Gupta and Akash Ng were welcomed into the group.

**Main Topic**
Establishment of a dedicated communication space to centralize Project Light discussion. The focus shifted from initial slide consolidation to addressing complex strategic questions regarding fulfillment models, cart unification, and AI architecture generated by Michael Bui during the review process.

**Pending Actions & Ownership**
*   **Action:** Address specific architectural inquiries raised by Michael Bui regarding:
    1.  Fulfillment model changes post-"Project Hive" (inventory movement, location binding).
    2.  Cart unification across channels (SNG, Shop Beyond, FPON, MKP DF).
    3.  AI/Agentic integration strategy (centralized vs. embedded).
*   **Ownership:** Alvin Choo and Gopalakrishna Dhulipati (tagged in Michael's query for response).
*   **Context:** The initial request to "read, digest, and reply" has evolved into a specific requirement for architectural clarification. Akash Gupta and Daryl Ng were explicitly tagged by Gopalakrishna in the morning greeting on March 20.

**Decisions Made**
*   A specific Google Chat space was created to centralize project discussion.
*   Initial approach of sharing consolidated screenshots remains valid but has been superseded by deep-dive architectural questions.
*   The team is now engaging in multi-channel strategic planning rather than simple content review.

**Key Dates & Follow-ups**
*   **Creation Date:** March 19, 2026 (10:10 AM UTC).
*   **Review Requested:** March 19, 2026 (10:20 AM UTC).
*   **Strategic Inquiry Raised:** March 20, 2026 (12:24 PM UTC) by Michael Bui.
*   **Group Expansion/Welcome:** March 20, 2026 (7:23 AM UTC) by Gopalakrishna Dhulipati.
*   **Last Activity:** March 20, 2026 (12:18 PM UTC).
*   **Space URL:** https://chat.google.com/space/AAQAsFyLso4

**Summary of Activity Log**
*   **March 19, 10:10 AM:** Alvin Choo tagged six leads to form the group and confirmed space creation.
*   **March 19, 10:20 AM:** Alvin instructed the team to digest shared slide screenshots and reply.
*   **March 20, 7:23 AM:** Gopalakrishna Dhulipati welcomed Daryl Gupta and Akash Ng (likely correcting or adding names to the original list) to the "Light party."
*   **March 20, 12:24 PM:** Michael Bui initiated a detailed technical discussion while digesting information. He raised three critical questions regarding fulfillment models under Project Hive, cross-channel cart unification, and AI/Agentic architecture centralization.
*   **March 20, 12:18 PM:** Final activity recorded with replies directed at Alvin Choo and Gopalakrishna Dhulipati.


## [25/30] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/Jef2i4clEGo | Last Activity: 2026-03-20T07:02:57.062000+00:00 | Last Updated: 2026-03-20T15:55:42.606240+00:00
**Daily Work Briefing: BCRS Firefighting Group**
**Resource:** Google Chat Space (URL: https://chat.google.com/space/AAQAgT-LpYY)
**Date:** March 20, 2026

**1. Key Participants & Roles**
*   **Sathya Murthy Karthik:** Initiator of the inquiry; seeking clarification on beta testing logistics.
*   **Onkar Bamane:** Tagged as a stakeholder responsible for providing details.
*   **Prajney Sribhashyam:** Tagged as a stakeholder responsible for providing details.

**2. Main Topic & Discussion**
The discussion focused on defining the operational scope and strategy for the upcoming beta testing phase. Sathya Murthy Karthik specifically requested a comprehensive plan covering:
*   The methodology of the beta test.
*   Identification of the tester pool (who will be testing).
*   Specific SKUs designated for the testing cycle.
*   Additional relevant details regarding the rollout.

**3. Pending Actions & Ownership**
*   **Action:** Provide a detailed beta testing plan, including tester identification and specific SKUs.
    *   **Owner:** Onkar Bamane and Prajney Sribhashyam (Tagged in response to query).
    *   **Status:** Awaiting response as of 07:07 UTC.

**4. Decisions Made**
*   No formal decisions or approvals were recorded in this exchange. The conversation remains in the information-gathering stage.

**5. Key Dates & Follow-ups**
*   **Inquiry Date:** March 20, 2026, at 07:02:57 UTC.
*   **Follow-up Required:** Immediate response from Onkar Bamane and Prajney Sribhashyam regarding the beta plan details is needed to proceed with planning.

**Note:** A message sent by an "Unknown" user at 07:07:02 UTC was deleted by its author and contains no actionable data.


## [26/30] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY | Last Activity: 2026-03-20T07:02:57.062000+00:00 | Last Updated: 2026-03-20T15:57:00.896333+00:00
**Updated Briefing: BCRS Firefighting Group**
**Date:** March 20, 2026 (Latest activity: 1:06 AM)
**Source:** Google Chat Space & Shared UAT Tracker (56 messages total)

### **Key Participants & Roles**
*   **Prajney Sribhashyam:** Project Lead/Test Coordinator.
*   **Michael Bui / Dany Jacob / De Wei Tey / Tiong Siong Tee:** Finance/Data/Invoice specialists.
*   **Onkar Bamane:** Technical Integration/SAP Liaison.
*   **Alvin Choo:** Product/Release Manager.
*   **Sathya Murthy Karthik:** QA Lead.
*   **Hendry Tionardi, Shiva Kumar Yalagunda Bas, Andin Eswarlal Rajesh:** Technical Support & Development.
*   **Shiva Kumar Yalagunda Bas:** Technical Lead (Deposit SKU focus).
*   **Sneha Parab:** Stakeholder (SKU/Feature inquiries).
*   **Daryl Ng:** Production deployment status liaison.

### **Main Topics**
1.  **Beta Testing Strategy:** Immediate clarification requested on the beta testing plan, including tester allocation and specific SKUs for validation (raised Mar 20).
2.  **Refunds UAT Centralization:** Dedicated tracker established for BCRS UAT 2026 Refunds issues (RPA, CS, Finance).
3.  **Production Deployment Verification:** Ongoing confirmation required on whether Invoice, Sales Posting, and Seller Reports changes are live in Production with correct feature flags.
4.  **UAT Readiness (SnG Refunds):** Validation confirmed for the March 23 UAT schedule regarding SnG refunds.
5.  **Deposit SKU Linking:** Investigation into Deposit SKUs failing to link to Master SKUs post-publishing.

### **Decisions Made**
*   **Mobile Release:** Proceeded with mobile release on March 6 (Confirmed by Alvin Choo).
*   **Linkpoints Logic:** Confirmed Linkpoints issued for BCRS SKUs, but *not* for Deposit items.
*   **Invoice Formatting:** Issue with missing minus signs (Order #75502500) redeployed on March 13; cache clearing instructed.

### **Pending Actions & Owners**
| Action Item | Owner(s) | Status/Context |
| :--- | :--- | :--- |
| **Beta Testing Plan Definition** | Onkar Bamane / Prajney Sribhashyam | **New (Mar 20, 1:06 AM):** Response required to Sathya Murthy Karthik's query regarding beta tester roles and specific test SKUs. Thread active with 1 reply. |
| **Refunds UAT Issue Tracking** | Prajney Sribhashyam / Team | Active (Mar 19, 2:42 PM): Launched dedicated thread/Google Sheet for RPA, CS, & Finance refund issues (6 replies). Link: `https://docs.google.com/spreadsheets/...` |
| **Production Deployment Confirmation** | Prajney Sribhashyam / Daryl Ng / Tiong Siong Tee / Michael Bui / Sneha Parab | Active (Mar 19, 3:49 AM): Query regarding Invoice, Sales Posting, and Seller Reports deployment status. Thread active with 3 replies. |
| **UAT Readiness for SnG Refunds** | Prajney Sribhashyam / De Wei Tey / Team | Active (Mar 19, 2:56 AM): Prajney confirmed readiness for March 23 UAT regarding SnG refunds. Thread active with 5 replies. |
| **Deposit SKU Linking Issue** | Shiva Kumar Yalagunda Bas / Chee Hoe Leong / Gautam Singh | Active (Mar 18, 06:17): Investigation required into Deposit SKU linking failure. Thread active with 18 replies. |
| **'BCRS Container Count' Field Assessment** | Prajney Sribhashyam / Sneha Parab | Pending: Awaiting effort/timeline estimates from Sneha Parab post-discussion (Mar 17). |
| **DBP UAT Access Check** | Sathya Murthy Karthik / Hanafi Yakub / Sneha Parab | Active (Mar 18, 10:39): Query regarding `shu_hui.lai@fairpricegroup.sg` DBP UAT access. Thread active with 4 replies. |
| **BCRS + DF SKU Validation** | Sathya Murthy Karthik / Sneha Parab | Pending: Awaiting response on "BCRS eligible + DF" SKU existence (Mar 16). |

### **Key Dates & Deadlines**
*   **March 6:** Mobile release executed.
*   **March 13:** Invoice format redeployed.
*   **March 16 (07:44 UTC):** Re-delivery flow test call initiated.
*   **March 18 (06:17 UTC):** Deposit SKU linking issue reported.
*   **March 19 (2:42 PM):** Refunds UAT tracker established.
*   **March 19 (3:49 AM):** Query raised regarding Production deployment of Invoice, Sales Posting, and Seller Reports.
*   **March 20 (7:06 AM):** Beta testing strategy discussion initiated.
*   **March 23:** Target date for SnG Refunds UAT.

### **Historical Context Retained**
*   Existing e-comm test accounts deemed unusable for Pre-order staff app; new BCRS CF items and specific GWP SKUs (e.g., Coca-Cola Zero) required.
*   Original deadline for SAP Deposit API development was Feb 20 (missed/risk noted).
*   Re-delivery flow testing ongoing with audio issues reported on March 16 awaiting resolution.


## [27/30] 📢 COM Notifications
Source: gchat | Group: space/AAAAu4WIubc | Last Activity: 2026-03-20T06:39:25.625000+00:00 | Last Updated: 2026-03-20T15:58:02.952635+00:00
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
*   **`seller-proxy-service` (PR-2306)**:
    *   **March 19**: Volatility observed. Initial failure at 13:38 UTC (80.2% coverage) resolved by 13:45 UTC (PASSED). Later that day, scans at 08:40 UTC failed (80.4%) but recovered to **PASSED** at 08:45 and 09:11 UTC with coverage stabilizing between 80.2%–80.4%.
    *   **March 20**: A scan at 04:58 UTC failed with **91.8%** coverage (ver. f9ece24). This was immediately resolved by a subsequent scan at 05:00 UTC, reporting **PASSED** with the same 91.8% coverage.
*   **`fni-product-license-alert`**: Scans on March 20 (PR-1433 and PR-1450) achieved **PASSED** status with 94.4% new code coverage.

**Pending Actions & Ownership**
*   **System Error Investigation**: The "Webhook Bot is unable to process your request" error persists in every notification from March 5 through the latest scans on March 20 (including `supplier-job` and `seller-proxy-service`). No specific owner assigned; requires immediate engineering attention.
*   **`fpon-sap-jobs` Unit Tests**: Discrepancy between 72.7% coverage and 0% unit test success requires review by the respective team.

**Decisions Made**
*   Recent merges in `supplier-job` (PRs #439, #440) and recovery scans for `seller-proxy-service` PR-2306 were accepted automatically following retries.
*   No manual interventions recorded; automated pipelines resolved all Quality Gate failures via subsequent successful scans.

**Key Dates & Timeline**
*   **March 5**: Initial scan failures in `catalogue-job`.
*   **March 9**: UAT deployment for `fpon-sap-jobs`; initial failure for `seller-proxy-service` PR-2318.
*   **March 12**: `seller-proxy-service` first passed after persistent failures; coverage stabilized above 95%.
*   **March 16 & 20**: Successful scans for `fni-product-license-alert` (PRs #1433, #1450) with 94.4% coverage.
*   **March 19**: 
    *   `supplier-job` PRs #439/#440 scanned successfully at 90.9% coverage.
    *   `seller-proxy-service` PR-2306 showed multiple failure/recovery cycles (failures at 13:38, 08:40; passes at 08:45, 09:11).
*   **March 20**: `seller-proxy-service` PR-2306 failed again at 04:58 UTC (91.8% coverage) but passed immediately at 05:00 UTC.


## [28/30] Retail out of home (Digital Screens & CMS)
Source: gchat | Group: space/AAQAXn1ocmE | Last Activity: 2026-03-20T06:35:40.826000+00:00 | Last Updated: 2026-03-20T15:59:13.721460+00:00
**Daily Work Briefing: Retail Out of Home (Digital Screens & CMS)**

**Key Participants & Roles**
*   **Priscilla Chan Li Wei:** Inventory management (Samsung ADE/FilmScreen); Escalation workflow impact analysis.
*   **David Anura Cooray:** Technical operations, screen connectivity, CMS verification; EPT Blank Screen investigation lead.
*   **Fiona U:** Project Lead/Coordinator; driving Phase 1 closure and stakeholder alignment.
*   **Rajkumar Romendro & Allen Umali:** Subject matter experts for Retail Media inventory and Screen Loading (MPBS/VXT).
*   **Cheng Joo Wu:** Assigned to Action Items regarding SOPs, Indirect Procurement (IP), IFM integration, and Engie scope liaison.
*   **Serene Tan Si Lin:** Clarification on facility management scope boundaries.

**Main Topic**
The discussion centers on operationalizing **Retail Out of Home (RoOH) Phase 1**, focusing on hardware inventory verification, digital screen content loading, transitioning from Hypercare to Business As Usual (BAU), and finalizing SOPs. A critical update concerns the **IFM** announcement: it is now confirmed that IFM will encompass the current Engie scope of responsibilities (building equipment, soft services, aircons, freezers). Digital monitors remain excluded from this maintenance scope. **New Issue:** David Anura Cooray raised an urgent ticket regarding **"EPT Blank Screen"** issues, requiring immediate technical investigation and potentially impacting screen connectivity workflows.

**Pending Actions & Ownership**
*   **Sync Meeting Attendance:** Priscilla, Allen, Cheng, and Rajkumar must attend or assign a proxy to the sync scheduled for **Tuesday at 2:00 PM**.
    *   *Pre-meeting Review:*
        *   **SOPs (Gdoc & Gslide):** Resolve unresolved comments and perform consistency checks. Owners: Team (implied Priscilla/Cheng).
        *   **SLA Finalization:** Must be completed by next week for the Samsung SI meeting. Owner: Fiona U / Team.
        *   **Communication Channels:** Define escalation paths between stores and AdOps; identify chat groups to sunset. Owner: Team.
        *   **Indirect Procurement (IP):** Clarify IP's specific role before integrating them into the Retail Media Workflow. Owner: Cheng Joo Wu.
*   **Inventory Verification:** David Anura Cooray requested a master list of all digital screens under Retail Media; pending response from Allen Umali and Rajkumar Romendro.
    *   *Scope Update:* Inventory scope explicitly includes **PDD Gondola End Large TVs**.
*   **Issue Resolution (EPT):** David Anura Cooray to investigate **"EPT Blank Screen"** occurrences immediately. This requires verification of CMS connectivity and screen status prior to the BAU transition.
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
*   **Incident Logs:** EPT Blank Screen thread (11 replies, last updated 7:37 AM).


## [29/30] DPD All Leads
Source: gchat | Group: space/AAAAQezbuRE/n1gAd6ytaqI | Last Activity: 2026-03-20T05:29:57.094000+00:00 | Last Updated: 2026-03-20T15:59:45.525823+00:00
**Daily Work Briefing: DPD All Leads**

**Key Participants & Roles**
*   **Winson Lim**: Raised initial concerns regarding service decommissioning and process governance.
*   **Michael Bui**: Confirmed initiation of the decommission process with the RE team.
*   **Daryl Ng**: Leading discussions with Microsoft (MS) on decommissioning; confirmed ownership of communication protocols.
*   **Maou Sheng Lee**: Provided technical constraints regarding database availability and provider billing models.

**Main Topic**
Discussion centered on the potential decommissioning of services related to the "DPD All Leads" resource, specifically following the removal of a food tile due to recent events. The conversation focused on cost savings, technical feasibility of shutting down resources (specifically DBs and Elasticsearch), and the operational risk of losing access if services are needed again.

**Key Decisions & Findings**
*   **Decommission Status**: Michael Bui has already initiated the process with the RE team to achieve significant savings.
*   **Scope of Shutdown**: Daryl Ng clarified that as the infrastructure is serverless, only the Databases (DB) and Elasticsearch (ES) need to be shut down; application services may remain or are irrelevant if resources are paused.
*   **Technical Constraints**: Maou Sheng Lee noted that Elasticsearch (ES) cannot currently be shut down. Furthermore, many cloud providers do not offer "pay-for-what-you-use" pricing models like AWS when power is off, implying shutdowns may not yield immediate cost reductions for all components.
*   **Uncertainty**: There is no certainty regarding whether the services will need to be reactivated in the future.

**Pending Actions & Ownership**
*   **Formal Communication/Ticketing**: Daryl Ng must provide a written message or create a formal ticket prior to shutting down any resources. (Action Owner: **Daryl Ng**; Status: **Confirmed/Acknowledged**)
*   **Vendor Coordination**: Continue discussions with Microsoft (MS) regarding the specific requirements for decommissioning. (Action Owner: **Daryl Ng**)

**Key Dates & Follow-ups**
*   **2026-03-20**: All discussion occurred on this date between 03:38 and 05:29 UTC.
*   **Next Step**: Execution of the shutdown process contingent upon Daryl Ng delivering the required written notification/ticket.

**Resource Reference**
*   Space URL: https://chat.google.com/space/AAAAQezbuRE


## [30/30] Alvin Choo
Source: gchat | Group: dm/zmMZpgAAAAE | Last Activity: 2026-03-20T04:09:06.293000+00:00 | Last Updated: 2026-03-20T16:00:34.978644+00:00
**Daily Work Briefing: RMN & Postmortem Updates**
**Resource:** Alvin Choo (Lead/Manager) | **Participant:** Michael Bui (Domain Expert, Backend Dev)
**Date Range:** March 3 – March 20, 2026

### **Key Participants & Roles**
*   **Alvin Choo:** Leads coordination for RMN postmortem reports, prioritization, performance management (PM25), and upcoming workshop preparation.
*   **Michael Bui:** Domain expert for RMN; responsible for backend implementation, documentation, design plans, and travel logistics support.

### **Main Topics**
1.  **RMN Postmortem & Incident Review:** Finalizing the report for BCRS completion, addressing "Overage on transaction sync," and "Transition to impressions-based model."
2.  **Upcoming Workshop Preparation:** Aligning on integration flow and timing for Sept milestones; focus on new app and Smart Cart expectations.
3.  **Technical Implementation:** Backend-only work for RMN tickets; integration with Advertima (Grassfish CMS) and Vijaykumar (PDA owner).
4.  **Project Prioritization & Travel:** Deprioritized SAP invoice work due to low ROI. Confirmed travel destination is Wuhan, China, requiring visa checks.

### **Decisions Made**
*   **Workshop Deliverables:** Michael will prepare "as-is" and "to-be" design plans rather than full presentation slides; Alvin confirmed existing documents need only alignment ("gel it").
*   **Advertima Status:** Confirmed as a "Proof of Value" (POV) pilot operating without formal architecture approval until end of Q1 2026.
*   **Ticket Prioritization:** OMNI-1282 (SAP invoice) deprioritized; OMNI-1191 and OMNI-1247 remain active but OSMOS-focused.
*   **Travel Logistics:** Travel confirmed for Wuhan, China. Michael to check visa requirements immediately.

### **Pending Actions & Ownership**
| Action Item | Owner | Details/Context |
| :--- | :--- | :--- |
| **Workshop Prep (Design)** | Michael Bui | Create docs detailing "as-is" vs. "to-be" integration flows for new app and Smart Cart; share during progress. |
| **Postmortem Review** | Alvin Choo | Final review after PDA impact verification (Vijay) and Advertima POV status inclusion. |
| **Travel Visa Check** | Michael Bui | Investigate visa requirements for Wuhan, China following confirmation from Alvin. |
| **PDA Impact Verification** | Michael Bui | Confirmed no downstream impacts on operations with Vijaykumar@fairpricegroup.sg. |
| **GLMS Re-testing** | Michael Bui | RMN APIs fixed for Pentest issues (DPD-591); GLMS instructed to re-test. |
| **PM25 Rating Meeting** | Alvin Choo | Scheduled before March 30, 2026; Winson invited to join. |

### **Key Dates & Milestones**
*   **March 4:** Michael worked from home due to illness.
*   **March 5:** Segment update completed; Pentest fixes submitted for GLMS re-test.
*   **March 10:** Alvin committed to scheduling PM25 meeting before **end of March**.
*   **March 13:** Quick video call held to clarify OMNI ticket statuses.
*   **March 16:** Player Error [5100] identified as originating from Advertima (Grassfish CMS).
*   **Next Wednesday (Approx. March 25):** Alvin working from home; Workshop preparation due for alignment on integration flow and timing.
*   **End of Q1 2026:** Advertima POV pilot period concludes.
*   **March 19-20:** Discussion held regarding workshop scope (integration flow, Smart Cart) and travel to Wuhan.
