# Slash Command: /marketing.analytics.campaign

## Purpose

Generate an analytics report for a completed or active campaign, including KPI performance, insights, and optimization recommendations.

## Command Usage

```
/marketing.analytics.campaign <campaign_id> [start_date] [end_date]
```

## Prerequisites

- Campaign must exist
- Actual metrics data available (from user input or tools)

## Execution Steps

### Step 1: Read Campaign Context

Load campaign details:
- Expected KPIs
- Budget
- Timeline
- Goal

### Step 2: Gather Actual Metrics

Ask user for actual performance data:
- Impressions, reach, engagement
- Click-through rate, conversions
- Cost per metric (CPC, CPM, CPA)
- Revenue (if conversion campaign)

### Step 3: Calculate KPI Comparisons

For each KPI, calculate:
- **Target** vs **Actual**
- **Achievement %**: (Actual / Target) × 100
- **Status**: exceeds (>110%), meets (90-110%), on_track (70-90%), below_target (50-70%), far_below (<50%)

### Step 4: AI-Generated Insights

Analyze data to produce 3-10 insights:

**Success Insights** (what worked well):
- "Twitter engagement 150% of target due to viral thread"
- "Dev.to tutorial drove 40% of all conversions"

**Concern Insights** (what underperformed):
- "Reddit post removed by moderators, 0 reach"
- "CTR 30% below target, creative may need refresh"

**Opportunity Insights** (what to do next):
- "High engagement on feature X, consider dedicated campaign"
- "B2B segment converted 3x better than B2C"

### Step 5: Generate Optimization Recommendations

Provide 3-10 prioritized recommendations:

**High Priority** (immediate action):
- "Pause underperforming Reddit ads, reallocate $500 to Twitter"
- "A/B test new headlines (current CTR: 1.2%, target: 2%)"

**Medium Priority** (near-term improvements):
- "Create more tutorial content (highest conversion content type)"
- "Increase posting frequency on Twitter (best engagement channel)"

**Low Priority** (nice-to-have):
- "Experiment with video content for next campaign"

### Step 6: Output Analytics Report

```yaml
analytics:
  - id: "analytics-q4-awareness-1"
    type: "campaign"
    entity_id: "q4-awareness-launch"
    period:
      start_date: "2025-10-01"
      end_date: "2025-10-21"
    metrics:
      impressions: 45000
      engagements: 1800
      clicks: 900
      conversions: 120
      spend: 1950
    vs_target:
      impressions:
        target: 30000
        actual: 45000
        achievement: 150
        status: "exceeds"
      engagement_rate:
        target: 0.03
        actual: 0.04
        achievement: 133
        status: "exceeds"
      click_through_rate:
        target: 0.02
        actual: 0.012
        achievement: 60
        status: "below_target"
      conversions:
        target: 100
        actual: 120
        achievement: 120
        status: "exceeds"
    insights:
      - type: "success"
        description: "Impressions exceeded target by 50%"
        evidence: "Twitter thread went viral (15K impressions alone)"
        recommendation: "Replicate thread format in future campaigns"
      
      - type: "concern"
        description: "Click-through rate 40% below target"
        evidence: "CTR: 1.2% vs target 2%, despite high impressions"
        recommendation: "A/B test new call-to-action copy"
      
      - type: "opportunity"
        description: "Tutorial content drives highest conversions"
        evidence: "Dev.to tutorials: 60% of conversions from 20% of traffic"
        recommendation: "Double down on educational content"
    
    optimizations:
      - priority: "high"
        action: "A/B test 3 new headline variations for Twitter posts"
        expected_impact: "Increase CTR from 1.2% to 1.8%"
        effort: "low"
      
      - priority: "high"
        action: "Pause Reddit campaigns (0 ROI), reallocate $500"
        expected_impact: "Save $500, reinvest in Twitter"
        effort: "low"
      
      - priority: "medium"
        action: "Create 2 more tutorial articles for Dev.to"
        expected_impact: "Increase conversions by 30%"
        effort: "medium"
      
      - priority: "low"
        action: "Experiment with short-form video on Twitter"
        expected_impact: "Potentially higher engagement"
        effort: "high"
    
    generated_at: "2025-10-22T10:00:00Z"
```

