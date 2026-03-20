## Contents
- The Re-engagement Opportunity
  - Why Re-engagement Matters
  - The Re-engagement Math
- Churn Prediction
  - Why Predict Churn Before It Happens?
  - Behavioral Signals of Impending Churn
  - Building a Churn Prediction Model
  - Intervention Strategies by Risk Level
- The Pinterest Notification System: Casey Winters's Framework
  - Principle 1: Notification Quality Over Quantity
  - Principle 2: Personalized Frequency
  - Principle 3: Content-Based, Not Engagement-Based
  - Principle 4: Downstream Metrics
- Re-engagement Campaigns
  - Campaign Types
  - Campaign Timing
  - Re-engagement Campaign Design Template
- Resurrection User Experience
  - Resurrection Onboarding
  - Resurrection Flow for your product
- Measuring Re-engagement Success
  - Resurrection Metrics
  - The Resurrection Quality Test
- Cancellation and Save Flows
  - Cancellation Save Framework
  - Save Offer Best Practices
  - Save Rate Benchmarks
- Applied to your product: Re-engagement Architecture
  - Priority 1: Churn Prediction
  - Priority 2: Notification System
  - Priority 3: Cancellation Save Flow
  - Priority 4: Seasonal Re-engagement
- Ongoing Retention Mechanics: Streaks and Content Freshness
  - Streak Mechanics
  - Content Freshness and Retention
  - The Current User Retention System

---
# Re-engagement & Resurrection Systems — Deep Reference
*Source: Casey Winters, "How Pinterest Grew Its Notifications System," caseyaccidental.com (2018); Mastering Retention & Engagement course syllabus; Erika Warren lifecycle framework*

---

## The Re-engagement Opportunity

Most products lose 70-90% of users within the first 30 days. Of those lost users, a meaningful percentage can be brought back -- if the re-engagement system is well-designed.

### Why Re-engagement Matters

1. **Cheaper than acquisition:** Re-engaging a churned user costs a fraction of acquiring a new one (they already have your app installed or account created)
2. **Known preferences:** You have behavioral data on churned users that you don't have on new prospects
3. **Revenue recovery:** For subscription products, resurrecting a churned subscriber recovers LTV that was otherwise lost
4. **Compounds with time:** As your user base grows, the pool of lapsed users grows -- re-engagement becomes an increasingly large opportunity

### The Re-engagement Math

```
Monthly resurrection potential = Lapsed user pool x Reachability x Resurrection rate

Example for your product:
- Total lapsed users (last 12 months): 500,000
- Reachable via push/email: 60% (300,000)
- Resurrection rate: 3% (9,000 users/month)
- Average subscriber revenue: $8/month
- Monthly resurrection revenue: $72,000
```

Even modest resurrection rates produce meaningful revenue for subscription products.

---

## Churn Prediction

### Why Predict Churn Before It Happens?

Intervening before a user churns is 3-5x more effective than trying to resurrect them after. Churn prediction identifies at-risk users while they can still be saved.

### Behavioral Signals of Impending Churn

| Signal | Description | Urgency |
|---|---|---|
| Frequency decline | User goes from daily to weekly to monthly | High |
| Session depth decline | User opens app but completes fewer actions | Medium |
| Notification disable | User turns off push notifications | Very High |
| Streak break | User breaks a multi-day streak and doesn't restart | High |
| Content skip rate increase | User skips or abandons more content | Medium |
| Feature disengagement | User stops using secondary features (sharing, saving) | Medium |
| Subscription downgrade inquiry | User views cancel/downgrade page | Critical |
| Support complaint | User contacts support with frustration | High |

### Building a Churn Prediction Model

**Simple approach (rule-based):**
```
IF user was daily active AND has been inactive for 3+ days
  → Flag as "at risk"

IF user was weekly active AND has been inactive for 10+ days
  → Flag as "at risk"

IF user turned off notifications
  → Flag as "high risk" regardless of recent activity

IF user visited cancellation page
  → Flag as "critical risk"
```

**Advanced approach (ML-based):**
- Features: login frequency, session duration, core action completions, content consumption patterns, notification response rate, time since last activity
- Target: Did the user churn within the next 14 days?
- Model: Logistic regression or gradient boosted trees
- Output: Churn probability score for each user

