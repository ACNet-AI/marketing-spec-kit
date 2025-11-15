# Change Proposal: Add Complete Workflow System

**ID**: 2025-11-15-add-workflow-system  
**Date**: 2025-11-15  
**Status**: Draft  
**Type**: Breaking Change (Architecture Redesign)

---

## Summary

Transform marketing-spec-kit from a "tool collection" to a "workflow system" by adding 5-phase workflow definition, Plan entity for strategic management, and 9 new AI-assisted commands for end-to-end marketing operations (planning → analytics).

---

## Motivation

### Why is this change needed?

**User feedback** (Internal review):
- Users don't know where to start with 13 isolated commands
- No way to manage overall marketing strategy (只有Campaign，没有Plan)
- No guidance on operation sequencing (应该先用哪个命令？)
- No performance tracking or optimization loop (做完就结束，无法持续改进)

**Design gap discovered**:
- ❌ **Current**: "API toolbox" - 13 commands with no workflow context
- ✅ **Should be**: "Workflow system" - Clear path from strategy to execution to analytics
- ✅ **Inspiration**: MetaSpec itself has perfect workflow design (SDS/SDD phases), but doesn't enforce this for domain specs

**Real-world requirement**:
- To promote MetaSpec, we need: Marketing Plan → Launch Campaign → Content Calendar → Publish → Track KPIs
- Current toolkit only supports middle steps (Campaign, Content generation)
- Missing: Strategic planning (Plan) + Performance analysis (Analytics)

---

## Proposed Changes

### Entity Changes

#### 1. **ADD** Entity: `MarketingPlan`

**Purpose**: Manage overall marketing strategy, objectives, budget, and timeline

**Fields** (17 core fields):
```yaml
MarketingPlan:
  id: string                    # Required
  name: string                  # Required
  project_id: string            # Required (link to Project)
  
  period:                       # Required
    start_date: string          # ISO 8601
    end_date: string            # ISO 8601
    duration_weeks: number
  
  objectives: array[string]     # Required (SMART goals)
  target_audience: array[object] # Required
    - segment: string
      description: string
      size_estimate: number
      priority: enum[high, medium, low]
  
  strategies: array[object]     # Required
    - name: string
      description: string
      rationale: string
      success_criteria: string
  
  budget:                       # Required
    total: number
    currency: string
    allocation: object
      content_creation: number
      paid_promotion: number
      tools: number
      contingency: number
  
  kpis: array[object]           # Required
    - name: string
      target: number
      unit: string
      measurement: string
      priority: enum[P0, P1, P2]
  
  campaign_ids: array[string]   # Optional (filled as campaigns created)
  status: enum[draft, approved, active, completed, archived]
  created_at: string
  updated_at: string
  
  approval:                     # Optional
    approved_by: string
    approved_at: string
    comments: string
```

**Relationships**:
```
Project (1) → MarketingPlan (N)
MarketingPlan (1) → Campaign (N)
MarketingPlan (1) → Analytics (N)
```

---

#### 2. **ADD** Entity: `Analytics`

**Purpose**: Track KPI performance at Campaign or Plan level

**Fields** (8 core fields):
```yaml
Analytics:
  id: string                    # Required
  type: enum[campaign, plan]    # Required
  entity_id: string             # Required (Campaign ID or Plan ID)
  
  period:                       # Required
    start_date: string
    end_date: string
  
  metrics: object               # Required (actual values)
    # Example: github_stars: 3500
  
  vs_target: object             # Required (comparison with target)
    # Example:
    # github_stars:
    #   target: 5000
    #   actual: 3500
    #   achievement: 70%
    #   status: "below_target"
  
  insights: array[object]       # Optional (AI-generated)
    - type: enum[success, concern, opportunity]
      description: string
      evidence: string
      recommendation: string
  
  optimizations: array[object]  # Optional (AI recommendations)
    - priority: enum[high, medium, low]
      action: string
      expected_impact: string
      effort: enum[low, medium, high]
  
  generated_at: string          # Required
```

**Relationships**:
```
Campaign (1) → Analytics (N)
MarketingPlan (1) → Analytics (N)
```

---

#### 3. **ADD** Sub-entity: `ContentCalendar` (embedded in Campaign)

