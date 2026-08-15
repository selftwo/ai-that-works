# Dynamic Schemas

Status: curated from imported YouTube captions and checked against the source episode files.

Source episode: [`2025-09-30-dyanmic-schemas`](../../../2025-09-30-dyanmic-schemas)

## Purpose, audience, and message

Purpose: Demonstrate a two stage pipeline that first proposes a schema for unfamiliar content and then extracts data into that schema.

Audience: Teams building document extraction systems or interfaces where the data shape is not known in advance.

Message: Let the model propose structure, but keep schema generation, extraction, rendering, and validation as separate steps that can be inspected.

## Practical knowledge

- Ask for a schema before asking for extracted values. See 03:30 to 06:14.
- Pass the generated schema back as a typed extraction target. See 05:40 to 07:16.
- Render from the same schema rather than inventing a separate UI contract. See 08:10 to 09:22.
- Treat schema generation as a loop that can be refined, not a one shot answer. See 09:48 to 10:08.
- Keep the dynamic type boundary explicit in the backend and stream useful intermediate results to the frontend.

## Failure modes and limits

- A plausible schema can still omit important content or choose the wrong level of detail.
- Generated UI code adds another untrusted generation step and needs validation.
- The episode is a live prototype, not production evidence about accuracy or latency.
- Imported captions lack reliable speaker labels and contain errors in product names.

## Sources and uncertainty

Primary evidence is the [timestamped caption transcript](transcripts/stitched.txt). The source README and implementation files explain the intended architecture. Exact recording time and caption generation details are not known.
