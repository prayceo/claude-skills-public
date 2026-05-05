#!/usr/bin/env python3
"""Search Steve's organized YPO prompt library."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]


def first_existing_path(candidates: list[Path]) -> Path:
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


LIBRARY_ROOT = first_existing_path(
    [
        SKILL_ROOT / "references" / "ypo-ai-prompts",
        SKILL_ROOT.parent / "ypo-ai-prompts",
        SKILL_ROOT.parent.parent / "ypo-ai-prompts",
        Path("/Users/stevegatena/Desktop/SuperSteve/ypo-ai-prompts"),
    ]
)
INDEX_CSV = LIBRARY_ROOT / "output" / "category-index.csv"
CATEGORIES_DIR = LIBRARY_ROOT / "output" / "categories"

JSON_SOURCES = [
    LIBRARY_ROOT / "output" / "ypo_checkpoint_6500.json",
    LIBRARY_ROOT / "output" / "all-prompts.json",
    Path("/Users/stevegatena/Downloads/ypo_checkpoint_6500.json"),
]


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")


def tokenize(value: str) -> list[str]:
    return [token for token in re.findall(r"[a-z0-9]+", value.lower()) if len(token) > 1]


def load_index() -> list[dict[str, str]]:
    if not INDEX_CSV.exists():
        return []
    with INDEX_CSV.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def print_categories(filter_text: str | None) -> None:
    rows = load_index()
    if filter_text:
        terms = tokenize(filter_text)
        rows = [
            row
            for row in rows
            if all(term in row["category"].lower() for term in terms)
            or any(term in row["category"].lower() for term in terms)
        ]

    for row in rows[:200]:
        print(f"{row['prompt_count']:>5}  {row['category']}  {row['file']}")
    if len(rows) > 200:
        print(f"... {len(rows) - 200} more categories not shown")


def load_from_json() -> list[dict]:
    for source in JSON_SOURCES:
        if source.exists():
            with source.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
            for idx, item in enumerate(data, start=1):
                item.setdefault("_source_row", idx)
            return data
    return []


def parse_markdown_prompt(block: str, category: str, source_file: Path) -> dict | None:
    lines = block.splitlines()
    if not lines or not lines[0].startswith("## "):
        return None

    title = lines[0][3:].strip()
    meta: dict[str, str] = {}
    idx = 1

    while idx < len(lines) and not lines[idx].strip():
        idx += 1

    while idx < len(lines):
        line = lines[idx]
        if not line.strip():
            idx += 1
            break
        if not line.startswith("- ") or ": " not in line:
            break
        key, value = line[2:].split(": ", 1)
        meta[key.strip().lower()] = value.strip()
        idx += 1

    body_start = idx

    categories = [
        part.strip()
        for part in meta.get("categories", category).split(",")
        if part.strip()
    ]

    source_row = meta.get("source row", "")
    try:
        source_row_value: int | str = int(source_row)
    except ValueError:
        source_row_value = source_row

    return {
        "title": title,
        "url": meta.get("url", ""),
        "categories": categories,
        "body": "\n".join(lines[body_start:]).strip(),
        "bodyLen": meta.get("body length", ""),
        "_source_row": source_row_value,
        "_source_file": str(source_file),
    }


def load_from_markdown() -> list[dict]:
    records_by_url: dict[str, dict] = {}
    records_without_url: list[dict] = []

    for path in sorted(CATEGORIES_DIR.glob("*.md")):
        category = path.stem
        text = path.read_text(encoding="utf-8", errors="replace")
        blocks = re.split(r"\n---\n\n", text)
        for block in blocks[1:]:
            item = parse_markdown_prompt(block, category, path)
            if not item:
                continue
            url = item.get("url")
            if url:
                records_by_url.setdefault(url, item)
            else:
                records_without_url.append(item)

    return list(records_by_url.values()) + records_without_url


def load_prompts() -> list[dict]:
    data = load_from_json()
    if data:
        return data
    return load_from_markdown()


def category_matches(item: dict, category: str) -> bool:
    wanted = normalize(category)
    for item_category in item.get("categories") or []:
        normalized = normalize(str(item_category))
        if wanted == normalized or wanted in normalized:
            return True
    return False


def score_item(item: dict, query: str | None) -> int:
    if not query:
        return 1

    terms = tokenize(query)
    title = str(item.get("title", "")).lower()
    categories = " ".join(str(cat) for cat in item.get("categories") or []).lower()
    body = str(item.get("body", "")).lower()

    score = 0
    for term in terms:
        if term in title:
            score += 12
        if term in categories:
            score += 8
        if term in body:
            score += 2
    if query.lower() in title:
        score += 20
    if query.lower() in body:
        score += 6
    return score


def snippet(text: str, query: str | None, width: int = 420) -> str:
    clean = re.sub(r"\s+", " ", text).strip()
    if not clean:
        return ""
    if not query:
        return clean[:width] + ("..." if len(clean) > width else "")

    lower = clean.lower()
    positions = [lower.find(term) for term in tokenize(query) if lower.find(term) >= 0]
    start = max(min(positions) - 80, 0) if positions else 0
    excerpt = clean[start : start + width]
    if start > 0:
        excerpt = "..." + excerpt
    if start + width < len(clean):
        excerpt += "..."
    return excerpt


def print_results(items: list[dict], query: str | None, limit: int) -> None:
    for rank, item in enumerate(items[:limit], start=1):
        title = item.get("title") or "Untitled"
        categories = ", ".join(str(cat) for cat in item.get("categories") or [])
        body = item.get("body") or ""
        print(f"## {rank}. {title}")
        if item.get("url"):
            print(f"URL: {item['url']}")
        if categories:
            print(f"Categories: {categories}")
        if item.get("_source_row"):
            print(f"Source row: {item['_source_row']}")
        preview = snippet(str(body), query)
        if preview:
            print(f"Snippet: {preview}")
        print()


def main() -> int:
    parser = argparse.ArgumentParser(description="Search Steve's YPO prompt library.")
    parser.add_argument("--query", help="Keyword or phrase to search for.")
    parser.add_argument("--category", help="Limit results to a category.")
    parser.add_argument("--limit", type=int, default=10, help="Maximum results to show.")
    parser.add_argument(
        "--list-categories",
        nargs="?",
        const="",
        metavar="FILTER",
        help="List categories, optionally filtered by a word.",
    )
    args = parser.parse_args()

    if args.list_categories is not None:
        print_categories(args.list_categories or None)
        return 0

    prompts = load_prompts()
    if args.category:
        prompts = [item for item in prompts if category_matches(item, args.category)]

    scored = [
        (score_item(item, args.query), item)
        for item in prompts
        if not args.query or score_item(item, args.query) > 0
    ]
    scored.sort(key=lambda pair: (-pair[0], str(pair[1].get("title", ""))))
    results = [item for _, item in scored]

    if not results:
        print("No matching prompts found.")
        return 1

    print_results(results, args.query, args.limit)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
