# Thinking Models

> A mental-model skill that decides whether a question deserves depth: a direct answer for simple ones, models plus a counterargument pass and verifiable next steps when the stakes are real.

[简体中文](README.md) | **English**

![License](https://img.shields.io/badge/license-MIT-green) ![Models](https://img.shields.io/badge/models-77-blue) ![Biases](https://img.shields.io/badge/biases-39-orange) ![Platform](https://img.shields.io/badge/platform-Claude%20Code%20%7C%20Qoder%20%7C%20Cursor%20%7C%20Codex%20%7C%20Cline-purple)

**Version**: v1.3.1 | **Updated**: 2026-10-29 | **License**: MIT

## What is this

A mental-model skill that adjusts how much analysis it applies to the stakes of the question. 77 models and 39 cognitive biases, but it usually picks just 1-3 of them.

**It is NOT**: a tool that runs every question through a model checklist.
**It IS**: depth grading first. Simple questions get a normal answer; decisions with consequences get models, a counterargument pass, and verifiable actions. It gives a direct recommendation by default; Socratic questioning is enabled only when you explicitly ask for it.

The guardrails are in the repo, not in slogans: every model entry lives in one `tools/models.json`, and the six domain files plus the source list are generated from it. Six checks (numbering, broken links, counts, version, emoji, file coverage) must pass before anything ships, and prompt edits have to clear a 10-case behavioral regression suite against real models. Three candidate edits were measured and none beat the current wording, so the prompt stayed as it was; that is recorded in the CHANGELOG too.

## Who needs this

| You are | What you face | What this skill does for you |
|---|---|---|
| **Everyday user** | Job changes, buying a home, kids' education, family conversations: life's high-stakes decisions with no one to consult | Breaks dilemmas into "conclusion → key analysis → actions → risk"; no more wishy-washy AI answers. Say "guide me" to switch into Socratic questioning |
| **Tech / business professional** | Business judgment, competitive strategy, negotiation pricing, resource allocation: costly when wrong | 77 models matched to scenarios (game theory / moats / antifragility / expected value...); L2 picks 1-3 and L3 picks 2-5 for cross-checking, every conclusion passes a counterargument review |
| **AI creator / developer** | You want your agent to have a "deep-thinking layer" that goes beyond parroting search results | Out-of-the-box graded intervention protocol + cross-platform formats (SKILL.md / AGENTS.md / .cursorrules); also a reference architecture for building your own reasoning skills |

## Before vs. after

| Dimension | Ordinary AI chat | With thinking-models |
|---|---|---|
| "Should I switch careers?" | "Consider the pros and cons": correct nonsense | Names the real question + a counter-intuitive insight + an action list with verification steps and timelines |
| Depth calibration | Rambling or too brief, regardless of stakes | L0-L3 graded intervention: no overkill on small things, no laziness on big ones |
| Blind spots | Follows your premises. You say it, it agrees | Adversarial review: red-teams its own conclusion before answering |
| Biases | Can't see you're sunk in "sunk cost" or "survivorship bias" | Built-in Top 12 bias quick scan surfaces the most common traps |
| Long term | Ask, forget, never improve | L3 or explicit requests write a decision log for a 30-day outcome review |

## Sister skill: bias-correction

This skill pairs with [bias-correction](https://github.com/Hoodas101/bias-correction) (cognitive bias correction system) as a complementary set:

| | thinking-models (this skill) | bias-correction |
|---|---|---|
| Positioning | **How to decide better**: analysis toolbox | **Where reasoning goes wrong**: error guardrail |
| Content | 77 mental models + scenario matching table | 39 biases + dual-channel trigger detection |
| Trigger | Grades depth first; full protocol only for L2-L3 | Bias-signal driven, not active by default |

The two share interoperable numbering (e.g., Sunk Cost = TM#1 = BC#29) and compatible protocols. **Installing both is recommended**, but each works standalone: with only this skill installed, bias checks fall back to the built-in `BIAS-CORRECTION.md` quick-reference card (Top 12); with bias-correction installed, call its full 39-bias analysis on demand instead of expanding two frameworks at once.

## Core capabilities

- **77 mental models**: from Sunk Cost to Antifragility, across 6 domains: strategy / decision-making / systems / interpersonal / growth / advanced decision procedures
- **Top 12 bias quick scan**: built in; the full 39-bias catalog lives in the sister skill [bias-correction](https://github.com/Hoodas101/bias-correction) and loads on demand
- **Graded intervention**: L0/L1 answered directly; only L2-L3 activate the full internal protocol. No overkill on simple questions
- **Direct recommendation by default**: Socratic questioning only when you explicitly say "guide me / help me think it through"; no questionnaire instead of an answer
- **First principles**: decompose to indivisible facts, separating real constraints from convention
- **Counterargument check**: before output, ask "what's the strongest opposing case, and what evidence would change my mind?" instead of only seeking support
- **Restrained model count**: 1-3 models at L2, 2-5 at L3, never more than 5; every model must add unique information
- **Decision tracking**: writes a decision log at L3 or on explicit request, for a 30-day outcome review
- **Safety guardrails**: recommends professional help for high-stakes scenarios (mental health / legal / medical / major financial); Eastern cultural contexts are not misdiagnosed as biases
- **Exit mechanism**: say "just answer" and it obeys. No forced intervention

## How it compares

| Approach | Setup cost | Context cost | Coverage | Sustainability |
|---|---|---|---|---|
| Asking ChatGPT / Claude directly | Zero | Zero | Depends on how you ask | Nothing retained |
| Writing your own system prompt | High (research the methodology yourself) | **Full cost every turn** (prompt is always resident) | Only what you thought to write | Maintenance burden on you |
| Reading books on mental models | Medium (tens of hours) | Zero | Comprehensive, but no "match to the actual question" mechanism | Relies on willpower, rarely used |
| **This skill** | 5 minutes | Entry loaded only when triggered (~2.9K tokens); extensions load on demand | 77 models + Top 12 bias quick scan, matched to scenarios | Active on deep questions + optional decision-log review |

## What actually changes

No invented metrics, just mechanisms, each verifiable in a single conversation:

- **Decision quality**: every deep analysis passes three gates (first-principles decomposition → model matching → adversarial review) and surfaces at least one counter-intuitive insight
- **Blind spots exposed**: built-in Top 12 bias quick scan catches traps like "sunk cost" and "survivorship bias"; use bias-correction for the full 39-bias catalog
- **A feedback loop**: at L3 or on explicit request, the decision log can be reconciled against real outcomes 30 days later
- **Time saved**: graded intervention keeps simple questions undisturbed; deep thinking is spent only where it's worth it

## Installation

**One command (macOS / Linux, recommended)**

```bash
curl -fsSL https://raw.githubusercontent.com/Hoodas101/thinking-models/main/install.sh | bash
```

Claude Code is the default target. To install into Qoder:

```bash
curl -fsSL https://raw.githubusercontent.com/Hoodas101/thinking-models/main/install.sh | bash -s -- --qoder
```

Restart your agent (Claude Code / Qoder, etc.), then try: "Help me think through whether I should change jobs".

<details>
<summary>No curl? Windows / Cursor / Codex / manual install → expand</summary>

### Claude Code (macOS / Linux, manual)

```bash
# 1. Clone the repo
git clone https://github.com/Hoodas101/thinking-models.git ~/.cc-switch/skills/thinking-models

# 2. Create a symlink to mount
ln -s ~/.cc-switch/skills/thinking-models ~/.claude/skills/thinking-models

# 3. Restart Claude Code
```

### Claude Code (Windows)

```powershell
# 1. Clone the repo
git clone https://github.com/Hoodas101/thinking-models.git %USERPROFILE%\.cc-switch\skills\thinking-models

# 2. Create a symlink (PowerShell as Administrator)
cmd /c mklink /D %USERPROFILE%\.claude\skills\thinking-models %USERPROFILE%\.cc-switch\skills\thinking-models

# 3. Restart Claude Code
```

### Qoder (macOS / Linux / Windows)

```bash
# Clone directly into Qoder's skills directory
git clone https://github.com/Hoodas101/thinking-models.git ~/.qoder/skills/thinking-models
# Restart Qoder
```

### Cursor

```bash
# Copy .cursorrules to your project root
cp ~/.cc-switch/skills/thinking-models/.cursorrules /path/to/your/project/.cursorrules
```

### Codex / Cline / Continue

```bash
# Copy AGENTS.md to your project root
cp ~/.cc-switch/skills/thinking-models/AGENTS.md /path/to/your/project/AGENTS.md
```

### Manual installation (without git)

1. Download and unzip this repo
2. Put the unzipped `thinking-models` folder anywhere (e.g. `~/.cc-switch/skills/`)
3. Create a symlink pointing to it (see the commands above)

</details>

## File structure

```
thinking-models/
├── SKILL.md            ← Entry file (~2.9K tokens), handles most scenarios
├── BIAS-CORRECTION.md  ← Extension: Top 12 bias quick-reference card (full 39 in bias-correction skill)
├── REFERENCE.md        ← Reference: decision trees / anti-abuse / usage guide / scenario entries
├── models/             ← Extension: models #11-77 in 6 domain files; SOURCES.md lists verifiable sources
├── AGENTS.md           ← Cross-platform format (Codex/Cline/Continue)
├── .cursorrules        ← Cursor format
├── tools/              ← Build: models.json (single source) + gen.py (generate) + check.py (validate)
│                         Regression: cases.json (cases + gates) + regress.py (runs models)
├── install.sh          ← One-line install script
├── docs/               ← Donation QR images (copied on install, ~400 KB)
├── CHANGELOG.md        ← Version changes and measured A/B data
├── CONTRIBUTING.md     ← Contribution flow and the checks to run
├── LICENSE
├── README.md           ← Chinese version (default)
└── README.en.md        ← This file
```

## How it works

```
Question received → depth grading
    ├─ L0 Simple (standard answer / pure fact)     → normal reply + at most 1 bonus line, no template headings
    ├─ L1 Medium (comparison / causation / light)  → conclusion + 2-4 reasons + 1 insight, still no template headings
    └─ L2-L3 Deep (dilemma / systemic / stakes)    → internal protocol: facts & constraints → model selection
                                                     → counterargument check → output check
                                                     → decision log only at L3 / on explicit request
```

## Output examples

### L0 Simple question

**Q**: "What's the latest Python version?"

**A**: Python 3.12.4 (released June 2024).

> Worth noting: 3.12 brought major typing changes — cleaner `TypeVar` syntax, and the `@override` decorator entered the standard library.

### L1 Medium question

**Q**: "Why is React more popular than Vue?"

**A**: Three main reasons: ecosystem first-mover advantage, a positive feedback loop in the job market, and JSX's learning curve paradoxically acting as a moat.

> One bias to flag: "popular = better" is the availability heuristic. Vue's actual usage among SMEs is high — its share of voice is just lower. Popularity reflects ecosystem size, not technical merit.

### L2-L3 Deep question (everyday life)

**Q**: "My kid hit the rebellious phase and won't listen to anything. What do I do?"

**A**:

I understand how exhausting this is — let's clear our heads and take it step by step.

**Conclusion**: What you're facing isn't a "disobedient kid" but a normal developmental stage of autonomy awakening. The way through isn't tighter control but bounded choices.

**Key analysis**: Most parents respond with "more control," which reinforces the rebellion — the child isn't resisting the rules themselves but the feeling of being controlled. Counter-intuitive insight: what a rebellious kid needs most isn't better rules, but room to decide inside a framework. When you turn "you must do A" into "A or B, you pick," the need for autonomy is satisfied and the pushback fades.

**Actions**:
1. **Offer bounded choices** — turn "you must do A" into "A or B, you pick" — verify by counting how many conflicts end in a choice rather than a standoff — start today
2. **Separate bottom lines from flexibility** — safety and ethics are non-negotiable; everything else gets space — if you find yourself negotiating the bottom line, the framework is too loose — map this week
3. **Record positive behavior** — note 1 thing your kid did well each day; reinforce, don't criticize — if two weeks pass with nothing recorded, the bar is too high — for 2 weeks

**Risk / counterargument**: The worst outcome isn't "the phase drags on" — it's "the kid learns to lie to escape control": obedient on the surface, distant underneath.

**Confidence**: Medium — this reads the behavior as autonomy-seeking, which fits most cases; if there are sudden changes in sleep, friends, or school performance, treat those as separate signals rather than teenage mood.

### L2-L3 Deep question (with vs. without the skill)

**Q**: "Should I stay in the big city?"

**A typical AI answer**:

> It depends on your career development, cost of living, and personal preferences. Big cities have more opportunities but more pressure; small towns are comfortable but offer fewer opportunities. Consider everything and decide for yourself.

**Thinking-models-enhanced answer**:

**Conclusion**: You asked "should I stay," but the real question is "what kind of life do you want." Decide by comparing three-year trajectories, not by which city sounds better.

**Key analysis**: Staying in a big city isn't a good/bad binary — it's a trade-off between different life paths. Counter-intuitive insight: most people decide on "more opportunities = stay," ignoring diminishing marginal utility — "more opportunities" means different things in year 3 versus year 10. The real question: in which environment is your sweet spot (passion × skill × demand) easier to realize?

**Actions**:
1. **List your core needs** — career growth / family time / housing / social life, which ranks first? — verify by asking whether your current city serves the top one — 1 day
2. **Compute the 3-year delta** — big city vs. hometown in 3 years: net worth / position / quality of life — if the gap is small, the decision is reversible and speed matters less — 1 week
3. **Run a trial** — take a week off, live in your hometown, feel the real difference — if a week feels like a vacation rather than a life, you've learned something — 1 month

**Risk / counterargument**: The worst outcome isn't "choosing wrong" — it's "never choosing": five years later, rooted in neither place, empty-handed in both.

**Confidence**: Medium — the framing is sound, but the answer depends on facts only you have (family obligations, savings, career ceiling); treat the three-year delta as the deciding evidence, not the vibe of a visit.

### Explicitly requested guiding mode (Socratic)

**Q**: "Should I move from engineer to manager?" (user says: help me think this through)

**A**:

I understand this is a hard decision — let's clear our heads and take it step by step.

Before answering, let me ask a few questions:

**What's your real motivation for moving to management?**
- Because "I've hit my technical ceiling"?
- Because "I enjoy leading people and watching them grow"?
- Because "management seems more senior / better paid"?

These three motivations lead to completely different five-year outcomes.

**Have you considered that your current "technical skill" is a kind of hard currency?**
- Universally accepted — you can make a living with it in any company, any city.
- But management skill is "organizational currency" — leave this company, and it may lose value.

**Another angle — this isn't a binary choice**
- Could you do "80% technical + 20% leading people"?
- Try it for 3 months and see whether you actually enjoy the fulfillment of "getting work done through others".

Sit with these questions, then tell me your first reaction.

## Evidence honesty: we don't pretend all 77 models have experimental backing

The biggest disease of "mental model" content is selling Munger anecdotes and Kahneman RCTs as one undifferentiated pile. All 67 extension models (#11-77) carry an explicit evidence label (the 10 first-layer models are omitted as near-axioms). The distribution:

<!-- AUTO:evidence_en -->
| Grade | Count | Meaning | How to use it |
|---|---|---|---|
| 1 Academic consensus | 28 | Textbook-level findings in cognitive science / behavioral economics | Safe as grounds for a correction |
| 2 Empirically supported | 10 | Backed by specific studies (e.g. Flywheel traces to Collins' comparative research) | Primary reference; check that the study's context matches yours |
| 3 Practitioner heuristic | 21 | From Munger / Taleb-style experience, no systematic experiments | Use as a mirror for questions, not an authority for answers |
| 4 Borrowed metaphor | 6 | Concepts imported from physics/chemistry/biology (Black Swan, dissipative structures, Le Chatelier) | **Caution**: a metaphor is an analogy, not a proof; cross-domain transfer is where errors concentrate |
| 5 Controversial | 2 | Real academic disagreement (Peter Principle, Broken Windows) | Entry point for thinking only, never the basis of a decision |
<!-- /AUTO:evidence_en -->

Three corollaries, and the reason we publish this table:

1. **The more "profound" a model sounds, the thinner its evidence.** Black Swan, dissipative structures, emergence: the most pleasurable to read are exactly the ones that collapse under "does this analogy hold in your case?"
2. **Controversial models stay, but get flagged.** The Peter Principle and Broken Windows have genuine insight and genuine empirical pushback; labeling beats hiding.
3. **The skill's own protocol obeys this standard.** The internal protocol's counterargument check requires every conclusion to carry a confidence label (high/med/low). A tool against fake certainty can't fake its own.

> Per-model labels live in `models/`. The sister skill bias-correction has a stronger base: 37 academic consensus + 2 experience-based out of 39 biases; bias research is an experiment-dense field.

## Design decisions: answers to "why isn't it more elaborate?"

| What might feel "not enough" | Why it's built this way |
|---|---|
| Simple questions get one sentence, no full analysis | Graded intervention is the core design. Running the full internal protocol on an L0 fact question is hammer-nail thinking. A tool's first virtue is knowing when **not** to fire |
| Model selection is hidden from the output (conclusions only) | Printing "I applied #4 Antifragile + #23 Second-order thinking" performs analysis at you instead of doing it for you. Reasoning internalized, conclusions external |
| Socratic mode asks questions instead of concluding — only when you ask for it | Core finding of decision science: people don't execute decisions they were talked into; they execute decisions they talked themselves into. But an answer you didn't ask to be questioned about is just friction, so the default is a direct recommendation |
| No visual cards, no "fit score /10" | Such decoration swaps "looks professional" for "is useful", and invites you to audit the formatting, not the conclusions |
| High-stakes scenarios get "see a professional first" | Depression, litigation, medication are not "cognitive bias" problems. A thinking tool that absorbs professional territory is overstepping |
| Eastern contexts (deferring to parents, saving face) are not force-corrected | Diagnosing them as bandwagon/halo bias silently assumes an individualist reference frame. The cultural-adaptation layer isn't political correctness; it prevents systematic misdiagnosis |

## Limitations: what this skill does NOT do

- **It can't fetch facts for you.** No matter how well models match, garbage premises produce garbage conclusions; the first-principles step can only decompose down to the facts you provide.
- **Its self-review has no external verifier.** The internal protocol forces a counterargument pass, but "AI grading itself" is inherently limited. That's why the decision log exists: the final judge is your real outcome 30 days later, not the analysis.
- **Depth grading can misfire.** Small-looking questions (where to eat) and big-looking ones (should I do a master's) can both be classified wrong. Say "keep it short" or "analyze in depth" to override at any time.
- **It is not emotional support.** When anxiety/depression signals are detected it refers out to professionals. It genuinely shouldn't improvise in that territory, and that has nothing to do with liability.
- **Execution quality depends on the host model.** Weak models complete the protocol less faithfully, though the honest-declaration step still applies (it won't fake completion).

## 5-minute self-test: don't trust the pitch, run these three

Install it, then enter each of these four lines. Each maps to one core promise:

| You enter | What it tests | Pass criterion |
|---|---|---|
| "What's the difference between Python 3.12 and 3.11" | Graded intervention (no overkill on L0) | Normal answer, **no** conclusion → analysis → actions template, at most 1 bonus line |
| "I've spent two years on this project with no traction, but one more half-year should work, right?" | Bias detection + counterargument check | Names sunk cost, poses the "would you choose it today for the first time" test instead of encouraging persistence |
| "Help me think through moving to management" (phrased as "help me think it through") | Explicit Socratic mode | You receive questions (motivation / constraints / trial), not a decision made for you |
| "We plan to ship this feature in 6 weeks — realistic?" | Reference-class forecasting (#67) | Asks for the historical distribution of similar projects first, then explains why this one is faster/slower and gives a range, not a single point |

If all four pass, it deserves this page. If not, open an issue. That matters more than anything written here.

## FAQ

**Q: Running every question through models, isn't that noisy?**
No. L0/L1 don't start the protocol or show the framework; only L2-L3 (stakes / dilemma / systemic) expand. That's exactly what graded intervention is for.

**Q: How is this different from just telling the AI "analyze this with mental models"?**
Three things: ① depth is graded for you, so a simple question doesn't get a wall of analysis and a real decision doesn't get a shrug; ② the internal protocol is enforced — facts and constraints, model selection, then a counterargument pass; freely-prompted AI tends to perform analysis rather than red-team it; ③ deep decisions can be logged for a 30-day outcome check, turning one-off chats into calibration data.

**Q: Isn't 77 models bloat that degenerates into cargo-culting?**
The protocol is strict "quality over quantity": L2 uses 1-3 models, every model must add unique information gain, and repeating a perspective counts as a violation. The library is an armory, not a salvo you fire every time.

**Q: Can I install thinking-models and bias-correction together? Conflicts?**
Recommended pair, no conflict. TM owns "how to decide better" (active grading), BC owns "where reasoning goes wrong" (signal-driven). Interoperable numbering (Sunk Cost = TM#1 = BC#29) and compatible protocols. Each also stands alone: TM ships a Top 12 bias quick-reference card as fallback, and calls BC's full 39-bias analysis only on demand.

**Q: Beyond Claude Code?**
Qoder uses the same `~/.qoder/skills` layout (or run the installer with `--qoder`). For Cursor copy `.cursorrules`, for Codex/Cline/Continue copy `AGENTS.md` — same protocol, adapted format.

**Q: Paid? Will the library grow?**
MIT, free. Growth goes through the CHANGELOG, and the evidence-labeling rule won't change: a new model gets labeled or doesn't get in.

## Use cases

###  Great fit
- Career decisions (job change / career switch / starting a business)
- Interpersonal communication (parenting / partner / colleagues)
- Spending decisions (house / insurance / big purchases)
- Self-growth (what to learn / how to improve)
- Business analysis (competitive strategy / resource allocation / growth)
- Everyday dilemmas (what to eat / where to go / which to pick)

###  Consult a professional first
- Mental health (depression / anxiety / self-harm)
- Legal disputes (divorce / contracts / litigation)
- Medical decisions (treatment plans / medication)

###  Not for
- Pure fact lookups (weather / dates / definitions)
- Code errors / debugging
- Creative entertainment (stories / jokes)

## Tips

| You say | AI behavior |
|---|---|
| "Keep it short" / "one sentence" | Direct conclusion + at most 1 key insight |
| "Help me think it through" / "guide me" | Socratic questions, no decision made for you |
| "Analyze in depth" / "as detailed as possible" | Conclusion → key analysis → actions → risk / confidence |
| "No analysis / just answer" | Exit mechanism kicks in, normal reply |

## Methodology sources

The mental models and cognitive biases in this skill are curated from:
- Daniel Kahneman, *Thinking, Fast and Slow*
- Charlie Munger, *Poor Charlie's Almanack*
- Nassim Taleb, *Antifragile* and *The Black Swan*
- Chip & Dan Heath, *Decisive*
- Richard Thaler, *Nudge*
- Plus the academic consensus of behavioral economics and cognitive psychology

## A note for users

This skill doesn't think for you, it helps you **discover what you already know but haven't noticed**.

Most of the time, the answer is already in your head; I just help you dig it out.

## Share

If you find this skill useful, here's how you might recommend it to a friend:

> I installed a "thinking coach" skill for my agent. It gives a straight recommendation, then pressure-tests it and tells me what it's least sure about. Check it out: github.com/Hoodas101/thinking-models

## Changelog

See [CHANGELOG.md](CHANGELOG.md)

## Support this project

This skill is free and open source (MIT). If it helped you avoid a bad decision or finally think through something you'd been wrestling with, consider buying the author a coffee.

<p align="center">
  <img src="docs/donate-wechat.png" alt="WeChat Pay" width="220">&nbsp;&nbsp;
  <img src="docs/donate-alipay.jpg" alt="Alipay" width="220">
</p>

- **Overseas / GitHub Sponsors**: [github.com/sponsors/Hoodas101](https://github.com/sponsors/Hoodas101) (credit cards supported)
- Or drop a Star, which helps others find this and matters just as much for an open-source project

**Elsewhere in the world?** These QR codes need a WeChat or Alipay account with a mainland
bank card, so they won't work for everyone. Overseas readers can use the **GitHub Sponsors**
link above. A star or a bug report helps just as much.
## License

MIT
