## Contents
- Pricing Strategy Overview
  - The Three Pricing Models
  - Pricing Architecture for Consumer Subscriptions
  - Annual vs. Monthly Strategy
  - Pricing Communication Tactics
  - Price Anchoring Techniques
- The Value-Based Pricing Process
  - Step 1: Identify Target Customer Segments
  - Step 2: Research Willingness to Pay
  - Step 3: Identify the Value Metric
  - Step 4: Set Price Points
  - Step 5: Validate with Data
- Pricing Psychology
  - The Psychology of Price Endings
  - Decoy Pricing
  - Loss Aversion in Pricing
- Tier Packaging Design
  - Feature Allocation Decision Matrix
  - The Feature Allocation Process
  - Content-Based Tier Differentiation
  - Add-On and Expansion Packaging
  - Bundling vs. Unbundling
  - Packaging Anti-Patterns
- Pricing Experiments
  - Why Experiment with Pricing
  - Types of Pricing Experiments
- Experiment Design Best Practices
  - Statistical Rigor
  - Metrics Hierarchy
  - Common Pricing Experiment Mistakes
- Pricing Experiment Analysis Template
- Pricing Experimentation Roadmap
  - Phase 1: Foundation (Month 1-2)
  - Phase 2: Packaging (Month 3-4)
  - Phase 3: Price Optimization (Month 5-6)
- Ethical Considerations in Pricing Experiments
  - What Is Acceptable
  - What Is Not Acceptable
  - Best Practices
- Implementing Price Changes
  - Rolling Out a Price Increase
  - Rolling Out New Packaging
- Pricing Page Design Principles
  - Measuring Packaging Success

---
# Pricing Research, Experiments & Tier Packaging -- Deep Reference
*Sources: Patrick Campbell, ProfitWell Blog pricing series; Dan Hockenmaier, Monetization & Pricing Strategy course*

---

## Pricing Strategy Overview

### The Three Pricing Models

**Model 1: Cost-Plus Pricing** -- Calculate costs, add a margin. Fails for digital products where marginal cost is near zero.

**Model 2: Competitor-Based Pricing** -- Price relative to competitors. Fails because competitor pricing may also be wrong and creates race-to-the-bottom dynamics.

**Model 3: Value-Based Pricing (the right approach)** -- Price based on perceived value the customer receives. Process: identify segments, research WTP, identify value metric, set price to capture fair share, package features to match segment needs.

### Pricing Architecture for Consumer Subscriptions

**The Plan Matrix:**

| Plan | Price Range | Purpose | Target User |
|------|-------------|---------|-------------|
| Free | $0 | Acquisition, habit formation, viral growth | Everyone -- top of funnel |
| Monthly | $7.99-12.99 | Low-commitment entry point | Price-sensitive, trying it out |
| Annual | $49.99-79.99 | Core plan (highest LTV) | Committed users (40-60% discount vs. monthly) |
| Family/Group | $89.99-129.99/yr | Expansion revenue | Households, multi-user groups |
| Lifetime | $149.99-199.99 | One-time (use sparingly) | Super-fans (test carefully) |

**The Good/Better/Best Framework:**

Three tiers work because of the compromise effect: people prefer the middle option. Two options creates a binary buy/don't-buy decision. Three creates a "which one" decision. Four or more creates decision paralysis.

- GOOD tier exists to acquire and activate, not to monetize
- BETTER tier is where most revenue comes from -- it should feel like the obvious choice
- BEST tier serves two purposes: extract max value from power users AND make BETTER look like a good deal via anchoring

### Annual vs. Monthly Strategy

**Annual advantages:** Higher total revenue per subscriber, lower churn rate (sunk cost + longer commitment), better cash flow, higher LTV by 2-3x.

**Monthly advantages:** Lower barrier to entry, more frequent decision points, faster pricing experiment feedback.

**Optimal strategy:** Strongly incentivize annual, offer monthly as fallback. 40-50% discount for annual vs. monthly is common. Healthy apps have 60-70%+ on annual. Campbell recommends 20-30% discount; more than 35% starts leaving significant revenue on the table.

