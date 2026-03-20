---
name: gatena-cookbook
description: "Analyze, improve, and CREATE designs using 190 behavioural science principles from the Gatena Cookbook research and academic literature. Use in TWO scenarios. REVIEWING - Trigger when the user asks to review, audit, critique, or improve any design including screenshots, mockups, wireframes, landing pages, product flows, marketing materials, or branding. Even 'review my design' or 'how can I improve this' should trigger this. CREATING FROM SCRATCH - Trigger when the user asks to design, build, or create any UI, landing page, website, app screen, product flow, pricing page, checkout, signup form, dashboard, or any user-facing design. Apply behavioural principles proactively during creation. Also trigger for 'what principles apply here', behavioural audits, nudges, cognitive biases, persuasion, or conversion optimization."
---

# Gatena Cookbook

**Author:** Steve Gatena

Apply 190 behavioural science principles — sourced from the Gatena Cookbook research and academic literature — to analyze, audit, and create high-converting designs.

## When to Use This Skill

- Reviewing/critiquing any design (screenshot, mockup, wireframe, prototype)
- Creating new designs with behavioural science principles applied
- Auditing a page, flow, or experience for behavioural opportunities
- Suggesting which principles to apply to a specific design challenge
- Scoring a design against behavioural best practices
- Diagnosing why a design is underperforming (conversion, engagement, retention)

## Step 1: Load the Principle Library

Before any analysis, read the full principle reference. The file is located in the same directory as this skill:

```
Read references/principles.md
```

This file contains 190 principles organized into 13 categories. Each principle includes:
- **Name** and definition
- **Design application** — concrete, actionable guidance
- **Academic citation** (📎) where available — sourced from the Gatena Cookbook's peer-reviewed research base

The citations matter because they let you explain *why* a recommendation works, not just *what* to do. When presenting recommendations, cite the underlying research to build credibility with stakeholders.

## Step 2: Determine the Analysis Mode

Based on the user's request, operate in one or more of these modes:

### Mode A: Issue Identification + Fix Suggestions
1. Examine the design carefully
2. Identify specific elements that conflict with behavioural principles
3. For each issue, name the principle, explain the conflict, and suggest a concrete fix
4. Prioritize issues by likely impact on user behaviour
5. Format: List of issues ranked by severity, each with principle name, problem, and solution

### Mode B: Behavioural Audit / Scorecard
1. Evaluate the design against the most relevant principles for its type
2. Select 20-30 principles most applicable to this specific design
3. Score each as: ✅ Well Applied | ⚠️ Opportunity | ❌ Violation | ➖ N/A
4. Provide an overall behavioural design score (percentage of applicable principles well-applied)
5. Format: Scorecard table with principle, status, and brief note

### Mode C: Proactive Principle Application
1. Understand the design's goal (conversion, engagement, trust, etc.)
2. Select the 10-15 most impactful principles for that goal
3. For each, describe specifically how to apply it to this design
4. Include implementation priority (quick win vs. major redesign)
5. Format: Prioritized recommendation list with effort/impact ratings

### Mode D: Design Creation (From Scratch)
When creating a new design rather than reviewing one:
1. Ask about the design's primary goal, audience, and context
2. Select 8-12 principles most relevant to the goal using the category mapping in Step 3
3. Create a brief **Behavioural Strategy** before designing:
   - Primary goal (conversion, trust, engagement, retention, etc.)
   - Target audience mindset (cautious, curious, impatient, skeptical, etc.)
   - Top principles to apply and WHERE in the design they'll appear
4. Build the design, explicitly integrating the selected principles into layout, copy, structure, and interaction patterns
5. After creating, provide a **Behavioural Design Notes** section that maps each design decision to its underlying principle and supporting research, e.g.:
   - "CTA colour uses Von Restorff Effect (visual isolation)"
   - "Testimonials placed before pricing leverages Social Proof — Bandura & Menlove (1968) showed vicarious modeling reduces uncertainty"
   - "Progress bar starts at 20% using Endowed Progress Effect — Nunes & Dreze (2006) found artificial advancement increases effort"
   - "Target plan in centre column uses Centre-Stage Effect — users default to middle options in horizontal layouts"

