---
name: marketspec.discover
description: Discover and document marketing needs
layer: sdm
status: implemented
type: core
category: Core Flow
source: Adapted from metaspec.sdd.specify
version: 0.3.0
---

# /marketspec.discover 🔴 Core

**Purpose**: Discover and document marketing needs, objectives, and initial requirements.

**Category**: Core Flow (Essential Workflow)  
**Adapted from**: `metaspec.sdd.specify`

---

## Purpose

Guide users through systematically discovering and defining their marketing needs:
- Project/product overview
- Marketing objectives
- Target audiences
- Budget and timeline constraints
- Success metrics (preliminary)
- Key challenges and opportunities

This creates the foundation for all subsequent marketing planning and execution.

---

## Command Usage

```
/marketspec.discover [optional: brief description]
```

**Examples**:
```
/marketspec.discover
/marketspec.discover "Launch MetaSpec to developer community"
/marketspec.discover "Q1 2025 growth campaign"
```

---

## Prerequisites

- **Recommended**: Run `/marketspec.constitution` first to establish principles
- **Optional**: Have existing project/product documentation ready

---

## Execution Steps

### Step 1: Read Constitution (if exists)

Check if `memory/marketing-constitution.md` exists:
- If YES: Reference principles and guidelines during discovery
- If NO: Suggest running `/marketspec.constitution` first (but continue if user prefers)

### Step 2: Discover Project Context

Ask about the project/product being marketed:

```yaml
project_context:
  name: "What is the project/product name?"
  tagline: "What's a short tagline? (≤100 chars)"
  description: "Describe the project in 2-3 sentences"
  website: "Website URL (if exists)"
  current_stage: "Stage?" 
    # Options: idea, development, alpha, beta, launched, mature
  
  # Optional but helpful
  unique_value: "What makes this unique/different?"
  problem_solved: "What problem does it solve?"
```

**Example Questions**:
- "What are you marketing?"
- "Is this a new product launch or existing product growth?"
- "What stage is the product at?"

### Step 3: Identify Marketing Objectives

Guide user to define 3-5 clear marketing objectives:

```yaml
marketing_objectives:
  - type: "awareness | consideration | conversion | retention"
    description: "Specific objective description"
    rationale: "Why this objective matters"
    priority: "high | medium | low"
    timeframe: "When should this be achieved?"
```

**Example Questions**:
- "What are your top 3-5 marketing goals?"
- "Are you focused on awareness, driving conversions, or both?"
- "What does success look like in 3 months? 6 months?"

**Common Objectives**:
- Increase brand awareness
- Drive product signups/downloads
- Generate qualified leads
- Build community engagement
- Establish thought leadership
- Drive revenue/sales

### Step 4: Define Target Audiences

Identify 1-3 primary audience segments:

```yaml
target_audiences:
  - segment_name: "Name the segment"
    description: "Who are they? What do they care about?"
    size_estimate: "Rough size (if known)"
    characteristics:
      - "Key characteristic 1"
      - "Key characteristic 2"
    pain_points:
      - "Pain point 1"
      - "Pain point 2"
    where_they_are: "Where can you reach them?"
      # Examples: Twitter, Reddit, LinkedIn, conferences, blogs
    priority: "high | medium | low"
```

**Example Questions**:
- "Who is your primary audience?"
- "What are their key characteristics?"
- "What problems are they trying to solve?"
- "Where do they spend time online?"

### Step 5: Understand Constraints

Document constraints and boundaries:

```yaml
constraints:
  budget:
    total: "Approximate total budget (if known)"
    currency: "USD | EUR | etc."
    flexibility: "fixed | flexible | unknown"
  
  timeline:
    start_date: "When do you want to start?"
    key_dates: 
      - "Important deadlines or milestones"
    urgency: "urgent | moderate | flexible"
  
  resources:
    team_size: "How many people working on marketing?"
    skills_available: ["Content writing", "Design", "etc."]
    skills_needed: ["What skills are missing?"]
  
  limitations:
    - "Any constraints? (e.g., legal, brand, regional)"
```

**Example Questions**:
- "What's your approximate marketing budget?"
- "When do you need to launch/achieve results?"
- "Who's on your marketing team?"
- "Are there any legal or brand constraints?"

### Step 6: Identify Current State

Understand the starting point:

```yaml
current_state:
  existing_channels:
    - channel: "Channel name"
      status: "active | inactive"
      performance: "How's it performing?"
  
  existing_content:
    - "What content do you already have?"
  
  past_efforts:
    - effort: "What have you tried before?"
      result: "What happened?"
      learnings: "What did you learn?"
  
  assets_available:
    - "Logo, brand guidelines, etc."
```

**Example Questions**:
- "What marketing channels are you currently using?"
- "What's worked well in the past?"
- "What hasn't worked?"
- "What marketing assets do you have ready?"

### Step 7: Clarify Success Metrics (Preliminary)

Define high-level success indicators:

```yaml
success_indicators:
  primary_metric: "What's the #1 metric that matters?"
  
  preliminary_targets:
    - metric: "Metric name"
      current_value: "Where are you now?"
      target_value: "Where do you want to be?"
      timeframe: "By when?"
      measurement_method: "How will you track this?"
```

**Example Questions**:
- "How will you measure success?"
- "What's the most important metric?"
- "What's your target for the primary metric?"
- "Do you have baseline/current numbers?"

