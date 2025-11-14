# Marketing-Spec-Kit - Product Requirements Document

**Version**: 1.0  
**Last Updated**: 2025-11-12  
**Status**: Planning

---

## 📋 项目概述

### 产品定位

**Marketing-Spec-Kit** 是一个市场运营领域的 **Specification Toolkit (Speckit)**，用于定义和验证市场运营规范，驱动 AI Agent 生成内容和执行市场运营任务。

**重要说明**：
- ✅ **marketing-spec-kit 提供**：规范定义、验证工具、AI Agent 指引
- ❌ **marketing-spec-kit 不提供**：内容生成逻辑、任务执行逻辑
- 🤖 **AI Agent 负责**：读取规范 → 生成内容 → 执行任务

**类比理解**：
- **MCP-Spec-Kit**：定义 MCP 服务器规范 → AI 根据规范**生成** MCP 服务器代码
- **Marketing-Spec-Kit**：定义营销活动规范 → AI 根据规范**生成**营销内容和执行任务

### 核心价值主张

- **规范定义**：定义清晰的市场运营规范（目标、策略、渠道、内容）
- **规范验证**：确保营销活动定义完整、一致、符合最佳实践
- **AI 驱动**：通过规范和 Slash Commands 指引 AI Agent 工作

### 第一个用例：MetaSpec 自举

**场景**：MetaSpec 本身需要市场运营来推广框架、吸引用户、建立社区

**目标**：使用 marketing-spec-kit 定义 MetaSpec 的运营规范，驱动 AI 帮助执行运营任务

---

## 🎯 目标用户

### 主要用户画像

**项目运营者**
- 开源项目维护者（需要推广项目、吸引贡献者）
- 产品团队（需要市场推广、用户增长）
- 独立开发者（需要推广自己的产品）

**用户痛点**
- ❌ 不知道如何系统化地做市场运营
- ❌ 缺乏市场营销经验和最佳实践
- ❌ 手动创建营销内容耗时耗力
- ❌ 不知道该在哪些渠道推广
- ❌ 难以保持品牌一致性

**用户期望**
- ✅ 有清晰的市场运营指南和框架
- ✅ AI 帮助生成高质量的营销内容
- ✅ 自动化执行重复性运营任务
- ✅ 确保品牌信息一致性

---

## 🎨 核心功能

### Speckit 职责边界

**marketing-spec-kit（规范工具包）提供**：
1. ✅ 规范定义：定义营销活动的结构和约束
2. ✅ 规范验证：检查营销规范是否完整、一致
3. ✅ Slash Commands：为 AI Agent 提供规范访问接口
4. ✅ 模板和示例：帮助用户快速创建规范

**AI Agent（如 Claude in Cursor）负责**：
1. 🤖 读取规范：通过 Slash Commands 理解营销要求
2. 🤖 生成内容：基于规范约束生成营销文案
3. 🤖 执行任务：根据规范指引执行运营动作

---

### 功能 1: 规范定义（Speckit 核心）

**目的**：定义市场运营的结构化规范

**规范实体**（初步设想）：
- **Project（项目）**：项目基本信息、品牌定位、核心价值
- **Product/Feature（产品/功能）**：项目下的具体产品或功能模块（如 MetaSpec 的 SDS 命令集、Speckit 生成器等）
- **Campaign（营销活动）**：活动目标、目标受众、执行策略（可关联到特定 Product）
- **Channel（推广渠道）**：社交媒体、论坛、博客、邮件等
- **Tool/Integration（工具/集成）**：MCP 工具或 REST API，用于执行营销任务
- **ContentTemplate（内容模板）**：品牌声音、风格指南、内容约束
- **Milestone（里程碑）**：版本发布、功能上线、社区活动

**实体关系**：
- Project **has many** Products
- Campaign **targets** one or more Products
- Campaign **uses** Channels
- Channel **has** Tools (MCP 优先)
- Tool **executes** marketing actions
- Content **promotes** Product through Channel using Tool

**规范格式**：YAML/JSON Schema

