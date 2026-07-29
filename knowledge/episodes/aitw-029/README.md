# Ralph Wiggum under the hood: Coding Agent Power Tools

Status: curated from imported YouTube captions and checked against the source episode files.

Source episode: [`2025-10-28-ralph-wiggum-coding-agent-power-tools`](../../../2025-10-28-ralph-wiggum-coding-agent-power-tools)

## Purpose, audience, and message

Purpose: Explain and demonstrate a small outer loop that gives a coding agent one bounded step at a time.

Audience: Developers designing coding agent harnesses for greenfield work, refactors, research, or specification recovery.

Message: Fresh short contexts can produce sustained progress when the desired state is explicit, checks provide back pressure, progress is recorded, and each successful loop creates a rollback point.

## Practical knowledge

- Start a fresh context instead of letting one chat degrade over a long run. See 07:03 to 07:38.
- Review specifications carefully because one bad requirement can multiply into large amounts of bad code. See 17:15 to 20:11.
- Use tests, builds, type checks, and security checks as back pressure that stops bad generations. See 23:06 to 25:38.
- Give each loop one priority item, require checks, update the plan, then commit. See 31:02 to 31:44.
- End the run after one item so work stays in the useful part of the context window. See 40:58 to 41:55.
- Run the pattern in reverse to derive specifications from an existing system before rebuilding forward. See 47:04 to 48:30.
- Commit after every successful loop so an overrun can be rolled back to the last good state. See 63:58 to 64:25.

## Failure modes and limits

- Weak or incorrect specifications can drive repeated implementation failure at high token cost.
- Checks must be fast enough to run each loop and strong enough to reject a bad change.
- Context spent on large harness prompts or tools leaves less room for the actual task.
- The basic loop does not know when the whole project is done. A human may need to stop it and choose the best commit.
- Clean room reimplementation has legal and policy risks that require advice beyond this episode.

## Sources and uncertainty

Primary evidence is the [timestamped caption transcript](transcripts/stitched.txt). The source README and included prompts and loop scripts show the demonstrated harness. Imported captions contain name and product errors. Performance, cost, and legal claims are speaker reports and were not independently checked.
