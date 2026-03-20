## Contents
- Self-Determination Theory (SDT) — Full Framework
  - Origins and Core Premise
  - The Three Needs in Product Context
- The Fogg Behavior Model — Implementation Guide
  - Core Formula: B = MAP
  - The Motivation-Ability Tradeoff
  - The Simplicity Chain (Ability Factors)
  - Prompt Design Framework
- The Motivation Stack — Diagnostic Tool
  - Layer-by-Layer Assessment Template
  - Migration Strategy (Moving Users Up the Stack)
  - your product Motivation Stack Analysis
- Intrinsic vs. Extrinsic Motivation — When to Use Each
  - Extrinsic Motivation (External Rewards)
  - Intrinsic Motivation (Internal Satisfaction)
  - The Motivation Transition Curve
- Emotional Design and Resonance
  - The Resonance Framework
  - Emotional Design Principles
  - The Empathy Map for Product Decisions
  - Designing for Negative Emotions

---
# Motivation Models — Deep Reference
*Source: Mallory Contois, User Psych Foundations; synthesized with Deci & Ryan (SDT), BJ Fogg (Behavior Model), and Dan Pink (Drive)*

---

## Self-Determination Theory (SDT) — Full Framework

### Origins and Core Premise
Developed by Edward Deci and Richard Ryan (1985, refined through 2000s), SDT posits that humans have three innate psychological needs. When these needs are met, people experience intrinsic motivation — the most durable form of engagement. When thwarted, motivation degrades to extrinsic forms or disappears entirely.

### The Three Needs in Product Context

#### Autonomy
**Definition:** The need to feel volitional — that one's actions are self-endorsed rather than controlled.

**In product design:**
- Choice architecture that feels empowering, not overwhelming
- Customization options that create ownership
- Opt-in rather than opt-out for non-essential features
- Language that invites rather than directs ("Choose your path" vs. "Complete step 3")

**Autonomy-supportive patterns:**
- User-set goals and schedules
- Multiple pathways through onboarding
- Ability to skip or defer without penalty
- Settings that respect user preferences over engagement metrics

**Autonomy-thwarting patterns (anti-patterns):**
- Forced tutorials that can't be skipped
- Dark patterns that manipulate choices
- Notifications that guilt-trip non-usage
- Removing features as punishment for non-payment

**your product diagnostic questions:**
- Can users choose their engagement session focus area?
- Can users set their own notification schedule?
- Is there a way to personalize the daily experience?
- Do users feel like they're choosing to engage, or being pushed?

#### Competence
**Definition:** The need to feel effective — that one can achieve desired outcomes and grow in capability.

**In product design:**
- Clear feedback on progress and achievement
- Appropriate challenge level (not too easy, not too hard)
- Skill progression visible to the user
- Celebration of milestones without patronizing

**Competence-supportive patterns:**
- Progress bars and journey maps
- Gradually increasing depth of content
- Achievement acknowledgment (streaks, badges, milestones)
- Performance feedback that feels informative, not evaluative

**Competence-thwarting patterns (anti-patterns):**
- Overwhelming complexity at the start
- No visible progress indicators
- Features that make users feel incompetent
- Comparisons that highlight inadequacy

**your product diagnostic questions:**
- Do users feel they're growing in their daily practice?
- Is there visible progress in their engagement/engagement session journey?
- Does content difficulty match user readiness?
- Do milestone celebrations feel meaningful?

#### Relatedness
**Definition:** The need to feel connected to others — to care and be cared for.

**In product design:**
- Community features that create genuine connection
- Shared experiences that build belonging
- Social features that feel warm, not performative
- Acknowledgment of the user as a person, not a data point

**Relatedness-supportive patterns:**
- Group activities and shared goals
- Community spaces for authentic interaction
- Social proof that creates belonging ("Join your community")
- Personalized communication that acknowledges the individual

**Relatedness-thwarting patterns (anti-patterns):**
- Isolating solo experiences when community would help
- Competitive leaderboards that create comparison anxiety
- Impersonal, automated communication
- Social features that feel forced or surveilled

**your product diagnostic questions:**
- Do users feel part of a community through the app?
- Are community groups creating genuine connection or empty social mechanics?
- Does community activity feel authentic or performative?
- Is there a sense of "we're in this together"?

---

## The Fogg Behavior Model — Implementation Guide

### Core Formula: B = MAP
Behavior happens when three elements converge at the same moment:
- **M**otivation — Sufficient desire to act
- **A**bility — The behavior is easy enough given current motivation
- **P**rompt — A cue that triggers the behavior at the right moment

