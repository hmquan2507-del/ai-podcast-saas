# 03 Aggregates

Version: 1.0

Status: Draft

Owner: CTO

---

# Overview

Aggregates define transaction boundaries and consistency boundaries inside the domain.

An aggregate protects business rules around a group of related entities.

External contexts must not directly modify internal entities of an aggregate.

All changes must go through the aggregate root.

---

# Aggregate Design Principles

1. Keep aggregates small.

2. One aggregate should protect one consistency boundary.

3. Aggregate roots expose behavior, not raw data mutation.

4. Cross-aggregate communication happens through domain events.

5. Do not use database joins to enforce business rules across aggregates.

6. Long-running workflows must be coordinated through events, not synchronous transactions.

7. AI processing and rendering must not block core user actions.

---

# Aggregate Roots

The platform uses the following aggregate roots:

- Workspace
- Project
- SourceVideo
- Analysis
- Timeline
- RenderJob
- Export
- Subscription

---

# 1. Workspace Aggregate

## Purpose

Workspace represents a business space where users manage projects, billing, team members, and assets.

## Aggregate Root

Workspace

## Owns

- Workspace settings
- Membership references
- Billing owner reference
- Brand kit reference

## Business Rules

- A workspace must have one owner.
- A user may belong to many workspaces.
- A workspace may contain many projects.
- Workspace deletion must not immediately delete projects; it should archive them.
- Billing is attached to workspace, not individual project.

## Emits Events

- WorkspaceCreated
- WorkspaceUpdated
- WorkspaceArchived
- MemberAdded
- MemberRemoved

---

# 2. Project Aggregate

## Purpose

Project is the main business object representing a user editing job.

Every uploaded talking video belongs to a Project.

## Aggregate Root

Project

## Owns

- Project metadata
- Project status
- Source video reference
- Processing state
- User-selected style
- Export preferences

## Business Rules

- A project belongs to exactly one workspace.
- A project has exactly one primary source video in MVP.
- A project can have multiple exports.
- A project cannot be rendered before a timeline exists.
- A project cannot be analyzed before the source video is uploaded.
- A project can be archived but not hard-deleted during MVP.

## Valid Statuses

- created
- uploading
- uploaded
- queued
- analyzing
- analysis_completed
- timeline_generated
- rendering
- completed
- failed
- archived

## Emits Events

- ProjectCreated
- ProjectQueued
- ProjectAnalysisRequested
- ProjectTimelineReady
- ProjectRenderingRequested
- ProjectCompleted
- ProjectFailed
- ProjectArchived

---

# 3. SourceVideo Aggregate

## Purpose

SourceVideo represents the original uploaded media file.

It is responsible for video metadata, storage reference, validation, and ingestion state.

## Aggregate Root

SourceVideo

## Owns

- File metadata
- Storage path
- Duration
- Size
- Format
- Codec
- Resolution
- FPS
- Audio availability
- Language hint
- Validation result

## Business Rules

- A source video must belong to one project.
- A source video must pass validation before processing.
- A source video must not be modified after upload.
- Any edit must be represented as timeline instructions, not by changing the source video.
- MVP supports MP4 and MOV.
- MVP maximum upload size is 5GB.

## Valid Statuses

- pending_upload
- uploading
- uploaded
- validating
- valid
- invalid
- metadata_extracted
- failed

## Emits Events

- SourceVideoUploaded
- SourceVideoValidated
- SourceVideoRejected
- SourceVideoMetadataExtracted

---

# 4. Analysis Aggregate

## Purpose

Analysis represents AI understanding of a source video.

It stores structured intelligence extracted from audio, speech, and video metadata.

## Aggregate Root

Analysis

## Owns

- Transcript
- Speaker segments
- Topics
- Keywords
- Hook candidates
- CTA candidates
- Emotion markers
- Silence segments
- Highlight candidates

## Business Rules

- Analysis belongs to one source video.
- Analysis can be regenerated.
- Analysis version must be stored.
- AI provider output must be normalized before entering the domain.
- Raw AI responses must not be treated as domain truth.
- Highlight candidates must include confidence score and reason.

## Valid Statuses

- pending
- transcribing
- analyzing
- completed
- failed

## Emits Events

- AnalysisStarted
- TranscriptGenerated
- TopicsDetected
- HighlightsGenerated
- AnalysisCompleted
- AnalysisFailed

---

# 5. Timeline Aggregate

## Purpose

Timeline is the structured edit plan used by the renderer.

It is the most important bridge between AI and rendering.

AI creates or updates Timeline.

Render workers execute Timeline.

