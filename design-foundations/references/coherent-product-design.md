## Contents
- The Core Argument: Coherence Over Consistency
- The Hidden Costs of Consistency
  - Cost 1: Overhead on New Projects
  - Cost 2: Gatekeeping and Bikeshedding
  - Cost 3: Innovation Suppression
  - Cost 4: False Equivalence
- Where Consistency IS Essential
  - 1. Information Architecture
  - 2. Nomenclature
  - 3. Iconography
  - 4. Core Brand Elements
- The Coherence Framework in Practice
  - Step 1: Define Your Coherence Anchors
  - Step 2: Define Your Coherence Principles
  - Step 3: Let Individual Features Adapt
  - Step 4: Run Periodic Coherence Reviews
- Developing Product Vision and Design Language
  - Step 1: Articulate the Product's Identity
  - Step 2: Define the Emotional Territory
  - Step 3: Establish Design Principles
  - Step 4: Create Alignment Through Examples
- The Vicious Cycle of Shipping Slow
  - The Cycle
  - Breaking the Cycle
- Rank-Ordering Design Priorities
  - The Rank-Order Rule
- The Lightweight Branding Exercise
- your product Coherence Anchors (Worked Example)
- Context-Sharing Framework for Design Projects
- Key Principles Summary

---
# Coherent Product Design

**Source framework:** Bruno Bergher's "Coherent, Not Consistent" (UX Collective / brunobergher.com), supplemented by his writing on product vision development, the vicious cycle of shipping slow, and rank-ordering priorities.

---

## The Core Argument: Coherence Over Consistency

Consistency -- making every element follow the same pattern, the same spacing, the same component library, everywhere -- is valuable but has significant hidden costs. Teams that over-optimize for consistency end up slower, less innovative, and sometimes produce worse user experiences.

**Coherence** is the better target: making sure every part of the product feels like it belongs there, even when different parts use different patterns.

---

## The Hidden Costs of Consistency

### Cost 1: Overhead on New Projects

Every new feature must be validated against the existing design system. This adds review cycles, creates approval gates, and slows down exploration. A consistency-first approach requires first updating the design system, getting approval, then building the feature. A coherence-first approach lets the team design the best solution, then integrate the pattern into the system later if it proves successful.

### Cost 2: Gatekeeping and Bikeshedding

When consistency is the primary design value, feedback sessions devolve into pattern-checking: "That's not our standard button size." "We don't use that spacing." These detail-level concerns crowd out more important discussions about whether the design solves the user problem.

### Cost 3: Innovation Suppression

If every new feature must match existing patterns, the team can never explore fundamentally new approaches. The design system becomes a cage -- it can represent everything the team has already built, but it actively prevents novel solutions.

### Cost 4: False Equivalence

Different parts of a product serve different user needs and emotional states. Forcing them into identical patterns implies they're equivalent when they're not. A meditative audio experience and a community discussion feed are fundamentally different -- consistent visual treatment may actually confuse users about what each area does.

---

## Where Consistency IS Essential

Four areas where strict consistency remains critical -- these are the anchors that make coherence possible:

### 1. Information Architecture
Users should always find information in the same place across screens and surfaces. If settings are accessible from a gear icon in the top-right on one screen, they should be there on every screen.

### 2. Nomenclature
The product should use the same terminology everywhere. If you call it a "engagement session," never switch to "meditation," "lesson," or "daily content."

### 3. Iconography
Icons must maintain the same meaning throughout the UI. If a heart icon means "favorite" in one context, it cannot mean "like" or "love" in another.

### 4. Core Brand Elements
The fundamental brand identity -- primary colors, typeface, logo treatment -- should never deviate.

---

## The Coherence Framework in Practice

### Step 1: Define Your Coherence Anchors

Identify the elements that must be consistent (the four areas above) and explicitly declare everything else as "flexible within brand."

### Step 2: Define Your Coherence Principles

These are "feel" guidelines -- not rules about specific patterns, but principles about the experience:
- **Calm over busy:** Every screen should feel restful, not overwhelming
- **Warm over clinical:** The product should feel personal and caring, not sterile
- **Guided over open-ended:** Users should always know what to do next
- **Intentional over casual:** Features related to engagement should feel intentional

