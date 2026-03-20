## Contents
- The Core Error: Data as Team or Tool
- The Strategy → Stage → Team → Tools Framework
  - 1. Strategy: What Are Your Points of Leverage?
  - 2. Stage: What Stage Is the Product At? What Stage Is the Data At?
  - 3. Team: Are the Right People Set Up for Success?
  - 4. Tools: What's Needed to Execute?
- The Three Stages in Full Detail
  - Stage 1: Data Informed
  - Stage 2: Data Driven
  - Stage 3: Data Led
- How to Sequence Between Stages
- The 4 Capabilities Matrix
- Diagnosing your product's Data Maturity Stage

---
# Data Maturity Framework — Deep Reference
*Source: Crystal Widjaja, "The Scaling Data Framework: Data Informed to Data Driven to Data Led," Blog, April 2021; supplemented by her Mind the Product APAC keynote on Data Scaling for Startups*

---

## The Core Error: Data as Team or Tool

The most common mistake in scaling data:

> "Viewing data as a team to hire or a set of tools to implement — instead of a strategic lever for growth."

This leads to asking the wrong questions:
- "Should I hire a data engineer or analyst?" (depends on stage, not preference)
- "Do I need a data scientist right now?" (almost always no, until Stage 3)
- "Should I use Looker?" (depends on whether your team can use self-serve tools yet)

**The right framing:**
Data capabilities should be selected and sequenced based on what the business needs to grow right now — not based on what feels sophisticated or what the last company you worked at used.

---

## The Strategy → Stage → Team → Tools Framework

Always work through these in order, never skip to Team or Tools:

### 1. Strategy: What Are Your Points of Leverage?

Questions to answer before any data investment:
- How much data do our product and operations generate daily?
- How can customer value be improved by leveraging data?
- What kinds of decisions could data inform today?
- How would decision-making change with 1000× the data?
- How much more efficient could operations be with data automation?

**The uncomfortable truth:** Most companies at early stages don't have enough data for advanced ML/data science to be meaningfully impactful. Even the most sophisticated data science team will fail at a company generating insufficient data. There aren't enough signups, retained users, or product actions for meaningful models to exist.

### 2. Stage: What Stage Is the Product At? What Stage Is the Data At?

The mismatch between product stage and data stage is the source of most data dysfunction.

**Data stage assessment questions:**
- How much of our data is tracked, stored, and owned by us?
- Is data tracked at the right granularity (event-based vs. aggregate only)?
- Is data deterministic enough for confident decisions?
- How accessible is the data to both people and systems?
- How timely and accurate is it?

**The overbuilding trap:**
Building data infrastructure ahead of product maturity impedes growth. Crystal's example at Gojek: hired a data scientist to build fraud detection before having enough data — unproductive for weeks. Eventually simple business rules caught 80% of fraud. Years later, those same rules still catch 80%.

> "Stories like these are incredibly common. The shiny, enterprise-level data products prevent companies from making productive use of the data they have."

**The underbuilding trap:**
Equally dangerous. Signals you've underbuilt:
- Multiple products using inconsistent data attributes (different time zone logic, different definitions)
- Months or years of data not tracked at all
- Data stuck in 3rd-party systems you don't own (Firebase: does not store individual event data)
- Business operating with sub-optimal decisions for so long that data culture is broken

The most painful underbuilding scenario: realizing years of data are trapped in a system that doesn't allow export. Crystal's example: a company using Firebase thinking they could "eventually export logs" — Firebase doesn't store individual event data, so they literally wasted years of data collection.

### 3. Team: Are the Right People Set Up for Success?

