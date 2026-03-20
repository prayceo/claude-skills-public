## Contents
- The Martech Operating Model
  - Who Owns Martech?
- Tool Lifecycle Management
  - The Tool Lifecycle
  - Phase 1: Evaluation
  - Phase 2: POC/Trial
  - Phase 3: Implementation
  - Phase 4: Adoption
  - Phase 5: Optimization
  - Phase 6: Renewal or Sunset
- The Quarterly Stack Audit
  - Audit Process
- Data Governance Framework
  - Event Tracking Governance
  - PII and Privacy Governance
  - Vendor Management Governance
- Team Structure and Skills
  - The Martech Team Skills Map
  - Hay's Hiring Philosophy
  - Career Development
- Applied to your product: Governance Playbook
  - Immediate Actions
  - Quarterly Cadence
  - Monthly Cadence

---
# Martech Governance and Operations

**Source framework:** Austin Hay's Mastering Marketing Technology course, supplemented by his writing and interviews on martech team structures, tool lifecycle management, vendor evaluation, and operating models for marketing technology.

---

## The Martech Operating Model

### Who Owns Martech?

The ownership question is one of the most consequential organizational decisions affecting marketing technology. Hay identifies four models:

**Model 1: Marketing-Owned**
The marketing team selects, implements, and manages all marketing tools.

| Pro | Con |
|-----|-----|
| Fast decision-making | Technical debt accumulates |
| Marketing needs are prioritized | Security/compliance gaps |
| Low organizational overhead | Integrations may be brittle |
| Direct accountability | Engineering may not support |

Best for: Small teams (<20 people), early-stage companies, marketing-heavy organizations.

**Model 2: Engineering-Owned**
Engineering implements and maintains all marketing technology.

| Pro | Con |
|-----|-----|
| Technical rigor | Marketing can't self-serve |
| Reliable integrations | Slow implementation cycles |
| Security and compliance | Marketing needs deprioritized |
| Scalable architecture | Engineers may not understand marketing needs |

Best for: Engineering-heavy organizations, companies with strict compliance requirements.

**Model 3: Dedicated Martech Team**
A cross-functional martech team bridges marketing and engineering.

| Pro | Con |
|-----|-----|
| Balanced perspective | Organizational overhead |
| Deep martech expertise | May become a bottleneck |
| Marketing self-service enabled | Requires specialized talent |
| Strategic technology planning | Can feel like a service team |

Best for: Mid-to-large companies (100+ employees), companies with complex martech stacks.

**Model 4: Marketing Ops Hybrid**
A marketing ops person or small team with engineering liaison.

| Pro | Con |
|-----|-----|
| Cost-effective | Dependent on one or two people |
| Understands both sides | Limited bandwidth |
| Can move fast | May lack deep engineering skills |
| Flexible | Knowledge concentration risk |

Best for: Growth-stage companies (50-200 employees), post-PMF but pre-enterprise.

**Recommended for your product:** Marketing Ops Hybrid. A marketing ops / growth engineer who understands both the marketing requirements and the technical implementation. This person is the bridge between growth marketing and engineering. They should be able to:
- Configure and manage the CDP (Segment)
- Build campaigns and audiences in Braze
- Write basic SQL for warehouse queries
- Manage vendor relationships and contracts
- Document the event taxonomy and data flows
- Train the marketing team on self-service tools

---

## Tool Lifecycle Management

### The Tool Lifecycle

Every martech tool goes through a predictable lifecycle:

```
EVALUATION --> POC/TRIAL --> IMPLEMENTATION --> ADOPTION --> OPTIMIZATION --> RENEWAL/SUNSET
```

### Phase 1: Evaluation

**When to evaluate a new tool:**
- A capability gap exists that no current tool can fill
- A current tool is failing (performance, cost, support)
- The team has outgrown a tool's capabilities
- A significantly better option has emerged

**When NOT to evaluate a new tool:**
- A vendor sales rep reached out with a compelling pitch
- A competitor uses something different
- One team member saw something at a conference
- The current tool works but someone wants something "better"

