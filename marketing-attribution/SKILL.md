---
name: marketing-attribution
description: Applies Pranav Piyush's Mastering Marketing Attribution frameworks to measure marketing effectiveness and determine what channels and campaigns are actually working. Covers multi-touch attribution, marketing mix modeling (MMM), incrementality testing, and how AI is changing measurement. Activates when making decisions about marketing spend allocation, channel performance evaluation, attribution model selection, or when you need to understand true channel ROI. Triggers when asked about marketing measurement, attribution, incrementality, MMM, ROAS, or when someone says "we don't know what's working."
---

**Reference files:**
- `references/attribution-models-deep-dive.md` — Detailed comparison of MTA, MMM, and incrementality with when to use each
- `references/incrementality-testing.md` — How to design and run incrementality experiments for marketing channels
- `references/measurement-in-ai-era.md` — How AI is changing marketing measurement and what to do about it

---

## How to Use This Skill

When this skill activates:
1. Identify which attribution and measurement framework from this skill best applies to the question
2. Apply the relevant decision tree from the Decision Tools section
3. Ground all recommendations in the context of your product
4. Cite the specific framework and Pranav Piyush's methodology when making claims
5. If deeper detail is needed, read the relevant reference file before responding

## Gotchas

Common mistakes to avoid when applying these frameworks:

1. **Don't trust last-click attribution for brand or upper-funnel campaigns:** Pranav's Triangulation Framework exists because no single model captures the full picture. Last-click systematically under-credits brand, content, and awareness channels that influence conversions without being the final touchpoint.
2. **Don't recommend MMM for companies with less than 18 months of spend data:** MMM requires sufficient historical data with meaningful spend variation across channels. Recommending it prematurely leads to unreliable models and false confidence in the outputs.
3. **Don't treat platform-reported ROAS as ground truth:** Meta, Google, and TikTok each claim credit for overlapping conversions. Self-reported platform numbers are inflated 20-50% on average -- always flag this when citing platform data and recommend cross-referencing with incrementality.
4. **Don't skip self-reported attribution for your product:** For a consumer app, word-of-mouth, community referrals, and expert recommendations are likely significant acquisition channels that no digital attribution model can detect. A "How did you hear about us?" survey is not optional -- it's critical infrastructure.

## Example

**User asks:** "Meta says our ROAS is 4.5x but our finance team says overall marketing ROI is only 1.8x. Who's right?"

**Approach:**
1. Apply the Triangulation Framework -- explain that Meta's self-reported ROAS is likely inflated 20-50% due to over-attribution (claiming organic conversions) and use Decision 3 (Should I Trust This Platform's Self-Reported ROAS?)
2. Recommend running a Meta Conversion Lift study to measure true incremental impact, sizing the holdout at 10-15% of the target audience
3. Cross-reference with self-reported attribution data and any MMM results to identify where the gap comes from (organic cannibalization, cross-platform double-counting, or missing offline channels)
4. Output a measurement action plan: which test to run first, expected timeline, and how to reconcile the two numbers using incrementality-adjusted ROAS

---

## Core Philosophy

> "There is no single source of truth for marketing measurement. The goal is not to find the perfect attribution model — it's to triangulate across multiple imperfect signals to make better decisions."

Marketing attribution has been in crisis since iOS 14.5 broke user-level tracking in 2021. The old model — deterministic multi-touch attribution (MTA) based on cookies and device IDs — is increasingly unreliable. The new model requires combining multiple measurement approaches (MTA, MMM, incrementality testing) to triangulate truth. Pranav's core insight is that the question isn't "which model is right?" but "how do we make better allocation decisions given uncertainty?" The shift from attribution as accounting to attribution as decision science is the central theme of this course.

---

## Module 1: The Attribution Landscape — What Broke and Why

### The Attribution Crisis

**What happened:**
1. iOS 14.5 (2021): Apple requires opt-in for cross-app tracking. ~75% of iOS users opt out.
2. Cookie deprecation: Third-party cookies being phased out across browsers
3. Privacy regulations: GDPR, CCPA, and similar laws restrict data collection
4. Walled gardens: Meta, Google, TikTok each report in their own ecosystems with overlap

**What broke:**
- Multi-touch attribution (MTA) lost visibility into cross-device, cross-platform journeys
- Last-click attribution became even more unreliable (misses upper-funnel influence)
- Self-reported platform attribution double-counts (Meta and Google both claim the same conversion)
- Attribution windows shortened (7-day click, 1-day view standard)

### The Three Pillars of Marketing Measurement

Modern marketing measurement requires three complementary approaches:

**Pillar 1: Multi-Touch Attribution (MTA)**
- What it does: Assigns credit to touchpoints in the customer journey
- Strengths: Granular, real-time, actionable for tactical optimization
- Weaknesses: Increasingly blind (privacy), biased toward measurable channels, misses offline
- Best for: Tactical channel optimization within known digital journeys

