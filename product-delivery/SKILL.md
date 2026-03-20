---
name: product-delivery
description: >
  Applies frameworks from Andy Johns and Matt Greenberg for shipping big-bet product
  initiatives at scale. Covers building product conviction, dynamic delivery
  planning, cross-functional execution, and staged launch strategy. Activates when
  your product is planning ambitious new features (e.g., live group sessions, AI
  engagement sessions, family plans) that require more than two weeks of engineering and
  carry meaningful risk if they miss.
---

**Reference files:**
- `references/building-product-conviction.md` -- Problem classification, customer signal validation, stakeholder alignment, kill criteria
- `references/dynamic-delivery-plans.md` -- Complexity assessment, effort estimation, sequencing, milestones, tradeoff guardrails
- `references/launch-and-post-launch-strategy.md` -- Staged launch approaches, pre-launch tiers, failure mode responses, outcome measurement

---

## How to Use This Skill

When this skill activates:
1. Identify which product delivery framework from this skill best applies to the question
2. Apply the relevant decision tree from the Decision Tools section
3. Ground all recommendations in the context of your product
4. Cite the specific framework when making claims
5. If deeper detail is needed, read the relevant reference file before responding

## Gotchas

Common mistakes to avoid when applying these frameworks:

1. **Don't mistake stakeholder enthusiasm for product conviction.** Johns is explicit: a VP who is excited is not validated customer demand. At your company, internal excitement about a feature idea (e.g., "AI-generated engagements") is not evidence. Conviction must be built through the customer signal ladder -- stated interest is weak, behavioral proof is strong. Skip the signal ladder and you'll commit resources to vitamins disguised as painkillers.
2. **Don't add engineers when milestones slip.** Brooks's Law applies: adding people to a late project makes it later. Johns and Greenberg's default response to slippage is (1) reduce scope, (2) extend timeline, (3) add resources *only* when work is genuinely parallelizable. The instinct to throw more people at a late your product initiative usually compounds the problem.
3. **Don't launch big bets to 100% on Day 1.** Johns's staged launch strategy exists because early cohorts (often power users) behave differently than the general population. At your company, rolling out a new feature to daily streak users first may show strong engagement that collapses when casual users encounter it. Always monitor segmented metrics as you expand percentages.
4. **Don't skip kill criteria in the Problem Framing Document.** Kill criteria are the most commonly omitted section, and their absence means the team has no objective way to stop a failing initiative. "If it doesn't feel right, we'll reconsider" is not a kill criterion. "If fewer than 15% of beta users return within 7 days, we pause" is.

## Example

**User asks:** "We want to build live group sessions rooms in the your product app. How should we plan and deliver this?"

**Approach:**
1. Start with Johns's conviction-building process -- classify the problem (Painkiller, Vitamin, or Vegetable?), validate with customer signals beyond stated interest (do users currently use workarounds like Zoom engagement calls?), and write a Problem Framing Document with explicit kill criteria
2. Run a complexity assessment -- live audio with multiple simultaneous users is "Complicated" or "Very Complicated" (novel approach, real-time infrastructure unknowns), which means a throwaway prototype or time-boxed spike before committing to real estimates
3. Build a Dynamic Delivery Plan with 5 milestones (working audio prototype -> moderation/safety layer -> room creation flow -> scheduling/notifications -> launch-ready polish), with tradeoff guardrails establishing quality as fixed (personal content is trust-sensitive) and scope as flexible
4. Plan a combined staged launch: iOS first, then 5% of users with 7+ day streaks, expanding by percentage while monitoring completion rate, return rate, and support ticket volume at each stage

---

## Andy Johns's Core Philosophy

Johns rejects the false binary between agile and waterfall. His central claim: teams that ship big bets repeatably invest heavily in upfront conviction-building, then create structured-but-flexible delivery plans, then execute with disciplined checkpoints. The real question is whether you have a system that compounds learning across successive big bets, or whether each one is an ad hoc scramble.

