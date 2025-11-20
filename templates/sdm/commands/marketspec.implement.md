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
- `src/campaigns/{sequence}-{name}.ts` - Executable campaign code ⭐
- `config/{sequence}-{name}.yaml` - Campaign configuration
- `templates/{sequence}-{name}/` - Content templates  
**Adapted from**: `metaspec.sdd.implement`

---

## Purpose

This is the **implementation command** that generates:
1. **Executable code** (`src/`) - TypeScript scripts that call MCP tools
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

src/                                ← HOW (执行代码 - TypeScript)
├── campaigns/
│   └── 001-q1-campaign.ts          ← Main execution script ⭐
└── shared/
    ├── mcp-tools/
    │   ├── github.ts               ← GitHub MCP tool wrapper
    │   ├── twitter.ts
    │   └── analytics.ts
    ├── config-loader.ts
    └── template-renderer.ts
```

---

## Command Usage

```
/marketspec.implement
/marketspec.implement --dry-run
/marketspec.implement --language [typescript|python]
```

**Examples**:
```
/marketspec.implement                        # Generate TypeScript (default)
/marketspec.implement --language python      # Generate Python
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

**Output**: `src/campaigns/{sequence}-{name}.ts`

**Purpose**: Executable script that orchestrates campaign execution using MCP tools

**Example**:
```typescript
// src/campaigns/001-q1-github-stars.ts
import * as github from '../shared/mcp-tools/github';
import * as twitter from '../shared/mcp-tools/twitter';
import * as devto from '../shared/mcp-tools/devto';
import { loadConfig, saveData, renderTemplate } from '../shared/utils';

/**
 * Q1 GitHub Stars Growth Campaign
 * 
 * Spec: specs/001-q1-github-stars/spec.md
 * Config: config/001-q1-github-stars.yaml
 * 
 * Objectives:
 * - Grow GitHub stars from 100 to 500
 * - Increase website traffic from 1000 to 5000 sessions
 * 
 * Channels: Twitter (3/day), Dev.to (2/week)
 * Budget: $5000
 * Timeline: Q1 2025 (Jan 1 - Mar 31)
 */

async function execute001Q1Campaign() {
  console.log('🚀 Starting Q1 GitHub Stars Growth Campaign\n');
  
  // Step 1: Load configuration
  const config = await loadConfig('config/001-q1-github-stars.yaml');
  console.log(`Campaign: ${config.campaign.name}`);
  console.log(`Target: ${config.kpis.github_stars.target} stars\n`);
  
  // Step 2: Publish Twitter content
  console.log('📱 Publishing Twitter content...');
  const twitterTemplate = await renderTemplate(
    config.channels.twitter.template,
    { theme: 'Getting Started', hashtags: '#OpenSource #DevTools' }
  );
  
  for (const time of config.channels.twitter.times) {
    await twitter.scheduleTweet({
      text: twitterTemplate,
      scheduledTime: time
    });
    console.log(`  ✅ Scheduled tweet at ${time}`);
  }
  
  // Step 3: Publish Dev.to articles
  console.log('\n📝 Publishing Dev.to articles...');
  const blogTemplate = await renderTemplate(
    config.channels.devto.template,
    { 
      title: 'Getting Started with marketing-spec-kit',
      tags: ['opensource', 'marketing', 'automation']
    }
  );
  
  await devto.publishArticle({
    title: 'Getting Started with marketing-spec-kit',
    body: blogTemplate,
    published: true
  });
  console.log('  ✅ Published article on Dev.to');
  
  // Step 4: Track KPIs
  console.log('\n📊 Tracking KPIs...');
  
  // GitHub Stars (data filtered in execution environment, not in LLM context)
  const currentStars = await github.getStarCount({
    repo: config.kpis.github_stars.repo
  });
  const starsProgress = (currentStars / config.kpis.github_stars.target) * 100;
  console.log(`  GitHub Stars: ${currentStars}/${config.kpis.github_stars.target} (${starsProgress.toFixed(1)}%)`);
  
  // Website Traffic
  const traffic = await analytics.getSessions({
    startDate: config.timeline.start,
    endDate: 'today'
  });
  const trafficProgress = (traffic / config.kpis.website_traffic.target) * 100;
  console.log(`  Website Traffic: ${traffic}/${config.kpis.website_traffic.target} (${trafficProgress.toFixed(1)}%)`);
  
  // Step 5: Save data (persists in data/, not in LLM context)
  await saveData('data/001-q1/github-stars.json', {
    timestamp: new Date().toISOString(),
    value: currentStars,
    target: config.kpis.github_stars.target,
    progress: starsProgress
  });
  
  await saveData('data/001-q1/website-traffic.json', {
    timestamp: new Date().toISOString(),
    value: traffic,
    target: config.kpis.website_traffic.target,
    progress: trafficProgress
  });
  
  console.log('\n✅ Campaign execution completed');
  console.log(`📂 Data saved to data/001-q1/`);
}

// Execute the campaign
execute001Q1Campaign().catch(console.error);
```

