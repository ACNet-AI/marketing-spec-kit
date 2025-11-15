---
description: Generate landing page copy with conversion optimization
argument-hint: "<campaign_id> <product_id> [template_id]"
allowed-tools: read_file, grep
model-override: null
priority: P1
---

## Purpose

Generate **landing page copy** optimized for conversions:
- Hero section (headline + subheadline)
- Features section
- Benefits section
- Social proof (testimonials)
- Clear CTAs

## Inputs

```yaml
campaign_id: string       # Required - Campaign context
product_id: string        # Required - Product to promote
template_id: string       # Optional - Landing page template
```

## Output

```yaml
landing_page:
  hero_headline: string              # Main headline (5-10 words)
  hero_subheadline: string           # Supporting text (10-20 words)
  hero_cta_text: string              # Primary CTA button
  features: array[object]            # 3-5 features with icons
  benefits: array[string]            # "You will be able to..." statements
  social_proof: array[object]        # Testimonials or logos
  secondary_cta_text: string         # Bottom CTA
  meta_title: string                 # SEO title
  meta_description: string           # SEO description
```

## Generation Strategy

1. **Load context**:
   - Campaign, product, project

2. **Hero section**:
   - Headline: Clear value proposition
   - Subheadline: Explain who it's for
   - CTA: Action-oriented ("Start Free Trial", "Get Started")

3. **Features** (3-5):
   - Use `product.key_features`
   - Icon + Title + Short description
   - Focus on differentiation

4. **Benefits**:
   - Transform features → outcomes
   - "You will be able to..."
   - Address pain points

5. **Social proof**:
   - Testimonials (if available)
   - Company logos (if B2B)
   - Stats (users, downloads)

## Example Output

```yaml
landing_page:
  hero_headline: "Transform Specifications Into Production Code"
  hero_subheadline: "MetaSpec uses AI to generate domain-specific toolkits from your specifications in minutes, not weeks"
  hero_cta_text: "Get Started Free"
  features:
    - icon: "⚡"
      title: "Lightning Fast Generation"
      description: "Create complete toolkits in under 5 minutes"
    - icon: "🤖"
      title: "AI-Powered Customization"
      description: "Intelligent code generation with best practices"
    - icon: "✅"
      title: "Built-in Validation"
      description: "Automatic testing and quality checks"
  benefits:
    - "Save 80% of development time on repetitive tool creation"
    - "Maintain consistent code quality across all toolkits"
    - "Focus on domain logic, not boilerplate code"
  social_proof:
    - quote: "MetaSpec cut our toolkit development time from weeks to hours"
      author: "Jane Doe, CTO at TechCorp"
    - quote: "The best tool for building developer tools"
      author: "John Smith, Open Source Maintainer"
  secondary_cta_text: "Start Building Today"
  meta_title: "MetaSpec - AI-Powered Specification Toolkit Generator"
  meta_description: "Transform your specifications into production-ready code with MetaSpec. AI-assisted development, built-in validation, and best practices included."
```

## Notes

- **Priority P1**
- Use conversion-focused copywriting
- A/B test headlines and CTAs
- Mobile-responsive design assumed

