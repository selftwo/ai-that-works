# Using Subagents Effectively

Synthesis from raw transcripts, not the curated `knowledge/episodes/*/claims.jsonl`
layer — that layer only surfaced 3 episodes with subagent content on a keyword
check. A full-transcript scan found 9 episodes with substantial discussion.
This supersedes `analysis/pi-agent-configuration/01-subagents-and-model-routing.md`
as the source for subagent tactics; that file is settings-advisory for one
specific tool (pi) and should be read as a downstream application of the
points below, not a primary source.

Claims are cited by episode GUID and the timestamp given in the transcript
(format varies by episode — some have `HH:MM:SS`, some don't; noted where
absent). Quotes are direct where they're strong one-liners.

## 1. The core mental model: context control, not personas

- `aitw-017` ~00:16:29–00:16:35: "sub agents are not for playing house.
  They're not for anthropomorphizing. They are for exactly one thing, which
  is context control." A subagent gets a fresh context window, does the
  searching/reading, and returns a tight assistant message — the tool-call
  noise never enters the parent's context.
- `aitw-017` ~00:16:45–00:17:07: the subagent "read read read... until it
  finds the thing and then it's going to return an assistant message which
  is pretty tight" — the parent's tool response stays small regardless of
  how much work the subagent did to produce it.
- `aitw-033` 00:59:20: sub-agents handle implementation, testing, and
  validation for a `/phased-implement` command, then "report to the parent
  model," which checks the result again before asking the human to validate.

**This is the same distinction documented in
`analysis/writing-effective-skills.md`:** a subagent solves "too much noise
in this context," a skill solves "this context is missing an instruction."
Confirmed here from a different episode set — not a one-off claim.

## 2. When parallel dispatch works, and when it doesn't

- `aitw-017` 00:17:21–00:18:32: parallel dispatch worked well when writing
  unit tests across cleanly separable types (recursive types, unions,
  classes) — one subagent per type, each building its own context. Result:
  "incredible performance wins... it's not just about speed... accuracy."
- `aitw-020` 00:24:24: "use sub-agents for every single branch" — dispatching
  one subagent per git branch to summarize diffs for release notes, rather
  than one long serial pass.
- `aitw-029` 00:32:11: the Ralph loop prompt allows "up to 50 sub agents,"
  but the speaker notes their CLI defaults to ~5 concurrent — an explicit
  env var change is needed to raise the cap. Don't assume "parallel" means
  unlimited without checking the harness default.
