

## [1/58] [Bitbucket]  Pipeline for master failed on 22b106d (ntuclink/website-service)
Source: gmail | Thread: 19d3c707df3654ae | Labels: Inbox, Updates | Priority: None | Senders: Bitbucket | Last Date: Mon, Mar 30, 2026, 1:51 AM | Last Updated: 2026-03-30T02:01:21.231015+00:00
**Daily Work Briefing: Bitbucket Pipeline Failure**

**1. Key Participants & Roles**
*   **Michael Bui**: Developer/Contributor (Committed code `22b106d`).
*   **Lester Santiago Soriano**: Approver of Pull Request #652.
*   **Zaw Myo Htet**: Approver of Pull Request #652.
*   **Bitbucket System**: Automated notification source (failed pipeline trigger).

**2. Main Topic/Request**
The `master` branch pipeline for the `ntuclink/website-service` repository on Bitbucket has failed immediately following a merge. The failure is attributed to test execution results in commit `22b106d`.
*   **Merge Context**: Pull Request #652 (Ticket: DPD-715), titled "Fix shared position map mutation in ReorderProductsAds".

**3. Pending Actions & Ownership**
*   **Action**: Investigate and resolve the pipeline failure where 0 out of 1,153 tests passed (interpreted as 1,153 tests failed based on standard CI failure reporting context).
*   **Owner**: Michael Bui (as the committer) or the development team responsible for `website-service`. No specific assignment is mentioned in the thread; ownership defaults to the author of the failing commit.

**4. Decisions Made**
*   The code change defined in DPD-715 was merged into the `master` branch despite subsequent pipeline failure, indicating the merge occurred before the full test suite validation or the CI gate failed post-merge.

**5. Key Dates, Deadlines & Follow-ups**
*   **Date/Time of Failure**: March 30, 2026, at 1:51 AM.
*   **Duration of Pipeline Run**: 6 minutes and 40 seconds.
*   **Commit Hash**: `22b106d`.
*   **Follow-up Required**: Immediate review of the test results to identify the cause of the mutation failure in `ReorderProductsAds` before further deployments.

**Summary**
The automated pipeline for `ntuclink/website-service` failed on March 30, 2026 (1:51 AM), halting progress on `master`. The failure occurred after Michael Bui merged PR #652 (DPD-715) approved by Lester Santiago Soriano and Zaw Myo Htet. The pipeline reported a critical test failure rate (0/1153 tests passed). Immediate investigation is required to address the shared position map mutation issue introduced in this commit.


## [2/58] Re: [Bitbucket] Pull request #652: DPD-715: Fix shared position map mutation in ReorderProductsAds (ntuclink/website-service)
Source: gmail | Thread: 19d3c5101edbc5b5 | Labels: Inbox, Updates | Priority: None | Senders: Zaw | Last Date: Mon, Mar 30, 2026, 1:46 AM | Last Updated: 2026-03-30T02:01:36.593132+00:00
**Daily Work Briefing: Pull Request #652 (DPD-715)**

**Key Participants & Roles**
*   **Zaw Myo Htet:** Reviewer/Approver.
*   **Lester Santiago Soriano:** Reviewer/Approver.
*   **Daryl Ng:** Reviewer/Approver.
*   **ntuclink/website-service:** Repository owner of the pull request.

**Main Topic/Request**
Review and approval of Pull Request #652 regarding ticket **DPD-715**. The PR addresses a technical defect titled "Fix shared position map mutation in ReorderProductsAds."

**Decisions Made**
Three separate approvals were recorded for this specific pull request:
1.  **Zaw Myo Htet** approved the changes on March 30, 2026, at 1:17 AM.
2.  **Lester Santiago Soriano** approved the changes on March 30, 2026, at 1:24 AM.
3.  **Daryl Ng** approved the changes on March 30, 2026, at 1:46 AM.

All three reviewers have officially signified approval for the code changes associated with DPD-715.

**Actions Pending & Ownership**
*   **Merge Action:** While approvals are secured, the specific action of merging the pull request is not explicitly detailed in this email thread as completed. The PR remains in a state where it has received necessary approvals.
*   **Ownership:** The merge responsibility typically falls to the repository maintainers or the original author (not listed in these approval notifications), though no specific owner was assigned a pending task in this text.

**Key Dates & Deadlines**
*   **March 30, 2026, 1:17 AM:** First approval received (Zaw Myo Htet).
*   **March 30, 2026, 1:24 AM:** Second approval received (Lester Santiago Soriano).
*   **March 30, 2026, 1:46 AM:** Third approval received (Daryl Ng).
*   **No deadlines or follow-up dates** are specified in the provided content.

**Summary Status**
The pull request #652 for DPD-715 has successfully secured three approvals within a 29-minute window on March 30, 2026. The technical issue regarding shared position map mutation in `ReorderProductsAds` has been validated by Zaw Myo Htet, Lester Santiago Soriano, and Daryl Ng.


## [3/58] Opsgenie Alert: [Datadog] [P4] [Triggered] Service marketing-service has an abnormal change in throughput on env:prod
Source: gmail | Thread: 19d3bfcc25dc99ae | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Sun, Mar 29, 2026, 11:50 PM | Last Updated: 2026-03-30T02:01:58.055493+00:00
**Daily Work Briefing: Opsgenie Alert Summary**

**1. Key Participants & Roles**
*   **System/Source:** Opsgenie (Notification Engine), Datadog (Monitoring Source).
*   **Alert Owner:** DPD Staff Excellence - Retail Media.
*   **Notify Channels:** `@hangouts-dd-dpd-grocery-alert` (Google Hangouts channel), `@opsgenie-dpd-grocery-retail-media` (Opsgenie responder group).
*   **Service Owner:** `marketing-service`.

**2. Main Topic/Request**
*   **Alert Type:** P4 Priority Alert regarding abnormal throughput changes in the production environment (`env:prod`).
*   **Specific Trigger:** 100% of `sum:trace.http.request.hits{env:prod,service:marketing-service}` values exceeded 3 deviations from predicted values over the last 15 minutes.
*   **Request:** Immediate investigation of service health via provided Datadog APM links, Kubernetes (GCP) console, and Runbook documentation.

**3. Pending Actions & Ownership**
*   **Action:** Investigate throughput anomaly, review metrics graphs, and determine root cause for `marketing-service`.
*   **Owner:** DPD Staff Excellence - Retail Media (Assigned via Opsgenie responders).
*   **Required Resources:**
    *   Datadog APM: [Link to marketing-service operations](https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod)
    *   Kubernetes Console: [GCP Cluster Overview](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview?cloudshell=false&project=fponprd)
    *   Runbook: [Atlassian Wiki - marketing-service](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book)

**4. Decisions Made**
*   None recorded in this thread; the alert is currently active and awaiting human intervention.

**5. Key Dates, Deadlines & Follow-ups**
*   **Alert Trigger Time:** Mar 30, 2026, at 11:44 PM UTC (Last Updated: 2026-03-29 23:44:10 +0000).
*   **Notification Timestamps:**
    *   First Opsgenie Notification: Mar 29, 2026, 11:45 PM.
    *   Duplicate Notification Received: Mar 29, 2026, 11:50 PM.
*   **Integration Created At:** Mar 30, 2026, 7:45:13 AM (System timestamp discrepancy noted in metadata).
*   **Follow-up Required:** Immediate resolution or status update required by the Retail Media team to clear the P4 alert status.

