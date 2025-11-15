# Slash Command: /marketing.plan.get

## Purpose

Retrieve and display a marketing plan's complete details.

## Command Usage

```
/marketing.plan.get <plan_id>
```

## Prerequisites

- Plan must exist in specification

## Execution Steps

### Step 1: Read Plan

Load the specified plan from the specification file.

### Step 2: Format Output

Display plan details in a structured, readable format:

```markdown
# Marketing Plan: Q4 2025 Growth Plan

**ID**: `q4-2025-growth-plan`
**Status**: Draft
**Period**: 2025-10-01 to 2025-12-31 (13 weeks)

## Objectives

1. Increase brand awareness by 50%
2. Drive 10,000 new signups
3. Achieve $100K revenue

## Target Audience

### Early Adopters (High Priority)
- **Size**: 50,000
- **Description**: Tech-savvy developers looking for cutting-edge tools

## Strategies

### 1. Content Marketing
- **Description**: Publish weekly technical blog posts
- **Rationale**: Developers trust educational content
- **Success Criteria**: 10K monthly blog visitors

### 2. Community Engagement
- **Description**: Active participation in developer forums
- **Rationale**: Build trust and credibility
- **Success Criteria**: 1000 forum interactions

## Budget

**Total**: $5,000 USD

| Category | Amount |
|----------|--------|
| Content Creation | $2,000 |
| Paid Promotion | $2,500 |
| Tools | $300 |
| Contingency | $200 |

## Key Performance Indicators

| KPI | Target | Unit | Priority |
|-----|--------|------|----------|
| Brand Awareness | 50,000 | impressions | P0 |
| Signups | 10,000 | users | P0 |
| Revenue | $100,000 | USD | P1 |

## Campaigns

- (No campaigns yet)

## Timestamps

- **Created**: 2025-11-15 10:00:00 UTC
- **Updated**: 2025-11-15 10:00:00 UTC
```

## Success Criteria

- All plan fields displayed
- Readable formatting
- Proper grouping of related information

## Example Interaction

```
User: /marketing.plan.get q4-2025-growth-plan

AI: [Displays formatted plan as shown above]
```

