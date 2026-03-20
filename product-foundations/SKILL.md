---
name: product-foundations
description: Applies Product Foundations frameworks to any product decision, from opportunity discovery through feature launch and iteration. Activates for junior/mid PM fundamentals — first time writing a spec, first roadmap, learning OKRs, validating a feature idea, designing and prioritizing features, running user research, or developing as a PM. Also triggers when evaluating a product decision or building anything at your company — this skill applies across the full feature lifecycle. For senior PM deliverables (4D roadmaps, stakeholder narratives, OKR loops), use product-management. For PM leadership (portfolio strategy, coaching, team composition), use product-strategy-leadership.
---

**Sources:** First Round Review "Don't Serve Burnt Pizza" (JZ), Lenny's Podcast episode (JZ), Stanford PM course (JZ + Anand), Product Foundations course syllabus

**Reference files:**
- `references/mlp-framework.md` — Full Minimum Lovable Product system
- `references/feature-lifecycle.md` — Validation → Design → Development → Launch → Iteration
- `references/pm-craft.md` — OKRs, roadmaps, career, first 90 days, working with stakeholders

---

## How to Use This Skill

When this skill activates:
1. Identify which product foundations framework from this skill best applies to the question
2. Apply the relevant decision tree from the Decision Tools section
3. Ground all recommendations in the context of your product
4. Cite the specific framework when making claims
5. If deeper detail is needed, read the relevant reference file before responding

## Gotchas

Common mistakes to avoid when applying these frameworks:

1. **Don't confuse MVP with MLP.** JZ's framework says MVP is about learning whether a problem exists; MLP is about learning whether users *love* your solution. Shipping a lovable product to the wrong audience is bad, but shipping a "burnt pizza" MVP when users have alternatives (they always do at your company) gives you feedback on the flaws, not the idea.
2. **Don't open solution space before fully mapping problem space.** JZ's two-column exercise deliberately blocks the right column (solutions) until the left column (problems) is exhaustively mapped and force-ranked. Jumping to "what if we built X?" before answering "what is the highest-value problem?" is the single most common PM mistake.
3. **Don't rush from Beta to GA.** JZ warns that launching buggy features to GA is "crying wolf" -- you burn user trust that's hard to regain. At your company, where the app is part of someone's daily daily practice, a broken GA launch doesn't just lose users, it disrupts a intentional routine. Stay in beta longer than feels comfortable.
4. **Don't mistake "this is cool" for lovability.** JZ's lovability signal is specific: "Oh my god, when can I start using it?" means lovable. "This is cool, I can see myself using this" means you haven't found a high-value problem or the right solution. If beta testers at your company say the latter, iterate before going wider.

## Example

**User asks:** "We want to build a personal journaling feature for your product. Where do we start?"

**Approach:**
1. Apply JZ's Pillar 1 (Start with the user's why) -- complete the sentence "Wouldn't it be amazing if your product could ___?" and verify the blank ends with user value, not business value like "increase engagement"
2. Use the Problem/Solution Separation Exercise -- list all problems personal journaling might solve (users forget what they engaged for, users want to see answered engagements over time, users feel disconnected between sessions) without discussing solutions, then force-rank by value
3. Apply the MLP lens -- identify the one problem to solve lovably, define the pixie dust moment (e.g., the first time a user sees their milestone achieved and marked in their journal), and use the Peanut Butter Principle to resist spreading across all journaling use cases
4. Recommend progressive release: alpha with loyal daily users, extended beta to validate the "when can I use this?" reaction, GA only after clear lovability signal

---

## The Course in One Sentence

> Product management is the discipline of understanding what to build, working with a team to build it well, and getting it to market effectively.

The course follows a single feature all the way through its lifecycle: **Validation → Design → Development → Launch → Iteration** — grounded in a set of foundational pillars that govern every stage.

---

## The Product Development Pillars

Everything in the course rests on three non-negotiable pillars:

