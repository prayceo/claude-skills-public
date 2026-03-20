---
name: growth-experimentation
description: >
  Unified growth experimentation system covering strategy, statistical rigor, growth engineering execution, and organizational scaling.
  Merges Fareed Mosavat's strategic experimentation frameworks, Elena Verna's PLG experimentation principles, and Alexey Komissarouk's growth engineering practices.
  Activates when you need to design rigorous experiments, build growth engineering infrastructure, prioritize experiment backlogs, scope growth features for speed, or scale experimentation across the organization.
---

**Reference files:**
- `references/experiment-design-and-statistical-rigor.md` -- A/B testing mechanics, sample size calculation, statistical pitfalls deep dive, experiment templates, and the complete decision analysis framework
- `references/growth-engineering-patterns-and-velocity.md` -- Scope Ladder, reusable growth patterns (paywall/onboarding/notification/referral), tent vs. skyscraper code quality, technical debt management, and velocity optimization
- `references/scaling-experimentation-org-and-culture.md` -- Growth team structure, Writer's Room model, hiring growth engineers, experiment pipeline operations, portfolio management, and building experimentation culture

---

## How to Use This Skill

When this skill activates:
1. Identify which experimentation or growth engineering framework best applies to the question (experiment design, statistical rigor, scoping, or scaling)
2. Apply the relevant decision tree from the Decision Tools section
3. Ground all recommendations in the context of your product
4. Cite the specific framework when making claims
5. If deeper detail is needed, read the relevant reference file before responding

## Gotchas

Common mistakes to avoid when applying these frameworks:

1. **Designing a statistically rigorous test that answers the wrong question:** Mosavat's central warning is that the most dangerous failure mode is a well-designed A/B test answering an irrelevant strategic question. Before recommending sample sizes and test durations, first validate that the experiment connects to a strategic question using the Experiment Quality Scorecard.
2. **Running experiments shorter than full weekly cycles for your product:** Engagement Session usage has strong day-of-week patterns (weekday vs. weekend). Running a test for 10 days captures one full week plus three extra days, biasing results. Always run in 7-day or 14-day multiples to capture complete weekly engagement session patterns.
3. **Over-scoping the first version of an experiment:** Komissarouk's Scope Ladder exists because over-scoping is the number one velocity killer. A new paywall hypothesis does not need a fully engineered paywall system -- start with a Painted Door test or Wizard of Oz before investing engineering time. Most experiments (~70%) lose, so compound learnings by running more, not building more.
4. **Peeking at results mid-experiment and calling a winner early:** Peeking inflates false positive rates dramatically. Mosavat lists peeking as the first of six major statistical pitfalls. Pre-commit to the test duration and decision criteria before launch -- if a stakeholder wants to end early, that is the Opinionist's Veto anti-pattern.

## Example

**User asks:** "We want to test whether a new onboarding flow improves Day 7 retention. How should we set this up?"

**Approach:**
1. Apply the Experiment Design Canvas: define the strategic context (why onboarding matters now), write a structured hypothesis with a "because" clause ("We believe [new flow] will improve D7 retention because [it delivers the aha moment faster]"), set D7 retention as the primary metric with daily engagement completion rate and subscription conversion as guardrails
2. Scope using the Scope Ladder: if the new flow is a significant redesign with low confidence, start with a Wizard of Oz version (manually curated first experience) before building the full flow
3. Calculate sample size for the minimum detectable effect, and set duration in 14-day multiples (to capture two full weekly cycles plus the full D7 measurement window)
4. Pre-commit to decision criteria: define what "win," "lose," and "inconclusive" mean before launch, and document in the experiment brief so the team cannot rationalize a neutral result into a ship decision

---

## Core Philosophies

**Mosavat:** Experimentation is a strategic discipline, not a statistical one. The most dangerous failure is a well-designed test that answers the wrong question. Teams that run hundreds of experiments without connecting them to product strategy are practicing "experiment theater."

**Verna:** The growth team's goal is to discover where the mental model of the user diverges most from reality -- not to validate assumptions, but to find perception-reality gaps.

**Komissarouk:** Growth engineering optimizes for speed of learning, not durability. Most experiments fail (~70% lose), so compound learnings by running as many well-designed experiments as possible. "You're not building a skyscraper -- you're building a tent."

---

## Module 1: Experimentation Strategy

*Primary instructor: Fareed Mosavat, with Elena Verna*

