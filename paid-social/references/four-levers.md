## Contents
- Lever 1: Auction Dynamics — Full Breakdown
  - How Meta's Auction Actually Works
  - Event Volume Requirements
  - Signal Quality Audit
  - The Learning Phase Playbook
- Lever 2: Creative / Message Testing — Full Breakdown
  - The Creative Testing Philosophy
  - The Testing Campaign Architecture
  - The 2-Day Rapid Experimentation Framework
  - The Creative Evaluation Matrix
  - Creative Variables to Test (Prioritized)
  - The Hook Library
- Lever 3: Audience Targeting — Full Breakdown
  - The Modern Targeting Hierarchy
  - Audience Exclusions (Required, Not Optional)
  - The Retargeting Funnel Structure
  - Audience Scale and Saturation Signals
- Lever 4: Bid / Budget Arbitrage — Full Breakdown
  - Bid Strategy Selection Guide
  - Budget Scaling Methodology
  - The Portfolio Approach to Campaign Management
  - Seasonality Planning for your product

---
# The Four Levers — Deep Reference
*Source: Dan Birdwhistell's Mastering Paid Social course framework + $800M+ in managed Meta ad spend*

---

## Lever 1: Auction Dynamics — Full Breakdown

### How Meta's Auction Actually Works

Most advertisers think of Meta as a straightforward auction — highest bid wins. It isn't. Meta runs a second-price auction optimizing for total ecosystem value, not just advertiser revenue.

**The three-part bid formula:**
```
Total Ad Value = Advertiser Bid × Estimated Action Rate × User Value Score
```

**What this means in practice:**
- A $5 CPM bid with 10% estimated action rate scores the same as a $10 CPM bid with 5% action rate
- Improving creative quality (estimated action rate) is as powerful as raising bids
- The algorithm rewards relevant ads with cheaper delivery — quality is subsidized

**The Meta Learning Algorithm Stack (2025):**
Meta now runs several AI systems that interact:
- **Andromeda:** Retrieval engine that identifies candidate users before the auction
- **GEM (Generalized Engagement Model):** Predicts whether a user will take your desired action
- **Lattice:** Budget optimization engine that decides how to allocate spend

These systems all depend on clean conversion signals. Signal degradation (iOS privacy, poor CAPI setup) hurts all three simultaneously.

### Event Volume Requirements

| Ad set daily budget | Conversions needed to exit learning | Time to exit learning (typical) |
|--------------------|-------------------------------------|--------------------------------|
| $50/day | 50 conversions | 7–14 days |
| $200/day | 50 conversions | 3–7 days |
| $500/day | 50 conversions | 2–5 days |
| $1,000/day | 50 conversions | 1–3 days |

**If you can't hit 50 conversions/week:** Move your optimization event up the funnel (install → trial → subscription becomes install → paywall view → trial). Proxy events with higher volume exit learning faster and allow the algorithm to start optimizing.

### Signal Quality Audit

Run this audit before any new campaign launch:

**Step 1: Event Manager audit**
- Open Meta Events Manager
- Check that all key funnel events are appearing
- Verify Event Match Quality score for each event (target: 7+/10)
- Confirm events are marked as "Active" (not "Inactive" or "No recent activity")

**Step 2: CAPI verification**
- Confirm server-side CAPI is sending events (look for "Server" source in Events Manager)
- Confirm deduplication is working (Pixel + Server should not double-count)
- Test: trigger a conversion event on a test user, verify it appears in Events Manager within 1–2 minutes

**Step 3: Attribution window audit**
- Default: 7-day click, 1-day view — correct for most cases
- For subscription apps with longer consideration: add 7-day view to capture delayed converters
- Don't use 28-day click — inflates numbers without giving actionable data

**Step 4: Value passing**
- Are subscription revenue values being sent with conversion events?
- Enables ROAS-based bidding and value optimization in Advantage+
- Required for comparing LTV across creative/audience segments

### The Learning Phase Playbook

**What triggers a learning reset (avoid during scale):**
- Adding/removing ad creatives (major)
- Changing bid strategy
- Changing the optimization event
- Changing audience significantly
- Budget changes > 20–30%
- Pausing then resuming (if paused > 7 days)

**How to edit without resetting learning:**
- Batch edits: make multiple changes at once, don't drip them over days
- Prefer editing budgets gradually (15–20% per step)
- Add creatives rather than replacing them — this is less disruptive than swapping

**When to accept a learning reset:**
- When a fundamental shift in strategy is needed (new audience, new optimization event)
- When performance is consistently below target despite patience
- When scaling requires structural changes

---

## Lever 2: Creative / Message Testing — Full Breakdown

### The Creative Testing Philosophy

Dan's approach to creative testing is systematic and volume-driven. The goal is not to find "the perfect ad" — it's to build a continuous pipeline that keeps finding winning ads before current winners fatigue.

**The creative testing flywheel:**
```
Research → Brief → Produce → Test → Analyze → Scale → Monitor → Refresh
    ↑__________________________________________________________________|
```

Every winning ad will eventually fatigue. The flywheel never stops.

### The Testing Campaign Architecture