### Step 8: Identify Challenges & Opportunities

Discuss obstacles and advantages:

```yaml
challenges:
  - challenge: "What might make this difficult?"
    impact: "high | medium | low"
    mitigation_ideas: "Any ideas to address this?"

opportunities:
  - opportunity: "What advantages do you have?"
    potential: "high | medium | low"
    how_to_leverage: "How can you capitalize on this?"
```

**Example Questions**:
- "What are your biggest marketing challenges?"
- "What advantages or opportunities do you have?"
- "Are there competitors doing this well?"

### Step 9: Generate Discovery Document

Create `specs/discovery/[project-name]-discovery.md`:

```markdown
# Marketing Discovery: [Project Name]

**Date**: 2025-11-16  
**Status**: Initial Discovery  
**Next Step**: Clarify (use /marketspec.clarify)

---

## Project Context

[Content from Step 2]

---

## Marketing Objectives

[Content from Step 3]

---

## Target Audiences

[Content from Step 4]

---

## Constraints

[Content from Step 5]

---

## Current State

[Content from Step 6]

---

## Success Metrics (Preliminary)

[Content from Step 7]

---

## Challenges & Opportunities

[Content from Step 8]

---

## Next Steps

1. **Clarify** ambiguities and assumptions → `/marketspec.clarify`
2. **Plan** marketing strategy → `/marketspec.strategy`
3. **Create** detailed specification → `/marketspec.create`

---

## Questions for Clarification

[Auto-generated list of things that need clarification]
- [ ] Question 1
- [ ] Question 2
```

### Step 10: Validate Completeness

Check discovery document has:
- ✅ Clear project context
- ✅ At least 3 marketing objectives
- ✅ At least 1 target audience defined
- ✅ Preliminary success metrics identified
- ⚠️ Highlight any missing critical information

---

## Success Criteria

- Discovery document created at `specs/discovery/[project-name]-discovery.md`
- All 8 discovery areas have meaningful content
- Clear next steps identified
- User feels confident about what they're trying to achieve

---

## Output

**Primary Output**: `specs/discovery/[project-name]-discovery.md`

**Structure**:
```
specs/
└── discovery/
    └── [project-name]-discovery.md  # Discovery document
```

**Optional**: Generate preliminary YAML snippet for reference:

```yaml
# preliminary-requirements.yaml
project:
  name: "..."
  tagline: "..."
  
objectives_summary:
  - "..."
  
target_audiences:
  - "..."
```

---

## Error Handling

- If user can't answer a question, mark it for clarification in Step 9
- If budget/timeline unknown, note as "TBD" and flag for later
- If objectives are too vague, provide examples and ask for specificity
- Suggest industry benchmarks if user has no baseline metrics

---

## Example Interaction

```
User: /marketspec.discover "Launch MetaSpec to developers"

AI: Great! I'll help you discover and document your marketing needs for MetaSpec.

First, let me understand the project context:

**Project Context**
1. Project name: MetaSpec ✅
2. What's a short tagline for MetaSpec? (≤100 chars)

---

User: "Spec-Driven Development Framework"

AI: Perfect! Now tell me about the product:

3. Can you describe MetaSpec in 2-3 sentences?
4. What's the website URL?
5. What stage is MetaSpec at? (idea/development/alpha/beta/launched/mature)

---

User: 
- It's a framework for specification-driven development
- metaspec.dev
- Beta stage

AI: Excellent. Now let's define your marketing objectives:

**Marketing Objectives**

What are your top 3-5 marketing goals for MetaSpec? For example:
- Increase GitHub stars to 1000
- Get 500 beta users
- Establish presence in developer community

What are your main objectives?

---

[Continues through all 8 steps]

---

[After completing discovery]

AI: Perfect! I've documented all your marketing needs.

📄 **Discovery Document**: specs/discovery/metaspec-discovery.md

**Summary**:
✅ Project: MetaSpec (Beta stage)
✅ 4 Marketing Objectives defined
✅ 2 Target Audiences identified (CTOs, Developers)
✅ Budget: $5,000 (flexible)
✅ Timeline: Launch in Q1 2025
✅ Primary Metric: GitHub stars (target: 1000)

**Next Steps**:
1. 🔍 Clarify 3 ambiguous items → `/marketspec.clarify`
2. 📋 Plan marketing strategy → `/marketspec.strategy`

Would you like to proceed with clarification?
```

---

## Notes

- Keep the conversation natural - don't interrogate, have a dialogue
- Use examples liberally to help users articulate their needs
- It's okay to have unknowns - mark them for clarification
- Discovery is iterative - users can refine later with `/marketspec.clarify`
- Focus on "what" and "why", not "how" (that comes in strategy phase)

---

## Integration with Other Commands

This discovery document feeds into:
- `/marketspec.clarify` - Resolves ambiguities and unanswered questions
- `/marketspec.strategy` - Uses objectives and audiences for planning
- `/marketspec.tasks` - Task breakdown references objectives
- `/marketspec.create` - Generates final YAML from discovered requirements

---

## See Also

- `/marketspec.constitution` - Should run before discovery
- `/marketspec.clarify` - Next step after discovery
- Domain Specification: `specs/domain/001-marketing-operations-spec/spec.md`
- Discovery examples in `examples/` directory