**Purpose**: Plan content publishing schedule for a campaign

**Implementation**: Add to existing `Campaign` entity as optional field

```yaml
Campaign:
  # ... existing fields ...
  content_calendar:             # Optional
    entries: array[object]
      - date: string            # ISO 8601
        content_type: string
        channel_id: string
        title: string
        status: enum[planned, created, published]
```

---

#### 4. **MODIFY** Entity: `Campaign`

**Changes**:
- **ADD** field `plan_id: string` (Required) - Link to MarketingPlan
- **ADD** field `expected_kpis: object` (Optional) - Expected KPI values inherited from Plan
- **ADD** field `content_calendar` (Optional) - Content publishing schedule

**Rationale**: Campaigns must be linked to strategic Plans, not created in isolation

---

### Validation Changes

#### **ADD** Validation Rules (10 new rules)

**Plan Validation**:
1. **PLAN-01**: `Plan.budget.total > 0` - Budget must be positive
2. **PLAN-02**: `Plan.budget.allocation总和 = Plan.budget.total` - Budget allocation must sum to total
3. **PLAN-03**: `Plan.period.start_date < Plan.period.end_date` - Valid date range
4. **PLAN-04**: `Plan.period.duration_weeks >= 4 AND <= 52` - Reasonable planning horizon
5. **PLAN-05**: `Plan.objectives.length >= 1` - At least one objective required

**Campaign-Plan Relationship**:
6. **CAMP-08**: `Campaign.plan_id` must reference existing Plan
7. **CAMP-09**: `Campaign.budget <= Plan.remaining_budget` - Campaign budget within Plan budget
8. **CAMP-10**: `Campaign.start_date` within Plan period
9. **CAMP-11**: `Campaign.end_date` within Plan period

**Analytics Validation**:
10. **ANLY-01**: `Analytics.period.end_date >= Analytics.period.start_date + 7 days` - Minimum 1 week of data

---

### CLI Changes

**No CLI changes** - This proposal focuses on AI Agent operations (Slash Commands)

---

### Slash Command Changes

#### **ADD** Commands (9 new commands)

**Phase 1: Strategic Planning**
1. `/marketing.plan.create` - Create marketing plan
2. `/marketing.plan.validate` - Validate plan completeness
3. `/marketing.plan.get` - Retrieve plan details
4. `/marketing.plan.analyze` - AI analysis and suggestions

**Phase 2: Campaign Design**
5. `/marketing.campaign.design` - AI-generate campaign suggestions based on Plan

**Phase 3: Content Creation**
6. `/marketing.content.plan` - Generate content calendar for campaign

**Phase 5: Analytics & Optimization**
7. `/marketing.analytics.campaign` - Analyze campaign KPI performance
8. `/marketing.analytics.plan` - Analyze plan-level performance
9. `/marketing.optimize.suggest` - AI optimization recommendations

#### **MODIFY** Commands (6 existing commands)

**Changes to all generate/execute commands**:
- **ADD** parameter `campaign_id: string` (Required) - Link content to campaign
- **ADD** parameter `content_calendar_id: string` (Optional) - Link to calendar entry
- **Behavior**: Auto-update campaign's content_calendar status

**Affected commands**:
- `/marketing.generate.post`
- `/marketing.generate.article`
- `/marketing.generate.email`
- `/marketing.generate.landing_page`
- `/marketing.execute.schedule`
- `/marketing.execute.publish`

---

### Workflow Changes

#### **ADD** Workflow: 5-Phase Marketing Operations Workflow

**Phase 1: Strategic Planning**
- Purpose: Define marketing strategy and resource allocation
- Entry: Business goals defined, Project/Product specs ready
- Operations: `/marketing.plan.create`, `/marketing.plan.validate`, `/marketing.plan.analyze`
- Exit: Approved Plan with budget and KPIs
- Quality Gate: Plan status = "approved", KPIs defined

**Phase 2: Campaign Design**
- Purpose: Design campaigns to achieve Plan objectives
- Entry: Approved Plan exists
- Operations: `/marketing.campaign.design`, `/marketing.campaign.create`
- Exit: Campaigns linked to Plan, budget allocated
- Quality Gate: Campaign.budget ≤ Plan.remaining_budget

