

## [1/43] Invitation:  D&T International Food Day! @ Thu Apr 30, 2026 12pm - 2pm (SGT) (Michael Bui)
Source: gmail | Thread: 19d626f73d5d1fd1 | Labels: Inbox | Priority: None | Senders: Trina Boquiren | Last Date: Mon, Apr 6, 2026, 10:56 AM | Last Updated: 2026-04-06T14:01:33.638478+00:00
**Daily Work Briefing: D&T International Food Day**

**Key Participants & Roles**
*   **Trina Boquiren (trina.boquiren@fairpricegroup.sg):** Event Organizer. Primary point of contact for logistics, registration, and rules.
*   **Michael Bui (michael.bui@fairpricegroup.sg):** Guest/Attendee (Sender of the briefing resource). Has RSVPed "Yes."
*   **D&T Family:** Target audience comprising all staff within the Design & Technology department.

**Main Topic & Request**
Invitation to the **International Food Day**, a cultural celebration featuring food sharing, storytelling, and a competitive element ("The Delicious Showdown"). Staff are invited to either contribute a dish for a contest or attend as guests to vote.

**Pending Actions & Ownership**
*   **RSVP Deadline:** All staff must respond by **Friday, 24 Apr 2026**.
    *   *Contestants:* Must register explicitly via the calendar invite to enter the prize pool.
    *   *Attendees:* Must accept the calendar invite for headcount accuracy.
*   **Event Setup:** Contestant contributors must deliver dishes to **L10 Clubhouse** by **10:00 AM on Thursday, 30 Apr 2026**.

**Decisions Made**
*   Event logistics confirmed: Date (30 Apr), Time (12:00 PM – 2:00 PM SGT), and Location (L10 Clubhouse).
*   Competition parameters established: Voting for Top 3 Most Popular Dishes with a **$50 voucher** prize for winners.

**Key Dates & Deadlines**
*   **24 Apr 2026 (Friday):** Final deadline for all RSVPs and contest registrations.
*   **30 Apr 2026 (Thursday), 10:00 AM:** Deadline for food contributors to arrive at L10 Clubhouse for setup.
*   **30 Apr 2026 (Thursday), 12:00 PM – 2:00 PM:** Scheduled event time.

**Meeting Details**
*   **Platform:** Google Meet Link provided (`meet.google.com/zta-zopx-wuj`) and Phone PIN: `494269436`.
*   **Registration Link:** Attached via Google Drive (File ID: `1hf_SXn0lX8H3ra3zeOMMnbryTPZSmEIX`).

**Summary Note**
The event aims to foster culture and connection. Immediate attention is required from staff by the 24 Apr deadline to confirm attendance or register for the dish competition.


## [2/43] [Action Required] Service Account Key Expiring, Renewal Required - aa003fb613da95c20d5009d28e84c111cd64b291
Source: gmail | Thread: 19d626134135e75b | Labels: Inbox, Forums | Priority: None | Senders: noreply-sre | Last Date: Mon, Apr 6, 2026, 10:40 AM | Last Updated: 2026-04-06T14:01:47.230156+00:00
**Daily Work Briefing: Service Account Key Renewal Alert**

**1. Key Participants & Roles**
*   **Sender:** `noreply-sre@ntucenterprise.sg` (SRE Team / Automated System). Role: Notifying and requesting action on infrastructure security.
*   **Recipient:** Unspecified engineering/ops team member responsible for the `fp-marketing-tech-production` project.

**2. Main Topic & Request**
The SRE team has identified that a specific service account key is nearing expiration and requires immediate rotation to prevent authentication failures and system disruptions. The core request is to download the newly generated key (sent in a separate email) and replace the existing credential within the target system before it becomes invalid.

**3. Pending Actions & Ownership**
*   **Action:** Download the new service account key sent via separate notification email.
    *   *Owner:* Service Account Owner / Engineering Team.
*   **Action:** Update/Replace the existing key (`aa003fb613da95c20d5009d28e84c111cd64b291`) in the target system with the new key.
    *   *Owner:* Service Account Owner / Engineering Team.
*   **Action (Conditional):** If the key is confirmed stale and no longer needed, raise a SRE request to remove it permanently.
    *   *Owner:* Service Account Owner / Engineering Team.

**4. Decisions Made**
No new decisions were made in this thread; the notification serves as a directive based on automated monitoring of credential lifecycles.

**5. Key Dates & Deadlines**
*   **Notification Date:** April 6, 2026, at 10:40 AM.
*   **Critical Deadline:** May 6, 2026 (Key Expiration). The key `aa003fb613da95c20d5009d28e84c111cd64b291` will cease to function after this date.
*   **Follow-up:** Immediate action required prior to May 6, 2026, to ensure no service disruption.

**Service Account Details for Reference:**
*   **Key ID:** `aa003fb613da95c20d5009d28e84c111cd64b291`
*   **Account Email:** `martech-etl-non-pii@fp-marketing-tech-production.iam.gserviceaccount.com`
*   **Project Context:** `fp-marketing-tech-production/martech-etl-non-pii`


## [3/43] Notes: Meeting Apr 6, 2026 at 5:00 PM GMT+08:00
Source: gmail | Thread: 19d623fae78f5cc6 | Labels: Inbox, Updates | Priority: None | Senders: Gemini | Last Date: Mon, Apr 6, 2026, 10:03 AM | Last Updated: 2026-04-06T14:02:03.657729+00:00
**Daily Work Briefing: Meeting Notes (April 6, 2026)**

**Key Participants & Roles**
*   **Nikhil Grover:** Responsible for Segment architecture review and tracking alignment.
*   **Michael Bui:** Owner of effort estimates for invoicing automation and SFMC data transfer.
*   **Yadi:** Technical contact for the Segment architecture session with Nikhil Grover.
*   **Daryl & Rajes:** Stakeholders to be consulted regarding UTM tracking implementation approaches.
*   **Rajiv:** Source for effort estimation on user information transfer to SFMC.
*   **Gemini (System):** Auto-generated notes from Google Meet; sent to invited guests.

