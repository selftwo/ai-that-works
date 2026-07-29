# Evaluating Prompts Across Models

Status: curated from imported YouTube captions and evaluation code.

Source episode: [`2025-07-29-eval-many-models-same-prompt`](../../../2025-07-29-eval-many-models-same-prompt)

## Purpose, audience, and message

Purpose: Build a small comparison tool for deciding whether a new model fits a real application.

Audience: AI teams choosing models for established prompts and user experiences.

Message: Evaluate models on your own tasks and inspect quality, speed, and cost together. Start with a focused comparison interface rather than a universal eval platform.

## Tactical practices

- Keep a private benchmark made from representative application inputs. See 03:30 to 04:22.
- Define the business behavior that counts as accurate before scoring. See 08:31 to 16:18.
- Run the same prompt and examples across several configured models. See 18:44 to 30:12.
- Record latency and cost alongside output. See 31:08 to 38:47.
- Compare outputs side by side and keep human judgment for subjective quality. See 39:20 to 50:31.
- Build a focused tool for the current decision, then automate repeated runs. See 52:08 to 01:02:42.

## Failure modes and limits

- Public model benchmarks may not represent the product task.
- One accuracy score can hide user experience costs from slow output.
- A general eval UI can add parameters before the team knows which comparison matters.
- Human preference judgments need stable criteria to remain comparable.

## Sources and uncertainty

Evidence: [captions](transcripts/stitched.txt), [README](../../../2025-07-29-eval-many-models-same-prompt/README.md), BAML model and test files, and the Streamlit interface. Results shown live were not preserved as a full benchmark report.
