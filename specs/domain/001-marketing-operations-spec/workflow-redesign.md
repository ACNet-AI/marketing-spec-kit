# Marketing Operations Workflow 重设计方案

**版本**: 2.0.0-draft  
**日期**: 2025-11-15  
**状态**: 设计中  
**类型**: 架构级改进提案

---

## 🎯 改进目标

### 当前问题

**v1.0.0的设计（"工具箱"模式）**：
```yaml
实体: Project, Product, Campaign, Channel, Tool, ContentTemplate, Milestone
命令: 
  - 7个读取命令 (/marketing.project, /marketing.product, ...)
  - 4个生成命令 (/marketing.generate.post, ...)
  - 2个执行命令 (/marketing.execute.schedule, ...)

问题:
  ❌ 用户不知道从哪里开始
  ❌ 命令之间没有明确的先后顺序
  ❌ 缺少整体战略管理（Plan）
  ❌ 无法追踪从战略到执行的完整路径
```

### 设计目标

**v2.0.0的设计（"工作流系统"模式）**：
```yaml
目标:
  ✅ 定义清晰的5阶段工作流
  ✅ 每个阶段有明确的目标、输入、输出
  ✅ 命令映射到工作流阶段
  ✅ 添加Plan实体管理整体战略
  ✅ 支持从战略规划到效果分析的完整闭环
```

---

## 📊 完整工作流架构

### 工作流概览

```
┌─────────────────────────────────────────────────────────────────┐
│                   Marketing Operations Workflow                 │
└─────────────────────────────────────────────────────────────────┘

Phase 1: Strategic Planning (战略规划)
   ↓
   定义营销方案、目标、预算、受众
   输出: MarketingPlan 实体
   
Phase 2: Campaign Design (活动设计)
   ↓
   基于Plan设计具体的Campaign
   输出: Campaign 实体
   
Phase 3: Content Creation (内容创作)
   ↓
   为Campaign生成各渠道内容
   输出: 可发布的内容资产
   
Phase 4: Execution & Publishing (执行发布)
   ↓
   发布内容到各个渠道
   输出: 已发布的内容，开始收集数据
   
Phase 5: Analytics & Optimization (效果分析)
   ↓
   追踪KPI，生成报告，优化建议
   输出: Analytics报告，优化方案
   
   ↺ 循环回Phase 1或Phase 2
```

---

## 🏗️ Phase 1: Strategic Planning (战略规划)

### 阶段目标

定义营销方案的整体战略，包括目标、受众、预算、周期。

### 输入条件

- ✅ Project已定义（品牌identity）
- ✅ Products已定义（产品特性）
- ✅ 业务目标明确（增长、品牌、转化等）

### 核心实体：MarketingPlan（新增）

```yaml
MarketingPlan:
  id: string                    # 方案唯一ID
  name: string                  # 方案名称
  project_id: string            # 关联的Project
  
  # 战略定义
  period:
    start_date: string          # ISO 8601 日期
    end_date: string            # ISO 8601 日期
    duration_weeks: number      # 周期（周）
  
  objectives: array[string]     # SMART目标
    # 例如: "Q1实现10K GitHub stars"
    # 例如: "6个月内获得5000个注册用户"
  
  target_audience: array[object]
    - segment: string           # 受众细分
      description: string       # 描述
      size_estimate: number     # 预估规模
      priority: enum[high, medium, low]
  
  strategies: array[object]     # 核心策略
    - name: string              # 策略名称
      description: string       # 策略描述
      rationale: string         # 选择理由
      success_criteria: string  # 成功标准
  
  # 预算分配
  budget:
    total: number               # 总预算
    currency: string            # 货币单位
    allocation: object          # 分配
      content_creation: number  # 内容创作预算
      paid_promotion: number    # 付费推广预算
      tools: number             # 工具费用
      contingency: number       # 应急预算
  
  # KPI定义
  kpis: array[object]
    - name: string              # KPI名称
      target: number            # 目标值
      unit: string              # 单位
      measurement: string       # 测量方法
      priority: enum[P0, P1, P2]
  
  # 关联的Campaign（后续填充）
  campaign_ids: array[string]   # Campaign列表
  
  # 状态管理
  status: enum[draft, approved, active, completed, archived]
  created_at: string
  updated_at: string
  
  # 审批信息（可选）
  approval:
    approved_by: string
    approved_at: string
    comments: string
```

