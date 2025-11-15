# Implementation Tasks: marketing-spec-kit

**Toolkit**: marketing-spec-kit  
**Version**: 1.0.0  
**Generated**: 2025-11-15  
**Total Tasks**: 65  
**Estimated Duration**: 6 weeks

---

## Task Overview

This task breakdown follows the 5-phase implementation plan from `plan.md`:

- **Phase 1**: Core Components (Models + Parser) - 15 tasks
- **Phase 2**: Validation - 14 tasks  
- **Phase 3**: CLI Commands - 12 tasks
- **Phase 4**: Slash Commands - 15 tasks
- **Phase 5**: Documentation & Examples - 9 tasks

**Legend**:
- `- [ ]` = Pending task
- `[P]` = Can be parallelized (no dependencies on other pending tasks)
- `[Component]` = Component label (SETUP, MODELS, PARSER, VALIDATOR, CLI, SLASH, DOCS, TESTS)

---

## Phase 1: Core Components (Week 1-2)

**Goal**: Implement entity models and parser for all 7 entities

### Setup Tasks

- [ ] T001 [SETUP] Create project directory structure per plan.md lines 25-52
  - Create: src/marketing_spec_kit/, tests/unit/, tests/integration/, tests/fixtures/, templates/
  - Verify: All directories exist

- [ ] T002 [SETUP] Initialize pyproject.toml with dependencies from plan.md lines 57-77
  - Add: pydantic>=2.0.0, typer>=0.9.0, pyyaml>=6.0, jsonschema>=4.0.0, rich>=13.0.0
  - Add dev dependencies: pytest>=7.4.0, pytest-cov>=4.1.0, mypy>=1.0.0, ruff>=0.1.0
  - Verify: pip install -e . works

- [ ] T003 [SETUP] Create src/marketing_spec_kit/__init__.py with package exports
  - Export: __version__ = "0.1.0"
  - Export: MarketingSpec, Project, Product, Campaign (main entities)
  - Export: MarketingSpecParser, MarketingSpecValidator
  - Verify: from marketing_spec_kit import MarketingSpec works

### Entity Models Tasks

- [ ] T004 [MODELS] Create src/marketing_spec_kit/models.py with base imports
  - Import: pydantic BaseModel, Field, HttpUrl
  - Import: typing List, Dict, Optional
  - Import: enum Enum
  - Verify: File runs without errors

- [ ] T005 [P] [MODELS] Define Enum classes in models.py (plan.md lines 197-214)
  - Create: BrandVoice enum (Technical, Friendly, Professional, Casual, Educational)
  - Create: CampaignGoal enum (awareness, consideration, conversion)
  - Create: ChannelType enum (social_media, email, blog, forum, video, podcast)
  - Verify: All enums have correct values

- [ ] T006 [P] [MODELS] Define Project entity in models.py (plan.md lines 206-223)
  - Fields: name (str), tagline (str, max_length=100), brand_voice (BrandVoice)
  - Fields: website (HttpUrl), target_audience (List[str], min_items=1)
  - Fields: value_propositions (List[str], min_items=1)
  - Optional: logo_url (HttpUrl), social_handles (Dict[str, str])
  - Verify: Pydantic validates correctly

- [ ] T007 [P] [MODELS] Define Product entity in models.py (plan.md lines 236-252)
  - Fields: id (str, pattern), name (str), description (str, max_length=500)
  - Fields: project_id (str), target_audience (List[str]), key_features (List[str])
  - Optional: positioning (str), launch_date (str)
  - Verify: Pattern validation works for id

- [ ] T008 [P] [MODELS] Define Campaign entity in models.py (plan.md lines 265-282)
  - Fields: id, name, goal (CampaignGoal), project_id, target_audience
  - Fields: budget (float, gt=0), start_date, end_date, channels (List[str])
  - Fields: status (str, default="draft")
  - Optional: product_ids (List[str]), kpis (Dict[str, float])
  - Verify: budget > 0 validation works