### Pillar 1: Start with the user's why
Every product decision must be rooted in a genuine user problem — not a business goal dressed up as a user need. The business "why" and the user "why" are different things. Great PMs hold both, but always start with the user.

**The litmus test:** Complete this sentence:
> "Wouldn't it be amazing if this product could ___?"

The blank must end with **value for the user**, not value for the business. If it ends with "help us compete with X" or "grow our revenue," you haven't found the user's why yet.

### Pillar 2: Separate problem space from solution space
The single most common PM mistake is jumping to solutions before fully understanding the problem. Solutions feel productive. Problem exploration feels slow. But solutions built on shallow problem understanding consistently miss the mark.

**The two-column exercise:**
```
LEFT COLUMN (problems only)  |  RIGHT COLUMN (solutions — blocked)
-----------------------------|-----------------------------------
Users struggle to remember   |  (don't discuss yet)
their streak                 |
Users feel disconnected from |  
their community       |
Users don't know what to     |
engage about today             |
```
Only open the right column once you've fully mapped and ranked the left column.

### Pillar 3: The PM as orchestrator, not hero
PMs don't build — they make building possible. The PM's job is to align everyone toward the right problem and remove friction from the path to solution. Authority comes from clarity, not title.

---

## Framework 1: Minimum Lovable Product (MLP)

*JZ's most cited framework — from "Don't Serve Burnt Pizza," First Round Review*

> "If you serve people burnt pizza, you're not testing whether they like pizza. You're only learning they don't like burnt pizza. Similarly, if you ship an MVP that's flawed or undercooked, you're not testing your product — you're testing a poor version of it."

**MLP vs MVP:**

| | MVP | MLP |
|---|---|---|
| Goal | Validate existence of a problem | Validate that your solution is lovable |
| Risk | Tests a burnt version → wrong signal | Forces deeper problem understanding |
| Output | "Does this work?" | "Do users love this enough to tell others?" |
| Right use | Pre-PMF for pure existence testing | Any time users have alternatives |

**When MLP beats MVP:** We live past the era of "the first X." Users have alternatives in almost every category. Shipping a merely functional product gives you feedback on the wrong thing.

**The four MLP principles:**
1. Start with the user's why, not the business why
2. Separate problem space from solution space
3. Listen to users — but don't take their word literally
4. Enter solution space and choose your game

**The Peanut Butter Principle:**
> "Spread too thin, it's no longer tasty."

An MLP focuses on **one or two features** that deliver the core lovable experience. Trying to solve every problem with a single launch solves none of them well.

**Pixie Dust:**
The moment in the user journey where users realize this product is different from anything they've experienced. Small, well-timed details that exceed expectations. Not generic delight — specific to your user.

Questions to identify pixie dust:
- When a user signs up, what should be the first emotion they feel?
- What would bring a smile to a user's face?
- What would give a user a reason to rave to their friends?

**The lovability signal:** You're aiming for users to say "Oh my god, when can I start using it?" — not "This is cool, I can see myself using this." The second response means you haven't solved a high-value problem.

**For your product — MLP lens:**
- Is the daily engagement experience lovable, or just functional?
- What's the single moment that makes a user want to tell their expert/friend about your product?
- What does pixie dust look like at 6am when someone opens the app for the first time?

*→ Full MLP playbook: `references/mlp-framework.md`*

---

## Framework 2: Feature Opportunity Validation

*Module 1 of the course — the discipline before you write a single spec*

**The validation sequence:**
```
1. Problem framing       → What is the exact problem we're solving?
2. User segmentation     → Who specifically has this problem?
3. Problem sizing        → How many people? How painful? How often?
4. Solution hypothesis   → What's our initial belief about a solution?
5. Assumption mapping    → What must be true for this to work?
6. Validation approach   → How do we test assumptions cheaply?
```

### User Research — Listen but Not Literally

