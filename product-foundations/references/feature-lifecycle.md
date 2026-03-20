## Contents
- The Full Lifecycle Overview
- Module 1: Feature Opportunity Validation
  - Step 1: Problem Framing
  - Step 2: User Segmentation
  - Step 3: Assumption Mapping
  - Step 4: Research Approach
  - Step 5: Problem Sizing and Prioritization
  - Step 6: The "Choose Your Game" Gate
- Module 2: Feature Design
  - The Solution Space Entry Criteria
  - Design Principles from JZ + Anand
  - The Spec Template
  - Spec Anti-Patterns
- Module 3: Feature Development
  - The PM's Role During Development
  - The Scope Trade-Off Framework
  - The "Minimum Viable Test" Mindset
  - Working With Engineers and Designers
- Module 4: Feature Launch and Iteration
  - Pre-Launch Checklist
  - The Alpha → Beta → GA Progression
  - Launch Anti-Patterns
  - Post-Launch Iteration
  - Iteration Cadence
- The PM as Decision-Maker

---
# Feature Lifecycle — Deep Reference
*Source: Product Foundations course modules 1–4, JZ + Anand Subramani*

---

## The Full Lifecycle Overview

```
VALIDATION → DESIGN → DEVELOPMENT → LAUNCH → ITERATION
    ↑                                              |
    └──────────────────────────────────────────────┘
                  (iteration feeds next cycle)
```

Every feature is a hypothesis. The lifecycle is the system for forming, testing, and improving that hypothesis as cheaply and quickly as possible.

---

## Module 1: Feature Opportunity Validation

The goal of validation is to answer: **Is this the right problem to solve, and do we understand it deeply enough to design a great solution?**

### Step 1: Problem Framing

Before any research, write a rough problem statement:
- Who is experiencing this problem?
- What is the problem (in terms of the user's experience, not your solution)?
- When and where does it occur?
- How does it affect them?

This is your starting hypothesis. It will almost certainly change after research — that's expected.

**Good problem statement format:**
> "[User type] struggles to [do X] when [context/situation], which causes [emotional/practical consequence]."

**Bad problem statement (solution-baked-in):**
> "Users need a search feature."

### Step 2: User Segmentation

Not all users have the same problem. Before conducting research, define which segment you're investigating.

**Segmentation dimensions:**
- Behavioral: how often they use the product, which features they use
- Motivational: why they use the product (social, financial, personal utility)
- Lifecycle: new users, power users, churned users, returning users
- Demographic: when relevant to the product domain

**Rule:** Research one segment at a time. Mixed-segment interviews produce mixed-up insights.

### Step 3: Assumption Mapping

Before research, surface your assumptions. You have more than you think.

**Four assumption categories:**

| Category | Question | Example |
|----------|----------|---------|
| **Desirability** | Do users want this? | "Daily engagement reminders would increase engagement" |
| **Feasibility** | Can we build this? | "We can detect a user's daily habit pattern from usage data" |
| **Viability** | Is this good for the business? | "This feature will improve 30-day retention by 10%+" |
| **Usability** | Can users figure it out? | "Users will understand how to set a session time preference" |

**Test riskiest assumptions first.** The riskiest assumption is the one that, if wrong, kills the whole idea. Most teams test the easiest assumptions (usability) and skip the hardest (desirability). That's why they build features nobody wants.

### Step 4: Research Approach

Match research method to what you need to learn:

| What you need to learn | Best method |
|----------------------|-------------|
| What problems exist | User interviews, observation, support ticket analysis |
| How severe the problem is | Surveys (quantitative), usage data analysis |
| How users currently solve it | Contextual observation, diary studies |
| Whether your solution direction is right | Concept testing, prototypes |
| Whether your specific design works | Usability testing |

**User interview guide — the core questions:**

Opening (establish rapport and context):
- "Walk me through a typical [day/week] as it relates to [domain]."
- "Tell me about the last time you [core activity]."

Problem exploration:
- "What do you find tedious, stressful, or painful about [activity]?"
- "Walk me through exactly what you do when [situation occurs]."
- "What do you wish was different about how you currently [activity]?"

Depth probing:
- "Why does that matter to you?"
- "What happens when that goes wrong?"
- "How do you handle that today?"

**NEVER ask:** "Would you use a feature that [description]?" — users almost always say yes. It tells you nothing.

### Step 5: Problem Sizing and Prioritization

After research, rank problems by:

```
Value = (Frequency × Severity × Lack of good alternatives)
```

- **Frequency:** How often does this occur? Daily vs. monthly vs. annually
- **Severity:** How much does it hurt when it does occur? Minor friction vs. task failure vs. emotional distress
- **Alternatives:** Does a good solution already exist? Can they work around it easily?

The highest-value problem is frequent, severe, and poorly served by alternatives.

### Step 6: The "Choose Your Game" Gate

Before moving to design, the PM and team must explicitly answer:
1. Is this the highest-value problem we could work on right now?
2. Do we have the right team to solve it?
3. Are we willing to commit to this problem for the next quarter?

This is a deliberate gate — not every validated problem deserves to be built right now.

---

## Module 2: Feature Design

The goal of design is to answer: **What is the smallest, most lovable solution to our highest-value problem?**

### The Solution Space Entry Criteria

Only enter solution space when you can answer all three:
1. What is the exact user problem we're solving? (one sentence, user's why)
2. Who specifically is the user? (persona and context)
3. What does "solved" look like from their perspective? (success state)

