---
name: marketspec.analyze
description: Check consistency across specification documents
layer: sdm
status: implemented
type: quality_gate
category: Quality Gates
source: Adapted from metaspec.sds.analyze
version: 0.3.0
---

# /marketspec.analyze 🟡 Quality Gate

**Purpose**: Check consistency across all planning documents before generating the final specification.

**Category**: Quality Gates (Recommended for QA)  
**Timing**: BEFORE create  
**Adapted from**: `metaspec.sdd.analyze`

---

## Purpose

Ensure all planning documents are consistent and complete:
- Verify objective alignment across documents
- Check budget consistency
- Validate timeline coherence
- Ensure complete coverage (no gaps)
- Identify conflicts or contradictions
- Verify all entity references

This is a **Quality Gate** - run before `/marketspec.create` to catch issues early.

---

## Command Usage

```
/marketspec.analyze
/marketspec.analyze --fix-suggestions
```

**Examples**:
```
/marketspec.analyze
/marketspec.analyze --fix-suggestions  # Include auto-fix recommendations
```

---

## Prerequisites

- **Required**: Draft specification from `/marketspec.specify`
- **Required**: Marketing plan from `/marketspec.plan`
- **Required**: Tasks from `/marketspec.tasks`
- **Recommended**: Clarifications from `/marketspec.clarify`
- **Optional**: Constitution from `/marketspec.constitution`

---

## Execution Steps

### Step 1: Load All Planning Documents

Read all available documents:

```yaml
documents_to_load:
  required:
    - specs/{sequence}-{name}/spec.md         # Draft specification
    - specs/{sequence}-{name}/plan.md         # Marketing plan
    - specs/{sequence}-{name}/tasks.md        # Task breakdown
  
  optional:
    - specs/{sequence}-{name}/clarifications.md
    - memory/constitution.md
```

Extract key data:
- Objectives and goals
- Budget allocations
- Timeline and milestones
- Target audiences
- Campaigns and channels
- Resources and team
- KPIs and metrics

### Step 2: Objective Alignment Check

Verify objectives are consistent across all documents:

```yaml
objective_alignment:
  discovery_objectives:
    - "Reach 500 GitHub stars"
    - "Acquire 1000 email subscribers"
    - "Generate 50K website visits"
  
  strategy_campaigns:
    - campaign: "dev-onboarding"
      supports_objectives: ["GitHub stars", "email subscribers"]
      alignment: ✅ "Aligned"
    
    - campaign: "power-user-stories"
      supports_objectives: ["email subscribers", "website visits"]
      alignment: ✅ "Aligned"
  
  tasks_coverage:
    - objective: "Reach 500 GitHub stars"
      related_tasks: ["content-001", "dist-001", "engage-001"]
      coverage: ✅ "Covered"
    
    - objective: "Acquire 1000 email subscribers"
      related_tasks: ["content-002", "dist-003"]
      coverage: ⚠️ "Partially covered - no dedicated lead magnet task"
  
  issues_found:
    - issue: "Objective 'email subscribers' lacks dedicated conversion task"
      severity: "medium"
      recommendation: "Add task for creating lead magnet or email capture optimization"
```

### Step 3: Budget Consistency Check

Verify budget numbers match across documents:

```yaml
budget_consistency:
  discovery_budget: 10000
  
  strategy_budget:
    total: 10000
    allocation:
      content_creation: 4000
      paid_promotion: 3000
      tools: 1500
      community: 1000
      contingency: 500
    sum: 10000
    matches_discovery: ✅ true
  
  strategy_campaign_budgets:
    - campaign: "dev-onboarding"
      budget: 6000
    - campaign: "power-user-stories"
      budget: 4000
    total: 10000
    matches_strategy_total: ✅ true
  
  tasks_implied_costs:
    content_creation: 4000  # From task effort estimates
    paid_ads: 3000
    tools: 1500
    other: 1500
    total: 10000
    matches_strategy: ✅ true
  
  issues_found: []
  status: ✅ "All budget numbers consistent"
```

### Step 4: Timeline Coherence Check

Verify dates and timelines align:

```yaml
timeline_coherence:
  discovery_timeline:
    start: "2025-01-15"
    end: "2025-03-31"
    duration: 11 weeks
  
  strategy_timeline:
    start: "2025-01-15"
    end: "2025-03-31"
    duration: 11 weeks
    matches_discovery: ✅ true
  
  campaign_timelines:
    - campaign: "dev-onboarding"
      start: "2025-01-15"
      end: "2025-02-28"
      within_strategy_period: ✅ true
    
    - campaign: "power-user-stories"
      start: "2025-02-15"
      end: "2025-03-31"
      within_strategy_period: ✅ true
      overlap_with_campaign_1: "2 weeks"
  
  tasks_timeline:
    earliest_task: "2025-01-15" (setup-001)
    latest_task: "2025-03-31" (opt-011)
    within_strategy_period: ✅ true
  
  milestone_spacing:
    - milestone: "Campaign Launch"
      date: "2025-01-15"
      aligned_with: "Strategy start, Task start"
      status: ✅ "Aligned"
    
    - milestone: "Mid-Campaign Review"
      date: "2025-02-15"
      aligned_with: "Campaign 2 start"
      status: ✅ "Aligned"
    
    - milestone: "Campaign Completion"
      date: "2025-03-31"
      aligned_with: "Strategy end, Task end"
      status: ✅ "Aligned"
  
  issues_found: []
  status: ✅ "All timelines coherent"
```

### Step 5: Coverage Analysis

Check if strategy covers all discovery requirements:

```yaml
coverage_analysis:
  discovery_requirements:
    target_audiences:
      - "Senior Python/JS Developers"
      - "Technical Decision Makers"
    
    channels_mentioned:
      - "Blog"
      - "Twitter"
      - "Developer communities"
    
    content_types_needed:
      - "Technical tutorials"
      - "Case studies"
  
  strategy_coverage:
    target_audiences_addressed:
      - "Senior Python/JS Developers": ✅ "Covered by dev-onboarding"
      - "Technical Decision Makers": ✅ "Covered by power-user-stories"
    
    channels_defined:
      - "Blog": ✅ "dev-blog channel defined"
      - "Twitter": ✅ "dev-twitter channel defined"
      - "Developer communities": ⚠️ "Mentioned but no specific channel config"
    
    content_types_planned:
      - "Technical tutorials": ✅ "In content plan"
      - "Case studies": ✅ "In content plan"
  
  tasks_coverage:
    all_strategy_campaigns_have_tasks: ✅ true
    all_channels_have_setup_tasks: ⚠️ "github-discussions missing setup"
    all_content_types_have_creation_tasks: ✅ true
  
  gaps_identified:
    - gap: "Developer communities channel not fully specified"
      severity: "medium"
      recommendation: "Add github-discussions or reddit channel configuration"
    
    - gap: "No setup task for github-discussions"
      severity: "low"
      recommendation: "Add setup task or remove channel reference"
  
  coverage_score: "92%" (23/25 items covered)
```

### Step 6: Entity Reference Validation

Check all references between entities are valid:

```yaml
reference_validation:
  campaign_references:
    - campaign: "dev-onboarding"
      plan_id: "q1-2025-growth"
      plan_exists_in_strategy: ✅ true
      product_ids: ["metaspec-core"]
      products_exist: ✅ true
      channel_ids: ["dev-blog", "dev-twitter", "dev-to", "github-discussions"]
      channels_exist: ⚠️ "github-discussions not in strategy channels"
  
  task_references:
    - task: "dist-001"
      dependencies: ["content-001"]
      dependencies_exist: ✅ true
      assigned_to: "Content Manager"
      role_exists: ✅ true
  
  milestone_references:
    - milestone: "campaign-launch"
      campaign_ids: ["dev-onboarding"]
      campaigns_exist: ✅ true
  
  issues_found:
    - issue: "Campaign references undefined channel 'github-discussions'"
      location: "strategy → campaigns → dev-onboarding"
      severity: "medium"
      fix: "Add channel definition or remove reference"
```

### Step 7: KPI Consistency Check

Verify KPIs are defined consistently:

```yaml
kpi_consistency:
  discovery_kpis:
    - "GitHub Stars: 50 → 500"
    - "Email Subscribers: 100 → 1000"
    - "Website Traffic: 500 → 50000"
  
  strategy_kpis:
    - name: "GitHub Stars"
      baseline: 50
      target: 500
      matches_discovery: ✅ true
    
    - name: "Email Subscribers"
      baseline: 100
      target: 1000
      matches_discovery: ✅ true
    
    - name: "Website Traffic"
      baseline: 500
      target: 50000
      matches_discovery: ✅ true
  
  tasks_kpi_support:
    - kpi: "GitHub Stars"
      supporting_tasks: ["content-001", "dist-001", "engage-001"]
      adequate_support: ✅ true
    
    - kpi: "Email Subscribers"
      supporting_tasks: ["content-002"]
      adequate_support: ⚠️ "Only 1 task - may need more effort"
  
  measurement_readiness:
    - kpi: "GitHub Stars"
      tracking_defined: ✅ "GitHub API"
      tool_configured: ⚠️ "Not in tasks"
    
    - kpi: "Email Subscribers"
      tracking_defined: ✅ "ConvertKit"
      tool_configured: ✅ "Tool setup in tasks"
```

