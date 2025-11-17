# Implementation Plan: marketing-spec-kit

**Toolkit**: marketing-spec-kit  
**Version**: 0.3.0  
**Language**: Python 3.9+  
**Architecture**: Modular  
**Created**: 2025-11-15  
**Updated**: 2025-11-17 (Domain Spec v0.3.0)

---

## ⚠️ Note on Regeneration

**This plan has been regenerated** to reflect Domain Spec v0.3.0 (9 entities, 45 rules, 10 SDM commands).

For a fully detailed implementation plan (with code examples, complete file structures, and detailed component designs), run `/metaspec.sdd.plan` in an AI conversation when ready to begin implementation.

This document provides **key architecture decisions** and **implementation guidance**.

---

## Overview

This plan details the implementation architecture for **marketing-spec-kit**, a Python toolkit that parses, validates, and provides AI-driven workflow guidance for marketing operations based on the Marketing Operations Specification (`domain/001-marketing-operations-spec v0.3.0`).

**Components**:
1. **Parser** - Parse YAML/JSON specifications (9 entities)
2. **Validator** - Enforce 45 validation rules
3. **CLI** - User commands (info, init, validate)
4. **Slash Commands** - 10 SDM workflow commands (workflow-guidance, Type B toolkit)

---

## Dependencies

**Domain Specification**:
- `specs/domain/001-marketing-operations-spec/spec.md` **v0.3.0** ✅ Current

**Key Dependencies**:
- **9 Entities**: Project, Product, MarketingPlan, Campaign, Channel, Tool, ContentTemplate, Milestone, Analytics
- **45 Validation Rules**: Comprehensive coverage (VR-P01 to VR-A05)
- **SDM Workflow**: 10-step Specification Usage Workflow (constitution → discover → clarify → strategy → checklist → tasks → analyze → create → review → optimize)
- **Entity State Machines**: 3 lifecycles (MarketingPlan, Campaign, Milestone)

**Dependency Usage**:
- **Parser**: Implements parsing for all 9 entities
- **Validator**: Implements all 45 validation rules
- **Slash Commands**: Implement 10-step SDM workflow (Type B - Workflow-Guidance Toolkit)

---

## Architecture

### Design Principles

1. **Modular**: Each component (Parser, Validator, CLI, Slash Commands) is independent
2. **Spec-Driven**: Domain specification is the source of truth
3. **Type-Safe**: Pydantic models for all entities
4. **AI-Friendly**: YAML format, slash commands for AI agents
5. **Extensible**: Easy to add new entities, rules, commands

### Component Architecture

```
User/AI Agent
      ↓
┌─────────────────────────────────────────────────────┐
│                  marketing-spec-kit                  │
│                                                      │
│  ┌──────────┐   ┌───────────┐   ┌──────────────┐  │
│  │  Parser  │ → │ Validator │ → │  CLI/Output  │  │
│  └──────────┘   └───────────┘   └──────────────┘  │
│       ↓              ↓                              │
│  ┌──────────────────────────────────────────────┐  │
│  │  MarketingSpec (9 entities, Pydantic)       │  │
│  └──────────────────────────────────────────────┘  │
│                                                      │
│  ┌──────────────────────────────────────────────┐  │
│  │  Slash Commands (10 SDM workflow commands)  │  │
│  └──────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

---

## Component 1: Parser

### Purpose
Parse YAML/JSON marketing specifications into typed Python objects.

### Entities (9 total)

Based on Domain Spec v0.3.0:

1. **Project** (8 fields) - Brand identity
2. **Product** (7 fields) - Feature offerings  
3. **MarketingPlan** (11 fields) - Strategic planning ⭐ NEW in v0.3.0
4. **Campaign** (14 fields) - Marketing activities (plan_id REQUIRED since v0.2.0)
5. **Channel** (9 fields) - Distribution platforms
6. **Tool** (9 fields) - MCP/API integrations
7. **ContentTemplate** (9 fields) - Brand guidelines
8. **Milestone** (8 fields) - Timeline markers
9. **Analytics** (10 fields) - Performance tracking ⭐ NEW in v0.3.0

### Implementation Strategy

```python
# Using Pydantic for type safety and validation
from pydantic import BaseModel, Field
import yaml

class Project(BaseModel):
    name: str
    tagline: str
    brand_voice: str
    # ... all 8 fields

class MarketingPlan(BaseModel):  # NEW
    id: str
    name: str
    project_id: str
    objectives: list[dict]
    # ... all 11 fields

# Parser
def parse_spec(file_path: str) -> MarketingSpec:
    data = yaml.safe_load(open(file_path))
    return MarketingSpec(**data)
