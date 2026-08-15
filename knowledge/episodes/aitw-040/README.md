# Applying 12-Factor Principles to Coding Agent SDKs

Status: curated from the existing upstream transcript and supporting repository
files. Claim verification is transcript first. The transcript source, model,
cleanup history, and exact recording start are not recorded upstream.

Source episode: [`2026-01-13-applying-12-factor-principles-to-coding-agent-sdks`](../../../2026-01-13-applying-12-factor-principles-to-coding-agent-sdks)

## Purpose, audience, and message

Purpose: Show how to make coding agent workflows more consistent by moving known
control flow out of prompts and into code, while keeping agent loops for work that
still needs judgment.

Audience: Engineers building coding agents, agent SDK workflows, or team processes
for research, planning, implementation, and review.

Message: Use deterministic code for known phase transitions, structured outputs as
workflow state, and small agent contexts for uncertain work. Add human or automated
checks at the points where an error would create expensive downstream work.

## How the system works

The main example divides planning into design discussion, structure outline, and
plan writing. Each phase has a smaller prompt and a structured result. Code checks
the result, such as whether open questions remain, before moving to the next phase.
This replaces one long prompt whose instructions and context compete for the
model's attention.

The episode also shows a bounded Ralph loop, a team workflow that stores research,
plans, and task state as Markdown and JSON, and background checks that can warn a
human without blocking the main path. Supporting files include the demo source,
event logs, `IMPLEMENTATION_PLAN.md`, and the one task per loop instructions in
`RALPH.md`.

## Tactical practices

- If the order of operations is already known, encode it in code instead of adding
  more prompt instructions. See 13:20 to 15:00 and 01:14:30 to 01:15:13.
- Split a long workflow into phases with separate prompts and structured output
  schemas. See 24:00 to 28:45.
- Keep resolved decisions in structured state and advance only when the phase exit
  condition is met. See 27:11 to 28:45 and 37:20 to 43:37.
- Start broad when the input space is unknown. Codify common paths after real usage
  shows which cases repeat, and retain an agentic escape hatch for the rest. See
  29:19 to 32:20.
- Put a human, evaluator, or background agent at checkpoints where it can prevent
  downstream rework. See 32:37 to 36:44.
- Review a short structure outline rather than a long implementation plan when the
  goal is mental alignment. See 01:04:54 to 01:06:43.
- Make architecture constraints executable with dependency checks, and keep build
  output warning free to reduce agent context noise. See 01:00:32 to 01:03:22.
- Decide which work must be synchronous and which verification can run in the
  background. See 01:15:41 to 01:16:35.

## Failure modes and limits

- Step errors compound across long autonomous runs, even when each decision is
  usually correct. See 07:15 to 09:33.
- Long planning contexts make late feedback lower leverage and can cause partial,
  inconsistent edits. See 18:26 to 23:37.
- Models can skip instructions inside large prompts, especially when many rules are
  marked important. See 23:59 to 25:57.
- More structure reduces fluidity and can impose one person's workflow on a team.
  Mike's workflow was only 24 hours old, so its team results were not established.
  See 42:26 to 45:10 and 52:32 to 56:48.
- A judge or checkpoint adds latency. Background checks can reduce blocking, but
  the product still needs a clear way to handle late findings.
- The live structured planning demo used alpha code and initially called the wrong
  interaction mechanism. See 38:45 to 42:10.
- The supporting BurritoOps plan reports completion and test results generated
  during an agent run. Those reports were not independently rerun for this packet.

## Sources and uncertainty

Primary evidence: [source transcript](../../../2026-01-13-applying-12-factor-principles-to-coding-agent-sdks/transcript.md),
[episode metadata](../../../2026-01-13-applying-12-factor-principles-to-coding-agent-sdks/meta.md), and
[source README](../../../2026-01-13-applying-12-factor-principles-to-coding-agent-sdks/README.md).
Supporting evidence includes [the implementation plan](../../../2026-01-13-applying-12-factor-principles-to-coding-agent-sdks/IMPLEMENTATION_PLAN.md),
[Ralph loop instructions](../../../2026-01-13-applying-12-factor-principles-to-coding-agent-sdks/RALPH.md),
[episode email](../../../2026-01-13-applying-12-factor-principles-to-coding-agent-sdks/email.md),
[whiteboard links](../../../2026-01-13-applying-12-factor-principles-to-coding-agent-sdks/whiteboards.md),
demo source, and saved workflow logs.

Several numerical examples and tool results are speaker reports. The episode mixes
conceptual advice, unfinished live code, a guest's day old workflow, and later demos.
Treat the design rules as informed practices, not measured universal results.
