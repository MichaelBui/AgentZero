# Daily Work Report - April 7, 2026

## Executive Summary

**Key Highlights:**
• **Critical Data Integrity Incident**: Osmos vendor escalated UBID missing issue affecting retail media tracking accuracy (Relevance: 9/10)
• **BCRS Launch Blocker**: Express Delivery launch blocked by incorrect cost center mapping for deposits; ticket DPD-898 created with Finance confirmation pending
• **SLO V2 Migration Urgent**: All SLO V1 monitors must be muted tomorrow as part of transition to request-based alerting framework
• **Vendor Coordination Pressure**: Project Light sprint kickoff requires immediate API specs and documentation from Michael
• **Production Stability Concerns**: GKE cluster capacity exhaustion caused March 23rd outage; Redis CPU high on Catalogue Service; Datadog logging costs at $3k+

**Data Sources Processed:**
• Jira: 56 tickets fetched, 22 summaries generated (high relevance items)
• Gmail: 60 threads scanned, 13 summaries generated (critical incidents and meetings)
• Google Chat: 71 conversations found, 32 summaries generated (active engineering discussions)

**Work Stream Status:**
- **Retail Media/Ad Tech**: Active development on impression-based inventory model; critical UBID tracking issue requires immediate intervention
- **BCRS Compliance**: Phase 2 deployment imminent; cost center mapping fix needed before April 9th deadline
- **SLO Framework**: V1 to V2 migration in progress; action items require completion by tomorrow
- **Project Light**: Vendor sprint kickoff; API specs due end-of-day today
- **Infrastructure**: Cost optimization inquiry on logging services; capacity issues resolved but monitoring needed

---

## Action Items

### Critical (Today)
• **Respond to Osmos UBID Data Integrity Issue** - Email thread 19d52fdf13c8b0bd (Relevance: 9/10). Vendor Rahul Jain flagged that FairPriceGroup systems are not sending User Browsing ID in 'uclid' parameter during funnel impression events. Osmos is assigning dummy UBIDs, compromising tracking accuracy for display and product ads. Michael must provide clarification on UBID/uclid definitions, specific customer journey context, and scope of impact (platform/page/ad type). Nikhil Grover also engaged to identify specific ad units involved.

• **Approve Access Request for Project LIGHT** - Email thread 19d60df9559bf07b. Hengky Sucanda requested access to 'Project LIGHT' Confluence space. As engineering leader governing platform architecture, Michael must review this request and ensure proper access controls for staff-level personnel working on retail e-commerce initiatives.

• **RSVP to Carrier-Based Targeting Meeting** - Email thread 19d65c01ab98b4d9 (Relevance: 9/10). Nikhil Grover invited Michael to meeting on April 7th at 11:45 AM SGT regarding carrier-based targeting capabilities for retail media network. Session aims to resolve technical requirements for syncing user data from mobile carriers (Singtel, M1) into Segment platform. Michael's input critical for validating technical feasibility and defining synchronization strategy.

• **Provide RMN Invoicing Fields Review** - Email thread 19d621a83c12208d (Relevance: 9/10). Nikhil Grover shared spreadsheet titled "RMN Invoicing - Fields requirement". Michael must review to confirm technical feasibility and provide architectural input on how fields map to existing microservices and event-driven systems.

• **Complete SLO V1 Monitor Muting** - Email thread 19d67245db53ca1b (Relevance: 7/10). Meeting notes from April 7th SLO updates session indicate all V1 monitors must be muted by tomorrow. Team must acknowledge new alerts and investigate root causes. Michael owns backend architecture standards and SLO governance.

### High Priority (This Week)
• **Create Jira Ticket for BCRS Cost Center Mapping Fix** - GChat thread 25/32 (Relevance: 9/10). Express Delivery launch blocked by orders with BCRS SKUs incorrectly routing to cost center 004 instead of store-specific mapping (F418). Rajesh Dobariya created DPD-898 after awaiting Finance confirmation. Michael must ensure ticket creation and track resolution before April 9th deployment deadline.

• **Finalize Project Light API Specifications** - GChat thread 32/32 (Relevance: 9/10). Alvin Choo explicitly requested Michael to ensure RMN first sprint spec is ready. Michael confirmed discussing with Nikhil previously and designing APIs, committed to sharing spec by end-of-day today (April 7th).

• **Review GCP Service Account Key Rotation** - GChat thread 19/32 (Relevance: 8/10). Kyle Nguyen and Himal Hewagamage leading security initiative for key rotation/decommissioning. Michael needs to review spreadsheet and consent to automated rotation for legacy keys in non-prod environments.

