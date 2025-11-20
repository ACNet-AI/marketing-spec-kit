# SDM Commands Rewrite Guide

**Date**: 2024-11-20  
**Purpose**: Align marketing-spec-kit SDM commands with MetaSpec SDS/SDD pattern  
**Status**: ✅ COMPLETED (10/10 commands + distributed architecture)

---

## Core Principle (Updated)

**Specification-Driven Development with Quality Assurance**

```
✅ Specification Commands (specs/): Define WHAT
   - specify, clarify, plan

✅ Quality Assurance (specs/): Optional but recommended
   - checklist: Generate quality standards (optional reference)
   - tasks: Create implementation plan
   - analyze: Cross-artifact consistency & coverage validation

✅ Implementation Command (src/ + config/ + templates/): Generate code
   - implement (generates executable code + configs)

✅ Post-Campaign Commands (specs/): Analyze results
   - review, optimize (generate Markdown analysis)
```

**Key Innovation from spec-kit**: 
- **checklist**: "Unit Tests for English" - defines quality standards
- **analyze**: Cross-artifact validation - ensures consistency & coverage
- Both work independently, complement each other when used together

---

## Quality Assurance Approach

Inspired by [spec-kit's SDD methodology](https://github.com/github/spec-kit/blob/main/spec-driven.md), we use two complementary validation commands:

### checklist: Generate Quality Standards

**Purpose**: Create a quality checklist ("unit tests for English")

**What it does**:
- Generates checklist items that define "complete, clear, and consistent"
- Based on spec and plan content
- Acts as quality reference for team

**Example output**:
```markdown
### Requirement Completeness
- [ ] Every channel has budget allocation
- [ ] Every KPI has target value
- [ ] Content strategy defined

### Strategic Clarity  
- [ ] Channel selection rationale documented
- [ ] Timeline includes all milestones

### Consistency
- [ ] Total budget equals sum of channel budgets
- [ ] KPIs measurable with available tools
```

**Value**: 
- Defines quality standards early
- Prevents scope creep
- Provides objective criteria

---

### analyze: Validate Specifications

**Purpose**: Cross-artifact consistency & coverage analysis

**What it does**:
- **Coverage Analysis**: Do tasks cover all requirements from spec/plan?
- **Consistency Check**: Are spec, plan, and tasks aligned?
- **Conflict Detection**: Any contradictions or gaps?

**Inputs**:
- **Primary**: spec.md, plan.md, tasks.md
- **Optional reference**: checklist.md (as quality criteria)

**Example output**:
```markdown
### Coverage Analysis
✅ All 8 requirements from spec.md have corresponding tasks
✅ All 4 strategic channels from plan.md covered in tasks
⚠️ Budget allocation in tasks ($9,500) < plan ($10,000)

### Consistency Check
✅ Timeline in tasks aligns with plan (11 weeks)
❌ Conflict: plan mentions "email marketing" but no tasks defined
✅ Task dependencies form valid DAG (no circular deps)

### Checklist Validation (optional)
✅ 12/15 checklist items covered by current documents
⚠️ Missing: Risk mitigation strategies (checklist item #14)
```

**Value**:
- Catches misalignments before implementation
- Identifies missing coverage
- Validates logical consistency

---

### How They Work Together

**checklist** and **analyze** are **independent but complementary**:

```
checklist (optional but recommended):
  → Generates quality standards
  → Teams use as reference during tasks creation

tasks:
  → Created with or without checklist
  → Aims to cover spec + plan requirements

analyze (always useful):
  → Validates tasks against spec/plan
  → Can optionally reference checklist for quality criteria
  → Works fine even without checklist
```

**TDD-inspired flow** (when using both):
```
1. plan          → Define strategy
2. checklist     → Define quality standards
3. tasks         → Create implementation (guided by standards)
4. analyze       → Validate coverage & consistency (reference standards)
5. implement     → Execute
```

**Simplified flow** (checklist optional):
```
1. plan          → Define strategy
2. tasks         → Create implementation
3. analyze       → Validate coverage & consistency
4. implement     → Execute
```

---

## Architecture Understanding

### Two-Layer Architecture

```
Layer 1: specs/ (Specification Layer - Markdown)
└── Define WHAT to do
    - Requirements (specify)
    - Strategy (plan)
    - Tasks (tasks)
    - Analysis documents

Layer 2: operations/ (Operations Layer - YAML)
└── Define HOW to execute
    - Campaign configurations
    - Tracking setups
    - Content templates
    - Publishing schedules
```

### Complete Workflow

```
Phase 1: Requirements & Strategy (specs/)
├── /marketspec.specify      → specs/001/spec.md
├── /marketspec.clarify      → specs/001/clarifications.md
└── /marketspec.plan         → specs/001/plan.md

Phase 2: Quality Assurance (specs/)
├── /marketspec.checklist    → specs/001/checklist.md (optional: quality standards)
├── /marketspec.tasks        → specs/001/tasks.md
└── /marketspec.analyze      → specs/001/analysis.md (consistency & coverage validation)

Phase 3: Build Operations (operations/)
└── /marketspec.implement    → operations/campaigns/001.yaml
                               operations/content-templates/001/
                               operations/schedules/001.yaml
                               operations/tracking/001.yaml

Phase 4: Execute Campaign
    [Team uses operations/ files to run campaign]
    [Tools collect data to operations/data/001/]

Phase 5: Review & Optimize (specs/)
├── /marketspec.review       → specs/001/review.md
└── /marketspec.optimize     → specs/001/optimize.md
```

**Key Insights**:
- **checklist** (optional): Defines quality standards ("unit tests for English")
- **analyze** (recommended): Validates consistency & coverage before implement
- Per spec-kit: analyze runs "after `/speckit.tasks`, before `/speckit.implement`"

---

## Command Structure

### Core Commands (8) - Aligned with MetaSpec
1. ✅ **constitution** - Define marketing principles (Markdown)
2. ✅ **specify** - Define marketing requirements (Markdown)
3. ✅ **clarify** - Clarify marketing objectives (Markdown)
4. ✅ **plan** - Plan marketing strategy (Markdown)
5. ✅ **checklist** - Generate quality standards (Markdown) - *optional but recommended*
6. ✅ **tasks** - Break down implementation tasks (Markdown)
7. ✅ **analyze** - Cross-artifact consistency & coverage analysis (Markdown) - *before implement*
8. ✅ **implement** - **Execute tasks, build operations** (YAML) ⭐

### Extension Commands (2) - Marketing-Specific
9. ✅ **review** - Analyze campaign results (Markdown)
10. ✅ **optimize** - Generate optimization recommendations (Markdown)

---

## Completed Commands

### 1. marketspec.constitution ✅

**Status**: Rewritten  
**Source**: Adapted from metaspec.sds.constitution  
**Output**: `memory/constitution.md` (Part II: Marketing Specification Design Principles)

**Key Changes**:
- 8 marketing-specific principles (Audience Clarity, Objective Measurability, etc.)
- Focus on specification design, not campaign execution
- Domain-specific constraints (GDPR, brand guidelines, etc.)

### 2. marketspec.specify ✅

**Status**: Rewritten  
**Source**: Adapted from metaspec.sds.specify  
**Output**: `specs/{sequence}-{name}/spec.md` (draft specification)

**Key Changes**:
- Define marketing **requirements** (not strategy details)
- Focus on WHAT to achieve (objectives, audience, success criteria)
- NOT execution plans (those come in plan/implement)

**Template Structure**:
1. Executive Summary
2. Product/Service Overview
3. Marketing Objectives
4. Target Audience
5. Market Context
6. Resources & Constraints
7. Success Measurement
8. Assumptions & Risks

---

## Completed Command Details

### 3. marketspec.clarify ✅

**Status**: ✅ Rewritten

**Changes Made**:
- Updated frontmatter: `source: Adapted from metaspec.sds.clarify`
- Output: `specs/{sequence}-{name}/clarifications.md`
- Updated all references from discover/strategy to specify/plan
- Focus: Resolve ambiguities in marketing requirements

### 4. marketspec.plan ✅

**Status**: ✅ Rewritten and renamed

**Changes Made**:
- Renamed file from `marketspec.strategy.md` to `marketspec.plan.md`
- Updated all references from "strategy" to "plan"
- Source: `Adapted from metaspec.sds.plan`
- Output: `specs/{sequence}-{name}/plan.md`
- Focus: Plan marketing strategy **architecture** (not detailed tactics)

**Should Include**:
- Channel selection rationale
- Content strategy framework
- Campaign structure
- Budget allocation principles
- Timeline and milestones

### 5. marketspec.checklist ✅

**Status**: ✅ Updated

**Changes Made**:
- Updated frontmatter: `source: Adapted from metaspec.sds.checklist`
- Output: `specs/{sequence}-{name}/checklist.md`
- Updated references to implement instead of create
- Focus: Generate quality checklist (like "unit tests for English")

**Purpose**: Generate quality standards as reference
- Defines what "complete, clear, and consistent" means for this campaign
- Creates objective quality criteria
- Optional but recommended (helps guide subsequent work)

**Timing**: Runs **after plan**, before tasks
- Generates quality checklist items based on spec and plan
- Teams can reference during tasks creation
- Analyze can optionally use as validation criteria

**Example Checklist Items**:
```markdown
### Requirement Completeness
- [ ] Every channel has budget allocation defined
- [ ] Every KPI has target value specified
- [ ] Timeline includes all major milestones

### Strategic Clarity
- [ ] Channel strategy rationale documented
- [ ] Content themes aligned with objectives
- [ ] Budget allocation justified

### Consistency Validation
- [ ] Total budget equals sum of channel budgets
- [ ] Timeline feasible for planned activities
- [ ] KPIs measurable with available tools
```

**Note**: Checklist is **recommended but optional** - analyze can work without it.

### 6. marketspec.tasks ✅

**Status**: ✅ Updated

**Changes Made**:
- Updated frontmatter: `source: Adapted from metaspec.sds.tasks`
- Output: `specs/{sequence}-{name}/tasks.md`
- Updated references to plan instead of strategy
- Focus: Break down **implementation tasks** (what implement command will execute)

### 7. marketspec.analyze ✅

**Status**: ✅ Updated

**Changes Made**:
- Updated frontmatter: `source: Adapted from metaspec.sds.analyze`
- Output: `specs/{sequence}-{name}/analysis.md`
- Updated references to specify/plan/implement
- Focus: Cross-artifact consistency & coverage analysis

**Purpose**: Validate specifications before implementation
- **Coverage Analysis**: Do tasks cover all spec/plan requirements?
- **Consistency Check**: Are spec, plan, tasks aligned?
- **Conflict Detection**: Any contradictions or gaps?

**Timing**: Runs **after tasks**, before implement
- Per spec-kit: "run after `/speckit.tasks`, before `/speckit.implement`"
- Catches issues before costly implementation work
- Last quality gate before execution

**Primary Inputs**:
- spec.md (requirements)
- plan.md (strategy)
- tasks.md (implementation plan)

**Optional Input**:
- checklist.md (as quality reference)

**Example Analysis Output**:
```markdown
### Coverage Analysis
✅ All 8 requirements covered by tasks
⚠️ Budget in tasks ($9,500) < plan ($10,000)

### Consistency Check
✅ Timeline aligns across documents
❌ plan mentions "email marketing" but no tasks defined

### Checklist Reference (if available)
✅ 12/15 checklist items addressed
⚠️ Missing: Risk mitigation strategies
```

**Validation Commands Comparison**:

| Aspect | checklist | analyze |
|--------|-----------|---------|
| **Timing** | After `plan` | After `tasks`, before `implement` |
| **Nature** | Generate quality standards | Validate consistency & coverage |
| **Output** | Checklist items | Analysis report |
| **Question** | "What makes this complete?" | "Is this consistent and complete?" |
| **Primary Inputs** | spec + plan | spec + plan + tasks |
| **Optional Input** | N/A | checklist (as reference) |
| **Can work alone?** | Yes | Yes |
| **Benefit** | Defines quality criteria | Catches issues before implementation |

### 8. marketspec.implement ✅ **CRITICAL - MAJOR REWRITE**

**Status**: ✅ Completely rewritten (ARCHITECTURE CHANGE)

**Changes Made** (FUNDAMENTAL CHANGE):
- Renamed from `marketspec.create` to `marketspec.implement`
- Source: `Adapted from metaspec.sdd.implement` (**SDD**, not SDS!)
- Output: `operations/campaigns/{sequence}-{name}.yaml` + supporting files
- **Changed from Markdown generation to YAML/operations generation**

**Now Does** (Execute tasks, not aggregate docs):
```markdown
1. Read tasks.md (implementation tasks)
2. Read spec.md and plan.md (for context)
3. Execute each task systematically:
   - Task T001: Configure GitHub Stars tracking
     → Generate operations/tracking/001-tracking.yaml
   
   - Task T002: Create blog post templates
     → Generate operations/content-templates/001/blog-template.md
   
   - Task T003: Set up publishing schedule
     → Generate operations/schedules/001-schedule.yaml
   
   - Task T004: Configure channel settings
     → Generate operations/campaigns/001.yaml (main config)

4. Validate all generated files
5. Mark tasks as complete in tasks.md
```

**Example Output Structure**:
```
operations/
├── campaigns/
│   └── 001-q1-campaign.yaml           ← Main campaign configuration ⭐
│
├── content-templates/                 ← Content templates
│   └── 001-q1-campaign/
│       ├── blog-post-template.md
│       ├── tweet-template.md
│       ├── email-template.md
│       └── reddit-post-template.md
│
├── schedules/                         ← Publishing schedules
│   └── 001-q1-campaign-schedule.yaml
│
├── tracking/                          ← Tracking configurations
│   └── 001-q1-campaign-tracking.yaml
│
└── data/                              ← Data collection directory
    └── 001-q1-campaign/
        ├── .gitkeep
        └── README.md
```

**Key Distinction**:
- **Before**: Document aggregation → `specs/xxx/spec.md` (Markdown)
- **After**: Task execution → `operations/campaigns/xxx.yaml` (YAML + templates)

**Similar To**: `metaspec.sdd.implement` (executes code implementation tasks)

### 9. marketspec.review ✅ **CRITICAL - MAJOR REWRITE**

**Status**: ✅ Completely rewritten (ARCHITECTURE CHANGE)

**Changes Made** (FUNDAMENTAL CHANGE):
- Source: `Marketing-specific extension`
- Output: `specs/{sequence}-{name}/review.md` ⭐
- Changed from **defining review process** to **executing review analysis**

**Now Does** (Execute analysis, not define process):
```markdown
1. Read expected targets from specs/001/spec.md
   - KPI targets (GitHub Stars: 500, Email: 1000)
   - Budget ($10,000)
   - Timeline

2. Collect actual data:
   - From operations/data/001/ (collected during campaign)
   - Or via tracking tools (operations/tracking/001-tracking.yaml)
   - Or ask user for manual input

3. Compare actual vs expected:
   - GitHub Stars: 450/500 = 90% ⚠️
   - Email: 1200/1000 = 120% ✅
   - Calculate achievement rates

4. Analyze performance:
   - Channel analysis (Twitter 9/10, Reddit 4/10)
   - Content effectiveness (tutorials 2x better)
   - Budget utilization

5. Document lessons learned:
   - What worked (landing page design, Twitter frequency)
   - What didn't (Reddit targeting, announcements)

6. Generate review report → specs/001/review.md
```

**Example Output**:
```markdown
# Campaign Review: Q1 2025 Developer Outreach

**Overall Achievement**: 100.2%

## KPI Achievement
| KPI | Target | Actual | Achievement |
|-----|--------|--------|-------------|
| GitHub Stars | 500 | 450 | 90% ⚠️ |
| Email Subs | 1000 | 1200 | 120% ✅ |

## Channel Performance
- Twitter: 9/10 (top performer)
- Blog: 8/10
- Dev.to: 7/10
- Reddit: 4/10 (underperformer)

## Lessons Learned
✅ Landing page simplicity drove 8% conversion
✅ Tutorial content outperformed 2:1
❌ Reddit broad targeting failed
```

**Key Distinction**:
- **Before**: Define review process/methodology
- **After**: Execute review, analyze results, generate report

**Similar To**: Conducting an actual post-mortem analysis

### 10. marketspec.optimize ✅ **CRITICAL - MAJOR REWRITE**

**Status**: ✅ Completely rewritten (ARCHITECTURE CHANGE)

**Changes Made** (FUNDAMENTAL CHANGE):
- Source: `Marketing-specific extension`
- Output: `specs/{sequence}-{name}/optimize.md` ⭐
- Changed from **defining optimization methodology** to **executing optimization analysis**

**Now Does** (Generate recommendations, not define process):
```markdown
1. Read review results from specs/001/review.md
   - KPI achievement
   - Channel performance
   - Success factors
   - Issues identified

2. Identify optimization opportunities:
   - Scale what works: Twitter (9/10) → increase budget 30%
   - Fix what's broken: Reddit (4/10) → pivot strategy or cut
   - Optimize existing: Blog timing → Tuesday/Thursday only

3. Generate budget reallocation:
   - Twitter: $1000 → $1300 (+30%)
   - Dev.to: $500 → $700 (+40%)
   - Reddit: $500 → $250 (-50%)

4. Create content strategy optimization:
   - Shift to 70% tutorials (from 55%)
   - Reduce announcements to 5% (from 14%)

5. Develop implementation plan:
   - Week 1: Create templates
   - Week 2: Update content calendar
   - Week 3-4: Test new strategies

6. Generate optimization report → specs/001/optimize.md
```

**Example Output**:
```markdown
# Optimization Recommendations: Q1 Campaign

## Priority Recommendations

### P0: Increase Twitter Budget by 30%
- Current: $1,000
- Proposed: $1,300
- Rationale: Top performer (9/10)
- Expected impact: +36 conversions

### P1: Shift to 70% Tutorial Content
- Current: 55% tutorials
- Proposed: 70% tutorials
- Rationale: 2x performance
- Expected impact: +15% engagement

## Budget Reallocation
| Channel | Current | Proposed | Change |
|---------|---------|----------|--------|
| Twitter | $1,000 | $1,300 | +30% |
| Reddit | $500 | $250 | -50% |

## Implementation Timeline
- Week 1: Setup & templates
- Week 2: Content calendar update
- Week 3-4: Testing
```

**Key Distinction**:
- **Before**: Define optimization methodology/framework
- **After**: Execute optimization analysis, generate specific recommendations

**Similar To**: Generating an actual improvement plan with specific actions

---

## Implementation Checklist

### Phase 1: Rewrite Commands ✅ COMPLETED

- [x] 1. constitution (Done)
- [x] 2. specify (Done)
- [x] 8. **implement** (✅ MAJOR REWRITE - now generates operations/)
- [x] 4. plan (Important - rename from strategy)
- [x] 9. **review** (✅ MAJOR REWRITE - now executes analysis)
- [x] 10. **optimize** (✅ MAJOR REWRITE - now generates recommendations)
- [x] 3. clarify (Minor fixes)
- [x] 5. checklist (Minor fixes)
- [x] 6. tasks (Minor fixes)
- [x] 7. analyze (Minor fixes)

### Phase 2: Update Documentation (✅ MOSTLY COMPLETED)

- [ ] Update `specs/toolkit/001-marketing-spec-kit-implementation/spec.md`
  - Component 5: Update architecture (specs/ vs operations/)
  - Update workflow diagram
  - Document two-layer architecture
  
- [x] Update `templates/sdm/commands/README.md`
  - ✅ Updated command table (8 Core + 2 Extension)
  - ✅ Documented two-layer architecture
  - ✅ Added workflow examples
  - ✅ Clarified implement generates operations/ YAML
  
- [x] Update `AGENTS.md`
  - ✅ Complete rewrite with two-layer architecture
  - ✅ Added step-by-step workflow examples
  - ✅ Documented all 10 commands with outputs
  - ✅ Clarified review/optimize execute post-campaign analysis
  
- [x] Update project `README.md`
  - ✅ Updated Quick Start with two-layer architecture
  - ✅ Replaced old command names (discover/strategy/create) with new (specify/plan/implement)
  - ✅ Updated architecture diagram
  - ✅ Added complete workflow examples
  - ✅ Updated project structure section

- [x] Update `src/marketing_spec_kit/generator.py`
  - ✅ Generator creates infrastructure only (memory/, specs/, README, .gitignore)
  - ✅ Generator does NOT pre-create `config/`, `templates/`, `data/`, `src/` directories
  - ✅ These directories created by `/marketspec.implement` when generating code + configs
  - ✅ Comments updated to reflect distributed architecture

### Phase 3: Testing (PENDING)

- [ ] Test complete workflow
  - specify → plan → tasks → implement
  - Verify operations/ files generated
- [ ] Test review with actual/mock data
- [ ] Test optimize based on review
- [ ] Integration test full cycle

---

## Key Architecture Changes

### 1. Distributed Directory Structure (Final Architecture)

**specs/** (战略规范 - Markdown)
- Human-readable specifications
- Strategy, planning, reports

**config/** (活动配置 - YAML)
- Campaign configurations
- Adjustable parameters

**templates/** (内容模板 - Markdown/Text)
- Content templates
- Reusable formats

**data/** (收集的数据 - JSON)
- Runtime metrics
- Performance data

**src/** (执行代码 - TypeScript)
- Executable campaign code
- MCP tool wrappers

### 2. Command Types

**Specification Commands** (4): Define WHAT
- constitution, specify, clarify, plan

**Quality Assurance Commands** (2): Validate specifications
- **checklist** (generate quality standards - optional but recommended)
- **analyze** (consistency & coverage analysis - always recommended)

**Planning Command** (1): Define HOW
- tasks (break down into implementation steps)

**Implementation Command** (1): Generate code + configs
- implement (generates src/ code + config/ + templates/)

**Post-Campaign Commands** (2): Analyze & improve
- review (analyze results - Markdown)
- optimize (generate recommendations - Markdown)

**QA Flow** (recommended):
```
plan → checklist (define standards) → tasks → analyze (validate) → implement
```

**Minimal Flow** (if skipping checklist):
```
plan → tasks → analyze (validate) → implement
```

### 3. Data Flow

```
specs/001/spec.md (WHAT) ← specify
       ↓
specs/001/clarifications.md ← clarify
       ↓
specs/001/plan.md (Strategy) ← plan
       ↓
       ├─→ specs/001/checklist.md ← checklist (optional: quality standards)
       │                                │
       │                                │ (can reference)
       ↓                                ↓
specs/001/tasks.md (Tasks) ← tasks ←────┘
       ↓
specs/001/analysis.md ← analyze (validates spec+plan+tasks, optionally refs checklist)
       ↓
/marketspec.implement (Generate code + configs)
       ↓
src/campaigns/001.ts ← executable TypeScript code ⭐
src/shared/mcp-tools/*.ts
config/001.yaml (configuration)
templates/001/ (content templates)
       ↓
[Campaign Execution]
       ↓
operations/data/001/ (Collected data)
       ↓
/marketspec.review (Analyze results)
       ↓
specs/001/review.md (Results)
       ↓
/marketspec.optimize (Generate improvements)
       ↓
specs/001/optimize.md (Recommendations)
       ↓
[Feed into next campaign's specify/plan]
```

**Key Points**:
- **checklist** is optional but recommended (provides quality standards)
- **tasks** can reference checklist if it exists (but not required)
- **analyze** always validates spec+plan+tasks (checklist is optional reference)
- **implement** executes tasks regardless of checklist existence

---

## ✅ Completion Summary

**Date Completed**: 2024-11-19 (Major update evening)

### What Was Accomplished

All 10 SDM commands successfully rewritten with **major architecture changes**:

**Specification Commands (7)**: Markdown output
1. ✅ marketspec.constitution
2. ✅ marketspec.specify
3. ✅ marketspec.clarify
4. ✅ marketspec.plan (renamed from strategy)
5. ✅ marketspec.tasks
6. ✅ marketspec.analyze
7. ✅ marketspec.checklist

**Implementation Command (1)**: YAML + template output
8. ✅ marketspec.implement - **MAJOR REWRITE** ⭐
   - Changed from document aggregation to task execution
   - Generates operations/*.yaml files
   - Creates content templates
   - Sets up tracking configurations

**Analysis Commands (2)**: Markdown output
9. ✅ marketspec.review - **MAJOR REWRITE** ⭐
   - Changed from defining process to executing analysis
   - Analyzes actual campaign results
   - Generates review report

10. ✅ marketspec.optimize - **MAJOR REWRITE** ⭐
    - Changed from defining methodology to generating recommendations
    - Creates specific improvement plan
    - Proposes budget reallocations

### Key Changes

1. **Two-layer architecture**: specs/ (Markdown) + operations/ (YAML)
2. **implement generates YAML**, not Markdown
3. **review executes analysis**, not defines process
4. **optimize generates recommendations**, not defines methodology
5. **Complete workflow** from specification → implementation → execution → analysis

### Files Changed

**Major Rewrites**:
- `templates/sdm/commands/marketspec.implement.md` - **COMPLETELY REWRITTEN** ⭐
- `templates/sdm/commands/marketspec.review.md` - **COMPLETELY REWRITTEN** ⭐
- `templates/sdm/commands/marketspec.optimize.md` - **COMPLETELY REWRITTEN** ⭐

**Renamed**:
- `templates/sdm/commands/marketspec.plan.md` - **NEW** (replaces strategy)
- `templates/sdm/commands/marketspec.strategy.md` - **DELETED**

**Updated**:
- `templates/sdm/commands/marketspec.clarify.md`
- `templates/sdm/commands/marketspec.checklist.md`
- `templates/sdm/commands/marketspec.tasks.md`
- `templates/sdm/commands/marketspec.analyze.md`

---

## Architecture Evolution Summary (2024-11-20)

### From Three-Layer to Distributed Structure

**Previous (2024-11-19)**:
```
specs/ (Markdown)
operations/ (YAML + templates + data)
src/ (TypeScript)
```

**Final (2024-11-20)**:
```
specs/ (Markdown - 战略规范)
config/ (YAML - 活动配置)
templates/ (Markdown/Text - 内容模板)
data/ (JSON - 收集的数据)
src/ (TypeScript - 执行代码)
```

### Key Rationale

1. **Semantic Clarity**: "operations" ambiguous in marketing context (strategy vs data)
2. **Industry Standards**: config/, templates/, data/ are universal conventions
3. **Single Responsibility**: Each directory has one clear purpose
4. **12-Factor App**: Separates config from code
5. **Discoverability**: Clear names reduce cognitive load

### Documentation Updated

- ✅ `marketspec.implement.md` - All path references updated
- ✅ `README.md` - Complete architecture section rewrite
- ✅ `AGENTS.md` - Full refactor with new structure
- ✅ `templates/sdm/commands/README.md` - Updated for AI assistants
- ✅ `generator.py` - Comments reflect distributed architecture
- ✅ `sdm-commands.md` - This document

---

## Next Steps

### Immediate (Phase 2)

1. Update documentation to reflect two-layer architecture
2. Update README with complete workflow examples
3. Update AGENTS.md with operations/ examples
4. Ensure `generator.py` creates operations/ directory

### Testing (Phase 3)

1. Test full workflow: specify → implement → review → optimize
2. Verify operations/ files generate correctly
3. Test review with mock data
4. Integration test complete cycle

### Future Enhancements

1. Consider MCP tool integration for data collection
2. Add validation schemas for operations/*.yaml
3. Create example operations/ files
4. Document operations/ file formats