**Annual default decision guide:**
```
What is your average subscriber retention (monthly)?
  > 85% monthly retention -> Monthly default is viable
  70-85% monthly retention -> Annual default, monthly as option
  < 70% monthly retention -> Annual default with steep discount (30-35%)
```

### Pricing Communication Tactics

- Annual plan should always be the highlighted default on every paywall
- Show monthly-equivalent price for annual ("Just $4.99/month")
- Price anchoring: Show monthly plan price first, then annual savings
- Frame daily cost: "Less than $0.XX per day" makes any subscription feel accessible
- Introductory pricing: First year at discount converts more, then retain at full price

### Price Anchoring Techniques

Show the most expensive option first to anchor perception. Use decoy pricing: a 6-month plan priced nearly as high as annual makes the annual plan the obvious deal. Frame pricing around what the user loses by not subscribing (loss aversion).

---

## The Value-Based Pricing Process

### Step 1: Identify Target Customer Segments

Not all customers perceive the same value. Before researching price, segment your market:

**Segmentation dimensions:**
- **Usage intensity:** How much they use the product (daily vs. weekly vs. monthly)
- **Use case:** What job they hire the product for
- **Budget context:** Individual consumer vs. family vs. organization
- **Price sensitivity:** How important price is in their decision
- **Feature needs:** Which features they use or would use

### Step 2: Research Willingness to Pay

**Method A: Van Westendorp Price Sensitivity Meter (PSM)**

Requires: 200+ respondents per segment. Time: 2-4 weeks for survey design, fielding, and analysis.

**Survey design:**
1. Present the product offering (feature set of the tier being priced)
2. Ask four questions:
   - "At what monthly price would [product] be so inexpensive that you would question its quality?"
   - "At what monthly price would you consider [product] to be a bargain -- a great buy for the money?"
   - "At what monthly price would [product] begin to seem expensive, although you might still consider buying it?"
   - "At what monthly price would [product] be too expensive, and you would definitely not buy it?"
3. Collect demographic/behavioral data for segmentation

**Analysis:**
Plot four cumulative distribution curves. Key intersections:
- **Indifference Price Point (IPP):** Where "too cheap" = "too expensive" -- neutral price
- **Optimal Price Point (OPP):** Where "too cheap" = "expensive but acceptable" -- revenue-maximizing
- **Range of Acceptable Prices:** Between point of marginal cheapness and point of marginal expensiveness

**Interpretation example:**
```
Too Cheap intersects Expensive at: $6.99  (Point of Marginal Cheapness)
Too Cheap intersects Too Expensive at: $9.99  (Optimal Price Point)
Cheap intersects Too Expensive at: $12.99  (Point of Marginal Expensiveness)

Acceptable range: $6.99 - $12.99
Optimal price: $9.99
```

**Method B: Gabor-Granger Direct Pricing**

Requires: 100+ respondents per segment. Time: 1-2 weeks.

**Survey design:**
1. Present the product offering
2. "Would you subscribe to [product] for $X per month?" (YES/NO)
3. If YES: repeat at $X + increment
4. If NO: repeat at $X - increment
5. Find each respondent's maximum WTP

**Analysis:**
Plot a demand curve showing % who would buy at each price point. Calculate revenue-maximizing price: Price x Volume at that Price.

**Method C: Conjoint Analysis (Most Rigorous)**

Requires: 300+ respondents, statistical expertise. Time: 4-8 weeks.

How it works:
1. Define product attributes and levels (features, price points, content types)
2. Create choice scenarios with different combinations
3. Ask respondents to choose preferred option in each scenario
4. Statistical analysis reveals utility/importance of each attribute
5. Price sensitivity is derived from tradeoffs respondents make

Best for: Testing feature packaging alongside pricing.

### Step 3: Identify the Value Metric

**Value metric selection criteria:**

