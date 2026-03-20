## Contents
- CDP Deep Dive
  - What a CDP Actually Does
  - The CDP Landscape Has Evolved
  - CDP Selection for your product
- Event Taxonomy Design
  - Why Event Taxonomy Is the Foundation
  - Event Naming Convention
  - Event Categories for your product
  - Event Property Standards
  - Event Taxonomy Governance
- Data Pipeline Architecture
  - The Three Pipeline Types
  - Pipeline Architecture for your product
- Identity Resolution
  - The Identity Challenge
  - Identity Resolution Strategies
  - Identity Resolution for your product
- Data Quality Monitoring
  - The Data Quality Dashboard
  - Common Data Quality Issues
  - Data Quality Checklist (Monthly)

---
# CDP and Data Infrastructure

**Source framework:** Austin Hay's Mastering Marketing Technology course, supplemented by his Lenny's Podcast interview, Hightouch interview on the evolution of martech, and his frameworks for CDP evaluation, event taxonomy design, and data pipeline architecture.

---

## CDP Deep Dive

### What a CDP Actually Does

A Customer Data Platform is the central nervous system of a modern martech stack. At its core, a CDP performs five functions:

1. **Data Collection** -- Ingest events and user attributes from all sources
2. **Identity Resolution** -- Stitch anonymous and known user profiles across devices and sessions
3. **Profile Unification** -- Build a single customer record combining all data sources
4. **Segmentation** -- Create audiences based on any combination of attributes and behaviors
5. **Activation** -- Send segments, events, and profiles to downstream tools

### The CDP Landscape Has Evolved

Hay notes that the CDP landscape has shifted dramatically. The B2C stack was largely standardized between 2017 and 2020, with the rise of CDPs. But by 2021, it became cost-efficient to operate a data team with your own warehouse and to manage data centrally.

This creates three distinct CDP approaches:

**Approach 1: Standalone CDP (Traditional)**
The CDP is a separate platform that collects, stores, and activates data.

| Tool | Strengths | Limitations |
|------|-----------|-------------|
| Segment | Best-in-class event collection, broad integration library | Segmentation is basic; expensive at scale |
| mParticle | Strong mobile focus, good identity resolution | Smaller integration library than Segment |
| RudderStack | Open-source option, warehouse-native | Smaller team, less enterprise support |

**Approach 2: Campaign CDP (All-in-One)**
The campaign platform IS the CDP -- it collects data, builds profiles, and sends messages.

| Tool | Strengths | Limitations |
|------|-----------|-------------|
| Braze | Strong mobile push/email + user profiles | Not as flexible for routing data to non-Braze tools |
| Iterable | Good cross-channel + data model | More email-centric than mobile-centric |
| Customer.io | Simple, developer-friendly | Less sophisticated for enterprise use cases |

**Approach 3: Warehouse-Native CDP (Composable)**
The data warehouse (Snowflake, BigQuery) is the CDP. Reverse ETL tools push segments to activation tools.

| Tool | Strengths | Limitations |
|------|-----------|-------------|
| Hightouch | SQL-based audiences, warehouse as source of truth | Requires existing warehouse infrastructure |
| Census | Similar to Hightouch, strong Salesforce integration | Smaller company |
| dbt + Hightouch | Transformation + activation in one workflow | Requires analytics engineering talent |

### CDP Selection for your product

**Decision framework:**

```
Do you already have a data warehouse with clean user data?
+-- Yes
|   +-- Do you need real-time event routing?
|   |   +-- Yes --> Segment + Hightouch (event routing + warehouse activation)
|   |   +-- No --> Hightouch alone (warehouse-native CDP)
|   +-- Is your primary need segmentation for campaigns?
|       +-- Yes --> Hightouch (SQL audiences pushed to Braze)
|       +-- No --> Evaluate based on specific need
+-- No
    +-- Do you need both event routing AND campaign messaging?
    |   +-- Yes --> Braze (campaign CDP -- collect + message in one)
    |   +-- No, just event routing --> Segment (routes to all destinations)
    +-- What's your budget?
        +-- <$50K/year --> Segment (starter tier) or Customer.io
        +-- $50-150K/year --> Segment + Braze
        +-- $150K+/year --> Full stack (Segment + Braze + Snowflake + Hightouch)
```

**Recommended for your product:** Segment for event collection and routing + Braze for campaign CDP + Snowflake for warehouse + Hightouch for reverse ETL (activate warehouse data). This gives maximum flexibility: real-time event routing via Segment, campaign execution via Braze, deep analysis via Snowflake, and warehouse-to-tool activation via Hightouch.

---

## Event Taxonomy Design

### Why Event Taxonomy Is the Foundation

The event taxonomy is the naming convention and schema for every user action you track. It's the foundation of your entire martech stack because every downstream tool -- analytics, campaigns, segmentation, personalization, attribution -- depends on clean, consistent event data.

