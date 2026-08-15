# No Vibes Allowed February

Status: curated from the existing upstream timestamped transcript. Claims are transcript observations, not independent tests of the demonstrated systems.

Source episode: [2026-02-24-no-vibes-february](../../../2026-02-24-no-vibes-february)

## Purpose, audience, and message

Purpose: Apply proof research and vertical planning while adding queued messages to an agent product.

Audience: Developers building interactive agent systems and teams applying agent workflows to real product work.

Message: Test opaque SDK behavior first, update the design with findings, then implement one observable path before expanding edge cases.

## Tactical practices

- Define queue behavior separately from interruption behavior, including editing and combining queued messages. See 00:02:21 to 00:06:54.
- Ask for exactly one small test that exercises tool use and a queued followup against the real SDK. See 00:06:54 to 00:09:05.
- Use an established learning test pattern and shared vocabulary so an agent can reproduce proof work reliably. See 00:09:05 to 00:10:00.
- Combine code research, web research, and executable proof research before choosing a design. See 00:09:30 to 00:10:50.
- Resolve more assumptions before implementation because design correctness strongly affects implementation correctness. See 00:10:50 to 00:11:30.

## Failures, limits, and uncertainty

- Documentation or its interpretation can be wrong, causing a plan to fail only after implementation has begun. See 00:09:30 to 00:10:50.

## Sources and uncertainty

Primary evidence: [transcript](../../../2026-02-24-no-vibes-february/transcript.txt), [metadata](../../../2026-02-24-no-vibes-february/meta.md), and [source README](../../../2026-02-24-no-vibes-february/README.md). Supporting files are listed in [source-materials.json](source-materials.json). Speaker claims, demos, and generated artifacts were not independently reproduced. The transcript source model and cleanup history are not recorded upstream.
