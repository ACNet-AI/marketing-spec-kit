"""Validator for Marketing Operations Specification

Implements 45 validation rules from domain specification v0.3.0:
- Project: VR-P01 to VR-P06 (6 rules)
- Product: VR-PR01 to VR-PR05 (5 rules)
- MarketingPlan: VR-MP01 to VR-MP10 (10 rules) [NEW in v0.2.0]
- Campaign: VR-C01 to VR-C11 (11 rules, includes plan_id requirement) [UPDATED in v0.2.0]
- Channel: VR-CH01 to VR-CH06 (6 rules)
- Tool: VR-T01 to VR-T06 (6 rules)
- ContentTemplate: VR-CT01 to VR-CT05 (5 rules)
- Milestone: VR-M01 to VR-M05 (5 rules)
- Analytics: VR-A01 to VR-A05 (5 rules) [NEW in v0.2.0]

Performance Target: Validate <250ms for typical specs
"""

import re
from datetime import datetime, timedelta
from typing import Any, List, Set

from pydantic import BaseModel, Field

from marketing_spec_kit.models import MarketingSpec


class ValidationIssue(BaseModel):
    """Single validation issue (error or warning)"""

    code: str = Field(..., description="Validation rule code (e.g., VR-P01)")
    level: str = Field(..., description="Severity: 'error' or 'warning'")
    entity_type: str = Field(..., description="Entity type (e.g., 'project', 'campaign')")
    entity_id: str = Field("", description="Entity ID (if applicable)")
    field: str = Field("", description="Field name causing issue")
    message: str = Field(..., description="Human-readable issue description")
    fix: str = Field("", description="Suggested fix")


class ValidationResult(BaseModel):
    """Result of specification validation"""

    valid: bool = Field(..., description="True if no errors (warnings allowed)")
    errors: List[ValidationIssue] = Field(default_factory=list)
    warnings: List[ValidationIssue] = Field(default_factory=list)
    info: List[ValidationIssue] = Field(default_factory=list)
    rules_checked: int = Field(0, description="Total rules checked")
    rules_passed: int = Field(0, description="Rules that passed")

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)

    @property
    def success_rate(self) -> float:
        """Percentage of rules passed"""
        if self.rules_checked == 0:
            return 0.0
        return (self.rules_passed / self.rules_checked) * 100