### Intervention Strategies by Risk Level

| Risk Level | Trigger | Intervention |
|---|---|---|
| Low risk (slight decline) | Frequency dropped 20% | Personalized content recommendation notification |
| Medium risk (notable decline) | Inactive 3-7 days after being daily | "Your streak can still be saved" + best content |
| High risk (significant decline) | Inactive 7-14 days, notifications disabled | Email with high-value content + "what's new" |
| Critical risk (cancellation intent) | Visited cancel page | In-app save offer (discount, pause, downgrade option) |

---

## The Pinterest Notification System: Casey Winters's Framework

Casey Winters built Pinterest's notification system during its hypergrowth phase. The principles are widely applicable.

### Principle 1: Notification Quality Over Quantity

Pinterest discovered that sending more notifications increased short-term engagement but decreased long-term retention. Users who received too many notifications were more likely to:
- Disable notifications (permanent loss of re-engagement channel)
- Uninstall the app
- Report as spam

**The insight:** Each notification is a withdrawal from a trust bank. Each valuable notification is a deposit. The balance must stay positive.

### Principle 2: Personalized Frequency

Not all users should receive the same number of notifications. Pinterest built a frequency model based on:
- User engagement level (power users tolerate more)
- Historical notification response rate (responsive users get more)
- Time since last notification (respect cooldown periods)
- Notification type (transactional > social > marketing)

### Principle 3: Content-Based, Not Engagement-Based

**Bad notification:** "You haven't opened Pinterest in 3 days!"
- User reaction: "So what? Don't guilt-trip me."

**Good notification:** "25 new ideas in home decor have been saved to your feed"
- User reaction: "Oh, I want to see those."

The notification's value should stand on its own, regardless of whether the user has been active.

### Principle 4: Downstream Metrics

Pinterest measured notification success by downstream retention, not by notification-level metrics:

| Metric | What It Tells You | Limitation |
|---|---|---|
| Send rate | How many notifications sent | Says nothing about quality |
| Open rate | % who opened the notification | Can be gamed with clickbait |
| CTR | % who clicked through | Doesn't measure long-term value |
| D7 retention after notification | Whether the notification actually helped retention | Better, but lagging |
| Notification disable rate | Whether users trust your notifications | Critical health metric |
| Uninstall rate post-notification | Whether you're pushing too hard | The nuclear metric |

**The right metric hierarchy:**
1. Notification disable rate (keep as low as possible)
2. D7 retention of notified users vs. control group
3. Open rate (secondary, useful for content optimization)
4. Volume sent (irrelevant if quality is bad)

---

## Re-engagement Campaigns

### Campaign Types

**1. Content-Based Re-engagement**
- Send lapsed users the best content they missed
- Personalize based on their past engagement patterns
- Example: "While you were away, 50,000 people found strength in this engagement session"
- Best for: Content products, first 14-30 days of lapse

**2. Feature-Based Re-engagement**
- Announce new features or improvements
- Works best when the new feature addresses a known churn reason
- Example: "New: Evening engagements -- wind down your day with a 3-minute guided session"
- Best for: Product with active development, any lapse period

**3. Social Re-engagement**
- Leverage social connections to bring users back
- Example: "Your accountability partner Sarah has been rooting for you this week"
- Best for: Products with social features, any lapse period

**4. Seasonal Re-engagement**
- Tie re-engagement to calendar events
- Example: "seasonal campaign begins next week -- 40 days of daily engagements to guide your journey"
- Best for: Products with seasonal relevance, long-lapsed users

**5. Incentive-Based Re-engagement**
- Offer a discount or free access to bring users back
- Example: "We'd love to welcome you back -- enjoy 1 month of Premium free"
- Best for: Subscription products, 30-90 day lapsed users
- Warning: Can train users to churn and wait for offers

### Campaign Timing

| Lapse Duration | Campaign Type | Channel | Frequency |
|---|---|---|---|
| 3-7 days | Content + streak recovery | Push notification | 1-2 total |
| 7-14 days | Best-of content + what's new | Push + email | 2-3 total |
| 14-30 days | Feature announcement + social | Email primary | 1-2 total |
| 30-60 days | Seasonal/incentive | Email only | 1 per month |
| 60-90 days | Major product update | Email only | 1 per quarter |
| 90+ days | Nothing (or annual event only) | Email only | 1 per year max |

