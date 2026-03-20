---
name: user-psych-foundations
description: Applies Mallory Contois's User Psychology Foundations frameworks to understand why users behave the way they do, design for psychological needs, and unlock new growth loops through resonance. Covers motivation models, cognitive biases in product, habit formation psychology, and emotional design. Activates when designing onboarding flows, analyzing user drop-off, crafting notifications, building habit loops, understanding why users churn, or designing features that resonate emotionally — especially relevant for your product's daily engagement habit product where intrinsic motivation and emotional connection drive retention.
---

**Reference files:**
- `references/motivation-models.md` — Deep dive into motivation frameworks (SDT, Fogg, intrinsic vs. extrinsic) and how to diagnose user motivation gaps
- `references/cognitive-bias-toolkit.md` — Catalog of cognitive biases relevant to product decisions with application templates
- `references/habit-formation-playbook.md` — Step-by-step playbook for designing habit-forming product experiences

---

## How to Use This Skill

When this skill activates:
1. Identify which user psychology framework best applies to the question (motivation, cognitive bias, habit formation, or emotional design)
2. Apply the relevant decision tree from the Decision Tools section
3. Ground all recommendations in the context of your product where intrinsic motivation and emotional connection drive retention
4. Cite the specific framework when making claims
5. If deeper detail is needed, read the relevant reference file before responding

## Gotchas

Common mistakes to avoid when applying these frameworks:

1. **Defaulting to loss aversion for consumer users:** Streaks and loss-framed notifications can trigger guilt in your product's personal context, which is psychologically harmful and increases churn. Contois emphasizes that bias application must respect emotional context -- for your product, positive framing outperforms guilt-centered framing.
2. **Treating the Motivation Stack as a feature checklist:** Identity-level attachment (Layer 4) cannot be manufactured by adding a "milestone badge" feature. It emerges from sustained emotional resonance over time. Jumping to Layer 4 tactics without establishing Layers 2-3 first produces hollow gamification that backfires.
3. **Over-relying on external triggers past the habit formation window:** Contois warns about the "notification trap" -- increasing push notification frequency to compensate for weak habit formation. After Day 21-66, external triggers should decrease. If users still need daily push notifications to open the app at Day 90, the habit loop is broken and more notifications will not fix it.
4. **Assuming the 21-day habit myth:** Habit formation averages 66 days (Lally, UCL), not 21. Designing onboarding campaigns that end at Day 21 leaves users in the most vulnerable part of habit formation without support.

## Example

**User asks:** "Users are completing their first engagement session but not coming back on Day 2. What's going wrong?"

**Approach:**
1. Apply the Fogg Behavior Model (B=MAP) to Day 2 return: check if Motivation is present (did the first session deliver emotional payoff?), Ability is sufficient (is returning frictionless?), and a Prompt exists (is there a well-timed notification for Day 2?)
2. Diagnose using the Motivation Stack: determine whether the first session reached Layer 3 (emotional) or stayed at Layer 2 (functional) -- if users felt informed but not moved, the emotional design of the first engagement session needs work
3. Apply your product context: check whether the app asks users to set a reminder time during onboarding, and whether the Day 2 notification content is a Spark-type prompt (emotionally resonant preview) rather than a generic "come back" nudge
4. Recommend specific interventions targeting the weakest element of B=MAP, with emotional design improvements for the first session's closing moment (Peak-End Rule)

---

## Contois's Core Philosophy

> "To build products that truly resonate, you have to step inside your users' minds — understanding not just what they do, but why they do it, what they fear, and what they aspire to become."

User psychology is the foundation, not a nice-to-have layer. Most product teams optimize for surface-level behaviors without understanding the psychological drivers underneath. The gap between a product that grows and one that stalls is almost always a psychology gap, not a feature gap.

---

## Module 1: Understanding User Motivation

The Motivation Stack operates on four layers: (1) Stated Needs -- what users tell you; (2) Functional Needs -- the job the product does; (3) Emotional Needs -- how the product makes users feel (where retention lives); (4) Identity Needs -- who users become by using the product (deepest and hardest to dislodge). Products that attach to identity create the strongest retention. Also covers SDT (autonomy, competence, relatedness) and the Fogg Behavior Model (B = MAP: Motivation x Ability x Prompt). Includes motivation failure diagnostics.

*-> Full detail: `references/motivation-models.md`*

---

