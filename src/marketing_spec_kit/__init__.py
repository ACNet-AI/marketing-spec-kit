"""marketing-spec-kit - Marketing Operations Specification Toolkit

This toolkit provides:
- Specification parsing (YAML/JSON → Pydantic models)
- Validation (45 rules from domain specification v0.3.0)
- CLI commands (init, validate)
- AI Agent Slash Commands (10 SDM workflow commands)

Version 0.3.0 introduces complete SDM (Spec-Driven Marketing) workflow system
with 10 workflow commands and comprehensive validation (9 entities, 45 rules).
"""

__version__ = "0.3.0"

# Entity models (will be implemented in models.py)
# Exceptions (will be implemented in exceptions.py)
from marketing_spec_kit.exceptions import (
    MarketingSpecError,
    ParseError,
    ValidationError,
)
from marketing_spec_kit.models import (
    Analytics,
    AnalyticsType,
    # Enums
    BrandVoice,
    Campaign,
    CampaignGoal,
    Channel,
    ChannelType,
    ContentTemplate,
    InsightType,
    MarketingPlan,
    # Root spec
    MarketingSpec,
    Milestone,
    OptimizationPriority,
    PlanApproval,
    PlanBudget,
    PlanKPI,
    # Nested Models
    PlanPeriod,
    PlanStatus,
    Product,
    # Entities
    Project,
    Strategy,
    TargetAudience,
    Tool,
)

# Parser (will be implemented in parser.py)
from marketing_spec_kit.parser import MarketingSpecParser

# Validator (will be implemented in validator.py)
from marketing_spec_kit.validator import MarketingSpecValidator, ValidationResult

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
