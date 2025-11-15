---
description: Schedule content for future publication via tool integration
argument-hint: "<content> <channel_id> <tool_id> <scheduled_time>"
allowed-tools: read_file, grep, run_terminal_cmd
model-override: null
priority: P1
warning: "⚠️ NOT IDEMPOTENT - Creates side effects (schedules content)"
---

## Purpose

**Schedule content** for future publication using integrated tools (MCP or REST API).

## Inputs

```yaml
content: object               # Required - Content to schedule
  type: enum[post, article, email]
  text: string
  media: array[string]        # Optional - Image/video URLs
channel_id: string            # Required - Target channel
tool_id: string               # Required - Tool to use (must support "schedule" capability)
scheduled_time: string        # Required - ISO 8601 datetime (e.g., "2025-11-20T10:00:00Z")
```

## Output

```yaml
schedule_result:
  scheduled_id: string          # Unique scheduling ID
  status: enum[scheduled, pending, failed]
  publish_time: string          # Confirmed publish time (ISO 8601)
  tool_used: string             # Tool that handled scheduling
  channel_name: string          # Human-readable channel name
  preview_url: string           # Optional - Preview link
  errors: array[string]         # Any errors encountered
```

## Execution Steps

1. **Validate inputs**:
   - Check `channel_id` exists
   - Check `tool_id` exists and status == "active"
   - Verify tool has "schedule" capability
   - Validate `scheduled_time` is in future

2. **Get tool configuration**:
   - Load tool via `/marketing.tool <tool_id>`
   - Extract `mcp_config` or `api_config`

3. **Schedule content**:
   - **If MCP tool**: Call MCP server's schedule operation
   - **If REST API**: POST to `api_config.base_url/schedule`
   - **If manual**: Return error (manual tools don't support scheduling)

4. **Handle response**:
   - Parse scheduling ID
   - Confirm publish time
   - Return result

## Example Usage

```
AI Agent: /marketing.execute.schedule 
  content: {type: "post", text: "🚀 New release!"} 
  channel_id: "twitter" 
  tool_id: "buffer-scheduler" 
  scheduled_time: "2025-11-20T10:00:00Z"
```

## Example Output

```yaml
schedule_result:
  scheduled_id: "buf_abc123"
  status: "scheduled"
  publish_time: "2025-11-20T10:00:00Z"
  tool_used: "buffer-scheduler"
  channel_name: "Twitter/X"
  preview_url: "https://buffer.com/preview/abc123"
  errors: []
```

## Error Handling

- **Tool not found**: List available tools with "schedule" capability
- **Tool inactive**: Cannot schedule with inactive tools
- **Past scheduled_time**: Must be in future
- **API error**: Return error message from tool

## Notes

- **⚠️ NOT IDEMPOTENT**: Each call creates a new scheduled post
- **Priority P1** (not MVP)
- Requires tool integration (MCP or REST API)
- Check tool `capabilities` includes "schedule"
- Use for automation workflows
- Consider timezone handling (ISO 8601 with Z suffix = UTC)

