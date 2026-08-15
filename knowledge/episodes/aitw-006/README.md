# Policy to Prompt

Status: curated from imported YouTube captions and the Enron email demo files.

Source episode: [`2025-05-20-policies-to-prompts`](../../../2025-05-20-policies-to-prompts)

## Purpose, audience, and message

Purpose: Turn written compliance policy into an inspectable prompt pipeline and improve it with labeled evidence.

Audience: Engineers and policy teams building review or classification systems from prose rules.

Message: Split policy into explicit questions, require evidence for each result, review errors with humans, and use those judgments to revise prompts and tests.

## Tactical practices

- Convert broad policy into separate questions that can each return compliance and evidence. See 03:14 to 05:12.
- Use a public corpus such as Enron email for repeatable development. See 06:21 to 07:06.
- Keep policy checks generic until evidence shows where a specialized check is needed. See 11:57 to 12:16.
- Preserve reasons and evidence, not only a yes or no label. See 04:39 to 05:12.
- Build a review surface where humans mark flagged examples correct or incorrect. See 61:07 to 61:17.
- Turn reviewed errors into a growing evaluation set. See 65:58 to 66:18.

## Failure modes and limits

- Policy prose contains ambiguity that prompt text alone does not remove.
- One giant prompt makes individual policy failures hard to locate.
- A flag without quoted evidence is hard for reviewers to assess.
- Human review can be wasted if judgments are not saved as evaluation cases.
- Enron email is a useful public corpus but may not match a current company or policy distribution.

## Sources and uncertainty

Primary evidence: [caption transcript](transcripts/stitched.txt), [policy prompts](../../../2025-05-20-policies-to-prompts/baml_src), [pipeline](../../../2025-05-20-policies-to-prompts/pipeline.py), and [tests](../../../2025-05-20-policies-to-prompts/test_pipeline.py). Results shown in the live demo were not rerun for this packet.
