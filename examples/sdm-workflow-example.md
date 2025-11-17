# SDM Workflow Example

完整的营销规划和优化闭环示例。

---

## 🎯 场景

**目标**：为 MetaSpec 项目规划 Q1 2025 开发者增长活动，并在执行后进行优化。

**预算**：$10,000  
**周期**：11 周（2025-01-15 到 2025-03-31）  
**团队**：4 人（内容、设计、社媒、负责人）

---

## 📋 第一期活动：规划阶段（8 步）

### 1. 定义营销原则（可选）

```bash
/marketspec.constitution
```

**AI 输出**：
```markdown
# Marketing Constitution - MetaSpec

## Core Principles

1. **Developer-First**
   - Speak developer language
   - Focus on technical value
   - Avoid marketing jargon

2. **Open & Transparent**
   - Share metrics publicly
   - Acknowledge failures
   - Community-driven roadmap

3. **Quality Over Quantity**
   - Deep technical content
   - No clickbait
   - Long-term relationships

4. **Data-Driven**
   - Track everything
   - A/B test decisions
   - Optimize continuously

5. **Community-Centric**
   - Listen to feedback
   - Engage authentically
   - Give back to OSS

## Quality Standards

- All content must be technically accurate
- All claims must be verifiable
- All metrics must be public

## Prohibited Practices

- No buying followers/stars
- No spam or mass DMs
- No misleading comparisons
```

**保存到**：`memory/marketing-constitution.md`

---

### 2. 发现营销需求（必需）

```bash
/marketspec.discover "Grow MetaSpec developer user base in Q1 2025"
```

**AI 交互**：
```
AI: I'll help you discover your marketing needs for MetaSpec.

Let's start with some questions:

1️⃣ What's your primary goal for Q1 2025?
   > Increase GitHub stars from 50 to 500

2️⃣ Who is your target audience?
   > Senior Python/JavaScript developers (5+ years exp)
   > Engineering managers evaluating tools

3️⃣ What's your budget?
   > $10,000

4️⃣ What channels are you currently using?
   > Blog, Twitter (small following)

5️⃣ What's worked in the past?
   > Technical tutorials on our blog got good engagement

6️⃣ What hasn't worked?
   > Product announcements on LinkedIn got no traction

---

✅ Discovery Complete!

Key findings:
- Ambitious growth target (10x GitHub stars)
- Technical audience prefers depth over breadth
- Limited budget requires high ROI channels
- Blog content is a proven strength
- Need to expand beyond current channels

📄 Saved to: specs/discovery/metaspec-q1-2025-discovery.md
```

---

### 3. 澄清需求（可选）

```bash
/marketspec.clarify
```

**AI 交互**：
```
AI: I've reviewed your discovery document. Let me clarify some ambiguities:

❓ Question 1: GitHub Stars Goal
Your target is 500 stars (10x growth). This is ambitious.
- Conservative target: 200 stars (4x)
- Balanced target: 350 stars (7x)
- Aggressive target: 500 stars (10x)

Which do you prefer, or should we keep 500?
> Keep 500, but add milestone at 350

✅ Clarified: Primary target 500, success milestone 350

---

❓ Question 2: Target Audience Segmentation
You mentioned two segments. Which is higher priority?
- Senior developers (hands-on users)
- Engineering managers (decision-makers)

> Primary: Senior developers (80% effort)
> Secondary: Engineering managers (20% effort)

✅ Clarified: 80/20 split in targeting

---

📄 Saved to: specs/clarifications/metaspec-q1-2025-clarification.md
```

---

### 4. 规划策略（可选）

```bash
/marketspec.strategy
```

**AI 输出**（摘要）：
```yaml
strategy:
  approach: "Developer-first content marketing with community amplification"
  
  campaigns:
    - name: "Developer Onboarding"
      goal: "Drive GitHub stars and email signups"
      duration: "11 weeks"
      budget: 6000
      
    - name: "Power User Stories"
      goal: "Build trust with case studies"
      duration: "6 weeks"
      budget: 4000
  
  channels:
    - dev-blog (owned, high priority)
    - dev-twitter (amplification)
    - dev-to (community reach)
    - reddit-programming (viral potential)
    - github-discussions (community)
  
  content_pillars:
    - Technical tutorials
    - Case studies
    - Tool comparisons
  
  budget_allocation:
    content_creation: 4000
    paid_promotion: 3000
    tools: 1500
    community: 1000
    contingency: 500
```

**保存到**：`specs/strategy/metaspec-q1-2025-strategy.md`

---

### 5. 质量检查（推荐）

```bash
/marketspec.checklist
```

