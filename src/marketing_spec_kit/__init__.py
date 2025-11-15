"""marketing-spec-kit - Marketing Operations Specification Toolkit

This toolkit provides:
- Specification parsing (YAML/JSON → Pydantic models)
- Validation (35 rules from domain specification v2.0.0)
- CLI commands (init, validate)
- AI Agent Slash Commands (22 operations for content generation)

Version 2.0.0 introduces workflow-driven marketing operations with MarketingPlan
and Analytics entities.
"""

__version__ = "2.0.0"

# Entity models (will be implemented in models.py)
from marketing_spec_kit.models import (
    # Enums
    BrandVoice,
    CampaignGoal,
    ChannelType,
    PlanStatus,
    AnalyticsType,
    InsightType,
    OptimizationPriority,
    # Nested Models
    PlanPeriod,
    PlanBudget,
    TargetAudience,
    Strategy,
    PlanKPI,
    PlanApproval,
    # Entities
    Project,
    Product,
    MarketingPlan,
    Campaign,
    Channel,
    Tool,
    ContentTemplate,
    Milestone,
    Analytics,
    # Root spec
    MarketingSpec,
)

# Parser (will be implemented in parser.py)
from marketing_spec_kit.parser import MarketingSpecParser

# Validator (will be implemented in validator.py)
from marketing_spec_kit.validator import MarketingSpecValidator, ValidationResult

# Exceptions (will be implemented in exceptions.py)
from marketing_spec_kit.exceptions import (
    MarketingSpecError,
    ParseError,
    ValidationError,
)

__all__ = [
    # Version
    "__version__",
    # Enums
    "BrandVoice",
    "CampaignGoal",
    "ChannelType",
    "PlanStatus",
    "AnalyticsType",
    "InsightType",
    "OptimizationPriority",
    # Nested Models
    "PlanPeriod",
    "PlanBudget",
    "TargetAudience",
    "Strategy",
    "PlanKPI",
    "PlanApproval",
    # Entities
    "Project",
    "Product",
    "MarketingPlan",
    "Campaign",
    "Channel",
    "Tool",
    "ContentTemplate",
    "Milestone",
    "Analytics",
    "MarketingSpec",
    # Parser
    "MarketingSpecParser",
    # Validator
    "MarketingSpecValidator",
    "ValidationResult",
    # Exceptions
    "MarketingSpecError",
    "ParseError",
    "ValidationError",
]
