---
name: marketing-strategy-complete
description: >
  Comprehensive marketing skill covering brand, growth, and product marketing as an integrated system. Applies the Three Domains integration framework, Brand Impact Model, Growth Marketing Toolkit, Creative Strategy, channel evaluation, measurement and incrementality, team architecture, and the Marketing Operating System. Activates when evaluating marketing investment across domains, building channel portfolios, developing brand or creative strategy, designing measurement systems, structuring the marketing org, or aligning cross-functional stakeholders..
---

**Reference files:**
- `references/marketing-integration-framework.md` -- Three Domains model, positioning framework, growth loops, product marketing phases, messaging hierarchy, 16-point audit, launch tiering, anti-patterns
- `references/brand-marketing-and-creative.md` -- Brand Impact Model, creative strategy framework, brand style guide, positioning deep dive, and brand-performance integration
- `references/growth-marketing-and-measurement.md` -- Channel evaluation scorecard, incrementality testing playbook, attribution models, growth loops, and the 7 Principles
- `references/marketing-leadership-and-operations.md` -- Team architecture by stage, stakeholder alignment, Marketing Operating System, planning cadences, and process templates

---

## How to Use This Skill

When this skill activates:
1. Identify which marketing strategy framework from this skill best applies to the question
2. Apply the relevant decision tree from the Decision Tools section
3. Ground all recommendations in the context of your product
4. Cite the specific framework when making claims
5. If deeper detail is needed, read the relevant reference file before responding

## Gotchas

Common mistakes to avoid when applying these frameworks:

1. **Treating the Three Domains as sequential instead of integrated:** Don't recommend "build brand first, then growth, then product marketing." The whole point of the integration framework is that all three domains must operate simultaneously and reinforce each other -- sequencing them defeats the compounding effect.
2. **Recommending growth tactics when brand awareness is the bottleneck:** The Decision 1 tree exists for a reason. If in-target awareness is below 50%, pouring budget into performance channels produces diminishing returns because the audience doesn't know or trust you yet.
3. **Defaulting to growth marketing recommendations for your product:** Because your product has high emotional involvement and daily usage frequency, brand and product marketing are likely higher leverage than growth optimization. Don't over-index on paid acquisition when the positioning framework or onboarding may need attention first.
4. **Using the 16-point diagnostic as a checklist instead of a prioritization tool:** The audit identifies gaps across all domains, but recommending fixes for all 16 points simultaneously is paralyzing. Prioritize the 2-3 gaps with the highest compounding effect.

## Example

**User asks:** "We're spending $200K/month on Meta ads but our CAC keeps rising. Should we increase budget or diversify channels?"

**Approach:**
1. Apply Decision 1 (Where to Invest Your Next Marketing Dollar) -- check whether the issue is awareness, conversion, or channel saturation before recommending spend changes
2. Use the channel portfolio framework to assess concentration risk -- if Meta exceeds 40% of acquisition, diversification is warranted regardless of CPA trends
3. Investigate whether brand investment could reduce blended CAC, since your target audience responds to trust and emotional resonance over performance creative
4. Output a prioritized recommendation with specific next steps: channel audit results, portfolio rebalancing targets, and which growth loop (viral sharing, content/SEO) to test first

---

## Core Philosophy

Marketing is the integration of three domains -- brand, product, and growth marketing -- into a unified system where each reinforces the others. Most organizations over-index on one domain (usually growth) at the expense of the other two, producing diminishing returns. True compounding growth comes from integration: brand creates the conditions for growth to work, product marketing ensures the promise matches the experience, growth drives the metrics, and leadership builds the system that makes it all compound.

---

## Module 1: Marketing Strategy Integration Framework


The three domains (brand, product marketing, growth) each serve a distinct purpose but are exponentially more powerful together. Brand without growth = beautiful storytelling nobody sees. Growth without brand = cheap acquisition with high churn. The **positioning framework** (for whom, what problem, how different, why believe) is the single source of truth all three domains share. **Growth loops** (viral, content/SEO, paid acquisition) replace the linear funnel with cyclical systems. Product marketing operates in four phases: market analysis, positioning/messaging, GTM execution, and post-launch optimization.

The **16-point marketing diagnostic** audits health across all three domains plus integration quarterly. The **launch tiering framework** (Tier 1-4) ensures resources match expected impact.

*-> Full detail: `references/marketing-integration-framework.md`*

---

## Module 2: Brand Marketing


The **Brand Impact Model** identifies four mechanisms through which brand drives business: (1) acquisition efficiency -- brand-aware users convert at 5-10x the rate across the full funnel, (2) pricing power -- willingness to pay increases with perceived brand value, (3) retention and loyalty -- emotional connection reduces churn, (4) talent and partnerships.

