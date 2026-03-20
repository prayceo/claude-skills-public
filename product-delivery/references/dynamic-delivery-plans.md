## Contents
- The Problem with Existing Approaches
- The Five Components
  - 1. Complexity Assessment
  - 2. Effort Estimation
  - 3. Sequencing
  - 4. Milestone Definition
  - 5. Tradeoff Guardrails
- Dynamic Delivery Plan Template
- Resource Tradeoffs (Brooks's Law)
- Common Failure Modes

---
# Dynamic Delivery Plans

> Source: Andy Johns and Matt Greenberg, Mastering Product Delivery

---

## The Problem with Existing Approaches

**Agile sprints fail big bets** because: visibility horizon too short, no structural accountability for the whole initiative, cross-team dependencies invisible, stakeholder communication breaks down ("23 story points" does not answer "will this ship by Q3?").

**Waterfall fails big bets** because: requirements change as you learn, false precision creates false confidence, communication ossifies, late integration surprises.

**The insight:** Borrow structured planning and communication from waterfall with adaptive scope and iterative learning from agile. The Dynamic Delivery Plan makes this explicit.

---

## The Five Components

### 1. Complexity Assessment

**Four Levels:**
- **Straightforward:** Done before, familiar stack, clear requirements
- **Normal:** Similar prior experience, some open questions
- **Complicated:** Novel, significant unknowns, cross-team dependencies
- **Very Complicated:** Unprecedented, major unknowns, need research/prototyping

**Four Factors:** Scale (users/systems affected), Magnitude (surface UI vs. core architecture), Stability (of requirements), Access (needed data/APIs/infrastructure).

A project Straightforward on three factors but Very Complicated on one is effectively Complicated overall.

### 2. Effort Estimation

Match approach to complexity:
- **Straightforward:** Story points calibrated to recent velocity
- **Normal:** T-shirt sizes mapped to historical data
- **Complicated:** Time-boxed spike (1-3 days), then optimistic/likely/pessimistic ranges
- **Very Complicated:** Throwaway prototype (1-2 weeks), then 2-3x wide range

**Anti-pattern: "Precision theater."** 37 story points for a Very Complicated initiative implies confidence that does not exist. Better: "4-8 weeks with these three unknowns. After Week 2, we resolve the biggest and narrow the range."

> For basic scoping and estimation practices (document templates, t-shirt sizing, anti-patterns), see **technical-foundations**.

### 3. Sequencing

**Risk-First:** Front-load hardest, most uncertain work. Fail early and cheaply.

**Value-First:** When uncertainty is low, deliver user value incrementally.

**Dependency-Aware:** Map all dependencies with owning team and expected date. Add 50% buffer for external teams. Identify critical path. Sequence to resolve critical-path dependencies first.

### 4. Milestone Definition

3-5 milestones per big bet. Each must:
1. Represent a meaningful product state (not "Phase 1 done")
2. Have clear exit criteria (objectively testable)
3. Trigger a checkpoint review
4. Enable a go/no-go decision

| Initiative Length | Milestones |
|------------------|-----------|
| 1-2 months | 3 |
| 3-4 months | 4-5 |
| 5-6 months | 5-7 |
| >6 months | Break into separate initiatives |

### 5. Tradeoff Guardrails

Pre-establish at initiative start: "[DIMENSION] is fixed. [DIMENSION] is flex lever. [DIMENSION] has floor of [THRESHOLD]."

**Delivery Time:** Fixed when external deadline. Flexible when value does not decay.
**Scope:** Fixed when minimum feature set required for value. Flexible when smaller version delivers value.
**Quality:** Fixed for trust-sensitive areas (payments, health, personal content). Flexible for internal tools.

> For tradeoff decision-making frameworks (options matrices, reversibility, stakeholder alignment), see **technical-strategy**.

---

## Dynamic Delivery Plan Template

```
INITIATIVE: [Name]
COMPLEXITY: [Level]
CONVICTION: [Painkiller with hard commitment / etc.]

TRADEOFF GUARDRAILS:
- Fixed: [Dimension]
- Flex: [Dimension]
- Floor: [Dimension] minimum = [Threshold]

ESTIMATE: [Optimistic] / [Likely] / [Pessimistic]
KEY UNKNOWNS:
1. [Unknown -- resolved by Milestone X]

DEPENDENCIES:
- [Dependency]: Owner=[Team], Expected=[Date], Buffer=[Days]

MILESTONES:
M1: [Name] -- [Exit Criteria] -- Target: [Date]
M2: ...

KILL CRITERIA: [Conditions under which we stop]

SEQUENCE:
Week 1-2: [Work items -- rationale]
Week 3-4: [Work items]
...
```

---

## Resource Tradeoffs (Brooks's Law)

**When adding people helps:** Remaining work is genuinely parallelizable, new people already know codebase, sufficient onboarding runway.

**When adding people hurts:** Work is deeply interconnected, onboarding taxes existing team, critical path is not parallelizable.

**Default for slips:** (1) Reduce scope, (2) extend timeline, (3) add resources only when genuinely parallelizable.

---

## Common Failure Modes

**Planning as one-time event:** Plan must be updated throughout execution.
**Estimating without spikes:** For Complicated+ work, spike investment (1-3 days) saves weeks.
**Ignoring critical path:** Unmanaged dependency slips cascade unpredictably.
**Treating all milestones equally:** Early = risk reduction. Late = polish and readiness.
**No kill criteria:** Without them, sunk-cost bias drives continued investment in failing bets.
