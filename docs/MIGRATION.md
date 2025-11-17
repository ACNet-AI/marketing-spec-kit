# Migration Guide: v1.x → v2.0.0

This guide helps you upgrade existing marketing specifications from v1.x to v2.0.0.

---

## 🚨 Breaking Changes

### 1. Campaign.plan_id is now REQUIRED

**What changed**: Every `Campaign` must now have a `plan_id` field that references a `MarketingPlan`.

**Why**: v2.0.0 introduces a structured 5-phase workflow where campaigns are tactical executions of strategic plans.

**Impact**: All existing v1.x specifications with campaigns will fail validation in v2.0.0.

---

## 📋 Migration Checklist

- [ ] Review your existing campaigns
- [ ] Create at least one MarketingPlan
- [ ] Add `plan_id` to all campaigns
- [ ] Validate with `marketing_spec_kit validate`
- [ ] Update any automation/scripts that create specs

---

## 🔄 Step-by-Step Migration

### Step 1: Audit Your Current Spec

First, understand what you have:

```bash
# Validate your v1.x spec (will show errors in v2.0.0)
marketing_spec_kit validate your-spec.yaml
```

Expected errors:
```
❌ [CAMP-08] Campaign 'summer-campaign' missing required field: 'plan_id'
❌ [MKT-VAL-002] Missing required field: 'campaigns.0.plan_id'
```

### Step 2: Create a MarketingPlan

Add a `plans` section to your spec before `campaigns`:

```yaml
# Add this BEFORE your campaigns section
plans:
  - id: "2025-marketing-plan"
    name: "2025 Marketing Strategy"
    project_id: "your-project-id"
    
    # Time period (4-52 weeks)
    period:
      start_date: "2025-01-01"
      end_date: "2025-12-31"
      duration_weeks: 52
    
    # 1-5 objectives
    objectives:
      - "Increase brand awareness"
      - "Drive product signups"
    
    # Target audience (at least 1)
    target_audience:
      - segment: "Primary Users"
        description: "Your main audience"
        size_estimate: 10000
        priority: "high"
    
    # 1-8 strategies
    strategies:
      - name: "Content Marketing"
        description: "Regular blog posts and tutorials"
        rationale: "Build authority and trust"
        success_criteria: "10K monthly visitors"
    
    # Budget (must sum to total)
    budget:
      total: 5000
      currency: "USD"
      allocation:
        content: 3000
        paid_ads: 1500
        tools: 500
    
    # 1-10 KPIs
    kpis:
      - name: "Website Traffic"
        target: 100000
        unit: "visitors"
        measurement: "Google Analytics"
        priority: "P0"
    
    # List campaign IDs that belong to this plan
    campaign_ids:
      - "summer-campaign"
      - "fall-campaign"
    
    status: "active"
    created_at: "2025-01-01T00:00:00Z"
    updated_at: "2025-01-01T00:00:00Z"
```

### Step 3: Add plan_id to All Campaigns

For each campaign, add the `plan_id` field:

**Before (v1.x)**:
```yaml
campaigns:
  - id: "summer-campaign"
    name: "Summer Sale Campaign"
    goal: "conversion"
    project_id: "my-project"
    # ... other fields
```

**After (v2.0.0)**:
```yaml
campaigns:
  - id: "summer-campaign"
    name: "Summer Sale Campaign"
    goal: "conversion"
    plan_id: "2025-marketing-plan"  # ADD THIS
    project_id: "my-project"
    # ... other fields
```

### Step 4: Ensure Campaign Dates Are Within Plan Period

**New Validation**: Campaign start/end dates must fall within the plan's period.

Check each campaign:
```yaml
campaigns:
  - id: "summer-campaign"
    # ...
    plan_id: "2025-marketing-plan"
    start_date: "2025-06-01"  # Must be >= plan.period.start_date
    end_date: "2025-08-31"    # Must be <= plan.period.end_date
```