- [ ] T009 [P] [MODELS] Define Channel entity in models.py (plan.md lines 295-311)
  - Fields: id, name, type (ChannelType), platform, content_types (List[str])
  - Optional: audiences, constraints (Dict), tool_id, config (Dict)
  - Verify: content_types min_items=1 works

- [ ] T010 [P] [MODELS] Define Tool entity in models.py (plan.md lines 324-340)
  - Fields: id, name, type (str), capabilities (List[str]), status (str)
  - Optional: mcp_config (Dict), api_config (Dict), channel_ids (List[str])
  - Verify: Conditional fields work correctly

- [ ] T011 [P] [MODELS] Define ContentTemplate entity in models.py (plan.md lines 353-364)
  - Fields: id, name, type, tone, style_guidelines (List[str]), project_id
  - Optional: constraints (Dict), examples (List[str])
  - Verify: style_guidelines min_items=1 works

- [ ] T012 [P] [MODELS] Define Milestone entity in models.py (plan.md lines 377-389)
  - Fields: id, name, type, date, project_id, status (default="planned")
  - Optional: description, product_ids, campaign_ids
  - Verify: All fields validate

- [ ] T013 [MODELS] Define MarketingSpec root entity in models.py (plan.md lines 392-401)
  - Fields: project (Project), products (List[Product], default_factory)
  - Fields: campaigns, channels, tools, content_templates, milestones (all optional lists)
  - Verify: Can instantiate with just Project

- [ ] T014 [TESTS] Create tests/unit/test_models.py with entity validation tests
  - Test: Each entity with valid data succeeds
  - Test: Each entity with invalid data fails (missing fields, wrong types)
  - Test: Field constraints work (max_length, pattern, gt, min_items)
  - Target: 10 test cases (one per entity + MarketingSpec)

### Parser Tasks

- [ ] T015 [PARSER] Create src/marketing_spec_kit/exceptions.py (plan.md lines 403-423)
  - Create: MarketingSpecError base exception with code, message, fix
  - Create: ParseError (MKT-VAL-001, MKT-VAL-002)
  - Create: ValidationError (MKT-VAL-003, MKT-REF-001, MKT-REF-002)
  - Verify: Exception hierarchy works

- [ ] T016 [PARSER] Create src/marketing_spec_kit/parser.py with MarketingSpecParser class
  - Import: yaml, json, pathlib, models, exceptions
  - Define: MarketingSpecParser class with parse() method
  - Verify: File structure correct

- [ ] T017 [PARSER] Implement parse() method for YAML format (plan.md lines 426-445)
  - Handle: File path, string content, dict input
  - Parse: yaml.safe_load() → pydantic validation
  - Error: Convert yaml.YAMLError to ParseError(MKT-VAL-001)
  - Verify: Can parse valid YAML file

- [ ] T018 [PARSER] Implement parse() method for JSON format (plan.md lines 426-445)
  - Handle: File path, string content
  - Parse: json.load() → pydantic validation
  - Error: Convert json.JSONDecodeError to ParseError(MKT-VAL-001)
  - Verify: Can parse valid JSON file

- [ ] T019 [TESTS] Create tests/unit/test_parser.py with parsing tests
  - Test: Parse valid YAML (minimal, full specs)
  - Test: Parse valid JSON
  - Test: Parse from dict (programmatic)
  - Test: Invalid YAML syntax raises ParseError with fix suggestion
  - Test: Missing required fields raises ParseError
  - Target: 8 test cases (valid + invalid for each format)

---

## Phase 2: Validation (Week 2-3)

**Goal**: Implement all 25 validation rules from domain specification

### Validator Setup

- [ ] T020 [VALIDATOR] Create validator.py with ValidationResult class (plan.md lines 448-456)
  - Fields: valid (bool), errors (List), warnings (List), info (List)
  - Fields: rules_checked (int), rules_passed (int)
  - Verify: Class structure correct

- [ ] T021 [VALIDATOR] Create MarketingSpecValidator class with validate() method
  - Method signature: validate(spec: MarketingSpec) -> ValidationResult
  - Structure: Call _validate_project, _validate_product, etc.
  - Verify: Empty validator runs without errors

