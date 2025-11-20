---
name: marketspec.tasks
description: Break down plan into actionable implementation tasks
layer: sdm
status: implemented
type: core
category: Core Flow
source: Adapted from metaspec.sds.tasks
version: 0.3.0
---

# /marketspec.tasks 🔴 Core

**Purpose**: Break down the marketing strategy into concrete, actionable tasks with priorities, dependencies, and assignments.

**Category**: Core Flow (Essential Workflow)  
**Adapted from**: `metaspec.sdd.tasks`

---

## Purpose

Transform the high-level marketing strategy into a detailed task breakdown:
- Decompose campaigns into executable tasks
- Define task dependencies and sequencing
- Assign priorities and effort estimates
- Identify required resources and owners
- Create clear acceptance criteria
- Establish timeline and milestones

This task breakdown serves as the execution roadmap for the marketing team.

---

## Command Usage

```
/marketspec.tasks
/marketspec.tasks --campaign [campaign_id]
```

**Examples**:
```
/marketspec.tasks
/marketspec.tasks --campaign "launch-campaign"
```

---

## Prerequisites

- **Required**: Marketing plan from `/marketspec.plan`
- **Recommended**: Clarification document from `/marketspec.clarify`
- **Optional**: Constitution for alignment check

---

## Execution Steps

### Step 1: Load Strategy Document

Read the plan document from `specs/{sequence}-{name}/plan.md`:

**Extract key information**:
- Campaign structure and timelines
- Channel strategies and content plans
- Budget allocation
- Milestones and deadlines
- Team resources

### Step 2: Identify Task Categories

Group tasks into logical categories:

```yaml
task_categories:
  setup:
    description: "Initial setup and preparation"
    examples:
      - "Create social media accounts"
      - "Set up analytics tracking"
      - "Configure email platform"
  
  content_creation:
    description: "Content development and production"
    examples:
      - "Write blog posts"
      - "Design graphics"
      - "Produce videos"
  
  content_distribution:
    description: "Publishing and promotion"
    examples:
      - "Schedule social posts"
      - "Send email campaigns"
      - "Submit to aggregators"
  
  engagement:
    description: "Community interaction"
    examples:
      - "Respond to comments"
      - "Moderate discussions"
      - "Answer questions"
  
  optimization:
    description: "Analysis and improvement"
    examples:
      - "Review analytics"
      - "A/B test variations"
      - "Optimize based on data"
  
  reporting:
    description: "Measurement and reporting"
    examples:
      - "Generate weekly reports"
      - "Track KPIs"
      - "Present to stakeholders"
```

### Step 3: Break Down Campaigns into Tasks

For each campaign in the strategy, decompose into specific tasks:

**Example Campaign**: "Developer Onboarding Campaign"

