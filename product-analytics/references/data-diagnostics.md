## Contents
- The Diagnostic Framework
- The Data Trust Diagnostic
- The Investigate Discipline — Questions Before Queries
- Crystal's 10 Analytics Mistakes to Avoid
- Communicating Data to Stakeholders

---
# Advanced Data Diagnostics — Deep Reference
*Source: Crystal Widjaja, Mastering Product Analytics course (Module 3); "Why Most Analytics Efforts Fail" (Blog, 2020)*

---

## The Diagnostic Framework

How to investigate when something is wrong — a metric moved unexpectedly and you need to diagnose why.

```
Step 1: Scope — What exactly moved? When? By how much?
Step 2: Decompose — Which segment(s) drove the movement?
Step 3: Trace — Which events in those segments explain the change?
Step 4: Hypothesize — What product/external change could explain this?
Step 5: Validate — Test the hypothesis with additional cuts of data
Step 6: Act — What do we do about it?
```

**Common metric movements and their causes:**

| Symptom | Likely root cause | Where to look |
|---------|------------------|---------------|
| Sudden retention drop | Product change, bug, notification policy change | Look at specific cohort that dropped; compare event patterns before/after |
| Gradual CAC increase | Audience saturation, creative fatigue, competitive pressure | Segment by acquisition source; check external market signals |
| Activation rate declining | Onboarding change, new user profile (different acquisition source), UI regression | Funnel step-by-step breakdown; segment by cohort month |
| Revenue drop without user drop | Pricing/offer change, trial → subscription conversion drop, higher cancellation rate | Revenue per user by cohort; funnel from trial to subscription |

---

## The Data Trust Diagnostic

Crystal's test for whether an organization's data can be trusted:

**Level 1 — Do the numbers add up?**
"Can more people have done Action B than Action A if B always follows A?"
If yes → tracking is broken. Fix before any analysis.

**Level 2 — Do teams agree on the number?**
"If Finance and Marketing both pull last month's new users, do they get the same number?"
If no → metric definitions are misaligned. Fix the data dictionary.

**Level 3 — Can business users access and interpret it independently?**
"Can a non-technical PM or marketer answer their own questions without a data analyst?"
If no → self-serve analytics is not working. Fix tooling and documentation.

**Level 4 — Does analysis change behavior?**
"When analysis produces a finding, does someone act on it?"
If no → data culture problem. Analysis that doesn't influence decisions is a waste.

---

## The Investigate Discipline — Questions Before Queries

The most important discipline Crystal teaches:

> "Don't run analyses that entertain but don't influence decision-making. Ask: am I looking for information to change my behavior, or am I scratching a curiosity itch for a dopamine hit?"

**The four-level question framework:**
Before any analysis, answer these in order:

1. **Business goals:** What are the OKRs/KRIs this analysis is connected to?
2. **Team goals:** What specific team metric is being investigated?
3. **Product experiences:** What product behaviors drive that metric?
4. **Hypotheses:** What specific questions or assumptions are being tested?

An analysis without a hypothesis is data tourism. Expensive, feels productive, generates no action.

---

## Crystal's 10 Analytics Mistakes to Avoid

(from her LinkedIn):

1. Believing analytics only matter after PMF → start from day one
2. Including internal/test account usage in analysis → filter it out
3. Tracking data for every feature without asking "why" → use job-to-be-done to guide what to track
4. No screenshots in event documentation → every event needs a visual
5. Treating data documentation as a drag → maintain a central Google Sheet as your living dictionary
6. Running analyses that don't influence decisions → ask "will this change behavior?" before running
7. Complicating event names past the point of understanding → simplify, optimize for business user readability
8. Allowing outdated/unused events to clutter analytics → Marie Kondo your event tracking quarterly
9. Mixing internal team usage with real user data → always filter test accounts
10. Viewing data as a project with an end date → treat it as a product with continuous iteration

---

## Communicating Data to Stakeholders

Data that doesn't change decisions is waste. Getting to influence requires:

**1. Know your audience's altitude.** Executives want high-altitude summaries. PMs want mid-altitude input metrics. Engineers want low-altitude event specifics. Present at the right level for each audience.

**2. Lead with the "so what."** Don't present data and then explain the implication. Lead with the implication and use data to support it.
- Wrong: "Our D7 retention dropped 3 points. Here's the chart. As you can see..."
- Right: "We have a retention problem in our new user cohort that will cost us ~$X in LTV if not addressed. The data shows it started when we changed the onboarding flow on [date]."

**3. Visual beats written every time.** Screenshot of the product + chart of the metric + one-sentence implication beats a paragraph of explanation.

**4. Pair every finding with a recommended action.** A finding without a recommendation puts the burden on the audience. Do the work for them.

**5. Build data trust over time.** Don't present data you're not confident in. One wrong number permanently damages credibility. When uncertain, say "directionally, the data suggests X — but I'd want to validate Y before acting on it."