**示例**：
```yaml
# specs/metaspec-marketing.yaml
project:
  name: MetaSpec
  tagline: "Meta-Specification Framework for Spec-Driven Development"
  brand_voice: "Technical, Approachable, Community-driven"
  website: "https://github.com/ACNet-AI/MetaSpec"
  
products:
  - id: speckit-generator
    name: "Speckit Generator"
    description: "Generate spec-driven toolkits with metaspec init"
    target_audience: ["Developers", "AI Agents"]
    key_features:
      - "One-command speckit generation"
      - "Built-in MetaSpec commands"
      - "Template-based initialization"
    
  - id: sds-commands
    name: "SDS Command Set"
    description: "Specification-Driven Specification definition tools"
    target_audience: ["Specification Designers", "Domain Experts"]
    key_features:
      - "Constitution-driven design"
      - "Iterative specification development"
      - "Quality validation"
  
  - id: awesome-spec-kits
    name: "Awesome Spec Kits Community"
    description: "Community registry for MetaSpec-generated speckits"
    target_audience: ["Open Source Contributors", "Speckit Users"]
    key_features:
      - "Discover community speckits"
      - "Contribute your speckits"
      - "Best practice sharing"

tools:
  # MCP 工具（优先）
  - id: twitter-mcp
    name: "Twitter MCP Server"
    type: "mcp"
    mcp_server_name: "@twitter-mcp"
    purpose: "发布推文和管理 Twitter 账号"
    channels: ["twitter"]
    capabilities:
      - "post-tweet"
      - "schedule-tweet"
      - "get-mentions"
    preferred: true
    
  - id: github-mcp
    name: "GitHub MCP Server"
    type: "mcp"
    mcp_server_name: "@github-mcp"
    purpose: "更新 README、发布 Release、管理 Discussions"
    channels: ["github"]
    capabilities:
      - "update-readme"
      - "create-release"
      - "post-discussion"
    preferred: true
  
  # 传统 API（备选方案）
  - id: twitter-api
    name: "Twitter REST API"
    type: "rest-api"
    purpose: "如果没有 MCP，使用 REST API 发布"
    channels: ["twitter"]
    auth_required:
      - "TWITTER_API_KEY"
      - "TWITTER_API_SECRET"
      - "TWITTER_ACCESS_TOKEN"
    fallback_for: "twitter-mcp"
    documentation: "https://developer.twitter.com/en/docs"

campaign:
  id: v0.6.0-launch
  name: "v0.6.0 Community Launch"
  goal: "Attract 100 GitHub stars, 20 community contributors"
  target_audience: ["AI Developers", "Open Source Contributors"]
  focus_products: ["speckit-generator", "awesome-spec-kits"]
  channels: ["twitter", "reddit", "github", "product-hunt"]
  tools_to_use:  # ← 指定活动使用的工具
    - tool_id: twitter-mcp
      usage: "自动发布每日推文"
      frequency: "daily"
    - tool_id: github-mcp
      usage: "发布 v0.6.0 Release 和更新 README"
      trigger: "on-release"
  duration: "2025-11-15 to 2025-12-15"
```

### 功能 2: 规范验证（Speckit 核心）

**目的**：确保营销规范完整、一致

**CLI 命令**：
```bash
marketing-spec-kit validate specs/metaspec-marketing.yaml

# 输出：
✅ Project definition complete
✅ Campaign goals clearly defined
⚠️  Warning: No content templates specified
❌ Error: Missing target audience for campaign 'v0.6.0-launch'
```

**验证规则**：
- 必填字段检查
- 数据类型验证
- 逻辑一致性（如：渠道与内容类型匹配）
- 最佳实践建议

### 功能 3: Slash Commands（AI Agent 接口）

**目的**：让 AI Agent 能够读取和理解规范

**命令列表**：
- `/marketing.show-spec` - 显示完整的营销规范
- `/marketing.show-project` - 显示项目信息和品牌定位
- `/marketing.show-products` - 显示所有产品/功能列表
- `/marketing.show-product <id>` - 显示特定产品详情
- `/marketing.show-campaign <id>` - 显示特定营销活动
- `/marketing.show-channels` - 显示可用推广渠道
- `/marketing.show-tools` - 显示所有可用工具（MCP 和 API）
- `/marketing.show-tools-for-channel <channel>` - 显示特定渠道的工具
- `/marketing.show-tool <id>` - 显示工具详情（MCP 名称、capabilities）
- `/marketing.check-mcp-available <mcp-name>` - 检查 MCP 是否在环境中可用
- `/marketing.validate-content <file>` - 验证内容是否符合品牌规范
- `/marketing.get-template <type>` - 获取内容模板（tweet, blog, email）

