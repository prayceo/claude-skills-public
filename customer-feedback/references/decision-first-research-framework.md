## Contents
- The Core Principle
- The Five-Step Decision-First Process
  - Step 1: Define the Decision
  - Step 2: Map the Evidence Landscape
  - Step 3: Select the Minimum Viable Method
  - Step 4: Execute with Discipline
  - Step 5: Synthesize for Decision
- The Research Brief in Practice
- Common Decision-First Anti-Patterns at your company
  - "We should talk to users about the app"
  - "Let's survey all our users"
  - "The executive wants research to support the new feature"
  - "We don't have time for research"
- Measuring Research Effectiveness

---
# Decision-First Research Framework — Deep Reference
*Source: Behzod Sirjani, Mastering Customer Feedback; Growthmates interview; Research That Scales Episode 6*

---

## The Core Principle

Most product teams practice "decision-last" research: they collect feedback, generate insights, and then try to figure out what to do with the findings. This is backwards. Decision-first research starts with the end state — the specific decision that needs to be made — and works backward to determine exactly what evidence is required.

> "Scaling research is the work of building and supporting whatever it takes to gather and synthesise more evidence to make better decisions in service of our customers."

The decision-first approach eliminates the two most common research failures:
1. **Shelf research:** Insights that are interesting but never acted on because no decision was waiting for them
2. **Confirmation research:** Studies designed to validate what the team already believes rather than genuinely testing assumptions

---

## The Five-Step Decision-First Process

### Step 1: Define the Decision

Before any research activity, articulate the specific decision the research will inform. This is harder than it sounds. Most teams default to vague learning objectives.

**Decision Quality Checklist:**

```
[ ] Is this a real decision (not just curiosity)?
    BAD:  "Let's learn about our users' daily habits"
    GOOD: "Should we invest Q3 in a community activity feature or enhanced solo engagement sessions?"

[ ] Are there identifiable alternatives?
    BAD:  "How should we improve onboarding?"
    GOOD: "Should onboarding focus on content sampling, preference setup, or social connection?"

[ ] Is there a decision-maker?
    BAD:  "The team would benefit from understanding this"
    GOOD: "The VP of Product needs this to finalize the Q3 roadmap"

[ ] Is there a deadline?
    BAD:  "Whenever we get to it"
    GOOD: "Sprint planning is March 15 — we need findings by March 12"

[ ] Would the decision be different based on research findings?
    BAD:  Leadership has already decided; research is for optics
    GOOD: The team is genuinely split and evidence would tip the scale
```

### Step 2: Map the Evidence Landscape

Once the decision is clear, identify what evidence already exists and what gaps remain.

**Evidence Inventory Template:**

| Evidence Type | What We Have | Confidence | Gap |
|--------------|-------------|------------|-----|
| Behavioral data | 6 months of engagement analytics | High | No data on group sessions behavior |
| Qualitative | 3 customer interviews from Q1 | Low | Outdated, small sample |
| Market data | Competitor feature comparison | Medium | No demand validation |
| Internal expertise | PM intuition based on support tickets | Medium | Not systematic |
| Survey data | NPS scores by segment | Medium | No feature-level feedback |

**Gap Prioritization:**
- Which gaps, if filled, would most change the decision?
- Which gaps can be filled within the timeline?
- Which gaps can we accept as remaining uncertainty?

### Step 3: Select the Minimum Viable Method

Choose the research method that fills the most critical evidence gap within the time constraint. Sirjani emphasizes minimum viable research — not the most rigorous method, but the method that provides sufficient evidence for the decision at hand.

**Method Selection by Time Available:**

| Time Available | Method Options | Participants | Confidence Level |
|---------------|---------------|-------------|-----------------|
| 1-2 days | Desk research + stakeholder interviews | 0 external | Low but fast |
| 3-5 days | Guerrilla usability test OR quick survey | 5-8 users | Low-medium |
| 1-2 weeks | Semi-structured interviews | 8-12 users | Medium |
| 2-4 weeks | Full research sprint (interviews + survey) | 12-15 interviews + 200 survey | Medium-high |
| 4-8 weeks | Mixed methods longitudinal study | 20+ across methods | High |

**The 80/20 Rule of Research:**
80% of the useful insight comes from the first 20% of research effort. Five well-conducted interviews reveal more than a poorly designed survey of 500 people. The goal is not exhaustive knowledge — it is sufficient confidence to make a good decision.

### Step 4: Execute with Discipline

Research execution failures usually come from three sources:

**1. Recruitment Failure**
- Start recruiting on Day 1 (recruitment always takes longer than expected)
- Have a standing panel of users ready to activate (the "feedback river" approach)
- Incentivize appropriately: your product could offer 3 months free premium, not cash
- Screen for behavioral diversity, not just demographics

**2. Moderation Failure**
- Ask open-ended questions ("Tell me about...") not leading ones ("Don't you think...")
- Follow the participant's story, not your script
- Listen for 70% of the time, speak for 30%
- Probe on surprises: "That's interesting — can you say more about why?"

