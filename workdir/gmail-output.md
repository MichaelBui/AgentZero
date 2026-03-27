

## [1/50] To be modified / 驳回待修改
Source: gmail | Thread: 19d2da940cb36e48 | Labels: Inbox, Updates | Priority: None | Senders: service | Last Date: Fri, Mar 27, 2026, 4:59 AM | Last Updated: 2026-03-27T06:01:43.416884+00:00
**Daily Work Briefing: Visa Application Status Update**

**Key Participants & Roles**
*   **Applicant (You):** The primary subject of the application; responsible for reviewing rejection reasons and submitting amendments.
*   **Visa Application Service Center (`service@visaforchina.org`):** Issuer of the rejection notice; provides audit criteria and revision instructions.

**Main Topic/Request**
Notification regarding the rejection of Business Visa Application Form No. **SGP3260325AL0800072**. The application was flagged because the requested entry count and validity period violated the standard constraints for first-time business visa applicants.

**Pending Actions & Ownership**
*   **Action:** Log in to the Visa Application Service Center website, review the specific rejection feedback, and amend the application form (Form No. SGP3260325AL0800072).
*   **Owner:** Applicant.
*   **Specific Requirement:** The applicant must choose one of the following compliant options based on their needs:
    1.  **Standard First-Time Compliance:** Apply for a maximum of **two entries** with a validity of **6 months**.
    2.  **Long-Stay Option:** If staying for **180 days**, select a **single entry** visa instead.

**Decisions Made**
*   The Visa Application Service Center has **rejected** the initial submission due to non-compliant request parameters (excessive entries/validity for a first-time applicant). No decision on the final visa eligibility has been made pending the corrected application.

**Key Dates & Follow-ups**
*   **Notification Date:** March 27, 2026, at 4:59 AM.
*   **Reference ID:** Last message ID `19d2da940cb36e48`.
*   **Next Step:** Immediate amendment required before re-submission to avoid further delays. No specific deadline was provided in the notification; immediate action is recommended to secure appointment slots.


## [2/50] Opsgenie Alert: [Datadog] [P4] [Triggered] Service marketing-service has an abnormal change in throughput on env:prod
Source: gmail | Thread: 19d2c9102a5fde4d | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Fri, Mar 27, 2026, 4:25 AM | Last Updated: 2026-03-27T06:02:07.067738+00:00
**Daily Work Briefing: Opsgenie Alert Summary (Updated)**

**Key Participants & Roles**
*   **System/Integration:** Opsgenie (Notification engine), Datadog (Monitoring source).
*   **Alert Responders:** DPD Staff Excellence - Retail Media.
*   **Target Notification Channels:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`.

**Main Topic/Request**
*   **Alert Trigger:** A P4 anomaly detected in the production environment (`env:prod`) for the service `marketing-service`.
*   **Issue Description:** Throughput (HTTP request hits) deviated by more than 3 standard deviations from predicted values. Specifically, 100% of metric values for `sum:trace.http.request.hits{env:prod,service:marketing-service}` were anomalous over the last 15 minutes.
*   **Action Required:** Immediate investigation into service performance and infrastructure health using provided resources.

**Pending Actions & Ownership**
*   **Investigation:** Team members must review the following resources immediately:
    1.  Datadog APM HTTP request metrics: `https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod`
    2.  Kubernetes deployment details (Google Cloud, `asia-southeast1`, cluster `fpon-cluster`): `https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview`
    3.  Operational runbook: `https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book`
*   **Ownership:** "DPD Staff Excellence - Retail Media" is the designated responder group responsible for triaging and resolving this alert.

**Decisions Made**
*   No manual decisions were recorded; alerts are auto-generated based on pre-defined monitoring rules (Monitor ID: `17447110`).

**Key Dates, Deadlines & References**
*   **New Alert Timestamp:** Mar 27, 2026, at 4:20 AM (Last Updated: 2026-03-27 04:19:10 +0000).
*   **Opsgenie TinyId:** `139160`.
*   **Datadog Event ID:** `8561788215633308129`.
*   **Relevant Links:**
    *   Datadog Monitor Event URL: `https://app.datadoghq.eu/monitors/17447110`
    *   Metric Snapshot: `https://app.datadoghq.eu/monitors/17447110?from_ts=1774584250000&to_ts=1774585450000&event_id=8561788215633308129`
    *   Runbook: `https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book`
*   **Datadog Tags:** `env:prod`, `service:marketing-service`, `managed_by:datadog-sync`, `monitor`, `priority:p4`.

**Status Note**
The alert is currently active. A new instance (TinyId: `139160`) was generated at 4:20 AM on March 27, 2026, following the initial notification. No resolution or status update has been logged in the provided thread since the latest generation. The team should prioritize this P4 incident based on the 100% anomalous rate observed over the last 15 minutes.


## [3/50] Trivy compromise & LiteLLM infected
Source: gmail | Thread: 19d2d713065f8bdf | Labels: Inbox, Forums | Priority: None | Senders: 'Nicholas Tan' via . | Last Date: Fri, Mar 27, 2026, 3:58 AM | Last Updated: 2026-03-27T06:02:28.516503+00:00
**Executive Briefing: Trivy & LiteLLM Supply Chain Compromise**

**Key Participants & Roles**
*   **Nicholas Tan (Platform Team):** Issuer of the security advisory and lead coordinator for immediate remediation.
*   **Forensic Team:** Tasked with analyzing terminal outputs to verify compromised versions.
*   **Tech Infra & CyberSecurity Teams:** Collaborating on code search indicators and broader investigation.
*   **General Staff/Developers:** Target audience required to execute local verification steps.

**Main Topic & Request**
A critical security advisory regarding the compromise of **Trivy v0.69.4**, a popular open-source security scanner. This compromise has led to the distribution of an infected version of **LiteLLM** (versions 1.82.7 and 1.82.8) via the Trivy packaging process.
*   **Risk:** Potential exfiltration of local credentials (files or environment variables) to malicious endpoints.
*   **Request:** Immediate verification of installed versions and isolation/remediation if compromised.

**Pending Actions & Ownership**
1.  **Local Verification (All Staff):**
    *   Run `command -v trivy`.
    *   If Trivy is present, run `trivy --version`. Output must be sent to the Platform Team for forensic inspection.
    *   Check LiteLLM versions: `pip show litellm | grep Version`. Report any instances of v1.82.7 or v1.82.8.
    *   **Action:** Remove Trivy immediately via package manager if not needed, or reinstall safe version v0.69.3 (via `brew update`, `uninstall`, `install`).
2.  **Infrastructure Scanning (Platform Team):**
    *   Complete analysis of clusters (nodes & pods) for Trivy-related artifacts.
    *   Status: Completed; no infected images found in clusters.
    *   Tracking: https://docs.google.com/spreadsheets/d/1zZ05TeGQq49T9CCia4m5SqKSilX7UOKcyKikpiHaXi8/edit?gid=0#gid=0
3.  **Code Search (Tech Infra & CyberSecurity):**
    *   WIP: Searching for indicators of infected packages (Trivy, LiteLLM).
    *   Tracking: https://docs.google.com/spreadsheets/d/17bB4F2GR62rSsfQIDwm3QxeBvq3bXUGQXG5y3_GoP2M/edit?gid=172681731#gid=172681731

**Decisions Made**
*   **Discontinuation of v0.69.4:** Any instance of Trivy v0.69.4 is deemed compromised and requires forensic review or removal.
*   **Safe Version Protocol:** If Trivy usage is required, the organization mandates a hard reset to version **v0.69.3** using Homebrew (`brew update`, `uninstall trivy`, `install trivy`).

