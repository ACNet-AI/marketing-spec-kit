---
name: marketspec.review
description: Analyze actual campaign performance vs. planned
layer: sdm
status: implemented
type: extension
category: Extension (Feedback Loop)
source: Original to marketing-spec-kit
version: 0.3.0
---

# /marketspec.review 🔵 Extension

**Purpose**: Analyze actual campaign performance after execution and compare against planned objectives.

**Category**: Extension (Feedback Loop)  
**Timing**: POST-EXECUTION  
**Note**: Original to marketing-spec-kit (no MetaSpec equivalent)

---

## Purpose

After campaign execution, this command helps you:
- Compare actual results vs planned objectives
- Analyze KPI achievement rates
- Review budget execution
- Identify success factors
- Document lessons learned
- Prepare insights for optimization

This is an **Extension Command** - run after campaign execution to enable data-driven optimization.

---

## Command Usage

```
/marketspec.review
/marketspec.review --data-source analytics.json
/marketspec.review --period "2025-01-15 to 2025-03-31"
```

**Examples**:
```
/marketspec.review
/marketspec.review --data-source google-analytics-export.json
/marketspec.review --period "Q1 2025"
```

---

## Prerequisites

- **Required**: Original spec `marketing-spec.yaml`
- **Required**: Campaign completed or in progress
- **Recommended**: Analytics data (GA, social media, email metrics)
- **Recommended**: Actual spend data
- **Optional**: Team feedback

---

## Execution Steps

### Step 1: Load Original Plan

Read the original specification:

```yaml
original_plan:
  name: "metaspec-developer-onboarding"
  version: "1.0.0"
  
  objectives:
    - name: "GitHub Stars"
      baseline: 50
      target: 500
      timeline: "11 weeks"
    
    - name: "Email Subscribers"
      baseline: 100
      target: 1000
      timeline: "11 weeks"
    
    - name: "Website Traffic"
      baseline: 500
      target: 50000
      timeline: "11 weeks"
  
  budget:
    total: 10000
    breakdown:
      content_creation: 4000
      paid_promotion: 3000
      tools: 1500
      community: 1000
      contingency: 500
  
  timeline:
    start: "2025-01-15"
    end: "2025-03-31"
    duration: "11 weeks"
  
  campaigns: 2
  channels: 5
  content_pieces: 12
```

### Step 2: Collect Actual Performance Data

**Interactive Prompts**:

```
📊 Let's review your campaign performance!

I've loaded your original plan: "metaspec-developer-onboarding"
Period: 2025-01-15 to 2025-03-31 (11 weeks)

---

**KPI Performance**

1️⃣ GitHub Stars
   Planned: 50 → 500 (+450)
   Actual: ?
   
   > Please provide actual GitHub stars at end of campaign: _____

2️⃣ Email Subscribers
   Planned: 100 → 1000 (+900)
   Actual: ?
   
   > Please provide actual email subscribers: _____

3️⃣ Website Traffic (visits)
   Planned: 500 → 50,000 (+49,500)
   Actual: ?
   
   > Please provide total website visits: _____

---

**Budget Execution**

Planned Total: $10,000
Actual Spent: ?

> Please provide total actual spend: _____

Or provide breakdown:
- Content Creation (planned: $4,000): _____
- Paid Promotion (planned: $3,000): _____
- Tools (planned: $1,500): _____
- Community (planned: $1,000): _____
- Other: _____

---

**Data Sources** (optional)

Do you have analytics exports?
- [ ] Google Analytics JSON
- [ ] Social media reports
- [ ] Email marketing data
- [ ] Other

> Upload or paste data here: _____
```

**Example Input**:

```yaml
actual_performance:
  kpis:
    github_stars:
      actual: 420
      planned: 500
      
    email_subscribers:
      actual: 850
      planned: 1000
      
    website_traffic:
      actual: 45000
      planned: 50000
  
  budget:
    total_spent: 9500
    planned: 10000
    breakdown:
      content_creation: 3800
      paid_promotion: 3200
      tools: 1500
      community: 800
      contingency: 200
  
  timeline:
    actual_start: "2025-01-15"
    actual_end: "2025-03-31"
    completed_on_time: true
```