### 阶段操作

#### 1. `/marketing.plan.create`

**用途**: 创建新的营销方案

**输入参数**:
```yaml
name: string              # 方案名称
period_weeks: number      # 周期（周）
objectives: array[string] # SMART目标
budget_total: number      # 总预算
```

**输出**:
```yaml
plan_id: string           # 新创建的Plan ID
status: "draft"
next_steps:
  - "完善target_audience"
  - "定义核心strategies"
  - "设置KPIs"
  - "运行 /marketing.plan.validate"
```

**示例**:
```
AI: "我将为MetaSpec创建Q1营销方案..."

/marketing.plan.create 
  name="MetaSpec Q1 2025 Growth Plan"
  period_weeks=12
  objectives=["Reach 10K GitHub stars", "Acquire 5K developers"]
  budget_total=5000

AI: "✅ Plan created (ID: plan-001)
    📝 Next: Define target audience and strategies"
```

---

#### 2. `/marketing.plan.validate`

**用途**: 验证方案的完整性和合理性

**验证规则**:
- ✅ Objectives是否符合SMART原则
- ✅ 预算分配是否合理（总和=100%）
- ✅ KPIs是否可测量
- ✅ 周期是否合理（4-52周）
- ✅ Target audience是否明确

**输出**:
```yaml
validation_result:
  score: 85/100
  errors: []
  warnings:
    - "KPI 'brand awareness' 缺少具体测量方法"
  suggestions:
    - "建议为每个strategy添加success_criteria"
```

---

#### 3. `/marketing.plan.get`

**用途**: 检索方案详情

**输入**: `plan_id: string`

**输出**: 完整的Plan实体JSON

---

#### 4. `/marketing.plan.analyze`

**用途**: AI分析方案，给出改进建议

**分析维度**:
- 目标可实现性
- 预算合理性
- 策略一致性
- KPI覆盖度
- 竞争对手对比

**输出**:
```yaml
analysis:
  feasibility_score: 80/100
  strengths:
    - "目标明确且可测量"
    - "预算分配合理"
  risks:
    - "预算偏低，可能影响付费推广效果"
  recommendations:
    - "建议增加20%预算用于内容创作"
    - "建议添加'社区参与度'作为KPI"
```

---

### 输出产物

- ✅ **MarketingPlan实体**（已验证）
- ✅ **预算分配表**
- ✅ **KPI仪表盘定义**

### 质量门

在进入Phase 2之前：
- ✅ Plan状态必须是`approved`
- ✅ 所有P0 KPIs已定义
- ✅ 预算分配总和=100%
- ✅ 至少定义2个target audience segments

---

## 🎨 Phase 2: Campaign Design (活动设计)

### 阶段目标

基于MarketingPlan，设计具体的Campaign来实现战略目标。

### 输入条件

- ✅ MarketingPlan已批准（status=approved）
- ✅ Project和Products已定义
- ✅ Channels已配置

### 阶段操作

#### 1. `/marketing.campaign.design` ⭐ **新命令**

**用途**: AI基于Plan自动设计Campaign建议

**输入参数**:
```yaml
plan_id: string           # 基于哪个Plan
num_campaigns: number     # 建议生成几个Campaign（默认3-5）
focus: enum[awareness, consideration, conversion] # 侧重点（可选）
```

**AI处理逻辑**:
1. 读取Plan的objectives和strategies
2. 分析target_audience
3. 检查可用的Channels
4. 生成3-5个互补的Campaign建议

