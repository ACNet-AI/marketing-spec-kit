---
name: marketspec.checklist
description: Validate specification completeness and quality
layer: sdm
status: implemented
type: quality_gate
category: Quality Gates
source: Adapted from metaspec.sds.checklist
version: 0.3.0
---

# /marketspec.checklist 🟡 Quality Gate

**Purpose**: Generate a comprehensive quality checklist to validate the marketing specification against best practices and constitution requirements.

**Category**: Quality Gates (Recommended for QA)  
**Timing**: AFTER strategy  
**Adapted from**: `metaspec.sdd.checklist`

---

## 📖 Navigation Guide (Token Optimization)

**File Size**: 984 lines (~3445 tokens)  
**Recommended**: Read specific sections to save 70-90% tokens

| Section | Lines | Size | Usage |
|---------|-------|------|-------|
| 1. Command Overview | 1-97 | 97 lines | `read_file(target, offset=1, limit=97)` |
| 2. Execution Steps | 98-384 | 287 lines | `read_file(target, offset=98, limit=287)` |
| 3. Summary & Issues | 385-423 | 39 lines | `read_file(target, offset=385, limit=39)` |
| 4. Checklist Categories | 424-715 | 292 lines | `read_file(target, offset=424, limit=292)` |
| 5. Validation & Assessment | 716-769 | 54 lines | `read_file(target, offset=716, limit=54)` |
| 6. Action Items & Sign-off | 770-813 | 44 lines | `read_file(target, offset=770, limit=44)` |
| 7. Success Criteria & Examples | 814-984 | 171 lines | `read_file(target, offset=814, limit=171)` |

**💡 Typical Usage**:
```python
# Quick reference: Read overview only (97 lines)
read_file(target, offset=1, limit=97)

# Core logic: Read execution steps (287 lines)
read_file(target, offset=98, limit=287)

# Checklist items: Read all categories (292 lines)
read_file(target, offset=424, limit=292)

# Output format: Read validation and assessment (54 lines)
read_file(target, offset=716, limit=54)
```

**Token Savings**:
- Full file: 984 lines (~3445 tokens)
- Single section: 39-292 lines (~135-1020 tokens) → **70-90% savings** 🏆
- Core logic only: 287 lines (~1005 tokens) → **71% savings**

---

## Purpose

Ensure marketing specification quality through:
- Automated validation checks
- Manual review guidelines
- Best practice verification
- Constitution compliance
- Data integrity validation
- Completeness assessment

This command generates both automated checks and human review checklists.

---

## Command Usage

```
/marketspec.checklist
/marketspec.checklist --auto-only
/marketspec.checklist --output-format [markdown|yaml|json]
```

**Examples**:
```
/marketspec.checklist
/marketspec.checklist --auto-only  # Skip manual checklist
/marketspec.checklist --output-format yaml
```

---

## Prerequisites

- **Required**: Specification from `/marketspec.specify` or `/marketspec.implement`
- **Recommended**: Constitution from `/marketspec.constitution`
- **Optional**: Source documents for cross-validation

---

## Execution Steps

### Step 1: Load Specification

Read and parse `marketing-spec.yaml`:

```yaml
specification:
  path: "marketing-spec.yaml"
  size: "42 KB"
  lines: 1245
  entities:
    project: 1
    products: 2
    plans: 1
    campaigns: 2
    channels: 4
    tools: 5
    content_templates: 2
    milestones: 4
    analytics: 3
```

**Basic Checks**:
- ✅ File exists and readable
- ✅ Valid YAML syntax
- ✅ Contains required top-level keys
- ✅ Specification version declared

### Step 2: Run Automated Validation

Perform automated checks across 6 categories:

#### 2.1 Structure Validation

```yaml
structure_checks:
  - check: "specification_version field present"
    result: ✅ PASS
    value: "0.3.0"
  
  - check: "metadata section present"
    result: ✅ PASS
  
  - check: "project section present"
    result: ✅ PASS
  
  - check: "All entity arrays defined (even if empty)"
    result: ✅ PASS
    entities: ["products", "plans", "campaigns", "channels", "tools", "content_templates", "milestones", "analytics"]
  
  - check: "No undefined top-level keys"
    result: ✅ PASS
  
  - check: "Proper YAML indentation (2 spaces)"
    result: ✅ PASS

structure_score: 6/6 (100%)
```

