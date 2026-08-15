# No Vibes Allowed - July Edition

Status: curated from the existing upstream transcript. The episode records a live
design discussion, so the system design and product decisions remain provisional.

Source episode: [`2026-07-21-no-vibes-july`](../../../2026-07-21-no-vibes-july)

## Purpose, audience, and message

Purpose: Work through a proposed shared-memory system for coding agents and show
how a design changes when another experienced builder challenges it in public.

Audience: Teams building agent workflows, shared coding context, or human review
paths around automated suggestions.

Message: Treat shared agent context as a reviewed, evidence-backed team asset.
Use small, focused background checks to propose and maintain it, then fit review
into tools people already use.

## Practical lessons

- Promote repeated, useful team behavior into context; do not let one agent action
  become permanent memory by itself.
- Keep a clear source trail for a proposed rule so reviewers can see the repeated
  user statements and their surrounding task context.
- Route review into an existing inbox such as Slack, and allow a person to refine a
  suggestion rather than forcing a simple approve-or-reject decision.
- Give each background agent one narrow job. A post-tool hook plus a small model
  can supply a useful nudge without a separate autonomous loop.
- Run non-urgent discovery in batch, but use a faster path when a person triggers
  it directly. Optimize only after value and cost are known.

## Failures and uncertainty

The speakers reject several parts of the initial design during the session. Their
preferred final shape should not be treated as an implementation commitment. Names
such as Claude memory, HumanLayer, and BAML may be imperfectly transcribed.

Sources: [timestamped transcript](../../../2026-07-21-no-vibes-july/transcript.txt),
[metadata](../../../2026-07-21-no-vibes-july/meta.md), and
[upstream summary](../../../2026-07-21-no-vibes-july/README.md).
