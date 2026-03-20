## Contents
- System 1 / System 2 — Product Design Implications
  - When Users Are in System 1 Mode
  - When Users Are in System 2 Mode
- Bias Catalog — 15 Product-Relevant Biases
  - 1. Loss Aversion
  - 2. Social Proof
  - 3. Endowment Effect
  - 4. Default Effect
  - 5. Peak-End Rule
  - 6. IKEA Effect
  - 7. Anchoring
  - 8. Commitment & Consistency
  - 9. Scarcity
  - 10. Mere Exposure Effect
  - 11. Reciprocity
  - 12. Authority
  - 13. The Zeigarnik Effect
  - 14. Paradox of Choice
  - 15. Sunk Cost Fallacy
- Bias Stacking Strategies
  - The Retention Stack
  - The Conversion Stack
  - The Referral Stack
- Ethical Framework for Bias Application
  - The Alignment Test
  - The Vulnerability Test

---
# Cognitive Bias Toolkit — Deep Reference
*Source: Mallory Contois, User Psych Foundations; synthesized with Kahneman (Thinking, Fast and Slow), Thaler & Sunstein (Nudge), and Cialdini (Influence)*

---

## System 1 / System 2 — Product Design Implications

### When Users Are in System 1 Mode
- Browsing, scrolling, routine actions
- Responding to notifications
- Making low-stakes decisions (which content to read)
- Default behaviors (accepting suggestions)

