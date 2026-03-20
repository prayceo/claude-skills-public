## Contents
- The Five Core Analytical Techniques
- Tool 1: Segmentation Analysis
  - When to Use Segmentation
  - Segmentation Mechanics
  - Segmentation for your product — Worked Example
- Tool 2: Retention Cohorts
  - Cohort Basics
  - Reading a Cohort Retention Table
  - The Activation → Retention Sequence
  - Cohort Benchmarks for Subscription Apps
- Tool 3: User Journey Funnels
  - When to Use Funnel Analysis
  - Building a Funnel
  - your product Full Activation Funnel
  - Funnel Diagnostics
- Tool 4: Correlation Analysis
  - The Core Purpose
  - Correlation Analysis Methodology
  - Example — your product Correlation Hypothesis
  - Correlation ≠ Causation (The Important Caveat)
- Tool 5: Risk Ratios
  - When to Use Risk Ratios
  - How to Calculate
  - Risk Ratio for Subscription Cancellation Analysis
- Advanced Diagnostic: The Segmentation Tree

---
# Analytical Tools — Deep Reference
*Source: Crystal Widjaja, Mastering Product Analytics course (Modules 2 & 3)*

---

## The Five Core Analytical Techniques

These are Crystal's "key analytical tools" — the techniques every product analytics practitioner must master to answer the most important product questions.

---

## Tool 1: Segmentation Analysis

**The core act of product analytics.**

Segmentation is how you move from "what happened" to "why it happened and for whom." It's the mechanism for separating what successful users do from what unsuccessful users do.

### When to Use Segmentation

- Any time a metric looks "fine" overall but you suspect it's masking variation
- When diagnosing a metric movement (something changed — which segment drove it?)
- When validating that a product change improved outcomes for the right users
- When building a business case for a product investment

### Segmentation Mechanics

**Step 1: Define your success metric**
What does "successful user" mean in this context? Examples:
- Subscribed user (vs. free)
- Retained at Day 30 (vs. churned)
- High-engagement user (completed 10+ engagement sessions)
- Converted from trial (vs. trial that lapsed)

**Step 2: Identify candidate segmentation dimensions**
Work through the property buckets systematically:
- Acquisition: where did this user come from?
- Activation: what did they do in their first 7 days?
- Behavioral: how do they typically use the product?
- Demographic: what do we know about their identity?
- Product context: what features do they use?

**Step 3: Cut the success metric by each dimension**
For each segment, calculate: % who are "successful" vs. "unsuccessful."

**Step 4: Identify the most differentiated segments**
The highest-value segments to understand are those with the largest delta between successful and unsuccessful rates.

**Step 5: Investigate the "why" behind the delta**
Once you've found a meaningful segmentation, dig deeper: what do users in the high-performing segment do differently?

### Segmentation for your product — Worked Example

**Success metric:** 30-day retention (returned to app in Day 29-31)

**Dimension 1: First content type experienced**
| First content type | 30-day retention |
|-------------------|-----------------|
| Guided engagement session | 62% |
| Engagement audio | 41% |
| Music/worship | 28% |

Finding: Engagement Session-first users retain at 2.2× the rate of music-first users. Implication: consider making engagement sessions the default first experience.

**Dimension 2: Streak length at Day 7**
| Streak at Day 7 | 30-day retention |
|----------------|-----------------|
| 0 days | 12% |
| 1-2 days | 28% |
| 3-4 days | 45% |
| 5-6 days | 67% |
| 7 days (perfect) | 84% |

Finding: Users who achieve a 7-day streak retain at 7× the rate of users who never build a streak. This is your activation moment — optimize for it.

---

## Tool 2: Retention Cohorts

**Measures how well you retain users over time, by when they joined.**

### Cohort Basics

A cohort is a group of users who share a common attribute — typically when they first joined or activated.

**Why cohort-based retention, not overall retention?**
Overall retention mixes users from all time periods together. A product that's declining could look fine in aggregate because the large base of old users is masking new user churn. Cohort analysis separates these.

### Reading a Cohort Retention Table

