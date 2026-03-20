---
name: growth-strategy
description: Applies Growth Strategy frameworks to any strategic growth problem. com essays (Why Figma Wins, Aligning Business Models to Markets, Making Uncommon Knowledge Common, Notes on Superhuman's Acquisition Loops) and Casey Winters' caseyaccidental.com writing (When Growth Plateaus, The Monetization Playbook, Every Product Starts in Oklahoma). Activates when asked about growth strategy, loop sequencing, market structure, business model alignment, channel layering, monetization strategy, network effects, platform strategy, or how to think about the next phase of growth. Triggers proactively when discussing your product's strategic direction, competitive positioning, channel decisions, or pricing and packaging — especially if growth is plateauing or a new growth phase is being considered.
---

**Reference files:**
- `references/kwok-frameworks.md` — Loop sequencing, structural alignment, network effects, platform strategy
- `references/winters-frameworks.md` — Channel layering, monetization, Sooners/Missourians, feature pricing
- `references/loop-sequencing-playbook.md` — The full loop sequencing decision system

---

## How to Use This Skill

When this skill activates:
1. Identify which strategic growth framework best applies to the question (loop sequencing, structural alignment, channel layering, or monetization)
2. Apply the relevant decision tree from the Decision Tools section
3. Ground all recommendations in the context of your product
4. Cite the specific framework when making claims
5. If deeper detail is needed, read the relevant reference file before responding

## Gotchas

Common mistakes to avoid when applying these frameworks:

1. **Optimizing the current loop past its ceiling instead of sequencing into the next one:** Kwok's central insight is that most companies fail because they try to squeeze more from a capped loop. When top experiments return less than 5% improvement, the loop has hit its invisible asymptote -- the answer is building the next loop, not running more experiments on the current one.
2. **Recommending a channel because it worked for a different company:** Winters warns that your first channel was chosen for a reason -- it was structurally optimal for your product. Adding a new channel only works when something has changed (LTV increased, UGC volume grew, product bundle expanded). Without a structural change, a new channel adds 5-10% at best.
3. **Treating Sooners feedback as representative of the mainstream market:** Sooners (early adopters) tolerate rough edges and give enthusiastic feedback. Missourians (mainstream users) need proof and social validation from peers. Designing your product's growth strategy around power-user feedback will miss the adoption barriers that prevent mainstream audiences from converting.
4. **Building a data content loop without the information asymmetry:** The Rich Barton playbook only works when there is genuinely uncommon knowledge to make common. For your product, generic generic content are not uncommon knowledge -- but curated guidance for specific use cases is underserved and defensible.

## Example

**User asks:** "Should your product invest in building a content/SEO growth loop?"

**Approach:**
1. Apply Kwok's loop sequencing framework: identify your product's current primary loop (likely app store + paid UA), assess whether it is approaching its invisible asymptote, and evaluate whether a content/SEO loop is the correct next loop to sequence into
2. Evaluate using the Data Content Loop criteria: does your product have genuine information asymmetry (curated content for specific situations) and is there search volume for these topics?
3. Apply Winters' channel layering prerequisite check: what has your product's scale unlocked that makes content/SEO viable now when it was not before (content library depth, domain authority, user-generated engagement data)?
4. Output a sequencing recommendation with the specific loop type, ceiling estimate, prerequisites to build, and timeline -- citing both Kwok's structural alignment framework and Winters' channel layering prerequisites

---

## Core Mental Model: Companies Are a Sequencing of Loops

> "Companies are a sequencing of loops. While it's possible to stumble into an initial core loop that works, the companies that are successful long-term are the ones that can repeatedly find the next loop." — Kevin Kwok

Growth strategy is not about optimizing a single loop forever. It's about:
1. Understanding the **structural forces** that make your current loop work
2. Identifying the **invisible asymptote** where that loop will cap out
3. Sequencing into the **next loop** before the current one plateaus

Most companies fail at step 3 — they try to optimize the current loop past its ceiling instead of building the next one.

---

## Framework 1: Structural Alignment of Business Models to Markets

*Source: "Aligning Business Models to Markets," kwokchain.com*

> "Never attribute to stupidity or malice that which can be adequately explained by structural alignment of incentives."

The central insight: **market structure determines which business models win**. When market dynamics shift, new business models emerge and old ones erode. Companies that understand the structural forces shaping their market can align their business model to ride those forces — rather than fighting them.

**The pattern:**
```
Structural shift in market
        ↓
New constraints / opportunities emerge
        ↓
New business model becomes optimal
        ↓
Companies aligned to new model win; old incumbents struggle
```

**Examples:**
- Gaming: ubiquitous internet → multiplayer viable → network effects drive utility → free-to-play + IAP beats paid upfront
- Productivity (Figma/Notion/Airtable): browser-first → frictionless collaboration → bottoms-up PLG beats top-down enterprise sales
- Restaurants (USHG/Shake Shack): Yelp + social → informed consumers → service quality creates differentiation → farm-club employee model becomes viable

**Key questions to diagnose structural alignment:**
1. What structural shifts have happened in our market in the last 3–5 years? (internet penetration, platform changes, regulation, demographics)
2. What new constraints or opportunities have those shifts created?
3. Which business models are newly advantaged by those shifts? Are we one of them?
4. What does the *next* structural shift likely look like, and which model will it advantage?

**For your product:**
- Structural shift: consumer habits shifted digital; daily habit apps normalized (Headspace, Duolingo); subscription fatigue increasing
- New opportunity: similar content has historically been free; your product can be the first to create a premium daily habit worth paying for
- Emerging shift: AI enables personalized personalized content at scale; first mover here could create a defensibility loop

---

## Framework 2: Data Content Loops — The Rich Barton Playbook

*Source: "Making Uncommon Knowledge Common," kwokchain.com*

The most underutilized growth loop in consumer tech. Used by Expedia, Zillow, and Glassdoor to dominate search and own demand in their categories.

**The playbook:**
1. Identify **information asymmetry** — knowledge that exists but is hoarded by intermediaries or hard to aggregate
2. Make that uncommon knowledge **common and public** — become the Schelling Point for that information
3. Use that content to **dominate search** — create a page for every entity in the category
4. Scale into a **trusted brand** — own demand before customers are even ready to buy

**Why it works:**
- Creates a content moat that compounds over time
- SEO/direct traffic → near-zero marginal CAC at scale
- Common knowledge creates its own network effect: the more people trust and use it, the more legitimate it becomes

**The Data Content Loop:**
```
Collect/generate unique data
        ↓
Create content for every entity in the category (house, company, hotel)
        ↓
Rank in search for every query in that category
        ↓
Users find content → engage → contribute more data
        ↓
More data → better content → better rankings
        ↑___________________________________|
```

**Good candidates for this loop:**
- Categories with information asymmetry between buyers and sellers/intermediaries
- Low-frequency decisions where people research before acting (real estate, jobs, travel, healthcare)
- Topics people talk about but can't easily verify (salaries, reviews, valuations)

**For your product:**
- Opportunity: content for specific situations ("content for anxiety," "content for grieving," "content for relationships") is highly searched but poorly served
- A data content loop could index every content topic → rank for every relevant query → pull in users who aren't yet paying → convert into subscribers
- This is an underexplored moat that pure app-store competitors can't easily replicate

---

## Framework 3: Loop Sequencing — The Strategic Arc

*Source: "Why Figma Wins," kwokchain.com*

Every loop has a ceiling — Kevin Kwok calls this the **invisible asymptote** (coined by Eugene Wei). The strategic imperative is to sequence into the next loop *before* the current one hits its ceiling.

**Figma's sequencing:**
```
Phase 1: Direct network effects (designers invite designers within a team)
         → Asymptote: limited by how many designers work together directly

Phase 2: Cross-side network effects (designers pull in PMs, engineers, CEOs)
         → Asymptote: limited to within-company spread

Phase 3: Global network effects (Communities + Plugins)
         → Ecosystem compounds across companies
```

**The sequencing principle:**
- Early loops are often **social capital loops** — fast to ignite, fast to cap out
- Mid-stage loops are often **network effect loops** — slow to start, high ceiling
- Late-stage loops are often **platform/ecosystem loops** — require structural bets early to unlock later

**Types of loops ranked by ceiling height:**

| Loop type | Speed to ignite | Ceiling | Defensibility |
|-----------|----------------|---------|---------------|
| Social capital / WOM | Fast | Low | Low |
| Content / SEO | Medium | Medium | Medium |
| Viral / referral | Fast | Medium | Low-medium |
| Direct network effects | Slow | Medium | High |
| Cross-side network effects | Slow | High | High |
| Data flywheel | Medium | Very high | Very high |
| Platform / ecosystem | Slow | Highest | Highest |

**The sequencing rule:** Start with what can ignite quickly (social capital, referral, content) to reach the minimum viable scale needed to light the next loop (network effects, data flywheel, platform).

**Superhuman's sequencing challenge:**  
Social capital loop ignited fast → but email is interoperable → no personal utility network effect → must sequence into intra-team features to build the higher-ceiling loop.

**For your product sequencing:**
```
Current: App store + paid UA + viral sharing (social capital loop)
Next: Content/SEO loop (topic pages → organic search dominance)
Then: Community/social loop (community groups, accountability partners, community integration)
Then: Platform/data loop (personalized content AI trained on user usage patterns)
```

---

## Framework 4: Good Friction

*Source: "Notes on Superhuman's Acquisition Loops," kwokchain.com*

> "Good friction looks like it hurts its step of the loop, but it net improves the entire loop."

Counter-intuitive principle: adding friction at one step can improve total loop output if it:
- Pre-qualifies users (improves conversion and retention downstream)
- Creates delight that triggers sharing (improves referral)
- Builds investment that reduces churn (improves LTV)

**Superhuman example:** Manual onboarding call with every user. Looks like massive friction at sign-up. Actually: increases delight, reduces churn, creates brand moments that drive Twitter/WOM acquisition. Net effect is positive on the full loop.

**Test for good friction:**
1. Does it reduce volume at this step?  → Yes (it's friction)
2. Does it improve quality at this step? → Usually yes
3. Does the quality improvement compound into downstream loop steps? → If yes = good friction

**For your product:** A guided onboarding that asks "what are your goals?" and sets a specific first engagement session — more friction than a generic sign-up, but far higher activation and habit formation. Good friction.

---

## Framework 5: Sooners vs. Missourians

*Source: "Every Product Starts in Oklahoma," caseyaccidental.com*

> "Every product starts in Oklahoma. Every successful one eventually crosses into Missouri."

Two fundamentally different user types require fundamentally different products:

| | Sooners (early adopters) | Missourians (mainstream) |
|---|---|---|
| **Motivation** | Social status, curiosity, being early | Financial return, risk reduction, proof |
| **Feedback style** | Engaged, exploratory, tolerant of rough edges | Rational, gap-focused, non-committal |
| **What they need** | Vision + potential | Evidence + infrastructure |
| **Signal value** | High for PMF, low for scale | Low for PMF, high for scale |

**The trap:** Missourians *look* valuable. They give articulate feedback. Founders chase their notes. But closing the gaps Missourians identify doesn't move the needle because Missourian *adoption* is driven by social proof from their peers — not by feature completeness.

**Crossing the chasm = rearchitecting motivations:**
- Social capital → financial capital
- Attention → income  
- Play → business
- "I want to be early" → "Show me the money / show me the ROI"

**All user behavior falls into three motivations:**
- **Social:** helps me signal identity or status
- **Financial:** helps me make or save money
- **Personal utility:** makes my life meaningfully easier or better

Sooners buy on social. Missourians buy on financial or personal utility proof.

**For your product:**
- Current users are likely Sooners: motivated early adopters who want daily engagement structure
- To cross into Missouri: need proof that the app creates measurable personal growth, community belonging, or life change — something Missourians can point to as evidence

---

## Framework 6: Channel Layering

*Source: "When Growth Plateaus: How and When to Layer on New Acquisition Channels," caseyaccidental.com*

> "It is unlikely you just dramatically missed an important channel early on. Your first channel is likely that channel for a reason: it was the most optimal one."

Growth plateaus are not solved by stacking more channels. They're solved by asking: **what has my scale now unlocked that wasn't possible before?**

**The four acquisition channels:**

| Channel | Scales because... | Prerequisite to unlock |
|---------|------------------|----------------------|
| **Virality** | Users tell users | Product has shareable moment; social/financial/personal incentive to share |
| **Sales** | Compensation manages payback | LTV big enough to support salesperson salary + commission |
| **Paid acquisition** | LTV funds more ads | LTV:CAC > 3:1; payback period < 12 months |
| **Content** | Volume compounds in SEO/social | Users generate content; critical mass of UGC to index |

**The channel sequencing question:**  
Before adding a new channel, ask:
1. Has my LTV improved enough to support a new CAC ceiling?
2. Has my content/UGC base grown enough to distribute?
3. Has scale improved conversion enough that expensive channels are now viable?
4. Has product breadth changed the unit economics?

If none of those have changed, adding a new channel will add at most 5–10% growth, not the 3–10× you need.

**Engagement loops that compound:**  
Layering engagement on top of acquisition unlocks higher-ceiling channels:

| Type | Mechanism |
|------|-----------|
| **People** | Direct employee → user touch; viable when LTV increase > cost |
| **Product** | Features that increase frequency of use |
| **Incentives** | Financial, utility, social rewards for deeper usage |
| **Messaging** | Notifications, emails, texts that bring users back |

**For your product:**
- Current channel: likely app store + paid social
- What scale has unlocked: if daily completion rates are high → evidence for content/SEO (high-intent personal search)
- What would unlock sales: community partnerships (B2B2C) require higher ACV — bundle pricing for teams
- What would unlock virality: "share today's engagement" or "community request" social features embedded in product

---

## Framework 7: Monetization Decision Framework

*Source: "The Monetization Playbook We Used at Eventbrite," caseyaccidental.com*

For every feature or product, ask before building:

**Step 1: What does it drive?**
```
Does it drive virality?
  → Yes: Give it away free (virality expands the denominator)

Does it drive activation to long-term retention?
  → Yes: Give it away until activation is achieved

Does it drive lifetime value?
  → Yes: Compare LTV gain vs. willingness to pay
       → Charge if WTP > opportunity cost of paywalling it

Does it drive none of the above?
  → If WTP exists → charge for it
  → If no WTP → evaluate cost to support; sunset if cost > value
```

**Step 2: If charging, how?**

The 2×2 for packaging:

```
                    High usage        Low usage
                ┌─────────────────┬─────────────────┐
High WTP        │  Core tier /    │  Add-on or      │
                │  anchor value   │  premium bundle  │
                ├─────────────────┼─────────────────┤
Low WTP         │  Include in     │  Don't build or  │
                │  base plan      │  sunset          │
                └─────────────────┴─────────────────┘
```

**The packaging trap:** A-la-carte pricing every feature creates toothpaste-aisle complexity. Bundle into tiers. Use the 2×2 to decide what anchors each tier.

**The default to ship problem:** Teams that default-ship every feature to all tiers destroy monetization leverage over time. Every new feature should ask: "Does this improve the value of our premium tier, or just raise the floor?"

---

## Decision Tools

### Is my growth plateau a loop problem or an optimization problem?

```
Have you run significant experiments on the current loop in the last 90 days?
  → No → Optimize first; you may not be at the ceiling yet

Are your best experiments returning <5% improvement?
  → Yes → You're near the loop's asymptote

Has the market structure shifted? (new competitors, platform changes, pricing pressure)
  → Yes → Revisit structural alignment; loop may be broken, not just capped

If at asymptote → What loop can you sequence into next?
  (See loop sequencing table above)
```

### Is this a channel worth adding?

```
What has changed since we picked our first channel?
  → LTV increased? → Higher CAC channels now viable
  → UGC volume grew? → Content/SEO loop may be ready
  → Product bundle expanded? → New use cases open new channels
  → Scale improved conversion? → More expensive channels turn profitable

Nothing has changed → Don't add the channel yet; invest in what will change these inputs
```

### Am I talking to Sooners or Missourians?

```
User gives you detailed gap analysis → Likely Missourian
User is excited despite rough edges → Likely Sooner
User asks "how does this make me money / save me money" → Missourian
User asks "what's next / what are you building" → Sooner
User churned without giving feedback → Missourian (needed more proof)
User became a power user despite missing features → Sooner
```

### Should I charge for this feature?

```
Drives virality? → Free
Drives activation? → Free until activated
Drives LTV? → Charge if WTP > LTV opportunity cost of paywalling
None of the above? → Charge if WTP; sunset if no WTP and costly
```

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **Invisible asymptote** | The ceiling every loop eventually hits; identified when top experiments return <5% |
| **Loop sequencing** | Deliberately transitioning from one growth loop to the next before hitting the asymptote |
| **Structural alignment** | When your business model is naturally suited to the structural forces shaping your market |
| **Data content loop** | Aggregating unique data to create content that dominates search and owns demand |
| **Cross-side network effect** | Network effect between two distinct user types (e.g., designers ↔ non-designers in Figma) |
| **Social capital loop** | Growth driven by users sharing because it enhances their status/identity, not because of personal utility |
| **Good friction** | Friction that hurts one loop step but improves total loop output |
| **Sooners** | Early adopters motivated by social capital and curiosity; tolerant of rough edges |
| **Missourians** | Mainstream users motivated by financial return and risk reduction; need proof |
| **Schelling point** | A focal point of common knowledge; becoming one creates durable demand ownership |

---

## Read Next

- `references/kwok-frameworks.md` — Full depth on structural alignment, data content loops, Figma loop sequencing, social capital acquisition
- `references/winters-frameworks.md` — Full depth on channel layering, monetization 2×2, Sooners/Missourians
- `references/loop-sequencing-playbook.md` — Step-by-step system for identifying your current loop ceiling and building the next one