**Phase 3: Content Creation**
- Purpose: Generate marketing content for campaigns
- Entry: Campaign created, Channels configured
- Operations: `/marketing.content.plan`, `/marketing.generate.*`
- Exit: Content assets ready for publishing
- Quality Gate: Content passes brand consistency check

**Phase 4: Execution & Publishing**
- Purpose: Publish content to channels
- Entry: Content ready, publish date reached
- Operations: `/marketing.execute.schedule`, `/marketing.execute.publish`
- Exit: Content live on channels, data tracking active
- Quality Gate: All scheduled content published successfully

**Phase 5: Analytics & Optimization**
- Purpose: Measure performance and optimize
- Entry: Campaign running ≥1 week, data available
- Operations: `/marketing.analytics.campaign`, `/marketing.analytics.plan`, `/marketing.optimize.suggest`
- Exit: Analytics report, optimization decisions
- Decision: If KPI met → continue; if not → optimize and retry

**Workflow Visualization**:
```
Plan → Campaign → Content → Publish → Analytics
  ↑                                        ↓
  └─────── Optimize (if needed) ──────────┘
```

---

## Impact Analysis

### Breaking Changes

**Summary**: YES - Major breaking changes

**Affected Components**:

1. **Models** (High Impact):
   - ADD `MarketingPlan` model (new)
   - ADD `Analytics` model (new)
   - MODIFY `Campaign` model (+3 new fields)
   - Impact: Existing Campaign YAML specs need migration

2. **Parser** (Medium Impact):
   - ADD Plan parsing logic
   - ADD Analytics parsing logic
   - MODIFY Campaign parser to handle new fields
   - Impact: Must handle old Campaign specs without `plan_id`

3. **Validator** (High Impact):
   - ADD 10 new validation rules
   - MODIFY Campaign validation (must validate plan_id reference)
   - Impact: Old specs may fail new validation rules

4. **Slash Commands** (High Impact):
   - ADD 9 new command templates
   - MODIFY 6 existing command templates
   - Impact: AI agents need to learn new commands

5. **Tests** (High Impact):
   - ADD tests for 2 new entities
   - ADD tests for 9 new commands
   - MODIFY tests for 6 existing commands
   - Impact: ~40+ new test cases needed

### Migration Required

**YES** - Migration guide required

**For existing users**:

**Before** (v1.0.0 - Campaign without Plan):
```yaml
# metaspec-marketing.yaml
campaigns:
  - id: "camp-001"
    name: "Launch Campaign"
    goal: "awareness"
    budget: 1500
    start_date: "2025-11-15"
    end_date: "2025-12-15"
    channels: ["twitter", "blog"]
```

**After** (v2.0.0 - Campaign linked to Plan):
```yaml
# metaspec-marketing.yaml
plans:  # NEW!
  - id: "plan-001"
    name: "Q1 2025 Growth Plan"
    period:
      start_date: "2025-11-01"
      end_date: "2026-01-31"
      duration_weeks: 12
    objectives: ["Reach 10K GitHub stars"]
    budget:
      total: 5000
      currency: "USD"
      allocation:
        content_creation: 2000
        paid_promotion: 2500
        tools: 300
        contingency: 200
    kpis:
      - name: "github_stars"
        target: 10000
        unit: "stars"

campaigns:
  - id: "camp-001"
    name: "Launch Campaign"
    plan_id: "plan-001"  # NEW! Required
    goal: "awareness"
    budget: 1500
    start_date: "2025-11-15"
    end_date: "2025-12-15"
    channels: ["twitter", "blog"]
    expected_kpis:  # NEW! Optional
      github_stars: 5000
```

**Migration steps**:
1. Create a default Plan for each existing Campaign
2. Link Campaigns to Plans via `plan_id`
3. Optionally define KPIs and budget allocation
4. Run validator to check compliance

**Backward compatibility**: NO
- Old specs without `plan_id` will fail validation
- Parser can provide helpful error: "Campaign.plan_id is required in v2.0.0. Create a Plan first using /marketing.plan.create"

### Version Bump

**Proposed**: v1.0.0 → **v2.0.0** (MAJOR)

