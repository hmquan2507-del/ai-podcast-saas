# 01 Database Strategy

Version: 1.0

Status: Draft

Owner: CTO

---

# Decision

Use PostgreSQL as the primary database.

For MVP, production database may run on Supabase PostgreSQL.

Local development uses Docker PostgreSQL.

The application must not be tightly coupled to Supabase-specific features.

---

# Why PostgreSQL

PostgreSQL is reliable, mature, relational, and suitable for SaaS systems with complex business workflows.

The platform needs:

- Users
- Workspaces
- Projects
- Source Videos
- Transcripts
- Highlights
- Timelines
- Render Jobs
- Exports
- Credits
- Subscriptions
- Event Logs

These are relational business objects.

---

# Supabase Role

Supabase can be used for:

- Managed PostgreSQL
- Authentication
- Row Level Security later
- Admin dashboard
- Quick MVP setup

Supabase should not own core business logic.

Business logic stays in FastAPI domain modules.

---

# What Supabase Should Not Handle

Do not use Supabase as the main video storage layer for large uploaded videos.

Large video files should use object storage such as Cloudflare R2.

Do not write business logic directly inside Supabase functions during MVP.

Do not make the backend depend on Supabase-only APIs.

---

# Development Strategy

Local development:

- PostgreSQL via Docker Compose
- Redis via Docker Compose
- FastAPI connects through DATABASE_URL

Production MVP:

- Supabase PostgreSQL
- FastAPI backend
- Cloudflare R2 for video storage
- Redis managed service or self-hosted Redis

---

# Database Access Pattern

FastAPI owns database access.

Use:

- SQLAlchemy
- Alembic migrations
- Repository pattern
- Service layer
- Domain layer

Frontend must not directly mutate business tables.

---

# Portability Rule

The system must be able to move from Supabase PostgreSQL to another PostgreSQL provider without rewriting business logic.

Allowed:

- Standard PostgreSQL
- Standard SQL constraints
- Standard indexes
- Alembic migrations

Avoid:

- Vendor-specific business logic
- Supabase-only database behavior for core workflows

---

# Database Design Principles

1. Database reflects Domain Model.

2. Every important domain entity gets a table.

3. Every stateful workflow has explicit status fields.

4. Every long-running process has logs.

5. Every expensive operation is auditable.

6. Soft delete is preferred over hard delete.

7. Event log is required.

8. Timestamps are required.

9. Foreign keys are required.

10. Indexes are designed based on query patterns.

---

# Core Tables

Initial database design will include:

- users
- workspaces
- workspace_members
- projects
- source_videos
- analyses
- transcripts
- speaker_segments
- highlights
- timelines
- render_jobs
- exports
- subscriptions
- credit_transactions
- domain_events
- audit_logs

---

# Storage Strategy

Database stores metadata only.

Video files are stored in object storage.

Database stores:

- storage_provider
- bucket_name
- object_key
- file_size
- checksum
- mime_type
- duration_ms
- status

---

# Billing Strategy

Billing data must be auditable.

Credit transactions must never be deleted.

Every credit change must have:

- workspace_id
- amount
- reason
- reference_type
- reference_id
- created_at

---

# Event Strategy

Domain events are stored in PostgreSQL.

This allows:

- debugging
- retry
- audit
- analytics
- workflow reconstruction

---

# MVP Database Provider Decision

Use Supabase PostgreSQL for production MVP if speed and simplicity are prioritized.

Use self-managed PostgreSQL later if cost, scale, or compliance requires it.

