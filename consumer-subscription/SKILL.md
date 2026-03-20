---
name: consumer-subscription
description: Applies Phil Carter's consumer subscription growth frameworks and Patrick Campbell's monetization and pricing methodology to diagnose, measure, and accelerate subscription app growth. Covers the subscription growth equation, paywall optimization, trial conversion strategy, churn diagnosis, pricing architecture, willingness-to-pay research, value-based pricing, tier design, pricing experiments, and LTV modeling. The most relevant skill for your product as a consumer subscription app. Activates when analyzing subscription metrics, designing paywall experiences, optimizing free-to-paid conversion, diagnosing churn, setting pricing strategy, running WTP research, designing tier packaging, forecasting LTV, or making any growth decision for a consumer subscription business.
---

**Reference files:**
- `references/subscription-growth-and-conversion.md` -- Growth equation, four levers, health metrics, paywall architectures, paywall design principles, trial optimization, acquisition quality, conversion funnel, A/B testing playbook, ARPU strategies
- `references/churn-retention-and-ltv.md` -- Churn taxonomy with intervention strategies, save flow implementation, retention system design, LTV modeling methods (simple, cohort, segmented), engagement scoring
- `references/pricing-research-and-experiments.md` -- Pricing strategy overview, plan matrix, good/better/best framework, annual vs monthly strategy, value-based pricing process, WTP research (Van Westendorp, Gabor-Granger), value metric, tier packaging, pricing experiments

---

## How to Use This Skill

When this skill activates:
1. Identify which subscription growth or pricing framework best applies to the question
2. Apply the relevant decision tree from the Decision Tools section
3. Ground all recommendations in the context of your product
4. Cite the specific framework when making claims
5. If deeper detail is needed, read the relevant reference file before responding

## Gotchas

Common mistakes to avoid when applying these frameworks:

1. **Optimizing conversion rate in isolation:** Higher conversion from a lower or more aggressive paywall often degrades retention and LTV. Always evaluate paywall changes on cohort LTV and RPV, not just conversion rate -- Carter is explicit that these levers are interdependent.
2. **Using simple LTV when cohorts behave differently:** The formula LTV = ARPU / Churn is only valid when churn is roughly constant across cohorts. For your product, where annual vs. monthly subscribers and acquisition channel mix vary widely, use cohort-based survival analysis or you will overestimate LTV for low-quality segments.
3. **Running WTP research on current subscribers only:** Van Westendorp and Gabor-Granger must include non-subscribers and churned users to capture the full willingness-to-pay distribution. Surveying only active subscribers produces inflated price points because you are sampling the people who already accepted your price.
4. **Treating involuntary churn as a retention problem:** Involuntary churn (payment failures) is 20-40% of total churn and is solved with dunning engineering, not product improvements. Mixing it into voluntary churn metrics masks the real retention signal.

## Example

**User asks:** "Our free trial conversion rate is 8% but we think it should be higher. What should we do?"

**Approach:**
1. Apply Carter's CRO testing priority hierarchy: check paywall placement/timing first, then plan presentation, then pricing levels, then social proof
2. Diagnose whether the 8% is a timing problem (paywall too early before value realization) or a value communication problem (paywall at the right moment but not compelling)
3. Check trial length against your product's value realization speed -- Carter recommends 7-day for content apps, so validate this matches how quickly users form the daily engagement habit
4. Recommend a structured A/B test sequence starting with paywall timing, with cohort LTV (not just conversion rate) as the primary success metric

---

## Core Philosophy

Consumer subscription growth is a system, not a set of isolated levers. Carter frames it as an interconnected equation where acquisition quality, activation depth, monetization timing, and retention durability all compound on each other. Optimizing one in isolation often breaks another.

Campbell adds that pricing is the most under-invested lever: a 1% improvement in pricing yields an estimated 12.7% improvement in profit, vs. roughly 3.3% for acquisition and 6.7% for retention. Three foundations: (1) Pricing is a process, not a project -- revisit quarterly. (2) Value-based pricing beats cost-plus and competitor-based. (3) The value metric is the linchpin determining how pricing scales and aligns with customer value.

---