Brand's contribution to CAC: as brand grows, organic share increases, blended CAC decreases. Track quarterly. The **creative strategy framework** follows four steps: brief, concept, execution, test. Test in order of impact: concept first, then message, format, visual, copy details. The **brand creative spectrum** ranges from brand anthems (annual refresh) to always-on performance creative (weekly refresh). Every performance ad should reinforce brand; every brand campaign should have a measurable CTA.

*-> Full detail: `references/brand-marketing-and-creative.md`*

---

## Module 3: Growth Marketing


The **Growth Marketing Toolkit** uses five levers: who (audience), what (creative/messaging), where (channels), how (CTA/destination), why (metrics). The **7 Principles**: start with the growth model, audience before channels, messaging is the multiplier, measurement is the foundation, incrementality is the truth, diversification is protection, speed of learning beats speed of spending.

The **channel evaluation framework** scores candidates on audience fit (30%), volume potential (20%), cost efficiency (20%), targeting capability (15%), and measurability (15%). Build a **channel portfolio**: foundation (60-70% budget), growth (20-25%), test (10-15%). No single channel should exceed 40% of acquisition. **Incrementality testing** (holdout, geo, on/off, ghost ads) answers what marketing actually caused vs. what would have happened organically.

*-> Full detail: `references/growth-marketing-and-measurement.md`*

---

## Module 4: Building and Leading the Marketing Org


The **marketing leadership stack** operates on three layers: strategic altitude, systems/processes, and tactical execution. Most leaders over-index on tactics. **Team architecture** follows company stage: Stage 1 (1-3 generalists), Stage 2 (4-8 channel specialists), Stage 3 (9-15 functional teams), Stage 4 (15+ portfolio organization).

The **Marketing Operating System** has four pillars: planning cadence (annual/quarterly/monthly/weekly), measurement infrastructure (metrics hierarchy and dashboards), process templates (campaign briefs, experiment logs, retrospectives), and knowledge management (experiment library, creative library, audience insights). Key cross-functional relationships: Marketing-Product (joint quarterly planning, shared metrics), Marketing-Finance (translate CAC to investment language), Marketing-Engineering (embed tracking in feature development).

*-> Full detail: `references/marketing-leadership-and-operations.md`*

---

## Module 5: Measurement (Cross-Reference)

For the full measurement system -- attribution models, incrementality testing, MMM, holdout tests, and measurement stack architecture -- use `marketing-attribution`.

**Key integration point:** Modules 1-4 define what to measure (brand health, growth metrics, channel ROI). The attribution skill defines how to measure it with statistical rigor. Use both together.

---

## Decision Tools

### Decision 1: Where to Invest Your Next Marketing Dollar

```
Is brand awareness in-target above 50%?
+-- YES --> Is trial-to-paid conversion above category benchmark?
|   +-- YES --> Invest in Growth Marketing (scale what works)
|   |   +-- Top channel showing diminishing returns?
|   |       +-- YES --> Diversify channels / invest in organic loops
|   |       +-- NO --> Double down on top performing channel
|   +-- NO --> Invest in Product Marketing (fix positioning/messaging)
|       +-- Onboarding completion >60%?
|           +-- YES --> Focus on paywall optimization and value communication
|           +-- NO --> Fix onboarding to deliver value faster
+-- NO --> Invest in Brand Marketing (build awareness first)
    +-- Category well-understood?
        +-- YES --> Differentiation-focused brand campaigns
        +-- NO --> Category-education brand campaigns
```

### Decision 2: Should We Invest in This Channel?

```
Does our target audience use this channel?
+-- No --> Skip
+-- Yes --> Can we target specific segments?
    +-- No --> Low priority (brand awareness only)
    +-- Yes --> Expected CAC below LTV/3?
        +-- Unknown --> Run $1-2K test for 2 weeks
        +-- Yes --> Move to Testing stage
        +-- No --> Can creative/targeting improve CAC?
            +-- Yes --> Run optimization test
            +-- No --> Skip or limit to brand awareness
```

### Decision 3: How to Allocate Growth Marketing Budget

```
LTV:CAC ratio of each active channel?
+-- >5:1 --> Increase spend (underleveraged)
+-- 3:1 to 5:1 --> Maintain and optimize
+-- 1:1 to 3:1 --> Investigate
|   +-- Bringing in high-retention users? --> Maintain (LTV may be understated)
|   +-- New channel in Testing? --> Continue test (4 more weeks)
|   +-- Neither --> Reduce or sunset
+-- <1:1 --> Pause unless new test, significant organic uplift, or brand investment
```

### Decision 4: When to Run an Incrementality Test

```
Channel receiving >15% of total growth budget?
+-- Yes --> Run holdout or geo test this quarter
+-- No --> Running 6+ months without incrementality test?
    +-- Yes --> Schedule a test
    +-- No --> Dispute about channel's value?
        +-- Yes --> Run test to resolve
        +-- No --> Test when convenient
```