#### 2.2 Required Fields Validation

```yaml
required_fields_checks:
  project:
    - field: "name"
      required: true
      present: ✅ true
      value: "MetaSpec"
    
    - field: "tagline"
      required: true
      present: ✅ true
      length: 45  # chars
    
    - field: "target_audience"
      required: true
      present: ✅ true
      count: 2  # segments
    
    - field: "value_propositions"
      required: true
      present: ✅ true
      count: 3  # propositions
  
  campaigns:
    - campaign: "dev-onboarding"
      required_fields:
        name: ✅ present
        goal: ✅ present
        target_audience: ✅ present
        channels: ✅ present
        budget: ✅ present
        start_date: ✅ present
        end_date: ✅ present
      missing: []
    
    - campaign: "power-user-stories"
      required_fields:
        [similar checks]
  
  plans:
    - plan: "q1-2025-growth"
      required_fields:
        name: ✅ present
        objectives: ✅ present (4 items)
        strategies: ✅ present (2 items)
        budget: ✅ present
        kpis: ✅ present (8 items)
      missing: []

required_fields_score: 45/45 (100%)
```

#### 2.3 Data Type Validation

```yaml
data_type_checks:
  - field: "plans[0].budget.total"
    expected_type: "number"
    actual_type: "number"
    value: 10000
    result: ✅ PASS
  
  - field: "campaigns[0].start_date"
    expected_type: "date (ISO 8601)"
    actual_type: "string"
    value: "2025-01-15"
    format: ✅ valid
    result: ✅ PASS
  
  - field: "channels[0].publishing_schedule.frequency"
    expected_type: "string"
    actual_type: "string"
    value: "2 posts per week"
    result: ✅ PASS
  
  - field: "tools[0].cost"
    expected_type: "number"
    actual_type: "number"
    value: 0
    result: ✅ PASS
  
  - field: "project.target_audience"
    expected_type: "array"
    actual_type: "array"
    length: 2
    result: ✅ PASS

data_type_score: 52/52 (100%)
```

#### 2.4 Reference Integrity Validation

```yaml
reference_checks:
  campaign_to_plan:
    - campaign: "dev-onboarding"
      plan_id: "q1-2025-growth"
      plan_exists: ✅ true
    
    - campaign: "power-user-stories"
      plan_id: "q1-2025-growth"
      plan_exists: ✅ true
  
  campaign_to_channels:
    - campaign: "dev-onboarding"
      channel_ids: ["dev-blog", "dev-twitter", "dev-to", "github-discussions"]
      all_exist: ✅ true
      valid: ["dev-blog", "dev-twitter", "dev-to"]
      invalid: ⚠️ ["github-discussions"]  # Not defined in channels
  
  campaign_to_products:
    - campaign: "dev-onboarding"
      product_ids: ["metaspec-core"]
      all_exist: ✅ true
  
  plan_to_campaigns:
    - plan: "q1-2025-growth"
      campaign_ids: ["dev-onboarding", "power-user-stories"]
      all_exist: ✅ true
  
  analytics_to_tools:
    - analytics: "website-analytics"
      tool_id: "google-analytics"
      tool_exists: ✅ true

reference_score: 14/15 (93%)
issues:
  - ⚠️ Campaign "dev-onboarding" references undefined channel "github-discussions"
```

#### 2.5 Business Logic Validation

```yaml
business_logic_checks:
  budget_consistency:
    - plan: "q1-2025-growth"
      total_budget: 10000
      allocation_sum: 10000
      difference: 0
      result: ✅ PASS
  
  date_consistency:
    - campaign: "dev-onboarding"
      start_date: "2025-01-15"
      end_date: "2025-02-28"
      plan_start: "2025-01-15"
      plan_end: "2025-03-31"
      within_plan: ✅ true
      duration_days: 44
      result: ✅ PASS
  
  kpi_targets:
    - kpi: "GitHub Stars"
      baseline: 50
      target: 500
      growth_factor: 10x
      realistic: ⚠️ "Ambitious (review if achievable)"
    
    - kpi: "Email Subscribers"
      baseline: 100
      target: 1000
      growth_factor: 10x
      realistic: ⚠️ "Ambitious (review if achievable)"
  
  channel_coverage:
    - campaign: "dev-onboarding"
      channels: 4
      content_types: 4
      coverage: ✅ "Good diversity"
  
  team_capacity:
    - role: "Content Writer"
      weekly_hours: 13.3
      capacity_percent: 66
      status: ✅ "Under capacity"
    
    - role: "Social Media Manager"
      weekly_hours: 20
      capacity_percent: 100
      status: ⚠️ "At full capacity"

business_logic_score: 16/18 (89%)
warnings:
  - ⚠️ KPI targets are 10x - verify if realistic
  - ⚠️ Social Media Manager at 100% capacity - consider backup
```