Three common user research mistakes:
1. **Asking what they want** → Users describe solutions, not problems. You get feature requests, not insight.
2. **Positioning yourself as the expert** → Users defer to you. You lose the real data.
3. **Mixing personas** → Feedback from different user types cancels out and confuses signal.

**The right question to ask:**
> "What do you find tedious, stressful, or painful?"

If a user says "I can't believe I spend so many hours on this" — you've found a high-value problem.

**The "not literal" principle:**
Users often request solutions, not problems. Henry Ford's aphorism applies: "If I had asked people what they wanted, they would have said faster horses." Listen for emotional signals (frustration, joy, embarrassment, pride) — those reveal the real problem.

### Embrace User Misbehavior
When users interact with your product in ways you didn't intend, they're often signaling what they find most lovable. At Pocket Gems, users kept tapping on fog-shrouded objects that weren't interactive — a signal that led to entirely new game mechanics.

**Watch for:** Users who use your product for purposes you didn't design for. They're your most valuable informants.

### Assumption Mapping

Before validating anything, map your assumptions:

```
Desirability assumptions:  Users want this
Feasibility assumptions:   We can build this
Viability assumptions:     This is good for the business
Usability assumptions:     Users can figure out how to use this
```

Test the **riskiest** assumptions first — not the easiest. The riskiest assumption is the one that, if wrong, would kill the whole idea.

### Validation Technique: Problem/Solution Separation Exercise

Draw a vertical line. Left side = problems only. Right side = solutions (blocked from discussion).

1. Brainstorm all problems — no filtering, no solutions
2. Force ranking: which problem is highest-value to solve?
3. Sanity check: "Is this the game we want to play for the next quarter?"
4. **Only then:** open the right side and brainstorm solutions

*→ Full lifecycle playbook: `references/feature-lifecycle.md`*

---

## Framework 3: Feature Design

*Module 2 — translating problem clarity into a designed solution*

Follow the double-diamond: `Diverge (problems) → Converge (highest-value problem) → Diverge (solutions) → Converge (lovable solution)`. Only enter solution space when you can answer: what is the single highest-value problem, who is the user, and what does "solved" look like from their perspective?

Key principles: "Minimum" means fewer problems addressed, not fewer features. Pick one problem, solve it lovably. Match medium to moment (mobile vs. desktop context). Every spec must cover: problem, success metrics, non-goals, user stories, edge cases, and open questions.

*→ Full design process and spec template: `references/feature-lifecycle.md`*

---

## Framework 4: Feature Development

*Module 3 — shipping well, not just shipping*

The PM's job during development: maintain problem clarity, unblock fast, make scope trade-offs quickly. For scope changes: if aligned with core problem and improves lovability, accept if <10% timeline impact; otherwise negotiate cuts. Every sprint should have a minimum viable test — the smallest version that gives a real signal on lovability.

*→ Full scope trade-off framework: `references/feature-lifecycle.md`*

---

## Framework 5: Feature Launch & Iteration

*Module 4 — testing, learning, and compounding*

