---
description: Retrieve project brand identity, core values, and target audience
argument-hint: "(no arguments - returns root project)"
allowed-tools: read_file, grep
model-override: null
---

## Purpose

Retrieve the **Project** entity from the marketing specification. This provides:
- Brand identity (name, tagline, voice)
- Target audience segments
- Value propositions
- Social media handles

## Inputs

**None** - This command always returns the root project entity.

## Output

Returns the complete Project entity in YAML format:

```yaml
project:
  name: string
  tagline: string (≤100 chars)
  brand_voice: enum[Technical, Friendly, Professional, Casual, Educational]
  website: string (HTTPS URL)
  target_audience: array[string] (≥1 item)
  value_propositions: array[string] (≥1 item)
  logo_url: string (optional, HTTPS URL)
  social_handles: object (optional, platform: handle)
```

## Validation Rules

- **VR-P01**: `name` must be non-empty and unique
- **VR-P02**: `tagline` must be ≤ 100 characters
- **VR-P03**: `website` must be valid HTTPS URL
- **VR-P04**: `target_audience` must have at least 1 item
- **VR-P05**: `brand_voice` must match standard archetypes
- **VR-P06**: If `social_handles` provided, handles must be valid format

## Execution Steps

1. **Locate specification file**: Search for `*.yaml` or `*.json` in current directory or `specs/` subdirectory
2. **Parse specification**: Use `MarketingSpecParser` to load and validate
3. **Extract project**: Return `spec.project` entity
4. **Format output**: Display as YAML

## Example Usage

```
AI Agent: /marketing.project
→ Returns MetaSpec project with brand voice "Technical" and target audiences
```

## Example Output

```yaml
project:
  name: "MetaSpec"
  tagline: "Specification-Driven Development for GenAI Era"
  brand_voice: "Technical"
  website: "https://metaspec.dev"
  target_audience:
    - "Developers"
    - "AI Engineers"
    - "Open Source Maintainers"
  value_propositions:
    - "Transform specifications into production-ready code"
    - "AI-assisted development with best practices"
    - "Extensible toolkit architecture"
  logo_url: "https://metaspec.dev/logo.png"
  social_handles:
    twitter: "@metaspec"
    github: "metaspec"
    discord: "metaspec-community"
```

## Error Handling

- **No spec file found**: List available `.yaml`/`.json` files and prompt user
- **Parse error**: Display parsing error with line number and fix suggestion
- **Validation error**: Display validation errors (should not happen for project)

## Notes

- This is a **read-only** operation (no side effects)
- Always returns exactly one project (root entity)
- Use this before generating content to understand brand voice and audience