**Main Topic/Request**
The meeting focused on resource planning for prioritized features, technical alignment on tracking integration via external vendors, and budget allocation for de-prioritized features. Key discussions covered carrier targeting solutions, Segment integration scalability, and front-end ad tracking implementation.

**Decisions Made**
*   **Budget & Resources:** Budget availability permits hiring external resources to address de-prioritized features. Four display touch points are allocated 8 weeks of development time.
*   **Carrier Targeting Method:** The team proposed using IP address lookups to identify carrier data, subject to legal approval.
*   **Integration Strategy:** Ad tracking implementation will prioritize front-end methods to minimize complexity.
*   **Segment Focus:** The group decided to investigate backend scalability specifically for Segment integration.

**Pending Actions & Owners**
1.  **[The Group]: Secure Legal/DPO Approval.** Obtain approval from legal and the Data Protection Officer (DPO) regarding the use of personal information to target users based on carrier data.
2.  **[Nikhil Grover]: Review Segment Architecture.** Schedule a session with Yadi to review Segment architecture for carrier targeting, specifically verifying tagging capabilities at the device level.
3.  **[Michael Bui]: Finalize Invoicing Estimate.** Provide a high-level effort estimate for the invoicing automation project (tentatively estimated at 2–4 weeks).
4.  **[Michael Bui]: Obtain SFMC Transfer Estimate.** Secure a high-level effort estimate from Rajiv or relevant parties regarding securely sending user information to SFMC for prefilled survey forms.
5.  **[Nikhil Grover]: Align Tracking Approach.** Schedule an alignment meeting with Daryl and Rajes to confirm the implementation approach for UTM tracking (front-end vs. server-to-server).

**Key Dates & Deadlines**
*   **Meeting Date:** April 6, 2026, at 5:00 PM GMT+08:00.
*   **Notes Generated:** April 6, 2026, at 5:59 PM GMT+08:00.
*   **Development Timeline:** Four display touch points require an 8-week window.
*   **Project Estimates:** Invoicing API integration is tentatively estimated at 2 to 4 weeks.

**References & Metadata**
*   **Meeting Resource ID:** last_message_id "19d623fae78f5cc6".
*   **Labels:** Inbox, Updates.
*   **Contact Info:** Google LLC, 1600 Ampitheatre Parkway, Mountain View, CA 94043, USA.


## [4/43] Canceled event: [DPD AI Guild] Committee Monthly Meeting @ Tue Apr 7, 2026 10am - 10:50am (SGT) (Zheng Ming New)
Source: gmail | Thread: 19d622a7f5dbff9b | Labels: None | Priority: None | Senders: me | Last Date: Mon, Apr 6, 2026, 9:40 AM | Last Updated: 2026-04-06T10:01:28.825039+00:00
**Daily Work Briefing: Event Cancellation Notification**

**1. Key Participants & Roles**
*   **Michael Bui (michael.bui@fairpricegroup.sg):** Organizer of the event and source of cancellation notification.
*   **Attendees:** Varun Chauhan, James Lai Li Hao, Jazz Tong, Mohammed Miran, Zheng Ming New.

**2. Main Topic/Request**
*   Notification regarding the cancellation of the **[DPD AI Guild] Committee Monthly Meeting**.
*   The event has been officially removed from all attendees' calendars effective April 6, 2026.

**3. Pending Actions & Ownership**
*   **Status:** No pending actions required by recipients; the meeting is canceled.
*   **Ownership:** Organizer (Michael Bui) has completed the cancellation process.
*   **Note:** Attendees must ensure they do not attempt to join the previously scheduled session on April 7, 2026.

**4. Decisions Made**
*   The **[DPD AI Guild] Committee Monthly Meeting** scheduled for Tuesday, April 7, 2026, is **canceled**.
*   The meeting link (Google Meet: `meet.google.com/zhj-udzb-apd`) and phone dial-in details are no longer active for this session.

**5. Key Dates & Specific References**
*   **Original Meeting Date:** Tuesday, April 7, 2026.
*   **Time:** 10:00 AM – 10:50 AM (Singapore Standard Time).
*   **Original Location:** FairPrice Hub-11-L11 Room 10 (6) [Google Meet].
*   **Cancellation Sent:** April 6, 2026, at 9:40 AM.
*   **Event Reference:** [DPD AI Guild] Committee Monthly Meeting @ Tue Apr 7, 2026 10am - 10:50am (SGT) (Zheng Ming New).


## [5/43] Canceled event: [DPD AI Guild] Committee Monthly Meeting @ Tue Apr 7, 2026 10am - 10:50am (SGT) (James Lai Li Hao)
Source: gmail | Thread: 19d622a74576bd1d | Labels: None | Priority: None | Senders: me | Last Date: Mon, Apr 6, 2026, 9:40 AM | Last Updated: 2026-04-06T10:01:46.097822+00:00
**Daily Work Briefing: Event Cancellation Notice**

**Key Participants & Roles**
*   **Michael Bui (michael.bui@fairpricegroup.sg):** Organizer; sender of the cancellation notice.
*   **James Lai Li Hao:** Guest attendee.
*   **Other Attendees:** Varun Chauhan, Jazz Tong, Mohammed Miran, Zheng Ming New.

**Main Topic/Request**
The "DPD AI Guild" Committee Monthly Meeting scheduled for Tuesday, April 7, 2026, has been officially canceled and removed from all attendees' calendars by the organizer.

**Actions Pending & Ownership**
*   **Status:** No active action items remain regarding this specific meeting as it is canceled.
*   **Ownership:** N/A (Meeting nullified).

**Decisions Made**
*   The organizer has decided to cancel the event entirely, removing it from the calendar invite system effective April 6, 2026, at 9:40 AM SGT.