If dates are outside the plan period, either:
- **Option A**: Adjust campaign dates to fit within plan
- **Option B**: Adjust plan period to accommodate campaigns
- **Option C**: Create multiple plans for different time periods

### Step 5: Validate Your Updated Spec

```bash
marketing_spec_kit validate your-spec.yaml
```

Expected output:
```
✅ Validation passed (45/45 rules)
   - Project: ✅ (6/6)
   - Products: ✅ (5/5)
   - Plans: ✅ (5/5)
   - Campaigns: ✅ (11/11)
   - ...
```

---

## 🆕 Optional v2.0.0 Features

While not required for migration, you can enhance your specs with new features:

### 1. Add expected_kpis to Campaigns (Planning Phase)

```yaml
campaigns:
  - id: "summer-campaign"
    # ... existing fields
    
    # NEW: Expected performance (for design phase)
    expected_kpis:
      impressions: 50000
      click_through_rate: 0.02
      conversions: 1000
```

### 2. Add content_calendar to Campaigns

```yaml
campaigns:
  - id: "summer-campaign"
    # ... existing fields
    
    # NEW: Scheduled content
    content_calendar:
      - date: "2025-06-01"
        content_type: "announcement"
        channel_id: "twitter"
        title: "Summer Sale Starts Today!"
        status: "planned"
      
      - date: "2025-06-15"
        content_type: "reminder"
        channel_id: "email"
        title: "50% Off Ends This Weekend"
        status: "planned"
```

### 3. Add Analytics Reports

After campaigns complete, add analytics:

```yaml
analytics:
  - id: "summer-campaign-report"
    type: "campaign"
    entity_id: "summer-campaign"
    
    period:
      start_date: "2025-06-01"
      end_date: "2025-08-31"
    
    metrics:
      impressions: 65000
      clicks: 1300
      conversions: 1200
      revenue: 30000
    
    vs_target:
      impressions:
        target: 50000
        actual: 65000
        achievement: 130
        status: "exceeds"
      
      conversions:
        target: 1000
        actual: 1200
        achievement: 120
        status: "exceeds"
    
    insights:
      - type: "success"
        description: "Campaign exceeded all targets"
        evidence: "130% impressions, 120% conversions"
        recommendation: "Replicate strategy for fall campaign"
    
    optimizations:
      - priority: "medium"
        action: "Increase budget for next campaign"
        expected_impact: "+30% reach"
        effort: "low"
    
    generated_at: "2025-09-01T10:00:00Z"
```

---

## 📊 Migration Examples

### Example 1: Simple Migration (One Plan, Two Campaigns)

**v1.x spec**:
```yaml
project:
  name: "MyApp"
  # ...

campaigns:
  - id: "launch"
    name: "Product Launch"
    goal: "awareness"
    project_id: "myapp"
    budget: 2000
    start_date: "2025-06-01"
    end_date: "2025-06-30"
    # ...
  
  - id: "growth"
    name: "Growth Campaign"
    goal: "conversion"
    project_id: "myapp"
    budget: 3000
    start_date: "2025-07-01"
    end_date: "2025-09-30"
    # ...
```