**输出**:
```yaml
campaign_suggestions:
  - name: "Open Source Launch Campaign"
    goal: "awareness"
    rationale: "对应Plan目标: Reach 10K GitHub stars"
    recommended_channels: ["github", "twitter", "reddit"]
    estimated_budget: 1500
    duration_weeks: 4
    expected_kpis:
      github_stars: 5000
      twitter_impressions: 100000
    
  - name: "Developer Onboarding Campaign"
    goal: "consideration"
    rationale: "对应Plan目标: Acquire 5K developers"
    recommended_channels: ["blog", "youtube", "email"]
    estimated_budget: 2000
    duration_weeks: 8
    expected_kpis:
      signups: 3000
      tutorial_completions: 1500
```

**示例**:
```
User: "基于Q1 Plan设计Campaign"

AI: "分析Plan目标和预算..."

/marketing.campaign.design 
  plan_id="plan-001"
  num_campaigns=3

AI: "✅ 生成3个Campaign建议：
     1. Launch Campaign (awareness) - $1.5K, 4周
     2. Onboarding Campaign (consideration) - $2K, 8周  
     3. Conversion Campaign (conversion) - $1K, 4周
     
     这3个Campaign覆盖完整漏斗，预算总计$4.5K（符合Plan预算$5K）
     
     下一步: 选择要实施的Campaign，运行 /marketing.campaign.create"
```

---

#### 2. `/marketing.campaign.create`

**用途**: 创建Campaign（手动或基于AI建议）

**改进点**:
```yaml
新增字段:
  plan_id: string          # 必须关联到Plan
  expected_kpis: object    # 预期KPI（从Plan继承）
```

**验证规则（新增）**:
- ✅ Campaign.budget ≤ Plan剩余预算
- ✅ Campaign.channels在Plan允许的范围内
- ✅ Campaign日期在Plan period范围内

---

#### 3. `/marketing.campaign.get`

**用途**: 检索Campaign详情（已有，保持不变）

---

### 输出产物

- ✅ **Campaign实体列表**（关联到Plan）
- ✅ **Campaign时间表**
- ✅ **预算使用追踪**

### 质量门

在进入Phase 3之前：
- ✅ 至少创建1个Campaign
- ✅ Campaign总预算 ≤ Plan预算
- ✅ 每个Campaign至少关联1个Channel
- ✅ 每个Campaign定义了明确的goal和KPI

---

## ✍️ Phase 3: Content Creation (内容创作)

### 阶段目标

为Campaign生成各渠道的营销内容。

### 输入条件

- ✅ Campaign已创建
- ✅ Channels已配置
- ✅ ContentTemplates已定义（品牌指南）

### 阶段操作

#### 1. `/marketing.content.plan` ⭐ **新命令**

**用途**: 为Campaign生成内容日历

**输入参数**:
```yaml
campaign_id: string       # 为哪个Campaign规划内容
frequency: string         # 发布频率 "daily" | "weekly" | "custom"
duration_weeks: number    # 持续周数（默认从Campaign获取）
```

**输出**:
```yaml
content_calendar:
  campaign_id: "camp-001"
  campaign_name: "Open Source Launch"
  schedule:
    - date: "2025-11-18"
      content_type: "announcement"
      channel: "twitter"
      title: "Announcing MetaSpec v0.6.0"
      status: "planned"
      
    - date: "2025-11-18"
      content_type: "blog_post"
      channel: "blog"
      title: "What's New in MetaSpec v0.6.0"
      status: "planned"
      
    - date: "2025-11-19"
      content_type: "tutorial"
      channel: "youtube"
      title: "Getting Started with MetaSpec"
      status: "planned"
      
  summary:
    total_content_pieces: 15
    by_channel:
      twitter: 8
      blog: 4
      youtube: 3
```

**示例**:
```
User: "为Launch Campaign规划内容"

AI: "分析Campaign目标和渠道..."

/marketing.content.plan
  campaign_id="camp-001"
  frequency="daily"
  duration_weeks=4

AI: "✅ 生成4周内容日历，共15个内容：
     - Twitter: 8 posts (发布、更新、案例、互动)
     - Blog: 4 articles (公告、教程、最佳实践、案例)
     - YouTube: 3 videos (快速上手、深入教程、Q&A)
     
     下一步: 使用 /marketing.generate.* 命令创建内容"
```

---

#### 2. `/marketing.generate.post` （改进）