## Module 1: The Subscription Growth System

Revenue is driven by: MRR = Active Subscribers x ARPU, where New Subscribers = New Users x Activation Rate x Conversion Rate. These variables are interdependent -- improving acquisition volume with lower-quality users degrades activation, conversion, and retention.

**Four levers:** (1) Acquisition Quality (channel-level cohort analysis, not just volume), (2) Free-to-Paid Conversion (the most leveraged metric, influenced by paywall design, trial structure, timing), (3) ARPU (pricing architecture, plan mix, expansion revenue), (4) Retention (the multiplier -- 10% retention improvement often worth more than 30% acquisition improvement). The subscription user journey runs: Awareness -> Install -> Onboard -> Activate -> Paywall -> Trial -> Convert -> Retain -> Expand.

*-> Full detail (growth equation, health metrics benchmarks, diagnostic framework): `references/subscription-growth-and-conversion.md`*

---

## Module 2: Paywall Strategy and Free-to-Paid Conversion

Three paywall architectures: Hard Paywall (subscribe to access -- best for strong brand), Freemium (meaningful free tier + premium -- best for habit formation), and Free Trial (full access then paywall -- best when value requires sustained usage). Core design principles: show value before asking for money, trigger at the right moment, reduce perceived risk, and anchor on value not price.

Trial length should match value realization speed: 3-day for immediate value, 7-day for content apps like your product, 14-day for habit-forming products. CRO testing priority: (1) paywall placement/timing, (2) plan presentation, (3) pricing levels, (4) social proof.

*-> Full detail (paywall design principles, trial optimization calendar, CRO playbook, screen design anatomy): `references/subscription-growth-and-conversion.md`*

---

## Module 3: Pricing Strategy and Value-Based Pricing

Value-based pricing is the right approach for consumer subscriptions. The value metric (the unit you charge on) is the most important pricing decision. For consumer content products, flat monthly/annual pricing works best because simplicity is critical and per-usage pricing feels punitive.

Use the Good/Better/Best framework: GOOD (free, for acquisition), BETTER (premium, the revenue core), BEST (family/ultimate, for max ARPU + anchoring). Strongly incentivize annual plans -- healthy apps have 60-70%+ on annual. Research WTP using Van Westendorp (4 price sensitivity questions) or Gabor-Granger (buy/no-buy at sequential prices). Campbell's data: companies who research WTP outperform those who guess by 30-40% in revenue per customer.

*-> Full detail (pricing models, plan matrix, annual vs monthly strategy, WTP research methods, tier packaging, pricing experiments): `references/pricing-research-and-experiments.md`*

---

## Module 4: Retention, Churn Management, and LTV

Three churn types: Involuntary (payment failure, 20-40% of total -- most recoverable via dunning), Voluntary Active (conscious cancel with sub-types: value, use-case, competitive, experience), and Voluntary Passive (disengagement then cancel -- largest bucket, hardest to address). The retention curve has three phases: early churn (day 1-30, fix activation), medium-term (month 1-6, fix habit formation), and steady-state (month 6+, fix value depth).

Deploy a save flow at cancellation: ask why, address the specific objection, offer pause (30-50% reactivation rate), offer final incentive, graceful exit. LTV = ARPU / Monthly Churn (simple) or cohort-based survival analysis (more accurate). The LTV improvement hierarchy: reduce churn > increase conversion > shift to annual > increase ARPU > reduce CAC.

*-> Full detail (churn taxonomy, save flow architecture, retention system layers, LTV modeling methods, engagement scoring): `references/churn-retention-and-ltv.md`*

---

## Decision Tools

### Decision 1: Where to Focus Growth Effort

```
IF LTV/CAC < 2:
  STOP: Don't invest in acquisition until unit economics are healthy
  Focus on: Retention improvement and conversion rate optimization

IF LTV/CAC 2-3 and conversion rate < 3%:
  Focus on: Free-to-paid conversion (paywall optimization, trial design)

IF LTV/CAC 2-3 and conversion rate > 3%:
  Focus on: Retention (churn diagnosis, engagement depth)

IF LTV/CAC > 3 and growth is below target:
  Focus on: Acquisition volume and quality

IF LTV/CAC > 3 and growth is on target:
  Focus on: ARPU expansion (pricing, plan mix, upsell)
```

