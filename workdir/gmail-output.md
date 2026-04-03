

## [1/17] Issue with Missing UBID
Source: gmail | Thread: 19d52fdf13c8b0bd | Labels: Inbox | Priority: None | Senders: Rahul, Nikhil, me | Last Date: Fri, Apr 3, 2026, 12:50 PM | Last Updated: 2026-04-03T14:01:46.241463+00:00
**Daily Work Briefing: Resource Issue (Missing UBID)**

**Key Participants & Roles:**
*   **Rahul Jain** (osmos.ai): Identified the technical discrepancy and provided diagnostic logs.
*   **Nikhil Grover** (fairpricegroup.sg): Recipient of the notification; seeking clarification on ad unit scope. Added Rajesh and Soumya for support.
*   **Michael Bui** (fairpricegroup.sg): Primary point of contact responding to technical clarifications regarding UBID/uclid definitions and customer journey context.

**Main Topic/Request:**
Rahul Jain flagged a critical tracking configuration issue where the client is failing to send the `UBID` within the `uclid` parameter during event transmission. Consequently, Osmos.ai's system is generating "DUMMY_UBID" values (e.g., `BRAND_AD_TAG|DUMMY_UBID`). The immediate request is for the client to audit their events configuration to ensure proper UBID transmission.

**Pending Actions & Ownership:**
*   **Action:** Provide specific clarification on what `UBID` and `uclid` refer to in this context, confirm the associated customer journey, and define the scope of impact (platform, page type: banner vs. product ads).
    *   **Owner:** Michael Bui (fairpricegroup.sg) / Support Team (Rajesh, Soumya).
*   **Action:** Identify the specific ad unit(s) generating these events (Display only or Product Ads as well).
    *   **Owner:** Nikhil Grover (fairpricegroup.sg).

**Decisions Made:**
No final technical resolution was made in this thread. The discussion remains at the information-gathering phase to understand the scope of the tracking error before configuration changes are implemented.

**Key Dates & Follow-ups:**
*   **Issue Identified:** April 3, 2026, 10:57 AM (Email from Rahul Jain).
*   **Logs Provided:** Sample logs dated April 1, 2026 (timestamps approx. 18:20 UTC) showing `uclid` parameters containing `DUMMY_UBID`.
*   **Current Status:** Pending clarification response from FairPrice Group to Osmos.ai regarding ad unit specifics and parameter definitions. No deadline set; immediate follow-up required to prevent data integrity issues in funnel tracking.


## [2/17] Opsgenie Alert: [Datadog] [P2] [Warn] Service marketing-service has a high error rate on env:prod
Source: gmail | Thread: 19d523ef32e8f816 | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Fri, Apr 3, 2026, 12:34 PM | Last Updated: 2026-04-03T14:02:14.300632+00:00
**Daily Work Briefing: Opsgenie Alert Thread Summary**

