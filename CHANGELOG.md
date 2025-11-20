# Changelog

All notable changes to marketing-spec-kit will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.0] - 2025-11-20

### 🚀 Major Update: Distributed Architecture + Code Generation

#### 🏗️ Architecture Redesign

**From**: Three-layer architecture (`specs/` + `operations/` + `src/`)  
**To**: Distributed directory structure (5 directories with clear purposes)

```
specs/      ← Strategy specifications (Markdown)
config/     ← Campaign configurations (YAML)
templates/  ← Content templates (Markdown/Text)
data/       ← Collected metrics (JSON)
src/        ← Executable code (TypeScript)
```

**Rationale**:
- ✅ **Semantic Clarity**: "operations" was ambiguous in marketing context
- ✅ **Industry Standards**: `config/`, `templates/`, `data/` are universal conventions
- ✅ **Single Responsibility**: Each directory has one clear purpose
- ✅ **12-Factor App**: Separates configuration from code
- ✅ **Discoverability**: Clear names reduce cognitive load

#### 🔥 Code Generation (Inspired by Anthropic's MCP)

**Before**: `/marketspec.implement` generated YAML configurations  
**After**: `/marketspec.implement` generates **executable TypeScript code** + configs

**What's generated**:
- `src/campaigns/{seq}-{name}.ts` - Main campaign execution script
- `src/shared/mcp-tools/*.ts` - MCP tool wrappers (GitHub, Twitter, etc.)
- `config/{seq}-{name}.yaml` - Campaign configuration (adjustable parameters)
- `templates/{seq}-{name}/` - Content templates (reusable)

