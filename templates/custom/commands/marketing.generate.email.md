---
description: Generate email campaign content with subject line optimization
argument-hint: "<campaign_id> <template_id> [segment]"
allowed-tools: read_file, grep
model-override: null
priority: P1
---

## Purpose

Generate **email campaign content** including:
- Subject line (optimized for open rates)
- Preview text
- HTML body
- Plain text version
- Clear CTA

## Inputs

```yaml
campaign_id: string       # Required - Campaign context
template_id: string       # Required - Email template
segment: string           # Optional - Audience segment (e.g., "developers", "enterprise")
```

## Output

```yaml
email:
  subject: string                  # Subject line (≤50 chars recommended)
  preview_text: string             # First line visible in inbox (≤90 chars)
  body_html: string                # HTML version
  body_plain: string               # Plain text version
  cta_text: string                 # Call-to-action button text
  cta_url: string                  # CTA link
  estimated_open_rate: float       # Predicted open rate (0-1)
  spam_score: integer              # Spam likelihood (0-10, lower better)
```

## Generation Strategy

1. **Load context**:
   - Campaign, template, project

2. **Craft subject line**:
   - Personalization (if segment known)
   - Action verbs
   - Urgency (for conversion campaigns)
   - A/B test variants

3. **Structure email**:
   - **Preview text**: Extend subject, create curiosity
   - **Header**: Logo, brand identity
   - **Body**: Problem → Solution → Benefits
   - **CTA**: Single, clear action
   - **Footer**: Unsubscribe, social links

4. **Optimize**:
   - Mobile-friendly HTML
   - Plain text fallback
   - Avoid spam triggers
   - Test links

## Example Output

```yaml
email:
  subject: "🚀 MetaSpec v0.6.0 is Live!"
  preview_text: "Transform your specifications into production code with AI"
  body_html: |
    <!DOCTYPE html>
    <html>
    <body>
      <div style="max-width: 600px; margin: 0 auto;">
        <h1>MetaSpec v0.6.0 Released</h1>
        <p>We're excited to announce...</p>
        <a href="https://metaspec.dev?utm_source=email" style="...">Get Started</a>
      </div>
    </body>
    </html>
  body_plain: |
    MetaSpec v0.6.0 Released
    
    We're excited to announce...
    
    Get Started: https://metaspec.dev?utm_source=email
  cta_text: "Get Started"
  cta_url: "https://metaspec.dev?utm_source=email&utm_campaign=v060-launch"
  estimated_open_rate: 0.28
  spam_score: 2
```

## Notes

- **Priority P1**
- Use UTM parameters for tracking
- Test subject lines for open rates
- Comply with CAN-SPAM Act