#### 4.2 Create MCP Tool Wrappers

**Output**: `src/shared/mcp-tools/*.ts`

**Purpose**: Wrap MCP tools for progressive disclosure (load tool definitions on-demand)

**Example - GitHub Tool**:
```typescript
// src/shared/mcp-tools/github.ts
import { callMCPTool } from '../mcp-client';

/**
 * GitHub MCP Tool Wrapper
 * 
 * Progressive disclosure: Tool definitions loaded on-demand,
 * not upfront in LLM context (reduces token usage by 98%)
 * 
 * Reference: https://www.anthropic.com/engineering/code-execution-with-mcp
 */

interface GetStarCountInput {
  repo: string;
}

interface GetStarCountResponse {
  stars: number;
  forksCount: number;
  watchersCount: number;
}

/**
 * Get star count for a GitHub repository
 * 
 * @param input - Repository in format "owner/repo"
 * @returns Star count and other metrics
 */
export async function getStarCount(input: GetStarCountInput): Promise<number> {
  const result = await callMCPTool<GetStarCountResponse>('github__get_star_count', input);
  return result.stars;
}

/**
 * Star a GitHub repository
 */
export async function starRepo(input: { repo: string }): Promise<void> {
  await callMCPTool('github__star_repo', input);
}

/**
 * Get repository contributors
 */
export async function getContributors(input: { repo: string, limit?: number }): Promise<string[]> {
  const result = await callMCPTool<{ contributors: string[] }>('github__get_contributors', input);
  return result.contributors;
}
```

**Example - Twitter Tool**:
```typescript
// src/shared/mcp-tools/twitter.ts
import { callMCPTool } from '../mcp-client';

interface ScheduleTweetInput {
  text: string;
  scheduledTime: string;
  mediaUrls?: string[];
}

/**
 * Schedule a tweet for future posting
 */
export async function scheduleTweet(input: ScheduleTweetInput): Promise<void> {
  await callMCPTool('twitter__schedule_tweet', input);
}

/**
 * Publish a tweet immediately
 */
export async function publishTweet(input: { text: string; mediaUrls?: string[] }): Promise<void> {
  await callMCPTool('twitter__publish_tweet', input);
}

/**
 * Get tweet engagement metrics
 */
export async function getTweetMetrics(input: { tweetId: string }): Promise<{
  likes: number;
  retweets: number;
  replies: number;
}> {
  return await callMCPTool('twitter__get_tweet_metrics', input);
}
```

#### 4.3 Create Utility Functions

**Output**: `src/shared/utils.ts`

**Purpose**: Helper functions for config loading, template rendering, data persistence

**Example**:
```typescript
// src/shared/utils.ts
import * as fs from 'fs/promises';
import * as yaml from 'js-yaml';

/**
 * Load YAML configuration file
 */
export async function loadConfig(path: string): Promise<any> {
  const content = await fs.readFile(path, 'utf-8');
  return yaml.load(content);
}

/**
 * Render template with variables
 */
export async function renderTemplate(templatePath: string, vars: Record<string, any>): Promise<string> {
  let template = await fs.readFile(templatePath, 'utf-8');
  
  // Simple template rendering (replace {{variable}} with values)
  for (const [key, value] of Object.entries(vars)) {
    template = template.replace(new RegExp(`{{${key}}}`, 'g'), value);
  }
  
  return template;
}

/**
 * Save data to JSON file (for later review/analysis)
 */
export async function saveData(path: string, data: any): Promise<void> {
  await fs.mkdir(path.split('/').slice(0, -1).join('/'), { recursive: true });
  await fs.writeFile(path, JSON.stringify(data, null, 2), 'utf-8');
}
```

#### 4.4 Create MCP Client

**Output**: `src/shared/mcp-client.ts`

**Purpose**: Low-level MCP tool calling interface

**Example**:
```typescript
// src/shared/mcp-client.ts
/**
 * MCP Client - Calls MCP tools via stdio transport
 * 
 * This is a simplified example. In production, use official MCP SDK:
 * - TypeScript: @modelcontextprotocol/sdk
 * - Python: mcp
 */

export async function callMCPTool<T = any>(toolName: string, input: any): Promise<T> {
  // In real implementation, this would:
  // 1. Connect to MCP server via stdio
  // 2. Send tool call request
  // 3. Receive and parse response
  // 4. Return result
  
  console.log(`[MCP] Calling tool: ${toolName}`);
  console.log(`[MCP] Input:`, JSON.stringify(input, null, 2));
  
  // Placeholder - replace with actual MCP SDK call
  throw new Error('MCP client not implemented - use @modelcontextprotocol/sdk');
}
```

