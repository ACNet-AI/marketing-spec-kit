---
name: marketspec.plan
description: Plan marketing strategy architecture
layer: sdm
status: implemented
type: core
category: Core Flow
source: Adapted from metaspec.sds.plan
version: 0.3.0
---

# /marketspec.plan 🔴 Core

**Purpose**: Develop a comprehensive marketing strategy plan based on clarified requirements.

**Category**: Core Flow (Essential Workflow)  
**Output**: `specs/{sequence}-{name}/plan.md` ⭐  
**Adapted from**: `metaspec.sds.plan`

---

## 📖 Navigation Guide (Token Optimization)

**File Size**: 998 lines (~3495 tokens)  
**Recommended**: Read specific sections to save 70-90% tokens

| Section | Lines | Size | Usage |
|---------|-------|------|-------|
| 1. Command Overview | 1-96 | 96 lines | `read_file(target, offset=1, limit=96)` |
| 2. Execution Steps | 97-505 | 409 lines | `read_file(target, offset=97, limit=409)` |
| 3. Output Format - Executive & Approach | 506-537 | 32 lines | `read_file(target, offset=506, limit=32)` |
| 4. Campaign Structure & Channels | 538-603 | 66 lines | `read_file(target, offset=538, limit=66)` |
| 5. Content Plan & KPIs | 604-663 | 60 lines | `read_file(target, offset=604, limit=60)` |
| 6. Budget, Timeline & Risk | 664-759 | 96 lines | `read_file(target, offset=664, limit=96)` |
| 7. Tools, Success Criteria & Examples | 760-998 | 239 lines | `read_file(target, offset=760, limit=239)` |

**💡 Typical Usage**:
```python
# Quick reference: Read overview only (96 lines)
read_file(target, offset=1, limit=96)

# Core logic: Read execution steps (409 lines)
read_file(target, offset=97, limit=409)

# Output structure: Read campaign structure and channels (66 lines)
read_file(target, offset=538, limit=66)

# Implementation details: Read budget, timeline and risk (96 lines)
read_file(target, offset=664, limit=96)
```

**Token Savings**:
- Full file: 998 lines (~3495 tokens)
- Single section: 32-409 lines (~110-1430 tokens) → **70-90% savings** 🏆
- Core logic only: 409 lines (~1430 tokens) → **59% savings**

---

## Purpose

Transform discovered and clarified requirements into a concrete marketing strategy plan:
- Define marketing approach and tactics
- Select channels and content types
- Plan campaigns and milestones  
- Allocate budget across initiatives
- Set measurable KPIs and success metrics
- Create execution timeline

This plan serves as the **architecture blueprint** for implementation.

---

## Command Usage

```
/marketspec.plan
/marketspec.plan --approach [approach]
```

**Examples**:
```
/marketspec.plan
/marketspec.plan --approach "content-led growth"
/marketspec.plan --approach "community-first"
```

---

## Prerequisites

- **Required**: Draft specification from `/marketspec.specify`
- **Recommended**: Clarifications from `/marketspec.clarify`
- **Recommended**: Constitution from `/marketspec.constitution`

---

## Execution Steps

### Step 1: Review Requirements

Load and analyze:
1. Draft specification (`specs/{sequence}-{name}/spec.md`)
2. Clarification sessions (if any)
3. Constitution principles (if defined)

**Extract key inputs**:
- Marketing objectives and priorities
- Target audiences and their characteristics
- Budget and timeline constraints
- Current state and available resources
- Success metrics

### Step 2: Define Marketing Approach

Choose primary marketing approach(es) based on objectives and audience:

**Common Approaches**:

#### A. Content-Led Growth
```yaml
approach: "content-led"
description: "Build audience through valuable content"
best_for:
  - Educational products
  - Technical audiences
  - Thought leadership
tactics:
  - Blog posts and tutorials
  - Technical documentation
  - Developer guides
  - Video tutorials
```

#### B. Community-First
```yaml
approach: "community-first"
description: "Build engaged community before pushing product"
best_for:
  - Open source projects
  - Developer tools
  - Niche audiences
tactics:
  - Discord/Slack community
  - GitHub discussions
  - Community events
  - User-generated content
```

