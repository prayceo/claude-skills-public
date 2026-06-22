---
name: bible-study-webpage
description: >
  Build a finished, premium theological research webpage on any Bible topic
  (gossip, envy, anger, pride, forgiveness, anxiety, lust, greed, fear, etc.)
  and/or a quote provided. Outputs a self-contained .html file using the
  American Christian brand design (black + gold, Satoshi/Bodoni fonts) with
  an 8-section format and a working one-click "Download as PDF" button.
  TRIGGER for: "make a Bible study page for [topic]", "build a webpage on
  [topic]", "bible-study-webpage", "create a research page for [topic]",
  "American Christian page for [topic]", or any request to create a
  theological research page for a faith/Christian topic.
---

# Bible Study Webpage

## What this skill does

Creates a premium, fully-written, brand-matched HTML research page on any
faith/Bible topic. Uses the 8-section "American Christian" format.
The template file lives at:
`~/american-christian-topics/gossip-is-a-sin.html`

Finished pages are saved to:
`~/american-christian-topics/[topic-slug].html`

---

## Step 1 — Gather inputs

1. **Topic** — e.g. "envy", "pride", "anger", "forgiveness", "anxiety"
   - If not provided, ask for the topic.
2. **Quote (optional)** — becomes a pull-quote in the Three Points section.
3. **Topic slug** — kebab-case filename:
   - "Greed" → `greed-is-a-sin.html`
   - "Dealing with Anxiety" → `dealing-with-anxiety.html`
   - "The Sin of Pride" → `why-pride-comes-before-the-fall.html`

---

## Step 2 — Research the topic

Gather content for all 8 sections:

### A. Headline
Frame as a question: "Why Does God Say That [Topic] Is a Sin?"

### B. One-sentence thesis (≤ 40 words)
Arresting summary of the unified theological answer. Non-obvious.
Model: *"Eight centuries of theological wisdom converge on one truth: gossip
is not a harmless habit — it is an assault on love, an expression of pride,
and an act of violence against image-bearers of God."*

### C. Hook (2–3 sentences)
A relatable opening line everyone recognizes, then pivot: "But why?"

### D. Three Points — "Three Reasons God Forbids [Topic]"
Each point requires:
- A punchy heading (e.g. "Greed Is Idolatry — Not Just Irresponsibility")
- 2–3 sentences of theological explanation
- One anchor Bible verse (full text + reference)
- 2–3 theologian references with brief paraphrases
- One bold takeaway: "God says [topic] is a sin because…"
- One pull-quote with author + book title

The Three Points must be **surprising and non-obvious** — give the reader
a fresh theological lens, not just "the Bible says so."

### E. Deeper Dive — 6–8 theologians
Per entry: author, book, 2–3 sentence summary, 2–3 direct quotes with
labels, 3–5 scripture references.

Preferred pool: Thomas Aquinas, Augustine, C.S. Lewis, Dietrich Bonhoeffer,
John Wesley, Richard Baxter, Jerry Bridges, A.W. Tozer, Tim Keller,
John Piper, Matthew Mitchell, N.T. Wright, J.I. Packer, Spurgeon,
Jonathan Edwards.

### F. Key Scripture Grid — 10–12 verses
Each: reference + one-line summary.

### G. Practical Application — 7 steps
What to do instead. Each step: bold heading, 2–3 sentences, one verse.

### H. Final Challenge — 3 gut-check questions

---

## Step 3 — Build the HTML file

### Method
1. Read `~/american-christian-topics/gossip-is-a-sin.html`
   as the base template.
2. Write a Python script that copies that file and replaces only the text
   inside the `<!-- CONTENT:xxx -->` … `<!-- /CONTENT:xxx -->` blocks.
3. Use this regex pattern (handles comments with extra text):
   ```python
   pattern = rf'(<!-- CONTENT:{re.escape(key)}.*?-->).*?(<!-- /CONTENT:{re.escape(key)} -->)'
   ```
4. Also replace `<title>`, meta description, og:title, og:description,
   and the `PDF_FILENAME` JS variable.
5. Save to `~/american-christian-topics/[slug].html`

### CONTENT blocks to replace

| Block | What to replace |
|-------|----------------|
| `CONTENT:hero` | eyebrow, h1, thesis, buttons |
| `CONTENT:hook` | relatable opening + "But why?" pivot |
| `CONTENT:points-head` | h2 + subline |
| `CONTENT:point-1` | Point One (full structure) |
| `CONTENT:point-2` | Point Two (full structure) |
| `CONTENT:point-3` | Point Three (full structure) |
| `CONTENT:deeper-dive` | All `<details>` accordion entries |
| `CONTENT:scripture-grid` | All `.scard` verse cards |
| `CONTENT:steps` | All `.step` practical entries |
| `CONTENT:challenge` | eyebrow + 3 gut-check questions |
| `CONTENT:footer` | source credits + brand mark |
| `CONTENT:pdf-filename` | JS `PDF_FILENAME` variable |

### HTML components reference

**Verse block:**
```html
<div class="verse">"Verse text here."<span class="ref">Book 1:2</span></div>
```

**Pull-quote block:**
```html
<div class="pull"><blockquote>"Quote text."<cite>— Author, <em>Book Title</em></cite></blockquote></div>
```

**Theologian accordion entry:**
```html
<details>
  <summary><span><span class="who">Name</span><span class="src">Book Title</span></span><span class="plus">+</span></summary>
  <div class="dd-body">
    <p>Summary paragraph.</p>
    <div class="dd-quote"><span class="lbl">Label</span>"Direct quote."</div>
    <div class="dd-quote"><span class="lbl">Label</span>"Direct quote."</div>
    <p class="refs"><b>References:</b> Verse · Verse · Verse</p>
  </div>
</details>
```

**Scripture card:**
```html
<div class="scard"><div class="ref">Book 1:2</div><p>One-line summary</p></div>
```

**Practical step:**
```html
<div class="step"><div class="n">1</div><div>
  <h3>Step Title</h3>
  <p>2–3 sentences of guidance.</p>
  <div class="verse">"Verse text."<span class="ref">Book 1:2</span></div>
</div></div>
```

---

## Step 4 — Design rules (never change)

The visual design lives in the `<style>` block of the template. Do not
modify it. Brand tokens:

- Background: `#0a0b0c` (near-black)
- Gold accent: `#e3af4a`
- Body text: `#d7d9dd`
- Headlines: `#f4f1ea` (warm off-white)
- Fonts: Satoshi (body), Bodoni Moda (serif headlines)

---

## Step 5 — Deliver

1. Run the Python build script to write the file.
2. Open in browser: `open ~/american-christian-topics/[slug].html`
3. Report:
   - Filename and location
   - One-line summary of the Three Points
   - Confirm the "Download as PDF" button is live
   - Invite feedback before building the next topic

---

## Quality bar

- **Depth**: real theologian quotes, not paraphrases
- **Scripture**: cite chapter and verse; use actual NIV or ESV text
- **Tone**: reverent, serious, intellectually honest — not preachy or listicle
- **Length**: each Point ≥ 150 words; each theologian entry ≥ 2 direct quotes
- **Originality**: Three Points must give a fresh theological lens

---

## Example invocations

- `Make a Bible study page for pride`
- `Build a webpage on forgiveness`
- `Create a research page for anxiety`
- `Bible study webpage — anger, with this quote: "In your anger do not sin"`
- `Make an American Christian page for lust`
