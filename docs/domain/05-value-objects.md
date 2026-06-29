# 05 Value Objects

Version: 1.0

Status: Draft

Owner: CTO

---

# Overview

Value Objects describe immutable concepts within the domain.

They have no identity.

Equality is determined entirely by their values.

Value Objects are immutable.

Replacing a Value Object creates a new instance.

---

# Design Principles

- Immutable
- No identity
- Equality by value
- No lifecycle
- Safe to share
- Independent of persistence

---

# Value Object Catalog

## Email

Represents a validated email address.

Rules:

- RFC compliant
- Lowercase
- Trim whitespace

---

## VideoResolution

Examples:

- 1920x1080
- 1080x1920
- 3840x2160

Rules:

- Width > 0
- Height > 0

---

## AspectRatio

Examples:

- 16:9
- 9:16
- 1:1
- 4:5

---

## Duration

Represents video duration.

Rules:

- Greater than zero
- Stored in milliseconds

---

## TimeRange

Represents a segment inside a video.

Properties:

- start
- end

Rules:

- start < end

---

## Language

ISO language code.

Examples:

- en
- vi
- ja
- ko

---

## FileSize

Represents file size.

Units:

- Bytes
- KB
- MB
- GB

---

## VideoFormat

Supported formats:

- MP4
- MOV

Future:

- MKV
- AVI
- WEBM

---

## AudioCodec

Examples:

- AAC
- MP3
- PCM

---

## VideoCodec

Examples:

- H264
- H265
- AV1

---

## CreditAmount

Represents AI credits.

Rules:

- Must not be negative

---

## Money

Represents billing value.

Properties:

- amount
- currency

---

## SubtitleStyle

Represents subtitle appearance.

Properties:

- font
- size
- color
- stroke
- animation

---

## CropArea

Represents crop coordinates.

Properties:

- x
- y
- width
- height

---

## ZoomLevel

Represents camera zoom.

Rules:

- Minimum 1.0x

---

## EmotionScore

Represents detected emotion.

Range:

0.0 - 1.0

---

# Value Object Rules

Value Objects:

- Never own entities
- Never emit events
- Never have lifecycle
- Never contain business identity
- Can be reused across Aggregates

---

# Future Value Objects

- BrandColor
- BrandFont
- Watermark
- AIModelVersion
- VoiceProfile
- ThumbnailStyle
- PublishSchedule

