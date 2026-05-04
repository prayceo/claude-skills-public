---
name: linkedin-profile-analyzer
description: Analyze any LinkedIn profile end-to-end — pull the top 50 most-liked posts, download every photo, rewrite each post as a viral original using Gatena Cookbook + Welsh Brain frameworks, and generate an AB-test recommendation memo. Trigger when the user provides a LinkedIn profile URL (linkedin.com/in/...) and asks to analyze it, study it, rank posts, find their best content, get their photos, rewrite their content, learn from their feed, or any variation. Also trigger for "study this LinkedIn profile", "analyze [URL]", "what's working on this profile", "give me the top X posts for [profile]", "rewrite their best posts", "competitor LinkedIn audit", "personal brand teardown", or "build me a LinkedIn engine from this profile".
---

# LinkedIn Profile Analyzer

**Purpose:** End-to-end LinkedIn profile analysis agent. Give it a profile URL → get back a ranked top-50, image archive, content rewrites, and AB-test recommendations.

## When to Use This Skill

Trigger whenever the user provides any LinkedIn profile URL (typically `https://www.linkedin.com/in/[handle]/` or its `/recent-activity/all/` variant) AND wants any of:

- The top N most-liked posts from that profile
- A photo archive of those posts
- Rewrites of those posts using behavioral science + content frameworks
- AB-test recommendations / personal brand teardown
- Competitive intel on a creator, executive, or peer

Default scope per run: top 50 + photos + rewrites + AB-test memo. Adjust if the user requests a lighter version.

## Required Inputs

1. **Profile URL** — must be `linkedin.com/in/[handle]/...`
2. **Confirmation that Chrome is connected** (browser automation required)

If either is missing, ask the user with `AskUserQuestion`.

## Required Tools

- `mcp__Claude_in_Chrome__*` (browser automation — must be connected)
- `Write`, `Read`, `Edit`
- `mcp__workspace__bash` (optional, for file operations)
- `TaskCreate`, `TaskUpdate` (progress tracking)

## Companion Skills (read these inline when generating rewrites)

- `gatena-cookbook` — 190 behavioral science principles
- `welsh-brain` — Welsh Creator MBA frameworks (UVP, 5 Levels of Awareness, 10 Content Frameworks)

## Output Deliverables (saved to outputs folder)

For a profile at `linkedin.com/in/[handle]`, produce:

1. `[handle]_top50_linkedin_posts.md` — ranked list with snippets + framework analysis
2. `[handle]_top50_images_manifest.csv` — image filename → rank → like count → URL
3. `[handle]_top50_images.zip` — bundle of all 50 images (triggered as browser download)
4. `[handle]_top50_rewrites.md` — 50 fresh posts annotated with Welsh + Cookbook stacks
5. `[handle]_ab_test_recommendations.md` — strategic memo: which 3 archetypes to test first, posting cadence, KPIs to watch

---

# WORKFLOW (8 steps)

## Step 1 — Validate input + setup

```
1. Confirm URL matches /linkedin\.com\/in\/([^\/]+)/. Extract handle.
2. Normalize to: https://www.linkedin.com/in/[handle]/recent-activity/all/
3. Confirm Chrome is connected (call mcp__Claude_in_Chrome__list_connected_browsers).
   If not connected, ask the user to connect it and retry.
4. Create output folder if needed.
5. Initialize TaskList with the 8 workflow steps so progress is visible.
```

## Step 2 — Navigate + load activity feed

