

## [1/54] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 16 | Last Activity: 2026-04-01T14:27:52.874000+00:00 | Last Updated: 2026-04-01T14:33:30.583359+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (Updated April 1, ~14:30 UTC)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
Instability in the `engage-my-persona-api-go` service and related downstream services persists into the afternoon of April 1. Following morning incidents (09:58–10:26 UTC), a new wave of latency spikes, error rate cycles, and endpoint failures emerged starting at **13:57 UTC**, affecting Identity, Gamification, Recommendation, and Personalization services.

**Status Summary & Timeline (April 1 Afternoon)**
*   **Identity API Instability (`engage-my-persona-api-go` / Squad Dynamics):**
    *   *Error Rate:* High error rate triggered at **13:57 UTC** (Value: 0.105) and remained cyclical, peaking again at **14:26 UTC**.
    *   *Latency Spikes:* `post_/new-myinfo/confirm` P90 latency spiked to **1.859s** at **14:17 UTC** (Recovered 14:27).
    *   *Phone Update Latency:* `put_/user/phone` P90 exceeded 4.0s (**5.091s**) and P99 exceeded 5.0s at **14:22 UTC**, recovering by 14:25 UTC.
    *   *Critical Success Rate Drops:*
        *   `post_/pwl/availability/phone-number` (Login/Signup) success rate dropped to **96.4%** at **14:25 UTC**.
        *   `post_/pwl/reverify` (Phone Re-verification) success rate plummeted to **90.9%** at **14:26 UTC**.
*   **Recommendation & Personalization Services:**
    *   *Orchid Failures:* Success rate for `get_/api/recommender/orchid` dipped to **99.676%** at **14:22 UTC** (Squad Journey).
    *   *Banner Loading:* `post_/banner` success rate dropped to **99.583%** at **14:17 UTC**, recovering by 14:18 UTC (Squad Compass).
    *   *Category Browse:* Success rate for `get_/api/layout/category/v2` dipped to **99.863%** at **14:17 UTC**, recovering by 14:27 UTC.
*   **Gamification:** The high error rate alert for `gamification-api` triggered at 13:57 but recovered immediately (Value: 0.0).

**Pending Actions & Ownership**
*   **Investigate Identity API Correlation:** Analyze the resurgence of error rates (>0.1) and critical `post_/pwl/reverify` failure (90.9%) alongside latency spikes on `put_/user/phone`. Owner: **Squad Dynamics**.
*   **Diagnose Phone Number Workflow:** Investigate the severe success rate drops for phone availability and re-verification endpoints at 14:25–14:26 UTC. Owner: **Squad Dynamics**.
*   **Monitor Recommendation Degradation:** Address Orchid failures (99.676%) observed at 14:22 UTC. Owner: **Squad Journey**.

**Decisions Made**
*   **Status Update:** Incident severity remains Critical due to continuous, cyclical failures across Identity (`engage-my-persona-api-go`) and Recommendation services extending from the morning through the afternoon (09:58–14:26 UTC).
*   **Pattern Confirmation:** The recurrence of latency exceeding 1.8s for `new-myinfo/confirm` and error rates >0.1 confirms a persistent instability cycle affecting multiple squads simultaneously.

**Key Dates & Follow-ups**
*   **Active Window:** April 1, 09:58 – 14:26 UTC (Latest Critical Activity).
*   **Reference Links (Latest):**
    *   `engage-my-persona-api-go` Error Rate Monitor #92965074 (Triggered: 13:57, Value: 0.105)
    *   `post_/pwl/reverify` Success Rate Monitor #17447647 (Triggered: 14:26, Value: 90.9%)
    *   `put_/user/phone` Latency Monitors #17447657/#17447659 (Triggered: 14:22, P99 Value: 5.091s)
    *   `get_/api/recommender/orchid` Monitor #17448311 (Triggered: 14:22, Value: 99.676%)


## [2/54] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-04-01T13:58:43.531000+00:00 | Last Updated: 2026-04-01T14:34:12.983465+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Update)**
**Date:** April 1, 2026 (Mid-Day Shift)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 842

### Key Participants & Roles
*   **System/Tool:** Datadog App (Automated Monitoring)
*   **Notification Channel:** `@hangouts-ShoppingCartNotification`
*   **Ownership Teams:** `dpd-pricing`, `dpd-pricing-cart`.

### Main Topic
Instability persists across `frontend-gateway` and `st-cart-prod`. The incident window has extended to 13:58 UTC on April 1, characterized by high-frequency oscillations (flare-ups every ~10–20 minutes) involving both success rate drops (<99.9%) and latency spikes (>thresholds) across Checkout, Cart Update, Wish List, and Shopping List endpoints. The P2 Error Budget Alert remains critical.

### Incident Timeline & Actions
**Previous Context:**
*   *Extended activity from March 20 through late March 31.*
*   *April 1 (04:18 – 08:52 UTC):* Earlier oscillation on Wish List latency and Checkout success rate dips noted in prior update.

**New Activity (April 1, 11:24 – 13:58 UTC)**
*   **11:24–11:47 UTC:** `st-cart-prod` (`post /cart`) success rate dropped to **99.787%**, recovered to 100%, then dipped again to **99.896%** before recovering at 11:47 UTC (Monitor ID 22710472).
*   **12:13–12:23 UTC:** `frontend-gateway` (`post /api/cart`) P99 latency spiked to **2.826s** (>2.6s threshold), recovering at 12:23 UTC (Monitor ID 21245713).
*   **13:43–13:44 UTC:** `frontend-gateway` (`get /api/wish-list/{_id}`) P90 latency reached **1.747s** (>1.7s threshold), recovering immediately (Monitor ID 21245720).
*   **13:48–13:58 UTC:** Simultaneous degradation observed:
    *   `get /api/v2/shopping-list` success rate dropped to **99.653%** (Recovered at 13:58 UTC, Monitor ID 21245735).
    *   `post /api/checkout` success rate dropped to **99.886%** (Recovered at 13:58 UTC with 99.911%, Monitor ID 21245708).

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** The failure pattern has intensified, showing a multi-service "cascade" effect where latency in `frontend-gateway` correlates with success rate drops in `st-cart-prod` within tight time windows (e.g., 13:48–13:50 UTC).
*   **Immediate Action Required:** Prioritize investigation into the correlation between the 12:13 UTC `post /api/cart` latency spike and the subsequent success rate drops at 11:24, 13:48, and 13:49 UTC. Trace root causes for cyclic throttling or database contention affecting both `frontend-gateway` and `st-cart-prod`.

### Decisions Made
*   **Priority Status:** Remains **"Critical Incident"**. The system exhibits a multi-service failure profile with active, recurring monitor triggers across four distinct endpoints today alone.
*   **Focus Shift:** Priority must remain split between `post /api/checkout` success rates (currently oscillating between 99.8–100%) and latency monitoring for both `get /api/v2/shopping-list` and `get /api/wish-list/{_id}`.
*   **Metric Update:** Latest recorded Checkout P99 peak remains 20.242s (Mar 31); latest Wish List P99 peak is 6.838s (Apr 1). New low points: Cart Update success **99.787%** (11:24 UTC) and Shopping List success **99.653%** (13:48 UTC).

### Key Dates & Follow-ups
*   **Critical Window:** Extended activity from March 20 through at least April 1, 13:58 UTC.
*   **Follow-up:** Immediate trace correlation for the 11:24–13:58 UTC window to determine if `frontend-gateway` and `st-cart-prod` share a common root cause (e.g., database lock) driving this high-frequency cyclic failure.

### References
*   **Active Monitors:** `21245708` (Checkout Success), `22710472` (Cart Update Success), `21245713` (Cart P99 Latency), `21245720` (Wish List P90), `21245735` (Shopping List Success).
*   **SLO Monitor:** `8569058961838035695` (Error Budget Alert, ID 21245791).
*   **Service Tags:** `service:frontend-gateway`, `service:st-cart-prod`, `team:dpd-pricing`.


## [3/54] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw | Messages: 3 | Last Activity: 2026-04-01T13:51:21.196000+00:00 | Last Updated: 2026-04-01T14:34:59.202758+00:00
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

**Pending Actions & Owners**
*   **FPPay Image Team (Andin Eswarlal Rajesh, DevOps):** Investigate root cause of banner image loading failures in production and deploy fix. Priority: High.
*   **S&G Verification Team (Vivian Lim Yu Qian, Product/Dev Teams):** Investigate current S&G flows against the WIP verification logic document to confirm if forced staff verification screens exist for restricted SKUs like milk powder. Reference: `https://ntuclink.atlassian.net/wiki/spaces/SE/pages/1995997683/WIP+S+G+Verification+Flow`.
*   **Incident Response Team (Jazz Tong, Akash Gupta, Gopalakrishna Dhulipati, Kyle Nguyen):** Act as support guides for the active DPD Incidents channel; monitor and resolve incoming incident queries.
*   **GP Team (Nicholas Tan / Mohit Niranwal):** Investigate Bitnami image replacement strategy to resolve TTR issues and update Golden Pipeline dependencies.
*   **iOS/Dev Team (Tiong Siong Tee):** Re-verify the previously identified iOS FPPay QR code login bypass bug status.
*   **Security Team (Mohammad Adyatma, All Devs):** Audit all projects for `axios` dependency versions to mitigate risks associated with the reported npm package compromise. Reference: `https://socket.dev/blog/axios-npm-package-compromised`.
*   **FPG Bonus Discussion (Wai Ching Chan):** Review details regarding FPG bonus distribution and linked content.

**Decisions Made**
*   No formal change freeze; feature releases are currently active (Alvin Choo).
*   Datadog team configurations must strictly follow Infrastructure as Code (Terraform) protocols; manual overrides are deprecated.
*   Miro's acquisition of Reforge is recognized as a strategic move to bridge product strategy and delivery gaps.
*   **New:** Active incident support protocol established for Jazz Tong, Akash Gupta, Gopalakrishna Dhulipati, and Kyle Nguyen on March 27, 2026.
*   **New:** Winson Lim endorsed the `affaan-m/everything-claude-code` repository as a key resource for AI-first engineering patterns and skill development.

**Key Dates & Follow-ups**
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


## [4/54] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Messages: 16 | Last Activity: 2026-04-01T11:12:12.455000+00:00 | Last Updated: 2026-04-01T14:35:29.758606+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Apr 1, 11:12 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`.
*   **Escalations:** `@oncall-dpd-staff-excellence-pdm`, `@hangouts-GT-Search-DatadogAlerts`, `@hangouts-GT-Discovery-DatadogAlerts`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Retail Media.

**Main Topic**
**P2 INCIDENTS (RESOLVED):** High error rate for `marketing-service` on `env:prod`.
*   **Current Status:** Resolved at 11:12 UTC on Apr 1. No active incidents remain.
*   **Incident Timeline:**
    *   Triggered: Apr 1, 11:03 UTC (Metric value: 0.011 error ratio).
    *   Recovered: Apr 1, 11:12 UTC (Metric value: 0.003 error ratio).

**Resolved Incidents**
*   **`marketing-service` (Error Rate):** P2 anomaly triggered at 11:03 UTC on Apr 1; recovered at 11:12 UTC.
    *   *Query:* `sum(last_10m):( sum:trace.http.request.errors{env:prod,service:marketing-service}.as_count()/sum:trace.http.request.hits{env:prod,service:marketing-service}.as_count() ) > 0.05`.
    *   *Details:* Error rate spiked to 1.1% (threshold > 5%). Monitor ID `17447106`.
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/17447106) | [K8s](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview) | [Runbook](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book)
*   **`go-catalogue-service` (Latency):** P3 anomaly triggered at 07:54 UTC; recovered at 09:10 UTC (Previously resolved).
    *   *Query:* `percentile(last_20m):p90:trace.http.request{env:prod,service:go-catalogue-service,resource_name:get_/category/_id} > 2`.
*   **`marketing-service` (Throughput):** P4 anomaly triggered at 03:54 UTC; recovered at 05:04 UTC (Previously resolved).

**Pending Actions & Ownership**
*   **Action:** **POST-INCIDENT REVIEW (`marketing-service` Error Rate):** [Status: OPEN] New P2 error rate event detected this morning (11:03–11:12 UTC). Determine if RCA is needed alongside previous throughput anomalies.
    *   **Owner:** Retail Media Team / Product Data Management.
*   **Action:** **POST-INCIDENT REVIEW (`go-catalogue-service`):** [Status: OPEN] Follow-up required for the 07:54–09:10 UTC latency spike to determine if RCA is needed.
    *   **Owner:** Product Data Management (`team:dpd-staff-excellence-pdm`).

**Decisions Made**
*   The `marketing-service` error rate spike was transient and self-resolving within 9 minutes (11:03 to 11:12 UTC). No manual restart required.
*   Previous throughput anomalies for `marketing-service` (Mar 31/07:54) were transient, self-resolving within ~54–70 minutes.

**Key Dates & Follow-ups (Mar 31 – Apr 1, 2026)**
*   **Service: `marketing-service` (P2 - Retail Media) [RESOLVED]**
    *   *Latest Timeline:* Triggered Apr 1, 11:03 UTC; Recovered Apr 1, 11:12 UTC.
    *   *Details:* P95 error rate exceeded 5% threshold in production.
*   **Service: `go-catalogue-service` (P3 - Product Data Management) [RESOLVED]**
    *   *Latest Timeline:* Triggered Apr 1, 07:54 UTC; Recovered Apr 1, 09:10 UTC.

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c


