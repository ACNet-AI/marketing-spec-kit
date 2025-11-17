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

### Core Commands (8) - Planning Phase

```
Core Flow:      constitution → discover → strategy → tasks → create
Quality Gates:             ↓ clarify ↓     ↓ checklist     ↓ analyze
                           (before)      (after)         (before)
```

**Planning Flow** (Based on MetaSpec SDD):

| Step | Command | Type | Purpose |
|------|---------|------|---------|
| 1 | constitution | Core | Define principles |
| 2 | discover | Core | Define requirements |
| 3 | **clarify** | **Quality Gate** | **Resolve ambiguities (BEFORE strategy)** |
| 4 | strategy | Core | Plan approach |
| 5 | **checklist** | **Quality Gate** | **Validate requirements (AFTER strategy)** |
| 6 | tasks | Core | Break down work |
| 7 | **analyze** | **Quality Gate** | **Check consistency (BEFORE create)** |
| 8 | create | Core | Generate spec |

**Execution Order**: `constitution → discover → clarify → strategy → checklist → tasks → analyze → create`

### Extension Commands (2) - Post-Execution Phase

```
... → create → [Execute Campaign] → review → optimize
                                      ↓         ↓
                                 分析效果   优化建议
```

**Post-Execution Flow**:

| Step | Command | Type | Purpose |
|------|---------|------|---------|
| 9 | **review** | **Extension** | **Analyze actual performance vs plan** |
| 10 | **optimize** | **Extension** | **Generate recommendations for next campaign** |

**Complete Marketing Cycle**:

```
Planning (8 steps):   constitution → discover → clarify → strategy → 
                      checklist → tasks → analyze → create
                                                       ↓
Execution:                                    [Execute Campaign]
                                                       ↓
Review (2 steps):                            review → optimize
                                                       ↓
Next Cycle:                              feed into next discover
```

### Command Details

#### 1. /marketspec.constitution ⚪
**Purpose**: Define marketing execution principles  
**Adapted from**: `metaspec.sds.constitution`  
**Output**: Marketing execution principles document  
**When to skip**: If principles already documented or simple one-off campaign

#### 2. /marketspec.discover 🔴
**Purpose**: Discover marketing needs and requirements  
**Adapted from**: `metaspec.sds.specify`  
**Output**: Initial requirements definition  
**Required**: Always - this is the foundation

#### 3. /marketspec.clarify ⚪
**Purpose**: Clarify marketing objectives and resolve ambiguities  
**Adapted from**: `metaspec.sds.clarify`  
**Output**: Clarified requirements  
**Type**: Quality Gate (BEFORE strategy)  
**When to skip**: If requirements are already clear and unambiguous

#### 4. /marketspec.strategy ⚪
**Purpose**: Plan marketing strategy and approach  
**Adapted from**: `metaspec.sds.plan`  
**Output**: Strategic plan document  
**When to skip**: Simple campaigns (< $5K, single channel, < 4 weeks)

#### 5. /marketspec.tasks ⚪
**Purpose**: Break down marketing tasks  
**Adapted from**: `metaspec.sds.tasks`  
**Output**: Task breakdown  
**When to skip**: Small team (1-2 people) or simple execution

#### 6. /marketspec.create 🔴
**Purpose**: Create marketing specification (YAML)  
**Adapted from**: `metaspec.sds.implement`  
**Output**: `marketing-spec.yaml`  
**Required**: Always - this is the deliverable

#### 5. /marketspec.checklist ⚪
**Purpose**: Generate quality checklist (automated validation + manual review)  
**Adapted from**: `metaspec.sds.checklist`  
**Output**: Quality checklist document  
**Type**: Quality Gate (AFTER strategy)  
**When to use**: Validate strategy before breaking down tasks

#### 8. /marketspec.analyze ⚪
**Purpose**: Check cross-document consistency before creating spec  
**Adapted from**: `metaspec.sds.analyze`  
**Output**: Consistency analysis report  
**Type**: Quality Gate (BEFORE create)  
**When to skip**: Simple campaigns or when checklist is sufficient

#### 9. /marketspec.review ⚪
**Purpose**: Analyze actual campaign performance after execution  
**New Command**: Original to marketing-spec-kit  
**Output**: Campaign review report  
**Type**: Extension (POST-EXECUTION)  
**When to use**: After campaign execution to document results and lessons learned

#### 10. /marketspec.optimize ⚪
**Purpose**: Generate optimization recommendations based on review data  
**New Command**: Original to marketing-spec-kit  
**Output**: Optimization recommendations  
**Type**: Extension (POST-EXECUTION, after review)  
**When to use**: After review to prepare data-driven recommendations for next campaign

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