**The Evaluation Process:**

Step 1: Define requirements
- Must-have capabilities (deal-breakers if missing)
- Nice-to-have capabilities (differentiate between options)
- Integration requirements (what must it connect to?)
- Budget constraints (all-in: license + implementation + training + maintenance)

Step 2: Market scan
- Identify 3-5 candidates (no more)
- Eliminate any that don't meet must-have requirements
- Request pricing from remaining candidates

Step 3: Vendor evaluation

**The RICE Score for Martech:**

| Criterion | Question | Weight |
|-----------|----------|--------|
| Reach | How many campaigns/use cases will this tool enable? | 25% |
| Impact | How much will it improve key metrics? | 30% |
| Confidence | How certain are we this works? (References, POC results) | 20% |
| Effort | Implementation effort (engineering time, migration, training) | 25% |

Step 4: Reference checks
- Talk to 2-3 companies at similar stage/scale
- Ask about implementation experience, not just feature quality
- Ask about support responsiveness and roadmap reliability
- Ask about hidden costs (overage fees, professional services)

### Phase 2: POC/Trial

**POC design:**
- Duration: 2-4 weeks
- Scope: Test the 2-3 most critical use cases
- Success criteria: Defined before the POC begins
- Team: Dedicated evaluator (not a side project)

**POC evaluation checklist:**
- [ ] Does it meet the must-have requirements in practice (not just in demos)?
- [ ] Is the integration with our stack straightforward?
- [ ] Can marketing self-serve for day-to-day operations?
- [ ] Is the data quality and latency acceptable?
- [ ] Does the vendor's support meet our needs?
- [ ] Is the UI/UX acceptable for our team?
- [ ] Are there any surprise limitations?

### Phase 3: Implementation

**Implementation planning:**
1. Define the implementation scope (full rollout or phased?)
2. Assign an owner (who is responsible for making this work?)
3. Set a timeline with milestones
4. Plan data migration if replacing an existing tool
5. Plan training for end users
6. Define success metrics for the first 90 days

**Implementation best practices:**
- Run new and old tools in parallel during migration
- Validate data parity between old and new
- Don't sunset the old tool until the new one is proven in production
- Document everything (configuration, integrations, processes)

### Phase 4: Adoption

**Measuring adoption:**
- Active users: How many team members use the tool weekly?
- Use case coverage: What % of planned use cases are actually being used?
- Self-service rate: What % of tasks can marketing do without engineering help?

**Driving adoption:**
- Training: Hands-on workshops, not just documentation
- Champions: Identify 1-2 power users who can help others
- Quick wins: Show early results to build momentum
- Remove barriers: If the tool is hard to use, address the UX issues

### Phase 5: Optimization

**Quarterly tool optimization review:**
- Are we using all the features we're paying for?
- Are there new features that could add value?
- Is the team proficient, or do they need more training?
- Is the tool performing as expected (speed, reliability, accuracy)?
- Is the cost still justified relative to the value delivered?

### Phase 6: Renewal or Sunset

**Renewal evaluation (60-90 days before contract expiration):**
- Is the tool still the best option for our needs?
- Has the competitive landscape changed?
- Is the pricing still competitive?
- Are there consolidation opportunities (could another tool absorb this function)?

**Sunset criteria:**
1. LTV:Cost ratio below 1.5:1 (the tool costs more than it delivers)
2. Active users below 2 (only one person uses it)
3. Use case coverage below 30% (we're paying for features we don't use)
4. A superior alternative exists at lower total cost
5. The tool has been replaced by a capability in another tool

---

## The Quarterly Stack Audit

### Audit Process

**Step 1: Inventory (Week 1)**

Create a complete inventory of every marketing tool:

| Tool | Category | Annual Cost | Primary Owner | Active Users | Key Integrations |
|------|----------|-------------|---------------|-------------|-----------------|
| Segment | CDP | $XX,000 | Marketing Ops | 5 | Braze, Amplitude, Snowflake |
| Braze | Campaign | $XX,000 | Growth Marketing | 8 | Segment, Snowflake |
| Amplitude | Analytics | $XX,000 | Product + Marketing | 15 | Segment |
| AppsFlyer | Attribution | $XX,000 | Growth Marketing | 3 | Segment, ad platforms |
| Snowflake | Warehouse | $XX,000 | Data/Engineering | 10 | Segment, Hightouch, Looker |

Include informal/free tools: Google Sheets for audience lists, Canva for creative, etc.

**Step 2: Usage Assessment (Week 2)**

For each tool, measure:
- Monthly active users (unique team members who logged in)
- Key actions taken (campaigns sent, queries run, segments created)
- Events processed / data volume
- Support tickets filed

**Step 3: Overlap Analysis (Week 2)**

Map capabilities across tools:

| Capability | Tool 1 | Tool 2 | Tool 3 | Owner |
|-----------|--------|--------|--------|-------|
| Event collection | Segment | Braze (native SDK) | - | Segment |
| User segmentation | Segment | Braze | Amplitude | Braze |
| Push notifications | Braze | OneSignal (legacy?) | - | Braze |
| Email | Braze | Mailchimp (legacy?) | - | Braze |
| Analytics | Amplitude | Braze (basic) | Looker | Amplitude |

Flag any capability served by more than one tool. For each overlap, decide: consolidate to one tool or explicitly designate one as primary.

**Step 4: Gap Analysis (Week 3)**

Identify missing capabilities:

| Capability Needed | Current Workaround | Priority | Candidate Solutions |
|------------------|-------------------|----------|-------------------|
| Send-time optimization | Manual scheduling | Medium | Braze AI (built-in) |
| Churn prediction | No prediction | High | Internal model + Hightouch |
| Dynamic content personalization | Segment-based variants | Medium | Braze connected content |
| A/B testing on push | Limited to 2 variants | Low | Braze multivariate |

**Step 5: Rationalize (Week 3-4)**

Produce recommendations:
- Tools to consolidate (migrate capabilities to one tool)
- Tools to sunset (no longer needed or underutilized)
- Tools to upgrade (current tool is a bottleneck)
- New tools to evaluate (address critical gaps)
- Budget impact (net cost change from recommended actions)

---

## Data Governance Framework

### Event Tracking Governance

**The Event Tracking Approval Process:**

```
New event requested
    --> Marketing/Product defines: What action does this represent?
    --> Martech owner reviews: Does it follow naming conventions? Is it needed?
    --> Schema documented: Event name, properties, types, descriptions
    --> Engineering implements: Using approved schema
    --> Martech validates: Event fires correctly with all properties
    --> Production: Event is live and documented in the tracking plan
```

**Event Naming Rules:**
1. Object Action format (e.g., "Engagement Session Completed")
2. Use English, capitalize each word
3. No abbreviations (use "Subscription" not "Sub")
4. No platform-specific names (use "Content Shared" not "iOS Share Sheet Opened")
5. Verbs in past tense (Viewed, Started, Completed, Created)

**Event Property Rules:**
1. Use snake_case for property names
2. Include data type in documentation (string, integer, boolean, array)
3. Required properties must be validated before sending
4. Null handling: Use null for missing values, not empty strings
5. Enums: Define allowed values for categorical properties

### PII and Privacy Governance

**PII Classification:**

| Category | Examples | Handling |
|----------|---------|---------|
| Direct PII | Email, name, phone, address | Encrypt in transit and at rest; limit tool access |
| Indirect PII | Device ID, IP address | Anonymize where possible; time-limited retention |
| Sensitive PII | Payment info, health data | Never store in martech tools; keep in secure systems only |
| Behavioral Data | App usage, content preferences | Pseudonymize; comply with consent requirements |