#### 2.6 Constitution Compliance (if available)

```yaml
constitution_checks:
  brand_voice:
    specified: "Professional"
    constitution: "Professional yet approachable"
    match: ✅ "Compatible"
  
  content_standards:
    - standard: "All claims backed by evidence"
      check: "Review blog post templates"
      status: ⚠️ "Manual review required"
    
    - standard: "Technical content reviewed by engineering"
      check: "Review process defined"
      status: ✅ "Defined in templates"
  
  workflow_constraints:
    - constraint: "Approval required for campaigns > $5K"
      campaigns_over_threshold: ["dev-onboarding ($6K)"]
      approval_documented: ⚠️ "Not in spec (manual process)"

constitution_score: 4/6 (67%)
notes:
  - Need manual review for content standards
  - Document approval process for large campaigns
```

### Step 3: Generate Automated Validation Summary

Create summary of automated checks:

```markdown
# Automated Validation Results

**Overall Score**: 137/142 checks passed (96.5%)

## Summary by Category

| Category | Score | Status |
|----------|-------|--------|
| Structure | 6/6 (100%) | ✅ PASS |
| Required Fields | 45/45 (100%) | ✅ PASS |
| Data Types | 52/52 (100%) | ✅ PASS |
| Reference Integrity | 14/15 (93%) | ⚠️ WARNING |
| Business Logic | 16/18 (89%) | ⚠️ WARNING |
| Constitution Compliance | 4/6 (67%) | ⚠️ WARNING |

## Issues Found

### Errors (0)
None 🎉

### Warnings (5)
1. ⚠️ Campaign "dev-onboarding" references undefined channel "github-discussions"
2. ⚠️ KPI target "GitHub Stars" is 10x baseline - verify if realistic
3. ⚠️ KPI target "Email Subscribers" is 10x baseline - verify if realistic
4. ⚠️ Social Media Manager at 100% capacity - consider backup
5. ⚠️ Campaign approval process not documented for budgets > $5K

### Recommendations
- Add "github-discussions" to channels or remove from campaign
- Review KPI targets with historical data
- Plan for Social Media Manager backup or reduce workload
- Document approval workflow in constitution or notes
```

### Step 4: Generate Manual Review Checklist

Create human review checklist:

```markdown
# Manual Review Checklist

Use this checklist to verify aspects that require human judgment.

## Strategic Alignment (10 items)

### Objectives and Goals
- [ ] Marketing objectives align with business goals
- [ ] KPIs directly measure objective achievement
- [ ] Success metrics are SMART (Specific, Measurable, Achievable, Relevant, Time-bound)
- [ ] Target audience definition is specific enough to guide content

### Budget and Resources
- [ ] Budget allocation aligns with priorities
- [ ] Resource estimates are realistic
- [ ] Team capacity is adequate for planned activities
- [ ] Contingency budget is sufficient (5-10% recommended)

### Timeline
- [ ] Timeline accounts for dependencies
- [ ] Milestones are achievable given resources
- [ ] Buffer time included for delays

### Competitive Context
- [ ] Strategy differentiates from competitors
- [ ] Positioning is clear and defensible

## Content Quality (12 items)

### Messaging
- [ ] Brand voice is consistent across channels
- [ ] Key messages resonate with target audience
- [ ] Value propositions are clear and compelling
- [ ] Headlines and taglines are memorable

### Content Strategy
- [ ] Content mix balances education and promotion
- [ ] Content calendar is sustainable
- [ ] Content types match audience preferences
- [ ] Content templates ensure consistency

### Channel Strategy
- [ ] Channels match audience presence
- [ ] Publishing frequency is realistic
- [ ] Channel mix provides reach and engagement
- [ ] Cross-channel amplification planned

### Creative Quality
- [ ] Content examples are high quality
- [ ] Visual guidelines are clear
- [ ] Brand consistency maintained

## Execution Feasibility (10 items)

### Operations
- [ ] Workflow roles and responsibilities clear
- [ ] Approval processes defined
- [ ] Tools and platforms appropriate
- [ ] Integration requirements identified

### Risk Management
- [ ] Key risks identified
- [ ] Mitigation strategies are practical
- [ ] Backup plans for critical dependencies
- [ ] Escalation paths defined

### Measurement
- [ ] Analytics setup is complete
- [ ] Tracking covers all important metrics
- [ ] Reporting frequency matches decision needs
- [ ] Dashboard access for stakeholders

## Legal and Compliance (6 items)

### Regulatory
- [ ] GDPR/privacy compliance addressed
- [ ] CAN-SPAM compliance for email
- [ ] Accessibility considerations included
- [ ] Copyright and licensing clear

### Brand Protection
- [ ] Brand guidelines followed
- [ ] Approval workflow protects brand
- [ ] Crisis communication plan exists (if needed)

## Technical Implementation (8 items)

### Setup
- [ ] All tools and accounts created
- [ ] Analytics tracking installed and tested
- [ ] Email platform configured
- [ ] Social accounts set up

### Integration
- [ ] Tool integrations working
- [ ] Data flows validated
- [ ] Backup and recovery planned
- [ ] Security best practices followed

---

**Total Checklist Items**: 46  
**Recommended Completion**: Before campaign launch

**Review Process**:
1. Marketing Lead: Complete Strategic Alignment section
2. Content Manager: Complete Content Quality section
3. Operations Manager: Complete Execution Feasibility section
4. Legal/Compliance: Complete Legal and Compliance section
5. Technical Lead: Complete Technical Implementation section
```

### Step 5: Check Specification Completeness

Assess overall completeness:

```yaml
completeness_assessment:
  core_entities:
    project: ✅ complete (8/8 recommended fields)
    products: ✅ complete (2 products fully defined)
    plans: ✅ complete (1 plan, all sections populated)
    campaigns: ✅ complete (2 campaigns, all required fields)
    channels: ✅ complete (4 channels with strategies)
    tools: ✅ complete (5 tools documented)
    content_templates: ⚠️ limited (2 templates, consider more)
    milestones: ✅ complete (4 milestones covering timeline)
    analytics: ✅ complete (3 tracking setups)
  
  optional_enhancements:
    - ⚠️ Consider adding: Product personas
    - ⚠️ Consider adding: Competitor analysis
    - ⚠️ Consider adding: Customer journey maps
    - ⚠️ Consider adding: Content calendar details
    - ℹ️ Optional: Case study templates
    - ℹ️ Optional: Email campaign templates
  
  documentation:
    - ✅ Source documents referenced
    - ✅ Version and metadata complete
    - ✅ Authors documented
    - ⚠️ Change log could be added

completeness_score: 85%
recommendation: "Ready for execution with minor enhancements"
```

### Step 6: Benchmark Against Best Practices

Compare to industry standards:

```yaml
best_practices_comparison:
  campaign_structure:
    - practice: "Multiple campaigns for different funnel stages"
      status: ✅ "2 campaigns: awareness + consideration"
      grade: "A"
    
    - practice: "Clear campaign objectives"
      status: ✅ "All campaigns have defined goals"
      grade: "A"
  
  channel_strategy:
    - practice: "3-5 core channels"
      status: ✅ "4 channels defined"
      grade: "A"
    
    - practice: "Channel-specific strategies"
      status: ✅ "Each channel has strategy"
      grade: "A"
    
    - practice: "Cross-channel amplification"
      status: ⚠️ "Mentioned but not detailed"
      grade: "B"
  
  content_approach:
    - practice: "Content calendar planned"
      status: ⚠️ "Frequency defined, not calendar"
      grade: "B"
    
    - practice: "Content templates for consistency"
      status: ✅ "2 templates defined"
      grade: "A-"
    
    - practice: "SEO optimization guidelines"
      status: ✅ "Included in templates"
      grade: "A"
  
  measurement:
    - practice: "KPIs aligned with objectives"
      status: ✅ "8 KPIs match 4 objectives"
      grade: "A"
    
    - practice: "Both leading and lagging indicators"
      status: ✅ "Mix of activity and outcome metrics"
      grade: "A"
    
    - practice: "Weekly/monthly reporting cadence"
      status: ✅ "Weekly reporting defined"
      grade: "A"

overall_best_practices_grade: "A- (90%)"
notes:
  - "Strong foundation with industry best practices"
  - "Minor enhancements would elevate to A+"
```

