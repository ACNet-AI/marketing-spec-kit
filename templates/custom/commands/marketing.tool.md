---
description: Retrieve tool integration details (MCP server or REST API configuration)
argument-hint: "<tool_id>"
allowed-tools: read_file, grep
model-override: null
---

## Purpose

Retrieve a specific **Tool** entity by ID. This provides:
- Tool type (MCP, REST API, or manual)
- Capabilities (schedule, publish, analyze)
- Integration configuration
- Associated channels

## Inputs

```yaml
tool_id: string  # Required - Tool identifier (e.g., "buffer-scheduler")
```

## Output

```yaml
tool:
  id: string (pattern: ^[a-z0-9-]+$)
  name: string
  type: enum[mcp, rest_api, manual]
  capabilities: array[string] (≥1 item)
  status: enum[active, inactive, testing]
  mcp_config: object (if type == mcp)
  api_config: object (if type == rest_api)
  channel_ids: array[string] (optional)
```

## Validation Rules

- **VR-T01**: `id` must be unique
- **VR-T02**: If `type` == "mcp", `mcp_config` must be provided
- **VR-T03**: If `type` == "rest_api", `api_config` must be provided
- **VR-T04**: `capabilities` must have at least 1 item
- **VR-T05**: If `api_config.base_url` provided, must be HTTPS
- **VR-T06**: `channel_ids` (if provided) must reference existing channels

## Execution Steps

1. **Parse user input**: Extract `tool_id`
2. **Load specification**: Use `MarketingSpecParser`
3. **Find tool**: Search `spec.tools` for matching `id`
4. **Check status**: Warn if `status` != "active"
5. **Return tool**: Format as YAML with config

## Example

```yaml
tool:
  id: "buffer-scheduler"
  name: "Buffer Social Scheduler"
  type: "rest_api"
  capabilities:
    - "schedule"
    - "publish"
    - "analytics"
  status: "active"
  api_config:
    base_url: "https://api.bufferapp.com"
    auth_type: "oauth2"
  channel_ids:
    - "twitter"
```

## Notes

- **Read-only** operation
- Use for automation (schedule/publish commands)
- Check `status` before attempting integration
- MCP tools prioritized over REST APIs