**Creation Checklist:**
- [ ] Social proof is visible near key decision points
- [ ] Cognitive load is minimized (progressive disclosure, chunking)
- [ ] Primary CTA leverages visual salience and Fitts's Law
- [ ] Copy uses appropriate framing (gain vs. loss based on context)
- [ ] Trust signals appear before commitment points
- [ ] Defaults and choice architecture are intentional
- [ ] Halo Effect leveraged — first impressions are strong and positive
- [ ] At least 3 principle categories are actively applied

## Step 3: Contextual Principle Selection

Not all 190 principles apply to every design. Use this guide to select relevant ones:

| Design Type | Priority Categories | Key Gatena Cookbook Principles |
|---|---|---|
| Product/UX flows | Decision Architecture, Cognitive Load, Motivation & Engagement, Trust & Credibility | Default Effect, Friction, Tiny Habits, Feedback Loops, Fresh Start Effect |
| Landing pages | Attention & Perception, Framing & Presentation, Trust & Credibility, Social Dynamics | Halo Effect, Social Proof, Scarcity Framing, Authority, Contrast Effect |
| E-commerce | Pricing & Value, Social Dynamics, Decision Architecture, Loss & Risk | Decoy Effect, Anchoring, Centre-Stage Effect, Zero Price Bias, Boundary Pricing |
| Branding | Emotion & Affect, Memory & Recall, Identity & Self, Social Dynamics | Nostalgia Effect, Storytelling, Biophilia Effect, Product-Person Bias, Self-Expression |
| Onboarding | Cognitive Load, Motivation & Engagement, Decision Architecture | Endowed Progress, Zeigarnik Effect, Tiny Habits, Chunking, Goal Gradient |
| Forms/Checkout | Cognitive Load, Decision Architecture, Loss & Risk, Trust & Credibility | Friction, Default Effect, Certainty Effect, Risk Reversal, Commitment |
| Retention/Loyalty | Motivation & Engagement, Emotion & Affect, Identity & Self | Hedonic Adaptation, Segregation Effect, Collection Bias, Rewards, Status |
| Pricing pages | Pricing & Value, Decision Architecture, Framing & Presentation | Anchoring, Decoy Effect, Centre-Stage Effect, Round Pricing Preference, Charm Pricing |

## Step 4: Deliver the Analysis

### Formatting Rules
- Always name the specific principle when making a recommendation
- Include the academic citation when available — this builds credibility with stakeholders and product teams
- Give concrete, actionable suggestions — not vague advice
- Use the design's own elements in examples ("Move the CTA above the testimonials" not "Put important things higher")
- When multiple principles conflict, acknowledge the tension and recommend a resolution
- Group findings by theme, not by principle number

### Quality Checklist
Before delivering, verify:
- [ ] At least 3 different principle categories are represented
- [ ] Every suggestion is specific and actionable
- [ ] Priorities are clearly indicated
- [ ] Trade-offs are acknowledged where they exist
- [ ] The analysis matches the user's design type and goals
- [ ] Academic citations are included where available to support recommendations

## Principle Categories (Quick Reference)

The full library in `references/principles.md` contains these 13 categories:

1. **Attention & Perception** — How people notice and process visual information (16 principles)
2. **Cognitive Load & Processing** — Mental effort and information handling (16 principles)
3. **Decision Architecture** — How choice environments shape decisions (18 principles)
4. **Framing & Presentation** — How context and wording change perception (17 principles)
5. **Social Dynamics** — How others influence our behaviour (18 principles)
6. **Trust & Credibility** — What makes people believe and feel safe (13 principles)
7. **Motivation & Engagement** — What drives action and sustained interest (19 principles)
8. **Emotion & Affect** — How feelings shape decisions (14 principles)
9. **Memory & Recall** — What people remember and why (14 principles)
10. **Loss, Risk & Uncertainty** — How people evaluate potential downsides (15 principles)
11. **Pricing & Value Perception** — How people assess worth and cost (14 principles)
12. **Identity & Self-Concept** — How self-image drives behaviour (10 principles)
13. **Cross-Cutting Principles** — Powerful principles that span multiple categories (8 principles)

Each principle entry includes: Name | Definition | Design Application | 📎 Academic Citation (where available)
