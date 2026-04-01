

## [1/29] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-04-01T06:30:58.385000+00:00 | Last Updated: 2026-04-01T06:40:57.568126+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Update)**
**Date:** April 1, 2026 (Early Shift)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 820

### Key Participants & Roles
*   **System/Tool:** Datadog App (Automated Monitoring)
*   **Notification Channel:** `@hangouts-ShoppingCartNotification`
*   **Ownership Teams:** `dpd-pricing`, `dpd-pricing-cart`.

### Main Topic
Instability persists across `frontend-gateway` and `st-cart-prod`. The incident window has extended into April 1, shifting from late-afternoon volatility to a recurring cycle of latency spikes on Wish List endpoints and success rate breaches on Checkout and Cart Update operations. A P2 Error Budget Alert was triggered at 04:43 UTC due to rapid budget consumption (70.053% in 7 days).

### Incident Timeline & Actions
**Previous Context:**
*   *Extended activity from March 20 through late March 31.*
*   *March 30–31:* Checkout latency and success rate fluctuations observed between 17:55–20:10 UTC.

**New Activity (April 1, 04:18 – 06:30 UTC)**
*   **04:18–04:20 UTC:** Brief recovery on Wish List latency monitors (P99/P90).
*   **04:28–04:37 UTC:** Transient spike in `get /api/wish-list/{_id}` P99 (3.3s) followed by recovery.
*   **04:34–04:45 UTC:** Checkout success rate dipped to **99.874%** (<99.9% threshold); recovered to 99.917%.
*   **04:43 UTC:** **P2 Error Budget Alert** triggered for `slo_pricing_cart_post_checkout` (70.053% consumed).
*   **05:14–05:23 UTC:** Recurring oscillation on `put /api/product/{_id}/wish-list`. P99 reached **6.838s** (>6s threshold), with frequent triggers and recoveries on P90/P99 within a 9-minute window.
*   **06:27–06:30 UTC:** Latest breach cycle. Checkout success rate dropped to **99.889%**; `st-cart-prod` `post /cart` success rate fell to **99.75%**.

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** Error budget burning accelerates (P2 Alert). The pattern now includes a new service failure (`st-cart-prod`) alongside persistent `frontend-gateway` issues.
*   **Immediate Action Required:** Investigate the correlation between the 05:14 UTC Wish List P99 spike (6.838s) and the simultaneous Checkout/Cart success rate drops. Trace `frontend-gateway` resource utilization during the 06:27–06:30 UTC window to identify if throttling or dependency timeouts are causing the new `st-cart-prod` errors.

### Decisions Made
*   **Priority Escalation:** Status remains **"Critical Incident"**. The system exhibits a multi-service failure profile (Frontend Gateway + St-Cart-Prod) with an active Error Budget burn alarm.
*   **Focus Shift:** Priority must be split between `post /api/checkout` success rates and `put /api/product/{_id}/wish-list` latency, as both are now actively triggering monitors in the early morning shift.
*   **Metric Update:** Latest recorded Checkout P99 peak remains 20.242s (March 31); latest Wish List P99 peak is **6.838s** (April 1). Lowest success rates: Checkout **99.543%** (Mar 31) and Cart Update **99.75%** (Apr 1).

### Key Dates & Follow-ups
*   **Critical Window:** Extended activity from March 20 through at least April 1, 06:30 UTC.
*   **Follow-up:** Immediate trace correlation for the 04:18–06:30 UTC window to determine if `frontend-gateway` and `st-cart-prod` are sharing a common root cause (e.g., database lock or upstream dependency).

### References
*   **Active Monitors:** `21245701` (Wish List P99), `21245708` (Checkout Success Rate), `22710472` (Cart Update Success Rate).
*   **SLO Monitor:** `8569058961838035695` (Error Budget Alert, ID 21245791).
*   **Service Tags:** `service:frontend-gateway`, `service:st-cart-prod`, `team:dpd-pricing`.