### Step 8: Resource Allocation Check

Verify team capacity is realistic:

```yaml
resource_allocation:
  strategy_team:
    - role: "Content Writer"
      allocated: "13.3 hrs/week"
    - role: "Designer"
      allocated: "8 hrs/week"
    - role: "Social Media Manager"
      allocated: "20 hrs/week"
    - role: "Marketing Lead"
      allocated: "10 hrs/week"
  
  tasks_workload:
    - role: "Content Writer"
      total_hours: 80
      weeks: 11
      hours_per_week: 7.3
      matches_strategy: ⚠️ "Strategy says 13.3, tasks only need 7.3"
    
    - role: "Social Media Manager"
      total_hours: 220
      weeks: 11
      hours_per_week: 20
      matches_strategy: ✅ true
  
  issues_found:
    - issue: "Content Writer allocated capacity exceeds task requirements"
      severity: "low"
      recommendation: "Either add more content tasks or reduce allocation"
```

### Step 9: Generate Consistency Report

Create comprehensive consistency report:

```markdown
# Consistency Analysis Report

**Generated**: 2025-11-16  
**Documents Analyzed**: 4 (discovery, clarifications, strategy, tasks)  
**Overall Consistency**: 92/100 (A-)

---

## Executive Summary

Your planning documents are **highly consistent** with a few minor issues to address.

**Strengths**:
✅ Budget numbers perfectly aligned across all documents
✅ Timeline coherent with no conflicts
✅ All objectives have supporting campaigns
✅ 92% coverage of discovery requirements

**Issues to Address** (5):
1. ⚠️ Channel reference: "github-discussions" mentioned but not configured
2. ⚠️ Coverage gap: Email subscriber objective needs more task support
3. ⚠️ Resource mismatch: Content Writer capacity exceeds requirements
4. ℹ️ Tracking setup: GitHub Stars tracking not in task list
5. ℹ️ Minor: Some task dependencies could be optimized

---

## Detailed Analysis

### 1. Objective Alignment ✅ (100%)

All objectives from discovery are addressed in strategy and tasks.

### 2. Budget Consistency ✅ (100%)

Perfect alignment:
- Discovery: $10,000
- Strategy Total: $10,000
- Strategy Campaigns: $10,000
- Tasks Implied: $10,000

### 3. Timeline Coherence ✅ (100%)

All dates align perfectly across documents.

### 4. Coverage Analysis ⚠️ (92%)

**Gaps**:
- Developer communities channel mentioned but not fully specified
- Email subscriber tasks may be insufficient

**Recommendations**:
1. Add GitHub Discussions channel configuration to strategy
2. Add lead magnet creation task for email growth

### 5. Entity References ⚠️ (95%)

**Issues**:
- Campaign "dev-onboarding" references undefined channel "github-discussions"

**Fix**: Add channel definition or remove reference

### 6. KPI Consistency ✅ (95%)

Minor issue: GitHub Stars tracking setup not in task list

### 7. Resource Allocation ⚠️ (85%)

Content Writer capacity exceeds task requirements by 45%

---

## Recommended Fixes

### Critical (Before create)
- [ ] Add github-discussions channel to strategy OR remove from campaign
- [ ] Add task for GitHub Stars analytics setup

### Important (Should fix)
- [ ] Add 1-2 tasks for email lead magnet creation
- [ ] Adjust Content Writer allocation or add more content tasks

### Optional (Nice to have)
- [ ] Review task dependencies for optimization opportunities

---

## Consistency Score Breakdown

| Category | Score | Status |
|----------|-------|--------|
| Objective Alignment | 100% | ✅ Excellent |
| Budget Consistency | 100% | ✅ Excellent |
| Timeline Coherence | 100% | ✅ Excellent |
| Coverage Analysis | 92% | ⚠️ Good |
| Entity References | 95% | ⚠️ Good |
| KPI Consistency | 95% | ⚠️ Good |
| Resource Allocation | 85% | ⚠️ Acceptable |

**Overall**: 92/100 (A-)

---

## Readiness Assessment

✅ **Ready to proceed to /marketspec.create**

With minor fixes applied, you're ready to generate the specification.

Estimated fix time: 30 minutes

---

## Next Steps

1. Review and apply recommended fixes
2. Re-run `/marketspec.analyze` to verify (optional)
3. Proceed with `/marketspec.create`
```