### Project Validation (6 rules)

- [ ] T022 [VALIDATOR] Implement _validate_project() for VR-P01 to VR-P06 (plan.md lines 464-478)
  - VR-P01: name unique (workspace-level check)
  - VR-P02: tagline ≤ 100 chars (pydantic handles)
  - VR-P03: website HTTPS (pydantic handles)
  - VR-P04: target_audience ≥ 1 (pydantic handles)
  - VR-P05: brand_voice enum (pydantic handles)
  - VR-P06: social_handles format (custom validation)
  - Verify: All 6 rules checked, warnings generated

### Product Validation (5 rules)

- [ ] T023 [VALIDATOR] Implement _validate_product() for VR-PR01 to VR-PR05 (plan.md lines 481-506)
  - VR-PR01: id unique within products
  - VR-PR02: project_id exists (pydantic handles)
  - VR-PR03: description ≤ 500 (pydantic handles)
  - VR-PR04: key_features 3-5 items (warning)
  - VR-PR05: launch_date validation
  - Verify: Duplicate ID detection works

### Campaign Validation (9 rules)

- [ ] T024 [VALIDATOR] Implement _validate_campaign() Part 1: VR-C01 to VR-C05 (plan.md lines 509-551)
  - VR-C01: id unique
  - VR-C02: project_id exists
  - VR-C03: product_ids all exist (reference validation)
  - VR-C04: budget > 0 (pydantic handles)
  - VR-C05: start_date < end_date (date comparison logic)
  - Verify: Reference validation works

- [ ] T025 [VALIDATOR] Implement _validate_campaign() Part 2: VR-C06 to VR-C09
  - VR-C06: start_date not in past (warning)
  - VR-C07: channels all exist (reference validation)
  - VR-C08: CTR range 0-1 (if kpis provided)
  - VR-C09: ROAS ≥ 3 (warning if kpis provided)
  - Verify: KPI validation works

### Channel Validation (6 rules)

- [ ] T026 [VALIDATOR] Implement _validate_channel() for VR-CH01 to VR-CH06
  - VR-CH01: id unique
  - VR-CH02: type valid enum
  - VR-CH03: platform lowercase no spaces
  - VR-CH04: tool_id exists (if provided)
  - VR-CH05: content_types ≥ 1
  - VR-CH06: max_text_length > 0 (if in constraints)
  - Verify: All 6 rules work

### Tool Validation (6 rules)

- [ ] T027 [VALIDATOR] Implement _validate_tool() for VR-T01 to VR-T06
  - VR-T01: id unique
  - VR-T02: mcp_config required if type=mcp
  - VR-T03: api_config required if type=rest_api
  - VR-T04: capabilities ≥ 1
  - VR-T05: api_config.base_url HTTPS (if provided)
  - VR-T06: channel_ids all exist (if provided)
  - Verify: Conditional validation works

### ContentTemplate & Milestone Validation

- [ ] T028 [VALIDATOR] Implement _validate_content_template() for VR-CT01 to VR-CT05
  - VR-CT01: id unique
  - VR-CT02: project_id exists
  - VR-CT03: style_guidelines ≥ 1
  - VR-CT04: min_length < max_length (if both in constraints)
  - VR-CT05: tone aligns with project brand_voice (warning)
  - Verify: Cross-entity validation works (project reference)

- [ ] T029 [VALIDATOR] Implement _validate_milestone() for VR-M01 to VR-M05
  - VR-M01: id unique
  - VR-M02: project_id exists
  - VR-M03: product_ids all exist (if provided)
  - VR-M04: campaign_ids all exist (if provided)
  - VR-M05: date ≤ 1 year in future (warning)
  - Verify: Multiple reference validation works

### Validator Testing

