# Agent Visibility and Guardrail Tactics

Cross-episode synthesis of tactics for making agent work legible and trustworthy,
matched against patterns already present in five personal repos: agentsmith,
defkeys, natural-selection, portfolio-site, benirl-workshop. Claims below are
observed statements from transcripts, cited by episode GUID and timestamp span.
Repo connections are inference, labeled as such.

## A. Evidence over narration

- `aitw-064` 00:00:01–00:00:25: when engineers stop reading all generated code,
  execution evidence is needed to know what the code actually did.
- `aitw-064` 00:16:46–00:18:23: wide events preserve enough dimensions to
  investigate unknown failures later, instead of a few predefined metrics.
- `aitw-064` (~00:20:00–00:24:00 span): a trace and flame graph reveal call
  order, repetition, timing, and unexpected branches without reading every
  function first.
- `aitw-064`: missing instrumentation removes the evidence needed for later
  debugging; generated code will not reliably add every trace point on its own.

**Inference:** agentsmith's `Reported<T>` contract (`adapters/contract.ts`) is
this same idea applied to a status UI — it can only say `supported |
unsupported | not-reported`, never invent state. Natural-selection wants to
visualize exactly this kind of evidence (its Process view is a question →
evidence → iteration schema) but has no live event source. `aitw-064`'s "wide
events" model is the missing piece: a concrete shape for the data
natural-selection's stub node (`id:'signatures'`, status `waiting`) is asking
for.

## B. Learning tests: proof work before design commits to an assumption

- `aitw-044` 00:12:36–00:14:13: reading complete API documentation can still
  leave subtle misunderstandings that enter a plan as assumptions.
- `aitw-044` 00:13:30–00:15:42: write a learning test to check how an external
  field or behavior works before building on it.
- `aitw-044` 00:16:30–00:17:59: treat learning tests as proof work during
  research, not as feature implementation.
- `aitw-042` 01:03:37–01:04:47: use tiny proof programs or learning tests when
  a model confidently describes behavior that can be checked at runtime.
- `aitw-046` 00:09:05–00:10:00: use an established learning test pattern and
  shared vocabulary so an agent can reproduce proof work reliably.

**Inference:** none of the five repos have a named "learning test" stage.
Closest analogue: natural-selection's amber dashed iteration loop marks rework
after the fact, but nothing captures the proof-before-commit step this cluster
describes. This is a gap worth naming directly if a new tool gets built.

## C. Guardrail modeling for untrusted content

- `aitw-049` 00:06:59–00:07:34: model severe prompt injection risk as the
  combination of untrusted content, private data access, and external
  communication.
- `aitw-049` 00:07:34–00:10:11: reduce risk by removing production data
  access, restricting network egress, or placing a human or model guard
  before action.
- `aitw-049` 00:10:11–00:17:19: structured output constrains shape, but the
  episode's own demonstration challenges the claim that structure alone
  prevents data leakage.
- `aitw-049` 00:25:39–00:27:00: add deterministic output checks for content
  that should never be shown or passed onward.

**Inference:** agentsmith's human-approval gate before code leaves the repo
for an external model is this exact "human guard before action" pattern
already in production use. defkeys' `AGENT_REVIEW.md` rule — an agent "may
not override the engine action without showing the conflict" — is a
deterministic check in the sense `aitw-049` describes.

## D. Data sensitivity tiers

- `aitw-047` 00:01:47–00:02:17: separate zero-tolerance data from
  contextually sensitive data before designing a redaction system.
- `aitw-047` 00:02:17–00:06:46: handle data with legal liability through a
  software control plane and security analysis, not an LLM prompt.
- `aitw-047` 00:18:53–00:20:30: model redaction as three rule types — static
  rules, dynamic rules from current data, generative rules for ambiguous
  content.

**Inference:** benirl-workshop's `bin/protect-check` (hash baseline of
protected files) is a static rule in this taxonomy. Nothing in the five repos
yet models the "contextual" or "generative" tiers — worth flagging if any
future tool touches real user data.

## E. Harness restraint

- `aitw-054` 00:26:18–00:27:10: exhaust prompt, tool, and context
  improvements in one simple harness before adding another loop.
- `aitw-054` 00:29:08–00:30:05: building a general custom harness means
  competing with large lab teams that continuously evaluate their own tools
  and compaction.
- `aitw-054` 00:29:33–00:33:00: a custom layer is justified only when
  task-specific evidence shows the default harness cannot express or optimize
  the needed behavior.
- `aitw-054` 00:39:00–00:48:00: evals are the durable specification that
  survives changes in models and harness code.

