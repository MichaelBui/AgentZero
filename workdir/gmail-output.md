

## [1/26] Opsgenie Alert: [Datadog] [P2] [Warn] Service marketing-service has a high error rate on env:prod
Source: gmail | Thread: 19d48b628df6e566 | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Wed, Apr 1, 2026, 11:08 AM | Last Updated: 2026-04-01T14:01:25.146923+00:00
**Daily Work Briefing: Opsgenie Alert Thread**

**1. Key Participants & Roles**
*   **System (Opsgenie/Datadog):** Automated alert generator triggering notifications based on metric thresholds.
*   **Responders:** "DPD Staff Excellence - Retail Media" (Primary team assigned to the incident).
*   **Notified Channels/Groups:** `@hangouts-dd-dpd-grocery-alert` and `@opsgenie-dpd-grocery-retail-media`.
*   **Incident Owner:** The thread does not explicitly name an individual engineer, but ownership is assigned to the "DPD Staff Excellence - Retail Media" team.

**2. Main Topic/Request**
*   **Alert Subject:** [P2] [Warn] High error rate detected on the `marketing-service` in the production environment (`env:prod`).
*   **Trigger Condition:** The ratio of HTTP request errors to total hits exceeded 5% (`> 0.05`) over a 10-minute window.
*   **Current Status:** The alert was triggered (sent at 11:03 AM), but the actual metric value recorded at the time of notification was **0.011** (1.1%), which is below the 5% threshold, suggesting a potential transient spike or false positive that requires verification against the runbook.

**3. Pending Actions & Ownership**
*   **Action:** Investigate the `marketing-service` anomalies immediately.
*   **Required Steps:**
    1.  Review Datadog APM metrics for HTTP request resources: [Link](https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod).
    2.  Check Kubernetes deployment status in `asia-southeast1` cluster: [Link](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview?cloudshell=false&project=fponprd).
    3.  Consult the specific Runbook for remediation steps: [Link](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book).
*   **Owner:** DPD Staff Excellence - Retail Media (via `@hangouts-dd-dpd-grocery-alert` and `@opsgenie-dpd-grocery-retail-media`).

**4. Decisions Made**
*   No human decisions or resolutions were recorded in this thread. The content consists entirely of automated system notifications sent within a 5-minute window (11:03 AM, 11:05 AM, 11:08 AM).

**5. Key Dates, Deadlines, & Follow-ups**
*   **Alert Creation Time:** April 1, 2026, at 7:03:08 PM (UTC+00:00 timestamp in metadata; local notifications sent at 11:03 AM).
*   **Last Metric Update:** April 1, 2026, 11:02:06 +0000.
*   **Alert Frequency:** The system re-sent identical alert data three times (11:03, 11:05, and 11:08 AM).
*   **Monitor ID:** `17447106`.
*   **Next Step:** Immediate triage required by the Retail Media team to determine if the service stability issue is active or a monitoring artifact. No specific deadline was set by the system other than the standard P2 response SLA implied by the priority level.


## [2/26] Re: [## 112603 ##] Sev1 incident: Ad Products per response is low for PLA
Source: gmail | Thread: 19d2ead5d3ae56a5 | Labels: Inbox | Priority: None | Senders: Nikhil, Osmos | Last Date: Wed, Apr 1, 2026, 11:01 AM | Last Updated: 2026-04-01T14:01:45.718437+00:00
**Daily Work Briefing: Sev1 Incident #112603 (Final Update)**

**Key Participants & Roles**
*   **Nikhil Grover** (nikhil.grover@fairpricegroup.sg): Incident coordinator/escalation lead. Confirmed implementation of fixes on the client side.
*   **Michael Bui**: Technical subject matter expert. Provided advisory support and requested URLs for analysis.
*   **Osmos Support** (support@onlinesalesai.zohodesk.in): Support team coordinating with Engineering to verify the `pcnt` parameter configuration.

