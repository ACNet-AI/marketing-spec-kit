---
name: marketspec.create
description: Generate the final marketing specification YAML
layer: sdm
status: implemented
type: core
category: Core Flow
source: Adapted from metaspec.sdd.implement
version: 0.3.0
---

# /marketspec.create 🔴 Core

**Purpose**: Generate a complete, validated `marketing-spec.yaml` from all discovery, strategy, and task documents.

**Category**: Core Flow (Essential Workflow)  
**Output**: `marketing-spec.yaml` ⭐  
**Adapted from**: `metaspec.sdd.implement`

---

## Purpose

This is the **culmination command** that:
- Aggregates all information from previous phases
- Generates structured YAML specification
- Includes all 9 marketing entities
- Validates data integrity and relationships
- Creates production-ready specification file

The output `marketing-spec.yaml` is the **single source of truth** for all marketing operations.

---

## Command Usage

```
/marketspec.create
/marketspec.create --template [minimal|default|full]
/marketspec.create --validate-only
```

**Examples**:
```
/marketspec.create
/marketspec.create --template full
/marketspec.create --validate-only  # Check without creating
```

---

## Prerequisites

- **Required**: Discovery document from `/marketspec.discover`
- **Required**: Strategy document from `/marketspec.strategy`
- **Recommended**: Clarification from `/marketspec.clarify`
- **Recommended**: Tasks from `/marketspec.tasks`
- **Optional**: Constitution for validation

---

## Execution Steps

### Step 1: Gather All Source Documents

Collect and read all relevant documents:

```yaml
source_documents:
  required:
    - path: "specs/discovery/[name]-discovery.md"
      purpose: "Project context, objectives, audiences"
    - path: "specs/strategy/[name]-strategy.md"
      purpose: "Campaigns, channels, content, KPIs"
  
  recommended:
    - path: "specs/clarifications/[name]-clarification.md"
      purpose: "Refined requirements"
    - path: "specs/tasks/[name]-tasks.md"
      purpose: "Milestones, timeline"
  
  optional:
    - path: "memory/marketing-constitution.md"
      purpose: "Brand guidelines, constraints"
```

**Validation**:
- ✅ Check all required documents exist
- ⚠️ Warn if recommended documents missing
- ℹ️ Note if optional documents available

### Step 2: Extract Project Information

From discovery document, extract project entity:

```yaml
# Source: discovery document → Project Context

project:
  name: "MetaSpec"
  tagline: "Spec-Driven Development Framework"
  description: "A framework that transforms specifications into production code through AI-assisted generation"
  brand_voice: "Professional"  # From constitution or discovery
  website: "https://metaspec.dev"
  
  target_audience:
    - "Senior Python Developers"
    - "Mid-level JavaScript Developers"
    - "Technical CTOs at startups"
  
  value_propositions:
    - "Reduce development time by 50%"
    - "Ensure spec-implementation consistency"
    - "Streamline team collaboration"
  
  # Optional fields
  logo_url: "https://metaspec.dev/logo.png"
  social_handles:
    twitter: "@metaspec_dev"
    github: "metaspec"
    linkedin: "metaspec"
  
  primary_color: "#0066CC"  # From constitution if available
  secondary_color: "#00CC66"
```

**Mapping**:
- `name` ← Discovery: Project Context > name
- `tagline` ← Discovery: Project Context > tagline
- `description` ← Discovery: Project Context > description
- `target_audience` ← Discovery: Target Audiences (refined in Clarify)
- `value_propositions` ← Discovery: Project Context > value propositions
- `brand_voice` ← Constitution: Brand Guidelines > voice

### Step 3: Extract Products (if applicable)

From discovery/strategy, identify products:

```yaml
# If marketing multiple products/tiers

products:
  - id: "metaspec-core"
    name: "MetaSpec Core"
    description: "Open source spec-driven development framework"
    project_id: "metaspec"
    target_audience:
      - "Individual Developers"
      - "Small Teams"
    key_features:
      - "Spec parsing and validation"
      - "Code generation templates"
      - "CLI tooling"
      - "VS Code extension"
    positioning: "Free, powerful, community-driven"
    pricing: "free"
    launch_date: "2025-01-15"
  
  - id: "metaspec-pro"
    name: "MetaSpec Pro"
    description: "Enterprise features with advanced capabilities"
    project_id: "metaspec"
    target_audience:
      - "Enterprise Teams"
      - "Large Organizations"
    key_features:
      - "All core features"
      - "Team collaboration"
      - "Custom templates"
      - "Priority support"
      - "SLA guarantees"
    positioning: "Enterprise-grade solution for large teams"
    pricing: "$99/user/month"
    launch_date: "2025-03-01"
```