## [2/29] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4 | Messages: 6 | Last Activity: 2026-04-01T06:29:26.566000+00:00 | Last Updated: 2026-04-01T06:41:50.895718+00:00
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
    *   **Ownership:** Alvin Choo and Gopalakrishna Dhulipati. **(Update):** Daryl Ng queried on April 1 if Tiong Siong should be included in these discussion calls.
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
*   **Call Participant Query:** April 1, 2026 (06:29 AM UTC) – Daryl Ng queried Tiong Siong Tee's inclusion in calls.


## [3/29] Offer Service Monitors Improvement - Apr 1
Source: gchat | Group: space/AAQA-iRTwV0 | Messages: 4 | Last Activity: 2026-04-01T06:19:07.381000+00:00 | Last Updated: 2026-04-01T06:42:02.613580+00:00
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


## [4/29] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/8-Q3gLE8QP8 | Messages: 31 | Last Activity: 2026-04-01T06:16:15.675000+00:00 | Last Updated: 2026-04-01T06:42:25.880000+00:00
**Daily Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Lead/Coordinator (Overseeing checklist, adoption metrics, and flag deployment).
*   **Andin Eswarlal Rajesh:** App Adoption Data (Tracking Android/iOS adoption rates).
*   **Onkar Bamane:** SKU/Data Operations (Managing BCRS SKUs, barcodes, and deposit linkages).
*   **Gautam Singh:** Technical/Database Verification (Checking DBP system records and product linkages).
*   **Sneha Parab:** Data Enrichment & Stakeholder Management (Coordinating DBA support and informing stakeholders).
*   **Daryl Ng:** App Adoption (Requested to update numbers).

**Main Topic**
Discussion focused on the status of the BCRS POS cutover, specifically:
1.  Completing data downloads and running enrichment scripts for newly created SKUs.
2.  Verifying barcode generation against total new SKUs (361 out of 837).
3.  Validating SKU creation and deposit linkages in the DBP system.
4.  Assessing app adoption metrics to determine readiness for enabling the feature flag.

**Pending Actions & Owners**
*   **Onkar Bamane:** Investigate why specific SKUs (listed below) are not created in the DBP system and confirm if data can be sent to FPON for the 361 SKUs with barcodes.
    *   *Missing SKUs to investigate:* 13280794, 13280852, 13280864, 13281403, 13281448, 13281453, 13281688, 13281689, 13281710, 13281712.
*   **Sneha Parab:** Raise a DBA Service Request (SR) for data enrichment on the affected SKUs and obtain access to the "BCRS - POS Cutover Plan.xlsx" sheet. Once completed, inform Jonathan Ho & Cheryl Ho.
*   **Gautam Singh:** Complete verification of product linkage tables and confirm unique SKU counts in DBP vs. the source sheet.
*   **Andin Eswarlal Rajesh / Daryl Ng:** Update app adoption numbers on the dashboard once the current lag resolves (currently reflecting data as of March 28).

**Decisions Made**
*   **Enrichment Strategy:** Proceed with raising a DBA SR for data enrichment before notifying stakeholders.
*   **Adoption Timeline:** Acknowledged that reaching >95% adoption typically takes ~2 months, with significant slowdown after the 85% mark.

**Key Data Points & Dates**
*   **Data Status (as of March 28):** Android adoption 75.6%; iOS adoption 86.38%.
*   **SKU Discrepancy:** Out of 837 newly created SKUs, barcodes exist for only 361. In the DBP system, unique SKUs are 361, but only 351 are present in the system and 349 have active deposit linkages.
*   **Timeline Context:** Download was scheduled for April 1, 2026 (previously noted as "yesterday" by Prajney).
*   **Action Date:** April 1, 2026 (Discussion took place between 23:16 UTC on March 31 and 06:16 UTC on April 1).


## [5/29] [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Messages: 6 | Last Activity: 2026-04-01T06:14:07.638000+00:00 | Last Updated: 2026-04-01T06:42:57.187190+00:00
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


## [6/29] ❗ Important Email
Source: gchat | Group: space/AAQAUJW8HMo | Messages: 4 | Last Activity: 2026-04-01T05:08:57.252000+00:00 | Last Updated: 2026-04-01T06:43:27.702738+00:00
**Daily Work Briefing Summary (Updated)**

