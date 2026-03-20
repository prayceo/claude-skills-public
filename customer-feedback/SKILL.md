---
name: customer-feedback
description: Applies Behzod Sirjani's decision-first customer feedback frameworks to systematically gather, synthesize, and act on user insights at your company. Covers research planning, feedback collection methods, insight synthesis, and stakeholder communication. Activates when planning user research, designing interview guides, setting up feedback systems, synthesizing qualitative data, choosing between research methods, or building a case from customer evidence to influence product decisions.
---

**Reference files:**
- `references/decision-first-research-framework.md` — The complete decision-first approach to planning and executing research that drives action
- `references/feedback-collection-methods.md` — Deep playbook for choosing and executing the right feedback method at the right time
- `references/insight-synthesis-and-storytelling.md` — Framework for transforming raw research data into compelling narratives that drive organizational decisions

---

## How to Use This Skill

When this skill activates:
1. Identify which customer feedback framework from this skill best applies to the question
2. Apply the relevant decision tree from the Decision Tools section
3. Ground all recommendations in the context of your product
4. Cite the specific framework when making claims
5. If deeper detail is needed, read the relevant reference file before responding

## Gotchas

Common mistakes to avoid when applying these frameworks:

1. **Don't start with the research method -- start with the decision.** Sirjani's Decision-First Framework means every research project must begin with "What decision will this inform?" not "Should we do interviews or a survey?" If you can't name the specific decision, you're setting up for insight-rich, action-poor research that never gets used.
2. **Don't confuse stated interest with validated demand.** Users saying "that sounds great" in an interview is the weakest signal Sirjani identifies. At your company, users may enthusiastically endorse a "accountability partner matching" concept out of politeness or aspiration, but never actually use it. Focus research on what people *do*, not what they *say* they'd do.
3. **Don't skip the evidence threshold assessment.** Sirjani's 2x2 (reversibility x impact) determines how much research you need. A small UI copy change (high reversibility, low impact) needs zero research -- just ship it. A new subscription tier structure (low reversibility, high impact) needs mixed methods. Applying the same research depth to both wastes time on one and under-invests in the other.
4. **Don't treat synthesis as optional.** Raw interview quotes are not insights. Sirjani's synthesis pipeline (raw data -> observations -> patterns -> insights -> recommendations) requires three passes through the data. Skipping to "here's what users said" without coding and theming means stakeholders get anecdotes, not actionable intelligence.

## Example

**User asks:** "We're thinking about adding a community activity wall feature. Should we do user research first?"

**Approach:**
1. Apply the Decision-First Framework -- define the specific decision: "Should we invest a full quarter in building a public engagement wall, and if so, what form should it take?" This is a medium-to-high consequence decision (significant engineering investment, partially reversible)
2. Use the evidence threshold 2x2 -- this is medium reversibility (can remove it but sunk cost is real) and medium-high impact (touches community dynamics and content moderation). Recommend a standard research sprint: 12-15 interviews over 2-3 weeks
3. Select the right method -- since the team doesn't yet understand the problem space around communal engagement (generative need), recommend in-depth interviews with users segmented by engagement frequency and community engagement, focusing on current workarounds and emotional needs around shared engagement
4. Define the stopping criteria upfront -- research is "done" when the team can answer: Do users want public engagement sharing? What are the trust/privacy concerns? What form factor matches existing engagement behavior? Recommend synthesizing with Sirjani's five-level pipeline before presenting to stakeholders

---

## Core Philosophy

Sirjani's approach starts from a counterintuitive premise: most organizations collect too much feedback, not too little. The problem is a shortage of clarity about what decisions the data should inform. His "decision-first" framework reverses the typical process -- instead of starting with "what should we learn?" he starts with "what decision do we need to make?" and works backward to the minimum evidence required. This prevents the two most common research failures: gathering insights that never get used, and conducting research that confirms what the team already believes.

His second core principle: research is not a department -- it is an organizational capability. The goal is to help everyone in the organization become a better decision-maker by bringing more rigor to their curiosity.

---

## Module 1: Decision-First Research Planning

The most common mistake is "decision-last research" -- teams collect feedback, generate insights, then try to figure out what to do with them. **Decision-first research** starts with the end state: (1) Define the specific decision, (2) Determine what evidence would make you confident, (3) Select the minimum viable method, (4) Execute with discipline, (5) Synthesize for decision.

A well-formed research decision is **specific** (names the exact choice), **bounded** (finite set of outcomes), **timely** (clear deadline), and **consequential** (worth the research investment). The **evidence threshold** uses a 2x2 of reversibility vs. impact: high reversibility + low impact = skip research, just ship it; low reversibility + high impact = deep research with mixed methods.

Key anti-patterns: **Validation theater** (using research to confirm decisions already made), **Boil the ocean** (trying to answer everything in one study), **Perpetual discovery** (continuous research without decision points), **Stakeholder surprise** (researching without aligning on what evidence would change minds).

*-> Full detail: `references/decision-first-research-framework.md`*

---

