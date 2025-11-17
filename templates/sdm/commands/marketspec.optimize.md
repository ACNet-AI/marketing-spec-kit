---
name: marketspec.optimize
description: Generate optimization recommendations for next cycle
layer: sdm
status: implemented
type: extension
category: Extension (Feedback Loop)
source: Original to marketing-spec-kit
version: 0.3.0
---

# /marketspec.optimize 🔵 Extension

**Purpose**: Generate AI-powered optimization recommendations based on actual campaign performance data.

**Category**: Extension (Feedback Loop)  
**Timing**: POST-EXECUTION (after review)  
**Note**: Original to marketing-spec-kit (no MetaSpec equivalent)

---

## Purpose

After reviewing campaign performance, this command helps you:
- Identify optimization opportunities
- Generate data-driven recommendations
- Suggest budget reallocation
- Propose channel mix adjustments
- Refine KPI targets
- Create actionable next steps
- Package learnings for next campaign

This is an **Extension Command** - run after `/marketspec.review` to close the optimization loop.

---

## Command Usage

```
/marketspec.optimize
/marketspec.optimize --focus budget
/marketspec.optimize --scenario aggressive
```

**Options**:
- `--focus`: Specific area (budget, channels, content, kpis, all)
- `--scenario`: Optimization scenario (conservative, balanced, aggressive)
- `--next-budget`: Budget for next campaign (for reallocation suggestions)

**Examples**:
```
/marketspec.optimize
/marketspec.optimize --focus channels --scenario aggressive
/marketspec.optimize --next-budget 15000
```

---

## Prerequisites

- **Required**: Campaign review from `/marketspec.review`
- **Required**: Original spec `marketing-spec.yaml`
- **Recommended**: Historical campaign data (if available)
- **Optional**: Business constraints or priorities

---

## Execution Steps

### Step 1: Load Review Data

Read the campaign review report:

```yaml
review_data:
  campaign: "metaspec-developer-onboarding"
  period: "2025-01-15 to 2025-03-31"
  
  achievement:
    overall: 85.1%
    kpis:
      github_stars: 82.2%
      email_subscribers: 83.3%
      website_traffic: 89.9%
  
  budget:
    planned: 10000
    spent: 9500
    efficiency: 95%
  
  roi: 154%
  grade: "B+"
  
  top_channels:
    - name: "reddit"
      roi: 9
      cost_per_star: 6.25
    - name: "dev-to"
      roi: 8
      cost_per_star: 8
    - name: "dev-blog"
      roi: 8
      cost_per_conversion: 7.5
  
  underperforming_channels:
    - name: "linkedin"
      roi: 4
      cost_per_conversion: 20
  
  top_content:
    - type: "tutorial"
      performance: 9
      github_referral_rate: 5%
    - type: "case_study"
      performance: 8
      email_conversion_rate: 2.5%
  
  lessons:
    - "Email growth needs dedicated lead magnet"
    - "LinkedIn requires business-value messaging"
    - "Content variety prevents plateau"
    - "Community engagement sustains growth"
```

### Step 2: Identify Optimization Opportunities

Analyze data for improvement areas:

```yaml
optimization_opportunities:
  high_impact:
    - opportunity: "Reallocate budget from LinkedIn to Reddit"
      current_state: "LinkedIn $1,000 (ROI 4), Reddit $500 (ROI 9)"
      potential_impact: "+50-80 GitHub stars"
      confidence: "High"
      effort: "Low"
      priority: 1
      
    - opportunity: "Create email lead magnet"
      current_state: "No dedicated lead magnet, 850 subscribers"
      potential_impact: "+200-300 email subscribers"
      confidence: "High"
      effort: "Medium"
      priority: 2
      
    - opportunity: "Introduce content variety after week 7"
      current_state: "Growth plateau in weeks 8-11"
      potential_impact: "Sustain 60 stars/week through week 11"
      confidence: "Medium"
      effort: "Medium"
      priority: 3
  
  medium_impact:
    - opportunity: "Add community engagement tactics"
      potential_impact: "+15-20% GitHub stars"
      confidence: "Medium"
      effort: "Medium"
      priority: 4
      
    - opportunity: "Optimize email signup CTAs"
      potential_impact: "+10-15% email conversions"
      confidence: "Medium"
      effort: "Low"
      priority: 5
  
  low_impact:
    - opportunity: "Adjust LinkedIn content strategy"
      potential_impact: "+20-30 conversions"
      confidence: "Low"
      effort: "High"
      priority: 6
```

### Step 3: Budget Reallocation Recommendations

**Scenario Analysis**:

```yaml
budget_optimization:
  current_allocation:
    total: 10000
    breakdown:
      content_creation: 4000 (40%)
      paid_promotion: 3000 (30%)
      tools: 1500 (15%)
      community: 1000 (10%)
      contingency: 500 (5%)
  
  # Scenario 1: Conservative (Same Total Budget)
  conservative_reallocation:
    total: 10000
    changes: "Minimal changes, optimize within categories"
    breakdown:
      content_creation: 4200 (42%)  # +200 for lead magnet
      paid_promotion: 3000 (30%)    # No change
      tools: 1700 (17%)             # +200 for email automation
      community: 800 (8%)           # -200 (underutilized)
      contingency: 300 (3%)         # -200 (overestimated)
    channel_reallocation:
      reddit: 700 (+200 from LinkedIn)
      dev_to: 1000 (+200 from LinkedIn)
      dev_blog: 1000 (no change)
      linkedin: 600 (-400)
      twitter: 700 (no change)
    expected_improvement: "+5-8% overall achievement"
  
  # Scenario 2: Balanced (Same Budget, Bigger Shifts)
  balanced_reallocation:
    total: 10000
    changes: "Significant shifts based on performance"
    breakdown:
      content_creation: 4500 (45%)  # +500 for variety
      paid_promotion: 2800 (28%)    # -200 (organic works better)
      tools: 1800 (18%)             # +300 for email + analytics
      community: 700 (7%)           # -300 (optimize efficiency)
      contingency: 200 (2%)         # -300 (better planning)
    channel_reallocation:
      reddit: 1000 (+500)           # Double investment
      dev_to: 1200 (+400)           # Increase
      dev_blog: 1300 (+300)         # Owned channel priority
      linkedin: 300 (-700)          # Minimal presence
      twitter: 0 (-200)             # Cut if underperforming
      new_channels: 200             # Test HackerNews
    expected_improvement: "+10-15% overall achievement"
  
  # Scenario 3: Aggressive (Increased Budget)
  aggressive_reallocation:
    total: 15000 (+50%)
    changes: "Scale what works, cut what doesn't"
    breakdown:
      content_creation: 7000 (47%)  # +75% (more variety + quality)
      paid_promotion: 4000 (27%)    # +33% (on best channels only)
      tools: 2500 (17%)             # +67% (better analytics + automation)
      community: 1200 (8%)          # +20% (community manager)
      contingency: 300 (2%)         # -40% (better planning)
    channel_reallocation:
      reddit: 1500 (+1000)          # 3x investment
      dev_to: 1800 (+1000)          # 2.25x investment
      dev_blog: 2000 (+1000)        # 2x investment
      linkedin: 0 (-1000)           # Cut entirely
      twitter: 700 (no change)      # Maintain
      hackernews: 500 (new)         # Add high-ROI channel
      youtube: 500 (new)            # Add video content
    expected_improvement: "+25-35% overall achievement"
```

### Step 4: Channel Mix Optimization

Recommend optimal channel strategy:

```yaml
channel_optimization:
  current_mix:
    channels: 5
    spend_distribution: "Relatively even"
    effectiveness: "3 strong, 1 weak, 1 average"
  
  recommended_mix:
    strategy: "Power law distribution - heavy investment in proven channels"
    
    tier_1_channels:  # 60% of budget
      - channel: "reddit"
        current: 500
        recommended: 1000-1500
        rationale: "Best ROI (9/10), highest engagement rate"
        tactics:
          - "Increase posting frequency: 1x/week → 2x/week"
          - "Expand to r/programming + r/opensource + r/selfhosted"
          - "Run 1 AMA session per quarter"
        expected_impact: "+40-60 GitHub stars"
      
      - channel: "dev-to"
        current: 800
        recommended: 1200-1800
        rationale: "Strong ROI (8/10), growing community"
        tactics:
          - "Launch series format: 'MetaSpec in Practice' (8 parts)"
          - "Collaborate with Dev.to influencers"
          - "Cross-promote blog content"
        expected_impact: "+50-80 GitHub stars"
      
      - channel: "dev-blog"
        current: 1500
        recommended: 1300-2000
        rationale: "Owned channel, high conversion, sustainable"
        tactics:
          - "Improve SEO for tutorial content"
          - "Add video tutorials"
          - "Optimize email capture CTAs"
        expected_impact: "+150-200 email subscribers"
    
    tier_2_channels:  # 30% of budget
      - channel: "twitter"
        current: 1200
        recommended: 700-1000
        rationale: "Average performance, maintain presence"
        tactics:
          - "Focus on community engagement vs broadcasting"
          - "Share behind-the-scenes content"
          - "Engage with developer influencers"
        expected_impact: "+20-30 GitHub stars"
    
    tier_3_channels:  # 10% of budget
      - channel: "linkedin"
        current: 1000
        recommended: 300-500
        rationale: "Underperformed, but has different audience"
        tactics:
          - "Pivot to business-value content"
          - "Target engineering managers, not developers"
          - "Share case studies, not technical tutorials"
        expected_impact: "+10-20 decision-maker awareness"
    
    experimental_channels:  # Minimal budget
      - channel: "hackernews"
        current: 0
        recommended: 200-500
        rationale: "Similar to Reddit, high-quality audience"
        tactics:
          - "1 Show HN post"
          - "Engage authentically in comments"
        expected_impact: "+20-40 GitHub stars (if successful)"
      
      - channel: "youtube"
        current: 0
        recommended: 300-500
        rationale: "Video content performs well"
        tactics:
          - "Create 3-5 tutorial videos"
          - "Repurpose blog content"
        expected_impact: "+1000-2000 views, +20-30 stars"
  
  channels_to_cut:
    - channel: "linkedin"
      if: "Budget is tight"
      rationale: "Lowest ROI, audience mismatch"
      savings: 700-1000
      risk: "Low - not core audience"
```

