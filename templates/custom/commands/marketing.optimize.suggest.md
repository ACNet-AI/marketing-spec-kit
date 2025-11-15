# Slash Command: /marketing.optimize.suggest

## Purpose

AI-generated optimization suggestions for an active campaign or plan based on current performance and industry best practices.

## Command Usage

```
/marketing.optimize.suggest <entity_type> <entity_id>
```

Where `entity_type` is either `campaign` or `plan`.

## Prerequisites

- Entity must exist
- Some performance data available (even partial)

## Execution Steps

### Step 1: Read Entity Context

Load entity details and current performance data (if available):
- Objectives/goals
- Budget and spend
- Timeline
- Channels
- Current metrics (if campaign is active)

### Step 2: Identify Optimization Opportunities

Analyze entity across multiple dimensions:

#### Budget Optimization
- Is budget allocated efficiently across channels?
- Are there underperforming channels to cut?
- Are there high-ROI channels to scale?

#### Content Optimization
- Which content types perform best?
- Are posting frequencies optimal?
- Is messaging resonating with audience?

#### Channel Optimization
- Are the right channels selected for the goal?
- Is channel mix balanced?
- Are there untapped channels?

#### Timing Optimization
- Is campaign duration optimal?
- Are posts scheduled at best times?
- Is there seasonality to consider?

#### Audience Optimization
- Is targeting precise enough?
- Are there high-value segments to focus on?
- Should audience be expanded or narrowed?

#### Conversion Optimization
- Is the funnel optimized?
- Are CTAs clear and compelling?
- Is landing page conversion-optimized?

### Step 3: Prioritize Recommendations

Categorize by:
- **Priority**: High (critical), Medium (important), Low (nice-to-have)
- **Effort**: Low (quick win), Medium (moderate work), High (significant investment)
- **Expected Impact**: Quantify when possible (e.g., "+20% conversions")

### Step 4: Generate Suggestions

For each recommendation, provide:
- **Action**: Specific, actionable step
- **Rationale**: Why this matters
- **Expected Impact**: Quantified result
- **Effort**: Time/resource estimate
- **Implementation Steps**: How to execute

### Step 5: Output Recommendations

```yaml
optimizations:
  # High Priority + Low Effort = QUICK WINS
  - priority: "high"
    action: "Pause underperforming Reddit channel, reallocate $500"
    rationale: "Reddit CPA is $45 vs $18 average, burning budget"
    expected_impact: "Save $500, redeploy to email (60x ROI channel)"
    effort: "low"
    implementation:
      - "Pause Reddit ads immediately"
      - "Move $500 to email campaign budget"
      - "Monitor results for 1 week"
  
  # High Priority + Medium Effort
  - priority: "high"
    action: "A/B test 3 new headline variations"
    rationale: "Current CTR 1.2% vs 2% target, headlines may be weak"
    expected_impact: "Increase CTR from 1.2% to 1.8% (+50%)"
    effort: "medium"
    implementation:
      - "Write 3 headline variations focusing on benefits"
      - "Set up A/B test with 33/33/33 split"
      - "Run for 1 week, choose winner"
  
  # Medium Priority + Low Effort
  - priority: "medium"
    action: "Increase Twitter posting frequency from 3x to 5x per week"
    rationale: "Twitter engagement is high, but reach is limited by frequency"
    expected_impact: "Increase impressions by 40%"
    effort: "low"
    implementation:
      - "Add 2 more posts per week (Tue, Thu)"
      - "Use content calendar generator"
      - "Maintain quality standards"
  
  # High Priority + High Effort = STRATEGIC MOVES
  - priority: "high"
    action: "Redesign landing page with simplified signup flow"
    rationale: "Conversion rate 0.17% vs 2% industry avg (10x gap)"
    expected_impact: "Increase conversions from 260 to 2,600 annually (+900%)"
    effort: "high"
    implementation:
      - "Conduct user research (Week 1-2)"
      - "Design 2-step signup vs current 5-step (Week 3)"
      - "Develop and QA (Week 4-5)"
      - "A/B test for 2 weeks (Week 6-7)"
  
  # Low Priority + Low Effort
  - priority: "low"
    action: "Experiment with short-form video content on Twitter"
    rationale: "Video engagement rates 2-3x higher than images"
    expected_impact: "Potentially +20-30% engagement"
    effort: "low"
    implementation:
      - "Create 2 test videos (30-60 sec)"
      - "Post on high-traffic days (Mon, Wed)"
      - "Measure engagement vs image posts"
```