## Module 2: Feedback Collection Methods

Four categories of research, each serving a different purpose:

| Category | Purpose | Key Methods |
|----------|---------|-------------|
| **Generative** | Discover unmet needs and new opportunities | In-depth interviews, diary studies, contextual inquiry |
| **Evaluative** | Assess whether something works as intended | Usability testing, A/B testing, concept testing |
| **Descriptive** | Measure current state and quantify behaviors | Surveys, analytics review, benchmarking |
| **Causal** | Understand cause-and-effect relationships | Controlled experiments, cohort analysis, regression |

**Interviews** are the most versatile tool. The interview arc: context (5 min) -> behavior (15 min) -> needs/pain (10 min) -> reaction (10 min) -> wrap-up (5 min). Focus on what people DO, not what they SAY they do. Silence is a tool -- wait 3-5 seconds after an answer for deeper insight.

**Feedback rivers** are continuous streams of customer signal: support tickets, app store reviews, sales call notes, social media, NPS/CSAT, in-app feedback. Improve the quality of feedback already flowing rather than creating new channels. Build a **Accountability Partner Panel** (25-50 opted-in users segmented by engagement, subscription status, and product convention) as a standing research resource.

*-> Full detail: `references/feedback-collection-methods.md`*

---

## Module 3: Insight Synthesis and Sense-Making

Raw data is not insight. The synthesis pipeline: **raw data -> observations -> patterns -> insights -> recommendations -> decisions**. The five levels of analysis progress from transcription (what they said) through observation, pattern, insight, to recommendation (what to do about it).

**Coding and theming**: Read all data once without coding, then create initial codes on second pass, group codes into themes on third pass. A strong theme is mentioned by 60%+ of participants, appears across segments, shows strong emotional intensity, is consistent in direction, and has clear product implications.

The **insight hierarchy** ranks findings by potential impact: Level 1 (preference -- what users say they want), Level 2 (usability -- friction that can be removed), Level 3 (behavioral -- unexpected patterns affecting key metrics), Level 4 (strategic -- changes understanding of market or customers).

*-> Full detail: `references/insight-synthesis-and-storytelling.md`*

---

## Module 4: Communicating Research and Driving Action

Research only matters if it changes decisions. The **research narrative** follows: situation -> finding -> insight ("so what?") -> recommendation -> evidence (appendix for skeptics).

Tailor by audience: **Executives** (2 min) -- lead with recommendation, one slide, clear ask. **Product/design partners** (30 min) -- lead with findings, show video clips, co-create action plan. **Broader org** (5 min) -- one vivid user story connected to company goals.

The **research maturity model** tracks organizational growth: Level 1 (ad hoc) through Level 5 (cultural, where every decision references customer evidence). your product is likely Level 1-2; the path to Level 3 requires a research plan tied to the product roadmap, a shared repository, and basic research training for PMs.

*-> Full detail: `references/insight-synthesis-and-storytelling.md`*

---

## Decision Tools

### Decision 1: Which Research Method to Use

```
START: What decision are we trying to make?
|
+-- "What should we build next?"
|   +-- Do we understand the problem space?
|   |   +-- NO -> Generative interviews (12-20 users)
|   |   +-- YES -> Concept testing with prototypes (8-12 users)
|   +-- Is this a new market/segment?
|       +-- YES -> Ethnographic/contextual inquiry (8-12 users)
|       +-- NO -> Jobs-to-be-done interviews (12-15 users)
|
+-- "Is this design working?"
|   +-- Pre-launch?
|   |   +-- YES -> Usability testing (5-8 users per round)
|   |   +-- NO -> A/B test + follow-up interviews
|   +-- Specific flow or holistic experience?
|       +-- FLOW -> Task-based usability test
|       +-- HOLISTIC -> Diary study (15-20 users, 2 weeks)
|
+-- "How big is this problem?"
|   +-- Do we have behavioral data?
|   |   +-- YES -> Analytics deep dive + validation interviews
|   |   +-- NO -> Quantitative survey (200+ respondents)
|   +-- Do we need to segment?
|       +-- YES -> Survey with segmentation analysis
|       +-- NO -> Simple frequency/severity rating
|
+-- "Why is this metric moving?"
    +-- Sudden change?
    |   +-- YES -> Analytics investigation + rapid interviews (5-8 users)
    |   +-- NO -> Longitudinal behavioral analysis
    +-- Can we isolate the variable?
        +-- YES -> Controlled experiment
        +-- NO -> Mixed methods (quant + qual triangulation)
```

### Decision 2: How Much Research Is Enough

