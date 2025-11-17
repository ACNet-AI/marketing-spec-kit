---
name: marketspec.constitution
description: Define marketing execution principles
layer: sdm
status: implemented
source: Adapted from metaspec.sds.constitution
version: 0.3.0
---

# /marketspec.constitution

**Purpose**: Define core principles and constraints for marketing execution and specification creation.

**Adapted from**: `metaspec.sds.constitution`

---

## Purpose

Establish a "constitution" document that defines:
- Marketing execution principles
- Brand guidelines and constraints
- Quality standards for marketing specifications
- Workflow best practices
- Required vs. optional specification sections

This document acts as a **north star** for all marketing activities and ensures consistency across campaigns and content.

---

## Command Usage

```
/marketspec.constitution
```

---

## Prerequisites

- None (can be run at any time)
- Recommended: Run before creating any marketing specifications

---

## Execution Steps

### Step 1: Determine Constitution Scope

Ask the user what aspects they want to define:

**Core Sections** (recommended to include):
1. **Marketing Principles** - Core values and approaches
2. **Brand Guidelines** - Voice, tone, visual identity
3. **Target Audience** - Primary and secondary audiences
4. **Content Standards** - Quality requirements and prohibited patterns
5. **Workflow Constraints** - Process requirements and approval flows
6. **Measurement Philosophy** - How to define and track success

### Step 2: Gather Constitution Content

For each selected section, guide the user through defining:

#### 2.1 Marketing Principles
```yaml
marketing_principles:
  - principle: "Customer-First Approach"
    description: "Always prioritize customer value over promotional messaging"
    rationale: "Builds trust and long-term relationships"
  
  - principle: "Data-Driven Decisions"
    description: "Base marketing decisions on analytics and user feedback"
    rationale: "Reduces guesswork and improves ROI"
```

#### 2.2 Brand Guidelines
```yaml
brand_guidelines:
  voice: "Professional yet approachable"
  tone: "Educational and empowering"
  
  visual_identity:
    primary_colors: ["#0066CC", "#00CC66"]
    typography: "Inter for headings, Source Sans for body"
    
  prohibited_patterns:
    - "Excessive exclamation marks (!!!!!)"
    - "All-caps headlines"
    - "Clickbait language"
    - "Overpromising without evidence"
```

#### 2.3 Target Audience
```yaml
target_audience:
  primary:
    name: "Technical Decision Makers"
    description: "CTOs, Engineering Leads, Senior Developers"
    characteristics:
      - "5+ years experience"
      - "Values efficiency and quality"
      - "Prefers technical depth over marketing fluff"
    
  secondary:
    name: "Individual Contributors"
    description: "Developers and engineers"
    characteristics:
      - "Looking for tools to improve workflow"
      - "Active in developer communities"
```

#### 2.4 Content Standards
```yaml
content_standards:
  required:
    - "All claims must be backed by evidence or user testimonials"
    - "Technical content must be reviewed by engineering team"
    - "Include clear CTAs (Call-to-Actions)"
    
  quality_thresholds:
    - "Blog posts: minimum 800 words, maximum 3000 words"
    - "Social posts: minimum 50 characters, maximum 280 characters"
    - "Readability: Flesch Reading Ease score ≥ 60"
    
  prohibited:
    - "False or misleading claims"
    - "Competitor bashing"
    - "Unsubstantiated superlatives (best, fastest, etc.)"
```

#### 2.5 Workflow Constraints
```yaml
workflow_constraints:
  approval_required_for:
    - "Public-facing campaigns with budget > $5,000"
    - "Content mentioning partnerships or customers"
    - "Legal or compliance-sensitive topics"
    
  review_process:
    - step: "Draft Creation"
      owner: "Marketing Team"
    - step: "Technical Review"
      owner: "Engineering Lead"
      required_for: ["Technical content", "Product announcements"]
    - step: "Final Approval"
      owner: "Marketing Director"
```

#### 2.6 Measurement Philosophy
```yaml
measurement_philosophy:
  success_metrics_must:
    - "Be specific and measurable"
    - "Align with business objectives"
    - "Have baseline and target values"
    
  kpi_tiers:
    P0: "Critical metrics that directly impact revenue or growth"
    P1: "Important metrics for operational efficiency"
    P2: "Nice-to-have metrics for additional insights"
    
  reporting_frequency:
    campaigns: "Weekly during active period"
    overall_marketing: "Monthly dashboard"
```

