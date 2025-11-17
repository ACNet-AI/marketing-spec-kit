# Implementation Tasks: 2025-11-15-add-workflow-system

**Proposal**: Add Complete Workflow System  
**Version**: v1.0.0 → v2.0.0  
**Estimated Total**: 7-8 days

---

## Phase 1: Update Domain Specification (1 day)

### Spec Updates

- [ ] **T001** [SPEC] Add "Workflow Specification" chapter to `specs/domain/001-marketing-operations-spec/spec.md`
  - Copy from `workflow-redesign.md`
  - Define 5 phases with entry/exit criteria
  - Map all commands to workflow phases
  - Estimated: 2 hours

- [ ] **T002** [SPEC] Add `MarketingPlan` entity definition
  - 17 fields with types, descriptions, examples
  - Relationships to Project and Campaign
  - Validation rules
  - Estimated: 1 hour

- [ ] **T003** [SPEC] Add `Analytics` entity definition
  - 8 fields with types, descriptions, examples
  - Relationships to Campaign and Plan
  - Estimated: 1 hour

- [ ] **T004** [SPEC] Modify `Campaign` entity definition
  - Add `plan_id` field (Required)
  - Add `expected_kpis` field (Optional)
  - Add `content_calendar` field (Optional)
  - Update examples
  - Estimated: 30 minutes

- [ ] **T005** [SPEC] Add 10 new validation rules
  - PLAN-01 to PLAN-05: Plan validation
  - CAMP-08 to CAMP-11: Campaign-Plan relationship
  - ANLY-01: Analytics validation
  - Document in "Validation Rules" section
  - Estimated: 1 hour

- [ ] **T006** [SPEC] Update "AI Agent Operations" section
  - Add 9 new commands with full specifications
  - Update 6 existing command specs (add campaign_id)
  - Update command count: 13 → 22
  - Estimated: 2 hours

- [ ] **T007** [SPEC] Update spec metadata
  - Version: 1.0.0 → 2.0.0
  - Entity count: 7 → 9
  - Operation count: 13 → 22
  - Validation rules: 25 → 35
  - Estimated: 15 minutes

---

## Phase 2: Update Toolkit Specification (0.5 days)

- [ ] **T008** [TOOLKIT-SPEC] Update `specs/toolkit/001-marketing-spec-kit-implementation/spec.md`
  - Update entity count
  - Update command count
  - Add Plan and Analytics to dependencies
  - Estimated: 1 hour

- [ ] **T009** [TOOLKIT-SPEC] Update `plan.md` architecture
  - Add Plan and Analytics to component design
  - Update validation strategy
  - Estimated: 1 hour

- [ ] **T010** [TOOLKIT-SPEC] Update `tasks.md`
  - Add tasks for Phase 6: Analytics
  - Add tasks for Phase 7: Workflow Support
  - Estimated: 1 hour

- [ ] **T011** [TOOLKIT-SPEC] Re-run `/metaspec.sdd.analyze` (optional)
  - Verify consistency after changes
  - Estimated: 30 minutes

---

## Phase 3: Implement Models (1 day)

### Pydantic Models

- [ ] **T012** [MODELS] Add `MarketingPlan` class to `models.py`
  - 17 Pydantic fields
  - Enums: PlanStatus
  - Validation: budget > 0, dates valid
  - Estimated: 2 hours

- [ ] **T013** [MODELS] Add `Analytics` class to `models.py`
  - 8 Pydantic fields
  - Enums: AnalyticsType, InsightType
  - Nested objects: metrics, vs_target
  - Estimated: 1.5 hours

- [ ] **T014** [MODELS] Add nested classes
  - `PlanBudget` (allocation breakdown)
  - `PlanKPI` (KPI definition)
  - `TargetAudience` (audience segment)
  - `Strategy` (strategy definition)
  - `AnalyticsInsight` (insight object)
  - `Optimization` (optimization suggestion)
  - Estimated: 1.5 hours

