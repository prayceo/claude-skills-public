---
name: small-ai-prompts
description: An organized library of 6,500 AI prompts across every business function — desktop-friendly, packed into ~120 files. Use when someone asks for prompt ideas, AI prompt templates, prompt inspiration, or category-specific prompts ("find me a prompt for X", "what's in the prompt library"). Trigger for "AI prompt library", "prompt vault", "prompt for [function]" (marketing, sales, finance, operations, HR, product, strategy, leadership, etc.), "prompt template", "prompt idea", or any request to surface AI prompt examples for a specific business goal.
---

# Small AI Prompts Skill

A compact, desktop-friendly library of 6,500 AI prompts spanning every major business function.

## Source Library

The prompts are bundled with this skill at `references/ypo-ai-prompts`.

Key files:

- `output/category-index.md` — readable list of all categories with prompt counts.
- `output/category-index.csv` — spreadsheet-friendly category index.
- `output/categories/prompts-NNN.md` — packed prompt files. Each file holds several whole categories; its header lists which categories are inside.

Total: 6,500 unique prompts. Each prompt is stored once but keeps its full `Categories:` tag line — so a search for any category (e.g. "sales") still surfaces every prompt tagged with it, regardless of which file it lives in. Think of it like a library where each book sits on one shelf but the catalog finds it under every subject it covers. (This build packs the prompts into ~120 files to stay within typical app file and size limits; content is identical to the full library.)

## Workflow

1. **Clarify the business goal.** If it isn't already clear, ask one focused question to nail down: audience, department, channel, job to be done, desired output format. Skip this if context is already clear.
2. **Search the library before drafting from scratch.** This library is the first stop, not the last resort.
3. **Use the helper script for targeted search** (run from the skill's root folder; it auto-locates the bundled library relative to itself):

```bash
python3 scripts/search_ypo_prompts.py --query "customer retention" --limit 8
python3 scripts/search_ypo_prompts.py --category marketing --query "campaign planning" --limit 10
python3 scripts/search_ypo_prompts.py --list-categories marketing
```

If the script can't run, fall back to grep/ripgrep over `references/ypo-ai-prompts/output/categories/*.md` for the topic or a `Categories:` tag.

4. **If a result needs deeper inspection,** open the prompt file the script points to.
5. **Synthesize.** Pull the strongest prompt ideas for the user's use case. Don't dump raw text unless they ask for the exact original prompts.

## Output Rules

Default output:

- Lead with the strongest prompt ideas — not a recap of the search.
- Rewrite prompts so they fit the user's stated business context.
- Preserve useful structure from the source prompts; improve clarity and specificity.
- Surface the source category so the user can trace the idea.
- Label any new prompt inspired by the library as "adapted" or "new" — never imply it's a verbatim source prompt.
- Tie prompts to OKRs / metrics where possible.

## Search Guidance

Prefer targeted searches over reading huge files directly. Use `--category` for a known area, `--query` for a fuzzy topic, `--list-categories` for discovery. Avoid loading every prompt file into context — find a small relevant set first.

## Quality Check

Before finalizing, verify:

- Prompt ideas match the user's stated goal.
- Prompts are paste-ready into ChatGPT, Claude, or Gemini.
- Variables use clear bracket syntax: `[audience]`, `[product]`, `[campaign]`, `[KPI]`.
- Strong prompts are listed first; mediocre ones are pruned, not buffered.
