# ADR-004: Use FFmpeg For Rendering

## Status

Accepted

## Context

The product needs reliable and cost-efficient video rendering.

AI video generation APIs are expensive and unpredictable for deterministic editing.

## Decision

Use FFmpeg as the main rendering engine.

AI generates timeline JSON. FFmpeg executes the timeline.

## Consequences

Benefits:

- Lower cost
- Predictable output
- Fast rendering
- Full control over subtitles, crops, audio, transitions, and exports

Tradeoffs:

- Requires building a custom render abstraction layer
- Complex effects may require additional tooling later
