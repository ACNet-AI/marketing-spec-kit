# Slash Command: /marketing.campaign.design

## Purpose

AI-assisted campaign design based on a marketing plan. Suggests campaign structure, timeline, budget, and channels.

## Command Usage

```
/marketing.campaign.design <plan_id> [campaign_goal]
```

## Prerequisites

- Plan must exist in specification
- Plan should have defined objectives and strategies

## Execution Steps

### Step 1: Read Plan Context

Load plan details:
- Objectives
- Target audience
- Strategies
- Budget available
- Period (for timeline constraints)

### Step 2: Determine Campaign Goal

If not provided, suggest based on plan objectives:
- **awareness**: Top of funnel (brand awareness)
- **consideration**: Middle of funnel (engagement)
- **conversion**: Bottom of funnel (sales/signups)

### Step 3: AI-Generated Campaign Design

Generate a campaign proposal including:

#### Basic Information
- `id`: Suggested campaign ID
- `name`: Descriptive campaign name
- `goal`: Campaign objective (awareness/consideration/conversion)
- `plan_id`: Parent plan ID

#### Timeline
- `start_date`: Suggested start (within plan period)
- `end_date`: Suggested end (within plan period, typically 2-4 weeks)

#### Targeting
- `target_audience`: Segments from plan (prioritize high-priority segments)

#### Budget
- `budget`: Suggested amount (% of plan budget, typically 20-40%)
- `expected_kpis`: Projected performance based on industry benchmarks

#### Channels
- `channels`: Recommended channel mix based on:
  - Target audience preferences
  - Campaign goal (awareness vs conversion)
  - Budget constraints

#### Content Calendar (Optional)
- Suggested content publishing schedule
- Content types per channel
- Frequency recommendations

### Step 4: Provide Rationale

Explain design decisions:
- Why this goal aligns with plan objectives
- Why these channels were selected
- How budget was allocated
- Timeline reasoning

### Step 5: Output Campaign Proposal

```yaml
campaigns:
  - id: "q4-awareness-launch"
    name: "Q4 Product Launch Awareness Campaign"
    goal: "awareness"
    plan_id: "q4-2025-growth-plan"
    project_id: "my-project"
    target_audience:
      - "Early Adopters"
    budget: 2000  # 40% of plan budget
    start_date: "2025-10-01"
    end_date: "2025-10-21"  # 3 weeks
    channels:
      - "twitter"
      - "dev-to"
      - "reddit"
    expected_kpis:
      impressions: 30000
      engagement_rate: 0.03
      click_through_rate: 0.02
    content_calendar:
      - date: "2025-10-01"
        content_type: "announcement"
        channel_id: "twitter"
        title: "Product Launch Announcement"
        status: "planned"
      - date: "2025-10-08"
        content_type: "tutorial"
        channel_id: "dev-to"
        title: "Getting Started Tutorial"
        status: "planned"
    status: "draft"
```

```markdown
## Design Rationale

**Goal Selection**: Awareness
- Aligns with plan objective "Increase brand awareness by 50%"
- Appropriate for campaign launch phase

**Channel Mix**: Twitter + Dev.to + Reddit
- **Twitter**: Real-time engagement, developer audience
- **Dev.to**: Long-form technical content, SEO benefits
- **Reddit**: Community discussions, r/programming reach

**Budget Allocation**: $2,000 (40% of plan)
- Awareness campaigns typically need 30-50% of budget
- Leaves $3,000 for follow-up campaigns

**Timeline**: 3 weeks (Oct 1-21)
- Standard awareness campaign duration
- Aligns with plan start date
- Allows time for measurement before next campaign

**Expected KPIs**:
- **30K impressions**: Based on $2K budget at $0.067 CPM (industry avg)
- **3% engagement**: Conservative estimate for developer audience
- **2% CTR**: Typical for awareness campaigns

## Next Steps

1. Review and adjust proposed campaign
2. Validate with /marketing.campaign (existing command)
3. Create content using /marketing.generate.* commands
4. Execute with /marketing.execute.schedule
```

## Success Criteria

- Campaign design aligns with plan
- Budget fits within plan constraints
- Timeline respects plan period
- Channels match target audience
- Rationale is clear and data-driven

## Example Interaction

```
User: /marketing.campaign.design q4-2025-growth-plan awareness

AI: Designing awareness campaign for 'q4-2025-growth-plan'...

[Displays complete campaign proposal with YAML and rationale]

✅ Campaign validated (passes CAMP-08, CAMP-09, CAMP-10)

Would you like me to:
A) Add this campaign to your specification
B) Adjust the design (budget/timeline/channels)
C) Design another campaign with a different goal
```