**The cost of getting it wrong:**
- Analytics are unreliable (different tools interpret events differently)
- Campaigns target the wrong users (segmentation based on inconsistent data)
- Personalization fails (recommendations based on noisy data)
- Attribution is inaccurate (conversion events don't match across tools)
- Technical debt compounds (fixing a taxonomy at scale requires touching every integration)

### Event Naming Convention

**Pattern: Object Action (two words, capitalized)**

```
Good:
- Engagement Session Viewed
- Engagement Session Completed
- Engagement Created
- Subscription Started
- Trial Started
- Content Shared
- Push Notification Opened
- Paywall Viewed
- Group Joined
- Profile Updated

Bad:
- viewed_engagement session (inconsistent format)
- userClickedPlayButton (too specific, too technical)
- page_view (too generic, no context)
- convert (ambiguous -- convert to what?)
- subscription (is this started? renewed? cancelled?)
```

### Event Categories for your product

**Core Content Events:**
```
Engagement Session Viewed
Engagement Session Started
Engagement Session Completed
Engagement Session Paused
Engagement Session Resumed
Engagement Session Shared
Content Opened
Content Read
Engagement Created
Engagement Updated
Engagement Answered (marked by user)
```

**Monetization Events:**
```
Paywall Viewed
Paywall Dismissed
Trial Started
Trial Extended
Subscription Started
Subscription Renewed
Subscription Cancelled
Subscription Restarted
Payment Failed
Payment Recovered
```

**Engagement Events:**
```
App Opened
App Backgrounded
Session Started
Session Ended
Search Performed
Content Browsed
Category Viewed
Notification Received
Notification Opened
Notification Dismissed
```

**Social/Community Events:**
```
Group Created
Group Joined
Group Left
Group Invite Sent
Group Invite Accepted
Community Request Shared
Community Request Supported (by other user)
Comment Created
Content Recommended
```

**Account Events:**
```
Account Created
Profile Updated
Preferences Set
Notification Settings Changed
Subscription Settings Changed
Account Deleted
```

### Event Property Standards

Every event should include a standard set of properties plus event-specific properties:

**Standard properties (included with every event):**
```json
{
  "event": "Engagement Session Completed",
  "timestamp": "2024-03-15T08:23:41Z",
  "user_id": "usr_abc123",
  "anonymous_id": "anon_xyz789",
  "platform": "ios",
  "app_version": "4.2.1",
  "os_version": "17.3",
  "device_type": "iPhone 15",
  "session_id": "sess_def456"
}
```

**Event-specific properties:**
```json
{
  "engagement session_id": "dev_2024_0315",
  "engagement session_title": "Finding Peace in Uncertainty",
  "content_type": "audio",
  "content_format": "guided_engagement",
  "duration_seconds": 420,
  "completion_percent": 100,
  "category": "anxiety",
  "series_name": "Daily Calm",
  "is_premium": true,
  "author": "Jane Smith",
  "position_in_series": 3
}
```

**User properties (attached to the user profile, updated with each event):**
```json
{
  "subscription_status": "premium_annual",
  "subscription_start_date": "2023-09-01",
  "trial_status": "converted",
  "days_since_signup": 196,
  "total_engagement sessions_completed": 89,
  "current_streak_days": 14,
  "longest_streak_days": 45,
  "preferred_content_type": "audio",
  "preferred_time_of_day": "morning",
  "preferred_categories": ["anxiety", "gratitude", "daily_bread"],
  "groups_joined": 2,
  "lifetime_engagement_requests": 12,
  "acquisition_source": "facebook_ads",
  "acquisition_campaign": "seasonal_2024"
}
```

### Event Taxonomy Governance

**Before implementation:**
- Every new event must be documented in the taxonomy registry
- Documentation includes: event name, description, when it fires, all properties with types and descriptions
- Taxonomy review by martech owner before engineering implements

**During implementation:**
- Use a tracking plan tool (Segment Protocols, Avo, or a shared spreadsheet)
- Validate events match the schema before sending to production
- Include schema version in event metadata

**After implementation:**
- Quarterly audit: Are events still firing correctly?
- Quarterly audit: Are deprecated events removed?
- Monitor for anomalies: Sudden drops in event volume indicate broken tracking
- Monitor property completeness: What % of events have all required properties?

---

## Data Pipeline Architecture

### The Three Pipeline Types

**1. Real-Time Pipeline (Streaming)**
Events flow from source to destination in near-real-time (<1 second).

- Use for: Push notification triggers, in-app personalization, real-time segmentation
- Technology: CDP event streaming (Segment, mParticle)
- your product example: User completes their 7th engagement session --> trigger premium trial offer push notification immediately

**2. Near-Real-Time Pipeline (Micro-Batch)**
Events are processed in small batches every 1-15 minutes.

- Use for: Campaign audience updates, analytics dashboards, engagement scoring
- Technology: CDC (Change Data Capture) tools, streaming ETL
- your product example: User's subscription status changes --> update their profile in Braze within 5 minutes

**3. Batch Pipeline (Scheduled)**
Data is processed in large batches on a schedule (hourly, daily).

- Use for: ML model training, BI reporting, complex segmentation, data warehouse updates
- Technology: dbt, Airflow, ELT tools (Fivetran, Airbyte)
- your product example: Nightly job calculates each user's churn risk score and updates it in the warehouse

### Pipeline Architecture for your product

```
REAL-TIME PIPELINE:
App Events --> Segment --> Braze (immediate triggers)
                       --> Amplitude (real-time analytics)

NEAR-REAL-TIME PIPELINE:
Segment --> Snowflake (events land in staging tables)
Billing System --> Snowflake (subscription changes via Fivetran)

BATCH PIPELINE (nightly):
Snowflake --> dbt transforms --> Computed user profiles
    --> Hightouch --> Braze (enriched user profiles for segmentation)
    --> Hightouch --> Meta Custom Audiences (for ad targeting)
    --> Hightouch --> Looker (BI dashboards)

BATCH PIPELINE (weekly):
Snowflake --> ML Models --> Churn risk scores, content recommendations
    --> Hightouch --> Braze (churn risk segment, recommended content)
```

---

## Identity Resolution

### The Identity Challenge

A single your product user may have multiple identities:
- Anonymous app visitor (before account creation)
- Anonymous web visitor (different device)
- Known user (after signup, with email)
- Known user on a second device (logged in elsewhere)

Identity resolution stitches these into a single profile.

### Identity Resolution Strategies

**Strategy 1: Deterministic Matching**
Match profiles when they share a known identifier (email, user ID, phone number).

- Highest accuracy, lowest coverage
- Works when users log in across devices
- your product: When a user logs into the app on a new device, merge the profiles

**Strategy 2: Probabilistic Matching**
Match profiles based on statistical likelihood (device fingerprint, IP address, behavioral patterns).

- Lower accuracy, higher coverage
- Useful for pre-login identity stitching
- your product: Match an anonymous web visitor to a known app user if they share an IP and browse similar content

**Strategy 3: Hybrid**
Use deterministic when available, probabilistic as fallback.

- Best balance of accuracy and coverage
- Most CDPs use this approach
- your product: Default approach -- let the CDP handle it

### Identity Resolution for your product

**Key identity events:**
1. Anonymous Install --> First app open (anonymous ID assigned)
2. Account Creation --> Email provided (known user ID)
3. Second Device Login --> Merge with existing profile
4. Web Visit --> Anonymous web ID, merge if user logs in

**Implementation:**
- Use Segment's `identify()` call when user signs up or logs in
- Pass both `anonymous_id` and `user_id` to enable stitching
- Ensure consistent `user_id` format across all platforms
- Set up alias calls for known identity merges (e.g., web to app)

---

## Data Quality Monitoring

### The Data Quality Dashboard

Monitor these metrics continuously:

| Metric | What It Measures | Alert Threshold |
|--------|-----------------|-----------------|
| Event Volume | Total events per hour/day | >20% deviation from 7-day average |
| Event Completeness | % of events with all required properties | <95% |
| Identity Resolution Rate | % of events tied to a known user | Falling trend |
| Latency | Time from event to destination | >5 seconds for real-time, >1 hour for batch |
| Integration Health | % of destinations receiving data | <100% |
| Duplicate Rate | % of duplicate events detected | >1% |
| Schema Violations | Events that don't match the expected schema | Any above 0 |

### Common Data Quality Issues

**Issue 1: Missing Events**
- Symptom: Event volume suddenly drops
- Causes: SDK update broke tracking, app version issue, integration disabled
- Fix: Set up volume anomaly alerts, investigate immediately

**Issue 2: Property Drift**
- Symptom: A property that used to be populated is now frequently null
- Causes: App update changed event implementation, A/B test altered flow
- Fix: Automated schema validation, property completeness monitoring

**Issue 3: Duplicate Events**
- Symptom: Same event fires multiple times for single user action
- Causes: SDK retry logic, network issues, implementation bug
- Fix: Deduplication logic in the pipeline (use event ID + timestamp)

**Issue 4: Identity Fragmentation**
- Symptom: Single users appear as multiple profiles
- Causes: Identity calls not implemented correctly, anonymous IDs not merged
- Fix: Audit identity resolution logic, ensure identify() calls on every login

### Data Quality Checklist (Monthly)

- [ ] Review event volume trends -- any unexpected changes?
- [ ] Check property completeness rates -- any degradation?
- [ ] Verify all integrations are active and healthy
- [ ] Spot-check 10 random user profiles -- do they look correct?
- [ ] Review new events added this month -- do they follow the taxonomy?
- [ ] Check for deprecated events still firing
- [ ] Verify identity resolution rates -- any increase in fragmented profiles?
- [ ] Test critical event paths end-to-end (install to subscription)