**Key Participants & Roles**
*   **Michael Bui (You):** Managing Osmos support, event RSVPs, FileVault compliance, performance feedback, Project Light coordination, AI training follow-ups, and GCP Service Account security.
*   **Alvin Choo:** Organizer of the joint DPD, Core Product, and Picking Teams meeting (Apr 2).
*   **Sip Khoon Tan / FPG AI CoE:** Coordinating weekly AI guidance sessions and launching the Agentic Evolution Contest.
*   **Kyle Nguyen / Nicholas Tan:** Leading legacy GCP SA key remediation (starts week of Mar 30).

**Main Topics**
1.  **GCP Security & Service Account Decommissioning:**
    *   **Objective:** Clean up legacy keys; immediate focus on non-production (56 keys) and automated rotation.
    *   **Timeline:** Kyle Nguyen's team begins remediation week of March 30, 2026.
    *   **Action:** Review spreadsheet to indicate consent for automated key rotation.
    *   **Resources:** Legacy SAs Sheet; Working Document (Links unchanged).

2.  **AI Training & Agentic Evolution Contest:**
    *   **Weekly Support:** Google AI Specialists hosting 30-min sessions Wednesdays, 2:00–2:30 PM SGT (Mar 25 – May 31, 2026). Q&A document for March 19 session is available.
    *   **Agentic Evolution Contest:** Launched by FPG AI CoE & Google. Submissions accepted until **April 25, 2026**. Prizes include exclusive Google gear.
    *   **Action:** Submit contest entry (Role, Problem Solved, Value Created) by April 25. Submit questions via form prior to weekly sessions.

3.  **DPD, Core Product & Picking Teams Meeting:**
    *   **New Event:** Joint meeting scheduled for **Thursday, April 2, 2026, 9:30 AM – 11:00 AM SGT**.
    *   **Location:** FairPrice Hub-13-L13 Heritage Room (50) + Google Meet (`mgv-sdor-ejt`).
    *   **Organizer:** Alvin Choo.
    *   **Action:** RSVP required to confirm attendance preference.

4.  **BCRS & Project Light:**
    *   **BCRS Regroup:** Thursday, March 26, 2026, 4:00–5:00 PM SGT (Organizer: Prajney Sribhashyam).
    *   **RMN Discussion:** Rescheduled to Thursday, March 26, 2026, 2:00–3:00 PM SGT.
        *   *Conflict:* RMN (2-3 PM) overlaps with start of BCRS Regroup preparation (4 PM).

**Pending Actions & Ownership**
*   **GCP Security Consent (Michael Bui):** Immediate Action Required. Review legacy SA spreadsheet and indicate consent for automated rotation.
*   **DPD/Core Product/Picking Meeting RSVP (Michael Bui):** Respond to April 2 invitation.
*   **Agentic Evolution Contest (Michael Bui):** Submit AI agent entry by **April 25, 2026**.
*   **BCRS Regroup & RMN Meetings (Michael Bui):** Confirm attendance for March 26 sessions (4:00 PM and 2:00 PM respectively). Note the scheduling conflict.
*   **AI Weekly Sessions:** Submit questions via form prior to each Wednesday session.

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
*   **Apr 25, 2026:** Agentic Evolution Contest Submission Deadline.
*   **Mar 31, 2026:** FileVault Final Deadline.


## [7/29] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Messages: 9 | Last Activity: 2026-04-01T05:06:22.935000+00:00 | Last Updated: 2026-04-01T06:44:09.278737+00:00
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
2.  **Mar 18/19:** `10aaf170-dac2-5fec-97bf-cfd442f8706b` (~5.6h). Status: **Resolved**.
3.  **Mar 20, 2026:** `2787bcd7-d59e-58f0-961a-8f578260cd84` (~4.4h). Status: **Resolved**.
4.  **Mar 22, 2026:** `08f5624a-14f1-50e5-9a4a-7418b3602953` (~3.4h). Status: **Resolved**.
5.  **Mar 24–25, 2026:** `de0cbb14-ade3-5de2-bfab-cbddd41da779` (~3h 51m). Status: **Resolved**.
6.  **Mar 25, 2026:** `978f6328-424c-53dd-83c8-6411c3aa2158`. Recovered 12:09 UTC (~24h). Status: **Resolved**.
7.  **Mar 26, 2026:** `7b73b037-696a-5016-bca4-5c22e31b6245` (~3h 22m). Status: **Resolved**.
8.  **Mar 27, 2026:** `f5d0894a-4a42-515d-985f-d06644833529`. Recovered 17:37 UTC. Status: **Resolved**.
9.  **Mar 28–30, 2026:** Multiple P3 incidents recovered (Keys: `8874d9ed...`, `784f6ec6...`, `acd815df...`).

