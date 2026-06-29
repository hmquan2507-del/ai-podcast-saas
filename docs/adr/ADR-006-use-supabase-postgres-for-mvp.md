# ADR-006: Use Supabase PostgreSQL For MVP

## Status

Accepted

## Context

The product needs a reliable PostgreSQL database quickly.

The MVP goal is to serve the first 100 users without spending too much time on database operations.

## Decision

Use Supabase PostgreSQL as the managed production database for MVP.

Use local Docker PostgreSQL for development.

FastAPI remains the owner of business logic and database access.

## Consequences

Benefits:

- Faster MVP setup
- Managed PostgreSQL
- Easy database dashboard
- Possible Auth integration
- Lower operational burden

Tradeoffs:

- Must avoid vendor lock-in
- Must keep business logic outside Supabase
- Large video storage should not use Supabase Storage

## Portability Rule

The application must remain portable to any PostgreSQL provider.
