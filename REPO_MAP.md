# 🗺️ AI That Works — Repo Map / Wiki Index

> **Last updated:** 2026-09-01  |  **Source:** `ai-that-works/ai-that-works` upstream + `selftwo` fork  |  **Episodes:** 75 total (70 past · 1 upcoming · 3 workshops)

> **Transcripts:** 37 episodes have timestamped, speaker-diarized transcripts (`@dexhorthy` / `@vaibcode` / guests).

---

## How to use this map

- **Chapters** are one folder per episode at the repo root: `YYYY-MM-DD-topic/`
- Each folder contains `meta.md` (guid, date, links), `README.md` (highlights + takeaways), `transcript.txt` (diarized), plus `email.md`/`email.json` (newsletter) and sometimes `whiteboard-*.png`
- **Knowledge layer:** `knowledge/episodes/aitw-XXX/` holds derived claims, stitched transcripts, and verification (65 reviewed packets, 444 claims in current index). Source folders remain the source of truth — see `knowledge/PIPELINE.md`.
- **Selftwo addition:** `2026-08-18-next-token-show/` is a separate 5-episode podcast review corpus (raw VTT captions + cleaned transcripts + theme analysis) — not counted in the 75-episode `data.json`.

---

## ✨ New since last sync (3 episodes)

