

## gchat/space/AAAAxwwNw2U: #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 16 | Last Activity: 2026-03-17T17:06:19.423000+00:00
**Daily Work Briefing: #dd-dpd-engage-alert (2026-03-17)**

**Key Participants & Roles**
*   **Datadog Monitor Bot:** Primary notification source for production incidents.
*   **@hangouts-dd-dpd-engage-alert:** Channel group receiving all alerts.
*   **@oncall-dpd-engage-dynamics:** On-call squad notified during critical MyInfo failures (15:00 UTC).
*   **Squads Involved:** Journey, Dynamics, Compass.

**Main Topic / Summary of Incidents**
The channel recorded 49 automated alerts between 10:37 and 17:06 UTC regarding production instability in the "Engage" tribe. Three primary services were affected:
1.  **`engage-my-persona-api-go` (Dynamics Squad):** Experienced intermittent latency spikes (>1.8s P90, >2.6s P99) and high error rates for MyInfo endpoints (`/new-myinfo/confirm`, `/new-myinfo/signup/confirm`, `/v1/oidc/token`). Critical failure occurred at 15:00 UTC where success rate dropped to **87.5%** (triggering a <90% monitor).
2.  **`frontend-gateway` (Journey Squad):** Recurring availability issues for recommendation engine endpoints (`orchid`, `boughtbought`). Success rates dipped below 99.9%, with P99 latency spiking to **14.617s** for the `boughtbought` endpoint at 16:28 UTC.
3.  **`lyt-p13n-layout` (Compass Squad):** Intermittent high latency (>1.8s) on landing page (`/v1/home`) and scan-door endpoints.

**Pending Actions & Ownership**
*   **Investigate `engage-my-persona-api-go`:** The Dynamics squad must investigate the root cause of MyInfo latency and error rate spikes, particularly around 17:05 UTC (P99 latency reached 7.152s). *Owner: Squad: Dynamics.*
*   **Analyze Frontend Gateway Slowness:** Journey squad to review `orchid` and `boughtbought` request patterns causing sub-99.9% success rates and high P99 latency. *Owner: Squad: Journey.*
*   **Monitor Stability:** Continue observing the recovery of Android linkpoint load issues and Algolia search anomalies, which have shown transient fluctuations but are currently recovered.

**Decisions Made**
No manual decisions were recorded; all alerts were automated trigger/recovery events from Datadog monitors. No user intervention was required to resolve the incidents as most metrics returned to normal (Recovered) status shortly after triggering.

**Key Dates & Follow-ups**
*   **10:37 UTC:** Initial cluster of alerts triggered for Algolia, MyInfo latency, and Android availability. All recovered by 11:09 UTC.
*   **14:25 - 16:55 UTC:** Secondary wave of instability affecting `frontend-gateway` (Orchid/Boughtbought) and `engage-my-persona-api-go`.
*   **15:00 UTC:** Critical alert for MyInfo signup success rate (<90%, value 87.5%). Escalated to on-call.
*   **16:28 UTC:** Maximum latency recorded for `boughtbought` (P99: 14.617s).
*   **17:05 - 17:06 UTC:** Peak instability for `engage-my-persona-api-go` with P99 latency of 7.152s and error rate >0.1%.

**Status at End of Log:** Most monitors show "Recovered" status, though intermittent triggers continue through 17:06 UTC.


## gchat/space/AAAAsbHANyc: Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-03-17T17:03:46.178000+00:00
**Daily Work Briefing: Shopping Cart Notification Monitor Alerts**

**Key Participants & Roles**
*   **System:** Datadog (Automated Monitoring) triggering alerts to the `@hangouts-ShoppingCartNotification` channel.
*   **Team:** DPD Pricing Cart (`team:dpd-pricing-cart`, `tribe:pricing`).
*   **Services Involved:** `st-cart-prod` (Shopping Cart Service), `frontend-gateway`.

**Main Topic**
The conversation consists entirely of automated Datadog alerts regarding performance degradation and availability issues in the Production environment. Alerts alternate between "Triggered" (issues detected) and "Recovered" (performance returned to normal). No human discussion or manual intervention is recorded in this log.

**Issues Detected & Resolved**
1.  **Cart Service Availability:**
    *   **Issue:** `post_/cart` request success rate dropped below 99.9% (Metric: 99.803%).
    *   **Status:** Recovered to 100%.
2.  **Frontend Gateway Latency:**
    *   **Get Guest Shopping List (v2):** P90 latency exceeded 2s; P99 exceeded 3s. Multiple trigger/recovery cycles observed throughout the day (e.g., 05:58, 07:10, 14:08).
    *   **Put Product to Wish List:** P90/P99 latency exceeded thresholds (5s/6s) multiple times (e.g., 06:50, 12:57, 16:01).
    *   **Get Wish List by ID:** Frequent P90 (>1.7s) and P99 (>3.1s) latency spikes observed, particularly between 13:33 and 15:42.
    *   **Get Cart:** P99 latency exceeded 1.8s in the late afternoon (16:44, 17:00).

**Pending Actions & Ownership**
*   **No Pending Actions Identified:** All alerts listed in the log show a corresponding "Recovered" status before the end of the conversation window.
*   **Ownership:** The `team:dpd-pricing-cart` and `dept:dpd` are responsible for investigating root causes, though no tickets or comments were created in this channel.

**Decisions Made**
*   None recorded.

**Key Dates & Follow-ups**
*   **Date:** March 17, 2026 (UTC).
*   **Timeframe of Activity:** 05:55 UTC to 17:03 UTC.
*   **Follow-up Required:** While all alerts have recovered, the high frequency of latency spikes in `frontend-gateway` endpoints (specifically Wish List and Shopping List) suggests an intermittent performance issue requiring post-incident analysis by the Pricing Cart team.


## gchat/space/AAQAqwOWBZ4: Madhawa, Soumya, Tayza, Madhuri, ...
Source: gchat | Group: space/AAQAqwOWBZ4 | Last Activity: 2026-03-17T14:44:52.368000+00:00
**Daily Work Briefing Summary**

**Key Participants & Roles**
*   **Wai Ching Chan:** Announced arrival at a destination.
*   **Sundy Yaputra:** Inquired about specific location details and acknowledged receipt of information.
*   **Yangyu Wang:** Provided clarification regarding the location level and positioning relative to the mall.

**Main Topic/Discussion**
The conversation concerns the real-time location status of an arrival event, specifically clarifying which floor or area corresponds to "level 1" versus "level 2" and whether the location is inside or outside the mall structure.

**Decisions Made**
*   Confirmed that the arrival point is located **outside of the mall**.
*   Verified that the specific location corresponds to **Level 1**.

**Pending Actions & Ownership**
*   No explicit pending actions, tasks, or assignments were identified in this thread. The discussion concluded with Sundy Yaputra acknowledging the information ("Thx").

**Key Dates & Follow-ups**
*   **Date:** March 17, 2026.
*   **Timeline:**
    *   Arrival confirmed at 10:03 AM UTC.
    *   Location clarification completed by 10:12 AM UTC.
*   **Next Steps:** None currently indicated in the chat log.

**Metadata Reference**
*   **Space URL:** https://chat.google.com/space/AAQAqwOWBZ4
*   **Total Messages Analyzed:** 5


## gchat/space/AAAAnlKPglA: #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Last Activity: 2026-03-17T14:43:26.661000+00:00
**Daily Work Briefing: #dd-fpg-watchdog-alert**

**Key Participants & Roles**
*   **Datadog App (Automated Bot):** Primary sender of P3 alert notifications regarding infrastructure watchdog incidents. No human participants are currently visible in the provided chat log; no manual intervention or discussion has occurred yet.

**Main Topic**
The channel is monitoring automated "DPD Watchdog" events for production infrastructure. The alerts indicate system instability where Datadog detects specific infrastructure stories recurring over 30-minute windows. All incidents are classified as **P3 (Low Priority)** but have triggered repeated cycles of [Triggered] and [Recovered] states within a short timeframe.

**Incident Timeline & Status**
Three distinct incident groups were identified based on `story_key`:

1.  **Group A (`story_key: ed1a5b57...`)**
    *   **Trigger:** 2026-03-16 07:43 UTC
    *   **Recovery:** 2026-03-16 10:37 UTC (Duration: ~3 hours)
    *   **Status:** Resolved.

2.  **Group B (`story_key: 9ec650c5...`)**
    *   **Trigger:** 2026-03-17 09:29 UTC (Note: "An additional 1 events also triggered this monitor")
    *   **Recovery:** 2026-03-17 12:00 UTC (Duration: ~2.5 hours)
    *   **Status:** Resolved.

3.  **Group C (`story_key: e40567bb...`)**
    *   **Trigger:** 2026-03-17 14:43 UTC
    *   **Recovery:** None reported as of the last log entry.
    *   **Status:** **Active/Open**.

**Pending Actions & Ownership**
*   **Action:** Investigate the active incident (Group C, `story_key: e40567bb-115b-5b81-be58-09d665e5969f`) triggered on 2026-03-17 at 14:43 UTC.
*   **Owner:** Unassigned in chat log; implied ownership lies with the Infrastructure or SRE team monitoring this channel.
*   **Context:** The monitor query excludes `tcp_retrans_jump` and `full_disk_forecast`, suggesting the issue relates to other infrastructure watchdog stories (e.g., service health, connectivity).

**Decisions Made**
No human decisions, discussions, or resolutions were recorded in the provided conversation history. All status changes were automated via Datadog.

**Key Dates & Follow-ups**
*   **Critical Date:** 2026-03-17 (Current active incident date).
*   **Next Step:** Review the latest Datadog monitor link for Group C to determine the root cause of the recurring infrastructure watchdog triggers.
*   **Monitoring:** Continue observing `story_key: e40567bb...` until a [Recovered] status is received.