Greenberg extends this: delivery plans must account for technical complexity honestly, and leaders must treat technical debt as a strategic lever. Together they argue for a disciplined hybrid -- neither pure agile nor pure waterfall.

---

## Module 1: Building Product Conviction

### The Core Problem

At scale, product conviction cannot come from one person's "product sense." You need a system to discover and validate opportunities that builds conviction across product, engineering, design, and commercial.

### Problem Classification: Painkillers, Vitamins, and Vegetables

| Type | Description | Signal Strength |
|------|-------------|----------------|
| Painkiller | Solves an acute, urgent need customers feel daily | Strongest |
| Vitamin | Nice-to-have improvement; no urgency if missing | Moderate |
| Vegetable | Valued abstractly but not urgently sought | Weakest |

Most failed big bets are vitamins the team convinced themselves were painkillers. The classification forces intellectual honesty before committing resources.

**Anti-pattern: "Stakeholder enthusiasm as conviction."** A VP who is excited is not validated customer conviction. Enthusiasm is not evidence.

### Building Conviction Through Customer Signals

1. **Stated interest** -- "That sounds great" in an interview. Very weak. People are polite.
2. **Soft commitment** -- Waitlist signup, beta email. Moderate signal.
3. **Hard commitment** -- Money down, LOI, plan upgrade for early access. Strongest pre-launch signal.
4. **Behavioral proof** -- Post-launch retention and engagement data. Indisputable.

### The Problem Framing Document

A one-page artifact that aligns all stakeholders:

**Section 1: Customer Problem**
- Who experiences this problem? (Specific segment, not "all users")
- How often do they experience it? (Daily, weekly, situationally)
- What is the current workaround? (If no workaround, is the pain real?)
- What evidence do we have? (Customer signal level and strength)

**Section 2: Solution Hypothesis**
- What will we build? (One paragraph, not a spec)
- Why do we believe this will solve the problem? (Reasoning, not hope)
- What is the primary success metric? (One metric, not a dashboard)

**Section 3: Key Assumptions**
- What must be true for this to work? (List 3-5 assumptions)
- Which assumption, if wrong, kills the bet? (Identify the riskiest one)

**Section 4: Kill Criteria**
- Under what conditions will we stop? (Specific, measurable)
- By when will we know? (Specific date or milestone)

Good kill criteria: "If fewer than 15% of beta users return within 7 days, we pause." "If engineering prototype reveals latency above 500ms, we deprioritize."
Bad kill criteria: "If it doesn't feel right, we'll reconsider." No kill criteria at all (defeats the purpose of conviction-building).

### Stakeholder Alignment as Conviction Multiplier

All key functions must be present from the beginning: product, design, engineering, customer support, and commercial. Each provides a unique perspective that, if excluded early, creates expensive rework later.

Each function pressure-tests assumptions from their vantage point:

| Function | Key Question |
|----------|-------------|
| Engineering | Can we build this at required quality in timeline? |
| Design | Is the interaction model learnable for our users? |
| Support | Can we support without unsustainable ticket load? |
| Commercial | Can we price and sell this? |
| Content (your product) | Is this foundationally sound and brand-appropriate? |

---

## Module 2: Dynamic Delivery Plans

### Why Traditional Planning Fails Big Bets

Agile sprints: two-week visibility is insufficient for 3-month initiatives, no structural accountability for the whole, cross-team dependencies invisible.
Waterfall: requirements change as you learn, false precision creates false confidence, communication ossifies.

### The Dynamic Delivery Plan

A structured planning artifact that captures critical details early but explicitly builds in room to change. Five components:

#### 1. Complexity Assessment

| Level | Description | Planning Implication |
|-------|-------------|---------------------|
| Straightforward | Done before, familiar territory | High confidence estimates |
| Normal | Similar prior experience | Moderate confidence |
| Complicated | Novel approach, unknowns | Wide ranges needed |
| Very Complicated | Unprecedented, high uncertainty | Spike/prototype first |

