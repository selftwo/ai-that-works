# Subagents and model routing in pi

Status: advisory notes for a manual change you will make in pi's settings.
Not yet applied. Cites episode transcripts by GUID and timestamp, and one
real run already logged in `defkeys/orchestration/2026-07-13-product-build.md`
(read 2026-07-13; check it is still current before relying on it).

**Durability note:** everything below is written at the level of structure
(how many slots, who decides, what pattern), not at the level of specific
models or providers. Models and their capabilities will keep moving. Nothing
here should need to be thrown away because a model got better or a provider
changed — only the model assigned to a slot should ever need to change.

## What you asked for

Three configurable model slots in pi's settings, not fixed subagent personas:

- **Worker** — cheap, fast model. Default for most subagent calls: explore,
  gather, do routine implementation.
- **Advisor** — a stronger model. Used when a subagent is planning, or doing
  critical review, and needs more intelligence than a worker call.
- **Designer** — a model picked for taste in UI and design-type work, used
  when the task is about how something looks or feels, not just whether it
  runs.

All three are just model choices behind a slot name. None of them is a
persona or a fixed job description. The **main agent is the orchestrator**:
it decides, at the moment you tell it to use subagents, which slot(s) to
call, how many, and whether to run them serially or in parallel. Nothing
about which subagent does what is baked in ahead of time — you tell the main
agent "use subagents" for a given task, and it decides the dispatch pattern
in the moment, drawing on whichever of worker/advisor/designer fits.

This replaces an earlier, narrower version of this note that suggested
task-named custom subagents (explore/plan/implement/review) with a model
picked per name. That was closer to the "role-named subagent" pattern the
episode below warns against. Model slots by capability tier, dispatched at
call time by the orchestrator, is the better fit for what you actually want.

## What the episodes say

- `aitw-048` 00:11:55–00:17:08: a subagent is defined by the context
  boundary — fresh context window, short result back to parent — not by a
  job title. This still holds: worker/advisor/designer are capability
  labels for a model, not job titles for a subagent.
- `aitw-048` 00:19:27–00:21:35: a saved, reusable subagent prompt is worth
  defining only when the same stable task will repeat. One-off dispatch
  doesn't need a saved definition — matches you telling the main agent
  "use subagents" ad hoc, rather than baking the decision in.
- `aitw-048` 00:21:35–00:24:00, direct warning: naming subagents after roles
  blurs the task boundary and pushes teams toward modeling an org chart
  instead of a task. This is why the slots below are capability tiers
  (worker/advisor/designer), not named subagent roles — the orchestrator
  picks a slot per task, it doesn't own a permanent cast of subagents.
- `aitw-054` 00:17:45–00:18:40: the episode distinguishes a model-facing
  harness (the loop a single model runs inside) from an outer orchestration
  harness (the layer that dispatches to those loops). Your main agent is
  that outer orchestration harness; worker/advisor/designer calls are the
  model-facing loops it dispatches into.
- `aitw-054` 00:22:13–00:23:20: subagents and larger orchestrators are the
  same repeated work loop at different levels of abstraction — supports
  having one orchestrator decide dispatch rather than nesting fixed
  sub-orchestrators per subagent.
- `aitw-021` 00:38:20–00:41:40: separate supervisors can enforce separate
  rules or validate extracted information — this is the precedent for the
  **worker + validator** pairing: one call produces output, a second call
  (typically an advisor-tier model) checks it, as a pattern the orchestrator
  can invoke, not a fixed subagent pair that always runs together.
- `aitw-034` 00:43:51–00:45:38 and 00:46:30–00:50:46: standardizing the
  shape of parallel outputs makes them easier to compare, but running
  everything in parallel by default adds merge and context overhead —
  parallel dispatch should be a deliberate choice per task, not a default.
- `aitw-039` 00:21:34–00:23:01: for parallel calls sharing a prompt prefix,
  starting one call first to warm the cache before firing the rest in
  parallel can reduce latency — worth checking whether pi's provider(s)
  benefit from this before assuming it matters.
- `aitw-017` 00:19:10–00:21:40: focused subagents researching separate parts
  of a problem, then assembling results into the main context, is already a
  working, ordinary pattern — this is one shape the orchestrator can pick,
  not the only shape.

## What today's real pi run already tells you

`defkeys/orchestration/2026-07-13-product-build.md` records an attempt at
model routing before this note existed: `grok-4.5` for exploration and
planning, `grok-composer-2.5-fast` for implementation, `grok-4.5:high` for
architecture and failure review. It did not run — the environment blocked
sending repository contents to the external Grok service. Work fell back to
Codex agents split by product area, with the root agent owning integration
and review.

**Read on this:** the actual lesson isn't a missing API key (that detail
turned out not to matter and is dropped from this note). The real lesson is
that calling pi headlessly *from inside* another agent runner (Codex, in
that run) adds a layer that can silently block cross-service calls you don't
control. Your stated plan — run the main model from pi itself, rather than
having an outer runner call pi headlessly — sidesteps that layer instead of
patching around it. Treat the failed run as evidence for that plan, not as a
plumbing bug to fix in isolation.

## Concrete checks before changing pi's subagent settings

1. Confirm pi's settings actually expose three independent model slots
   (worker / advisor / designer) that any dispatch call can reference by
   slot name, not by a fixed subagent definition.
2. Confirm the main agent, when you tell it "use subagents," can choose
   serial or parallel dispatch and can choose how many calls to make,
   rather than a fixed number or fixed order being wired in anywhere.
3. Test the worker + validator pattern once as a controlled case: one
   worker-tier call produces output, one advisor-tier call reviews it, and
   you log whether the review call actually catches something the worker
   missed. That log is your evidence the advisor tier is worth the extra
   cost, not a guess.
4. Since you plan to run the main model from pi itself instead of calling
   pi headlessly from Codex, re-check whether the earlier egress block was
   specific to the Codex-hosted run or a property of pi's own network
   policy — if the latter, it will still need addressing once pi is the
   main runner.

## Open questions for the next note

- Does pi let you set worker/advisor/designer once per workspace, or does
  every dispatch call need to name the slot explicitly? Check pi's settings
  directly before assuming either.
- `aitw-048`'s "fork context" case (needs parent context, isolates tool
  noise) is distinct from a subagent (fresh context, short result back).
  Worth checking whether pi has both mechanisms, since the worker/advisor/
  designer slots above assume the fresh-context subagent case specifically.
