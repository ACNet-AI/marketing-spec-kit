# Templates Directory

marketing-spec-kit provides a single command layer for marketing execution.

---

## 📂 Directory Structure

```
templates/
└── sdm/                    # Spec-Driven Marketing
    ├── commands/           # 8 SDM commands
    └── templates/          # YAML output templates
```

---

## 🚀 SDM Layer (Spec-Driven Marketing)

### Purpose
Execute marketing activities by creating structured YAML specifications.

### Commands (8)

| Command | Purpose | Adapted From |
|---------|---------|--------------|
| `/marketspec.constitution` | Define marketing execution principles | metaspec.sds.constitution |
| `/marketspec.discover` | Discover marketing needs | metaspec.sds.specify |
| `/marketspec.clarify` | Clarify marketing objectives | metaspec.sds.clarify |
| `/marketspec.strategy` | Plan marketing strategy | metaspec.sds.plan |
| `/marketspec.tasks` | Break down marketing tasks | metaspec.sds.tasks |
| `/marketspec.create` | Create marketing specification | metaspec.sds.implement |
| `/marketspec.checklist` | Generate quality checklist | metaspec.sds.checklist |
| `/marketspec.analyze` | Analyze specification consistency | metaspec.sds.analyze |

**Status**: 🚧 Commands are placeholder stubs, to be implemented.

### Quick Start Example

```bash
# Complete workflow
/marketspec.discover "Market MetaSpec to developers"
/marketspec.strategy
/marketspec.create
→ Output: marketing-spec.yaml
```

---

## 🔧 Advanced: Extending the Specification

### When do you need to extend?

The default specification includes 9 entities:
- Project, Product, MarketingPlan, Campaign, Channel, Tool, ContentTemplate, Milestone, Analytics

If you need domain-specific entities (e.g., FlashSale for e-commerce), you need to extend.

### How to extend?

**Use MetaSpec's SDS commands** (already available):

```bash
# Step 1: Define extension
/metaspec.sds.specify "Add E-commerce promotion entities"

# Step 2: Implement
/metaspec.sds.implement

# Step 3: Validate
/metaspec.sds.checklist
```

### Extension Examples

#### E-commerce Extension
Add entities: `FlashSale`, `Promotion`, `Coupon`, `AbandonedCart`

```yaml
FlashSale:
  extends: Campaign
  fields:
    - discount_percentage: float (10-90)
    - duration_hours: int (1-48)
    - max_quantity: int
```

#### B2B Extension
Add entities: `TargetAccount`, `LeadNurturing`, `Webinar`, `ABM`

```yaml
TargetAccount:
  fields:
    - company_name: string
    - industry: string
    - engagement_score: int (0-100)
```

#### SaaS Extension
Add entities: `FreeTrial`, `Onboarding`, `FeatureLaunch`, `Upsell`

```yaml
FreeTrial:
  extends: Campaign
  fields:
    - trial_days: int (7-30)
    - conversion_target: float
```

---

## 📚 Learn More

- [SDM Commands Guide](./sdm/README.md)
- [Domain Specification](../specs/domain/001-marketing-operations-spec/spec.md)
- [MetaSpec SDS Documentation](../.metaspec/README.md)
- [Architecture Decisions](../docs/internal/architecture-decisions-2025-11-16.md)