• **Provide Project Nova Cost Analysis** - Email thread 8/13 (Relevance: 8/10). B2b discussion notes indicate Michael assigned action items: calculate B2C core infrastructure costs (including AWS Identity/Communication, catalog, FPM Pro components) and identify data source for DBP catalog service product enrichment. Group must compile performance data (RPS, storage, cache) to validate vendor proposals before Huawei follow-up.

• **Grant Access for FairPrice+to+DSP Migration Design** - GChat thread 20/32 (Relevance: 9/10). Lester Santiago Soriano requested access to Confluence page 'FairPrice+to+DSP+Transaction+Migration+Design'. Michael must review or grant access as Engineering Governance lead for architectural RFCs.

• **Share Original BCIS Ticket Details** - Email thread 9/13 (Relevance: 7/10). Meeting notes from BCRS SKU posting discussion suggest Michael share details of original BCIS ticket regarding deposit mapping discrepancy. Decision involves Finance validation and Jira ticket creation related to DBD3.

• **Confirm China Visa Documentation** - GChat thread 18/32 (Relevance: 9/10). Michael preparing business trip to CoMall Wuhan; Alvin Choo securing invitation letter for Visa Type M application. Michael needs to confirm if prioritization request is complete and provide any additional details needed.

• **Review RTI Document Request** - GChat thread 21/32 (Relevance: 9/10). Gautam Singh directly messaged requesting document Michael created regarding 'RTI'. Michael must locate and share specific deliverable as direct stakeholder communication requiring immediate attention.

### Medium Priority (When Possible)
• **Attend SLO Updates Session** - Email thread 4/13 (Relevance: 8/10). Dodla Gopi Krishna invited Michael to 'Session 1: Sharing on SLO updates' scheduled April 7th at 4 PM SGT. Agenda covers limitations of existing framework, new architectural design, impact on developers, migration planning, Q&A session.

• **Review Unit Price Calculation Refactor** - Jira ticket OMNI-1179 (Relevance: 7/10). Compliance improvements for cart calculation logic; scope reduced to core CRUD and calculation services. Recent discussion involved conflict where Rajesh Dobariya initially confirmed removal but reversed decision after realizing it's a compliance topic requiring SteerCo discussion.

• **Evaluate Impression-Based Inventory Model** - Jira ticket OMNI-1421 (Relevance: 6/10). Transition from fixed slots to impressions-based system targets $900k annual incremental revenue. Assigned to Nikhil Grover with 'In Development' status pending completion of related activation tasks.

• **Monitor TP Domain Link Configuration** - Jira ticket OMNI-1420 (Relevance: 6/10). Enabling 3P domain links to open in-app browser without app updates, reducing campaign lead times from 4 weeks. Final solution involves backoffice-managed configuration approach.

• **Review AI Shopping Assistant Scope** - Jira ticket OMNI-1235 (Relevance: 6/10). Koklin Gan managing scope definition and PRD delays. Technical constraints identified by Vivian Lim (3-week web app, 2-week backend) and strategic questions from Peter Talbot regarding scalability across Omni home and PDP journeys.

• **Validate Available to Promise MVP** - Jira ticket OMNI-1391 (Relevance: 6/10). Addresses inventory logic flaw causing false stock-outs; proposes time-based ATP calculations for Fresh/Van SKUs with $5.5M GMV impact. Project scope remains fluid due to alignment discussions with HIVE team.

---

## Follow-ups

### Waiting on Others
• **Finance Confirmation on BCRS Cost Center Mapping** - Requested from Finance team regarding correct store-specific mapping for BCRS deposits. Last status: Rajesh Dobariya awaiting confirmation after April 6th meeting. Escalation needed if not received by end of day today to meet April 9th deployment deadline.

• **Osmos Vendor UBID Clarification** - Rahul Jain (Osmos) flagged data integrity issue on April 3rd, requesting clarification from Michael. Last status: Michael responded with questions about definitions and scope; awaiting vendor response with specific customer journey context and impact assessment.

• **SLO V2 Migration Timeline** - Dodla Gopi Krishna sent SLO updates session invite for April 7th at 4 PM. Last status: Meeting scheduled but migration plan details not yet finalized. Need confirmation on final timeline for complete V1 removal within 3-4 weeks after month observation.

• **Project Light Vendor Sprint Coordination** - Alvin Choo flagged sprint kickoff with vendor team accelerating rapidly. Last status: Michael confirmed discussing RMN expectations with Nikhil; API specs due end-of-day today but vendor team moving fast and may need immediate alignment on documentation gaps.

