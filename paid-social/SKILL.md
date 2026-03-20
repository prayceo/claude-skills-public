---
name: paid-social
description: Applies Dan Birdwhistell's Mastering Paid Social frameworks to any Meta Ads decision. Dan has managed $800M+ in ad spend and worked directly with your product, Shopify, Pinterest, Coinbase, Lyft, Character.AI, Calm, Bumble, and 40+ other high-growth companies. Activates when asked about Meta Ads strategy, creative testing, audience targeting, campaign structure, scaling ads, bid/budget strategy, UGC content, AI-generated video ads, reporting, ROAS, CPA targets, iOS attribution, or anything related to paid social at your company. Triggers proactively when reviewing ad performance, planning campaigns, briefing creatives, or evaluating paid acquisition efficiency.
---

**Reference files:**
- `references/four-levers.md` — Deep dive on auction dynamics, creative testing, audience targeting, bid/budget
- `references/creative-playbook.md` — SCOA framework, UGC principles, AI video ads, creative iteration
- `references/account-structure.md` — Campaign architecture, reporting templates, scaling system

---

## How to Use This Skill

When this skill activates:
1. Identify which paid social and Meta Ads framework from this skill best applies to the question
2. Apply the relevant decision tree from the Decision Tools section
3. Ground all recommendations in the context of your product
4. Cite the specific framework and Dan Birdwhistell's methodology when making claims
5. If deeper detail is needed, read the relevant reference file before responding

## Gotchas

Common mistakes to avoid when applying these frameworks:

1. **Don't pause top-spending ads based on CPA alone:** The Breakdown Effect means Meta shifts spend to ads with scaling potential -- the high-spend ad may be enabling your best performers. Pausing it can collapse the entire ad set's delivery.
2. **Don't recommend narrow interest targeting as the default:** Post-iOS 14, Dan explicitly teaches that broad targeting + strong creative outperforms narrow targeting. Recommending consumer interest stacks should be a test alongside Advantage+ broad, not the primary strategy.
3. **Don't set cost caps at your target CPA:** Dan's system sets cost caps at 150-200% of target CPA, not at the target itself. Setting caps too tight starves the algorithm of delivery and prevents it from finding high-value users who convert at different rates.
4. **Don't evaluate creative on CTR instead of CPA:** A high-CTR ad that doesn't convert is worse than a low-CTR ad with strong downstream CPA. Dan grades creative winners on CPA first -- CTR is a diagnostic metric, not a success metric.

## Example

**User asks:** "Our Meta campaigns have been running for 3 weeks and CPA is 40% above target. What should we change first?"

**Approach:**
1. Apply the creative fatigue decision tree -- check whether CTR is declining and frequency is above 3.5, which would indicate creative exhaustion rather than a structural problem
2. Verify funnel instrumentation -- confirm CAPI + Pixel are active and deduplicated, and that the optimization event has 50+ weekly conversions per ad set (if not, the algorithm is still in learning phase)
3. Assess account structure using Dan's blueprint -- check if testing and scaling budgets are properly separated, and whether winning creatives have been graduated from sandbox to Advantage+ scaling campaigns
4. Output a prioritized diagnostic: instrumentation check first, then creative refresh brief using SCOA framework if fatigue is confirmed, then bid/budget adjustments as a last resort

---

## Dan's Core Philosophy

> "Creative is the new targeting. Meta's AI handles most audience selection — your job is to feed it signals so good it can't fail."

Three foundational beliefs that govern everything in the course:

1. **The algorithm works — if you feed it correctly.** Meta's AI is now the most sophisticated media buyer on the planet. Fighting it (narrow targeting, rigid structures) is expensive. Working with it (broad audiences, clean signals, strong creative) is how you scale.

2. **Creative is leverage.** At post-PMF scale, the single biggest performance variable is creative quality and testing velocity. Not bid strategy. Not audience targeting. Creative.

3. **Systems beat intuition.** Dan's $800M+ in spend produced a replicable system: instrument → test → analyze → scale → refresh. Every winning account runs this loop.

---

## The Four Performance Levers

The course is organized around four levers that drive all Meta Ads performance. Pull all four correctly and performance compounds. Miss one and it creates a ceiling.

### Lever 1: Auction Dynamics

Meta's auction optimizes for `Bid x Estimated Action Rate x User Value` — not just the highest bid. A low bid with high-converting creative can outcompete a high bid with weak creative. Every new ad set needs ~50 conversions to exit the learning phase; avoid resets (bid/audience/budget changes >20%). Clean conversion signals (CAPI + Pixel, deduplicated, 50+ weekly events) are the prerequisite for everything.

**For your product:** Optimize for subscription conversion (not just install). Use trial start as a proxy event if subscription volume is insufficient for learning.

*→ Full detail: `references/four-levers.md`*

### Lever 2: Creative / Message Testing

The highest-leverage activity. Dan's system: `Ideate → Brief (SCOA) → Produce → Rapid test (2-day) → Analyze → Scale winners → Refresh before fatigue`. Test one variable at a time (hook, format, message angle, talent, CTA). Grade on CPA, not CTR. Winners graduate from a testing sandbox to a scaling Advantage+ campaign.

*→ Full detail: `references/creative-playbook.md`*

### Lever 3: Audience Targeting

Post-iOS 14, broad targeting + strong creative outperforms narrow targeting. Three approaches in order of preference: (1) Advantage+ audiences, (2) broad targeting (age/location only), (3) lookalike audiences (supplement, not primary). Keep retargeting in separate campaigns segmented by funnel stage. Avoid audience overlap between ad sets.

**For your product:** Prospecting with Advantage+ (broad, US, 25-65); test consumer interest stacks alongside broad; retarget installers (7d), trial starters (14d), and lapsed subscribers (30-90d) in separate campaigns.