#### C. Product-Led Growth
```yaml
approach: "product-led"
description: "Product drives adoption through free tier/trial"
best_for:
  - SaaS products
  - Self-service tools
  - Viral potential
tactics:
  - Free tier optimization
  - In-product education
  - Referral programs
  - Usage analytics
```

#### D. Partnership-Led
```yaml
approach: "partnership-led"
description: "Grow through strategic partnerships"
best_for:
  - B2B products
  - Integration platforms
  - Ecosystem plays
tactics:
  - Integration partnerships
  - Co-marketing
  - Affiliate programs
  - Reseller channels
```

#### E. Paid Acquisition
```yaml
approach: "paid-acquisition"
description: "Scale through paid advertising"
best_for:
  - High LTV products
  - Competitive markets
  - Fast growth needs
tactics:
  - Google Ads
  - Social ads (LinkedIn, Twitter, Facebook)
  - Sponsored content
  - Retargeting
```

**Select Approach**:
- Can choose 1 primary + 1-2 secondary approaches
- Base decision on objectives, audience, and budget

### Step 3: Design Campaign Structure

Plan high-level campaign structure:

```yaml
campaign_structure:
  # Campaign 1: Launch/Awareness
  - campaign_id: "launch-campaign"
    name: "Product Launch Campaign"
    objective: "awareness"
    duration: "6 weeks"
    budget: "$4,000"
    priority: "high"
    
    phases:
      - phase: "Pre-launch (weeks 1-2)"
        focus: "Teaser content, waitlist building"
      - phase: "Launch (week 3)"
        focus: "Launch announcements, PR push"
      - phase: "Post-launch (weeks 4-6)"
        focus: "User testimonials, case studies"
  
  # Campaign 2: Ongoing Engagement
  - campaign_id: "content-series"
    name: "Educational Content Series"
    objective: "consideration"
    duration: "12 weeks"
    budget: "$6,000"
    priority: "high"
```

### Step 4: Channel Selection & Strategy

Select and define strategy for each channel:

```yaml
channels:
  # Primary Channels
  - channel_id: "dev-twitter"
    name: "Twitter/X (Developer Focus)"
    type: "social_media"
    role: "primary"
    objectives: ["awareness", "engagement"]
    audience_fit: "high"  # Matches target audience
    
    content_strategy:
      frequency: "2-3 posts per day"
      content_mix:
        - type: "Tips & tricks" 
          percentage: 40
        - type: "Product updates"
          percentage: 30
        - type: "Community highlights"
          percentage: 30
      
    engagement_strategy:
      - "Reply to mentions within 2 hours"
      - "Engage with community conversations"
      - "Run weekly polls/questions"
    
    budget: "$500/month"
    expected_reach: "50K impressions/month"
  
  # Secondary Channels
  - channel_id: "dev-blog"
    name: "Developer Blog"
    type: "blog"
    role: "primary"
    objectives: ["consideration", "conversion"]
    
    content_strategy:
      frequency: "2 posts per week"
      content_types:
        - "Technical tutorials"
        - "Use case guides"
        - "Architecture deep-dives"
      
    distribution:
      - "Cross-post to Dev.to"
      - "Share on Hacker News"
      - "Newsletter digest"
    
    budget: "$2,000/month"
    expected_traffic: "5K visits/month"
```

**Channel Selection Criteria**:
- ✅ Audience presence (where target audience spends time)
- ✅ Content fit (matches content types you can create)
- ✅ Resource availability (can maintain quality and frequency)
- ✅ Budget efficiency (ROI potential)

### Step 5: Content Planning

Define content themes and production plan:

```yaml
content_plan:
  themes:
    - theme: "Getting Started"
      purpose: "Onboard new users"
      content_pieces:
        - "Quick start guide"
        - "Video tutorial series"
        - "Common pitfalls article"
    
    - theme: "Advanced Use Cases"
      purpose: "Engage power users"
      content_pieces:
        - "Architecture patterns"
        - "Performance optimization"
        - "Integration guides"
  
  production_pipeline:
    - role: "Content Writer"
      capacity: "4 articles/month"
      cost: "$2,000/month"
    
    - role: "Designer"
      capacity: "8 graphics/month"
      cost: "$800/month"
    
    - role: "Video Producer"
      capacity: "2 videos/month"
      cost: "$1,200/month"
```

