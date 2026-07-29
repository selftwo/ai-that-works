# OpenAI Tells You Not to Build Your Own Harness

Status: curated from the existing upstream timestamped transcript. Claim verification is transcript only. The transcript source, model, cleanup history, and exact recording start are not recorded upstream.

Source episode: [2026-05-05-openai-tells-you-not-to-build-your-own-harness](../../../2026-05-05-openai-tells-you-not-to-build-your-own-harness)

## Purpose, audience, and message

Purpose: Test the claim that model labs will erase the advantage of alternative coding harnesses through post training.

Audience: Builders choosing between a lab supplied coding agent and custom tool or orchestration layers.

Message: Post training gives model native tool shapes a real edge, but builders can still gain advantage through domain specific outer loops, observable interfaces, and difficult structured outputs.

## Tactical practices

- Separate the inner tool harness from domain specific outer orchestration.
- Measure small per call differences across the full task length.
- Inspect the tool interface that actually runs on the user's machine.
- Keep evals stable while models and harness implementations change.
- Use custom structured output methods where the schema creates known failures.

## Failure modes and limits

- A small tool accuracy loss compounds across hundreds of calls.
- Claims of secret local harness advantage are weak when the API surface is observable.
- Optimization against one benchmark can overfit rather than improve the target workflow.

## Sources and uncertainty

Primary evidence: [source transcript](../../../2026-05-05-openai-tells-you-not-to-build-your-own-harness/transcript.txt), [episode metadata](../../../2026-05-05-openai-tells-you-not-to-build-your-own-harness/meta.md), and [source README](../../../2026-05-05-openai-tells-you-not-to-build-your-own-harness/README.md).

Claims describe what the speakers said or demonstrated. Screen only details, reported measurements, exact speaker attribution, and transcript cleanup remain uncertain unless a claim note says otherwise.

