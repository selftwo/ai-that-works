# Designing Evals

Status: curated from imported YouTube captions and the lesson plan example.

Source episode: [`2025-05-13-designing-evals`](../../../2025-05-13-designing-evals)

## Purpose, audience, and message

Purpose: Make evaluation concrete by showing how to define cases, answer keys, and checks for an AI pipeline.

Audience: Teams deciding whether a prompt or pipeline change is better and safe to ship.

Message: Start with a small set of cases you understand, state what good means, inspect failures, and keep adding production examples. The evaluation harness is less important than the judgment encoded in its cases and checks.

## Tactical practices

- Write an answer key or rubric for each representative input. See 13:52 to 14:45.
- Evaluate intermediate structured fields, not only the final output. See 23:55 to 24:28.
- Begin with about five cases and read the prompt and outputs closely. See 66:20 to 66:40.
- Add production examples to the golden set on a regular cadence. See 44:03 to 44:24.
- Use runtime checks on production data where a deterministic invariant exists. See 24:15 to 24:28.
- Treat evaluation design as product specification work. See 32:19 to 32:32.

## Failure modes and limits

- A score without an answer key hides what the team values.
- A golden set can be overfit if it is not refreshed with production cases.
- LLM judges can reproduce ambiguity rather than resolve it.
- Large case counts can hide that nobody reads failures.
- High measured accuracy applies only to the covered distribution and checks.

## Sources and uncertainty

Primary evidence: [caption transcript](transcripts/stitched.txt), [source README](../../../2025-05-13-designing-evals/README.md), and [lesson plan BAML](../../../2025-05-13-designing-evals/baml_src/lessonplan.baml). Examples are demonstrations, not independent benchmark results.
