## Contents
- The Launch Is Not the Finish Line
- Pre-Launch Preparation
  - Three-Tier Prioritization
  - Launch Checklists
  - The Rollback Plan
- Staged Launch Approaches
  - Strategy 1: Percent of Users
  - Strategy 2: Customer Segment
  - Strategy 3: Technology Platform
  - Combining Strategies
- Post-Launch Failure Mode Responses
  - Optimize in Place
  - Throttle
  - Temporary Block
  - Full Rollback
- Measuring Outcomes
  - Four Dimensions
  - The Three Outcome Decisions
- Post-Mortem Process
- your product Example: "Guided Family Engagement Sessions"

---
# Launch and Post-Launch Strategy

> Source: Andy Johns and Matt Greenberg, Mastering Product Delivery

---

## The Launch Is Not the Finish Line

Launch is the beginning of the most informative phase: real behavioral data from real users. Choices in the first two weeks often determine whether the bet succeeds or fails.

---

## Pre-Launch Preparation

### Three-Tier Prioritization

**Launch Blockers:** Non-negotiable. If incomplete, launch does not happen. Criteria: user safety/data integrity at risk, feature literally non-functional, legal/compliance obligation, would damage brand or trust.

**Critical Items:** Important but deferrable. Ship in fast-follow. Feature works without them but experience is noticeably degraded.

**Non-Critical:** Nice-to-have. Cut from scope, move to backlog.

**The 20% Rule:** If >20% of remaining items are blockers, force-rank. "If we could only ship 5 of these 15, which 5?"

### Launch Checklists

**Product/Engineering:** Feature flags configured, monitoring dashboards live, rollback plan tested (<10 min), load testing at 2x traffic, error tracking configured, analytics verified, edge cases documented.

**Customer Support:** FAQ updated, team briefed, escalation path defined, canned responses drafted.

**Marketing/Comms:** App Store updated, in-app messaging scheduled, email queued, press coordinated, social scheduled.

**Data/Analytics:** Event tracking verified, baseline captured, success dashboard created, anomaly alerts configured.

### The Rollback Plan

Four questions: (1) How do we detect a problem? (2) How do we assess severity? (3) How do we roll back? (4) How long does rollback take? Target: <10 min for feature flag, <30 min for code revert. Test in staging before launch.

---

## Staged Launch Approaches

### Strategy 1: Percent of Users
1% -> 5% -> 25% -> 50% -> 100%. Monitor: crash rate, engagement, feature metrics, support volume. Advance on evidence, not schedule.

**Risk:** Early adopters may not represent average users. Mitigation: monitor segmented metrics.

### Strategy 2: Customer Segment
Restrict to geography, user type, or behavioral cohort. Choose highest expected value + lowest blast radius.

**Risk:** Segment-specific behaviors may mask broader problems.

### Strategy 3: Technology Platform
Launch on one platform first (e.g., iOS), learn, then launch other. Useful when platform-specific issues likely or one platform has better instrumentation.

### Combining Strategies
Example: (1) iOS only, (2) 5% iOS with 7+ day streak, (3) 25% all iOS, (4) 25% Android, (5) 100% both.

---

## Post-Launch Failure Mode Responses

### Optimize in Place
**When:** Non-critical, minor friction. Feature adoption lower than expected but positive. Minor UI confusion.
**Action:** Track in backlog, fix in next release, do not pause rollout.

### Throttle
**When:** Performance degradation under load. Increased latency, capacity approaching limits.
**Action:** Cap rollout, fix performance, resume when metrics return.

### Temporary Block
**When:** Significant bug for subset. Broken on specific device/OS, data integrity issue.
**Action:** Pause rollout, deploy targeted fix, regression test, resume.

### Full Rollback
**When:** Critical issue -- crashes, data loss, trust damage.
**Action:** Revert immediately (feature flag or code revert). Communicate with affected users within 24 hours. Thorough post-mortem. Do not relaunch until root cause fixed AND checklist reviewed.

**your product trigger:** If AI-generated engagement session content produces foundationally inaccurate output, this is Full Rollback. Trust damage in a consumer app is disproportionately severe.

---

## Measuring Outcomes

### Four Dimensions

**1. Adoption:** Exposure rate, activation rate (% who engaged at least once), depth of engagement.

**2. Retention Impact:** D1/D7/D30 delta for exposed vs. control. A successful big bet should show 5-15% relative D7 improvement. <2% delta suggests feature is not meaningful enough.

**3. Revenue Impact:** Free-to-paid conversion, churn reduction, LTV impact. Should see measurable conversion impact within 30 days.

**4. Qualitative:** App Store reviews, support tickets, social media, NPS.

### The Three Outcome Decisions

**Double Down:** Metrics clearly exceed criteria. Invest in optimization, expansion, marketing. Shift from launch to growth mode.

**Iterate:** Mixed signal. Run targeted experiments: low adoption -> improve discovery; low retention -> improve repeat-use loop; low conversion -> improve premium value prop. Timebox: 4-6 weeks. If no improvement, escalate to Deprecate.

**Deprecate:** Clearly not working despite iteration. Remove cleanly. Communicate with adopters. Document learnings. Celebrate the learning.

---

## Post-Mortem Process

After every big bet launch (success or failure):

1. **Conviction accuracy:** Did pre-launch conviction match outcomes? Signals missed?
2. **Estimate accuracy:** Delivery timeline vs. plan? What caused variance?
3. **Tradeoff quality:** Were execution tradeoffs correct in retrospect?
4. **Launch execution:** Staged rollout work? Surprises the checklist missed?
5. **Team process:** What worked in execution cadence? What to change?

**Outputs:** Updated estimation calibration, updated launch checklist, updated conviction criteria, team process improvements.

---

## your product Example: "Guided Family Engagement Sessions"

**Pre-launch tiers:**
- Blockers: Age-appropriate content review, family account linking, parental controls, content accuracy
- Critical: Family progress sharing via notifications, discussion prompt quality rating
- Non-Critical: Custom family cover photo, completion badges

**Staged rollout:**
1. iOS, 5% with 2+ household members (validate linking)
2. iOS, 25% with 2+ household members (validate engagement)
3. All iOS, 25% (validate discovery for non-family users)
4. Android, 25% (platform validation)
5. Full rollout both platforms

**Success criteria:**
- Family activation rate >20% of exposed accounts
- D7 retention for family participants >50% (vs. 40% baseline)
- Family plan upgrade rate >8% within 30 days
- Parent NPS for family experience >60

**Kill criteria:**
- Family activation <5% after 2 weeks at 25% rollout -> pause
- Editorial accuracy issue flagged by content team -> full rollback
- Children's content surfaces age-inappropriate material -> full rollback within 1 hour