Complexity factors: Scale, Magnitude, Stability (of requirements), Access (to needed data/APIs).

> **For basic scoping and estimation practices** (scoping documents, t-shirt sizing, estimation anti-patterns), see **technical-foundations**. This module covers the Dynamic Delivery Plan's estimation approach unique to big bets.

**Estimation by complexity:** Straightforward = point estimates. Normal = calibrated t-shirt sizes. Complicated = time-boxed spike first, then estimate with optimistic/likely/pessimistic ranges. Very Complicated = throwaway prototype (1-2 week timebox), then calibrate real estimates.

**Anti-pattern: "Precision theater."** Estimating a Very Complicated initiative to the story-point level. Better: "4-8 weeks with these three unknowns."

#### 2. Sequencing

- **Risk-first:** Front-load the hardest, most uncertain work. If it fails, fail fast and cheap.
- **Value-first:** When uncertainty is low, deliver user value incrementally.
- **Dependency-aware:** Map cross-team dependencies explicitly. A 1-week slip can cascade to a month.

#### 3. Milestone Definition

Define 3-5 milestones for a big bet. Each milestone should:
- Represent a meaningful state of the product (not "Phase 1 done" -- rather, "Users can create and join a engagement room")
- Have clear exit criteria (objectively testable conditions)
- Trigger a checkpoint review (team demonstrates progress, surfaces issues)
- Enable a go/no-go decision (given what we now know, should we continue, pivot, or stop?)

| Initiative Length | Recommended Milestones |
|------------------|----------------------|
| 1-2 months | 3 |
| 3-4 months | 4-5 |
| 5-6 months | 5-7 |
| >6 months | Consider breaking into separate initiatives |

**your product example for "Live Group Engagement Rooms":**
M1: Working audio prototype with 5+ simultaneous users
M2: Moderation tools and content safety layer
M3: Engagement room creation and discovery flow
M4: Notification and scheduling flow
M5: Launch-ready polish and performance optimization

#### 4. Tradeoff Guardrails

Pre-establish which dimension is fixed and which is flexible:

- **Delivery time:** Fixed when external deadline exists. Flexible otherwise.
- **Scope / feature richness:** Fixed when minimum feature set is required for value. Flexible when value can be delivered smaller.
- **Quality of experience:** Fixed when feature touches trust-sensitive areas (payments, health, personal content). Flexible for internal tools or power-user features.

> **For tradeoff decision-making frameworks** (options matrices, reversibility assessment, stakeholder alignment), see **technical-strategy**. This section covers the Tradeoff Guardrails unique to the Dynamic Delivery Plan.

When milestones slip, the guardrails tell you how to respond: if time is flexible, absorb the slip. If scope is flexible, cut to minimum. If quality is fixed, delay to fix.

### The Resource Tradeoff Reality

When milestones slip, resist adding people. Brooks's Law: adding engineers to a late project often makes it later. Default response: (1) reduce scope, (2) extend timeline, (3) add resources only when work is genuinely parallelizable.

---

## Module 3: Execution and Adoption

### The Vector Math of Teams

Each team member is a vector with magnitude (impact/skill) and direction (where they push the product). Maximum output when vectors are aligned. Conflicting vectors cancel out -- brilliant people at cross-purposes can produce zero progress.

Alignment is not a one-time kickoff. It degrades and must be actively maintained. A mediocre aligned team outships a brilliant misaligned team. The leader's primary job during execution: maintaining vector alignment, not doing the work.

> **For meeting cadences, team alignment infrastructure, and collaboration specs**, see **engineering-leadership**. This section covers the Vector Math concept and the three essential meetings unique to big-bet execution.

### Three Essential Meetings

#### 1. Kick-Off Meeting
Start of each major milestone. Full cross-functional team + executive sponsor. Establish shared vision, clarify exit criteria, surface assumptions, confirm roles. Output: everyone can articulate what "done" looks like.

#### 2. Product Reviews
Recurring (weekly/biweekly) throughout execution. Core team presents to executive sponsor. Demonstrate progress, surface blockers, make tradeoff decisions with authority in the room.

