---
description: Publish content immediately via tool integration
argument-hint: "<content> <channel_id> <tool_id>"
allowed-tools: read_file, grep, run_terminal_cmd
model-override: null
priority: P1
warning: "⚠️ NOT IDEMPOTENT - Creates side effects (publishes content)"
---

## Purpose

**Publish content immediately** using integrated tools (MCP or REST API).

## Inputs

```yaml
content: object               # Required - Content to publish
  type: enum[post, article, email]
  text: string
  media: array[string]        # Optional - Image/video URLs
  hashtags: array[string]     # Optional - For social media
channel_id: string            # Required - Target channel
tool_id: string               # Required - Tool to use (must support "publish" capability)
```

## Output

```yaml
publish_result:
  published_id: string          # Unique post ID
  status: enum[published, pending, failed]
  publish_time: string          # Actual publish time (ISO 8601)
  url: string                   # Public URL of published content
  channel_name: string          # Human-readable channel name
  analytics_url: string         # Optional - Link to analytics
  errors: array[string]         # Any errors encountered
```

## Execution Steps

1. **Validate inputs**:
   - Check `channel_id` exists
   - Check `tool_id` exists and status == "active"
   - Verify tool has "publish" capability
   - Validate content meets channel constraints

2. **Get tool configuration**:
   - Load tool via `/marketing.tool <tool_id>`
   - Extract `mcp_config` or `api_config`

3. **Publish content**:
   - **If MCP tool**: Call MCP server's publish operation
   - **If REST API**: POST to `api_config.base_url/publish`
   - **If manual**: Return error (requires manual action)

4. **Handle response**:
   - Parse published post ID
   - Get public URL
   - Return result with analytics link

## Example Usage

```
AI Agent: /marketing.execute.publish 
  content: {type: "post", text: "🚀 MetaSpec v0.6.0 is live!", hashtags: ["#DevTools", "#OpenSource"]} 
  channel_id: "twitter" 
  tool_id: "buffer-scheduler"
```

## Example Output

```yaml
publish_result:
  published_id: "tw_1234567890"
  status: "published"
  publish_time: "2025-11-15T14:30:00Z"
  url: "https://twitter.com/metaspec/status/1234567890"
  channel_name: "Twitter/X"
  analytics_url: "https://buffer.com/analytics/1234567890"
  errors: []
```

## Error Handling

- **Tool not found**: List available tools with "publish" capability
- **Tool inactive**: Cannot publish with inactive tools
- **Content too long**: Exceeds channel `constraints.max_text_length`
- **API error**: Return error message from tool
- **Rate limit**: Tool API rate limit exceeded

## Notes

- **⚠️ NOT IDEMPOTENT**: Each call publishes content publicly
- **Priority P1** (not MVP)
- Requires tool integration (MCP or REST API)
- Check tool `capabilities` includes "publish"
- **Use with caution**: Content is immediately visible
- Consider using `/marketing.execute.schedule` for review workflows
- Always validate content against channel constraints first

