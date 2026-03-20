## Contents
- The Four Research Categories
  - Category 1: Generative Research
  - Category 2: Evaluative Research
  - Category 3: Descriptive Research
  - Category 4: Causal Research
- Building Feedback Rivers
  - The River Metaphor
  - Passive Feedback River Architecture
  - Setting Up Each River
  - The Customer Advisory Board
- Method Selection Quick Reference
  - By Decision Type
  - By Confidence Required
  - By Budget and Time

---
# Feedback Collection Methods — Deep Reference
*Source: Behzod Sirjani, Mastering Customer Feedback; Growthmates interview on research methods by company stage*

---

## The Four Research Categories

Sirjani organizes all research into four categories based on what you're trying to learn. Every research project should map to exactly one category — if you're trying to do two at once, split them.

### Category 1: Generative Research

**Purpose:** Discover what you don't know you don't know. Explore new problem spaces, uncover unmet needs, understand the full context of user behavior.

**When to Use:**
- Entering a new market or segment
- Planning a major new feature area
- You suspect there are user needs you haven't identified
- The product team disagrees on what the core problem is

**Methods:**

| Method | Description | Best For | Sample | Duration |
|--------|-------------|----------|--------|----------|
| In-depth interviews | 45-60 min semi-structured conversations | Understanding motivations, behaviors, mental models | 12-20 | 2-4 weeks |
| Contextual inquiry | Observe users in their natural environment | Understanding real behavior (not reported) | 8-12 | 2-3 weeks |
| Diary studies | Participants log behavior over time | Capturing habits, routines, temporal patterns | 15-25 | 2-4 weeks |
| Ethnographic observation | Immerse in the user's world | Deep cultural/contextual understanding | 5-10 | 4-8 weeks |
| Jobs-to-be-done interviews | Focus on the "job" the user is "hiring" the product for | Understanding underlying motivations | 12-20 | 2-3 weeks |

**your product Application:** Generative research should be used to understand the full daily practice ecosystem. What does a user's daily personal routine look like? Where does your product fit? What do they do before and after using the app? A diary study where users log their daily practices for 2 weeks would reveal contexts and needs the team cannot see from analytics alone.

**Interview Guide Template for Generative Research:**

```
OPENING (5 min)
"Thank you for speaking with me. I'm interested in understanding your daily
routine around [topic]. There are no right or wrong answers — I just want
to learn about your experience."

CONTEXT & BACKGROUND (10 min)
- "Walk me through a typical day for you."
- "Where does [activity] fit into your routine?"
- "How long have you been doing [activity] this way?"
- "What prompted you to start?"

DEEP DIVE ON BEHAVIOR (20 min)
- "Tell me about the most recent time you [specific action]."
- "What happened right before that? Right after?"
- "Walk me through exactly what you did, step by step."
- "What tools or resources did you use?"
- "What was the hardest part?"
- "What would have made it easier?"

NEEDS & ASPIRATIONS (10 min)
- "If you could wave a magic wand, what would change about [activity]?"
- "What have you tried that didn't work?"
- "What does 'success' look like for you with [activity]?"

WRAP-UP (5 min)
- "Is there anything I should have asked about that I missed?"
- "Who else do you know who does [activity] differently than you?"
- "Can I follow up if I have more questions?"
```

### Category 2: Evaluative Research

**Purpose:** Assess whether something works as intended. Test designs, prototypes, or existing features for usability, comprehension, and effectiveness.

**When to Use:**
- Before launching a new feature or redesign
- After noticing a drop in a specific flow's conversion
- Comparing design alternatives
- Validating that a fix actually fixes the problem

**Methods:**

| Method | Description | Best For | Sample | Duration |
|--------|-------------|----------|--------|----------|
| Usability testing | Task-based testing with think-aloud | Identifying friction and confusion | 5-8 per round | 1-2 weeks |
| A/B testing | Controlled experiment comparing variants | Measuring behavioral impact | Statistical significance | 1-4 weeks |
| Concept testing | Presenting ideas/mockups for reaction | Early validation before building | 8-12 | 1-2 weeks |
| Heuristic evaluation | Expert review against usability principles | Quick identification of obvious issues | 2-3 evaluators | 2-3 days |
| First-click testing | Where do users click first on a page? | Navigation and information architecture | 20-50 | 1-3 days |
| Preference testing | Which option do users prefer and why? | Choosing between design alternatives | 15-30 | 1-2 days |