**Pillar 2: Marketing Mix Modeling (MMM)**
- What it does: Uses statistical models to correlate marketing spend with business outcomes at the aggregate level
- Strengths: Privacy-safe (uses aggregate data), captures offline and brand effects, portfolio-level view
- Weaknesses: Requires 2-3 years of historical data, slow (quarterly refresh), less granular
- Best for: Strategic budget allocation across channels, long-term planning

**Pillar 3: Incrementality Testing**
- What it does: Uses experiments (holdout tests, geo-lift tests) to measure causal impact of marketing
- Strengths: Gold standard for causation (not just correlation), privacy-safe, channel-specific
- Weaknesses: Requires pausing or reducing spend (opportunity cost), takes time, not always feasible
- Best for: Validating channel performance, resolving disagreements between MTA and MMM

### The Triangulation Framework

```
MTA says Channel A drives 40% of conversions
MMM says Channel A drives 25% of conversions
Incrementality test says Channel A drives 30% of conversions

→ True impact is likely ~30% (incrementality is most trustworthy)
→ MTA over-attributes (probably getting credit for organic conversions)
→ MMM under-attributes (may not capture all digital touchpoints)
→ Use 30% for planning, validate with next incrementality test
```

**The Triangulation Process:**
1. Run MTA for tactical, daily optimization
2. Run MMM quarterly for portfolio-level allocation
3. Run incrementality tests on highest-spend channels annually
4. When models disagree, trust incrementality > MMM > MTA
5. Update MTA calibration based on incrementality learnings
6. Rinse and repeat — measurement is ongoing, not a one-time exercise

**Anti-patterns:**
- Relying on a single attribution model as "the truth"
- Trusting ad platform self-reported numbers without validation
- Not investing in measurement because "it's impossible to measure perfectly"
- Measuring everything except incrementality (the only causal approach)

---

## Module 2: Multi-Touch Attribution (MTA) in Practice

MTA assigns credit to touchpoints using models (last click, first click, linear, time decay, position-based, data-driven) — each with different biases. MTA works best when journeys are primarily digital/single-device with high volume (>1,000 conversions/month). It's least useful with cross-device journeys, offline touchpoints, or heavy privacy restrictions.

**Making MTA actionable:** Use for relative measurement (trends, not absolutes), compare within-platform data, and supplement with self-reported attribution surveys. Never make large budget decisions based solely on MTA numbers.

*→ Full MTA model comparison and usage guide: `references/attribution-models-deep-dive.md`*

---

## Module 3: Marketing Mix Modeling (MMM) and Media Optimization

MMM uses regression analysis to correlate aggregate marketing inputs with business outcomes. Key concepts: adstock/carryover (spend has delayed effects), saturation curves (diminishing returns per channel), and decomposition (separating channel contributions from organic baseline).

Modern open-source MMM (Meta Robyn, Google Meridian, PyMC Marketing) has dramatically reduced the cost and speed vs. traditional consulting-firm approaches: 1-2 years of data (vs. 3+), quarterly refresh (vs. annual), $50-200K (vs. $200K-$1M+).

**Primary use case:** Answering "How should I allocate my next $1M across channels?" by identifying which channels are on the steep vs. flat part of their response curves. Always validate large shifts with incrementality tests.

**Anti-patterns:** Running MMM once as permanent truth, not varying spend enough to give signal, using MMM for daily tactical decisions, treating decomposition as exact.

*→ Full MMM comparison and optimization process: `references/attribution-models-deep-dive.md`*

---

## Module 4: Incrementality Testing and the Future of Measurement

### Incrementality Testing

The only measurement approach that proves causation: compare a group exposed to marketing vs. a holdout group. Four test types: (1) Geo-lift tests (turn off marketing in some regions), (2) Ghost ads (show control group a neutral ad), (3) Conversion lift studies (platform-native holdout from Meta/Google), (4) Matched market tests (pair similar markets). Design steps: define the specific question, choose test type, run power analysis (hold out 10-20%), run the full test without other changes, analyze with confidence intervals, act on results. Re-test periodically since incrementality changes over time.

*→ Full test design and analysis guide: `references/incrementality-testing.md`*

### How AI Is Changing Measurement

AI creates a measurement paradox: platforms are more automated but less transparent. AI ad platforms (Advantage+, PMax) make it harder to know who saw what, while optimizing for platform-attributed conversions (inflating self-reported numbers). Counter-measures: run more incrementality tests (not fewer), use modern MMM with frequent updates, invest in first-party data, and never assume AI-optimized campaigns are automatically efficient.

*→ Full AI measurement framework: `references/measurement-in-ai-era.md`*

---

## Decision Tools

### Decision 1: Which Attribution Approach Should I Use?

```
Annual marketing spend?
├── < $500K → Last click + self-reported + simple incrementality tests
├── $500K - $5M → MTA + incrementality tests on top channels
│   └── Consider: modern open-source MMM (Robyn or Meridian)
└── > $5M → Full triangulation (MTA + MMM + incrementality)
    └── Consider: commercial MMM platform (Paramark, Measured)
```

### Decision 2: Should I Run an Incrementality Test?

