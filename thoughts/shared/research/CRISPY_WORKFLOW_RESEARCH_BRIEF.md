# CRISPY / Enhanced RPI — Research Brief for External Agents

**Purpose:** Give an external research agent enough grounded context to investigate Dexter Horthy & Vaibhav's agentic coding methodology as documented in the *AI That Works* corpus and the MLOps.community talk *"Everything We Got Wrong About Research-Plan-Implement."*

**Primary external source:** [MLOps talk (YouTube)](https://www.youtube.com/watch?v=YwZR6tc7qYg)

**Primary internal corpus:** This repo (`hellovai/ai-that-works`) — episodes, transcripts, READMEs, `EPISODE.md` files.

**Last synthesized:** 2026-06-23

---

## 1. Naming & lineage (do not conflate)

| Name | Stages | Where used |
|------|--------|------------|
| **RPI** | Research → Plan → Implement (3) | Original HumanLayer/CodeLayer prompts; `HOWTO.md`; early No Vibes episodes |
| **Q-R-D-S-O-PI** (aka **enhanced RPI**) | Research **Questions** → **Research** → **Design Discussion** → **Structured Outline** → **Plan** → **Implement** (6) | Episode #42 email recap; Jan 2026 transcripts |
| **CRISPY** | **C**ontext/questions → **R**esearch → **I**nterface/design → **S**tructure outline → **P**lan work → **I**mplement → **PR** (7) | MLOps talk; productized in **Riptide** (rebuilt CodeLayer); frontend episodes say "Crispy workflow" |

**Agent note:** The repo rarely uses the acronym "QRDSPI." Search for `RPI`, `Crispy`, `enhanced RPI`, `research questions`, `design discussion`, `structured outline`, `Riptide`.

**Relationship:** CRISPY is not a totally different methodology — it is RPI decomposed into smaller deterministic phases, plus explicit PR, plus tooling. The MLOps talk is the retrospective; episodes #42–#55 are the live demonstrations.

---

## 2. Why the methodology changed (failures of production RPI)

### 2.1 Magic words dependency
- Early RPI required expert prompting tricks or the model bulldozed ahead without alignment.
- Canonical magic phrase (from animation pipeline episode): *"work back and forth with me starting with your open questions and outline before writing the plan."*
- Team explicitly **hated** calling these "magic words" and moved to **deterministic control flow** instead of prompt sprinkling.
- **Source:** `2026-01-27-no-vibes-allowed/transcript.txt` (~lines 61–66); `2025-11-18-building-an-animation-pipeline/transcript.md` (~411)

### 2.2 Instruction budget collapse
- Original planning prompt: **85+ instructions** in one monolithic file; design discussion split from a **50-instruction** mega-prompt.
- Frontier models degrade instruction adherence past **~150–200 total system instructions** (includes tools, MCPs, subagent defs).
- Fix: **multiple prompts, each under ~40 instructions**, orchestrated by harness — not one giant plan prompt.
- **Source:** MLOps talk; `2026-01-27-no-vibes-allowed/transcript.txt` (~535–539); `2026-03-10-claude-agent-skills-deep-dive/transcript.txt` (~568–570)

### 2.3 "Don't read the code" fallacy
- Early advice: reviewing the plan is enough; skip reading generated source.
- Reality: 1,000-line plans contain 1,000 lines of code surprises; six months of skipping code review forced large rip-and-replace.
- **Current stance:** For production code with on-call responsibility, **you must read and own the code.** Sustainable target: **2–3× speed with human-grade craft**, not 10× velocity + slop cleanup.
- Nuance from episodes: Dex no longer recommends humans **primary-review full plans** (double code review); Vaibhav still reads plans and has caught bugs there. High-leverage human review = **design discussion + structured outline**, then **code review on PR**.
- **Source:** MLOps talk; `2026-01-27-no-vibes-allowed/transcript.txt` (~644–656, 1585–1593)

### 2.4 Biased research ("lazy RPI")
- Giving the agent the ticket during research biases findings toward the proposed solution.
- Skilled practitioners manually translated tickets into objective questions; CRISPY automates that split.
- **Source:** `2026-01-27-no-vibes-allowed/transcript.txt` (~233–239)

### 2.5 Horizontal vs vertical planning
- Models default to **horizontal** plans: all migrations → all services → all APIs → frontend. Nothing testable until the end.
- CRISPY forces **vertical slices**: end-to-end thin slices with explicit test/checkpoint commands between steps (like a C header file outline).
- **Source:** MLOps talk; `2026-01-27-no-vibes-allowed/transcript.txt` (~632–638); `2026-02-24-no-vibes-february/README.md`

---

## 3. CRISPY pipeline — stage-by-stage spec

```
[Questions] → [Research] → [Design] → [Structure Outline] → [Plan Work] → [Implement] → [PR]
```

Optional **Phase 0** (episodes, not in MLOps acronym): **Learning Tests / Proof Research**

Each stage should use a **fresh context window** where possible. Critical outputs are persisted as **static Markdown files** on disk (not only chat history) to survive context degradation.

### Phase 0: Learning tests (optional but high leverage)
- **When:** Before research/planning when integrating external SDKs, closed-source APIs, or behavior docs may lie.
- **What:** Small runnable programs that assert how the external system *actually* behaves.
- **Pattern:** Question → minimal setup → assertion → documented `Key findings:` header in file.
- **Slogan:** *Proofs before specs before code.*
- **Sources:** `2026-02-10-agentic-backpressure-deep-dive/EPISODE.md`, `2026-02-24-no-vibes-february/README.md`

### Stage 1: Questions (Research Questions)
- **Input:** Ticket/spec (may be used lightly for codebase orientation only).
- **Output:** List of **objective** questions — no solution baked in.
- **Rule:** **Hide the ticket from the researcher's context.** Researcher receives only the questions in a fresh window.
- **Human role:** Edit/delete/add questions before advancing.
- **Typical size:** Small (dozens of lines).
- **Source:** `2026-01-27-no-vibes-allowed/transcript.txt` (~233–256, 1666)

### Stage 2: Research
- **Input:** Objective questions only (not the feature ticket).
- **Output:** Factual compression of current system state; code references with file:line; open questions list.
- **Goal:** *Compress truth* about how things work today — not how to implement the feature.
- **Typical size:** 400–1,000 lines.
- **Human role:** Optional for small tasks; errors often surface in design if missed.
- **Source:** `2026-01-27-no-vibes-allowed/transcript.txt` (~448, 1666)

### Stage 3: Design (Design Discussion)
- **Input:** Research + ticket (solution context returns here).
- **Output:** ~**200-line Markdown** doc — current state, desired end state, relevant patterns from codebase, multiple-choice decisions (often **4 options** per question + recommendation).
- **Human role:** **Highest leverage review.** Interactive back-and-forth. Catch bad legacy pattern adoption before code.
- **Mechanics:** Open questions from research should be resolved here; new open questions may propagate to structure stage.
- **Typical size:** ~half of research doc.
- **Source:** MLOps talk; `2026-01-27-no-vibes-allowed/transcript.txt` (~535–625, 1518–1520, 1666)

### Stage 4: Structure Outline
- **Input:** Design discussion + research + ticket.
- **Output:** Concise **vertical** phase list — order of work optimized for testability and incremental verification. Not full code snippets.
- **Human role:** Team alignment artifact (share this, not the full plan). Reorder/combine phases before plan generation.
- **Anti-pattern:** Generating the full plan immediately — hard to reorder; editing plan line ranges is context-inefficient.
- **Typical size:** Low relative to plan.
- **Source:** `2026-01-27-no-vibes-allowed/transcript.txt` (~627–671, 1666)

### Stage 5: Plan Work
- **Input:** Approved structure outline + prior artifacts.
- **Output:** Detailed implementation plan for the **agent** — can be 1,000–3,000+ lines with code snippets, checkboxes, commands to run.
- **Human role:** Dex **discourages** primary human review of full plans (duplicate of PR review). Vaibhav still spot-checks. Plans should embed **automated backpressure** (exact test/build/lint commands per phase).
- **Source:** `2026-01-27-no-vibes-allowed/transcript.txt` (~638–671, 1666); `2026-02-10-agentic-backpressure-deep-dive/transcript.txt` (~721–726)

### Stage 6: Implement
- **Input:** Plan + artifacts.
- **Output:** Code changes, often via worktrees for parallel agents.
- **Human role:** Review **code** (not just plan). Magnitude-based gates discussed (e.g. require attestation for >N lines).
- **Goal:** When prior stages done well, **one-shot implementation per phase** is common.
- **Source:** `2026-01-27-no-vibes-allowed/transcript.txt` (~1593–1599)

### Stage 7: PR
- Explicit in CRISPY naming; implied in RPI.
- Reviewer agents may compare plan vs implementation for deviations.
- Feature flags for experimental/slop paths discussed in later episodes.

---

## 4. Harness & tooling architecture

### Inner vs outer loop
- **Inner loop:** Standard coding agent (Claude Code) — read, bash, edit.
- **Outer loop:** Orchestration harness knows which **engineering phase** is active; swaps prompts; uses structured outputs for phase transitions.
- **RPI/CRISPY as outer harness** beats model upgrades for many tasks (episode #56).
- **Source:** `2026-01-13-applying-12-factor-principles-to-coding-agent-sdks/transcript.md` (~369–382, 952–958); `2026-05-05-openai-tells-you-not-to-build-your-own-harness/transcript.txt`

### Product: Riptide (rebuilt CodeLayer)
- Episode #42 demos **Riptide** as preview of rebuilt CodeLayer.
- Organizes tasks, labels phases automatically, fresh context per phase.
- Planned: **Crispy vs Free Mode** UI toggle; autonomy slider (approve outline → auto-run to PR).
- Skills map to phases; can run in Claude Code manually but UX is worse for context reset/organization.
- **Source:** `2026-01-27-no-vibes-allowed/transcript.txt`; `2026-04-14-agentic-coding-for-frontend-apps/transcript.txt` (~625)

### Artifact file conventions (evolving)
- Numbered sequential files preferred: `01-research-questions`, `02-research`, `03-design-discussion`, etc.
- Moving away from date-based naming.
- All artifacts are plain Markdown on disk — editable by human or agent.
- **Source:** `2026-01-27-no-vibes-allowed/transcript.txt` (~554–563)

### Supporting engineering tools (not CRISPY stages but coupled)
| Tool | Role |
|------|------|
| **cargo stow** | Enforce crate dependency boundaries via architecture diagrams |
| **Auto architecture diagrams** | Detect invalid dependencies before implementation (e.g. playground → compiler internals) |
| **CodSpeed / perf gates** | Deterministic backpressure on performance regressions |
| **Git worktrees** | Parallel implementers; not used for markdown planning phase |
| **rpi-coordination-template** | Multi-repo RPI coordination (skills episode) |

---

## 5. Context engineering rules

| Rule | Detail | Source |
|------|--------|--------|
| Fresh context per phase | Don't carry unnecessary history between stages | `HOWTO.md`; episode #42 |
| Context budget | Stay **below ~40%** window usage; reset near **~60%** | MLOps talk |
| Persist to Markdown | Map critical outputs to static files; don't rely on compaction | MLOps talk |
| Instruction hierarchy | `CLAUDE.md` > prompts > research > plans > implementation — spend human effort highest first | `HOWTO.md` |
| No static agent MD for fast-moving codebases | Rebuild context per task via research | `2025-12-23-founding-humanlayer/transcript.md` (~325) |
| Enhanced RPI option pattern | ~4 choices per decision + recommendation; re-steer paths when wrong | `2026-01-27-no-vibes-allowed/transcript.txt` (~1518) |
| Phase sizing | Big enough to complete in one context; small enough to verify at end; combinable | `2026-01-27-no-vibes-allowed/transcript.txt` (~1526–1532) |

---

## 6. Agentic backpressure (cross-cutting)

Not a CRISPY stage but tightly integrated into plans:

- **Deterministic feedback loops** > LLM-as-judge for implementation verification.
- Plans should specify **exact commands** to run after each phase (tests, typecheck, curl, etc.).
- Convert manual verification steps to automated tests when possible.
- Pre-commit hooks, stop hooks, typecheckers as governors.
- Best engineers sometimes spend days designing the backpressure harness before writing feature code.
- **Sources:** `2026-02-10-agentic-backpressure-deep-dive/EPISODE.md`, transcript (~721–726)

---

## 7. When to use full CRISPY vs lighter workflows

| Task type | Recommended depth | Source |
|-----------|-------------------|--------|
| Trivial (button color) | Direct implement / Cursor plan-mode | `2026-01-27-no-vibes-allowed/transcript.txt` (~1564–1570) |
| Medium | Plan → Implement (RPI-lite) | same |
| Large multi-module backend | Full CRISPY / enhanced RPI | same |
| Frontend / UI taste | Full CRISPY **too heavy**; use **Plan Mode / RPI++** + **Storybook stories** as visual learning tests before implement | `2026-04-14-agentic-coding-for-frontend-apps/transcript.txt` (~70–92, 588–600) |
| Massive tasks (10k+ LOC) | Multiple research files, multiple structure outlines, split plans by phase groups | `2026-01-27-no-vibes-allowed/transcript.txt` (~1623–1628) |

**Frontend-specific pattern:** Research → Design → **Storybook prototype stories** (component exploration in browser) → Outline → Implement. Storybook replaces Figma MCP for agent-native UI iteration.

---

## 8. Ticket / spec prerequisites

CRISPY does not replace good upstream specification:

- March No Vibes episode: significant human/agent work produces the **ticket/spec first**; then zero-loop RPI generates questions → research → design.
- Upcoming episode #62 theme: **split product questions from technical questions** in design docs.
- **Sources:** `2026-03-31-no-vibes-march/transcript.txt` (~756); `README.md` (episode #62 blurb)

---

## 9. Philosophy & explicit rejections

- **2026 = no more slop** — pivot from 10× low-quality to 2–3× sustainable craft.
- **Reject lights-off software factories** — humans must read production code; no "compiled assembly humans never read."
- **RPI goal was never perfect one-shot** on huge tasks — it's **2–3× acceleration** with human architectural ownership.
- **Trust + culture** can substitute for mandatory review on small changes if tests/architecture rules are strong; large changes need magnitude-based human attestation.
- **Source:** MLOps talk; founding humanlayer; feature-flag episode (#58)

---

## 10. Episode index for researchers

Search transcripts with `rg -i "rpi|crispy|research questions|design discussion|structured outline|magic word|backpressure|learning test" <path>`

| Ep # | Date | Folder | Focus |
|------|------|--------|-------|
| #27 | 2025-10-14 | `2025-10-14-no-vibes-allowed/` | Original **3-phase RPI** live; fresh context; plan quality |
| #33 | 2025-11-25 | `2025-11-25-no-vibes-allowed-using-codelayer-to-build-codelayer/` | CodeLayer dogfooding RPI |
| #35 | 2025-12-23 | `2025-12-23-founding-humanlayer/` | RPI origin story; 2–3× goal; magic words; champions |
| #41 | 2026-01-13 | `2026-01-13-applying-12-factor-principles-to-coding-agent-sdks/` | **Harness architecture**; 5–6 step internal RPI; structured outputs |
| **#42** | **2026-01-27** | **`2026-01-27-no-vibes-allowed/`** | **Canonical enhanced RPI / QRDSPI walkthrough**; Riptide; questions phase |
| #44 | 2026-02-10 | `2026-02-10-agentic-backpressure-deep-dive/` | Learning tests; plan backpressure commands |
| #46 | 2026-02-24 | `2026-02-24-no-vibes-february/` | Full workflow + learning tests in design; vertical slices |
| #51 | 2026-03-31 | `2026-03-31-no-vibes-march/` | Auto-advance phases; ticket-before-RPI |
| #54 | 2026-04-14 | `2026-04-14-agentic-coding-for-frontend-apps/` | Crispy vs light mode; Storybook |
| #55 | 2026-04-28 | `2026-04-28-no-vibes-design-docs/` | Design docs as review artifacts; comments/versions |
| #56 | 2026-05-05 | `2026-05-05-openai-tells-you-not-to-build-your-own-harness/` | Outer harness > model; RPI as stacked loop |
| #58 | 2026-05-19 | `2026-05-19-feature-flag-everything/` | Shipping slop safely |

**External talk:** Dexter Horthy, *Everything We Got Wrong About Research-Plan-Implement*, MLOps.community — [YouTube](https://www.youtube.com/watch?v=YwZR6tc7qYg)

**Stale doc warning:** `HOWTO.md` still describes **3-phase RPI** only — episodes are ahead of HOWTO on methodology depth.

---

## 11. Research prompts for external agents

Use these if delegated to investigate the corpus:

1. **Trace the phase split:** How did the monolithic RPI plan prompt get decomposed? Find all mentions of instruction counts and skipped steps.
2. **Artifact schema:** What fields/sections appear in design discussions, structure outlines, and plans across episodes?
3. **Human review points:** Where do Dex and Vaibhav disagree on whether humans should read plans vs only design/outline?
4. **Tooling coupling:** How do cargo stow, architecture diagrams, and CI gates interact with CRISPY stages?
5. **Frontend exception:** Document the Storybook-based alternative path and when Crispy is intentionally skipped.
6. **Product evolution:** Riptide/CodeLayer features mentioned (auto-advance, Crispy vs Free Mode, autonomy slider) — what's demo vs shipped?
7. **Compare to industry:** Cursor plan mode, Claude plan mode, Devin, etc. — how does Dex position CRISPY vs those?

### High-signal `rg` commands

```sh
rg -n "research questions|design discussion|structured outline|enhanced RPI|magic word" \
  2026-01-27-no-vibes-allowed 2026-02-10-agentic-backpressure-deep-dive \
  2026-02-24-no-vibes-february 2026-01-13-applying-12-factor-principles-to-coding-agent-sdks

rg -n "Crispy|Plan Mode|Storybook|RPI\+\+" 2026-04-14-agentic-coding-for-frontend-apps

rg -n "learning test|backpressure|Phase 0" 2026-02-10-agentic-backpressure-deep-dive
```

---

## 12. Anti-patterns checklist

- [ ] Passing the feature ticket into the research context
- [ ] Single prompt with 50–85+ planning instructions
- [ ] Relying on magic words instead of harness phase gates
- [ ] Horizontal plans with no intermediate verification
- [ ] Human primary-review of 1,000–3,000 line plans instead of design + outline + code
- [ ] Skipping code review on production paths
- [ ] Letting context exceed ~60% without reset
- [ ] Using full Crispy for UI taste iteration
- [ ] One giant plan for 10k+ LOC without splitting research/outline/plan
- [ ] LLM-as-judge without matching the production message structure

---

## 13. Open / evolving areas (as of corpus date)

- **Crispy vs Free Mode** UI in Riptide (mentioned, in progress)
- **Autonomy slider** — approve outline then auto-run to PR
- **Product vs technical question split** in design docs (episode #62 upcoming)
- **Plan visualizer** — jokingly proposed; design doc comment UI exists in BEPs tooling
- **Magnitude-based review gates** — LLM or line-count triggered human attestation
- **Numbered artifact filenames** — migrating from dated names

---

## 14. Key quotes (for grounding)

> "The goal of RPI is not to perfectly one-shot a long complex task. It's to speed you up by 2 to 3x." — Dex, founding humanlayer episode

> "A bad line of code is a bad line of code. A bad part of a plan is a hundred bad lines of code." — episode #27 README

> "Proofs before specs before code." — backpressure EPISODE.md

> "We've done a lot of replacing the usage of prompting for control flow by splitting up the workflow." — Dex, episode #42

> "Research tells you what the docs say. Learning tests tell you what the code does." — backpressure EPISODE.md

---

## 15. Related repo files (start here)

| File | Why |
|------|-----|
| `2026-01-27-no-vibes-allowed/transcript.txt` | Richest end-to-end CRISPY demo |
| `2026-01-27-no-vibes-allowed/email.json` | Official 6-step naming |
| `2026-02-10-agentic-backpressure-deep-dive/EPISODE.md` | Learning tests + backpressure theory |
| `2026-01-13-applying-12-factor-principles-to-coding-agent-sdks/transcript.md` | Harness / structured-output phase transitions |
| `2026-04-14-agentic-coding-for-frontend-apps/transcript.txt` | When not to use full Crispy |
| `AGENT_NAVIGATION_INDEX.md` | Broader repo navigation for agents |
| `HOWTO.md` | Older 3-phase summary (incomplete vs episodes) |
