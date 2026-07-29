# Prompting With Current Models

Synthesis of tactical prompting advice across five episodes. No single
episode is "the latest technique" doc — this is a recurring thread pulled
from `aitw-009`, `aitw-002`, `aitw-036`, `aitw-057`, and `aitw-043`. Claims
cited by GUID and timestamp where mined from transcript; quotes marked "host
notes" come from each episode's own source README, which in most cases is
more specific than the curated claims.jsonl.

## Structural techniques (aitw-009, Cracking the Prompting Interview)

Host notes, `2025-06-10-cracking-the-prompting-interview/README.md`:

- **Use indexes for URLs and citations.** Give the model content tagged with
  simple IDs (`[SOURCE_1]`) and have it output the ID, not the text. Map the
  ID back to the real source in application code. Matches `aitw-009`
  00:03:57–00:12:09: replace source URLs with indexes and map indexes back
  to URLs in application code.
- **Index-based diarization.** For tasks like speaker diarization, have the
  model output the index of the dialogue turn plus the identified speaker
  (`{"dialogue_idx": 0, "speaker": "Nurse"}`) rather than asking it to copy
  the turn's text. Matches `aitw-009` 00:13:12–00:20:04.
- **Always include an escape hatch for classification.** Provide context
  upfront and an "Other"/"Unknown" category to handle ambiguous inputs.
  Matches `aitw-009` 00:22:41–00:28:13: classification prompts need an
  escape label for inputs that don't fit the supplied classes.
- **Put reasoning in comments or non-standard fields.** Include the model's
  reasoning as comments or extra fields in structured output, purely to make
  debugging easier. Matches `aitw-009` 00:33:17–00:40:09.
- **Generate code as a markdown-fenced string field**, not raw embedded
  JSON, for higher-quality code output.
- **RTFP — reread the prompt.** When a model follows an unintended
  interpretation, the fix is usually rereading your own prompt for the
  ambiguity, not adding more instructions. Matches `aitw-009`
  00:56:02–01:04:36: review the entire prompt when a model follows an
  unintended interpretation.

## Reasoning models vs. reasoning prompts (aitw-002)

Host notes, `2025-04-07-reasoning-models-vs-prompts/README.md`:

- A cheap, non-reasoning model can be made to reason well just by prompting
  it correctly — a reasoning model isn't always necessary.
- Guided reasoning (a structured prompt that walks the model through steps)
  beats generic `<think>` tokens in general-purpose models, and can improve
  a model that already reasons.
- Time and cost tradeoffs: reach for a reasoning model when you want to move
  fast without hand-tuning prompts; reach for a smaller model with a guided
  prompt when cost, speed, or edge/OSS constraints matter.
- Actor/checker/LLM-as-judge workflows can work but cost scales
  exponentially with each added check — use sparingly.

## Optimizing prompts without breaking shared ones (aitw-036)

- `aitw-036` 00:08:38–00:10:38: optimizing a shared instruction or type for
  only one prompt can over-specialize it and reduce performance in other
  prompts that reuse it. If a system prompt or shared type is used by
  multiple call sites, optimize across all of them, not just the one in
  front of you.
- `aitw-036` 00:56:31–00:58:24: read the generated/optimized prompt
  yourself — a small or unrepresentative eval set can reward accidental
  overfitting even when the metrics look good.
- `aitw-036` 00:37:25–00:40:26: giving an optimizer the full test source
  (not just a failure message) improved its reflection, because one failure
  message can omit other assertions and intended behavior the fix needs to
  respect.
- `aitw-036` 00:03:17–00:04:51: prompt optimization needs automated feedback
  (tests or evals) to direct candidate improvement — optimizing blind
  doesn't work.

## Tool-calling as an extension of prompting (aitw-057, Code Mode Deep Dive)

Host notes, `2026-05-12-code-mode-deep-dive/README.md`:

- **Tool calls are the primitive; MCP, bash, CLIs, and code mode are just
  different expressions of "name + input + output."** Pick the format that
  fits the context, not a permanent architecture.
- **Code mode's biggest win is output shaping.** In bash, extracting one
  field from a command's output means piping through `jq` and hoping the
  model remembers — if it forgets, that's thousands of tokens of noise in
  context. In code mode, intermediate output stays out of context entirely;
  only what you `console.log` reaches the model.
- **A clean OpenAPI spec is the most durable investment** — it converts to
  bash skills, code mode declarations, or MCP tools, so the spec outlives
  whichever harness format is current.
- **Manage a tool catalog, not a tool format.** Think in terms of a catalog
  of named tools with typed inputs/outputs; how you expose that catalog to
  a given model is a swappable implementation detail.

## Prompting as a user-facing product surface (aitw-043)

Thinner source material — the episode's README has no synthesized "Key
Takeaways" section, only whiteboard images. From mined claims:

- `aitw-043` 00:03:02–00:05:26: use domain language in the product surface
  instead of exposing developer terms like "object" or "JSON schema" —
  represent both the requested field type and how the product should render
  it.
- `aitw-043` 00:18:56–00:20:54: convert a plain-language request into a
  schema once, store it, and reuse it for later inputs, rather than
  re-deriving the schema every time.
- `aitw-043` 00:20:54–00:25:16: keep display-only properties in the schema
  without passing them into the model's output contract.

**Gap:** if a whiteboard-image review turns out to add tactics beyond the
above, this section should be revised — the images weren't reviewed for
this synthesis.

## Cross-cutting pattern

Every episode in this set converges on the same discipline: don't guess
whether a prompt or tool format works, check it — reread the prompt when
output goes wrong (`aitw-009`), measure across all consumers before
optimizing a shared prompt (`aitw-036`), read the actual generated prompt
rather than trusting the eval score (`aitw-036`), and treat the tool-calling
format itself as swappable rather than fixed (`aitw-057`). This is the same
"evidence over narration" discipline documented in
`analysis/agent-visibility-and-guardrail-tactics.md`, applied specifically
to prompt and tool design instead of runtime agent behavior.
