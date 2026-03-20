## Contents
- Churn Taxonomy -- Complete Classification
  - Type 1: Involuntary Churn (Payment Failure)
  - Type 2: Voluntary Active Churn
  - Type 3: Voluntary Passive Churn (Disengagement -> Cancel)
- The Save Flow -- Detailed Implementation
  - Save Flow Architecture
  - Save Flow Benchmarks
- LTV Modeling -- Complete Guide
  - Method 1: Simple LTV (Steady-State)
  - Method 2: Cohort-Based LTV
  - Method 3: LTV by Plan Type
  - Method 4: Segmented LTV
  - LTV/CAC by Channel Analysis
- Retention System Design
  - The Retention Stack
  - Engagement Scoring Model
  - Retention Calendar Template

---
# Churn Diagnosis, Retention & LTV Modeling -- Deep Reference
*Sources: Phil Carter, Mastering Consumer Subscription Growth; Patrick Campbell, ProfitWell Blog*

---

## Churn Taxonomy -- Complete Classification

### Type 1: Involuntary Churn (Payment Failure)

**Causes:**
- Credit card expiration
- Insufficient funds
- Bank-flagged transaction
- Payment processor error
- Changed payment method not updated

**Typical percentage:** 20-40% of all churn in consumer subscription apps

**Recovery strategies:**

| Strategy | Implementation | Expected Recovery |
|----------|---------------|-------------------|
| Smart retry | Retry on 1st, 15th, and payday of month | 15-25% of failures |
| Pre-expiration email | Email 30 days before card expiry | 30-50% update their card |
| In-app prompt | Banner when card is about to expire | 20-30% update |
| Grace period | Continue access for 7 days during retry | Reduces frustration churn |
| Alternative payment | Offer PayPal, Apple Pay as fallback | 5-10% of failures |

**Dunning sequence template:**
```
Day 0: Payment fails -> Auto-retry immediately
Day 1: Email: "Payment issue -- update your card to keep access"
Day 2: Push notification: "Action needed -- keep your subscription active"
Day 3: Auto-retry #2
Day 4: In-app banner persistent until resolved
Day 7: Auto-retry #3
Day 7: Email: "Last chance to keep your subscription"
Day 10: If still failed -> subscription paused (not canceled)
Day 14: Final retry -> if failed, subscription canceled
Day 15: Win-back email with easy resubscribe link
```

### Type 2: Voluntary Active Churn

**Sub-type A: Value Churn ("Not worth the price")**

Diagnostic signals:
- User engages but cancels citing price
- User downgrades plan before canceling
- Cancel survey: "Too expensive" is top reason
- User has been paying for 3+ months (they tried it)

Intervention strategies:
- Downsell to lower tier
- Annual lock-in: "Switch to annual and save 50%"
- Demonstrate unrealized value: "Did you know you have access to [unused feature]?"
- Re-evaluate whether price is genuinely too high for delivered value

**Sub-type B: Use-case Churn ("Don't need this anymore")**

Diagnostic signals:
- Usage declined over time before cancellation
- Life event changes (moved, changed routine, seasonal)
- Cancel survey: "Not using it enough" or "Life changed"

Intervention strategies:
- Pause option: "Pause for 1-3 months instead of canceling"
- Flexible usage: Different content for different life stages
- Re-engagement before cancel: Detect declining usage, intervene early
- Seasonal content matched to life changes

**Sub-type C: Competitive Churn ("Found something better")**

Diagnostic signals:
- Abrupt cancellation (no gradual decline)
- Cancels after competitor launches feature
- Cancel survey: "Switched to [competitor]"

Intervention strategies:
- Competitive feature parity (if warranted)
- Differentiation emphasis: What you do that they don't
- Community lock-in: Relationships that don't transfer
- Content exclusivity: Creators/series only available here

**Sub-type D: Experience Churn ("Product frustrated me")**

Diagnostic signals:
- Support tickets before cancellation
- App store reviews mentioning bugs/issues
- Cancel survey: "Technical issues" or "Poor experience"

Intervention strategies:
- Fix the bugs/issues (obvious but often deprioritized)
- Proactive outreach after support tickets
- Apology + free month as retention tool
- Regular UX audits focused on friction points

### Type 3: Voluntary Passive Churn (Disengagement -> Cancel)

This is the largest category for most consumer subscription apps and the hardest to address because the user has already mentally left before they formally cancel.