**Reasoning**:
- ✅ Breaking change: Campaign requires plan_id (breaks existing specs)
- ✅ Major feature: Complete workflow system redesign
- ✅ New entities: Plan, Analytics
- ✅ 9 new commands + 6 modified commands
- ⚠️ Not backward compatible with v1.x.x specs

**Semantic Versioning**:
- MAJOR bump: Breaking changes to entity schema
- NOT MINOR: Would be non-breaking feature addition
- NOT PATCH: Would be bug fix only

---

## Constitution Alignment

### Principles Affected

#### ✅ **Part II: Specification Design Principles**

1. **Entity Clarity** - ENHANCED
   - Plan and Analytics entities fully specified with 17 and 8 fields respectively
   - All relationships documented

2. **Validation Completeness** - ENHANCED
   - 10 new validation rules added
   - Cross-entity validation (Campaign → Plan budget check)

3. **Operation Semantics** - ENHANCED
   - 9 new commands with clear input/output/side-effects
   - 6 commands improved with campaign_id linkage

4. **Workflow Completeness** (NEW! Principle 7) - FULLY ALIGNED ⭐
   - 5-phase workflow defined
   - All commands mapped to workflow phases
   - Quality gates and decision points documented
   - This proposal was created BECAUSE we added this principle!

#### ✅ **Part III: Toolkit Implementation Principles**

1. **Entity-First Design** - ALIGNED
   - Start with Pydantic models for Plan and Analytics
   - Validator follows entity structure

2. **Three-Layer Validator** - ALIGNED
   - New rules fit into existing layers:
     - Structural: Plan.budget > 0
     - Semantic: Campaign.plan_id exists
     - Domain: Budget allocation sums to 100%

3. **AI-Agent Friendly** - ENHANCED
   - Workflow context helps AI guide users
   - AI-assisted commands: `/marketing.campaign.design`, `/marketing.optimize.suggest`

### Violations

**None** - This proposal strengthens constitutional compliance by implementing Principle 7 (Workflow Completeness)

---

## Implementation Plan

### Estimated Effort

**Total**: 7-8 days (1-1.5 weeks)

### Phases

**Phase 1: Update Domain Spec** (1 day)
- Update `specs/domain/001-marketing-operations-spec/spec.md`
- Add Workflow章节 (based on workflow-redesign.md)
- Add Plan and Analytics entities
- Add 10 validation rules
- Update command list (13 → 22)

**Phase 2: Update Toolkit Spec** (0.5 days)
- Update `specs/toolkit/001-marketing-spec-kit-implementation/spec.md`
- Reflect new entities and commands
- Update architecture for Analytics support

**Phase 3: Implement Models** (1 day)
- ADD `models.py`: MarketingPlan class (Pydantic)
- ADD `models.py`: Analytics class (Pydantic)
- MODIFY `models.py`: Campaign class (+3 fields)
- ADD tests for new models

**Phase 4: Implement Parser** (0.5 days)
- MODIFY `parser.py`: Parse Plan and Analytics sections
- Handle backward compatibility (old Campaign specs)

**Phase 5: Implement Validator** (1.5 days)
- ADD 10 new validation rules
- Cross-entity validation (Campaign → Plan references)
- ADD tests for validation rules

**Phase 6: Implement Slash Commands** (2 days)
- ADD 9 new command templates in `templates/custom/commands/`
- MODIFY 6 existing templates (add campaign_id parameter)
- ADD command documentation

**Phase 7: Update Tests** (1 day)
- ADD integration tests for workflow
- ADD tests for new commands
- UPDATE existing tests for modified commands

**Phase 8: Update Documentation** (0.5 days)
- UPDATE README.md with workflow diagram
- UPDATE AGENTS.md with new commands
- UPDATE CHANGELOG.md for v2.0.0
- ADD migration guide

---

## Risks

### Technical Risks

**Risk 1**: Complex cross-entity validation (Campaign → Plan budget check)
- **Mitigation**: Cache Plan data during validation pass, avoid N+1 queries

**Risk 2**: Backward compatibility handling for v1.x specs
- **Mitigation**: Parser detects old specs, provides helpful error message with migration guide

**Risk 3**: AI command quality (new `/marketing.campaign.design`, `/marketing.optimize.suggest`)
- **Mitigation**: Extensive prompt engineering, provide clear examples in templates

### User Impact