The distinction between good and bad experiments is strategic intent, not statistical rigor. A perfectly designed A/B test answering the wrong question is worse than a crude analysis illuminating a strategic truth. Good experiments connect to strategy, build on prior learning, generate reusable insight, and consider system effects. Bad experiments are scattered, stand alone, or defer decisions that should be made with available information.

Key concepts: Experiment Quality Scorecard (7 dimensions, 1-5 scale), the Experimentation Spectrum (from "Just Ship It" through Multi-Variant Sequential Testing), Pre-Commitment Decision Frameworks, and the role of qualitative research in experimentation cycles.

*-> Full detail: `references/experiment-design-and-statistical-rigor.md`*

---

## Module 2: Experiment Design and Statistical Rigor

*Combined from Mosavat, Verna, and Komissarouk*

Every experiment follows the Experiment Design Canvas: strategic context, structured hypothesis (with a "because" clause revealing the team's mental model), primary metric, guardrail metrics, expected impact, MDE, and duration in 7-day multiples. The six major statistical pitfalls are peeking, underpowered tests, multiple testing, Simpson's Paradox, novelty/primacy effects, and survivorship bias.

For your product, run experiments in full 7-day or 14-day cycles to capture weekly engagement session patterns. Key guardrails: daily engagement completion rate, subscription renewal rate, and DAU.

*-> Full detail (templates, sample size formulas, pitfall deep dives): `references/experiment-design-and-statistical-rigor.md`*

---

## Module 3: Growth Engineering Execution

*Primary instructor: Alexey Komissarouk*

Growth engineering optimizes for experiment velocity using the equation: Growth Output = Experiment Velocity x Win Rate x Average Impact per Win. Velocity is the most controllable variable. The Scope Ladder (Painted Door -> Wizard of Oz -> MVP -> Scaled Solution) prevents over-scoping, which is the #1 velocity killer. Growth teams should build reusable configurable components (paywall, onboarding, notification engine, referral system) so future experiments require zero engineering time.

Tent code (experiments) optimizes for speed with must-haves of correct analytics and clean removal paths. Skyscraper code (production) is for proven winners only. Dedicate 20-30% of engineering time to cleanup and infrastructure.

*-> Full detail (pattern architectures, AI opportunity, velocity tips): `references/growth-engineering-patterns-and-velocity.md`*

---

## Module 4: Scaling Experimentation

*Combined from Mosavat, Verna, and Komissarouk*

The experiment pipeline has seven stages: Ideation (open to everyone, target 5-10 ideas/week), Prioritization (ICE with strategic filter), Design (peer-reviewed canvas), Build/Launch (pre-launch checklist), Monitoring (no peeking), Analysis (SRM check, guardrails, segmentation), and Learning Distribution (write-ups, weekly reviews, searchable repository).

Maintain a balanced portfolio: 50-60% quick optimizations (1-5% lift), 25-35% medium bets (5-20%), 10-20% big bets (20-100%+). When winning experiments only produce 1-2% lifts, you have hit the optimization ceiling and need a big bet. Verna's rule: allocate 20-25% of growth resources to exploring new loops.

*-> Full detail (velocity benchmarks, team structure, Writer's Room model, maturity assessment, culture): `references/scaling-experimentation-org-and-culture.md`*

---

## Decision Tools

### Decision 1: Should We A/B Test or Just Ship?

```
Is the change easily reversible?
+-- Yes --> Is there meaningful risk to user experience or revenue?
|   +-- No --> Just ship it. Monitor post-launch metrics.
|   +-- Yes --> Do you have enough traffic for significance in 2-4 weeks?
|       +-- Yes --> A/B test with guardrail metrics
|       +-- No --> Ship with holdback group (10-20%) and pre/post analysis
+-- No --> Is the expected impact large enough to justify the test cost?
    +-- Yes --> A/B test or staged rollout with clear decision criteria
    +-- No --> Ship with careful monitoring. Document the rationale.
```

### Decision 2: Is This Experiment Strategic or Theater?

```
Can you articulate which strategic question this experiment answers?
+-- No --> Deprioritize. Refine the hypothesis or kill the idea.
+-- Yes --> Does it build on a previous experiment's learning?
    +-- No --> Is it opening a new strategic area?
    |   +-- Yes --> Treat as exploration. Set learning goals, not metric goals.
    |   +-- No --> Likely theater. Deprioritize.
    +-- Yes --> Does it consider system effects (guardrail metrics)?
        +-- No --> Redesign with guardrails before launching.
        +-- Yes --> Good experiment. Prioritize using ICE.
```

### Decision 3: How to Scope a Growth Experiment

```
What is your confidence that this will work?
+-- Low (new hypothesis, no prior data)
|   --> Start with Painted Door test
|   +-- Did >10% of exposed users engage?
|       +-- Yes --> Proceed to Wizard of Oz or MVP
|       +-- No --> Kill the idea, move on
+-- Medium (some signal, analogy from other companies)
|   --> Start with MVP experiment
|   +-- Statistically significant improvement?
|       +-- Yes --> Productionize (Scaled Solution)
|       +-- No --> Iterate once, then kill if still null
+-- High (proven pattern, strong prior data)
    --> Build Scaled Solution directly
    +-- But still A/B test the rollout for validation
```

### Decision 4: Optimization vs. Big Bet

```
Are most recent experiments producing lifts under 3%?
+-- Yes --> You may be hitting the optimization ceiling.
|   +-- Have you mapped all growth loops? If no, map them first.
|   +-- Have you identified a new loop to test? If yes, design a big bet.
|   +-- If no, invest in qualitative research to discover new opportunities.
+-- No --> Continue the optimization program.
    +-- Is your portfolio balanced?
        +-- Less than 10% big bets --> Increase big bet allocation
        +-- More than 10% big bets --> Maintain current mix
```

---

## Experimentation Anti-Patterns

1. **Experiment Theater** -- Running experiments without strategic intent. Fix: Connect every experiment to a strategic question.
2. **The Opinionist's Veto** -- Senior leader overrules results. Fix: Pre-commit to decision criteria.
3. **Over-Segmentation** -- Slicing results until you find a "winning" segment. Fix: Define segments before the experiment.
4. **The Local Maximum Trap** -- Optimizing the same surface until returns approach zero. Fix: Force 10-20% big bets.
5. **Ignoring Negative Results** -- Treating failures as waste. Fix: Document negative results with the same rigor.
6. **The Tiebreaker Test** -- A/B testing button colors to settle design disagreements. Fix: Make the decision.
7. **The Competitor Copy Test** -- Testing a competitor's feature without articulating why it works for your users. Fix: Test the hypothesis, not the feature.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| Strategic Experiment | A test designed to advance understanding of a specific strategic question, connected to product vision |
| Experiment Theater | Running experiments for the appearance of data-driven decisions without genuine strategic intent |
| ICE Framework | Prioritization method scoring experiments on Impact, Confidence, and Ease (each 1-10) |
| Guardrail Metric | A metric that must not degrade as a result of an experiment |
| Minimum Detectable Effect | The smallest effect size an experiment can reliably detect given its sample size and duration |
| Holdback Group | A percentage of users excluded from a change to serve as a control group |
| Experiment Portfolio | Distribution of experiments across risk levels: quick optimizations, medium bets, big bets |
| Optimization Ceiling | The point at which incremental optimization produces diminishing returns |
| Scope Ladder | Komissarouk's progressive scoping model: Painted Door, Wizard of Oz, MVP, Scaled Solution |
| Painted Door Test | A minimal test showing a fake feature to measure demand before building anything |
| Wizard of Oz Test | A test where a manual process is disguised as an automated feature to validate the experience |
| Tent vs. Skyscraper | Code quality tradeoff: tent code is fast experiment code; skyscraper code is production-grade for proven winners |
| Experiment Velocity | The number of completed experiments per unit time, measured by analyzed-and-documented tests |
| Growth Loop | A cyclical system where the output of one user's action feeds the input for the next cycle |
| Writer's Room Model | Collaborative ideation model where all team members contribute experiment ideas regardless of title |
| Four Types of Product Work | Mosavat's framework: Feature Work, Growth Work, Scaling Work, PMF Expansion Work (full framework in product-strategy-leadership) |
| Decision Framework | Pre-committed criteria defining what action the team will take based on each possible experiment outcome |

---

## Reference Files

- `references/experiment-design-and-statistical-rigor.md` -- A/B testing mechanics, sample size calculation, statistical pitfalls deep dive, experiment templates, and the complete decision analysis framework
- `references/growth-engineering-patterns-and-velocity.md` -- Scope Ladder, reusable growth patterns (paywall/onboarding/notification/referral), tent vs. skyscraper code quality, technical debt management, and velocity optimization
- `references/scaling-experimentation-org-and-culture.md` -- Growth team structure, Writer's Room model, hiring growth engineers, experiment pipeline operations, portfolio management, and building experimentation culture
