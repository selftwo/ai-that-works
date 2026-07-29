# AI That Works Knowledge Layer

This folder holds derived, reviewable knowledge from the upstream episode corpus.
The dated folders at the repository root remain the source. Do not move or rewrite
them as part of this workflow because that would make upstream sync harder.

## Layout

- `_catalog/`: generated coverage and episode indexes
- `episodes/<guid>/`: transcript imports, source inventories, knowledge notes, and run records
- `runs/`: reports for periodic repository refreshes
- `scripts/`: deterministic inventory and catalog tools

Large audio, video, Whisper chunks, and temporary files do not belong here. Keep
them in a separate work directory such as
`/Users/corphr.software/Documents/work/ytt-pam-workspace` and record their hashes
and paths in run manifests.

Every derived claim should record the episode GUID, the episode recording time,
the source commit, and a transcript timestamp or source file path. Treat
`eventDate` as the recording time only when no better recording timestamp exists.
Keep the YouTube publication time separate.

See [PIPELINE.md](PIPELINE.md) for the staged rollout and failure rules.
