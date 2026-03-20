## Contents
- The Martech Maturity Model
- The Capability-First Framework
- Common Martech Anti-Patterns
- Stack Architecture Fundamentals
  - The Four Core Data Components
  - The Hub-and-Spoke Architecture
- Stack Design by Company Stage
  - Stage 1: Pre-Product-Market Fit (0-50K users)
  - Stage 2: Post-PMF, Pre-Scale (50K-500K users)
  - Stage 3: Growth Stage (500K-5M users)
  - Stage 4: Scale (5M+ users)
- The Build vs. Buy Framework
  - The Decision Matrix
  - The Decision Rule
- Stack Evaluation Principles
  - Principle 1: Redundancy Awareness
  - Principle 2: Coupling Assessment
  - Principle 3: Future-State Design
- The Golden Stacks
  - Golden B2C Stack (Consumer Subscription App)
  - Golden B2B Stack
- Stack Migration and Evolution
  - When to Migrate a Tool
  - Migration Planning
  - The Migration Risk Matrix
- Marketing Automation and Personalization Infrastructure
  - The Marketing Automation Maturity Ladder
  - Campaign Architecture for your product
  - Personalization Infrastructure
  - Cross-Channel Orchestration
- Applied to your product: Stack Recommendation

---
# Martech Stack Architecture

**Source framework:** Austin Hay's Mastering Marketing Technology course, supplemented by his Lenny's Podcast interview "The Ultimate Guide to Martech," his Hightouch interview on the evolution of martech, and his writing on stack architecture, build vs. buy, and the four core data components.

---

## The Martech Maturity Model

Companies progress through predictable stages of martech sophistication:

**Stage 1: Ad Hoc (0-1)**
- Tools adopted reactively, one at a time, by individual teams
- No central architecture or data strategy
- Marketing data lives in silos (email tool, analytics tool, ad platform)
- Typical company: Pre-Series A or early startup
- your product signal: "I have to export a CSV from one tool and upload it to another"

**Stage 2: Connected (1-2)**
- Point-to-point integrations between key tools
- Basic event tracking implemented (analytics + email at minimum)
- Some data standardization (e.g., consistent user IDs across tools)
- Marketing can run basic automated campaigns
- your product signal: "We have Segment/mParticle connecting a few tools"

**Stage 3: Integrated (2-3)**
- Central data layer (CDP or data warehouse) serves as source of truth
- Event taxonomy is documented and governed
- Marketing team can self-serve most campaigns without engineering
- Cross-channel orchestration is possible (coordinate email + push + in-app)
- your product signal: "We can build segments and trigger campaigns across channels"

**Stage 4: Intelligent (3-4)**
- Real-time data activation across all channels
- ML-driven personalization (content recommendations, send-time optimization)
- Automated testing and optimization infrastructure
- Marketing experimentation is self-serve
- your product signal: "We personalize engagement session recommendations based on user behavior and preferences"

**Stage 5: Predictive (4-5)**
- Predictive models drive proactive marketing (churn prediction, LTV scoring)
- Marketing and product data are fully unified
- Marketing tech enables new product experiences (not just messaging)
- The stack is a competitive advantage
- your product signal: "Our martech predicts when a subscriber is at risk and automatically adjusts their experience"

---

## The Capability-First Framework

Instead of asking "What tools do we need?", ask "What capabilities do we need?"

**Step 1: List your marketing capabilities needed**
```
Example for your product:
1. Track user behavior across app and web (event collection)
2. Send personalized push notifications (messaging)
3. Segment users by behavior, subscription status, content preferences (segmentation)
4. Trigger automated campaigns based on user actions (automation)
5. Personalize content recommendations (personalization)
6. Attribute conversions to marketing channels (attribution)
7. Run A/B tests on messaging and content (experimentation)
8. Manage subscription lifecycle communications (lifecycle)
```

**Step 2: Map capabilities to data requirements**
```
Capability -> Data Needed -> Data Source
Personalized push -> User preferences, behavior history -> CDP + app events
Churn prevention -> Usage patterns, payment status -> CDP + billing system
Content recs -> Content consumption history -> CDP + content metadata
Attribution -> Install source, campaign data -> MMP + ad platforms
```

**Step 3: Select the minimum tools that deliver all capabilities**
- Eliminate redundancy: If your CDP can do segmentation, you don't need a separate segmentation tool
- Prioritize tools that serve multiple capabilities
- Prefer tools with native integrations to your existing stack

---

## Common Martech Anti-Patterns

