## Contents
- Source Context
- The Velocity Equation
- Scope Optimization: The Primary Velocity Lever
  - The Over-Scoping Problem
  - The Scope Ladder
  - Scope Ladder Example for your product
- Reusable Growth Patterns
  - Pattern 1: Configurable Paywall
  - Pattern 2: Onboarding Framework
  - Pattern 3: Lifecycle Notification Engine
  - Pattern 4: Referral and Sharing System
- The Tent vs. Skyscraper Quality Model
  - When to Build a Tent
  - When to Build a Skyscraper
  - The Transition Process
- Technical Debt Management
  - The Debt Accumulation Problem
  - The 20-30% Rule
  - Cleanup Cadence
- Going Fast: Practical Tips
  - 1. Server-Driven UI for Growth Surfaces
  - 2. Parallel Experimentation
  - 3. Template-Based Experiment Creation
  - 4. Automated Experiment Lifecycle
  - 5. Reduce Deployment Friction
- The AI Opportunity in Growth Engineering
  - Dynamic Content Optimization
  - Automated Experimentation
  - Strategic Pattern Recognition
  - The Important Caveat
  - The Future Growth Engineer
- your product Velocity Assessment

---
# Growth Engineering Patterns and Velocity

## Source Context

This reference synthesizes velocity optimization and design pattern frameworks from Alexey Komissarouk's Mastering Growth Engineering course, his growth engineering advisory practice, and his Martech Family interview. The central premise: since most experiments fail (~70%), the primary lever for growth output is experiment velocity -- how many well-designed experiments you can run per unit time.

---

## The Velocity Equation

```
Growth Output = Experiment Velocity x Win Rate x Average Impact per Win
```

- **Win Rate** is hard to improve directly (it comes from better intuition, which comes from running more experiments -- a chicken-and-egg problem)
- **Average Impact per Win** is largely determined by the product and market
- **Experiment Velocity** is the variable you can most directly control through engineering practices

If you double your experiment velocity, you double your expected growth output. This is why going fast is the single most important growth engineering capability.

---

## Scope Optimization: The Primary Velocity Lever

### The Over-Scoping Problem

Engineers are trained to build complete, robust, scalable systems. This training is counterproductive in growth engineering, where the goal is to learn -- not to build a permanent system. Over-scoping is the number one killer of experiment velocity.

**Signs of over-scoping:**
- An experiment takes more than 2 weeks of engineering time
- The team is building features "because users might want them later"
- Edge cases are being handled before the hypothesis is validated
- The engineer is building for scale before proving the concept works

### The Scope Ladder

Komissarouk teaches a progressive scoping model: start with the cheapest test that generates a valid signal, and only invest more if the signal is positive.

**Level 1: Painted Door Test (hours)**

Build nothing functional. Show a UI element (button, banner, link) that suggests a feature exists. Measure how many users interact with it.

What it proves: demand exists (or does not exist).
What it does NOT prove: that the feature will improve the target metric when fully built.

Examples:
- A "Share with a friend" button that shows a "Coming soon" modal when tapped
- A "Community groups" section on the home screen that shows "Join the waitlist" when tapped
- A premium badge next to certain content that shows upgrade options when tapped

Criteria for success: >10-15% of exposed users interact with the element.

**Level 2: Wizard of Oz Test (days)**

Build a thin interface, but handle the backend manually. The user thinks they are interacting with an automated system, but behind the scenes, a human (or simple script) is doing the work.

What it proves: the user experience is valuable. Users will complete the flow and benefit from the outcome.
What it does NOT prove: that you can deliver this at scale.

Examples:
- A "personalized engagement session recommendation" that is actually hand-picked by a content editor
- A "accountability partner matching" feature where matching is done manually
- A "daily verse" notification where content is selected manually each day

Criteria for success: meaningful engagement and retention improvement among test users.

**Level 3: MVP Experiment (1-2 weeks)**

Build the minimum functional version. Take shortcuts: hardcode values, skip edge cases, limit to one platform, use existing UI components without customization.

What it proves: the feature works and improves the target metric when delivered by real technology.
What it does NOT prove: that it works at full scale, across all segments, in all edge cases.