**References**
*   Monitor ID: 17447511
*   Space URL: https://chat.google.com/space/AAAAnlKPglA
*   Active Incident Link: https://app.datadoghq.eu/monitors/17447511?group=story_key%3Ae40567bb-115b-5b81-be58-09d665e5969f


## gchat/space/AAAAx50IkHw: Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw | Last Activity: 2026-03-17T12:12:53.733000+00:00
**Daily Work Briefing: Digital Product Development (DPD) Space**

**Key Participants & Roles**
*   **Kyle Nguyen:** Announcer/Contributor.
*   **Wai Ching Chan:** Participant/Responder.
*   **Vincent Wei Teck Lim:** Mentioned in reply thread; likely attendee or participant.

**Main Topic/Discussion**
The conversation centered on an upcoming team event: the **DPD BBQ**. Kyle Nguyen initiated the discussion with a confirmation message stating, "We come first," signaling attendance and priority for the event. Wai Ching Chan responded with a brief expression of enthusiasm ("wow"). The thread also indicates that Vincent Wei Teck Lim is being tagged or referenced regarding this topic in a follow-up reply.

**Pending Actions & Ownership**
*   **Action:** No specific action items were assigned in the provided text.
*   **Ownership:** Not applicable based on current content.

**Decisions Made**
*   **Event Confirmation:** The team has implicitly confirmed attendance for the DPD BBQ, as indicated by Kyle Nguyen's statement "We come first."

**Key Dates & Follow-ups**
*   **Event Date:** March 17, 2026 (Current date of conversation).
*   **Timeframes:**
    *   Initial announcement: 10:03 AM UTC.
    *   Response/Engagement: 12:12 PM UTC.
    *   Last activity noted: 12:15 PM UTC.
*   **Follow-up Status:** The conversation thread remains active with "1 unread" message involving Wai Ching Chan and a reply directed at Vincent Wei Teck Lim as of the last update (12:15 PM).

**Metadata Reference**
*   **Resource:** Digital Product Development {DPD}
*   **Space URL:** https://chat.google.com/space/AAAAx50IkHw
*   **Total Messages Reviewed:** 2


## gchat/dm/62iuUSAAAAE: Yaxin Hao
Source: gchat | Group: dm/62iuUSAAAAE | Last Activity: 2026-03-17T09:57:08.515000+00:00
**Daily Work Briefing: Google Chat Summary**

**Resource:** Yaxin Hao
**Conversation URL:** https://chat.google.com/dm/62iuUSAAAAE
**Date Range:** March 17, 2026 (09:56 – 09:57 UTC)

### **Key Participants & Roles**
*   **Yaxin Hao:** Initiator of the inquiry regarding location/meeting availability.
*   **Michael Bui:** Respondent; currently engaged in an offline event.

### **Main Topic**
The discussion concerned a potential physical meeting or visit to location **"L10"** scheduled for March 17, 2026. Yaxin Hao inquired about Michael Bui's availability to attend this location.

### **Decisions Made**
*   **Meeting Status:** The proposed meeting at L10 on March 17, 2026, was **cancelled/noted as not occurring**.
*   **Reasoning:** Michael Bui confirmed he has an existing commitment to an "offline event" at the time of inquiry.

### **Pending Actions**
*   **No specific new action items were generated** in this thread based on the provided transcript. The conversation concluded with a refusal/confirmation of unavailability rather than a reschedule or delegation.

### **Key Dates & Follow-ups**
*   **Date:** March 17, 2026.
*   **Timeframe:** 09:56 UTC to 09:57 UTC.
*   **Follow-up Required:** None explicitly stated in the text. No new time or date was proposed for rescheduling L10.

### **Summary of Chronology**
1.  **09:56:16 UTC:** Yaxin Hao asked, "Will you come down L10?"
2.  **09:57:08 UTC:** Michael Bui responded, "Not today, I'm going to have an offline event now."


## gchat/space/AAQACfHCuNI: BCRS - UAT
Source: gchat | Group: space/AAQACfHCuNI | Last Activity: 2026-03-17T09:48:50.185000+00:00
**Daily Work Briefing: BCRS - UAT Space**

**Key Participants & Roles**
*   **Danielle Lee:** Inquired about the updated technical live date and production release status regarding Feature Flag (FF) toggling.
*   **Prajney Sribhashyam:** Tagged for clarification on the live date; no response recorded in this thread.
*   **Sathya Murthy Karthik:** Provided the official UAT update summary for March 17, 2026.
*   **Finance Team:** Tasked with verifying specific test cases and marking status.

**Main Topic**
Status of User Acceptance Testing (UAT) for the BCRS project as of March 17, 2026, at 5:45 PM, covering Returns & Refunds, Customer Service (CS), Finance, and In-store Pre-order modules.

**Pending Actions & Ownership**
*   **Retest Delivery/Cancellation Cases:** Re-test "Re-delivery" and "manual cancellation after delivery" test cases for Returns & Refunds. *Owner: Testing Team.*
*   **Finance Verification:** Verify all sales posting, invoice, and credit note number updates in the test sheet. The Finance team must mark these statuses accordingly. *Owner: Finance Team.*
*   **Pre-order Clarification & Retest:** Address clarification for 14 pending In-store Pre-order test cases following an issue report regarding FOC BCRS deposit not being charged. *Owner: Testing Team.*

**Decisions Made**
*   No final decision on the technical live date or production release status was established in this thread; Danielle Lee's query regarding the "9 March" adoption benchmark remains open pending clarification from Prajney Sribhashyam.

**Key Dates & Follow-ups**
*   **Report Date:** March 17, 2026 (5:45 PM).
*   **Reference Date:** March 9, 2026 (cited by Danielle Lee regarding app update adoption and FF status).
*   **Next Steps:** Completion of finance verification and re-testing of pending cases before the next UAT cycle.


## gchat/space/AAQAUJW8HMo: ❗ Important Email
Source: gchat | Group: space/AAQAUJW8HMo | Last Activity: 2026-03-17T09:24:58.263000+00:00
**Daily Work Briefing Summary**

**Key Participants & Roles**
*   **Michael Bui:** Recipient/Subject of briefings; attendee in meetings.
*   **Alvin Choo:** Meeting organizer (Performance Feedback).
*   **Trina Boquiren:** Event organizer (Team BBQ); IT Security Reminder sender.
*   **Bryan Choong:** Unavailable team lead regarding OSMOS support issues.
*   **HR Advisory Team / HR BP:** Support for Performance Management.
*   **Geek Squad:** Service providers for MacBook encryption setup.
*   **OB Sensory Team:** Organizers of the Chapati sensory recruitment.

**Main Topics**
1.  **Mandatory Compliance & Deadlines:** FY2025 Performance Management closing and critical MacBook FileVault encryption requirements to close security audit gaps.
2.  **Team Events:** A farewell BBQ dinner for the DPD team and a recruitment drive for the OB Sensory Team.
3.  **Meeting Scheduling:** Upcoming performance feedback session.
4.  **Support Status:** Out-of-office notification regarding OSMOS support inquiries.

**Pending Actions & Ownership**
*   **RSVP to Meeting:** You must reply "Yes" to Alvin Choo's calendar invitation for the performance feedback meeting. (Owner: You)
*   **Accept BBQ Invitation:** Must accept the DPD team BBQ invite by EOD Monday, 16 March, to allow food pre-ordering. (Owner: You)
*   **MacBook Security Protocol:**
    *   Book a FileVault appointment via the calendar by **March 28**.
    *   Backup files to Google Drive prior to arrival.
    *   Bring MacBook to Geek Squad (FP Hub Level 15, 9 AM–5 PM) for setup between March 20–28. (Owner: You/DPD Users)
*   **Performance Management:**
    *   Managers must click "Send to Staff for Conversation" in MyHR. (Owner: Managers)
    *   Employees must sign off electronically on MyHR after discussions. (Owner: All Eligible Staff)

**Decisions Made**
*   No new decisions recorded; actions are based on mandatory policy updates and scheduled invitations. The OSMOS support query was deferred due to the recipient's leave status.

**Key Dates, Deadlines & Follow-ups**
*   **March 17, 2026 (Today):** DPD Team BBQ dinner from 6:00 PM–9:00 PM at BBQ Box, Jurong Point. Depart Lobby A at 5:45 PM for train to Boon Lay Station.
*   **March 18, 2026:** Performance Feedback "1 on 1" with Alvin Choo and Winson Lim from 4:00 PM–4:30 PM (SGT).
*   **March 28, 2026:** Internal deadline for DPD users to register MacBook for FileVault encryption.
*   **March 31, 2026:** Final deadline for FY2025 Performance Management sign-offs and full MacBook FileVault compliance (non-compliance risks restricted access).
*   **March 9–20, 2026:** Bryan Choong is on leave.
*   **March 24, 2026:** Bryan Choong returns; OSMOS support follow-up to occur then.

**Support Contacts**
*   HR Advisory Team or HR Business Partner for Performance Management questions.
*   Maeves Goh or Geek Squad Level 15 for FileVault issues.


## gchat/dm/t3wf6EAAAAE: Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Last Activity: 2026-03-17T09:20:39.851000+00:00
**Daily Work Briefing Summary**
**Resource:** Nikhil Grover | **Date:** March 17, 2026

### Key Participants & Roles
*   **Nikhil Grover:** Product/Project Owner (Requester for status updates, metrics, and feature clarification).
*   **Michael Bui:** Technical Lead/Engineer (Provided technical assessment of ads implementation, swimlane logic, and service architecture).

### Main Topic
Technical alignment on enabling product ads for "vertical scrolling" and additional "swimlanes" under the Product Ads Epic (specifically tickets DPD-733 and DPD-734) ahead of an upcoming Monday go-live. The discussion focused on whether new development was required, effort estimation changes, and service architecture details.

