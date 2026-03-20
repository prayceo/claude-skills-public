---
name: retention-engagement
description: Applies Casey Winters, Erika Warren, and Shaun Clowes's retention and engagement frameworks to diagnose churn, build habit loops, design re-engagement systems, and measure retention health. com), Shaun Clowes's work scaling Atlassian and Confluent, and Erika Warren's growth frameworks. Activates when diagnosing retention problems, designing activation flows, building notification/re-engagement systems, analyzing cohort retention curves, improving daily/weekly engagement, reducing churn for subscription products, or evaluating the health of your product's core habit loop.
---

**Reference files:**
- `references/retention-curves-cohorts.md` — Retention curve analysis, cohort mechanics, flattening curves
- `references/engagement-loops.md` — Engagement loop design, habit formation, core action identification
- `references/reengagement-resurrection.md` — Notification systems, dormant user resurrection, churn prediction

---

## How to Use This Skill

When this skill activates:
1. Identify which retention or engagement framework best applies to the question (retention curves, engagement loops, activation, or re-engagement)
2. Apply the relevant decision tree from the Decision Tools section
3. Ground all recommendations in the context of your product
4. Cite the specific framework when making claims
5. If deeper detail is needed, read the relevant reference file before responding

## Gotchas

Common mistakes to avoid when applying these frameworks:

1. **Goaling on retention before fixing activation:** Retention metrics are misleading when only a small fraction of users activate. You end up measuring a biased, self-selected group. Winters is clear that activation is the highest-leverage retention lever -- improving activation by 10% has the same impact as improving acquisition by 10% at a fraction of the cost.
2. **Measuring notification success by open rate instead of downstream retention:** A notification that gets opened but does not lead to core action completion (daily engagement for your product) is a false positive. Winters's Pinterest principle: success is measured by downstream retention, not open rate. High open rates with flat retention means your notifications are interrupting, not engaging.
3. **Applying the same retention strategy across all three stages:** New user retention (Days 0-14), current user retention (Days 14-90+), and resurrected user retention are different problems with different causes. Sending re-engagement emails to Day 3 users who never activated treats an activation failure as a re-engagement problem.
4. **Building streaks without grace mechanics:** Streaks leverage loss aversion, but a broken streak without a grace day or freeze option causes rage-quit churn -- especially for your product where missed days carry unnecessary guilt. Winters's design principle: never be punitive. Include grace days and celebrate re-engagement warmly.

## Example

**User asks:** "Our D7 retention is 25% but D30 drops to 8%. Where is the problem?"

**Approach:**
1. Apply Decision Tool 1 (Diagnosing a Retention Problem): D7 at 25% is above the engagement loop threshold, but D30 at 8% signals an ongoing value delivery problem in the Day 7-30 window
2. Check whether the retention curve is flattening (stabilizing at 8%) or still declining -- if declining, the product has a fundamental recurring value problem; if flattening, there is a viable retained segment but the habit loop is failing for 70%+ of activated users
3. For your product, investigate whether users who complete engagement sessions on 5+ of their first 7 days have significantly better D30 retention -- if yes, the problem is habit formation frequency in the first week, not content quality
4. Recommend a diagnostic plan: segment D30 churners by their Day 1-7 engagement pattern, identify the behavioral threshold that predicts retention, then redesign the Day 7-14 experience to push more users past that threshold

---

## Core Philosophy

> "Retention is the single most important thing for growth. If you don't retain users, nothing else matters — not acquisition, not monetization, not virality. A leaky bucket never fills."

Casey Winters's foundational insight is that retention is not a feature or a team's responsibility — it is the output of the entire product experience. Companies that treat retention as a "thing to fix" with emails and push notifications are treating the symptom, not the disease. The disease is almost always a product that does not deliver recurring value.

Three foundational beliefs:
1. **Retention is the foundation of growth.** Acquisition without retention is waste. Every 1% improvement in retention compounds across all future cohorts.
2. **Engagement precedes retention.** Users who are deeply engaged with the core action naturally retain. The job is to design the product so the core action is easy, rewarding, and habitual.
3. **Retention has stages, not a single metric.** New user retention, current user retention, and resurrected user retention are different problems requiring different solutions.

---

## Module 1: Retention Foundations — Why Retention Is Everything

Retention compounds: a 30-point improvement in monthly retention can nearly triple the active user base within a year at the same acquisition spend. Retention amplifies every other growth lever — it increases LTV, fuels viral loops, and builds brand advocacy.