Examples:
- A sharing flow that generates a basic deep link and pre-composed message (no custom share images, no landing page optimization)
- A streak counter that tracks consecutive daily completions (no grace days, no visual flourish, no rewards)
- A paywall variant with different copy and pricing (hardcoded, not CMS-driven)

Criteria for success: statistically significant improvement in the target metric via A/B test.

**Level 4: Scaled Solution (4-8 weeks)**

Build the production-quality version: full error handling, edge cases, scalability, observability, localization, accessibility.

When to invest: only after Level 3 has proven the hypothesis with a statistically significant result.

### Scope Ladder Example for your product

Hypothesis: "Users want to share community requests with specific friends, not just the community."

| Scope Level | Implementation | Cost |
|-------------|---------------|------|
| Painted Door | "Share with a friend" button shows "Coming soon!" | 2 hours |
| Wizard of Oz | Button sends pre-formatted text message; responses routed manually | 1 day |
| MVP | Basic sharing flow with deep link, no notification preferences | 1 week |
| Scaled | Full sharing with preferences, notifications, threading, moderation | 4-6 weeks |

Start at Painted Door. If 15%+ of users tap, move to Wizard of Oz. If engagement is strong, build the MVP. Only invest 4-6 weeks if the MVP proves the hypothesis.

---

## Reusable Growth Patterns

Building a library of reusable components is the second-biggest velocity lever after scope optimization. Each pattern reduces time-to-ship for future experiments on the same surface.

### Pattern 1: Configurable Paywall

The paywall is the highest-leverage growth surface for a subscription app. Building it as a configurable component enables rapid experimentation.

**Architecture:**
```
PaywallComponent
+-- Config (fetched from server or feature flag)
|   +-- layout: "fullscreen" | "bottomsheet" | "inline" | "banner"
|   +-- headline: string (A/B testable)
|   +-- body: string (A/B testable)
|   +-- imageUrl: string (A/B testable)
|   +-- ctaText: string (A/B testable)
|   +-- plans: Plan[] (prices, billing periods)
|   +-- selectedPlanDefault: "monthly" | "annual"
|   +-- showSocialProof: boolean
|   +-- showFreeTrial: boolean
|   +-- trialDuration: number (days)
+-- Analytics (built-in)
|   +-- paywall_impression (with config variant)
|   +-- paywall_plan_selected
|   +-- paywall_cta_tapped
|   +-- paywall_dismissed
|   +-- paywall_purchase_completed
+-- Trigger Logic
    +-- triggerAfterNActions: number
    +-- triggerAfterNDays: number
    +-- triggerOnContentType: string[]
    +-- triggerMaxFrequency: "once_per_session" | "once_per_day" | "once"
```

**Value:** With this component, launching a new paywall experiment requires zero engineering time -- the PM or growth analyst configures a new variant through the feature flag system.

### Pattern 2: Onboarding Framework

**Architecture:**
```
OnboardingFlow
+-- Steps[] (ordered, configurable)
|   +-- type: "welcome" | "question" | "tutorial" | "permission" | "paywall"
|   +-- content: StepContent (headline, body, image, options)
|   +-- required: boolean
|   +-- skipCondition: UserSegment (skip if already known)
|   +-- branchLogic: BranchRule[] (if answer = X, show step Y next)
+-- Progress Indicator (step N of M)
+-- Analytics (per-step)
|   +-- onboarding_step_viewed
|   +-- onboarding_step_completed
|   +-- onboarding_step_skipped
|   +-- onboarding_flow_completed
+-- Resume Logic (if user drops off, resume where they left)
```

**Key experiments enabled:**
- Different step orderings (does asking denomination first improve personalization?)
- Different numbers of steps (3-step vs. 5-step)
- Different content at each step (aspirational vs. functional messaging)
- Different permission request placement (in onboarding vs. after first engagement session)

### Pattern 3: Lifecycle Notification Engine