**Key Participants & Roles**
*   **System:** Opsgenie (Alert Automation), Datadog (Monitoring Source).
*   **Responder Group:** DPD Staff Excellence - Retail Media.
*   **Notification Channels:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`.
*   **Team Context:** Managed by Datadog-sync; Environment: Production (prod).

**Main Topic/Request**
Automated alerts triggered for the `marketing-service` in the production environment due to elevated HTTP error rates. The system is requesting immediate investigation of service health, Kubernetes deployment status, and adherence to established runbooks.

*   **Alert Criteria:** Error rate > 5% over the last 10 minutes (`sum:trace.http.request.errors / sum:trace.http.request.hits > 0.05`).
*   **Status:** Alerts have been active throughout April 3, 2026. Metric values fluctuated between 0.01 (1%) and 0.021 (2.1%), remaining below the 5% trigger threshold in recent notifications but flagged as P2 warnings.

**Pending Actions & Ownership**
*   **Action:** Investigate high error rate causes for `marketing-service`.
*   **Ownership:** DPD Staff Excellence - Retail Media (Assigned Responder).
*   **Required Steps:**
    1.  Review Datadog APM metrics: [Link](https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod)
    2.  Check Kubernetes deployment status in `fpon-cluster` (asia-southeast1): [Link](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview?cloudshell=false&project=fponprd)
    3.  Consult the specific runbook: [Link](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book)

**Decisions Made**
No human decisions or resolution actions are recorded in this thread; it consists entirely of automated system notifications. The alert state remains "Open" with no manual acknowledgment or closure noted.

**Key Dates & Timeline (April 3, 2026)**
*   **07:28 UTC:** Alert first triggered (Metric value: 0.016). Duplicates sent at 07:30 and 07:33 UTC.
*   **11:24 UTC:** Alert active (Metric value: 0.021). Duplicates sent at 11:25, 11:27, and 11:30 AM.
*   **12:17 UTC:** Metric value dropped to 0.01. Duplicates sent at 12:18 PM, 12:20 PM, and 12:23 PM.
*   **12:28 UTC:** Metric value slightly rose to 0.012. Duplicates sent at 12:29 PM, 12:31 PM, and 12:34 PM.

**References & Links**
*   **Monitor Event URL:** https://app.datadoghq.eu/monitors/17447106
*   **Service:** `marketing-service`
*   **Environment:** `env:prod`
*   **Integration:** `dpd-grocery-retail-media-eu`


## [3/17] Updates to Notion’s Terms
Source: gmail | Thread: 19d50f4f7945d100 | Labels: Inbox, Updates | Priority: None | Senders: Notion Team | Last Date: Fri, Apr 3, 2026, 1:28 AM | Last Updated: 2026-04-03T14:02:25.316103+00:00
### Executive Briefing: Notion Terms Update

**Key Participants & Roles**
*   **Sender:** Notion Team (team@mail.notion.so) – Service provider.
*   **Recipient:** Michael – Customer account holder.

**Main Topic/Request**
Notification of updates to Notion's legal documentation, specifically the Master Subscription Agreement and Notion AI/Credits Supplementary Terms. The primary change involves the introduction of a credit system for "Custom Agents."

**Pending Actions & Ownership**
*   **Action Required:** None at this time.
*   **Owner:** Michael (Not required to act yet).
*   **Note:** No immediate action is needed prior to May 1, 2026.

**Decisions Made**
*   Notion has finalized updates requiring credits to run Custom Agents.
*   Credits are designated as an optional add-on for Business and Enterprise plans only.

**Key Dates & Deadlines**
*   **May 1, 2026:** Updated terms officially take effect.
*   **May 4, 2026:** Notion credits become available as an add-on; this is the date Custom Agents will require credits to operate.
*   **April 3, 2026:** Notification sent (Current status: No changes apply before May 1).

**Summary of Changes**
Starting May 4, 2026, running Custom Agents will require Notion credits. These credits will be purchasable as an add-on for Business and Enterprise plans on that same date. Until the terms take effect on May 1, 2026, all current operations remain unchanged.

**References**
*   Full updated terms: [Link provided in email body]
*   Summary overview: [Link provided in email body]
*   Original Message ID: `19d50f4f7945d100`


## [4/17] [Dashboard Report] Retail Media - DD Dashboard | Fri 3 Apr 11:00AM +08
Source: gmail | Thread: 19d514aa8123e26b | Labels: Inbox, Updates | Priority: None | Senders: Datadog HQ | Last Date: Fri, Apr 3, 2026, 3:02 AM | Last Updated: 2026-04-03T06:01:15.987435+00:00
**Daily Work Briefing: Retail Media Dashboard Report**

**Key Participants & Roles**
*   **Michael:** Recipient of the report; primary stakeholder for dashboard monitoring.
*   **Team Datadog / Datadog HQ (no-reply@dtdg.eu):** Sender providing automated reporting and support resources.

**Main Topic & Request**
The sender provided an attachment containing the **"Retail Media - DD Dashboard"** report. The specific scope of this data covers the **past 3 days**. The intent is to ensure Michael has up-to-date metrics for monitoring purposes.

**Pending Actions & Ownership**
*   **Action:** Review and analyze the attached "Retail Media - DD Dashboard" report covering the last three days.
*   **Owner:** Michael.

**Decisions Made**
No strategic decisions or approvals were recorded in this thread; this is a standard data delivery notification.

**Key Dates & Deadlines**
*   **Report Generation Date:** Friday, April 3, 2026.
*   **Transmission Time:** 11:00 AM +08 (Timezone).
*   **Data Scope:** The 3-day period preceding the report generation date (March 31 – April 2, 2026, assuming standard rolling window).

**Specific References**
*   **File Name:** Retail Media - DD Dashboard.
*   **Sender Email:** no-reply@dtdg.eu.
*   **Support Contact:** Manage reports via the link in the footer; physical address provided is Datadog HQ (620 8th Avenue, 45th Floor, New York, NY 10018).

**Next Steps**
Michael should verify data integrity and monitor trends within the specified three-day window. No further action from the sender is required unless anomalies are detected during the review.


## [5/17] Re: Hyper stores visual - Advertima
Source: gmail | Thread: 19b6e85f67d0d448 | Labels: Inbox | Priority: None | Senders: Abdel-R., Rajkumar | Last Date: Fri, Apr 3, 2026, 2:44 AM | Last Updated: 2026-04-03T06:01:54.634333+00:00
**Subject:** Daily Briefing: Hyper Stores Visual Management & Campaign Execution (Updated Apr 3)

**Key Participants:**
*   **Rajkumar Romendro (NTUC Guest):** Client-side Coordinator; submits content, requests schedule changes, and tracks status.
*   **Jan Plojhar (Advertima):** Customer Success Manager; manages scheduling, technical implementation, and final confirmations.
*   **Simone Pici (Advertima):** Customer Operations Manager; handles asset uploads and validates technical compliance.
*   **Christian Bahrendt (Advertima):** Technical Lead; clarified system limitations regarding selective ad slots.
*   **Abdel-Rahman Khater (Advertima):** Director Project Delivery; provided end-of-year content expiration notice.

**Main Topic:**
Management of digital advertising assets for NTUC Hyper stores (SCO/Cashier, Wall of Value, and Entrance screens), including uploads, technical compliance corrections, schedule updates, campaign replacements, and immediate content termination.

**Pending Actions & Ownership:**
*   **Urgent Action Required:** As of Apr 3, 2026, at 2:44 AM, Rajkumar Romendro requested the immediate cessation of the NPS content video playback. Status pending confirmation from Advertima.
*   **Active Campaigns:**
    *   **Mar 5 – Mar 25, 2026:** "Raya Scan at Entry" is active, replacing the expiring "Scan & Go."
    *   **Feb 26 – Mar 4, 2026:** ActiveSg (Briq Pte Ltd) Weeks 1 & 2.
*   **Historical Context:** On Feb 27, Raj confirmed a campaign period change for ActiveSg to Weeks 1 & 2 of March; Jan confirmed these adjustments on Mar 3. All uploads and adjustments between Dec 30, 2025, and Mar 16, 2026, remain marked as completed in the tracking sheet.

**Key Decisions & Technical Constraints:**
*   **Selective Play Slots:** On Feb 10, Raj requested isolated ads at VivoCity Hyper Cashier for a photo shoot (scheduled Feb 11). Advertima (Christian Bahrendt) declined, citing system architecture that uses one central playlist across all screens. Isolated play requires rewiring and testing, impossible with short notice. Future requests require **one week prior notice**.
*   **Technical Compliance:** Multiple uploads (Feb 9–13) were initially rejected due to non-integer duration/framerate or missing portrait assets. Raj updated specifications:
    *   Duration: Integer seconds only (e.g., 15.00).
    *   Resolution: 1920x1080 landscape / 1080x1920 portrait.
    *   Framerate: 25 or 30 fps integer.

**Key Dates & Campaign Timelines:**
*   **Dec 31, 2025:** Wall of Value expired (Christmas content). No replacement provided; filler content requested for Jan 1, 2026.
*   **Mar 12 – Apr 30, 2026:** Haleon campaign scheduled.
*   **Mar 16, 2026:** NPS content video set for playback (Evergreen). *Note: Playback requested to be stopped immediately on Apr 3, 2026.*

**References:**
*   Google Sheet for tracking status: `https://docs.google.com/spreadsheets/d/1w2gA4DlIClJonZ7k3IfrdifyX87DKMwGXqiAlkap2kY/edit`
*   Key Assets updated: NPS, Xtra Play Market, ActiveSg (Briq Pte Ltd), Raya Scan at Entry, Haleon.


