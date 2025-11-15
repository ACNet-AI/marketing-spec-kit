# Slash Command: /marketing.analytics.plan

## Purpose

Generate a comprehensive analytics report for a marketing plan, aggregating metrics across all campaigns.

## Command Usage

```
/marketing.analytics.plan <plan_id> [start_date] [end_date]
```

## Prerequisites

- Plan must exist
- At least one campaign under the plan should be completed or active
- Campaign metrics available

## Execution Steps

### Step 1: Read Plan Context

Load plan details:
- Objectives
- Budget
- KPIs
- All campaigns under this plan

### Step 2: Aggregate Campaign Metrics

Sum/average metrics across all campaigns:
- Total impressions, reach, engagement
- Total conversions, revenue
- Total spend vs budget
- Average performance metrics

### Step 3: Compare Against Plan KPIs

For each plan KPI, calculate:
- **Target** (from plan.kpis)
- **Actual** (aggregated from campaigns)
- **Achievement %**
- **Status**

### Step 4: AI-Generated Insights

Generate plan-level insights:

**Success Insights**:
- "Plan objective achieved: 12K signups vs 10K target (+20%)"
- "Budget efficiency: $16 CPA vs $20 target (-20% cost)"

**Concern Insights**:
- "Objective missed: 35K brand impressions vs 50K target (-30%)"
- "Campaign 2 underperformed, dragged down overall results"

**Opportunity Insights**:
- "B2B campaigns performed 2x better, shift focus for Q1"
- "Tutorial content has 4x ROI vs other formats"

### Step 5: Campaign Performance Comparison

Rank campaigns by performance:
```markdown
| Campaign | Budget | Conversions | CPA | ROI | Status |
|----------|--------|-------------|-----|-----|--------|
| Launch Awareness | $2,000 | 120 | $16.67 | 300% | ✅ Excellent |
| Retargeting | $1,500 | 80 | $18.75 | 250% | ✅ Good |
| Email Nurture | $500 | 60 | $8.33 | 500% | ⭐ Outstanding |
```

### Step 6: Output Analytics Report

```yaml
analytics:
  - id: "analytics-q4-plan-final"
    type: "plan"
    entity_id: "q4-2025-growth-plan"
    period:
      start_date: "2025-10-01"
      end_date: "2025-12-31"
    metrics:
      total_spend: 4900
      total_impressions: 150000
      total_engagements: 7500
      total_clicks: 3000
      total_conversions: 260
      revenue: 65000
    vs_target:
      brand_awareness:
        target: 50000
        actual: 150000
        achievement: 300
        status: "exceeds"
      signups:
        target: 10000
        actual: 260
        achievement: 2.6
        status: "far_below"
      revenue:
        target: 100000
        actual: 65000
        achievement: 65
        status: "below_target"
    insights:
      - type: "success"
        description: "Brand awareness tripled target"
        evidence: "150K impressions vs 50K target across 3 campaigns"
        recommendation: "Maintain awareness strategy for Q1"
      
      - type: "concern"
        description: "Signup conversions critically low"
        evidence: "260 signups vs 10K target (97.4% miss)"
        recommendation: "Fundamental funnel issue: conduct user research"
      
      - type: "opportunity"
        description: "Email nurture campaign showed 5x ROI"
        evidence: "$500 spend, 60 conversions, $30K revenue"
        recommendation: "Allocate 30% of Q1 budget to email"
    
    optimizations:
      - priority: "high"
        action: "Conduct user research to understand conversion barriers"
        expected_impact: "Identify funnel drop-off points"
        effort: "medium"
      
      - priority: "high"
        action: "Shift Q1 budget: 30% email, 20% retargeting, 50% awareness"
        expected_impact: "Improve overall plan ROI by 40%"
        effort: "low"
      
      - priority: "medium"
        action: "A/B test signup flow (current conversion rate: 0.17%)"
        expected_impact: "Double conversion rate to 0.34%"
        effort: "high"
    
    generated_at: "2026-01-05T10:00:00Z"
```

