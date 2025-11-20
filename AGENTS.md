# marketing-spec-kit - AI Agent Guide

> **For AI Assistants**: This document provides complete guidance on using marketing-spec-kit's distributed directory structure and 10 SDM commands.

---

## 🎯 Your Role

You are helping a marketing team use **marketing-spec-kit** - a specification-driven toolkit for marketing operations.

**Toolkit Version**: 0.4.0  
**Architecture**: Distributed directories (specs/ + config/ + templates/ + data/ + src/) ⭐  
**Commands**: 10 SDM commands (8 Core + 2 Extension)  
**Lifecycle**: Development (0.x phase)  
**Inspired by**: [Anthropic's Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)

---

## 🏗️ Distributed Directory Structure

marketing-spec-kit uses clear separation of concerns:

### `specs/` - Strategy Specifications (Markdown)

**Purpose**: Define WHAT to achieve  
**Format**: Markdown (`.md`)  
**Audience**: Marketing teams, stakeholders, AI agents

**Documents**:
- `spec.md` - Requirements and objectives
- `clarifications.md` - Resolved ambiguities
- `plan.md` - Marketing strategy architecture
- `checklist.md` - Quality standards
- `tasks.md` - Task breakdown
- `analysis.md` - Consistency check
- `review.md` - Performance report (post-campaign)
- `optimize.md` - Optimization recommendations

### `config/` - Campaign Configurations (YAML)

**Purpose**: Configurable campaign parameters  
**Format**: YAML (`.yaml`)  
**Audience**: Code execution, human adjustments

**Files**:
- `{seq}-{name}.yaml` - Campaign configuration (adjustable parameters)

### `templates/` - Content Templates (Markdown/Text)

**Purpose**: Reusable content templates  
**Format**: Markdown (`.md`), Text  
**Audience**: Content creation, code rendering

**Directories**:
- `{seq}-{name}/` - Campaign-specific templates

### `data/` - Collected Metrics (JSON)

**Purpose**: Runtime collected metrics  
**Format**: JSON (`.json`)  
**Audience**: Analysis, review

**Directories**:
- `{seq}-{name}/` - Campaign data (runtime)

### `src/` - Executable Code (TypeScript) ⭐

**Purpose**: Define HOW to execute (code calling MCP tools)  
**Format**: TypeScript (`.ts`)  
**Audience**: Node.js runtime, developers

**Directories**:
- `campaigns/*.ts` - Campaign execution scripts
- `shared/mcp-tools/*.ts` - MCP tool wrappers
- `shared/utils.ts` - Helper functions

**Key Principle**: Like MetaSpec's `specs/` → `src/`, marketing-spec-kit uses `specs/` → `src/` + `config/` + `templates/` + `data/`.

---

## 📋 10 SDM Commands

### Core Commands (8) - Aligned with MetaSpec

| Command | Purpose | Output | Layer |
|---------|---------|--------|-------|
| `/marketspec.constitution` | Define marketing principles | `memory/constitution.md` | Setup |
| `/marketspec.specify` | Define requirements | `specs/{seq}-{name}/spec.md` | specs/ |
| `/marketspec.clarify` | Clarify objectives | `specs/{seq}-{name}/clarifications.md` | specs/ |
| `/marketspec.plan` | Plan strategy | `specs/{seq}-{name}/plan.md` | specs/ |
| `/marketspec.checklist` | Generate quality standards | `specs/{seq}-{name}/checklist.md` | specs/ |
| `/marketspec.tasks` | Break down tasks | `specs/{seq}-{name}/tasks.md` | specs/ |
| `/marketspec.analyze` | Check consistency | `specs/{seq}-{name}/analysis.md` | specs/ |
| `/marketspec.implement` | **Generate code + configs** ⭐ | `src/campaigns/{seq}-{name}.ts` + `config/` + `templates/` | src/ + config/ + templates/ |

### Extension Commands (2) - Marketing-Specific

| Command | Purpose | Output | Layer |
|---------|---------|--------|-------|
| `/marketspec.review` | Analyze campaign results | `specs/{seq}-{name}/review.md` | specs/ |
| `/marketspec.optimize` | Generate recommendations | `specs/{seq}-{name}/optimize.md` | specs/ |

---

## 📝 Complete Workflow

### Phase 1: Define WHAT (Commands 1-7 → `specs/`)

```
User: "Create a Q1 campaign to grow GitHub stars"

AI Agent:
1. /marketspec.specify
   → Creates specs/001-q1-github-stars/spec.md
   → Defines: objectives, KPIs (target: 500 stars), budget, timeline

2. /marketspec.clarify
   → Creates specs/001-q1-github-stars/clarifications.md
   → Resolves: Which GitHub repos? What content types?

3. /marketspec.plan
   → Creates specs/001-q1-github-stars/plan.md
   → Defines: Channels (Twitter, Dev.to, Reddit), content themes, budget allocation

4. /marketspec.checklist
   → Creates specs/001-q1-github-stars/checklist.md
   → Defines quality standards (e.g., "All channels have budget allocated")

5. /marketspec.tasks
   → Creates specs/001-q1-github-stars/tasks.md
   → Lists: T001 Configure tracking, T002 Create templates, T003 Set schedule

6. /marketspec.analyze
   → Creates specs/001-q1-github-stars/analysis.md
   → Validates: All tasks cover spec requirements, no contradictions
```

### Phase 2: Build HOW + DATA (Command 8) ⭐

```
7. /marketspec.implement
   → Executes all tasks from tasks.md
   → Generates executable code AND configurations:
   
   src/
   ├── campaigns/
   │   └── 001-q1-github-stars.ts        ← Executable script ⭐
   └── shared/
       ├── mcp-tools/
       │   ├── github.ts                 ← GitHub MCP wrapper
       │   ├── twitter.ts
       │   └── devto.ts
       ├── utils.ts
       └── mcp-client.ts
   
   config/
   └── 001-q1-github-stars.yaml          ← Campaign config
   
   templates/
   └── 001-q1-github-stars/
       ├── tweet-template.md
       └── blog-post-template.md
```

**Example `src/campaigns/001-q1-github-stars.ts`**:
```typescript
import * as github from '../shared/mcp-tools/github';
import * as twitter from '../shared/mcp-tools/twitter';
import { loadConfig, saveData } from '../shared/utils';

async function execute001Q1Campaign() {
  const config = await loadConfig('config/001-q1-github-stars.yaml');
  
  // Publish tweets
  await twitter.scheduleTweet({ 
    text: '🚀 Check out marketing-spec-kit!',
    time: '09:00'
  });
  
  // Track GitHub stars
  const stars = await github.getStarCount({ 
    repo: config.kpis.github_stars.repo 
  });
  
  // Save data
  await saveData('data/001-q1/github-stars.json', {
    timestamp: new Date().toISOString(),
    value: stars
  });
  
  console.log(`✅ Campaign executed. Stars: ${stars}`);
}

execute001Q1Campaign();
```

**Example `config/001-q1-github-stars.yaml`**:
```yaml
campaign:
  id: "001-q1-github-stars"
  name: "Q1 GitHub Stars Growth"
  spec_ref: "specs/001-q1-github-stars/spec.md"
  
  kpis:
    - name: "GitHub Stars"
      target: 500
      baseline: 100
      tool: "github-api"
  
  channels:
    - name: "twitter"
      frequency: "3 posts/day"
      budget: 1000
      content_template: "templates/001-q1-github-stars/tweet-template.md"
    
    - name: "dev_to"
      frequency: "2 posts/week"
      budget: 500
  
  # Note: Tracking and scheduling logic embedded in src/campaigns/001-q1-github-stars.ts
```

### Phase 3: Execute Campaign (Run Generated Code)

**Execute the generated TypeScript code**:

```bash
# Install dependencies (first time only)
npm install

# Run the campaign
ts-node src/campaigns/001-q1-github-stars.ts
```

**During execution**:
- Code loads config from `config/001-q1-github-stars.yaml`
- Renders templates from `templates/001-q1-github-stars/`
- Calls MCP tools (twitter-api, github-api, etc.)
- Collects data → `data/001-q1-github-stars/`

### Phase 4: Review & Optimize (Commands 9-10 → `specs/`)

```
8. /marketspec.review
   → Reads:
     - specs/001-q1-github-stars/spec.md (expected targets)
     - config/001-q1-github-stars.yaml (configuration)
     - data/001-q1-github-stars/* (actual data)
   → Generates: specs/001-q1-github-stars/review.md
   → Contains: KPI achievement (e.g., 450/500 stars = 90%), budget variance, lessons learned

9. /marketspec.optimize
   → Reads: specs/001-q1-github-stars/review.md
   → Generates: specs/001-q1-github-stars/optimize.md
   → Contains: Recommendations (e.g., "Increase Dev.to posting frequency", "Adjust Reddit timing")
   → Feeds into next campaign's /marketspec.specify
```

---

## 🚀 Quick Start for AI Agents

### Step 1: Help User Initialize Project

```
Human: "I want to create a new marketing project"

AI: "I'll help you initialize a project with marketing-spec-kit:

[Run command]
marketing_spec_kit init my-marketing-project

This creates:
✅ memory/constitution.md - Marketing principles
✅ specs/README.md - Workflow guidance
✅ .marketingspeckit/commands/ - 10 SDM commands for me to use

Now, what marketing campaign do you want to create?"
```

### Step 2: Guide Campaign Creation

```
Human: "Create a Q1 campaign to grow our GitHub stars"

AI: "I'll create a complete campaign specification using the SDM workflow.

Starting with /marketspec.specify...
[Creates specs/001-q1-github-stars/spec.md]

This defines:
- Objective: Grow GitHub stars from 100 to 500
- Budget: $5000
- Timeline: Q1 2025 (Jan 1 - Mar 31)
- Target Audience: Developers, DevOps engineers

Should I continue with /marketspec.clarify to resolve any ambiguities?"
```

### Step 3: Generate Operations

```
Human: "Yes, please continue and generate the operational files"

AI: "I'll complete the workflow:

[Runs /marketspec.clarify, /marketspec.plan, /marketspec.tasks]
[Runs /marketspec.implement]

✅ Generated code + configs:
- src/campaigns/001-q1-github-stars.ts (executable code)
- src/shared/mcp-tools/*.ts (MCP wrappers)
- config/001-q1-github-stars.yaml (configuration)
- templates/001-q1-github-stars/ (content templates)

Your marketing team can now run the campaign:
$ ts-node src/campaigns/001-q1-github-stars.ts
Data will be collected in data/001-q1-github-stars/"
```

---

## 🔒 Key Constraints

### ALWAYS Follow These Rules

1. **Separation of Concerns**:
   - `specs/` = WHAT (strategy, plans, reports)
   - `config/` = Campaign configurations (YAML)
   - `templates/` = Content templates
   - `data/` = Collected metrics
   - `src/` = HOW (executable code)

2. **Command Output**:
   - Commands 1-7, 9-10 → Generate `.md` files in `specs/`
   - Command 8 (`implement`) → Generates code in `src/` + configs in `config/` + templates in `templates/`

3. **File Naming**:
   - Specs: `specs/{sequence}-{name}/{document}.md`
   - Config: `config/{sequence}-{name}.yaml`
   - Templates: `templates/{sequence}-{name}/`
   - Code: `src/campaigns/{sequence}-{name}.ts`

4. **Workflow Order**:
   - Specification phase (1-7) BEFORE implementation (8)
   - Review/optimize (9-10) AFTER campaign execution

### NEVER Do These

❌ Generate code/configs from specification commands (1-7, 9-10)  
❌ Generate Markdown files from `/marketspec.implement`  
❌ Skip `/marketspec.specify`, `/marketspec.plan`, or `/marketspec.tasks` (required)  
❌ Run `/marketspec.review` before campaign execution  

---

## 🛠️ For Speckit Developers

If you want to **develop or maintain** marketing-spec-kit itself (not just use it), see:

- **`.metaspec/README.md`** - Complete development guide
- **`.metaspec/commands/`** - 19 MetaSpec SDS/SDD commands
- **`docs/sdm-commands.md`** - SDM commands documentation

This includes specifications for defining specifications (SDS), developing toolkit features (SDD), and managing changes (Evolution).

---

## 📚 Examples

See complete examples:
- **`examples/q1-github-stars-campaign/`** - Full working campaign example
- **`examples/sdm-workflow-example.md`** - Step-by-step walkthrough
- **`templates/sdm/commands/`** - Command definitions

---

**Generated by**: MetaSpec 0.9.5  
**Date**: 2025-11-20  
**Domain**: marketing  
**Architecture**: Distributed directories (specs/ + config/ + templates/ + data/ + src/)

