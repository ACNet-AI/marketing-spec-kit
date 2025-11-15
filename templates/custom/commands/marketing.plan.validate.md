# Slash Command: /marketing.plan.validate

## Purpose

Validate a marketing plan against all validation rules (PLAN-01 to PLAN-05).

## Command Usage

```
/marketing.plan.validate <plan_id>
```

## Prerequisites

- Plan must exist in specification
- Specification file must be accessible

## Execution Steps

### Step 1: Read Plan

Load the specified plan from the specification file.

### Step 2: Run Validation Rules

Check all 5 validation rules:

1. **PLAN-01**: All objectives are non-empty strings
2. **PLAN-02**: duration_weeks is 4-52
3. **PLAN-03**: Budget allocation sums to total (±$0.01 tolerance)
4. **PLAN-04**: If status is APPROVED/ACTIVE, approval metadata exists
5. **PLAN-05**: Strategies count is 1-8

### Step 3: Report Results

Output validation results in a clear format:

```
✅ PLAN-01: Objectives valid (3 objectives)
✅ PLAN-02: Duration valid (13 weeks)
✅ PLAN-03: Budget balanced ($5000 total, $5000 allocated)
✅ PLAN-04: Approval valid (status: draft, no approval required)
✅ PLAN-05: Strategies valid (2 strategies)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ VALIDATION PASSED (5/5 rules)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Or if errors exist:

```
✅ PLAN-01: Objectives valid
✅ PLAN-02: Duration valid
❌ PLAN-03: Budget mismatch
   Total: $5000
   Allocated: $5100 (+$100)
   Fix: Adjust allocation to sum to $5000
✅ PLAN-04: Approval valid
✅ PLAN-05: Strategies valid

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❌ VALIDATION FAILED (4/5 rules passed)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Success Criteria

- All 5 rules checked
- Clear pass/fail for each rule
- Actionable error messages

## Example Interaction

```
User: /marketing.plan.validate q4-2025-growth-plan

AI: Validating plan 'q4-2025-growth-plan'...

✅ PLAN-01: Objectives valid (3 objectives)
✅ PLAN-02: Duration valid (13 weeks)
✅ PLAN-03: Budget balanced ($5000)
✅ PLAN-04: Approval not required (status: draft)
✅ PLAN-05: Strategies valid (2 strategies)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ VALIDATION PASSED (5/5 rules)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Plan is ready for execution!
```