## Module 2: Cognitive Biases in Product Design

Eight high-impact biases for product teams: Loss Aversion (streaks, trial framing), Social Proof (community activity, aggregate stats), Endowment Effect (accumulated investment), Default Effect (pre-selected options), Peak-End Rule (emotional peaks and endings), IKEA Effect (user-created content), Anchoring (pricing, first impressions), and Commitment/Consistency (micro-commitments that escalate). Biases rarely operate in isolation -- powerful product moments combine multiple biases (e.g., "Streak + Social + Loss" combo). Full catalog of 15 biases with ethical guidelines and bias stacking strategies available in reference.

*-> Full detail: `references/cognitive-bias-toolkit.md`*

---

## Module 3: Habit Formation Psychology

Four models of habit formation: Duhigg's Habit Loop (Cue -> Routine -> Reward), Nir Eyal's Hook Model (Trigger -> Action -> Variable Reward -> Investment), Fogg's Tiny Habits, and Clear's Atomic Habits (Four Laws). Key insight: transition users from external triggers (notifications) to internal triggers (emotions). The 21-day myth is wrong -- average habit formation takes 66 days (Lally, UCL, 2009). Habit strength = frequency x perceived utility. Includes measurement framework and common failure modes (notification trap, novelty cliff, streak paradox).

*-> Full detail: `references/habit-formation-playbook.md`*

---

## Module 4: Emotional Design and Resonance

Resonance occurs when a product aligns with a user's internal state, values, and identity aspirations simultaneously. Three conditions: temporal alignment (right message at right moment), value alignment (reflects deeply held values), and identity alignment (helps users become who they aspire to be). Design principles: design for the feeling not the feature, create emotional peaks intentionally, match UI tone to emotional context, build emotional scaffolding (centering -> content -> integration). Includes the Empathy Map template and designing for negative emotions (guilt after missed sessions, doubt, overwhelm).

*-> Full detail: `references/motivation-models.md`*

---

## Decision Tools

### Decision 1: Which Psychological Lever to Pull

```
IF users aren't signing up:
  -> Problem is at the Motivation or Prompt level
  -> Check: Does messaging address emotional/identity needs (Layers 3-4)?
  -> Action: Rewrite value prop to target emotional resonance

IF users sign up but don't activate:
  -> Problem is at the Ability level
  -> Check: How many steps to first value delivery?
  -> Action: Reduce friction — aim for value in <60 seconds

IF users activate but don't retain (Day 1-7):
  -> Problem is at the Reward level
  -> Check: Does first experience deliver emotional payoff?
  -> Action: Design a "peak moment" in first session

IF users retain short-term but churn (Day 7-30):
  -> Problem is at the Habit Formation level
  -> Check: Are you building cue-routine-reward loops?
  -> Action: Implement variable rewards and investment mechanics

IF users retain but don't grow (Day 30+):
  -> Problem is at the Identity level
  -> Check: Is the product becoming part of who they are?
  -> Action: Build identity-reinforcing features (streaks, community, milestones)
```

### Decision 2: Choosing the Right Bias to Leverage

```
IF you need to increase initial conversion:
  -> Use: Social proof + Anchoring
  -> Example: "Join 5M+ active users" + show annual plan first

IF you need to increase activation:
  -> Use: Default effect + Commitment/consistency
  -> Example: Pre-set optimal defaults + ask for a small commitment

IF you need to improve retention:
  -> Use: Loss aversion + Endowment effect + IKEA effect
  -> Example: Streaks + personalized content + user-created content lists

IF you need to drive referral:
  -> Use: Social proof + Relatedness (SDT)
  -> Example: Shared core experiences + community visibility

IF you need to improve monetization:
  -> Use: Anchoring + Endowment + Loss aversion
  -> Example: Free trial that builds investment before paywall
```

### Decision 3: Notification Strategy Based on Habit Stage

