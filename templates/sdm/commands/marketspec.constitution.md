---
name: marketspec.constitution
description: Define design principles and governance rules for marketing strategy specifications
layer: sdm
status: implemented
type: core
category: Core Flow
source: Adapted from metaspec.sds.constitution
version: 0.4.0
---

# /marketspec.constitution

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are creating or updating **Part II: Marketing Specification Design Principles** in `/memory/constitution.md`. This section defines guidelines for creating marketing strategy specifications.

Follow this execution flow:

### 1. Load existing constitution

- Read `/memory/constitution.md` if exists
- Locate `## Part II: Marketing Specification Design Principles` section
- Preserve other parts unchanged

### 2. Understand the marketing context

**Critical**: Before defining principles, understand the marketing environment:
- What products/services are being marketed?
- What are the business goals? (Awareness, leads, conversions?)
- What are the constraints? (Budget, timeline, resources?)
- What channels are available? (Social, email, content, paid?)

**Ask clarifying questions if unclear**:
- "What products or services will this marketing project promote?"
- "What are the primary marketing objectives?"
- "What budget and timeline constraints exist?"

### 3. Define Part II principles

Based on user input, establish these **marketing specification design principles**:

#### **I. Audience Clarity**
- Target audiences are precisely defined
- Personas include demographics, psychographics, pain points
- Audience needs and motivations documented
- Channel preferences identified

**Rationale**: Clear audience definitions enable focused, effective campaigns.

#### **II. Objective Measurability**
- All marketing objectives have measurable KPIs
- Success metrics defined upfront
- Baseline and target values specified
- Measurement methods documented

**Rationale**: Measurable objectives enable data-driven optimization.

#### **III. Channel Appropriateness**
- Channel selection justified by audience behavior
- Channel capabilities match content requirements
- Budget allocation aligns with channel ROI
- Channel mix addresses multiple touchpoints

**Rationale**: Right channels ensure message reaches the audience effectively.

#### **IV. Content Consistency**
- Brand voice and tone consistently applied
- Messaging aligned across channels
- Visual identity maintained
- Value propositions clearly communicated

**Rationale**: Consistent content builds brand recognition and trust.

#### **V. Budget Realism**
- Budget allocations are realistic and justified
- Contingency funds included
- ROI expectations documented
- Cost-benefit analysis performed

**Rationale**: Realistic budgets prevent mid-campaign resource issues.

#### **VI. Timeline Feasibility**
- Campaign timelines account for production time
- Dependencies and milestones identified
- Buffer time included for iterations
- Seasonal factors considered

**Rationale**: Feasible timelines prevent rushed execution and quality issues.

#### **VII. Review & Optimization**
- Review checkpoints defined
- Optimization criteria specified
- A/B testing methodology documented
- Feedback incorporation process defined

**Rationale**: Continuous optimization maximizes marketing effectiveness.

#### **VIII. Compliance & Ethics**
- Legal requirements documented (GDPR, CAN-SPAM, etc.)
- Ethical guidelines established
- Disclosure requirements specified
- Data privacy principles defined

**Rationale**: Compliance prevents legal issues and maintains brand reputation.

### 4. Add domain-specific constraints

Include marketing-specific constraints relevant to this project:

**Example constraints**:
- "All campaigns must comply with GDPR"
- "Brand voice: Professional but approachable"
- "No paid advertising on platforms with < 5% conversion rate"
- "All content must pass accessibility standards (WCAG AA)"
- "Influencer partnerships require 30-day advance approval"

### 5. Output format

Update `/memory/constitution.md` with this structure:

```markdown
# Marketing Project Constitution

## Part I: Project Principles
[User-defined project values and mission]

## Part II: Marketing Specification Design Principles

### Specification Quality Standards

#### I. Audience Clarity
[Details based on step 3]

#### II. Objective Measurability
[Details based on step 3]

[...continue with all 8 principles...]

### Domain-Specific Constraints

1. [Constraint from step 4]
2. [Constraint from step 4]
...

## Part III: Review & Evolution
[How this constitution will be reviewed and updated]
```

## Validation

Before finalizing, verify:
- [ ] All 8 principles are included
- [ ] Each principle has rationale
- [ ] Domain constraints are specific and actionable
- [ ] Document is clear and unambiguous
- [ ] Marketing terminology is used correctly

## Example Output

```markdown
# MetaSpec Marketing Constitution

## Part I: Project Principles

**Mission**: Establish MetaSpec as the leading specification toolkit in the developer tools ecosystem.

**Core Values**:
- Developer-first: All messaging speaks to developer needs
- Education-focused: Content educates, not just promotes
- Community-driven: Engage authentically with developer community

## Part II: Marketing Specification Design Principles

### I. Audience Clarity

**Target Audience**: Senior Python/JavaScript developers (5+ years experience) building developer tools or internal platforms.

**Persona**: Alex, 32, Senior Engineer
- Pain: Tired of building tools from scratch
- Goal: Reusable tool generation system
- Channels: Dev.to, Twitter, GitHub, HackerNews

**Rationale**: Clear audience definition enables focused content strategy.

### II. Objective Measurability

**Primary KPI**: GitHub stars (50 → 500 in 11 weeks)
**Secondary KPIs**:
- Website traffic: 500 → 50,000 visits/month
- Email subscribers: 100 → 1,000
- Community engagement: 0 → 50 active contributors

**Rationale**: Measurable objectives enable data-driven optimization.

[...continue with all principles...]

### Domain-Specific Constraints

1. All content must pass technical review by core team
2. No paid promotion until organic reach validated (>1000 monthly visits)
3. Community guidelines: No spam, no hard sells, education-first
4. Brand voice: Technical but accessible, authoritative but friendly
5. Content must be open-source friendly (CC BY-SA 4.0 licensing)

## Part III: Review & Evolution

This constitution will be reviewed:
- Weekly during active campaigns
- Quarterly for strategic alignment
- After significant market changes

Updates require consensus from marketing lead and product owner.
```

## Notes

- This command focuses on **specification design principles**, not campaign execution
- The constitution guides how to create good marketing strategy specifications
- It does NOT define specific campaigns (that's done in `/marketspec.specify` and `/marketspec.plan`)
- Review and optimize the constitution based on campaign learnings