**Inference — worth sitting with, not just filing:** agentsmith and
natural-selection are both custom harness-adjacent tools (a process/agent
dashboard, an agent-session visualizer). Neither repo's docs cite the kind of
task-specific evidence `aitw-054` says should justify building one. That's not
necessarily wrong — these are personal QoL tools, not production
infrastructure — but it's the direct test to apply before extending either
one: what can't be expressed in an existing tool (Claude Code's own session
view, an existing tracer) that justifies a new build?

## F. Subagent and context boundaries

- `aitw-048` 00:11:55–00:17:08: use a subagent when work needs a fresh
  context window and only a short result should return to the parent.
- `aitw-048` 00:19:27–00:20:21: subagent output quality depends on the parent
  delegation prompt and can omit or invent information like any tool call.
- `aitw-048` 00:21:35–00:24:00: role-named subagents can blur execution
  isolation with reusable instructions, encouraging teams to model an
  organization instead of a task boundary.

**Inference:** agentsmith's orchestration log and defkeys' multi-agent task
splits are both doing subagent delegation already, without this shared
vocabulary. `aitw-048`'s warning about role-named subagents blurring
isolation is a direct check against over-personifying agent roles in future
tooling.

## G. Human checkpoint discipline (the "No Vibes Allowed" cluster)

- `aitw-042` 01:21:13–01:24:18: keep research, design, structure, and plan
  documents because they carry decisions into fresh context windows.
- `aitw-042` 01:24:18–01:26:13: approve a structured outline before allowing
  a long implementation loop to run.
- `aitw-017` 00:29:00–00:31:40: incorrect research can survive into later
  work unless a human catches it.
- `aitw-017` 00:33:20–00:36:10: use multiple human checkpoints before code
  review, not just one at the end.
- `aitw-033` 00:00:07–00:00:20: humans must bring product opinions because a
  model cannot replace that thinking.
- `aitw-027` 01:20:41–01:35:46: human review catches naming and design
  problems while agents perform code search and implementation.

**Inference:** this is your strongest existing practice, not a gap.
portfolio-site's multi-stage review workflow (research / plan / implementation
/ wrap-up review, independent reviewer identities) and benirl-workshop's
12-step lifecycle with a human review gate before commit already implement
this cluster closely. The episodes validate the approach rather than reveal a
missing piece here.

## H. Eval design as scenario groups, not booleans

- `aitw-005` 00:13:52–00:14:45: evaluation requires an answer key or rubric
  stating expected behavior per case.
- `aitw-005` 00:23:55–00:24:28: check intermediate pipeline outputs, not only
  the final response.
- `aitw-005` 00:44:03–00:44:24: refresh a golden set by spot-checking
  production data on a cadence; a pipeline can overfit its golden dataset.
- `aitw-051` 00:13:01–00:14:15: group cases into named, product-oriented
  scenarios.
- `aitw-051` 00:13:44–00:14:40: evaluate nondeterministic behavior with
  expected rates and aggregate metrics, not a single boolean result.

**Inference:** defkeys' `learning/EVALUATION.md` (confidence thresholds before
a "weak target" surfaces) is the one place across the five repos already doing
this. It's a template worth reusing wherever the next tool needs to judge
noisy human-performance or model-output data.

## I. Measurement discipline

- `aitw-059` 00:00:01–00:00:18: performance engineering starts with
  measurement and a feedback loop, not intuition.
- `aitw-059` 00:13:01–00:13:25: benchmarks need variance data (standard
  deviation), so noise isn't mistaken for a real change.
- `aitw-059` 00:15:45–00:16:06: persist benchmark results so agents and
  humans can compare runs without re-paying the full benchmark cost.

**Inference:** portfolio-site has `tools/benchmark.mjs` and
`tools/profile.mjs` already; unconfirmed whether either persists variance
data or just point measurements — worth checking before treating it as
already solved.

## What this means for the next build

Three concrete candidates, ranked by how directly they close a gap above
rather than duplicate what already exists:

1. **Give natural-selection a real event source**, shaped by the "wide
   events" model from `aitw-064` (cluster A), instead of hand-copied sample
   data. This is the one place a visibility tool exists but the visibility
   itself doesn't.
2. **Name and template the "learning test" stage** (cluster B) as a shared
   convention — none of the five repos have it, and it's cheap to add before
   the next design commits to an assumption about an external system.
3. Before extending agentsmith or building anything harness-shaped, write
   down the task-specific evidence `aitw-054` asks for (cluster E) — what
   existing tools can't already show you.
