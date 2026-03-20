## Contents
- The 7 Principles of Growth Marketing -- Expanded
  - Principle 1: Start with the Growth Model
  - Principle 2: Audience Before Channels
  - Principle 3: Messaging is the Multiplier
  - Principle 4: Measurement is the Foundation
  - Principle 5: Incrementality is the Truth
  - Principle 6: Diversification is Protection
  - Principle 7: Speed of Learning Beats Speed of Spending
- Channel Evaluation Scorecard -- Full Framework
  - Phase 1: Channel Identification
  - First-Pass Filter
  - Phase 2: Channel Scoring (5 Dimensions)
  - Phase 3: Channel Testing Protocol
  - Phase 4: Channel Optimization Hierarchy
  - Phase 5: Channel Scaling Principles
  - Phase 6: Channel Sunsetting
- Growth Loop Design -- Deep Dive
  - Loop Components
  - Loop Types for Subscription Apps
  - Loop Health Assessment
- Incrementality Testing Playbook
  - Method 1: Holdout Tests (Gold Standard)
  - Method 2: Geo-Based Tests
  - Method 3: Time-Based (On/Off) Tests
  - Method 4: Ghost Ads / PSA Tests
- Attribution Models Comparison
- Measurement Stack Architecture
- Key Metrics Reference
  - Acquisition Metrics
  - Retention Metrics
  - Monetization Metrics
  - Incrementality Metrics
- Common Measurement Pitfalls

---
# Growth Marketing, Channel Evaluation, and Measurement


---

## The 7 Principles of Growth Marketing -- Expanded

### Principle 1: Start with the Growth Model

Never start with channels. Start with the growth model -- the system of loops and levers that drive your business. Understand which inputs drive outputs and focus marketing on the highest-leverage inputs.

For a subscription app, the growth model is:
```
Acquisition --> Activation --> Retention --> Monetization --> Referral --> [loops back]
```

Map which levers growth marketing controls at each stage before selecting channels or allocating budget.

### Principle 2: Audience Before Channels

Define who you are trying to reach before deciding where to reach them. The audience determines the channel, not the other way around. Segment by behavior and need:

| Segment Type | Example |
|-------------|---------|
| Behavioral | Users who completed 3+ sessions but have not subscribed |
| Need-based | People seeking a structured daily daily practice |
| Lifecycle | Churned premium subscribers who were active for 3+ months |
| Demographic | consumer women ages 25-45 with children |

### Principle 3: Messaging is the Multiplier

Two campaigns on the same channel targeting the same audience can perform 10x differently based on messaging alone. Creative and messaging are the biggest levers once channel and audience are set. Invest in messaging strategy before scaling spend.

### Principle 4: Measurement is the Foundation

If you cannot measure it, you cannot optimize it. Invest in measurement infrastructure before scaling spend. This includes: event tracking at every growth model stage, attribution setup, cohort analysis capability, and experiment infrastructure.

### Principle 5: Incrementality is the Truth

Attribution tells you what happened. Incrementality tells you what marketing caused. Always seek incrementality over attribution. Platforms are incentivized to over-claim credit. Many attributed conversions would have happened without marketing.

### Principle 6: Diversification is Protection

Single-channel dependency is an existential business risk. Build a portfolio. Facebook's iOS 14 privacy changes, Google algorithm updates, and TikTok bans have all destroyed companies that relied on a single channel.

### Principle 7: Speed of Learning Beats Speed of Spending

The fastest-learning marketing team wins, not the biggest-spending one. Run more experiments, make decisions faster, iterate continuously. Document every learning.

---

## Channel Evaluation Scorecard -- Full Framework

### Phase 1: Channel Identification

Build a comprehensive candidate list by type:

**Paid Channels:** Paid social (Meta, TikTok, YouTube, Pinterest, Snapchat, Reddit), paid search (Google Ads, Apple Search Ads), display/programmatic, video (YouTube, CTV/OTT), podcast sponsorships, influencer marketing, affiliate.

**Owned Channels:** Email, push notifications, in-app messaging, SMS, blog/content, owned social, app store listing (ASO).

**Earned Channels:** SEO, organic ASO, PR/media, word of mouth, UGC, community/forums, app store features.

