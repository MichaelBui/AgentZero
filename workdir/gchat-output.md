

## [1/48] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 16 | Last Activity: 2026-04-02T10:33:16.786000+00:00 | Last Updated: 2026-04-02T10:44:56.500221+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (Updated April 2, ~10:33 UTC)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
A persistent wave of cyclical instability continues into the late morning of April 2 (approx. 10:14–10:33 UTC), extending the critical window started on April 1. The incident involves recurring latency spikes and error rate cycles in Identity (`engage-my-persona-api-go`), Personalization/Launchpad (`frontend-gateway`, `orchid`), Store Check-ins, and Mobile App services.

**Status Summary & Timeline (Updated: ~10:33 UTC)**
*   **Identity API Instability (`engage-my-persona-api-go` / Squad Dynamics):**
    *   *Latency:* Cyclical p90 latency spikes observed for `post_/new-myinfo/confirm`. Recovered briefly at 10:17, then triggered again at **10:21 UTC** (1.978s), recovering at **10:25 UTC**.
    *   *Residential Address:* New latency trigger for `put_/user/residential-address` observed at **10:14 UTC** (p90: 1.949s), recovered by **10:16 UTC** (1.159s).
    *   *Error Rate:* High error rate triggered at **10:14 UTC** (Value: 0.094).
    *   *Verify User Data:* Severe success rate degradation observed at **10:16 UTC** (75.0%), recovered by **10:26 UTC**.
*   **Recommendation & Frontend Services (`squad:journey`):**
    *   *Home Page Latency:* P90 latency exceeded threshold for `get_/api/layout/home/v2` at **10:17 UTC** (1.406s), recovered by **10:18 UTC**.
    *   *Orchid Failures:* Success rate dipped below 99.9% at **10:33 UTC** (Value: 99.862%). Brief recovery at 10:19 UTC.
    *   *Boughtbought Latency:* P99 latency spike observed for `get_/api/recommender/boughtbought` at **10:28 UTC** reaching **2.04s**.
*   **Store Operations:**
    *   *Scan & Go Check-ins:* Success rate dropped to **98.718%** at **10:22 UTC**, recovered by **10:32 UTC**.

**Pending Actions & Ownership**
*   **Investigate Identity API Correlation (Critical):** Analyze recurring latency spikes (>1.8s) on `post_/new-myinfo/confirm` and `put_/user/residential-address`. Investigate the severe 75% success rate drop on `post_/new-myinfo/verify` at 10:16 UTC. Owner: **Squad Dynamics**.
*   **Diagnose Recommendation & Frontend:** Address Orchid failures (99.862%), P99 latency spikes for `boughtbought`, and Home Page V2 latency. Owner: **Squad Journey**.
*   **Monitor Store Stability:** Continue tracking Scan & Go check-in success rates following the 10:22 UTC dip. Owner: **Squad Journey**.

**Decisions Made**
*   **Status Update:** Incident severity remains Critical due to continuous, cyclical failures across Identity, Recommendation, and Store services extending from April 1 afternoon through the current morning window (10:33 UTC).
*   **Pattern Confirmation:** The recurrence of latency exceeding thresholds for `new-myinfo/confirm`, `residential-address`, and the newly observed severe failure in `verify user data` requests confirms a persistent instability cycle affecting multiple squads simultaneously.

**Key Dates & Follow-ups**
*   **Active Window:** April 1, 09:58 – April 2, 10:33 UTC (Latest Critical Activity).
*   **Reference Links (Latest):**
    *   `engage-my-persona-api-go` Error Rate Monitor #92965074 (Triggered: 10:14 UTC, Value: 0.094)
    *   `put_/user/residential-address` Latency Monitor #17447643 (Triggered: 10:14 UTC, Value: 1.949s)
    *   `post_/new-myinfo/verify` Success Rate Monitor #17447667 (Triggered: 10:16 UTC, Value: 75.0%)
    *   `get_/api/layout/home/v2` Latency Monitor #17448324 (Triggered: 10:17 UTC, Value: 1.406s)
    *   `post_/new-myinfo/confirm` Latency Monitor #50879027 (Triggered: 10:21 UTC, Value: 1.978s)
    *   `get_/api/recommender/orchid` Success Rate Monitor #17448311 (Triggered: 10:33 UTC, Value: 99.862%)


## [2/48] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw | Messages: 2 | Last Activity: 2026-04-02T10:02:59.061000+00:00 | Last Updated: 2026-04-02T10:45:45.714635+00:00
**Daily Work Briefing: Digital Product Development (DPD)**

**Key Participants & Roles**
*   **Flora Wo Ke:** Team Lead.
*   **Alvin Choo:** Developer/QA.
*   **Nicholas Tan:** DevOps/Infrastructure.
*   **Tiong Siong Tee / Andin Eswarlal Rajesh:** QA/Engineering (iOS).
*   **Winson Lim:** Engineering Lead/Strategy.
*   **Natalya Kosenko:** DevOps/SRE.
*   **Boning He / Gopalakrishna Dhulipati:** Team Members.
*   **Kyle Nguyen:** Team Member.
*   **Maou Sheng Lee:** Team Member.
*   **Jazz Tong:** Incident Coordinator.
*   **Akash Gupta:** Support Lead.
*   **Vivian Lim Yu Qian:** Staff Verification Specialist.
*   **Mohammad Adyatma:** Team Member (Security).
*   **Wai Ching Chan:** Team Member.

**Main Topics & Discussions**
1.  **FPPay Production Issue:** On March 30, 2026 (09:11 UTC), Andin Eswarlal Rajesh reported FPPay banner images failing to load in production. Activity continues with 25+ replies.
2.  **Staff Verification Logic:** Vivian Lim Yu Qian queried app screens for staff verification during SKU purchases requiring force verification (e.g., milk powder). The team is validating compliance against existing protocols.
3.  **Incident Management Response:** Earlier on March 27, Jazz Tong raised an urgent query regarding a potential incident ("it is incident?"). The team mobilized support for the DPD Incidents channel involving Gopalakrishna Dhulipati, Akash Gupta, and Kyle Nguyen.
4.  **Infrastructure & Operations Risk:** Nicholas Tan flagged risks regarding Broadcom ending free Bitnami images, causing `kubectl` image tag failures and increased Time To Recovery (TTR) impacting the Golden Pipeline (GP).
5.  **Payment Service Issues:** Alvin Choo reported promo code redemption failures in FP Pay; confirmed that a change freeze has ended and feature releases are proceeding.
6.  **Mobile Quality Assurance:** Andin Eswarlal Rajesh previously identified an iOS FPPay bug where QR codes load without user login, escalated via file download.
7.  **Datadog Governance:** Natalya Kosenko reported unauthorized manual changes to Datadog On-Call teams (removals of Maxine, Arijit, Minu). Terraform manages this config; manual console edits are overwritten on the next run.
8.  **Strategic Planning & Tooling:** Winson Lim highlighted data centers as potential targets in modern warfare (Iran conflict context) to inform Disaster Recovery (DR) scenarios and noted Reforge joined Miro to bridge strategy and delivery gaps.
9.  **AI Engineering Learning:** On March 30, 2026 (23:25 UTC), Winson Lim shared a GitHub repository (`affaan-m/everything-claude-code`) as a resource for learning AI-first engineering patterns and reusable skills.
10. **Security Alert (NPM):** On March 31, 2026 (04:38 UTC), Mohammad Adyatma flagged the compromise of the `axios` npm package via `https://socket.dev/blog/axios-npm-package-compromised`. Immediate review of dependencies is required.
11. **Bonus Communication:** On April 1, 2026 (13:51 UTC), Wai Ching Chan initiated a discussion regarding "FPG Bonus" with 2 replies. A YouTube link (`https://youtu.be/dQw4w9WgXcQ?si=xUc5b9AlRJE4gCah`) was shared in the thread.
12. **Social Events:** Kyle Nguyen announced an upcoming DPD BBQ ("We come first"). Boning He and Gopalakrishna Dhulipati shared snacks; Maou Sheng Lee expressed sentiment regarding energy waste on March 18.
13. **Employee Code of Conduct Update:** On April 2, 2026 (10:02 UTC), Alvin Choo circulated a critical update to the Employee Code of Conduct via NTUC Enterprise Mail (`Important Updates to the Employee Code of Conduct.pdf`), urging all staff to review for doubts.

**Pending Actions & Owners**
*   **FPPay Image Team (Andin Eswarlal Rajesh, DevOps):** Investigate root cause of banner image loading failures in production and deploy fix. Priority: High.
*   **S&G Verification Team (Vivian Lim Yu Qian, Product/Dev Teams):** Investigate current S&G flows against the WIP verification logic document to confirm if forced staff verification screens exist for restricted SKUs like milk powder. Reference: `https://ntuclink.atlassian.net/wiki/spaces/SE/pages/1995997683/WIP+S+G+Verification+Flow`.
*   **Incident Response Team (Jazz Tong, Akash Gupta, Gopalakrishna Dhulipati, Kyle Nguyen):** Act as support guides for the active DPD Incidents channel; monitor and resolve incoming incident queries.
*   **GP Team (Nicholas Tan / Mohit Niranwal):** Investigate Bitnami image replacement strategy to resolve TTR issues and update Golden Pipeline dependencies.
*   **iOS/Dev Team (Tiong Siong Tee):** Re-verify the previously identified iOS FPPay QR code login bypass bug status.
*   **Security Team (Mohammad Adyatma, All Devs):** Audit all projects for `axios` dependency versions to mitigate risks associated with the reported npm package compromise. Reference: `https://socket.dev/blog/axios-npm-package-compromised`.
*   **FPG Bonus Discussion (Wai Ching Chan):** Review details regarding FPG bonus distribution and linked content.
*   **All Staff:** Review the "Important Updates to the Employee Code of Conduct" PDF shared by Alvin Choo on April 2, 2026; raise any doubts immediately.

**Decisions Made**
*   No formal change freeze; feature releases are currently active (Alvin Choo).
*   Datadog team configurations must strictly follow Infrastructure as Code (Terraform) protocols; manual overrides are deprecated.
*   Miro's acquisition of Reforge is recognized as a strategic move to bridge product strategy and delivery gaps.
*   **New:** Active incident support protocol established for Jazz Tong, Akash Gupta, Gopalakrishna Dhulipati, and Kyle Nguyen on March 27, 2026.
*   **New:** Winson Lim endorsed the `affaan-m/everything-claude-code` repository as a key resource for AI-first engineering patterns and skill development.
*   **New:** Mandatory review of updated Employee Code of Conduct (April 2, 2026) initiated by Alvin Choo; staff must clarify doubts with management.

**Key Dates & Follow-ups**
*   **Apr 2, 2026 (10:02 UTC):** Alvin Choo distributed critical Employee Code of Conduct updates.
*   **Apr 1, 2026 (13:51 UTC):** Wai Ching Chan initiated FPG Bonus discussion; video shared.
*   **Mar 31, 2026 (04:38 UTC):** Mohammad Adyatma flagged `axios` npm package compromise; security audit initiated.
*   **Mar 30, 2026 (23:25 UTC):** Winson Lim shared AI engineering resource repo.
*   **Mar 30, 2026 (09:11 UTC):** Andin Eswarlal Rajesh flagged FPPay banner image loading failure in prod; discussion ongoing (25+ replies).
*   **Mar 27, 2026 (03:03 UTC):** Jazz Tong flagged potential DPD incident; support team mobilized.
*   **Mar 27, 2026 (08:11 AM):** Vivian Lim Yu Qian raised S&G verification flow query; discussion concluded with 12 replies.
*   **Mar 26, 2026:** Winson Lim shared Reforge joining Miro.
*   **Mar 25, 2026:** Natalya Kosenko highlighted DPD alumni participation in a Google AI event.
*   **Mar 18, 2026:** Maou Sheng Lee noted sentiment regarding wasted energy.

**Social Notes**
*   Upcoming DPD BBQ announced by Kyle Nguyen ("We come first, see you!").


## [3/48] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/9KYZsmc-670 | Messages: 20 | Last Activity: 2026-04-02T10:02:11.714000+00:00 | Last Updated: 2026-04-02T10:46:03.489055+00:00
**Daily Work Briefing: S&G Store Enablement Discussion (Updated)**

**Key Participants & Roles**
*   **Daryl Ng:** Digital Product Development (Inquiry lead, capacity planning).
*   **Sneha Parab:** Digital Product Development / SME (Process owner, technical implementation).
*   **David:** Action Owner (Ticket submission/assignment).
*   **Hanafi:** Ticket Processor.

**Main Topic**
Assessment of effort and timeline for a temporary "Pop-up S&G" store setup at Jewel. Discussion focused on verifying SOPs, identifying dependencies, and finalizing the request workflow.

**Decisions Made**
*   **Documentation:** The previously cited SOP is outdated. The team agreed to utilize Hanafi's automated process, referencing version 3.0 of the store setup doc or the new Jira form.
*   **Workflow Confirmation:** While SAP handles master data downloads directly to GCS, DPD must still create the store in DBP and coordinate with the DE team for search/browse data flow upon receiving Stock on Hand (SOH).
*   **Timeline Estimate:** End-to-end lead time is estimated at approximately 2 weeks.

**Pending Actions & Ownership**
1.  **Submit Request Ticket:**
    *   **Owner:** David.
    *   **Status:** **Completed.** The request was submitted via the new Jira form to accommodate the team's workload starting next week.
    *   **Reference Form:** https://ntuclink.atlassian.net/jira/core/projects/STOR/form/577
2.  **Ticket Assignment:**
    *   **Owner:** David / Daryl Ng.
    *   **Action:** **Completed.** As of April 2, 2026, the ticket has been assigned to **Hanafi** for processing.
    *   **Update:** This action supersedes previous pending assignments; no further assignment is required at this stage.
3.  **Stakeholder Coordination:**
    *   **Owner:** Daryl Ng / Brendon.
    *   **Action:** Confirm with Brendon regarding awareness of this specific request and ensure proper handover if he is not the originator.

**Key Dates & Follow-ups**
*   **Event Timeline:** The pop-up store event is likely to occur approximately 3 weeks from April 1, 2026.
*   **Current Date:** April 2, 2026.
*   **Capacity Check:** Request submission was prioritized immediately to prevent delays given the team's increased workload starting next week.

**Reference Links**
*   Outdated SOP: https://ntuclink.atlassian.net/wiki/spaces/SE/pages/1995999558/S+G+Store+Enabling+-+SOP
*   Current Setup Doc (v3.0): https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008160308/Store+setup+doc+v3.0


## [4/48] RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU/PYIHH8s-2LQ | Messages: 6 | Last Activity: 2026-04-02T09:54:24.246000+00:00 | Last Updated: 2026-04-02T10:46:21.723634+00:00
**Daily Work Briefing: RMN Leadership Space**

**Key Participants & Roles**
*   **Bryan Choong:** Team Leader/Sender of directive.
*   **Allen Umali:** Team Member/Respondent (completed initial task).
*   **Christopher Yong:** Team Member (inquired and confirmed compliance).
*   **Rajiv:** Subject matter contact (initiated the request).
*   **Wendi:** Team member whose acknowledgement was shared by Christopher.
*   **Wilson:** Source of relevant message on MT chat.
*   **@all:** The broader team audience addressed in the message.

**Main Topic**
The conversation concerns urgent updates to the **Employee Code of Conduct**. Leadership is emphasizing a shift in compliance posture and mindset, requiring explicit acknowledgement from all team members regarding these new updates.

**Pending Actions & Ownership**
*   **Action:** Review HR email and Wilson's MT chat message for Code of Conduct updates; provide explicit acknowledgement.
*   **Owner:** Team members (specifically those who missed the initial notification).
*   **Status Update:** Christopher Yong confirmed completion ("Done") at 09:45 UTC on April 2, 2026, by sharing Wendi's acknowledgement.

**Decisions Made**
No new policy decisions were made. The discussion clarified that the directive originated from Rajiv and was disseminated via a specific HR email and a message from Wilson on MT chat. Immediate, explicit acknowledgement is required to satisfy organizational compliance protocols.

**Key Dates & Deadlines**
*   **Date:** April 2, 2026.
*   **Deadlines:**
    *   Initial deadline: "Within the day" (set at 02:37 UTC).
    *   Allen Umali confirmed completion: 03:42 UTC.
    *   Christopher Yong confirmed completion: 09:45 UTC.

**Summary of Flow**
1.  **02:37 UTC:** Bryan Choong notified the team that Rajiv initiated a request for explicit acknowledgement regarding Employee Code of Conduct updates, noting only one response was received. He set a deadline for the same day.
2.  **03:42 UTC:** Allen Umali confirmed completion ("Done").
3.  **09:16 UTC:** Christopher Yong apologized for missing the initial notification and asked if the request was via email, quoting Bryan's original instruction.
4.  **09:17 UTC:** Bryan Choong confirmed it was via email and directed the team to check Wilson's message on MT chat alongside the HR email.
5.  **09:45 UTC:** Christopher Yong confirmed he had read the email and Code of Conduct, sharing Wendi's acknowledgement as proof of completion.

**Reference Data**
*   **Space URL:** https://chat.google.com/space/AAAAQQGZSZU
*   **Sources:** HR Email (Code of Conduct updates), Wilson's message on MT chat.


## [5/48] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-04-02T09:54:11.461000+00:00 | Last Updated: 2026-04-02T10:47:04.712475+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Update)**
**Date:** April 2, 2026 (Morning Shift)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 904

### Main Topic
Instability persists across `frontend-gateway` and `st-cart-prod`. Following the critical burst at 06:14–06:20 UTC, activity has shifted to intermittent latency spikes in **Wish List operations** (PUT/GET) and a **recurring Cart Update trigger**. The system shows cyclic degradation rather than continuous failure.

### Incident Timeline & Actions
**Previous Context:**
*   *Extended activity from March 20 through late March 31.*
*   *April 2 (04:55 – 06:26 UTC):* Critical burst affecting Cart/Checkout; all monitors recovered by 06:26 UTC.

**New Activity (Post-Recovery, April 2)**
*   **06:46 – 07:00 UTC:** Brief instability in `post /api/cart` and `get /api/wish-list/{_id}`.
    *   **Cart Update P99:** Triggered at 06:46 (3.101s), recovered by 06:50 (1.918s).
    *   **Wish List GET P90:** Triggered at 07:00 (2.04s), recovered by 07:01 (1.694s).
