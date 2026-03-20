---
name: martech
description: Applies Austin Hay's Mastering Marketing Technology frameworks to build resilient, powerful, flexible martech systems. Covers CDP architecture, data infrastructure design, martech stack strategy, tool evaluation, vendor selection, and marketing data governance. Activates when making decisions about your product's marketing technology stack, evaluating CDPs or new marketing tools, designing event tracking and data pipelines, integrating marketing platforms, managing marketing data quality, or building the infrastructure that enables personalization, automation, and attribution. Triggers when asked about martech, CDPs, marketing automation, Segment, mParticle, data pipelines, marketing tool evaluation, or when someone says "our tools don't talk to each other" or "we need a CDP."
---

**Reference files:**
- `references/martech-stack-architecture.md` -- Maturity model, capability-first framework, anti-patterns, four core data components, hub-and-spoke architecture, stack design by stage, build vs buy, golden stacks, marketing automation maturity, campaign architecture, personalization layers, cross-channel orchestration
- `references/cdp-and-data-infrastructure.md` -- CDP selection, implementation, event taxonomy design, event categories for your product, data pipeline architecture, identity resolution, data quality monitoring
- `references/martech-governance-and-ops.md` -- Marketing data governance, tool lifecycle management, stack audit process, PII/privacy governance, martech team operating models and skills

---

## How to Use This Skill

When this skill activates:
1. Identify which martech and data infrastructure framework from this skill best applies to the question
2. Apply the relevant decision tree from the Decision Tools section
3. Ground all recommendations in the context of your product
4. Cite the specific framework and Austin Hay's methodology when making claims
5. If deeper detail is needed, read the relevant reference file before responding

## Gotchas

Common mistakes to avoid when applying these frameworks:

1. **Don't recommend tools before defining capabilities needed:** Austin Hay's Capability-First Framework exists because most martech failures come from buying tools and then looking for problems to solve. Always start with "what capability is missing?" not "which tool should we buy?"
2. **Don't recommend Stage 4 solutions for a Stage 2 company:** ML-driven personalization, real-time data activation, and predictive churn models require mature event tracking and clean data foundations. Recommending advanced capabilities before the event taxonomy and CDP are solid creates technical debt and wasted spend.
3. **Don't allow direct tool-to-tool integrations:** Hay's hub-and-spoke architecture routes all data through a central hub (CDP). Recommending direct integrations between marketing tools (e.g., Meta directly to email platform) creates the Frankenstein Stack anti-pattern -- brittle, hard to audit, and impossible to scale.
4. **Don't skip the event taxonomy for your product:** Every downstream capability -- lifecycle campaigns, personalization, attribution, churn prediction -- depends on clean, consistent event data. Recommending any new tool or campaign automation before auditing whether events like "Engagement Session Completed" and "Subscription Started" are properly tracked is putting the cart before the horse.

## Example

**User asks:** "Our marketing team wants to buy Braze for push notifications and email. Should we go ahead?"

**Approach:**
1. Apply Decision 2 (Which Martech Tool Should We Buy?) -- first determine whether lifecycle messaging is a core differentiator (likely no, so buy not build) and check if Braze integrates natively with your product's existing CDP/stack
2. Assess current maturity stage using the Maturity Model -- if your product is at Stage 2 without clean event tracking, implementing Braze will underperform because the data feeding it is incomplete or inconsistent
3. Apply the Capability-First Framework -- confirm that the real need is campaign orchestration (not just a push notification tool), and verify that the event taxonomy supports the lifecycle triggers Braze would need (onboarding steps, trial events, content engagement, churn signals)
4. Output a recommendation: either proceed with Braze evaluation (with a vendor checklist and POC plan) or sequence it after foundational data work, with specific prerequisites to complete first

---

## Hay's Core Philosophy

Most companies approach martech backwards -- starting with tools instead of capabilities. This tools-first approach produces a Frankenstein stack: overlapping tools with brittle integrations, inconsistent data, and a marketing team that cannot execute without engineering. The alternative is a systems-first approach: define capabilities needed, map data flows, then select the minimum set of tools that deliver those capabilities reliably. The goal is a resilient stack that compounds in value as the business grows.

---

## Module 1: Martech Strategy Foundations

