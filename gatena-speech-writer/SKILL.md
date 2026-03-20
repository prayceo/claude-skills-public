---
name: gatena-speech-writer
description: >
  The Gatena Speech Writer — a comprehensive speech-writing skill created by Steve Gatena for crafting
  powerful, memorable speeches using proven rhetorical devices, structural frameworks, and literary
  techniques. Use this skill whenever the user asks to write, draft, edit, improve, or review a speech,
  keynote, sermon, toast, eulogy, commencement address, TED-style talk, investor pitch narrative,
  motivational talk, acceptance speech, or any form of public address. Also trigger when the user asks
  about speech structure, rhetorical devices, how to open/close a speech, speech hooks, persuasion
  techniques, or how to make a speech more memorable, powerful, or emotional. Trigger for "write me a
  speech", "help me with my talk", "make this more persuasive", "add rhetorical devices", "punch up this
  speech", "speech outline", "keynote structure", "sermon outline", "toast for a wedding", "eulogy",
  "Gatena speech", or any variation. Even if the user just says "speech", "talk", "address", or
  "remarks" — use this skill.
---

# Gatena Speech Writer

**Created by Steve Gatena**

## Overview

This skill enables Claude to write, structure, and enhance speeches using the full arsenal of classical
and modern rhetorical technique. It covers 8 structural frameworks, 40+ rhetorical/literary devices,
10 opening hooks, 12 closing techniques, vocal delivery systems, audience psychology, persuasion
architecture, impromptu speaking, argument design, and storytelling frameworks — synthesized from
research across classical rhetoric, modern speechwriting coaches, TED methodology, crowd theory,
and political oratory.

## Quick-Start Decision Tree

Before writing, determine the speech type and load the right reference:

| If the user needs...                        | Read this reference first                        |
|---------------------------------------------|--------------------------------------------------|
| Overall speech structure / framework        | `references/structures.md`                       |
| Specific rhetorical or literary devices     | `references/devices.md`                          |
| Opening hooks or closing techniques         | `references/openings-closings.md`                |
| Delivery, voice, audience psychology        | `references/delivery-performance.md`             |
| Full speech from scratch                    | Read ALL FOUR references, then draft             |

## Core Workflow

### Step 1: Determine Speech Parameters (Performance Design)

Before writing, use the **10-Question Executive Performance Design** framework from `references/delivery-performance.md`. At minimum, clarify these critical inputs (ask the user if not provided):

1. **Goal** — What is this performance trying to accomplish? (Not "what is the topic" — what is the GOAL?)
2. **Audience** — Who are they? What do they care about? What do they NEED to hear?
3. **Context** — Where/when is this delivered? (Conference, boardroom, church, wedding, graduation, podcast)
4. **Duration** — How long? (~150 words per minute of spoken delivery)
5. **Tone** — Formal, conversational, urgent, reflective, celebratory, prophetic?
6. **Core Message** — What is the ONE idea the audience must remember? (If you can't say it in 1-2 sentences, it's not clear enough.)
7. **Emotional Effect** — What should the audience FEEL? (Anger, hope, urgency, relief, pride, fear?)
8. **Call to Action** — What should the audience DO after hearing this?
9. **Three-Word Brand** — What three words should the audience use to describe this experience?
10. **Change** — A speaker's job is to CHANGE the audience. No performance should leave them unchanged. What changes?

**The Critical Reframe:** Don't think "What's the next point I have to make?" Think "What's the next question I want the audience asking themselves?" Great presentations are mysteries that slowly unfold.

### Step 2: Select Structure

Choose a structural framework from `references/structures.md` based on purpose:

| Purpose            | Recommended Structure                          |
|--------------------|------------------------------------------------|
| Persuade to act    | Monroe's Motivated Sequence                    |
| Inspire/motivate   | Duarte Sparkline (Status Quo ↔ New Bliss)      |
| Teach/explain      | TED 4-Step (Hook → Promise → Body → Close)     |
| Tell a story       | Hero's Journey / SCR (Situation-Complication-Resolution) |
| Argue a position   | Classical 5-Part Argument                      |
| Celebrate/honor    | Past → Present → Future arc                    |
| Pitch an idea      | Problem → Agitate → Solve (PAS)                |
| Faith/sermon       | Text → Tension → Truth → Transformation        |

### Step 3: Layer in Devices

After drafting structure, enhance with rhetorical devices from `references/devices.md`.
Apply the **3-Layer Model**:

**Layer 1 — Macro Devices (Structure-level)**
These shape the entire speech arc:
- Aristotle's Appeals (Ethos → Logos → Pathos)
- The Rule of Three (3 main points)
- Contrast/Toggle (Status Quo vs. New Bliss)
- Narrative arc (Character → Conflict → Resolution)

**Layer 2 — Meso Devices (Paragraph/section-level)**
These shape individual sections:
- Anaphora (repeat at beginning of successive clauses)
- Epistrophe (repeat at end of successive clauses)
- Antithesis (contrasting ideas in parallel structure)
- Tricolon (three parallel phrases building in intensity)
- Hypophora (ask a question, then answer it)

**Layer 3 — Micro Devices (Sentence/word-level)**
These add texture and memorability:
- Alliteration, assonance, consonance (sound patterns)
- Metaphor and simile (imagery)
- Chiasmus / antimetabole (reversed structure)
- Anadiplosis (end-word becomes next start-word)
- Litotes, hyperbole (emphasis through under/overstatement)
- Asyndeton / polysyndeton (conjunction removal/addition)

### Step 4: Craft Opening and Closing

Read `references/openings-closings.md` for 10 proven hooks and 12 closing techniques.