**Shared Channels:** Co-marketing partnerships, platform features (App Store Today), cross-promotions, organizational partnerships.

### First-Pass Filter

| Filter Question | If No... |
|----------------|----------|
| Does our target audience use this channel? | Eliminate |
| Can it deliver at least 1,000 monthly impressions? | Deprioritize |
| Can we create appropriate content for this channel? | Deprioritize |
| Is it legally and ethically acceptable for our brand? | Eliminate |
| Can we measure any form of outcome? | Deprioritize |

### Phase 2: Channel Scoring (5 Dimensions)

**1. Audience Fit (30% weight)**

| Score | Criteria |
|-------|----------|
| 5 | Core audience highly concentrated; precise targeting available |
| 4 | Core audience uses regularly; good targeting |
| 3 | Core audience present but mixed; moderate targeting |
| 2 | Some overlap but not a primary platform for target users |
| 1 | Minimal overlap; poor targeting |

**2. Volume Potential (20% weight)**

| Score | Criteria |
|-------|----------|
| 5 | Can deliver 10,000+ conversions/month at scale |
| 4 | 5,000-10,000 conversions/month |
| 3 | 1,000-5,000 conversions/month |
| 2 | 100-1,000 conversions/month |
| 1 | <100 conversions/month |

**3. Cost Efficiency (20% weight)**

| Score | Criteria |
|-------|----------|
| 5 | Expected CAC < 25% of first-year LTV |
| 4 | 25-50% of first-year LTV |
| 3 | 50-75% of first-year LTV |
| 2 | 75-100% of first-year LTV |
| 1 | >100% of first-year LTV |

**4. Targeting Capability (15% weight)**

| Score | Criteria |
|-------|----------|
| 5 | Granular behavioral + interest + demographic targeting |
| 4 | Strong interest and demographic targeting |
| 3 | Moderate targeting (broad categories, demographics) |
| 2 | Limited targeting (mostly contextual) |
| 1 | No targeting (mass audience only) |

**5. Measurability (15% weight)**

| Score | Criteria |
|-------|----------|
| 5 | Full-funnel attribution: impression to install to conversion |
| 4 | Install-level attribution with conversion tracking |
| 3 | Click-level tracking with some conversion attribution |
| 2 | Click tracking only, limited conversion data |
| 1 | Minimal measurement (reach/impressions only) |

### Phase 3: Channel Testing Protocol

For channels scoring above threshold (weighted score > 3.0):

**Test budget:** $1,000-5,000 per channel
**Test duration:** Minimum 14 days (accounts for day-of-week effects)

**Test structure:**
1. Define success metric (CPI, CPA, trial start cost)
2. Define success threshold (CAC must be below X)
3. Set up tracking before launching
4. Run 2-3 creative/audience variants simultaneously
5. Check daily but do not optimize until Day 7 (let algorithm learn)
6. Go/no-go decision on Day 14

**Post-test decision:**
- Hit threshold --> Move to Optimization (scale budget 2-3x over 30 days)
- Within 2x of threshold --> Extend 14 days with creative/audience adjustments
- >3x above threshold --> Sunset the channel
- Unclear cause --> Test different audience or fundamentally different creative; if still unclear, sunset

### Phase 4: Channel Optimization Hierarchy

Optimize in this order (most impactful first):

1. **Audience optimization:** Which segments convert best? Which have highest LTV? Lookalike audiences? Suppress low-value segments?
2. **Offer optimization:** What value proposition drives conversions? Trial length? Free content preview vs. feature-list ad?
3. **Creative optimization:** Format (video, static, carousel)? Hooks (question, statistic, testimonial)? Emotional tone? Refresh frequency?
4. **Bidding and budget:** Manual vs. automated? Optimization event? Day-parting? Pacing?
5. **Landing/destination:** App store, landing page, or deep link? Is destination aligned with ad message?

### Phase 5: Channel Scaling Principles

1. **Scale what is working, not what is promising.** Test results must hold at 2-3x the test budget.
2. **Scale in steps, not leaps.** Increase budget 25-50% per week. Sudden increases degrade performance.
3. **Monitor efficiency as you scale.** Track CAC and LTV at each budget level.
4. **Diversify within the channel.** New segments, creative, placements, formats delay saturation.

