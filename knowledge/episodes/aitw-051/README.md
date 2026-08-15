# No Vibes Allowed March Edition

Status: curated from the existing upstream timestamped transcript. Claim verification is transcript only. The transcript source, model, cleanup history, and exact recording start are not recorded upstream.

Source episode: [2026-03-31-no-vibes-march](../../../2026-03-31-no-vibes-march)

## Purpose, audience, and message

Purpose: Design an eval framework for nondeterministic agent systems while showing the design process used before implementation.

Audience: Teams building eval infrastructure and engineers directing coding agents on complex work.

Message: Define product scenarios and aggregate metrics, load representative data before execution, and settle the design before asking an agent to implement it.

## Tactical practices

- Name product scenarios instead of relying on one pass or fail assertion.
- Aggregate soft checks across repeated runs.
- Load cases from datasets or production derived stores.
- Collect the full test set before scheduling parallel execution.
- Ask the model for options and preserve human judgment during design.

## Failure modes and limits

- Hand written cases reflect expected behavior and can miss real user traffic.
- Boolean assertions hide useful variance in nondeterministic systems.
- A weak design can expand into a large implementation that is hard to review.

## Sources and uncertainty

Primary evidence: [source transcript](../../../2026-03-31-no-vibes-march/transcript.txt), [episode metadata](../../../2026-03-31-no-vibes-march/meta.md), and [source README](../../../2026-03-31-no-vibes-march/README.md).

Claims describe what the speakers said or demonstrated. Screen only details, reported measurements, exact speaker attribution, and transcript cleanup remain uncertain unless a claim note says otherwise.