### Decision 2: Paywall Architecture Choice

```
IF your product has strong brand recognition and unique content:
  Consider: Hard paywall or tight freemium

IF your product relies on habit formation for retention:
  Choose: Freemium with generous free tier

IF your product's value is immediately obvious (within 1 session):
  Choose: Free trial (3-7 day)

IF your product's value compounds over weeks:
  Choose: Freemium with trial for premium features
```

### Decision 3: How to Set Your Price

```
Do you have willingness-to-pay data from customer research?
  YES -> Use Van Westendorp or Gabor-Granger results
    Set base price at the Optimal Price Point
    Create 2-3 tiers spanning the acceptable range
    Test with a pricing experiment
  NO -> Use proxy methods
    What do competitors charge for similar products?
      Position 10-20% above if you have clear differentiation
      Position at parity if undifferentiated
      Position below only if cost advantage is sustainable
    What is the value to the customer in saved time or money?
      Capture 10-20% of the value delivered
    THEN: Plan to run WTP research within 90 days
```

### Decision 4: Pricing Optimization Priority

```
IF annual plan adoption < 50%:
  Priority: Increase annual incentive (bigger discount, better presentation)

IF trial-to-paid conversion < 50%:
  Priority: Improve trial experience (better onboarding, value demonstration)

IF churn within first 30 days > 15%:
  Priority: Post-conversion experience (avoid buyer's remorse)

IF average subscription tenure < 6 months:
  Priority: Long-term retention (content freshness, community depth)
```

### Decision 5: When to Raise Prices

```
Have you raised prices in the last 12 months?
  NO -> You are probably underpriced. Consider:
    Is WTP research showing headroom above current price? Raise.
    Has your product improved significantly? Raise.
    Are acquisition costs increasing? Raise to maintain margins.
  YES -> Wait, unless:
    Major value-add (new product line, significant new features)
    Market conditions shifted (inflation, competitor raised prices)
    WTP research shows significant headroom remaining
```

### Decision 6: Churn Diagnosis and Response

```
IF involuntary churn > 30% of total churn:
  Action: Implement/improve dunning flow (retry logic, card update prompts)
  Expected impact: 20-40% recovery of involuntary churn

IF voluntary churn driven by "not using enough":
  Action: Re-engagement campaigns + notification optimization

IF voluntary churn driven by "too expensive":
  Action: Test downsell tier OR demonstrate more value at current price
  Warning: Don't lower price without addressing underlying value perception

IF voluntary churn driven by "found alternative":
  Action: Competitive differentiation audit
```

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| Subscription Growth Equation | System of interconnected variables (acquisition, conversion, ARPU, retention) that drive subscription revenue |
| Quick Ratio | New MRR divided by Lost MRR; measures growth efficiency (>3 is healthy) |
| Involuntary Churn | Subscriber loss due to payment failure rather than deliberate cancellation |
| Save Flow | Cancellation intervention sequence designed to retain at-risk subscribers |
| Dunning | Automated sequence to recover failed payments (retry, card update, grace period) |
| Value Metric | The unit of value that determines how much a customer pays |
| Van Westendorp | Pricing research method using four price sensitivity questions to find optimal price range |
| Gabor-Granger | Pricing research method that directly asks buy/no-buy at sequential prices to plot demand curve |
| Revenue Per Visitor (RPV) | Conversion rate multiplied by average price paid; primary metric for pricing experiments |

---

## Reference Files

- `references/subscription-growth-and-conversion.md` -- Growth equation, four levers, health metrics, paywall architectures, design principles, trial optimization, acquisition quality, conversion funnel, A/B testing playbook
- `references/churn-retention-and-ltv.md` -- Complete churn taxonomy with interventions, save flow implementation, retention system design, LTV modeling, engagement scoring
- `references/pricing-research-and-experiments.md` -- Pricing strategy overview, plan matrix, annual vs monthly, value-based pricing, WTP research methods, tier packaging, pricing experiments, experiment templates
