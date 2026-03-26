

## [1/37] BCRS ECOMM SAP POSTING
Source: gchat | Group: space/AAQA-ICuJRM | Messages: 48 | Last Activity: 2026-03-26T02:26:27.823000+00:00 | Last Updated: 2026-03-26T02:37:35.940339+00:00
**Daily Work Briefing: BCRS ECOMM SAP POSTING & Refunds UAT (Mar 26 Update)**

**Key Participants & Roles**
*   **Wei Fen Ching:** Accounting verification lead.
*   **De Wei Tey:** Provided examples; confirmed refund status for order 75567408.
*   **Yap Chye Soon Adrian / Hendry Tionardi:** SAP/DBP technical owners.
*   **Onkar Bamane:** Stakeholder managing IT audit sign-off requirements and deployment coordination.
*   **Prajney Sribhashyam:** UAT lead; coordinating validation and technical resolution.
*   **Lai Shu Hui:** Accounting participant; facing login/access issues; requesting SAP posting confirmations for Scan 'n Go (SNG).
*   **Tan Gay Lee:** Stakeholder prioritizing Ecomm UAT sign-off before deployment.
*   **Sathya Murthy Karthik:** Confirmed no Credit Notes (CN) created for SNG; added invoices to system.

**Main Topic**
UAT testing continues with a focus on resolving SAP posting discrepancies for Scan 'n Go (SNG) transactions and securing necessary IT audit sign-offs for deployment. Critical issues identified include Lai Shu Hui's inability to access tickets/invoices and the technical clarification that SNG sales/returns are aggregated via "Data 8" before posting to SAP, rather than individual transactions. A major blocker is Onkar Bamane's requirement for a separate formal sign-off covering specific API configurations (Deposit Accounting, SKU creation, and Concess Reports) distinct from the existing Ecomm-to-SAP sign-off.

**Status of Issues & Updates**
*   **Meeting Reschedule:** Prajney Sribhashyam moved the UAT review meeting from 9:30 AM to 10:00 AM due to a clash; Tan Gay Lee confirmed Lai Shu Hui will join at 10 AM. Tan emphasized prioritizing this UAT and requiring his update before sign-off.
*   **Access Issues:** Lai Shu Hui reported inability to download invoices, login to the system, or access tickets on Mar 26. Sathya Murthy Karthik confirmed that invoices were subsequently added by him.
*   **SNG Posting Clarification:** Lai Shu Hui queried if SNG transactions post to SAP as individual entries. Prajney and Onkar clarified that SNG sales and returns are consolidated/aggregated via "Data 8" before posting to SAP; deposits are also posted as a consolidated amount. No individual CNs were created for SNG by the system.
*   **IT Audit Sign-off Blocker:** Onkar Bamane requested a separate sign-off form for IT audit purposes, specifically listing four items: (1) API for Posting Deposit Accounting, (2) Marketplace SKU creation API changes, (3) Concess Sales Detail Report, and (4) Concess Sales Summary Report. Prajney Sribhashyam noted that the existing signed document cannot be amended but agreed to use the current testing record as a basis for deployment while acknowledging Onkar's need for a distinct sign-off to proceed with today's deployment.

**Pending Actions & Ownership**
1.  **UAT Meeting:** Join the rescheduled call at 10:00 AM to verify SAP postings and resolve access issues. **(Owner: Lai Shu Hui, Prajney Sribhashyam)**.
2.  **Separate Sign-off Form:** Onkar Bamane requires a new sign-off document covering specific API/Report configurations (Items 1-4 listed above) as the existing form cannot be updated. **(Owner: Onkar Bamane / Prajney Sribhashyam)**.
3.  **SNG Validation:** Lai Shu Hui to validate that consolidated SNG postings match SAP records; technical owners to support verification. **(Owner: Lai Shu Hui, Onkar Bamane)**.
4.  **Pre-order Clarification:** Address Tan Gay Lee's inquiry on Pre-order return testing status (previously pending). **(Owner: Prajney Sribhashyam)**.

**Decisions Made**
*   Meeting time adjusted to 10:00 AM; UAT prioritized for completion before final sign-off.
*   Confirmed that SNG sales/returns are aggregated via Data 8, not posted individually.
*   Agreed that the existing signed document cannot be amended; a separate sign-off is required for IT audit compliance regarding specific APIs and reports to enable deployment.

**Key Dates & Follow-ups**
*   **Mar 26, 09:30 AM (UTC):** Meeting rescheduled to 10:00 AM by Prajney Sribhashyam due to clashes.
*   **Mar 26, 12:46 AM:** Lai Shu Hui reported login and ticket access failures; invoices added by Sathya Murthy Karthik.
*   **Mar 26, 01:34 PM (UTC):** Prajney confirmed SNG posting via Data 8 aggregation.
*   **Mar 26, 02:11 PM (UTC):** Prajney declined amending the signed form; Onkar insisted on a separate sign-off for deployment.

**Immediate Follow-up:** Attend the 10:00 AM call to validate SAP postings, resolve Lai Shu Hui's access issues, and finalize the strategy for the required separate IT audit sign-off to clear the path for today's deployment.


## [2/37] Vivian Lim Yu Qian
Source: gchat | Group: dm/k9UsaIAAAAE | Messages: 2 | Last Activity: 2026-03-26T02:26:26.730000+00:00 | Last Updated: 2026-03-26T02:37:46.276536+00:00
**Daily Work Briefing: Google Chat Summary**

**Key Participants & Roles**
*   **Michael Bui:** Proposer of user experience issue; likely Product Manager or Stakeholder.
*   **Vivian Lim Yu Qian (Resource):** Technical lead or implementer responding to the inquiry.
*   **Ravi:** Third-party mentioned by Michael Bui as part of a prior discussion.

**Main Topic**
Discussion regarding the user experience (UX) potential for confusion on the **search banner** feature, specifically concerning ambiguous keywords like **"Apple."** The core concern is ensuring visual consistency between the banner imagery and the subsequent product list results.

**Pending Actions & Ownership**
*   **Action:** Clarify which specific technical component or module within the search interface Michael Bui is referring to regarding the "search banner" discrepancy.
*   **Owner:** Vivian Lim Yu Qian (to clarify scope) / Michael Bui (to provide further details once identified).

**Decisions Made**
No final decisions were reached in this conversation thread. The exchange consists of an issue report followed by a clarification request.

**Key Dates & Follow-ups**
*   **Date:** March 26, 2026.
*   **Follow-up Required:** Michael Bui must specify the exact UI component (e.g., banner logic, filtering algorithm, or rendering layer) to proceed with addressing the "Apple" keyword confusion scenario (where banners show phones but lists show fruit).

**Detailed Context**
Michael Bui reported a discussion with Ravi highlighting a UX inconsistency. When users search for ambiguous terms like "Apple," the current implementation may display a banner featuring "Apple phones" while the product list below displays only fruits, causing customer confusion. Vivian Lim Yu Qian responded by requesting clarification on which specific component of the search banner system is being referenced to facilitate further investigation.


## [3/37] #dd-dpd-engage-alert
Source: gchat | Group: space/AAAAxwwNw2U | Messages: 16 | Last Activity: 2026-03-26T02:24:52.731000+00:00 | Last Updated: 2026-03-26T02:38:26.439943+00:00
# Daily Work Briefing: #dd-dpd-engage-alert Monitoring Activity (Updated March 26, 02:31 UTC)

**Key Participants**
*   **System:** Datadog App (Automated Alerting)
*   **Target Audience:** `@hangouts-dd-dpd-engage-alert`, `@oncall-dpd-engage-journey`, `@oncall-dpd-engage-dynamics`
*   **Relevant Squads/Tribes:** Dynamics, Compass, Journey (`squad:dynamics`, `squad:compass`, `squad:journey`, `tribe:engage`).

**Main Topic**
Instability persists into the early hours of **March 26**, transitioning from evening volatility to a recurring cycle of high error rates and latency spikes in `engage-my-persona-api-go`. The issue has expanded to affect mobile success rates for both iOS (`ef-ios`) and Android (`ef-android`), indicating a broader synchronization failure across core APIs and frontend clients.

**Status Summary & Timeline (Early Morning Volatility)**
*   **Service Error Rates (`engage-my-persona-api-go`):**
    *   Recurring high error alarms (>0.1%) triggered multiple times between **01:42 UTC** and **02:21 UTC**. Specific triggers occurred at **01:52** (Peak: 0.102%), **01:58** (Peak: 0.108%), **02:14**, and **02:21** (Peak: 0.119%).
    *   A P90 latency alert (>1.8s) for `post_/new-myinfo/confirm` triggered at **02:16 UTC** (Metric: 2.072s), recovering by **02:24 UTC**.
*   **User Profile & Discount Scheme Latency:**
    *   Monitor #50879029 for `get_/user/profile/myinfo` success rate (<99.9%) triggered at **01:50** (99.891%), recovered at **02:01**, and re-triggered at **02:20** (99.896%).
*   **Mobile Client Errors:**
    *   `ef-ios`: "View user linkpoints" success rate dropped to 97.59% at **02:14 UTC**, recovered by **02:15 UTC**.
    *   `ef-android`: "View user linkpoints" success rate dropped to 99.696% at **02:31 UTC** (active).

**Pending Actions & Ownership**
*   **Investigate Recurring Error Loops:** Immediate RCA required for the oscillating error rates in `engage-my-persona-api-go` throughout the night (01:42–02:21). Owner: **Squad Dynamics/Journey**.
*   **Analyze Mobile & Profile Correlation:** Investigate the correlation between API latency on `post_/new-myinfo/confirm` and the concurrent success rate drops in iOS and Android linkpoints. Owner: **Squad Journey/Dynamics**.
*   **Monitor Android Stability:** Continue monitoring `ef-android` cart errors following the 02:31 event. Owner: **Squad Journey/Compass**.

**Decisions Made**
*   **Severity Maintenance:** Incident severity remains high due to the continuous re-emergence of instability across the night window (March 25 evening through March 26 early morning), specifically the synchronized failure of user profile updates and mobile linkpoint loading.
*   **Pattern Continuity:** Activity confirms a persistent issue affecting `engage-my-persona-api-go` error rates, latency spikes on MyInfo confirmations, and downstream impact on iOS/Android client success rates.

**Key Dates & Follow-ups**
*   **Active Window:** March 24–26 (UTC). Recent critical activity: **01:42 – 02:31 UTC** (March 26).
*   **Reference Links (Updated):**
    *   `engage-my-persona-api-go` Error Monitor #92965074 (Peak: 0.119% @ 02:21)
    *   `post_/new-myinfo/confirm` P90 Latency Monitor #50879027 (Triggered @ 02:16, Peak: 2.072s)
    *   `get_/user/profile/myinfo` Success Rate Monitor #50879029 (Re-triggered @ 02:20)
    *   `ef-ios` Linkpoints Monitor #63109468 (Triggered @ 02:14, Value: 97.59%)
    *   `ef-android` Linkpoints Monitor #63109467 (Triggered @ 02:31, Value: 99.696%)


## [4/37] [Prod Support] Offers
Source: gchat | Group: space/AAAAzZ3qkNU | Messages: 1 | Last Activity: 2026-03-26T02:24:26.546000+00:00 | Last Updated: 2026-03-26T02:38:47.731630+00:00
**Daily Work Briefing: [Prod Support] Offers**

**Key Participants & Roles**
*   **Willie Tan:** Reported initial issue (Mar 17) with offer visibility; escalated on Mar 26 regarding promo flow failure for specific SKUs.
*   **Angela Yeo:** Previously escalated discrepancy regarding incorrect promo display for SKU 13066243.
*   **Alvin Choo:** Previously flagged urgency and assigned owners for the initial case.
*   **Zaw Myo Htet & Daryl Ng:** Previously tagged as owners; now required to investigate the new flow issue.

**Main Topic**
Investigation into production offer display errors involving two distinct but potentially related scenarios:
1.  **Historical Context (Mar 17–19):** Issues with Offer ID `sap offer 202603000112484` for **SKU 13066243**. The team confirmed "2 for $5.40" is the correct configuration, but it failed to display as expected while incorrect promotions were visible.
2.  **New Escalation (Mar 26):** Willie Tan reported that promos created in SAP are not flowing to FPON for a list of SKUs, despite these items *not* being on the promo blacklist. The specific SKUs provided were samples; a full investigation of the flow mechanism is required.

**Pending Actions & Ownership**
*   **Action 1:** Investigate why correct offers ("2 for $5.40") are not displaying or if incorrect offers are showing for historical cases (SKU 13066243).
*   **Action 2:** Investigate the root cause of promo flow failure from SAP to FPON for SKUs not on the blacklist, as reported by Willie Tan on March 26.
*   **Owners:** @Zaw Myo Htet, @Daryl Ng (assigned by Alvin Choo previously; applicable to both current issues).
*   **Status:** Active/Urgent. The scope has expanded from a single SKU display error to a systemic flow issue affecting multiple SKUs as of March 26, 02:24 AM UTC.

**Decisions Made**
No final technical fixes have been implemented yet. The team has established the expected outcome for historical cases: offers must display "2 for $5.40." For the new case, it is confirmed that SKUs in question should be eligible for promos (not blacklisted) but are failing to receive them from SAP.

**Key Dates & Deadlines**
*   **Initial Issue Reported:** March 17, 2026 (09:01 AM).
*   **Historical Escalation:** March 19, 2026 (10:04 AM and 12:35 PM).
*   **New Flow Issue Reported:** March 26, 2026 (02:24 AM UTC) by Willie Tan.
*   **Deadline:** Immediate resolution requested for both the display error and the new flow failure.

**Reference Links & IDs**
*   **Chat Space URL:** https://chat.google.com/space/AAAAzZ3qkNU
*   **Historical Offer ID:** `sap offer 202603000112484`
*   **Historical SKU:** 13066243
*   **New Case Scope:** Multiple SKUs (samples provided by Willie Tan) not under promo blacklist.
*   **System Components:** SAP (source), FPON (destination).


## [5/37] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4/h-WUXwPta8M | Messages: 11 | Last Activity: 2026-03-26T02:24:17.600000+00:00 | Last Updated: 2026-03-26T02:39:04.350288+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**
**Source:** Google Chat Space (11 messages) | **Date:** March 26, 2026

### Key Participants & Roles
*   **Daryl Ng:** Raises architectural queries regarding data indexing ownership and schema requirements.
*   **Michael Bui:** Initially suggests DSP handles Algolia integration; seeks clarification on system boundaries.
*   **Alvin Choo:** Corrects the architecture scope (B2C backend, not DSP) and defines governance protocols for changes.
*   **Gopalakrishna Dhulipati:** Provides architectural context on the Distributed Service Platform (DSP) and requests an updated "Source of Truth" diagram.
*   *(Note: EA is referenced as the entity responsible for providing the Source of Truth; KDD is referenced regarding sign-offs).*

### Main Topic/Discussion
The team discussed the technical ownership of **Algolia data indexing** within the B2C ecosystem and clarified the architectural distinction between the core commerce engine (DSP) and channel-specific backends.
*   **Clarification:** While DSP powers the Omni experience (Product, Promo, OMS), Algolia integration is specific to the **B2C backend**, not DSP. Each channel (B2C, B2B, POS) utilizes its own Frontend and Backend for specific needs.
*   **Schema Requirements:** Current data schemas are product-focused. To support searching vouchers, brands, etc., a new data schema discussion is required.

### Decisions Made
*   **Ownership Confirmed:** The **B2C backend** manages the indexing of data to Algolia, not the DSP.
*   **Governance Rule:** Any changes affecting upstream and downstream systems require **KDD sign-off**.

### Pending Actions & Owners
| Action Item | Owner/Responsible | Context |
| :--- | :--- | :--- |
| Provide a single "Source of Truth" architecture diagram (noting current diagrams may be outdated). | **Enterprise Architecture (EA)** | Requested by Gopalakrishna Dhulipati. |
| Discuss and finalize the data schema to support searching for vouchers, brands, etc., beyond just products. | **Daryl Ng** / Team | Identified as a prerequisite for Algolia functionality. |

