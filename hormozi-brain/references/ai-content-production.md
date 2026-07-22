# AI-Powered Content & Ad Production Pipeline

**Source:** ACQ Marketing Masterclass (2026) — a live session presented by four Acquisition.com team members (Preston: paid + testing philosophy; Hunter: the ad machine; Julian: organic strategy; Maddex: the clip machine) — plus three companion documents: the *AI Ad Machine* build guide (Hunter Ray Barker, Video Editor/Paid Ads), the *AI Editing Tool List*, and the *Vibe Editing* onboarding guide (a productized, consumer-facing version of the same pipeline built on Claude Code).

Unlike the other reference files in this archive, this file is not strategy to translate — it is a concrete, buildable technical system for turning raw video into ads and organic clips at scale using AI coding agents. It answers a different question than the rest of the archive: not "what should we say or charge," but "how do we actually produce the volume of creative that More/Better/New and Kaleidoscope demand without a proportional increase in headcount."

## The Core System: "One Engine"

```
One source asset -> Organic tests it cheap -> Winners graduate to paid -> Scale what prints
```

"Volume is a system output, not a headcount output." This is the connective tissue between this file and the rest of the archive: `marketing-workshop.md`'s volume principle and Kaleidoscope process aren't achieved by hiring more editors — they're achieved by building the pipeline below.

## The Paid/Testing Layer (Preston + the Masterclass deck)

