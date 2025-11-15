# Slash Command: /marketing.plan.analyze

## Purpose

Analyze a marketing plan's strategic alignment, feasibility, and provide AI-generated recommendations.

## Command Usage

```
/marketing.plan.analyze <plan_id>
```

## Prerequisites

- Plan must exist in specification
- Project context should be available

## Execution Steps

### Step 1: Read Plan & Context

Load the plan and related entities (project, campaigns, etc.)

### Step 2: Perform Multi-Dimensional Analysis

#### 2.1 Strategic Alignment (Score: 0-10)

- Are objectives aligned with project's value propositions?
- Do strategies support the objectives?
- Are target audience segments consistent with project audience?

#### 2.2 Resource Feasibility (Score: 0-10)

- Is budget realistic for the objectives?
- Is budget allocation balanced?
- Is timeline achievable (4-52 weeks)?

#### 2.3 KPI Quality (Score: 0-10)

- Are KPIs SMART (Specific, Measurable, Achievable, Relevant, Time-bound)?
- Do KPIs have appropriate priorities?
- Are there at least 1-2 P0 (critical) KPIs?

#### 2.4 Execution Readiness (Score: 0-10)

- Are strategies actionable?
- Are success criteria clear?
- Is approval process defined (if needed)?

### Step 3: Generate Recommendations

Provide 3-5 actionable recommendations categorized by priority:

- **Critical (P0)**: Must address before approval
- **Important (P1)**: Should address for better outcomes
- **Nice-to-have (P2)**: Optional improvements

### Step 4: Output Structured Report

```markdown
# Plan Analysis Report: Q4 2025 Growth Plan

**Overall Score**: 8.5/10 ⭐
**Status**: Ready for approval with minor improvements

## Dimension Scores

| Dimension | Score | Status |
|-----------|-------|--------|
| Strategic Alignment | 9/10 | ✅ Excellent |
| Resource Feasibility | 8/10 | ✅ Good |
| KPI Quality | 9/10 | ✅ Excellent |
| Execution Readiness | 8/10 | ✅ Good |

## Strengths

1. **Clear Objectives**: 3 well-defined objectives aligned with project goals
2. **Balanced Budget**: Allocation matches priorities ($2500 for paid promotion)
3. **Strong KPIs**: P0 KPIs (Brand Awareness, Signups) directly measure objectives

## Areas for Improvement

### 🔴 Critical (P0)
- None

### 🟡 Important (P1)
1. **Increase Contingency Budget**: Current $200 (4%) is low for a 13-week plan
   - **Recommendation**: Increase to $500 (10%) by reducing paid promotion
   - **Impact**: Better risk management

2. **Add Mid-Point Milestones**: No checkpoints defined in 13-week period
   - **Recommendation**: Add week 7 review milestone
   - **Impact**: Earlier course correction if needed

### 🟢 Nice-to-have (P2)
1. **Target Audience Sizing**: 50K estimate seems rough
   - **Recommendation**: Conduct TAM/SAM/SOM analysis for precision
   - **Impact**: Better resource allocation

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Budget overrun | Medium | Medium | Increase contingency to 10% |
| Timeline slip | Low | High | Add mid-point checkpoints |
| Audience mismatch | Low | Medium | Validate with user research |

## Next Steps

1. Consider P1 recommendations
2. Create 2-3 campaigns under this plan
3. Schedule approval review

---

**Generated**: 2025-11-15 10:30:00 UTC
```

## Success Criteria

- Multi-dimensional analysis performed
- Clear strengths and improvements identified
- Actionable recommendations with priorities

## Example Interaction

```
User: /marketing.plan.analyze q4-2025-growth-plan

AI: Analyzing plan 'q4-2025-growth-plan'...

[Displays complete analysis report as shown above]
```