**Note**: If single product, `products` array can be empty or contain one entry.

### Step 4: Create Marketing Plans

From strategy document, extract campaigns and convert to plan:

```yaml
# Source: strategy document → Campaign Structure, Timeline

plans:
  - id: "q1-2025-growth"
    name: "Q1 2025 Growth Plan"
    project_id: "metaspec"
    
    period:
      start_date: "2025-01-15"
      end_date: "2025-03-31"
      duration_weeks: 11
    
    objectives:
      - "Reach 500 GitHub stars"
      - "Acquire 1000 email subscribers"
      - "Generate 50K website visits"
      - "Establish presence in developer community"
    
    target_audience:
      - segment: "Senior Python/JS Developers"
        description: "Experienced developers at startups and mid-size companies"
        size_estimate: 50000
        priority: "high"
      
      - segment: "Technical Decision Makers"
        description: "CTOs and Engineering Leads evaluating tools"
        size_estimate: 10000
        priority: "medium"
    
    strategies:
      - name: "Content-Led Growth"
        description: "Publish weekly technical tutorials and guides"
        rationale: "Developers trust educational content"
        success_criteria: "10K monthly blog visitors"
      
      - name: "Community Engagement"
        description: "Active participation in developer forums"
        rationale: "Build trust and credibility"
        success_criteria: "1000 community interactions"
    
    budget:
      total: 10000
      currency: "USD"
      allocation:
        content_creation: 4000
        paid_promotion: 3000
        tools: 1500
        community: 1000
        contingency: 500
    
    kpis:
      - name: "GitHub Stars"
        target: 500
        unit: "stars"
        measurement: "GitHub API"
        priority: "P0"
        baseline: 50
      
      - name: "Email Subscribers"
        target: 1000
        unit: "subscribers"
        measurement: "ConvertKit analytics"
        priority: "P0"
        baseline: 100
      
      - name: "Website Traffic"
        target: 50000
        unit: "visits"
        measurement: "Google Analytics"
        priority: "P1"
        baseline: 500
    
    campaign_ids:
      - "dev-onboarding"
      - "power-user-stories"
    
    status: "draft"
    created_at: "2025-11-16T10:00:00Z"
    updated_at: "2025-11-16T10:00:00Z"
```

### Step 5: Define Campaigns

From strategy document, extract individual campaigns:

```yaml
# Source: strategy document → Campaign Structure

campaigns:
  - id: "dev-onboarding"
    name: "Developer Onboarding Campaign"
    goal: "awareness"  # awareness, consideration, conversion
    project_id: "metaspec"
    plan_id: "q1-2025-growth"
    product_ids: ["metaspec-core"]
    
    target_audience:
      - "Senior Python/JS Developers"
      - "Technical Decision Makers"
    
    messaging:
      headline: "Build Better Software with Spec-Driven Development"
      tagline: "From specification to production in minutes"
      key_messages:
        - "Reduce development time significantly"
        - "Eliminate spec-code drift"
        - "Collaborate more effectively"
    
    channels:
      - "dev-blog"
      - "dev-twitter"
      - "dev-to"
      - "github-discussions"
    
    content_types:
      - "Tutorial blog posts"
      - "Code examples"
      - "Video walkthroughs"
      - "Social media tips"
    
    budget: 6000
    start_date: "2025-01-15"
    end_date: "2025-02-28"
    
    kpis:
      target_impressions: 100000
      target_engagement_rate: 0.05  # 5%
      target_click_through_rate: 0.03  # 3%
      target_conversions: 300  # GitHub stars
    
    status: "draft"
    created_by: "Marketing Team"
    created_at: "2025-11-16T10:00:00Z"
  
  - id: "power-user-stories"
    name: "Power User Success Stories"
    goal: "consideration"
    project_id: "metaspec"
    plan_id: "q1-2025-growth"
    product_ids: ["metaspec-core", "metaspec-pro"]
    
    target_audience:
      - "Technical Decision Makers"
    
    messaging:
      headline: "See How Teams Use MetaSpec"
      tagline: "Real stories from real developers"
      key_messages:
        - "Learn from successful implementations"
        - "Discover advanced use cases"
        - "Understand ROI and benefits"
    
    channels:
      - "dev-blog"
      - "linkedin"
      - "youtube"
    
    content_types:
      - "Case studies"
      - "Video testimonials"
      - "Technical deep-dives"
    
    budget: 4000
    start_date: "2025-02-15"
    end_date: "2025-03-31"
    
    kpis:
      target_impressions: 50000
      target_engagement_rate: 0.08  # 8% (higher quality content)
      target_conversions: 200  # Email signups
    
    status: "draft"
```

