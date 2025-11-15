# Toolkit Spec Delta: 2025-11-15-add-workflow-system

**Base Version**: v1.0.0  
**Target Version**: v2.0.0  
**Type**: MAJOR (Breaking Changes)

---

## Domain Specification Changes

### File: `specs/domain/001-marketing-operations-spec/spec.md`

---

## Entity Changes

### **ADD** Entity: `MarketingPlan`

```yaml
MarketingPlan:
  # Identity
  - field: id
    type: string
    required: true
    description: Unique plan identifier
    example: "plan-2025-q1"

  - field: name
    type: string
    required: true
    description: Human-readable plan name
    example: "Q1 2025 Growth Plan"

  - field: project_id
    type: string
    required: true
    description: Reference to Project entity
    example: "proj-metaspec"

  # Time Period
  - field: period
    type: object
    required: true
    fields:
      - start_date: string (ISO 8601)
      - end_date: string (ISO 8601)
      - duration_weeks: number
    example:
      start_date: "2025-11-01"
      end_date: "2026-01-31"
      duration_weeks: 12

  # Strategy
  - field: objectives
    type: array[string]
    required: true
    description: SMART objectives for this plan
    example: ["Reach 10K GitHub stars", "Acquire 5K developers"]

  - field: target_audience
    type: array[object]
    required: true
    fields:
      - segment: string
      - description: string
      - size_estimate: number
      - priority: enum[high, medium, low]
    example:
      - segment: "AI Engineers"
        description: "Developers working with LLMs"
        size_estimate: 50000
        priority: "high"

  - field: strategies
    type: array[object]
    required: true
    fields:
      - name: string
      - description: string
      - rationale: string
      - success_criteria: string

  # Budget
  - field: budget
    type: object
    required: true
    fields:
      - total: number
      - currency: string
      - allocation: object
          content_creation: number
          paid_promotion: number
          tools: number
          contingency: number
    example:
      total: 5000
      currency: "USD"
      allocation:
        content_creation: 2000
        paid_promotion: 2500
        tools: 300
        contingency: 200

  # KPIs
  - field: kpis
    type: array[object]
    required: true
    fields:
      - name: string
      - target: number
      - unit: string
      - measurement: string
      - priority: enum[P0, P1, P2]
    example:
      - name: "github_stars"
        target: 10000
        unit: "stars"
        measurement: "GitHub API"
        priority: "P0"

  # Relationships
  - field: campaign_ids
    type: array[string]
    required: false
    description: List of campaigns under this plan
    example: ["camp-001", "camp-002"]

  # Status
  - field: status
    type: enum[draft, approved, active, completed, archived]
    required: true
    default: "draft"

  - field: created_at
    type: string (ISO 8601)
    required: true

  - field: updated_at
    type: string (ISO 8601)
    required: true

  # Approval (Optional)
  - field: approval
    type: object
    required: false
    fields:
      - approved_by: string
      - approved_at: string (ISO 8601)
      - comments: string
```

**Relationships**:
```
Project (1) ──→ MarketingPlan (N)
MarketingPlan (1) ──→ Campaign (N)
MarketingPlan (1) ──→ Analytics (N)
```

---

### **ADD** Entity: `Analytics`

```yaml
Analytics:
  - field: id
    type: string
    required: true
    description: Unique analytics report identifier
    example: "analytics-camp-001-2025-11"

  - field: type
    type: enum[campaign, plan]
    required: true
    description: Whether this is campaign or plan-level analytics

  - field: entity_id
    type: string
    required: true
    description: ID of Campaign or Plan being analyzed
    example: "camp-001"

  - field: period
    type: object
    required: true
    fields:
      - start_date: string (ISO 8601)
      - end_date: string (ISO 8601)

  - field: metrics
    type: object
    required: true
    description: Actual metric values achieved
    example:
      github_stars: 3500
      twitter_impressions: 85000
      signups: 2800

  - field: vs_target
    type: object
    required: true
    description: Comparison with target KPIs
    example:
      github_stars:
        target: 5000
        actual: 3500
        achievement: 70
        status: "below_target"

  - field: insights
    type: array[object]
    required: false
    description: AI-generated insights
    fields:
      - type: enum[success, concern, opportunity]
      - description: string
      - evidence: string
      - recommendation: string

  - field: optimizations
    type: array[object]
    required: false
    description: AI-generated optimization suggestions
    fields:
      - priority: enum[high, medium, low]
      - action: string
      - expected_impact: string
      - effort: enum[low, medium, high]

  - field: generated_at
    type: string (ISO 8601)
    required: true
```