### Step 5: Content Strategy Optimization

Recommend content improvements:

```yaml
content_optimization:
  current_strategy:
    types: ["tutorial", "case_study", "comparison", "announcement"]
    frequency: "3x/week"
    top_performer: "tutorial"
    weakness: "Repetitive format after week 7"
  
  recommended_strategy:
    content_mix:
      - type: "Tutorial"
        current_share: 42% (5/12)
        recommended_share: 50% (6/12)
        rationale: "Highest performance, 5% GitHub referral rate"
        formats:
          - "Step-by-step guides"
          - "Video tutorials (new)"
          - "Interactive examples"
        frequency: "2x/month"
        
      - type: "Case Study"
        current_share: 33% (4/12)
        recommended_share: 25% (3/12)
        rationale: "Strong email conversion (2.5%)"
        formats:
          - "Written deep dives"
          - "Customer interviews (new)"
          - "Before/after comparisons"
        frequency: "1.5x/month"
        
      - type: "Comparison"
        current_share: 17% (2/12)
        recommended_share: 17% (2/12)
        rationale: "Good engagement, addresses skepticism"
        formats:
          - "Tool comparisons"
          - "Methodology comparisons"
        frequency: "1x/month"
        
      - type: "Announcement"
        current_share: 25% (3/12)
        recommended_share: 8% (1/12)
        rationale: "Low performance, reduce drastically"
        formats:
          - "Major releases only"
          - "Embed in tutorials, not standalone"
        frequency: "Quarterly only"
    
    new_content_types:
      - type: "Developer Stories"
        share: "17% (2/12 new)"
        rationale: "Community-driven, authentic"
        format: "Guest posts from users"
        frequency: "1x/month"
        
      - type: "Live Coding"
        share: "8% (1/12 new)"
        rationale: "High engagement, interactive"
        format: "Twitch/YouTube streams"
        frequency: "1x/month"
    
    content_calendar_optimization:
      phase_1:  # Weeks 1-4: Education
        focus: "Tutorials + comparisons"
        goal: "Build awareness"
        content: 60% tutorial, 40% comparison
        
      phase_2:  # Weeks 5-8: Validation
        focus: "Case studies + developer stories"
        goal: "Build trust"
        content: 40% case study, 40% tutorial, 20% stories
        
      phase_3:  # Weeks 9-12: Engagement
        focus: "Interactive + community"
        goal: "Drive conversion"
        content: 30% tutorial, 30% live, 40% community
    
    posting_schedule_optimization:
      best_days: ["Tuesday", "Wednesday", "Thursday"]
      best_times: "9-11 AM ET (developer working hours)"
      avoid: ["Friday afternoon", "Weekends", "Holidays"]
      
      recommended_schedule:
        monday: "Plan + prep"
        tuesday: "Publish tutorial (Reddit + Dev.to)"
        wednesday: "Publish case study (Blog + LinkedIn)"
        thursday: "Publish comparison/story (Twitter + Dev.to)"
        friday: "Community engagement (respond, share)"
        weekend: "None (negligible traffic)"
```

### Step 6: KPI Refinement

Adjust targets based on learnings:

```yaml
kpi_optimization:
  current_kpis:
    - name: "GitHub Stars"
      original_target: 500
      achieved: 420 (84%)
      
    - name: "Email Subscribers"
      original_target: 1000
      achieved: 850 (85%)
      
    - name: "Website Traffic"
      original_target: 50000
      achieved: 45000 (90%)
  
  refined_kpis:
    - name: "GitHub Stars"
      rationale: "Original target was aggressive but achievable with optimizations"
      next_target_options:
        conservative: 450  # +7% from last campaign
        balanced: 520      # +24% with optimizations
        aggressive: 600    # +43% with increased budget
      recommended: 520
      adjustments_needed:
        - "Increase Reddit investment"
        - "Add content variety"
        - "Community engagement tactics"
      
    - name: "Email Subscribers"
      rationale: "Underinvested in email tactics, high upside"
      next_target_options:
        conservative: 900   # +6% from last campaign
        balanced: 1100      # +29% with lead magnet
        aggressive: 1400    # +65% with automation
      recommended: 1100
      adjustments_needed:
        - "Create lead magnet"
        - "Optimize CTAs"
        - "Build nurture sequence"
        - "Add email automation tool"
      
    - name: "Website Traffic"
      rationale: "Closest to target, maintain trajectory"
      next_target_options:
        conservative: 50000  # Original target
        balanced: 60000      # +33% with SEO
        aggressive: 80000    # +78% with video + SEO
      recommended: 60000
      adjustments_needed:
        - "SEO optimization for tutorials"
        - "Add video content"
        - "Expand to YouTube"
  
  new_kpis_to_add:
    - name: "Community Engagement Rate"
      definition: "(Comments + Shares) / Content Pieces"
      baseline: 18  # (450 reactions / 25 pieces)
      target: 30
      rationale: "Leading indicator of virality"
      
    - name: "Content ROI"
      definition: "GitHub Stars / Content Pieces"
      baseline: 14.8  # (370 stars / 25 pieces)
      target: 20
      rationale: "Content effectiveness metric"
      
    - name: "Email Conversion Rate"
      definition: "Email Signups / Website Visits"
      baseline: 1.9%  # (850 / 45000)
      target: 2.5%
      rationale: "Email funnel optimization metric"
```

### Step 7: Risk Analysis

Identify potential risks in optimizations:

```yaml
risk_analysis:
  high_risk_changes:
    - change: "Cut LinkedIn investment by 70%"
      risk: "Lose visibility with decision-makers"
      mitigation: "Maintain minimal presence, pivot messaging"
      probability: "Medium"
      impact: "Low"
      recommendation: "Proceed with mitigation"
      
    - change: "Triple Reddit investment"
      risk: "Diminishing returns, community fatigue"
      mitigation: "Expand to multiple subreddits, vary content"
      probability: "Low"
      impact: "Medium"
      recommendation: "Proceed with monitoring"
  
  medium_risk_changes:
    - change: "Add video content (YouTube)"
      risk: "Resource-intensive, unproven for this audience"
      mitigation: "Start with 3 videos, measure engagement"
      probability: "Medium"
      impact: "Medium"
      recommendation: "Pilot first"
      
    - change: "Increase aggressive KPI targets"
      risk: "Team demotivation if missed again"
      mitigation: "Use balanced targets, celebrate progress"
      probability: "Low"
      impact: "High"
      recommendation: "Use balanced scenario"
  
  low_risk_changes:
    - change: "Add lead magnet for email growth"
      risk: "Minimal - proven tactic"
      probability: "Very Low"
      impact: "Low"
      recommendation: "Implement immediately"
```

### Step 8: Implementation Roadmap

Create actionable next steps:

```yaml
implementation_roadmap:
  immediate_actions:  # Week 1-2
    - action: "Create email lead magnet"
      owner: "Content Writer"
      effort: "20 hours"
      cost: 500
      expected_outcome: "+30% email conversion rate"
      
    - action: "Optimize email signup CTAs"
      owner: "Designer"
      effort: "8 hours"
      cost: 200
      expected_outcome: "+10% email signups"
      
    - action: "Pivot LinkedIn content strategy"
      owner: "Marketing Lead"
      effort: "4 hours planning"
      cost: 0
      expected_outcome: "Test new messaging"
  
  short_term:  # Week 3-4
    - action: "Set up email automation tool"
      owner: "Marketing Lead"
      effort: "12 hours"
      cost: 500
      expected_outcome: "Enable nurture sequences"
      
    - action: "Expand Reddit presence"
      owner: "Social Media Manager"
      effort: "Ongoing"
      cost: 500
      expected_outcome: "+40 GitHub stars"
      
    - action: "Create first 3 video tutorials"
      owner: "Content Writer + Designer"
      effort: "40 hours"
      cost: 1000
      expected_outcome: "+1000 YouTube views"
  
  medium_term:  # Week 5-8
    - action: "Launch Dev.to series"
      owner: "Content Writer"
      effort: "60 hours"
      cost: 1500
      expected_outcome: "+50 GitHub stars"
      
    - action: "Test HackerNews"
      owner: "Marketing Lead"
      effort: "8 hours"
      cost: 0
      expected_outcome: "+20-40 stars if successful"
      
    - action: "Build 5-email nurture sequence"
      owner: "Content Writer"
      effort: "20 hours"
      cost: 500
      expected_outcome: "+15% email engagement"
  
  long_term:  # Week 9-12
    - action: "Community engagement program"
      owner: "Social Media Manager"
      effort: "Ongoing"
      cost: 1000
      expected_outcome: "Sustain growth through campaign"
      
    - action: "SEO optimization"
      owner: "Marketing Lead"
      effort: "20 hours"
      cost: 500
      expected_outcome: "+20% organic traffic"
```