**Why generate code?** (Ref: [Anthropic's Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp))
- 📉 **98% token savings**: Progressive disclosure, load tools on-demand
- ⚡ **Better performance**: Filter data in execution environment, not LLM context
- 🔄 **Control flow**: Use code loops/conditions instead of chaining tool calls
- 🔒 **Privacy**: Sensitive data stays in execution environment
- ✅ **Testable**: Standard testing frameworks (Jest, pytest)
- 📝 **Version control**: Git tracks code changes

#### Changed

- **Command #8 (`/marketspec.implement`)**: Complete rewrite
  - Before: Generated YAML in `operations/`
  - After: Generates TypeScript code in `src/` + configs in `config/` + templates in `templates/`
  - Reads: `tasks.md`, `spec.md`, `plan.md`
  - Executes: All tasks to build complete marketing campaign operations

- **Workflow update**: Minimum workflow now 4 steps (not 3)
  - Before: `specify → plan → implement`
  - After: `specify → plan → tasks → implement` (tasks is required)
  - Reason: `implement` needs to read `tasks.md` to know what to generate

- **Command outputs**:
  - Commands 1-7, 9-10: Still generate Markdown in `specs/`
  - Command 8: Now generates code + configs in multiple directories

#### Documentation

**Completely rewritten**:
- `README.md` - Distributed architecture, code generation rationale, 10+ path updates
- `AGENTS.md` - Complete AI agent workflow guide with new structure
- `templates/sdm/commands/README.md` - Updated for AI assistants
- `templates/README.md` - Updated command list and extension examples
- `marketspec.implement.md` - Complete rewrite with code generation
- `marketspec.review.md` - Updated data paths (`operations/data/` → `data/`)
- `generator.py` - Updated comments to reflect new architecture

**Added**:
- `docs/sdm-commands.md` - Architecture evolution summary
- Detailed "Why Generate Code?" section with Anthropic MCP reference
- Progressive disclosure examples and benefits

#### Files Renamed/Restructured

**Directory changes**:
- `operations/configs/` → `config/`
- `operations/templates/` → `templates/`
- `operations/data/` → `data/`
- Added: `src/` (new directory for executable code)

**Naming convention**:
- Config: `config/{seq}-{name}.yaml`
- Templates: `templates/{seq}-{name}/`
- Data: `data/{seq}-{name}/`
- Code: `src/campaigns/{seq}-{name}.ts`

#### Technical Details

**Generator changes**:
- Does NOT pre-create `config/`, `templates/`, `data/`, `src/`
- These directories created by `/marketspec.implement` (like MetaSpec's `src/`)
- Only creates infrastructure: `memory/`, `specs/`, `README.md`, `.gitignore`

**Alignment with MetaSpec**:
- MetaSpec: `specs/` → `src/`
- marketing-spec-kit: `specs/` → `src/` + `config/` + `templates/` + `data/`

### 🐛 Bug Fixes

- Fixed minimum workflow documentation (3 steps → 4 steps, tasks is required)
- Fixed all `operations/` references in documentation (140+ updates across 7 files)

### 📚 References

- Anthropic: [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)
- MetaSpec: Specification-Driven Development pattern
- 12-Factor App: Configuration management principles

---

## [0.3.1] - 2025-11-19

### 🚀 Major Update: MetaSpec v0.9.5 Alignment

#### Changed
- **MetaSpec sync**: Updated to MetaSpec v0.9.5 (Generator vs AI Commands pattern)
- **init command**: Now creates complete project structure (not single file)
  - Before: `marketing_spec_kit init my-spec.yaml` (single file)
  - After: `marketing_spec_kit init my-project` (full structure)
- **AI-first workflow**: Specifications generated by AI dialogue, not manual templates
- **Project structure**: Follows MetaSpec v0.9.5 standards
  - `.marketingspeckit/commands/` - 10 slash commands for AI
  - `memory/constitution.md` - Marketing principles
  - `specs/README.md` - Workflow guidance (NOT spec templates)
  - No `spec-template.yaml` or `example-spec.yaml`

#### Added
- `specs-readme.md.j2` template (8.2KB) - Comprehensive AI workflow guidance
- Complete slash commands deployment to user projects
- MetaSpec v0.9.5 compliance verification

#### Removed
- `spec-template.yaml.j2` - Anti-pattern per MetaSpec v0.9.5
- `example-campaign.yaml.j2` - Anti-pattern per MetaSpec v0.9.5

#### Documentation
- Updated README.md quick start guide
- Updated AGENTS.md to reflect AI-driven workflow
- Archived 6 resolved MetaSpec feedback documents

### Changed
- **Command classification refactor**: Aligned with MetaSpec SDD patterns
  - Core Flow (5 commands): constitution, discover, strategy, tasks, create
  - Quality Gates (3 commands): clarify, checklist, analyze
  - Extension (2 commands): review, optimize
  - Promoted `constitution` and `tasks` from Optional to Core Flow
  - Updated all documentation to reflect new classification

## [0.3.0] - 2025-11-16

### 🚨 Breaking Changes
- **Command system refactor**: Entity operations → Workflow commands
- **Command prefix change**: `/marketing.*` → `/marketspec.*`
- **22 entity commands deprecated** (archived to `.archive/`)
- **SDS/SDD separation**: Domain spec no longer defines operations

### ✨ Features

#### 🔄 Complete SDM Command System (10 Commands)
Implemented full Spec-Driven Marketing command system with closed-loop optimization:

**Core Commands (8) - Planning Phase**:
1. `/marketspec.constitution` - Define marketing principles (363 lines)
2. `/marketspec.discover` - Discover marketing needs (464 lines)
3. `/marketspec.clarify` - Clarify objectives (478 lines)
4. `/marketspec.strategy` - Plan marketing strategy (721 lines)
5. `/marketspec.checklist` - Quality validation (839 lines)
6. `/marketspec.tasks` - Break down tasks (639 lines)
7. `/marketspec.analyze` - Consistency checking (500 lines)
8. `/marketspec.create` - Generate marketing-spec.yaml (987 lines)

**Extension Commands (2) - Post-Execution Phase**:
9. `/marketspec.review` - Analyze actual campaign performance (~700 lines)
10. `/marketspec.optimize` - Generate optimization recommendations (~800 lines)

**Key Features**:
- 📋 ~7,500 lines of comprehensive documentation
- 🔄 Complete marketing cycle: Plan → Execute → Review → Optimize → Next Plan
- 🎯 Flexible workflows: Minimal (2 steps), Recommended (5 steps), Complete (10 steps)
- 📊 Data-driven optimization based on actual campaign results
- ✅ 13-part standardized structure for all commands
- 🔗 Clear input/output chains and dependencies
- 🎨 Marketing-friendly naming (discover, strategy, create)

**Command Categories** (aligned with MetaSpec SDD):
- 🔴 Core Flow (5): constitution, discover, strategy, tasks, create
- 🟡 Quality Gates (3): clarify, checklist, analyze
- 🔵 Extension (2): review, optimize

**Differentiation**:
- Based on MetaSpec SDD pattern with marketing domain adaptation
- Unique closed-loop system (review + optimize) not found in MetaSpec
- Continuous improvement through data-driven optimization

### 📚 Documentation

- Added `templates/sdm/README.md` - SDM layer overview and workflow guide
- Added `examples/sdm-workflow-example.md` - Complete Q1 to Q2 workflow example
- Added `.archive/README.md` - Explaining why old commands were archived
- Updated `AGENTS.md` with SDM command system guidance
- Updated `README.md` with SDM workflow introduction

### 🔧 Infrastructure

- **MetaSpec sync**: Updated to v0.7.3 with SDS/SDD separation guidance
- **Domain spec cleaned**: Removed Operations definition (SDS = structure only)
- **Toolkit spec updated**: Declared Type B (Workflow-Guidance)
- **Archive management**: Old commands moved to `.archive/` (local-only)
- **pyproject.toml**: Fixed dependencies placement

## [0.2.0] - 2025-11-15

### Note on Versioning
This project is in **0.x development phase**. Breaking changes can occur between 0.x releases. 
Version 1.0.0 will be released when the API is stable and production-ready.

### 🚨 Breaking Changes

- **Campaign.plan_id is now REQUIRED**: All campaigns must be linked to a MarketingPlan
- **Spec validation now requires 45 rules** (was 42)
- **New entities added**: MarketingPlan, Analytics

### ✨ Major Features

#### 🎯 5-Phase Marketing Workflow System
Complete workflow redesign from "toolbox" to "workflow system":
```
Strategic Planning → Campaign Design → Content Creation → Execution → Analytics
```

#### 📋 New Entity: MarketingPlan (14 fields)
- **Purpose**: Strategic marketing planning with objectives, budget allocation, and KPIs
- **Fields**: id, name, project_id, period, objectives, target_audience, strategies, budget, kpis, campaign_ids, status, created_at, updated_at, approval
- **Validation Rules**: PLAN-01 to PLAN-05 (5 rules)
- **Key Features**:
  - Budget allocation with automatic sum validation
  - 1-5 objectives, 1-8 strategies
  - Multi-segment target audience with priorities
  - 1-10 KPIs with P0/P1/P2 prioritization
  - Approval workflow for APPROVED/ACTIVE status

#### 📊 New Entity: Analytics (9 fields)
- **Purpose**: AI-powered performance analytics and optimization recommendations
- **Fields**: id, type, entity_id, period, metrics, vs_target, insights, optimizations, generated_at
- **Validation Rules**: ANLY-01 (1 rule)
- **Key Features**:
  - Campaign-level and Plan-level analytics
  - Target vs actual KPI comparisons
  - AI-generated insights (success/concern/opportunity)
  - Prioritized optimization recommendations (high/medium/low)

#### 🔄 Updated Entity: Campaign
- **New Required Field**: `plan_id` (links to MarketingPlan)
- **New Optional Fields**: 
  - `expected_kpis`: Projected performance for design phase
  - `content_calendar`: List of scheduled content entries
- **New Validation Rules**: CAMP-08 to CAMP-11 (4 rules)
  - CAMP-08: plan_id must reference existing plan
  - CAMP-09: start_date within plan period
  - CAMP-10: end_date within plan period and >= start_date
  - CAMP-11: Budget check (warning if campaigns exceed plan budget)

### 🤖 New AI Agent Slash Commands (+9, total 22)

#### Strategic Planning Commands (4)
1. **`/marketing.plan.create`** (217 lines)
   - Create marketing plan with AI assistance
   - Interactive gathering of objectives, audience, strategies, budget, KPIs
   - Validates against PLAN-01~05

2. **`/marketing.plan.validate`** (67 lines)
   - Validate plan against 5 rules
   - Clear pass/fail reporting with actionable fixes

3. **`/marketing.plan.get`** (71 lines)
   - Display formatted plan details
   - Markdown output with tables and structured sections

4. **`/marketing.plan.analyze`** (149 lines)
   - Multi-dimensional AI analysis
   - Scores: Strategic Alignment, Resource Feasibility, KPI Quality, Execution Readiness
   - Prioritized recommendations (P0/P1/P2)
   - Risk assessment

#### Campaign Design Command (1)
5. **`/marketing.campaign.design`** (198 lines)
   - AI-assisted campaign design based on plan
   - Suggests timeline, budget, channels, content calendar
   - Validates against CAMP-08~11 constraints
   - Provides design rationale

#### Content Planning Command (1)
6. **`/marketing.content.plan`** (187 lines)
   - Generate content calendar for campaign
   - Cadence based on goal (awareness/consideration/conversion)
   - Even distribution across timeline
   - Content strategy summary

#### Analytics & Optimization Commands (3)
7. **`/marketing.analytics.campaign`** (318 lines)
   - Campaign performance report
   - KPI target vs actual comparisons with status
   - AI insights (3-10 per report)
   - Optimization recommendations with effort/impact estimates

8. **`/marketing.analytics.plan`** (402 lines)
   - Plan-level aggregate analytics
   - Cross-campaign performance comparison
   - Objective achievement analysis
   - Q+1 plan recommendations based on learnings

9. **`/marketing.optimize.suggest`** (380 lines)
   - Multi-dimensional optimization analysis
   - Effort vs Impact priority matrix
   - Quick Wins + Strategic Improvements
   - Implementation steps for each suggestion

### 🏗️ Models & Architecture

#### New Enums (8)
- `PlanStatus`: draft, approved, active, completed, archived
- `AnalyticsType`: campaign, plan
- `InsightType`: success, concern, opportunity
- `OptimizationPriority`: high, medium, low
- `OptimizationEffort`: low, medium, high
- `KPIPriority`: P0 (critical), P1 (important), P2 (nice-to-have)
- `AudiencePriority`: high, medium, low
- `ContentStatus`: planned, created, published

#### New Nested Models (11)
- `PlanPeriod`: Time period with start/end dates and duration_weeks
- `PlanBudget`: Total, currency, and allocation breakdown
- `TargetAudience`: Segment definition with size estimate and priority
- `Strategy`: Marketing strategy with rationale and success criteria
- `PlanKPI`: KPI definition with target, unit, measurement, priority
- `PlanApproval`: Approval metadata (required for APPROVED/ACTIVE plans)
- `ContentCalendarEntry`: Single content entry with date, type, channel, status
- `AnalyticsPeriod`: Time range for analytics reports
- `KPIComparison`: Target vs actual comparison with achievement percentage
- `AnalyticsInsight`: AI insight with type, description, evidence, recommendation
- `Optimization`: Optimization recommendation with priority, action, impact, effort

### ✅ Validation Enhancements

- **Total Rules**: 42 → 45 (+3 net, +10 new rules, -7 renumbered)
- **New Rule Families**:
  - PLAN-01 to PLAN-05: MarketingPlan validation (5 rules)
  - CAMP-08 to CAMP-11: Campaign-Plan relationship validation (4 rules)
  - ANLY-01: Analytics entity reference validation (1 rule)
- **Performance**: <250ms for typical specs (was <200ms)

### 📖 Documentation

#### Major Updates
- **README.md**: Complete rewrite for v2.0.0
  - 5-phase workflow documentation
  - 22 command reference
  - v1.0 vs v2.0 comparison table
  - Breaking changes section

- **Domain Spec**: `specs/domain/001-marketing-operations-spec/spec.md` (v2.0.0)
  - 1,917 → 3,143 lines (+64%)
  - New: Workflow Specification section (310 lines)
  - New: MarketingPlan entity (360 lines)
  - New: Analytics entity (240 lines)
  - Updated: Campaign entity with 3 new fields

- **Constitution**: `memory/constitution.md` (v1.3.0)
  - Part II: Added "Workflow Completeness" principle
  - Part III: Unchanged (toolkit implementation principles)

#### Evolution Proposal
- **Complete Change Documentation**: `changes/2025-11-15-add-workflow-system/`
  - `proposal.md`: 661 lines - Full change rationale and design
  - `tasks.md`: 436 lines - 55 implementation tasks across 9 phases
  - `impact.md`: 632 lines - Breaking changes, migration guide, version bump
  - `specs/spec-delta.md`: 839 lines - Detailed spec changes

#### Examples
- **`examples/metaspec-marketing.yaml`** (395 lines)
  - Complete v2.0.0 specification example
  - Includes Plan, Campaigns, Analytics
  
- **`examples/metaspec-marketing-plan.md`** (292 lines)
  - Detailed strategic plan documentation
  - Demonstrates Plan-to-Campaign relationship

#### Design Documents
- **`specs/domain/.../workflow-redesign.md`** (1,060 lines)
  - 5-phase workflow design
  - New entities and commands
  - Validation rules expansion

### 🔧 Technical Improvements

- **Parser**: Automatic support for `plans` and `analytics` fields (no code changes, Pydantic handles)
- **Validator**: 
  - Extended to support Plan and Analytics entities
  - Added cross-entity validation (campaign dates within plan period)
  - Budget sum validation with tolerance (±$0.01)
- **Type Safety**: All new entities fully typed with Pydantic v2
- **Error Handling**: Clear error messages for new validation rules

### 📦 Package Changes

- **Version**: 0.1.0 → 2.0.0
- **Exports**: Added 8 enums, 11 nested models, 2 entities to `__init__.py`
- **Backward Compatibility**: ❌ **BREAKING** - `Campaign.plan_id` now required

### 📊 Code Statistics

| Metric | v1.0.0 | v2.0.0 | Change |
|--------|---------|---------|--------|
| Entities | 7 | 9 | +2 |
| Enums | 3 | 11 | +8 |
| Nested Models | 0 | 11 | +11 |
| Validation Rules | 42 | 45 | +3 |
| Slash Commands | 13 | 22 | +9 |
| Python Code Lines | 1,836 | 2,379 | +543 |
| Template Lines | 1,593 | 3,394 | +1,801 |
| Total Lines | 3,429 | 5,773 | +2,344 (+68%) |

### 🐛 Bug Fixes

- None (clean v1.0.0 to v2.0.0 upgrade)

### ⚠️ Deprecations

- None (v1.0.0 specs require migration due to breaking change)

---

## [0.1.0] - 2025-11-15

### Added

#### Core Components (Phase 1)
- **7 Entity Models**: Project, Product, Campaign, Channel, Tool, ContentTemplate, Milestone
- **3 Enums**: BrandVoice, CampaignGoal, ChannelType
- **Parser**: YAML/JSON support with automatic format detection
- **Performance**: Parse <100ms for typical specs

#### Validation (Phase 2)
- **42 Validation Rules**: VR-P01 to VR-M05 across all 7 entities
- **Three-layer Architecture**: Structural, business logic, reference integrity
- **Rich Error Messages**: Error codes, entity context, actionable fix suggestions
- **Validation Result**: Success rate, errors, warnings, info levels

#### CLI Commands (Phase 3)
- **init command**: Create specs from 3 templates (minimal, default, full)
- **validate command**: Parse + validate with rich table output
- **info command**: Toolkit metadata and command list
- **Rich UI**: Color-coded output, tables for errors/warnings
- **Options**: --strict, --verbose, --force, --template

#### AI Agent Slash Commands (Phase 4)
- **13 Slash Commands** (1255 lines):
  * 7 Specification Access commands (P0): project, product, campaign, channel, tool, content_template, milestone
  * 4 Content Generation commands (1 P0, 3 P1): generate.post, generate.article, generate.email, generate.landing_page
  * 2 Task Execution commands (P1): execute.schedule, execute.publish

#### Templates
- **3 Spec Templates**: minimal (21 lines), default (101 lines), full (216 lines)
- **13 Command Templates**: Self-documenting Markdown with examples
- **Complete Documentation**: Inputs, outputs, validation rules, execution steps

### Implementation Quality
- **Total Code**: 1,836 lines of Python
- **Total Templates**: 1,593 lines (spec templates + command templates)
- **Test Coverage**: Ready for unit/integration tests
- **Performance Targets**: Parse <100ms, Validate <200ms
- **Dependencies**: Pydantic 2.0+, Typer, Rich, PyYAML, JSONSchema

### Documentation
- README with quick start guide
- AGENTS.md for AI assistant integration
- Domain specification (001-marketing-operations-spec)
- Toolkit specification (001-marketing-spec-kit-implementation)
- Constitution with implementation principles
- Complete analysis report (98/100 score)

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 2.0.0 | 2025-11-15 | Workflow system with Plan & Analytics entities (BREAKING) |
| 0.1.0 | 2025-11-15 | Full MVP release with 4 phases complete |

---

**Note**: This changelog is maintained manually.

For detailed commit history, see: [Git Log](../../commits/main)

