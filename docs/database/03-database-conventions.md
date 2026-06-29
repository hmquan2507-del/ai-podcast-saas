# 03 Database Conventions

Version: 1.0

Status: Draft

Owner: CTO

---

# Purpose

This document defines database standards for the AI Talking Video Platform.

All database schemas, migrations, indexes, constraints, and models must follow these conventions.

---

# Database Engine

Primary database:

PostgreSQL

Production MVP:

Supabase PostgreSQL

Local development:

Docker PostgreSQL

---

# Naming Convention

Use snake_case for all database identifiers.

Correct:

- users
- workspaces
- source_videos
- render_jobs
- credit_transactions

Incorrect:

- Users
- userTable
- tbl_users
- sourceVideo
- RenderJobs

---

# Table Naming

Use plural table names.

Examples:

- users
- projects
- timelines
- exports

Join tables should describe the relationship.

Examples:

- workspace_members
- project_templates

---

# Primary Keys

Every table must use UUID primary keys.

Primary key column name:

id

Example:

id UUID PRIMARY KEY

Do not use:

- integer auto increment IDs
- table-specific IDs like user_id as primary key

---

# Foreign Keys

Foreign key columns use singular entity name plus _id.

Examples:

- workspace_id
- project_id
- source_video_id
- timeline_id
- render_job_id

Foreign keys must reference id.

Example:

workspace_id UUID REFERENCES workspaces(id)

---

# Timestamp Convention

Every table must include:

created_at TIMESTAMPTZ NOT NULL DEFAULT now()

Mutable tables must include:

updated_at TIMESTAMPTZ NOT NULL DEFAULT now()

Soft-deletable tables must include:

deleted_at TIMESTAMPTZ NULL

Archived business objects may include:

archived_at TIMESTAMPTZ NULL

---

# Status Fields

Stateful tables must include a status column.

Examples:

- projects.status
- source_videos.status
- analyses.status
- render_jobs.status
- exports.status
- subscriptions.status

Status values must match domain state machines.

---

# Enum Convention

For MVP, store enum values as TEXT with CHECK constraints.

Reason:

- Easier migrations
- Easier portability
- Easier Supabase compatibility

Example:

status TEXT NOT NULL CHECK (status IN ('created', 'uploading', 'uploaded'))

---

# JSONB Convention

JSONB is allowed for flexible AI outputs and Timeline instructions.

Allowed JSONB fields:

- timelines.timeline_json
- analyses.raw_result
- source_videos.metadata
- domain_events.payload
- audit_logs.metadata

Rules:

- JSONB must be validated at application layer.
- JSONB must not replace relational modeling for core business objects.
- JSONB fields must be versioned when schema may change.

---

# Index Convention

Index names must follow:

idx_<table>_<columns>

Examples:

- idx_projects_workspace_id
- idx_projects_status
- idx_render_jobs_status
- idx_domain_events_project_id

Unique index names:

uq_<table>_<columns>

Examples:

- uq_users_email
- uq_workspaces_slug

---

# Constraint Convention

Foreign key constraints:

fk_<table>_<column>

Check constraints:

chk_<table>_<rule>

Unique constraints:

uq_<table>_<columns>

---

# Soft Delete Convention

User-facing business objects should use soft delete.

Use deleted_at.

Examples:

- workspaces
- projects
- exports

Do not soft delete append-only ledgers.

Never soft delete:

- credit_transactions
- domain_events
- audit_logs

---

# Append-Only Tables

The following tables are append-only:

- credit_transactions
- domain_events
- audit_logs

Append-only means:

- Records are never updated for business changes.
- Records are never deleted.
- Corrections are represented by new records.

---

# Money and Credits

Money values must store:

- amount
- currency

Credit values must store integer amounts.

Do not store floating point money.

---

# File Metadata

PostgreSQL stores file metadata only.

Video files are stored in object storage.

Required file metadata:

- storage_provider
- bucket_name
- object_key
- file_size
- mime_type
- checksum
- duration_ms

---

# Multi-Tenancy

The system is workspace-based.

Most business tables must include:

workspace_id

This supports:

- permissions
- billing
- filtering
- future row-level security

---

# Audit Fields

Important tables should include:

- created_by
- updated_by

Where applicable.

Audit logs should store:

- actor_id
- workspace_id
- action
- entity_type
- entity_id
- metadata
- created_at

---

# Migration Rules

Use Alembic for migrations.

Migration files must be:

- deterministic
- reviewable
- reversible when possible

Never edit an already-applied production migration.

Create a new migration instead.

---

# Performance Rules

Index all frequently queried foreign keys.

Index all status columns used by workers.

Index created_at when used for dashboards or history.

Avoid large unbounded queries.

Always paginate list endpoints.

---

# Security Rules

Never store secrets in the database unless encrypted.

Never store raw API keys.

Never store payment card data.

Use references to payment provider objects instead.

---

# Portability Rules

Avoid Supabase-only features for core business logic.

Allowed:

- PostgreSQL
- UUID
- JSONB
- CHECK constraints
- standard indexes

Avoid:

- database-specific business workflows
- vendor-only functions for domain logic

---

# Implementation Mapping

These conventions apply to:

- PostgreSQL schema
- Alembic migrations
- SQLAlchemy models
- Repository layer
- Pydantic schemas
- API contracts
