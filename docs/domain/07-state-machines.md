# 07 State Machines

Version: 1.0

Status: Draft

Owner: CTO

---

# Overview

State Machines define all valid lifecycle transitions for business entities.

Every state transition must be validated.

Invalid transitions are rejected.

State transitions emit Domain Events.

---

# Project State Machine

States

created

↓

uploading

↓

uploaded

↓

queued

↓

analyzing

↓

analysis_completed

↓

timeline_generated

↓

rendering

↓

completed

↓

archived

Allowed transitions

created → uploading

uploading → uploaded

uploaded → queued

queued → analyzing

analyzing → analysis_completed

analysis_completed → timeline_generated

timeline_generated → rendering

rendering → completed

completed → archived

Failure transitions

uploading → failed

analyzing → failed

rendering → failed

Retry

failed → queued

---

# Source Video State Machine

pending_upload

↓

uploading

↓

uploaded

↓

validating

↓

valid

↓

metadata_extracted

Failure

validating → invalid

invalid → archived

---

# Analysis State Machine

pending

↓

transcribing

↓

analyzing

↓

completed

Failure

transcribing → failed

analyzing → failed

Retry

failed → pending

---

# Timeline State Machine

draft

↓

generated

↓

validated

↓

render_ready

↓

archived

Failure

generated → invalid

invalid → generated

---

# Render Job State Machine

queued

↓

running

↓

completed

Failure

running → failed

Retry

failed → retrying

retrying → queued

Cancel

queued → cancelled

running → cancelled

---

# Export State Machine

pending

↓

ready

↓

downloaded

↓

expired

↓

deleted

---

# Subscription State Machine

trialing

↓

active

↓

past_due

↓

cancelled

↓

expired

---

# Credit Transaction State Machine

created

↓

reserved

↓

consumed

↓

completed

Refund

consumed → refunded

---

# Global Rules

A state transition:

- Must be atomic.
- Must emit a Domain Event.
- Must be logged.
- Must update timestamps.
- Must be idempotent.

Illegal transitions must return an error.

