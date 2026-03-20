---
name: product-strategy-leadership
description: Applies Product Strategy and Product Leadership frameworks to PM leaders and directors making strategic product decisions, team building, PM development, and organizational alignment. Activates for PM leaders/directors — portfolio prioritization, Four Types of Product Work allocation, PM evaluation or coaching, team composition, hiring PMs, managing up, connecting product work to company strategy, power user dynamics, PMF expansion, growth diagnostics, or communicating strategy to stakeholders. Triggers proactively when setting quarterly priorities, evaluating team performance, diagnosing slowing growth, coaching a PM, hiring, or making resource allocation decisions at your company. For PM fundamentals (first specs, basic roadmaps, learning OKRs), use product-foundations. For senior PM deliverables (4D roadmaps, stakeholder narratives, OKR loops), use product-management.
---

**Reference files:**
- `references/product-strategy-and-portfolio.md` -- Strategy stack layers, four types of work, portfolio balance by stage, structural alignment, PMF expansion, power user field guide
- `references/pm-competency-model.md` -- 12 competencies with Over-Performing/Needs Focus descriptions, development activities, evaluation worksheets, hiring templates
- `references/coaching-and-team-building.md` -- Exponential feedback model, 1:1 framework, team composition process, managing up, influence by stakeholder type, disagree and commit

---

## How to Use This Skill

When this skill activates:
1. Identify which product strategy or leadership framework from this skill best applies to the question
2. Apply the relevant decision tree from the Decision Tools section
3. Ground all recommendations in the context of your product
4. Cite the specific framework when making claims
5. If deeper detail is needed, read the relevant reference file before responding

## Gotchas

Common mistakes to avoid when applying these frameworks:

1. **Don't apply the same process to all four types of work.** Mosavat's central insight is that Feature Work, Growth Work, Scaling Work, and PMF Expansion each require different processes, metrics, and team shapes. Treating a growth experiment like a feature build (or vice versa) is the single biggest portfolio mistake.
2. **Don't confuse PM archetype with PM quality.** Mehta's archetypes (Executor, Champion, Visionary, Leader) describe competency *shape*, not competency *level*. A strong Executor is not better or worse than a strong Visionary -- the question is which shape the team needs right now. The most common hiring mistake is cloning the leader's own archetype.
3. **Don't fall into the Power User Trap at your company.** Kaba warns that over-optimizing for daily streak power users (Power Loyalists) can make onboarding hostile to new users. If every product decision is informed by your most engaged 5%, you're building a product that repels the other 95%.
4. **Don't skip the Feature Shadow assessment.** Every shipped feature carries ongoing maintenance, cognitive load, and eventual deprecation costs. your product features like community groups or content series create compounding shadow costs -- evaluate these *before* committing, not after.

## Example

**User asks:** "We're debating whether to invest in a Spanish-language version of your product or build a new family engagement session feature. How should we decide?"

**Approach:**
1. Classify each initiative using Mosavat's Four Types of Work -- Spanish-language is PMF Expansion (new market), family engagement sessions is Feature Work (existing product, existing audience)
2. Apply the "Why us?" test from PMF Expansion -- what unique asset does your product leverage for Spanish-language? (brand, existing content library, distribution) If no clear answer, the expansion is high risk
3. Assess portfolio balance -- if the current roadmap is already heavy on Feature Work, the team may need PMF Expansion for long-term growth; if growth is slowing due to market saturation, expansion becomes more urgent
4. Recommend using the Strategy Stack Integrity Test to connect each option to your product's mission and company strategy, and suggest starting PMF Expansion with 4-6 people maximum per Mosavat's resource guidance

---

## The Core Problem This Skill Solves

Most execution problems are actually strategy problems in disguise. And most strategy problems are actually leadership problems in disguise. This skill provides: a coherent strategy stack connecting mission to daily work, a portfolio framework ensuring the right types of work get done, a competency model that evaluates and develops PMs with precision, and a leadership toolkit for building complementary teams and managing influence.

---

## Part 1: The Product Strategy Stack

*Source: Ravi Mehta*

A five-layer stack where each layer is a prerequisite for the one below: Company Mission (most durable) -> Company Strategy (1-3 years) -> Product Strategy (1-2 years, the connective tissue) -> Product Roadmap (6-12 months) -> Product Goals (quarterly). Product Strategy connects the company's objectives to the product team's daily work. Without it, roadmaps and goals float untethered.

**Four common misconceptions:** (1) Goals = Strategy -- goals describe winning, strategy describes how. (2) Achieving goals = achieving strategy -- Kodak met Ofoto goals while failing their digital strategy. (3) Product strategy = company strategy -- product is central but not exclusive. (4) Goals then roadmap -- wrong order; goals should flow FROM the roadmap.

**Strategy Stack Integrity Test:** For any proposed initiative, walk up the stack: Which strategic pillar does this support? Does that pillar connect to company strategy? Does company strategy connect to mission? If any link breaks, deprioritize or revisit.