**Recent Sequence Update:**
*   **Mar 31, 2026:** Incident `0404fba2-a49b-51a3-a07f-1c4bb6b19362` triggered at 11:49 UTC and resolved at 15:05 UTC (~3h 16m). Status: **Resolved**.

*   **Apr 1, 2026 Sequence:**
    *   **Trigger (Story Key `c6d476e4...`):** 2026-04-01T23:27:22 UTC. Error: "Datadog is unable to process your request."
    *   **Recovery (Story Key `c6d476e4...`):** 2026-04-01T02:53:22 UTC. Duration: ~3 hours 26 minutes. Status: **[P3] Recovered**.
    *   **Trigger (Story Key `f28ed3be...`):** 2026-04-01T01:53:22 UTC. Error: "Datadog is unable to process your request."
    *   **Recovery (Story Key `f28ed3be...`):** 2026-04-01T05:06:22 UTC. Duration: ~3 hours 13 minutes. Status: **[P3] Recovered**.

*Note: Both incidents triggered on April 1st have self-resolved.*

### Pending Actions & Ownership
*   **Current Status:** All active incidents as of Apr 1, 2026 are **Resolved**.
    *   `c6d476e4-c442-588a-b897-2b40fb9b0dbc` (Recovered ~3h 26m).
    *   `f28ed3be-edbe-58c8-93f0-1324928ebb9a` (Recovered ~3h 13m).
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Action Required:** None. Both incidents resolved well within the 6-hour escalation threshold. Continue standard surveillance for new triggers.

### Decisions Made
*   **Escalation Status:** No escalation required; recent sequence of transient incidents resolved automatically.
*   **Protocol:** Standard observation protocol remains effective.