| Criterion | Test Question | Weight |
|---|---|---|
| Easy to understand | Can a customer explain what they are paying for in one sentence? | High |
| Aligns with value | As the customer gets more value, does the metric naturally increase? | High |
| Predictable | Can the customer predict their bill before they get it? | Medium |
| Scales | Does the metric grow as the customer succeeds? | High |
| Measurable | Can you accurately measure and bill on this metric? | High |

**The ProfitWell 10-5-20 Rule:**
When evaluating a potential value metric, survey customers:
- <10% should find it confusing ("I don't understand what I'm paying for")
- >5x more likely to convert when aligned to perceived value
- >20% higher willingness to pay compared to flat/arbitrary pricing

If the metric does not pass these thresholds, it is the wrong metric.

**Value Metric Evolution:**
```
Stage 1 (Startup): Flat rate -- simple, easy to sell
Stage 2 (Growth): Feature tiers -- segment by needs
Stage 3 (Scale): Usage + tiers -- capture more value from power users
Stage 4 (Mature): Platform + usage + tiers -- multi-product complexity
```

Consumer subscription products typically stay at Stage 1-2, adding a family tier as the primary expansion mechanism.

**Common value metrics for consumer content products:**

| Metric | Example | Fit for Content Apps |
|---|---|---|
| Flat monthly/annual | Netflix, Spotify | High -- simple, content-based |
| Per user/seat | Family plans | Medium -- for family tier only |
| Per content piece | Pay-per-view, Audible credits | Low -- friction per transaction |
| Usage-based | Metered content | Low -- punitive for daily habit |
| Tiered feature access | Calm (basic/premium) | High -- natural tier differentiator |

### Step 4: Set Price Points

**Revenue maximization formula:**
```
Revenue at Price P = Customers willing to pay P x P
Optimal Price = argmax(Customers(P) x P)
```

**Pricing strategies within the acceptable range:**

| Strategy | Where to Price | When to Use |
|---|---|---|
| Penetration | Bottom of acceptable range | New market, need rapid adoption |
| Neutral | Middle (optimal price) | Established product, balanced growth |
| Skimming | Top of acceptable range | Premium positioning, strong brand |

### Step 5: Validate with Data

After setting prices, validate through:
1. A/B testing pricing pages (different price points with new users)
2. Cohort analysis (do users acquired at different prices retain differently?)
3. Revenue per lead (total revenue from a cohort, accounting for conversion rate AND price)
4. Churn analysis by price (do higher-priced plans have different churn patterns?)

---

## Pricing Psychology

### The Psychology of Price Endings

- **$9.99 vs. $10.00:** The left-digit effect. $9.99 is perceived as significantly cheaper.
- **$X.99 vs. $X.95:** Minimal difference. $X.99 is standard for digital products.
- **Round numbers ($10, $15):** Signal quality/premium. Use for higher-tier plans.

### Decoy Pricing

The decoy effect: adding a third option that is clearly inferior to one of the other options makes that option more attractive.

```
Without decoy:
  Monthly: $9.99    Annual: $79.99 (33% savings)
  Many choose monthly (lower commitment)

With decoy:
  Monthly: $9.99    6-month: $54.99    Annual: $79.99
  6-month plan is the "decoy" -- nearly as expensive as annual but much less savings
  More people choose annual (feels like the obvious deal)
```

### Loss Aversion in Pricing

Frame pricing around what the user loses by not subscribing, not just what they gain:

**Weak framing:** "Get access to 1,000+ engagement sessions for $8.99/month"
**Strong framing:** "Your daily daily practice, always ready -- for less than a coffee"
**Loss aversion framing:** "Don't miss tomorrow's engagement session -- continue your premium access"

---

## Tier Packaging Design

### Feature Allocation Decision Matrix

For each feature, decide which tier gets it:

| Feature Type | Tier Placement | Rationale |
|---|---|---|
| Core value features | GOOD (free) | Must be in free tier to drive activation |
| Activation-critical features | GOOD (free) | Required to reach aha moment |
| Differentiation features | BETTER (paid) | These are the "reasons to upgrade" |
| Convenience features | BETTER (paid) | Nice-to-have that many users want |
| Power user features | BEST (premium) | Advanced needs of most engaged users |
| Admin/sharing features | BEST (premium) | Multi-user/org features at premium |