```
Cohort    | Day 0 | Day 1 | Day 7 | Day 14 | Day 30
----------|-------|-------|-------|--------|-------
Jan users |  100% |  45%  |  32%  |   28%  |  24%
Feb users |  100% |  48%  |  35%  |   31%  |  26%
Mar users |  100% |  52%  |  40%  |   36%  |  30%
```

**Pattern interpretation:**
- Each row improving: product is getting better at retaining users (March cohort retains better than January)
- Each row staying flat: retention is stable
- Each row declining: retention is getting worse (cohorts are worse over time)
- Retention not reaching a floor (continuing to decline to near zero): no sticky core user base; PMF likely not achieved

**Crystal's key insight about cohort analysis:**
Don't measure retention on all users. Measure it on activated users separately from all users. The two populations are dramatically different.

If 20% of users activate and 80% of activated users retain at Day 30:
- Overall Day 30 retention: 20% × 80% = 16%
- Activated user Day 30 retention: 80%

Optimizing overall retention is confusing activation problems with retention problems. Separate them.

### The Activation → Retention Sequence

> "My biggest tip: do not goal on retention before you understand activation."

**Why this matters:**
If activation is 20%, your retention cohorts only measure what happens to the 20% who activate. That's a biased sample of your most committed users. Retention for this group looks strong — but you're ignoring the 80% who never activated.

**The correct approach:**
1. Define activation (first meaningful value moment — e.g., completed first engagement session, achieved 3-day streak)
2. Measure activation rate (% of new users who activate)
3. Measure retention separately for:
   - All users (includes non-activated)
   - Activated users only
4. Treat activation rate as your primary leading indicator of retention

**For your product — activation definition candidates:**
- "Activated" = completed first engagement session (strong signal of intent)
- "Activated" = achieved 3-day streak (stronger signal of habit)
- "Activated" = completed a full 7-day engagement session series (strongest signal, but low volume)

Test multiple activation definitions and see which one most strongly predicts 30-day retention. That's your activation north star.

### Cohort Benchmarks for Subscription Apps

**Industry context (2025 benchmarks for consumer subscription apps):**

*Overall retention (all users, not just subscribers):*
- Day 1 retention: 25-50% (varies widely by category and platform)
- Day 7 retention: 7-15% (iOS tends slightly higher than Android)
- Day 30 retention: 3-10% (most apps lose nearly all users within a month)

*Subscription-specific retention:*
- Hard paywall monthly retention: ~12.8% median (outperforms freemium at ~9.3%)
- Weekly plan retention: 65% cancel within first 30 days; only ~5% active at 1 year
- Monthly plan retention: ~43% at Day 90; ~17% at 1 year
- Annual plans: near-total retention through the term, but ~30% churn at first renewal

*Trial conversion:*
- Install → trial: 5-9% (varies by category; hard paywalls get 78% trial starts in first week)
- Trial → paid: 25-35% (Health & Fitness leads at ~35%; shorter trials convert better but longer trials have better LTV)
- Most trial conversions happen on Day 1 of install

*Key insight from RevenueCat 2025:*
- Weekly plans convert 1.7-7.4× better than annual across all price tiers
- Weekly+trial is the highest-LTV paywall configuration ($49.27 over 12 months)
- Monthly plans consistently underperform both weekly and annual
- 35% of apps now mix subscriptions with consumables or lifetime purchases (hybrid monetization)

*Revenue patterns:*
- Median app earns ~$492/month
- ~44% of cancellations happen within the first 90 days
- Users who engage weekly have 85% higher retention
- Top 20% of users ("super-users") generate ~72% of revenue

**Wellness/habit app context:**
Wellness and habit apps with daily engagement tend to have bimodal retention: either users form the habit (high long-term retention) or they don't (quick drop-off). The key is pushing more users into the habit-forming group during the first 7 days. Apps that integrate community features see ~23% lower churn. Notification-driven engagement lifts subscriptions by ~14% when done with clear value (not just reminders).

---

## Tool 3: User Journey Funnels