## [5/54] QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs | Messages: 7 | Last Activity: 2026-04-01T10:59:53.042000+00:00 | Last Updated: 2026-04-01T14:36:41.626867+00:00
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
1.  **Pipeline Error (Critical):** On **31 Mar**, Hang Chawin Tan reported a pipeline failure in `dp-gifting-web`. *Status:* Active discussion involving @Madhuri Nalamothu, @Milind Badame, and @Oktavianer Diharja awaiting resolution.
2.  **BCRS Swimlane Management:** On **31 Mar**, Milind Badame queried if BCRS swimlanes can be disabled post-UAT. *Status:* Discussion ongoing with @Daryl Ng and @Andin Eswarlal Rajesh to determine cleanup protocols.
3.  **BackOffice Domain Validation (New):** On **2026-04-01 10:59**, Milind Badame identified a validation gap where BackOffice accepts full invalid domains. *Status:* Awaiting investigation from @Daryl Ng.
4.  **System-Wide Intermittent Failures:** On **30 Mar**, Milind Badame reported frequent HTTP 500 errors affecting order placement, cart, and PDP pages. *Status:* Active investigation for backend instability vs. testing impact.
5.  **Order Placement Failure ('Strong Tasty Brew'):** On **30 Mar**, Madhuri Nalamothu reported inability to place orders for non-FP product 'Strong Tasty Brew'. Discussion ongoing with @Piraba Nagkeeran.
6.  **MiniGames Blank Screen:** On **30 Mar**, Milind Badame reported a blank white screen when tapping the MiniGames tile as a guest user followed by login on lower Android versions. *Owner:* @Aman Saxena, Mobile Team.
7.  **DC Membership Subscription Issue:** On **30 Mar**, Madhuri Nalamothu confirmed subscription failures impact both new and existing users. *Owner:* @Kadar Sharif.
8.  **LinkPoints Regression Failure:** Reported on **27 Mar** regarding CLS Award Balance API `500` errors. Status remains Critical/Blocked pending resolution with @Pandi.
9.  **JWC & Express Delivery Timeouts:** On **1 Apr**, Milind Badame flagged E2E test failures due to store timings. Request raised to configure JWC and Express Delivery timings for **24x7** in UAT. *Status:* Pending advice from @Andin Eswarlal Rajesh and @Daryl Ng.
10. **Express Delivery Service Fee Logic:** On **1 Apr**, Milind Badame reported service fees are not waived when the amount exceeds $30. *Status:* Awaiting investigation by @Daryl Ng.
11. **Unlimited Product API Error:** On **1 Apr**, Milind Badame queried behavior when calling APIs to increase counts for products set as unlimited in BackOffice. *Status:* Under review with @Wai Ching Chan and @Andin Eswarlal Rajesh.
12. **Tile Customization - PreOrder:** On **2026-04-01 10:18**, Milind Badame asked if tiles can be customized to include "PreOrder" functionality. *Status:* Pending response from @Daryl Ng (Latest activity: ~1 hour ago).

**Pending Actions & Ownership**
*   **Pipeline Resolution:** Resolve `dp-gifting-web` pipeline error reported by @Hang Chawin Tan. *Owners:* @Madhuri Nalamothu, @Milind Badame, @Oktavianer Diharja. **(Highest Priority)**
*   **BackOffice Validation Fix:** Investigate and prevent invalid domain entries in BackOffice. *Owner:* @Daryl Ng. *(New)*
*   **Tile Customization Inquiry:** Confirm feasibility of adding PreOrder logic to tiles. *Owner:* @Daryl Ng.
*   **BCRS Cleanup Strategy:** Confirm feasibility of disabling BCRS swimlanes post-UAT. *Owners:* @Daryl Ng, @Andin Eswarlal Rajesh.
*   **System Stability Investigation:** Identify cause of widespread HTTP 500 errors on PDP/Cart/Order Placement (30 Mar). *Owner:* Dev Team / @Hang Chawin Tan.
*   **MiniGames Crash Fix:** Resolve blank screen issue on MiniGames tile for guest users/login flow. *Owner:* @Aman Saxena.
*   **DC Membership Fix:** Resolve subscription failures impacting all user segments. *Owner:* @Kadar Sharif. **(Critical)**
*   **UAT Timezone Configuration:** Configure JWC and Express Delivery timings for 24x7 to prevent test failures. *Owners:* @Andin Eswarlal Rajesh, @Daryl Ng.
*   **Service Fee Logic Fix:** Investigate why fees are not waived for orders >$30 on Express Delivery. *Owner:* @Daryl Ng.
*   **API Behavior Verification:** Clarify error handling for unlimited product count increments. *Owners:* @Wai Ching Chan, @Andin Eswarlal Rajesh.

**Decisions Made**
*   System-wide errors on 30 Mar require immediate triage; potential testing activity suspected but not yet confirmed as root cause.
*   DC Membership issue escalated to @Kadar Sharif due to scope affecting existing users.
*   MiniGames blank screen investigation assigned to @Aman Saxena.
*   E2E test failures attributed to store timings require UAT configuration adjustment (24x7).
*   Tile customization for PreOrder is currently under review by Product/Dev.
*   BackOffice domain validation gap identified; requires immediate Dev attention.

**Key Dates & Deadlines**
*   **2026-04-01 10:59:** BackOffice invalid domain issue raised by @Milind Badame; awaiting response from @Daryl Ng.
*   **2026-04-01 10:18:** Tile Customization inquiry raised by @Milind Badame.
*   **1 Apr:** JWC/Express timing query, Service fee logic issue, and Unlimited product API behavior raised.
*   **31 Mar (Morning):** Pipeline error reported; BCRS swimlane query raised.
*   **30 Mar (Morning/Afternoon):** System-wide 500 errors, Cart issues, 'Strong Tasty Brew' failure, MiniGames blank screen, DC membership issue confirmed.
*   **27 Mar:** LinkPoints API failure and iOS SnG Flow loading stuck.
*   **26 Mar:** Express cart service fee discrepancy.


## [6/54] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/1UILrDfoupI | Last Activity: 2026-04-01T10:27:09.511000+00:00 | Last Updated: 2026-04-01T10:36:40.850063+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Resource:** [Leads] (Ecom/Omni) Digital Product Development
**Date of Discussion:** April 1, 2026
**Participants:** Sneha Parab, Daryl Ng

**Key Participants & Roles**
*   **Sneha Parab:** Product/Functional Lead raising technical constraints and migration risks.
*   **Daryl Ng:** Technical Lead providing feasibility assessment.

**Main Topic**
Technical feasibility of preventing migrated customers from placing orders in the existing B2B platform while retaining access to other channels. The core issue involves a customer scenario where users have dual access (B2C and B2B) on the current platform but are migrating to a new platform with separate logins.

**Discussion Summary & Decisions**
*   **Feasibility:** Sneha Parab asked if it is possible to block users from placing orders *only* in B2B based on user identification. Daryl Ng immediately indicated this is not technically feasible ("haha i don't think so").
*   **Migration Logic:** The proposed strategy was to allow customers to access the new platform while blocking them on the old B2B instance post-migration.
*   **Constraint Analysis:** Sneha Parab clarified that suspending a customer account on the current platform is not an option because these users also require access to B2C channels, which remain active on the same login system.
*   **Risk Assessment:** Sneha Parab noted she has previously communicated that attempting this partial blocking creates more operational issues than it solves.

**Pending Actions & Ownership**
*   **Action:** Provide final verdict/decision on how to proceed given the technical impossibility and operational risks.
*   **Owner:** Daryl Ng (requested explicitly by Sneha Parab at 10:27 AM).

**Key Dates & Follow-ups**
*   **Discussion Date:** April 1, 2026.
*   **Time of Request for Verdict:** 10:27:09 UTC.
*   **Follow-up Required:** Immediate decision from Daryl Ng to conclude the discussion on blocking logic.

**Reference URLs**
*   Chat Space: https://chat.google.com/space/AAQAN8mDauE


## [7/54] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/ODwikuuIYPU | Last Activity: 2026-04-01T10:15:12.442000+00:00 | Last Updated: 2026-04-01T10:38:12.506146+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Initiator of the invitation request.
*   **Daryl Ng:** Coordinator responsible for sending invitations; owner of "Search & Agolia context" knowledge.
*   **Tiong Siong Tee:** Stakeholder requesting information; confirmed receipt of the invitation.

**Main Topic**
The discussion centers on expanding the participant list for the "Project Light Attack and Defence Leads" space and scheduling a follow-up session to discuss technical search and Agolia context details.

**Decisions Made**
*   **Invitation Authorization:** Alvin Choo confirmed that an additional person should be invited to the group chat.
*   **Action Execution:** Daryl Ng successfully executed the invitation immediately after confirmation (06:45).
*   **Knowledge Sharing Commitment:** Tiong Siong Tee and Daryl Ng agreed that a discussion regarding "search & agolia context" is required, with Daryl Ng confirming his availability to provide this context.

**Pending Actions & Owners**
*   **Action:** Conduct a meeting or session to review search and Agolia context.
    *   **Owner:** Tiong Siong Tee (to find/schedule) and Daryl Ng (to provide context).
    *   **Status:** Awaiting scheduling; Daryl has verbally committed ("can") but no specific time is set yet.

**Key Dates, Deadlines & Follow-ups**
*   **2026-04-01 06:44:36 UTC:** Alvin Choo requested an invitation.
*   **2026-04-01 06:45:09 UTC:** Daryl Ng confirmed the person was invited.
*   **2026-04-01 08:11:05 UTC:** Tiong Siong Tee acknowledged receipt of the invitation ("thanks").
*   **2026-04-01 10:15:02 UTC:** Tiong Siong Tee initiated the request for the search/Agolia context session, tagging Daryl Ng.
*   **2026-04-01 10:15:12 UTC:** Daryl Ng confirmed availability to meet on this topic.

**Reference Links**
*   Chat Space URL: https://chat.google.com/space/AAQAsFyLso4


## [8/54] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/pA7_pZifIOE | Last Activity: 2026-04-01T10:09:56.915000+00:00 | Last Updated: 2026-04-01T10:38:36.810186+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Project Lead/Coordinator.
*   **De Wei Tey:** Technical Owner/RPA Lead (managing deployments, RPA logic, and production pushes).
*   **David Anura Cooray:** QA/Testing Lead.
*   **Joey Ang Hui Xin:** Operations/Front-end Tester (executing live order placement/refunds).
*   **Hendry Tionardi & Onkar Bamane:** Finance/System Integration (monitoring SAP, managing reversals).
*   **Zack Chan & Binte Abdul Karim Kamilah:** CS/Finance Support (handling manual fee refunds).

**Main Topic**
Validation and production deployment of the RPA refund feature for **BCRS (Scan & Go)**. The discussion confirmed live testing success for specific SKUs, managed financial reversals for test transactions, and addressed a user request regarding the non-automated refund of packing and delivery fees.

**Decisions Made**
1.  **RPA Scope Confirmation:** Confirmed RPA performs BCRS refunds but does not automatically cover packing/delivery fees. Manual intervention is required for these specific fees.
2.  **Manual Fee Refund Protocol:** For Order ID `259022496`, manual refund of packing and delivery fees ($8.99) was triggered by Finance/CS after confirmation that RPA does not cover these charges.
3.  **Ticket Closure:** CS ticket (ID: 4468575) regarding the live test refund was approved for closure after all refunds (SKU, BCRS, and fees) were processed.

**Pending Actions & Ownership**
*   **Manual Fee Refund Completion:** Confirmed completed by **Binte Abdul Karim Kamilah**.
    *   *Amount:* $8.99 (Delivery and Service fee).
    *   *Order ID:* `259022496`.
*   **Finance Reversal of Test Refund:** Finance to revert the test refund transaction generated during live testing.
    *   *Order IDs:* `259017167` (iOS), `259018320` (Android), and `259022496`.
    *   *Owner:* **Onkar Bamane** to inform Finance; **De Wei Tey** confirmed the RPA will refund these orders.
*   **SAP Monitoring:** Continued monitoring of SAP postings for test transactions.
    *   *Owner:* **Hendry Tionardi**.

**Key Dates & Deadlines**
*   **Critical Deadline:** **1 April 2026** (All sign-offs confirmed completed).
*   **Testing Execution Date:** **31 March 2026** (Live testing conducted between 06:26 and 07:32 UTC+8).
*   **Refund Log Timestamps:** Updates recorded on **1 April 2026** between 08:35 and 10:09 UTC+0.

**Specific References & New Findings**
*   **Tested Order ID:** `259022496`.
    *   *SKU:* 13280919 (BCRS).
    *   *RPA Refund Amount:* $0.10.
    *   *Outcome:* RPA successfully refunded SKU and BCRS amount; Packing/Delivery fees ($8.99) required manual processing by **Binte Abdul Karim Kamilah**.
*   **Zendesk Ticket:** `4468575`. Routed to store, then escalated for fee refund assistance. Closed after resolution.
*   **Environment:** Testing confirmed in the Live Environment at 07:19 UTC+8 equivalent.

**Status Update**
Live testing for BCRS refunds is successful regarding SKU and BCRS amounts. A procedural gap was identified where packing/delivery fees are excluded from automated RPA flows; this has been mitigated via manual processing for the test transaction. No impact on First Response or other CS automated processes remains.