Winters divides retention into **three stages**: (1) New User Retention (Days 0-14) — driven by activation quality, (2) Current User Retention (Days 14-90+) — driven by recurring value delivery, (3) Resurrected User Retention — driven by re-engagement system quality. Each stage has different causes and different solutions.

**Retention curve shapes** are diagnostic: a **flattening curve** (stabilizes at a positive %) indicates lasting value for a subset of users. A **declining curve** (never stabilizes) indicates a fundamental product problem. A **smile curve** (dips then rises) indicates strong re-engagement.

*→ Full detail: `references/retention-curves-cohorts.md`*

---

## Module 2: The Engagement Loop — Core Action, Triggers, and Rewards

The engagement loop is: **Trigger → Action → Reward → Investment → (back to Trigger)**. Triggers can be external (notifications, email) or internal (habits, emotions). Rewards should be variable. Investment (data, streaks, preferences) strengthens future loops.

The **core action** is the single behavior that, when repeated, drives retention. Find it using a Frequency-Retention Matrix — plot user actions by frequency and correlation with D30 retention. The top-right quadrant (high frequency + high retention correlation) is your core action. For your product, the hypothesized core action is completing a daily engagement.

Once identified, every product decision flows from the core action: onboarding drives to it, notifications trigger return to it, features support it, content feeds it, and metrics measure it.

*→ Full detail: `references/engagement-loops.md`*

---

## Module 3: Activation — The Bridge from Signup to Habit

Activation (the transition from new user to retained user) is the highest-leverage retention lever. Improving activation by 10% has the same effect as improving acquisition by 10% at a fraction of the cost. The critical distinction: the **Setup Moment** (account creation, preferences) is a prerequisite, while the **Aha Moment** (first experience of core value) predicts long-term retention. The gap between them is where most users are lost.

**Product activation sequence:** Download → Preference setup (< 2 min) → First engagement session auto-presented → Listen/read → Emotional resonance (aha) → Set daily reminder → Return Day 2. Key metrics: % completing first engagement session in first session, D1-to-D2 return rate, % setting reminders within 3 days.

*→ Full detail: `references/engagement-loops.md`*

---

## Module 4: Ongoing Retention — Notifications, Streaks, and Content Freshness

**Notifications** are the most powerful and most dangerous retention tool. Winters's principles from Pinterest: every notification must deliver value, frequency should match engagement level, content beats urgency, and success is measured by downstream retention (not open rate). Segment users into power/regular/cooling/dormant/churned and adjust strategy for each.

**Streaks** leverage loss aversion and identity formation. Design principles: streak on the core action, include grace days, celebrate milestones, and never be punitive. Product opportunity: daily engagement streak with freeze mechanic and milestone badges.

**Content freshness** drives retention for subscription content products. Content value = Relevance x Freshness x Quality x Discovery. The daily loop: notification/habit triggers app open, user completes engagement session (core action), receives emotional reward + streak progress, invests through preferences/history/journal, strengthening tomorrow's trigger.

*→ Full detail: `references/reengagement-resurrection.md`*

---

## Decision Tools

### Decision 1: Diagnosing a Retention Problem

```
Is D1 retention below benchmark (< 40% for consumer apps)?
├── YES → Activation problem. Focus on:
│   ├── Is the aha moment reachable in the first session?
│   │   ├── NO → Redesign onboarding to drive to aha moment faster
│   │   └── YES → Is the aha moment actually valuable?
│   │       ├── NO → Product-market fit issue. Reconsider core value.
│   │       └── YES → Friction problem. Audit and remove barriers.
└── NO (D1 is fine) → Is D7 retention below benchmark (< 20%)?
    ├── YES → Engagement loop problem. Focus on:
    │   ├── Is there a clear core action? → Define and drive it
    │   ├── Are triggers working? → Audit notification strategy
    │   └── Is reward variable and valuable? → Improve content/value delivery
    └── NO (D7 is fine) → Is D30 retention below benchmark (< 10%)?
        ├── YES → Ongoing value problem. Focus on:
        │   ├── Content freshness → Is there enough new content?
        │   ├── Feature depth → Are power users underserved?
        │   └── Competitor pull → Are users switching to alternatives?
        └── NO → Retention is healthy. Focus on growth loops and monetization.
```

### Decision 2: Notification Strategy Selection

