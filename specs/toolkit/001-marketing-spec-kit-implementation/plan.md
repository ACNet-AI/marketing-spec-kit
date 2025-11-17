# Implementation Plan: marketing-spec-kit

**Toolkit**: marketing-spec-kit  
**Version**: 1.0.0  
**Language**: Python 3.9+  
**Architecture**: Modular  
**Created**: 2025-11-15

---

## Overview

This plan details the implementation architecture for **marketing-spec-kit**, a Python toolkit that parses, validates, and enables AI-driven marketing operations based on the Marketing Operations Specification (`domain/001-marketing-operations-spec`).

**Components**:
1. Parser - Parse YAML/JSON specifications (7 entities)
2. Validator - Enforce 25 validation rules
3. CLI - User commands (init, validate)
4. Slash Commands - 13 AI agent operations

---

## Dependencies

**Domain Specification**:
- `specs/domain/001-marketing-operations-spec/spec.md` v1.0.0 ✅ Verified

**Dependency Usage**:
- Parser: Implements parsing for all 7 entities (Project, Product, Campaign, Channel, Tool, ContentTemplate, Milestone)
- Validator: Implements all 25 validation rules (VR-P01 to VR-M05)
- Slash Commands: Implements 13 AI operations defined in specification

---

## Technical Context

### Language: Python 3.9+

**Rationale**:
- **Target users**: Developers, open source maintainers, product teams (Python community)
- **Ecosystem strength**: pydantic (validation), typer (CLI), rich (formatting)
- **Deployment**: pip installable, cross-platform, minimal setup
- **Performance**: I/O-bound workload (parsing/validation) suits Python

**Key Dependencies**:

| Package | Version | Purpose | Justification |
|---------|---------|---------|---------------|
| pydantic | ≥2.0.0 | Data validation, models | Type-safe entity models, automatic validation |
| typer | ≥0.9.0 | CLI framework | Modern CLI with auto-help, parameter validation |
| pyyaml | ≥6.0 | YAML parsing | YAML is primary format for marketing specs |
| jsonschema | ≥4.0.0 | JSON Schema support | Alternative format support |
| rich | ≥13.0.0 | Terminal UI | Progress bars, tables, colored output |

**Development Dependencies**:
- pytest (≥7.4.0) - Testing framework
- pytest-cov (≥4.1.0) - Coverage reporting
- mypy (≥1.0.0) - Static type checking
- ruff (≥0.1.0) - Linting and formatting

### Performance Targets

- **Parse time**: < 100ms for typical spec (< 10 entities)
- **Validate time**: < 200ms for all 25 rules
- **CLI startup**: < 500ms
- **Memory usage**: < 50MB for typical spec

### Extensibility Requirements

- **Custom validators**: Plugin system for project-specific rules
- **Template system**: User-provided entity templates
- **Hook system**: Pre/post validation hooks

---

## Project Structure

```
marketing-spec-kit/
├── README.md                            # User documentation
├── AGENTS.md                            # AI agent guide
├── CHANGELOG.md                         # Version history
├── pyproject.toml                       # Python project configuration
├── uv.lock                              # Dependency lock file
├── LICENSE                              # MIT License
│
├── memory/
│   └── constitution.md                  # Design principles
│
├── specs/
│   ├── domain/
│   │   └── 001-marketing-operations-spec/   # Domain specification (dependency)
│   │       ├── spec.md                      # ✅ Verified
│   │       ├── analysis/
│   │       └── checklists/
│   │
│   └── toolkit/
│       └── 001-marketing-spec-kit-implementation/
│           ├── spec.md                  # THIS toolkit specification
│           ├── plan.md                  # THIS file
│           └── tasks.md                 # (To be generated)
│
├── templates/
│   ├── custom/
│   │   └── commands/                    # Slash commands (13 files)
│   │       ├── marketing.project.md
│   │       ├── marketing.product.md
│   │       ├── marketing.campaign.md
│   │       ├── marketing.channel.md
│   │       ├── marketing.tool.md
│   │       ├── marketing.content_template.md
│   │       ├── marketing.milestone.md
│   │       ├── marketing.generate.post.md
│   │       ├── marketing.generate.article.md
│   │       ├── marketing.generate.email.md
│   │       ├── marketing.generate.landing_page.md
│   │       ├── marketing.execute.schedule.md
│   │       └── marketing.execute.publish.md
│   │
│   └── entity_templates/                # Init command templates
│       ├── default.yaml                 # Default template (all entities)
│       ├── minimal.yaml                 # Minimal template (Project only)
│       └── full.yaml                    # Full example with data
│
├── src/
│   └── marketing_spec_kit/
│       ├── __init__.py                  # Package exports, version
│       ├── models.py                    # Pydantic models (7 entities)
│       ├── parser.py                    # YAML/JSON parser
│       ├── validator.py                 # 25 validation rules
│       ├── cli.py                       # Typer CLI app
│       ├── exceptions.py                # Custom exceptions (13 error codes)
│       └── utils.py                     # Helper functions
│
├── tests/
│   ├── unit/
│   │   ├── test_parser.py               # Parser unit tests
│   │   ├── test_validator.py            # Validator rule tests (25 tests)
│   │   ├── test_models.py               # Pydantic model tests
│   │   ├── test_cli.py                  # CLI command tests
│   │   └── test_exceptions.py           # Exception handling tests
│   │
│   ├── integration/
│   │   ├── test_end_to_end.py           # Full workflow tests
│   │   └── test_cli_integration.py      # CLI integration tests
│   │
│   └── fixtures/
│       ├── valid_specs/
│       │   ├── minimal.yaml             # Bare minimum spec
│       │   ├── full.yaml                # Complete spec
│       │   └── metaspec_example.yaml    # Real-world example
│       │
│       └── invalid_specs/               # One per validation rule (25 files)
│           ├── vr_p01_duplicate_name.yaml
│           ├── vr_p02_long_tagline.yaml
│           ├── vr_c04_zero_budget.yaml
│           └── ... (22 more files)
│
├── examples/
│   └── metaspec-marketing.yaml          # Complete MetaSpec marketing spec
│
└── scripts/
    └── init.sh                          # Project initialization
```

