# Building a Prompt Optimizer

Status: curated from the existing upstream transcript. Claim verification is
transcript only. The transcript source, model, cleanup history, and exact recording
start are not recorded upstream.

Source episode: [`2025-12-16-prompt-optimizer`](../../../2025-12-16-prompt-optimizer)

## Purpose, audience, and message

Purpose: Explain genetic Pareto prompt optimization, then show how the Boundary
team adapted it into a visible and editable BAML workflow.

Audience: Developers who build evaluated LLM functions and want prompt improvement
without model fine tuning or a hidden prompt generation system.

Message: An optimizer can explore prompt variants cheaply when it has useful tests,
multiple explicit objectives, constrained edit scope, and human review of the
resulting prompt.

## How the optimizer works

The optimizer begins with the current prompt and evaluates it. An LLM reflects on
test performance and proposes one candidate at a time. When several candidates are
best on different metrics, a merge prompt can combine their strengths. The system
keeps the nondominated candidates on a Pareto frontier and repeats until its budget
or stopping condition is reached.

The BAML implementation extracts the function and reachable types from the syntax
tree. It exposes the reflection, candidate, and merge prompts as BAML source. Its
terminal interface shows prompt variants and metrics, but it changes source only
after the developer selects a candidate.

## Tactical practices

- Build automated feedback before optimization. Without tests or other reliable
  backpressure, the optimizer has no useful direction. See 03:17 to 04:51.
- Optimize every use of shared prompt material together. Improving one function in
  isolation can damage other functions that use the same instruction or type. See
  08:38 to 10:38.
- Treat accuracy, token use, latency, and custom checks as separate objectives.
  Keep candidates that are best on at least one chosen dimension. See 12:18 to
  13:58 and 18:39 to 22:05.
- Give the optimizer a constrained, relevant edit surface. The demo traverses the
  function signature and reachable types rather than sending the whole code base.
  See 30:34 to 31:42 and 34:20 to 35:45.
- Include successful examples, failed examples, test source, and current metrics in
  reflection. A single assertion error can hide later failures in the same test.
  See 34:03 to 40:26.
- Keep optimizer prompts visible and editable. Domain facts, model choice, and
  objective guidance may need local changes. See 31:42 to 33:25 and 41:30 to 43:30.
- Inspect generated prompts before accepting them. Metrics from a small or
  unrepresentative eval set do not reveal every form of overfitting. See 56:31 to
  58:24.
- Preserve application contracts by default. The demonstrated implementation
  changes prompts, descriptions, and aliases, but not generated input or output
  type shapes. See 59:31 to 01:01:18.

## Failure modes and limits

- Shared instructions and types create hidden coupling. Optimizing only one caller
  can improve its score while reducing performance elsewhere.
- Weak or narrow evals can reward an overfit prompt. Human inspection remains a
  separate check.
- A failed assertion alone is incomplete feedback when the same test contains
  later assertions that never ran.
- Candidate generation is costly enough that search needs budgets and selective
  exploration rather than tens of thousands of LLM calls.
- The live demo exposed a custom check problem at about 55:58. The speakers called
  it a probable prerelease bug.
- The implementation shown was a beta. Statements about its interface and behavior
  describe the system on 2025-12-16, not its current release.
- The discussion sometimes confuses or self-corrects names for JEPA and GRPO. This
  packet follows the episode's intended concepts but does not independently verify
  the research terminology.

## Sources and uncertainty

Primary evidence: [source transcript](../../../2025-12-16-prompt-optimizer/transcript.md),
[episode metadata](../../../2025-12-16-prompt-optimizer/meta.md), and
[source README](../../../2025-12-16-prompt-optimizer/README.md).

No code, whiteboard image, optimizer run, or external paper is stored in this
episode folder. Demo results and the reported three day implementation time are
speaker reports. Screen details may be missing from the transcript, and the
transcript contains probable name and technical term errors.
