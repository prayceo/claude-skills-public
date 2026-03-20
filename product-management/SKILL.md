---
name: product-management
description: Applies Mastering Product Management frameworks to senior PM deliverables, including stakeholder communication and storytelling. Courses created by Sachin Rekhi (LinkedIn Sales Navigator, $200M ARR, 500 employees) and Tara Wellington (VP Product at BILL, Executive Partner), hosted by Michael Sippey (VP Product at Twitter, Medium, Descript). Activates for senior PM deliverables — 4D roadmaps, empowering product specs, OKR loops, lever dashboards, stakeholder narratives, product vision, and executive presentations. Triggers proactively when reviewing product deliverables, planning quarters, diagnosing why a roadmap feels incremental, preparing for leadership reviews, or crafting any product communication at your company. For PM fundamentals (first specs, basic roadmaps, learning OKRs), use product-foundations. For PM leadership (portfolio strategy, coaching, team composition), use product-strategy-leadership.
---

**Reference files:**
- `references/product-strategy-and-vision.md` — 6 PMF hypotheses, Product Strategy Map, Vision Narratives, buy-in framework
- `references/4d-roadmaps.md` — 4D roadmap system: 4 lenses, constrained brainstorm, KPI targets, OKR learning loop, decision architecture
- `references/stakeholder-communication.md` — Story arc, audience adaptation, stakeholder cascade, communication planning, delivery tactics
- `references/lever-dashboards-specs-and-feedback.md` — Lever dashboards, empowering product specs, Sippey's feedback management system

---

## How to Use This Skill

When this skill activates:
1. Identify which product management framework from this skill best applies to the question
2. Apply the relevant decision tree from the Decision Tools section
3. Ground all recommendations in the context of your product
4. Cite the specific framework when making claims
5. If deeper detail is needed, read the relevant reference file before responding

## Gotchas

Common mistakes to avoid when applying these frameworks:

1. **Don't build a 4D roadmap without constraining to target KPIs first.** Rekhi's system requires selecting 2-3 target KPIs *before* brainstorming from the four lenses. Without this constraint, the 4D process degenerates into a longer version of the same incremental brainstorm it was designed to replace.
2. **Don't write OKRs without explicit predictions.** The OOKRS learning loop only works if teams write down what they *predict* each initiative will do to each metric before the quarter starts. Without predictions, the postmortem teaches nothing -- you can't learn from surprise if you never stated your expectations. OKRs without predictions are just alignment theater.
3. **Don't default to the Problem-Solution story archetype.** Wellington provides five archetypes (Opportunity, Problem-Solution, Vision, Progress, Parallel), and PMs tend to default to Problem-Solution for everything. At your company, the Parallel Story -- interweaving a user's personal journey with business metrics -- is often the most powerful archetype for executive audiences.
4. **Don't skip the 30-meeting sprint before a major build.** Sippey's rule is specific: pattern recognition emerges around meeting 10, segmentation around 20, and clarity on what to build around 30. Most teams do 3-5 interviews and call it validated. If your product is building a major new feature, 30 conversations is the minimum to avoid building on shallow assumptions.

## Example

**User asks:** "I need to present our Q3 product roadmap to the leadership team. How should I structure it?"

**Approach:**
1. Verify the roadmap was built using Rekhi's 4D process -- check that items come from all four lenses (Strategy, Vision, Customer, Business) and are constrained to 2-3 target KPIs. If the roadmap is only Customer + Business lens items, flag that it's likely incremental and missing needle-movers
2. Apply Wellington's story archetype selection -- if leadership is familiar with the product direction, use the Progress Story (what we learned last quarter, what shifted, what's next); if presenting a new strategic direction, use the Vision Story (paint the full picture)
3. Structure using the product story arc: hook (one surprising insight from Q2), context (where we are on target KPIs), tension (what's not working or what opportunity we're missing), proposal (the Q3 roadmap as the response), ask (specific resources or decisions needed)
4. Apply the 10-2-1 Rule for executive delivery -- 10 minutes, 2 key points, 1 clear ask. Prepare the full 30-minute version for the product team separately using audience adaptation principles

