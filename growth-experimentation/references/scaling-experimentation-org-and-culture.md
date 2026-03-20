## Contents
- Source Context
- The Experiment Pipeline: Seven Stages
  - Stage 1: Ideation
  - Stage 2: Prioritization (ICE Framework)
  - Stage 3: Design
  - Stage 4: Build and Launch
  - Stage 5: Monitoring
  - Stage 6: Analysis
  - Stage 7: Learning Distribution
- The Experiment Portfolio
  - Portfolio Allocation
  - Why the Mix Matters
  - Quarterly Portfolio Review
  - Elena Verna's Growth Model Evolution
- Growth Team Structure
  - When to Build a Growth Team
  - Core Growth Pod Composition
  - Where Does Growth Sit?
- The Writer's Room Model
  - What It Is
  - Why It Works
  - How to Implement
- Hiring Growth Engineers
  - Three Essential Traits
  - Where to Find Them
  - Roles to Avoid Combining
- Building Experimentation Culture
  - The Five Cultural Behaviors
  - Healthy vs. Unhealthy Culture Signals
- Growth Team Operating Cadence
  - Weekly Rhythm
  - Monthly Cadence
  - Quarterly Cadence
- Growth Engineering Maturity Assessment
- your product Recommendations
  - Growth Team Structure
  - Growth Surfaces to Own
  - Tooling (Minimal Viable Stack)
  - Velocity Ramp
  - Operating Model

---
# Scaling Experimentation: Organization and Culture

## Source Context

This reference merges organizational frameworks from Fareed Mosavat's Mastering Experimentation course (experiment pipeline, culture, portfolio management), Elena Verna's PLG principles (growth model evolution, exploration allocation), and Alexey Komissarouk's Mastering Growth Engineering course (team structure, Writer's Room model, hiring, maturity assessment). It covers everything required to build and scale an experimentation function from the first experiment to a company-wide culture.

---

## The Experiment Pipeline: Seven Stages

### Stage 1: Ideation

**Goal:** Generate a high volume of diverse hypotheses from across the organization.

**Process:**
- Open the ideation funnel to everyone: product, engineering, design, marketing, customer support, sales
- Provide a simple intake form:
  - What is the hypothesis? (Structured: "We believe [change] will cause [effect] because [reason]")
  - What metric would this move?
  - How does it connect to current strategic priorities?
  - Estimated effort (T-shirt size: S/M/L)
- Review submissions weekly -- do not let ideas languish without feedback

**Common failure modes:**
- Only the growth team submits ideas (missing perspectives from people who talk to users daily)
- No intake form (ideas scattered across Slack, email, and meetings)
- No feedback loop (people stop submitting because they never hear what happened)

**Metrics:** Ideas submitted per week (target: 5-10 from across org). Percentage from outside the growth team (target: 40%+).

### Stage 2: Prioritization (ICE Framework)

Score each idea on three dimensions (1-10 scale):

- **Impact:** If this succeeds, how much will the target metric improve?
  - 1-3: Marginal (<5%)
  - 4-6: Meaningful (5-15%)
  - 7-10: Significant (>15%)

- **Confidence:** How confident is the team in the expected result?
  - 1-3: Speculative (intuition or analogy)
  - 4-6: Informed (qualitative data or benchmarks)
  - 7-10: Evidence-based (prior experiments or quantitative analysis)

- **Ease:** How easy to design, build, and run?
  - 1-3: Complex (multiple sprints, cross-team)
  - 4-6: Moderate (one sprint, standard tooling)
  - 7-10: Simple (days, existing tools)

**Composite score:** Impact x Confidence x Ease (max 1000).

**Strategic filter:** Before scoring, apply a strategic filter. Ideas not connected to a current strategic question go to a backlog regardless of ICE score. This prevents high-scoring but strategically irrelevant experiments from consuming capacity.

**Cadence:** Weekly. The growth team reviews the backlog, adjusts scores, and selects the next 2-4 experiments to move into design.

### Stage 3: Design

Create a detailed experiment plan using the Experiment Design Canvas (see SKILL.md Module 2). Peer review every design before launch. The reviewer checks for clear hypothesis, appropriate metric, adequate sample size, relevant guardrails, and pre-defined decision criteria.

### Stage 4: Build and Launch

**Pre-launch checklist:**
- [ ] Feature flags set correctly
- [ ] Tracking events fire as expected (verified in staging)
- [ ] Control and treatment groups properly randomized
- [ ] Guardrail metric tracking in place
- [ ] Launch and end dates documented
- [ ] Team notified