- `aitw-028` 00:26:05 (also in the episode's own README): subagents cannot
  spawn other subagents, by design — "one of the key things I had to stop it
  from doing," specifically to guarantee safety against runaway recursive
  fan-out. Subagents also get a lower iteration cap than the parent (50 vs.
  999 in this implementation).
- **Failure mode, `aitw-027` 00:31:38–00:32:16:** on complex tasks, if a
  subagent doesn't find what it needs in the first six calls, it tends to
  spawn six more — and by then "your context window is getting kind of bad
  and your plan's going to be low quality." The stated fix is skipping the
  research/subagent phase entirely for simple tasks rather than letting
  greedy sequential dispatch degrade the parent's context.
- **Failure mode, `aitw-027` 01:56:07–01:56:44:** a build-tool-level lock
  (Rust/Cargo, testing within the same package) blocked subagents from
  running tests in parallel — a concrete, non-obvious way "parallel"
  subagents silently become serial or fail.

## 3. Delegation prompt quality

- `aitw-023` 00:47:58–00:48:37: say "task," not "sub-agent," when prompting
  — "task" is the actual tool name exposed to the model, and that framing
  is more likely to produce the intended effect. Also: put explicit
  instructions for *how to prompt the subagent* inside the delegation
  prompt itself, to get more specific output back.
- `aitw-023` 00:07:04–00:08:27: tool/subagent naming materially affects
  invocation accuracy — cited as the reason Anthropic renamed their default
  subagent tool from a narrower name to "general-purpose," to disambiguate
  from custom-named subagents.
- `aitw-017` 00:17:31–00:17:44: the only reliable way to get good delegation
  is to explicitly tell the parent "use a sub agent and prompt it like
  this" in the user message — don't assume the model will delegate well
  unprompted.
- `aitw-023` 00:15:51–00:16:04: tools available to a subagent can be
  restricted (allow/disallow lists) to shrink its context and sharpen
  focus, but this is manual and requires understanding how the context
  window is actually being used — not a set-and-forget setting.

## 4. Cost and model tradeoffs

- `aitw-033` 00:18:20–00:19:03: subagents can be pinned to a specific model
  regardless of what the parent uses (in the observed harness, hardcoded to
  a cheaper/faster model in the agent header) — a direct cost lever: reserve
  the stronger model for the orchestrating parent, cheaper models for
  subagent grunt work. The TUI let the speaker inspect exactly what prompt
  was passed to a given subagent and which model it picked.
- `aitw-028` 01:11:14–01:14:34: a weaker model (GPT-5 Mini in this demo)
  failed to correctly emit the subagent tool call under complex
  instructions — a malformed tool call ("returned with tool colon") instead
  of a real invocation. Model capability floor matters for reliable
  subagent dispatch, not just for the work the subagent does once running.

## 5. Context discipline this pattern depends on

- `aitw-027` 00:16:41–00:17:02: resetting to a new context window between
  phases (research → plan → implement) is deliberate, not incidental —
  "these systems generally work better when you get the least amount of
  context you need." Subagents are one mechanism for this; starting a fresh
  parent context between phases is another.
- `aitw-017` 00:13:48–00:14:22: progress/plan files as external memory (path
  + line number, not full search transcripts) serve the same goal —
  avoiding permanent context bloat that persists until compaction.
- **Bias risk, `aitw-018` 00:44:20–00:44:29:** once a model has launched a
  subagent in a conversation, it becomes more likely to launch another —
  the pattern self-reinforces. `/clear` (fresh context) is more reliable
  than trying to talk the model out of a pattern mid-conversation.
- `aitw-027` 01:24:58–01:25:03: for a small pinpoint fix, "steer to the sub
  agents" instead of creating a full research document — a lighter-weight
  alternative to the full research phase when only one fact is needed.

## 6. Observability of subagent behavior

- `aitw-028` README: the TUI shows subagent depth explicitly (`🔄 Launching
  Sub-agent (Level 1)`), supports interrupting a specific subagent, and
  compacts subagent output to reduce clutter — a concrete UX pattern for
  keeping multi-level agent traces legible.
- `aitw-033` 00:18:20: inspecting the exact prompt passed to a subagent (via
  a TUI focus-and-inspect action) is presented as a normal debugging step,
  not an edge case — worth having in any subagent-dispatching tool.

**Inference — connects to `analysis/agent-visibility-and-guardrail-tactics.md`
cluster A:** this depth-tagged, inspectable-prompt UX is a concrete instance
of the "evidence over narration" pattern from the observability episode
(`aitw-064`) — applied specifically to subagent dispatch rather than
production tracing.

## 7. Soft rule of thumb, with a caveat

- `aitw-017` 00:16:52: "we use sub agents mostly for read-only stuff" — a
  soft guideline to reserve subagents for search/research/gather work whose
  value is a compact summary.
- **This loosened in practice by `aitw-033`** (recorded later): the same
  corpus shows subagents handling implementation, testing, and validation
  in a `/phased-implement` flow, with the parent still checking the result.
  Treat "subagents are read-only" as an early-stage default, not a hard
  rule — the corpus itself shows it evolving as harnesses matured.

## Source index

`aitw-033`, `aitw-028`, `aitw-027`, `aitw-017`, `aitw-020`, `aitw-023`,
`aitw-018`, `aitw-029`, `aitw-016`. Full per-episode breakdown available on
request — this document keeps only the tactical synthesis, not every raw
mention.
