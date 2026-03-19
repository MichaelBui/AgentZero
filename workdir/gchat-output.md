

## gchat/space/AAAAsbHANyc: Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Last Activity: 2026-03-19T07:49:13.383000+00:00 | Last Updated: 2026-03-19T14:56:07.549372+08:00
**Daily Work Briefing: Shopping Cart Notification Alerts**
**Date:** March 17–19, 2026 (Update)
**Space:** `Shopping Cart Notification` (Google Chat)

### Key Participants & Roles
*   **System/Tool:** Datadog App (Automated Monitoring)
*   **Notification Channel:** `@hangouts-ShoppingCartNotification`
*   **Ownership Teams:** `dpd-pricing`, `dpd-pricing-cart`.

### Main Topic
Following March 16–18 incidents, transient latency issues persisted into March 19. Afternoon instability expanded from Checkout reliability to the `put_v2_shopping_list` endpoint. At **14:52 UTC**, a new critical alert triggered for request load success rates dropping below 99.9%, with the metric value falling to **97.143%**. This follows earlier P99 latency spikes in `get_v2_shopping_list` (10.887s) and prior Checkout SLO breaches.

### Incident Timeline & Actions
**Morning Spike (March 19, ~02:15 – 03:49 UTC)**
*   **Get Wish List by ID P90 (>1.7s):** Triggered at 02:15; Recovered.
*   **Get V2 Shopping List P99 (>4.0s):** Triggered 03:49 (Metric: **10.887s**); Recovered 03:58.
*   **Status:** All latency monitors recovered within minutes.

**Afternoon Recurrence (March 19, ~13:00 – 14:52 UTC)**
*   **Checkout Success Rate (<99.9%):** Triggered at 13:10; Recovered at 13:19.
*   **SLO Error Budget Alert:** Triggered at 13:57 (94.894% budget consumed).
*   **Put V2 Shopping List Success Rate (<99.9%) - Monitor ID `21245717`:**
    *   **Trigger Time:** 14:52 UTC.
    *   **Metric Value:** **97.143%**.
    *   **Service:** `frontend-gateway` (Resource: `put_/api/v2/shopping-list`).
    *   **Status:** **Active**. Datadog notification sent to `@hangouts-ShoppingCartNotification`.

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Investigation:** The new alert at 14:52 UTC confirms systemic instability affecting write operations (`put_v2_shopping_list`) in addition to read-heavy operations (Wishlist) and Checkout.
*   **SLO Breach Risk:** With 94.894% of the error budget consumed by 13:57 UTC, the system is on the verge of a breach. The new success rate drop at 14:52 UTC exacerbates this risk immediately.
*   **Correlation Required:** Link Event ID `8550344912656464335` (Current Alert) with previous events (`8550242097997133452`, `8550289276827905120`) to validate if the root cause is service-wide.

### Decisions Made
*   **Auto-healing Confirmed:** Previous transient issues self-corrected within minutes; however, the current 14:52 UTC alert indicates a sustained failure requiring immediate intervention rather than passive monitoring.
*   **Priority Shift:** Focus must shift to investigating the `frontend-gateway` service for `put_v2_shopping-list` specifically, alongside existing Checkout/Wishlist correlations.
*   **SLO Mitigation:** Urgent root cause analysis is required to halt error budget burn before the threshold exceeds 95%.

### Key Dates & Follow-ups
*   **Critical Window (March 19):** 02:15 UTC to 14:52 UTC.
*   **Follow-up:** Investigate Event ID `8550344912656464335` immediately. Correlate with Wishlist and Checkout failure patterns.

**References:**
*   **New Monitor Alert:** `21245717` (Event: `8550344912656464335`)
*   **Service Tags:** `service:frontend-gateway`, `team:dpd-pricing`, `dept:dpd`.


## gchat/dm/t3wf6EAAAAE: Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Last Activity: 2026-03-19T07:48:28.418000+00:00 | Last Updated: 2026-03-19T14:24:34.126562+08:00
**Daily Work Briefing: Nikhil Grover & Michael Bui**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator; coordinating UAT, managing configuration split flags, providing cost-saving metrics, and requesting meeting access.
*   **Michael Bui:** Technical Lead (Engineering); enabling deployments, validating API logic, managing Jira tickets, and granting meeting co-host privileges.

**Main Topics**
1.  **Deployment Acceleration (Vertical Scroll & Swimlane Ads):**
    *   **Timeline Shift:** Target go-live moved from Monday (March 23) to **Wednesday, March 19**, contingent on immediate UAT signoff.
    *   **Process Change:** Deployment can proceed today if Nikhil signs off on the Jira ticket after lunch. Without this, deployment pushes to Tuesday.
    *   **Configuration Management:** Michael emphasized setting split flags correctly. Nikhil will configure slots and share for confirmation before managing configurations independently going forward. Configs can be adjusted while keeping features disabled ("off") for safety.

2.  **UAT Scope & Data Sources:**
    *   UAT must cover both swimlanes and vertical scrolling simultaneously to validate shared API logic.
    *   **Data Source Verification:** Daryl is still required to identify Algolia vs. DS swimlanes on OMNI Home and enable test instances for ads.

3.  **Ad Placement Anomaly:**
    *   Nikhil observed ads on slots 2 and 4 during UAT, deviating from the `[1,3,3,5]` logic. Michael suspects Out-of-Stock (OOS) products are masking the logic and requires checking "Normal" behavior to confirm.

4.  **Cost Optimization:**
    *   Nikhil confirmed an estimated cost saving of **$4k/month** for Segment overage optimization.

5.  **Meeting Access & Collaboration Tools:**
    *   **Access Restriction:** Nikhil requested co-host privileges for meetings, noting he lacks Gemini access otherwise.
    *   **Resolution:** Michael Bui confirmed the request was completed at 13:56 on March 19.

**Decisions Made**
*   **Accelerated Deployment:** Proceed with deployment on Wednesday, March 19, provided UAT signoff is received after lunch.
*   **Configuration Handover:** Nikhil to assume responsibility for setting slot split flags after initial confirmation by Michael.
*   **Ticket Consolidation:** Segment/ Omni optimization tasks consolidated into the existing DPD ticket structure.
*   **Collaborative Access:** Nikhil Grover granted co-host status on meetings to facilitate collaboration in the absence of Gemini access.

**Pending Actions & Owners**
*   **UAT Signoff (Nikhil Grover):** Provide Jira signoff and configure split flags after lunch on March 19 for today's deployment attempt.
*   **Data Source Verification (Daryl):** Identify Algolia vs. DS swimlanes on OMNI Home and enable instances for testing.
*   **Ad Placement Investigation (Michael Bui):** Verify if OOS products cause slot 2/4 anomalies by checking "Normal" behavior.
*   **Ticket Consolidation:** Nikhil Grover to ensure Segment optimization details are correctly linked within the DPD ticket.