### The Motivation-Ability Tradeoff

This is the most practically useful insight from Fogg's model:

```
High Motivation + Low Ability = Behavior possible (but frustrating)
Low Motivation + High Ability = Behavior possible (if prompted)
Low Motivation + Low Ability = No behavior (no amount of prompting helps)
High Motivation + High Ability = Behavior likely (any prompt works)
```

**Practical implication:** You can compensate for low motivation by increasing ability (making it easier), OR compensate for low ability by increasing motivation (making it more desirable). You cannot compensate for low everything.

### The Simplicity Chain (Ability Factors)

Ability is determined by the scarcest resource in the chain. Improving one factor while another remains constrained won't change behavior:

| Factor | Question | your product Example |
|--------|----------|------------------|
| Time | How long does it take? | 5-min engagement session vs. 30-min deep-dive session |
| Money | What's the financial cost? | Free tier vs. subscription barrier |
| Physical effort | How much exertion? | One-tap access vs. multi-step navigation |
| Brain cycles | How much thinking? | Pre-selected content vs. browse-and-choose |
| Social deviance | Does it break norms? | Private engagement vs. public sharing |
| Non-routine | How different from existing habits? | Integrating with morning routine vs. new time slot |

**Audit process:**
1. Map the complete behavior chain for your target action
2. Score each factor on a 1-5 simplicity scale
3. Identify the weakest link (lowest score)
4. Improve that specific factor first
5. Re-score and repeat

### Prompt Design Framework

**Three prompt types matched to user states:**

| User State | Motivation | Ability | Prompt Type | Design Approach |
|-----------|------------|---------|-------------|-----------------|
| Willing but stuck | Low | High | Spark | Inspire emotional motivation |
| Eager but blocked | High | Low | Facilitator | Remove friction, provide tools |
| Ready and able | High | High | Signal | Simple reminder, minimal content |

**Prompt timing principles:**
- Deliver prompts when motivation is naturally higher (morning for daily habits)
- Match prompt complexity to user's available attention
- Respect "prompt fatigue" — diminishing returns from repeated prompts
- Transition users from external prompts (notifications) to internal prompts (habit cues)

---

## The Motivation Stack — Diagnostic Tool

### Layer-by-Layer Assessment Template

Use this template to diagnose where your product's motivation strategy is weakest:

#### Layer 1: Stated Needs Assessment
- What do users say they want in surveys?
- What feature requests dominate support tickets?
- What language do users use to describe the product?
- **Warning:** Stated needs often mask deeper needs. Treat as input, not truth.

#### Layer 2: Functional Needs Assessment
- What job is the user hiring the product to do?
- What would the user do if this product didn't exist?
- What's the functional outcome they're seeking?
- **Diagnostic:** If users have many substitutes, you're stuck at Layer 2.

#### Layer 3: Emotional Needs Assessment
- How do users feel before, during, and after using the product?
- What emotional state triggers usage?
- What emotional state does usage create?
- **Diagnostic:** If users describe the product in emotional terms, you've reached Layer 3.

#### Layer 4: Identity Needs Assessment
- Do users self-identify through the product? ("I'm a [product] user")
- Does using the product reinforce who they aspire to be?
- Would abandoning the product feel like losing part of themselves?
- **Diagnostic:** If users proactively tell others about usage, you've reached Layer 4.

### Migration Strategy (Moving Users Up the Stack)

**Layer 1 → Layer 2:** Deliver on functional promise consistently
**Layer 2 → Layer 3:** Design emotional peaks; acknowledge feelings
**Layer 3 → Layer 4:** Create identity-reinforcing rituals and milestones

### your product Motivation Stack Analysis

| Layer | User Need | Current State | Opportunity |
|-------|-----------|---------------|-------------|
| Stated | "I want daily content" | Addressed via content library | Baseline met |
| Functional | Structure for daily daily practice | Engagement Session delivery works | Optimize for time-of-day alignment |
| Emotional | Peace, connection, personal comfort | Partially addressed | Invest in emotional design of content experience |
| Identity | "I am someone who engages daily" | Streak feature touches this | Deepen with journey mapping, milestone celebrations, community identity |

---

## Intrinsic vs. Extrinsic Motivation — When to Use Each

### Extrinsic Motivation (External Rewards)

**When appropriate:**
- Bootstrapping a new behavior (before intrinsic motivation develops)
- One-time actions that don't need to become habitual
- Referral mechanics (inherently transactional)

**Risks:**
- Overjustification effect: External rewards can undermine intrinsic motivation
- Once removed, behavior may decrease below baseline
- Creates transactional relationship with product