### Key Dates & Follow-ups
*   **Latest Events:** April 1, 2026 (Two distinct incidents: ~23:27 UTC and ~01:53 UTC triggers).
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Surveillance ongoing.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Datadog Monitor Link:** [View in Datadog](https://app.datadoghq.eu/monitors/17447511)
*   **Incident Logs:**
    *   Key `c6d476e4...`: https://app.datadoghq.eu/monitors/17447511?group=story_key%3Ac6d476e4-c442-588a-b897-2b40fb9b0dbc
    *   Key `f28ed3be...`: https://app.datadoghq.eu/monitors/17447511?group=story_key%3Af28ed3be-edbe-58c8-93f0-1324928ebb9a

### Monitor Configuration
*   **Query:** `events("source:watchdog (story_category:infrastructure -story_type:(tcp_retrans_jump OR full_disk_forecast)) env:(PROD OR production OR prod)").rollup("count").by("story_key").last("30m") > 0`


## [8/29] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Messages: 16 | Last Activity: 2026-04-01T05:04:15.670000+00:00 | Last Updated: 2026-04-01T06:44:37.075084+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Apr 1, 06:00 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`.
*   **Escalations:** `@oncall-dpd-staff-excellence-pdm`, `@hangouts-GT-Search-DatadogAlerts`, `@hangouts-GT-Discovery-DatadogAlerts`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Retail Media.

**Main Topic**
**P4 INCIDENTS (RESOLVED):** Recurring abnormal throughput anomalies for `marketing-service` on `env:prod`.
*   **Current Status:** Resolved at 05:04 UTC on Apr 1. No active incidents remain.
*   **Incident Timeline:**
    *   Triggered: Mar 31, 23:53 UTC (Recovered 00:47 UTC).
    *   Triggered: Apr 1, 03:54 UTC (Recovered 05:04 UTC).
*   **Monitor ID:** `17447110`.

**Resolved Incidents**
*   **`marketing-service` (Throughput):** P4 anomaly triggered at 23:53 UTC on Mar 31; recovered at 00:47 UTC.
    *   *Query:* `avg(last_4h):anomalies(sum:trace.http.request.hits{env:prod,service:marketing-service}) >= 1`.
    *   *Details:* 100% of values deviated >3 predictions over 15m.
*   **`marketing-service` (Throughput):** P4 anomaly triggered at 03:54 UTC on Apr 1; recovered at 05:04 UTC.
    *   *Query:* Same as above. Monitor ID `17447110`.
*   **`go-catalogue-service` (Latency):** P3 latency events resolved earlier in the day (19:35 & 19:56 UTC).
    *   *Links:* [Datadog](https://app.datadoghq.eu/monitors/17447976) | [Runbook](https://ntuc.atlassian.net/wiki/spaces/DIS/pages/2646212686/Catalogue+Service)
*   **`sap-job-file-plu-subscription`:** P2 PubSub backlog resolved at 21:50 UTC on Mar 31.

**Pending Actions & Ownership**
*   **Action:** **POST-INCIDENT REVIEW (`marketing-service`):** [Status: CLOSED] Two distinct throughput anomalies occurred within 6 hours (Mar 31 night, Apr 1 morning). No manual intervention recorded in logs; check if root cause analysis is needed for recurring patterns.
    *   **Owner:** Retail Media Team / Product Data Management.

**Decisions Made**
*   The `marketing-service` throughput anomalies were transient and self-resolving within ~54 minutes (Mar 31) and ~70 minutes (Apr 1).
*   The `sap-job-file-plu-subscription` backlog impacted pricing data integrity but recovered automatically; no manual restart was required.

**Key Dates & Follow-ups (Mar 31 – Apr 1, 2026)**
*   **Service: `marketing-service` (P4 - Retail Media) [RESOLVED]**
    *   *Latest Timeline:* Triggered Apr 1, 03:54 UTC; Recovered Apr 1, 05:04 UTC.
    *   *Details:* Two separate throughput anomaly events detected on `env:prod`.
    *   *Links:* [Datadog](https://app.datadoghq.eu/monitors/17447110) | [K8s](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview) | [Runbook](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book)

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c


## [9/29] QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs | Messages: 10 | Last Activity: 2026-04-01T04:40:14.849000+00:00 | Last Updated: 2026-04-01T06:45:25.072759+00:00
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
8.  **JWC & Express Delivery Timeouts (New):** On **1 Apr**, Milind Badame flagged E2E test failures due to store timings. Request raised to configure JWC and Express Delivery timings for **24x7** in UAT. *Status:* Pending advice from @Andin Eswarlal Rajesh and @Daryl Ng.
9.  **Express Delivery Service Fee Logic (New):** On **1 Apr**, Milind Badame reported service fees are not waived when the amount exceeds $30. *Status:* Awaiting investigation by @Daryl Ng.
10. **Unlimited Product API Error (New):** On **1 Apr**, Milind Badame queried behavior when calling APIs to increase counts for products set as unlimited in BackOffice. *Status:* Under review with @Wai Ching Chan and @Andin Eswarlal Rajesh.

**Pending Actions & Ownership**
*   **Pipeline Resolution:** Resolve `dp-gifting-web` pipeline error reported by @Hang Chawin Tan. *Owners:* @Madhuri Nalamothu, @Milind Badame, @Oktavianer Diharja. **(Highest Priority)**
*   **BCRS Cleanup Strategy:** Confirm feasibility of disabling BCRS swimlanes post-UAT and implement if approved. *Owners:* @Daryl Ng, @Andin Eswarlal Rajesh.
*   **System Stability Investigation:** Identify cause of widespread HTTP 500 errors on PDP/Cart/Order Placement (30 Mar). *Owner:* Dev Team / @Hang Chawin Tan.
*   **MiniGames Crash Fix:** Resolve blank screen issue on MiniGames tile for guest users/login flow. *Owner:* @Aman Saxena.
*   **DC Membership Fix:** Resolve subscription failures impacting all user segments. *Owner:* @Kadar Sharif. **(Critical)**
*   **UAT Timezone Configuration:** Configure JWC and Express Delivery timings for 24x7 to prevent test failures. *Owners:* @Andin Eswarlal Rajesh, @Daryl Ng.
*   **Service Fee Logic Fix:** Investigate why fees are not waived for orders >$30 on Express Delivery. *Owner:* @Daryl Ng.
*   **API Behavior Verification:** Clarify error handling for unlimited product count increments. *Owners:* @Wai Ching Chan, @Andin Eswarlal Rajesh.

**Decisions Made**
*   System-wide errors on 30 Mar require immediate triage; potential testing activity suspected by Milind Badame but not yet confirmed as the root cause.
*   DC Membership issue escalated to @Kadar Sharif due to scope affecting existing users.
*   MiniGames blank screen investigation assigned to @Aman Saxena.
*   E2E test failures attributed to store timings require UAT configuration adjustment (24x7).

**Key Dates & Deadlines**
*   **1 Apr:** JWC/Express timing query, Service fee logic issue, and Unlimited product API behavior raised.
*   **31 Mar (Morning):** Pipeline error reported; BCRS swimlane query raised.
*   **30 Mar (Morning/Afternoon):** System-wide 500 errors, Cart issues, 'Strong Tasty Brew' failure, MiniGames blank screen, DC membership issue confirmed.
*   **27 Mar:** LinkPoints API failure and iOS SnG Flow loading stuck.
*   **26 Mar:** Express cart service fee discrepancy.


## [10/29] RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU | Messages: 9 | Last Activity: 2026-04-01T04:38:03.171000+00:00 | Last Updated: 2026-04-01T06:45:51.125189+00:00
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


## [11/29] 📢 COM Notifications
Source: gchat | Group: space/AAAAu4WIubc | Messages: 12 | Last Activity: 2026-04-01T04:22:43.323000+00:00 | Last Updated: 2026-04-01T06:46:25.014649+00:00
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


## [12/29] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/aQBHf9eET0A | Messages: 7 | Last Activity: 2026-04-01T04:19:56.227000+00:00 | Last Updated: 2026-04-01T06:46:40.253846+00:00
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


## [13/29] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Messages: 8 | Last Activity: 2026-04-01T04:14:56.730000+00:00 | Last Updated: 2026-04-01T06:47:14.266707+00:00
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


## [14/29] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Messages: 16 | Last Activity: 2026-04-01T03:28:39.672000+00:00 | Last Updated: 2026-04-01T06:47:47.381653+00:00
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


## [15/29] RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Messages: 24 | Last Activity: 2026-04-01T03:21:06.545000+00:00 | Last Updated: 2026-04-01T06:48:10.587929+00:00
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


## [16/29] FPG Everyone - General
Source: gchat | Group: space/AAAAjDYVcBU | Messages: 4 | Last Activity: 2026-04-01T00:41:58.858000+00:00 | Last Updated: 2026-04-01T06:48:51.379665+00:00
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


## [17/29] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Messages: 2 | Last Activity: 2026-04-01T03:13:09.520000+00:00 | Last Updated: 2026-04-01T06:49:22.786908+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Sneha Parab:** Lead/Manager; coordinating cross-team support, SAP/API integration blockers.
*   **Michael Bui:** Engineering/RMN Architect; identified root cause for RMN incident and preparing UAT verification.
*   **Daryl Ng:** Investigating store network ownership and Omni Home data discrepancies. Recently engaged in chat regarding deployment status (March 31, 01:44 UTC) and new Linkpoints eligibility issue (April 1).
*   **Alvin Choo:** Leadership; addressing approval workflows for weekend deployments.
*   **Gopalakrishna Dhulipati:** On Child Care Leave until Wednesday (April 2). Will reach out individually if assistance is required to rep tasks.
*   **Others Active:** Andin Eswarlal Rajesh, Olivia, Koklin, Zaw, Ravi.

**Main Topics & Updates**
1.  **RMN Incident & Deployment Status:** Michael Bui identified the root cause and implemented a fix. Daryl Ng confirmed active inquiry regarding deployment status on March 31 (01:44 UTC). Immediate guidance remains required on weekend (Sat/Sun) deployment protocols, requiring an approval request to Hui Hui.
2.  **Linkpoints Eligibility Issue (New):** On April 1 at 03:13 UTC, Daryl Ng flagged that Wei Sing's team enabled "Linkpoints eligible" in SAP, but it remains disabled in DBP. Investigation is underway (Chat link provided).
3.  **Search Performance Drop:** Investigation continues regarding the severe 60–70% impression decline since March 18/19. The RMN root cause fix may correlate with these symptoms; release timing remains contingent on this investigation and UAT success.
4.  **Epic Lifecycle Query (DPD-710):** Sneha Parab flagged a technical live date of March 19, 2026, for the Omni ticket. Closure validation awaits Michael Bui's input given Daryl Ng's recent activity on deployment queries.
5.  **SIT Timeline & Redelivery Risk:** Discussion continues on SIT delivery feasibility before April 6/7 contingent on Knowledge Transfer (KT). Adrian remains unavailable for redeliveries between April 1–7 due to duplicate posting risks without a completed handover.
6.  **Infrastructure Compliance:** Bitnami ending free Docker images mandates migration for `sonic_raptor` and `mkp-fairnex`.

**Pending Actions & Owners**
*   **RMN Deployment Verification:** Confirm if the fix has been deployed following Daryl Ng's inquiry and proceed with UAT verification. Send approval request to Hui Hui for weekend deployment if applicable. (Owner: Michael Bui; Coordination: Alvin Choo/Hui Hui/Daryl Ng)
*   **Linkpoints Investigation:** Verify why "Linkpoints eligible" is disabled in DBP despite SAP enablement by Wei Sing's team. Follow up with Daryl Ng/Sneha Parab. (Owner: To be assigned/Wei Sing's team; Coordination: Sneha Parab/Daryl Ng)
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


## [18/29] Team Starship
Source: gchat | Group: space/AAQAX9iKYf0 | Messages: 1 | Last Activity: 2026-04-01T02:51:49.229000+00:00 | Last Updated: 2026-04-01T06:49:57.785137+00:00
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


## [19/29] DPD x Platform Engineering
Source: gchat | Group: space/AAQAcjNXKpA | Messages: 3 | Last Activity: 2026-04-01T02:37:40.979000+00:00 | Last Updated: 2026-04-01T06:50:30.713729+00:00
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


## [20/29] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/z_vFHR6ne-M | Messages: 5 | Last Activity: 2026-04-01T02:35:03.800000+00:00 | Last Updated: 2026-04-01T06:50:41.901609+00:00
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


## [21/29] DPD x DPM
Source: gchat | Group: space/AAQApzD7Im0 | Messages: 1 | Last Activity: 2026-04-01T02:33:57.348000+00:00 | Last Updated: 2026-04-01T06:51:10.348852+00:00
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


## [22/29] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/dRUQRmgzGzc | Messages: 6 | Last Activity: 2026-04-01T02:15:27.509000+00:00 | Last Updated: 2026-04-01T06:51:21.941641+00:00
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


## [23/29] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/69o051rSqd4 | Messages: 15 | Last Activity: 2026-04-01T00:59:59.910000+00:00 | Last Updated: 2026-04-01T06:51:38.489660+00:00
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


## [24/29] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Messages: 2 | Last Activity: 2026-04-01T00:03:09.167000+00:00 | Last Updated: 2026-04-01T06:52:30.919006+00:00
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


## [25/29] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY | Messages: 14 | Last Activity: 2026-03-31T23:16:10.242000+00:00 | Last Updated: 2026-04-01T06:53:28.491999+00:00
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


## [26/29] BCRS ECOMM SAP POSTING
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


## [27/29] [Prod Support] Ecom FFS Ops
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


## [28/29] BCRS Firefighting Group
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


## [29/29] Web Chapter
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
