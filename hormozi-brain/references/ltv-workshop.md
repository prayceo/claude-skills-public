# The LTV Workshop

**Source:** Alex Hormozi's ACQSA LTV Workshop (Dec 5, 2025) — a math-heavy deep-dive on Lifetime Gross Profit, Earnings Per Click, gross margin optimization, the fractal nature of customer value, and upsell timing.

**Relationship to `money-models.md`:** `money-models.md` covers the *construction* side (which offers to build — attraction / upsell / downsell / continuity). This file covers the *optimization* side — how to maximize gross profit per customer, the math of gross margins, fractal pricing architecture, the 5 upsell times, and the anti-patterns that destroy LTV. Load both for complete monetization work.

**When to load this:** Diagnosing LTV as constraint, calculating LTGP/EPC, raising gross margins, pricing architecture / tier design, subscription math (LTR / hypothetical max revenue), avatar selection, building upsell scripts, surveying customers to cut costs, or reframing commodity pricing.

---

## The Core Thesis

> **"You can only grow a business by selling more customers or making them worth more. That's it. There's nothing else to it."**

Two wars in business (Dan Kennedy):
1. **Get customers for free** (viral/zero-cost model) — few can do it
2. **Make so much money per customer that CAC is irrelevant** — most service businesses should play this game

Everyone stuck in the middle is on the "hamster wheel of death."

> **"He who can spend the most to acquire a customer wins."** — Dan Kennedy

The real goal isn't LTV itself — it's **EPC (Earnings Per Click)**. You're competing in an auction of attention. Whoever earns more per click wins the auction.

---

## LTGP vs LTV — Definitional Precision

Hormozi prefers **LTGP (Lifetime Gross Profit)** over LTV because:

- Software has 80%+ gross margins → revenue × months ≈ LTV
- Service/physical product has variable margins → revenue × months ≠ LTV
- **Correct formula:** `LTV = Lifetime Revenue × Gross Margin`

**Language matters:**
- **Gross margin** = percentage (e.g., 80%)
- **Gross profit** = dollar amount (e.g., $15 per sale)
- "Gross profit margin" sometimes means the percentage. Use the full words and always clarify.

**The 3-step process:**
1. **Know your current state** — your LTGP, to real accuracy
2. **Set a desired superior state** — the target LTV / gross margin
3. **Take action to bridge the gap** — implement the highest risk-adjusted-return path

---

## The Auction of Attention — EPC Framework

**Live example from the workshop:**

| Variable | $29/mo test | $99/mo test |
|---|---|---|
| Clicks | 100 | 100 |
| Signup rate | 3% | 4.5% |
| Signups | 3 | 4.5 |
| Trial → paid conversion | 66% | 33% |
| Monthly churn | 5% | 10% |
| **EPC (earnings per click)** | **Higher** | Lower |

**Lesson:** Lower price can produce higher EPC because it compounds conversion AND retention. Many variables affect one another. BF Skinner: *"If many variables exist, many variables must be studied."*

Don't throw up your hands. Learn to play it.

---

## The 2 "Novel" Concepts Hormozi Flagged

He explicitly said there were two concepts he'd never presented before that were "unbelievably powerful." They are:

### 1. The Fractal Nature of Customer Value (Pareto²)

Not just 80/20. **80/20 applied recursively:**

- Top 20% = **80%** of revenue
- Top 4% (20% of 20%) = **64%** of revenue
- Top 0.8% (20% of 4%) = **51%** of revenue
- Top 0.16% = ~**41%** of revenue

**Why this is true IF AND ONLY IF** you give customers a way to pay more. Most businesses fail to build the pricing structure that lets the fractal emerge. They cap their best customers at the same rate as their worst.

Proof: Progressive tax systems. More income → more tax → the recursive nature tracks wealth distribution automatically.

> "Pricing is fractal. The more people make, the more they can afford to pay. Sell them something so much more expensive. That's where we got to be."

### 2. Monetization Layers as Fractal Pricing Architecture

**Rule of thumb:** Each tier must be at least **5× the price** of the prior tier.

**The math:** 20% take rate × 5× price = **doubles revenue from that tier**