**Key Principle: Five Users Find 85% of Usability Issues**

Jakob Nielsen's research shows that 5 users in a usability test will uncover approximately 85% of usability problems. Sirjani builds on this: it's better to run 3 rounds of 5 users (with fixes between rounds) than 1 round of 15 users.

**Usability Test Script Template:**

```
PRE-TASK BRIEFING
"I'm going to ask you to complete some tasks using [product]. I'm testing
the product, not you — there are no wrong answers. Please think aloud as
you go, telling me what you're looking at and what you're thinking."

TASK FORMAT
"Imagine you want to [goal]. Starting from this screen, show me how you
would do that."

OBSERVATION NOTES
- Did they complete the task? [Yes / No / Partial]
- Time to completion: [X minutes]
- Path taken: [Screen 1 → Screen 2 → ...]
- Errors made: [List]
- Confusion points: [Where they hesitated or expressed uncertainty]
- Verbatim quotes: ["..."]

POST-TASK QUESTIONS
- "On a scale of 1-7, how easy was that?"
- "What was the hardest part?"
- "What did you expect to happen when you tapped [element]?"
```

### Category 3: Descriptive Research

**Purpose:** Measure the current state. Quantify behaviors, establish baselines, understand distributions across segments.

**When to Use:**
- Establishing metrics baselines
- Sizing a problem or opportunity
- Understanding user segments
- Tracking satisfaction or sentiment over time

**Methods:**

| Method | Description | Best For | Sample | Duration |
|--------|-------------|----------|--------|----------|
| Surveys | Structured questionnaire | Quantifying attitudes, preferences, frequency | 200-500+ | 1-3 weeks |
| Analytics review | Analyzing behavioral data | Understanding what users do (not why) | All users | 1-2 weeks |
| Benchmarking | Comparing against industry standards | Contextualizing your metrics | N/A | 1 week |
| Card sorting | Users organize information into categories | Information architecture, taxonomy | 20-30 | 1-2 weeks |
| Tree testing | Users navigate a content hierarchy | Validating navigation structure | 30-50 | 1-2 weeks |

**Survey Design Principles:**

1. **Every question must serve the decision.** If a question result wouldn't change your action, cut it.
2. **Behavioral questions > Opinion questions.** "How many times did you engage this week?" beats "How important is engagement to you?"
3. **Specific > General.** "In the last 7 days, did you use the daily engagement feature?" beats "Do you use engagement session features?"
4. **Short > Long.** Target under 5 minutes. Every additional minute drops completion rate by 10-15%.
5. **Pilot test.** Always test with 5-10 people before full launch.

### Category 4: Causal Research

**Purpose:** Understand why something is happening. Establish cause-and-effect relationships between variables.

**When to Use:**
- A key metric changed and you need to know why
- You want to predict the impact of a change before making it
- You need to isolate the effect of one variable from others

**Methods:**

| Method | Description | Best For | Sample | Duration |
|--------|-------------|----------|--------|----------|
| Controlled experiments | A/B or multivariate tests | Measuring causal impact | Statistical significance | 2-8 weeks |
| Regression analysis | Statistical modeling of relationships | Understanding drivers of behavior | 1000+ data points | 1-2 weeks |
| Cohort analysis | Comparing groups over time | Understanding retention drivers | All users in cohorts | 1-2 weeks |
| Pre/post analysis | Measuring before and after a change | Assessing intervention impact | Affected users | Varies |

---

## Building Feedback Rivers

### The River Metaphor

Sirjani advocates for meeting people where they are rather than asking them to come to you. Feedback rivers are continuous streams of customer signal that flow into the product team without requiring active research projects. The key is to improve the quality and usefulness of feedback that already exists in the organization.