**AI 输出**：
```
✅ Strategy Validation

Automated Checks (6/6 passed):
✅ Budget sums correctly ($10,000)
✅ Timeline is realistic (11 weeks)
✅ Channels are well-distributed (5 channels)
✅ Campaigns cover full period
✅ Target audience addressed in strategy
✅ All objectives have supporting campaigns

Manual Review Checklist (46 items):
- Strategic Alignment (8 items)
- Target Audience (6 items)
- Budget Allocation (8 items)
- Channel Selection (7 items)
- Content Strategy (8 items)
- Execution Feasibility (9 items)

📄 Full checklist: marketing-spec-checklist.md

✅ Ready to proceed to task breakdown!
```

---

### 6. 分解任务（可选）

```bash
/marketspec.tasks
```

**AI 输出**（摘要）：
```yaml
tasks:
  setup_phase:
    - SETUP-001: Configure analytics (Google Analytics, social tracking)
    - SETUP-002: Set up ConvertKit for email
    - SETUP-003: Create content calendar
  
  content_phase:
    - CONTENT-001: Write 5 technical tutorials
    - CONTENT-002: Create 3 case studies
    - CONTENT-003: Design visuals (12 graphics)
  
  distribution_phase:
    - DIST-001: Publish blog posts (weekly)
    - DIST-002: Share on Reddit (12 posts)
    - DIST-003: Cross-post to Dev.to
  
  engagement_phase:
    - ENGAGE-001: Respond to comments (<1hr)
    - ENGAGE-002: Host GitHub Discussions
    - ENGAGE-003: Weekly community check-ins
  
  optimization_phase:
    - OPT-001: Weekly analytics review
    - OPT-002: A/B test headlines
    - OPT-003: Adjust based on performance

Total: 25 tasks, 480 hours, $10,000 budget
```

**保存到**：`specs/tasks/metaspec-q1-2025-tasks.md`

---

### 7. 一致性检查（可选）

```bash
/marketspec.analyze
```

**AI 输出**：
```
📊 Consistency Analysis

Checking 7 categories across 4 documents...

✅ Objective Alignment: 100% (all objectives addressed)
✅ Budget Consistency: 100% (all numbers match)
✅ Timeline Coherence: 100% (no conflicts)
⚠️ Coverage Analysis: 92% (minor gap in email tactics)
⚠️ Entity References: 95% (1 undefined channel reference)
✅ KPI Consistency: 95% (minor tracking setup issue)
⚠️ Resource Allocation: 85% (capacity mismatch)

Overall Consistency: 92/100 (A-)

Issues Found (5):
1. ⚠️ Channel "github-discussions" referenced but not fully configured
2. ⚠️ Email subscriber growth needs dedicated tactics
3. ℹ️ Content Writer capacity exceeds requirements

✅ Ready to proceed to /marketspec.create

📄 Full report: consistency-report.md
```

---

### 8. 生成规范（必需）

```bash
/marketspec.create
```

**AI 输出**：
```
🎯 Generating marketing-spec.yaml...

Step 1/13: Creating project metadata... ✅
Step 2/13: Defining marketing plans... ✅
Step 3/13: Configuring products... ✅
Step 4/13: Setting up campaigns... ✅
Step 5/13: Defining channels... ✅
Step 6/13: Planning content... ✅
Step 7/13: Allocating budget... ✅
Step 8/13: Setting up tracking... ✅
Step 9/13: Configuring analytics... ✅
Step 10/13: Defining team roles... ✅
Step 11/13: Creating milestones... ✅
Step 12/13: Validating specification... ✅
Step 13/13: Writing YAML file... ✅

✅ Successfully generated marketing-spec.yaml (450 lines)

Summary:
- 1 marketing plan
- 2 campaigns
- 5 channels
- 12 content pieces
- $10,000 budget
- 11-week timeline

📄 Output: marketing-spec.yaml

Ready to execute! 🚀
```

---

## 🚀 执行阶段（11 周）

活动按计划执行...

**实际结果**（11 周后）：
- GitHub Stars: 420（目标 500）
- Email Subscribers: 850（目标 1,000）
- Website Traffic: 45,000（目标 50,000）
- 预算支出: $9,500（预算 $10,000）

---

## 📊 回顾优化阶段（2 步）

### 9. 分析实际效果

```bash
/marketspec.review
```

