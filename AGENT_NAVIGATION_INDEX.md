# AI That Works Navigation Index For Agents

Date added: 2026-06-22

Purpose: help future agents navigate this repo quickly, especially when researching Read Review or adjacent document-review products.

This repo is a corpus of episodes, transcripts, specs, demos, notes, and generated artifacts. Do not start with a full repo scan unless the user asks for one. Start from the clusters below.

## Read Review Lens

Read Review is a local, document-centric review surface for agent-era knowledge work. Useful source material changes one of these mechanisms:

- artifact readiness and plan-doc review;
- inline comments and thread state;
- human-first review checkpoints;
- reviewer personas and tagged invocation;
- sidecar JSON, events, versions, checkpoints, exports;
- async agent replies, stale output, cancellation;
- comment quality, evidence, evals, and reasoning trails;
- UI behavior for calm document review.

## Start Here

1. `2026-04-28-no-vibes-design-docs/README.md`
   - Best first stop for design docs as reviewable artifacts.
   - Look for comments, draft/proposed states, versions, export bundles, and why Git is awkward for comment-heavy docs.

2. `2026-04-28-no-vibes-design-docs/transcript.txt`
   - Stronger than the README for product mechanics.
   - Useful sections include design-doc tooling, comments, author readiness, version history, export-to-agent-context, and Git limitations.

3. `2025-08-26-claude-for-non-code-workflows/sops/daily-review-sop.md`
   - Read/write phase separation.
   - Checkpoints, human approval, resumability, and subagent collection.

4. `2025-11-05-event-driven-agents/README.md`
   - Append-only events and projections.
   - Useful for sidecar/event/checkpoint source-of-truth design.

5. `2026-03-10-claude-agent-skills-deep-dive/README.md`
   - Distinguishes skills, subagents, and invocation boundaries.
   - Useful for keeping persona, skill, and subagent separate.

6. `2025-09-23-evals-for-classification/src/shared/correctness.py`
   - Useful correctness taxonomy: exact, more general, more specific, sibling.
   - Good model for reviewer comment quality.

## Phase 1 / Phase 2 Results

The prior Read Review scans produced these external synthesis files:

- `/Users/corphr.software/Documents/Codex/2026-06-22/spa/outputs/ai-that-works-phase1-read-review-scan.md`
- `/Users/corphr.software/Documents/Codex/2026-06-22/spa/outputs/ai-that-works-phase1-5-intermediate-queue.md`
- `/Users/corphr.software/Documents/Codex/2026-06-22/spa/outputs/ai-that-works-phase2-read-review-synthesis.md`
- `/Users/corphr.software/Documents/Codex/2026-06-22/spa/outputs/ai-that-works-read-review-findings-artifact.html`
- `/Users/corphr.software/Documents/Codex/2026-06-22/spa/outputs/read-review-doc-population-prompt-and-checklist.md`

Use those before redoing the same scan.

## Source Clusters

### Document Review Core

- `2026-04-28-no-vibes-design-docs/README.md`
- `2026-04-28-no-vibes-design-docs/transcript.txt`
- `2025-06-24-ai-content-pipeline/specs/README.md`
- `.claude/commands/complete_episode.md`
- `2025-08-26-claude-for-non-code-workflows/sops/daily-review-sop.md`
- `2025-08-26-claude-for-non-code-workflows/dailies/2025-08-26-daily-review.md`
- `2025-08-26-claude-for-non-code-workflows/thoughts/shared/research/2025-08-26_09-29-35_humanlayer-self-structure.md`

Pull forward:

- plan docs as reviewable artifacts;
- `draft -> proposed` as a real readiness gate;
- human read/write phase separation;
- comments, discussions, questions, and versions as exportable context;
- sidecar state and checkpoint artifacts.

### Reviewer Personas And Agent Boundaries

- `2026-03-10-claude-agent-skills-deep-dive/README.md`
- `2026-03-10-claude-agent-skills-deep-dive/transcript.txt`
- `2026-03-17-prompt-injections-guardrails/README.md`
- `2026-02-03-prompting-is-becoming-a-product-surface/README.md`
- `2026-02-10-agentic-backpressure-deep-dive/EPISODE.md`

Pull forward:

- persona equals review lens;
- skill equals reusable rubric/instruction;
- subagent equals isolated execution;
- reviewed documents are untrusted input;
- evidence comes before confidence;
- reviewer output should be candidate output until a human decides.

### Async Review Loop And Live State