## [6/17] You have no events scheduled today.
Source: gmail | Thread: 19d5013cda0bfcf5 | Labels: Inbox, Updates | Priority: None | Senders: Google Calendar | Last Date: Thu, Apr 2, 2026, 9:22 PM | Last Updated: 2026-04-02T22:01:49.118550+00:00
**Daily Work Briefing Summary**

*   **Key Participants & Roles:**
    *   **Michael Bui** (Recipient): Account holder for `michael.bui@fairpricegroup.sg`. Subscribed to daily agenda notifications for the "Digital Business Tech Release/Changes" calendar.
    *   **Google Calendar System** (`calendar-notification@google.com`): Automated notification sender.

*   **Main Topic/Request:**
    *   Delivery of a standard automated daily agenda reminder confirming the user's schedule status for the current day.

*   **Pending Actions & Ownership:**
    *   **No actions pending.** The email serves as an informational notification only.
    *   No tasks, meetings, or deliverables are assigned to Michael Bui based on this message.

*   **Decisions Made:**
    *   None. This is a system-generated status update confirming the absence of scheduled events.

*   **Key Dates, Deadlines, & Follow-ups:**
    *   **Notification Date/Time:** April 2, 2026, at 9:22 PM.
    *   **Relevant Date:** Friday, April 3, 2026 (Current day referenced in the agenda).
    *   **Status Confirmation:** No events scheduled for Michael Bui on April 3, 2026.
    *   **Follow-up Required:** None.

*   **Additional Context:**
    *   The notification indicates subscription to specific calendar updates ("Digital Business Tech Release/Changes").
    *   Settings can be modified by logging into `https://calendar.google.com/calendar/`.
    *   Email contains standard confidentiality and privilege disclaimers.


## [7/17] Simplifying Jira's create experience
Source: gmail | Thread: 19d4f67520258079 | Labels: Inbox, Updates | Priority: None | Senders: Atlassian | Last Date: Thu, Apr 2, 2026, 6:14 PM | Last Updated: 2026-04-02T22:02:03.567388+00:00
**Daily Work Briefing: Simplifying Jira's Create Experience**

**Key Participants & Roles**
*   **Sender:** Atlassian (info@e.atlassian.com) – Product team communicating platform updates.
*   **Audience:** Site Administrators and end-users within the tenant.

**Main Topic**
Atlassian is rolling out an improved "create experience" for Jira work items (the "big blue button"). The update aims to make creating new tickets quicker, cleaner, and more intelligent by introducing a simplified default interface while retaining access to full forms when necessary.

**Pending Actions & Ownership**
*   **Action:** No immediate action required from administrators today.
*   **Owner:** Atlassian (for rollout execution); Administrators (optional intervention).
*   **Optional Admin Action:** Administrators who prefer the full-form layout for all users must utilize a new toggle to opt out of the simple default experience. This is not mandatory unless specific team workflows require it.

**Decisions Made**
*   **Product Strategy:** Atlassian has decided to shift the default create view from the full form to a "compact" window containing essentials (summary, description, required fields, and up to three optional fields).
*   **Configuration Logic:**
    *   For team-managed projects: The top three highest-ranked optional fields will be shown.
    *   For company-managed projects: The first three optional fields on the create screen will be shown.
*   **Flexibility:** Users can expand the compact window to access the full-form layout at any time. Projects with complex needs (extra required fields, tabs) will automatically default to the full form.
*   **Compatibility:** Existing configurations (required fields, validation rules, workflow requirements, and Forge app modifications) remain fully functional without modification.

