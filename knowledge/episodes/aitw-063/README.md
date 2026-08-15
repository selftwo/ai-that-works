# Software Factory for Agent Tools

Status: curated from the existing upstream transcript. Claim verification is
transcript only. The transcript source, model, cleanup history, and exact recording
start are not recorded upstream.

Source episode: [`2026-06-23-software-factory-for-agent-tools`](../../../2026-06-23-software-factory-for-agent-tools)

## Purpose, audience, and message

Purpose: Show how Boundary uses small agent loops to make BAML more reliable by
having agents exercise the language, turn trace evidence into reviewed issues, and
then produce reviewed fixes.

Audience: Teams building developer tools or complex software who want practical
patterns for persistent agent feedback loops with human control.

Message: Start with one bounded loop, keep trace evidence and workflow state, put
humans at problem definition and merge gates, and add loops when repeated work or
failure history shows where they help.

## How the system works

A challenge generator gives a BAML coding task to an agent. The system saves the
full chat log. A separate agent turns the trace into a structured report called a
“trophy.” Findings are classified, deduplicated, linked to evidence, and placed in
Linear. A human edits or approves the issue. Approval starts a Cursor coding agent.
GitHub CI and CodeRabbit provide feedback that later agents address. A human merges
when checks pass or intervenes after a bounded number of failed repair loops.

This is an evidence pipeline with a human friendly workflow state store. It is not
one autonomous agent.

## Tactical practices

- Generate realistic tasks and run them against the latest release, independent of
  the release trigger. See 17:19 to 18:32.
- Test discoverability and instructed use with cold and warm starts. See 18:32 to
  21:32. The transcript wording is unclear, but the later explanation confirms that
  cold start tests whether the agent can find and install the skill.
- Preserve the full trace, then use a separate agent to report what worked and what
  failed. See 18:32 to 20:13.
- Separate product bugs from skill or workflow problems. See 20:13 to 20:39.
- Deduplicate findings and attach each new trace as evidence. See 21:38 to 23:43.
- Use a human readable state store for ownership, comments, redraft, approval, and
  history. See 25:38 to 28:46 and 37:47 to 40:25.
- Put the human gate before code generation so problem framing is corrected before
  the PR loop starts. See 25:54 to 28:46.
- Open the PR early and let shared CI run the full suite. Later agents respond to CI
  and review feedback. See 28:46 to 30:37.
- Cap repair attempts. After four or five failed attempts, route the work to a
  human. See 30:37 to 32:32.
- Compare skill variants on the same tasks using success, cost, turns, issue count,
  and trace friction. See 46:20 to 48:25.

## Failure modes and limits

- Agents can misclassify root cause. A missing runtime description was first called
  a skill issue. See 10:10 to 10:47 and 37:53 to 40:25.
- Duplicate runs can flood the tracker without normalized findings and
  deduplication. See 21:38 to 23:43.
- Passing checks does not replace product judgment about names or the right
  implementation layer. See the `array.fill` example at 32:40 to 34:55.
- Repair loops can stall, so they need a retry cap and human escalation state.
- Agent generated changelogs can be useful diagnostics but poor release notes.
- Issues become stale unless another loop retests them after related fixes.
- The current arena used one model, so its skill result may not generalize.

## Sources and uncertainty

Primary evidence: [source transcript](../../../2026-06-23-software-factory-for-agent-tools/transcript.txt),
[episode metadata](../../../2026-06-23-software-factory-for-agent-tools/meta.md), and
[source README](../../../2026-06-23-software-factory-for-agent-tools/README.md).

The transcript contains name and product transcription errors. Speaker labels often
merge Dylan into Vaibhav. Metrics and screen demonstrations are speaker reports and
could not be checked against code or trace exports in this episode folder.