### Decisions Made
*   **No New Development Required:** Michael confirmed that vertical scrolling ads can utilize the existing API and solution logic used for dynamic slots; no new code is needed to enable ads in vertical scroll or split swimlanes.
*   **Effort Unchanged:** Since no new development is required, Nikhil will not update effort estimates for tickets DPD-733 and DPD-734.
*   **UAT Scope:** Michael agreed that User Acceptance Testing (UAT) must cover both the new swimlane names and vertical scrolling functionality simultaneously.
*   **Service Architecture Clarification:** It was clarified that ads are fetched via `marketing-service` (not `ad-service`) using `placementName` instead of `page_name`. OMNI Home is controlled by the Layout Service, while OG Home is controlled by the Website Service.

### Pending Actions & Owners
| Action Item | Owner | Details/Context |
| :--- | :--- | :--- |
| **Confirm Service Ownership** | Nikhil Grover | Verify if the "orchestrator service" controls OMNI home or if it was replaced by the layout service (Nikhil noted uncertainty regarding a November change). |
| **Enable Feature Flags** | [TBD/Flora's Team] | Turn on feature flags for all swimlanes and vertical scroll on OMNI Home. Note: This is a code change, not a Split.io flag. |
| **Verify UAT Coverage** | Michael Bui | Ensure UAT scripts explicitly test both swimlane names and vertical scrolling ads before the Monday deadline. |
| **Check Swimlane Logic** | Michael Bui | Investigate if OMNI Home can support swimlane names for "OMNI home" specifically, noting constraints between OG Home (known swimlane) and OMNI Home (unknown swimlane). |

### Key Dates & Deadlines
*   **Monday, March 23, 2026:** Target go-live date for vertical scrolling ads and the split swimlanes. Nikhil requested earlier delivery to generate clear metrics.
*   **Tomorrow (March 18):** Presentation on "RMN: Display Campaign Transition" is scheduled; slides were updated by Nikhil Grover for reference.

### Specific References
*   **Jira Tickets:** DPD-733, DPD-734 (Status currently "yet to start"; pending discussion with Daryl/Flora).
*   **Epic:** Product Ads Epic.
*   **Services/Terms:** `marketing-service`, `osmos`, `Split.IO`, OMNI Home vs. OG Home, Vertical Scrolling, Swimlanes.
*   **Stakeholders:** Daryl, Flora (Feature flag owner), Nikhil Grover, Michael Bui.


## gchat/space/AAAAQuMQ3Bs: Omni Fairmily
Source: gchat | Group: space/AAAAQuMQ3Bs | Last Activity: 2026-03-17T08:04:44.451000+00:00
**Daily Work Briefing: Omni Fairmily Space**

**Key Participants & Roles**
*   **Christine Yap Ee Ling:** Initiator of the participant recruitment drive; coordinates with Sriharsh.
*   **Sriharsh:** Co-confirmer for user research slots alongside Christine.
*   **Pauline Tan:** Reported on FPG ADvantage team activities at the FairPrice Partners' Excellence Awards.
*   **Recognized Team Members (FPG ADvantage):** Rajiv Kumar Singh, Christopher Yong, Wendi Koh, Karlie Sia, Allen Umali, Pamela Koh, Serene Tan Si Lin, Neo Seng Ka (acknowledged for their contributions to the awards event).

**Main Topic/Discussion**
1.  **User Research Recruitment:** Christine requested assistance in sourcing non-FPG staff friends/family for a *Project Light* (FPG app) usability test. The focus is on recruiting eligible users via WhatsApp/Telegram distribution.
2.  **Event Recap:** Pauline highlighted the FPG ADvantage team's showcase of retail media solutions at the FairPrice Partners' Excellence Awards, specifically noting the presentation of the "Most Outstanding Omnichannel Partner" recognition and engagement at the booth.

**Pending Actions & Ownership**
*   **Recruitment Execution:** Forward the provided recruitment message to trusted social circles (Christine Yap Ee Ling).
*   **Slot Confirmation:** Confirm participant slots within 2 working days upon booking (Sriharsh or Christine Yap Ee Ling).
*   **Event Follow-up:** Continue engagement on the awards event thread (5 replies noted in chat).

**Decisions Made**
*   No explicit strategic decisions were recorded; the conversation focused on operational requests and informational sharing.

**Key Dates & Deadlines**
*   **Usability Test Sessions:** March 25, 26, and 27, 2026 (Wed–Fri).
    *   Available Slots: 12:00 PM and 1:15 PM.
    *   Format: Online (Google Meet) or In-person (FairPrice Hub, Joo Koon, Level 12).
*   **Booking Link:** https://calendar.app.google/Lfaoj8r4Ewc3FAPv6
*   **Token of Appreciation:** $10 vouchers for online; $20 vouchers for in-person.
*   **Participant Eligibility Timeline:** Must have personally ordered online grocery delivery within the past 3 months and not participated in FairPrice customer interviews in the past 6 months.
*   **Chat Timestamps:** March 16, 2026 (Recruitment request); March 17, 2026 (Event update).


## gchat/space/AAQAgT-LpYY: BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY | Last Activity: 2026-03-17T07:50:33.400000+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Onkar Bamane:** Initiator of status updates.
*   **Prajney Sribhashyam:** Leads UAT execution and coordination; requested technical support for testing and new field estimation.
*   **Sathya Murthy Karthik:** Provided initial deployment status update; inquired about SKU eligibility logic.
*   **Michael Bui:** Joined a Google Meet session to assist with testing; reported audio issues.
*   **Sneha Parab:** Subject matter expert consulted regarding timeline/effort for new field creation (Viewed by 22 of 37).

**Main Topic/Discussion**
The group focused on the deployment status of SAP changes for Marketplace (MP) SKU creation and change APIs, specifically concerning BCRS (Barnes & Noble Corporate Retail Services) items. Discussions included:
1.  **Deployment Status:** SAP changes were not yet deployed to production as of March 16 morning.
2.  **UAT Execution:** Prajney Sribhashyam confirmed UAT for MP SKU creation was underway on March 16.
3.  **Technical Testing:** A call was convened to test the "re-delivery flow" for BCRS items, where audio connectivity issues were reported by Michael Bui.
4.  **Data Inquiries:** Sathya Murthy Karthik sought clarification on whether a BCRS-eligible SKU with "DF" designation exists.
5.  **Feature Request:** Prajney requested an effort estimate and timeline for creating a new 'BCRS container count' field within the MP system.

**Pending Actions & Ownership**
*   **Action:** Complete UAT for MP SKU creation and provide confirmation to trigger business user sign-off.
    *   **Owner:** Prajney Sribhashyam (Done today, March 16).
*   **Action:** Share SAP UAT form with the corresponding business user for sign-off upon UAT closure.
    *   **Owner:** Sathya Murthy Karthik (Pending confirmation from Prajney).
*   **Action:** Provide effort and timeline estimation for creating a new 'BCRS container count' field.
    *   **Owner:** Sneha Parab (Requested March 17; awaiting response).

**Decisions Made**
No formal decisions were recorded in the chat log. The group acknowledged that production deployment is pending UAT completion.

**Key Dates & Follow-ups**
*   **March 16, 2026:**
    *   02:16 UTC: Status check initiated by Onkar Bamane.
    *   07:44 UTC: Google Meet call scheduled for re-delivery flow testing (Link: `meet.google.com/vtj-thbc-utk`).
    *   Morning: UAT for MP SKU creation conducted.
*   **March 17, 2026:**
    *   07:50 UTC: Formal request sent to Sneha Parab regarding the 'BCRS container count' field timeline.

**Notes**
*   A Google Meet session held on March 16 at 07:44 UTC experienced audio issues reported by Michael Bui.
*   The inquiry regarding "BCRS eligible + DF sku" generated significant discussion (7 replies) involving Sneha Parab.


## gchat/space/AAQApypQTVg: [Urgent] BCRS SAP Posting - Redelivery - Mar 17
Source: gchat | Group: space/AAQApypQTVg | Last Activity: 2026-03-17T07:48:00.805000+00:00
**Daily Briefing: BCRS SAP Posting Redelivery Issue**

**Key Participants & Roles:**
*   **Prajney Sribhashyam:** Project Lead/Initiator (driving the solution).
*   **Onkar Bamane:** Engineering/SAP Expert (CAB deployment, technical feasibility).
*   **Alvin Choo / Michael Bui:** Technical Architects (proposing RPA solutions).
*   **Yap Chye Soon Adrian:** Operations Lead (managing manual SAP postings).
*   **De Wei Tey / Hebin Huang:** Functional/Integration Experts (assessing RPA feasibility and DBP data integrity).
*   **Wai Ching Chan:** Order Services expert.

**Main Topic:**
Addressing a critical financial compliance issue where "Plan B" for re-deliveries causes duplicate BCRS deposit postings to SAP when orders transition from *Completed* → *Packed* → *Completed*. Approximately 70 cases occur monthly, requiring a fix to prevent double billing and ensure accurate financial reconciliation.

**Current Status & Decisions:**
*   **Problem Confirmed:** The current flow triggers duplicate BCRS entries for all items in every re-delivery scenario.
*   **Proposed Options Discussed:**
    1.  **DBP Differential Logic:** Maintain a 'BCRS deposit posted' status in DBP to post only incremental amounts (Architecturally preferred by Hebin Huang).
    2.  **SAP Consolidation:** Allow duplicates but configure SAP to recognize only the last entry as valid.
    3.  **Manual Posting:** Disable auto-posting for re-deliveries; require manual updates by Operations.
*   **RPA Feasibility Rejected (for now):** De Wei Tey confirmed current Zendesk fields lack required data for RPA, and automation would require significant build time. Mass end-of-month posting was deemed unviable as consolidation happens daily.

**Pending Actions & Owners:**
1.  **Architectural Review:** @Yap Chye Soon Adrian and @De Wei Tey to provide specific feasibility feedback on the DBP differential approach (Option 1) vs. SAP consolidation.
2.  **Cancellation Logic:** Prajney Sribhashyam to separately address how BCRS deposits are reversed when a completed order is cancelled by CS (a related risk identified by Adrian).
3.  **Follow-up Session:** A short meeting is scheduled to finalize the approach after technical inputs are received.

**Key Dates & Deadlines:**
*   **Urgency:** High (identified as urgent on Mar 17).
*   **Meeting Scheduled:** Discussion occurred on Mar 17, 2026, at ~03:02 UTC; follow-up to close the decision pending.
*   **Reference Metadata:** Chat Space URL provided for full context.


## gchat/space/AAAAs0DTvmA: [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Last Activity: 2026-03-17T07:45:08.084000+00:00
**Daily Work Briefing: [Prod Support] Marketplace**

**Key Participants & Roles**
*   **Charlene Tan:** Seller/Fulfillment Partner (Reports email picklist issues, error under "offers").
*   **Amos Lam:** Operations/Support Lead (Inquires about order completion triggers and picklist generation logic).
*   **Lalita Phichagonakasit:** Support/Operations (Investigates product listing visibility for specific postal codes).
*   **Dang Hung Cuong:** Primary Technical Owner (Tagged in all inquiries; appears to be the central point of contact for troubleshooting).
*   **Shiva Kumar Yalagunda Bas & Cassandra Thoi:** Secondary stakeholders consulted on order status and logic queries.

**Main Topics Discussed**
1.  **Picklist Delivery Failure:** Charlene Tan is not receiving "Final Picklists" for Estalife (PFC), despite receiving other email picklists.
2.  **Order Status Anomalies:** Amos Lam needs to understand why orders #246974265 and #248270820 triggered a "Completed" status without delivery by NJV.
3.  **Product Visibility:** Lalita Phichagonakasit reports item #13226899 is missing from search results for postal code 762115, affecting customer reorders.
4.  **Seller System Error:** Charlene Tan flagged a specific error under the "offers" section within her new seller "woah group."
5.  **Process Logic Verification:** Amos Lam questioned the system logic regarding picklist generation when orders are postponed (e.g., original date March 3 vs. rescheduled to March 15).

**Pending Actions & Ownership**
*   **Investigate Picklist Missing Data:** Check why Estalife is not receiving Final Picklists for PFC. *(Owner: Dang Hung Cuong)*
*   **Audit Order Completion Triggers:** Determine cause of "Completed" status for orders #246974265 and #248270820 without NJV delivery. *(Owner: Dang Hung Cuong, Shiva Kumar Yalagunda Bas, Cassandra Thoi)*
*   **Resolve Search Visibility Issue:** Investigate why item #13226899 is not appearing for postal code 762115. *(Owner: Dang Hung Cuong)*
*   **Diagnose "Offers" Error:** Analyze the error occurring in Charlene Tan's new seller group under "offers." *(Owner: Dang Hung Cuong)*
*   **Clarify Postponement Logic:** Confirm if picklists are automatically adjusted when orders are rescheduled from March 3 to March 15. *(Owner: Dang Hung Cuong, Shiva Kumar Yalagunda Bas)*

**Decisions Made**
*   No formal decisions recorded; all threads remain open for technical investigation.

**Key Dates & Follow-ups**
*   **March 16, 2026:** Initial reports regarding Estalife picklists and order completion anomalies.
*   **March 17, 2026 (Morning):** Reports on item #13226895 visibility and "offers" errors.
*   **Current Status:** All threads remain active with recent replies noted as of "Yesterday" or "12 min" ago relative to the briefing time.
*   **Reference Links:** FairPrice search query for item #13226899; Space URL: https://chat.google.com/space/AAAAs0DTvmA


## gchat/space/AAQA85dw4So: RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Last Activity: 2026-03-17T06:43:13.471000+00:00
**Daily Work Briefing: RMN Notification Automation Logs**

**Key Participants & Roles**
*   **Automated Collection Runner:** Primary actor. An automated CI/CD bot executing test suites and reporting results to the "RMN Notification" Google Chat space.
*   **Webhook Bot:** Secondary component mentioned repeatedly; currently failing to process request notifications, though this does not appear to halt the test execution itself.
*   **Human Participants:** None identified in the provided log segment (purely automated system logs).

**Main Topic/Discussion**
The conversation consists entirely of automated post-execution summaries for API and API Contract tests running against the `staging` environment across three distinct services:
1.  `marketing-service`
2.  `promo-service`
3.  `marketing-personalization-service`

Executions occurred on **March 16, 2026**, and **March 17, 2026**. The logs indicate a recurring pattern of nightly or scheduled runs.

**Failures & Anomalies**
*   **System Limitation:** Every single message includes the error: *"Webhook Bot is unable to process your request."* This suggests an integration issue preventing detailed report links from being fully processed by the chat bot, though "View Report" links are still generated in the text.
*   **Test Failures (Critical):** The `marketing-service` API tests recorded consistent failures on March 17:
    *   **03:15 UTC:** 2 Failed out of 50 Passed.
    *   **06:43 UTC:** 2 Failed out of 51 Passed.
    *   *Note:* On March 16, the same service passed all 51 tests with 0 failures.
*   **Stable Services:** `promo-service` and `marketing-personalization-service` maintained 100% pass rates across all observed runs on both dates.

**Pending Actions**
*   **Investigate `marketing-service` Regressions:** The engineering team must identify the root cause of the 2 failing API tests in `marketing-service` that appeared on March 17 but were absent on March 16.
*   **Fix Webhook Integration:** The "Webhook Bot is unable to process your request" error requires resolution by the DevOps or Platform Engineering team to ensure full report functionality.

**Ownership**
*   **Test Failures:** Owned by the `marketing-service` Development Team.
*   **Webhook Errors:** Owned by the Infrastructure/DevOps Team managing the Collection Runner integration.

**Decisions Made**
No human decisions were recorded in this log segment, as no manual discussion occurred.

**Key Dates & Follow-ups**
*   **Last Run (Failure):** March 17, 2026, at 06:43:13 UTC (`marketing-service` API Tests).
*   **Previous Clean Run:** March 16, 2026, at 01:05:16 UTC.
*   **Next Scheduled Follow-up:** Immediate investigation required before the next daily run to prevent regression carry-over.


## gchat/space/AAQAXn1ocmE: Retail out of home (Digital Screens & CMS)
Source: gchat | Group: space/AAQAXn1ocmE | Last Activity: 2026-03-17T06:26:40.752000+00:00
**Daily Work Briefing: Retail Out of Home (Digital Screens & CMS)**

**Meeting Resource:** Google Chat Space  
**URL:** https://chat.google.com/space/AAQAXn1ocmE  
**Date of Activity:** March 17, 2026  

### Key Participants
*   **David Anura Cooray:** Initiator of the discussion regarding PDD Gondola End Large TVs.

### Main Topic
The conversation focuses on specifications or requirements for **"PDD Gondola End Large TVs"** within the Retail Out of Home resource category (Digital Screens & CMS). The thread generated 2 replies and remained active as of 6:31 AM UTC. Note: The provided content snippet does not include the text of the replies, only the metadata indicating activity occurred.

### Pending Actions
*   **Status:** Unable to determine specific pending actions or ownership from the provided summary snippet. The input data confirms a discussion took place but lacks the substance of the 2 replies to assign tasks.
*   **Recommendation:** Review the full chat log for the two replies to extract action items and assign owners.

### Decisions Made
*   No specific decisions are visible in the provided text excerpt. Confirmation of any agreements or technical specifications requires access to the body of the messages replied by other participants.

### Key Dates & Follow-ups
*   **Initiation:** March 17, 2026, at 06:26:40 UTC (David Anura Cooray).
*   **Last Activity:** March 17, 2026, at 06:31 AM UTC.
*   **Unread Status:** The thread currently shows **2 unread** messages as of the last update.

### Summary Notes
The briefing is based on a single message entry from David Anura Cooray initiated at 06:26:40 UTC. While the topic "PDD Gondola End Large TVs" indicates a focus on specific hardware deployment or configuration, the lack of reply content in this summary prevents further granularity regarding technical requirements, timelines, or stakeholder consensus. Immediate follow-up requires opening the chat link to read the two replies generated between 06:26 AM and 06:31 AM.


## gchat/space/AAAAS7vPcKs: QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs | Last Activity: 2026-03-17T06:24:43.924000+00:00
**Daily Work Briefing: Resource QE <-> All Tribes**

**Key Participants & Roles**
*   **Madhuri Nalamothu:** Identified a data inconsistency regarding DC (Digital Club) user membership status.
*   **Milind Badame:** Reported UI alignment issues on the cart page and queried about specific view buttons.
*   **Andin Eswarlal Rajesh:** Tagged regarding cart page view buttons.
*   **Tayza Htoon & Pandi:** Tagged by Madhuri regarding a subscription error issue.

**Main Topic/Discussion**
1.  **DC Membership Data Inconsistency (Madhuri Nalamothu):** A discrepancy exists where specific DC users show the "DC member" flag in the back office but are not receiving Digital Club awards based on LPs (Last Purchase) and lack an active digital membership plan (Monthly or Annual) in the Account -> Digital Club membership UI. Attempts to subscribe via the UI result in a critical error.
2.  **Cart Page UI Defects (Milind Badame):** The cart page displays broken alignment for highlighted products, specifically noting misalignment on the third product and confusion regarding unidentified "view buttons."

**Pending Actions & Ownership**
*   **Investigate DC Membership Logic:** Resolve the flag vs. LP/Award discrepancy and fix the subscription error preventing users from upgrading to a plan.
    *   *Owners:* **Tayza Htoon**, **Pandi**.
*   **Fix Cart Page UI:** Correct alignment issues for highlighted products (specifically the 3rd item) and define/clarify the function of unknown view buttons.
    *   *Owner:* **Andin Eswarlal Rajesh** (implied via tagging).

**Decisions Made**
*   No formal decisions recorded in this thread; discussions are currently focused on issue identification and initial triage.

**Key Dates & Follow-ups**
*   **2026-03-16:** Issue regarding DC member flags and subscription errors identified. Last reply noted "Yesterday 10:54 AM" (relative to the snapshot).
*   **2026-03-17:** UI alignment issues reported at 06:23 UTC. Follow-up replies occurred as late as 06:33 AM on the same day.
*   **Status:** Both threads show active engagement with multiple replies, though specific resolution deadlines were not explicitly set in the provided text.


## gchat/space/AAAAhWLveDE: FP x Mirakl
Source: gchat | Group: space/AAAAhWLveDE | Last Activity: 2026-03-17T06:16:17.058000+00:00
**Daily Work Briefing: FP x Mirakl Resource**

**Key Participants & Roles**
*   **Dang Hung Cuong:** Initiator of the discussion regarding API constraints.
*   **Intrepid:** Third-party integrator working with multiple sellers; source of the rate limit inquiry.
*   **Cheryl Jones:** Tagged participant for follow-up.
*   **LyLy Lim:** Tagged participant for follow-up.

**Main Topic**
Discussion centers on a request from Intrepid to increase the Mirakl API rate limiter thresholds. Currently, the integrator faces a limit of one request per minute for APIs they are monitoring across multiple sellers, which is causing friction. The team is evaluating the feasibility of raising these limits.

**Pending Actions & Ownership**
*   **Review/Response Required:** Cheryl Jones and LyLy Lim have been tagged regarding this inquiry (5 replies noted in thread). They need to address whether increasing the rate limit is technically feasible or operationally viable.
*   **Status:** Awaiting input from the tagged stakeholders to determine next steps with Intrepid.

**Decisions Made**
No final decisions were recorded in the provided snippet. The conversation remains an open inquiry pending response from Cheryl Jones and LyLy Lim.

**Key Dates & Deadlines**
*   **Discussion Start:** March 17, 2026, at 06:16 AM UTC.
*   **Last Activity:** March 17, 2026, at 06:40 AM UTC (5 unread replies remaining as of the last update).
*   **Follow-up:** Immediate attention required to clear the 5 unread replies and respond to Intrepid's request regarding API thresholds.


## gchat/space/AAQAeSWRtgQ/RZyBk6LBi14: Video & Product Ads Working Group
Source: gchat | Group: space/AAQAeSWRtgQ/RZyBk6LBi14 | Last Activity: 2026-03-17T06:11:57.822000+00:00
**Daily Work Briefing: Video & Product Ads Working Group**

**Key Participants**
*   **Michael Bui:** Initiator of the discussion; focused on implementation logic for dynamic ad positioning.
*   **Norman Goh:** Validated technical approach and raised concerns regarding testing coverage and historical UAT results.
*   **Nikhil Grover:** Mentioned as a stakeholder (CC'd) but did not contribute to this specific thread.

**Main Topic**
The group discussed the API usage and positioning logic for Product Ads within vertical scrolling compared to product swimlanes. The core objective was to confirm that ad positions remain dynamic, driven by **Split.IO** feature flags rather than hardcoded values, ensuring consistency across both layout types.

**Decisions Made**
*   **API Strategy:** Confirmed that the same product ads endpoint used for product swimlanes should be utilized for vertical scrolling.
*   **Logic Implementation:** No hardcoding of position values will occur. Positioning is to be controlled dynamically via Split.IO feature flags.
*   **Service Architecture:** The logic for Split.IO is managed entirely within the `marketing-service`. Upstream services are instructed to rely solely on the response data from `marketing-service` without needing direct interaction with Split.IO.

**Pending Actions & Ownership**
*   **Testing Verification (UAT):** Norman Goh noted that dynamic positioning via Split.IO should have been validated during previous User Acceptance Testing (UAT). He suggested that if this represents a new implementation or change, a re-verification or additional UAT cycle might be required to ensure current expectations are met.
    *   *Owner:* To be confirmed by the testing/QA team based on Norman's recommendation.
*   **Clarification of Scope:** Michael Bui clarified that the scope is limited to ensuring `marketing-service` outputs correct data, implying no changes are needed for upstream service logic.

**Key Dates & Follow-ups**
*   **Date of Conversation:** March 17, 2026 (05:57 – 06:11 UTC).
*   **Follow-up Required:** Confirmation on whether a new UAT cycle is necessary for the Split.IO integration in vertical scrolling, given Norman's concern that this specific behavior was not explicitly controlled or tested previously.

**References**
*   **Link:** https://chat.google.com/space/AAQAeSWRtgQ
*   **Tooling:** Split.IO (Feature Flags), Marketing-service.


## gchat/space/AAQAHH3dAYc: [D&T] Discussion service account key decommission
Source: gchat | Group: space/AAQAHH3dAYc | Last Activity: 2026-03-17T06:04:11.211000+00:00
**Daily Work Briefing: [D&T] Service Account Key Decommission**

**Key Participants & Roles**
*   **Himal Hewagamage:** Security Lead/Owner; driving the initiative to strengthen GCP security and manage service account key rotation.
*   **Nicholas Tan:** Identified specific project status ("Dpd has been defunct") and team affiliation ("D&T").
*   **Michael Bui:** Participant seeking clarification on the action plan and current usage status of keys.

**Main Topic**
The discussion centers on a security initiative to decommission duplicate and unused Google Cloud Platform (GCP) service account keys and onboard remaining accounts into an automated key rotation policy. The goal is to remove outdated credentials as part of security best practices.

**Pending Actions & Ownership**
*   **Application Pipeline Verification:** Team leads must confirm which identified service account keys are currently active in their application pipelines. *Owner: Application Owners/Leads.*
*   **Non-Rotated Account Identification:** For accounts not yet onboarded to automated rotation, the specific G Suite group name must be provided so new keys can be securely shared and included in the process. *Owner: Team Leads/Owners.*
*   **Action Plan Clarification:** Michael Bui requested a detailed brief on whether identified keys are unused or manually rotated (e.g., quarterly via email). A response from Himal Hewagamage is pending to address this query.

**Decisions Made**
*   It was confirmed that the project "Dpd" has been defunct.
*   The team will utilize a shared spreadsheet to track Service Account (SA) details: *[GCP][Security] Service Account Key Rotation & Decommission*.
    *   **Link:** https://docs.google.com/spreadsheets/d/1mGBCTRQDcTs0z_w0LjVtywDCtFHZhZfWYIRGqcNglpQ/edit?gid=0#gid=0

**Key Dates & Follow-ups**
*   **March 16, 2026 (07:43 UTC):** Initiation of the decommissioning process and request for confirmation on key usage.
*   **March 16, 2026 (07:45 UTC):** Distribution of the tracking spreadsheet by Himal Hewagamage.
*   **March 17, 2026 (06:04 UTC):** Michael Bui raised a follow-up question regarding the specific rotation mechanism and usage status of the keys listed in the document.

No explicit deadline was set for the response to Michael's query or the completion of the key verification; however, immediate action is implied by the security context.


## gchat/space/AAQAN8mDauE/ewxUvQHmSUM: [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/ewxUvQHmSUM | Last Activity: 2026-03-17T06:01:17.864000+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Gopalakrishna Dhulipati:** Initiator of the task; responsible for assigning ownership and managing access.
*   **Sneha Parab:** Service Lead participant; required access to the dedicated workspace but initially lacked permissions.
*   **Michael Bui:** Service Lead participant; required access to the dedicated workspace but initially lacked permissions.
*   **Rajesh:** Participant identified by Gopalakrishna as not requiring addition to the space (skipped).

**Main Topic/Discussion**
The conversation concerns a **Service Key Rotation** initiative involving collaboration with the SRE team. The discussion focused on granting necessary access to the Google Chat room dedicated to this topic for the involved leads.

**Pending Actions & Ownership**
*   **Action:** No immediate pending actions remain regarding access, as Gopalakrishna confirmed membership updates were completed. However, the primary work item remains:
    *   **Task:** Lead the Service Key Rotation topic with SRE.
    *   **Owner:** Sneha Parab and Michael Bui (assigned by Gopalakrishna).

**Decisions Made**
*   **Access Management:** Only Sneha Parab and Michael Bui were granted access to the specific Google Chat room regarding key rotation. Rajesh was explicitly excluded from this space based on assessment that his involvement was not required ("Rajesh can skip so didnt add").

**Key Dates & Follow-ups**
*   **2026-03-16 12:18 UTC:** Gopalakrishna Dhulipati assigned the task and shared the room link (`https://chat.google.com/room/AAQAHH3dAYc/0wjfMpKmFVI/0wjfMpKmFVI`).
*   **2026-03-17 06:00 UTC:** Sneha Parab and Michael Bui reported lack of access.
*   **2026-03-17 06:01 UTC:** Gopalakrishna confirmed adding the two users to the space.

**Reference Links**
*   Main Space URL: `https://chat.google.com/space/AAQAN8mDauE`
*   Specific Task Room: `https://chat.google.com/room/AAQAHH3dAYc/0wjfMpKmFVI/0wjfMpKmFVI`


## gchat/space/AAQAeSWRtgQ: Video & Product Ads Working Group
Source: gchat | Group: space/AAQAeSWRtgQ | Last Activity: 2026-03-17T05:57:47.364000+00:00
**Daily Work Briefing: Video & Product Ads Working Group**

**Key Participants & Roles**
*   **Michael Bui:** Raised technical inquiries regarding ad position data discrepancies and API usage for vertical scrolling.
*   **Norman Goh:** Tagged in discussions; noted as the last responder to both threads.
*   **Flora Wo Ke:** Tagged in the initial discussion thread.
*   **Nikhil Grover:** Tagged in the initial discussion thread context.

**Main Topic & Discussion**
The conversation focused on data inconsistencies and implementation details regarding product ad positions:
1.  **Data Discrepancy (March 16):** Michael Bui highlighted a mismatch where the UI displayed ad positions as `(1, 3)`, while the Marketing Service API response returned positions `(2, 5)` for specific SKUs (`90175183` and `90175149`). He requested clarification on the source of these position values.
2.  **API Implementation (March 17):** Michael Bui inquired about the specific API used to fetch product ads during vertical scrolling. He specifically asked whether the system currently relies on the `position` values returned by the API response or if these values are hardcoded.

**Pending Actions & Ownership**
*   **Clarify Position Logic:** The team must explain why UI positions differ from Marketing Service API positions (Thread 1: 32 replies).
    *   *Status:* Unresolved; discussion concluded with Norman Goh and Flora Wo Ke as last responders.
*   **Confirm Vertical Scroll Implementation:** Determine the specific API used for vertical scrolling product ads and verify if position values are dynamic (from API) or static (hardcoded).
    *   *Status:* Awaiting response; discussion thread closed by Norman Goh at 6:11 AM on March 17.

**Decisions Made**
*   No final decisions were recorded in the provided text snippets. The conversation remains inquiry-based, seeking confirmation on data sources and implementation logic.

**Key Dates & Follow-ups**
*   **March 16, 2026 (07:03 AM):** Initial query sent regarding position mismatch `(1,3)` vs `(2,5)`. Thread generated 32 replies; last reply recorded at 3:57 AM.
*   **March 16, 2026 (07:05 AM):** One message deleted by author.
*   **March 17, 2026 (05:57 AM):** Follow-up query sent regarding vertical scrolling API and position data handling. Thread generated 8 replies; last reply recorded at 6:11 AM.

**References**
*   Space URL: `https://chat.google.com/space/AAQAeSWRtgQ`
*   Specific SKUs discussed: `90175183`, `90175149`


## gchat/space/AAQAUbi9szY/aaaRSNHkOhU: [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/aaaRSNHkOhU | Last Activity: 2026-03-17T05:46:06.546000+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Key Participants & Roles**
*   **Michael Bui:** Lead developer/submitter; driving PR reviews and updates.
*   **Yangyu Wang:** Default reviewer; provided approval for PR #649.
*   **Daryl Ng:** Reviewer/Default reviewer; reviewed PRs and updated default reviewer settings.
*   **Lester Santiago Soriano:** Reviewer; provided specific feedback on map size and loop logic.
*   **Zaw Myo Htet & Sundy Yaputra:** Listed as reviewers for PR #362.

**Main Topic**
Code review and approval cycles for two Pull Requests (PRs) within the NTU-Link ecosystem:
1.  **Layout Service (PR #362):** Focused on layout updates.
2.  **Website Service (PR #649):** Addressed map size and loop logic issues; previously briefed to Daryl Ng.

**Actions Pending & Ownership**
*   **Review PR #362:** Requires review from Michael Bui's tagged colleagues (@Yangyu Wang, @Zaw Myo Htet, @Lester Santiago Soriano, @Sundy Yaputra). *Owner: Reviewers.*
*   **Monitor PR #649 Status:** While Yangyu Wang and Daryl Ng have provided approvals, the conversation notes "need an approval from default reviewer" before final merge. *Owner: System/Default Reviewer (Daryl Ng updated settings).*

**Decisions Made**
*   **PR #649 Feedback Accepted:** Michael Bui acknowledged specific feedback regarding "map size & loop skip" and responded to comments on March 17 at 02:55 UTC.
*   **Update Applied:** Michael Bui updated PR #649 (at 02:55 UTC) to address reviewer comments, triggering a re-review request.
*   **Reviewer Configuration Updated:** Daryl Ng confirmed the update of default reviewers for the repository at 03:17 UTC on March 17.

**Key Dates & Deadlines**
*   **March 16, 2026 (09:24 UTC):** Michael Bui requested review for PR #362 and referenced a prior briefing to Daryl Ng regarding PR #649 ("tmr").
*   **March 16, 2026 (09:51 UTC):** Acknowledgment of specific technical fixes in PR #649.
*   **March 17, 2026 (02:55 UTC):** Michael Bui submitted updates to PR #649 and requested re-review from Lester Santiago Soriano.
*   **March 17, 2026 (02:56 UTC):** @Yangyu Wang, @Zaw Myo Htet, and @Sundy Yaputra were cc'd on the updated PR #649.
*   **March 17, 2026 (05:41 UTC):** Michael Bui flagged the need for final approval from the default reviewer (@Yangyu Wang, @Daryl Ng).
*   **March 17, 2026 (05:42 UTC):** Yangyu Wang confirmed completion/approval.
*   **March 17, 2026 (05:46 UTC):** Daryl Ng confirmed updating default reviewer settings.

**References**
*   PR #362: https://bitbucket.org/ntuclink/layout-service/pull-requests/362/overview
*   PR #649: https://bitbucket.org/ntuclink/website-service/pull-requests/649/overview


## gchat/space/AAQAUbi9szY/9Bb7o5yFEdU: [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/9Bb7o5yFEdU | Last Activity: 2026-03-17T05:42:49.832000+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Source:** Google Chat Space [Internal] (Ecom/Omni) Digital Product Development
**Link:** https://chat.google.com/space/AAQAUbi9szY
**Reference Date:** March 17, 2026

**Key Participants & Roles**
*   **Michael Bui:** Inquired about system behavior regarding order status updates and timestamp logic.
*   **Wai Ching Chan:** Confirmed system logic and provided verification evidence via a UAT link.

**Main Topic**
The discussion focused on the database field `completed_at` within the delivery order workflow, specifically verifying if this timestamp updates when an order transitions from "dispatch" to "completed" status for a second time (re-delivery scenario).

**Decisions Made**
*   **Timestamp Logic Confirmed:** It was established that if an order is changed from "dispatch" to "completed" status a second time, the `completed_at` value in the order record **will be updated** to reflect the latest time of completion.

**Key Dates & References**
*   **Date of Discussion:** March 17, 2026 (Messages sent at 05:40:42 and 05:42:49 UTC).
*   **Verification URI:** https://admin-uat.fairprice.com.sg/operations/delivery-orders/order-log/75553187

**Pending Actions & Ownership**
*   **No pending actions identified.** The query was resolved immediately by Wai Ching Chan providing a definitive "yes" and a direct link to the UAT order log for verification. Michael Bui has received the necessary confirmation regarding the system behavior.


## gchat/space/AAQAUbi9szY: [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Last Activity: 2026-03-17T05:40:42.183000+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Key Participants & Roles**
*   **Sundy Yaputra:** Android Developer / Ticket owner.
*   **Daryl Ng:** Coordinator; driving UAT slot verification, PR reviews, and analytics integration queries.
*   **Michael Bui:** Lead/Developer; requesting PR reviews and clarifying order state logic (re-delivery).
*   **Lester Santiago Soriano:** Developer; submitting API change requests for review.
*   **Andin Eswarlal Rajesh:** Android Dev; primary assignee for Zendesk ticket and Amplitude tracking queries.
*   **Akash Gupta, Wai Ching Chan, Yangyu Wang, Zaw Myo Htet, Lester Santiago Soriano:** Reviewers/Respondents for specific technical reviews.

**Main Topics**
1.  **Android Support & Analytics:** Handling a Zendesk ticket requiring Android dev intervention and investigating Frontend event transmission to Amplitude via the tracking service.
2.  **UAT Testing:** Verifying slot availability for PFC (FairPrice) on UAT to enable BCRS order placement.
3.  **Code Reviews (PRs):** Multiple Pull Requests submitted across `layout-service`, `website-service`, and `lt-strudel-api-go` requiring peer review.
4.  **Order Logic Validation:** Clarifying behavior of the `completed_at` timestamp during order status re-delivery scenarios (dispatch to completed).

**Pending Actions & Ownership**
*   **Zendesk Ticket #4431873:** Investigate and resolve issue reported by user; Owner: **Andin Eswarlal Rajesh**.
*   **UAT Slot Check:** Verify PFC slot availability for BCRS UAT orders; Owners: **Akash Gupta** and **Wai Ching Chan** (per last reply).
*   **PR Review - Layout Service (#362):** Review code changes; Owner: Team including **Yangyu Wang**, **Zaw Myo Htet**, and **Lester Santiago Soriano**.
*   **PR Review - Website Service (#649):** Review code changes (referenced as urgent by Daryl Ng for "tomorrow"); Owner: **Daryl Ng** confirmed timeline.
*   **PR Review - LT Strudel API Go (#472):** Review code changes; Owner: **Lester Santiago Soriano** requested review.
*   **Amplitude Event Flow:** Investigate how Frontend sends events to Amplitude; Owner: **Andin Eswarlal Rajesh**.
*   **Order Logic Check:** Determine if `completed_at` updates on re-delivery when order status changes from dispatch to completed; Owner: **Wai Ching Chan**.

**Decisions Made**
*   No explicit final decisions recorded in the snippet; current focus is on execution of reviews and troubleshooting. Daryl Ng explicitly requested PR #649 be reviewed "tmr" (March 17), establishing an immediate deadline consensus.

**Key Dates & Deadlines**
*   **March 16, 2026:** Multiple requests initiated (Zendesk ticket, UAT check, PR submissions).
*   **March 17, 2026 (Tomorrow):** Deadline for reviewing Website Service PR #649 (per Daryl Ng's instruction on March 16).
*   **Last Activity Timestamps:** Most recent interactions occurred between March 16 and March 17 early morning hours (UTC+0).

**References**
*   Zendesk: `https://fairpriceon.zendesk.com/agent/tickets/4431873`
*   Bitbucket PRs:
    *   Layout Service: `.../pull-requests/362/overview`
    *   Website Service: `.../pull-requests/649/overview`
    *   LT Strudel API Go: `.../pull-requests/472`


## gchat/space/AAQAX9iKYf0: Team Starship
Source: gchat | Group: space/AAQAX9iKYf0 | Last Activity: 2026-03-17T05:04:01.478000+00:00
**Daily Work Briefing: Team Starship**
**Link:** https://chat.google.com/space/AAQAX9iKYf0

**Key Participants & Roles**
*   **Vivian Lim Yu Qian:** Reported a UI regression issue regarding app icon display.
*   **Prajney Sribhashyam:** Communicated strategic project status updates and compliance-related holds.
*   **Andin Eswarlal Rajesh / Alvin Choo:** Tagged as recipients/owners for the bug fix request.
*   **Danielle Lee / Koklin Gan:** Tagged for visibility on the sales breakdown project hold.

**Main Topics**
1.  **UI Regression (Bug):** The app icon incorrectly displays a Christmas theme instead of reverting to the default state after a Chinese New Year (CNY) update cycle. This was identified as a simple "Jobs to be Done" (JTBD) requirement failure.
2.  **Strategic Project Hold:** The "Sales Breakdown & Seller Payouts" initiative (OMNI-1345) requires a foundational change due to business license limitations and compliance inputs from the MP Business unit.

**Pending Actions & Ownership**
*   **Fix UI Bug:** Resolve the app icon display error (Default vs. Christmas theme).
    *   **Owner:** Engineering team (specifically @Andin Eswarlal Rajesh and @Alvin Choo via ticket DPD-783).
    *   **Ticket Reference:** https://ntuclink.atlassian.net/browse/DPD-783
*   **Resume OMNI-1345 Development:** Wait for finalization of requirements regarding the consolidated fulfilment business model.
    *   **Owner:** MP Business unit (to provide finalized compliance inputs).

**Decisions Made**
*   **Project Pause:** Development on the Sales Breakdown & Seller Payouts report and seller payouts logic has been officially placed on hold. Work will not proceed until the foundational business model changes are fully defined based on compliance constraints.

**Key Dates & Follow-ups**
*   **2026-03-17 01:59 UTC:** Vivian Lim Yu Qian created bug ticket DPD-783 and flagged the issue as urgent ("asap").
*   **2026-03-17 05:04 UTC:** Prajney Sribhashyam confirmed the hold on OMNI-1345 due to compliance inputs.
*   **Follow-up Required:** Monitoring ticket DPD-783 for resolution; awaiting requirement finalization from MP Business before resuming OMNI-1345 work.


## gchat/dm/zSwVhSAAAAE: Ben Tan
Source: gchat | Group: dm/zSwVhSAAAAE | Last Activity: 2026-03-17T04:48:40.367000+00:00
**Daily Work Briefing: Google Chat Summary**
**Resource:** Ben Tan
**Date:** March 17, 2026

**Key Participants & Roles**
*   **Ben Tan:** Lead for Food Services.
*   **Michael Bui:** Recipient of request; owner of technical documentation.
*   **Steven:** Network team member (not active in chat).

**Main Topic**
Resolution of a missing document required to secure approval for the deployment of VXT technology at Kopitiam locations.

**Discussion Summary**
Ben Tan initiated contact regarding a document shared with Steven from the network team, which Steven could not locate. Ben clarified that the missing item is the **Network Technical Specification for VXT**. He noted that Steven had previously requested this via email on **February 6th**, but it appears to have been overlooked by Michael.

**Actions Pending & Ownership**
*   **Status:** Completed/Resolved.
*   **Action:** Michael Bui acknowledged missing the original email request and has replied to Steven with the document.
*   **Owner:** Ben Tan confirmed receipt of Michael's response ("thanks").
*   **Current Blocker:** None. The immediate dependency on the document has been cleared.

**Decisions Made**
No new strategic decisions were recorded; the discussion focused solely on locating and delivering an existing technical specification.

**Key Dates & Follow-ups**
*   **February 6, 2026:** Date of Steven's original email request for the VXT specifications (referenced by Ben Tan).
*   **March 17, 2026:**
    *   **02:54 UTC:** Conversation initiated regarding missing document.
    *   **03:07 UTC:** Michael Bui confirmed he missed the email and replied.
    *   **04:48 UTC:** Ben Tan acknowledged receipt of the reply, closing the immediate communication loop.

**Next Steps**
The conversation indicates an implicit dependency on the document delivery to proceed with the approval process for the Kopitiam deployment. Since Michael has replied and Ben has thanked him, no further chat actions are required immediately unless Steven requires additional clarification directly from the network team.


## gchat/space/AAAAP63CaPo: Digital & Tech - General
Source: gchat | Group: space/AAAAP63CaPo | Last Activity: 2026-03-17T04:05:32.185000+00:00
**Daily Work Briefing: Digital & Tech – General**

**Key Participants & Roles**
*   **Sip Khoon Tan:** Announcer/Coordinator for the upcoming training workshop.
*   **Flora Wo Ke:** Staff member seeking assistance regarding a lost item.
*   **#all (Digital & Tech Team):** The target audience for both announcements and the owner of potential actions.

**Main Topic/Discussion**
The conversation covers two distinct items:
1.  **Training Announcement:** Promotion of a "Workbench Hands-on Training" focused on Gemini Enterprise and NotebookLM, featuring live demos, no-code/low-code agent building, and certified instruction.
2.  **Lost Item Report:** A request for assistance in locating missing AirPods Pro (2nd Gen) with case found or left at the office location L11.

**Pending Actions & Ownership**
*   **Action:** Sign up for the AI training workshop via the provided form.
    *   **Owner:** Any Digital & Tech team member interested in the session.
    *   **Details:** Registration link is open; seats are limited. Virtual attendance is available, or alternative dates (8 or 9 April) can be booked if March 19 is unavailable.
*   **Action:** Report finding missing AirPods Pro (2nd Gen).
    *   **Owner:** Any staff member who has located the item.
    *   **Details:** Item description: AirPods Pro (2nd Gen) with case. Location: L11 office area.

**Decisions Made**
*   No formal decisions were recorded in this thread. The content consists of an invitation and a request for information.

**Key Dates, Deadlines & Follow-ups**
*   **Training Date:** Thursday, 19 March, 2:00 PM – 5:00 PM (In-person at FP Hub L10, Training Rooms 3, 5, 7).
*   **Alternative Training Dates:** 8 April and 9 April (for those unable to attend on the 19th).
*   **Event Location:** FP Hub L10.
*   **Lost Item Date:** Left in office last week (approx. 10–16 March, based on current date of 17 March).


## gchat/space/AAQAeSWRtgQ/DTof-3CAoiw: Video & Product Ads Working Group
Source: gchat | Group: space/AAQAeSWRtgQ/DTof-3CAoiw | Last Activity: 2026-03-17T03:57:03.522000+00:00
**Daily Briefing: Video & Product Ads Working Group**

**Key Participants & Roles**
*   **Michael Bui:** Investigator/Tester (Identified position discrepancy, validated fix).
*   **Norman Goh:** Orchestrator Developer (Implemented logic fix for OOS handling).
*   **Yangyu Wang:** Lead Developer (Provided context on previous code issues and split logic).
*   **Flora Wo Ke:** Team Member (Raised initial query regarding release status).
*   **Daryl Ng:** PR Reviewer (Requested review of the proposed fix).

**Main Topic**
Investigation and resolution of a discrepancy in ad positioning where the marketing service returned positions `(2,5)` while the system displayed `(1,3)`. The root cause was identified as an incorrect execution order in the orchestrator: previously, products were sorted by ad position *before* filtering out Out-of-Stock (OOS) items. This caused index shifting when OOS items were subsequently removed.

**Key Decisions & Resolutions**
*   **Root Cause:** The fix to call the marketing service only after removing OOS items was incomplete/buggy in previous iterations and had not been released.
*   **Logic Correction (Done):** Norman updated the orchestrator workflow to:
    1.  Fetch product details and remove OOS products *first*.
    2.  Call the ads API to get advertised products *second*.
*   **Verification:** Michael confirmed on UAT that after reinstalling the app, ads appeared at the correct dynamic positions (e.g., slots 2, 5) as defined by Split.io configurations.

**Pending Actions & Ownership**
1.  **PR Review:** Norman has opened Pull Request #207 to formalize the logic update.
    *   *Action:* Daryl Ng and Yangyu Wang to review the PR at `https://bitbucket.org/ntuclink/engage-content-orchestration-go/pull-requests/207/overview`.
2.  **Testing Strategy:** Norman requested verification tests for the fix.
    *   *Clarification:* Michael noted that manual verification of dynamic slot positions (e.g., seeing ads in slots 2, 5) serves as sufficient validation given the Split.io configuration.

**Key Dates & Follow-ups**
*   **2026-03-16:** Issue reported (07:03 UTC); Fix implemented and tested on UAT (09:24 UTC).
*   **2026-03-16 10:05 UTC:** PR #207 submitted for review.
*   **2026-03-17:** Follow-up sent regarding test coverage; confirmation of fix efficacy received (03:57 UTC).

**Technical References**
*   **Orchestrator Service URL:** `https://api.p13n.preprod.fairprice.com.sg/orchestrator`
*   **PR Link:** https://bitbucket.org/ntuclink/engage-content-orchestration-go/pull-requests/207/overview
*   **Config Tool:** Split.io (used for dynamic position mapping).


## gchat/space/AAQApzD7Im0: DPD x DPM
Source: gchat | Group: space/AAQApzD7Im0 | Last Activity: 2026-03-17T03:36:49.381000+00:00
**Daily Work Briefing: DPD x DPM**

**Key Participants & Roles**
*   **Vivian Lim Yu Qian:** Product/Project Lead (initiating requests regarding Algolia, App Rollouts, and Content Migration).
*   **Andin Eswarlal Rajesh:** Engineering Contact (FE/BE).
*   **Daryl Ng:** Engineering/Product Owner (Gamification ownership).
*   **Sneha Parab & Arijit Mondal:** Technical Leads (SWA/Publitas migration context).
*   **Rajesh Dobariya:** CRM Team Representative (seeking data availability for automation).

**Main Topics**
1.  **Algolia Integration:** Discussion on participant allocation for an upcoming call regarding Algolia events.
2.  **Mobile App Feature Rollout:** Request to enable the "Search on Omni home" feature and sticky header UI for Android users at a 100% rollout rate.
3.  **Content Migration (SWA):** Investigation into technical effort required to revert SWA ad integration from Publitas back to WordPress.
4.  **Gamification Data Ownership:** Clarification on current ownership of Gamification data and its availability in BigQuery for CRM automation.

**Pending Actions & Owners**
*   **Action:** Confirm attendance/participant roles (FE/BE) for the Algolia call scheduled at 11:00 AM today.
    *   **Owner:** Vivian Lim Yu Qian / Team Leads.
*   **Action:** Enable "Search on Omni home" and sticky header UI features for Android users to 100% rollout effective immediately (today). Provide the minimum build number incorporating these changes.
    *   **Owner:** Engineering Team (referenced: Andin Eswarlal Rajesh, Daryl Ng).
    *   **References:** Jira `ENGM-2501`; Harness split definition URL provided in chat.
*   **Action:** Assess effort required to revert SWA ads from Publitas back to WordPress and provide a response.
    *   **Owner:** Technical Team (referenced: Sneha Parab, Arijit Mondal).
    *   **Reference:** Jira `DIS-585`.
*   **Action:** Confirm Gamification data ownership, verify existence of required data points in the system, and identify if data is pushed to BigQuery. If pushed, provide table/column details; if not, determine push requirements.
    *   **Owner:** Daryl Ng / Previous Team (Nhu/Jack).

**Decisions Made**
*   No final decisions recorded yet; all points are currently inquiries awaiting technical assessment or confirmation from respective owners.

**Key Dates & Deadlines**
*   **2026-03-16 11:00 AM:** Scheduled call regarding Algolia events (Vivian requested attendance).
*   **2026-03-16 (Today):** Target deadline for Android app feature enablement (Search on Omni home + Sticky Header).
*   **Follow-ups:** Pending replies to Vivian's requests and Rajesh's inquiry on Gamification.


## gchat/space/AAAAtxQjB7c: #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Last Activity: 2026-03-17T03:30:08.224000+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert**
**Date:** March 16–17, 2026
**Total Alerts:** 12 (All Datadog automated triggers/recoveries)

### **Key Participants & Roles**
*   **Notification Targets:** `@hangouts-dd-dpd-grocery-alert`, `@hangouts-GT-Discovery-DatadogAlerts`, `@opsgenie-dpd-grocery-discovery`.
*   **Service Owners:** `dpd-grocery`, `dpd-grocery-discovery`, `dpd-staff-excellence-pdm` (Product Data Management), `qc-layout-service` team.

### **Main Topic**
Automated monitoring of production environment stability across Grocery and Product Data Management services. The conversation consists entirely of system-generated alerts regarding service failures, latency spikes, low job throughput, and error rate violations, followed by automatic recovery notifications. No human discussion occurred in the chat log.

### **Incident Summary & Status**
1.  **Search Indexer Sanity Checks (P2):**
    *   **Trigger:** `fp-search-indexer` failed sanity checks.
    *   **Timeline:** Triggered at 00:39 UTC, Recovered at 01:39 UTC; Triggered again at 05:39 UTC, Recovered at 06:39 UTC.
    *   **Service:** `fp-search-indexer` (Grocery Discovery).

2.  **Catalogue Service Latency (P3):**
    *   **Trigger:** High p90 latency (>2000ms) on `go-catalogue-service` resource `get_/category/_id`.
    *   **Timeline:** Triggered at 04:59 UTC, Recovered at 05:15 UTC.
    *   **Peak Metric:** 2.07s (Threshold >2.0s).

3.  **SKU-Store-Attribute Job Throughput (P3):**
    *   **Trigger:** Low processed file count (<6 files in 4 hours) for `sku-store-attribute`.
    *   **Timeline:** Triggered at 22:15 UTC (Mar 16), Recovered at 01:03 UTC (Mar 17).

4.  **PLP Success Rate Violation (No Severity):**
    *   **Trigger:** Product listing success rate dropped below 99.9% for `qc-layout-service` (`get_/v1/pages/plp`).
    *   **Timeline:** Triggered at 02:48 UTC, Recovered at 02:58 UTC (Mar 17).
    *   **Metric Value:** Dropped to 66.667% success rate.

5.  **SKU Global Attribute Error Rate (P3):**
    *   **Trigger:** High error rate (>0.1%) for `sku_global_attribute` batch processing.
    *   **Timeline:** Triggered at 03:02 UTC, Recovered at 03:30 UTC (Mar 17).
    *   **Peak Metric:** 92.008% error rate.

### **Pending Actions & Ownership**
*   **No Active Incidents:** All monitored services have returned to "Recovered" status with current metric values within acceptable thresholds.
*   **Recommended Investigation (Post-Incident):** For the `sku-store-attribute` job and `qc-layout-service` outage, the alert text recommends checking logs for errors/warnings and verifying dependencies. No specific owner was assigned in the log, but standard ownership lies with `dpd-grocery-discovery` (for jobs) and `dpd-staff-excellence-pdm` (for layout service).

### **Decisions Made**
*   None recorded. All events were system-triggered and subsequently auto-resolved by Datadog.

### **Key Dates & Follow-ups**
*   **Mar 16, 04:59 UTC:** Latency incident resolved.
*   **Mar 16, 22:15 UTC:** Job throughput alert triggered.
*   **Mar 17, 02:48–03:30 UTC:** Cluster of issues (PLP success rate and SKU attribute errors) resolved within a 42-minute window.
*   **Follow-up:** Review post-mortem for the high error spike in `sku_global_attribute` (92% error rate) to prevent recurrence, as this indicates a significant processing failure prior to recovery.


## gchat/space/AAQAdWQ11dY: @omni-ops #standup - Mar 17
Source: gchat | Group: space/AAQAdWQ11dY | Last Activity: 2026-03-17T03:12:48.926000+00:00
**Daily Work Briefing: #omni-ops Standup (Mar 17)**

**Key Participants**
*   **Sundy Yaputra:** Initiator of standup; owner of FE popup support tasks.
*   **Daryl Ng:** Lead in discussion; clarifying approval flows, coordination with stakeholders (Vivian), and permission structures. CC: @Sathya Murthy Karthik.
*   **Rohit Pahuja:** Developer/Assignee for DPD-763; confirmed permissions logic.
*   **Yangyu Wang:** Developer; completed DPD-742; investigating API inconsistencies.

**Main Topics**
1.  **Service Desk & Deployment (DSD-11065):** Confirmed that the request submitted by Rohit requires no further approval as it is already approved. Daryl requested status updates be shared in the chat with @Sathya Murthy Karthik copied.
2.  **Browse API Issues:**
    *   Yangyu completed **DPD-742** (Picker app resolution).
    *   Current focus: Investigating product inconsistent ordering between Home and PLP pages.
    *   Decision: Daryl proposed deploying without the inconsistency fix first, pending confirmation from Vivian.
3.  **Whitelist Domain Permissions (DPD-763):**
    *   Rohit has received Backoffice permissions and is currently setting them up for the whitelist domain page.
    *   Clarification on access: Daryl asked if all users with "App Home" permissions would access this submenu.
    *   Confirmation: Rohit confirmed that **all** users with App Home permissions will have access to the new page.

**Pending Actions & Owners**
*   **Confirm Deployment Strategy:** Update Vivian regarding the deployment of DPD-742 without the inconsistency fix first; await her approval. *(Owner: Team/Daryl)*
*   **Finalize Permissions Setup:** Complete the setup for whitelist domain permissions in DPD-763. *(Owner: Rohit Pahuja)*
*   **Frontend Support for 1HD:** Prioritize work required to support the FE team in displaying the popup for "1HD". *(Owner: Sundy Yaputra)*

**Decisions Made**
*   **DSD-11065:** No approval action needed; ticket is already approved.
*   **DPD-742 Deployment Strategy:** Proceed with deployment of the picker app fix (DPD-742) before resolving the Browse API ordering inconsistency, subject to Vivian's confirmation.
*   **Permission Scope:** The whitelist domain page (DPD-763) is accessible to every user who currently has "App Home" permissions.

**Key Dates & References**
*   **Date:** March 17, 2026
*   **Jira Tickets:** DPD-742 (Completed), DPD-763 (In Development), DSD-11065 (Service Desk).
*   **Links:** [DSD-11065](https://ntucenterprise.atlassian.net/servicedesk/customer/portal/1459/DSD-11065?created=true), [DPD-742](https://ntuclink.atlassian.net/browse/DPD-742), [DPD-763](https://ntuclink.atlassian.net/browse/DPD-763).
