

## gchat/dm/8oukJSAAAAE: Lester Santiago Soriano
Source: gchat | Group: dm/8oukJSAAAAE | Messages: 2 | Last Activity: 2026-03-19T14:52:25.338000+08:00 | Last Updated: 2026-03-19T14:55:40.152708+08:00
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


## gchat/space/AAAAsbHANyc: Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-03-19T14:52:22.382000+08:00 | Last Updated: 2026-03-19T14:56:07.549372+08:00
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


## gchat/space/AAQAgT-LpYY/HAKjA0njutA: BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/HAKjA0njutA | Messages: 7 | Last Activity: 2026-03-19T14:51:09.560000+08:00 | Last Updated: 2026-03-19T14:56:24.358574+08:00
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


## gchat/space/AAAAxwwNw2U: #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 16 | Last Activity: 2026-03-19T14:49:52.778000+08:00 | Last Updated: 2026-03-19T14:56:54.683174+08:00
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


## gchat/space/AAQAX9iKYf0: Team Starship
Source: gchat | Group: space/AAQAX9iKYf0 | Messages: 3 | Last Activity: 2026-03-19T14:46:28.605000+08:00 | Last Updated: 2026-03-19T14:57:20.594719+08:00
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


## gchat/space/AAQAUJW8HMo: ❗ Important Email
Source: gchat | Group: space/AAQAUJW8HMo | Messages: 8 | Last Activity: 2026-03-19T14:46:08.491000+08:00 | Last Updated: 2026-03-19T14:57:46.798511+08:00
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


## gchat/space/AAQAgT-LpYY: BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY | Messages: 9 | Last Activity: 2026-03-19T14:42:21.866000+08:00 | Last Updated: 2026-03-19T14:58:18.911781+08:00
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
Source: gchat | Group: space/AAQAHH3dAYc/OceYc-m64a4 | Last Activity: 2026-03-19T14:41:21.327000+08:00 | Last Updated: 2026-03-19T14:42:45.479313+08:00
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
Source: gchat | Group: space/AAQAXn1ocmE | Last Activity: 2026-03-19T14:29:07.057000+08:00 | Last Updated: 2026-03-19T14:43:43.911205+08:00
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
Source: gchat | Group: space/AAQAN8mDauE/ewxUvQHmSUM | Last Activity: 2026-03-19T14:11:08.484000+08:00 | Last Updated: 2026-03-19T14:22:35.681744+08:00
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
Source: gchat | Group: space/AAQAHH3dAYc | Last Activity: 2026-03-19T14:06:01.925000+08:00 | Last Updated: 2026-03-19T14:22:59.237523+08:00
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
Source: gchat | Group: dm/yHhI1sAAAAE | Last Activity: 2026-03-19T13:59:42.142000+08:00 | Last Updated: 2026-03-19T14:23:34.171944+08:00
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


## gchat/dm/t3wf6EAAAAE: Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Last Activity: 2026-03-19T13:56:18.617000+08:00 | Last Updated: 2026-03-19T14:24:34.126562+08:00
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


## gchat/space/AAAAQQGZSZU: RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU | Last Activity: 2026-03-19T13:53:30.957000+08:00 | Last Updated: 2026-03-19T14:24:53.240827+08:00
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
Source: gchat | Group: dm/7d1XKcAAAAE | Last Activity: 2026-03-19T13:48:20.013000+08:00 | Last Updated: 2026-03-19T14:25:24.600564+08:00
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
Source: gchat | Group: space/AAAAu4WIubc | Last Activity: 2026-03-19T13:45:42.708000+08:00 | Last Updated: 2026-03-19T14:25:54.699327+08:00
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
Source: gchat | Group: space/AAQA5_B3lZQ/8u4mgk65pbo | Last Activity: 2026-03-19T13:45:01.869000+08:00 | Last Updated: 2026-03-19T14:26:05.501884+08:00
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
Source: gchat | Group: space/AAAAYX-ew1s | Last Activity: 2026-03-19T13:42:25.827000+08:00 | Last Updated: 2026-03-19T14:26:35.608685+08:00
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
Source: gchat | Group: space/AAQA5_B3lZQ | Last Activity: 2026-03-19T13:27:20.198000+08:00 | Last Updated: 2026-03-19T14:26:47.652173+08:00
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
Source: gchat | Group: space/AAAAQQGZSZU/sFEfapjbCgM | Last Activity: 2026-03-19T13:21:31.244000+08:00 | Last Updated: 2026-03-19T14:27:00.701343+08:00
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
Source: gchat | Group: space/AAAAzZ3qkNU | Last Activity: 2026-03-19T12:35:07.855000+08:00 | Last Updated: 2026-03-19T13:35:11.584637+08:00
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
Source: gchat | Group: space/AAAAwg3yipA | Last Activity: 2026-03-19T12:07:59.815000+08:00 | Last Updated: 2026-03-19T13:35:34.129729+08:00
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


## gchat/space/AAQAgT-LpYY/LNq_qjvCggc: BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/LNq_qjvCggc | Last Activity: 2026-03-19T11:56:03.757000+08:00 | Last Updated: 2026-03-19T13:35:49.578778+08:00
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


## gchat/space/AAQAUbi9szY: [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Last Activity: 2026-03-19T11:52:35.801000+08:00 | Last Updated: 2026-03-19T13:36:21.779688+08:00
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


## gchat/space/AAQAcjNXKpA: DPD x Platform Engineering
Source: gchat | Group: space/AAQAcjNXKpA | Last Activity: 2026-03-19T11:47:56.300000+08:00 | Last Updated: 2026-03-19T13:36:53.224725+08:00
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
Source: gchat | Group: space/AAQAN8mDauE/KtpVSnYJ3ys | Last Activity: 2026-03-19T11:39:26.426000+08:00 | Last Updated: 2026-03-19T13:37:04.472806+08:00
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
Source: gchat | Group: space/AAQA-ICuJRM | Last Activity: 2026-03-19T11:30:21.463000+08:00 | Last Updated: 2026-03-19T13:37:32.924893+08:00
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


## gchat/space/AAQAN8mDauE: [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Last Activity: 2026-03-19T11:29:34.982000+08:00 | Last Updated: 2026-03-19T13:37:56.311773+08:00
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


## gchat/space/AAQA85dw4So: RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Last Activity: 2026-03-19T11:21:05.866000+08:00 | Last Updated: 2026-03-19T13:38:46.631987+08:00
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
Source: gchat | Group: space/AAQAgT-LpYY/fN7jxS6RotE | Last Activity: 2026-03-19T10:53:49.779000+08:00 | Last Updated: 2026-03-19T13:38:59.240164+08:00
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