**The Bookend Rule**: The opening and closing are the two most remembered parts of any speech.
Invest disproportionate effort here. The opening earns attention; the closing earns action.

**Close Selection Guidance**: Closes range from structural (Callback, Title) to emotional (Crescendo, Vision) to participatory (Sing-Song, Repetitive). Match close type to speech energy:
- **High-energy finish needed?** → Sing-Song, Repetitive, Emotional Crescendo
- **Reflective/authoritative finish?** → Third Party, Echo, Quotation
- **Action-oriented finish?** → Call to Action, Challenge
- **Elegant structural finish?** → Callback, Title, Movie

### Step 5: Polish and Stress-Test

Run these quality checks on every draft:

- [ ] **The Bar Test**: Would this sound natural said aloud to a friend at a bar? If not, simplify.
- [ ] **The Bumper Sticker Test**: Can you reduce the core message to ≤10 words?
- [ ] **The Rhythm Test**: Read it aloud. Do sentences vary in length? Is there cadence?
- [ ] **The "So What?" Test**: After every major point, would the audience say "so what?" If yes, add stakes.
- [ ] **The "Now What?" Test**: Does the audience know exactly what to do after this speech?
- [ ] **The Device Density Check**: Are devices enhancing or cluttering? (Max 2-3 devices per paragraph)
- [ ] **The Transition Check**: Does each section flow naturally to the next?
- [ ] **The Emotional Arc Check**: Does the speech have highs and lows, tension and release?

### Step 6: Add Delivery Marks & Voice Scoring

Read `references/delivery-performance.md` for the full voice and delivery system. At minimum:

1. **Embed delivery marks** into the script: [PAUSE], [LONG PAUSE], [SLOW], [BUILD], [QUIET], [LOUD], [SMILE]
2. **Score key passages** for Volume (1-10), Pace (1-10), and Pause length
3. **Apply "light and shade"**: No section should be delivered at a single volume/pace. Vary within each passage.
4. **Mark the "flex budget"**: Highlight 1-2 sections that can be cut if running overtime. Never cut the opening or closing.
5. **Mark eye contact sections**: Note where to sweep left, center, right of the audience.

## Key Principles

1. **One Idea, Not Ten.** The best speeches are about ONE transformative idea supported by 2-3 points. Not a data dump.
2. **Write for the Ear, Not the Eye.** Short sentences. Active voice. Concrete nouns. Strong verbs. No jargon without definition.
3. **Devices Are Seasoning, Not the Meal.** A speech stuffed with devices sounds like a poetry textbook. Use them surgically.
4. **Stories Beat Statistics.** But statistics inside stories are the most powerful combination.
5. **The Audience Is the Hero.** The speaker is the guide. Frame everything around what the audience gains.
6. **Vulnerability Before Victory.** Audiences connect with struggle before they believe in triumph.
7. **Silence Is a Device.** Pauses after key lines let meaning land. Write "[PAUSE]" into drafts where silence should live.
8. **End on Elevation.** The last 30 seconds should be the emotional and intellectual peak.
9. **The Speaker Is the Leader.** The audience WANTS to be led. Project authority, clarity, and control. Always give the impression of being in command — even when something goes wrong.
10. **Change the Audience.** A speech that leaves the audience unchanged has failed. Every performance must shift how they think, feel, or act.
11. **A Speech Is a Performance, Not a Conversation.** This doesn't mean inauthentic — it means deliberately crafted and delivered with skill, energy, and intention. Your public speaking voice is fundamentally different from your conversational voice.
12. **Never Apologize.** Don't apologize for nervousness, technical issues, or the topic. Fix problems with composure. The audience takes its cues from you.

## Speech Duration Guide

| Duration    | Word Count  | Main Points | Best For                          |
|-------------|-------------|-------------|-----------------------------------|
| 2 min       | ~300        | 1           | Toasts, introductions             |
| 5 min       | ~750        | 1-2         | Lightning talks, pitches          |
| 10 min      | ~1,500      | 2-3         | TEDx, short keynotes              |
| 18 min      | ~2,700      | 3           | TED talks                         |
| 30 min      | ~4,500      | 3-4         | Keynotes, sermons                 |
| 45-60 min   | ~6,750-9,000| 3-5         | Full keynotes, lectures            |

## Output Format

When delivering a speech draft, always include:

1. **Speech metadata** (purpose, audience, duration, core message, emotional effect, three-word brand)
2. **Structural framework used** (name it)
3. **The full speech text** with delivery marks embedded: [PAUSE], [LONG PAUSE], [SLOW], [BUILD], [QUIET], [LOUD], [SMILE] — and stage directions in [brackets] where relevant
4. **Device annotations** — After the speech, list key devices used and where (optional, include if the user is learning)
5. **Delivery notes** — Volume/Pace scoring for key sections, pause points, vocal dynamics, "light and shade" guidance
6. **Flex budget** — Mark 1-2 sections that can be cut if running overtime

## References

For deep-dive content, read the following files in `references/`:

- **`structures.md`** — 8 proven speech structural frameworks with step-by-step breakdowns
- **`devices.md`** — 40+ rhetorical and literary devices organized by category with definitions, examples, and usage guidance
- **`openings-closings.md`** — 10 opening hooks and 12 closing techniques with examples from famous speeches
- **`delivery-performance.md`** — Executive Performance Design (10-question framework), 12-step preparation workflow, vocal delivery system (Volume/Pace/Pause with "light and shade"), Confident Speaker checklist, audience psychology (speaker-as-leader from crowd theory), impromptu speaking framework, argument architecture (inductive vs. deductive), political speaking techniques (claptraps), and the Acknowledge & Overcome strategy
