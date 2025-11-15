# Slash Command: /marketing.content.plan

## Purpose

Generate a content calendar for a campaign based on its goals, channels, and timeline.

## Command Usage

```
/marketing.content.plan <campaign_id>
```

## Prerequisites

- Campaign must exist in specification
- Campaign should have channels defined

## Execution Steps

### Step 1: Read Campaign Context

Load campaign details:
- Goal (awareness/consideration/conversion)
- Channels
- Timeline (start_date to end_date)
- Target audience
- Budget

### Step 2: Determine Content Strategy

Based on campaign goal:

**Awareness**: Focus on reach and impressions
- Content types: Announcements, tutorials, infographics
- Frequency: High (daily or every 2 days)
- Channels: Social media, blogs

**Consideration**: Focus on engagement and education
- Content types: Case studies, comparisons, webinars
- Frequency: Medium (2-3 times per week)
- Channels: Blog, email, video

**Conversion**: Focus on action and conversion
- Content types: Product demos, testimonials, offers
- Frequency: Targeted (weekly, high quality)
- Channels: Email, landing pages

### Step 3: Generate Content Calendar

For each channel, propose:
- **Cadence**: How often to post (daily/weekly)
- **Content Types**: What formats to use
- **Specific Entries**: Actual calendar items with dates

Rules:
- Distribute evenly across campaign period
- Start and end dates must be within campaign timeline
- Content types should match channel capabilities

### Step 4: Output Calendar

```yaml
content_calendar:
  - date: "2025-10-01"
    content_type: "announcement"
    channel_id: "twitter"
    title: "Product Launch Announcement"
    status: "planned"
  
  - date: "2025-10-03"
    content_type: "feature_highlight"
    channel_id: "twitter"
    title: "Feature Spotlight: Real-time Collaboration"
    status: "planned"
  
  - date: "2025-10-05"
    content_type: "tutorial"
    channel_id: "dev-to"
    title: "Getting Started in 5 Minutes"
    status: "planned"
  
  - date: "2025-10-08"
    content_type: "use_case"
    channel_id: "dev-to"
    title: "How Company X Uses Our Product"
    status: "planned"
  
  - date: "2025-10-10"
    content_type: "engagement"
    channel_id: "reddit"
    title: "AMA: Ask Me Anything About [Product]"
    status: "planned"
  
  - date: "2025-10-12"
    content_type: "tutorial"
    channel_id: "twitter"
    title: "Advanced Tips: Power User Workflows"
    status: "planned"
  
  - date: "2025-10-15"
    content_type: "case_study"
    channel_id: "dev-to"
    title: "Case Study: 10x Productivity Gains"
    status: "planned"
  
  - date: "2025-10-17"
    content_type: "announcement"
    channel_id: "twitter"
    title: "Week 3 Progress Update"
    status: "planned"
  
  - date: "2025-10-20"
    content_type: "summary"
    channel_id: "dev-to"
    title: "Launch Campaign Recap & What's Next"
    status: "planned"
```

```markdown
## Content Strategy Summary

**Campaign**: Q4 Product Launch Awareness Campaign
**Duration**: Oct 1-21, 2025 (21 days)
**Goal**: Awareness

### Channel Breakdown

#### Twitter (@your-product)
- **Frequency**: 3x per week (Mon/Wed/Fri)
- **Content Types**: Announcements, feature highlights, tips
- **Total Posts**: 9
- **Rationale**: High-frequency platform for real-time engagement

#### Dev.to
- **Frequency**: 1x per week (Thursdays)
- **Content Types**: Tutorials, case studies, deep dives
- **Total Posts**: 3
- **Rationale**: Long-form content for SEO and education

#### Reddit (r/programming, r/webdev)
- **Frequency**: 1x mid-campaign
- **Content Types**: AMA, discussion threads
- **Total Posts**: 1
- **Rationale**: Community engagement, authentic conversations

### Content Production Requirements

- **Total Pieces**: 13
- **Estimated Hours**: 65 hours (5 hrs/piece avg)
- **Required Skills**: Technical writing, design (for infographics)
- **Review Process**: Draft → Review → Approve → Schedule

### Success Metrics

- **Engagement Rate**: Target 3% (likes, comments, shares)
- **Click-Through Rate**: Target 2% to website
- **Content Coverage**: All 3 channels active throughout campaign

## Next Steps

1. Review calendar and adjust dates/content
2. Assign content creation to team members
3. Use /marketing.generate.post for each entry
4. Schedule with /marketing.execute.schedule
```

## Success Criteria

- Calendar spans entire campaign period
- Content frequency matches channel best practices
- Content types align with campaign goal
- All channels covered

## Example Interaction

```
User: /marketing.content.plan q4-awareness-launch

AI: Generating content calendar for 'q4-awareness-launch'...

Campaign: Oct 1-21 (21 days)
Goal: Awareness
Channels: Twitter, Dev.to, Reddit

[Displays YAML calendar + strategy summary]

📅 13 content pieces planned
📊 Breakdown: Twitter (9), Dev.to (3), Reddit (1)

Ready to start creating content?
```