Companies progress through five maturity stages: Ad Hoc (silos, CSV exports), Connected (point-to-point integrations), Integrated (central data layer, self-serve campaigns), Intelligent (real-time activation, ML personalization), and Predictive (proactive churn prediction, marketing as competitive advantage). Use the Capability-First Framework: list capabilities needed, map to data requirements, select minimum tools. Build only core differentiators (your product's recommendation engine); buy commodity capabilities (CDP, campaign tools, analytics). Watch for anti-patterns: Tool Hoarding, Frankenstein Stack, Engineering Bottleneck, and Data Drift.

*-> Full detail (maturity model stages, capability mapping, build vs buy matrix, anti-patterns): `references/martech-stack-architecture.md`*

---

## Module 2: The Data Layer -- CDPs and Event Architecture

A CDP collects, unifies, and activates customer data. Three CDP categories: Event Stream CDPs (Segment, mParticle -- best for data routing), Campaign CDPs (Braze, Iterable -- messaging + profiles in one), and Warehouse-Native CDPs (Hightouch, Census -- activate warehouse data). You need a CDP when you have 3+ marketing tools needing the same user data.

The event taxonomy is the foundation of the entire stack. Use Object Action naming (e.g., "Engagement Session Completed"). Every event needs standard properties plus event-specific properties plus user properties. Data flows through a hub-and-spoke architecture: sources -> central hub (CDP) -> destinations. No direct tool-to-tool integrations.

*-> Full detail (CDP selection decision tree, event categories for your product, data flow diagrams, identity resolution, data quality monitoring): `references/cdp-and-data-infrastructure.md`*

---

## Module 3: Marketing Automation and Personalization

Marketing automation progresses from batch campaigns through triggered campaigns to lifecycle journeys to dynamic ML-driven personalization. Personalization has three layers: segment-based (easiest), rule-based (if/then logic), and ML-driven (predictive content/timing/channel selection).

Cross-channel orchestration follows a priority hierarchy: in-app (highest engagement) -> push (high visibility) -> email (rich content) -> SMS (transactional only). Frequency capping is critical: push max 1-2/day, email max 3-4/week.

*-> Full detail (automation maturity ladder, campaign architecture table for your product, personalization layers, channel selection framework, frequency capping): `references/martech-stack-architecture.md`*

---

## Module 4: Martech Operations and Governance

Martech ownership models: Marketing-owned (fast but technical debt), Engineering-owned (rigorous but slow), Dedicated Martech Team (balanced but overhead), Marketing Ops Hybrid (recommended for your product -- a bridge between marketing and engineering). Run quarterly stack audits: inventory all tools, assess usage, analyze overlap, identify gaps, rationalize. Govern event tracking with an approval process, naming rules, and quarterly audits. Handle PII carefully -- only send PII to tools that need it, implement consent management, audit access quarterly.

*-> Full detail (operating models, tool evaluation RICE framework, vendor checklist, stack audit process, data governance, PII classification): `references/martech-governance-and-ops.md`*

---

## Decision Tools

### Decision 1: Do We Need a CDP?

```
How many downstream marketing tools do you need to send user data to?
+-- 1-2 tools --> No CDP needed
|   +-- Use native integrations between tools
+-- 3-5 tools --> CDP likely valuable
|   +-- Are you spending >10 engineering hours/month on marketing data requests?
|   |   +-- Yes --> Implement CDP now (Segment or mParticle for event streaming)
|   |   +-- No --> Monitor -- implement when engineering burden grows
|   +-- Do you need cross-channel user profiles?
|       +-- Yes --> CDP is essential (identity resolution is core)
|       +-- No --> Data warehouse + reverse ETL may suffice
+-- 6+ tools --> CDP is essential
    +-- Choose category based on need:
        +-- Need flexible data routing --> Event stream CDP (Segment, mParticle)
        +-- Need messaging + segmentation --> Campaign CDP (Braze, Iterable)
        +-- Already have mature warehouse --> Warehouse-native (Hightouch, Census)
```

### Decision 2: Which Martech Tool Should We Buy?

```
Is this capability a core competitive differentiator for our product?
+-- Yes --> Build it in-house (invest in custom solution)
|   +-- Example: your product's engagement session recommendation engine
+-- No --> Buy from a vendor
    +-- Is there a tool that integrates natively with our existing CDP/stack?
        +-- Yes --> Strongly prefer it (integration reduces implementation cost by 50%+)
        |   +-- Does it pass the vendor evaluation checklist?
        |       +-- Yes --> Proceed with POC
        |       +-- No --> Evaluate alternatives
        +-- No --> Evaluate top 3 options by RICE score
            +-- Run POC with the top scorer
            +-- If POC fails --> Try #2
            +-- If all fail --> Consider build option or adjust requirements
```

### Decision 3: When to Upgrade Your Martech Stack

```
Are you hitting the ceiling of your current maturity stage?
+-- Stage 1 (Ad Hoc) ceiling signs:
|   - Spending >5 hours/week on manual data tasks
|   - Can't answer basic questions about user behavior
|   --> Action: Implement event tracking + CDP (move to Stage 2)
|
+-- Stage 2 (Connected) ceiling signs:
|   - Integrations break frequently
|   - Can't coordinate campaigns across channels
|   --> Action: Centralize on CDP + campaign platform (move to Stage 3)
|
+-- Stage 3 (Integrated) ceiling signs:
|   - Personalization is limited to basic segments
|   - Can't react to real-time user behavior
|   --> Action: Invest in real-time data activation + ML (move to Stage 4)
|
+-- Stage 4 (Intelligent) ceiling signs:
    - Marketing is reactive, not predictive
    - Can't forecast churn or LTV at individual level
    --> Action: Build predictive models + automated optimization (move to Stage 5)
```

---

## Applied to your product

**Current State:** Likely Stage 2-3 of the martech maturity model. Core needs: (1) reliable event collection from iOS/Android, (2) campaign platform for push/email/in-app across the subscriber lifecycle, (3) data layer connecting acquisition -> retention -> monetization data.

**Critical Data Flow:** Acquisition Source -> App Behavior -> Subscription Status -> Content Engagement -> Churn Risk. If this flow is broken at any point, marketing is flying blind.

**Recommended Stack:** (1) Segment or mParticle for event collection, (2) Braze or Iterable for lifecycle messaging, (3) Amplitude or Mixpanel for product analytics, (4) AppsFlyer or Branch for mobile attribution, (5) Snowflake or BigQuery as data warehouse.

**Highest-Leverage Investment:** Getting the event taxonomy right. Every downstream capability depends on clean, consistent event data. Before buying any new tool, audit event tracking.

**Personalization Roadmap:** Start with segment-based (free vs. trial vs. premium messaging), graduate to rule-based (content type preferences, time-of-day), eventually invest in ML-driven (engagement session recommendations, send-time optimization).

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| Martech Stack | The collection of marketing technology tools a company uses, and how they connect |
| CDP (Customer Data Platform) | Platform that collects, unifies, and activates customer data across all touchpoints |
| Event Taxonomy | The standardized naming convention and property schema for all tracked user actions |
| Identity Resolution | Stitching anonymous and known user profiles across devices and sessions |
| Data Activation | Sending customer data and segments from your data layer to downstream tools for action |
| Reverse ETL | Moving data from a data warehouse back into operational tools |
| Campaign Orchestration | Coordinating messaging across channels based on user behavior |
| Frequency Capping | Limiting the number of messages a user receives across channels in a given time period |
| Event Stream | The real-time flow of user behavior events from source to destinations |
| Martech Maturity Model | Framework for assessing and advancing marketing technology sophistication (5 stages) |
| Data Governance | Policies and processes for maintaining data quality, consistency, and compliance |
| Lifecycle Campaign | Automated campaign triggered by a user's stage in their journey |
| Personalization Layer | Level of sophistication in customizing content per user (segment, rule, ML) |
| Tool Rationalization | Auditing, consolidating, and eliminating redundant or underused martech tools |

---

## Reference Files

- `references/martech-stack-architecture.md` -- Maturity model, capability-first framework, anti-patterns, stack architecture, build vs buy, golden stacks, marketing automation, personalization, cross-channel orchestration
- `references/cdp-and-data-infrastructure.md` -- CDP selection, event taxonomy design, event categories for your product, data pipeline architecture, identity resolution, data quality monitoring
- `references/martech-governance-and-ops.md` -- Marketing data governance, tool lifecycle management, stack audit process, PII/privacy, martech team operating models