### Step 7: Identify Risks and Gaps

Highlight potential issues:

```yaml
risk_assessment:
  high_priority:
    - risk: "Undefined channel 'github-discussions'"
      impact: "Medium"
      action: "Define channel or remove reference"
      urgency: "Before launch"
    
    - risk: "No backup for Social Media Manager"
      impact: "High"
      action: "Identify backup or reduce workload"
      urgency: "Week 1"
  
  medium_priority:
    - risk: "Ambitious 10x KPI targets"
      impact: "Medium"
      action: "Validate with historical data or adjust"
      urgency: "Before launch"
    
    - risk: "Limited content templates"
      impact: "Low"
      action: "Add more templates for efficiency"
      urgency: "Month 1"
  
  low_priority:
    - risk: "No documented approval process"
      impact: "Low"
      action: "Document in constitution"
      urgency: "Month 1"

gaps_identified:
  - gap: "No competitor analysis"
    recommendation: "Add competitive landscape section"
    priority: "Medium"
  
  - gap: "Missing customer personas"
    recommendation: "Create detailed personas"
    priority: "Low"
  
  - gap: "No crisis communication plan"
    recommendation: "Define escalation procedures"
    priority: "Low"
```

### Step 8: Generate Quality Score

Calculate overall quality score:

```yaml
quality_score:
  categories:
    structure: 100  # All structure checks passed
    completeness: 85  # Most entities complete
    data_quality: 96  # Very few data issues
    strategic_alignment: 90  # Strong alignment (manual review needed)
    execution_readiness: 85  # Ready with minor prep needed
    best_practices: 90  # Follows industry standards
  
  weighted_average: 91  # Overall score
  grade: "A-"
  
  rating_scale:
    90-100: "Excellent - Ready for execution"
    80-89: "Good - Minor improvements recommended"
    70-79: "Acceptable - Some work needed"
    60-69: "Needs Improvement - Significant gaps"
    0-59: "Incomplete - Major revision required"
  
  verdict: "Excellent - Ready for execution with minor fixes"
```

### Step 9: Generate Final Checklist Document

Create comprehensive checklist document:

```markdown
# Marketing Specification Quality Checklist

**Specification**: marketing-spec.yaml  
**Generated**: 2025-11-16  
**Version**: 1.0.0  
**Overall Quality Score**: 91/100 (A-)

---

## Executive Summary

Your marketing specification is **excellent** and ready for execution with minor fixes.

**Strengths**:
✅ Complete entity coverage
✅ Strong strategic alignment
✅ Comprehensive measurement framework
✅ Follows industry best practices
✅ Realistic budget and timeline

**Areas for Improvement**:
⚠️ Fix undefined channel reference
⚠️ Plan backup for at-capacity role
⚠️ Validate ambitious KPI targets

---

## Automated Validation Results

[Content from Step 3]

---

## Manual Review Checklist

[Content from Step 4]

---

## Completeness Assessment

[Content from Step 5]

---

## Best Practices Comparison

[Content from Step 6]

---

## Risk Assessment

[Content from Step 7]

---

## Quality Score

[Content from Step 8]

---

## Action Items

### Critical (Before Launch)
1. Add "github-discussions" to channels or remove from campaign
2. Validate 10x KPI targets with data or adjust
3. Identify Social Media Manager backup

### High Priority (Week 1)
4. Complete Technical Implementation checklist
5. Set up all analytics tracking
6. Document approval process

### Medium Priority (Month 1)
7. Add more content templates
8. Create detailed customer personas
9. Complete Strategic Alignment manual review

### Low Priority (As Needed)
10. Add competitor analysis
11. Define crisis communication plan
12. Create change log process

---

## Approval Sign-off

**Marketing Lead**: _______________ Date: _______  
**Product Manager**: _______________ Date: _______  
**Legal/Compliance**: _______________ Date: _______  

---

## Next Steps

1. Address critical action items
2. Complete manual review checklist
3. Run `/marketspec.analyze` for deeper analysis
4. Begin campaign execution
```

**Output Location**: `marketing-spec-checklist.md`

---

## Success Criteria

