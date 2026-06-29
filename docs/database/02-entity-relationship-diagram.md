# 02 Entity Relationship Diagram

Version: 1.0

Status: Draft

Owner: CTO

---

# Overview

This document defines the first database relationship model for the AI Talking Video Platform.

The ERD is derived from the Domain Model.

Database design must follow:

- Domain Overview
- Bounded Contexts
- Aggregates
- Entities
- Value Objects
- Domain Events
- State Machines
- Business Rules

---

# Core Relationship Map

Workspace
    |
    | 1:N
    v
Project
    |
    | 1:1
    v
SourceVideo
    |
    | 1:1
    v
Analysis
    |
    | 1:1
    v
Transcript
    |
    | 1:N
    v
SpeakerSegment

Project
    |
    | 1:N
    v
Highlight

Project
    |
    | 1:N
    v
Timeline
    |
    | 1:N
    v
RenderJob
    |
    | 1:N
    v
Export

Workspace
    |
    | 1:N
    v
WorkspaceMember

Workspace
    |
    | 1:1
    v
Subscription

Workspace
    |
    | 1:N
    v
CreditTransaction

Project
    |
    | 1:N
    v
DomainEvent

---

# Entity Relationship Decisions

## Workspace → Project

A Workspace may have many Projects.

A Project belongs to exactly one Workspace.

Reason:

Billing, permissions, usage limits, and future team features are workspace-based.

---

## Project → SourceVideo

For MVP, one Project has exactly one SourceVideo.

Future versions may support multiple SourceVideos.

Reason:

MVP should stay simple while preserving future expansion.

---

## SourceVideo → Analysis

A SourceVideo may have one active Analysis.

Future versions may support analysis versions.

Reason:

The first MVP should expose one primary analysis result, but the schema must allow future versioning.

---

## Analysis → Transcript

An Analysis has one Transcript.

Transcript stores language, provider, version, and confidence.

---

## Transcript → SpeakerSegment

A Transcript may contain many SpeakerSegments.

SpeakerSegments store start time, end time, speaker label, and confidence.

---

## Project → Highlight

A Project may contain many Highlights.

Highlights are AI-selected moments that may be used to create Timelines.

---

## Project → Timeline

A Project may have many Timelines.

Reason:

Future A/B testing, multiple templates, and multiple formats.

---

## Timeline → RenderJob

A Timeline may have many RenderJobs.

Reason:

The same Timeline may be rendered for TikTok, YouTube Shorts, Instagram Reels, Square, or Landscape.

---

## RenderJob → Export

A RenderJob may create one or more Exports.

For MVP, usually one RenderJob creates one Export.

---

## Workspace → Subscription

A Workspace has one active Subscription.

Subscription controls plan, credits, billing status, and renewal state.

---

## Workspace → CreditTransaction

A Workspace has many CreditTransactions.

CreditTransaction is append-only and auditable.

Never delete credit transactions.

---

## Project → DomainEvent

A Project may have many DomainEvents.

DomainEvents record workflow transitions and asynchronous activity.

---

# Initial Tables

The first PostgreSQL schema should include:

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

# High Level ERD

```text
users
  |
  | 1:N
  v
workspace_members
  ^
  |
workspaces
  |
  | 1:N
  v
projects
  |
  | 1:1
  v
source_videos
  |
  | 1:1
  v
analyses
  |
  | 1:1
  v
transcripts
  |
  | 1:N
  v
speaker_segments

projects
  | 1:N
  v
highlights

projects
  | 1:N
  v
timelines
  | 1:N
  v
render_jobs
  | 1:N
  v
exports

workspaces
  | 1:1
  v
subscriptions

workspaces
  | 1:N
  v
credit_transactions

projects
  | 1:N
  v
domain_events

workspaces
  | 1:N
  v
audit_logs