**AI Agent 工作流示例 1：生成并发布推文（MCP 可用）**
```
用户: "为 MetaSpec v0.6.0 发布生成一条推文，重点推广 Speckit Generator，并发布"
  ↓
AI 调用: /marketing.show-campaign v0.6.0-launch
AI 读取: 目标、受众、关联产品、工具 [twitter-mcp]
  ↓
AI 调用: /marketing.show-product speckit-generator
AI 读取: 产品描述、核心特性、目标用户
  ↓
AI 调用: /marketing.show-project
AI 读取: 品牌声音 "Technical, Approachable, Community-driven"
  ↓
AI 生成: 符合规范的推文内容
  ↓
AI 调用: /marketing.show-tools-for-channel twitter
AI 读取: preferred tool = twitter-mcp (@twitter-mcp)
  ↓
AI 调用: /marketing.check-mcp-available @twitter-mcp
AI 确认: ✅ MCP 可用
  ↓
AI 调用: @twitter-mcp post-tweet "🚀 MetaSpec v0.6.0 is here!..."
AI 执行: ✅ 推文已发布
  ↓
AI 输出: "推文已成功发布到 Twitter：[link]"
```

**AI Agent 工作流示例 2：生成内容（MCP 不可用）**
```
用户: "为 MetaSpec v0.6.0 生成一条推文"
  ↓
AI 调用: /marketing.show-campaign v0.6.0-launch
  ... (同上)
  ↓
AI 生成: 符合规范的推文内容
  ↓
AI 调用: /marketing.check-mcp-available @twitter-mcp
AI 确认: ❌ MCP 不可用
  ↓
AI 调用: /marketing.show-tool twitter-mcp
AI 读取: fallback_for = twitter-api
  ↓
AI 输出: 
  "✅ 推文内容已生成：
   
   [推文内容]
   
   ⚠️ 无法自动发布，因为 @twitter-mcp 未安装。
   
   你可以：
   1. 手动复制内容发布到 Twitter
   2. 安装 twitter-mcp: npm install -g @modelcontextprotocol/twitter
   3. 使用 Twitter API (需要配置 API keys)"
```

### 功能 4: 模板和示例（Speckit 辅助）

**目的**：帮助用户快速创建规范

**CLI 命令**：
```bash
marketing-spec-kit init project
marketing-spec-kit init campaign --template product-launch
```

**模板库**：
- `project-template.yaml` - 项目基本信息模板
- `campaign-templates/` - 各类营销活动模板
  - `product-launch.yaml` - 产品发布
  - `community-growth.yaml` - 社区增长
  - `feature-announcement.yaml` - 功能发布

---

## 🚫 非功能需求（明确不做什么）

- ❌ **不是 CRM 系统**：不管理客户关系和销售漏斗
- ❌ **不是数据分析平台**：不提供复杂的数据分析和 BI
- ❌ **不是社交媒体管理工具**：不替代 Buffer/Hootsuite
- ❌ **不是广告投放平台**：不管理付费广告

**核心聚焦**：
- ✅ 规范定义：WHAT（运营做什么）
- ✅ 内容生成：HOW（AI 如何帮助）
- ✅ 任务执行：DO（AI 执行运营任务）

---

## 🏗️ 工作流程

### 完整流程：从规范到执行

```
1️⃣ 用户定义规范
   ↓
   创建 specs/metaspec-marketing.yaml
   定义项目、活动、渠道、品牌

2️⃣ Speckit 验证规范
   ↓
   marketing-spec-kit validate specs/metaspec-marketing.yaml
   确保规范完整、一致

3️⃣ AI Agent 读取规范
   ↓
   用户: "为 v0.6.0 生成推文"
   AI 调用: /marketing.show-campaign v0.6.0-launch
   AI 理解: 目标、受众、品牌声音

4️⃣ AI Agent 生成内容
   ↓
   AI 基于规范约束生成内容
   AI 调用: /marketing.validate-content tweet.md
   AI 确认内容符合规范

5️⃣ 用户审核和发布
   ↓
   用户审核 AI 生成的内容
   用户决定是否发布（手动或通过工具）
```

### 技术组件

**Speckit 提供的组件**：
- `models.py` - 规范实体定义（Project, Product, Campaign, Channel, Tool, ContentTemplate）
- `validator.py` - 规范验证逻辑（包括实体关联验证、工具可用性检查）
- `cli.py` - CLI 命令（init, validate）
- `.metaspec/commands/` - Slash Commands for AI
  - 规范读取命令（show-spec, show-campaign, show-product, show-tool）
  - 工具检查命令（show-tools, check-mcp-available）
  - 内容验证命令（validate-content）
- `templates/` - 规范模板库

**AI Agent 使用的接口**：
- Slash Commands - 读取规范和工具信息
- MCP Tools - 直接调用执行营销任务（优先）
- Validation API - 验证内容符合品牌规范
- Template API - 获取内容模板