**Architecture:**
```
NotificationEngine
+-- Trigger Definitions
|   +-- Event-based: "user_completed_engagement session" -> send follow-up 6 hours later
|   +-- Time-based: "daily_engagement session_reminder" -> send at user's preferred time
|   +-- Behavioral: "user_inactive_3_days" -> send re-engagement message
|   +-- Milestone: "user_streak_7_days" -> send celebration message
+-- Content Templates
|   +-- template: string (with personalization tokens: {{user.name}}, {{content.title}})
|   +-- variants: ContentVariant[] (A/B testable)
|   +-- locale: string (for internationalization)
+-- Delivery Logic
|   +-- channel: "push" | "email" | "in_app" | "sms"
|   +-- sendTimeOptimization: boolean (ML-based optimal send time)
|   +-- frequencyCap: number (max messages per day/week)
|   +-- quietHours: TimeRange (do not send between 10pm-7am)
+-- Analytics
    +-- notification_sent
    +-- notification_delivered
    +-- notification_opened
    +-- notification_action_taken
    +-- notification_opt_out
```

### Pattern 4: Referral and Sharing System

**Architecture:**
```
ReferralSystem
+-- Share Mechanisms
|   +-- DeepLink: unique referral link per user
|   +-- ShareSheet: pre-composed message with referral link
|   +-- SocialShare: platform-specific (WhatsApp, iMessage, Twitter)
|   +-- QRCode: for in-person sharing
+-- Referral Tracking
|   +-- referrer_id, referred_id, channel, timestamp, conversion
+-- Incentive Logic
|   +-- referrerReward: RewardConfig (unlock content, free month, badge)
|   +-- referredReward: RewardConfig (extended trial, discount)
|   +-- triggerCondition: "install" | "signup" | "subscribe"
|   +-- fraudPrevention: FraudRules (max referrals, device fingerprint)
+-- Analytics
    +-- share_initiated, share_completed
    +-- referral_link_clicked, referral_installed, referral_subscribed
    +-- k_factor (computed: referral_subscribed / active_users per period)
```

---

## The Tent vs. Skyscraper Quality Model

### When to Build a Tent

Tent code is experiment code. It is built to generate a valid signal quickly and then be discarded.

**Tent code standards:**
- MUST have: correct analytics tracking (if the data is wrong, the experiment is worthless)
- MUST have: proper A/B test integration (users correctly assigned to variants)
- MUST have: a clean removal path (can you delete this code without breaking anything?)
- ACCEPTABLE: hardcoded values, limited error handling, single-platform only
- ACCEPTABLE: minimal test coverage (manual QA for the happy path)
- ACCEPTABLE: temporary UI that does not match the design system perfectly

**Tent code lifespan:** 2-4 weeks. If the experiment wins, the code is rewritten as skyscraper code. If it loses, the code is deleted.

### When to Build a Skyscraper

Skyscraper code is production code for proven winners. It is built to last.

**Skyscraper code standards:**
- Full error handling and edge case coverage
- Performance optimization (lazy loading, caching, pagination)
- Proper code review and documentation
- Automated test coverage (unit, integration, key E2E paths)
- Design system compliance
- Accessibility compliance
- Localization support
- Observability (logging, monitoring, alerting)

**Skyscraper code lifespan:** Months to years.

### The Transition Process

When an experiment wins:
1. **Document the winning variant**: exact behavior, metrics impact, edge cases discovered
2. **Create a productionization ticket**: explicitly scoped to bring experiment code to production quality
3. **Allocate dedicated time**: schedule productionization in the current or next sprint -- do not "improve later"
4. **Code review**: senior engineer reviews with production code standards
5. **Remove experiment code**: delete losing variant, remove feature flag, clean up conditionals

---

## Technical Debt Management

### The Debt Accumulation Problem

Growth teams accumulate technical debt faster than any other team because:
- High volume of experiments (each leaves code behind)
- Speed-over-quality tradeoffs (tent code has more shortcuts)
- Feature flags accumulate (stale flags create combinatorial complexity)
- Losing experiments may not be cleaned up promptly
- Winning experiments may run in "experiment mode" for months without productionization

### The 20-30% Rule

Komissarouk recommends dedicating 20-30% of growth engineering time to cleanup and infrastructure:

**10% Experiment Cleanup:**
- Remove losing experiment code
- Remove stale feature flags
- Consolidate experiment remnants

**10% Productionization:**
- Rewrite winning experiment code to production standards
- Add proper error handling, tests, documentation
- Integrate into main codebase with proper review

