---
name: marketspec.clarify
description: Clarify marketing objectives and resolve ambiguities
layer: sdm
status: implemented
source: Adapted from metaspec.sds.clarify
version: 0.3.0
---

# /marketspec.clarify

**Purpose**: Clarify ambiguities, resolve unanswered questions, and refine requirements from the discovery phase.

**Adapted from**: `metaspec.sds.clarify`

---

## Purpose

After initial discovery, there are often:
- Ambiguous requirements
- Unanswered questions
- Conflicting objectives
- Missing details

This command helps systematically:
- Identify areas needing clarification
- Resolve ambiguities through targeted questions
- Document assumptions and decisions
- Refine requirements for strategy planning

---

## Command Usage

```
/marketspec.clarify
/marketspec.clarify [specific area]
```

**Examples**:
```
/marketspec.clarify
/marketspec.clarify "target audience definition"
/marketspec.clarify "budget allocation"
```

---

## Prerequisites

- **Required**: Discovery document from `/marketspec.discover`
- **Recommended**: Constitution document from `/marketspec.constitution`

---

## Execution Steps

### Step 1: Read Discovery Document

Load the discovery document from `specs/discovery/[project-name]-discovery.md`:
- Identify sections marked as "TBD" or "Unknown"
- Find questions flagged for clarification
- Note any vague or ambiguous statements
- Check for conflicting information

### Step 2: Auto-Generate Clarification Questions

Analyze the discovery document and generate targeted questions:

**Categories**:

#### 2.1 Project Context Clarifications
```yaml
project_clarifications:
  - question: "What defines 'success' for this project?"
    reason: "Value proposition unclear"
    priority: "high"
  
  - question: "Who are your top 3 competitors?"
    reason: "Competitive landscape not defined"
    priority: "medium"
```

#### 2.2 Objective Clarifications
```yaml
objective_clarifications:
  - objective: "Increase brand awareness"
    questions:
      - "How will you measure awareness? (impressions, mentions, surveys?)"
      - "What's the baseline awareness level?"
      - "What geography/market segments are in scope?"
    rationale: "Objective is too vague to measure"
```

#### 2.3 Audience Clarifications
```yaml
audience_clarifications:
  - audience: "Developers"
    questions:
      - "What level? (junior, senior, lead, architect?)"
      - "What technologies? (Python, JS, Go, etc.?)"
      - "Company size preference? (startups, enterprises, all?)"
      - "Geographic focus? (US, global, specific regions?)"
    rationale: "Audience too broad to target effectively"
```

#### 2.4 Budget Clarifications
```yaml
budget_clarifications:
  - question: "Is the $5,000 budget monthly, quarterly, or total?"
    rationale: "Timeline for budget unclear"
  
  - question: "What's NOT included in budget? (salaries, tools?)"
    rationale: "Budget scope undefined"
  
  - question: "Can budget be reallocated between categories?"
    rationale: "Budget flexibility unclear"
```

#### 2.5 Timeline Clarifications
```yaml
timeline_clarifications:
  - question: "What happens if Q1 launch is delayed?"
    rationale: "Contingency plan needed"
  
  - question: "Are there intermediate milestones?"
    rationale: "Only end date specified"
```

#### 2.6 Constraints Clarifications
```yaml
constraints_clarifications:
  - question: "Are there brand guidelines or visual assets?"
    rationale: "Creative constraints undefined"
  
  - question: "Any legal/compliance requirements? (GDPR, CAN-SPAM, etc.)"
    rationale: "Regulatory constraints not mentioned"
```

### Step 3: Present Clarification Questions

Group questions by priority and present to user:

**Priority Structure**:
- 🔴 **Critical** (P0): Must answer to proceed
- 🟡 **Important** (P1): Should answer for better strategy
- 🟢 **Nice-to-have** (P2): Can document assumptions instead

### Step 4: Interactive Clarification Session

For each question:
1. **Ask the question** with context
2. **Provide examples** if helpful
3. **Suggest options** when appropriate
4. **Document the answer** clearly
5. **Note any new questions** that arise