**Key Dates & Deadlines**
*   **Original Event Date/Time:** Tuesday, April 7, 2026, 10:00 AM – 10:50 AM (SGT).
*   **Cancellation Notification Sent:** Monday, April 6, 2026, 9:40 AM (SGT).
*   **Location (Now Inactive):** FairPrice Hub-11-L11 Room 10 (6) [Google Meet].
*   **Meeting Link (Inaccessible):** meet.google.com/zhj-udzb-apd.

**Summary**
The DPD AI Guild Committee Monthly Meeting scheduled for April 7, 2026, is canceled. All guests (Varun Chauhan, James Lai Li Hao, Jazz Tong, Mohammed Miran, Zheng Ming New) have been notified via calendar update that the event has been removed from their schedules. No follow-up meeting time was indicated in this specific notification.


## [6/43] Invitation: Andin Eswarlal / Nikhil - Roadmap clarifications @ Tue Apr 7, 2026 9:45am - 10:15am (SGT) (Michael Bui)
Source: gmail | Thread: 19d6229f40254382 | Labels: Inbox | Priority: None | Senders: Nikhil Grover | Last Date: Mon, Apr 6, 2026, 9:40 AM | Last Updated: 2026-04-06T10:02:02.160180+00:00
**Daily Work Briefing: Roadmap Clarifications**

**Key Participants & Roles**
*   **Nikhil Grover** (`nikhil.grover@fairpricegroup.sg`): Meeting organizer.
*   **Andin Eswarlal Rajesh**: Guest attendee.
*   **Michael Bui** (`michael.bui@fairpricegroup.sg`): Optional guest (Recipient).

**Main Topic/Request**
The invitation is for a session titled "Roadmap clarifications" scheduled between Nikhil Grover and Andin Eswarlal. The objective is to discuss and clarify strategic roadmap items.

**Meeting Logistics**
*   **Date & Time**: Tuesday, April 7, 2026, from 9:45 AM to 10:15 AM (Singapore Standard Time).
*   **Format**: Virtual meeting via Google Meet.
    *   **Link**: `meet.google.com/mnp-tzae-sjf`
    *   **Phone Access**: US (+1 541-638-0404), PIN: 920202600.

**Pending Actions & Ownership**
*   **Action**: Confirm attendance status (RSVP).
*   **Owner**: Michael Bui (`michael.bui@fairpricegroup.sg`).
*   **Status**: Attendance is marked as **optional**. The system indicates the recipient must select "Yes," "No," or "Maybe."

**Decisions Made**
*   No decisions recorded in this thread. This is a calendar invitation initiating the meeting event.

**Key Dates & Follow-ups**
*   **Meeting Occurrence**: April 7, 2026.
*   **Follow-up Required**: Michael Bui should review the agenda or confirm availability prior to the start time on April 7.


