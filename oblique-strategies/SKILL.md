---
name: oblique-strategies
description: Break mental blockers using Oblique Strategies (Brian Eno/Peter Schmidt). Use this skill whenever the user says they're stuck, blocked, in a rut, can't decide, overthinking, going in circles, need a fresh perspective, or asks for a creative prompt / random strategy / oblique strategy / lateral thinking. Also trigger when the user says 'draw a card', 'give me a strategy', 'help me think differently', 'I'm blocked on...', 'unstick me', 'shake things up', or any variation of seeking creative unblocking. Even if the user just says 'oblique', 'Eno', 'OS Skill', or 'OS' (short for Oblique Strategies), use this skill.
---

# Oblique Strategies — Mental Blocker Breaker

Based on Oblique Strategies © 1975, 1978, 1979 Brian Eno / Peter Schmidt. 129 strategies extracted and recontextualized for business, leadership, and strategic decision-making.

## How This Works

The original Oblique Strategies were a deck of cards designed to break creative deadlocks in the recording studio. Each card carries a cryptic prompt that forces lateral thinking. This skill adapts those prompts for business and leadership contexts — turning art-world provocations into CEO-grade pattern interrupts.

## When to Deploy

Oblique Strategies are most effective when:
- You've been grinding on the same problem with diminishing returns
- The team is stuck in group-think or analysis paralysis
- A decision keeps getting deferred because no option feels "right"
- You need to challenge assumptions but don't know which ones
- You're pattern-matching to old playbooks that may not apply
- Energy is low and you need a creative jolt

## How to Use

### Mode 1: Single Card Draw
When the user asks for a card, strategy, or is stuck:

1. Read `references/strategies.json`
2. Select 1 strategy at random (use a random number or hash of the current timestamp)
3. Present the original Eno/Schmidt quote and the business reframe
4. Offer a 2-3 sentence provocation that connects the strategy to the user's specific context (if known)
5. Ask: "Want another card, or want to dig into this one?"

### Mode 2: Triple Draw (Spread)
When the user wants broader inspiration or says "give me a few" / "spread" / "draw three":

1. Select 3 strategies at random — ideally from different tag categories
2. Present all three with originals and business reframes
3. Briefly note the tension or complementarity between the three (e.g., "Card 1 says slow down, Card 3 says sprint — which instinct is right for THIS moment?")

### Mode 3: Targeted Draw
When the user describes a specific blocker (e.g., "I can't close this deal" / "team is demoralized" / "we keep debating and not shipping"):

1. Read the strategies and identify 2-3 that are most relevant based on tags and business reframes
2. Present them as a curated prescription, not a random draw
3. For each, explain WHY this strategy applies to their specific situation
4. Suggest one concrete action they could take in the next 24 hours based on each strategy

### Mode 4: Full Deck Review
When the user asks to see all strategies, browse the deck, or wants a specific category:

1. Group strategies by their tags
2. Present them organized by theme with both original and business reframe
3. Allow filtering by tag (e.g., "show me all the courage-related ones")

## Presentation Format

When presenting a single strategy:

```
🃏 OBLIQUE STRATEGY #[ID]

"[Original Eno/Schmidt text]"

→ [Business reframe]

[Contextual provocation tied to the user's situation if known]
```

When presenting a spread:

```
🃏 CARD 1 — [Tag]
"[Original]"
→ [Business reframe]

🃏 CARD 2 — [Tag]  
"[Original]"
→ [Business reframe]

🃏 CARD 3 — [Tag]
"[Original]"
→ [Business reframe]

🔗 The tension: [Brief note on how these three interact]
```

## Key Principles

- **Don't over-explain.** The power of Oblique Strategies is in their ambiguity. Present the provocation and let the user sit with it. Resist the urge to interpret too literally.
- **Connect to context.** If you know what the user is working on, make the connection specific. "Turn it upside down" is generic. "Instead of asking 'how do we grow subscribers,' ask 'what's causing people to leave in the first 30 days?'" is actionable.
- **Embrace contradiction.** Some strategies will seem to contradict others. That's the point. The deck is a tool for lateral thinking, not a consistent philosophy.
- **One card can change everything.** Don't rush past a single strategy to serve more. If one lands, dig in.
- **Physical analogy matters.** Reference "drawing a card" — the physicality of the original deck is part of its power. Maintain that ritual feeling.

## Reference

All 129 strategies with IDs, original text, business reframes, and tags are in:
`references/strategies.json`

Read this file when the skill triggers to select and present strategies.