**Design for System 1:**
- Clear visual hierarchy — don't make users think
- Sensible defaults that serve user interests
- Familiar patterns (don't reinvent navigation)
- Emotional cues (imagery, tone, color)
- Minimal cognitive load per interaction

### When Users Are in System 2 Mode
- Purchasing decisions (subscription sign-up)
- Account settings and preferences
- Comparing plans or options
- Evaluating whether to continue using the product

**Design for System 2:**
- Clear, honest information presentation
- Comparison tools and decision aids
- Reduce decision fatigue (limit options to 3-4)
- Provide social proof and expert endorsement
- Allow time and space for deliberation

---

## Bias Catalog — 15 Product-Relevant Biases

### 1. Loss Aversion
**Mechanism:** People feel losses approximately twice as strongly as equivalent gains (Kahneman & Tversky, 1979).

**Product applications:**
- Streak mechanics: "Don't lose your 45-day streak" is more motivating than "Build a 46-day streak"
- Trial expiration: "Your saved engagement sessions will be unavailable" vs. "Subscribe to access more"
- Churn prevention: Showing users what they'll lose (engagement history, community connections)

**Ethical guardrails:**
- Don't manufacture false losses
- Don't use loss framing to create anxiety in vulnerable populations
- your product specific: Product contexts require positive framing — "Your streak is a tool, not a test"
- Balance loss framing with positive reinforcement

**Implementation template:**
```
Screen/Message: [Context]
Loss frame: "You'll lose [specific thing they value]"
Positive reframe: "Keep [specific thing] by [simple action]"
Test both; monitor sentiment alongside conversion
```

### 2. Social Proof
**Mechanism:** People look to others' behavior to determine correct action, especially in uncertain situations (Cialdini, 1984).

**Product applications:**
- Aggregate statistics: "5M+ people were active with us today"
- Similar-user proof: "Popular with people in your area"
- Activity streams: "Sarah just completed 30 days of engagement"
- Testimonials and reviews from relatable users

**Effectiveness factors:**
- Similarity: Social proof from similar people is more persuasive
- Proximity: Local/community proof > global statistics
- Recency: Current activity > historical totals
- Specificity: "1,247 people are active right now" > "Millions of users"

**Product applications:**
- "342 people in [city] were active this morning"
- "Your community group completed 100 sessions together"
- Denomination-specific social proof for targeted audiences
- Real-time activity counter during live events

### 3. Endowment Effect
**Mechanism:** People value what they already have more than equivalent items they don't possess (Thaler, 1980).

**Product applications:**
- Free trial strategy: Let users build value before paywall
- Content accumulation: Journal entries, saved engagement sessions, reflection history
- Personalization: Algorithm-tuned content that gets better over time
- Community connections: Relationships formed in community groups

**Building endowment systematically:**
```
Day 1-7:   Help user create first personal content (content list, first journal entry)
Day 7-14:  Accumulate personalized recommendations based on behavior
Day 14-30: Build social connections that create relational endowment
Day 30+:   User has significant invested value that's painful to abandon
```

### 4. Default Effect
**Mechanism:** People disproportionately stick with pre-selected options (Johnson & Goldstein, 2003).

**Product applications:**
- Onboarding defaults: Pre-set notification time to 7:00 AM
- Content defaults: "Today's engagement session" as the primary home screen action
- Settings defaults: Community features opted-in by default
- Plan defaults: Highlight recommended subscription plan

**Ethical implementation:**
- Defaults should genuinely serve user interests, not just business metrics
- Make defaults easy to change
- Be transparent about why a default was chosen
- Test whether users who stick with defaults have better outcomes

### 5. Peak-End Rule
**Mechanism:** People judge experiences primarily by their most intense point and their ending (Kahneman, 1999).

**Product applications:**
- Design at least one "peak moment" in every session
- End sessions on emotionally positive notes
- Don't let the last interaction be a paywall or error message
- Onboarding peak: First "aha moment" should be emotionally powerful

**your product session design:**
```
Opening:     Centering moment (calm transition into engagement session)
Content:     Daily engagement session with one "peak" insight or emotional moment
Reflection:  Personal journaling or journaling prompt (deepens the peak)
Closing:     Encouraging, warm ending ("Go in peace" or blessing)
             ^ This is the "end" — make it count
```

### 6. IKEA Effect
**Mechanism:** People assign higher value to things they helped create, even if the result is imperfect (Norton, Mochon & Ariely, 2012).

**Product applications:**
- User-created content lists (more valued than pre-made lists)
- Custom engagement session plans (more engaging than algorithmic suggestions)
- Journal entries (create personal, irreplaceable content)
- Community contributions (answering community requests, sharing reflections)

**Implementation principle:** The effort must feel meaningful and achievable. Too much effort creates frustration; too little doesn't create investment.

### 7. Anchoring
**Mechanism:** First piece of information encountered disproportionately influences subsequent judgments (Tversky & Kahneman, 1974).

**Product applications:**
- Pricing: Show annual plan first ($59.99/year) before monthly ($9.99/month)
- Content quality: First engagement session experienced sets quality expectations
- Community: First interaction in community group sets social norms
- Onboarding: First question asked frames the user's mental model

### 8. Commitment & Consistency
**Mechanism:** Once people commit to a position or action, they strive to remain consistent (Cialdini, 1984).

**Product applications:**
- Micro-commitments in onboarding: "What's your engagement goal this week?"
- Public commitments: Sharing goals with accountability partners
- Escalation: Small commitments (set schedule) → medium (join group) → large (subscribe)
- Labeling: "You're on a personal growth journey" creates consistency pressure

**Commitment escalation ladder for your product:**
```
1. Choose preferred session time (tiny commitment)
2. Set a weekly engagement goal (small commitment)
3. Create a content list (medium commitment — IKEA effect stacks)
4. Join a community group (social commitment)
5. Invite a friend (public commitment)
6. Subscribe (financial commitment — by now, high consistency pressure)
```

### 9. Scarcity
**Mechanism:** People value things more when they perceive limited availability (Cialdini, 1984).

**Product applications:**
- Limited-time engagement session series
- Exclusive content for subscribers
- Time-limited community events (live live sessions)
- Countdown timers for special programs

**Ethical guardrails:**
- Scarcity must be genuine, not manufactured
- Don't create FOMO in personal wellness contexts (antithetical to peace)
- Use scarcity for engagement, not anxiety

### 10. Mere Exposure Effect
**Mechanism:** Repeated exposure to something increases liking for it (Zajonc, 1968).

**Product applications:**
- Consistent brand touchpoints build affinity
- Daily engagement session exposure builds content attachment
- Regular notification timing creates familiarity
- Consistent design language builds trust

### 11. Reciprocity
**Mechanism:** People feel obligated to return favors and gestures (Cialdini, 1984).

**Product applications:**
- Free valuable content creates obligation to give back (subscribe, share)
- Community help received creates motivation to help others
- Gift mechanics (send a engagement session to a friend)

### 12. Authority
**Mechanism:** People defer to perceived experts and authorities (Cialdini, 1984).

**Product applications:**
- Expert-authored content (experts, thought leaders, wellness leaders)
- Endorsements from respected industry leaders
- "Curated by" labels that signal quality curation

### 13. The Zeigarnik Effect
**Mechanism:** People remember and are motivated to complete uncompleted tasks more than completed ones.

**Product applications:**
- Engagement Session series that create "open loops" — must return tomorrow for continuation
- Progress indicators showing partial completion
- "You're 3 days into a 7-day journey" messaging

### 14. Paradox of Choice
**Mechanism:** Too many options lead to decision paralysis and reduced satisfaction (Schwartz, 2004).

**Product applications:**
- Limit daily content choices to 1-3 options, not a full library browse
- Curate recommendations rather than showing everything
- "Today's engagement session" as the clear default reduces choice burden

### 15. Sunk Cost Fallacy
**Mechanism:** People continue investing in something because of prior investment, not future value.

**Product applications:**
- Accumulated streak days create sunk cost attachment
- Library of saved content represents past investment
- Community relationships built over time
- Payment history ("You've been a member for 6 months")

---

## Bias Stacking Strategies

### The Retention Stack
Combine biases that reinforce daily return:
- **Commitment** (set daily goal) + **Loss aversion** (streak at risk) + **Zeigarnik** (series incomplete) + **Social proof** (community is active)

### The Conversion Stack
Combine biases that drive subscription:
- **Endowment** (free trial builds value) + **Loss aversion** (trial ending) + **Anchoring** (annual price first) + **Social proof** (millions subscribe)

### The Referral Stack
Combine biases that drive sharing:
- **Reciprocity** (app gave value, share it) + **Social proof** (friends already using) + **Authority** (respected content creators) + **Identity** (sharing reflects who you are)

---

## Ethical Framework for Bias Application

### The Alignment Test
For every bias application, ask: "Does this serve the user's genuine interests, or only the business's interests?"

| Aligned (Ethical) | Misaligned (Dark Pattern) |
|-------------------|--------------------------|
| Streak that helps build genuine habit | Streak that creates anxiety |
| Social proof that builds community | Fake activity indicators |
| Default that matches majority preference | Default that maximizes revenue |
| Loss framing for genuine value | Manufactured loss to create fear |

### The Vulnerability Test
For consumer apps specifically: "Could this application of psychology cause psychological harm?"

- Don't exploit guilt about personal inconsistency
- Don't create anxiety about engagement frequency
- Don't use scarcity tactics that contradict messages of abundance
- Don't use competitive comparison in personal wellness contexts
- Frame streaks through grace, not performance metrics