Open the normalized URL in a new tab. The activity feed lazy-loads via a "Show more results" button (NOT scroll-based — scrolling alone won't trigger more posts).

The button click loop has a 45-second JS execution timeout per call. Run it in batches of 8-10 clicks at a time, with ~3-second waits between clicks.

```js
// Run this in a loop, batched per call (don't exceed ~25-30s per JS call):
(async () => {
  let prev = document.querySelectorAll('div.feed-shared-update-v2').length;
  let stable = 0;
  for (let i = 0; i < 8; i++) {
    const btns = Array.from(document.querySelectorAll('button')).filter(b => {
      const t = (b.innerText || '').trim().toLowerCase();
      return (t === 'show more results' || t === 'show more') && b.offsetParent !== null;
    });
    if (btns.length) { btns[0].scrollIntoView({block: 'center'}); btns[0].click(); }
    else { window.scrollTo(0, document.body.scrollHeight); }
    await new Promise(r => setTimeout(r, 3000));
    const c = document.querySelectorAll('div.feed-shared-update-v2').length;
    if (c === prev) { stable++; if (stable >= 2) break; } else { stable = 0; prev = c; }
  }
  return JSON.stringify({count: prev, height: document.body.scrollHeight});
})()
```

**Stopping condition:** Continue running batches until the count is stable across 2 consecutive batches OR you've loaded ~600+ posts (LinkedIn caps activity feed pagination at ~25 months). Whichever comes first.

**Realistic ceiling:** ~500-700 posts for an active poster's last 25 months. Older posts are not paginated by LinkedIn.

## Step 3 — Extract post data

Once loading is done, extract each post's like count, full text, and image URL. The structure:

- Post container: `div.feed-shared-update-v2`
- Activity URN: `data-urn` attribute (format: `urn:li:activity:[id]`)
- Like count: button with `aria-label="You and N others"` → likes = N + 1
  - If aria says "N reactions" instead, likes = N
- Post text: `.update-components-text` element
- Image: `<img>` inside the post (filter out avatars, reaction icons, profile photos)

```js
(() => {
  const posts = document.querySelectorAll('div.feed-shared-update-v2');
  const out = [];
  posts.forEach((post, idx) => {
    const urn = post.getAttribute('data-urn');
    const reactBtn = post.querySelector('button[data-reaction-details], button[aria-label*="reaction" i], button[aria-label*="others" i]');
    let likes = null, reactAria = null;
    if (reactBtn) {
      reactAria = reactBtn.getAttribute('aria-label');
      const m = reactAria && reactAria.match(/([\d,]+)/);
      if (m) {
        likes = parseInt(m[1].replace(/,/g, ''));
        if (/you and/i.test(reactAria)) likes += 1;
      }
    }
    const descEl = post.querySelector('.update-components-text, [class*="update-components-text"]');
    let text = descEl ? (descEl.innerText || '').trim() : '';
    text = text.replace(/\s*…more\s*$/i, '').replace(/\s+/g, ' ').trim();

    // Image extraction (filter junk)
    const imgs = [];
    post.querySelectorAll('img').forEach(img => {
      const src = img.src || img.getAttribute('data-delayed-url') || img.getAttribute('data-ghost-url');
      if (!src) return;
      if (src.includes('avatar') || src.includes('reactions-icon') || src.includes('emoji')) return;
      if (src.includes('profile-displayphoto') || src.includes('profile-displaybackgroundimage')) return;
      if (src.includes('licdn.com') || src.startsWith('http')) imgs.push(src);
    });

    const idMatch = urn && urn.match(/\d+/);
    out.push({
      urn, activityId: idMatch ? idMatch[0] : null,
      likes, fullText: text, imgs
    });
  });
  window.__profileData = out;
  return JSON.stringify({total: out.length, withLikes: out.filter(p => p.likes !== null).length});
})()
```

## Step 4 — Rank top 50 + save manifest

Sort by likes descending, take top 50. Save manifest CSV with rank, likes, filename, activity URL.

```js
(() => {
  const sorted = window.__profileData.slice().sort((a, b) => (b.likes || 0) - (a.likes || 0));
  window.__top50 = sorted.slice(0, 50).map((p, i) => ({
    r: i + 1,
    l: p.likes,
    a: p.activityId,
    u: `https://www.linkedin.com/feed/update/urn:li:activity:${p.activityId}/`,
    t: p.fullText.replace(/\s+/g, ' '),
    img: (p.imgs.find(x => !x.startsWith('VIDEO_POSTER:')) || p.imgs[0] || '')
  }));
  return JSON.stringify({stored: window.__top50.length});
})()
```

**Important — Tool output truncation:** The browser JS tool truncates output at ~1500 chars and may block strings containing query-string tokens (LinkedIn signed URLs). To extract the data:

1. Build a compact string per post (rank, likes, URL, snippet)
2. Chunk into 900-char pieces stored on `window.__chunks`
3. Retrieve one chunk per JS call

```js
// Build chunks
(() => {
  const compact = window.__top50.map(p =>
    `${p.r}|${p.l}|${p.u}|${p.t.substring(0, 180).replace(/\|/g, '/')}`
  ).join('\n');
  window.__chunks = [];
  for (let i = 0; i < compact.length; i += 900) {
    window.__chunks.push(compact.substring(i, i + 900));
  }
  return JSON.stringify({chunks: window.__chunks.length, totalLen: compact.length});
})()
```

Then retrieve chunks one at a time: `window.__chunks[0]`, `window.__chunks[1]`, etc.

After collecting all chunks, write the **ranked list markdown** with snippets + the manifest CSV to outputs.

## Step 5 — Bundle images into ZIP + trigger download

LinkedIn images are at signed URLs on `media.licdn.com`. The Linux sandbox CANNOT curl them (network blocked for licdn). The browser CAN fetch them (already authenticated).

**Strategy:** Use the browser to fetch all images, build a hand-rolled ZIP using STORED format (no compression — simpler, avoids needing a CDN library that LinkedIn's CSP would block), then trigger ONE download.

The download lands in Chrome's Downloads folder. Tell the user to drag the zip to their target folder and extract.

```js
// Fetch all images + build ZIP in one call
(async () => {
  const crcTable = new Uint32Array(256);
  for (let i = 0; i < 256; i++) {
    let c = i;
    for (let j = 0; j < 8; j++) c = (c & 1) ? (0xedb88320 ^ (c >>> 1)) : (c >>> 1);
    crcTable[i] = c >>> 0;
  }
  function crc32(buf) {
    let crc = 0xffffffff;
    for (let i = 0; i < buf.length; i++) crc = crcTable[(crc ^ buf[i]) & 0xff] ^ (crc >>> 8);
    return (crc ^ 0xffffffff) >>> 0;
  }

  const files = [];
  let failed = 0;
  for (const meta of window.__top50) {
    const url = meta.img;
    if (!url) { failed++; continue; }
    try {
      const resp = await fetch(url);
      if (!resp.ok) { failed++; continue; }
      const data = new Uint8Array(await resp.arrayBuffer());
      const ct = resp.headers.get('content-type') || '';
      let ext = 'jpg';
      if (ct.includes('png')) ext = 'png';
      else if (ct.includes('gif')) ext = 'gif';
      else if (ct.includes('webp')) ext = 'webp';
      files.push({name: `rank${String(meta.r).padStart(2,'0')}_id${meta.a}.${ext}`, data});
    } catch(e) { failed++; }
  }

  const enc = new TextEncoder();
  const localParts = [], cdParts = [];
  let offset = 0;
  for (const f of files) {
    const nameBytes = enc.encode(f.name);
    const data = f.data;
    const crc = crc32(data);
    const lfh = new ArrayBuffer(30);
    const lv = new DataView(lfh);
    lv.setUint32(0, 0x04034b50, true);
    lv.setUint16(4, 20, true); lv.setUint16(6, 0, true); lv.setUint16(8, 0, true);
    lv.setUint16(10, 0, true); lv.setUint16(12, 0x21, true);
    lv.setUint32(14, crc, true); lv.setUint32(18, data.length, true); lv.setUint32(22, data.length, true);
    lv.setUint16(26, nameBytes.length, true); lv.setUint16(28, 0, true);
    localParts.push(new Uint8Array(lfh), nameBytes, data);
    const cd = new ArrayBuffer(46);
    const cv = new DataView(cd);
    cv.setUint32(0, 0x02014b50, true);
    cv.setUint16(4, 20, true); cv.setUint16(6, 20, true); cv.setUint16(8, 0, true);
    cv.setUint16(10, 0, true); cv.setUint16(12, 0, true); cv.setUint16(14, 0x21, true);
    cv.setUint32(16, crc, true); cv.setUint32(20, data.length, true); cv.setUint32(24, data.length, true);
    cv.setUint16(28, nameBytes.length, true); cv.setUint16(30, 0, true); cv.setUint16(32, 0, true);
    cv.setUint16(34, 0, true); cv.setUint16(36, 0, true); cv.setUint32(38, 0, true);
    cv.setUint32(42, offset, true);
    cdParts.push(new Uint8Array(cd), nameBytes);
    offset += 30 + nameBytes.length + data.length;
  }
  const cdSize = cdParts.reduce((s, p) => s + p.length, 0);
  const eocd = new ArrayBuffer(22);
  const ev = new DataView(eocd);
  ev.setUint32(0, 0x06054b50, true);
  ev.setUint16(4, 0, true); ev.setUint16(6, 0, true);
  ev.setUint16(8, files.length, true); ev.setUint16(10, files.length, true);
  ev.setUint32(12, cdSize, true); ev.setUint32(16, offset, true); ev.setUint16(20, 0, true);

  const blob = new Blob([...localParts, ...cdParts, new Uint8Array(eocd)], {type: 'application/zip'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = '[HANDLE]_top50_images.zip'; // <-- replace [HANDLE] before running
  document.body.appendChild(a);
  a.click();
  setTimeout(() => { URL.revokeObjectURL(url); a.remove(); }, 2000);
  return JSON.stringify({files: files.length, failed, sizeMB: (blob.size/1024/1024).toFixed(2)});
})()
```

Tell the user the zip is in their Chrome Downloads folder.

## Step 6 — Generate rewrites using Cookbook + Welsh

For each of the top 50, generate a fresh rewrite. **Critical IP guidance:** Use the underlying real-world EVENT (which is a fact, not copyright) as the basis. Do NOT paraphrase the original wording. Write entirely new copy from scratch.

### The formula
```
Hook (1-2 lines visible before "see more")
→ Story (vivid, specific, white-space heavy)
→ Author's lens (leadership / faith / human truth)
→ Aspirational close (question or imperative)
```
Target ratio: ~70% story / 30% author commentary.

### Welsh framework rotation
Pick one primary framework per post (rotate so the same one isn't used twice in a row):
1. Story Arc (default — use ~70% of the time)
2. Hot Take (commentary on a current event)
3. Contrarian Take (challenge a common belief)
4. Step-by-Step (frame as teachable process)
5. Before/After (transformation framing)
6. Data Drop (lead with a stat)
7. Framework Reveal (name the lens)
8. Mistake List (vulnerability)
9. Curated List (3-5 connected stories)
10. Comparison (side-by-side)

### Cookbook stack rotation
Pick 3-4 principles per post. The high-leverage stacks for Story Arc posts:
- **Identifiable Victim Effect** (specific name + age)
- **Negativity Bias hook** (open with the conflict)
- **Halo Effect** (show character early)
- **Peak-End Rule** (close strong)
- **Self-Reference Effect** (let reader project)
- **Reciprocity** (act of grace)
- **Authority Figure** (cop, surgeon, veteran)
- **Reverse Norm** (someone defying expectation)
- **Anchoring** (specific number)
- **Tiny Habits** (small recurring acts)
- **Goal Gradient** (proximity to outcome)
- **Identity & Self-Concept** (who they are)

### Per-post output format
```
## #N — original [LIKES] likes

**Subject:** [The factual event in 1 sentence]
**Welsh framework:** [Primary] → [Secondary]
**Cookbook stack:** [Principle 1] → [Principle 2] → [Principle 3] → [Principle 4]
**Original:** [URL]

---

[FRESH POST COPY — 120-220 words, no paraphrase of original wording]
```

Save all 50 to `[handle]_top50_rewrites.md` with a header explaining the methodology.

## Step 7 — AB-test recommendation memo

Generate a strategic memo at `[handle]_ab_test_recommendations.md`:

```markdown
# [Handle] — LinkedIn Content Engine: AB-Test Recommendations

## Pattern recognition (from top 50 analysis)
- Welsh frameworks used: [list with counts]
- Cookbook principles activated: [list with counts]
- Most common archetype: [name + count]
- Engagement floor (top 50 minimum): [N likes]
- Engagement ceiling (top 1): [N likes — viral outlier]

## Top 3 archetypes to AB-test first
For each archetype:
- The pattern (1-2 sentences)
- Original example (rank + URL)
- Rewrite example (link to rewrites doc)
- Hypothesis (e.g., "rewrite + Cookbook stack will outperform original by 15%")
- Variables to control (post time, image, length)

## Posting cadence (Welsh Hub & Spoke applied)
- Recommended cadence: [N] posts/week
- Framework rotation: [framework day-by-day breakdown]
- Hub & Spoke: each post → 2-3 derivative pieces (quote graphic, video script, newsletter section)

## KPIs to watch
1. Click-to-expand rate (>30% = strong hook)
2. Comment-to-like ratio (>5% = CTA converting)
3. Reshare velocity in first 60 minutes (algorithmic signal)
4. Unique commenter rate (community vs broadcast)

## What to test next
- [3 specific test ideas based on this profile's gaps]
```

## Step 8 — Deliver + close out

Save all files to `outputs/` with the handle prefix. Mark all tasks completed. Summarize for the user:

- Link to top 50 markdown
- Link to manifest CSV
- Note that zip is in Chrome Downloads
- Link to rewrites doc
- Link to AB-test memo
- One BLUF strategic recommendation

---

# Quirks + edge cases

**LinkedIn URL variants:** Profile URLs come in many forms. Always normalize to `/in/[handle]/recent-activity/all/`. Note that `/recent-activity/posts/` redirects to `/articles/` — don't use it.

**Activity feed pagination:** Caps at ~25 months. Older posts are not retrievable through this method. To get the true all-time top 50, ask the user to request their LinkedIn data export (Settings → Data Privacy → Get a copy of your data → Posts). CSV arrives in 24-48 hours.

**Image-only posts:** Some viral posts have no caption. Mark them as `[Image post — no caption]` in the snippet, but still extract the image URL.

**Video posts:** Use `video.poster` attribute as the thumbnail. Prefix the URL with `VIDEO_POSTER:` so downstream code can identify them.

**Tool output truncation:** ~1500 char limit per JS tool call. Strings with auth tokens may get blocked entirely. Use chunking + base64 to bypass.

**JS execution timeout:** ~45 seconds per call. Keep loops bounded (e.g., 8 iterations of 3-second waits = 24s, leaving margin).

**Chrome download permission:** Chrome may prompt "Allow [site] to download multiple files?" the first time. The user must approve once.

**Repeat profiles:** If the user re-runs on the same profile, the data may have changed (likes accumulate). Always re-pull, never trust a cache.

**Privacy:** Don't run on profiles where the user doesn't have legitimate need (creator they follow, competitor, themselves, public figure). Don't aggregate PII from random profiles for cross-referencing.

**IP-aware rewriting:** Most viral story posts on LinkedIn are reshares of third-party content. Even with releases in hand, the BEST output is transformative original commentary on the underlying real-world event — not a paraphrase. Use the facts as basis; write fresh wording.

---

# Quality checklist (run before declaring done)

- [ ] Profile URL was validated and normalized
- [ ] At least 100 posts loaded before extraction
- [ ] All top 50 have non-null like counts
- [ ] Image manifest CSV matches rank order
- [ ] Zip download was triggered with correct filename
- [ ] All 50 rewrites are 120-220 words
- [ ] Each rewrite tagged with Welsh framework + Cookbook stack
- [ ] AB-test memo names 3 specific archetypes with hypotheses
- [ ] All files saved to outputs with `[handle]_` prefix
- [ ] User given direct links to view each output