Progressive release: Alpha (loyal users, early signal only), Beta (your most valuable testing group — stay here longer than feels comfortable), GA (unforgiving audience, don't rush). Launching buggy features to GA is "crying wolf" — you burn trust that's hard to regain. Plan for 2-3 post-launch iterations. Stay curious about unexpected user behavior during launch — it often signals the next iteration.

*→ Full launch playbook and iteration cadence: `references/feature-lifecycle.md`*

---

## Framework 6: OKRs — Setting Ambitious Goals

*From JZ's Lenny's Podcast episode and Stanford course*

Objectives are qualitative and ambitious (should make you uncomfortable). Key Results are quantitative, measurable, 3-5 per objective, achievable ~70% of the time. JZ's principles: start with user outcomes not product outputs ("Reduce time to first engagement completion by 40%" not "Ship 3 features"), make OKRs crisp enough to force trade-offs, 70% attainment is success, cascade don't dictate.

*→ Full OKR system: `references/pm-craft.md`*

---

## Framework 7: Roadmaps as Storytelling

*From JZ's Lenny's Podcast episode*

A roadmap is a narrative arc, not a feature list. The reader should understand: what user problem are we solving, why this sequence, and what does success look like? Saying yes to roadmap items means saying no to everything not on it — make the nos explicit. Common failures: no connective tissue between features, serving internal requests over user problems, no deprioritization rationale.

*→ Full roadmap framework: `references/pm-craft.md`*

---

## Framework 8: The First 90 Days Playbook

*From JZ's Lenny's Podcast and public talks*

Three modes: Weeks 1-4 listen and map (don't ship or opine), Weeks 5-8 form hypotheses about highest-value problems, Weeks 9-12 act by shipping one small thing that demonstrates judgment. Trust is built in the listening phase — the biggest mistake is shipping too fast to prove value.

*→ Full 90-day playbook: `references/pm-craft.md`*

---

## PM Career Phases

*From JZ's First Round podcast and public talks*

Three phases requiring fundamentally different skills: (1) Contributing PM — understand what to build, ship features users love; (2) Managing PMs — multiply others' effectiveness through coaching and alignment; (3) Leading the function — treat the product org as a product. JZ's meta-framework: treat your career like a product — who are you building for, what problem gives you energy, what's your north star?

*→ Full career framework: `references/pm-craft.md`*

---

## Decision Tools

### Is this the right problem to solve?
```
Can you articulate the user's why in one sentence?
  → No → Keep digging. You don't understand the problem yet.
  → Yes → Is it a high-value problem? (frequent + painful + no good alternatives)
              → No → Deprioritize. Solving a low-value problem perfectly is still a waste.
              → Yes → Is this the game we want to play for the next quarter?
                          → No → Table it. Intentionality about problem choice matters.
                          → Yes → Begin solution space ideation.
```

### Is this solution lovable?
```
When users see the prototype, do they say:
"This is cool, I can see using this" → Not lovable enough. Wrong problem or wrong solution.
"Oh my god, when can I use this?" → Lovable. Proceed.
```

### Is this feature ready to ship?
```
Did we validate it with beta users (not just alpha)?
  → No → Stay in beta. Don't rush to GA.
  → Yes → Are we getting the "when can I use this" reaction?
              → No → Iterate before going wide.
              → Yes → Ship. Plan iteration cadence from day one.
```

### Is my spec good enough?
```
Does it clearly state the user problem (not the feature description)?
Does it define what success looks like in measurable terms?
Does it list explicit non-goals?
Does it surface the riskiest assumptions?
Would an engineer who'd never talked to me understand what to build?
  All yes → Good spec. Ship it.
  Any no → Rewrite that section.
```

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **MLP** | Minimum Lovable Product — the smallest thing users could love, not just use |
| **Burnt pizza test** | Shipping a flawed MVP gives feedback on the flaws, not the underlying idea |
| **User's why** | The emotional/practical reason a user needs your product; distinct from business why |
| **Problem space** | The exploration phase — fully mapping user problems before considering solutions |
| **Solution space** | The ideation phase — opened only after problem space is fully mapped |
| **Pixie dust** | The moment in the user journey that exceeds expectations and makes the product memorable |
| **Peanut butter principle** | Spreading features too thin across too many problems makes them all tasteless |
| **Alpha/Beta/GA** | Progressive release stages; beta is the key validation stage, not GA |
| **Lovability signal** | "When can I use this?" vs. "This is cool" — only the first means you've hit it |
| **User misbehavior** | Unexpected user actions that signal what they actually want |

---

## Reference Files

- `references/mlp-framework.md` — Complete MLP system with all four principles, exercises, and examples
- `references/feature-lifecycle.md` — Full Validation → Design → Development → Launch → Iteration playbook
- `references/pm-craft.md` — OKRs, roadmaps, first 90 days, career phases, stakeholder management
