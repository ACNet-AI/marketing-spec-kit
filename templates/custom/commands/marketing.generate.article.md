---
description: Generate long-form blog article with SEO optimization
argument-hint: "<campaign_id> <template_id> [product_id] [length]"
allowed-tools: read_file, grep
model-override: null
priority: P1
---

## Purpose

Generate a **long-form blog article** (800-3000 words) based on:
- Campaign messaging
- Content template guidelines
- Product features (if specified)
- SEO best practices

## Inputs

```yaml
campaign_id: string       # Required - Campaign context
template_id: string       # Required - Content template with style guidelines
product_id: string        # Optional - Specific product to feature
length: integer           # Optional - Target word count (default: 1500)
```

## Output

```yaml
article:
  title: string                   # SEO-optimized title (≤60 chars)
  subtitle: string                # Engaging subtitle
  body: string                    # Markdown content
  word_count: integer             # Actual word count
  reading_time: integer           # Estimated minutes
  seo_keywords: array[string]     # Primary keywords
  meta_description: string        # For <meta> tag (≤160 chars)
  sections: array[string]         # Section headings
  internal_links: array[string]   # Suggested internal links
  external_links: array[string]   # Reference URLs
```

## Generation Strategy

1. **Load context**:
   - Get campaign via `/marketing.campaign`
   - Get template via `/marketing.content_template`
   - Get product via `/marketing.product` (if provided)
   - Get project via `/marketing.project`

2. **Follow template**:
   - Use `template.style_guidelines`
   - Respect `template.constraints` (min/max length)
   - Match `template.tone`
   - Include `template.constraints.required_sections`
   - Avoid `template.constraints.forbidden_words`

3. **Structure article**:
   - **Introduction**: Problem + hook
   - **Problem Statement**: Pain points
   - **Solution**: How product/campaign addresses it
   - **Examples**: Code snippets, use cases
   - **Benefits**: Value propositions
   - **Conclusion**: Summary + CTA

4. **SEO optimization**:
   - Title includes primary keyword
   - Headings (H2, H3) with keywords
   - Meta description compelling
   - Internal links to related content
   - Alt text for images (if applicable)

5. **Brand alignment**:
   - Use `project.brand_voice`
   - Reference `project.value_propositions`
   - Address `campaign.target_audience`

## Example Output

```yaml
article:
  title: "Specification-Driven Development: Transform Specs into Production Code"
  subtitle: "How MetaSpec v0.6.0 uses AI to generate domain-specific toolkits"
  body: |
    # Introduction
    
    Building developer tools from scratch is time-consuming...
    
    [Full Markdown content here]
  word_count: 1847
  reading_time: 8
  seo_keywords:
    - "specification-driven development"
    - "AI code generation"
    - "developer tooling"
  meta_description: "Learn how MetaSpec v0.6.0 transforms specifications into production-ready code with AI-assisted development and best practices."
  sections:
    - "Introduction"
    - "The Challenge of Tool Development"
    - "How MetaSpec Solves This"
    - "Real-World Example"
    - "Getting Started"
  internal_links:
    - "/docs/getting-started"
    - "/blog/introducing-metaspec"
  external_links:
    - "https://github.com/metaspec/metaspec"
```

## Notes

- **Priority P1** (not MVP critical)
- Generation takes longer (~30-60 seconds)
- Always follow `template.style_guidelines`
- Include code examples for technical content
- Proofread for `forbidden_words`