- `2025-11-05-event-driven-agents/README.md`
- `2025-06-03-humans-as-tools-async/README.md`
- `2025-09-02-voice-agent-supervisor-threading/specification_updates.md`
- `2026-01-20-email-is-all-you-need/email.md`
- `2026-01-20-email-is-all-you-need/transcript.txt`
- `2025-08-19-interruptible-agents/README.md`
- `2026-04-07-sse-streaming/README.md`
- `2026-04-07-sse-streaming/main.py`
- `2026-04-07-sse-streaming/index.html`

Pull forward:

- append-only events;
- projected UI and persistence state;
- per-thread queues;
- stale, late, cancelled, and interrupted output;
- background reviewer output that never blocks the human;
- SSE as live projection, not storage.

### Comment Quality And Evals

- `2025-05-13-designing-evals/README.md`
- `2025-05-20-policies-to-prompts/README.md`
- `2025-09-23-evals-for-classification/tests/integration/test_pipeline_accuracy.py`
- `2025-09-23-evals-for-classification/src/shared/correctness.py`
- `2025-09-23-evals-for-classification/tests/integration/test_narrowing_accuracy.py`
- `2025-09-23-evals-for-classification/tests/data/test_cases.py`

Pull forward:

- answer keys and fixture sets;
- categorical rubrics over numeric confidence;
- evidence span checks;
- exact, too general, too specific, and sibling failure classes;
- intermediate probes and failure metadata;
- drift monitoring.

### UI And Product Surface

- `2025-09-09-generative-uis/README.md`
- `2026-04-14-agentic-coding-for-frontend-apps/README.md`
- `2026-01-06-latency/README.md`
- `2026-02-03-prompting-is-becoming-a-product-surface/README.md`

Pull forward:

- semantic partials instead of raw token streaming;
- UI state matrices;
- perceived latency;
- product controls that translate into model instructions without exposing prompt plumbing.

## Read Review Decisions To Preserve

These decisions came from the later narrowing pass and should guide future scans:

- Human review comes before agent/persona review.
- Personas run only when tagged in comments.
- Persona agents comment and propose patches. They do not directly edit documents.
- Persona agents do not edit human comments, resolve threads, mark anything read, or mark review complete.
- Gate, decide, approve, reject, edit, and resolve are human-owned.
- Every accepted write creates a stored version.
- User-facing version labels may distinguish major review rounds from small accepted writes: `v1`, `v1.1`, `v1.2`, `v2`.
- TLDRs may exist at the top of a document but cannot replace reading.
- Read checkpoints should include opened, scroll depth, time-on-doc, and explicit review/readiness attestation.
- Readability scoring and diagram/canvas review are roadmap items, not v1 core.

## Defer Or Park

Do not lead a Read Review scan with these unless the user asks for the expanded scope:

- prompt optimizer;
- dynamic schemas;
- git worktrees;
- multimodal evals;
- model comparison;
- Slack integration;
- full live streaming;
- diagram/canvas editing;
- readability scoring.

They are useful later, but they can distract from the core review loop.

## Search Hints

Useful searches:

```sh
rg -n "draft|proposed|comment|version|export|Git" 2026-04-28-no-vibes-design-docs
rg -n "READ|WRITE|checkpoint|approval|resume" 2025-08-26-claude-for-non-code-workflows
rg -n "event|projection|stream|interrupt|approval" 2025-11-05-event-driven-agents 2025-06-03-humans-as-tools-async
rg -n "skill|subagent|invocation|context" 2026-03-10-claude-agent-skills-deep-dive
rg -n "exact|general|specific|sibling|correct" 2025-09-23-evals-for-classification
```

## CRISPY / Enhanced RPI Workflow

If researching Dexter Horthy's agentic coding methodology (RPI → Q-R-D-S-O-PI → CRISPY):

- `thoughts/shared/research/CRISPY_WORKFLOW_RESEARCH_BRIEF.md`
  - Start here. Synthesizes the MLOps talk with episode transcripts: stage specs, failures, tooling, episode index, `rg` hints, anti-patterns.
- `2026-01-27-no-vibes-allowed/transcript.txt`
  - Canonical live walkthrough of the expanded workflow (Riptide demo).
- `2026-02-10-agentic-backpressure-deep-dive/EPISODE.md`
  - Learning tests (Phase 0) and backpressure in plans.

Note: `HOWTO.md` still describes 3-phase RPI only; episodes are ahead of HOWTO on methodology depth.

## If Asked For Another Scan

Prefer a narrow staged scan:

1. Clarify the target mechanism.
2. Read the matching source cluster above.
3. Extract product rules, implementation candidates, caveats, and deferred ideas.
4. Avoid broad episode summaries unless the user asks for them.
5. Keep source paths in the final output.

