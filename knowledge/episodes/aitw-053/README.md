# Agentic Coding for Frontend Apps

Status: curated from the existing upstream timestamped transcript. Claim verification is transcript only. The transcript source, model, cleanup history, and exact recording start are not recorded upstream.

Source episode: [2026-04-14-agentic-coding-for-frontend-apps](../../../2026-04-14-agentic-coding-for-frontend-apps)

## Purpose, audience, and message

Purpose: Show a frontend workflow in which agents can build and inspect real component states before wiring the full application.

Audience: Frontend teams using coding agents for UI implementation and review.

Message: Separate display components from data wiring, model states in Storybook, and make visual output part of the agent feedback loop.

## Tactical practices

- Create Storybook stories during research and design, before full implementation.
- Keep pure render components separate from data fetching wrappers.
- Model loading, empty, error, deletion, and completed states as stories.
- Use browser screenshots to review the same component code an application will ship.
- Wire approved components to application data only after visual behavior is clear.

## Failure modes and limits

- A full application makes isolated visual states slow to reproduce.
- Wired components require API and state mocks that obscure display work.
- A design mock introduces a translation step before the real component exists.

## Sources and uncertainty

Primary evidence: [source transcript](../../../2026-04-14-agentic-coding-for-frontend-apps/transcript.txt), [episode metadata](../../../2026-04-14-agentic-coding-for-frontend-apps/meta.md), and [source README](../../../2026-04-14-agentic-coding-for-frontend-apps/README.md).

Claims describe what the speakers said or demonstrated. Screen only details, reported measurements, exact speaker attribution, and transcript cleanup remain uncertain unless a claim note says otherwise.

