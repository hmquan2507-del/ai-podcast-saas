# ADR-001: Use Monorepo Architecture

## Status

Accepted

## Context

The product includes frontend, backend, AI workers, render workers, shared types, shared config, and infrastructure files.

Managing these as separate repositories would increase complexity during early development.

## Decision

Use a monorepo with pnpm workspaces and TurboRepo.

## Consequences

Benefits:

- Easier code sharing
- Easier local development
- Unified CI/CD
- Better AI-assisted development consistency

Tradeoffs:

- Requires clear folder boundaries
- Requires strong documentation discipline