**Common build mistakes:**
- Logging bugs that corrupt data (discovered only at analysis)
- Incorrect targeting (wrong user segment)
- Missing guardrail tracking
- Treatment leaking to control (feature flags not properly isolated)

### Stage 5: Monitoring

**What to monitor:** Is traffic splitting correctly? Are all events firing? Any data anomalies? Are guardrails stable?

**What NOT to do:** Do not check primary metric results before the end date. Do not adjust the experiment based on early results. Do not extend because results "almost" reached significance.

### Stage 6: Analysis

**Analysis checklist:**
- [ ] Verify data quality (sample sizes match expectations, no logging gaps)
- [ ] Check for Sample Ratio Mismatch (SRM)
- [ ] Analyze primary metric against hypothesis
- [ ] Check statistical significance or directional confidence
- [ ] Analyze guardrail metrics
- [ ] Segment analysis (pre-defined segments only)
- [ ] Document anomalies or unexpected findings

**Results classification:**
- **Significant win:** Treatment outperforms control, guardrails intact
- **Significant loss:** Control outperforms treatment
- **Inconclusive:** Effect within noise range
- **Mixed:** Primary improves but guardrail degrades

### Stage 7: Learning Distribution

**Write-up template:**
```
Experiment: [Name]
Date: [Start - End]
Owner: [Name]
Status: [Win / Loss / Inconclusive / Mixed]

Summary (2-3 sentences):
What did we test? What happened? What did we learn?

Results:
- Primary metric: [Result with confidence interval]
- Guardrail 1: [Result]
- Guardrail 2: [Result]

Key Learning:
[1-2 paragraphs on what this tells us about users, product, or strategy]

What Is Next:
[Based on this learning, what should we test next?]
```

**Distribution channels:**
- Experiment repository (searchable Notion or Confluence database)
- Weekly experiment review (15-30 minutes, open to the company)
- Monthly learning digest (email summary of top learnings)
- Quarterly strategy update (how cumulative learnings shifted strategy)

---

## The Experiment Portfolio

### Portfolio Allocation

| Category | % of Experiments | Expected Lift | Win Rate | Time to Result |
|----------|-----------------|---------------|----------|----------------|
| Quick optimizations | 50-60% | 1-5% | 30-40% | 1-2 weeks |
| Medium bets | 25-35% | 5-20% | 15-25% | 2-4 weeks |
| Big bets | 10-20% | 20-100%+ | 5-15% | 4-12 weeks |

### Why the Mix Matters

**100% optimizations:** Steady small wins but never step-function growth. Over time, the optimization ceiling is reached on every surface and the program stalls.

**100% big bets:** Frequent failures erode morale and organizational trust. Without quick wins to sustain momentum, the program loses support.

**Balanced portfolio:** Quick wins maintain trust. Medium bets produce meaningful improvements. Big bets create the possibility of step-function growth.

### Quarterly Portfolio Review

1. What percentage of experiments fell into each category?
2. What was the total value generated by each category?
3. Has the team drifted toward 100% optimizations? (Most common failure)
4. Are there strategic questions requiring big bets that are not being addressed?
5. What new surfaces or growth loops should enter the portfolio?

### Elena Verna's Growth Model Evolution

Verna argues growth models should evolve every 18 months. Teams that rely on the same loops too long become vulnerable when channels shift or competitors enter.

**The 20-25% Exploration Rule:** Allocate 20-25% of growth resources to exploring new growth loops, even when existing loops perform well. Without a dedicated allocation, exploration loses to optimization every time.

**Signs the model needs evolution:**
- Primary acquisition channel becoming more expensive or saturated
- Retention curves plateaued despite optimization
- A new competitor growing faster with a different model
- Product expanding into segments the current model does not serve
- Technological or market shifts creating new possibilities

---

## Growth Team Structure

### When to Build a Growth Team

Komissarouk is emphatic about timing: do not build a growth team before product-market fit.

**Pre-PMF: No Growth Team**
- All engineering effort goes to core product
- "Growth" means talking to customers and iterating
- Premature growth optimization is a distraction from the existential question

**Post-PMF, Pre-$5M ARR: Light Touch**
- One product engineer at 20% on growth experiments
- Off-the-shelf tools (Statsig, Amplitude, Braze)
- Focus on obvious levers: onboarding, activation, basic notifications
- Squeeze value from existing tools before custom solutions

**Post-$5M ARR: Dedicated Growth Engineering**
- First dedicated growth engineer
- Formal experimentation process
- Begin investing in infrastructure
- Growth roadmap alongside product roadmap

