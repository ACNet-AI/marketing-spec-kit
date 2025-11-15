"""Pydantic models for Marketing Operations Specification

This module defines 7 entities from the domain specification:
- Project: Brand identity and core values
- Product: Feature offerings and positioning
- Campaign: Time-bound marketing activities
- Channel: Distribution platforms
- Tool: Integration automation
- ContentTemplate: Brand guidelines and constraints
- Milestone: Timeline markers and events

All models use Pydantic v2.0+ for automatic validation.
"""

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, HttpUrl


# ============================================================================
# Enums
# ============================================================================


class BrandVoice(str, Enum):
    """Brand personality and tone options"""

    TECHNICAL = "Technical"
    FRIENDLY = "Friendly"
    PROFESSIONAL = "Professional"
    CASUAL = "Casual"
    EDUCATIONAL = "Educational"


class CampaignGoal(str, Enum):
    """Marketing campaign objective types (AIDA funnel stages)"""

    AWARENESS = "awareness"  # Top of funnel
    CONSIDERATION = "consideration"  # Middle of funnel
    CONVERSION = "conversion"  # Bottom of funnel


class ChannelType(str, Enum):
    """Distribution channel categories"""

    SOCIAL_MEDIA = "social_media"
    EMAIL = "email"
    BLOG = "blog"
    FORUM = "forum"
    VIDEO = "video"
    PODCAST = "podcast"


# ============================================================================
# Entity Models
# ============================================================================


class Project(BaseModel):
    """Project entity - Brand identity and core values
    
    Represents the top-level project with brand guidelines and target audience.
    Referenced by Products, Campaigns, ContentTemplates, and Milestones.
    """

    name: str = Field(..., description="Official project name")
    tagline: str = Field(..., max_length=100, description="Short memorable description")
    brand_voice: BrandVoice = Field(..., description="Primary brand personality")
    website: HttpUrl = Field(..., description="Official project website (HTTPS)")
    target_audience: List[str] = Field(
        ..., min_items=1, description="Primary user segments"
    )
    value_propositions: List[str] = Field(
        ..., min_items=1, description="Core benefits and differentiators"
    )
    logo_url: Optional[HttpUrl] = Field(None, description="Project logo image URL")
    social_handles: Optional[Dict[str, str]] = Field(
        None, description="Social media accounts (platform: handle)"
    )


class Product(BaseModel):
    """Product entity - Features and positioning
    
    Represents a specific product or service offering within the project.
    Referenced by Campaigns.
    """

    id: str = Field(
        ...,
        pattern=r"^[a-z0-9-]+$",
        description="Unique product identifier (lowercase, hyphens only)",
    )
    name: str = Field(..., description="Display name")
    description: str = Field(
        ..., max_length=500, description="Detailed description for marketing materials"
    )
    project_id: str = Field(..., description="Parent Project identifier")
    target_audience: List[str] = Field(
        ..., min_items=1, description="User segments for this product"
    )
    key_features: List[str] = Field(
        ..., min_items=1, description="Top 3-5 features (recommended: 3-5 items)"
    )
    positioning: Optional[str] = Field(
        None,
        max_length=200,
        description="Unique selling proposition (how it differs from competitors)",
    )
    launch_date: Optional[str] = Field(
        None, description="Launch date (ISO 8601 format: YYYY-MM-DD)"
    )


class Campaign(BaseModel):
    """Campaign entity - Time-bound marketing activity
    
    Represents a marketing campaign with goals, budget, timeline, and target channels.
    References Products and Channels.
    """

    id: str = Field(
        ...,
        pattern=r"^[a-z0-9-]+$",
        description="Unique campaign identifier (lowercase, hyphens only)",
    )
    name: str = Field(..., description="Campaign name")
    goal: CampaignGoal = Field(..., description="Primary objective (AIDA funnel stage)")
    project_id: str = Field(..., description="Parent Project identifier")
    product_ids: Optional[List[str]] = Field(
        None, description="Products promoted in this campaign"
    )
    target_audience: List[str] = Field(
        ..., min_items=1, description="User segments to reach"
    )
    budget: float = Field(..., gt=0, description="Campaign budget (must be > 0)")
    start_date: str = Field(..., description="Campaign start date (ISO 8601: YYYY-MM-DD)")
    end_date: str = Field(..., description="Campaign end date (ISO 8601: YYYY-MM-DD)")
    channels: List[str] = Field(
        ..., min_items=1, description="Channel IDs where campaign will run"
    )
    kpis: Optional[Dict[str, float]] = Field(
        None,
        description="Key performance indicators (e.g., {'CTR': 0.05, 'ROAS': 4.0})",
    )
    status: str = Field(default="draft", description="Campaign status")


