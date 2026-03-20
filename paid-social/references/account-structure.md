## Contents
- The Turnkey Account Structure
- Campaign Architecture Blueprint
  - Full Account Structure
  - Why This Structure Works
- Campaign Setup Checklists
  - New Campaign Launch Checklist
- Naming Conventions
- Reporting System
  - The Weekly Performance Report (Dan's Template)
  - Reporting Frequency and Depth
- Scaling Decision Framework
  - When to Scale a Creative
  - When to Pause a Creative
  - When to Refresh a Creative
- Automated Rules Setup
- Common Account Audit Findings
- Funnel Instrumentation — The Prerequisite

---
# Account Structure & Reporting — Deep Reference
*Source: Dan Birdwhistell's course framework + $800M in managed Meta ad spend across 40+ companies*

---

## The Turnkey Account Structure

Dan's goal: an account structure that produces consistent results with **less than 10 hours of weekly maintenance**. This requires:
1. Clear separation of testing and scaling
2. Minimal campaigns that don't compete with each other
3. Automated rules for routine decisions
4. Weekly reporting cadence that surfaces only what matters

---

## Campaign Architecture Blueprint

### Full Account Structure

```
META AD ACCOUNT
│
├── PROSPECTING — SCALING [60–70% of budget]
│   └── Campaign: [Brand] Scale | Advantage+ | CBO
│       └── Ad Set: Broad / Advantage+ Audience
│           ├── Ad: [Winning creative 1]
│           ├── Ad: [Winning creative 2]
│           ├── Ad: [Winning creative 3]
│           └── Ad: [Winning creative N] (all proven winners live here)
│
├── PROSPECTING — TESTING [15–20% of budget]
│   └── Campaign: [Brand] Creative Test | Manual | CBO
│       ├── Ad Set: Theme A — [Problem-led hooks]
│       │   ├── Ad: Concept A1
│       │   └── Ad: Concept A2
│       ├── Ad Set: Theme B — [Social proof]
│       │   ├── Ad: Concept B1
│       │   └── Ad: Concept B2
│       └── Ad Set: Theme C — [New format test]
│           └── Ad: Concept C1
│
├── INTEREST/LOOKALIKE TESTING [optional, 5–10% of budget]
│   └── Campaign: [Brand] Audience Test | Manual | ABO
│       ├── Ad Set: Wellness interest stack
│       ├── Ad Set: 1% Lookalike — subscribers
│       └── Ad Set: Broad (control)
│
└── RETARGETING [10–15% of budget]
    └── Campaign: [Brand] Retargeting | Manual | ABO
        ├── Ad Set: Installers → Trial (7-day)
        │   [Different bid/budget from prospecting]
        ├── Ad Set: Trial → Subscribe (14-day)
        └── Ad Set: Lapsed subscribers (30–90 day)
```

### Why This Structure Works

**Separation of testing and scaling:**
- Testing campaign has lower budget → limits risk of new creative
- Scaling campaign has proven winners only → algorithm learns from strong signal
- Retargeting is isolated → prevents retargeting audiences from diluting prospecting

**CBO vs. ABO (Ad Set Budget Optimization):**
- Use CBO (campaign budget) for scaling and testing campaigns — let Meta optimize allocation across ad sets
- Use ABO (ad set budget) for retargeting — you want predictable spend per audience segment

**Why Advantage+ audience for scaling:**
- Broader liquidity → lower CPMs
- Algorithm uses conversion history to find best targets
- Less micromanagement than manual audiences

---

## Campaign Setup Checklists

### New Campaign Launch Checklist

**Before launch:**
- [ ] Pixel and CAPI are both active and sending events
- [ ] Event match quality score is 7+/10 for optimization event
- [ ] Optimization event has 50+ weekly conversions in last 30 days (or use proxy event)
- [ ] Ad account has minimum $5,000 historical ad spend (algorithm needs history)
- [ ] Creative briefs completed for all ads going into campaign
- [ ] Audience exclusions configured (existing subscribers excluded from prospecting)
- [ ] Attribution window set: 7-day click, 1-day view
- [ ] Naming convention applied (see naming convention section below)

**Campaign settings:**
- [ ] Objective: App Promotion → App Events → [Subscription or Trial Start]
- [ ] Budget type: Campaign (CBO) for prospecting; Ad Set (ABO) for retargeting
- [ ] Bid strategy: Highest Volume (unless cost cap is needed)
- [ ] Advantage+ Campaign Budget enabled (CBO campaigns)

**Ad set settings:**
- [ ] Advantage+ Audience selected (or Broad if testing)
- [ ] Audience controls configured (geographic, age restrictions only)
- [ ] Excluded audiences added (existing subscribers, recent purchasers)
- [ ] Placement: Advantage+ Placements (default — let Meta optimize)

**Ad settings:**
- [ ] All required assets uploaded (video, headline, description, CTA)
- [ ] URL parameters added for tracking (UTMs)
- [ ] Creative tagged with correct naming convention
- [ ] At least 3 creatives per ad set (gives algorithm options to optimize)

---

## Naming Conventions

Consistent naming makes reporting manageable at scale. Dan's recommended convention:

**Campaign naming:**
```
[Brand] | [Objective] | [Audience type] | [Date launched]
```
Example: `your product | Scale | Broad-Adv+ | 2025-01`

**Ad Set naming:**
```
[Audience] | [Targeting type] | [Exclusions]
```
Example: `US 25-54 | Advantage+ | -Subscribers`

**Ad naming:**
```
[Format] | [Message angle] | [Hook identifier] | [Version]
```
Example: `UGC-Video | Morning-habit | Streak-hook | v1`

**Why this matters:**
When reviewing performance across 20+ ads, clear naming tells you immediately:
- Which format is winning (UGC vs. static vs. carousel)
- Which message angle is winning (problem vs. social proof vs. authority)
- Which hook variant is winning
- How old the creative is (is it due for refresh?)

---

## Reporting System

### The Weekly Performance Report (Dan's Template)

**Section 1: Account-level snapshot**
| Metric | This week | Last week | 4-week avg | Target | Status |
|--------|-----------|-----------|------------|--------|--------|
| Spend | | | | | |
| CPA | | | | | |
| Installs | | | | | |
| Trials | | | | | |
| Subscriptions | | | | | |
| ROAS | | | | | |

**Section 2: Creative performance (top 10 by spend)**
| Ad name | Spend | CPA | CTR | Freq. | Status |
|---------|-------|-----|-----|-------|--------|
| | | | | | |

Status options: 🟢 Scale | 🟡 Monitor | 🔴 Fatigue/Pause

**Section 3: Audience performance (by ad set)**
| Ad set | Audience type | Spend | CPA | CPM | Status |
|--------|---------------|-------|-----|-----|--------|
| | | | | | |

**Section 4: Action items**
- Creatives to pause this week:
- Creatives to scale this week:
- New creatives to launch in testing:
- Budget adjustments to make:
- Audience changes to make:

---

### Reporting Frequency and Depth

**Daily (5–10 minutes):**
- Check delivery — are campaigns spending?
- Flag anomalies: CPA spike >50%, sudden drop in delivery, billing issues
- Do not make optimization decisions based on daily data alone

**Weekly (45–60 minutes):**
- Full creative performance review (use template above)
- Creative fatigue assessment (CTR, frequency, CPA trends)
- Budget allocation decisions
- Test campaign analysis — what's ready to graduate?
- New creative brief drafting

**Monthly (2–3 hours):**
- Account-level trend analysis (is the account improving over time?)
- Audience efficiency analysis (which targeting approaches are winning?)
- Creative format analysis (which formats are producing the best performers?)
- Channel-level efficiency (how does Meta compare to other channels in mix?)
- Strategic decisions: new campaign types, market expansion, seasonal planning

---

## Scaling Decision Framework

### When to Scale a Creative

**Green light to scale (all three must be true):**
1. Creative has been running for 7+ days (enough time to stabilize)
2. CPA is at or below target for 5 of the last 7 days
3. Spend is >$50 (enough data to be meaningful)

**How to scale:**
1. Add the creative to the Scaling Campaign (Advantage+ campaign)
2. Keep original in Testing Campaign at current budget for 7 more days (parallel running builds confidence)
3. If performance holds in both campaigns: retire from testing and let scale campaign run

### When to Pause a Creative

**Red light (pause immediately):**
- CPA is 3× target for 3+ consecutive days
- Delivery has stopped entirely (zero impressions for 24+ hours)
- Creative is causing account-level policy flag

**Yellow light (monitor closely):**
- CPA is 1.5–3× target for 3+ consecutive days
- CTR has declined >30% from baseline for 7+ days
- Frequency is above 4.0

**For yellow light:** Extend monitoring window by 3 days before pausing. Premature pauses waste creative and can hurt account learning.

### When to Refresh a Creative

Refresh (don't retire) when:
- Core message angle is proven (CPA was good, CTR was strong)
- But frequency and fatigue are setting in
- The creative concept is sound but execution needs refreshing

**Refresh brief approach:**
- Identify what made the original work (hook type, message, format)
- Keep the working element
- Change one or two surface variables (different actor, different setting, different hook delivery)

---

## Automated Rules Setup

Set these once and reduce weekly maintenance time:

**Rule 1: Pause low-delivery creatives**
- If: Ad has spent $50+ and has 0 conversions in last 7 days
- Then: Pause ad
- Purpose: Stop wasting budget on non-converting creative

**Rule 2: Flag high CPA creatives**
- If: Ad's 7-day CPA is >2× target CPA AND ad has spent >$100
- Then: Send notification (don't auto-pause — human review needed)
- Purpose: Get attention to underperforming creative without automatic disruption

**Rule 3: Flag rising frequency**
- If: Ad frequency (7-day) > 4.0
- Then: Send notification
- Purpose: Early warning for creative fatigue

**Rule 4: Scale daily budget gradually**
- If: Campaign 7-day CPA < target CPA by >20% AND campaign is spending >80% of budget
- Then: Increase campaign budget by 15%
- Purpose: Capture upside when performance is strong, within safe scaling parameters

**Rule 5: Protect learning phase**
- Set rule to notify you before any automatic rules apply to campaigns in learning phase
- Purpose: Learning phase stability should not be disrupted by automation

---

## Common Account Audit Findings

Dan has audited accounts for 40+ companies. These are the most common structural problems he finds:

**Problem 1: Too many campaigns, too little budget each**
Symptom: 8+ active campaigns, none with sufficient budget to exit learning
Fix: Consolidate. Start with 2–3 core campaigns. Add campaigns only when there's budget to support them.

**Problem 2: Targeting too narrow**
Symptom: High CPMs, low delivery, frequent audience saturation warnings
Fix: Switch to Advantage+ or broad targeting. Trust the algorithm.

**Problem 3: Creative testing confused with scaling**
Symptom: New creatives in the same campaign as proven winners, causing learning instability
Fix: Dedicated testing campaign, separate from scaling campaign.

**Problem 4: Poor CAPI setup → bad signal → bad performance**
Symptom: Event match quality below 6/10, inconsistent CPA, algorithm making poor targeting decisions
Fix: Audit CAPI setup, fix deduplication, ensure all funnel events are firing correctly.

**Problem 5: Reacting to daily data**
Symptom: Constant bid changes, creative pauses after 24 hours, budget micromanagement
Fix: Establish weekly review cadence. Stop touching campaigns daily. Data needs time to stabilize.

**Problem 6: Not testing creative frequently enough**
Symptom: Account running the same 3 creatives for 3+ months, fatigue setting in, CPA rising
Fix: Monthly creative pipeline. Brief 3–5 new concepts per month minimum.

**Problem 7: Pausing based on CPA alone without understanding Breakdown Effect**
Symptom: Top-spending ad is paused because CPA looks high → entire campaign performance collapses
Fix: Evaluate at campaign level first. Understand that Meta shifts spend to high-potential ads — the high-spending ad may not be the problem.

**Problem 8: Not excluding existing subscribers from prospecting**
Symptom: Paying to acquire people who are already customers
Fix: Create custom audience of current subscribers, exclude from all prospecting campaigns.

---

## Funnel Instrumentation — The Prerequisite

> "You can't optimize what you can't measure. Bad tracking is the most expensive mistake in paid social."

**Required events for a subscription app like your product:**

```
App Install
↓
Account Created / Onboarding Started
↓
Key Activation Event (e.g., first engagement session completed, 3-day streak)
↓
Paywall Viewed
↓
Trial Started
↓
Subscription Converted
↓
Renewal (Day 30)
```

**Instrumentation checklist:**
- [ ] Meta Pixel installed on web (if applicable) + CAPI configured server-side
- [ ] Mobile SDK (Meta SDK or MMP like Adjust/AppsFlyer) tracking app events
- [ ] All funnel events are passing back to Meta with correct event names
- [ ] Deduplication configured (Pixel + CAPI sending same event = double-counting)
- [ ] Test events verified in Meta's Event Testing tool
- [ ] Event match quality score > 7/10 (found in Events Manager)
- [ ] Subscription revenue values being passed (enables ROAS bidding)

**Choosing your optimization event:**
- **Too deep (subscription):** Low volume → algorithm can't learn → unstable performance
- **Too shallow (install):** High volume → algorithm optimizes for installers, not subscribers
- **Sweet spot:** The deepest event with 50+ weekly conversions per ad set

For early-stage campaigns: optimize for trial start or activation event
For scaled campaigns: optimize for subscription conversion