**100K+ MAU: Growth Engineering Team**
- 2-5 growth engineers
- Dedicated growth PM and data analyst
- Custom experimentation infrastructure
- Own key surfaces (onboarding, paywall, notifications, referral)

### Core Growth Pod Composition

**Growth Product Manager (1)** -- Owns growth strategy and roadmap. Defines hypotheses and success criteria. Prioritizes experiment backlog. Communicates results to stakeholders.

**Growth Engineers (2-3)** -- Build and ship experiments rapidly. Maintain experimentation infrastructure. Clean up experiment code. Build reusable growth components.

**Data Analyst (1)** -- Designs experiment analysis frameworks. Monitors results and guardrails. Identifies opportunities through data exploration. Maintains dashboards.

**Growth Designer (0.5-1)** -- Designs experiment variants. Creates reusable design patterns. Ensures brand consistency. Often shared with product design.

### Where Does Growth Sit?

**Option 1: Standalone team (recommended for most)**
Growth team reports independently with dotted lines to Product, Engineering, and Marketing. Pros: clear ownership, dedicated resources. Cons: risk of siloing.

**Option 2: Within Product**
Tight integration with product roadmap. Risk: growth work deprioritized for feature development.

**Option 3: Within Marketing**
Natural lifecycle messaging ownership. Risk: engineers feel misplaced; growth becomes "marketing automation."

---

## The Writer's Room Model

### What It Is

Komissarouk advocates a "Writer's Room-style culture" for growth teams. In a TV writers' room, everyone contributes ideas regardless of title. The best idea wins, not the most senior person's.

**Traditional model (PM-led):**
PM generates ideas -> PM prioritizes -> Engineers execute -> Analysts measure. Engineers are implementers who build what they are told.

**Writer's Room model (collaborative):**
Everyone generates ideas -> Team collaboratively prioritizes -> Engineers execute with context -> Everyone analyzes and learns. Engineers, analysts, designers, and PMs all contribute to ideation.

### Why It Works

1. **Better ideas**: Engineers see technical opportunities PMs miss. Analysts see data patterns no one else notices. Designers understand user behavior from a different angle.
2. **Higher motivation**: Engineers who understand why they are building something are more creative and committed.
3. **Faster iteration**: When engineers understand the hypothesis, they make better scoping decisions and suggest simpler implementations.
4. **Knowledge compounding**: When the whole team learns from every experiment, institutional knowledge grows faster.

### How to Implement

**Step 1: Share Context** -- Educate the team on core metrics, customer data, strategy, competitive landscape, and previous learnings.

**Step 2: Structured Brainstorming** -- Bi-weekly sessions where everyone brings 2-3 experiment ideas. Brief discussion (2-3 minutes each). No idea dismissed without discussion.

**Step 3: Collaborative Prioritization** -- Round 1: everyone scores by ICE. Round 2: deeper analysis on top ideas (dollar-value impact, engineering complexity, dependencies). This dual-step process uncovers counterintuitive wins.

**Step 4: Transparent Results** -- Share wins and losses. Discuss what was learned, not just what happened. Celebrate learning, not just winning.

---

## Hiring Growth Engineers

### Three Essential Traits

**1. Speed and Adaptability** -- Comfortable shipping imperfect code, making deliberate quality tradeoffs, context-switching between experiments.
Interview signal: Ask about shipping something quickly. How did they decide what to cut?

**2. Business Acumen** -- Fluent in CAC, LTV, ARPU, retention curves, contribution margins. Can explain the business impact of their work.
Interview signal: Can they walk through unit economics of a subscription business?

**3. Statistical Rigor** -- Understand A/B testing deeply enough to avoid peeking, underpowered tests, multiple testing.
Interview signal: "You are running an A/B test. After 3 days of a planned 14, the treatment is winning with p=0.03. What do you do?" Right answer: wait.

### Where to Find Them

- **Convert internal product engineers** who are curious about metrics and enjoy shipping fast
- **Hire from growth-oriented companies** (Airbnb, Pinterest, Uber, Bumble)
- **Hire from analytics backgrounds** -- data analysts who want to move into engineering

### Roles to Avoid Combining

- Growth engineer + infrastructure engineer (context-switching destroys velocity)
- Growth engineer + on-call SRE (interrupts kill experiment velocity)
- Growth PM + product PM (different time horizons, metrics, stakeholders)

---

## Building Experimentation Culture

### The Five Cultural Behaviors

**1. Celebrate learnings, not wins**
- Lead weekly reviews with "What did we learn?" not "Did we win?"
- Recognize experiments that produced surprising negative results
- Reframe: "the hypothesis was not supported" instead of "failed"