### Step 3: Calculate Achievement Rates

Compare actual vs planned:

```yaml
achievement_analysis:
  kpis:
    - name: "GitHub Stars"
      baseline: 50
      target: 500
      planned_growth: 450
      actual: 420
      actual_growth: 370
      achievement_rate: 82.2%  # (370/450)
      status: "⚠️ Below target"
      delta: -80 stars
      
    - name: "Email Subscribers"
      baseline: 100
      target: 1000
      planned_growth: 900
      actual: 850
      actual_growth: 750
      achievement_rate: 83.3%  # (750/900)
      status: "⚠️ Below target"
      delta: -150 subscribers
      
    - name: "Website Traffic"
      baseline: 500
      target: 50000
      planned_growth: 49500
      actual: 45000
      actual_growth: 44500
      achievement_rate: 89.9%  # (44500/49500)
      status: "⚠️ Below target"
      delta: -5000 visits
  
  overall_kpi_achievement: 85.1%  # Average
  
  budget:
    planned: 10000
    spent: 9500
    utilization: 95%
    status: "✅ Under budget"
    saved: 500
  
  timeline:
    planned_duration: "11 weeks"
    actual_duration: "11 weeks"
    status: "✅ On time"
```

### Step 4: Channel Performance Analysis

Analyze which channels performed best:

```yaml
channel_analysis:
  - channel: "dev-blog"
    metrics:
      traffic: 15000 visits
      conversions: 200 email signups
      conversion_rate: 1.33%
      budget: 1500
      cost_per_conversion: 7.5
      status: "✅ Strong performer"
      roi_score: 8/10
    
  - channel: "dev-twitter"
    metrics:
      impressions: 500000
      engagements: 5000
      engagement_rate: 1%
      github_referrals: 150
      budget: 1200
      cost_per_github_star: 8
      status: "✅ Good performer"
      roi_score: 7/10
    
  - channel: "dev-to"
    metrics:
      views: 25000
      reactions: 800
      github_referrals: 100
      budget: 800
      cost_per_github_star: 8
      status: "✅ Efficient"
      roi_score: 8/10
    
  - channel: "reddit-programming"
    metrics:
      posts: 12
      upvotes: 450
      traffic: 8000
      github_referrals: 80
      budget: 500
      cost_per_github_star: 6.25
      status: "✅ Best ROI"
      roi_score: 9/10
    
  - channel: "linkedin-tech"
    metrics:
      impressions: 50000
      clicks: 500
      click_rate: 1%
      conversions: 50
      budget: 1000
      cost_per_conversion: 20
      status: "⚠️ Underperformed"
      roi_score: 4/10
  
  top_performers:
    - "reddit-programming" (best ROI)
    - "dev-to" (efficient)
    - "dev-blog" (strong conversions)
  
  underperformers:
    - "linkedin-tech" (high cost, low conversion)
```

### Step 5: Content Performance Analysis

Identify which content worked best:

```yaml
content_analysis:
  top_performing:
    - title: "Building Your First MetaSpec - Tutorial"
      type: "Tutorial"
      channel: "dev-blog"
      views: 5000
      github_referrals: 80
      shares: 150
      performance_score: 9/10
      success_factors:
        - "Practical hands-on approach"
        - "Clear step-by-step instructions"
        - "Solved real developer pain point"
    
    - title: "How We Automated Our Spec Process with MetaSpec"
      type: "Case Study"
      channel: "dev-to"
      views: 8000
      reactions: 300
      github_referrals: 60
      performance_score: 8/10
      success_factors:
        - "Real-world use case"
        - "Quantified results"
        - "Relatable developer workflow"
    
    - title: "MetaSpec vs Manual Documentation: A Comparison"
      type: "Comparison"
      channel: "reddit-programming"
      upvotes: 200
      comments: 45
      traffic: 3000
      performance_score: 8/10
      success_factors:
        - "Addressed common skepticism"
        - "Data-driven comparison"
        - "Sparked discussion"
  
  underperforming:
    - title: "MetaSpec 2.0 Release Notes"
      type: "Announcement"
      channel: "linkedin-tech"
      views: 500
      engagements: 10
      performance_score: 3/10
      issues:
        - "Too technical for LinkedIn audience"
        - "No clear value proposition"
        - "Poor timing (posted during holidays)"
  
  content_insights:
    - "Tutorials and case studies outperformed announcements 3:1"
    - "Dev.to and Reddit audiences prefer deep technical content"
    - "LinkedIn requires more business-focused messaging"
    - "Step-by-step guides generated 2x more GitHub referrals"
```

