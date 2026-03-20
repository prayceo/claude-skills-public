---
name: product-analytics
description: Applies Crystal Widjaja's Mastering Product Analytics frameworks to any data decision. Crystal built Gojek's data org from 0 to 200+ people and scaled from 30K to 5M orders/day as the first data hire and eventual SVP of Growth & Data. Activates when asked about product analytics, metrics, event tracking, data strategy, retention analysis, user segmentation, funnel analysis, cohort analysis, what to measure, why data feels like a mess, how to become data-driven, what data infrastructure your product needs, data theater, altitude maps, subscription benchmarks, activation funnels, feature bundles, or hybrid monetization. Triggers proactively when reviewing any product decision that should be grounded in data, when designing experiments, when building dashboards, when diagnosing why a metric is moving, or when prioritizing features using data.
---

**Reference files:**
- `references/altitude-maps.md` — Altitude Maps framework, Data Theater diagnosis, Data Wheel of Death, controllable vs. uncontrollable inputs, Solution Scorecard
- `references/event-tracking.md` — Full event tracking system: Intent/Success/Failure, properties, Event Tracking Dictionary
- `references/data-maturity.md` — Full 3-stage x 4-capability scaling framework
- `references/analytical-tools.md` — Key analytical techniques: segmentation, cohort retention, funnels, correlation, risk ratios
- `references/data-diagnostics.md` — Diagnostic framework, Data Trust Diagnostic, 10 analytics mistakes, communicating data to stakeholders

---

## How to Use This Skill

When this skill activates:
1. Identify which product analytics framework from this skill best applies to the question
2. Apply the relevant decision tree from the Decision Tools section
3. Ground all recommendations in the context of your product
4. Cite the specific framework when making claims
5. If deeper detail is needed, read the relevant reference file before responding

## Gotchas

Common mistakes to avoid when applying these frameworks:

1. **Don't goal on retention before understanding activation.** Crystal warns that retention metrics are misleading if activation is broken -- you're measuring a biased self-selected group, not your actual user base.
2. **Don't build Data Led infrastructure at a Data Driven stage.** The most common startup data mistake is overbuilding. If your product hasn't stabilized retention curves per cohort, investing in real-time data products is premature and wasteful.
3. **Don't track events without the Intent/Success/Failure triple.** Logging a "engagement session_completed" event without the corresponding intent event ("engagement session_started") and failure events (drop-offs, errors) makes the data descriptively interesting but analytically useless -- you can't diagnose *why* completion rates change.
4. **Don't confuse an Altitude Map with a dashboard.** An Altitude Map connects company OKRs to team metrics to user events in a causal chain. A dashboard just displays numbers. If the map doesn't show how moving a low-altitude event changes a high-altitude metric, it's decoration.

## Example

**User asks:** "Our Day 7 retention dropped 4 points this month. What should we do?"

**Approach:**
1. Apply Crystal's 6-step diagnostic framework (Scope -> Decompose -> Trace -> Hypothesize -> Validate -> Act) from Module 3
2. Decompose by user segment -- separate new users vs. existing, acquisition source, platform, and cohort month to isolate which group is driving the drop
3. Trace event-level changes in those segments -- look for shifts in activation funnel completion, content engagement patterns, or new failure events
4. Ground in your product context -- check whether content calendar changes, paywall experiments, or notification timing shifts coincide with the drop, and recommend specific data cuts before jumping to solutions

---

## Crystal's Core Philosophy

> "The real goal of data initiatives isn't to track metrics — it's to analyze them. Those two things are very different. Making information actionable is about how we separate what successful people do vs. what failed people do in our products."

Three foundational beliefs:

1. **Data is a strategic lever, not a team or toolset.** The question is: how does data create leverage at our current stage?
2. **Humanize data systems.** Build data systems with the same product thinking you'd apply to your actual product. If your ops team can't use the data independently, the system has failed.
3. **Track journeys, not metrics.** Tracking intent -> success -> failure events tells you *why*. The "why" is the only thing that's actionable.

---

## Module 1: Data Theater & Altitude Maps

Data Theater is Crystal's diagnosis of organizational data dysfunction: using copious data in ways that feel smart without impacting decisions. The cure is Altitude Maps — a framework connecting high-altitude strategy (company OKRs), mid-altitude product metrics (feature KPIs), and low-altitude operational events (user behaviors). Altitude Maps also include the Solution Scorecard for feature prioritization and the distinction between controllable vs. uncontrollable inputs.

*-> Full detail: `references/altitude-maps.md`*

---

## Module 2: Key Analytical Tools

Five techniques form the core toolkit: (1) Segmentation Analysis — separate what successful users do from unsuccessful ones; (2) Retention Cohorts — measure retention by when users joined, always separating activated from all users; (3) User Journey Funnels — visualize step-by-step drop-off; (4) Correlation Analysis — find "magic moment" behaviors that predict long-term retention; (5) Risk Ratios — quantify how much riskier one user segment is than another. Includes subscription app benchmarks and your product worked examples.

*-> Full detail: `references/analytical-tools.md`*

---

## Module 3: Advanced Data Diagnostics

How to investigate when a metric moves unexpectedly. Includes a 6-step diagnostic framework (Scope -> Decompose -> Trace -> Hypothesize -> Validate -> Act), the Data Trust Diagnostic (4-level test of organizational data trustworthiness), the "Questions Before Queries" discipline, Crystal's 10 analytics mistakes, and stakeholder communication principles.

