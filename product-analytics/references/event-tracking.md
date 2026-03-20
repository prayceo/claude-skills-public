## Contents
- Why Event Tracking Fails: The Root Causes
  - Root Cause 1: Tracking Metrics as the Goal vs. Analyzing Them
  - Root Cause 2: Developer/Data Mindset vs. Business User Mindset
  - Root Cause 3: Wrong Level of Abstraction
  - Root Cause 4: Written Only vs. Visual Communication
  - Root Cause 5: Data as a Project vs. Core Initiative
- The Step-by-Step Event Tracking System
  - Step 1: Business User Mindset
  - Step 2: Journeys Instead of Metrics
  - Step 3: Properties
- The Event Tracking Dictionary
- your product Event Tracking Audit Checklist
  - Activation Funnel Analysis — Procedural Steps

---
# Event Tracking — Deep Reference
*Source: Crystal Widjaja, "Why Most Analytics Efforts Fail," Blog, October 2020*

---

## Why Event Tracking Fails: The Root Causes

Most analytics programs fail not from bad tools or insufficient data, but from these five root causes. Treating the symptoms (new tool, more training, higher hiring bar) without fixing the root causes guarantees failure.

### Root Cause 1: Tracking Metrics as the Goal vs. Analyzing Them

The goal of data is not to track metrics. The goal is to analyze them and make them actionable.

"Actionable" means: knowing what successful users do differently from unsuccessful users, and being able to take steps to push more users toward success.

A metric without segmentation is noise. "50% of users completed onboarding" is useless. "50% of users completed onboarding, but among users who arrive from community partner links, it's 72%, vs. 31% from paid social" — that's actionable.

### Root Cause 2: Developer/Data Mindset vs. Business User Mindset

The customers of your analytics system are business users: PMs, marketers, ops managers, support teams. Not data analysts. Most analytics systems are built for analysts.

**Crystal's test at Gojek:**
> "The true test: Can someone in our operations/customer care team — the least educated on the market and most distant from the product development process — access the event tracking tool and use it independently without a full onboarding session?"

If operations/care can do it, everyone else can too. If they can't, the system needs rebuilding.

**Practical implications of business user mindset:**
- Event names should read like natural language ("Signup Method Selected" not "signup_method_select_evt_v2")
- Every event should have a screenshot showing exactly what's on screen when it fires
- A non-technical person should be able to map events to product screens without reading documentation
- Properties should be named so their values are self-explanatory ("source: facebook" not "source: 1")

### Root Cause 3: Wrong Level of Abstraction

**Too specific (bad):** `facebook_signup`, `google_signup` — different events for what is essentially the same action with a variable
- Problem: Can't query "all signups" without adding multiple events; can't segment by source because source is baked into the event name

**Too specific (ok):** `signup_clicked` — clear what happened, but no way to segment
- Problem: No properties to understand which signup method; no way to ask "which source converts better?"

**Right level (great):** `signup_method_selected` with property `source: [facebook | google | email | phone]`
- Why: Single event name for the query; property enables all segmentation needs

