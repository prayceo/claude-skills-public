---
name: ypo-ai-prompts
description: Steve's organized YPO AI prompt library — 6,500 prompts cross-filed into 1,060 category files covering every business function. Use when Steve asks for prompt ideas, AI prompt templates, prompt inspiration, category-specific prompts, "find me a prompt for X", "what's in my YPO library", or wants to mine the YPO collection saved in SuperSteve. Trigger for "YPO prompts", "ypo-ai-prompts", "AI prompt library", "prompt vault", "prompt for [function]" (marketing, sales, finance, operations, HR, product, strategy, leadership, etc.), "prompt template", "prompt idea", or any request to surface AI prompt examples for a specific business goal.
---

# YPO AI Prompts Skill

## Source Library

The library lives at:

`/Users/stevegatena/Desktop/SuperSteve/ypo-ai-prompts`

If packaged for portability, a bundled copy may also be at:

`references/ypo-ai-prompts`

Key files:

- `output/category-index.md` — readable list of all categories with prompt counts.
- `output/category-index.csv` — spreadsheet-friendly category index.
- `output/categories/*.md` — one Markdown file per category, containing the actual prompts.

Total: 6,500 YPO AI prompts cross-filed into 1,060 category files. A single prompt can appear in multiple category files because most prompts have multiple tags — like cross-listing a video in multiple playlists.

## Workflow

1. **Clarify the business goal.** If Steve hasn't already, ask one focused question to nail down: audience, department, channel, job to be done, desired output format. Skip this if context is already clear.
2. **Search the library before drafting from scratch.** This library is the first stop, not the last resort.
3. **Use the helper script for targeted search:**

```bash
python3 /Users/stevegatena/.claude/skills/ypo-ai-prompts/scripts/search_ypo_prompts.py --query "customer retention" --limit 8
```

Useful options:

```bash
# Discover categories by keyword
python3 /Users/stevegatena/.claude/skills/ypo-ai-prompts/scripts/search_ypo_prompts.py --list-categories marketing

# Search inside a specific category
python3 /Users/stevegatena/.claude/skills/ypo-ai-prompts/scripts/search_ypo_prompts.py --category marketing --query "campaign planning" --limit 10

# Browse a category's top prompts
python3 /Users/stevegatena/.claude/skills/ypo-ai-prompts/scripts/search_ypo_prompts.py --category sales --limit 12
```

4. **If a result needs deeper inspection,** open the category file the script points to.
5. **Synthesize.** Pull the strongest prompt ideas for Steve's use case. Don't dump raw text unless he asks for the exact original prompts.

## Output Rules

Steve runs Pray.com, follows BLUF, is an ENTJ / high-D / Enneagram 8. Default output:

- Lead with the strongest prompt ideas — not a recap of the search.
- Rewrite prompts so they fit Steve's stated business context.
- Preserve useful structure from the source prompts; improve clarity and specificity.
- Surface the source category so Steve can trace the idea.
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

- Prompt ideas match Steve's stated goal.
- Prompts are paste-ready into ChatGPT, Claude, or Gemini.
- Variables use clear bracket syntax: `[audience]`, `[product]`, `[campaign]`, `[KPI]`.
- Output avoids unnecessary jargon unless Steve asks for implementation detail.
- Strong prompts are listed first; mediocre ones are pruned, not buffered.