**Example Flow**:
```
AI: Let's clarify your target audience "Developers":

Q1: What experience level are you targeting?
   a) Junior developers (0-2 years)
   b) Mid-level developers (3-5 years)
   c) Senior developers (5+ years)
   d) All levels

User: Primarily senior developers with some mid-level.

AI: Got it. "Senior (5+) and mid-level (3-5) developers" ✅

Q2: What technologies/languages do they use?
   Examples: Python, JavaScript, Go, Rust, Java, etc.

User: Mainly Python and JavaScript developers.

AI: Perfect. "Python and JavaScript developers" ✅

Q3: What company types?
   a) Startups (< 50 people)
   b) Mid-size (50-500 people)
   c) Enterprise (500+ people)
   d) Mix of all

User: Mix, but emphasis on startups and mid-size.

AI: Excellent. "Startups and mid-size companies (< 500 people)" ✅
```

### Step 5: Resolve Conflicts

If discovery revealed conflicting requirements:

```yaml
conflicts:
  - conflict: "Objective: 'Low budget' vs 'Aggressive growth'"
    resolution_needed: "Which takes priority?"
    options:
      a: "Focus on organic/low-cost growth (slower)"
      b: "Increase budget to support growth goals"
      c: "Adjust growth targets to match budget"
    user_choice: "b"
    resolution: "Increase budget to $10,000 for Q1"
```

### Step 6: Document Assumptions

For unanswered questions, document reasonable assumptions:

```yaml
assumptions:
  - assumption: "Primary audience is in US/Europe timezone"
    rationale: "Website analytics show 80% traffic from these regions"
    validation_needed: true
    validation_method: "Review analytics in strategy phase"
  
  - assumption: "Users prefer email over SMS for communications"
    rationale: "Industry standard for developer tools"
    validation_needed: false
```

### Step 7: Update Discovery Document

Create a new version or clarification session document:

**Option A**: Update original discovery (add "Clarifications" section)

**Option B**: Create separate clarification session document:

```markdown
# Clarification Session: [Project Name]

**Date**: 2025-11-16  
**Discovery Version**: 1.0  
**Clarification Version**: 1.0  
**Status**: Clarified, ready for strategy

---

## Questions Answered (15/18)

### Project Context ✅
- [Answered question 1]
- [Answered question 2]

### Target Audience ✅
- [Answered question 3]
- [Answered question 4]

### Budget ⚠️
- [Answered question 5]
- [Assumption documented for question 6]

---

## Resolutions

### Conflicts Resolved (2)
1. [Conflict 1 resolution]
2. [Conflict 2 resolution]

---

## Documented Assumptions (3)

1. **Assumption**: [Description]
   - **Rationale**: [Why]
   - **Validation**: [How/when to validate]

---

## Refined Requirements

### Target Audience (Refined)
**Original**: "Developers"
**Clarified**: "Senior and mid-level Python/JavaScript developers at startups and mid-size companies (< 500 employees), primarily US/Europe"

### Budget (Refined)
**Original**: "$5,000 (flexible)"
**Clarified**: "$10,000 for Q1 campaign, allocated as: Content $4K, Promotion $5K, Tools $1K"

---

## Unanswered Questions (3)

Low-priority questions that can be addressed later:
- [ ] Question 16: [Description]
- [ ] Question 17: [Description]  
- [ ] Question 18: [Description]

---

## Next Steps

✅ Discovery complete and clarified  
➡️ Ready for: `/marketspec.strategy`
```

### Step 8: Generate Clarification Summary

Create a brief summary highlighting key clarifications:

```yaml
clarification_summary:
  total_questions: 18
  answered: 15
  assumptions_documented: 3
  conflicts_resolved: 2
  
  key_clarifications:
    - "Target audience refined to senior/mid-level Python/JS developers"
    - "Budget increased from $5K to $10K for Q1"
    - "Primary metric clarified: GitHub stars (baseline: 50, target: 500)"
  
  readiness: "Ready for strategy planning"
```

---

