# Slash Command: /marketing.plan.create

## Purpose

Create a new marketing plan with strategic objectives, target audience, strategies, and budget allocation.

## Command Usage

```
/marketing.plan.create
```

## Prerequisites

- Must have a Project defined in the specification
- Specification file must be accessible

## Execution Steps

### Step 1: Read Current Specification

Read the marketing specification file to understand the project context:

```yaml
# Expected structure
project:
  name: "..."
  tagline: "..."
  brand_voice: "..."
  target_audience: [...]
  value_propositions: [...]
```

### Step 2: Gather Plan Requirements

Ask the user for the following information (if not provided):

**Required**:
- `name`: Plan name (string, min 3 chars)
- `period`: Time period
  - `start_date`: ISO 8601 date (YYYY-MM-DD)
  - `end_date`: ISO 8601 date (YYYY-MM-DD)
  - `duration_weeks`: Integer (4-52)
- `objectives`: High-level marketing objectives (1-5 strings)
- `target_audience`: List of audience segments, each with:
  - `segment`: Segment name
  - `description`: Detailed description
  - `size_estimate`: Estimated size (integer > 0)
  - `priority`: high | medium | low
- `strategies`: Marketing strategies (1-8), each with:
  - `name`: Strategy name
  - `description`: Strategy details
  - `rationale`: Why this strategy
  - `success_criteria`: How to measure success
- `budget`: Budget allocation
  - `total`: Total budget (float > 0)
  - `currency`: Currency code (default: USD)
  - `allocation`: Dict mapping categories to amounts
- `kpis`: Key performance indicators (1-10), each with:
  - `name`: KPI name
  - `target`: Target value (float)
  - `unit`: Measurement unit
  - `measurement`: How to measure
  - `priority`: P0 | P1 | P2

**Optional**:
- `campaign_ids`: List of campaign IDs (if campaigns already exist)
- `approval`: Approval metadata (if plan is already approved)
  - `approved_by`: Approver name/ID
  - `approved_at`: Approval timestamp (ISO 8601)
  - `comments`: Optional approval notes

### Step 3: Generate plan_id

Create a unique plan ID:
- Lowercase
- Hyphens only
- Example: `q4-2025-growth-plan`

### Step 4: Set Timestamps

Generate current ISO 8601 timestamps:
- `created_at`: Current time
- `updated_at`: Current time

### Step 5: Validate Plan Data

Check the following validation rules (PLAN-01 to PLAN-05):

1. **PLAN-01**: All objectives must be non-empty strings
2. **PLAN-02**: `duration_weeks` must be 4-52
3. **PLAN-03**: Budget `allocation` sum must equal `total` (±$0.01)
4. **PLAN-04**: If `status` is APPROVED or ACTIVE, `approval` is required
5. **PLAN-05**: Strategies count must be 1-8

### Step 6: Generate YAML/JSON

Output the complete MarketingPlan entity:

```yaml
plans:
  - id: "q4-2025-growth-plan"
    name: "Q4 2025 Growth Plan"
    project_id: "my-project"
    period:
      start_date: "2025-10-01"
      end_date: "2025-12-31"
      duration_weeks: 13
    objectives:
      - "Increase brand awareness by 50%"
      - "Drive 10,000 new signups"
      - "Achieve $100K revenue"
    target_audience:
      - segment: "Early Adopters"
        description: "Tech-savvy developers looking for cutting-edge tools"
        size_estimate: 50000
        priority: "high"
    strategies:
      - name: "Content Marketing"
        description: "Publish weekly technical blog posts"
        rationale: "Developers trust educational content"
        success_criteria: "10K monthly blog visitors"
      - name: "Community Engagement"
        description: "Active participation in developer forums"
        rationale: "Build trust and credibility"
        success_criteria: "1000 forum interactions"
    budget:
      total: 5000
      currency: "USD"
      allocation:
        content_creation: 2000
        paid_promotion: 2500
        tools: 300
        contingency: 200
    kpis:
      - name: "Brand Awareness"
        target: 50000
        unit: "impressions"
        measurement: "Social media reach + website traffic"
        priority: "P0"
      - name: "Signups"
        target: 10000
        unit: "users"
        measurement: "New user registrations"
        priority: "P0"
      - name: "Revenue"
        target: 100000
        unit: "USD"
        measurement: "Total sales"
        priority: "P1"
    campaign_ids: []
    status: "draft"
    created_at: "2025-11-15T10:00:00Z"
    updated_at: "2025-11-15T10:00:00Z"
```

## Success Criteria

- Plan passes all validation rules (PLAN-01 to PLAN-05)
- YAML is syntactically correct
- All required fields are present
- Budget allocation sums to total

## Error Handling

- If project doesn't exist, prompt user to create one first
- If budget allocation doesn't sum to total, suggest corrections
- If date range is invalid, suggest valid ranges

## Example Interaction

```
User: /marketing.plan.create

AI: I'll help you create a marketing plan. Let me gather the necessary information:

1. What's the plan name? (e.g., "Q4 2025 Growth Plan")
2. What's the time period?
   - Start date (YYYY-MM-DD):
   - End date (YYYY-MM-DD):
3. What are your top 3-5 marketing objectives?
4. Who is your target audience?
5. What marketing strategies will you use?
6. What's your total budget and how should it be allocated?
7. What KPIs will you track?

[After gathering info]

Here's your marketing plan:

```yaml
plans:
  - id: "q4-2025-growth-plan"
    ...
```

✅ Validation passed (5/5 rules)
Ready to add to your specification file.
```

## Notes

- Plan should align with Project's `value_propositions` and `target_audience`
- Budget should be realistic for the plan duration
- KPIs should be SMART (Specific, Measurable, Achievable, Relevant, Time-bound)
- At least one P0 (critical) KPI is recommended