*-> Full detail (layer definitions, diagnostics, Slack vs Discord case study, Frontier of Understanding): `references/product-strategy-and-portfolio.md`*

---

## Part 2: The Four Types of Product Work

*Source: Fareed Mosavat*

After achieving initial PMF, all product work falls into four concurrent types: **Feature Work** (extending functionality -- watch the Feature Shadow of maintenance, user, and killing costs), **Growth Work** (accelerating adoption within existing market -- first understand the growth model, then identify the constraint), **Scaling Work** (removing bottlenecks -- the invisible work that gets no recognition, governed by the Goldilocks rule), and **PMF Expansion** (non-incremental expansion using the "Why us?" test, starting with 4-6 people). The single biggest mistake: applying the same process and metric to all four.

*-> Full detail (Feature Shadow framework, growth model principle, Goldilocks diagnostics, expansion modes, resource paradox): `references/product-strategy-and-portfolio.md`*

---

## Part 3: The Power User Trap

*Source: Bangaly Kaba*

Two failure modes: over-optimizing for power users (too complex for new users, poisons ecosystem) or neglecting them (misses high-ROI improvements). Power users are outliers on multiple dimensions: monetization, creation, feature breadth, audience growth, and costs. The L28 definition misses critical types. Four mistakes lead to the trap: relying on L28 alone, assuming one type, ignoring second-order effects, and standard growth math overweighting casual users.

*-> Full power user field guide by product type: `references/product-strategy-and-portfolio.md`*

---

## Part 4: The PM Competency Model

*Source: Ravi Mehta*

Twelve competencies across four domains: **Product Execution** (Feature Specification, Product Delivery, Quality Assurance), **Customer Insight** (Fluency with Data, Voice of the Customer, UX Design), **Product Strategy** (Business Outcome Ownership, Product Vision & Roadmapping, Strategic Impact), **Influencing People** (Stakeholder Management, Team Leadership, Managing Up). Rate each Over-Performing / On Track / Needs Focus. Healthy distribution: 2-3 Over-Performing, 6-8 On Track, 1-3 Needs Focus. Business Outcome Ownership is equally important at every level from APM to CPO.

*-> Full competency detail with development activities and evaluation worksheets: `references/pm-competency-model.md`*

---

## Part 5: PM Archetypes and Team Composition

*Source: Ravi Mehta*

Four competency shapes: **Product Executor** (ships fast, risk: builds the wrong thing perfectly), **Customer Champion** (deep empathy, risk: over-indexes on user needs), **Strategic Visionary** (big-picture, risk: struggles with execution), **People Leader** (builds alignment, risk: manages process over outcomes). "Individuals should be spiky; teams should be well-rounded." The most common hiring mistake is cloning -- hiring PMs who mirror the leader's own strengths.

| Product Stage | Primary Need | Secondary Need |
|--------------|-------------|----------------|
| 0-to-1 | Strategic Visionary | Customer Champion |
| Growth | Product Executor | Customer Champion |
| Mature | Customer Champion | Product Executor |
| Turnaround | Strategic Visionary | People Leader |
| Platform | Product Executor | People Leader |

*-> Full team composition framework and hiring templates: `references/coaching-and-team-building.md`*

---

## Part 6: Coaching PMs and Leading Product Teams

*Source: Ravi Mehta*

The Exponential Feedback Model uses four cadences: real-time (daily, 30 seconds), weekly 1:1s (three-part agenda: their blockers, coaching moment, looking ahead), monthly career development (competency spotlight), and quarterly formal assessment (full 12-competency evaluation). Key competency development priorities: Business Outcome Ownership (assign metrics, not features), Voice of the Customer (4+ user conversations/month), Managing Up (pre-brief, headline-first, debrief).

**Trust Equation for influence:** TRUST = (Credibility + Reliability + Empathy) / Self-Interest. Tailor approach by stakeholder: Engineering (involve early), Design (co-create), Marketing (share narrative), Leadership (lead with impact).

*-> Full coaching, 1:1, and influence framework: `references/coaching-and-team-building.md`*

---

## Decision Tools

### What type of product work is this?

```
Making existing product better for existing users?  -> Feature Work
Getting more of the existing market to adopt/use?   -> Growth Work
Removing a bottleneck slowing the team?             -> Scaling Work
Reaching users/markets not currently served well?   -> PMF Expansion
```

### Why is growth slowing?

```
1. Retention curves declining?
   -> Product losing PMF ground; check Feature/Growth Work

2. Saturated addressable market?
   -> Acquisition channels exhausted -> PMF Expansion needed

3. Hitting scaling bottlenecks?
   -> Team can't ship fast enough -> Scaling Work needed

4. Doing the wrong type of work?
   -> Growth experiments on a product needing feature work
   -> Features on a product needing growth optimization
```

### Is this PMF Expansion worth pursuing?