### Step 6: Configure Channels

From strategy document, extract channel configurations:

```yaml
# Source: strategy document → Channel Strategy

channels:
  - id: "dev-blog"
    name: "MetaSpec Developer Blog"
    type: "blog"
    platform: "Ghost"
    url: "https://blog.metaspec.dev"
    
    audiences:
      - "Senior Python/JS Developers"
      - "Technical Decision Makers"
    
    content_types:
      - "long_form_text"
      - "code_samples"
      - "diagrams"
      - "videos"
    
    publishing_schedule:
      frequency: "2 posts per week"
      days: ["Tuesday", "Thursday"]
      time: "10:00 AM EST"
    
    content_guidelines:
      min_length: 800
      max_length: 3000
      required_elements:
        - "Code examples"
        - "Practical use cases"
        - "Clear takeaways"
      tone: "Educational and technical"
    
    distribution:
      - "Cross-post to Dev.to"
      - "Share on Twitter"
      - "Submit to Hacker News"
      - "Include in newsletter"
    
    metrics_tracked:
      - "Page views"
      - "Time on page"
      - "Scroll depth"
      - "Social shares"
      - "GitHub stars from referral"
    
    owner: "Content Manager"
    status: "active"
  
  - id: "dev-twitter"
    name: "Twitter/X Developer Account"
    type: "social_media"
    platform: "twitter"
    handle: "@metaspec_dev"
    url: "https://twitter.com/metaspec_dev"
    
    audiences:
      - "Senior Python/JS Developers"
    
    content_types:
      - "short_text"
      - "images"
      - "videos"
      - "polls"
    
    publishing_schedule:
      frequency: "2-3 posts per day"
      times: ["09:00 AM", "02:00 PM", "06:00 PM"]
      timezone: "EST"
    
    content_mix:
      tips_tricks: 40  # %
      product_updates: 30
      community_highlights: 20
      industry_news: 10
    
    engagement_strategy:
      response_time: "< 2 hours"
      daily_engagement: "10-15 interactions"
      hashtag_strategy:
        - "#DevTools"
        - "#Python"
        - "#JavaScript"
        - max_per_post: 3
    
    constraints:
      max_text_length: 280
      max_hashtags: 5
      max_images: 4
    
    metrics_tracked:
      - "Impressions"
      - "Engagement rate"
      - "Profile visits"
      - "Link clicks"
      - "Follower growth"
    
    owner: "Social Media Manager"
    status: "active"
  
  - id: "dev-to"
    name: "Dev.to Community"
    type: "community"
    platform: "dev_to"
    url: "https://dev.to/metaspec"
    
    audiences:
      - "Senior Python/JS Developers"
    
    content_types:
      - "technical_tutorials"
      - "discussion_posts"
    
    publishing_schedule:
      frequency: "Cross-post blog articles"
      timing: "Same day as blog"
    
    engagement_strategy:
      response_time: "< 4 hours"
      comment_engagement: "Reply to all comments"
    
    metrics_tracked:
      - "Post views"
      - "Reactions"
      - "Comments"
      - "Followers"
    
    owner: "Content Manager"
    status: "active"
```

### Step 7: Define Tools

List marketing tools and platforms:

```yaml
# Source: strategy document → Tools Required

tools:
  - id: "google-analytics"
    name: "Google Analytics 4"
    category: "analytics"
    purpose: "Website traffic and behavior tracking"
    url: "https://analytics.google.com"
    cost: 0
    cost_frequency: "free"
    integration_required: true
    owner: "Marketing Lead"
    status: "active"
  
  - id: "convertkit"
    name: "ConvertKit"
    category: "email_marketing"
    purpose: "Email list management and campaigns"
    url: "https://convertkit.com"
    cost: 29
    cost_frequency: "monthly"
    integration_required: true
    owner: "Content Manager"
    status: "active"
  
  - id: "buffer"
    name: "Buffer"
    category: "social_media"
    purpose: "Social media scheduling and management"
    url: "https://buffer.com"
    cost: 15
    cost_frequency: "monthly"
    integration_required: false
    owner: "Social Media Manager"
    status: "active"
  
  - id: "canva-pro"
    name: "Canva Pro"
    category: "design"
    purpose: "Graphics and visual content creation"
    url: "https://canva.com"
    cost: 12.99
    cost_frequency: "monthly"
    integration_required: false
    owner: "Designer"
    status: "active"
  
  - id: "notion"
    name: "Notion"
    category: "project_management"
    purpose: "Content calendar and task tracking"
    url: "https://notion.so"
    cost: 10
    cost_frequency: "monthly"
    integration_required: false
    owner: "Marketing Team"
    status: "active"
```

### Step 8: Create Content Templates

Define reusable content templates:

```yaml
# Source: strategy document → Content Plan

content_templates:
  - id: "tutorial-blog-post"
    name: "Tutorial Blog Post Template"
    type: "blog_post"
    channel_ids: ["dev-blog", "dev-to"]
    
    structure:
      - section: "Introduction"
        guidelines: "State the problem and what reader will learn"
        length: "100-150 words"
      
      - section: "Prerequisites"
        guidelines: "List required knowledge and tools"
        length: "50-100 words"
      
      - section: "Step-by-Step Guide"
        guidelines: "Detailed walkthrough with code examples"
        length: "500-1500 words"
      
      - section: "Common Pitfalls"
        guidelines: "Address typical mistakes"
        length: "100-200 words"
      
      - section: "Conclusion"
        guidelines: "Summarize and provide next steps"
        length: "100-150 words"
    
    required_elements:
      - "At least 2 code examples"
      - "1-2 diagrams or screenshots"
      - "Clear call-to-action"
      - "Links to documentation"
    
    seo_guidelines:
      target_keyword_density: 0.02  # 2%
      meta_description_length: "150-160 characters"
      h2_tags: "3-5"
      h3_tags: "5-8"
    
    review_checklist:
      - "Technical accuracy verified"
      - "Code examples tested"
      - "SEO optimized"
      - "Images compressed"
      - "Links validated"
    
    estimated_time: "8 hours"
    owner: "Content Writer"
  
  - id: "social-tip-post"
    name: "Social Media Tip Post"
    type: "social_post"
    channel_ids: ["dev-twitter", "linkedin"]
    
    structure:
      - element: "Hook"
        guidelines: "Grab attention in first line"
        max_length: 50
      
      - element: "Tip Content"
        guidelines: "Practical, actionable advice"
        max_length: 150
      
      - element: "CTA"
        guidelines: "Encourage engagement or link click"
        max_length: 30
    
    format_options:
      - "Text only"
      - "Text + code screenshot"
      - "Text + tip graphic"
      - "Short video (< 60s)"
    
    best_practices:
      - "Use line breaks for readability"
      - "Include 1-3 relevant hashtags"
      - "Tag relevant accounts if appropriate"
      - "Post at optimal times"
    
    estimated_time: "30 minutes"
    owner: "Social Media Manager"
```

### Step 9: Define Milestones

From tasks document, extract key milestones:

```yaml
# Source: tasks document → Timeline → Milestones

milestones:
  - id: "campaign-launch"
    name: "Campaign Launch"
    description: "All channels active, first content published"
    plan_id: "q1-2025-growth"
    campaign_ids: ["dev-onboarding"]
    date: "2025-01-15"
    
    deliverables:
      - "Website live with tracking"
      - "Social accounts created and active"
      - "First 5 blog posts published"
      - "Email list setup complete"
    
    success_criteria:
      - "All channels functional"
      - "Analytics tracking verified"
      - "Team trained on tools"
    
    status: "pending"
  
  - id: "content-rhythm-established"
    name: "Content Publishing Rhythm Established"
    description: "Consistent content production and publishing"
    plan_id: "q1-2025-growth"
    campaign_ids: ["dev-onboarding"]
    date: "2025-02-01"
    
    deliverables:
      - "2 blog posts/week sustained"
      - "Daily social media activity"
      - "Community engagement active"
      - "First metrics review completed"
    
    success_criteria:
      - "Content buffer: 2 weeks ahead"
      - "Engagement rate > 3%"
      - "No missed publications"
    
    status: "pending"
  
  - id: "mid-campaign-review"
    name: "Mid-Campaign Performance Review"
    description: "Comprehensive review and optimization"
    plan_id: "q1-2025-growth"
    campaign_ids: ["dev-onboarding", "power-user-stories"]
    date: "2025-02-15"
    
    deliverables:
      - "Full KPI analysis"
      - "Content performance review"
      - "Channel effectiveness assessment"
      - "Strategy adjustment recommendations"
    
    success_criteria:
      - "50% progress toward KPI targets"
      - "Optimization plan documented"
      - "Budget pacing on track"
    
    status: "pending"
  
  - id: "campaign-completion"
    name: "Q1 Campaign Completion"
    description: "Final results and learnings documentation"
    plan_id: "q1-2025-growth"
    campaign_ids: ["dev-onboarding", "power-user-stories"]
    date: "2025-03-31"
    
    deliverables:
      - "Final KPI report"
      - "ROI analysis"
      - "Lessons learned document"
      - "Q2 recommendations"
    
    success_criteria:
      - "Primary KPIs achieved (≥80%)"
      - "Full campaign documentation"
      - "Team retrospective completed"
    
    status: "pending"
```

### Step 10: Add Analytics Configuration

Define analytics and measurement setup:

```yaml
# Source: strategy document → KPIs, measurement

analytics:
  - id: "website-analytics"
    name: "Website Performance Tracking"
    type: "web_analytics"
    tool_id: "google-analytics"
    
    tracked_metrics:
      - metric: "page_views"
        target: 50000
        frequency: "daily"
      
      - metric: "unique_visitors"
        target: 10000
        frequency: "daily"
      
      - metric: "bounce_rate"
        target: 45  # %
        direction: "lower_is_better"
        frequency: "daily"
      
      - metric: "avg_session_duration"
        target: 180  # seconds
        direction: "higher_is_better"
        frequency: "daily"
    
    reporting:
      frequency: "weekly"
      dashboard_url: "https://analytics.google.com/..."
      stakeholders: ["Marketing Lead", "Product Manager"]
  
  - id: "social-analytics"
    name: "Social Media Performance"
    type: "social_analytics"
    tool_id: "buffer"
    
    tracked_metrics:
      - metric: "impressions"
        target: 100000
        frequency: "daily"
      
      - metric: "engagement_rate"
        target: 5  # %
        direction: "higher_is_better"
        frequency: "daily"
      
      - metric: "follower_growth"
        target: 1000
        frequency: "weekly"
      
      - metric: "link_clicks"
        target: 2000
        frequency: "daily"
    
    reporting:
      frequency: "weekly"
      dashboard_url: "https://buffer.com/..."
      stakeholders: ["Social Media Manager", "Marketing Lead"]
  
  - id: "conversion-tracking"
    name: "Conversion Funnel Tracking"
    type: "conversion_analytics"
    tool_id: "google-analytics"
    
    funnel_stages:
      - stage: "awareness"
        metric: "website_visits"
        target: 50000
      
      - stage: "interest"
        metric: "blog_reads"
        target: 10000
      
      - stage: "consideration"
        metric: "email_signups"
        target: 1000
      
      - stage: "conversion"
        metric: "github_stars"
        target: 500
    
    conversion_rates:
      visit_to_read: 0.20  # 20%
      read_to_signup: 0.10  # 10%
      signup_to_star: 0.50  # 50%
    
    reporting:
      frequency: "weekly"
      dashboard_url: "https://analytics.google.com/..."
      stakeholders: ["Marketing Lead", "Product Manager", "CEO"]
```

### Step 11: Add Metadata

Include specification metadata:

```yaml
# At top of file

specification_version: "0.3.0"

metadata:
  generated_at: "2025-11-16T10:00:00Z"
  generated_by: "marketing-spec-kit v0.3.0"
  
  source_documents:
    - "specs/discovery/metaspec-discovery.md"
    - "specs/clarifications/metaspec-clarification-2025-11-16.md"
    - "specs/strategy/metaspec-strategy.md"
    - "specs/tasks/metaspec-tasks.md"
  
  authors:
    - "Marketing Team"
    - "Product Team"
  
  version: "1.0.0"
  last_updated: "2025-11-16T10:00:00Z"
  status: "draft"
  
  review_cycle: "monthly"
  next_review: "2025-12-16"
```

### Step 12: Validate Specification

Perform comprehensive validation:

```yaml
validation_checks:
  structure:
    - ✅ All required entities present
    - ✅ Valid YAML syntax
    - ✅ Proper indentation
    - ✅ No duplicate IDs
  
  references:
    - ✅ All campaign.plan_id reference valid plans
    - ✅ All plan.campaign_ids reference valid campaigns
    - ✅ All channel_ids in campaigns exist in channels
    - ✅ All tool_ids in analytics exist in tools
    - ✅ All product_ids in campaigns exist in products
  
  data_integrity:
    - ✅ Dates are valid ISO 8601 format
    - ✅ Budget allocations sum to total
    - ✅ All required fields populated
    - ✅ Enum values are valid
    - ✅ Email addresses valid format
    - ✅ URLs valid format
  
  business_logic:
    - ✅ Campaign dates within plan dates
    - ✅ Budget totals match allocations
    - ✅ KPI targets realistic
    - ✅ No timeline conflicts
  
  constitution_alignment:
    - ✅ Brand voice consistent
    - ✅ Target audiences align
    - ✅ Content guidelines followed
```

**Validation Levels**:
- 🔴 **Error**: Must fix (blocks creation)
- 🟡 **Warning**: Should fix (allows creation)
- 🟢 **Info**: Nice to fix (optional)

### Step 13: Generate Final YAML

Create complete `marketing-spec.yaml`:

```yaml
# marketing-spec.yaml

specification_version: "0.3.0"

metadata:
  [metadata from Step 11]

project:
  [project from Step 2]

products:
  [products from Step 3]

plans:
  [plans from Step 4]

campaigns:
  [campaigns from Step 5]

channels:
  [channels from Step 6]

tools:
  [tools from Step 7]

content_templates:
  [templates from Step 8]

milestones:
  [milestones from Step 9]

analytics:
  [analytics from Step 10]
```

**Output Location**: `marketing-spec.yaml` (project root)

---

## Success Criteria

- ✅ All 9 entities populated with real data
- ✅ All cross-references valid
- ✅ YAML validates against schema
- ✅ No validation errors (warnings acceptable)
- ✅ File size reasonable (< 50KB typically)
- ✅ Human-readable and maintainable
- ✅ Aligned with source documents

---

## Output

**Primary Output**: `marketing-spec.yaml` (project root)

**Optional Outputs**:
- `marketing-spec.json` - JSON format
- `marketing-spec-summary.md` - Human-readable summary
- `validation-report.md` - Validation results

**Structure**:
```
project-root/
├── marketing-spec.yaml          # Main specification (PRIMARY)
├── marketing-spec.json          # Optional JSON format
├── marketing-spec-summary.md    # Optional summary
└── specs/
    ├── discovery/
    ├── clarifications/
    ├── strategy/
    └── tasks/
```

---

## Error Handling

**Missing Required Documents**:
```
❌ Error: Discovery document not found
→ Run /marketspec.discover first
```

**Validation Errors**:
```
🔴 Error: Budget allocation doesn't sum to total
   Plan: "q1-2025-growth"
   Total: $10,000
   Sum: $9,500
   Difference: $500
→ Fix budget allocation in strategy document
```

**Invalid References**:
```
🔴 Error: Campaign references non-existent plan
   Campaign: "dev-onboarding"
   plan_id: "q1-2025" (not found)
→ Valid plan IDs: ["q1-2025-growth"]
```

**Schema Validation**:
```
🔴 Error: Invalid date format
   Field: campaigns[0].start_date
   Value: "January 15, 2025"
   Expected: "2025-01-15" (ISO 8601)
→ Use YYYY-MM-DD format
```

---

## Example Interaction

