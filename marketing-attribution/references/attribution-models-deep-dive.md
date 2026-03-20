## Contents
- The Attribution Model Landscape
  - Model Comparison Matrix
- Multi-Touch Attribution (MTA) — Deep Dive
  - How MTA Works Technically
  - MTA Models in Detail
  - Making MTA Work Despite Limitations
- Marketing Mix Modeling (MMM) — Deep Dive
  - How MMM Works Technically
  - Running MMM
  - Open Source MMM Tools
  - Common MMM Pitfalls
- Self-Reported Attribution — Deep Dive
  - Why Self-Reported Matters
  - Implementation Best Practices
- The Triangulation Decision Framework
  - When Models Disagree
  - Building Your Measurement Roadmap
- Application to your product

---
# Attribution Models Deep Dive — Deep Reference
*Source: Pranav Piyush, Mastering Marketing Attribution*

---

## The Attribution Model Landscape

Every attribution model makes trade-offs. Understanding these trade-offs is more important than choosing the "right" model.

### Model Comparison Matrix

| Dimension | MTA (Multi-Touch) | MMM (Marketing Mix) | Incrementality | Self-Reported |
|-----------|-------------------|--------------------|--------------:|---------------|
| What it measures | Touchpoint credit | Channel contribution | Causal impact | Perceived source |
| Data required | User-level events | Aggregate time series | Experiment design | Survey responses |
| Privacy impact | High (needs tracking) | Low (aggregate data) | Low (aggregate) | None |
| Granularity | User/session level | Channel/week level | Channel level | User level |
| Time to results | Real-time | 4-8 weeks | 2-4 weeks | Ongoing |
| Cost to implement | Medium | Medium-High | Low-Medium | Low |
| Causation vs. correlation | Correlation | Correlation | Causation | Perception |
| Best for | Tactical optimization | Budget allocation | Channel validation | Hidden channels |

---

## Multi-Touch Attribution (MTA) — Deep Dive

### How MTA Works Technically

MTA systems collect touchpoint data (ad impressions, clicks, site visits, emails opened) and assign credit using a model:

**Data collection:**
1. Pixel fires on website/app track user events
2. UTM parameters identify campaign/channel/creative
3. Identity resolution links events to a single user (cookies, device IDs, login)
4. Conversion events (purchase, signup, subscription) are recorded
5. The model assigns credit to touchpoints that preceded each conversion

**The identity resolution problem:**
Post-iOS 14.5, identity resolution is the weakest link:
- Cross-device tracking requires probabilistic matching (less accurate)
- Cookie-based tracking loses 30-50% of journeys (browsers block third-party cookies)
- iOS IDFA opt-out rates of ~75% make mobile attribution largely modeled

### MTA Models in Detail

**Last-Click Attribution:**
```
User sees Meta ad → Clicks Google ad → Visits site directly → Subscribes
Credit: 0% → 0% → 100% → (conversion)
```
- Simplest to implement
- Heavily biased toward lower-funnel, direct-response channels
- Under-credits brand and awareness channels
- Still the most common model (often by default)

**First-Click Attribution:**
```
User sees Meta ad → Clicks Google ad → Visits site directly → Subscribes
Credit: 100% → 0% → 0% → (conversion)
```
- Credits the channel that drove initial awareness
- Over-credits top-of-funnel channels
- Under-credits conversion-stage channels
- Useful for understanding how users discover you

**Linear Attribution:**
```
User sees Meta ad → Clicks Google ad → Visits site directly → Subscribes
Credit: 33% → 33% → 33% → (conversion)
```
- Equal credit to all touchpoints
- Simple and "fair" but naive
- Doesn't account for varying influence of different touchpoints
- Better than last-click but still over-simplifies

**Time-Decay Attribution:**
```
User sees Meta ad (7 days ago) → Clicks Google ad (3 days ago) → Visits direct (today) → Subscribes
Credit: 15% → 30% → 55% → (conversion)
```
- More credit to recent touchpoints
- Assumes recency = importance (not always true)
- Better for short consideration cycles
- Half-life parameter is arbitrary