**10% Infrastructure:**
- Improve experimentation platform
- Enhance analytics tracking
- Build or improve reusable growth patterns
- Optimize build and deploy pipeline

### Cleanup Cadence

**Weekly (sprint planning):** Identify concluded experiments. Assign cleanup tickets for losers, productionization tickets for winners.

**Monthly (growth review):** Audit stale feature flags (any flag >30 days old with no active experiment). Review accumulated debt and prioritize cleanup.

**Quarterly (strategy planning):** Major infrastructure investments. Architectural refactoring. Performance optimization of growth-critical paths.

---

## Going Fast: Practical Tips

### 1. Server-Driven UI for Growth Surfaces

Build growth surfaces (paywall, onboarding, notifications) as server-driven UI:
- Content, layout, and configuration fetched from the server
- Changes do not require app store deployment
- A/B test variants are server-side configurations
- Instant rollback if something goes wrong

This eliminates the biggest bottleneck for mobile apps: the app store review cycle.

### 2. Parallel Experimentation

Run multiple experiments simultaneously on different surfaces:
- Onboarding experiment + paywall experiment + notification experiment (all in parallel)
- Ensure experiments are orthogonal (do not test overlapping surfaces simultaneously)
- Track interaction effects between concurrent experiments

### 3. Template-Based Experiment Creation

Create templates for common experiment types:
- "New paywall variant" template: copy config, change copy/images, launch
- "New onboarding step" template: add step to config, set A/B test, launch
- "New notification" template: define trigger, write copy, set targeting, launch

Each template should include pre-defined analytics events, pre-calculated sample sizes, and automated health checks.

### 4. Automated Experiment Lifecycle

```
Experiment Created -> Automated Validation (sample size, metrics, guardrails)
    -> Launched -> Health Monitoring (daily automated checks)
    -> Reached Sample Size -> Automated Analysis
    -> Results Published -> Decision Prompt (ship, iterate, kill)
    -> Decision Made -> Cleanup Ticket Auto-Created
```

### 5. Reduce Deployment Friction

**For mobile apps:**
- Feature flags to separate deploy from release
- Over-the-air updates where possible (React Native, CodePush)
- Frequent app store submissions (weekly)

**For web:**
- Continuous deployment (merge to main = deploy)
- Feature flags for gradual rollout
- Instant rollback capability

---

## The AI Opportunity in Growth Engineering

Komissarouk identifies AI as a significant growth multiplier:

### Dynamic Content Optimization
AI can personalize content -- headlines, push notifications, email copy -- across multiple languages and segments at scale. What previously required massive human effort can now be done semi-autonomously.

### Automated Experimentation
Emerging tools can manage landing page flows with minimal human oversight. AI agents can ideate experiment variations, generate copy, and set up test infrastructure. The growth engineer's role shifts from building each experiment to overseeing the system that generates experiments.

### Strategic Pattern Recognition
AI can analyze vast datasets to uncover opportunities: which content types correlate with retention in which segments, which notification sequences produce the best reactivation, which onboarding paths lead to the highest LTV.

### The Important Caveat
Human oversight remains essential. AI agents may generate ideas that do not align with brand values. For a consumer app, any AI-generated content must be reviewed for foundational accuracy and brand alignment.

### The Future Growth Engineer
As code generation becomes more automated, the value of a growth engineer lies increasingly in understanding the business and using that insight to move key metrics. Future growth engineers will function as translators -- bridging technical execution with business impact.

---

## your product Velocity Assessment

**Current bottlenecks (likely):**
1. App store deployment cycle (iOS review limits iteration speed)
2. Lack of server-driven UI for growth surfaces
3. Manual experiment analysis (no automated significance detection)
4. No reusable growth component library

**Priority investments:**
1. Server-driven paywall (could 3x paywall experiment velocity alone)
2. Feature flag platform (Statsig, LaunchDarkly) for remote A/B testing
3. Configurable notification engine with behavioral triggers
4. Experiment lifecycle automation (sample size, health monitoring, significance)

**Target velocity:**
- Month 1-2: 1 experiment per week (building infrastructure)
- Month 3-4: 2 experiments per week (infrastructure maturing)
- Month 5+: 3-4 experiments per week (full velocity, parallel experimentation)