---

## Core Philosophy: The PM's Four Dimensions

Sachin Rekhi's foundational definition of the PM role — everything maps to one of these:

```
Vision      -> What future are we building toward?
Strategy    -> How will we win our market?
Design      -> What exactly will we build?
Execution   -> How do we ship and iterate?
```

**The core insight:** Most PMs perform the activities associated with each dimension, but don't treat them as concrete deliverables. When you treat each as a deliverable — something to craft, refine, and share — you unlock a different level of quality and alignment.

---

## Module 1: Product Strategy Map + Vision Narratives

A product strategy is a set of **product/market fit hypotheses** you constantly refine — not a static document. Every strategy needs answers to six dimensions: problem to solve, target audience, value proposition, competitive advantage, growth strategy, and business model. The **coherence test** validates the strategy: (1) Does the problem resonate with the target audience? (2) Does the value prop solve the problem? (3) Does the business model enable the growth strategy?

A **vision narrative** is 1-2 pages of prose (not bullet points) covering: the world today, current product value, the future state, and the path to get there. Prose forces narrative structure, prioritization, and specificity that bullet points never do.

*-> Full detail: `references/product-strategy-and-vision.md`*

---

## Module 2: Lever Dashboards + Feedback Management Systems

**Lever dashboards** are the PM's core analytical tool — three dashboards (acquisition, engagement, monetization) reviewed daily to build product intuition. Unlike standard analytics, lever dashboards focus on *input metrics* you can actually move, connected to the outcomes you're targeting. Daily review builds the intuition to recognize anomalies before they compound.

**Feedback management** centers on Sippey's rule: talk to at least one customer a day. His 30-meeting sprint requires 30 customer conversations before writing code — pattern recognition emerges around meeting 10, segmentation around 20, and clarity on what to build around 30. The 55-minute meeting structure spends over half the time on the customer's problem, not your solution.

*-> Full detail: `references/lever-dashboards-specs-and-feedback.md`*

---

## Module 3: 4D Roadmaps + Empowering Product Specs

**4D Roadmaps** solve the incrementalism problem with RICE/voting by brainstorming from four lenses (Strategy, Vision, Customer, Business), all constrained to 2-3 target KPIs. Customer + Business lenses = "keep the lights on." Strategy + Vision lenses = "the something big." A healthy roadmap has work from all four.

**Empowering product specs** require five elements: the problem, target audience, rationale, success metrics, and experience details. Specs are a forcing function for clarity — include explicit design principles that capture key tradeoffs so designers understand guardrails, not just requirements.

*-> Full 4D system: `references/4d-roadmaps.md`*
*-> Specs and feedback detail: `references/lever-dashboards-specs-and-feedback.md`*

---

## Module 4: OKR Loops + Decision Architecture

**OOKRS** (outcomes-focused OKRs) turn OKRs from a goal-setting tool into a learning loop. The key: write explicit predictions before the quarter starts ("We believe initiative X will move metric Y by Z"), then run a postmortem comparing predictions to results. Teams that don't predict don't learn. The OKR Learning Loop: Set OOKRS -> Execute -> Measure -> Postmortem -> Feed learning into next roadmap. This is how product intuition compounds.

**Decision architecture:** The PM's job is to create a system where the best ideas win. The critical discipline is communicating decision *rationales*, not just decisions — this builds trust, documents assumptions, and creates organizational learning. Match decision velocity to decision type: fast for reversible/low-stakes, slow for irreversible/high-stakes.

*-> Full OKR and decision frameworks: `references/4d-roadmaps.md`*

---

## Module 5: Stakeholder Communication and Storytelling

