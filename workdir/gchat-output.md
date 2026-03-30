

## [1/29] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-03-30T02:30:26.278000+00:00 | Last Updated: 2026-03-30T02:38:01.119517+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Update)**
**Date:** March 30, 2026 (Early Morning Shift)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 699

### Key Participants & Roles
*   **System/Tool:** Datadog App (Automated Monitoring)
*   **Notification Channel:** `@hangouts-ShoppingCartNotification`
*   **Ownership Teams:** `dpd-pricing`, `dpd-pricing-cart`.

### Main Topic
Instability persists in `frontend-gateway` and `st-cart-prod`. Following the critical cascade on March 29, activity continues into March 30 (01:10–02:30 UTC). The failure mode has evolved to include recurring oscillation across **Checkout**, **Cart Update** (`post /api/cart`), and **Wish List** endpoints. Notably, a new success rate drop was detected on the `st-cart-prod` service (Monitor `22710472`).

### Incident Timeline & Actions
**Previous Context:**
*   *Extended activity from March 20 through March 29, with critical peaks at 21:15 UTC (Cart P99 >20s).*

**New Activity (March 30 UTC)**
*   **01:10–01:47 UTC:** Recurring latency spikes on `put /api/product/_id/wish-list` and `get /api/wish-list/_id`. Monitor `21245706` triggered at 01:10 (P90: 4.099s) and recovered by 01:13.
*   **01:12–01:29 UTC:** Checkout success rate dipped to **99.87%** (Monitor `21245708`) before recovering at 01:29 (99.913%).
*   **01:14–01:36 UTC:** Cart Update P99 spiked to **3.678s** (Threshold: 2.6s; Monitor `21245713`), recovering at 01:36 (P99: 0.805s).
*   **01:47–02:13 UTC:** Oscillation on Wish List GET (`get /api/wish-list/_id`). Triggers occurred at 01:47 (P90: 1.721s), 02:01 (P90: 2.009s), and 02:28/02:30 (P90: 1.802s). Intermittent recovery observed between triggers.
*   **02:03–02:13 UTC:** Additional spike on `put /api/product/_id/wish-list` (P90: 5.173s; Monitor `21245706`). Recovered at 02:13 (P90: 0.638s).
*   **02:08–02:19 UTC:** Critical Success Rate Drop on `st-cart-prod`. Monitor `22710472` detected Checkout/Cart load success rate of **99.611%** (Threshold <99.9%). Recovered at 02:19 (100.0%).

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** The incident window has extended to March 30. New degradation observed on `st-cart-prod` success rates, distinct from the `frontend-gateway` latency issues previously tracked.
*   **Immediate Action Required:** Correlate trace data for the 01:10–02:30 UTC window. Investigate specific Event IDs: `8565947574587741934` (Checkout Success Rate), `8565949686211893059` (Cart P99 Peak @ 01:14), and `8566004698553781073` (`st-cart-prod` Success Rate).

### Decisions Made
*   **Priority Escalation:** Status remains **"Critical Incident"**. Activity is continuous from March 20 through at least 02:30 UTC on March 30.
*   **Focus Shift:** Analysis must now prioritize `st-cart-prod` success rate degradation (Monitor `22710472`) alongside the persistent latency oscillation on `frontend-gateway`.
*   **Metric Update:** Confirmed rotating failure mode: Cart Update P99 reached 3.678s; Checkout Success Rate dropped to 99.87%; Wish List GET P90 peaked at 2.009s; `st-cart-prod` success rate dropped to 99.611%.

### Key Dates & Follow-ups
*   **Critical Window:** Extended activity from March 20 through at least March 30, 02:30 UTC.
*   **Follow-up:** Immediate trace correlation for the early morning cascade (01:10–02:30 UTC) to determine if root cause is environmental or traffic-based before shift handover.

### References
*   **Active Monitors:** `21245706` (Wish List PUT P90), `21245708` (Checkout Success Rate), `21245713` (Cart Update P99), `21245720` (Wish List GET P90), `22710472` (`st-cart-prod` Success Rate).
*   **Service Tags:** `service:frontend-gateway`, `service:st-cart-prod`, `team:dpd-pricing`.