**Position-Based (U-Shaped):**
```
User sees Meta ad → Clicks Google ad → Opens email → Visits direct → Subscribes
Credit: 40% → 10% → 10% → 40% → (conversion)
```
- Credits first and last touchpoints most heavily
- Assumes awareness and conversion are most important
- Arbitrary 40/20/40 split (why not 30/40/30?)
- Popular but not evidence-based

**Data-Driven (Algorithmic):**
```
Machine learning model analyzes all conversion and non-conversion paths
Assigns credit based on statistical contribution to conversion probability
Credit varies by touchpoint, channel, and user behavior
```
- Most sophisticated, uses ML to determine credit
- Requires significant data volume (>1,000 conversions/month per channel)
- Black box (hard to explain why credit is assigned)
- Available in Google Analytics 4, some paid tools
- Still limited by the same tracking blind spots

### Making MTA Work Despite Limitations

**Strategy 1: Use MTA for within-channel optimization**
MTA is most reliable when comparing performance within a single channel (Meta ad A vs. Meta ad B) rather than across channels (Meta vs. Google).

**Strategy 2: Track MTA trends, not absolutes**
If MTA shows Channel A's attributed revenue growing 20% MoM, the trend is probably directionally correct even if the absolute number is wrong.

**Strategy 3: Supplement with first-party data**
Use logged-in user data, email addresses, and subscription IDs for identity resolution. First-party data is more durable than third-party cookies.

**Strategy 4: Calibrate with incrementality**
Run an incrementality test on your top channel. Compare the incremental result to MTA's attribution. Apply the calibration factor to MTA going forward.

Example: MTA says Meta drives 1,000 conversions/week. Incrementality test shows 650 incremental conversions. Calibration factor: 0.65. Apply to all MTA-reported Meta numbers.

---

## Marketing Mix Modeling (MMM) — Deep Dive

### How MMM Works Technically

MMM uses regression analysis to model the relationship between inputs (marketing spend, pricing, seasonality) and outputs (revenue, conversions):

```python
# Simplified MMM equation
Revenue = β₀ + β₁(TV_spend_adstocked) + β₂(Digital_spend_adstocked)
        + β₃(Price) + β₄(Seasonality) + β₅(Competition) + ε
```

**Key technical concepts:**

**Adstock transformation:**
Marketing spend has effects that persist beyond the week/month it runs:
```
Adstock(t) = Spend(t) + decay_rate × Adstock(t-1)
```
Decay rate varies by channel:
- TV: 0.7-0.9 (long-lasting)
- Digital display: 0.3-0.5 (moderate)
- Paid search: 0.1-0.3 (short-lived, intent-based)
- Social media: 0.4-0.6 (moderate)

**Saturation (diminishing returns):**
Each channel has a point where additional spend yields decreasing returns:
```
Saturated_spend = 1 - exp(-λ × spend)
```
or using Hill function:
```
Saturated_spend = spend^α / (spend^α + K^α)
```

This produces the classic S-curve: slow start → rapid growth → plateau

**Decomposition:**
MMM decomposes total revenue into:
- Base (organic demand without any marketing)
- Incremental contribution from each channel
- External factors (seasonality, competition, pricing)

### Running MMM

