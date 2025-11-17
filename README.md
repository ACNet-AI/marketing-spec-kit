# marketing-spec-kit

**Specification Toolkit for Marketing Operations** - Transform marketing chaos into structured, AI-driven workflows.

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](./CHANGELOG.md)
[![Python](https://img.shields.io/badge/python-3.9+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](./LICENSE)

---

## 🌟 What is marketing-spec-kit?

A **Spec-Driven Toolkit** that enables marketing teams to:

✅ **Define** marketing operations as structured YAML specifications  
✅ **Validate** plans, campaigns, and content against 45 business rules  
✅ **Execute** with 22 AI Agent Slash Commands for automated workflows  
✅ **Analyze** performance with AI-generated insights and optimization recommendations  

**v2.0.0** introduces a complete **5-phase marketing workflow** system:

```
Strategic Planning → Campaign Design → Content Creation → Execution → Analytics & Optimization
```

---

## 🚀 Quick Start

### Installation

```bash
# Using pip
pip install marketing-spec-kit

# Using uv (recommended)
uv pip install marketing-spec-kit
```

### Create Your First Marketing Plan

```bash
# Initialize a new specification
marketing_spec_kit init my-marketing-spec.yaml

# Validate the specification
marketing_spec_kit validate my-marketing-spec.yaml
```

### Use SDM (Spec-Driven Marketing) Commands

**New in v2.1**: Complete 10-command workflow system with closed-loop optimization!

```bash
# Minimal workflow (2 steps) - Quick campaign
/marketspec.discover "Grow user base in Q1 2025"
/marketspec.create
→ Output: marketing-spec.yaml

# Recommended workflow (5 steps) - Standard project
/marketspec.discover "Grow user base in Q1 2025"
/marketspec.clarify
/marketspec.strategy
/marketspec.create
/marketspec.checklist
→ Output: marketing-spec.yaml + quality report

# Complete workflow (10 steps) - Complex campaign with optimization
# Planning Phase (8 steps)
/marketspec.constitution
/marketspec.discover "Q1 2025 Growth"
/marketspec.clarify
/marketspec.strategy
/marketspec.checklist
/marketspec.tasks
/marketspec.analyze
/marketspec.create

# Execute campaign...

# Review Phase (2 steps)
/marketspec.review         # Analyze actual vs planned
/marketspec.optimize       # Get optimization recommendations for next campaign
```

**See [SDM Workflow Example](./examples/sdm-workflow-example.md) for complete walkthrough!**

---

## 📋 Core Entities (9)

marketing-spec-kit v2.0.0 manages 9 marketing entities:

| Entity | Purpose | Fields | New in v2.0 |
|--------|---------|--------|-------------|
| **Project** | Brand identity and core values | 9 | |
| **Product** | Feature offerings and positioning | 8 | |
| **MarketingPlan** | Strategic marketing plan | 14 | ✅ |
| **Campaign** | Time-bound marketing activities | 15 | ✨ Updated |
| **Channel** | Distribution platforms | 9 | |
| **Tool** | Integration automation | 7 | |
| **ContentTemplate** | Brand guidelines and constraints | 9 | |
| **Milestone** | Timeline markers and events | 9 | |
| **Analytics** | Performance analytics report | 9 | ✅ |

**New in v2.0.0**:
- **MarketingPlan**: Strategic planning with objectives, budget, KPIs
- **Analytics**: AI-powered performance analysis and optimization
- **Campaign.plan_id**: Now REQUIRED (links campaigns to plans)

---

## 🎯 5-Phase Workflow

### Phase 1: Strategic Planning

```bash
/marketing.plan.create      # Create plan with objectives, budget, KPIs
/marketing.plan.validate    # Validate against 5 rules
/marketing.plan.analyze     # AI strategic analysis
```

### Phase 2: Campaign Design

```bash
/marketing.campaign.design  # AI-assisted campaign design
/marketing.campaign         # Get campaign details
```

### Phase 3: Content Creation

```bash
/marketing.content.plan           # Generate content calendar
/marketing.generate.post          # Generate social media post
/marketing.generate.article       # Generate blog article
/marketing.generate.email         # Generate email campaign
/marketing.generate.landing_page  # Generate landing page copy
```

### Phase 4: Execution & Publishing

```bash
/marketing.execute.schedule  # Schedule content for future publication
/marketing.execute.publish   # Publish content immediately
```

### Phase 5: Analytics & Optimization

```bash
/marketing.analytics.campaign     # Campaign performance report
/marketing.analytics.plan         # Plan-level analytics
/marketing.optimize.suggest       # AI optimization suggestions
```

---

## 🔧 CLI Commands

| Command | Description |
|---------|-------------|
| `init <file>` | Create a new marketing specification from template |
| `validate <file>` | Validate specification against 45 rules |
| `info` | Show toolkit version and statistics |

---

## 🎯 SDM Command System (10)

**New in v2.1**: Complete Spec-Driven Marketing workflow with closed-loop optimization!

### Core Commands (8) - Planning Phase

| # | Command | Purpose | Type | Output |
|---|---------|---------|------|--------|
| 1 | `/marketspec.constitution` | Define marketing principles | ⚪ Optional | `marketing-constitution.md` |
| 2 | `/marketspec.discover` | Discover marketing needs | 🔴 Required | `*-discovery.md` |
| 3 | `/marketspec.clarify` | Clarify objectives | ⚪ Optional | `*-clarification.md` |
| 4 | `/marketspec.strategy` | Plan marketing strategy | ⚪ Optional | `*-strategy.md` |
| 5 | `/marketspec.checklist` | Quality validation | 🟡 Recommended | `*-checklist.md` |
| 6 | `/marketspec.tasks` | Break down tasks | ⚪ Optional | `*-tasks.md` |
| 7 | `/marketspec.analyze` | Consistency checking | ⚪ Optional | `consistency-report.md` |
| 8 | `/marketspec.create` | Generate spec YAML | 🔴 Required | `marketing-spec.yaml` ⭐ |

### Extension Commands (2) - Post-Execution Phase

| # | Command | Purpose | Type | Output |
|---|---------|---------|------|--------|
| 9 | `/marketspec.review` | Analyze actual performance | ⚪ Optional | `campaign-review.md` |
| 10 | `/marketspec.optimize` | Optimization recommendations | ⚪ Optional | `optimization-recommendations.md` |

### Workflow Patterns

**Minimal** (2 steps): `discover → create`  
**Recommended** (5 steps): `discover → clarify → strategy → create → checklist`  
**Complete** (10 steps): All commands for complex campaigns with optimization

**Closed-Loop Marketing**:
```
Planning (8) → Execution → Review (2) → Next Campaign Planning
     ↑____________________________________________↓
              (Continuous Improvement)
```

### Documentation

- 📄 [SDM Layer Overview](./templates/sdm/README.md)
- 📖 [Complete Workflow Example](./examples/sdm-workflow-example.md)
- 🏗️ [Architecture Decisions](./docs/internal/architecture-decisions-2025-11-16.md)
- ✅ [Implementation Report](./docs/internal/sdm-implementation-complete-2025-11-16.md)

---

## 🤖 Entity Commands (Planned)

### Data Access (7 commands)
- `/marketing.project` - Get brand identity
- `/marketing.product` - Get product features
- `/marketing.plan.get` - Get plan details **[NEW]**
- `/marketing.campaign` - Get campaign goals
- `/marketing.channel` - Get channel details
- `/marketing.tool` - Get tool integrations
- `/marketing.milestone` - Get milestone events

### Strategic Planning (4 commands) **[NEW]**
- `/marketing.plan.create` - Create marketing plan
- `/marketing.plan.validate` - Validate plan
- `/marketing.plan.analyze` - AI strategic analysis

### Campaign & Content (3 commands)
- `/marketing.campaign.design` - AI-assisted campaign design **[NEW]**
- `/marketing.content_template` - Get content guidelines
- `/marketing.content.plan` - Generate content calendar **[NEW]**

### Content Generation (4 commands)
- `/marketing.generate.post` - Generate social media post
- `/marketing.generate.article` - Generate blog article
- `/marketing.generate.email` - Generate email campaign
- `/marketing.generate.landing_page` - Generate landing page copy

### Task Execution (2 commands)
- `/marketing.execute.schedule` - Schedule content
- `/marketing.execute.publish` - Publish content

### Analytics & Optimization (3 commands) **[NEW]**
- `/marketing.analytics.campaign` - Campaign analytics report
- `/marketing.analytics.plan` - Plan-level analytics
- `/marketing.optimize.suggest` - AI optimization suggestions

---

## ✅ Validation Rules (45)

marketing-spec-kit enforces 45 business rules across all entities:

| Entity | Rules | Key Validations |
|--------|-------|----------------|
| Project | 6 | Brand voice, website HTTPS, target audience |
| Product | 5 | Pricing, launch date, feature list |
| **MarketingPlan** | **5** | **Budget balance, approval, objectives** **[NEW]** |
| Campaign | 11 | Budget, dates, channels, **plan linkage** **[UPDATED]** |
| Channel | 6 | Platform, constraints, tool integration |
| Tool | 6 | Credentials, rate limits, integration |
| ContentTemplate | 5 | Brand compliance, format, examples |
| Milestone | 5 | Date validity, product/campaign links |
| **Analytics** | **1** | **Entity reference validation** **[NEW]** |

**Performance**: Validation completes in <250ms for typical specifications.

---

## 📊 Example Specification

```yaml
# my-marketing-spec.yaml
project:
  name: "AwesomeApp"
  tagline: "Ship faster with AI"
  brand_voice: "Technical"
  website: "https://awesomeapp.com"
  target_audience:
    - "Developers"
    - "DevOps Engineers"
  value_propositions:
    - "10x faster deployment"
    - "AI-powered automation"

plans:
  - id: "q4-2025-growth"
    name: "Q4 2025 Growth Plan"
    project_id: "awesomeapp"
    period:
      start_date: "2025-10-01"
      end_date: "2025-12-31"
      duration_weeks: 13
    objectives:
      - "Increase brand awareness by 50%"
      - "Drive 10,000 new signups"
      - "Achieve $100K revenue"
    budget:
      total: 5000
      currency: "USD"
      allocation:
        content_creation: 2000
        paid_promotion: 2500
        tools: 300
        contingency: 200
    kpis:
      - name: "Brand Awareness"
        target: 50000
        unit: "impressions"
        measurement: "Social media + website"
        priority: "P0"
    status: "draft"
    created_at: "2025-11-15T10:00:00Z"
    updated_at: "2025-11-15T10:00:00Z"

campaigns:
  - id: "q4-awareness-launch"
    name: "Product Launch Campaign"
    goal: "awareness"
    plan_id: "q4-2025-growth"  # REQUIRED in v2.0.0
    project_id: "awesomeapp"
    target_audience: ["Developers"]
    budget: 2000
    start_date: "2025-10-01"
    end_date: "2025-10-21"
    channels: ["twitter", "dev-to", "reddit"]
    expected_kpis:
      impressions: 30000
      engagement_rate: 0.03
    status: "draft"
```

See [`examples/`](./examples/) for complete examples.

---

## 🏗️ Project Structure

```
marketing-spec-kit/
├── README.md                   # This file
├── CHANGELOG.md                # Version history
├── AGENTS.md                   # AI Agent guide (v2.0.0 workflow)
├── pyproject.toml              # Python project config
│
├── memory/
│   └── constitution.md         # Core principles (v1.3.0)
│
├── specs/
│   ├── domain/
│   │   └── 001-marketing-operations-spec/
│   │       ├── spec.md         # Domain specification (v2.0.0)
│   │       └── workflow-redesign.md
│   └── toolkit/
│       └── 001-marketing-spec-kit-implementation/
│           └── spec.md         # Toolkit specification
│
├── changes/
│   └── 2025-11-15-add-workflow-system/  # v2.0.0 evolution
│       ├── proposal.md
│       ├── tasks.md
│       ├── impact.md
│       └── specs/spec-delta.md
│
├── examples/
│   ├── metaspec-marketing.yaml        # Complete v2.0.0 example
│   └── metaspec-marketing-plan.md     # Plan documentation
│
├── templates/
│   ├── entity_templates/       # Init templates (minimal/default/full)
│   └── custom/
│       └── commands/           # 22 Slash Command definitions
│
└── src/marketing_spec_kit/
    ├── __init__.py             # Package exports (v2.0.0)
    ├── models.py               # 9 entities + 11 nested models
    ├── parser.py               # YAML/JSON parser
    ├── validator.py            # 45 validation rules
    ├── cli.py                  # CLI commands
    └── exceptions.py           # Custom exceptions
```

---

## 🆚 v2.0.0 vs v1.0.0

| Feature | v1.0.0 | v2.0.0 | Change |
|---------|--------|--------|--------|
| **Entities** | 7 | 9 | +2 (Plan, Analytics) |
| **Slash Commands** | 13 | 22 | +9 |
| **Validation Rules** | 42 | 45 | +3 |
| **Workflow Phases** | ❌ None | ✅ 5 phases | NEW |
| **Strategic Planning** | ❌ | ✅ Plan entity | NEW |
| **Performance Analytics** | ❌ | ✅ Analytics entity | NEW |
| **AI Campaign Design** | ❌ | ✅ campaign.design | NEW |
| **Content Calendar** | ❌ | ✅ content.plan | NEW |

**Breaking Changes**:
- `Campaign.plan_id` is now **REQUIRED** (was not present in v1.x)
- All campaigns must belong to a MarketingPlan

See [MIGRATION.md](./docs/MIGRATION.md) for upgrade guide.

---

## 📚 Documentation

- **[AGENTS.md](./AGENTS.md)** - Complete AI Agent workflow guide
- **[CHANGELOG.md](./CHANGELOG.md)** - Version history and changes
- **[memory/constitution.md](./memory/constitution.md)** - Core principles (v1.3.0)
- **[specs/domain/](./specs/domain/)** - Domain specification (v2.0.0)
- **[changes/](./changes/)** - Evolution proposals

---

## 🤝 Contributing

This project follows **Spec-Driven Development** using [MetaSpec](https://github.com/yourusername/MetaSpec):

1. **Specify First**: Define changes in `specs/` before coding
2. **Validate Early**: Run validation before implementation
3. **Document Changes**: Use Evolution Proposals for breaking changes
4. **Test Thoroughly**: Validate against all 45 rules

See [`.metaspec/README.md`](./.metaspec/README.md) for development guide.

---

## 🔍 Use Cases

### For Marketing Teams
- ✅ Standardize marketing operations across campaigns
- ✅ Ensure brand consistency with validated templates
- ✅ Track performance with built-in analytics

### For AI Agents
- ✅ Structured access to marketing context via 22 Slash Commands
- ✅ Generate on-brand content with brand guidelines
- ✅ Automate campaign execution and scheduling

### For Developers
- ✅ Integrate marketing data into apps via validated specs
- ✅ Build marketing automation tools on top of spec-kit
- ✅ Extend with custom entities and validation rules

---

## 📝 License

MIT License - see [LICENSE](./LICENSE) for details.

---

## 🙏 Acknowledgments

Built with:
- **[MetaSpec](https://github.com/yourusername/MetaSpec)** - Spec-Driven Development framework
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Data validation
- **[Typer](https://typer.tiangolo.com/)** - CLI framework
- **[Rich](https://rich.readthedocs.io/)** - Terminal formatting

---

**Generated by**: MetaSpec 0.6.2  
**Version**: 2.0.0  
**Release Date**: 2025-11-15  

For questions or issues, please [open an issue](https://github.com/yourusername/marketing-spec-kit/issues).