```yaml
campaign: "developer-onboarding"
duration: "6 weeks"

tasks:
  # Setup Phase (Week 1)
  - id: "setup-001"
    name: "Set up Twitter developer account"
    category: "setup"
    priority: "P0"
    estimated_hours: 2
    deadline: "Week 1, Day 1"
    dependencies: []
    owner: "Social Media Manager"
    acceptance_criteria:
      - "Account created and verified"
      - "Profile complete with bio and logo"
      - "Initial followers from team members"
  
  - id: "setup-002"
    name: "Configure Google Analytics tracking"
    category: "setup"
    priority: "P0"
    estimated_hours: 4
    deadline: "Week 1, Day 2"
    dependencies: []
    owner: "Marketing Lead"
    acceptance_criteria:
      - "GA4 property created"
      - "Tracking code installed"
      - "Goals configured"
      - "Test tracking verified"
  
  # Content Creation (Weeks 1-2)
  - id: "content-001"
    name: "Write 'Getting Started' blog post"
    category: "content_creation"
    priority: "P0"
    estimated_hours: 8
    deadline: "Week 1, Day 5"
    dependencies: []
    owner: "Content Writer"
    acceptance_criteria:
      - "1500-2000 words"
      - "Includes code examples"
      - "SEO optimized"
      - "Reviewed by tech lead"
      - "Images and diagrams included"
  
  - id: "content-002"
    name: "Design social media graphics (batch 1)"
    category: "content_creation"
    priority: "P1"
    estimated_hours: 6
    deadline: "Week 1, Day 5"
    dependencies: []
    owner: "Designer"
    acceptance_criteria:
      - "10 graphics in brand style"
      - "Multiple sizes (Twitter, LinkedIn)"
      - "Accessible (alt text ready)"
  
  # Distribution (Weeks 2-6)
  - id: "dist-001"
    name: "Publish 'Getting Started' post"
    category: "content_distribution"
    priority: "P0"
    estimated_hours: 2
    deadline: "Week 2, Day 1"
    dependencies: ["content-001"]
    owner: "Content Manager"
    acceptance_criteria:
      - "Post published on blog"
      - "Cross-posted to Dev.to"
      - "Submitted to Hacker News"
      - "Announced on Twitter"
  
  - id: "dist-002"
    name: "Schedule week 2 social posts"
    category: "content_distribution"
    priority: "P0"
    estimated_hours: 3
    deadline: "Week 1, Day 5"
    dependencies: ["content-002"]
    owner: "Social Media Manager"
    acceptance_criteria:
      - "14 posts scheduled (2/day)"
      - "Mix of tips, updates, engagement"
      - "Optimal timing for audience"
  
  # Engagement (Ongoing)
  - id: "engage-001"
    name: "Daily social media engagement"
    category: "engagement"
    priority: "P1"
    estimated_hours: "1/day"
    deadline: "Daily, Weeks 1-6"
    dependencies: ["setup-001"]
    owner: "Community Manager"
    recurring: true
    acceptance_criteria:
      - "Respond to all mentions within 2 hours"
      - "Engage with 10 relevant posts daily"
      - "Answer questions in GitHub discussions"
  
  # Optimization (Weekly)
  - id: "opt-001"
    name: "Weekly performance review"
    category: "optimization"
    priority: "P1"
    estimated_hours: 4
    deadline: "Every Friday"
    dependencies: ["setup-002"]
    owner: "Marketing Lead"
    recurring: true
    acceptance_criteria:
      - "Review all KPIs"
      - "Identify top/bottom performers"
      - "Adjust content strategy if needed"
      - "Document learnings"
```

### Step 4: Define Task Properties

For each task, specify:

```yaml
task_properties:
  id:
    format: "[category]-[number]"
    example: "content-001"
    required: true
  
  name:
    description: "Clear, actionable task name"
    format: "Verb + Object"
    example: "Write blog post about X"
    required: true
  
  category:
    description: "Task category"
    options: ["setup", "content_creation", "content_distribution", "engagement", "optimization", "reporting"]
    required: true
  
  priority:
    description: "Task priority"
    options:
      P0: "Critical - blocks other work"
      P1: "High - important for success"
      P2: "Medium - should do"
      P3: "Low - nice to have"
    required: true
  
  estimated_hours:
    description: "Time estimate in hours"
    type: "number or 'X/day' for recurring"
    required: true
  
  deadline:
    description: "When task must be completed"
    format: "Week X, Day Y or specific date"
    required: true
  
  dependencies:
    description: "Task IDs that must complete first"
    type: "array of task IDs"
    required: true  # Can be empty array
  
  owner:
    description: "Person/role responsible"
    required: true
  
  acceptance_criteria:
    description: "How to know task is done"
    type: "array of criteria"
    min_items: 1
    required: true
  
  recurring:
    description: "Is this a recurring task?"
    type: "boolean"
    default: false
    required: false
  
  status:
    description: "Current status"
    options: ["not_started", "in_progress", "blocked", "completed"]
    default: "not_started"
    required: false
```

### Step 5: Map Dependencies

Create a dependency graph to ensure proper sequencing:

```yaml
dependency_chains:
  # Setup Chain
  - chain: "account_setup"
    tasks: ["setup-001", "setup-002"]
    blocks: ["dist-001", "engage-001", "opt-001"]
  
  # Content Creation → Distribution
  - chain: "content_flow"
    tasks: ["content-001", "dist-001"]
    description: "Content must be created before distribution"
  
  - chain: "graphics_flow"
    tasks: ["content-002", "dist-002"]
    description: "Graphics must be ready before scheduling"
  
  # Parallel Tracks (no dependencies)
  parallel_tracks:
    - ["content-001", "content-002", "setup-003"]
    - ["engage-001", "engage-002"]
```

**Validation**:
- ✅ No circular dependencies
- ✅ All dependencies reference valid task IDs
- ✅ Critical path identified
- ✅ No orphaned tasks

### Step 6: Estimate Total Effort

Calculate total effort by role:

```yaml
effort_by_role:
  content_writer:
    total_hours: 80
    tasks: 10
    weeks: 6
    hours_per_week: 13.3
    capacity_check: "OK (< 20 hours/week)"
  
  designer:
    total_hours: 48
    tasks: 8
    weeks: 6
    hours_per_week: 8
    capacity_check: "OK"
  
  social_media_manager:
    total_hours: 120
    tasks: 20
    weeks: 6
    hours_per_week: 20
    capacity_check: "At capacity"
  
  marketing_lead:
    total_hours: 60
    tasks: 15
    weeks: 6
    hours_per_week: 10
    capacity_check: "OK"

total_effort_hours: 308
average_hours_per_week: 51.3
team_size: 4
realistic: true
```

**Capacity Analysis**:
- 🟢 Green: < 80% capacity
- 🟡 Yellow: 80-100% capacity
- 🔴 Red: > 100% capacity (need to adjust)

### Step 7: Create Timeline Visualization

Map tasks to timeline:

```yaml
timeline:
  week_1:
    focus: "Setup & Initial Content"
    tasks:
      monday: ["setup-001", "setup-002"]
      tuesday: ["content-001", "content-002"]
      wednesday: ["content-001", "content-003"]
      thursday: ["content-002", "setup-003"]
      friday: ["dist-002", "opt-001"]
    deliverables:
      - "All accounts created"
      - "First blog post drafted"
      - "Week 2 content scheduled"
  
  week_2:
    focus: "Launch & Engagement"
    tasks:
      monday: ["dist-001", "engage-001-start"]
      tuesday-friday: ["engage-001", "content-004"]
    deliverables:
      - "First post published"
      - "Engagement rhythm established"
      - "First metrics collected"
  
  week_3-6:
    focus: "Sustained Execution & Optimization"
    recurring_tasks:
      - "Daily engagement"
      - "Weekly content"
      - "Weekly optimization"
    deliverables:
      - "2 posts/week published"
      - "Steady social presence"
      - "KPI tracking active"
```

### Step 8: Define Task Templates

Create reusable templates for common tasks:

**Template: Blog Post Publication**
```yaml
template: "blog_post_publication"
tasks:
  - id: "[post-id]-write"
    name: "Write blog post: [topic]"
    category: "content_creation"
    priority: "P0"
    estimated_hours: 8
    owner: "Content Writer"
    acceptance_criteria:
      - "[target] words written"
      - "SEO optimized"
      - "Code examples included"
      - "Technical review passed"
  
  - id: "[post-id]-design"
    name: "Design graphics for: [topic]"
    category: "content_creation"
    priority: "P1"
    estimated_hours: 3
    owner: "Designer"
    dependencies: ["[post-id]-write"]
    acceptance_criteria:
      - "Header image created"
      - "In-post diagrams completed"
      - "Social share images ready"
  
  - id: "[post-id]-publish"
    name: "Publish blog post: [topic]"
    category: "content_distribution"
    priority: "P0"
    estimated_hours: 2
    owner: "Content Manager"
    dependencies: ["[post-id]-write", "[post-id]-design"]
    acceptance_criteria:
      - "Published on blog"
      - "Cross-posted to Dev.to"
      - "Shared on social media"
      - "Submitted to aggregators"
```