**Maps the step-by-step path users take through a key flow and quantifies drop-off at each step.**

### When to Use Funnel Analysis

- Activation flow analysis (from install to first meaningful action)
- Conversion flow analysis (from free user to subscriber)
- Feature adoption flow (from awareness to regular use)
- Payment flow (from paywall view to successful charge)

### Building a Funnel

**Step 1: Define the entry event and success event**
- Entry: the first event in the flow (e.g., `app_installed`)
- Success: the final desired outcome (e.g., `subscription_converted`)

**Step 2: Map all intermediate intent events**
Every meaningful step between entry and success that a user must (or likely will) take.

**Step 3: Calculate conversion at each step**
```
Conversion at step N = (users who completed step N) / (users who completed step N-1)
```

**Step 4: Identify the highest drop-off step**
The step with the lowest conversion rate is the highest-leverage optimization opportunity.

**Step 5: Segment the funnel**
Cut the entire funnel by user segment to find which segments have dramatically different conversion patterns.

### your product Full Activation Funnel

```
Step                         | Conversion | Cumulative |
-----------------------------|------------|------------|
App Installed                | 100%       | 100%       |
Account Created              | [measure]% | [X]%       |
Onboarding Started           | [measure]% | [X]%       |
Onboarding Completed         | [measure]% | [X]%       |
First Engagement Session Opened      | [measure]% | [X]%       |
First Engagement Session Completed   | [measure]% | [X]%       |
Day 2 Return                 | [measure]% | [X]%       |
3-Day Streak Achieved        | [measure]% | [X]%       |
Paywall Viewed               | [measure]% | [X]%       |
Trial Started                | [measure]% | [X]%       |
Subscription Converted       | [measure]% | [X]%       |
```

**Funnel analysis questions to ask:**
- Where is the single biggest drop in the funnel? That's your first priority.
- Does the drop-off pattern differ by acquisition source? (e.g., users from community partner links may have higher onboarding completion)
- Does the drop-off pattern differ by device type or operating system?
- How has each step's conversion changed month-over-month?

### Funnel Diagnostics

**Sudden drop-off at a specific step:**
→ Usually indicates a UX friction point, a technical issue, or a clarity problem
→ Investigate: is there a confusing screen? A required step users don't understand? A technical error?

**Gradual decline across all steps:**
→ Usually indicates acquisition quality issues — the wrong users are entering the funnel
→ Investigate: has acquisition source mix changed? Are you attracting users with lower intent?

**Good conversion early, poor conversion late:**
→ Product interest exists but value proposition isn't strong enough at the conversion moment
→ Investigate: is the paywall explaining value clearly? Is the offer competitive? Is trial friction appropriate?

---

## Tool 4: Correlation Analysis

**Finds the behavioral signals that most strongly predict your success metrics.**

### The Core Purpose

> "What behaviors in the first N days most strongly predict long-term retention (or subscription, or LTV)?"

This is how companies discover their "magic moments" — the specific product behaviors that, once a user completes them, dramatically increase the probability of long-term value.

### Correlation Analysis Methodology

**Step 1: Define your outcome variable**
The success metric you're trying to predict:
- 30-day retention
- Trial → subscription conversion
- High LTV (lifetime subscription value)
- 90-day retention

**Step 2: Define your observation window**
How many days of early behavior will you analyze? Usually: first 7 days, first 14 days.

**Step 3: Identify candidate behavioral variables**
What user actions in the observation window might predict your outcome? All the events and properties you track become candidates.

**Step 4: Compare retained vs. churned users across each variable**

For each behavioral variable:
```
Retained users: what % did [behavior X] in first 7 days?
Churned users: what % did [behavior X] in first 7 days?
Delta: retained rate - churned rate
```

Large deltas = strong correlation with retention.

**Step 5: Find the "magic moment" threshold**

For behavioral variables with strong correlation, find the threshold that most separates retained from churned:
- Not just "completed a engagement session" but "completed X engagement sessions" where X maximizes the retention delta
- Not just "achieved a streak" but "achieved a streak of length X"