### Step 6: Define KPIs and Success Metrics

Set specific, measurable KPIs for each objective:

```yaml
kpis:
  # Awareness KPIs
  - name: "Brand Impressions"
    category: "awareness"
    baseline: 5000
    target: 100000
    timeframe: "Q1 2025"
    priority: "P0"
    measurement_method: "Twitter Analytics + Blog Analytics"
    
  - name: "Website Traffic"
    category: "awareness"
    baseline: 500
    target: 5000
    timeframe: "Q1 2025"
    priority: "P0"
    measurement_method: "Google Analytics"
  
  # Consideration KPIs
  - name: "Content Engagement Rate"
    category: "consideration"
    baseline: 2.5
    target: 5.0
    unit: "percentage"
    timeframe: "Q1 2025"
    priority: "P1"
    measurement_method: "Avg time on page, scroll depth"
  
  # Conversion KPIs
  - name: "GitHub Stars"
    category: "conversion"
    baseline: 50
    target: 500
    timeframe: "Q1 2025"
    priority: "P0"
    measurement_method: "GitHub API"
  
  - name: "Email Signups"
    category: "conversion"
    baseline: 100
    target: 1000
    timeframe: "Q1 2025"
    priority: "P1"
    measurement_method: "Email platform (Mailchimp/ConvertKit)"
```

**KPI Requirements**:
- Must have baseline (current state)
- Must have target (goal)
- Must have timeframe (deadline)
- Must have measurement method (how to track)
- Must have priority (P0/P1/P2)

### Step 7: Budget Allocation

Allocate budget across initiatives:

```yaml
budget_allocation:
  total: 10000
  currency: "USD"
  period: "Q1 2025"
  
  breakdown:
    content_creation: 4000
      # Writers, designers, video producers
    paid_promotion: 3000
      # Ads, sponsored posts, influencer partnerships
    tools_and_platforms: 1500
      # Analytics, marketing automation, design tools
    community_and_events: 1000
      # Meetups, webinars, swag
    contingency: 500
      # Buffer for unexpected opportunities
  
  justification:
    - category: "content_creation"
      amount: 4000
      rationale: "Content-led approach requires quality content production"
    - category: "paid_promotion"
      amount: 3000
      rationale: "Amplify organic content to reach target audience faster"
```

### Step 8: Timeline and Milestones

Create execution timeline:

```yaml
timeline:
  start_date: "2025-01-15"
  end_date: "2025-03-31"
  duration: "11 weeks"
  
  milestones:
    - date: "2025-01-15"
      milestone: "Campaign Launch"
      deliverables:
        - "Website live"
        - "Social channels active"
        - "First 5 blog posts published"
    
    - date: "2025-02-01"
      milestone: "Content Pipeline Established"
      deliverables:
        - "2 posts/week rhythm"
        - "Community engagement active"
        - "First metrics review"
    
    - date: "2025-02-15"
      milestone: "Mid-Campaign Review"
      deliverables:
        - "KPI performance analysis"
        - "Plan adjustments if needed"
        - "A/B test results"
    
    - date: "2025-03-31"
      milestone: "Campaign Complete"
      deliverables:
        - "Final KPI report"
        - "Lessons learned document"
        - "Recommendations for next phase"
  
  weekly_cadence:
    monday: "Content planning meeting"
    tuesday: "Content production day"
    wednesday: "Content review and approval"
    thursday: "Publication day"
    friday: "Analytics review and community engagement"
```

### Step 9: Risk Assessment

Identify risks and mitigation strategies:

```yaml
risks:
  - risk: "Low engagement on technical content"
    probability: "medium"
    impact: "high"
    mitigation:
      - "A/B test different content formats"
      - "Interview target users for topic validation"
      - "Pivot to community-preferred topics"
  
  - risk: "Budget overspend on paid ads with low ROI"
    probability: "medium"
    impact: "medium"
    mitigation:
      - "Start with small test budgets"
      - "Set strict CPA/CPM thresholds"
      - "Review performance weekly"
  
  - risk: "Key team member unavailable"
    probability: "low"
    impact: "high"
    mitigation:
      - "Cross-train team members"
      - "Maintain content buffer (2 weeks ahead)"
      - "Have freelancer backup list"
```

### Step 10: Generate Marketing Plan Document

Create comprehensive plan document:

```markdown
# Marketing Plan: [Campaign Name]

**Version**: 1.0  
**Date**: 2025-11-19  
**Period**: Q1 2025  
**Status**: Approved, ready for implementation

---

## Executive Summary

[2-3 paragraph summary of plan]

**Approach**: Content-led growth + Community-first  
**Budget**: $10,000 for Q1 2025  
**Primary Goal**: Reach 500 GitHub stars and 1K email signups  
**Timeline**: Jan 15 - Mar 31, 2025 (11 weeks)

---

## Marketing Approach

[Content from Step 2]

### Primary Approach: [Name]

**Description**: [What and why]

**Rationale**: [Why this fits objectives and audience]

**Key Tactics**:
- [Tactic 1]
- [Tactic 2]
- [Tactic 3]

### Supporting Approach: [Name]

[If applicable]

---

## Campaign Structure

[Content from Step 3]

### Campaign 1: [Name]

**Objective**: [Awareness/Consideration/Conversion]  
**Duration**: [Timeline]  
**Budget**: [Amount]  
**Priority**: [High/Medium/Low]

**Phases**:
1. **[Phase 1]** ([Dates])
   - Focus: [What]
   - Key Activities: [List]
   
2. **[Phase 2]** ([Dates])
   - Focus: [What]
   - Key Activities: [List]

**Success Metrics**: [How to measure]

### Campaign 2: [Name]

[Similar structure]

---

## Channel Strategy

[Content from Step 4]

### Channel Selection Rationale

[Why these channels]

### Primary Channels

#### [Channel 1]

**Type**: [Blog, Social, Email, etc.]  
**Role**: [Primary/Secondary]  
**Audience Fit**: [High/Medium/Low]

**Content Strategy**:
- Frequency: [How often]
- Content Mix: [Types and percentages]
- Distribution: [How content reaches audience]

**Engagement Strategy**:
- [Strategy point 1]
- [Strategy point 2]

**Budget**: [Amount]  
**Expected Reach**: [Metric]

#### [Channel 2]

[Similar structure for each channel]

### Channel Integration

[How channels work together to amplify each other]

---

## Content Plan

[Content from Step 5]

### Content Themes

#### Theme 1: [Name]

**Purpose**: [Goal]  
**Target Audience**: [Segment]

**Content Pieces**:
1. [Piece 1]
   - Format: [Type]
   - Channel: [Where]
   - Timeline: [When]
   
2. [Piece 2]
   [Details]

#### Theme 2: [Name]

[Similar structure]

### Content Production

**Team Structure**:
- [Role 1]: [Capacity and cost]
- [Role 2]: [Capacity and cost]

**Content Calendar Framework**:
[Week-by-week outline]

**Quality Standards**:
[From constitution or requirements]

---

## KPIs and Success Metrics

[Content from Step 6]

### Primary KPIs (P0)

| KPI | Baseline | Target | Timeframe | Measurement |
|-----|----------|--------|-----------|-------------|
| [Name] | [Number] | [Number] | [Period] | [Method] |

### Secondary KPIs (P1)

| KPI | Baseline | Target | Timeframe | Measurement |
|-----|----------|--------|-----------|-------------|
| [Name] | [Number] | [Number] | [Period] | [Method] |

### Leading Indicators

[Early signals that predict success]

---

## Budget Allocation

[Content from Step 7]

### Total Budget

**Amount**: $[Total]  
**Period**: [Timeline]  
**Currency**: USD

### Breakdown by Category

| Category | Amount | % | Rationale |
|----------|--------|---|-----------|
| Content Creation | $[Amount] | [%] | [Why] |
| Paid Promotion | $[Amount] | [%] | [Why] |
| Tools & Platforms | $[Amount] | [%] | [Why] |
| Community & Events | $[Amount] | [%] | [Why] |
| Contingency | $[Amount] | [%] | [Why] |
| **Total** | **$[Total]** | **100%** | - |

### Budget by Channel

| Channel | Budget | % of Total | Expected ROI |
|---------|--------|------------|--------------|
| [Channel 1] | $[Amount] | [%] | [Est.] |

---

## Timeline and Milestones

[Content from Step 8]

### Campaign Timeline

**Start**: [Date]  
**End**: [Date]  
**Duration**: [Weeks]

### Milestones

#### Milestone 1: [Name]

**Date**: [Date]  
**Description**: [What]

**Deliverables**:
- [Deliverable 1]
- [Deliverable 2]

**Success Criteria**:
- [Criterion 1]
- [Criterion 2]

#### Milestone 2: [Name]

[Similar structure]

### Weekly Cadence

| Day | Activity | Owner |
|-----|----------|-------|
| Monday | [Activity] | [Role] |
| Tuesday | [Activity] | [Role] |
| Wednesday | [Activity] | [Role] |
| Thursday | [Activity] | [Role] |
| Friday | [Activity] | [Role] |

---

## Risk Assessment

[Content from Step 9]

### Identified Risks

#### Risk 1: [Name]

**Description**: [What could go wrong]  
**Probability**: [High/Medium/Low]  
**Impact**: [High/Medium/Low]  
**Priority**: [H/M/L]

**Mitigation**:
- [Strategy 1]
- [Strategy 2]

**Contingency Plan**:
[What to do if risk occurs]

#### Risk 2: [Name]

[Similar structure]

---

## Tools & Resources

### Required Tools

| Tool | Purpose | Cost | Owner |
|------|---------|------|-------|
| [Tool name] | [Use] | $[Amount]/month | [Role] |

### Team Resources

| Role | Capacity | Responsibilities |
|------|----------|------------------|
| [Role] | [Hours/week or output] | [What they do] |

---

## Next Steps

1. **Break down into tasks** → `/marketspec.tasks`
2. **Generate checklist** → `/marketspec.checklist`
3. **Create final specification** → `/marketspec.implement`
4. **Begin execution** → Follow campaign plan

---

## Appendices

### A. Approach Research

[Details on why chosen approach fits]

### B. Channel Analysis

[Competitive analysis of chosen channels]

### C. Content Examples

[Sample content structures or examples]

### D. Reference Materials

**Source Documents**:
- Draft Specification: `specs/{sequence}-{name}/spec.md`
- Clarifications: `specs/{sequence}-{name}/clarifications.md`
- Constitution: `memory/constitution.md`
```

