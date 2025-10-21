# Lead Qualification Reference Guide

This document provides detailed guidance on the ICP (Ideal Customer Profile) framework, qualification criteria, and scoring methodology used by the Lead Research Assistant skill.

## Table of Contents

- [ICP Framework Overview](#icp-framework-overview)
- [Qualification Dimensions](#qualification-dimensions)
- [Scoring Methodology](#scoring-methodology)
- [Customizing ICP Criteria](#customizing-icp-criteria)
- [Industry-Specific ICP Examples](#industry-specific-icp-examples)
- [Lead Tier Definitions](#lead-tier-definitions)
- [Data Sources and Signals](#data-sources-and-signals)

---

## ICP Framework Overview

The Lead Research Assistant uses a **four-dimensional qualification framework** to evaluate leads:

| Dimension | Weight | Focus |
|-----------|--------|-------|
| **Firmographic** | 35% | Company characteristics (size, revenue, industry, location) |
| **Technographic** | 25% | Technology adoption and digital maturity |
| **Behavioral** | 25% | Growth signals and buying intent indicators |
| **Strategic** | 15% | Deal potential and competitive positioning |

This weighted approach ensures comprehensive evaluation while prioritizing company fit characteristics.

---

## Qualification Dimensions

### 1. Firmographic Criteria (35% weight)

Evaluates fundamental company characteristics that indicate fit.

#### Company Size (30% of firmographic)

| Segment | Employee Range | Score | Best For |
|---------|---------------|-------|----------|
| Enterprise | 1,000+ | 100 | Complex solutions, high-touch sales |
| Mid-Market | 200-999 | 80 | Scalable solutions, solution sales |
| SMB | 50-199 | 60 | Self-service products, inside sales |
| Startup | 10-49 | 40 | Early-stage tools, PLG models |
| Micro | 1-9 | 20 | Solopreneur tools, low-touch |

**When to adjust**:
- If you sell enterprise software → increase weight and minimum threshold
- If you have PLG motion → give higher scores to smaller companies

#### Revenue (25% of firmographic)

| Range | Annual Revenue | Score | Budget Signal |
|-------|---------------|-------|---------------|
| Large | $100M+ | 100 | Enterprise budgets |
| Medium | $10M-$99M | 80 | Established budgets |
| Small | $1M-$9M | 60 | Growing budgets |
| Micro | <$1M | 30 | Limited budgets |

**Data sources**: Crunchbase, ZoomInfo, LinkedIn, public financials

#### Industry Match (25% of firmographic)

Evaluates vertical alignment with your solution.

**Scoring approach**:
- **Exact match** (100 points): Lead's industry is in your target list
- **Adjacent match** (60 points): Related industry with similar use cases
- **Other** (20 points): Industry not typically served

**Example target industries** (B2B SaaS):
- Technology & Software
- SaaS & Cloud Services
- Fintech & Financial Services
- E-commerce & Retail Tech
- Healthcare Technology
- Marketing & Advertising Tech

**Customization**: Replace with your specific verticals

#### Geographic Match (20% of firmographic)

Evaluates location alignment with your go-to-market strategy.

**Scoring**:
- **Target region** (100 points): North America, Europe, APAC
- **Other regions** (50 points): May have timezone, language, or regulatory challenges

**Adjust based on**:
- Regulatory requirements (GDPR, data residency)
- Language support capabilities
- Timezone coverage for support
- Payment processing availability

---

### 2. Technographic Criteria (25% weight)

Assesses technology adoption and digital sophistication.

#### Tech Stack Compatibility (50% of technographic)

Evaluates whether the lead uses complementary or compatible technologies.

**Compatible technologies** (default list):
- Cloud platforms: AWS, Azure, GCP
- Container orchestration: Kubernetes, Docker
- Languages/frameworks: Python, Node.js, React, Java
- Data platforms: PostgreSQL, MongoDB, Snowflake, Databricks
- Developer tools: GitHub, GitLab, CircleCI, Datadog

**Scoring**: 15 points per matching technology (max 100)

**Data sources**:
- ZoomInfo technographics
- BuiltWith / StackShare
- GitHub organization repositories
- Job postings mentioning specific tools

**Why this matters**:
- Integration compatibility
- Technical sophistication indicator
- Developer-friendly culture signal
- Implementation complexity predictor

#### Digital Maturity (50% of technographic)

Evaluates overall digital transformation level.

| Indicator | Points | What It Signals |
|-----------|--------|-----------------|
| Has public API | 25 | API-first mindset, technical capability |
| Has mobile app | 20 | Omnichannel strategy, user experience focus |
| Cloud infrastructure | 25 | Modern architecture, scalability focus |
| Modern tech stack | 30 | Technical currency, innovation orientation |

**Total possible**: 100 points

**Assessment approach**:
- Review company website for API documentation
- Check app stores for mobile presence
- Analyze job postings for cloud technologies
- Examine engineering blog posts

---

### 3. Behavioral Criteria (25% weight)

Identifies growth momentum and buying intent.

#### Growth Signals (40% of behavioral)

Indicates company is in growth mode and may need new solutions.

| Signal | Points | Data Source |
|--------|--------|-------------|
| Recent funding | 30 | Crunchbase, press releases |
| Hiring actively | 25 | LinkedIn jobs, job boards |
| Product launch | 20 | News, company blog, Product Hunt |
| Market expansion | 25 | Press releases, LinkedIn posts |

**Why these matter**:
- **Funding** → Budget available, growth mandate
- **Hiring** → Scaling pains, need for tools
- **Product launch** → Need for supporting infrastructure
- **Expansion** → New requirements emerging

**How to detect**:
- Google News search for company
- LinkedIn company posts and job listings
- Crunchbase funding updates
- Product Hunt launches

#### Buying Intent (35% of behavioral)

Signals active evaluation or need for your solution category.

| Signal | Points | How to Detect |
|--------|--------|---------------|
| Job postings relevant to your category | 35 | Job board APIs, LinkedIn jobs |
| Technology investment signals | 30 | Hiring for related roles, new tech stack |
| Competitive tool switch indicators | 20 | Reviews mentioning switching, job posts for "replacement" |
| Pain point mentioned publicly | 15 | Social media, forums, review sites |

**Example**: If you sell API testing tools:
- Job posting for "API Quality Engineer" = 35 points
- Blog post about API reliability challenges = 15 points
- G2 review complaining about current tool = 20 points

#### Engagement Potential (25% of behavioral)

Assesses likelihood of responding to outreach.

| Signal | Points | Platform |
|--------|--------|----------|
| Active social media | 20 | LinkedIn, Twitter/X |
| Publishing content | 30 | Blog, LinkedIn articles |
| Event participation | 25 | Conference speaking, webinars |
| Thought leadership | 25 | Podcasts, industry publications |

**High engagement companies**:
- Respond faster to outreach
- More receptive to partnerships
- Better cultural fit for modern tools
- Easier to build relationships with

---

### 4. Strategic Criteria (15% weight)

Evaluates sales opportunity quality and competitive dynamics.

#### Deal Potential (50% of strategic)

Assesses likelihood of successful deal closure.

| Factor | Points | What to Look For |
|--------|--------|------------------|
| Budget signals | 30 | Recent funding, profitability indicators, purchase history |
| Decision timeline indicators | 25 | Hiring urgency, project deadlines, quarter-end timing |
| Authority access | 25 | Ability to reach decision-makers via LinkedIn/email |
| Economic buyer identified | 20 | CFO/CEO for budget, VP for operational decisions |

**BANT Framework alignment**:
- **Budget**: Evidence of financial capacity
- **Authority**: Access to decision-makers
- **Need**: Clear pain point or opportunity
- **Timeline**: Urgency or event-driven timing

#### Competitive Position (50% of strategic)

Evaluates competitive landscape and switching likelihood.

| Factor | Points | Assessment |
|--------|--------|------------|
| No incumbent solution | 35 | Greenfield opportunity - easiest to win |
| Weak incumbent | 25 | Low satisfaction, outdated solution |
| Low switching cost | 20 | Easy migration, no data lock-in |
| Clear competitive advantage | 20 | Unique features they need |

**How to assess**:
- G2/Capterra reviews mentioning competitors
- Job postings listing current tools
- LinkedIn profiles showing tool experience
- BuiltWith / StackShare data

---

## Scoring Methodology

### Overall Score Calculation

```
Total Score =
  (Firmographic Score × 0.35) +
  (Technographic Score × 0.25) +
  (Behavioral Score × 0.25) +
  (Strategic Score × 0.15)
```

### Tier Assignment

| Tier | Score Range | Priority | Action |
|------|-------------|----------|--------|
| **A** | 80-100 | Highest | Immediate personalized outreach, executive engagement |
| **B** | 60-79 | High | Tailored messaging, multi-touch sequence |
| **C** | 40-59 | Medium | Nurture campaign, monitor for triggers |
| **D** | 0-39 | Low | Passive monitoring, wait for signals |

### Confidence Scoring

Each lead also receives a **confidence score** based on data completeness:

| Data Completeness | Confidence | Reliability |
|-------------------|------------|-------------|
| LinkedIn + Crunchbase + ZoomInfo | 90-100% | Very high |
| LinkedIn + one other source | 70-89% | High |
| LinkedIn only | 50-69% | Medium |
| Generic web search only | 30-49% | Low |
| Minimal data | <30% | Very low |

**Best practice**: Only act on leads with >60% confidence score

---

## Customizing ICP Criteria

### Creating Custom ICP Config

Create a JSON file with your specific criteria:

```json
{
  "firmographic": {
    "weight": 0.40,
    "criteria": {
      "company_size": {
        "weight": 0.35,
        "ranges": {
          "enterprise": {"min": 500, "max": null, "score": 100},
          "mid_market": {"min": 100, "max": 499, "score": 70},
          "smb": {"min": 20, "max": 99, "score": 40}
        }
      },
      "industry_match": {
        "weight": 0.30,
        "target_industries": [
          "Healthcare Technology",
          "Medical Devices",
          "Biotech"
        ],
        "score_match": 100,
        "score_adjacent": 50,
        "score_other": 10
      },
      "geographic_match": {
        "weight": 0.20,
        "target_regions": ["United States", "Canada"],
        "score_match": 100,
        "score_other": 30
      }
    }
  }
}
```

**Use with qualification script**:
```bash
python scripts/lead_qualification.py \
  --company-data lead.json \
  --icp-criteria custom_icp.json
```

### Common Customization Scenarios

#### Enterprise-Only Sales
- Increase firmographic weight to 45%
- Set minimum employee count to 1,000
- Increase revenue minimum to $100M
- Add "enterprise sales cycle" to strategic criteria

#### Product-Led Growth (PLG)
- Decrease firmographic weight to 20%
- Increase technographic weight to 35%
- Prioritize digital maturity and modern tech stack
- Lower employee count thresholds (10-50 range)

#### Industry-Specific Solution
- Increase industry_match weight to 40% of firmographic
- Define narrow target_industries list
- Add industry-specific behavioral signals
- Include regulatory compliance as criterion

#### Geographic-Constrained
- Add specific countries to target_regions
- Include data residency requirements
- Account for language support
- Consider timezone overlap for support

---

## Industry-Specific ICP Examples

### B2B SaaS (Enterprise)

**Ideal Profile**:
- 500+ employees
- $50M+ revenue
- Technology, Financial Services, or Healthcare industry
- Uses modern cloud infrastructure
- Active hiring for engineering/product roles
- Strong digital presence and content marketing

**Key signals**: Funding rounds, product launches, API documentation

### Developer Tools

**Ideal Profile**:
- 50-500 employees
- $5M-$50M revenue
- Technology/Software industry
- Modern tech stack (cloud, containers, CI/CD)
- Active on GitHub, high engineering blog activity
- Attending/speaking at developer conferences

**Key signals**: Open source activity, engineering blog posts, conference presence

### Marketing Technology

**Ideal Profile**:
- 100-1,000 employees
- $10M-$100M revenue
- E-commerce, SaaS, Media industries
- Multiple marketing tools in stack
- Content-heavy website
- Active social media presence

**Key signals**: Marketing team hiring, content volume, social engagement

### Fintech Solutions

**Ideal Profile**:
- 200+ employees
- $20M+ revenue
- Financial Services, Banking, Payments
- Cloud infrastructure, API-first
- Recent funding or regulatory approval
- Strong compliance/security posture

**Key signals**: Regulatory announcements, funding, partnership news

---

## Lead Tier Definitions

### A-Tier Leads (80-100 points)

**Characteristics**:
- Perfect firmographic fit
- Strong behavioral signals (growth, intent)
- Clear decision-maker access
- Favorable competitive landscape

**Recommended actions**:
1. Deep research on decision-makers
2. Personalized multi-channel outreach
3. Executive-level engagement
4. Custom demo/POC preparation
5. Fast response to inquiries

**Expected conversion**: 15-25%

**Sales cycle**: 30-90 days

### B-Tier Leads (60-79 points)

**Characteristics**:
- Good firmographic fit
- Some behavioral signals present
- Decision-maker access possible
- May have incumbent solution

**Recommended actions**:
1. Tailored email sequences (3-5 touches)
2. LinkedIn connection + engagement
3. Educational content sharing
4. Webinar invitations
5. Periodic check-ins

**Expected conversion**: 8-15%

**Sales cycle**: 60-120 days

### C-Tier Leads (40-59 points)

**Characteristics**:
- Moderate fit on some dimensions
- Limited behavioral signals
- Unclear decision-maker access
- May lack budget indicators

**Recommended actions**:
1. Add to nurture email campaigns
2. Share valuable content monthly
3. Monitor for trigger events
4. Engage on social media
5. Invite to low-commitment events

**Expected conversion**: 3-8%

**Sales cycle**: 90-180 days

### D-Tier Leads (0-39 points)

**Characteristics**:
- Poor firmographic fit
- No behavioral signals
- Unknown decision-makers
- Strong incumbent or no budget

**Recommended actions**:
1. Passive monitoring only
2. Wait for major trigger events
3. Focus resources on A/B tiers
4. Revisit quarterly if signals change

**Expected conversion**: <3%

**Sales cycle**: 180+ days or never

---

## Data Sources and Signals

### Primary Data Sources

#### LinkedIn
- Company profiles (size, industry, location, employee count)
- People profiles (decision-makers, background)
- Job postings (hiring signals, tech stack mentions)
- Company posts (news, culture, initiatives)
- Employee activity (engagement signals)

**Bright Data MCP tools**:
- `web_data_linkedin_company_profile`
- `web_data_linkedin_person_profile`
- `web_data_linkedin_people_search`
- `web_data_linkedin_job_listings`
- `web_data_linkedin_posts`

#### Crunchbase
- Funding rounds and amounts
- Investors and valuations
- Leadership team
- Acquisition history
- Technology categories

**Bright Data MCP tools**:
- `web_data_crunchbase_company`

#### ZoomInfo
- Technographic data (tech stack)
- Contact information
- Revenue estimates
- Department headcounts
- Intent signals

**Bright Data MCP tools**:
- `web_data_zoominfo_company_profile`

#### Google Search
- Company news and press releases
- Blog posts and thought leadership
- Technology mentions
- Partnership announcements
- Customer testimonials

**Bright Data MCP tools**:
- `search_engine` (Google, Bing, Yandex)

#### News Sources
- Recent company developments
- Market positioning
- Industry trends
- Competitive moves

**Bright Data MCP tools**:
- `web_data_reuter_news`

### Behavioral Signal Detection

#### Growth Signals

**Recent Funding**:
- Crunchbase funding updates
- Press release searches
- LinkedIn company announcements

**Hiring Activity**:
- LinkedIn job postings count
- Job board aggregators
- LinkedIn employee count trends

**Product Launches**:
- Product Hunt launches
- Company blog announcements
- TechCrunch coverage

**Market Expansion**:
- New office announcements
- Geographic job postings
- Partnership press releases

#### Intent Signals

**Technology Investment**:
- Job postings for technical roles
- Engineering team growth
- New tech stack mentions

**Active Evaluation**:
- G2/Capterra review activity
- Comparison blog posts
- RFP/RFI documents (if available)

**Pain Point Expression**:
- Social media complaints
- Forum discussions
- Review site feedback

### Engagement Signals

**Social Media Activity**:
- LinkedIn post frequency
- Twitter/X engagement
- Response rates to mentions

**Content Creation**:
- Blog post frequency
- Technical documentation
- Case studies published

**Community Participation**:
- Conference speaking
- Webinar hosting
- Open source contributions

---

## Best Practices

### Data Quality
1. **Cross-reference** data across multiple sources
2. **Flag** inferred vs. confirmed data points
3. **Update** lead data quarterly or when signals change
4. **Document** assumptions made during scoring

### Qualification Process
1. **Start broad**, then narrow based on tier
2. **Prioritize** A/B-tier leads for deep research
3. **Automate** C/D-tier leads into nurture streams
4. **Review** ICP criteria monthly based on conversion data

### Scoring Calibration
1. **Track** actual conversion rates by tier
2. **Adjust** weights based on what predicts wins
3. **Validate** with sales team on lead quality
4. **Iterate** quarterly as market evolves

### Privacy & Compliance
1. **Use only** publicly available information
2. **Respect** opt-out requests immediately
3. **Comply** with GDPR, CCPA, and regional laws
4. **Document** data sources for audits

---

## Quick Reference: Scoring Cheat Sheet

| Dimension | Weight | Top Signals | Data Sources |
|-----------|--------|-------------|--------------|
| **Firmographic** | 35% | Employee count, revenue, industry | LinkedIn, Crunchbase, ZoomInfo |
| **Technographic** | 25% | Tech stack, cloud usage, APIs | ZoomInfo, BuiltWith, job posts |
| **Behavioral** | 25% | Funding, hiring, product launches | Crunchbase, LinkedIn, news |
| **Strategic** | 15% | Budget signals, decision-maker access | LinkedIn, reviews, intel |

**Minimum viable lead data**:
- Company name (required)
- Industry (highly recommended)
- Employee count or revenue (highly recommended)
- Website or LinkedIn URL (highly recommended)

**Optimal lead data**:
- All firmographic fields
- LinkedIn company + contact URLs
- Recent news/signals
- Technology stack information
- Decision-maker names and titles

---

**For outreach strategies and messaging templates, see [OUTREACH.md](OUTREACH.md)**