- [ ] T030 [TESTS] Create tests/unit/test_validator.py with rule-specific tests
  - Test: One test per validation rule (25 tests minimum)
  - Test: Multiple errors collected (don't stop at first)
  - Test: Warning vs error distinction
  - Test: Error message format (code, message, entity, field, fix)
  - Target: 30 test cases (25 rules + 5 additional scenarios)

- [ ] T031 [TESTS] Create tests/fixtures/valid_specs/ with valid specification examples
  - Create: minimal.yaml (Project only)
  - Create: full.yaml (all entities with all optional fields)
  - Create: metaspec_example.yaml (real MetaSpec marketing spec)
  - Verify: Parser + Validator accept all files

- [ ] T032 [TESTS] Create tests/fixtures/invalid_specs/ with one file per validation rule
  - Create: 25 YAML files testing each VR-* rule
  - Examples: vr_p02_long_tagline.yaml, vr_c04_zero_budget.yaml
  - Verify: Validator catches each specific error

- [ ] T033 [TESTS] Create tests/integration/test_end_to_end.py with full workflow tests
  - Test: Parse valid spec → Validate → Success
  - Test: Parse invalid spec → Validate → Errors with fixes
  - Test: MetaSpec example → Validate → Pass all rules
  - Target: 5 integration tests

---

## Phase 3: CLI Commands (Week 3-4)

**Goal**: Implement user-facing CLI with init and validate commands

### CLI Setup

- [ ] T034 [CLI] Update src/marketing_spec_kit/cli.py with typer and rich imports
  - Import: typer, rich.console, rich.table, pathlib
  - Import: parser, validator, exceptions
  - Create: app = typer.Typer() with metadata
  - Verify: CLI loads without errors

- [ ] T035 [CLI] Implement info command (already exists, verify)
  - Check: Current implementation shows toolkit info
  - Update: Add version, domain, available commands
  - Verify: marketing_spec_kit info works

### Init Command Implementation

- [ ] T036 [CLI] Create templates/entity_templates/minimal.yaml
  - Content: Project only with placeholder values
  - Fields: All required fields with "TODO: Fill this"
  - Comments: Inline guidance for each field
  - Verify: Valid YAML structure

- [ ] T037 [CLI] Create templates/entity_templates/default.yaml
  - Content: Project + 2 Products + 1 Campaign + 2 Channels
  - Fields: Complete example with real values
  - Comments: Explain each section
  - Verify: Parser accepts, Validator passes

- [ ] T038 [CLI] Create templates/entity_templates/full.yaml
  - Content: All 7 entities with all optional fields
  - Fields: Comprehensive example (MetaSpec-like)
  - Comments: Document all features
  - Verify: Parser accepts, Validator passes

- [ ] T039 [CLI] Implement init command (plan.md lines 654-674)
  - Arguments: filename (required)
  - Options: --template (minimal/default/full), --format (yaml/json), --overwrite
  - Logic: Check file exists, load template, copy to output
  - Output: Success message + next steps
  - Verify: marketing_spec_kit init test.yaml works

### Validate Command Implementation

- [ ] T040 [CLI] Implement validate command Part 1: Core logic (plan.md lines 677-707)
  - Arguments: filename (required)
  - Options: --strict, --format (text/json/table), --quiet
  - Logic: Parse → Validate → Format results
  - Error handling: ParseError, file not found
  - Verify: Basic validation works

- [ ] T041 [CLI] Implement _output_text() helper for text format
  - Show: ✅ success or ❌ errors with counts
  - Format: Error code, message, location, fix
  - Format: Warning messages (unless --quiet)
  - Format: Summary (X/25 rules passed)
  - Verify: Rich formatting works (colors, bold)

- [ ] T042 [CLI] Implement _output_json() helper for JSON format
  - Format: {"valid": bool, "errors": [...], "warnings": [...]}
  - Include: rules_checked, rules_passed
  - Verify: Valid JSON output for CI/CD

- [ ] T043 [CLI] Implement _output_table() helper for table format
  - Create: Rich Table with rule-by-rule status
  - Columns: Rule ID, Status, Message
  - Color: Green (pass), Yellow (warning), Red (error)
  - Verify: Table displays correctly

### CLI Testing

- [ ] T044 [TESTS] Create tests/unit/test_cli.py with command tests
  - Test: info command output
  - Test: init with each template (minimal, default, full)
  - Test: init with --overwrite flag
  - Test: validate with valid spec (exit code 0)
  - Test: validate with invalid spec (exit code 1)
  - Test: validate --strict mode (warnings as errors)
  - Target: 10 test cases

- [ ] T045 [TESTS] Create tests/integration/test_cli_integration.py
  - Test: init → edit → validate workflow
  - Test: validate all output formats (text, json, table)
  - Test: Error handling (file not found, parse errors)
  - Target: 5 integration tests

---

## Phase 4: Slash Commands (Week 4-6)

**Goal**: Implement 13 AI agent operations for content generation

### Command Template Creation

- [ ] T046 [SLASH] Create templates/custom/commands/ directory structure
  - Create directory: templates/custom/commands/
  - Verify: Directory exists

### Specification Access Commands (P0: 7 commands)

- [ ] T047 [P] [SLASH] Create marketing.project.md (plan.md lines 825-857)
  - Frontmatter: description, argument-hint, allowed-tools, model
  - Purpose: Retrieve project brand identity
  - Embedded Spec: Project entity schema, VR-P01 to VR-P06, examples
  - Execution Steps: Load spec → Extract project → Validate → Return
  - Output Template: YAML format
  - Verify: AI can read and understand command

- [ ] T048 [P] [SLASH] Create marketing.product.md
  - Purpose: Retrieve product features and positioning
  - Embedded Spec: Product entity schema, VR-PR01 to VR-PR05, examples
  - Execution Steps: Load spec → Find product by ID → Return
  - Output Template: YAML format
  - Verify: Command complete

- [ ] T049 [P] [SLASH] Create marketing.campaign.md
  - Purpose: Retrieve campaign goals, budget, timeline
  - Embedded Spec: Campaign entity schema, VR-C01 to VR-C09, examples
  - Execution Steps: Load spec → Find campaign by ID → Return
  - Output Template: YAML format with KPIs
  - Verify: Command complete

- [ ] T050 [P] [SLASH] Create marketing.channel.md
  - Purpose: Retrieve channel platform details and constraints
  - Embedded Spec: Channel entity schema, constraints structure, examples
  - Execution Steps: Load spec → Find channel → Return constraints
  - Output Template: YAML with content_types and constraints
  - Verify: Command complete

- [ ] T051 [P] [SLASH] Create marketing.tool.md
  - Purpose: Retrieve tool integration details (MCP/API config)
  - Embedded Spec: Tool entity schema, mcp_config, api_config structures
  - Execution Steps: Load spec → Find tool → Return config
  - Output Template: YAML with capabilities and config
  - Verify: Command complete

- [ ] T052 [P] [SLASH] Create marketing.content_template.md
  - Purpose: Retrieve brand guidelines and style rules
  - Embedded Spec: ContentTemplate schema, style_guidelines, constraints
  - Execution Steps: Load spec → Find template → Return guidelines
  - Output Template: YAML with tone and guidelines
  - Verify: Command complete

- [ ] T053 [P] [SLASH] Create marketing.milestone.md
  - Purpose: Retrieve milestone event details
  - Embedded Spec: Milestone schema, date format, examples
  - Execution Steps: Load spec → Find milestone → Return details
  - Output Template: YAML with date and associated campaigns
  - Verify: Command complete

### Content Generation Commands (P0: 1 command, P1: 3 commands)

- [ ] T054 [SLASH] Create marketing.generate.post.md (P0 - MVP critical)
  - Purpose: Generate platform-specific social media post
  - Embedded Spec: Channel constraints (280 chars for Twitter), brand voice
  - Inputs: campaign_id, channel_id, tone (optional), hashtags (optional)
  - Output: text, hashtags, character_count, estimated_reach
  - Execution Steps: Get campaign → Get channel → Get project → Generate
  - Verify: Command complete with examples

- [ ] T055 [P] [SLASH] Create marketing.generate.article.md (P1)
  - Purpose: Generate long-form blog article
  - Embedded Spec: ContentTemplate structure, length constraints
  - Inputs: campaign_id, template_id, product_id (optional), length
  - Output: title, subtitle, body (Markdown), word_count, SEO keywords
  - Verify: Command complete

- [ ] T056 [P] [SLASH] Create marketing.generate.email.md (P1)
  - Purpose: Generate email campaign content
  - Embedded Spec: Email template structure, subject line best practices
  - Inputs: campaign_id, template_id, segment (optional)
  - Output: subject, preview_text, body (HTML), plain_text, CTA
  - Verify: Command complete

- [ ] T057 [P] [SLASH] Create marketing.generate.landing_page.md (P1)
  - Purpose: Generate landing page copy
  - Embedded Spec: Landing page structure, conversion optimization
  - Inputs: campaign_id, product_id, template_id (optional)
  - Output: hero_headline, hero_subheadline, features, testimonials, CTA
  - Verify: Command complete

### Task Execution Commands (P1: 2 commands)

- [ ] T058 [P] [SLASH] Create marketing.execute.schedule.md (P1)
  - Purpose: Schedule content for future publication
  - Embedded Spec: Tool capabilities, scheduling requirements
  - Inputs: content (object), channel_id, tool_id, scheduled_time
  - Output: scheduled_id, status, publish_time, tool_used
  - Warning: NOT idempotent (side effects)
  - Verify: Command complete with error codes

- [ ] T059 [P] [SLASH] Create marketing.execute.publish.md (P1)
  - Purpose: Publish content immediately
  - Embedded Spec: Tool capabilities, publishing requirements
  - Inputs: content (object), channel_id, tool_id
  - Output: published_id, status, publish_time, url
  - Warning: NOT idempotent (side effects)
  - Verify: Command complete with error codes

### Slash Command Testing

- [ ] T060 [TESTS] Test slash commands with AI agent (manual test)
  - Test: Load each command in AI chat (Cursor/Claude)
  - Test: AI can understand embedded specification
  - Test: AI generates correct output format
  - Verify: All 13 commands work with AI
  - Document: Any command improvements needed

---

## Phase 5: Documentation & Examples (Week 6)

**Goal**: Complete documentation and create real-world examples

### Example Creation

- [ ] T061 [DOCS] Create examples/metaspec-marketing.yaml
  - Content: Complete MetaSpec marketing specification
  - Entities: MetaSpec project, 3 products (Speckit Generator, SDS Commands, Awesome Spec Kits)
  - Campaigns: v0.6.0 launch campaign
  - Channels: Twitter, Reddit, Dev.to
  - Tools: MCP tools (twitter-mcp, github-mcp)
  - Templates: Technical blog post template
  - Milestones: v0.6.0 release
  - Verify: Parser accepts, Validator passes (25/25 rules)

### Documentation Updates

- [ ] T062 [DOCS] Update README.md with comprehensive usage guide
  - Add: Installation instructions (pip install)
  - Add: Quick start guide (init → validate workflow)
  - Add: CLI command reference with examples
  - Add: Entity descriptions with field tables
  - Add: Validation rule reference
  - Add: Troubleshooting section
  - Verify: Documentation complete and clear

- [ ] T063 [DOCS] Update AGENTS.md with slash commands documentation
  - Add: All 13 slash commands with descriptions
  - Add: Usage examples for each command
  - Add: AI agent workflow examples
  - Add: Content generation examples
  - Remove: Generic template content
  - Verify: AI-friendly documentation complete

- [ ] T064 [DOCS] Update CHANGELOG.md for v0.1.0 release
  - Add: Initial release notes
  - Add: Features list (parser, validator, CLI, slash commands)
  - Add: 7 entities, 25 validation rules, 13 AI operations
  - Add: Examples and templates
  - Verify: Changelog follows Keep a Changelog format

### Final Quality Checks

- [ ] T065 [TESTS] Run full test suite and verify 80%+ coverage
  - Run: pytest --cov=marketing_spec_kit --cov-report=term
  - Check: All tests pass
  - Check: Coverage ≥ 80%
  - Run: mypy src/ (no type errors)
  - Run: ruff check src/ (no linting errors)
  - Verify: All quality gates pass

---

## Task Dependencies

### Critical Path (Cannot Parallelize)

```
T001 (Setup) → T002 (pyproject) → T003 (__init__)
  ↓
T004 (models base) → T005 (enums) → T006-T012 (entities) → T013 (MarketingSpec)
  ↓
T015 (exceptions) → T016 (parser base) → T017-T018 (parse methods)
  ↓
T020-T021 (validator setup) → T022-T029 (validation rules)
  ↓
T034-T035 (CLI setup) → T036-T038 (templates) → T039-T043 (commands)
  ↓
T046 (slash dir) → T047-T059 (slash commands)
  ↓
T061-T064 (documentation) → T065 (final checks)
```

### Parallelizable Tasks (Can Do Simultaneously)

- **Entity Models**: T006-T012 (7 entities can be coded in parallel)
- **Validation Methods**: T022-T029 (8 validation methods after setup)
- **Slash Commands**: T047-T053 (7 access commands), T055-T059 (5 generation/execution commands)
- **Templates**: T036-T038 (3 template files)
- **Documentation**: T062-T064 (3 doc files)

---

## Milestone Checklist

### Milestone 1: Core Parser (Week 1-2)
- [ ] All models defined (T004-T013) ✓
- [ ] Parser works for YAML/JSON (T015-T019) ✓
- [ ] Model tests pass (T014) ✓
- [ ] Parser tests pass (T019) ✓

### Milestone 2: Complete Validator (Week 2-3)
- [ ] All 25 validation rules implemented (T020-T029) ✓
- [ ] Validator tests pass (T030) ✓
- [ ] Test fixtures created (T031-T032) ✓
- [ ] Integration tests pass (T033) ✓

### Milestone 3: Working CLI (Week 3-4)
- [ ] Init command works (T034-T039) ✓
- [ ] Validate command works (T040-T043) ✓
- [ ] CLI tests pass (T044-T045) ✓

### Milestone 4: AI Operations (Week 4-6)
- [ ] 8 P0 slash commands created (T047-T054) ✓
- [ ] 5 P1 slash commands created (T055-T059) ✓
- [ ] Commands tested with AI (T060) ✓

### Milestone 5: Production Ready (Week 6)
- [ ] Documentation complete (T061-T064) ✓
- [ ] All tests pass with 80%+ coverage (T065) ✓
- [ ] Ready for v0.1.0 release ✓

---

## Estimated Effort

| Phase | Tasks | Estimated Time | Complexity |
|-------|-------|----------------|------------|
| Phase 1: Core | 19 | 12-16 hours | Medium |
| Phase 2: Validation | 14 | 16-20 hours | High |
| Phase 3: CLI | 12 | 10-14 hours | Medium |
| Phase 4: Slash Commands | 15 | 14-18 hours | Medium |
| Phase 5: Documentation | 9 | 6-8 hours | Low |
| **Total** | **69** | **58-76 hours** | **6 weeks** |

**Assumptions**:
- Working 10-15 hours per week
- Parallel execution where possible
- Testing integrated throughout (not separate phase)

---

## Success Criteria (From spec.md)

**Functional**:
- ✅ Parser handles all 7 entity types
- ✅ Validator enforces all 25 validation rules
- ✅ CLI provides init, validate commands
- ✅ 13 slash commands enable AI content generation
- ✅ Error messages clear with fix suggestions

**Quality**:
- ✅ 80%+ code coverage
- ✅ All validation rules have dedicated tests
- ✅ mypy passes with no errors
- ✅ ruff check passes
- ✅ Performance: parse <100ms, validate <200ms, startup <500ms

**User Experience**:
- ✅ Clear error messages with MKT-* codes
- ✅ Colored output with rich formatting
- ✅ Intuitive CLI commands
- ✅ AI agents can use slash commands effectively

---

**Generated by**: /metaspec.sdd.tasks (MetaSpec v0.6.2)  
**Based on**: spec.md (1127 lines) + plan.md (1130 lines)  
**Ready to**: Begin implementation with `/metaspec.sdd.implement`