**Output Location**: `specs/{sequence}-{name}/plan.md`

---

## Success Criteria

- ✅ Clear marketing approach selected and justified
- ✅ 2-4 campaigns designed with objectives and budgets
- ✅ 3-5 channels selected with content strategies
- ✅ Specific KPIs defined with baselines and targets
- ✅ Budget allocated across initiatives with rationale
- ✅ Timeline with milestones and weekly cadence
- ✅ Risks identified with mitigation plans
- ✅ Plan document is Markdown (not YAML or operational data)

---

## Output

**Primary Output**: `specs/{sequence}-{name}/plan.md`

**Example**:
```
specs/001-q1-campaign-strategy/
├── spec.md              ← Draft (from /marketspec.specify)
└── plan.md              ← Marketing plan (from this command) ⭐
```

**Structure**:
```
specs/
├── 001-q1-campaign-strategy/
│   ├── spec.md                  ← Draft specification
│   ├── clarifications.md        ← Clarifications (optional)
│   └── plan.md                  ← Marketing plan (NEW)
```

---

## Error Handling

- If draft specification incomplete, prompt to complete first
- If objectives conflict with budget, highlight trade-offs
- If timeline unrealistic, suggest adjustment or phasing
- If KPIs unmeasurable, help define tracking method

---

## Example Interaction

