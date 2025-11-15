---
description: Retrieve product features, positioning, and target audience
argument-hint: "<product_id>"
allowed-tools: read_file, grep
model-override: null
---

## Purpose

Retrieve a specific **Product** entity by ID. This provides:
- Product name and description
- Key features (3-5 recommended)
- Target audience
- Positioning statement
- Launch date

## Inputs

```yaml
product_id: string  # Required - Product identifier (e.g., "speckit-generator")
```

## Output

Returns the complete Product entity in YAML format:

```yaml
product:
  id: string (pattern: ^[a-z0-9-]+$)
  name: string
  description: string (≤500 chars)
  project_id: string
  target_audience: array[string] (≥1 item)
  key_features: array[string] (≥1 item, recommended 3-5)
  positioning: string (optional, ≤200 chars)
  launch_date: string (optional, ISO 8601: YYYY-MM-DD)
```

## Validation Rules

- **VR-PR01**: `id` must be unique within project
- **VR-PR02**: `project_id` must reference existing project
- **VR-PR03**: `description` must be ≤ 500 characters
- **VR-PR04**: `key_features` should have 3-5 items (warning if outside range)
- **VR-PR05**: If `launch_date` provided, must not be in future (for launched products)

## Execution Steps

1. **Parse user input**: Extract `product_id` from command arguments
2. **Load specification**: Use `MarketingSpecParser`
3. **Find product**: Search `spec.products` for matching `id`
4. **Validate existence**: Error if product not found
5. **Return product**: Format as YAML

## Example Usage

```
AI Agent: /marketing.product speckit-generator
→ Returns Speckit Generator product details for feature announcement
```

## Example Output

```yaml
product:
  id: "speckit-generator"
  name: "Speckit Generator"
  description: "Generate domain-specific specification toolkits from templates with AI assistance"
  project_id: "metaspec"
  target_audience:
    - "Developers"
    - "Tool creators"
  key_features:
    - "Template-based generation"
    - "AI-powered customization"
    - "Built-in validation"
  positioning: "The fastest way to create specification toolkits"
  launch_date: "2025-11-01"
```

## Error Handling

- **No spec file found**: Prompt user to create specification
- **Product not found**: List available product IDs
- **Invalid product_id format**: Must match `^[a-z0-9-]+$`

## Notes

- **Read-only** operation
- Use for content generation about specific products
- `key_features` should be concise (1-2 sentences each)
- `positioning` differentiates from competitors