• **China Visa Invitation Letter** - Michael preparing trip to CoMall Wuhan; Alvin Choo securing invitation letter from CoMall. Last status: Application delayed due to being on leave; need confirmation if invitation letter received and visa application submitted successfully.

• **GCP Service Account Rotation Consent** - Kyle Nguyen leading key rotation initiative with spreadsheet review required. Last status: Michael notified of initiative but hasn't provided consent yet for automated rotation of legacy keys in non-prod environments.

• **Unit Price Calculation SteerCo Decision** - Rajesh Dobariya reversed decision on removing cart calculation service after realizing compliance topic requires SteerCo discussion. Last status: Ticket remains active with Sathya Murthy Karthik re-adding to avoid closing prematurely; awaiting steering committee alignment.

### Pending Michael's Action
• **Project LIGHT Confluence Access** - Hengky Sucanda requested access approval pending Michael review. Last status: System-generated notification received April 6th at 11:39 AM SGT; no response yet from Michael on granting/rejecting access request.

• **Carrier-Based Targeting Meeting RSVP** - Nikhil Grover invited to April 7th meeting at 11:45 AM. Last status: Invitation received but Michael hasn't confirmed attendance yet despite critical technical feasibility questions requiring his input.

• **RMN Invoicing Fields Review** - Spreadsheet shared by Nikhil Grover on April 6th at 5:23 PM SGT. Last status: Email notification received; no review comments or architectural feedback provided yet from Michael.

• **TP Domain Link Solution Validation** - OMNI-1420 ticket shows final solution involves backoffice-managed configuration approach. Last status: Design completed but Michael hasn't reviewed and approved the architecture pattern for platform stability compliance.

---

## Work Stream Summaries

### Retail Media / Ad Technology (RMN)
**Current Status:** Active development with critical incidents requiring immediate intervention

**Recent Changes:**
• **Impression-Based Inventory Transition**: DPD-838 moving from 'To Be Defined' to 'In Development'. Michael identified critical architectural ambiguities on April 1st regarding scope boundaries between new video-capable components and legacy services. Video support restricted to Omni Home/FP Pay; endemic detection uses exact boolean matching.
• **UBID Data Integrity Incident**: Osmos vendor escalated that FairPriceGroup systems not sending User Browsing ID in 'uclid' parameter during funnel impression events. Vendor assigning dummy UBIDs, compromising tracking accuracy for display and product ads. Immediate architectural review required to restore SLO compliance.
• **Carrier-Based Targeting Integration**: Nikhil Grover coordinating with Singtel/M1 carriers to sync user data into Segment platform for precise audience segmentation. Technical feasibility validation needed from Michael before implementation proceeds.

**Decisions Pending:**
• **Feature Flag vs Backend Config**: OMNI-1420 involves decision between Split feature flags (rejected by Winson Lim as intended for experimentation) versus backoffice-managed configuration approach for 3P domain link handling. Michael must validate architecture pattern for platform stability.
• **RMN Invoicing Fields Mapping**: Spreadsheet shared with specific data fields required; Michael needs to confirm how these map to existing microservices and event-driven systems before technical implementation begins.

**Blockers:**
• **UBID Tracking Accuracy**: Critical incident blocking ad inventory tracking until configuration corrected. Vendor impact assessment needed before deployment can proceed safely.
• **Sprint Velocity Coordination**: Project Light vendor team accelerating rapidly; documentation gaps creating risk of misalignment on RMN integration requirements.

**Cross-References:**
• Jira: DPD-838 (Impression-based transition), OMNI-1421 ($900k revenue opportunity), OMNI-1420 (TP domain links)
• Gmail: UBID incident thread, RMN invoicing fields spreadsheet
• GChat: Project Light Attack/Defence leads discussions on API specs and vendor coordination

### BCRS Compliance & Express Delivery
**Current Status:** Deployment imminent with critical cost center mapping issue blocking launch

**Recent Changes:**
• **Cost Center Mapping Discovery**: Orders with BCRS SKUs incorrectly routing to cost center 004 instead of store-specific mapping (F418). Technical solution agreed upon: retrieving store identification directly from order service during SIT.
• **Ticket DPD-898 Created**: Rajesh Dobariya created tracking ticket after awaiting Finance confirmation on deposit posting flow. Ticket links to BCRS compliance epic and requires Finance validation before deployment.
• **UAT Issue Identified**: Wai Ching Chan reported BCRS deposits missing during checkout in UAT testing, requiring immediate investigation and fix.