**Relationships**:
```
Campaign (1) ──→ Analytics (N)
MarketingPlan (1) ──→ Analytics (N)
```

---

### **MODIFY** Entity: `Campaign`

**ADD** field `plan_id`:
```yaml
- field: plan_id
  type: string
  required: true  # ⚠️ BREAKING CHANGE (was not required in v1.0)
  description: Reference to MarketingPlan this campaign belongs to
  example: "plan-2025-q1"
```

**ADD** field `expected_kpis`:
```yaml
- field: expected_kpis
  type: object
  required: false
  description: Expected KPI values for this campaign (inherited from Plan)
  example:
    github_stars: 5000
    twitter_impressions: 100000
```

**ADD** field `content_calendar`:
```yaml
- field: content_calendar
  type: object
  required: false
  description: Content publishing schedule for this campaign
  fields:
    - entries: array[object]
        - date: string (ISO 8601)
        - content_type: string
        - channel_id: string
        - title: string
        - status: enum[planned, created, published]
  example:
    entries:
      - date: "2025-11-18"
        content_type: "announcement"
        channel_id: "twitter-main"
        title: "Announcing MetaSpec v0.6.0"
        status: "planned"
```

**Rationale**: 
- `plan_id` links Campaigns to strategic Plans (enables workflow)
- `expected_kpis` tracks campaign-level targets vs. Plan targets
- `content_calendar` manages content publishing schedule

**Migration Impact**: 
- ❌ **BREAKING**: All existing Campaigns without `plan_id` will FAIL validation
- Migration required: Auto-generate Plan from existing Campaigns

---

## Validation Changes

### **ADD** Validation Rules (10 new rules)

**Plan Validation (5 rules)**:

```yaml
PLAN-01:
  description: Plan budget must be positive
  constraint: Plan.budget.total > 0
  layer: Structural
  error_code: "E011"
  error_message: "Plan budget must be greater than 0. Got: {value}"

PLAN-02:
  description: Budget allocation must sum to total
  constraint: sum(Plan.budget.allocation.*) == Plan.budget.total
  layer: Semantic
  error_code: "E012"
  error_message: "Budget allocation ({allocation_sum}) must equal total budget ({total})"

PLAN-03:
  description: Plan period dates must be valid
  constraint: Plan.period.start_date < Plan.period.end_date
  layer: Structural
  error_code: "E013"
  error_message: "Plan end date must be after start date"

PLAN-04:
  description: Plan duration must be reasonable
  constraint: 4 <= Plan.period.duration_weeks <= 52
  layer: Domain
  error_code: "W001"  # Warning
  error_message: "Plan duration ({weeks} weeks) is outside typical range (4-52 weeks)"

PLAN-05:
  description: Plan must have at least one objective
  constraint: len(Plan.objectives) >= 1
  layer: Structural
  error_code: "E014"
  error_message: "Plan must have at least one objective"
```

**Campaign-Plan Relationship (4 rules)**:

```yaml
CAMP-08:
  description: Campaign must reference existing Plan
  constraint: Campaign.plan_id in [Plan.id for Plan in spec.plans]
  layer: Semantic
  error_code: "E015"
  error_message: "Campaign references non-existent Plan: {plan_id}"

CAMP-09:
  description: Campaign budget must not exceed Plan budget
  constraint: Campaign.budget <= Plan.remaining_budget
  layer: Domain
  error_code: "W002"  # Warning
  error_message: "Campaign budget ({campaign_budget}) exceeds Plan remaining budget ({remaining})"
  note: "Remaining = Plan.total - sum(other_campaigns.budget)"

CAMP-10:
  description: Campaign start date must be within Plan period
  constraint: Plan.period.start_date <= Campaign.start_date <= Plan.period.end_date
  layer: Semantic
  error_code: "E016"
  error_message: "Campaign start date ({start}) outside Plan period ({plan_start} to {plan_end})"

CAMP-11:
  description: Campaign end date must be within Plan period
  constraint: Plan.period.start_date <= Campaign.end_date <= Plan.period.end_date
  layer: Semantic
  error_code: "E017"
  error_message: "Campaign end date ({end}) outside Plan period ({plan_start} to {plan_end})"
```

**Analytics Validation (1 rule)**:

```yaml
ANLY-01:
  description: Analytics must have at least 7 days of data
  constraint: (Analytics.period.end_date - Analytics.period.start_date).days >= 7
  layer: Domain
  error_code: "W003"  # Warning
  error_message: "Analytics period ({days} days) is too short for meaningful analysis (min 7 days recommended)"
```

**Total Validation Rules**: 25 → **35** (+10, +40%)

---

## Slash Command Changes

### **ADD** Commands (9 new commands)

#### 1. `/marketing.plan.create`

```yaml
command: /marketing.plan.create
phase: Phase 1 (Strategic Planning)
purpose: Create new marketing plan

input:
  - name: string (required)
  - period_weeks: number (required)
  - objectives: array[string] (required)
  - budget_total: number (required)

output:
  - plan_id: string
  - status: "draft"
  - next_steps: array[string]

example:
  input:
    name: "Q1 2025 Growth Plan"
    period_weeks: 12
    objectives: ["Reach 10K stars"]
    budget_total: 5000
  output:
    plan_id: "plan-001"
    status: "draft"
    next_steps:
      - "Complete target_audience"
      - "Define strategies"
      - "Set KPIs"
```

#### 2. `/marketing.plan.validate`

```yaml
command: /marketing.plan.validate
phase: Phase 1 (Strategic Planning)
purpose: Validate plan completeness

input:
  - plan_id: string (required)

output:
  - score: number (0-100)
  - errors: array[object]
  - warnings: array[object]
  - suggestions: array[object]
```

#### 3. `/marketing.plan.get`

```yaml
command: /marketing.plan.get
phase: Phase 1 (Strategic Planning)
purpose: Retrieve plan details

input:
  - plan_id: string (required)

output:
  - plan: object (full MarketingPlan JSON)
```

#### 4. `/marketing.plan.analyze`

```yaml
command: /marketing.plan.analyze
phase: Phase 1 (Strategic Planning)
purpose: AI analysis and improvement suggestions

input:
  - plan_id: string (required)

output:
  - feasibility_score: number (0-100)
  - strengths: array[string]
  - risks: array[string]
  - recommendations: array[string]
```

#### 5. `/marketing.campaign.design`

```yaml
command: /marketing.campaign.design
phase: Phase 2 (Campaign Design)
purpose: AI-generate campaign suggestions based on Plan

input:
  - plan_id: string (required)
  - num_campaigns: number (default 3)
  - focus: enum[awareness, consideration, conversion] (optional)

output:
  - campaign_suggestions: array[object]
      - name: string
      - goal: enum
      - rationale: string
      - recommended_channels: array[string]
      - estimated_budget: number
      - duration_weeks: number
      - expected_kpis: object
```

#### 6. `/marketing.content.plan`

```yaml
command: /marketing.content.plan
phase: Phase 3 (Content Creation)
purpose: Generate content calendar for campaign

input:
  - campaign_id: string (required)
  - frequency: enum[daily, weekly, custom] (default "daily")
  - duration_weeks: number (optional, from Campaign)

output:
  - content_calendar: object
      - campaign_id: string
      - schedule: array[object]
          - date: string
          - content_type: string
          - channel: string
          - title: string
          - status: "planned"
      - summary: object
```