class Channel(BaseModel):
    """Channel entity - Distribution platform
    
    Represents a specific channel (e.g., Twitter, email newsletter) where content is distributed.
    May reference a Tool for automation.
    """

    id: str = Field(
        ...,
        pattern=r"^[a-z0-9-]+$",
        description="Unique channel identifier (lowercase, hyphens only)",
    )
    name: str = Field(..., description="Channel name")
    type: ChannelType = Field(..., description="Channel category")
    platform: str = Field(..., description="Specific platform (e.g., 'twitter', 'mailchimp')")
    content_types: List[str] = Field(
        ..., min_items=1, description="Supported content types (e.g., ['short_text', 'images'])"
    )
    audiences: Optional[List[str]] = Field(
        None, description="Target audiences for this channel"
    )
    constraints: Optional[Dict[str, Any]] = Field(
        None,
        description="Platform-specific constraints (e.g., {'max_text_length': 280, 'max_hashtags': 5})",
    )
    tool_id: Optional[str] = Field(
        None, description="Tool used for automation (if any)"
    )
    config: Optional[Dict[str, Any]] = Field(
        None, description="Channel-specific configuration"
    )


class Tool(BaseModel):
    """Tool entity - Integration automation
    
    Represents a tool used for marketing automation (MCP server, REST API, or manual).
    Referenced by Channels.
    """

    id: str = Field(
        ...,
        pattern=r"^[a-z0-9-]+$",
        description="Unique tool identifier (lowercase, hyphens only)",
    )
    name: str = Field(..., description="Tool name")
    type: str = Field(
        ..., description="Tool type: 'mcp', 'rest_api', or 'manual'"
    )
    capabilities: List[str] = Field(
        ..., min_items=1, description="Supported operations (e.g., ['schedule', 'publish', 'analyze'])"
    )
    status: str = Field(
        ..., description="Tool status: 'active', 'inactive', or 'testing'"
    )
    mcp_config: Optional[Dict[str, Any]] = Field(
        None,
        description="MCP server configuration (required if type='mcp')",
    )
    api_config: Optional[Dict[str, Any]] = Field(
        None,
        description="REST API configuration (required if type='rest_api')",
    )
    channel_ids: Optional[List[str]] = Field(
        None, description="Channels using this tool"
    )


class ContentTemplate(BaseModel):
    """ContentTemplate entity - Brand guidelines and constraints
    
    Represents a reusable template for content creation with brand guidelines.
    Referenced by Campaigns for consistent content generation.
    """

    id: str = Field(
        ...,
        pattern=r"^[a-z0-9-]+$",
        description="Unique template identifier (lowercase, hyphens only)",
    )
    name: str = Field(..., description="Template name")
    type: str = Field(..., description="Content type (e.g., 'social_post', 'blog_article', 'email')")
    tone: str = Field(..., description="Content tone (should align with project brand_voice)")
    style_guidelines: List[str] = Field(
        ..., min_items=1, description="Writing style rules (e.g., ['Use active voice', 'Avoid jargon'])"
    )
    project_id: str = Field(..., description="Parent Project identifier")
    constraints: Optional[Dict[str, Any]] = Field(
        None,
        description="Content constraints (e.g., {'min_length': 100, 'max_length': 500})",
    )
    examples: Optional[List[str]] = Field(
        None, description="Example content following this template"
    )


class Milestone(BaseModel):
    """Milestone entity - Timeline markers and events
    
    Represents a significant event or deadline in the marketing timeline.
    May reference Products and Campaigns.
    """

    id: str = Field(
        ...,
        pattern=r"^[a-z0-9-]+$",
        description="Unique milestone identifier (lowercase, hyphens only)",
    )
    name: str = Field(..., description="Milestone name")
    type: str = Field(..., description="Milestone type (e.g., 'launch', 'release', 'event')")
    date: str = Field(..., description="Milestone date (ISO 8601: YYYY-MM-DD)")
    project_id: str = Field(..., description="Parent Project identifier")
    status: str = Field(default="planned", description="Milestone status")
    description: Optional[str] = Field(None, description="Detailed description")
    product_ids: Optional[List[str]] = Field(
        None, description="Products associated with this milestone"
    )
    campaign_ids: Optional[List[str]] = Field(
        None, description="Campaigns associated with this milestone"
    )


# ============================================================================
# Root Specification Model
# ============================================================================


class MarketingSpec(BaseModel):
    """Root specification model containing all marketing entities
    
    This is the top-level model representing a complete marketing specification.
    It contains one Project and optional collections of other entities.
    
    Example:
        >>> spec = MarketingSpec(
        ...     project=Project(
        ...         name="MyProject",
        ...         tagline="Amazing software",
        ...         brand_voice=BrandVoice.TECHNICAL,
        ...         website="https://example.com",
        ...         target_audience=["developers"],
        ...         value_propositions=["Fast", "Reliable"],
        ...     ),
        ...     products=[...],
        ...     campaigns=[...],
        ... )
    """

    project: Project = Field(..., description="Project brand identity (required)")
    products: List[Product] = Field(
        default_factory=list, description="Product offerings"
    )
    campaigns: List[Campaign] = Field(
        default_factory=list, description="Marketing campaigns"
    )
    channels: List[Channel] = Field(
        default_factory=list, description="Distribution channels"
    )
    tools: List[Tool] = Field(
        default_factory=list, description="Automation tools"
    )
    content_templates: List[ContentTemplate] = Field(
        default_factory=list, description="Content templates"
    )
    milestones: List[Milestone] = Field(
        default_factory=list, description="Timeline milestones"
    )