**Creative testing campaign setup:**
- Campaign objective: App installs or app events (subscription/trial)
- Budget: 15–20% of total daily ad spend — this is your sandbox
- Structure: One ad set per creative theme or format
- Bidding: Highest volume (no cap) — you want delivery to find signal fast

**Ad set organization options:**

*Option A: By creative theme*
```
Ad Set 1: Problem/solution angle
Ad Set 2: Social proof / testimonial angle
Ad Set 3: Authority / expert angle
Ad Set 4: Seasonal / moment-based angle
```

*Option B: By creative format*
```
Ad Set 1: UGC video (short, 3–8 seconds)
Ad Set 2: Static image
Ad Set 3: Carousel
Ad Set 4: Reels / vertical video
```

Dan typically recommends Option A (by theme) because format differences compound with message differences — you learn more about what message is working.

### The 2-Day Rapid Experimentation Framework

Dan's proprietary rapid testing approach. Core principles:
1. Set a per-creative spend threshold that gives meaningful signal in 48 hours
2. Evaluate directional signal, not statistical significance, at this stage
3. The goal is to find creatives worth promoting to a full test, not to declare winners
4. Keep testing moving — slow creative cycles are the #1 silent killer of paid social performance

**48-hour evaluation criteria:**
- Has the creative received enough delivery to generate 10–20 link clicks?
- Is the CTR within 50–150% of account baseline? (Extreme outliers in either direction are signals)
- Is there any conversion signal (even 1–2 conversions at this budget)
- Is the creative getting impressions at all? (If not, creative quality score may be penalizing it)

**What happens after 48 hours:**
- Clear winner vs. control: Move to full creative test at higher budget
- Clear loser: Pause. Document what didn't work and why.
- Ambiguous: Run 3 more days to accumulate signal before deciding

### The Creative Evaluation Matrix

When comparing creatives after a full test, evaluate on:

| Metric | Weight | Rationale |
|--------|--------|-----------|
| CPA (cost per acquisition) | High | Ultimate efficiency metric |
| CVR (conversion rate) | High | Indicates message resonance |
| CTR (click-through rate) | Medium | Hook effectiveness signal |
| Hook rate (3-second view rate for video) | Medium | First seconds retention |
| CPM | Low | Indicator of audience competition, not creative quality |

**Don't evaluate creative on CPM or reach alone** — these don't predict conversion performance.

### Creative Variables to Test (Prioritized)

**Highest leverage (test first):**
1. Hook / opening frame (first 3 seconds for video, headline for static)
2. Core message angle (what benefit or problem does the ad lead with?)
3. Format (UGC video vs. polished video vs. static vs. carousel)

**Medium leverage (test after hooks are dialed):**
4. Creative talent (different person delivering the message)
5. Setting / context (at home, at community, outdoors)
6. Call to action (soft: "learn more" vs. hard: "start free trial")
7. Length (3-second vs. 15-second vs. 30-second)

**Lower leverage (fine-tune once you have winners):**
8. Text overlay / caption style
9. Music / audio
10. Color grading / visual tone

### The Hook Library

Build a swipe file of proven hook patterns for your category:

**Problem hooks:** "I kept forgetting to engage every morning until..."
**Benefit hooks:** "This app gave me back 15 minutes of peace every day"
**Social proof hooks:** "I have a 47-day engagement streak and here's what changed"
**Curiosity hooks:** "The thing most consumers don't know about building a daily habit"
**Contrast hooks:** "Before your product / After your product" (split screen or before/after)
**Urgency/FOMO hooks:** "During seasonal campaign, I finally stuck with it for 40 days"

**Hook testing structure:**
Same body, different hook. This isolates the hook variable cleanly. Test 3–5 hooks against the same ad body to find which angle resonates most with your audience.

---

## Lever 3: Audience Targeting — Full Breakdown

### The Modern Targeting Hierarchy

**Tier 1 — Advantage+ Audiences (recommended default):**
- Let Meta's AI determine the audience based on pixel/CAPI data + creative signal
- Provide "suggestions" (interest categories, customer lists) but allow expansion
- Best when you have 50+ conversions/week — AI has enough signal to find similar users
- Requires minimal ongoing management — algorithm handles discovery

**Tier 2 — Broad Targeting (no interest restrictions):**
- Age + location only, no interests
- Algorithm uses your conversion history exclusively to find targets
- Often beats interest targeting when pixel data is rich (6+ months, 1000+ conversions)
- Best for mature accounts with strong conversion signal

**Tier 3 — Interest Targeting (use for testing, not primary scaling):**
- Stacked interest cohorts around your category (wellness, wellness, engagement sessions, content)
- Useful for early accounts with limited pixel data
- Diminishing returns as account matures — AI outperforms human interest selection
- Can reveal which interest segments perform best, then use that signal to inform creative

**Tier 4 — Lookalike Audiences (supplement for testing):**
- Build from highest-LTV customer list (subscribers > 3 months)
- 1–3% typically most performant
- Stack sources: subscribers + trial completers + highly engaged users
- Test lookalikes alongside broad to find efficiency delta