---

### Step 5: Generate README and Package Files

#### 5.1 Create src/README.md

**Output**: `src/README.md`

**Content**:
```markdown
# Campaign Execution Scripts

This directory contains executable TypeScript scripts for running marketing campaigns.

## Structure

\`\`\`
src/
├── campaigns/
│   └── 001-q1-github-stars.ts    ← Main campaign scripts
└── shared/
    ├── mcp-tools/                 ← MCP tool wrappers
    ├── utils.ts                   ← Helper functions
    └── mcp-client.ts              ← MCP client interface
\`\`\`

## Running a Campaign

\`\`\`bash
# Install dependencies
npm install

# Run a campaign
ts-node src/campaigns/001-q1-github-stars.ts

# Or compile and run
npm run build
node dist/campaigns/001-q1-github-stars.js
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

#### 5.2 Create package.json

**Output**: `package.json`

**Content**:
```json
{
  "name": "marketing-campaigns",
  "version": "1.0.0",
  "description": "Executable marketing campaign scripts",
  "scripts": {
    "build": "tsc",
    "start": "node dist/campaigns/001-q1-github-stars.js",
    "dev": "ts-node src/campaigns/001-q1-github-stars.ts"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^0.5.0",
    "js-yaml": "^4.1.0"
  },
  "devDependencies": {
    "@types/js-yaml": "^4.0.5",
    "@types/node": "^20.0.0",
    "ts-node": "^10.9.0",
    "typescript": "^5.0.0"
  }
}
```

#### 5.3 Create tsconfig.json

**Output**: `tsconfig.json`

**Content**:
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "commonjs",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
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
   ├─ campaigns/001-q1-github-stars.ts           ← Main script ⭐
   ├─ shared/
   │  ├─ mcp-tools/
   │  │  ├─ github.ts                            ← GitHub wrapper
   │  │  ├─ twitter.ts                           ← Twitter wrapper
   │  │  └─ devto.ts                             ← Dev.to wrapper
   │  ├─ utils.ts                                ← Helper functions
   │  └─ mcp-client.ts                           ← MCP client
   ├─ README.md                                  ← Execution guide
   ├─ package.json                               ← Dependencies
   └─ tsconfig.json                              ← TypeScript config

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Next Steps:
1. Install dependencies: npm install
2. Configure MCP tools (github-api, twitter-api, devto-api)
3. Run campaign: ts-node src/campaigns/001-q1-github-stars.ts
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
```typescript
import * as github from './mcp-tools/github';  // Only loads github tools
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
```typescript
const allRows = await sheets.getSheet({ id: 'abc' });
const filtered = allRows.filter(row => row.status === 'pending');
console.log(filtered.slice(0, 5));  // Only 5 rows logged
→ 1,000 tokens (99.8% savings)
```

### 3. Control Flow in Code

**Without code execution**:
```
LLM makes 10 sequential tool calls with sleep between each
→ High latency, many roundtrips
```

**With code execution**:
```typescript
while (!found) {
  const messages = await slack.getMessages();
  found = messages.some(m => m.text.includes('deployed'));
  if (!found) await sleep(5000);
}
→ Single code execution, efficient polling
```

### 4. Privacy-Preserving Operations

**With code execution**:
```typescript
const users = await db.getUsers();  // PII stays in execution environment
for (const user of users) {
  await crm.updateContact({ email: user.email });  // Flows directly, not through LLM
}
console.log(`Updated ${users.length} contacts`);  // Only count logged
```

Sensitive data never enters LLM context.

---

## Output Summary

### Primary Outputs

**Executable Code**:
- `src/campaigns/{sequence}-{name}.ts` - Main campaign script
- `src/shared/mcp-tools/*.ts` - MCP tool wrappers
- `src/shared/utils.ts` - Helper functions

**Configurations**:
- `config/{sequence}-{name}.yaml` - Campaign config
- `templates/{sequence}-{name}/*.md` - Content templates
- `data/{sequence}-{name}/` - Data directory (empty)

**Supporting Files**:
- `src/README.md` - Execution documentation
- `package.json` - Dependencies
- `tsconfig.json` - TypeScript configuration

---

## Execution

**To run the generated code**:

```bash
# Install dependencies
npm install

# Run campaign (TypeScript)
ts-node src/campaigns/001-q1-github-stars.ts

# Or compile and run (JavaScript)
npm run build
node dist/campaigns/001-q1-github-stars.js
```

**Prerequisites**:
- Node.js 18+ and npm installed
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
| **Execution** | External tools read YAML | Run TypeScript code directly |
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