```markdown
## Optimization Suggestions Report

**Entity**: Q4 Product Launch Awareness Campaign
**Type**: Campaign
**Current Performance**: 3/4 metrics met, CTR below target

---

### 🎯 Quick Wins (High Priority + Low Effort)

Do these immediately for fast results:

#### 1. Pause Reddit, Reallocate $500 ⚡
- **Problem**: Reddit CPA $45 vs $18 average (2.5x higher cost)
- **Action**: Stop Reddit ads, move budget to email
- **Impact**: Save $500, 60x ROI potential on email
- **Effort**: 30 minutes
- **Steps**:
  1. Pause Reddit campaign in ads manager
  2. Increase email campaign budget by $500
  3. Monitor for 1 week

#### 2. Increase Twitter Frequency ⚡
- **Problem**: High engagement but limited reach (3 posts/week)
- **Action**: Post 5x per week instead of 3x
- **Impact**: +40% impressions (minimal extra cost)
- **Effort**: 2 hours/week
- **Steps**:
  1. Generate 2 more posts per week
  2. Schedule for Tue and Thu
  3. Maintain content quality

---

### 🚀 High-Impact Improvements (Worth the Effort)

Invest in these for significant gains:

#### 3. A/B Test Headlines 📈
- **Problem**: CTR 1.2% vs 2% target (40% below)
- **Action**: Test 3 benefit-focused headline variations
- **Impact**: +50% CTR (1.2% → 1.8%)
- **Effort**: 4 hours + 1 week test
- **Steps**:
  1. Write 3 variations:
     - Current: "Introducing [Product]"
     - Variation A: "Double Your Productivity in 5 Minutes"
     - Variation B: "[Product] Helps 10K Developers Ship Faster"
     - Variation C: "The Developer Tool You Didn't Know You Needed"
  2. Set up 25/25/25/25 A/B test
  3. Run for 1 week, choose winner

#### 4. Redesign Landing Page 🎨
- **Problem**: Conversion rate 0.17% vs 2% industry avg (10x gap!)
- **Action**: Simplify signup from 5 steps to 2 steps
- **Impact**: +900% conversions (0.17% → 1.7%)
- **Effort**: 6 weeks (research + dev + test)
- **Steps**:
  1. User research: Why are 99.83% dropping off? (Week 1-2)
  2. Design simplified flow (Week 3)
  3. Develop & QA (Week 4-5)
  4. A/B test vs current (Week 6-7)

---

### 💡 Strategic Experiments (Lower Priority)

Try these when capacity allows:

#### 5. Video Content Experiment 🎥
- **Opportunity**: Video engagement 2-3x higher than images
- **Action**: Create 2 short-form videos (30-60 sec)
- **Impact**: Potentially +20-30% engagement
- **Effort**: 4 hours
- **Steps**:
  1. Record 2 quick demos or tips
  2. Edit with captions (for silent viewing)
  3. Post Mon & Wed, compare to image posts

#### 6. Influencer Partnership 🤝
- **Opportunity**: Developer influencers can amplify reach
- **Action**: Partner with 2-3 micro-influencers (10K-50K followers)
- **Impact**: +20K impressions, higher trust
- **Effort**: 1 week outreach + coordination
- **Steps**:
  1. Identify 5 relevant micro-influencers
  2. Reach out with partnership offer
  3. Provide content/product access
  4. Track with unique links

---

### 📊 Optimization Priority Matrix

```
High Impact │ 4. Landing Page    │ 3. A/B Headlines   │
            │    Redesign        │                    │
            │ (High Effort)      │ (Medium Effort)    │
            ├────────────────────┼────────────────────┤
            │ 1. Pause Reddit    │ 2. Twitter         │
            │ 5. Video Content   │    Frequency       │
Low Impact  │ (Low Effort)       │ (Low Effort)       │
            └────────────────────┴────────────────────┘
             Low Effort          High Effort
```

**Recommended Order**:
1. Quick Wins (#1, #2) - Do this week
2. A/B Headlines (#3) - Start next week
3. Landing Page (#4) - Q1 priority project
4. Experiments (#5, #6) - If capacity allows

---

### 📈 Expected Cumulative Impact

If all high-priority optimizations are implemented:

| Metric | Current | After Optimizations | Improvement |
|--------|---------|---------------------|-------------|
| CTR | 1.2% | 1.8% | +50% |
| Conversions | 260 | 520 | +100% |
| CPA | $18.85 | $12.50 | -34% |
| ROI | 13.3x | 20x | +50% |

---

### 🎯 Next Steps

1. **Immediate** (This Week):
   - [ ] Execute Quick Win #1 (pause Reddit)
   - [ ] Execute Quick Win #2 (Twitter frequency)

2. **Short-Term** (Next 2 Weeks):
   - [ ] Implement A/B headline test
   - [ ] Analyze results and scale winner

3. **Long-Term** (Q1 2026):
   - [ ] Kickoff landing page redesign project
   - [ ] Allocate dev resources

4. **Optional** (If Capacity):
   - [ ] Try video content experiment
   - [ ] Explore influencer partnerships

---

**Report Generated**: 2025-11-15 12:00 UTC
```

## Success Criteria

- At least 5 optimization suggestions
- Clear prioritization (effort vs impact)
- Actionable implementation steps
- Quantified expected impact

## Example Interaction

```
User: /marketing.optimize.suggest campaign q4-awareness-launch

AI: Analyzing 'q4-awareness-launch' for optimization opportunities...

Current Status:
- 3/4 metrics met
- CTR below target (1.2% vs 2%)
- Reddit underperforming ($45 CPA vs $18 avg)

[Displays complete optimization report]

🎯 Top 3 Recommendations:
1. ⚡ QUICK WIN: Pause Reddit ($500 savings)
2. 📈 HIGH IMPACT: A/B test headlines (+50% CTR)
3. 🎨 STRATEGIC: Redesign landing page (+900% conversions)

Would you like me to:
A) Create an implementation plan for Quick Wins
B) Help you set up the A/B test
C) Draft a landing page redesign brief
```