**AI 交互**：
```
AI: Let's review your campaign performance!

📄 Loaded: marketing-spec.yaml
📅 Period: 2025-01-15 to 2025-03-31 (11 weeks)

---

Please provide actual results:

1️⃣ GitHub Stars
   Planned: 50 → 500 (+450)
   > Actual: 420

2️⃣ Email Subscribers
   Planned: 100 → 1,000 (+900)
   > Actual: 850

3️⃣ Website Traffic
   Planned: 500 → 50,000 (+49,500)
   > Actual: 45000

4️⃣ Total Spent
   Planned: $10,000
   > Actual: 9500

---

✅ Analysis Complete!

Achievement Summary:
- GitHub Stars: 420 (82% of target) ⚠️
- Email Subscribers: 850 (83% of target) ⚠️
- Website Traffic: 45,000 (90% of target) ⚠️
- Budget: $9,500 (95% utilized) ✅

Overall Achievement: 85.1% (B+)
ROI: 154% (Excellent!)

Top Performers:
✅ Reddit (ROI: 9/10) - Best cost-per-star
✅ Dev.to (ROI: 8/10) - Strong engagement
✅ Blog (ROI: 8/10) - High conversions

Underperformers:
⚠️ LinkedIn (ROI: 4/10) - Wrong audience fit

Key Insights:
- Tutorial content outperformed announcements 3:1
- Growth plateaued in weeks 8-11 (content fatigue)
- No dedicated email lead magnet hurt conversions
- Community-driven channels (Reddit, Dev.to) performed best

📄 Full report: campaign-review.md
```

---

### 10. 生成优化建议

```bash
/marketspec.optimize
```

**AI 输出**（摘要）：
```
📈 Optimization Recommendations

Based on your 85.1% achievement rate, here are data-driven recommendations:

🔴 High Impact Changes:

1. Budget Reallocation: LinkedIn → Reddit/Dev.to
   - Current: LinkedIn $1,000 (ROI 4) → Recommended: $300
   - Increase: Reddit $500 → $1,000 (+$500)
   - Increase: Dev.to $800 → $1,200 (+$400)
   - Expected Impact: +50-80 GitHub stars

2. Add Email Lead Magnet
   - Current: No lead magnet, 850 subscribers
   - Recommended: Create "MetaSpec Quick Start Guide" PDF
   - Expected Impact: +200-300 subscribers

3. Content Variety (Prevent Plateau)
   - Problem: Growth plateaued weeks 8-11
   - Solution: Add developer stories, live coding
   - Expected Impact: Sustain 60 stars/week through week 11

---

Budget Scenarios:

Conservative ($10K, same budget):
- Expected achievement: 90-93% (+5-8%)
- Key changes: Reallocate within categories

Balanced ($10K, bigger shifts):
- Expected achievement: 95-100% (+10-15%)
- Key changes: Cut LinkedIn 70%, double Reddit

Aggressive ($15K, increased budget):
- Expected achievement: 110-120% (+25-35%)
- Key changes: Scale what works, test YouTube

---

Recommended KPI Targets (Next Campaign):

| KPI | Last Target | Achievement | Next Target | Increase |
|-----|-------------|-------------|-------------|----------|
| GitHub Stars | 500 | 84% (420) | 520 | +24% |
| Email Subscribers | 1,000 | 85% (850) | 1,100 | +29% |
| Website Traffic | 50,000 | 90% (45K) | 60,000 | +33% |

---

Implementation Roadmap:

⚡ Immediate (Week 1-2): $700, 32 hours
- Create email lead magnet
- Optimize email CTAs

📅 Short-term (Week 3-4): $2,000, 52 hours
- Expand Reddit presence
- Create first 3 video tutorials

🎯 Medium-term (Week 5-8): $2,000, 88 hours
- Launch Dev.to series
- Test HackerNews

---

Expected Results (Balanced Scenario):
- GitHub Stars: 520 → 95% of target ✅
- Email Subscribers: 1,100 → 100% of target ✅
- Website Traffic: 60,000 → 100% of target ✅
- Overall Achievement: 95-100% (up from 85%)

📄 Full recommendations: optimization-recommendations.md

Ready to start Q2 campaign with these insights! 🚀
```

---

## 🔄 第二期活动：应用优化建议

### 基于优化建议开始新一轮

```bash
/marketspec.discover "Q2 2025 Growth with Q1 Learnings" --based-on optimization-recommendations.md
```

**AI 输出**：
```
AI: I'll help you plan Q2 based on Q1 learnings!

📄 Loaded Q1 optimization recommendations

Key learnings applied:
✅ Reddit budget increased: $500 → $1,000
✅ LinkedIn reduced: $1,000 → $300
✅ Lead magnet planned: "MetaSpec Quick Start Guide"
✅ Content variety: Added developer stories + live coding
✅ Targets adjusted: Stars 500→520, Email 1000→1100

Let me ask a few questions about Q2:

1️⃣ Will your total budget change?
   Q1: $10,000
   > Q2: $12,000 (20% increase based on Q1 ROI)

2️⃣ Any new channels to test?
   Q1 best performers: Reddit, Dev.to, Blog
   > Yes, test YouTube (recommended in optimization)

3️⃣ Team capacity changes?
   > Same team, but add 10 hrs/week for video content

---

✅ Q2 Discovery Complete with Q1 optimizations applied!

This is continuous improvement in action! 🎉

📄 Saved to: specs/discovery/metaspec-q2-2025-discovery.md
```

