## Contents
- Source Context
- The Case for Rigorous Experimentation
- A/B Testing: The Complete Framework
  - Step 1: Formulate a Hypothesis
  - Step 2: Design the Experiment
  - Step 3: Calculate Sample Size and Duration
  - Step 4: Launch and Monitor
  - Step 5: Analyze Results
- Statistical Pitfalls: Deep Dive
  - Pitfall 1: Peeking
  - Pitfall 2: Underpowered Tests
  - Pitfall 3: Multiple Testing
  - Pitfall 4: Simpson's Paradox / Segment Effects
  - Pitfall 5: Novelty and Primacy Effects
  - Pitfall 6: Survivorship Bias
- Pre/Post Analysis for Low-Traffic Surfaces
- Good vs. Bad Experiments: Diagnostic Framework
  - Mosavat's Seven Dimensions of Experiment Quality
  - Common Bad Experiment Archetypes
- Building Experimentation Infrastructure
  - Choosing a Platform
  - Minimum Viable Experimentation Stack
- Experiment Templates for your product
  - Template 1: Onboarding Experiment
  - Template 2: Paywall Timing Experiment
  - Template 3: Notification Timing Experiment

---
# Experiment Design and Statistical Rigor

## Source Context

This reference merges experiment design frameworks from Fareed Mosavat's Mastering Experimentation course, Elena Verna's PLG experimentation principles, and Alexey Komissarouk's Mastering Growth Engineering course. It covers the complete lifecycle of experiment design, from hypothesis formation through statistical analysis, with deep dives on the pitfalls that invalidate results.

---

## The Case for Rigorous Experimentation

Komissarouk shares a cautionary example: a company saw its key activation metric fall 3x over a year despite having a dedicated optimization team running experiments continuously. The root cause: the team was not monitoring metrics closely, lacked proper A/B testing protocols, and was shipping changes they believed were "wins" based on flawed analysis. They were making the product worse while celebrating false victories.

This failure mode is extremely common. The appearance of experimentation (running tests, looking at data, shipping "winners") creates an illusion of rigor that masks fundamental statistical errors.

---

## A/B Testing: The Complete Framework

### Step 1: Formulate a Hypothesis

Every experiment starts with a clear, testable hypothesis:

```
We believe that [specific change]
will cause [specific metric] to [improve/decrease] by [estimated amount]
for [specific user segment]
because [reasoning based on data, user research, or prior experiments]
```

**Good hypothesis example:**
"We believe that adding a personalized engagement session recommendation to the home screen will increase Day 1 engagement session completion rate by 15% because users currently face a cold start problem -- they see a generic list and do not know where to begin."

**Bad hypothesis example:**
"We believe the new home screen will increase engagement." (Vague change, vague metric, no reasoning, no estimate.)

The "because" clause is the most important part. It reveals the team's mental model of the user, which is what the experiment is actually testing. Without it, a positive result teaches nothing about why users responded, and a negative result provides no direction for iteration.

### Step 2: Design the Experiment

**Define the groups:**
- **Control**: The existing experience (no change)
- **Treatment**: The new experience (one change only; do not bundle multiple changes)
- **Randomization**: Users are randomly assigned to control or treatment. Randomization must be consistent (a user stays in the same group for the duration) and unbiased

**Define the metrics:**
- **Primary metric**: The one metric the hypothesis targets. The experiment is judged on this metric alone.
- **Secondary metrics**: Other metrics monitored for additional insight but not used to declare a winner.
- **Guardrail metrics**: Metrics that must NOT degrade. Examples: crash rate, support ticket volume, overall revenue, retention rate. If a guardrail degrades, the experiment is a failure regardless of primary metric improvement.

**Define the statistical criteria:**
- **Minimum Detectable Effect (MDE)**: The smallest improvement you care about. If a 1% improvement is not actionable, set MDE higher (e.g., 5%).
- **Significance level (alpha)**: Typically 0.05 (5% chance of false positive). For high-stakes tests, use 0.01.
- **Power (1-beta)**: Typically 0.80 (80% chance of detecting a real effect). For important tests, use 0.90.
- **Sample size**: Calculated from MDE, alpha, power, and baseline conversion rate.

