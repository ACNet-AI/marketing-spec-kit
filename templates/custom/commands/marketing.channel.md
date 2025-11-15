---
description: Retrieve channel platform details, content constraints, and tool configuration
argument-hint: "<channel_id>"
allowed-tools: read_file, grep
model-override: null
---

## Purpose

Retrieve a specific **Channel** entity by ID. This provides:
- Platform-specific constraints (character limits, etc.)
- Supported content types
- Tool integration details
- Target audiences

## Inputs

```yaml
channel_id: string  # Required - Channel identifier (e.g., "twitter", "dev-blog")
```

## Output

```yaml
channel:
  id: string (pattern: ^[a-z0-9-]+$)
  name: string
  type: enum[social_media, email, blog, forum, video, podcast]
  platform: string
  audiences: array[string] (optional)
  content_types: array[string] (≥1 item)
  constraints: object (optional)
  tool_id: string (optional)
  config: object (optional)
```

## Validation Rules

- **VR-CH01**: `id` must be unique within project
- **VR-CH02**: `type` must be valid channel category
- **VR-CH03**: `platform` should follow naming convention (lowercase, no spaces)
- **VR-CH04**: If `tool_id` provided, must reference existing tool
- **VR-CH05**: `content_types` must have at least 1 item
- **VR-CH06**: If `constraints.max_text_length` provided, must be > 0

## Execution Steps

1. **Parse user input**: Extract `channel_id`
2. **Load specification**: Use `MarketingSpecParser`
3. **Find channel**: Search `spec.channels` for matching `id`
4. **Return channel**: Format as YAML with constraints

## Example

```yaml
channel:
  id: "twitter"
  name: "Twitter/X"
  type: "social_media"
  platform: "twitter"
  audiences:
    - "Developers"
    - "AI Engineers"
  content_types:
    - "short_text"
    - "images"
    - "video"
  constraints:
    max_text_length: 280
    max_hashtags: 5
    image_formats: ["png", "jpg", "gif"]
  tool_id: "buffer-scheduler"
```

## Notes

- **Critical for content generation**: Use `constraints` to validate output
- Check `max_text_length` before generating posts
- Use `content_types` to determine what media to include