### Step 9: Generate Optimization Report

Create comprehensive recommendations document:

```markdown
# Optimization Recommendations Report

**Based on**: Campaign Review (2025-01-15 to 2025-03-31)  
**Campaign**: MetaSpec Developer Onboarding  
**Overall Achievement**: 85.1% (B+)  
**Generated**: 2025-04-05

---

## Executive Summary

Based on your campaign performance, here are **data-driven recommendations** to achieve **95%+ goal achievement** in your next campaign.

**Key Recommendations**:
1. 🔄 Reallocate budget: LinkedIn → Reddit/Dev.to (+50-80 stars)
2. 📧 Add email lead magnet (+200-300 subscribers)
3. 🎨 Introduce content variety after week 7 (prevent plateau)
4. 👥 Add community engagement tactics (+15-20% growth)
5. 📹 Test video content (new channel: YouTube)

**Expected Impact**: +10-15% overall achievement (85% → 95-100%)

**Confidence**: High (based on actual performance data)

---

## Budget Optimization

### Current vs Recommended Allocation

| Category | Current | Recommended | Change | Rationale |
|----------|---------|-------------|--------|-----------|
| **Content Creation** | $4,000 (40%) | $4,500 (45%) | +$500 | Add variety, lead magnet |
| **Paid Promotion** | $3,000 (30%) | $2,800 (28%) | -$200 | Organic works better |
| **Tools** | $1,500 (15%) | $1,800 (18%) | +$300 | Email automation |
| **Community** | $1,000 (10%) | $700 (7%) | -$300 | Optimize efficiency |
| **Contingency** | $500 (5%) | $200 (2%) | -$300 | Better planning |
| **TOTAL** | **$10,000** | **$10,000** | **$0** | Same budget |

### Channel Budget Reallocation

| Channel | Current | Recommended | Change | Expected Impact |
|---------|---------|-------------|--------|-----------------|
| **Reddit** | $500 | $1,000 | +$500 ✅ | +40-60 stars (ROI: 9/10) |
| **Dev.to** | $800 | $1,200 | +$400 ✅ | +50-80 stars (ROI: 8/10) |
| **Blog** | $1,000 | $1,300 | +$300 ✅ | +100-150 subscribers |
| **Twitter** | $1,200 | $700 | -$500 | Maintain presence |
| **LinkedIn** | $1,000 | $300 | -$700 ❌ | Lowest ROI, cut 70% |
| **HackerNews** | $0 | $200 | +$200 🆕 | +20-40 stars (experiment) |
| **YouTube** | $0 | $300 | +$300 🆕 | +1K views (new format) |
| **TOTAL** | **$4,500** | **$5,000** | **+$500** | - |

---

## Channel Strategy Optimization

### Tier 1: Double Down (60% of Budget)

#### 🥇 Reddit → $1,000 (+100%)
**Why**: Best ROI (9/10), lowest cost-per-star ($6.25)

**Tactics**:
- Increase frequency: 1x/week → 2x/week
- Expand subreddits: r/programming + r/opensource + r/selfhosted
- Best posting time: Tuesday 10 AM ET
- Run 1 AMA per quarter

**Expected Impact**: +40-60 GitHub stars

---

#### 🥈 Dev.to → $1,200 (+50%)
**Why**: Strong ROI (8/10), engaged community

**Tactics**:
- Launch series: "MetaSpec in Practice" (8 parts)
- Collaborate with Dev.to influencers
- Cross-promote blog content
- Use series format (40% higher follow-through)

**Expected Impact**: +50-80 GitHub stars

---

#### 🥉 Developer Blog → $1,300 (+30%)
**Why**: Owned channel, highest email conversion (1.33%)

**Tactics**:
- SEO optimization for tutorials
- Add video content
- Optimize email CTAs
- Create lead magnet

**Expected Impact**: +150-200 email subscribers

---

### Tier 2: Maintain (30% of Budget)

#### Twitter → $700 (-40%)
**Why**: Average performance, reduce but maintain presence

**Tactics**:
- Focus on engagement vs broadcasting
- Share behind-the-scenes
- Engage with influencers

**Expected Impact**: +20-30 GitHub stars

---

### Tier 3: Pivot or Cut (10% of Budget)

#### LinkedIn → $300 (-70%)
**Why**: Underperformed (ROI: 4/10), wrong audience fit

**Tactics**:
- Pivot to business-value content
- Target engineering managers, not developers
- Share case studies, not tutorials
- Minimal investment

**Expected Impact**: +10-20 decision-maker awareness

---

### Experimental: Test New Channels

#### 🆕 HackerNews → $200 (new)
**Why**: Similar to Reddit, high-quality audience

**Tactics**:
- 1 "Show HN" post
- Engage authentically in comments

**Expected Impact**: +20-40 stars (if successful)

---

#### 🆕 YouTube → $300 (new)
**Why**: Video format, untapped channel

**Tactics**:
- Create 3-5 tutorial videos
- Repurpose blog content

**Expected Impact**: +1,000-2,000 views, +20-30 stars

---

## Content Strategy Optimization

### Current Problems
❌ Announcements underperformed (25% of content, 3/10 score)
❌ Content repetition caused week 8-11 plateau
❌ No email lead magnet

### Recommended Content Mix

| Type | Current | Recommended | Change | Rationale |
|------|---------|-------------|--------|-----------|
| **Tutorial** | 42% (5/12) | 50% (6/12) | +1 | Best performer (9/10) |
| **Case Study** | 33% (4/12) | 25% (3/12) | -1 | Strong but sufficient |
| **Comparison** | 17% (2/12) | 17% (2/12) | 0 | Keep as is |
| **Announcement** | 25% (3/12) | 8% (1/12) | -2 ❌ | Cut drastically |
| **Dev Stories** | 0% | 17% (2/12) | +2 🆕 | Community-driven |
| **Live Coding** | 0% | 8% (1/12) | +1 🆕 | Interactive |

### Content Calendar by Phase

**Phase 1 (Weeks 1-4): Education**
- 60% tutorials, 40% comparisons
- Goal: Build awareness

**Phase 2 (Weeks 5-8): Validation**
- 40% case studies, 40% tutorials, 20% stories
- Goal: Build trust

**Phase 3 (Weeks 9-12): Engagement** ⚠️ (Previously plateau)
- 30% tutorials, 30% live, 40% community
- Goal: Drive conversion + prevent plateau

### Posting Schedule Optimization

| Day | Action | Content Type |
|-----|--------|--------------|
| **Mon** | Plan + prep | - |
| **Tue** | Publish | Tutorial (Reddit + Dev.to) ✅ |
| **Wed** | Publish | Case Study (Blog + LinkedIn) ✅ |
| **Thu** | Publish | Comparison/Story (Twitter + Dev.to) ✅ |
| **Fri** | Engage | Community (respond, share) |
| **Sat-Sun** | None | Negligible developer traffic ❌ |

**Best Time**: 9-11 AM ET (developer working hours)

---

## KPI Refinement

### Recommended Targets (Balanced Scenario)

| KPI | Last Campaign | Achievement | Next Target | Increase | Feasibility |
|-----|---------------|-------------|-------------|----------|-------------|
| **GitHub Stars** | 500 (420 actual) | 84% | **520** | +24% | ✅ High |
| **Email Subscribers** | 1,000 (850 actual) | 85% | **1,100** | +29% | ✅ High |
| **Website Traffic** | 50,000 (45K actual) | 90% | **60,000** | +33% | ✅ Medium |

### Adjustments Needed

**For GitHub Stars → 520**:
- ✅ Increase Reddit investment (+$500)
- ✅ Add content variety (prevent plateau)
- ✅ Community engagement tactics

**For Email Subscribers → 1,100**:
- ✅ Create lead magnet (high priority)
- ✅ Optimize CTAs
- ✅ Build nurture sequence
- ✅ Add email automation tool

**For Website Traffic → 60,000**:
- ✅ SEO optimization for tutorials
- ✅ Add video content
- ✅ Expand to YouTube

---

## New KPIs to Track

| KPI | Definition | Baseline | Target | Why Track |
|-----|------------|----------|--------|-----------|
| **Community Engagement Rate** | (Comments + Shares) / Content | 18 | 30 | Leading indicator of virality |
| **Content ROI** | GitHub Stars / Content Pieces | 14.8 | 20 | Content effectiveness |
| **Email Conversion Rate** | Email Signups / Website Visits | 1.9% | 2.5% | Email funnel optimization |

---

## Implementation Roadmap

### ⚡ Immediate (Week 1-2)

| Action | Owner | Effort | Cost | Impact |
|--------|-------|--------|------|--------|
| Create email lead magnet | Content Writer | 20h | $500 | +30% email conversion |
| Optimize email CTAs | Designer | 8h | $200 | +10% signups |
| Pivot LinkedIn strategy | Marketing Lead | 4h | $0 | Test new messaging |

**Total**: 32 hours, $700

---

### 📅 Short-Term (Week 3-4)

| Action | Owner | Effort | Cost | Impact |
|--------|-------|--------|------|--------|
| Set up email automation | Marketing Lead | 12h | $500 | Enable nurture sequences |
| Expand Reddit presence | Social Manager | Ongoing | $500 | +40 stars |
| Create 3 video tutorials | Content + Designer | 40h | $1,000 | +1K YouTube views |

**Total**: 52 hours, $2,000

---

### 🎯 Medium-Term (Week 5-8)

| Action | Owner | Effort | Cost | Impact |
|--------|-------|--------|------|--------|
| Launch Dev.to series | Content Writer | 60h | $1,500 | +50 stars |
| Test HackerNews | Marketing Lead | 8h | $0 | +20-40 stars |
| Build nurture sequence | Content Writer | 20h | $500 | +15% email engagement |

**Total**: 88 hours, $2,000

---

### 🚀 Long-Term (Week 9-12)

| Action | Owner | Effort | Cost | Impact |
|--------|-------|--------|------|--------|
| Community engagement | Social Manager | Ongoing | $1,000 | Prevent plateau |
| SEO optimization | Marketing Lead | 20h | $500 | +20% organic traffic |

**Total**: 20 hours, $1,500

---

**Grand Total**: 192 hours, $6,200 (within $10K budget with existing operations)

---

## Risk Assessment

| Change | Risk | Probability | Impact | Mitigation | Decision |
|--------|------|-------------|--------|------------|----------|
| Cut LinkedIn 70% | Lose decision-maker visibility | Medium | Low | Maintain minimal presence | ✅ Proceed |
| Triple Reddit | Diminishing returns | Low | Medium | Expand subreddits, vary content | ✅ Proceed |
| Add YouTube | Resource-intensive | Medium | Medium | Pilot with 3 videos | ⚠️ Pilot first |
| Aggressive KPI targets | Team demotivation | Low | High | Use balanced targets | ✅ Use balanced |

---

## Expected Results

### Scenario: Balanced Optimizations (Recommended)

**Investment**: $10,000 (same budget)

**Expected Achievement**:
- GitHub Stars: 520 (previously 420) → **95% of target** ✅
- Email Subscribers: 1,100 (previously 850) → **100% of target** ✅
- Website Traffic: 60,000 (previously 45K) → **100% of target** ✅

**Overall Achievement**: **95-100%** (up from 85%)

**Confidence Level**: **High** (based on proven tactics from review)

**ROI**: Estimated **180-200%** (up from 154%)

---

## Next Steps

1. **Review recommendations** with team
2. **Select scenario**: Conservative / Balanced / Aggressive
3. **Adjust budget** if needed
4. **Start /marketspec.discover** for next campaign with these learnings
5. **Implement immediate actions** (Week 1-2)

---

## How to Use This Report

This report should feed into your next campaign planning:

```bash
# Start next campaign with optimization insights
/marketspec.discover "Q2 2025 Growth" --based-on optimization-recommendations.md

