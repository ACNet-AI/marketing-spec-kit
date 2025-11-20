"""Pydantic models for Marketing Operations Specification

This module defines 9 entities from the domain specification (v0.3.0):
- Project: Brand identity and core values
- Product: Feature offerings and positioning
- MarketingPlan: Strategic marketing plan (NEW in v0.2.0)
- Campaign: Time-bound marketing activities
- Channel: Distribution platforms
- Tool: Integration automation
- ContentTemplate: Brand guidelines and constraints
- Milestone: Timeline markers and events
- Analytics: Performance analytics report (NEW in v0.2.0)

All models use Pydantic v2.0+ for automatic validation.

Breaking Changes in v0.2.0:
- Campaign.plan_id is now REQUIRED (was not present in v0.1.x)
- All campaigns must belong to a MarketingPlan
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


class PlanStatus(str, Enum):
    """Marketing plan status (NEW in v2.0.0)"""

    DRAFT = "draft"
    APPROVED = "approved"
    ACTIVE = "active"
    COMPLETED = "completed"
    ARCHIVED = "archived"


class AnalyticsType(str, Enum):
    """Analytics report type (NEW in v2.0.0)"""

    CAMPAIGN = "campaign"
    PLAN = "plan"


class InsightType(str, Enum):
    """Analytics insight category (NEW in v2.0.0)"""

    SUCCESS = "success"
    CONCERN = "concern"
    OPPORTUNITY = "opportunity"


class OptimizationPriority(str, Enum):
    """Optimization recommendation priority (NEW in v2.0.0)"""

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class OptimizationEffort(str, Enum):
    """Implementation effort for optimization (NEW in v2.0.0)"""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class KPIPriority(str, Enum):
    """KPI importance level (NEW in v2.0.0)"""

    P0 = "P0"  # Critical
    P1 = "P1"  # Important
    P2 = "P2"  # Nice-to-have


class AudiencePriority(str, Enum):
    """Target audience segment priority (NEW in v2.0.0)"""

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class ContentStatus(str, Enum):
    """Content calendar entry status (NEW in v2.0.0)"""

    PLANNED = "planned"
    CREATED = "created"
    PUBLISHED = "published"


# ============================================================================
# Nested Models (NEW in v2.0.0)
# ============================================================================


class PlanPeriod(BaseModel):
    """Time period for marketing plan"""

    start_date: str = Field(..., description="Plan start date (ISO 8601)")
    end_date: str = Field(..., description="Plan end date (ISO 8601)")
    duration_weeks: int = Field(..., ge=4, le=52, description="Duration in weeks")


class PlanBudget(BaseModel):
    """Budget allocation for marketing plan"""

    total: float = Field(..., gt=0, description="Total budget")
    currency: str = Field(default="USD", description="Currency code (ISO 4217)")
    allocation: Dict[str, float] = Field(
        ...,
        description="Budget breakdown by category",
        examples=[
            {
                "content_creation": 2000,
                "paid_promotion": 2500,
                "tools": 300,
                "contingency": 200,
            }
        ],
    )


class TargetAudience(BaseModel):
    """Target audience segment for marketing plan"""

    segment: str = Field(..., description="Audience segment name")
    description: str = Field(..., description="Detailed segment description")
    size_estimate: int = Field(..., gt=0, description="Estimated audience size")
    priority: AudiencePriority = Field(..., description="Targeting priority")


class Strategy(BaseModel):
    """Marketing strategy for plan"""

    name: str = Field(..., description="Strategy name")
    description: str = Field(..., description="Strategy details")
    rationale: str = Field(..., description="Why this strategy was chosen")
    success_criteria: str = Field(..., description="How success is measured")


class PlanKPI(BaseModel):
    """Key Performance Indicator for plan"""

    name: str = Field(..., description="KPI name")
    target: float = Field(..., description="Target value to achieve")
    unit: str = Field(..., description="Measurement unit")
    measurement: str = Field(..., description="How to measure this KPI")
    priority: KPIPriority = Field(..., description="KPI priority")


class PlanApproval(BaseModel):
    """Approval metadata for plan"""

    approved_by: str = Field(..., description="Name or ID of approver")
    approved_at: str = Field(..., description="Approval timestamp (ISO 8601)")
    comments: Optional[str] = Field(None, description="Approval notes or feedback")


class ContentCalendarEntry(BaseModel):
    """Single entry in content calendar"""

    date: str = Field(..., description="Publish date (ISO 8601)")
    content_type: str = Field(..., description="Type of content")
    channel_id: str = Field(..., description="Target channel")
    title: str = Field(..., description="Content title or description")
    status: ContentStatus = Field(..., description="Content status")


class AnalyticsPeriod(BaseModel):
    """Time period for analytics report"""

    start_date: str = Field(..., description="Analysis start date (ISO 8601)")
    end_date: str = Field(..., description="Analysis end date (ISO 8601)")


class KPIComparison(BaseModel):
    """KPI target vs actual comparison"""

    target: float = Field(..., description="Target value")
    actual: float = Field(..., description="Actual value achieved")
    achievement: float = Field(..., description="Achievement percentage")
    status: str = Field(
        ..., description="Status: exceeds, meets, on_track, below_target, far_below"
    )


class AnalyticsInsight(BaseModel):
    """AI-generated insight from data analysis"""

    type: InsightType = Field(..., description="Insight category")
    description: str = Field(..., description="What the insight is about")
    evidence: str = Field(..., description="Data supporting this insight")
    recommendation: str = Field(..., description="Suggested action")


class Optimization(BaseModel):
    """AI-generated optimization recommendation"""

    priority: OptimizationPriority = Field(..., description="Optimization priority")
    action: str = Field(..., description="Specific action to take")
    expected_impact: str = Field(..., description="Expected result")
    effort: OptimizationEffort = Field(..., description="Implementation effort")


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
    plan_id: str = Field(
        ...,
        description="Parent MarketingPlan identifier (REQUIRED in v2.0.0, BREAKING CHANGE)",
    )
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
    expected_kpis: Optional[Dict[str, float]] = Field(
        None,
        description="Expected KPI targets (NEW in v2.0.0, for design phase)",
    )
    content_calendar: Optional[List[ContentCalendarEntry]] = Field(
        None,
        description="Content publishing schedule (NEW in v2.0.0)",
    )
    status: str = Field(default="draft", description="Campaign status")


class MarketingPlan(BaseModel):
    """MarketingPlan entity - Strategic marketing plan (NEW in v2.0.0)
    
    Represents a comprehensive marketing plan with objectives, strategies, budget allocation,
    and KPI targets. Plans contain multiple campaigns and span weeks to months.
    """

    id: str = Field(
        ...,
        pattern=r"^[a-z0-9-]+$",
        description="Unique plan identifier (lowercase, hyphens only)",
    )
    name: str = Field(..., min_length=3, description="Plan name")
    project_id: str = Field(..., description="Parent Project identifier")
    period: PlanPeriod = Field(..., description="Plan time period")
    objectives: List[str] = Field(
        ...,
        min_items=1,
        max_items=5,
        description="High-level marketing objectives (1-5)",
    )
    target_audience: List[TargetAudience] = Field(
        ..., min_items=1, description="Target audience segments"
    )
    strategies: List[Strategy] = Field(
        ...,
        min_items=1,
        max_items=8,
        description="Marketing strategies to achieve objectives",
    )
    budget: PlanBudget = Field(..., description="Budget allocation")
    kpis: List[PlanKPI] = Field(
        ...,
        min_items=1,
        max_items=10,
        description="Key performance indicators (1-10)",
    )
    campaign_ids: Optional[List[str]] = Field(
        None, description="Campaigns executed under this plan"
    )
    status: PlanStatus = Field(default=PlanStatus.DRAFT, description="Plan status")
    created_at: str = Field(..., description="Creation timestamp (ISO 8601)")
    updated_at: str = Field(..., description="Last update timestamp (ISO 8601)")
    approval: Optional[PlanApproval] = Field(
        None, description="Approval metadata (required for APPROVED/ACTIVE status)"
    )


class Analytics(BaseModel):
    """Analytics entity - Performance analytics report (NEW in v2.0.0)
    
    Represents an AI-generated analytics report for a campaign or plan,
    including KPI comparisons, insights, and optimization recommendations.
    """

    id: str = Field(
        ...,
        pattern=r"^[a-z0-9-]+$",
        description="Unique analytics report identifier",
    )
    type: AnalyticsType = Field(..., description="Report type: campaign or plan")
    entity_id: str = Field(
        ..., description="ID of the campaign or plan being analyzed"
    )
    period: AnalyticsPeriod = Field(..., description="Analysis time period")
    metrics: Dict[str, float] = Field(
        ..., description="Measured metrics (e.g., {'reach': 50000, 'conversions': 120})"
    )
    vs_target: Dict[str, KPIComparison] = Field(
        ..., description="KPI target vs actual comparisons"
    )
    insights: List[AnalyticsInsight] = Field(
        ...,
        min_items=1,
        max_items=10,
        description="AI-generated insights (1-10)",
    )
    optimizations: Optional[List[Optimization]] = Field(
        None,
        max_items=10,
        description="AI-generated optimization recommendations (max 10)",
    )
    generated_at: str = Field(
        ..., description="Report generation timestamp (ISO 8601)"
    )


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
    plans: List[MarketingPlan] = Field(
        default_factory=list, description="Marketing plans (NEW in v2.0.0)"
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
    analytics: List[Analytics] = Field(
        default_factory=list, description="Analytics reports (NEW in v2.0.0)"
    )