### Re-engagement Campaign Design Template

**Campaign name:** [Descriptive name]
**Target audience:** Users who [behavior] for [duration]
**Exclusions:** Users who [disabled notifications / unsubscribed / gave negative feedback]
**Channel:** [Push / Email / SMS / In-app]
**Content:** [Specific message and creative]
**CTA:** [Specific action the user should take]
**Success metric:** [D7 retention of resurrected users]
**Kill criteria:** [Stop if notification disable rate increases by X%]

---

## Resurrection User Experience

When a lapsed user returns, the re-entry experience is critical. If they come back to the same experience that caused them to leave, they'll leave again.

### Resurrection Onboarding

**Do:**
- Welcome them back warmly (acknowledge the gap without guilt)
- Show what they missed (new content, features, community activity)
- Reduce friction to the core action (deep link to content, not home screen)
- Refresh their preferences if content may have shifted
- Restart their streak at Day 1 with a clean slate (no penalty)

**Don't:**
- Show an empty or stale state
- Ask them to re-onboard from scratch
- Send a barrage of catch-up notifications
- Show a paywall immediately if their subscription lapsed
- Guilt them for being away

### Resurrection Flow for your product

```
User returns after 3-week lapse
↓
Welcome screen: "Welcome back! We've been rooting for you."
↓
"Here's what's resonating with the community this week:"
[Show 3 top-rated engagement sessions from the last week]
↓
"Start with today's engagement session? It's a 4-minute listen."
[Deep link to today's content — one tap to start]
↓
After completing engagement session:
"Your new streak starts today. Day 1!"
[Encouraging message, no reference to broken streak]
↓
"Want a daily reminder? Set your preferred time."
[Offer to re-enable or adjust notifications]
```

---

## Measuring Re-engagement Success

### Resurrection Metrics

| Metric | Definition | Target |
|---|---|---|
| Resurrection Rate | % of lapsed users who return in a given month | 2-5% monthly |
| Resurrection Retention | D30 retention of resurrected users | Should approach new user D30 retention |
| Resurrection LTV | Lifetime value of resurrected users | Should approach new user LTV |
| Campaign ROI | Revenue from resurrected subscribers / cost of campaign | > 3x |
| Channel Disable Rate | % of users who disable notifications after campaign | < 0.5% per campaign |

### The Resurrection Quality Test

A common mistake is celebrating resurrection volume without checking quality. Key test: **Do resurrected users retain like new users, or do they churn again quickly?**

```
If resurrected user D30 retention > 50% of new user D30 retention
  → Re-engagement is creating genuine value. Scale it.

If resurrected user D30 retention < 25% of new user D30 retention
  → Re-engagement is creating false activity. Users return but don't stick.
  → Investigate: Is the return experience addressing why they left?
```

---

## Cancellation and Save Flows

For subscription products, the cancellation flow is the last chance to retain a paying user.

### Cancellation Save Framework

```
User clicks "Cancel Subscription"
↓
Step 1: Reason collection
"We're sorry to see you go. What's the main reason?"
□ Too expensive
□ Not using it enough
□ Content isn't relevant to me
□ Found an alternative
□ Technical issues
□ Other
↓
Step 2: Targeted save offer (based on reason)

If "Too expensive" → Offer discounted rate or annual plan
If "Not using it enough" → Offer pause (3 months) instead of cancel
If "Content not relevant" → Offer to customize content preferences
If "Found alternative" → Show unique value proposition, offer free month
If "Technical issues" → Escalate to support immediately
↓
Step 3: If save rejected → Easy cancel (don't make it painful)
"We've cancelled your subscription. Your access continues until [date].
You can rejoin anytime. We'll keep your personal journal and history safe."
↓
Step 4: Post-cancel survey (optional, short)
"One last question: what would bring you back?"
↓
Step 5: Grace period marketing
Send 1-2 emails during remaining access period showing value
```

### Save Offer Best Practices

