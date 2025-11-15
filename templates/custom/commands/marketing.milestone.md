---
description: Retrieve milestone event details and associated campaigns
argument-hint: "<milestone_id>"
allowed-tools: read_file, grep
model-override: null
---

## Purpose

Retrieve a specific **Milestone** entity by ID. This provides:
- Milestone date and type
- Associated products and campaigns
- Event description
- Status (planned, in-progress, completed)

## Inputs

```yaml
milestone_id: string  # Required - Milestone identifier (e.g., "v060-release")
```

## Output

```yaml
milestone:
  id: string (pattern: ^[a-z0-9-]+$)
  name: string
  type: enum[version_release, feature_launch, community_event, announcement]
  date: string (ISO 8601: YYYY-MM-DD)
  description: string (optional, ≤500 chars)
  project_id: string
  product_ids: array[string] (optional)
  campaign_ids: array[string] (optional)
  status: enum[planned, in_progress, completed, cancelled]
```

## Validation Rules

- **VR-M01**: `id` must be unique
- **VR-M02**: `project_id` must reference existing project
- **VR-M03**: `product_ids` (if provided) must reference existing products
- **VR-M04**: `campaign_ids` (if provided) must reference existing campaigns
- **VR-M05**: `date` should not be > 1 year in future (warning)

## Execution Steps

1. **Parse user input**: Extract `milestone_id`
2. **Load specification**: Use `MarketingSpecParser`
3. **Find milestone**: Search `spec.milestones` for matching `id`
4. **Return milestone**: Format as YAML with associations

## Example

```yaml
milestone:
  id: "v060-release"
  name: "MetaSpec v0.6.0 Release"
  type: "version_release"
  date: "2025-11-14"
  description: "Major release with SDS/SDD commands and speckit generator"
  project_id: "metaspec"
  product_ids:
    - "speckit-generator"
    - "sds-commands"
  campaign_ids:
    - "metaspec-v060-launch"
  status: "completed"
```

## Notes

- **Read-only** operation
- Use to coordinate marketing around releases
- Check `campaign_ids` to see associated marketing activities
- Use `date` for content scheduling