---

## Phase 0: Domain Research

### Research Focus

**Domain**: Marketing Operations & Content Management

**Research Objectives**:
1. Marketing specification formats and standards
2. Existing marketing automation tools and their approaches
3. Common validation patterns for marketing content
4. Error message best practices for marketing tools

### Research Tasks

#### Task 1: Marketing Standards Research

**Query**: "Marketing operations workflow standards, campaign management best practices"

**Expected Findings**:
- Marketing funnel models (AIDA: Awareness, Interest, Desire, Action)
- Campaign management frameworks (Goals, KPIs, Channels)
- Content management standards (style guides, brand voice, templates)
- Marketing metrics standards (CTR, CPM, ROAS, CPC)

**Application to Architecture**:
- Inform entity structure (Campaign.goal should use AIDA stages)
- Validation rules should enforce industry standards (e.g., CTR range 0-1)
- Error messages should use marketing terminology

#### Task 2: Reference Tool Analysis

**Tools to Analyze**:
1. **HubSpot** - Marketing automation platform
   - Analyze: Campaign structure, content templates, channel management
2. **Mailchimp** - Email marketing tool
   - Analyze: Template system, audience segmentation, validation
3. **Hootsuite** - Social media management
   - Analyze: Multi-channel publishing, scheduling, content constraints
4. **Buffer** - Social scheduling tool
   - Analyze: Post formatting, character limits, platform variations

**Expected Insights**:
- How tools structure marketing campaigns
- Common validation patterns (character limits, required fields)
- Error message approaches
- Template and content management patterns

**Application to Architecture**:
- Parser should support common campaign structures
- Validator should check platform-specific constraints (Twitter 280 chars)
- CLI should provide intuitive commands similar to existing tools

#### Task 3: Validation Pattern Research

**Query**: "Marketing content validation, brand guideline enforcement, style guide checking"

**Expected Patterns**:
- **Required field validation**: name, budget, dates, target audience
- **Format validation**: URLs (HTTPS), email formats, social handles
- **Range validation**: budget > 0, dates (start < end), CTR (0-1)
- **Enum validation**: brand_voice, campaign_goal, channel_type
- **Reference validation**: Campaign → Product IDs, Channel → Tool ID

**Application to Architecture**:
- Validator should group rules by pattern type
- Error messages should be consistent within pattern groups
- Custom validators should follow same patterns

#### Task 4: Error Message Best Practices

**Query**: "Effective error messages for developer tools, CLI validation feedback"

**Best Practices Expected**:
- **Clear location**: Line number, field name, entity ID
- **Actionable fix**: Specific suggestion, not just "invalid"
- **Error codes**: Categorized (MKT-VAL-001, MKT-REF-001)
- **Examples**: Show valid examples when possible