### Design Principles from JZ + Anand

**Depth over breadth:** Solve one problem completely rather than three problems partially. The Peanut Butter Principle applies to features within a design too — don't try to cram multiple problem solutions into one feature.

**Medium-native design:** What works on desktop may break on mobile. Design for the context of use. Ask: what is the user doing, what device are they on, what emotional state are they in?

**User misbehavior as signal:** During design and testing, watch for what users do that you didn't intend. Unexpected behaviors often reveal what users find most valuable. Design for what users actually do, not what you intended them to do.

**Build in the pixie dust moment:** Before finalizing any design, identify: where is the moment that will make users want to tell their friends? If you can't identify it, the design isn't ready.

### The Spec Template

A good spec contains:

```markdown
## Feature Name

### Problem
[One sentence: who has what problem in what context with what consequence]

### User's Why
[What does the user actually want to be true? Not what they want to use.]

### Business Why  
[How does this serve the company's goals? Secondary to user's why.]

### Success Metrics
- Primary: [the metric that proves users love this]
- Secondary: [supporting indicators]
- Counter-metrics: [things we must not break]

### Non-Goals
- [Explicitly what this does NOT solve — prevents scope creep]

### User Stories
As a [user type], when [context], I want to [action] so that [outcome].

### Design Requirements
[What must the solution do to satisfy the user's why]
[Not how to build it — what it must accomplish]

### Edge Cases
[What happens when things go wrong?]
[What happens for edge case users?]

### Open Questions
[Decisions that still need to be made, and by whom, by when]

### Assumptions Being Tested
[What must be true for this to work? What are we betting on?]
```

### Spec Anti-Patterns

- **Feature description as problem statement:** "We're adding a search bar" is not a problem statement. It's a solution.
- **Metrics that measure output, not outcome:** "Ship by Q2" is not a success metric. "40% of users who open the search feature find what they're looking for" is.
- **No non-goals:** Without explicit non-goals, scope creep is inevitable.
- **Missing edge cases:** Edge cases found in production are 10× more expensive than edge cases found in spec review.

---

## Module 3: Feature Development

The goal of development is to answer: **Are we building the right thing in the right way, and making good trade-offs as we learn?**

### The PM's Role During Development

During development, the PM is not building. The PM is:
1. **Maintaining problem clarity** — reminding the team what problem they're solving when implementation details start to drift
2. **Unblocking fast** — decisions that take 3 days to make in a meeting should take 30 minutes with the PM available
3. **Making scope trade-offs** — when reality meets the plan, scope must be negotiated intelligently
4. **Staying open to discovery** — sometimes engineers find better solutions while building. Recognize the difference between "scope creep" and "better solution discovered."

### The Scope Trade-Off Framework

When a new idea or problem surfaces during development:

```
Is this aligned with the user problem we defined?
  → No → Defer. Put it in the backlog. Don't derail the current build.
  → Yes → Does it materially improve lovability?
              → No → Defer. Nice-to-have isn't a reason to extend.
              → Yes → What's the timeline impact?
                          → < 10% of remaining time → Do it.
                          → > 10% → Negotiate: what can we cut to make room?
                                    Cut something of lower lovability impact.
```

### The "Minimum Viable Test" Mindset

Even within development, stay iterative. The first build should be the smallest version that gives you a real signal on lovability — not the fully polished final version.

Build → test internally → confirm direction → polish → ship to beta.

Don't polish before you've confirmed direction.

### Working With Engineers and Designers

**With engineers:**
- Come to conversations with clear "what" (requirements), not "how" (implementation)
- Surface constraints early — "I need X to happen by Y" not "build it this way"
- Respect technical judgments on implementation; make product judgments on priority
- Fast unblocking > perfect decisions. A good decision now beats a perfect decision next week.