## Success Criteria

- ✅ All P0 (critical) questions answered
- ✅ Conflicts resolved with clear decisions
- ✅ Assumptions documented for P1/P2 questions if not answered
- ✅ Discovery document updated or clarification session created
- ✅ User feels confident requirements are clear

---

## Output

**Primary Output**: 

**Option A**: Updated discovery document with "Clarifications" section  
`specs/discovery/[project-name]-discovery.md` (updated)

**Option B**: Separate clarification session document  
`specs/clarifications/[project-name]-clarification-2025-11-16.md`

**Structure**:
```
specs/
├── discovery/
│   └── [project-name]-discovery.md  # Original or updated
└── clarifications/
    └── [project-name]-clarification-2025-11-16.md  # Session notes
```

---

## Error Handling

- If no discovery document exists, suggest running `/marketspec.discover` first
- If user can't answer critical questions, suggest research/discussion
- If conflicts can't be resolved, document trade-offs and defer decision
- If too many assumptions needed, flag concern about readiness

---

## Example Interaction

```
User: /marketspec.clarify

AI: I'll help clarify the requirements from your discovery. Let me analyze the discovery document...

📄 Loading: specs/discovery/metaspec-discovery.md

I found **18 items** needing clarification:
- 🔴 Critical (5): Must answer to proceed
- 🟡 Important (8): Should answer for better strategy  
- 🟢 Nice-to-have (5): Can document assumptions

Let's start with the critical items:

---

**🔴 Critical Clarification 1/5: Target Audience**

Your discovery mentions "Developers" as target audience. Let's refine this:

Q1: What experience level?
   a) Junior (0-2 years)
   b) Mid-level (3-5 years)  
   c) Senior (5+ years)
   d) Mix (please specify)

User: Primarily senior, some mid-level.

AI: Great! "Senior (5+) and mid-level (3-5) developers" ✅

Q2: What technologies?

User: Python and JavaScript mainly.

AI: Perfect! "Python and JavaScript developers" ✅

[Continues through all critical questions]

---

[After answering critical questions]

AI: Excellent! All 5 critical questions answered ✅

Now let's tackle the 8 important questions. These will help create a better strategy.

**🟡 Important Clarification 1/8: Budget Timeline**

Discovery mentions "$5,000 (flexible)" but unclear if this is:
   a) Monthly budget
   b) Quarterly budget (Q1)
   c) Total for entire campaign

User: It's for Q1, but we can increase if needed.

AI: Perfect! Would you like to keep it at $5K or adjust based on objectives?

User: Let's increase to $10K for better reach.

AI: Excellent decision. "$10,000 for Q1 2025" ✅

[Continues...]

---

[After completing clarifications]

AI: Perfect! Clarification session complete:

✅ **Answered**: 15/18 questions  
📝 **Assumptions documented**: 3 questions  
🔧 **Conflicts resolved**: 2  

**Key Clarifications**:
1. Target audience: Senior/mid-level Python/JS devs at startups/mid-size
2. Budget: $10K for Q1 (increased from $5K)
3. Primary metric: GitHub stars (50 → 500 target)

📄 **Clarification document created**:
specs/clarifications/metaspec-clarification-2025-11-16.md

✅ **Ready for next step**: `/marketspec.strategy`

Would you like to proceed with strategy planning?
```

---

## Notes

- Clarification is iterative - can run multiple times
- Not all questions need answers - reasonable assumptions are okay
- Focus on reducing ambiguity, not achieving perfection
- Document the "why" behind decisions for future reference
- Use brand voice and constitution as guidance when clarifying

---

## Integration with Other Commands

Feeds into:
- `/marketspec.strategy` - Uses clarified requirements for planning
- `/marketspec.create` - Generates spec from clarified requirements

References:
- `/marketspec.constitution` - Use guidelines to resolve ambiguities
- `/marketspec.discover` - Source of requirements being clarified

---

## See Also

- `/marketspec.discover` - Previous step
- `/marketspec.strategy` - Next step
- Clarification examples in `examples/` directory