**2. Share broadly and frequently**
- Default to transparency (protect only competitive intelligence and pricing)
- Multiple formats: written, verbal (standup), visual (dashboard)

**3. Make it safe to be wrong**
- Evaluate experimenters on process quality and learning output, not win rate
- Leaders model humility: publicly share their own wrong predictions

**4. Connect every experiment to strategy**
- Post strategic questions prominently and reference them in every design
- Reward experiments that change strategic thinking, even if negative

**5. Kill things quickly and move on**
- Define maximum durations upfront
- Sunk cost fallacy is the enemy

### Healthy vs. Unhealthy Culture Signals

| Signal | Healthy | Unhealthy |
|--------|---------|-----------|
| Idea sources | Across the company | Only growth team |
| Failure response | "What did we learn?" | "Who approved this?" |
| Win rate | 15-30% | 70%+ (testing safe things) |
| Documentation | Every experiment has a write-up | Results in Slack messages |
| Leadership | Attend reviews, ask about learnings | Only care about metric lifts |
| Duration | Predetermined and respected | Extended hoping for significance |

---

## Growth Team Operating Cadence

### Weekly Rhythm

**Monday: Sprint Planning** -- Review previous week's results. Update backlog. Assign experiments. Set priorities.

**Wednesday: Mid-Week Sync** -- Check experiment health. Review guardrails. Unblock technical issues. No conclusions from partial data.

**Friday: Results and Learning** -- Analyze completed experiments. Document in learnings database. Share insights broadly.

### Monthly Cadence

Review the month's results (wins, losses, learnings). Assess progress against quarterly goals. Review metric trends. Reprioritize backlog. Present to leadership.

### Quarterly Cadence

Set quarterly growth OKRs. Define strategic themes (e.g., "Q1: onboarding; Q2: retention mechanics"). Allocate resources. Review infrastructure needs. Align with product and marketing plans.

---

## Growth Engineering Maturity Assessment

| Dimension | Level 1 (Ad Hoc) | Level 2 (Systematic) | Level 3 (Rigorous) | Level 4 (Cultural) |
|-----------|------------------|---------------------|--------------------|--------------------|
| Experimentation | Occasional, informal | Regular cadence, documented | Statistically enforced | Default for all decisions |
| Analytics | Basic, gaps | Comprehensive | Real-time, automated | Self-serve for all teams |
| Team | No dedicated growth | Growth pod | Full growth team | Growth mindset across org |
| Velocity | <1/month | 1-2/week | 3-4/week | Continuous, parallel |
| Infrastructure | Off-the-shelf only | Some custom tooling | Reusable library | Server-driven, automated |
| Culture | Growth = marketing | Growth = team job | Growth = discipline | Growth = company DNA |

Score each dimension 1-4. Total: /24.
- 6-10: Getting started. Focus on foundations (tracking, first experiments).
- 11-15: Building momentum. Invest in infrastructure and team.
- 16-20: Strong capability. Optimize velocity and culture.
- 21-24: Elite. Focus on compounding and AI-augmented experimentation.

---

## your product Recommendations

### Growth Team Structure

```
Growth Team (reporting to Head of Product or CEO)
+-- Growth PM (1) -- strategy, backlog, stakeholder communication
+-- Growth Engineers (2) -- experiments, infrastructure, cleanup
+-- Growth Analyst (1) -- analysis, dashboards, opportunity identification
+-- (Shared) Growth Designer (0.5) -- variant design, growth surface UX
```

### Growth Surfaces to Own
1. Onboarding flow (install to first engagement session completion)
2. Paywall and subscription conversion
3. Notification and lifecycle messaging
4. Sharing and referral mechanics
5. Retention mechanics (streaks, personalization, recommendations)

### Tooling (Minimal Viable Stack)
1. Idea intake: Notion form feeding a database
2. Prioritization board: Notion with columns (Backlog, Prioritized, In Design, Running, Analyzing, Learning Shared)
3. Feature flags: Statsig or Firebase Remote Config
4. Analysis: Amplitude or Statsig experiment analysis
5. Learning repository: Searchable Notion database by date, surface, strategic question, result

### Velocity Ramp
- Month 1-3: 2-3 experiments per month (build system and muscle)
- Month 4-6: 4-6 per month (system working, increase throughput)
- Month 7+: 6-10 per month (mature system, parallel streams)

### Operating Model
- Writer's Room brainstorming every 2 weeks
- Target: 2-3 experiments launched per week at maturity
- Monthly growth review with leadership
- Quarterly strategy and OKR setting
- 20-30% of engineering time allocated to cleanup and infrastructure
