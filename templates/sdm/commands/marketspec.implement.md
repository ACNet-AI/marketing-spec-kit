---
name: marketspec.implement
description: Generate executable code and operational configurations
layer: sdm
status: implemented
type: core
category: Core Flow
source: Adapted from metaspec.sdd.implement
version: 0.4.0
---

# /marketspec.implement 🔴 Core

**Purpose**: Execute all tasks to generate executable campaign code and configurations.

**Category**: Core Flow (Essential Workflow)  
**Output**: 
- `src/campaigns/{sequence}-{name}.py` - Executable campaign code ⭐
- `config/{sequence}-{name}.yaml` - Campaign configuration
- `templates/{sequence}-{name}/` - Content templates  
**Adapted from**: `metaspec.sdd.implement`

---

## Purpose

This is the **implementation command** that generates:
1. **Executable code** (`src/`) - Python scripts that call MCP tools
2. **Configuration** (`config/`) - YAML configuration files
3. **Templates** (`templates/`) - Content templates

**Key Principle** (from [Anthropic's Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)):
- Generate **code that calls MCP tools**, not just configuration files
- Use code execution for efficiency: progressive disclosure, context efficiency, control flow
- Separate configuration (DATA) from implementation (CODE)

---

## Directory Structure

```
specs/                              ← WHAT (战略规范 - Markdown)
└── 001-q1-github-stars/
    ├── spec.md
    ├── plan.md
    └── tasks.md

config/                             ← 活动配置 (YAML - 可调参数)
└── 001-q1-campaign.yaml            ← Campaign config ⭐

templates/                          ← 内容模板 (Markdown/Text)
└── 001-q1/
    ├── tweet-template.md           ← Twitter template
    └── blog-post-template.md       ← Blog template

data/                               ← 收集的数据 (JSON - 运行时)
└── 001-q1/
    └── (created during execution)

src/                                ← HOW (执行代码 - Python)
├── campaigns/
│   └── 001_q1_campaign.py          ← Main execution script ⭐
└── shared/
    ├── mcp_tools/
    │   ├── github.py               ← GitHub MCP tool wrapper
    │   ├── twitter.py
    │   └── analytics.py
    ├── config_loader.py
    └── template_renderer.py
```

---

## Command Usage

```
/marketspec.implement
/marketspec.implement --dry-run
/marketspec.implement --language [python|typescript]
```

**Examples**:
```
/marketspec.implement                        # Generate Python (default)
/marketspec.implement --language typescript  # Generate TypeScript
/marketspec.implement --dry-run              # Preview structure
```

---

## Prerequisites

- **Required**: Task breakdown from `/marketspec.tasks`
- **Required**: Marketing specification from `/marketspec.specify`
- **Required**: Marketing plan from `/marketspec.plan`
- **Optional**: Constitution principles (`memory/constitution.md`)

---

## Execution Steps

### Step 1: Check Prerequisites

**Required files**:
- `specs/{sequence}-{name}/tasks.md` - Task breakdown (MUST exist)
- `specs/{sequence}-{name}/spec.md` - Marketing specification (MUST exist)
- `specs/{sequence}-{name}/plan.md` - Marketing plan (MUST exist)

**If missing**:
- Stop and instruct user to run `/marketspec.tasks` first

**Validation**:
- ✅ Check all required documents exist
- ⚠️ Warn if constitution is missing
- Display status of all prerequisite files

---

### Step 2: Load Implementation Context

**Read specification documents**:

```yaml
context_files:
  - path: "specs/{sequence}-{name}/spec.md"
    extract:
      - campaign_name
      - objectives
      - kpis (name, baseline, target, tracking_tool)
      - timeline (start_date, end_date)
      - target_audience
      - budget_total
  
  - path: "specs/{sequence}-{name}/plan.md"
    extract:
      - channels (name, frequency, budget, role)
      - content_themes
      - budget_allocation
      - milestones
  
  - path: "specs/{sequence}-{name}/tasks.md"
    extract:
      - all_tasks (id, description, type)
      - task_dependencies
```

---

### Step 3: Generate Operational Configurations

#### 3.1 Create Main Configuration

**Output**: `config/{sequence}-{name}.yaml`

**Purpose**: Store adjustable campaign parameters (separate from code)

**Example**:
```yaml
# config/001-q1-github-stars.yaml
campaign:
  id: "001-q1-github-stars"
  name: "Q1 GitHub Stars Growth"
  spec_ref: "specs/001-q1-github-stars/spec.md"
  
kpis:
  github_stars:
    baseline: 100
    target: 500
    repo: "owner/marketing-spec-kit"
    tracking_tool: "github-api"
    
  website_traffic:
    baseline: 1000
    target: 5000
    tracking_tool: "google-analytics"

channels:
  twitter:
    frequency: "3 posts/day"
    budget: 1000
    times: ["09:00", "13:00", "17:00"]
    template: "templates/001-q1/tweet-template.md"
  
  devto:
    frequency: "2 posts/week"
    budget: 500
    template: "templates/001-q1/blog-post-template.md"

budget:
  total: 5000
  content_creation: 2000
  paid_promotion: 3000

timeline:
  start: "2025-01-01"
  end: "2025-03-31"
  milestones:
    - date: "2025-02-01"
      target_stars: 250
    - date: "2025-03-01"
      target_stars: 400
```

#### 3.2 Create Content Templates

**Output**: `templates/{sequence}-{name}/*.md`

**Purpose**: Store reusable content templates (separate from code)

**Example - Tweet Template**:
```markdown
<!-- templates/001-q1/tweet-template.md -->
---
theme: {{theme}}
hashtags: {{hashtags}}
link: {{link}}
---

🚀 {{theme}}

{{content}}

Learn more: {{link}}

{{hashtags}}
```

**Example - Blog Post Template**:
```markdown
<!-- templates/001-q1/blog-post-template.md -->
---
title: {{title}}
tags: {{tags}}
---

# {{title}}

## Introduction

{{intro}}

## Main Content

{{main_content}}

## Conclusion

{{conclusion}}

---

⭐ Star us on GitHub: {{repo_link}}
```

#### 3.3 Initialize Data Directory

**Output**: `data/{sequence}-{name}/`

**Purpose**: Directory for runtime data collection

**Create**:
- `data/{sequence}-{name}/` (empty directory)
- `data/{sequence}-{name}/.gitkeep` (to commit empty directory)

---

### Step 4: Generate Executable Code

#### 4.1 Create Main Campaign Script

**Output**: `src/campaigns/{sequence}_{name}.py`

**Purpose**: Executable script that orchestrates campaign execution using MCP tools

**Example**:
```python
# src/campaigns/001_q1_github_stars.py
"""
Q1 GitHub Stars Growth Campaign

Spec: specs/001-q1-github-stars/spec.md
Config: config/001-q1-github-stars.yaml

Objectives:
- Grow GitHub stars from 100 to 500
- Increase website traffic from 1000 to 5000 sessions

Channels: Twitter (3/day), Dev.to (2/week)
Budget: $5000
Timeline: Q1 2025 (Jan 1 - Mar 31)
"""

import asyncio
from datetime import datetime
from pathlib import Path

from ..shared.mcp_tools import github, twitter, devto, analytics
from ..shared.config_loader import load_config
from ..shared.template_renderer import render_template
from ..shared.data_saver import save_data


async def execute_001_q1_campaign():
    """Execute Q1 GitHub Stars Growth Campaign"""
    print('🚀 Starting Q1 GitHub Stars Growth Campaign\n')
    
    # Step 1: Load configuration
    config = await load_config('config/001-q1-github-stars.yaml')
    print(f"Campaign: {config['campaign']['name']}")
    print(f"Target: {config['kpis']['github_stars']['target']} stars\n")
    
    # Step 2: Publish Twitter content
    print('📱 Publishing Twitter content...')
    twitter_template = await render_template(
        config['channels']['twitter']['template'],
        {'theme': 'Getting Started', 'hashtags': '#OpenSource #DevTools'}
    )
    
    for time in config['channels']['twitter']['times']:
        await twitter.schedule_tweet(
            text=twitter_template,
            scheduled_time=time
        )
        print(f"  ✅ Scheduled tweet at {time}")
    
    # Step 3: Publish Dev.to articles
    print('\n📝 Publishing Dev.to articles...')
    blog_template = await render_template(
        config['channels']['devto']['template'],
        {
            'title': 'Getting Started with marketing-spec-kit',
            'tags': ['opensource', 'marketing', 'automation']
        }
    )
    
    await devto.publish_article(
        title='Getting Started with marketing-spec-kit',
        body=blog_template,
        published=True
    )
    print('  ✅ Published article on Dev.to')
    
    # Step 4: Track KPIs
    print('\n📊 Tracking KPIs...')
    
    # GitHub Stars (data filtered in execution environment, not in LLM context)
    current_stars = await github.get_star_count(
        repo=config['kpis']['github_stars']['repo']
    )
    target_stars = config['kpis']['github_stars']['target']
    stars_progress = (current_stars / target_stars) * 100
    print(f"  GitHub Stars: {current_stars}/{target_stars} ({stars_progress:.1f}%)")
    
    # Website Traffic
    traffic = await analytics.get_sessions(
        start_date=config['timeline']['start'],
        end_date='today'
    )
    target_traffic = config['kpis']['website_traffic']['target']
    traffic_progress = (traffic / target_traffic) * 100
    print(f"  Website Traffic: {traffic}/{target_traffic} ({traffic_progress:.1f}%)")
    
    # Step 5: Save data (persists in data/, not in LLM context)
    await save_data('data/001-q1/github-stars.json', {
        'timestamp': datetime.now().isoformat(),
        'value': current_stars,
        'target': target_stars,
        'progress': stars_progress
    })
    
    await save_data('data/001-q1/website-traffic.json', {
        'timestamp': datetime.now().isoformat(),
        'value': traffic,
        'target': target_traffic,
        'progress': traffic_progress
    })
    
    print('\n✅ Campaign execution completed')
    print(f'📂 Data saved to data/001-q1/')


if __name__ == '__main__':
    asyncio.run(execute_001_q1_campaign())
```

#### 4.2 Create MCP Tool Wrappers

**Output**: `src/shared/mcp_tools/*.py`

**Purpose**: Wrap MCP tools for progressive disclosure (load tool definitions on-demand)

**Example - GitHub Tool**:
```python
# src/shared/mcp_tools/github.py
"""
GitHub MCP Tool Wrapper

Progressive disclosure: Tool definitions loaded on-demand,
not upfront in LLM context (reduces token usage by 98%)

Reference: https://www.anthropic.com/engineering/code-execution-with-mcp
"""

from typing import Optional
from ..mcp_client import call_mcp_tool


async def get_star_count(repo: str) -> int:
    """
    Get star count for a GitHub repository
    
    Args:
        repo: Repository in format "owner/repo"
        
    Returns:
        Star count
    """
    result = await call_mcp_tool('github__get_star_count', {'repo': repo})
    return result['stars']


async def star_repo(repo: str) -> None:
    """Star a GitHub repository"""
    await call_mcp_tool('github__star_repo', {'repo': repo})


async def get_contributors(repo: str, limit: Optional[int] = None) -> list[str]:
    """Get repository contributors"""
    result = await call_mcp_tool('github__get_contributors', {
        'repo': repo,
        'limit': limit
    })
    return result['contributors']
```

**Example - Twitter Tool**:
```python
# src/shared/mcp_tools/twitter.py
"""Twitter MCP Tool Wrapper"""

from typing import Optional
from ..mcp_client import call_mcp_tool


async def schedule_tweet(
    text: str,
    scheduled_time: str,
    media_urls: Optional[list[str]] = None
) -> None:
    """Schedule a tweet for future posting"""
    await call_mcp_tool('twitter__schedule_tweet', {
        'text': text,
        'scheduledTime': scheduled_time,
        'mediaUrls': media_urls
    })


async def publish_tweet(
    text: str,
    media_urls: Optional[list[str]] = None
) -> None:
    """Publish a tweet immediately"""
    await call_mcp_tool('twitter__publish_tweet', {
        'text': text,
        'mediaUrls': media_urls
    })


async def get_tweet_metrics(tweet_id: str) -> dict:
    """Get tweet engagement metrics"""
    return await call_mcp_tool('twitter__get_tweet_metrics', {
        'tweetId': tweet_id
    })
```

#### 4.3 Create Utility Functions

**Output**: `src/shared/config_loader.py`, `src/shared/template_renderer.py`, `src/shared/data_saver.py`

**Purpose**: Helper functions for config loading, template rendering, data persistence

**Example - Config Loader**:
```python
# src/shared/config_loader.py
"""Configuration loading utilities"""

from pathlib import Path
import yaml


async def load_config(path: str) -> dict:
    """Load YAML configuration file"""
    config_path = Path(path)
    with config_path.open('r', encoding='utf-8') as f:
        return yaml.safe_load(f)
```

**Example - Template Renderer**:
```python
# src/shared/template_renderer.py
"""Template rendering utilities"""

import re
from pathlib import Path


async def render_template(template_path: str, vars: dict) -> str:
    """
    Render template with variables
    
    Simple template rendering (replace {{variable}} with values)
    """
    template_file = Path(template_path)
    template = template_file.read_text(encoding='utf-8')
    
    for key, value in vars.items():
        pattern = r'\{\{' + re.escape(key) + r'\}\}'
        template = re.sub(pattern, str(value), template)
    
    return template
```

**Example - Data Saver**:
```python
# src/shared/data_saver.py
"""Data persistence utilities"""

import json
from pathlib import Path


async def save_data(path: str, data: dict) -> None:
    """Save data to JSON file (for later review/analysis)"""
    data_path = Path(path)
    data_path.parent.mkdir(parents=True, exist_ok=True)
    
    with data_path.open('w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
```

#### 4.4 Create MCP Client

**Output**: `src/shared/mcp_client.py`

**Purpose**: Low-level MCP tool calling interface

**Example**:
```python
# src/shared/mcp_client.py
"""
MCP Client - Calls MCP tools via stdio transport

This is a simplified example. In production, use official MCP SDK:
- Python: mcp (https://github.com/modelcontextprotocol/python-sdk)
"""

import json
from typing import Any


async def call_mcp_tool(tool_name: str, input_data: dict) -> Any:
    """
    Call MCP tool
    
    In real implementation, this would:
    1. Connect to MCP server via stdio
    2. Send tool call request
    3. Receive and parse response
    4. Return result
    """
    print(f"[MCP] Calling tool: {tool_name}")
    print(f"[MCP] Input: {json.dumps(input_data, indent=2)}")
    
    # Placeholder - replace with actual MCP SDK call
    raise NotImplementedError(
        'MCP client not implemented - use mcp Python SDK'
    )
```

---

### Step 5: Generate README and Package Files

#### 5.1 Create src/README.md

**Output**: `src/README.md`

**Content**:
```markdown
# Campaign Execution Scripts

This directory contains executable Python scripts for running marketing campaigns.

## Structure

\`\`\`
src/
├── campaigns/
│   └── 001_q1_github_stars.py    ← Main campaign scripts
└── shared/
    ├── mcp_tools/                 ← MCP tool wrappers
    ├── config_loader.py           ← Config loading
    ├── template_renderer.py       ← Template rendering
    ├── data_saver.py              ← Data persistence
    └── mcp_client.py              ← MCP client interface
\`\`\`

## Running a Campaign

\`\`\`bash
# Install dependencies
uv sync  # or: pip install -r requirements.txt

# Run a campaign
python -m src.campaigns.001_q1_github_stars

# Or with uv
uv run python -m src.campaigns.001_q1_github_stars
\`\`\`

## MCP Tools Required

This project uses MCP tools for external integrations:

- **github-api**: GitHub repository interactions
- **twitter-api**: Twitter posting and scheduling
- **devto-api**: Dev.to article publishing
- **google-analytics**: Website traffic tracking

Configure MCP tools in your MCP settings or environment.

## Configuration

Campaign parameters are stored in \`config/\`:
- Adjust KPI targets, budgets, schedules without changing code
- Content templates in \`templates/\`
- Runtime data collected in \`data/\`
```

#### 5.2 Create pyproject.toml

**Output**: `pyproject.toml`

**Content**:
```toml
[project]
name = "marketing-campaigns"
version = "1.0.0"
description = "Executable marketing campaign scripts"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "mcp>=0.5.0",
    "pyyaml>=6.0.0",
    "aiofiles>=23.0.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv]
dev-dependencies = [
    "ruff>=0.1.0",
    "pytest>=7.0.0",
    "pytest-asyncio>=0.21.0",
]
```

#### 5.3 Create requirements.txt (Optional)

**Output**: `requirements.txt`

**Content**:
```
mcp>=0.5.0
pyyaml>=6.0.0
aiofiles>=23.0.0
```

---

### Step 6: Final Report

Generate implementation summary:

**Output**: Display to user

**Example**:
```
✅ Implementation Complete!

Generated Files:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 config/ + templates/ + data/
   ├─ config/001-q1-github-stars.yaml            ← Campaign config
   ├─ templates/001-q1/
   │  ├─ tweet-template.md                       ← Twitter template
   │  └─ blog-post-template.md                   ← Blog template
   └─ data/001-q1/                               ← Data directory (empty)

💻 src/ (Executable Code)
   ├─ campaigns/001_q1_github_stars.py           ← Main script ⭐
   ├─ shared/
   │  ├─ mcp_tools/
   │  │  ├─ github.py                            ← GitHub wrapper
   │  │  ├─ twitter.py                           ← Twitter wrapper
   │  │  └─ devto.py                             ← Dev.to wrapper
   │  ├─ config_loader.py                        ← Config loading
   │  ├─ template_renderer.py                    ← Template rendering
   │  ├─ data_saver.py                           ← Data persistence
   │  └─ mcp_client.py                           ← MCP client
   ├─ README.md                                  ← Execution guide
   ├─ pyproject.toml                             ← Dependencies
   └─ requirements.txt                           ← Pip requirements

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Next Steps:
1. Install dependencies: uv sync  (or: pip install -r requirements.txt)
2. Configure MCP tools (github-api, twitter-api, devto-api)
3. Run campaign: python -m src.campaigns.001_q1_github_stars
4. Monitor data: data/001-q1/
5. After execution, run: /marketspec.review
```

---

## Benefits of Code Execution with MCP

Based on [Anthropic's research](https://www.anthropic.com/engineering/code-execution-with-mcp):

### 1. Progressive Disclosure (98% Token Savings)

**Without code execution**:
```
Load all 1000 tool definitions upfront
→ 150,000 tokens consumed before any work
```

**With code execution**:
```python
from .mcp_tools import github  # Only loads github tools
→ 2,000 tokens (98.7% savings)
```

### 2. Context-Efficient Tool Results

**Without code execution**:
```
Fetch 10,000-row spreadsheet
→ All rows pass through LLM context
→ 500,000 tokens
```

**With code execution**:
```python
all_rows = await sheets.get_sheet(id='abc')
filtered = [row for row in all_rows if row['status'] == 'pending']
print(filtered[:5])  # Only 5 rows logged
→ 1,000 tokens (99.8% savings)
```

### 3. Control Flow in Code

**Without code execution**:
```
LLM makes 10 sequential tool calls with sleep between each
→ High latency, many roundtrips
```

**With code execution**:
```python
while not found:
    messages = await slack.get_messages()
    found = any('deployed' in m.text for m in messages)
    if not found:
        await asyncio.sleep(5)
→ Single code execution, efficient polling
```

### 4. Privacy-Preserving Operations

**With code execution**:
```python
users = await db.get_users()  # PII stays in execution environment
for user in users:
    await crm.update_contact(email=user.email)  # Flows directly, not through LLM
print(f"Updated {len(users)} contacts")  # Only count logged
```

Sensitive data never enters LLM context.

---

## Output Summary

### Primary Outputs

**Executable Code**:
- `src/campaigns/{sequence}_{name}.py` - Main campaign script
- `src/shared/mcp_tools/*.py` - MCP tool wrappers
- `src/shared/config_loader.py` - Config loading
- `src/shared/template_renderer.py` - Template rendering
- `src/shared/data_saver.py` - Data persistence

**Configurations**:
- `config/{sequence}-{name}.yaml` - Campaign config
- `templates/{sequence}-{name}/*.md` - Content templates
- `data/{sequence}-{name}/` - Data directory (empty)

**Supporting Files**:
- `src/README.md` - Execution documentation
- `pyproject.toml` - Dependencies
- `requirements.txt` - Pip requirements

---

## Execution

**To run the generated code**:

```bash
# Install dependencies
uv sync  # or: pip install -r requirements.txt

# Run campaign (Python)
python -m src.campaigns.001_q1_github_stars

# Or with uv
uv run python -m src.campaigns.001_q1_github_stars
```

**Prerequisites**:
- Python 3.11+ installed
- MCP tools configured (github-api, twitter-api, etc.)
- Environment variables set (API keys, tokens)

**During execution**:
- Content published to channels
- Metrics tracked automatically
- Data saved to `data/{sequence}-{name}/`

**After execution**:
- Run `/marketspec.review` to analyze results
- Run `/marketspec.optimize` to get recommendations

---

## Key Differences from Previous Version

| Aspect | Previous (v0.3) | Current (v0.4) |
|--------|-----------------|----------------|
| **Output** | YAML configs only | Code + Configs |
| **Execution** | External tools read YAML | Run Python code directly |
| **MCP Integration** | Not specified | Built-in MCP tool wrappers |
| **Token Efficiency** | N/A | 98% savings (progressive disclosure) |
| **Alignment** | Custom pattern | MetaSpec + Anthropic pattern |

---

## See Also

- `/marketspec.specify` - Define campaign requirements
- `/marketspec.plan` - Plan marketing strategy
- `/marketspec.tasks` - Break down implementation tasks
- `/marketspec.review` - Analyze campaign results
- **Anthropic Blog**: [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)
- **MetaSpec**: `/metaspec.sdd.implement`

---

**Version**: 0.4.0  
**Last Updated**: 2025-11-20  
**Architecture**: Distributed directories (specs/ + config/ + templates/ + data/ + src/)
