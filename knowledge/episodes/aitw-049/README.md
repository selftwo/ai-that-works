# Prompt Injections and Guardrails

Status: curated from the existing upstream timestamped transcript. Claims are transcript observations, not independent tests of the demonstrated systems.

Source episode: [2026-03-17-prompt-injections-guardrails](../../../2026-03-17-prompt-injections-guardrails)

## Purpose, audience, and message

Purpose: Explain prompt injection as a system security problem and demonstrate layered controls.

Audience: Teams giving agents access to untrusted content, private data, or tools that can communicate externally.

Message: Break at least one side of the untrusted input, private data, and external action combination, then validate model output before it reaches tools or users.

## Tactical practices

- Model severe prompt injection risk as the combination of untrusted content, private data access, and external communication. See 00:06:59 to 00:07:34.
- Reduce risk by removing production data access, restricting network egress, or placing a human or model guard before action. See 00:07:34 to 00:10:11.
- Add deterministic output checks for content that should never be shown or passed onward. See 00:25:39 to 00:27:00.

## Failures, limits, and uncertainty

- A context window containing retrieved or tool supplied content cannot be treated as fully trusted. See 00:10:11 to 00:10:43.
- Structured output can constrain shape, but the episode demonstration challenges the claim that structure alone prevents data leakage. See 00:10:11 to 00:17:19.
- A single successful injection can still create a serious security failure even when model providers add defenses. See 00:17:19 to 00:20:57.

## Sources and uncertainty

Primary evidence: [transcript](../../../2026-03-17-prompt-injections-guardrails/transcript.txt), [metadata](../../../2026-03-17-prompt-injections-guardrails/meta.md), and [source README](../../../2026-03-17-prompt-injections-guardrails/README.md). Supporting files are listed in [source-materials.json](source-materials.json). Speaker claims, demos, and generated artifacts were not independently reproduced. The transcript source model and cleanup history are not recorded upstream.
