# Prompting Is Becoming a Product Surface

Status: curated from the existing upstream timestamped transcript. Claims are transcript observations, not independent tests of the demonstrated systems.

Source episode: [2026-02-03-prompting-is-becoming-a-product-surface](../../../2026-02-03-prompting-is-becoming-a-product-surface)

## Purpose, audience, and message

Purpose: Show how a product can let users express desired output without exposing prompt or schema implementation details.

Audience: Product and AI teams building configurable extraction or generation workflows for domain users.

Message: Translate user intent into a stored schema, keep rendering choices separate from model output, and give users safe ways to revise that schema.

## Tactical practices

- Use domain language in the product surface instead of exposing developer terms such as object or JSON schema. See 00:03:02 to 00:05:26.
- Represent both the requested field type and how the product should render it. See 00:03:02 to 00:05:26.
- Mix fixed fields with dynamic user configured fields and add guardrails around invalid configurations. See 00:10:13 to 00:11:55.
- Convert a plain language request into a schema once, store it, and reuse it for later inputs. See 00:18:56 to 00:20:54.
- Keep display only properties in the schema without passing them into the model output contract. See 00:20:54 to 00:25:16.
- Let a user revise a saved schema through a form or a chat based amendment flow. See 00:31:00 to 00:33:06.

## Failures, limits, and uncertainty

- A live demo failed when code treated a generated model object as a subscriptable dictionary. See 00:27:27 to 00:30:38.

## Sources and uncertainty

Primary evidence: [transcript](../../../2026-02-03-prompting-is-becoming-a-product-surface/transcript.txt), [metadata](../../../2026-02-03-prompting-is-becoming-a-product-surface/meta.md), and [source README](../../../2026-02-03-prompting-is-becoming-a-product-surface/README.md). Supporting files are listed in [source-materials.json](source-materials.json). Speaker claims, demos, and generated artifacts were not independently reproduced. The transcript source model and cleanup history are not recorded upstream.