## [9/54] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Last Activity: 2026-04-01T09:54:27.077000+00:00 | Last Updated: 2026-04-01T10:39:12.206525+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Sneha Parab:** Lead/Manager; coordinating cross-team support, SAP/API integration blockers. Recently queried B2B user blocking logic for migrated customers.
*   **Michael Bui:** Engineering/RMN Architect; identified root cause for RMN incident and preparing UAT verification.
*   **Daryl Ng:** Investigating store network ownership and Omni Home data discrepancies. Flagged Linkpoints eligibility issue (April 1). Inquired about learning budget (Sundy's course) and S&G Store Enabling SOP adherence. Currently replying to B2B blocking use case discussion.
*   **Alvin Choo:** Leadership; addressing approval workflows for weekend deployments. Also consulted regarding Sundy's training budget inquiry.
*   **Gopalakrishna Dhulipati:** On Child Care Leave until Wednesday (April 2). Will reach out individually if assistance is required to rep tasks.

**Main Topics & Updates**
1.  **RMN Incident & Deployment Status:** Michael Bui identified the root cause and implemented a fix. Daryl Ng confirmed active inquiry regarding deployment status on March 31 (01:44 UTC). Immediate guidance remains required on weekend (Sat/Sun) deployment protocols, requiring an approval request to Hui Hui.
2.  **Linkpoints Eligibility Issue:** On April 1 at 03:13 UTC, Daryl Ng flagged that Wei Sing's team enabled "Linkpoints eligible" in SAP, but it remains disabled in DBP. Investigation is underway.
3.  **Search Performance Drop:** Investigation continues regarding the severe 60–70% impression decline since March 18/19. The RMN root cause fix may correlate with these symptoms; release timing remains contingent on this investigation and UAT success.
4.  **B2B Order Blocking Use Case (New):** Sneha Parab proposed blocking migrated customers from placing orders in the existing B2B platform by identifying user types during migration. Active discussion ongoing between Sneha and Daryl Ng.
5.  **S&G Store Enabling SOP:** Daryl Ng queried on April 1 (09:18 UTC) regarding current adherence to the "S+G Store Enabling - SOP" document. Thread has generated 18 replies; last reply by Sneha Parab 41 minutes ago.
6.  **Learning Budget Inquiry:** On April 1 at 06:51 UTC, Daryl Ng asked Alvin Choo if the learning budget is still available for Sundy to attend a specific course.

**Pending Actions & Owners**
*   **RMN Deployment Verification:** Confirm if the fix has been deployed following Daryl Ng's inquiry and proceed with UAT verification. Send approval request to Hui Hui for weekend deployment if applicable. (Owner: Michael Bui; Coordination: Alvin Choo/Hui Hui/Daryl Ng)
*   **Linkpoints Investigation:** Verify why "Linkpoints eligible" is disabled in DBP despite SAP enablement by Wei Sing's team. Follow up with Daryl Ng/Sneha Parab. (Owner: To be assigned/Wei Sing's team; Coordination: Sneha Parab/Daryl Ng)
*   **B2B Logic Feasibility:** Evaluate technical possibility of blocking migrated users from B2B orders based on identification logic. (Owner: Engineering Team; Discussion Owner: Daryl Ng/Sneha Parab)
*   **SOP Adherence Confirmation:** Clarify current status of the S&G Store Enabling SOP to address Daryl Ng's query. (Owner: To be assigned; Coordination: Sneha Parab/Daryl Ng)
*   **Training Budget Check:** Confirm availability of learning budget for Sundy's course request. (Owner: Alvin Choo/Sundeep's team lead)
*   **Epic Closure Validation:** Determine if DPD-710 can be closed given the March 19 live date discrepancy. (Owner: Michael Bui; Requestor: Sneha Parab)
*   **SIT Delivery Assessment:** Evaluate KT feasibility to complete SIT before April 6/7. (Owners: Michael Bui/Daryl Ng)
*   **Store Network Ownership:** Confirm scope under Data COE vs. Miguel's team regarding `Omni Home` store ID mismatch (OMNI-1157). (Owner: Daryl Ng/Michael Bui)
*   **SAP Timeline Resolution:** Resolve deposit SKU data integration blockers. *Note: Gopalakrishna Dhulipati is on leave until Wednesday; individual rep requests will be made if needed.* (Owners: Sneha Parab/Alvin Choo/Gopalakrishna Dhulipati)
*   **RAW Forms Review:** Complete Risk Register review for DPD RAW forms; confirm handovers and renew expired forms by Tomorrow EOD. (Owner: All Leads/Sazali Bin Mohammed Ali's team)

**Decisions Made & Status Changes**
*   **RMN Deployment Inquiry:** Daryl Ng raised a query on March 31 regarding the deployment status of the RMN fix, indicating active monitoring of the release phase.
*   **Linkpoints Discrepancy (New):** SAP enablement by Wei Sing's team does not reflect in DBP status; root cause analysis required.
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


## [10/54] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/9KYZsmc-670 | Last Activity: 2026-04-01T09:50:13.304000+00:00 | Last Updated: 2026-04-01T10:39:28.156890+00:00
**Daily Work Briefing: S&G Store Enablement Discussion**

**Key Participants & Roles**
*   **Daryl Ng:** Digital Product Development (Inquiry lead, capacity planning).
*   **Sneha Parab:** Digital Product Development / SME (Process owner, technical implementation).

**Main Topic**
Assessment of effort and timeline for a potential temporary "Pop-up S&G" store setup at Jewel. Discussion focused on verifying current Standard Operating Procedures (SOPs), identifying dependencies, and establishing the request submission workflow.

**Decisions Made**
*   **Documentation:** The previously cited SOP is outdated. The team agreed to utilize the automated process established by Hanafi, referencing version 3.0 of the store setup doc or the new Jira form.
*   **Workflow Confirmation:** Sneha Parab confirmed that while SAP handles master data downloads directly to GCS (reducing manual work), the Digital Product Development (DPD) team must still create the store in DBP and coordinate with the DE team for search/browse data flow upon receiving Stock on Hand (SOH).
*   **Timeline Estimate:** The end-to-end lead time is estimated at approximately 2 weeks.

**Pending Actions & Ownership**
1.  **Submit Request Ticket:**
    *   **Owner:** David (via Brendon from CCMO team or direct assignment).
    *   **Action:** Submit the pop-up store request immediately using the new Jira form to prevent delays, as the team will be busy starting next week.
    *   **Reference Form:** https://ntuclink.atlassian.net/jira/core/projects/STOR/form/577
2.  **Ticket Assignment:**
    *   **Owner:** David (upon ticket creation).
    *   **Action:** Assign the created ticket to Hanafi for processing.
3.  **Stakeholder Coordination:**
    *   **Owner:** Daryl Ng / Brendon.
    *   **Action:** Confirm with Brendon regarding awareness of this specific request and ensure proper handover if he is not the originator.

**Key Dates & Follow-ups**
*   **Event Timeline:** The popup store event is likely to occur approximately 3 weeks from today (April 1, 2026).
*   **Current Date:** April 1, 2026.
*   **Capacity Check:** Urgent need to submit the request now to accommodate the team's increased workload starting next week.

**Reference Links**
*   Outdated SOP: https://ntuclink.atlassian.net/wiki/spaces/SE/pages/1995999558/S+G+Store+Enabling+-+SOP
*   Current Setup Doc (v3.0): https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008160308/Store+setup+doc+v3.0


## [11/54] D&T Funtastic Team
Source: gchat | Group: space/AAQARGCS1Wk/5YZW6i2wniE | Last Activity: 2026-04-01T09:17:55.052000+00:00 | Last Updated: 2026-04-01T10:39:57.113264+00:00
**Daily Work Briefing: D&T Funtastic Team**

**Key Participants & Roles**
*   **Trina Boquiren:** Initiator, project lead for the International Food Day eDM design selection, and active follow-up on voting.
*   **Team (@all):** Stakeholders responsible for reviewing options and casting votes.

**Main Topic**
Selection of the final email design (eDM) for the upcoming **International Food Day**. Trina presented three shortlisted design concepts to gather team consensus on which best represents the event's spirit.

**Pending Actions & Ownership**
*   **Action:** Review the three provided design options and vote for the top two favorites using reaction emojis ("on" the images).
*   **Owner:** All team members.
*   **Context:** Voting is required to determine the final design choice based on collective preference. Trina sent a direct reminder to the team on April 1, 2026, urging immediate participation: "pls vote on the design you want for our International Food Day."

**Decisions Made**
*   No final decision has been made yet; the process remains in the voting phase. The final selection will be determined by the aggregate votes received from the team following the initial request and subsequent reminders.

**Key Dates & Follow-ups**
*   **Event:** International Food Day (Upcoming).
*   **Discussion Timeline:**
    *   **March 31, 2026:** Initial design posting occurred between 06:11 and 06:14 UTC; voting requested at 06:07 UTC.
    *   **April 1, 2026 (09:17 UTC):** Trina Boquiren issued a follow-up reminder to the @all channel to ensure votes were cast.
*   **Next Step:** Completion of voting to finalize the design before the event date.

**Reference Data**
*   **Space URL:** https://chat.google.com/space/AAQARGCS1Wk
*   **Message Count:** 5 (Increased from previous count due to new follow-up).
*   **Options Presented:** Option 1, Option 2, Option 3.


## [12/54] Release - FPG Back Office (Mon-Thurs)
Source: gchat | Group: space/AAAAoJgpZBM | Last Activity: 2026-04-01T09:14:20.453000+00:00 | Last Updated: 2026-04-01T10:40:38.072140+00:00
**Daily Work Briefing: FPG Back Office Releases (Updated)**

**Key Participants & Roles**
*   **Rohit Pahuja:** Primary communicator for scheduled releases.
*   **Jonathan Tanudjaja:** Executor for previous urgent release v8.37.1.
*   **Minu Varghese:** New executor for immediate release v8.37.2 (effective April 1, 2026).

**Main Topic**
The conversation tracks confirmed software deployment schedules for the **Back Office** system across versions **v8.35.0**, **v8.36.0**, **v8.37.0**, **v8.37.1**, and the newly announced urgent release of **v8.37.2**. All updates align with the FPG Back Office (Mon-Thurs) resource schedule.

**Pending Actions & Ownership**
*   **Action:** Monitor the Back Office system during release execution for all scheduled versions.
    *   **Owner:** Team.
*   **Action:** Review specific release notes upon receipt.
    *   **Owner:** Team members referencing provided links.
*   **New Action:** Execute deployment of version **v8.37.2** immediately.
    *   **Owner:** Minu Varghese.
    *   **Note:** Release notes to be shared shortly by the executor.

**Decisions Made**
No new strategic decisions were made; messages confirm a sequence of five deployment plans:
1.  Deployment of **Backoffice_v8.35.0**.
2.  Deployment of **Backoffice_v8.36.0**.
3.  Deployment of **Backoffice_v8.37.0**.
4.  Deployment of **Backoffice_v8.37.1** (Completed March 25, 2026).
5.  **Deployment of Backoffice_v8.37.2** (Newly initiated by Minu Varghese on April 1, 2026).

**Key Dates, Deadlines, & Follow-ups**
*   **Release 1:**
    *   **Version:** Backoffice_v8.35.0
    *   **Announced:** March 9, 2026, at 05:11 UTC.
    *   **Scheduled Execution:** ~1:20 PM on March 9, 2026.
*   **Release 2:**
    *   **Version:** Backoffice_v8.36.0
    *   **Announced:** March 12, 2026, at 13:44 UTC.
    *   **Scheduled Execution:** Same day (March 12, 2026).
*   **Release 3:**
    *   **Version:** Backoffice_v8.37.0
    *   **Announced:** March 24, 2026, at 02:17 UTC.
    *   **Scheduled Execution:** Same day (March 24, 2026).
*   **Release 4:**
    *   **Version:** Backoffice_v8.37.1
    *   **Announced:** March 25, 2026, at 02:33 UTC.
    *   **Scheduled Execution:** Today (March 25, 2026) by Jonathan Tanudjaja.
*   **Release 5 (New):**
    *   **Version:** Backoffice_v8.37.2
    *   **Announced:** April 1, 2026, at 09:14 UTC.
    *   **Scheduled Execution:** Immediate execution by Minu Varghese.
    *   **Status:** Release notes pending (to be shared soon).

**Contextual Notes**
*   These updates align with the resource schedule for **FPG Back Office (Mon-Thurs)**.
*   The v8.37.2 release follows a rapid succession of hotfixes/updates initiated by different team members (Jonathan Tanudjaja previously, now Minu Varghese).


## [13/54] AdOps x Osmos
Source: gchat | Group: space/AAQAHz9NRfw | Last Activity: 2026-04-01T08:52:13.872000+00:00 | Last Updated: 2026-04-01T10:41:58.910674+00:00
**Daily Work Briefing: AdOps x Osmos**

**Key Participants & Roles**
*   **Prajwal Prakash:** Requestor/Ad Ops (Initiated ticket, driving urgency for ad launch).
*   **Shubhangi Agrawal:** Support/Operations (Owner of the support ticket status check).

**Main Topic**
Urgent status inquiry regarding a blocked workflow preventing the creation of ads for an imminent launch. Prajwal Prakash raised a specific support ticket yesterday to resolve this technical or procedural blockage.

**Pending Actions & Ownership**
*   **Action:** Provide status update and expedite resolution on ticket #112743.
*   **Owner:** Shubhangi Agrawal.
*   **Context:** Prajwal confirmed receipt of the request at 07:48 but followed up again at 08:52 with "Any update??" indicating the initial acknowledgment has not yet resulted in a solution or detailed status report.

**Decisions Made**
*   None recorded. The conversation currently reflects an active bottleneck where support intake was acknowledged, but no technical resolution or timeline was agreed upon by the close of this thread.

**Key Dates & Deadlines**
*   **Ticket Raised:** April 1, 2026 (Yesterday relative to chat context).
*   **Launch Deadline:** Today's launch ("tmrw" in the original message refers to the day after the ticket was raised, which is today, April 1, 2026).
*   **Follow-up Timestamps:**
    *   Initial request: 07:44 AM.
    *   Acknowledgment: 07:48 AM.
    *   Urgency escalation (No update received): 08:52 AM.

**Critical Constraint**
The inability to create ads is actively blocking the launch scheduled for today, April 1, 2026. Immediate attention from Shubhangi Agrawal is required to prevent a missed launch window.


## [14/54] ❗ Important Email
Source: gchat | Group: space/AAQAUJW8HMo | Last Activity: 2026-04-01T08:30:23.223000+00:00 | Last Updated: 2026-04-01T10:42:29.631720+00:00
**Daily Work Briefing Summary (Updated)**

**Key Participants & Roles**
*   **Michael Bui (You):** Managing Osmos support, event RSVPs, FileVault compliance, performance feedback, Project Light coordination, AI training follow-ups, GCP Service Account security, and D&T Power Breakfast engagement.
*   **Alvin Choo:** Organizer of the joint DPD, Core Product, and Picking Teams meeting (Apr 2).
*   **Sip Khoon Tan / FPG AI CoE:** Coordinating weekly AI guidance sessions and launching the Agentic Evolution Contest.
*   **Trina Boquiren:** Host of D&T Power Breakfasts (Last Thursday monthly); Organizer of upcoming April 28 event.
*   **Kyle Nguyen / Nicholas Tan:** Leading legacy GCP SA key remediation (starts week of Mar 30).

**Main Topics**
1.  **GCP Security & Service Account Decommissioning:**
    *   **Objective:** Clean up legacy keys; immediate focus on non-production (56 keys) and automated rotation.
    *   **Timeline:** Kyle Nguyen's team begins remediation week of March 30, 2026.
    *   **Action:** Review spreadsheet to indicate consent for automated key rotation.

2.  **AI Training & Agentic Evolution Contest:**
    *   **Weekly Support:** Google AI Specialists hosting 30-min sessions Wednesdays, 2:00–2:30 PM SGT (Mar 25 – May 31, 2026). Q&A document for March 19 session is available.
    *   **Agentic Evolution Contest:** Launched by FPG AI CoE & Google. Submissions accepted until **April 25, 2026**. Prizes include exclusive Google gear.

3.  **DPD, Core Product & Picking Teams Meeting:**
    *   **Event:** Joint meeting scheduled for **Thursday, April 2, 2026, 9:30 AM – 11:00 AM SGT**.
    *   **Location:** FairPrice Hub-13-L13 Heritage Room (50) + Google Meet (`mgv-sdor-ejt`).

4.  **D&T Power Breakfasts:**
    *   **Upcoming Event:** First meetup on **Tuesday, April 28, 2026, 9:00 AM – 10:30 AM SGT**.
    *   **Location:** FairPrice Hub Level 11, Lobby B Pantry (Virtual option via Google Meet available).
    *   **Future Schedule:** Hosted monthly on the **last Thursday** of every month by Trina Boquiren.

5.  **BCRS & Project Light:**
    *   **BCRS Regroup:** Thursday, March 26, 2026, 4:00–5:00 PM SGT (Organizer: Prajney Sribhashyam).
    *   **RMN Discussion:** Rescheduled to Thursday, March 26, 2026, 2:00–3:00 PM SGT.

**Pending Actions & Ownership**
*   **GCP Security Consent (Michael Bui):** Immediate Action Required. Review legacy SA spreadsheet and indicate consent for automated rotation.
*   **DPD/Core Product/Picking Meeting RSVP (Michael Bui):** Respond to April 2 invitation.
*   **Agentic Evolution Contest (Michael Bui):** Submit AI agent entry by **April 25, 2026**.
*   **Power Breakfast RSVP (Michael Bui):** Must click "Yes" on the calendar invitation by **April 24** to confirm attendance for April 28.
*   **BCRS Regroup & RMN Meetings (Michael Bui):** Confirm attendance for March 26 sessions (4:00 PM and 2:00 PM respectively). Note the scheduling conflict.

**Decisions Made**
*   **Agentic Evolution Contest:** Winners will receive Google gear; focus on ideas that eliminate toil and scale impact.
*   **RMN Integration Timeline:** Prioritized focused working session on March 26 for architecture definition.
*   **GCP Remediation Priority:** Highest priority is legacy key cleanup; dedicated Google Group to be created for weekly status updates.

**Critical Dates & Deadlines**
*   **Mar 18, 2026:** Performance Feedback Meeting.
*   **Mar 25–May 31, 2026:** Weekly AI Workbench Sessions (Wednesdays).
*   **Mar 26, 2026:** RMN Discussion (2:00 PM) & BCRS Regroup (4:00 PM).
*   **Mar 30, 2026:** GCP Key Removal activities begin.
*   **Apr 2, 2026:** DPD/Core Product/Picking Joint Meeting (9:30 AM SGT).
*   **Apr 24, 2026:** Deadline to RSVP for D&T Power Breakfast.
*   **Apr 25, 2026:** Agentic Evolution Contest Submission Deadline & FileVault Final Deadline.
*   **Apr 28, 2026:** D&T Power Breakfast (9:00 AM SGT).


## [15/54] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Last Activity: 2026-04-01T08:26:22.317000+00:00 | Last Updated: 2026-04-01T10:43:07.381552+00:00
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

**Recent Sequence Update:**
*   **Mar 31, 2026:** Incident `0404fba2...` triggered at 11:49 UTC and resolved at 15:05 UTC (~3h 16m). Status: **Resolved**.

*   **Apr 1, 2026 Sequence:**
    *   **Incident A (Story Key `c6d476e4...`):** Triggered 2026-04-01T23:27:22 UTC. Recovered 2026-04-01T02:53:22 UTC (~3h 26m). Status: **[P3] Recovered**.
    *   **Incident B (Story Key `f28ed3be...`):** Triggered 2026-04-01T01:53:22 UTC. Recovered 2026-04-01T05:06:22 UTC (~3h 13m). Status: **[P3] Recovered**.
    *   **Incident C (Story Key `ba9617bc...`):** Triggered **2026-04-01T07:07:22 UTC**. Recovered **2026-04-01T08:26:22 UTC** (~1h 19m). Status: **[P3] Recovered**.

*Note: All three incidents triggered on April 1st have self-resolved.*

### Pending Actions & Ownership
*   **Current Status:** All active incidents as of Apr 1, 2026 are **Resolved**.
    *   `c6d476e4...` (Recovered ~3h 26m).
    *   `f28ed3be...` (Recovered ~3h 13m).
    *   `ba9617bc-8391-54dd-84f4-5019d5d5efce` (Recovered ~1h 19m).
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Action Required:** None. All incidents resolved well within the 6-hour escalation threshold. Continue standard surveillance for new triggers.

### Decisions Made
*   **Escalation Status:** No escalation required; recent sequence of transient incidents (including the latest `ba9617bc` event) resolved automatically.
*   **Protocol:** Standard observation protocol remains effective.

### Key Dates & Follow-ups
*   **Latest Events:** April 1, 2026 (Three distinct incidents: ~23:27 UTC, ~01:53 UTC, and ~07:07 UTC triggers).
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Surveillance ongoing.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Datadog Monitor Link:** [View in Datadog](https://app.datadoghq.eu/monitors/17447511)
*   **New Incident Log:**
    *   Key `ba9617bc-8391-54dd-84f4-5019d5d5efce`: https://app.datadoghq.eu/monitors/17447511?group=story_key%3Aba9617bc-8391-54dd-84f4-5019d5d5efce

### Monitor Configuration
*   **Query:** `events("source:watchdog (story_category:infrastructure -story_type:(tcp_retrans_jump OR full_disk_forecast)) env:(PROD OR production OR prod)").rollup("count").by("story_key").last("30m") > 0`


## [16/54] FP x Mirakl
Source: gchat | Group: space/AAAAhWLveDE | Last Activity: 2026-04-01T07:58:04.751000+00:00 | Last Updated: 2026-04-01T10:43:28.272049+00:00
**Daily Work Briefing: FP x Mirakl Integration Update**

**Key Participants & Roles**
*   **Dang Hung Cuong:** Initiated initial API rate limiting discussion (March 17).
*   **Jill Ong:** Raised seller status query on March 25; tagged for visibility.
*   **Prajney Sribhashyam:** Proposed a three-way call (FP, Intrepid, Mirakl) on April 1 to align roadmap and clarify needs.
*   **Cheryl Jones:** Confirmed availability via leave confirmation until April 13; identified root cause of rate limiting as architectural misalignment by Intrepid.
*   **LyLy Lim:** Previously assigned for feasibility review.
*   **Michelle Lim & Sneha Parab:** Tagged by Prajney Sribhashyam for the proposed call.

**Main Topic**
The thread addresses two technical inquiries:
1.  **API Rate Limiting (Resolved Context):** Intrepid requested increasing the limit from one check per minute to support multi-seller operations. Investigation revealed that rate limiting was caused by incorrect endpoint usage not aligned with Mirakl documentation, rather than a need for higher thresholds. The team now requests an endpoint usage summary and the issued seller guide from Intrepid for further architectural review.
2.  **Seller Status Configuration:** Jill Ong queried (March 25) on creating additional statuses in Mirakl; still requires investigation.

**Pending Actions & Ownership**
*   **Action A:** Obtain endpoint usage summary and the issued seller guide from Intrepid to facilitate an architecture review under Mirakl Partnership support scope.
    *   **Owner:** Prajney Sribhashyam (to assist with request); Cheryl Jones (for final feedback).
    *   **Note:** Cheryl Jones is on leave until April 13; immediate follow-up required before her return.
*   **Action B:** Coordinate a three-way call involving FP, Intrepid, and Mirakl to discuss findings and roadmap alignment.
    *   **Owner:** Prajney Sribhashyam (proposer); all tagged participants (@Cheryl Jones, @Jill Ong, @Michelle Lim, @Sneha Parab, @Dang Hung Cuong).
*   **Action C:** Investigate technical feasibility of creating additional seller statuses in Mirakl.
    *   **Owner:** Cheryl Jones, LyLy Lim (pending return from leave).

**Decisions Made**
*   **Rate Limit Strategy Shift:** The approach has shifted from evaluating a threshold increase to correcting Intrepid's endpoint usage. No immediate rate limit increase is proposed until the architectural review confirms proper usage.
*   **Collaboration Model:** Agreed in principle on a three-way call (FP, Intrepid, Mirakl) to ensure FP visibility and better understand seller needs for the roadmap.

**Key Dates & Follow-ups**
*   **Original Inquiry:** March 17, 2026 – API Rate Limit discussion initiated by Dang Hung Cuong.
*   **Status Update (Root Cause):** April 1, 2026 (08:16 AM) – Cheryl Jones clarified that usage was incorrect per endpoint docs; Intrepid acknowledged design misalignment.
*   **New Proposal:** April 1, 2026 (07:48 AM) – Prajney Sribhashyam proposed the three-way call for visibility and roadmap alignment.
*   **Next Steps:** 
    *   Secure seller guide/usage data from Intrepid immediately.
    *   Schedule three-way call pending Cheryl Jones' return or delegation.
    *   Resume investigation on Seller Status configuration upon team availability.

**Specific References**
*   **Integrator:** Intrepid.
*   **Current Limit:** Once per minute (caused by incorrect usage, not hard cap).
*   **New Query Topic:** Creation of additional seller status in Mirakl.
*   **Platform:** Mirakl API.
*   **Source URL:** https://chat.google.com/space/AAAAhWLveDE


## [17/54] SRE / Network / DBA / DevOps / Infra
Source: gchat | Group: space/AAAAYX-ew1s | Last Activity: 2026-04-01T07:36:27.961000+00:00 | Last Updated: 2026-04-01T10:44:15.878542+00:00
**Daily Work Briefing: SRE / Infrastructure Team**

**Key Participants & Roles**
*   **Natalya Kosenko:** Submitted PR #12 (`infra-gcp-gen-ai-spark`) for service account rotation compliance; tagged @Himal Hewagamage, @Mohit Niranwal, and @Isuru Dilhan.
*   **Apurva Shingne:** Previously submitted Datadog PR #142 (GCD-8995); pending review by @Sneha Parab and @Nicholas Tan.
*   **Boning He:** Requested pricing workspace access via PR #722; pending review.
*   **Amit Giri:** Submitted new Datadog permission change PR #152 (`fp-datadog-eu`) on 2026-04-01.
*   **Tayza Htoon:** Requested approval for Terraform workspace access PR #725 (`tfe-workspaces`) for the Engage core product/pricing teams; tagged @Himal Hewagamage and @Tiong Siong Tee.
*   **Zheng Ming, Wai Ching Chan, Calvin Phan:** Reported connectivity/network issues (GCD-8941, GCD-8954, DSD-11066).
*   **Himal Hewagamage & Isuru Dilhan:** Primary reviewers/approvers for Gen-AI, Datadog, and Terraform requests.

**Main Topics**
1.  **Gen-AI Compliance:** Natalya Kosenko submitted PR #12 on 2026-03-31 to remove an unused, unrotated service account key from `infra-gcp-gen-ai-spark`.
2.  **Datadog Infrastructure:** Ongoing review of `fp-datadog-eu` PRs (#135–#152). Apurva Shingne's PR #142 (GCD-8995) remains pending. On 2026-04-01, Amit Giri submitted PR #152 for permission changes, requiring review by @Kyle Nguyen, @Himal Hewagamage, @Isuru Dilhan, and @Mohit Niranwal.
3.  **Terraform & Workspaces:** Natalya's Terraform PR #719, Boning He's PR #722 (pricing access), and Tayza Htoon's new PR #725 (Engage terraform workspaces) remain pending review. A failed Terraform plan (`run-CZVLtajJGbLVojLM`) and ticket GCD-8900 are active.
4.  **CI/CD Pipeline Failures:** Soni-BE golden pipeline clone failures persist; `lt-strudel-api-go` Go versioning conflicts (Go 1.25.8 vs `golangci-lint`) require resolution.
5.  **Cloud Networking:** AI agents in `us-central1` face internet connectivity issues (Ticket GCD-8941). Mohit Niranwal mandated non-prod testing prior to rollout.
6.  **Bastion Connectivity:** Wai Ching Chan's ticket GCD-8954 remains under investigation.
7.  **Database Subnet Request:** Calvin Phan requested CloudSQL subnets for SOT-SONI (Ticket DSD-11066); DBA coordination with @Himal Hewagamage is active.

**Pending Actions & Ownership**
*   **Review Datadog PR #152:** Owned by Amit Giri; requires immediate review by @Kyle Nguyen, @Himal Hewagamage, @Isuru Dilhan, and @Mohit Niranwal.
*   **Approve Terraform Workspace PRs:**
    *   **PR #725:** Owned by Tayza Htoon; requires approval from @Himal Hewagamage and @Tiong Siong Tee.
    *   **PR #12 (Gen-AI):** Owned by Natalya Kosenko; tagged for review by @Himal, @Mohit, and @Isuru.
    *   **PR #719 & #722:** Pending review by @Isuru Dilhan and @Himal Hewagamage.
*   **Review Datadog PR #142:** Owned by Apurva Shingne; tagged for review by @Sneha Parab, @Nicholas Tan.
*   **Troubleshoot Pipeline Issues:** Investigate Soni-BE SSH keys (Kalana) and `lt-strudel-api-go` config conflicts (Lester).
*   **Network & DBA Tickets:** Execute non-prod testing for Cloud NAT (GCD-8941); investigate Bastion issues (GCD-8954); review SOT-SONI subnet requirements (DSD-11066).

**Decisions Made**
*   **IaC Requirement:** Mandatory adoption of IaC for Datadog pipelines.
*   **Change Management:** Mohit Niranwal mandated non-prod testing for Cloud NAT changes before production deployment (GCD-8941).
*   **Compliance Action:** Removal of unused, unrotated service account keys is confirmed via PR #12 to address compliance gaps.

**Key Dates & Follow-ups**
*   **2026-03-31 (08:22 UTC):** Natalya Kosenko submitted PR #12 for service account key removal.
*   **2026-04-01 (06:58 UTC):** Amit Giri requested review and merge of Datadog PR #152.
*   **2026-04-01 (07:36–07:38 AM):** Tayza Htoon requested approval for Terraform PR #725; @Himal Hewagamage responded promptly.


## [18/54] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/8-Q3gLE8QP8 | Last Activity: 2026-04-01T06:56:39.283000+00:00 | Last Updated: 2026-04-01T10:44:38.054216+00:00
**Daily Briefing Update: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Lead/Coordinator.
*   **Andin Eswarlal Rajesh:** App Adoption Data.
*   **Onkar Bamane:** SKU/Data Operations.
*   **Gautam Singh:** Technical/Database Verification.
*   **Sneha Parab:** Data Enrichment & Stakeholder Management.
*   **Daryl Ng:** App Adoption.

**Main Topic**
Discussion continued on the BCRS POS cutover, focusing on SKU creation validation, barcode generation, and DBP system linkages. A specific discrepancy regarding product linkage missing for two SKUs was identified and resolved.

**Pending Actions & Owners**
*   **Onkar Bamane:** Investigate why 10 specific SKUs (13280794, 13280852, 13280864, 13281403, 13281448, 13281453, 13281688, 13281689, 13281710, 13281712) are not created in the DBP system. Confirm if data can be sent to FPON for the 361 SKUs with barcodes.
*   **Sneha Parab:** Raise a DBA Service Request (SR) for data enrichment on affected SKUs, obtain access to "BCRS - POS Cutover Plan.xlsx," and inform Jonathan Ho & Cheryl Ho upon completion.
*   **Gautam Singh:** Complete verification of product linkage tables and confirm unique SKU counts in DBP vs. the source sheet. Note: Two SKUs (13280733, 13280736) were flagged for missing linkage but clarified as external to FPON scope.
*   **Andin Eswarlal Rajesh / Daryl Ng:** Update app adoption numbers on the dashboard once the current lag resolves (data currently reflects March 28).

**Decisions Made**
*   **Enrichment Strategy:** Proceed with raising a DBA SR for data enrichment before notifying stakeholders.
*   **Technical Clarification:** SKUs **13280733** and **13280736** are confirmed as not listed to FPON; therefore, they should not exist in the internal database. Gautam Singh has acknowledged this update.

**Key Data Points & Dates**
*   **Data Status (as of March 28):** Android adoption 75.6%; iOS adoption 86.38%.
*   **SKU Discrepancy:** Out of 837 newly created SKUs, barcodes exist for only 361. In the DBP system:
    *   Unique SKUs listed: 361.
    *   Present in system: 351.
    *   Active deposit linkages: 349.
*   **Missing Linkage (Resolved):** Two SKUs (13280733, 13280736) were initially flagged by Gautam Singh as missing product linkage. Onkar Bamane clarified these are not intended for FPON/DBP, and the issue was closed with "Noted" from Gautam.
*   **Timeline Context:** Download scheduled for April 1, 2026. Discussion occurred between 23:16 UTC March 31 and 06:56 UTC April 1, 2026.

**Historical Context**
Previous actions regarding the 10 missing SKUs (starting with 13280794) remain active pending investigation. The adoption timeline remains ~2 months to reach >95%, slowing significantly after 85%.


## [19/54] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4 | Last Activity: 2026-04-01T06:44:36.338000+00:00 | Last Updated: 2026-04-01T10:45:26.714045+00:00
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

On **April 1**, Daryl Ng highlighted an epic for Phase 2 of "1HD to scale to more stores" (link: `DPD-627`), noting a recall that this initiative had not yet been aligned with Dennis. This generated five replies, with the last interaction occurring at 2:15 AM UTC. Later that morning (06:29 AM UTC), Daryl Ng queried whether Tiong Siong Tee should be included in related calls.

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
    *   **Ownership:** Alvin Choo. **(Updated Context):** Alignment with Dennis regarding Phase 2 scaling (Epic DPD-627) remains a critical dependency raised on April 1.
*   **Action:** Address technical clarifications raised by Tiong Siong Tee regarding Inventory visibility, Corporate Control alignment, and Product management portal structure (FP vs. Sellers).
    *   **Ownership:** Alvin Choo and Gopalakrishna Dhulipati. **(Update):** Daryl Ng queried on April 1 if Tiong Siong should be included in these discussion calls. **New Status:** On April 1 at 06:44 AM UTC, Alvin Choo confirmed permission to invite him ("Yes, can invite him?"), generating 4 replies with the last reply occurring 20 minutes ago.
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
*   **Phase 2 Scaling Epic (DPD-627):** April 1, 2026 (~01:46 AM UTC) – Daryl Ng flagged alignment status with Dennis; 5 replies generated.
*   **Call Participant Query & Invitation:** April 1, 2026 (06:29 AM UTC query; 06:44 AM UTC confirmation "Yes, can invite him?"); Tiong Siong Tee is now included in calls based on Alvin's approval at 06:44 AM UTC.


## [20/54] Offer Service Monitors Improvement - Apr 1
Source: gchat | Group: space/AAQA-iRTwV0 | Last Activity: 2026-04-01T06:19:07.381000+00:00 | Last Updated: 2026-04-01T06:42:02.613580+00:00
**Daily Work Briefing: Offer Service Monitors Improvement**

**Key Participants & Roles**
*   **Zaw Myo Htet:** Initiator; requested payment team attendance.
*   **Tayza Htoon:** Tagged participant (Payment Team).
*   **Dany Jacob:** Participant; owner of monitoring/log updates.
*   **Tiong Siong Tee:** Participant; reviewed content availability.

**Main Topic**
A brief coordination meeting regarding the "Offer Service Monitors Improvement" initiative, specifically focusing on payment service visibility and gap analysis.

**Decisions Made**
No formal decisions were recorded in this thread. The session was primarily a check-in where participants managed their immediate schedules.

**Pending Actions & Ownership**
*   **Action:** Investigate data gaps, implement additional logging, and update monitoring configurations for services.
    *   **Owner:** Dany Jacob.
    *   **Context:** Stated during departure from the call to address missing visibility ("check the gaps").

**Key Dates, Deadlines & Follow-ups**
*   **Date:** April 1, 2026.
*   **Timeframe:** 06:05 AM – 06:19 PM UTC.
*   **Status:** The meeting concluded with participants dropping off for other commitments. No specific deadline was set in the chat logs; however, Dany Jacob's action is ongoing pending the next update.

**Conversation Summary**
At 06:05 UTC, Zaw Myo Htet initiated the session seeking payment team members (specifically tagging Tayza Htoon and Dany Jacob). Tiong Siong Tee immediately asked for a chart to support the discussion. By 06:09 UTC, Tiong Siong Tee departed for another call without receiving the requested visual data. Finally, at 06:19 UTC, Dany Jacob confirmed dropping off for a conflicting commitment but committed to addressing the monitoring gaps by adding logs to their services and updating the monitoring systems.


## [21/54] [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Last Activity: 2026-04-01T06:14:07.638000+00:00 | Last Updated: 2026-04-01T06:42:57.187190+00:00
**Daily Work Briefing: [Prod Support] Marketplace**

**Key Participants & Roles**
*   **Support/Operations:** Willie Tan, Iris Chang, Lalita Phichagonakasit, Charlene Tan, Jie Yi Tan, Ayton See, Amos Lam, Michelle Lim.
*   **Technical/Admin Team:** Dang Hung Cuong, Shiva Kumar Yalagunda Bas, Olivia -, Jill Ong, Greta Lee, Zaw Myo Htet, Angella Yeo, Cassandra Thoi, Gopalakrishna Dhulipati, Ee Ling Tan.
*   **New Reporter:** Muhammad Sufi Hakim Bin Safarudin.

**Main Topics & Discussion Summary**
Discussions continue to focus on operational blockers regarding seller onboarding, order fulfillment discrepancies, system configuration errors, and data visibility gaps. New reports from April 1 highlight critical platform performance issues (lag), DBP barcode conflicts, and delivery window synchronization failures. Major themes include:

1.  **Transporter App Performance (New):** Anwar Nur Amalina reported (Apr 1, 03:17 UTC) that the Transporter Inform app is experiencing severe lag and failing to load jobs.
2.  **DBP Barcode Duplicate/NotFound Error (New):** Charlene Tan flagged (Apr 1, 06:07 UTC) a barcode unable to be found in DBP despite appearing as a duplicate entry. Dang Hung Cuong was tagged for investigation.
3.  **Delivery Window Synchronization (New):** Jie Yi Tan reported (Apr 1, 06:14 UTC) that the delivery window configuration is failing again for seller "Funa Artistic Hampers & Gifts." Despite updating to a 5-day window, the system displays 3 days. Dang Hung Cuong was tagged.
4.  **Seller Account Sync Failure:** Michelle Lim reported (Mar 31, 07:48 UTC) that two new seller accounts failed to sync to DBP despite having allocated internal codes and no error messages.
    *   Operator Internal Codes: 32208, 32207.
5.  **Email Distribution Logic:** Iris Chang requested confirmation regarding Sales Breakdown Report delivery for DF vendors. The goal is to ensure `db-online-marketplace@ntucenterprise.sg` is automatically CC'd regardless of the "Report Emails" field status in Mirakl.
6.  **SKU Publishing Failure:** Charlene Tan flagged (Mar 31, ~09:09 UTC) that SKU 90248069 was published with an offer but remains offline on the website.

**Pending Actions & Ownership**
*   **Transporter App Investigation (Urgent):** Technical team to investigate lag and job loading failures reported by Anwar Nur Amalina (Apr 1).
*   **DBP Barcode Discrepancy:** Dang Hung Cuong to investigate why a specific barcode cannot be found in DBP while showing as a duplicate (Charlene Tan, Apr 1).
*   **Delivery Window Fix:** Dang Hung Cuong to resolve the delivery window sync issue for "Funa Artistic Hampers & Gifts" (Jie Yi Tan, Apr 1).
*   **Seller Sync Investigation:** Tech team to investigate why DBP accounts 32208 and 32207 failed to sync despite valid internal codes (Michelle Lim, Mar 31).
*   **Report Email Logic:** Confirm and implement automatic CC of `db-online-marketplace@ntucenterprise.sg` for all DF vendor Sales Breakdown Reports (Iris Chang, Mar 31; cc: Amos Lam, Michelle Lim, Jill Ong).
*   **SKU Live Status:** Investigate why SKU 90248069 is not live on the website despite being published with an offer (Charlene Tan, Mar 31).
*   **Picklist Investigation:** Tech team to investigate failures for Order #258155683 and Postponed Order #256653797.

**Decisions Made**
*   Dang Hung Cuong is prioritizing the removal of Item ID: 90244361, new picklist failures, Woah Group offers errors, Pureen barcode truncation, DBP sync issues, **Transporter app lag**, and **delivery window failures**.
*   Dang Hung Cuong and Shiva Kumar Yalagunda Bas are assigned to investigate vendor picklist anomalies.
*   **Completed:** Access linkage for Seller ID 31435 was successfully executed by Shiva Kumar Yalagunda Bas on Mar 27, 11:29 UTC.

**Key Dates & Deadlines**
*   **2026-04-01:** Anwar Nur Amalina reported Transporter app lag; Charlene Tan flagged DBP barcode conflicts; Jie Yi Tan reported delivery window sync failure for "Funa Artistic Hampers & Gifts."
*   **2026-03-31:** Michelle Lim reported DBP sync failure for codes 32208 and 32207. Iris Chang raised Sales Breakdown Report email logic query. Charlene Tan reported SKU 90248069 not live.
*   **2026-03-30:** Muhammad Sufi Hakim Bin Safarudin reported picklist generation failures for Order #258155683 and Postponed Order #256653797.


## [22/54] RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU | Last Activity: 2026-04-01T04:38:03.171000+00:00 | Last Updated: 2026-04-01T06:45:51.125189+00:00
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


## [23/54] 📢 COM Notifications
Source: gchat | Group: space/AAAAu4WIubc | Last Activity: 2026-04-01T04:22:43.323000+00:00 | Last Updated: 2026-04-01T06:46:25.014649+00:00
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
    *   **April 1 (03:52–04:22 UTC)**: PR-2334 experienced volatility. Initial scans at 03:52 UTC (ver. `389f4e9`, 84.4% coverage) and 04:09 UTC (ver. `266d842`, 84.1% coverage) **FAILED**. Status recovered to **PASSED** by 04:22 UTC (ver. `97dd14a`) with 84.4% new code coverage.
    *   **March 31**: PR-2333 failed at 06:34 UTC but recovered to PASSED by 07:06 UTC.
*   **`fni-product-license-alert`**:
    *   **April 1 (03:51–04:01 UTC)**: PR-1479 scan recorded a **PASSED** status despite showing **0% Coverage on New Code**. Concurrently, the UAT branch (ver. `08158b5`) passed with 94.4% new code coverage at 04:01 UTC.
    *   **March 31**: PR-1478 passed with 94.4% new code coverage; subsequent UAT scans also achieved PASSED status.
*   **`supplier-job` (Shiva Kumar Yalagunda Bas)**: PRs #439/#440 scanned successfully on March 19 at 90.9% coverage; no new activity reported.

**Pending Actions & Ownership**
*   **System Error Investigation**: The "Webhook Bot is unable to process your request" error persists in every notification from March 5 through the latest scans on April 1 (including `seller-proxy-service` PR-2334 and `fni-product-license-alert` PR-1479). No specific owner assigned; requires immediate engineering attention.
*   **`fni-product-license-alert` Coverage Anomaly**: PR-1479 passed the Quality Gate with 0% new code coverage on April 1. This contradicts typical gate logic and requires investigation to determine if tolerance settings were bypassed or if data reporting is incorrect.
*   **`fpon-sap-jobs` Unit Tests**: Discrepancy between 72.7% coverage and 0% unit test success requires review by the respective team.

**Decisions Made**
*   **April 1 Action**: Quality Gate failures for `seller-proxy-service` PR-2334 resolved via automated retries within minutes of initial failures at 03:52 UTC. Pipelines successfully recovered the gate to **PASSED** status by 04:22 UTC despite lower coverage metrics (84.4%).
*   Recent merges in `supplier-job`, recovery scans for `seller-proxy-service` (PR-2333 and PR-2334), and UAT branches were accepted automatically following retries.

**Key Dates & Timeline**
*   **March 5**: Initial scan failures in `catalogue-job`.
*   **March 9**: UAT deployment for `fpon-sap-jobs`; initial failure for `seller-proxy-service` PR-2318.
*   **March 16 & 20**: Successful scans for `fni-product-license-alert` (PRs #1433, #1450) with 94.4% coverage.
*   **March 19**: `supplier-job` PRs #439/#440 scanned successfully at 90.9% coverage; `seller-proxy-service` PR-2306 showed multiple failure/recovery cycles.
*   **March 25**: `seller-proxy-service` PR-2330 and PR-2331 passed with stabilized coverage (97.8%–100%).
*   **March 31**: 
    *   **06:34 UTC**: `seller-proxy-service` PR-2333 failed (100.0% coverage); recovered to PASSED by 07:06 UTC.
    *   **07:43–09:26 UTC**: `fni-product-license-alert` PR-1478 and UAT branches passed (94.4% coverage).
*   **April 1**: 
    *   **03:51 UTC**: `fni-product-license-alert` PR-1479 PASSED with **0%** new code coverage.
    *   **03:52–04:22 UTC**: `seller-proxy-service` PR-2334 failed twice (84.4% and 84.1% coverage) before recovering to PASSED at 04:22 UTC (84.4% coverage).
    *   **04:01 UTC**: `fni-product-license-alert` UAT branch passed with 94.4% new code coverage.


## [24/54] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/aQBHf9eET0A | Last Activity: 2026-04-01T04:19:56.227000+00:00 | Last Updated: 2026-04-01T06:46:40.253846+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Daryl Ng:** Initiator of the inquiry; investigating Linkpoints eligibility and product categorization discrepancies.
*   **Sneha Parab:** Subject matter expert confirming technical scannability implications.
*   **Wei Sing:** Team member (via SAP) referenced regarding configuration enablement.

**Main Topic**
Investigation into "Linkpoints eligible" status for specific SKUs within the DBP system versus SAP, and subsequent categorization anomalies affecting product search/browse behavior.

**Pending Actions & Owners**
*   **Action:** Verify why certain items are categorized as "search as browse" despite being enabled in SAP.
    *   **Owner:** Daryl Ng (stated intent: "let me check with Wei Sing").
*   **Action:** Clarify impact of "search as browse" categorization on scanning functionality for S&G (Search & Go).
    *   **Status:** Resolved/Confirmed by Sneha; no further action required at this time.

**Decisions Made**
*   **Initial Check:** Most items were confirmed to be enabled after an initial review.
*   **Functional Impact:** It was determined that the "search as browse" categorization does not prevent SKU scanning for S&G operations (confirmed by Sneha Parab).
*   **SKU Status:** The specific SKU discussed remains scannable despite the categorization discrepancy.

**Key Dates, Deadlines & References**
*   **Date of Discussion:** April 1, 2026 (Between 03:13 and 04:19 UTC).
*   **Systems Referenced:** SAP, DBP, FairPrice Admin Catalogue.
*   **Specific Product Reference:** FairPrice Catalogue Edit URL provided for product ID `163074`.
    *   *URL:* `https://admin.fairprice.com.sg/catalogue/products/edit/163074`
*   **Follow-up:** Daryl Ng to follow up with Wei Sing regarding the categorization logic.

**Summary of Flow**
Daryl Ng initially queried Linkpoints eligibility, noting a discrepancy where SAP enabled the feature but DBP appeared disabled. Upon further review, most items were found enabled. However, one specific product (ID 163074) was flagged as categorized incorrectly ("search as browse"). Daryl questioned if this affected scanning; Sneha confirmed SKUs remain scannable. Daryl concluded the conversation with confirmation that no functional blockage occurs.


## [25/54] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Last Activity: 2026-04-01T04:14:56.730000+00:00 | Last Updated: 2026-04-01T06:47:14.266707+00:00
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
*   **Gopalakrishna Dhulipati & Dang Hung Cuong:** Address emoji validation.
*   **Alvin Choo:** Announced annual planning meeting for Apr 2, 9:30 AM.
*   **Yangyu Wang:** Tagged regarding split flag issues; reported iOS Instore page issue.

**Main Topics Discussed**
1.  **Unit Price Calculation Compliance (New):** On Mar 31, Lester highlighted a government compliance requirement for Phase 2 unit price calculations. Current reliance on parsing `display_units` is unscaleable.
    *   **Proposed Solution:** Ingest structured fields (`pack_size`, `pack_size_unit`, `pack_size_bundle`) from Mirakl/SAP into DBP for `website-service`.
    *   **Action:** Sneha Parab requested an initial effort assessment to map these fields.
2.  **iOS Instore Page Regression (New):** On Apr 1 at 04:14 UTC, Yangyu Wang reported a functional issue on the iOS instore page, noting Android is unaffected. Andin Eswarlal Rajesh has been tagged for investigation.
3.  **B2B SKU Sync Clarification:** On Mar 30, Sneha Parab requested clarity on B2B SKU synchronization to WMS. Akash Gupta responded by 9:20 AM.
4.  **UAT Stock Sourcing Update:** Sneha Parab requested specific SKUs (128373, 13205552, etc.) be marked as unlimited stock in UAT for bulk order testing. Wai Ching Chan is handling the update.
5.  **BCRS Deposit Logic Failure:** On Mar 30, Wai Ching Chan reported missing deposit values during UAT checkout. Sundy Yaputra has been flagged to investigate this regression.
6.  **Annual Planning Meeting (New):** Alvin Choo announced a meeting for tomorrow, Apr 2 at 9:30 AM, to share the finalised yearly plan and project priorities.
7.  **BCRS Epic Closure Urgency:** Sneha Parab continues to push for the closure of the BCRS epic (DPD-637 and DPD-807 remain in "Define" state). Inputs required from Akash Gupta, Michael Bui, and Andin Eswarlal Rajesh.
8.  **Slot Date Discrepancy:** Shiva Kumar Yalagunda Bas reported a delivery slot mismatch (UI shows 25th, API indicates 23rd). Daryl Ng and Sundy Yaputra are resolving this.
9.  **Omni Home Split Flag Regression:** On Mar 31 at 02:27 UTC, Daryl Ng reported that Omni home swimlanes fail to follow the split flag due to backend default setting updates.

**Pending Actions & Ownership**
*   **Sundy Yaputra:** Investigate missing BCRS deposit values in UAT checkout (Reported by Wai Ching Chan, Mar 30).
*   **Wai Ching Chan:** Update specified SKUs to "unlimited stock" in UAT.
*   **Akash Gupta, Michael Bui, Andin Eswarlal Rajesh:** Provide immediate inputs on BCRS tickets **DPD-637** and **DPD-807**.
*   **Lester Santiago Soriano / Sneha Parab:** Assess effort required to map `pack_size`, `pack_size_unit`, and `pack_size_bundle` from Mirakl/SAP to DBP.
*   **Andin Eswarlal Rajesh:** Investigate iOS instore page regression reported by Yangyu Wang (Apr 1).
*   **Daryl Ng:** Review Michael Bui's PR #7 (`bcrs-deposit-posting`). Investigate Omni home split flag issue with Nikhil and Yangyu Wang.
*   **Zaw Myo Htet:** Clarify pre-order payment redemption logic; execute UAT testing on offboarded Pinelabs split feature flag.

**Decisions Made**
*   **Unit Price Structure:** Move from parsing `display_units` to utilizing structured fields for Phase 2 compliance.
*   **BCRS Epic Priority:** Immediate action required to close the BCRS epic; ticket status must be verified for DPD-637 and DPD-807.
*   **UAT Stock Critical:** Specific SKUs identified by Sneha Parab must be set to unlimited stock immediately.
*   **iOS Issue:** Investigation initiated into iOS-specific instore page failure (Android unaffected).

**Key Dates & Deadlines**
*   **Mar 30, 2026:** B2B sync clarity requested; UAT stock updates required; BCRS deposit failure reported.
*   **Mar 31, 2026:** Unit price compliance discussion initiated; Omni home split flag regression reported. Sports Hub FFS store closure deadline active.
*   **Apr 2, 2026 (Tomorrow):** Annual planning meeting scheduled for 9:30 AM (Host: Alvin Choo).

**Note on Historical Context:** Previous mentions of code review priorities for `layout-service` PR #362 are superseded by the urgent Strudel SDK deployment update (`go-platform-website`). The current focus includes investigating the UAT BCRS deposit regression, updating UAT stock levels, resolving slot date mismatches, closing the BCRS epic via tickets DPD-637 and DPD-807, debugging the Omni home split flag configuration, assessing structured unit price field ingestion, and troubleshooting the new iOS instore page regression.


## [26/54] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Last Activity: 2026-04-01T03:28:39.672000+00:00 | Last Updated: 2026-04-01T06:47:47.381653+00:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
Production instability persists in Mirakl and DBP integrations. A significant incident cluster occurred on **April 1** between **03:20 UTC** and **03:28 UTC**, affecting `fni-order-create` with six P2 alerts regarding database fetching, API errors, and route exceptions. Concurrently, the `picklist-pregenerator` latency issue has recurred, now exceeding 3,600s on April 1. The March 31 cluster previously noted is superseded by this new April 1 event window.

**Incident Summary & Timeline**
*   **Service: `fni-order-create` (Cluster of Errors) – Early Morning (Apr 1)**
    *   **Trigger Window:** Alerts began at **03:20:46 UTC**:
        *   "Failure occurred during fetching orders from DBP" (`17447925`) triggered at **03:20:46 UTC**.
        *   "Error while calling APIs" (`17447928`) triggered at **03:20:51 UTC**.
        *   "Failure occurred during fetching orders" (`17447942`) triggered at **03:21:03 UTC**.
        *   "Exception Occurred At DBP Route" (`17447943`) triggered at **03:21:04 UTC**.
        *   "Exception Occurred At Mirakl Route" (`17447918`) triggered at **03:23:40 UTC**.
    *   **Recovery:** All monitors returned to normal between **03:25:46 UTC** and **03:28:39 UTC**. Total duration: ~8 minutes.

*   **Service: `picklist-pregenerator` (Latency Warning) – Late Night (Apr 1)**
    *   **Trigger:** P2 Warning "taking too long to complete" triggered at **23:01:22 UTC** on Mar 31/transitioning to Apr 1. Metric value: **3611.571s**. This follows previous triggers on Mar 29 (3609.523s) and Mar 30 (3608.92s).

*   **Historical Context:**
    *   **Mar 31 Afternoon:** Test monitor `29851723` triggered intermittently for Apple Pay transactions between 16:41 UTC and 17:12 UTC.
    *   **Mar 27 Evening:** P1 alert "SAP authentication failed" on `fpon-seller-sap-picklist-reporter` (recovered in 5 mins).

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of the April 1 cluster affecting `fni-order-create` (Monitors `17447925`, `17447928`, `17447942`, `17447943`, `17447918`). Focus on DBP fetching failures, API errors, and Mirakl route exceptions.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Address critical latency in `picklist-pregenerator`. Recurrence of >3,600s execution times (Mar 29, Mar 30, Apr 1) indicates continuous systemic failure.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Investigate intermittent triggers for Monitor `29851723` regarding Apple Pay transaction ratios (Mar 31).
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Summary for Leadership**
Instability in Mirakl and DBP integrations continues, marked by a new incident cluster on **April 1**. Between **03:20:46 UTC** and **03:28:39 UTC**, `fni-order-create` triggered six distinct P2 alerts, including "Failure occurred during fetching orders from DBP" (`Monitor ID 17447925`) and "Exception Occurred At Mirakl Route" (`Monitor ID 17447918`). All issues resolved within approximately 8 minutes. Additionally, the `picklist-pregenerator` service exhibits persistent critical latency, with execution times exceeding 3,600s logged on March 29, 30, and April 1 (value: 3611.571s). This pattern indicates systemic degradation requiring urgent engineering review by the `dpd-fulfilment` and `seller-experience` squads.


## [27/54] RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Last Activity: 2026-04-01T03:21:06.545000+00:00 | Last Updated: 2026-04-01T06:48:10.587929+00:00
**Daily Work Briefing: Automated Test Results Summary (RMN Notification)**

**Key Participants & Roles**
*   **Collection Runner App:** Automated testing agent executing API suites.
*   **Webhook Bot:** Reporting mechanism; consistently returning "unable to process your request" on all notifications through April 1, 2026.
*   **Parties Involved:** System-generated notification log only.

**Main Topic/Discussion**
Automated nightly API test executions across `promo-service`, `marketing-personalization-service`, and `marketing-service` in the **staging** environment. Monitoring period spans March 12 through **April 1, 2026**. Execution windows occur at approximately 01:05 UTC (morning), 02:30/02:31 UTC (midnight), and **03:20/03:21 UTC** (early morning).

**Test Execution Status & Anomalies**
*   **`marketing-service` Stability Confirmation:** The streak of resolution extends through April 1.
    *   **April 1, 01:05 UTC:** Executed successfully.
        *   **API Contract Tests:** 20 Passed / 0 Failed / 0 Skipped (Total Requests: 16).
        *   **API Tests:** 49 Passed / 0 Failed / 0 Skipped (Total Requests: 17).
    *   **Historical Context:** Recurring instability persisted from March 17 through early March 25. Temporary stabilization occurred on March 25; the morning failure streak broke on March 26. Stability confirmed for March 26–30, now extended to April 1.
*   **`promo-service`:** Confirmed stable on April 1 at **02:31 UTC**.
    *   **API Tests:** 10 Passed / 0 Failed (Total Requests: 3).
    *   **Contract Tests:** 6 Passed / 0 Failed (Total Requests: 3).
    *   Stability confirmed for March 26–April 1.
*   **`marketing-personalization-service`:** New data confirms a successful run at **03:21 UTC on April 1**.
    *   **API Contract Tests:** 125 Passed / 0 Failed (Total Requests: 21).
    *   **API Tests:** 96 Passed / 0 Failed (Total Requests: 21).
    *   This confirms stability for April 1, extending the successful streak from March 27–April 1.

**Pending Actions & Ownership**
*   **Webhook Bot Remediation (High Priority):** The bot failed to process requests in every notification cycle from March 12 through the latest log on **April 1 at 03:21 UTC**. Immediate attention is required from DevOps or Automation Infrastructure.
*   **Verify `marketing-service` Stability:** Engineering must continue monitoring subsequent runs to confirm the resolution of early-morning flakiness observed between March 17–25 was permanent.

**Decisions Made**
*   No human decisions recorded; all entries are automated system outputs.

**Key Dates & Deadlines**
*   **Failure Window (Historical):** Instability noted on March 12, 13, and persistently from **March 17 through March 25**.
*   **Current Status:** Successful runs observed on March 26–April 1 across all three services.
    *   `marketing-service`: Passed at 01:05 UTC (April 1). Previous stable window noted March 26–30.
    *   `promo-service`: Passed at 02:30/02:31 UTC (March 26–April 1).
    *   `marketing-personalization-service`: Passed at 03:20/03:21 UTC (March 27–April 1).
*   **Monitoring Period:** Data covers runs from **March 12, 2026**, through **April 1, 2026**.

**Resource Info**
*   **Message Count:** Updated to reflect notifications through April 1.
*   **URL:** https://chat.google.com/space/AAQA85dw4So


## [28/54] FPG Everyone - General
Source: gchat | Group: space/AAAAjDYVcBU | Last Activity: 2026-04-01T00:41:58.858000+00:00 | Last Updated: 2026-04-01T06:48:51.379665+00:00
**Daily Work Briefing: FPG Everyone Chat Summary (Updated)**
**Date Range:** March 3 – April 1, 2026
**Source:** Google Chat (FPG Everyone - General)

### Key Participants & Roles
*   **Serene Kua Puay Leng:** Promotes daily product deals and lobangs.
*   *(Previous participants retained: Siti Nabilah, Jasmine Neo, Keith Lee, Melissa Lim, Maisy Heeng, Si Min Ng)*

### Main Topics
1.  **Digital Access Rollout:** Completed as of Mar 30; user guide distributed.
2.  **Media Collaboration – "Bowl of Love":** Final episodes featuring Tyler Ten, Tasha Low, and Xiang Yun are live (Mar 21 launch). Focuses on warmth/healing with fresh Malaysian pork via @mediacorp.re.dian TikTok.
3.  **Industry Recognition:** Lau Pa Sat's "Spin for your Huat" featured by Campaign Asia as a top CNY 2026 campaign alongside Nike and Apple.
4.  **FairPrice Heartland Hits Launch (Mar 27):** Community storytelling contest (#FPHeartlandHits, #FPNorthie). Incentive: $50 E-Vouchers + song feature. Deadline: April 5, 2026.
5.  **Unity Wellness Promotions:** B1G1 offer on health/wessentials (Mar 26–29) at Unity stores. Featured brands include Moom Health and Elastine.
6.  **New Brand Launch – Shabu Days (FPG Food Services):** Launched April 3 at Hillion Mall with hotel-inspired dining.
7.  **Linkpoints Loyalty Promo ($0.99):** Redemption active for FairPrice Maple Syrup Cashews and Myojo Bowl Noodles. Collection deadline: April 5, 2026.
8.  **New Product Promo – Delicato Sausages:** Deal on Japanese-style sausages (Curry & Bonito Seaweed) at $3.95/packet until April 15, 2026.
9.  **New Promotional Launch – KitKat F1 Pack (Apr 1):** Darren Goh announced the "Ready, Set, Break!" campaign. Exclusive to FairPrice, Cheers, and FairPrice Online.
    *   **Price:** $29.95.
    *   **Contents:** 2 KitKat 10s Sharebags + 1 KitKat & F1 Flask.

### Pending Actions & Ownership
*   **Shorty Awards Voting (Owner: All Staff):** Vote daily for *Bridge to Equity* and *2025 End-Of-Year Unpacked*. Deadline: **April 8**.
*   **Linkpoints Redemption (Owner: All Staff):** Redeem $0.99 rewards. Collection deadline: **April 5, 2026**.
*   **Volunteer Engagement:** Sign up via `https://forms.gle/UkyQDagmDy4mcY7K7`. "Willing Hearts Kitchen Crew" is fully booked.
*   **Sensory Test Sign-ups:** Chapati screening form open (`https://forms.gle/DFYrahZcvhtcoJ9R7`). Frozen Snacks sign-up closed.
*   **Delicato Sausage Trial (Owner: All Staff):** Encouraged purchase during promo through April 15 for instant meal upgrade.

### Decisions Made
*   **Awards Campaign:** Mobilization approved for Shorty Awards voting.
*   **Wellness Extension:** Unity B1G1 offer extended (Mar 26–29).
*   **Loyalty Initiative:** $0.99 redemption launched with specific SKUs.
*   **Brand Expansion:** Shabu Days launch executed April 3.
*   **Product Promotion:** Delicato sausage promo activated through April 15.
*   **Promotional Campaign:** KitKat F1 Flask Pack activation approved for exclusive retail distribution starting April 1, 2026.

### Critical Dates & Deadlines
*   **April 1:** KitKat F1 Pack launch (FairPrice/Cheers).
*   **April 3:** Shabu Days launch (Hillion Mall).
*   **April 5:** Heartland Hits contest closes; Linkpoints redemption collection ends.
*   **April 8:** Shorty Awards voting deadline.
*   **April 15:** Delicato Japanese-style sausage promo expires.


## [29/54] Team Starship
Source: gchat | Group: space/AAQAX9iKYf0 | Last Activity: 2026-04-01T02:51:49.229000+00:00 | Last Updated: 2026-04-01T06:49:57.785137+00:00
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
    *   **Technical Clarification:** Danielle Lee queried implementation specifics, asking if the solution requires a backend configuration change only or further development. Awaiting Alvin Choo's technical assessment regarding scope and effort.

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
| **Clarify:** Cart-level coupon logic & Project Light inclusion | Alvin Choo / Ryan's team | Pending decision on backend config scope |
| **Clarify:** B2B Cybersource OTP flow applicability | Alvin Choo | As needed |
| **Submit:** Omni Roadmap deprioritization list | All PMs | **EOD Today (March 25)** |
| **Update:** OMNI-1282 status (De-prioritize) | Alvin Choo / Koklin Gan | Pending confirmation |
| **PAUSE:** OMNI-1345 requirements | All Stakeholders | Until business model finalized |
| **Prioritize:** Scan@Door AI Personalisation review | Danielle Lee, Daryl Ng, Tech Leads | Immediate |
| **Provide:** Performance Marketing alias contact | Alvin Choo / Andin Eswarlal Rajesh | Immediate |

**Key Dates & Follow-ups**

*   **Meeting Rescheduled:** Weekly Epics meeting postponed to **Wednesday, March 12 (tomorrow) at 11:00 AM**. Location: Level 12 Room 18 (or virtual/pantry).
*   **Reference Tickets:** SHOP-3779, OMNI-1099, DPD-100, **DPD-783**, OMNI-1345, OMNI-1282, OMNI-1421.


## [30/54] DPD x Platform Engineering
Source: gchat | Group: space/AAQAcjNXKpA | Last Activity: 2026-04-01T02:37:40.979000+00:00 | Last Updated: 2026-04-01T06:50:30.713729+00:00
**Daily Work Briefing: DPD x Platform Engineering**
*(Updated with April 1 SLO Alert Validation & Redis Investigation)*

**Key Participants & Roles**
*   **Kyle Nguyen:** Infrastructure/Platform Engineering (Reviewer, Incident Triage, Redis Alert Lead).
*   **Daryl Ng:** Incident Analyst / Automation query responder.
*   **Gopalakrishna Dhulipati:** Addressed in new alert chain.
*   **Sneha Parab:** Addressed in new alert chain.
*   **Alvin Choo:** Team Lead; CC'd on high-urgency Redis alert.
*   **Sampada Shukla:** Reported SLO error budget alerts on March 31; involved in April 1 validation.
*   **Dodla Gopi Krishna:** Owner of Fulfillment/Pricing SLOs; reported new Get serviceable area journey issue on April 1.
*   **Wai Ching Chan & Akash Gupta:** Engaged in April 1 SLO monitoring discussion.

**Main Topics & Discussions**
1.  **Get Serviceable Area Journey Alert (April 1):** Dodla Gopi Krishna initiated a query at ~02:37 UTC on April 1 regarding the "Get serviceable area" journey. Citing an SLO V2 alert around 02:55 PM local time (approx. 06:55 AM UTC), they requested validation of the alerting logic via Datadoghq link.
    *   *Status:* Thread is active with 8 replies and 8 unread messages as of 05:16 AM April 1. Participants include Sampada Shukla, Wai Ching Chan, and Akash Gupta to verify alert accuracy.

2.  **High-Urgency Redis CPU Spike (March 30):** Kyle Nguyen reported a critical alert at ~03:00 AM UTC regarding the Redis instance `zs-fpon-prd-catalogue-service` in `asia-southeast1`. The instance hit nearly 100% CPU usage.
    *   *Investigation Status:* Verified latency spikes originating from `go-catalogue-service`. Latency has normalized, preventing escalation to a formal incident.
    *   *Action:* Kyle requested priority RCA for the March 30 event.

3.  **SLO Error Budget Alerts (March 31):** Sampada Shukla reported SLO error budget alerts on March 31 at ~03:55 AM UTC referencing two monitors in Datadoghq EU.
    *   *Status:* Alert acknowledged by Dodla Gopi Krishna; thread remains active with ongoing degradation in Fulfillment and Pricing tribes requiring attention due to error budget consumption.

4.  **Historical Context (Retained):**
    *   *Critical Picking App & Backoffice Incident (March 23):* `SocketTimeoutExceptions` caused by GKE cluster (`jarvis-prod-ap-v2`) hard memory limits triggering forced pod evictions. Root cause identified as memory exhaustion between 15:22–15:39 SGT.
    *   *SLO Performance Degradation (March 25):* Initial error budget depletion in Fulfillment and Pricing tribes reported by Dodla Gopi Krishna.

**Pending Actions & Owners**
*   **Validate Get Serviceable Area Alert:** Verify if the SLO V2 alert on April 1 was accurate or a false positive. *(Owners: Sampada Shukla, Wai Ching Chan, Akash Gupta)*
*   **Investigate Redis CPU Saturation:** Prioritize RCA for `zs-fpon-prd-catalogue-service` hitting 100% CPU on March 30. *(Owners: Daryl Ng, Gopalakrishna Dhulipati, Sneha Parab)*
*   **Address SLO Error Budget Alerts:** Resolve current alert status and prevent further budget depletion for the two affected SLOs reported by Sampada Shukla. *(Owner: Dodla Gopi Krishna, relevant service owners)*
*   **Resolve Cluster Capacity Scaling:** Investigate why the cluster failed to scale out during peak traffic (March 23) and implement fixes for memory limits. *(Owners: Kyle Nguyen, Nicholas Tan)*
*   **Evaluate On-Call Tooling Strategy:** Assess Akash Gupta's proposal to use Datadog UI instead of Terraform for new on-call teams. *(Owner: Platform Engineering)*
*   **Restore Bastion Access:** Investigate PROD `asia-southeast1-c` Bastion inaccessibility. *(Owners: Nicholas Tan, Kyle Nguyen, Harry Akbar Ali Munir)*
*   **Review Infrastructure PRs:** Natalya Kosenko's PR `infra-gcp-fpg-titan/344` and Akash Gupta's PR #917 require reviews.

**Decisions Made**
*   *Tentative:* Debate continues on retaining Terraform-based change-freeze vs. direct Datadog UI management for on-call teams.
*   **QC Food Status:** Disabling confirmed on production (as of March 19). Resource scale-down planning initiated pending ES confirmation.

**Key Dates & Follow-ups**
*   **April 1, ~02:37 AM UTC:** Dodla Gopi Krishna queried validation for Get serviceable area journey SLO V2 alert.
*   **April 1, 05:16 AM:** Last reply recorded in the SLO validation thread (8 unread messages).
*   **March 31, ~03:55 AM UTC:** Sampada Shukla reported SLO error budget alerts; Dodla Gopi Krishna acknowledged.
*   **March 30, ~03:00 AM UTC:** High-urgency Redis CPU alert triggered.
*   **March 23, 03:40–03:45 PM SGT:** Critical incident involving GKE memory exhaustion.


## [31/54] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/z_vFHR6ne-M | Last Activity: 2026-04-01T02:35:03.800000+00:00 | Last Updated: 2026-04-01T06:50:41.901609+00:00
**Daily Work Briefing: Digital Product Development Team**

**Key Participants & Roles**
*   **Alvin Choo:** Initiator; Owner of the meeting agenda regarding the annual plan.
*   **Daryl Ng:** Coordinator; Managing attendance and leave notifications.
*   **Yangyu Wang:** Attendee (Remote); Confirmed dial-in status while on leave.
*   **Chee Hoe:** Attendee (Remote); Attending via dial-in while on leave.
*   **Andin Eswarlal Rajesh:** Coordinator; Confirming remote attendance for a colleague on leave.
*   **Vibin:** Attendee (Remote); Dialing in while on leave.

**Main Topic/Discussion**
The team is discussing the logistics and attendance for an upcoming meeting to review the finalized digital product direction for the year. Specific focus includes sharing the overall plan, identifying "project light" initiatives, and covering other strategic areas. Alvin Choo also confirmed securing a conference room ("Heritage Room") for the session.

**Decisions Made**
*   **Meeting Confirmation:** A meeting is scheduled for tomorrow at 9:30 AM to present the finalized annual direction.
*   **Attendance Protocol:** Team members currently on leave (Yangyu Wang, Chee Hoe, and Vibin) will join remotely via dial-in rather than attending in person.

**Pending Actions & Ownership**
*   **Attendees Dialing In:** Yangyu Wang, Chee Hoe, and Vibin must ensure remote connectivity for the 9:30 AM session. (Confirmed by Daryl Ng and Andin Eswarlal Rajesh).
*   **Agenda Presentation:** Alvin Choo to deliver the overview of the overall plan, project light scope, and other areas.

**Key Dates & Follow-ups**
*   **Meeting Date/Time:** Tomorrow, April 2, 2026, at 9:30 AM (Local time inferred from chat context).
*   **Venue:** Heritage Room.
*   **Context Note:** All communications occurred on April 1, 2026.


## [32/54] DPD x DPM
Source: gchat | Group: space/AAQApzD7Im0 | Last Activity: 2026-04-01T02:33:57.348000+00:00 | Last Updated: 2026-04-01T06:51:10.348852+00:00
### Daily Work Briefing: DPD x DPM Collaboration Space (Updated)

**Key Participants & Roles**
*   **Daryl Ng:** Tech Lead; flagged CHAS calculation issues (`DPD-530`). Tagged regarding Gamification ownership, delivery logic, and urgent ticket status updates for the OMNI review.
*   **Rajesh Dobariya:** Inquired about Gamification data and "Normal" vs. "Express" display logic. Initiated "1HD Business testing." Recently flagged a discrepancy where tickets are ready for UAT (per Zaw) but show 0% completion status. Urged Daryl Ng to update ticket statuses by the afternoon OMNI review, noting Andin is on leave.
*   **Andin Eswarlal Rajesh:** Previously initiated "1HD Business testing" (March 25). Currently on leave as of March 27; however, posted new updates regarding "Dynamic Whitelisting UAT" on March 30.
*   **Vivian Lim Yu Qian:** Driving mandates (MTI price per piece) and SWA migration history.
*   **Zaw:** Credited with confirming tickets are ready for UAT.
*   **Eva Yeo:** Requested access to the space on April 1, 2026; request was denied by Google Chat system processing error or manual intervention.

**Main Topics**
1.  **Dynamic Whitelisting UAT:** Andin Eswarlal Rajesh initiated a new discussion on "Dynamic Whitelisting UAT" on March 30, replacing the earlier focus solely on 1HD testing.
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
*   Access control: Eva Yeo was denied entry to the collaboration space on April 1, 2026.

**Key Dates & Deadlines**
*   **April 1, 2026, ~02:33 AM:** Eva Yeo requests to join the space; request processing failed or was denied.
*   **March 30, ~03:05 AM:** Andin Eswarlal Rajesh posts regarding "Dynamic Whitelisting UAT" with 2 replies; last reply noted at 3:45 AM.
*   **March 27, ~03:02 AM:** Rajesh Dobariya tags Daryl Ng to update statuses by the afternoon OMNI review, noting Andin is on leave.
*   **March 27, ~02:50 AM:** Rajesh notes tickets are ready for UAT (per Zaw) but show 0% done; flags need for status update.
*   **March 25, 06:59 AM:** Andin initiates "1HD Business testing" discussion.

**Reference Links**
*   Price Per Piece Wiki: `https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008175965/Price+Per+Piece+Multipack+in+Display+Unit`
*   CHAS Ticket: `DPD-530`
*   Sticky Header UI Ticket: `ENGM-2501`
*   SWA Migration Ticket: `DIS-585`


## [33/54] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/dRUQRmgzGzc | Last Activity: 2026-04-01T02:15:27.509000+00:00 | Last Updated: 2026-04-01T06:51:21.941641+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Daryl Ng:** Initiator; tracking project alignment and estimates for Phase 2 scaling.
*   **Alvin Choo:** Decision-maker; prioritizing the current epic for leadership review.
*   **Akash Gupta:** Technical lead/Coordinator; liaising with subject matter experts for estimations.

**Main Topic**
Discussion regarding **Phase 2 of Project "1HD"** (scaling to more stores), specifically focusing on:
1.  Alignment status of the Phase 2 epic (DPD-627) with stakeholder Dennis.
2.  Prioritization and scheduling of this work for leadership review.
3.  Estimation requirements for a related issue (DPD-629).

**Pending Actions & Ownership**
*   **Owner:** Akash Gupta
    *   **Action:** Discuss the estimation for ticket **DPD-629** with Sampada upon her return and provide the final estimate to Daryl Ng.
    *   **Reasoning:** Subject Matter Expert (PIC) Sampada is currently on leave; estimates cannot be finalized without her input.

**Decisions Made**
*   **Prioritization:** Alvin Choo confirmed that the Phase 2 epic (**DPD-627**) requires immediate prioritization and must be presented to the leadership table ("bring up the table").
*   **Alignment Status:** The previous recollection regarding alignment with Dennis is acknowledged as "no"; this will be addressed through the new prioritization.

**Key Dates, Deadlines & References**
*   **Date of Conversation:** April 1, 2026.
*   **Ticket Reference (Phase 2 Epic):** `DPD-627` (Scaling to more stores).
*   **Ticket Reference (Estimation Request):** `DPD-629`.
*   **Deadline for Estimate:** Tomorrow (April 2, 2026), as communicated by Akash Gupta.
*   **Constraint:** Sampada is unavailable today (April 1) to provide input on **DPD-629**.


## [34/54] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/69o051rSqd4 | Last Activity: 2026-04-01T00:59:59.910000+00:00 | Last Updated: 2026-04-01T06:51:38.489660+00:00
**Daily Work Briefing: Digital Product Development (Leads Ecom/Omni)**

**Key Participants & Roles**
*   **Daryl Ng:** Initiator; previously tracking deployment status, later confirmed flag enablement.
*   **Sneha Parab:** Technical lead/owner; confirmed completion of MP production deployment.
*   **Shiva:** Tester; concluded validation late yesterday evening (March 30).
*   **Alvin Choo:** Team member; coordinated BCRS focus and verified final status; initiated query regarding PM agreement.

**Main Topic**
Discussion centered on the finalization of the BCRS deliverable, MP production deployment confirmation, and subsequent resolution of feature flag configuration timing in alignment with Product Management (PM).

**Pending Actions & Ownership**
*   **Deploy Feature (MP):** **COMPLETED.** Sneha Parab deployed pending changes for MP to production as of 10:51 AM on March 31.
    *   **Owner:** Sneha Parab.
*   **BCRS Deliverable:** **CONFIRMED COMPLETE.** Alvin Choo verified the status at 10:49 AM, confirming "all okay," and subsequently celebrated the completion with the team.
*   **Feature Flags Configuration:** **COMPLETED.** Daryl Ng enabled the flags on April 1, 2026, following a query from Alvin Choo regarding the PM agreement.
    *   **Owner:** Daryl Ng.
    *   **Alignment:** Prajney (PM).

**Decisions Made**
*   **Deployment Timing:** The deployment of MP changes to production was executed on March 31, 2026, following Shiva's successful testing (concluded March 30 evening).
*   **Daily Focus Priority:** The team successfully prioritized and completed all BCRS tasks by the end of the day.
*   **Flag Configuration Resolution:** The issue regarding flag scheduling was resolved on April 1, 2026. Daryl Ng confirmed enabling the flags at 00:59 AM, explicitly aligning this action with Prajney (PM) after Alvin Choo queried the existing agreement at 00:47 AM.

**Status Updates & Key Dates**
*   **Current Date:** April 1, 2026.
*   **BCRS Status:** Final deliverable confirmed ready and complete as of March 31 (10:49 AM). Alvin Choo expressed congratulations to the team at 11:02 AM on March 31.
*   **MP Deployment:** Successfully pushed to production by Sneha Parab at 10:51 AM on March 31.
*   **Critical Deadline:** Met; March 31 was the final day for BCRS deliverables and deployment activities.
*   **Flag Enablement:** Resolved at 00:59 AM on April 1, 2026.

**Reference Links**
*   Deployment Verification Link: `https://chat.google.com/room/AAQAX9iKYf0/CjKvfZ07Lb4/kIo2WYTccYY?cls=10`


## [35/54] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Last Activity: 2026-04-01T00:03:09.167000+00:00 | Last Updated: 2026-04-01T06:52:30.919006+00:00
**Daily Work Briefing Summary (Updated: April 1, 2026)**

**Main Topics & Discussions**
1.  **Programmatic Advertising (Advertima/TTD):** Focus remains on validating discrepancies for `advertima_ttd-fixed-price-test-1.5`. Ravi Singh confirmed receipt of raw BURLs; validation was targeted for Monday, March 17th. Yian Koh requested confirmation on deals `advertima_ttd-first-price-test` and `advertima_ttd-fixed-price-test-1`.
2.  **New Deal Setup:** Yasmina Tregan (Advertima) required an end-to-end test setup this week. Wei Phung to share live campaign details; Ravi Singh to execute setup, push to TradeDesk, and map segments before launch.
3.  **BCRS UAT & Finance Integration:** Progress on SAP document numbers, duplicate posting fixes via PubSub "exactly once" policy (PR #1033), and Bukit Timah Plaza pricing/display issues.
4.  **Event Sync Optimization (DPD-645):** Addressing the massive event overage (14M vs. normal 550k). PRD deployment plan set for Sunday, March 15.
5.  **Security & Compliance:** RMN Pentest fixes (DPD-700) deployed to Prod; Bitbucket App Passwords deprecated effective June 9, 2026.

**Status Update: Inbox & Communications**
*   **Inbox Status:** As of April 1, 2026 (00:03 UTC), the workspace inbox is fully caught up across all categories (**Urgent Action Items**, **Thematic Project Updates**, **Meeting Updates**, and **FYI**). No pending unread items require immediate attention. This status follows confirmations from daily summaries dated March 24 through March 31. The latest update from Workspace Studio confirms zero backlog in all sections, including Code Reviews and Project Updates.

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
*   **June 9, 2026:** Bitbucket App Password deprecation deadline.

**Note on New Content:** The daily summary from April 1, 2026 (00:03 UTC), via Workspace Studio confirms the inbox remains clear of urgent action items across all categories. No changes to pending actions or decisions were required based on this update; historical context regarding project statuses and deadlines remains valid.


## [36/54] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY | Last Activity: 2026-03-31T23:16:10.242000+00:00 | Last Updated: 2026-04-01T06:53:28.491999+00:00
**Updated Briefing: BCRS Firefighting Group**
**Date:** March 31, 2026 (Latest activity: ~11:17 PM / New update @ 11:16 PM)
**Source:** Google Chat Space & Shared UAT Tracker (95 messages total)

### **Key Participants & Roles**
*   **Prajney Sribhashyam:** Project Lead/Test Coordinator.
*   **De Wei Tey / Michael Bui / Wai Ching Chan:** Finance/SAP, Re-delivery specialists, and Technical Integration.
*   **Dany Jacob / Eswarlal Rajesh / Sneha Parab:** Active test participants and finance coordinators.
*   **Alvin Choo:** Status reporting lead (monitoring Starship channel updates).
*   **Akash Gupta:** Mentioned stakeholder regarding Quick Buy deployment.
*   **New/Active Stakeholders:** Shiva Kumar Yalagunda Bas, Chee Hoe Leong, Tiong Siong Tee, Daryl Ng, Koklin Gan, Hang Chawin Tan.

### **Main Topics**
1.  **Business Live Checklist Initiation (March 31, ~11:16 PM):** Prajney posted a "Business live checklist," triggering significant engagement with 31 replies and views by 28 of 42 members. This supersedes previous status inquiries as the primary focus for final readiness verification.
2.  **Quick Buy Deployment Confirmation:** Wai Ching Chan confirmed GovTech Quick Buy integration was deployed to production on March 30; inclusion in communication loops is verified.
3.  **Critical Feature Sign-Offs Confirmed (March 30):** Prajney confirmed sign-off for refunds across E-Comm and Scan & Go channels, completing critical features for the April 1 launch. Updated were CC'd to Koklin Gan.
4.  **Legacy App Invoice Logic Query:** Prajney raised a critical question regarding invoice reflection for customers on older app versions purchasing BCRS items (specifically deposit reflection). Thread generated 10 replies and was viewed by 29 of 42 members, with last reply @Tiong Siong Tee and @Hang Chawin Tan at 8:46 AM.
5.  **Linkage Investigation:** Shiva Kumar Yalagunda Bas flagged missing linkages on March 30 (~09:20 AM), requiring immediate investigation by Chee Hoe Leong.

### **Decisions & Updates**
*   **Launch Readiness Transition:** Focus has shifted from status queries to a formal checklist review initiated at 11:16 PM. While refund sign-off solidifies readiness for the April 1 deadline, the legacy app invoice logic query remains a potential risk requiring resolution before launch.
*   **RPA Status Inquiry:** Previous inquiry regarding live RPA execution in production (raised ~05:30 AM) generated 10 replies and was viewed by 26 of 40 members; this is now subsumed under the new Business Live Checklist.

### **Pending Actions & Owners**
| Action Item | Owner(s) | Status/Context |
| :--- | :--- | :--- |
| **Execute Business Live Checklist** | Prajney Sribhashyam / Team | **Critical:** 31 replies active; requires immediate completion to validate April 1 readiness. |
| **Clarify Legacy App Invoice Logic** | Tiong Siong Tee / Hang Chawin Tan | **Urgent:** Address invoice behavior for older app versions (deposit reflection) raised at 06:55 AM. |
| **Resolve Missing Linkages** | Shiva Kumar Yalagunda Bas / Chee Hoe Leong | **Active:** Investigating linkage failures flagged March 30; viewed by 18 of 39 members. |
| **Overall Status Update** | Alvin Choo / Team | **Pending:** Report Starship channel updates and final checklist outcomes to stakeholders. |

### **Key Dates & Deadlines**
*   **April 1:** Critical launch deadline; all critical features (including Refunds) signed off as of March 30.
*   **March 31 (Today):** Date of active RPA verification request, legacy app invoice logic query, Quick Buy confirmation, and Business Live Checklist initiation (~11:16 PM).
*   **March 30:** Date of refund sign-off, linkage issue flagging, and Quick Buy deployment to production.

### **Historical Context Retained**
*   Original SAP Deposit API development deadline of Feb 20 remains noted as missed/risked; current effort focuses on resolving specific re-delivery logic gaps via live testing.
*   Existing e-comm test accounts remain unusable for Pre-order staff app; new BCRS CF items and specific GWP SKUs are required.
*   Deposit SKU linking investigation continues due to failure to link post-publishing (now explicitly flagged by Shiva Kumar Yalagunda Bas).
*   Previous Re-delivery flow testing experienced audio issues on March 16; current Production effort aims to resolve logic gaps via grooming and live validation.


## [37/54] BCRS ECOMM SAP POSTING
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


## [38/54] [Prod Support] Ecom FFS Ops
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


## [39/54] Web Chapter
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


## [40/54] BCRS Firefighting Group
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


## [41/54] [BCRS]-SAP to POS & DBP Interface Deployment
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


## [42/54] QE <-> All Tribes
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


## [43/54] Yangyu Wang
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


## [44/54] [Internal] (Ecom/Omni) Digital Product Development
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


## [45/54] D&T Funtastic Team
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


## [46/54] Plan the activity for Power Breakfast - Mar 31
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


## [47/54] Web Chapter
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


## [48/54] BCRS Firefighting Group
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


## [49/54] [D&T] Discussion service account key decommission
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


## [50/54] @ecom-ops #standup - Mar 31
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


## [51/54] Backend Chapter
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


## [52/54] @omni-ops #standup - Mar 31
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


## [53/54] Project Light Attack and Defence Leads
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


## [54/54] Nikhil Grover
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
