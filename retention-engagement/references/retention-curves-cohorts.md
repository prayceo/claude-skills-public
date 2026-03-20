## Contents
- Understanding Retention Curves
  - How to Read a Retention Curve
  - The Four Curve Shapes
- Cohort Analysis Mechanics
  - What Is a Cohort?
  - Building a Retention Cohort Table
  - Reading the Cohort Table
  - Cohort Analysis Best Practices
- Retention Benchmarks by Product Type
  - Consumer Apps (General)
  - Consumer Subscription (Daily Content)
  - Target Benchmarks
- Flattening the Curve: Strategies
  - Strategy 1: Improve Activation
  - Strategy 2: Strengthen the Core Loop
  - Strategy 3: Content and Feature Expansion
  - Strategy 4: Re-engagement Systems
- Advanced: Retention Accounting
  - The Retention Accounting Framework
  - Retention Accounting for your product
- Cohort Analysis Workflow: Step-by-Step
  - Step 1: Define "Active"
  - Step 2: Choose Cohort Definition
  - Step 3: Build the Table
  - Step 4: Identify Patterns
  - Step 5: Set Targets and Track
- Common Retention Analysis Mistakes

---
# Retention Curves & Cohort Analysis — Deep Reference
*Source: Casey Winters, "Retention is the King," caseyaccidental.com (2019); "The Three Retention Stages," caseyaccidental.com (2020); Mastering Retention & Engagement course syllabus*

---

## Understanding Retention Curves

A retention curve plots the percentage of a user cohort that remains active over time. It is the single most important chart in product analytics.

### How to Read a Retention Curve

The X-axis represents time since the user's first activity (Day 0, Day 1, Day 7, Day 14, Day 30, Day 60, Day 90).
The Y-axis represents the percentage of the original cohort still active.

```
100% |*
     | \
     |  \
     |   \
     |    \_ _ _ _ _ _ _ _    ← Healthy: flattens at ~25%
     |
     |     \
     |      \
     |       \
     |        \
     |         \_ _ _ _       ← OK: flattens at ~10%
     |
     |           \
     |            \
     |             \
     |              \         ← Sick: approaches 0%, never flattens
   0%|________________________
     D0  D1  D7  D14 D30 D60 D90
```

### The Four Curve Shapes

**1. Flattening (Healthy)**
- Characteristics: Sharp initial drop, then stabilizes at a meaningful percentage
- What it means: A subset of users find lasting value
- Action: Expand the stable cohort (improve activation) and reduce initial drop-off

**2. Declining (Product Problem)**
- Characteristics: Continuous decline, never stabilizes
- What it means: No user segment finds lasting value
- Action: This is a product-market fit issue. Do not try to fix with growth tactics.

**3. Smile (Re-engagement Working)**
- Characteristics: Drops, then partially recovers
- What it means: Re-engagement efforts are working -- lapsed users return
- Rare; seen in products with strong notification/email systems or seasonal patterns
- Action: Invest more in re-engagement systems

**4. Staircase (Periodic Use)**
- Characteristics: Drops between usage occasions, spikes during them
- What it means: Product has periodic (not daily) use cases
- Examples: Tax software, travel booking, event ticketing
- Action: Optimize for return at the natural cadence, not forced daily use

---

## Cohort Analysis Mechanics

### What Is a Cohort?

A cohort is a group of users defined by a shared characteristic, most commonly the date they first used the product.

**Time-based cohorts:** Users grouped by signup date (Week 1, Week 2, Week 3...)
**Behavioral cohorts:** Users grouped by actions taken (completed onboarding, used feature X, subscribed)
**Segment cohorts:** Users grouped by characteristics (geography, platform, acquisition source)

### Building a Retention Cohort Table

```
            Week 0  Week 1  Week 2  Week 3  Week 4  Week 5
Jan 1-7     100%    45%     30%     25%     22%     20%
Jan 8-14    100%    42%     28%     23%     20%     —
Jan 15-21   100%    48%     32%     27%     —       —
Jan 22-28   100%    44%     29%     —       —       —
Feb 1-7     100%    50%     —       —       —       —
```

### Reading the Cohort Table

**Down a column (same week, different cohorts):** Are newer cohorts retaining better or worse?
- Improving: Product or onboarding changes are working
- Declining: Something is getting worse (content quality, market saturation, bugs)

**Across a row (same cohort, over time):** How does a single cohort behave over time?
- Flattening: Healthy retention for that cohort
- Continuous decline: That cohort never found lasting value

**Diagonal patterns:** Can reveal seasonal effects or external events

### Cohort Analysis Best Practices

1. **Always look at cohort retention, not aggregate retention.** Aggregate retention can be misleading because new user signups mask churn of older users.

2. **Use weekly or monthly cohorts, not daily** (unless DAU is very large). Daily cohorts are noisy.

3. **Look at both short-term and long-term retention.** D1/D7 measures activation. D30/D60/D90 measures product value.

4. **Segment cohorts by acquisition source.** Paid users, organic users, and referred users retain differently.

5. **Track cohorts by "did X in first week" vs. "didn't do X."** This reveals which first-week actions predict retention.

---

## Retention Benchmarks by Product Type

### Consumer Apps (General)