## [7/43] Spreadsheet shared with you: "RMN Roadmap till Light"
Source: gmail | Thread: 19d6222a912f2e16 | Labels: Inbox, Updates | Priority: None | Senders: Nikhil Grover (via . | Last Date: Mon, Apr 6, 2026, 9:32 AM | Last Updated: 2026-04-06T09:37:18.181434+00:00
System notification from Google Sheets informing Michael Bui that Nikhil Grover has shared a spreadsheet titled "RMN Roadmap till Light" and granted edit permissions. No human-written message or action is included.


## [8/43] Spreadsheet shared with you: "RMN Invoicing - Fields requirement"
Source: gmail | Thread: 19d621a83c12208d | Labels: Inbox, Updates | Priority: None | Senders: Nikhil Grover (via . | Last Date: Mon, Apr 6, 2026, 9:23 AM | Last Updated: 2026-04-06T09:37:24.558267+00:00
A spreadsheet titled "RMN Invoicing - Fields requirement" has been shared with you. This document details the specific data fields and requirements necessary for invoicing related to the RMN (Retail Media Network) project. Given your dual mandate over Retail Media/Ad Technology and Engineering Governance, understanding these precise field definitions is critical for validating backend architecture standards, ensuring correct data orchestration for programmatic advertising and campaign management, and verifying that financial reporting aligns with engineering delivery. As a direct participant in this thread, immediate review is likely required to confirm technical feasibility or provide architectural input on how these fields map to your existing microservices and event-driven systems.


## [9/43] Notes: “BCRS SKU Posting for Express Delivery” Apr 6, 2026
Source: gmail | Thread: 19d61da362615067 | Labels: Inbox | Priority: None | Senders: Gemini | Last Date: Mon, Apr 6, 2026, 8:13 AM | Last Updated: 2026-04-06T09:37:33.505132+00:00
Automated meeting notes from April 6, 2026, summarize a discussion on aligning Barcode Carton Return Scheme (BCRS) deposit postings for one-hour delivery orders to specific store cost centers. The team identified a discrepancy where deposits currently default to cost center 004 instead of the required store-specific mapping. A technical solution was agreed upon: retrieving store identification directly from the order service during System Integration Testing. While Michael Bui is explicitly listed in the 'Suggested next steps' section with the action to 'Share details of the original BCIS ticket,' the content itself is an auto-generated summary rather than a direct human request. The decision involves Finance validation and Jira ticket creation (related to DBD3), indicating this falls under Medium Relevance as it pertains to governance, architecture implementation, and stakeholder alignment in Michael's domain.


## [10/43] Notes: Meeting Apr 6, 2026 at 3:22 PM GMT+08:00
Source: gmail | Thread: 19d61b084b1e4ddb | Labels: Inbox, Updates | Priority: None | Senders: Google Meet | Last Date: Mon, Apr 6, 2026, 7:27 AM | Last Updated: 2026-04-06T09:37:38.779158+00:00
Auto-generated email from Google Meet containing meeting notes for a session held on April 6, 2026. The message is a system notification informing the recipient that notes summarizing the meeting are available and that transcripts or recordings will be linked when ready. It includes a request to review Gemini's generated notes for accuracy. This is an informational update regarding meeting artifacts rather than a discussion requiring direct input or decision-making at this moment.


## [11/43] Accepted: BCRS SKU Posting for Express Delivery @ Mon Apr 6, 2026 3:30pm - 4pm (SGT) (Rajesh Dobariya)
Source: gmail | Thread: 19d61acc92d7b67f | Labels: None | Priority: None | Senders: me | Last Date: Mon, Apr 6, 2026, 7:23 AM | Last Updated: 2026-04-06T09:37:46.503586+00:00
Michael Bui has accepted a calendar invitation for the 'BCRS SKU Posting for Express Delivery' meeting. The session is scheduled for Monday, April 6, 2026, from 3:30 PM to 4:00 PM SGT. It was organized by Rajesh Dobariya with other attendees including Prajney Sribhashyam, Daryl Ng, and Olivia. This email is a system-generated notification confirming the RSVP status. While Michael is directly mentioned as an attendee, the content itself is informational (a meeting confirmation) rather than requiring immediate action or containing new technical decisions.


## [12/43] Notes: “B2b discussion” Apr 6, 2026
Source: gmail | Thread: 19d61a77ab00d0ed | Labels: Inbox | Priority: None | Senders: Gemini | Last Date: Mon, Apr 6, 2026, 7:17 AM | Last Updated: 2026-04-06T09:37:53.824801+00:00
System-generated meeting notes from a 'B2b discussion' on April 6, 2026. The team discussed shifting B2C infrastructure management from hands-on operations to a vendor governance model based on SLAs. Key decisions involved retaining core identity and communication services on GCP while evaluating other services for migration. Michael Bui is explicitly assigned two action items: calculate B2C core infrastructure costs (including AWS Identity/Communication, catalog, and FPM Pro components) and identify the specific data source for the DBP catalog service product enrichment. The group must compile performance data (RPS, storage, cache) to validate vendor proposals before a scheduled follow-up with Huawei.


## [13/43] NED-254147 [General Service request] Add OSMOS system to IT Helpdesk for user onboarding process and access changes
Source: gmail | Thread: 199c705ee4529c98 | Labels: Inbox, Updates | Priority: None | Senders: NE | Last Date: Mon, Apr 6, 2026, 6:01 AM | Last Updated: 2026-04-06T09:38:04.092491+00:00
Michael Bui received a request to add the 'OSMOS Portal' to the IT Helpdesk for user onboarding and access changes within the Retail Media (RMN) domain. The conversation involved Jira ticket NED-254147, where Rafael Guerta from IT Helpdesk sought clarification on the system category and requested a specific individual email for the 'System Owner' rather than a group address. Michael provided the necessary delegation details (dpd-staff-excellence-rmn@fairpricegroup.sg), leading to the configuration update. The request specified a three-tier approval flow: requester submission, Cost Center Authorization Manager approval, and System Owner approval before routing to Allen Umali for access grants. Rafael confirmed the implementation was successful on October 22, and the ticket was marked resolved in April 2026. As an Engineering Governance lead owning backend architecture standards and vendor/system integrations, Michael's direct involvement in defining the governance model for this platform is critical.


## [14/43] Re: Invitation: G5: Building a Better Workplace Together: Your Feedback M... @ Tue 7 Apr 2026 11am - 11:45am (SGT) (Carol Lee)
Source: gmail | Thread: 19d417701b5fac61 | Labels: Inbox | Priority: None | Senders: Melissa Hauw | Last Date: Mon, Apr 6, 2026, 5:48 AM | Last Updated: 2026-04-06T09:38:10.644509+00:00
This is a human-written follow-up from Melissa Hauw (HR) regarding an upcoming 'Focus Group Discussion' scheduled for Tuesday, April 7, 2026, from 11:00 AM to 11:45 AM SGT. The purpose of the session is to gather employee feedback on workplace challenges and strengths to improve the overall experience at FairPrice Group (FPG). As Michael Bui is explicitly invited via TO/CC, he has been asked to accept or decline the invitation by April 6 to help manage session size and ensure diverse representation. While this falls under HR communications which typically score lower for an engineering leader, the direct personal address regarding a workplace feedback initiative warrants medium relevance.


## [15/43] Invitation: BCRS SKU Posting for Express Delivery @ Mon Apr 6, 2026 3:30pm - 4pm (SGT) (Michael Bui)
Source: gmail | Thread: 19d6125aded53d7f | Labels: Inbox | Priority: None | Senders: Rajesh Dobariya | Last Date: Mon, Apr 6, 2026, 4:55 AM | Last Updated: 2026-04-06T09:38:17.905642+00:00
This is a system-generated Google Calendar invitation for a meeting titled 'BCRS SKU Posting for Express Delivery' scheduled for Monday, April 6, 2026, from 3:30 PM to 4:00 PM SGT. The organizer is Rajesh Dobariya, and the guest list includes Prajney Sribhashyam, Daryl Ng, Michael Bui, and Olivia. As a direct attendee, Michael's presence is required for this session focused on SKU posting capabilities within the Express Delivery domain. The email provides Google Meet join details and phone dial-in options. A response (Yes/No/Maybe) is requested from Michael to confirm attendance.


## [16/43] Notes: “ACNxOsmos: Daily Cadence” Apr 6, 2026
Source: gmail | Thread: 19d6125a03414160 | Labels: Inbox | Priority: None | Senders: Gemini | Last Date: Mon, Apr 6, 2026, 4:55 AM | Last Updated: 2026-04-06T09:38:26.211790+00:00
This is an auto-generated email containing meeting notes from the 'ACNxOsmos: Daily Cadence' held on April 6, 2026. The content summarizes discussions on ad infrastructure capabilities, specifically resolving PCNT issues that increased revenue potential. While Michael Bui (via direct mention in TO/CC) is not the primary author or explicitly assigned a new action item in this specific digest, the subject matter directly aligns with his domain expertise in Retail Media and Ad Technology. The notes highlight critical roadmap updates and outstanding items regarding video ad campaigns and API documentation standards. Notable tasks include resolving a ROAS drop-off (Ticket 964), clarifying User ID issues, and analyzing homepage inventory uptake. As a governance lead, this information is relevant for tracking project timelines and technical blockers but requires no immediate direct action from Michael.


## [17/43] Delivery Status Notification (Failure)
Source: gmail | Thread: 19d6124e9d10e456 | Labels: Inbox, Updates | Priority: None | Senders: Mail Delivery Subsy. | Last Date: Mon, Apr 6, 2026, 4:55 AM | Last Updated: 2026-04-06T09:38:30.901020+00:00
A system-generated delivery status notification indicates that an email sent to artharn.senrit_fp@ntucguest.com failed because the address could not be found or does not exist. The recipient's account appears inactive or invalid according to Google Mail's NoSuchUser error. No human interaction is present in this thread, and it serves as a passive informational update rather than an alert requiring immediate engineering action or architectural review.


## [18/43] Delivery Status Notification (Failure)
Source: gmail | Thread: 19d6124e822fe166 | Labels: Inbox, Updates | Priority: None | Senders: Mail Delivery Subsy. | Last Date: Mon, Apr 6, 2026, 4:55 AM | Last Updated: 2026-04-06T09:38:36.511748+00:00
A system-generated Delivery Status Notification (Failure) was received regarding an email sent to tanul.mehta@accenture.com. The message failed because the recipient's address could not be found (Error: 550 5.1.1 User Unknown). As a direct notification of a delivery failure, this falls under informational system alerts where no immediate engineering action is typically required unless Michael was attempting to contact a vendor or stakeholder for critical work. Given the 'direct' mention type and the nature of the alert, it scores as medium relevance (6) but does not require urgent technical intervention.


## [19/43] Updated invitation: ACNxOsmos: Daily Cadence @ Mon Apr 6, 2026 12:30pm - 1pm (SGT) (artharn.senrit@accenture.com)
Source: gmail | Thread: 19d6124e3f92afe7 | Labels: None | Priority: None | Senders: me | Last Date: Mon, Apr 6, 2026, 4:55 AM | Last Updated: 2026-04-06T09:38:52.679798+00:00
This is a system-generated calendar update email regarding the 'ACNxOsmos: Daily Cadence' meeting scheduled for Monday, April 6, 2026. The organizer, Michael Bui, updated the event attachments to include the document 'FPG Project Plan 2905025'. The meeting runs from 12:30 PM to 1:00 PM (SGT) and includes a Google Meet link for virtual attendance. Attendees include internal team members such as Flora Wo Ke, Daryl Ng, John Henji Mantaring, and representatives from Onlinesales.ai and Accenture. As Michael is the organizer who initiated this system update to modify meeting details, he requires awareness of the change, though no immediate action or decision-making is explicitly required by the email body itself.


## [20/43] Updated invitation: ACNxOsmos: Daily Cadence @ Mon Apr 6, 2026 12:30pm - 1pm (SGT) (tanul.mehta@accenture.com)
Source: gmail | Thread: 19d6124e3bd4c895 | Labels: None | Priority: None | Senders: me | Last Date: Mon, Apr 6, 2026, 4:55 AM | Last Updated: 2026-04-06T09:39:17.030541+00:00
This is a system-generated calendar update regarding the 'ACNxOsmos: Daily Cadence' meeting scheduled for Monday, April 6, 2026, from 12:30 PM to 1:00 PM SGT. Michael Bui (the organizer) updated the event attachments and sent this notification. The invitation includes a Google Meet link and dial-in details. Attendees include internal staff (Flora Wo Ke, Daryl Ng, John Henji Mantaring), external partners from Accenture (Tanul Mehta, Artharn Senrit, Satish Pamidimarthi, Shravan Kankaria), and Onlinesales.ai representatives (Vipul Gupta, Barkha Kewalramani, Rahul Jain, Tanish Nevatia, Nabhey Samant, Shubhangi Agrawal, Siddharth Aklujkar, Rachit Sachdeva). Ravi Goel is listed as optional. An attachment titled 'FPG Project Plan 2905025' was added to the meeting details.


## [21/43] Updated invitation: ACNxOsmos: Daily Cadence @ Mon Apr 6, 2026 12:30pm - 1pm (SGT) (Artharn Senrit)
Source: gmail | Thread: 19d6124e2c4785eb | Labels: None | Priority: None | Senders: me | Last Date: Mon, Apr 6, 2026, 4:55 AM | Last Updated: 2026-04-06T09:39:27.831634+00:00
Michael Bui received a system-generated update regarding the 'ACNxOsmos: Daily Cadence' meeting scheduled for Monday, April 6, 2026. The organizer (Michael) modified the event attachments. The email confirms the Google Meet link and dial-in details remain active. Michael is listed as an attendee alongside various internal stakeholders (Flora Wo Ke, Daryl Ng, Artharn Senrit) and external vendors from Onlinesales.ai and Accenture. This update serves as an informational notification confirming a change to the meeting resources rather than requiring immediate new action or decision-making.


## [22/43] Updated invitation: ACNxOsmos: Daily Cadence @ Mon Apr 6, 2026 12:30pm - 1pm (SGT) (satish.pamidimarthi@accenture.com)
Source: gmail | Thread: 19d6124e23b98a90 | Labels: None | Priority: None | Senders: me | Last Date: Mon, Apr 6, 2026, 4:55 AM | Last Updated: 2026-04-06T09:39:39.713492+00:00
Michael Bui updated a recurring daily cadence meeting (ACNxOsmos) scheduled for Monday, April 6, 2026, from 12:30 PM to 1:00 PM SGT. The update involved modifying the attachments associated with the calendar event, specifically adding or changing 'FPG Project Plan 2905025'. This meeting serves as a key stakeholder cadence involving Michael and multiple external vendors (Accenture) and partners (OnlineSales.ai), including Flora Wo Ke, Vipul Gupta, Barkha Kewalramani, Rahul Jain, Daryl Ng, John Henji Mantaring, Artharn Senrit, Nikhil Grover, Aman Khatri, Tanul Mehta, Shravan Kankaria, Ravi Goel, and Satish Pamidimarthi. As the organizer, Michael manages this session to align on project progress, likely covering retail media or platform engineering topics given his governance role.


## [23/43] Invitation: [Session 1] Sharing on SLO updates @ Tue Apr 7, 2026 4pm - 4:30pm (SGT) (Michael Bui)
Source: gmail | Thread: 19d60ea98665d1a9 | Labels: Inbox | Priority: None | Senders: Dodla Gopi Krishna | Last Date: Mon, Apr 6, 2026, 3:51 AM | Last Updated: 2026-04-06T09:39:47.206508+00:00
Dodla Gopi Krishna sent a direct invitation for 'Session 1: Sharing on SLO updates' scheduled for Tue Apr 7, 2026, at 4 PM SGT. As an engineering leader governing backend architecture standards and SLO targets, Michael Bui is the intended audience for this discussion on transitioning from the current SLO V1 framework to the proposed SLO V2 Framework. The agenda covers critical topics including limitations of the existing framework, new architectural design, impact on developers, migration planning, and a Q&A session. A reference link to NTUCLink guidelines is provided. Michael needs to attend to provide technical judgment on the architecture changes and approve or guide the migration plan.


## [24/43] Hengky Sucanda requested access to your space
Source: gmail | Thread: 19d60df9559bf07b | Labels: Inbox, Updates | Priority: None | Senders: Hengky Sucanda | Last Date: Mon, Apr 6, 2026, 3:39 AM | Last Updated: 2026-04-06T09:39:52.269063+00:00
Hengky Sucanda has requested access to the 'Project LIGHT' Confluence space. This notification is a system-generated action item requiring manual approval or management by Michael Bui. As an engineering leader governing platform architecture and project spaces, Michael must review this request to ensure proper access controls for staff-level personnel working on retail e-commerce initiatives.


## [25/43] Accepted: B2b discussion @ Mon Apr 6, 2026 2pm - 3pm (SGT) (Jazz Tong)
Source: gmail | Thread: 19d60c9b6f2aff29 | Labels: None | Priority: None | Senders: me | Last Date: Mon, Apr 6, 2026, 3:15 AM | Last Updated: 2026-04-06T09:39:59.420588+00:00
This is a system-generated calendar notification confirming that Michael Bui has accepted an invitation for a 'B2b discussion' meeting. The meeting was organized by Jazz Tong and is scheduled for Monday, April 6, 2026, from 2:00 PM to 3:00 PM SGT. Other attendees include Kyle Nguyen and Alvin Choo. The message provides Google Meet details and phone dial-in options. As this is an informational system response regarding a scheduled meeting where Michael is an attendee, it falls under the 'Informational' category of direct mention with a system-generated body.


## [26/43] Invitation: B2b discussion @ Mon Apr 6, 2026 2pm - 3pm (SGT) (Michael Bui)
Source: gmail | Thread: 19d60c25c835f548 | Labels: Inbox | Priority: None | Senders: Alvin Choo | Last Date: Mon, Apr 6, 2026, 3:07 AM | Last Updated: 2026-04-06T09:40:06.410000+00:00
A system-generated Google Calendar invitation for a 'B2b discussion' meeting scheduled for Monday, April 6, 2026, from 2:00 PM to 3:00 PM SGT. The meeting is organized by Jazz Tong and includes attendees Kyle Nguyen, Alvin Choo, and Michael Bui. The email contains the Google Meet link (meet.google.com/hok-cswr-cnw) and dial-in details. As a direct invitation requiring an RSVP, it falls under informational/medium relevance for Michael, necessitating a review of availability rather than immediate technical action or architectural decision-making.


## [27/43] Invitation: Postmortem: [P2] App icon showed seasonal design instead ... @ Mon Apr 6, 2026 3pm - 3:30pm (SGT) (Michael Bui)
Source: gmail | Thread: 19d60c1af41a24e6 | Labels: Inbox | Priority: None | Senders: Andin Eswarlal Raje. | Last Date: Mon, Apr 6, 2026, 3:06 AM | Last Updated: 2026-04-06T09:40:19.760662+00:00
Michael Bui received an automated calendar invitation for a Postmortem meeting regarding a P2 incident where the e-commerce app displayed a seasonal design instead of the correct icon. The meeting is scheduled for Monday, April 6, 2026, at 3:00 PM SGT (1 hour duration). Organizer Andin Eswarlal Rajesh has included Michael in the guest list alongside key stakeholders from Ecomm Product Development, Reliability Engineering, and DPD-Omni teams. A Google Meet link and a Postmortem Report document are provided for review prior to the session. As this is a system-generated invitation directly addressed to Michael requiring an RSVP response (Yes/No/Maybe) and involving his domain of e-commerce platform reliability, it warrants attention for scheduling confirmation.


## [28/43] [Dashboard Report] Retail Media - DD Dashboard | Mon 6 Apr 11:00AM +08
Source: gmail | Thread: 19d60bec530e19f3 | Labels: Inbox, Updates | Priority: None | Senders: Datadog HQ | Last Date: Mon, Apr 6, 2026, 3:03 AM | Last Updated: 2026-04-06T09:40:25.922359+00:00
Automated system-generated email from Datadog HQ sent to Michael Bui on April 6, 2026, at 11:03 AM. The message delivers a scheduled dashboard report titled 'Retail Media - DD Dashboard' covering the past three days of data metrics. As a Staff-level engineering leader responsible for Retail Media and Ad Technology architecture, this informational update aligns with Michael's domain expertise in monitoring and SLO tracking, though it requires no immediate action or decision.


## [29/43] Mohammed Miran requested access to your space
Source: gmail | Thread: 19d6088a3c73d81e | Labels: Inbox, Updates | Priority: None | Senders: Mohammed Miran | Last Date: Mon, Apr 6, 2026, 2:04 AM | Last Updated: 2026-04-06T09:40:33.014522+00:00
Mohammed Miran has requested access to the 'Project LIGHT' Confluence space. The notification was triggered automatically by Atlassian Confluence on April 6, 2026. As this is a system-generated request for permissions regarding a specific project workspace, it falls under medium relevance. While Michael Bui may need to review and approve this if he manages the Project LIGHT space or its access policies, there is no explicit indication in the thread that he owns this specific resource or has been directly assigned the task yet. The email requires action to manage the access request.


## [30/43] Daily Agenda for Michael Bui as of 5am
Source: gmail | Thread: 19d5f8e35c1f9faa | Labels: Inbox, Updates | Priority: None | Senders: Google Calendar | Last Date: Sun, Apr 5, 2026, 9:30 PM | Last Updated: 2026-04-06T09:40:39.978359+00:00
This is an automated daily agenda digest from Google Calendar sent to Michael Bui at 05:30 AM on April 6, 2026. It outlines a single scheduled event for the day: 'Monthly Webapp Scan' running from 12am to 8am, categorized under the 'Digital Business Tech Release/Changes' calendar. As a system-generated informational update providing Michael's schedule without requiring immediate action or decision-making, it falls into the low-to-medium relevance category.


## [31/43] Declined: ACNxOsmos: Daily Cadence @ Mon Apr 6, 2026 12:30pm - 1pm (SGT) (michael.bui@fairpricegroup.sg)
Source: gmail | Thread: 19d5f05bc6066c48 | Labels: Inbox | Priority: None | Senders: Rahul Jain | Last Date: Sun, Apr 5, 2026, 7:01 PM | Last Updated: 2026-04-06T09:40:49.915882+00:00
Michael Bui received a system-generated notification that the 'ACNxOsmos: Daily Cadence' meeting scheduled for Monday, April 6, 2026, at 12:30 PM SGT has been declined by organizer Rahul Jain. The invitation included an attachment titled 'FPG Project Plan 2905025'. While Michael was added as an optional participant (or guest) in the original invite, no direct action is currently required from him beyond acknowledging the status change of this vendor-led coordination meeting.


## [32/43] [Dashboard Report] Retail Media - DD Dashboard | Sun 5 Apr 11:00AM +08
Source: gmail | Thread: 19d5b97fdedf8d5d | Labels: Inbox, Updates | Priority: None | Senders: Datadog HQ | Last Date: Sun, Apr 5, 2026, 3:03 AM | Last Updated: 2026-04-06T09:40:55.857345+00:00
Michael Bui received an automated system-generated email from Datadog HQ containing a daily dashboard report titled 'Retail Media - DD Dashboard'. The message includes data covering the past three days (April 3–5, 2026). This communication falls under medium relevance as it is a scheduled informational update regarding monitoring metrics in Michael's domain of Retail Media. While Michael is explicitly tagged in the distribution list and owns governance for these services, the content is purely observational with no actionable items, escalations, or architecture decisions required at this time.


## [33/43] You have no events scheduled today.
Source: gmail | Thread: 19d5a6ad0efffc5b | Labels: Inbox, Updates | Priority: None | Senders: Google Calendar | Last Date: Sat, Apr 4, 2026, 9:34 PM | Last Updated: 2026-04-06T09:41:01.107805+00:00
Automated notification from Google Calendar confirming Michael Bui has no scheduled events for Sunday, April 5, 2026. This is a standard daily agenda digest sent to the michael.bui@fairpricegroup.sg account based on subscriptions to 'Digital Business Tech Release/Changes'. No human-written content or action required.


## [34/43] [Dashboard Report] Retail Media - DD Dashboard | Sat 4 Apr 11:00AM +08
Source: gmail | Thread: 19d56716fade7584 | Labels: Inbox, Updates | Priority: None | Senders: Datadog HQ | Last Date: Sat, Apr 4, 2026, 3:02 AM | Last Updated: 2026-04-06T09:41:07.053427+00:00
This is a system-generated email from Datadog HQ sent directly to Michael Bui on April 4, 2026. It serves as an automated delivery of the 'Retail Media - DD Dashboard' report, containing data aggregated over the past three days. As the sender explicitly addresses Michael but provides no action items or requires no decision, this falls under informational system-generated content with direct mention.


## [35/43] [RAW Overdue] Expired Risk Acceptance & Waiver Form
Source: gmail | Thread: 19d56038fde0ac6d | Labels: Inbox | Priority: None | Senders: cyberrisk.automation | Last Date: Sat, Apr 4, 2026, 1:02 AM | Last Updated: 2026-04-06T09:41:15.780561+00:00
This is an automated system-generated reminder regarding an expired Risk Acceptance & Waiver (RAW) form for the 'Signcloud Saas User access management' asset. The waiver ID RAW-20240306_01-v1.0 expired on May 15, 2025. Michael Bui is explicitly included in the recipient list (direct mention). While the email does not directly address him by name as an individual owner, his role involves setting and enforcing engineering governance standards, making compliance with risk waivers a relevant operational concern. The sender instructs the Requestor to either provide evidence of remediation or submit a new RAW form via Google Docs by following specific steps involving the Cybersecurity Risk Team (cyberRisk@ntucenterprise.sg) and Technology Governance team (techgrc@ntucenterprise.sg). No immediate human-written action is required from Michael, but this falls under medium relevance as it pertains to a governance artifact in his domain that may require oversight or validation.


## [36/43] You have no events scheduled today.
Source: gmail | Thread: 19d55488549f3608 | Labels: Inbox, Updates | Priority: None | Senders: Google Calendar | Last Date: Fri, Apr 3, 2026, 9:38 PM | Last Updated: 2026-04-06T09:41:20.731993+00:00
Automated system notification from Google Calendar informing Michael Bui that no events are scheduled for Sat Apr 4, 2026. This is a standard daily agenda digest with no action required.


## [37/43] Opsgenie Alert: [Datadog] [P2] [Warn] Service marketing-service has a high error rate on env:prod
Source: gmail | Thread: 19d523ef32e8f816 | Labels: Inbox, Updates | Priority: None | Senders: Opsgenie | Last Date: Fri, Apr 3, 2026, 5:40 PM | Last Updated: 2026-04-06T09:41:36.670102+00:00
Multiple automated Opsgenie alerts from Datadog triggered for the 'marketing-service' in production due to elevated error rates (threshold >5%). The service is part of the Retail Media domain. No human involvement or direct assignment detected.


## [38/43] Issue with Missing UBID
Source: gmail | Thread: 19d52fdf13c8b0bd | Labels: Inbox | Priority: None | Senders: Rahul, Nikhil, me | Last Date: Fri, Apr 3, 2026, 12:50 PM | Last Updated: 2026-04-06T09:41:45.755253+00:00
On April 3, 2026, vendor partner Rahul Jain (Osmos) flagged a critical data integrity issue in the retail media advertising pipeline. The vendor identified that the FairPriceGroup systems are not sending the required User Browsing ID (UBID) within the 'uclid' parameter during funnel impression events. Consequently, Osmos is assigning dummy UBIDs, which compromises tracking accuracy for display and product ads. Michael Bui directly responded to this escalation by requesting clarification on the definitions of UBID and uclid, the specific customer journey context, and the scope of impact (platform, page, ad type). Nikhil Grover also engaged to identify the specific ad units involved. This email constitutes a direct technical escalation requiring immediate architectural review and configuration correction to restore SLO compliance for impression tracking.


## [39/43] [Dashboard Report] Retail Media - DD Dashboard | Fri 3 Apr 11:00AM +08
Source: gmail | Thread: 19d514aa8123e26b | Labels: Inbox, Updates | Priority: None | Senders: Datadog HQ | Last Date: Fri, Apr 3, 2026, 3:02 AM | Last Updated: 2026-04-06T09:41:51.506635+00:00
An automated system-generated report titled 'Retail Media - DD Dashboard' was sent to Michael Bui by Datadog HQ on Friday, April 3, 2026, at 11:02 AM. The message contains a summary of data from the past three days regarding Retail Media metrics. As this is an informational dashboard report rather than a critical incident or action-required alert, it falls under medium relevance for monitoring trends without immediate intervention.


## [40/43] Re: Hyper stores visual - Advertima
Source: gmail | Thread: 19b6e85f67d0d448 | Labels: Inbox | Priority: None | Senders: Abdel-R., Rajkumar | Last Date: Fri, Apr 3, 2026, 2:44 AM | Last Updated: 2026-04-06T09:42:12.262595+00:00
This email thread documents the management of a retail digital advertising campaign with vendor Advertima for Hyper stores. Rajkumar Romendro coordinates visual uploads, campaign scheduling, and technical specifications with Advertima representatives (Jan Plojhar, Simone Pici, Christian Bahrendt). Key activities include deploying CNY-themed visuals, managing GWP campaigns, resolving technical asset rejections due to incorrect frame rates or resolutions, and handling urgent requests for specific ad slots which were denied due to system limitations. The thread covers the full lifecycle from content submission to live status verification and campaign termination. While Michael Bui is not explicitly mentioned (indirect involvement via distribution list), this represents a critical operational domain (Retail Media/Ad Tech) where he sets governance standards, reviews technical protocols, and manages vendor relationships.


## [41/43] Updates to Notion’s Terms
Source: gmail | Thread: 19d50f4f7945d100 | Labels: Inbox, Updates | Priority: None | Senders: Notion Team | Last Date: Fri, Apr 3, 2026, 1:28 AM | Last Updated: 2026-04-06T09:42:16.907093+00:00
Notion Team sent an automated notice regarding updates to their Terms and Master Subscription Agreement. The changes include new credit requirements for Notion Custom Agents effective May 4, 2026, with the updated terms taking effect May 1, 2026. No immediate action is required from Michael Bui.


## [42/43] You have no events scheduled today.
Source: gmail | Thread: 19d5013cda0bfcf5 | Labels: Inbox, Updates | Priority: None | Senders: Google Calendar | Last Date: Thu, Apr 2, 2026, 9:22 PM | Last Updated: 2026-04-06T09:42:21.629524+00:00
System-generated notification indicating no events are scheduled for Michael Bui on Friday, April 3, 2026. The message is an auto-agenda digest from Google Calendar regarding the 'Digital Business Tech Release/Changes' calendar.


## [43/43] Simplifying Jira's create experience
Source: gmail | Thread: 19d4f67520258079 | Labels: Inbox, Updates | Priority: None | Senders: Atlassian | Last Date: Thu, Apr 2, 2026, 6:14 PM | Last Updated: 2026-04-06T09:42:33.005345+00:00
Atlassian is rolling out an improved Jira 'create' experience starting in late April 2026. The update simplifies the default form to show only essentials (summary, description, required fields, and a few optional fields) while retaining a full-form option for complex needs. Existing configurations like validation rules and workflows remain intact. As an Admin, there is no immediate action required; however, toggles exist to force the full-form layout if preferred. This falls under informational updates about tools Michael oversees but does not directly own or require intervention from.