**v2.0.0 spec** (add plan):
```yaml
project:
  name: "MyApp"
  # ...

# NEW: Add plan
plans:
  - id: "2025-h2-plan"
    name: "2025 H2 Growth Plan"
    project_id: "myapp"
    period:
      start_date: "2025-06-01"
      end_date: "2025-09-30"
      duration_weeks: 17
    objectives:
      - "Launch product successfully"
      - "Achieve 5K signups"
    target_audience:
      - segment: "Early Adopters"
        description: "Tech-savvy users"
        size_estimate: 50000
        priority: "high"
    strategies:
      - name: "Launch Marketing"
        description: "Big bang launch"
        rationale: "Create momentum"
        success_criteria: "1K signups in first month"
    budget:
      total: 5000
      allocation:
        launch: 2000
        growth: 3000
    kpis:
      - name: "Signups"
        target: 5000
        unit: "users"
        measurement: "Database count"
        priority: "P0"
    campaign_ids:
      - "launch"
      - "growth"
    status: "active"
    created_at: "2025-05-01T00:00:00Z"
    updated_at: "2025-05-01T00:00:00Z"

campaigns:
  - id: "launch"
    name: "Product Launch"
    goal: "awareness"
    plan_id: "2025-h2-plan"  # ADD THIS
    project_id: "myapp"
    budget: 2000
    start_date: "2025-06-01"
    end_date: "2025-06-30"
    # ...
  
  - id: "growth"
    name: "Growth Campaign"
    goal: "conversion"
    plan_id: "2025-h2-plan"  # ADD THIS
    project_id: "myapp"
    budget: 3000
    start_date: "2025-07-01"
    end_date: "2025-09-30"
    # ...
```

### Example 2: Multiple Plans for Different Time Periods

If your campaigns span different quarters or have different strategic goals:

```yaml
plans:
  - id: "q2-awareness-plan"
    name: "Q2 Brand Awareness Plan"
    period:
      start_date: "2025-04-01"
      end_date: "2025-06-30"
      duration_weeks: 13
    # ... awareness objectives
  
  - id: "q3-conversion-plan"
    name: "Q3 Conversion Plan"
    period:
      start_date: "2025-07-01"
      end_date: "2025-09-30"
      duration_weeks: 13
    # ... conversion objectives

campaigns:
  - id: "q2-launch"
    plan_id: "q2-awareness-plan"
    start_date: "2025-04-01"
    end_date: "2025-06-30"
    # ...
  
  - id: "q3-growth"
    plan_id: "q3-conversion-plan"
    start_date: "2025-07-01"
    end_date: "2025-09-30"
    # ...
```

---

## ⚠️ Common Migration Errors

### Error 1: Missing plan_id

```
❌ [CAMP-08] Campaign 'my-campaign' references non-existent plan ''
```

**Fix**: Add `plan_id` field to the campaign.

### Error 2: Campaign dates outside plan period

```
❌ [CAMP-09] Campaign start (2025-01-01) outside plan period (2025-06-01 to 2025-12-31)
```

**Fix**: Either adjust campaign dates or extend plan period.

### Error 3: Budget allocation doesn't sum to total

```
❌ [PLAN-03] Budget allocation sum ($5100) != total ($5000)
```

**Fix**: Adjust allocation values to sum exactly to `budget.total`.

### Error 4: Invalid plan duration

```
❌ [PLAN-02] duration_weeks must be between 4 and 52
```

**Fix**: Adjust `period.duration_weeks` to be 4-52.

### Error 5: Missing approval for active plan

```
❌ [PLAN-04] Plan status 'active' requires approval metadata
```

**Fix**: Add `approval` field:
```yaml
plans:
  - id: "my-plan"
    status: "active"
    approval:
      approved_by: "Your Name"
      approved_at: "2025-01-01T00:00:00Z"
```

---

## 🛠️ Automated Migration Script (Python)

For large specs or multiple files, use this helper script:

```python
#!/usr/bin/env python3
"""
Migrate marketing-spec-kit v1.x to v2.0.0
Adds a default plan and plan_id to all campaigns
"""

import yaml
from datetime import datetime

def migrate_spec(input_file, output_file):
    # Load v1.x spec
    with open(input_file) as f:
        spec = yaml.safe_load(f)
    
    # Extract project info
    project_id = spec['project']['name'].lower().replace(' ', '-')
    
    # Create default plan if not exists
    if 'plans' not in spec or not spec['plans']:
        # Find earliest and latest campaign dates
        campaigns = spec.get('campaigns', [])
        if campaigns:
            start_dates = [c['start_date'] for c in campaigns if 'start_date' in c]
            end_dates = [c['end_date'] for c in campaigns if 'end_date' in c]
            
            plan_start = min(start_dates) if start_dates else "2025-01-01"
            plan_end = max(end_dates) if end_dates else "2025-12-31"
            
            # Calculate duration (approximate)
            from datetime import datetime
            start = datetime.fromisoformat(plan_start)
            end = datetime.fromisoformat(plan_end)
            duration_weeks = min(52, max(4, (end - start).days // 7))
            
            # Total budget from campaigns
            total_budget = sum(c.get('budget', 0) for c in campaigns)
            
            # Create default plan
            default_plan = {
                'id': f'{project_id}-plan',
                'name': f'{spec["project"]["name"]} Marketing Plan',
                'project_id': project_id,
                'period': {
                    'start_date': plan_start,
                    'end_date': plan_end,
                    'duration_weeks': duration_weeks
                },
                'objectives': [
                    'Drive brand awareness',
                    'Increase product adoption'
                ],
                'target_audience': [{
                    'segment': 'Target Users',
                    'description': spec['project'].get('target_audience', ['General audience'])[0],
                    'size_estimate': 10000,
                    'priority': 'high'
                }],
                'strategies': [{
                    'name': 'Multi-channel Marketing',
                    'description': 'Execute campaigns across channels',
                    'rationale': 'Reach users where they are',
                    'success_criteria': 'Achieve campaign KPIs'
                }],
                'budget': {
                    'total': total_budget if total_budget > 0 else 5000,
                    'currency': 'USD',
                    'allocation': {
                        'campaigns': total_budget if total_budget > 0 else 5000
                    }
                },
                'kpis': [{
                    'name': 'Overall Success',
                    'target': 10000,
                    'unit': 'users',
                    'measurement': 'Campaign metrics',
                    'priority': 'P0'
                }],
                'campaign_ids': [c['id'] for c in campaigns],
                'status': 'active',
                'created_at': datetime.now().isoformat() + 'Z',
                'updated_at': datetime.now().isoformat() + 'Z'
            }
            
            spec['plans'] = [default_plan]
            plan_id = default_plan['id']
        else:
            print("No campaigns found, skipping plan creation")
            plan_id = None
    else:
        plan_id = spec['plans'][0]['id']
    
    # Add plan_id to all campaigns
    if plan_id:
        for campaign in spec.get('campaigns', []):
            if 'plan_id' not in campaign:
                campaign['plan_id'] = plan_id
                print(f"✅ Added plan_id to campaign: {campaign['id']}")
    
    # Write v2.0.0 spec
    with open(output_file, 'w') as f:
        yaml.dump(spec, f, default_flow_style=False, sort_keys=False)
    
    print(f"\n✅ Migration complete: {input_file} → {output_file}")
    print(f"   Run: marketing_spec_kit validate {output_file}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: python migrate.py <input.yaml> <output.yaml>")
        sys.exit(1)
    
    migrate_spec(sys.argv[1], sys.argv[2])
```

**Usage**:
```bash
python migrate.py old-spec.yaml new-spec.yaml
marketing_spec_kit validate new-spec.yaml
```

---

## 📚 Additional Resources

- **[README.md](../README.md)**: Full v2.0.0 documentation
- **[CHANGELOG.md](../CHANGELOG.md)**: Complete list of changes
- **[examples/complete-v2-example.yaml](../examples/complete-v2-example.yaml)**: Full v2.0.0 example
- **[AGENTS.md](../AGENTS.md)**: AI Agent workflow guide

---

## 🆘 Need Help?

If you encounter issues during migration:

1. **Check validation errors**: Run `marketing_spec_kit validate` for detailed error messages
2. **Review examples**: See `examples/complete-v2-example.yaml` for a working spec
3. **Open an issue**: [GitHub Issues](https://github.com/yourusername/marketing-spec-kit/issues)

---

**Last Updated**: 2025-11-15  
**Applies to**: v2.0.0