**改进点**:
```yaml
新增参数:
  campaign_id: string      # 关联到Campaign
  content_calendar_id: string  # 关联到内容日历条目

改进逻辑:
  1. 读取Campaign的goal和messaging
  2. 读取Plan的target_audience
  3. 确保内容符合Campaign主题
  4. 自动标记内容日历条目为"created"
```

---

#### 3. `/marketing.generate.article` （改进）
#### 4. `/marketing.generate.email` （改进）
#### 5. `/marketing.generate.landing_page` （改进）

**改进方式同上**：添加campaign_id关联，确保内容一致性

---

### 输出产物

- ✅ **内容日历**（15-30个内容条目）
- ✅ **已生成的内容资产**（文本、图片、视频脚本）
- ✅ **内容审核报告**

### 质量门

在进入Phase 4之前：
- ✅ 至少50%的计划内容已创建
- ✅ 所有内容通过品牌一致性检查
- ✅ 所有内容符合Channel要求（字数、格式等）

---

## 🚀 Phase 4: Execution & Publishing (执行发布)

### 阶段目标

将内容发布到各个渠道，开始Campaign执行。

### 输入条件

- ✅ 内容已创建并审核通过
- ✅ Channels已配置且可用
- ✅ Campaign开始日期已到

### 阶段操作

#### 1. `/marketing.execute.schedule` （改进）

**改进点**:
```yaml
新增参数:
  campaign_id: string      # 关联到Campaign
  content_calendar_id: string  # 关联到内容日历

改进逻辑:
  1. 验证内容是否符合Campaign时间表
  2. 检查Channel是否在Campaign允许列表中
  3. 自动更新内容日历状态为"scheduled"
  4. 追踪Campaign执行进度
```

---

#### 2. `/marketing.execute.publish` （改进）

**改进点**:
```yaml
新增参数:
  campaign_id: string      # 关联到Campaign

改进逻辑:
  1. 立即发布到Channel
  2. 更新内容日历状态为"published"
  3. 开始追踪该内容的KPI数据
  4. 触发Analytics数据收集
```

---

### 输出产物

- ✅ **已发布的内容**（在各个Channel上线）
- ✅ **发布日志**（时间、渠道、状态）
- ✅ **开始收集KPI数据**

### 质量门

在进入Phase 5之前：
- ✅ Campaign至少发布了首批内容
- ✅ 所有Channel的发布都成功
- ✅ 数据追踪已启动

---

## 📊 Phase 5: Analytics & Optimization (效果分析)

### 阶段目标

追踪Campaign和Plan的KPI达成情况，生成报告，提出优化建议。

### 输入条件

- ✅ Campaign已运行至少1周
- ✅ KPI数据已收集
- ✅ 有足够的数据样本

### 核心实体：Analytics（新增）

```yaml
Analytics:
  id: string
  type: enum[campaign, plan]  # 分析Campaign或Plan
  entity_id: string            # Campaign ID或Plan ID
  
  period:
    start_date: string
    end_date: string
  
  # KPI实际值
  metrics: object
    # 例如:
    github_stars: 3500        # 实际值
    twitter_impressions: 85000
    signups: 2800
  
  # 对比目标
  vs_target: object
    github_stars:
      target: 5000
      actual: 3500
      achievement: 70%
      status: "below_target"
    
    twitter_impressions:
      target: 100000
      actual: 85000
      achievement: 85%
      status: "on_track"
  
  # AI生成的洞察
  insights: array[object]
    - type: enum[success, concern, opportunity]
      description: string
      evidence: string
      recommendation: string
  
  # 建议的优化措施
  optimizations: array[object]
    - priority: enum[high, medium, low]
      action: string
      expected_impact: string
      effort: enum[low, medium, high]
  
  generated_at: string
```

### 阶段操作

#### 1. `/marketing.analytics.campaign` ⭐ **新命令**

**用途**: 生成Campaign效果分析报告

**输入参数**:
```yaml
campaign_id: string       # Campaign ID
include_recommendations: boolean  # 是否包含优化建议（默认true）
```