## [2/29] @ecom-ops #standup - Mar 30
Source: gchat | Group: space/AAQAqo-_GgY | Messages: 5 | Last Activity: 2026-03-30T02:28:31.460000+00:00 | Last Updated: 2026-03-30T02:38:15.614543+00:00
**Daily Work Briefing: @ecom-ops #standup (Mar 30)**

**Key Participants & Roles**
*   **Sneha Parab**: Standup facilitator; initiated the session call.
*   **Dang Hung Cuong**: Technical lead/architect; identified memory issues and defined test scope.
*   **Hanafi Yakub**: Invitee (attendance not explicitly confirmed in snippet).
*   **Shiva Kumar Yalagunda Bas**: Provided technical clarification on data synchronization logic and operational review requirements.

**Main Topic/Discussion**
The discussion focused on the scope of an upcoming load test for the order synchronization system, specifically addressing a previous Out of Memory (OOM) error. The team debated whether to isolate the "CM51" component or test the entire order sync process. Additionally, there was a brief technical clarification regarding the latency and operational workflow of seller profile changes within the master data.

**Decisions Made**
*   **Test Scope**: Dang Hung Cuong directed that the load test must cover the **whole order sync** process, explicitly rejecting a test limited only to "CM51."
*   **Rationale**: The decision was driven by a prior incident where testing the whole process resulted in an OOM error; isolating CM51 would not replicate this systemic risk.

