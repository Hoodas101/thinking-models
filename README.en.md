# Thinking Models

> AI that doesn't just give answers — it helps you avoid thinking traps, surface hidden assumptions, and make clearer decisions.

[简体中文](README.md) | **English**

![License](https://img.shields.io/badge/license-MIT-green) ![Models](https://img.shields.io/badge/models-66-blue) ![Biases](https://img.shields.io/badge/biases-39-orange) ![Platform](https://img.shields.io/badge/platform-Claude%20Code%20%7C%20Cursor%20%7C%20Codex%20%7C%20Cline-purple)

**Version**: v1.0.3 | **Updated**: 2026-09-09 | **License**: MIT

## What is this

A skill that makes AI automatically apply mental models and cognitive bias checks to every question it answers.

**It is NOT**: a tool that only triggers when you say "analyze".
**It IS**: every question passes through a thinking framework first, which then decides the response depth — a one-line nudge for simple questions, full analysis for deep ones.

## Who needs this

| You are | What you face | What this skill does for you |
|---|---|---|
| **Everyday user** | Job changes, buying a home, kids' education, family conversations — life's high-stakes decisions with no one to consult | Breaks dilemmas into "essence → analysis → actions → risk"; no more wishy-washy AI answers. Socratic questioning helps YOU think it through, instead of deciding for you |
| **Tech / business professional** | Business judgment, competitive strategy, negotiation pricing, resource allocation — costly when wrong | 66 models matched precisely to scenarios (game theory / moats / antifragility / expected value...), multi-model cross-validation on deep questions, adversarial review on every conclusion |
| **AI creator / developer** | You want your agent to have a "deep-thinking layer" instead of parroting search results | Out-of-the-box graded intervention protocol + tri-mode output + cross-platform formats (SKILL.md / AGENTS.md / .cursorrules); also a reference architecture for building your own reasoning skills |

## Before vs. after

| Dimension | Ordinary AI chat | With thinking-models |
|---|---|---|
| "Should I switch careers?" | "Consider the pros and cons" — correct nonsense | Names the real question + a counter-intuitive insight + an action list with verification steps and timelines |
| Depth calibration | Rambling or too brief, regardless of stakes | L0-L3 graded intervention: no overkill on small things, no laziness on big ones |
| Blind spots | Follows your premises — you say it, it agrees | Adversarial review: red-teams its own conclusion before answering |
| Biases | Can't see you're sunk in "sunk cost" or "survivorship bias" | 39 biases automatically checked against your reasoning chain |
| Long term | Ask, forget, never improve | Deep decisions logged automatically, 30-day review reminder |

## Sister skill: bias-correction

This skill pairs with [bias-correction](https://github.com/Mihooni/bias-correction) (cognitive bias correction system) as a complementary set:

| | thinking-models (this skill) | bias-correction |
|---|---|---|
| Positioning | **How to decide better** — analysis toolbox | **Where reasoning goes wrong** — error guardrail |
| Content | 66 mental models + scenario matching table | 39 biases + dual-channel trigger detection |
| Trigger | Automatically grades every question | Bias-signal driven, not active by default |

The two share interoperable numbering (e.g., Sunk Cost = TM#1 = BC#29) and compatible protocols. **Installing both is recommended**, but each works standalone: with only this skill installed, bias checks fall back to the built-in `BIAS-CORRECTION.md` quick-reference cards (39 biases); with bias-correction installed, they link automatically and call its full version when deep bias analysis is needed.

## Core capabilities

- **66 mental models**: from Sunk Cost to Antifragility, across 5 domains — strategy / decision-making / systems / interpersonal / growth
- **39 cognitive biases**: from Confirmation Bias to Overfitting, automatically checking reasoning chains (full bias correction in the sister skill [bias-correction](https://github.com/Mihooni/bias-correction))
- **Graded intervention**: three levels (L0/L1/L2-L3) auto-adjusted — no overkill on simple questions, full six-step protocol on deep ones
- **Tri-mode output**: concise / guiding (Socratic questioning) / deep analysis, adapting to question complexity and user preference
- **First principles**: applied to every question, broken down to indivisible facts
- **Tacit knowledge**: activates experience-based intuition, not just logical deduction
- **Adversarial review**: red-teams its own conclusions before output — strongest opponent / stress test / cost asymmetry
- **Dynamic model count**: 1-7 models based on complexity — quality over quantity; every model must add unique information gain
- **Decision tracking**: generates a decision log after deep analysis, with a 30-day review reminder
- **Safety guardrails**: recommends professional help for high-stakes scenarios (mental health / legal / medical / major financial); Eastern cultural contexts are not misdiagnosed as biases
- **Exit mechanism**: say "just answer" and it obeys — no forced intervention

## How it compares

| Approach | Setup cost | Coverage | Sustainability |
|---|---|---|---|
| Asking ChatGPT / Claude directly | Zero | Depends on how you ask | Nothing retained |
| Writing your own system prompt | High (research the methodology yourself) | Only what you thought to write | Maintenance burden on you |
| Reading books on mental models | Medium (tens of hours) | Comprehensive, but no "match to the actual question" mechanism | Relies on willpower, rarely used |
| **This skill** | 5 minutes | 66 models + 39 biases, auto-matched to scenarios | Active in every conversation + decision-log feedback loop |

## What actually changes

No invented metrics — just mechanisms, each verifiable in a single conversation:

- **Decision quality**: every deep analysis passes three gates — first-principles decomposition → model matching → adversarial review — and surfaces at least one counter-intuitive insight
- **Blind spots exposed**: 39 biases checked automatically; catches traps like "sunk cost" and "survivorship bias" that are nearly impossible to see on your own
- **A feedback loop**: decision log + 30-day review reminder calibrates your judgment against real outcomes — something books and articles can't give you
- **Time saved**: graded intervention keeps simple questions undisturbed; deep thinking is spent only where it's worth it

## Installation

### Claude Code (macOS/Linux)

```bash
# 1. Clone the repo
git clone https://github.com/Mihooni/thinking-models.git ~/.cc-switch/skills/thinking-models

# 2. Create a symlink to mount
ln -s ~/.cc-switch/skills/thinking-models ~/.claude/skills/thinking-models

# 3. Restart Claude Code
```

### Claude Code (Windows)

```powershell
# 1. Clone the repo
git clone https://github.com/Mihooni/thinking-models.git %USERPROFILE%\.cc-switch\skills\thinking-models

# 2. Create a symlink (PowerShell as Administrator)
cmd /c mklink /D %USERPROFILE%\.claude\skills\thinking-models %USERPROFILE%\.cc-switch\skills\thinking-models

# 3. Restart Claude Code
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

## File structure

```
thinking-models/
├── SKILL.md            ← Entry file (~3K tokens), handles most scenarios
├── FULL-MODELS.md      ← Extension: models #11-66, 5 domains
├── BIAS-CORRECTION.md  ← Extension: 39 bias quick-reference cards (full version in bias-correction skill)
├── REFERENCE.md        ← Reference: decision trees / anti-abuse / usage guide / scenario entries
├── AGENTS.md           ← Cross-platform format (Codex/Cline/Continue)
├── .cursorrules        ← Cursor format
├── install.sh          ← One-line install script
├── README.md           ← Chinese version (default)
└── README.en.md        ← This file
```

## How it works

```
Question received → depth grading
    ├─ L0 Simple (standard answer / pure fact)     → normal reply + 1 bonus line, no framework shown
    ├─ L1 Medium (comparison / causation / light)  → normal reply + 1 insight
    └─ L2-L3 Deep (dilemma / systemic / stakes)    → six-step protocol: first-principles decomposition
                                                     → tacit knowledge → model matching → output check
                                                     → adversarial review → decision log
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

## Essence
What you're facing isn't a "disobedient kid" but a **normal developmental stage of autonomy awakening**. The core conflict: the child needs to prove "I can decide for myself," while the parent still controls through "it's for your own good."

## Analysis
Most parents respond with "more control," which reinforces the rebellion — the child isn't resisting the rules themselves but the feeling of being controlled. Counter-intuitive insight: **what a rebellious kid needs most isn't better rules, but bounded choices**. When you give them room to decide within a framework ("do you want to start with math or English?"), the need for autonomy is satisfied and the pushback fades.

## Actions
1. **Offer bounded choices** — turn "you must do A" into "A or B, you pick" — start today
2. **Separate bottom lines from flexibility** — safety and ethics are non-negotiable; everything else gets space — map this week
3. **Record positive behavior** — note 1 thing your kid did well each day; reinforce, don't criticize — for 2 weeks

## Risk
The worst outcome isn't "the phase drags on" — it's "the kid learns to lie to escape control": obedient on the surface, distant underneath.

### L2-L3 Deep question (with vs. without the skill)

**Q**: "Should I stay in the big city?"

**A typical AI answer**:

> It depends on your career development, cost of living, and personal preferences. Big cities have more opportunities but more pressure; small towns are comfortable but offer fewer opportunities. Consider everything and decide for yourself.

**Thinking-models-enhanced answer**:

## Essence
You asked "should I stay," but the real question is **"what kind of life do you want"**. Staying in a big city isn't a good/bad binary — it's a trade-off between different life paths.

## Analysis
Counter-intuitive insight: most people decide on "more opportunities = stay," ignoring **diminishing marginal utility** — "more opportunities" means different things in year 3 versus year 10. The real question: **in which environment is your sweet spot (passion × skill × demand) easier to realize?**

## Actions
1. **List your core needs** — career growth / family time / housing / social life, which ranks first? — 1 day
2. **Compute the 3-year delta** — big city vs. hometown in 3 years: net worth / position / quality of life — 1 week
3. **Run a trial** — take a week off, live in your hometown, feel the real difference — 1 month

## Risk
The worst outcome isn't "choosing wrong" — it's "never choosing": five years later, rooted in neither place, empty-handed in both.

### Guiding mode (Socratic)

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

## Use cases

### ✅ Great fit
- Career decisions (job change / career switch / starting a business)
- Interpersonal communication (parenting / partner / colleagues)
- Spending decisions (house / insurance / big purchases)
- Self-growth (what to learn / how to improve)
- Business analysis (competitive strategy / resource allocation / growth)
- Everyday dilemmas (what to eat / where to go / which to pick)

### ⚠️ Consult a professional first
- Mental health (depression / anxiety / self-harm)
- Legal disputes (divorce / contracts / litigation)
- Medical decisions (treatment plans / medication)

### ❌ Not for
- Pure fact lookups (weather / dates / definitions)
- Code errors / debugging
- Creative entertainment (stories / jokes)

## Tips

| You say | AI behavior |
|---|---|
| "Keep it short" / "one sentence" | Mode A: direct conclusion + 1 key insight |
| "Help me think it through" / "guide me" | Mode B: Socratic questions, no decision made for you |
| "Analyze in depth" / "as detailed as possible" | Mode C: essence → analysis → actions → risk |
| "No analysis / just answer" | Exit mechanism kicks in, normal reply |

## Methodology sources

The mental models and cognitive biases in this skill are curated from:
- Daniel Kahneman, *Thinking, Fast and Slow*
- Charlie Munger, *Poor Charlie's Almanack*
- Nassim Taleb, *Antifragile* and *The Black Swan*
- Chip & Dan Heath, *Decisive*
- Richard Thaler, *Nudge*
- Plus the academic consensus of behavioral economics and cognitive psychology

## One-line install

```bash
curl -fsSL https://raw.githubusercontent.com/Mihooni/thinking-models/main/install.sh | bash
```

After installing, restart Claude Code and try: "Help me decide whether to change jobs"

## A note for users

This skill doesn't think for you — it helps you **discover what you already know but haven't noticed**.

Most of the time, the answer is already in your head — I just help you dig it out.

## Share

If you find this skill useful, here's how you might recommend it to a friend:

> I installed a "thinking coach" skill for Claude. Instead of cold answers, it asks probing questions and surfaces my blind spots. Check it out: github.com/Mihooni/thinking-models

## Changelog

See [CHANGELOG.md](CHANGELOG.md)

## Support this project

This skill is free and open source (MIT). If it helped you avoid a bad decision or finally think through something you'd been wrestling with, consider buying the author a coffee:

- **GitHub Sponsors**: [github.com/sponsors/Mihooni](https://github.com/sponsors/Mihooni)
- Or drop a ⭐ Star — it helps others find this, which matters just as much for an open-source project

## License

MIT