**输出**:
```yaml
analytics_report:
  campaign_id: "camp-001"
  campaign_name: "Open Source Launch"
  status: "active"
  progress: 50%  # 时间进度
  
  kpi_summary:
    github_stars:
      target: 5000
      actual: 3500
      achievement: 70%
      trend: "↗️ +200/week"
      status: "below_target"
    
    twitter_impressions:
      target: 100000
      actual: 85000
      achievement: 85%
      trend: "↗️ +15K/week"
      status: "on_track"
  
  insights:
    - type: "concern"
      description: "GitHub stars增长速度低于预期"
      evidence: "当前周均+200，需要+350才能达标"
      recommendation: "增加技术博客内容，提高开发者社区曝光"
    
    - type: "success"
      description: "Twitter互动率高于行业平均"
      evidence: "CTR 3.2% vs 行业平均2.1%"
      recommendation: "继续当前内容策略，增加发布频率"
  
  optimizations:
    - priority: "high"
      action: "在Reddit r/programming发布技术案例"
      expected_impact: "+500 GitHub stars"
      effort: "medium"
    
    - priority: "medium"
      action: "与3个技术KOL合作推广"
      expected_impact: "+30K Twitter impressions"
      effort: "high"
```

**示例**:
```
User: "分析Launch Campaign效果"

AI: "正在分析Campaign数据..."

/marketing.analytics.campaign
  campaign_id="camp-001"
  include_recommendations=true

AI: "📊 Campaign分析报告:
     
     ✅ 进展: 50% (2周/4周)
     
     KPI达成:
     • GitHub stars: 70% ⚠️ 低于预期
     • Twitter曝光: 85% ✅ 正常
     
     🔍 关键洞察:
     1. GitHub增长慢，需要更多技术内容
     2. Twitter互动率很好，建议增加频率
     
     🎯 优化建议:
     1. [High] 在Reddit发布技术案例 → +500 stars
     2. [Med] 与KOL合作 → +30K impressions
     
     是否需要调整Campaign策略？"
```

---

#### 2. `/marketing.analytics.plan` ⭐ **新命令**

**用途**: 生成Plan整体效果分析

**输入参数**:
```yaml
plan_id: string           # Plan ID
include_campaign_breakdown: boolean  # 是否包含Campaign分解（默认true）
```

**输出**:
```yaml
plan_analytics:
  plan_id: "plan-001"
  plan_name: "MetaSpec Q1 2025 Growth Plan"
  progress: 33%  # 时间进度 (4周/12周)
  
  overall_kpis:
    github_stars:
      target: 10000
      actual: 3500
      achievement: 35%
      projected_final: 8500  # AI预测
      status: "at_risk"
    
    developer_signups:
      target: 5000
      actual: 2800
      achievement: 56%
      projected_final: 6200
      status: "on_track"
  
  campaign_breakdown:
    - campaign_id: "camp-001"
      name: "Launch Campaign"
      contribution:
        github_stars: 3500 (100% of current)
        developer_signups: 1500 (54% of current)
      status: "active"
      health: "needs_attention"
    
    - campaign_id: "camp-002"
      name: "Onboarding Campaign"
      contribution:
        developer_signups: 1300 (46% of current)
      status: "active"
      health: "healthy"
  
  budget_usage:
    allocated: 5000
    spent: 2200
    remaining: 2800
    burn_rate: 550_per_week
    projected_final_spend: 4800  # 符合预算
  
  strategic_insights:
    - type: "risk"
      description: "GitHub stars可能无法达到10K目标"
      impact: "high"
      recommendation: "启动补充Campaign，重点关注开源社区"
    
    - type: "success"
      description: "开发者注册超预期，有望超额完成"
      impact: "high"
      recommendation: "将部分预算从品牌转向转化优化"
```

---

#### 3. `/marketing.optimize.suggest` ⭐ **新命令**

**用途**: 基于Analytics数据，AI提供优化方案

**输入参数**:
```yaml
campaign_id: string       # Campaign ID
focus: enum[performance, budget, channels, content]  # 优化重点（可选）
```