### Step 3: Calculate Sample Size and Duration

**Sample size formula (simplified for conversion rate tests):**
```
n per group = (Z_alpha + Z_beta)^2 x 2 x p(1-p) / (MDE)^2

Where:
p = baseline conversion rate
MDE = minimum detectable effect (absolute difference)
Z_alpha = 1.96 for 95% confidence
Z_beta = 0.84 for 80% power
```

**Example calculation:**
```
Baseline trial-to-paid conversion: 10% (p = 0.10)
MDE: 2 percentage points (from 10% to 12%)
n per group = (1.96 + 0.84)^2 x 2 x 0.10 x 0.90 / (0.02)^2
n per group = 7.84 x 0.18 / 0.0004
n per group = 3,528

Total users needed: ~7,056 across both groups
If 500 new trials per day: ~14 days to run
```

**Duration considerations:**
- Minimum 7 days (to capture day-of-week effects)
- Ideally 14-28 days (to capture weekly cycles and avoid novelty effects)
- Maximum 60 days (beyond this, too many confounding variables accumulate)
- Never shorter than 2 full conversion cycles
- Always run in full 7-day multiples for products with weekly usage patterns

### Step 4: Launch and Monitor

**During the experiment:**
- Monitor for technical errors (is the experiment running correctly? are both groups getting the right experience?)
- Check guardrail metrics daily (are crash rates or error rates spiking?)
- Do NOT check primary metric results until the pre-determined end date
- Document any external events that may confound results (holiday, outage, PR event, marketing campaign)

### Step 5: Analyze Results

**After the experiment reaches its pre-determined end point:**

1. Check for data quality issues (sample ratio mismatch between groups, tracking errors)
2. Calculate the observed difference in primary metric
3. Calculate the p-value and confidence interval
4. Check if the result is statistically significant (p < alpha)
5. Check if the result is practically significant (is the improvement large enough to matter?)
6. Review guardrail metrics
7. Segment results by pre-defined dimensions (platform, user age, subscription status)
8. Document the result and share with the team

**Decision framework:**
```
Is the primary metric improvement statistically significant (p < 0.05)?
+-- YES --> Is it also practically significant (above MDE)?
|   +-- YES --> Are all guardrails clean?
|   |   +-- YES --> Ship the treatment. Productionize the code.
|   |   +-- NO --> Investigate guardrail degradation. May need to iterate.
|   +-- NO --> Stat sig but small effect. Consider if worth code maintenance.
+-- NO --> Is the confidence interval entirely below zero (clearly worse)?
    +-- YES --> The change hurt. Remove treatment. Learn why.
    +-- NO --> Inconclusive. Consider:
        +-- Was the test underpowered? (Run longer or with bigger change)
        +-- Was the hypothesis wrong? (User research needed)
        +-- Was the implementation correct? (Technical review)
```

---

## Statistical Pitfalls: Deep Dive

### Pitfall 1: Peeking

**The problem:** Checking results multiple times during an experiment inflates the false positive rate. If you check 10 times at 95% confidence, your actual false positive rate can be 25-40%.

**Why it happens:** Stakeholders are excited. The data is available. The temptation to "just take a quick look" is overwhelming.

**Solution 1: Hard blackout.** The experimentation platform hides results until the pre-determined end date. No one can see results early.

**Solution 2: Sequential testing.** Use a sequential testing framework (available in Eppo, Statsig, and others) that adjusts the significance threshold each time you look. This allows controlled peeking without inflating false positives.

**Solution 3: Cultural norm.** Establish a team norm that early results are unreliable and that "peeking" is a known cognitive bias, not diligent monitoring.

### Pitfall 2: Underpowered Tests

**The problem:** Running tests with too few users to detect meaningful differences. An underpowered test almost always shows a null result, regardless of whether the treatment actually works. This leads teams to discard potentially valuable ideas.

