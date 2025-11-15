---
description: Retrieve campaign goals, budget, timeline, and KPIs
argument-hint: "<campaign_id>"
allowed-tools: read_file, grep
model-override: null
---

## Purpose

Retrieve a specific **Campaign** entity by ID. This provides:
- Campaign goal (AIDA funnel stage)
- Budget allocation
- Timeline (start/end dates)
- Target channels
- KPIs (CTR, conversions, ROAS)

## Inputs

```yaml
campaign_id: string  # Required - Campaign identifier (e.g., "launch-campaign")
```

## Output

Returns the complete Campaign entity in YAML format:

```yaml
campaign:
  id: string (pattern: ^[a-z0-9-]+$)
  name: string
  goal: enum[awareness, consideration, conversion]
  project_id: string
  product_ids: array[string] (optional)
  target_audience: array[string] (≥1 item)
  budget: number (>0)
  start_date: string (ISO 8601: YYYY-MM-DD)
  end_date: string (ISO 8601: YYYY-MM-DD)
  channels: array[string] (≥1 item, channel IDs)
  kpis: object (optional)
  status: enum[draft, scheduled, active, paused, completed]
```

## Validation Rules

- **VR-C01**: `id` must be unique within project
- **VR-C02**: `project_id` must reference existing project
- **VR-C03**: `product_ids` (if provided) must all reference existing products
- **VR-C04**: `budget` must be > 0
- **VR-C05**: `start_date` < `end_date`
- **VR-C06**: `start_date` should not be in past (warning)
- **VR-C07**: `channels` must all reference existing channel entities
- **VR-C08**: If `kpis.target_ctr` provided, must be between 0 and 1
- **VR-C09**: If `kpis.target_roas` provided, should be ≥ 3 for profitability (warning)

## Execution Steps

1. **Parse user input**: Extract `campaign_id`
2. **Load specification**: Use `MarketingSpecParser`
3. **Find campaign**: Search `spec.campaigns` for matching `id`
4. **Validate existence**: Error if campaign not found
5. **Return campaign**: Format as YAML with KPIs

## Example Usage

```
AI Agent: /marketing.campaign metaspec-v060-launch
→ Returns v0.6.0 launch campaign parameters for content generation
```

## Example Output

```yaml
campaign:
  id: "metaspec-v060-launch"
  name: "MetaSpec v0.6.0 Launch"
  goal: "awareness"
  project_id: "metaspec"
  product_ids:
    - "speckit-generator"
    - "sds-commands"
  target_audience:
    - "Developers"
    - "AI Engineers"
    - "Open Source Maintainers"
  budget: 500.0
  start_date: "2025-11-15"
  end_date: "2025-11-29"
  channels:
    - "twitter"
    - "reddit-programming"
    - "devto-blog"
  kpis:
    target_impressions: 50000
    target_ctr: 0.05  # 5% CTR
    target_conversions: 100
    target_roas: 5.0
  status: "scheduled"
```

## Error Handling

- **Campaign not found**: List available campaign IDs
- **Invalid campaign_id format**: Must match `^[a-z0-9-]+$`
- **Past dates**: Warn if campaign dates are outdated

## Notes

- **Read-only** operation
- Use `goal` to determine content tone (awareness → educational, conversion → action-oriented)
- Check `budget` to gauge campaign scale
- Reference `channels` to understand distribution strategy
- Use `kpis` to set content performance targets

