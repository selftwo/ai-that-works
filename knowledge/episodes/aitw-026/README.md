# Anthropic Post Mortem

Status: curated from imported YouTube captions and checked against upstream episode notes.

Source episode: [`2025-10-07-anthropic-post-mortem`](../../../2025-10-07-anthropic-post-mortem)

## Purpose, audience, and message

Purpose: Use Anthropic incident reports to explain why AI quality failures need deployment controls, product signals, and technical observability.

Audience: Engineers operating model based products in production.

Message: Model output can degrade without normal application errors, so watch user outcome signals, deploy gradually, preserve rollback paths, and test the real usage distribution.

## Practical knowledge

- Larger context windows can change quality and should not be treated as free capacity. See 07:49 to 12:03.
- Floating point and distributed selection details can change the chosen token. See 22:42 to 29:37.
- User reports and social signals can reveal subtle quality regressions. See 30:35 to 31:47.
- Use feature flags and roll back first during an incident. See 33:57 to 35:26.
- Separate infrastructure failures from ordinary model uncertainty, then turn production examples into eval cases.

## Failure modes and limits

- Aggregate error rates can hide severe failures for a small segment.
- Long context may reduce performance on tasks that do not need it.
- The speakers simplify low level inference details while interpreting a public postmortem.
- Claims about incident impact come from the discussed article, not an independent reproduction here.

## Sources and uncertainty

Primary evidence is the [timestamped caption transcript](transcripts/stitched.txt). The source README is a useful structured recap but contains secondary interpretation. Imported captions have transcription errors.