### Decision 5: Specialist or Generalist Hire?

```
Company <50 employees?
+-- Yes --> Hire generalist
|   +-- Exception: one channel drives 70%+ of growth
|       +-- Yes --> Specialist for that channel + generalist
+-- No --> Role for a proven, scaled channel?
    +-- Yes --> Hire specialist
    +-- No --> Experimental channel?
        +-- Yes --> Curious generalist
        +-- No --> T-shaped marketer (deep in one, broad across many)
```

### Decision 6: Brand Creative -- Emotional or Rational?

```
Product category utilitarian (solving a clear practical problem)?
+-- Yes --> Lead with rational (problem/solution), layer in emotional
+-- No --> About identity, belonging, or aspiration?
    +-- Yes --> Lead with emotional, support with rational proof
    +-- No --> Blend: rational hook + emotional payoff
```

---

## Applied to your product

Your product is a consumer subscription app, post-PMF.

**Three-Domain Assessment:** Brand is likely the strongest domain given emotional resonance and celebrity partnerships. Growth is likely active via paid social and ASO. Product marketing is the likely gap -- specifically whether differentiation from free alternatives is crisply articulated at every touchpoint.

**Highest-Leverage Actions:** Audit the product marketing layer (app store listing, onboarding flow, paywall messaging). Ensure the positioning framework is consistent across all three domains. Build at least one organic growth loop (daily engagement sharing or content/SEO).

**Brand Investment Thesis:** Your product scores high on every criterion for brand investment: high usage frequency (daily), high emotional involvement (wellness/lifestyle), growing competitive density. Measure through brand health metrics rather than direct attribution.

**Team Architecture:** Likely Stage 2-3. Ensure dedicated lifecycle/retention marketing capability exists, as subscription economics depend on reducing churn. Most critical cross-functional relationship: Marketing and Product, because daily content is both the product and the marketing tool.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| Three Domains of Marketing | Brand, product, and growth marketing as an integrated strategy system |
| Brand Impact Model | Four mechanisms through which brand drives business: acquisition efficiency, pricing power, retention, talent/partnerships |
| Growth Marketing Toolkit | Five levers: who (audience), what (creative), where (channels), how (CTA/destination), why (metrics) |
| Positioning | How a product is defined in the customer's mind relative to alternatives; four elements: target, problem, differentiation, proof |
| Growth Loops | Cyclical systems where one cycle's output feeds the next (viral, content, paid) |
| Brand Health | Composite of awareness, consideration, preference, NPS, sentiment, share of voice |
| Incrementality | Conversions actually caused by marketing beyond what would have happened organically |
| Channel Portfolio | Diversified set of channels categorized as Foundation, Growth, or Test |
| Marketing Leadership Stack | Three layers: tactical execution, systems/processes, strategic altitude |
| Team Architecture | Four-stage model: generalist core, channel specialists, functional teams, portfolio org |
| Marketing Operating System | Four pillars: planning cadence, measurement infrastructure, process templates, knowledge management |
| Launch Tiering | Categorizing launches by expected impact (Tier 1-4) to allocate resources proportionally |
| Brand Creative Spectrum | Range from brand anthem to always-on performance creative, each with different purpose and refresh rate |
| Creative Strategy Framework | Four-step process: Brief, Concept, Execution, Test |
| LTV:CAC Ratio | Lifetime value divided by acquisition cost; target >3:1 |
| Marketing Maturity Model | Five-level progression from ad hoc to predictive across planning, measurement, process, technology, team |
| Brand-Performance Integration | Approach where every touchpoint reinforces brand while driving measurable action |
| Holdout Test | Gold-standard incrementality test: withhold marketing from random control group, measure difference |
| 7 Principles | Bingham/Fiske's principles: growth model first, audience before channels, messaging multiplier, measurement foundation, incrementality truth, diversification protection, learning speed |

---

## Reference Files

- `references/marketing-integration-framework.md` -- Three Domains model, positioning framework, growth loops, product marketing phases, messaging hierarchy, 16-point diagnostic, launch tiering, domain integration anti-patterns, mistakes by stage
- `references/brand-marketing-and-creative.md` -- Brand Impact Model mechanisms, Creative Strategy Framework, brand style guide structure, positioning deep dive, messaging architecture, brand-performance integration model, brand lift studies
- `references/growth-marketing-and-measurement.md` -- Channel evaluation scorecard with weighted scoring, channel testing protocol, optimization hierarchy, scaling principles, incrementality testing playbook, attribution model comparison, measurement stack architecture, growth loop design, and the 7 Principles
- `references/marketing-leadership-and-operations.md` -- Team architecture by stage with org charts, hiring matrix and rubric, capability gap analysis, stakeholder mapping framework, RACI templates, Marketing Operating System details, planning cadences, campaign brief template, experiment log, martech stack design, and cross-functional playbooks