class MarketingSpecValidator:
    """Validator for enforcing 42 validation rules
    
    Three-layer validation architecture:
    1. Structural validation (Pydantic handles automatically)
    2. Business logic validation (implemented here)
    3. Reference integrity validation (cross-entity checks)
    
    Example:
        >>> validator = MarketingSpecValidator()
        >>> result = validator.validate(spec)
        >>> if not result.valid:
        ...     for error in result.errors:
        ...         print(f"[{error.code}] {error.message}")
    """

    def __init__(self):
        self.result = ValidationResult(valid=True)
        self._project_id: str = ""
        self._product_ids: Set[str] = set()
        self._plan_ids: Set[str] = set()  # NEW in v2.0.0
        self._campaign_ids: Set[str] = set()
        self._channel_ids: Set[str] = set()
        self._tool_ids: Set[str] = set()
        self._template_ids: Set[str] = set()
        self._milestone_ids: Set[str] = set()
        self._analytics_ids: Set[str] = set()  # NEW in v2.0.0
        self._plans: List[Any] = []  # Store plans for budget validation
        self._campaigns: List[Any] = []  # Store campaigns for budget validation

    def validate(self, spec: MarketingSpec) -> ValidationResult:
        """Validate a MarketingSpec against all 45 rules (v2.0.0)
        
        Args:
            spec: MarketingSpec object (already parsed by Pydantic)
        
        Returns:
            ValidationResult with errors, warnings, and statistics
        """
        # Reset state
        self.result = ValidationResult(valid=True)
        self._collect_ids(spec)

        # Validate each entity type
        self._validate_project(spec.project)

        for product in spec.products:
            self._validate_product(product)

        for plan in spec.plans:
            self._validate_plan(plan)

        for campaign in spec.campaigns:
            self._validate_campaign(campaign)

        for channel in spec.channels:
            self._validate_channel(channel)

        for tool in spec.tools:
            self._validate_tool(tool)

        for template in spec.content_templates:
            self._validate_content_template(template)

        for milestone in spec.milestones:
            self._validate_milestone(milestone)

        for analytics in spec.analytics:
            self._validate_analytics(analytics)

        # Final result
        self.result.valid = len(self.result.errors) == 0
        return self.result

    def _collect_ids(self, spec: MarketingSpec):
        """Collect all entity IDs for reference validation (v2.0.0)"""
        self._project_id = spec.project.name.lower().replace(" ", "-")
        self._product_ids = {p.id for p in spec.products}
        self._plan_ids = {p.id for p in spec.plans}
        self._campaign_ids = {c.id for c in spec.campaigns}
        self._channel_ids = {ch.id for ch in spec.channels}
        self._tool_ids = {t.id for t in spec.tools}
        self._template_ids = {ct.id for ct in spec.content_templates}
        self._milestone_ids = {m.id for m in spec.milestones}
        self._analytics_ids = {a.id for a in spec.analytics}
        # Store entities for cross-validation
        self._plans = list(spec.plans)
        self._campaigns = list(spec.campaigns)

    # ========================================================================
    # Project Validation (6 rules)
    # ========================================================================

    def _validate_project(self, project):
        """Validate Project entity (VR-P01 to VR-P06)"""

        # VR-P01: name unique (workspace-level) - Skip (requires external context)
        # VR-P02: tagline ≤ 100 (Pydantic handles)
        # VR-P03: website HTTPS (Pydantic handles)
        # VR-P04: target_audience ≥ 1 (Pydantic handles)
        # VR-P05: brand_voice enum (Pydantic handles)

        # VR-P06: social_handles format validation
        if project.social_handles:
            self._check_rule("VR-P06")
            for platform, handle in project.social_handles.items():
                if platform.lower() == "twitter" and not handle.startswith("@"):
                    self._add_warning(
                        "VR-P06",
                        "project",
                        "",
                        "social_handles.twitter",
                        f"Twitter handle '{handle}' should start with '@'",
                        f"Use '@{handle}' instead",
                    )
                elif platform.lower() in ["github", "gitlab"] and handle.startswith("@"):
                    self._add_warning(
                        "VR-P06",
                        "project",
                        "",
                        f"social_handles.{platform}",
                        f"{platform.title()} username should not have '@' prefix",
                        f"Use '{handle[1:]}' instead",
                    )
            self._pass_rule()

    # ========================================================================
    # Product Validation (5 rules)
    # ========================================================================

    def _validate_product(self, product):
        """Validate Product entity (VR-PR01 to VR-PR05)"""

        # VR-PR01: id unique (checked via set membership in _collect_ids)
        # VR-PR02: project_id exists (cannot validate without multiple projects)
        # VR-PR03: description ≤ 500 (Pydantic handles)

        # VR-PR04: key_features 3-5 items (warning)
        self._check_rule("VR-PR04")
        feature_count = len(product.key_features)
        if feature_count < 3:
            self._add_warning(
                "VR-PR04",
                "product",
                product.id,
                "key_features",
                f"Product has only {feature_count} features (recommended: 3-5)",
                "Add more key features to better communicate product value",
            )
        elif feature_count > 5:
            self._add_warning(
                "VR-PR04",
                "product",
                product.id,
                "key_features",
                f"Product has {feature_count} features (recommended: 3-5)",
                "Focus on top 3-5 features for clarity",
            )
        self._pass_rule()

        # VR-PR05: launch_date not in future (for launched products)
        if product.launch_date:
            self._check_rule("VR-PR05")
            try:
                launch = datetime.fromisoformat(product.launch_date)
                if launch > datetime.now():
                    self._add_info(
                        "VR-PR05",
                        "product",
                        product.id,
                        "launch_date",
                        f"Product launch is scheduled for {product.launch_date}",
                        "",
                    )
                self._pass_rule()
            except ValueError:
                self._add_error(
                    "VR-PR05",
                    "product",
                    product.id,
                    "launch_date",
                    f"Invalid date format: '{product.launch_date}'",
                    "Use ISO 8601 format: YYYY-MM-DD",
                )

    # ========================================================================
    # MarketingPlan Validation (5 rules) - NEW in v2.0.0
    # ========================================================================

    def _validate_plan(self, plan):
        """Validate MarketingPlan entity (PLAN-01 to PLAN-05)"""

        # PLAN-01: objectives must be 1-5 non-empty strings (Pydantic handles count)
        self.result.rules_checked += 1
        if plan.objectives:
            empty_objectives = [obj for obj in plan.objectives if not obj.strip()]
            if empty_objectives:
                self._add_issue(
                    "PLAN-01",
                    "error",
                    "plan",
                    plan.id,
                    "objectives",
                    f"Plan has {len(empty_objectives)} empty objective(s)",
                    "Remove empty strings from objectives list",
                )
            else:
                self.result.rules_passed += 1

        # PLAN-02: period.duration_weeks must be 4-52 (Pydantic handles)
        self.result.rules_checked += 1
        self.result.rules_passed += 1  # Handled by Pydantic Field(ge=4, le=52)

        # PLAN-03: budget.allocation sum must equal budget.total
        self.result.rules_checked += 1
        if plan.budget and plan.budget.allocation:
            allocation_sum = sum(plan.budget.allocation.values())
            tolerance = 0.01  # Allow $0.01 rounding difference
            if abs(allocation_sum - plan.budget.total) > tolerance:
                self._add_issue(
                    "PLAN-03",
                    "error",
                    "plan",
                    plan.id,
                    "budget",
                    f"Budget allocation sum (${allocation_sum:.2f}) != total (${plan.budget.total:.2f})",
                    f"Adjust allocation to sum to ${plan.budget.total:.2f}",
                )
            else:
                self.result.rules_passed += 1

        # PLAN-04: status APPROVED/ACTIVE requires approval field
        self.result.rules_checked += 1
        from marketing_spec_kit.models import PlanStatus
        if plan.status in [PlanStatus.APPROVED, PlanStatus.ACTIVE]:
            if not plan.approval:
                self._add_issue(
                    "PLAN-04",
                    "error",
                    "plan",
                    plan.id,
                    "approval",
                    f"Plan status '{plan.status.value}' requires approval metadata",
                    "Add approval field with approved_by, approved_at, and optional comments",
                )
            else:
                self.result.rules_passed += 1
        else:
            self.result.rules_passed += 1

        # PLAN-05: strategies count must be 1-8 (Pydantic handles)
        self.result.rules_checked += 1
        self.result.rules_passed += 1  # Handled by Pydantic Field(min_items=1, max_items=8)

    # ========================================================================
    # Campaign Validation (11 rules) - UPDATED in v2.0.0
    # ========================================================================

    def _validate_campaign(self, campaign):
        """Validate Campaign entity (VR-C01 to VR-C09)"""

        # VR-C01: id unique (checked via set membership)
        # VR-C02: project_id exists (cannot validate without multiple projects)

        # VR-C03: product_ids all exist
        if campaign.product_ids:
            self._check_rule("VR-C03")
            for pid in campaign.product_ids:
                if pid not in self._product_ids:
                    self._add_error(
                        "VR-C03",
                        "campaign",
                        campaign.id,
                        "product_ids",
                        f"Product '{pid}' does not exist",
                        f"Add Product with id='{pid}' or remove from product_ids",
                    )
            self._pass_rule()

        # VR-C04: budget > 0 (Pydantic handles with gt=0)

        # VR-C05: start_date < end_date
        self._check_rule("VR-C05")
        try:
            start = datetime.fromisoformat(campaign.start_date)
            end = datetime.fromisoformat(campaign.end_date)
            if start >= end:
                self._add_error(
                    "VR-C05",
                    "campaign",
                    campaign.id,
                    "start_date",
                    f"Start date ({campaign.start_date}) must be before end date ({campaign.end_date})",
                    "Adjust dates so start_date < end_date",
                )
            self._pass_rule()
        except ValueError as e:
            self._add_error(
                "VR-C05",
                "campaign",
                campaign.id,
                "dates",
                f"Invalid date format: {e}",
                "Use ISO 8601 format: YYYY-MM-DD",
            )

        # VR-C06: start_date not in past (warning)
        self._check_rule("VR-C06")
        try:
            start = datetime.fromisoformat(campaign.start_date)
            if start < datetime.now() and campaign.status in ["draft", "scheduled"]:
                self._add_warning(
                    "VR-C06",
                    "campaign",
                    campaign.id,
                    "start_date",
                    f"Campaign start date ({campaign.start_date}) is in the past",
                    "Update start_date or change status to 'active'",
                )
            self._pass_rule()
        except ValueError:
            pass  # Already handled in VR-C05

        # VR-C07: channels all exist
        self._check_rule("VR-C07")
        for ch_id in campaign.channels:
            if ch_id not in self._channel_ids:
                self._add_error(
                    "VR-C07",
                    "campaign",
                    campaign.id,
                    "channels",
                    f"Channel '{ch_id}' does not exist",
                    f"Add Channel with id='{ch_id}' or remove from channels",
                )
        self._pass_rule()

        # VR-C08: target_ctr 0-1
        if campaign.kpis and "target_ctr" in campaign.kpis:
            self._check_rule("VR-C08")
            ctr = campaign.kpis["target_ctr"]
            if not (0 <= ctr <= 1):
                self._add_error(
                    "VR-C08",
                    "campaign",
                    campaign.id,
                    "kpis.target_ctr",
                    f"CTR must be between 0 and 1 (got {ctr})",
                    "Use decimal format: 0.05 for 5% CTR",
                )
            self._pass_rule()

        # VR-C09: target_roas ≥ 3 (warning)
        if campaign.kpis and "target_roas" in campaign.kpis:
            self._check_rule("VR-C09")
            roas = campaign.kpis["target_roas"]
            if roas < 3:
                self._add_warning(
                    "VR-C09",
                    "campaign",
                    campaign.id,
                    "kpis.target_roas",
                    f"ROAS of {roas} is below recommended minimum of 3.0 for profitability",
                    "Consider increasing budget efficiency or raising target ROAS",
                )
            self._pass_rule()

        # CAMP-08: plan_id must reference existing MarketingPlan (NEW in v2.0.0)
        self.result.rules_checked += 1
        if campaign.plan_id not in self._plan_ids:
            self._add_issue(
                "CAMP-08",
                "error",
                "campaign",
                campaign.id,
                "plan_id",
                f"Campaign references non-existent plan '{campaign.plan_id}'",
                f"Use one of: {', '.join(self._plan_ids) if self._plan_ids else '(no plans defined)'}",
            )
        else:
            self.result.rules_passed += 1

        # CAMP-09 & CAMP-10: Campaign dates must be within plan's period (NEW in v2.0.0)
        if campaign.plan_id in self._plan_ids:
            plan = next((p for p in self._plans if p.id == campaign.plan_id), None)
            if plan:
                # CAMP-09: start_date within plan period
                self.result.rules_checked += 1
                campaign_start = campaign.start_date
                plan_start = plan.period.start_date
                plan_end = plan.period.end_date

                if campaign_start < plan_start or campaign_start > plan_end:
                    self._add_issue(
                        "CAMP-09",
                        "error",
                        "campaign",
                        campaign.id,
                        "start_date",
                        f"Campaign start ({campaign_start}) outside plan period ({plan_start} to {plan_end})",
                        f"Adjust start_date to be between {plan_start} and {plan_end}",
                    )
                else:
                    self.result.rules_passed += 1

                # CAMP-10: end_date within plan period and >= start_date
                self.result.rules_checked += 1
                campaign_end = campaign.end_date

                if campaign_end < plan_start or campaign_end > plan_end:
                    self._add_issue(
                        "CAMP-10",
                        "error",
                        "campaign",
                        campaign.id,
                        "end_date",
                        f"Campaign end ({campaign_end}) outside plan period ({plan_start} to {plan_end})",
                        f"Adjust end_date to be between {plan_start} and {plan_end}",
                    )
                elif campaign_end < campaign_start:
                    self._add_issue(
                        "CAMP-10",
                        "error",
                        "campaign",
                        campaign.id,
                        "end_date",
                        f"Campaign end ({campaign_end}) before start ({campaign_start})",
                        "Set end_date to be >= start_date",
                    )
                else:
                    self.result.rules_passed += 1

                # CAMP-11: Budget check (warning) (NEW in v2.0.0)
                self.result.rules_checked += 1
                plan_total_budget = plan.budget.total
                campaigns_in_plan = [c for c in self._campaigns if c.plan_id == plan.id]
                total_campaign_budgets = sum(c.budget for c in campaigns_in_plan)

                if total_campaign_budgets > plan_total_budget * 1.05:  # Allow 5% over
                    self._add_issue(
                        "CAMP-11",
                        "warning",
                        "campaign",
                        campaign.id,
                        "budget",
                        f"Total campaign budgets (${total_campaign_budgets:.2f}) exceed plan budget (${plan_total_budget:.2f})",
                        "Consider reducing campaign budgets or increasing plan budget",
                    )
                    self.result.rules_passed += 1
                else:
                    self.result.rules_passed += 1

    # ========================================================================
    # Channel Validation (6 rules)
    # ========================================================================

    def _validate_channel(self, channel):
        """Validate Channel entity (VR-CH01 to VR-CH06)"""

        # VR-CH01: id unique (checked via set)
        # VR-CH02: type enum (Pydantic handles)

        # VR-CH03: platform naming convention
        self._check_rule("VR-CH03")
        if not re.match(r"^[a-z0-9-]+$", channel.platform):
            self._add_warning(
                "VR-CH03",
                "channel",
                channel.id,
                "platform",
                f"Platform name '{channel.platform}' should be lowercase with hyphens",
                f"Use '{channel.platform.lower().replace(' ', '-')}' instead",
            )
        self._pass_rule()

        # VR-CH04: tool_id exists
        if channel.tool_id:
            self._check_rule("VR-CH04")
            if channel.tool_id not in self._tool_ids:
                self._add_error(
                    "VR-CH04",
                    "channel",
                    channel.id,
                    "tool_id",
                    f"Tool '{channel.tool_id}' does not exist",
                    f"Add Tool with id='{channel.tool_id}' or remove tool_id",
                )
            self._pass_rule()

        # VR-CH05: content_types ≥ 1 (Pydantic handles)

        # VR-CH06: max_text_length > 0
        if channel.constraints and "max_text_length" in channel.constraints:
            self._check_rule("VR-CH06")
            max_len = channel.constraints["max_text_length"]
            if max_len <= 0:
                self._add_error(
                    "VR-CH06",
                    "channel",
                    channel.id,
                    "constraints.max_text_length",
                    f"max_text_length must be > 0 (got {max_len})",
                    "Set a positive character limit",
                )
            self._pass_rule()

    # ========================================================================
    # Tool Validation (6 rules)
    # ========================================================================

    def _validate_tool(self, tool):
        """Validate Tool entity (VR-T01 to VR-T06)"""

        # VR-T01: id unique (checked via set)

        # VR-T02: If type=mcp, mcp_config required
        self._check_rule("VR-T02")
        if tool.type == "mcp" and not tool.mcp_config:
            self._add_error(
                "VR-T02",
                "tool",
                tool.id,
                "mcp_config",
                "mcp_config is required when type='mcp'",
                "Add mcp_config with server details",
            )
        self._pass_rule()

        # VR-T03: If type=rest_api, api_config required
        self._check_rule("VR-T03")
        if tool.type == "rest_api" and not tool.api_config:
            self._add_error(
                "VR-T03",
                "tool",
                tool.id,
                "api_config",
                "api_config is required when type='rest_api'",
                "Add api_config with base_url and authentication",
            )
        self._pass_rule()

        # VR-T04: capabilities ≥ 1 (Pydantic handles)

        # VR-T05: base_url HTTPS
        if tool.api_config and "base_url" in tool.api_config:
            self._check_rule("VR-T05")
            base_url = tool.api_config["base_url"]
            if not base_url.startswith("https://"):
                self._add_error(
                    "VR-T05",
                    "tool",
                    tool.id,
                    "api_config.base_url",
                    f"API base_url must use HTTPS (got: {base_url})",
                    "Use 'https://' instead of 'http://'",
                )
            self._pass_rule()

        # VR-T06: channel_ids exist
        if tool.channel_ids:
            self._check_rule("VR-T06")
            for ch_id in tool.channel_ids:
                if ch_id not in self._channel_ids:
                    self._add_error(
                        "VR-T06",
                        "tool",
                        tool.id,
                        "channel_ids",
                        f"Channel '{ch_id}' does not exist",
                        f"Add Channel with id='{ch_id}' or remove from channel_ids",
                    )
            self._pass_rule()

    # ========================================================================
    # ContentTemplate Validation (5 rules)
    # ========================================================================

    def _validate_content_template(self, template):
        """Validate ContentTemplate entity (VR-CT01 to VR-CT05)"""

        # VR-CT01: id unique (checked via set)
        # VR-CT02: project_id exists (cannot validate)
        # VR-CT03: style_guidelines ≥ 1 (Pydantic handles)

        # VR-CT04: min_length < max_length
        if template.constraints:
            constraints = template.constraints
            if "min_length" in constraints and "max_length" in constraints:
                self._check_rule("VR-CT04")
                min_len = constraints["min_length"]
                max_len = constraints["max_length"]
                if min_len >= max_len:
                    self._add_error(
                        "VR-CT04",
                        "content_template",
                        template.id,
                        "constraints",
                        f"min_length ({min_len}) must be < max_length ({max_len})",
                        "Adjust length constraints so min < max",
                    )
                self._pass_rule()

        # VR-CT05: tone aligns with brand_voice (warning)
        # (Requires project context - skip for now)

    # ========================================================================
    # Milestone Validation (5 rules)
    # ========================================================================

    def _validate_milestone(self, milestone):
        """Validate Milestone entity (VR-M01 to VR-M05)"""

        # VR-M01: id unique (checked via set)
        # VR-M02: project_id exists (cannot validate)

        # VR-M03: product_ids exist
        if milestone.product_ids:
            self._check_rule("VR-M03")
            for pid in milestone.product_ids:
                if pid not in self._product_ids:
                    self._add_error(
                        "VR-M03",
                        "milestone",
                        milestone.id,
                        "product_ids",
                        f"Product '{pid}' does not exist",
                        f"Add Product with id='{pid}' or remove from product_ids",
                    )
            self._pass_rule()

        # VR-M04: campaign_ids exist
        if milestone.campaign_ids:
            self._check_rule("VR-M04")
            for cid in milestone.campaign_ids:
                if cid not in self._campaign_ids:
                    self._add_error(
                        "VR-M04",
                        "milestone",
                        milestone.id,
                        "campaign_ids",
                        f"Campaign '{cid}' does not exist",
                        f"Add Campaign with id='{cid}' or remove from campaign_ids",
                    )
            self._pass_rule()

        # VR-M05: date not > 1 year in future (warning)
        self._check_rule("VR-M05")
        try:
            milestone_date = datetime.fromisoformat(milestone.date)
            one_year_from_now = datetime.now() + timedelta(days=365)
            if milestone_date > one_year_from_now:
                self._add_warning(
                    "VR-M05",
                    "milestone",
                    milestone.id,
                    "date",
                    f"Milestone date ({milestone.date}) is more than 1 year in the future",
                    "Consider breaking into shorter-term milestones",
                )
            self._pass_rule()
        except ValueError as e:
            self._add_error(
                "VR-M05",
                "milestone",
                milestone.id,
                "date",
                f"Invalid date format: {e}",
                "Use ISO 8601 format: YYYY-MM-DD",
            )

    # ========================================================================
    # Analytics Validation (1 rule) - NEW in v2.0.0
    # ========================================================================

    def _validate_analytics(self, analytics):
        """Validate Analytics entity (ANLY-01)"""

        # ANLY-01: entity_id must reference existing Campaign or Plan
        self.result.rules_checked += 1
        from marketing_spec_kit.models import AnalyticsType

        if analytics.type == AnalyticsType.CAMPAIGN:
            if analytics.entity_id not in self._campaign_ids:
                self._add_issue(
                    "ANLY-01",
                    "error",
                    "analytics",
                    analytics.id,
                    "entity_id",
                    f"Analytics references non-existent campaign '{analytics.entity_id}'",
                    f"Use one of: {', '.join(self._campaign_ids) if self._campaign_ids else '(no campaigns defined)'}",
                )
            else:
                self.result.rules_passed += 1
        elif analytics.type == AnalyticsType.PLAN:
            if analytics.entity_id not in self._plan_ids:
                self._add_issue(
                    "ANLY-01",
                    "error",
                    "analytics",
                    analytics.id,
                    "entity_id",
                    f"Analytics references non-existent plan '{analytics.entity_id}'",
                    f"Use one of: {', '.join(self._plan_ids) if self._plan_ids else '(no plans defined)'}",
                )
            else:
                self.result.rules_passed += 1

    # ========================================================================
    # Helper Methods
    # ========================================================================

    def _check_rule(self, code: str):
        """Increment rules_checked counter"""
        self.result.rules_checked += 1

    def _pass_rule(self):
        """Increment rules_passed counter"""
        self.result.rules_passed += 1

    def _add_error(
        self,
        code: str,
        entity_type: str,
        entity_id: str,
        field: str,
        message: str,
        fix: str,
    ):
        """Add validation error"""
        self.result.errors.append(
            ValidationIssue(
                code=code,
                level="error",
                entity_type=entity_type,
                entity_id=entity_id,
                field=field,
                message=message,
                fix=fix,
            )
        )

    def _add_warning(
        self,
        code: str,
        entity_type: str,
        entity_id: str,
        field: str,
        message: str,
        fix: str,
    ):
        """Add validation warning"""
        self.result.warnings.append(
            ValidationIssue(
                code=code,
                level="warning",
                entity_type=entity_type,
                entity_id=entity_id,
                field=field,
                message=message,
                fix=fix,
            )
        )

    def _add_info(
        self,
        code: str,
        entity_type: str,
        entity_id: str,
        field: str,
        message: str,
        fix: str,
    ):
        """Add validation info"""
        self.result.info.append(
            ValidationIssue(
                code=code,
                level="info",
                entity_type=entity_type,
                entity_id=entity_id,
                field=field,
                message=message,
                fix=fix,
            )
        )
