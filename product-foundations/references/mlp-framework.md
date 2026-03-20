## Contents
- Why MLP Replaced MVP
- The Four MLP Principles in Full
  - Principle 1: Start with the User's Why, Not the Business Why
  - Principle 2: Separate Problem Space from Solution Space
  - Principle 3: Listen to Users — But Not Literally
  - Principle 4: Enter Solution Space and Choose Your Game
- The Minimum Part — How to Scope an MLP
- Pixie Dust — Making It Memorable
- Testing MLP Lovability — The Alpha/Beta/GA Framework
- MLP Anti-Patterns

---
# Minimum Lovable Product — Deep Reference
*Source: JZ's "Don't Serve Burnt Pizza," First Round Review + Lenny's Podcast episode*

---

## Why MLP Replaced MVP

The Minimum Viable Product served a specific era: when products were the "first of X" and users had no alternatives. Ship something functional, learn if the problem exists, iterate.

That era is over. Today:
- Users have alternatives in almost every category
- Competition means the first impression is often the only impression
- Shipping a barely-functional version teaches you about the flaw, not the underlying idea

**The burnt pizza test:** If you're testing whether people like pizza and you serve them burnt pizza, you learn they don't like burnt pizza — not whether they like pizza. An MVP that's flawed or undercooked gives you feedback on the flaws, not on your core hypothesis.

**MLP shifts the question:**
- MVP: "Does this problem exist?"
- MLP: "Do users love our solution enough to tell others about it?"

---

## The Four MLP Principles in Full

### Principle 1: Start with the User's Why, Not the Business Why

Every product initiative has two "whys" — the business's and the user's. They are not the same. Great PMs hold both, but always start with the user's.

**Business why vs. user why — examples:**

| Business Why | User Why |
|-------------|----------|
| Grow supply of homes (Airbnb) | Have more great options at desirable destinations |
| Compete with luxury hotels | Have a vacation experience that feels special and uniquely Airbnb |
| Increase engagement metrics | Have a daily practice that actually fits into my daily life |
| Reduce churn | Feel like the app understands what I need today |

**The litmus test sentence:**
> "Wouldn't it be amazing if this product could ___?"

Fill in the blank with a user benefit. If you instinctively fill it with a business benefit ("help us compete with X"), you haven't found the user's why yet.

**The local maximum trap:**
When JZ's team at Dropbox built Project Harmony (showing when collaborators are in the same doc), they were optimizing a local maximum — a useful but shallow fix. The user's actual why was real-time collaborative editing. By not understanding the user's why deeply enough, they missed the global maximum (what became Dropbox Paper). Every local maximum solution has a global maximum solution adjacent to it that you'll miss if you stop too early.

---

### Principle 2: Separate Problem Space from Solution Space

The single most common product mistake. Solutions feel productive. They're concrete, discussable, shippable. Problem exploration feels slow and fuzzy.

But the quality of your solution is entirely bounded by the quality of your problem understanding.

**JZ's classroom rule:** Students can't discuss solutions for the first third of the semester. On day one, she writes their solution ideas on the board — then ignores them. By the time they're ready to open solution space, their original ideas are almost always wrong.

**The two-column exercise:**

```
PROBLEM SPACE (discuss freely)     |  SOLUTION SPACE (blocked until ready)
-----------------------------------|------------------------------------------
Users don't know what to engage      |  
about when they open the app       |  
                                   |  
Users feel their streak doesn't    |  
actually reflect their personal   |  
growth                             |  
                                   |  
Users want community but feel      |  
awkward interacting with strangers     |  
```

Rules:
1. No filtering during problem brainstorm — all problems welcome
2. If someone proposes a solution, acknowledge it, write it on the right, set it aside
3. Only after ranking problems by value: open the right column
4. The highest-value problem constrains the solution space

**Choosing your game:**
Once you've ranked problems, ask: "Is this the problem we want to spend the next quarter on? Do we have the right skills? Are we willing to invest 5–10 years in this space?" Being intentional about problem selection is itself a strategic act.

---

### Principle 3: Listen to Users — But Not Literally

User research is essential. Taking users literally is fatal.

**Three common mistakes in user research:**

**1. Asking what they want**
Users describe solutions, not problems. "I want a search feature" is a solution. The problem might be "I can't find engagements I've saved." If you build the search feature without understanding why they want it, you'll build the wrong search feature.

Instead, ask: "What do you find tedious, stressful, or painful?" Then listen for emotional signals — frustration, embarrassment, relief, joy. These indicate high-value problems.

**2. Positioning yourself as the expert**
Users defer to perceived authority. If you walk into a user interview as "the product manager," users will try to give you answers they think you want to hear. Make the dynamic explicit: "You are the expert on your experience. I know nothing about what it's like to be you. Help me understand."

**3. Mixing personas without segmentation**
Feedback from different user types cancels out. Early consumers trying to build a daily habit have completely different needs from longtime communitygoers who want premium content notes. Interview them separately and be explicit about which findings belong to which segment.

**The literal trap — Henry Ford principle:**
"If I had asked people what they wanted, they would have said faster horses." Users request solutions in the frame of what they already know. Your job is to hear the underlying problem (getting somewhere faster) and imagine solutions they haven't conceived of.

**What to listen for:**
- Intensity of frustration: "I can't believe I still have to do this manually"
- Time lost: "I spend so much time doing X when I just want Y"
- Workarounds: "What I usually do is..." (workarounds = unmet needs)
- Emotional stakes: "It's embarrassing when..." / "It makes me so happy when..."

