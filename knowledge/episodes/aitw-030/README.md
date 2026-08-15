# Event-driven agentic loops

Status: curated from imported YouTube automatic captions. Claims are checked
against the timestamped transcript. The source folder also contains the demo
implementation and tests.

Source episode: [`2025-11-05-event-driven-agents`](../../../2025-11-05-event-driven-agents)

## Purpose, audience, and message

Purpose: Explain how an append-only event stream can support agent chat features
such as streaming, queued messages, interruption, and tool approval without
keeping several mutable views in sync.

Audience: Engineers building interactive agents whose users need to act while a
model or tool is still running.

Message: Record interactions as events, derive the state each consumer needs with
pure projections, and test behavior by replaying events.

## How the system works

User messages, model stream chunks, commands, approvals, and interrupts enter an
event bus. Reducers turn the event history into message, command, and interrupt
state. The UI and the model each receive a projection suited to their contract.
Services can both observe events and publish new events. This separates the write
path from the views and makes an interaction replayable.

## Tactical practices

- Do not make a frontend request call a linear agent loop when the user must be
  able to interrupt or add input. See 14:40 to 15:35.
- Treat the event history as the source of truth and derive current state from it.
  See 20:23 to 22:24.
- Let queued input finish behind the current response, while an interrupt cancels
  the active work and restores a valid input state. See 08:37 to 11:05 and 23:53
  to 25:55.
- Build separate projections for the UI and the model. Queued text can be visible
  in the UI without entering the model context early. See 25:55 to 28:25.
- Replay fixed event sequences in tests and assert the resulting controls and
  state. See 29:15 to 31:13.

## Failure modes and limits

- A mutable frontend state and mutable backend state can drift apart.
- Event sourcing adds schema and projection work. Event types need stable IDs,
  timestamps, and conversation ownership.
- A queue event and an interrupt event have different cancellation behavior and
  must not be handled as the same action.
- An in-memory demo bus is not durable production storage. Retention, ordering,
  delivery, and recovery still need explicit choices.
- The transcript is automatic caption output and has errors such as “cute event”
  for “queued event.”

## Sources and uncertainty

Primary evidence: [timestamped transcript](transcripts/stitched.txt),
[source README](../../../2025-11-05-event-driven-agents/README.md), and
[episode metadata](../../../2025-11-05-event-driven-agents/meta.md).

The source demo and tests support the architecture described in the episode, but
no production load or recovery test was run for this enrichment pass.