**Application to Architecture**:
- Exceptions should include: code, message, entity, field, fix
- Validator should collect all errors (don't stop at first)
- CLI should format errors with rich (colors, tables)

### Research Output Location

**File**: `specs/toolkit/001-marketing-spec-kit-implementation/research.md`

**Format**:
```markdown
# Domain Research: Marketing Operations

## Marketing Standards
- AIDA Funnel Model
- Marketing Metrics Standards (CTR, CPM, ROAS)
- Campaign Management Best Practices

## Reference Tool Insights
- HubSpot: Campaign structure, content templates
- Mailchimp: Audience segmentation, template system
- Hootsuite: Multi-channel management, scheduling

## Validation Patterns
- Required field validation
- Format validation (URLs, dates, enums)
- Reference integrity validation

## Error Message Recommendations
- Include error codes (MKT-XXX-YYY)
- Provide actionable fixes
- Show valid examples

## Architecture Recommendations
- Use AIDA model for Campaign.goal enum
- Implement platform-specific constraints (Channel.constraints)
- Follow marketing terminology in error messages
```

---

## Phase 1: Architecture Design

### Component Overview

```
User Input (YAML/JSON)
    ↓
  Parser (models.py + parser.py)
    - Load file (pyyaml)
    - Parse entities (7 types)
    - Resolve references
    ↓
  MarketingSpec Object
    - Project, Products, Campaigns, etc.
    - Typed with Pydantic
    ↓
  Validator (validator.py)
    - Run 25 validation rules
    - Collect errors/warnings
    ↓
  ValidationResult
    - valid: bool
    - errors: List[ValidationError]
    - warnings: List[ValidationWarning]
    ↓
  CLI Output (cli.py + rich)
    - Format results
    - Show errors with fixes
    - Exit with appropriate code
```

### Component 1: Models & Parser

#### Architecture: models.py

**Purpose**: Define Pydantic models for 7 entities from domain specification

**Entity Models** (from `domain/001-marketing-operations-spec`):

```python
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Dict, Optional
from enum import Enum

# Enums
class BrandVoice(str, Enum):
    TECHNICAL = "Technical"
    FRIENDLY = "Friendly"
    PROFESSIONAL = "Professional"
    CASUAL = "Casual"
    EDUCATIONAL = "Educational"

class CampaignGoal(str, Enum):
    AWARENESS = "awareness"
    CONSIDERATION = "consideration"
    CONVERSION = "conversion"

class ChannelType(str, Enum):
    SOCIAL_MEDIA = "social_media"
    EMAIL = "email"
    BLOG = "blog"
    FORUM = "forum"
    VIDEO = "video"
    PODCAST = "podcast"

# Entity Models
class Project(BaseModel):
    """Project entity - Brand identity and core values"""
    name: str = Field(..., description="Official project name")
    tagline: str = Field(..., max_length=100, description="Short memorable description")
    brand_voice: BrandVoice = Field(..., description="Primary brand personality")
    website: HttpUrl = Field(..., description="Official project website (HTTPS)")
    target_audience: List[str] = Field(..., min_items=1, description="Primary user segments")
    value_propositions: List[str] = Field(..., min_items=1, description="Core benefits")
    logo_url: Optional[HttpUrl] = Field(None, description="Project logo image URL")
    social_handles: Optional[Dict[str, str]] = Field(None, description="Social media accounts")

class Product(BaseModel):
    """Product entity - Features and positioning"""
    id: str = Field(..., pattern="^[a-z0-9-]+$", description="Unique product identifier")
    name: str = Field(..., description="Display name")
    description: str = Field(..., max_length=500, description="Detailed description")
    project_id: str = Field(..., description="Parent Project identifier")
    target_audience: List[str] = Field(..., min_items=1, description="User segments")
    key_features: List[str] = Field(..., min_items=1, description="Top 3-5 features")
    positioning: Optional[str] = Field(None, max_length=200, description="Unique selling proposition")
    launch_date: Optional[str] = Field(None, description="Launch date (ISO format)")

class Campaign(BaseModel):
    """Campaign entity - Time-bound marketing activity"""
    id: str = Field(..., pattern="^[a-z0-9-]+$")
    name: str
    goal: CampaignGoal
    project_id: str
    product_ids: Optional[List[str]] = None
    target_audience: List[str] = Field(..., min_items=1)
    budget: float = Field(..., gt=0)
    start_date: str  # ISO date
    end_date: str    # ISO date
    channels: List[str] = Field(..., min_items=1)
    kpis: Optional[Dict[str, float]] = None
    status: str = Field(default="draft")

class Channel(BaseModel):
    """Channel entity - Distribution platform"""
    id: str = Field(..., pattern="^[a-z0-9-]+$")
    name: str
    type: ChannelType
    platform: str
    audiences: Optional[List[str]] = None
    content_types: List[str] = Field(..., min_items=1)
    constraints: Optional[Dict[str, any]] = None
    tool_id: Optional[str] = None
    config: Optional[Dict[str, any]] = None

class Tool(BaseModel):
    """Tool entity - MCP server or REST API"""
    id: str = Field(..., pattern="^[a-z0-9-]+$")
    name: str
    type: str  # mcp, rest_api, manual
    capabilities: List[str] = Field(..., min_items=1)
    mcp_config: Optional[Dict[str, str]] = None
    api_config: Optional[Dict[str, any]] = None
    channel_ids: Optional[List[str]] = None
    status: str = Field(default="active")

class ContentTemplate(BaseModel):
    """ContentTemplate entity - Brand guidelines"""
    id: str = Field(..., pattern="^[a-z0-9-]+$")
    name: str
    type: str
    tone: str
    style_guidelines: List[str] = Field(..., min_items=1)
    constraints: Optional[Dict[str, any]] = None
    examples: Optional[List[str]] = None
    project_id: str

class Milestone(BaseModel):
    """Milestone entity - Release events"""
    id: str = Field(..., pattern="^[a-z0-9-]+$")
    name: str
    type: str
    date: str  # ISO date
    description: Optional[str] = Field(None, max_length=500)
    project_id: str
    product_ids: Optional[List[str]] = None
    campaign_ids: Optional[List[str]] = None
    status: str = Field(default="planned")

class MarketingSpec(BaseModel):
    """Root specification object"""
    project: Project
    products: Optional[List[Product]] = Field(default_factory=list)
    campaigns: Optional[List[Campaign]] = Field(default_factory=list)
    channels: Optional[List[Channel]] = Field(default_factory=list)
    tools: Optional[List[Tool]] = Field(default_factory=list)
    content_templates: Optional[List[ContentTemplate]] = Field(default_factory=list)
    milestones: Optional[List[Milestone]] = Field(default_factory=list)
```

**Design Decisions**:
- Use pydantic for automatic validation and type safety
- Enums for constrained values (brand_voice, campaign_goal)
- Field validators for complex constraints (pattern, length, range)
- Optional fields with default_factory for lists
- HttpUrl type for automatic URL validation

#### Architecture: parser.py

**Purpose**: Parse YAML/JSON files into MarketingSpec objects

```python
from pathlib import Path
from typing import Union
import yaml
import json
from .models import MarketingSpec
from .exceptions import ParseError

class MarketingSpecParser:
    """Parse marketing specifications from YAML/JSON"""
    
    def parse(
        self, 
        source: Union[str, Path, dict], 
        format: str = "yaml"
    ) -> MarketingSpec:
        """
        Parse marketing specification
        
        Args:
            source: File path, string content, or dict
            format: "yaml", "json", or "dict"
        
        Returns:
            MarketingSpec object
        
        Raises:
            ParseError: If parsing fails
        """
        try:
            # Load data
            if format == "dict":
                data = source
            elif format == "yaml":
                if isinstance(source, (str, Path)):
                    with open(source, 'r') as f:
                        data = yaml.safe_load(f)
                else:
                    data = yaml.safe_load(source)
            elif format == "json":
                if isinstance(source, (str, Path)):
                    with open(source, 'r') as f:
                        data = json.load(f)
                else:
                    data = json.loads(source)
            
            # Parse with pydantic (automatic validation)
            spec = MarketingSpec(**data)
            return spec
            
        except yaml.YAMLError as e:
            raise ParseError(
                code="MKT-VAL-001",
                message=f"Invalid YAML syntax: {e}",
                fix="Check YAML syntax, ensure proper indentation"
            )
        except json.JSONDecodeError as e:
            raise ParseError(
                code="MKT-VAL-001",
                message=f"Invalid JSON syntax: {e}",
                fix="Check JSON syntax, ensure proper brackets and quotes"
            )
        except Exception as e:
            raise ParseError(
                code="MKT-VAL-002",
                message=f"Parsing failed: {e}",
                fix="Check field types and required fields"
            )
```

**Design Decisions**:
- Support 3 formats: YAML (primary), JSON (alternative), dict (programmatic)
- Let pydantic handle field validation (automatic)
- Convert parsing errors to custom ParseError with error codes
- Provide actionable fix suggestions

---

### Component 2: Validator

#### Architecture: validator.py

**Purpose**: Enforce 25 validation rules from domain specification

**Validator Structure**:

```python
from typing import List
from .models import MarketingSpec
from .exceptions import ValidationError, ValidationWarning

class ValidationResult:
    """Validation result with errors/warnings"""
    def __init__(self):
        self.valid = True
        self.errors: List[ValidationError] = []
        self.warnings: List[ValidationWarning] = []
        self.info: List[str] = []
        self.rules_checked = 0
        self.rules_passed = 0

class MarketingSpecValidator:
    """Validate marketing specifications"""
    
    def validate(self, spec: MarketingSpec) -> ValidationResult:
        """
        Validate specification against all rules
        
        Args:
            spec: Parsed MarketingSpec object
        
        Returns:
            ValidationResult with errors/warnings
        """
        result = ValidationResult()
        
        # Project validation (6 rules)
        self._validate_project(spec.project, result)
        
        # Product validation (5 rules)
        for product in spec.products:
            self._validate_product(product, spec, result)
        
        # Campaign validation (9 rules)
        for campaign in spec.campaigns:
            self._validate_campaign(campaign, spec, result)
        
        # Channel validation (6 rules)
        for channel in spec.channels:
            self._validate_channel(channel, spec, result)
        
        # Tool validation (6 rules)
        for tool in spec.tools:
            self._validate_tool(tool, spec, result)
        
        # ContentTemplate validation (5 rules)
        for template in spec.content_templates:
            self._validate_content_template(template, spec, result)
        
        # Milestone validation (5 rules)
        for milestone in spec.milestones:
            self._validate_milestone(milestone, spec, result)
        
        # Calculate final result
        result.valid = len(result.errors) == 0
        result.rules_passed = result.rules_checked - len(result.errors) - len(result.warnings)
        
        return result
    
    def _validate_project(self, project, result):
        """Validate Project entity (VR-P01 to VR-P06)"""
        result.rules_checked += 6
        
        # VR-P01: name unique (workspace-level check)
        # VR-P02: tagline ≤ 100 chars (handled by pydantic)
        # VR-P03: website is HTTPS (handled by pydantic HttpUrl)
        # VR-P04: target_audience ≥ 1 (handled by pydantic min_items)
        # VR-P05: brand_voice enum (handled by pydantic Enum)
        
        # VR-P06: social_handles format
        if project.social_handles:
            for platform, handle in project.social_handles.items():
                if platform == "twitter" and not handle.startswith("@"):
                    result.warnings.append(
                        ValidationWarning(
                            code="MKT-VAL-003",
                            message=f"Twitter handle should start with @: {handle}",
                            entity="project",
                            field="social_handles.twitter",
                            fix=f"Change to: @{handle}"
                        )
                    )
    
    def _validate_product(self, product, spec, result):
        """Validate Product entity (VR-PR01 to VR-PR05)"""
        result.rules_checked += 5
        
        # VR-PR01: id unique
        ids = [p.id for p in spec.products]
        if ids.count(product.id) > 1:
            result.errors.append(
                ValidationError(
                    code="MKT-REF-002",
                    message=f"Duplicate product ID: {product.id}",
                    entity=product.id,
                    field="id",
                    fix="Use unique product IDs"
                )
            )
        
        # VR-PR02: project_id exists (checked by parser)
        # VR-PR03: description ≤ 500 (handled by pydantic)
        
        # VR-PR04: key_features 3-5 items (warning)
        if len(product.key_features) < 3 or len(product.key_features) > 5:
            result.warnings.append(
                ValidationWarning(
                    code="MKT-VAL-003",
                    message=f"Product {product.id}: key_features should have 3-5 items (has {len(product.key_features)})",
                    entity=product.id,
                    field="key_features",
                    fix="Provide 3-5 key features for best communication"
                )
            )
        
        # VR-PR05: launch_date validation (if provided)
    
    def _validate_campaign(self, campaign, spec, result):
        """Validate Campaign entity (VR-C01 to VR-C09)"""
        result.rules_checked += 9
        
        # VR-C01: id unique
        # VR-C02: project_id exists
        
        # VR-C03: product_ids all exist
        if campaign.product_ids:
            product_ids = [p.id for p in spec.products]
            for pid in campaign.product_ids:
                if pid not in product_ids:
                    result.errors.append(
                        ValidationError(
                            code="MKT-REF-001",
                            message=f"Campaign {campaign.id} references non-existent product: {pid}",
                            entity=campaign.id,
                            field="product_ids",
                            fix=f"Create product with ID '{pid}' or remove reference"
                        )
                    )
        
        # VR-C04: budget > 0 (handled by pydantic gt=0)
        
        # VR-C05: start_date < end_date
        from datetime import datetime
        try:
            start = datetime.fromisoformat(campaign.start_date)
            end = datetime.fromisoformat(campaign.end_date)
            if start >= end:
                result.errors.append(
                    ValidationError(
                        code="MKT-VAL-003",
                        message=f"Campaign {campaign.id}: start_date must be before end_date",
                        entity=campaign.id,
                        field="start_date, end_date",
                        fix=f"Ensure start ({campaign.start_date}) < end ({campaign.end_date})"
                    )
                )
        except ValueError as e:
            result.errors.append(
                ValidationError(
                    code="MKT-VAL-002",
                    message=f"Campaign {campaign.id}: Invalid date format: {e}",
                    entity=campaign.id,
                    field="start_date or end_date",
                    fix="Use ISO date format: YYYY-MM-DD"
                )
            )
        
        # VR-C06: start_date not in past (warning)
        # VR-C07: channels all exist
        # VR-C08: CTR range 0-1
        # VR-C09: ROAS ≥ 3 (warning)
    
    # Similar methods for Channel, Tool, ContentTemplate, Milestone...
```

**Validation Rule Summary** (25 rules):

| Rule Group | Count | Validator Method |
|------------|-------|------------------|
| Project (VR-P01-P06) | 6 | `_validate_project()` |
| Product (VR-PR01-PR05) | 5 | `_validate_product()` |
| Campaign (VR-C01-C09) | 9 | `_validate_campaign()` |
| Channel (VR-CH01-CH06) | 6 | `_validate_channel()` |
| Tool (VR-T01-T06) | 6 | `_validate_tool()` |
| ContentTemplate (VR-CT01-CT05) | 5 | `_validate_content_template()` |
| Milestone (VR-M01-M05) | 5 | `_validate_milestone()` |
| **Total** | **42** | 7 methods |

**Note**: Some rules are automatically handled by pydantic (field types, lengths, patterns), so actual validator method implementations focus on cross-entity validation and business logic.

---

### Component 3: CLI

#### Architecture: cli.py

**Purpose**: Provide user-facing commands (info, init, validate)

```python
import typer
from rich.console import Console
from rich.table import Table
from pathlib import Path

from .parser import MarketingSpecParser
from .validator import MarketingSpecValidator
from .exceptions import ParseError, ValidationError

app = typer.Typer(
    name="marketing_spec_kit",
    help="Marketing Operations Specification Toolkit",
    no_args_is_help=True
)
console = Console()

@app.command()
def info():
    """Show toolkit information"""
    console.print("[cyan]Toolkit:[/cyan] marketing_spec_kit")
    console.print("[cyan]Version:[/cyan] 0.1.0")
    console.print("[cyan]Domain:[/cyan] Marketing Operations")
    console.print("\n[yellow]Commands:[/yellow]")
    console.print("  info     - Show toolkit information")
    console.print("  init     - Initialize new marketing specification")
    console.print("  validate - Validate marketing specification")

@app.command()
def init(
    filename: str = typer.Argument(..., help="Output file name"),
    template: str = typer.Option("default", help="Template: minimal, default, full"),
    format: str = typer.Option("yaml", help="Format: yaml, json"),
    overwrite: bool = typer.Option(False, help="Overwrite existing file")
):
    """Initialize new marketing specification"""
    
    # Check if file exists
    output_path = Path(filename)
    if output_path.exists() and not overwrite:
        console.print(f"[red]Error: File already exists: {filename}[/red]")
        console.print("Use --overwrite to replace it")
        raise typer.Exit(1)
    
    # Load template
    template_path = Path(__file__).parent / "templates" / f"{template}.yaml"
    if not template_path.exists():
        console.print(f"[red]Error: Template not found: {template}[/red]")
        console.print("Available templates: minimal, default, full")
        raise typer.Exit(2)
    
    # Copy template to output
    import shutil
    shutil.copy(template_path, output_path)
    
    console.print(f"[green]✓[/green] Created: {filename}")
    console.print("\n[yellow]Next steps:[/yellow]")
    console.print(f"  1. Edit {filename} to define your marketing specification")
    console.print(f"  2. Run: marketing_spec_kit validate {filename}")

@app.command()
def validate(
    filename: str = typer.Argument(..., help="Specification file to validate"),
    strict: bool = typer.Option(False, help="Treat warnings as errors"),
    format: str = typer.Option("text", help="Output format: text, json, table"),
    quiet: bool = typer.Option(False, help="Only show errors")
):
    """Validate marketing specification"""
    
    # Parse specification
    parser = MarketingSpecParser()
    try:
        spec = parser.parse(filename)
    except ParseError as e:
        console.print(f"[red]Parse Error ({e.code}):[/red] {e.message}")
        console.print(f"[yellow]Fix:[/yellow] {e.fix}")
        raise typer.Exit(1)
    
    # Validate specification
    validator = MarketingSpecValidator()
    result = validator.validate(spec)
    
    # Output results
    if format == "text":
        _output_text(result, quiet, strict, console)
    elif format == "json":
        _output_json(result)
    elif format == "table":
        _output_table(result, console)
    
    # Exit code
    if not result.valid or (strict and result.warnings):
        raise typer.Exit(1)
    raise typer.Exit(0)

def _output_text(result, quiet, strict, console):
    """Output validation results as text"""
    if result.valid and not result.warnings:
        console.print(f"[green]✓ All validation rules passed ({result.rules_checked}/{result.rules_checked})[/green]")
        return
    
    # Show errors
    if result.errors:
        console.print(f"\n[red]❌ Errors ({len(result.errors)}):[/red]")
        for error in result.errors:
            console.print(f"  [{error.code}] {error.message}")
            console.print(f"    Location: {error.entity}.{error.field}")
            console.print(f"    Fix: {error.fix}")
            console.print()
    
    # Show warnings
    if result.warnings and not quiet:
        console.print(f"\n[yellow]⚠️  Warnings ({len(result.warnings)}):[/yellow]")
        for warning in result.warnings:
            console.print(f"  [{warning.code}] {warning.message}")
            console.print(f"    Fix: {warning.fix}")
            console.print()
    
    # Summary
    console.print(f"\n[cyan]Summary:[/cyan] {result.rules_passed}/{result.rules_checked} rules passed")

# Entry point
def main():
    app()
```

**Design Decisions**:
- Use typer for modern CLI with automatic help
- Use rich for colored output, tables, progress bars
- Provide 3 output formats: text (default), json (CI/CD), table (detailed)
- Strict mode treats warnings as errors
- Exit codes: 0 (pass), 1 (fail), 2 (error)

---

### Component 4: Slash Commands

#### Architecture: Slash Command Files

**Purpose**: 13 AI-accessible operations for content generation

**Location**: `templates/custom/commands/marketing.*.md`

**Command List** (13 files):

**Specification Access (7)**:
1. `marketing.project.md` - Get brand identity
2. `marketing.product.md` - Get product features
3. `marketing.campaign.md` - Get campaign goals
4. `marketing.channel.md` - Get channel constraints
5. `marketing.tool.md` - Get tool integration details
6. `marketing.content_template.md` - Get brand guidelines
7. `marketing.milestone.md` - Get milestone events

**Content Generation (4)**:
8. `marketing.generate.post.md` - Generate social media post
9. `marketing.generate.article.md` - Generate blog article
10. `marketing.generate.email.md` - Generate email campaign
11. `marketing.generate.landing_page.md` - Generate landing page copy

**Task Execution (2)**:
12. `marketing.execute.schedule.md` - Schedule content
13. `marketing.execute.publish.md` - Publish content

**Command Template Structure** (Example: marketing.project.md):

```markdown
---
description: Retrieve project brand identity and core values
argument-hint: [project_id]
allowed-tools: FileEdit(specs/*)
model: claude-3-5-sonnet-20241022
---

# /marketing.project

## User Input

\```text
$ARGUMENTS
\```

You **MUST** consider the user input before proceeding (if not empty).

## Purpose

Retrieve project brand identity (name, tagline, brand voice, target audience, value propositions) to guide AI in generating consistent marketing content.

## Domain Specification (EMBEDDED)

**From**: specs/domain/001-marketing-operations-spec/spec.md

### Entity Structure: Project

\```yaml
project:
  name: string (required)
  tagline: string (required, ≤100 chars)
  brand_voice: enum (required) - ["Technical", "Friendly", "Professional", "Casual", "Educational"]
  website: string (required, HTTPS)
  target_audience: array[string] (required, ≥1)
  value_propositions: array[string] (required, ≥1)
  logo_url: string (optional, URL)
  social_handles: object (optional)
\```

### Validation Rules

- VR-P01: name must be unique
- VR-P02: tagline ≤ 100 characters
- VR-P03: website must be HTTPS
- VR-P04: target_audience ≥ 1 item
- VR-P05: brand_voice must match enum
- VR-P06: social_handles must use valid format

### Examples

\```yaml
project:
  name: "MetaSpec"
  tagline: "Meta-Specification Framework for Spec-Driven Development"
  brand_voice: "Technical"
  website: "https://github.com/ACNet-AI/MetaSpec"
  target_audience:
    - "Developers"
    - "AI Engineers"
  value_propositions:
    - "Generate spec-driven toolkits with one command"
\```

## AI Execution Steps

1. **Load Specification**
   - Read: marketing specification file (YAML/JSON)
   - Parse: Extract `project` section

2. **Validate Structure**
   - Check: All required fields present
   - Verify: Field types and constraints

3. **Return Project Entity**
   - Format: YAML or JSON
   - Include: All project fields

4. **Self-Validate**
   - Check: brand_voice is valid enum
   - Check: tagline ≤ 100 chars

## Output Template

\```yaml
project:
  name: "..."
  tagline: "..."
  brand_voice: "Technical"
  website: "https://..."
  target_audience:
    - "..."
  value_propositions:
    - "..."
\```

## Related Commands

- `/marketing.product` - Get product details
- `/marketing.campaign` - Get campaign goals
- `/marketing.generate.post` - Generate content using brand voice
```

**Implementation Priority**:
- **P0 (MVP)**: Specification access commands (7) + generate.post (1) = 8 commands
- **P1 (Important)**: Remaining generation (3) + execution (2) = 5 commands

---

## Implementation Phases

### Phase 1: Core Components (Week 1-2)

**Tasks**:
1. ✅ Create models.py (7 entity models)
2. ✅ Create parser.py (YAML/JSON parsing)
3. ✅ Create exceptions.py (13 error codes)
4. ✅ Unit tests for models and parser

**Deliverables**:
- Functional parser with all 7 entities
- 80%+ test coverage for parser
- All entity models with pydantic validation

### Phase 2: Validation (Week 2-3)

**Tasks**:
1. ✅ Create validator.py (25 validation rules)
2. ✅ Implement all 7 validation methods
3. ✅ Unit tests for each validation rule (25 tests)
4. ✅ Integration tests for validator

**Deliverables**:
- Complete validator with all rules
- One test per rule (25 tests)
- Validation result formatting

### Phase 3: CLI (Week 3-4)

**Tasks**:
1. ✅ Implement `init` command with templates
2. ✅ Implement `validate` command with formatting
3. ✅ Create 3 entity templates (minimal, default, full)
4. ✅ CLI integration tests

**Deliverables**:
- Working CLI with 3 commands (info, init, validate)
- 3 entity templates
- Colored output with rich

### Phase 4: Slash Commands (Week 4-6)

**Tasks**:
1. ✅ Create 8 P0 commands (7 access + 1 generation)
2. ✅ Create 5 P1 commands (3 generation + 2 execution)
3. ✅ Test with AI agent (Claude in Cursor)
4. ✅ Refine based on AI feedback

**Deliverables**:
- 13 slash command files
- Embedded specification knowledge
- Tested with AI agents

### Phase 5: Documentation & Examples (Week 6)

**Tasks**:
1. ✅ Create metaspec-marketing.yaml example
2. ✅ Update README with usage guide
3. ✅ Update AGENTS.md with slash commands
4. ✅ Create test fixtures (valid + invalid specs)

**Deliverables**:
- Complete MetaSpec marketing example
- Updated documentation
- Test fixtures for all validation rules

---

## Success Criteria

### Functional Requirements

- ✅ Parser handles all 7 entity types (Project, Product, Campaign, Channel, Tool, ContentTemplate, Milestone)
- ✅ Validator enforces all 25 validation rules
- ✅ CLI provides init, validate commands with good UX
- ✅ Slash Commands enable AI content generation (13 commands)
- ✅ Error messages are clear with fix suggestions

### Quality Metrics

- ✅ 80%+ code coverage (unit + integration tests)
- ✅ All 25 validation rules have dedicated tests
- ✅ mypy passes with no errors (full type hints)
- ✅ ruff check passes (no linting errors)
- ✅ CLI startup < 500ms, parse < 100ms, validate < 200ms

### User Experience

- ✅ Clear error messages with error codes (MKT-*)
- ✅ Colored output with rich formatting
- ✅ Intuitive CLI commands
- ✅ AI agents can use slash commands effectively

---

## Next Steps

1. ⏭️ **Run `/metaspec.sdd.tasks`** - Break down implementation into concrete tasks
2. ⏭️ **Run `/metaspec.sdd.implement`** - Start implementing components
3. ⏭️ Create test fixtures for each validation rule
4. ⏭️ Implement models.py with all 7 entities

---

**Generated by**: /metaspec.sdd.plan (MetaSpec v0.6.2)  
**Date**: 2025-11-15  
**Toolkit**: marketing-spec-kit  
**Status**: Ready for implementation