| Layer | Who | Price Multiple | Example (ACQ) |
|---|---|---|---|
| L1 (base) | 80% of buyers | 1× | School at $100/mo |
| L2 | Top 20% | 5–10× | School premium tiers |
| L3 | Top 4% | 25–100× | Portfolio company tools |
| L4 | Top 0.8% | 100×+ | Advisory engagements |
| L5 | Top 0.1% | 1,000×+ | Acquisition relationships |

**Warnings:**
- Don't build all layers at once (Shopify: ~20 years, Apple: 50+, McKinsey: 50+)
- A new tier must be worth the operational cost. If adding a tier doubles the work but adds only 20% revenue, it's not worthwhile.
- **Price like you mean it.** If you hedge on price, you attract hedging customers.

---

## The 3 Gross Margin Improvement Options (Full Math)

**Starting scenario:** Marketing agency, 50 customers, $5K/month price, 5-person team costing $1M/yr in total.
- Revenue: $3M/yr
- Cost base: $1M
- **Current gross margin: 67%** ($2M gross profit)
- **Target: 80%**

### Option A — Raise Prices (same customers, same cost)
- $1M cost base × 5 = $5M revenue target
- $5M ÷ 50 customers = $100K/customer/yr
- $100K ÷ 12 = **$8,333/mo (up from $5K)**
- Risk: Severe price elasticity shock

### Option B — Add Customers (same price, same cost base)
- $1M × 5 = $5M revenue target
- $5M ÷ $5K/mo ÷ 12 = 83 customers
- **Add 33 customers (66% more) with no new hires**
- Risk: Do you have the operational leverage?

### Option C — High-Ticket Upsell (same cost to deliver)
- **C1:** $10K/mo tier → need 66% take rate to hit 80% GM (unrealistic)
- **C2:** $25K/mo tier → need only **18% take rate** (9 out of 50 customers)
- **C2 is the winning move** because of the fractal nature — 20% will pay 5–10× more

> **"20% of people have 5–10× willingness to pay. Price your upsells accordingly."**

---

## Rejecting Industry Standards

> "Unless the laws of physics prevent it, consider 'industry standards' mental handicaps your competitors get to live by."

**Why to ignore averages:**
- Average business = mediocre
- Successful entrepreneurs reject averages, target physics-and-math limits
- "Industry averages" are a story competitors tell themselves to justify underperformance

Hormozi billionaire mentor: *"Profit is unnatural. When money is there, people spend it. There has to be someone who holds the f***ing line and says we will not spend more."*

---

## Subscription Math — The Equations

### Lifetime Revenue (LTR)
```
LTR = Price ÷ Churn Rate
```
- $100/mo × 10% monthly churn = $1,000 LTR
- $5,000/mo × 5% monthly churn = $100,000 LTR

### Lifetime Gross Profit (LTGP)
```
LTGP = LTR × Gross Margin %
```
- $1,000 LTR × 85% margin = $850 LTGP

### Hypothetical Max Revenue (growth/shrink test)
```
Sales Velocity × LTR = Hypothetical Max Revenue
```
- 30 units/mo × $10K LTR = $300K/mo max stable revenue
- Current $1M/mo + 20 sales × $25K LTR = $500K max → **business is shrinking**
- Current $300K/mo + 20 sales × $25K LTR = $500K max → **business is growing**

### Sales Rep Sizing Example
- Goal: $2M/mo with $2,000 LTR
- Customers needed per month: $2M ÷ $2K = **1,000**
- If each rep closes 10 deals/week (40/mo) → need **25 reps**

---

## The LTV Arms Race Story

Hormozi's consulting call with a trainer competitor in the same fitness/training space:

| Metric | Hormozi (Gym Launch) | Competitor |
|---|---|---|
| CAC | ~$2,500 | ~$2,500 |
| Sales velocity | 50/mo | 50/mo |
| Revenue | ~$3M/mo | ~$300K/mo |
| LTV | ~$60K–$101K | ~$6K |
| Net profit | ~$15M/yr | ~$400K/yr |

**Same auction of attention. Same customer flow. 7× revenue, 60× net profit.**

Starbucks: $15,000 LTV per customer. Generic coffee shop: $2,000.

> "That's not a fair fight. You want to be the guy with the baseball bat."

---

## The Meals Business Story (What NOT to Do)

**Vision:** 1,000 gym partners × 200 customers × 30% conversion × $600/mo = $36M/mo

