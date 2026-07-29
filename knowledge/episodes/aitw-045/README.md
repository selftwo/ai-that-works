# AI Content Pipeline Revisited

Status: curated from the existing upstream timestamped transcript. Claims are transcript observations, not independent tests of the demonstrated systems.

Source episode: [2026-02-17-automating-aitw](../../../2026-02-17-automating-aitw)

## Purpose, audience, and message

Purpose: Review the podcast production automation and show where specialized tools and human checkpoints fit.

Audience: Teams automating recurring content and operations work with coding agents, browser agents, and APIs.

Message: Automating most of a workflow is valuable when the remaining review and risky actions stay explicit.

## Tactical practices

- Treat 90 to 95 percent automation as useful when the generated result still needs one human review pass. See 00:16:04 to 00:19:03.
- Collect a small set of episode inputs once and let the workflow derive later artifacts. See 00:19:03 to 00:21:35.
- Use a browser agent when the service API is unavailable at the current account level. See 00:29:22 to 00:30:38.
- Stop at an explicit human action for settings and asset upload that the browser flow cannot safely finish. See 00:34:51 to 00:35:54.
- Use the service API or CLI for the next step when it is available instead of forcing all work through the browser. See 00:35:54 to 00:36:20.

## Failures, limits, and uncertainty

- Browser automation can enter a loop when similar controls lead to an unexpected product popup. See 00:33:51 to 00:34:51.

## Sources and uncertainty

Primary evidence: [transcript](../../../2026-02-17-automating-aitw/transcript.txt), [metadata](../../../2026-02-17-automating-aitw/meta.md), and [source README](../../../2026-02-17-automating-aitw/README.md). Supporting files are listed in [source-materials.json](source-materials.json). Speaker claims, demos, and generated artifacts were not independently reproduced. The transcript source model and cleanup history are not recorded upstream.