**Anti-pattern 1: Tool Hoarding**
- Symptom: 20+ marketing tools, most underutilized
- Root cause: Each new need -> new tool purchase, no consolidation review
- Fix: Annual stack audit -- every tool must justify its existence with usage data

**Anti-pattern 2: The Frankenstein Stack**
- Symptom: Brittle point-to-point integrations that break constantly
- Root cause: No central data layer; tools connected directly to each other
- Fix: Implement a CDP or data warehouse as central hub; route all data through it

**Anti-pattern 3: Engineering Bottleneck**
- Symptom: Every marketing campaign requires engineering support
- Root cause: Tools configured for developers, not marketers
- Fix: Invest in tools with marketer-friendly interfaces; build self-serve templates

**Anti-pattern 4: Data Drift**
- Symptom: Same metric shows different numbers in different tools
- Root cause: No single source of truth; event definitions not standardized
- Fix: Establish event taxonomy, designate source of truth for each metric, run regular audits

---

## Stack Architecture Fundamentals

Austin Hay approaches martech stack architecture as a systems design problem. The key insight: most companies think about martech as a collection of tools. Hay thinks about it as a data architecture with tools plugged into it.

> A martech professional is "a product manager whose specific role and focus is the system or the third-party or first-party platform."

### The Four Core Data Components

Hay's framework for understanding any martech stack breaks it down into four core data components:

**1. Inputs (Data Collection)**
Where we get data about our customers from. This includes event tracking SDKs, form submissions, CRM entries, third-party data enrichment, and import pipelines.

- Tools: Segment, mParticle, RudderStack, GTM, native SDKs
- your product inputs: iOS/Android app events, website events, payment system events, customer support data

**2. Storage (Data Persistence)**
Where we keep our customer data. This is the central nervous system of the stack -- the source of truth for customer profiles, behaviors, and derived attributes.

- Tools: Snowflake, BigQuery, Redshift, CDP profile stores
- your product storage: Data warehouse (Snowflake/BigQuery) for historical analysis + CDP for real-time profiles

**3. Capabilities (Processing and Enrichment)**
Tools that enrich, analyze, or transform our data. Analytics platforms, ML models, identity resolution, segmentation engines.

- Tools: Amplitude, Mixpanel, Looker, dbt, ML platforms
- your product capabilities: Product analytics (Amplitude), BI/reporting (Looker/Mode), content recommendation engine

**4. Federation (Data Distribution)**
How data gets moved between the other components. This is the plumbing that connects inputs to storage, storage to capabilities, and everything to activation destinations.

- Tools: Hightouch, Census (reverse ETL), native CDP routing, API integrations, Fivetran/Airbyte
- your product federation: CDP event routing to campaign tools + reverse ETL from warehouse to ad platforms

### The Hub-and-Spoke Architecture

The fundamental architecture principle: all data flows through a central hub (CDP or warehouse). No direct tool-to-tool integrations.

```
                  ┌─────────────────────┐
                  │     DATA SOURCES     │
                  │  (App, Web, Server)  │
                  └──────────┬──────────┘
                             │
                      ┌──────▼──────┐
                      │   CENTRAL   │
                      │     HUB     │
                      │ (CDP and/or │
                      │  Warehouse) │
                      └──────┬──────┘
              ┌──────────────┼──────────────┐
              │              │              │
     ┌────────▼─────┐  ┌────▼─────┐  ┌─────▼───────┐
     │  ACTIVATION  │  │ ANALYSIS │  │  ENRICHMENT │
     │   Campaign   │  │ Analytics│  │  Identity   │
     │   Ads        │  │ BI       │  │  ML Models  │
     │   CRM        │  │ Reporting│  │  Scoring    │
     └──────────────┘  └──────────┘  └─────────────┘
```

**Why hub-and-spoke:**
1. **Resilience:** If you replace any single tool, only one integration changes
2. **Data consistency:** Every tool receives the same data from the same source
3. **Scalability:** Adding a new destination is one integration, not N
4. **Governance:** You can control and audit data flow from a central point

**Anti-pattern: Mesh architecture**
When tools are connected directly to each other (email tool pulls from analytics, analytics pulls from CRM, CRM pulls from app), you get an unmaintainable web of integrations. Changing any one tool requires updating multiple integrations, and data consistency degrades.

---

## Stack Design by Company Stage

### Stage 1: Pre-Product-Market Fit (0-50K users)

**Philosophy:** Minimal viable stack. Don't invest in infrastructure until you have product-market fit.