**继续 Q2 规划**：strategy → tasks → create...

---

## 📊 完整闭环示意图

```
┌─────────────────────────────────────────────────────┐
│              Q1 Campaign (规划阶段)                    │
├─────────────────────────────────────────────────────┤
│ 1. constitution  → 定义原则                          │
│ 2. discover      → 发现需求 (目标: 500 stars)         │
│ 3. clarify       → 澄清目标                          │
│ 4. strategy      → 规划策略 (预算: $10K)              │
│ 5. checklist     → 质量检查                          │
│ 6. tasks         → 分解任务 (25 tasks)                │
│ 7. analyze       → 一致性检查                         │
│ 8. create        → 生成 YAML                         │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│              Q1 Campaign (执行阶段)                    │
├─────────────────────────────────────────────────────┤
│ 执行活动 11 周...                                      │
│                                                     │
│ 结果:                                                │
│ - Stars: 420 (84%)                                 │
│ - Email: 850 (85%)                                 │
│ - Traffic: 45K (90%)                               │
│ - ROI: 154%                                        │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│            Q1 Campaign (回顾优化阶段)                  │
├─────────────────────────────────────────────────────┤
│ 9. review        → 分析实际效果                       │
│                    - Reddit 表现最好 (ROI 9/10)      │
│                    - LinkedIn 表现差 (ROI 4/10)      │
│                    - 需要 lead magnet               │
│                                                     │
│ 10. optimize     → 生成优化建议                       │
│                    - 预算重分配方案                   │
│                    - 新 KPI 目标                     │
│                    - 实施路线图                      │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│              Q2 Campaign (规划阶段)                    │
├─────────────────────────────────────────────────────┤
│ 1. discover      → 应用 Q1 learnings                 │
│                    - Stars 目标: 520 (调整后)        │
│                    - Reddit 预算: $1,000 (翻倍)      │
│                    - 添加 lead magnet                │
│                    - 预期达成率: 95-100%             │
│                                                     │
│ 2-8. 继续完整流程...                                  │
└─────────────────────────────────────────────────────┘
                        ↓
                     持续改进...
```

---

## 🎯 关键要点

### 1. 灵活的工作流

**最小流程**（快速测试）：
```bash
discover → create
```

**推荐流程**（标准项目）：
```bash
discover → clarify → strategy → create → checklist
```

**完整规划**（复杂项目）：
```bash
constitution → discover → clarify → strategy → 
checklist → tasks → analyze → create
```

**闭环优化**（持续改进）：
```bash
完整规划 → [执行] → review → optimize → 下一期 discover
```

### 2. 数据驱动的改进

- Q1：凭经验规划，85% 达成率
- Q2：基于 Q1 数据优化，预期 95-100% 达成率
- Q3：基于 Q2 数据继续优化...

### 3. 命令类型

- 🔴 **Required (2)**：discover, create
- 🟡 **Recommended (1)**：checklist
- ⚪ **Optional (7)**：根据项目复杂度选择

### 4. 输出文件

**规划阶段**：
- `memory/marketing-constitution.md`
- `specs/discovery/*.md`
- `specs/clarifications/*.md`
- `specs/strategy/*.md`
- `specs/tasks/*.md`
- `consistency-report.md`
- `marketing-spec.yaml` ⭐（核心输出）

**执行后**：
- `campaign-review.md`
- `optimization-recommendations.md`

---

## 💡 最佳实践

### 1. 首次使用

如果是第一次使用 marketing-spec-kit：
1. 从最小流程开始（discover → create）
2. 熟悉后逐步添加其他步骤
3. 复杂项目才使用完整 8 步

### 2. 闭环优化

确保每期活动都执行 review → optimize：
- 积累数据资产
- 避免重复错误
- 持续提升 ROI

### 3. 文档保存

妥善保存所有输出文档：
- 规划文档可复用
- review 是宝贵的学习资料
- optimize 建议可应用多期

### 4. 团队协作

- constitution：团队共同制定
- discover/strategy：营销负责人主导
- review：全团队参与复盘
- optimize：基于数据客观分析

---

**恭喜！你已掌握完整的 SDM 闭环营销系统！** 🎉