*   **07:45 – 09:54 UTC:** Persistent, cyclic latency in `put /api/product/{_id}/wish-list`.
    *   **07:45 Trigger:** P99 spiked to **7.389s** (Threshold >6s). Recovered by 08:01.
    *   **09:11 Cluster:** Simultaneous triggers on `put` P99 (**7.985s**) and `put` P90 (**5.336s**). Both recovered by 09:21/09:48.
    *   **09:46 – 09:54:** Rapid re-triggering of `put` P90 (peaking at **5.015s**), recovering and re-triggering within minutes until final recovery at 09:54.

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** The pattern has evolved from a systemic cart/checkout failure to a **cyclic Write operation degradation** specifically on Wish List updates (`put /api/product/{_id}/wish-list`).
*   **Immediate Action Required:** Investigate resource contention or database locks driving the 09:11 and 09:46–09:54 spikes. The recurrence suggests a non-transient issue (e.g., connection pool exhaustion or lock wait) rather than transient load.

### Decisions Made
*   **Priority Status:** Remains **"Critical Incident"**. While the severe Checkout failure window has passed, the return of high-latency triggers on Wish List and Cart Update endpoints prevents full resolution.
*   **Focus Shift:** Immediate attention must realign to the `put /api/product/{_id}/wish-list` recurrence (Monitors: `21245701`, `21245706`). The error budget consumption rate necessitates an urgent SLA resolution.
*   **Metric Update:** New highest recorded values in this session:
    *   `put /api/product/{_id}/wish-list` P99: **7.985s** (09:11 UTC).
    *   `put /api/product/{_id}/wish-list` P90: **5.336s** (09:11 UTC).

### References
*   **Active Monitors:** `21245701` (Wish List PUT P99), `21245706` (Wish List PUT P90), `21245720` (Wish List GET P90), `21245713` (Cart Update P99).
*   **SLO Monitor:** `8569058961838035695`.
*   **Service Tags:** `service:frontend-gateway`, `team:dpd-pricing`.


## [6/48] FPG Everyone - General
Source: gchat | Group: space/AAAAjDYVcBU | Messages: 4 | Last Activity: 2026-04-02T09:09:29.579000+00:00 | Last Updated: 2026-04-02T10:47:42.929754+00:00
**Daily Work Briefing: FPG Everyone Chat Summary (Updated)**
**Date Range:** March 3 – April 2, 2026
**Source:** Google Chat (FPG Everyone - General)

### Key Participants & Roles
*   **Serene Kua Puay Leng:** Promotes daily product deals and lobangs.
*   *(Previous participants retained: Siti Nabilah, Jasmine Neo, Keith Lee, Melissa Lim, Maisy Heeng, Si Min Ng)*