**Key Dates & Deadlines**
*   **March 19, 2026 (Today):** Target deployment date contingent on afternoon UAT signoff; cost saving ($4k/mo) confirmed; meeting co-host access granted at 13:56.
*   **Next Monday (March 23, 2026):** Original target go-live (now superseded by today's accelerated timeline).
*   **Monday Stand-up:** Review OSMOS SKU support process.

**Historical Context Note**
Previous discussions established readiness for dynamic slots UAT with the `[1,3,3,5]` logic resolved. This session introduced vertical scrolling complexities and data source uncertainties (Algolia vs. DS). On March 20, negotiations shifted focus from a Monday go-live to an immediate deployment on Wednesday, March 19, pending configuration signoff. New discussions also clarified Segment optimization savings ($4k/mo) and ticket organization protocols. Additionally, operational access was updated on March 19 at 13:56 to grant Nikhil Grover co-host privileges for meetings due to limited Gemini access.


## gchat/space/AAAAxwwNw2U: #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Last Activity: 2026-03-19T07:46:03.409000+00:00 | Last Updated: 2026-03-19T14:56:54.683174+08:00
# Daily Work Briefing: #dd-dpd-rich-alert Monitoring Activity (Extended Update)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert` channel members.
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey, DPD Engage (`squad:dynamics`, `squad:journey`, `squad:compass`, `tribe:engage`).

**Main Topic**
The incident window persists on **March 19**, characterized by a "flicker" pattern of latency spikes and error rate degradation. New volatility has been observed affecting `engage-my-persona-api-go` (MyInfo flows), `gamification-api`, `lyt-p13n-layout`, and iOS linkpoint loading metrics.

**Status Summary & Timeline (Extended)**
*   **March 16–18:** Initial cascade involving `gamification-api`, transient cart errors, and intermittent MyInfo latency. Continued instability detected on March 18 with peak error rates of 0.158% in `engage-my-persona-api-go`.
*   **March 19 (Afternoon Volatility):**
    *   **iOS Linkpoint Loading:** At 14:44 UTC, Monitor #63109468 triggered for `ef-ios` success rates dropping to **97.81%** (<99.9% threshold). Recovered by 14:45 UTC (metric at 100%).
    *   **MyInfo Error Rate:** At 14:46 UTC, Monitor #92965074 for `engage-my-persona-api-go` showed a high error rate but recovered immediately to **0.092%** (just below the >0.1% trigger threshold).
    *   **MyInfo Latency Spike:** At 14:49 UTC, Monitor #50879027 triggered for P90 latency on `post_/new-myinfo/confirm` exceeding 1.8s. Metric reached **2.528s**.
    *   **Orchid Recommendations:** Frontend Gateway requests (`get_/api/recommender/orchid`) previously dipped to 99.853% success rate around 14:38 UTC (Monitor #17448311), recovering by 14:48 UTC (metric at 100%).
    *   **Previous Events:** MyInfo P99 latency (2.656s) and Gamification error rates (0.435%) occurred earlier between 14:17–14:33 UTC, consistent with the flicker pattern.

**Pending Actions & Ownership**
*   **Investigate `engage-my-persona-api-go` (Dynamics):** Address recurring P90 latency spikes (peak 2.528s at 14:49 UTC) and error rate fluctuations. Prioritize monitors #50879027, #50879037, and #92965074.
*   **Investigate `ef-ios` (Compass):** Analyze transient linkpoint loading failures dropping to 97.81% at 14:44 UTC. Owner: Squad **Compass**.
*   **Investigate Mobile Services (`ef-android`) (Compass):** Correlate previous iOS dips with backend API volatility. Owner: Squad **Compass**.
*   **Investigate `lyt-p13n-layout` (Journey) & Frontend Gateway:** Analyze transient P99 latency spikes on scan-door requests and Orchid recommendation success rates. Owner: Squad **Journey**.

**Decisions Made**
No strategic decisions recorded. The incident confirms a systemic "flicker" pattern persisting into March 19 afternoon (14:44–14:49 UTC):
1.  **Latency Instability:** `engage-my-persona-api-go` exhibits recurring P90 latency spikes (>2.5s) with rapid recovery times (<5 mins).
2.  **Error Rate Volatility:** iOS linkpoint success rates and `gamification-api` error rates show transient surges, suggesting shared infrastructure or dependency contention affecting the Omni Home experience.

**Key Dates & Follow-ups**
*   **Active Window:** March 16–19 (UTC).
*   **Follow-up Required:** Immediate root cause analysis for recurring latency spikes in MyInfo confirm flows and iOS linkpoint loading; stabilize `gamification-api` error rates.
*   **Reference Links:**
    *   iOS Linkpoints: Monitor #63109468
    *   MyInfo Latency (P90): Monitor #50879027
    *   Gamification Errors: Monitor #92939290
    *   Orchid Requests: Monitor #17448311


## gchat/space/AAQAgT-LpYY/HAKjA0njutA: BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/HAKjA0njutA | Last Activity: 2026-03-19T07:42:39.598000+00:00 | Last Updated: 2026-03-19T14:56:24.358574+08:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Initiator/Coordinator; tracking UAT refund issues and escalating discrepancies to Finance, CS, and RPA teams.
*   **Hendry Tionardi:** Technical Analyst (RPA); investigating duplicate API calls and SAP Odata logs.
*   **De Wei Tey:** Assigned recipient of investigation requests regarding order anomalies.
*   **Wai Ching Chan:** Assigned recipient of query regarding sales posting logic for vouchers/Linkpoints.

**Main Topic**
Investigation into specific refund and sales data discrepancies observed during the BCRS UAT 2026 cycle, specifically focusing on duplicate entries and missing postings in Finance records.

**Pending Actions & Ownership**
*   **Investigate Duplicate Refund Entry (Order #75549782):** Determine why two refund entries were posted with a ~4-minute gap.
    *   *Owner:* **De Wei Tey** (and RPA Team).
    *   *Context:* Hendry suspects the RPA may have triggered duplicate SAP Odata calls.
*   **Investigate Missing Sales/Refund Postings:** Verify if Finance's report of "no sales or refund posting" is expected for orders #75549643 and #75549853, specifically regarding customer usage of e-vouchers and/or Linkpoints.
    *   *Owner:* **Wai Ching Chan**.
*   **RPA Log Review:** Check RPA logs to confirm if the system called SAP Odata twice for Order #75549782.
    *   *Owner:* **De Wei Tey** (explicitly requested by Prajney).

**Decisions Made**
*   No final root cause was determined during this session; however, Hendry hypothesized that the duplicate refund entries were caused by the RPA calling SAP Odata twice rather than a functional error.
*   The team agreed to use the "UAT Refunds (RPA, CS & Finance)" track in the Google Sheet for centralized tracking.

**Key Dates & Follow-ups**
*   **Date:** March 19, 2026.
*   **Timeframe:** Discussion occurred between 14:42 and 14:51 (SGT).
*   **Next Steps:** Immediate log analysis for Order #75549782 and clarification on voucher/Linkpoint posting rules for the two specified orders.

**References**
*   **Tracking Sheet:** https://docs.google.com/spreadsheets/d/1o6oklFTFyzpT490vQ4x8IKc00vdL41pl9hUAaQgg-ns/edit?usp=sharing
*   **Space URL:** https://chat.google.com/space/AAQAgT-LpYY


## gchat/space/AAQAN8mDauE: [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Last Activity: 2026-03-19T07:27:36.925000+00:00 | Last Updated: 2026-03-19T13:37:56.311773+08:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Sneha Parab:** Lead/Manager; coordinating cross-team support, SAP/API integration blockers.
*   **Michael Bui:** Engineering/RMN Architect; managing architecture updates and infrastructure compliance.
*   **Alvin Choo:** Leadership; addressing feedback loops, release schedules, and new epic queries.
*   **Gopalakrishna Dhulipati:** Lead; overseeing risk registers, delivery approvals, and now leading service key rotation with SRE.
*   **Others Active:** Daryl Ng (raised recent inquiry), Andin Eswarlal Rajesh, Olivia, Koklin, Zaw.

**Main Topics**
1.  **SAP/Deposit SKU Integration Blocker:** Marketplace lacks deposit data for SAP API integration. Proposed manual UD failed MP Ops sign-off due to poor PM communication; Olivia rejected new technical solutions. Immediate action from SAP team required.
2.  **Requirement Clarity (BCRS):** Michael Bui flagged that "follow existing ones" is unacceptable acceptance criteria for BCRS deposit posting. Explicit UAT scenarios are required for Definition of Ready (DoR).
3.  **Infrastructure Compliance:** Bitnami ending free Docker images impacts `sonic_raptor` and `mkp-fairnex`. Migration is mandatory.
4.  **Service Key Rotation:** Gopalakrishna Dhulipati requested leads take ownership with the SRE team; discussion moved to a dedicated room.
5.  **B2B Testing Alignment:** Sneha Parab raised queries on finalized B2B testing procedures. Zaw requires guidance on producing MP SKUs specifically for B2B testing.
6.  **New Epic Inquiry (OMNI-1157):** Daryl Ng raised an item from the weekly epics (Jira link: OMNI-1157). Ravi indicated this action should only be performed for the new app. Alvin Choo and Gopalakrishna Dhulipati were tagged to clarify status.

**Pending Actions & Owners**
*   **OMNI-1157 Clarification:** Confirm if the item applies solely to the new app as per Ravi's feedback; coordinate with Daryl Ng. (Owners: Alvin Choo/Gopalakrishna Dhulipati)
*   **Service Key Rotation:** Leads to take ownership of rotation with SRE. Review details in dedicated room. (Owner: All Leads / Gopalakrishna Dhulipati)
*   **B2B Testing Procedure:** Clarify process for producing MP SKUs and confirm alignment status. Response required from Gopalakrishna Dhulipati regarding Zaw's inquiry. (Owner: Sneha Parab/Gopalakrishna Dhulipati)
*   **SAP Timeline Resolution:** Push SAP team to explore deposit SKU data solutions; provide timeline. (Owner: Sneha Parab/Alvin Choo/Gopalakrishna Dhulipati)
*   **BCRS Requirements:** Define explicit UAT scenarios with Koklin. (Owner: Alvin Choo/Gopalakrishna Dhulipati)
*   **Infrastructure Migration:** Address Bitnami Docker image end-of-life. (Owner: Engineering Team/Michael Bui)
*   **RAW Forms Review:** Review Risk Register for DPD RAW forms; confirm handovers and renew expired forms. Deadline: Tomorrow EOD. (Owner: All Leads/Sazali Bin Mohammed Ali's team)

**Decisions Made**
*   **RMN Architecture:** Michael Bui updated current, future, and transition architecture diagrams.
*   **Townhall Coordination:** Team to meet Hui Hui post-townhall; no full Q&A scheduled.
*   **Release Status:** Questions remain regarding holding today's regular app release (pending confirmation).

**Key Dates & Deadlines**
*   **RAW Forms Review:** Due Tomorrow EOD.
*   **Townhall Meeting:** Today post-townhall session.
*   **Chee Hoe Support:** Effective end of March for Product Catalogue/MarTech scope.
*   **Bitnami Migration:** Ongoing (immediate action required).


## gchat/space/AAQAUbi9szY: [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Last Activity: 2026-03-19T07:09:48.304000+00:00 | Last Updated: 2026-03-19T13:36:21.779688+08:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Key Participants & Roles**
*   **Sneha Parab:** BCRS/Fees/Store Closure Impact Lead.
*   **Daryl Ng:** Backoffice/Order Management/Bug Reporting / Amplitude Tracking inquiry.
*   **Michael Bui:** BCRS Deposit Logic/SAP Integration/Publisher of PRs.
*   **Wai Ching Chan:** Order Service Deployment/Slot Logic Validation.
*   **Andin Eswarlal Rajesh:** Frontend (iOS/Android) & BCRS UX queries / Amplitude tracking investigation.
*   **Lester Santiago Soriano:** Backend Services Lead.
*   **Others:** Akash Gupta, Piraba Nagkeeran, Jonathan Tanudjaja, Zaw Myo Htet.

**Main Topics Discussed**
1.  **Order Verification Bug (NED-278216):** Daryl Ng flagged an order verification failure. The investigation points to the Whitelisting API returning older contract data (identified by Andin Eswarlal Rajesh). Team members Akash Gupta and Wai Ching Chan are reviewing this issue.
2.  **BCRS Deposit & SAP Integration:** Critical issue regarding duplicate deposit postings remains active (Fix in progress: PR #6).
3.  **Order Re-delivery Logic:** Confirmation received regarding `completed_at` value updates during re-delivery status changes from "dispatch" to "completed".
4.  **Event Tracking Integration:** Investigation ongoing into Frontend event flow to Amplitude via the tracking service (Andin Eswarlal Rajesh assigned).
5.  **Payment Feature Flagging:** Zaw Myo Htet announced the complete offboarding of the split feature flag for Pinelabs in UAT to facilitate specific testing.
6.  **Store Closing Process:** Sports Hub FFS store closure scheduled for **31 Mar 2026**. Team continues to request inputs on Marketplace SKU removal and fulfillment impact.
7.  **UAT & Inventory Logic:** Sneha Parab flagged a UAT query regarding bulk threshold data for Meiji Paigen Cultured Milk SKU (`0-fat-13023506`). Investigation focuses on `inventory-service` vs. catalogue/stock_override tables (Wai Ching Chan, Akash Gupta, Daryl Ng involved).
8.  **Notification Deployment:** Query regarding gChat notification changes for "1HD" deployment status in production.

**Pending Actions & Ownership**
*   **Lester Santiago Soriano:** Review PR #1538 (`bitbucket.org/ntuclink/go-platform-website/pull-requests/1538`). Assist with Whitelisting API contract issue (cc: Piraba Nagkeeran, Jonathan Tanudjaja).
*   **Akash Gupta & Wai Ching Chan:** Investigate NED-278216 order verification failure and the Whitelisting API returning older contracts.
*   **Zaw Myo Htet:** Execute testing on offboarded Pinelabs split feature flag in UAT.
*   **Michael Bui:** Deploy PLU processor changes (scheduled ~2-3pm); Request UD for listed SKUs; Review PR `bcrs-deposit-posting` #6.
*   **Wai Ching Chan:** Validate PFC slot logic in UAT (requested by Daryl Ng). Assist in identifying the source of bulk threshold settings for UAT SKU `13023506`.
*   **Andin Eswarlal Rajesh:** Investigate iOS slot mapping error and assist with Amplitude event tracking flow inquiry.
*   **Team/Backend:** Resolve Daryl Ng's query regarding 1HD gChat notification deployment status.

**Decisions Made**
*   **Deployment Approval:** Sneha Parab approved PLU processor deployment pending UD alignment. Wai Ching Chan confirmed order-service PR #2910 is safe for production at 11 PM on Mar 9 (Note: Current date context suggests this decision applies to past planning or requires re-verification).
*   **Delivery Fee Config:** "Express" segment addition deemed acceptable.
*   **UAT Configuration:** Pinelabs split feature flag disabled in UAT by Zaw Myo Htet for testing purposes.

**Key Dates & Deadlines**
*   **Mar 9 (Historical/Reference):** PLU processor deployment; Production deploy of order-service changes (11 PM).
*   **Thursday (Upcoming):** D&T All Hands meeting.
*   **Mar 31, 2026:** Sports Hub FFS store closure deadline.
*   **Ongoing:** UAT validation for inventory thresholds, Code Review cycles, and Amplitude/Re-delivery logic investigations.

**Note on Historical Context:** Previous mentions of code review priorities for `layout-service` PR #362, `website-service` PR #649, and `lt-strudel-api-go` PR #472 are superseded by the new urgent request for Lester to review PR #1538. The focus has now shifted to resolving NED-278216 and Pinelabs UAT testing.


## gchat/space/AAQAUJW8HMo: ❗ Important Email
Source: gchat | Group: space/AAQAUJW8HMo | Last Activity: 2026-03-19T07:05:17.753000+00:00 | Last Updated: 2026-03-19T14:57:46.798511+08:00
**Daily Work Briefing Summary (Updated)**

**Key Participants & Roles**
*   **Michael Bui (You):** Managing Osmos support, event RSVPs, FileVault compliance, performance feedback, and Project Light coordination.
*   **Alvin Choo:** Organizer of the "1 on 1 with michael" meeting; organizer of "[Placeholder] Project Light."
*   **Miguel Ho Xian Da (FairPrice):** Lead requesting OSMOS integration for new retail media touchpoints.
*   **Tong A. Yu (Accenture):** Proposed focused working session to review content landscape and integration options.
*   **Winson Lim:** Guest attendee for Alvin Choo's performance meeting.
*   **Bryan Choong (FairPrice):** On leave until Mar 24; OSMOS concerns deferred to his return.

**Main Topics**
1.  **Performance Feedback & Project Light:**
    *   **Feedback Session:** Scheduled for Wednesday, Mar 18, 2026, at 4:00 PM SGT with Alvin Choo and Winson Lim.
    *   **Project Light:** **UPDATED TIME**: Meeting rescheduled to **Thursday, March 19, 2026, from 5:00 PM – 6:00 PM SGT** (previously 3:00–4:00 PM). Location: FairPrice Hub-11-L11 Cappuccino (10) [Google Meet]. Attendees include Tiong Siong Tee, Akash Gupta, Daryl Ng, and Gopalakrishna Dhulipati.
2.  **OSMOS Retail Media Integration (High Priority):** FairPrice Group is scaling Smart Carts, Digital Price Card, and IPOS, creating a need to consolidate disparate Content Management Systems (CMS).
    *   **Status:** OSMOS supports dynamic video/images; short-term integration is feasible if architecture details are provided.
    *   **Action:** Accenture team (Tong A. Yu) and Miguel Ho agreed to prioritize a working session next week to define the integration architecture.
3.  **DPD Team BBQ:** Celebratory dinner for Mar 17, 2026 (6:00 PM – 9:00 PM) at BBQ Box, Jurong Point. Meet Lobby A at 5:45 PM.
4.  **Mandatory Security Compliance:** FileVault encryption required by Mar 31, 2026.

**Pending Actions & Ownership**
*   **Project Light RSVP (Michael Bui):** **Critical**: Reply to Alvin Choo's updated invitation immediately confirming attendance for the new slot (Mar 19, 5:00 PM SGT).
*   **Performance Meeting RSVP (Michael Bui):** Confirm attendance for Mar 18, 4:00 PM SGT.
*   **OSMOS Coordination:** Support Accenture team in developing the detailed integration architecture. Await timeslots from Miguel Ho to schedule the working session.
*   **FileVault Encryption (Michael Bui):** Register via calendar ASAP. Book appointment with Geek Squad (FP Hub Level 15) for Mar 28 deadline (Final: Mar 31). Bring MacBook; backup files to Google Drive.

**Decisions Made**
*   **OSMOS Capability:** Confirmed feasible short-term integration for dynamic media, contingent on receiving SmartCart/IPOS architecture details from FPG.
*   **Working Session:** Prioritized for the week following March 12 to clarify requirements and determine long-term vision (Centralized CMS vs. intermediary layer).
*   **Legacy SA Definition:** Accounts from 2019–2020; key removal priority before decommissioning.

**Critical Dates & Deadlines**
*   **Mar 16, 2026 (EOD):** RSVP deadline for DPD BBQ.
*   **Mar 18, 2026 (4:00 PM):** Performance Feedback Meeting with Alvin Choo/Winson Lim.
*   **Mar 19, 2026 (5:00 PM – 6:00 PM):** **Updated** Project Light meeting with Alvin Choo and team at FairPrice Hub-11-L11 Cappuccino.
*   **Mar 24, 2026:** Bryan Choong returns; OSMOS support resumes.
*   **Mar 28, 2026:** Internal FileVault deadline.
*   **Mar 31, 2026:** Final FileVault compliance and FY2025 cycle closure.


## gchat/space/AAQAgT-LpYY/LNq_qjvCggc: BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/LNq_qjvCggc | Last Activity: 2026-03-19T06:59:02.027000+00:00 | Last Updated: 2026-03-19T13:35:49.578778+08:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Initiator/Inquirer regarding deployment status.
*   **Michael Bui:** Deployment lead (handling BCRS deposit posting).
*   **Sneha Parab:** Release manager clarifying dependency logic for Seller Reports and Marketplace changes.

**Main Topic**
Status verification of three specific feature deployments (Invoice, Sales Posting, Seller Reports) to Production (PRD), specifically regarding feature flags and UAT sign-off requirements.

**Decisions Made**
1.  **No Immediate Deployment:** None of the requested features (Invoice, Sales Posting, Seller Reports) are currently deployed to PRD.
2.  **Batch Release Strategy:** All changes must be released together to Production. Partial deployment is prohibited due to dependencies on BCRS data flows within the sync process.
3.  **Trigger Condition:** The combined release will occur only after receiving UAT sign-off for Marketplace based on new requirement changes.

**Pending Actions & Ownership**
*   **Michael Bui (Owner):** Await PRD deployment request.
    *   *Constraint:* Can only begin deploying to PRD after UAT sign-off is explicitly indicated in the Jira ticket.
    *   *Requirement:* Must include the expected completion date on the ticket.
*   **Team/Jira Owners:** Obtain and record UAT sign-off for Marketplace new requirement changes.
*   **Michael Bui (Owner):** Estimate a 1–2 day timeline for PRD deployment once initiated.

**Key Dates & Deadlines**
*   **Current Date of Discussion:** March 19, 2026.
*   **Estimated Deployment Duration:** 1–2 days post-initiation.
*   **Next Milestone:** Submission of UAT sign-off to Jira (Date TBD by team).

**Clarifications**
Prajney Sribhashyam sought clarification on whether the restriction referred specifically to the "SKU creation flow," though Sneha Parab confirmed the broader scope involves all changes dependent on BCRS data sync.


## gchat/dm/8oukJSAAAAE: Lester Santiago Soriano
Source: gchat | Group: dm/8oukJSAAAAE | Last Activity: 2026-03-19T06:52:25.338000+00:00 | Last Updated: 2026-03-19T14:55:40.152708+08:00
**Daily Work Briefing: Google Chat Summary**

**1. Key Participants & Roles**
*   **Lester Santiago Soriano**: Initiator of the inquiry; likely a Stakeholder, Project Manager, or Peer responsible for deployment coordination.

**2. Main Topic/Discussion**
*   The discussion centers on the operational status and scheduling of a specific deployment. Lester is confirming whether the `go-platform-website` service is scheduled for deployment on the current date (March 19, 2026).

**3. Pending Actions & Ownership**
*   **Action**: Provide confirmation regarding the deployment schedule for `go-platform-website`.
    *   **Owner**: The recipient of Lester's message (likely a Developer, DevOps Engineer, or Release Manager).
    *   **Status**: Awaiting response.

**4. Decisions Made**
*   No decisions were made in this conversation thread; it is an active inquiry seeking status confirmation.

**5. Key Dates & Deadlines**
*   **Date of Inquiry**: March 19, 2026 (14:52 UTC+8).
*   **Target Deployment Window**: "Today" (March 19, 2026).
*   **Follow-up Required**: Immediate response needed to clarify deployment status.

**6. Reference Details**
*   **Resource**: Lester Santiago Soriano
*   **Chat URL**: https://chat.google.com/dm/8oukJSAAAAE
*   **Project Artifact**: `go-platform-website`


## gchat/space/AAQAX9iKYf0: Team Starship
Source: gchat | Group: space/AAQAX9iKYf0 | Last Activity: 2026-03-19T06:46:28.605000+00:00 | Last Updated: 2026-03-19T14:57:20.594719+08:00
**Daily Work Briefing: Team Starship (Updated)**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Operations/Testing Lead (CT58, OMNI tickets).
*   **Danielle Lee:** Biz Ops/S&G Representative.
*   **Vivian Lim Yu Qian:** Product/Design Liaison.
*   **Alvin Choo:** Compliance Lead.
*   **Koklin Gan:** Technical Lead/POC for DPD-100 and OMNI tickets.
*   **Andin Eswarlal Rajesh:** Mentioned in bug ticket discussion.
*   **Sathya Murthy Karthik:** Shared Omni Roadmap update (March 2026).
*   **Ravi Goel:** Tagged regarding deprioritization review.

**Main Topics & Decisions**

1.  **Bug Report: App Icon Display (DPD-783)**
    *   **Issue:** Vivian reported a regression where the app icon displays a Christmas theme instead of the default, despite requests to revert from a CNY dress-up version.
    *   **Action:** A bug ticket (**DPD-783**) was created immediately with a request for urgent resolution ("asap").

2.  **OMNI Project Status & Compliance (Critical Updates)**
    *   **Omni Roadmap Review:** Per Sathya Murthy Karthik's message during today's Weekly Epics, PMs must review the "Omni Roadmap Consolidated from Jan 2026." A list of items to deprioritize is required by **EOD tomorrow**.
    *   **OMNI-1345 (Sales Breakdown):** MP Business has instructed an indefinite **hold** on this project due to foundational changes in the consolidated fulfilment business model driven by compliance inputs and business license limitations. No further work should proceed until requirements are finalized.
    *   **OMNI-1282:** Previously de-prioritized status remains valid; ticket requires a formal status change from "Define" to reflect this.
    *   **OMNI-1421:** SOP alignment with Ops team is TBC. Alvin has soft-blocked 5 days for this item.
    *   **Compliance Priorities:** Two high-priority topics remain: Quick Commerce and E-voucher Terms & Conditions.

3.  **Operational Pilots**
    *   Operations continues piloting the "picker app enhanced for CT58" on newer models (DT50S, DT66S). Prajney emphasized testing new models before store rollout. Pre-order staff application testing is noted.

4.  **CHAS Verification Flow**
    *   Auto-verification via MyInfo for CHAS/Senior/Pioneer/Merdeka remains technically feasible but outside current "Light" scope. Vivian to verify technical assumptions with Serene.

**Pending Actions & Owners**

| Action Item | Owner | Deadline/Note |
| :--- | :--- | :--- |
| **Urgent Fix:** Revert app icon display (DPD-783) | Engineering Team / Andin Eswarlal Rajesh | ASAP |
| Submit list of items to deprioritize from Jan 2026 Omni Roadmap | All PMs | **EOD Tomorrow** |
| Update OMNI-1282 status (De-prioritize) | Alvin Choo / Koklin Gan | Pending confirmation |
| **PAUSE** work on OMNI-1345 requirements | All Stakeholders | Until business model is finalized |
| Soft-block 5 days for OMNI-1421 SOP alignment | Alvin Choo | Completed |
| Prepare for BCRS progress review & capacity planning | Danielle Lee | See Meeting Below |
| Review Quick Commerce compliance items | Team | High Priority |
| Review E-voucher Terms & Conditions compliance | Team | High Priority |

**Key Dates & Follow-ups**

*   **Meeting Rescheduled:** Weekly Epics meeting postponed to **Wednesday, March 12 (tomorrow) at 11:00 AM**.
    *   **Location:** Level 12 Room 18 (subject to availability; virtual or pantry table as backup).
    *   **Agenda:** BCRS work progress review and upcoming ticket capacity planning.
*   **Reference Tickets:** SHOP-3779, OMNI-1099, DPD-100, **DPD-783**, OMNI-1345, OMNI-1282, OMNI-1421.


## gchat/space/AAQAgT-LpYY: BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY | Last Activity: 2026-03-19T06:42:21.866000+00:00 | Last Updated: 2026-03-19T14:58:18.911781+08:00
**Updated Briefing: BCRS Firefighting Group**
**Date:** March 19, 2026 (Latest activity: 3:49 PM)
**Source:** Google Chat Space & Shared UAT Tracker (55 messages total)

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
1.  **Refunds UAT Centralization:** Prajney established a dedicated tracker for BCRS UAT 2026 Refunds issues, specifically covering RPA, CS, and Finance domains. Accessible via Google Sheet (viewed by 11/37).
2.  **Production Deployment Verification:** Ongoing confirmation required on whether Invoice, Sales Posting, and Seller Reports changes are live in Production with correct feature flags.
3.  **UAT Readiness (SnG Refunds):** Validation requested for the March 23 UAT schedule regarding SnG refunds.
4.  **Deposit SKU Linking:** Investigation into Deposit SKUs failing to link to Master SKUs post-publishing.
5.  **Feature Expansion:** Assessment of effort/timeline for a 'BCRS container count' field in MP.

### **Decisions Made**
*   **Mobile Release:** Proceeded with mobile release on March 6 (Confirmed by Alvin Choo).
*   **Linkpoints Logic:** Confirmed Linkpoints issued for BCRS SKUs, but *not* for Deposit items.
*   **Invoice Formatting:** Issue with missing minus signs (Order #75502500) redeployed on March 13; cache clearing instructed.

### **Pending Actions & Owners**
| Action Item | Owner(s) | Status/Context |
| :--- | :--- | :--- |
| **Refunds UAT Issue Tracking** | Prajney Sribhashyam / Team | **New (Mar 19, 2:42 PM):** Launched dedicated thread and Google Sheet to track refund issues for RPA, CS, & Finance. 6 replies active. Link: `https://docs.google.com/spreadsheets/...` |
| **Production Deployment Confirmation** | Prajney Sribhashyam / Daryl Ng / Tiong Siong Tee / Michael Bui / Sneha Parab | **Active (Mar 19, 3:49 AM):** Query regarding Invoice, Sales Posting, and Seller Reports deployment status. Thread active with 3 replies. |
| **UAT Readiness for SnG Refunds** | Prajney Sribhashyam / De Wei Tey / Team | **Active (Mar 19, 2:56 AM):** Prajney confirmed readiness for March 23 UAT regarding SnG refunds. Thread active with 5 replies. |
| **Deposit SKU Linking Issue** | Shiva Kumar Yalagunda Bas / Chee Hoe Leong / Gautam Singh | **Active (Mar 18, 06:17):** Investigation required into Deposit SKU linking failure. Thread active with 18 replies. |
| **'BCRS Container Count' Field Assessment** | Prajney Sribhashyam / Sneha Parab | **Pending (Mar 17, 07:50):** Awaiting effort/timeline estimates from Sneha Parab post-discussion. |
| **DBP UAT Access Check** | Sathya Murthy Karthik / Hanafi Yakub / Sneha Parab | **Active (Mar 18, 10:39):** Query regarding `shu_hui.lai@fairpricegroup.sg` DBP UAT access. Thread active with 4 replies. |
| **BCRS + DF SKU Validation** | Sathya Murthy Karthik / Sneha Parab | **Pending:** Awaiting response on "BCRS eligible + DF" SKU existence (Mar 16). |

### **Key Dates & Deadlines**
*   **March 6:** Mobile release executed.
*   **March 13:** Invoice format redeployed.
*   **March 16 (07:44 UTC):** Re-delivery flow test call initiated.
*   **March 18 (06:17 UTC):** Deposit SKU linking issue reported.
*   **March 19 (2:42 PM):** Refunds UAT tracker established.
*   **March 19 (3:49 AM):** Query raised regarding Production deployment of Invoice, Sales Posting, and Seller Reports.
*   **March 23:** Target date for SnG Refunds UAT.

### **Historical Context Retained**
*   Existing e-comm test accounts deemed unusable for Pre-order staff app; new BCRS CF items and specific GWP SKUs (e.g., Coca-Cola Zero) required.
*   Original deadline for SAP Deposit API development was Feb 20 (missed/risk noted).
*   Re-delivery flow testing ongoing with audio issues reported on March 16 awaiting resolution.


## gchat/space/AAQAHH3dAYc/OceYc-m64a4: [D&T] Discussion service account key decommission
Source: gchat | Group: space/AAQAHH3dAYc/OceYc-m64a4 | Last Activity: 2026-03-19T06:41:21.327000+00:00 | Last Updated: 2026-03-19T14:42:45.479313+08:00
**Daily Work Briefing: D&T Discussion Service Account Key Decommission**

**Key Participants & Roles**
*   **Mohit Niranwal**: Defines security standards; confirms the initiative is compliance-driven.
*   **Michael Bui**: Implementation lead; seeking context on the driver for this specific initiative compared to previous automation requests.

**Main Topic**
Discussion regarding the decommissioning of D&T Discussion service account keys and adherence to a strict key rotation policy. The conversation addresses technical requirements, the strategic driver behind the current push, and questions regarding timeline delays in automation efforts.

**Key Decisions & Standards Established**
*   **Key Age Limit**: Service account keys must not be older than 90 days.
*   **Key Quantity**: Ideally, only one key per service account (SA) should exist at any time.
*   **Rotation Requirement**: All keys must be part of an active rotation process.
*   **Initiative Driver**: Confirmed by Mohit Niranwal that this is a mandatory **compliance initiative**.

**Pending Actions & Ownership**
*   **Action**: Provide detailed context on the compliance driver and explain the delay in automation solutions previously requested by Michael Bui (who asked for automated SA rotation last year).
*   **Owner**: Unspecified, but implied to be Mohit Niranwal or the security team responsible for the initiative communication.

**Key Dates & Timeline**
*   **2026-03-19**: Entire discussion occurred on this date.
    *   13:23 (IST): Policy standards defined.
    *   14:19 (IST): Michael Bui sought clarification on compliance drivers and automation history.
    *   14:41 (IST): Compliance nature confirmed.

**Follow-ups Required**
*   Clarification needed from Mohit Niranwal regarding the specific compliance mandates necessitating this immediate action despite prior requests for automated rotation.
*   Alignment required to resolve the gap between previous automation attempts and current manual/key-based enforcement.

**References**
*   **Space URL**: https://chat.google.com/space/AAQAHH3dAYc
*   **Subject**: [D&T] Discussion service account key decommission


## gchat/space/AAQAXn1ocmE: Retail out of home (Digital Screens & CMS)
Source: gchat | Group: space/AAQAXn1ocmE | Last Activity: 2026-03-19T06:29:07.057000+00:00 | Last Updated: 2026-03-19T14:43:43.911205+08:00
**Daily Work Briefing: Retail Out of Home (Digital Screens & CMS)**

**Key Participants & Roles**
*   **Priscilla Chan Li Wei:** Inventory management (Samsung ADE/FilmScreen); Escalation workflow impact analysis.
*   **David Anura Cooray:** Technical operations, screen connectivity, and CMS verification.
*   **Fiona U:** Project Lead/Coordinator; driving Phase 1 closure and stakeholder alignment.
*   **Rajkumar Romendro & Allen Umali:** Subject matter experts for Retail Media inventory and Screen Loading (MPBS/VXT).
*   **Cheng Joo Wu:** Assigned to Action Items regarding SOPs, Indirect Procurement (IP), IFM integration, and Engie scope liaison.
*   **Serene Tan Si Lin:** Clarification on facility management scope boundaries.

**Main Topic**
The discussion centers on operationalizing **Retail Out of Home (RoOH) Phase 1**, focusing on hardware inventory verification, digital screen content loading, transitioning from Hypercare to Business As Usual (BAU), and finalizing SOPs. A critical update concerns the **IFM** announcement: it is now confirmed that IFM will encompass the current Engie scope of responsibilities (building equipment, soft services, aircons, freezers). Digital monitors remain excluded from this maintenance scope.

**Pending Actions & Ownership**
*   **Sync Meeting Attendance:** Priscilla, Allen, Cheng, and Rajkumar must attend or assign a proxy to the sync scheduled for **Tuesday at 2:00 PM**.
    *   *Pre-meeting Review:*
        *   **SOPs (Gdoc & Gslide):** Resolve unresolved comments and perform consistency checks. Owners: Team (implied Priscilla/Cheng).
        *   **SLA Finalization:** Must be completed by next week for the Samsung SI meeting. Owner: Fiona U / Team.
        *   **Communication Channels:** Define escalation paths between stores and AdOps; identify chat groups to sunset. Owner: Team.
        *   **Indirect Procurement (IP):** Clarify IP's specific role before integrating them into the Retail Media Workflow. Owner: Cheng Joo Wu.
*   **Inventory Verification:** David Anura Cooray requested a master list of all digital screens under Retail Media; pending response from Allen Umali and Rajkumar Romendro.
    *   *Scope Update:* Inventory scope explicitly includes **PDD Gondola End Large TVs**.
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


## gchat/space/AAQAN8mDauE/ewxUvQHmSUM: [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/ewxUvQHmSUM | Last Activity: 2026-03-19T06:11:08.484000+00:00 | Last Updated: 2026-03-19T14:22:35.681744+08:00
**Daily Work Briefing: Service Key Rotation Initiative**

**Key Participants & Roles**
*   **Gopalakrishna Dhulipati:** Initiator/Owner. Assigned lead role for the service key rotation topic with SRE.
*   **Sneha Parab & Michael Bui:** Leads (Ecom/Omni) Digital Product Development. Granted access to the discussion space; currently seeking clarification on initiative drivers.
*   **Rajesh:** Excluded from the specific thread by Gopalakrishna Dhulipati at the request of the assigner.
*   **Alvin Choo & Himal & Mohit:** Mentioned in recent queries regarding compliance status; provided no clear answer to Michael Bui's inquiry.

**Main Topic**
Coordination regarding a **service key rotation** initiative involving the SRE (Site Reliability Engineering) team under the "Leads" resource group for Ecom/Omni Digital Product Development. Recent focus has shifted from access resolution to understanding the strategic drivers of the project.

**Pending Actions & Ownership**
*   **Action:** Michael Bui requires clarification on whether the initiative is a **compliance requirement** or a **normal operational improvement**. He previously consulted Himal and Mohit without success.
    *   **Ownership:** **Gopalakrishna Dhulipati** (along with **Alvin Choo**) must address this inquiry to clarify the driving factor.
*   **Technical Execution:** While Michael Bui has indicated he understands the necessary tasks and is ready to assist ("I can help us with that"), execution is paused pending clarity on the "why" behind the initiative.

**Decisions Made**
*   **Access Control:** Only specific leads (Sneha Parab, Michael Bui) were granted access to the dedicated Google Chat room. Rajesh was explicitly excluded.
*   **Scope Confirmation:** The discussion involves the SRE team for key rotation procedures.
*   **Clarification Gap:** It remains undetermined whether the initiative is compliance-driven or an improvement project, as initial inquiries to Himal and Mohit yielded no clear answers.

**Key Dates & Follow-ups**
*   **2026-03-16T12:18:42 UTC:** Gopalakrishna Dhulipati initiated the request and shared the room link.
*   **2026-03-17T06:00:07 UTC & 06:00:59 UTC:** Sneha Parab and Michael Bui reported lack of access.
*   **2026-03-17T06:01:17 UTC:** Gopalakrishna Dhulipati resolved the access issue for Sneha and Michael, noting Rajesh's exclusion.
*   **2026-03-19T14:11:08+08:00:** Michael Bui raised a query regarding compliance vs. improvement status via Google Chat, tagging Gopalakrishna Dhulipati and Alvin Choo.

**Next Steps**
1.  **Gopalakrishna Dhulipati** and **Alvin Choo** must provide a definitive answer to Michael Bui's question regarding the compliance nature of the initiative.
2.  Once the driving factor is confirmed, Michael Bui and Sneha Parab will proceed with coordinating technical execution with SRE based on their understanding of the requirements.


## gchat/space/AAQAHH3dAYc: [D&T] Discussion service account key decommission
Source: gchat | Group: space/AAQAHH3dAYc | Last Activity: 2026-03-19T06:06:01.925000+00:00 | Last Updated: 2026-03-19T14:22:59.237523+08:00
**Daily Work Briefing: [D&T] Service Account Key Decommission**

**Key Participants & Roles**
*   **Himal Hewagamage:** Project Lead/Owner. Confirming key status and defining the onboarding/decommission workflow.
*   **Michael Bui:** Stakeholder seeking clarification on security compliance context, prioritization (PRD/UAT), and execution plans.
*   **Nicholas Tan:** Confirmed project affiliation ("D&T"), noting "dpd" is defunct.
*   **Kyle Nguyen:** Infrastructure team lead; clarified that the Infra team leads this workstream (distinct from RE teams) but will review SAs on their own projects.
*   **Mohit Niranwal:** Provided specific security standards regarding key age and quantity.

**Main Topic**
A security hardening initiative to decommission duplicate, unused, or manually rotated GCP service account keys and migrate active accounts to an automated rotation policy. The scope covers the D&T domain (excluding defunct "dpd"). Current focus is on identifying specific usage patterns for accounts like `firebase-adminsdk-j0aml@fairprice-on-mobile-app` and establishing a standard where no key exceeds 90 days old, with ideally one key per SA.

**Pending Actions & Ownership**
*   **G Suite Group Onboarding:** Application teams must provide G Suite group names for any service accounts still in use with old keys to enable automated rotation onboarding.
    *   *Owner:* Application Team Leads (General).
*   **Key Decommissioning:** Once new keys are generated and pipelines updated, existing old keys will be removed from GCP. If an SA is confirmed unused, all associated keys will be deleted immediately.
    *   *Owner:* Himal Hewagamage / Infra Team.
*   **Prioritization Strategy:** Prioritize Service Accounts (SAs) related to PRD first, followed by UAT-related SAs for verification.
    *   *Owner:* Michael Bui (Proposed), Himal Hewagamage (Execution).
*   **Clarification on Execution Plan:** Determine specific steps to unblock or expedite the process.
    *   *Owner:* Kyle Nguyen / Infra Team.

**Decisions Made & Standards**
*   **Security Standard:** Keys must not be older than 90 days; ideally, only one key per SA should exist, and all must be part of the automated rotation policy.
*   **Workflow Logic:**
    *   If an SA is in use: Onboard new keys via G Suite group -> Update pipeline -> Decommission old keys.
    *   If an SA is unused: Remove all associated keys immediately.
*   **Defunct Services:** "dpd" remains confirmed as defunct and excluded from active usage.

**Key Dates & References**
*   **Initiation Date:** March 16, 2026 (Messages began at 07:43 UTC).
*   **Recent Discussion:** March 19, 2026, between 13:09 and 14:06 UTC.
    *   *Specific Case:* `firebase-adminsdk-j0aml@fairprice-on-mobile-app.iam.gserviceaccount.com` identified as having multiple active keys.
*   **Primary Resource:** [GCP][Security] Service Account Key Rotation & Decommission Spreadsheet.
    *   URL: https://docs.google.com/spreadsheets/d/1mGBCTRQDcTs0z_w0LjVtywDCtFHZhZfWYIRGqcNglpQ/edit?gid=0#gid=0
*   **Space Link:** https://chat.google.com/space/AAQAHH3dAYc

**Next Steps**
Himal Hewagamage will await G Suite group names from leads to onboard active accounts. Michael Bui has requested prioritization of PRD-related SAs and seeks confirmation on the current execution plan to assist in unblocking progress. Kyle Nguyen clarified that while the Infra team leads this workstream, they will also conduct independent reviews for their own projects.


## gchat/dm/yHhI1sAAAAE: Zaw Myo Htet
Source: gchat | Group: dm/yHhI1sAAAAE | Last Activity: 2026-03-19T05:59:42.142000+00:00 | Last Updated: 2026-03-19T14:23:34.171944+08:00
**Daily Work Briefing Summary**

**Key Participants & Roles**
*   **Zaw Myo Htet:** Initiator of the inquiry; requesting process clarification.
*   **Michael Bui:** Respondent; unable to answer specific question, provided referral.
*   **Calvin Phan:** Identified as the subject matter expert for preorder processes (no direct participation in this thread).

**Main Topic**
Clarification on operational workflow regarding order posting procedures specifically comparing "OG order posting" versus "Preorder order posting."

**Key Dates & Context**
*   **Date of Conversation:** March 19, 2026.
*   **Timeframe:** 13:50 – 14:00 (Local Time).
*   **Urgency Level:** Marked as "a bit urgent" by Zaw Myo Htet at 13:51.

**Decisions Made**
*   Michael Bui confirmed he does not possess the knowledge to answer whether OG and Preorder posting processes are identical.
*   The inquiry was effectively closed within this thread after Michael directed the question to Calvin Phan.

**Pending Actions & Ownership**
*   **Action:** Verify if "OG order posting" and "Preorder order posting" follow the same procedure.
*   **Owner:** Zaw Myo Htet (to contact Calvin Phan) or Calvin Phan (if approached directly).
*   **Reference:** The specific question remains open pending input from Calvin Phan.

**Follow-ups Required**
*   Contact **Calvin Phan** to resolve the procedural ambiguity regarding Preorder posting processes.


## gchat/space/AAAAQQGZSZU: RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU | Last Activity: 2026-03-19T05:53:30.957000+00:00 | Last Updated: 2026-03-19T14:24:53.240827+08:00
**Daily Briefing Summary: RMN Leadership Space**

**Key Participants & Roles**
*   **Bryan Choong:** Leadership (Out of office Mar 9–23).
*   **Rajiv Kumar Singh:** Team member; coordinating SOAC planning and Advertima operations.
*   **Michael Bui:** Inquired about Advertima future clarity.
*   **Allen Umali, Alvin Choo:** Addressed SRA/Advertima inquiries.
*   *Note: Jaren Loy Xing Wei (Departing), Pauline Tan, Christopher Yong remain as per previous context.*

**Main Topics**
1.  **Advertima Partnership Status:** Michael Bui questioned the future of Advertima operations, noting the current SRA covers only the Proof-of-Value (PoV) period. He clarified that an extended PoV or long-term partnership requires a new Service Request Agreement (SRA).
2.  **Operational Clarification:** Rajiv Kumar Singh confirmed that Advertima devices will continue operating under an extended PoV specifically through the end of April.
3.  **Previous Strategic Context:** Discussions on Criteo's AI integration, Jaren's departure, and rOOH sales priorities remain active background context for team alignment during Bryan's absence.

**Pending Actions & Owners**
*   **Advertima SRA Renewal:** Secure a new SRA for long-term Advertima partnership or extended PoV beyond the current agreement. *Owners: Allen Umali, Alvin Choo.*
*   **Ad Suppression with Osmos:** Provide firm ETA to resolve weeks-old issue. *Owner: Team.*
*   **SOAC Planning:** Finalize targets per CM, supplier, and category by end of March. *Owner: Rajiv Kumar Singh & Ryan.*
*   **Brand/Non-Endemic Sales:** Continue rOOH sales efforts (endemic via JBP; non-endemic via WOG/govt campaigns) and prepare for HPB meeting. *Owner: Team.*
*   **LinkedIn Content Cadence:** Maintain 1–2 posts weekly starting Mar 9. Gather ideas/case studies from the team. *Owner: Pauline Tan & Team.*

**Decisions Made**
*   **Advertima Continuity:** Confirmed extended PoV for Advertima devices through end of April pending SRA formalization.
*   **LinkedIn Launch:** "FPG ADvantage" page is live; frequency set at 1–2 times weekly.
*   **Strategic Focus:** Priorities during Bryan's absence locked to SOAC targets, rOOH sales, and HPB prep.

**Key Dates & Deadlines**
*   **Mar 2:** Criteo/ChatGPT partnership analyzed; Jaren's departure announced.
*   **Mar 5:** FPG ADvantage LinkedIn page went live.
*   **Mar 9 – Mar 23:** Bryan Choong away from office.
*   **Mar 19 (Today):** Advertima extended PoV confirmed for end of April; SRA update identified as necessary for long-term continuity.
*   **End of March:** Deadline to finalize SOAC targets per CM/supplier/category.
*   **April End:** Current deadline for Advertima extended PoV operations.
*   **Upcoming:** HPB meeting preparation required.


## gchat/dm/7d1XKcAAAAE: Google Drive
Source: gchat | Group: dm/7d1XKcAAAAE | Last Activity: 2026-03-19T05:48:20.013000+00:00 | Last Updated: 2026-03-19T14:25:24.600564+08:00
**Daily Work Briefing Summary (Updated)**

**Key Participants & Roles:**
*   **Nikhil Grover (FairPriceGroup):** Attempted to access "ACNxOsmos: Daily Cadence" notes; encountered Drive processing errors. Previously attempted to share "Programmatic Ads tracking events."
*   **Sujit Jha (Onlinesales.ai):** Attempted to share "Ads tracking events"; file access failed due to recipient blocking.
*   **Michael Bui (Business/Stakeholder):** Blocked Sujit Jha's document; previously flagged as a blocked user in Drive incidents.
*   **Tan Gay Lee (Finance):** Driving UAT financial validation requiring SAP document numbers.
*   **Hendry Tionardi (Operations/IT):** Managing technical clarifications on POS/SAP integration.

**Main Topics:**
1.  **BCRS UAT 2026 Financial Validation:** Finance requires SAP document numbers to verify end-to-end posting. Queries remain regarding discrepancies in document counts (3 documents for a $45.90 order) and missing BCRS documents affecting Row 4 and 5 validation.
2.  **Ads Tracking Data Sharing & Access Issues:** Continued failures in sharing tracking event documents between FairPriceGroup and Onlinesales.ai domains.
    *   **March 18:** Sujit Jha's "Ads tracking events" shared failed due to Michael Bui blocking `sujit.jha@onlinesales.ai`.
    *   **March 18:** Nikhil Grover's "Programmatic Ads tracking events - Source OSMOS" share failed with a Google Drive processing error.
    *   **March 19 (13:48 GMT+08):** Nikhil Grover requested Editor access to the document **"ACNxOsmos: Daily Cadence - 2026/03/16"** but received a "Google Drive is unable to process your request" error.

**Pending Actions & Owners:**
*   **UAT SAP Document Update:** Hendry Tionardi and the BCRS team must update Column J with valid SAP document numbers immediately. Finance cannot proceed without this data. *(Note: Original deadline was March 10; current date is now March 19, requiring urgent resolution).*
*   **Scan & Go Flow Confirmation:** Hendry Tionardi requested **Onkar Bamane** to confirm if the "Scan and Go" flow posts sales data as an aggregate invoice to SAP rather than individual receipts.
*   **Ads Tracking Resolution:** Michael Bui or Nikhil Grover must resolve access permissions for tracking documents (OSMOS source) with Finance/Operations, given persistent blockages and processing errors between domains.

**Decisions Made:**
*   **RMN Incident Impact:** Confirmed there is **no financial revenue impact**.
*   **Postmortem Template:** Michael Bui confirmed that breaking down the Executive Summary follows the approved **v2 postmortem template**.

**Key Dates & Deadlines:**
*   **March 6, 2026:** Initial request for SAP document numbers issued.
*   **March 10, 2026 (Original Deadline):** Finance required SAP document numbers in BCRS UAT spreadsheet (Missed).
*   **March 12, 2026:** D&T Q1 All Hands meeting.
*   **March 18, 2026:** Failed attempts to share Ads tracking files by Sujit Jha and Nikhil Grover.
*   **March 19, 2026 (13:48):** Nikhil Grover failed to gain Editor access to "ACNxOsmos" notes due to Drive processing error.

**References:**
*   **BCRS UAT 2026 Spreadsheet:** [Link](https://docs.google.com/spreadsheets/d/1o6oklFTFyzpT490vQ4x8IKc00vdL41pl9hUAaQgg-ns/edit)
*   **RMN Incident Report (v2 Template):** [Link](https://docs.google.com/document/d/1XiN0diQicup7ujoCWWKdD3Hvp8J0OJD5LPOfnthegyE/edit)
*   **Postmortem v2 Template:** [Link](https://docs.google.com/document/d/1ZntG-Ggb1NI7WLUa2uLb6u5RX9VxYUefUT364OWOJhI/edit)
*   **ACNxOsmos Daily Cadence (Access Failed):** [Link](https://docs.google.com/document/d/1LWKTTxcCJxIS12EkIvJmyXFNfjHXCF5ZYu2v5Vg4r9o/edit?usp=drive-dynamite&userstoinvite=nikhil.grover@fairpricegroup.sg&role=writer&ts=69bb8e22)
*   **Ads Tracking Events (Failed Share):** [Sujit Jha Link](https://docs.google.com/document/d/1LkZAkPEP5jNy1mkJDc9JzrpTG0PrDWZ8V2YVcmp2KA0/edit) | **Blocker:** Michael Bui.
*   **Programmatic Ads Tracking (Failed Share):** [Nikhil Grover Link](https://docs.google.com/document/d/1_DirQKHwYEkq2eOyfYkt0wcNj2jg2G_lOkvxghKIAj0/edit)


## gchat/space/AAAAu4WIubc: 📢 COM Notifications
Source: gchat | Group: space/AAAAu4WIubc | Last Activity: 2026-03-19T05:45:42.708000+00:00 | Last Updated: 2026-03-19T14:25:54.699327+08:00
**Daily Work Briefing: SonarCloud Quality Monitoring**

**Key Participants & Roles**
*   **gautam-ntuc**: Developer/Author; responsible for `catalogue-job` service commits and refactors.
*   **bitbucket-pipelines**: Automated CI/CD bot; triggered merges and UAT deployments.
*   **System/Webhook Bot**: Notification sender; continues to report recurring processing failures ("Webhook Bot is unable to process your request").

**Main Topic**
Automated SonarCloud quality gate scans for `catalogue-job`, `fpon-sap-jobs`, `seller-proxy-service`, and `fni-product-license-alert`. The conversation tracks code coverage, temporary hotfixes, and the resolution of failing Quality Gates.

**Status Summary by App**
*   **`catalogue-job` (gautam-ntuc)**:
    *   Addressed a temporary logic change to skip SKUs not existing in the DBP system.
    *   Coverage on new code fluctuated between 0% and 83.3%.
    *   Actions included reverting changes, merging commits, and refactoring the SKU exclusion list.
*   **`fpon-sap-jobs`**:
    *   Automated pipelines deployed artifacts and k8s configurations to UAT on March 9.
    *   Coverage: 72.7%. Unit Test Success was reported at 0%.
*   **`seller-proxy-service` (PR-2318 & PR-2306)**:
    *   **Historical Context**: Experienced persistent failure from March 9 through the morning of March 12; resolved to **PASSED** on March 12 with coverage stabilizing above 95%.
    *   **Recent Activity (March 19)**: PR-2306 (`ver. 0495bb5`) showed volatility on March 19 afternoon.
        *   Initial scan at **13:38 UTC** resulted in a **FAILED** status with 80.2% coverage.
        *   Subsequent scans at **13:44 UTC** and **13:45 UTC** both reported **PASSED**.
        *   Coverage on New Code stabilized at **80.2%** following the failure.
*   **`fni-product-license-alert`**:
    *   Two recent scans completed successfully on March 16.
    *   **PR-1433** and **PR-1450** (ver. 25b8d29) both achieved a Quality Gate Status of **PASSED**.
    *   Coverage on New Code stabilized at 94.4% for both requests.

**Pending Actions & Ownership**
*   **System Error Investigation**: The "Webhook Bot is unable to process your request" error persists in every notification from March 5 through the latest scans on March 19 (including PR-2306). No specific owner was assigned; this requires immediate engineering attention.
*   **`fpon-sap-jobs` Unit Tests**: Despite a 72.7% coverage rate, "Unit Test Success (%)" is reported at 0%. This discrepancy requires review by the `fpon-sap-jobs` team.

**Decisions Made**
*   No explicit human decisions were recorded; changes were driven by automated commits and pipeline executions.
*   The `catalogue-job` branch (`chore/DPD-671-temp-exclude-not-found-sku`) underwent multiple iterations of logic changes before stabilizing.
*   Recent merges in `fni-product-license-alert` (PR-1433, PR-1450) and the recovery scans for `seller-proxy-service` PR-2306 were accepted without manual intervention as Quality Gates passed automatically after initial failures or retries.

**Key Dates & Timeline**
*   **March 5**: Initial scan failures and coverage drops in `catalogue-job`; subsequent reverts and refactors by gautam-ntuc. Coverage recovered to 83.3% by 07:15 UTC.
*   **March 9**: UAT deployment for `fpon-sap-jobs` (04:30 & 05:09 UTC). First Quality Gate Failure recorded for `seller-proxy-service` PR-2318.
*   **March 12**: Final Quality Gate Failure for `seller-proxy-service` at 04:16 UTC. First **PASSED** status achieved shortly after (ver e8d8a39). Subsequent passes recorded on March 12 and 13 with coverage stabilizing above 95%.
*   **March 16**: Two successful scans for `fni-product-license-alert` at 04:26 UTC (PR-1433) and 04:30 UTC (PR-1450), both passing with 94.4% new code coverage.
*   **March 19**: PR-2306 in `seller-proxy-service` initially failed at **13:38 UTC** (ver. 0495bb5) with 80.2% coverage but recovered to **PASSED** in two subsequent scans at **13:44 UTC** and **13:45 UTC**.


## gchat/space/AAQA5_B3lZQ/8u4mgk65pbo: DPD AI Guild
Source: gchat | Group: space/AAQA5_B3lZQ/8u4mgk65pbo | Last Activity: 2026-03-19T05:45:01.869000+00:00 | Last Updated: 2026-03-19T14:26:05.501884+08:00
**Daily Work Briefing: DPD AI Guild**

**Key Participants & Roles**
*   **Zaw Myo Htet:** Proposer/Initiator. Suggested a technical strategy to optimize model usage and costs.
*   **Maou Sheng Lee:** Reviewer/Critic. Challenged the financial feasibility and tone of the proposal.

**Main Topic/Discussion**
The group discussed reducing heavy dependency on Retrieval-Augmented Generation (RAG) for local knowledge by utilizing quantized open-weight models to lower operational costs. Zaw Myo Htet shared a resource link (**Unsloth Docs**) suggesting this approach could reduce expenses, though it requires an initial investment. Maou Sheng Lee initially responded with skepticism regarding the budget ("no $"). Following Zaw's clarification that upfront spending is necessary to achieve long-term savings, Maou questioned whether the response sounded like "AI text."

**Actions Pending & Owners**
*   **Investigate Unsloth quantization:** Validate if the initial investment aligns with current budget constraints and technical requirements. (Owner: TBD/Team)
*   **Budget Approval:** Determine if funds are available for the proposed upfront cost to achieve future savings. (Owner: Maou Sheng Lee)

**Decisions Made**
No formal decisions or approvals were reached during this exchange. The discussion remains in the exploration and feasibility stage.

**Key Dates & Follow-ups**
*   **Date:** March 19, 2026
*   **Timeframe:** 13:27 – 13:45 (Local Time +08:00)
*   **Next Steps:** No specific follow-up date or deadline was set. Further discussion is pending budget clarification and validation of the Unsloth methodology.

**References**
*   URL: https://chat.google.com/space/AAQA5_B3lZQ
*   Resource: Unsoth Docs (https://unsloth.ai/docs)


## gchat/space/AAAAYX-ew1s: SRE / Network / DBA / DevOps / Infra
Source: gchat | Group: space/AAAAYX-ew1s | Last Activity: 2026-03-19T05:42:25.827000+00:00 | Last Updated: 2026-03-19T14:26:35.608685+08:00
**Daily Work Briefing: SRE / Infrastructure Team**

**Key Participants & Roles**
*   **Madhawa Mallika Arachchige:** Requests PR reviews/merges for Datadog configurations.
*   **Natalya Kosenko:** Raises IaC strategy questions, requests Terraform support, and submits compliance-related PRs.
*   **Kalana Thejitha:** Reports pipeline failures in new projects (Soni-BE).
*   **Lester Santiago Soriano:** Reports Go versioning conflicts in CI/CD pipelines.
*   **Dodla Gopi Krishna:** Requests Terraform review.
*   **Zheng Ming:** New stakeholder reporting US-Central1 internet connectivity failure for AI agents; opened ticket GCD-8941.
*   **Himal Hewagamage & Isuru Dilhan:** Primary reviewers/approvers for PRs and incident support.
*   **Mohit Niranwal:** Stages non-production verification for infrastructure changes.
*   **Tan Nhu Duong, Kyle Nguyen, Mohit Niranwal, Prabu Ramamurthy Selvaraj:** Tagged stakeholders/reviewers.

**Main Topics**
1.  **Datadog Infrastructure & Compliance:** Multiple requests to review/merge PRs (#135–#147) related to `fp-datadog-eu`. Strategic discussion initiated regarding IaC for Datadog log pipelines and RBAC enforcement for Agentic traces.
2.  **Terraform & Workspaces Management:** New PR **#719** submitted for `tfe-workspaces` by Natalya Kosenko. Previous requests included PR #716. A failed Terraform plan (`run-CZVLtajJGbLVojLM`) and ticket GCD-8900 remain active.
3.  **CI/CD Pipeline Failures:**
    *   **Soni-BE:** `golden pipeline` clone step failing on new projects; SSH key status questioned.
    *   **lt-strudel-api-go:** Build failure after upgrading Go to `1.25.8`; `golangci-lint` conflict noted.
4.  **Cloud Networking (New):** AI agents in `us-central1` mothership subnets cannot connect to the internet. Zheng Ming raised ticket **GCD-8941** to provision Cloud NAT for `us-central1`.

**Pending Actions & Ownership**
*   **Merge/Review Datadog PRs:**
    *   PR #135, #137–#139 (`fp-datadog-eu`): Owned by @Himal Hewagamage and @Isuru Dilhan.
    *   PR #144 & #147 (`fp-datadog-eu`): Owned by @Isuru Dilhan and @Himal Hewagamage.
    *   **PR #148 (`fp-datadog-eu`) & PR #719 (`tfe-workspaces`):** New requests from Natalya Kosenko; review pending with @Isuru Dilhan, @Himal Hewagamage, and @Kyle Nguyen.
*   **Troubleshoot Pipeline Issues:**
    *   Soni-BE Golden Pipeline clone failure: Investigate SSH key/environment (Kalana).
    *   `lt-strudel-api-go` Go version mismatch: Resolve `golangci-lint` config vs. target Go version conflict (Lester).
*   **Infrastructure Strategy:** Evaluate IaC implementation for Datadog log pipelines (Natalya; discussion ongoing with @Prabu Ramamurthy Selvaraj).
*   **Terraform Support:** Investigate failed run `run-CZVLtajJGbLVojLM` and ticket GCD-8900.
*   **Cloud NAT Provisioning (New):** Review Cloud NAT request for `us-central1`. **@Mohit Niranwal** requested testing in non-prod first before full rollout. @Himal Hewagamage and @Tan Nhu Duong are cc'd on ticket GCD-8941.

**Decisions Made**
*   **IaC Requirement:** Clear requirement established for IaC adoption for Datadog pipelines to ensure auditability.
*   **Change Management Protocol:** Mohit Niranwal mandated testing new Cloud NAT configurations in non-production environments prior to production deployment (regarding GCD-8941).

**Key Dates & Follow-ups**
*   **2026-03-02 to 03-05:** Multiple PR requests from Madhawa.
*   **2026-03-11 to 03-12:** Critical pipeline failures reported by Kalana and Lester.
*   **2026-03-13:** Datadog strategy discussion initiated; Terraform plan failure reported.
*   **2026-03-16:** Service desk ticket GCD-8900 opened; PR #147, #148 (`fp-datadog-eu`), and #719 (`tfe-workspaces`) requested by Natalya Kosenko.
*   **2026-03-19:** Zheng Ming reported connectivity failure for AI agents; raised ticket GCD-8941 for Cloud NAT provisioning in `us-central1`. Mohit Niranwal intervened regarding non-prod testing.


## gchat/space/AAQA5_B3lZQ: DPD AI Guild
Source: gchat | Group: space/AAQA5_B3lZQ | Last Activity: 2026-03-19T05:27:20.198000+00:00 | Last Updated: 2026-03-19T14:26:47.652173+08:00
### Daily Work Briefing: DPD AI Guild

**1. Key Participants & Roles**
*   **Michael Bui:** Research/Technical Lead – Introduced the new model release.
*   **Zaw Myo Htet:** Technical Strategy/Engineering – Proposed optimization strategy and cost reduction.

**2. Main Topic**
Discussion on leveraging the newly released **Mistral Small 4** to optimize local knowledge handling, specifically targeting a reduction in RAG (Retrieval-Augmented Generation) dependency and infrastructure costs through model quantization.

**3. Pending Actions & Ownership**
*   **Action:** Evaluate feasibility of replacing heavy RAG pipelines with quantized open-weight models to reduce costs.
    *   **Owner:** Zaw Myo Htet
    *   **Context:** Requires further technical assessment based on the Unsloth documentation provided.
*   **Action:** Investigate integration of Mistral Small 4's specific architecture (MoE, 119B total/6B active parameters) into current workflows.
    *   **Owner:** TBD (Team-wide due to recent announcement).

**4. Decisions Made**
*   **No formal decisions** were recorded in this thread; the conversation remains in the exploration and proposal phase. The team has acknowledged the technical capabilities of Mistral Small 4 and identified a strategic direction for cost reduction via quantization tools like Unsloth.

**5. Key Dates & References**
*   **2026-03-17:** Michael Bui announced the release of **Mistral Small 4**.
    *   *Specs:* MoE Architecture, 119B total parameters (6B active), 256k context window, Vision capability.
    *   *Reference:* https://mistral.ai/news/mistral-small-4
*   **2026-03-19:** Zaw Myo Htet suggested utilizing **Unsloth** for quantization to make open-weight models more cost-effective and reduce RAG reliance.
    *   *Reference:* https://unsloth.ai/docs
*   **Thread Status:** Active (Last reply noted as 36 minutes ago relative to briefing generation).


## gchat/space/AAAAQQGZSZU/sFEfapjbCgM: RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU/sFEfapjbCgM | Last Activity: 2026-03-19T05:21:31.244000+00:00 | Last Updated: 2026-03-19T14:27:00.701343+08:00
**Daily Work Briefing: RMN Leadership Space**

**Key Participants & Roles**
*   **Michael Bui:** Initiator of the inquiry; likely responsible for project continuity or device management.
*   **Allen Umali:** Copied on the SRA inquiry (likely decision-maker or legal/compliance contact).
*   **Alvin Choo:** Recipient of both inquiries (SRA clarification and access request).
*   **Rajiv Kumar Singh:** Requested to be added to the chat space.

**Main Topic**
Discussion regarding the operational status of **Advertima devices** following the conclusion of the Proof of Value (PoV) period, specifically concerning legal documentation (SRA) required for extended operations or a long-term partnership. Additionally, a request was made to expand the communication channel's membership.

**Pending Actions & Ownership**
1.  **SRA Clarification:** Michael Bui has requested clarity on whether a new Service Request Agreement (SRA) is required to continue running Advertima devices beyond the current PoV period. If confirmed, a new SRA must be drafted and executed.
    *   *Owner:* Team led by Alvin Choo (implied as the point of contact for documentation).
2.  **Chat Access Request:** Michael Bui requested that his Role Owner (**RO**) be added to this chat space.
    *   *Owner:* Alvin Choo (requested directly in the second message).

**Decisions Made**
*   No formal decisions were recorded in this thread. The conversation highlights an existing constraint: the current SRA only covers the PoV period, necessitating a new agreement for future operations.

**Key Dates & Follow-ups**
*   **Date of Conversation:** March 19, 2026 (Timestamps: 13:20 and 13:21).
*   **Reference Date:** The current SRA validity is tied to the PoV period; no specific expiry date was mentioned in the text.
*   **Next Steps:** Await confirmation from Alvin Choo regarding the necessity of a new SRA and the addition of Michael Bui's RO to the space.

**Contextual Notes**
*   **Resource Link:** https://chat.google.com/space/AAAAQQGZSZU
*   **Critical Constraint:** Continuing Advertima device operations without a new SRA is not permitted under current terms.


## gchat/space/AAAAzZ3qkNU: [Prod Support] Offers
Source: gchat | Group: space/AAAAzZ3qkNU | Last Activity: 2026-03-19T04:35:07.855000+00:00 | Last Updated: 2026-03-19T13:35:11.584637+08:00
**Daily Work Briefing: [Prod Support] Offers**

**Key Participants & Roles**
*   **Willie Tan:** Reported initial issue with offer visibility.
*   **Angela Yeo:** Escalated discrepancy regarding incorrect promo display; clarified expected pricing ($5.40).
*   **Alvin Choo:** Urgently flagged the pending resolution and requires immediate action.
*   **Zaw Myo Htet & Daryl Ng:** Tagged by Alvin Choo as the owners for investigation.

**Main Topic**
Investigation into production offer display errors for **SKU 13066243**. Two distinct issues were raised:
1.  Initial report (March 17) that Offer ID `sap offer 202603000112484` was not appearing online.
2.  Subsequent escalation (March 19) where two different promotions are currently visible; the team confirmed "2 for $5.40" is the correct configuration, but it has not appeared as expected.

**Pending Actions & Ownership**
*   **Action:** Urgently investigate and resolve why the correct offer ("2 for $5.40") is not displaying correctly (or if incorrect offers are showing) for the specified SKU.
*   **Owner:** @Zaw Myo Htet, @Daryl Ng.
*   **Status:** Active; flagged as urgent by Alvin Choo 17 minutes ago.

**Decisions Made**
No final technical decisions or fixes have been documented in this thread yet. The team has only agreed on the expected outcome: the offer must display as "2 for $5.40."

**Key Dates & Deadlines**
*   **Issue Reported:** March 17, 2026 (09:01 AM).
*   **Escalation to Investigation:** March 19, 2026 (10:04 AM and 12:35 PM).
*   **Most Recent Activity:** March 19, 2026 (Tagging of owners 17 minutes prior to briefing time).
*   **Deadline:** Immediate/Urgent resolution requested by Alvin Choo.

**Reference Links & IDs**
*   **Chat Space URL:** https://chat.google.com/space/AAAAzZ3qkNU
*   **Offer ID:** `sap offer 202603000112484`
*   **SKU:** 13066243
*   **Expected Price:** $5.40 (for "2 for" promo)


## gchat/space/AAAAwg3yipA: PFM x Events/UID Martech Issues
Source: gchat | Group: space/AAAAwg3yipA | Last Activity: 2026-03-19T04:07:59.815000+00:00 | Last Updated: 2026-03-19T13:35:34.129729+08:00
**Daily Work Briefing: PFM x Events/UID Martech Issues**

**Key Participants & Roles**
*   **Nicole Lim (PFM):** Initiator of requests regarding access, operational incidents, and automation validation.
*   **Sneha Parab:** Primary technical contact; tagged for access issues, event incidents, and the new exclusion list query.
*   **James Huang:** Tagged regarding the missing event incident and the current ownership of the Exclusion List automation.
*   **Stephanie & MA Team:** Requiring system access.

**Main Topic & Discussion**
1.  **Performance Marketing Exclusion List (New):** Nicole Lim reported a new update to a Google Sheet used for self-service exclusion of SKUs/categories from the DB catalogue to prevent prohibited product ads. A new `category_l3` was added on March 19. She requested confirmation that the associated automated job runs are functioning correctly, noting uncertainty regarding current ownership or handover status since Tze Hsien's departure.
2.  **Martech AI Chatbot Access:** Nicole Lim previously requested access for Stephanie and the MA team, creating ticket **NEDMT-2346**.
3.  **Critical Incident: Missing Events:** A data integrity issue occurred on **March 11**, where zero events were sent to all platforms. On **March 12**, Nicole flagged this as a potential upstream change.

**Pending Actions & Owners**
*   **Action:** Validate the automated job run for the Performance Marketing Exclusion List (DB catalogue) after the recent `category_l3` update.
    *   **Owner:** Sneha Parab, James Huang.
    *   **Context:** Confirm if automation is operational and identify current process ownership/handover status.
*   **Action:** Investigate and resolve the missing event issue for March 11 (0 events sent to all platforms).
    *   **Owner:** Sneha Parab, James Huang, and respective teams.
    *   **Context:** Requires confirmation on upstream changes causing the data gap.
*   **Action:** Process access request for Martech AI Chatbot.
    *   **Owner:** Technical team (assigned to Sneha Parab).
    *   **Scope:** Grant access for Stephanie and the MA team.

**Decisions Made**
*   No final resolution on the root cause of the March 11 missing events or the status of the Exclusion List automation; both require immediate technical validation.
*   Access request for Martech AI Chatbot remains pending completion.

**Key Dates & Follow-ups**
*   **March 10, 2026:** Ticket NEDMT-2346 created for access request.
*   **March 11, 2026 (UTC):** Incident date; zero events sent to platforms.
*   **March 12, 2026:** Missing event issue reported and escalated. Last reply at 02:22 AM UTC.
*   **March 19, 2026:** New exclusion category added; automation validation requested.
    *   *Last Reply Timestamp:* March 19, 12:07 PM UTC (Local Time).
*   **Immediate Follow-up:** Confirmation of upstream changes for the March 11 gap and verification of the Exclusion List automation workflow are required.

**Reference Links**
*   Ticket: https://ntuclink.atlassian.net/browse/NEDMT-2346
*   Chat Space: https://chat.google.com/space/AAAAwg3yipA
*   Confluence Ref: https://ntuclink.atlassian.net/wiki/spaces/CMT/pages/2674622589/Exclusion+Inclusion+Self-service+System


## gchat/space/AAQAcjNXKpA: DPD x Platform Engineering
Source: gchat | Group: space/AAQAcjNXKpA | Last Activity: 2026-03-19T03:47:56.300000+00:00 | Last Updated: 2026-03-19T13:36:53.224725+08:00
**Daily Work Briefing: DPD x Platform Engineering**

**Key Participants & Roles**
*   **Madhawa Mallika Arachchige:** On-call team restructuring lead.
*   **Alvin Choo:** Team Lead/Organizational structure owner.
*   **Michael Bui:** Stakeholder for RMN on-call grouping.
*   **Kyle Nguyen:** Infrastructure/Platform Engineering (Reviewer, Incident Triage).
*   **Sampada Shukla:** Reliability Engineer (Incident lead for Picking App).
*   **Wai Ching Chan:** Operations/On-call liaison.
*   **Lester Soriano:** Developer (Strudel API Go dependency issue).
*   **Daryl Ng:** Incident Analyst (ESP CPU usage, QC Food status).
*   **Akash Gupta:** User reporting Bastion access failure; proposing IaC policy change for on-call.
*   **Gopalakrishna Dhulipati:** Mentioned in on-call discussion.
*   **Maou Sheng Lee:** Mentioned in recent scaling discussion.

**Main Topics & Discussions**
1.  **On-Call Restructuring Methodology Debate:** Akash Gupta proposed shifting the new on-call team configuration from Terraform (IaC) to direct management via the Datadog UI (`https://app.datadoghq.eu/on-call/teams`).
    *   *Rationale:* Easier manual overrides for leave coverage, manageable volume of teams, and elimination of PR overhead.
    *   *Context:* This challenges the previous decision to use a strict two-PR Terraform process. The team (Madhawa, Kyle, Gopalakrishna) is reviewing this proposal following 7 replies in the thread.
2.  **Picking App Incident:** Sampada Shukla identified a spike in `502 Bad Gateway` errors for the Picking App since March 9, attributed to high churn on `picking-service-ilb` (>2,000 load balancer updates). Wai Ching Chan confirmed this impacts picker operations.
3.  **ESP Incident Analysis:** Daryl Ng noted CPU usage dropped during the incident period, hypothesizing a network-related cause rather than compute saturation.
4.  **Security & Dependency Updates:** Lester Soriano upgraded `lt-strudel-api-go` to address vulnerability `GO-2026-4603` but encountered pipeline failures due to `golangci-lint` being built on Go v1.24 while the target is v1.25.8.
5.  **Infrastructure Access & Changes:** Akash Gupta reported Bastion unavailability in PROD (`asia-southeast1-c`). Natalya Kosenko flagged potential manual deletion of Datadog monitoring resources causing Terraform drift.
6.  **QC Food Environment Status:** Daryl Ng confirmed the QC Food tile has been disabled on production (as of March 19). The team is now planning resource scale-downs. It remains unconfirmed whether Elastic Search (ES) will be scaled down or if services need to be restored.

**Pending Actions & Owners**
*   **Evaluate On-Call Tooling Strategy:** Madhawa, Kyle Nguyen, and Gopalakrishna Dhulipati to assess Akash Gupta's proposal to use Datadog UI instead of Terraform for the new on-call teams. *(Owner: Platform Engineering)*
*   **Investigate Picking App Churn:** Kyle Nguyen, Nicholas Tan, and Wai Ching Chan to determine the root cause of `picking-service-ilb` updates causing 502 errors.
*   **Restore Bastion Access:** Nicholas Tan, Kyle Nguyen, and Harry Akbar Ali Munir to investigate why the Bastion host is inaccessible for PROD order republishing.
*   **Resolve Go Pipeline Error:** Support required for Lester Soriano to reconcile `golangci-lint` version mismatch (v1.24 build vs v1.25.8 target).
*   **Review Infrastructure PR:** Natalya Kosenko's pull request `infra-gcp-fpg-titan/344` requires review from Kyle, Nicholas, Madhawa, and Dodla Gopi Krishna.
*   **Plan Resource Scale-Down:** Daryl Ng to coordinate with Kyle Nguyen, Maou Sheng Lee, and Alvin Choo regarding the scale-down of QC Food resources pending confirmation on ES requirements.

**Decisions Made**
*   *Tentative:* The team is debating whether to retain the Terraform-based change-freeze process or adopt direct Datadog UI management for on-call teams. No final decision recorded yet; awaiting review of Akash Gupta's proposal.
*   **QC Food Status:** Disabling confirmed on production. Resource scale-down planning initiated pending ES confirmation.
*   **Historical Context:** On-call teams were previously established under Alvin Choo's groups (`omni Opsa`, `App/Web`), with the RMN team retained as a distinct entity.

**Key Dates & Follow-ups**
*   **March 4:** On-call restructuring announcement issued.
*   **March 10:** Datadog resource deletion detected (Terraform drift).
*   **March 11:** Urgent request for QC Food UAT environment raised.
*   **March 12:** Go dependency vulnerability fix attempted; pipeline failure reported.
*   **March 13:** Critical incident regarding Picking App 502 errors and Bastion access failures.
*   **March 16, 08:58 UTC:** Akash Gupta submitted proposal to replace Terraform with Datadog UI for on-call management.
*   **March 19, 11:47 AM SGT:** Daryl Ng confirmed QC Food tile disabled on production and initiated scale-down planning discussion.


## gchat/space/AAQAN8mDauE/KtpVSnYJ3ys: [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/KtpVSnYJ3ys | Last Activity: 2026-03-19T03:39:26.426000+00:00 | Last Updated: 2026-03-19T13:37:04.472806+08:00
**Daily Work Briefing: Digital Product Development (Leads Ecom/Omni)**

**Key Participants & Roles**
*   **Daryl Ng:** Initiator of the discussion; referenced feedback from Ravi regarding scope.
*   **Alvin Choo:** Confirmed technical/functional alignment.
*   **Michael Bui:** Raised a query regarding project timelines.
*   **Ravi:** Provided prior feedback (referenced by Daryl).

**Main Topic**
Clarification on the implementation scope for Ticket **OMNI-1157**, specifically whether a specific requirement discussed during weekly epics applies to the new application or existing systems.

**Decisions Made**
*   **Scope Confirmation:** It was confirmed that the requirement in question should only be implemented for the **new app**. This aligns with feedback previously provided by Ravi, as noted by both Daryl Ng and Alvin Choo.

**Pending Actions & Ownership**
*   **Timeline Validation:** Michael Bui has questioned whether the targeted timeline for this task remains valid following the scope clarification.
    *   **Action Required:** Confirm current timeline status against the confirmed "new app" only scope.
    *   **Ownership:** Unassigned in chat; requires response from the team managing the ticket or project lead.

**Key Dates, Deadlines & References**
*   **Discussion Date:** March 19, 2026 (11:29 AM – 11:39 AM +08:00).
*   **Ticket Reference:** [OMNI-1157](https://ntuclink.atlassian.net/browse/OMNI-1157) (Raised during weekly epics).
*   **Space URL:** https://chat.google.com/space/AAQAN8mDauE

**Summary Status**
The scope for OMNI-1157 is confirmed as "new app only." The immediate next step is to verify if the original timeline holds true or requires adjustment given this specific constraint.


## gchat/space/AAQA-ICuJRM: BCRS ECOMM SAP POSTING
Source: gchat | Group: space/AAQA-ICuJRM | Last Activity: 2026-03-19T03:30:21.463000+00:00 | Last Updated: 2026-03-19T13:37:32.924893+08:00
**Daily Work Briefing: BCRS ECOMM SAP POSTING & Refunds UAT**

**Key Participants & Roles**
*   **Dany Jacob:** Project Lead/Coordinator.
*   **Yaxin Hao / Jianbin Huang (DBP Team):** Technical owners for SAP data processing and uploads.
*   **Hendry Tionardi / Michael Bui / Tan Gay Lee:** Finance/UAT testers verifying order postings.
*   **Onkar Bamane / Prajney Sribhashyam:** Stakeholders managing UAT validation, coordination (PSR/Data8), and environment access.
*   **Wei Fen Ching:** Accounting verification lead.
*   **Lai Shu Hui:** Requester for Blackoffice/Zendesk UAT access; currently reviewing test cases.
*   **Pazhanisamy Harish Prabhu:** IT Ops providing Zendesk sandbox credentials.
*   **Sathya Murthy Karthik:** Coordinated invoice updates and testing closure today (Mar 19).

**Main Topic**
UAT testing for BCRS E-commerce involving Sales Posting to SAP (F420) and the initiation of Refunds UAT. Focus has shifted from resolving data posting issues to finalizing test case execution, specifically validating invoice entries in the test sheet and securing necessary system access for Finance teams.

**Status of Issues**
*   **SAP Posting & Data:** Duplicate delivery issues and data8 blockages were resolved on March 6. Manual file uploads by Yaxin Hao on March 9 successfully posted test orders (e.g., 75507127, 75506869).
*   **Invoice Validation (Mar 19):** On March 19 at 10:46 AM, Sathya Murthy Karthik confirmed all invoices were added to the test sheet and requested review/markup of test cases.
*   **Access & Environment:** Lai Shu Hui requested Blackoffice UAT access and Ticket visibility. While Pazhanisamy Harish Prabhu provided Zendesk sandbox credentials (link: `fairpriceon1701663131.zendesk.com`), the user reported inability to view specific tickets initially. Requests were also made for access to the Operations Delivery Orders UAT portal (`admin-uat.fairprice.com.sg`).

**Pending Actions & Ownership**
1.  **Test Case Review:** Lai Shu Hui (and Finance Team) must review the updated test sheet containing all invoices and mark test cases accordingly to close out testing today. **(Owner: Lai Shu Hui / Finance Team)**.
2.  **System Access Resolution:** Pazhanisamy Harish Prabhu / IT Ops to troubleshoot Zendesk ticket visibility for Lai Shu Hui and grant access to the Operations Delivery Orders UAT portal (`admin-uat.fairprice.com.sg`). **(Owner: Pazhanisamy Harish Prabhu)**.
3.  **UD Code Process:** Clarify current process for requesting User Defined codes in Production following the cessation of email requests. **(Owner: Olivia - / IT Ops)**.

**Decisions Made**
*   Proceeded with manual file upload by DBP team (Yaxin Hao) for specific test orders after data8 was fixed on March 6.
*   Confirmed changes to the "face of receipt" do not impact SAP posting integrity.
*   Zendesk sandbox access initiated via password reset link; further troubleshooting required for ticket visibility within the agent interface.
*   **New:** Testing is targeting closure today (Mar 19) pending final review and marking of test cases by Lai Shu Hui.

**Key Dates & Follow-ups**
*   **Mar 5:** Initial identification of missing SnG/Pre-order postings (Orders: 75502397, 75504631).
*   **Mar 6:** Data8 issue confirmed as rectified.
*   **Mar 9:** Manual file upload completed; confirmation sent by Yaxin Hao at 12:22 PM.
*   **Mar 17:** Thread opened regarding BCRS Refunds UAT & Sign Off.
*   **Mar 18 (08:48 AM):** Lai Shu Hui requested Blackoffice/Zendesk access and Ticket visibility.
*   **Mar 18 (09:06 AM):** Pazhanisamy Harish Prabhu provided Zendesk sandbox link; user reported inability to view tickets.
*   **Mar 18 (09:53 AM):** Request made for Operations Delivery Orders UAT access (`admin-uat.fairprice.com.sg`).
*   **Mar 19 (10:12 AM):** Sathya Murthy Karthik inquired about invoice status and testing closure requirements.
*   **Mar 19 (10:46 AM):** Sathya Murthy Karthik confirmed all invoices added to the test sheet; requested final review by Lai Shu Hui.
*   **Immediate Follow-up:** Complete test case markup by Lai Shu Hui and finalize Zendesk/Operations Portal access issues to close UAT today.


## gchat/space/AAQA85dw4So: RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Last Activity: 2026-03-19T03:21:05.866000+00:00 | Last Updated: 2026-03-19T13:38:46.631987+08:00
**Daily Work Briefing: Automated Test Results Summary (RMN Notification)**

**Key Participants & Roles**
*   **Collection Runner App:** Automated testing agent executing API suites.
*   **Webhook Bot:** Reporting mechanism (consistently non-functional, returning "unable to process your request" on all notifications).
*   **Parties Involved:** No human participants engaged; system-generated notification log.

**Main Topic/Discussion**
The conversation comprises automated notifications from the Collection Runner regarding nightly and periodic API test executions across `promo-service`, `marketing-personalization-service`, and `marketing-service` in the **staging** environment. Logs track "API Tests" (functional) and "API Contract Tests." New entries cover runs on **March 19, 2026**.

**Test Execution Status & Anomalies**
*   **Stable Services:**
    *   `promo-service`: 10 API tests / 6 contract tests passed consistently across all dates with zero failures.
    *   `marketing-personalization-service`: 96 API tests / 126 contract tests passed consistently across all dates with zero failures.
*   **Persistent Failures (`marketing-service`):**
    *   Contrary to previous stabilization assumptions, `marketing-service` API tests remain intermittent. The pattern of **2 recurring failures per run** has continued through March 19.
    *   **Recurring Failures:** Observed on every run from March 17 through March 19:
        *   **Mar 17 (01:04, 03:15, 06:43 UTC):** 50–51 Passed / **2 Failed**.
        *   **Mar 18 (01:04 UTC):** 50 Passed / **2 Failed**.
        *   **Mar 19 (09:04+08:00 UTC):** 50 Passed / **2 Failed**.
    *   **Contract Tests:** `marketing-service` contract tests remain stable with 100% pass rates (20 Passed / 0 Failed) across all recent runs, including March 19.

**Pending Actions & Ownership**
*   **Investigate Persistent `marketing-service` Failures:** The root cause for the consistent 2 API test failures observed daily from March 17 through **March 19** is unaddressed. Engineering teams must review failure reports immediately.
*   **Webhook Bot Remediation:** The bot failed to process requests in every notification cycle from March 12 through at least March 19. Immediate attention is required from DevOps or Automation Infrastructure.

**Decisions Made**
*   No human decisions recorded; all entries are automated system outputs.

**Key Dates & Deadlines**
*   **Failure Window (Historical):** March 12 and March 13 showed earlier instability.
*   **Current Failure Window:** The service has been failing consistently since **March 17, 2026**, continuing through **March 19, 2026**.
*   **Monitoring Period:** Data covers runs from **March 12, 2026**, through **March 19, 2026**.
*   **Next Steps:** Immediate investigation into the `marketing-service` API flakiness (2 failures/run) and Webhook Bot connectivity issues.


## gchat/space/AAQAgT-LpYY/fN7jxS6RotE: BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/fN7jxS6RotE | Last Activity: 2026-03-19T02:53:49.779000+00:00 | Last Updated: 2026-03-19T13:38:59.240164+08:00
**Daily Work Briefing: BCRS Firefighting Group**

**1. Key Participants & Roles**
*   **Prajney Sribhashyam:** Inquiry lead; responsible for confirming UAT readiness and risk management.
*   **De Wei Tey:** Technical confirmation owner; responsible for delivery status updates and identifying risks.

**2. Main Topic**
Verification of User Acceptance Testing (UAT) readiness specifically for the "SnG refunds" feature, ensuring alignment with the operational calendar to avoid holiday conflicts.

**3. Decisions Made**
*   The UAT release date was adjusted from **23 March 2026** to **24 March 2026**.
*   This change was made because **23 March** is a public holiday, rendering the original deadline operationally unsuitable.

**4. Pending Actions & Ownership**
*   **Action:** Identify and communicate any potential risks regarding the new schedule.
    *   **Owner:** De Wei Tey
    *   **Status:** Committed ("Sure i will"). No further details on specific risks provided in this thread yet.

**5. Key Dates & Deadlines**
*   **Original Target Date:** 23 March 2026 (Confirmed as a holiday).
*   **Revised UAT Readiness Deadline:** 24 March 2026.
*   **Discussion Timestamp:** 19 March 2026, 10:52 AM – 10:53 AM (SST+8).

**Summary of Discussion Flow**
On 19 March, Prajney Sribhashyam inquired about UAT readiness for SnG refunds by 23 March. De Wei Tey initially confirmed readiness for that date. Upon noting that 23 March is a holiday, Prajney prompted for an alternative; De Wei Tey immediately proposed shifting the target to 24 March. Prajney concluded the thread by requesting a risk call-out if any issues arise, which De Wei Tey acknowledged.

**Reference Resources**
*   **Group:** BCRS Firefighting Group
*   **Chat URL:** https://chat.google.com/space/AAQAgT-LpYY


## gchat/space/AAAAs0DTvmA: [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Last Activity: 2026-03-19T02:40:22.291000+00:00 | Last Updated: 2026-03-19T13:39:59.701362+08:00
**Daily Work Briefing: [Prod Support] Marketplace**

**Key Participants & Roles**
*   **Support/Operations:** Willie Tan, Iris Chang, Lalita Phichagonakasit, Charlene Tan, Jie Yi Tan, Ayton See.
*   **Technical/Admin Team:** Dang Hung Cuong, Shiva Kumar Yalagunda Bas (Frequent recipients of access/access issues), Olivia -, Amos Lam, Jill Ong, Greta Lee, Zaw Myo Htet, Angella Yeo, Cassandra Thoi.

**Main Topics & Discussion Summary**
The conversation covers critical operational blockers regarding seller onboarding, order fulfillment discrepancies, system configuration errors, and recent customer-facing listing failures. Major themes include:
1.  **Access Management:** Multiple requests to grant "PickerApp" access for new or existing sellers (Meat Affair, Old Shanghai, BulkMartGo, PETS STATION HOLDING). Charlene Tan reported a new seller (Woah Group) encountering errors under the "Offers" section.
2.  **Sales Data & Reporting:** Issues with vendors (CoLab Apac, Old Shanghai) not receiving sales breakdown reports since inception.
3.  **Promotion & Pricing Conflicts:**
    *   Conflicting promotions for "Falcon Galaxy Strong Garbage Bag" requiring one to be disabled.
    *   Incorrect backend promotion configuration causing frontend stuck states (Ayton See).
    *   Urgent case: A promotion expired in Mirakl but remains active on the front end, risking financial loss (Jill Ong).
    *   Discount prices not showing despite SKU publication.
4.  **Fulfillment & System Errors:**
    *   Delivery slot display discrepancy for seller "Funa" (Mirakl shows 91h vs Frontend date) reported previously; now updated to a specific window duration issue on Mar 19.
    *   Missing items in PickerApp compared to email picklists (Atasco Dairy, Estalife).
    *   Orders completed without delivery by NJV (Order #246974265, #248270820).
    *   Seller description/image updates not triggering "Pending Verification" status.
5.  **New Listing & Logic Queries:**
    *   **Item Visibility:** Lalita Phichagonakasit reported SKU **13226899** failing to appear under postal code **762115** since March 14th, despite prior online availability.
    *   **Picklist Logic:** Amos Lam raised a query regarding picklist generation for postponed orders (e.g., shifting from March 3rd to March 15th) and whether the system adjusts accordingly.
6.  **SAP Configuration Inquiry:** Iris Chang queried the definition and data source of "Lead Time" within SAP T-code ZMP_VENDOR on Mar 18, seeking clarification on field extraction (Dang Hung Cuong, Amos Lam, Jill Ong cc'd).

**Pending Actions & Ownership**
*   **Close DF SOF Order:** Willie Tan requested closure; tracking via DST-2578 (Owners: Dang Hung Cuong, Shiva Kumar Yalagunda Bas).
*   **Vendor Report Issues:** Investigate missing sales breakdown reports for CoLab Apac (NED-277148) and Old Shanghai (NED-277329).
*   **Access Grants:** Grant PickerApp access to Meat Affair (tianying@tlfood.com.sg), BulkMartGo, PETS STATION HOLDING, and others.
*   **Promotion Resolution:** Disable conflicting promotion for Falcon Galaxy Bags; urgently disable stuck backend promotion per Jill Ong. Investigate Woah Group "Offers" error (Charlene Tan).
*   **Fulfillment Investigation:** Check why Estalife missing Final Picklist PFC; investigate delivery slot display for Funa Artistic Hampers & Gifts (Current focus: Window shows 4 days vs expected 2 days); determine trigger for NJV non-delivery completions (Orders #246974265, #248270820).
*   **System Logic & Listing Fixes:**
    *   Investigate missing SKU 13226899 listing for postcode 762115.
    *   Clarify picklist generation logic for postponed orders (Amos Lam query to Dang Hung Cuong, Shiva Kumar Yalagunda Bas).
    *   Resolve SAP ZMP_VENDOR Lead Time definition and data source question raised by Iris Chang (Dang Hung Cuong/Amos Lam ownership implied).

**Decisions Made**
*   None explicitly stated as final decisions; most items are requests for technical investigation or approval. Ayton See decided to educate a seller on promotion setup rules after identifying a configuration error. Dang Hung Cuong is currently addressing the Woah Group offers error, the postponed order logic query, and the SAP Lead Time inquiry.

**Key Dates & Deadlines**
*   **2026-03-03:** DF SOF order request raised.
*   **2026-03-18 (Yesterday):** Iris Chang inquired about SAP T-code ZMP_VENDOR "Lead Time" definition; 8 replies generated.
*   **2026-03-19 (Today/Recent):** Jie Yi Tan reported Funa Artistic Hampers & Gifts delivery window discrepancy (4 days vs 2 days expected); discussion ongoing with 34 replies and last update 24 minutes ago.
*   **Historical Context:** Previous dates regarding NJV orders, Estalife picklists, and SKU visibility remain relevant to the active investigation list.


## gchat/space/AAAA8dv5lp0: fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Last Activity: 2026-03-19T02:39:45.338000+00:00 | Last Updated: 2026-03-19T13:40:31.414818+08:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
The conversation comprises automated Datadog alerts for the production environment (`env:prod`). Instability in Mirakl integration has extended from March 17 through mid-day on March 18, and resumed on March 19. Additionally, a recurring latency spike was detected in the `picklist-pregenerator` service on the night of March 17 and again early morning March 19. All new alerts triggered today (March 19) were automatically recovered.

**Incident Summary & Timeline (2026-03-15 to 2026-03-19)**
*   **Service:** `fni-order-create` (Mirakl Integration) – **Recurring Pattern Continuation**
    *   **Cycle D (Mar 18, 08:46):** Triggered at 08:46:39 UTC. Recovered by 08:51:50 UTC (~5 mins).
    *   **Cycle E (Mar 18, 13:02):** Triggered at 13:02:39 UTC. Recovered by 13:09:49 UTC (~7 mins).
    *   **Cycle F (Mar 19, 01:38):** Triggered at 09:38:39 UTC (Local Time) with "Exception Occurred At Mirakl Route" and "Error while calling APIs." Both alerts recovered by 09:43:40 UTC (~5 mins duration).
    *   **Note:** This confirms a persistent recurrence of Mirakl integration failures across March 17, 18, and 19.

*   **Service:** `seller` (`picklist-pregenerator`) – **Recurring Latency**
    *   **Cycle (Mar 17, 23:01):** Triggered with P2 warning (3604.897s duration). Recovered subsequently.
    *   **Cycle F (Mar 19, 07:01):** Triggered at 07:01:23 UTC (Local Time) with P2 warning regarding completion time. Metric value: 3605.054s. Status recovered by subsequent monitoring cycles.

*   **Service:** `fni-offer`
    *   Historical incidents from March 15–17 remain noted. No new events reported in the current window.

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of expanded Mirakl integration instability affecting `fni-order-create`. The pattern now includes three distinct recurrence windows across three consecutive days (Mar 17, 18, and 19), involving DBP route failures and persistent order-fetching issues.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Investigate the root cause of extreme latency spikes in `picklist-pregenerator`. A cycle occurred on March 17 (3604s) and a near-identical spike was recorded on March 19 at 07:01 UTC (3605.054s).
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Review Monitor `29851723` logic for Apple Pay/Google Pay transactions following the March 16 spike (historical context) and resolve the test alert triggered on March 19 at 07:04 UTC regarding Google Pay metrics.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Key Dates & Follow-ups**
*   **Active Period:** March 15–19, 2026.
*   **Critical Deadlines:** Immediate investigation required due to the continuous recurrence of Mirakl errors and high-latency events in `picklist-pregenerator` spanning four days.

**Summary for Leadership**
Mirakl integration instability has persisted and intensified across March 17, 18, and 19. On March 19 (09:38 UTC), the system triggered "Exception Occurred At Mirakl Route" and "Error while calling APIs," resolving within 5 minutes. Simultaneously, `picklist-pregenerator` exhibited a critical performance anomaly on March 19 at 07:01 UTC with a completion time of 3605.054 seconds, mirroring the severity of the March 17 event (3604s). These recurring patterns suggest systemic issues within the data pipeline and job processing logic requiring urgent engineering review.


## gchat/space/AAQAaCRlnFQ: @omni-ops #standup - Mar 19
Source: gchat | Group: space/AAQAaCRlnFQ | Last Activity: 2026-03-19T02:02:26.108000+00:00 | Last Updated: 2026-03-19T13:40:41.357460+08:00
**Daily Work Briefing: #standup Channel Update**

**Key Participants & Roles**
*   **Yangyu Wang**: Initiated the standup discussion. (Role inferred: Team member/Lead initiating daily sync).
*   **Channel Audience**: 7 of 8 members viewed the message, indicating broad awareness within the `#standup` channel and the broader @omni-ops resource group.

**Main Topic/Discussion**
The sole recorded interaction is a prompt to commence or initiate the daily standup meeting. No specific project updates, blockers, or status reports were exchanged in this log snippet. The conversation consists entirely of the query "standup?", suggesting the session was just beginning or attendance was being confirmed.

**Pending Actions & Ownership**
*   **Initiate Standup**: Action to begin the meeting is pending.
    *   **Owner**: Yangyu Wang (based on who initiated the call).
    *   **Status**: Awaiting response from other team members to proceed with full participation or agenda setting.

**Decisions Made**
No formal decisions were recorded in this conversation segment due to the lack of substantive discussion beyond the initiation prompt.

**Key Dates, Deadlines, & Follow-ups**
*   **Date/Time**: March 19, 2026, at 10:02 AM (UTC+8).
*   **Context**: Daily standup scheduled for this time slot.
*   **Follow-up**: Next step is the actual completion of the standup round-robin or status sharing, which was not captured in the provided text.

**Summary Note**
This log represents only a single initiating message from Yangyu Wang to start the daily sync on March 19, 2026. The conversation ended immediately after the query with no further updates reported in this dataset.


## gchat/space/AAQAR16KXqc: Product x RMN x Platform
Source: gchat | Group: space/AAQAR16KXqc | Last Activity: 2026-03-19T02:00:12.056000+00:00 | Last Updated: 2026-03-19T13:41:00.981585+08:00
**Daily Work Briefing: Product x RMN x Platform**

**Key Participants**
*   **Christopher Yong:** Product/Business Lead (seeking in-store data to close Nestle deal).
*   **Rajiv Kumar Singh:** Ad Operations/Strategy.
*   **Sanjana Sanjana:** Analytics/Measurement (GA tracking for sponsored vs. organic impressions).
*   **Nikhil Grover:** Product Engineering (in-store data lead).
*   **Vivian Lim Yu Qian:** Data Science/Ecom Search Lead.
*   **Ravi Goel:** Source of FPG app user data and in-store transaction breakdowns.

**Main Topics Discussed**
1.  **In-Store Data Requirements (Nestle Deal):** Christopher Yong requested the average percentage breakdown of DCC (Direct-to-Consumer) vs. non-DCC in-store payments to validate measurable data scale for Nestle.
    *   **Initial Response:** On March 19, Ravi Goel provided December 2025 GMV data, noting ~41% of grocery business GMV was checked out via app/digital loyalty.
    *   **Current Status:** Christopher Yong noted that <50% DCC activity is not advantageous for the pitch. He has requested a deeper dive into transaction-level data to find more flattering metrics for Nestle engagement.
2.  **Banner UX Standardization:** Nikhil Grover proposed standardizing banner auto-scroll timers from 5 to 3 seconds. Approved pending beta testing with CTR variance within 10% of baseline.
3.  **Ecom Search Analysis:** Post-launch review showed stable RMN revenue (~$300/week uplift) but no significant new customer acquisition or conversion uplift despite increased search traffic.

**Decisions Made**
*   **Banner Timer Change:** Standardization to a 3-second auto-scroll timer approved, conditional on successful beta testing (CTR within 10% of baseline).
*   **Data Analysis Direction:** Christopher Yong directed Ravi Goel and Nikhil Grover to investigate transaction-level data more deeply rather than relying solely on GMV percentages.

**Pending Actions & Ownership**
*   **Deep-Dive Data Analysis:** Ravi Goel and Nikhil Grover must analyze transaction-level data to identify a higher percentage of DCC activity that can be presented to the Nestle brand team.
*   **Provide User Metrics:** Christopher Yong still awaits weekly/monthly active FPG app user data from Ravi.
*   **Monitor Banner Beta Performance:** Product team to track impressions and CTR during the phased rollout (currently 20% on March 16–19; scaling to 50% by March 19). Proceed only if CTR variance stays within 10% of baseline.
*   **GA Tracking Implementation:** Sanjana Sanjana to finalize tracking for Sponsored vs. Organic Product Impressions.

**Key Dates & Deadlines**
*   **March 16 (Mon):** Banner beta test began on iOS v7.24.0 and Android v7.22.1; Ecom Search rollout scheduled for Android.
*   **March 16–19:** Banner phased rollout at 20% user volume.
*   **March 19:** Banner scale-up to 50% of users. (Note: In-store data inquiry occurred during this phase).
*   **March 23:** Banner full (100%) rollout scheduled.


## gchat/space/AAAAjDYVcBU: FPG Everyone - General
Source: gchat | Group: space/AAAAjDYVcBU | Last Activity: 2026-03-19T01:44:24.863000+00:00 | Last Updated: 2026-03-19T13:41:26.774616+08:00
**Daily Work Briefing: FPG Everyone Chat Summary (Updated)**
**Date Range:** March 3 – March 19, 2026
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

### Main Topics
1.  **Digital Access Rollout:** Schedule confirmed: Live (Facilities/Tech); Mar 16 (C-suite/HR/Finance); Mar 23 (Customer/Marketing/E-Commerce); Mar 30 (Remaining Hub staff). User guide distributed.
2.  **Media Collaboration – "Bowl of Love":** FairPrice launched a microdrama with Mediacorp featuring fresh pork from Malaysia, focusing on Mdm Gao and porridge.
    *   **Trailer:** Live on FB, IG, and TikTok.
    *   **Episodes:** Dropping March 20–21, 2026, on @mediacorp.re.dian TikTok.
    *   **Cast:** Tyler Tennn, Tasha Low, Xiang Yun.
3.  **Sensory Testing Panels:**
    *   **Frozen Snacks:** Evaluation scheduled for March 18 & 19, 2026 (3 slots). Limited to 40 panelists. Mobile device submission required.
    *   **Chapati:** Screening form remains open.
    *   **Frozen Processed Food/Nuts:** Session status pending confirmation of overlap with Frozen Snacks dates.
4.  **Wellness Campaign – World Oral Health Day:** Ariel Yap promoted daily oral care routines ahead of the occasion. Featured products include Euthymol Whitening Purple Corrector Toothpaste, Curatick Oral Wound & Ulcer Patch, Dentalpro Interdental Brush Assorted, and Sensodyne Repair & Protect Toothpaste.
    *   **Offer Link:** https://go.fpg.sg/HABAFPG_WK3

### Pending Actions & Ownership
*   **Sensory Test Sign-ups (Owner: All Staff):**
    *   **Frozen Snacks Evaluation:** Register immediately for March 18 or 19 via `https://tinyurl.com/HQSEC`. Select tabs "SEC 18.03.2026" or "SEC 19.03.2026".
    *   **Chapati Recruitment:** Complete screening form (`https://forms.gle/DFYrahZcvhtcoJ9R7`).
*   **Wellness Engagement (Owner: All Staff):**
    *   Visit nearest Unity store for recommended oral care essentials.
    *   Explore deals at https://go.fpg.sg/HABAFPG_WK3.
*   **Social Engagement:** Watch trailer and share "Bowl of Love" content on social channels before the March 20–21 episode drop.

### Critical Dates & Deadlines
*   **March 6:** End of Foaming Hand Soap offer (Completed).
*   **March 8:** International Women's Day Celebration (Completed).
*   **March 12:** Non-Halal Soup Sensory Evaluation (Completed).
*   **March 16–30:** Cardless access rollout phases.
*   **March 17:** Frozen Food/Nuts session (Status: Pending confirmation/overshadowed).
*   **March 18–19 (Wed & Thu):** Frozen Snacks Sensory Evaluation.
*   **March 20–21:** "Bowl of Love" episodes drop on TikTok.
*   **March 22:** FairPrice Walnuts with Cranberries redemption ends.

### Decisions Made
*   No formal strategic decisions recorded; focus remains on correcting Cardless Access communication, recruiting panelists for Frozen Snacks/Chapati testing, promoting the "Bowl of Love" microdrama collaboration, and supporting World Oral Health Day wellness initiatives via Unity stores.


## gchat/space/AAAAnlKPglA: #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Last Activity: 2026-03-19T01:37:23.221000+00:00 | Last Updated: 2026-03-19T13:41:50.135854+08:00
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

**Resolved Incident (New):**
*   **Mar 19 (Morning):** Incident `story_key`: `10aaf170-dac2-5fec-97bf-cfd442f8706b`.
    *   **Triggered:** Mar 18, 22:14 UTC.
    *   **Recovered:** Mar 19, 03:37 UTC (approx., based on alert timestamp 09:37+08:00).
    *   **Status:** **Resolved**.
    *   **Duration:** ~5.6 hours (slightly above the historical average of ~4 hours).

**Current Status:** All alerts resolved. No active incidents pending recovery.

### Pending Actions & Ownership
*   **Immediate Action:** None required at this time; the Mar 18/19 incident has successfully recovered.
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Investigation Note:** The recent incident duration (~5.6 hours) exceeded the ~4-hour historical average. While resolved, continued observation is recommended given the frequency of triggers on consecutive days (Mar 17–19).

### Decisions Made
*   None recorded. The conversation reflects system state transitions only.

### Key Dates & Follow-ups
*   **Latest Event:** March 19, 2026, at ~03:37 UTC (Recovery confirmed).
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Maintain routine monitoring. No escalation required for the resolved incident unless frequency increases or resolution times consistently exceed averages.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Datadog Monitor Link:** [View in Datadog](https://app.datadoghq.eu/monitors/17447511)
*   **Resolved Incident Link (Mar 18/19):** https://app.datadoghq.eu/monitors/17447511?group=story_key%3A10aaf170-dac2-5fec-97bf-cfd442f8706b&from_ts=1773883251000&to_ts=1773884451000&event_id=8550027906224008084
*   **Recovered Incident Link (Mar 17):** https://app.datadoghq.eu/monitors/17447511?group=story_key%3Ae40567bb-115b-5b81-be58-09d665e5969f

### Monitor Configuration
*   **Query:** `events("source:watchdog (story_category:infrastructure -story_type:(tcp_retrans_jump OR full_disk_forecast)) env:(PROD OR production OR prod)").rollup("count").by("story_key").last("30m") > 0`


## gchat/space/AAQAP-kMoqY: 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Last Activity: 2026-03-19T00:03:09.293000+00:00 | Last Updated: 2026-03-19T13:42:16.747547+08:00
**Daily Work Briefing Summary (Updated: March 19, 2026)**

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
*   **Inbox Status:** As of March 19, 2026, the workspace inbox is fully caught up across all categories (Urgent Action Items, Project Themes, Meeting Updates, and FYI). No pending unread items require immediate attention.

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


## gchat/space/AAAAx50IkHw: Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw | Last Activity: 2026-03-18T12:22:26.402000+00:00 | Last Updated: 2026-03-18T22:37:50.842992+00:00
**Daily Work Briefing: Digital Product Development (DPD)**

**Key Participants & Roles**
*   **Flora Wo Ke:** Team Lead (Project Status, Incident Response).
*   **Alvin Choo:** Developer/QA (Feature Release, Payment Services).
*   **Nicholas Tan:** DevOps/Infrastructure (Golden Pipeline, Container Risks).
*   **Tiong Siong Tee / Andin Eswarlal Rajesh:** QA/Engineering (iOS Bug Reporting).
*   **Winson Lim:** Engineering Lead/Strategy (Disaster Recovery Scenarios, UX Trends).
*   **Natalya Kosenko:** DevOps/SRE (Datadog Infrastructure as Code Governance).
*   **Boning He / Gopalakrishna Dhulipati:** Team Members (Social/Culture).
*   **Kyle Nguyen:** Team Member (Event Coordination).
*   **Maou Sheng Lee:** Team Member.

**Main Topics & Discussions**
1.  **Infrastructure & Operations Risk:** Nicholas Tan flagged an operational risk regarding Broadcom ending free Bitnami images, causing `kubectl` image tag failures and increased Time To Recovery (TTR) during service resuscitation. The issue impacts the Golden Pipeline (GP).
2.  **Payment Service Issues:** Alvin Choo reported that promo codes failed to redeem in FP Pay. Later confirmed that a change freeze has ended and feature releases are proceeding.
3.  **Mobile Quality Assurance:** Andin Eswarlal Rajesh identified a bug on iOS FPPay where QR codes load correctly without user login. The issue was escalated via file download.
4.  **Datadog Governance:** Natalya Kosenko reported unauthorized manual changes to Datadog On-Call teams (removals of Maxine, Arijit, Minu). She emphasized that Terraform manages this config; manual console edits are overwritten on the next run.
5.  **Strategic Planning:** Winson Lim highlighted data centers as potential targets in modern warfare (Iran conflict context) to inform Disaster Recovery (DR) scenarios.
6.  **Social Events & Sentiment:** Kyle Nguyen announced an upcoming DPD BBQ with the sentiment "We come first." Wai Ching Chan responded positively, tagging Vincent Wei Teck Lim regarding event details. Maou Sheng Lee expressed a sentiment of feeling like energy is being wasted on March 18.
7.  **Social Notes:** Boning He and Gopalakrishna Dhulipati shared snacks (Chinese cookies with chicken gizzard/medicinal barley and Indian cookies) in pantry areas.

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

**Social Notes**
*   Boning He and Gopalakrishna Dhulipati shared snacks in pantry areas.
*   Upcoming DPD BBQ announced by Kyle Nguyen ("We come first, see you!").


## gchat/space/AAQAgT-LpYY/K3BvO-zFaHE: BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/K3BvO-zFaHE | Last Activity: 2026-03-18T10:39:40.482000+00:00 | Last Updated: 2026-03-18T22:39:12.631066+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Sathya Murthy Karthik:** Requester; initiated the inquiry regarding user access.
*   **Sneha Parab:** Investigator; verified user status within the DBP UAT environment.
*   **Prajney Sribhashyam:** Proposer of alternative solution; managing stakeholder follow-up.
*   **Hanafi Yakub:** Tagged for assistance and context regarding the proposed workaround.

**Main Topic**
Verification of database access rights for `shu_hui.lai@fairpricegroup.sg` in the DBP UAT environment and determining the fastest method to achieve the required workflow.

**Key Discussion Points**
*   Sathya Murthy Karthik requested confirmation of whether Shu Hui Lai has existing access to DBP UAT.
*   Sneha Parab confirmed that the user account could not be found in the DBP UAT system.
*   Sathya sought assistance to provision this access immediately.
*   Prajney Sribhashyam noted that creating a new account is time-consuming and proposed an alternative workflow: adding invoices directly to a sheet instead of relying on DBP UAT access.

**Decisions Made**
*   **Process Change:** The team agreed that manually adding invoices to a sheet is more efficient than provisioning a new user account for Shu Hui Lai due to the time constraints associated with account creation.

**Pending Actions & Ownership**
1.  **Follow-up with Stakeholder:** Prajney Sribhashyam is following up directly with Shu Hui Lai (`shu_hui.lai@fairpricegroup.sg`) regarding the alternative solution (adding invoices to a sheet).
    *   *Owner:* Prajney Sribhashyam

**Key Dates & References**
*   **Date:** 2026-03-18
*   **Timeframe:** Discussion occurred between 10:17 and 10:39 (UTC+0).
*   **Target User:** `shu_hui.lai@fairpricegroup.sg`
*   **System:** DBP UAT
*   **Group Channel:** BCRS Firefighting Group (URL: https://chat.google.com/space/AAQAgT-LpYY)


## gchat/space/AAQACfHCuNI: BCRS - UAT
Source: gchat | Group: space/AAQACfHCuNI | Last Activity: 2026-03-18T10:25:00.437000+00:00 | Last Updated: 2026-03-18T22:40:38.750183+00:00
**BCRS UAT Daily Briefing Summary (Updated: 18 Mar 2026)**

**Key Participants & Roles**
*   **Sathya Murthy Karthik:** UAT Lead/Coordinator (Provided status update as of 18 Mar).
*   **Danielle Lee:** Previously inquired about technical live date and production release status.
*   **Prajney Sribhashyam:** Tagged regarding live date confirmation.
*   **Finance Team:** Currently testing; numbers to be updated.
*   **S&G Team:** Developing Returns & Refunds functionality.

**Main Topic**
Progress tracking on OG Returns & Refunds, In-store Pre-order, CS Testing, and Finance Testing as of 18 Mar 2026 at 6:25 PM. Clarification provided on S&G development status and upcoming sign-off timelines.

**Pending Actions & Owners**
*   **Returns & Refunds (OG):** Manual cancellation after delivery test cases require retesting. Owner: Testing Team.
*   **In-store Pre-order:** Most test cases pending retest following clarification and bug fixes. Owner: Sathya Murthy Karthik / Testing Team.
*   **Finance Testing:** Testing is underway; numbers to be updated in the test sheet. Owner: Finance Team.
*   **S&G Development:** Ongoing development for Returns & Refunds.

**Decisions Made & Clarifications**
*   **Sign-off Timeline:** Sign-off for OG returns and refunds is planned for 19 Mar 2026 (tomorrow).
*   **CS Testing Updates:** Manual cancellation case status changed to pending; re-delivery case remains failed.
*   **Production Status:** Previous query regarding production release timing (Feature Flag off since 9 Mar) remains noted in history, though current focus is on UAT execution and S&G development.

**Status Snapshot (as of 18 Mar, 6:25 PM)**
*   **OG Returns & Refunds:** Testing underway. Sign-off scheduled for tomorrow.
    *   *Note:* In-store pre-order testing also currently underway.
*   **CS Testing:**
    *   **Passed:** 17
    *   **Pending:** 1 (Manual cancellation)
    *   **Failed:** 1 (Re-delivery)
*   **Finance Testing:** Underway. Numbers to be updated in test sheet.
*   **In-store Pre-order:** Most cases pending retest after clarification and bug fixes; specific pass/fail/pending counts to be updated.

**Key Dates & Deadlines**
*   **9 Mar 2026:** Feature Flag turned off for production.
*   **17 Mar 2026:** Previous status reporting date (context only).
*   **18 Mar 2026:** Current status reporting date.
*   **19 Mar 2026:** Planned sign-off for OG returns and refunds.


## gchat/space/AAAAS7vPcKs: QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs | Last Activity: 2026-03-18T09:54:33.288000+00:00 | Last Updated: 2026-03-18T22:42:28.333804+00:00
**Daily Work Briefing: QE <-> All Tribes** (Updated)

**Key Participants & Roles**
*   **Patrick Thun:** Lead/Coordination.
*   **Madhuri Nalamothu:** QA Lead/Test Execution.
*   **Milind Badame:** QA Engineer.
*   **Hang Chawin Tan:** DevOps/Backend Support.
*   **Daryl Ng / Michael Bui:** Dev/Product.
*   **Others:** Dany Jacob, Piraba Nagkeeran, Yangyu Wang, Andin Eswarlal Rajesh.

**Main Topics & Discussion**
1.  **LinkPoints Test Failure (New):** Tests remain disabled in regression due to the LinkPoints fix status update is pending. Milind Badame and Michael Bui are awaiting ETA on the resolution. *Status:* Blocked waiting for dev update.
2.  **Postal Code Offer Label Missing (New):** Milind Badame reported a missing `label` attribute for the first product in "TestHasOffer swimlane" for Postal code **098619**. Requires investigation.
3.  **QC Food Tile Removal Testing:** Daryl Ng confirmed testing is underway on the removal of QC (O2O) food tiles on the Omni home page.
4.  **Load Testing & Environment Stability:** Small-scale load test completed on **5 Mar, 11 AM–1 PM** (UAT LEAP env). Scale-down operations executed successfully.
5.  **DC Membership Logic Discrepancy:** Critical inconsistency where users have `DC member` flags in back office but lack active plans/UI awards. *Status:* Investigation ongoing regarding award logic and payment errors for new DC trial members.
6.  **E2E Test Failures & UI Defects:**
    *   **Cart Page:** Broken alignment on the third highlighted product; unidentified "view buttons" require clarification (Refs: Andin Eswarlal Rajesh).
    *   **iOS/Navigation:** Disappearing swimlanes, EVoucher errors, Express delivery label changes ("Get in 1Hr"), and 1-hour filter chip failures.

**Pending Actions & Ownership**
*   **LinkPoints Fix Status:** Provide ETA for the LinkPoints fix to re-enable tests. *Owner: Dev Team / Michael Bui.* (High Priority).
*   **Postal Code Label Debug:** Investigate missing `label` for Postal code 098619 in TestHasOffer swimlane. *Owner: Milind Badame / Dev Team.*
*   **SonarCloud Fix:** Change `invoice-service` New Code baseline from "Specific version" to "Previous version". *Owner: Hang Chawin Tan / Project Admins.*
*   **Cart Page UI & Payment Issues:** Resolve Cart alignment, view buttons, and payment failures for new DC trial members. *Owners: Milind Badame, Andin Eswarlal Rajesh, Madhuri Nalamothu, Dev Team.*
*   **QC Removal Testing:** Monitor progress of QC (O2O) food tile removal on Omni home. *Owner: Daryl Ng / QA Team.*

**Decisions Made**
*   Ad slot changes proceed; known test impacts acknowledged.
*   No decision yet on LinkPoints fix or Cart view buttons; awaiting dev clarification.

**Key Dates & Deadlines**
*   **5 Mar:** Load testing window (completed).
*   **16 Mar:** DC membership logic discrepancy logged.
*   **17 Mar:** UI defects reported on cart page (06:23–06:33 AM).
*   **Today (18 Mar):** LinkPoints fix ETA required; Postal code 098619 issue flagged.


## gchat/space/AAAA1BqTEzo: Digital Signage - Network and StoreTech
Source: gchat | Group: space/AAAA1BqTEzo | Last Activity: 2026-03-18T08:40:00.545000+00:00 | Last Updated: 2026-03-18T22:44:09.082980+00:00
**Daily Work Briefing: Digital Signage Network Support**

**Key Participants & Roles**
*   **Daryl Ng:** Requester (Service Desk Ticket Owner).
*   **Steven Ng Teck Leong:** Technical Support/Network Administrator.

**Main Topic**
Provisioning network connectivity (IP address) for a digital signage TV associated with Service Desk ticket **NED-195890**. The discussion focuses on determining the connection method (Wired vs. Wi-Fi) to assign appropriate network credentials and security configurations.

**Decisions Made**
*   **Wired Connection:** If the device connects via Ethernet, it must be assigned an IP within the range **10.19.77.66–10.19.77.78**, with a Subnet Mask of **255.255.255.240** and Gateway at **10.19.77.65**.
*   **Wi-Fi Connection:** If the device connects via Wi-Fi, static IP assignment is insufficient; the MAC address must be whitelisted before connectivity can be established.

**Pending Actions & Ownership**
*   **Action:** Determine the connection type (Wired or Wi-Fi) for the TV and provide necessary credentials (IP details or MAC address).
    *   **Owner:** Daryl Ng (to confirm with the site/user).
    *   **Context:** The specific IP cannot be finalized until the connection method is confirmed. If Wi-Fi, Steven requires the MAC address to proceed with whitelisting.

**Key Dates & References**
*   **Date of Conversation:** March 18, 2026 (Timeline: 08:31 – 08:40 UTC).
*   **Ticket Reference:** [NED-195890](https://ntucenterprise.atlassian.net/servicedesk/customer/portal/8/NED-195890?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0Z3QiOiJhbm9ueW1vdXMtbGluayIsInFzaCI6IjViOThmMWY0MWUwZmZmNjI3NTliZjBjZTE2OGI1ZmRkNTE1MWY1NWFmY2NlMTVhYjI2MmJiY2I1ZWIxZGEwMWYiLCJpc3MiOiJzZXJ2aWNlZGVzay1qd3QtdG9rZW4taXNzdWVyIiwiY29udGV4dCI6eyJ1c2VyIjoiMTA2MDUiLCJpc3N1ZSI6Ik5FRC0xOTU4OTAifSwiZXhwIjoxNzc2MjE0MzgzLCJpYXQiOjE3NzM3OTUxODN9.lVNBoVHVpF4WMA1KrZH_5yMV1o-Ruw77n_9mCSWJCgI)
*   **Next Follow-up:** Daryl Ng to reply regarding the connection method or provide the MAC address if Wi-Fi is required.


## gchat/space/AAQAh7WXRkE: Alvin, Winson
Source: gchat | Group: space/AAQAh7WXRkE | Last Activity: 2026-03-18T08:00:42.568000+00:00 | Last Updated: 2026-03-18T22:48:43.049185+00:00
**Daily Work Briefing: Google Chat Summary**
**Resource:** Alvin, Winson
**Date:** March 18, 2026

**Key Participants & Roles**
*   **Alvin Choo:** Participant; scheduled to arrive late and join the discussion later.
*   **Winson Lim:** Participant; initiating the session independently due to Alvin's delay.

**Main Topic**
Coordination of a meeting or presentation involving "Michael," specifically regarding strategic planning for the year 2026 onwards. The discussion focused on scheduling adjustments to accommodate Alvin's late arrival and Winson's early departure.

**Decisions Made**
1.  **Meeting Start:** Winson Lim will commence the session immediately without waiting for Alvin Choo.
2.  **Presentation Handover:** Alvin Choo is designated to join later specifically to provide Michael with a view of "2026 onwards."

**Pending Actions & Ownership**
*   **Action:** Join the meeting later to present 2026+ details to Michael.
    *   **Owner:** Alvin Choo (Confirmed via: "okay thanks!")
*   **Action:** Conduct initial portion of the session/meeting prior to Alvin's arrival.
    *   **Owner:** Winson Lim

**Key Dates, Deadlines & Follow-ups**
*   **Meeting Date:** Tuesday, March 18, 2026.
*   **Start Time:** Approximately 07:56 UTC (Winson started).
*   **Deadline/Departure:** 4:30 PM (Local time implied) – Winson Lim must leave by this time.
*   **Next Step:** Alvin Choo to join the session after the initial start time but before the 4:30 PM deadline to deliver his specific segment to Michael.

**Metadata Reference**
*   Chat URL: https://chat.google.com/space/AAQAh7WXRkE


## gchat/space/AAAAS7vPcKs/I2HUUWoIMDY: QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs/I2HUUWoIMDY | Last Activity: 2026-03-18T07:01:49.417000+00:00 | Last Updated: 2026-03-18T22:49:32.402607+00:00
**Daily Work Briefing: QE <-> All Tribes**

**Participants & Roles**
*   **Milind Badame:** QA/Test Lead (Reporting defects, validating fixes).
*   **Michael Bui:** Development/Engineering (Investigating issues, applying fixes).

**Main Topic**
Resolution of a labeling defect in the "TestHasOffer" swimlane for Postal Code `098619`, specifically regarding a missing "Ad" label on the first product.

**Key Issues & Findings**
*   **Defect Identified:** Milind reported that for postal code `098619`, the first product in the TestHasOffer swimlane was incorrectly missing the "Ad" label.
*   **Fix Applied:** Michael confirmed a hotfix was deployed to ensure the first product is now labeled as "add" (Ad).

**Pending Actions & Ownership**
*   **Action:** Re-run test cases for postal code `098619`.
    *   **Owner:** Milind Badame.
    *   **Status:** Initiated immediately upon fix confirmation.
*   **Action:** Notify the team once User Acceptance Testing (UAT) is completed to confirm test success.
    *   **Owner:** Michael Bui.

**Decisions Made**
*   **Immediate Fix:** Engineering proceeded with updating the data/label for the first product immediately rather than waiting for a scheduled release cycle.
*   **Timeline Management:** The team agreed to wait until next week for any broader UAT cycles or long-term updates, though Michael will proactively communicate if significant changes occur over an extended period.

**Dates & Deadlines**
*   **Issue Reported:** March 18, 2026, at 05:24 UTC.
*   **Fix Confirmed:** March 18, 2026, at 07:01 UTC.
*   **Next Follow-up:** Post-UAT completion (Date TBD; team to wait until next week for formal closure).

**References**
*   Meeting/Room Link: `https://chat.google.com/room/AAAAS7vPcKs/YgGvvuD2Ow8/YgGvvuD2Ow8?cls=10`


## gchat/dm/4Ut7xcAAAAE: Yangyu Wang
Source: gchat | Group: dm/4Ut7xcAAAAE | Last Activity: 2026-03-18T07:00:06.516000+00:00 | Last Updated: 2026-03-18T22:49:47.986890+00:00
**Daily Work Briefing: Prod Deployment Discussion**

**Key Participants & Roles**
*   **Yangyu Wang:** Initiator/Deployer (Requesting approval, executing deployment).
*   **Michael Bui:** Approver/Monitor (Validating safety, offering oversight during deployment).

**Main Topic**
Discussion regarding the safety and scheduling of a production deployment for "express order" changes. The conversation centers on risk mitigation due to an unavailability feature flag.

**Decisions Made**
*   **Safety Approval:** Michael Bui confirmed the changes are safe for production. Because the specific feature flag is unavailable, the system will automatically fallback to default slots (1, 3).
*   **Deployment Timing:** The deployment window was agreed upon for approximately **2:30 PM**.

**Actions & Ownership**
*   **Pending Action:** Monitor the deployment closely.
    *   **Owner:** Michael Bui
    *   **Trigger:** Requires a ping from Yangyu Wang immediately prior to the PRD deployment start.
*   **Completed Action:** Initiated deployment.
    *   **Owner:** Yangyu Wang
    *   **Status:** Confirmed at 06:59:28 UTC on 2026-03-18.

**Key Dates, Deadlines & Timeline**
*   **2026-03-18 | 03:30 AM - 03:32 AM:** Initial discussion regarding safety and timing.
*   **Target Deployment Time:** Approx. **2:30 PM** (Local time implied by context).
*   **Prod Testing Deadline:** **5:00 PM** following the deployment window.
*   **Deployment Execution:** Started at **06:59:28 UTC** (Note: This timestamp differs from the planned 2:30 PM local estimate, suggesting a timezone offset or schedule adjustment).
*   **Confirmation Noted:** Michael Bui acknowledged the start at **07:00:06 UTC**.

**Summary of Event Flow**
Yangyu Wang initiated the conversation asking for deployment safety confirmation prior to an afternoon test. Michael Bui approved the move, citing a safe fallback mechanism (default slots 1,3) due to the missing feature flag and requested pre-deployment notification for monitoring. Yangyu confirmed the target time (2:30 PM) with a subsequent test at 5:00 PM. Following this agreement, Yangyu executed the deployment at 06:59:28 UTC on March 18, 2026, which Michael Bui acknowledged one minute later. No further actions are currently pending.


## gchat/space/AAQAgT-LpYY/rpB8hFkpx_c: BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/rpB8hFkpx_c | Last Activity: 2026-03-18T06:48:54.954000+00:00 | Last Updated: 2026-03-18T22:50:05.307951+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Shiva Kumar Yalagunda Bas:** Initiated investigation; troubleshooting lead.
*   **Hendry Tionardi:** SAP technical analysis (database queries).
*   **Onkar Bamane:** Identified root cause and applied fix.
*   **Chee Hoe Leong, Gautam Singh:** Tagged for initial awareness/verification.

**Main Topic**
Investigation into a data integrity issue where the `depositSKU` was missing from the SAP response for specific product configurations (Scheme: BCRS, Quantity Unit of Measure: 4), despite successful message publishing.

**Technical Details & Root Cause**
*   **Affected SKU:** `90175783`.
*   **Configuration Parameters:** `"Zzscheme":"BCRS"`, `"Zzqtybuom":"4"`.
*   **Diagnosis:** Hendry Tionardi executed a SAP query (`zbcrs_deposku`) confirming no record existed for `zzqtybuom = 4` with scheme BCRS. The system returned "no record."
*   **Root Cause:** Onkar Bamane confirmed that the missing configuration entry was removed earlier for testing purposes and had not been restored to production.

**Decisions Made**
*   No issue was found with the Pub/Sub publishing mechanism; the failure was purely data-related due to missing master data in SAP.
*   The team agreed to restore the missing record rather than investigate further into message processing logic.

**Pending Actions & Owners**
*   **Action:** Restore the removed `depositSKU` configuration for `zzqtybuom = 4`.
    *   **Owner:** Onkar Bamane (stated intent: "let me put it and confirm").
*   **Verification:** Confirm that the issue is resolved after the data restoration.
    *   **Owner:** Shiva Kumar Yalagunda Bas (implied requirement to verify).

**Key Dates & Follow-ups**
*   **Date:** 2026-03-18 (Session time: 06:17 – 06:49 UTC).
*   **Immediate Follow-up:** Onkar Bamane to update the database record and provide confirmation of success.
*   **Status Update:** Shiva Kumar Bas noted ("Pls ignore") once the root cause was identified, indicating no further action is required on the Pub/Sub side pending Onkar's confirmation.

**Reference Links**
*   Chat Space: https://chat.google.com/space/AAQAgT-LpYY
*   Attachment: `scratch_204.json` (Request payload).


## gchat/space/AAAAtxQjB7c: #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Last Activity: 2026-03-18T04:03:56.808000+00:00 | Last Updated: 2026-03-18T22:51:05.572528+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Mar 18, 04:03 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-discovery`.
*   **Escalations:** `@hangouts-GT-Search-DatadogAlerts`, `@oncall-dpd-staff-excellence-pdm`.
*   **Service Teams:** DPD Grocery Discovery (`team:dpd-grocery-discovery`), Search Indexing (`service:fp-search-indexer`), Product Data Management (`team:dpd-staff-excellence-pdm`).

**Main Topic**
**CRITICAL ALERT:** The `fp-search-indexer` service has transitioned from stable to a **P2 Error State** on the production environment. While previous volatility in `sku-store-attribute` and transient issues in `qc-layout-service` were noted, immediate attention is now required for the Search Indexer due to 100% unavailability of error tolerance.

**Pending Actions & Ownership**
*   **Action:** **URGENT INVESTIGATION:** Address errors on `fp-search-indexer` (env: prod).
    *   **Owner:** Product Data Management On-Call (`@oncall-dpd-staff-excellence-pdm`) & Search Team.
    *   **Status:** Alert triggered at **Mar 18, 04:03 UTC**. Metric `trace.http.request.errors` exceeded 0.0 (Value: 1.0) in the last minute.
    *   **Required Checks:**
        1.  Review Datadog logs for `fp-search-indexer`.
        2.  Inspect K8s deployment (`fpon-cluster/default/fp-search-indexer` in asia-southeast1).
        3.  Consult Support Runbook (Jira SR-2001831558).
    *   **Context:** This contradicts prior status where the service was stable; immediate manual intervention is now mandatory.

*   **Action:** Investigate chronic low file processing counts for `sku-store-attribute`.
    *   **Owner:** DPD Grocery Discovery Team (`@hangouts-dd-dpd-grocery-alert`).
    *   **Status:** Job remains unstable with high-frequency flapping. Recent cycles: Mar 17, 22:07–00:02 UTC; Mar 18, 00:35–01:01 UTC. Pattern suggests intermittent dependency issues requiring log review.

*   **Action:** Monitor `sku-global-attribute` error rates.
    *   **Owner:** Product Data Management Team (`@opsgenie-dpd-grocery-discovery`).
    *   **Status:** Alert triggered Mar 17, 03:02 UTC (92% error rate); recovered by 03:30 UTC. Verification of batch processing logic recommended.

**Decisions Made**
*   Automated monitoring detected a critical failure in `fp-search-indexer` at 04:03 UTC; no prior resolution exists for this specific P2 event. The previous "resolved" status for this service is now superseded by the active error condition.

**Key Dates & Follow-ups (Mar 16–18, 2026)**
*   **Service: `fp-search-indexer` (P2 - Product Data Management) [ACTIVE CRITICAL]**
    *   *Issue:* `trace.http.request.errors` > 0 on prod.
    *   *Timeline:* Triggered **Mar 18, 04:03 UTC**.
    *   *Metric:* Value 1.0 over last 1m.
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/17447691) | [K8s Console](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/fp-search-indexer/overview) | [Runbook](https://ntuclink.atlassian.net/wiki/spaces/SR/pages/2001831558/Support+Run+book).
*   **Service: `sku-store-attribute` (P3 - Grocery Discovery)**
    *   *Pattern:* Recurring "Low Processed Files" (<6 files in 5h).
    *   *Latest Activity:* Triggered/Recovered cycle on **Mar 17, 22:07–00:02 UTC** and **Mar 18, 00:35–01:01 UTC**. Monitor ID: `20382848`.
*   **Service: `qc-layout-service` (P3 - Product Data Management)**
    *   *Issue:* Success rate dropped below 99.9% for PLP requests.
    *   *Timeline:* Triggered **Mar 17, 02:48 UTC** (66.66%); Recovered **02:58 UTC**. Monitor ID: `20382951`.
*   **Service: `sku-global-attribute` (P3 - Product Data Management)**
    *   *Issue:* High error rate in batch processing.
    *   *Timeline:* Triggered **Mar 17, 03:02 UTC** (92.0%); Recovered **03:30 UTC**. Monitor ID: `91573503`.

**Summary of Critical Issues**
1.  **P2 Search Indexer Failure:** Immediate attention required for `fp-search-indexer` errors on prod as of Mar 18, 04:03 UTC.
2.  **Flapping SKU Jobs:** The `sku-store-attribute` job shows a concerning pattern of short-lived failures.
3.  **Transient PLP Failure:** Brief drop in success rate for `qc-layout-service` on Mar 17 morning (resolved).

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c


## gchat/space/AAQA-bdVPoA: Jacob, Sathya, Daryl, Tiong Siong, ...
Source: gchat | Group: space/AAQA-bdVPoA | Last Activity: 2026-03-18T04:00:26.997000+00:00 | Last Updated: 2026-03-18T22:51:25.361763+00:00
**Daily Work Briefing: Project Light Leave Planning (Updated)**

**Key Participants & Roles**
*   **Sathya Murthy Karthik:** Requester/Owner of the "Omni Leave Plans" spreadsheet; driving data collection.
*   **Michael Bui, Daryl Ng, Tiong Siong Tee, Akash Gupta:** Team members requested to submit leave plans.

**Main Topic**
Collection of individual leave plans extending through October 2026. While a central Google Sheet was established for long-term tracking, team feedback indicates that accurate planning beyond one month is difficult due to standard travel booking cycles (1–1.5 months in advance).

**Pending Actions & Ownership**
*   **Action:** Input all known leave dates into the "Omni Leave Plans" spreadsheet.
    *   **Scope Nuance:** Akash Gupta has noted that planning beyond one month is not feasible for him currently; he will update plans 1–1.5 months prior to travel.
*   **Owner:** All tagged team members (**Michael Bui, Daryl Ng, Tiong Siong Tee, Akash Gupta**).
*   **Status Update:**
    *   **Akash Gupta:** Initially required access (granted by Sathya). Confirmed no major leave plans for the next month. Stated inability to commit to a full October 2026 schedule due to planning horizons; will provide updates closer to dates.
    *   **Michael Bui:** Confirmed leave for late March (~1 week).
    *   **Daryl Ng:** Provided initial coverage dates (Reservist duties on 30 March PM; 22–30 April) but noted long-term plans are unavailable. Committed to securing team coverage during absences.
    *   **Tiong Siong Tee:** Confirmed no long-term leave plan yet, pending update on specific leaves.

**Decisions Made**
*   A centralized Google Sheet has been designated as the single source of truth for Project Light leave planning.
*   **Revised Expectation:** While Sathya requested data "till Oct," participants (specifically Akash) have clarified that accurate input is limited to ~1 month in advance, with long-term dates being tentative or unavailable.

**Key Dates & Deadlines**
*   **March 18, 2026:** Initial deadline for known leave plans.
    *   **Access Confirmed:** Akash Gupta provided access at 03:53 UTC on this date.
*   **Future Coverage Data:**
    *   **Next Month (April 2026):** No major leaves confirmed by Akash.
    *   Late March (~1 week): Michael Bui's confirmed leave.
    *   March 30 (PM): Daryl Ng's reservist duty.
    *   April 22–30: Daryl Ng's reservist duty.

**Reference**
*   **Document:** Omni Leave Plans (Project Light)
*   **Link:** https://docs.google.com/spreadsheets/d/1BuohjrUTREwWgj_4JNLUnu4d2c-a4VPEPWrvJJks_eo/edit?gid=0#gid=0


## gchat/space/AAAAnyFGr84: PDM Notification
Source: gchat | Group: space/AAAAnyFGr84 | Last Activity: 2026-03-18T03:57:43.330000+00:00 | Last Updated: 2026-03-18T22:51:35.669592+00:00
**Daily Work Briefing: PDM Notification Summary**

**Key Participants & Roles**
*   **Gchat Notification / API Bot (Collection Runner):** Automated system generating test reports.
*   **Webhook Bot:** System component responsible for processing requests; currently operational failure.

**Main Topic**
Automated API contract and functional tests for the `gt-catalogue-service` in the Staging environment failed to execute due to a backend processing error. No actual test cases were run or evaluated.

**Pending Actions & Ownership**
*   **Action:** Investigate why the "Webhook Bot is unable to process your request" error occurred for both API Contract and API Tests.
*   **Owner:** Engineering/DevOps Team (implied ownership of the notification pipeline).
*   **Context:** Two separate test suites (`[API Contract Tests]` and `[API Tests]`) returned zero requests, zero passed, and zero failed results because execution was blocked before completion.

**Decisions Made**
None recorded in this conversation; all outcomes indicate system failure rather than business decisions.

**Key Dates & Follow-ups**
*   **Date:** March 18, 2026 (03:57 UTC).
*   **Environment:** Staging.
*   **Service:** `gt-catalogue-service`.
*   **Immediate Follow-up Required:** Review the notification pipeline to ensure the Webhook Bot is functional before re-running tests on the Collection Runner.

**Status Summary**
The automated run summary indicates a critical failure in the test execution pipeline itself, not the service being tested. Both reports show 0 total requests due to the webhook bot's inability to process the trigger. No manual intervention or code changes were discussed; this requires technical troubleshooting of the CI/CD notification mechanism.


## gchat/space/AAAAde_cYKA: [Prod Support] Ecom FFS Ops
Source: gchat | Group: space/AAAAde_cYKA | Last Activity: 2026-03-18T03:36:00.064000+00:00 | Last Updated: 2026-03-18T22:52:03.522368+00:00
**Daily Work Briefing: [Prod Support] Ecom FFS Ops**

**Key Participants & Roles**
*   **Wai Ching Chan / Sampada Shukla:** Operations/Product Leads (investigating packlist discrepancies and managing app releases).
*   **TL HCBP FFS, TL - HGPT FFS, TLEPT FFS, Harry Akbar Ali Munir:** Store/Regional Team Leads reporting operational blockers.
*   **Adrian Yap Chye Soon:** Technical Lead/Support (reviewing app release candidates and packlist validation).

**Main Topics**
1.  **Packlist Discrepancies & Validation:** Ongoing investigation into orders where `packed_qty` significantly exceeds `delivered_qty`.
    *   **New Incident (Mar 18):** Order #22828448 at Hyper Hougang (Store ID 212) shows a critical mismatch: `packed_qty` of 11,570,930 vs. `delivered_qty` of 7. Reported by Harry Akbar Ali Munir on Mar 18 at 03:36 UTC.
    *   **Ongoing Focus:** Hyper Sports Hub (HSPH), Orchid Country Club (OCCL), and Hyper Parkway (HPWP).
2.  **Inventory System Glitches:** Reports of Store SOH showing 0 while IC app shows stock, missing "Last SOH" on reports, and pagination failures in the T18 order list.
3.  **Picker App Release:** Preparation for rolling out version 10.4.0 to address authentication loops (OE-3518) and performance improvements.

**Pending Actions & Ownership**
*   **Critical Order Validation (New):**
    *   *TL - HGPT FFS:* Investigate order #2282848 at Hyper Houngang (Store ID 212). Discrepancy: `packed_qty` (11,570,930) vs. `delivered_qty` (7). Date: Mar 18.
    *   *Adrian Yap Chye Soon:* Review packlist status NULL issue for order #22789688 (Orchid Country Club, Mar 14).
*   **Order Validation (Packlist Discrepancies):**
    *   *TL HSPH FFS:* Confirm packlists for orders #22738044, #22754559, #22780412.
    *   *TL OCCL2 FFS:* Double-confirm orders #22756415 and #22752129 (Mar 11).
    *   *TL HPWP FFS:* Confirm packlist for order #22786748 and investigate discrepancy in order #22781194.
*   **Technical Investigation:**
    *   *Wai Ching Chan:* Investigate "Missing pagination button" in T18 view reported by TLEPT FFS.
    *   *Adrian Yap Chye Soon:* Review IC app inventory sync issue (SOH mismatch) reported by TLEPT FFS.
*   **System Fixes:**
    *   *TL HCBP FFS:* Resolve order #256307387 stuck in "pending" status after accidental picker unassignment; verify other packlists are clean.

**Decisions Made**
*   **App Release Strategy:** Sampada Shukla to release Picker App 10.4.0 to a single store on March 10 at 1:30 PM. Full rollout is contingent on no issues reported within 2 days. Choice of the initial store was deferred for decision.

**Key Dates & Deadlines**
*   **Mar 9:** Picker App 10.4.0 release target (Single store).
*   **Mar 10 – Mar 11:** Observation window for app stability.
*   **Immediate:** Validation of specific packlist discrepancies for deliveries scheduled between Mar 10 and Mar 15, including the new Mar 18 incident at Hyper Hougang.

**Critical Alerts**
*   **New Alert (Mar 18):** Critical `packed_qty` anomaly detected in order #22828448 (Hyper Hougang), where packed quantity is orders of magnitude higher than delivered. Immediate attention required from TL - HGPT FFS.
*   Persistent issues with `packed_qty` being NULL or mismatched against delivered quantities across multiple stores (HSPH, HPWP, OCCL).
*   TLEPT FFS reports a critical UI bug preventing view of orders beyond the first 20 in the T18 fulfillment list.


## gchat/space/AAQAgT-LpYY/2-RpHBXJWBw: BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/2-RpHBXJWBw | Last Activity: 2026-03-18T03:02:57.052000+00:00 | Last Updated: 2026-03-18T03:31:25.128717+00:00
**Daily Work Briefing: BCRS Firefighting Group (BCRS Container Count Field)**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Business Lead/Stakeholder; coordinating UAT planning and requesting timelines.
*   **Sneha Parab:** Development Lead/Engineering; confirmed development completion and managing SIT.
*   **Sathya Murthy Karthik:** Stakeholder (CC'd); involved in UAT coordination.
*   **Amos:** Seller Operations representative; assigned to perform UAT on behalf of sellers.
*   **Jon Ho:** Catalog Ops representative; assigned to perform UAT.
*   **TBD:** CMs/KAMs representatives; role identified but specific individuals not yet confirmed.

**Main Topic**
Discussion regarding the implementation timeline and User Acceptance Testing (UAT) strategy for the new "BCRS container count" field in MP. The team reviewed development status, SIT completion targets, and defined UAT scope and participants.

**Pending Actions & Owners**
*   **Prepare UAT Test Cases:** Owner: Prajney Sribhashyam. Action: Draft test cases to facilitate next week's UAT.
*   **Confirm CMs/KAMs Participants:** Owner: Prajney Sribhashyam / Team. Action: Finalize specific names for Customer Management and Key Account Manager roles (currently TBD).
*   **Execute Parallel Tracking Proposal:** Owner: Sneha Parab. Action: Evaluate feasibility of starting UAT immediately to run in parallel with SIT, as requested by Prajney.

**Decisions Made**
*   **UAT Participant List:** Confirmed involvement from Seller Ops (Amos), Catalog Ops (Jon Ho), and CMs/KAMs (TBD).
*   **SIT Completion Target:** Scheduled for completion by End of Day (EOD) on March 20, 2026.

**Key Dates & Deadlines**
*   **March 18, 2026:** UAT test case preparation initiated; proposal to parallel track SIT and UAT raised.
*   **March 20, 2026 (EOD):** Deadline for System Integration Testing (SIT) completion.
*   **Next Week (Week of March 23-27):** Scheduled window for execution of UAT.

**Follow-Ups**
*   Sneha Parab to respond regarding the feasibility of parallel SIT and UAT tracks starting tomorrow.
*   Prajney Sribhashyam to finalize CMs/KAMs names and complete test case preparation ahead of next week's UAT cycle.


## gchat/space/AAQABQNOFAs: @ecom-ops #standup - Mar 18
Source: gchat | Group: space/AAQABQNOFAs | Last Activity: 2026-03-18T02:17:47.299000+00:00 | Last Updated: 2026-03-18T03:31:57.080848+00:00
**Daily Work Briefing: @ecom-ops #standup**
**Date:** March 18, 2026 (UTC)
**Channel:** Resource: @ecom-ops #standup
**Source URL:** https://chat.google.com/space/AAQABQNOFAs

### 1. Key Participants & Roles
*   **Shiva Kumar Yalagunda Bas**: Participant in the channel. Role inferred as a team member or lead initiating logistics coordination.
*   **Channel Audience**: The message was viewed by 6 of 8 total members, indicating active engagement from the broader ops team.

### 2. Main Topic/Discussion
The discussion focused on determining the attendance modality for an upcoming session or meeting. Specifically, the team is verifying whether they are connecting via a virtual platform ("online"). No other topics were introduced in this log entry.

### 3. Pending Actions & Ownership
*   **Action**: Confirm attendance modality (Online vs. In-person) and communicate final decision to all members.
*   **Owner**: Shiva Kumar Yalagunda Bas (initiator); Team consensus required from the remaining 2 members not yet recorded as viewing the message.

### 4. Decisions Made
*   **Status**: No decisions were finalized in this specific log entry. The conversation is currently in the inquiry phase to establish the meeting format.

### 5. Key Dates & Follow-ups
*   **Date of Log**: March 18, 2026 (Timestamp: 02:17:47 UTC).
*   **Follow-up Required**: Immediate confirmation regarding the "online" status is needed to proceed with logistics or agenda setting for the standup session.

**Summary Note:** This log represents a single inquiry at the start of the day's coordination. The team must resolve the attendance format query before proceeding with standard operational updates or task allocation.


## gchat/space/AAQAVIu_P4s: Banner delivery for impressions-based campaigns - Mar 18
Source: gchat | Group: space/AAQAVIu_P4s | Last Activity: 2026-03-18T02:09:51.991000+00:00 | Last Updated: 2026-03-18T03:32:10.480303+00:00
**Daily Work Briefing: Banner Delivery for Impressions-Based Campaigns**
**Date:** March 18, 2026
**Source:** Google Chat Space (Resource ID: AAQAVIu_P4s)

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator of scheduling change; likely meeting lead.
*   **Allen Umali:** Participant confirming availability.
*   **Cecilia Koo Hai Ling:** Participant requesting tool assistance (Gemini).
*   *Note: Conversation viewed by 7 of 8 space members.*

**Main Topic/Discussion**
The discussion centered on rescheduling a meeting regarding "Banner delivery for impressions-based campaigns." The conversation was brief, consisting solely of scheduling coordination and a request for AI assistance. No technical details or campaign data were discussed in this specific thread.

**Decisions Made**
*   **Meeting Time Change:** Nikhil Grover requested to start the session at 10:05 due to being slightly late. Allen Umali explicitly agreed ("ok"). The meeting time was officially set for 10:05.

**Pending Actions & Ownership**
*   **Action:** Generate or utilize "Gemini" (presumably Google's AI model) to summarize, analyze, or draft content related to the campaign topic.
    *   **Owner:** Cecilia Koo Hai Ling (Requested "can gemini this").
    *   **Status:** Pending execution by Cecilia or an assigned assistant.

**Key Dates & Deadlines**
*   **Meeting Start Time:** 10:05 (March 18, 2026).
*   **Context Date:** March 18, 2026.

**Summary of Chronology**
At 01:44 UTC on March 18, Nikhil Grover notified the group he was running late and proposed a new start time of 10:05. Allen Umali confirmed this adjustment at 01:49 UTC. Approximately 20 minutes later (02:09 UTC), Cecilia Koo Hai Ling requested to "gemini" the context, implying a need for AI processing or summarization of the campaign details.


## gchat/space/AAQAqwOWBZ4: Madhawa, Soumya, Tayza, Madhuri, ...
Source: gchat | Group: space/AAQAqwOWBZ4 | Last Activity: 2026-03-17T14:44:52.368000+00:00 | Last Updated: 2026-03-17T17:24:25.606268+00:00
**Daily Work Briefing: Google Chat Summary**

**Key Participants & Roles**
*   **Wai Ching Chan:** Reported arrival status.
*   **Sundy Yaputra:** Inquired about location details; acknowledged confirmation.
*   **Yangyu Wang:** Provided specific location clarification (Level 1, outside mall).

**Main Topic/Discussion**
The conversation focused on the immediate physical location of Wai Ching Chan upon arrival at a facility. The group clarified whether the arrival point was inside or outside the mall and identified the specific floor (Level 1).

**Actions Pending & Ownership**
*   **Pending:** None explicitly stated in this thread.
*   **Ownership:** No new action items were assigned; the discussion concluded with Sundy Yaputra thanking Yangyu Wang for the clarification.

**Decisions Made**
*   Confirmed location: Outside the mall on Level 1.
*   Confirmed status: The team member (Wai Ching Chan) has successfully arrived.

**Key Dates & Follow-ups**
*   **Date:** March 17, 2026.
*   **Time Window:** 10:03 AM – 10:12 AM UTC.
*   **Follow-up:** Immediate follow-up required to integrate the arrival status with any pre-scheduled meeting or handover plans (implied by the context of "reached" and location queries).

**Specific References**
*   **Resource List:** Madhawa, Soumya, Tayza, Madhuri.
*   **Space URL:** https://chat.google.com/space/AAQAqwOWBZ4
*   **Location Details:** Level 1, Outside the mall.


## gchat/dm/62iuUSAAAAE: Yaxin Hao
Source: gchat | Group: dm/62iuUSAAAAE | Last Activity: 2026-03-17T09:57:08.515000+00:00 | Last Updated: 2026-03-17T17:27:27.135865+00:00
**Daily Work Briefing: Google Chat Summary**

**Resource:** Yaxin Hao
**Conversation URL:** https://chat.google.com/dm/62iuUSAAAAE
**Date Range:** March 17, 2026 (09:56 – 09:57 UTC)

### Key Participants & Roles
*   **Yaxin Hao:** Initiator of the invitation/meeting request.
*   **Michael Bui:** Recipient; confirmed non-attendance due to conflicting commitments.

### Main Topic
Scheduling a physical meeting or attendance at location **"L10"**. Yaxin Hao inquired if Michael Bui would attend, and Michael responded regarding his availability for the day.

### Decisions Made
*   **Attendance Status:** Michael Bui explicitly declined the request to visit L10 on March 17, 2026.
*   **Reasoning:** Michael is currently attending an "offline event."

### Pending Actions & Ownership
*   **Current Status:** No new meeting has been scheduled based on this exchange.
*   **Ownership:** Neither participant assigned a specific follow-up action in the chat log. The topic remains pending unless rescheduled via a separate communication channel, as Michael indicated he is unavailable *today*.

### Key Dates & Deadlines
*   **Primary Date:** March 17, 2026 (Today's date of conversation).
*   **Timeframe:** Discussion occurred between 09:56 and 09:57 UTC.
*   **Follow-up Required:** None explicitly stated in the provided text.

### Summary
On March 17, 2026, Yaxin Hao initiated a brief exchange asking Michael Bui if he would come down to L10. Michael Bui declined immediately, citing a scheduled offline event as the reason for his unavailability that day. The conversation concluded with no new action items or future dates established within this specific thread.


## gchat/space/AAAAQuMQ3Bs: Omni Fairmily
Source: gchat | Group: space/AAAAQuMQ3Bs | Last Activity: 2026-03-17T08:04:44.451000+00:00 | Last Updated: 2026-03-17T17:30:05.738102+00:00
**Daily Work Briefing Summary: Omni Fairmily Space**

**Key Participants & Roles**
*   **Pauline Tan:** Announced FPG ADvantage LinkedIn launch; highlighted team's showcase at the FairPrice Partners' Excellence Awards. Acknowledged cross-functional contributors including Rajiv Kumar Singh, Christopher Yong, Wendi Koh, Karlie Sia, Allen Umali, Pamela Koh, Serene Tan Si Lin, and Neo Seng Ka.
*   **Fiona U:** Organized group lunch orders; confirmed food distribution.
*   **Christine Yap Ee Ling:** Lead for Project Light user research; coordinating participant recruitment.
*   **Jacob Yeo:** Edited previous lunch order messages (Meta-data note).

**Main Topic/Discussion**
The conversation covers three distinct activities:
1.  **Marketing & Brand Presence:** Following the official FPG ADvantage LinkedIn launch, Pauline Tan reported on the team's successful showcase of retail media solutions at the FairPrice Partners' Excellence Awards last week. Activities included presenting the "Most Outstanding Omnichannel Partner" recognition and engaging guests at the booth to demonstrate connectivity between brands and shoppers across the ecosystem.
2.  **Team Logistics:** Coordination of a group lunch order for "Heybo," including collection logistics at L12 main pantry.
3.  **User Research Recruitment:** Urgent request to recruit non-staff participants (friends/family) for usability testing on the FPG App ("Project Light").

**Pending Actions & Ownership**
*   **Social Media Engagement:** Follow, like, and share the FPG ADvantage LinkedIn page. *Owner: All Team Members.*
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
*   **Upcoming Research Sessions:** March 25–27, 2026 (Wednesday to Friday). Available slots are 12:00 PM and 1:15 PM.
*   **Confirmation Timeline:** Sriharsh or Christine will confirm booked slots within 2 working days.

**Participant Eligibility Criteria (Project Light)**
Participants must be non-FPG staff, aged 25+, fluent in English, currently use the FPG App, have ordered online grocery delivery in the past 3 months, and manage household grocery shopping. They must not have participated in a FairPrice customer interview in the last 6 months.