**Reality:**
- Launched at $600/mo → low demand
- Reset to $10/meal retail, $9 fully-baked cost
- **Gross margin: 10%**

**The trap:** Team said "spend $10 to make $20 back, let's scale."
- True math: $10 CAC × 10% margin = $1 gross profit per dollar spent
- Need to sell 100+ meals just to break even on CAC

**Lesson:** This is how you make $100K+ mistakes in commodity markets. Don't enter a business without knowing gross margin mechanics.

---

## The Gym Launch Tech Support Story

**Setup:** 35-person tech support department. 3-minute response promise. Built because Hormozi thought it showed commitment.

**The survey:**
- "Which single component would you fight hardest for us to keep?"
- "Which single component would you be happiest to see gone?"

**Result:** Tech support was *overwhelmingly* first to go.

**What happened when he cut it:** Nothing. Zero churn impact.

**The real insight:** Customer perception of value ≠ what you built. You probably have costly components that don't move churn. Survey to find them.

---

## The $99 → $299 Gym Case Study

**Before:** $99/mo, 1-to-many group training

**The play:**
- New tier at $299/mo with 1-on-6 to 1-on-8 ratio
- Offered 14-day trial of new tier to existing customers
- Framing: "I realize you need more structured support. This is what I should have offered first."

**Result:**
- 70% retention on new $299 tier
- **3× price × 70% retention = 2× revenue**
- Overhead dropped (lost the cheapest, most problematic 30%)
- Gross margin improved at the same time

**Why it worked:**
- Conviction (Hormozi genuinely believed in the new structure)
- Risk reversal (14-day trial)
- Better service actually delivered better outcomes

---

## The 5 Best Times to Upsell

Upsells work at the **point of greatest deprivation**, not greatest satisfaction. Use all five.

### 1. Immediately (Day 0)
Maximum excitement, maximum buying momentum.
**Script:** *"You just bought X. To get the full experience, most people add Y."*

### 2. 24–48 Hours
Introduce a **new problem** they didn't realize they had.
**Script:** *"Now that you've started, you'll realize [new problem]. We have something for that."*
Example: Gym member → nutrition consultation *("Now you realize diet matters")*

### 3. First Activation Point
The moment of first win. They're in buying-cycle momentum with a new deprivation.
**Script:** *"You got your first win. You're in the cycle. What's next?"*
Example: B2B lead gen → sales training *("Now you have leads, but you need to close them")*

### 4. Halfway Point
Greatest deprivation inside the current program. **~70% of upsell revenue happens here.**
**Happy customer script:** *"How's it going? Great — but you said your goal was [bigger goal]. This gets you halfway. Want to see the full vision?"*
**Unhappy customer script:** *"I misdiagnosed your level of need. You need [higher tier]. First month at [intro price] to make it right."*

### 5. Last Chance / End of Contract
"Abandoned hope" reframe. Reframes short-term success as insufficient for long-term goals.
**Script:** *"You lost 10 lbs but said you wanted 60. That's great — but step 1 of 12. Let's keep going."*

**Important:** Upselling at the END loses ~⅔ of the revenue you'd get at the halfway point because customers have cooled off.

### Upselling Unhappy Customers
Take the blame. Misdiagnose yourself. Offer higher tier with intro price break. Unhappy customers are still *deprived of a solution* → still buyable.

### Classic / Menu / Anchor / Rollover Mapping
- **Classic upsell** → immediate / 24–48 hr
- **Menu upsell** → first activation / halfway
- **Anchor upsell** → immediate (sets framing)
- **Rollover** → last chance (credit their past spending into a bigger program)

---

## The "More of That Thing You Just Bought" Rule

Hormozi proposed a split-test survey against a partner's upsell idea. The result:

**85% preferred "More of that thing you just bought."**

**The two highest-converting upsells of all time:**
1. **More of that thing** (bulk, quantity, frequency)
2. **More help with that thing** (support, quality, acceleration)

Single-issue buyers want MORE of the solution they just bought — not to be taught a new business / new skill / new problem.

---

## Risk / Speed / Ease — The Value Components

Three levers to construct any upsell, premium tier, or offer improvement:

| Lever | Mechanism | Example |
|---|---|---|
| **Risk** | Remove uncertainty, guarantees, proof | 14-day trial, money-back, case studies |
| **Speed** | Compress timeline, priority access | Same-day vs. 2-week wait, priority support |
| **Ease** | Remove friction, concierge, pre-made decisions | White-glove onboarding, done-for-you delivery |