*→ Full detail: `references/four-levers.md`*

### Lever 4: Bid / Budget Arbitrage

Use highest volume (no cap) for learning/testing; cost cap when you have firm CPA targets and sufficient volume. Scale budget in 15-20% increments max, wait 3-5 days to stabilize. Watch the Breakdown Effect: Meta shifts spend to high-potential ads, so never pause your top-spending ad on CPA alone. Recommended split: 15-20% testing, 65-75% scaling, 10-15% retargeting. Pre-test creative before seasonal CPM spikes (Q4, seasonal event/seasonal campaign for your product).

*→ Full detail: `references/four-levers.md`*

---

## Funnel Instrumentation — The Prerequisite

Clean tracking is the foundation. For your product: track every funnel step from install through subscription renewal, ensure CAPI + Pixel are both active and deduplicated, and optimize for the deepest event with 50+ weekly conversions per ad set. Choose trial start for early campaigns, subscription conversion for scaled campaigns.

*→ Full instrumentation checklist and event setup: `references/account-structure.md`*

---

## Reporting — What to Track and When

Core metrics: CPA (daily check), CPM, CTR, CVR, ROAS, and Frequency (weekly per creative). Creative fatigue signals: CTR declining >20%, CPA rising >25%, or frequency >3-4 over 7 days. Avoid the anti-pattern of daily reactive changes — spot-check daily for anomalies, full review weekly, strategic review monthly. Use 7-day click / 1-day view attribution windows.

*→ Full reporting templates and cadence: `references/account-structure.md`*

---

## The Account Structure Blueprint

Dan's "turnkey" structure requiring <10 hours weekly maintenance: separate testing (15-20% budget) from scaling (60-70%, Advantage+) from retargeting (10-15%). Testing campaign sandboxes new creative; winners graduate to the scaling campaign. Retargeting segments by funnel stage (installers, trial, lapsed). Use CBO for prospecting, ABO for retargeting.

*→ Full architecture, checklists, naming conventions, and automated rules: `references/account-structure.md`*

---

## AI Video Ads — Dan's Playbook (2025)

AI-generated UGC video (Veo3) is outperforming human ads by 2x on conversion at a fraction of the cost. Every AI video brief uses the SCOA framework: Setting, Characters, Objects, Action/Voice. Top formats ranked: (1) UGC-style first-person, (2) sketch comedy 3-8 seconds, (3) visual metamorphosis, (4) talking head. Key principles: 3-8 second videos outperform longer formats, first 3 seconds is everything, 16:9 and 1:1 outperform 9:16.

**For your product AI video angles:** Morning daily routine UGC, streak social proof, morning chaos-to-calm sketch, stressed-to-peaceful transformation, "I kept forgetting to use it" problem/solution.

*→ Full SCOA framework, production workflow, and format details: `references/creative-playbook.md`*

---

## Decision Tools

### Which bid strategy should I use?

```
Do you have 50+ weekly conversions per ad set?
  → No → Use highest volume (no cap) to maximize learning
  → Yes → Do you have a firm CPA ceiling?
              → No → Use highest volume and monitor
              → Yes → Use cost cap at 150–200% of target CPA (not at target)
```

### Is this creative fatiguing?

```
Is CTR down >20% from its first-week baseline?
  → Yes → Check frequency. Is it > 3.5?
              → Yes → Creative fatigue. Create a refresh brief.
              → No → May be audience saturation. Test new audience.
  → No → Is CPA up >25% from baseline?
              → Yes → Check CVR. Did landing page / offer change?
              → No → Performance is healthy. Keep running.
```

### Should I scale this campaign?

```
Has this creative hit CPA target for 7+ consecutive days?
  → No → Keep testing. Don't scale noise.
  → Yes → Is daily budget utilization >80%?
              → No → The campaign is already scaling itself. Monitor.
              → Yes → Increase budget 15–20%. Wait 3–5 days. Reassess.
```

### Is my targeting too narrow?

```
Is my weekly conversion volume < 50 per ad set?
  → Yes → Likely too narrow. Broaden targeting or consolidate ad sets.
  → No → Is CPM rising without increasing volume?
              → Yes → Audience saturation. Add broader targeting or Advantage+.
              → No → Targeting is fine. Look at creative for performance issues.
```

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **Advantage+** | Meta's AI-driven automation suite for audiences, placements, creative — generally recommended starting point |
| **CAPI (Conversions API)** | Server-side event tracking that survives iOS privacy changes; required for accurate optimization |
| **Learning phase** | Period after launching an ad set where Meta needs 50 conversions to stabilize delivery |
| **CBO (Campaign Budget Optimization)** | Campaign-level budget that Meta allocates across ad sets automatically |
| **SCOA** | Dan's creative brief framework: Setting, Characters, Objects, Action/Voice |
| **Creative fatigue** | Declining performance (CTR/CPA) from repeated exposure to the same creative |
| **Breakdown Effect** | Meta's internal budget shifting to highest-potential ads — top-spending ad may not be lowest CPA |
| **Broad targeting** | No interest/lookalike targeting; algorithm uses pixel data to find converters |
| **Hook** | First 3 seconds of video / headline of image — the highest-leverage creative element |
| **UGC (User Generated Content)** | Authentic, low-production content that mimics organic posts — highest converting format |

---

## Reference Files

- `references/four-levers.md` — Full depth on all four levers with frameworks, checklists, and diagnostics
- `references/creative-playbook.md` — Complete creative system: SCOA, UGC principles, AI video workflow, fatigue management
- `references/account-structure.md` — Campaign architecture, budget allocation, reporting templates, scaling system