### Main Topics
1.  **Digital Access Rollout:** Completed as of Mar 30; user guide distributed.
2.  **Media Collaboration – "Bowl of Love":** Final episodes featuring Tyler Ten, Tasha Low, and Xiang Yun are live (Mar 21 launch). Focuses on warmth/healing with fresh Malaysian pork via @mediacorp.re.dian TikTok.
3.  **Industry Recognition:** Lau Pa Sat's "Spin for your Huat" featured by Campaign Asia as a top CNY 2026 campaign alongside Nike and Apple.
4.  **FairPrice Heartland Hits Launch (Mar 27):** Community storytelling contest (#FPHeartlandHits, #FPNorthie). Incentive: $50 E-Vouchers + song feature. Deadline: April 5, 2026.
5.  **Unity Wellness Promotions:** B1G1 offer on health/wellness (Mar 26–29) at Unity stores. Featured brands include Moom Health and Elastine.
6.  **Kopitiam Food Hall & Shabu Days Launch (Apr 3):** Confirmed launch of the brand-new Kopitiam Food Hall at Hillion Mall tomorrow (April 3). Features 25 F&B stalls, 14 halal-certified options, and the debut of **Shabu Days** ("Your Personal Shabu Treat Ritual"). Opening weekend includes live performances and exclusive swag.
7.  **Linkpoints Loyalty Promo ($0.99):** Redemption active for FairPrice Maple Syrup Cashews and Myojo Bowl Noodles. Collection deadline: April 5, 2026.
8.  **New Product Promo – Delicato Sausages:** Deal on Japanese-style sausages (Curry & Bonito Seaweed) at $3.95/packet until April 15, 2026.
9.  **Promotional Launch – KitKat F1 Pack (Apr 1):** Darren Goh announced the "Ready, Set, Break!" campaign. Exclusive to FairPrice, Cheers, and FairPrice Online. Price: $29.95; Contents: 2 KitKat 10s Sharebags + 1 KitKat & F1 Flask.

### Pending Actions & Ownership
*   **Shorty Awards Voting (Owner: All Staff):** Vote daily for *Bridge to Equity* and *2025 End-Of-Year Unpacked*. Deadline: **April 8**.
*   **Linkpoints Redemption (Owner: All Staff):** Redeem $0.99 rewards. Collection deadline: **April 5, 2026**.
*   **Easter Outreach @ Sunlove Abode (Owner: All Staff):** Join "Protein Pledge" Day of Service on **Thursday, April 9** (10:30 AM – 12:30 PM). Activities include Easter Bingo, serving buffet lunch to seniors, and egg distribution. Sign up here: `https://forms.gle/Y4B22gtUmU7SF42V6`.
*   **Volunteer Engagement:** Sign up via `https://forms.gle/UkyQDagmDy4mcY7K7`. "Willing Hearts Kitchen Crew" is fully booked.
*   **Sensory Test Sign-ups:** Chapati screening form open (`https://forms.gle/DFYrahZcvhtcoJ9R7`). Frozen Snacks sign-up closed.
*   **Delicato Sausage Trial (Owner: All Staff):** Encouraged purchase during promo through April 15 for instant meal upgrade.

### Decisions Made
*   **Awards Campaign:** Mobilization approved for Shorty Awards voting.
*   **Wellness Extension:** Unity B1G1 offer extended (Mar 26–29).
*   **Loyalty Initiative:** $0.99 redemption launched with specific SKUs.
*   **Brand Expansion:** Kopitiam Food Hall and Shabu Days launch confirmed for April 3 at Hillion Mall.
*   **Product Promotion:** Delicato sausage promo activated through April 15.
*   **Promotional Campaign:** KitKat F1 Flask Pack activation approved for exclusive retail distribution starting April 1, 2026.

### Critical Dates & Deadlines
*   **April 3:** Kopitiam Food Hall & Shabu Days launch (Hillion Mall).
*   **April 5:** Heartland Hits contest closes; Linkpoints redemption collection ends.
*   **April 8:** Shorty Awards voting deadline.
*   **April 9:** Easter Day of Service at Sunlove Abode (10:30 AM – 12:30 PM).
*   **April 15:** Delicato Japanese-style sausage promo expires.


## [7/48] ❗ Important Email
Source: gchat | Group: space/AAQAUJW8HMo | Messages: 6 | Last Activity: 2026-04-02T09:00:39.963000+00:00 | Last Updated: 2026-04-02T10:48:14.972706+00:00
**Daily Work Briefing Summary (Updated)**

**Key Participants & Roles**
*   **Michael Bui (You):** Managing Osmos support, event RSVPs, FileVault compliance, performance feedback, Project Light coordination, AI training follow-ups, GCP Service Account security, D&T Power Breakfast engagement, and Internal Talent Marketplace exploration.
*   **HR / FairPrice Group:** Expanded the Internal Talent Marketplace to include Corporate/HQ Non-Executive and Frontline Executive staff.
*   **TPA (ta@fairpricegroup.sg):** Point of contact for Internal Mobility programme queries.

**Main Topics**
1.  **GCP Security & Service Account Decommissioning:**
    *   **Objective:** Clean up legacy keys; focus on non-production (56 keys) and automated rotation.
    *   **Timeline:** Kyle Nguyen's team begins remediation week of March 30, 2026.

2.  **AI Training & Agentic Evolution Contest:**
    *   **Weekly Support:** Google AI Specialists hosting Wednesdays, 2:00–2:30 PM SGT (Mar 25 – May 31, 2026).
    *   **Contest:** Launched by FPG AI CoE & Google. Submissions due **April 25, 2026**.

3.  **DPD AI Guild Committee Monthly Meeting:**
    *   **Status:** Recurring first Tuesday, 10:00–10:50 AM SGT. Organizer: Michael Bui.
    *   **Location:** FairPrice Hub-11-L11 Room 10 (6) + Google Meet (`zhj-udzb-apd`).
    *   **Note:** Jazz Tong has declined the recurring invitation.

4.  **DPD, Core Product & Picking Teams Meeting:**
    *   **Event:** Thursday, April 2, 2026, 9:30–11:00 AM SGT (FairPrice Hub-13-L13 Heritage Room + Meet `mgv-sdor-ejt`).

5.  **D&T Power Breakfasts:**
    *   **Upcoming Event:** Tuesday, April 28, 2026, 9:00–10:30 AM SGT (Hub Level 11 Lobby B). Monthly on last Thursday hosted by Trina Boquiren.

6.  **BCRS & Project Light:**
    *   **Events:** RMN Discussion (Mar 26, 2:00 PM) and BCRS Regroup (Mar 26, 4:00 PM). Scheduling conflict noted.

7.  **Internal Talent Marketplace Expansion (New):**
    *   **Announcement:** Expanded April 2, 2026, to include Corporate/HQ Non-Executive and Frontline Executive staff.
    *   **Eligibility:** Min tenure of 2 years (Grade S/D) or 3 years (Grade C+); Green rating in last 2–3 years; no PIP/disciplinary actions in last 2–3 years. New role grade must match current grade.

**Pending Actions & Ownership**
*   **GCP Security Consent (Michael Bui):** Review legacy SA spreadsheet and indicate consent for automated rotation immediately.
*   **DPD/Core Product/Picking Meeting RSVP (Michael Bui):** Respond to April 2 invitation.
*   **Agentic Evolution Contest (Michael Bui):** Submit entry by **April 25, 2026**.
*   **Power Breakfast RSVP (Michael Bui):** Confirm "Yes" by **April 24** for April 28 event.
*   **BCRS & RMN Meetings (Michael Bui):** Confirm attendance for March 26 sessions; note conflict between 2:00 PM and 4:00 PM slots.
*   **Internal Talent Marketplace Exploration (Michael Bui):** View step-by-step guide and explore opportunities on the [myTalentHub portal]. Contact `ta@fairpricegroup.sg` for clarifications.

**Decisions Made**
*   **Agentic Evolution Contest:** Winners receive Google gear; focus on eliminating toil.
*   **Internal Mobility:** Greater cross-functional mobility encouraged between HQ and Frontline staff.
*   **GCP Remediation Priority:** Legacy key cleanup is highest priority; weekly status updates to follow via dedicated Google Group.

**Critical Dates & Deadlines**
*   **Mar 18, 2026:** Performance Feedback Meeting.
*   **Mar 25–May 31, 2026:** Weekly AI Workbench Sessions (Wednesdays).
*   **Mar 26, 2026:** RMN Discussion (2:00 PM) & BCRS Regroup (4:00 PM).
*   **Mar 30, 2026:** GCP Key Removal activities begin.
*   **Apr 2, 2026:** DPD/Core Product/Picking Joint Meeting; Internal Talent Marketplace officially expanded.
*   **Apr 24, 2026:** Deadline to RSVP for D&T Power Breakfast.
*   **Apr 25, 2026:** Agentic Evolution Contest Submission & FileVault Final Deadline.
*   **Apr 28, 2026:** D&T Power Breakfast (9:00 AM SGT).


## [8/48] [Prod Support] Ecom FFS Ops
Source: gchat | Group: space/AAAAde_cYKA | Messages: 4 | Last Activity: 2026-04-02T08:49:43.823000+00:00 | Last Updated: 2026-04-02T10:48:49.134249+00:00
**Daily Work Briefing: [Prod Support] Ecom FFS Ops (Updated Apr 2)**

**Key Participants & Roles**
*   **Wai Ching Chan / Sampada Shukla:** Operations/Product Leads.
*   **TL HCBP FFS / TL - HGPT FFS:** Store Leads reporting picking queue blockages and SOH anomalies.
*   **Adrian Yap Chye Soon:** Technical Lead/Support (investigating data anomalies, dispatcher app failures, and packlist issues).
*   **Akash Gupta:** DPD / Fulfilment / On Call.
*   **Yoongyoong Tan:** Reporting HCBP picking Q issues.
*   **Ler Whye Ling Angel:** Escalation point for "No picking Q."

**Main Topics**
1.  **Packlist & SOH Discrepancies (Expanded):** Ongoing investigation into critical `packed_qty` anomalies and Stock on Hand (SOH) NULL values across multiple sites.
    *   **New Critical Incident (Apr 2, ~08:49 AM):** Sampada Shukla flagged a new anomaly at **Hyper Changi (Store ID 45)**. Order #23013763 shows Packlist status as `RECEIVED` but `packed_quantity` is `NULL`.
    *   **Ongoing Critical Incidents:**
        *   **Hyper Changi (Store ID 45) - Mar 29:** Order #22972590 showed `packed_qty` of 90,203,969 vs. `delivered_qty` of 2 ($19.95 MRP/$39.9).
        *   **VivoCity - Mar 26:** Orders #22912255/#22906879 with ~13M discrepancy.

2.  **Dispatcher App & Zone Scanning Failure (Mar 28):** Escalation regarding the dispatcher app's inability to scan new zones at **hvivo**.
    *   **Status:** Reported 01:45 AM Mar 28; Adrian Yap Chye Soon provided video evidence for review; technical investigation remains active.

3.  **HCBP Picking Queue Issues (Mar 27):** Escalated urgency regarding "No picking Q" blockage and T18 display failures.
    *   **Status:** Initial blockage reported 02:08 AM; escalated by Ler Whye Ling Angel at 02:52 AM; T18 data failure reported by TL HCBP FFS at 07:47 AM.

**Pending Actions & Ownership**
*   **Data Validation (Urgent - Apr 2):**
    *   *@Adrian Yap Chye Soon:* Immediate investigation into Order #23013763 (Hyper Changi) where Packlist status is `RECEIVED` but `packed_quantity` is `NULL`.
    *   *@Akash Gupta / On Call:* Continue validation of SOH NULL values for bulk orders at **HGPT** (Mar 31 incident).
    *   *@Wai Ching Chan @Sampada Shukla:* Prioritize review of the new Hyper Changi anomaly alongside pending validations for Sun Plaza, VivoCity, and HGPT.
*   **Dispatcher App Investigation:**
    *   *@Adrian Yap Chye Soon / Technical Team:* Continue RCA on "unable to scan new zone" failure at hvivo based on video evidence.
*   **HCBP Queue Investigation:**
    *   *@Adrian Yap Chye Soon / @Gopalakrishna Dhulipati:* Monitor resolution of Mar 27 "No picking Q" and T18 display failures following escalations by Ler Whye Ling Angel.

**Decisions Made**
*   **App Release Strategy:** Picker App 10.4.0 rollout remains on hold pending resolution of critical data anomalies (Mar 18–Apr 2). Full rollout is contingent on stability post-fixes, specifically addressing:
    *   The newly discovered Apr 2 Hyper Changi `packed_quantity` NULL issue (Order #23013763).
    *   The Mar 31 HGPT SOH NULL issue.
    *   The Mar 29 Hyper Changi anomaly (Order #22972590).
    *   The resolved/pending Mar 26 VivoCity alerts.
    *   The resolved/pending Mar 27 HCBP queue/T18 failures.
    *   The new dispatcher app zone scanning issue at hvivo.

**Key Dates & Deadlines**
*   **Immediate:** Investigation of Apr 2 Hyper Changi `packed_quantity` NULLs and RCA for Mar 28 Dispatcher App failure at hvivo. Also urgent validation of Mar 31 HGPT SOH NULLs and Mar 29 Order #22972590.
*   **Pending:** Comprehensive RCA for recent anomalies across Sports Hub, VivoCity, Parkway, Changi, Sun Plaza, Hyper VivoCity, Hyper Changi, and the new HGPT site.

**Critical Alerts**
*   **Active Alert (Apr 2):** Packlist status `RECEIVED` but `packed_quantity` is `NULL` at **Hyper Changi (Order #23013763)**. Requires immediate technical check by Ops/Support.
*   **Active Alert (Mar 31):** Bulk order SOH indicated **NULL** at **HGPT**.
*   **Active Alert (Mar 30/29):** Packlist quantity (`90M`) significantly exceeds delivered quantity at **Hyper Changi (Store ID 45)**.
*   **Secondary Active Alert (Mar 28):** Dispatcher app unable to scan new zone at **hvivo**. Video evidence available.
*   **Tertiary Active Alert (Mar 27):** HCBP "No picking Q" issue escalated by Ler Whye Ling Angel.


## [9/48] SRE / Network / DBA / DevOps / Infra
Source: gchat | Group: space/AAAAYX-ew1s | Messages: 8 | Last Activity: 2026-04-02T08:46:52.272000+00:00 | Last Updated: 2026-04-02T10:49:28.019378+00:00
**Daily Work Briefing: SRE / Infrastructure Team**

**Key Participants & Roles**
*   **Kalana Thejitha:** Escalated CloudSQL PSC connectivity block (GCD-9015). Investigating DNS resolution failures for `soni-be` Cloud Run to `soni-preprod` CloudSQL. Requesting guidance on Private Zone configuration in `store-of-tmrw-nonprod-vpc`. Tagged @Saranga Colambage, @Kim Tong Ng, @Isuru Dilhan.
*   **Natalya Kosenko:** Submitted PR #12 (`infra-gcp-gen-ai-spark`) for service account rotation; pending review.
*   **Apurva Shingne:** Datadog PR #142 (GCD-8995) pending review by @Sneha Parab and @Nicholas Tan.
*   **Boning He:** Pricing workspace access PR #722 pending.
*   **Amit Giri:** Submitted Datadog permission change PR #152 (`fp-datadog-eu`) on 2026-04-01.
*   **Tayza Htoon:** Requested approval for Terraform workspace access PR #725; tagged @Himal Hewagamage and @Tiong Siong Tee.
*   **Zheng Ming, Wai Ching Chan, Calvin Phan:** Previously reported connectivity/network issues (GCD-8941, GCD-8954, DSD-11066).
*   **Himal Hewagamage & Isuru Dilhan:** Primary reviewers/approvers.

**Main Topics**
1.  **Gen-AI Compliance:** Natalya Kosenko submitted PR #12 on 2026-03-31 to remove an unused service account key from `infra-gcp-gen-ai-spark`.
2.  **Datadog Infrastructure:** Ongoing review of `fp-datadog-eu` PRs (#135–#152). Amit Giri submitted PR #152 on 2026-04-01. Apurva Shingne's PR #142 remains pending.
3.  **Terraform & Workspaces:** Natalya's PR #719, Boning He's PR #722, and Tayza Htoon's PR #725 remain pending review. A failed Terraform plan (`run-CZVLtajJGbLVojLM`) and ticket GCD-8900 are active.
4.  **CI/CD Pipeline Failures:** Soni-BE golden pipeline clone failures persist; `lt-strudel-api-go` Go versioning conflicts require resolution.
5.  **Critical CloudSQL Block (GCD-9015):** Kalana Thejitha reports a multi-day UAT block for `soni-be` Cloud Run (revision: `soni-be-00033-zjj`). Direct egress via PSC failed; DNS name `29eed2f7aa61.3fqp9bm8nzyts.asia-southeast1.sql.goog.` resolves but maps to no IP. Investigation required on `store-of-tmrw-nonprod-vpc` Private Zone configuration.
6.  **Cloud Networking:** AI agents in `us-central1` face internet connectivity issues (Ticket GCD-8941). Mohit Niranwal mandated non-prod testing prior to rollout.
7.  **Bastion Connectivity:** Wai Ching Chan's ticket GCD-8954 remains under investigation.

**Pending Actions & Ownership**
*   **Resolve CloudSQL DNS/PSC Block (GCD-9015):** Owned by @Saranga Colambage, @Kim Tong Ng, @Isuru Dilhan, and @Kalana Thejitha. Action: Create/update Private Zone in `store-of-tmrw-nonprod-vpc` to map the PSC DNS name to the correct IP for the Cloud Run backend.
*   **Review Datadog PR #152:** Owned by Amit Giri; requires immediate review by @Kyle Nguyen, @Himal Hewagamage, @Isuru Dilhan, and @Mohit Niranwal.
*   **Approve Terraform Workspace PRs:**
    *   **PR #725:** Owned by Tayza Htoon; requires approval from @Himal Hewagamage and @Tiong Siong Tee.
    *   **PR #12 (Gen-AI):** Owned by Natalya Kosenko; tagged for review by @Himal, @Mohit, and @Isuru.
    *   **PR #719 & #722:** Pending review by @Isuru Dilhan and @Himal Hewagamage.
*   **Review Datadog PR #142:** Owned by Apurva Shingne; tagged for review by @Sneha Parab, @Nicholas Tan.
*   **Troubleshoot Pipeline Issues:** Investigate Soni-BE SSH keys (Kalana) and `lt-strudel-api-go` config conflicts (Lester).

**Decisions Made**
*   **IaC Requirement:** Mandatory adoption of IaC for Datadog pipelines.
*   **Change Management:** Mohit Niranwal mandated non-prod testing for Cloud NAT changes before production deployment (GCD-8941).
*   **Compliance Action:** Removal of unused, unrotated service account keys is confirmed via PR #12 to address compliance gaps.

**Key Dates & Follow-ups**
*   **2026-03-31 (08:22 UTC):** Natalya Kosenko submitted PR #12 for service account key removal.
*   **2026-04-01 (06:58 UTC):** Amit Giri requested review and merge of Datadog PR #152.
*   **2026-04-01 (07:36–07:38 AM):** Tayza Htoon requested approval for Terraform PR #725.
*   **2026-04-02 (03:38 UTC):** Kalana Thejitha escalated GCD-9015, noting a multi-day UAT block and proposing VPC Connector as a solution.
*   **2026-04-02 (08:46 UTC):** Kalana Thejitha updated status on GCD-9015, identifying the root cause as likely DNS/Private Zone misconfiguration in `store-of-tmrw-nonprod-vpc` for PSC connections.


## [10/48] PDM Notification
Source: gchat | Group: space/AAAAnyFGr84 | Messages: 9 | Last Activity: 2026-04-02T08:38:30.160000+00:00 | Last Updated: 2026-04-02T10:49:50.790346+00:00
**Daily Work Briefing: PDM Notification Summary (Updated)**

**Key Participants & Roles**
*   **Gchat Notification / API Bot (Collection Runner):** Automated system generating test reports.
*   **Webhook Bot:** System component responsible for processing requests; currently failing to render/deliver links despite successful test execution.

**Main Topic**
Automated API contract and functional tests for the `gt-catalogue-service` in the Staging environment executed successfully but failed to generate final notifications due to a persistent Webhook Bot error. The system returns "Webhook Bot is unable to process your request" immediately following summary data, blocking access to detailed reports.

**Pending Actions & Ownership**
*   **Action:** Investigate the specific failure point in the Webhook Bot rendering logic. Prioritize verifying if the failure count discrepancy (1 vs 2 failed tests) aligns with raw Collection Runner data. Resolve the post-execution delivery issue to enable full report visibility.
*   **Owner:** Engineering/DevOps Team (responsible for the notification pipeline).
*   **Context:** New logs from April 2, 2026, confirm two separate execution windows where tests passed but reporting failed. The error is a systemic post-processing block, not a test execution failure.

**Decisions Made**
None recorded; priority remains on repairing the Webhook Bot's rendering capability. No code modifications to service logic are required as failures (if any) are isolated to the notification layer.

**Key Dates & Follow-ups**
*   **Historical Background:** March 18 and March 30, 2026 – Previous incidents with zero execution.
*   **Most Recent Failures/Issues:** April 2, 2026 (Two distinct runs):
    *   **Run 1 (05:38 UTC):** [API Tests] showed 1 Failed; [Contract Tests] showed 0 Failed.
    *   **Run 2 (08:38 UTC):** [API Tests] showed 2 Failed; [Contract Tests] showed 0 Failed.
*   **Environment:** Staging.
*   **Service:** `gt-catalogue-service`.
*   **Immediate Follow-up Required:** Correlate the "1 Failed" (Run 1) and "2 Failed" (Run 2) counts against raw data to determine if test stability is degrading or if the error message is masking variable results. Resolve Webhook Bot rendering errors to restore visibility.

**Status Summary**
The automated run summary indicates a critical failure in the *reporting layer*, not the test execution pipeline itself. Unlike previous incidents on March 30 where Total Requests were zero, April 2 runs show successful completion with varying test outcomes:

*   **Run 1 (07:26 UTC):**
    *   **[API Tests]:** 398 Total Requests, 677 Passed, **1 Failed**, 91 Skipped.
    *   **[API Contract Tests]:** 188 Total Requests, 350 Passed, 0 Failed, 13 Skipped.
*   **Run 2 (08:38 UTC):**
    *   **[API Tests]:** 398 Total Requests, 676 Passed, **2 Failed**, 91 Skipped.
    *   **[API Contract Tests]:** 188 Total Requests, 350 Passed, 0 Failed, 13 Skipped.

Despite these results, the Gchat Notification app explicitly states: "Webhook Bot is unable to process your request" for all runs. This confirms a systemic issue where the notification pipeline blocks finalization or display, even though the underlying Collection Runner executed cases. The presence of failed tests in the second run suggests potential instability that was previously obscured by earlier assumptions of total execution success. Immediate technical troubleshooting of the Webhook Bot's post-execution logic is required to restore full visibility into test outcomes and accurate failure reporting.


## [11/48] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Messages: 5 | Last Activity: 2026-04-02T08:10:34.920000+00:00 | Last Updated: 2026-04-02T10:50:24.961177+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Key Participants & Roles**
*   **Sneha Parab:** BCRS/Fees/Store Closure Impact Lead.
*   **Akash Gupta:** IMS availability/UAT stock sourcing, B2B SKU sync queries.
*   **Wai Ching Chan:** Order Service Deployment/Slot Logic Validation / UAT Stock updates.
*   **Michael Bui:** BCRS Deposit Logic/SAP Integration/Publisher of PRs.
*   **Daryl Ng:** Backoffice/Order Management/Bug Reporting / Slot Logic validation / SOH Sourcing.
*   **Andin Eswarlal Rajesh:** Frontend (iOS/Android) & BCRS UX queries / Amplitude tracking.
*   **Lester Santiago Soriano:** Backend Services Lead.
*   **Zaw Myo Htet:** Payment/Feature Flagging / Pre-order Voucher Logic.
*   **Shiva Kumar Yalagunda Bas:** Slot discrepancy reporting.
*   **Gopalakrishna Dhulipati & Dang Hung Cuong:** Address emoji validation.
*   **Alvin Choo:** Announced annual planning meeting for Apr 2, 9:30 AM.
*   **Yangyu Wang:** Tagged regarding split flag issues; reported iOS Instore page issue.

**Main Topics Discussed**
1.  **HPWP Serviceable Area Routing Issue (New):** On Apr 2 at 08:10 UTC, Daryl Ng reported that Parkway postal codes are incorrectly routing to HCBP instead of HPWP in the serviceable area logic. Akash Gupta and Wai Ching Chan have been tagged for access verification and investigation.
2.  **Unit Price Calculation Compliance:** On Mar 31, Lester highlighted a government compliance requirement for Phase 2 unit price calculations. Current reliance on parsing `display_units` is unscaleable. Proposed solution involves ingesting structured fields (`pack_size`, etc.) from Mirakl/SAP into DBP. Sneha Parab requested an effort assessment.
3.  **iOS Instore Page Regression:** On Apr 1 at 04:14 UTC, Yangyu Wang reported a functional issue on the iOS instore page (Android unaffected). Andin Eswarlal Rajesh is investigating.
4.  **BCRS Stock Sourcing for Sign-off:** On Apr 2 at 02:54 AM, Daryl Ng requested adding Stock on Hand (SOH) for product ID `1152196` in "1HD" store (Store ID: 768). Wai Ching Chan is handling this for Finance sign-off.
5.  **Pre-order Voucher Payment Logic:** On Apr 2 at 03:14 AM, Zaw Myo Htet queried app voucher charging logic for in-store pickups. Wai Ching Chan is addressing queries on sales and voucher cost posting.
6.  **BCRS Deposit Logic Failure:** On Mar 30, Wai Ching Chan reported missing deposit values during UAT checkout. Sundy Yaputra is investigating this regression.
7.  **Slot Date Discrepancy:** Shiva Kumar Yalagunda Bas reported a delivery slot mismatch (UI shows 25th, API indicates 23rd). Daryl Ng and Sundy Yaputra are resolving this.
8.  **Omni Home Split Flag Regression:** On Mar 31 at 02:27 UTC, Daryl Ng reported that Omni home swimlanes fail to follow the split flag due to backend default setting updates.

**Pending Actions & Ownership**
*   **Akash Gupta & Wai Ching Chan:** Verify access to HPWP serviceable area data and investigate Parkway postal code routing to HCBP (New).
*   **Wai Ching Chan:** Add SOH for product `1152196` in store 768; Update specific SKUs to "unlimited stock" in UAT; Clarify pre-order voucher posting logic.
*   **Sundy Yaputra:** Investigate missing BCRS deposit values in UAT checkout and resolve slot date mismatch (UI vs API).
*   **Akash Gupta, Michael Bui, Andin Eswarlal Rajesh:** Provide immediate inputs on BCRS tickets DPD-637 and DPD-807 to close the epic.
*   **Lester Santiago Soriano / Sneha Parab:** Assess effort for mapping structured unit price fields from Mirakl/SAP.
*   **Andin Eswarlal Rajesh:** Investigate iOS instore page regression reported by Yangyu Wang.
*   **Daryl Ng:** Review Michael Bui's PR #7 (`bcrs-deposit-posting`) and investigate Omni home split flag issue with Nikhil and Yangyu Wang.

**Decisions Made**
*   **Unit Price Structure:** Move from parsing `display_units` to utilizing structured fields for Phase 2 compliance.
*   **BCRS Epic Priority:** Immediate action required to close the BCRS epic; ticket status must be verified for DPD-637 and DPD-807.
*   **UAT Stock Critical:** Specific SKUs identified by Sneha Parab must be set to unlimited stock immediately. Product `1152196` requires SOH in store 768.
*   **iOS Issue:** Investigation initiated into iOS-specific instore page failure.

**Key Dates & Deadlines**
*   **Mar 30, 2026:** B2B sync clarity requested; UAT stock updates required; BCRS deposit failure reported.
*   **Mar 31, 2026:** Unit price compliance discussion initiated; Omni home split flag regression reported.
*   **Apr 2, 2026 (Today):** Annual planning meeting scheduled for 9:30 AM (Host: Alvin Choo); HPWP routing issue flagged at 08:10 UTC.

**Note on Historical Context:** Previous mentions of code review priorities for `layout-service` PR #362 are superseded by the urgent Strudel SDK deployment update (`go-platform-website`). Current focus includes investigating UAT BCRS deposit regression, updating UAT stock levels, resolving slot date mismatches, closing the BCRS epic via tickets DPD-637 and DPD-807, debugging the Omni home split flag configuration, assessing structured unit price field ingestion, troubleshooting the new iOS instore page regression, clarifying pre-order voucher payment posting logic, and verifying HPWP serviceable area routing.


## [12/48] [Prod Support] Marketplace
Source: gchat | Group: space/AAAAs0DTvmA | Messages: 11 | Last Activity: 2026-04-02T08:10:29.847000+00:00 | Last Updated: 2026-04-02T10:51:18.467929+00:00
**Daily Work Briefing: [Prod Support] Marketplace**

**Key Participants & Roles**
*   **Support/Operations:** Willie Tan, Iris Chang, Lalita Phichagonakasit, Charlene Tan, Jie Yi Tan, Ayton See, Amos Lam, Michelle Lim.
*   **Technical/Admin Team:** Dang Hung Cuong, Shiva Kumar Yalagunda Bas, Olivia -, Jill Ong, Greta Lee, Zaw Myo Htet, Angella Yeo, Cassandra Thoi, Gopalakrishna Dhulipati, Ee Ling Tan, Sneha Parab.
*   **New Reporter:** Muhammad Sufi Hakim Bin Safarudin.

**Main Topics & Discussion Summary**
Discussions continue to focus on operational blockers regarding seller onboarding, order fulfillment discrepancies, system configuration errors, and data visibility gaps. New reports from April 1 highlight critical platform performance issues (lag), DBP barcode conflicts, and delivery window synchronization failures. Additionally, queries arose on April 2 regarding picker app historical data, specific seller app issues, and image identification problems.

1.  **Transporter App Performance:** Anwar Nur Amalina reported (Apr 1) severe lag and job loading failures in the Transporter Inform app.
2.  **DBP Barcode Duplicate/NotFound Error:** Charlene Tan flagged (Apr 1) a barcode unable to be found in DBP despite appearing as a duplicate entry. Dang Hung Cuong was tagged for investigation.
3.  **Delivery Window Synchronization:** Jie Yi Tan reported (Apr 1) that the delivery window configuration failed for seller "Funa Artistic Hampers & Gifts" (displaying 3 days instead of configured 5). Dang Hung Cuong was tagged.
4.  **Seller Account Sync Failure:** Michelle Lim reported (Mar 31) that two new seller accounts failed to sync to DBP despite allocated internal codes and no error messages (Codes: 32208, 32207).
5.  **Image Identification Query (New):** On Apr 2, Charlene Tan queried the team regarding how to identify specific image problems. The discussion involved multiple replies by early afternoon.
6.  **Picklist Investigation:** Tech team is investigating failures for Order #258155683 and Postponed Order #256653797 (reported Apr 30).

**Pending Actions & Ownership**
*   **Transporter App Investigation:** Technical team to investigate lag and job loading failures (Anwar Nur Amalina, Apr 1).
*   **DBP Barcode Discrepancy:** Dang Hung Cuong to investigate why a specific barcode cannot be found in DBP while showing as a duplicate (Charlene Tan, Apr 1).
*   **Delivery Window Fix:** Dang Hung Cuong to resolve the delivery window sync issue for "Funa Artistic Hampers & Gifts" (Jie Yi Tan, Apr 1).
*   **Seller Sync Investigation:** Tech team to investigate why DBP accounts 32208 and 32207 failed to sync (Michelle Lim, Mar 31).
*   **Report Email Logic:** Confirm and implement automatic CC of `db-online-marketplace@ntucenterprise.sg` for all DF vendor Sales Breakdown Reports (Iris Chang, Mar 31; cc: Amos Lam, Michelle Lim, Jill Ong).
*   **SKU Live Status:** Investigate why SKU 90248069 is not live on the website despite being published with an offer (Charlene Tan, Mar 31).
*   **Picker App Functionality:** Dang Hung Cuong and Amos Lam to clarify picker app history viewing capabilities for sellers (Iris Chang, Apr 2).
*   **Toh Thye San Issue / Urgent Fulfillment Block:** Jing Ying Foo raised a "similar issue from Aw's Market" on Apr 2 at 07:02 UTC. Amos Lam escalated this urgently to Dang Hung Cuong, Shiva Kumar Yalagunda Bas, and Sneha Parab at 07:04 UTC due to potential fulfillment impacts. Charlene Tan (Apr 2, 15:06) clarified that storage type assignments are managed by GLS, not tech; the immediate fix is using an alternative PA label to scan orders before end-of-day cutoffs.
*   **Image Problem Analysis:** Team to determine root cause of image identification issues raised by Charlene Tan (Apr 2).

**Decisions Made**
*   Dang Hung Cuong is prioritizing the removal of Item ID: 90244361, new picklist failures, Woah Group offers errors, Pureen barcode truncation, DBP sync issues, Transporter app lag, and delivery window failures.
*   Dang Hung Cuong and Shiva Kumar Yalagunda Bas are assigned to investigate vendor picklist anomalies.
*   **Clarification:** Storage type assignments for GLS-related scanning issues are confirmed as non-technical; the operational workaround is applying alternate PA labels immediately.
*   **Completed:** Access linkage for Seller ID 31435 was successfully executed by Shiva Kumar Yalagunda Bas on Mar 27, 11:29 UTC.

**Key Dates & Deadlines**
*   **2026-04-02:** Jing Ying Foo raised "Aw's Market" issue; Amos Lam escalated urgent fulfillment risk request (cc: Sneha Parab, Shiva Kumar Yalagunda Bas); Charlene Tan clarified GLS storage logic and advised on PA label workaround. Iris Chang queried picker app history functionality; Charlene Tan initiated image problem discussion.
*   **2026-04-01:** Anwar Nur Amalina reported Transporter app lag; Charlene Tan flagged DBP barcode conflicts; Jie Yi Tan reported delivery window sync failure for "Funa Artistic Hampers & Gifts."
*   **2026-03-31:** Michelle Lim reported DBP sync failure for codes 32208 and 32207. Iris Chang raised Sales Breakdown Report email logic query. Charlene Tan reported SKU 90248069 not live.
*   **2026-03-30:** Muhammad Sufi Hakim Bin Safarudin reported picklist generation failures for Order #258155683 and Postponed Order #256653797.


## [13/48] [Prod Support] Onsite/Search/Browsing
Source: gchat | Group: space/AAAA8Ot7GRg | Messages: 5 | Last Activity: 2026-04-02T07:22:12.112000+00:00 | Last Updated: 2026-04-02T10:51:47.408401+00:00
**Daily Work Briefing: [Prod Support] Onsite/Search/Browsing**

**Key Participants & Roles**
*   **Terence Cheah:** Investigating Amplitude tracking anomalies (March) and recently flagged potential bot activity on specific search terms.
*   **Lalita Phichagonakasit:** Originally raised issues regarding SKU `13226899` visibility and reordering (March).
*   **Emerald Sia:** Reported a critical outage where Preorder SKUs failed to appear despite going live at 09:00; noted removal of comms due to the issue.
*   **Tiffany Teo:** New report regarding Promo SKU `13279469` not reflected in HPWP (Home Page Widget Platform).

**Main Topics**
The discussion has expanded from historical anomalies to four active operational incidents:
1.  **Preorder Visibility Outage (Critical):** Preorder SKUs are not displaying on the site or via deep link (`fairprice://preorder/campaign`) despite a scheduled 09:00 go-live. Emerald Sia confirmed all communications were halted due to this failure.
2.  **Search Traffic Anomalies:** Terence Cheah identified suspicious "dirty traffic" on two specific terms: `Nescafe concentrate` (new, high volume) and `Bio-home capsule` (elevated volume with zero post-click interactions).
3.  **HPWP Display Failure (New):** Tiffany Teo reported that Promo SKU `13279469` is not appearing in the Home Page Widget Platform as of April 2, 2026, at 07:22 UTC+00:00.
4.  **Historical Context:** Ongoing investigation into Amplitude tracking gaps (March 10+) and SKU `13226899` visibility for postal code `762115`.

**Pending Actions & Ownership**
*   **Action A (Preorder/Engineering):** Immediate root cause analysis of why Preorder SKUs are invisible at go-live.
    *   *Owner:* Unassigned (Engineering/Product).
    *   *Context:* Critical business impact; comms already removed by Emerald Sia.
*   **Action B (HPWP/Product):** Investigate and resolve visibility failure for Promo SKU `13279469` in HPWP.
    *   *Owner:* Unassigned (Product/Engineering).
    *   *Context:* High priority; reported by Tiffany Teo with 12 replies awaiting resolution.
*   **Action C (Search/Safety):** Investigate bot activity on `Nescafe concentrate` and `Bio-home capsule`. Verify traffic sources and click-through behavior anomalies.
    *   *Owner:* Unassigned (Security/Search teams).
    *   *Context:* High volume/zero conversion suggests malicious or broken traffic.
*   **Action D (Analytics):** Continue investigation into Amplitude event gaps (March 10+) and backend deployment impact. (Status unchanged from March report).
*   **Action E (Product/Search):** Re-evaluate SKU `13226899` visibility for postal code `762115`.

**Decisions Made**
No formal resolutions recorded. The Preorder issue has triggered an immediate halt to marketing communications. A message regarding potential bot activity remains under investigation. An "Unknown User" sent a deleted message at 03:37 UTC+00:00 on April 2, 2026, adding no new actionable data.

**Key Dates & Follow-ups**
*   **Preorder Failure Date:** April 2, 2026 (Failed to launch at 09:00 local time).
*   **HPWP Report Time:** April 2, 2026, 07:22 UTC+00:00.
*   **Search Anomaly Report:** April 2, 2026, 03:35 UTC+00:00.
*   **Amplitude Gap Start:** March 10, 2026.
*   **Thread Activity:** Last confirmed reply recorded on April 2, 2026 (Emerald Sia and Terence Cheah). Thread shows 36 unread replies to the Preorder alert; HPWP thread has 12 unread replies.

**Specific References**
*   **Resource Tag:** `#Amplitude-discussions` | `#Preorder-Outage` | `#Search-Traffic-Spoofing` | `#HPWP-Display-Issue`
*   **Analytics URL:** https://app.amplitude.com/analytics/fairprice/chart/y69ylkn/edit/r76iv7h7
*   **Metric Affected:** "order checkout for online grocery completed"
*   **Product IDs (Historical):** `13226899`
*   **New Product ID:** `13279469` (Promo SKU)
*   **Affected Postal Code:** `762115`
*   **Search Terms Flagged:** `Nescafe concentrate`, `Bio-home capsule`
*   **Preorder Deep Link:** `fairprice://preorder/campaign`


## [14/48] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Messages: 16 | Last Activity: 2026-04-02T07:09:11.547000+00:00 | Last Updated: 2026-04-02T10:52:19.557096+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Apr 2, 07:10 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-retail-media`.
*   **Escalations:** `@oncall-dpd-staff-excellence-pdm`, `@hangouts-GT-Search-DatadogAlerts`, `@hangouts-GT-Discovery-DatadogAlerts`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Retail Media.

**Main Topic**
**P2 INCIDENT (RESOLVED):** High error rate in `marketing-service`.
*   **Current Status:** All incidents resolved as of 07:09 UTC on Apr 2. No active incidents remain.
*   **Incident Timeline:**
    *   Triggered: 06:59 UTC (P2 Error Rate).
    *   Recovered: 07:09 UTC.

**Resolved Incidents**
*   **`marketing-service` (High Error Rate):** P2 anomaly triggered at 06:59 UTC; recovered at 07:09 UTC on Apr 2. [Status: Resolved]
    *   *Monitor ID:* `17447106`. Triggered when error rate exceeded 5% (Metric: 1.6%). Recovered when metric dropped to 0.1%.
    *   *Duration:* ~10 mins.
*   **`go-catalogue-service` (Latency):** P3 anomaly triggered at 03:24 UTC; recovered at 03:33 UTC on Apr 2. [Status: Resolved]
    *   *Monitor ID:* `17447967`. Triggered when p90 latency exceeded 2.0s (Metric: 4.338s). Recovered when metric dropped to 0.636s.
*   **`marketing-service` (Throughput):** P4 anomaly triggered at 01:29 UTC; recovered at 02:21 UTC on Apr 2. [Status: Resolved]
    *   *Monitor ID:* `17447110`. Detected >3 deviations from predicted values.

**Pending Actions & Ownership**
*   **Action:** **POST-INCIDENT REVIEW (`marketing-service` High Error Rate - Apr 2):** [Status: OPEN] Investigate transient P2 error rate spike (06:59–07:09 UTC). Recommended checks: Datadog traces, K8s pod metrics.
    *   **Owner:** Retail Media / Product Data Management.
*   **Action:** **POST-INCIDENT REVIEW (`go-catalogue-service` Latency - Apr 2):** [Status: OPEN] Investigate transient latency spike on `get_/category/_id` (03:24–03:33 UTC). Recommended checks: Datadog traces, K8s pod metrics.
    *   **Owner:** Product Data Management (`team:dpd-staff-excellence-pdm`).
*   **Action:** **POST-INCIDENT REVIEW (`sku-store-attribute Job`):** [Status: OPEN] Investigate root cause of Apr 1, 16:27–16:43 stuck job. Recommended checks: logs, pending DB files, pod restart.
    *   **Owner:** Product Data Management / Retail Media.

**Decisions Made**
*   The Apr 2, 06:59 UTC `marketing-service` error rate spike was transient (~10 mins) and resolved automatically upon metric stabilization (error rate dropped from 1.6% to 0.1%). No manual restart required.
*   Previous incidents on Apr 1 (`sku-store-attribute`, PubSub, and `go-catalogue`) were transient or recovered without intervention.

**Key Dates & Follow-ups (Apr 1–2, 2026)**
*   **P2:** `marketing-service` high error rate (Apr 2, 06:59–07:09).
*   **P3:** `go-catalogue-service` latency spike on `get_/category/_id` (Apr 2, 03:24–03:33).
*   **P4:** `marketing-service` throughput anomaly (Apr 2, 01:29–02:21).
*   **Historical P3/P2:** Various incidents on Apr 1.

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c
*   **New Monitor Link (`marketing-service` Error Rate):** https://app.datadoghq.eu/monitors/17447106
*   **APM Resource:** https://app.datadoghq.com/apm/services/marketing-service/operations/http.request/resources?env=prod
*   **K8s Resource:** https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/marketing-service/overview
*   **Runbook:** https://ntuclink.atlassian.net/wiki/spaces/DIS/pages/2008167992/marketing-service+-+Run+book


## [15/48] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/jPGy0nmdYfc | Messages: 3 | Last Activity: 2026-04-02T07:02:16.916000+00:00 | Last Updated: 2026-04-02T10:52:28.548138+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Daryl Ng:** Lead requesting clarification on team composition.
*   **Alvin Choo:** Tagged participant (likely responsible for providing documentation).
*   **Tiong Siong Tee:** Participant offering context/humor regarding information retention.

**Main Topic**
Discussion centered on the need to re-verify the organizational structure and specific personnel assignments within Daryl Ng's team due to memory overload regarding current roster members.

**Pending Actions & Ownership**
*   **Action:** Provide the updated organization chart containing team member details.
*   **Owner:** Alvin Choo (implied by context of request).
*   **Status:** Pending response from Alvin Choo as of 07:02 AM.

**Decisions Made**
No formal decisions were recorded in this thread; the conversation remains a status inquiry and clarification request.

**Key Dates & Follow-ups**
*   **Date:** April 2, 2026 (07:01 – 07:02 UTC).
*   **Follow-up Required:** Immediate response from Alvin Choo regarding the organization chart to resolve Daryl Ng's query.

**Contextual Notes**
The conversation highlights a temporary information gap regarding team composition for Project Light Attack and Defence Leads, necessitating external verification of roles rather than internal recall.


## [16/48] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4 | Messages: 6 | Last Activity: 2026-04-02T07:01:14.547000+00:00 | Last Updated: 2026-04-02T10:52:57.058412+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Space Creator; Lead coordinating the briefing.
*   **Daryl Ng, Gopalakrishna Dhulipati, Tiong Siong Tee, Michael Bui, Akash Gupta:** Designated "Project Light Attack and Defence Leads".
*   **Tiong Siong Tee:** Recently queried on April 1 regarding inclusion in calls; confirmed invited by Alvin at 06:44 AM UTC.

**Main Topic**
Following the transition to active strategic planning ("Room 2") on March 24, the team is finalizing slide preparation within six "Spotlight Topics." While collaboration on **"RMN"** and **"Payment"** slides began March 24, a flexibility protocol established March 25 allows leads to attend other meetings (e.g., BCRS) if required. Technical direction remains focused on decoupling from SAP, with consensus that SAP serves primarily for finance and sales records.

On April 1, Daryl Ng highlighted an epic for Phase 2 ("1HD to scale to more stores," `DPD-627`), noting a lack of alignment with Dennis. On **April 2**, the discussion shifted to technical architecture and team clarity. Tiong Siong Tee raised a critical risk regarding data architecture: adding a "Data8" layer between DSP and SAP could potentially introduce reconciliation issues, citing recurring problems with Caltran or Data8 in FPPay workflows (06:31 AM UTC). Concurrently, Daryl Ng requested clarification on the team's organizational structure, asking for the org chart again to confirm his specific team members (07:01 AM UTC).

**Pending Actions & Ownership**
*   **Action:** Evaluate technical feasibility of adding a "Data8" layer between DSP and SAP.
    *   **Ownership:** Engineering/Architecture Team.
    *   **Status:** Pending; Query raised by Tiong Siong Tee on April 2, 06:31 AM UTC regarding potential reconciliation issues with Caltran/Data8.
*   **Action:** Review "Promotion Conflict Test Case_05.NOV.20" and summarize for Alvin Choo.
    *   **Ownership:** Michael Bui. (Access initially denied March 25).
*   **Action:** Provide updated organizational chart to Daryl Ng.
    *   **Ownership:** Team/Alvin Choo.
    *   **Status:** Requested by Daryl Ng on April 2, 07:01 AM UTC ("forgot who are in my team").
*   **Action:** Clarify backend API responsibilities with CoMall regarding personalization and orchestration.
    *   **Ownership:** Michael Bui (to note and document).
*   **Action:** Identify the owner managing data indexing to Algolia.
    *   **Ownership:** Daryl Ng raised this query on March 26; team response pending.
*   **Action:** Confirm CoMall contract status and determine timing for creating a dedicated GChat space with CoMall teams.
    *   **Ownership:** Michael Bui (initiated inquiry March 26); pending confirmation from Alvin Choo or Gopalakrishna Dhulipati.
*   **Action:** Clarify if a dedicated communication space exists between the internal team and CoMall.
    *   **Ownership:** Daryl Ng raised this query on April 2, 07:00 AM UTC ("do we have a space between us and co-mall?").

**Decisions Made**
*   **Meeting Flexibility:** Leads may prioritize other critical meetings (e.g., BCRS) if necessary (Confirmed March 25).
*   **System Architecture:** SAP integration should be decoupled from core operational logic; designated strictly for finance and sales records (Agreed March 25).
*   **Governance Structure:** FPG cannot be treated merely as a standard seller due to governance conflicts; distinct data structures or models are required for FP vs. non-governance sellers (Clarified by Gopalakrishna Dhulipati).

**Key Dates & Follow-ups**
*   **April 2, 06:31 AM UTC:** Tiong Siong Tee queried risks of a "Data8" layer between DSP and SAP regarding reconciliation issues.
*   **April 2, 07:00 AM UTC:** Daryl Ng asked if a dedicated space exists between the team and CoMall.
*   **April 2, 07:01 AM UTC:** Daryl Ng requested the org chart again to clarify team composition; replies received @Alvin Choo.
*   **April 1, 06:44 AM UTC:** Alvin Choo confirmed permission to invite Tiong Siong Tee to discussion calls.
*   **March 30:** "No Data Migration" strategy proposed by Alvin Choo to reduce risk; generated significant engagement.


## [17/48] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Messages: 9 | Last Activity: 2026-04-02T06:58:23.106000+00:00 | Last Updated: 2026-04-02T10:53:35.015514+00:00
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
2.  **Mar 18/19:** `10aaf170...` (~5.6h). Status: **Resolved**.
3.  **Mar 20, 2026:** `2787bcd7...` (~4.4h). Status: **Resolved**.
4.  **Mar 22, 2026:** `08f5624a...` (~3.4h). Status: **Resolved**.
5.  **Mar 24–25, 2026:** `de0cbb14...` (~3h 51m). Status: **Resolved**.
6.  **Mar 25, 2026:** `978f6328...`. Recovered 12:09 UTC (~24h). Status: **Resolved**.
7.  **Mar 26, 2026:** `7b73b037...` (~3h 22m). Status: **Resolved**.
8.  **Mar 27, 2026:** `f5d0894a...`. Recovered 17:37 UTC. Status: **Resolved**.
9.  **Mar 28–30, 2026:** Multiple P3 incidents recovered (Keys: `8874d9ed...`, `784f6ec6...`, `acd815df...`).

**Recent Sequence Update:**
*   **Mar 31, 2026:** Incident `0404fba2...` triggered at 11:49 UTC and resolved at 15:05 UTC (~3h 16m). Status: **Resolved**.

*   **Apr 1, 2026 Sequence:**
    *   **Incident A (Story Key `c6d476e4...`):** Triggered 2026-04-01T23:27:22 UTC. Recovered ~2026-04-01T02:53:22 UTC (~3h 26m). Status: **[P3] Recovered**.
    *   **Incident B (Story Key `f28ed3be...`):** Triggered 2026-04-01T01:53:22 UTC. Recovered ~2026-04-01T05:06:22 UTC (~3h 13m). Status: **[P3] Recovered**.
    *   **Incident C (Story Key `ba9617bc...`):** Triggered **2026-04-01T07:07:22 UTC**. Recovered **2026-04-01T08:26:22 UTC** (~1h 19m). Status: **[P3] Recovered**.

*   **Apr 2, 2026 Update:**
    *   **Incident D (Story Key `fa62ae68...`):** Triggered **2026-04-02T06:58:23 UTC**.
    *   Current Status: **[Active / Triggered]**.
    *   Note: Alert indicates "Datadog is unable to process your request."

### Pending Actions & Ownership
*   **Current Status:** **One active incident** detected on April 2, 2026 (`fa62ae68-9098-51f3-bb09-48de381d3daa`). All previous incidents from the Apr 1 sequence are resolved.
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Action Required:** Monitor status for self-resolution. Historical pattern suggests transient issues resolve within ~3 hours, but this new trigger requires observation to confirm if it follows the established recovery trend or escalates beyond the 6-hour threshold.

### Decisions Made
*   **Escalation Status:** No escalation yet; waiting on resolution of `fa62ae68...`.
*   **Protocol:** Continue standard surveillance. If the incident persists beyond 09:58 UTC (3 hours post-trigger) or exceeds 12:58 UTC (6-hour threshold), manual review is advised.

### Key Dates & Follow-ups
*   **Latest Event:** April 2, 2026 at 06:58:23 UTC.
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Surveillance ongoing for `story_key:fa62ae68-9098-51f3-bb09-48de381d3daa`.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Datadog Monitor Link:** [View in Datadog](https://app.datadoghq.eu/monitors/17447511)
*   **New Incident Log:**
    *   Key `fa62ae68-9098-51f3-bb09-48de381d3daa`: https://app.datadoghq.eu/monitors/17447511?group=story_key%3Afa62ae68-9098-51f3-bb09-48de381d3daa&from_ts=1775112111000&to_ts=1775113311000&event_id=8570644753996362919


## [18/48] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/KTy1--6dEUY | Messages: 2 | Last Activity: 2026-04-02T06:31:43.183000+00:00 | Last Updated: 2026-04-02T10:53:46.148589+00:00
### Daily Work Briefing: Project Light Attack and Defence Leads

**Key Participants & Roles**
*   **Tiong Siong Tee:** Raised a technical concern regarding data layer architecture and historical reconciliation risks.
*   **Gopalakrishna Dhulipati:** Provided immediate directive to escalate the identified risk.

**Main Topic/Discussion**
The discussion focused on the architectural implications of inserting a `data8` layer between the DSP and SAP systems within Project Light Attack and Defence Leads. Tiong Siong Tee queried whether this addition would introduce increased reconciliation issues, citing historical precedents from the `fppay` project where similar integrations with `caltran` or `data8` frequently encountered problems.

**Pending Actions & Ownership**
*   **Action:** Raise the concern regarding potential `data8` reconciliation issues immediately.
*   **Owner:** Tiong Siong Tee (inferred from Gopalakrishna's directive "you should raise it now" addressed to the proposer).
*   **Context:** The escalation must address the risk of introducing new reconciliation failures between DSP and SAP via the proposed `data8` layer, referencing past `fppay` experience.

**Decisions Made**
No technical decision regarding the architecture has been finalized yet. The only outcome was an administrative directive to escalate the issue for review or formal discussion immediately rather than delaying it.

**Key Dates & Follow-ups**
*   **Date of Discussion:** April 2, 2026 (UTC) at 06:31 UTC.
*   **Immediate Next Step:** The concern must be raised "now" (relative to the chat timestamp of 06:31:43).
*   **Reference Data:** `fppay` project history involving `caltran` and `data8`.

**Resource Metadata**
*   **Space URL:** https://chat.google.com/space/AAQAsFyLso4
*   **Total Messages:** 2


## [19/48] 📢 COM Notifications
Source: gchat | Group: space/AAAAu4WIubc | Last Activity: 2026-04-02T06:29:56.703000+00:00 | Last Updated: 2026-04-02T06:38:09.262656+00:00
**Daily Work Briefing: SonarCloud Quality Monitoring**

**Key Participants & Roles**
*   **gautam-ntuc**: Developer; responsible for `catalogue-service` (PR-535) and `catalogue-job` commits.
*   **Shiva Kumar Yalagunda Bas**: Developer; previously authored `supplier-job` changes.
*   **bitbucket-pipelines**: Automated CI/CD bot triggering merges and deployments.
*   **System/Webhook Bot**: Continues reporting recurring "Webhook Bot is unable to process your request" errors across all notifications, including new scans on April 2.

**Main Topic**
Automated SonarCloud quality gate scans for `catalogue-service`, `fni-product-license-alert`, and other services. The conversation tracks code coverage, pipeline volatility, the resolution of failing Quality Gates, and persistent system notification errors.

**Status Summary by App**
*   **`fni-product-license-alert`**:
    *   **April 2 (03:14–06:29 UTC)**: PR-1433 underwent multiple scans (ver. `1242b0a`, `3212fc0`, `770f1f6`, `d5a9f8a`), all **PASSED** with 94.4% new code coverage.
    *   **April 2 (06:29 UTC)**: PR-1483 scanned and **PASSED**, but recorded **0%** Coverage on New Code. This mirrors a previous anomaly seen in PR-1479 on April 1.
*   **`catalogue-service`**:
    *   **April 2 (05:21–05:25 UTC)**: gautam-ntuc opened PR-535 (`feature/rebase/PRDM-513-make-deposit-sku-data-available`). Status is currently **OPEN** with **95.9%** new code coverage.
*   **`supplier-job`**: No new activity reported; previous scans on March 19 remain the last recorded success.

**Pending Actions & Ownership**
*   **System Error Investigation**: The "Webhook Bot is unable to process your request" error persists in every notification from March 5 through April 2 (including `catalogue-service` PR-535 and `fni-product-license-alert` PR-1483). No specific owner assigned; requires immediate engineering attention.
*   **`fni-product-license-alert` Coverage Anomaly**: A second instance of a **PASSED** Quality Gate with **0%** new code coverage occurred in PR-1483 on April 2. This contradicts typical gate logic (following the PR-1479 incident on April 1) and requires investigation into tolerance settings or data reporting integrity.
*   **`catalogue-service` Monitoring**: PR-535 is currently OPEN; teams should monitor for potential failure/recovery cycles similar to previous `seller-proxy-service` incidents.

**Decisions Made**
*   **April 2 Action**: `fni-product-license-alert` PR-1433 scans consistently recovered and passed immediately despite volatility in previous days' logs. The system accepted the merge logic automatically.
*   Recent merges in `supplier-job` and recovery scans for `seller-proxy-service` remain valid historical context, though current focus has shifted to `catalogue-service`.

**Key Dates & Timeline**
*   **April 1**: 
    *   **03:51 UTC**: `fni-product-license-alert` PR-1479 PASSED with 0% coverage.
    *   **03:52–04:22 UTC**: `seller-proxy-service` PR-2334 failed/recovered cycle.
*   **April 2**: 
    *   **03:14 – 06:27 UTC**: Multiple PASSED scans for `fni-product-license-alert` PR-1433 at 94.4% coverage.
    *   **05:21 – 05:25 UTC**: `catalogue-service` PR-535 opened by gautam-ntuc (OPEN, 95.9% coverage).
    *   **06:29 UTC**: `fni-product-license-alert` PR-1483 PASSED with **0%** new code coverage.


## [20/48] QE <-> All Tribes
Source: gchat | Group: space/AAAAS7vPcKs | Last Activity: 2026-04-02T06:15:05.625000+00:00 | Last Updated: 2026-04-02T06:40:30.701173+00:00
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
1.  **Pipeline Error (Critical):** On **31 Mar**, Hang Chawin Tan reported a pipeline failure in `dp-gifting-web`. *Status:* Active discussion involving @Madhuri Nalamothu, @Milind Badame, and @Oktavianer Diharja awaiting resolution.
2.  **BCRS Swimlane Management:** On **31 Mar**, Milind Badame queried if BCRS swimlanes can be disabled post-UAT. *Status:* Discussion ongoing with @Daryl Ng and @Andin Eswarlal Rajesh to determine cleanup protocols.
3.  **BackOffice Domain Validation (New):** On **2026-04-01 10:59**, Milind Badame identified a validation gap where BackOffice accepts full invalid domains. *Status:* Awaiting investigation from @Daryl Ng.
4.  **System-Wide Intermittent Failures:** On **30 Mar**, Milind Badame reported frequent HTTP 500 errors affecting order placement, cart, and PDP pages. *Status:* Active investigation for backend instability vs. testing impact.
5.  **Order Placement Failure ('Strong Tasty Brew'):** On **30 Mar**, Madhuri Nalamothu reported inability to place orders for non-FP product 'Strong Tasty Brew'. Discussion ongoing with @Piraba Nagkeeran.
6.  **MiniGames Blank Screen:** On **30 Mar**, Milind Badame reported a blank white screen when tapping the MiniGames tile as a guest user followed by login on lower Android versions. *Owner:* @Aman Saxena, Mobile Team.
7.  **DC Membership Subscription & Enrollment (Critical/Escalated):** On **2026-04-02**, Milind Badame confirmed regression failures in DC membership tests (enrollment for new users, promote/demote). Specific errors include "Unable to Process Payment" and backend enrollment blockage. *Status:* Escalated; awaiting investigation from @Daryl Ng and @Andin Eswarlal Rajesh.
8.  **iOS SnG Flow List Update Bug:** On **2026-04-02**, Madhuri Nalamothu reported that adding items to "My List" via the PDP Products card in iOS does not update the count. *Status:* Video evidence shared; discussion ongoing with @Piraba Nagkeeran and @Andin Eswarlal Rajesh.
9.  **LinkPoints Regression Failure:** Reported on **27 Mar** regarding CLS Award Balance API `500` errors. Status remains Critical/Blocked pending resolution with @Pandi.
10. **JWC & Express Delivery Timeouts:** On **1 Apr**, Milind Badame flagged E2E test failures due to store timings. Request raised to configure JWC and Express Delivery timings for **24x7** in UAT. *Status:* Pending advice from @Andin Eswarlal Rajesh and @Daryl Ng.
11. **Express Delivery Service Fee Logic:** On **1 Apr**, Milind Badame reported service fees are not waived when the amount exceeds $30. *Status:* Awaiting investigation by @Daryl Ng.
12. **Unlimited Product API Error:** On **1 Apr**, Milind Badame queried behavior when calling APIs to increase counts for products set as unlimited in BackOffice. *Status:* Under review with @Wai Ching Chan and @Andin Eswarlal Rajesh.
13. **Tile Customization - PreOrder:** On **2026-04-01 10:18**, Milind Badame asked if tiles can be customized to include "PreOrder" functionality. *Status:* Pending response from @Daryl Ng (Latest activity: ~1 hour ago).
14. **iOS Express Delivery UI Issue:** On **2026-04-02 06:15**, Madhuri Nalamothu observed the cart icon "Add to Cart" text is not displaying clearly in iOS PLP for specific products (e.g., Milo Chocolate Malt). *Status:* Notified @Piraba Nagkeeran.

**Pending Actions & Ownership**
*   **DC Membership Payment Fix:** Resolve "Unable to Process Payment" errors blocking new enrollments and promote/demote tests. *Owners:* @Daryl Ng, @Andin Eswarlal Rajesh. **(Highest Priority)**
*   **Pipeline Resolution:** Resolve `dp-gifting-web` pipeline error reported by @Hang Chawin Tan. *Owners:* @Madhuri Nalamothu, @Milind Badame, @Oktavianer Diharja.
*   **iOS SnG List Update Fix:** Investigate and resolve count update failure in iOS PDP My List flow. *Owners:* @Piraba Nagkeeran, @Andin Eswarlal Rajesh.
*   **BackOffice Validation Fix:** Investigate and prevent invalid domain entries in BackOffice. *Owner:* @Daryl Ng.
*   **iOS Express UI Fix:** Clarify cart icon display issues on iOS PLP. *Owner:* @Piraba Nagkeeran.

**Decisions Made**
*   DC Membership payment failures are confirmed as a regression blocking new user enrollment and require immediate escalation to Dev.
*   iOS SnG flow "My List" count update failure is validated via video; mobile team engagement initiated.
*   System-wide errors on 30 Mar require immediate triage; potential testing activity suspected but not yet confirmed as root cause.

**Key Dates & Deadlines**
*   **2026-04-02 06:15:** iOS Express Delivery UI issue reported by @Madhuri Nalamothu.
*   **2026-04-02 03:09:** iOS SnG "My List" update bug reported; video shared.
*   **2026-04-02 04:48 - 05:13:** Escalation regarding DC membership payment failures and backend enrollment blockage.
*   **2026-04-01 10:59:** BackOffice invalid domain issue raised by @Milind Badame.
*   **2026-04-01 10:18:** Tile Customization inquiry raised by @Milind Badame.


## [21/48] Alvin Choo
Source: gchat | Group: dm/zmMZpgAAAAE | Last Activity: 2026-04-02T05:15:22.777000+00:00 | Last Updated: 2026-04-02T06:41:57.055186+00:00
**Daily Work Briefing: RMN & Postmortem Updates (Updated)**
**Resource:** Alvin Choo (Lead/Manager) | **Participant:** Michael Bui (Domain Expert, Backend Dev)
**Date Range:** March 3 – April 2, 2026 + Upcoming Planning

### **Key Participants & Roles**
*   **Alvin Choo:** Leads coordination for RMN postmortem reports, travel logistics, and visa invitations. Contact: +65 9351 0653.
*   **Michael Bui:** Domain expert responsible for backend implementation; returned to Singapore on April 2 after leave (ended April 2).

### **Main Topics**
1.  **Wuhan Travel & Visa Processing:** Departure confirmed for **April 6, 2026**. Michael requires a multi-entry Type M visa applied for one month in advance. Alvin is securing an invitation letter from CoMall.
2.  **RMN Postmortem & Incident Review:** Finalizing report for BCRS completion; addressing "Overage on transaction sync" and transition to impressions-based model.
3.  **Technical Implementation & Prioritization:** Michael has returned and identified the project timeline as "very tight and challenging." He requested immediate focus areas from Alvin to utilize his upcoming long weekend for preparation.

### **Decisions Made**
*   **Task Reassignment:** The Nikhil ticket (5-man-day) is assigned to a Backend Engineer from Daryl's team. Michael will remain available for logic verification but no formal KT session is required.
*   **Support Model:** AI assists in logic derivation; Michael clarifies complex dependencies during development if needed.
*   **Visa Strategy:** Visa Type M confirmed. Alvin advised checking with Gopal and Ravi regarding self-processing methods while waiting for the invitation letter.
*   **Strategic Focus (New):** Michael to prioritize critical path items immediately upon return to mitigate tight timeline risks. Specific focus areas to be defined by Alvin.
*   **Contact Exchange:** On March 25, Alvin provided his mobile number (**93510653**) for direct coordination.

### **Pending Actions & Ownership**
| Action Item | Owner | Details/Context |
| :--- | :--- | :--- |
| **Focus Direction** | Alvin Choo | Communicate specific priority tasks to Michael immediately so he can prepare during his long weekend. |
| **Ticket Reassignment** | Alvin Choo | Assign Nikhil ticket to a BE from Daryl's team; allow self-learning with Michael support. |
| **Visa Application** | Michael Bui | Apply for multi-entry Type M visa immediately upon receiving invitation letter. Use Alvin's number (93510653). |
| **Invitation Letter** | Alvin Choo | Secure business letter from CoMall to expedite the visa process. |
| **Workshop Prep (Design)** | Michael Bui | Create docs detailing "as-is" vs. "to-be" flows; note: Returned April 2, targeting long weekend prep. |
| **Postmortem Review** | Alvin Choo | Final review after PDA impact verification (Vijay) and Advertima POV status inclusion. |

### **Key Dates & Milestones**
*   **April 2:** Michael returned to Singapore; leave period ended.
*   **April 3:** Public Holiday in Singapore.
*   **Upcoming Long Weekend:** Critical preparation window for Michael regarding tight project timeline.
*   **April 6:** Confirmed departure date for Wuhan, China.
*   **April 9:** Target PRD deployment deadline (Nikhil's requirement); UAT readiness targeted for April 7-8 if needed.
*   **End of Q1 2026:** Advertima POV pilot period concludes.


## [22/48] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Last Activity: 2026-04-02T05:12:44.547000+00:00 | Last Updated: 2026-04-02T06:42:31.949315+00:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
Continued instability in Mirakl/DBP integrations and persistent latency in `picklist-pregenerator` are joined by a resolved intermittent alert on Apple Pay transaction ratios. A new incident cluster occurred on **April 1**, while the `picklist-pregenerator` shows recurring critical latency (>3,600s). On **April 2**, Monitor `29851723` triggered and subsequently recovered, resolving a specific test alert regarding Apple Pay logs.

**Incident Summary & Timeline**
*   **Service: `fni-order-create` (Cluster of Errors) – Early Morning (Apr 1)**
    *   **Trigger Window:** Alerts began at **03:20:46 UTC**:
        *   "Failure occurred during fetching orders from DBP" (`Monitor ID 17447925`) triggered at **03:20:46 UTC**.
        *   "Error while calling APIs" (`17447928`) triggered at **03:20:51 UTC**.
        *   "Failure occurred during fetching orders" (`17447942`) triggered at **03:21:03 UTC**.
        *   "Exception Occurred At DBP Route" (`17447943`) triggered at **03:21:04 UTC**.
        *   "Exception Occurred At Mirakl Route" (`17447918`) triggered at **03:23:40 UTC**.
    *   **Recovery:** All monitors returned to normal between **03:25:46 UTC** and **03:28:39 UTC**. Total duration: ~8 minutes.

*   **Service: `picklist-pregenerator` (Latency Warning) – Late Night (Apr 1)**
    *   **Trigger:** P2 Warning "taking too long to complete" triggered at **23:01:23 UTC** on Apr 1.
    *   **Metric Value:** **3601.936s**.
    *   **Context:** Confirms a pattern of systemic degradation (>3,600s) across Mar 29 (3609.523s), Mar 30 (3608.92s), and Apr 1.

*   **Service: `fpon-seller-sap-picklist-reporter` (SAP Auth) – Historical**
    *   **Mar 27 Evening:** P1 alert "SAP authentication failed" (recovered in 5 mins).

*   **Service: Apple Pay Transaction Ratio (Monitor `29851723`) – April 2 Update**
    *   **Trigger:** [Test] Alert triggered at **04:56:45 UTC** on Apr 2. Condition met: >0.5 log events matched in the last 1h against query `formula("a / b").last("1h") > 0.5` for group `@request.payment_method:APPLE_PAY`.
    *   **Recovery:** [Recovered] Alert cleared at **05:12:44 UTC** on Apr 2. Condition met: <=0.5 log events matched.
    *   **Note:** This supersedes the "Mar 31 Afternoon" intermittent trigger noted in previous summaries, confirming the issue has persisted into April 2 before self-resolving.

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of the April 1 cluster affecting `fni-order-create` (Monitors `17447925`, `17447928`, `17447942`, `17447943`, `17447918`). Focus on DBP fetching failures, API errors, and Mirakl route exceptions.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Address critical latency in `picklist-pregenerator`. The recurrence of >3,600s execution times indicates continuous systemic failure.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Status Update:** Monitor `29851723` (Apple Pay) has recovered as of 05:12:44 UTC on Apr 2; no immediate action required unless recurrence is observed.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Summary for Leadership**
Instability persists in Mirakl and DBP integrations, marked by a cluster of six P2 alerts on **April 1** affecting `fni-order-create` between **03:20:46 UTC** and **03:28:39 UTC**. Concurrently, the `picklist-pregenerator` exhibits systemic latency degradation with values exceeding 3,600s on Mar 29, 30, and Apr 1 (current: 3601.936s). Additionally, Monitor `29851723` regarding Apple Pay transaction ratios triggered at **04:56:45 UTC** on April 2 but resolved automatically by **05:12:44 UTC**. Urgent engineering review is required for the Mirakl/DBP errors and systemic latency.


## [23/48] DPD x Platform Engineering
Source: gchat | Group: space/AAQAcjNXKpA | Last Activity: 2026-04-02T04:22:24.431000+00:00 | Last Updated: 2026-04-02T06:43:37.697132+00:00
**Daily Work Briefing: DPD x Platform Engineering**
*(Updated with April 2 P1 Incident IR-49 & Terraform Execution)*

**Key Participants & Roles**
*   **Kyle Nguyen:** Infrastructure/Platform Engineering (Reviewer, Incident Triage).
*   **Daryl Ng:** Incident Analyst.
*   **Gopalakrishna Dhulipati:** Addressed in new P1 incident; involved in Redis RCA.
*   **Sneha Parab:** Involved in Redis RCA.
*   **Alvin Choo:** Team Lead; escalated regarding April 2 P1 incident.
*   **Sampada Shukla:** Reported SLO alerts March 31; validated April 1 alerts.
*   **Dodla Gopi Krishna:** Owner of Fulfillment/Pricing SLOs; queried April 1 "Get serviceable area" journey.
*   **Maou Sheng Lee:** Initiated inquiry on April 2 regarding P1 incident status.
*   **Jazz Tong:** Provided Terraform run link for `infra-gcp-fpon-prod`.

**Main Topics & Discussions**
1.  **P1 Incident: IR-49 "Picking list not available" (April 2):** Maou Sheng Lee flagged the incident as "Active" and breaching group policy at ~03:36 UTC on April 2, requesting status updates and follow-up owners. The alert was directed to Alvin Choo and Gopalakrishna Dhulipati.
    *   *Status:* Incident remains Active P1; requires immediate resolution validation.

2.  **Terraform Execution (April 2):** Jazz Tong shared a Terraform run link (`run-g4Lg24A7Y21cJzPQ`) for the `infra-gcp-fpon-prod` workspace at ~04:22 UTC.
    *   *Status:* One reply received; last activity recorded shortly after.

3.  **Get Serviceable Area Journey Alert (April 1):** Dodla Gopi Krishna queried SLO V2 alert validation (~02:55 PM local time).
    *   *Status:* Thread active with ongoing verification by Sampada Shukla, Wai Ching Chan, and Akash Gupta.

4.  **High-Urgency Redis CPU Spike (March 30):** Kyle Nguyen reported `zs-fpon-prd-catalogue-service` hitting ~100% CPU in `asia-southeast1`.
    *   *Investigation Status:* Latency spikes from `go-catalogue-service` verified; latency normalized. No formal incident escalation required.

5.  **SLO Error Budget Alerts (March 31):** Sampada Shukla reported alerts regarding Fulfillment and Pricing tribes.
    *   *Status:* Acknowledged by Dodla Gopi Krishna; ongoing degradation in error budget consumption remains a concern.

**Pending Actions & Owners**
*   **Resolve P1 Incident IR-49:** Determine current status of "Picking list not available" breach and assign follow-up owner. *(Owners: Alvin Choo, Gopalakrishna Dhulipati, Maou Sheng Lee)*
*   **Validate Get Serviceable Area Alert:** Confirm accuracy of April 1 SLO V2 alert. *(Owners: Sampada Shukla, Wai Ching Chan, Akash Gupta)*
*   **Investigate Redis CPU Saturation:** Prioritize RCA for March 30 event. *(Owners: Daryl Ng, Gopalakrishna Dhulipati, Sneha Parab)*
*   **Address SLO Error Budget Alerts:** Prevent further depletion for Fulfillment and Pricing SLOs. *(Owner: Dodla Gopi Krishna)*
*   **Resolve Cluster Capacity Scaling:** Investigate March 23 memory limit failures. *(Owners: Kyle Nguyen, Nicholas Tan)*
*   **Restore Bastion Access:** Investigate PROD `asia-southeast1-c` inaccessibility. *(Owners: Nicholas Tan, Kyle Nguyen, Harry Akbar Ali Munir)*

**Decisions Made**
*   *Tentative:* Debate continues on Terraform-based change-freeze vs. direct Datadog UI management for on-call teams.
*   **QC Food Status:** Disabling confirmed on production (as of March 19); resource scale-down planning initiated pending ES confirmation.

**Key Dates & Follow-ups**
*   **April 2, ~03:36 UTC:** Maou Sheng Lee queried P1 incident IR-49 status; active breach noted.
*   **April 2, ~04:22 UTC:** Jazz Tong posted Terraform run `run-g4Lg24A7Y21cJzPQ`.
*   **April 1, ~05:16 AM:** Last reply recorded in SLO validation thread (8 unread messages).
*   **March 31, ~03:55 UTC:** Sampada Shukla reported SLO error budget alerts.
*   **March 30, ~03:00 UTC:** Redis CPU spike triggered; latency normalized.


## [24/48] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/8-Q3gLE8QP8 | Last Activity: 2026-04-02T03:58:51.220000+00:00 | Last Updated: 2026-04-02T06:43:59.904629+00:00
**Daily Briefing Update: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Lead/Coordinator.
*   **Andin Eswarlal Rajesh:** App Adoption Data.
*   **Onkar Bamane:** SKU/Data Operations.
*   **Gautam Singh:** Technical/Database Verification.
*   **Sneha Parab:** Data Enrichment & Stakeholder Management.
*   **Daryl Ng:** App Adoption.

**Main Topic**
Continued focus on the BCRS POS cutover, specifically SKU enrichment execution and database linkage validation. The group addressed the immediate execution of the SKU enrichment script for downloaded SKUs and confirmed resolution of specific missing linkage issues (SKUs 13280733, 13280736).

**Pending Actions & Owners**
*   **Gautam Singh:** Execute the SKU enrichment script for downloaded SKUs. Status: Assigned for execution by 14:00 on April 2, 2026 (confirmed via separate chat).
*   **Sneha Parab:** Await Gautam's update and request sharing of the Service Request (SR) draft for approval. Identify any blockers to proceeding with enrichment.
*   **Onkar Bamane:** Continue investigation into why 10 specific SKUs (13280794, 13280852, 13280864, 13281403, 13281448, 13281453, 13281688, 13281689, 13281710, 13281712) are not created in the DBP system. Confirm if data can be sent to FPON for the 361 SKUs with barcodes.
*   **Sneha Parab:** Obtain access to "BCRS - POS Cutover Plan.xlsx" and inform Jonathan Ho & Cheryl Ho upon completion of enrichment actions.
*   **Andin Eswarlal Rajesh / Daryl Ng:** Update app adoption numbers on the dashboard once current lag resolves (data reflects March 28).

**Decisions Made**
*   **Enrichment Execution:** Gautam Singh has confirmed readiness to execute the SKU enrichment script for downloaded SKUs today. The process is scheduled for completion by 14:00 on April 2, 2026.
*   **SR Approval Protocol:** Sneha Parab requires the SR from Gautam Singh prior to approval to ensure no blockers exist before proceeding.
*   **Technical Clarification:** SKUs **13280733** and **13280736** are confirmed as external to FPON scope; they should not exist in the internal database. This issue is closed.

**Key Data Points & Dates**
*   **Data Status (as of March 28):** Android adoption 75.6%; iOS adoption 86.38%.
*   **SKU Discrepancy:** Out of 837 newly created SKUs, barcodes exist for only 361. In the DBP system: Unique SKUs listed (361), Present in system (351), Active deposit linkages (349).
*   **Timeline Context:** Download scheduled for April 1, 2026. New discussion regarding script execution occurred on April 2, 2026 (03:56 – 03:58 UTC). Previous discussions spanned March 31 to April 1, 2026.

**Historical Context**
Previous actions regarding the 10 missing SKUs remain active pending investigation. The adoption timeline remains ~2 months to reach >95%, with growth slowing significantly after 85%. Gautam Singh has acknowledged the clarification regarding external SKUs in previous interactions.


## [25/48] [Prod Support] Offers
Source: gchat | Group: space/AAAAzZ3qkNU | Last Activity: 2026-04-02T03:48:03.820000+00:00 | Last Updated: 2026-04-02T06:44:29.176547+00:00
**Daily Work Briefing: [Prod Support] Offers**

**Key Participants & Roles**
*   **Willie Tan:** Reported initial issue (Mar 17) with offer visibility; escalated on Mar 26 regarding promo flow failure for specific SKUs.
*   **Angela Yeo:** Previously escalated discrepancy regarding incorrect promo display for SKU 13066243.
*   **Alvin Choo:** Previously flagged urgency and assigned owners for the initial case.
*   **Zaw Myo Htet & Daryl Ng:** Assigned to investigate both historical, new flow, and recent voucher issues.
*   **Neo Seng Ka:** Investigating database segment configuration (Mar 27).
*   **Tiffany Teo:** Raised query regarding [Drinks] Tier 1 - 4.4 Campaign [Unico] (Apr 2–8, 2026).
*   **Karen Chia:** Reported missing HPB voucher for customer e-wallet ticket #4446847; requested Zaw Myo Htet's assistance.

**Main Topic**
Investigation into production offer display errors and voucher availability spanning three distinct scenarios:
1.  **Historical Context (Mar 17–19):** Issues with Offer ID `sap offer 202603000112484` for **SKU 13066243**. The team confirmed "2 for $5.40" is the correct configuration, but it failed to display as expected while incorrect promotions were visible.
2.  **New Escalation (Mar 26):** Willie Tan reported that promos created in SAP are not flowing to FPON for a list of SKUs, despite items *not* being on the promo blacklist. A full investigation of the flow mechanism is required.
3.  **DBP Configuration Query (Mar 27):** Neo Seng Ka raised a query regarding DBP segment configuration ("union + dcc" logic), noting no results found when searching for "union."
4.  **Recent Voucher Issue (Apr 2):** Karen Chia reported a customer could not locate an HPB voucher in their e-wallet despite it being active and unexpired. This aligns with the broader flow/display investigation regarding SAP-to-FPON delivery.

**Pending Actions & Ownership**
*   **Action 1:** Investigate why correct offers ("2 for $5.40") are not displaying or if incorrect offers are showing for historical cases (SKU 13066243).
*   **Action 2:** Investigate the root cause of promo flow failure from SAP to FPON for SKUs not on the blacklist (Willie Tan, Mar 26).
*   **Action 3 (New):** Clarify DBP segment logic regarding "union + dcc" configurations and confirm why no applicable segments were found in the database.
*   **Action 4 (New):** Investigate missing HPB voucher for customer ticket #4446847; verify if the campaign logic or e-wallet sync is at fault.
*   **Owners:** @Zaw Myo Htet, @Daryl Ng (assigned to all issues). @Neo Seng Ka (DBP config). @Karen Chia/Willie Tan/Customer context for voucher case.
*   **Status:** Active/Urgent. Scope has expanded from single SKU display errors and DBP logic gaps to a systemic flow issue affecting multiple SKUs and live customer vouchers.

**Decisions Made**
No final technical fixes have been implemented yet. The team established the expected outcome for historical cases: offers must display "2 for $5.40." For the new SAP-to-FPON case, it is confirmed that affected SKUs should be eligible but are failing to receive promos. Neo Seng Ka's inquiry suggests a potential gap in DBP "union + dcc" segment logic contributing to flow failures. The HPB voucher incident (ticket #4446847) requires immediate validation of the campaign delivery mechanism for the [Drinks] Tier 1 - 4.4 Campaign period.

**Key Dates & Deadlines**
*   **Initial Issue Reported:** March 17, 2026 (09:01 AM).
*   **New Flow Issue Reported:** March 26, 2026 (02:24 AM UTC) by Willie Tan.
*   **DBP Query Raised:** March 27, 2026 (06:17 AM UTC) by Neo Seng Ka.
*   **New Voucher Report:** April 2, 2026 (approx. 4:00 AM UTC) regarding ticket #4446847.
*   **Campaign Period:** [Drinks] Tier 1 - 4.4 Campaign runs Apr 2–8, 2026.
*   **Deadline:** Immediate resolution requested for all display errors and voucher availability issues.

**Reference Links & IDs**
*   **Chat Space URL:** https://chat.google.com/space/AAAAzZ3qkNU
*   **Historical Offer ID:** `sap offer 202603000112484`
*   **Historical SKU:** 13066243
*   **Customer Ticket:** #4446847 (HPB Voucher issue)
*   **System Components:** SAP, FPON, DBP.


## [26/48] #dpd-dba
Source: gchat | Group: space/AAAAMh7T8Y0 | Last Activity: 2026-04-02T03:42:02.739000+00:00 | Last Updated: 2026-04-02T06:46:05.151650+00:00
**Daily Work Briefing: #dpd-dba (Updated)**

**Key Participants & Roles**
*   **Akash Gupta:** DBA Team Representative/Requestor.
*   **Wai Ching Chan:** Deployment Coordinator (Service Owner).
*   **Tiong Siong Tee:** Communication Initiator.
*   **Maou Sheng Lee:** Advisor.
*   **Gopalakrishna Dhulipati:** Primary DBA Contact (Active on recent urgent tickets and new incident).
*   **Saranga Colambage, Kim Tong Ng:** New responders to the password update request.
*   **Sampada Shukla, Hanafi Yakub, Dodla Gopi Krishna, Alvin Choo, Natalya Kosenko, Lester Santiago Soriano, Borja Adrian Dominguez:** DBA Team/Stakeholders.

**Main Topic**
The conversation covers executing critical Jira service tickets for production/pre-production updates (order zone IDs, picking zones) and investigating GKE Autopilot scale-down incidents. **New Focus:** An urgent incident regarding the WMS Integration deployment failure in Production due to a database password mismatch, requiring immediate secret rotation.

**Pending Actions & Owners**
*   **Fix Prod DB Secret (NEW URGENT):**
    *   **Action:** Update database password/secret for `wms-integration-app-user` in Cloud SQL Proxy to resolve "Access denied" errors.
    *   **Context:** WMS Integration deployment failed with Error 1045; incident referenced as follow-up to DSD-10589.
    *   **Owner:** DBA Team (Tagged: @Gopalakrishna Dhulipati, @Saranga Colambage, @Kim Tong Ng).
    *   **Status:** **Active Incident.** Reported Apr 2, 2026 at 03:42 UTC. Requires immediate secret rotation in `fpg-jarvis-prod`.
*   **Execute DSD-11124 Ticket (Pork Products):**
    *   **Action:** Insert new picking zone ("Pork products") into the picking service table for Prod and Pre-prod.
    *   **Owner:** DBA Team (@Gopalakrishna Dhulipati).
    *   **Status:** **APPROVED**. Submitted Mar 27 at 12:55 UTC; requires immediate execution.
*   **Approve URGENT Patch DSD-11122 & DSD-11119:**
    *   **Action:** Patch `orders` zone ID for specific statuses (non-COMPLETED/CANCELLED and general).
    *   **Owner:** DBA Team (@Gopalakrishna Dhulipati, @Alvin Choo, @Natalya Kosenko, @Akash Gupta).
    *   **Status:** Requires immediate approval; requested Mar 27.
*   **Execute DSD-11003 Ticket:**
    *   **Action:** Add `container_deposit` column to `order_service.order_items`.
    *   **Owner:** DBA Team (Akash Gupta).
    *   **Status:** Pending execution if not completed; initial request Mar 6.
*   **Investigate SLO Impact & Proxy Scale-Down:**
    *   **Action:** Investigate "bad connection" errors caused by `sqlproxy-prod-ap` GKE Autopilot scale-downs.
    *   **Owner:** @Gopalakrishna Dhulipati, @Dodla Gopi Krishna.
    *   **Status:** Reported Mar 25; critical SLO risk.

**Decisions Made**
*   `container_deposit` column (JSON, NULL default) to be added via transaction for DSD-11003.
*   Ticket DSD-11124 is approved and ready for execution.
*   Future requests must explicitly name the specific DB owner (per Maou Sheng Lee).
*   **New Decision:** Secret rotation for `wms-integration-app-user` is prioritized over standard deployment windows due to active production failure.

**Key Dates & Updates**
*   **Mar 6, 2026 (01:48 UTC):** Initial request for DSD-11003.
*   **Mar 9, 2026 (04:36 UTC):** Deployment window scheduled; script shared.
*   **Mar 25, 2026 (05:52 UTC):** SLO impact report regarding GKE scale-downs.
*   **Mar 27, 2026 (03:12–12:55 UTC):** Series of urgent tickets submitted and approved (DSD-11119, DSD-11122, DSD-11124).
*   **Apr 2, 2026 (03:42 UTC):** **New:** Akash Gupta reports WMS deployment failure in Prod due to DB password error; flags incident for immediate fix.

**References**
*   **Jira Tickets:** `DSD-11003`, `DSD-11119` (Urgent), `DSD-11122` (Urgent), `DSD-11124` (Approved), **New: DSD-10589** (Preceding incident context).
*   **Database:** `fpon.order_service.order_items`, Picking service tables, Cloud SQL (`wms-integration-app-user`).
*   **Affected Cluster:** `sqlproxy-prod-ap` (GKE Autopilot), `fpg-jarvis-prod`.
*   **Error Log:** Panic: "failed to ping database: Error 1045 (28000): Access denied for user 'wms-integration-app-user'".


## [27/48] RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU | Last Activity: 2026-04-02T02:37:49.662000+00:00 | Last Updated: 2026-04-01T06:45:51.125189+00:00
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


## [28/48] RMN Notification
Source: gchat | Group: space/AAQA85dw4So | Last Activity: 2026-04-02T03:21:03.482000+00:00 | Last Updated: 2026-04-02T06:48:53.472296+00:00
**Daily Work Briefing: Automated Test Results Summary (RMN Notification)**

**Key Participants & Roles**
*   **Collection Runner App:** Automated testing agent executing API suites.
*   **Webhook Bot:** Reporting mechanism; consistently returning "unable to process your request" on all notifications through April 2, 2026.
*   **Parties Involved:** System-generated notification log only.

**Main Topic/Discussion**
Automated nightly API test executions across `promo-service`, `marketing-personalization-service`, and `marketing-service` in the **staging** environment. Monitoring period spans March 12 through **April 2, 2026**. Execution windows occur at approximately 01:05 UTC (morning), 02:30/02:31 UTC (midnight), and **03:21 UTC** (early morning).

**Test Execution Status & Anomalies**
*   **`marketing-service`:** Stability streak broken.
    *   **April 2, 01:05 UTC:** Mixed results. API Contract Tests passed (20 Passed / 0 Failed), but API Tests failed (44 Passed / **3 Failed**).
    *   **Historical Context:** While stability was confirmed March 26–April 1, the recurrence of failures on April 2 indicates a return to instability patterns similar to the March 17–25 window.
*   **`promo-service`:** Confirmed stable on April 2 at **02:31 UTC**.
    *   **API Contract Tests:** 6 Passed / 0 Failed.
    *   **API Tests:** 10 Passed / 0 Failed.
    *   Stability confirmed for March 26–April 2.
*   **`marketing-personalization-service`:** **STATUS UPDATED.** Contrary to prior logs indicating no data, the service successfully executed on April 2 at **03:21 UTC**.
    *   **[API Contract Tests]:** 125 Passed / 0 Failed / 0 Skipped (Total Requests: 21).
    *   **[API Tests]:** 96 Passed / 0 Failed / 0 Skipped (Total Requests: 21).

**Pending Actions & Ownership**
*   **Webhook Bot Remediation (High Priority):** The bot failed to process requests in every notification cycle from March 12 through the latest log on **April 2 at 03:21 UTC**. Immediate attention is required from DevOps or Automation Infrastructure.
*   **Investigate `marketing-service` Regression:** Engineering must immediately analyze the root cause of the 3 API test failures observed on April 2, 01:05 UTC, following a period of apparent stability.

**Decisions Made**
*   No human decisions recorded; all entries are automated system outputs.

**Key Dates & Deadlines**
*   **Failure Window (Historical):** Instability noted March 12–13 and persistently from **March 17 through March 25**.
*   **Current Status:** Mixed results on April 2.
    *   `marketing-service`: Failed API tests at 01:05 UTC.
    *   `promo-service`: Passed at 02:31 UTC.
    *   `marketing-personalization-service`: **Fully successful** run recorded at 03:21 UTC (125/96 passed).
*   **Monitoring Period:** Data covers runs from **March 12, 2026**, through **April 2, 2026**.

**Resource Info**
*   **Message Count:** Updated to reflect notifications through April 2.
*   **URL:** https://chat.google.com/space/AAQA85dw4So


## [29/48] D&T Funtastic Team
Source: gchat | Group: space/AAQARGCS1Wk/5YZW6i2wniE | Last Activity: 2026-04-02T02:07:15.235000+00:00 | Last Updated: 2026-04-02T02:37:32.835999+00:00
**Daily Work Briefing: D&T Funtastic Team**

**Key Participants & Roles**
*   **Trina Boquiren:** Initiator, project lead for the International Food Day eDM design selection. Recently issued an urgent deadline for voting and confirmed she will finalize and send out the event invite immediately upon closing votes.
*   **Team (@all):** Stakeholders responsible for reviewing options and casting votes.

**Main Topic**
Selection of the final email design (eDM) for the upcoming **International Food Day**. Trina presented three shortlisted design concepts to gather team consensus. The process has shifted from general voting requests to a strict deadline-driven selection.

**Pending Actions & Ownership**
*   **Action:** Submit votes for the top design options by **12:00 PM (local time) on April 2, 2026**.
*   **Owner:** All team members.
*   **Context:** Trina Boquiren sent a direct message at 02:07 UTC on April 2, 2026, stating: "Send in your votes by 12pm today as I'll be sending out the invite this afternoon." Immediate participation is required to finalize the design before the invitation dispatch.

**Decisions Made**
*   The final decision remains pending and is contingent upon votes received by the 12:00 PM deadline on April 2, 2026. Once the deadline passes and Trina confirms receipt of votes, she will proceed to send out the official event invite that afternoon.

**Key Dates & Follow-ups**
*   **Event:** International Food Day (Upcoming).
*   **Discussion Timeline:**
    *   **March 31, 2026:** Initial design posting occurred between 06:11 and 06:14 UTC; voting requested at 06:07 UTC.
    *   **April 1, 2026 (09:17 UTC):** Trina Boquiren issued a follow-up reminder to the @all channel urging immediate participation.
    *   **April 2, 2026 (02:07 UTC):** Trina Boquiren set a hard deadline of **12:00 PM today** for vote submission, linking completion directly to the afternoon distribution of event invites.
*   **Next Step:** Team members must vote before 12:00 PM on April 2. Post-deadline action is the dispatching of the final invite by Trina.

**Reference Data**
*   **Space URL:** https://chat.google.com/space/AAQARGCS1Wk
*   **Message Count:** 6 (Updated to reflect new reminder).
*   **Options Presented:** Option 1, Option 2, Option 3.


## [30/48] DPD AI Guild
Source: gchat | Group: space/AAQA5_B3lZQ/DIiDn7sJXrg | Last Activity: 2026-04-02T01:50:07.450000+00:00 | Last Updated: 2026-04-02T02:37:45.530915+00:00
**Daily Work Briefing: DPD AI Guild Chat Summary**

**Key Participants & Roles**
*   **Nicholas Tan:** Contributor; expresses skepticism regarding Microsoft Copilot's enterprise viability and legal posture.
*   **Maou Sheng Lee:** Contributor; agrees with critiques of corporate messaging and hypocrisy in AI usage terms.
*   *Note: No formal roles (e.g., Lead, Manager) are explicitly defined in the provided log.*

**Main Topic/Discussion**
The group discussed the legitimacy and safety of using **Microsoft Copilot** for work purposes, specifically analyzing its Terms of Service (TOS).
*   **Nicholas Tan** shared a link to the Microsoft Copilot TOS for individuals, characterizing the document's tone as overly cautious ("afraid") regarding potential AI errors. He labeled the tool a "toy" unsuitable for professional use and criticized Microsoft as a company that merely "piggybacked on OpenAI."
*   **Maou Sheng Lee** concurred, highlighting the contradiction in capitalists promoting public use of these tools while simultaneously shifting liability to users ("at own risks"). They described the corporate messaging as containing "never ending contradicting words."

**Pending Actions & Ownership**
*   **None identified.** The conversation is purely analytical and critical; no tasks, research assignments, or follow-up actions were assigned.

**Decisions Made**
*   **No formal decisions** were recorded in this thread. The participants collectively expressed a negative sentiment regarding the readiness of Microsoft Copilot for production work, but this remains an opinion rather than a ratified team decision.

**Key Dates & References**
*   **Date:** April 2, 2026 (Timestamps: 01:28 AM – 01:50 AM UTC).
*   **Resource Link:** https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/termsofuse
*   **Space URL:** https://chat.google.com/space/AAQA5_B3lZQ

**Summary Note**
The discussion reflects individual sentiment regarding AI tool maturity and legal risk mitigation strategies rather than operational coordination. No immediate action items require attention for the daily workflow.


## [31/48] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/1UILrDfoupI | Last Activity: 2026-04-02T01:31:46.818000+00:00 | Last Updated: 2026-04-02T02:38:23.365143+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Resource:** [Leads] (Ecom/Omni) Digital Product Development
**Date of Discussion:** April 1–2, 2026
**Participants:** Sneha Parab, Daryl Ng, Gopalakrishna Dhulipati, Andin Eswarlal Rajesh

**Key Participants & Roles**
*   **Sneha Parab:** Product/Functional Lead driving migration strategy and operational workflows.
*   **Daryl Ng:** Technical Lead providing feasibility assessments.
*   **Gopalakrishna Dhulipati:** Contributor offering account suspension strategy for specific segments.
*   **Andin Eswarlal Rajesh:** Stakeholder identified for UI/UX roadmap prioritization.

**Main Topic**
Strategies to prevent migrated customers from placing orders in the legacy B2B platform while retaining B2C access, and defining migration workflows for dual-channel users.

**Discussion Summary & Decisions**
*   **Initial Technical Feasibility (April 1):** Sneha Parab queried if selective blocking of B2B order placement was possible. Daryl Ng initially indicated full user blocking was technically infeasible due to shared login systems for B2C access.
*   **Risk Assessment:** Sneha Parab noted that removing payment methods is ineffective for customers using credit terms or gateways like "GE Biz" and "QuickBuy." The consensus shifted toward operational workarounds rather than strict technical blocking.
*   **New Strategy: Account Suspension (April 2):** Gopalakrishna Dhulipati proposed suspending accounts for users who do not place B2C orders. He noted that the initial migrated cohort consists primarily of schools, making this approach "safe to suspend."
*   **Data Verification:** Sneha Parab agreed to validate the number of customers who do not place B2C orders to determine the viability of suspension during gradual migration.
*   **Alternative Workflows (April 2):** If suspension is not feasible for specific users, Gopalakrishna outlined two options:
    1.  Alert Business and Operations teams to manually cancel legacy orders or redirect customers.
    2.  Enhance the current DBP system to support this logic (requiring roadmap prioritization).
*   **UX Intervention:** Sneha Parab announced a plan to implement a popup on the legacy B2B platform for migrated users, informing them to use the new portal with a CTA redirecting to the new site.

**Pending Actions & Ownership**
*   **Action:** Analyze and provide a list of customers who do not place B2C orders to assess suspension feasibility.
    *   **Owner:** Sneha Parab
*   **Action:** Prioritize roadmap efforts for two potential solutions:
    1.  Enhancing the DBP system to support migration logic.
    2.  Implementing the legacy portal popup with redirect CTA.
    *   **Owner:** Sneha Parab (aligned with Andin Eswarlal Rajesh)
*   **Action:** Prepare effort estimates for the DBP enhancement and roadmap submission.

**Key Dates & Follow-ups**
*   **Initial Discussion:** April 1, 2026.
*   **Strategy Update:** April 2, 2026 (Suspension proposal and UX popup planning).
*   **Next Milestone:** Immediate verification of the non-B2C customer list to finalize the migration approach for school accounts.

**Reference URLs**
*   Chat Space: https://chat.google.com/space/AAQAN8mDauE


## [32/48] DPD AI Guild
Source: gchat | Group: space/AAQA5_B3lZQ | Last Activity: 2026-04-02T01:28:01.028000+00:00 | Last Updated: 2026-04-02T02:38:56.895981+00:00
### Daily Work Briefing: DPD AI Guild

**1. Key Participants & Roles**
*   **Michael Bui:** Research/Technical Lead – Introduced the new model release.
*   **Zaw Myo Htet:** Technical Strategy/Engineering – Proposed optimization strategy and cost reduction.
*   **Nicholas Tan:** Strategic Monitor – Highlighted industry trends regarding AI executive automation (Meta) and recently critiqued consumer Copilot terms of service.
*   **Oktavianer Diharja:** Engineering Support – Suggested relevant Go skill utility libraries.

**2. Main Topic**
The discussion centered on leveraging **Mistral Small 4** to optimize local knowledge handling via quantization (Unsloth) to reduce RAG dependency, contextualized by Meta's "AI CEO" automation shift. On March 30, the conversation broadened to include engineering tooling (`samber/cc-skills-golang`). On April 2, Nicholas Tan introduced a critical risk assessment regarding consumer-grade AI assistants, citing Microsoft's restrictive Terms of Service as evidence of liability concerns in production environments.

**3. Pending Actions & Ownership**
*   **Action:** Evaluate feasibility of replacing heavy RAG pipelines with quantized open-weight models to reduce costs.
    *   **Owner:** Zaw Myo Htet
    *   **Context:** Requires further technical assessment based on Unsloth documentation.
*   **Action:** Investigate integration of Mistral Small 4's specific architecture (MoE, 119B total/6B active parameters) into current workflows.
    *   **Owner:** TBD (Team-wide due to recent announcement).
*   **Action:** Analyze the implications of Meta's "AI CEO" model on our autonomous agent roadmap.
    *   **Owner:** Nicholas Tan / Team
    *   **Context:** Assess if similar high-level executive automation patterns are applicable to DPD workflows given the efficiency gains in large-scale operations.
*   **Action (New):** Review Microsoft Copilot Terms of Service to define risk boundaries for internal AI usage.
    *   **Owner:** Nicholas Tan
    *   **Context:** Analyze the "toy" designation and liability clauses (https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/termsofuse) to determine why consumer tools are unsuitable for DPD work compared to our proposed autonomous agent stack.
*   **Action (Existing):** Evaluate utility of `samber/cc-skills-golang` for managing AI agent skills or context within Go-based infrastructure.
    *   **Owner:** Oktavianer Diharja / Engineering Team

**4. Decisions Made**
*   **Strategic Alignment:** The team acknowledged that while Mistral Small 4 offers specific architectural benefits for cost reduction, the broader industry (exemplified by Meta) is moving toward high-level autonomous agents. This suggests future DPD AI initiatives should balance model quantization with agent-based autonomy.
*   **Risk Assessment:** Nicholas Tan concluded that consumer-grade copilots are "toys not for work" due to restrictive legal frameworks and liability fears evident in Microsoft's Terms of Service. The team agreed to avoid relying on such tools for production workflows, reinforcing the need for custom-built solutions or strictly governed enterprise models.
*   **Tooling Consideration:** The `samber/cc-skills-golang` library has been flagged for potential use in standardizing skill management for Go-integrated agents, pending technical review by Oktavianer Diharja.

**5. Key Dates & References**
*   **2026-03-17:** Michael Bui announced the release of **Mistral Small 4**.
    *   *Specs:* MoE Architecture, 119B total parameters (6B active), 256k context window, Vision capability.
*   **2026-03-19:** Zaw Myo Htet suggested utilizing **Unsloth** for quantization to make open-weight models more cost-effective and reduce RAG reliance.
*   **2026-03-24:** Nicholas Tan shared an article detailing Mark Zuckerberg's launch of an AI CEO bot to manage Meta operations.
    *   *Relevance:* Highlights the maturity of agentic workflows for executive-level tasks.
*   **2026-03-30:** Oktavianer Diharja recommended the `cc-skills-golang` library for potential skill management integration.
*   **2026-04-02T01:28:01:** Nicholas Tan flagged Microsoft Copilot Terms of Service, labeling it a "toy not for work" due to liability concerns.
    *   *Reference:* https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/termsofuse

**Thread Status:** Active (Last reply noted 43 minutes ago relative to briefing generation).


## [33/48] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Last Activity: 2026-04-02T00:03:09.886000+00:00 | Last Updated: 2026-04-02T02:41:03.249446+00:00
**Daily Work Briefing Summary (Updated: April 2, 2026)**

**Main Topics & Discussions**
1.  **Programmatic Advertising:** Focus remains on validating discrepancies for `advertima_ttd-fixed-price-test-1.5`. Ravi Singh confirmed receipt of raw BURLs; validation was targeted for Monday, March 17th. Yian Koh requested confirmation on deals `advertima_ttd-first-price-test` and `advertima_ttd-fixed-price-test-1`.
2.  **New Deal Setup:** Yasmina Tregan (Advertima) requires an end-to-end test setup this week. Wei Phung to share live campaign details; Ravi Singh to execute setup, push to TradeDesk, and map segments before launch.
3.  **BCRS UAT & Finance Integration:** Progress continues on SAP document numbers, duplicate posting fixes via PubSub "exactly once" policy (PR #1033), and Bukit Timah Plaza pricing/display issues.
4.  **Event Sync Optimization (DPD-645):** Addressing the massive event overage (14M vs. normal 550k). PRD deployment plan set for Sunday, March 15.
5.  **Security & Compliance:** RMN Pentest fixes (DPD-700) deployed to Prod; Bitbucket App Passwords deprecated effective June 9, 2026.

**Status Update: Inbox & Communications**
*   **Inbox Status:** As of April 2, 2026 (00:03 UTC), the workspace inbox is fully caught up across all categories (**Urgent Action Items**, **Meeting Updates**, and **FYI**). No pending unread items require immediate attention. This status follows confirmations from daily summaries dated March 24 through April 1. The latest update from Workspace Studio confirms zero backlog in all sections, including Code Reviews and Project Updates.

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
*   **April 2, 2026:** Daily inbox review completed; no new urgent items identified across any category.
*   **June 9, 2026:** Bitbucket App Password deprecation deadline.

**Note on New Content:** The daily summary from April 2, 2026 (00:03 UTC), via Workspace Studio confirms the inbox remains clear of urgent action items across all categories (**Urgent Action Items**, **Meeting Updates**, and **FYI**). No changes to pending actions or decisions were required based on this update; historical context regarding project statuses and deadlines remains valid.


## [34/48] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/ODwikuuIYPU | Last Activity: 2026-04-01T10:15:12.442000+00:00 | Last Updated: 2026-04-01T10:38:12.506146+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Initiator of the invitation request.
*   **Daryl Ng:** Coordinator responsible for sending invitations; owner of "Search & Agolia context" knowledge.
*   **Tiong Siong Tee:** Stakeholder requesting information; confirmed receipt of the invitation.

**Main Topic**
The discussion centers on expanding the participant list for the "Project Light Attack and Defence Leads" space and scheduling a follow-up session to discuss technical search and Agolia context details.

**Decisions Made**
*   **Invitation Authorization:** Alvin Choo confirmed that an additional person should be invited to the group chat.
*   **Action Execution:** Daryl Ng successfully executed the invitation immediately after confirmation (06:45).
*   **Knowledge Sharing Commitment:** Tiong Siong Tee and Daryl Ng agreed that a discussion regarding "search & agolia context" is required, with Daryl Ng confirming his availability to provide this context.

**Pending Actions & Owners**
*   **Action:** Conduct a meeting or session to review search and Agolia context.
    *   **Owner:** Tiong Siong Tee (to find/schedule) and Daryl Ng (to provide context).
    *   **Status:** Awaiting scheduling; Daryl has verbally committed ("can") but no specific time is set yet.

**Key Dates, Deadlines & Follow-ups**
*   **2026-04-01 06:44:36 UTC:** Alvin Choo requested an invitation.
*   **2026-04-01 06:45:09 UTC:** Daryl Ng confirmed the person was invited.
*   **2026-04-01 08:11:05 UTC:** Tiong Siong Tee acknowledged receipt of the invitation ("thanks").
*   **2026-04-01 10:15:02 UTC:** Tiong Siong Tee initiated the request for the search/Agolia context session, tagging Daryl Ng.
*   **2026-04-01 10:15:12 UTC:** Daryl Ng confirmed availability to meet on this topic.

**Reference Links**
*   Chat Space URL: https://chat.google.com/space/AAQAsFyLso4


## [35/48] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/pA7_pZifIOE | Last Activity: 2026-04-01T10:09:56.915000+00:00 | Last Updated: 2026-04-01T10:38:36.810186+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Project Lead/Coordinator.
*   **De Wei Tey:** Technical Owner/RPA Lead (managing deployments, RPA logic, and production pushes).
*   **David Anura Cooray:** QA/Testing Lead.
*   **Joey Ang Hui Xin:** Operations/Front-end Tester (executing live order placement/refunds).
*   **Hendry Tionardi & Onkar Bamane:** Finance/System Integration (monitoring SAP, managing reversals).
*   **Zack Chan & Binte Abdul Karim Kamilah:** CS/Finance Support (handling manual fee refunds).

**Main Topic**
Validation and production deployment of the RPA refund feature for **BCRS (Scan & Go)**. The discussion confirmed live testing success for specific SKUs, managed financial reversals for test transactions, and addressed a user request regarding the non-automated refund of packing and delivery fees.

**Decisions Made**
1.  **RPA Scope Confirmation:** Confirmed RPA performs BCRS refunds but does not automatically cover packing/delivery fees. Manual intervention is required for these specific fees.
2.  **Manual Fee Refund Protocol:** For Order ID `259022496`, manual refund of packing and delivery fees ($8.99) was triggered by Finance/CS after confirmation that RPA does not cover these charges.
3.  **Ticket Closure:** CS ticket (ID: 4468575) regarding the live test refund was approved for closure after all refunds (SKU, BCRS, and fees) were processed.

**Pending Actions & Ownership**
*   **Manual Fee Refund Completion:** Confirmed completed by **Binte Abdul Karim Kamilah**.
    *   *Amount:* $8.99 (Delivery and Service fee).
    *   *Order ID:* `259022496`.
*   **Finance Reversal of Test Refund:** Finance to revert the test refund transaction generated during live testing.
    *   *Order IDs:* `259017167` (iOS), `259018320` (Android), and `259022496`.
    *   *Owner:* **Onkar Bamane** to inform Finance; **De Wei Tey** confirmed the RPA will refund these orders.
*   **SAP Monitoring:** Continued monitoring of SAP postings for test transactions.
    *   *Owner:* **Hendry Tionardi**.

**Key Dates & Deadlines**
*   **Critical Deadline:** **1 April 2026** (All sign-offs confirmed completed).
*   **Testing Execution Date:** **31 March 2026** (Live testing conducted between 06:26 and 07:32 UTC+8).
*   **Refund Log Timestamps:** Updates recorded on **1 April 2026** between 08:35 and 10:09 UTC+0.

**Specific References & New Findings**
*   **Tested Order ID:** `259022496`.
    *   *SKU:* 13280919 (BCRS).
    *   *RPA Refund Amount:* $0.10.
    *   *Outcome:* RPA successfully refunded SKU and BCRS amount; Packing/Delivery fees ($8.99) required manual processing by **Binte Abdul Karim Kamilah**.
*   **Zendesk Ticket:** `4468575`. Routed to store, then escalated for fee refund assistance. Closed after resolution.
*   **Environment:** Testing confirmed in the Live Environment at 07:19 UTC+8 equivalent.

**Status Update**
Live testing for BCRS refunds is successful regarding SKU and BCRS amounts. A procedural gap was identified where packing/delivery fees are excluded from automated RPA flows; this has been mitigated via manual processing for the test transaction. No impact on First Response or other CS automated processes remains.


## [36/48] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Last Activity: 2026-04-01T09:54:27.077000+00:00 | Last Updated: 2026-04-01T10:39:12.206525+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Sneha Parab:** Lead/Manager; coordinating cross-team support, SAP/API integration blockers. Recently queried B2B user blocking logic for migrated customers.
*   **Michael Bui:** Engineering/RMN Architect; identified root cause for RMN incident and preparing UAT verification.
*   **Daryl Ng:** Investigating store network ownership and Omni Home data discrepancies. Flagged Linkpoints eligibility issue (April 1). Inquired about learning budget (Sundy's course) and S&G Store Enabling SOP adherence. Currently replying to B2B blocking use case discussion.
*   **Alvin Choo:** Leadership; addressing approval workflows for weekend deployments. Also consulted regarding Sundy's training budget inquiry.
*   **Gopalakrishna Dhulipati:** On Child Care Leave until Wednesday (April 2). Will reach out individually if assistance is required to rep tasks.

**Main Topics & Updates**
1.  **RMN Incident & Deployment Status:** Michael Bui identified the root cause and implemented a fix. Daryl Ng confirmed active inquiry regarding deployment status on March 31 (01:44 UTC). Immediate guidance remains required on weekend (Sat/Sun) deployment protocols, requiring an approval request to Hui Hui.
2.  **Linkpoints Eligibility Issue:** On April 1 at 03:13 UTC, Daryl Ng flagged that Wei Sing's team enabled "Linkpoints eligible" in SAP, but it remains disabled in DBP. Investigation is underway.
3.  **Search Performance Drop:** Investigation continues regarding the severe 60–70% impression decline since March 18/19. The RMN root cause fix may correlate with these symptoms; release timing remains contingent on this investigation and UAT success.
4.  **B2B Order Blocking Use Case (New):** Sneha Parab proposed blocking migrated customers from placing orders in the existing B2B platform by identifying user types during migration. Active discussion ongoing between Sneha and Daryl Ng.
5.  **S&G Store Enabling SOP:** Daryl Ng queried on April 1 (09:18 UTC) regarding current adherence to the "S+G Store Enabling - SOP" document. Thread has generated 18 replies; last reply by Sneha Parab 41 minutes ago.
6.  **Learning Budget Inquiry:** On April 1 at 06:51 UTC, Daryl Ng asked Alvin Choo if the learning budget is still available for Sundy to attend a specific course.

**Pending Actions & Owners**
*   **RMN Deployment Verification:** Confirm if the fix has been deployed following Daryl Ng's inquiry and proceed with UAT verification. Send approval request to Hui Hui for weekend deployment if applicable. (Owner: Michael Bui; Coordination: Alvin Choo/Hui Hui/Daryl Ng)
*   **Linkpoints Investigation:** Verify why "Linkpoints eligible" is disabled in DBP despite SAP enablement by Wei Sing's team. Follow up with Daryl Ng/Sneha Parab. (Owner: To be assigned/Wei Sing's team; Coordination: Sneha Parab/Daryl Ng)
*   **B2B Logic Feasibility:** Evaluate technical possibility of blocking migrated users from B2B orders based on identification logic. (Owner: Engineering Team; Discussion Owner: Daryl Ng/Sneha Parab)
*   **SOP Adherence Confirmation:** Clarify current status of the S&G Store Enabling SOP to address Daryl Ng's query. (Owner: To be assigned; Coordination: Sneha Parab/Daryl Ng)
*   **Training Budget Check:** Confirm availability of learning budget for Sundy's course request. (Owner: Alvin Choo/Sundeep's team lead)
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


## [37/48] Release - FPG Back Office (Mon-Thurs)
Source: gchat | Group: space/AAAAoJgpZBM | Last Activity: 2026-04-01T09:14:20.453000+00:00 | Last Updated: 2026-04-01T10:40:38.072140+00:00
**Daily Work Briefing: FPG Back Office Releases (Updated)**

**Key Participants & Roles**
*   **Rohit Pahuja:** Primary communicator for scheduled releases.
*   **Jonathan Tanudjaja:** Executor for previous urgent release v8.37.1.
*   **Minu Varghese:** New executor for immediate release v8.37.2 (effective April 1, 2026).

**Main Topic**
The conversation tracks confirmed software deployment schedules for the **Back Office** system across versions **v8.35.0**, **v8.36.0**, **v8.37.0**, **v8.37.1**, and the newly announced urgent release of **v8.37.2**. All updates align with the FPG Back Office (Mon-Thurs) resource schedule.

**Pending Actions & Ownership**
*   **Action:** Monitor the Back Office system during release execution for all scheduled versions.
    *   **Owner:** Team.
*   **Action:** Review specific release notes upon receipt.
    *   **Owner:** Team members referencing provided links.
*   **New Action:** Execute deployment of version **v8.37.2** immediately.
    *   **Owner:** Minu Varghese.
    *   **Note:** Release notes to be shared shortly by the executor.

**Decisions Made**
No new strategic decisions were made; messages confirm a sequence of five deployment plans:
1.  Deployment of **Backoffice_v8.35.0**.
2.  Deployment of **Backoffice_v8.36.0**.
3.  Deployment of **Backoffice_v8.37.0**.
4.  Deployment of **Backoffice_v8.37.1** (Completed March 25, 2026).
5.  **Deployment of Backoffice_v8.37.2** (Newly initiated by Minu Varghese on April 1, 2026).

**Key Dates, Deadlines, & Follow-ups**
*   **Release 1:**
    *   **Version:** Backoffice_v8.35.0
    *   **Announced:** March 9, 2026, at 05:11 UTC.
    *   **Scheduled Execution:** ~1:20 PM on March 9, 2026.
*   **Release 2:**
    *   **Version:** Backoffice_v8.36.0
    *   **Announced:** March 12, 2026, at 13:44 UTC.
    *   **Scheduled Execution:** Same day (March 12, 2026).
*   **Release 3:**
    *   **Version:** Backoffice_v8.37.0
    *   **Announced:** March 24, 2026, at 02:17 UTC.
    *   **Scheduled Execution:** Same day (March 24, 2026).
*   **Release 4:**
    *   **Version:** Backoffice_v8.37.1
    *   **Announced:** March 25, 2026, at 02:33 UTC.
    *   **Scheduled Execution:** Today (March 25, 2026) by Jonathan Tanudjaja.
*   **Release 5 (New):**
    *   **Version:** Backoffice_v8.37.2
    *   **Announced:** April 1, 2026, at 09:14 UTC.
    *   **Scheduled Execution:** Immediate execution by Minu Varghese.
    *   **Status:** Release notes pending (to be shared soon).

**Contextual Notes**
*   These updates align with the resource schedule for **FPG Back Office (Mon-Thurs)**.
*   The v8.37.2 release follows a rapid succession of hotfixes/updates initiated by different team members (Jonathan Tanudjaja previously, now Minu Varghese).


## [38/48] AdOps x Osmos
Source: gchat | Group: space/AAQAHz9NRfw | Last Activity: 2026-04-01T08:52:13.872000+00:00 | Last Updated: 2026-04-01T10:41:58.910674+00:00
**Daily Work Briefing: AdOps x Osmos**

**Key Participants & Roles**
*   **Prajwal Prakash:** Requestor/Ad Ops (Initiated ticket, driving urgency for ad launch).
*   **Shubhangi Agrawal:** Support/Operations (Owner of the support ticket status check).

**Main Topic**
Urgent status inquiry regarding a blocked workflow preventing the creation of ads for an imminent launch. Prajwal Prakash raised a specific support ticket yesterday to resolve this technical or procedural blockage.

**Pending Actions & Ownership**
*   **Action:** Provide status update and expedite resolution on ticket #112743.
*   **Owner:** Shubhangi Agrawal.
*   **Context:** Prajwal confirmed receipt of the request at 07:48 but followed up again at 08:52 with "Any update??" indicating the initial acknowledgment has not yet resulted in a solution or detailed status report.

**Decisions Made**
*   None recorded. The conversation currently reflects an active bottleneck where support intake was acknowledged, but no technical resolution or timeline was agreed upon by the close of this thread.

**Key Dates & Deadlines**
*   **Ticket Raised:** April 1, 2026 (Yesterday relative to chat context).
*   **Launch Deadline:** Today's launch ("tmrw" in the original message refers to the day after the ticket was raised, which is today, April 1, 2026).
*   **Follow-up Timestamps:**
    *   Initial request: 07:44 AM.
    *   Acknowledgment: 07:48 AM.
    *   Urgency escalation (No update received): 08:52 AM.

**Critical Constraint**
The inability to create ads is actively blocking the launch scheduled for today, April 1, 2026. Immediate attention from Shubhangi Agrawal is required to prevent a missed launch window.


## [39/48] FP x Mirakl
Source: gchat | Group: space/AAAAhWLveDE | Last Activity: 2026-04-01T07:58:04.751000+00:00 | Last Updated: 2026-04-01T10:43:28.272049+00:00
**Daily Work Briefing: FP x Mirakl Integration Update**

**Key Participants & Roles**
*   **Dang Hung Cuong:** Initiated initial API rate limiting discussion (March 17).
*   **Jill Ong:** Raised seller status query on March 25; tagged for visibility.
*   **Prajney Sribhashyam:** Proposed a three-way call (FP, Intrepid, Mirakl) on April 1 to align roadmap and clarify needs.
*   **Cheryl Jones:** Confirmed availability via leave confirmation until April 13; identified root cause of rate limiting as architectural misalignment by Intrepid.
*   **LyLy Lim:** Previously assigned for feasibility review.
*   **Michelle Lim & Sneha Parab:** Tagged by Prajney Sribhashyam for the proposed call.

**Main Topic**
The thread addresses two technical inquiries:
1.  **API Rate Limiting (Resolved Context):** Intrepid requested increasing the limit from one check per minute to support multi-seller operations. Investigation revealed that rate limiting was caused by incorrect endpoint usage not aligned with Mirakl documentation, rather than a need for higher thresholds. The team now requests an endpoint usage summary and the issued seller guide from Intrepid for further architectural review.
2.  **Seller Status Configuration:** Jill Ong queried (March 25) on creating additional statuses in Mirakl; still requires investigation.

**Pending Actions & Ownership**
*   **Action A:** Obtain endpoint usage summary and the issued seller guide from Intrepid to facilitate an architecture review under Mirakl Partnership support scope.
    *   **Owner:** Prajney Sribhashyam (to assist with request); Cheryl Jones (for final feedback).
    *   **Note:** Cheryl Jones is on leave until April 13; immediate follow-up required before her return.
*   **Action B:** Coordinate a three-way call involving FP, Intrepid, and Mirakl to discuss findings and roadmap alignment.
    *   **Owner:** Prajney Sribhashyam (proposer); all tagged participants (@Cheryl Jones, @Jill Ong, @Michelle Lim, @Sneha Parab, @Dang Hung Cuong).
*   **Action C:** Investigate technical feasibility of creating additional seller statuses in Mirakl.
    *   **Owner:** Cheryl Jones, LyLy Lim (pending return from leave).

**Decisions Made**
*   **Rate Limit Strategy Shift:** The approach has shifted from evaluating a threshold increase to correcting Intrepid's endpoint usage. No immediate rate limit increase is proposed until the architectural review confirms proper usage.
*   **Collaboration Model:** Agreed in principle on a three-way call (FP, Intrepid, Mirakl) to ensure FP visibility and better understand seller needs for the roadmap.

**Key Dates & Follow-ups**
*   **Original Inquiry:** March 17, 2026 – API Rate Limit discussion initiated by Dang Hung Cuong.
*   **Status Update (Root Cause):** April 1, 2026 (08:16 AM) – Cheryl Jones clarified that usage was incorrect per endpoint docs; Intrepid acknowledged design misalignment.
*   **New Proposal:** April 1, 2026 (07:48 AM) – Prajney Sribhashyam proposed the three-way call for visibility and roadmap alignment.
*   **Next Steps:** 
    *   Secure seller guide/usage data from Intrepid immediately.
    *   Schedule three-way call pending Cheryl Jones' return or delegation.
    *   Resume investigation on Seller Status configuration upon team availability.

**Specific References**
*   **Integrator:** Intrepid.
*   **Current Limit:** Once per minute (caused by incorrect usage, not hard cap).
*   **New Query Topic:** Creation of additional seller status in Mirakl.
*   **Platform:** Mirakl API.
*   **Source URL:** https://chat.google.com/space/AAAAhWLveDE


## [40/48] Offer Service Monitors Improvement - Apr 1
Source: gchat | Group: space/AAQA-iRTwV0 | Last Activity: 2026-04-01T06:19:07.381000+00:00 | Last Updated: 2026-04-01T06:42:02.613580+00:00
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


## [41/48] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/aQBHf9eET0A | Last Activity: 2026-04-01T04:19:56.227000+00:00 | Last Updated: 2026-04-01T06:46:40.253846+00:00
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


## [42/48] Team Starship
Source: gchat | Group: space/AAQAX9iKYf0 | Last Activity: 2026-04-01T02:51:49.229000+00:00 | Last Updated: 2026-04-01T06:49:57.785137+00:00
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


## [43/48] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/z_vFHR6ne-M | Last Activity: 2026-04-01T02:35:03.800000+00:00 | Last Updated: 2026-04-01T06:50:41.901609+00:00
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


## [44/48] DPD x DPM
Source: gchat | Group: space/AAQApzD7Im0 | Last Activity: 2026-04-01T02:33:57.348000+00:00 | Last Updated: 2026-04-01T06:51:10.348852+00:00
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


## [45/48] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/dRUQRmgzGzc | Last Activity: 2026-04-01T02:15:27.509000+00:00 | Last Updated: 2026-04-01T06:51:21.941641+00:00
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


## [46/48] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/69o051rSqd4 | Last Activity: 2026-04-01T00:59:59.910000+00:00 | Last Updated: 2026-04-01T06:51:38.489660+00:00
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


## [47/48] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY | Last Activity: 2026-03-31T23:16:10.242000+00:00 | Last Updated: 2026-04-01T06:53:28.491999+00:00
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


## [48/48] BCRS ECOMM SAP POSTING
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