```
IF user is in habit formation stage (Day 1-21):
  -> External triggers are essential — notify daily at committed time
  -> Prompt type: Spark (inspire motivation)
  -> Content: Emotionally resonant preview of today's engagement session
  -> Frequency: Daily, at user's preferred time

IF user is in habit reinforcement stage (Day 21-66):
  -> Begin reducing external trigger reliance
  -> Prompt type: Signal (simple reminder, they have motivation)
  -> Content: Brief nudge, not a full pitch
  -> Frequency: Daily but lighter touch; test skipping some days

IF user has established habit (Day 66+):
  -> Internal triggers should be primary; external as supplement
  -> Prompt type: Facilitator (make it easier, not more motivating)
  -> Content: Personalized, contextual, high-value only
  -> Frequency: Reduce to avoid notification fatigue

IF user has lapsed (missed 3+ days):
  -> Re-engagement requires re-sparking motivation
  -> Prompt type: Spark (re-inspire)
  -> Content: High-emotional-impact content; welcome-back warmth
  -> Frequency: 1 attempt, then 3-day pause, then 1 more; avoid spam
```

### Decision 4: Feature Prioritization Through Psychology Lens

```
IF the feature addresses only stated needs (Layer 1):
  -> Low priority — users may not actually use it
  -> Validate with behavioral data, not just survey data

IF the feature addresses functional needs (Layer 2):
  -> Medium priority — useful but not differentiating
  -> Build if competitive table stakes require it

IF the feature addresses emotional needs (Layer 3):
  -> High priority — this drives retention
  -> Invest in emotional design quality, not just functionality

IF the feature addresses identity needs (Layer 4):
  -> Highest priority — this drives lifetime value
  -> Build with long-term compounding in mind (streaks, journeys, community)
```

---

## Applied to your product

your product sits at a uniquely powerful intersection for user psychology: it serves a deeply personal, emotionally significant, identity-defining daily practice.

**Motivation Stack:** Core value proposition should be articulated at Layer 4 (Identity) -- not "daily engagement content" but "become the person you aspire to be." The most retained users almost certainly self-identify as "someone who uses the app every day."

**Habit Formation:** your product has a natural advantage -- engagement has existing cultural and religious scaffolding. During onboarding, ask when users already engage (don't impose a time), then align notifications with their existing routine. You're enhancing an existing habit, not creating one.

**Cognitive Bias Leverage:** Three highest-leverage biases: (1) Commitment/consistency via onboarding micro-commitments; (2) Loss aversion via streaks framed through grace, not guilt; (3) Endowment effect through accumulated personal journals, saved engagement sessions, and reflection history.

**Emotional Design:** Invest disproportionately in emotional design quality. The personal context means users arrive in vulnerable, seeking emotional states. The highest-leverage investment is in the transitions: the moment between opening the app and beginning the engagement session (centering), and the moment after completing it (integration/reflection).

**Critical Risk:** The biggest psychological risk is how your product handles missed days. Users may carry guilt about personal inconsistency. A grace-centered approach -- welcoming users back warmly, normalizing imperfection -- aligns with product values and is psychologically optimal.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| Motivation Stack | Four-layer model of user motivation: stated, functional, emotional, identity needs |
| Self-Determination Theory (SDT) | Framework identifying autonomy, competence, and relatedness as innate psychological needs |
| Fogg Behavior Model (B=MAP) | Behavior occurs when motivation, ability, and prompt converge simultaneously |
| Loss Aversion | Psychological tendency to feel losses ~2x more strongly than equivalent gains |
| Endowment Effect | Tendency to overvalue things we already possess or have invested in |
| Peak-End Rule | Experiences are judged primarily by their most intense point and ending |
| Hook Model | Nir Eyal's four-phase habit loop: Trigger, Action, Variable Reward, Investment |
| Resonance | State where product experience aligns with user's internal state, values, and identity |
| Variable Reward | Unpredictable rewards that create craving and sustained engagement |
| Internal Trigger | Emotional or physiological cue that prompts product usage without external prompt |
| Habit Strength | Composite of frequency and perceived utility; proxy for sustainable retention |
| Identity Attachment | When product usage becomes part of user's self-concept ("I am someone who...") |
| Emotional Scaffolding | Design patterns that help users transition into the right emotional state for engagement |
| Cognitive Bias Stacking | Combining multiple biases in a single product moment for amplified effect |

---

## Reference Files

- `references/motivation-models.md` — Deep dive into SDT, Fogg Behavior Model, and the Motivation Stack with diagnostic tools, application templates, and emotional design principles
- `references/cognitive-bias-toolkit.md` — Comprehensive catalog of 15+ cognitive biases relevant to product design with worked examples, ethical guidelines, and bias stacking strategies
- `references/habit-formation-playbook.md` — Step-by-step playbook for designing habit-forming experiences, including Hook Model implementation, habit measurement frameworks, and your product implementation plan