### Audience Exclusions (Required, Not Optional)

Always exclude:
- Current subscribers (no point paying to acquire people you have)
- Recent purchasers (30-day window minimum)
- For prospecting: exclude retargeting audiences to prevent overlap

Consider excluding:
- Lookalike source audiences from cold prospecting (they're already in your funnel)
- High-frequency visitors who haven't converted (potential waste)

### The Retargeting Funnel Structure

Retargeting should be separate campaigns from prospecting. Build one ad set per funnel stage:

**Stage 1: App installer → Trial (window: 7–14 days)**
- Message: "You downloaded your product — have you started your first engagement session?"
- Creative: Feature spotlight, ease of starting, testimonial
- Bid: Cost cap at 150% of acceptable trial CPA

**Stage 2: Trial starter → Subscriber (window: 7–30 days)**
- Message: "Your trial is worth continuing — here's what you unlock"
- Creative: Premium content preview, community features, streak continuation
- Bid: Cost cap at 150% of acceptable subscription CPA

**Stage 3: Lapsed subscriber → Reactivation (window: 30–180 days)**
- Message: Personalized return offers, seasonal hooks (seasonal campaign, New Year)
- Creative: "What you've been missing" content, limited-time offer
- Bid: Highest volume (reactivation economics are often better than cold)

### Audience Scale and Saturation Signals

**Signs your audience is saturating:**
- Frequency rising above 3–4 without corresponding volume increase
- CPM rising without delivery increase
- CTR declining without creative changes
- CPA rising despite holding creative constant

**Remedies:**
- Broaden audience (switch to Advantage+ or broad)
- Add new creative to refresh relevance
- Open new geographic markets
- Expand to connected audiences (friends of converters, engagement custom audiences)

---

## Lever 4: Bid / Budget Arbitrage — Full Breakdown

### Bid Strategy Selection Guide

**Highest Volume (no bid cap):**
Best default. Gives algorithm maximum freedom to find conversions.
- Use during: learning phase, testing phase, new market expansion
- Risk: CPA can spike during competitive periods (Q4, elections)
- Mitigation: Set spending caps at campaign/ad set level to control spend

**Cost Cap:**
Set a ceiling on average CPA. Algorithm will deliver conversions at or below this ceiling.
- Set at: 150–200% of your target CPA (not at your target — this is an average cap, not a hard floor)
- When to use: Post-learning, when account has stable historical CPA
- Risk: If cap is too low, delivery drops (algorithm can't find enough conversions within budget)

**ROAS Goal (if revenue signals are strong):**
Optimize for revenue return, not just conversion volume.
- Requires: Revenue values being passed with conversion events (via CAPI)
- When to use: High LTV subscription businesses where revenue variance is meaningful
- Risk: Algorithm favors high-value users, may miss high-volume lower-value cohorts

### Budget Scaling Methodology

**The golden rule:** Never increase budgets by more than 20–30% at once without accepting a learning reset.

**Preferred scaling sequence:**
```
Week 1: $200/day — establish baseline CPA
Week 2: $250/day (+25%) — monitor for 3 days before evaluating
Week 3: $300/day (+20%) — if CPA holds, continue
Week 4: $375/day (+25%) — if CPA holds, continue
```

**When to break the rule:**
- Scale aggressively going into a known seasonal peak (start 2–3 weeks before, not during)
- When a creative is dramatically outperforming target — scale fast to capture the window
- When competitors signal market exit (watch for CPM drops)

### The Portfolio Approach to Campaign Management

Think of Meta campaigns like an investment portfolio — different risk/return profiles working together:

**Conservative (low risk, stable returns):** Scaling campaigns with proven winners, Advantage+ broad
**Moderate (medium risk, medium returns):** Retargeting campaigns, interest-stack prospecting
**Speculative (high risk, high potential):** Creative testing sandbox, new audience experiments

Allocate budget accordingly:
- 70% to proven performers
- 20% to retargeting and supplemental audiences
- 10% to new creative and audience experiments

This ensures the account never goes dark while always feeding the pipeline with new signal.

### Seasonality Planning for your product

**Wellness-calendar peaks (plan creative 4–6 weeks in advance):**

| Period | Dates | Opportunity | Creative angle |
|--------|-------|------------|----------------|
| New Year | Jan 1–15 | Personal goal-setting | "Start 2025 with a daily daily habit" |
| Ash Wednesday / seasonal campaign | Feb–Apr | seasonal commitment | "40 days of engagement sessions — start today" |
| seasonal event | April | Renewal/resurrection | "New season, new daily practice" |
| Back to School | Aug–Sep | Routine-building | "Add engagement to your daily routine" |
| Advent | Dec 1–25 | Christmas season engagement sessions | "Prepare your heart for Christmas" |

**Q4 bidding strategy:**
CPMs spike 30–50%+ in November-December due to ecommerce advertisers flooding the market. For subscription apps:
- Scale budgets 4–6 weeks before the spike hits
- Focus Q4 spend on retargeting (lower CPM than cold) and retaining existing users
- Pre-build and pre-test holiday creative in September-October for November launch