Team alignment signals (when things aren't working):
- Teams bring hypotheses to the data team to validate, rather than collaborating on both problems and solutions
- Data and product teams are too busy with tactical tasks to align on strategic initiatives
- Analyses are evaluated as "win or not" rather than as findings that move closer to objectives

### 4. Tools: What's Needed to Execute?

Tools are the last consideration, not the first. Tools should be selected to enable the team you have, to execute the strategy you've chosen, at the stage you're at.

Common sequencing mistake: buying Looker or Snowflake before having a data analyst who can use them. The tools sit unused or are adopted superficially without unlocking their value.

---

## The Three Stages in Full Detail

### Stage 1: Data Informed

**Also called:** "Survival" stage (Crystal's Mind the Product APAC framing)

**Company state:** Pre-PMF or just reaching PMF. Building the business, figuring out what works.

**Data's role:** Operational visibility. Know if the business is working.

**Key business needs:**
- Business health monitoring (are we growing?)
- Product KPI visibility (are users doing the right things?)
- Getting to PMF (flattened retention curves)
- Metric definitions and alignment

**Critical success factor:** Single source of truth.

> "The most common pitfall at the data informed stage is being indecisive about the truth and allowing multiple versions to co-exist."

Example: Finance thinks you got 100 new users from Facebook in October. Marketing thinks it's 120. Both are working from different tools, metrics, definitions, time zones, or accounting methods. This friction causes teams to avoid using data altogether.

**Required capabilities at this stage:**

*Infrastructure:*
- Reliable availability of transactional and financial data
- Off-the-shelf visualization and integration tools (Amplitude, Mixpanel, Segment)
- No need for custom data warehouse yet

*Analytics:*
- Company-level KPI dashboards
- Basic retention curves per cohort
- Basic funnel visualization

*Operations:*
- Functional ops support for a handful of multi-disciplinary ICs
- Basic alerting on critical metrics

*Team:*
- Generalist data analyst or PM with strong data skills
- No data scientist needed
- No data engineer needed unless data volume is very high

**Most common mistake at this stage:**
Jumping to Stage 2 tools (data warehouse, experimentation platform) before establishing a single source of truth. The advanced tools amplify the confusion instead of fixing it.

### Stage 2: Data Driven

**Also called:** "Functionality" stage (Crystal's Mind the Product APAC framing)

**Company state:** Post-PMF. Actively scaling, optimizing features, expanding user base.

**Data's role:** Decision-making guidance. Support the organization's growth with scalable tooling and deep insights.

**Key business needs:**
- Feature-level product optimization
- Smarter, faster function-specific business operations
- Data-informed guidance on marketing, growth tactics, support
- Expanded monetization of core and adjacent users

**The organizational shift at Stage 2:**
Teams move from shared responsibility for output metrics (revenue, retention) to accountability for input metrics (feature-specific usage, funnel conversion rates, activation events). This only works if data is reliable and accessible enough to measure input metrics accurately.

**Required capabilities at Stage 2:**

*Infrastructure:*
- Proactive data governance policies
- Scalable data warehouse (Snowflake, BigQuery, Redshift)
- Customer data platform (CDP) for unified user profiles
- Data lake for raw event storage

*Analytics:*
- Self-serve analytics tools (Looker, Metabase, Mode)
- Org-wide experimentation framework (A/B testing infrastructure)
- Reporting standardization (how do teams format and share findings?)
- Deep-dive segmentation and cohort analysis capabilities

*Operations:*
- Feature teams own their metrics and run their own analyses
- Data team focused on infrastructure and strategic questions, not ad hoc queries

*Team:*
- Analytics engineers (build the data models, maintain the warehouse)
- Product analysts (own analytics for specific product areas)
- Data analyst or scientist for strategic questions
- Data PM or Head of Data to coordinate strategy

**The biggest pitfall at Stage 2:**
Misalignment of organizational incentives. If PMs take credit for "asking the right question" without crediting data insights, data teams are incentivized to design pretty tables instead of impactful analysis. Or they seek out interesting but irrelevant questions for the dopamine hit of a clever analysis.

**The fix:** Measure data team success by the impact of analyses on business outcomes, not by analysis volume or question quality.

### Stage 3: Data Led

**Also called:** "Form" stage (Crystal's Mind the Product APAC framing — "data as the form, beyond just functionality")

**Company state:** At significant scale. Operations and product experiences require data products to function.

**Data's role:** Productized data services that automate operational decisions and user experiences.

**Key business needs:**
- Data-leveraged defensibility (data moats)
- Self-serve data onboarding and productization
- Prescriptive, automated operational decision-making
- Deepened engagement and monetization via personalization

**The defining characteristic of Stage 3:**
> "The most differentiated thing about Stage 3 businesses is that they cannot operationally function without data products."

Example: Amazon cannot manage fulfillment, logistics routing, or warehouse SKU storage without proprietary predictive models. The scale and complexity make human-generated recommendations insufficient.

**Required capabilities at Stage 3:**

*Infrastructure:*
- Platformized, self-serve data warehouse
- Feature engineering pipelines to train ML models
- Near-real-time data availability
- Self-service data onboarding (teams can add new data sources without data team involvement)

*Analytics:*
- ML model development and deployment
- Real-time personalization systems
- Automated anomaly detection
- Predictive forecasting

*Operations:*
- Data products run by non-data teams
- Automated operational decision-making (pricing, recommendations, content surfacing)

*Team:*
- Data scientists (ML model development)
- ML engineers (productionize and deploy models)
- Platform engineers (maintain data infrastructure)
- Data governance team

**Important caveat:**
> "Not all companies need to become Data Led."

Stage 3 applies to globally scaled organizations where data dictates operations. Companies with small numbers of SKUs, low-frequency products, or evolving markets may never find Data Led capabilities impactful relative to the investment. Businesses with meaningful traction may reach Stage 3 technically but not benefit strategically from it.

---

## How to Sequence Between Stages

**The governing principle:**
> "A key to success is to not try and enable a stage all at once."

Two forces must stay balanced:
1. Unlocking product insights and business capabilities
2. Scaling data operations and infrastructure

These must advance together. Investing heavily in infrastructure without corresponding analytical capability leaves you with expensive tools generating no insights. Investing heavily in analytics without infrastructure leads to brittle, one-off analyses that don't compound.

**The transition check from Stage 1 → Stage 2:**
- Do you have a single source of truth for all key metrics?
- Do all teams agree on metric definitions?
- Is the data reliable enough that teams trust it without constant verification?
- Have you achieved stable retention curves (PMF)?

If no to any → stay at Stage 1 and fix these first.

**The transition check from Stage 2 → Stage 3:**
- Do you have 50+ data points per day per key user segment for ML models to learn meaningfully?
- Are there operational processes that are impossible to do manually at your current scale?
- Do you have the engineering capacity to productionize ML models?

If no to any → stay at Stage 2 and don't over-invest in Stage 3.

---

## The 4 Capabilities Matrix

For each of the 3 stages, 4 capability areas must evolve:

| Capability | Stage 1: Data Informed | Stage 2: Data Driven | Stage 3: Data Led |
|-----------|----------------------|---------------------|------------------|
| **Infrastructure** | Off-the-shelf tools, basic event tracking | Scalable warehouse, CDP, governance | Real-time, self-serve, ML-ready platform |
| **Analytics** | KPI dashboards, basic retention | Self-serve, experimentation, segmentation | Predictive models, real-time personalization |
| **Operations** | Manual monitoring by generalists | Feature teams own their metrics | Automated decision-making by data products |
| **Team** | Generalist analyst or data-strong PM | Analytics engineers + product analysts | Data scientists + ML engineers + platform team |

---

## Diagnosing your product's Data Maturity Stage

**Evidence for Stage 2 (Data Driven):**
- Post-PMF (subscription product with paying users indicates PMF was found)
- Daily engagement product with meaningful event volume
- Active growth and optimization work happening
- Paid acquisition campaigns requiring attribution and measurement

**Capabilities to prioritize at Stage 2:**
1. Self-serve analytics for PMs and marketers (can they run their own cohort analysis without analyst help?)
2. A/B experimentation infrastructure (can teams test product changes rigorously?)
3. Feature-level analytics ownership (does each PM own specific metrics?)
4. Deep segmentation of key funnel metrics (activation, trial conversion, subscription retention)

**What NOT to do at Stage 2:**
- Don't hire data scientists — simple rules and correlations will outperform ML at this scale
- Don't build a custom data platform — off-the-shelf tools (Mixpanel/Amplitude + a BI tool) are sufficient
- Don't try to build real-time data systems — batch/daily refresh is fine for product decisions

**Monetization analytics to explore at Stage 2:**
- Track and segment by subscription plan type (weekly vs. monthly vs. annual) — industry data shows weekly+trial configurations generate highest 12-month LTV
- Analyze whether hybrid monetization (subscriptions + one-time purchases for premium content) could capture revenue from non-subscribers
- Monitor cancellation timing — ~44% of cancellations happen in the first 90 days, so early subscriber engagement analytics are critical