**Technical Metadata**
*   **Monitor ID:** 17447110
*   **Event ID:** 8565860058801546694
*   **Tags:** `env:prod`, `service:marketing-service`, `managed_by:datadog-sync`, `priority:p4`
*   **Alert Snapshot Link:** [Datadog Monitor Snapshot](https://app.datadoghq.eu/monitors/17447110?from_ts=1774826950000&to_ts=1774828150000&event_id=8565860058801546694)


## [4/58] You have no events scheduled today.
Source: gmail | Thread: 19d3b6b347f5f06b | Labels: Inbox, Updates | Priority: None | Senders: Google Calendar | Last Date: Sun, Mar 29, 2026, 9:06 PM | Last Updated: 2026-03-29T22:04:31.516241+00:00
**Daily Work Briefing Summary**

**Key Participants & Roles**
*   **Michael Bui**: Account holder (michael.bui@fairpricegroup.sg).
*   **Google Calendar System**: Automated notification sender.

**Main Topic/Request**
*   Automated delivery of a "daily agenda" notification confirming the absence of scheduled events for the specified date. This communication is triggered by subscription to the **"Digital Business Tech Release/Changes"** calendar.

**Pending Actions & Ownership**
*   **No actions pending.** The email explicitly states there are no events scheduled, and no tasks require attention or ownership as of this briefing.

**Decisions Made**
*   None recorded in this thread. This is an informational status update only.

**Key Dates, Deadlines, & Follow-ups**
*   **Notification Sent**: March 29, 2026, at 9:06 PM.
*   **Relevant Date**: Monday, March 30, 2026 (No events scheduled).
*   **Follow-up**: None required based on current content.
*   **Account Configuration**: If agenda settings need modification regarding which calendars are monitored, the user must log in to `https://calendar.google.com/calendar/`.

**Additional Metadata**
*   **Labels**: Inbox, Updates.
*   **Priority**: Unspecified (null).
*   **Last Message ID**: 19d3b6b347f5f06b.


## [5/58] Opsgenie Alert: [Datadog] [P2] [Triggered] Marketing Service Gateway Error
Source: gmail | Thread: 19d3ae5eb3b0090e | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Sun, Mar 29, 2026, 6:45 PM | Last Updated: 2026-03-29T22:04:50.307013+00:00
**Daily Work Briefing: Marketing Service Gateway Incident**

**1. Key Participants & Roles**
*   **System:** Opsgenie (Alerting System) receiving data from Datadog.
*   **Affected Team:** DPD Staff Excellence - Retail Media (`@opsgenie-dpd-grocery-retail-media`).
*   **Integration Source:** `dpd-grocery-retail-media-eu` (Datadog).

**2. Main Topic/Request**
An automated P2 alert triggered due to a production error spike in the Marketing Gateway service. The service is responsible for banners, video ads, and authentication.
*   **Error Volume:** >1,000 log events matched within the last 5 minutes.
*   **Monitored Query:** `service:martech-personalization-service-api-gateway env:prod status:error`.

**3. Pending Actions & Ownership**
*   **Action:** Investigate and resolve the high volume of error logs in the production environment for the Martech Personalization Service API Gateway.
*   **Owner:** DPD Staff Excellence - Retail Media (as designated responders).
*   **Reference Links:**
    *   Datadog Monitor: https://app.datadoghq.eu/monitors/65699796

**4. Decisions Made**
No manual decisions recorded in this thread; the alert was automated by system monitoring rules without human intervention noted in the log history.

**5. Key Dates & Timeline**
*   **Alert Trigger Time:** March 29, 2026, at 18:39:36 UTC (Last Updated).
*   **Notification Timestamps (Opsgenie):**
    *   Mar 29, 2026, 6:40 PM
    *   Mar 29, 2026, 6:42 PM
    *   Mar 29, 2026, 6:45 PM
*   **System Creation Timestamp:** Mar 30, 2026, at 2:40:37 AM (Note: This appears to be a system generation timestamp distinct from the alert trigger time).
*   **Alert ID:** `71c276fd-1010-4578-b555-effd2bb881a3-1774809637590` (TinyId: 139261).
*   **Last Message ID:** `19d3aea79f9a34bb`.

**Status Summary:** The alert has been generated and routed to the Retail Media team three times within a 5-minute window. No resolution or status update comments are present in the provided thread log. Immediate investigation is required by the assigned team.


## [6/58] Opsgenie Alert: [Datadog] [P2] [Warn] Service marketing-service has a high error rate on env:prod
Source: gmail | Thread: 19d35a661786941f | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Sun, Mar 29, 2026, 2:12 PM | Last Updated: 2026-03-29T22:05:24.977305+00:00
**Daily Work Briefing: Opsgenie Alert Summary (Updated)**

**Key Participants & Roles**
*   **System/Integration:** Opsgenie (Alerting) and Datadog (Monitoring Source).
*   **Responders/Owner:** DPD Staff Excellence - Retail Media.
*   **Notification Channels:** `@hangouts-dd-dpd-grocery-alert` (Google Hangouts) and `@opsgenie-dpd-grocery-retail-media`.

**Main Topic & Request**
An automated P2 warning alert remains active for the production environment (`env:prod`) regarding the `marketing-service`. The system detects a high HTTP error rate where the ratio of errors to total hits exceeds the 5% threshold (trigger condition: `> 0.05`). Despite recent metric improvements, the alert continues to trigger P2 notifications.

**Alert Details**
*   **Service:** `marketing-service`
*   **Environment:** Production (`prod`)
*   **Triggered Metric:** Error Rate over the last 10 minutes.
*   **Query:** `sum(last_10m):( sum:trace.http.request.errors{env:prod,service:marketing-service}.as_count()/sum:trace.http.request.hits{env:prod,service:marketing-service}.as_count() ) > 0.05`
*   **Threshold vs. Actual:** Threshold > 0.05; Current Metric Value: 0.014 (Latest update).
    *   *Note:* Previous values ranged from 0.044 to 0.011. The metric has stabilized at 0.014, yet the P2 alert persists.
*   **Alert ID/Event ID:** `2876abed-d7c2-442b-b7be-247333e4f4b5-1774793229072` / Event ID `8565278154849940428`.
*   **Monitor URL:** https://app.datadoghq.eu/monitors/17447106
*   **Snapshot Link:** https://app.datadoghq.eu/monitors/17447106?from_ts=1774792266000&to_ts=1774793466000&event_id=8565278154849940428
*   **Datadog Tags:** `env:prod`, `service:marketing-service`, `managed_by:datadog-sync`, `monitor`, `priority:p2`.

**Pending Actions & Ownership**
*   **Action:** Immediate investigation required to resolve why the P2 alert persists despite metric values (0.014) falling below the 5% threshold. Review recent alerts for recurrence and confirm if this is a false positive or intermittent issue.
*   **Owner:** DPD Staff Excellence - Retail Media.
*   **Required Checks (as per runbook):**
    1.  Review Datadog APM resources: [Datadog Link](https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod)
    2.  Review Kubernetes deployment status: [GCP K8s Link](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview?cloudshell=false&project=fponprd)
    3.  Consult the official Runbook: [Atlassian Wiki Link](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book)

**Decisions Made**
No human decisions were recorded in this thread; all entries are automated system notifications. The alert remains active as of Mar 29, 2026, at 14:06 UTC (Local time approx. 2:07 PM).

**Key Dates & Timeline**
*   **Latest Alert Update:** Mar 29, 2026, at 14:06:06 +0000 (Metric Value: 0.014).
*   **Notification Sent:** Mar 29, 2026, at 10:07:09 PM UTC (Created At), with subsequent identical notifications logged at 2:07 PM, 2:09 PM, and 2:12 PM local time.
*   **Previous Activity:** Earlier alerts on Mar 28, 2026, showed a metric value of 0.044.

**Status Note**
The alert status remains "Warn" (P2) for the production environment. Although the current metric value (0.014 or 1.4%) is significantly below the 5% threshold (>0.05), the system continues to generate P2 notifications. Immediate investigation per the provided links and runbook is required to determine why the alert persists despite improved metrics and to rule out intermittent issues.


## [7/58] [Action Required] Service Account Key Expiring, Renewal Required - a36a1c8b456f387db4ba32e73f8a243479423bf0
Source: gmail | Thread: 19d38b3c9f3ad7ec | Labels: Inbox, Forums | Priority: None | Senders: noreply-sre | Last Date: Sun, Mar 29, 2026, 8:26 AM | Last Updated: 2026-03-29T10:01:34.356027+00:00
**Daily Work Briefing: Service Account Key Expiration Notice**

*   **Key Participants & Roles:**
    *   **Sender:** `noreply-sre@ntucenterprise.sg` (SRE Team/Notification System).
    *   **Recipient:** The service account owner responsible for the `fpon-224503/seller-analytics-service`.

*   **Main Topic/Request:**
    *   Notification that the service account key `a36a1c8b456f387db4ba32e73f8a243479423bf0` for the account `fpon-224503/seller-analytics-service@fpon-224503.iam.gserviceaccount.com` is scheduled to expire.
    *   Immediate instruction to rotate this key before expiration to prevent authentication failures and service disruption.

*   **Pending Actions & Ownership:**
    *   **Action:** Download the newly issued service account key (sent separately) and replace the existing key in the target system.
    *   **Owner:** The ticket owner/service account administrator.
    *   **Alternative Action:** If the key is determined to be stale, a SRE request must be raised to permanently remove it.

*   **Decisions Made:**
    *   None recorded in this thread; this is an automated notification requiring recipient action.

*   **Key Dates & Deadlines:**
    *   **Notification Date:** March 29, 2026 (8:26 AM).
    *   **Expiration Deadline:** April 28, 2026. The key becomes invalid after this date.
    *   **Follow-up:** Await the separate email containing the new service account credentials to initiate rotation immediately upon receipt.


## [8/58] [Dashboard Report] Retail Media - DD Dashboard | Sun 29 Mar 11:00AM +08
Source: gmail | Thread: 19d378a961f79e91 | Labels: Inbox, Updates | Priority: None | Senders: Datadog HQ | Last Date: Sun, Mar 29, 2026, 3:02 AM | Last Updated: 2026-03-29T06:01:45.068609+00:00
**Daily Work Briefing: Retail Media Datadog Dashboard Update**

**Key Participants & Roles**
*   **Datadog HQ (no-reply@dtdg.eu):** Service Provider/Sender. Automated sender on behalf of the "Team Datadog."
*   **Michael:** Recipient (Internal Stakeholder/Client). Primary point of contact for the report delivery.

**Main Topic & Request**
Delivery of the **"Retail Media - DD Dashboard"** report containing data aggregated over the past three days leading up to March 29, 2026. The email serves as a notification that the attachment is available for review and monitoring purposes.

**Pending Actions & Ownership**
*   **Action:** Review the attached dashboard report (containing 3 days of historical data).
*   **Owner:** Michael.
*   **Status:** Awaiting receipt/acknowledgment or internal analysis by Michael. No further action from Datadog HQ is required at this stage.

**Decisions Made**
None recorded in this thread. The communication is a standard automated delivery notification without explicit decision-making logs.

**Key Dates & Deadlines**
*   **Report Generation Date:** Sunday, March 29, 2026 (11:00 AM +08).
*   **Data Range:** Past 3 days relative to the report generation date.
*   **Sent Timestamp:** March 29, 2026, at 3:02 AM (Timezone not specified in body, but server timestamp indicates early morning UTC/Europe likely given "HQ <no-reply@dtdg.eu>").

**Specific References & Metadata**
*   **Report Title:** Retail Media - DD Dashboard.
*   **Sender Email:** no-reply@dtdg.eu.
*   **Last Message ID:** 19d378a961f79e91.
*   **Labels:** Inbox, Updates.
*   **Datadog HQ Address:** 620 8th Avenue, 45th Floor, New York, NY 10018.
*   **Recipient Name:** Michael.

**Summary for Executive Review**
The automated system from Datadog HQ successfully delivered the latest Retail Media performance report to Michael on March 29, 2026. The content covers a 72-hour window ending at the time of generation. No follow-up requests or escalations were initiated by the sender; the ball is now in Michael's court to analyze the metrics.


## [9/58] Opsgenie Alert: [Datadog] [P4] [Triggered] Service marketing-service has an abnormal change in throughput on env:prod
Source: gmail | Thread: 19d36f49cbc748cd | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Sun, Mar 29, 2026, 1:26 AM | Last Updated: 2026-03-29T02:01:05.109307+00:00
**Daily Work Briefing: Opsgenie Alert Summary**

**1. Key Participants & Roles**
*   **System:** Opsgenie (Alerting System) and Datadog (Monitoring Source).
*   **Notification Targets:**
    *   `@hangouts-dd-dpd-grocery-alert` (Hangouts Group: Operations/Incident Response).
    *   `@opsgenie-dpd-grocery-retail-media` (Opsgenie Team Channel).
*   **Assigned Responders:** DPD Staff Excellence - Retail Media.

**2. Main Topic & Request**
*   **Subject:** Abnormal throughput change detected in the `marketing-service` production environment (`env:prod`).
*   **Alert Type:** P4 Priority Anomaly Detection.
*   **Trigger Condition:** 100% of trace HTTP request hit values deviated by more than 3 standard deviations from predicted values over a 15-minute window.
*   **Requested Actions:** Immediate investigation via provided links to Datadog APM, Google Kubernetes Engine (GKE) deployment overview, and the specific Runbook.

**3. Pending Actions & Ownership**
*   **Action:** Investigate service throughput anomaly using supplied monitoring links.
*   **Owner:** DPD Staff Excellence - Retail Media (Assigned via Opsgenie responder group).
*   **Reference Links Provided:**
    *   Datadog APM: `marketing-service` operations.
    *   Kubernetes Console: `asia-southeast1/fpon-cluster/default/marketing-service`.
    *   Runbook: `NTUCLink - marketing-service Run book`.

**4. Decisions Made**
*   No human decisions or mitigations recorded in this thread yet; the content consists entirely of automated system alerts indicating an ongoing, unresolved issue.

**5. Key Dates & Timeline**
*   **March 29, 2026, 12:18 AM (UTC):** Initial alert triggered. Last Updated: 00:17:10 +0000. Created At: 08:18:13 AM (System timestamp).
*   **March 29, 2026, 12:23 AM (UTC):** Duplicate alert received (Last Updated same as initial).
*   **March 29, 2026, 1:21 AM (UTC):** Alert updated/retriggered. Last Updated: 01:20:10 +0000. Created At: 09:21:12 AM (System timestamp).
*   **March 29, 2026, 1:26 AM (UTC):** Duplicate of the 1:21 AM alert received.

**Status:** Alert remains active with repeated notifications indicating no resolution or acknowledgment has been logged in this thread.


## [10/58] [RAW Overdue] Expired Risk Acceptance & Waiver Form
Source: gmail | Thread: 19d371d74be27bd7 | Labels: Inbox | Priority: None | Senders: cyberrisk.automation | Last Date: Sun, Mar 29, 2026, 1:02 AM | Last Updated: 2026-03-29T02:01:22.713174+00:00
**Daily Briefing: Resource [RAW Overdue] Expired Risk Acceptance & Waiver Form**

**Key Participants & Roles**
*   **Cyber Risk Team / Automation System:** Sender of the reminder; responsible for monitoring expiry and reviewing remediation evidence. Contact: `cyberRisk@ntucenterprise.sg`.
*   **Technology Governance and Compliance Team:** Recipient for form sharing to ensure correct completion prior to sign-off. Contact: `techgrc@ntucenterprise.sg`.
*   **Requestor (Entity Owner):** The individual responsible for raising the new RAW request, completing Section A, and securing approvals. Currently unspecified in thread but is the target audience of this alert.

**Main Topic/Request**
The system has detected an expired Risk Acceptance & Waiver (RAW) form for the asset **Signcloud Saas User access management** (Entity: FPG-Fairprice). The original waiver expired on **May 15, 2025**, due to a lack of user access management by the respective business owner. The requestor must either provide evidence of remediation or submit a new RAW form immediately.

**Pending Actions & Ownership**
*   **Action:** Determine if residual risks have been remediated.
    *   *If Yes:* Provide evidence to `cyberRisk@ntucenterprise.sg` for closure review.
    *   *If No:* Initiate a new RAW request via Gsuite immediately. This action is owned by the **Requestor**.
*   **Action:** If submitting a new form, complete Section A of the template and share it with `cyberRisk@ntucenterprise.sg` for pre-submission review and with `techgrc@ntucenterprise.sg`. Ownership: **Requestor**.
*   **Action:** Obtain sign-offs on Google Docs (full names or initials) accompanied by specific comments stating "Approved" or "Signed". Ownership: **Approvers**.
*   **Ownership Note:** The automation system will continue sending reminders until the new RAW is approved.

**Decisions Made**
No decisions were made in this thread; it serves as a notification of non-compliance and an instruction to act. The process requires all interactions and approvals to occur strictly within Google Docs (via Gsuite), not via email downloads.

**Key Dates & Deadlines**
*   **Current Date:** March 29, 2026.
*   **Original Expiry Date:** May 15, 2025.
*   **Status:** Overdue (expired ~1 year ago).
*   **Follow-up:** Continuous reminders will be sent until a new form is approved. Immediate action is required to stop the cycle.

**Specific References**
*   **RAW ID:** RAW-20240306_01-v1.0
*   **Email Address (Sender):** `cyberrisk.automation@fairpricegroup.sg`
*   **Email Address (Remediation/Review):** `cyberRisk@ntucenterprise.sg`
*   **Email Address (Governance):** `techgrc@ntucenterprise.sg`


## [11/58] You have no events scheduled today.
Source: gmail | Thread: 19d36528a7ca0ffc | Labels: Inbox, Updates | Priority: None | Senders: Google Calendar | Last Date: Sat, Mar 28, 2026, 9:21 PM | Last Updated: 2026-03-28T22:02:06.885346+00:00
**Daily Work Briefing Summary**

**Key Participants & Roles**
*   **Michael Bui** (Recipient/Account Holder): `michael.bui@fairpricegroup.sg`. Subscribed to daily agenda notifications for the "Digital Business Tech Release/Changes" calendar.
*   **Google Calendar System**: Automated notification sender (`calendar-notification@google.com`).

**Main Topic/Request**
*   Automated system confirmation of the user's schedule status for Sunday, March 29, 2026. The email confirms that no events are currently scheduled on the specific calendars to which the user is subscribed.

**Pending Actions & Ownership**
*   **None.** No manual actions are required based on this notification.
*   *Optional (User Discretion)*: To modify calendar subscription settings, Michael Bui must log in to `https://calendar.google.com/calendar/` and adjust notification preferences for specific calendars.

**Decisions Made**
*   None. This is a system-generated status update.

**Key Dates & Deadlines**
*   **Date of Notification**: March 28, 2026, at 9:21 PM.
*   **Reference Date (Schedule Check)**: Sunday, March 29, 2026.
*   **Status**: No events scheduled for the reference date on the "Digital Business Tech Release/Changes" calendar.

**Additional Notes**
*   The email footer indicates confidentiality and privilege status.
*   Resource status confirms zero scheduled events for today (Mar 29, 2026).


## [12/58] [JIRA] (DPD-838) Transition to Impression-Based Inventory & Multi-Banner Delivery
Source: gmail | Thread: 19d2e82fa82f66fe | Labels: Inbox, Updates | Priority: None | Senders: Nikhil | Last Date: Sat, Mar 28, 2026, 2:47 PM | Last Updated: 2026-03-28T22:02:52.274590+00:00
**Daily Work Briefing: JIRA (DPD-838)**

**Project Context**
*   **JIRA ID:** DPD-838
*   **Topic:** Transition to Impression-Based Inventory & Multi-Banner Delivery
*   **Category:** Ecom/Omni
*   **Updated By:** Michael Bui (via Jira automated system) / Nikhil Grover

**Key Participants**
*   **Nikhil Grover:** Product Manager/Ad Ops Lead; Defined initial acceptance criteria.
*   **Michael Bui:** Technical Stakeholder; Raised critical clarifications regarding scope, logic, and edge cases.

**Main Topic & Request**
The initiative involves migrating ad architecture from fixed-slot tenancy to an impression-based model with multi-banner support. A new comment by Michael Bui (Mar 28, 2026) challenges the initial assumption that all six page types must migrate simultaneously, highlighting that Category and Search pages currently use the legacy RMN/MPS service which does not support video UIs.

**Critical Clarifications & Questions Raised**
1.  **Scope of Migration:** Is it mandatory to change logic for Category and Search pages? The current assumption is that only Omni Home, OG Home, and FPPay need updates due to video support; other pages may remain on MPS. This impacts Front-End (FE) component changes.
2.  **Non-Endemic Identification Logic:** The method to identify non-endemic banners/videos via the "Campaign type" field is undefined. Clarification is needed: Is this an exact match or substring match?
3.  **OSMOS Capacity Limits:** OSMOS currently supports a `pcnt` (priority/sequence count?) limit of 10. The team needs to know when support for >10 will be available and what the fallback strategy is if the system remains capped at 10 while expecting 20 slots.
4.  **Position Tracking & Slot Values:** Clarification is required on how "position" values are maintained for tracking, specifically regarding OSMOS-provided slot sequences (e.g., `[-1, 0, 1, 2, 2, 5, 999]`). It is unclear if OSMOS manages these or if the client must map them.
5.  **Video Behavior:** Logic for auto-play and auto-next is undefined for scenarios involving multiple videos.
6.  **Failure Handling:** Expectations are needed for cases where OSMOS returns no banners or the API becomes inaccessible.

**Decisions Made**
*   No final decisions were made in this update; instead, specific technical ambiguities have been identified that block further development estimation and scope confirmation.

**Pending Actions & Ownership**
*   **Action:** Clarify if Category and Search pages are in scope for the new banner component (video support) or remain on MPS.
    *   **Owner:** Nikhil Grover (Immediate).
*   **Action:** Define the exact matching logic for "Campaign type" to distinguish endemic vs. non-endemic content.
    *   **Owner:** Product/Architecture Team.
*   **Action:** Confirm OSMOS `pcnt` support timeline and define the strategy for handling requests exceeding the current 10-item limit.
    *   **Owner:** Nikhil Grover / Engineering Lead.
*   **Action:** Define tracking logic for position values (e.g., `[-1, 0, ...]`) and clarify who manages slot assignment.
    *   **Owner:** Development Team.
*   **Action:** Specify fallback behavior for empty responses or API unavailability.
    *   **Owner:** Product/Engineering.

**Key Dates & Follow-ups**
*   **Last Update Timestamp:** March 28, 2026, at 10:44 PM Singapore Time (Michael Bui comment).
*   **Follow-up:** Immediate response required from Nikhil Grover regarding scope expansion and technical constraints before development can proceed.

**Summary for Executive Review**
Michael Bui has flagged significant scope and technical ambiguities in DPD-838, challenging the initial plan to update all six page types (Category, Search, etc.). He questions if legacy MPS pages require migration given their lack of video UI support. Furthermore, critical logic gaps exist regarding how non-endemic content is identified (exact vs. substring match), how OSMOS handles limits exceeding its current `pcnt` cap of 10, and how specific slot position values are tracked. The update also highlights undefined behaviors for auto-play/auto-next scenarios and API failure states. These questions must be resolved before the development team can finalize estimates or begin implementation of the unified batch request logic.


## [13/58] Re: [Bitbucket] Pull request #7: DPD-383: Suppress duplicate BCRS deposit posting via order metadata (ntuclink/bcrs-deposit-posting)
Source: gmail | Thread: 19d3315c2ea65f6f | Labels: Inbox, Updates | Priority: None | Senders: Lester | Last Date: Sat, Mar 28, 2026, 8:50 AM | Last Updated: 2026-03-28T10:01:20.857461+00:00
**Daily Work Briefing: Bitbucket Pull Request #7 (DPD-383)**

**Key Participants & Roles**
*   **Lester Santiago Soriano:** Developer/Contributor. Modified code in `internal/model/order.go` and initiated the discussion regarding data type precision.
*   **Zaw Myo Htet:** Reviewer. Provided feedback on dependency management, variable length concerns, and service constructor arguments across multiple files.
*   **Bitbucket System:** Automated notification service generating logs for pull request updates.

**Main Topic/Request**
The thread concerns Pull Request #7 for the repository `ntuclink/bcrs-deposit-posting`, tracking ticket **DPD-383**: "Suppress duplicate BCRS deposit posting via order metadata." The technical focus involves refactoring the `Customer` struct in `internal/model/order.go`, updating service constructors, and implementing logic to suppress duplicate deposits.

**Pending Actions & Ownership**
*   **Action 1:** Resolve the redundant argument in `main.go` Line 198 where `orderV3Repo` is passed twice as an argument to `service.NewDepositService`. Zaw Myo Htet questioned if this is a mistake.
    *   **Owner:** Developer (Lester Santiago Soriano) / Reviewer (Zaw Myo Htet).
*   **Action 2:** Address code style concerns regarding the length of the `UpdateDeliveryOrderRequest` structure in `internal/repo/order_v3.go`. Zaw Myo Htet noted that the reference number formatting and action list appear "very long."
    *   **Owner:** Developer (Lester Santiago Soriano).
*   **Action 3:** Refactor `internal/service/deposit_service.go` to optimize dependency injection. Suggestions include reducing constructor arguments (limiting to 3–4), making the logger a singleton, and moving static strings like `sapUsername` to local variables or configuration structures.
    *   **Owner:** Developer (Lester Santiago Soriano).

**Decisions Made**
*   No final decisions were recorded in this thread segment. The discussion is currently open regarding:
    1.  Data type precision for the `ReferenceNumber` field (`int64` vs. `decimal.Decimal`).
    2.  Structural integrity of the service constructor (redundant repository injection).
    3.  Code maintainability and line length in the update request logic.

**Key Dates & Follow-ups**
*   **Date:** March 28, 2026
*   **Time:**
    *   6:15 AM: Lester Santiago Soriano commented on `internal/model/order.go` regarding data types.
    *   8:09 AM: Zaw Myo Htet flagged the duplicate `orderV3Repo` argument in `main.go`.
    *   8:43 AM: Zaw Myo Htet raised a style concern regarding line length in `internal/repo/order_v3.go`.
    *   8:50 AM: Zaw Myo Htet suggested architectural improvements for `internal/service/deposit_service.go` dependency injection.
*   **Next Step:** The developer must clarify the duplicate repository argument, refactor service dependencies per suggestions, and potentially simplify the order update request structure before the PR can be merged.


## [14/58] [GCP] New Service Account Key Created - dfbeaa78dbcc29b8fe1bc5027e84d27ceab3f778
Source: gmail | Thread: 19d3380ff846e647 | Labels: Inbox, Forums | Priority: None | Senders: noreply-sre | Last Date: Sat, Mar 28, 2026, 8:13 AM | Last Updated: 2026-03-28T10:01:37.502653+00:00
### Daily Work Briefing: GCP Service Account Key Generation

**1. Key Participants & Roles**
*   **Sender:** `noreply-sre@ntucenterprise.sg` (Automated System Notification / SRE Team)
    *   *Role:* Initiator of the security generation event; provides system alerts regarding cloud infrastructure credentials.
*   **Recipient (Implied):** The owner or administrator of the service account `fp-marketing-tech-production/martech-internal-ai-chatbot@fp-marketing-tech-production.iam.gserviceaccount.com`.

**2. Main Topic/Request**
*   Notification that a new GCP Service Account key has been successfully generated for the production environment.
*   The specific key ID is `dfbeaa78dbcc29b8fe1bc5027e84d27ceab3f778`.
*   The system requires the recipient to download and secure this new credential immediately.

**3. Pending Actions & Ownership**
*   **Action:** Download the newly generated service account key via the provided link in the original notification email.
    *   **Owner:** The service account administrator (recipient of `noreply-sre@ntucenterprise.sg`).
*   **Action:** Securely store the key and rotate the previous active key if applicable to maintain security hygiene.
    *   **Owner:** Security/DevOps team managing the `fp-marketing-tech-production` project.

**4. Decisions Made**
*   **Decision:** A new service account key was generated on March 28, 2026.
*   **Scope:** The generation applies specifically to the 'martech-internal-ai-chatbot' service within the `fp-marketing-tech-production` project.

**5. Key Dates, Deadlines & Follow-ups**
*   **Generation Date:** March 28, 2026, at 8:13 AM.
*   **Expiration Deadline:** June 26, 2026 (90 days from generation).
*   **Follow-up Required:** Immediate download of the key upon receipt; verification that the new key is integrated into any dependent services before the old key expires or is decommissioned.

**Reference Data**
*   **Service Account Email:** `fp-marketing-tech-production/martech-internal-ai-chatbot@fp-marketing-tech-production.iam.gserviceaccount.com`
*   **Key ID:** `dfbeaa78dbcc29b8fe1bc5027e84d27ceab3f778`
*   **Message Context:** Inbox / Forums (Metadata: Priority null, Last Message ID: 19d3380ff846e647)


## [15/58] Opsgenie Alert: [Datadog] [P4] [Triggered] Service marketing-service has an abnormal change in throughput on env:prod
Source: gmail | Thread: 19d327223226bbf4 | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Sat, Mar 28, 2026, 3:22 AM | Last Updated: 2026-03-28T03:57:16.143199+00:00
**Daily Work Briefing: Opsgenie Alert Summary**

**Key Participants & Roles**
*   **System/Source:** Opsgenie (Automation), Datadog (Monitoring Integration).
*   **Notification Targets:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`.
*   **Assigned Team:** DPD Staff Excellence - Retail Media.

**Main Topic/Request**
An automated P4 alert triggered regarding abnormal throughput variations in the production environment (`env:prod`) for the service `marketing-service`. Datadog anomaly detection identified that 100% of HTTP request hit values deviated by more than 3 standard deviations from predicted values over a 15-minute window.

**Pending Actions & Ownership**
*   **Immediate Investigation:** The DPD Staff Excellence - Retail Media team is required to investigate the root cause of the throughput anomaly immediately upon alert receipt.
*   **Required Checks:** Responder must verify the following resources:
    1.  **Datadog APM:** [View HTTP Request Resources](https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod)
    2.  **Kubernetes Deployment:** [View Cluster Overview (asia-southeast1)](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview?cloudshell=false&project=fponprd)
    3.  **Runbook:** [Access `marketing-service` Runbook](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book)

**Decisions Made**
No human decisions were recorded in this thread. The alert was generated automatically by the Datadog integration (`dpd-grocery-retail-media-eu`) based on pre-configured monitor ID `17447110`.

**Key Dates, Deadlines & Follow-ups**
*   **Alert Trigger Time:** March 28, 2026, at 03:16:10 UTC (Last Updated).
*   **Opsgenie Notification Times:**
    *   First notification sent: March 28, 2026, 03:17 AM.
    *   Duplicate/Re-triggered notification sent: March 28, 2026, 03:22 AM.
*   **Metric Window:** Anomaly detected over the last 15 minutes prior to alert generation (approx. 03:01 – 03:16 UTC).
*   **Follow-up Required:** None scheduled; status depends on investigation completion by the assigned team.

**Reference Data**
*   **Monitor ID:** 17447110
*   **Event URL:** https://app.datadoghq.eu/monitors/17447110
*   **Alert Snapshot:** [Direct Snapshot Link](https://app.datadoghq.eu/monitors/17447110?from_ts=1774666870000&to_ts=1774668070000&event_id=8563174360182172995&link_source=monitor_notif&link_monitor_id=17447110&link_event_id=8563174360182172995)
*   **Alert ID:** 440c94cd-4a5e-47a2-8b84-ff9f7c88fbfa-1774667833113


## [16/58] [Search&Relevancy] [GCP] New Service Account Key Created - b5a766243501e9d9981779fc00ebdd0a445dd449
Source: gmail | Thread: 19d326d010f3ca64 | Labels: Inbox, Forums | Priority: None | Senders: noreply-sre via Gro. | Last Date: Sat, Mar 28, 2026, 3:11 AM | Last Updated: 2026-03-28T03:57:32.392350+00:00
**Daily Work Briefing: Service Account Key Generation Alert**

**1. Key Participants & Roles**
*   **Sender:** `noreply-sre via Grocery Tribe - Search & Relevancy` (Email: `db-tech-online-grocery-search@fairprice.com.sg`). This is an automated notification from the Site Reliability Engineering (SRE) team regarding the "Grocery Tribe" infrastructure.
*   **Recipient/Owner:** The email serves as a notification to stakeholders of the project `fpon-224503`. No specific individual name is listed in the send log, but the associated service account implies ownership by the `fp-search-indexer` team.

**2. Main Topic/Request**
*   **Event:** A new Google Cloud Platform (GCP) Service Account Key has been automatically generated for the project `fpon-224503`.
*   **Specific Resource:** The key ID is `b5a766243501e9d9981779fc00ebdd0a445dd449`.
*   **Associated Service Account:** `fpon-224503/fp-search-indexer@fpon-224503.iam.gserviceaccount.com`.
*   **Action Required:** Recipients must download the new key immediately via the provided link to ensure continuity for the search indexer service.

**3. Pending Actions & Ownership**
*   **Action:** Download and secure the new service account key using the link included in the original email (noted as "Click the link here" in the source).
*   **Owner:** The `fp-search-indexer` team or designated SREs for project `fpon-224503`.
*   **Status:** Critical. The key is active but must be retrieved to prevent service interruption upon rotation of older credentials.

**4. Decisions Made**
*   No explicit human decision recorded; this is an automated system event triggered by the generation of a new credential within the GCP environment. The system has determined that the key `b5a766243501e9d9981779fc00ebdd0a445dd449` is valid for immediate use.

**5. Key Dates & Deadlines**
*   **Generation Date:** March 28, 2026, at 3:11 AM.
*   **Expiration Date:** June 26, 2026 (90-day lifecycle).
*   **Follow-up Required:** Immediate download and configuration of the key before the current active credentials are retired or expire.

**Summary Note:** This notification is labeled with "Inbox" and "Forums" metadata. If your team does not manage the `fp-search-indexer` service for project `fpon-224503`, this email may be ignored. Otherwise, immediate action is required to download the key before it becomes obsolete or if previous keys are revoked.


## [17/58] [Search&Relevancy] [Action Required] Service Account Key Expiring, Renewal Required - 15088472b46aa51560af2eacac7196ccdf96d4f8
Source: gmail | Thread: 19d326ce2a188b9b | Labels: Inbox, Forums | Priority: None | Senders: noreply-sre via Gro. | Last Date: Sat, Mar 28, 2026, 3:11 AM | Last Updated: 2026-03-28T03:57:45.302490+00:00
**Daily Work Briefing: Service Account Key Renewal Alert**

**1. Key Participants & Roles**
*   **Sender:** `noreply-sre` (automated notification from SRE team) on behalf of Grocery Tribe - Search & Relevancy (`db-tech-online-grocery-search@fairprice.com.sg`).
*   **Recipient:** The owner of the expiring service account key.
*   **Service Account:** `fpon-224503/fp-search-indexer@fpon-224503.iam.gserviceaccount.com`.

**2. Main Topic/Request**
Automated notification that a specific Service Account Key is scheduled to expire and must be rotated immediately to prevent authentication disruptions. The system has already triggered the generation of a new key, which will be sent via a follow-up email.

**3. Pending Actions & Ownership**
*   **Action:** Download the newly generated service account key from the incoming email and replace the existing key in the target system (`fp-search-indexer`).
*   **Ownership:** The current owner of the service account (recipient of this alert).
*   **Conditional Action:** If the key is confirmed to be stale/unused, a SRE request must be raised by the recipient to permanently remove the key.

**4. Decisions Made**
No decisions were made in this thread; this is an initial system-generated alert requiring immediate attention from the recipient.

**5. Key Dates & Deadlines**
*   **Alert Date:** March 28, 2026, at 3:11 AM.
*   **Expiration Deadline (Critical):** April 26, 2026. After this date, key ID `15088472b46aa51560af2eacac7196ccdf96d4f8` will be invalid.
*   **Follow-up:** An email containing the new service account key is expected shortly after the alert date (March 28, 2026).

**Summary of Required Steps:**
1.  Await the follow-up email with the new key instructions.
2.  Download the new key immediately upon receipt.
3.  Update the target system before April 26, 2026.
4.  If the key is obsolete, submit a SRE request to remove it.


## [18/58] [Dashboard Report] Retail Media - DD Dashboard | Sat 28 Mar 11:00AM +08
Source: gmail | Thread: 19d32651dd4ac55d | Labels: Inbox, Updates | Priority: None | Senders: Datadog HQ | Last Date: Sat, Mar 28, 2026, 3:03 AM | Last Updated: 2026-03-28T03:57:56.012386+00:00
**Daily Work Briefing: Retail Media Dashboard Report**

**Key Participants & Roles:**
*   **Michael (Recipient):** End-user/Owner of the dashboard monitoring.
*   **Team Datadog / Datadog HQ (Sender):** Automated reporting service providing data analysis and notifications.

**Main Topic/Request:**
Distribution of the latest "Retail Media - DD Dashboard" report containing aggregated performance metrics from the past three days. The sender explicitly requests Michael to review the attached file for ongoing monitoring purposes.

**Pending Actions & Ownership:**
*   **Action:** Review the attached dashboard report and analyze the last 3 days of data.
*   **Owner:** Michael.
*   **Status:** Awaiting execution; no further action is required from the sender unless anomalies are found in the report.

**Decisions Made:**
*   No strategic or operational decisions were made in this thread. The interaction is purely informational regarding data delivery.

**Key Dates & Deadlines:**
*   **Report Generation Date:** Saturday, March 28, 2026 (3:03 AM UTC+0).
*   **Data Scope:** Data covering the three days immediately preceding the report generation date (March 25–27, 2026).
*   **Next Follow-up:** No specific follow-up deadline was scheduled; monitoring is continuous based on the "Happy monitoring" instruction.

**Specific References:**
*   **Subject Line:** Retail Media - DD Dashboard | Sat 28 Mar 11:00AM +08 (Note: Timezone discrepancy between email body 3:03 AM and subject line 11:00 AM exists; content references March 28).
*   **Contact Email:** no-reply@dtdg.eu.
*   **Sender ID:** Datadog HQ.
*   **Metadata Reference:** Last Message ID `19d32651dd4ac55d`.


## [19/58] Daily digest: updates from Tan Nhu Duong
Source: gmail | Thread: 19d3190616ddf3a5 | Labels: Inbox, Updates | Priority: None | Senders: Confluence | Last Date: Fri, Mar 27, 2026, 11:10 PM | Last Updated: 2026-03-28T02:01:42.750778+00:00
**Daily Work Briefing: Content Update Digest**

**1. Key Participants & Roles**
*   **Tan Nhu Duong:** Primary contributor; responsible for updates to the "Handover Identity scope" page.
*   **Confluence System (confluence@ntuclink.atlassian.net):** Automated notification sender providing daily digest summaries.

**2. Main Topic/Request**
*   The email is an automated system notification summarizing content changes on the NTU Confluence platform for March 27, 2026.
*   **Specific Focus:** Updates made to a page titled **"Handover Identity scope."**

**3. Pending Actions & Ownership**
*   **Review Changes:** No immediate action is mandated by the system email itself; however, stakeholders are prompted to "View changes" to understand Tan Nhu Duong's contributions.
*   **Ownership:** The review of these specific updates falls to relevant team members monitoring the "Handover Identity scope" documentation.

**4. Decisions Made**
*   No strategic decisions or new commitments were recorded in this notification thread. It serves solely as a status update log.

**5. Key Dates & Deadlines**
*   **Digest Date:** March 27, 2026.
*   **Update Time:** Notification sent at 11:10 PM (chronological timestamp).
*   **Next Steps:** No specific deadlines are listed; users must proactively access the Confluence link to view the changes.

**6. Specific References & Metadata**
*   **Last Message ID:** 19d3190616ddf3a5
*   **Labels:** Inbox, Updates
*   **Platform:** Atlassian Confluence (ntuclink.atlassian.net)
*   **Page Title:** Handover Identity scope

**Summary:** Tan Nhu Duong updated the "Handover Identity scope" page. This digest serves as a record of that activity for March 27, 2026. Stakeholders should access Confluence to review specific edit details if required for their workflow.


## [20/58] You have no events scheduled today.
Source: gmail | Thread: 19d314eea87a1d60 | Labels: Inbox, Updates | Priority: None | Senders: Google Calendar | Last Date: Fri, Mar 27, 2026, 9:59 PM | Last Updated: 2026-03-27T22:01:30.160610+00:00
**Daily Work Briefing Summary**

*   **Key Participants & Roles:**
    *   **Michael Bui** (`michael.bui@fairpricegroup.sg`): Recipient of the daily agenda notification and account holder for the subscribed calendars.
    *   **Google Calendar System**: Automated sender providing status updates on scheduled events.

*   **Main Topic/Request:**
    *   Automated confirmation regarding the user's calendar availability for the current day (Saturday, March 28, 2026). The email serves as a notification that no meetings or events are currently booked for Michael Bui.

*   **Pending Actions & Ownership:**
    *   **No pending actions** identified.
    *   No manual follow-up is required based on this message; it is an informational status update only.

*   **Decisions Made:**
    *   None. This entry contains system-generated data rather than human decision-making or meeting outcomes.

*   **Key Dates, Deadlines & Follow-ups:**
    *   **Notification Date/Time:** March 27, 2026, at 9:59 PM.
    *   **Relevant Date:** Saturday, March 28, 2026 (The date for which the "no events" status applies).
    *   **Follow-up:** None required.

*   **Technical & Reference Details:**
    *   **Account Email:** `michael.bui@fairpricegroup.sg`
    *   **Subscribed Calendars:** Digital Business Tech Release/Changes.
    *   **Management Link:** https://calendar.google.com/calendar/ (for modifying notification settings).
    *   **System Message ID:** 19d314eea87a1d60.


## [21/58] Opsgenie Alert: [Datadog] [P2] [Warn] Service marketing-service has a high error rate on env:prod
Source: gmail | Thread: 19d2e6031921b6cd | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Fri, Mar 27, 2026, 8:16 PM | Last Updated: 2026-03-27T22:01:57.314023+00:00
**Daily Work Briefing: Marketing Service Error Rate Alert (P2)**

**Key Participants & Roles**
*   **System Source:** Opsgenie / Datadog (Automated alerting system).
*   **Notification Target Teams:** `@hangouts-dd-dpd-grocery-alert` and `@opsgenie-dpd-grocery-retail-media`.
*   **Assigned Responder Group:** DPD Staff Excellence - Retail Media.

**Main Topic/Request**
An automated P2 (Warning) alert was triggered for the `marketing-service` in the production environment (`env:prod`). Datadog monitoring detected a high error rate where the ratio of HTTP request errors to total hits exceeded 5% over a 10-minute window. Multiple notifications were generated by Opsgenie between March 27, 2026, at 8:11 PM and 8:16 PM (UTC).

**Pending Actions & Ownership**
*   **Action:** Investigate the root cause of the elevated error rate and review service health immediately.
*   **Ownership:** DPD Staff Excellence - Retail Media (assigned responders).
*   **Required Resources for Investigation:**
    1.  **Datadog APM:** [Marketing Service HTTP Request Operations](https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod)
    2.  **Kubernetes Console:** [GCP K8s Overview (asia-southeast1)](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview?cloudshell=false&project=fponprd)
    3.  **Runbook:** [Marketing Service Runbook](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book)

**Decisions Made**
*   No human decisions or resolutions were recorded in this thread. The content consists solely of repeated automated system notifications (timestamps: 4:11 AM, 4:13 AM, and 4:16 AM on March 28, 2026).

**Key Dates, Deadlines, & Follow-ups**
*   **Alert Created:** March 27, 2026, at 4:19:08 PM (UTC) [Original]; Latest notification created March 28, 2026, at 4:11:08 AM.
*   **Last Metric Update:** March 27, 2026, at 20:10:06 UTC (8:10 PM).
*   **Current Metric Status:** The metric value is **0.028 (2.8%)**. While this remains below the 5% (0.05) threshold for failure states, it indicates a significant error rate warranting investigation as a P2 warning. This contradicts earlier captured data suggesting a 1% metric value; the current status reflects the active alert window.
*   **Notification History:** Alerts were pushed to Opsgenie repeatedly at 8:11 PM, 8:13 PM, and 8:16 PM on March 27, 2026.

**Metadata Summary**
*   **Monitor ID:** 17447106
*   **Trigger Query:** `sum(last_10m):( sum:trace.http.request.errors{env:prod,service:marketing-service}.as_count()/sum:trace.http.request.hits{env:prod,service:marketing-service}.as_count() ) > 0.05`
*   **Event URL:** https://app.datadoghq.eu/monitors/17447106
*   **Snapshot Link:** [View Metric Graph](https://app.datadoghq.eu/monitors/17447106?from_ts=1774641306000&to_ts=1774642506000&event_id=8562745452290480721&link_source=monitor_notif&link_monitor_id=17447106&link_event_id=8562745452290480721)
*   **Tags:** `env:prod`, `service:marketing-service`, `managed_by:datadog-sync`, `monitor`, `priority:p2`.
*   **Integration Source:** dpd-grocery-retail-media-eu (Datadog).


## [22/58] [JIRA] (DPD-715) Dynamic ad slot configuration for Homepage swimlanes
Source: gmail | Thread: 19cd82204175d296 | Labels: Inbox, Updates | Priority: None | Senders: Nikhil | Last Date: Fri, Mar 27, 2026, 7:49 PM | Last Updated: 2026-03-27T22:02:21.472268+00:00
**Daily Work Briefing: DPD-715 Dynamic Ad Slot Configuration (Production Deployed with Post-Deploy Issue)**

**Key Participants & Roles**
*   **Nikhil Grover:** Product Manager.
*   **Michael Bui:** Development Lead/Manager; executed deployment, verified initial configuration, and identified post-deployment race condition.

**Main Topic/Request**
Development of a dynamic ad slot configuration system (Ticket: **DPD-715**) for Omni and OG Homepage swimlanes, enabling Product Managers to control ad placement indices via Split feature flags without code deployments.

**Decisions Made & Status Updates**
*   **Status Change:** The ticket transitioned from "IN RELEASE QUEUE" to **"Done"** on March 25, 2026, following initial production deployment. However, a critical regression was identified post-launch.
*   **Production Deployment:** Michael Bui deployed the feature to Production (PRD) on March 25, 2026 (12:02 AM Singapore Time). Initial verification confirmed slot positions updated correctly based on SplitIO flag values `[3, 5, 7, 11, 13, 15]`.
*   **Configuration Approval:** Product Manager Nikhil Grover signed off on UAT and requested the specific configuration `[3, 5, 7, 11, 13, 15]` (Commented March 25, 10:11 PM Singapore Time).
*   **Critical Defect Identified:** On March 27, 2026 (at 03:38 AM Singapore Time), Michael Bui identified a race condition in the code where a `share` variable is overwritten. This impacts concurrent or subsequent requests.
    *   **Impact:** The feature flag `pnct=1` stopped functioning correctly after deployment.
    *   **Verification:** The failure was verified on the UAT environment.
    *   **Evidence:** Michael Bui attached a screenshot (`image-20260327-193706.png`) documenting the issue.

**Pending Actions & Ownership**
*   **Immediate Action Required:** The identified race condition requires immediate investigation and a hotfix or patch release to restore `pnct=1` functionality.
*   **Ownership:** Michael Bui is responsible for diagnosing the variable overwrite logic and implementing the fix.
*   **Monitoring:** Standard post-deployment monitoring is paused regarding this specific feature until the race condition is resolved.

**Key Dates & Deadlines**
*   **Start Date:** March 10, 2026
*   **UAT Sign-off:** March 25, 2026 (10:11 PM Singapore Time).
*   **Production Deployment:** March 25, 2026 (12:02 AM Singapore Time).
*   **Post-Deploy Verification (Initial):** March 26, 2026 (12:19 AM – 12:21 AM Singapore Time).
*   **Issue Discovery:** March 27, 2026 (03:38 AM Singapore Time).

**Reference Data**
*   **Ticket ID:** DPD-715
*   **Project:** (Ecom/Omni) DPD
*   **Last Message ID:** 19d30d7ccd9ed15b
*   **Attachments:**
    *   `image-20260325-160055.png` (Visual confirmation of slot changes).
    *   `ScreenRecording_03-26-2026 00-15-50_1.MP4` (Initial post-deployment validation).
    *   **New:** `image-20260327-193706.png` (Evidence of race condition affecting `pnct=1`).

**Historical Context Retained**
*   Boundary handling logic remains valid: Configured indices exceeding available content range are ignored; only valid bounds render.
*   Stock integrity checks remain active: Out-of-stock items cannot be served as ads regardless of slot configuration.
*   Previous mobile app issues were resolved in the earlier UAT cycle and verified during initial deployment, though the current race condition represents a new code-level defect unrelated to previous mobile fixes.


## [23/58] [Bitbucket]  Pipeline for DPD-383 failed on 10d28d9 (ntuclink/bcrs-deposit-posting)
Source: gmail | Thread: 19d30bec61b50cb9 | Labels: Inbox, Updates | Priority: None | Senders: Bitbucket | Last Date: Fri, Mar 27, 2026, 7:21 PM | Last Updated: 2026-03-27T22:02:33.759207+00:00
**Daily Work Briefing: Bitbucket Pipeline Failure (DPD-383)**

**1. Key Participants & Roles**
*   **Michael Bui**: Commit author for the failing change related to DPD-383.
*   **Bitbucket System**: Automated notification source triggering alerts on pipeline failures.
*   **Team/Engineering**: Implicit recipients of the failure alert (via "Inbox" and "Updates" labels).

**2. Main Topic & Request**
The thread reports an automated CI/CD pipeline failure for the repository `ntuclink/bcrs-deposit-posting` triggered by commit `10d28d9`. The failing change, titled **"DPD-383: Suppress duplicate BCRS deposit posting via order metadata,"** resulted in a build error.

**3. Pending Actions & Ownership**
*   **Action**: Investigate the root cause of the pipeline failure and resolve the build issue to restore CI stability.
*   **Ownership**: Michael Bui (as the committer) or the assigned engineering team responsible for the `bcrs-deposit-posting` repository.
*   **Next Step**: Access the "View this pipeline" link in the notification to analyze error logs and implement a fix.

**4. Decisions Made**
No strategic decisions were made during this thread; it is a system-generated status update indicating a regression in the deployment pipeline.

**5. Key Dates, Deadlines, & Follow-ups**
*   **Date of Incident**: March 27, 2026.
*   **Time of Failure**: 7:21 PM (Notification timestamp).
*   **Pipeline Duration**: 3 minutes, 10 seconds.
*   **Commit Hash**: `10d28d9`.
*   **Ticket Reference**: DPD-383.
*   **Repository**: `ntuclink/bcrs-deposit-posting`.

**6. Specific References & Metadata**
*   **Source**: Bitbucket Notifications (`notifications-noreply@bitbucket.org`).
*   **Email Labels**: "Inbox", "Updates".
*   **Last Message ID**: `19d30bec61b50cb9`.
*   **Priority Status**: Currently null (requires manual triage based on severity).


## [24/58] [JIRA] (DPD-842) Suppress duplicate BCRS deposit posting via order metadata
Source: gmail | Thread: 19d30b2835e5120b | Labels: Inbox, Updates | Priority: None | Senders: Michael Bui (Jira) | Last Date: Fri, Mar 27, 2026, 7:08 PM | Last Updated: 2026-03-27T22:02:49.495866+00:00
**Daily Work Briefing: DPD-842 Update**

**Key Participants & Roles**
*   **Michael Bui:** Reporter; created the work item, performed updates, and provided technical clarification on delivery behaviors.

**Main Topic/Request**
*   **Item:** [DPD-842] Suppress duplicate BCRS deposit posting via order metadata.
*   **Context:** Part of the Ecom/Omni initiative (Parent: DPD-383). The objective is to ensure that re-delivering an order does not trigger a duplicate Bank Card Receipt System (BCRS) deposit posting to SAP.

**Decisions & Technical Clarifications**
*   Michael Bui confirmed via comment and attachment that the system logic prevents duplicate postings upon re-delivery of an order.
*   Evidence provided includes screenshots captured after a BCRS post, demonstrating the correct behavior where no second entry is generated in SAP for the same order transaction.

**Status & Progression**
*   **Initial Status:** TO BE DEFINED (Created on Mar 27, 2026).
*   **Progression Path:** Rapidly moved through statuses: READY FOR DEVELOPMENT $\rightarrow$ IN DEVELOPMENT $\rightarrow$ Testing in Preproduction.
*   **Current State:** The work item is currently in the "Testing in Preproduction" phase as of 03:02 AM Singapore Time on Mar 28, 2026 (UTC+8).
*   **Priority:** High.
*   **Work Type:** Subtask.

**Pending Actions & Ownership**
*   **Action:** Complete and validate testing in the Preproduction environment.
*   **Owner:** Development/QA Team (implied by Michael Bui's updates moving status to "Testing"). No specific new owner was assigned in this thread, but the reporter is driving the status changes.

**Key Dates & References**
*   **Work Item Created:** Mar 27, 2026, 02:57 AM Singapore Time.
*   **Status Updated to Preproduction Testing:** Mar 28, 2026, 03:02 AM Singapore Time.
*   **Attachments:** Two images added (ID: image-20260327-185919.png; image-20260327-190158.png) illustrating the post-posting state and re-delivery logic.
*   **Jira Issue ID:** DPD-842.
*   **Parent Issue:** DPD-383.
*   **Last Message ID:** 19d30b2835e5120b.

**Summary for Review**
The issue regarding duplicate BCRS deposit postings has been successfully addressed in code and is currently undergoing preproduction validation. The reporter confirmed that re-delivery logic effectively prevents SAP duplicates, supported by attached evidence. The ticket remains under active development/testing control with no blockers identified in this thread.


## [25/58] [JIRA] Michael Bui assigned DPD-842 to you
Source: gmail | Thread: 19d30a8f49fa308a | Labels: Inbox, Updates | Priority: None | Senders: Michael Bui (Jira) | Last Date: Fri, Mar 27, 2026, 6:57 PM | Last Updated: 2026-03-27T22:03:01.237059+00:00
**Daily Work Briefing: JIRA Assignment DPD-842**

**1. Key Participants & Roles**
*   **Michael Bui:** Initiator/Assigner (Jira User). Sent the assignment notification on March 27, 2026.
*   **Recipient (You):** Current Assignee of work item DPD-842. Previously marked as "Unassigned."

**2. Main Topic/Request**
*   **Work Item:** JIRA ticket **DPD-842**.
*   **Project:** (Ecom/Omni) DPD.
*   **Task Description:** Implement logic to suppress duplicate BCRS deposit postings by utilizing order metadata.

**3. Pending Actions & Ownership**
*   **Action Required:** Review the assigned work item and execute the task to suppress duplicate BCRS deposit postings.
*   **Owner:** You (Current Assignee).
*   **Status Change:** The assignee field has been updated from "Unassigned" to your name by Michael Bui.

**4. Decisions Made**
*   **Assignment Decision:** Michael Bui formally assigned the responsibility for DPD-842 to you to address the duplicate posting issue.

**5. Key Dates & Follow-ups**
*   **Notification Date/Time:** March 27, 2026, at 6:57 PM (Local time not specified in footer, but message timestamp indicates Singapore Time: 02:57 AM on the same day relative to notification logic).
    *   *Note: The email body cites "02:57 AM Singapore Time" for Michael Bui's action, while the header shows a PM timestamp. Ensure time zone alignment when reviewing.*
*   **Next Steps:** Open the JIRA work item (DPD-842) to view attachments and details immediately.

**6. References & Metadata**
*   **Ticket ID:** DPD-842
*   **Last Message ID:** 19d30a8f49fa308a
*   **Email Labels:** Inbox, Updates
*   **Notification Source:** Jira Cloud (jira@ntuclink.atlassian.net)


## [26/58] Verifying it's you
Source: gmail | Thread: 19d301429f6276db | Labels: Inbox, Updates | Priority: None | Senders: Atlassian | Last Date: Fri, Mar 27, 2026, 4:15 PM | Last Updated: 2026-03-27T22:03:10.059456+00:00
**Daily Work Briefing Summary**

**Participants & Roles:**
*   **Sender:** Atlassian (noreply+b7101f8@id.atlassian.com) – Automated system notification.
*   **Recipient:** Michael Bui – User requiring account access verification.

**Main Topic/Request:**
Atlassian Cloud is requesting identity verification from Michael Bui to complete a login or download process. The communication serves as a security measure confirming the user's identity before granting access.

**Pending Actions & Ownership:**
*   **Action:** Verify identity using the provided code.
*   **Owner:** Michael Bui.
*   **Details:** The recipient must enter the verification code **63435857** into the Atlassian Cloud interface to proceed with the requested action (Download). No further action is required from Atlassian at this time pending user input.

**Decisions Made:**
None recorded in this thread; this is a transactional security prompt rather than a decision-making discussion.

**Key Dates & Follow-ups:**
*   **Date Sent:** March 27, 2026, at 4:15 PM.
*   **Expiration:** Not specified in the message text (standard verification codes typically expire within minutes to hours). Immediate action is recommended.
*   **Follow-up Required:** None automatically; success depends on Michael Bui entering the code promptly.

**Specific References:**
*   **Verification Code:** 63435857
*   **Message ID:** 19d301429f6276db
*   **Labels:** Inbox, Updates


## [27/58] Urgent - PLA Impressions drop by 50%
Source: gmail | Thread: 19d24c9e00402c74 | Labels: Inbox | Priority: None | Senders: Rachit, me, Nikhil | Last Date: Fri, Mar 27, 2026, 11:27 AM | Last Updated: 2026-03-27T14:01:17.936075+00:00
**Daily Work Briefing: Urgent PLA Impressions Drop – Data Delivery & Analysis Phase**

**Key Participants & Roles**
*   **Rachit Sachdeva** (rachit.sachdeva@osmos.ai): Source of data; responsible for extracting and sharing request logs.
*   **Michael Bui** (michael.bui@fairpricegroup.sg): Investigating root cause; coordinating internal teams.
*   **Nikhil Grover** (nikhil.grover@fairpricegroup.sg): Identified potential root cause; requested specific metric analysis.

**Main Topic/Request**
Investigate a 50% drop in PLA impressions over the last week. Initial data showed search page impressions falling from 1.3M to 550K and category page impressions dropping by 62% (205K to 77K). While request volumes remained stable, Nikhil Grover identified a critical hypothesis: the average number of products per response has significantly decreased. Historical data showed 4-5 products per response; current data indicates most responses now contain only a single product across categories like "Drinks > Beverage" and "Beauty & Personal Care > Oral Care." This reduction in product density is presumed to be the primary driver of the impression drop.

**Pending Actions & Ownership**
*   **Analyze average products per response:** Owned by Rachit Sachdeva. He must verify if this metric has declined over the last 7 days and correlate it with the impression drop, as Nikhil lacks data beyond that window.
*   **Verify granular/hourly data:** Pending review of the newly provided dataset for the 4th UTC hour on March 27, 2026.
*   **Cross-check internal activities:** Owned by Michael Bui (and his team). Awaiting confirmation that the new request log aligns with Nikhil's hypothesis regarding product density.

**Decisions Made**
*   Confirmed that ad requests remained stable; the drop is isolated to impressions, not traffic volume.
*   **Hypothesis Shifted:** The investigation has pivoted from a general "traffic/impression" issue to a specific "product density per response" issue. The drop in impressions is likely driven by fewer products being served per request rather than a lack of requests.

**Key Dates & Follow-ups**
*   **March 25, 2026:**
    *   **11:38 AM:** Alert raised regarding declining PLA impressions.
    *   **12:00 PM – 12:07 PM:** Michael requested hourly data and clarification on request volume.
    *   **12:56 PM:** Rachit confirmed stable request volumes and committed to compiling detailed time-frame data.
    *   **2:37 PM:** Nikhil Grover highlighted the reduction in products per response (from 4-5 down to 1) via screenshots for specific categories. He requested a historical check on this metric from Rachit.
*   **March 27, 2026:**
    *   **11:27 AM:** Rachit Sachdeva provided the request details logged in the system specifically for the **4th UTC hour of March 27**. Data is available in the "FPG Requests" sheet.

**Status Summary**
Investigation remains active with a refined hypothesis regarding product density. The immediate blocker has been partially addressed: Rachit has delivered specific request logs for the 4th UTC hour on March 27, moving the team from data collection to granular verification. Michael must now analyze this new dataset to validate if the "single product per response" anomaly persists in the latest hourly window, confirming whether the root cause is systemic or a recent fluctuation.


## [28/58] Re: [## 112603 ##] Sev1 incident: Ad Products per response is low for PLA
Source: gmail | Thread: 19d2ead5d3ae56a5 | Labels: Inbox | Priority: None | Senders: Nikhil Grover | Last Date: Fri, Mar 27, 2026, 9:43 AM | Last Updated: 2026-03-27T10:07:05.558515+00:00
**Daily Work Briefing: Sev1 Incident #112603**

**Key Participants & Roles**
*   **Nikhil Grover** (nikhil.grover@fairpricegroup.sg): Incident coordinator/escalation lead. Note: Lacks access to the specific request URL required for analysis.
*   **Michael Bui**: Technical subject matter expert. Requested by Nikhil for immediate advisory support regarding the incident scope.

**Main Topic & Request**
The thread addresses a Severity 1 (Sev1) incident [#112603] concerning low volume responses from Ad Products specifically within Programmatic Local Ads (PLA). The core issue is an inability to validate or troubleshoot the problem due to missing access credentials for the specific request URL by Nikhil Grover.

**Pending Actions & Ownership**
*   **Action:** Provide advisory guidance on the Sev1 incident and PLA response low-volume issue.
    *   **Owner:** Michael Bui.
*   **Action:** Gain access to the specific request URL or provide an alternative means of investigation for Nikhil Grover.
    *   **Owner:** Implied shared responsibility, but specifically requires resolution by the team managing URL permissions (Michael Bui is currently blocked).

**Decisions Made**
No formal decisions were recorded in this specific exchange. The thread represents an escalation step where access limitations halted further progress until expert intervention was requested.

**Key Dates & Follow-ups**
*   **Date:** March 27, 2026
*   **Time:** 9:43 AM
*   **Incident ID:** [#112603]
*   **Follow-up Status:** Immediate response required from Michael Bui to unblock the Sev1 investigation.

**Summary of Thread Chronology**
At 9:43 AM on March 27, 2026, Nikhil Grover escalated the matter by adding Michael Bui to the thread. Nikhil explicitly stated an inability to access the necessary request URL and requested Michael's advice to proceed with the Sev1 investigation regarding low PLA responses.


## [29/58] Re: CISA Adds One Known Exploited Vulnerability to Catalog
Source: gmail | Thread: 19d2ea0ef27d9afe | Labels: Inbox, Forums | Priority: None | Senders: Cyber Alert | Last Date: Fri, Mar 27, 2026, 9:29 AM | Last Updated: 2026-03-27T10:07:16.373260+00:00
**Daily Work Briefing: CISA & Security Vulnerability Alert**

**1. Key Participants & Roles**
*   **Sender:** Cyber Alert (<cyberalert@fairpricegroup.sg>) – Issued security notification and instructions.
*   **Audience:** "Hi All" (Internal workforce/IT teams).
*   **External Reference:** Aqua Security (Source of vulnerability data); CISA (Catalog context in subject line, though content focuses on Trivy).

**2. Main Topic/Request**
The sender alerts the team to a specific security incident: **"Aqua Security Trivy Embedded Malicious Code Vulnerability."** The email references "CISA Adds One Known Exploited Vulnerability to Catalog" in the subject line but directs attention specifically to the Trivy issue for immediate risk mitigation.

**3. Pending Actions & Ownership**
*   **Action:** Identify if the organization is affected by the vulnerability.
*   **Action:** Execute quick mitigation measures if the vulnerability is present.
*   **Owner:** All recipients ("Hi All") are instructed to perform these checks and actions immediately.

**4. Decisions Made**
No formal decisions were recorded in this thread. The communication functions as an advisory directive to investigate and act proactively.

**5. Key Dates & References**
*   **Date Issued:** March 27, 2026, at 9:29 AM.
*   **Vulnerability Subject:** Aqua Security Trivy Embedded Malicious Code Vulnerability.
*   **Reference Link:** "refer here" (Specific URL not provided in text; requires access to original email for resolution).
*   **Metadata:** Last message ID `19d2ea0ef27d9afe`; Priority marked as null; Filed under Inbox and Forums.

**Summary:** Immediate attention is required from all staff to determine exposure to the Aqua Security Trivy vulnerability and implement mitigation steps. The specific technical details are located in the linked reference provided by the sender.


## [30/58] A Little Better: Coming Together to Make Our Iftar Possible
Source: gmail | Thread: 19d2e873a4aa9f15 | Labels: Inbox, Updates | Priority: None | Senders: Internal Comms | Last Date: Fri, Mar 27, 2026, 9:01 AM | Last Updated: 2026-03-27T10:07:31.249449+00:00
**Daily Work Briefing: Ramadan Iftar Initiative Summary**

**Key Participants & Roles**
*   **Internal Comms / FairPrice Foundation:** Led the initiative planning and communication.
*   **Fresh Category Managers:** Collaborated with the Foundation to select produce.
*   **Products Team:** Secured new partners and managed inventory optimization following supplier shifts.
*   **Frontline Staff:** Packed and distributed refreshment sets at 60 stores (30 minutes before/after Buka Puasa).
*   **Support Functions:** Finance, Customer & Marketing, and Supply Chain teams managed back-end operations.
*   **FairPrice Group (FPG):** The collective entity executing "Winning As One."

**Main Topic/Request**
The email reports on the 18th annual Ramadan Buka Puasa initiative where FPG distributed **80,000 refreshment sets** across **60 stores**. It highlights a strategic shift from traditional dry snacks (bread, biscuits) to include **fresh Royal Gala apples**, selected for hydration and convenience. The message serves as an internal acknowledgment of cross-functional collaboration and reinforces the "Growth Mindset in Action" cultural values.

**Pending Actions & Ownership**
*   **Action:** Submit nominations for colleagues who contributed significantly ("heroes") to be featured in future communications.
*   **Owner:** All employees (Self-nomination).
*   **Method:** Submit request via the provided link in the original email.

**Decisions Made**
*   **Product Selection:** Fresh Royal Gala apples were chosen over other fruits due to their sweetness, small size, and ability to provide quick hydration and satiety.
*   **Operational Scope:** The initiative was executed islandwide across all 60 FairPrice stores without interruption despite supply chain challenges between Chinese New Year and Ramadan.

**Key Dates & Deadlines**
*   **Date of Initiative Execution:** March 27, 2026 (Email sent; distribution occurred during the Ramadan period leading up to this date).
*   **Distribution Window:** Daily operations ran 30 minutes before and after Buka Puasa throughout the Ramadan month.
*   **Submission Deadline:** No specific deadline listed for hero nominations; submission is ongoing via the link.

**Specific References & Metrics**
*   **Total Sets Distributed:** 80,000.
*   **Stores Involved:** 60 FairPrice stores (islandwide).
*   **Initiative Anniversary:** 18th year.
*   **New Item Added:** Royal Gala apples (fresh fruit).
*   **Sender Email:** internal_comms@fairpricegroup.sg


## [31/58] [JIRA] (DPD-838) Fetch personalised banners from OSMOS
Source: gmail | Thread: 19d2e7ac19e05d88 | Labels: Inbox, Updates | Priority: None | Senders: Nikhil Grover (Jira) | Last Date: Fri, Mar 27, 2026, 8:48 AM | Last Updated: 2026-03-27T10:07:55.264923+00:00
**Daily Work Briefing: JIRA DPD-838**

**Key Participants & Roles**
*   **Nikhil Grover:** Issue updater/Contributor (Ecom/Omni team). Contact via `jira@ntuclink.atlassian.net`.

**Main Topic/Request**
*   **JIRA Ticket:** [DPD-838] Fetch personalised banners from OSMOS.
*   **Component/Team:** Ecom/Omni (DPD).
*   **Objective:** Technical implementation to retrieve personalized banner assets from the OSMOS system.

**Status Update & Actions**
*   **Current Status:** The issue was updated by Nikhil Grover on March 27, 2026. The update summary reads: "Fetch banners based on Fetch personalised banners from OSMOS."
*   **Pending Actions:** No specific new action items or assignees were explicitly listed in the provided thread snippet. The next steps depend on the full Jira workflow state (e.g., whether this is a status change to "In Progress," "Done," or a requirement clarification).
*   **Ownership:** Nikhil Grover is currently active on this ticket based on the update timestamp.

**Decisions Made**
*   No formal decisions are recorded in the provided text snippet beyond the acknowledgment of the task scope (fetching banners from OSMOS).

**Key Dates & Follow-ups**
*   **Last Activity:** March 27, 2026, at 4:44 PM Singapore Time.
*   **Notification ID:** `19d2e7ac19e05d88`.
*   **Labels:** Inbox, Updates.
*   **Priority:** Not set (null).

**Attachments & Resources**
*   The update notes that attachments larger than 100 KB are available within the work item view.
*   Mobile notifications for Jira Cloud are available via Android/iOS apps.


## [32/58] [JIRA] (DPD-838) Fetch multiple banners per slot from OSMOS
Source: gmail | Thread: 19d2e7613ef55388 | Labels: Inbox, Updates | Priority: None | Senders: Nikhil Grover (Jira) | Last Date: Fri, Mar 27, 2026, 8:43 AM | Last Updated: 2026-03-27T10:08:05.937971+00:00
**Daily Work Briefing: JIRA Update DPD-838**

**Key Participants & Roles**
*   **Nikhil Grover:** Reporter; initiated the work item and provided initial updates.
*   **Michael Bui:** Assignee; responsible for execution of the story.

**Main Topic/Request**
Creation of user story **[DPD-838] Fetch multiple banners per slot from OSMOS**. This task is a sub-story under parent ticket **DPD-385**. The objective is to modify functionality to retrieve multiple banner assets per display slot directly from the OSMOS system.

**Pending Actions & Ownership**
*   **Action:** Develop and implement logic to fetch/serve multiple banners per slot.
*   **Owner:** Michael Bui.
*   **Status:** Currently marked as **"TO BE DEFINED"**. No development work appears to have commenced yet based on the status label.

**Decisions Made**
*   **Classification:** The item was classified as a **Story** with **High** priority.
*   **Parentage:** Confirmed linkage to parent ticket **DPD-385**.
*   **Scope:** Explicitly defined to handle multiple banners rather than single assets per slot.

**Key Dates & Timeline**
*   **Creation Date:** March 27, 2026 (4:32 PM Singapore Time).
*   **Last Update:** March 27, 2026 (4:37 PM Singapore Time) by Nikhil Grover to update the summary and parent link.
*   **Deadlines/Follow-ups:** None specified in this thread; status remains "TO BE DEFINED" pending further scoping or planning discussions.

**System Metadata**
*   **Labels:** Inbox, Updates.
*   **Last Message ID:** 19d2e7613ef55388.
*   **Source:** JIRA (jira@ntuclink.atlassian.net).


## [33/58] [Action Required] Service Account Key Expiring, Renewal Required - 0b001c303f2e01cefa4828ea0d37f46d8e76ae05
Source: gmail | Thread: 19d2e5a71666e00b | Labels: Inbox, Forums | Priority: None | Senders: noreply-sre | Last Date: Fri, Mar 27, 2026, 8:12 AM | Last Updated: 2026-03-27T10:08:36.702191+00:00
**Daily Work Briefing: Service Account Key Expiration**

*   **Key Participants & Roles:**
    *   **Sender:** `noreply-sre@ntucenterprise.sg` (SRE Team/NTU Centerprise) – Issued automated rotation notification and instructions.
    *   **Recipient:** The owner(s) of the service account `fp-marketing-tech-production/martech-internal-ai-chatbot@fp-marketing-tech-production.iam.gserviceaccount.com` (Referred to as "you" in email).

*   **Main Topic/Request:**
    *   Notification that the existing service account key (`0b001c303f2e01cefa4828ea0d37f46d8e76ae05`) is expiring and requires immediate rotation to prevent authentication failure.

*   **Pending Actions & Ownership:**
    *   **Action 1 (Immediate):** Await the automated email containing the new service account key. The recipient must download this new key upon receipt.
    *   **Action 2 (Critical):** Replace the existing key (`0b...ae05`) with the newly downloaded key in the target system immediately after receiving the new credentials.
    *   **Ownership:** Service Account Owner / Development Team maintaining `fp-marketing-tech-production`.

*   **Decisions Made:**
    *   No formal decisions were made in this thread; however, a conditional instruction was provided: If the key is determined to be stale and removal is required rather than renewal, a specific SRE request must be raised.

*   **Key Dates & Deadlines:**
    *   **Expiration Date:** 2026-04-26 (Service account will become invalid after this date).
    *   **Action Deadline:** Before 2026-04-26 to ensure no service disruption.
    *   **Notification Sent:** March 27, 2026, at 8:12 AM.

*   **Specific References:**
    *   Service Account ID: `fp-marketing-tech-production/martech-internal-ai-chatbot@fp-marketing-tech-production.iam.gserviceaccount.com`
    *   Key ID to expire: `0b001c303f2e01cefa4828ea0d37f46d8e76ae05`
    *   Project/Environment Context: `fp-marketing-tech-production`


## [34/58] To be modified / 驳回待修改
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


## [35/58] Opsgenie Alert: [Datadog] [P4] [Triggered] Service marketing-service has an abnormal change in throughput on env:prod
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


## [36/58] Trivy compromise & LiteLLM infected
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


## [37/58] Canceled event with note: [Virtual] Smart Cart x RMN Catchup @ Fri Mar 27, 2026 4pm - 4:30pm (SGT) (Michael Bui)
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


## [38/58] Re: [Bitbucket] Pull request #919: chore/omni ops monitor (ntuclink/dpd-datadog-monitoring)
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


## [39/58] [Dashboard Report] Retail Media - DD Dashboard | Fri 27 Mar 11:00AM +08
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


## [40/58] Safeguarding our Foundation - The new Regulatory Compliance Policy
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


## [41/58] You have no events scheduled today.
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


## [42/58] It's raining new Jira updates!
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


## [43/58] [JIRA] (DPD-383) Sales posting for BCRS deposit amount
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


## [44/58] March 2026 Google Cloud on Coursera Newsletter
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


## [45/58] DOS: Don't Wait for a Special Season - Give with Purpose Today!
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


## [46/58] Notes: “BCRS Regroup - Open Item Planning” Mar 26, 2026
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


## [47/58] [JIRA] Wai Ching Chan mentioned you on DPD-807
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


## [48/58] New event: Michael On Leave @ Sat 28 Mar - Sun 5 Apr 2026 (CPD Team Calendar)
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


## [49/58] New event: Michael On Leave @ Sat Mar 28 - Sun Apr 5, 2026 (CPD Team Calendar)
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


## [50/58] Declined: BCRS Regroup - Open Item Planning @ Thu Mar 26, 2026 4pm - 5pm (SGT) (Prajney Sribhashyam)
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


## [51/58] Updated invitation: BCRS Regroup - Open Item Planning @ Thu Mar 26, 2026 4pm - 5pm (SGT) (Michael Bui)
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


## [52/58] Opsgenie Alert: [Datadog] [P4] [Triggered] Service marketing-service has an abnormal change in throughput on env:prod
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


## [53/58] Invitation: BCRS Regroup - Open Item Planning @ Thu Mar 26, 2026 4pm - 5pm (SGT) (Michael Bui)
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


## [54/58] Re: [Not Virus Scanned] Re: FairPrice Performance Marketing Meta x Osmos
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


## [55/58] Data COE Org Announcement
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


## [56/58] [Dashboard Report] Retail Media - DD Dashboard | Thu 26 Mar 11:00AM +08
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


## [57/58] Declined: ACNxOsmos: Daily Cadence @ Thu Mar 26, 2026 1:30pm - 2pm (SGT) (michael.bui@fairpricegroup.sg)
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


## [58/58] Message from Group CEO: Leadership Team announcement
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