Wellington's core insight: PMs are surrounded by communication, but most is information transfer, not influence. The **product story arc** (hook, context, tension, proposal, ask) is the delivery vehicle for every PM deliverable. Five **story archetypes** match common PM situations: Opportunity, Problem-Solution, Vision, Progress, and Parallel. The **Parallel Story** is most powerful at your company — interweaving the user's personal journey with business metrics.

**Audience adaptation** is critical: leadership needs recommendation-first in 5-10 minutes with business framing; your team needs user-problem-first in 30-60 minutes with full context; stakeholders need function-relevant framing in 15-30 minutes. The **stakeholder cascade** sequences communication by influence level, checking reactions at each phase before advancing.

*-> Full communication frameworks: `references/stakeholder-communication.md`*

---

## The 7 Core PM Deliverables

From Rekhi's framework — the concrete outputs a PM is accountable for, mapped to dimension:

| Deliverable | Dimension | What makes it great |
|------------|-----------|---------------------|
| **Vision Narrative** | Vision | 1-2 pages of prose; state of world + future state + path; inspiring story |
| **Product Strategy Map** | Strategy | 6 PMF hypotheses that are coherent with each other; constantly iterated |
| **Customer Insights** | Strategy/Design | Quality and quantity of valuable surprises from real customer conversations |
| **Product Roadmap** | Execution | 4D balanced; constrained to target KPIs; has a coherent story |
| **Product Specs** | Execution | Problem + audience + rationale + success metrics + experience details |
| **Metric Dashboards** | Execution | 3 core dashboards (acquisition, engagement, monetization) reviewed daily |
| **Team OKRs (OOKRS)** | Execution | Outcomes-focused; predictions made upfront; postmortem runs learning loop |

**The connector:** Every deliverable requires stakeholder communication to be effective. The deliverable is the substance; the story arc is the delivery vehicle. Wellington's storytelling frameworks (Module 5) are how each deliverable achieves its purpose.

---

## Decision Tools

### Is this roadmap incremental?

```
Can you trace every item on the roadmap to a target KPI?
  -> No -> Roadmap wasn't built with top-down constraint; redo with 4D process

Do you have items from all four lenses (strategy, vision, customer, business)?
  -> Missing strategy or vision lens -> roadmap is likely incremental
  -> All customer and business lens -> short-term focus; missing needle-movers

Does the roadmap tell a coherent story to leadership?
  -> No -> Objectives aren't connected; can't explain the roadmap as a whole
```

### Is the product strategy compelling?

```
Are all 6 PMF hypotheses documented?
  -> No -> Incomplete strategy; missing pieces will create blind spots

Do the 3 coherence questions pass?
  -> Does the problem resonate with the target audience?
  -> Does the value proposition solve the problem?
  -> Does the business model enable the growth strategy?
  -> Any "no" -> weak link that will undermine the strategy
```

### Are we doing enough customer discovery?

```
When did you last talk to a customer who surprised you?
  -> More than 2 weeks ago -> insufficiently frequent discovery

What's the ratio of confirming interviews to surprising interviews?
  -> Mostly confirming -> you're asking the wrong questions or the wrong people

Have you completed the 30-meeting sprint before your current major build?
  -> No -> you don't yet know what to build
```

### Are OKRs building product intuition?

```
Did you write down predictions before the quarter started?
  -> No -> the postmortem won't teach you anything
  -> Yes -> run postmortem: what did your predictions get right vs. wrong?

Does the postmortem update the next roadmap?
  -> No -> the learning loop is broken; OKRs are just alignment theater
  -> Yes -> this is how product intuition compounds
```

### Which story archetype should I use?