```
What is the user's current engagement level?
├── Power user (daily active):
│   └── Send: New features, social activity, advanced content
│       Frequency: Multiple per day OK
│       Goal: Deepen engagement, prevent power-user churn
├── Regular user (weekly active):
│   └── Send: Core content, personalized recommendations
│       Frequency: 1-2 per day maximum
│       Goal: Increase frequency toward daily
├── Cooling user (active 7-14 days ago):
│   └── Send: Best content of the week, emotional/seasonal trigger
│       Frequency: 1 per day, test reduction
│       Goal: Prevent slide to dormancy
├── Dormant user (14-30 days inactive):
│   └── Send: Single high-value piece, "we have new [feature/content]"
│       Frequency: 1 per week maximum
│       Goal: One resurrection attempt
└── Churned user (30+ days inactive):
    └── Send: Monthly product update or seasonal content only
        Frequency: Monthly maximum
        Goal: Low-pressure awareness for future re-engagement
```

### Decision 3: Should We Build a Streak Mechanic?

```
Is the product designed for daily use?
├── YES → Does the core action naturally happen daily?
│   ├── YES → Streak on core action. Build: counter, milestones, freeze.
│   │   ├── Is the user base sensitive to gamification?
│   │   │   ├── YES → Add leaderboards, sharing, streak badges
│   │   │   └── NO → Keep streaks subtle. Progress indicator only.
│   │   └── Test: Does streak introduction improve D30 retention?
│   └── NO → Can the core action be broken into daily micro-actions?
│       ├── YES → Create daily micro-action and streak on that
│       └── NO → Streaks may not fit. Use weekly goals instead.
└── NO (not daily use) → Do not build streaks. Consider:
    ├── Weekly engagement targets
    ├── Progress toward a goal (course completion, etc.)
    └── Usage milestones (not time-based)
```

### Decision 4: Churn Intervention Priority

```
Is churn concentrated in a specific cohort or segment?
├── YES → Which segment?
│   ├── New users (< 7 days) → Activation problem. Fix onboarding.
│   ├── Users at subscription renewal → Value perception problem. Fix pre-renewal communication.
│   ├── Users after a product change → Regression. Roll back or mitigate.
│   └── Users in a specific geography/demo → Segment-specific product gap.
└── NO (churn is evenly distributed) → Systemic issue:
    ├── Is overall engagement declining? → Content freshness or product fatigue
    ├── Is a competitor gaining share? → Competitive response needed
    └── Has nothing changed? → Natural maturation. Focus on resurrection.
```

### Decision 5: Content vs. Product Investment for Retention

```
Is content consumption per session stable or growing?
├── YES → Content is not the problem. Invest in:
│   ├── Engagement mechanics (streaks, social, personalization)
│   ├── Notification optimization
│   └── Feature depth for power users
└── NO (content consumption declining) → Content is the problem.
    ├── Is the content catalog sufficient?
    │   ├── NO → Invest in content production volume
    │   └── YES → Is discovery working?
    │       ├── NO → Improve recommendation/personalization
    │       └── YES → Is content quality declining?
    │           ├── YES → Invest in content quality, not volume
    │           └── NO → Audience interest may be shifting. Research needed.
```

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| Retention Curve | Graph showing % of a cohort still active over time (D1, D7, D30, D60, D90) |
| Flattening Curve | Retention curve that stabilizes at a positive %, indicating lasting value for a user subset |
| Declining Curve | Retention curve that never stabilizes, indicating a fundamental product-value problem |
| Core Action | The single behavior that, when repeated, drives long-term retention |
| Engagement Loop | Repeating cycle of Trigger, Action, Reward, Investment that drives habitual use |
| Activation Rate | % of new users who reach the aha moment / complete the key setup milestone |
| Aha Moment | The first experience of core product value that predicts long-term retention |
| Streak Mechanic | Gamification element that counts consecutive days of completing the core action |
| Resurrection Rate | % of churned users who return to active usage after a period of dormancy |
| Notification Segmentation | Sending different notification types/frequencies based on user engagement level |
| Content Freshness | The rate and quality of new content added to a content-driven product |
| New User Retention | Retention behavior in the first 0-14 days, driven by activation quality |
| Current User Retention | Retention behavior from Day 14 to 90+, driven by ongoing value delivery |
| Churn Prediction | Using behavioral signals to identify users likely to churn before they leave |
| Grace Day | Streak mechanic that allows users to miss one day without losing their streak |

---

## Reference Files

- `references/retention-curves-cohorts.md` — Retention curve analysis, cohort mechanics, flattening curves
- `references/engagement-loops.md` — Engagement loop design, habit formation, core action identification
- `references/reengagement-resurrection.md` — Notification systems, dormant user resurrection, churn prediction
