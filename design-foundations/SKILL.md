---
name: design-foundations
description: >
  Applies Bruno Bergher's Design Foundations frameworks to collaborate with designers effectively
  and ship coherent products users love. Covers the Feedback Ladder, design critique facilitation,
  PM-designer disagreement resolution, and the "coherent, not consistent" design philosophy.
  Activates when working with designers on your product features, evaluating design work, giving feedback
  on UI/UX, running design critiques, resolving PM-designer tension, or making product decisions
  that involve visual/interaction design tradeoffs. Triggers when someone says "the designer and I
  disagree," "how should I give feedback on this design," "our product feels inconsistent," or
  when any PM-design collaboration question arises.
---

**Reference files:**
- `references/design-critique-framework.md` -- How to run design critiques, the prescriptive-to-descriptive spectrum, PM Crits, and building a critique culture
- `references/coherent-product-design.md` -- Bergher's "coherent, not consistent" philosophy, product vision development, the vicious cycle of shipping slow, and rank-ordering design priorities

---

## How to Use This Skill

When this skill activates:
1. Identify which design and UX framework from this skill best applies to the question
2. Apply the relevant decision tree from the Decision Tools section
3. Ground all recommendations in the context of your product
4. Cite the specific framework when making claims
5. If deeper detail is needed, read the relevant reference file before responding

## Gotchas

Common mistakes to avoid when applying these frameworks:

1. **Don't give pixel-level feedback on early explorations.** Bergher's Feedback Ladder requires matching feedback granularity to design stage. Commenting on spacing or color on an early wireframe skips the direction-level question ("Does this approach solve the user problem?") and wastes both PM and designer time on details that will change.
2. **Don't default to prescriptive feedback.** "Move the button to the left" tells the designer *what* to do but closes the conversation. Bergher insists on descriptive feedback ("Users aren't finding the CTA -- it feels buried") because the designer likely has a better solution than your specific suggestion. Prescriptive feedback is only appropriate for domain constraints or brand requirements.
3. **Don't pursue consistency at the expense of coherence.** Bergher's central framework says forcing every your product surface into identical patterns can hurt users. The audio engagement session player, the community feed, and the content library each have different emotional needs -- they should feel coherent (all clearly your product) but not identical.
4. **Don't involve designers after the PRD is written.** Bergher identifies "Late Involvement" as a key anti-pattern. At your company, involving the designer from Day 0 of problem definition (not after decisions are made) can reduce design cycles by avoiding misdirected exploration.

## Example

**User asks:** "The designer and I disagree about the onboarding flow. She wants a longer, more guided flow and I want to get users to content faster. How do we resolve this?"

