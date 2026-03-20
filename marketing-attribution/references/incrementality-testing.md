## Contents
- Why Incrementality Is the Gold Standard
  - The Incrementality Question
  - Why Organic Cannibalization Matters
- Incrementality Test Designs
  - Design 1: Geo-Lift Test
  - Design 2: Conversion Lift Study (Platform-Native)
  - Design 3: Matched Market Test
  - Design 4: Holdout Test (Simple On/Off)
- Incrementality Test Planning Template
  - Pre-Test Checklist
  - Test Documentation Template
- Incrementality Testing Calendar
- Common Mistakes
  - Testing Mistakes
  - Interpretation Mistakes
- Application to your product

---
# Incrementality Testing — Deep Reference
*Source: Pranav Piyush, Mastering Marketing Attribution*

---

## Why Incrementality Is the Gold Standard

Attribution tells you who touched the customer. Incrementality tells you whether the marketing actually caused the conversion. This is the fundamental difference between correlation and causation in marketing measurement.

### The Incrementality Question

For any marketing channel or campaign, the question is:
"How many conversions happened BECAUSE of this marketing that would NOT have happened otherwise?"

```
Incremental conversions = Total conversions with marketing - Total conversions without marketing
```

Conversions that would have happened anyway (organic demand captured by marketing) are NOT incremental. They represent organic cannibalization — you're paying for conversions you'd get for free.

### Why Organic Cannibalization Matters

Most marketing channels experience some organic cannibalization:

| Channel | Typical Organic Cannibalization | Explanation |
|---------|-------------------------------|-------------|
| Branded search (Google) | 50-80% | Users searching your brand name would likely navigate to you anyway |
| Retargeting | 30-60% | Users who already visited your site have high baseline conversion |
| Meta (broad targeting) | 20-40% | AI optimization targets users likely to convert anyway |
| Meta (lookalike/interest) | 10-30% | More targeted, higher incrementality |
| Influencer | 10-30% | New audience exposure, higher incrementality |
| TV | 5-15% | Broad reach, mostly new awareness |
| Podcast | 10-25% | Niche audience, moderate overlap |

These numbers vary widely by brand, category, and competitive intensity. The only way to know YOUR organic cannibalization rate is to test incrementality.

---

## Incrementality Test Designs

### Design 1: Geo-Lift Test

**Concept:** Turn off marketing in some geographic regions while maintaining it in others. Compare outcomes.

**Step-by-step:**

1. **Select regions:**
   - Choose 15-30 geographic regions (DMAs, states, or cities)
   - Regions should be large enough to have statistically significant activity
   - Mix of test (marketing off) and control (marketing on) regions

2. **Match regions:**
   - Use pre-test data to find pairs of similar regions
   - Match on: conversion volume, growth rate, seasonality patterns, demographics
   - Statistical matching methods: propensity score matching, synthetic control

3. **Assign treatment:**
   - Randomly assign matched pairs to test vs. control
   - Test regions: pause marketing spend
   - Control regions: maintain normal marketing spend

4. **Run the test:**
   - Duration: minimum 2 weeks, ideally 4 weeks
   - Don't change anything else during the test period
   - Monitor for contamination (people in test regions seeing control region ads)

5. **Analyze:**
   ```
   Incremental lift = (Control region conversion rate) - (Test region conversion rate)
   Incremental CPA = Spend in control regions / Incremental conversions
   ```

**Advantages:**
- Privacy-safe (aggregate data only)
- Works for any channel (digital, TV, OOH, radio)
- Can test total channel impact (not just individual campaigns)

**Limitations:**
- Opportunity cost of pausing spend in test regions
- Requires enough geographic regions with sufficient volume
- Cross-region contamination possible (people travel, see digital ads outside their region)
- Seasonality and external events can confound results

### Design 2: Conversion Lift Study (Platform-Native)

**Concept:** The ad platform randomly holds back ads from a subset of your target audience. Survey or measure conversions in both groups.

**How it works on Meta:**
1. You set up a campaign as normal
2. Meta randomly selects a holdout group (typically 10-15% of your target audience)
3. Holdout group is shown a Public Service Announcement (PSA) or blank ad instead of yours
4. Meta measures conversions in both groups
5. Meta reports: incremental lift, incremental conversions, cost per incremental conversion

**Requirements:**
- Minimum spend: ~$10K over 2 weeks (varies by region)
- Minimum campaign duration: 2 weeks
- Must be running conversion campaigns (not just awareness)
- Results available 1-2 weeks after test ends

**How it works on Google:**
- Similar concept: holdout group doesn't see your ads
- Available for YouTube, Search, Display
- Requires Google team to set up (not self-serve for all)
- Measures brand lift (surveys) and conversion lift (behavioral)

**Advantages:**
- Free (platform provides)
- Randomized at the user level (most precise)
- Easy to set up
- Platform handles statistical analysis

