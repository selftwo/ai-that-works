# Cracking the Prompting Interview

Status: curated from imported YouTube captions. The captions have timestamps but no reliable speaker labels.

Source episode: [`2025-06-10-cracking-the-prompting-interview`](../../../2025-06-10-cracking-the-prompting-interview)

## Purpose, audience, and message

Purpose: Work through practical prompt design problems and show patterns that make structured outputs easier to validate and use.

Audience: AI engineers who build extraction, classification, citation, diarization, and code generation features.

Message: Shape the output around stable references and explicit types, give ambiguity an escape route, and keep reasoning visible enough to debug.

## Tactical practices

- Replace copied URLs with compact source indexes, then map indexes back in code. See 03:57 to 12:09.
- For diarization, return the dialogue turn index with the speaker rather than reproducing dialogue text. See 13:12 to 20:04.
- Add `Other` or `Unknown` when the supplied labels do not cover every valid answer. See 22:41 to 28:13.
- Ask for reasoning in a separate field or comment so failures can be inspected. See 33:17 to 40:09.
- Put generated code inside a typed string field and preserve its formatting. See 42:31 to 49:18.
- Test prompts on concrete examples and read the complete prompt when output is surprising. See 56:02 to 01:04:36.

## Failure modes and limits

- Asking the model to reproduce long URLs or text creates avoidable copy errors.
- A closed label set forces confident wrong answers when the input is ambiguous.
- Hidden reasoning makes it harder to tell whether the prompt, context, or parser failed.
- The session demonstrates tactics on selected examples. It does not compare them with a controlled benchmark.

## Sources and uncertainty

Primary evidence: [captions](transcripts/stitched.txt), [README](../../../2025-06-10-cracking-the-prompting-interview/README.md), [metadata](../../../2025-06-10-cracking-the-prompting-interview/meta.md), and the example BAML files in the source folder. Exact recording start, caption model, and speaker attribution are unknown.
