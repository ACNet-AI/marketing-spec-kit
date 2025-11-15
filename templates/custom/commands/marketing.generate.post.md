---
description: Generate platform-specific social media post (short-form content)
argument-hint: "<campaign_id> <channel_id> [tone] [hashtags]"
allowed-tools: read_file, grep
model-override: null
priority: P0
---

## Purpose

Generate a **platform-specific social media post** based on:
- Campaign goals and messaging
- Channel constraints (character limits)
- Brand voice and tone
- Target audience

## Inputs

```yaml
campaign_id: string       # Required - Campaign to promote
channel_id: string        # Required - Channel to publish on
tone: string              # Optional - Overrides campaign/project tone
hashtags: array[string]   # Optional - Suggested hashtags
```

## Output

```yaml
post:
  text: string                    # Main post content
  hashtags: array[string]         # Recommended hashtags
  character_count: integer        # Total characters used
  estimated_reach: integer        # Estimated audience reach
  fits_constraints: boolean       # Whether post meets channel limits
  warnings: array[string]         # Any constraint violations
```

## Generation Strategy

1. **Load context**:
   - Get campaign via `/marketing.campaign <campaign_id>`
   - Get channel via `/marketing.channel <channel_id>`
   - Get project via `/marketing.project`

2. **Understand constraints**:
   - Check `channel.constraints.max_text_length`
   - Check `channel.constraints.max_hashtags`
   - Note `channel.content_types`

3. **Generate content**:
   - Use `project.brand_voice` or override `tone`
   - Align with `campaign.goal`:
     * awareness → Educational, value-focused
     * consideration → Problem-solution
     * conversion → Action-oriented, urgent
   - Address `campaign.target_audience`
   - Include `campaign.product_ids` features if relevant

4. **Optimize for platform**:
   - Twitter: Hook + value + CTA (≤280 chars)
   - LinkedIn: Professional, longer form
   - Reddit: Conversational, community-focused

5. **Add hashtags**:
   - Max `channel.constraints.max_hashtags`
   - Mix brand + topic + trending tags
   - Separate from main text count

6. **Validate**:
   - Check character count
   - Ensure all constraints met
   - Provide warnings if over limit

## Example Usage

```
AI Agent: /marketing.generate.post metaspec-v060-launch twitter Technical ["#OpenSource"]
```

## Example Output

```yaml
post:
  text: "🚀 MetaSpec v0.6.0 is here! Transform specifications into production-ready code with AI-assisted development. Perfect for developers building tools and frameworks. Try the Speckit Generator today → metaspec.dev"
  hashtags:
    - "#OpenSource"
    - "#DevTools"
    - "#GenAI"
  character_count: 247
  estimated_reach: 5000
  fits_constraints: true
  warnings: []
```

## Content Best Practices

- **Hook** (first 10 words): Grab attention
- **Value** (middle): What's in it for them?
- **CTA** (end): Clear next action
- **Emojis**: 1-2 for engagement (if appropriate for brand_voice)
- **Links**: Shortened URLs, track with UTM parameters
- **Timing**: Consider `campaign.start_date`

## Error Handling

- **Campaign not found**: List available campaigns
- **Channel not found**: List available channels
- **Over character limit**: Provide shorter version
- **Missing constraints**: Use platform defaults

## Notes

- **NOT idempotent**: Each call generates new content
- Always validate against channel constraints before publishing
- Use `/marketing.channel` first to understand limits
- Consider A/B testing by generating multiple variations

