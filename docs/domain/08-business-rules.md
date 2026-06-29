# 08 Business Rules

Version: 1.0

Status: Draft

Owner: CTO

---

# Overview

Business Rules define the immutable business logic of the AI Talking Video Platform.

These rules are independent of frameworks, databases, AI providers, and infrastructure.

Every implementation must respect these rules.

---

# Workspace Rules

BR-001

Every Project belongs to exactly one Workspace.

BR-002

A Workspace may contain unlimited Projects depending on subscription limits.

BR-003

Deleting a Workspace archives all Projects.

---

# Project Rules

BR-010

Every Project has exactly one Source Video during MVP.

BR-011

Project names are not required to be unique.

BR-012

A Project cannot enter Rendering without a valid Timeline.

BR-013

A completed Project becomes read-only.

BR-014

Archived Projects cannot start new processing jobs.

---

# Source Video Rules

BR-020

Only supported formats are accepted.

Current:

- MP4
- MOV

BR-021

Maximum upload size is determined by subscription plan.

BR-022

Source Videos are immutable.

BR-023

Editing must never modify the original file.

---

# AI Analysis Rules

BR-030

Analysis starts only after:

- Upload completed
- Validation successful
- Credits reserved

BR-031

AI output must always be normalized before entering the Domain.

BR-032

Analysis may be regenerated.

BR-033

Previous analysis versions are preserved.

---

# Timeline Rules

BR-040

Timeline is the only editable representation of a Project.

BR-041

Rendering always consumes Timeline.

Never Source Video.

BR-042

Timeline schema must be versioned.

BR-043

Timeline validation is mandatory.

---

# Rendering Rules

BR-050

Rendering starts only after Timeline validation.

BR-051

Render jobs must be idempotent.

BR-052

Failed rendering preserves logs.

BR-053

Retry count is limited.

BR-054

Render output must be verified before completion.

---

# Export Rules

BR-060

Exports are created only after successful rendering.

BR-061

Download URLs expire.

BR-062

Expired exports may be regenerated.

---

# Billing Rules

BR-070

Credits are reserved before AI processing.

BR-071

Credits are consumed after processing begins.

BR-072

Insufficient credits block processing.

BR-073

Partial refunds may occur if rendering fails.

---

# Security Rules

BR-080

Users only access resources inside their Workspace.

BR-081

Signed URLs are required for downloads.

BR-082

Secrets must never appear in Domain Events.

---

# Retry Rules

BR-090

Retry only transient failures.

Retry examples:

- AI timeout
- Temporary storage failure
- Worker restart

Never retry:

- Invalid file
- Unsupported codec
- Invalid Timeline

---

# Observability Rules

BR-100

Every state transition must be logged.

BR-101

Every Domain Event must be traceable.

BR-102

Every Render Job must keep execution history.

---

# AI Rules

BR-110

AI never edits video directly.

AI only generates structured editing instructions.

BR-111

Timeline is the contract between AI and Rendering.

BR-112

AI providers are replaceable.

---

# Future Rules

Future versions may introduce:

- Team permissions
- Brand Kit enforcement
- Auto publishing
- AI model selection
- Enterprise policies