**Key Dates & Follow-ups**
*   **Announcement Date:** April 2, 2026 (18:14).
*   **Rollout Start:** Late April 2026.
*   **Communication Schedule:** Further details and release notes will be shared closer to the launch date.
*   **Adoption Note:** The experience is rolling out gradually; availability may vary by tenant initially.

**Specific References**
*   **Resource Title:** "Simplifying Jira's create experience" / "An improved Jira create experience is on its way."
*   **Email Metadata Labels:** Inbox, Updates.
*   **Atlassian Contact/Location:** 341 George Street, Sydney, NSW, 2000, Australia.


## [8/17] Unlock your potential with FairPrice Group’s Internal Talent Marketplace
Source: gmail | Thread: 19d4d6c1534ec8e5 | Labels: Inbox, Updates | Priority: None | Senders: HR Announcement | Last Date: Thu, Apr 2, 2026, 9:00 AM | Last Updated: 2026-04-02T10:02:37.849254+00:00
**Daily Work Briefing: Internal Talent Marketplace Expansion**

**Key Participants & Roles**
*   **HR Announcement (hr@fairpricegroup.sg):** Issuer of the official policy update regarding talent mobility.
*   **Eligible Staff:** All Corporate/HQ Non-Executive and Frontline Executive staff at FairPrice Group (FPG).
*   **Support Contact:** ta@fairpricegroup.sg for clarifications.

**Main Topic**
Announcement of the expansion of FPG's Internal Talent Marketplace to explicitly include **Corporate/HQ Non-Executive** and **Frontline Executive** staff. This change enables cross-functional mobility, allowing HQ staff to access Frontline Executive roles and all eligible employees to discover internal opportunities for skill development and career growth via the **myTalentHub** portal.

**Eligibility Criteria (Mandatory)**
To apply for an internal transfer, candidates must meet all of the following:
*   **Tenure:** Minimum 2 years in current position for Job Grade S/D; minimum 3 years for Job Grade C and above.
*   **Performance:** Attained at least a "Green" rating in the last 2 to 3 years.
*   **Discipline:** No recorded Performance Improvement Plan (PIP) or disciplinary actions within the last 2 to 3 years.
*   **Competency:** Meets minimum competencies for the target role.
*   **Job Grade:** Current role must be at least the same job grade as the new role applied for.

**Pending Actions & Ownership**
*   **Action:** Review eligibility and explore opportunities on the portal.
    *   **Owner:** All eligible staff (Corporate/HQ Non-Executive and Frontline Executive).
    *   **Instruction:** Click "Click to visit myTalentHub" or download the "HEAR WHAT IT'S LIKE TO MAKE THE MOVE!" resource.
*   **Action:** Consult step-by-step application guide.
    *   **Owner:** Prospective applicants.
    *   **Instruction:** Access the comprehensive guide provided in the email body.
*   **Action:** Submit inquiries regarding eligibility or process.
    *   **Owner:** Staff with questions.
    *   **Contact:** ta@fairpricegroup.sg.

**Decisions Made**
*   FPG has officially extended the Internal Mobility programme scope to include previously excluded groups (Corporate/HQ Non-Executive and Frontline Executive).
*   HQ staff are now explicitly authorized to apply for Frontline Executive roles to encourage cross-functional mobility.

**Key Dates & Follow-ups**
*   **Announcement Date:** April 2, 2026, at 9:00 AM.
*   **Effective Status:** Immediate ("The doors are officially wide open").
*   **Application Window:** Open indefinitely until roles are filled; no specific closing deadline stated in the announcement.


## [9/17] Opsgenie Alert: [Datadog] [P2] [Warn] Service marketing-service has a high error rate on env:prod
Source: gmail | Thread: 19d4cfd200d6d7bc | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Thu, Apr 2, 2026, 7:04 AM | Last Updated: 2026-04-02T10:02:57.609786+00:00
**Daily Work Briefing: Opsgenie Alert Thread**

**Key Participants & Roles**
*   **Automated Source:** Opsgenie (Notification System) / Datadog (Monitoring Integration).
*   **Assigned Team:** DPD Staff Excellence - Retail Media (Responders).
*   **Notified Channels/Groups:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`.
*   **System Owner:** `dpd-grocery-retail-media-eu` (Datadog Integration).

**Main Topic & Request**
An automated alert was triggered for the **marketing-service** in the **prod** environment, indicating a high error rate. The system requested immediate investigation into:
1.  HTTP request error metrics on Datadog APM.
2.  Kubernetes deployment status (GKE) in cluster `fpon-cluster`.
3.  Execution of the specific runbook for this service.

**Alert Specifications**
*   **Trigger Condition:** Error rate > 5% (`0.05`) over the last 10 minutes.
*   **Current Metric Value:** 0.016 (1.6%), which is currently below the 5% threshold but triggered a P2 alert, likely due to system state persistence or specific aggregation logic at trigger time.
*   **Priority:** P2.
*   **Service Tags:** `env:prod`, `service:marketing-service`, `managed_by:datadog-sync`, `monitor`.

**Pending Actions & Ownership**
*   **Action Required:** Investigate the high error rate, check Datadog APM traces, review K8s deployment health, and follow the provided runbook.
*   **Owner:** DPD Staff Excellence - Retail Media team (via Opsgenie assignment).
*   **Status:** Alert remains open with no human acknowledgment or resolution updates recorded in this thread.

**Decisions Made**
*   No decisions were made within this thread; it contains only automated system notifications.

**Key Dates & References**
*   **Alert Created:** Apr 2, 2026, 14:59:08 UTC (Note: Email timestamps show 06:59 AM local time).
*   **Last Updated (Metric):** 2026-04-02 06:58:06 +0000.
*   **Critical Links:**
    *   Datadog Monitor: `https://app.datadoghq.eu/monitors/17447106`
    *   Runbook: `https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book`
    *   K8s Overview: `.../fpon-cluster/default/marketing-service/overview`
