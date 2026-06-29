# 02 Bounded Contexts

Version: 1.0

Status: Draft

Owner: CTO

---

# Overview

The platform is divided into bounded contexts.

Each context owns its own business logic, entities, services, events, and responsibilities.

Contexts communicate through events or well-defined APIs.

No context may directly manipulate another context's internal state.

---

# 1. Identity Context

Responsibilities:

- User
- Authentication
- Authorization
- Workspace
- Team
- Roles
- Permissions

Owns:

- User
- Workspace
- Membership

Events:

- UserCreated
- WorkspaceCreated
- MemberInvited

---

# 2. Project Context

Responsibilities:

- Project lifecycle
- Source video
- Metadata
- Upload
- Video status

Owns:

- Project
- SourceVideo

Events:

- ProjectCreated
- VideoUploaded
- MetadataExtracted

---

# 3. AI Analysis Context

Responsibilities:

- Speech-to-text
- Speaker detection
- Emotion detection
- Topic detection
- Hook detection
- CTA detection
- Highlight scoring

Owns:

- Transcript
- Speaker
- Topic
- HighlightCandidate

Events:

- TranscriptGenerated
- HighlightsGenerated
- AnalysisCompleted

---

# 4. Editing Context

Responsibilities:

- Timeline generation
- Subtitle generation
- Crop decisions
- Zoom effects
- Motion presets
- Templates

Owns:

- Timeline
- Subtitle
- EditDecision
- Template

Events:

- TimelineGenerated
- SubtitleGenerated

---

# 5. Rendering Context

Responsibilities:

- FFmpeg execution
- Render queue
- Export generation
- Thumbnail generation (future)

Owns:

- RenderJob
- Export

Events:

- RenderStarted
- RenderCompleted
- RenderFailed

---

# 6. Billing Context

Responsibilities:

- Subscription
- Credits
- Usage
- Invoice
- Payment

Owns:

- Subscription
- CreditBalance
- Invoice

Events:

- CreditsConsumed
- SubscriptionRenewed

---

# 7. Notification Context

Responsibilities:

- Email
- In-app notification
- Webhook

Events:

- ExportReady
- RenderFailed
- PaymentSucceeded

---

# 8. Monitoring Context

Responsibilities:

- Logs
- Metrics
- Audit
- Health check
- Error tracking

Events:

- WorkerCrashed
- QueueDelayed
- APIError

---

# Context Relationships

Identity
    ↓
Project
    ↓
AI Analysis
    ↓
Editing
    ↓
Rendering
    ↓
Notification

Billing interacts with every context through authorization and credit validation.

Monitoring observes every context but owns no business entities.

---

# Architectural Rules

1. Every bounded context owns its own business logic.

2. Cross-context communication must happen through events or public APIs.

3. No context may directly modify another context's entities.

4. Shared code belongs in packages/.

5. Business rules must remain inside the owning context.