- [ ] **T015** [MODELS] Modify `Campaign` class
  - Add `plan_id: str` (required)
  - Add `expected_kpis: dict` (optional)
  - Add `content_calendar: dict` (optional)
  - Update validation
  - Estimated: 30 minutes

- [ ] **T016** [MODELS] Update `MarketingSpec` root class
  - Add `plans: List[MarketingPlan]`
  - Add `analytics: List[Analytics]` (optional)
  - Estimated: 15 minutes

- [ ] **T017** [MODELS] Add unit tests
  - Test Plan creation and validation
  - Test Analytics creation
  - Test Campaign with plan_id
  - Test invalid data handling
  - Estimated: 2 hours

---

## Phase 4: Implement Parser (0.5 days)

- [ ] **T018** [PARSER] Add Plan parsing in `parser.py`
  - Parse `plans:` section from YAML
  - Convert to `MarketingPlan` objects
  - Handle validation errors
  - Estimated: 1 hour

- [ ] **T019** [PARSER] Add Analytics parsing in `parser.py`
  - Parse `analytics:` section (optional)
  - Convert to `Analytics` objects
  - Estimated: 45 minutes

- [ ] **T020** [PARSER] Handle backward compatibility
  - Detect v1.x specs (Campaign without plan_id)
  - Provide helpful error message
  - Suggest migration command
  - Estimated: 1 hour

- [ ] **T021** [PARSER] Add parser tests
  - Test Plan parsing (valid/invalid)
  - Test Analytics parsing
  - Test backward compatibility error
  - Estimated: 1 hour

---

## Phase 5: Implement Validator (1.5 days)

### Validation Rules

- [ ] **T022** [VALIDATOR] Add Plan validation rules (5 rules)
  - PLAN-01: Budget > 0
  - PLAN-02: Budget allocation sums to total
  - PLAN-03: Valid date range
  - PLAN-04: Duration 4-52 weeks
  - PLAN-05: At least 1 objective
  - Estimated: 2 hours

- [ ] **T023** [VALIDATOR] Add Campaign-Plan validation rules (4 rules)
  - CAMP-08: plan_id references existing Plan
  - CAMP-09: Campaign budget ≤ Plan remaining budget
  - CAMP-10: Campaign start_date within Plan period
  - CAMP-11: Campaign end_date within Plan period
  - Estimated: 2 hours

- [ ] **T024** [VALIDATOR] Add Analytics validation (1 rule)
  - ANLY-01: Minimum 7 days of data
  - Estimated: 30 minutes

- [ ] **T025** [VALIDATOR] Update validator architecture
  - Support cross-entity validation (Campaign → Plan lookups)
  - Cache Plan data for performance
  - Estimated: 1.5 hours

- [ ] **T026** [VALIDATOR] Add validator tests
  - Test all 10 new validation rules
  - Test cross-entity validation
  - Test error messages
  - Estimated: 2 hours

---

## Phase 6: Implement Slash Commands (2 days)

### New Command Templates

- [ ] **T027** [COMMANDS] `/marketing.plan.create`
  - Template: `templates/custom/commands/marketing.plan.create.md`
  - Input: name, period, objectives, budget
  - Output: Created Plan ID + next steps
  - Estimated: 1.5 hours

- [ ] **T028** [COMMANDS] `/marketing.plan.validate`
  - Template: `templates/custom/commands/marketing.plan.validate.md`
  - Input: plan_id
  - Output: Validation report (errors/warnings/suggestions)
  - Estimated: 1 hour

- [ ] **T029** [COMMANDS] `/marketing.plan.get`
  - Template: `templates/custom/commands/marketing.plan.get.md`
  - Input: plan_id
  - Output: Full Plan JSON
  - Estimated: 45 minutes

- [ ] **T030** [COMMANDS] `/marketing.plan.analyze`
  - Template: `templates/custom/commands/marketing.plan.analyze.md`
  - Input: plan_id
  - Output: AI analysis (feasibility, strengths, risks, recommendations)
  - Estimated: 2 hours