**3. Documentation Failure**
- Record every session (with permission)
- Take notes in real-time using a structured template
- Capture verbatim quotes — paraphrasing loses the voice
- Note non-verbal cues: hesitation, confusion, excitement

**Session Documentation Template:**

```
PARTICIPANT: [ID]    DATE: [Date]    INTERVIEWER: [Name]

CONTEXT:
- User segment: [new/active/churned/free/paid]
- Usage pattern: [daily/weekly/sporadic]
- Key characteristic: [relevant trait]

KEY QUOTES:
1. "[Verbatim quote]" — Context: [when/why they said it]
2. "[Verbatim quote]" — Context: [when/why they said it]

BEHAVIORS OBSERVED:
- [What they did, not what they said]

SURPRISES:
- [Anything unexpected]

RELEVANCE TO DECISION:
- [How does this inform the decision we're trying to make?]
```

### Step 5: Synthesize for Decision

The synthesis step bridges evidence and action. Sirjani's approach:

**1. Individual Analysis:** After each session, write a one-paragraph summary answering "What did this participant tell us about our decision?"

**2. Cross-Participant Pattern Analysis:**
- Create an affinity map grouping observations by theme
- Count frequency: How many participants exhibited each pattern?
- Note intensity: How strongly did participants feel about each theme?
- Check for segments: Do patterns differ by user type?

**3. Decision Recommendation:**
- State the recommendation clearly: "Based on X evidence, we recommend Y"
- Quantify confidence: "We are [high/medium/low] confidence because..."
- Acknowledge what we still don't know
- Specify what would change our mind

---

## The Research Brief in Practice

The research brief is the single most important document in the decision-first process. It forces alignment before any time is spent.

```
============================================
RESEARCH BRIEF
============================================

PROJECT: [Name]
DATE: [Date]
RESEARCHER: [Name]
DECISION MAKER: [Name]

--------------------------------------------
THE DECISION
--------------------------------------------
What specific decision will this research inform?
[One clear sentence]

What are the possible outcomes of this decision?
Option A: _______________
Option B: _______________
Option C: _______________

When does this decision need to be made?
[Date]

--------------------------------------------
CURRENT STATE
--------------------------------------------
What do we currently believe?
[The team's hypothesis]

What evidence supports this belief?
[Existing data, anecdotes, intuition]

What would change our mind?
[Specific evidence that would shift the decision]

--------------------------------------------
RESEARCH DESIGN
--------------------------------------------
Method: _______________
Sample: _______________
Timeline: _______________
Analysis approach: _______________

--------------------------------------------
DELIVERABLE
--------------------------------------------
What artifact will communicate findings?
[Report, presentation, workshop, email]

Who needs to see it?
[Specific names and roles]

When will it be delivered?
[Date — must be before decision deadline]

--------------------------------------------
SUCCESS CRITERIA
--------------------------------------------
This research will be successful if:
[We have enough evidence to make a confident recommendation]

This research will have failed if:
[The findings are too vague to differentiate between options]

============================================
```

---

## Common Decision-First Anti-Patterns at your company

### "We should talk to users about the app"
**Problem:** No decision, no focus. Conversations will wander and produce interesting-but-useless anecdotes.
**Fix:** "We need to decide whether to invest in audio-only content or video engagement sessions for Q3. Let's interview 12 users about their content consumption habits to inform this decision."

### "Let's survey all our users"
**Problem:** Surveys are only useful for quantifying known patterns, not discovering new ones. A survey without a specific decision question produces a spreadsheet of noise.
**Fix:** "We believe 40% of churned users left because of content staleness. Let's survey 200 recently churned users to validate this hypothesis and size the opportunity."

### "The executive wants research to support the new feature"
**Problem:** This is confirmation research — the decision is already made. Research becomes theater.
**Fix:** Reframe the research question as "Under what conditions would this feature succeed or fail?" This produces genuinely useful findings even when the strategic direction is set.

### "We don't have time for research"
**Problem:** Usually means "we don't have time for a 6-week study." But not all research takes 6 weeks.
**Fix:** "We have 3 days. Let's do 5 rapid interviews with users who recently completed onboarding to validate our top 3 assumptions about the new flow."

---

## Measuring Research Effectiveness

Research is an investment. Measure its return.

**Leading Indicators:**
- Research utilization rate: % of research projects referenced in subsequent product decisions
- Time to insight: Days from research question to delivered finding
- Stakeholder satisfaction: Do decision-makers find research useful?
- Research coverage: % of major product decisions informed by some evidence

**Lagging Indicators:**
- Decision quality: Did research-informed decisions produce better outcomes?
- Confidence calibration: Were we right about what we were confident about?
- Rework reduction: Did research reduce wasted engineering effort?

**your product Research Dashboard:**

| Metric | Current (Estimated) | Q3 Target | Q4 Target |
|--------|-------------------|-----------|-----------|
| Research-informed decisions | ~20% | 50% | 70% |
| Time to insight | 4-6 weeks | 2 weeks | 1 week |
| Active research panel | 0 | 30 users | 50 users |
| Feedback rivers active | 1 (support) | 3 | 5 |
| Research repository items | 0 | 10 | 25 |