*   **Unique Identifiers:** Alert ID `a8f4a0be-ab4e-45aa-a0fc-8ea63cb490c2-1775113148971`, TinyID `139454`.

**Follow-up Required**
*   Immediate technical review by the Retail Media team to confirm if the alert is a false positive (given metric 0.016 < threshold 0.05) or requires remediation.


## [10/17] Accepted: ACNxOsmos: Daily Cadence @ Thu Apr 2, 2026 1:30pm - 2pm (SGT) (michael.bui@fairpricegroup.sg)
Source: gmail | Thread: 19d4caaff361b29c | Labels: Inbox | Priority: None | Senders: Shubhangi Agrawal | Last Date: Thu, Apr 2, 2026, 5:29 AM | Last Updated: 2026-04-02T06:01:05.075274+00:00
**Daily Work Briefing: ACNxOsmos Daily Cadence**

**Key Participants & Roles**
*   **Organizer:** Michael Bui (michael.bui@fairpricegroup.sg)
*   **Core Attendees:** Flora Wo, Tanish Nevatia, Vipul Gupta, Barkha Kewalramani (ntucguest.com), Rahul Jain, Tiongsiong Tee, Daryl Ng, Shravan Kankaria, John Henry Mantaring, Artharn Senrit, Nikhil Grover, Aman Khatri, Tanul Mehta, Nabhey Samant, Winson Lim.
*   **Accenture Representatives:** Siddharth Aklujkar, Rachit Sachdeva, Satish Pamidimarthi.
*   **Optional Attendee:** Ravi Goel.

**Main Topic/Request**
Confirmation of attendance and distribution of the project roadmap for the "FPG Project Plan 2905025." The meeting serves as the designated daily cadence for the ACNxOsmos initiative.

**Pending Actions & Owners**
*   **Join Meeting:** All listed guests are expected to attend the scheduled slot. No specific pre-meeting action items were identified in this thread; the primary task is participation at the scheduled time.

**Decisions Made**
*   **Meeting Confirmation:** The invitation was accepted by Shubhangi Agrawal (onlinesales.ai) as confirmed in the earliest log entry.
*   **Schedule Fixed:** The recurring daily cadence is locked for Thursday, April 2, 2026.

**Key Dates & Follow-ups**
*   **Date:** Thursday, April 2, 2026.
*   **Time:** 1:30 PM – 2:00 PM (Singapore Standard Time).
*   **Reference Document:** "FPG Project Plan 2905025" (Attached to the invitation).
*   **Meeting Access:** Google Meet link (`meet.google.com/ise-ydtd-por`) and US dial-in details provided.


## [11/17] [JIRA] (DPD-838) Transition to Impression-Based Inventory & Multi-Banner Delivery
Source: gmail | Thread: 19d2e82fa82f66fe | Labels: Inbox, Updates | Priority: None | Senders: Nikhil | Last Date: Thu, Apr 2, 2026, 3:24 AM | Last Updated: 2026-04-02T06:01:30.039228+00:00
**Daily Work Briefing: JIRA (DPD-838)**

**Project Context**
*   **JIRA ID:** DPD-838
*   **Topic:** Transition to Impression-Based Inventory & Multi-Banner Delivery
*   **Category:** Ecom/Omni
*   **Status:** IN DEVELOPMENT (Updated Apr 2, 2026)
*   **Assignee:** Chee Hoe Leong
*   **Last Update:** April 2, 2026 (Milind Badame comment)

**Key Participants**
*   **Chee Hoe Leong:** DM; Provided definitive answers to technical ambiguities and updated ticket status.
*   **Nikhil Grover:** Product Manager; Confirmed slot value constraints in reply to Chee Hoe Leong.
*   **Michael Bui:** Technical Stakeholder (Previously identified blockers).
*   **Milind Badame:** QA/Test Lead; Determined E2E automation requirements.

**Main Topic & Request**
Following critical clarifications raised by Michael Bui on Mar 28, the team received definitive responses regarding scope and logic. The project status remains "IN DEVELOPMENT," now updated with final testing constraints from Milind Badame on April 2.

**Resolved Technical Ambiguities & Decisions**
1.  **Migration Scope:** Confirmed that video support is restricted to **Omni Home** and **FPPay**. Category and Search pages will remain on the legacy MPS service (No migration required).
2.  **Non-Endemic Identification:** The method uses a Boolean value explicitly labeled **"Endemic"** or **"Non-endemic"**, rather than substring matching logic.
3.  **OSMOS Capacity Limits:** Support for limits exceeding 10 `pcnt` items is expected by early April; confirmation of on-track delivery was pending Monday verification (Apr 2 status update required).
4.  **Position Tracking & Slot Values:** The "position" value excludes multiple banners targeting the same slot (e.g., preventing duplicate 999s), not for sequencing. Values are limited to integers **1–20** or empty (default).
5.  **Video Behavior:** Auto-play and auto-scroll remain **Front-End managed**. Sales policy limits videos to one per Carousel.
6.  **Failure Handling:** If no banners are configured, the API returns nothing, causing banners to collapse (managed by Ops). API unavailability results in the same output; an incident will be created.