**Scaling signals and responses:**

| Signal | Action |
|--------|--------|
| CAC increasing >20% at current budget | Approaching saturation -- diversify creative/audience |
| Frequency >3 on same audience | Creative fatigue -- refresh urgently |
| Conversion rate declining steadily | Check landing page, creative, audience alignment |
| New user quality declining (lower retention) | Reaching lower-quality audience -- cap budget |

### Phase 6: Channel Sunsetting

Sunset when: LTV:CAC below 1.5:1 after optimization; volume too small to matter (<50 conversions/month); user quality consistently poor; team time exceeds marginal value; incrementality testing shows near-zero contribution.

Process: Reduce budget 50% for 2 weeks. If no improvement, pause completely for 2 weeks. Measure impact on organic and overall metrics. If no material impact, sunset permanently. Document learnings.

---

## Growth Loop Design -- Deep Dive

### Loop Components

Every growth loop has three parts:
1. **Input:** What triggers the loop? (new user, content, payment)
2. **Action:** What does the user do? (share, create, invite, pay)
3. **Output:** What feeds back into the loop? (new user, new content, revenue)

### Loop Types for Subscription Apps

**Viral/Social Loop:**
```
User completes meaningful content --> App prompts "Share with someone who needs this" --> Friend receives shared content with deep link --> Friend downloads and engages --> Friend shares
```
Key metric: k-factor (new users per existing user per time period)
Optimization: share prompt timing, message pre-composition, landing page conversion

**User-Generated Content Loop:**
```
User writes community request or testimony --> Content surfaces in community --> Community content attracts new users (search, social) --> New users contribute --> More content
```
Key metric: content creation rate, content-driven acquisition
Optimization: friction to create, discoverability, SEO of user content

**Paid Acquisition Loop:**
```
Subscriber pays --> Revenue reinvested in ads --> Ads acquire new subscriber --> Subscriber pays
```
Key metric: payback period
Optimization: LTV improvement, CAC reduction, payback compression

**Content/SEO Loop:**
```
Team publishes content --> Ranks in search --> Organic traffic --> App downloads --> Some convert --> Engagement signals boost rankings --> More traffic
```
Key metric: organic traffic growth, organic-to-install conversion
Optimization: keyword strategy, content quality, conversion optimization

### Loop Health Assessment

For each active loop, measure:
- **Cycle time:** How long does one complete loop take?
- **Conversion at each step:** Where is the biggest drop-off?
- **Growth rate:** Is the loop accelerating, steady, or decelerating?
- **Marginal cost:** What does it cost to add one more cycle?

---

## Incrementality Testing Playbook

### Method 1: Holdout Tests (Gold Standard)

1. Define audience eligible for marketing activity
2. Randomly assign 5-20% to holdout group (no marketing)
3. Run campaign for test group
4. Compare conversion rates: test vs. holdout
5. Difference = incremental lift

**Design principles:**
- Holdout must be randomly assigned (no cherry-picking)
- Minimum 5% of audience or 1,000 users for statistical significance
- Duration: minimum 7 days for most subscription decisions
- Do not contaminate the holdout via other channels

**When to run:**
- Any channel receiving >15% of marketing budget
- Internal debate about a channel's value
- Quarterly on largest channels
- Before major budget reallocation decisions

### Method 2: Geo-Based Tests

Select matched geographic regions. Run marketing in test regions, not control. Compare outcomes. Best for offline channels (TV, events, community partnerships) and regional budget decisions. Match carefully on population, demographics, and existing penetration. Run at least 4 weeks with 3+ regions per group.

### Method 3: Time-Based (On/Off) Tests

Alternate channel on/off in equal periods. Compare outcomes. Best for quick directional tests. Limitations: confounded by seasonality and carryover effects. Less rigorous than holdout tests.

### Method 4: Ghost Ads / PSA Tests

Show test group real ad; show control group a PSA or blank ad. Difference = your ad's specific incremental impact. Available via Meta Conversion Lift, Google Brand Lift/Search Lift, and some programmatic platforms.

---