**Why it happens:** Impatience. The team wants to test many things quickly. Smaller pages or features may not get enough traffic.

**Solutions:**
- Calculate required sample size before launching. If the required duration exceeds 30 days, either increase the MDE (make a bolder change) or find a higher-traffic surface.
- Combine related features into a single test (but track individual metrics as secondary).
- Use Bayesian methods which can be more efficient with smaller samples.
- Accept that some surfaces cannot be A/B tested and must be evaluated through cohort-over-cohort or pre/post analysis.

### Pitfall 3: Multiple Testing

**The problem:** If you test 20 metrics and declare significance at p < 0.05, you expect one false positive by chance alone. If you test 20 variations of an experiment, same problem.

**Why it happens:** Exploratory analysis is natural. Teams want to find something positive in every experiment.

**Solutions:**
- Pre-register one primary metric. The experiment is judged on that metric only.
- Apply Bonferroni correction for multiple comparisons (divide alpha by number of tests).
- Use False Discovery Rate (FDR) correction for exploratory analysis.
- Clearly distinguish between confirmatory analysis (pre-registered) and exploratory analysis (hypothesis-generating, not proof).

### Pitfall 4: Simpson's Paradox / Segment Effects

**The problem:** An experiment shows a positive result overall but a negative result in every subgroup (or vice versa). This happens when the composition of control and treatment groups differs across segments.

**Why it happens:** Imperfect randomization, or external factors that differentially affect segments during the experiment.

**Solution:** Monitor results by key segments. Use proper randomization. Check for demographic or behavioral imbalances between groups.

### Pitfall 5: Novelty and Primacy Effects

**The problem:** Users react to change itself, not the change's value. A new feature may get clicks because it is new (novelty), or users may stick with the old way because it is familiar (primacy). Both effects fade over time.

**Solution:** Run experiments for at least 2-4 weeks. Compare week 1 results to week 3-4 results. If the effect diminishes significantly, you are seeing novelty, not genuine improvement.

### Pitfall 6: Survivorship Bias

**The problem:** Analyzing only users who completed a flow, not all users who started it. This makes treatments look better than they are because you are ignoring users who were so confused by the treatment that they dropped off entirely.

**Solution:** Always define the denominator carefully. For conversion experiments, the denominator should be ALL users exposed to the experiment, not just those who reached the conversion step.

---

## Pre/Post Analysis for Low-Traffic Surfaces

Elena Verna specifically addresses this for products that cannot reach statistical significance with A/B tests.

**When to use pre/post analysis:**
- Low-traffic surfaces where A/B test sample requirements exceed available traffic
- Changes that affect the entire product (cannot isolate a treatment group)
- Infrastructure changes where holdback groups are technically infeasible

**Guidelines:**
- Use at least 4 weeks of pre-period data
- Account for known external factors (marketing campaigns, seasonal patterns, app store features)
- Be explicit that the evidence is directional, not causal
- Use holdback groups when possible (ship to 90%, hold back 10%)
- Document all known confounders

**Elena Verna's 80/20 of experimentation methods:** For most product teams, simple methods cover 80% of needs: A/B tests for high-traffic surfaces, pre/post with holdback groups for lower-traffic surfaces, and qualitative user research for hypothesis generation. The remaining 20% (multi-armed bandits, sequential testing, causal inference) are valuable for mature teams but premature for most.

---

## Good vs. Bad Experiments: Diagnostic Framework

### Mosavat's Seven Dimensions of Experiment Quality

**1. Strategic Connection** -- Does the experiment test a hypothesis derived from the product strategy? Diagnostic: "If this experiment succeeds, what strategic question does it help answer?"

**2. Learning Compounding** -- Does it build on previous experiments and inform future ones? A good experiment exists in a chain: prior learning, this experiment, next experiment. A bad experiment has no antecedent and no descendant.

**3. System Awareness** -- Does it consider second-order effects? Common system effects to watch: improving conversion may reduce average user quality; improving activation through reduced friction may reduce retention; improving engagement through notifications may increase uninstalls.

