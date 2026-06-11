---
name: ypo-ai-prompts
description: An organized YPO AI prompt library — 6,500 prompts cross-filed into 1,060 category files covering every business function. Use when someone asks for prompt ideas, AI prompt templates, prompt inspiration, category-specific prompts, "find me a prompt for X", or "what's in the YPO library". Trigger for "YPO prompts", "ypo-ai-prompts", "AI prompt library", "prompt vault", "prompt for [function]" (marketing, sales, finance, operations, HR, product, strategy, leadership, etc.), "prompt template", "prompt idea", or any request to surface AI prompt examples for a specific business goal.
---

# YPO AI Prompts Skill

## Source Library

The prompts are bundled with this skill at `references/ypo-ai-prompts`.

Key files:

- `output/category-index.md` — readable list of all categories with prompt counts.
- `output/category-index.csv` — spreadsheet-friendly category index.
- `output/categories/*.md` — one Markdown file per category, containing the actual prompts.

Total: 6,500 YPO AI prompts cross-filed into 1,060 category files. A single prompt can appear in multiple category files because most prompts have multiple tags — like cross-listing a video in multiple playlists.

## Workflow

1. **Clarify the business goal.** If it isn't already clear, ask one focused question to nail down: audience, department, channel, job to be done, desired output format. Skip this if context is already clear.
2. **Search the library before drafting from scratch.** This library is the first stop, not the last resort.
3. **Use the helper script for targeted search** (run from the skill's root folder; it auto-locates the bundled library relative to itself):

```bash
python3 scripts/search_ypo_prompts.py --query "customer retention" --limit 8
```

Useful options:

```bash
# Discover categories by keyword
python3 scripts/search_ypo_prompts.py --list-categories marketing

# Search inside a specific category
python3 scripts/search_ypo_prompts.py --category marketing --query "campaign planning" --limit 10

# Browse a category's top prompts
python3 scripts/search_ypo_prompts.py --category sales --limit 12
```

If the script can't run, fall back to grep/ripgrep over `references/ypo-ai-prompts/output/categories/*.md`.

4. **If a result needs deeper inspection,** open the category file the script points to.
5. **Synthesize.** Pull the strongest prompt ideas for the user's use case. Don't dump raw text unless they ask for the exact original prompts.

## Output Rules

Default output:

- Lead with the strongest prompt ideas — not a recap of the search.
- Rewrite prompts so they fit the user's stated business context.
- Preserve useful structure from the source prompts; improve clarity and specificity.
- Surface the source category so the user can trace the idea.
- Label any new prompt inspired by the library as "adapted" or "new" — never imply it's a verbatim YPO prompt.
- Tie prompts to OKRs / metrics where possible.

## Search Guidance

Prefer targeted searches over reading huge files directly:

- For a known category, use `--category`.
- For a fuzzy topic, use `--query` across the whole library.
- For category discovery, use `--list-categories`.
- Avoid loading every category file into context. Use the script or `rg` to find a small set of relevant files first.

## Quality Check

Before finalizing, verify:

- Prompt ideas match the user's stated goal.
- Prompts are paste-ready into ChatGPT, Claude, or Gemini.
- Variables use clear bracket syntax: `[audience]`, `[product]`, `[campaign]`, `[KPI]`.
- Output avoids unnecessary jargon unless the user asks for implementation detail.
- Strong prompts are listed first; mediocre ones are pruned, not buffered.