**Components that hit all three** = most compelling upsells.
- AI assistant: instant answers (speed), pre-fitted to you (ease), reduces execution risk (risk)
- Playbooks: get answers fast (speed), don't have to figure out (ease), proven (risk)

Rich people pay most for **speed**.

### The Texting Test
> "Offers should be simple enough to communicate in a single text message. If you have to explain it, cut it."

If a customer asks more questions after reading it, it's too complicated.

---

## The Customer Survey Template (For Cost-Cutting)

**Q1:** Your name + [company/revenue/address]
- Purpose: identify customer tier

**Q2 (Last one standing):** *"If we were forced to remove all but one component, which single one would you fight hardest to keep?"*
- Purpose: find non-negotiable value

**Q3 (First to go):** *"Which single one would you be happiest to see gone? You wouldn't miss it at all?"*
- Purpose: find waste

**How to read the data:**
- **Even distribution:** offer is coherent, don't change
- **Concentration on one:** build business around it
- **High-value customers prefer different components** than low-value: segment offers, or kill the cheap cohort
- **Components only low-value customers care about:** cut them; serve the whales

---

## DFY Pricing Sliding Scale (By Close Rate)

For done-for-you service businesses:

| Close Rate | Pricing Move |
|---|---|
| **80%+** | **3–4× the price** — severely underpriced |
| 60–80% | 2–3× the price |
| 50–60% | ~2× the price |
| 40–50% | 1.25–1.5× |
| 30–40% | Maintain or small raise |
| < 30% | **Don't raise — fix sales first** |

> "You will have 'yes' said to you less often, but you will make more money. More yeses ≠ more money."

Why it works: High price attracts serious buyers (better LTV, lower churn). Low price attracts tire-kickers.

### The Virtuous Cycle of Price
Raise price → better customer → better outcome → better reputation → more demand → raise price.

(This is NOT the race to the bottom strategy.)

---

## "Outcome Minus All Pain" — The Product Framework

> "A great product/service = **Outcome − All Pain**"

The iPhone didn't invent the smartphone. It **removed everything that sucked** about having a phone.

**Process:**
1. Define the outcome
2. Follow customers through the entire journey
3. List every friction / delay / risk / lost opportunity
4. Eliminate them one by one