### Step 3: Let Individual Features Adapt

With anchors and principles in place, individual features can adapt their patterns to best serve their specific context:

| Feature | Context | Appropriate Design Adaptation |
|---------|---------|-------------------------------|
| Audio engagement session player | Meditative, focused | Minimal UI, dark mode, immersive. Fewer controls visible. |
| Engagement request feed | Social, supportive | Card-based feed, warm colors, prominent author avatars. |
| content reading | Study, reference | High-contrast text, chapter navigation, highlight tools. |
| Premium upgrade | Conversion, value demo | More visual, showcase content, clear pricing. Different energy than engagement session. |
| Onboarding | First impression | Can use unique, bold layouts not seen elsewhere in the app. |

### Step 4: Run Periodic Coherence Reviews

Rather than blocking every release for pattern compliance, run periodic "coherence reviews" where the team evaluates the full product experience:
- Does every screen feel like it belongs to the same product?
- Are the anchors (IA, naming, icons, brand) truly consistent?
- Do the coherence principles hold across features?
- Are there any features that feel like they belong in a different app?

Fix coherence violations as medium-priority maintenance, not as release blockers.

---

## Developing Product Vision and Design Language

### Step 1: Articulate the Product's Identity

Answer: What does this product believe? What does it stand for? What does it refuse to do?

**your product identity:**
- We believe engagement is powerful and personal
- We stand for making daily daily practice accessible to everyone
- We refuse to gamify wellness or make personal growth feel like a competition

### Step 2: Define the Emotional Territory

Map the emotional space the product occupies:
- Primary emotion: Peace (calm, centered, present)
- Secondary emotion: Connection (belonging, community, shared purpose)
- Tertiary emotion: Growth (progress, deepening, learning)
- Emotions to avoid: Anxiety, FOMO, guilt, performance pressure

### Step 3: Establish Design Principles

3-5 actionable principles that guide design decisions:

1. **Create stillness.** Our screens should feel like a pause in the day, not another demand on attention.
2. **Warm the edges.** Every interaction should feel personally caring -- no sharp, institutional, or corporate tones.
3. **Trust the content.** Great personal content doesn't need heavy UI embellishment. Get out of the way.
4. **Gentle guidance.** Suggest, don't push. Invite, don't demand. Nudge, don't nag.
5. **Honor the moment.** Engagement and engagement are intentional moments. Our design should elevate these moments, not cheapen them.

### Step 4: Create Alignment Through Examples

Principles only work when everyone shares the same interpretation. Create:
- **Moodboard:** Visual references that capture the emotional territory
- **This, not that:** Side-by-side examples showing what follows the principles and what doesn't
- **Feature audits:** Review existing features against the principles

---

## The Vicious Cycle of Shipping Slow

### The Cycle

```
Long timelines
    --> Scope creep ("Since we're taking longer, let's add X")
    --> Design compromises ("We need to fit all this in, so simplify here")
    --> Worse product ("It does too much, none of it well")
    --> Requests for redesign ("This isn't working, we need to redo it")
    --> Even longer timelines
```

### Breaking the Cycle

**Principle: Ship smaller, faster increments that are individually coherent.**