**Key skill: Interpreting executive feedback.**

> See **engineering-leadership** for the full Idea/Recommendation/Command framework. In brief: not all executive input carries equal weight. Ideas can be acknowledged and evaluated later. Recommendations should be seriously considered. Commands should be executed.

#### 3. Dependency Touchpoints
Weekly when cross-team work is in flight. Engineering leads from dependent teams. Surface delays, renegotiate timing, identify shared blockers.

### Deliberate Tradeoff Decisions

When tradeoffs arise: (1) name the tradeoff explicitly, (2) present options with consequences, (3) escalate to the right decision-maker using pre-established guardrails, (4) document and communicate the decision.

---

## Module 4: Launch Strategy and Post-Launch Management

### Staged Launch Approaches

Big bets should never launch to 100% of users on Day 1. Johns and Greenberg outline three staging strategies:

**Strategy 1: Staging by Percent of Users**
The most common approach. Roll out to 1% -> 5% -> 25% -> 50% -> 100%. At each stage, monitor crash rate, core engagement metrics, feature-specific metrics, and support ticket volume. Hold at current percentage until metrics stabilize and meet thresholds. Advance on evidence, not schedule.
- **Risk:** Power users in early cohorts may not represent average users.
- **Mitigation:** Monitor segmented metrics. If engagement is high for power users but drops for casual users as you expand, investigate before proceeding.
- **Product application:** For "Daily Engagement Video," roll out: 1% (verify player, CDN, analytics), 5% (monitor completion rate, next-day return), 25% (server load, CDN costs), 50% (full A/B test vs. control on retention), 100% (full launch with marketing).

**Strategy 2: Staging by Customer Segment**
Restrict launch to a specific geography, user type, or behavioral cohort. Choose where feature has highest expected value and lowest blast radius. Avoid segments atypical of the broader user base.
- **Risk:** Segment-specific behaviors may mask problems in broader rollout.
- **Product application:** For "Accountability Partner Matching," start with users who have 30+ day streaks AND have shared a community request recently. Do NOT start with new users (overwhelming) or lapsed users (need re-engagement, not new features).

**Strategy 3: Staging by Technology Platform**
Launch on one platform first (e.g., iOS), learn, then launch on the other. Useful when platform-specific issues are likely or one platform has better instrumentation.
- **Product application:** If iOS users dominate (common for subscription apps), launch on iOS first. If the feature fails on iOS, Android investment is saved.

**Best practice: Combine strategies.** (1) iOS only, (2) 5% of iOS users with 7+ day streak, (3) 25% all iOS, (4) 25% Android, (5) 100% both.

### Pre-Launch Prioritization Tiers

| Tier | Definition | Decision Rule |
|------|-----------|---------------|
| Launch Blocker | Non-negotiable prerequisite | Must complete or delay |
| Critical | Important but deferrable | Complete if time allows |
| Non-Critical | Nice-to-have | Cut from launch scope |

**Anti-pattern: "Everything is a launch blocker."** If >20% of items are blockers, the team has not prioritized. Force-rank.

### Post-Launch Failure Mode Responses

| Response | When to Use | Action |
|----------|------------|--------|
| Optimize in Place | Minor friction, non-critical | Iterate in next release |
| Throttle | Performance degradation under load | Limit traffic while fixing |
| Temporary Block | Significant bug, subset of users | Pause rollout, fix, resume |
| Full Rollback | Critical issue, core experience broken | Revert immediately |

### Measuring Outcomes

1. **Adoption:** Exposure rate, activation rate, depth of engagement
2. **Retention impact:** D1/D7/D30 retention delta for exposed vs. control
3. **Revenue impact:** Free-to-paid conversion, churn reduction, LTV impact
4. **Qualitative:** App Store reviews, support tickets, social media