**The abstraction test:**
- Can you answer all likely questions about this event with just the event name + properties?
- If you query just this one event, can a business user understand what happened and why?
- If 99% of users trigger this event, what would you do? (If nothing, the event isn't useful)

### Root Cause 4: Written Only vs. Visual Communication

A data dictionary is necessary but not sufficient. Text descriptions of events can always be misinterpreted. Add screenshots.

**The visual requirements:**
1. Every event has a screenshot of the exact screen state when it triggers
2. Intent → Success → Failure journeys are mapped visually (flowchart or annotated screen)
3. When presenting findings, show the product screen alongside the data chart

Crystal's principle: when people discuss events, they're visualizing product screens in their heads. Short-circuit that process by including the actual visuals.

### Root Cause 5: Data as a Project vs. Core Initiative

Product changes. Features are added and removed. Flows change. If event tracking is treated as a one-time setup, it will be stale within months.

**The iteration requirement:**
- Treat your event tracking system as a product with continuous iteration
- Run a quarterly audit (Crystal says "Marie Kondo every quarter") — remove events no longer in the product, update events that have changed, add events for new features
- New features should never ship without a corresponding update to the Event Tracking Dictionary

**The Data Wheel of Death** (Balfour/Widjaja) is the failure mode of treating data as a project:
```
Event tracked → Not analyzed → Trust erodes → Teams bypass it
     ↑                                               ↓
Product ships → Event goes stale → Numbers wrong  ← New tool purchased
```

The fix: continuous ownership of data as a living system.

---

## The Step-by-Step Event Tracking System

### Step 1: Business User Mindset

Before tracking a single event, understand the business user's information needs:

**Level 1: Business goals**
What are the company's current OKRs and KPIs? What are executives optimizing for?
Sources: OKR documents, board decks, quarterly planning docs

**Level 2: Team goals**
What are each team's specific objectives that ladder to business goals?
Sources: Team OKRs, team lead conversations, historical quarterly reviews

**Level 3: Product experiences**
For each goal, what product experiences drive it? What context could influence the goal?
Example: For "subscription conversions," experiences include paywall views, trial starts, and features that drive users to the paywall. Context includes: what content did they just finish? What streak length do they have?

**Level 4: Questions and hypotheses**
What specific questions do teams have about those product experiences? What hypotheses are being tested?
Example: "Do users who complete a 7-day engagement session series before seeing the paywall convert at higher rates?"

### Step 2: Journeys Instead of Metrics

Stop asking "can I calculate all my KPIs with these events?" Start asking "do these events tell me the full story of the user journey — what they intended, what succeeded, and what failed?"

**The three event types:**

#### Success Events
A desired action has been completed. Stems directly from business and team goals.

Success event pressure test: "If 99% of users did this, what would I do?" If you can't answer → the event isn't useful.

Examples for your product:
- `engagement session_completed`
- `streak_achieved` (with property `length: [3|7|14|30|...]`)
- `trial_started`
- `subscription_converted`
- `engagement_request_submitted`

#### Intent Events
Steps required before reaching success. Track the full journey from initial intent to final success.

Intent events answer "why?" around success events. They reveal:
- How many steps the user is navigating
- Which paths users take (and which paths high-converters take vs. drop-offs)
- At what point in the journey users abandon

Examples for your product:
- `engagement session_opened` (intent before `engagement session_completed`)
- `paywall_viewed` (intent before `trial_started`)
- `notification_tapped` (intent before `app_opened`)
- `engagement_category_selected` (intent before `engagement session_opened`)
- `streak_freeze_viewed` (intent before `streak_freeze_used`)

Intent events have levels:
- High intent: `engagement session_content_scrolled` (user is actively reading)
- Lower but meaningful intent: `engagement session_opened` (user started but hasn't committed)

#### Failure Events

**Explicit failures:** Events where the experience goes wrong
- `payment_failed` + property `error_type`
- `subscription_cancellation_initiated` + property `reason`
- `notification_permission_denied`

**Implicit failures:** Drop-offs before a success event
- User `opened_engagement session` but never `completed_engagement session` within 10 minutes → implicit abandonment
- User `viewed_paywall` but never `started_trial` within 48 hours → implicit rejection

Track implicit failures by combining event analysis with time windows.

### Step 3: Properties

Properties are what transform events from "what happened" to "why it happened and for whom."

**Property buckets:**

**User Profile Properties:**
Who is this user at the time of the event?
- `user_tenure_days` — days since account creation
- `subscription_status` — free / trial / subscribed
- `streak_current_length`
- `content_completed_lifetime` — total engagement sessions finished
- `acquisition_source` — how they originally found the app

**Marketing Properties:**
What brought the user to this moment?
- `session_source` — organic / notification / push / email / direct
- `campaign_id` — if from a specific campaign
- `entry_surface` — home screen / deep link / search

**User Action Properties:**
What specific action was taken?
- `content_id` — which content
- `content_type` — engagement session / engagement / music / premium content
- `content_length_minutes`
- `completion_percentage` — 0-100% for partial completions

**Type of Action Properties:**
What variant of the action?
- `signup_method: [google|apple|email]`
- `cancellation_reason: [too_expensive|not_using|found_alternative|other]`
- `notification_type: [streak_reminder|new_content|daily_engagement session|special_event]`

**Contextual Properties:**
What was the environment when the action occurred?
- `hour_of_day` — what time did the user engage?
- `content_recommendations_shown` — how many options were visible?
- `time_since_last_session_hours`

**Property selection test:**
- How will I be able to segment users who were frustrated vs. disinterested?
- How will I be able to identify different paths mature vs. casual users take?
- If this were the last event I ever tracked from a user, what would I want to know?

---

## The Event Tracking Dictionary

The organizational artifact that makes all of this work.

**Required fields for every event:**

| Field | Description |
|-------|-------------|
| **Event Name** | Natural language phrase: "Signup Method Selected" |
| **Triggers when...** | Precise description: "User taps a signup option on the account creation screen" |
| **Screen** | Screenshot of exact screen state when event fires |
| **Properties** | List of property names + data types |
| **Property Values** | Exhaustive list of possible values for each property |
| **Description** | How would you describe this to someone who's never used the product? |
| **Technical Comments** | API quirks, aggregation rules, deduplication notes |
| **Testing Comments** | QA notes, known issues, last verified date |

**What makes a good Event Tracking Dictionary:**
1. **Simple:** Someone new to the company can map events to product screens without reading every definition
2. **Actionable:** A business user can move from the sheet to the data to a decision without analyst involvement
3. **Visual:** Every event has a screenshot

**Maintenance cadence:**
- New feature ship: update dictionary before code ships (not after)
- Quarterly: audit for stale/removed events; clean up duplicates
- Team onboarding: walk new PMs, marketers, and ops through the dictionary as part of onboarding

---

## your product Event Tracking Audit Checklist

Run this before any new analytics investment:

### Activation Funnel Analysis — Procedural Steps

Crystal's step-by-step process for running an activation funnel analysis (from her public Activation Funnel Analysis talks):

**Step 1: Define the four activation funnel stages**
Map your user journey into these four categories:
- **Signup:** Account creation and identity establishment
- **Setup:** Configuration steps required before value delivery (e.g., onboarding preferences, notification permissions)
- **Aha Moment:** The first experience of core product value (e.g., completing first engagement session, hearing first audio content)
- **Habit:** The repeated behavior that signals long-term retention (e.g., 3-day streak, returning for 3+ sessions in week 1)

**Step 2: Identify database tables and columns for each step**
For each funnel stage, identify:
- Which database table contains the event
- Which columns define success at this step
- What timestamp marks completion
- What user properties are available for segmentation at this step

**Step 3: Analyze the funnel output**
- Calculate conversion rate at each step (both step-over-step and cumulative from install)
- Segment the funnel by acquisition source, device, and cohort month
- Identify the single biggest drop-off — that's your first priority
- Look for segments with dramatically different patterns (these reveal opportunities)

**Step 4: Communicate findings to stakeholders**
- Lead with the "so what" — the business implication, not the data
- Show the product screen alongside the metric chart
- Pair every finding with a recommended action
- Present at the right altitude for each audience (exec vs. PM vs. engineer)

**Foundation check:**
- [ ] Every key funnel step has a corresponding event in the analytics system
- [ ] All events have a "triggered when" description
- [ ] All events have corresponding screenshots
- [ ] All events have meaningful properties that enable segmentation
- [ ] Internal/test accounts are filtered from all analyses

**Reliability check:**
- [ ] More users can NOT have completed Step B than Step A when B always follows A
- [ ] Finance and Product agree on "monthly active subscribers" to within 5%
- [ ] The data shows no events firing after account deletion (zombie events)

**Business user check:**
- [ ] A non-technical team member can run their own basic query without analyst help
- [ ] The Event Tracking Dictionary is up-to-date (last reviewed within 90 days)
- [ ] Every tracked event has a clear connection to a business goal or OKR

**Impact check:**
- [ ] In the last quarter, at least 3 product decisions were changed as a result of data analysis
- [ ] Analysis findings are regularly shared in a format decision-makers can act on
- [ ] There is a clear owner for each key metric who is accountable for its movement