```

### File Structure
```
src/marketing_spec_kit/
├── models.py          # Pydantic models for 9 entities
├── parser.py          # YAML/JSON parser
└── exceptions.py      # ParseError, SchemaError, etc.
```

---

## Component 2: Validator

### Purpose
Enforce 45 validation rules from Domain Spec v0.3.0.

### Validation Rules Breakdown

Based on Domain Spec validation rules:

- **Project Rules (VR-P01 to VR-P06)**: 6 rules
- **Product Rules (VR-PR01 to VR-PR05)**: 5 rules
- **MarketingPlan Rules (VR-MP01 to VR-MP10)**: 10 rules ⭐ NEW
- **Campaign Rules (VR-C01 to VR-C11)**: 11 rules (updated with plan_id requirement)
- **Channel Rules (VR-CH01 to VR-CH06)**: 6 rules
- **Tool Rules (VR-T01 to VR-T06)**: 6 rules
- **ContentTemplate Rules (VR-CT01 to VR-CT05)**: 5 rules
- **Milestone Rules (VR-M01 to VR-M05)**: 5 rules
- **Analytics Rules (VR-A01 to VR-A05)**: 5 rules ⭐ NEW

**Total**: 45 validation rules (was 25 in v1.0.0)

### Key New Validations

**MarketingPlan**:
- VR-MP07: Campaign budgets must not exceed plan total_budget
- VR-MP08: Campaign dates must be within plan period
- VR-MP10: At least one P0 objective required

**Campaign**:
- VR-C02: plan_id is REQUIRED (breaking change since v0.2.0)
- VR-C11: Campaign dates must be within referenced plan's period

**Analytics**:
- VR-A01: entity_id must reference existing Campaign or MarketingPlan
- VR-A04: Insights must have type (success/concern/opportunity)

### Implementation Strategy

```python
class Validator:
    def validate(self, spec: MarketingSpec) -> ValidationResult:
        errors = []
        warnings = []
        
        # Run all 45 validation rules
        errors.extend(self._validate_project(spec.project))
        errors.extend(self._validate_products(spec.products))
        errors.extend(self._validate_plans(spec.marketing_plans))  # NEW
        errors.extend(self._validate_campaigns(spec.campaigns))
        # ... 9 entity types total
        
        return ValidationResult(errors=errors, warnings=warnings)
```

### File Structure
```
src/marketing_spec_kit/
├── validator.py       # 45 validation rules
└── exceptions.py      # ValidationError with error codes
```

---

## Component 3: CLI

### Purpose
Provide command-line interface for users.

### Commands

1. **`info`** - Show toolkit information
   - Display version, domain spec version (v0.3.0)
   - Show entity count (9), validation rule count (45)

2. **`init`** - Initialize new specification
   - Create template YAML with all 9 entities
   - Support --minimal flag (Project only)

3. **`validate`** - Validate specification
   - Run all 45 validation rules
   - Output errors/warnings with actionable fixes

### Implementation Strategy

```python
import typer

app = typer.Typer()

@app.command()
def validate(file: str):
    """Validate marketing specification."""
    spec = parse_spec(file)
    result = validator.validate(spec)
    
    if result.errors:
        console.print(f"[red]✗ {len(result.errors)} errors[/red]")
        for error in result.errors:
            console.print(f"  {error.code}: {error.message}")
    else:
        console.print("[green]✓ Valid specification[/green]")
```

### File Structure
```
src/marketing_spec_kit/
├── cli.py             # Typer app with 3 commands
└── __main__.py        # Entry point
```

---

## Component 4: Slash Commands (10 SDM Workflow Commands)

### Purpose
Provide AI-driven workflow guidance for creating marketing specifications.

### Toolkit Type

**Type B - Workflow-Guidance Toolkit** (Speckit standard)

- Purpose: Guide users to CREATE marketing specifications
- NOT for accessing existing data (Type A)
- Follows MetaSpec/spec-kit pattern
- Commands map 1:1 to Domain Spec's Specification Usage Workflow

### Command Inventory

Based on Domain Spec's SDM (Spec-Driven Marketing) workflow:

**Core Workflow (8 commands)**:
1. `/marketspec.constitution` - Establish project principles
2. `/marketspec.discover` - Identify business objectives
3. `/marketspec.clarify` - Resolve ambiguities
4. `/marketspec.strategy` - Design campaign structure
5. `/marketspec.checklist` - Validate completeness
6. `/marketspec.tasks` - Break down into actions
7. `/marketspec.analyze` - Check consistency
8. `/marketspec.create` - Generate YAML specification

**Extension Commands (2 commands)**:
9. `/marketspec.review` - Collect execution feedback
10. `/marketspec.optimize` - Generate improvements

### Workflow Flow

```
Core Flow:      constitution → discover → strategy → create
Quality Gates:             ↓ clarify ↓   ↓ checklist  ↓ analyze
Post-Execution:  execute campaign → review → optimize → [next cycle]
```

### Implementation Strategy

Each command is a Markdown file in `templates/sdm/commands/` with:
- Command description
- Input requirements
- Output format (which entities to create)
- Quality criteria
- Example output

```
templates/
└── sdm/
    ├── README.md
    └── commands/
        ├── marketspec.constitution.md
        ├── marketspec.discover.md
        ├── marketspec.clarify.md
        ├── marketspec.strategy.md
        ├── marketspec.checklist.md
        ├── marketspec.tasks.md
        ├── marketspec.analyze.md
        ├── marketspec.create.md
        ├── marketspec.review.md
        └── marketspec.optimize.md
