# SDM Layer: Spec-Driven Marketing

**Spec-Driven Marketing** - Execute marketing activities using validated specifications.

---

## 🎯 Purpose

The SDM layer provides commands to **execute marketing activities** by creating structured YAML specifications:
- ✅ Discover marketing needs
- ✅ Plan marketing strategies
- ✅ Create marketing specifications
- ✅ Validate quality
- ✅ Analyze consistency

---

## 📋 Commands (10)

### Architecture (Based on MetaSpec SDD)

```
Core Flow:      constitution → discover → strategy → tasks → create
                       🔴           🔴         🔴        🔴      🔴
Quality Gates:             ↓ clarify ↓     ↓ checklist     ↓ analyze
                              🟡              🟡                🟡
                           (before)        (after)          (before)
```

### Core Flow (5) - Essential Workflow

| # | Command | Type | Purpose |
|---|---------|------|---------|
| 1 | `/marketspec.constitution` | 🔴 Core | Establish marketing principles |
| 2 | `/marketspec.discover` | 🔴 Core | Discover marketing needs |
| 4 | `/marketspec.strategy` | 🔴 Core | Plan marketing strategy |
| 6 | `/marketspec.tasks` | 🔴 Core | Break down implementation tasks |
| 8 | `/marketspec.create` | 🔴 Core | Generate specification YAML |

### Quality Gates (3) - Recommended for Quality Assurance

| # | Command | Type | Purpose |
|---|---------|------|---------|
| 3 | `/marketspec.clarify` | 🟡 Quality Gate | Clarify ambiguities (before strategy) |
| 5 | `/marketspec.checklist` | 🟡 Quality Gate | Validate completeness (after strategy) |
| 7 | `/marketspec.analyze` | 🟡 Quality Gate | Check consistency (before create) |

### Extension (2) - Feedback Loop

| # | Command | Type | Purpose |
|---|---------|------|---------|
| 9 | `/marketspec.review` | 🔵 Extension | Analyze actual vs. planned |
| 10 | `/marketspec.optimize` | 🔵 Extension | Generate optimization recommendations |

### Complete Marketing Cycle

```
Phase 1 - Specification (Core + Quality Gates):
constitution → discover → clarify → strategy → 
checklist → tasks → analyze → create
                              ↓
Phase 2 - Execution (AI Agent + MCP Tools):
                     [Execute Campaign]
                              ↓
Phase 3 - Optimization (Feedback Loop):
                  review → optimize
                              ↓
Next Cycle:      feed into next discover
```

### Command Details

#### 1. /marketspec.constitution 🔴 Core
**Purpose**: Establish marketing principles for the project  
**Adapted from**: `metaspec.sdd.constitution`  
**Output**: `marketing-constitution.md`  
**Rationale**: Sets foundation for consistent decision-making across campaigns

#### 2. /marketspec.discover 🔴 Core
**Purpose**: Discover and document marketing needs  
**Adapted from**: `metaspec.sdd.specify`  
**Output**: `*-discovery.md`  
**Rationale**: Starting point - defines what needs to be specified

#### 3. /marketspec.clarify 🟡 Quality Gate
**Purpose**: Resolve ambiguities before planning strategy  
**Adapted from**: `metaspec.sdd.clarify`  
**Output**: `*-clarification.md`  
**Timing**: BEFORE strategy  
**Rationale**: Prevents strategy mistakes from unclear requirements

#### 4. /marketspec.strategy 🔴 Core
**Purpose**: Plan the marketing approach and architecture  
**Adapted from**: `metaspec.sdd.plan`  
**Output**: `*-strategy.md`  
**Rationale**: Defines how to structure the specification

#### 5. /marketspec.checklist 🟡 Quality Gate
**Purpose**: Validate strategy completeness  
**Adapted from**: `metaspec.sdd.checklist`  
**Output**: `*-checklist.md`  
**Timing**: AFTER strategy  
**Rationale**: Catches missing requirements before task breakdown

#### 6. /marketspec.tasks 🔴 Core
**Purpose**: Break down into actionable implementation tasks  
**Adapted from**: `metaspec.sdd.tasks`  
**Output**: `*-tasks.md`  
**Rationale**: Guides what to include in the specification

#### 7. /marketspec.analyze 🟡 Quality Gate
**Purpose**: Check consistency before finalizing specification  
**Adapted from**: `metaspec.sdd.analyze`  
**Output**: `consistency-report.md`  
**Timing**: BEFORE create  
**Rationale**: Final validation before generating YAML

#### 8. /marketspec.create 🔴 Core
**Purpose**: Generate the final marketing specification YAML  
**Adapted from**: `metaspec.sdd.implement` (for specifications)  
**Output**: `marketing-spec.yaml` ⭐  
**Rationale**: Core output - the executable specification

#### 9. /marketspec.review 🔵 Extension
**Purpose**: Analyze campaign performance after execution  
**Timing**: POST-EXECUTION  
**Output**: `campaign-review.md`  
**Rationale**: Measures actual vs. planned results

