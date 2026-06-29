# ADR-002: Use FastAPI For Backend API

## Status

Accepted

## Context

The backend needs strong Python support because the product depends heavily on AI, video processing, FFmpeg orchestration, and background jobs.

## Decision

Use FastAPI as the backend API framework.

## Consequences

Benefits:

- Native Python AI ecosystem
- High performance
- Strong typing with Pydantic
- Good API documentation via OpenAPI

Tradeoffs:

- Frontend and backend use different languages
- Requires Python dependency management discipline