### Example — your product Correlation Hypothesis

**Hypothesis analysis structure:**

| Behavior in first 7 days | Retained at Day 30 | Churned at Day 30 | Delta |
|--------------------------|-------------------|-------------------|-------|
| Completed 0 engagement sessions | [low]% | [high]% | [large] |
| Completed 1+ engagement sessions | — | — | — |
| Completed 3+ engagement sessions | — | — | — |
| Completed 7+ engagement sessions | [high]% | [low]% | [large] |
| Achieved 3-day streak | — | — | — |
| Achieved 7-day streak | — | — | — |
| Opted in to notifications | — | — | — |
| Opened 3+ notifications | — | — | — |
| Invited a friend | — | — | — |

**What to look for:**
The behavior(s) with the largest delta AND a threshold that's achievable during onboarding — that's your activation milestone to optimize for.

### Correlation ≠ Causation (The Important Caveat)

Correlation analysis reveals association, not cause. Users who do 7 engagement sessions in their first week probably retain better — but is it because they did 7 engagement sessions, or because people committed enough to do 7 engagement sessions were always going to retain?

**How to validate correlation findings:**
- Run an A/B test that nudges users toward the correlated behavior and measures retention impact
- If nudging users to complete more engagement sessions (via notifications, incentives) improves their retention, the correlation is causal
- If it doesn't, the behavior was just a signal of pre-existing commitment

---

## Tool 5: Risk Ratios

**Quantifies how much riskier (or safer) one user segment is than another for a specific negative outcome.**

### When to Use Risk Ratios

- Building a business case: "investing in X activation step reduces churn risk by Y×"
- Prioritizing interventions: "which at-risk segment should we target first?"
- Quantifying the value of onboarding milestones
- Comparing churn risk across acquisition sources

### How to Calculate

```
Risk Ratio = Rate of outcome in Group A ÷ Rate of outcome in Group B

Where: Rate of outcome = % of users in this group who experienced the outcome
```

**Example:**
- Churn rate in first 30 days, users with no streak at Day 7: 75%
- Churn rate in first 30 days, users with 7-day streak at Day 7: 12%
- Risk Ratio = 75% ÷ 12% = 6.25

**Interpretation:** Users who don't achieve a 7-day streak are 6.25× more likely to churn within 30 days.

This is a much more compelling business case than "users with streaks retain better."

### Risk Ratio for Subscription Cancellation Analysis

Track users who cancel by what they did and didn't do:

```
Cancellation rate within 60 days of subscription:
- Users who completed 0 engagement sessions after subscribing: [X]%
- Users who completed 1-5 engagement sessions: [Y]%
- Users who completed 10+ engagement sessions: [Z]%

Risk ratio (0 completions vs. 10+): X ÷ Z = [N]×
```

This quantifies the value of post-subscription engagement — and tells you what to invest in to reduce cancellation.

---

## Advanced Diagnostic: The Segmentation Tree

When a top-level metric is moving, use a segmentation tree to decompose it:

```
Metric: 30-day subscription retention dropped 5 points this month

Level 1 cut: By acquisition source
  → App store organic: -1 point (not the driver)
  → Paid social: -8 points (this is the driver)

Level 2 cut: Paid social, by campaign
  → Community partner campaigns: -1 point
  → Broad interest targeting: -11 points (this is the driver)

Level 3 cut: Broad interest paid social, by first content type
  → Engagement Session first: -2 points
  → Music first: -15 points (this is the driver)

Root cause hypothesis: New music-first users from broad paid social are not converting to subscribers or retaining. Possible causes: wrong audience (music seekers vs. wellness seekers), or music-first onboarding isn't converting to daily habit.

Action: Redirect broad interest paid social budget toward engagement session-first messaging; A/B test music-first vs. engagement session-first onboarding for this segment.
```

The segmentation tree approach:
1. Start with the aggregate metric change
2. Cut by the broadest segmentation dimension
3. Identify which segment(s) is driving the movement
4. Go one level deeper within the driver segment
5. Continue until you've identified a root cause narrow enough to act on