**Privacy-by-Default Rules:**
1. Only send PII to tools that need it (Braze needs email for messaging; Amplitude does not)
2. Use hashed identifiers where possible (send hashed email to ad platforms, not raw email)
3. Implement consent management: track consent status as a user property
4. Honor data deletion requests across all tools (GDPR/CCPA right to erasure)
5. Audit PII access quarterly: which tools have access? Is it still justified?

**your product specific considerations:**
- Engagement requests may contain sensitive personal information
- Engagement content should never be used for ad targeting or shared with ad platforms
- User's religious affiliation and practice data requires careful handling
- Group engagement data must respect privacy of all group members

### Vendor Management Governance

**Vendor Access Control:**
- Each tool has a designated admin (usually martech owner)
- Access is role-based (admin, editor, viewer)
- Quarterly access review: Remove access for departed employees
- SSO enforced where possible
- Vendor contracts reviewed annually for compliance with data policies

**Vendor Performance SLAs:**
Monitor and hold vendors accountable for:
- Uptime (target: 99.9%)
- Data latency (real-time tools: <5 seconds; batch tools: <1 hour)
- Support response time (P1 issues: <1 hour; P2: <4 hours)
- Data accuracy (event delivery rate: >99%)

---

## Team Structure and Skills

### The Martech Team Skills Map

| Skill | Description | Where to Find |
|-------|-----------|--------------|
| Tool configuration | Set up and manage CDPs, campaign tools, analytics | Marketing Ops / Martech specialist |
| Data architecture | Design event taxonomies, data flows, schemas | Marketing Ops + Data Engineering |
| SQL and analytics | Query warehouse, build segments, analyze data | Marketing Ops / Analytics |
| Campaign execution | Build and manage campaigns, A/B tests | Growth Marketing |
| Integration management | Configure and maintain tool-to-tool integrations | Marketing Ops + Engineering |
| Vendor management | Evaluate, negotiate, and manage vendor relationships | Marketing Ops / Marketing leadership |
| Privacy and compliance | Ensure data handling meets legal requirements | Marketing Ops + Legal |

### Hay's Hiring Philosophy

Hay looks for two key traits when hiring martech talent:

1. **Intellectual curiosity** -- The martech landscape changes constantly. You need people who genuinely enjoy learning new tools and approaches, not people who just want to operate existing ones.

2. **Scrappiness in engineering** -- Martech sits at the intersection of marketing and engineering. The best martech people can write basic code, troubleshoot integrations, and think in systems -- even if they're not formal engineers.

### Career Development

For the martech team at your company:

**Junior (0-2 years):** Campaign operations, basic segmentation, event tracking QA, tool administration
**Mid (2-5 years):** Data architecture, advanced segmentation, integration management, vendor evaluation
**Senior (5+ years):** Stack strategy, team leadership, cross-functional partnership with engineering and data, vendor negotiation

---

## Applied to your product: Governance Playbook

### Immediate Actions

1. **Document the current stack.** List every tool, its cost, its owner, and its integrations.
2. **Establish the event taxonomy.** Define naming conventions and property standards. Document every event.
3. **Assign a martech owner.** One person responsible for the stack -- ideally a Marketing Ops / growth engineer hybrid.
4. **Set up data quality monitoring.** Alert on event volume anomalies, integration failures, and property completeness drops.
5. **Create a vendor calendar.** Track every contract renewal date, at least 90 days in advance.

### Quarterly Cadence

| Quarter | Activity |
|---------|----------|
| Q1 | Full stack audit + annual budget planning |
| Q2 | Focus on gap analysis and tool evaluation |
| Q3 | Focus on optimization and adoption measurement |
| Q4 | Renewal negotiation and next-year planning |

### Monthly Cadence

| Week | Activity |
|------|----------|
| Week 1 | Data quality check (event volumes, property completeness) |
| Week 2 | Integration health check (all connections active?) |
| Week 3 | Usage review (who's using what? Any underutilized tools?) |
| Week 4 | Team feedback collection (what's working? What's painful?) |