```
User: /marketspec.plan

AI: I'll help you develop a marketing plan based on your specification.

📄 **Loaded**:
- Draft Spec: specs/001-q1-campaign/spec.md
- Clarifications: specs/001-q1-campaign/clarifications.md

**Key Inputs**:
✅ Objectives: Awareness + GitHub stars
✅ Audience: Senior/mid-level Python/JS developers  
✅ Budget: $10K for Q1
✅ Timeline: Jan-Mar 2025

---

Let's define your marketing approach. Based on your objectives and audience, I recommend:

**Primary Approach**: Content-Led Growth
- Developers trust educational content
- Builds long-term organic reach
- Cost-effective for your budget

**Secondary Approach**: Community-First
- Engage developers where they are
- Creates advocates and word-of-mouth
- Complements content strategy

Does this align with your vision, or would you prefer a different approach?

---

User: Sounds good, let's go with that.

AI: Perfect! Now let's design your campaign structure.

I recommend 2 main campaigns for Q1:

**Campaign 1: "Developer Onboarding" (Weeks 1-6)**
- Goal: Awareness + Education
- Budget: $6K
- Focus: Help developers understand your product

**Campaign 2: "Power User Stories" (Weeks 7-11)**
- Goal: Social proof + Conversion
- Budget: $4K  
- Focus: Showcase advanced use cases

Does this structure work?

---

User: Yes, let's proceed.

AI: Excellent. Let me select optimal channels...

Based on your audience (Python/JS developers), I recommend:

**Primary Channels** (80% of effort):
1. **Developer Blog** - Technical tutorials and guides
   - Frequency: 2 posts/week
   - Budget: $4K (writers + designers)

2. **Twitter/X** - Tips, updates, engagement
   - Frequency: 2-3 posts/day
   - Budget: $1K (tools + some promotion)

**Secondary Channels** (20% of effort):
3. **Dev.to** - Republished content
4. **GitHub Discussions** - Community support

[Continues through all steps...]

---

[After completing all steps]

AI: Perfect! Your marketing plan is complete:

📄 **Plan Document**: specs/001-q1-campaign/plan.md

**Summary**:
✅ Approach: Content-led + Community-first
✅ 2 Campaigns designed (Onboarding + Power Users)
✅ 4 Channels selected (Blog, Twitter, Dev.to, GitHub)
✅ 8 KPIs defined with targets
✅ $10K budget allocated
✅ 11-week timeline with 4 milestones
✅ 3 risks identified with mitigation

**Next Steps**:
1. 📋 Break down into tasks → `/marketspec.tasks`
2. ✅ Generate quality checklist → `/marketspec.checklist`
3. 📄 Write final specification → `/marketspec.implement`

Ready to break down the tasks?
```

---

## Notes

- **Plan defines ARCHITECTURE, not execution details**
- Strategy should be realistic given constraints
- Align with constitution principles if defined
- Focus on 2-3 channels done well vs. many channels done poorly
- Content-led and community approaches work well for developer tools
- Include both leading (activity) and lagging (outcome) metrics
- Build in flexibility - plan may need adjustment mid-execution
- **This is still a SPECIFICATION (how to market), not operational data**

---

## Integration with Other Commands

Feeds into:
- `/marketspec.tasks` - Break plan into actionable tasks
- `/marketspec.implement` - Generate final complete specification

References:
- `/marketspec.constitution` - Ensure plan aligns with principles
- `/marketspec.specify` - Source requirements
- `/marketspec.clarify` - Source refined requirements

**Workflow Position**:
```
specify → clarify → plan → tasks → analyze → implement
                      ↑
                  (you are here)
```

---

## See Also

- `/marketspec.clarify` - Previous step
- `/marketspec.tasks` - Next step
- `/marketspec.implement` - Final specification generation
- Plan examples in `examples/` directory
- Marketing approaches documented in project specs
- MetaSpec SDD Plan: `.metaspec/commands/metaspec.sdd.plan.md`
