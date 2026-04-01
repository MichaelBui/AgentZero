

## [1/30] Michael Bui, here is your weekly update for 1 Apr
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


## [2/30] What is Next – The Agentic Evolution with Workbench
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


## [3/30] Opsgenie Alert: [Datadog] [P4] [Triggered] Service marketing-service has an abnormal change in throughput on env:prod
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


## [4/30] [Dashboard Report] Retail Media - DD Dashboard | Wed 1 Apr 11:00AM +08
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


## [5/30] Re: [Bitbucket] Pull request #919: chore/omni ops monitor (ntuclink/dpd-datadog-monitoring)
Source: gmail | Thread: 19d2d6690d21cc23 | Labels: Inbox, Updates | Priority: None | Senders: Sundy Yaputra | Last Date: Wed, Apr 1, 2026, 2:47 AM | Last Updated: 2026-04-01T06:03:06.182968+00:00
**Daily Work Briefing: Pull Request #919 Summary (Updated)**

**Key Participants & Roles**
*   **Sundy Yaputra**: Author and primary contributor. Responsible for executing code changes, refactoring monitoring logic, restructuring service locations, and merging branches within the `ntuclink/dpd-datadog-monitoring` repository.

**Main Topic/Request**
The thread concerns Pull Request #919 titled "chore/omni ops monitor." The objective is to reorganize Datadog monitoring configurations for the DPD Omni-Ops team, specifically dividing logic into SLO and monitor components, relocating services, establishing dedicated folder structures, and adding specific service definitions.

**Actions Pending & Ownership**
*   **Review/Merge**: No explicit approval or rejection is noted in the latest email update (April 1, 2026). The PR remains open for review by the team.
    *   *Owner*: Not specified (Default: Reviewers assigned to the repository).
*   **Monitoring Implementation & Updates**: Sundy Yaputra has completed multiple iterations of code changes on April 1, 2026. Recent actions include dividing logic into SLOs/monitors, moving services for the DPD Omni-Ops team, copying monitors to the "omni ops folder," and adding "engage journey" and "engage compass" services.
    *   *Owner*: Sundy Yaputra (Status: Complete/Updated).

**Decisions Made**
No formal business decisions are recorded. The technical trajectory confirms the architectural restructuring of the monitoring codebase, evidenced by the full commit history including updates on April 1, 2026:

1.  **Modularization**: Initial and subsequent separation of logic into SLO and monitor components (Commits `8ca2912` from Mar 26, `a42edd0` from Apr 1).
2.  **Service Relocation**: Movement of services to align with the DPD Omni-Ops team structure (Commits `c6b7b50` from Mar 26, `214a537` from Apr 1).
3.  **Directory Restructure**: Copying monitors specifically to the "omni ops folder" (Commit `87748fe` from Mar 26, `4aeb667` from Apr 1).
4.  **Service Addition**: Inclusion of "engage journey" and "engage compass" services (Commit `fa21787`).
5.  **Branch Merging**: Successful merge of the feature branch into the target branch (Commit `74ede15`).

**Key Dates & Follow-ups**
*   **Last Activity Date**: April 1, 2026.
*   **Activity Time**: Between 2:16 AM and 2:47 AM UTC.
*   **Latest Commit ID**: `fa21787` (Add service) / `74ede15` (Merge).
*   **Previous Activity**: Significant updates also occurred on March 26, 2026, establishing the initial restructure logic.
*   **Next Steps**: Stakeholders must review the finalized changes (including the new merge and additional services) within Bitbucket to provide feedback or grant merge approval. No specific deadline was set in this notification.

**Reference Data**
*   **Repository**: `ntuclink/dpd-datadog-monitoring`
*   **Pull Request ID**: #919
*   **Branch/Topic**: `chore/omni ops monitor`
*   **Message ID**: `19d46f0961a538e6` (Latest notification) / `19d2d6690d21cc23` (Previous context).


## [6/30] Updated invitation: DPD + Core Product + Picking Team meeting + Light @ Thu Apr 2, 2026 9:30am - 11am (SGT) (Michael Bui)
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


## [7/30] Invitation: DPD + Core Product + Picking Team meeting @ Thu Apr 2, 2026 9:30am - 11am (SGT) (Michael Bui)
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