### Key Dates & Follow-ups
*   **March 26, 2026:** Conversation took place between 01:55 and 02:24 UTC.
*   **Immediate Follow-up:** EA to share the updated architectural diagram.
*   **Next Step:** Schedule a discussion on data schema expansion (Daryl Ng).

**Reference URL:** https://chat.google.com/space/AAQAsFyLso4


## [6/37] Backend Chapter
Source: gchat | Group: space/AAAAHhDyHI4 | Messages: 2 | Last Activity: 2026-03-26T02:23:13.900000+00:00 | Last Updated: 2026-03-26T02:39:32.389027+00:00
**Daily Work Briefing: Backend Chapter**

**Key Participants & Roles**
*   **Michael Bui:** Investigated GCP PubSub configuration for message delivery.
*   **Nicholas Tan:** Flagged security concerns regarding Service Account (SA) keys; recently paused pipelines due to Trivy CLI issues.
*   **Lester Santiago Soriano:** Previously blocked on CI/CD pipeline errors after upgrading Go dependencies; requested support.
*   **Maou Sheng Lee:** Suggested using AI tools to resolve Lester's issue.
*   **Boon Seng Ong:** Investigated deployment failures with `deploy-esp-image` for ESPv2, noting discrepancies between past success and current failures.

**Main Topics**
1.  **GCP PubSub Configuration (March 6):** Michael Bui sought configuration flags for "at-most-once" delivery in GCP PubSub but found no samples. Nicholas Tan followed up, noting limited expertise. No resolution reached; discussion remains open regarding specific flag implementation.
2.  **CI/CD & Dependency Upgrade (March 12):** Lester Santiago Soriano upgraded `stdlib` to `v1.25.8` to address SonarQube vulnerability `GO-2026-4603`. The pipeline failed due to a version mismatch: the build agent's `golangci-lint` was compiled with Go 1.24, while the project targeted Go 1.25.8.
    *   *Root Cause Identified:* The error requires an update to the `dpd-backend-cicd` resource.
3.  **ESPv2 Deployment Failure (March 25):** Boon Seng Ong reported that redeploying ESPv2 via `deploy-esp-image` fails with `gcloud beta run deploy` errors, specifically: "expected a container image path" and invalid flag value for `--to-revisions`.
    *   *Investigation:* Code unchanged from 7 days prior; usage of an older `google/cloud-sdk:546.0.0-slim` image also failed. Boon suspects recent changes to the "golden pipeline."
    *   *Error Detail:* `gcloud run services update-traffic` rejected `--to-revisions [value=100]`, suggesting a syntax or parameter shift in the deployment logic.
4.  **Service Account Security Audit (March 16):** Nicholas Tan identified JSON keys embedded in Service Accounts (`pong-club-agent`, `vertex-client`) within the `fpg-titan-preprod` project. These accounts require decomposition due to security best practices.
5.  **Pipeline Maintenance Pause (March 26, 02:23 UTC):** Nicholas Tan announced via Bitbucket (`infra-gcp-fpg-titan/pipelines`) that pipelines will be disabled until further notice. This action is precautionary following potential Trivy CLI calls used to check Terraform code, which may have disrupted service stability.

**Pending Actions & Ownership**
*   **Resolve CI/CD Pipeline Block (Go Version):** Update `dpd-backend-cicd` resource configuration to support Go 1.25.8 or align linter version.
    *   *Owner:* **TBD** (Lester requested ownership; current owner unknown).
*   **Investigate Golden Pipeline Breakage:** Determine recent changes causing `gcloud beta run deploy` and `update-traffic` flag failures for ESPv2.
    *   *Owner:* **Boon Seng Ong** (to coordinate with pipeline maintainers).
*   **Service Account Cleanup:** Identify owners and decompose identified SAs (`pong-club-agent`, `vertex-client`) in `fpg-titan-preprod`.
    *   *Owner:* **TBD** (Nicholas Tan flagged this; ownership unknown).
*   **Pipeline Restoration:** Monitor pipeline status and re-enable services once Trivy CLI risks are resolved.
    *   *Owner:* **Nicholas Tan**.

**Decisions Made**
*   Pipelines for `infra-gcp-fpg-titan` have been temporarily disabled to prevent further issues related to Trivy CLI checks on Terraform code.
*   The team acknowledged the Go version mismatch requires a CICD resource update, identified the need to decompose specific Service Accounts, and flagged the golden pipeline as a potential root cause for recent deployment failures.

**Key Dates & Follow-ups**
*   **March 6, 2026:** Initial PubSub inquiry (Open).
*   **March 12, 2026:** Pipeline failure reported; escalation for CICD ownership required.
*   **March 16, 2026:** Security flag raised regarding `fpg-titan-preprod` SAs. Follow-up on SA ownership is critical.
*   **March 25, 2026:** Critical deployment failure reported; investigation into golden pipeline changes initiated.
*   **March 26, 2026 (02:23):** Pipelines disabled pending Trivy CLI resolution; immediate follow-up required for restoration.


## [7/37] Theo Adi
Source: gchat | Group: dm/4g6tFSAAAAE | Messages: 5 | Last Activity: 2026-03-26T02:22:57.015000+00:00 | Last Updated: 2026-03-26T02:39:50.181161+00:00
**Daily Work Briefing**  
**Resource:** Theo Adi  
**Date:** March 26, 2026  
**Time Window:** 01:59 – 02:23 UTC  

**1. Key Participants & Roles**  
*   **Michael Bui:** Manager/Supervisor; currently in an important meeting.
*   **Theo Adi:** Subject resource; initiates request to discuss a "big fix."

**2. Main Topic/Discussion**  
The exchange shifts from a previous one-way data relay (March 25) regarding the identifier `NLPE-3ZEF-CWP4-LLLU-5MH3-HMAU` to an active coordination between Theo Adi and Michael Bui.
*   **Theo Adi's Request:** Initiates contact ("hi morning boss") to request Michael Bui's immediate attention to "check your big fix."
*   **Michael Bui's Response:** Confirms availability during a short break from a critical meeting.
*   **Scheduling Negotiation:** Michael Bui inquires about the duration of the check due to the importance of his current meeting. Theo Adi confirms the session will take **15 minutes**.

**3. Pending Actions & Ownership**  
*   **Action:** Conduct a 15-minute review/check of the "big fix" (potentially related to previous identifier `NLPE-3ZEF-CWP4-LLLU-5MH3-HMAU` or a separate operational issue).
*   **Owner:** Michael Bui (to perform the check) and Theo Adi (to facilitate the discussion).
*   **Status:** Scheduled. The meeting is tentatively set for the short break following 02:22 UTC, pending Michael Bui's availability.

**4. Decisions Made**  
*   **Agreed Duration:** The review session is confirmed to last approximately 15 minutes.
*   **Timing:** Meeting to occur during Michael Bui's next scheduled break from his current important meeting.

**5. Key Dates, Deadlines, & Follow-ups**  
*   **Original Message Timestamp (March 25):** 03:52 UTC (Single data transmission of `NLPE-3ZEF-CWP4-LLLU-5MH3-HMAU`).
*   **New Coordination Timestamp:** March 26, 2026.
    *   Request Initiated: 01:59:04 UTC.
    *   Meeting Break Confirmation: 01:59:49 UTC.
    *   Duration Confirmation: 02:22:57 UTC.
*   **Next Step:** Michael Bui to initiate the check during his break after 02:23 UTC.

**Summary Note**  
The interaction has evolved from a passive data handover on March 25 into an active operational request on March 26. Theo Adi requires immediate assistance from Michael Bui to review a "big fix." Despite Michael Bui being in a critical meeting, a 15-minute window for this review was successfully negotiated and confirmed by Theo Adi at 02:22 UTC. The session is pending execution during the next available break. Historical context regarding `NLPE-3ZEF-CWP4-LLLU-5MH3-HMAU` remains relevant as a potential subject of this "big fix" review, though the current conversation focuses on scheduling rather than the code itself.


## [8/37] #dd-dpd-grocery-alert
Source: gchat | Group: space/AAAAtxQjB7c | Messages: 13 | Last Activity: 2026-03-26T02:13:32.673000+00:00 | Last Updated: 2026-03-26T02:40:22.692883+00:00
**Daily Work Briefing: #dd-dpd-grocery-alert** (Updated Mar 26, 02:15 UTC)

**Key Participants & Roles**
*   **System:** Datadog (Automated monitoring agent).
*   **Alert Recipients/Owners:** `@hangouts-dd-dpd-grocery-alert`, `@opsgenie-dpd-grocery-discovery`.
*   **Escalations:** `@hangouts-GT-Search-DatadogAlerts`, `@oncall-dpd-staff-excellence-pdm`, `@hangouts-GT-Discovery-DatadogAlerts`.
*   **Service Teams:** DPD Grocery Discovery, Product Data Management (`team:dpd-staff-excellence-pdm`), Search Indexing.

**Main Topic**
**P3 ALERT (Flapping):** The `go-catalogue-service` exhibits recurring latency instability in production. While the `get_/category/_id` endpoint stabilized earlier today, it **flapped again on Mar 26**. A previous flapping event occurred earlier on the `get_/product` endpoint.

**Pending Actions & Ownership**
*   **Action:** **MONITOR LATENCY FLAPPING (`get_/category/_id`):** Address P90 latency spikes > 2000ms for the `get_/category/_id` endpoint.
    *   **Owner:** Discovery Team (`@hangouts-GT-Discovery-DatadogAlerts`) & Product Data Management (`@opsgenie-dpd-staff-excellence-pdm`).
    *   **Status:** **RECOVERED (02:13 UTC).** The alert cycled states on Mar 26 with the following sequence for `get_/category/_id`:
        *   **Triggered 01:39 UTC** (p90: **2.029s**).
        *   **Recovered 02:13 UTC** (p90: **0.703s**).
    *   **Required Checks:** Review Datadog logs, inspect K8s deployment (`fpon-cluster/default/go-catalogue-service`), and consult Runbook.
*   **Action:** **RESOLVE LATENCY FLAPPING (`get_/product`):** Address P90 latency spikes > 150ms for the `get_/product` endpoint.
    *   **Owner:** Discovery Team & Product Data Management.
    *   **Status:** Previously recovered at 19:27 UTC on Mar 25 (p90: 129ms). Monitor ID: `17447976`. No new activity reported for this specific monitor in the current cycle.
*   **Action:** **PERSISTENT INVESTIGATION:** Address critical errors on `fp-search-indexer` (env: prod).
    *   **Owner:** Product Data Management On-Call (`@oncall-dpd-staff-excellence-pdm`).
    *   **Status:** Active since Mar 18. Last re-triggered Mar 24, 16:29 UTC. No resolution achieved.

**Decisions Made**
*   The `go-catalogue-service` latency on `get_/category/_id` spiked to **2.029s** (p90) at **01:39 UTC**, recovering immediately to **0.703s** by **02:13 UTC**. This confirms a recurring flapping pattern for this endpoint, following the earlier incident where it was stable after 13:00 UTC on Mar 25.
*   Root cause analysis is required for the current `get_/category/_id` monitor (ID: `17447967`) and the previous `get_/product` incident to identify systemic instability triggers.
*   `fp-search-indexer` failure remains persistent since Mar 18; root cause analysis is critical.