**Limitations:**
- Only measures within that platform (doesn't capture cross-platform effects)
- Platform has incentive to show favorable results (potential bias)
- Only available for campaigns of sufficient size
- Can't test non-digital channels

### Design 3: Matched Market Test

**Concept:** Find pairs of similar markets, apply marketing treatment to one market in each pair, and compare outcomes.

**When to use:**
- When you have fewer than 15 geographic regions (too few for proper geo-lift)
- When you want to test a specific market-level initiative (new market entry, major campaign shift)

**Process:**
1. Identify potential market pairs using historical data
2. Match pairs on: volume, growth rate, demographics, seasonal patterns
3. For each pair, randomly assign one to treatment, one to control
4. Run the marketing treatment in test markets only
5. Compare outcomes between matched pairs

**Statistical methods:**
- Difference-in-differences (DiD): Compare the change in outcomes between test and control
- Synthetic control: Create a weighted combination of control markets to match each test market

### Design 4: Holdout Test (Simple On/Off)

**Concept:** The simplest form of incrementality testing. Turn off a channel completely for a period and see what happens.

**When to use:**
- When you suspect a channel has very low incrementality
- When you can't afford more sophisticated test designs
- When you need a quick directional answer

**Process:**
1. Pause a channel completely for 2-4 weeks
2. Monitor total conversions (not just attributed conversions)
3. If total conversions don't change much, the channel had low incrementality
4. If total conversions drop proportionally to attributed conversions, high incrementality

**Limitations:**
- Very blunt instrument (can't measure partial effects)
- Opportunity cost of turning off a channel
- Other channels may pick up some of the slack (substitution effects)
- Hard to attribute small changes with statistical confidence

---

## Incrementality Test Planning Template

### Pre-Test Checklist

| Item | Status |
|------|--------|
| Test hypothesis clearly defined | |
| Primary metric selected (installs, subscriptions, revenue) | |
| Test design chosen (geo-lift, conversion lift, matched market, holdout) | |
| Power analysis completed (sample size, duration) | |
| Budget for test period confirmed | |
| No conflicting experiments during test window | |
| No major promotions/launches during test window | |
| Baseline data collected (2-4 weeks pre-test) | |
| Monitoring dashboard set up | |
| Success criteria defined before test starts | |

### Test Documentation Template

**Test name:** [Channel] Incrementality Test Q[X] [Year]
**Owner:** [Name]
**Test period:** [Start date] — [End date]
**Pre-test baseline period:** [Start date] — [End date]

**Hypothesis:**
"[Channel] drives [X]% incremental conversions above organic baseline."

**Test design:** [Geo-lift / Conversion lift / Matched market / Holdout]

**Test parameters:**
- Holdout size: [X]% of audience / [N] regions
- Primary metric: [conversion event]
- Secondary metrics: [list]
- Minimum detectable effect: [X]% (from power analysis)

**Results:**
| Metric | Control Group | Test Group | Lift | Confidence Interval | Statistical Significance |
|--------|-------------|-----------|------|---------------------|-------------------------|
| | | | | | |

**Decisions based on results:**
- [ ] Adjust channel budget (increase/decrease/maintain)
- [ ] Calibrate MTA model with incrementality factor
- [ ] Update MMM priors
- [ ] Schedule follow-up test for Q[X]

---

## Incrementality Testing Calendar

For a company spending across 4-5 channels, here's a recommended annual testing calendar:

| Quarter | Test | Channel | Estimated Duration |
|---------|------|---------|-------------------|
| Q1 | Conversion Lift | #1 Paid channel (likely Meta) | 3 weeks |
| Q2 | Geo-Lift | #2 Paid channel (likely Google) | 4 weeks |
| Q3 | Conversion Lift | #1 channel re-test + new creative | 3 weeks |
| Q4 | Holdout test | Retargeting (likely low incrementality) | 2 weeks |

Rotate channels annually. Test your biggest spend channels first and most frequently.

---

## Common Mistakes

### Testing Mistakes

1. **Peeking at results early:** Running a 4-week test but checking results after 1 week and making decisions. Wait for the full duration.

2. **Confounding the test:** Running a promotion or product launch during the test period. Any change besides the marketing treatment invalidates results.

3. **Insufficient power:** Running a test on too small an audience or too short a duration. Results will be inconclusive (wide confidence intervals).

4. **Testing the wrong thing:** Testing whether Meta drives any conversions (yes, it does) vs. testing whether Meta drives conversions at the current spend level that justify the cost (the actionable question).

### Interpretation Mistakes

1. **Binary thinking:** Treating incrementality as "works or doesn't work" instead of "what's the incremental ROI?"

2. **Ignoring confidence intervals:** An incremental lift of 15% with CI [-5%, 35%] is NOT the same as 15% with CI [12%, 18%].

3. **Extrapolating:** "Channel A is incremental at $50K/month" doesn't mean it's incremental at $500K/month (diminishing returns).

4. **One-and-done:** Running one test and treating the results as permanent. Incrementality changes over time (competition, audience saturation, creative fatigue).

---

## Application to your product

Recommended incrementality testing sequence for your product:

1. **First test: Meta Conversion Lift** — Your largest paid channel. Run a 3-week conversion lift study measuring incremental app installs AND incremental subscriptions. This will reveal your true incremental CPA vs. Meta-reported CPA.

2. **Second test: Retargeting holdout** — Pause retargeting for 2 weeks and measure total subscription conversions. Retargeting often has very low incrementality for subscription apps (users who started a trial are likely to convert anyway).

3. **Third test: Branded search holdout** — Pause branded Google search ads for 2 weeks. Measure whether organic search captures most of the volume. For well-known brands, branded search ads often have 50-80% cannibalization.

4. **Fourth test: ASO/App Store holdout** (if using Apple Search Ads) — Run a geo-lift test to measure incremental installs from App Store ads vs. organic browse.
