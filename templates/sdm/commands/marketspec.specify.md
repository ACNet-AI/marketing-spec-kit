---
name: marketspec.specify
description: Define marketing strategy requirements and objectives
layer: sdm  
status: implemented
type: core
category: Core Flow
source: Adapted from metaspec.sds.specify
version: 0.4.0
---

# /marketspec.specify

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

The text after `/marketspec.specify` is the **marketing strategy description**.

**PURPOSE**: Define marketing strategy requirements - WHAT needs to be achieved.

- **Focus**: Business objectives, target audiences, success criteria
- **Output**: `specs/{sequence}-{name}/spec.md` (draft specification)
- **NOT**: Execution plans or campaign tactics (those come in `/marketspec.plan`)

Follow this execution flow:

### 1. Gather Marketing Context

Ask clarifying questions to understand:

**Product/Service Context**:
- What product/service is being marketed?
- What makes it unique? What problem does it solve?
- What is the current stage? (Pre-launch, launched, mature?)
- Website/repository URL?

**Business Objectives**:
- What are the primary goals? (Awareness, leads, conversions, retention?)
- What metrics define success?
- What are current baselines?
- What are target values and timeframes?

**Target Audience**:
- Who are the primary target audiences?
- What are their characteristics? (Demographics, psychographics, behaviors?)
- Where do they spend time online/offline?
- What are their pain points and motivations?

**Constraints**:
- What is the budget range?
- What is the timeline?
- What resources are available? (Team, tools, content?)
- What constraints exist? (Legal, brand guidelines, channel restrictions?)

### 2. Define Specification Structure

Create `specs/{sequence}-{name}/spec.md` with:

```markdown
---
specification_id: "{sequence}-{name}"
specification_version: "1.0.0"
specification_status: "draft"
domain: "marketing_strategy"
generated_by: "marketing-spec-kit"
generated_date: "{today}"
---

# Marketing Strategy Specification: {Name}

**Version**: 1.0.0  
**Status**: Draft  
**Created**: {today}

---

## Executive Summary

**Project**: {Product/Service name}

**Marketing Objective**: {Primary goal in one sentence}

**Target Outcome**: {Measurable success criteria}

**Timeline**: {Start} to {End}

---

## 1. Product/Service Overview

### 1.1 Product Description

{What is being marketed? Core value proposition?}

### 1.2 Unique Selling Points (USPs)

1. {USP 1}
2. {USP 2}
3. {USP 3}

### 1.3 Problem-Solution Fit

**Problem**: {What problem does the product solve?}

**Solution**: {How does the product solve it?}

**Differentiation**: {Why choose this over alternatives?}

### 1.4 Current State

- Stage: {Pre-launch / Launched / Mature}
- Current metrics: {Baseline data}
- Market position: {Where we are now}

---

## 2. Marketing Objectives

### 2.1 Primary Objectives

| Objective | Current | Target | Timeline | Priority |
|-----------|---------|--------|----------|----------|
| {Obj 1}   | {Base}  | {Goal} | {Time}   | High     |
| {Obj 2}   | {Base}  | {Goal} | {Time}   | Medium   |

### 2.2 Success Criteria

**Must-Have** (Critical):
- {Critical success metric 1}
- {Critical success metric 2}

**Nice-to-Have** (Secondary):
- {Secondary metric 1}
- {Secondary metric 2}

### 2.3 Key Performance Indicators (KPIs)

**Awareness KPIs**:
- Website traffic
- Social media reach
- Brand mentions

**Engagement KPIs**:
- Email open/click rates
- Social engagement rate
- Content interactions

**Conversion KPIs**:
- Signups / Downloads
- Trial activations
- Purchase conversions

---

## 3. Target Audience

### 3.1 Primary Audience

**Persona**: {Name, e.g., "Alex the Developer"}

**Demographics**:
- Age: {Range}
- Location: {Geographic focus}
- Occupation: {Job titles/roles}
- Experience: {Level}

**Psychographics**:
- Motivations: {What drives them?}
- Pain points: {What frustrates them?}
- Values: {What matters to them?}
- Goals: {What do they want to achieve?}

**Behavioral Characteristics**:
- Online presence: {Where do they hang out?}
- Content preferences: {What formats do they prefer?}
- Decision factors: {What influences their choices?}
- Buying journey: {How do they evaluate solutions?}

### 3.2 Secondary Audiences

{If applicable, describe secondary audience segments}

---

## 4. Market Context

### 4.1 Competitive Landscape

**Direct Competitors**:
- {Competitor 1}: {Their positioning}
- {Competitor 2}: {Their positioning}

**Our Differentiation**: {How we're different}

### 4.2 Market Trends

**Opportunities**:
- {Trend/opportunity 1}
- {Trend/opportunity 2}

**Threats**:
- {Challenge/threat 1}
- {Challenge/threat 2}

---

## 5. Resources & Constraints

### 5.1 Budget

**Total Budget**: ${Amount}

**Budget Allocation Principles**:
- {Allocation guideline 1}
- {Allocation guideline 2}

### 5.2 Timeline

**Campaign Duration**: {Start date} to {End date}

**Key Milestones**:
- {Milestone 1}: {Date}
- {Milestone 2}: {Date}

### 5.3 Team & Resources

**Available Resources**:
- Team: {Team composition}
- Tools: {Marketing tools available}
- Content: {Existing content assets}

**Resource Gaps**:
- {What's missing and needed}

### 5.4 Constraints

**Must Follow**:
- {Legal requirements (GDPR, CAN-SPAM, etc.)}
- {Brand guidelines}
- {Channel restrictions}

**Must Avoid**:
- {Prohibited practices}
- {Out-of-scope activities}

---

## 6. Success Measurement

### 6.1 Measurement Framework

**Data Sources**:
- {Source 1}: {What it tracks}
- {Source 2}: {What it tracks}

**Reporting Frequency**: {Weekly / Bi-weekly / Monthly}

**Review Checkpoints**:
- {Checkpoint 1}: {Date and purpose}
- {Checkpoint 2}: {Date and purpose}

### 6.2 Definition of Success

**Minimum Success**: {What constitutes basic success?}

**Target Success**: {What is the target outcome?}

**Exceptional Success**: {What would exceed expectations?}

---

## 7. Assumptions & Risks

### 7.1 Key Assumptions

1. {Assumption 1}
2. {Assumption 2}
3. {Assumption 3}

### 7.2 Risks & Mitigation

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| {Risk 1} | {H/M/L} | {H/M/L} | {How to mitigate} |
| {Risk 2} | {H/M/L} | {H/M/L} | {How to mitigate} |

---

## 8. Next Steps

This specification defines **WHAT** needs to be achieved. Next commands will define **HOW**:

1. `/marketspec.clarify` - Resolve any ambiguities in this specification
2. `/marketspec.plan` - Define detailed marketing strategy and tactics
3. `/marketspec.tasks` - Break down into actionable tasks

---

## Appendix

### A. References

- Constitution: `memory/constitution.md`
- Domain specification: `specs/domain/001-marketing-operations-spec/spec.md`

### B. Version History

- v1.0.0 ({today}): Initial specification
```

### 3. Validate Specification

Before saving, ensure:
- [ ] All required sections are complete
- [ ] Objectives are SMART (Specific, Measurable, Achievable, Relevant, Time-bound)
- [ ] Target audience is clearly defined
- [ ] Success criteria are measurable
- [ ] Constraints are documented
- [ ] Aligns with constitution principles

### 4. Save and Confirm

Write to `specs/{sequence}-{name}/spec.md` and inform user:

```
✓ Marketing strategy specification created: specs/{sequence}-{name}/spec.md

Next steps:
1. Review the specification
2. Run /marketspec.clarify to resolve any ambiguities
3. Run /marketspec.plan to define detailed strategy
```

## Notes

- This command defines **requirements**, not solutions
- Focus on **WHAT** to achieve, not **HOW** to do it
- The specification is a draft - it will be refined by subsequent commands
- All decisions should reference the constitution (`memory/constitution.md`)