- [ ] **T031** [COMMANDS] `/marketing.campaign.design`
  - Template: `templates/custom/commands/marketing.campaign.design.md`
  - Input: plan_id, num_campaigns, focus
  - Output: 3-5 Campaign suggestions with rationale
  - Estimated: 2.5 hours (complex AI logic)

- [ ] **T032** [COMMANDS] `/marketing.content.plan`
  - Template: `templates/custom/commands/marketing.content.plan.md`
  - Input: campaign_id, frequency, duration_weeks
  - Output: Content calendar (15-30 entries)
  - Estimated: 2 hours

- [ ] **T033** [COMMANDS] `/marketing.analytics.campaign`
  - Template: `templates/custom/commands/marketing.analytics.campaign.md`
  - Input: campaign_id, include_recommendations
  - Output: KPI report + insights + optimizations
  - Estimated: 2 hours

- [ ] **T034** [COMMANDS] `/marketing.analytics.plan`
  - Template: `templates/custom/commands/marketing.analytics.plan.md`
  - Input: plan_id, include_campaign_breakdown
  - Output: Plan-level KPI report + campaign contributions
  - Estimated: 2 hours

- [ ] **T035** [COMMANDS] `/marketing.optimize.suggest`
  - Template: `templates/custom/commands/marketing.optimize.suggest.md`
  - Input: campaign_id, focus
  - Output: Quick wins + strategic adjustments + risk mitigation
  - Estimated: 1.5 hours

### Modified Command Templates

- [ ] **T036** [COMMANDS] Update `/marketing.generate.post`
  - Add campaign_id parameter (required)
  - Add content_calendar_id parameter (optional)
  - Update logic to link to Campaign
  - Estimated: 30 minutes

- [ ] **T037** [COMMANDS] Update `/marketing.generate.article`
  - Same changes as T036
  - Estimated: 30 minutes

- [ ] **T038** [COMMANDS] Update `/marketing.generate.email`
  - Same changes as T036
  - Estimated: 30 minutes

- [ ] **T039** [COMMANDS] Update `/marketing.generate.landing_page`
  - Same changes as T036
  - Estimated: 30 minutes

- [ ] **T040** [COMMANDS] Update `/marketing.execute.schedule`
  - Add campaign_id parameter
  - Update content_calendar status
  - Estimated: 30 minutes

- [ ] **T041** [COMMANDS] Update `/marketing.execute.publish`
  - Add campaign_id parameter
  - Trigger Analytics data collection
  - Estimated: 30 minutes

---

## Phase 7: Update Tests (1 day)

### Integration Tests

- [ ] **T042** [TESTS] Add workflow integration test
  - Test: Plan → Campaign → Content → Analytics flow
  - File: `tests/integration/test_workflow.py`
  - Estimated: 2 hours

- [ ] **T043** [TESTS] Add Plan lifecycle tests
  - Create → Validate → Approve → Use
  - File: `tests/integration/test_plan_lifecycle.py`
  - Estimated: 1.5 hours

- [ ] **T044** [TESTS] Add Analytics tests
  - Campaign analytics generation
  - Plan analytics aggregation
  - File: `tests/integration/test_analytics.py`
  - Estimated: 1.5 hours

### Unit Tests

- [ ] **T045** [TESTS] Update Campaign tests
  - Test plan_id requirement
  - Test budget validation against Plan
  - File: `tests/unit/test_campaign.py`
  - Estimated: 1 hour

- [ ] **T046** [TESTS] Add command template tests
  - Test new command outputs
  - Mock AI responses
  - File: `tests/unit/test_commands.py`
  - Estimated: 2 hours

---

## Phase 8: Update Documentation (0.5 days)

### User Documentation

