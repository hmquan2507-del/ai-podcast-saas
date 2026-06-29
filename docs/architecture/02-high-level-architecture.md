# 02 High Level Architecture

## Architecture Style

The system uses a modular monorepo with separate runtime services.

## Runtime Services

- apps/web: Next.js frontend
- apps/api: FastAPI backend API
- apps/ai-worker: background AI processing worker
- apps/render-worker: FFmpeg rendering worker
- PostgreSQL: relational database
- Redis: queue and cache
- Object Storage: raw and exported video storage

## Request Flow

Frontend sends requests to API.

API creates jobs and stores metadata.

Workers consume jobs from Redis.

Workers update job status in PostgreSQL.

Frontend polls or subscribes to job status.

## Why This Architecture

Video processing is slow and expensive.

Therefore, upload, AI analysis, and rendering must be asynchronous.

The API should stay fast and stateless.

Workers handle long-running tasks.