```markdown
## Plan Analytics Report

**Plan**: Q4 2025 Growth Plan
**Period**: Oct 1 - Dec 31, 2025 (13 weeks)
**Budget**: $4,900 / $5,000 (98% spent)
**Campaigns**: 3

---

### 📊 Plan Objectives Performance

| Objective | Target | Actual | Achievement | Status |
|-----------|--------|--------|-------------|--------|
| Brand Awareness | 50K impressions | 150K | 300% | ✅ Tripled |
| New Signups | 10,000 users | 260 | 2.6% | ❌ Critical Miss |
| Revenue | $100K | $65K | 65% | ⚠️ Below Target |

**Overall Plan Status**: ⚠️ Mixed Results - 1/3 objectives met

---

### 💰 Financial Summary

- **Total Spend**: $4,900
- **Total Revenue**: $65,000
- **ROAS**: 13.3x (Excellent)
- **Cost Per Conversion**: $18.85
- **Budget Efficiency**: 98% utilized

---

### 📈 Campaign Performance Comparison

| Campaign | Duration | Spend | Conversions | CPA | ROI | Grade |
|----------|----------|-------|-------------|-----|-----|-------|
| Email Nurture | 4 weeks | $500 | 60 | $8.33 | 60x | ⭐ A+ |
| Launch Awareness | 3 weeks | $2,000 | 120 | $16.67 | 15x | ✅ A |
| Retargeting | 6 weeks | $1,500 | 80 | $18.75 | 10x | ✅ B+ |

**Best Performer**: Email Nurture (lowest CPA, highest ROI)
**Worst Performer**: Retargeting (highest CPA, lowest ROI)

---

### 💡 Key Insights

#### ✅ Successes
1. **Exceptional Brand Awareness**: 3x target with viral content
2. **Strong ROAS**: 13.3x return, well above 3x target
3. **Email Channel Discovery**: Email nurture had 5x better ROI than paid

#### ❌ Critical Issues
1. **Signup Catastrophe**: 260 vs 10K target (97.4% miss)
   - **Root Cause**: Awareness didn't convert to action
   - **Funnel Analysis**: 0.17% conversion rate (industry avg: 2-5%)

2. **Revenue Shortfall**: $65K vs $100K target
   - **Linked to**: Low signup numbers
   - **Impact**: 35% revenue gap

3. **Strategy Mismatch**: Heavy awareness focus, weak conversion tactics
   - **Observation**: 40% budget on awareness, only 10% on email (best performer)

#### 🎯 Opportunities
1. **Email Channel**: Proven 5x ROI, dramatically underinvested
2. **Conversion Optimization**: Massive opportunity (current 0.17% vs 2% target)
3. **Budget Reallocation**: Shift from awareness to conversion campaigns

---

### 🚀 Optimization Recommendations

#### 🔴 Critical (Q1 Priority)
1. **Conduct User Research** (Week 1)
   - **Problem**: 97% signup miss indicates fundamental issue
   - **Action**: User interviews, session recordings, drop-off analysis
   - **Expected Impact**: Identify conversion barriers
   - **Effort**: Medium (2-3 weeks)

2. **Redesign Signup Flow** (Week 4-6)
   - **Problem**: 0.17% conversion vs 2% industry avg
   - **Action**: A/B test simplified 2-step signup vs current 5-step
   - **Expected Impact**: 10x conversion improvement (0.17% → 1.7%)
   - **Effort**: High (development required)

#### 🟡 Important (Q1 Execution)
3. **Reallocate Q1 Budget**
   - **Current**: 40% awareness, 30% retargeting, 10% email, 20% other
   - **Proposed**: 30% email, 30% conversion campaigns, 20% retargeting, 20% awareness
   - **Expected Impact**: +40% overall ROI
   - **Effort**: Low (planning only)

4. **Scale Email Nurture**
   - **Evidence**: $500 → $30K revenue (60x ROI)
   - **Action**: Increase email budget from $500 to $1,500
   - **Expected Impact**: 3x conversions from email channel
   - **Effort**: Low (scale existing campaign)

#### 🟢 Nice-to-Have (Q1 Experiments)
5. **Explore Retargeting Optimization**
   - **Current**: $18.75 CPA (highest)
   - **Action**: Experiment with dynamic retargeting ads
   - **Expected Impact**: -20% CPA
   - **Effort**: Medium

---

### 🎓 Lessons Learned

1. **Awareness ≠ Conversions**: Generated 3x impressions but <3% signups
2. **Email Undervalued**: Smallest budget, highest ROI (60x)
3. **Conversion Funnel Broken**: 0.17% rate vs 2-5% industry standard
4. **Budget Allocation Error**: 40% on awareness, only 10% on best channel

---

### 📋 Q1 2026 Plan Recommendations

Based on Q4 learnings, propose Q1 plan with:

**Objectives** (Revised Priorities):
1. Fix conversion funnel (0.17% → 2%)
2. Scale email channel (proven 60x ROI)
3. Maintain brand awareness (Q4 success)

**Budget Allocation**:
- 30% Email nurture campaigns
- 30% Conversion optimization & landing pages
- 20% Retargeting (optimized)
- 20% Brand awareness (maintain momentum)

**Success Metrics**:
- Signup conversion rate: 0.17% → 2% (10x improvement)
- Total signups: 10,000 (vs Q4's 260)
- ROAS: Maintain 13x+ 

---

**Report Generated**: 2026-01-05 10:00 UTC
```

## Success Criteria

- All plan-level KPIs analyzed
- Campaign performance compared
- Actionable recommendations for next plan period
- Lessons learned documented

## Example Interaction

```
User: /marketing.analytics.plan q4-2025-growth-plan

AI: Generating plan analytics for 'q4-2025-growth-plan'...

Analyzing 3 campaigns across 13 weeks...

[Displays complete analytics report]

📊 Plan Performance: 1/3 objectives met
🚨 Critical Issue: Signup conversion 97% below target
⭐ Hidden Gem: Email channel with 60x ROI

Top Recommendation: Conduct user research to fix conversion funnel

Would you like me to:
A) Create a Q1 plan based on these learnings
B) Design a conversion optimization campaign
C) Generate a stakeholder presentation
```