*-> Full detail: `references/data-diagnostics.md`*

---

## Module 4: Event Tracking System

Crystal's Intent/Success/Failure event tracking framework — her most cited public work. Events should be named at the right abstraction level with rich properties for segmentation. The Event Tracking Dictionary is the organizational artifact that makes it work: every event needs a name, trigger description, screenshot, properties, and values. Includes the business user mindset test and your product event audit checklist.

*-> Full detail: `references/event-tracking.md`*

---

## The Scaling Data Framework

Crystal's framework for diagnosing what data capabilities your company actually needs. Follows a Strategy -> Stage -> Team -> Tools sequence. Three maturity stages: Data Informed (pre-PMF, operational visibility), Data Driven (post-PMF, feature optimization), and Data Led (at scale, productized data). your product is likely at Data Driven stage. Includes overbuilding/underbuilding traps and stage transition checklists.

*-> Full detail: `references/data-maturity.md`*

---

## Decision Tools

### What should we track?

```
What are the success events for this feature?
  -> Define the completed action first

What are the intent events before each success event?
  -> Every step required to reach success

What are the failure events between intent and success?
  -> Both explicit (error states) and implicit (drop-offs)

For each event: what properties do I need to segment it?
  -> User profile + marketing source + action type + context
```

### Is our data trustworthy?

```
Does more of Event B ever happen than Event A when B follows A?
  -> Yes -> Tracking is broken. Stop all analysis until fixed.
  -> No -> Do Finance and Product agree on key metrics?
              -> No -> Metric definitions misaligned. Fix data dictionary.
              -> Yes -> Can business users self-serve?
                          -> No -> Analytics tool or documentation problem.
                          -> Yes -> Does analysis change behavior?
                                      -> No -> Culture problem. Address before more analysis.
                                      -> Yes -> Data is trustworthy and influential.
```

### What's causing this metric to move?

```
1. Scope: When exactly did it start? Which metric specifically?
2. Decompose: Which user segment(s) is driving it?
   -> New vs. existing users? Specific acquisition source? Platform? Cohort month?
3. Trace: What events changed in those segments?
   -> Look for event frequency changes, funnel drop-off shifts, new failure events
4. Hypothesize: What product/external change could explain this?
5. Validate: Test hypothesis with additional data cuts
6. Act: What is the recommendation?
```

### Am I at the right data maturity stage?

```
Have you achieved stable retention curves (PMF)?
  -> No -> You're Data Informed. Focus on: single source of truth, basic KPI dashboards,
          metric definitions, and activation tracking. Don't build more.
  -> Yes -> Are you actively optimizing feature-level metrics?
              -> No -> Move to Data Driven. Invest in: self-serve analytics,
                      experimentation tooling, deeper segmentation.
              -> Yes -> Do business operations require real-time data products to function?
                          -> No -> Stay Data Driven. Don't overbuild toward Data Led.
                          -> Yes -> Consider Data Led capabilities selectively.
```

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **Altitude Map** | Crystal's framework mapping company OKRs -> team metrics -> product events at three levels of analysis |
| **Data Theater** | The organizational sin of using data in ways that feel smart without actually impacting decisions or core metrics |
| **Solution Scorecard** | The third layer of an Altitude Map that indexes features being built and assesses how they move altitude metrics |
| **Controllable input** | An input metric that can be directly influenced through product or operational changes |
| **Uncontrollable input** | An input metric influenced by external forces the team can't directly change |
| **Intent event** | An event that precedes a success event; required to understand the "why" behind success |
| **Success event** | An event representing a desired completed action |
| **Failure event** | An explicit or implicit event representing a blocked path to success |
| **Event Tracking Dictionary** | Shared document defining every tracked event with name, trigger, screenshot, properties, and description |
| **Data Wheel of Death** | The cycle where unanalyzed data loses trust -> teams stop using it -> product changes -> data goes stale |
| **Feature bundle** | A group of product features that map to a single job-to-be-done; analytics should be segmented by bundle |
| **Data Informed** | Stage 1: pre-PMF; data provides operational visibility |
| **Data Driven** | Stage 2: post-PMF; data guides feature-level decisions |
| **Data Led** | Stage 3: at scale; operations cannot function without data products |
| **Overbuilding** | Building data infrastructure ahead of product maturity — most common startup mistake |
| **Business user mindset** | Designing analytics systems for non-technical decision-makers, not analysts |
| **Magic moment** | The specific activation behavior that strongly predicts long-term retention |

---

## Reference Files

- `references/altitude-maps.md` — Altitude Maps framework, Data Theater diagnosis, Data Wheel of Death, controllable vs. uncontrollable inputs, Solution Scorecard with your product hypothesis
- `references/event-tracking.md` — Full Intent/Success/Failure system, property types, Event Tracking Dictionary template, abstraction rules, activation funnel analysis procedure
- `references/data-maturity.md` — Full 3-stage x 4-capability framework with stage-specific capabilities, pitfalls, and sequencing guidance
- `references/analytical-tools.md` — Deep reference on all five analytical techniques with worked examples and subscription app benchmarks
- `references/data-diagnostics.md` — Diagnostic framework, Data Trust Diagnostic, 10 analytics mistakes to avoid, communicating data to stakeholders