**Decisions Pending:**
• **Finance Mapping Confirmation**: Must confirm correct store-specific cost center mapping logic for deposit postings before April 9th deployment deadline.
• **BCRS Deposit Posting Suppression**: DPD-842 subtask in 'TESTING IN PREPRODUCTION' status; Michael documented issue capture mechanism and confirmed re-delivering order will no longer trigger duplicate postings to SAP.

**Blockers:**
• **Finance Validation Delay**: Cost center mapping fix blocked awaiting Finance confirmation on deposit posting logic. Risk of missing April 9th deployment window if not resolved today.
• **UAT Test Coverage**: Missing BCRS deposits during checkout indicates test coverage gaps that must be addressed before production rollout.

**Cross-References:**
• Jira: OMNI-1294 (BCRS Phase 2), DPD-383 (Sales posting Done), DPD-842 (Duplicate suppression in testing)
• Gmail: BCRS SKU Posting meeting notes, cost center mapping discussion
• GChat: Multiple threads on BCRS deployment coordination and resource allocation

### SLO Framework & Infrastructure Governance
**Current Status:** V1 to V2 migration in progress with urgent action items requiring completion tomorrow

**Recent Changes:**
• **SLO V2 Transition**: Session 1 sharing on updates scheduled April 7th at 4 PM. V1 found ineffective due to false positives and maintenance overhead; V2 introduces request-based formula for better customer impact reflection.
• **Production Incident Review**: March 23rd outage caused by GKE cluster capacity exhaustion (Memory pressure leading to pod evictions on picking-service), resulting in SocketTimeoutExceptions for Picker App users.
• **Cost Optimization Inquiry**: Datadog logging costs at $3k+ for services named 'be', 'fe', and 'N/A'; Michael identified project as 'fpg-retail-pos-prod' running on doriscluster under Project Nova scope.

**Decisions Pending:**
• **V1 Monitor Muting**: All V1 monitors must be muted tomorrow as part of transition to request-based alerting framework. Team must acknowledge new alerts and investigate root causes immediately.
• **On-Call Structure Alignment**: Sneha Parab raised question about on-call management under new team structure. Structural changes to Datadog teams and SLO v2 migration will significantly alter engineering responsibilities for on-call duties.

**Blockers:**
• **Alert Migration Timeline**: V1 removal planned within 3-4 weeks after month observation; must ensure complete transition without service degradation during this window.
• **Infrastructure Scaling Issues**: Redis CPU high on Catalogue Service; unresolved P1 incident (IR-49) regarding unavailability of picking lists requiring immediate investigation.

**Cross-References:**
• Jira: DPD-644 (Event synchronization Done), DPD-733/715 (Ad slots completed)
• Gmail: SLO updates session invitation and meeting notes
• GChat: Multiple infrastructure governance discussions on scaling, cost optimization, and incident triage

### Project Light & Vendor Management
**Current Status:** Sprint kickoff underway with immediate API spec requirements

**Recent Changes:**
• **Vendor Sprint Acceleration**: Alvin Choo flagged sprint 1 start with vendor team moving rapidly; Michael noted vendor likely utilizes AI agents for speed, requiring immediate coordination to manage velocity.
• **API Design Ownership**: Michael confirmed discussing RMN expectations with Nikhil previously and designing APIs; committed to sharing spec document by end-of-day today (April 7th).
• **Documentation Gap Identification**: Tiong Siong Tee questioned documentation status and methods to proceed with 'fppay' tasks without clarification, creating risk of misalignment.

**Decisions Pending:**
• **API Specification Delivery**: Must share RMN first sprint spec by end-of-day today; Alvin Choo explicitly requested this as prerequisite for vendor work to proceed correctly.
• **Chat Space Establishment**: Michael raised follow-up question regarding establishing official chat space to connect with CoMall teams for project kick-off activities.

**Blockers:**
• **Documentation Completeness**: Vendor team moving fast but spec documents not yet finalized; risk of rework if requirements misunderstood or incomplete.
• **Cross-Team Coordination**: Need to establish proper communication channels between FairPrice and Comall teams to ensure alignment on technical requirements and delivery timelines.

**Cross-References:**
• Jira: OMNI-1407 (Seller catalogue compliance), DPD-898 (BCRS fix)
• Gmail: Project Light planning workshop materials, analytics reports
• GChat: Multiple threads on vendor coordination, API design, and sprint planning

### Infrastructure & Cost Optimization
**Current Status:** Active cost inquiry with potential $3k+ monthly savings opportunity