# The discover command will incorporate:
# - Budget reallocation suggestions
# - Channel mix optimization
# - Content strategy improvements
# - Refined KPI targets
# - Lessons learned
```

---

**Report Prepared By**: Marketing AI Assistant  
**Based On**: campaign-review.md + marketing-spec.yaml  
**Confidence**: High (data-driven recommendations)  
**Ready to Implement**: Yes ✅
```

**Output Location**: `optimization-recommendations.md`

---

## Success Criteria

- ✅ Review data loaded and analyzed
- ✅ Optimization opportunities identified
- ✅ Budget reallocation recommended (3 scenarios)
- ✅ Channel mix optimized
- ✅ Content strategy refined
- ✅ KPI targets adjusted
- ✅ Risks assessed
- ✅ Implementation roadmap created
- ✅ Expected outcomes projected

---

## Output

**Primary Output**: `optimization-recommendations.md`

**Structure**:
```
project-root/
├── marketing-spec.yaml                # Original plan
├── campaign-review.md                 # Review from /marketspec.review
└── optimization-recommendations.md    # Optimization report (NEW)
```

---

## Error Handling

**Missing Review Data**:
```
❌ Error: Cannot find campaign-review.md
→ Run /marketspec.review first to analyze campaign performance
→ Optimization requires actual performance data
```