**输出**:
```yaml
optimization_suggestions:
  campaign_id: "camp-001"
  
  quick_wins:  # 低投入高回报
    - action: "调整Twitter发布时间为晚上8-10点"
      reason: "数据显示该时段互动率高30%"
      effort: "low"
      expected_lift: "+10K impressions"
      
    - action: "在GitHub README添加Star号召"
      reason: "当前转化率只有2%，行业平均5%"
      effort: "low"
      expected_lift: "+300 stars"
  
  strategic_adjustments:  # 需要预算/资源
    - action: "增加技术博客内容（每周2篇→3篇）"
      reason: "博客流量→GitHub stars转化率最高(8%)"
      effort: "medium"
      budget_required: 500
      expected_lift: "+800 stars"
    
    - action: "启动Reddit社区推广"
      reason: "技术受众集中，竞品成功案例多"
      effort: "high"
      budget_required: 800
      expected_lift: "+1200 stars"
  
  risk_mitigation:  # 应对风险
    - risk: "GitHub stars增长趋缓"
      mitigation: "启动开发者激励计划（贡献者奖励）"
      effort: "high"
      budget_required: 1000
```

---

### 输出产物

- ✅ **Analytics报告**（Campaign级别和Plan级别）
- ✅ **KPI仪表盘**（实时追踪）
- ✅ **优化建议清单**（可执行的改进措施）

### 质量门

循环条件：
- ✅ 如果KPI达标 → 进入下一个Campaign或Phase 1（新的Plan）
- ⚠️ 如果KPI未达标 → 执行优化建议，返回Phase 3或Phase 4
- ❌ 如果严重偏离 → 返回Phase 2重新设计Campaign

---

## 🔄 完整的命令映射表

### 新增命令（v2.0.0）

| 命令 | 阶段 | 优先级 | 说明 |
|------|------|--------|------|
| `/marketing.plan.create` | Phase 1 | P0 | 创建营销方案 |
| `/marketing.plan.validate` | Phase 1 | P0 | 验证方案完整性 |
| `/marketing.plan.get` | Phase 1 | P0 | 读取方案详情 |
| `/marketing.plan.analyze` | Phase 1 | P1 | AI分析方案 |
| `/marketing.campaign.design` | Phase 2 | P0 | AI设计Campaign |
| `/marketing.content.plan` | Phase 3 | P0 | 生成内容日历 |
| `/marketing.analytics.campaign` | Phase 5 | P0 | Campaign效果分析 |
| `/marketing.analytics.plan` | Phase 5 | P0 | Plan效果分析 |
| `/marketing.optimize.suggest` | Phase 5 | P1 | 优化建议 |

### 改进的现有命令

| 命令 | 改进点 | 优先级 |
|------|--------|--------|
| `/marketing.campaign.create` | 添加plan_id关联、预算验证 | P0 |
| `/marketing.campaign.get` | 显示Plan关联信息 | P1 |
| `/marketing.generate.*` | 添加campaign_id、内容日历关联 | P0 |
| `/marketing.execute.*` | 添加campaign_id、状态追踪 | P0 |

### 保留的现有命令（不变）

| 命令 | 阶段 | 说明 |
|------|------|------|
| `/marketing.project` | 全局 | 读取品牌identity |
| `/marketing.product` | 全局 | 读取产品特性 |
| `/marketing.channel` | 全局 | 读取渠道配置 |
| `/marketing.tool` | 全局 | 读取工具集成 |
| `/marketing.content_template` | Phase 3 | 读取品牌指南 |
| `/marketing.milestone` | 全局 | 读取里程碑事件 |

---

## 📐 新增实体总结

### 1. MarketingPlan

**关系**:
```
Project (1) → MarketingPlan (N)
MarketingPlan (1) → Campaign (N)
MarketingPlan (1) → Analytics (N)
```

**字段**: 17个核心字段（详见Phase 1定义）

---

### 2. ContentCalendar（嵌入到Campaign或独立）

**选项A**: 作为Campaign的子实体（推荐）
```yaml
Campaign:
  ...
  content_calendar:
    entries: array[object]
```

