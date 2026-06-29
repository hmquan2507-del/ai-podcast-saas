# AI Podcast SaaS

AI SaaS platform that converts long podcast videos into short-form videos for TikTok, YouTube Shorts, and Instagram Reels.

## Core Workflow

Upload podcast video → AI transcription → highlight detection → subtitle generation → timeline JSON → FFmpeg render → short-form video export.

## Architecture Rule

AI does not directly render videos. AI generates structured editing decisions. Rendering is handled by FFmpeg and render workers.

## Stack

- Frontend: Next.js
- Backend: FastAPI
- Database: PostgreSQL
- Queue/Cache: Redis
- AI: Gemini + Whisper
- Rendering: FFmpeg
- Monorepo: pnpm + TurboRepo
- Infrastructure: Docker Compose

## Development

```bash
pnpm install
pnpm dev