### Step 9: Risk Identification

Identify task-related risks:

```yaml
task_risks:
  - risk: "Content bottleneck - writer overwhelmed"
    affected_tasks: ["content-001", "content-003", "content-005"]
    probability: "medium"
    impact: "high"
    mitigation:
      - "Start content creation 1 week early"
      - "Hire freelance writer for backup"
      - "Reduce content frequency if needed"
  
  - risk: "Designer unavailable Week 3"
    affected_tasks: ["content-002", "content-006"]
    probability: "high"
    impact: "medium"
    mitigation:
      - "Batch design work in Weeks 1-2"
      - "Use templates for Week 3"
      - "Have contingency designer on call"
  
  - risk: "Hacker News submission fails (shadowbanned)"
    affected_tasks: ["dist-001", "dist-004"]
    probability: "low"
    impact: "low"
    mitigation:
      - "Have team members upvote"
      - "Use Reddit as backup"
      - "Don't rely solely on HN traffic"
```

### Step 10: Generate Task Document

Create comprehensive task breakdown document:

```markdown
# Marketing Tasks: [Project Name]

**Campaign**: [Campaign Name]  
**Duration**: [Start Date] - [End Date]  
**Team**: [Team Members]  
**Status**: Ready for execution

---

## Executive Summary

- **Total Tasks**: 45
- **Total Effort**: 308 hours
- **Duration**: 6 weeks
- **Team Size**: 4 people
- **Critical Path**: 12 tasks

---

## Task Categories

### Setup (5 tasks, 15 hours)
[List setup tasks]

### Content Creation (15 tasks, 120 hours)
[List content tasks]

### Content Distribution (10 tasks, 40 hours)
[List distribution tasks]

### Engagement (8 tasks, 96 hours)
[List engagement tasks]

### Optimization (5 tasks, 27 hours)
[List optimization tasks]

### Reporting (2 tasks, 10 hours)
[List reporting tasks]

---

## Weekly Breakdown

### Week 1: Setup & Foundation
[Detailed task list]

### Week 2: Launch
[Detailed task list]

### Weeks 3-6: Execution
[Detailed task list]

---

## Task Dependencies

[Dependency graph or list]

---

## Resource Allocation

[Effort by role, capacity analysis]

---

## Risk Assessment

[Task-related risks and mitigation]

---

## Task Templates

[Reusable task templates]

---

## Next Steps

1. **Assign tasks** → Distribute to team members
2. **Set up tracking** → Add to project management tool
3. **Begin execution** → Start with P0 tasks
4. **Create specification** → `/marketspec.create`
```

**Export Options**:
- Markdown: `specs/tasks/[project-name]-tasks.md`
- YAML: `specs/tasks/[project-name]-tasks.yaml`
- CSV: For import into project tools
- JSON: For programmatic access

---

## Success Criteria

- ✅ All strategy elements broken down into tasks
- ✅ Each task has clear acceptance criteria
- ✅ Dependencies mapped with no circular references
- ✅ Effort estimates realistic and balanced across team
- ✅ Timeline aligned with strategy milestones
- ✅ Resource capacity validated
- ✅ Risks identified with mitigation plans

---

## Output

**Primary Output**: `specs/{sequence}-{name}/tasks.md`

**Example Structure**:
```
specs/
└── 001-q1-campaign-strategy/
    ├── spec.md                 ← Draft specification
    ├── plan.md                 ← Marketing plan
    └── tasks.md                ← Task breakdown (from this command) ⭐
```

---

## Error Handling

- If plan incomplete, prompt to complete `/marketspec.plan` first
- If effort estimates exceed team capacity, suggest reducing scope or extending timeline
- If circular dependencies detected, help resolve conflicts
- If critical path too long, suggest parallelization
- If tasks lack acceptance criteria, prompt for specifics