1. **Offer a pause, not just a cancel.** Many users who "cancel" would prefer to pause for a month or three.
2. **Discount strategically.** Don't offer discounts to users who didn't cite price. It trains users to cancel to get a discount.
3. **Address the stated reason.** A save offer that doesn't address the churn reason feels tone-deaf.
4. **Make cancel easy.** Difficult cancellation flows create negative brand sentiment and app store reviews. The goal is to save who you can, not trap everyone.
5. **Preserve data.** Always keep the user's data (journal, history, preferences) so re-joining is frictionless.

### Save Rate Benchmarks

| Save Tactic | Typical Save Rate |
|---|---|
| Pause option | 10-20% of cancel attempts |
| Price discount | 15-25% of price-sensitive cancels |
| Content personalization | 5-10% of relevance cancels |
| Feature demonstration | 3-8% of "not using enough" cancels |
| Overall save rate | 10-20% of all cancel attempts |

---

## Applied to your product: Re-engagement Architecture

### Priority 1: Churn Prediction
Build a simple rules-based churn prediction model:
- Flag users who were daily and haven't opened in 3 days
- Flag users who turned off notifications
- Flag users who visited the cancellation page

### Priority 2: Notification System
Segment all users by engagement level and send appropriate notifications:
- Daily active: Feature discovery, new content series, community
- Weekly active: Best daily engagement of the week, personalized
- Cooling (3-7 days): "Your engagement session today is especially meaningful" + streak prompt
- Dormant (7-30 days): 1-2 high-quality re-engagement emails

### Priority 3: Cancellation Save Flow
Implement a multi-step cancellation flow:
- Reason collection
- Pause option (default over cancel)
- Targeted save offer by reason
- Easy cancel if user persists
- Data preservation always

### Priority 4: Seasonal Re-engagement
Build an annual calendar of re-engagement campaigns tied to seasonal events:
- seasonal campaign (seasonal engagement session challenge)
- seasonal event
- Advent/Christmas
- New Year (self-improvement resolution)
- Seasonal events
- Back-to-school (family engagement session plans)

---

## Ongoing Retention Mechanics: Streaks and Content Freshness

### Streak Mechanics

Streaks are a powerful retention mechanic for daily-use products.

**Why streaks work:**
- Loss aversion: users fear breaking a streak more than they desire building one
- Visual progress: streak counters provide tangible evidence of commitment
- Social proof: sharing streak achievements creates mild accountability
- Identity: "I'm a person who does this every day"

**Streak design principles:**
1. The streaked action must be the core action (not a vanity metric)
2. Streaks should have a "freeze" or "grace day" mechanic to prevent frustration
3. Streak milestones should be celebrated (7 days, 30 days, 100 days)
4. Streaks should not be punitive — losing a streak should encourage restart, not quit
5. Streak notifications should be sent at the user's habitual time, not company time

**Streak examples:**
- Duolingo: Longest-running streak mechanic in consumer apps. Fire animation, streak freezes, friend leaderboards.
- Headspace: Meditation streaks with milestone celebrations
- Product opportunity: Daily engagement streak with grace days, milestone badges, and optional sharing

### Content Freshness and Retention

For content-driven subscription products, retention is fundamentally tied to content supply:

**The Content-Retention Equation:**
```
Content value = Relevance x Freshness x Quality x Discovery

If any factor drops to zero, engagement drops.
```

**Content strategy for retention:**
1. **Daily new content:** Users need a reason to come back today that didn't exist yesterday
2. **Personalization:** The right content for the right user at the right time
3. **Content depth:** Multiple content types serve different engagement modes (quick read, deep listen, meditation)
4. **Seasonal/timely content:** Content tied to holidays, events, or cultural moments drives return visits
5. **Content catalog value:** Back-catalog content that users discover over time increases perceived value

### The Current User Retention System

For users past the activation phase, retention is maintained through:

```
Daily Loop:
Trigger (notification/habit) → Open app → Core action (engagement session)
→ Reward (emotional value + streak progress)
→ Investment (preferences refined, history built, streak continued)
→ Next-day trigger stronger (personalized, streak-protecting)
```

**Levers to strengthen the daily loop:**
1. Improve trigger timing (send notification when user is most receptive)
2. Reduce friction to core action (deep link to today's engagement session)
3. Increase reward variability (surprise content, milestones, social validation)
4. Increase investment (saved content, journal entries, progress tracking)
