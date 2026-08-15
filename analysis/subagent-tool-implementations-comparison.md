# Three Shipped Pi Subagent Extensions, Compared Against Our Notes

Compares three real, installable pi extensions against
`analysis/using-subagents-effectively.md` (corpus-derived),
`analysis/subagent-first-principles-external-comparison.md` (external doc +
web-verified), and Pi's own in-progress design brainstorm (pasted into
conversation, not yet a file). Unlike the external research document, these
are inspectable source code and documentation, fetched directly — claims
below are checked against actual README/design-doc content, not secondhand
description.

- **`nicobailon/pi-subagents`** — 2552 stars, pushed 2026-07-10. Natural-
  language delegation, named persona agents, adversarial watchdog.
- **`tintinweb/pi-subagents`** — 624 stars, pushed 2026-07-13. Claude-Code-
  style tool names, worktree isolation, scheduling.
- **`davis7dotsh/my-pi-setup/extensions/subagents`** — 415 stars, pushed
  2026-07-14. Multi-backend (pi / Claude Code / Codex) behind one
  normalized interface, Effect-based service architecture.

## The one finding that resolves an open disagreement

**Pi's principle 12 ("treat slots as model choices, not personas") and the
corpus's role-naming warning (`aitw-048` 00:21:35–00:24:00) are both partly
wrong in practice.** The most popular of the three extensions by a wide
margin (4x the next one) is built entirely around named persona agents —
`scout`, `researcher`, `planner`, `worker`, `reviewer`, `oracle`,
`context-builder`, `delegate` — invoked in plain language ("Ask oracle for a
second opinion"). This isn't a fringe design; it's the dominant one by
adoption.

The resolution: the corpus warning is about **identity accumulating memory
and standing trust**, not about naming itself. `oracle` doesn't remember
previous calls — it's a stateless prompt-and-tool template with a name
attached for discoverability. Named roles are fine as long as invoking
`reviewer` twice doesn't carry state between calls and doesn't grant the
second call more trust because "it's the same reviewer as last time." Pi's
principle 12 should be rewritten: not "no personas," but "no *persistent*
personas" — a name is a UI/discoverability convenience over a stateless
template, never an identity with memory.

## The verifier/builder separation is already a shipped feature, not just research

This is the strongest single validation across everything gathered so far.
`nicobailon/pi-subagents` has an explicit **watchdog**: an opt-in
adversarial change reviewer, architecturally distinct from the `reviewer`
subagent, that by design should run a **different, complementary strong
model** than whatever the main session is using. The extension ships a
`/subagents-watchdog recommend-model` command that actively pairs models
against each other (e.g., "if your main session uses Opus 4.8, the watchdog
should use GPT 5.5, and vice versa").

This is Anthropic's trust-escalation research (cited in the external-
comparison doc, §7) turned into a real, adopted feature — independently
converged on, not copied from Anthropic's writeup. It also refines the
recommendation from the prior conversation: don't just say "verify should
use a different model tier," build the model-pairing logic into the tool
itself so it's not something a user has to remember to configure by hand.

The watchdog is also **edit-gated**, not run-every-turn: it fires only when
the repo's final state actually changed since the turn started, coalesces
multiple edits in one turn into one review, and skips reverted/unchanged
diffs. This is a concrete, cheap answer to the "verify everything" cost
problem — review triggers on evidence of a state change, not on a fixed
schedule.

## "Frontier capability readiness" has a concrete answer: backend abstraction, not a bigger model list

This is the direct answer to the actual ask in the last turn.
`davis7dotsh/my-pi-setup` doesn't just add more models to pick from — it
defines a `SubagentBackend` service interface with three implementations
(`pi`, `claude` via the Claude Agent SDK, `codex` via `codex app-server`),
each normalized into one `SubagentEvent` stream
(`RunStarted`/`AssistantDelta`/`ToolStart`/`ToolEnd`/`UsageChanged`/
`RunSettled`/...). A subagent task doesn't have to run inside pi's own
model slots at all — it can be handed to an entirely different coding
agent product as the execution backend, and the manager/UI/tools don't know
or care which one produced the events.

This is what "frontier readiness" actually buys you: when a new frontier
model ships inside a different harness (say, GPT-5.6's own native parallel-
subagent "ultra mode," confirmed real in the external-comparison doc's
verification pass), Pi doesn't need to reimplement that capability — it
can add one more backend file and let that harness's own orchestration
run underneath a normalized event contract. The design doc states this
explicitly as a goal: "Adding a 4th backend = one new file and one line in
the registry layer."

This should reframe the guidance to Pi: **the task-type × model-tier preset
table from the previous turn is still useful, but it's solving the wrong
layer of the problem if "frontier readiness" is the goal.** The preset
table picks a model *within* pi. A backend abstraction picks which
*harness* executes the task, of which "run inside pi with model X" is only
one option. These aren't mutually exclusive — presets could select a
(backend, model) pair instead of just a model — but the backend axis is the
one that actually answers "stay ready as frontier capabilities move."

## Concrete answers to Pi's open questions

- **Q9 (same working tree vs. worktrees):** `tintinweb/pi-subagents` ships
  `isolation: worktree` per-agent-type frontmatter — runs the agent in an
  isolated git worktree, auto-commits changes to a branch on completion.
  This is a direct, shipped solution to the exact failure mode the corpus
  documents in `aitw-027` (a Cargo/Rust build lock blocking parallel
  subagents testing the same package) — isolate the working tree, not just
  the context window. Answer: yes, support worktree isolation, and make it
  an opt-in per-agent-type setting, not a global default (matches
  `tintinweb`'s choice — most agent types don't need it, implementation
  agents touching shared files do).
- **Q5 (parent's full system prompt vs. clean task-specific prompt):**
  `tintinweb/pi-subagents` doesn't pick one — it exposes `prompt_mode:
  "replace" | "append"` per agent type. Their `general-purpose` type
  defaults to `append` (full parent prompt, a "parent twin" that follows
  the same AGENTS.md/CLAUDE.md rules); their read-only `Explore`/`Plan`
  types default to `replace` (standalone, tailored prompt). Answer: this
  isn't a single design decision, it's a per-agent-type setting, and the
  corpus's read-only research tasks and the write-capable "parent twin"
  case genuinely want different answers.
- **Q3 (explicit slot vs. inferred):** partially answered by all three —
  every agent type has a *default* model but every one of the three
  extensions lets a per-call override win. `nicobailon` additionally has a
  `modelScope` allowlist that can hard-error on a caller-supplied
  out-of-scope model while only warning on a frontmatter-pinned one — a
  governance layer neither Pi's brainstorm nor the earlier research
  considered. Worth adding to Pi's design: a model-scope enforcement
  concept for anyone running this in a cost- or compliance-sensitive
  setting, even if off by default.
- **Q7 (report length):** none of the three hardcode a word count. Instead
  they truncate with explicit budgets and a pointer to the full transcript
  file (`davis7dotsh`: 24KB/600 lines with a session-file pointer;
  `nicobailon`: 48KB total/16KB per agent with per-section `[omitted: ...]`
  fallbacks). Answer: don't pick a fixed word limit, pick a byte/line
  budget with graceful truncation and always leave a pointer to the full
  transcript on disk — matches Pi's own "keep full execution details for
  TUI expansion" instinct, just made concrete.
- **Q8 (do full traces persist or exist only while running):** all three
  persist. `davis7dotsh` writes a session file per backend (pi session
  file, Claude JSONL, Codex rollout path); `tintinweb` streams to
  `.pi/output/agent-<id>.jsonl`; `nicobailon` writes `status.json` +
  `events.jsonl` + per-output logs to an async directory, explicitly
  designed for "workflow gates" — other tooling can read these files to
  make decisions. Answer: persist, and treat the files as a stable
  machine-readable contract (`nicobailon` versions its event schema —
  `lifecycleArtifactVersion` — specifically so consumers don't break when
  the format evolves).

## A gap in Pi's brainstorm that none of the three research docs caught

**Graceful degradation at the turn/budget limit.** `tintinweb/pi-subagents`
gives an agent a "wrap up" warning before a hard abort, producing a clean
partial result instead of truncated garbage mid-sentence. Neither the
corpus, the external-comparison doc's stopping-condition section, nor Pi's
own brainstorm mentions this. It's a small, cheap, concrete implementation
of the "a budget running out isn't the same as being done" principle from
the external doc (§6, Symphony's Human Review handoff state) — instead of
the report silently getting cut off, the agent gets one more turn
specifically to summarize where it got to. Worth adding to the delegation
envelope design directly: reserve the last turn (or last N% of budget) for
a forced wrap-up pass, not an abrupt stop.

## What to actually tell Pi, in priority order

1. Rewrite principle 12: personas are fine if they're stateless templates,
   not standing identities. Naming isn't the risk; accumulated memory and
   trust-by-familiarity are.
2. Build the watchdog concept explicitly — not just a `review` mode, but a
   named, edit-gated, cross-model-paired adversarial reviewer, closely
   modeled on `nicobailon`'s implementation since it's the most validated
   version of this idea across everything gathered so far.
3. Reframe "frontier readiness" as a backend abstraction question, not a
   model-slot question — look at `davis7dotsh`'s `SubagentBackend`
   interface as the concrete shape, even if Pi's v1 only implements the
   `pi` backend. Design the interface for a second backend from day one so
   it isn't a rewrite later.
4. Answer Q9 with opt-in worktree isolation per agent/task type (from
   `tintinweb`), Q5 with a `prompt_mode` field instead of a single fixed
   answer (from `tintinweb`), and Q7/Q8 with byte-budgeted truncation plus
   persisted, versioned transcript files (from both `nicobailon` and
   `davis7dotsh`) instead of a fixed word count.
5. Add a forced wrap-up turn before hard abort — the one genuinely new gap
   none of the prior research surfaced.