**Incomplete Review**:
```
⚠️ Warning: Review data is incomplete
→ Missing: Channel performance data
→ Recommendations will be limited without complete data
```

**No Clear Optimization Opportunities**:
```
✅ Campaign performed excellently (98% achievement)
→ Optimization opportunities are minimal
→ Recommend: Maintain current strategy, scale budget if possible
```

---

## Example Interaction

```
User: /marketspec.optimize

AI: I'll generate optimization recommendations based on your campaign review!

📄 **Review Data Loaded**: campaign-review.md
📊 **Overall Achievement**: 85.1% (B+)
💰 **Budget**: $9,500 spent / $10,000 planned
📈 **ROI**: 154%

---

**Analyzing performance data...**

✅ **Opportunities Identified**: 6

**High Impact** (Top 3):
1. 🔄 Reallocate budget: LinkedIn → Reddit/Dev.to
   Impact: +50-80 GitHub stars
   Effort: Low
   
2. 📧 Add email lead magnet
   Impact: +200-300 subscribers
   Effort: Medium
   
3. 🎨 Add content variety after week 7
   Impact: Prevent plateau, sustain 60 stars/week
   Effort: Medium

---

**Budget Optimization**:

🎯 **Recommended Scenario**: Balanced (same $10K budget)

**Key Changes**:
- Reddit: $500 → $1,000 (+100%)
- Dev.to: $800 → $1,200 (+50%)
- LinkedIn: $1,000 → $300 (-70%)
- YouTube: $0 → $300 (new)

**Expected Impact**: +10-15% overall achievement (85% → 95-100%)

---

**Channel Strategy**:

✅ **Double Down**: Reddit, Dev.to, Blog (top performers)
⚠️ **Reduce**: LinkedIn, Twitter (underperformers)
🆕 **Test**: YouTube, HackerNews (new opportunities)

---

**Content Strategy**:

Current Problem: Announcements (25%) underperformed, plateau in weeks 8-11

Recommendations:
- Cut announcements: 25% → 8% (-2 pieces)
- Add tutorials: 42% → 50% (+1 piece)
- Add dev stories: 0% → 17% (+2 pieces, new format)
- Add live coding: 0% → 8% (+1 piece, new format)

---

**Refined KPI Targets** (Balanced Scenario):

| KPI | Last Target | Next Target | Increase | Feasibility |
|-----|-------------|-------------|----------|-------------|
| GitHub Stars | 500 | 520 | +24% | ✅ High |
| Email Subscribers | 1,000 | 1,100 | +29% | ✅ High |
| Website Traffic | 50,000 | 60,000 | +33% | ✅ Medium |

---

**Implementation Roadmap**:

⚡ Immediate (Week 1-2): $700, 32 hours
- Create lead magnet
- Optimize CTAs
- Pivot LinkedIn

📅 Short-term (Week 3-4): $2,000, 52 hours
- Email automation
- Expand Reddit
- First videos

🎯 Medium-term (Week 5-8): $2,000, 88 hours
- Dev.to series
- Test HackerNews

🚀 Long-term (Week 9-12): $1,500, 20 hours
- Community engagement
- SEO optimization

---

**Expected Results**:
- Achievement: 85% → **95-100%** ✅
- ROI: 154% → **180-200%** ✅
- Confidence: **High**

---

📄 **Full Report Generated**: optimization-recommendations.md

**Next Step**: Use this report as input for your next `/marketspec.discover` to plan Q2 campaign with these optimizations baked in.

Would you like me to:
- Show detailed channel analysis?
- Export in different format?
- Start next campaign planning with these insights?
```

---

## Notes

- **Data-Driven**: All recommendations based on actual performance
- **Actionable**: Every recommendation has clear tactics
- **Realistic**: Considers budget, resources, and risks
- **Prioritized**: Focus on high-impact, low-effort changes first
- **Scenarios**: Provides options for different budgets/ambitions
- **Closes Loop**: Feeds back into next `/marketspec.discover`

---

## Integration with Other Commands

**Position**: Extension (AFTER review)

References:
- `/marketspec.review` - Source of performance data
- `/marketspec.create` - Original specification

Feeds into:
- `/marketspec.discover` - Next campaign planning (closes the loop)

**Complete Cycle**:
```
discover → ... → create → [Execute] → review → optimize
    ↑                                               ↓
    └───────────────────── (closes loop) ──────────┘
```

---

## See Also

- `/marketspec.review` - Previous step
- `/marketspec.discover` - Next campaign planning
- `/marketspec.create` - Original specification
- Optimization examples in `examples/` directory

