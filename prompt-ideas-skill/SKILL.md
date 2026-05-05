---
name: prompt-ideas-skill
description: Use Steve's organized YPO AI prompt library to find, adapt, and generate prompt ideas by category, role, function, campaign, workflow, or business goal. Use when Steve asks for prompt ideas, AI prompt templates, prompt inspiration, category-specific prompts, or wants to mine the YPO prompt collection saved in SuperSteve.
---

# Prompt Ideas Skill

## Source Library

Use the organized prompt library here:

`/Users/stevegatena/Desktop/SuperSteve/ypo-ai-prompts`

When this skill is packaged for SuperSteve or GitHub, it can also use a bundled copy here:

`references/ypo-ai-prompts`

Key files:

- `output/category-index.md` - readable list of categories and counts.
- `output/category-index.csv` - spreadsheet-friendly category index.
- `output/categories/` - one Markdown file per category, containing the actual prompts.

The library contains 6,500 YPO AI prompts cross-filed into 1,060 category files. A prompt can appear in multiple category files because most prompts have multiple tags.

## Workflow

1. Clarify the business goal if needed: audience, department, channel, job to be done, and desired output.
2. Search the library before drafting from scratch.
3. Use the helper script for targeted search:

```bash
python3 /Users/stevegatena/.codex/skills/prompt-ideas-skill/scripts/search_prompt_ideas.py --query "customer retention" --limit 8
```

Useful options:

```bash
python3 /Users/stevegatena/.codex/skills/prompt-ideas-skill/scripts/search_prompt_ideas.py --list-categories marketing
python3 /Users/stevegatena/.codex/skills/prompt-ideas-skill/scripts/search_prompt_ideas.py --category marketing --query "campaign planning" --limit 10
python3 /Users/stevegatena/.codex/skills/prompt-ideas-skill/scripts/search_prompt_ideas.py --category sales --limit 12
```

4. If a result needs deeper inspection, open the category file listed by the script.
5. Synthesize the best prompt ideas for Steve's use case. Do not simply dump raw prompt text unless Steve asks for the exact original prompts.

## Output Rules

Default output should be practical and executive-friendly:

- Start with the strongest prompt ideas, not a long explanation of the search.
- Rewrite prompts so they fit Steve's stated business context.
- Preserve useful structure from the source prompts, but improve clarity and specificity.
- Include source category or URL when it helps trace where the idea came from.
- If inventing a new prompt inspired by the library, label it as an adapted or new prompt rather than implying it is a verbatim YPO prompt.

## Search Guidance

Prefer targeted searches over reading huge files directly:

- For a known category, search that category file or use `--category`.
- For a fuzzy topic, use `--query` across the library.
- For category discovery, use `--list-categories`.
- Avoid loading every category file into context; use the script or `rg` to identify a small set of relevant files first.

## Quality Check

Before finalizing, verify:

- The prompt ideas match Steve's stated goal.
- The prompts are ready to paste into an AI tool.
- Variables are clear, using brackets like `[audience]`, `[product]`, or `[campaign]`.
- The output avoids unnecessary technical jargon unless Steve asks for implementation detail.