### Passive Feedback River Architecture

```
SUPPORT TICKETS ──────────┐
                          │
APP STORE REVIEWS ────────┤
                          │
SALES CALL NOTES ─────────┤     ┌─────────────────┐     ┌──────────────┐
                          ├────→│  FEEDBACK HUB    │────→│  WEEKLY      │
SOCIAL MEDIA ─────────────┤     │  (tagged,        │     │  DIGEST      │
                          │     │   categorized,   │     │  to product  │
NPS/CSAT RESPONSES ───────┤     │   searchable)    │     │  team        │
                          │     └─────────────────┘     └──────────────┘
IN-APP FEEDBACK ──────────┤
                          │
COMMUNITY FORUMS ─────────┘
```

### Setting Up Each River

**Support Ticket Mining:**
1. Work with the support team to add product-relevant tags to their taxonomy
2. Tags should include: feature area, user action, emotional tone, severity
3. Create a weekly digest of top themes for the product team
4. Quarterly: deep analysis of ticket volume trends by category

**App Store Review Monitoring:**
1. Set up automated monitoring (AppFollow, AppBot, or similar)
2. Tag reviews by: feature mentioned, sentiment, user segment (if identifiable)
3. Respond to negative reviews (customer recovery opportunity)
4. Monthly: theme analysis of new reviews

**In-App Feedback Prompts:**
1. Trigger at high-signal moments (not random)
2. Keep it short: 1 question maximum
3. Rotate questions on a monthly cycle
4. Best trigger points for your product:
   - After completing a 7-day streak
   - After a first-time purchase
   - After sharing content for the first time
   - When a user returns after 14+ days away

### The Customer Advisory Board

For your product, a structured advisory board creates the most reliable ongoing feedback channel:

**Structure:**
- 15-20 members, rotating 5 per quarter
- Segmented: 5 new users, 5 power users, 5 paid subscribers, 5 recently churned
- Monthly 30-minute group sessions (virtual)
- Quarterly individual check-ins

**Session Format:**
```
MONTH 1: Strategic Direction
  Show upcoming roadmap priorities, gather reactions
  "If you could only have one of these three features, which and why?"

MONTH 2: Experience Deep-Dive
  Pick one product area, walk through the experience together
  "Show me how you currently [task]. What works? What doesn't?"

MONTH 3: Open Forum
  User-driven agenda
  "What's on your mind about your product?"
```

---

## Method Selection Quick Reference

### By Decision Type

| I need to decide... | Start with... | Then validate with... |
|---------------------|--------------|---------------------|
| What to build | Generative interviews (12-20) | Concept testing (8-12) |
| How to build it | Usability testing (5-8 per round) | A/B test post-launch |
| Whether it's working | Analytics + churn interviews | Survey for scale |
| Why metrics changed | Analytics deep dive | Targeted interviews (5-8) |
| Whether to enter a new space | JTBD interviews (15-20) | Market sizing survey |
| How to price | Willingness-to-pay survey + interviews | A/B test |
| Whether to sunset a feature | Usage analytics | Interviews with users of the feature |

### By Confidence Required

```
LOW CONFIDENCE OK             HIGH CONFIDENCE NEEDED
(reversible decisions)        (irreversible decisions)

5 interviews                  15-20 interviews
Quick survey                  + Quantitative survey
Internal data review          + Behavioral analytics
1 week                        + Competitive analysis
                              4-6 weeks
```

### By Budget and Time

| Budget | <1 week | 1-2 weeks | 2-4 weeks | 4+ weeks |
|--------|---------|-----------|-----------|----------|
| $0 | Guerrilla testing, internal review | 5 interviews (personal network) | 10 interviews + desk research | Diary study with personal network |
| $500-2K | Online usability test (5-8) | Quick survey (200+) | Interview panel (12-15) | Mixed methods |
| $2-5K | Professional usability test | Survey + interviews | Full research sprint | Longitudinal study |
| $5K+ | Expert heuristic review + testing | Segmented research panels | Multi-method study | Ethnographic research |
