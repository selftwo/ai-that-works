# No Vibes Allowed: Using CodeLayer to Build CodeLayer

Status: curated from imported YouTube captions and checked against upstream episode metadata.

Source episode: [`2025-11-25-no-vibes-allowed-using-codelayer-to-build-codelayer`](../../../2025-11-25-no-vibes-allowed-using-codelayer-to-build-codelayer)

## Purpose, audience, and message

Purpose: Dogfood CodeLayer while using research, plan, implement on concurrent product changes.

Audience: Engineers managing several coding agent tasks and repeated context switches.

Message: Persist concise task state and separate research from planning so a human can resume work quickly, but do not outsource product choices or review.

## Practical knowledge

- Work on two features to expose the real cost of switching between agent tasks. See 00:00 to 06:38.
- Store a short reminder of the current stage, decisions, and next action. See 05:09 to 06:38.
- Keep unrelated codebase context out of the research and planning window. See 12:34 to 14:40.
- Test the core behavior before moving to a later phase. See 10:54 to 11:39.
- Review diffs and give direct feedback when implementation diverges from the intended design.

## Failure modes and limits

- State summaries can become stale when code or decisions change.
- Two active features increase human review load even when agents run in parallel.
- Models may implement the wrong design when the human does not state an opinion.
- The session is a live dogfooding demonstration, not a controlled productivity test.

## Sources and uncertainty

Primary evidence is the [timestamped caption transcript](transcripts/stitched.txt). The upstream README is brief, so most interpretation comes from the captions. Speaker attribution and screen state are uncertain.