**Impact 1**: All existing v1.x specs break
- **Mitigation**: Provide automated migration script `marketing_spec_kit migrate v1-to-v2`

**Impact 2**: Learning curve for new workflow
- **Mitigation**: Update README with workflow diagram, add tutorial examples

**Impact 3**: More complex spec files (Plan + Campaign instead of just Campaign)
- **Mitigation**: Provide templates (`init --template=with-plan`), AI assistance

---

## Alternatives Considered

### Alternative 1: Add Plan as optional, keep Campaign independent

**Description**: Make `Campaign.plan_id` optional to maintain backward compatibility

**Pros**:
- ✅ Backward compatible
- ✅ Easier migration
- ✅ No breaking changes (MINOR bump, not MAJOR)

**Cons**:
- ❌ Defeats the purpose - users can still ignore workflow
- ❌ Half-baked solution - still a "toolbox" not a "system"
- ❌ No forcing function for strategic thinking

**Why rejected**: 
- Purpose of this change is to transform toolkit into a workflow system
- Optional Plan means users won't adopt it
- Better to make breaking change now (v2.0) than accumulate technical debt

---

### Alternative 2: Separate toolkit for workflow (marketing-workflow-kit)

**Description**: Keep marketing-spec-kit as-is, create new toolkit for workflow management

**Pros**:
- ✅ No breaking changes to existing toolkit
- ✅ Users can choose toolbox OR workflow approach
- ✅ Clean separation of concerns

**Cons**:
- ❌ Fragmented user experience (两个toolkit难以选择)
- ❌ Duplicated code (both parse Campaign, Channel, etc.)
- ❌ Confusing for new users (which toolkit to use?)
- ❌ Maintenance burden (2 toolkits to maintain)

**Why rejected**:
- Fragmentation is worse than migration cost
- MetaSpec itself doesn't have "metaspec-lite" and "metaspec-full"
- Single toolkit with clear workflow is better UX

---

### Alternative 3: Only add Analytics, skip Plan entity

**Description**: Add Analytics for KPI tracking, but don't add Plan (keep Campaign-centric)

**Pros**:
- ✅ Smaller change, easier to implement
- ✅ Addresses "no performance tracking" pain point
- ✅ Less breaking (only add, not restructure)

**Cons**:
- ❌ Doesn't solve "no strategic management" problem
- ❌ Still a toolbox, not a workflow system
- ❌ Analytics without Plan context is less useful
- ❌ Misses opportunity to align with MetaSpec's workflow philosophy

**Why rejected**:
- Band-aid solution, doesn't address root cause
- User feedback clearly indicates need for Plan-level management
- MetaSpec case study (promoting MetaSpec) requires Plan → Campaign → Analytics flow

---

## Approval Checklist

- [x] **Constitution compliant** - Implements Principle 7 (Workflow Completeness)
- [x] **Impact assessed** - Breaking changes documented, migration guide planned
- [x] **Migration path defined** - v1 → v2 migration steps specified
- [x] **Tests planned** - 40+ new test cases identified
- [x] **Documentation planned** - README, AGENTS.md, CHANGELOG, migration guide

### Review Status

- [ ] **Reviewed by**: [Name/Date]
- [ ] **Approved by**: [Name/Date]

**Current Status**: **Draft** (awaiting review)

---

## Next Steps

1. **Review this proposal**
   - Validate workflow design
   - Confirm entity schemas
   - Check implementation effort estimate

2. **Get approval**
   - Stakeholder sign-off
   - Constitution compliance verified

3. **Implement**
   - Run `/metaspec.evolution.apply 2025-11-15-add-workflow-system`
   - Follow 8-phase implementation plan
   - Target completion: 2025-11-22 (1 week)

4. **Release**
   - Update CHANGELOG.md for v2.0.0
   - Publish migration guide
   - Announce breaking changes

---

**Proposal Author**: marketing-spec-kit team  
**Date Created**: 2025-11-15  
**Last Updated**: 2025-11-15  
**Related Documents**:
- `specs/domain/001-marketing-operations-spec/workflow-redesign.md` (detailed design)
- `memory/constitution.md` (Part II, Principle 7)
- `docs/internal/metaspec-feedback.md` (MetaSpec framework feedback)