```
What is the purpose of this communication?

  "I want to pitch a NEW initiative"
    -> Is the market opportunity clearly sized?
      -> Yes -> Opportunity Story (lead with market size)
      -> No -> Problem-Solution Story (lead with user pain)

  "I want to present our ROADMAP or strategy"
    -> Is the audience familiar with our direction?
      -> Yes -> Progress Story (build on what they know)
      -> No -> Vision Story (paint the full picture)

  "I want to REPORT on results"
    -> Progress Story (key metric, what surprised us, what's next)

  "I want to BUILD ALIGNMENT across functions"
    -> Parallel Story (user story + business story = same story)
```

### How should I handle stakeholder resistance?

```
What type of resistance am I encountering?

  "They don't believe the data"
    -> Is the data solid?
      -> Yes -> Present methodology; offer to walk through analysis
      -> No -> Acknowledge gaps; propose additional research

  "They say it doesn't align with strategy"
    -> Can you connect to an existing strategic pillar?
      -> Yes -> Show the connection explicitly
      -> No -> Propose adding a pillar or adjust the initiative

  "They say we can't afford it"
    -> Propose a phased approach (MVP first)
    -> Show the cost of inaction
    -> Compare to ROI of the next-best alternative

  "They're not saying no but not saying yes"
    -> Make the ask smaller and more specific
    -> Ask: "What would you need to see to feel confident?"
    -> Set a decision deadline
```

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **Product Strategy Map** | The 6 PMF hypotheses (problem, audience, value prop, competitive advantage, growth strategy, business model) treated as living documents |
| **Vision Narrative** | 1-2 page prose document covering: world today, current product value, future vision, path to get there |
| **4D Roadmap** | Roadmap built from four lenses (Strategy, Vision, Customer, Business) constrained to target KPIs |
| **Lever Dashboard** | The 3 core dashboards (acquisition, engagement, monetization) reviewed daily to build product intuition |
| **OOKRS** | Outcomes-focused OKRs treated as a learning loop: predict, execute, postmortem, update strategy |
| **Feedback Management System** | Structured, ongoing system for customer discovery; Sippey's rule: at least one customer conversation daily |
| **The 30-Meeting Sprint** | Sippey's framework: set up 30 customer meetings before writing code; pattern recognition only emerges at scale |
| **Decision Rationale** | The documented reasoning behind a decision; as important as the decision itself for building team trust and learning |
| **Coherence Test** | Three questions that reveal whether the 6 PMF hypotheses are working together as a strategy |
| **OKR Learning Loop** | Predict, execute, measure, postmortem, feed learning into next roadmap — the mechanism for building product intuition |
| **Story Arc** | The five-part sequence for product stories: hook, context, tension, proposal, ask (Wellington) |
| **Story Archetype** | A reusable story pattern (Opportunity, Problem-Solution, Vision, Progress, Parallel) matching common PM communication situations |
| **Parallel Story** | Storytelling technique that interweaves the customer narrative with the business narrative to show they are the same story |
| **Audience Adaptation** | Tailoring story content, structure, and delivery to match each audience's concerns, time, and decision mode |
| **Stakeholder Cascade** | Sequenced rollout strategy: present to audiences in order of influence, checking reactions before advancing |
| **One-Page Product Story** | Single-page document capturing the complete initiative narrative: opportunity, problem, evidence, proposal, impact, ask, risks, timeline |
| **10-2-1 Rule** | Executive presentation constraint: 10 minutes, 2 key points, 1 clear ask |

---

## Reference Files

- `references/product-strategy-and-vision.md` — 6 PMF hypotheses in depth, coherence test, vision narrative structure, buy-in framework (substance + style)
- `references/4d-roadmaps.md` — Full 4D system: lens details, over-indexing signals, constrained brainstorm process, OKR learning loop, decision architecture
- `references/stakeholder-communication.md` — Story arc and archetypes, audience adaptation, stakeholder cascade, communication planning, delivery tactics, one-page product story template
- `references/lever-dashboards-specs-and-feedback.md` — Lever dashboards (3 core dashboards), empowering product specs (required elements, design principles), Sippey's feedback management system (30-meeting sprint, 55-minute meeting structure)