```

**Status**: ✅ Already implemented in `templates/sdm/commands/`

---

## File Structure

```
marketing-spec-kit/
├── src/
│   └── marketing_spec_kit/
│       ├── __init__.py           # Package init, version
│       ├── models.py              # 9 Pydantic entity models
│       ├── parser.py              # YAML/JSON parser
│       ├── validator.py           # 45 validation rules
│       ├── cli.py                 # CLI commands (typer)
│       ├── exceptions.py          # Custom exceptions
│       └── __main__.py            # CLI entry point
│
├── templates/
│   └── sdm/
│       ├── README.md              # SDM workflow documentation
│       └── commands/              # 10 slash command files ✅
│
├── tests/
│   ├── test_parser.py             # Parser tests (9 entities)
│   ├── test_validator.py          # Validator tests (45 rules)
│   ├── test_cli.py                # CLI tests
│   └── fixtures/                  # Test YAML files
│
├── examples/
│   ├── complete-example.yaml      # Full example (9 entities)
│   ├── minimal-example.yaml       # Minimal example
│   └── sdm-workflow-example.md    # SDM workflow walkthrough
│
├── pyproject.toml                 # Project config
├── README.md                      # User documentation
├── AGENTS.md                      # AI agent guidance
└── CHANGELOG.md                   # Version history
```

---

## Implementation Phases

### Phase 1: Core Components (Weeks 1-2)
- [ ] Create Pydantic models for 9 entities
- [ ] Implement YAML/JSON parser
- [ ] Basic error handling

### Phase 2: Validation (Week 3)
- [ ] Implement 45 validation rules
- [ ] Error message formatting
- [ ] Cross-entity validation

### Phase 3: CLI (Week 4)
- [ ] `info` command
- [ ] `init` command with templates
- [ ] `validate` command with rich output

### Phase 4: Testing & Documentation (Week 5)
- [ ] Unit tests for all components
- [ ] Integration tests
- [ ] README and examples

### Phase 5: Polish & Release (Week 6)
- [ ] Code quality (ruff, mypy)
- [ ] Performance optimization
- [ ] Release preparation

**Note**: Slash commands (10 SDM workflow commands) are already implemented in `templates/sdm/commands/`.

---

## Success Criteria

### Functional Requirements
- ✅ Parse all 9 entity types from YAML/JSON
- ✅ Enforce all 45 validation rules
- ✅ CLI commands working (info, init, validate)
- ✅ Clear error messages with fix suggestions
- ✅ Support both YAML and JSON formats

### Quality Requirements
- ✅ 80%+ code coverage
- ✅ Type hints complete (mypy passes)
- ✅ No critical linting errors (ruff)
- ✅ All 45 validation rules have dedicated tests

### Documentation Requirements
- ✅ README with quickstart
- ✅ AGENTS.md with slash command docs
- ✅ Complete examples (minimal, full, workflow)
- ✅ CHANGELOG tracking version history

---

## Technology Stack

**Core**:
- Python 3.9+
- Pydantic 2.0+ (entity models, validation)
- PyYAML (YAML parsing)
- Typer (CLI framework)
- Rich (CLI output formatting)

**Development**:
- pytest (testing)
- ruff (linting)
- mypy (type checking)
- pytest-cov (coverage)

**Optional**:
- jsonschema (JSON Schema generation)

---

## Next Steps

1. Review this plan for completeness
2. Set up project structure (`pyproject.toml`, directory layout)
3. Begin Phase 1: Implement Pydantic models for 9 entities
4. Reference Domain Spec v0.3.0 for all entity schemas and validation rules

---

**Generated by**: Manual plan regeneration (MetaSpec v0.8.1 guidance)  
**Based on**: Domain Spec v0.3.0 (9 entities, 45 rules, 10 SDM commands)  
**Last Updated**: 2025-11-17

**For detailed implementation guidance**: Run `/metaspec.sdd.plan` when ready to begin coding.

