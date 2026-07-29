# Transcript rollout report

Run date: 2026-07-12

Source commit: recorded in `knowledge/_catalog/episodes.json` and each batch
fingerprint.

## Result

- 68 dated source directories inventoried.
- 64 normal numbered episodes identified.
- 63 episodes now have verified timestamped transcripts.
- 30 transcripts came from the upstream repository.
- 33 transcript sets were imported from YouTube captions in this run.
- Four workshop or unconference folders were excluded from episode transcription.
- One normal episode remains unresolved: `aitw-002`.

## Pilot B

A two minute local clip was extracted at 16 kHz mono and transcribed on CPU with
the cached `tiny.en` and `base.en` Whisper models.

- `tiny.en`: 8.30 seconds wall time.
- `base.en`: 14.61 seconds wall time.
- Both produced JSON, SRT, VTT, TXT, and TSV files with monotonic timestamps.
- `base.en` had slightly better wording in the manual sample comparison and is the
  preferred local fallback for full episodes.

The batch did not require full local Whisper runs because English YouTube captions
were available for every reachable missing episode. The resumable Whisper chunk
test remains relevant only when a future episode has no captions.

## Caption batches

Four chronological batches of eight direct video IDs were attempted. The first
quality gate caught repeated rolling-caption text. The normalizer was fixed and
the schema version was advanced before the batch continued.

After regeneration:

- 31 direct-ID episodes passed.
- One direct-ID episode failed source acquisition because YouTube reports the video
  as unavailable.
- Performance engineering and agent observability were reconciled against the
  official playlist, then both passed.
- All 33 completed runs contain nonempty JSON, SRT, VTT, TXT, and Markdown files.
- Minimum normalized cue count was 332.
- Largest difference between source duration and caption end was 13.28 seconds.

## Unresolved source

`aitw-002`, Reasoning Models vs Prompts, points to YouTube ID `D-pcKduKdYM`.
The official playlist still lists that ID but YouTube reports the video as
unavailable. Earlier schema output is preserved but is not accepted by the current
catalog because the current verification manifest failed. A trusted audio mirror,
caption export, or restored video is needed before this episode can pass.

## Excluded directories

- `2025-05-10-workshop-nyc-twelve-factor-agents`
- `2025-05-17-workshop-sf-twelve-factor-agents`
- `2025-10-12-unconference-sf`
- `2026-04-11-unconf-sf`

These are event or workshop folders rather than numbered podcast episodes. They
remain in the source inventory and can be handled as a separate collection later.
