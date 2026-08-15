# Episode Knowledge Pipeline

## Goal

Build a local, queryable record of the practical lessons in each AI That Works
episode. Preserve the source evidence and make uncertainty visible.

## Layers

1. Source: the upstream episode folders at the repository root.
2. Knowledge: transcripts, episode notes, claims, topics, and catalogs in `knowledge/`.
3. Analysis: cross-episode explainers and experiments in `analysis/`.

Supporting code, diagrams, whiteboards, and design documents stay in their source
episode folders. Knowledge files link to them. Event signup and promotion files
are inventoried but excluded from technical analysis unless they add useful facts.

## Stable identity and time

Use the `guid` from `meta.md` or `data.json` as the episode identity. Record these
fields for every curated episode:

- episode GUID, number, title, and source folder
- event or recording time and its provenance
- YouTube video ID and publication time when known
- source Git commit and pipeline observation time
- transcript origin, model or caption source, and timestamp precision

An episode title or planned topic can change. Match videos by explicit video ID
first. Use episode number, date, and title only as evidence. Mark uncertain matches
for review instead of binding them automatically.

## Stages

`inventory -> reconcile-video -> acquire -> probe/chunk -> transcribe/import -> stitch -> verify -> enrich -> review -> publish-catalog`

Each stage writes its input fingerprint and status to a run manifest. Status is one
of `pending`, `running`, `done`, `failed`, `stale`, or `needs_review`. Write output
to a temporary path, validate it, promote it, then write the stage completion
marker. A rerun starts at the first stale or incomplete stage.

The fingerprint includes the source commit, source URL or video ID, input file
size and modification time, duration, transcript hash, model, language, decode
settings, and knowledge schema version.

## Transcript priority

1. Import an existing timestamped source transcript.
2. Import suitable YouTube captions and label them as captions.
3. Run local Whisper with resumable chunks.

For Whisper, probe every input with `ffprobe`, use cumulative real chunk durations
for offsets, and keep raw and adjusted JSON. A chunk is complete only when its
validated output and matching completion marker exist. Benchmark cached `tiny.en`
and `base.en` on a one to three minute CPU sample before a long run.

## Episode knowledge contract

Understand the episode before cleaning its transcript. Each reviewed episode
should contain:

- purpose, audience, and message
- short overview
- tactical practices and when to use them
- failure modes and limits
- tools and supporting source artifacts
- timestamped observed claims
- clearly marked inferred synthesis
- open questions, confidence, and manual corrections

## Verification gate

Do not publish an episode to the global catalog until:

- the source mapping is confirmed
- transcript timestamps are monotonic
- transcript start, middle, and end pass spot checks
- final transcript time is close to source duration when duration is known
- at least five useful claims point to timestamp spans
- a no-change rerun does no transcript work
- a failed refresh does not replace a previously verified artifact

## Rollout

### Pilot A: import and enrich

Use episode 63, `2026-06-23-software-factory-for-agent-tools`. It has a direct
YouTube link and a timestamped source transcript. Test inventory, import,
provenance, episode knowledge, verification, catalog publication, and no-op rerun.

### Pilot B: local transcription

Use a one to three minute clip from a locally available video. Compare cached
`tiny.en` and `base.en` on CPU, verify timestamps and names against captions or a
known transcript, then test resume by removing one chunk completion marker.

### Batch rollout

After both pilots pass, process five to ten episodes per batch. Start with episodes
that have direct YouTube IDs and no transcript. Stop a batch on ambiguous source
mapping, repeated timestamp failure, or catalog schema failure. Publish a coverage
report after each batch.

Preview the eligible queue without network access:

```text
python3 knowledge/scripts/run_transcript_batch.py --limit 5
```

After reviewing that list, allow caption inspection and download explicitly:

```text
python3 knowledge/scripts/run_transcript_batch.py --limit 5 --execute
```

The runner prefers manual English YouTube captions, then automatic English
captions. It writes normalized JSON, SRT, VTT, TXT, and Markdown files under the
episode knowledge folder. If captions are unavailable, the manifest records
`local_whisper_pending`; this command does not download audio or start Whisper.
Run its offline self-checks with:

```text
python3 -m unittest knowledge/scripts/test_run_transcript_batch.py
```

## Periodic refresh

Fetch upstream separately from artifact generation. Record the old and new commit
IDs, scan only changed episode folders and registry files, process new or stale
stages, rebuild catalogs deterministically, and write a report of added, changed,
skipped, failed, and review-needed episodes.