### Step 6: Identify Success Factors

What worked well:

```yaml
success_factors:
  strategy:
    - factor: "Developer-first content approach"
      impact: "High"
      evidence: "Tutorial posts got 2x engagement vs promotional"
      replicable: true
      
    - factor: "Community-driven distribution"
      impact: "High"
      evidence: "Reddit and Dev.to drove 60% of GitHub traffic"
      replicable: true
      
    - factor: "Consistent posting schedule"
      impact: "Medium"
      evidence: "Weeks with 3+ posts averaged 30% higher traffic"
      replicable: true
  
  content:
    - factor: "Hands-on tutorials with code examples"
      impact: "High"
      evidence: "Highest GitHub referral rate (5%)"
      replicable: true
      
    - factor: "Real-world case studies"
      impact: "High"
      evidence: "Highest email conversion rate (2.5%)"
      replicable: true
  
  channels:
    - factor: "Reddit timing (Tuesday/Wednesday morning)"
      impact: "Medium"
      evidence: "3x more upvotes vs other days"
      replicable: true
      
    - factor: "Dev.to series format"
      impact: "Medium"
      evidence: "Follow-through rate 40% higher"
      replicable: true
  
  execution:
    - factor: "Rapid response to comments"
      impact: "High"
      evidence: "Posts with <1hr response time got 2x engagement"
      replicable: true
```

### Step 7: Document Lessons Learned

What didn't work and why:

```yaml
lessons_learned:
  challenges:
    - challenge: "LinkedIn underperformed expectations"
      planned_roi: 6/10
      actual_roi: 4/10
      root_causes:
        - "Audience mismatch: Too technical for decision-makers"
        - "Content format: Long-form didn't fit platform"
        - "Timing: Posted during slow periods"
      lesson: "LinkedIn needs business-value messaging, not technical deep dives"
      action_for_next_time: "Create separate content track for LinkedIn focused on ROI/efficiency"
      
    - challenge: "Email conversion slower than expected"
      planned: 1000
      actual: 850
      root_causes:
        - "No dedicated lead magnet"
        - "Email signup CTA buried in posts"
        - "No email nurture sequence"
      lesson: "Email growth needs dedicated tactics, not just passive signups"
      action_for_next_time: "Create lead magnet, optimize CTAs, build nurture sequence"
      
    - challenge: "GitHub stars growth plateaued in week 8"
      weeks_1_7_avg: 45/week
      weeks_8_11_avg: 20/week
      root_causes:
        - "Content fatigue: Same format repeated"
        - "No re-engagement campaigns"
        - "Low community engagement"
      lesson: "Growth requires variety and ongoing engagement, not just content volume"
      action_for_next_time: "Plan content variety, add community engagement tactics"
  
  surprises:
    - surprise: "Reddit performed 2x better than expected"
      impact: "Positive"
      insight: "Technical communities highly receptive to well-explained tools"
      
    - surprise: "Tutorial content outperformed case studies"
      impact: "Positive"
      insight: "Developers want hands-on learning over success stories"
      
    - surprise: "Weekend traffic was negligible"
      impact: "Neutral"
      insight: "Developer marketing is B2B workday-driven, not 24/7"
```

### Step 8: Calculate ROI and Efficiency

Overall campaign effectiveness:

```yaml
roi_analysis:
  investment:
    budget: 9500
    team_hours: 220
    team_cost_estimate: 11000  # At $50/hr average
    total_investment: 20500
  
  returns:
    github_stars:
      achieved: 370
      value_per_star: 50  # Estimated based on open-source project value
      estimated_value: 18500
    
    email_subscribers:
      achieved: 750
      value_per_subscriber: 15  # Estimated LTV
      estimated_value: 11250
    
    website_traffic:
      achieved: 44500
      value_per_visit: 0.50  # Engagement value
      estimated_value: 22250
    
    total_estimated_value: 52000
  
  roi_calculation:
    total_investment: 20500
    total_value: 52000
    net_value: 31500
    roi_percentage: 154%
    status: "✅ Positive ROI"
  
  efficiency_metrics:
    cost_per_github_star: 25.68  # 9500/370
    cost_per_email_subscriber: 12.67  # 9500/750
    cost_per_1000_visits: 213.48  # 9500/(44500/1000)
    
    budget_efficiency: 95%  # Spent vs planned
    goal_efficiency: 85.1%  # Achievement vs target
    
    overall_efficiency_score: 8.2/10
```

### Step 9: Generate Campaign Review Report

Create comprehensive review document:

```markdown
# Campaign Review Report

**Campaign**: MetaSpec Developer Onboarding  
**Period**: 2025-01-15 to 2025-03-31 (11 weeks)  
**Status**: Completed On Time  
**Generated**: 2025-04-05

---

## Executive Summary

Campaign achieved **85.1% of planned objectives** with **95% budget utilization** and **154% ROI**.

**Key Results**:
- ⚠️ GitHub Stars: 420 (84% of target)
- ⚠️ Email Subscribers: 850 (85% of target)
- ⚠️ Website Traffic: 45K (90% of target)
- ✅ Budget: $9,500 spent (saved $500)
- ✅ Timeline: Completed on schedule

**Overall Grade**: B+ (Strong performance with room for improvement)

---

## KPI Achievement

| Objective | Baseline | Target | Actual | Achievement | Status |
|-----------|----------|--------|--------|-------------|--------|
| GitHub Stars | 50 | 500 | 420 | 82.2% | ⚠️ Below |
| Email Subscribers | 100 | 1,000 | 850 | 83.3% | ⚠️ Below |
| Website Traffic | 500 | 50,000 | 45,000 | 89.9% | ⚠️ Below |

**Average Achievement**: 85.1%

**Analysis**: All KPIs moved in the right direction but fell short of ambitious targets. Most growth happened in first 7 weeks, with plateau in final 4 weeks.

---

## Budget Performance

**Total Budget**: $10,000  
**Total Spent**: $9,500 (95%)  
**Saved**: $500

| Category | Planned | Actual | Variance |
|----------|---------|--------|----------|
| Content Creation | $4,000 | $3,800 | -$200 (5%) |
| Paid Promotion | $3,000 | $3,200 | +$200 (7%) |
| Tools | $1,500 | $1,500 | $0 (0%) |
| Community | $1,000 | $800 | -$200 (20%) |
| Contingency | $500 | $200 | -$300 (60%) |

**Analysis**: Budget well-managed. Slight overspend on paid promotion compensated by underspend on community and contingency.

---

## Channel Performance

### Top Performers (Keep & Expand)

1. **Reddit (r/programming)** - ROI: 9/10
   - Best cost-per-star: $6.25
   - 80 GitHub referrals from 12 posts
   - Success factor: Technical depth resonated

2. **Dev.to** - ROI: 8/10
   - 25K views, 100 GitHub referrals
   - Strong developer community engagement
   - Series format worked well

3. **Developer Blog** - ROI: 8/10
   - Highest email conversion: 1.33%
   - 200 subscribers from 15K visits
   - Owned channel, sustainable long-term

### Underperformers (Optimize or Cut)

1. **LinkedIn** - ROI: 4/10
   - Highest cost-per-conversion: $20
   - Wrong audience fit
   - **Recommendation**: Pivot to business-value messaging or reduce investment

---

## Content Insights

### What Worked ✅

- **Tutorials**: 2x engagement vs announcements
- **Case studies**: Highest email conversion (2.5%)
- **Hands-on code examples**: 5% GitHub referral rate
- **Consistent 3x/week posting**: 30% higher traffic

### What Didn't Work ❌

- **Product announcements**: Low engagement
- **LinkedIn technical content**: Audience mismatch
- **Weekend posting**: Negligible traffic
- **Repetitive formats**: Growth plateau after week 7

### Content Performance Summary

| Content Type | Count | Avg Views | GitHub Referrals | Performance |
|--------------|-------|-----------|------------------|-------------|
| Tutorials | 5 | 4,000 | 250 (50/ea) | ✅ Excellent |
| Case Studies | 4 | 6,000 | 150 (37.5/ea) | ✅ Strong |
| Comparisons | 2 | 3,500 | 80 (40/ea) | ✅ Good |
| Announcements | 3 | 800 | 20 (6.7/ea) | ❌ Poor |

---

## Success Factors (Replicate These)

1. **Developer-first content** → 2x engagement
2. **Community-driven distribution** → 60% of traffic
3. **Rapid comment response** (<1hr) → 2x engagement
4. **Tuesday/Wednesday Reddit posting** → 3x upvotes
5. **Hands-on tutorials** → Highest conversion
6. **Dev.to series format** → 40% higher follow-through

---

## Lessons Learned

### What We'll Do Differently Next Time

1. **Email Growth**
   - Problem: No dedicated lead magnet
   - Solution: Create downloadable guide or template
   - Expected impact: +30% email growth

2. **LinkedIn Strategy**
   - Problem: Too technical for audience
   - Solution: Business-value focused content
   - Expected impact: 2x LinkedIn ROI

3. **Content Variety**
   - Problem: Format repetition caused plateau
   - Solution: Mix formats (video, interactive, guest posts)
   - Expected impact: Sustain growth through week 11

4. **Community Engagement**
   - Problem: One-way content distribution
   - Solution: Active participation in discussions
   - Expected impact: +20% GitHub stars

---

## ROI Analysis

**Total Investment**: $20,500
- Budget: $9,500
- Team time: $11,000 (220 hrs @ $50/hr)

**Estimated Value Generated**: $52,000
- GitHub stars value: $18,500
- Email subscriber value: $11,250
- Website traffic value: $22,250

**Net ROI**: 154% ($31,500 net value)

**Efficiency Score**: 8.2/10

---

## Timeline Analysis

**Execution**: ✅ Completed on time (11 weeks)

**Growth Pattern**:
- Weeks 1-4: Slow ramp-up (avg 25 stars/week)
- Weeks 5-7: Peak growth (avg 60 stars/week)
- Weeks 8-11: Plateau (avg 20 stars/week)

**Insight**: Need sustained engagement tactics to prevent mid-campaign plateau.

---

## Team Performance

**Roles**:
- Content Writer: 80 hrs (efficient)
- Social Media Manager: 220 hrs (as planned)
- Designer: 88 hrs (on target)
- Marketing Lead: 110 hrs (on target)

**Efficiency**: ✅ Team capacity well-utilized

---

## Recommendations for Next Campaign

Based on this review, here's what to do next:

### Immediate Actions (Next 2 Weeks)
1. Create email lead magnet based on top-performing tutorial
2. Optimize email signup CTAs on blog
3. Build 5-email nurture sequence

### Strategic Changes (Next Campaign)
1. Double down on Reddit, Dev.to, and Blog
2. Reduce LinkedIn investment by 50% or pivot strategy
3. Add content variety to prevent fatigue
4. Introduce community engagement tactics
5. Plan re-engagement campaigns for weeks 8-11

### Budget Adjustments
- Reddit: +$500 (increase from $500 to $1,000)
- Dev.to: +$300 (increase from $800 to $1,100)
- LinkedIn: -$500 (decrease from $1,000 to $500)
- Email tools: +$200 (for lead magnet and automation)

---

## Next Steps

1. **Share report** with team for feedback
2. **Run /marketspec.optimize** to get AI-powered recommendations
3. **Plan Q2 campaign** incorporating these lessons
4. **Archive this campaign** for future reference

---

**Report prepared by**: Marketing AI Assistant  
**Data sources**: Campaign tracking, Analytics, Team input  
**Confidence level**: High (based on actual data)
```