**4. Humility vs. Deferral** -- Is the experiment testing genuine uncertainty, or deferring a decision that should be made with available information? Diagnostic: "If forced to make this decision without an experiment, would we have enough information?"

**5. Impact Potential** -- Would a successful result change the team's behavior? Diagnostic: "If this produces a 20% improvement, will we change our investment? If it fails, will we stop working on this?" If neither changes behavior, the experiment wastes resources.

**6. Communication Plan** -- Will results be documented and findable six months later? Undocumented experiments are worse than no experiments because they create the illusion of learning.

**7. Falsifiability** -- Can the team describe what failure looks like? "Let's see what happens if we change X" is not a hypothesis.

### Common Bad Experiment Archetypes

**The Tiebreaker Test:** Two people disagree about button color, so they propose an A/B test. This is decision deferral -- the button color is almost certainly not the binding constraint.

**The Vanity Metric Test:** Testing whether a new step increases "profile completion rate" without verifying that profile completion has a causal relationship with retention or revenue.

**The Competitor Copy Test:** Testing a competitor's feature without articulating why it would work for your specific users and strategy.

**The Optimization Treadmill:** Running test #47 on the same landing page, testing every conceivable permutation of headline and CTA, when the page is already optimized.

**The Launch Validation Test:** Retroactively calling a shipped feature an "experiment" by looking at pre/post metrics. Without a pre-defined hypothesis and control group, this is post-hoc rationalization.

---

## Building Experimentation Infrastructure

### Choosing a Platform

| Platform | Strengths | Best For |
|----------|----------|---------|
| Statsig | Anti-peeking, auto-analysis, feature flags | Teams wanting statistical guardrails |
| Eppo | Statistical rigor, warehouse-native | Data-sophisticated teams |
| LaunchDarkly | Feature flagging, rollout control | Teams needing feature flags with basic experimentation |
| Optimizely | Mature platform, multi-channel | Large teams with web and mobile |
| Custom-built | Full control | Very large teams (100+ engineers) |

Komissarouk recommends Eppo and Statsig specifically because they enforce statistical rigor: they limit premature analysis, ensure valid results, and prevent peeking.

### Minimum Viable Experimentation Stack

For a team starting out:
1. **Event tracking**: Amplitude, Mixpanel, or Segment
2. **Feature flags**: LaunchDarkly, Statsig, or Firebase Remote Config
3. **A/B test analysis**: Statsig, Eppo, or manual analysis with proper sample size calculation
4. **Dashboards**: Looker, Mode, or Amplitude dashboards

---

## Experiment Templates for your product

### Template 1: Onboarding Experiment
```
Hypothesis: Asking users about their product convention during onboarding
and personalizing the first engagement session will increase Day 1 engagement session
completion from 45% to 55%.

Control: Current onboarding (generic first engagement session)
Treatment: Tradition question + personalized first engagement session
Primary metric: Day 1 engagement session completion rate
Guardrails: Onboarding completion rate (must not drop >5%), crash rate
MDE: 10 percentage points
Required sample: ~400 per group (large effect size)
Duration: 7-14 days
```

### Template 2: Paywall Timing Experiment
```
Hypothesis: Showing the paywall after the 3rd engagement session instead of
the 1st will increase trial start rate from 12% to 18%.

Control: Paywall after first engagement session
Treatment: Paywall after third engagement session
Primary metric: Trial start rate (among users completing 1+ engagement session)
Guardrails: D7 retention, revenue per user at D30
MDE: 6 percentage points
Required sample: ~700 per group
Duration: 21 days
```

### Template 3: Notification Timing Experiment
```
Hypothesis: Sending the daily engagement notification at the user's
historical peak engagement time (vs. fixed 7am) will increase
notification open rate from 8% to 12%.

Control: Fixed 7am notification
Treatment: Personalized send time based on historical open patterns
Primary metric: Notification-to-app-open rate
Guardrails: Notification opt-out rate, D7 retention
MDE: 4 percentage points
Required sample: ~2,000 per group
Duration: 14 days
```
