# Email is All You Need

Status: curated from the existing upstream transcript and supporting editorial
files. Claim verification is transcript first. The transcript source, model,
cleanup history, and exact recording start are not recorded upstream.

Source episode: [`2026-01-20-email-is-all-you-need`](../../../2026-01-20-email-is-all-you-need)

## Purpose, audience, and message

Purpose: Explain why email is a useful agent interface and work through the systems
design needed to handle messy inputs, replies, interruptions, and irreversible
actions.

Audience: Engineers building production agents over email or other asynchronous
channels, especially systems that update records, schedule work, or send messages.

Message: Email can be a universal delegation interface, but a reliable email agent
needs typed ingress, durable event history, queues keyed by conversation, guarded
writes, and full context about actions the system has already taken.

## How the system works

The demonstrated application receives a typed email webhook, verifies it, routes
on the destination address, fetches large bodies or attachments, transforms the
content with an AI function, and sends a response. The production design adds a
durable raw copy, a queue, per-thread serialization, events and actions as separate
state, and verification before database writes, external actions, and replies.

When a correction arrives while earlier work is running, the system checks for a
newer message at a write or send yield point. It discards or rolls back work that
has not escaped, then processes the latest thread state. If an irreversible action
already occurred, the next agent run receives that action as explicit context.

## Tactical practices

- Use email for delegation where users and business records already exist, rather
  than treating it as another chat screen. See 02:35 to 08:43.
- Convert inbound email into a typed, verified event before application logic. See
  17:08 to 18:57 and 35:33 to 36:47.
- Keep large bodies and attachments behind signed URLs so webhook payloads remain
  usable. See 19:21 to 23:36 and 55:34 to 56:30.
- Put received work on a queue so rate limits and concurrency are explicit. See
  38:28 to 42:39.
- Serialize processing by email thread so two messages in one conversation are not
  acted on concurrently. See 44:34 to 47:01.
- Separate events from actions and preserve raw inbound messages before interpreting
  them. See 42:52 to 43:59 and 49:25 to 50:48.
- Verify again before each write or send. If a newer thread message exists, cancel
  the stale run and process the new state. See 47:20 to 51:33.
- Queue planned external actions until commit when possible because an email or
  calendar operation cannot be rolled back like a database transaction. See 48:07
  to 51:54.
- Record outbound actions and inject them into later context when a race lets an
  action escape before a correction arrives. See 51:54 to 54:09.

## Failure modes and limits

- A normal forward may omit authentication headers, reducing confidence in sender
  verification. See 13:51 to 15:20.
- The live extraction test used the wrong route for a message without an image and
  did not return the expected error response. See 15:33 to 19:51.
- Email threads can be edited, branched, or duplicated in quoted text. The inbound
  copy must not be treated as a perfect history. See 49:25 to 50:48 and 54:30 to
  55:34.
- Large threads and attachments can exceed serverless request limits, so raw
  history may need references instead of inline payloads.
- Database rollback does not undo a sent email or created calendar event.
- The demonstrated inbound service was a new proprietary product. Its threading
  API was not yet available during the episode, and the promised open source demo
  code is not present in this episode folder.
- The queue design is a live whiteboard proposal. It was not implemented or load
  tested in the source folder.

## Sources and uncertainty

Primary evidence: [source transcript](../../../2026-01-20-email-is-all-you-need/transcript.txt),
[episode metadata](../../../2026-01-20-email-is-all-you-need/meta.md), and
[source README](../../../2026-01-20-email-is-all-you-need/README.md).
Supporting editorial artifacts are [the episode email](../../../2026-01-20-email-is-all-you-need/email.md)
and [raw generated email summary](../../../2026-01-20-email-is-all-you-need/raw_email.json).

The source folder has no implementation, diagrams, raw email samples from the live
demo, or queue tests. Product behavior and scale claims are speaker reports. Names
such as MyMX are transcribed inconsistently, and screen-only details could not be
verified from local artifacts.
