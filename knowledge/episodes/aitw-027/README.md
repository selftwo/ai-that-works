# No Vibes Allowed: Live Coding with AI Agents

Status: curated from imported YouTube captions and checked against upstream episode notes.

Source episode: [`2025-10-14-no-vibes-allowed`](../../../2025-10-14-no-vibes-allowed)

## Purpose, audience, and message

Purpose: Demonstrate research, plan, implement on a real timeout feature in a large codebase.

Audience: Engineers using coding agents for changes that cross languages, runtimes, and tests.

Message: Spend context on research and a reviewed plan, then implement in small verified phases with fresh context and human review.

## Practical knowledge

- Refine the desired user contract before researching implementation. See 03:35 to 09:09.
- Produce a research document that compresses codebase facts for planning. See 09:09 to 12:54.
- Resolve timeout semantics and error behavior in the plan before code generation. See 13:31 onward.
- Split work into independently testable phases and verify after each phase.
- Restart with focused context instead of carrying the full conversation through every stage.

## Failure modes and limits

- A vague issue can yield a large amount of internally consistent but wrong code.
- Plans amplify mistakes, so a domain expert must review them before implementation.
- Streaming and composite timeout behavior have different semantics from a basic request timeout.
- The session completed only part of the larger planned feature, despite the successful demonstration.

## Sources and uncertainty

Primary evidence is the [timestamped caption transcript](transcripts/stitched.txt). The source README provides a structured recap. Exact productivity comparisons are speaker estimates, not controlled measurements.