**Output Location**: `consistency-report.md`

---

## Success Criteria

- ✅ All planning documents loaded and parsed
- ✅ Consistency checks completed across 7 categories
- ✅ Issues identified with severity levels
- ✅ Fix recommendations provided
- ✅ Overall consistency score calculated
- ✅ Clear readiness assessment

---

## Output

**Primary Output**: `specs/{sequence}-{name}/analysis.md`

**Example Structure**:
```
specs/
└── 001-q1-campaign-strategy/
    ├── spec.md                 ← Draft specification
    ├── plan.md                 ← Marketing plan
    ├── tasks.md                ← Task breakdown
    └── analysis.md             ← Consistency analysis (from this command) ⭐
```

---

## Error Handling

**Missing Required Document**:
```
❌ Error: Required document not found: specs/{sequence}-{name}/plan.md
→ Run /marketspec.plan first
```

**Parse Error**:
```
❌ Error: Cannot parse budget from plan document
→ Check Markdown syntax in plan document
```

**Too Many Issues**:
```
⚠️ Warning: 15 consistency issues found (threshold: 10)
→ Recommend fixing critical issues before proceeding to implement
```

---

## Example Interaction

```
User: /marketspec.analyze

AI: I'll analyze consistency across your planning documents. Loading documents...

📄 **Documents Loaded**:
✅ Draft Spec: specs/001-q1-campaign/spec.md
✅ Clarifications: specs/001-q1-campaign/clarifications.md
✅ Plan: specs/001-q1-campaign/plan.md
✅ Tasks: specs/001-q1-campaign/tasks.md

---

**Running consistency checks** (7 categories)...

✅ Objective Alignment: 100% (4/4 objectives covered)
✅ Budget Consistency: 100% (all numbers match)
✅ Timeline Coherence: 100% (no conflicts)
⚠️ Coverage Analysis: 92% (2 minor gaps)
⚠️ Entity References: 95% (1 undefined reference)
✅ KPI Consistency: 95% (1 minor tracking issue)
⚠️ Resource Allocation: 85% (capacity mismatch)

---

**Issues Found**: 5

**Critical** (0): None 🎉

**Important** (2):
1. ⚠️ Channel "github-discussions" referenced but not defined
2. ⚠️ Email subscriber objective may need more task support

**Minor** (3):
3. ℹ️ Content Writer capacity exceeds requirements
4. ℹ️ GitHub Stars tracking setup not in tasks
5. ℹ️ Some task dependencies could be optimized

---

**Overall Consistency**: 92/100 (A-)

✅ **Readiness**: Ready to proceed with minor fixes

📄 **Full Report**: specs/001-q1-campaign/analysis.md

**Recommended Actions**:
1. Add github-discussions channel OR remove reference (5 min)
2. Add task for lead magnet creation (10 min)
3. Add GitHub tracking setup task (5 min)

Total fix time: ~20 minutes

Would you like me to:
- Show detailed fix suggestions?
- Proceed to /marketspec.implement anyway?
- Wait for fixes and re-analyze?
```

---

## Notes

- **Purpose**: Quality gate, not optimization tool
- **Focus**: Consistency and completeness, not plan quality
- **Quick**: Should run in < 1 minute
- **Actionable**: Every issue has a clear fix recommendation
- **Threshold**: < 5 critical issues = ready to proceed
- **Re-runnable**: Can run multiple times as you fix issues

---

## Integration with Other Commands

**Position**: Quality Gate (BEFORE implement)

Feeds into:
- `/marketspec.implement` - Should only run after passing this check

References:
- `/marketspec.specify` - Source of objectives and requirements
- `/marketspec.clarify` - Refined requirements
- `/marketspec.plan` - Campaign and channel definitions
- `/marketspec.tasks` - Task breakdown

**Next Commands**:
- If pass (> 80%): `/marketspec.implement`
- If fail (< 80%): Fix issues and re-run

---

## See Also

- `/marketspec.tasks` - Previous step
- `/marketspec.implement` - Next step (final specification)
- `/marketspec.checklist` - Quality validation (companion command)
- Consistency examples in `examples/` directory
- MetaSpec SDS Analyze: `.metaspec/commands/metaspec.sds.analyze.md`