**Output Location**: `campaign-review.md`

---

## Success Criteria

- ✅ Original plan loaded and parsed
- ✅ Actual performance data collected
- ✅ Achievement rates calculated for all KPIs
- ✅ Channel performance analyzed
- ✅ Content effectiveness evaluated
- ✅ Success factors identified
- ✅ Lessons learned documented
- ✅ ROI calculated
- ✅ Actionable recommendations provided

---

## Output

**Primary Output**: `campaign-review.md`

**Structure**:
```
project-root/
├── marketing-spec.yaml           # Original plan
└── campaign-review.md            # Review report (NEW)
```

---

## Error Handling

**Missing Original Spec**:
```
❌ Error: Cannot find marketing-spec.yaml
→ This command requires the original specification to compare against
→ Run /marketspec.create first or provide spec file location
```

**Incomplete Data**:
```
⚠️ Warning: Some metrics not provided
→ Review will be partial without complete data
→ Provide at minimum: KPIs, budget spent, timeline
```

**Campaign Not Started**:
```
❌ Error: Campaign start date is in the future (2025-11-15)
→ This command should only run after campaign execution begins
→ For pre-launch analysis, use /marketspec.analyze instead
```

---

## Example Interaction

```
User: /marketspec.review

AI: I'll help you review your campaign performance!

📄 **Original Plan Found**: metaspec-developer-onboarding
📅 **Campaign Period**: 2025-01-15 to 2025-03-31 (11 weeks)
🎯 **Planned Objectives**: 3 KPIs

---

Let's collect your actual performance data:

**1. GitHub Stars**
   - Baseline: 50
   - Target: 500
   - Actual: ?
   
   > Please provide your actual GitHub stars: 420

**2. Email Subscribers**
   - Baseline: 100
   - Target: 1,000
   - Actual: ?
   
   > Please provide actual subscribers: 850

**3. Website Traffic**
   - Baseline: 500
   - Target: 50,000
   - Actual: ?
   
   > Please provide total visits: 45000

**4. Budget**
   - Planned: $10,000
   - Actual spent: ?
   
   > Please provide actual spend: 9500

---

✅ **Data collected!** Analyzing performance...

**Achievement Summary**:
- GitHub Stars: 420 (82% of target) ⚠️
- Email Subscribers: 850 (83% of target) ⚠️
- Website Traffic: 45,000 (90% of target) ⚠️
- Budget: $9,500 (95% utilized) ✅

**Overall Achievement**: 85.1%
**ROI**: 154% (Excellent!)
**Grade**: B+ (Strong performance)

---

**Top Performers**:
✅ Reddit - Best ROI (9/10)
✅ Dev.to - Strong engagement (8/10)
✅ Developer Blog - High conversions (8/10)

**Needs Improvement**:
⚠️ LinkedIn - Underperformed (4/10)

**Key Insight**: Tutorial content outperformed announcements 3:1

---

📄 **Full Report Generated**: campaign-review.md

**Recommended Next Step**: Run `/marketspec.optimize` to get AI-powered recommendations for your next campaign based on this data.

Would you like me to:
- Show detailed channel analysis?
- Export report to different format?
- Proceed to /marketspec.optimize?
```

---

## Notes

- **Timing**: Run during or after campaign execution
- **Data Sources**: Combines plan + actuals + analytics
- **Focus**: What happened and why
- **Objective**: Document for learning and improvement
- **Output**: Feeds into `/marketspec.optimize` for recommendations

---

## Integration with Other Commands

**Position**: Extension (AFTER campaign execution)

References:
- `/marketspec.create` - Original specification
- Original campaign documents (discovery, strategy, tasks)

Feeds into:
- `/marketspec.optimize` - Uses review data for optimization recommendations

**Typical Sequence**:
```
create → [Execute Campaign] → review → optimize → [Next Campaign]
```

---

## See Also

- `/marketspec.create` - Original specification
- `/marketspec.optimize` - Next step for optimization recommendations
- `/marketspec.analyze` - For pre-launch consistency checking
- Campaign tracking examples in `examples/` directory