## [8/30] [RAW Overdue] Expired Risk Acceptance & Waiver Form
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


## [9/30] You have no events scheduled today.
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


## [10/30] Opsgenie Alert: [Datadog] [P2] [Warn] Service marketing-service has a high error rate on env:prod
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


## [11/30] Singapore’s Beverage Container Return Scheme Launches 1 April 2026
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


## [12/30] Re: [## 112603 ##] Sev1 incident: Ad Products per response is low for PLA
Source: gmail | Thread: 19d2ead5d3ae56a5 | Labels: Inbox | Priority: None | Senders: Nikhil, Osmos | Last Date: Tue, Mar 31, 2026, 7:14 AM | Last Updated: 2026-03-31T10:02:14.272161+00:00
**Daily Work Briefing: Sev1 Incident #112603 (Updated)**

**Key Participants & Roles**
*   **Nikhil Grover** (nikhil.grover@fairpricegroup.sg): Incident coordinator/escalation lead. Previously blocked by access limitations; now implementing fixes on the client side.
*   **Michael Bui**: Technical subject matter expert. Requested for advisory support regarding incident scope and ad request URL analysis.
*   **Osmos Support** (support@onlinesalesai.zohodesk.in): Support team providing diagnostic guidance regarding the `pcnt` parameter.