**Recommended stack:**
- Analytics: Amplitude free tier or Mixpanel
- Email/Push: Customer.io or OneSignal
- Attribution: Branch or AppsFlyer free tier
- No CDP needed yet (direct SDK integrations are fine)

**your product equivalent:** If your product were pre-PMF, a simple setup with native analytics + one messaging tool would suffice.

### Stage 2: Post-PMF, Pre-Scale (50K-500K users)

**Philosophy:** Build the data foundation. This is when a CDP becomes valuable and event taxonomy matters.

**Recommended stack:**
- CDP: Segment or mParticle (event collection + routing)
- Campaign: Braze or Iterable (lifecycle messaging)
- Analytics: Amplitude or Mixpanel
- Attribution: AppsFlyer or Branch
- Data warehouse: Snowflake or BigQuery (start sending CDP data here)

**Key investment:** Event taxonomy design. Get this right now or pay for it forever.

### Stage 3: Growth Stage (500K-5M users)

**Philosophy:** Optimize and personalize. Add capabilities that drive efficiency and personalization.

**Recommended stack (additions):**
- Reverse ETL: Hightouch or Census (activate warehouse data)
- Experimentation: LaunchDarkly or internal A/B testing
- Content personalization: Internal recommendation engine or vendor
- BI: Looker, Mode, or equivalent

**Key investment:** Marketing self-service. The growth marketing team should be able to build segments, trigger campaigns, and analyze results without engineering support for routine tasks.

### Stage 4: Scale (5M+ users)

**Philosophy:** Automate and predict. ML-driven personalization, automated optimization, predictive models.

**Recommended stack (additions):**
- ML platform: Internal models for content recommendation, churn prediction, send-time optimization
- Feature store: Serve ML features to campaign tools in real-time
- Advanced segmentation: Real-time behavioral triggers
- Automated testing: Multi-armed bandit for campaign optimization

---

## The Build vs. Buy Framework

Hay emphasizes a structured approach to build vs. buy decisions:

### The Decision Matrix

| Factor | Build (Custom) | Buy (Vendor) |
|--------|---------------|--------------|
| Speed to value | Slow (months) | Fast (weeks) |
| Customization | Unlimited | Constrained |
| Maintenance cost | High (ongoing engineering) | Included in license |
| Data control | Full | Depends on vendor |
| Switching cost | Low (you own it) | High (vendor lock-in) |
| Talent required | Engineering | Marketing ops |
| Best when | Core competitive advantage | Commodity capability |

### The Decision Rule

**Build when:**
1. The capability is a core competitive differentiator
2. No vendor solution exists that meets your needs
3. You have the engineering talent to build AND maintain
4. The total cost of building (including opportunity cost) is less than 3 years of vendor fees
5. Data sensitivity requires full in-house control

**Buy when:**
1. The capability is commodity (everyone needs it, solutions exist)
2. Speed to market matters more than customization
3. The vendor's R&D exceeds what you could invest internally
4. You don't have specialized engineering talent for this domain
5. The vendor's integration ecosystem adds value beyond the core tool

**your product build vs. buy examples:**

| Capability | Decision | Rationale |
|-----------|----------|-----------|
| Event collection (CDP) | BUY (Segment/mParticle) | Commodity; vendor integration libraries save months |
| Lifecycle messaging (push/email) | BUY (Braze/Iterable) | Commodity; vendor deliverability and templates are superior |
| Product analytics | BUY (Amplitude/Mixpanel) | Commodity; building analytics from scratch is years of work |
| Mobile attribution | BUY (AppsFlyer/Branch) | Commodity; requires partnerships with ad networks |
| Engagement Session recommendation engine | BUILD | Core differentiator; category-specific personalization requires domain knowledge |
| Engagement group matching | BUILD | Unique to your product; no vendor solution exists |
| Data warehouse | BUY (Snowflake/BigQuery) | Commodity; cloud providers do this better than you can |
| Churn prediction model | BUILD (on bought infrastructure) | Use vendor ML tools but build your product-specific models |

---

## Stack Evaluation Principles

### Principle 1: Redundancy Awareness

Hay identifies redundancy as a key concern: multiple vendors in the stack often offer similar functions. This creates waste (paying for the same capability twice) and confusion (which tool is the source of truth?).

**Audit for redundancy:**
- List every capability in your stack
- Map which tools provide each capability
- Identify overlaps (e.g., both CDP and campaign tool do segmentation)
- Decide which tool is the "owner" for each capability
- Either sunset the redundant tool or clearly delineate ownership

