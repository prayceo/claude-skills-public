# Gatena Cookbook Principles Library

> 190 principles from academic behavioural science research, organized for design application.
> Each entry: **Name** | Definition | Design Application | 📎 Academic Citation (where available)
> Sourced and enriched from the Gatena Cookbook research + additional behavioural science literature.

## Table of Contents
1. [Attention & Perception](#1-attention--perception) (Principles 1-16)
2. [Cognitive Load & Processing](#2-cognitive-load--processing) (Principles 17-31)
3. [Decision Architecture](#3-decision-architecture) (Principles 32-48)
4. [Framing & Presentation](#4-framing--presentation) (Principles 49-63)
5. [Social Dynamics](#5-social-dynamics) (Principles 64-82)
6. [Trust & Credibility](#6-trust--credibility) (Principles 83-95)
7. [Motivation & Engagement](#7-motivation--engagement) (Principles 96-115)
8. [Emotion & Affect](#8-emotion--affect) (Principles 116-130)
9. [Memory & Recall](#9-memory--recall) (Principles 131-143)
10. [Loss, Risk & Uncertainty](#10-loss-risk--uncertainty) (Principles 144-158)
11. [Pricing & Value Perception](#11-pricing--value-perception) (Principles 159-178)
12. [Identity & Self-Concept](#12-identity--self-concept) (Principles 179-189)
13. [Cross-Cutting Principles](#13-cross-cutting-principles) (Principles 190+)

---

## 1. Attention & Perception

**1. Von Restorff Effect (Isolation Effect)**
Things that stand out from their surroundings are more likely to be remembered and noticed.
*Design: Make your primary CTA visually distinct from everything else on the page — different colour, size, or shape.*

**2. Visual Salience**
Elements that contrast with their environment in colour, size, motion, or orientation capture attention automatically.
*Design: Use colour contrast and whitespace to draw the eye to key actions. Avoid making everything "pop" — when everything is bold, nothing stands out.*
📎 Taylor & Thompson (1982). Stalking the elusive "vividness" effect. Psychological Review.

**3. Banner Blindness**
People have learned to ignore content that looks like advertising or appears in typical ad locations.
*Design: Avoid placing important information in banner-like formats at the top of pages. Integrate key messages into content areas instead.*

**4. Inattentional Blindness**
When focused on one task, people fail to notice unexpected elements even when they're clearly visible.
*Design: Don't rely on passive notifications or subtle changes to communicate important information. Use interruptive patterns for critical alerts.*

**5. Change Blindness**
People often fail to notice changes that occur during a visual disruption (like a page transition).
*Design: When updating content dynamically, use animation or highlighting to draw attention to what changed. Don't silently update values.*

**6. Selective Attention**
People focus on information relevant to their current goal and filter out the rest.
*Design: Understand the user's primary task and remove visual noise that competes for attention. Progressive disclosure keeps focus tight.*

**7. Gestalt Principles (Proximity, Similarity, Closure, Continuity)**
People perceive visual elements as organized groups based on proximity, similarity, enclosure, and alignment.
*Design: Group related elements spatially. Use consistent styling for items that belong together. Separate unrelated sections with whitespace or dividers.*

**8. Figure-Ground Relationship**
People instinctively separate visual fields into a foreground (focus) and background (context).
*Design: Use contrast, elevation (shadows), and layering to clearly separate interactive elements from the background. Modals and overlays rely on this.*

**9. Fitts's Law**
The time to reach a target is a function of its size and distance. Larger, closer targets are faster to interact with.
*Design: Make primary actions large and position them near where the user's cursor or thumb already is. Reduce distance between related actions.*

**10. Hick's Law**
Decision time increases logarithmically with the number of options presented.
*Design: Limit choices at each step. Break complex decisions into sequential smaller ones. Use progressive disclosure rather than overwhelming option sets.*

**11. Serial Position Effect**
People best remember items at the beginning (primacy) and end (recency) of a list.
*Design: Place the most important items or features first and last in any list, navigation, or sequence. Middle items get less attention.*

**12. Attentional Bias**
People pay more attention to emotionally stimulating information.
*Design: Use emotionally relevant imagery and language near important elements. A face showing emotion near a CTA draws more attention than a stock photo.*

**13. Weber's Law**
The just-noticeable difference between two stimuli is proportional to the original stimulus magnitude.
*Design: Small changes to large numbers go unnoticed (price increases on expensive items). To make changes perceptible, they need to be proportionally significant.*

**14. Visual Hierarchy**
People scan content in predictable patterns (F-pattern for text, Z-pattern for visual pages) prioritizing larger, bolder, higher elements.
*Design: Structure layouts to match natural scanning patterns. Place key messages and CTAs in hotspots. Use size, weight, and position to establish clear reading order.*

**15. Peripheral Vision Influence**
Information in peripheral vision is processed at a basic level and can influence attention and behaviour.
*Design: Use subtle motion, colour changes, or pattern breaks in peripheral areas to redirect attention without being disruptive. Sidebar notifications can leverage this.*

**16. Centre-Stage Effect**
We prefer the middle option in a set of choices.
*Design: Place your target option in the center position of any horizontal layout. In pricing pages, put the plan you want most users to choose in the middle column.*

---

## 2. Cognitive Load & Processing

**17. Cognitive Load Theory**
Working memory has limited capacity (~4 chunks). Exceeding it causes errors, frustration, and abandonment.
*Design: Reduce the amount of information and choices presented at once. Break complex tasks into steps. Don't require users to remember information across screens.*

**18. Miller's Law**
People can hold approximately 7±2 items in working memory at once.
*Design: Chunk information into groups of 5-9. Phone numbers, account numbers, and step counts should respect this limit. Navigation items ideally stay under 7.*

**19. Processing Fluency**
People prefer things that are easy to process mentally. Fluent experiences feel more true, more beautiful, and more trustworthy.
*Design: Use clean layouts, legible typography, simple language, and high contrast. If it feels easy to read, people trust it more.*

**20. Cognitive Ease**
When things feel easy to think about, people are more likely to feel positive about them and take action.
*Design: Reduce friction everywhere — simpler forms, clearer labels, fewer steps. Pre-fill what you can. Make the default path the easiest path.*

**21. Curse of Knowledge**
Once you know something, it's difficult to imagine not knowing it, leading to communication that assumes too much.
*Design: Write copy and design flows as if the user has zero context. Test with people outside your team. Jargon that seems obvious to you is often confusing.*

**22. Paradox of Choice**
Too many options can lead to decision paralysis, dissatisfaction, and regret.
*Design: Curate choices. Offer recommended options. Use filters and progressive disclosure rather than showing everything at once.*

**23. Information Overload**
When presented with too much information, people's decision quality degrades and they may disengage entirely.
*Design: Show only what's needed for the current decision. Use progressive disclosure, expandable sections, and smart defaults to manage information volume.*

**24. Dual Process Theory (System 1 / System 2)**
People have two thinking modes: fast/intuitive (System 1) and slow/deliberate (System 2). Most decisions use System 1.
*Design: Design for System 1 by default — make key paths intuitive and require minimal deliberation. Only invoke System 2 for high-stakes decisions where careful thought helps.*

**25. Chunking**
Breaking information into meaningful groups (chunks) makes it easier to process and remember.
*Design: Group form fields logically. Break long content into scannable sections. Use headers, bullets, and whitespace to create digestible chunks.*
📎 Miller, G. (1956). The Magical Number Seven, Plus or Minus Two. Psychological Review.

**26. Disfluency Effect**
Slightly harder-to-process information can sometimes lead to deeper processing and better retention.
*Design: For educational content or important disclosures, a slightly unusual font or layout can increase careful reading. Use sparingly and intentionally.*

**27. Representativeness Heuristic**
People judge probability by how well something matches a prototype or stereotype rather than actual statistics.
*Design: Make your product look like what users expect the "best" version to look like. A financial app should look trustworthy and clean. A creative tool should feel vibrant.*

**28. Availability Heuristic**
People judge the likelihood of events based on how easily examples come to mind.
*Design: Show recent, vivid examples of success (testimonials, case studies) to make positive outcomes feel more probable. Use concrete examples over abstract statistics.*
📎 Tversky & Kahneman (1973). Availability: A heuristic for judging frequency and probability. Cognitive Psychology.

**29. Recognition Over Recall**
People are better at recognizing previously encountered information than recalling it from memory.
*Design: Use menus, dropdowns, and suggestion lists rather than requiring users to type from memory. Show recent items and favourites.*

**30. Fluency Heuristic**
Information that is processed more fluently (easily) is judged as more true, familiar, or valuable.
*Design: Ensure key claims and value propositions are typographically clear, well-spaced, and use simple language. Hard-to-read text reduces credibility.*

**31. Satisficing**
Rather than optimizing, people often choose the first option that meets a minimum threshold of acceptability.
*Design: Present your strongest option first. Make your recommended choice clearly visible and easy to select. Don't bury the best option in a long list.*

**32. Metaphorical Shortcut**
We use metaphors to simplify complex decisions.
*Design: Use familiar metaphors in UX copy and information architecture. "Shopping cart," "dashboard," and "inbox" all leverage metaphorical shortcuts to reduce cognitive load.*

---

## 3. Decision Architecture

**33. Default Effect**
People tend to stick with pre-selected or default options, even when alternatives are available.
*Design: Set defaults thoughtfully — the default option gets chosen disproportionately. Pre-check beneficial settings. Make the default the action you want most users to take.*
📎 Johnson & Goldstein (2003). Do defaults save lives? Science, Vol. 302.

**34. Nudge Theory**
Small changes in the choice environment (nudges) can significantly influence behaviour without restricting options.
*Design: Use defaults, framing, social proof, and simplification to guide users toward beneficial choices without removing alternatives.*

**35. Choice Architecture**
The way options are arranged and presented systematically influences which options people choose.
*Design: Order matters. Options presented first and last get more attention. Recommended/highlighted options get selected more. Structure your layout intentionally.*

**36. Anchoring Effect**
The first piece of information encountered serves as a reference point for all subsequent judgments.
*Design: Show the higher price first to make other options seem affordable. Present the ideal plan first. In negotiations, set the starting point strategically.*
📎 Tversky & Kahneman (1974). Judgment under Uncertainty: Heuristics and Biases. Science.

**37. Decoy Effect (Asymmetric Dominance)**
Adding an inferior third option can make one of two original options seem significantly more attractive.
*Design: In pricing tiers, add a "decoy" plan that's clearly worse than the target plan to make the target look like the obvious best value.*
📎 Huber, Payne & Puto (1982). Adding Asymmetrically Dominated Alternatives. Journal of Consumer Research.

**38. Paradox of Choice / Choice Overload**
Having too many options leads to decision paralysis, lower satisfaction, and increased regret.
*Design: Limit the number of product variants shown. Offer curated selections. Use "recommended for you" to reduce choice burden.*

**39. Status Quo Bias**
People prefer the current state of affairs and resist change, even when change would benefit them.
*Design: Minimize disruption in redesigns. Introduce changes gradually. When asking users to switch, emphasize what stays the same alongside what improves.*
📎 Samuelson & Zeckhauser (1988). Status quo bias in decision making. Journal of Risk and Uncertainty.

**40. Commitment and Consistency**
Once people commit to something (even a small action), they feel compelled to behave consistently with that commitment.
*Design: Start with small asks (email signup, free trial) before larger ones (purchase). Multi-step forms that begin with easy questions leverage this.*
📎 Cialdini, R. (1984). Influence: The Psychology of Persuasion.

**41. Foot-in-the-Door Technique**
Agreeing to a small request makes people more likely to agree to a larger related request later.
*Design: Ask users to do something small first (take a quiz, create a free account, watch a demo) before asking for the big commitment (purchase, subscribe).*
📎 Freedman & Fraser (1966). Compliance Without Pressure: The Foot-in-the-Door Technique. Journal of Personality and Social Psychology.

**42. Door-in-the-Face Technique**
Starting with a large request that gets refused, then following with a smaller request, increases compliance with the smaller one.
*Design: Show the premium/enterprise option first. After seeing a high price, the standard option feels much more reasonable.*
📎 Cialdini, Vincent, Lewis, Catalan, Wheeler & Darby (1975). Reciprocal concessions procedure for inducing compliance. Journal of Personality and Social Psychology.

**43. Mere Exposure Effect**
Repeated exposure to something increases preference for it, even without conscious awareness.
*Design: Consistent branding across touchpoints builds preference. Retargeting works because familiarity breeds liking. Repeat key messages.*
📎 Zajonc (1968). Attitudinal effects of mere exposure. Journal of Personality and Social Psychology.

**44. Distinction Bias**
People overvalue differences when comparing options side-by-side, but those differences often don't matter in actual use.
*Design: Be thoughtful with comparison tables — they can make trivial differences seem important and lead to over-spending. Highlight differences that genuinely matter.*

**45. Single-Option Aversion**
People are reluctant to choose when only one option is presented, even if it's a good one.
*Design: Always present at least two options (even if one is clearly better). "Choose your plan" works better than "Here's our plan, take it or leave it."*

**46. Decision Fatigue**
The quality of decisions deteriorates after making many decisions in sequence.
*Design: Put the most important decision early in the flow. Reduce unnecessary choices. Use smart defaults later in processes when user energy is depleted.*

**47. Implementation Intentions**
Specific plans about when, where, and how to act dramatically increase follow-through.
*Design: After a user commits to something, help them plan the specifics. "When would you like to start?" is more effective than "Good luck!"*

**48. Present Bias**
People disproportionately value immediate rewards over future ones, even when waiting is objectively better.
*Design: Offer immediate gratification — instant access, immediate feedback, quick wins. Frame future benefits in terms of what the user gets right now.*
📎 O'Donoghue & Rabin (1999). Doing It Now or Later. American Economic Review.

**49. Pre-commitment**
People are more likely to follow through on goals if they commit to a plan of action in advance.
*Design: Allow users to schedule future actions, set reminders, or publicly commit to goals. Meal prep apps and savings tools use this effectively.*

**50. Path of Least Resistance**
People tend to take whatever action requires the least effort.
*Design: Make the desired action the easiest one. Reduce form fields. Auto-fill information. One-click actions. Every extra step loses users.*

---

## 4. Framing & Presentation

**51. Framing Effect**
The way information is presented (framed) significantly affects decisions and judgments, even when the underlying facts are identical.
*Design: "95% satisfaction rate" is more compelling than "5% dissatisfaction rate." Frame outcomes positively. Frame inaction in terms of loss.*
📎 Tversky & Kahneman (1981). The framing of decisions and the psychology of choice. Science, 211(4481).

**52. Loss Framing**
Describing outcomes in terms of what people stand to lose is more motivating than equivalent gains.
*Design: "Don't miss out" and "You'll lose access" are more motivating than "Join now" and "Gain access." Use loss framing for important actions.*

**53. Gain Framing**
Positive framing works better for encouraging preventive or low-risk behaviours.
*Design: For building trust and encouraging exploration, use gain framing: "Save 2 hours per week" rather than "Stop wasting 2 hours per week."*

**54. Attribute Framing**
Describing a single attribute positively vs. negatively changes how the whole product is perceived.
*Design: "90% lean" beef sells better than "10% fat" beef. Frame product attributes in the most positive truthful way.*

**55. Temporal Framing**
How time is framed affects perceived value. Costs feel smaller when broken into smaller time periods.
*Design: "$1/day" feels much cheaper than "$365/year" even though it's the same. Frame subscription costs daily or weekly for lower perceived cost.*

**56. Narrative Framing / Storytelling**
Information embedded in stories is more engaging, memorable, and persuasive than abstract facts.
*Design: Use customer stories and case studies rather than feature lists. Structure your marketing as a narrative: problem → solution → transformation.*

**57. Reframing**
Changing the reference point or context for information can fundamentally alter its perceived meaning.
*Design: A $50 product next to a $500 product feels cheap. Time saved framed as "that's a whole extra vacation day per month" is more tangible.*

**58. Primacy Effect**
Information presented first has a stronger influence on overall impression than information that comes later.
*Design: Lead with your strongest benefit, most impressive stat, or most compelling image. First impressions set the tone for everything that follows.*

**59. Recency Effect**
The most recently presented information is often the most readily recalled.
*Design: End on a strong note. Put your CTA and key value proposition at the end of a page/flow as well as the beginning. Last impressions drive action.*

**60. Context Effect**
The surrounding context in which something is presented changes how it's perceived.
*Design: Premium products should be displayed in premium-looking environments. Low-quality surroundings diminish perceived product quality.*

**61. Contrast Effect**
People evaluate things relative to what they've just experienced, not in absolute terms.
*Design: Show a complex competitor experience before your simple one. Present the expensive option before the target option. Before/after comparisons leverage this.*

**62. Order Effects**
The sequence in which options or information are presented influences which gets chosen or remembered.
*Design: The first and last positions in a list get disproportionate attention. Place your recommended option first or use visual emphasis to override position effects.*

**63. Number Framing**
The format of numbers (percentages vs. frequencies, large vs. small units) changes their psychological impact.
*Design: "9 out of 10" feels more concrete than "90%." "$1,247 saved" is more tangible than "15% savings." Match number format to desired emotional impact.*

**64. Halo Effect**
Our overall positive impression of something colors how we judge its specific traits.
*Design: Invest in first impressions — a beautiful landing page makes users rate your product's features higher. A strong brand transfers positive perception to everything associated with it.*

**65. Devil Effect**
A single negative attribute unfairly bleeds into other unrelated areas.
*Design: Fix visible problems first — one obvious bug makes users doubt your entire product quality. Remove anything that creates a negative first impression.*

---

## 5. Social Dynamics

**66. Social Proof**
People look to others' behaviour to determine correct action, especially in uncertain situations.
*Design: Show user counts, testimonials, ratings, "popular" tags, and "X people bought this." Real-time activity indicators ("5 people viewing this") amplify urgency.*
📎 Bandura & Menlove (1968). Factors determining vicarious extinction through symbolic modeling. Journal of Personality and Social Psychology.

**67. Authority Principle**
People defer to experts and authoritative sources when making decisions.
*Design: Display credentials, endorsements from recognized experts, certifications, press logos, and awards. Expert recommendations carry outsized weight.*

**68. Bandwagon Effect**
People are more likely to adopt behaviours or beliefs that are already popular.
*Design: Emphasize popularity — "Join 2 million users," "Most popular plan," "Trending." Showing growing adoption encourages more adoption.*

**69. Liking Principle**
People are more easily influenced by people they like — those who are similar, attractive, or who compliment them.
*Design: Use relatable imagery and language. Show testimonials from people similar to your target audience. A friendly, warm tone builds liking.*

**70. Reciprocity**
When someone gives us something, we feel obligated to give something back.
*Design: Offer genuine value first — free tools, valuable content, free trials — before asking for anything in return. Generosity increases conversion.*
📎 Jacob, C., Guéguen, N., & Boulbry, G. (2015). Effect of an unexpected small favor on compliance with a survey request. Journal of Business Research.

**71. Consensus Heuristic**
When uncertain, people assume the majority's choice is correct.
*Design: Label the most chosen option. Show which option "most customers choose." Display aggregate ratings and review counts prominently.*

**72. Informational Social Influence**
In ambiguous situations, people look to others for information about what to do.
*Design: For novel products or unfamiliar flows, show how others have used it. Tutorials, example use cases, and community content reduce uncertainty.*

**73. Normative Social Influence**
People conform to social norms to gain acceptance and avoid rejection.
*Design: Frame desired behaviour as the social norm: "Most people in your area recycle" is more effective than "You should recycle." Descriptive norms drive behaviour.*

**74. Social Comparison**
People evaluate themselves by comparing with others, motivating behaviour change.
*Design: Leaderboards, progress comparisons ("You're in the top 10%"), and peer benchmarks motivate action. Use carefully — negative comparisons can demotivate.*

**75. Herding Behaviour**
People follow the crowd, especially in high-uncertainty situations, sometimes irrationally.
*Design: Real-time indicators of others' behaviour ("12 people signed up in the last hour") create momentum. But ensure this is truthful — fake urgency erodes trust.*

**76. In-Group Bias**
People favour and trust members of their own group over outsiders.
*Design: Signal shared identity with your audience — use language, imagery, and references that resonate with their specific community or profession.*

**77. Social Facilitation**
The presence of others enhances performance on simple/well-learned tasks but hinders complex ones.
*Design: Social features (shared workspaces, live collaboration) work well for routine tasks but may add pressure in complex creative work. Offer privacy options.*

**78. Bystander Effect**
The more people present, the less likely any individual is to help or take action.
*Design: Direct your CTA at the individual, not the group. "You can make a difference" outperforms "We all need to help." Personalize calls to action.*

**79. Scarcity (Social)**
When something is available to only a few, it signals exclusivity and increases desirability.
*Design: Invite-only access, waitlists, member-only features, and limited cohorts create social scarcity. Being "chosen" increases commitment.*

**80. Mere Belonging**
Even trivial social connections to a group increase motivation and persistence.
*Design: Welcome users into a community, even with simple gestures. "You're one of us now" after signup. Display community membership prominently.*

**81. Social Norms Messaging**
Telling people what others actually do (descriptive norms) is more effective than telling them what they should do (injunctive norms).
*Design: "80% of your neighbours reduced energy use" is more powerful than "Reduce your energy use." Show actual behaviour data when possible.*

**82. Competition**
We strive harder when competing against others for limited resources.
*Design: Leaderboards, challenges, and "limited spots" messaging activate competitive drive. Use carefully — competition motivates some personality types but demotivates others.*

**83. Product-Person Bias**
We look for and value human connections in our products.
*Design: Show the humans behind the product — founder stories, team photos, handcrafted touches. "Made by real people" signals authenticity and builds emotional connection.*

---

## 6. Trust & Credibility

**84. Source Credibility**
The perceived expertise and trustworthiness of a source determines how persuasive its message is.
*Design: Display credentials, certifications, and relevant experience. "As featured in..." press sections. Expert testimonials over anonymous reviews.*

**85. Transparency Effect**
Showing how something works (process, ingredients, decision criteria) increases trust.
*Design: Explain your pricing, show your process, reveal the "why" behind recommendations. Transparency signals integrity. Algorithm explanations increase acceptance.*

**86. Mere Exposure Effect (Trust)**
Familiarity breeds trust. Repeated encounters with a brand increase positive sentiment.
*Design: Maintain consistent branding across all touchpoints. Remarketing and brand presence build comfort even before conversion.*
📎 Zajonc (1968). Attitudinal effects of mere exposure. Journal of Personality and Social Psychology.

**87. Risk Reversal**
Removing the customer's risk (money-back guarantees, free returns) increases willingness to act.
*Design: Prominently display guarantees, return policies, and free trial terms near the point of commitment. Risk reversal can be more powerful than discounts.*

**88. Trust Transference**
Trust in one entity can transfer to associated entities.
*Design: Partner logos, "as seen on" media mentions, integration with trusted platforms, and endorsements from trusted figures all transfer trust to your brand.*

**89. Pratfall Effect**
A competent entity that shows a small flaw is perceived as more likeable and trustworthy than one that appears perfect.
*Design: Acknowledging a minor weakness ("We're not the cheapest, but...") can increase overall credibility. Perfect claims feel unbelievable.*

**90. Ambiguity Aversion**
People avoid options where the probability of outcomes is unknown, preferring known risks.
*Design: Be specific about what users will get, how long things take, and what happens next. Vague promises create anxiety. Specificity builds confidence.*

**91. Certainty Effect**
People overweight outcomes that are certain relative to merely probable outcomes.
*Design: "Guaranteed to arrive by Friday" is disproportionately more compelling than "95% chance of Friday delivery." Where possible, offer certainties.*
📎 Kahneman & Tversky (1979). Prospect Theory. Econometrica.

**92. Social Proof (Trust)**
Reviews, ratings, and testimonials from real users serve as trust signals that reduce perceived risk.
*Design: Show reviews prominently — with photos, verified purchase badges, and specific details. Volume of reviews matters (a 4.5 with 10,000 reviews beats a 5.0 with 3).*

**93. Operational Transparency**
Showing people the work being done on their behalf increases perceived value and satisfaction.
*Design: Show search progress animations, "finding the best results for you" indicators, and behind-the-scenes processes. People value what they see effort behind.*

**94. Peak-End Rule (Trust Recovery)**
People judge experiences largely by their peak moment and final moment.
*Design: If something goes wrong, make the recovery experience excellent. A well-handled complaint creates more loyalty than no complaint at all.*
📎 Kahneman, Fredrickson, Schreiber & Redelmeier (1993). When More Pain is Preferred to Less. Psychological Science.

**95. Competence Signalling**
Demonstrating expertise through specificity and detail signals competence.
*Design: Specific claims ("saves 2.3 hours/week") feel more credible than vague ones ("saves time"). Use precise numbers, detailed explanations, and clear evidence.*

**96. Benevolence Signalling**
Showing that you prioritize the user's interests over your own increases trust.
*Design: Honest downsides, "this plan might be too much for you" suggestions, and transparent pricing all signal benevolence. Sometimes recommending less builds more trust.*

---

## 7. Motivation & Engagement

**97. Goal Gradient Effect**
People accelerate effort as they approach a goal — motivation increases with proximity to completion.
*Design: Show progress visually. Starting a progress bar at 20% (by crediting prior actions) increases completion. "You're almost there!" messages leverage this.*
📎 Kivetz, Urminsky & Zheng (2006). The Goal-Gradient Hypothesis Resurrected. Journal of Marketing Research.

**98. Endowed Progress Effect**
Artificial advancement toward a goal increases motivation to complete it.
*Design: Give users a head start — "2 of 5 steps complete" (where the first 2 were automatic) outperforms "0 of 3 steps complete" even though the remaining work is identical.*
📎 Nunes & Dreze (2006). The Endowed Progress Effect: How Artificial Advancement Increases Effort. Journal of Consumer Research.

**99. Zeigarnik Effect**
Incomplete tasks occupy the mind more than completed ones — people are driven to finish what they've started.
*Design: Show incomplete profiles, partially filled forms, and unfinished sequences. "Your profile is 70% complete" creates psychological tension that motivates completion.*
📎 Zeigarnik, B. (1927). On Finished and Unfinished Tasks.

**100. Variable Ratio Reinforcement**
Unpredictable rewards (like slot machines) are the most engaging reinforcement pattern.
*Design: Gamified elements with surprise rewards, random bonuses, and varied content feeds leverage this. The uncertainty of "what's next?" keeps people engaged.*

**101. Self-Determination Theory (Autonomy, Competence, Relatedness)**
Intrinsic motivation requires feeling autonomous (in control), competent (capable), and connected (belonging).
*Design: Offer choices (autonomy), show progress and achievements (competence), and build community features (relatedness).*

**102. Flow State**
People experience optimal engagement when challenge level matches skill level, with clear goals and immediate feedback.
*Design: Gradually increase complexity. Provide clear objectives and instant feedback. Remove distractions during key tasks. Adaptive difficulty keeps users in flow.*

**103. Curiosity Gap**
When people notice a gap between what they know and what they want to know, they're motivated to fill it.
*Design: Tease information without revealing everything. "See how Company X increased conversions by 300%" creates a gap. Effective subject lines and headlines leverage this.*
📎 Loewenstein (1994). The psychology of curiosity. Psychological Bulletin.

**104. Feedback Loops**
Immediate feedback on actions helps people understand consequences and adjust behaviour.
*Design: Show real-time results of user actions. Instant validation in forms, live previews, and progress updates keep users oriented and motivated.*

**105. Intrinsic vs. Extrinsic Motivation**
Intrinsic motivation (doing something because it's inherently rewarding) is more sustainable than extrinsic (rewards/punishments).
*Design: Design for mastery and purpose, not just points and badges. Meaningful progress indicators outperform superficial gamification long-term.*

**106. Overjustification Effect**
External rewards for intrinsically motivated behaviour can decrease intrinsic motivation.
*Design: Be careful adding rewards to activities people already enjoy. Paying users for referrals can undermine genuine advocacy. Use rewards for non-enjoyable tasks.*

**107. Self-Efficacy**
People who believe they can succeed are more likely to try and persist. Success builds confidence for more success.
*Design: Start users with easy wins. Celebrate small achievements. Show similar users who succeeded. "You can do this" messaging increases completion rates.*

**108. Autonomy Bias**
People value having control and choice, even when it doesn't improve outcomes.
*Design: Let users customize, choose, and configure — even when a default would work. The illusion of control increases satisfaction and commitment.*
📎 Leotti, Iyengar & Ochsner (2010). Born to choose: The origins and value of the need for control. Trends in Cognitive Sciences.

**109. Competence Need**
People seek to feel effective and capable in their environment.
*Design: Celebrate user accomplishments. Provide clear skill progression. Avoid making users feel stupid — error messages should be helpful, not blaming.*

**110. Progress Principle**
Making progress on meaningful work is the single biggest driver of positive engagement.
*Design: Make progress visible and frequent. Break big tasks into milestones. Show users how far they've come, not just how far they have to go.*

**111. Fresh Start Effect**
People are more motivated to pursue goals at temporal landmarks (new year, birthday, Monday, new month).
*Design: Time campaigns and prompts around fresh starts. "New week, new goals" and "Start your year right" messages see higher engagement.*
📎 Dai, Milkman & Riis (2014). The Fresh Start Effect: Temporal Landmarks Motivate Aspirational Behavior. Management Science.

**112. Temptation Bundling**
Pairing something people should do with something they want to do increases follow-through.
*Design: Bundle unpleasant tasks with rewards — "Complete your profile to unlock a bonus feature." Make the tedious step a gateway to something enjoyable.*
📎 Milkman, Minson & Volpp (2013). Holding The Hunger Games Hostage at the Gym. Management Science.

**113. Power of Free**
People disproportionately value free items, even when a low-cost alternative is objectively better value.
*Design: "Free shipping over $50" is extremely motivating. Free trials, free tiers, and free gifts with purchase generate disproportionate engagement.*

**114. Tiny Habits**
Small actions anchored to existing routines create lasting change.
*Design: Design onboarding around tiny first actions attached to existing user behaviors. "After you check your email, spend 30 seconds on X" is more effective than "Use X daily."*
📎 Fogg, B.J. (2019). Tiny Habits: The Small Changes That Change Everything.

**115. Aggregation Effect**
Small consistent changes compound into significant results.
*Design: Show users the compound impact of small actions over time. "5 minutes/day = 30 hours/year" makes micro-commitments feel worthwhile.*

---

## 8. Emotion & Affect

**116. Affect Heuristic**
People make judgments based on current emotions rather than objective analysis — feelings override facts.
*Design: Create positive emotional states before asking for commitment. Beautiful design, warm imagery, and positive copy prime better decisions.*

**117. Peak-End Rule**
People judge an experience primarily based on its most intense moment (peak) and its final moment (end).
*Design: Design memorable highlights and strong endings. A delightful confirmation page after purchase matters more than optimizing every middle step.*
📎 Kahneman, Fredrickson, Schreiber & Redelmeier (1993). When More Pain is Preferred to Less. Psychological Science.

**118. Negativity Bias**
Negative experiences are psychologically more powerful than equivalent positive ones — roughly 3:1.
*Design: One bad experience requires approximately three good ones to compensate. Prioritize eliminating pain points over adding delights.*

**119. Positive Emotion and Decision-Making**
Positive emotions broaden attention and thinking, leading to more creative and open decision-making.
*Design: Use warm colours, friendly language, and uplifting imagery to create positive emotional contexts, especially before presenting options.*

**120. Emotional Contagion**
Emotions spread between people (and between content and people) through mimicry and suggestion.
*Design: Happy testimonials, smiling faces, and enthusiastic language create emotional contagion. The emotional tone of your interface affects users' moods.*

**121. Anticipatory Emotion**
The anticipation of an experience often generates as much emotion as the experience itself.
*Design: Build excitement before product launches, deliveries, or experiences. Countdown timers, sneak peeks, and "coming soon" teasers leverage anticipation.*

**122. Aesthetic-Usability Effect**
People perceive aesthetically pleasing designs as easier to use, regardless of actual usability.
*Design: Invest in visual design — it directly affects perceived usability. Beautiful products get more patience from users when things go wrong.*

**123. Catharsis Effect**
Expressing emotions (especially negative ones) provides relief and satisfaction.
*Design: Give users ways to express frustration productively — feedback forms, ratings, complaint channels. Feeling heard reduces churn.*

**124. Surprise and Delight**
Unexpected positive experiences create outsized emotional impact and memorability.
*Design: Add unexpected touches — a funny loading message, a birthday discount, a handwritten note. Small surprises generate disproportionate loyalty.*

**125. Nostalgia Effect**
Nostalgic feelings increase willingness to spend, social connectedness, and positive brand associations.
*Design: Reference shared cultural memories, vintage aesthetics, or "remember when" messaging to create warm emotional connections with your audience.*
📎 Muehling & Sprott (2004). The Power of Reflection: An Empirical Examination of Nostalgia Advertising Effects. Journal of Advertising.

**126. Emotional Granularity**
People who can identify specific emotions (vs. just "good/bad") make better decisions.
*Design: Help users articulate what they feel — mood selectors, specific feedback options, and nuanced rating scales lead to better self-understanding and engagement.*

**127. Hedonic Adaptation**
People quickly return to a baseline happiness level after positive or negative events — novelty wears off.
*Design: Continuously introduce new features, content, and experiences to counter adaptation. What delighted users last month may feel expected this month.*
📎 Lyubomirsky, S. (2011). Hedonic Adaptation to Positive and Negative Experiences. Oxford Handbook of Stress, Health, and Coping.

**128. Segregation Effect**
Positive experiences feel better overall when we spread them out.
*Design: Deliver rewards, upgrades, and positive surprises at intervals rather than all at once. Multiple small wins feel better than one big win.*

**129. Biophilia Effect**
We're drawn to and benefit from natural elements.
*Design: Incorporate nature imagery, organic shapes, green color palettes, and natural textures. Nature elements reduce stress and increase positive perception of digital products.*

---

## 9. Memory & Recall

**130. Primacy and Recency Effects**
People best recall the first and last items in a sequence.
*Design: Front-load key messages and end with a strong CTA or takeaway. Middle content gets forgotten — don't bury important information there.*

**131. Spacing Effect**
Information encountered repeatedly over spaced intervals is remembered better than information crammed into one exposure.
*Design: Multi-touch onboarding (spread over days) beats a single tutorial. Drip campaigns, repeated exposure to key features, and spaced reminders aid retention.*
📎 Cepeda, Pashler, Vul, Wixted & Rohrer (2006). Distributed practice in verbal recall tasks. Review of Educational Psychology.

**132. Testing Effect (Retrieval Practice)**
Actively recalling information strengthens memory more than passive review.
*Design: Interactive quizzes, prompts to recall information, and practice exercises in educational products dramatically improve retention over passive content.*

**133. Picture Superiority Effect**
Images are remembered significantly better than words alone.
*Design: Use imagery to convey key concepts. Icons alongside text, product photos, and visual metaphors all improve recall. Don't rely on text alone for important information.*
📎 Paivio & Csapo (1973). Picture superiority in free recall: Imagery or dual coding? Cognitive Psychology.

**134. Bizarreness Effect**
Unusual or bizarre information is more memorable than common information.
*Design: Memorable brands often use unexpected elements — mascots, unusual colour choices, surprising copy. Convention is forgettable; surprise is memorable.*

**135. Generation Effect**
People remember information better when they actively generate it rather than passively receive it.
*Design: Interactive calculators ("See your savings"), configurators, and personalized result generators create stronger engagement than static content.*

**136. Levels of Processing**
Information processed at a deeper, more meaningful level is remembered better than shallowly processed information.
*Design: Ask users to engage with information meaningfully — apply it, discuss it, connect it to their own experience — rather than just read it.*

**137. State-Dependent Memory**
People recall information better when they're in the same state (physical, emotional) as when they learned it.
*Design: Brand consistency across contexts helps — if users learn about your product on mobile, the desktop experience should feel similar enough to trigger recall.*

**138. Storytelling for Memory**
Narratives create stronger, more connected memories than isolated facts.
*Design: Embed your key messages in stories. A customer journey narrative is more memorable than a bullet list of features.*

**139. Interference Theory**
New information can interfere with the recall of previously learned information.
*Design: Don't overwhelm users with competing messages. A single, clear value proposition is remembered better than five diluted ones.*

**140. Modality Effect**
Information presented through multiple sensory channels (visual + auditory) is remembered better than single-channel.
*Design: Combine text with images, video with captions, audio with visual aids. Multi-modal content improves comprehension and retention.*

**141. Elaborative Encoding**
Connecting new information to existing knowledge creates stronger memories.
*Design: Use analogies, metaphors, and comparisons to familiar concepts. "It's like Uber, but for dog walking" is instantly memorable because it connects to existing knowledge.*

**142. Rhyme As Reason Effect**
Rhyming statements are perceived as more truthful and trustworthy.
*Design: Use rhyme in taglines, slogans, and key messaging for memorability and perceived credibility. "A stitch in time saves nine" feels more true than its non-rhyming equivalent.*
📎 McGlone & Tofighbakhsh (2000). Birds of a feather flock together: Rhyme as reason in aphorisms.

**143. Humor Effect**
We remember funny information better than serious information.
*Design: Strategic humor in error messages, loading states, and empty states increases memorability and positive brand association. Keep humor on-brand and audience-appropriate.*

---

## 10. Loss, Risk & Uncertainty

**144. Loss Aversion**
Losses feel approximately twice as painful as equivalent gains feel pleasurable.
*Design: Frame inaction as a loss ("You're missing out on $500/year in savings") rather than action as a gain. Highlight what users lose by not acting.*
📎 Kahneman & Tversky (1979). Prospect Theory: An analysis of decision under risk. Econometrica.

**145. Endowment Effect**
People value things more once they own them (or feel ownership over them).
*Design: Free trials, customization, and "your" language create ownership. Once users have invested time personalizing something, they're reluctant to give it up.*
📎 Kahneman, Knetsch & Thaler (1990). Experimental Tests of the Endowment Effect. Journal of Political Economy.

**146. Sunk Cost Fallacy**
People continue investing in something because of past investments, even when the future outlook is negative.
*Design: Show accumulated progress, time invested, and content created to increase switching costs. "You've built 47 projects here" reduces churn.*
📎 Arkes & Blumer (1985). The psychology of sunk cost. Organizational Behavior and Human Decision Processes.

**147. Prospect Theory**
People evaluate outcomes as gains and losses relative to a reference point, and are risk-averse for gains but risk-seeking for losses.
*Design: When users are in a "gain" frame (things are going well), offer safe options. When in a "loss" frame (things aren't working), they'll take bigger risks on new solutions.*
📎 Kahneman & Tversky (1979). Prospect Theory: An analysis of decision under risk. Econometrica.

**148. Zero-Risk Bias**
People prefer completely eliminating a small risk over significantly reducing a larger risk.
*Design: "100% money-back guarantee" is more powerful than "95% satisfaction rate." Complete certainty, even on a small aspect, is disproportionately reassuring.*

**149. Omission Bias**
People judge harmful actions as worse than equally harmful inactions — doing nothing feels safer.
*Design: Make inaction feel like an active choice with consequences. "By not upgrading, you're choosing to lose these features" reframes inaction as a decision.*

**150. Regret Aversion**
People avoid choices they think they'll regret, sometimes avoiding decisions altogether.
*Design: Reduce regret risk — offer easy returns, trial periods, and "you can always change this later" messaging. Make decisions feel reversible.*

**151. Ambiguity Effect**
People prefer options with known probabilities over those with unknown probabilities.
*Design: Be specific about outcomes, timelines, and what to expect. "Most users see results in 2 weeks" is better than "You may see results."*

**152. Optimism Bias**
People tend to overestimate the probability of positive events happening to them.
*Design: Users will overestimate their own follow-through on exercise apps, courses, and saving plans. Design for the realistic user, not the optimistic one.*

**153. Pessimism Bias**
In high-stakes situations, people may overestimate risks.
*Design: For high-commitment decisions (surgery, large purchases), provide extensive reassurance, social proof, and risk mitigation to counter exaggerated risk perception.*

**154. Reactance**
When people feel their freedom is threatened, they're motivated to restore it, often by doing the opposite.
*Design: Avoid aggressive push tactics, forced actions, and "you must" language. Give users genuine choice and control. Hard sells trigger resistance.*
📎 Brehm, J.W. (1966). A Theory of Psychological Reactance.

**155. Scarcity (Time Limit & Limited Quantity)**
When something is available for limited time or in limited quantity, it increases perceived value and urgency.
*Design: "Only 3 left" and "Offer ends in 2 hours" create urgency. Show real-time availability. Limited editions and exclusive access windows leverage this.*
📎 Worchel, Lee & Adewole (1975). Effects of supply and demand on ratings of object value. Journal of Personality and Social Psychology.

**156. Choice-Supportive Bias**
We remember our past choices as better than they actually were.
*Design: Reinforce past purchase decisions with "great choice" messaging and reminders of what users gained. Post-purchase reassurance reduces returns and increases loyalty.*

**157. Measurement Paradox**
Measuring behavior can change the behavior being measured.
*Design: Be aware that asking users about satisfaction can change their satisfaction. Tracking metrics that users see (like "streak counts") alters the behavior being tracked — which can be leveraged intentionally.*

**158. Afterlife Effect**
Products gain value when they have a life beyond their owner.
*Design: Highlight resale value, recyclability, or legacy aspects. "Built to last" and "Retains its value" messaging increases willingness to pay a premium.*

---

## 11. Pricing & Value Perception

**159. Anchoring in Pricing**
The first price seen sets the reference point for evaluating all subsequent prices.
*Design: Show the original/highest price first. Strikethrough pricing, "was $199, now $99" works because the anchor is set at $199.*
📎 Tversky & Kahneman (1974). Judgment under Uncertainty: Heuristics and Biases. Science.

**160. Price-Quality Heuristic**
People assume higher prices indicate higher quality, especially when they can't evaluate quality directly.
*Design: Pricing too low can signal low quality. For premium positioning, price higher and justify with quality signals. Cheap prices invite skepticism.*

**161. Charm Pricing**
Prices ending in 9 or 99 are perceived as significantly lower than the next round number.
*Design: $9.99 feels meaningfully cheaper than $10.00. Use charm pricing for value positioning. Round numbers ($10, $100) signal quality and premium positioning.*

**162. Pennies-a-Day Pricing**
Reframing costs in smaller daily amounts reduces perceived expense.
*Design: "$2.49/day" feels much more affordable than "$74.99/month." The smaller the time unit, the smaller the perceived cost.*

**163. Partitioned Pricing**
Separating a total price into components (base + add-ons) can make the total feel lower.
*Design: "$199 + $19 shipping" sometimes feels cheaper than "$218 with free shipping" because people anchor on the $199. But transparency builds trust — test both.*

**164. Bundle Pricing / Bundling**
Grouping items together at a single price makes people less sensitive to individual component costs.
*Design: Bundles obscure individual item evaluation. "Get all three for $99" avoids users rejecting any single item's price.*

**165. Payment Decoupling**
Separating the payment from the consumption reduces the "pain of paying."
*Design: Subscriptions, pre-payment, and stored payment methods decouple the moment of payment from usage, making each use feel "free."*

**166. Pain of Paying**
The psychological discomfort of spending money. Cash hurts more than card; card hurts more than auto-pay.
*Design: Reduce payment friction — saved payment methods, one-click purchase, subscriptions. Every additional payment step reactivates the pain.*

**167. Relative Value Perception**
People evaluate prices relative to context, not in absolute terms.
*Design: A $5 coffee seems reasonable at an airport but expensive at a gas station. Position your pricing in a context that makes it feel fair.*

**168. Fairness Heuristic**
People reject offers they perceive as unfair, even when accepting would benefit them.
*Design: Explain price differences. Dynamic pricing without explanation feels exploitative. Show why premium tiers cost more. Fairness drives acceptance.*

**169. Free Effect / Zero Price Effect**
People irrationally overvalue free offers. "Free" triggers an emotional response that distorts rational calculation.
*Design: Free shipping, free trial, buy-one-get-one-free, and free tier all leverage this. Adding "free" to any aspect of an offer disproportionately increases its appeal.*
📎 Shampanier, Mazar & Ariely (2007). Zero as a Special Price: The True Value of Free Products. Marketing Science.

**170. Mental Accounting**
People categorize money into different "accounts" (entertainment, savings, food) and treat them differently.
*Design: Position your product within a mental account where the user is more willing to spend. A $50 productivity tool framed as "business expense" feels different from "personal expense."*

**171. Refund Effect**
Consumers spend refunded money differently than earned money — more freely and on indulgent items.
*Design: Frame credits, refunds, and bonus money as "found money" to encourage spending. Gift cards and store credit leverage this principle.*
📎 Hershfield et al. (2021).

---

## 12. Identity & Self-Concept

**172. Self-Image Congruence**
People prefer products and brands that match how they see themselves (or want to be seen).
*Design: Understand your audience's aspirational identity. Show users who represent who your audience wants to be, not just who they currently are.*

**173. Identity-Based Motivation**
People act in ways consistent with their identity. "I am a runner" motivates more than "I should run."
*Design: Help users adopt identity labels — "You're a creator," "Welcome to the Pro community." Identity shifts drive sustained behaviour change.*

**174. Self-Serving Bias**
People attribute successes to themselves and failures to external factors.
*Design: Let users take credit for wins ("Look what you built!") but absorb blame for failures ("We need to improve this feature"). Protect user self-esteem.*

**175. Cognitive Dissonance**
People experience discomfort when their actions conflict with their beliefs and are motivated to resolve the tension.
*Design: After a purchase or commitment, reinforce the user's decision with confirmation messaging. "Great choice!" and success stories reduce post-decision anxiety.*

**176. Social Identity Theory**
People derive self-esteem from group membership and favour in-group members.
*Design: Create meaningful user tiers, communities, and groups. "Pro member" and "Early adopter" labels create identity and loyalty. Exclusive communities increase engagement.*

**177. Self-Signalling**
People take actions partly to signal things to themselves about who they are.
*Design: Premium, sustainable, or charitable purchasing lets users tell themselves they're successful, responsible, or generous. Enable identity-affirming choices.*

**178. Labelling Effect**
Assigning a positive label to someone increases the likelihood they'll behave consistently with that label.
*Design: Telling users "You're one of our most engaged members" increases engagement. Positive labels become self-fulfilling prophecies.*

**179. Consistency Principle (Identity)**
People strive to be consistent with their past statements, actions, and self-image.
*Design: Once users publicly identify with your brand or product, they'll work to maintain consistency. Encourage public commitments, reviews, and sharing.*

**180. Above-Average Effect**
Most people believe they are above average in positive qualities.
*Design: Features that let users compare favourably ("You read more than 80% of users") satisfy this bias. Be cautious with comparisons that make users feel below average.*

**181. Aspirational Identity**
People are motivated by who they want to become, not just who they are now.
*Design: Show the transformation. "Before and after" narratives. Future-self visualizations. Frame your product as a tool for becoming the person the user aspires to be.*

**182. IKEA Effect**
People place disproportionately high value on things they helped create.
*Design: Let users build, customize, and co-create. Products with user investment (playlists, configurations, designs) feel more valuable and are harder to abandon.*
📎 Norton, Mochon & Ariely (2012). The IKEA effect: When labor leads to love. Journal of Consumer Psychology.

---

## 13. Cross-Cutting Principles

These appear across multiple categories and are particularly powerful:

**183. Reciprocity Cascade**
Each act of giving creates obligation that can compound through a relationship.
*Design: Multiple small gifts (free content, tools, advice) over time create stronger reciprocity than one large gift.*

**184. Commitment Escalation**
Small commitments lead to larger ones in a predictable ladder.
*Design: Map your engagement ladder — visit → signup → profile → first use → paid → advocate. Each step should feel like a natural next commitment.*

**185. Paradox of Specificity**
Highly specific claims are more believable than general ones, even when unverifiable.
*Design: "Saves 2.4 hours per week" is more credible than "Saves hours." "Based on a study of 1,847 users" beats "Based on user studies."*

**186. Completion Bias**
People are motivated to complete sets, sequences, and collections.
*Design: Badge collections, feature checklists, and "complete your profile" prompts leverage the innate desire to finish what was started.*

**187. The Labour Illusion**
People value outcomes more when they can see evidence of effort behind them.
*Design: Show the work — "We compared 147 hotels to find your top 3." Loading animations that describe the process increase perceived value of results.*

**188. Noble Edge Effect**
Companies that demonstrate genuine social responsibility are perceived more positively, but only when the effort is authentic.
*Design: Highlight genuine charitable or environmental efforts. But inauthentic "purpose-washing" backfires. Authenticity is critical.*

**189. Paradox of Authority**
Showing vulnerability alongside expertise can increase trust and influence.
*Design: Experts who admit uncertainty ("This is our best understanding, but research is ongoing") can be more trusted than those who claim absolute certainty.*

**190. Dynamic Norms**
We adjust our behavior based on the observed behavior of people around us in dynamic, real-time situations.
*Design: Show real-time activity ("5 people booking this flight right now") and dynamic updates to social proof. Live leaderboards and active user counts leverage this principle.*