Based on outcomes:
- **Double down:** Metrics clearly exceed criteria. Invest in optimization, expansion, and marketing. Shift from launch mode to growth mode.
- **Iterate:** Mixed signal. Run targeted experiments: low adoption -> improve discovery; low retention -> improve repeat-use loop; low conversion -> improve premium value prop. Timebox 4-6 weeks. If no improvement, escalate to deprecate.
- **Deprecate:** Clearly not working despite iteration. Remove cleanly. Communicate with adopters. Document learnings. A team that never deprecates is a team that never takes sufficiently ambitious bets.

---

## Decision Tools

### Decision 1: Should We Pursue This Big Bet?

```
Is the problem a Painkiller, Vitamin, or Vegetable?
|
|-- Vegetable -> STOP. Reframe as painkiller or deprioritize.
|
|-- Vitamin -> Do you have hard commitment signals?
|   |-- No -> Run soft commitment test (waitlist, behavioral proxy)
|   |   |-- <10% conversion -> STOP.
|   |   |-- >10% conversion -> Proceed cautiously. Test hard commitment.
|   |-- Yes -> Proceed, monitor early adoption closely.
|
|-- Painkiller -> Do all functions agree on problem framing?
    |-- No -> Problem framing session. Do not proceed until aligned.
    |-- Yes -> Kill criteria defined?
        |-- No -> Define kill criteria first.
        |-- Yes -> PROCEED to Dynamic Delivery Plan.
```

### Decision 2: How Should We Plan This Initiative?

```
Complexity level?
|
|-- Straightforward -> Standard sprint planning.
|
|-- Normal -> Dynamic Delivery Plan with 3 milestones.
|
|-- Complicated -> Spike first (1-3 days).
|   |-- Resolves unknowns -> Estimate with ranges.
|   |-- Deeper unknowns -> Escalate to Very Complicated.
|
|-- Very Complicated -> Throwaway prototype (2-week timebox).
    |-- Succeeds -> Calibrate real estimates. 5 milestones, wide ranges.
    |-- Fails -> Revisit conviction. Consider killing the bet.
```

### Decision 3: How Should We Respond to a Launch Issue?

```
Severity?
|
|-- Low (cosmetic, minor friction) -> Optimize in Place.
|
|-- Medium (degraded for subset) -> Throttle or Temporary Block.
|   |-- Load-related -> Cap rollout, fix performance, resume.
|   |-- Functional -> Pause rollout, fix, regression test, resume.
|
|-- High (core broken, trust issue) -> Full Rollback.
    |-- User data affected -> Communicate within 24 hours.
    |-- No data affected -> Roll back silently. Internal post-mortem.
    |-- Either case -> Do not relaunch until root cause fixed
        AND launch checklist reviewed for gaps.
```

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| Big Bet | Product initiative requiring >1 month engineering with uncertain outcome |
| Product Conviction | Evidence-backed confidence that a bet will succeed, built through customer signals |
| Painkiller | Problem type addressing an acute, urgent customer need |
| Vitamin | Problem type that is nice-to-have but not urgently sought |
| Hard Commitment | Customer signal involving real cost/effort that validates demand |
| Dynamic Delivery Plan | Structured planning artifact with built-in room for change |
| Complexity Assessment | Four-level classification determining planning approach |
| Vector Math of Teams | Framework viewing members as vectors; aligned vectors maximize output |
| Tradeoff Guardrails | Pre-established rules defining which dimension (time, scope, quality) is fixed vs. flexible |
| Staged Launch | Rolling out incrementally by percentage, segment, or platform |
| Launch Blocker | Non-negotiable prerequisite that must complete before any users see the feature |
| Full Rollback | Reverting all changes immediately for critical issues |

---

## Reference Files

- `references/building-product-conviction.md` -- Problem classification, customer signals, stakeholder alignment, kill criteria
- `references/dynamic-delivery-plans.md` -- Complexity assessment, estimation, sequencing, milestones, tradeoff guardrails
- `references/launch-and-post-launch-strategy.md` -- Staged launches, pre-launch tiers, failure mode responses, outcome measurement