**Approach:**
1. Apply Bergher's disagreement resolution framework -- classify this as a "user impact disagreement" (will users benefit from guidance or speed?), which means it should be resolved with data or research, not by pulling rank
2. Check whether evidence exists -- if usability testing or funnel data shows where users drop off in the current flow, let that data decide; if no data exists, recommend running a quick usability test with 5-8 users
3. Ground in your product context -- for a engagement session app, the first-time emotional experience matters enormously (Bergher's "coherence" principle), so frame the question as "What does the user need to feel in their first 60 seconds?" rather than "How many screens?"
4. If no test is feasible, apply the disagreement type hierarchy -- since this is about user experience (not aesthetics or business metrics), lean toward the designer's expertise while ensuring the PM's concern about time-to-content is captured as a measurable success criterion

---

## Core Philosophy

> "Making sure every part of your product feels like it belongs there, instead of trying to make them exactly the same."

Bruno Bergher believes that great products emerge from deep collaboration between product managers and designers -- not from PMs handing specs to designers or designers working in isolation. The PM's job is not to design, but to create the conditions where great design happens: share full context, invest in understanding the design process, give feedback that opens possibilities rather than narrowing them, and treat designers as strategic partners rather than a service center.

---

## Module 1: Understanding the Design Process

### PM Anti-Patterns in Design

**Anti-pattern 1: The Drive-By Solution**
- PM says: "Can you make it look like [specific mockup/competitor screenshot]?"
- Problem: Skips the problem-framing step; designer becomes a production tool
- Better: "Users are struggling to find X. How might we make it more discoverable?"

**Anti-pattern 2: The Late Involvement**
- PM says: "We already decided the feature. Can you design the screens?"
- Problem: Designer has no context, no input on approach, no ownership
- Better: Involve the designer from the problem-definition stage

**Anti-pattern 3: The Death by Committee**
- PM facilitates feedback from 8 stakeholders, each with conflicting opinions
- Problem: Designer tries to please everyone, pleases no one
- Better: PM synthesizes stakeholder input into a clear brief; designer presents to a small decision-making group

**Anti-pattern 4: The Premature Pixel Critique**
- PM gives detailed visual feedback on an early wireframe
- Problem: Direction-level decisions haven't been made; pixel feedback is premature
- Better: Match feedback granularity to the stage of work (concept vs. wireframe vs. final)

### The Time Investment in Design

PMs consistently underestimate how long design takes. A rough guide:

| Scope | Design Investment | What's Included |
|-------|------------------|----------------|
| Small feature (1 screen) | 3-5 days | Exploration, wireframe, high-fi, edge cases |
| Medium feature (3-5 screens) | 2-4 weeks | Research, multiple explorations, wireframes, high-fi, specs |
| Large feature (new flow) | 4-8 weeks | User research, competitive analysis, multiple directions, wireframes, prototyping, testing, final design |
| New product / redesign | 8-16 weeks | All of the above, plus design system work, cross-platform |

**Rule of thumb:** If you think design should take a week, it probably needs two. If you've allotted no time for design exploration, the result will be predictable and uninspired.

---

## Module 2: Giving Effective Design Feedback

### The Feedback Problem

Bergher identifies a core challenge: most design feedback is either too prescriptive ("Move the button to the left") or too vague ("I don't like it"). Neither helps the designer improve the work.

> "Getting useless feedback? It's your fault."

Bergher argues that the quality of feedback you receive is largely determined by how you ask for it. The four elements of an effective feedback ask:

1. **Context**: What stage is this work at? What decisions have already been made?
2. **Specific question**: What do you want feedback on? ("Does this flow make sense for a first-time user?" not "What do you think?")
3. **Constraints**: What can and can't change? ("The copy is final, but layout is open")
4. **Type of feedback desired**: Direction-level, detail-level, or emotional reaction?

### The Feedback Ladder

Match your feedback type to the stage of design work:

**Level 1: Direction Feedback (Concept/Exploration stage)**
- Is this the right approach to the problem?
- Does this concept address the user need we identified?
- Are we solving for the right persona?
- Example: "I think this approach assumes users already understand what a community group is. New users might not. Is there a way to introduce the concept?"

**Level 2: Flow Feedback (Wireframe stage)**
- Does the user journey make sense?
- Are there steps that could be removed or combined?
- Is the information hierarchy correct?
- Example: "In this flow, the user has to create a profile before they can see any content. Could we let them browse first?"

**Level 3: Detail Feedback (High-fidelity stage)**
- Is the copy clear and on-brand?
- Are interaction patterns consistent with the rest of the product?
- Are edge cases handled?
- Example: "What happens when a user has no community requests yet? This empty state needs to guide them toward creating one."

**Level 4: Polish Feedback (Pre-ship)**
- Are animations smooth?
- Is spacing and alignment pixel-perfect?
- Does it feel right when you use it?
- Example: "The transition between engagement session cards feels jumpy. Can we smooth it?"

### Prescriptive vs. Descriptive Feedback

**Prescriptive feedback** tells the designer what to do:
- "Make the font bigger"
- "Move the signup button above the fold"
- "Use our brand blue for this"

**Descriptive feedback** describes the problem and lets the designer solve it:
- "I'm having trouble reading this text on mobile -- the hierarchy isn't clear"
- "I worry users won't discover the signup action -- it feels buried"
- "This screen doesn't feel like it belongs in our app -- something about the color palette feels off"

**Why descriptive is better:**
1. The designer has more context about design tradeoffs than you do
2. Descriptive feedback opens a conversation; prescriptive feedback closes it
3. The designer may find a better solution than your specific suggestion
4. It respects the designer's expertise and agency

**When prescriptive is acceptable:**
- When you're the domain expert (e.g., "The engagement format needs to include the key closing element -- it's a product tradition requirement")
- When there's a hard business constraint ("Legal says we must show the subscription price before checkout")
- When you're reviewing copy, not design ("This should say 'engagement session' not 'meditation' -- it's our brand vocabulary")

Full critique structure and PM Crit framework -> `references/design-critique-framework.md`

---

## Module 3: Cross-Functional Collaboration

### The Four Pillars of PM-Designer Collaboration

**Pillar 1: Invest in Understanding Product Design**
- Learn the basics of design principles (hierarchy, contrast, proximity, alignment)
- Understand the design tools your designer uses (Figma, etc.) well enough to review work effectively
- Read about design thinking -- not to become a designer, but to speak the same language

**Pillar 2: Prioritize Open Conversation**
- Establish weekly 1:1s with your designer (Bergher considers this foundational)
- Don't limit conversations to current projects -- talk about craft, career, vision
- Create psychological safety to disagree (the best PM-designer relationships involve healthy tension)

**Pillar 3: Share All Context, Not Just Tasks**
- Share the business strategy, competitive landscape, and user research
- Share the "why" behind priorities, not just the prioritized list
- Include the designer in stakeholder conversations when possible
- Don't filter information -- let the designer draw their own conclusions

**Pillar 4: Build Mutual Understanding**
- Understand what motivates your designer (craft excellence? user impact? career growth?)
- Help your designer understand your constraints (business metrics, timelines, technical debt)
- Celebrate design wins publicly -- make design quality visible to leadership

### Handling PM-Designer Disagreements

**Step 1: Identify the type of disagreement**
- Taste disagreement (subjective preference) -- Defer to the designer
- User impact disagreement (will users benefit?) -- Resolve with data/research
- Business impact disagreement (will it drive metrics?) -- PM makes the call with designer input
- Feasibility disagreement (can we build it?) -- Engineering makes the call

**Step 2: Separate opinions from evidence**
- "I don't like the color" is an opinion
- "Users couldn't find the CTA in testing" is evidence
- Always seek evidence before pulling rank

**Step 3: Make the decision and move forward**
- Once decided, both PM and designer commit to the direction
- Document the reasoning so it can be revisited with new data
- Never say "I told you so" if the decision turns out wrong

---

## Module 4: Building Coherent Product Experiences

### Coherent, Not Consistent

Bergher's most influential framework challenges the conventional wisdom that consistency is the highest design virtue.

**Consistency** means: Every element follows the same pattern, the same spacing, the same component library, everywhere.

**Coherence** means: Every part of the product feels like it belongs, even if different parts use different patterns when appropriate.

**Why coherence beats consistency:**

1. **Consistency has hidden costs.** It adds overhead to new projects (must validate against the system), creates gatekeeping (designs get rejected for system violations rather than user problems), and eats time that could improve the product.

2. **Consistency blocks innovation.** If every new feature must match existing patterns, you can never explore fundamentally new approaches. The design system becomes a cage rather than a foundation.

3. **Consistency can hurt users.** Different contexts sometimes need different patterns. A checkout flow has different needs than a content browsing flow -- forcing both into identical patterns may harm usability.

### Where Consistency IS Essential

Bergher identifies four areas where strict consistency remains critical:

1. **Information Architecture** -- Users should always find information in the same place across surfaces
2. **Nomenclature** -- Use the same terms consistently (always "engagement session," never switching to "meditation" or "lesson")
3. **Iconography** -- Icons must maintain the same meaning everywhere in the UI
4. **Core Brand Elements** -- Brand colors, typography, and logo usage should never deviate

### Where Coherence Allows Flexibility

Everything else -- layout, component usage, interaction patterns, visual style -- can vary as long as it feels like it belongs:

- A new community group feature can use a different card layout than the content feed, as long as the typography and color language are recognizable
- An experimental onboarding flow can break existing patterns if it better serves new users
- A promotional screen can use bolder visuals than the daily experience, as long as it still feels like your product

### Practical Approach: Periodic Consistency Bug Bashes

Rather than blocking releases for consistency issues, Bergher recommends periodic "consistency-themed bug bashes" where the team identifies and fixes inconsistencies as medium-priority maintenance work. This keeps the product coherent without slowing down shipping.

### The Vision and Design Language

Bergher's approach to developing a product vision includes four steps:

1. **Articulate the product's identity** -- What does this product believe? What does it stand for?
2. **Define the emotional territory** -- How should users feel when using it?
3. **Establish design principles** -- 3-5 principles that guide decisions (not rules that constrain them)
4. **Create alignment through examples** -- Show, don't just tell. A moodboard beats a principles doc.

### Design Principles for your product (Example)

Using Bergher's framework:

1. **Calm over clever.** The UI should feel peaceful, never anxious or demanding. Avoid aggressive CTAs, countdown timers, or FOMO tactics that conflict with the personal tone.
2. **Guided, not overwhelming.** Present one clear path forward. Don't show the user everything at once -- guide them through content discovery naturally.
3. **Community without exposure.** Social features should feel supportive and safe, never performative. Engagement requests should feel intimate, not like social media posts.
4. **Daily rhythm.** The design should support a daily habit -- quick to enter, clear progression, gentle reminders. Respect the user's time and attention.

### The Vicious Cycle of Shipping Slow

Bergher warns about a common trap: when teams ship slowly, design quality actually decreases (not increases). The vicious cycle:

1. Long timelines lead to scope creep
2. Scope creep leads to design compromises
3. Compromises lead to worse products
4. Worse products lead to requests for redesign
5. Redesigns add to timelines

**Breaking the cycle:** Ship smaller, faster increments. Each increment should be coherent on its own -- not a half-finished version of a grand vision. Design for what can ship in 2-4 weeks, then iterate.

Full deep-dive with coherence framework, rank-ordering, and branding exercise -> `references/coherent-product-design.md`

---

## Decision Tools

### Decision 1: When to Involve Design

```
Is this change user-facing?
+-- No (backend, infrastructure, data) --> Design involvement optional
|   +-- But does it affect future user-facing work? --> Brief the designer
+-- Yes
    +-- Is it a net-new feature or flow?
    |   +-- Yes --> Involve designer from problem definition (Day 0)
    |   +-- No, it's a modification to existing feature
    |       +-- Does it change the interaction model?
    |       |   +-- Yes --> Involve designer for exploration
    |       |   +-- No (copy change, minor tweak) --> Designer review before ship
    |       +-- Does it affect multiple screens/flows?
    |           +-- Yes --> Involve designer to assess system impact
    |           +-- No --> Designer review before ship
```

### Decision 2: How to Give Feedback on Design Work

```
What stage is the design at?
+-- Concept/exploration
|   +-- Give DIRECTION feedback only
|   +-- "Does this approach solve the user problem?"
|   +-- DO NOT comment on visual details, spacing, or copy
+-- Wireframe/flow
|   +-- Give FLOW feedback
|   +-- "Does the user journey make sense? Are steps missing?"
|   +-- DO NOT comment on visual polish
+-- High-fidelity mockup
|   +-- Give DETAIL feedback
|   +-- "Is the copy clear? Are edge cases handled?"
|   +-- Visual feedback now appropriate
+-- Pre-ship / prototype
    +-- Give POLISH feedback
    +-- "Does it feel right in use? Are transitions smooth?"
    +-- Everything is fair game
```

### Decision 3: How to Resolve a PM-Designer Disagreement

```
What is the disagreement about?
+-- Aesthetic preference (color, style, visual tone)
|   +-- Defer to designer (this is their expertise)
|   +-- Unless it conflicts with brand guidelines --> Brand team decides
+-- User impact (will users understand/use this?)
|   +-- Is there data or research to resolve it?
|   |   +-- Yes --> Let data decide
|   |   +-- No --> Run a quick test (usability test, A/B, user interview)
|   |       +-- Can't test? --> PM makes the call, document reasoning
+-- Business impact (will this drive our metrics?)
|   +-- PM makes the call
|   +-- Share the full reasoning with the designer
|   +-- Revisit if metrics don't materialize
+-- Technical feasibility (can we build this?)
    +-- Engineering makes the call
    +-- Ask: "What's the closest achievable version?"
```

---

## Applied to your product

your product sits at a unique intersection where design decisions carry emotional and personal weight beyond typical consumer apps. A engagement session app's design isn't just about usability -- it's about creating a intentional space in a user's daily life.

**Coherence Application:** your product spans audio engagement sessions, content reading, engagement communities, and premium content. These experiences should feel coherent (all clearly your product) without being forced into identical patterns. The audio engagement session player should feel calm and meditative; the community should feel warm and supportive; the content library should feel curated and inviting. Same brand, different moods, all coherent.

**Specific Hypotheses:**
- Running a "Calm Audit" where PM and designer review every screen for emotional tone could surface 3-5 places where the design creates anxiety instead of peace (aggressive upsell modals, complex navigation, overwhelming content grids)
- Implementing design critiques specifically focused on "Does this feel like your product?" could improve design coherence without creating rigid consistency rules
- Moving designer involvement to Day 0 of new feature planning (rather than after PRD) could reduce design cycles by 30% by avoiding misdirected exploration

**Key Metric to Watch:** "Time to first meaningful engagement session" -- the time between app open and a user engaging with content. This is where design quality most directly affects the daily habit.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| Feedback Ladder | Framework for matching feedback granularity to design stage (direction, flow, detail, polish) |
| Prescriptive Feedback | Feedback that tells the designer what to do ("Move the button left") -- usually counterproductive |
| Descriptive Feedback | Feedback that describes the problem and lets the designer solve it ("Users can't find the CTA") |
| Coherence | Design principle where every part of a product feels like it belongs, without requiring identical patterns |
| Consistency | Design principle where every element follows the same pattern -- valuable but often over-applied |
| Design Critique | Structured feedback session where designers present work for peer review, focused on specific questions |
| PM Crit | Bruno Bergher's framework for applying design critique methodology to PM work (PRDs, strategies, analyses) |
| Context Sharing | The practice of giving designers full business, user, technical, and decision context before design begins |
| Coherence Bug Bash | Periodic team exercise to identify and fix design inconsistencies as maintenance work |
| Double Diamond | Design process model: Discover (explore problem), Define (frame problem), Develop (explore solutions), Deliver (refine solution) |

---

## Reference Files

- `references/design-critique-framework.md` -- How to run design critiques, the prescriptive-to-descriptive spectrum, PM Crits, and building a critique culture
- `references/coherent-product-design.md` -- Bergher's "coherent, not consistent" philosophy, product vision development, the vicious cycle of shipping slow, and rank-ordering design priorities