- **Separate testing from scaling.** Testing runs as ABO (Advantage+ creative testing, budget set at the ad-set level). Scaling runs as CBO (stack the winners, duplicate the proven post ID to preserve its social proof) once a winner is confirmed.
- **Test by angle, not by ad.** Each creative angle (e.g., AI-generated ads, Q&A-style, testimonials) gets its own ad set. Keep ad sets narrowly focused so budget concentrates instead of spreading thin across variants.
- **Optimize for the real downstream event, not the top-of-funnel action.** Their example: optimize for `invitee_meeting_scheduled` (a booked call), not the opt-in.
- **The efficiency metric they manage to: cost per callable MQL.** Read leading indicators against your own account average — not generic industry benchmarks.
- **Kill rule: 3x the target CPA and the ad is dead.** "Most ads die. That's the point." Winners that hold under target earn more budget; there is no sentimentality about a creative that isn't working.
- **The Golden BBs (their own stated principles, verbatim in spirit):**
  1. Creative is the lever.
  2. Angles open new pockets (a new creative angle can unlock an audience segment the account wasn't reaching at all, not just improve performance on the existing one).
  3. Kill fast, scale slow (confirm a winner is real before duplicating budget into it).
  4. Trust blended numbers, not platform numbers (a single platform's own attribution will oversell its own performance — reconcile against blended reality).

## The Ad Machine Build Process (Hunter Barker's SOP)

**Headline result:** moved from manually editing 2,000+ ads in 2025 to producing the same volume in a month using this system. The leverage is not "AI edits one video well" — it's a documented, repeatable folder structure and SOP that an AI coding agent can run against reliably every time, without needing the same requirements re-explained on every project.

**The tool stack it runs on** (all four categories are swappable — "stay tool-agnostic, think in workflows, not tools"):

| Function | Tools |
|---|---|
| IDE / agent environment | Cursor, Windsurf, Claude desktop app, Codex app |
| AI coding agent | Codex, Claude Code |
| Video editor | Premiere Pro, DaVinci Resolve |
| Editor control bridge (MCP) | `premiere-pro-mcp` (Premiere Pro), `davinci-resolve-mcp` (DaVinci Resolve) |
| Transcription + word timing | AssemblyAI (cloud), NVIDIA Parakeet/Parakeet MLX (free, local, Apple Silicon) |
| Silence removal / dead-air cleanup | Silero VAD |
| Captions + on-screen text | Remotion (code-based, React), HyperFrames (HTML/CSS/JS, AI-promptable) |
| VFX + motion graphics | HyperFrames, Remotion |
| Reframing to vertical (face-aware) | MediaPipe (tracking data) applied through the MCP bridge |
| Rendering | FFmpeg, Remotion, HyperFrames |
| Automated QC | Gemini API (watches/listens to finished clips, returns timestamped notes on problems), FFmpeg (technical checks, quick review exports) |
| Rough-cut assembly / generative media | OpenMontage, Open-Generative-AI, Generative Media Skills |
| Helper utilities | FFmpeg (general media probing/conversion), yt-dlp (pull source/reference video) |

**The 7-step build process:**

1. **Plan the folder structure before touching a single clip.** This is the most important step — everything else compounds from it. Don't impose a structure; have the agent propose one, then refine it together until it matches how the team actually works. One main video directory, organized by content type (ads/, VSLs/, testimonials/, organic-content/, client-projects/, documentation/); inside each content type, a numbered project structure (`01_footage/`, `02_audio/`, `03_selects/`, `04_project-files/`, `05_exports/`, `06_scripts/`, `07_notes/`, `08_docs/`).
2. **Document every workflow as a living SOP** — one SOP per content type, stored in a `documentation/` directory (e.g., `ads-workflow-SOP.md`, `VSL-workflow-SOP.md`). Update it after every run with what worked and what to change next time. Skipping this step means re-explaining the same requirements to the agent forever.
3. **Connect the video editor to the agent through the MCP bridge.** Confirm the agent can see the active project, its sequences, and its bins before doing anything else.
4. **Mirror the folder structure inside the editor as numbered bins,** matching the folder names exactly, so the agent never has to guess where anything goes.
5. **Work one step at a time — never try to "one-shot" an entire project in a single prompt.** The 14-step sequence: create project folder -> create subfolder structure -> document the structure -> open the editor -> connect the MCP bridge -> create matching bins -> import media -> organize media -> create selects -> assemble the first timeline -> review the edit -> revise the SOP -> export the deliverable -> document what worked and what changed. Especially on the first run, move through this in a clear sequence with review at each step — trying to compress it loses the system and returns you to a manual edit you can't repeat.
6. **Review the workflow with the team after a run or two, hunting for bottlenecks.** Ask: which steps took too long? Which needed too much manual correction? What could be standardized before editing even begins? Which production choices (on set, before the footage even exists) would make the AI edit easier? Their own example: once they standardized keeping the speaker's head centered in the same position across every camera angle, that single production change eliminated an entire follow-focus and reframing step in post — the edit got faster because production got cleaner, not because the AI got smarter.
7. **Update the documentation after every project.** This is what makes the system self-evolving instead of a one-time script — every project that ends with an updated SOP makes the next one faster, cleaner, and more automated.

**Final principle:** "AI unlocks unprecedented speed in media production — but that speed comes from structure, not from doing everything at once." The biggest mistake is skipping the planning phase and asking AI to do it all in one shot.

## The Organic / Clip Machine Layer (Julian + Maddex)

- **Case study — MoreMozi channel:** started 6 months prior to the masterclass, ~280 mid-form-plus-shorts pieces produced per week, highest month achieved 2x the revenue of the main channel, largely automated via a mid-form clipper + scheduler + short-form clipper.
- **What's behind the organic machine:** more specific content (narrower, higher-intent topics beat generic ones — same principle as Content Bingo's audience specificity); live demonstration; capture vs. manufacture (build the pre-production process so real moments get captured rather than staged after the fact); the marketing flywheel connecting shorts to ads (an organic winner becomes the seed for a paid angle, closing the loop back to the One Engine model above).
- **"The clip machine": how one long-form video becomes a hundred ads and clips.** Same four tool categories as the ad machine (IDE, coding agent, video editor, MCP bridge) — this is the same underlying pipeline, pointed at organic/clip output instead of paid ad variants.

## Vibe Editing — A Working Tool, Not Just a Philosophy

Acquisition.com productized this exact internal pipeline into a public, non-technical setup guide called **Vibe Editing**, built explicitly on Claude Code, with its own public GitHub repo (`github.com/maddexritter-rgb/vibe-editing`).

- **Setup is genuinely about 15 minutes:** install the Claude Code app (paid Pro or Max plan), paste one pre-written prompt block into a new chat (it contains the GitHub link and full setup instructions — clone the repo, run a `doctor.py` environment check, install only what's missing), then answer plain-English questions about brand (logo, fonts, colors, music, how clips should open/end).
- **What it does once running, entirely through conversation** ("make clips from this," "mine highlights from this," "post and schedule these," "make the captions bigger"):
  - **Clips:** long video -> vertical (9:16) clips, captioned, face-tracked, music-mixed, run through a 6-point quality check before being called done.
  - **Highlights:** mines a long recording (e.g., a Q&A or podcast) into ranked horizontal "mid" videos built to grow subscribers, then titles and schedules them.
  - **Brand baked in:** it interviews the user for their brand once, so every clip looks like theirs, not a generic template.
  - **Self-QC:** six automated audit gates catch bad framing, audio, captions, and weak cuts — a clip that fails an audit doesn't ship.
- **No editing software, no timeline, no terminal required from the user** — the entire interaction is plain-English chat with Claude Code.

## Applying This to the company

This is the most directly buildable file in this entire archive — unlike the offer/sales/marketing frameworks, it needs almost no faith-context translation, because it's pure production tooling, agnostic to what the video actually contains. The company already has the raw material this pipeline is built for: sermons, devotionals, Bible readings, and worship music that could become hundreds of short-form clips and paid-ad variants without a proportional increase in editing headcount.

- **Fastest test:** stand up Vibe Editing directly against one piece of existing long-form the company content and see what it produces in an afternoon, before committing to a custom build.
- **If it proves out:** the 7-step SOP process above is a reasonable model for the company's own paid-ad and organic-clip production, on the same open tools or adapted to the company's existing editing stack.
- **Borrow the paid-testing discipline regardless of the tooling decision:** separate ABO-test from CBO-scale budgets, test creative angles in isolated ad sets, and set a hard 3x-kill rule against the company's own account average rather than a generic benchmark.
- **This is the concrete implementation of Layer 6 (Code leverage)** in the Hormozi Operating System diagram in `SKILL.md` — where Content and Code leverage meet: an AI agent doing the mechanical work of production so a small team can produce at an institutional scale.

## Numbers to Treat as Directional

This document is a single team's account of their own results, not an audited or third-party-verified case study.

- The "2,000+ ads manually -> same volume in a month" claim is Hunter Barker's own reported before/after — a strong directional signal, not a guaranteed multiplier for any other team or content type.
- The MQL summary and results-by-industry tables shown in the live deck reflect one portfolio's actual account data at one point in time (June figures, ROAS ranging from 7.2x for Law down to 0.3x for Food/Beverage) — useful as an illustration of how much variance exists by vertical, not as a benchmark to import directly.