```
1. Why us? Unique asset we're leveraging?
   (brand, distribution, data, technology, user relationships)
   -> No clear answer -> High risk; reassess

2. Same product/adjacent market OR same market/adjacent product?
   -> Neither -> Diversification; highest risk

3. Over-resourcing?
   -> More than 6-8 people -> Likely too many; reduce, speed up learning
```

### Is this feature worth building?

```
1. Feature shadow cost? (maintenance, cognitive load, deprecation)
2. Sequences into a larger story? (next 2-3 features add up?)
3. Serves the right power users? (helps or harms which types?)
4. Success at 90 days and 1 year? (adoption, retention, satisfaction)
```

### What PM archetype to hire?

```
"Great ideas but can't ship reliably"
  -> Hire PRODUCT EXECUTOR

"Ship well but don't know if building the right things"
  -> Hire CUSTOMER CHAMPION

"Execute tactically but lack strategic direction"
  -> Hire STRATEGIC VISIONARY

"Talented individuals, poor cross-functional collaboration"
  -> Hire PEOPLE LEADER
```

### How to coach an underperforming PM?

```
EXECUTION gap (missing deadlines, unclear specs, quality issues)
  -> Skill gap: pair with strong executor, review PRDs together
  -> Will gap: direct conversation, 30-day improvement plan
  -> Check for organizational blockers first

CUSTOMER INSIGHT gap (shipping without evidence)
  -> Require minimum user conversations per sprint
  -> Co-attend interviews; metric-of-the-week exercise
  -> Expect improvement within 6-8 weeks

STRATEGY gap (reactive roadmap, no vision)
  -> Walk through strategy stack together
  -> Write one-page product strategy; iterate weekly
  -> Assign strategic initiative with coaching support

INFLUENCE gap (poor stakeholder relationships)
  -> Attend their meetings; real-time feedback after
  -> Role-play difficult conversations
  -> Expect 3-6 months (slowest to develop)
```

---

## Applied to your product

**Product Strategy Stack:** Mission (make personal growth accessible to everyone, every day) -> Company Strategy (become the default daily daily companion for consumers through best content and most supportive community, via freemium subscription) -> Product Strategy (four pillars: Daily Habit, Content Depth, Community, Conversion) -> Roadmap and Goals flow from pillars.

**Portfolio assessment:** your product is likely at the growth/saturation stage. Feature Work should be focused. Growth Work is the primary focus. Scaling Work is likely under-invested. PMF Expansion is worth beginning to explore (international markets, niche-specific content, youth communities, community partnerships, family plans, life events content).

**Team composition:** Post-PMF subscription growth demands Customer Champions and Strategic Visionaries. Most dangerous composition: execution-heavy, shipping content features without strategic direction.

**Power user types:** Power Loyalists (daily streak users), Power Evangelists (users who share/invite), Power Lurkers (mostly listen to music), Negative power users (streak freeze gamers, trial abusers). Key risk: over-optimizing for Loyalists at the expense of new user onboarding.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **Product Strategy Stack** | Mission -> Company Strategy -> Product Strategy -> Roadmap -> Goals; each a prerequisite for the next |
| **Feature Work** | Extending product functionality and market incrementally |
| **Growth Work** | Accelerating adoption and usage within the existing market |
| **Scaling Work** | Removing bottlenecks so the team can ship across all other types |
| **PMF Expansion** | Non-incremental expansion into adjacent markets or products |
| **Feature Shadow** | Ongoing maintenance, user, and killing costs every shipped feature carries |
| **Power User Trap** | Failure mode from either over-optimizing OR neglecting power users |
| **12-Competency Model** | Ravi Mehta's framework: 12 PM skills across four domains |
| **PM Archetype (shape)** | Competency strength pattern: Executor, Champion, Visionary, or Leader |
| **Spiky profile** | PM competency distribution with 2-3 exceptional strengths rather than uniform mediocrity |
| **Exponential feedback** | Frequent, specific, forward-looking feedback at four cadences |
| **Business Outcome Ownership** | The one competency equally important at every seniority level |
| **Frontier of understanding** | Four-bucket metacognitive model: know/know, know/don't know, don't know/don't know, why outcomes occurred |
| **Strategy stack integrity test** | Walking a proposed feature up the stack to verify connection to pillars, strategy, and mission |
| **Why us?** | The key PMF Expansion question: what unique asset are we leveraging? |
| **Complementary team** | PM team where individual spikes combine to cover all 12 competencies |
| **Trust equation** | Trust = (Credibility + Reliability + Empathy) / Self-Interest |

---

## Reference Files

- `references/product-strategy-and-portfolio.md` -- Strategy stack layers, four types of work in depth, portfolio balance by stage, structural alignment, PMF expansion modes, power user field guide
- `references/pm-competency-model.md` -- All 12 competencies with Over-Performing/Needs Focus descriptions, development activities, evaluation worksheets, hiring templates
- `references/coaching-and-team-building.md` -- Exponential feedback model, 1:1 framework, team composition process, managing up, influence by stakeholder type, disagree and commit