---

## Example Interaction

```
User: /marketspec.tasks

AI: I'll help you break down the marketing plan into actionable tasks. Let me load your plan document...

📄 Loaded: specs/001-q1-campaign/plan.md

**Plan Summary**:
- 2 Campaigns: Developer Onboarding, Power User Stories
- 4 Channels: Blog, Twitter, Dev.to, GitHub
- 11 weeks duration
- $10K budget

I'll now decompose this into concrete tasks.

---

**Campaign 1: Developer Onboarding (6 weeks)**

I've identified 6 task categories:
1. Setup (5 tasks, ~15 hours)
2. Content Creation (15 tasks, ~120 hours)
3. Content Distribution (10 tasks, ~40 hours)
4. Engagement (8 tasks, ~96 hours)
5. Optimization (5 tasks, ~27 hours)
6. Reporting (2 tasks, ~10 hours)

Let me break down the first category - Setup tasks:

**Setup Tasks**:

1. **setup-001**: Set up Twitter developer account
   - Priority: P0 (critical)
   - Owner: Social Media Manager
   - Estimated: 2 hours
   - Deadline: Week 1, Day 1
   - Acceptance criteria:
     ✓ Account created and verified
     ✓ Profile complete
     ✓ Initial followers from team

Does this level of detail work for you, or would you like more/less detail?

---

User: This looks good. Continue.

AI: Great! Continuing with all tasks...

[Processes all campaigns and tasks]

---

[After completing task breakdown]

AI: Perfect! I've created a comprehensive task breakdown:

📄 **Task Document**: specs/001-q1-campaign/tasks.md

**Summary**:
✅ **45 total tasks** across 6 categories
✅ **308 hours** total effort
✅ **4 team members** assigned
✅ **6 weeks** timeline
✅ **Dependencies mapped** - no conflicts
✅ **Resource capacity** - all roles under 100%

**Task Distribution**:
- Setup: 5 tasks (Week 1)
- Content Creation: 15 tasks (ongoing)
- Distribution: 10 tasks (ongoing)
- Engagement: 8 tasks (daily)
- Optimization: 5 tasks (weekly)
- Reporting: 2 tasks (weekly)

**Critical Path** (longest dependency chain):
setup-001 → content-001 → dist-001 → engage-001 (4 days)

**Resource Analysis**:
🟢 Content Writer: 13.3 hrs/week (66% capacity)
🟢 Designer: 8 hrs/week (40% capacity)
🟡 Social Media Manager: 20 hrs/week (100% capacity)
🟢 Marketing Lead: 10 hrs/week (50% capacity)

⚠️ **Note**: Social Media Manager at full capacity. Consider reducing engagement frequency or adding support if issues arise.

**Next Steps**:
1. Review task breakdown
2. Run analysis → `/marketspec.analyze`
3. Generate final specification → `/marketspec.implement`

Ready to analyze consistency?
```

---

## Notes

- Break down to the right level - not too granular, not too high-level
- **Rule of thumb**: Tasks should be 2-8 hours each
- Recurring tasks (daily engagement) can be grouped
- Include buffer time in estimates (add 20%)
- Consider team capacity and availability
- Document assumptions in task descriptions
- Use task templates for consistency
- Link tasks to strategy objectives for traceability

---

## Integration with Other Commands

Feeds into:
- `/marketspec.analyze` - Consistency analysis
- `/marketspec.implement` - Final specification generation

References:
- `/marketspec.plan` - Source of campaigns and channels
- `/marketspec.specify` - Original objectives for validation
- `/marketspec.constitution` - Workflow constraints

---

## See Also

- `/marketspec.plan` - Previous step
- `/marketspec.analyze` - Next step (consistency analysis)
- `/marketspec.implement` - Final specification generation
- Task examples in `examples/` directory
- MetaSpec SDS Tasks: `.metaspec/commands/metaspec.sds.tasks.md`