#### 10. /marketspec.optimize 🔵 Extension
**Purpose**: Generate optimization recommendations based on review  
**Timing**: POST-EXECUTION (after review)  
**Output**: `optimization-plan.md`  
**Rationale**: Continuous improvement for next cycle

---

## 🎓 Quick Start

### Minimal Workflow (Required steps only)

```bash
# 1. Discover needs (REQUIRED)
/marketspec.discover "Grow MetaSpec user base"

# 2. Create specification (REQUIRED)
/marketspec.create
→ Output: marketing-spec.yaml
```

**Use for**: Quick campaigns, simple promotions, testing

### Recommended Workflow (Most common)

```bash
# 1. Discover needs (REQUIRED)
/marketspec.discover "Grow MetaSpec user base"

# 2. Clarify requirements (optional)
/marketspec.clarify

# 3. Plan strategy (optional but recommended for > $5K)
/marketspec.strategy

# 4. Create specification (REQUIRED)
/marketspec.create
→ Output: marketing-spec.yaml

# 5. Validate quality (RECOMMENDED)
/marketspec.checklist
```

**Use for**: Standard campaigns, multi-channel marketing, team projects

### Complete Workflow (All steps)

```bash
# ===== PLANNING PHASE =====

# 1. Define principles (if first time)
/marketspec.constitution

# 2. Discover needs (REQUIRED)
/marketspec.discover "Grow MetaSpec user base"

# 3. Clarify ambiguities
/marketspec.clarify

# 4. Plan strategy
/marketspec.strategy

# 5. Validate strategy (RECOMMENDED)
/marketspec.checklist

# 6. Break down tasks
/marketspec.tasks

# 7. Check consistency
/marketspec.analyze

# 8. Create specification (REQUIRED)
/marketspec.create
→ Output: marketing-spec.yaml

# ===== EXECUTION PHASE =====

# Execute the campaign...
# (3-12 weeks typically)

# ===== REVIEW PHASE (Extension) =====

# 9. Analyze actual performance
/marketspec.review
→ Output: campaign-review.md

# 10. Generate optimization recommendations
/marketspec.optimize
→ Output: optimization-recommendations.md

# Feed recommendations into next campaign
/marketspec.discover "Q2 Growth" --based-on optimization-recommendations.md
```

**Use for**: Complex campaigns (> $10K), long-term (> 3 months), critical launches, continuous improvement cycles

---

## 📁 Directory Structure

```
sdm/
├── README.md                     # This file
├── commands/                     # 10 SDM commands
│   ├── marketspec.constitution.md   # 1. Define principles
│   ├── marketspec.discover.md       # 2. Define requirements
│   ├── marketspec.clarify.md        # 3. Clarify ambiguities (QG)
│   ├── marketspec.strategy.md       # 4. Plan strategy
│   ├── marketspec.checklist.md      # 5. Validate strategy (QG)
│   ├── marketspec.tasks.md          # 6. Break down tasks
│   ├── marketspec.analyze.md        # 7. Check consistency (QG)
│   ├── marketspec.create.md         # 8. Generate spec
│   ├── marketspec.review.md         # 9. Analyze performance (Extension)
│   └── marketspec.optimize.md       # 10. Optimization recommendations (Extension)
│
└── templates/                    # YAML output templates
    ├── minimal.yaml
    ├── default.yaml
    └── full.yaml
```

---

## 📄 Output Format

### Primary Format: YAML

```yaml
# marketing-spec.yaml
specification_version: "0.3.0"

project:
  name: "MetaSpec"
  tagline: "Spec-Driven Development Framework"

plans:
  - id: "2025-q1"
    name: "2025 Q1 Growth Plan"
    objectives:
      - "Increase GitHub stars to 1000"

campaigns:
  - id: "dev-outreach"
    name: "Developer Outreach"
    plan_id: "2025-q1"
    goal: "awareness"
```

### Optional: Markdown Documentation

```markdown
# marketing-plan.md (optional)
Human-readable strategy documentation, background analysis
```

---

## 🔄 MetaSpec Framework Mapping

| MetaSpec SDS | marketing-spec-kit SDM | Change |
|--------------|------------------------|--------|
| constitution | constitution | ✅ Same |
| specify | **discover** | 🔄 Renamed (marketing-friendly) |
| clarify | clarify | ✅ Same |
| plan | **strategy** | 🔄 Renamed (marketing-friendly) |
| tasks | tasks | ✅ Same |
| implement | **create** | 🔄 Renamed (more intuitive) |
| checklist | checklist | ✅ Same |
| analyze | analyze | ✅ Same |

**Design Principle**: Balance framework consistency with domain usability.

---

## 📚 Learn More

- [Main Templates Guide](../README.md)
- [Domain Specification](../../specs/domain/001-marketing-operations-spec/spec.md)
- [Architecture Decisions](../../docs/internal/architecture-decisions-2025-11-16.md)
- [Complete Examples](../../examples/)