**Data requirements:**
- 2-3 years of weekly data (minimum 1 year for modern Bayesian approaches)
- Marketing spend by channel by week
- Revenue/conversions by week
- External variables: seasonality indicators, pricing changes, competitive events
- Must have spend variation (if you spend the same every week, MMM can't detect signal)

**Process:**
1. Collect and clean data
2. Choose model type (frequentist or Bayesian)
3. Set priors for Bayesian models (domain knowledge about channel effects)
4. Fit model with adstock and saturation transformations
5. Validate model (out-of-sample prediction, business sense checks)
6. Generate channel-level response curves and ROI estimates
7. Run optimization: "Given budget X, what's the optimal allocation?"

### Open Source MMM Tools

**Meta Robyn (R):**
- Automated hyperparameter tuning
- Built-in adstock and saturation modeling
- Multi-objective optimization
- Active community, well-documented
- Best for: Companies with digital-heavy channel mix, R proficiency

**Google Meridian (Python):**
- Bayesian approach (better uncertainty quantification)
- Integrates Google reach/frequency data
- Prior specification for business knowledge
- Best for: Companies with Google-heavy spend, Python proficiency

**PyMC Marketing (Python):**
- Most flexible (full control over model specification)
- Bayesian, with rich uncertainty quantification
- Requires more statistical expertise
- Best for: Companies with data science teams who want full control

### Common MMM Pitfalls

1. **Not enough spend variation:** If you spend $50K on Meta every month, MMM can't distinguish Meta's effect from baseline. You need natural or deliberate variation.

2. **Confounding variables:** If you always increase spend during holidays, MMM may attribute holiday demand to your spend increase. Include proper seasonality controls.

3. **Treating results as exact:** MMM produces estimates with confidence intervals. A channel showing ROI of 2.5x with CI [1.2, 3.8] is very different from one showing 2.5x with CI [2.3, 2.7].

4. **Not refreshing:** The marketing landscape changes. MMM results from 12 months ago may not apply today. Refresh quarterly if possible.

---

## Self-Reported Attribution — Deep Dive

### Why Self-Reported Matters

"How did you hear about us?" captures channels that no digital attribution can track:
- Word-of-mouth / friend recommendation
- Community community / religious community recommendation
- Podcast mention (hard to attribute digitally)
- In-person event or recommendation
- Social media browsing (not clicking an ad)

### Implementation Best Practices

**When to ask:** During sign-up or onboarding (not after — completion rate drops)

**How to ask:**
- Multiple choice with common options + "Other" with free text
- Options should match your actual channel mix
- Include "Friend or family recommendation" (always larger than people think)
- Include offline channels (community, event, in-person)

**Example for your product:**
```
How did you first hear about your product?
○ Social media ad (Facebook, Instagram, TikTok)
○ Search (Google, App Store search)
○ Friend or family recommendation
○ Community or community
○ Podcast or radio
○ News article or blog
○ Browsing the App Store
○ Other: _________
```

**How to use the data:**
- Compare self-reported channel mix to MTA-reported channel mix
- The gap between MTA and self-reported often reveals under-measured channels
- Track self-reported mix over time (is word-of-mouth growing?)
- Use as a calibration signal alongside MTA and MMM

---

## The Triangulation Decision Framework

### When Models Disagree

| MTA Says | MMM Says | Incrementality Says | Decision |
|----------|---------|--------------------:|----------|
| Channel is great | Channel is great | Channel is great | Increase spend with confidence |
| Channel is great | Channel is mediocre | Not tested yet | Test incrementality before scaling |
| Channel is mediocre | Channel is great | Channel is great | MTA is under-attributing (fix calibration) |
| Channel is great | Channel is mediocre | Channel is mediocre | MTA is over-attributing (reduce spend) |
| All disagree | | | Run incrementality test — it's the tiebreaker |

### Building Your Measurement Roadmap

**Quarter 1:** Set up MTA + self-reported attribution
**Quarter 2:** Run first incrementality test on your #1 channel
**Quarter 3:** Calibrate MTA with incrementality results; begin MMM data collection
**Quarter 4:** Run incrementality on #2 channel; first MMM results

**Year 2:** Full triangulation operational. Quarterly incrementality tests, semi-annual MMM refresh, daily MTA for tactical optimization.

---

## Application to your product

For your product's measurement stack:

1. **MTA:** Branch or AppsFlyer for mobile attribution. Accept iOS blindness, use as within-platform optimization tool.
2. **Self-reported:** Critical. "Community community" and "friend recommendation" likely represent 20-40% of acquisition that's invisible to digital attribution.
3. **Incrementality:** Start with Meta Conversion Lift study (largest paid channel). Compare incremental CPA to Meta-reported CPA.
4. **MMM:** Begin collecting weekly spend data now. In 12-18 months, run first MMM to understand true channel contributions.