### The Feature Allocation Process

**Step 1: List all features.** Create an exhaustive list of current and planned features.

**Step 2: Categorize by WTP impact.** For each feature, determine: Does gating this feature increase or decrease free-to-paid conversion? Does including it in free help or hurt activation? Is this a "reason to upgrade" that customers cite?

**Step 3: Apply the "1-2-3 Rule."**
- GOOD tier: 1 core value experience (the minimum to demonstrate value)
- BETTER tier: 2 major upgrades over GOOD (the clear reasons to pay)
- BEST tier: 3 exclusive extras over BETTER (premium differentiation)

**Step 4: Test and iterate.** Run surveys or experiments to validate packaging.

### Content-Based Tier Differentiation

| Dimension | GOOD (Free) | BETTER (Premium) | BEST (Family) |
|---|---|---|---|
| Content volume | Limited daily selection | Full catalog | Full catalog |
| Content types | 1 type (e.g., audio) | All types (audio, video, text, guided) | All types + exclusive |
| Personalization | Basic | Full recommendations | Individual profiles per member |
| Ads | Yes | No | No |
| Offline access | No | Yes | Yes |
| Sharing | Limited or none | Personal sharing | Family sharing (up to 6) |
| Community features | View only | Participate | Create groups, lead |

### Add-On and Expansion Packaging

**Add-on types:**
- Feature add-ons: Extra features not in standard tiers (e.g., partner leader tools)
- Content add-ons: Premium content collections beyond standard library
- Usage add-ons: Expanding limits within a tier (e.g., additional family members)

**Add-on pricing strategy:**
- Price at 10-25% of the base subscription
- Base tier should feel complete without add-ons
- Add-ons should never be essential features extracted from base tier (creates resentment)
- Maximum 2-3 add-ons before complexity becomes a problem

### Bundling vs. Unbundling

**Bundle when:**
- Features are used by overlapping user segments
- Individual features have low standalone WTP but high combined WTP
- You want to simplify the purchase decision

**Unbundle when:**
- Distinct segments want very different things
- Some features have high standalone WTP
- Bundling forces low-value users to pay for unused features

### Packaging Anti-Patterns

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Free tier too generous | Low conversion -- no reason to upgrade | Gate 2-3 key features that drive upgrade intent |
| Free tier too restrictive | Low activation -- users can't reach aha moment | Ensure aha moment is achievable on free tier |
| Too many tiers | Decision paralysis, confusion | Maximum 3-4 tiers for consumer products |
| Features split illogically | Users feel nickel-and-dimed | Bundle related features, test with users |
| No clear upgrade trigger | Users don't know when to upgrade | Create in-product moments that showcase premium value |
| Best tier never purchased | Pricing anchor not working | Research what power users actually want |

---

## Pricing Experiments

### Why Experiment with Pricing

Campbell's data shows that companies who actively experiment with pricing grow revenue 2-3x faster than those who set-and-forget. Most companies run hundreds of A/B tests on acquisition but zero experiments on pricing.

### Types of Pricing Experiments

**1. New User Price Testing**
Test different prices on new users who have no price expectation.

```
Control:  $8.99/month (current price)
Variant A: $9.99/month (+$1.00)
Variant B: $7.99/month (-$1.00)

Sample: New visitors to pricing page
Duration: 2-4 weeks (or until statistical significance)
Primary metric: Revenue per visitor (conversion rate x price)
Secondary metric: D30 retention
```

Key insight: The goal is not to maximize conversion rate -- it is to maximize revenue per visitor. A 10% price increase with a 5% conversion drop is a net win.

**2. Packaging Experiments**
Test different feature allocations across tiers.

```
Control:  Current packaging (2 tiers: Free, Premium)
Variant A: 3 tiers (Free, Premium, Family)
Variant B: 3 tiers with different feature allocation

Duration: 4-6 weeks
Primary metric: ARPU across all tiers
Secondary metric: Tier distribution, upgrade rate within 30 days
```