#### 7. `/marketing.analytics.campaign`

```yaml
command: /marketing.analytics.campaign
phase: Phase 5 (Analytics & Optimization)
purpose: Analyze campaign KPI performance

input:
  - campaign_id: string (required)
  - include_recommendations: boolean (default true)

output:
  - analytics_report: object
      - campaign_id: string
      - status: string
      - progress: number (%)
      - kpi_summary: object
      - insights: array[object]
      - optimizations: array[object]
```

#### 8. `/marketing.analytics.plan`

```yaml
command: /marketing.analytics.plan
phase: Phase 5 (Analytics & Optimization)
purpose: Analyze plan-level performance

input:
  - plan_id: string (required)
  - include_campaign_breakdown: boolean (default true)

output:
  - plan_analytics: object
      - plan_id: string
      - progress: number (%)
      - overall_kpis: object
      - campaign_breakdown: array[object]
      - budget_usage: object
      - strategic_insights: array[object]
```

#### 9. `/marketing.optimize.suggest`

```yaml
command: /marketing.optimize.suggest
phase: Phase 5 (Analytics & Optimization)
purpose: AI optimization recommendations

input:
  - campaign_id: string (required)
  - focus: enum[performance, budget, channels, content] (optional)

output:
  - optimization_suggestions: object
      - quick_wins: array[object]
      - strategic_adjustments: array[object]
      - risk_mitigation: array[object]
```

---

### **MODIFY** Commands (6 existing commands)

All `/marketing.generate.*` and `/marketing.execute.*` commands:

**ADD parameter** `campaign_id`:
```yaml
campaign_id:
  type: string
  required: true  # ⚠️ BREAKING CHANGE
  description: Link content to campaign for tracking
```

**ADD parameter** `content_calendar_id` (optional):
```yaml
content_calendar_id:
  type: string
  required: false
  description: Link to specific content calendar entry
```

**Affected commands**:
1. `/marketing.generate.post`
2. `/marketing.generate.article`
3. `/marketing.generate.email`
4. `/marketing.generate.landing_page`
5. `/marketing.execute.schedule`
6. `/marketing.execute.publish`

**Example** (before/after):

**Before** (v1.0.0):
```yaml
/marketing.generate.post:
  input:
    channel_id: "twitter-main"
    tone: "friendly"
```

**After** (v2.0.0):
```yaml
/marketing.generate.post:
  input:
    campaign_id: "camp-001"  # ⚠️ NEW REQUIRED
    channel_id: "twitter-main"
    tone: "friendly"
    content_calendar_id: "cal-entry-001"  # ⚠️ NEW OPTIONAL
```

**Total Command Count**: 13 → **22** (+9, +69%)

---

## Workflow Changes

### **ADD** Workflow Specification Chapter

**New Section**: "Workflow Specification" (add after "AI Agent Operations")

**Content**:

```markdown
## Workflow Specification

### Overview

Marketing operations follow a 5-phase workflow from strategic planning to performance analysis.

### Phase 1: Strategic Planning

**Purpose**: Define marketing strategy and resource allocation

**Entry Criteria**:
- Business goals defined
- Project and Product specifications ready

**Operations**:
- /marketing.plan.create - Create marketing plan
- /marketing.plan.validate - Verify plan completeness
- /marketing.plan.get - Retrieve plan details
- /marketing.plan.analyze - Get AI improvement suggestions

**Exit Criteria**:
- Plan status = "approved"
- All P0 KPIs defined
- Budget allocated 100%

**Quality Gate**: Plan must pass validation (score ≥ 80/100)

---

### Phase 2: Campaign Design

**Purpose**: Design campaigns to achieve Plan objectives

**Entry Criteria**:
- Approved Plan exists

**Operations**:
- /marketing.campaign.design - AI-generate campaign suggestions
- /marketing.campaign.create - Create campaign
- /marketing.campaign.get - Retrieve campaign details

**Exit Criteria**:
- At least 1 Campaign created
- Campaign.budget ≤ Plan.remaining_budget
- Campaign linked to Plan (plan_id set)

**Quality Gate**: Campaign dates within Plan period

---

### Phase 3: Content Creation

**Purpose**: Generate marketing content for campaigns

**Entry Criteria**:
- Campaign created
- Channels configured

**Operations**:
- /marketing.content.plan - Generate content calendar
- /marketing.generate.post - Create social media posts
- /marketing.generate.article - Create blog articles
- /marketing.generate.email - Create email campaigns
- /marketing.generate.landing_page - Create landing pages

**Exit Criteria**:
- At least 50% of planned content created
- All content passes brand consistency check

**Quality Gate**: Content matches Channel requirements

---

### Phase 4: Execution & Publishing

**Purpose**: Publish content to channels

**Entry Criteria**:
- Content created and reviewed
- Publish date reached

**Operations**:
- /marketing.execute.schedule - Schedule future publish
- /marketing.execute.publish - Publish immediately

**Exit Criteria**:
- All scheduled content published successfully
- Data tracking active

**Quality Gate**: No publishing errors

---

### Phase 5: Analytics & Optimization

**Purpose**: Measure performance and optimize

**Entry Criteria**:
- Campaign running ≥ 1 week
- KPI data available

**Operations**:
- /marketing.analytics.campaign - Analyze campaign KPIs
- /marketing.analytics.plan - Analyze plan-level performance
- /marketing.optimize.suggest - Get AI optimization recommendations

**Exit Criteria**:
- Analytics report generated
- Optimization decisions made

**Decision Point**:
- If KPI met → Continue to next campaign or next Plan
- If KPI below target → Apply optimizations, return to Phase 3 or 4

---

### Workflow Diagram

```
┌─────────────────────────────────────────────┐
│         Marketing Operations Workflow        │
└─────────────────────────────────────────────┘

Phase 1: Strategic Planning
   ↓ (create Plan)
   
Phase 2: Campaign Design
   ↓ (design Campaigns)
   
Phase 3: Content Creation
   ↓ (generate content)
   
Phase 4: Execution & Publishing
   ↓ (publish content)
   
Phase 5: Analytics & Optimization
   ↓ (track KPIs)
   
   Decision: KPI met?
      YES → Next Campaign or Next Plan
      NO  → Optimize → Back to Phase 3 or 4
   
   ↺ Loop continues
```
```

**Rationale**: 
- Provides clear user guidance
- Maps all operations to workflow phases
- Defines entry/exit criteria and quality gates
- Aligns with Constitution Part II, Principle 7 (Workflow Completeness)

---

## Metadata Changes

### Domain Spec Metadata

```yaml
# Before (v1.0.0)
specification_version: "1.0.0"
entity_count: 7
operation_count: 13
validation_rules: 25
error_codes: 13

# After (v2.0.0)
specification_version: "2.0.0"
entity_count: 9           # +2 (Plan, Analytics)
operation_count: 22       # +9 new commands
validation_rules: 35      # +10 new rules
error_codes: 16           # +3 (E011-E017, W001-W003)
```

---

## Summary of Changes

| Change Type | Count | Impact |
|-------------|-------|--------|
| **Entities Added** | 2 | MarketingPlan, Analytics |
| **Entities Modified** | 1 | Campaign (+3 fields) |
| **Validation Rules Added** | 10 | PLAN-01~05, CAMP-08~11, ANLY-01 |
| **Commands Added** | 9 | 4 plan + 1 campaign + 1 content + 3 analytics |
| **Commands Modified** | 6 | All generate + execute commands |
| **Workflow Phases Defined** | 5 | Strategic → Design → Content → Execute → Analytics |
| **Breaking Changes** | YES | Campaign.plan_id required, command signatures |

---

**Spec Delta Author**: marketing-spec-kit team  
**Date**: 2025-11-15  
**Base Version**: v1.0.0  
**Target Version**: v2.0.0  
**Proposal ID**: 2025-11-15-add-workflow-system

