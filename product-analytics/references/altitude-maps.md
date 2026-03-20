## Contents
- Data Theater
- The Data Wheel of Death
- Altitude Maps — Full Framework
  - Controllable vs. Uncontrollable Inputs
  - The Solution Scorecard

---
# Altitude Maps & Data Theater — Deep Reference
*Source: Crystal Widjaja, "Stop Data Theater" (Altitude Maps guest post, FishmanAF, 2024); Mastering Product Analytics course (Module 1)*

---

## Data Theater

Crystal's broader diagnosis of organizational data dysfunction, expanded in her 2024 FishmanAF guest post. Data Theater is the sin of using copious amounts of data in ways that make teams feel smart and data-driven without actually impacting any real decision-making or core business metrics.

**The three symptoms of Data Theater:**

**Symptom 1: Disconnect between org structure and the "physics of the business."**
Teams focus on metrics or initiatives that aren't truly critical. Silos emerge with conflicting or redundant goals. At its worst, a team's charisma and ability to manage upwards becomes the primary way they receive resources — rather than their actual contributions to business outputs.

**Symptom 2: Rigid focus on low-level KPIs despite new insights.**
Teams fixate on a narrow set of metrics and celebrate when those metrics improve — even if higher-level goals remain unchanged. Data is cherry-picked to "prove" the success of features that didn't meaningfully impact the business. Teams continue optimizing their assigned metric for the year while improvements aren't yielding results at the company level.

**Symptom 3: Lack of a repeatable, systematic approach to separate signal from noise.**
Teams go through the motions of tracking and reviewing data during weekly meetings, but without genuine commitment to understanding or acting on it. Leaders have knee-jerk reactions to short-term fluctuations — celebrating when numbers go up and sounding alarms when they go down — without understanding whether changes are normal variance or driven by specific actions.

**Crystal's one-line diagnostic:** "Most companies would probably say 'we have the data, it's just not really being used.'"

**The cure:** Altitude Maps (see below).

---

## The Data Wheel of Death

The anti-pattern that kills analytics programs (coined by Brian Balfour, diagnosed by Crystal):

```
Data is tracked → Never analyzed → Loses trust → Teams stop using it
         ↑                                               ↓
Product changes → Tracking goes stale → Data becomes wrong
         ↑                                               ↓
         └─────────── New tools purchased ───────────────┘
                        (doesn't fix it)
```

The root causes are NOT tool quality or analyst headcount. They are:
1. Tracking metrics as the goal instead of analyzing them
2. Developer/data mindset instead of business user mindset
3. Wrong level of abstraction in event naming
4. Written-only documentation instead of visual communication
5. Treating data as a project instead of an ongoing initiative

**The fix:** Address root causes, not symptoms. Symptoms (bad data, slow queries, untrusted numbers) are treated with new tools and more training. That's treating the wrong disease.

---

## Altitude Maps — Full Framework

Crystal's framework for navigating between strategic and tactical views of data — and the primary cure for Data Theater. The central insight: different decisions require different altitudes of analysis, and teams constantly confuse them.

**The three altitudes:**

```
HIGH ALTITUDE (strategic)
  → Company-level OKRs and north star metric
  → "Are we growing the right things?"
  → Cadence: monthly/quarterly

MID ALTITUDE (product/team)
  → Feature-level KPIs and input metrics
  → "Is this product area healthy?"
  → Cadence: weekly

LOW ALTITUDE (operational)
  → Event-level behavior and user journeys
  → "Why is this specific metric moving?"
  → Cadence: daily/ad hoc
```

**The altitude mistake:** Teams spend most of their time at low altitude (individual events, one-off queries) while leaders demand high-altitude answers. The mismatch creates frustration on both sides.

**The Altitude Map as goal-setting tool:**
Crystal uses Altitude Maps to connect company OKRs to product decisions. Each level of the map answers a different question:
- High altitude: *What does business success look like?*
- Mid altitude: *What product behaviors drive that success?*
- Low altitude: *What events tell us those behaviors are happening?*

A well-built Altitude Map lets any team member trace a line from their daily work up to the company's north star — and trace any metric anomaly back down to the events causing it.

### Controllable vs. Uncontrollable Inputs

Crystal distinguishes two types of input metrics at each altitude:

**Controllable inputs:** Metrics you can directly influence through product or operational changes.
- Onboarding completion rate (can be improved with UX changes)
- Notification opt-in rate (can be improved with permission priming)
- Paywall conversion rate (can be improved with offer testing)

**Uncontrollable inputs:** Metrics influenced by external forces you can't directly change.
- Market demand / seasonal interest in the product content
- Competitor launches
- App store algorithm changes
- Macroeconomic factors affecting discretionary spending

**Why this matters:** Teams performing Data Theater often goal on uncontrollable inputs, then rationalize why they missed targets. Altitude Maps force explicit identification of what you can and can't control — so effort concentrates on controllable levers.

### The Solution Scorecard

The third layer of the Altitude Map — an index of the features being built and an assessment of their value as it relates to altitude metrics.

For each active solution/feature, answer:
1. How does this solution move the needle on our key altitude metrics?
2. Is the solution driving measurable impact, and if so, how much?
3. Can we use available data to improve it?
4. Are we using data to keep looking forward — making timely decisions on what to work on next?

**The Solution Scorecard transforms the Altitude Map from a measurement tool into a prioritization tool.** It turns intuition-driven "bets" into data-backed decisions that directly ladder up to altitude metrics.

**For your product — Altitude Map hypothesis:**
```
HIGH: North Star = Daily Engagement Completions (or Subscription Revenue)

MID: Input metrics that drive NSM (mark each as controllable [C] or uncontrollable [U])
  → 7-day streak completion rate [C]
  → Engagement Session completion rate per session [C]
  → Trial-to-subscription conversion rate [C]
  → 30-day retention rate [C - via activation improvements]
  → Organic install volume [U - market/seasonal]
  → Notification opt-in rate [C]

LOW: Events that explain mid-altitude metrics
  → engagement session_opened, engagement session_completed, engagement session_skipped
  → streak_maintained, streak_lost, streak_restored
  → paywall_viewed, trial_started, subscription_converted
  → notification_received, notification_tapped, notification_dismissed

SOLUTION SCORECARD:
  → [Feature: Guided onboarding engagement session] → Targets: activation rate, D7 retention
  → [Feature: Streak freeze] → Targets: streak completion rate, D30 retention
  → [Feature: Personalized content recs] → Targets: engagement session completion rate
```
