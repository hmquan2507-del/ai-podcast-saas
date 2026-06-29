# 06 Domain Events

Version: 1.0

Status: Draft

Owner: CTO

---

# Overview

Domain Events represent important business facts that have already happened inside the system.

Events are used to connect bounded contexts without tightly coupling them.

The platform uses events to coordinate long-running workflows such as upload, AI analysis, timeline generation, rendering, billing, notification, and failure recovery.

---

# Event Design Principles

1. Events describe something that already happened.

2. Event names must use past tense.

3. Events must be immutable.

4. Events must include enough data for consumers to react.

5. Events must not expose internal entity implementation details.

6. Events must be versioned.

7. Event consumers must be idempotent.

8. Events should be safe to replay.

9. Events should not contain secrets.

10. Events should be logged for audit and debugging.

---

# Event Naming Convention

Use PascalCase.

Examples:

- ProjectCreated
- SourceVideoUploaded
- TranscriptGenerated
- TimelineGenerated
- RenderJobCompleted
- ExportReady

---

# Base Event Schema

Every event must include:

- event_id
- event_type
- event_version
- occurred_at
- correlation_id
- causation_id
- workspace_id
- actor_id
- payload

---

# Event Categories

## Identity Events

- UserCreated
- UserLoggedIn
- WorkspaceCreated
- MemberInvited
- MemberJoined
- MemberRemoved

## Project Events

- ProjectCreated
- ProjectUpdated
- ProjectArchived
- ProjectFailed

## Source Video Events

- SourceVideoUploadStarted
- SourceVideoUploaded
- SourceVideoValidated
- SourceVideoRejected
- SourceVideoMetadataExtracted

## AI Analysis Events

- AnalysisRequested
- AnalysisStarted
- TranscriptGenerated
- SpeakerSegmentsGenerated
- TopicsDetected
- HooksDetected
- HighlightsGenerated
- AnalysisCompleted
- AnalysisFailed

## Editing Events

- TimelineGenerationRequested
- TimelineGenerated
- TimelineValidated
- TimelineInvalid
- TimelineRenderReady

## Rendering Events

- RenderRequested
- RenderJobQueued
- RenderJobStarted
- RenderJobCompleted
- RenderJobFailed
- RenderJobRetried
- RenderJobCancelled

## Export Events

- ExportCreated
- ExportReady
- ExportDownloaded
- ExportExpired
- ExportDeleted

## Billing Events

- CreditsReserved
- CreditsConsumed
- CreditsRefunded
- InsufficientCreditsDetected
- SubscriptionCreated
- SubscriptionRenewed
- SubscriptionCancelled
- PaymentSucceeded
- PaymentFailed

## Notification Events

- NotificationQueued
- NotificationSent
- NotificationFailed

## Monitoring Events

- WorkerStarted
- WorkerStopped
- WorkerCrashed
- QueueDelayed
- APIErrorDetected

---

# Core Event Flow

The primary video processing flow is:

ProjectCreated

↓

SourceVideoUploaded

↓

SourceVideoValidated

↓

SourceVideoMetadataExtracted

↓

AnalysisRequested

↓

AnalysisStarted

↓

TranscriptGenerated

↓

HighlightsGenerated

↓

AnalysisCompleted

↓

TimelineGenerationRequested

↓

TimelineGenerated

↓

TimelineValidated

↓

TimelineRenderReady

↓

RenderRequested

↓

RenderJobQueued

↓

RenderJobStarted

↓

RenderJobCompleted

↓

ExportCreated

↓

ExportReady

---

# Critical Events

## ProjectCreated

Triggered when a user creates a new video project.

Consumers:

- Billing Context
- Monitoring Context

Payload:

- project_id
- workspace_id
- created_by
- title
- project_type

---

## SourceVideoUploaded

Triggered after the original video file is uploaded successfully.

Consumers:

- Project Context
- AI Analysis Context
- Monitoring Context

Payload:

- project_id
- source_video_id
- workspace_id
- storage_path
- file_size
- filename

---

## SourceVideoValidated

Triggered after source video passes validation.

Consumers:

- AI Analysis Context
- Billing Context

Payload:

- project_id
- source_video_id
- duration_ms
- format
- resolution
- has_audio

---

## AnalysisRequested

Triggered after billing confirms enough credits and the video is valid.

Consumers:

- AI Worker
- Monitoring Context

Payload:

- project_id
- source_video_id
- workspace_id
- analysis_mode
- priority

---

## TranscriptGenerated

Triggered after speech-to-text completes.

Consumers:

- AI Analysis Context
- Editing Context

Payload:

- project_id
- source_video_id
- transcript_id
- language
- provider
- confidence_score

---

## HighlightsGenerated

Triggered after AI identifies high-value segments.

Consumers:

- Editing Context
- Monitoring Context

Payload:

- project_id
- analysis_id
- highlight_count
- top_score
- provider

---

## TimelineGenerated

Triggered after the editing engine creates timeline JSON.

Consumers:

- Rendering Context
- Monitoring Context

Payload:

- project_id
- timeline_id
- timeline_version
- template_id
- duration_ms

---

## TimelineRenderReady

Triggered after timeline validation succeeds.

Consumers:

- Rendering Context
- Billing Context

Payload:

- project_id
- timeline_id
- export_targets

---

## RenderJobCompleted

Triggered after FFmpeg successfully renders a video.

Consumers:

- Export Context
- Billing Context
- Notification Context
- Monitoring Context

Payload:

- render_job_id
- timeline_id
- project_id
- output_path
- duration_ms
- file_size

---

## ExportReady

Triggered when the final video is ready for user download.

Consumers:

- Notification Context
- Web App
- Monitoring Context

Payload:

- export_id
- project_id
- workspace_id
- download_url
- expires_at

---

# Event Delivery Strategy

MVP:

- Redis queue for async job coordination.
- PostgreSQL stores durable event logs.
- Workers consume jobs idempotently.

Future:

- Dedicated event bus.
- Kafka or NATS for high-throughput event streaming.
- Outbox pattern for reliable event publishing.

---

# Idempotency Rules

Every event consumer must be idempotent.

If the same event is received multiple times, the system must not duplicate side effects.

Examples:

- Do not create duplicate render jobs.
- Do not consume credits twice.
- Do not send duplicate notifications.
- Do not create duplicate exports.

---

# Retry Rules

Retryable failures:

- Temporary AI provider failure
- Temporary render worker failure
- Temporary storage failure
- Temporary network failure

Non-retryable failures:

- Invalid source video
- Unsupported file format
- Insufficient credits
- Corrupted upload
- Invalid timeline schema

---

# Event Storage

Events must be stored for:

- Debugging
- Audit
- Retry
- Analytics
- Workflow reconstruction

Minimum stored fields:

- event_id
- event_type
- event_version
- occurred_at
- aggregate_type
- aggregate_id
- workspace_id
- payload
- metadata

---

# Event Versioning

Events must include event_version.

Breaking changes require a new version.

Consumers should support old event versions during migration.

---

# Security Rules

Events must not contain:

- API keys
- Access tokens
- Payment card data
- Raw passwords
- Private user secrets

Events may contain references to secure resources, but not the secret content itself.

---

# Implementation Mapping

Future implementation locations:

- apps/api/domain/events/
- apps/api/modules/*/events/
- apps/ai-worker/events/
- apps/render-worker/events/
- packages/types/events/
- packages/shared/event-bus/
- packages/database/event-log/

---

# Future Expansion

The event model supports:

- Multi-worker orchestration
- AI provider fallback
- Render farm scaling
- Team collaboration
- Publishing automation
- Analytics pipelines
- Enterprise audit logs