**The disengagement cascade:**
```
Week 1-2: Usage frequency drops (7 days/week -> 3-4 days)
Week 2-4: Usage depth drops (full content -> quick glance -> nothing)
Week 4-8: Product forgotten (no opens, notifications ignored)
Week 8-12: User notices charge, considers canceling
Week 12+: User cancels or lets subscription lapse
```

**Early warning system -- detect disengagement BEFORE it leads to churn:**

| Signal | Threshold | Action |
|--------|-----------|--------|
| Days since last open | >3 days (was daily) | Trigger re-engagement notification |
| Session duration drop | <50% of average | Surface engaging content |
| Feature usage narrowing | Only using 1 feature (was 3+) | Recommend other features |
| Notification dismissal rate | >80% | Change notification strategy |
| Streak break | First break after 14+ day streak | Grace-centered welcome-back message |

---

## The Save Flow -- Detailed Implementation

### Save Flow Architecture

```
[User taps "Cancel Subscription"]
          |
          v
[Step 1: Reason Selection]
"We're sorry to see you go. What's the main reason?"
  - Too expensive
  - Not using it enough
  - Found an alternative
  - Technical issues
  - Content not relevant
  - Other: ___________
          |
          v
[Step 2: Personalized Response based on reason]
  "Too expensive" --> Offer downsell or discount
  "Not using enough" --> Offer pause, show usage tips
  "Found alternative" --> Show unique differentiators
  "Technical issues" --> Offer support contact + free month
  "Content not relevant" --> Offer to customize, show new content
  "Other" --> Offer pause option
          |
          v
[Step 3: Pause Offer (if not accepted above)]
"Instead of canceling, would you like to pause for 1-3 months?"
  Paused users reactivate at 30-50% rate
          |
          v
[Step 4: Final Offer (if still proceeding)]
"Before you go: Get 3 months at 50% off"
  Or: "Get 1 month free to reconsider"
          |
          v
[Step 5: Confirmation + Graceful Exit]
"Your subscription will end on [date]. You can keep using premium until then."
"Your engagement history and journal entries are saved."
"You can resubscribe anytime."
          |
          v
[Post-Cancel: Win-back Sequence]
Day 7: "We miss you. Here's what's new."
Day 30: "Special offer: Come back at 40% off"
Day 60: "Still thinking about us? We're here when you're ready."
Day 90: Final attempt, then quiet
```

### Save Flow Benchmarks