## Aggregate Root

Timeline

## Owns

- Clip selections
- Subtitle instructions
- Crop instructions
- Zoom events
- Music instructions
- Sound effect instructions
- Template reference
- Export format settings

## Business Rules

- A timeline belongs to one project.
- A timeline may be generated from one or more highlights.
- A timeline must be valid before rendering.
- A timeline must be deterministic.
- AI must not directly render video.
- All editing decisions must be represented in timeline JSON.
- Timeline schema must be versioned.

## Valid Statuses

- draft
- generated
- validated
- invalid
- render_ready
- archived

## Emits Events

- TimelineGenerated
- TimelineValidated
- TimelineInvalid
- TimelineRenderReady
- TimelineArchived

---

# 6. RenderJob Aggregate

## Purpose

RenderJob represents one execution of the rendering engine.

A single timeline may produce multiple render jobs for different formats.

## Aggregate Root

RenderJob

## Owns

- Render status
- Render attempt count
- Worker assignment
- FFmpeg command reference
- Error logs
- Output reference

## Business Rules

- A render job belongs to one timeline.
- A render job cannot start unless timeline is render_ready.
- A render job may be retried.
- Retry count must be limited.
- Render jobs must be idempotent.
- Failed render jobs must preserve logs.
- Render output must be verified before marking completed.

## Valid Statuses

- queued
- running
- completed
- failed
- retrying
- cancelled

## Emits Events

- RenderJobQueued
- RenderJobStarted
- RenderJobCompleted
- RenderJobFailed
- RenderJobRetried
- RenderJobCancelled

---

# 7. Export Aggregate

## Purpose

Export represents the final user-facing video output.

## Aggregate Root

Export

## Owns

- Output file path
- Format
- Duration
- Resolution
- File size
- Download status
- Expiration policy
- Thumbnail reference

## Business Rules

- An export is created only after successful render.
- An export belongs to one project.
- An export must reference one render job.
- Download URLs must be temporary.
- Exports may expire based on workspace plan.
- Export metadata must be stored for billing and analytics.

## Valid Statuses

- pending
- ready
- expired
- deleted
- failed

## Emits Events

- ExportCreated
- ExportReady
- ExportDownloaded
- ExportExpired
- ExportDeleted

---

# 8. Subscription Aggregate

## Purpose

Subscription manages workspace billing, credits, plans, and usage limits.

## Aggregate Root

Subscription

## Owns

- Plan
- Credit balance
- Usage records
- Billing cycle
- Renewal status
- Payment provider reference

## Business Rules

- Subscription belongs to one workspace.
- Credits are deducted before expensive processing begins.
- Credit refunds may happen when processing fails before render starts.
- Render failure after successful AI processing may trigger partial refund policy.
- A workspace cannot start processing if it has insufficient credits.
- Enterprise billing may override credit rules later.

## Valid Statuses

- trialing
- active
- past_due
- cancelled
- expired

## Emits Events

- SubscriptionCreated
- SubscriptionRenewed
- SubscriptionCancelled
- CreditsAdded
- CreditsConsumed
- CreditsRefunded
- InsufficientCreditsDetected

---

# Aggregate Relationship Map

Workspace
    |
    v
Project
    |
    v
SourceVideo
    |
    v
Analysis
    |
    v
Timeline
    |
    v
RenderJob
    |
    v
Export

Subscription is attached to Workspace.

Billing validates usage before AI Analysis and Rendering.

---

# Transaction Boundary Rules

## Project Creation

Create Project inside Project aggregate.

Do not create SourceVideo until upload begins.

## Video Upload

SourceVideo owns validation and metadata.

Project only tracks reference and high-level status.

## AI Analysis

Analysis is created after SourceVideo is valid.

Analysis completion emits event to Editing Context.

## Timeline Generation

Timeline is created after Analysis is completed.

Timeline validation must happen before rendering.

## Rendering

RenderJob consumes Timeline.

RenderJob creates Export after successful rendering.

## Billing

Subscription validates and consumes credits before expensive operations.

---

# Anti-Patterns

The following are not allowed:

- Project directly modifies Transcript.
- RenderJob directly modifies SourceVideo.
- Billing directly modifies Project internals.
- AI provider output directly becomes Timeline without validation.
- API updates internal entities without aggregate methods.
- Workers skip domain rules and write directly to database tables.

---

# Future Expansion

The aggregate model supports future features:

- Multiple source videos per project
- Multiple timelines per project
- A/B testing
- Multi-format exports
- Team workspace
- Brand kit
- Publishing automation
- Analytics
- Enterprise billing