## Attribution Models Comparison

| Model | How It Works | Best For | Weakness |
|-------|-------------|----------|----------|
| Last-touch | 100% credit to last touchpoint | Simple daily channel management | Ignores upper funnel; over-credits bottom |
| First-touch | 100% credit to first touchpoint | Understanding acquisition source quality | Ignores conversion drivers |
| Linear MTA | Equal credit to all touchpoints | Simple multi-touch, no assumptions | Over-simplifies |
| Time decay MTA | More credit to recent touchpoints | Conversion-focused analysis | Arbitrary decay rate |
| Position-based (U-shape) | 40% first, 40% last, 20% middle | Valuing both acquisition and conversion | Still somewhat arbitrary |
| Data-driven MTA | ML-determined weights | Large datasets, sophisticated teams | Black box, requires scale |
| MMM | Aggregate spend-to-outcome regression | Portfolio-level budget allocation | Slow, requires 12+ months of data |
| Incrementality | Controlled experiments | Proving causal impact | Requires experiment infrastructure |

**Recommendation by stage:**
- Early: Last-touch + "How did you hear about us?"
- Growth: Multi-touch + incrementality on biggest channels
- Scale: MMM + incrementality + multi-touch (triangulation)

---

## Measurement Stack Architecture

| Layer | Tool | Model | Use Case | Cadence |
|-------|------|-------|----------|---------|
| Daily attribution | Mobile attribution platform (AppsFlyer, Branch) | Last-touch | Channel spend allocation | Daily dashboards, weekly reviews |
| Journey analysis | Product analytics (Amplitude, Mixpanel) | Multi-touch | Understanding user paths | Weekly analysis, monthly reporting |
| Strategic validation | Internal testing framework | Holdout/geo/on-off | Validate channel ROI | Monthly on major channels |
| Portfolio allocation | MMM tool or internal model | Aggregate regression | Cross-channel budget optimization | Quarterly refresh |

---

## Key Metrics Reference

### Acquisition Metrics

| Metric | Definition |
|--------|-----------|
| CPI (Cost Per Install) | Total acquisition spend / installs |
| CPA (Cost Per Activation) | Spend / users who complete first key action |
| CPTS (Cost Per Trial Start) | Spend / users who start premium trial |
| CPS (Cost Per Subscriber) | Spend / new paying subscribers |
| Organic Install Rate | % of installs from unpaid sources |

### Retention Metrics

| Metric | Definition |
|--------|-----------|
| D1/D7/D30 Retention | % active at Day 1, 7, 30 after install |
| Push Opt-In Rate | % allowing push notifications |
| Email Engagement Rate | Open and click rates |
| Re-engagement Rate | % of lapsed users (7+ days inactive) who return |

### Monetization Metrics

| Metric | Definition |
|--------|-----------|
| Trial Start Rate | % of new users who start premium trial |
| Trial-to-Paid Rate | % of trial users who convert |
| LTV | Average total revenue per user over lifetime |
| Payback Period | Months to recover acquisition cost |
| LTV:CAC Ratio | Lifetime value / acquisition cost; target >3:1 |

### Incrementality Metrics

| Metric | Definition |
|--------|-----------|
| Incremental Conversions | Test group conversions minus holdout group conversions |
| Incremental ROAS | Incremental revenue / channel spend |
| Organic Baseline | Holdout group conversion rate |
| Lift % | (Test rate - Control rate) / Control rate |
| iCAC | Channel spend / incremental conversions |

---

## Common Measurement Pitfalls

1. **Platform self-attribution bias:** Every platform over-claims conversions. Use independent mobile measurement partner as source of truth.
2. **Organic cannibalization:** Branded paid search often cannibalizes organic installs. Run on/off tests for branded keywords.
3. **Optimizing for installs instead of revenue:** Cheap installs from incentivized sources convert at near-zero. Track downstream metrics by acquisition source.
4. **Seasonal attribution confusion:** Seasonal demand spikes (seasonal event, Advent) inflate attributed conversions. Run holdout tests during peaks.
5. **Over-crediting retargeting:** Retargeting targets users who already showed intent. Expect incremental lift to be much lower than attributed conversions suggest.