---

### Principle 4: Enter Solution Space and Choose Your Game

Once you've mapped the problem space and selected the highest-value problem, you're ready for solution space ideation.

**The diverge → converge → diverge → converge pattern:**
```
Diverge: explore all possible problems (problem space)
Converge: select the highest-value problem
Diverge: brainstorm all possible solutions (solution space)
Converge: select the most lovable, minimum solution
```

**In solution space ideation:**
- Generate many ideas without filtering (quantity first)
- Ask users: "Out of these possibilities, which do you wish existed?"
- Watch for the "face lighting up" signal — that's your direction

**The lovability test:**
When users see a prototype or hear a concept, listen for:
- "This is cool, I can see myself using this" → NOT lovable enough
- "Oh my god, when can I start using this?" → LOVABLE — you've solved a high-value problem in a way they love

The second reaction is rarer than you think. Most product teams celebrate the first reaction and ship. The teams that build truly beloved products hold out for the second.

---

## The Minimum Part — How to Scope an MLP

The hardest word in "minimum lovable product" is minimum. How do you deliver something lovable while keeping it minimum?

**The answer: focus minimum on problems addressed, not features shipped.**

Pick ONE problem. Solve it completely and lovably. Don't solve three problems at 60% each.

**The Airbnb Plus 200-point list lesson:**
JZ's team built a hotel-grade checklist of 200 items that Airbnb Plus homes needed to have. When they looked at it, they realized they'd have zero qualifying homes — and had lost sight of what made Airbnb special (feeling like home, not a hotel). They scoped back to one lovable digital feature: the Home Tour, a photography flow that let users virtually "walk through" a home. Cheaper, more distinctively Airbnb, and more lovable than any hotel amenity.

**The Peanut Butter Principle:**
> "Spread too thin, it's no longer tasty."

Every feature you add to an MLP dilutes your ability to make any of them truly lovable. The discipline is saying no — not to the user's need, but to solving it right now.

---

## Pixie Dust — Making It Memorable

Pixie dust is the moment in the user journey where the product transcends utility and becomes memorable. It's what users talk about. It's what earns word-of-mouth.

**Properties of good pixie dust:**
- **Specific to your user** — generic delight is hollow; targeted delight resonates deeply
- **Timed perfectly** — meets the user at a moment of peak emotional relevance
- **Doesn't require much** — often a small gesture, not a major feature
- **Surprising** — by definition, pixie dust exceeds expectations

**Examples:**

*Airbnb check-in guide:* As a traveler approaches their destination with GPS on, a check-in guide pops up with exactly what they need: where the key is, the lockbox code, the WiFi password. The anxiety of arriving in an unfamiliar place is met with a perfectly timed gesture. Lovable because it anticipated a specific moment of stress.

*Snackpass:* Emoji-rich copy, gifting features with puns ("I love you a latte"), playful language that speaks exactly to college students. Pixie dust doesn't need to be sophisticated — it needs to be *right for your user*.

**Finding your pixie dust — three questions:**
1. When a user signs up, what should be the first emotion they feel?
2. What would bring a smile to a user's face at an unexpected moment?
3. What would give a user a reason to tell their friends?

**For your product — pixie dust hypotheses:**
- A content suggestion that appears exactly when your GPS shows you're at a hospital (contextual personal support)
- A milestone notification: "You've completed 40 days of morning routine" with a meaningful message (meaningful framing)
- A streak visualization that shows your active days as a personal progress map
- A personalized note from the engagement session author when you complete a full series

---

## Testing MLP Lovability — The Alpha/Beta/GA Framework

**Alpha (most loyal users):**
- Already love you — would appreciate almost anything you ship
- Use for: directional signal, major bugs, baseline usability
- Don't trust: their enthusiasm (it's not representative)

**Beta (satisfied but critical users):**
- Root for you AND give hard feedback
- Remember friction moments they've forgiven but haven't forgotten
- Use for: validating lovability, testing pixie dust, iterating before wide release
- This is where MLP testing happens — not alpha, not GA

**GA (everyone):**
- Skeptical, unforgiving, high bar
- Launching unlovable features to GA = burning trust
- Trust is hard to earn and very hard to regain once lost

**The rule:** Stay in beta longer than feels comfortable. Ship to GA only when you have strong beta evidence of the "when can I start using this?" reaction.

---

## MLP Anti-Patterns

**The feature checklist fallacy:** Building a list of features that together "make" a product lovable, then building them all. Lovability isn't additive — it comes from depth on the right feature, not breadth across many.

**The copy-paste trap:** Seeing a feature that works at another company and building it without understanding *why* it works. JZ's Gardenscapes moves counter mistake: the counter worked in Gardenscapes because each move was a strategic decision. Duolingo lessons don't involve strategy — you either know the answer or you don't. Context kills copy-pastes.

The right way to borrow: Ask (1) why does this work in that product? (2) why might it succeed or fail in our context? (3) what adaptations are necessary?

**The local maximum fixation:** Optimizing a feature that works but misses the bigger opportunity. Always ask: is this the highest-value problem, or am I solving the nearest one?

**Shipping to prove you can ship:** New PMs and product leaders often feel pressure to ship quickly. Shipping fast without MLP discipline ships something unlovable — and damages both user trust and team credibility.