### Principle 2: Coupling Assessment

Coupling measures the dependency between vendors/systems. Tightly coupled systems are harder to change.

**Assess coupling for each tool:**
- How many other tools depend on this tool's data?
- If we replaced this tool, how many integrations would break?
- Does this tool store data that no other system has?
- Can we export our data from this tool?

**Minimize coupling by:**
- Routing all data through the central hub (CDP/warehouse)
- Avoiding tool-to-tool direct integrations
- Ensuring all tools can export data in standard formats
- Maintaining documentation of all integration dependencies

### Principle 3: Future-State Design

Hay emphasizes always thinking about the future when building systems. His approach: design systems that preserve the future state in a minimally invasive way.

**Practical application:**
- When implementing event tracking, include properties you'll need later (even if no tool uses them yet)
- When selecting a CDP, choose one that supports real-time AND batch (even if you only need batch today)
- When building the data warehouse schema, design for the analytics questions you'll ask in 12 months
- When choosing a campaign tool, ensure it supports ML-driven personalization (even if you're doing batch sends today)

---

## The Golden Stacks

Hay recommends specific tool combinations based on company type:

### Golden B2C Stack (Consumer Subscription App)

This is the most relevant for your product:

| Layer | Tool | Role |
|-------|------|------|
| CDP/Event Collection | Segment or mParticle | Collect events, route to destinations |
| Campaign Platform | Braze or Iterable | Push, email, in-app messaging |
| Product Analytics | Amplitude | User behavior analysis, funnel optimization |
| Data Warehouse | Snowflake or BigQuery | Historical data storage, ad hoc analysis |
| Reverse ETL | Hightouch | Activate warehouse data to ad platforms, CRM |
| Mobile Attribution | AppsFlyer | Acquisition source tracking |

**Data flow:**
```
App events --> Segment/mParticle --> Braze (campaigns)
                                  --> Amplitude (analytics)
                                  --> Snowflake (warehouse)
                                       --> Hightouch --> Ad platforms
                                       --> Hightouch --> Braze (enriched segments)
                                       --> Looker (BI dashboards)
```

### Golden B2B Stack

| Layer | Tool | Role |
|-------|------|------|
| CRM | Salesforce | Central customer record |
| Marketing Automation | Marketo or HubSpot | Email, lead scoring, nurture |
| CDP | Segment | Event collection, identity |
| Analytics | Amplitude | Product analytics |
| Attribution | Branch | Multi-touch attribution |
| Reverse ETL | Hightouch | Warehouse to Salesforce/Marketo |

---

## Stack Migration and Evolution

### When to Migrate a Tool

**Strong signals:**
- The tool can't scale with your user growth (hitting volume limits)
- The tool lacks a critical capability you need and won't build it
- The vendor's pricing model becomes unsustainable at your scale
- The tool's integration ecosystem doesn't cover your needs
- Support and reliability have degraded significantly

**Weak signals (don't migrate for these alone):**
- A shinier tool exists
- A competitor uses something different
- The sales team from a competitor tool is persistent
- One team member prefers a different tool

### Migration Planning

1. **Document current state:** Every integration, data flow, and dependency
2. **Define requirements:** What must the new tool do? What's nice-to-have?
3. **Evaluate candidates:** Score against requirements (not demo quality)
4. **Run parallel:** Operate both tools simultaneously during migration
5. **Migrate in phases:** Move one integration at a time, validate each before proceeding
6. **Decommission:** Only sunset the old tool after all integrations are migrated and validated

### The Migration Risk Matrix

| Risk | Mitigation |
|------|-----------|
| Data loss during migration | Run parallel tracking, verify data parity |
| Integration breaks | Migrate one integration at a time, validate each |
| Team disruption | Train the team on the new tool before migration |
| Historical data loss | Ensure historical data is preserved in the warehouse |
| Vendor lock-in with new tool | Verify data export capabilities before committing |

---

## Marketing Automation and Personalization Infrastructure

### The Marketing Automation Maturity Ladder

**Level 1: Batch Campaigns**
- Manually scheduled email/push sends to static lists
- "Send this engagement session recommendation to all premium subscribers"
- Low effort, low personalization, low impact

**Level 2: Triggered Campaigns**
- Event-based triggers fire messages automatically
- "When a user completes their 7th engagement session, send a premium trial offer"
- Medium effort, medium personalization, high impact

**Level 3: Lifecycle Journeys**
- Multi-step, branching campaigns that adapt based on user behavior
- "New user journey: Day 1 welcome -> Day 2 content rec -> Day 3 (if engaged: deeper content; if not: re-engagement) -> Day 7 trial offer"
- High effort to build, high personalization, highest impact

**Level 4: Dynamic Personalization**
- Content, timing, and channel dynamically selected per user
- "ML model selects the best engagement session to recommend, the best channel to reach them, and the best time to send"
- Highest effort, maximum personalization

### Campaign Architecture for your product

**Critical Lifecycle Campaigns:**

| Campaign | Trigger | Channel | Goal |
|----------|---------|---------|------|
| Welcome Series | App install + activation | Push + email | Establish daily habit |
| Trial Nudge | Trial day 3 | Push + in-app | Demonstrate premium value |
| Trial Expiring | Trial day 6 | Push + email | Convert to paid |
| Subscription Confirmed | Subscription started | Email | Validate decision, set expectations |
| Engagement Drop | No app open in 3 days | Push | Re-engage before habit breaks |
| Content Milestone | 30/60/90 engagement sessions completed | In-app + push | Celebrate and deepen engagement |
| Renewal Approaching | 30 days before annual renewal | Email + in-app | Reinforce value before renewal |
| Payment Failed | Billing failure | Push + email | Recover involuntary churn |
| Win-Back | 30 days post-churn | Email | Re-acquire churned subscribers |
| Seasonal | seasonal event, seasonal campaign, Advent, New Year | All channels | Drive engagement spikes |

### Personalization Infrastructure

**Personalization Layers:**

**Layer 1: Segment-based (easiest)**
- Define user segments based on attributes and behavior
- Serve different content/messaging to each segment
- Example: "Free users see engagement session previews; premium users see full library"
- Infrastructure needed: CDP segmentation + campaign tool

**Layer 2: Rule-based (medium)**
- If/then logic customizes specific elements
- Example: "If user's preferred content type is audio, lead with audio engagement sessions in push"
- Infrastructure needed: CDP properties + campaign tool dynamic content

**Layer 3: ML-driven (hardest, highest value)**
- Models predict best content, timing, channel per user
- Example: "Recommendation engine selects today's engagement session based on past consumption"
- Infrastructure needed: ML infrastructure, feature store, real-time serving

**Personalization Priority for your product:**
1. Content type personalization (audio vs. text vs. video engagement sessions) -- Layer 2
2. Send-time optimization (when to push based on user open patterns) -- Layer 3
3. Content recommendation (which engagement session to surface) -- Layer 3
4. Channel preference (push vs. email vs. in-app) -- Layer 2
5. Paywall personalization (messaging variant by user segment) -- Layer 1

### Cross-Channel Orchestration

**Channel Selection Framework:**
```
Priority 1: In-app message (if user is in the app right now)
  -> Highest engagement, zero marginal cost, contextually relevant

Priority 2: Push notification (if user is opted in)
  -> High visibility, real-time, but notification fatigue risk

Priority 3: Email (for longer content, lower urgency)
  -> Rich content, user controls timing, lower open rates

Priority 4: SMS (for critical/transactional only)
  -> Highest open rate, but highest irritation risk and cost
```

**Frequency Capping:**
- Push: Max 1-2/day for consumer app (core notification + 1 optional)
- Email: Max 3-4/week (2 content + 1-2 lifecycle)
- In-app: No hard cap, but contextual relevance required
- SMS: Only transactional (payment issues, account security)

**Anti-patterns:**
- Sending the same message on every channel simultaneously ("carpet bombing")
- No global frequency cap across channels (user gets push + email + in-app for same event)
- Treating all users the same regardless of channel preferences and engagement

---

## Applied to your product: Stack Recommendation

**Current likely state:** Stage 2-3 (Post-PMF, scaling)

**Recommended immediate stack:**
1. **Segment** as CDP (event collection + routing)
2. **Braze** as campaign platform (push, email, in-app -- strong mobile-first architecture, popular with subscription apps)
3. **Amplitude** for product analytics
4. **AppsFlyer** for mobile attribution
5. **Snowflake** or BigQuery as data warehouse

**Near-term additions (6-12 months):**
6. **Hightouch** for reverse ETL (activate warehouse segments to Braze and ad platforms)
7. **dbt** for data transformation in the warehouse

**Longer-term investments (12-24 months):**
8. Internal recommendation engine for engagement session personalization
9. Churn prediction model (built on warehouse data, served via Braze connected content)
10. Send-time optimization (either Braze native or custom model)