```
Is this channel >15% of your total marketing spend?
├── Yes → You should test incrementality at least annually
│   └── Is MTA showing results that seem "too good"?
│       ├── Yes → Test immediately (likely inflated)
│       └── No → Schedule for next quarter
└── No → Is this a new channel you're considering scaling?
    ├── Yes → Test before scaling (don't invest more without proof)
    └── No → Focus incrementality tests on your biggest channels first
```

### Decision 3: Should I Trust This Platform's Self-Reported ROAS?

```
Is the platform reporting the attribution? (e.g., Meta reporting on Meta)
├── Yes → Expect 20-50% inflation over true incremental impact
│   └── Use as directional signal only, not for budget decisions
│   └── Cross-reference with: MTA, self-reported attribution, MMM
└── No → Is it a third-party attribution platform?
    ├── Yes → More trustworthy, but still limited by tracking gaps
    │   └── Validate top channels with incrementality tests
    └── No → What data is this based on?
        └── If unclear → Do not use for decisions
```

### Decision 4: How Should I Allocate Budget Across Channels?

```
Do you have incrementality data for your top channels?
├── Yes → Use incrementality-adjusted ROAS for allocation
│   └── Shift from channels with low incrementality to high
└── No → Do you have MMM data?
    ├── Yes → Use MMM response curves for allocation
    │   └── But validate top 2-3 channels with incrementality tests
    └── No → Use MTA as directional signal
        └── Supplement with: self-reported attribution, holdout tests
        └── Plan to invest in better measurement within 6 months
```

---

## Applied to your product

your product as a mobile subscription app faces specific measurement challenges that this course's frameworks directly address.

**The Attribution Stack for your product:** As a mobile-first subscription app, your product operates in the most attribution-challenged environment. iOS users (likely 60%+ of your product's audience given the US demographic) largely opt out of IDFA tracking. This means multi-touch attribution has significant blind spots. The recommended measurement approach:

1. **MTA (daily tactical):** Use Branch or AppsFlyer for mobile attribution. Accept that iOS attribution will be modeled/probabilistic, not deterministic. Use for daily campaign optimization within each ad platform, but don't trust cross-platform attribution at face value.

2. **Self-reported attribution:** Add "How did you hear about us?" during onboarding. This captures word-of-mouth and community referrals that no digital attribution can track — likely a significant channel for a consumer app.

3. **Incrementality testing (quarterly):** Run Meta Conversion Lift studies on your largest paid channel. Hold out 10-15% of the target audience and measure incremental installs and subscriptions. This will reveal your true incremental CAC vs. what Meta self-reports.

4. **MMM (semi-annual):** Once your product has 18+ months of spend data with sufficient variation, implement an open-source MMM (Meta Robyn is a good starting point) to understand the relative contribution of paid social, ASO, content marketing, partnerships, and organic/word-of-mouth.

**Key Measurement Questions for your product:**
- What percentage of subscribers that Meta claims credit for would have subscribed anyway (organic cannibalization)?
- Are community partnership referrals and word-of-mouth driving more subscriptions than paid channels? (Self-reported attribution will reveal this.)
- What is the incrementally-adjusted CAC vs. the platform-reported CAC? This determines actual unit economics.
- Does brand investment (content marketing, PR, podcast sponsorships) reduce paid channel CAC over time? (Track organic share trend quarterly.)

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| Multi-Touch Attribution (MTA) | Assigns conversion credit to touchpoints in the user journey based on a model |
| Marketing Mix Modeling (MMM) | Statistical model correlating aggregate marketing inputs with business outcomes |
| Incrementality Testing | Experimental measurement of the causal impact of marketing (exposed vs. holdout) |
| Triangulation | Combining MTA, MMM, and incrementality to arrive at better measurement than any single approach |
| Geo-Lift Test | Incrementality test using geographic regions as test and control groups |
| Conversion Lift Study | Platform-native test holding back ads from a random subset to measure lift |
| Adstock / Carryover | The delayed and decaying effect of marketing spend beyond the period it runs |
| Saturation Curve | The diminishing returns curve for each marketing channel |
| ROAS | Return on ad spend (revenue attributed to ads / ad spend) |
| Incremental ROAS (iROAS) | ROAS measured by incrementality testing (only counting truly incremental conversions) |
| Self-Reported Attribution | "How did you hear about us?" survey capturing channels invisible to digital tracking |
| First-Party Data | Data collected directly from users with their consent (most reliable in privacy era) |
| IDFA | Apple's Identifier for Advertisers — now requires opt-in, breaking mobile attribution |
| Ghost Ads | Control methodology showing a neutral ad to a holdout group to measure true ad impact |

---

## Reference Files

- `references/attribution-models-deep-dive.md` — Detailed comparison of MTA, MMM, and incrementality with decision frameworks for each
- `references/incrementality-testing.md` — Step-by-step guide to designing, running, and analyzing incrementality experiments
- `references/measurement-in-ai-era.md` — How AI ad platforms, privacy changes, and new tools are reshaping marketing measurement