**With designers:**
- Design and product should be in problem space together, not just solution space
- Designers often see user problems PMs miss — bring them into user research
- Critique designs on whether they solve the user problem, not on aesthetic preference
- "Does this deliver the user's why?" is a better design critique question than "I don't like how this looks"

---

## Module 4: Feature Launch and Iteration

The goal of launch is to answer: **Does this feature deliver the lovability we designed for, and what do we learn to make the next iteration better?**

### Pre-Launch Checklist

Before shipping anything:
- [ ] Success metrics defined and instrumented
- [ ] Counter-metrics defined and instrumented
- [ ] Beta user group identified
- [ ] Rollout plan defined (what % of users, in what order)
- [ ] Rollback plan exists (what happens if something breaks)
- [ ] Support team briefed (they hear from users before analytics do)
- [ ] "What we're watching for" list written (not just success metrics — surprises)

### The Alpha → Beta → GA Progression

**Alpha phase (days 1–7 typically):**
- Audience: your most loyal, enthusiastic users
- Goal: catch major bugs, confirm basic functionality, get directional signal
- Signal quality: low (these users love you no matter what)
- Key question: "Is this fundamentally broken?"

**Beta phase (weeks 1–4+ typically):**
- Audience: regular users who have experienced friction and remember it
- Goal: validate lovability, test pixie dust, identify high-friction moments
- Signal quality: high — they're honest and representative
- Key question: "Are users getting the 'when can I use this' reaction?"
- Stay here longer than feels comfortable

**GA phase:**
- Audience: everyone, including skeptics
- Goal: grow adoption, compound on what you've validated
- Prerequisite: strong beta evidence of lovability
- Risk: launching unlovable features to GA burns trust permanently

### Launch Anti-Patterns

**The big bang launch:** Shipping to everyone at once. You lose the ability to learn and iterate before you've committed publicly.

**The stealth launch:** Shipping with no observation plan. You ship, metrics tick up, you move on. No learning happened.

**The premature GA:** Moving from beta to GA as soon as the feature is technically stable. Technical stability ≠ lovability. Stay in beta until you have lovability evidence.

### Post-Launch Iteration

Plan for iteration from day one. No feature is finished at launch.

**The iteration signal hierarchy:**
1. **User behavior** (what users actually do) — most honest signal
2. **User feedback** (what users say) — honest if from beta, less so from alpha
3. **Support tickets** (what users complain about) — lagging but high-signal
4. **Analytics** (what the numbers say) — broad but shallow

**What to look for post-launch:**
- Unexpected user behavior (what are they doing with this that you didn't design for?)
- Drop-off points (where are users abandoning the feature flow?)
- Delight signals (what are users sharing or commenting on positively?)
- The "tell a friend" behavior (referral, social share, app store review)

**The unexpected feature trap:**
Often the most lovable part of a feature is something you didn't plan. The Airbnb host message templates were discovered during user research as an afterthought — and became one of the most-loved features in the host app redesign. Stay curious post-launch. Track what users are using in ways you didn't expect.

### Iteration Cadence

```
Week 1 post-launch: Fix bugs, watch for major issues, gather raw feedback
Week 2–3: Pattern the feedback, identify top 3 iteration opportunities
Week 4: Prioritize iterations using the validation framework (restart cycle)
```

The feature lifecycle is a loop. Each iteration restarts the validation phase at a higher level of knowledge.

---

## The PM as Decision-Maker

Throughout the lifecycle, the PM makes hundreds of small decisions. The quality of those decisions is the job.

**Decision-making principles (from Anand Subramani's Stanford teaching):**

1. **Make decisions at the right altitude.** Some decisions belong to the PM. Some belong to the team. Some belong to leadership. Know which is which before you escalate or override.

2. **Disagree and commit.** When the team has debated and you've made a call, commit fully — even if you had reservations. Hedge-shipping (building something you're not sure about half-heartedly) produces neither good products nor good signals.

3. **Document your reasoning.** Decisions you can't explain are decisions you haven't made yet. Write down why — for the team's alignment and for your own retrospective.

4. **Make the reversible/irreversible distinction.** Low-stakes, reversible decisions should be made quickly. High-stakes, hard-to-reverse decisions deserve more process. Most product decisions are more reversible than they feel.

5. **Communicate proactively.** The people affected by a decision should hear about it from you before they see it in the product. Surprises erode trust. Heads-up conversations build it.