| Metric | Below Average | Average | Good | Excellent |
|--------|--------------|---------|------|-----------|
| Save rate (% who don't cancel) | <10% | 15-20% | 20-30% | >30% |
| Pause acceptance rate | <5% | 10-15% | 15-25% | >25% |
| Discount acceptance rate | <8% | 10-15% | 15-20% | >20% |
| Pause-to-reactivation rate | <20% | 30-40% | 40-50% | >50% |

---

## LTV Modeling -- Complete Guide

### Method 1: Simple LTV (Steady-State)

```
LTV = ARPU per month / Monthly Churn Rate

Example:
ARPU = $7.50/month (blended across monthly and annual)
Monthly Churn = 5%
LTV = $7.50 / 0.05 = $150
```

**Limitations:** Assumes constant churn rate. In reality, churn decreases over time (survivors are more engaged).

### Method 2: Cohort-Based LTV

More accurate -- uses actual retention curves:

```
LTV = Sum of (Survival Rate at month t x ARPU at month t) for t = 1 to T

Where:
Survival Rate(t) = % of original cohort still subscribed at month t
ARPU(t) = Revenue per surviving subscriber at month t
T = Reasonable time horizon (typically 24-36 months)
```

**Example calculation:**

| Month | Survival Rate | ARPU | Revenue Contribution |
|-------|--------------|------|---------------------|
| 1 | 100% | $7.50 | $7.50 |
| 2 | 90% | $7.50 | $6.75 |
| 3 | 83% | $7.50 | $6.23 |
| 6 | 65% | $7.50 | $4.88 |
| 12 | 48% | $7.50 | $3.60 |
| 18 | 40% | $7.50 | $3.00 |
| 24 | 35% | $7.50 | $2.63 |
| **24-month LTV** | | | **~$110** |

### Method 3: LTV by Plan Type

```
LTV (Monthly plan) = Monthly Price x (1 / Monthly Churn Rate)
LTV (Annual plan) = Annual Price x Average Renewal Count
Where Average Renewal Count = 1 / (1 - Annual Renewal Rate)

Example:
Monthly plan: $9.99 x (1 / 0.07) = $143 LTV
Annual plan: $59.99 x (1 / (1 - 0.70)) = $59.99 x 3.33 = $200 LTV

Blended LTV (65% annual, 35% monthly):
= (0.65 x $200) + (0.35 x $143) = $130 + $50 = $180 blended LTV
```

### Method 4: Segmented LTV

Different user segments have dramatically different LTVs:

| Segment | Monthly Churn | Est. LTV | Index vs. Average |
|---------|--------------|---------|-------------------|
| Annual plan, organic acquisition | 2% | $250 | 1.7x |
| Annual plan, paid acquisition | 3.5% | $175 | 1.2x |
| Monthly plan, organic | 5% | $120 | 0.8x |
| Monthly plan, paid | 8% | $75 | 0.5x |
| Trial converter, Day 1 | 10% | $50 | 0.3x |
| **Blended average** | **~5%** | **$150** | **1.0x** |

**Strategic implication:** The difference between your best and worst segments can be 5x+. Growing the best segments is far more valuable than growing total volume.

### LTV/CAC by Channel Analysis

| Channel | CAC | Segment LTV | LTV/CAC | Payback | Verdict |
|---------|-----|-------------|---------|---------|---------|
| Organic (ASO) | $5 | $180 | 36.0 | <1 month | Scale |
| Referral | $8 | $250 | 31.3 | 1 month | Scale |
| Wellness podcast ads | $25 | $200 | 8.0 | 3 months | Scale |
| Facebook (targeted) | $15 | $120 | 8.0 | 2 months | Optimize |
| Instagram (broad) | $12 | $80 | 6.7 | 2 months | Optimize |
| TikTok | $8 | $50 | 6.3 | 1 month | Test/watch quality |
| Broad display | $5 | $30 | 6.0 | 1 month | Cautious |

---

## Retention System Design

### The Retention Stack

Layer retention strategies across the subscriber lifecycle:

**Layer 1: Onboarding (Day 0-7)**
- Goal: Deliver on the promise; establish routine
- Tactics: Guided first experience, quick wins, setup completion
- Metric: 7-day engagement rate

**Layer 2: Habit Formation (Day 7-30)**
- Goal: Build daily usage habit
- Tactics: Streak mechanics, notification optimization, content personalization
- Metric: DAU/MAU ratio, unprompted usage rate

**Layer 3: Value Deepening (Day 30-90)**
- Goal: Increase investment and feature breadth
- Tactics: Community features, journaling, new content discovery
- Metric: Features used per session, community participation

**Layer 4: Community Lock-in (Day 90+)**
- Goal: Create switching costs through relationships
- Tactics: Community groups, accountability partners, shared experiences
- Metric: Social connections count, group participation rate

**Layer 5: Identity Integration (Day 180+)**
- Goal: Product becomes part of user identity
- Tactics: Annual journey reflections, milestone celebrations, community roles
- Metric: Organic referral rate, NPS, qualitative identity indicators

### Engagement Scoring Model

Create a composite engagement score to predict churn risk:

```
Engagement Score =
  (0.3 x Recency Score) +    // How recently they used the app
  (0.25 x Frequency Score) +  // How often they use it
  (0.25 x Depth Score) +      // How deeply they engage per session
  (0.2 x Social Score)        // How connected they are to community

Where each component is normalized to 0-100 scale
```

| Risk Level | Engagement Score | Action |
|-----------|-----------------|--------|
| Green (safe) | 70-100 | Standard experience, upsell opportunities |
| Yellow (monitor) | 40-69 | Proactive engagement nudges, content recommendations |
| Orange (at risk) | 20-39 | Re-engagement campaign, personal outreach |
| Red (likely to churn) | 0-19 | Save intervention, pause offer, discount |

### Retention Calendar Template

| Timing | Retention Action | Purpose |
|--------|-----------------|---------|
| Day 0 | Premium welcome + guided setup | Deliver immediate value |
| Day 3 | "How's your experience?" check-in | Early problem detection |
| Day 7 | Usage milestone celebration | Reinforce commitment |
| Day 14 | Community feature introduction | Deepen engagement |
| Day 30 | 1-month milestone + growth reflection | Identity reinforcement |
| Day 60 | New content series launch | Prevent content fatigue |
| Day 90 | Quarterly journey review | Value demonstration |
| Day 180 | Half-year milestone | Celebrate, prep for annual renewal |
| Day 330 | Pre-renewal value reinforcement | Reduce annual churn |
| Day 365 | Renewal day + year-in-review | Celebrate anniversary |