**3. Discount Experiments**
Test the impact of different discount levels on annual plan adoption.

```
Control:  20% annual discount
Variant A: 25% discount
Variant B: 33% discount
Variant C: 15% discount

Duration: 4-8 weeks
Primary metric: Annual plan adoption rate
Secondary metric: Total revenue per user over 12 months
```

Key insight: Deeper annual discounts increase adoption but decrease per-user revenue. The optimal point balances adoption against revenue loss. Measure whether annual subscribers retain better -- if so, the discount pays for itself through reduced churn.

**4. Free Trial Length Experiments**
```
Control:  7-day free trial
Variant A: 3-day free trial
Variant B: 14-day free trial
Variant C: No free trial (freemium only)

Duration: 6-8 weeks
Primary metric: Trial-to-paid conversion rate
Secondary metric: Revenue per signup
```

Common findings: Shorter trials (3-7 days) have higher conversion rates per trial start. Longer trials (14-30 days) have lower conversion rates but higher absolute conversions (more people start). Optimal length depends on time-to-aha-moment.

**5. Price Increase Tests**
Gradually introduce higher pricing for new users while grandfathering existing.

Important principles:
- NEVER show different prices to users who can compare
- Only test on new users who have no price expectation
- Grandfather ALL existing users at their current price
- If testing in a specific market, ensure geo-segmentation

---

## Experiment Design Best Practices

### Statistical Rigor

**Sample size:** Pricing experiments need larger samples than typical A/B tests because conversion is a low-frequency event. Typical requirement: 5,000-20,000 visitors per variant.

**Duration:** Run for at least 2 full billing cycles. Minimum 4 weeks, ideally 6-8 weeks.

### Metrics Hierarchy

**Primary: Revenue per Visitor (RPV)**
```
RPV = Conversion Rate x Average Price Paid
```
This is the single most important metric.

**Secondary: Lifetime Revenue per Visitor (LRPV)**
```
LRPV = RPV x Average Retention Duration
```
Price changes may affect retention. Measure LRPV at D30, D60, D90.

**Tertiary: Qualitative Signals**
- Support tickets about pricing
- App store reviews mentioning price
- Social media sentiment about pricing
- Cancel reason data (% citing price)

### Common Pricing Experiment Mistakes

| Mistake | Consequence | Prevention |
|---|---|---|
| Under-powered test | Inconclusive results | Calculate sample size BEFORE launching |
| Measuring only conversion rate | Miss revenue impact | Always use RPV as primary metric |
| Not accounting for retention | Higher price may attract different profile | Track D30-D90 retention by variant |
| Testing too many variables | Cannot attribute results | Change one variable at a time |
| Short test duration | Misses billing cycle effects | Minimum 4 weeks, ideally 6-8 |
| No grandfather plan | Existing users see change and churn | Always grandfather existing customers |

---

## Pricing Experiment Analysis Template

```
EXPERIMENT: [Name]
DATE: [Start] - [End]
SAMPLE: [Size per variant]

VARIANTS:
- Control: [Description, price]
- Variant A: [Description, price]
- Variant B: [Description, price]

RESULTS:
| Metric | Control | Variant A | Variant B | Winner |
|--------|---------|-----------|-----------|--------|
| Conversion Rate | X% | X% | X% | |
| Average Price | $X | $X | $X | |
| RPV | $X | $X | $X | |
| D30 Retention | X% | X% | X% | |
| LRPV (90-day) | $X | $X | $X | |
| Significance | -- | p=X | p=X | |

DECISION: [Ship variant X / No change / Further testing needed]
RATIONALE: [Why]
NEXT STEP: [Follow-up experiment or implementation plan]
```

---

## Pricing Experimentation Roadmap

### Phase 1: Foundation (Month 1-2)

**Experiment 1: Annual Discount Optimization**
- Test 20%, 25%, and 33% annual discounts
- Goal: Find the annual discount that maximizes 12-month RPV