### Step 3: Document Versioning

Add version control metadata:

```yaml
constitution_metadata:
  version: "1.0.0"
  created_at: "2025-11-16T10:00:00Z"
  last_updated: "2025-11-16T10:00:00Z"
  authors: ["Marketing Team", "Brand Team"]
  review_cycle: "Quarterly"
```

### Step 4: Generate Constitution Document

Create the constitution file at `memory/marketing-constitution.md`:

```markdown
# Marketing Execution Constitution

**Version**: 1.0.0  
**Last Updated**: 2025-11-16  
**Review Cycle**: Quarterly

---

## 1. Marketing Principles

[Generated content from Step 2.1]

---

## 2. Brand Guidelines

[Generated content from Step 2.2]

---

## 3. Target Audience

[Generated content from Step 2.3]

---

## 4. Content Standards

[Generated content from Step 2.4]

---

## 5. Workflow Constraints

[Generated content from Step 2.5]

---

## 6. Measurement Philosophy

[Generated content from Step 2.6]

---

## Change History

- **v1.0.0** (2025-11-16): Initial constitution
```

### Step 5: Validate Constitution

Check for completeness:
- ✅ At least 3 core sections defined
- ✅ Brand guidelines include voice and tone
- ✅ Content standards include both required and prohibited patterns
- ✅ Measurement philosophy defines success criteria

---

## Success Criteria

- Constitution document is created at `memory/marketing-constitution.md`
- All selected sections have meaningful content (not just placeholders)
- Document is version-controlled
- Easy to reference in future marketing activities

---

## Output

**Primary Output**: `memory/marketing-constitution.md`

**Structure**:
```
memory/
└── marketing-constitution.md  # Marketing execution principles
```

**Alternative**: If user prefers YAML format, can generate `memory/marketing-constitution.yaml`

---

## Error Handling

- If user is unsure about a section, provide examples and templates
- If sections are too generic, prompt for more specific details
- Suggest industry best practices when user needs guidance

---

## Example Interaction

```
User: /marketspec.constitution

AI: I'll help you create a marketing execution constitution. This will define the core principles and constraints for all your marketing activities.

Let's start with the essential sections. Which would you like to define?

1. ✅ Marketing Principles (recommended)
2. ✅ Brand Guidelines (recommended)
3. ✅ Target Audience (recommended)
4. ✅ Content Standards (recommended)
5. ⚪ Workflow Constraints (optional)
6. ⚪ Measurement Philosophy (optional)

Would you like to define all 6 sections, or start with the core 4?

---

User: Let's define all 6 sections.

AI: Great! Let's start with Marketing Principles.

**1. Marketing Principles**

What are your top 3-5 core marketing principles? For example:
- "Customer-first approach"
- "Data-driven decisions"
- "Transparency and authenticity"

What principles guide your marketing efforts?

[User provides principles]

AI: Excellent. Let me document those with descriptions and rationale...

[Continues through all sections]

---

[After completing all sections]

AI: Perfect! I've created your marketing constitution at:

📄 **memory/marketing-constitution.md**

This document includes:
✅ 5 Marketing Principles
✅ Brand Guidelines (voice, tone, visual identity)
✅ 2 Target Audience Segments
✅ Content Standards (required, quality thresholds, prohibited)
✅ Workflow Constraints (approval process)
✅ Measurement Philosophy (KPI tiers, reporting frequency)

You can now reference this constitution when creating marketing specifications with `/marketspec.discover`.

Would you like to proceed with discovering your marketing needs?
```

---

## Notes

- Constitution should be **living document** - review and update quarterly
- Can be referenced in all subsequent marketing commands
- Acts as validation criteria for `/marketspec.checklist`
- If project already has brand guidelines, incorporate them
- Keep it concise but comprehensive (2-5 pages is ideal)

---

## Integration with Other Commands

This constitution will be referenced by:
- `/marketspec.discover` - Ensures requirements align with principles
- `/marketspec.clarify` - Uses brand guidelines to resolve ambiguities
- `/marketspec.strategy` - Plans must align with marketing principles
- `/marketspec.create` - Generated specs must comply with standards
- `/marketspec.checklist` - Uses constitution as validation criteria

---

## See Also

- `/marketspec.discover` - Next step after defining constitution
- Domain Specification: `specs/domain/001-marketing-operations-spec/spec.md`
- Marketing Constitution examples in `examples/` directory