```
START: How consequential is this decision?
|
+-- LOW consequence (easily reversible, low cost)
|   +-- Ship it and measure
|   +-- No research needed -- set up analytics to learn post-launch
|
+-- MEDIUM consequence (some investment, partially reversible)
|   +-- Do we have existing data/research?
|   |   +-- YES -> Quick synthesis of existing evidence (1-2 days)
|   |   +-- NO -> Lightweight research: 5-8 interviews OR survey (1-2 weeks)
|   +-- Confidence threshold: 70%+ team alignment on direction
|
+-- HIGH consequence (significant investment, hard to reverse)
|   +-- Standard research sprint: 12-15 interviews + analysis (2-4 weeks)
|   +-- Complement with quantitative data where possible
|   +-- Confidence threshold: Clear evidence pattern across participants
|
+-- CRITICAL consequence (company-level bet, irreversible)
    +-- Mixed methods: Interviews + survey + behavioral data + competitive
    +-- Multiple rounds of research with iteration
    +-- External validation (market sizing, expert review)
    +-- Confidence threshold: Triangulation across 3+ data sources
```

### Decision 3: When to Stop Collecting and Start Acting

```
START: Have we reached the decision deadline?
|
+-- YES -> Synthesize what we have and decide
|   +-- Enough evidence for a directional bet?
|   |   +-- YES -> Make the decision, document confidence level
|   |   +-- NO -> Make the decision, but plan post-launch research
|   +-- Flag: Missing evidence and residual risk
|
+-- NO -> Are we seeing new themes in each interview?
    +-- YES -> Continue collecting (haven't reached saturation)
    |   +-- But check: Are new themes relevant to our decision?
    |       +-- YES -> Continue
    |       +-- NO -> Stop -- new themes are interesting but out of scope
    |
    +-- NO -> Likely reached saturation
        +-- Have at least 3 data points per key theme?
        |   +-- YES -> Stop collecting, begin synthesis
        |   +-- NO -> Targeted recruitment for under-represented segments
        +-- Can the remaining uncertainty be resolved post-launch?
            +-- YES -> Ship with measurement plan
            +-- NO -> One more round focused on the specific gap
```

---

## Applied to your product

your product's most critical product decisions -- what content to produce, how to structure the core experience, how to convert free users to subscribers -- all benefit from systematic user research. The biggest risk is building based on assumptions about what "consumer users want" rather than observing what they actually do. Wellness and personality are deeply personal; surface-level feedback masks the real drivers of engagement and retention.

**Highest-Leverage Action: Build a Continuous Feedback System.**
1. Tag all support tickets by product area and user segment
2. Establish a "Accountability Partner Panel" -- 30-50 opted-in users segmented by engagement, subscription status, and product convention
3. Implement in-context feedback prompts at key moments (after completing a engagement session, after 7 consecutive days, at the paywall)
4. Run quarterly "decision sprint" research focused on the highest-impact product decision each quarter

**Key Hypotheses to Test:**
- "Users who engage with others retain at higher rates than solo users" -- behavioral analysis + interviews
- "Free users who engage with 3+ content types before the paywall convert at higher rates" -- analytics + churner interviews
- "Daily notification timing should match users' existing daily routine, not a generic morning send" -- diary study

**Research Maturity Assessment:** Likely Level 1-2 (Ad Hoc to Reactive). Path to Level 3 requires a research plan tied to the product roadmap, a shared repository, and basic research training for PMs -- achievable in one quarter.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| Decision-first research | Planning research by starting with the decision to be made, then working backward to determine what evidence is needed |
| Feedback river | A continuous, passive stream of customer feedback flowing from support, sales, reviews, and other existing channels |
| Research saturation | The point at which additional interviews stop producing new themes relevant to the research question |
| Evidence threshold | The minimum amount and quality of evidence required to make a decision with acceptable confidence |
| Generative research | Research aimed at discovering new opportunities, needs, and problem spaces (vs. evaluating existing solutions) |
| Evaluative research | Research aimed at assessing how well an existing or proposed solution works for users |
| Insight hierarchy | The ranking of insights from preference (least actionable) to strategic (most transformative) |
| Research democratization | Building the capability for non-researchers (PMs, designers, engineers) to conduct basic research effectively |
| Synthesis | The process of transforming raw research data into patterns, insights, and actionable recommendations |
| Research brief | A one-page alignment document created before research begins that defines the decision, method, and success criteria |
| Validation theater | The anti-pattern of using research to confirm a decision already made rather than genuinely testing assumptions |
| Organizational anthropology | Applying research skills inward to understand how the company makes decisions, not just outward to understand customers |
| Research operations | The infrastructure, tools, and processes that enable research to happen consistently and at quality |
| Coding (qualitative) | The process of labeling segments of qualitative data with short descriptive tags to enable pattern identification |
| Triangulation | Using multiple research methods or data sources to validate a finding, increasing confidence in the insight |

---

## Reference Files

- `references/decision-first-research-framework.md` — Decision-first sequence, evidence inventory, minimum viable method selection, research brief template, anti-patterns, measuring research effectiveness
- `references/feedback-collection-methods.md` — Four research categories with method details, interview guide templates, usability test scripts, feedback river architecture, customer advisory board structure, method selection quick reference
- `references/insight-synthesis-and-storytelling.md` — Synthesis pipeline (capture/code/theme/insight/recommend), bias avoidance, research narrative framework, audience tailoring, video highlight reel structure, repository architecture, research maturity model
