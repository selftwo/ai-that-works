# PDFs, Multimodality, Vision Models

Status: partially curated from imported YouTube captions. The available transcript stops at 11:52, so later episode claims come only from repository files and are not included in `claims.jsonl`.

Source episode: [`2025-07-22-multimodality`](../../../2025-07-22-multimodality)

## Purpose, audience, and message

Purpose: Show how controlled PDF preprocessing and deterministic validation improve vision based extraction.

Audience: Teams extracting structured records from scanned or layout heavy documents.

Message: Do not treat PDF upload as a transparent operation. Control page images and cross page context, then validate extracted values with code.

## Tactical practices observed in the available transcript

- Convert and filter pages before extraction rather than sending the raw PDF blindly. See 00:31 to 01:16.
- Remove recurring headers and footers before asking for records. See 01:04 to 01:21 and 03:52 to 07:09.
- Give the current page together with prior page context for split records. See 00:31 to 02:47.
- Use ordinary image operations for repeated layout elements. See 03:52 to 07:09.
- Treat medical and financial extraction as requiring more control than basic OCR. See 10:42 to 11:52.

## Failure modes and limits

- Provider PDF preprocessing hides resolution and tokenization choices.
- Page boundaries split records and can cause omission or duplication.
- Headers can be mistaken for records.
- This transcript is incomplete. Runtime total checks and later demonstrations described in the README were not transcript verified.

## Sources and uncertainty

Evidence: [partial captions](transcripts/stitched.txt), [README](../../../2025-07-22-multimodality/README.md), [implementation](../../../2025-07-22-multimodality/main.py), sample PDF, and page images. The partial transcript is the main uncertainty.