**your product examples of appropriate extrinsic motivation:**
- Referral bonuses (one-time behavior, inherently transactional)
- First-week gamification to establish routine (bootstrapping phase only)

### Intrinsic Motivation (Internal Satisfaction)

**When to cultivate:**
- Core engagement behaviors you want to sustain long-term
- Behaviors that define the product's unique value
- Community participation and content creation

**How to cultivate:**
- Meet SDT needs (autonomy, competence, relatedness)
- Design for flow states (clear goals, immediate feedback, matched challenge)
- Connect actions to user's values and identity
- Make progress visible and meaningful

**your product examples of intrinsic motivation cultivation:**
- Engagement Session content that delivers genuine meaningful insight (intrinsically rewarding)
- Engagement journaling that creates personal meaning over time
- Community activity that fulfills relatedness needs
- Personal growth journey that builds competence and identity

### The Motivation Transition Curve

```
Week 1-2:    Extrinsic dominant (notifications, streaks, novelty)
Week 2-4:    Mixed (extrinsic scaffolding + emerging intrinsic value)
Week 4-8:    Intrinsic emerging (habit forming, emotional attachment)
Week 8+:     Intrinsic dominant (identity, community, personal meaning)
```

**Critical insight:** If you haven't transitioned users to intrinsic motivation by week 8, extrinsic mechanics will eventually fail. The product must deliver genuine value — no amount of gamification sustains engagement without it.

---

## Emotional Design and Resonance

### The Resonance Framework

Resonance occurs when a product experience aligns with a user's internal state, values, and identity aspirations simultaneously. Resonant products don't feel like tools — they feel like extensions of self.

**Three conditions for resonance:**

1. **Temporal alignment** — Right message at the right moment in the user's emotional journey
   - Morning engagement session when user is in reflective state
   - Evening gratitude prompt when processing the day
   - Crisis-moment content when user is seeking comfort

2. **Value alignment** — Product reflects and reinforces the user's deeply held values
   - Content that matches personal preferences
   - Tone that respects the gravity of daily practice
   - Community norms that reflect product values

3. **Identity alignment** — Product helps users become who they aspire to be
   - "I am someone who starts every day with the app"
   - "I am growing in my practice"
   - "I am part of a engaged community"

### Emotional Design Principles

**1. Design for the feeling, not the feature**
- Don't ask "What feature should we build?" Ask "What should the user feel?"
- your product: The goal isn't "daily content delivery" — it's "daily peace and connection"
- Map every feature to an intended emotional outcome

**2. Create emotional peaks intentionally**
- Identify 2-3 moments in the user journey where emotional impact should be highest
- Invest disproportionate design effort in these moments
- your product peaks: First engagement session completion, first milestone achieved, first community connection

**3. Match UI tone to emotional context**
- Visual design, copy, and interaction patterns should reinforce the intended emotion
- Calm, warm, spacious design for contemplative moments
- Celebratory design for milestones and achievements
- Gentle, supportive design for moments of struggle

**4. Build emotional scaffolding**
- Users don't arrive in the right emotional state — help them transition
- Pre-content: Breathing exercise, centering prompt, or gratitude reflection
- During content: Pacing, pauses, reflective questions
- Post-content: Integration prompt, journaling space, community sharing option

### The Empathy Map for Product Decisions

For every major product decision, map the user's full psychological state:

| Dimension | Question | Example (your product morning user) |
|-----------|----------|-------------------------------|
| Think | What occupies their mind? | Today's responsibilities, worries, gratitude |
| Feel | What emotions are present? | Seeking peace, possibly anxious, hopeful |
| Say | What do they express to others? | "I try to start my day in engagement" |
| Do | What actions are they taking? | Morning routine, checking phone, making coffee |
| Pain | What frustrations exist? | Inconsistency, feeling disconnected, guilt |
| Gain | What are they hoping for? | Personal growth, peace, consistency |

### Designing for Negative Emotions

Products often design only for positive states. But users arrive in negative emotional states too, and how you handle these moments defines loyalty:

**Guilt after missed sessions:**
- Don't punish or shame ("You broke your streak!")
- Welcome back warmly ("Welcome back. Every day is a new beginning.")
- Reframe: Emphasize grace, not performance

**Doubt or personal struggle:**
- Provide content for difficult seasons
- Normalize struggle as part of the journey
- Community features that allow vulnerability

**Overwhelm from content volume:**
- Simple, focused daily experience (don't make them choose from 1000 options)
- "Today's engagement session" as the clear default path
- Progressive disclosure of content depth
