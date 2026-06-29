# 01 System Overview

## Product

AI Podcast SaaS is a web platform that converts long podcast videos into short-form vertical videos.

## Core Workflow

User uploads podcast video.

The system stores the raw video.

The AI pipeline extracts audio, creates transcript, detects highlights, generates subtitles, and produces structured edit decisions.

The render pipeline uses FFmpeg to generate final short-form videos.

Users preview and download exports.

## Main System Components

- Web App
- Backend API
- PostgreSQL Database
- Redis Queue
- AI Worker
- Render Worker
- Storage Layer
- Billing System
- Monitoring System

## Critical Architecture Rule

AI does not directly render videos.

AI produces structured editing instructions.

The rendering engine executes those instructions.

## Scale Target

The architecture must support:

- 100 users during MVP
- 1,000 users after validation
- 10,000 users after infrastructure optimization