| Date | # | Title | YouTube | What it's about (one line) | Transcript |
|---|---|---|---|---|---|
| 2026-08-18 | 70 | syncs and A/B testing 200 agents | [watch](https://www.youtube.com/watch?v=GF7dnSlCM4U) | We've got a special two-part episode for you this week! We brought on two guests to tackle | ✅ 1009 lines |
| 2026-08-25 | 71 | Software Factory Design Patterns | [watch](https://www.youtube.com/watch?v=tGbjIvvYuHE) | In this episode, we'll talk about key interfaces and how they fit together in the modern s | ✅ 1282 lines |
| 2026-09-01 | 72 | Code Mode for Extensible Software | — (upcoming) | Making software extensible has always involved designing good and flexible interfaces (e.g | ⏳ upcoming |

### New episode details

#### 2026-08-18 — #70 · syncs and A/B testing 200 agents

**Folder:** `2026-08-18-syncs-and-ab-testing-200-agents/` · **GUID:** `aitw-070` · **YouTube:** https://www.youtube.com/watch?v=GF7dnSlCM4U

> A two-part episode: Avery from Boundary on why AI agents keep picking bad data structures (and how that compounds into slop), then Kyle Mistele from HumanLayer on how their sync engine keeps hundreds of live coding agent sessions in sync across web, mobile, and desktop clients.

We've got a special two-part episode for you this week! We brought on two guests to tackle two massive technical challenges in production AI:

What actually happens when you spin up 200 agents in parallel to run real A/B tests?

How do you cleanly sync data all the way from raw state, through your agent layer, down to the frontend?

Tune in for practical takeaways on scaling agent infrastructure that works.

**Highlights**

- "Show me your flowcharts and conceal your tables and I shall continue to be mystified. Show me your tables and I won't usually need your flowcharts, they'll be obvious."
- "If you've chosen the right data structures and organized things well, the algorithms will almost always be self-evident."
- "Bad programmers worry about the code. Good programmers worry about the data structures and the relationships."
- "One out of those ten is gonna make my codebase worse in a way that compounds. That means after a hundred features, my codebase will be like 40% slop."

**Key takeaways**

- Agents default to the convenient data structure, not the correct one, and it shows up immediately.
- The right data structure was staring everyone in the face, and 40% of runs still missed it.
- A 12.5% bad-decision rate per feature compounds into a wrecked codebase.

**Transcript:** `2026-08-18-syncs-and-ab-testing-200-agents/transcript.txt` — 1009 lines, ~12559 words, speakers: dexhorthy, vaibcode

**Newsletter:** `2026-08-18-syncs-and-ab-testing-200-agents/email.md` — 703 words

---

#### 2026-08-25 — #71 · Software Factory Design Patterns

**Folder:** `2026-08-25-software-factory-design-patterns/` · **GUID:** `aitw-071` · **YouTube:** https://www.youtube.com/watch?v=tGbjIvvYuHE

> Dex and Vaibhav zoom in on the part of the software factory where agents actually build and test the thing, mapping out the four core layers (compute, dev environment, harness, orchestration) and where to buy versus build at each one.

In this episode, we'll talk about key interfaces and how they fit together in the modern software factory, what you could buy vs build, what you should always own, across compute, dev environment, harness, and orchestration. We'll dig into how sessions / traces / artifacts / plans all become perrs of code in the new forge / system of record for software

**Highlights**

- "A factory that cannot trace a part back to the station that made it cannot compute yield, and yield is the entire reason to build a factory."
- "The goal of the software factory is not to build software. The goal of the software factory is to deliver on whatever's on the other side of that. This is the industrialization of the process."
- "The folly a lot of people make is they try to build a system that is fully automatic. That's much harder than getting a system that's 95% automatic."
- "You should be able to instead of having to buy everything below whatever layer you buy at, or build the whole thing yourself, work in open systems and plug these things together. It's composition over inheritance."

**Key takeaways**

- Every agentic software factory breaks down into four layers: compute, dev environment, harness, and orchestration.
- The dev environment layer causes the most friction, and Google and Facebook already solved it a decade ago.
- Decide whether your dev environment is "pets" or "cattle" before you scale.

**Transcript:** `2026-08-25-software-factory-design-patterns/transcript.txt` — 1282 lines, ~16699 words, speakers: dexhorthy, vaibcode

**Newsletter:** `2026-08-25-software-factory-design-patterns/email.md` — 776 words

---

#### 2026-09-01 — #72 · Code Mode for Extensible Software

**Folder:** `2026-09-01-code-mode-extensible-software/` · **GUID:** `aitw-072` · **YouTube:** —

Making software extensible has always involved designing good and flexible interfaces (e.g. vs code extensions, iphone apps). But the most flexible interface is code, and today Vaibhav's gonna share some very futuristic ideas on what the next generation of customizable tools looks like.

**Transcript:** `2026-09-01-code-mode-extensible-software/transcript.txt` — 0 lines, ~0 words, speakers: —

---


## 📚 Full episode chronology (oldest → newest)

| Date | # | Title | Past? | Links | Transcript | About |
|---|---|---|---|---|---|---|
| 2025-03-31 | 1 | S01E01 – Large Scale Classification | ✅ | [▶](https://youtu.be/6B7MzraQMZk) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-03-31-large-scale-classification) | — | LLMs are great at classification from 5, 10, maybe even 50 categories. But how do … |
| 2025-04-08 | 2 | S01E02 – Reasoning Models vs Reasoning Prompts | ✅ | [▶](https://youtu.be/D-pcKduKdYM) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-04-07-reasoning-models-vs-prompts) | — | Models can reason but you can also reason within a prompt. Which technique wins ou… |
| 2025-04-15 | 3 | S01E03 – Code Generation with Small Models | ✅ | [▶](https://youtu.be/KJkvYdGEnAY) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-04-15-code-generation-small-models) | — | Large models can do a lot, but so can small models. We'll discuss techniques for h… |
| 2025-04-22 | 4 | S01E04 – Twelve Factor Agents | ✅ | [▶](https://youtu.be/yxJDyQ8v6P0) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-04-22-twelve-factor-agents) | — | Learn how to build production-ready AI agents using the twelve-factor methodology.… |
| 2025-05-10 | None | Workshop NYC – Twelve Factor Agents | ✅ | [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-05-10-workshop-nyc-twelve-factor-agents) | — | Live workshop in NYC on building 12 factor agents. Interactive instruction, code-a… |
| 2025-05-13 | 1 | S02E01 – Designing Evals | ✅ | [▶](https://youtu.be/-N6MajRfqYw) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-05-13-designing-evals) | — | Minimalist and high-performance testing/evals for LLM applications. Stay tuned for… |
| 2025-05-17 | None | Workshop SF – Twelve Factor Agents | ✅ | [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-05-17-workshop-sf-twelve-factor-agents) | — | Live workshop in San Francisco on building 12 factor agents. Interactive instructi… |
| 2025-05-20 | 2 | S02E02 – Policy to Prompt: Evaluating w/ the Enron Emails Dataset | ✅ | [▶](https://www.youtube.com/watch?v=gkekVC67iVs) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-05-20-policies-to-prompts) | — | One of the most common problems in AI engineering is looking at a set of policies/… |
| 2025-05-27 | 3 | S02E03 – 12-factor agents: selecting from thousands of MCP tools | ✅ | [▶](https://www.youtube.com/watch?v=P5wRLKF4bt8) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-05-27-mcp-with-10000-tools) | — | MCP is only as great as your ability to pick the right tools. We'll dive into show… |
| 2025-06-03 | 4 | S02E04 – Humans as Tools: Async Agents and Durable Execution | ✅ | [▶](https://youtu.be/NMhH5_ju3-I) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-06-03-humans-as-tools-async) | — | Agents are great, but for the most accuracy-sensitive scenarios, we some times wan… |
| 2025-06-10 | 5 | S02E05 – Cracking the Prompting Interview | ✅ | [▶](https://youtu.be/PU2h0V-pANQ) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-06-10-cracking-the-prompting-interview) | — | Ready to level up your prompting skills? Join us for a deep dive into advanced pro… |
| 2025-06-17 | 6 | S02E06 – Entity Resolution: Extraction, Deduping, and Enriching | ✅ | [▶](https://youtu.be/niR896pQWOQ) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-06-17-entity-extraction) | — | Disambiguating many ways of naming the same thing (companies, skills, etc.) - from… |
| 2025-06-24 | 7 | S02E07 – Building an AI Content Pipeline | ✅ | [▶](https://www.youtube.com/watch?v=Xece-W7Xf48) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-06-24-ai-content-pipeline) | — | Content creation involves a lot of manual work - uploading videos, sending emails,… |
| 2025-07-01 | 8 | S02E08 – Boosting AI Output Quality | ✅ | [▶](https://www.youtube.com/watch?v=HsElHU44xJ0) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-07-01-ai-content-pipeline-2) | — | This week's session was a bit meta! We explored 'Boosting AI Output Quality' by bu… |
| 2025-07-08 | 9 | S02E09 – Building AI with Memory & Context | ✅ | [▶](https://www.youtube.com/watch?v=-doV02eh8XI) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-07-08-context-engineering) | — | How do we build agents that can remember past conversations and learn over time? W… |
| 2025-07-15 | 10 | S02E10 – Implementing Decaying-Resolution Memory | ✅ | [▶](https://www.youtube.com/watch?v=CEGSDlCtI8U) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-07-15-decaying-resolution-memory) | — | Last week on #13, we did a conceptual deep dive on context engineering and memory … |
| 2025-07-22 | 11 | S02E11 – PDFs, Multimodality, Vision Models | ✅ | [▶](https://youtu.be/sCScFZB4Am8) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-07-22-multimodality) | — | Dive deep into practical PDF processing techniques for AI applications. We'll expl… |
| 2025-07-29 | 12 | S02E12 – Evaluating Prompts Across Models | ✅ | [▶](https://www.youtube.com/watch?v=OawyQOrlubM) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-07-29-eval-many-models-same-prompt) | — | AI That Works #16 will be a super-practical deep dive into real-world examples and… |
| 2025-08-05 | 13 | S02E13 – Context Engineering for Coding Agents | ✅ | [▶](https://www.youtube.com/watch?v=42AzKZRNhsk) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-08-05-advanced-context-engineering-for-coding-agents) | — | By popular demand, AI That Works #17 will dive deep on a new kind of context engin… |
| 2025-08-12 | 14 | S02E14 – Decoding Context Engineering Lessons from Manus | ✅ | [▶](https://youtu.be/OaUOHEHtlOU) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-08-12-manus-context-engineering) | — | A few weeks ago, the Manus team published an excellent paper on context engineerin… |
| 2025-08-19 | 15 | S02E15 – Interruptible Agents | ✅ | [▶](https://youtu.be/2ivXNdHJpxk) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-08-19-interruptible-agents) | — | Anyone can build a chatbot, but the user experience is what truly sets it apart. C… |
| 2025-08-26 | 16 | Claude for Non-Code Tasks | ✅ | [▶](https://youtu.be/NJcph4j9sNg) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-08-26-claude-for-non-code-workflows) | — | On #17 we talked about advanced context engineering workflows for using Claude cod… |
| 2025-09-02 | 21 | Voice Agents and Supervisor Threading | ✅ | [▶](https://youtu.be/UCqD_KUyUJA) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-09-02-voice-agents-supervisor-threading) | — | Exploring voice-based AI agents and supervisor threading patterns for managing com… |
| 2025-09-09 | 22 | Generative UIs and Structured Streaming | ✅ | [▶](https://www.youtube.com/watch?v=RX8D5oJrV9k) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-09-09-generative-uis) | — | We'll explore hard problems in building rich UIs that rely on streaming data from … |
| 2025-09-16 | 23 | Bash vs. MCP - token efficient coding agent tooling | ✅ | [▶](https://www.youtube.com/watch?v=RtXpXIY4sLk) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-09-16-coding-agent-tools-bash-vs-mcp) | — | In this conversation, Dex and Vaibhav delve into the intricacies of coding agents,… |
| 2025-09-23 | 24 | Evals for Classification | ✅ | [▶](https://youtu.be/5Fy0hBzyduU) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-09-23-evals-for-classification) | — | In this episode of AI That Works, hosts Vaibhav Gupta and Dex, along with guest Ke… |
| 2025-09-30 | 25 | Dynamic Schemas | ✅ | [▶](https://youtu.be/bak7-C--azc) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-09-30-dyanmic-schemas) | — | In this episode, Dex and Vaibhav explore the concept of dynamic UIs and how to bui… |
| 2025-10-07 | 26 | Anthropic Post Mortem | ✅ | [▶](https://youtu.be/bLx-UlRTiEw) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-10-07-anthropic-post-mortem) | — | In this conversation, Vaibhav Gupta and Aaron discuss various aspects of AI model … |
| 2025-10-12 | None | Unconference SF | ✅ | [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-10-12-unconference-sf) | — | Special unconference episode from San Francisco. |
| 2025-10-14 | 27 | No Vibes Allowed - Live Coding with AI Agents | ✅ | [▶](https://youtu.be/zNZs19fIDHk) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-10-14-no-vibes-allowed) | — | Vaibhav Gupta and Dex demonstrate the power of AI-assisted coding by implementing … |
| 2025-10-21 | 28 | Agentic RAG + Context Engineering | ✅ | [▶](https://youtu.be/grGSFfyejA0) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-10-21-agentic-rag-context-engineering) | — | In this conversation, Vaibhav Gupta and Dex explore the intricacies of building an… |
| 2025-10-28 | 29 | Ralph Wiggum under the hood: Coding Agent Power Tools | ✅ | [▶](https://www.youtube.com/watch?v=fOPvAPdqgPo) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-10-28-ralph-wiggum-coding-agent-power-tools) | — | We've talked a lot about how to use context engineering to get more out of coding … |
| 2025-11-04 | 30 | Event-driven agentic loops | ✅ | [▶](https://www.youtube.com/watch?v=_VB9TT1Vus4) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-11-05-event-driven-agents) | — | Key takeaway: treat agent interactions as an event log, not mutable state. Modelin… |
| 2025-11-11 | 31 | Dates, Times, and LLMs | ✅ | [▶](https://www.youtube.com/watch?v=l7txtbgCFGU) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-11-11-dates-and-times) | — | How do you make an LLM amazing at dates? Relative dates, absolute dates, timezones… |
| 2025-11-18 | 32 | Building an Animation Pipeline | ✅ | [▶](https://www.youtube.com/watch?v=WhtT7K5Pkv0) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-11-18-building-an-animation-pipeline) | ✅ 10k w | We do a lot of work with Excalidraw, and this session shows the AI-first workflow |
| 2025-11-25 | 33 | No Vibes Allowed: Using CodeLayer to Build CodeLayer | ✅ | [▶](https://www.youtube.com/watch?v=fF3GssyaTcc) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-11-25-no-vibes-allowed-using-codelayer-to-build-codelayer) | — | Live coding with CodeLayer, we'll use Research / Plan / Implement live |
| 2025-12-02 | 35 | Multimodal Evals | ✅ | [▶](https://www.youtube.com/watch?v=jzhVo0iAX_I) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-12-02-multimodal-evals) | ✅ 12k w | Building evals for multimodal AI - testing vision models, document understanding, |
| 2025-12-09 | 34 | Git Worktrees for AI Coding Agents | ✅ | [▶](https://www.youtube.com/watch?v=OpM-G3WNH4g) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-12-09-git-worktrees) | ✅ 11k w | Since ~ May 2025, there's been a ton of buzz around AI coding agents, parallelizin… |
| 2025-12-16 | 36 | Building a Prompt Optimizer | ✅ | [▶](https://www.youtube.com/watch?v=IkSEXg6f4KY) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-12-16-prompt-optimizer) | ✅ 12k w | What happens when models can write really good prompts? We dive deep into prompt o… |
| 2025-12-23 | 37 | Founding HumanLayer: Dex's Journey | ✅ | [▶](https://www.youtube.com/watch?v=LEOA19Ss9lc) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-12-23-founding-humanlayer) | ✅ 13k w | End of year special part 1: Dex shares his journey from physics undergrad with hal… |
| 2025-12-30 | 38 | Founding Boundary: Vaibhav's Journey | ✅ | [▶](https://www.youtube.com/watch?v=4YTl9w_bESE) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2025-12-30-founding-boundary) | ✅ 16k w | End of year special part 2: Vaibhav shares his journey from building card games in… |
| 2026-01-06 | 39 | Understanding Latency in AI Applications | ✅ | [▶](https://www.youtube.com/watch?v=wadVIkJnjQE) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-01-06-latency) | ✅ 14k w | A deep dive into performance engineering for AI applications. We explore all the b… |
| 2026-01-13 | 40 | Applying 12-Factor Principles to Coding Agent SDKs | ✅ | [▶](https://www.youtube.com/watch?v=qgAny0sEdIk) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-01-13-applying-12-factor-principles-to-coding-agent-sdks) | ✅ 14k w | We've done a lot of talking in the last few months about prompting coding agents a… |
| 2026-01-20 | 41 | Email is All You Need | ✅ | [▶](https://www.youtube.com/watch?v=zpfXzk-3Yxw) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-01-20-email-is-all-you-need) | ✅ 13k w | Email is about as adversarial as inputs get: malformed HTML, inconsistent template… |
| 2026-01-27 | 42 | No Vibes Allowed | ✅ | [▶](https://www.youtube.com/watch?v=Xq8VxnGVStg) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-01-27-no-vibes-allowed) | ✅ 20k w | We received great feedback from our previous live coding sessions, so this week we… |
| 2026-02-03 | 43 | Prompting Is Becoming a Product Surface | ✅ | [▶](https://www.youtube.com/watch?v=qdfwmYTO0Aw) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-02-03-prompting-is-becoming-a-product-surface) | ✅ 6k w | Prompting used to be an engineering problem. Write the right string, tweak it unti… |
| 2026-02-10 | 44 | Agentic Backpressure Deep Dive | ✅ | [▶](https://www.youtube.com/watch?v=Zx_GOhGik0o) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-02-10-agentic-backpressure-deep-dive) | ✅ 11k w | In our next installment of advanced coding agent workflows, we'll explore some alt… |
| 2026-02-17 | 45 | AI Content Pipeline Revisited | ✅ | [▶](https://www.youtube.com/watch?v=U5Gssat8IUw) · [code](https://github.com/hellovai/ai-that-works/tree/main/2026-02-17-automating-aitw) | ✅ 11k w | We have another meta episode this week! Several months ago, we did an episode back… |
| 2026-02-24 | 46 | No Vibes Allowed February | ✅ | [▶](https://www.youtube.com/watch?v=YcT7gjzj2TU) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-02-24-no-vibes-february) | ✅ 11k w | In our February edition of our No Vibes Allowed series, we will be coding and ship… |
| 2026-03-03 | 47 | PII Redaction and Sensitive Data Scrubbing | ✅ | [▶](https://www.youtube.com/watch?v=Ql2gLHWuX7M) · [code](https://github.com/hellovai/ai-that-works/tree/main/2026-03-03-pii-redaction-and-sensitive-data-scrubbing) | ✅ 13k w | When building generative AI systems, one of the biggest risks companies face is th… |
| 2026-03-10 | 48 | Claude Agent Skills Deep Dive | ✅ | [▶](https://www.youtube.com/watch?v=b5O6gb_Zuk8) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-03-10-claude-agent-skills-deep-dive) | ✅ 13k w | Claude Code has exploded in its abilities over the past 8 months, and it can be ha… |
| 2026-03-17 | 49 | Prompt Injections Guardrails | ✅ | [▶](https://www.youtube.com/watch?v=zU8GpxgYDvc) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-03-17-prompt-injections-guardrails) | ✅ 10k w | A major risk factor in agentic coding is Prompt Injections. Tool output, document … |
| 2026-03-24 | 50 | MCP is Dead? | ✅ | [▶](https://www.youtube.com/watch?v=z5inaSXkiTU) · [code](https://github.com/hellovai/ai-that-works/tree/main/2026-03-24-mcp-is-dead) | ✅ 12k w | MCP isn't dead...or is it? This week on the podcast, we'll dive into this debate. … |
| 2026-03-31 | 51 | No Vibes Allowed March Edition | ✅ | [▶](https://www.youtube.com/watch?v=0rMG-3iiilc) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-03-31-no-vibes-march) | ✅ 27k w | This week on the podcast is our March episode of our no vibes allowed series! Join… |
| 2026-04-07 | 52 | SSE Streaming | ✅ | [▶](https://www.youtube.com/watch?v=9MFiATinGC0) · [code](https://github.com/hellovai/ai-that-works/tree/main/2026-04-07-sse-streaming) | ✅ 12k w | This week we build a real-time site summarizer using Server-Sent Events (SSE) stre… |
| 2026-04-14 | 53 | Agentic Coding for Frontend Apps | ✅ | [▶](https://www.youtube.com/watch?v=adpUOpW85ns) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-04-14-agentic-coding-for-frontend-apps) | ✅ 11k w | We do a lot of deep research and planning advice for building complex backend syst… |
| 2026-04-21 | 54 | Harness Engineering Without the Hype | ✅ | [▶](https://www.youtube.com/watch?v=gX9WpYY61xA) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-04-21-harness-engineering-without-the-hype) | — | This week on the pod we are going to cut through the hype around harness engineeri… |
| 2026-04-28 | 55 | No Vibes Allowed - Building Design Docs with AI | ✅ | [▶](https://www.youtube.com/watch?v=KCqsoXveqiI) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-04-28-no-vibes-design-docs) | ✅ 13k w | In this month's no vibes allowed episode, Vaibhav will show how he uses AI to make… |
| 2026-05-05 | 56 | OpenAI tells you not to build your own harness | ✅ | [▶](https://www.youtube.com/watch?v=h99bTZTR_IU) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-05-05-openai-tells-you-not-to-build-your-own-harness) | ✅ 11k w | Harness engineering is all the hype now, so on this week on the podcast we're look… |
| 2026-05-12 | 57 | "Code Mode" Deep Dive | ✅ | [▶](https://www.youtube.com/watch?v=0dx3j4CmSFw) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-05-12-code-mode-deep-dive) | ✅ 12k w | On Monday, Pash from OpenAI shared that Codex has a secret "code mode" feature - a… |
| 2026-05-19 | 58 | How AI Agents Can Safely Ship Code to Production | ✅ | [▶](https://www.youtube.com/watch?v=gRqb7R4Pcrs) · [code](https://github.com/hellovai/ai-that-works/tree/main/2026-05-19-feature-flag-everything) | ✅ 7k w | This week, the top headline is vibe coders realizing that they can use feature fla… |
| 2026-05-26 | 59 | No Vibes Allowed: Performance Engineering | ✅ | [code](https://github.com/ai-that-works/ai-that-works) | — | This week on the podcast, we are doing another no vibes allowed episode focusing o… |
| 2026-06-02 | 60 | How to Build AI Agents that Work in Any Language | ✅ | [▶](https://www.youtube.com/watch?v=-gFdtc-HbOY) · [code](https://github.com/hellovai/ai-that-works/tree/main/2026-06-02-multilingual-ai-apps) | ✅ 12k w | In this episode, we discuss the challenge of building multilingual AI applications… |
| 2026-06-09 | 61 | Hands-on with Fable 5 | ✅ | [▶](https://www.youtube.com/watch?v=hTkmSVuDMPg) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-06-09-agent-observability) | ✅ 8k w | We had agent observability on the schedule, but Anthropic shipped Fable 5 about tw… |
| 2026-06-16 | 62 | Product Specs with AI | ✅ | [▶](https://www.youtube.com/watch?v=0LPBw3NO3Jc) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-06-16-product-specs-with-ai) | ✅ 11k w | We've talked a lot about design discussions for planning work with AI and getting … |
| 2026-06-23 | 63 | Software Factory for Agent Tools | ✅ | [▶](https://www.youtube.com/watch?v=485FGIq8LKM) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-06-23-software-factory-for-agent-tools) | ✅ 11k w | Everyone's obsessed with software factories, and the core of a software factory is… |
| 2026-07-07 | 64 | agent observability | ✅ | [▶](https://www.youtube.com/watch?v=_WLVv1C6-VM) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-07-07-agent-observability) | ✅ 12k w | In this episode, we will dive into AI agent observability and answer a question ev… |
| 2026-07-14 | 65 | SOTA Coding Agent Benchmarks | ✅ | [▶](https://www.youtube.com/watch?v=X5mI1ZVxaIc) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-07-14-sota-coding-agent-benchmarks) | ✅ 10k w | We've had a lot of benchmarks for coding agents for a long time. We'll talk about … |
| 2026-07-21 | 66 | No Vibes Allowed - July Edition | ✅ | [▶](https://www.youtube.com/watch?v=rTn8Vhdt-Jo) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-07-21-no-vibes-july) | ✅ 12k w | This week on the podcast we will be hosting another session of our No Vibes Allowe… |
| 2026-07-28 | 67 | Your Model is Already Obsolete | ✅ | [▶](https://www.youtube.com/watch?v=Y-I9m5YsAcs) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-07-28-your-model-is-already-obsolete) | ✅ 11k w | In the last month alone: Opus 5, Sonnet 5, Grok 4.5, Kimi K3, GPT-5.6, Gemini 3.6.… |
| 2026-08-04 | 68 | SlopCodeBench | ✅ | [▶](https://www.youtube.com/watch?v=Yh4eL60Ncxs) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-08-04-slop-code-bench) | ✅ 11k w | On the podcast this week, we will examine a new AI coding benchmark called SlopCod… |
| 2026-08-11 | 69 | Unconference RECAP | ✅ | [▶](https://www.youtube.com/watch?v=fyZ0i4USjgc) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-08-11-unconference-recap) | ✅ 11k w | On Saturday, August 8th, we are hosting another unconference bringing together som… |
| 2026-08-18 | 70 | syncs and A/B testing 200 agents | ✅ | [▶](https://www.youtube.com/watch?v=GF7dnSlCM4U) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-08-18-syncs-and-ab-testing-200-agents) | ✅ 12k w | We've got a special two-part episode for you this week! We brought on two guests t… |
| 2026-08-25 | 71 | Software Factory Design Patterns | ✅ | [▶](https://www.youtube.com/watch?v=tGbjIvvYuHE) · [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-08-25-software-factory-design-patterns) | ✅ 16k w | In this episode, we'll talk about key interfaces and how they fit together in the … |
| 2026-09-01 | 72 | Code Mode for Extensible Software | ⏳ | [code](https://github.com/ai-that-works/ai-that-works/tree/main/2026-09-01-code-mode-extensible-software) | — | Making software extensible has always involved designing good and flexible interfa… |

---

## 🧩 Themes & topic clusters

Quick lens for research (see `AGENT_NAVIGATION_INDEX.md` for the Read Review lens).

| Cluster | Episodes | Core idea |
|---|---|---|
| **Context engineering** | 2025-07-08, 2025-08-05, 2025-08-26, 2026-01-06 (latency), 2026-02-10 (backpressure) | Less context > more, cache, reinject, perceived latency |
| **Evals & correctness** | 2025-05-13 (designing evals), 2025-09-23 (classification evals), 2026-01-27 no-vibes | Rubrics > scores, fixtures, narrowing taxonomy, evals for skills |
| **Agents & harness** | 2025-04-22 12-factor agents, 2026-04-21 harness, 2026-03-10 skills, 2025-08-19 interruptible, 2026-04-07 SSE | State machines, own your context window, hooks vs protocols (ACP/AG-UI) |
| **Software factory / orchestration** | 2026-06-23, 2026-08-25 (design patterns — compute/env/harness/orchestration), 2025-11-05 event-driven | Four layers, pets vs cattle, composition over inheritance, yield/traceability |
| **Sync & scale** | 2026-08-18 (two-part: 200-agent A/B tests + HumanLayer sync engine) | Data structures compound slop (40% after 100 features); sync is shape-churn, not write volume; two paths (WAL + streaming) |
| **Code quality / slop** | 2026-08-04 SlopCodeBench, 2026-08-11 unconference recap, 2026-07-28 obsolete model | Single-shot benchmarks miss maintenance; deterministic linters vs memory; adversarial review; model swaps as planned outage |
| **Front-end & streaming** | 2025-09-09 generative UIs, 2026-04-14 frontend, 2026-04-07 SSE | Semantic partials, UI state matrices, BAML streaming |
| **Prompting & product surface** | 2026-02-03 prompting-as-product, 2026-03-17 guardrails, 2025-12-16 prompt optimizer | Prompt controls → model instructions, citations via indexes |
| **Workshops** | 2025-05-10 NYC, 2025-05-17 SF, 2026-04-11 SF unconf | Live 12-factor builds |
| **Selftwo bonus** | `2026-08-18-next-token-show/` (5 eps) | Next Token podcast review: captions → cleaned transcripts → theme capture |

---

## 📦 Repo layout

```
ai-that-works/
├── 2025-03-31-large-scale-classification/   # episode folders (77 dated dirs)
├── …
├── 2026-08-18-syncs-and-ab-testing-200-agents/  # ← new: transcript 1009 lines + README + whiteboard
├── 2026-08-25-software-factory-design-patterns/ # ← new: transcript 1281 lines + whiteboard
├── 2026-09-01-code-mode-extensible-software/   # ← new: meta only (upcoming Sep 1)
├── 2026-08-18-next-token-show/   # selftwo: 5 transcripts + VTT + review notes
├── knowledge/
│   ├── _catalog/  # coverage.csv, episodes.json, claims.jsonl
│   ├── episodes/aitw-001…066/  # 65 reviewed packets, 444 claims
│   └── PIPELINE.md
├── tools/  # validate-metadata.ts → README.md + feed.xml + data.json
├── data.json  # 75 episodes (70 past, 1 upcoming)
├── feed.xml   # RSS (70 items)
├── README.md  # generated episode table + next-episode CTA
├── REPO_MAP.md  # ← this file (wiki index)
└── AGENT_NAVIGATION_INDEX.md  # Read Review lens
```

---

## 🔍 Verification & provenance

- **Upstream:** `ai-that-works/ai-that-works` @ `upstream/main` HEAD `25027b9` (2026-08-31)
- **Selftwo fork:** `selftwo/ai-that-works` @ `origin/main` (`1e767ad` + this sync)
- **Staged sync:** 3 upstream episodes + 1 updated (2026-08-11 enriched README/email/transcript/whiteboard)
- **Generated files:** `README.md`, `data.json`, `feed.xml` via `bun run tools/validate-metadata.ts --fix --generate-readme` (patched to ignore `2026-08-18-next-token-show`)
- **Transcripts verified:** speaker-diarized `@dexhorthy`/`@vaibcode` format, monotonic timestamps, 1009 + 1281 lines for new episodes

```
git log upstream/main --oneline -3
25027b9 090126 episode prep
5eeeede 090126 episode prep
5197038 082526 episode
```

---

## ▶️ Next steps

- [ ] Review this map → `git commit` (staged: 20 files, +3720 -1521 lines)
- [ ] `git push origin main`
- [ ] When 2026-09-01 video publishes, fetch YouTube captions → enrich `transcript.txt` → re-run `bun run tools/validate-metadata.ts --fix --generate-readme`