```
User: /marketspec.create

AI: I'll generate your complete marketing specification. Let me gather all the source documents...

📄 **Source Documents**:
✅ Discovery: specs/discovery/metaspec-discovery.md
✅ Clarifications: specs/clarifications/metaspec-clarification-2025-11-16.md
✅ Strategy: specs/strategy/metaspec-strategy.md
✅ Tasks: specs/tasks/metaspec-tasks.md
✅ Constitution: memory/marketing-constitution.md

All required documents found. Generating specification...

---

**Step 1/13**: Extracting project information...
✅ Project: MetaSpec
✅ Target audiences: 2 segments
✅ Value propositions: 3 items

**Step 2/13**: Identifying products...
✅ Products: 2 (Core, Pro)

**Step 3/13**: Creating marketing plans...
✅ Plans: 1 (Q1 2025 Growth)
✅ Budget: $10,000
✅ KPIs: 8 metrics

**Step 4/13**: Defining campaigns...
✅ Campaigns: 2 (Dev Onboarding, Power User Stories)
✅ Duration: 11 weeks total

**Step 5/13**: Configuring channels...
✅ Channels: 4 (Blog, Twitter, Dev.to, GitHub)
✅ Publishing schedules defined

**Step 6/13**: Setting up tools...
✅ Tools: 5 platforms
✅ Monthly cost: $67

**Step 7/13**: Creating content templates...
✅ Templates: 2 (Tutorial, Social Tip)

**Step 8/13**: Defining milestones...
✅ Milestones: 4 key dates

**Step 9/13**: Configuring analytics...
✅ Analytics: 3 tracking setups

**Step 10/13**: Adding metadata...
✅ Version: 1.0.0
✅ Generated: 2025-11-16

**Step 11/13**: Validating specification...

🔍 **Running validation checks**:
✅ Structure: 10/10 checks passed
✅ References: 8/8 checks passed
✅ Data integrity: 12/12 checks passed
✅ Business logic: 6/6 checks passed
✅ Constitution alignment: 4/4 checks passed

🎉 **All validation checks passed!**

**Step 12/13**: Generating YAML...
✅ YAML generated (1,245 lines, 42KB)

**Step 13/13**: Writing file...
✅ File written: marketing-spec.yaml

---

✅ **Marketing specification created successfully!**

📄 **Output**: `marketing-spec.yaml`

**Specification Summary**:
- **Project**: MetaSpec
- **Products**: 2
- **Plans**: 1 (Q1 2025)
- **Campaigns**: 2
- **Channels**: 4
- **Tools**: 5
- **Content Templates**: 2
- **Milestones**: 4
- **Analytics Setups**: 3
- **Total Budget**: $10,000
- **Duration**: Jan 15 - Mar 31, 2025 (11 weeks)

**Key Metrics**:
- Target GitHub Stars: 500
- Target Email Subscribers: 1,000
- Target Website Visits: 50,000
- Estimated ROI: 5x

**Validation**: ✅ All checks passed (40/40)

**Next Steps**:
1. Review specification → Open marketing-spec.yaml
2. Validate quality → `/marketspec.checklist`
3. Analyze consistency → `/marketspec.analyze`
4. Begin execution → Follow campaign plans

Would you like me to:
- Generate a human-readable summary?
- Export to JSON format?
- Run quality checklist?
```

---

## Notes

- **Single source of truth**: This YAML is the authoritative specification
- **Version control**: Commit to git for tracking changes
- **Iterative**: Can regenerate as source documents evolve
- **Extensible**: Easy to add custom fields for specific needs
- **Tool-friendly**: YAML format works with many tools
- **Human-readable**: Can be edited manually if needed
- **Validated**: All data integrity checks ensure quality

---

## Integration with Other Commands

Feeds into:
- `/marketspec.checklist` - Validates the generated spec
- `/marketspec.analyze` - Analyzes consistency and quality

References:
- `/marketspec.discover` - Source of project and objectives
- `/marketspec.clarify` - Source of refined requirements
- `/marketspec.strategy` - Source of campaigns and channels
- `/marketspec.tasks` - Source of milestones and timeline
- `/marketspec.constitution` - Validation criteria

---

## See Also

- `/marketspec.tasks` - Previous step
- `/marketspec.checklist` - Next step (quality validation)
- `/marketspec.analyze` - Consistency analysis
- Domain Specification: `specs/domain/001-marketing-operations-spec/spec.md`
- YAML templates in `templates/sdm/templates/`
- Example specifications in `examples/` directory