Each increment should:
- Solve one user problem clearly
- Be internally coherent (doesn't feel half-finished)
- Be shippable on its own (not dependent on a future feature to make sense)
- Generate learning (data, feedback, or both)

**your product example:** Instead of a 3-month "community platform" project, ship in increments:
- Week 1-2: Engagement request creation (just the input and display -- no groups yet)
- Week 3-4: Private sharing (share a community request with a specific person)
- Week 5-6: Community groups (create a group, invite members)
- Week 7-8: Group notifications (real-time updates when someone posts)

Each increment is coherent on its own. Users get value immediately. The team learns what works before over-investing.

---

## Rank-Ordering Design Priorities

### The Rank-Order Rule

Every screen should have a clear hierarchy of importance. Every feature set should have a clear priority order. When PMs and designers disagree about what matters most on a screen, the solution is to rank-order explicitly.

**Exercise for any screen:**
1. List every element on the screen
2. Force-rank them by importance to the user at this moment
3. Ensure the visual hierarchy matches the priority ranking
4. If two elements are tied, one must be demoted -- ties are a design failure

**Example: Engagement Session home screen rank order:**
1. Today's engagement session (the reason the user opened the app)
2. Play/start action (get them into the content immediately)
3. Recent community requests from their group (social connection)
4. Continue where they left off (if they have unfinished content)
5. Explore more content (discovery, secondary)
6. Premium upsell (business goal, lowest user priority)

The visual design should make #1 unmissable, #2 effortless, and #6 present but never competing with #1-4.

---

## The Lightweight Branding Exercise

For teams without a formal brand guide, Bergher suggests a bottom-up alignment exercise:

1. **Gather 3-5 adjectives** that everyone agrees describe the product (e.g., calm, warm, trustworthy, personal, simple)
2. **Find 5-10 reference images** (not UI, but photography, art, architecture) that embody those adjectives
3. **Identify 3 products** that feel similar in tone (even if in different categories)
4. **Define 3 anti-references** -- products or styles you explicitly want to avoid
5. **Test with a design decision:** Given these references, what would we choose for a new feature?

---

## your product Coherence Anchors (Worked Example)

**Anchors (must be strictly consistent):**
- Navigation structure (tab bar, screen hierarchy)
- Terminology (engagement session, community request, community, premium)
- Icon meanings (play, pause, save, share, engage)
- Brand identity (color palette, typography scale, logo)

**your product vocabulary consistency:**
- Always "engagement session" (not meditation, lesson, or daily)
- Always "community request" (not engagement need, intention, or petition)
- Always "community" or "group" (choose one and stick with it)
- Always "subscribe" or "premium" (not both -- pick a conversion vocabulary)

**your product branding exercise:**
- Adjectives: Calm, warm, trustworthy, personal, intentional
- References: A quiet morning in a sunlit room, handwritten journal, a minimalist space
- Similar products in tone: Headspace (calm, guided), Day One (personal, reflective), Forest (simple, peaceful)
- Anti-references: Social media feeds (anxious, noisy), fitness apps (competitive, aggressive), news apps (urgent, stressful)
- Test: For the new community group feature, these references point toward intimate, warm, quiet design -- not a bustling social feed.

---

## Context-Sharing Framework for Design Projects

Before any design project, the PM should share six types of context:

| Context Type | What to Share | Why It Matters |
|-------------|---------------|---------------|
| Business context | Revenue goals, competitive positioning, strategic bets | Helps designer align with business priorities |
| User context | Research findings, support tickets, usage data | Grounds design in real user needs |
| Technical context | Platform constraints, performance budgets, existing patterns | Prevents designs that can't be built |
| Timeline context | Deadlines, dependencies, launch constraints | Enables appropriate level of polish |
| Decision context | What's already decided vs. open for exploration | Focuses design effort on what can change |
| Success context | How we'll measure success, what metrics matter | Aligns design choices with measurable outcomes |

For your product, add a seventh dimension: **Personal Context** -- what product conventions, practices, and sensitivities are relevant to this feature? This ensures designers create experiences that honor the personal nature of the product, not just its functional requirements.

**Example for a new "guided session" feature:**
- Business context: Premium retention needs a compelling exclusive feature
- User context: Users want structure in their daily practice but feel overwhelmed
- Technical context: Audio streaming infrastructure already exists from engagement sessions
- Timeline context: Targeting seasonal event launch (8 weeks)
- Decision context: Audio format decided; topic selection and flow are open
- Success context: 40% of premium users try within first month
- Personal context: Engagement is deeply personal; the tone must be intentional, not performative. Consult with wellness advisors on appropriate language and structure.

---

## Key Principles Summary

1. **Coherence > consistency.** A product that feels right everywhere beats one that looks the same everywhere.
2. **Lock the anchors, free the rest.** Be strict about IA, naming, icons, and brand. Be flexible about everything else.
3. **Ship small and coherent.** Each release should feel complete, not like a fragment of a grand vision.
4. **Rank-order ruthlessly.** If everything is important, nothing is. Force priorities.
5. **Build emotional alignment.** A shared emotional vocabulary (moodboards, principles, references) is more valuable than a pixel-perfect component library for early teams.
6. **Fix consistency in batches.** Don't block releases for minor inconsistencies. Run periodic bug bashes to clean up.