**Key Dates & Follow-ups (Mar 16–26, 2026)**
*   **Service: `go-catalogue-service` (P3 - Discovery/Product Data) [FLAPPING]**
    *   *Latest Timeline:* 
        *   `get_/category/_id`: Flapped between 07:14 and 13:00 UTC (Mar 25). Stable after 13:00. **Re-triggered 01:39 UTC** (p90: 2.029s), **Recovered 02:13 UTC** (p90: 0.703s) on Mar 26. Monitor ID: `17447967`.
        *   `get_/product`: Triggered 19:16 UTC (Mar 25, p90: 151ms), Recovered 19:27 UTC (p90: 129ms). Monitor ID: `17447976`.
    *   *Links:* [Datadog Monitor (`get_/category/_id`)](https://app.datadoghq.eu/monitors/17447967) | [K8s Console](https://console.cloud.google.com/kubernetes/deployment/asia-southeast1/fpon-cluster/default/go-catalogue-service/overview?project=fponprd).
*   **Service: `fp-search-indexer` (P2 - Product Data Management) [ACTIVE CRITICAL]**
    *   *Latest Timeline:* Active since Mar 18; re-triggered Mar 24, 16:29 UTC.
    *   *Links:* [Datadog Monitor](https://app.datadoghq.eu/monitors/17447691) | [Runbook](https://ntuclink.atlassian.net/wiki/spaces/SR/pages/2001831558/Support+Run+book).

**Reference Links:**
*   Datadog Space: https://chat.google.com/space/AAAAtxQjB7c


## [9/37] Digital Product Development {DPD}
Source: gchat | Group: space/AAAAx50IkHw | Messages: 2 | Last Activity: 2026-03-26T01:59:19.364000+00:00 | Last Updated: 2026-03-26T02:40:49.419947+00:00
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

**Main Topics & Discussions**
1.  **Infrastructure & Operations Risk:** Nicholas Tan previously flagged operational risks regarding Broadcom ending free Bitnami images, causing `kubectl` image tag failures and increased Time To Recovery (TTR). The issue impacts the Golden Pipeline (GP).
2.  **Payment Service Issues:** Alvin Choo reported promo code redemption failures in FP Pay; confirmed that a change freeze has ended and feature releases are proceeding.
3.  **Mobile Quality Assurance:** Andin Eswarlal Rajesh identified an iOS FPPay bug where QR codes load without user login, escalated via file download.
4.  **Datadog Governance:** Natalya Kosenko reported unauthorized manual changes to Datadog On-Call teams (removals of Maxine, Arijit, Minu). Terraform manages this config; manual console edits are overwritten on the next run.
5.  **Strategic Planning:** Winson Lim highlighted data centers as potential targets in modern warfare (Iran conflict context) to inform Disaster Recovery (DR) scenarios.
6.  **Product Strategy & Tooling Expansion:** On March 26, 2026, Winson Lim noted that Reforge joined Miro. This acquisition signals Miro's expansion into product strategy, aiming to close the gap between decision-making and delivery for modern product teams.
7.  **Social Events & Sentiment:** Kyle Nguyen previously announced an upcoming DPD BBQ with the sentiment "We come first." Maou Sheng Lee expressed a sentiment of feeling like energy is being wasted on March 18.
8.  **Alumni Engagement:** Natalya Kosenko noted DPD alumni participation in a Google AI event (March 25, 2026).

**Pending Actions & Owners**
*   **GP Team (Nicholas Tan / Mohit Niranwal):** Investigate Bitnami image replacement strategy to resolve TTR issues and update Golden Pipeline dependencies.
*   **iOS/Dev Team (Tiong Siong Tee / Andin Eswarlal Rajesh):** Investigate the iOS FPPay QR code login bypass bug.
*   **Datadog Admins:** Anyone who manually altered Datadog Teams must submit a Pull Request to `https://bitbucket.org/ntuclink/fp-datadog-eu` instead of editing the console to prevent configuration loss.
*   **Product Strategy Team (Winson Lim / Product Folks):** Evaluate Miro's strategic expansion and Reforge integration opportunities to optimize decision-to-delivery workflows.

**Decisions Made**
*   No formal change freeze; feature releases are currently active (Alvin Choo).
*   Datadog team configurations must strictly follow Infrastructure as Code (Terraform) protocols; manual overrides are deprecated.
*   Miro's acquisition of Reforge is recognized as a strategic move to bridge product strategy and delivery gaps.

**Key Dates & Follow-ups**
*   **Mar 3, 2026:** Project status noted as "one step behind."
*   **Mar 7, 2026:** FP Pay promo code issue raised; change freeze lifted same day.
*   **Mar 9, 2026:** BCRS discussion and Meta AI news shared.
*   **Mar 10, 2026:** iOS bug discovered.
*   **Mar 12, 2026:** "BB incident" query raised; Data center DR scenario discussed.
*   **Mar 13, 2026:** Datadog governance warning issued.
*   **Mar 17, 2026:** DPD BBQ announcement made by Kyle Nguyen; Wai Ching Chan engaged with Vincent Wei Teck Lim regarding the event (Last Reply: 12:15 PM).
*   **Mar 18, 2026:** Maou Sheng Lee noted sentiment regarding wasted energy.
*   **Mar 25, 2026:** Natalya Kosenko highlighted DPD alumni participation in a Google AI event.
*   **Mar 26, 2026:** Winson Lim shared Reforge joining Miro; potential impact on product strategy workflows identified.

**Social Notes**
*   Boning He and Gopalakrishna Dhulipati shared snacks (Chinese cookies with chicken gizzard/medicinal barley and Indian cookies) in pantry areas.
*   Upcoming DPD BBQ announced by Kyle Nguyen ("We come first, see you!").


## [10/37] Project Light Attack and Defence Leads
Source: gchat | Group: space/AAQAsFyLso4 | Messages: 26 | Last Activity: 2026-03-26T01:55:52.031000+00:00 | Last Updated: 2026-03-26T02:41:22.211820+00:00
**Daily Work Briefing: Project Light Attack and Defence Leads**

**Key Participants & Roles**
*   **Alvin Choo:** Space Creator; Lead coordinating the briefing.
*   **Daryl Ng, Gopalakrishna Dhulipati, Tiong Siong Tee, Michael Bui, Akash Gupta:** Designated "Project Light Attack and Defence Leads".
*   **Hui Hui Voon:** Owner of the D&T Scope for Project Light Workshop document.
*   **Pauline Pong:** Owner of promotion conflict test case file.
*   **Jacob Yeo:** Edited CDTO Internal RFP requirements file on March 25, 2026.

**Main Topic**
Following the transition to active strategic planning ("Room 2") on March 24, the team is finalizing specific slide preparation within six "Spotlight Topics." While Alvin Choo initiated collaboration on **"RMN"** and **"Payment"** slides on March 24, a new flexibility protocol was established on March 25 allowing leads to attend other meetings (e.g., BCRS) if required. Concurrently, technical direction has shifted toward decoupling from SAP, with consensus that SAP should serve primarily for finance and sales records purposes. New RFP documentation and promotion conflict testing cases have been identified for review. On March 26, the discussion expanded to data infrastructure specifics, with Daryl Ng querying the management of data indexing to Algolia.

**Pending Actions & Ownership**
*   **Action:** Finalize content for "RMN" and "Payment" slides in the D&T Scope document.
    *   **Ownership:** Alvin Choo (initiated), Hui Hui Voon (Document Owner).
    *   **Status:** In progress; collaboration initiated March 24, ~9:32 AM UTC.
*   **Action:** Review "Promotion Conflict Test Case_05.NOV.20" and summarize the file for Alvin Choo.
    *   **Ownership:** Michael Bui (requested by Alvin Choo on March 25, ~2:46 AM UTC). Note: Access was initially denied to Alvin Choo on March 25, 2:51 AM UTC.
*   **Action:** Review "[CDTO Internal] Project Light Requirements for RFP by MVP Scope.xlsx".
    *   **Ownership:** Gopalakrishna Dhulipati (Owner). Jacob Yeo edited this file on March 25, 2026. Alvin Choo shared the link on March 25, ~3:56 AM UTC for summary.
*   **Action:** Clarify backend API responsibilities with CoMall regarding personalization and orchestration.
    *   **Ownership:** Michael Bui (to note and document).
*   **Action:** Identify the owner managing data indexing to Algolia.
    *   **Ownership:** Daryl Ng raised this query on March 26, ~1:55 AM UTC; team response pending in chat space (10 replies noted).
*   **Action:** Finalize the Attack/Defence team composition pending Dennis's confirmation following Alvin Choo's email.
    *   **Ownership:** Alvin Choo.
*   **Action:** Address technical clarifications raised by Tiong Siong Tee regarding Inventory visibility, Corporate Control alignment, and Product management portal structure (FP vs. Sellers).
    *   **Ownership:** Alvin Choo and Gopalakrishna Dhulipati.

**Decisions Made**
*   **Session Protocol:** Participants are encouraged to listen during live sessions; questions should be raised in the chat space.
*   **Meeting Flexibility:** Leads attending this project may prioritize other critical meetings (e.g., BCRS) if necessary, as confirmed by Alvin Choo on March 25.
*   **Platform Resilience:** Integration testing is a strict technical requirement prioritized from "Day 1."
*   **Governance Structure:** FPG cannot be treated merely as a standard seller due to governance conflicts; distinct data structures or models are required for FP vs. non-governance sellers (Clarified by Gopalakrishna Dhulipati).
*   **System Architecture:** SAP integration should be decoupled from core operational logic; it is designated strictly for finance and sales records purposes (Agreed by Tiong Siong Tee on March 25, aligning with Rock's prior position).
*   **Gamification:** Confirmed not part of the DSP scope.

**Key Dates & Follow-ups**
*   **Slide Collaboration Initiated:** March 24, 2026 (~9:32 AM UTC) – Alvin Choo requested work on RMN and Payment slides.
*   **SAP Decoupling Consensus:** March 25, 2026 (1:36 AM UTC) – Tiong Siong Tee agreed to limit SAP usage to finance/sales records.
*   **Meeting Flexibility Policy:** March 25, 2026 (1:31 AM UTC) – Alvin Choo authorized attendance at other meetings like BCRS.
*   **RFP File Sharing & Review Request:** March 25, 2026 (~3:56 AM UTC) – Alvin Choo shared the "Project Light Requirements for RFP by MVP Scope" file.
*   **Test Case Identification:** March 25, 2026 (~2:46 AM UTC) – Michael Bui identified "Promotion Conflict Test Case_05.NOV.20" (Owner: Pauline Pong); Alvin Choo noted access issues at ~2:51 AM UTC.
*   **Algolia Indexing Query:** March 26, 2026 (~1:55 AM UTC) – Daryl Ng asked "who is managing the indexing of the data to Algolia?" with 10 replies recorded.
*   **Session Start ("Room 2"):** March 24, 2026 (1:02 AM UTC).
*   **Spotlight Topics List Published:** March 24, 2026 (3:14 AM UTC).
*   **Email Sent for Team Confirmation:** March 24, 2026 (3:51 AM UTC) by Alvin Choo.


## [11/37] [BCRS]-SAP to POS & DBP Interface Deployment
Source: gchat | Group: space/AAQAeMC3qBk/0rSvmSBcJD0 | Messages: 9 | Last Activity: 2026-03-26T01:49:57.562000+00:00 | Last Updated: 2026-03-26T02:41:37.316381+00:00
**Daily Work Briefing: [BCRS]-SAP to POS & DBP Interface Deployment**

**Key Participants & Roles**
*   **Prajney Sribhashyam:** Initiator; coordinating deployment sequence.
*   **Yangyu Wang:** Technical lead (DBP); confirmed changes deployed.
*   **Sneha Parab:** Operations liaison; managing communications to Catalog Ops & MP Ops.
*   **Daryl Ng:** Deployment lead; assessing risk regarding midnight release.
*   **Michael Bui:** Verification lead; monitoring post-deployment status.
*   **Onkar Bamane:** Release engineer; executing the deployment window.

**Main Topic**
Confirmation of deployment sequence for the [BCRS]-SAP to POS & DBP Interface update, specifically verifying that the **DBP** component proceeds before the SAP changes. The discussion focused on establishing a maintenance window where MP SKU creation is suspended to mitigate risk during the transition.

**Decisions Made**
1.  **Deployment Sequence:** Confirmed that **DBP will go first**, followed by SAP changes.
2.  **Maintenance Window:** Catalog Ops and MP Ops will be instructed not to approve any SKUs starting **10:00 PM today (March 26, 2026)** until the deployment is verified.
3.  **Risk Assessment:** Daryl Ng confirmed no known risks prevent proceeding with this schedule, contingent on Onkar's midnight release plan.

**Pending Actions & Owners**
*   **Send Operational Communications:** Sneha Parab will notify Catalog Ops and MP Ops of the 10:00 PM SKU approval freeze and the deployment window details. *Owner: Sneha Parab.*
*   **Execute Release:** Onkar Bamane to deploy changes between **00:10 AM and 01:30 AM**. *Owner: Onkar Bamane.*
*   **Monitor & Verify:** Michael Bui will observe system status post-deployment (approx. 12:00 AM – 1:00 AM) to confirm successful deployment of SAP changes and identify any issues. *Owner: Michael Bui.*

**Key Dates, Deadlines & Follow-ups**
*   **March 26, 2026 @ 10:00 PM:** Deadline for Catalog Ops/MP Ops to stop approving SKUs.
*   **March 27, 2026 @ 00:10 AM – 01:30 AM:** Scheduled deployment window.
*   **March 27, 2026 @ ~12:00 AM – 1:00 AM:** Verification period for SAP changes.

**Reference**
*   Chat URL: https://chat.google.com/space/AAQAeMC3qBk


## [12/37] Shopping Cart Notification
Source: gchat | Group: space/AAAAsbHANyc | Messages: 16 | Last Activity: 2026-03-26T01:45:30.999000+00:00 | Last Updated: 2026-03-26T02:42:24.067910+00:00
**Daily Work Briefing: Shopping Cart Notification Alerts (Update)**
**Date:** March 26, 2026 (Night Shift)
**Space:** `Shopping Cart Notification` (Google Chat)
**Message Count:** 404

### Key Participants & Roles
*   **System/Tool:** Datadog App (Automated Monitoring)
*   **Notification Channel:** `@hangouts-ShoppingCartNotification`
*   **Ownership Teams:** `dpd-pricing`, `dpd-pricing-cart`.

### Main Topic
Instability in `frontend-gateway` continues with extreme high-frequency oscillation. The scope has expanded to include checkout latency, reduced cart update success rates, and severe degradation in Wish List operations (Write/Read) and V2 Shopping List retrieval. Activity persists through 01:45 UTC on March 26.

### Incident Timeline & Actions
**Previous Context:**
*   *Activity from March 20–March 25 regarding `frontend-gateway` latency, checkout dips, and a 99.728% success rate failure at 19:29 UTC.*

**New Activity (March 26, UTC+0)**
*   **00:46–00:50 UTC:** P90 of "Put Product ID to Wish List" spiked to 5.254s (>5s threshold, Monitor `21245706`), recovering to 3.794s.
*   **01:10–01:13 UTC:** Rapid oscillation in "Put Product ID to Wish List" P99 (peaked at 7.164s, Monitor `21245701`) and P90 (Monitor `21245706`).
*   **01:11–01:38 UTC:** Severe latency in "Get V2 Shopping List" P99 peaking at 10.887s (>4s threshold, Monitor `21245734`) and "Get Wish List by ID" P99 peaking at 3.199s (>3.1s threshold, Monitor `21245725`).
*   **01:19–01:20 UTC:** Minor spike in "Get Wish List by ID" P90 to 1.747s (Monitor `21245720`).
*   **Status:** All monitors recovered to normal ranges (< thresholds) by 01:45 UTC, but the frequency of triggers indicates continuous system contention.

### Pending Actions & Ownership
*   **Owner:** `dpd-pricing-cart` and `dpd-pricing`.
*   **Critical Risk:** The incident has escalated to include **multi-vector availability degradation**. Beyond the prior 19:29 UTC success rate drop (Event ID `8559804196539338360`), new data shows extreme tail latency (P99 >10s) affecting shopping list reads. This confirms a systemic bottleneck in shared dependencies (likely database or cache saturation) affecting both write and read paths simultaneously.
*   **Scope:** Immediate correlation required between the 12:22 UTC trigger events, the 19:29 UTC success rate failure, and the new March 26 oscillations. Investigate resource contention across `frontend-gateway` operations.

### Decisions Made
*   **Priority Escalation:** Status remains **"Critical Incident"**. Activity extends from March 20 through at least March 26, 01:45 UTC. No stabilization observed; failure modes have diversified from latency to partial failures and extreme tail latencies.
*   **Focus Shift:** Prioritize analysis of Event IDs `8560147245808731272` (Wish List P99), `8560148805621577580` (Shopping List P99), and `8559804196539338360` (Cart Success Rate) to identify the common root cause.

### Key Dates & Follow-ups
*   **Critical Window:** Extended activity from March 20 through at least March 26, 01:45 UTC.
*   **Follow-up:** Analyze trace correlation for Event IDs `8560147328265805593`, `8560169943885050119`, and `8560172823919279036` to identify specific resource saturation points.

### References
*   **Active Monitors:** `21245710` (Checkout P90), `21245714` (Cart Success Rate), `21245706` (Wish List Put P90), `21245701` (Wish List Put P99), `21245720/21245725` (Wish List Get P90/P99), `21245734` (Shopping List P99).
*   **Service Tags:** `service:frontend-gateway`, `team:dpd-pricing`, `tribe:pricing`.


## [13/37] Project Light: Mobilization and Planning Workshop Day 1 - Mar 24
Source: gchat | Group: space/AAQAA8d_pfI | Messages: 25 | Last Activity: 2026-03-26T01:44:03.497000+00:00 | Last Updated: 2026-03-26T02:43:08.033418+00:00
**Daily Work Briefing: Project Light – Mobilization & Planning Workshop (Day 1)**
**Date:** March 24, 2026 (Session concluded; new insights added Mar 26)
**Resource Link:** https://chat.google.com/space/AAQAA8d_pfI

**Key Participants & Roles**
*   **Jacob Yeo:** Meeting facilitator.
*   **Vivian Lim Yu Qian:** Presenter/UI Walkthrough; defined technical/action items.
*   **Tiong Siong Tee:** UX Lead; proposed agenda flow and requested Figma access.
*   **Cecilia Koo Hai Ling:** Design/UX Contributor; shared DoorDash, NTUC FairPrice, Lazada references; clarified SKU logic; provided RedMart video analysis.
*   **Christine Yap Ee Ling:** Internal Liaison; handling Figma link distribution.
*   **Rajesh Dobariya:** Stakeholder; reviewed delivery categorization references.
*   **Sophia Liao & Rock Shi:** Identified as audience for Cecilia's latest Flash Deal observations.

**Main Topic & Discussion Updates**
The team conducted a high-level UX walkthrough and UI review, significantly expanding reference analysis to include RedMart's current "mega campaign" (running for 2 days) and Lazada app mechanics:
*   **RedMart Campaign Analysis:** Cecilia Koo Hai Ling shared screenshots, a Lazada campaign calendar link ([s.l.38p5B](https://s.lazada.sg/s.38p5B)), and a video demo (`Video_20260326_094235_087_1.mp4`, viewed by 13 of 23). The team reviewed critical components:
    1.  **Flash Deal Mechanics:** Flash deal sections are clickable, directing users back to the dedicated flash deal landing page.
    2.  **Label System:** RedMart displays multiple scrollable labels, including unclaimed vouchers.
    3.  Voucher center structure and gamification mechanics.
    4.  Promo mechanisms (claim, apply, stack, and nudge toward next tiers).
    5.  Social sharing features.
    6.  "Store-in-store" concepts (default views, dedicated flash deals, seller vouchers).
    7.  User journey flow: Homepage → Category → Search → Campaign → General Merchandise.
*   **Lazada & FairPrice References:** Reviewed DoorDash's first-time app open and NTUC FairPrice examples (SharkNinja Official Store, FP Unilever Tag). The Lazada "promo label" (dynamic seller section) and gamified "Help me click" mechanic were accepted as engagement drivers.
*   **Navigation & Filters:** Clarification remains needed on whether category page filters should be pre-configured ("dynamic") or retrieved dynamically.
*   **UI Clarity:** The toggle selection between "Scheduled" and "Quick" modes requires improved visual definition.
*   **Compliance:** Discussed potential separation of eGift cards from vouchers to meet compliance requirements.
*   **SKU Logic:** Clarified that when any SKU is clicked, it is displayed as the primary SKU in Slot 1.

**Decisions Made**
*   **Reference Alignment:** Agreed that DoorDash's categorization and Lazada/RedMart campaign mechanics (voucher stacking, gamification, store-in-store) are valid benchmarks for Project Light integration.
*   **Specific Feature Validation:** Confirmed RedMart's clickable flash deal section behavior and scrollable label system (including unclaimed vouchers) as key UX patterns to analyze.
*   **Filter Logic:** No final consensus on filter behavior; pending technical solution discussion led by Vivian.
*   **Slot 1 Behavior:** Clarified that the clicked SKU populates Slot 1, establishing a baseline interaction pattern.

**Pending Actions & Owners**
1.  **Share Figma Link:** Christine Yap Ee Ling to send via separate internal chat (requested by Tiong Siong Tee).
2.  **Resolve Filter Logic:** Vivian Lim Yu Qian and the technical team to finalize category page filter behavior.
3.  **Refine UI Toggle:** Design team to address visual clarity for "Scheduled/Quick" toggle selection.
4.  **Compliance Review:** Determine if eGift cards must be standalone from vouchers.
5.  **Deep-Dive Analysis:** UX Lead (Tiong Siong Tee) to analyze RedMart's specific mechanics: clickable flash deal navigation, scrollable label system (vouchers/unclaimed), voucher center, gamification logic, and store-in-store flows for Project Light integration.

**Key Dates & Follow-ups**
*   **Event:** Project Light Mobilization and Planning Workshop Day 1 (March 24, 2026).
*   **Status:** Session concluded; RedMart campaign materials and video (`Video_20260326_094235_087_1.mp4`) shared via chat on March 26.
*   **Next Step:** Internal distribution of Figma link by Christine Yap Ee Ling; UX team to evaluate RedMart's "mega campaign" mechanics (specifically flash deal redirection and label scrolling) for potential application in Project Light mega campaigns.


## [14/37] [BCRS]-SAP to POS & DBP Interface Deployment
Source: gchat | Group: space/AAQAeMC3qBk | Messages: 30 | Last Activity: 2026-03-26T01:12:07.849000+00:00 | Last Updated: 2026-03-26T02:43:40.326204+00:00
**Daily Work Briefing: [BCRS]-SAP to POS & DBP Interface Deployment**

**Key Participants & Roles**
*   **Onkar Bamane:** Deployment Lead/Coordinator.
*   **Michael Bui:** Deployer (Production OData/SAP).
*   **Hendry Tionardi:** Technical Advisor.
*   **Prajney Sribhashyam:** Process Owner/Test Coordinator.
*   **Daryl Ng:** Technical Advisor/Approver.
*   **Others:** Sneha Parab, Wai Ching Chan, Olivia, Kandasamy Magesh (Deployed team members).

**Main Topic**
Coordination and execution of the deployment for the ECOM flow ([BCRS]-SAP to POS & DBP Interface) scheduled for Friday, March 26, at 00:00 UTC. The discussion focused on resolving a critical timing conflict regarding Michael Bui's availability versus the Production OData maintenance window.

**Decisions Made**
1.  **Deployment Sequence:** Confirmed that the **DBP deployment will proceed first**, followed by SAP OData.
2.  **Risk Mitigation:** Validated that deploying DBP first poses no risk of error logs from BCRS deposits, as there are currently no active BCRS or deposit items in production.
3.  **Constraint Confirmation:** Confirmed Michael Bui's statement: he cannot deploy to Production on Friday (the day after the deployment) and will be on leave next week; therefore, tonight is his final opportunity for this release cycle if required.

**Pending Actions & Ownership**
*   **Update Deployment Schedule:** Michael Bui must add his specific deployment steps to the shared spreadsheet. *(Owner: Michael Bui)*
*   **Add Missing PICs:** Identify and add any missing Persons In Charge (PICs) not currently listed in the coordination group. *(Owner: Sneha Parab, Prajney Sribhashyam)*
*   **Redelivery Status:** Discuss latest status on "redelivery" separately in the working group meeting; do not discuss in this chat. *(Owner: Prajney Sribhashyam)*
*   **Exceptional Release (Conditional):** If standard timing fails, request approval for an exceptional release on Friday. *(Owner: Daryl Ng / Team)*

**Key Dates & Deadlines**
*   **Deployment Window:** Friday, March 26, 2026, at 00:00 UTC.
*   **Meeting Invite:** Deployment call invite has been shared; all participants must join.
*   **Missed Opportunity:** If deployment does not occur tonight, Michael Bui will be unable to deploy to Prod on the following Friday and is unavailable next week due to leave.

**References**
*   **Deployment Plan/Tracker:** https://docs.google.com/spreadsheets/d/1gvCjdXWB2BeWr7XgBQs0-zKeLxGi3OmX4ZrbY6pNMeQ/edit?gid=1022676232#gid=1022676232
*   **Chat Space:** https://chat.google.com/space/AAQAeMC3qBk


## [15/37] BCRS Production Deployment Planning Session - Mar 25
Source: gchat | Group: space/AAQAjVLsLrE | Last Activity: 2026-03-25T04:31:31.177000+00:00 | Last Updated: 2026-03-25T06:50:18.131240+00:00
**Daily Work Briefing: BCRS Production Deployment Planning (Mar 25)**

**Key Participants & Roles**
*   **Sneha Parab:** Meeting organizer/facilitator; confirmed location (L11, Room 11) and verified SKUs.
*   **Yang Yu:** Co-organizer (present at location).
*   **Sathya Murthy Karthik:** Attendee (joined late).
*   **Sundy Yaputra:** Contributor; provided status on deployed features.
*   **Michael Bui:** Requester of API access confirmation.
*   **Onkar Bamane:** Responsible for verifying API access requests and checking ticket status.
*   **Prajney Sribhashyam:** IT Support/Ticket Owner; created the access request ticket (NED-275153).

**Main Topic**
Coordination of the BCRS Production Deployment planning session, specifically focusing on confirming room availability, verifying current production deployment status, and resolving pending API access requirements for the production environment.

**Pending Actions & Owners**
*   **Verify Access Request Status:** Onkar Bamane has acknowledged a ticket exists and is currently checking its status to confirm if API access on Production (PRD) is ready.
*   **Join Meeting:** Sathya Murthy Karthik indicated he would join at 11:10 (timezone implied as local/UTC relative to context). Sundy Yaputra noted potential inability to attend but provided updates asynchronously.

**Decisions Made**
*   No formal strategic decisions were recorded in this thread; the discussion focused on status verification and logistical coordination.
*   It was confirmed that specific components are already live: Cart, Shopping List, Wishlist, and Amplitude "order completed" events for BCRS are deployed to production.

**Key Dates & References**
*   **Meeting Date:** March 25, 2026.
*   **Location:** L11 Room 11.
*   **Ticket Reference:** NED-275153 (Jira Service Desk portal).
*   **SKU Verification Data Provided by Sneha Parab:**
    *   *Non BCRS:* SKU 13278877 / Barcode 8888030317266.
    *   *BCRS Items:* SKUs 13280984, 12714758, 12714881 with corresponding barcodes and deposit SKUs (13285192, 13285203, 13285197).
*   **Deployment Timeline:** Amplitude events deployed yesterday (March 24, 2026 context); other features currently in prod.


## [16/37] fairnex-datadog-notification
Source: gchat | Group: space/AAAA8dv5lp0 | Messages: 17 | Last Activity: 2026-03-26T00:17:49.591000+00:00 | Last Updated: 2026-03-26T02:44:14.985113+00:00
**Daily Work Briefing: Datadog Monitoring Alerts (fairnex-datadog-notification)**

**Key Participants & Roles**
*   **Datadog App:** Automated monitoring system.
*   **Service Owner(s):** `dpd-fulfilment` / `seller-experience` squad.
*   **Notification Target:** `@hangouts-fairnex-datadog-notification`.

**Main Topic**
Production instability persists in Mirakl integration and seller job processing. The timeline extends from March 17 through the early hours of **March 26**, with new incidents triggered late on March 25 (23:00 UTC) and continuing into March 26 (00:12 UTC).

**Incident Summary & Timeline**
*   **Service:** `fni-order-create` (Mirakl Integration) – **Escalated Recurrence on Mar 26 (Early Morning)**
    *   **Pattern Continuation:** Instability spans March 17–26. Following the afternoon cluster on March 25, new incidents occurred at **00:12 UTC on March 26**.
    *   **Incident Window (Mar 26, ~00:12 UTC):** Two distinct P2 triggers initiated simultaneous alerts for "Exception Occurred At Mirakl Route" and "Error while calling APIs".
        *   Both monitors triggered at **00:12:40 UTC** (`Monitor ID: 17447918`) and **00:12:49 UTC** (`Monitor ID: 17447928`).
        *   Logs confirmed >1 event match within a 5-minute window.
    *   **Recovery:** Monitors returned to normal by **00:17:39 UTC** and **00:17:49 UTC**. Duration was approximately **5 minutes**.

*   **Service:** `fni-offer` (Mirakl Integration) – **New Late-Night Cluster (Mar 25)**
    *   **Incident Window (Mar 25, ~23:07 UTC):** Simultaneous P2 triggers for "Error while calling API" and "Exception Occurred at Mirakl Route".
        *   Triggered at **23:07:41 UTC** (`Monitor ID: 17447919`) and **23:08:15 UTC** (`Monitor ID: 17447953`).
    *   **Recovery:** Monitors recovered by **23:12:40 UTC** and **23:13:14 UTC**. Duration was approximately **5 minutes**.

*   **Service:** `seller` (`picklist-pregenerator`) – **Recurring Latency**
    *   **Latest Update (Mar 25, ~23:02 UTC):** A new P2 warning triggered with metric value **3657.213s** (Monitor ID `20383097`), continuing the cycle from March 20 (3611s), March 23 (3607s), and March 24 (3607.798s).

**Actions Pending & Ownership**
*   **Action:** Investigate root cause of expanded Mirakl integration instability affecting `fni-order-create` and `fni-offer`. The pattern now includes recurrence windows on Mar 17–25 history, clusters on Mar 24/25 (afternoon/evening), and a new early-morning cluster at **00:12 UTC** on March 26.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Investigate root cause of extreme latency spikes in `picklist-pregenerator`. The cycle has now reached a peak metric value of **3657.213s** on March 25 (23:02 UTC).
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.
*   **Action:** Review Monitor `29851723` logic for Apple Pay/Google Pay transactions following the March 23 test alert indicating potential false positives.
    *   **Owner:** `dpd-fulfilment` / `seller-experience` squad.

**Decisions Made**
None. The conversation remains purely alert-driven without human discussion.

**Summary for Leadership**
Mirakl integration instability has persisted across ten consecutive days (March 17–26). On March 25, the service exhibited clusters in the afternoon (~13:04 UTC), evening (~23:08 UTC), and early morning (~08:22 UTC). A new cluster occurred at **00:12 UTC on March 26**, affecting both `fni-order-create` and `fni-offer`, with all incidents resolving within ~5 minutes. Concurrently, `picklist-pregenerator` shows a continuous cycle of critical latency spikes, reaching **3657.213s** on March 25 (23:02 UTC). These systemic failures in Mirakl and job processing logic require urgent engineering review to stabilize production performance.


## [17/37] 📅 Daily summary
Source: gchat | Group: space/AAQAP-kMoqY | Messages: 2 | Last Activity: 2026-03-26T00:03:08.804000+00:00 | Last Updated: 2026-03-26T02:44:41.044281+00:00
**Daily Work Briefing Summary (Updated: March 26, 2026)**

**Main Topics & Discussions**
1.  **Programmatic Advertising (Advertima/TTD):** Focus remains on validating discrepancies for `advertima_ttd-fixed-price-test-1.5`. Ravi Singh confirmed receipt of raw BURLs; validation was targeted for Monday, March 17th. Yian Koh requested confirmation on deals `advertima_ttd-first-price-test` and `advertima_ttd-fixed-price-test-1`.
2.  **New Deal Setup:** Yasmina Tregan (Advertima) required an end-to-end test setup this week. Wei Phung to share live campaign details; Ravi Singh to execute setup, push to TradeDesk, and map segments before launch.
3.  **BCRS UAT & Finance Integration:** Progress on SAP document numbers, duplicate posting fixes via PubSub "exactly once" policy (PR #1033), and Bukit Timah Plaza pricing/display issues.
4.  **Event Sync Optimization (DPD-645):** Addressing the massive event overage (14M vs. normal 550k). PRD deployment plan set for Sunday, March 15.
5.  **Security & Compliance:** RMN Pentest fixes (DPD-700) deployed to Prod; Bitbucket App Passwords deprecated effective June 9, 2026.

**Status Update: Inbox & Communications**
*   **Inbox Status:** As of March 26, 2026, the workspace inbox is fully caught up across all categories (**Urgent Action Items**, **Project Activity & Reviews**, **Meeting Updates**, and **FYI**). No pending unread items require immediate attention. This status follows confirmations from daily summaries dated March 24, 25, and now March 26, 2026.

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
*   **June 9, 2026:** Bitbucket App Password deprecation deadline.

**Note on New Content:** Daily summaries received on March 24, 25, and 26, 2026, confirm the inbox remains clear of urgent action items across all categories (including Project Activity & Reviews). No changes to pending actions or decisions were required based on these updates.


## [18/37] Nikhil Grover
Source: gchat | Group: dm/t3wf6EAAAAE | Last Activity: 2026-03-25T16:22:08.429000+00:00 | Last Updated: 2026-03-25T22:35:14.718342+00:00
**Daily Work Briefing: Nikhil Grover & Michael Bui**

**Key Participants & Roles**
*   **Nikhil Grover:** Initiator; confirmed ranking fix, managing deployment requests and stakeholder timelines. Investigated prod visibility issues post-deployment.
*   **Michael Bui:** Technical Lead (Engineering); successfully deployed to PRD. Identified severe resource constraints due to "Project Light" and upcoming travel/leave from April 6th–12th.
*   **Flora:** Frontend resource; previously raised analytics payload concerns. Confirmed backend control for swim lanes historically resided with Yang Yu.

**Main Topics**
1.  **Deployment Status & Visibility Issues:**
    *   Michael Bui confirmed deployment and verification on PRD at **16:06 UTC**. However, both Nikhil Grover and Michael observed no ads appearing in production (previously verified only by Daryl).
    *   Investigation revealed only one swim lane active in "OG Home." Michael noted backend control historically belonged to Yang Yu per Flora's info.
    *   **Action:** Team agreed to request enabling of other swim lanes, likely requiring assistance from a third party or confirmation from Yang Yu regarding PRD data access protocols.

2.  **Future Resource Constraints & Timeline Conflict:**
    *   **Impressions Delivery Tickets:** Nikhil asked Michael to start these tickets tomorrow (March 26).
    *   **Michael's Availability:** Confirmed he cannot start due to travel preparations this weekend and a strict leave block starting April 6th. He may need to visit China, depending on visa status.
    *   **Project Light Conflict:** The week of April 6th is "unprecedentedly tight" for Project Light. Michael cannot promise availability then; he estimates focusing on the project until April 12th, potentially doing UAT on April 13–14 and deploying by April 15.
    *   **Timeline Clash:** Nikhil requires deployment by **April 9th**. He noted that waiting for a full week of unavailability (until April 6th) is not feasible, as he can only manage 1–2 days of delay.

**Decisions Made & Status Updates**
*   **Deployment Readiness:** The core ranking fix is deployed to PRD, but visibility remains blocked pending the activation of additional swim lanes.
*   **Capacity Planning:** Michael Bui has declined starting impressions tickets immediately due to travel and Project Light constraints. A tentative window for future work (beyond April 12th) was proposed by Michael, but Nikhil flagged this as too late for the required April 9th deadline.
*   **Investigation Pivot:** Focus shifted from analytics payload verification to production visibility troubleshooting (swim lane activation).

**Pending Actions & Owners**
*   **Swim Lane Activation (Nikhil Grover/Team):** Coordinate with Yang Yu or another qualified resource to enable remaining swim lanes in PRD. Michael Bui suggested creating a Jira ticket to track this request formally.
*   **Impressions Delivery Scheduling (Nikhil Grover/Michael Bui):** Urgent negotiation required to find a delivery window before April 9th, despite Michael's unavailability until mid-April due to Project Light and travel.
*   **Project Light Context:** Nikhil requested clarification on the specific demands causing the "unprecedentedly tight" timeline for the week of April 6th.

**Key Dates & Deadlines**
*   **March 25, 2026:**
    *   **14:32–14:36 UTC:** Discussion on starting impressions tickets; Michael cited travel and Project Light constraints.
    *   **16:06 UTC:** Deployment verified on PRD.
    *   **16:11–16:19 UTC:** Discovery that no ads are visible; agreement to enable other swim lanes.
*   **April 9, 2026:** Critical deadline for delivery raised by Nikhil Grover.
*   **April 6–12, 2026:** Michael Bui's anticipated leave/travel and Project Light focus period.

**Historical Context Note**
While the initial focus was on resolving the March 25 ranking anomaly (confirmed fixed), the conversation quickly pivoted to immediate post-deployment validation. Despite successful PRD deployment, ads remain invisible, necessitating swim lane configuration changes by Yang Yu or similar stakeholders. Simultaneously, a critical resource conflict emerged: Nikhil requires delivery by April 9th, but Michael is unavailable due to Project Light and travel until at least mid-April, creating a significant scheduling risk for the upcoming impressions delivery tickets.


## [19/37] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/o4m2XO8j1K0 | Last Activity: 2026-03-25T14:17:11.526000+00:00 | Last Updated: 2026-03-25T14:37:34.545953+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Michael Bui:** Initiator of the incident report; investigating search/category page impression drops.
*   **Daryl Ng:** Platform Ops/Frontend lead; verifying deployment history, traffic metrics, and Amplitude data.
*   **Andin Eswarlal Rajesh:** Team lead (likely Segment/Omni); cross-functional investigation and root cause analysis.
*   **Nikhil:** External/Allied team contact (Campaigns/Feature Flags) assisting with data comparison.
*   **Alvin Choo:** Copied on the initial alert; no direct contribution noted in this thread.

**Main Topic**
Investigation into a significant 60–70% drop in ad impressions on Search and Category pages since March 18–19, 2026. The team is determining if recent PRD deployments or operational changes caused the discrepancy between tracked requests and reported impressions.

**Status & Findings**
*   **Symptoms:** Impressions dropped significantly starting March 18/19. Traffic to pages remained stable; Amplitude data shows no drop in category page activity.
*   **Troubleshooting Results:**
    *   No related PRD deployments occurred on the affected dates for Search/Category pages.
    *   Platform Ops disabled swimlanes on Omni & OG Home (March 18–20), but this does not affect Search/Category tracking.
    *   OSMOS confirmed no drop in ad requests; MPS service shows no drop in tracking requests.
    *   **Root Cause Hypothesis:** Michael Bui and Nikhil identified that the number of responses containing "2 or more products" significantly reduced. This reduction is likely causing the impression drop, as impressions are tracked when an ad product card appears in the viewport (IAN standards).
*   **Related Issue:** Andin Eswarlal Rajesh noted a separate banner impression drop on the Omni Home page for Segment was caused by an IAB banner fix issue (previously identified) affecting iOS only.

**Pending Actions & Owners**
1.  **Cross-check with OSMOS:** Verify if the reduced response count (2+ products) is causing the SDK to fail sending impressions. *Owner: Michael Bui.*
2.  **Platform Breakdown:** Analyze data breakdown by platform (iOS vs. others) to confirm if the issue mirrors the iOS-only Segment banner problem. *Owner: Michael Bui & Andin Eswarlal Rajesh.*
3.  **Campaign/FF Audit:** Check with Nikhil regarding any campaigns or Feature Flags turned off on March 18/19. *Owner: Andin Eswarlal Rajesh (initiated).*

**Decisions Made**
*   The issue does not stem from platform traffic drops, Ad request failures, or direct PRD deployments targeting Search/Category logic during the specific window.
*   The investigation has pivoted to data structure changes (reduced multi-product responses) rather than infrastructure outages.

**Key Dates & Follow-ups**
*   **Incident Window:** March 18–19, 2026.
*   **Follow-up Date:** Investigation to continue "tomorrow" (March 26, 2026) regarding the potential link between the Segment banner fix issue and the current Search/Category drop.
*   **Next Update:** Michael Bui provided an interim update on March 25 at 14:17 regarding the response count analysis.


## [20/37] Video & Product Ads Working Group
Source: gchat | Group: space/AAQAeSWRtgQ/RZyBk6LBi14 | Last Activity: 2026-03-25T14:09:34.340000+00:00 | Last Updated: 2026-03-25T14:37:56.987677+00:00
**Daily Work Briefing: Video & Product Ads Working Group**
*Source: Google Chat (36 messages)*
*Date Range: March 17, 2026 – March 25, 2026 (UTC)*

### **Key Participants**
*   **Michael Bui:** Raised initial technical queries on API usage and feature flags; currently attending a full-day workshop.
*   **Norman Goh:** Validated assumptions regarding UAT rank issues; confirmed deployment to production; noted he is no longer part of the omni home experience team.
*   **Nikhil Grover:** Reported initial UAT discrepancies regarding event "rank"; requested verification post-production deployment.
*   **Flora Wo Ke:** Identified root cause: analytics payload generation occurred in the backend, rendering frontend Split.IO manipulations ineffective without backend config access; clarified team ownership changes.
*   **Others Involved:** Daryl Ng, Yangyu Wang (PR reviewers); Andin Eswarlal Rajesh.

### **Main Topic**
Discussion centered on the API strategy for **vertical scrolling product ads**, which evolved into resolving an incident involving incorrect event "rank" reporting in UAT after dynamic ad slot updates. The conversation concluded with the successful deployment of the fix to production and a request for final verification.

### **Decisions Made & Technical Clarifications**
*   **API Strategy (March 17):** Confirmed that vertical scrolling uses the same endpoint as "product swimlanes" with dynamic positioning values, not hardcoded. Split.IO logic resides entirely within the `marketing-service`.
*   **Root Cause of Rank Issue (March 25):** Incorrect ranks occurred because the analytics payload is built in the backend. Frontend manipulation via Split.IO was insufficient; the backend must retrieve the Split config to recalculate positions dynamically.
*   **Fix Implementation:** Norman Goh confirmed the fix utilizes dynamic calculation logic with no hardcoded values.

### **Pending Actions & Ownership**
*   **PR Status:** Pull Request #209 for `engage-content-orchestration-go` is submitted for review and approval by Daryl Ng and Yangyu Wang (requested on March 25).
*   **Production Verification (Critical):** Norman Goh (March 25, 14:09 UTC) confirmed the fix has been deployed to the **production environment**. He formally requested Nikhil Grover to verify the deployment in production.

### **Key Dates & Follow-ups**
*   **2026-03-17:** Initial strategy meeting regarding API endpoints and Split.IO architecture.
*   **2026-03-25 01:33 UTC:** Nikhil Grover reported rank discrepancies in UAT; Michael Bui unavailable due to workshop.
*   **2026-03-25 03:56 UTC:** Flora Wo Ke clarified backend retrieval of Split config is mandatory; Norman Goh confirmed leaving the omni home team.
*   **2026-03-25 04:11 UTC:** Norman Goh confirmed the fix uses dynamic calculation logic.
*   **2026-03-25 05:28 UTC:** PR #209 submitted for review and deployment.
*   **2026-03-25T14:09:34+00:00:** Norman Goh announced the fix is deployed to production and requested verification from Nikhil Grover.

### **Status Update**
The technical root cause has been resolved, and the dynamic position fix has been successfully **deployed to the production environment**. The immediate pending action is for Nikhil Grover to verify correct rank reporting in production scenarios (both "ad applied" and "non-ad"). While PR #209 remains pending final review by Daryl Ng and Yangyu Wang, the functional deployment to production allows for live validation. Future Split.IO changes affecting ad slots require backend integration to regenerate analytics payloads correctly.


## [21/37] Google Drive
Source: gchat | Group: dm/7d1XKcAAAAE | Last Activity: 2026-03-25T14:06:37.786000+00:00 | Last Updated: 2026-03-25T14:38:32.514566+00:00
**Daily Work Briefing Summary (Updated)**

**Key Participants & Roles:**
*   **Nikhil Grover (FairPriceGroup):** Repeatedly encountering "Google Drive unable to process your request" errors when sharing ads analytics and cadence notes. Previously attempted to share "Programmatic Ads tracking events."
*   **Sujit Jha (Onlinesales.ai):** Attempted to share "Ads tracking events"; file access failed due to recipient blocking.
*   **Michael Bui (Business/Stakeholder):** Blocked Sujit Jha's document; previously flagged as a blocked user in Drive incidents.
*   **Jacob Yeo (FairPriceGroup):** Encountered Drive processing errors while sharing the "Project Light: Mobilization & Planning Workshop" deck.
*   **Tan Gay Lee (Finance):** Driving UAT financial validation requiring SAP document numbers.
*   **Hendry Tionardi (Operations/IT):** Managing technical clarifications on POS/SAP integration.

**Main Topics:**
1.  **Google Drive Processing Failures:** A persistent system-wide or permission-based issue is preventing file sharing across FairPriceGroup domains.
    *   **March 18–19:** Nikhil Grover failed to share "Programmatic Ads tracking events" and gain Editor access to "ACNxOsmos: Daily Cadence."
    *   **March 23 (16:32):** Jacob Yeo attempted to share the "Project Light: Mobilization & Planning Workshop" presentation; request failed with a Drive processing error.
    *   **March 25 (14:00–14:06):** Nikhil Grover made three consecutive attempts to share specific Product Ads Analytics files (Baby-Child-Toys and Beauty/Oral-Care categories) for dates 20260304 and 20260325. All requests failed with the same "Google Drive is unable to process your request" error.
2.  **Ads Tracking Data Sharing & Access Issues:** Continued failures in sharing tracking event documents between FairPriceGroup and Onlinesales.ai domains, compounded by system processing errors.
    *   **March 18:** Sujit Jha's share failed due to Michael Bui blocking `sujit.jha@onlinesales.ai`.

**Pending Actions & Owners:**
*   **UAT SAP Document Update:** Hendry Tionardi and the BCRS team must update Column J with valid SAP document numbers immediately. Finance cannot proceed without this data. *(Note: Original deadline was March 10; current date is now March 25, requiring urgent resolution).*
*   **Scan & Go Flow Confirmation:** Hendry Tionardi requested **Onkar Bamane** to confirm if the "Scan and Go" flow posts sales data as an aggregate invoice to SAP rather than individual receipts.
*   **Drive Infrastructure Resolution:** IT support must investigate the recurring "Google Drive unable to process your request" errors affecting Jacob Yeo, Nikhil Grover, and others across multiple document types (Project Light, Ads Analytics, Cadence notes).
*   **Ads Tracking Resolution:** Michael Bui or Nikhil Grover must resolve access permissions for tracking documents (OSMOS source) with Finance/Operations.

**Decisions Made:**
*   **RMN Incident Impact:** Confirmed there is **no financial revenue impact**.
*   **Postmortem Template:** Michael Bui confirmed that breaking down the Executive Summary follows the approved **v2 postmortem template**.

**Key Dates & Deadlines:**
*   **March 6, 2026:** Initial request for SAP document numbers issued.
*   **March 10, 2026 (Original Deadline):** Finance required SAP document numbers in BCRS UAT spreadsheet (Missed).
*   **March 18–19, 2026:** Failed attempts to share Ads tracking files and Cadence notes by Sujit Jha and Nikhil Grover.
*   **March 23, 2026 (16:32):** Jacob Yeo failed to share "Project Light" workshop deck due to Drive error.
*   **March 25, 2026 (14:00–14:06):** Multiple failures by Nikhil Grover to share Product Ads Analytics files for Baby and Beauty categories.

**References:**
*   **BCRS UAT 2026 Spreadsheet:** [Link](https://docs.google.com/spreadsheets/d/1o6oklFTFyzpT490vQ4x8IKc00vdL41pl9hUAaQgg-ns/edit)
*   **RMN Incident Report (v2 Template):** [Link](https://docs.google.com/document/d/1XiN0diQicup7ujoCWWKdD3Hvp8J0OJD5LPOfnthegyE/edit)
*   **ACNxOsmos Daily Cadence (Access Failed):** [Link](https://docs.google.com/document/d/1LWKTTxcCJxIS12EkIvJmyXFNfjHXCF5ZYu2v5Vg4r9o/edit?usp=drive-dynamite&userstoinvite=nikhil.grover@fairpricegroup.sg&role=writer&ts=69bb8e22)
*   **Project Light Presentation (Failed Share):** [Link](https://docs.google.com/presentation/d/1iRcOI4v06WBUIERjlncMpkRre7z_jUkBl1J76fuzIso/edit?usp=drive-dynamite&ts=69c16b08)
*   **Product Ads Analytics (Failed Shares):** [Baby/Toys Link](https://docs.google.com/document/d/1_LkZAkPEP5jNy1mkJDc9JzrpTG0PrDWZ8V2YVcmp2KA0/edit), [Beauty Link](https://docs.google.com/document/d/1_DirQKHwYEkq2eOyfYkt0wcNj2jg2G_lOkvxghKIAj0/edit) (Note: Actual links for March 25 files not provided in source text, but file names recorded).


## [22/37] Sneha Parab
Source: gchat | Group: dm/50uphEAAAAE | Last Activity: 2026-03-25T12:22:51.489000+00:00 | Last Updated: 2026-03-25T14:40:50.812292+00:00
**Daily Work Briefing: Google Chat Summary**
**Resource:** Sneha Parab
**Date of Conversation:** March 25, 2026 (09:34 UTC)

**Key Participants & Roles**
*   **Sneha Parab:** Initiator of the query; verified tool status.
*   **Michael Bui:** Respondent who confirmed the operational history and contract status regarding "Citrus Ad."

**Main Topic/Discussion**
The conversation focused on validating the operational status of the marketing platform **"Citrus Ad."** Sneha Parab sought confirmation that the resource was no longer in use. Michael Bui provided a definitive affirmative response, clarifying that the vendor's contract was officially terminated last May (2025).

**Pending Actions & Ownership**
*   **Action:** None currently pending. The inquiry has been fully resolved with Michael's confirmation.
*   **Status Change:** The requirement for verification is complete. No further follow-up regarding this specific query is necessary until new information arises.

**Decisions Made**
*   **Confirmation of Termination:** It was confirmed that the "Citrus Ad" contract was terminated last May, rendering the tool no longer in use as of March 25, 2026. This settles the operational status inquiry raised by Sneha Parab.

**Key Dates & Follow-ups**
*   **Inquiry Sent:** March 25, 2026, at 09:34 UTC (Sneha Parab).
*   **Confirmation Received:** March 25, 2026, at 12:22:51 UTC (Michael Bui).
*   **Historical Context:** Contract termination occurred last May.

**Summary**
On March 25, 2026, Sneha Parab initiated a check-in to verify if "Citrus Ad" was no longer in use. Michael Bui responded at 12:22 UTC the same day, confirming that their contract was terminated last May. The thread has successfully concluded with this confirmation. All pending actions regarding the status of "Citrus Ad" have been resolved; the team may proceed with any necessary resource reallocations or workflow adjustments based on the confirmed deprecation of the tool.


## [23/37] DPD AI Guild
Source: gchat | Group: space/AAQA5_B3lZQ/9rNMaZEmMZE | Last Activity: 2026-03-25T12:13:58.891000+00:00 | Last Updated: 2026-03-25T14:41:07.560589+00:00
**Daily Work Briefing: DPD AI Guild**
**Resource:** Google Chat Space (URL: https://chat.google.com/space/AAQA5_B3lZQ)
**Date Range:** March 24 – 25, 2026

**Key Participants & Roles**
*   **Nicholas Tan:** Contributor; initiated the discussion by sharing industry news.
*   **Dodla Gopi Krishna:** Participant; provided commentary on leadership implications.
*   **Tan Nhu Duong:** Participant; questioned future development strategies regarding open source.
*   **Michael Bui:** Contributor; highlighted a parallel initiative by Y Combinator CEO Garry Tan and raised the question of open-sourcing.

**Main Topic**
The discussion initially centered on *The Independent*'s report (March 24) detailing Mark Zuckerberg's deployment of an "AI CEO" at Meta, characterized by Nicholas Tan as "tokenmaxxing." The group debated operational implications, including potential leadership redundancy and the tool's future availability. On March 25, Michael Bui expanded the scope by introducing a comparable project: Garry Tan (CEO of Y Combinator) has built a similar initiative hosted at `https://github.com/garrytan/gstack`.

**Decisions Made**
No formal decisions were made during this exchange. The conversation remained speculative regarding future corporate actions by Meta and Y Combinator.

**Pending Actions & Ownership**
*   **None:** No specific action items, tasks, or ownership assignments were generated from this chat thread. However, the community remains curious about the timeline for potential open-sourcing of both the Meta and Garry Tan's respective tools.

**Key Dates & Follow-ups**
*   **March 24, 2026 (06:57:45 UTC):** Nicholas Tan shared *The Independent* article regarding Mark Zuckerberg's AI CEO.
*   **March 24, 2026 (06:59:45 – 07:12:30 UTC):** Follow-up commentary regarding Meta leadership redundancy and open-source potential.
*   **March 25, 2026 (12:13:58 UTC):** Michael Bui shared the GitHub link to Garry Tan's project (`gstack`) and queried its future open-sourcing status.

**Summary of Conversation Flow**
The discussion began on March 24 with Nicholas Tan sharing a report that Mark Zuckerberg has deployed an "AI CEO" at Meta. Dodla Gopi Krishna interpreted this as a signal that Zuckerberg might be redundant or face layoffs, while Tan Nhu Duong questioned when the technology would be open-sourced. Nicholas Tan concluded the initial thread by labeling the trend "tokenmaxxing."

The conversation continued on March 25 when Michael Bui noted that Garry Tan (CEO of Y Combinator) has built a similar tool available at `https://github.com/garrytan/gstack`. Bui echoed the previous sentiment regarding availability, asking specifically when this project would be open-sourced, reinforcing the group's interest in the transparency and accessibility of these AI leadership tools.


## [24/37] #dd-fpg-watchdog-alert
Source: gchat | Group: space/AAAAnlKPglA | Last Activity: 2026-03-25T12:09:22.800000+00:00 | Last Updated: 2026-03-25T14:41:57.254460+00:00
# Daily Work Briefing: #dd-fpg-watchdog-alert

### Key Participants & Roles
*   **Datadog App:** Automated monitoring system.
*   **@hangouts-dd-dpd-watchdog-alert:** Targeted notification channel.
*   *Note: Interactions remain purely automated.*

### Main Topic
The channel tracks **P3 [DPD Watchdog] infrastructure incidents** in Production. Logs show recurring transient issues (excluding `tcp_retrans_jump` and `full_disk_forecast`) aggregated by `story_key`. The alert consistently reads: "Datadog is unable to process your request."

### Incident Summary & Status Update
**Historical Resolved Incidents:**
1.  **Mar 05–17:** 11 distinct events triggered and recovered within the period.
2.  **Mar 18/19:** Incident `story_key`: `10aaf170-dac2-5fec-97bf-cfd442f8706b`. Duration ~5.6 hours. Status: **Resolved**.

**Previously Active Incidents (Now Resolved):**
*   **Mar 20, 2026:** Incident `story_key`: `2787bcd7-d59e-58f0-961a-8f578260cd84`. Duration ~4.4 hours. Status: **Resolved**.
*   **Mar 22, 2026:** Incident `story_key`: `08f5624a-14f1-50e5-9a4a-7418b3602953`. Duration ~3.4 hours. Status: **Resolved**.
*   **Mar 24–25, 2026:** Incident `story_key`: `de0cbb14-ade3-5de2-bfab-cbddd41da779`. Triggered Mar 24 at 22:45 UTC; Recovered Mar 25 at 02:36 UTC. Duration ~3h 51m. Status: **Resolved**.

**Newly Resolved Incident (Mar 25):**
*   **Date:** March 25, 2026.
*   **Time:** Recovered at 12:09 UTC.
*   **Story Key:** `978f6328-424c-53dd-83c8-6411c3aa2158`.
*   **Context:** Previously listed in the "Mar 24 (Old)" entry as triggered at 12:04 UTC. This new data confirms recovery on Mar 25 at 12:09 UTC, extending the duration to approximately 24 hours.
*   **Status:** **Resolved**.

### Pending Actions & Ownership
*   **Immediate Action:** The systemic error "Datadog is unable to process your request" persists across multiple `story_keys`. The recent incident (`978f6328...`) exhibited a significantly longer duration (~24 hours) compared to the Mar 20–25 average (~1.8h to ~3.9h). This deviation suggests potential persistent pipeline degradation rather than standard transient load spikes.
*   **Ownership:** Automated monitoring (`managed_by:datadog-sync`).
*   **Investigation Note:** The extended duration of the `story_key` `978f6328-424c-53dd-83c8-6411c3aa2158` (Mar 24–25) requires immediate scrutiny to distinguish between transient spikes and pipeline stability issues.

### Decisions Made
*   **Status:** No escalation triggered yet as the incident has resolved. However, the resolution time (~24h) exceeds the standard historical average (~3-5 hours).
*   **Protocol:** Continue active surveillance. If a new trigger occurs with similar error messaging and resolution time again exceeds recent norms (specifically >6 hours), escalate immediately to SRE/Platform Engineering.

### Key Dates & Follow-ups
*   **Latest Event:** March 25, 2026, at 12:09 UTC (Recovered).
*   **Monitor ID:** 17447511 (Datadog EU).
*   **Next Steps:** Monitor for recurrence. The extended duration of the Mar 25 incident is an outlier requiring trend analysis.

### References
*   **Space URL:** https://chat.google.com/space/AAAAnlKPglA
*   **Datadog Monitor Link:** [View in Datadog](https://app.datadoghq.eu/monitors/17447511)
*   **Latest Incident (Mar 25 Resolved):** https://app.datadoghq.eu/monitors/17447511?group=story_key%3A978f6328-424c-53dd-83c8-6411c3aa2158&from_ts=1774439571000&to_ts=1774440771000&event_id=8559361398919485850

### Monitor Configuration
*   **Query:** `events("source:watchdog (story_category:infrastructure -story_type:(tcp_retrans_jump OR full_disk_forecast)) env:(PROD OR production OR prod)").rollup("count").by("story_key").last("30m") > 0`


## [25/37] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE | Last Activity: 2026-03-25T12:03:35.798000+00:00 | Last Updated: 2026-03-25T14:46:05.508073+00:00
**Daily Work Briefing: Leads (Ecom/Omni) Digital Product Development**

**Key Participants & Roles**
*   **Sneha Parab:** Lead/Manager; coordinating cross-team support, SAP/API integration blockers, tooling requests, and subscription processes.
*   **Michael Bui:** Engineering/RMN Architect; managing architecture updates, infrastructure compliance, reporting Omni Home swimlane issues, and investigating search performance drops.
*   **Alvin Choo:** Leadership; addressing feedback loops, release schedules, epic queries, AI personalization prioritization, and recent traffic anomalies.
*   **Gopalakrishna Dhulipati:** Lead; overseeing risk registers, delivery approvals, service key rotation with SRE, and clarifying PIC for store purchase surveys.
*   **Others Active:** Daryl Ng (raised OMNI-1157), Andin Eswarlal Rajesh, Olivia, Koklin, Zaw, Ravi.

**Main Topics**
1.  **Critical Search Performance Drop:** Michael Bui flagged a severe decline in impressions on search and category pages (60–70%) since March 18/19. Immediate investigation required to identify if PRD deployments caused this regression. Action involves Daryl Ng, Andin Eswarlal Rajesh, and Alvin Choo.
2.  **SAP/Deposit SKU Integration Blocker:** Marketplace lacks deposit data for SAP API integration. Proposed manual UD failed MP Ops sign-off due to poor PM communication; Olivia rejected new technical solutions. Immediate action from SAP team required.
3.  **Requirement Clarity (BCRS):** Michael Bui flagged that "follow existing ones" is unacceptable acceptance criteria for BCRS deposit posting. Explicit UAT scenarios are required for Definition of Ready (DoR).
4.  **Infrastructure Compliance:** Bitnami ending free Docker images impacts `sonic_raptor` and `mkp-fairnex`. Migration is mandatory.
5.  **Service Key Rotation:** Gopalakrishna Dhulipati requested leads take ownership with the SRE team; discussion moved to a dedicated room.
6.  **B2B Testing Alignment:** Sneha Parab raised queries on finalized B2B testing procedures. Zaw requires guidance on producing MP SKUs specifically for B2B testing.
7.  **New Epic Inquiry (OMNI-1157):** Daryl Ng raised an item from the weekly epics. Ravi indicated this action should only be performed for the new app. Alvin Choo and Gopalakrishna Dhulipati were tagged to clarify status.
8.  **Omni Home Data Discrepancy:** Michael Bui reported a store ID mismatch between Omni Home swimlane and "See All" screen. Team identification remains under investigation (involving Daryl Ng).
9.  **Store Purchase Survey PIC:** Gopalakrishna Dhulipati initiated a query regarding the responsible party for the survey on products purchased at stores.
10. **Scan@Door AI Personalization:** Daryl Ng noted the project lacks PM involvement and requires BE changes; prioritization on the Omni board is under review by Alvin Choo.
11. **1HD Changes & Production Testing:** Andin Eswarlal Rajesh confirmed production testing with leadership is targeted for Friday or Monday. *Note: Search drop investigation may impact this timeline.*
12. **Tooling & Admin (New):** Sneha Parab queried Cursor subscription requests for unsponsored engineers and sought confirmation on current system owners (Discussions concluded March 25).

**Pending Actions & Owners**
*   **Search Performance Investigation:** Identify root cause of 60–70% impression drop since Mar 18/19; correlate with PRD deployments. (Owners: Michael Bui, Daryl Ng, Andin Eswarlal Rajesh, Alvin Choo)
*   **SAP Timeline Resolution:** Push SAP team to explore deposit SKU data solutions. (Owner: Sneha Parab/Alvin Choo/Gopalakrishna Dhulipati)
*   **B2B Testing Procedure:** Clarify MP SKU production alignment. (Owner: Gopalakrishna Dhulipati/Sneha Parab)
*   **Service Key Rotation:** Leads to take ownership with SRE. (Owner: All Leads/Gopalakrishna Dhulipati)
*   **OMNI-1157 Clarification:** Confirm scope applies only to the new app. (Owners: Alvin Choo/Gopalakrishna Dhulipati)
*   **BCRS Requirements:** Define explicit UAT scenarios with Koklin. (Owner: Alvin Choo/Gopalakrishna Dhulipati)
*   **Infrastructure Migration:** Address Bitnami Docker image end-of-life. (Owner: Engineering Team/Michael Bui)
*   **RAW Forms Review:** Review Risk Register for DPD RAW forms; confirm handovers and renew expired forms. Deadline: Tomorrow EOD. (Owner: All Leads/Sazali Bin Mohammed Ali's team)
*   **Survey PIC Identification:** Confirm responsible party for store purchase survey. (Owner: Gopalakrishna Dhulipati/All Leads)
*   **Scan@Door AI Prioritization:** Determine prioritization status on Omni board. (Owner: Daryl Ng/Alvin Choo)
*   **1HD Release Verification:** Confirm release status prior to production testing. (Owner: All Leads/Daryl Ng)
*   **Cursor Subscription & System Owners:** Finalize request mechanism and validate owner list following March 25 discussion. (Owner: Sneha Parab/IT Admin)

**Decisions Made**
*   **RMN Architecture:** Michael Bui updated current, future, and transition architecture diagrams.
*   **Townhall Coordination:** Team to meet Hui Hui post-townhall; no full Q&A scheduled.
*   **Release Status:** Questions remain regarding holding today's regular app release pending the search performance investigation.

**Key Dates & Deadlines**
*   **RAW Forms Review:** Due Tomorrow EOD.
*   **Townhall Meeting:** Today post-townhall session.
*   **Chee Hoe Support:** Effective end of March for Product Catalogue/MarTech scope.
*   **Bitnami Migration:** Ongoing (immediate action required).
*   **1HD Production Testing:** Targeted for this Friday or Monday.


## [26/37] Miguel Ho Xian Da
Source: gchat | Group: dm/0pYlUwAAAAE | Last Activity: 2026-03-25T11:39:55.713000+00:00 | Last Updated: 2026-03-25T14:46:17.874621+00:00
**Daily Work Briefing**
**Source:** Google Chat (Miguel Ho Xian Da)
**Date:** March 25, 2026

**1. Key Participants & Roles**
*   **Michael Bui:** Issue reporter; identified a potential security vulnerability regarding the "MyApp" feature.
*   **Miguel Ho Xian Da:** Technical authority/Developer; confirmed system behavior and provided design rationale.

**2. Main Topic**
Discussion regarding a perceived security risk where office doors can be opened via the "MyApp" feature without requiring user authentication (login) on the device.

**3. Decisions Made**
*   **Confirmation:** The ability to open doors without logging in is an **intended design**, not a bug or security breach.
*   **Rationale Established:** Access logic mirrors physical key card functionality. Since losing a mobile phone is statistically less likely than losing a physical key card, the system prioritizes convenience and availability over mandatory re-authentication for the app.

**4. Actions Pending & Ownership**
*   **Status:** None. The matter was resolved within the conversation (Michael accepted the explanation).
*   **Next Steps:** No further action required at this time.

**5. Key Dates & References**
*   **Conversation Start:** March 25, 2026, 11:36:03 UTC
*   **Resources Referenced:** "MyApp" feature; physical key cards.
*   **Chat URL:** https://chat.google.com/dm/0pYlUwAAAAE

**Summary**
Michael Bui reported that the MyApp allows door access without login, flagging it as a potential security issue. Miguel Ho Xian Da clarified this is intentional design to ensure accessibility in case of lost physical cards, noting higher probability of card loss compared to phone loss. Michael confirmed understanding and accepted the explanation.


## [27/37] BCRS - UAT
Source: gchat | Group: space/AAQACfHCuNI | Last Activity: 2026-03-25T11:05:10.722000+00:00 | Last Updated: 2026-03-25T14:46:38.485586+00:00
**BCRS UAT Daily Briefing Summary (Updated: 25 Mar 2026)**

**Key Participants & Roles**
*   **Sathya Murthy Karthik:** UAT Lead/Coordinator (Provided status update as of 25 Mar).
*   **CS Team:** Completed testing for Returns & Refunds; currently retesting failed Scan & Go cases.
*   **Finance Team:** Reviewing test case statuses; alignment achieved except for Row 30.

**Main Topic**
Status update as of 25 Mar 2026 at 7:00 PM. MP SKU Listing and In-store Pre-order testing have concluded with sign-offs obtained. Focus has shifted to retesting failed Scan & Go cases within the Returns & Refunds module, pending final status updates from Finance.

**Pending Actions & Owners**
*   **Returns & Refunds / Scan & Go:** Failed test cases (specifically Scan & Go) are currently being retested by CS and RPA teams.
    *   *Owner:* S&G/CS Team.
*   **Finance Testing Status Update:** Alignment for failed cases is complete except for Row 30. Finance Team must update statuses for 9 failed and 8 pending cases, including the outstanding Row 30 item.
    *   *Owner:* Finance Team.

**Decisions Made & Clarifications**
*   **MP SKU Listing:** Testing concluded; sign-off officially completed (updated from "due today" to "done").
*   **In-store Pre-order:** Testing concluded; sign-off completed ahead of the scheduled 25 Mar deadline.
*   **Returns & Refunds:** Scope now includes retesting of failed Scan & Go cases following initial CS testing results.

**Status Snapshot (as of 25 Mar, 7:00 PM)**
*   **MP SKU Listing:**
    *   **Status:** Completed with Sign-off.
*   **In-store Pre-order:**
    *   **Status:** Completed with Sign-off.
*   **Returns & Refunds / Scan & Go:**
    *   **CS Testing:** 22 Passed, 0 Pending, 5 Failed (All related to Scan & Go; currently being retested).
    *   **Finance Testing:** 10 Passed, 8 Pending, 9 Failed.
        *   *Note:* Alignment for failed cases is done, pending status update on Row 30.

**Key Dates & Deadlines**
*   **25 Mar 2026 (Tue):** Current reporting time; MP SKU and In-store Pre-order sign-offs completed today.
*   **Previous:** 24 Mar 2026 (Mon).

**Historical Context**
*   **MP SKU Listing:** Previously pending sign-off on 24 Mar; now fully concluded with success.
*   **In-store Pre-order:** Previously delayed to 25 Mar due to FOC alignment issues; testing and sign-off are now complete.
*   **Returns & Refunds:** Scope expanded to include Scan & Go. Previous counts (26 Passed, 8 Failed) have been superseded by new CS data (22 Passed, 5 Failed for Scan & Go) indicating a shift in the test cycle toward retesting. Finance pending cases increased from 11 to 13 total (involving Row 30).


## [28/37] Project Light: Mobilization and Planning Workshop Day 3 - Mar 26
Source: gchat | Group: space/AAQAwOH7W8A | Last Activity: 2026-03-25T10:35:12.694000+00:00 | Last Updated: 2026-03-25T14:46:53.765175+00:00
**Daily Work Briefing: Project Light Mobilization Workshop (Day 3)**

**Key Participants & Roles**
*   **Jacob Yeo**: Primary communicator regarding agenda updates.
*   **Recipients**: 18 total members of the "Project Light" Mobilization and Planning group; 11 have viewed the current agenda document.

**Main Topic/Discussion**
The discussion focuses on critical updates to the agenda for **Day 3** of the Project Light Mobilization and Planning Workshop, scheduled for **March 26**. Jacob Yeo notified the team that there are "latest changes" to tomorrow's schedule, though the specific content of these alterations was not detailed in the chat message itself.

**Pending Actions & Ownership**
*   **Action**: Review the updated agenda containing the latest changes.
    *   **Owner**: All 18 workshop participants (Status: 11 viewed).
    *   **Reference**: [Project Light Workshop Agenda](https://docs.google.com/spreadsheets/d/1ODEEFsP8mMxmUhYNuQ1norNCnWoIJwddZzUFqEUX-qw/edit?gid=1079702164#gid_1079702164) (Spreadsheet).
*   **Action**: Note the changes prior to the start of Day 3.
    *   **Owner**: All participants.
    *   **Context**: Jacob Yeo explicitly requested: "pls take note of the latest changes."

**Decisions Made**
No formal decisions were recorded in this specific chat exchange. The communication serves as a notification mechanism to alert stakeholders that the official agenda has been modified.

**Key Dates & Follow-ups**
*   **Notification Date**: March 25, 2026 (10:35 AM UTC).
*   **Event Date**: March 26, 2026 (Tomorrow relative to notification).
*   **Event Phase**: Day 3 of Mobilization and Planning Workshop.
*   **Follow-up Required**: Immediate review of the linked spreadsheet by all attendees before tomorrow's session.

**Summary Note**
Participants must access the linked Google Sheet immediately, as it contains the finalized agenda for March 26 with unlisted updates that were highlighted by Jacob Yeo.


## [29/37] BCRS Firefighting Group
Source: gchat | Group: space/AAQAgT-LpYY/d1FwEozsGcU | Last Activity: 2026-03-25T10:13:21.909000+00:00 | Last Updated: 2026-03-25T10:39:57.012370+00:00
**Daily Work Briefing: BCRS Firefighting Group**

**Key Participants & Roles**
*   **Sathya Murthy Karthik:** Reported initial mobile crash; provided test credentials (`sng_learningjourney+3@fairprice.com.sg`) and screenshots of the refunded order.
*   **Daryl Ng:** Escalated issue to engineering/support; questioned root cause ("why is the date wrong?").
*   **Wai Ching Chan:** Investigated order details, confirmed system-wide impact (reproduced on own account #75582027), tested on Android (no issue), and coordinated physical debugging meeting.
*   **Piraba Nagkeeran:** Reproduced the crash on iOS; identified root cause as a loop iterating over zero quantity items in the API response.
*   **Andin Eswarlal Rajesh:** Reviewed refund display logic; assigned code fix responsibility to Piraba.

**Main Topic**
Troubleshooting Order #75577957, which crashes on iOS devices upon loading due to a backend data anomaly where delivered/refunded item quantities are recorded as **0**. Initial hypotheses regarding a "1 AD" date error were corrected; the crash is caused by code attempting to loop over zero items (`for _ in 0...serverCartItem.cartQuantity - 1`).

**Pending Actions & Ownership**
*   **Action:** Deploy code fix for the iOS loop crash (handling zero quantity items).
    *   **Owner:** Piraba Nagkeeran
    *   **Status:** Fixed in UAT build; pending deployment.
    *   **Reference Build:** v7.26.0 (51173) released EOD 2026-03-25, including fixes for DPD-822 and DPD-823.
*   **Action:** Verify fix on iOS device using the provided test account.
    *   **Owner:** Sathya Murthy Karthik (Tester) & Team
*   **Action:** Determine if Android requires similar handling despite currently working as expected.
    *   **Owner:** Andin Eswarlal Rajesh / Wai Ching Chan

**Decisions Made**
*   The root cause was confirmed to be the **zero quantity** field in refunded items, not a historical date error ("1 AD").
*   Android clients do not currently crash on this data (likely due to different rendering logic), but iOS requires a code patch.
*   UAT build 7.26.0 is ready for testing the reported issues by EOD 2026-03-25.

**Key Dates, Deadlines & Follow-ups**
*   **Order ID:** 75577957 (Refunded item count: 0)
*   **Recreated Issue Order:** #75582027 (Confirmed same date/quantity issue).
*   **Timeline:** Incident reported 01:50 UTC; UAT build released 10:13 UTC on 2026-03-25.
*   **Follow-up Required:** Validate the new UAT build resolves the crash for Sathya Murthy Karthik's iOS device.

**References**
*   Admin-UAT Order Log: `https://admin-uat.fairprice.com.sg/customer-support/delivery-orders/order-log/75577957`
*   Jira Tickets: DPD-822, DPD-823 (NTUCLink)


## [30/37] RMN Leadership
Source: gchat | Group: space/AAAAQQGZSZU | Last Activity: 2026-03-25T10:11:05.086000+00:00 | Last Updated: 2026-03-25T10:40:24.138704+00:00
**Daily Briefing Summary: RMN Leadership Space (Updated Mar 25)**

**Key Participants & Roles**
*   **Bryan Choong:** Leadership; active oversight on SignCloud cleanup timeline. Currently attending eTail Asia. Emphasized maximizing ROI from event efforts and requested compilation of decks for future reuse.
*   **Allen Umali:** Addressed SRA/Advertima inquiries; leading SignCloud screen cleanup and loop verification.
*   **Rajiv Kumar Singh:** Coordinating SOAC planning and Advertima operations.
*   **Michael Bui:** Inquired about Advertima future clarity.
*   **Pauline Tan:** Active in LinkedIn content cadence and event coordination. Currently attending eTail Asia (as of 04:21 UTC, Mar 25).
*   *Note: Jaren Loy Xing Wei (Departing) remains as per previous context.*

**Main Topics**
1.  **Advertima Partnership Status:** Michael Bui questioned the future of Advertima operations, noting the current SRA covers only the Proof-of-Value (PoV) period. An extended PoV or long-term partnership requires a new Service Request Agreement (SRA). Rajiv Kumar Singh confirmed devices will operate under an extended PoV through end of April pending SRA formalization.
2.  **Advertima Technical Issues:** Reports identified consecutive playback errors in specific stores: an Energy Market Authority (EMA) ad ran three times consecutively, and a "Trust sign up" ad appeared erroneously. Allen Umali clarified that the affected screen is legacy hardware still on SignCloud undergoing manual cleanup; all other screens in the store follow the current play loop correctly.
3.  **SignCloud Cleanup:** Bryan Choong requested a timeline for removing old SignCloud screens. Allen Umali confirmed the full list is available and cleanup will be completed within this week (by Mar 28).

**Pending Actions & Owners**
*   **Advertima SRA Renewal:** Secure a new SRA for long-term Advertima partnership or extended PoV beyond April. *Owners: Allen Umali, Alvin Choo.*
*   **SignCloud Cleanup:** Complete manual removal of legacy screens and resolve loop errors (EMA/Trust ads). *Owner: Allen Umali | Deadline: End of this week (Mar 28).*
*   **Event Asset Compilation:** Compile event decks for future reuse to maximize ROI. *Owner: Pauline Tan.*
*   **Ad Suppression with Osmos:** Provide firm ETA to resolve weeks-old issue. *Owner: Team.*
*   **SOAC Planning:** Finalize targets per CM, supplier, and category by end of March. *Owner: Rajiv Kumar Singh & Ryan.*
*   **Brand/Non-Endemic Sales:** Continue rOOH sales efforts (endemic via JBP; non-endemic via WOG/govt campaigns) and prepare for HPB meeting. *Owner: Team.*
*   **LinkedIn Content Cadence:** Maintain 1–2 posts weekly starting Mar 9. Gather ideas/case studies from the team. *Owners: Pauline Tan & Team (Currently at eTail Asia).*

**Decisions Made**
*   **Advertima Continuity:** Confirmed extended PoV for Advertima devices through end of April pending SRA formalization.
*   **LinkedIn Launch:** "FPG ADvantage" page is live; frequency set at 1–2 times weekly.
*   **SignCloud Resolution:** Old screens are being manually purged; full list identified and cleanup targeted for completion this week.
*   **Strategic Focus:** Priorities during Bryan Choong's absence (and eTail Asia attendance) locked to SOAC targets, rOOH sales, and HPB prep.
*   **Knowledge Management:** Event decks will be standardized and compiled for future reuse to optimize operational efficiency.

**Key Dates & Deadlines**
*   **Mar 2:** Criteo/ChatGPT partnership analyzed; Jaren's departure announced.
*   **Mar 5:** FPG ADvantage LinkedIn page went live.
*   **Mar 9 – Mar 23:** Bryan Choong away from office (Re-engaged Mar 24 regarding SignCloud).
*   **Mar 19:** Advertima extended PoV confirmed for end of April; SRA update identified as necessary.
*   **Mar 25:** Pauline Tan and Bryan Choong attending eTail Asia; request issued to compile event decks.
*   **Mar 28 (Est.):** Completion of SignCloud manual cleanup.
*   **End of March:** Deadline to finalize SOAC targets per CM/supplier/category.
*   **April End:** Current deadline for Advertima extended PoV operations.
*   **Upcoming:** HPB meeting preparation required.


## [31/37] FP x Mirakl
Source: gchat | Group: space/AAAAhWLveDE | Last Activity: 2026-03-25T09:26:19.161000+00:00 | Last Updated: 2026-03-25T10:41:26.258531+00:00
**Daily Work Briefing: FP x Mirakl Integration**

**Key Participants & Roles**
*   **Dang Hung Cuong:** Initiated the initial discussion regarding API rate limiting constraints.
*   **Jill Ong:** Raised a new query on March 25, 2026, regarding seller status creation.
*   **Intrepid (External Integrator):** Third-party partner requesting an increase in API thresholds due to bottlenecks while serving multiple sellers.
*   **Cheryl Jones & LyLy Lim:** Tagged for visibility and action on both the rate limit inquiry and the new seller status query.

**Main Topic**
The thread addresses two distinct technical inquiries regarding the Mirakl platform:
1.  **API Rate Limiting:** Intrepid requested an increase in the current limit of one check per minute, which is hindering multi-seller operations. The team investigated feasibility but had not finalized a decision as of March 17.
2.  **Seller Status Configuration:** As of March 25, Jill Ong queried whether additional seller statuses can be created within Mirakl to accommodate specific needs. Both inquiries require investigation and technical validation.

**Pending Actions & Ownership**
*   **Action A:** Evaluate and respond to Intrepid's request to increase the API rate limiter threshold (currently 1/minute).
    *   **Owner:** Cheryl Jones, LyLy Lim (assigned for feasibility review).
*   **Action B:** Investigate technical feasibility of creating additional seller statuses in Mirakl.
    *   **Owner:** Cheryl Jones, LyLy Lim (tagged by Jill Ong for response).

**Decisions Made**
*   No final decisions were recorded regarding the API rate limit increase or the seller status configuration. Both items remain active inquiries requiring investigation and technical confirmation rather than resolved directives.

**Key Dates & Follow-ups**
*   **Original Inquiry:** March 17, 2026 (06:16 UTC) – API Rate Limit discussion initiated by Dang Hung Cuong. Last activity recorded at 06:40 AM on the same day.
*   **New Inquiry:** March 25, 2026 (09:26 UTC) – Jill Ong raised question regarding additional seller status creation.
*   **Thread Status:** Active with multiple replies across different dates; requires follow-up on both technical constraints and configuration possibilities.
*   **Next Steps:** Review technical feasibility for increasing the API rate limit AND confirm capabilities for creating new seller statuses in Mirakl before coordinating responses to Intrepid and Jill Ong.

**Specific References**
*   **Integrator:** Intrepid.
*   **Current Limit:** Once per minute for checking APIs.
*   **New Query Topic:** Creation of additional seller status in Mirakl.
*   **Platform:** Mirakl API.
*   **Source URL:** https://chat.google.com/space/AAAAhWLveDE


## [32/37] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/BviHwkT97xU | Last Activity: 2026-03-25T09:10:08.322000+00:00 | Last Updated: 2026-03-25T10:42:11.936410+00:00
**Daily Work Briefing: Digital Product Development (Leads) Group**

**Key Participants & Roles**
*   **Sneha Parab:** Initiating inquiry regarding system ownership; coordinating with Sazali.
*   **Daryl Ng:** Providing clarification on current and past system owner assignments.
*   **Sazali:** The individual currently managing the tagging activity for which assistance is requested (mentioned by Sneha).
*   **James & Pandi:** Identified as potential names to tag for "loyalty" ownership.
*   **CCO:** Referenced as an existing owner for loyalty initiatives.

**Main Topic**
The conversation focuses on validating and correcting the list of **system owners** for specific digital product domains: Gifting, EV (Electric Vehicles), and Loyalty within the Ecom/Omni channel. The discussion arose from a request by Sazali to correctly tag system owners during an active data activity.

**Pending Actions & Ownership**
*   **Action:** Tagging system owners for "Loyalty."
    *   **Context:** Sneha requires specific names to tag based on the confirmation that James and Pandi are likely the correct contacts, rather than just "CCO" generally.
    *   **Owner:** Implicitly Sazali (who requested help) or Daryl Ng (who provided the candidate names), pending final confirmation from Sneha to proceed with tagging.

**Decisions Made**
*   **Gifting & EV Ownership:** Confirmed that **Daryl Ng** is the system owner for both "gifting" and "EV."
*   **Loyalty Ownership Status:** Clarified that while "CCO" was previously associated, specific individuals (**James and Pandi**) are likely the correct contacts to tag moving forward.

**Key Dates & Follow-ups**
*   **Date of Discussion:** March 25, 2026 (09:06 – 09:10 UTC).
*   **Next Steps:** Sneha needs to finalize the tagging list with James and Pandi for the Loyalty domain. No specific deadline was set in this thread, but the activity is currently underway.

**References**
*   **Space URL:** https://chat.google.com/space/AAQAN8mDauE
*   **Message Count:** 5


## [33/37] [Leads] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAN8mDauE/23aNS8tE76g | Last Activity: 2026-03-25T08:59:56.409000+00:00 | Last Updated: 2026-03-25T10:43:02.349904+00:00
**Daily Work Briefing: Digital Product Development (Leads)**
**Resource:** [Leads] (Ecom/Omni) Digital Product Development
**Date Range:** March 25, 2026

### Key Participants & Roles
*   **Sneha Parab:** Initiator of the inquiry regarding engineer software access.
*   **Daryl Ng:** Provided information on budget allocation and request channels.
*   **Michael Bui:** Expressed personal need for the subscription.
*   **Gopalakrishna Dhulipati:** Tagged as the point of contact for handling requests (Owner: Pending Action).

### Main Topic
Discussion regarding the process to secure sponsored **Cursor subscriptions** for engineers who do not currently have organization-sponsored licenses. The team confirmed that a budget exists for this purpose and identified the correct internal channel for submission.

### Decisions Made
*   It was confirmed that a specific budget is allocated for Cursor subscriptions.
*   The approved method to request these subscriptions is through **Jazz**.
*   Reference was made to "Winson" as the source of this guidance regarding Jazz and budget availability.

### Pending Actions & Ownership
*   **Action:** Submit requests for Cursor subscriptions via Jazz.
    *   **Owner:** Sneha Parab (confirmed intent to reach out) and Michael Bui (needs access).
*   **Action:** Process/approve the incoming subscription requests.
    *   **Owner:** Gopalakrishna Dhulipati (tagged explicitly by both Sneha Parab and Michael Bui).

### Key Dates & Follow-ups
*   **March 25, 2026, 08:38:** Daryl Ng clarified the Jazz process.
*   **March 25, 2026, 08:53:** Sneha Parab indicated she would follow up ("back to you on this") and tagged Gopalakrishna Dhulipati.
*   **March 25, 2026, 08:59:** Michael Bui reiterated the need for access and also tagged Gopalakrishna Dhulipati.
*   **Next Step:** Follow-up required from the team once Sneha Parab submits requests to Jazz or upon confirmation from Gopalakrishna Dhulipati regarding the intake of these requests.

**Metadata Reference:**
*   Message Count: 6
*   Chat URL: https://chat.google.com/space/AAQAN8mDauE


## [34/37] FPG Everyone - General
Source: gchat | Group: space/AAAAjDYVcBU | Last Activity: 2026-03-25T08:08:27.885000+00:00 | Last Updated: 2026-03-25T10:44:18.786132+00:00
**Daily Work Briefing: FPG Everyone Chat Summary (Updated)**
**Date Range:** March 3 – March 21, 2026 (plus Mar 25 update)
**Source:** Google Chat (FPG Everyone - General)

### Key Participants & Roles
*   **Maisy Heeng:** Marketing/Product Announcement Lead.
*   **Mary Pereira:** Mediacorp Microdrama Collaboration Lead.
*   **Jolene Lim:** Own Brands Team (FairPrice Foaming Hand Soap).
*   **Eva Wang, Siew Mei Chu, Ng Zhuang Shu:** OB Sensory Team.
*   **Zhaoyue Touw & Ariel Yap:** Unity/Wellness Campaign Lead.
*   **Cheryl Tan:** NTUC Women and Family Event Coordinator.
*   **Kara Pua & Chloe Ong:** Loyalty/Rewards Coordination.
*   **Pauline Tan:** FPG ADvantage LinkedIn Page Launch Lead.
*   **Vincent Phua:** Digital & Technology Announcement (Cardless Access).
*   **Jenna Poh:** Day of Service Coordinator.
*   **Siti Nabilah:** Day of Service Campaign Promoter (New context for Mar 25 update).

### Main Topics
1.  **Digital Access Rollout:** Schedule confirmed: Live (Facilities/Tech); Mar 16 (C-suite/HR/Finance); Mar 23 (Customer/Marketing/E-Commerce); Mar 30 (Remaining Hub staff). User guide distributed.
2.  **Media Collaboration – "Bowl of Love":** FairPrice launched a microdrama with Mediacorp featuring fresh pork from Malaysia, focusing on Mdm Gao and porridge.
    *   **Status:** Episodes 1–5 starring Tyler Ten were previously live. **Final episodes are now officially live** following the March 20 launch. The finale features Tyler Ten, Tasha Low, and Xiang Yun depicting a story of warmth and healing.
    *   **Platform:** @mediacorp.re.dian TikTok (`https://vt.tiktok.com/ZSusN9b4n/`).
3.  **Sensory Testing Panels:**
    *   **Frozen Snacks:** Evaluation conducted on March 18 & 19, 2026 (3 slots). Limited to 40 panelists. Mobile device submission required. Sign-up closed.
    *   **Chapati:** Screening form remains open.
    *   **Frozen Processed Food/Nuts:** Session status pending confirmation of overlap with Frozen Snacks dates.
4.  **Wellness Campaign – World Oral Health Day:** Ariel Yap promoted daily oral care routines ahead of the occasion, extending offers through March 25.
    *   **New Offer Details:** Up to 50% OFF essentials at Unity stores. Featured: Listerine Mouthwash (2 for $15.95), Colgate Charcoal Toothpaste (2 for $12.95), Colgate Gentle Gum Care Brushes (2 for $14.90), and Oral-B Vitality Electric Toothbrush ($48.10).
    *   **Offer Link:** https://go.fpg.sg/WOHD

### Pending Actions & Ownership
*   **Day of Service Registration (Owner: All Staff):** Final call issued by Siti Nabilah on March 25. Join the "Willing Hearts Kitchen Crew" on **March 27, 2026 (Friday)**, 1:00 PM – 5:00 PM at Joo Chiat Place to prep/cook/pack **3,000 meals**.
    *   **Urgency:** Only **20 spots left** remain.
    *   **Link:** `https://forms.gle/Y4B22gtUmU7SF42V6`
*   **Sensory Test Sign-ups (Owner: All Staff):** Chapati screening form remains open (`https://forms.gle/DFYrahZcvhtcoJ9R7`). Frozen Snacks sign-up is closed.
*   **Wellness Engagement:** Visit Unity stores for deals before Mar 25 or explore https://go.fpg.sg/WOHD.

### Critical Dates & Deadlines
*   **March 6:** End of Foaming Hand Soap offer (Completed).
*   **March 8:** International Women's Day Celebration (Completed).
*   **March 12:** Non-Halal Soup Sensory Evaluation (Completed).
*   **March 16–30:** Cardless access rollout phases.
*   **March 17:** Frozen Food/Nuts session (Status: Pending confirmation/overshadowed).
*   **March 18–19:** Frozen Snacks Sensory Evaluation (Completed).
*   **March 21:** "Bowl of Love" finale episodes live on TikTok.
*   **March 22:** FairPrice Walnuts with Cranberries redemption ends.
*   **March 25:** World Oral Health Day offers expire at Unity stores; Final call for Day of Service issued.
*   **March 27 (Friday):** Day of Service at Willing Hearts Kitchen (1:00 PM – 5:00 PM).

### Decisions Made
*   No formal strategic decisions recorded; focus remains on correcting Cardless Access communication, recruiting panelists for Frozen Snacks/Chapati testing, promoting the "Bowl of Love" microdrama collaboration (now complete with finale release), supporting World Oral Health Day initiatives via Unity stores (extended to Mar 25), and coordinating the March 27 Day of Service event.
*   **Updated:** Siti Nabilah has issued a final urgent call for the March 27 service, confirming only 20 spots remain for the "Kitchen Hero" mission at Joo Chiat Place.


## [35/37] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY/VjNIGhgr76c | Last Activity: 2026-03-25T07:57:46.777000+00:00 | Last Updated: 2026-03-25T10:44:37.022858+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Key Participants & Roles**
*   **Sneha Parab:** Initiator of the request; coordinating BCRS status and deployment planning.
*   **Engineers:** Target audience for the status update request.
*   **Daryl Ng:** Carbon copy recipient.
*   **Andin Eswarlal Rajesh:** Carbon copy recipient.

**Main Topic**
Urgent alignment on Jira ticket statuses within the Digital Product Development space to ensure accurate tracking of deployments and prevent blockers in the release queue. Sneha highlighted that many tickets lack assignees due to Frontend (FE) and Backend (BE) subtasks, complicating status updates.

**Pending Actions & Ownership**
*   **Update Ticket Status:** All engineers must mark tickets deployed to production as **"Done"**.
    *   *Owner:* All Engineers.
*   **Highlight Pending Deployments:** Any deployments currently pending must be explicitly highlighted in this chat thread.
    *   *Owner:* All Engineers.
*   **Resolve Subtask Blockers:** Address specific subtasks (e.g., FE/BE) that are keeping parent stories in the "In Release Queue" status. Sneha provided **DPD-79** as an example where one subtask remains in the queue, preventing the main story from moving forward.
    *   *Owner:* All Engineers.

**Decisions Made**
*   No formal project decisions were recorded; however, a protocol was established requiring immediate status updates to allow for contingency planning.
*   Immediate action is required today so that tomorrow can be utilized to plan for any missed deployments.

**Key Dates & Deadlines**
*   **Date of Communication:** March 25, 2026 (07:55 AM UTC).
*   **Action Deadline:** Today (March 25, 2026) via the end of the day to facilitate planning.
*   **Upcoming Release:** Marketplace tickets are planned for release tomorrow in sync with the SAP deployment.

**References & Links**
*   **Jira Filter for Open Tickets:** [View Link](https://ntuclink.atlassian.net/jira/software/projects/DPD/issues?jql=project+%3D+DPD%0Aand+parent+%3D+DPD-225%0Aand+status+IN+%28%22IN+RELASE+QUEUE%22%2C+%22TESTING+IN+PREPRODUCTION%22%2C+%22IN+DEVELOPMENT%22%29%0AORDER+BY+assignee+ASC%2C+status+ASC%2C+created+DESC&atlOrigin=eyJpIjoibDoxZGJlMzZkNjBjNDY3MmIxMzYwZmMyYTgzZDg4ZWEiLCJwIjoiaiJ9) (Statuses: "IN RELASE QUEUE", "TESTING IN PREPRODUCTION", "IN DEVELOPMENT").
*   **Example Issue:** [DPD-79](https://ntuclink.atlassian.net/browse/DPD-79).


## [36/37] [Internal] (Ecom/Omni) Digital Product Development
Source: gchat | Group: space/AAQAUbi9szY | Last Activity: 2026-03-25T07:55:26.595000+00:00 | Last Updated: 2026-03-25T10:45:03.850263+00:00
**Daily Work Briefing: Digital Product Development (Ecom/Omni)**

**Key Participants & Roles**
*   **Sneha Parab:** BCRS/Fees/Store Closure Impact Lead.
*   **Daryl Ng:** Backoffice/Order Management/Bug Reporting / Slot Logic validation.
*   **Michael Bui:** BCRS Deposit Logic/SAP Integration/Publisher of PRs.
*   **Wai Ching Chan:** Order Service Deployment/Slot Logic Validation.
*   **Andin Eswarlal Rajesh:** Frontend (iOS/Android) & BCRS UX queries / Amplitude tracking.
*   **Lester Santiago Soriano:** Backend Services Lead.
*   **Zaw Myo Htet:** Payment/Feature Flagging.
*   **Shiva Kumar Yalagunda Bas:** Slot discrepancy reporting.

**Main Topics Discussed**
1.  **Website SDK Deployment (Strudel):** Lester deployed `go-platform-website` on Mar 19 to update the Strudel SDK for maximum voucher validation. Changes were reviewed via Bitbucket diff between v1.5.11 and v1.5.10.
2.  **Pre-order Payment Logic & UAT:** Zaw initiated an inquiry on Mar 24 regarding pre-order flows (app payment vs. POS redemption) and requested peer review for the offline pre-order admin page (`https://admin-uat.fairprice.com.sg/in-store-preorder/offline`).
3.  **Slot Date Discrepancy:** Shiva reported a delivery slot mismatch (UI shows 25th, API indicates 23rd). Daryl Ng and Sundy Yaputra are resolving this.
4.  **UAT Stock Requirements:** Sneha requested high-stock SKUs for Zi Ying's bulk order testing; Wai Ching Chan and Akash Gupta were tasked to check IMS availability.
5.  **Order Verification Bug (NED-278216):** Investigation continues into the Whitelisting API returning older contract data (identified by Andin).
6.  **BCRS Deposit & SAP Integration:** Critical duplicate deposit posting fix remains active (PR #6). Marketplace tickets are planned for release tomorrow in sync with SAP deployment.

**Pending Actions & Ownership**
*   **All Engineers:** Mark all tickets deployed to production as "Status = Done." Highlight any pending deployments in this chat thread immediately (Sneha Parab).
*   **Zaw Myo Htet:** Clarify pre-order payment redemption logic; execute UAT testing on offboarded Pinelabs split feature flag.
*   **Lester Santiago Soriano:** Assist with Whitelisting API contract issue (cc: Piraba Nagkeeran, Jonathan Tanudjaja). Deployment completed Mar 19.
*   **Wai Ching Chan & Akash Gupta:** Source high-stock SKUs from IMS for Zi Ying's bulk order testing and investigate UAT SKU `13023506` threshold settings.
*   **Daryl Ng & Sundy Yaputra:** Resolve delivery slot date mismatch (UI showing 25th vs API 23rd).
*   **Andin Eswarlal Rajesh:** Investigate iOS slot mapping error and assist with Amplitude event tracking flow inquiry.

**Decisions Made**
*   **Status Protocol:** All engineers must update Jira ticket status to "Done" upon production deployment; pending items must be flagged in the chat thread.
*   **Deployment Approval:** PLU processor deployment approved pending UD alignment.
*   **Code Review Priority:** Focus shifted to `go-platform-website` PR #1538 for the Strudel SDK update, superseding previous layout-service priorities. Current focus includes reviewing the new offline pre-order admin page.

**Key Dates & Deadlines**
*   **Mar 19, 2026:** Website deployment completed at 4:00 PM; UAT stock sourcing required immediately.
*   **Mar 24, 2026:** Zaw Myo Htet initiated inquiry regarding the offline pre-order admin page and pre-order payment logic.
*   **Mar 25, 2026 (Today):** Sneha Parab requested status updates on production deployments and highlighted open tickets via Jira filter ID: DPD-225 queue.
*   **Tomorrow:** Marketplace tickets release in sync with SAP deployment.
*   **Thursday:** D&T All Hands meeting.
*   **Mar 31, 2026:** Sports Hub FFS store closure deadline.

**Note on Historical Context:** Previous mentions of code review priorities for `layout-service` PR #362 and `website-service` PR #649 are superseded by the urgent Strudel SDK deployment update. The focus has now shifted to resolving slot date mismatches, pre-order payment logic queries, and the newly flagged offline pre-order admin page review. A new procedural requirement mandates immediate status updates for production tickets.


## [37/37] Project Light: Spotlight Topic - HIVE/Inventory - Mar 25
Source: gchat | Group: space/AAQACrAwhoI | Last Activity: 2026-03-25T07:28:24.185000+00:00 | Last Updated: 2026-03-25T10:45:39.058153+00:00
**Daily Work Briefing: Project Light – HIVE/Inventory Session**

**Key Participants & Roles**
*   **Jacob Yeo:** Session Organizer/Coordinator (Confirmed via reminder message).
*   **Attendees:** Total of 14 participants viewed the initial notification out of a projected group of 23. Specific roles for other attendees were not detailed in the provided text.

**Main Topic/Discussion**
The conversation focused on logistical confirmation for an upcoming "Spotlight Topic" session regarding **HIVE/Inventory**. The primary objective was to ensure all participants are aware of the specific physical location for the meeting to prevent attendance issues.

**Pending Actions & Ownership**
*   **Action:** Attendees must proceed to the designated room at the scheduled time.
    *   **Owner:** All 23 group members (implied).
*   **Action:** Jacob Yeo has completed the notification duty; no further explicit action items were assigned in this specific thread segment.

**Decisions Made**
*   **Location Confirmation:** The session location was finalized as **Level 10, Training Room 2**. This decision was communicated to the group on March 25, 2026.

**Key Dates & Deadlines**
*   **Event Date:** March 25, 2026 (Today).
*   **Notification Time:** 07:28:24 UTC.
*   **Follow-up:** The meeting is scheduled to commence immediately following the notification window; no future follow-up meetings were mentioned in this snippet.

**Summary**
Jacob Yeo issued a logistical reminder for the Project Light "HIVE/Inventory" Spotlight Topic session held on March 25, 2026. The critical update was the venue assignment: **Lvl 10 Training Room 2**. This message reached 14 of the 23 expected participants prior to the briefing time. No other discussion points or action items were recorded in this specific log entry.