**Experiment 2: Free Trial Length**
- Test 3-day, 7-day, and 14-day free trials
- Goal: Find the trial length that maximizes trial-to-paid conversion

### Phase 2: Packaging (Month 3-4)

**Experiment 3: Family Tier Introduction**
- Control: Current 2-tier (Free + Premium)
- Variant: 3-tier (Free + Premium + Family)
- Goal: Measure ARPU lift from Family tier adoption

**Experiment 4: Free Tier Feature Allocation**
- Test different feature sets in the free tier
- Goal: Minimum free tier that preserves activation while maximizing upgrade intent

### Phase 3: Price Optimization (Month 5-6)

**Experiment 5: Price Point Testing**
- Test current price, +15%, and +25% on new users
- Goal: Find the revenue-maximizing price point
- Measure: RPV and LRPV (90-day)

**Experiment 6: Pricing Page Design**
- Test different pricing page layouts, CTA copy, and social proof elements
- Goal: Maximize pricing page conversion rate at established price point

---

## Ethical Considerations in Pricing Experiments

### What Is Acceptable

- Testing different prices on new users who have no price expectation
- Testing different packaging structures for new users
- Offering different discounts or promotions to different user segments
- Geographic pricing reflecting purchasing power
- Grandfathering existing customers at their current price

### What Is Not Acceptable

- Showing different prices to users in the same market who can compare
- Raising prices on existing customers without notice
- Bait-and-switch (advertising one price, charging another)
- Price discrimination based on protected characteristics
- Dynamic pricing that changes moment-to-moment based on user behavior

### Best Practices

1. **Always grandfather.** Existing customers keep their price.
2. **Be transparent.** If asked, explain that pricing may vary by market or offer.
3. **Do not exploit.** Never charge more based on urgency, desperation, or personal data.
4. **Test meaningful ranges.** $8.99 vs $9.99 is fine. $8.99 vs $29.99 is not a test -- it is a different product.
5. **Measure downstream effects.** If a pricing change increases short-term revenue but damages trust, it is not worth it.

---

## Implementing Price Changes

### Rolling Out a Price Increase

1. Announce 30-60 days before for existing customers (if applicable)
2. Frame as value increase: "We're adding [new features] and adjusting pricing to reflect the expanded value"
3. Grandfather loyally: Existing annual subscribers keep current price through their renewal
4. Monitor closely: Watch churn rate, support tickets, and app store reviews for 30 days
5. Have a save offer ready for customers who threaten to cancel due to price

### Rolling Out New Packaging

1. Launch for new users immediately -- cleanest execution
2. Migrate existing users gradually -- do not force change
3. Communicate the benefits -- "New plans, more options, same great content"
4. Map existing users to closest new tier -- never downgrade without consent
5. Offer one-time upgrade incentive

---

## Pricing Page Design Principles

1. **Show 3 options** (Good/Better/Best). 2 is not enough context. 4+ is overwhelming.
2. **Highlight the recommended plan** with visual emphasis (border, badge, color).
3. **Show annual pricing as default** with monthly as toggle/alternate.
4. **Display savings clearly** ("Save 33% with annual plan").
5. **Include social proof** (subscriber count, star rating).
6. **Add a FAQ** addressing common objections (cancellation policy, what's included).
7. **Mobile-first design** -- most consumer subscription purchases happen on mobile.

### Measuring Packaging Success

| Metric | What It Tells You | Target Direction |
|---|---|---|
| Free-to-paid conversion rate | Is the free tier motivating upgrades? | Increase |
| Tier distribution | Which tier are most customers choosing? | Majority on BETTER |
| ARPU | Is packaging capturing enough value? | Increase |
| Upgrade rate | Are free/BETTER users moving to higher tiers? | Increase |
| Downgrade rate | Are higher-tier users finding less value? | Decrease |
| Time to upgrade | How long before free users convert? | Decrease |
| Feature utilization by tier | Are paid features actually being used? | High for paid features |
| Churn rate by tier | Do tiers retain differently? | BEST retains best |
