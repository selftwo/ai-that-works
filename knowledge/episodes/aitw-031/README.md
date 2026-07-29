# Dates, Times, and LLMs

Status: curated from imported YouTube automatic captions. Claims are checked
against the timestamped transcript. The source folder includes the BAML schema,
tests, and a small Python recurrence helper.

Source episode: [`2025-11-11-dates-and-times`](../../../2025-11-11-dates-and-times)

## Purpose, audience, and message

Purpose: Show how to turn natural language dates into typed data while keeping
calendar arithmetic, timezone conversion, and validation in deterministic code.

Audience: Engineers building assistants, schedulers, memory systems, or analysis
tools that accept relative and recurring time expressions.

Message: Give the model a reference clock and user timezone, use it to classify
date intent into a small schema, then let ordinary software compute the result.

## How the system works

The extraction schema separates absolute, relative, and recurring dates. The
prompt supplies a source date so phrases such as “next Friday” have a reference.
Recurring output uses a cron expression plus an optional timezone. Python code
uses the user's zone when the text did not state one and computes the next concrete
occurrence. Missing details remain missing so the product can ask the user or show
a date control.

## Tactical practices

- Inject the current date into the prompt for every relative date extraction. See
  15:21 to 17:13.
- Represent absolute, relative, and recurring dates as different types. See 18:28
  to 20:10.
- Use the user's timezone unless the user explicitly provides another one. See
  22:40 to 23:30.
- Convert recurrence output to concrete dates with deterministic timezone and cron
  libraries. See 23:51 to 24:15.
- Use an intermediate representation that the model can produce and software can
  evaluate. See 31:40 to 34:40.
- Normalize timestamps for the model at the serialization boundary so it does not
  repeat timezone reasoning on every turn. See 48:20 to 54:25.

## Failure modes and limits

- A relative expression has no stable answer without a source clock.
- Server or UTC timestamps can conflict with the user's local meaning of “today”
  or “last night.”
- Missing time components should not be silently guessed when the product needs an
  exact appointment.
- Cron and ISO timestamps do not by themselves preserve all user intent about
  relative language and timezone defaults.
- Moving timezones can change day buckets. The guest describes accepting bounded
  errors in old memory buckets instead of recomputing all history.
- Automatic captions contain transcription errors, including “UCT” and “chron.”

## Sources and uncertainty

Primary evidence: [timestamped transcript](transcripts/stitched.txt),
[source README](../../../2025-11-11-dates-and-times/README.md), and
[episode metadata](../../../2025-11-11-dates-and-times/meta.md).

The transcript includes product examples and guest reports that were not checked
against production systems. The local code supports the extraction pattern but is
a small demonstration, not a complete scheduling service.