**Main Topic & Request**
The thread addresses Severity 1 incident [#112603] regarding low volume responses from Ad Products within Programmatic Local Ads (PLA). The root cause was identified as the `pcnt` parameter being set to `1`, limiting responses. Nikhil Grover implemented a fix setting `pcnt = 6`. Osmos Support and Engineering have now verified that this configuration is correctly passed for all PLA product requests.

**Pending Actions & Ownership**
*   **Action:** Monitor post-fix performance to ensure no discrepancies remain.
    *   **Owner:** Osmos Support / Nikhil Grover.
    *   **Status:** Verification complete as of April 1, 2026. No further immediate action required pending routine monitoring.

**Decisions Made & Outcomes**
*   **Root Cause Confirmed:** Low response volume was caused by the `pcnt` parameter being incorrectly set to `1`.
*   **Resolution Implemented:** Nikhil Grover confirmed on March 31, 2026, that the fix (`pcnt = 6`) was deployed effective from 3:00 PM Singapore time.
*   **Engineering Verification:** On April 1, 2026, at 11:01 AM, Osmos Support confirmed via their Engineering team that the FPG configuration update is active and `pcnt = 6` is now correctly passed for all PLA product requests.

**Key Dates & Follow-ups**
*   **Incident ID:** [#112603]
*   **Initial Escalation:** March 27, 2026, 9:43 AM (Nikhil Grover requested Michael Bui's support).
*   **Diagnostic Request:** March 31, 2026, 6:15 AM (Osmos Support requested URLs for "chocolate" and "toothpaste").
*   **Resolution Confirmation:** March 31, 2026, 7:14 AM (Nikhil Grover confirmed fix implementation).
*   **Engineering Verification:** April 1, 2026, 11:01 AM (Osmos Support verified `pcnt = 6` is correctly passed).

**Summary of Thread Chronology**
On March 27, 2026, Nikhil Grover escalated the Sev1 incident to Michael Bui due to URL access limitations hindering troubleshooting for low PLA responses. On March 31, 2026, Osmos Support requested specific ad request URLs to analyze the `pcnt` parameter. Following this, Nikhil Grover confirmed a client-side fix effective from 3:00 PM Singapore time on March 31, setting `pcnt = 6`. Finally, on April 1, 2026, at 11:01 AM, Osmos Support verified with their Engineering team that the FPG configuration update is live and `pcnt = 6` is now correctly passed for all PLA product requests. The incident has been resolved pending routine observation.


## [3/26] Re: [Bitbucket] Pull request #919: chore/omni ops monitor (ntuclink/dpd-datadog-monitoring)
Source: gmail | Thread: 19d2d6690d21cc23 | Labels: Inbox, Updates | Priority: None | Senders: Sun. | Last Date: Wed, Apr 1, 2026, 9:05 AM | Last Updated: 2026-04-01T10:01:14.524350+00:00
**Daily Work Briefing: Pull Request #919 Summary (Finalized)**

**Key Participants & Roles**
*   **Sundy Yaputra**: Author and primary contributor. Executed code changes, refactoring monitoring logic, restructuring service locations, merging branches, and coordinating review approvals within the `ntuclink/dpd-datadog-monitoring` repository.
*   **Madhawa Mallika Arachchige**: Reviewer who validated format and Terraform plans but deferred final approval pending team sign-off due to lack of prior monitor knowledge.
*   **Daryl Ng**: Final approver who granted explicit approval on April 1, 2026.

**Main Topic/Request**
The thread concerns Pull Request #919 titled "chore/omni ops monitor." The objective was to reorganize Datadog monitoring configurations for the DPD Omni-Ops team by dividing logic into SLO and monitor components, relocating services, establishing dedicated folder structures, and adding specific service definitions.

**Actions Pending & Ownership**
*   **Review/Merge**: The PR has been formally approved.
    *   *Status*: Approved.
    *   *Owner*: Daryl Ng (Action: Approval granted at 9:05 AM UTC on April 1, 2026).
*   **Monitoring Implementation & Updates**: Sundy Yaputra completed final iterations of code changes on April 1, 2026. Recent actions included dividing logic into SLOs/monitors, moving services for the DPD Omni-Ops team, copying monitors to the "omni ops folder," and adding "engage journey" and "engage compass" services.
    *   *Owner*: Sundy Yaputra (Status: Complete).

**Decisions Made**
No formal business decisions are recorded; however, two critical technical validations occurred on April 1, 2026:
1.  **Technical Validation**: Madhawa Mallika Arachchige confirmed the overall format was correct and verified that the Terraform plan was clean (Run ID: `run-6uXwa58bXjC4jSRi` via Terraform Cloud).
2.  **Approval Protocol**: Madhawa requested a primary team member approve the PR before proceeding, noting limited visibility into the specific monitors. This requirement was satisfied by Daryl Ng.
3.  **Final Approval**: Daryl Ng provided explicit approval for Pull Request #919 at 9:05 AM UTC on April 1, 2026.

**Key Dates & Follow-ups**
*   **Last Activity Date**: April 1, 2026.
*   **Timeline of Events (UTC)**:
    *   **2:16 AM – 2:47 AM**: Sundy Yaputra completed final code updates and merges.
    *   **8:13 AM**: Madhawa Mallika Arachchige commented, validating the TF plan but requesting a team approval.
    *   **9:05 AM**: Daryl Ng approved the pull request.
*   **Latest Commit ID**: `fa21787` (Add service) / `74ede15` (Merge).
*   **Next Steps**: With Daryl Ng's approval, the PR is ready for merge execution by maintainers or Sundy Yaputra. No further delays are indicated.

**Reference Data**
*   **Repository**: `ntuclink/dpd-datadog-monitoring`
*   **Pull Request ID**: #919
*   **Branch/Topic**: `chore/omni ops monitor`
*   **Previous Activity**: Significant structural updates occurred on March 26, 2026.


## [4/26] 4 strategic shifts defining security in 2026
Source: gmail | Thread: 19d4849ffb517233 | Labels: Inbox, Updates | Priority: None | Senders: Google Cloud | Last Date: Wed, Apr 1, 2026, 9:05 AM | Last Updated: 2026-04-01T10:01:28.300127+00:00
**Daily Work Briefing Summary**

**Key Participants & Roles**
*   **Sender:** Google Cloud Team (specifically the Google Threat Intelligence and Mandiant expert groups). Email: `googlecloud@google.com`.
*   **Recipient:** Michael.
*   **Context:** External vendor communication providing industry forecasting and strategic intelligence.

**Main Topic/Request**
The email announces the publication of the **"2026 Cybersecurity Forecast"** report. The primary objective is to provide Michael with actionable intelligence on four critical security trends expected to dominate the next 12–18 months:
1.  **AI Arms Race:** Adversary use of AI for rapid attacks versus the implementation of an "Agentic SOC" for defense.
2.  **Modern Extortion:** Persistent ransomware and data theft threats, including tactics to bypass multi-factor authentication (MFA).
3.  **Virtualization Frontline:** Increased targeting of core virtualization infrastructure as a critical blind spot.
4.  **Nation-State Strategies:** Long-term objectives of actors from China, Russia, North Korea, and Iran, specifically regarding supply chain attacks.

**Pending Actions & Ownership**
*   **Action:** Review the "2026 Cybersecurity Forecast" report.
*   **Owner:** Michael (Recipient).
*   **Details:** The email urges the recipient to use the provided intelligence to prioritize resources and build a more resilient defense strategy. No specific deadline for review was set in this communication.

**Decisions Made**
No internal decisions or strategic approvals were made within this thread, as it is a one-way informational broadcast from Google Cloud.

**Key Dates & Deadlines**
*   **Email Date:** April 1, 2026, 9:05 AM.
*   **Report Scope:** Covers trends for the year ahead (specifically the next 12–18 months from the report's publication).
*   **Reference ID:** Last message ID `19d4849ffb517233`.

**Specific References & Metadata**
*   **Source Entities:** Google Threat Intelligence, Mandiant.
*   **Sender Address:** `googlecloud@google.com`.
*   **Location Reference:** 70 Pasir Panjang Road, #03-71, Mapletree Business City, Singapore 117371 (Google Asia Pacific Pte. Ltd.).
*   **Labels:** Inbox, Updates.


## [5/26] Invitation: You’re Invited! The D&T Power Breakfast is Back! @ Tue Apr 28, 2026 9am - 10:30am (SGT) (Michael Bui)
Source: gmail | Thread: 19d482a1188a5541 | Labels: Inbox | Priority: None | Senders: Trina Boquiren | Last Date: Wed, Apr 1, 2026, 8:30 AM | Last Updated: 2026-04-01T10:01:42.449736+00:00
**Daily Work Briefing: D&T Power Breakfast Event**

**1. Key Participants & Roles**
*   **Organizer:** Trina Boquiren (trina.boquiren@fairpricegroup.sg) – Initiator and host of the event.
*   **Recipient/Attendee:** Michael Bui (michael.bui@fairpricegroup.sg) – Primary recipient requiring an RSVP response.
*   **Audience:** The D&T Team (FairPrice Group).

**2. Main Topic & Request**
Trina Boquiren has issued a formal invitation to the "D&T Power Breakfast," marking the return of this monthly team-building initiative. The event aims to facilitate connection, recharging, and social interaction over food. The specific request is for all D&T Team members to RSVP via the calendar invite by **24 April 2026** to assist with accurate food ordering and waste reduction.

**3. Pending Actions & Ownership**
*   **Action:** Submit an RSVP response ("Yes," "No," or "Maybe").
    *   **Owner:** Michael Bui (and other D&T team members).
    *   **Method:** Click the corresponding button on the Google Calendar invite.
*   **Action:** Confirm attendance logistics.
    *   **Owner:** All attendees.

**4. Decisions Made**
*   **Event Launch:** The "Power Breakfast" series has officially resumed after a hiatus.
*   **Future Schedule:** Moving forward, these events will be held on the **last Thursday of every month**.
*   **RSVP Deadline:** Responses are required no later than 24 April to finalize catering numbers.

**5. Key Dates & Logistics**
*   **Event Date:** Tuesday, 28 April 2026.
*   **Event Time:** 9:00 AM – 10:30 AM (SGT).
*   **RSVP Deadline:** 24 April 2026.
*   **Location:** FairPrice Hub, Level 11, Lobby B Pantry.
*   **Virtual Options:** A Google Meet link is provided for remote access (`meet.google.com/nbr-mdce-qro`) and phone dial-in details (+1 682-214-3669, PIN: 216437643).

**Summary Note:** Michael Bui needs to confirm attendance status by 24 April. The event serves as the kickoff for a recurring monthly schedule ending on the last Thursday of each month.


## [6/26] [JIRA] (DPD-838) Transition to Impression-Based Inventory & Multi-Banner Delivery
Source: gmail | Thread: 19d2e82fa82f66fe | Labels: Inbox, Updates | Priority: None | Senders: Nikh. | Last Date: Wed, Apr 1, 2026, 6:41 AM | Last Updated: 2026-04-01T10:02:04.833434+00:00
**Daily Work Briefing: JIRA (DPD-838)**

**Project Context**
*   **JIRA ID:** DPD-838
*   **Topic:** Transition to Impression-Based Inventory & Multi-Banner Delivery
*   **Category:** Ecom/Omni
*   **Status:** IN DEVELOPMENT (Updated Apr 1, 2026)
*   **Assignee:** Chee Hoe Leong
*   **Last Update:** April 1, 2026 (Chee Hoe Leong & Nikhil Grover comments)

**Key Participants**
*   **Chee Hoe Leong:** DM; Provided definitive answers to technical ambiguities and updated ticket status.
*   **Nikhil Grover:** Product Manager; Confirmed slot value constraints in reply to Chee Hoe Leong.
*   **Michael Bui:** Technical Stakeholder (Previously identified blockers).

**Main Topic & Request**
Following critical clarifications raised by Michael Bui on Mar 28, the team has received definitive responses from the DM (Chee Hoe Leong) regarding scope, logic, and system constraints. The project status has progressed from "TO BE DEFINED" to "IN DEVELOPMENT."

**Resolved Technical Ambiguities & Decisions**
1.  **Migration Scope:** Confirmed that video support is restricted to **Omni Home** and **FPPay**. Category and Search pages will remain on the legacy MPS service (No migration required).
2.  **Non-Endemic Identification:** The method uses a Boolean value explicitly labeled **"Endemic"** or **"Non-endemic"**, rather than substring matching logic.
3.  **OSMOS Capacity Limits:** Support for limits exceeding 10 `pcnt` items is expected by early April; confirmation of on-track delivery is pending Monday verification.
4.  **Position Tracking & Slot Values:**
    *   The "position" value is used to exclude multiple banners targeting the same slot (e.g., preventing duplicate 999s), not for sequencing.
    *   **Constraint:** Values are limited to integers **1–20** or empty (default).
5.  **Video Behavior:** Auto-play and auto-scroll remain **Front-End managed**. The system only defines the banner sequence. Sales policy limits videos to one per Carousel.
6.  **Failure Handling:** If no banners are configured, the API returns nothing, causing banners to collapse (managed by Ops). API unavailability results in the same output; an incident will be created for such cases.

**Pending Actions & Ownership**
*   **Action:** Confirm on-track delivery of OSMOS capacity >10 by early April.
    *   **Owner:** Chee Hoe Leong / Engineering Lead (Target: Monday).
*   **Action:** Update SOP to reflect slot logic for excluding duplicate banners and Integer 1-20 constraint.
    *   **Owner:** Development Team / Ops.

**Key Dates & Follow-ups**
*   **Last Update Timestamp:** April 1, 2026, at 02:38 PM Singapore Time (Nikhil Grover/Nikolai Chee Hoe Leong comments).
*   **Status Change:** Moved to "IN DEVELOPMENT" on Apr 1.

**Summary for Executive Review**
The DPD-838 initiative has resolved prior scope ambiguities and entered development. Key decisions confirm that only Omni Home and FPPay will adopt the new video-enabled multi-banner architecture; legacy MPS remains in place for Category/Search pages. Technical logic is now defined: non-endemic identification uses explicit Boolean labels ("Endemic"/"Non-endemic"), and slot values are integers 1–20 used to prevent duplicate renders rather than sequence ordering. OSMOS capacity expansion (>10 items) is targeted for early April pending Monday confirmation. Failure states result in banner collapse with incident creation, while media behaviors (auto-play/scroll) remain Front-End responsibilities. The ticket is now assigned to Chee Hoe Leong and marked as "IN DEVELOPMENT."


## [7/26] Michael Bui, here is your weekly update for 1 Apr
Source: gmail | Thread: 19d478fc4c185291 | Labels: Inbox, Updates | Priority: None | Senders: Jira | Last Date: Wed, Apr 1, 2026, 5:41 AM | Last Updated: 2026-04-01T06:01:55.701625+00:00
**Daily Work Briefing for Michael Bui**
**Date:** April 1, 2026
**Subject:** Weekly Jira Update (Ecom/Omni & Fulfilment Spaces)

**Key Participants & Roles**
*   **Michael Bui:** Recipient of the weekly update; involved in Ecom/Omni DPD and Fulfilment Ops Core domains.
*   **Milind Badame:** Commented on tickets DPD-715 and DPD-733 regarding E2E verification status.
*   **Prajney Sribhashyam:** Initiated a discussion/thread on ticket DPD-225 (7 days ago).
*   **Other Tagged Stakeholders in DPD-225:** Daryl Ng, Andin Eswarlal Rajesh, Sneha Parab, Shiva Kumar Yalagunda Bas, Dany Jacob, Gopalakrishna Dhulipati.

**Main Topic/Request**
The primary content is an automated weekly status report from Jira (Sent by `jira@ntuclink.atlassian.net`) highlighting recent comments on DPD tickets and three new work items assigned directly to Michael Bui within the **Ecom/Omni DPD** and **Fulfilment - Ops Core** spaces.

**Pending Actions & Ownership**
Three specific work items have been auto-assigned to **Michael Bui**:
1.  **DPD-820:** Switch weekly promotions from Publitas to Wordpress (Space: Ecom/Omni DPD).
2.  **OPCO-1902:** Test 1.1 (Space: Fulfilment - Ops Core).
3.  **OPCO-1809:** [Health] Offline Pre-order enhancement + LEAP (Space: Fulfilment - Ops Core).

*Note: Tickets DPD-715 and DPD-733 contain comments from Milind Badame regarding existing E2E tests for vertical/horizontal swimlanes verifying Ad label positions. While Michael is tagged, the immediate action appears to be awareness of current test coverage rather than a direct assignment.*

**Decisions Made**
*   No new strategic decisions were recorded in this specific thread snippet. The update confirms that E2E test coverage already exists for Ad label positions (per Milind Badame's comments).

**Key Dates, Deadlines, & Follow-ups**
*   **Update Date:** April 1, 2026 (5:41 AM timestamp on the email header; "1 day ago" and "7 days ago" relative to this date).
*   **Recent Activity:**
    *   DPD-715 & DPD-733: Commented 1 day ago.
    *   DPD-225: Discussion initiated 7 days ago.
*   **Follow-up Required:** Action is required on the three newly assigned tickets (DPD-820, OPCO-1902, OPCO-1809) by Michael Bui.

**System Metadata**
*   **Labels:** Inbox, Updates
*   **Source:** Atlassian Jira (`jira@ntuclink.atlassian.net`)
*   **Footer Address:** 341 George Street, Sydney, NSW, 2000, Australia


## [8/26] What is Next – The Agentic Evolution with Workbench
Source: gmail | Thread: 19d47719f5f0408a | Labels: Inbox | Priority: None | Senders: Sip Khoon Tan | Last Date: Wed, Apr 1, 2026, 5:08 AM | Last Updated: 2026-04-01T06:02:11.078785+00:00
**Subject:** Daily Briefing: Agentic Evolution with Workbench – Next Steps

**1. Key Participants & Roles**
*   **Sip Khoon Tan (sipkhoon_tan@fairpricegroup.sg):** Initiator/Coordinator. Leads the post-training engagement strategy and contest administration.
*   **Google AI Specialists:** Subject Matter Experts facilitating weekly sessions to guide agent building, answer questions, and explore features like Gemini Enterprise and NotebookLM.
*   **FairPrice Group Team (Attendees of 19 March session):** General participants invited to attend workshops and submit contest entries.

**2. Main Topic/Request**
To maintain momentum following the initial AI training on 19 March 2026, this communication outlines a structured follow-up plan involving weekly technical support sessions and the launch of an innovation contest ("Agentic Evolution Contest") focused on creating AI agents to reduce toil and scale departmental impact.

**3. Pending Actions & Ownership**
*   **Submit Pre-Session Questions:** All team members must submit questions via the *Question Submission Form* prior to weekly sessions to ensure preparation. (Owner: All Participants)
*   **Attend Weekly Workshops:** Participate in 30-minute Google AI Specialist sessions every Wednesday at 2:00–2:30 PM. A calendar invite has been issued. (Owner: All Participants)
*   **Submit Contest Entries:** Define an AI agent idea, including the role, problem solved, and value created. No technical build is required yet. (Owner: All Participants interested in contesting)
*   **Explore Platform:** Log in to Workbench at `work.fpg.sg` for exploration. (Owner: All Participants)

**4. Decisions Made**
*   Established a recurring Wednesday 2:00–2:30 PM slot for continuous Google AI Specialist support.
*   Confirmed the contest format prioritizes conceptual definitions over immediate technical implementation.
*   Pre-comiled Q&A from the March 19 training has been finalized and made publicly accessible via the *Q&A Document*.

**5. Key Dates & Deadlines**
*   **Ongoing Weekly:** Wednesdays, 2:00–2:30 PM (Google AI Specialist sessions).
*   **Deadline:** 25 April 2026 (Agentic Evolution Contest submission deadline).
*   **Reference Event:** Initial training session occurred on 19 March 2026.

**6. Resources & References**
*   **Q&A Document:** Contains answers to questions submitted prior to the 19 March session.
*   **Question Submission Form:** For submitting queries for upcoming weekly sessions.
*   **Contest Entry Portal:** Link provided to submit ideas.
*   **Platform URL:** `work.fpg.sg` (Workbench login).


## [9/26] Opsgenie Alert: [Datadog] [P4] [Triggered] Service marketing-service has an abnormal change in throughput on env:prod
Source: gmail | Thread: 19d4650c90bbc3a8 | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Wed, Apr 1, 2026, 3:59 AM | Last Updated: 2026-04-01T06:02:36.407634+00:00
**Daily Work Briefing: Opsgenie Alert Summary** (Updated)

**1. Key Participants & Roles**
*   **Sender:** Opsgenie Automated System (`opsgenie@opsgenie.net`).
*   **Targeted Responders/Teams:**
    *   `DPD Staff Excellence - Retail Media` (Primary ownership).
    *   `@hangouts-dd-dpd-grocery-alert` (Notification channel).
    *   `@opsgenie-dpd-grocery-retail-media` (Notification channel).
*   **System Integration:** `dpd-grocery-retail-media-eu` (Datadog source).

**2. Main Topic/Request**
*   **Alert Type:** P4 Alert triggered by Datadog anomaly detection.
*   **Affected Service:** `marketing-service` in the `prod` environment.
*   **Issue Description:** Abnormal change in throughput detected. Specifically, 100% of `sum:trace.http.request.hits{env:prod,service:marketing-service}` values exceeded 3 deviations from predicted values over a 15-minute window (Percent Anomalous: 100.0%).
*   **Status:** Active P4 alert. Last Updated: April 1, 2026, at 03:53:10 UTC. Created/Opsgenie timestamp: April 1, 2026, at 11:54:12 AM UTC (ID: `ca163ccb-ebac-48a0-89e9-d133059cd2fe-1775015652211`, TinyId: `139406`).

**3. Pending Actions & Ownership**
*   **Action:** Immediate investigation of throughput anomaly and validation of service health.
*   **Owner:** `DPD Staff Excellence - Retail Media`.
*   **Required Investigation Steps:**
    1.  Review Datadog APM metrics: [Datadog Link](https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod).
    2.  Check Kubernetes deployment status: [GCP Console Link](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview?cloudshell=false&project=fponprd).
    3.  Consult operational procedures: [Runbook Link](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book).

**4. Decisions Made**
*   No human decisions recorded; the alert remains an automated system trigger requiring immediate response per P4 protocols.

**5. Key Dates, Deadlines, & Follow-ups**
*   **Alert Last Updated:** April 1, 2026, at 03:53:10 UTC.
*   **Opsgenie Created At:** April 1, 2026, at 11:54:12 AM (UTC).
*   **Analysis Window:** Last 15 minutes prior to the last update.
*   **Monitor ID:** 17447110.
*   **Event URL:** [Datadog Monitor Event](https://app.datadoghq.eu/monitors/17447110).
*   **Snapshot Link:** Available via [Event Snapshot](https://app.datadoghq.eu/monitors/17447110?from_ts=1775014690000&to_ts=1775015890000&event_id=8569009799992849344&link_source=monitor_notif&link_monitor_id=17447110&link_event_id=8569009799992849344).
*   **Tags:** `env:prod`, `service:marketing-service`, `managed_by:datadog-sync`, `monitor`, `priority:p4`.

**Summary of Resources Referenced**
*   **Metric Graph:** Downloadable link provided in alert metadata.
*   **Source:** Datadog.
*   **Integration:** `dpd-grocery-retail-media-eu` (Datadog).


## [10/26] [Dashboard Report] Retail Media - DD Dashboard | Wed 1 Apr 11:00AM +08
Source: gmail | Thread: 19d46fd8c3c6da1b | Labels: Inbox, Updates | Priority: None | Senders: Datadog HQ | Last Date: Wed, Apr 1, 2026, 3:01 AM | Last Updated: 2026-04-01T06:02:45.283913+00:00
**Daily Work Briefing: Retail Media Dashboard Update**

**Key Participants & Roles**
*   **Sender:** Datadog HQ (`no-reply@dtdg.eu`) – Automated reporting system for Datadog Inc.
*   **Recipient:** Michael – Primary contact for dashboard monitoring and review.
*   **Organization:** Datadog Inc (HQ: New York, NY).

**Main Topic/Request**
Delivery of the "Retail Media - DD Dashboard" report containing data coverage spanning the past three days leading up to April 1, 2026. The communication serves as an automated notification for routine monitoring purposes.

**Pending Actions & Ownership**
*   **Action:** Review the attached Retail Media report (covering March 29–31, 2026).
*   **Owner:** Michael.
*   **Status:** Awaiting manual review initiated by recipient upon receipt of the email dated April 1 at 11:00 AM +08.

**Decisions Made**
No strategic decisions or approvals were made in this thread; it is a standard operational data delivery notification.

**Key Dates & Follow-ups**
*   **Report Date/Time:** Wednesday, April 1, 2026, at 11:00 AM (+08 time zone).
*   **Data Coverage Window:** The past 3 days relative to the report date (March 29–31, 2026).
*   **Follow-up Required:** None explicitly scheduled; monitoring is implied as an ongoing task.


## [11/26] Updated invitation: DPD + Core Product + Picking Team meeting + Light @ Thu Apr 2, 2026 9:30am - 11am (SGT) (Michael Bui)
Source: gmail | Thread: 19d46925b81178e3 | Labels: Inbox | Priority: None | Senders: Alvin Choo | Last Date: Wed, Apr 1, 2026, 1:04 AM | Last Updated: 2026-04-01T02:01:44.032139+00:00
**Daily Briefing: DPD + Core Product + Picking Team Meeting Update**

**1. Key Participants & Roles**
*   **Organizer:** Alvin Choo (alvin_choo@fairpricegroup.sg).
*   **Core Product Team:** Soumya Singh, Hanafi Yakub, Zaw Myo Htet, Lester Santiago Soriano, Mohammed Miran, Ecomm Product Development, Boning He, Haylee Lim, Tiong Siong Tee, Hang Chawin Tan, Aman Saxena, Jack Zin Oo Paing.
*   **DPD Team:** Michael Bui (michael.bui@fairpricegroup.sg), Daryl Ng, Harry Akbar Ali Munir, Gopalakrishna Dhulipati, Dang Hung Cuong, Andin Eswarlal Rajesh, Kadar Sharif, Varun Chauhan, Wai Ching Chan, Jonathan Tanudjaja.
*   **Additional Attendees:** Dany Jacob, Rohit Pahuja, Akash Gupta, Tayza Htoon, Piraba Nagkeeran, Gautam Singh, Sundy Yaputra, Shiva Kumar Yalagunda Bas, Sampada Shukla, Chee Hoe Leong, Sneha Parab, Yangyu Wang, Jeet Gandhi, Vibindas Mohandas.

**2. Main Topic/Request**
*   Update and confirmation of the joint meeting invitation between DPD, Core Product, and Picking Team.
*   Provision of updated access details (Google Meet link and dial-in PIN) for the scheduled session.

**3. Pending Actions & Ownership**
*   **Action:** RSVP to the meeting.
*   **Owner:** All listed guests (specifically noted for Michael Bui).
*   **Action:** Join the meeting via Google Meet or phone.
*   **Ownership:** All attendees.

**4. Decisions Made**
*   The meeting title was updated by the organizer, Alvin Choo.
*   The scheduled time and location were confirmed as follows: Thursday, April 2, 2026, from 9:30 AM to 11:00 AM (SGT).

**5. Key Dates & Logistics**
*   **Meeting Date/Time:** Thursday, April 2, 2026 | 9:30 AM – 11:00 AM (Singapore Standard Time).
*   **Location:** FairPrice Hub-13-L13 Heritage Room (50) [Google Meet].
*   **Virtual Access:**
    *   Google Meet Link: `meet.google.com/mgv-sdor-ejt`
    *   US Phone Number: +1 260-758-1044
    *   Meeting PIN: 166296012
*   **Notification Timestamp:** April 1, 2026, at 1:04 AM (SGT).

**Note:** This is an automated system notification regarding a calendar update. Recipients should verify their attendance status immediately to ensure proper representation from all three teams.


## [12/26] Invitation: DPD + Core Product + Picking Team meeting @ Thu Apr 2, 2026 9:30am - 11am (SGT) (Michael Bui)
Source: gmail | Thread: 19d4691f3863a710 | Labels: Inbox | Priority: None | Senders: Alvin Choo | Last Date: Wed, Apr 1, 2026, 1:04 AM | Last Updated: 2026-04-01T02:02:01.754160+00:00
**Daily Work Briefing: Meeting Summary**

**Meeting Overview**
*   **Event:** DPD + Core Product + Picking Team Sync
*   **Date & Time:** Thursday, April 2, 2026 | 9:30 AM – 11:00 AM (SGT)
*   **Location:** FairPrice Hub-13-L13 Heritage Room (50); Hybrid via Google Meet.
*   **Organizer:** Alvin Choo

**Key Participants & Roles**
The meeting convenes three primary functional groups:
1.  **Core Product Team:** Includes Soumya Singh, Boning He, Haylee Lim, Tiong Siong Tee, Hang Chawin Tan, Aman Saxena, Jack Zin Oo Paing, Michael Bui (reply pending), Daryl Ng, Harry Akbar Ali Munir, Gopalakrishna Dhulipati.
2.  **DPD (Delivery) Team:** Includes Dang Hung Cuong, Andin Eswarlal Rajesh, Kadar Sharif, Varun Chauhan, Wai Ching Chan, Jonathan Tanudjaja, Dany Jacob, Rohit Pahuja, Akash Gupta, Tayza Htoon, Piraba Nagkeeran, Gautam Singh, Sundy Yaputra, Shiva Kumar Yalagunda Bas, Sampada Shukla, Chee Hoe Leong, Sneha Parab, Yangyu Wang, Jeet Gandhi, Vibindas Mohandas.
3.  **Ecomm Product Development:** Ecomm Product Development (listed as a group in invitation).

**Main Topic/Request**
The primary objective is to facilitate alignment between the DPD logistics framework and Core Product capabilities regarding Picking operations. The session aims to discuss integration points, workflow efficiencies, and operational constraints across these departments.

**Pending Actions & Ownership**
*   **RSVP Confirmation:** Michael Bui (`michael.bui@fairpricegroup.sg`) is currently awaiting a response (Yes/No/Maybe). As the resource identifier suggests he may be a key point of contact, his attendance status requires immediate confirmation to finalize headcount and room logistics.
*   **Logistics Verification:** While the physical location and Google Meet link (`meet.google.com/mgv-sdor-ejt`) are confirmed by the organizer (Alvin Choo), no additional action items were explicitly assigned in this thread regarding agenda preparation or material distribution.

**Decisions Made**
No final decisions were recorded in this invitation sequence. The meeting is currently in the scheduling phase with a tentative date of April 2, 2026, set by the organizer.

**Key Dates & Follow-ups**
*   **Upcoming Deadline:** Attendance confirmation required prior to April 2, 2026.
*   **Meeting Execution:** The session is scheduled for April 2, 2026. No post-meeting follow-up dates are currently listed in the invitation metadata.

**Contact Reference**
*   **Email Link (US):** +1 260-758-1044 | PIN: 166296012


## [13/26] [RAW Overdue] Expired Risk Acceptance & Waiver Form
Source: gmail | Thread: 19d46907d49aeef1 | Labels: Inbox | Priority: None | Senders: cyberrisk.automation | Last Date: Wed, Apr 1, 2026, 1:02 AM | Last Updated: 2026-04-01T02:02:15.214605+00:00
**Daily Work Briefing: Expired Risk Acceptance & Waiver (RAW)**

**Key Participants & Roles**
*   **Cyber Risk Team:** Initiator of the reminder; responsible for reviewing remediation evidence or new forms. Contact: `cyberRisk@ntucenterprise.sg`.
*   **Technology Governance and Compliance Team:** Required to be shared the form during review/sign-off phase. Contact: `techgrc@ntucenterprise.sg`.
*   **Requestor (Entity Owner):** Responsible for raising, filling out, and obtaining approvals for the RAW form within Gsuite.

**Main Topic/Request**
Notification of an **expired Risk Acceptance & Waiver (RAW)** for the asset "Signcloud Saas User access management" under Entity: FPG-Fairprice. The underlying risk is a lack of user access management by the respective business owner.

**Pending Actions & Ownership**
*   **Riskor/Requestor:** Must determine if residual risks have been remediated.
    *   *If Remediated:* Submit evidence to `cyberRisk@ntucenterprise.sg` for closure review.
    *   *If Not Remediated:* Immediately submit a new RAW form via Gsuite/Google Docs.
*   **Requestor (Process Adherence):** Must follow specific Gsuite protocols:
    1.  Make a copy of the template to personal drive (do not download).
    2.  Complete Section A and share with `cyberRisk@ntucenterprise.sg` for pre-review.
    3.  Share the form with `techgrc@ntucenterprise.sg`.
    4.  Obtain sign-offs where full names or initials are used, accompanied by "Approved" or "Signed" comments in Google Docs.

**Decisions Made**
None recorded in this thread; the message is a procedural reminder and directive.

**Key Dates & Deadlines**
*   **Original Expiry Date:** May 15, 2025.
*   **Reminder Sent:** April 1, 2026.
*   **Deadline for Action:** Immediate (email reminders persist until a new RAW is approved).

**Specific References**
*   **RAW ID:** RAW-20240306_01-v1.0
*   **Asset Name:** Signcloud Saas User access management


## [14/26] You have no events scheduled today.
Source: gmail | Thread: 19d45b80d56a7030 | Labels: Inbox, Updates | Priority: None | Senders: Google Calendar | Last Date: Tue, Mar 31, 2026, 9:06 PM | Last Updated: 2026-03-31T22:01:24.107712+00:00
**Daily Work Briefing Summary**

**Key Participants & Roles**
*   **Michael Bui**: Recipient of the daily agenda notification (Account: `michael.bui@fairpricegroup.sg`). Role involves monitoring the "Digital Business Tech Release/Changes" calendar.
*   **Google Calendar System**: Automated sender (`calendar-notification@google.com`) providing system status updates.

**Main Topic/Request**
The email serves as an automated notification confirming that Michael Bui's calendar schedule for **Wednesday, April 1, 2026**, contains no events related to the subscribed "Digital Business Tech Release/Changes" calendar. It is an informational update rather than a request for action or discussion.

**Pending Actions & Ownership**
*   **No actions required.** The notification explicitly states there are no scheduled items for the day.
*   **Optional Maintenance**: If Michael Bui wishes to modify which calendars generate these daily agenda notifications, he must manually log in to `https://calendar.google.com/calendar/` to adjust settings. This is self-directed and not time-sensitive.

**Decisions Made**
No decisions were made or recorded in this thread. The content represents a system status check confirming an empty schedule.

**Key Dates & Follow-ups**
*   **Date of Notification**: March 31, 2026 (9:06 PM).
*   **Relevant Date for Schedule**: Wednesday, April 1, 2026.
*   **Follow-up Required**: None. The system confirms no events are scheduled for the aforementioned date.

**Metadata Reference**
*   **Message ID**: `19d45b80d56a7030`
*   **Labels**: Inbox, Updates
*   **Priority**: None assigned


## [15/26] Opsgenie Alert: [Datadog] [P2] [Warn] Service marketing-service has a high error rate on env:prod
Source: gmail | Thread: 19d44f04fe8dfbf2 | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Tue, Mar 31, 2026, 5:33 PM | Last Updated: 2026-03-31T22:01:46.913205+00:00
**Subject:** Daily Briefing: Opsgenie Alert on `marketing-service` High Error Rate (P2)

**1. Key Participants & Roles**
*   **Source System:** Opsgenie / Datadog integration (`dpd-grocery-retail-media-eu`).
*   **Notified Teams/Channels:**
    *   `@hangouts-dd-dpd-grocery-alert` (Alert Channel)
    *   `@opsgenie-dpd-grocery-retail-media` (Opsgenie Group)
    *   **Responder Group:** DPD Staff Excellence - Retail Media.

**2. Main Topic/Request**
*   Automated alert triggered regarding the **`marketing-service`** in the **`env:prod`** environment.
*   **Issue:** High error rate detected (P2 Warning).
*   **Trigger Condition:** The ratio of HTTP errors to total requests exceeded 0.05 threshold over a 10-minute window.
    *   *Query:* `sum(last_10m):( sum:trace.http.request.errors{env:prod,service:marketing-service}.as_count()/sum:trace.http.request.hits{env:prod,service:marketing-service}.as_count() ) > 0.05`
*   **Current Metric Value:** 0.045 (Note: Log indicates value is below the 0.05 threshold despite "high error rate" title; likely a flapping alert or delayed resolution state).

**3. Pending Actions & Ownership**
*   **Action Required:** Investigate root cause of elevated errors and verify service health.
*   **Ownership:** DPD Staff Excellence - Retail Media (as listed under Responders).
*   **Investigation Resources Provided:**
    1.  **Datadog APM:** [View Service Operations](https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod)
    2.  **Kubernetes Console:** [View Deployment (GCP)](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview?cloudshell=false&project=fponprd)
    3.  **Runbook:** [Marketing Service Runbook](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book)

**4. Decisions Made**
*   No manual decisions recorded in this thread; the content consists entirely of automated system notifications.

**5. Key Dates, Deadlines & Follow-ups**
*   **Alert Timestamps:** Mar 31, 2026, at 5:28 PM, 5:30 PM, and 5:33 PM (Three consecutive identical alerts).
*   **Last Metric Update:** 2026-03-31 17:27:06 UTC.
*   **Integration Created At:** Apr 1, 2026 1:28:09 AM (System log generation time).
*   **Monitor ID:** 17447106
*   **Event URL:** https://app.datadoghq.eu/monitors/17447106
*   **Follow-up:** Immediate investigation required by the Retail Media team to determine if the alert was a false positive (given metric value 0.045 < threshold 0.05) or if the rate spiked immediately after the snapshot.

**Summary for Briefing:**
The `marketing-service` in production triggered three identical P2 alerts between 5:28 PM and 5:33 PM on March 31, 2026. The alert monitors HTTP error rates exceeding 5%. Current logs show a metric value of 4.5%, suggesting the service may be recovering or the alert is flapping. The Retail Media team must review the Datadog APM, K8s deployment status, and runbook immediately to confirm if further intervention is needed.


## [16/26] Singapore’s Beverage Container Return Scheme Launches 1 April 2026
Source: gmail | Thread: 19d4322921d79bb3 | Labels: Inbox, Updates | Priority: None | Senders: iComms | Last Date: Tue, Mar 31, 2026, 9:03 AM | Last Updated: 2026-03-31T10:01:53.381246+00:00
**Daily Work Briefing: Singapore Beverage Container Return Scheme (BCRS)**

**Key Participants & Roles**
*   **iComms (internal_comms@fairpricegroup.sg):** Internal Communications lead; responsible for disseminating rollout information and FAQs to staff.
*   **National Environment Agency (NEA):** The governing body driving the national BCRS initiative.
*   **FPG (FairPrice Group) Teams:** Store, customer-facing, and sustainability teams executing the implementation, including installation of machines and customer training.
*   **Customers:** End-users required to pay deposits on eligible items and return containers via Return Right machines.

**Main Topic/Request**
The email announces the official launch of Singapore's Beverage Container Return Scheme (BCRS) effective 1 April 2026. The initiative aims to encourage recycling through a refundable deposit system. FairPrice Group (FPG) is acting as a key implementation partner, having installed infrastructure and completed staff training to support this national effort under the "One FPG" framework.

**Key Dates & Deadlines**
*   **1 April 2026:** Official launch date for BCRS; stores begin charging $0.10 deposits on eligible items with the Deposit Mark.
*   **30 September 2026:** End of the six-month transition period. During this window, stores may sell both pre-Deposit Mark and non-Deposit Mark products, but only marked items attract the deposit or are accepted at return machines.

**Decisions Made**
*   FPG has committed to installing more than **150 Return Right machines** across its store network.
*   Staff briefings, Standard Operating Procedures (SOPs), and customer-facing training have been finalized.
*   Point-of-sale systems are configured to apply the $0.10 deposit at checkout for eligible beverages.

**Eligibility & Operational Changes**
*   **Scope:** Pre-packaged plastic and metal beverage containers ranging from **150ml to 3,000ml** bearing the "Deposit Mark."
*   **Financial Mechanism:** Customers pay a refundable **$0.10 deposit** at purchase; refunds are issued upon return via Return Right machines.
*   **Logistics:** Machine locations and availability can be verified at https://returnright.sg.

**Pending Actions & Ownership**
*   **Staff Familiarization:** All teams must familiarize themselves with the BCRS initiative to assist customers effectively.
    *   *Owner:* All FPG Store and Customer-Facing Teams.
*   **Customer Support:** Staff must be prepared to answer queries regarding eligible products, deposit charges, and return procedures.
    *   *Owner:* Store and customer-facing teams.
*   **Technical Support:** For unresolved technical or policy questions, staff should contact sustainability@fairpricegroup.sg.
    *   *Owner:* Sustainability Team / iComms.

**Resources Referenced**
*   Store FAQs: BCRS FAQs (Link in original email)
*   National Info: https://bcrs.sg
*   Machine Locator: https://returnright.sg


## [17/26] Your NRF 2026 APAC registration is one click away
Source: gmail | Thread: 19d419ef3264ff6e | Labels: Inbox, Promotions | Priority: None | Senders: NRF 26: Retail's Bi. | Last Date: Tue, Mar 31, 2026, 6:25 AM | Last Updated: 2026-03-31T10:02:33.524139+00:00
**Daily Work Briefing: NRF 2026 APAC Registration Update**

**Key Participants & Roles**
*   **Sender:** NRF 26 Event Team (events@gevme.com), representing the conference organizers.
*   **Recipient:** Michael, a confirmed past attendee of NRF 2025.

**Main Topic/Request**
The email serves as an expedited registration invitation for **NRF 2026: Retail's Big Show Asia Pacific**. Leveraging Michael's history as a 2025 attendee, the system has fast-tracked his eligibility for a "1-Click Free Expo Pass," requiring no re-entry of personal details—only an opt-in confirmation. The message simultaneously promotes an upsell to the paid "Retailer All-Access Pass" with exclusive perks and pricing.

**Pending Actions & Ownership**
*   **Action Required:** Confirm acceptance of the free Expo Pass by clicking the provided redemption button.
    *   **Owner:** Michael (Recipient).
*   **Action Required (Optional):** Upgrade to the Retailer All-Access Pass using code `NRFLOYALIST` to access high-level insights.
    *   **Owner:** Michael (if interested in C-suite keynotes and strategy roundtables).

**Decisions Made**
*   No formal decision recorded; the email acts as a solicitation awaiting recipient action. The system assumes attendance intent based on prior history but requires explicit confirmation for the free pass.

**Key Dates, Deadlines, & Specific References**
*   **Event Dates:** June 2–4, 2026.
*   **Venue:** Marina Bay Sands, APAC region.
*   **Early Bird Deadline:** April 10, 2026 (pricing extended; previously noted as a standard deadline).
*   **Discount Code:** `NRFLOYALIST`.
*   **Pricing Details (All-Access Pass):** Reduced to USD $599 (Regular Price: USD $1,499) with the code. Total savings: USD $900.
*   **Event Content Highlights:**
    *   **Expo Pass Inclusions:** Full floor access (300+ exhibitors), 60 "Big Ideas" sessions, NRF Innovators Showcase (top 30 startups), Opening Party & Expo Happy Hour, and networking with 13,000+ attendees from 80+ countries.
    *   **All-Access Pass Additions:** Keynote sessions featuring C-suite leaders (LVMH North America, Shiseido Japan, Olive Young, Gill Capital, DFI Retail, Lotte Retail, SM Supermalls, AEON360, Nestle), deep-dive breakout sessions on Agentic AI, retail media, and cross-border commerce, plus invite-only Roundtable Luncheons.
    *   **Add-ons:** Expo Tours & Retail Store Tours available for separate purchase under both pass types.

**Summary**
Michael is invited to instantly secure his free Expo Pass via a one-click link, granting full access to the exhibition floor and social events. To unlock C-suite keynotes, strategic breakout sessions (e.g., Agentic AI), and invite-only roundtables, he must upgrade to the Retailer All-Access Pass. By using code `NRFLOYALIST` before the extended Early Bird deadline of April 10, 2026, he can lock in a rate of USD $599, saving USD $900 off the standard price.


## [18/26] Your Weekly Digest from Datadog
Source: gmail | Thread: 19d4280fdfb0dcd7 | Labels: Inbox, Updates | Priority: None | Senders: Datadog | Last Date: Tue, Mar 31, 2026, 6:07 AM | Last Updated: 2026-03-31T10:02:54.608424+00:00
**Daily Work Briefing: Datadog Weekly Digest (NTUC Enterprise)**

**Key Participants & Roles**
*   **System/Alerts:** Datadog monitoring system.
*   **On-Call Teams:** @oncall-test-slo-v2-alert, @opsgenie-com-team, @hangouts-test-seller-datadog-notification, @opsgenie-dpd-seller, @hangouts-dd-dpd-pricing-alert, @hangouts-dd-cco-tech-alert, @hangouts-dd-dpd-engage-alert, @oncall-dpd-engage-journey.
*   **Specific Owners:** Arijit Mondal (arijit.mondal@fairprice.com.sg), FST Notifications team (@hangouts-FSTNotifications).

**Main Topic**
Weekly operational summary for NTUC Enterprise Datadog instance covering the period since March 23, 2026. The digest highlights system stability, metric alerts, and error budget consumption across various production services (Linkpay, POS, Catalogue, UI).

**Pending Actions & Ownership**
*   **CRITICAL:** Investigate and resolve high SLO Error Budget burn rate for `slo_cp_linkpay_authorize_capture_transaction`. Burn rates of 9.1 (1h) and 9.11 (5m) were recorded on March 30.
    *   **Owner:** @oncall-test-slo-v2-alert.
*   **High Priority:** Review duplicated barcode logic in `fpon-catalogue-job-update-barcode-cache`.
    *   **Owner:** @opsgenie-com-team.
*   **Performance:** Analyze latency on the `get inventories` endpoint (Seller Proxy) and `put_/api/pos/transaction/extend` requests (99th percentile > 2.6s).
    *   **Owners:** @hangouts-test-seller-datadog-notification, @hangouts-dd-dpd-pricing-alert.
*   **Data Integrity:** Address KPOS data replication failures caused by missing local values (e.g., business branch ID) on device TS3721AP42211.
    *   **Action:** Fix local data, refresh POS, or reload POS.
    *   **Owner:** @hangouts-FSTNotifications.

**Decisions Made**
*   No strategic decisions recorded; this is an automated status digest.
*   Monitors for `engage-my-persona-api-go` (high error rate) and `slo_grocery_browse_home_page_v2` (error budget consumption at 69.8%) have triggered recovery notifications, indicating temporary incidents are resolved or stabilizing.

**Key Dates & Deadlines**
*   **Report Date:** March 31, 2026, 6:07 AM.
*   **Critical Incident Window:** March 30, 2026 (Between 15:47 UTC and 16:03 UTC).
    *   16:03: SLO Error Budget Alert triggered.
    *   16:02: Duplicate barcode alert triggered.
    *   15:59: Inventory endpoint failure.
    *   15:58: iOS UI component error recovered.
*   **SLA Requirement:** Resolve the `slo_grocery_browse_home_page_v2` incident within the defined SLA as 69.8% of the 7-day error budget was consumed by March 30, 02:09 UTC.

**Summary Statistics**
*   Total Events: 104.
*   Alerts Triggered: 16 (including 1 P1 Critical).
*   Alerts Recovered: 88.


## [19/26] Opsgenie Alert: [Datadog] [P4] [Triggered] Service marketing-service has an abnormal change in throughput on env:prod
Source: gmail | Thread: 19d41f20431fe72f | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Tue, Mar 31, 2026, 3:36 AM | Last Updated: 2026-03-31T06:01:44.999819+00:00
### Daily Work Briefing: Opsgenie Alert Summary

**Key Participants & Roles**
*   **System:** Opsgenie (Integration: `dpd-grocery-retail-media-eu`), Datadog, Google Kubernetes Engine.
*   **Notified Groups/Handlers:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`.
*   **Assigned Ownership:** DPD Staff Excellence - Retail Media.

**Main Topic/Request**
*   **Alert Type:** [P4] Abnormal change in throughput for the `marketing-service` in the production environment (`env:prod`).
*   **Trigger Condition:** 100% of `sum:trace.http.request.hits` values deviated more than 3 standard deviations from predicted values over the last 15 minutes.
*   **Timestamp:** Alert generated March 31, 2026, at 03:30:10 UTC (Opsgenie created notification at 11:31:12 AM local time).

**Pending Actions & Ownership**
*   **Action Required:** Immediate investigation of service anomalies.
*   **Owner:** DPD Staff Excellence - Retail Media.
*   **Investigation Steps:**
    1.  Review Datadog APM metrics: [Datadog - marketing-service](https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod).
    2.  Check Kubernetes deployment status: [K8s - marketing-service](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview?cloudshell=false&project=fponprd).
    3.  Consult the remediation guide: [Runbook- marketing-service](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book).

**Decisions Made**
*   None recorded in this thread. The content consists solely of automated system notifications and alert triggers.

**Key Dates, Deadlines & Follow-ups**
*   **Alert Issue Date:** March 31, 2026.
*   **Critical Window:** Anomaly detected during the last 15 minutes prior to 03:30:10 UTC on Mar 31, 2026.
*   **Reference Links:**
    *   Event URL: https://app.datadoghq.eu/monitors/17447110
    *   Snapshot Link: https://app.datadoghq.eu/monitors/17447110?from_ts=1774926910000&to_ts=1774928110000&event_id=8567537098122505766
    *   Datadog Tag ID: `env:prod`, `service:marketing-service`.

**Note:** The alert was duplicated in the source log (Sent at 3:31 AM and 3:36 AM). No human response or resolution status has been logged yet.


## [20/26] [GCP] New Service Account Key Created - 38d52f5f0c7aff77850e3d4cd55bca6616ff6a34
Source: gmail | Thread: 19d41d98e342213e | Labels: Inbox, Forums | Priority: None | Senders: noreply-sre | Last Date: Tue, Mar 31, 2026, 3:04 AM | Last Updated: 2026-03-31T06:01:58.397438+00:00
**Daily Work Briefing: GCP Service Account Key Notification**

**Key Participants & Roles**
*   **System/Automated Sender:** `noreply-sre@ntucenterprise.sg` – Delivered the automated alert regarding key generation.
*   **Service Account Owner (Implied):** The recipient of this notification, responsible for managing the service account `fponprd/fpon-gcs-sign-url@fponprd.iam.gserviceaccount.com`.

**Main Topic/Request**
The thread confirms the successful creation of a new GCP Service Account Key (`38d52f5f0c7aff77850e3d4cd55bca6616ff6a34`) for the project `fponprd`. The key is valid for 90 days.

**Pending Actions & Ownership**
*   **Action:** Download and securely store the new service account key.
    *   **Owner:** Notification recipient (Service Account Owner).
    *   **Method:** Click "the link here" in the original notification email to initiate the download.
*   **Action:** Validate that the new key has been successfully integrated into any dependent systems or applications replacing the previous key.
    *   **Owner:** Service Account Owner / DevOps Team.

**Decisions Made**
No human decisions were made in this thread; this is a system-generated notification confirming an action (key generation) already executed by the SRE team or automated policy.

**Key Dates & Deadlines**
*   **Creation Date:** March 31, 2026 (3:04 AM).
*   **Expiration Date:** June 29, 2026.
*   **Validity Period:** 90 days from creation.
*   **Next Follow-up Required:** Prior to June 29, 2026, to ensure key rotation or renewal is completed before expiration.

**Specific References**
*   **Project ID:** `fponprd`
*   **Service Account Email:** `fponprd/fpon-gcs-sign-url@fponprd.iam.gserviceaccount.com`
*   **Key Hash:** `38d52f5f0c7aff77850e3d4cd55bca6616ff6a34`
*   **Email Metadata Labels:** Inbox, Forums


## [21/26] [Dashboard Report] Retail Media - DD Dashboard | Tue 31 Mar 11:00AM +08
Source: gmail | Thread: 19d41d7dc9b98925 | Labels: Inbox, Updates | Priority: None | Senders: Datadog HQ | Last Date: Tue, Mar 31, 2026, 3:02 AM | Last Updated: 2026-03-31T06:02:09.633408+00:00
**Daily Work Briefing Summary: Retail Media Dashboard Report**

**1. Key Participants & Roles**
*   **Sender:** Datadog HQ (`no-reply@dtdg.eu`) – System automated notification from the monitoring platform provider.
*   **Recipient:** Michael – Internal stakeholder responsible for dashboard oversight and data analysis.
*   **Team:** Team Datadog – Automated distribution unit.

**2. Main Topic & Request**
*   **Topic:** Delivery of a periodic performance report titled **"Retail Media - DD Dashboard"**.
*   **Request:** Notification that the attached report contains aggregated data covering the **past 3 days** relative to the generation date. The sender explicitly requests "Happy monitoring," indicating the expectation is for Michael to review the metrics.

**3. Pending Actions & Ownership**
*   **Action Item:** Review the attached dashboard report containing the last 3 days of Retail Media data.
*   **Owner:** **Michael**.
*   **Status:** Awaiting execution (Report received; analysis pending).

**4. Decisions Made**
*   No strategic decisions or approvals were recorded in this specific thread. The communication is purely informational regarding data availability.

**5. Key Dates, Deadlines & Follow-ups**
*   **Reference Date:** Tuesday, March 31, 2026.
*   **Report Generation Time:** 11:00 AM +08 (Local time of report generation).
*   **Email Receipt Timestamp:** 3:02 AM UTC (Implied by the `no-reply` header and global send time relative to local report time).
*   **Data Scope:** March 28, 2026 – March 31, 2026.
*   **Follow-up:** None explicitly scheduled; review is implied as standard operational procedure ("Happy monitoring").

**Attachments Referenced:**
*   File: "Retail Media - DD Dashboard" (Sent via email body attachment).


## [22/26] [VidiCenter] Weekly Performance Report
Source: gmail | Thread: 19d41a8d3012e9c6 | Labels: Updates | Priority: None | Senders: Quividi | Last Date: Tue, Mar 31, 2026, 2:11 AM | Last Updated: 2026-03-31T06:02:22.423485+00:00
**Daily Work Briefing: VidiCenter Weekly Performance Report**

**Key Participants & Roles**
*   **Quividi (no-reply@quividi.com):** Automated system sender providing the weekly performance data.
*   **[Recipient/Organization]:** FairPrice network administrator responsible for reviewing location status and account settings.

**Main Topic/Request**
Review of the VidiCenter "FairPrice network" performance metrics for the week of **Monday, March 23, 2026 – Sunday, March 29, 2026**. The report highlights a critical failure in data collection across the entire network.

**Key Findings**
*   **Impressions Collected:** 0 impressions recorded for the current week and the previous week.
*   **Rate:** 0.00 impressions per active location per day (average).
*   **Network Health Status:** **NOT OPERATIONAL**.
*   **Historical Context:** No impressions have been recorded across any active locations over a one-month period.
*   **Diagnosis:** The system indicates that the 3 currently active locations are likely no longer in use.

**Pending Actions & Ownership**
*   **Action:** Review physical usage status of all 3 active FairPrice network locations.
*   **Action:** Deactivate any locations confirmed to be unused or offline within the VidiCenter dashboard.
*   **Owner:** Organization/FairPrice Network Administrator (implied recipient).

**Decisions Made**
No decisions were recorded in this thread; only an automated diagnostic alert was issued.

**Key Dates & Deadlines**
*   **Report Period:** March 23, 2026 – March 29, 2026.
*   **Historical Data Scope:** One month period (ending approx. March 31, 2026).
*   **Follow-up Required:** Immediate investigation into location status is recommended to resolve the "NOT OPERATIONAL" diagnosis.

**Specific References**
*   **System:** VidiCenter [Resource]
*   **Network Name:** FairPrice network
*   **Last Message ID:** 19d41a8d3012e9c6
*   **Labels:** Updates


## [23/26] Re: Invitation: G5: Building a Better Workplace Together: Your Feedback M... @ Tue 7 Apr 2026 11am - 11:45am (SGT) (Carol Lee)
Source: gmail | Thread: 19d417701b5fac61 | Labels: Inbox | Priority: None | Senders: Melissa Hauw | Last Date: Tue, Mar 31, 2026, 1:16 AM | Last Updated: 2026-03-31T06:02:47.734083+00:00
**Daily Work Briefing: FPG Focus Group Discussion**

**Key Participants & Roles**
*   **Melissa Hauw** (melissa_hauw@fairpricegroup.sg): Organizer/Sender.
*   **Attendees**: Invited recipients of the email thread (specific names not listed in the provided content).

**Main Topic/Request**
Follow-up communication regarding an invitation to a **Focus Group Discussion** titled "G5: Building a Better Workplace Together: Your Feedback." The session aims to gather employee perspectives on current workplace successes and challenges. The goal is to identify FPG-level themes and solutions to improve the overall employee experience.

**Pending Actions & Ownership**
*   **Action**: Confirm attendance availability for the scheduled session.
*   **Owner**: All invited recipients (implied by "If your schedule allows...").
*   **Context**: Participation is requested to ensure accurate identification of themes and solutions.

**Decisions Made**
No decisions were recorded in this specific email thread; it serves as a reminder and call-to-action following an initial invitation.

**Key Dates & Deadlines**
*   **Event Date/Time**: Tuesday, April 7, 2026.
*   **Event Time**: 11:00 AM – 11:45 AM (SGT).
*   **Follow-up Sent**: March 31, 2026.

**Summary**
Melissa Hauw sent a reminder on March 31 regarding the upcoming Focus Group Discussion on April 7, 2026. The session is scheduled for 45 minutes (11:00 AM – 11:45 AM SGT) and focuses on gathering feedback to enhance the workplace experience at FairPrice Group (FPG). Recipients are asked to confirm participation if their schedules permit.


## [24/26] Daily digest: updates from Shiva Kumar Yalagunda Bas
Source: gmail | Thread: 19d41033c33cb741 | Labels: Inbox, Updates | Priority: None | Senders: Confluence | Last Date: Mon, Mar 30, 2026, 11:10 PM | Last Updated: 2026-03-31T06:03:01.444596+00:00
### Daily Work Briefing: Confluence Update Digest

**Source:** Shiva Kumar Yalagunda Bas (via Atlassian Confluence automated digest)  
**Date of Report:** March 30, 2026  
**Email Time:** 11:10 PM  

#### 1. Key Participants & Roles
*   **Shiva Kumar Yalagunda Bas:** Content Contributor/Editor. Responsible for updates to the "BCRS Unit Count Sync Recovery" page.
*   **Atlassian Confluence (confluence@ntuclink.atlassian.net):** Automated system sender providing daily activity highlights.

#### 2. Main Topic/Request
The primary subject is a notification regarding content modifications made by Shiva Kumar Yalagunda Bas to the **"BCRS Unit Count Sync Recovery"** documentation page on the NTU Confluence instance. The email serves as an automated summary of changes to contributed content for review.

#### 3. Pending Actions & Ownership
*   **Action:** Review the specific changes made to the "BCRS Unit Count Sync Recovery" page.
*   **Owner:** Recipient of this digest (implied stakeholder or team member).
*   **Method:** Access the linked Confluence page via the "View changes" link provided in the email.

#### 4. Decisions Made
No formal business decisions were recorded in this automated notification. The content reflects a technical update regarding a recovery process for unit counts within the BCRS (likely Business Continuity and Recovery System) unit.

#### 5. Key Dates & Follow-ups
*   **Event Date:** March 30, 2026.
*   **Update Timestamp:** March 30, 2026, at 11:10 PM (UTC+1 assumed based on domain context).
*   **Follow-up Required:** Immediate review of the "BCRS Unit Count Sync Recovery" page updates to ensure data integrity and process accuracy.

#### 6. Specific References & Metadata
*   **Resource ID:** `19d41033c33cb741` (Last message ID).
*   **Sender Email:** `confluence@ntuclink.atlassian.net`.
*   **Page Title:** "BCRS Unit Count Sync Recovery".
*   **Labels:** Inbox, Updates.
*   **Action Link:** "Go to Confluence" / "View changes".

**Summary Statement:**
Shiva Kumar Yalagunda Bas updated the "BCRS Unit Count Sync Recovery" documentation on March 30, 2026. Stakeholders are advised to review these specific changes via the provided Confluence link to confirm the recovery process status.


## [25/26] You have no events scheduled today.
Source: gmail | Thread: 19d40c04e42da577 | Labels: Inbox, Updates | Priority: None | Senders: Google Calendar | Last Date: Mon, Mar 30, 2026, 9:57 PM | Last Updated: 2026-03-30T22:01:11.161185+00:00
**Daily Work Briefing Summary**

**Key Participants & Roles**
*   **Michael Bui** (michael.bui@fairpricegroup.sg): Primary recipient of the daily agenda notification; subscribed to the "Digital Business Tech Release/Changes" calendar.
*   **Google Calendar System**: Automated sender providing status updates on schedule availability.

**Main Topic/Request**
The email is an automated system notification confirming that the recipient's work schedule for the current day (Tuesday, March 31, 2026) contains no scheduled events. No manual request or discussion occurred in this thread; it serves purely as a status confirmation.

**Pending Actions & Ownership**
*   **No Pending Actions:** There are no tasks assigned, requests made, or follow-ups required based on this specific message.
*   **Ownership:** N/A (System-generated informational update).

**Decisions Made**
*   No decisions were recorded in this thread. The content reflects a static state of the calendar rather than an outcome of deliberation.

**Key Dates & Deadlines**
*   **Notification Date/Time:** March 30, 2026, at 9:57 PM.
*   **Relevant Day:** Tuesday, March 31, 2026 (Confirmed as having no scheduled events).
*   **Calendar Subscription:** Digital Business Tech Release/Changes.

**Specific References**
*   **Account Email:** michael.bui@fairpricegroup.sg
*   **Last Message ID:** 19d40c04e42da577
*   **Settings Link:** https://calendar.google.com/calendar/ (for modifying calendar subscription preferences).

**Conclusion**
The briefing confirms a clear schedule for Michael Bui on March 31, 2026. No immediate action is required unless the user wishes to modify their notification settings via the provided link.


## [26/26] How AI is actually changing developer productivity
Source: gmail | Thread: 19d4065007217075 | Labels: Inbox, Promotions | Priority: None | Senders: Team Atlassian | Last Date: Mon, Mar 30, 2026, 8:17 PM | Last Updated: 2026-03-30T22:01:23.426019+00:00
**Daily Briefing: AI Productivity Webinar Invitation**

**Key Participants & Roles**
*   **Sender:** Atlassian Team (team@eml.atlassian.com)
*   **Speaker 1:** Justin Reock, Deputy CTO at DX. Expert in developer experience and productivity with 20+ years of experience.
*   **Speaker 2:** Nathen Harvey, DORA Lead and Product Manager at Google Cloud. Leads the DORA team on software delivery metrics and co-author of influential reports including "97 Things Every Cloud Engineer Should Know."

**Main Topic & Request**
The email invites recipients to a free webinar titled **"Measuring AI's real impact on developers"** based on the 2025 DORA State of AI-Assisted Software Development report. The session aims to move beyond hype regarding "10x" productivity gains and discuss realistic metrics, benchmarking strategies, and prerequisites for scaling AI in engineering teams.

**Action Items & Ownership**
*   **Action:** Register for the webinar or sign up to receive the recording if unable to attend live.
    *   **Owner:** Recipient (implied need to save a spot).
    *   **Link:** "Save your spot" (CTA provided in original email).

**Decisions Made**
*   No internal decisions were made or recorded in this thread; this is an external invitation.

**Key Dates & Deadlines**
*   **Event Date:** April 23–24, 2026.
*   **Current Status:** Registration is open ("Limited spots available").
*   **Follow-up:** If the recipient cannot attend live, they are instructed to register anyway to receive a recording.

**Specific References**
*   **Report:** 2025 DORA State of AI-Assisted Software Development (140-page document).
*   **Topics Covered:** Realistic productivity gains, evaluation metrics, cross-team benchmarking, and leadership prerequisites for AI scale.
*   **Organization:** Atlassian Pty Ltd, 341 George Street, Sydney, NSW, 2000, Australia.