**Testing & Automation Decisions**
*   **E2E Automation Status:** Determined as **No**. Milind Badame confirmed on April 2 that this scenario "cannot be automated." The `Requires_e2e_test` flag has been updated to No. Manual testing is required for the new logic.

**Pending Actions & Ownership**
*   **Action:** Confirm on-track delivery of OSMOS capacity >10 by early April.
    *   **Owner:** Chee Hoe Leong / Engineering Lead (Target: Monday).
*   **Action:** Update SOP to reflect slot logic for excluding duplicate banners and Integer 1-20 constraint.
    *   **Owner:** Development Team / Ops.
*   **Action:** Execute manual E2E testing protocols (per Milind Badame's determination that automation is not feasible).
    *   **Owner:** QA Team / Milind Badame.

**Key Dates & Follow-ups**
*   **Last Update Timestamp:** April 2, 2026, at 11:15 AM Singapore Time (Milind Badame comment regarding E2E automation).
*   **Status Change:** Moved to "IN DEVELOPMENT" on Apr 1; Automated testing requirement removed on Apr 2.

**Summary for Executive Review**
The DPD-838 initiative has resolved prior scope ambiguities and entered development. Key decisions confirm that only Omni Home and FPPay will adopt the new video-enabled multi-banner architecture; legacy MPS remains in place for Category/Search pages. Technical logic is now defined: non-endemic identification uses explicit Boolean labels ("Endemic"/"Non-endemic"), and slot values are integers 1–20 used to prevent duplicate renders rather than sequence ordering. OSMOS capacity expansion (>10 items) is targeted for early April pending Monday confirmation. Failure states result in banner collapse with incident creation, while media behaviors remain Front-End responsibilities. Crucially, on April 2, Milind Badame determined that the new logic **cannot be automated**, updating the `Requires_e2e_test` status to "No." Consequently, QA must proceed with manual E2E testing strategies for this release.


## [12/17] [Dashboard Report] Retail Media - DD Dashboard | Thu 2 Apr 11:00AM +08
Source: gmail | Thread: 19d4c254d1e98e3f | Labels: Inbox, Updates | Priority: None | Senders: Datadog HQ | Last Date: Thu, Apr 2, 2026, 3:03 AM | Last Updated: 2026-04-02T06:01:42.181692+00:00
**Daily Work Briefing: Retail Media Data Update**

**Key Participants & Roles**
*   **Michael:** Recipient of the report (Action Owner).
*   **Datadog HQ / Team Datadog:** Sender; provided system-generated monitoring reports.
*   **System:** Automated sender interface (`no-reply@dtdg.eu`).

**Main Topic/Request**
Transmission of the **"Retail Media - DD Dashboard"** report containing aggregated data for the past three days leading up to April 2, 2026. The email serves as an automated notification rather than a specific request requiring immediate intervention beyond review.

**Pending Actions & Ownership**
*   **Action:** Review the attached "Retail Media - DD Dashboard" report.
*   **Owner:** Michael.
*   **Context:** The report includes three days of historical data for monitoring purposes. No explicit deadline was set in the email, but standard practice implies review within the current business day (April 2).

**Decisions Made**
No strategic decisions or policy changes were documented in this thread. The communication is purely informational regarding data availability.

**Key Dates & Follow-ups**
*   **Report Generation Date:** Thursday, April 2, 2026, at 11:00 AM (+08 time zone).
*   **Email Timestamp:** April 2, 2026, at 3:03 AM.
*   **Data Scope:** Past three days relative to the report generation date (approx. March 30 – April 2, 2026).
*   **Upcoming Follow-up:** None scheduled automatically; depends on Michael's analysis of anomalies or trends in the attached data.

**Specific References & Metadata**
*   **Attachment Filename/Subject:** Retail Media - DD Dashboard.
*   **Sender Email:** `no-reply@dtdg.eu`.
*   **Last Message ID:** `19d4c254d1e98e3f`.
*   **Labels:** Inbox, Updates.
*   **Company Address (Footer):** 620 8th Avenue, 45th Floor, New York, NY 10018.


## [13/17] Introducing our New Enterprise Governance & Compliance Policy and Policy Management Framework
Source: gmail | Thread: 19d4beb2c8723007 | Labels: Inbox, Updates | Priority: None | Senders: GRC | Last Date: Thu, Apr 2, 2026, 1:59 AM | Last Updated: 2026-04-02T02:01:57.385455+00:00
**Daily Work Briefing: Enterprise Governance & Compliance Update**

**Key Participants & Roles**
*   **Sender:** GRC (governance_announcements@fairpricegroup.sg) – Issued the announcement on behalf of the Governance, Risk & Compliance function.
*   **Recipients:** All FPG employees and leadership teams.
*   **Governance Structure Defined:**
    *   **1st Line:** Business Units (BUs) and Corporate Functions (CFs). Role: Own risks and ensure daily operational compliance.
    *   **2nd Line:** GRC. Role: Provide oversight, framework design, and expert guidance.
    *   **3rd Line:** Internal Audit. Role: Provide independent assurance to Senior Management and the Board.

**Main Topic & Request**
*   **Introduction of New Frameworks:** Launch of the **Enterprise Governance & Compliance Policy** and the **Policy Management Framework**.
*   **Objective:** To strengthen organizational resilience, ensure ethical operations within legal boundaries, and standardize policy development/approval processes.
*   **Call to Action:** Employees must acknowledge their role in risk ownership, adhere to the "Three Lines of Defence" model, and utilize the new Policy Management lifecycle for all documents.

**Pending Actions & Ownership**
*   **All Employees:** Await and complete an annual compliance refresher and policy acknowledgement exercise (scheduled later this year).
*   **Policy Owners/Writers:** Must assign ownership based on business needs or regulatory changes; use prescribed templates during drafting.
*   **Stakeholders:** Review policies for operational feasibility and legal compliance before approval.
*   **Leadership Approval Required:**
    *   **Enterprise-wide Policies:** Must be approved by the GCEO and CFO.
    *   **BU/CF-specific Policies:** Must be approved by respective Business Unit or Corporate Function Leadership Teams (LT).
*   **Documentation Team:** Publish approved versions as the "single source of truth" on the FPG Lighthouse site; retire obsolete documents by prefixing with "[Retired]" and archiving them.

**Decisions Made**
*   Adoption of the **Three Lines of Defence model** for independent review and accountability.
*   Implementation of a mandatory **seven-stage policy lifecycle**: Initiation, Drafting, Review, Approval, Publication, Periodic Review, and Archival.
*   Establishment of **Accountability** as a key performance indicator (KPI) for leadership and operational roles.

**Key Dates & Follow-ups**
*   **Announcement Date:** April 2, 2026, 1:59 AM.
*   **Upcoming Deadline:** Annual compliance refresher and acknowledgement exercise to be introduced later in 2026 (specific date TBD).
*   **Review Cycle:** All policies must undergo periodic review at least annually.
*   **Support Channels:** Questions regarding the policy or framework should be directed to `ask_grc@fairpricegroup.sg`. FAQs are available for "Enterprise Governance & Compliance" and "Policy Management."


## [14/17] Opsgenie Alert: [Datadog] [P4] [Triggered] Service marketing-service has an abnormal change in throughput on env:prod
Source: gmail | Thread: 19d4bcf0d759918a | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Thu, Apr 2, 2026, 1:34 AM | Last Updated: 2026-04-02T02:02:13.006556+00:00
**Daily Work Briefing: Opsgenie Alert Summary**

**Key Participants & Roles**
*   **System:** Opsgenie (Alert Orchestration), Datadog (Monitoring Source).
*   **Notification Channels/Teams:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`.
*   **Assigned Responders:** DPD Staff Excellence - Retail Media.
*   **Service Owner:** marketing-service team (implied via runbook and service context).

**Main Topic/Request**
*   **Alert Trigger:** P4 severity alert indicating an abnormal change in throughput for the `marketing-service` in the production environment (`env:prod`).
*   **Technical Specifics:** The metric `sum:trace.http.request.hits{env:prod,service:marketing-service}` showed 100% anomalous values (more than 3 deviations from predicted values) over a 15-minute window.
*   **Timestamp of Event:** Last Updated at 2026-04-02 01:28:10 UTC; Alert Created on Apr 2, 2026, at approximately 9:29 AM (local time context).

**Pending Actions & Ownership**
*   **Immediate Action Required:** Investigate the throughput anomaly and validate service health.
*   **Ownership:** DPD Staff Excellence - Retail Media.
*   **Required Investigation Steps (per alert description):**
    1.  Review Datadog APM HTTP request resources: [Link](https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod).
    2.  Check K8s deployment status in `asia-southeast1/fpon-cluster`: [Link](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview?cloudshell=false&project=fponprd).
    3.  Consult the Runbook for troubleshooting: [Link](https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book).

**Decisions Made**
*   No manual decisions recorded in this thread; the alert was automatically triggered and routed based on system thresholds.

**Key Dates, Deadlines, & Follow-ups**
*   **Alert Date:** April 2, 2026.
*   **Resolution Status:** Unresolved (No closing comments or status updates found in the provided log).
*   **Follow-up Needed:** Immediate investigation by the assigned responder group to determine if the anomaly is a false positive, deployment issue, or traffic spike requiring mitigation.


## [15/17] Declined: [DPD AI Guild] Committee Monthly Meeting @ Monthly from 10am to 10:50am on the first Tuesday (SGT) (Michael Bui)
Source: gmail | Thread: 19d4bc56d5361681 | Labels: Inbox | Priority: None | Senders: Jazz Tong | Last Date: Thu, Apr 2, 2026, 1:18 AM | Last Updated: 2026-04-02T02:02:25.237497+00:00
**Daily Work Briefing: [DPD AI Guild] Committee Monthly Meeting**

**Key Participants & Roles**
*   **Michael Bui:** Organizer (fairpricegroup.sg)
*   **Jazz Tong:** Attendee (declined invitation); Email: jazz_tong@fairpricegroup.sg
*   **Varun Chauhan:** Guest
*   **James Lai Li Hao:** Guest
*   **Mohammed Miran:** Guest
*   **Zheng Ming New:** Guest

**Main Topic/Request**
Regular monthly meeting for the DPD AI Guild Committee. The session is scheduled to run from 10:00 AM to 10:50 AM on the first Tuesday of every month (Singapore Standard Time).

**Decisions Made**
*   **RSVP Status:** Jazz Tong has formally declined the invitation. No other attendance confirmations or declines are recorded in this thread.
*   **Meeting Format:** Hybrid setup utilizing Google Meet and a physical location.

**Pending Actions & Ownership**
*   **Status Check:** No new action items were generated in this thread. The organizer (Michael Bui) retains ownership of agenda setting and meeting facilitation for the next cycle.
*   **Calendar Management:** Jazz Tong should verify if they wish to remain subscribed to future notifications from this calendar, as per the email footer instructions.

**Key Dates & Details**
*   **Meeting Time:** Monthly, 10:00 AM – 10:50 AM (SGT), first Tuesday of the month.
*   **Location:** FairPrice Hub-11-L11 Room 10 (6) [Google Meet].
*   **Upcoming Meeting Reference Date:** The system timestamp indicates a historical record from April 2, 2026.
*   **Meeting Identifier:** Last message ID `19d4bc56d5361681`.

**Technical Links**
*   **Google Meet URL:** meet.google.com/zhj-udzb-apd
*   **Phone Access:** (US) +1 608-571-6843 | PIN: 490466397


## [16/17] Daily digest: updates from Kyle Nguyen
Source: gmail | Thread: 19d4b50123517161 | Labels: Inbox, Updates | Priority: None | Senders: Confluence | Last Date: Wed, Apr 1, 2026, 11:10 PM | Last Updated: 2026-04-02T02:02:36.121677+00:00
**Daily Work Briefing: Confluence Update Digest**

**1. Key Participants & Roles**
*   **Kyle Nguyen:** Content Contributor (User). Identified as the individual who made recent updates to a specific guideline page.
*   **Confluence System (Atlassian):** Automated sender of the daily digest notification.
*   **Recipient:** The user receiving this summary, indicated by the "content you've contributed to" notification.

**2. Main Topic/Request**
*   **Subject:** April 1, 2026, Confluence Daily Digest highlighting changes to contributed content.
*   **Focus Area:** Updates made to the document titled **"Resources Tagging Guideline."**
*   **Purpose:** To notify the recipient of specific modifications Kyle Nguyen implemented within this guideline.

**3. Pending Actions & Ownership**
*   **Action:** Review the latest version of "Resources Tagging Guideline" and verify changes made by Kyle Nguyen.
*   **Owner:** Recipient (implied, as the digest is targeted at contributors).
*   **Next Step:** Click the "View changes" link within the Confluence notification to inspect the specific edits.

**4. Decisions Made**
*   No strategic decisions or business approvals were recorded in this thread. The content represents an automated system notification regarding a completed update action by Kyle Nguyen on April 1, 2026.

**5. Key Dates & Deadlines**
*   **Date of Event:** April 1, 2026.
*   **Timestamp:** 11:10 PM (Notification sent).
*   **Follow-up:** Immediate review recommended to stay current with the "Resources Tagging Guideline."

**Specific References Required for Context**
*   **Platform:** Atlassian Confluence (`confluence@ntuclink.atlassian.net`).
*   **Document Name:** Resources Tagging Guideline.
*   **Update Author:** Kyle Nguyen.
*   **Message ID Reference:** `19d4b50123517161`.


## [17/17] You have no events scheduled today.
Source: gmail | Thread: 19d4b0a92d907156 | Labels: Inbox, Updates | Priority: None | Senders: Google Calendar | Last Date: Wed, Apr 1, 2026, 9:54 PM | Last Updated: 2026-04-01T22:01:37.998475+00:00
**Daily Work Briefing Summary**

**Key Participants & Roles:**
*   **Michael Bui** (Account holder: `michael.bui@fairpricegroup.sg`): Recipient of the daily agenda notification.
*   **Google Calendar (`calendar-notification@google.com`)**: Automated system sender providing schedule updates for the "Digital Business Tech Release/Changes" calendar.

**Main Topic/Request:**
The email is an automated notification confirming that there are **no events scheduled** on Thursday, April 2, 2026, for Michael Bui within the subscribed "Digital Business Tech Release/Changes" calendar. The message primarily serves as a status confirmation and includes instructions on how to modify subscription settings via Google Calendar if necessary.

**Pending Actions & Ownership:**
*   **No actions pending.** The summary explicitly states: "You have no events scheduled today."
*   **Optional Action (Owner: Michael Bui):** If the user wishes to alter which calendars are included in future daily agendas, they must log in to `https://calendar.google.com/calendar/` and adjust notification settings.

**Decisions Made:**
No decisions were made or recorded in this thread; it is a system-generated status report.

**Key Dates & Deadlines:**
*   **Notification Sent:** April 1, 2026, at 9:54 PM.
*   **Relevant Date (Today):** Thursday, April 2, 2026.
*   **Follow-ups:** None required based on current schedule status.

**Reference Data:**
*   **Account Email:** `michael.bui@fairpricegroup.sg`
*   **Last Message ID:** `19d4b0a92d907156`
*   **Labels:** Inbox, Updates
*   **Calendar Source:** Digital Business Tech Release/Changes