**Pending Actions & Owners**
*   *Execute Load Test*: Conduct a load test on the entire order sync workflow (not just CM51). **Owner**: Implied engineering team (likely Dang Hung Cuong's direct reports or Shiva Kumar Yalagunda Bas based on context).
*   *Operational Review Protocol*: No new action item assigned yet, but the constraint that "seller changing won't be reflected in master immediately" without an ops team review was established as a system behavior.

**Key Dates, Deadlines & Follow-ups**
*   **Date**: March 30, 2026 (Standup session).
*   **Reference Case**: Previous OOM failure occurred during a full process test (specific date not cited, but referenced as "last time").
*   **Next Steps**: The team needs to execute the broader load test strategy defined by Dang Hung Cuong.

**Specific References & Technical Notes**
*   **System Issue**: Out of Memory (OOM) error previously encountered during full process testing.
*   **Component Mentioned**: CM51 (excluded from current test scope).
*   **Data Sync Behavior**: Seller profile changes do not reflect in the master database immediately; they require a review by the operations team before propagation.


## [3/29] @omni-ops #standup - Mar 30
Source: gchat | Group: space/AAQAPG9qdz4 | Messages: 5 | Last Activity: 2026-03-30T02:28:21.310000+00:00 | Last Updated: 2026-03-30T02:38:29.920098+00:00
**Daily Work Briefing: #standup (omni-ops)**
**Date:** March 30, 2026
**Channel:** Google Chat (#standup) | [Link](https://chat.google.com/space/AAQAPG9qdz4)

### **Key Participants & Roles**
*   **Daryl Ng:** Facilitator; initiated the meeting and followed up on attendance.
*   **Yangyu Wang:** Participant; confirmed meeting status.
*   **Rohit Pahuja:** Presenter/Engineer; reported on completed tasks and upcoming plans.
*   **Sundy Yaputra, Rohit Pahuja (again):** Mentioned as invitees.
*   **Hanafi & Sneha:** External colleagues referenced regarding task delegation.

### **Main Topic**
The team convened for the daily standup. The primary discussion focused on attendance issues and a technical update from Rohit Pahuja regarding the removal of redundant steps in the Backoffice deployment pipeline due to resolved flaky tests.

### **Pending Actions & Ownership**
*   **Discuss Hanafi-related work:** Rohit Pahuja is scheduled to discuss this with Sneha today.
    *   *Context:* This discussion was necessitated because **Hanafi** is currently on leave.
*   **Assign task for deprecated pages:** Sneha will assign Rohit the specific task of removing deprecated pages from Backoffice.

### **Decisions Made**
*   No new technical decisions were recorded in this log. The conversation confirmed that all previously mentioned flaky test cases are now passing in a single run, validating the removal of the "Backoffice PR rerun step."

### **Key Dates & Follow-ups**
*   **March 30, 2026:** Rohit Pahuja missed the initial standup at 02:01 UTC due to another discussion. He provided his status update later that morning (approx. 02:28 UTC) after Daryl Ng requested updates regarding his absence.
*   **Today (March 30):** Rohit is to finalize discussions with Sneha and receive task assignments for the Backoffice cleanup.

### **Summary of Status**
Rohit Pahuja successfully submitted a Pull Request (PR) to remove the Backoffice PR rerun step, citing that all flaky tests are now stable in one run. Despite missing the initial sync due to conflicting meetings, Rohit has communicated his current progress and immediate tomorrow's schedule regarding Hanafi-related dependencies and Backoffice maintenance.


## [4/29] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 16 | Last Activity: 2026-03-30T02:25:03.724000+00:00 | Last Updated: 2026-03-30T02:39:14.168131+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (Updated March 30, ~02:30 UTC)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
Instability persists into the early morning of **March 30**. The issue profile has evolved from cyclical failures to a sustained session of intermittent errors affecting Identity APIs, Recommendation Services (Orchid), and Backend Latency. While late-night volatility (Mar 29) showed some recovery, a new wave of alerts triggered between **01:53 and 02:25 UTC** on March 30 confirms recurring high error rates in `engage-my-persona-api-go` and significant P90/P99 latency spikes across `lyt-p13n-layout` and specific Identity endpoints.

**Status Summary & Timeline (March 28 – Mar 30, Early Morning)**
*   **Identity API Instability (`engage-my-persona-api-go` / Squad Dynamics):**
    *   *Mar 30 Activity (01:53 – 02:24 UTC):* Recurring high error rates (>0.1%) observed. Peak value 0.113% @ 01:53 UTC; subsequent triggers at 02:24 UTC (0.1%).
    *   *Endpoint Latency & Success Drops:*
        *   **02:07:** Social login connections success rate dropped to 81.818%. Recovered @ 02:18 UTC.
        *   **02:09:** User discount scheme (MyInfo) load failure detected (99.888%). Recovered @ 02:18 UTC.
        *   **02:13 – 02:15:** P90 latency spike for `post_/new-myinfo/confirm` reached 2.112s. Recovered @ 02:14 UTC.
        *   **02:15 – 02:20:** P90 latency spike for `patch_/user/profile` reached 2.239s. Recovered @ 02:25 UTC.
*   **Gamification & Recommendation Services:**
    *   **Orchid Service (`frontend-gateway` / Squad Journey):** Triggered success rate dip (<99.9%) at **02:23 UTC** (Value: 99.724%).
    *   **Layout Service Latency (`lyt-p13n-layout` / Squad Journey):** Multiple P99 latency spikes >1.8s observed between 02:06 and 02:09 UTC affecting `post_/v1/scan-door/scratch-cards/claim` (Peak 2.521s) and `get_/v1/scan-door/store` (Peak 2.009s). Both recovered by 02:14–02:16 UTC.
*   **Mobile & Layout Services:**
    *   Prior issues with `ef-android` linkpoints noted on Mar 29; no new specific Mobile alerts in the March 30 window, though concurrent backend latency persists.

**Pending Actions & Ownership**
*   **Investigate Identity API Recurrence:** Analyze repeated error rates and specific endpoint failures (`social-login-connections`, `myinfo`, `post_/new-myinfo/confirm`, `patch_/user/profile`) occurring between 01:53–02:24 UTC on March 30. Owner: **Squad Dynamics**.
*   **Analyze Orchid & Gateway Intermittency:** Investigate the latest Orchid dip at 02:23 UTC and correlate with `lyt-p13n-layout` latency spikes observed between 02:06–02:09 UTC. Owner: **Squad Journey**.
*   **Review Latency Patterns:** Correlate P90/P99 spikes in Identity and Layout services to identify root cause of the sustained "sustained cyclical failure" model. Owner: **Squad Dynamics**, **Squad Journey**.

**Decisions Made**
*   **Severity Escalation:** Incidents remain critical due to multi-squad recurrence extending from Mar 28 through early morning Mar 30 (latest activity 01:53 – 02:25 UTC).
*   **Pattern Continuity:** The ecosystem instability has shifted to a "sustained cyclical failure" model. New latency issues in `post_/new-myinfo/confirm` and `patch_/user/profile`, alongside Orchid dips, have joined existing Identity and recommendation service failures.

**Key Dates & Follow-ups**
*   **Active Window:** March 28–30 (UTC). Recent critical activity: **01:53 – 02:25 UTC**.
*   **Reference Links:**
    *   `engage-my-persona-api-go` Error Monitor #92965074 (Latest Peak: 0.113% @ 01:53)
    *   `post_/new-myinfo/confirm` Latency Monitor #50879027 (P90: 2.112s @ 02:13)
    *   `patch_/user/profile` Latency Monitor #17447638 (P90: 2.239s @ 02:15)
    *   `lyt-p13n-layout` Scratchcard Claim Monitor #20382857 (P99: 2.521s @ 02:06)
    *   `frontend-gateway` Orchid Monitor #17448311 (Latest Trigger: 02:23, Value 99.724%)


## [5/29] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/jfuh2YauMzM | Messages: 13 | Last Activity: 2026-03-30T02:15:27.555000+00:00 | Last Updated: 2026-03-30T02:39:32.004967+00:00
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


## [6/29] Web Chapter
Source: gchat | Group: space/AAAASzhKzV0 | Messages: 1 | Last Activity: 2026-03-30T02:15:26.223000+00:00 | Last Updated: 2026-03-30T02:39:44.232298+00:00
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


## [7/29] Alvin Choo
Source: gchat | Group: dm/zmMZpgAAAAE | Messages: 15 | Last Activity: 2026-03-30T02:14:07.739000+00:00 | Last Updated: 2026-03-30T02:40:07.029434+00:00
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


## [8/29] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Messages: 21 | Last Activity: 2026-03-30T02:05:50.029000+00:00 | Last Updated: 2026-03-30T02:40:44.034266+00:00
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


## [9/29] [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Messages: 9 | Last Activity: 2026-03-30T01:46:28.163000+00:00 | Last Updated: 2026-03-30T02:41:16.411324+00:00
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


## [10/29] RMN Incidents
Source: gchat | Group: space/AAQAz11ATzY | Messages: 8 | Last Activity: 2026-03-30T01:15:17.707000+00:00 | Last Updated: 2026-03-30T02:41:35.551227+00:00
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


## [11/29] DPD AI Guild
Source: gchat | Group: space/AAQA5_B3lZQ | Messages: 1 | Last Activity: 2026-03-30T01:14:44.773000+00:00 | Last Updated: 2026-03-30T02:42:00.029536+00:00
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


## [12/29] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Messages: 50 | Last Activity: 2026-03-30T01:05:31.724000+00:00 | Last Updated: 2026-03-30T02:42:22.305427+00:00
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


## [13/29] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Messages: 17 | Last Activity: 2026-03-30T01:02:15.259000+00:00 | Last Updated: 2026-03-30T02:42:56.334537+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Mar 30, 01:02 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`.
*   **Escalations:** `@oncall-dpd-staff-excellence-pdm`, `@hangouts-GT-Search-DatadogAlerts`, `@hangouts-GT-Discovery-DatadogAlerts`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Retail Media.

**Main Topic**
**P2 ALERTS (ACTIVE):** The critical P2 alert for `fp-search-indexer` remains active with 100% error rate. A new P2 alert for `go-catalogue-service` triggered at 21:14 UTC showing 346 errors.

**Resolved Incidents:**
*   **`sku-store-attribute`:** Triggered again at 00:53 UTC on Mar 30, but **Recovered** at 01:01 UTC (Monitor ID `20382848`). The job processed sufficient files (>6) in the last 5h.
*   **`marketing-service`:** A new P4 throughput anomaly triggered at 23:45 UTC on Mar 29, but **Recovered** at 01:02 UTC (Monitor ID `17447110`).

**Pending Actions & Ownership**
*   **Action:** **INVESTIGATE CRITICAL ERRORS (`fp-search-indexer`):** [Status: ACTIVE] Address P2 alert for >0 errors on `env:prod`.
    *   **Owner:** Product Data Management On-Call.
    *   **Status:** **RE-TRIGGERED (21:13 UTC Mar 29).** Metric value reached 1.0. Active since Mar 18; no resolution achieved. Monitor ID: `17447691`.
*   **Action:** **INVESTIGATE HIGH ERROR COUNT (`go-catalogue-service`):** [Status: ACTIVE] Address P2 alert for >100 errors on `env:prod`.
    *   **Owner:** Product Data Management Team.
    *   **Status:** **NEW TRIGGER (21:14 UTC Mar 29).** Metric value reached 346. Monitor ID: `17447762`.

**Decisions Made**
*   The `fp-search-indexer` incident is critical with trace errors at 100%. Immediate investigation of Datadog, K8s, and Runbooks is mandated.
*   The `go-catalogue-service` requires immediate attention due to a spike of 346 errors.
*   Intermittent issues with `sku-store-attribute` appear resolved for the moment; monitoring continues for recurrence.
*   Throughput anomalies on `marketing-service` have self-corrected; no further action required at this time.

**Key Dates & Follow-ups (Mar 29–30, 2026)**
*   **Service: `fp-search-indexer` (P2 - Product Data Management) [ACTIVE CRITICAL]**
    *   *Latest Timeline:* Active since Mar 18; Re-triggered Mar 29 (21:13 UTC).
    *   *Links:* [Datadog](https://app.datadoghq.eu/monitors/17447691) | [K8s](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/fp-search-indexer/overview) | [Runbook](https://ntuclink.atlassian.net/wiki/spaces/SR/pages/2001831558/Support+Run+book)
*   **Service: `go-catalogue-service` (P2 - Product Data Management) [ACTIVE]**
    *   *Latest Timeline:* Triggered Mar 29 (21:14 UTC).
    *   *Links:* [Datadog](https://app.datadoghq.eu/monitors/17447762) | [K8s](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/go-catalogue-service/overview) | [Runbook](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2646212686/Catalogue+Service)
*   **Service: `sku-store-attribute` (P3 - Grocery Discovery) [RESOLVED]**
    *   *Latest Timeline:* Re-triggered Mar 30 (00:53 UTC); Recovered Mar 30 (01:01 UTC).
    *   *Links:* [Datadog](https://app.datadoghq.eu/monitors/20382848)
*   **Service: `marketing-service` (P4 - Retail Media) [RESOLVED]**
    *   *Latest Timeline:* Triggered Mar 29 (23:45 UTC); Recovered Mar 30 (01:02 UTC).
    *   *Links:* [Datadog](https://app.datadoghq.eu/monitors/17447110) | [K8s](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview) | [Runbook](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book)

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c


## [14/29] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/jIquLFJEGIc | Messages: 10 | Last Activity: 2026-03-30T00:48:49.801000+00:00 | Last Updated: 2026-03-30T02:43:12.741573+00:00
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


## [15/29] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Messages: 6 | Last Activity: 2026-03-30T00:40:24.961000+00:00 | Last Updated: 2026-03-30T02:43:46.201139+00:00
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


## [16/29] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Messages: 4 | Last Activity: 2026-03-30T00:03:09.786000+00:00 | Last Updated: 2026-03-30T02:44:30.044510+00:00
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


## [17/29] RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU | Messages: 10 | Last Activity: 2026-03-29T23:51:01.397000+00:00 | Last Updated: 2026-03-30T02:44:53.694272+00:00
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


## [18/29] Nikhil Grover
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


## [19/29] Nikhil Grover
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


## [20/29] #dd-fpg-watchdog-alert
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


## [21/29] Nikhil Grover
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


## [22/29] Nikhil Grover
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


## [23/29] Nikhil Grover
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


## [24/29] [BCRS]-SAP to POS & DBP Interface Deployment
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


## [25/29] BCRS Firefighting Group
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


## [26/29] BCRS Firefighting Group
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


## [27/29] Nikhil Grover
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


## [28/29] [Leads] (Ecom/Omni) Digital Product Development
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


## [29/29] [Prod Support] Ecom FFS Ops
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