- [ ] **T047** [DOCS] Update README.md
  - Add workflow diagram (ASCII art)
  - Update entity count (7 → 9)
  - Update command count (13 → 22)
  - Add "Getting Started with Workflow" section
  - Estimated: 1.5 hours

- [ ] **T048** [DOCS] Update AGENTS.md
  - Document 9 new commands
  - Update 6 modified commands
  - Add workflow examples
  - Estimated: 2 hours

- [ ] **T049** [DOCS] Create MIGRATION.md
  - Document v1 → v2 migration steps
  - Provide before/after examples
  - Include automated migration script usage
  - Estimated: 1 hour

- [ ] **T050** [DOCS] Update CHANGELOG.md
  - Add v2.0.0 section
  - List breaking changes
  - List new features
  - Credit contributors
  - Estimated: 30 minutes

### Example Files

- [ ] **T051** [EXAMPLES] Create Plan example
  - File: `examples/metaspec-plan-only.yaml`
  - Simple Plan with 2 campaigns
  - Estimated: 30 minutes

- [ ] **T052** [EXAMPLES] Update full example
  - File: `examples/metaspec-marketing.yaml`
  - Add Plan section
  - Link Campaigns to Plan
  - Add Analytics section (optional)
  - Estimated: 45 minutes

- [ ] **T053** [EXAMPLES] Add workflow tutorial
  - File: `examples/workflow-tutorial.md`
  - Step-by-step: Plan → Campaign → Content → Analytics
  - Show command usage
  - Estimated: 1 hour

---

## Phase 9: Migration Support (Optional, 0.5 days)

- [ ] **T054** [CLI] Add `migrate` command
  - Command: `marketing_spec_kit migrate v1-to-v2 <spec-file>`
  - Logic: Auto-generate Plan from existing Campaigns
  - Output: Updated spec file + migration report
  - Estimated: 2 hours

- [ ] **T055** [CLI] Add migration tests
  - Test v1 spec migration
  - Test edge cases (multiple campaigns, budget conflicts)
  - Estimated: 1 hour

---

## Summary

| Phase | Task Count | Estimated Time |
|-------|------------|----------------|
| Phase 1: Domain Spec | 7 | 1 day |
| Phase 2: Toolkit Spec | 4 | 0.5 days |
| Phase 3: Models | 6 | 1 day |
| Phase 4: Parser | 4 | 0.5 days |
| Phase 5: Validator | 5 | 1.5 days |
| Phase 6: Slash Commands | 15 | 2 days |
| Phase 7: Tests | 5 | 1 day |
| Phase 8: Documentation | 7 | 0.5 days |
| Phase 9: Migration (Optional) | 2 | 0.5 days |
| **TOTAL** | **55 tasks** | **8.5 days** |

### Dependencies

```
Phase 1 (Domain Spec)
  ↓
Phase 2 (Toolkit Spec)
  ↓
Phase 3 (Models) ← must complete before Phase 4, 5, 6
  ↓
Phase 4 (Parser) ← can parallel with Phase 5, 6
Phase 5 (Validator) ← can parallel with Phase 4, 6
Phase 6 (Commands) ← can parallel with Phase 4, 5
  ↓
Phase 7 (Tests) ← requires Phase 3, 4, 5, 6 complete
  ↓
Phase 8 (Documentation)
  ↓
Phase 9 (Migration) ← optional, can parallel with Phase 8
```

### Parallelization Opportunities

- **Day 1-2**: Phase 1 + Phase 2 (Spec updates)
- **Day 3**: Phase 3 (Models)
- **Day 4-5**: Phase 4, 5, 6 in parallel (Parser, Validator, Commands)
- **Day 6**: Phase 7 (Tests)
- **Day 7**: Phase 8 + 9 (Documentation + Migration)

**Optimized Schedule**: 7 days (vs 8.5 days sequential)

---

**Task Breakdown Author**: marketing-spec-kit team  
**Date**: 2025-11-15  
**Based on Proposal**: 2025-11-15-add-workflow-system