**"All pain" includes:**
- Friction (what they have to do that they don't want to)
- Lost opportunities (what they have to stop doing)
- Delays (how long they wait)
- Risk (uncertainty they incur)

---

## The Downsell Trap (Full Math)

**Scenario:** 100 qualified leads, $10K core offer
- Standard flow: 60 qualify × 25% close × $10K = **$150K**
- With downsell: 60 qualify × 25% = $150K + 40 DQed × 30% close × $2K = $24K = **$174K (+16%)**

**But compare to raising price:**
- $10K → $12K (+20%). Close rate drops 25% → 23%.
- Result: similar revenue. Sales team NOT distracted. Brand NOT diluted. **Plus** reallocate freed time → close 2 more from existing pipeline = **$188K**

### Why Downsells Destroy Sales Teams
> "The main reinforcer of selling is hearing 'yes,' not making money."

Sales reps will drop to the lower offer the moment they hit price resistance. A $10K sale becomes a $2K sale. **Loss: $8K per converted deal.**

### The Only Exceptions
Downsells work **ONLY when:**
- 100% automated conversion + 100% automated delivery
- Examples: e-commerce, low-ticket SaaS, webinar funnels
- Person-to-person: needs 5× the volume of DQed leads relative to qualified to be worth the complexity

### Better Play: High-Ticket Anchor
Instead of downselling: add a **$50K top tier** anchor. Small volume × huge price > big volume × small price.

---

## The Crazy Eight (8 Ways to Make More Money Per Customer)

1. **Increase price** — raise rate, add tiers
2. **Decrease cost** — productize, offshore, batch, automate
3. **Increase purchase frequency** — reduce churn, create buyback reasons, subscription
4. **Cross-sell** different things (complementary)
5. **Sell more quantity** — bulk, packages, units
6. **Sell more quality** — premium tiers, faster, better provider
7. **Sell fewer** (downsell — only if automated or 5× volume)
8. **Sell worse** (downsell — rare)

### Applied to Physical Therapy
1. Price: $100 → $200+/session
2. Cost: cheaper therapists, AI screening, batch exercises
3. Frequency: 12-week program vs. ad-hoc
4. Cross-sell: massage guns, supplements, orthotics, tape
5. Quantity: 3-month prepay bundle, family packages
6. Quality: premium tier (manual therapy, clinical director, in-home)
7. Downsell: group classes (only if scale volume)
8. Worse: basic digital program

### Applied to Smartphones
1. $100 → $1,200 (iPhone Pro)
2. Vertical integration, optimized manufacturing
3. Family plan, trade-in cycles, subscriptions
4. Cases, insurance, AppleCare, apps
5. Family packs, corporate bulk
6. Pro / Pro Max tier escalation
7. iPhone SE
8. Smaller storage, fewer features

---

## Avatar Strategy — Whales vs. Minnows

**The SMMA trap:** Social Media Marketing Agencies often stuck at $1M–$5M because they serve volatile SMBs. SMB volatility → churn → margin compression.

**The barbell strategy:**
- **Very expensive** service to a few high-value clients (20–50 whales), OR
- **Very inexpensive, highly scalable** ($300–$400/mo) to many

**Avoid the middle.** The middle gets crushed between both.

> "Your goal should be to acquire 20–50 whales, not 3,000 minnows. Selling to fewer people does not reduce business value IF revenue retention, growth, and gross margin are all high."

Metrics priority: **RoAS / LTV-to-CAC > CPC / CPL.**

Be willing to say NO to bad customers.

---

## Offer Components & Loss Leaders

### Single-Issue Buyer Principle
**Every component of an offer must be valuable enough to justify the entire price on its own.**

If each component can't stand alone, you have fewer real reasons to buy — buyers focus on one thing.

### Fewer Better
**4 or fewer components.** Mental real estate kills conversions. Simplify the decision.

### Loss Leaders
> "3 hardback books for $15 — shipping included. **10× higher conversion than any offer I've ever seen in my life.**"

Tangible cost the customer can calculate. Drastically lowers perceived CAC.

### Avoid Discounts
Discounts **decrease LTV by ~40%** and attract a different, lower-value customer.

### Lead Magnets Change LTV
The lead magnet selects the customer type. High-friction scaling roadmap → different lead than free book → different LTV cohort.

---

## Onboarding Mechanics (The 5 Things That Matter)

1. **Quick win** within 7 days (material victory, not end goal) — proves the thing works
2. **Personalized welcome** — intro video, personal message, customized checklist
3. **Day 1–14 checklist** — map the activation journey step-by-step
4. **Human touch within 48 hours** — first call / message / video from a real person
5. **Proof of similar success** — reinforce the decision post-purchase

> "The first 24 hours after purchase is when customers judge whether they made the right call."

---

## Communication Cadence

```
Long-term nurture (soft CTAs, value content, weekly)
           ↕
Quarterly promotions (2–4×/year, fast-cash plays)
           ↕
Community (top-of-mind, peer validation)
```

Email revenue share (Hormozi's benchmarks):
- Acquisition.com: ~20% of total revenue from Mosy Minute nurture
- Typical business that takes email seriously: 25–50% achievable
- It's **free** (no ad spend). Drops straight to profit.

---

## Reframing Commodity Pricing

"My market is commoditized" is usually wrong. Reframe what you're selling.

- **HVAC / Chiropractic:** don't sell the service — sell a **wellness program** or **home improvement plan**
- **Home services:** reframe price from "local" cost (up-front) to **"global" cost** (long-term savings + higher quality)
- **Commodity products:** wrap in giveaways, loss leaders, or bundled programs

Low-cost leadership is a completely different business model. Don't stumble into it. Build for it from day one — or avoid it.

---

## Cost-Cutting Tactics (Decreasing COGS)

**Knowledge services:**
- **Employee-to-customer ratio** — semi-privates instead of 1-on-1
- **Offshore non-in-person talent** (most ops, admin, design work)
- **Tier delivery** — use cheaper staff for routine tasks
- **Narrow the avatar** ($750K–$3M biz) → productize delivery
- **Shift DFY → DWY** (done-with-you) → customer does more of the work
- **Service guard-rails** — guarantees tied to adherence

**Automation & batching:**
- Break jobs into smaller chunks → automate the chunks (not the whole job)
- **Batch work** — Fridays = X type of work (team efficiency)
- **Sync → async** communication = **60–80% team time savings**

---

## Punchy Quotes to Retain

> "The bigger your business, the fewer things you'll be able to execute. You only need one or two ideas from this workshop to ROI it many times over."
> "You can only grow the business by selling more customers or making them worth more. That's it."
> "He who can spend the most to acquire a customer wins. There are two wars: get customers for free OR make so much money from customers that acquisition cost is irrelevant."
> "Pricing is fractal. The more people make, the more they can afford to pay."
> "Unless the laws of physics prevent it, consider industry standards mental handicaps your competitors get to live by."
> "You will have yes said to you less often — and you will make more money. More yeses ≠ more money."
> "If you're closing 80%+, you're probably underpriced 3–4×. Change nothing about the offer. Multiply your price by three."
> "A downsell doesn't work because sales reps drop to the lower offer on price resistance. The main reinforcer of selling is hearing yes, not making money."
> "Starbucks makes $15K LTV per customer. Generic coffee shop makes $2K. That's not a fair fight. You want to be the guy with the baseball bat."
> "Loss leaders are unbelievably powerful. 3 books for $15 shipping included — 10× higher conversion than any offer I've ever seen."
> "If many variables exist, many variables must be studied." — BF Skinner
> "Gross margin is a percentage. Gross profit is a number. Language matters."
> "Profit is unnatural. There has to be someone who holds the f***ing line and says we will not spend more, we will keep making more." — A billionaire mentor
> "The time customers judge your product is the first 24 hours. You can blow them away, or they can be underwhelmed."
> "A great product/service = outcome minus all pain."

---

## Anti-Patterns (I See This All The Time)

1. **"We're meeting industry standards"** — mediocrity's polite cousin
2. **Downsells that destroy the core offer** — reps drop $10K to $2K on price resistance
3. **Bloated offers** — 9 components when 4 would win
4. **Growing without knowing LTGP** — flying blind, margin compresses invisibly
5. **Discounting first when demand softens** — attracts worse cohort, drops LTV 40%
6. **Upselling at end of contract** — ⅔ less revenue than upselling at halfway
7. **Not tracking churn** — can't calc LTV, can't forecast revenue ceiling
8. **Same price across tiers** — no perceived distinction, might as well have one offer
9. **Building all 5 monetization layers at once** — Shopify took 20 years; budget years, not weeks
10. **Assuming customers know what they want** — survey them; they'll tell you what to keep AND cut
11. **Maintaining a costly component out of pride** — Hormozi's 35-person tech team; zero churn impact when cut
12. **Stuck in the middle avatar** — neither whale-pricing nor commodity-scale. Barbell or lose.
13. **Using CPL / CPC as primary metric** — use ROAS / LTV-to-CAC instead
14. **"Yes-chasing"** as sales culture — more yeses ≠ more money

---

## How to Use This Reference

When diagnosing an LTV / monetization problem:

1. **Know the baseline** — do they know their LTGP? Their gross margin? Their churn? If not, stop and calculate first.
2. **Run the arithmetic** — LTR = price / churn; hypothetical revenue = velocity × LTR; gross margin gap to 80%
3. **Identify the lever** — is it price (Option A), volume (B), or tier architecture (C)?
4. **Check the avatar** — whales, minnows, or stuck in the middle?
5. **Apply the Crazy Eight** — which of the 8 has the highest risk-adjusted return based on existing skills?
6. **Design upsell timing** — are they capturing all 5 deprivation windows?
7. **Flag the traps** — downsells, discounts, middle-avatar, bloated offers, industry-average thinking

### Pair This Reference With
- **`money-models.md`** — the *construction* side (attraction / upsell / downsell / continuity playbook)
- **`offers.md`** — Value Equation, Grand Slam Offer, pricing anchoring
- **`sales-workshop.md`** — the sales-ops side (VSLs, follow-up, team ops)
- **`marketing-workshop.md`** — when the constraint is traffic, not LTV
- **`launch.md`** — for time-bounded LTV plays (VIP tiers, OTOs)

**Citations:** [Hormozi ACQSA LTV Workshop, 2025-12-05]
