---
description: Retrieve brand guidelines, style rules, and content constraints
argument-hint: "<template_id>"
allowed-tools: read_file, grep
model-override: null
---

## Purpose

Retrieve a specific **ContentTemplate** entity by ID. This provides:
- Writing tone and style guidelines
- Content constraints (length, structure)
- Forbidden words/phrases
- Example content

## Inputs

```yaml
template_id: string  # Required - Template identifier (e.g., "technical-blog-post")
```

## Output

```yaml
content_template:
  id: string (pattern: ^[a-z0-9-]+$)
  name: string
  type: enum[social_post, blog_article, email, landing_page]
  tone: enum[friendly, professional, technical, casual, educational]
  style_guidelines: array[string] (≥1 item)
  project_id: string
  constraints: object (optional)
  examples: array[string] (optional, URLs or text samples)
```

## Validation Rules

- **VR-CT01**: `id` must be unique
- **VR-CT02**: `project_id` must reference existing project
- **VR-CT03**: `style_guidelines` must have at least 1 item
- **VR-CT04**: If `constraints.min_length` and `max_length` both provided, min < max
- **VR-CT05**: `tone` should align with project `brand_voice` (warning if mismatch)

## Execution Steps

1. **Parse user input**: Extract `template_id`
2. **Load specification**: Use `MarketingSpecParser`
3. **Find template**: Search `spec.content_templates` for matching `id`
4. **Return template**: Format as YAML with guidelines

## Example

```yaml
content_template:
  id: "technical-blog-post"
  name: "Technical Blog Post Template"
  type: "blog_article"
  tone: "technical"
  style_guidelines:
    - "Use code examples to illustrate concepts"
    - "Define technical terms on first use"
    - "Include practical use cases"
    - "End with clear call-to-action"
  project_id: "metaspec"
  constraints:
    min_length: 800
    max_length: 2000
    required_sections:
      - "Introduction"
      - "Problem Statement"
      - "Solution"
      - "Example"
      - "Conclusion"
    forbidden_words:
      - "obviously"
      - "simply"
      - "just"
  examples:
    - "https://metaspec.dev/blog/introducing-metaspec"
```

## Notes

- **Critical for brand consistency**: Always use template guidelines
- Follow `style_guidelines` precisely
- Respect `constraints.forbidden_words`
- Check `examples` for reference style