**MCP 集成策略**：
- ✅ 优先使用 MCP 工具（如 @twitter-mcp, @github-mcp）
- ✅ AI 可检查 MCP 是否可用
- ✅ 提供 REST API 作为 fallback
- ✅ 规范中明确定义工具偏好

**不在 Speckit 范围内**：
- ❌ 内容生成引擎（AI Agent 自己决定如何生成）
- ❌ MCP 工具实现（使用社区已有的 MCP 工具）
- ❌ 数据分析平台（用户使用 Google Analytics 等）
- ❌ A/B 测试和优化（用户使用专业工具）

**注意**：
- ✅ Speckit **定义**使用哪些工具
- ✅ AI Agent **调用** MCP 工具执行任务
- ❌ Speckit **不实现**工具本身

---

## 📅 实施路径

### Phase 1: 规范定义（SDS）
使用 MetaSpec SDS 命令定义市场运营规范：

```bash
# Step 1: 定义规范设计原则
/metaspec.sds.constitution

# Step 2: 定义运营规范实体（Project, Product, Campaign, Channel, Tool, ContentTemplate）
/metaspec.sds.specify

# Step 3: 澄清和完善规范
/metaspec.sds.clarify
/metaspec.sds.checklist
/metaspec.sds.analyze
```

**产出**：`specs/domain/001-marketing-specification/spec.md`

### Phase 2: 工具包开发（SDD）
使用 MetaSpec SDD 命令开发工具包：

```bash
# Step 1: 定义工具包规范
/metaspec.sdd.specify

# Step 2: 规划实现架构
/metaspec.sdd.plan

# Step 3: 实现功能
/metaspec.sdd.tasks
/metaspec.sdd.implement
```

**产出**：
- CLI 命令（init, validate）
- 规范验证器（validator.py）
- Slash Commands（.metaspec/commands/）
- 模板库（templates/）

**不包含**：
- ❌ 内容生成逻辑（由 AI Agent 负责）
- ❌ 发布执行逻辑（用户手动或使用其他工具）

### Phase 3: 实战验证（MetaSpec 运营）
使用 marketing-spec-kit 和 AI Agent 为 MetaSpec 做市场运营：

**用户操作**：
1. 创建 `specs/metaspec-marketing.yaml` 定义运营规范
2. 运行 `marketing-spec-kit validate specs/metaspec-marketing.yaml` 验证

**AI Agent 工作**：
1. 通过 `/marketing.show-campaign v0.6.0-launch` 读取规范
2. 基于规范生成内容（推文、博客、公告）
3. 通过 `/marketing.validate-content` 验证生成的内容

**用户审核和发布**：
1. 审核 AI 生成的内容
2. 手动或使用工具发布到各渠道
3. 收集反馈并迭代规范

---

## 🎯 成功指标

### 短期目标（1 个月）
- ✅ 完成规范定义（SDS）
- ✅ 实现核心 CLI 命令（init, validate）
- ✅ 实现 Slash Commands 供 AI 使用
- ✅ 通过 AI Agent 为 MetaSpec 生成 1 篇博客、5 条推文

### 中期目标（3 个月）
- ✅ 完善规范验证规则
- ✅ MetaSpec GitHub stars 达到 100+（通过规范驱动的营销）
- ✅ 至少 2 个其他项目使用 marketing-spec-kit 定义运营规范

### 长期目标（6 个月）
- ✅ 社区贡献功能（共享营销规范模板）
- ✅ 支持多语言营销规范定义
- ✅ 建立 marketing-spec-kit 用户社区
- ✅ 集成到 awesome-spec-kits 社区

---

## 📚 附录

### 相关资源
- MetaSpec 框架：https://github.com/ACNet-AI/MetaSpec
- 市场运营最佳实践：待研究
- AI Agent 集成方案：待设计

### 下一步行动
1. **立即开始**：运行 `/metaspec.sds.constitution` 定义市场运营规范的设计原则
2. **关键问题**：确定运营规范的核心实体（Project, Product, Campaign, Channel, Tool, ContentTemplate）
3. **实体关系**：
   - Project → Products → Campaign
   - Campaign → Channels → Tools (MCP 优先)
4. **MCP 集成**：
   - 定义 Tool 实体支持 MCP 和 REST API
   - 提供 MCP 可用性检查
   - 优雅降级到备选方案
5. **明确边界**：
   - Speckit 负责规范定义和验证
   - AI Agent 负责内容生成
   - MCP 工具负责执行（发布、更新等）
6. **技术聚焦**：不需要实现生成逻辑和工具逻辑，专注于规范结构和验证规则

---

*此 PRD 将随着项目推进持续更新*