- ✅ All automated checks run successfully
- ✅ Quality score calculated (0-100)
- ✅ Manual review checklist generated
- ✅ Action items prioritized
- ✅ Risks and gaps identified
- ✅ Clear verdict (ready/not ready)

---

## Output

**Primary Output**: `specs/{sequence}-{name}/checklist.md`

**Example Structure**:
```
specs/
└── 001-q1-campaign-strategy/
    ├── spec.md                 ← Draft or final specification
    ├── plan.md                 ← Marketing plan
    └── checklist.md            ← Quality checklist (from this command) ⭐
```

---

## Error Handling

**Missing Specification**:
```
❌ Error: marketing-spec.yaml not found
→ Run /marketspec.create first
```

**Invalid YAML**:
```
❌ Error: Invalid YAML syntax at line 145
   Expected: proper indentation
   Found: mixed tabs and spaces
→ Fix YAML syntax before running checklist
```

**Missing Required Entity**:
```
🔴 Error: Required entity 'project' not found
→ Specification is incomplete, regenerate with /marketspec.create
```

---

## Example Interaction

```
User: /marketspec.checklist

AI: I'll generate a quality checklist for your marketing specification. Let me analyze marketing-spec.yaml...

📄 **Loading specification**:
✅ File found: marketing-spec.yaml (42 KB)
✅ Valid YAML syntax
✅ Specification version: 0.3.0

---

**Running automated validation** (6 categories)...

✅ Structure: 6/6 checks passed (100%)
✅ Required Fields: 45/45 checks passed (100%)
✅ Data Types: 52/52 checks passed (100%)
⚠️ Reference Integrity: 14/15 checks passed (93%)
⚠️ Business Logic: 16/18 checks passed (89%)
⚠️ Constitution Compliance: 4/6 checks passed (67%)

**Automated Score**: 137/142 checks passed (96.5%)

---

**Issues Found**:

🔴 **Errors**: 0  
⚠️ **Warnings**: 5

1. ⚠️ Campaign "dev-onboarding" references undefined channel "github-discussions"
2. ⚠️ KPI targets are 10x baseline - verify if realistic
3. ⚠️ Social Media Manager at 100% capacity
4. ⚠️ Content templates limited (only 2)
5. ⚠️ Approval process not documented

---

**Calculating quality score**...

📊 **Quality Breakdown**:
- Structure: 100/100 ✅
- Completeness: 85/100 ⚠️
- Data Quality: 96/100 ✅
- Strategic Alignment: 90/100 ✅
- Execution Readiness: 85/100 ⚠️
- Best Practices: 90/100 ✅

**Overall Quality Score**: 91/100 (A-)

🎉 **Verdict**: Excellent - Ready for execution with minor fixes

---

**Generating checklists**...

✅ Automated validation results compiled
✅ Manual review checklist generated (46 items)
✅ Completeness assessment complete
✅ Best practices comparison complete
✅ Risk assessment complete
✅ Action items prioritized (10 items)

📄 **Checklist created**: marketing-spec-checklist.md

---

**Summary**:

**Strengths**:
✅ Complete entity coverage
✅ Strong strategic foundation
✅ Comprehensive analytics setup
✅ Follows industry best practices

**Critical Actions** (before launch):
1. Fix undefined channel reference
2. Validate KPI targets
3. Plan Social Media Manager backup

**Recommendation**: Address 3 critical items, then ready to launch!

Would you like me to:
- Show detailed validation results?
- Run consistency analysis (`/marketspec.analyze`)?
- Export checklist in different format?
```

---

## Notes

- **Quality threshold**: 80+ score recommended for launch
- **Manual review essential**: Automated checks can't assess strategy quality
- **Regular reviews**: Run checklist after major updates
- **Team involvement**: Different roles should review relevant sections
- **Continuous improvement**: Use findings to refine specification
- **Documentation**: Keep checklist results for audit trail

---

## Integration with Other Commands

Feeds into:
- Decision making: Launch readiness assessment

References:
- `/marketspec.implement` - Validates the final specification
- `/marketspec.constitution` - Compliance validation
- `/marketspec.analyze` - Consistency analysis (companion command)

---

## See Also

- `/marketspec.implement` - Final specification generation
- `/marketspec.analyze` - Consistency analysis (companion command)
- Quality standards in `memory/constitution.md`
- MetaSpec SDS Checklist: `.metaspec/commands/metaspec.sds.checklist.md`
