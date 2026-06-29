# 04 Entities

Version: 1.0

Status: Draft

Owner: CTO

---

# Overview

Entities are business objects with a unique identity.

Unlike Value Objects, entities continue to exist even when their attributes change.

Each entity belongs to exactly one Aggregate.

---

# Entity Catalog

## Workspace

Identity:

- workspace_id

Attributes:

- name
- slug
- owner_id
- billing_plan
- timezone
- brand_settings
- created_at
- updated_at

---

## User

Identity:

- user_id

Attributes:

- email
- full_name
- avatar_url
- status
- last_login
- created_at

---

## Membership

Identity:

- membership_id

Attributes:

- workspace_id
- user_id
- role
- invited_by
- joined_at

---

## Project

Identity:

- project_id

Attributes:

- workspace_id
- title
- description
- status
- template_id
- created_at
- updated_at

---

## SourceVideo

Identity:

- video_id

Attributes:

- project_id
- filename
- storage_path
- duration
- resolution
- fps
- codec
- language
- file_size
- uploaded_at

---

## Transcript

Identity:

- transcript_id

Attributes:

- video_id
- language
- provider
- version
- confidence_score
- generated_at

---

## SpeakerSegment

Identity:

- segment_id

Attributes:

- transcript_id
- speaker_label
- start_time
- end_time
- confidence

---

## Highlight

Identity:

- highlight_id

Attributes:

- project_id
- score
- start_time
- end_time
- category
- confidence
- reason

---

## Timeline

Identity:

- timeline_id

Attributes:

- project_id
- version
- template
- duration
- render_ready
- created_at

---

## SubtitleTrack

Identity:

- subtitle_id

Attributes:

- timeline_id
- language
- style
- animation
- provider

---

## RenderJob

Identity:

- render_job_id

Attributes:

- timeline_id
- worker_id
- status
- started_at
- completed_at
- retry_count

---

## Export

Identity:

- export_id

Attributes:

- render_job_id
- format
- resolution
- download_url
- expires_at
- size

---

## Subscription

Identity:

- subscription_id

Attributes:

- workspace_id
- plan
- billing_cycle
- status
- renew_at

---

## CreditTransaction

Identity:

- transaction_id

Attributes:

- workspace_id
- amount
- reason
- reference
- created_at

---

# Entity Relationships

Workspace

↓

User

↓

Membership

↓

Project

↓

SourceVideo

↓

Transcript

↓

Highlight

↓

Timeline

↓

RenderJob

↓

Export

Subscription belongs to Workspace.

CreditTransaction belongs to Subscription.

---

# Entity Rules

- Every entity has one immutable identifier.
- Entity IDs never change.
- Business logic must be implemented through Aggregate Roots.
- Entities never communicate directly across Aggregates.
- Persistence technology must not affect entity design.

---

# Future Entities

Future versions may introduce:

- BrandKit
- MediaLibrary
- Comment
- TeamInvitation
- PublishJob
- AnalyticsReport
- AIModelProfile
- TemplateMarketplace