```markdown
## Campaign Analytics Report

**Campaign**: Q4 Product Launch Awareness Campaign
**Period**: Oct 1-21, 2025
**Budget**: $1,950 / $2,000 (97.5% spent)

---

### 📊 Performance Summary

| Metric | Target | Actual | Achievement | Status |
|--------|--------|--------|-------------|--------|
| Impressions | 30,000 | 45,000 | 150% | ✅ Exceeds |
| Engagement Rate | 3.0% | 4.0% | 133% | ✅ Exceeds |
| Click-Through Rate | 2.0% | 1.2% | 60% | ⚠️ Below Target |
| Conversions | 100 | 120 | 120% | ✅ Exceeds |

**Overall**: 3/4 metrics met or exceeded ✅

---

### 💡 Key Insights

#### ✅ Successes
1. **Viral Twitter Thread**: One thread generated 15K impressions (50% of Twitter total)
2. **Tutorial Power**: Dev.to tutorials drove 60% of conversions despite being 20% of traffic
3. **Conversion Performance**: 120 conversions exceeded target by 20%

#### ⚠️ Concerns
1. **Low Click-Through Rate**: 1.2% CTR vs 2% target despite high impressions
2. **Reddit Failure**: Post removed by moderators, $300 wasted
3. **Channel Imbalance**: Twitter dominated, other channels underutilized

#### 🎯 Opportunities
1. **Double Down on Education**: Tutorial content has 3x conversion rate vs other types
2. **Thread Format**: Replicate successful Twitter thread structure
3. **Audience Segment**: B2B converted 3x better than B2C

---

### 🚀 Optimization Recommendations

#### 🔴 High Priority (Implement Now)
1. **A/B Test Headlines**: Current CTR is 40% below target
   - **Action**: Test 3 new headline variations
   - **Expected Impact**: CTR 1.2% → 1.8%
   - **Effort**: Low (2 hours)

2. **Reallocate Reddit Budget**: $500 wasted, 0 ROI
   - **Action**: Pause Reddit, move budget to Twitter
   - **Expected Impact**: Better ROI, reach 60K impressions
   - **Effort**: Low (immediate)

#### 🟡 Medium Priority (Next 2 Weeks)
3. **Create More Tutorials**: Educational content = high conversion
   - **Action**: Publish 2 more Dev.to tutorials
   - **Expected Impact**: +30% conversions
   - **Effort**: Medium (20 hours)

4. **B2B Targeting**: B2B segment outperformed B2C
   - **Action**: Create B2B-focused content for next campaign
   - **Expected Impact**: Higher conversion rates
   - **Effort**: Medium (planning required)

#### 🟢 Low Priority (Future Consideration)
5. **Video Experimentation**: Explore short-form video on Twitter
   - **Action**: Create 1-2 test videos
   - **Expected Impact**: Unknown, potentially higher engagement
   - **Effort**: High (new capability)

---

### 📈 ROI Analysis

- **Total Spend**: $1,950
- **Conversions**: 120
- **Cost Per Conversion**: $16.25
- **Revenue** (if applicable): [User input needed]
- **ROAS** (if applicable): [Calculate when revenue provided]

---

**Report Generated**: 2025-10-22 10:00 UTC
```

## Success Criteria

- All metrics compared to targets
- At least 3 insights generated
- Optimization recommendations prioritized
- Actionable next steps provided

## Example Interaction

```
User: /marketing.analytics.campaign q4-awareness-launch

AI: Generating analytics report for 'q4-awareness-launch'...

I'll need actual performance data. Please provide:
1. Impressions: 45000
2. Engagements: 1800
3. Clicks: 900
4. Conversions: 120
5. Total Spend: $1950

[After gathering data]

[Displays complete analytics report with YAML + markdown summary]

📊 Performance: 3/4 metrics met
🎯 Top Priority: A/B test headlines (CTR below target)
💰 Quick Win: Reallocate $500 from Reddit to Twitter

Would you like me to:
A) Create an optimization plan for next campaign
B) Generate a summary for stakeholders
C) Update the campaign spec with learnings
```