**Recent Changes:**
• **Logging Cost Investigation**: Datadog logging costs at $3k+ for services named 'be', 'fe', and 'N/A'; Michael identified project as 'fpg-retail-pos-prod' running on doriscluster under Project Nova scope.
• **B2C Core Infrastructure Review**: Team discussing shifting B2C infrastructure management from hands-on operations to vendor governance model based on SLAs; core identity and communication services retained on GCP while evaluating other services for migration.
• **Service Account Security**: Kyle Nguyen leading GCP service account key rotation/decommissioning initiative with Michael needing to review spreadsheet and consent to automated rotation for legacy keys in non-prod environments.

**Decisions Pending:**
• **B2C Cost Calculation**: Michael assigned action item to calculate B2C core infrastructure costs including AWS Identity/Communication, catalog, and FPM Pro components; must identify data source for DBP catalog service product enrichment.
• **Vendor Proposal Validation**: Group must compile performance data (RPS, storage, cache) to validate vendor proposals before scheduled follow-up with Huawei.

**Blockers:**
• **Performance Data Collection**: Need comprehensive RPS, storage, and cache metrics from all services to properly evaluate vendor proposals and make informed migration decisions.
• **Legacy Key Security**: Non-prod environment requires automated rotation consent; delay in approval could leave legacy keys exposed longer than necessary.

**Cross-References:**
• Jira: OMNI-1249 (B2B integration), OMNI-1363 (SAP decoupling)
• Gmail: B2b discussion notes, infrastructure cost analysis request
• GChat: Cost optimization inquiry on logging services, vendor evaluation discussions

---

## Patterns and Observations

### Recurring Themes
1. **Architecture Governance Integration**: Michael consistently involved in technical decision-making across all work streams, from retail media to infrastructure governance. Pattern shows strong ownership of backend architecture standards and SLO targets.
2. **Vendor Coordination Pressure**: Multiple vendor partnerships (Osmos, Comall, Huawei, Accenture) requiring active management and documentation; pattern indicates Michael serves as critical bridge between internal teams and external partners.
3. **Compliance-Driven Development**: BCRS compliance, unit pricing regulations, data security policies driving engineering priorities; pattern shows business/regulatory requirements frequently becoming technical blockers requiring immediate attention.

### Stalling Items Requiring Attention
• **Finance Validation Delays**: BCRS cost center mapping blocked awaiting Finance confirmation; similar pattern observed in SLO V2 migration timeline and vendor proposal validation. Systemic delay in cross-functional approvals creating deployment risks.
• **Documentation Gaps**: Project Light vendor sprint accelerating but spec documents incomplete; risk of rework if requirements misunderstood. Pattern suggests documentation often lagging behind implementation velocity.

### Upcoming Deadlines (Within 7 Days)
• **April 9th**: BCRS Express Delivery deployment deadline requiring cost center mapping fix resolution today
• **April 10th**: SLO V1 monitor muting must be completed tomorrow as part of migration timeline
• **End of Day April 7th**: Project Light RMN API specifications due; vendor sprint coordination requires immediate alignment
• **April 25th**: Agentic Evolution Contest deadline mentioned in calendar notifications

### Risks Not Flagged Above
• **UBID Tracking Integrity**: Critical data integrity issue affecting retail media tracking accuracy; if not resolved, could compromise revenue attribution and customer journey analysis across entire platform.
• **Production Incident Recurrence**: March 23rd GKE cluster capacity exhaustion caused Picker App outages; unresolved Redis CPU issues on Catalogue Service suggest similar risks remain for other services.
• **Vendor Dependency Concentration**: Heavy reliance on external vendors (Osmos, Comall, Huawei) with limited internal documentation of critical architectural decisions; risk of knowledge loss if vendor teams change or contracts interrupted.
• **Cost Optimization Blind Spots**: $3k+ monthly logging costs identified but no systematic approach to cost monitoring across all services; pattern suggests reactive rather than proactive cost governance.

### Positive Signals
• **Proactive Architecture Reviews**: Michael consistently challenging implementation details and identifying scope ambiguities before code implementation begins, reducing rework risk.
• **Cross-Functional Collaboration**: Active engagement with Finance, vendor teams, and engineering leaders demonstrating strong coordination skills across organizational boundaries.
• **Documentation Initiative**: Multiple threads showing commitment to creating technical specifications and architectural documentation despite time pressures and competing priorities.

---

**Report Generated:** April 7, 2026 at 17:25 SGT
**Data Sources:** Jira (56 tickets), Gmail (60 threads), Google Chat (71 conversations)
**Next Review:** Daily briefing tomorrow at same time unless urgent issues require immediate attention