**Main Topic & Request**
The thread addresses a Severity 1 (Sev1) incident [#112603] concerning low volume responses from Ad Products within Programmatic Local Ads (PLA). Initial analysis suggested that the `pcnt` parameter in ad requests was incorrectly set to `1`, limiting responses to a single product. While Nikhil Grover initially lacked access to specific request URLs, Osmos Support requested Michael Bui provide URLs for keywords "chocolate" and "toothpaste" to verify this parameter.

**Pending Actions & Ownership**
*   **Action:** Monitor the impact of the client-side fix (`pcnt = 6`) and report on any discrepancies.
    *   **Owner:** Osmos Support / Nikhil Grover.
    *   **Deadline:** Update required tomorrow (March 27, 2026 context implies "tomorrow" relative to the March 31 update).
*   **Action:** Verification of `pcnt` parameter values in ad requests for keywords "chocolate" and "toothpaste."
    *   **Status:** Resolved by client.

**Decisions Made**
*   **Root Cause Identified:** The low response volume was attributed to the `pcnt` parameter being set to `1` instead of a higher value.
*   **Resolution Implemented:** Nikhil Grover confirmed on March 31, 2026, that the issue was fixed on their end by setting `pcnt = 6` for all product ad requests.
*   **Implementation Time:** The fix is effective starting 3:00 PM Singapore time on March 31, 2026.

**Key Dates & Follow-ups**
*   **Incident ID:** [#112603]
*   **Initial Escalation:** March 27, 2026, 9:43 AM (Nikhil Grover requested Michael Bui's support due to URL access issues).
*   **Diagnostic Request:** March 31, 2026, 6:15 AM (Osmos Support requested specific URLs to verify `pcnt`).
*   **Resolution Confirmation:** March 31, 2026, 7:14 AM (Nikhil Grover confirmed fix).
*   **Follow-up Status:** Pending monitoring and update tomorrow regarding discrepancies.

**Summary of Thread Chronology**
On March 27, 2026, Nikhil Grover escalated the Sev1 incident to Michael Bui due to an inability to access specific request URLs needed for troubleshooting low PLA responses. On March 31, 2026, Osmos Support requested specific ad request URLs for "chocolate" and "toothpaste" from Michael Bui to analyze the `pcnt` parameter. Subsequently, Nikhil Grover informed the team that the issue was resolved on their end. The fix involved setting the `pcnt` value to `6` for all product ad requests, effective from 3:00 PM Singapore time on March 31. The team is now awaiting a monitoring update "tomorrow" to confirm if the discrepancy has been cleared.


## [13/30] Your NRF 2026 APAC registration is one click away
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


## [14/30] Your Weekly Digest from Datadog
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


## [15/30] Opsgenie Alert: [Datadog] [P4] [Triggered] Service marketing-service has an abnormal change in throughput on env:prod
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


## [16/30] [GCP] New Service Account Key Created - 38d52f5f0c7aff77850e3d4cd55bca6616ff6a34
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


## [17/30] [Dashboard Report] Retail Media - DD Dashboard | Tue 31 Mar 11:00AM +08
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


## [18/30] [VidiCenter] Weekly Performance Report
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


## [19/30] Re: Invitation: G5: Building a Better Workplace Together: Your Feedback M... @ Tue 7 Apr 2026 11am - 11:45am (SGT) (Carol Lee)
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


## [20/30] Daily digest: updates from Shiva Kumar Yalagunda Bas
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


## [21/30] You have no events scheduled today.
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


## [22/30] How AI is actually changing developer productivity
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


## [23/30] [JIRA] (DPD-715) Dynamic ad slot configuration for Homepage swimlanes
Source: gmail | Thread: 19cd82204175d296 | Labels: Inbox, Updates | Priority: None | Senders: Nikhil | Last Date: Mon, Mar 30, 2026, 11:15 AM | Last Updated: 2026-03-30T14:02:12.655099+00:00
**Daily Work Briefing: DPD-715 Dynamic Ad Slot Configuration (Race Condition Identified; E2E Testing Required)**

**Key Participants & Roles**
*   **Nikhil Grover:** Product Manager.
*   **Michael Bui:** Development Lead/Manager; executed deployment and identified post-deployment race condition.
*   **Milind Badame:** Assigned QA/Test lead for new verification steps.

**Main Topic/Request**
Development of a dynamic ad slot configuration system (Ticket: **DPD-715**) for Omni and OG Homepage swimlanes, enabling Product Managers to control ad placement indices via Split feature flags without code deployments.

**Decisions Made & Status Updates**
*   **Status Change:** The ticket remains in a critical state following the initial "Done" status on March 25, 2026. A race condition was identified post-launch rendering the `pnct=1` flag ineffective.
*   **Current State:** As of March 30, 2026 (11:15 AM), the ticket requires execution of an End-to-End (E2E) test to validate the fix before re-deployment. The status is effectively **"Ready for E2E Test."**
*   **Production Deployment:** Initial deployment occurred on March 25, 2026 (12:02 AM Singapore Time). UAT was signed off by Nikhil Grover at 10:11 PM Singapore Time on the same date with configuration `[3, 5, 7, 11, 13, 15]`.
*   **Critical Defect Identified:** On March 27, 2026 (03:38 AM Singapore Time), Michael Bui identified a race condition where the `share` variable is overwritten, impacting concurrent requests. This was verified in UAT with evidence provided via screenshot (`image-20260327-193706.png`).
*   **New Testing Requirement:** Milind Badame has explicitly marked the ticket as requiring E2E testing (`Requires_e2e_test: Yes`) to ensure the race condition is resolved across the full user flow prior to final closure.

**Pending Actions & Ownership**
*   **Immediate Action Required:** Execute comprehensive E2E tests on the UAT environment to validate that the `share` variable overwrite logic has been corrected and `pnct=1` functions correctly under load.
*   **Ownership:** Milind Badame is responsible for initiating and executing the E2E test suite. Michael Bui must ensure the codebase is updated with the fix prior to testing.
*   **Monitoring:** Post-deployment monitoring remains paused pending successful E2E validation and subsequent re-deployment.

**Key Dates & Deadlines**
*   **Start Date:** March 10, 2026
*   **UAT Sign-off (Initial):** March 25, 2026 (10:11 PM Singapore Time).
*   **Production Deployment (Initial):** March 25, 2026 (12:02 AM Singapore Time).
*   **Issue Discovery:** March 27, 2026 (03:38 AM Singapore Time).
*   **E2E Test Requirement Added:** March 30, 2026 (11:15 AM) via Jira update by Milind Badame.

**Reference Data**
*   **Ticket ID:** DPD-715
*   **Project:** (Ecom/Omni) DPD
*   **Last Message ID:** 19d3e750cb60c97c (Updated from previous 19d30d7ccd9ed15b)
*   **New Flag:** `Requires_e2e_test: Yes`
*   **Attachments:**
    *   `image-20260325-160055.png` (Visual confirmation of slot changes).
    *   `ScreenRecording_03-26-2026 00-15-50_1.MP4` (Initial post-deployment validation).
    *   `image-20260327-193706.png` (Evidence of race condition affecting `pnct=1`).

**Historical Context Retained**
*   Boundary handling logic remains valid: Configured indices exceeding available content range are ignored; only valid bounds render.
*   Stock integrity checks remain active: Out-of-stock items cannot be served as ads regardless of slot configuration.
*   Previous mobile app issues were resolved in the earlier UAT cycle and verified during initial deployment, though the current race condition represents a new code-level defect unrelated to previous mobile fixes.


## [24/30] [JIRA] (DPD-733) Dynamic ad slots for vertical scroll on omni homepage
Source: gmail | Thread: 19d01d9056f39bea | Labels: Inbox, Updates | Priority: None | Senders: Michael | Last Date: Mon, Mar 30, 2026, 11:15 AM | Last Updated: 2026-03-30T14:02:30.023255+00:00
**Daily Work Briefing: DPD-733 (Dynamic Ad Slots for Vertical Scroll)**

**Key Participants & Roles**
*   **Michael Bui:** Developer/Project Lead. Previously identified as the sole actor performing updates on this work item within the provided log.
*   **Milind Badame:** Jira System User. Recently updated the ticket status and testing requirements.

**Main Topic**
*   **Issue:** [DPD-733] Dynamic ad slots for vertical scroll on omni homepage (Ecom/Omni).
*   **Objective:** Implement dynamic advertising functionality for vertical scrolling on the Omni homepage.

**Status Timeline & Decisions**
The following status transitions and updates were executed:
1.  **Development & Testing Phase:** On March 18, 2026, at 12:37 AM Singapore Time, Michael Bui moved the item from "TO BE DEFINED" through "READY FOR DEVELOPMENT," to "IN DEVELOPMENT," and finally to **"Testing in Preproduction."**
2.  **Completion Decision (Initial):** On March 18, 2026, at 12:37 AM Singapore Time, Michael Bui marked the item as **Resolution: Done** and updated the status to **"IN RELASE QUEUE"** (retaining the source typo) while retaining pre-production testing context.
3.  **Updated Testing Requirement:** On March 30, 2026, at 11:15 AM Singapore Time, Milind Badame updated the ticket indicating that **End-to-End (E2E) Testing is Required ("Yes").** This update supersedes the previous indication of completion pending only release execution.

**Pending Actions & Ownership**
*   **Action:** Conduct required End-to-End (E2E) testing before finalizing the release to production. The item cannot proceed to live deployment until E2E validation is confirmed as "Yes."
*   **Owner:** Milind Badame flagged this requirement; however, specific assignees for the execution of this new test phase are not explicitly defined in the latest log entry.
*   **Next Step:** Execute E2E testing protocols. Upon successful completion, proceed with release deployment from the queue to production.

**Key Dates & Deadlines**
*   **Last Update:** March 30, 2026, at 11:15 AM (E2E requirement update).
*   **Previous Status Change:** March 18, 2026, at 12:37 AM Singapore Time.
*   **Current State:** Item is in the release queue but requires E2E verification before final production launch.

**Additional Notes**
*   The work item includes attachments over 100 KB accessible via the "View work item" link.
*   Notification settings for Jira Cloud mobile apps (Android/iOS) are referenced in system comments.


## [25/30] [JIRA] Milind Badame mentioned you on DPD-715
Source: gmail | Thread: 19d3e71cd098db63 | Labels: Inbox, Updates | Priority: None | Senders: Milind Badame (Jira) | Last Date: Mon, Mar 30, 2026, 11:12 AM | Last Updated: 2026-03-30T14:02:44.252586+00:00
**Daily Work Briefing: Email Thread Summary**

**Key Participants & Roles**
*   **Milind Badame:** Jira User / Test Lead (Represents the testing team).
*   **Michael Bui:** Recipient of the mention; Stakeholder for test requirements.
*   **System/JIRA Bot:** Automated notification sender.

**Main Topic/Request**
Discussion regarding end-to-end (E2E) automation strategies for Jira work item **DPD-715: "Dynamic ad slot configuration for Homepage swimlanes"** within the **(Ecom/Omni) DPD** project. The core issue involves verifying Ad label positions based on split/on/off settings versus static configurations.

**Decisions Made**
*   **Automation Scope:** It was determined that E2E automation updates are **not required** at this time ("No for now").
*   **Verification Method:** Runtime verification of labels based on split settings cannot be automated. Verification must remain **static**, which is already covered by existing tests for vertical and horizontal swimlanes.

**Pending Actions & Ownership**
*   **Action:** Review specific label positions to determine if additional static test updates are needed.
    *   **Owner:** Michael Bui (implied).
    *   **Trigger:** If Michael Bui identifies specific positions requiring verification, he must inform the testing team ("If required, You can let us know...").
*   **Action:** Update E2E tests to include identified positions if requested.
    *   **Owner:** Milind Badame / Testing Team (conditional on Michael Bui's input).

**Key Dates & Follow-ups**
*   **Last Communication Date:** March 30, 2026, at 11:12 AM (Singapore Time).
*   **Work Item Reference:** DPD-715.
*   **Follow-up Status:** Pending. The testing team is waiting for Michael Bui to confirm if any specific positions need verification before proceeding with test updates. No immediate deadline was set, contingent on the user's input.

**Specific References**
*   **Jira Issue:** DPD-715
*   **Project:** (Ecom/Omni) DPD
*   **Feature:** Dynamic ad slot configuration for Homepage swimlanes
*   **Existing Coverage:** E2E tests currently verify Ad label positions for vertical and horizontal swimlanes.
*   **Constraint:** Labels cannot be verified at runtime based on split/on/off settings; verification must be static.


## [26/30] [JIRA] Milind Badame mentioned you on DPD-733
Source: gmail | Thread: 19d3e7152d3e2adf | Labels: Inbox, Updates | Priority: None | Senders: Milind Badame (Jira) | Last Date: Mon, Mar 30, 2026, 11:11 AM | Last Updated: 2026-03-30T14:02:55.060803+00:00
**Daily Work Briefing: JIRA Notification Summary**

**Key Participants & Roles:**
*   **Milind Badame:** System/Jira Tester or Developer (Sender). Provided status update on E2E automation feasibility.
*   **Michael Bui (You):** Recipient of the notification. Requested for input regarding test verification positions.

**Main Topic/Request:**
Discussion regarding **JIRA work item DPD-733** titled *"Dynamic ad slots for vertical scroll on omni homepage."* The focus is on the feasibility and scope of E2E automation for verifying Ad label positions within vertical and horizontal swimlanes, specifically concerning split/on-off settings.

**Decisions Made:**
1.  **Automation Limitation Confirmed:** It was established that runtime verification for label positions based on split/on-off settings cannot be automated at this time. Label verification must remain static.
2.  **E2E Update Status:** No immediate updates to the E2E test suite are required.

**Pending Actions & Ownership:**
*   **Action:** Provide specific label positions that require verification if additional testing is deemed necessary beyond the current static checks.
*   **Owner:** Michael Bui (You).
*   **Context:** Milind Badame has offered to update the tests accordingly should you provide these specific positions.

**Key Dates & References:**
*   **Date/Time:** March 30, 2026, at 11:11 AM (Sender noted as 7:11 PM Singapore Time).
*   **Work Item ID:** DPD-733.
*   **Project Context:** Ecom/Omni / DPD.
*   **Notification ID:** `19d3e7152d3e2adf`.

**Summary of Technical Stance:**
Milind confirmed existing E2E coverage for vertical and horizontal swimlanes verifies Ad label positions statically. Since runtime verification for dynamic split settings is not feasible, the current approach stands unless Michael Bui specifies alternative positions to be added to the test suite.


## [27/30] Opsgenie Alert: [Datadog] [P4] [Triggered] Service marketing-service has an abnormal change in throughput on env:prod
Source: gmail | Thread: 19d3bfcc25dc99ae | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Mon, Mar 30, 2026, 10:20 AM | Last Updated: 2026-03-30T14:03:21.700215+00:00
**Daily Work Briefing: Opsgenie Alert Summary (Updated)**

**1. Key Participants & Roles**
*   **System/Source:** Opsgenie (Notification Engine), Datadog (Monitoring Source).
*   **Alert Owner:** DPD Staff Excellence - Retail Media.
*   **Notify Channels:** `@hangouts-dd-dpd-grocery-alert` (Google Hangouts channel), `@opsgenie-dpd-grocery-retail-media` (Opsgenie responder group).
*   **Service Owner:** `marketing-service`.

**2. Main Topic/Request**
*   **Alert Type:** P4 Priority Alert regarding abnormal throughput changes in the production environment (`env:prod`).
*   **Specific Trigger:** 100% of `sum:trace.http.request.hits{env:prod,service:marketing-service}` values exceeded 3 deviations from predicted values over the last 15 minutes.
*   **Percent Anomalous:** 100.0%.
*   **Integration Details:** Source is Datadog via integration `dpd-grocery-retail-media-eu`.
*   **Request:** Immediate investigation of service health via provided Datadog APM links, Kubernetes (GCP) console, and Runbook documentation.

**3. Pending Actions & Ownership**
*   **Action:** Investigate throughput anomaly, review metrics graphs, and determine root cause for `marketing-service`.
*   **Owner:** DPD Staff Excellence - Retail Media (Assigned via Opsgenie responders).
*   **Required Resources:**
    *   Datadog APM: [Link to marketing-service operations](https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod)
    *   Kubernetes Console: [GCP Cluster Overview](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview?cloudshell=false&project=fponprd)
    *   Runbook: [Atlassian Wiki - marketing-service](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book)

**4. Decisions Made**
*   None recorded in this thread; the alert remains active and awaiting human intervention.

**5. Key Dates, Deadlines & Follow-ups**
*   **Alert Trigger Time:** Mar 30, 2026, at 11:44 PM UTC (Previous snapshot).
*   **Latest Status Update:** Mar 30, 2026, at 10:15 AM UTC (Newest notification received).
    *   *Note:* The "Last Updated" timestamp within the alert payload remains 2026-03-30 10:14:10 +0000.
*   **Notification Timestamps:**
    *   Initial Notification Received: Mar 30, 2026, at 6:15:12 PM (Local time noted in metadata as "Created At").
    *   Latest Status Update: Mar 30, 2026, at 10:15 AM UTC.
*   **Follow-up Required:** Immediate resolution or status update required by the Retail Media team to clear the P4 alert status.

**Technical Metadata**
*   **Monitor ID:** 17447110
*   **Event IDs:** 8565860058801546694 (Initial), 8566119760983702769 (Previous), 8566494225877288340 (Latest).
*   **Tags:** `env:prod`, `service:marketing-service`, `managed_by:datadog-sync`, `monitor`, `priority:p4`.
*   **Integration ID:** ff4c0851-ff71-4975-a76e-b9af95297a56-1774865712480 (TinyId: 139298).
*   **Alert Snapshot Link:** [Datadog Monitor Snapshot](https://app.datadoghq.eu/monitors/17447110?from_ts=1774864750000&to_ts=1774865950000&event_id=8566494225877288340&link_source=monitor_notif&link_monitor_id=17447110&link_event_id=8566494225877288340)
*   **Event URL:** https://app.datadoghq.eu/monitors/17447110


## [28/30] Indirect Procurement Q1 2026 Newsletter
Source: gmail | Thread: 19d3df93c2c73f8f | Labels: Inbox, Forums | Priority: None | Senders: 'Indirect Procureme. | Last Date: Mon, Mar 30, 2026, 9:00 AM | Last Updated: 2026-03-30T10:01:47.698304+00:00
**Executive Briefing: Indirect Procurement Q1 2026 Newsletter**

**Key Participants & Roles**
*   **Sender:** Project Buywell Team (via `grp_fpg_all@fairpricegroup.sg` and `project_buywell@fairpricegroup.sg`).
*   **Audience:** All FairPrice Group colleagues ("Colleagues").
*   **Stakeholders:** Indirect Procurement representatives, Finance team, Suppliers, and Subject Matter Experts (SMEs).

**Main Topic**
The newsletter outlines the final preparation phase for the "Project Buywell" indirect procurement system transition scheduled for Go-Live in Q1 2026. It introduces key features including the new **eInvoice module**, automated **Delegation of Authority (DOA)** streams, and clarifies usage boundaries between **Zycus eProc** and **MyClaims**.

**Pending Actions & Ownership**
*   **System Testing:** Users must prepare for User Acceptance Testing (UAT) and upcoming Key-User Testing/End-User Training sessions. *Owner: All Employees.*
*   **Training Compliance:** Employees must review feature spotlights to prepare for a mandatory quiz prior to Go-Live. Winners will receive prizes. *Owner: All Employees.*
*   **Process Adherence:** Users must stop using MyClaims for non-personal expenses and route such purchases to the correct dedicated systems (e.g., Zycus eProc for assets). *Owner: All Employees.*
*   **System Confirmation:** Recipients are requested to click a specific link (`https://forms.gle/D6whAz364PKpPznx5`) to confirm they have read the newsletter. *Owner: All Employees.*

**Decisions Made**
1.  **eInvoice Implementation:** Adoption of a digital-first eInvoice module to replace paper processing, enabling automated 3-way matching (PO, GR, Invoice) and real-time status tracking.
2.  **DOA Automation:** Approval streams will be automatically routed based on spend type:
    *   Standard Spend.
    *   Waiver Approval (Waiver of Competition/Tender).
    *   SME Approval (mandatory for technical exceptions like IT/Cybersecurity).
    *   Mobile approvals enabled for approvers.
3.  **Expense Policy Enforcement:** Strict prohibition on using credit card charge slips; only original itemized receipts are accepted. MyClaims is restricted strictly to personal expenses incurred while working.

**Key Dates & Deadlines**
*   **Newsletter Date:** March 30, 2026.
*   **Go-Live:** Imminent (Q1 2026 closure). A quiz will be administered immediately before Go-Live.
*   **Follow-up:** Training session emails are forthcoming; no specific dates provided yet.

**Specific References**
*   **Systems Mentioned:** Project Buywell, Zycus eProc, MyClaims, eInvoice module.
*   **Contact Email:** `project_buywell@fairpricegroup.sg`.
*   **Quiz Link:** Refer to "Ready for a Quiz?" section (link provided in original email).
*   **Sustainability Impact:** Digital invoicing cited as saving ~118 trees per 1M invoices and reducing carbon footprint by 63%.


## [29/30] [GCP] New Service Account Key Created - 5ef839aab5b8bfe27baf56b662a06e322aa14a8b
Source: gmail | Thread: 19d3dda3d1f0bd95 | Labels: Inbox, Forums | Priority: None | Senders: noreply-sre | Last Date: Mon, Mar 30, 2026, 8:26 AM | Last Updated: 2026-03-30T10:02:03.110799+00:00
**Daily Work Briefing: Service Account Notification**

**1. Key Participants & Roles**
*   **Sender:** `noreply-sre@ntucenterprise.sg` (System Automated Alert / SRE Team)
*   **Recipient Context:** The email targets the owner or administrator of the service account `fpon-224503/seller-analytics-service@fpon-224503.iam.gserviceaccount.com`. No specific human name is listed in the metadata, but the notification is directed at the entity responsible for this GCP resource.

**2. Main Topic/Request**
*   **Event:** Generation of a new Service Account Key.
*   **Key Identifier:** `5ef839aab5b8bfe27baf56b662a06e322aa14a8b`
*   **Resource:** GCP Service Account `fpon-224503/seller-analytics-service@fpon-224503.iam.gserviceaccount.com`.
*   **Action Required:** The recipient must download the new key via the provided link to ensure continuity of service access before the current credentials expire or are rotated.

**3. Pending Actions & Ownership**
*   **Action:** Download and securely store the new service account key `5ef839aab5b8bfe27baf56b662a06e322aa14a8b`.
*   **Owner:** The system administrator or developer responsible for the `seller-analytics-service` project.
*   **Urgency:** High; the key expires in 90 days, but immediate download is required to access it (as per standard security protocols for new keys).

**4. Decisions Made**
*   **System Decision:** A new key was automatically generated by the GCP system on March 30, 2026.
*   **Expiration Policy:** The new key is configured for a 90-day lifecycle.

**5. Key Dates & Deadlines**
*   **Creation Date/Time:** March 30, 2026, at 8:26 AM.
*   **Expiration Date:** June 28, 2026.
*   **Follow-up Required:** Immediate (Download). No specific follow-up meeting is noted in the thread; however, verification of successful deployment with the new key should occur prior to expiration.

**6. Metadata Context**
*   **Thread Labels:** Inbox, Forums.
*   **Priority:** Not set (null).
*   **Message ID:** `19d3dda3d1f0bd95`.


## [30/30] GCP Service Account Key clean UP
Source: gmail | Thread: 195892088be2d83b | Labels: Inbox | Priority: None | Senders: Mohit, Kyle, Himal | Last Date: Mon, Mar 30, 2026, 7:36 AM | Last Updated: 2026-03-30T10:02:27.546231+00:00
**Daily Work Briefing: GCP Service Account Key Cleanup (Updated)**

**1. Key Participants & Roles**
*   **Himal Hewagamage** (himal.hewagamage@fairpricegroup.sg): Initiator and Security Lead; followed up on March 30, 2026, regarding non-production remediation status.
*   **Kyle Nguyen**: Technical lead coordinating immediate cleanup; assigned Nicholas Tan to assist starting the week of March 30, 2026.
*   **Nicholas Tan**: New support resource added by Kyle Nguyen to assist with execution and tracking.
*   **Jazz Tong** (jazz_tong@fairpricegroup.sg): Previously identified as execution lead; role context remains relevant for scope verification.
*   **Mohit Niranwal** (mohit_niranwal@fairpricegroup.sg): Provided initial context on automated rotation gaps and legacy accounts.

**2. Main Topic/Request**
The team is addressing security risks associated with legacy GCP Service Account (SA) keys created between 2019–2024. Following the March 24, 2026, directive to remediate 56 keys in non-production environments, a status check on **March 30, 2026**, revealed no prior updates from Kyle's team. Consequently, work is now formally restarting with Nicholas Tan as support. Additionally, Himal confirmed the removal of old Datadog service account keys and updated the tracking sheet accordingly.

**3. Pending Actions & Owners**
*   **Immediate Remediation (Non-Prod)**: Kyle Nguyen and Nicholas Tan will commence execution for the 56 identified legacy keys starting the week of March 30, 2026.
*   **Progress Tracking**: Kyle Nguyen has added a "Status" column to the tracking sheet to monitor individual item progress; this is now the primary method for status reporting.
*   **Documentation Update**: Kyle must update the [GCP][Security] Service Account Key Rotation & Decommission document to reflect project owner information and current remediation status.
*   **Owner Verification**: Integration of Jazz Tong's previous task (tagging application owners) remains pending under Kyle's documentation responsibility.
*   **Onboarding Process**: For SAs without keys or those with outdated keys, the team will facilitate onboarding into the automated key rotation process via a specific Google Group.

**4. Decisions Made & Process Changes**
*   **Execution Strategy (Mar 30, 2026)**: The team confirmed that remediation for non-production environments will proceed immediately with expanded resources (Nicholas Tan).
*   **Data Hygiene**: Himal Hewagamage has proactively removed old Datadog service account keys and updated the central tracking sheet.
*   **Communication Channel**: A separate weekly communication channel remains the primary method for status updates regarding key decommissioning.
*   **Scope & Strategy**: The scope covers `cpd-dp`, `fpg-callisto`, `fpg-jarvis`, `fpg-optimus`, and `fponprd` environments. The strategy prioritizes enabling automated rotation for legacy accounts before decommissioning based on application utility.

**5. Key Dates & Follow-ups**
*   **Mar 10–24, 2026**: Initial requests, spreadsheet updates, meeting, and directive for immediate remediation of 56 keys issued by Himal.
*   **Mar 30, 2026 (4:11 AM)**: Himal requested a status update on non-production key removal, noting no response was received.
*   **Mar 30, 2026 (7:33 AM)**: Kyle confirmed the team will start work that week and added Nicholas Tan to support; tracking sheet updated with a new "Status" column.
*   **Mar 30, 2026 (7:36 AM)**: Himal confirmed removal of old Datadog keys and offered further support if clarification is needed.

**Links & References**
*   *Data Source*: https://docs.google.com/spreadsheets/d/1mGBCTRQDcTs0z_w0LjVtywDCtFHZhZfWYIRGqcNglpQ/edit?gid=0#gid=0 (Updated by Himal)
*   *Documentation*: [GCP][Security] Service Account Key Rotation & Decommission (To be updated by Kyle).