**选项B**: 作为独立实体
```yaml
ContentCalendar:
  id: string
  campaign_id: string
  entries: array[object]
```

**推荐**: 选项A（简化架构）

---

### 3. Analytics

**关系**:
```
Campaign (1) → Analytics (N)
MarketingPlan (1) → Analytics (N)
```

**字段**: 8个核心字段（详见Phase 5定义）

---

## 🎯 实施优先级

### MVP（v2.0.0-alpha）

**必须实现**（2-3天）：
1. ✅ MarketingPlan实体
2. ✅ `/marketing.plan.create`
3. ✅ `/marketing.plan.get`
4. ✅ `/marketing.plan.validate`
5. ✅ `/marketing.campaign.design` (AI)
6. ✅ 改进所有`generate.*`和`execute.*`命令（添加campaign_id）

**目标**: 用户可以创建Plan → 设计Campaign → 生成内容

---

### v2.0.0-beta

**添加**（2-3天）：
1. ✅ `/marketing.content.plan`
2. ✅ Analytics实体
3. ✅ `/marketing.analytics.campaign`
4. ✅ `/marketing.analytics.plan`
5. ✅ `/marketing.optimize.suggest`

**目标**: 完整的闭环（从战略到分析）

---

### v2.0.0 (稳定版)

**完善**（1-2天）：
1. ✅ `/marketing.plan.analyze`（AI深度分析）
2. ✅ 所有命令的错误处理和边界情况
3. ✅ 完整的文档和示例
4. ✅ 集成测试

---

## 📊 对比：v1.0.0 vs v2.0.0

| 维度 | v1.0.0 | v2.0.0 | 改进 |
|------|--------|--------|------|
| **实体数量** | 7 | 9 (+Plan, +Analytics) | +29% |
| **命令数量** | 13 | 22 (+9新命令) | +69% |
| **工作流** | ❌ 无明确定义 | ✅ 5阶段清晰流程 | 质的飞跃 |
| **战略管理** | ❌ 只有零散Campaign | ✅ Plan统一管理 | ✅ |
| **效果追踪** | ❌ 无 | ✅ Analytics + 优化建议 | ✅ |
| **用户体验** | "工具箱"（不知道从哪开始） | "工作流系统"（明确路径） | ✅ |
| **AI辅助** | 只有内容生成 | Campaign设计、分析、优化 | ✅ |

---

## ✅ 成功标准

### 用户体验

**场景**: 用户第一次使用marketing-spec-kit

**v1.0.0体验**:
```
User: "我想推广我的开源项目"
AI: "你可以用这些命令: /marketing.project, /marketing.campaign, ..."
User: "我应该先做什么？" 🤔
AI: "嗯...先定义Project吧..."
Result: ❌ 用户困惑，不知道完整流程
```

**v2.0.0体验**:
```
User: "我想推广我的开源项目"
AI: "让我们从创建营销方案开始！"
    
    Phase 1: 创建营销方案
    /marketing.plan.create 
      name="My Project Q1 Plan"
      ...
    
    ✅ Plan创建完成！
    
    Phase 2: 设计Campaign
    /marketing.campaign.design plan_id="plan-001"
    
    ✅ AI建议3个Campaign...
    
User: "太好了！" ✅
Result: ✅ 用户有清晰的路径，AI引导整个过程
```

---

## 🚀 下一步行动

### 立即行动

1. ✅ **审批这个设计方案**
   - Review工作流的5个阶段
   - Review新增的3个实体
   - Review新增的9个命令

2. ✅ **更新Constitution Part II**
   - 添加原则7 "Workflow Completeness"

3. ✅ **提交Evolution Proposal**
   - 使用 `/metaspec.evolution.proposal`
   - 正式管理这次重大变更

4. ✅ **开始实施**
   - 更新Domain Spec（添加Workflow章节 + 3个新实体）
   - 更新Toolkit Spec（添加9个新命令）
   - 实现代码

---

**设计者**: marketing-spec-kit team  
**审阅者**: [待定]  
**批准日期**: [待定]  
**实施目标**: 2025-11-18开始，1周内完成MVP

