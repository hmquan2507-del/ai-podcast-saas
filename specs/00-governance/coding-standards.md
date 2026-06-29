# Coding Standards

## General

- Production-ready code only.
- No demo-only implementation.
- No hardcoded secrets.
- Validate all external input.
- Log important state transitions.
- Write tests for business logic.

## Python

- Use Python 3.12.
- Use FastAPI.
- Use SQLAlchemy 2.0 async.
- Use Alembic migrations.
- Use Pydantic v2.
- Prefer explicit typing.

## Database

- Use PostgreSQL.
- Use UUID primary keys.
- Use snake_case.
- Use Alembic.
- Use append-only ledgers for credits and events.

## API

- REST first.
- Version API when needed.
- Commands mutate state.
- Queries read state.
