# Multimodal Evals

Status: curated from the existing upstream transcript and checked against the included receipt evaluator, BAML prompt, dashboard, and saved run summaries. The transcript source and cleanup history are not recorded upstream.

Source episode: [`2025-12-02-multimodal-evals`](../../../2025-12-02-multimodal-evals)

## Purpose, audience, and message

Purpose: Show how to evaluate structured data extracted from real receipt images with deterministic checks, inspect failures, and use them to improve the data model and product workflow.

Audience: Engineers building multimodal extraction systems for documents, receipts, claims, or other images with fields that have structural or mathematical relationships.

Message: Design evals around domain invariants, save inspectable results, and put failing examples beside their source images. Use the failures to learn the data before optimizing prompts, then reuse the same checks at runtime for retries and focused human review.

## How the system works

A BAML function sends a receipt image to a vision model and returns typed receipt data. A separate Python evaluator applies six checks for totals, signs, subtotal consistency, unit price arithmetic, grand total arithmetic, and required fields. Each run saves extraction data and evaluation results as JSON. A Streamlit dashboard compares runs and lets reviewers inspect the image, extracted data, and failed checks together.

The included saved runs preserve the iteration history: different models, added discount fields, retry logic, and larger receipt sets. The final stored run covers 350 receipts, with 349 successful extractions and 327 receipts passing every check.

## Tactical practices

- Start with messy real examples and inspect their variations before assuming the schema. The receipt set exposed taxes, discounts, rounding, blur, and unusual dimensions. See 03:04 to 07:33.
- Define deterministic checks from relationships already present in the output, such as line totals and receipt totals. See 13:23 to 16:15 and 28:44 to 30:34.
- Keep extraction, evaluation, and visualization separate with a shared data contract. This makes new checks cheap to add and lets the dashboard read saved results without rerunning models. See 30:45 to 32:25.
- Write intermediate and final records in a human readable format so people can inspect, resume, and turn failures into golden examples. See 32:25 to 34:48.
- Start with a small set, improve the prompt and output schema together, then expand the data to find new corner cases. See 40:30 to 44:29.
- Make failures easy to open beside the source image and extracted JSON. The value of the dashboard is rapid error understanding, not the charts alone. See 44:29 to 48:22.
- Do not optimize against a check until a person confirms that the check represents the desired outcome. Real negative discounts show how an apparently simple rule can be wrong. See 45:29 to 49:59.
- Turn reliable offline checks into runtime guardrails. Retry with the specific error, cap attempts, and ask a human to review only unresolved cases. See 49:59 to 53:35.
- Treat eval definitions as product knowledge. External services can run or display evals, but the domain-specific metrics remain the team's responsibility. See 55:33 to 01:00:18.

## Failure modes and limits

- OCR or vision extraction can lose layout, miss fields, double count amounts, or treat a discount as a purchased item.
- A deterministic check can encode the wrong rule. Discounts and rounding may be negative, and regional receipt conventions vary.
- High check pass rates do not prove exact transcription of every field. Several checks share extracted values and can agree on the same wrong interpretation.
- Prompt optimization can overfit to faulty labels or incomplete checks before the team understands the data.
- Model comparisons in the episode use this dataset and prompt. The reported advantage of Gemini 2.5 Flash is not a general benchmark.
- Retries can hide transient extraction failures but do not correct a wrong schema or an invalid eval.
- The checked-in BAML schema has several fields commented out while the Python evaluator references generated types that contain them. This makes the exact generated-client state unclear from the current source tree.
- The saved run summaries verify reported counts, but receipt images and generated client files are not checked in, so the end-to-end pipeline was not rerun.

## Sources and uncertainty

Primary evidence: [source transcript](../../../2025-12-02-multimodal-evals/transcript.md), [episode metadata](../../../2025-12-02-multimodal-evals/meta.md), and [source README](../../../2025-12-02-multimodal-evals/README.md).

Implementation evidence: [BAML extraction prompt](../../../2025-12-02-multimodal-evals/baml_src/receipts.baml), [receipt evaluator](../../../2025-12-02-multimodal-evals/src/receipt_evaluator.py), [dashboard](../../../2025-12-02-multimodal-evals/src/streamlit_app.py), and the saved `results/` summaries. Exact recording start, transcript model, transcript cleanup history, and screen-only receipt details remain uncertain.