| Timeframe | Weak | Average | Strong | Best-in-Class |
|---|---|---|---|---|
| D1 | < 25% | 25-35% | 35-50% | 50%+ |
| D7 | < 10% | 10-20% | 20-30% | 30%+ |
| D30 | < 5% | 5-10% | 10-20% | 20%+ |
| D90 | < 2% | 2-5% | 5-15% | 15%+ |

### Consumer Subscription (Daily Content)

Products like meditation apps, daily content apps, habit apps:

| Timeframe | Weak | Average | Strong | Best-in-Class |
|---|---|---|---|---|
| D1 | < 30% | 30-40% | 40-55% | 55%+ |
| D7 | < 15% | 15-25% | 25-35% | 35%+ |
| D30 | < 8% | 8-15% | 15-25% | 25%+ |
| D90 | < 4% | 4-10% | 10-20% | 20%+ |

### Target Benchmarks

As a consumer subscription app, Your product should target:
- D1: 50%+ (high bar -- engagement session should complete in first session)
- D7: 30%+ (daily habit forming by end of week 1)
- D30: 20%+ (subscribers and committed users)
- D90: 15%+ (long-term retained base)

---

## Flattening the Curve: Strategies

### Strategy 1: Improve Activation

The biggest drop occurs in the first days. Improving activation moves the flattening point higher.

**Tactics:**
- Reduce time to first core action (< 2 minutes for consumer apps)
- Personalize onboarding based on user intent (what brought you here?)
- Remove optional setup steps from the critical path
- Pre-populate content/data so users see value immediately
- Test onboarding flows with A/B experiments (measure D7, not just completion)

### Strategy 2: Strengthen the Core Loop

If users are activated but still churn in Week 2-4, the core engagement loop is weak.

**Tactics:**
- Ensure the core action has a clear trigger (notification, habit cue)
- Increase reward variability (new content, social feedback, progress)
- Build investment mechanisms (streaks, preferences, saved content)
- Reduce friction in the return path (deep links, cached state, fast loading)

### Strategy 3: Content and Feature Expansion

For retained users who begin to churn at D60-D90, the product may be running out of new value.

**Tactics:**
- Expand content catalog (new content types, new creators, new topics)
- Add depth features for power users (advanced settings, community, creation tools)
- Create progression systems (courses, levels, collections)
- Build social features that create new reasons to engage (groups, discussions)

### Strategy 4: Re-engagement Systems

For users who have already lapsed, re-engagement can create a "smile curve" effect.

**Tactics:**
- Email/push campaigns targeted at dormant users with high-value content
- "Here's what you missed" summaries for returning users
- Seasonal re-engagement (holiday content, New Year resolution timing)
- Win-back offers (free extended trial, temporary premium access)

---

## Advanced: Retention Accounting

### The Retention Accounting Framework

At any given time, your active user base is composed of:

```
Active Users(t) = New Users(t) + Retained Users(t) + Resurrected Users(t) - Churned Users(t)
```

Understanding which component is changing explains growth or decline:

| Scenario | Diagnosis |
|---|---|
| Active growing, mostly from new users | Growth is acquisition-driven; fragile if acquisition slows |
| Active growing, mostly from retained | Healthy organic growth; sustainable |
| Active growing from resurrection | Re-engagement working, but masking an activation problem |
| Active declining despite constant new users | Retention crisis; churning faster than acquiring |

### Retention Accounting for your product

Track monthly:
- How many new users joined this month?
- How many existing users remained active?
- How many previously inactive users returned?
- How many previously active users became inactive?

This decomposition reveals whether growth is sustainable or fragile.

---

## Cohort Analysis Workflow: Step-by-Step

### Step 1: Define "Active"
What does it mean to be "active" for your product?
- your product: Completed at least one engagement session in the measurement period
- This definition matters enormously. "Opened the app" is too loose. "Completed a engagement session and shared" is too restrictive.

### Step 2: Choose Cohort Definition
- Primary: Signup week
- Secondary: Acquisition source (organic, paid, referral)
- Behavioral: Users who completed first engagement session in Day 1 vs. Day 2+ vs. never

### Step 3: Build the Table
- Rows: Cohorts (by signup week)
- Columns: Weeks since signup
- Cells: % of cohort still "active"

### Step 4: Identify Patterns
- Are newer cohorts retaining better? (Product improvements working)
- Where is the biggest drop-off? (D1-D7 = activation; D7-D30 = engagement; D30+ = value)
- Do behavioral cohorts retain differently? (If so, drive more users to the winning behavior)

### Step 5: Set Targets and Track
- Set retention targets for each timeframe
- Track weekly whether new cohorts hit targets
- Alert if any cohort falls below threshold (indicating regression)

---

## Common Retention Analysis Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Using aggregate DAU/MAU as retention metric | Masks churn with new user growth | Use cohort-specific retention rates |
| Defining "active" as "opened app" | Too loose; captures accidental opens | Define based on core action completion |
| Only looking at D1 and D30 | Misses the shape between them | Track D1, D3, D7, D14, D30, D60, D90 |
| Comparing absolute numbers across cohorts | Larger cohorts look better | Always use percentages |
| Not segmenting by acquisition source | Paid users retain differently than organic | Segment cohorts and compare |
| Celebrating improving retention when acquisition is shrinking | Survivorship bias -- only best users remain when acquisition tightens | Control for acquisition volume changes |