**Key Dates & Follow-ups**
*   **Date of Advisory:** March 27, 2026 (3:58 AM).
*   **Critical Deadline:** Immediate action required. Users must report findings to the Platform Team immediately upon detection of compromised versions.
*   **References for Context:**
    *   Wiz.io Blog: Trivy Compromise (https://www.wiz.io/blog/trivy-compromised-teampcp-supply-chain-attack)
    *   Wiz.io Blog: LiteLLM Trojanization (https://www.wiz.io/blog/threes-a-crowd-teampcp-trojanizes-litellm-in-continuation-of-campaign)


## [4/50] Canceled event with note: [Virtual] Smart Cart x RMN Catchup @ Fri Mar 27, 2026 4pm - 4:30pm (SGT) (Michael Bui)
Source: gmail | Thread: 19d2d6e904472726 | Labels: Inbox | Priority: None | Senders: Ching Hui Ng | Last Date: Fri, Mar 27, 2026, 3:55 AM | Last Updated: 2026-03-27T06:02:39.646394+00:00
**Daily Work Briefing: [Virtual] Smart Cart x RMN Catchup Cancellation**

**Key Participants & Roles:**
*   **Ching Hui Ng** (`chinghui.ng@fairpricegroup.sg`): Initiator of the cancellation and primary stakeholder raising strategic inquiries.
*   **Nikhil**: Recipient of the inquiry (email address not provided in thread).
*   **Michael Bui**: Organizer/Resource holder; email address not provided in thread.

**Main Topic/Request:**
Ching Hui Ng requested a detailed roadmap for "Osmo" and sought clarification on how Osmo can be integrated with "Smart Cart." This request was intended to be addressed during the scheduled catch-up session.

**Pending Actions & Ownership:**
*   **Action**: Provide the Osmo roadmap and explain Smart Cart integration capabilities.
    *   **Owner**: Nikhil and Michael Bui (implied recipients).
*   **Status**: The meeting required to discuss this has been canceled; actions remain outstanding pending rescheduling.

**Decisions Made:**
*   The event scheduled for March 27, 2026, was officially **canceled** and removed from the calendar by Ching Hui Ng.
*   A specific note was added to the cancelled event stating: **"To revisit."**
*   No new date or time was set during this interaction; a follow-up discussion is required.

**Key Dates & Follow-ups:**
*   **Original Event Date/Time**: Friday, March 27, 2026, from 4:00 PM to 4:30 PM (SGT).
*   **Cancellation Notification Time**: March 27, 2026, at 3:55 AM.
*   **Meeting Link**: `meet.google.com/bjp-ywfj-viu` (No longer active due to cancellation).
*   **Next Steps**: The team must coordinate with Ching Hui Ng to reschedule the discussion regarding the Osmo roadmap and Smart Cart integration, adhering to the "To revisit" instruction.


## [5/50] Re: [Bitbucket] Pull request #919: chore/omni ops monitor (ntuclink/dpd-datadog-monitoring)
Source: gmail | Thread: 19d2d6690d21cc23 | Labels: Inbox, Updates | Priority: None | Senders: Sundy Yaputra | Last Date: Fri, Mar 27, 2026, 3:46 AM | Last Updated: 2026-03-27T06:02:53.551152+00:00
**Daily Work Briefing: Pull Request #919 Summary**

**Key Participants & Roles**
*   **Sundy Yaputra**: Author and primary contributor. Responsible for executing code changes, refactoring monitoring logic, and restructuring service locations within the `ntuclink/dpd-datadog-monitoring` repository.

**Main Topic/Request**
The thread concerns Pull Request #919 titled "chore/omni ops monitor." The objective is to reorganize Datadog monitoring configurations for the DPD Omni-Ops team. This involves moving existing services, separating logic into specific SLO (Service Level Objective) and monitor files, and establishing a dedicated folder structure for these operations.

**Actions Pending & Ownership**
*   **Review/Merge**: No explicit approval or rejection is noted in this email thread update. The PR remains open for review by the team.
    *   *Owner*: Not specified (Default: Reviewers assigned to the repository).
*   **Monitoring Implementation**: Sundy Yaputra has completed the code changes required to divide logic into SLOs and monitors and relocate services.
    *   *Owner*: Sundy Yaputra (Status: Complete/Submitted).

**Decisions Made**
No formal business decisions (e.g., budget approval, timeline extension) are recorded in this update. The technical decision documented is the architectural restructuring of the monitoring codebase as evidenced by the commit history:
1.  **Modularization**: Separation of logic into SLO and monitor components (Commit `95926a5`).
2.  **Service Relocation**: Movement of services to align with the DPD Omni-Ops team structure (Commit `14f6ab2`).
3.  **Directory Restructure**: Copying monitors specifically to the "omni ops folder" (Commit `fb483c9`).

**Key Dates & Follow-ups**
*   **Last Activity Date**: March 27, 2026.
*   **Activity Time**: 3:46 AM UTC.
*   **Latest Commit ID**: `14f6ab2` (and preceding commits).
*   **Next Steps**: The thread indicates the PR has been updated with new commits. The implicit next step is for stakeholders to review these changes within Bitbucket and provide feedback or merge approval. No specific deadline was set in this notification.

**Reference Data**
*   **Repository**: `ntuclink/dpd-datadog-monitoring`
*   **Pull Request ID**: #919
*   **Branch/Topic**: `chore/omni ops monitor`
*   **Message ID**: `19d2d6690d21cc23`


## [6/50] [Dashboard Report] Retail Media - DD Dashboard | Fri 27 Mar 11:00AM +08
Source: gmail | Thread: 19d2d3eb8bab7659 | Labels: Inbox, Updates | Priority: None | Senders: Datadog HQ | Last Date: Fri, Mar 27, 2026, 3:02 AM | Last Updated: 2026-03-27T06:03:04.555523+00:00
**Subject:** Daily Briefing: Retail Media Datadog Dashboard Report (Mar 27)

**Key Participants & Roles**
*   **Michael:** Recipient of the report; responsible for monitoring.
*   **Datadog HQ (no-reply@dtdg.eu):** Sender/Service provider; generated and transmitted the automated report on behalf of Team Datadog.

**Main Topic & Request**
*   **Topic:** Delivery of the "Retail Media - DD Dashboard" resource.
*   **Request:** Michael is requested to review the attached dashboard containing performance data for the past three days (Mar 24–Mar 27, 2026) and proceed with standard monitoring activities.

**Pending Actions & Ownership**
*   **Action:** Review the attached report ("Retail Media - DD Dashboard") covering the last three days of data.
*   **Owner:** Michael.
*   **Status:** Report delivered; awaiting review/monitoring initiation.

**Decisions Made**
*   No strategic decisions were made in this thread; this is a routine automated data delivery notification.

**Key Dates, Deadlines, & Follow-ups**
*   **Report Generation Date:** Fri, Mar 27, 2026, at 11:00 AM +08 (Timestamped in resource header).
*   **Email Transmission Time:** Mar 27, 2026, at 3:02 AM.
*   **Data Coverage:** Past 3 days relative to the report date.
*   **Next Steps:** No specific deadline or follow-up meeting scheduled; action depends on Michael's internal monitoring schedule.

**Specific References**
*   **Resource Name:** Retail Media - DD Dashboard.
*   **Sender Address:** no-reply@dtdg.eu.
*   **Report ID/Last Message ID:** 19d2d3eb8bab7659.
*   **Datadog HQ Location:** 620 8th Avenue, 45th Floor, New York, NY 10018.


## [7/50] Safeguarding our Foundation - The new Regulatory Compliance Policy
Source: gmail | Thread: 19d2d04c30ff7501 | Labels: Inbox, Updates | Priority: None | Senders: GRC | Last Date: Fri, Mar 27, 2026, 1:59 AM | Last Updated: 2026-03-27T02:01:30.772695+00:00
**Daily Work Briefing: Regulatory Compliance Policy Update**

**Key Participants & Roles**
*   **GRC Team (Governance, Risk & Compliance):** Sender of the announcement; provides guidance and manages the compliance framework. Contact: `ask_grc@fairpricegroup.sg`.
*   **All Employees:** Mandatory recipients responsible for daily operational risk management.
*   **Direct Managers / Heads of Department:** Responsible for receiving reports of non-compliance and providing immediate guidance to staff.
*   **Subsidiaries, Vendors, and Contract Workers:** Explicitly included in the policy scope as external partners subject to these regulations.

**Main Topic & Request**
The Governance, Risk & Compliance (GRC) team has officially introduced the new **Regulatory Compliance Policy**. The primary objective is to establish a structured framework for identifying, managing, and reporting regulatory risks (specifically citing potential breaches of the PDPA and Payment Services Act) to protect FairPrice Group (FPG) from financial and reputational exposure. All employees are required to align daily processes with these new legal standards.

**Pending Actions & Ownership**
*   **Risk Management:** All Business Units and Corporate Functions must own the management of their daily operational risks to ensure alignment with regulatory standards.
*   **Incident Reporting:** Any employee suspecting an actual or impending breach must:
    1.  Promptly escalate the issue to their Direct Manager or Head of Department.
    2.  Log the incident immediately via the **FPG Incident and Crisis Report channel**.
*   **Policy Adherence:** All staff must read and adhere to these mandatory requirements.

**Decisions Made**
*   The new Regulatory Compliance Policy is now active and applies universally across FPG, including all subsidiaries and external partners.
*   Transparency in reporting non-compliance has been mandated as a core cultural requirement.
*   A formal escalation path and incident logging channel have been designated as the sole mechanisms for reporting breaches.

**Key Dates & Follow-ups**
*   **Announcement Date:** March 27, 2026 (1:59 AM).
*   **Effective Action:** Immediate compliance is required regarding risk identification and incident reporting.
*   **Guidance Contact:** For doubts or clarification, contact `ask_grc@fairpricegroup.sg` or the relevant Direct Manager/Reporting Officer.


## [8/50] You have no events scheduled today.
Source: gmail | Thread: 19d2c11f1c0487ef | Labels: Inbox, Updates | Priority: None | Senders: Google Calendar | Last Date: Thu, Mar 26, 2026, 9:34 PM | Last Updated: 2026-03-26T22:01:21.544265+00:00
**Daily Work Briefing Summary**

**Key Participants & Roles:**
*   **Michael Bui** (Recipient/Account Owner): michael.bui@fairpricegroup.sg. Primary stakeholder for the Digital Business Tech Release/Changes calendar notifications.
*   **Google Calendar System**: Automated notification sender (calendar-notification@google.com).

**Main Topic/Request:**
*   Notification of daily agenda status regarding the "Digital Business Tech Release/Changes" calendar subscription. The system confirms that no schedule conflicts or events are recorded for the specified date.

**Pending Actions & Ownership:**
*   **Status Check**: No actions required by Michael Bui today as there are no scheduled events.
*   **Subscription Management (Optional)**: If Michael Bui wishes to modify which calendars receive daily agendas, he must manually log in to https://calendar.google.com/calendar/ to adjust notification settings for specific calendars.

**Decisions Made:**
*   None. This is an automated status update confirming a null result (no events).

**Key Dates & Deadlines:**
*   **Notification Date**: Mar 26, 2026, at 9:34 PM.
*   **Scope Date**: Fri Mar 27, 2026.
*   **Event Status**: No events scheduled for the scope date.

**Additional Details:**
*   **Primary Calendar Subscription**: Digital Business Tech Release/Changes.
*   **Message Metadata**: Labeled as "Inbox" and "Updates"; Priority set to null; Last message ID: 19d2c11f1c0487ef.
*   **Confidentiality Notice**: The email body contains a standard confidentiality disclaimer stating the content may be privileged.


## [9/50] It's raining new Jira updates!
Source: gmail | Thread: 19d2b32183edc65e | Labels: Inbox, Updates | Priority: None | Senders: Atlassian | Last Date: Thu, Mar 26, 2026, 5:29 PM | Last Updated: 2026-03-26T22:01:36.067468+00:00
**Daily Work Briefing: Jira Product Updates & Events**

**1. Key Participants & Roles**
*   **Sender:** Atlassian (info@e.atlassian.com) – Product updates and announcements.
*   **Featured Speakers/Leaders:**
    *   Emily Ditchfield (Confluence Whiteboards PM).
    *   Adam Grant (Guest speaker for upcoming summit).
    *   NVIDIA Director of Product and Engineering.
    *   Atlassian Rovo AI team members.

**2. Main Topic**
Monthly update covering the March 2026 Jira release cycle, focusing on new AI capabilities ("Agents in Jira," "Rovo Dev"), seasonal planning experiences, integrations with Loom and VS Code, and upcoming community events.

**3. Pending Actions & Ownership**
*   **Review Agents in Jira (Open Beta):** Evaluate assigning work to agents and triggering them via workflows for drafting/summarizing tasks. *Owner: Engineering/Product Teams.*
*   **Evaluate Rovo Dev:** Test the new VS Code extension for AI-assisted development with Atlassian context. *Owner: Development Teams.*
*   **Explore Nonprofit Offer:** Assess eligibility for the 100% off Teamwork Collection (up to 25 users) if applicable. *Owner: Procurement/Management.*

**4. Decisions Made**
*   None recorded in this communication thread; this is a broadcast informational update from Atlassian regarding feature releases and event invitations.

**5. Key Dates, Deadlines & Follow-ups**
*   **March 26, 2026:** Webinar "Rovo Dev ships the small tasks while you tackle the cool stuff" (Registration open).
*   **March 31, 2026:** Global digital summit "Teamwork in an AI era" featuring Adam Grant and NVIDIA leadership.
*   **Ongoing:** Visit the new seasonal release hub to track centralized updates.
*   **Future:** Jira Agents are currently in Open Beta; monitoring for broader availability is required.

**Summary of New Features:**
*   **Agents in Jira:** Assign work, @mention agents, and trigger workflows for execution.
*   **Seasonal Releases:** Centralized hub for "What's New" content.
*   **Rovo Dev (GA):** Integrated into VS Code for code-aware assistance using Atlassian context.
*   **Jira + Loom Integration:** Enhanced bug reporting mode and AI-suggested work item updates from recordings.


## [10/50] [JIRA] (DPD-383) Sales posting for BCRS deposit amount
Source: gmail | Thread: 19c0dd2af26388b0 | Labels: Inbox, Updates | Priority: None | Senders: Prajney | Last Date: Thu, Mar 26, 2026, 2:47 PM | Last Updated: 2026-03-26T22:01:56.627400+00:00
**Daily Briefing: JIRA DPD-383 – Sales posting for BCRS deposit amount**

**Key Participants & Roles**
*   **Michael Bui:** Developer/Lead. Responsible for implementation, SAP integration logic, and deployment verification.
*   **Prajney Sribhashyam:** Product/Business Analyst. Defined requirements, Acceptance Criteria (AC), and use cases (E-Comm, Marketplace, Returns).
*   **Daryl Ng:** Stakeholder. Set initial timeline and due dates.
*   **Yatlian Wee / SAP Team:** Provided clarification on AR line aggregation and posting structure.

**Main Topic/Request**
Implementation of a service to calculate and post BCRS (Bottle Deposit) amounts collected from customers at the order line level to SAP. The solution must handle E-Comm, Marketplace, Returns, Refunds, Donation orders, and FOC items.

**Decisions Made**
1.  **Trigger Logic:** Only `COMPLETED` orders are processed for deposit posting; `PENDING` PFC and non-Fulfillment orders are ignored. OFFLINE and RB PreOrder channels are excluded.
2.  **Data Source:** Deposit price is fetched dynamically from the Inventory Service, not hard-coded. Material numbers are retrieved via BigQuery/SAP integration (using SAP Material Number instead of DBP SKU).
3.  **Posting Structure:** Aggregated to a single Accounts Receivable (AR) line item per billing document (merging Marketplace and own-SKU amounts). Individual GL lines remain by SKU.
4.  **Technical Fix:** GCP PubSub "Delivery Once" policy enabled to prevent duplicate postings due to default at-least-once delivery semantics.

**Pending Actions & Owners**
*   **Status:** **DEPLOYED TO PRODUCTION (PRD)**. Verified with no observed issues.
*   **Action:** Monitor for actual BCRS orders to execute live SAP postings. While the deployment is stable, SAP access in PRD is pending validation against real-world deposit transactions.

**Key Dates & Timeline**
*   **Timeline Target:** Development completion by Feb 20, 2026 (achieved); Technical Go-Live targeted for Mar 2, 2026.
*   **Feb 10:** Task created; Due date extended to Feb 18.
*   **Feb 13-14:** Acceptance Criteria alignment and refinement regarding Inventory Service data usage and SKU aggregation.
*   **Feb 16:** Blocked by dependency on PLU Processor (DPD-551) for SAP Material Number; SAP access request submitted (NED-275153).
*   **Feb 20:** Development complete; blocked by SAP access.
*   **Feb 22:** Successfully posted to SAP DER/QER environments in Preproduction.
*   **Feb 23:** Confirmed successful payload and error handling logic with SAP side.
*   **Mar 4:** New discovery regarding `freeItems` field for FOC items identified.
*   **Mar 6:** Duplicate posting issue resolved via PubSub configuration update (PR #1033).
*   **Mar 26, 2:47 PM:** Deployed to PRD; observed and verified with no issues.

**References**
*   SAP Access Request: NED-275153
*   Postman Setup Guide & Chat Room links available in thread.
*   Sample Order ID: 75412611.
*   Deployment Verification: Image attachment (image-20260326-143621.png) posted by Michael Bui on Mar 26, 2026.


## [11/50] March 2026 Google Cloud on Coursera Newsletter
Source: gmail | Thread: 19d2a3af8e725b68 | Labels: Inbox, Updates | Priority: None | Senders: no-r...@...l.coursera.org | Last Date: Thu, Mar 26, 2026, 1:00 PM | Last Updated: 2026-03-26T22:02:13.777741+00:00
### Daily Work Briefing: March 2026 Google Cloud on Coursera Newsletter

**Key Participants & Roles**
*   **Google Cloud (Sender):** Providing official updates, learning resources, and webinar invitations via `no-reply@m.mail.coursera.org`.
*   **Recipients:** Professionals seeking cloud certification and upskilling (No specific individual names listed; audience is the general newsletter subscriber base).

**Main Topic/Request**
The email serves as the March 2026 edition of the "Google Cloud on Coursera" newsletter. It outlines key learning opportunities, specifically highlighting a new webinar for the **Cloud Digital Leader Exam** and listing newly available or localized training specializations in Generative AI, infrastructure, and application development across multiple languages (English, Deutsch, Indonesian, 日本語，Português, Français, 한국어, Español, 简体中文，繁體中文).

**Pending Actions & Ownership**
*   **Action:** Register for the "Take the Lead: Your Guide to Mastering the Cloud Digital Leader Exam" webinar.
    *   **Owner:** Recipients (via "Save your spot here" link).
    *   **Benefit:** Includes a discount voucher for the exam.
*   **Action:** Review and enroll in new learning content, including the "[New!] Build and Modernize Applications With Generative AI [Specialization]" and various localized courses.
    *   **Owner:** Recipients.

**Decisions Made**
No internal business decisions were made within this communication; it is a distribution of educational resources and event invitations.

**Key Dates & Deadlines**
*   **March 25, 2026, 8:00 am Pacific / 11:00 am Eastern:** The scheduled time for the Cloud Digital Leader Exam webinar (sent March 26, 2026). *Note: The event date listed in the content is prior to the newsletter send date.*
*   **March 2026:** Current context for wrapping up Q1 and establishing professional growth milestones.

**Specific References & Content Highlights**
*   **Certification Focus:** Cloud Digital Leader (no technical background required).
*   **New Specialization:** Build and Modernize Applications With Generative AI (English).
*   **Localized Content Updates:**
    *   Deutsch: Deploy and Scale AI Models with Cloud Run; Essential Google Cloud Infrastructure: Core Services.
    *   Indonesian: Deploy and Scale AI Models with Cloud Run.
    *   日本語：Select a Google Cloud Database for Your Applications; Service Orchestration and Choreography on Google Cloud.
    *   Português: Select a Google Cloud Database for Your Applications; Developing Containerized Applications on Google Cloud; Accelerate App Development with Gemini CLI.
    *   Français: Select a Google Cloud Database for Your Applications; Developing Containerized Applications on Google Cloud; Service Orchestration and Choreography on Google Cloud; Accelerate App Development with Gemini CLI.
    *   한국어：Developing Containerized Applications on Google Cloud; AI Infrastructure: Cloud GPUs.
    *   Español: Developing Containerized Applications on Google Cloud; Service Orchestration and Choreography on Google Cloud; Accelerate App Development with Gemini CLI.
    *   简体中文/繁體中文：Accelerate App Development with Gemini CLI; AI Infrastructure: Cloud GPUs (Traditional).


## [12/50] DOS: Don't Wait for a Special Season - Give with Purpose Today!
Source: gmail | Thread: 19d295fbcda1be58 | Labels: Inbox, Promotions | Priority: None | Senders: Day of Service | Last Date: Thu, Mar 26, 2026, 9:00 AM | Last Updated: 2026-03-26T22:02:24.725070+00:00
**Daily Work Briefing: Day of Service Initiative**

**Key Participants & Roles**
*   **Sender:** CSR Team (fairprice.com.sg) representing "Day of Service."
*   **Recipient Audience:** FPG colleagues, referred to as "Fairmily."
*   **Beneficiaries:** Seniors and community members receiving support.

**Main Topic/Request**
The email solicits immediate volunteer participation for the "Day of Service" initiative. The core message emphasizes that volunteering should not be reserved for special seasons but can occur through everyday actions. Specific examples of past impact include preparing 3,000 nutritious meals, celebrating Easter with seniors, and assisting beneficiaries with daily essentials.

**Pending Actions & Ownership**
*   **Action:** Explore upcoming volunteer opportunities via the provided link (image).
    *   **Owner:** FPG colleagues ("Fairmily").
*   **Action:** Contact the CSR team for clarification on specific locations or roles if needed.
    *   **Owner:** Interested FPG colleagues.
    *   **Contact Channel:** csr@fairprice.com.sg.

**Decisions Made**
No formal decisions were recorded in this thread; the communication is an informational solicitation inviting participation rather than reporting on a concluded decision-making process.

**Key Dates, Deadlines, and Follow-ups**
*   **Sent Date:** March 26, 2026, at 9:00 AM.
*   **Immediate Action Required:** Volunteers are encouraged to "explore upcoming volunteer opportunities today."
*   **Future Outlook:** The initiative describes ongoing activities (e.g., meal preparation, senior support) rather than a single fixed deadline, urging colleagues to act now ("Give with Purpose Today").

**Specific References & Data Points**
*   **Subject/Resource Title:** "DOS: Don't Wait for a Special Season - Give with Purpose Today!"
*   **Email Address:** csr@fairprice.com.sg
*   **Impact Metrics:** 3,000 nutritious meals prepared in previous initiatives.
*   **Volunteer Time Commitment Options:** Two hours or half a day.


## [13/50] Notes: “BCRS Regroup - Open Item Planning” Mar 26, 2026
Source: gmail | Thread: 19d295faa30a0ec9 | Labels: Inbox | Priority: None | Senders: Gemini | Last Date: Thu, Mar 26, 2026, 9:00 AM | Last Updated: 2026-03-26T22:02:40.668471+00:00
**Daily Work Briefing: BCRS Regroup - Open Item Planning**
**Date:** March 26, 2026
**Source:** Meeting Notes (Auto-generated by Gemini)

**Key Participants & Roles**
*   **Dany Jacob:** Code implementation lead.
*   **Sathya Murthy Karthik:** Support coordination and testing confirmation lead.
*   **Wai Ching Chan:** Configuration management, UAT status tracking, and FOC issue investigation.
*   **Emerald/Business Team:** Stakeholders required to confirm pre-order testing necessity.
*   **Daryl:** Technical support provider for Dany Jacob.
*   **External Team:** Conducting Scan and Go UAT testing.

**Main Topic/Request**
The meeting focused on resolving critical blockers for the April 1st BC go-live, specifically regarding **Refund SKU and container deposit implementation**, **Scan and Go testing status**, and a technical defect where deposits are not charging on Free of Charge (FOC) items due to POS omission of $0 value items.

**Decisions Made**
*   The team confirmed that refund SKU and container deposit details can be retrieved from the order detail SKU.
*   Deployment timelines were prioritized to allow immediate testing, as Finance is currently blocking sign-off on returns/refunds.
*   It was identified that a solution for FOC items requires investigation into whether the existing $0.01 dummy SKU setup needs modification since the POS omits $0 value items.

**Pending Actions & Owners**
*   **Dany Jacob:** Deploy code changes to the UAT environment by tomorrow morning (March 27, 2026).
*   **Sathya Murthy Karthik:** Secure support from Daryl for Dany Jacob and close out this task ASAP.
*   **Sathya Murthy Karthik:** Confirm with Emerald or the Business Team whether pre-order testing is necessary.
*   **Wai Ching Chan:** Request a status update and expected completion date from the UAT team regarding ongoing Scan and Go testing.
*   **Wai Ching Chan:** Implement necessary back-office configuration changes for the production environment.
*   **Wai Ching Chan:** Investigate the FOC deposit issue thread to determine how to handle deposit SKUs against zero-dollar items.
*   **Someone in L12 Room 4 (FairPrice Hub, 12):** Gather data team members into a chat and provide a heads-up regarding readiness for tomorrow morning testing.

**Key Dates & Deadlines**
*   **March 27, 2026 (Tomorrow Morning):** Deadline for Dany Jacob to deploy code to UAT; deadline for Data Team readiness check.
*   **April 1, 2026:** Target BC go-live date (current Finance block on returns/refunds poses a risk).
*   **Ongoing:** External team Scan and Go testing began Monday (March 23) in UAT; deployment awaits their completion.


## [14/50] [JIRA] Wai Ching Chan mentioned you on DPD-807
Source: gmail | Thread: 19d2955e3e3a835e | Labels: Inbox, Updates | Priority: None | Senders: Wai Ching Chan (Jir. | Last Date: Thu, Mar 26, 2026, 8:49 AM | Last Updated: 2026-03-26T22:02:53.768290+00:00
**Daily Work Briefing: DPD-807 Notification**

**1. Key Participants & Roles**
*   **Wai Ching Chan:** Jira User/Reporter; Identified as the initiator of the task notification.
*   **Michael Bui (You):** The assignee/receiver of the instruction; responsible for executing the technical update.
*   **System:** NTU Clink / FairPrice UAT environments acting as the execution target.

**2. Main Topic/Request**
The email addresses a specific technical requirement regarding Jira work item **DPD-807**: **"Charge BCRS deposit for re-delivery"**. The objective is to manually update the system metadata to reflect that a deposit has been successfully posted to SAP for delivery order **75588070**.

**3. Pending Actions & Ownership**
*   **Action:** Execute a `curl` PUT request to update the delivery order metadata in the UAT environment.
    *   **Endpoint:** `https://api.zs-uat.fairprice.com.sg/order-service/v3/deliveryOrders/75588070`
    *   **Payload Requirement:** Set `"metadata": { "Deposit posted to SAP": true }` and enable `"updateAction": ["UPDATE_ACTION_UPDATE_METADATA"]`.
*   **Owner:** Michael Bui.

**4. Decisions Made**
No strategic decisions were made in this thread. The communication confirms the requirement that the specific metadata flag (`Deposit posted to SAP`) must be toggled to `true` for order `75588070`. A reference link to the customer support view is provided at `https://admin-uat.fairprice.com.sg/customer-support/delivery-orders/75588070`.

**5. Key Dates & Follow-ups**
*   **Date:** March 26, 2026
*   **Time:** 8:49 AM (Notification timestamp) / 4:49 PM Singapore Time (Wai Ching Chan's action time).
*   **Follow-up:** Immediate execution of the provided `curl` command is required to close the update loop. No future deadline was specified beyond the immediate request context.

**6. Specific References**
*   **Jira ID:** DPD-807 (Ecom/Omni category).
*   **Order ID:** 75588070.
*   **Environment:** UAT (`api.zs-uat.fairprice.com.sg`, `admin-uat.fairprice.com.sg`).


## [15/50] New event: Michael On Leave @ Sat 28 Mar - Sun 5 Apr 2026 (CPD Team Calendar)
Source: gmail | Thread: 19d29498c1a3f9dc | Labels: None | Priority: None | Senders: me | Last Date: Thu, Mar 26, 2026, 8:36 AM | Last Updated: 2026-03-26T22:03:05.425124+00:00
**Daily Work Briefing: Calendar Notification Summary**

**Key Participants & Roles**
*   **Michael Bui** (`michael.bui@fairpricegroup.sg`): Event Organizer. The email indicates he is the subject of the leave event ("Michael On Leave").
*   **CPD Team**: Collective attendees/observers subscribed to the "CPD Team Calendar" receiving this notification.

**Main Topic/Request**
*   Automated system notification regarding a scheduled absence for Michael Bui.
*   The event title is explicitly defined as: **"New event: Michael On Leave @ Sat 28 Mar - Sun 5 Apr 2026"**.
*   The invitation was generated via Google Calendar and distributed to the CPD Team Calendar subscription list.

**Pending Actions & Ownership**
*   **No specific human actions are required** in this automated notification thread.
*   Recipients are instructed via the footer that forwarding the email allows them to modify the guest list or RSVP; however, no such action has been initiated by any recipient as of the last message timestamp.

**Decisions Made**
*   No new decisions were made during this specific communication exchange. The content reflects a pre-existing calendar entry notification rather than a discussion requiring consensus.

**Key Dates & Deadlines**
*   **Event Start Date:** Saturday, 28 March 2026.
*   **Event End Date:** Sunday, 5 April 2026.
*   **Notification Timestamp:** Wednesday, 26 March 2026, at 8:36 AM.
*   **Last Message ID:** `19d29498c1a3f9dc`.

**Specific References**
*   **Calendar System:** Google Calendar (CPD Team Calendar).
*   **Domain:** FairPrice Group (`@fairpricegroup.sg`).
*   **Confidentiality Notice:** The email body includes a standard legal disclaimer stating the message is "confidential and may also be privileged."

*Summary Note: This thread serves as an informational alert to the CPD Team regarding Michael Bui's upcoming two-week leave period in Q2 2026. No immediate follow-up is required unless operational coverage planning has already been triggered by this calendar block.*


## [16/50] New event: Michael On Leave @ Sat Mar 28 - Sun Apr 5, 2026 (CPD Team Calendar)
Source: gmail | Thread: 19d29498c065d410 | Labels: None | Priority: None | Senders: me | Last Date: Thu, Mar 26, 2026, 8:36 AM | Last Updated: 2026-03-26T22:03:15.876799+00:00
**Daily Work Briefing: Calendar Notification Summary**

**1. Key Participants & Roles**
*   **Organizer/Subject:** Michael Bui (`michael.bui@fairpricegroup.sg`)
*   **Audience:** Subscribers to the CPD Team Calendar (automated notification recipients).
*   **System:** Google Calendar infrastructure handling automated notifications and RSVP permissions.

**2. Main Topic/Request**
The email is an automated system notification regarding a scheduled event titled **"Michael On Leave."** It serves as an official calendar invitation alerting team members to the organizer's unavailability during the specified period. The content includes standard security disclaimers regarding forwarding confidentiality and details on how recipients can manage their subscription settings or permission levels.

**3. Pending Actions & Ownership**
*   **No manual actions required:** This is a read-only system notification generated by Google Calendar.
*   **Optional Management (Recipient-owned):** Subscribers may choose to stop receiving these notifications by navigating to Calendar settings, selecting the "CPD Team Calendar," and adjusting "Other notifications."
*   **RSVP/Permissions:** While the email notes that forwarding allows recipients to modify RSVPs or invite others, no specific action has been requested of the current recipients in this thread.

**4. Decisions Made**
*   Michael Bui has officially blocked out his schedule for leave from **Saturday, March 28, 2026**, through **Sunday, April 5, 2026**.
*   The CPD Team Calendar has been updated to reflect this unavailability.

**5. Key Dates & Deadlines**
*   **Event Start:** Saturday, March 28, 2026
*   **Event End:** Sunday, April 5, 2026
*   **Notification Date:** March 26, 2026, at 8:36 AM

**Note:** This summary is derived solely from the automated calendar notification provided. No further discussion or decision-making thread was present in the source content.


## [17/50] Declined: BCRS Regroup - Open Item Planning @ Thu Mar 26, 2026 4pm - 5pm (SGT) (Prajney Sribhashyam)
Source: gmail | Thread: 19d2908490bc9a1f | Labels: None | Priority: None | Senders: me | Last Date: Thu, Mar 26, 2026, 7:25 AM | Last Updated: 2026-03-26T22:03:29.134987+00:00
**Daily Work Briefing: BCRS Regroup Meeting Status**

**1. Key Participants & Roles**
*   **Organizer:** Prajney Sribhashyam
*   **Attendees:**
    *   Michael Bui (Declined)
    *   Sathya Murthy Karthik
    *   Daryl Ng
    *   Akash Gupta
    *   De Wei Tey
    *   Wai Ching Chan
    *   Zaw Myo Htet
*   **Optional Attendee:** Koklin Gan

**2. Main Topic/Request**
*   **Subject:** BCRS Regroup - Open Item Planning.
*   **Purpose:** Planning session for open items within the BCRS project.
*   **Meeting Details:** Scheduled for Thursday, March 26, 2026, from 4:00 PM to 5:00 PM (SGT).
*   **Location:** FairPrice Hub-12-L12 Room 4 (6) [Google Meet].

**3. Pending Actions & Ownership**
*   **Action:** Reschedule the meeting due to Michael Bui's unavailability.
*   **Owner:** Prajney Sribhashyam (Organizer).
*   **Context:** Michael Bui declined the invitation citing a "Meeting clash." No new time has been proposed in the current thread; the organizer must coordinate a new slot with the team, specifically ensuring Michael Bui's availability.

**4. Decisions Made**
*   **Status:** The meeting for March 26, 2026, at 4:00 PM SGT is effectively cancelled for Michael Bui pending rescheduling. No final decision on a new time was recorded in this thread snippet; the current status remains "Declined."

**5. Key Dates & Follow-ups**
*   **Original Date/Time:** Thursday, March 26, 2026 | 4:00 PM – 5:00 PM (SGT).
*   **Follow-up Required:** Immediate coordination by Prajney Sribhashyam to find an alternative time slot that accommodates Michael Bui.

**6. Contact Information & References**
*   **Michael Bui Email:** michael.bui@fairpricegroup.sg
*   **Meeting Link:** meet.google.com/gbg-fuft-uzq
*   **Phone Access (US):** +1 574-313-1033 | PIN: 366674343


## [18/50] Updated invitation: BCRS Regroup - Open Item Planning @ Thu Mar 26, 2026 4pm - 5pm (SGT) (Michael Bui)
Source: gmail | Thread: 19d2907bbd65bcc6 | Labels: Inbox | Priority: None | Senders: Prajney Sribhashyam | Last Date: Thu, Mar 26, 2026, 7:24 AM | Last Updated: 2026-03-26T22:03:41.149030+00:00
**Daily Work Briefing: BCRS Regroup – Open Item Planning**

**1. Key Participants & Roles**
*   **Organizer:** Prajney Sribhashyam (prajney.sribhashyam@fairpricegroup.sg)
*   **Confirmed/Noted Attendees:** Sathya Murthy Karthik, Daryl Ng, Akash Gupta, Michael Bui, De Wei Tey, Wai Ching Chan, Zaw Myo Htet.
*   **Optional Guest:** Koklin Gan.

**2. Main Topic/Request**
The session is an "Open Item Planning" meeting for the BCRS Regroup initiative. The primary purpose of this communication is to disseminate an updated calendar invitation containing revised location and access details for the scheduled discussion.

**3. Pending Actions & Ownership**
*   **Action:** RSVP to the updated meeting invitation (Yes/No/Maybe).
    *   **Owner:** All invited guests, specifically including Michael Bui (michael.bui@fairpricegroup.sg) as per the reply prompt context.
*   **Action:** Join the session via Google Meet or phone conference at the specified time.
    *   **Owner:** All attendees.

**4. Decisions Made**
*   No strategic decisions are recorded in this thread; the update reflects a logistical change regarding the meeting venue.

**5. Key Dates, Deadlines & Follow-ups**
*   **Event Date/Time:** Thursday, March 26, 2026, from 4:00 PM to 5:00 PM (Singapore Standard Time).
*   **Updated Location:** FairPrice Hub-12-L12 Room 4 (6) [Google Meet].
    *   *Note:* The location field was explicitly marked as "CHANGED" in the notification.
*   **Virtual Access Details:**
    *   **Google Meet Link:** meet.google.com/gbg-fuft-uzq
    *   **Phone Dial-in:** (US) +1 574-313-1033 | PIN: 366674343.
*   **Follow-up:** Attendees must verify the new physical room assignment prior to the meeting time.


## [19/50] Opsgenie Alert: [Datadog] [P4] [Triggered] Service marketing-service has an abnormal change in throughput on env:prod
Source: gmail | Thread: 19d28c94b778fa51 | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Thu, Mar 26, 2026, 6:21 AM | Last Updated: 2026-03-26T22:03:55.937269+00:00
**Daily Work Briefing: Opsgenie Alert Summary**

**Key Participants & Roles**
*   **System:** Opsgenie (Alerting Platform), Datadog (Monitoring Source).
*   **Responders/On-call Team:** "DPD Staff Excellence - Retail Media" team (specifically notified via `@hangouts-dd-dpd-grocery-alert` and `@opsgenie-dpd-grocery-retail-media`).
*   **Managed Service:** `marketing-service` in the `fpon-cluster` (Kubernetes environment).

**Main Topic/Request**
An automated P4 alert was triggered regarding an abnormal throughput change for the `marketing-service` in the production (`env:prod`) environment. The anomaly detection system identified that 100% of HTTP request hit values deviated by more than 3 standard deviations from predicted values over a 15-minute window.

**Pending Actions & Ownership**
*   **Investigation Required:** The on-call team must immediately investigate the cause of the throughput spike/drop.
*   **Ownership:** "DPD Staff Excellence - Retail Media" (assigned responders).
*   **Required Checks:**
    1.  Review Datadog APM metrics: [Marketing Service HTTP Request](https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod)
    2.  Review Kubernetes deployment status: [GKE Marketing Service Overview](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview?cloudshell=false&project=fponprd)
    3.  Execute standard troubleshooting procedures per the official runbook: [Marketing-Service Runbook](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book)

**Decisions Made**
No manual decisions were recorded in this thread. The alert generation and notification routing to the specific responder groups are automated system actions based on configured monitors.

**Key Dates, Deadlines & Follow-ups**
*   **Alert Trigger Time:** March 26, 2026, at 06:15:10 UTC (Last Updated).
*   **Opsgenie Notification Time:** March 26, 2026, at 06:16 AM and a duplicate notification at 06:21 AM.
*   **Metric Window Affected:** Last 15 minutes prior to the alert.
*   **Monitor ID:** `17447110` (Datadog).
*   **Follow-up Status:** Pending investigation by the Retail Media team. No closure or resolution timestamp is present in the current thread.


## [20/50] Invitation: BCRS Regroup - Open Item Planning @ Thu Mar 26, 2026 4pm - 5pm (SGT) (Michael Bui)
Source: gmail | Thread: 19d288af3d43dd36 | Labels: Inbox | Priority: None | Senders: Daryl Ng | Last Date: Thu, Mar 26, 2026, 5:08 AM | Last Updated: 2026-03-26T06:01:34.958053+00:00
**Daily Work Briefing: BCRS Regroup – Open Item Planning**

**1. Key Participants & Roles**
*   **Organizer:** Prajney Sribhashyam (FairPrice Group)
*   **Confirmed Attendees:** Sathya Murthy Karthik, Daryl Ng (daryl.ng@fairpricegroup.sg), Akash Gupta, Michael Bui (michael.bui@fairpricegroup.sg).
*   **Optional Attendee:** Koklin Gan.

**2. Main Topic/Request**
The meeting focuses on **"BCRS Regroup - Open Item Planning."** The objective is to review and plan outstanding items within the BCRS framework.

**3. Pending Actions & Ownership**
*   **Action:** Review "Open Items" (specific details not listed in this thread) during the scheduled session.
*   **Ownership:** Collective responsibility of the attendee group; execution leads to be determined during the meeting.
*   **Note:** Michael Bui has responded with a "Yes" confirmation to attend.

**4. Decisions Made**
No specific operational decisions or strategic outcomes were recorded in this thread. The primary decision made was the scheduling and confirmation of the meeting slot.

**5. Key Dates, Deadlines & Follow-ups**
*   **Meeting Date:** Thursday, March 26, 2026.
*   **Time:** 4:00 PM – 5:00 PM (Singapore Standard Time - SGT).
*   **Access Details:**
    *   **Google Meet Link:** `meet.google.com/gbg-fuft-uzq`
    *   **Phone Access (US):** +1 574-313-1033 | **PIN:** 366674343.
*   **Next Steps:** Attendees are expected to join the session as scheduled to address open items.

**Summary**
This is a standard calendar invitation and meeting reminder email for the "BCRS Regroup - Open Item Planning" session. The thread contains logistical details (time, location, RSVP status) but no substantive discussion or resolution of business issues prior to the meeting date.


## [21/50] Re: [Not Virus Scanned] Re: FairPrice Performance Marketing Meta x Osmos
Source: gmail | Thread: 19d25769187b9103 | Labels: Inbox | Priority: None | Senders: Nikhil, Gauri | Last Date: Thu, Mar 26, 2026, 5:07 AM | Last Updated: 2026-03-26T06:01:51.964662+00:00
**Daily Work Briefing: FairPrice Performance Marketing Meta x Osmos Integration Update**

**Key Participants & Roles**
*   **Nikhil Grover** (nikhil.grover@fairpricegroup.sg): Project Stakeholder – Initiated request for next steps and timeline.
*   **Gauri Salunke** (gauri.salunke@osmos.ai): Primary Point of Contact (Osmos) – Responded to inquiry regarding integration strategy.

**Main Topic & Current Status**
Following the confirmation of completed API testing on March 25, 2026, Gauri Salunke has officially responded to Nikhil Grover's request for a path forward. The project has transitioned from "waiting for guidance" to "active evaluation."

Gauri confirmed that Osmos will immediately begin evaluating the required integration changes on their end and is committed to sharing specific timelines in return. This response supersedes the previous pending status of Gauri's advice; the direction is now defined as an internal technical assessment by Osmos.

**Pending Actions & Ownership**
*   **Action**: Evaluate required integration changes internally.
    *   **Owner**: Gauri Salunke (Osmos team).
    *   **Status**: Active/In Progress (Initiated Mar 26, 2026).
*   **Action**: Share revised project timelines and deliverables with Nikhil Grover.
    *   **Owner**: Gauri Salunke.
    *   **Status**: Pending completion of evaluation; no specific deadline provided in response but implied immediate execution.

**Decisions Made**
*   **Agreed Path Forward**: Osmos (Gauri) has accepted the mandate to proceed with integration change evaluation rather than requesting further clarification on scope from Nikhil at this stage.
*   **Baseline Confirmed**: API testing completion remains the validated baseline for all subsequent work.
*   **Timeline Protocol**: Gauri will proactively provide the schedule upon completing the technical assessment, shifting ownership of timeline creation solely to Osmos until shared with FairPrice.

**Key Dates & Follow-ups**
*   **Original Inquiry Date**: March 25, 2026 (Time: 2:47 PM).
*   **Milestone Achieved**: API testing completion (Mar 25, 2026).
*   **Response Received**: Mar 26, 2026, at 5:07 AM from Gauri Salunke.
*   **Next Step/Deadline**: Osmos to share evaluated timelines and requirements following the internal review.

**Contextual Note**
This update continues within the "FairPrice Performance Marketing Meta x Osmos" discussion thread. The initial [Not Virus Scanned] header indicates the ongoing security-monitored workflow. The communication flow has shifted from a pending inquiry (Mar 25) to an active acceptance of task (Mar 26), moving the project into the technical evaluation phase.


## [22/50] Data COE Org Announcement
Source: gmail | Thread: 19d288431ce247d5 | Labels: Inbox, Forums | Priority: None | Senders: Shirley BH Peh | Last Date: Thu, Mar 26, 2026, 5:00 AM | Last Updated: 2026-03-26T06:02:07.211353+00:00
**Daily Work Briefing: Data COE Org Announcement Summary**

**Key Participants & Roles**
*   **Dennis Seah:** Chief Digital and Technology Officer (Sender; issued announcement on behalf of Shirley BH Peh).
*   **Shirley BH Peh:** Sent the email on Dennis Seah's behalf.
*   **Hu Yiqun:** Leader of the Data Centre of Excellence (COE); will transition functions.
*   **Karen Chan:** Incoming Chief Customer and Marketing Officer (CCMO); becoming Hu Yiqun's new direct reporter.
*   **FairPrice Group (FPG) Colleagues:** Recipients of the announcement.

**Main Topic/Request**
Formal announcement regarding the strategic realignment of the Data COE to accelerate the "Customer Centricity" strategy by moving data capabilities closer to business operations and customer-facing strategies.

**Decisions Made**
*   **Organizational Transfer:** Effective April 1, 2026, the Data COE (led by Hu Yiqun) transitions from the Digital & Tech function to the Customer and Marketing (CCMO) function.
*   **Reporting Line Change:** Hu Yiqun will report directly to Karen Chan. Existing reporting lines within the Data COE remain unchanged.
*   **Scope Retention:** The scope of work remains unchanged, continuing to serve all business units and corporate functions in:
    *   Data Platform and Engineering
    *   Data Product Solutions
    *   Advanced Analytics and Intelligence
*   **Strategic Objectives:** To eliminate silos (Unified Data Strategy), increase proximity to business challenges (Proximity to the Business), and expand internal mobility for staff (Enhanced Career Opportunities).

**Pending Actions & Ownership**
*   **Action:** Execute organizational transition.
    *   **Owner:** Hu Yiqun, Karen Chan, and all relevant stakeholders.
    *   **Context:** Team must begin operating under CCMO leadership immediately upon the effective date.
*   **Action:** Maintain operational continuity.
    *   **Owner:** Data COE team.
    *   **Context:** Continue delivering data products and services to all business units without interruption.

**Key Dates & Deadlines**
*   **Announcement Date:** March 26, 2026 (5:00 AM).
*   **Effective Transition Date:** April 1, 2026.
*   **Next Steps:** No specific follow-up meeting dates are listed; the instruction is to "support the team" as they embark on this chapter.

**Contact Information**
*   **Sender Email:** shirley_pehbh@fairpricegroup.sg
*   **Reference Thread ID:** 19d288431ce247d5


## [23/50] [Dashboard Report] Retail Media - DD Dashboard | Thu 26 Mar 11:00AM +08
Source: gmail | Thread: 19d2817d11501d86 | Labels: Inbox, Updates | Priority: None | Senders: Datadog HQ | Last Date: Thu, Mar 26, 2026, 3:02 AM | Last Updated: 2026-03-26T06:02:14.893319+00:00
**Daily Work Briefing: Retail Media Dashboard Report**

**Key Participants & Roles:**
*   **Datadog HQ (no-reply@dtdg.eu):** Sender; Operations/Support team providing the automated report.
*   **Michael:** Recipient and primary owner of the dashboard metrics.

**Main Topic/Request:**
Submission of the "Retail Media - DD Dashboard" containing performance data for the preceding three days. The email serves as a notification to share monitoring insights rather than an explicit request for new input or approval.

**Pending Actions & Ownership:**
*   **Action:** Review the attached dashboard report covering the last 3 days of data.
*   **Owner:** Michael.
*   **Status:** Awaiting internal review (no reply requested in original thread).

**Decisions Made:**
None recorded in this specific email thread; this is an informational update only.

**Key Dates, Deadlines & Follow-ups:**
*   **Report Date/Time:** Thursday, March 26, 2026, at 11:00 AM +08 (Timestamp of resource metadata).
*   **Email Sent Time:** Wednesday, March 25, 2026, at 3:02 AM.
*   **Data Scope:** Past 3 days relative to the report date.
*   **Contact/Reference:** Team Datadog; Addressed to Michael.


## [24/50] Declined: ACNxOsmos: Daily Cadence @ Thu Mar 26, 2026 1:30pm - 2pm (SGT) (michael.bui@fairpricegroup.sg)
Source: gmail | Thread: 19d281786814b122 | Labels: Inbox | Priority: None | Senders: Rahul Jain | Last Date: Thu, Mar 26, 2026, 3:02 AM | Last Updated: 2026-03-26T06:02:31.387229+00:00
**Daily Work Briefing: Meeting Status Update**

**Meeting Overview**
*   **Event:** ACNxOsmos: Daily Cadence
*   **Date/Time:** Thursday, March 26, 2026, from 1:30 PM to 2:00 PM (SGT)
*   **Status:** Declined by Rahul Jain.

**Key Participants & Roles**
*   **Organizer:** Michael Bui (`michael.bui@fairpricegroup.sg`)
*   **Primary Attendees (Confirmed/Invited):**
    *   Flora Wo, Tanish Nevatia, Vipul Gupta, Barkha Kewalramani (`barkha.kewalramani_fp@ntucguest.com`), Rahul Jain (`rahul.jain@onlinesales.ai`), Tiongsiong Tee, Daryl Ng, Shravan Kankaria, John Henji Mantaring, Artharn Senrit (both `@ntucguest.com` and `@accenture.com` addresses noted), Nikhil Grover, Aman Khatri, Tanul Mehta (`tanul.mehta_fp@ntucguest.com` & `tanul.mehta@accenture.com`), Nabhey Samant, Winson Lim, Shubhangi Agrawal, Siddharth Aklujkar, Rachit Sachdeva, Satish Pamidimarthi.
*   **Optional Attendee:** Ravi Goel (`ravi_goel@fairpricegroup.sg`)

**Main Topic/Request**
The meeting is a "Daily Cadence" session for the ACNxOsmos project. The organizer distributed the "FPG Project Plan 2905025" as an attachment to facilitate discussion on this specific plan (Ref: FPG Project Plan 2905025).

**Decisions Made**
*   **RSVP Action:** Rahul Jain (`rahul.jain@onlinesales.ai`) has formally declined the invitation as of March 26, 2026, at 3:02 AM. No other acceptance or decline statuses are recorded in this thread snippet.

**Pending Actions & Ownership**
*   **Action:** Verify if a quorum exists for the meeting given Rahul Jain's absence and confirm attendance with other key stakeholders listed.
*   **Owner:** The meeting organizer, Michael Bui (`michael.bui@fairpricegroup.sg`), or project coordination team.
*   **Context:** Ensure participation from Accenture (`accenture.com`) and FairPrice Group (`fairpricegroup.sg`, `fairprice.com.sg`) representatives as the thread involves cross-organizational collaboration (ONLINE SALES AI, NTUC Guest, NTU Centreprise).

**Key Dates & Follow-ups**
*   **Meeting Date:** March 26, 2026.
*   **Follow-up Trigger:** If the meeting proceeds despite Rahul Jain's decline, a summary of the FPG Project Plan discussion should be circulated to all attendees (excluding the declined participant unless specifically requested).

**Constraints & Notes**
*   The email contains confidential project data; sharing or forwarding without authorization is prohibited.
*   Google Meet link: `meet.google.com/ise-ydtd-por`.


## [25/50] Message from Group CEO: Leadership Team announcement
Source: gmail | Thread: 19d27f9ebd9b6ccb | Labels: Inbox, Updates | Priority: None | Senders: Internal Comms | Last Date: Thu, Mar 26, 2026, 2:29 AM | Last Updated: 2026-03-26T06:02:48.310014+00:00
**Daily Work Briefing: Leadership Team Announcement**

**1. Key Participants & Roles**
*   **Vipul:** Group CEO (Sender).
*   **Alvin Neo:** Outgoing Chief Customer and Marketing Officer (CCMO); transitioning to Advisor role until Dec 31, 2026.
*   **Karen Chan:** Incoming Chief Customer and Marketing Officer (CCMO), effective June 1, 2026. Previously Group Chief Commercial Officer at AirAsia Aviation Group; joined FairPrice Group (FPG) in 2024 as a key driver of customer transformation.
*   **Internal Comms (`internal_comms@fairpricegroup.sg`):** Sender of the official announcement on behalf of FPG leadership.

**2. Main Topic/Request**
Formal announcement regarding the restructuring of Leadership under "Customer & Marketing Transformation." The update details Alvin Neo's departure from the CCMO role to focus on community impact, and Karen Chan's appointment as his successor to integrate data, customer, marketing, and loyalty capabilities in an AI-driven economy.

**3. Pending Actions & Ownership**
*   **Action:** Share new organizational structure plans for Customer, Data, and Marketing functions.
    *   **Owner:** Karen Chan (in collaboration with Alvin Neo and Tongwen).
    *   **Status:** Plans are currently being developed; specific release date not yet stated other than "shortly."
*   **Action:** Execute smooth transition of CCMO remit from Alvin to Karen.
    *   **Owner:** Alvin Neo (providing support during transition) and Karen Chan.

**4. Decisions Made**
*   **Role Change:** Alvin Neo is relinquishing the role of Chief Customer and Marketing Officer effective June 1, 2026.
*   **Appointment:** Karen Chan appointed as the new CCMO effective June 1, 2026.
*   **New Mandate:** The CCMO mandate now focuses on fully integrating data, customer, marketing, and loyalty capabilities to maximize value realization for the FPG ecosystem.
*   **Advisory Role:** Alvin Neo will serve as an Advisor supporting strategic initiatives until December 31, 2026.

**5. Key Dates & Deadlines**
*   **March 26, 2026:** Announcement date (Sent at 2:29 AM).
*   **June 1, 2026:** Effective date for Karen Chan's appointment as CCMO and Alvin Neo's departure from the role.
*   **December 31, 2026:** End of Alvin Neo's advisory tenure.

**6. Contextual References**
*   **Strategic Goal:** Becoming Asia's most admired retailer by 2030; "Every Day, Made A Little Better."
*   **Key Initiatives Mentioned:** Project Leap (unified "golden customer profile"), Link program integration, "The Price of Being Fair" bestseller.

**Summary for Team:**
Please note the leadership transition effective June 1, 2026. Karen Chan will assume responsibility for merging data and marketing functions. Alvin Neo remains as an Advisor through year-end. Await further communication from Karen regarding the new organizational structure.


## [26/50] [GCP] New Service Account Key Created - a7a49005482a712992311bfb9b6be276b5103a07
Source: gmail | Thread: 19d27d8884ed630c | Labels: Inbox, Forums | Priority: None | Senders: noreply-sre | Last Date: Thu, Mar 26, 2026, 1:53 AM | Last Updated: 2026-03-26T02:01:23.502127+00:00
**Daily Work Briefing: GCP Service Account Activity**

**1. Key Participants & Roles**
*   **Sender:** `noreply-sre@ntucenterprise.sg` (Automated notification from the SRE team).
*   **Target Audience/Subject:** Owner(s) of the service account `fponprd/seller-analytics-service@fponprd.iam.gserviceaccount.com`.

**2. Main Topic/Request**
*   Notification that a new Service Account Key (`a7a49005482a712992311bfb9b6be276b5103a07`) has been generated for the `fponprd` environment.
*   The key is valid for 90 days and is set to expire on **2026-06-24**.

**3. Pending Actions & Ownership**
*   **Action:** Download the new service key immediately using the provided link in the original email (link text: "Click the link here").
*   **Owner:** The application team or administrator responsible for the `seller-analytics-service`.
*   **Condition:** This action is required only if a new key was intentionally requested; otherwise, the notification should be ignored.

**4. Decisions Made**
*   No explicit business decisions recorded in this thread.
*   System decision: The SRE automation triggered key generation for the specified service account on March 26, 2026.

**5. Key Dates & Deadlines**
*   **Generation Date:** March 26, 2026, at 1:53 AM.
*   **Expiration Deadline:** June 24, 2026 (90-day validity window).
*   **Follow-up:** Immediate download required upon receipt to ensure service continuity before the current key becomes obsolete or if rotation is part of a security protocol.

**6. Metadata & References**
*   **Resource ID:** [GCP] New Service Account Key Created - `a7a49005482a712992311bfb9b6be276b5103a07`
*   **Service Account:** `fponprd/seller-analytics-service@fponprd.iam.gserviceaccount.com`
*   **Labels:** Inbox, Forums
*   **Message ID:** `19d27d8884ed630c`


## [27/50] Invitation: [BCRS]-ECOM Flow Deployment @ Fri Mar 27, 2026 12am - 1am (SGT) (Michael Bui)
Source: gmail | Thread: 19d27b0df2580729 | Labels: Inbox | Priority: None | Senders: Onkar Bamane | Last Date: Thu, Mar 26, 2026, 1:09 AM | Last Updated: 2026-03-26T02:01:37.402505+00:00
**Daily Work Briefing: BCRS ECOM Flow Deployment**

**1. Key Participants & Roles**
*   **Organizer:** Onkar Bamane (onkar.bamane@fairpricegroup.sg)
*   **Confirmed Guests:** Wai Ching Chan, Hendry Tionardi, Bagavanantham Palaniappan, Sneha Parab, Kandasamy Magesh, Daryl Chang, Michael Bui (michael.bui@fairpricegroup.sg), Olivia.
*   **Optional Guest:** Prajney Sribhashyam.

**2. Main Topic/Request**
Deployment of the [BCRS]-ECOM Flow scheduled for Friday, March 27, 2026. The session is a technical deployment window requiring real-time coordination via Google Meet and telephone conference bridge.

**3. Pending Actions & Owners**
*   **RSVP Confirmation:** Michael Bui must confirm attendance status (Yes/No/Maybe) by responding to the calendar invitation sent from `michael.bui@fairpricegroup.sg`.
*   **Connection Preparation:** All attendees must prepare to join using either the Google Meet link or the provided US phone number.

**4. Decisions Made**
*   **Meeting Format:** Confirmed as a hybrid virtual session utilizing Google Meet (`meet.google.com/wkx-cwrw-ozm`) and a US dial-in line (+1 402-356-1090, PIN: 234960291).
*   **Schedule:** Fixed for Friday, March 27, 2026, from 12:00 AM to 1:00 AM (Singapore Standard Time).

**5. Key Dates & Follow-ups**
*   **Event Date/Time:** Fri Mar 27, 2026 @ 12am - 1am SGT.
*   **Notification Sent:** Mar 26, 2026, at 1:09 AM (by Onkar Bamane).
*   **Follow-up Required:** Immediate RSVP from Michael Bui and confirmation of connectivity for all listed guests prior to the 12:00 AM start time.

**Contact Reference**
*   Google Meet ID: `wkx-cwrw-ozm`
*   US Phone: +1 402-356-1090 | PIN: 234960291


## [28/50] [RAW Overdue] Expired Risk Acceptance & Waiver Form
Source: gmail | Thread: 19d27aa484a42190 | Labels: Inbox | Priority: None | Senders: cyberrisk.automation | Last Date: Thu, Mar 26, 2026, 1:02 AM | Last Updated: 2026-03-26T02:01:53.605952+00:00
**Daily Work Briefing: Expired Risk Acceptance & Waiver (RAW) Alert**

**1. Key Participants & Roles**
*   **Sender/Notifier:** Cyber Risk Team (`cyberrisk.automation@fairpricegroup.sg`).
*   **Recipient:** Requestor (Business Owner of the affected asset).
*   **Reviewers/Stakeholders:**
    *   Cybersecurity Risk Team (`cyberRisk@ntucenterprise.sg`): Reviews form completion in Section A prior to sign-off.
    *   Technology Governance and Compliance Team (`techgrc@ntucenterprise.sg`): Must be shared the form during the process.

**2. Main Topic & Request**
The system has flagged an **expired Risk Acceptance and Waiver (RAW)** for the asset **"Signcloud SaaS User access management"** under entity **FPG-Fairprice**. The original waiver expired on **May 15, 2025**, due to a lack of user access management by the business owner. The team requires immediate remediation or a new RAW submission (ID: `RAW-20240306_01-v1.0`).

**3. Pending Actions & Ownership**
*   **Action:** Determine if residual risks have been remediated.
    *   *If Remediated:* Provide evidence to `cyberRisk@ntucenterprise.sg` for closure review.
    *   *If Not Remediated:* Submit a new RAW form immediately via Gsuite (Google Docs).
*   **Action:** Execute the RAW process strictly within Gsuite (no downloads).
    1.  Copy the template to personal drive.
    2.  Complete Section A.
    3.  Share completed Section A with `cyberRisk@ntucenterprise.sg` and `techgrc@ntucenterprise.sg`.
    4.  Wait for Cybersecurity Risk Team review before seeking sign-off.
*   **Action:** Ensure all sign-offs include the signer's full name or initials accompanied by a comment stating "Approved" or "Signed."
*   **Owner:** The original Requestor/Business Owner.

**4. Decisions Made**
No new decisions were made in this thread; the email serves as an automated reminder enforcing existing compliance protocols regarding expired waivers.

**5. Key Dates & Deadlines**
*   **Original Expiry Date:** May 15, 2025.
*   **Current Status:** Expired (as of Mar 26, 2026).
*   **Future Action:** New RAW must be submitted "as soon as possible." Automated reminders will continue until a new form is approved.

**References:**
*   Asset: Signcloud SaaS User access management
*   RAW ID: RAW-20240306_01-v1.0
*   Risk Description: Lack of user access management by respective business owner.


## [29/50] Daily digest: updates from Tan Nhu Duong
Source: gmail | Thread: 19d27438db3870f3 | Labels: Inbox, Updates | Priority: None | Senders: Confluence | Last Date: Wed, Mar 25, 2026, 11:10 PM | Last Updated: 2026-03-26T02:02:04.008566+00:00
**Daily Work Briefing: Confluence Update Digest**

**1. Key Participants & Roles**
*   **System:** Atlassian Confluence (Automated Notification System).
*   **Sender:** `confluence@ntuclink.atlassian.net` (Platform Administrator/Service).
*   **Recipient/User:** Tan Nhu Duong (Content Contributor).
*   **Reference Content:** "Handover Identity scope" page.

**2. Main Topic/Request**
The email is an automated daily digest summarizing activity on content contributed by the recipient, Tan Nhu Duong. The primary focus of this specific update cycle is highlighting a new comment left by Tan Nhu Duong on the Confluence page titled **"Handover Identity scope."** No external requests or manual messages from colleagues were included in this thread.

**3. Pending Actions & Ownership**
*   **Action:** Review the "Handover Identity scope" page for context regarding the comments made by Tan Nhu Duong.
*   **Ownership:** Tan Nhu Duong (to review their own contribution).
*   **Status:** No external action items assigned to other team members in this specific digest.

**4. Decisions Made**
No formal decisions were recorded or communicated within this automated notification thread. The email serves strictly as an informational summary of platform activity.

**5. Key Dates & Deadlines**
*   **Digest Date:** March 25, 2026.
*   **Timestamp:** 11:10 PM (Local server time assumed).
*   **Next Steps:** No specific follow-up deadlines were set in the digest; recipients are instructed to click "Go to Confluence" for real-time access to the content.

**Summary Note:** This entry is a system-generated notification regarding Tan Nhu Duong's contribution to the "Handover Identity scope" page. All updates reflect activity generated on March 25, 2026. No further action is required unless specific comments within the linked Confluence page necessitate immediate attention from stakeholders not listed in this digest.


## [30/50] You have no events scheduled today.
Source: gmail | Thread: 19d26f48d1c1e331 | Labels: Inbox, Updates | Priority: None | Senders: Google Calendar | Last Date: Wed, Mar 25, 2026, 9:44 PM | Last Updated: 2026-03-25T22:01:10.756845+00:00
**Daily Work Briefing Summary**

**1. Key Participants & Roles**
*   **Michael Bui** (Recipient/Account Owner): `michael.bui@fairpricegroup.sg`. The summary is generated for this account holder regarding their calendar status.
*   **Google Calendar System** (`calendar-notification@google.com`): Automated notification service sending the daily agenda update.

**2. Main Topic/Request**
*   Automated delivery of a daily calendar agenda notification confirming the user's schedule status for the current day.

**3. Pending Actions & Ownership**
*   **No immediate actions required.** The email confirms "no events scheduled" and serves as an informational update rather than a task trigger.
*   **Optional Action:** If Michael Bui wishes to modify which calendars generate these notifications (specifically the "Digital Business Tech Release/Changes" calendar), he must log in to `https://calendar.google.com/calendar/` and adjust notification settings manually.

**4. Decisions Made**
*   None. This is a system-generated status report, not a record of business decisions or meeting outcomes.

**5. Key Dates & Deadlines**
*   **Current Date:** Thursday, March 26, 2026.
*   **Notification Time:** 9:44 PM (March 25, 2026) – *Note: The email was sent the evening prior to the date it covers.*
*   **Scheduled Events:** None for Thu Mar 26, 2026.

**Metadata Context**
*   **Labels:** Inbox, Updates.
*   **Priority:** Not specified (null).
*   **Message ID:** `19d26f48d1c1e331`.


## [31/50] Upcoming limits for all Jira apps
Source: gmail | Thread: 19d2645ba3f142a4 | Labels: Inbox, Updates | Priority: None | Senders: Atlassian | Last Date: Wed, Mar 25, 2026, 6:33 PM | Last Updated: 2026-03-25T22:01:23.608388+00:00
**Executive Briefing: Jira Cloud Limits & Data Management Update**

**Key Participants**
*   **Sender:** Atlassian (info@e.atlassian.com) – Platform provider issuing policy updates.
*   **Recipient:** Account administrators/users of Jira Cloud apps (Jira, Jira Service Management, Jira Product Discovery).

**Main Topic**
Atlassian is announcing expanded limits, new guardrails, and enhanced data management tools for the Jira Cloud family of applications to prevent performance slowdowns and ensure site health.

**Pending Actions & Ownership**
*   **Action:** Monitor upcoming enforcement of new limits on specific data types.
    *   **Owner:** IT/Admin Team (Site Administrators).
*   **Action:** Review and adopt new "guardrails" (recommended thresholds for data volume/configuration) to maintain site performance.
    *   **Owner:** Site Administrators.
*   **Action:** Utilize newly rolled-out data cleanup tools to identify and manage unused or outdated data, specifically optimizing work item security schemes and field options.
    *   **Owner:** Site Administrators.

**Decisions Made**
*   Atlassian has decided to enforce new limits on certain data types starting September 2026.
*   Enforcement of previously announced limits is now being rolled out immediately.
*   New data cleanup tools are being made available to all customers at no additional cost.
*   A migration grace period was established: migrating customers have **6 months** from their migration date to adhere to the new Jira Cloud limits (limits will not block the migration itself).

**Key Dates & Deadlines**
*   **March 25, 2026:** Notification sent regarding these changes.
*   **September 2026:** Mandatory enforcement start date for new data type limits.

**Additional Context**
These measures are designed to optimize site health and reliability. The communication emphasizes that these updates will simplify data management for admins while ensuring a smoother user experience for teams. Unsubscribing from this specific message type is not permitted as it constitutes an important account notification.


## [32/50] What's new in Atlassian for software teams
Source: gmail | Thread: 19d2628aabfd4196 | Labels: Inbox, Promotions | Priority: None | Senders: Bitbucket | Last Date: Wed, Mar 25, 2026, 6:01 PM | Last Updated: 2026-03-25T22:01:41.933206+00:00
**Daily Briefing: Atlassian Product Update & Event Announcements**

**Key Participants & Roles**
*   **Bitbucket (Atlassian):** Sender of the newsletter; primary resource provider.
*   **Warren Marusiak:** Senior Technical Evangelist leading the Bitbucket Pipelines lab.
*   **Guest Speakers (Team '26 Keynote):** An Emmy Award-winning journalist/author and an AI expert on work transformation (names not specified in text).
*   **Target Audience:** Developers and Platform/DevOps engineers using Bitbucket Cloud.

**Main Topic/Request**
The email serves as a promotional update for software teams regarding new capabilities and upcoming live sessions. Key themes include scaling Bitbucket Pipelines, integrating AI via Rovo Dev into Jira workflows, and adopting product engineering mindsets. The primary request is for eligible users to register for specific training sessions and guides.

**Pending Actions & Ownership**
*   **Action:** Register for the "Scaling Bitbucket Pipelines" live lab.
    *   **Owner:** Engineers/Platform Engineers using Bitbucket Cloud.
    *   **Requirement:** Registration must use an email tied to an Atlassian account with Bitbucket Cloud access.
*   **Action:** Register for the Rovo Dev in Jira session.
    *   **Owner:** Users interested in AI-assisted code assignment and PR creation.
    *   **Note:** This session was scheduled for "tomorrow" relative to the March 25, 2026 send date (March 26).
*   **Action:** Register for Team '26 Opening Keynote.
    *   **Owner:** General team or leadership attending the Anaheim event.
*   **Action:** Obtain product engineering guide.
    *   **Owner:** Product/Engineering teams seeking to shift from code shipping to problem solving.

**Decisions Made**
No internal decisions were made within this email thread; it is an outbound communication inviting registration and participation.

**Key Dates & Deadlines**
*   **March 26, 2026 (Yesterday/Tomorrow relative to send):** Rovo Dev in Jira live session. *Status: Likely past or immediate.*
*   **April 20, 2026:** Bitbucket Pipelines Live Lab.
    *   **Time:** 14:30 – 16:00 PDT (90 minutes).
    *   **Format:** Hands-on Zoom lab; no setup required (Atlassian provides environment).
*   **Future:** Team '26 Opening Keynote in Anaheim (specific date not listed, but registration is open).

**Logistics & Requirements**
*   **Pipelines Lab Participation:** Requires a laptop with a modern browser and stable internet. Participants must write and modify pipeline configs live during the session.
*   **Topics Covered:** Bitbucket Packages, Dynamic Pipelines, Advanced configurations (parent/child/shared pipelines), and code compliance automation.
*   **Contact/Support:** Questions to be directed to the Bitbucket Community or via provided contact links.


## [33/50] [JIRA] (DPD-715) Dynamic ad slot configuration for Homepage swimlanes
Source: gmail | Thread: 19cd82204175d296 | Labels: Inbox, Updates | Priority: None | Senders: Nikhil | Last Date: Wed, Mar 25, 2026, 4:29 PM | Last Updated: 2026-03-25T22:02:01.732041+00:00
**Daily Work Briefing: DPD-715 Dynamic Ad Slot Configuration (Production Deployed)**

**Key Participants & Roles**
*   **Nikhil Grover:** Product Manager.
*   **Michael Bui:** Development Lead/Manager; executed production deployment, verified slot configuration changes, and provided post-deployment validation recordings.

**Main Topic/Request**
Development of a dynamic ad slot configuration system (Ticket: **DPD-715**) for Omni and OG Homepage swimlanes, enabling Product Managers to control ad placement indices via Split feature flags without code deployments.

**Decisions Made & Status Updates**
*   **Status Change:** The ticket has transitioned from "IN RELEASE QUEUE" to **"Done"** following successful production deployment on March 25, 2026.
*   **Production Deployment:** Michael Bui deployed the feature to Production (PRD) on March 25, 2026 (12:02 AM Singapore Time). Verification confirmed that slot positions updated correctly based on the configured SplitIO flag values.
*   **Configuration Approval:** Product Manager Nikhil Grover signed off on UAT and explicitly requested deployment using the specific slot configuration: **[3, 5, 7, 11, 13, 15]** (Commented at 10:11 PM Singapore Time on March 25).
*   **Validation Evidence:** Post-deployment verification was completed on March 26, 2026. Michael Bui attached screen recordings (`ScreenRecording_03-26-2026 00-15-50_1.MP4`) demonstrating that the live environment reflects the new slot indices `[3, 5, 7, 11, 13, 15]`.

**Pending Actions & Ownership**
*   **No Immediate Action Required:** The feature is live in production with confirmed functionality. No further testing or deployment actions are pending by PM or Dev leads.
*   **Monitoring:** Standard post-deployment monitoring for ad density and empty array handling (`[]` returns 0 ads) continues as per standard operational procedures.

**Key Dates & Deadlines**
*   **Start Date:** March 10, 2026
*   **UAT Sign-off:** March 25, 2026 (10:11 PM Singapore Time).
*   **Production Deployment:** March 25, 2026 (12:02 AM Singapore Time).
*   **Post-Deploy Verification:** March 26, 2026 (12:19 AM – 12:21 AM Singapore Time).

**Reference Data**
*   **Ticket ID:** DPD-715
*   **Project:** (Ecom/Omni) DPD
*   **Last Message ID:** 19d25d4ace4be23e
*   **Attachments:**
    *   `image-20260325-160055.png` (Visual confirmation of slot changes).
    *   `ScreenRecording_03-26-2026 00-15-50_1.MP4` (Post-deployment validation).
*   **Timezone Context:** Singapore Time

**Historical Context Retained**
*   Boundary handling logic remains valid: Configured indices exceeding available content range are ignored; only valid bounds render.
*   Stock integrity checks remain active: Out-of-stock items cannot be served as ads regardless of slot configuration.
*   Previous mobile app issues (dynamic updates) were resolved in the earlier UAT cycle and verified again during this production deployment.


## [34/50] [Bitbucket]  Pipeline for master failed on fc067b7 (ntuclink/marketing-service)
Source: gmail | Thread: 19d259df3977b58a | Labels: Inbox, Updates | Priority: None | Senders: Bitbucket | Last Date: Wed, Mar 25, 2026, 3:30 PM | Last Updated: 2026-03-25T22:02:14.875840+00:00
**Daily Work Briefing: Bitbucket Pipeline Failure**

**Key Participants & Roles**
*   **Michael Bui**: Developer/Committer. Responsible for the code change that triggered the failure.
*   **Bitbucket System (notifications-noreply@bitbucket.org)**: Automated notification service. Role is to alert the team of pipeline status changes.
*   **NTUCLINK Team**: Owners of the `marketing-service` repository.

**Main Topic/Request**
The automated build pipeline for the `master` branch of the `ntuclink/marketing-service` repository failed immediately following a successful merge of Pull Request #131 (Ticket DPD-715). The failure occurred during the execution phase, halting deployment or validation processes.

**Pending Actions & Ownership**
*   **Action**: Investigate the specific error logs within the failing pipeline run to determine the root cause.
    *   **Owner**: Development team / Michael Bui (implied responsibility for the merged code).
*   **Action**: Review and fix the "Sanitize configured slots" logic implemented in commit `fc067b7`.
    *   **Owner**: Developer responsible for DPD-715.
*   **Action**: Re-trigger the pipeline or merge a hotfix once the issue is resolved to restore CI/CD stability.
    *   **Owner**: Development team.

**Decisions Made**
*   No new decisions were made in this thread; the event represents an automated status update regarding a failed build. The system automatically halted the process upon detecting the failure.

**Key Dates, Deadlines & References**
*   **Date/Time of Incident**: March 25, 2026, at 3:30 PM (Notification timestamp).
*   **Duration of Failed Run**: 17 minutes and 57 seconds.
*   **Commit Hash**: `fc067b7` by Michael Bui.
*   **Repository/Branch**: `ntuclink/marketing-service` / `master`.
*   **Ticket Reference**: DPD-715 (Pull Request #131).
*   **PR Description**: "Sanitize configured slots for multiple edge cases."
*   **Metadata Tags**: Inbox, Updates.

**Summary of Failure Context**
The failure is directly linked to the merge of PR #131. The commit message indicates changes regarding slot sanitization logic for edge cases. Immediate attention is required to analyze the 17-minute runtime logs to identify why these specific sanitization checks caused the pipeline to fail on the master branch.


## [35/50] New reply received for this ticket on which you are CC'd
Source: gmail | Thread: 19d2572b31597f0f | Labels: Inbox | Priority: None | Senders: Osmos Support | Last Date: Wed, Mar 25, 2026, 2:42 PM | Last Updated: 2026-03-25T22:02:37.454646+00:00
**Daily Work Briefing Summary**

**Key Participants & Roles**
*   **Michael Bui:** Recipient (CC'd on original ticket); Stakeholder receiving status update.
*   **Siddharth:** Internal team contact; Provided detailed notes and suggestions to Osmos Support.
*   **Nikhil:** Representative from Osmos Support (<support@onlinesalesai.zohodesk.in>); Acknowledged receipt of Siddharth's input and is leading the review process.

**Main Topic/Request**
Review of instances and internal suggestions regarding **Ticket #107110 (Nino Nana SKU Mapping)**. The discussion focuses on analyzing provided data to streamline the mapping process between teams.

**Pending Actions & Ownership**
*   **Action:** Review specific instances and suggestions shared by Siddharth's team.
    *   **Owner:** Nikhil (Osmos Support).
    *   **Status:** In progress.
*   **Action:** Communicate findings and propose further streamlining steps.
    *   **Owner:** Nikhil (Osmos Support).

**Decisions Made**
No final decisions or resolutions were recorded in this thread. The parties agreed to collaborate further once Nikhil completes his review.

**Key Dates & Follow-ups**
*   **Ticket Reference:** [##107672##] linked to original request #107110.
*   **Last Message Date:** March 25, 2026, at 2:42 PM (Time zone not specified).
*   **Next Follow-up Deadline:** Early next week (Specific date TBD based on "next week" relative to Mar 25, 2026 context). Nikhil is confirmed to provide findings by this time.

**Metadata Context**
This update was received as a new reply notification for the ticket on which you are CC'd. The system label indicates this is in the primary Inbox with no specific priority flag assigned.


## [36/50] [##107672##] Your reply has been received.
Source: gmail | Thread: 19d2572b10aa8779 | Labels: Inbox | Priority: None | Senders: Osmos Support | Last Date: Wed, Mar 25, 2026, 2:42 PM | Last Updated: 2026-03-25T22:02:51.465391+00:00
**Daily Work Briefing: Ticket #107672 / Reference #107110**

**Key Participants & Roles**
*   **Michael Bui:** Original ticket participant/CC. Addressed in the automated system confirmation.
*   **Osmos Support (support@onlinesalesai.zohodesk.in):** System notification provider; confirmed receipt of reply.
*   **Siddharth:** Internal stakeholder who provided a detailed note with instances and suggestions to the team.
*   **Nikhil:** Response sender within Osmos Support; responsible for reviewing internal feedback and coordinating process streamlining.

**Main Topic/Request**
The thread concerns **Ticket #107672**, specifically regarding **"Ticket #107110 (Nino Nana SKU Mapping)."** The core discussion involves Siddharth sharing a detailed internal note containing instances and suggestions to improve the workflow. Nikhil acknowledged receipt of this input and initiated a review process.

**Pending Actions & Ownership**
*   **Action:** Review shared instances and suggestions regarding the Nino Nana SKU mapping process.
    *   **Owner:** Nikhil.
*   **Action:** Deliver findings based on the review to Siddharth.
    *   **Owner:** Nikhil.
*   **Action:** Collaborate with Siddharth to streamline the process for both teams post-findings.
    *   **Owner:** Joint (Nikhil and Siddharth).

**Decisions Made**
No final technical or strategic decisions were recorded in this thread. The only formal agreement is Nikhil's commitment to review the provided data and return with findings to explore further process optimization.

**Key Dates, Deadlines & Follow-ups**
*   **Last Activity:** March 25, 2026, at 2:42 PM (Timestamp of Nikhil's reply).
*   **System Notification Date:** March 25, 2026, at 2:42 PM.
*   **Expected Follow-up:** Niklin will respond with findings **"early next week."**
    *   *Context:* "Next week" refers to the week commencing March 30, 2026 (following March 25, 2026).
*   **Ticket IDs Referenced:** #107672 and #107110.

**Summary Status**
The ticket is currently in a "Review/Analysis" phase. The support team has acknowledged the input from Siddharth and is processing it for a follow-up response scheduled for early next week. No further action is required from Michael Bui at this moment, other than monitoring for Nikhil's update.


## [37/50] Recurring concerns regarding the quality and effectiveness of the OSMOS support
Source: gmail | Thread: 19b4f4c3f38613b3 | Labels: Inbox, ⚠️IMPORTANT | Priority: ⚠️IMPORTANT | Senders: me, Siddh., Nikhil | Last Date: Wed, Mar 25, 2026, 2:42 PM
(Not yet fetched)


## [38/50] Urgent - PLA Impressions drop by 50%
Source: gmail | Thread: 19d24c9e00402c74 | Labels: Inbox | Priority: None | Senders: Rachit, me, Nikhil | Last Date: Wed, Mar 25, 2026, 2:37 PM | Last Updated: 2026-03-25T22:03:08.087276+00:00
**Daily Work Briefing: Urgent PLA Impressions Drop – Hypothesis Shift**

**Key Participants & Roles**
*   **Rachit Sachdeva** (rachit.sachdeva@osmos.ai): Source of data; investigating product response counts.
*   **Michael Bui** (michael.bui@fairpricegroup.sg): Investigating root cause; coordinating internal teams.
*   **Nikhil Grover** (nikhil.grover@fairpricegroup.sg): Identified potential root cause; requested specific metric analysis.

**Main Topic/Request**
Investigate a 50% drop in PLA impressions over the last week. Initial data showed search page impressions falling from 1.3M to 550K and category page impressions dropping by 62% (205K to 77K). While request volumes remained stable, Nikhil Grover identified a critical hypothesis: the average number of products per response has significantly decreased. Historical data showed 4-5 products per response; current data indicates most responses now contain only a single product across categories like "Drinks > Beverage" and "Beauty & Personal Care > Oral Care." This reduction in product density is presumed to be the primary driver of the impression drop.

**Pending Actions & Ownership**
*   **Analyze average products per response:** Owned by Rachit Sachdeva. He must verify if this metric has declined over the last 7 days and correlate it with the impression drop, as Nikhil lacks data beyond that window.
*   **Compile granular/hourly data:** Owned by Rachit Sachdeva. Still required to pinpoint the exact start time of the trend.
*   **Cross-check internal activities:** Owned by Michael Bui (and his team). Awaiting granular data and product count analysis to confirm root cause.

**Decisions Made**
*   Confirmed that ad requests remained stable; the drop is isolated to impressions, not traffic volume.
*   **Hypothesis Shifted:** The investigation has pivoted from a general "traffic/impression" issue to a specific "product density per response" issue. The drop in impressions is likely driven by fewer products being served per request rather than a lack of requests.

**Key Dates & Follow-ups**
*   **March 25, 2026:**
    *   **11:38 AM:** Alert raised regarding declining PLA impressions.
    *   **12:00 PM – 12:07 PM:** Michael requested hourly data and clarification on request volume.
    *   **12:56 PM:** Rachit confirmed stable request volumes and committed to compiling detailed time-frame data.
    *   **2:37 PM (New):** Nikhil Grover highlighted the reduction in products per response (from 4-5 down to 1) via screenshots for specific categories. He requested a historical check on this metric from Rachit.

**Status Summary**
Investigation is in progress with a refined hypothesis. The drop in impressions appears correlated with a sharp decline in the number of products returned per ad response rather than a drop in request volume. Root cause analysis is currently blocked pending Rachit's confirmation of product-per-response metrics over the last 7 days and the delivery of granular hourly data.


## [39/50] Notes: Meeting Mar 25, 2026 at 9:37 PM GMT+08:00
Source: gmail | Thread: 19d25579815d83ff | Labels: Inbox, Updates | Priority: None | Senders: Gemini | Last Date: Wed, Mar 25, 2026, 2:13 PM | Last Updated: 2026-03-25T22:03:20.248300+00:00
**Daily Work Briefing: Ad Revenue & Impression Decline Investigation**

**Key Participants & Roles**
*   **Nikhil Grover:** Lead investigator; responsible for data analysis, ticket management, and deployment execution.
*   **Michael Bui:** Provides technical access (Harness link) and requires review of resolution tickets.
*   **Gemini (Auto-generated):** Meeting note system.

**Main Topic/Request**
Investigation into a 62% drop in ad impressions and viewability index on category and search pages, which correlates to an estimated weekly revenue loss of $1,000–$6,000. Traffic volume remains stable, indicating the issue lies within impression event tracking or product response logic in Osmos.

**Decisions Made**
*   Primary hypothesis confirmed: The drop is driven by a reduction in active campaigns, resulting in fewer products returned per ad response (some categories returning only one).
*   Action prioritized: Investigate and deploy a configuration change to resolve the issue before escalating as a formal incident.

**Pending Actions & Ownership**
1.  **Nikhil Grover:** Share banner issue resolution ticket ID with Michael Bui for review.
2.  **Nikhil Grover:** Download oral care report data to compare product participation metrics.
3.  **Nikhil Grover:** Email the group/Osmos regarding the impression drop and share the "fewer products per response" hypothesis.
4.  **Michael Bui:** Send the Harness configuration link to Nikhil Grover.
5.  **Nikhil Grover:** Execute configuration changes via Harness (scheduled for tonight or early tomorrow morning).
6.  **Nikhil Grover:** Document deployment instructions in Z ticket comments.

**Key Dates & Deadlines**
*   **Meeting Date:** March 25, 2026, at 9:37 PM GMT+08:00.
*   **Deployment Window:** Tonight (March 25) or early tomorrow morning (March 26).
*   **Ticket Reference:** Z ticket 715.

**Status Summary**
Data discrepancy has been identified; traffic is not down, but impression events are dropping in Osmos. The team is proceeding with a configuration fix tonight pending the receipt of the Harness link from Michael Bui.


## [40/50] Spreadsheet shared with you: "Product_Ads_Analytics_Demand_&_Supply_High_Demand_Search_Queries_Beauty--Personal-Care_>_Oral-Care-1__E(20260325)__ID(69c3ebc2fa2a5efc3cc8cadc)"
Source: gmail | Thread: 19d25519687147a5 | Labels: Inbox, Updates | Priority: None | Senders: Nikhil Grover (via . | Last Date: Wed, Mar 25, 2026, 2:06 PM | Last Updated: 2026-03-25T22:03:33.767945+00:00
**Daily Work Briefing: Product Ads Analytics Thread**

**Key Participants & Roles**
*   **Sender:** [Name Not Provided] (Role: Requester/Analyst) – Initiating the data request for high-demand search queries.
*   **Recipient:** [Name Not Provided] (Role: Data Processor/Administrator) – Responsible for generating and sharing the specific analytics spreadsheet.
*   *Note: Specific names and email addresses were not included in the provided source text.*

**Main Topic/Request**
The thread centers on retrieving the "High Demand Search Queries" dataset specifically within the **Beauty > Personal Care > Oral Care** category. The requester requires a filtered view of product ad analytics focusing on demand versus supply dynamics for this specific vertical to support upcoming strategy sessions.

**Pending Actions & Ownership**
*   **Action:** Share the finalized spreadsheet file containing the requested data.
    *   **Owner:** Data Administrator (Recipient).
    *   **Status:** Pending completion based on the thread context.
*   **Action:** Review the specific data points within the "High Demand Search Queries" section of the shared file.
    *   **Owner:** Analyst/Sender.
    *   **Status:** Awaiting receipt of the document.

**Decisions Made**
*   **Data Scope Confirmed:** The dataset is explicitly scoped to the category path: `Beauty--Personal-Care > Oral-Care`.
*   **File Identification:** The specific file to be generated and shared has been identified by its unique system ID: `69c3ebc2fa2a5efc3cc8cadc`.
*   **Naming Convention Adhered To:** The file is designated as `Product_Ads_Analytics_Demand_&_Supply_High_Demand_Search_Queries_Beauty--Personal-Care_>_Oral-Care-1__E(20260325)`.

**Key Dates & Follow-ups**
*   **Report Date/Epoch:** The file metadata indicates a generation or effective date of **March 25, 2026 (20260325)**.
*   **Thread Activity:** The latest message in the sequence is identified by ID `19d25519687147a5`.
*   **Next Steps:** Follow-up required once the file `Product_Ads_Analytics...ID(69c3ebc2fa2a5efc3cc8cadc)` is uploaded and accessible to the sender.

**Contextual Metadata**
*   **Labels:** Inbox, Updates.
*   **Priority:** Null (Standard processing).


## [41/50] Spreadsheet shared with you: "Product_Ads_Analytics_Demand_&_Supply_High_Demand_Search_Queries_Baby-Child-Toys_>_Infant-Formula--1__E(20260325)__ID(69c3eb4efa2a5efc3cc8cab7)"
Source: gmail | Thread: 19d254fd66c7dcde | Labels: Inbox, Updates | Priority: None | Senders: Nikhil Grover (via . | Last Date: Wed, Mar 25, 2026, 2:04 PM | Last Updated: 2026-03-25T14:07:00.018161+00:00
**Daily Work Briefing: Product Ads Analytics Update**

**1. Key Participants & Roles**
*   **Nikhil Grover** (nikhil.grover@fairpricegroup.sg): Initiator and owner of the analytics data; shared via Google Sheets.
*   **Recipient**: The user receiving this briefing (invited to edit the spreadsheet).

**2. Main Topic/Request**
*   Sharing of a specific dataset titled: **"Product_Ads_Analytics_Demand_&_Supply_High_Demand_Search_Queries_Baby-Child-Toys_>_Infant-Formula--1"**.
*   The data focuses on high-demand search queries within the "Baby-Child-Toys" category, specifically targeting the "Infant Formula" sub-segment.
*   Permission granted to the recipient to **edit** the shared spreadsheet.

**3. Pending Actions & Ownership**
*   **Action Required**: Review and edit the shared Google Spreadsheet.
*   **Owner**: The Recipient (based on the invitation status).
*   **Deadline**: Not specified in the current communication; immediate review is implied by the sharing event.

**4. Decisions Made**
*   No strategic decisions were recorded in this thread. The sole action taken was the delegation of data access and collaboration rights.

**5. Key Dates & Follow-ups**
*   **Date Shared**: March 25, 2026, at 2:04 PM.
*   **System Identifier**: ID `19d254fd66c7dcde`.
*   **Follow-up Needed**: None explicitly stated; pending action depends on the Recipient's internal workflow regarding the "High Demand Search Queries" analysis.

**Summary of Resource Metadata**
*   **File Name**: Product_Ads_Analytics_Demand_&_Supply_High_Demand_Search_Queries_Baby-Child-Toys_>_Infant-Formula--1__E(20260325)__ID(69c3eb4efa2a5efc3cc8cab7)
*   **Platform**: Google Sheets (Google LLC, Mountain View, CA).
*   **Labels**: Inbox, Updates.


## [42/50] Spreadsheet shared with you: "Product_Ads_Analytics_Demand_&_Supply_High_Demand_Search_Queries_Baby-Child-Toys_>_Infant-Formula--1__E(20260304)__ID(69a7bed626389de5bba51941)"
Source: gmail | Thread: 19d254bc02296a8b | Labels: Inbox, Updates | Priority: None | Senders: Nikhil Grover (via . | Last Date: Wed, Mar 25, 2026, 2:00 PM | Last Updated: 2026-03-25T14:07:17.275442+00:00
**Daily Work Briefing: Product Ads Analytics Update**

**1. Key Participants & Roles**
*   **Nikhil Grover** (nikhil.grover@fairpricegroup.sg): Initiator of the shared resource; acting as data provider for analytics distribution.
*   **Recipient (You)**: End-user granted edit access to the shared spreadsheet.

**2. Main Topic/Request**
The primary communication concerns the sharing of a specific Google Sheets document titled "Product_Ads_Analytics_Demand_&_Supply_High_Demand_Search_Queries_Baby-Child-Toys_>_Infant-Formula--1__E(20260304)__ID(69a7bed626389de5bba51941)". The content focuses on high-demand search queries within the Baby/Child Toys category, specifically targeting "Infant Formula." Nikhil Grover has invited the recipient to **edit** this spreadsheet.

**3. Pending Actions & Ownership**
*   **Action**: Review and edit the shared analytics spreadsheet.
*   **Owner**: Recipient (You).
*   **Status**: Invitation sent; awaiting user interaction with the file link.

**4. Decisions Made**
*   No strategic decisions were recorded in this specific thread exchange. The action taken was the granting of "edit" permissions on the dataset by Nikhil Grover.

**5. Key Dates, Deadlines, & Follow-ups**
*   **Date of Communication**: March 25, 2026, at 2:00 PM.
*   **Last Message ID**: 19d254bc02296a8b.
*   **File Reference Date**: The file name indicates the data snapshot is from March 4, 2026 (E(20260304)).
*   **Deadline/Follow-up**: None specified in the current thread; immediate review is implied by the nature of a "Daily Work Briefing."

**Summary Note**
This email serves as an administrative notification regarding data access. No further action from Nikhil Grover is required at this stage. The recipient must now access the link provided to begin editing or analyzing the Infant Formula search query data.


## [43/50] [Search&Relevancy] Ticket - 4460996 Chatbot - App Issue
Source: gmail | Thread: 19d250ceeff727bb | Labels: Inbox, Forums | Priority: None | Senders: 'FairPrice Group' v. | Last Date: Wed, Mar 25, 2026, 12:51 PM | Last Updated: 2026-03-25T14:07:43.046749+00:00
**Daily Work Briefing: Search & Relevancy Ticket #4460996**

**Key Participants & Roles**
*   **Benny Lee (FairPrice Group Customer Service):** Originator of the request; escalated customer feedback to the Tech Team.
*   **Faith Chong (Customer):** Reported the technical issue via phone contact.
*   **Tech Team / Search & Relevancy:** Recipient of the escalation; responsible for investigation and rectification.

**Main Topic/Request**
Investigation and resolution of a persistent bug in the FairPrice mobile app's store locator functionality. Specifically, searching for "Towner Crescent" incorrectly redirects users to "Jalan Kayu" regardless of selection attempts. The customer noted this issue was previously reported at the physical outlet but remains unresolved.

**Pending Actions & Ownership**
*   **Action:** Investigate and rectify the search algorithm or mapping data error causing the redirect failure for Towner Crescent.
*   **Owner:** Tech Team / Search & Relevancy.
*   **Status:** Open; awaiting technical resolution based on customer feedback provided by CS.

**Decisions Made**
*   No formal decisions were recorded in this thread. The email serves as a direct escalation to trigger the technical fix process.
*   *Note:* Standard L1 Internal Escalation templates (RB, FS, Ecom, Loyalty) were attached but are not applicable to this specific app functionality bug.

**Key Dates & Deadlines**
*   **Issue Reported:** March 25, 2026, at approximately 4:48 PM (Customer call time).
*   **Escalation Sent:** March 25, 2026, at 12:51 PM.
*   **Urgency:** While the customer requested an urgent callback "by next day," the ticket was marked as **No** for urgent callback priority in the metadata. However, the CS team explicitly requested rectification.

**Specific References**
*   **Ticket ID:** 4460996
*   **Customer Details:** Faith Chong | Mobile: 90618109 | Email: fen_sg@yahoo.com.sg
*   **Affected Stores:** Towner Crescent (Target) vs. Jalan Kayu (Incorrect Redirect).
*   **Labels:** Inbox, Forums.


## [44/50] OOO - Travel 19th -27th Mar'26 Re: Urgent - PLA Impressions drop by 50%
Source: gmail | Thread: 19d24de93f9e8039 | Labels: Inbox | Priority: None | Senders: Anuj Nagpal | Last Date: Wed, Mar 25, 2026, 12:00 PM | Last Updated: 2026-03-25T14:07:55.345901+00:00
**Daily Work Briefing Summary**

**Key Participants & Roles**
*   **Anuj Nagpal** (anuj.nagpal@osmos.ai): Primary contact; currently Out of Office (Travel).
    *   *Context:* The subject line references a critical drop in PLA Impressions, but the provided content is solely Anuj's automated/unavailable response. No other sender or recipient names are present in the text body.

**Main Topic/Request**
*   **Subject:** Urgent issue regarding "PLA Impressions drop by 50%."
*   **Current Status:** The thread contains only a notification from Anuj Nagpal acknowledging receipt of an urgent query (presumably about the PLA metric drop) and stating his inability to respond immediately due to travel.

**Pending Actions & Ownership**
*   **Action Required:** Address the "Urgent - PLA Impressions drop by 50%" issue.
*   **Owner:** Unassigned in this specific email snippet; however, Anuj Nagpal is identified as the primary point of contact who will eventually need to address it.
*   **Immediate Escalation Path:** For anything urgent while Anuj is away, contacts are instructed to call or WhatsApp him directly rather than relying on email.

**Decisions Made**
*   No strategic decisions regarding the 50% drop in PLA impressions were made in this specific message; it is purely a status update on Anuj's availability.

**Key Dates & Deadlines**
*   **Current Date:** March 25, 2026 (Time: 12:00 PM).
*   **OOO Period:** March 19, 2026 – March 27, 2026.
*   **Return Date:** Expected availability resumes after March 27, 2026.
*   **Follow-up:** Anuj will respond once he returns from travel; no specific reply deadline was set in the note beyond standard urgency protocols (call/WhatsApp).

**Specific References & Metadata**
*   **Resource Note:** OOO - Travel dates confirmed as 19th - 27th Mar'26.
*   **Metric Alert:** PLA Impressions dropped by 50%.
*   **Message ID:** 19d24de93f9e8039.
*   **Labels:** Inbox.


## [45/50] Invitation: G5: Building a Better Workplace Together: Your Feedback M... @ Tue Apr 7, 2026 11am - 11:45am (SGT) (Michael Bui)
Source: gmail | Thread: 19d244719fe66719 | Labels: Inbox | Priority: None | Senders: Melissa Hauw | Last Date: Wed, Mar 25, 2026, 9:15 AM | Last Updated: 2026-03-25T10:01:29.887439+00:00
**Daily Work Briefing: G5 Workplace Feedback Focus Group**

**1. Key Participants & Roles**
*   **Melissa Hauw** (melissa_hauw@fairpricegroup.sg): Organizer/Sender of the engagement survey follow-up.
*   **Michael Bui**: Primary invitee/Participant for the session.
*   **Team Members**: General staff at FairPrice Group (FPG) invited to participate in the focus group.

**2. Main Topic & Request**
*   **Topic**: Discussion of 2025 engagement survey findings and collaborative solution-finding to improve the workplace environment.
*   **Request**: Participation in a virtual Focus Group Discussion titled "G5: Building a Better Workplace Together."
*   **Format**: 45-minute session conducted via Slido (participants must have phones ready). Responses will be anonymized to ensure candid input without individual/team assessment.

**3. Pending Actions & Ownership**
*   **Action**: Attend the Focus Group Discussion.
    *   **Owner**: Michael Bui and all invited team members.
    *   **Status**: Awaited (Meeting scheduled for April 7).
*   **Action**: Provide open, candid feedback on survey drivers, current challenges, and improvement ideas.
    *   **Owner**: All participants.

**4. Decisions Made**
*   No specific strategic decisions were recorded in this thread; the session is structured to *gather* input that will shape future FPG-level actions.
*   **Assurance Established**: The session focuses on identifying themes at the organizational level, not assessing individuals or teams.

**5. Key Dates & Logistics**
*   **Meeting Date/Time**: Tuesday, April 7, 2026, 11:00 AM – 11:45 AM (SGT).
*   **Virtual Access**:
    *   **Platform**: Slido (via Google Meet link provided in original invitation).
    *   **Google Meet Link**: `meet.google.com/eme-quew-dmw`
    *   **Phone Dial-in (US)**: +1 475-355-7387 | **PIN**: 222510805.
*   **Context Reference**: Follow-up to the 2025 engagement survey.


## [46/50] Invitation: Project Light: Spotlight Topic - Payments @ Wed Mar 25, 2026 4:30pm - 5:30pm (SGT) (Michael Bui)
Source: gmail | Thread: 19d2428aedda345f | Labels: Inbox | Priority: None | Senders: Jacob Yeo | Last Date: Wed, Mar 25, 2026, 8:42 AM | Last Updated: 2026-03-25T10:01:51.236483+00:00
**Daily Work Briefing: Project LIGHT – Spotlight Session on Payments**

**Meeting Overview**
*   **Topic:** Project LIGHT Workshop: Spotlight Topic – Payments.
*   **Date & Time:** Wednesday, March 25, 2026, 4:30 PM – 5:30 PM (SGT).
*   **Location/Link:** Google Meet (`meet.google.com/qos-xode-gpd`). Phone access available for US region (+1 931-486-4222, PIN: 979457835).
*   **Organizer:** Jacob Yeo (jacob.yeo@fairpricegroup.sg).

**Key Participants & Roles**
*   **Jacob Yeo:** Session organizer; coordinator for alignment on integration flows.
*   **Product/Tech Teams:** Primary attendees invited via the larger workshop invite; responsible for defining dependencies and sequencing.

**Main Topic & Objectives**
The session is designed to align stakeholders on the following:
1.  **Integration Flows:** Map end-to-end integration between Project LIGHT and existing Payment systems.
2.  **Dependencies:** Identify critical Sequencing requirements necessary for the **September release** and subsequent milestones.
3.  **Risk Management:** Surface gaps, risks, and specific ownership areas requiring follow-up actions.

**Decisions Made**
*   No formal decisions recorded in this thread; the session is a planning and alignment workshop.
*   Confirmation that most product and tech team members are already included in the broader workshop invitation.

**Pending Actions & Ownership**
*   **Action:** Attend the spotlight session to discuss integration flows and dependencies.
    *   **Owner:** All invited Product/Tech participants.
*   **Action:** Identify and document gaps, risks, and ownership areas during the meeting.
    *   **Owner:** Session attendees (to be captured post-meeting).
*   **Action:** Follow up on identified risks and ownership assignments.
    *   **Owner:** Relevant team leads/owners as determined during the session.

**Key Dates & Deadlines**
*   **Meeting Date:** March 25, 2026.
*   **Critical Release Milestone:** September 2026 (Project LIGHT release).
*   **Next Steps:** Post-session documentation of dependencies and risk registers must be completed to support the September timeline.

**System References**
*   Last Message ID: `19d2428aedda345f`
*   Labels: Inbox


## [47/50] [Confluence] Digital Product Development > Handover Identity scope
Source: gmail | Thread: 19d2415af3ab8ce7 | Labels: Inbox, Updates | Priority: None | Senders: Tan Nhu Duong (Conf. | Last Date: Wed, Mar 25, 2026, 8:21 AM | Last Updated: 2026-03-25T10:02:01.586424+00:00
**Daily Work Briefing: Handover Identity Scope (Confluence)**

**Key Participants & Roles**
*   **Tan Nhu Duong**: Confluence system user/observer; identified the need for documentation updates. Email sender from Atlassian service.
*   **Jack Zin Oo Paing**: Subject of an inline comment; expected to document Knowledge Transfer (KT) details.

**Main Topic/Request**
Notification regarding a single inline comment update on the Confluence page **"Handover Identity scope"** within the space *Digital Product Development*. The core request is for Jack Zin Oo Paing to record the description of a recent **KT session recording** into the third column of the page while his memory of the session remains fresh.

**Pending Actions & Ownership**
*   **Action**: Add a description of the KT session content to the "3rd column" of the *Handover Identity scope* page.
*   **Owner**: Jack Zin Oo Paing.
*   **Trigger Condition**: Execute immediately while memory of the session is fresh.

**Decisions Made**
*   No formal decisions were recorded in this thread. The interaction represents a procedural request for documentation completeness based on a recent knowledge transfer event.

**Key Dates & Follow-ups**
*   **Date of Notification**: March 25, 2026, at 8:21 AM.
*   **Reference Document**: [Confluence] Digital Product Development > Handover Identity scope.
*   **Follow-up ID**: Last message ID `19d2415af3ab8ce7`.
*   **Upcoming Deadline**: Not explicitly stated, but prioritized for immediate completion ("memory is still fresh").

**Metadata Context**
*   **Labels**: Inbox, Updates.
*   **Priority**: Unassigned (null).


## [48/50] Notes: “RMN integration planning” Mar 25, 2026
Source: gmail | Thread: 19d240b8bf6af76f | Labels: Inbox | Priority: None | Senders: Gemini | Last Date: Wed, Mar 25, 2026, 8:10 AM | Last Updated: 2026-03-25T10:02:19.517429+00:00
**Daily Work Briefing: RMN Integration Planning (Mar 25, 2026)**

**Key Participants & Roles**
*   **Gemini:** Auto-generated meeting notes from the "RMN integration planning" session held March 25, 2026.
*   **Rahul Jain:** Primary action owner for technical verification, data storage, latency analysis, and partner coordination.
*   **Nikhil Grover:** Action owner for filtering logic, documentation management, and user story preparation.

**Main Topic & Request**
The session focused on finalizing the global ad strategy and RMN integration architecture. Key discussions covered:
1.  **Ad Delivery:** Implementing a global ad structure with API parameters to support various formats across the customer journey. Principles mandate no ads on out-of-stock products and competitive separation. Relevance will be managed via boost/tag approaches, keeping non-endemic brands outside the main shopping journey.
2.  **Payment & Events:** Enabling payment method promotions (banners/sponsored vouchers) and order tracking page banners for non-endemic brands using a global ad object. Critical requirement: Decision needed on secure PII storage for lead generation.
3.  **Back Office:** Managing inventory, booking formats, banner sequencing, and story ads with sequential targeting via Osmos. Integration pillars include platform setup, ad serving, reporting, and billing.

**Decisions Made**
*   **Ad Object:** A unified global ad object will be utilized for flexibility across all integration topics (setup, serving, reporting, billing).
*   **Compliance:** Product ads require dynamic filters; impression compliance must verify a 1-second viewability threshold.
*   **Platform Logic:** Non-endemic brands are to be focused outside the main shopping journey via specific tagging.

**Pending Actions & Ownership**
*   **[Rahul Jain]:**
    *   Determine lead generation data storage and PII transfer method to advertisers.
    *   Provide max/min latency numbers and corresponding peak request rates.
    *   Verify if the product feed includes a tag list; check UDP info for FPG.
    *   Finalize custom targeting methodology and implement banner targeting using UDP IDs.
    *   Increase TPA request limit to 50 (verify maximum product number).
    *   Confirm UDP targeting/filtration methods to achieve Product Ads on campaign pages.
    *   Consult with Indian retailer partner regarding consent flags for programmatic ads.
    *   Investigate missing 1-second viewability threshold and provide implementation guidance for ad impression triggers.
*   **[Nikhil Grover]:**
    *   Finalize and provide the full list of dynamic product ad filters.
    *   Transfer the work-in-progress document to Google Docs and share updates.
    *   Complete existing display and product ad user stories.
    *   Prepare and send new user stories focusing on catalog sync and audience sync.

**Key Dates & Follow-ups**
*   **Meeting Date:** March 25, 2026 (Notes auto-generated at 4:09 PM GMT+08:00).
*   **Next Steps:** Immediate execution of the assigned action items by Rahul Jain and Nikhil Grover to finalize integration parameters and documentation.


## [49/50] Invitation: Project Light: Spotlight Topic - HIVE/Inventory @ Wed Mar 25, 2026 3:30pm - 4:30pm (SGT) (Michael Bui)
Source: gmail | Thread: 19d23ea0c9873128 | Labels: Inbox | Priority: None | Senders: Jacob Yeo | Last Date: Wed, Mar 25, 2026, 7:33 AM | Last Updated: 2026-03-25T10:02:33.516462+00:00
**Daily Work Briefing: Project LIGHT Workshop Invitation**

**Key Participants & Roles**
*   **Organizer:** Jacob Yeo (Snr Manager, Product Governance, Omnichannel COE).
*   **Facilitators:** Gopalakrishna Dhulipati (Gopal) and Hui Hui Voon.
*   **Attendees:** Fion Tan, Muni Vinay Kamisetty, Madhukar Vemula, Shawn Hu, Kai Xian Wong, Enoch Zhang, Hebin Huang, Suraj Taneja, Danielle Lee, Kenneth Yeo, Mervyn Yap, Qiuyan Tian, Yi Hao Tan, Prabhu Palanivelu, Alvin Choo, Akash Gupta, Daryl Ng, Koklin Gan, Michael Bui, Ravi Goel, and Tiong Siong Tee.
*   **Your Status:** Michael Bui (RSVP: Pending/Not yet confirmed in thread).

**Main Topic & Request**
*   **Event:** "Project LIGHT" workshop spotlight session focused on **HIVE/Inventory**.
*   **Objective:** Align on end-to-end integration flows between Project LIGHT and HIVE/inventory systems; identify key dependencies, sequencing for the September release, and surface gaps, risks, and ownership areas.
*   **Request:** Attendance at the scheduled meeting to facilitate alignment.

**Key Dates & Logistics**
*   **Date:** Wednesday, March 25, 2026.
*   **Time:** 3:30 PM – 4:30 PM (SGT).
*   **Location:** FairPrice Hub, L10, Training Room 2.
*   **Virtual Access:** Google Meet link provided (`meet.google.com/kix-eitm-spk`); Phone options available for US (+1 708-998-2306) and other regions (PIN: 772612594).

**Pending Actions & Ownership**
*   **Action:** Confirm attendance/RSVP.
*   **Owner:** All invited guests, specifically Michael Bui.
*   **Preparation:** Review current integration flows and dependency maps prior to the session to contribute effectively during the "surface gaps" discussion.

**Decisions Made**
*   No final decisions recorded in this thread; the meeting is convened to *identify* dependencies and risks for future decision-making regarding the September release timeline.

**Follow-ups**
*   Post-meeting: Facilitators (Gopal, Huihui) will address identified gaps and ownership areas requiring follow-up.


## [50/50] Deletion notice for your Google Cloud Shell home directory
Source: gmail | Thread: 19d23d47f0c52730 | Labels: Inbox, Updates | Priority: None | Senders: noreply-cloudshell | Last Date: Wed, Mar 25, 2026, 7:10 AM | Last Updated: 2026-03-25T10:02:44.127153+00:00
**Daily Work Briefing: Google Cloud Shell Deletion Notice**

**Key Participants & Roles**
*   **Sender:** `noreply-cloudshell@google.com` (Automated system notification from Google).
*   **Recipient:** Current Google Cloud Shell user (You/Executive).
*   **Role:** System Administrator/User responsible for maintaining local development environment data.

**Main Topic/Request**
The sender issued an automated notice stating that the recipient's Google Cloud Shell home directory has been inactive for over 120 days. Consequently, the system will automatically schedule the directory and its contents for deletion in 7 days unless action is taken to retain it.

**Pending Actions & Ownership**
*   **Action:** Log into the Google Cloud Platform console and open a new Cloud Shell session before the deadline to prevent data loss. Alternatively, manually backup any critical files currently residing in the home directory prior to deletion.
*   **Owner:** You (The recipient).

**Decisions Made**
No decisions were made by the user or sender within this thread; this is a unilateral system notification requiring user response to avoid data loss.

**Key Dates, Deadlines & Follow-ups**
*   **Notification Date:** March 25, 2026, at 7:10 AM.
*   **Inactivity Period Triggered:** >120 days since last login.
*   **Critical Deadline:** In 7 days from the notification date (approximately April 1, 2026), the home directory will be scheduled for deletion.
*   **Follow-up Required:** Immediate action to open Cloud Shell or backup data is required to retain existing files.

**Impact Analysis**
*   **If Action Taken:** The home directory and all associated data are preserved.
*   **If No Action Taken:** Only the Cloud Shell home directory content is lost. Access to Google Cloud projects, App Engine, Compute Engine, and other services remains unaffected; a fresh session will generate a new, empty home directory upon next login.
