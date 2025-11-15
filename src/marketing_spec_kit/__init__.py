"""marketing-spec-kit - Marketing Operations Specification Toolkit

This toolkit provides:
- Specification parsing (YAML/JSON → Pydantic models)
- Validation (25 rules from domain specification)
- CLI commands (init, validate)
- AI Agent Slash Commands (13 operations for content generation)
"""

__version__ = "0.1.0"

# Entity models (will be implemented in models.py)
from marketing_spec_kit.models import (
    # Enums
    BrandVoice,
    CampaignGoal,
    ChannelType,
    # Entities
    Project,
    Product,
    Campaign,
    Channel,
    Tool,
    ContentTemplate,
    Milestone,
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
    # Entities
    "Project",
    "Product",
    "Campaign",
    "Channel",
    "Tool",
    "ContentTemplate",
    "Milestone",
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
