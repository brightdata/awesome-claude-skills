---
name: lead-research-assistant
description: Identifies and qualifies potential leads by analyzing products/services, understanding ideal customer profiles, conducting intelligent web research using Bright Data MCP tools, and providing actionable outreach strategies. Use when researching leads, prospecting, qualifying contacts, analyzing companies, enriching lead data, or creating outreach campaigns.
---

# Lead Research Assistant

This skill helps you identify, research, and qualify potential leads through intelligent web research and systematic analysis. It works with minimal input, asks clarifying questions when needed, and delivers comprehensive lead intelligence with personalized outreach strategies.

## Core Capabilities

1. **Intelligent Lead Discovery** - Find leads based on ICP criteria using smart search queries
2. **Deep Company Research** - Enrich company data using LinkedIn, Crunchbase, ZoomInfo, and web sources
3. **Contact Intelligence** - Identify and research key decision-makers and influencers
4. **Custom Qualification** - Score leads against your unique ICP criteria
5. **Batch Processing** - Process multiple leads efficiently from CSV/Excel files
6. **Outreach Strategy** - Generate personalized messaging based on research insights
7. **Excel Reporting** - Create professional reports with enriched data and recommendations

## Quick Start Workflow

### Single Lead Research

When a user provides minimal information about a lead, follow this workflow:

1. **Gather Context** - Ask clarifying questions if needed (see [Clarifying Questions](#clarifying-questions))
2. **Smart Search** - Use Google search with intelligent queries to find initial data
3. **Deep Enrichment** - Use appropriate Bright Data MCP tools based on findings
4. **Qualify Lead** - Score against ICP criteria using `scripts/lead_qualification.py`
5. **Generate Strategy** - Create personalized outreach recommendations
6. **Deliver Report** - Present findings in clear format (see [OUTREACH.md](OUTREACH.md) for templates)

### Batch Lead Processing

For multiple leads from a file:

1. **Load Data** - Accept CSV/Excel file with lead information
2. **Process Batch** - Use `python scripts/batch_processor.py` to enrich all leads
3. **Generate Report** - Use `python scripts/report_generator.py` to create Excel output
4. **Review Results** - Present summary with top-qualified leads highlighted

## Clarifying Questions

When a user provides minimal lead information, ask relevant questions to maximize research effectiveness:

### About the Product/Service
- "What product or service are you selling?"
- "What problem does it solve for customers?"
- "What's the typical price point or deal size?"
- "What's the sales cycle length (days/weeks/months)?"

### About the Ideal Customer Profile (ICP)
- "What industries or verticals do you target?"
- "What company size (employees/revenue) is ideal?"
- "What geographic regions do you focus on?"
- "Are there specific technologies or tools your ideal customers use?"
- "What are common characteristics of your best customers?"

### About the Lead
- "Do you have a company name, website, or LinkedIn profile?"
- "Do you have specific contact names or titles you're targeting?"
- "What triggered your interest in this lead? (funding event, hiring, product launch, etc.)"

### About Outreach Goals
- "What's your primary goal? (book meeting, start conversation, nurture relationship)"
- "What channels will you use? (email, LinkedIn, phone)"
- "Do you have any existing relationship or warm introduction path?"

**Important**: Only ask questions that aren't already answered by the provided information. Be concise and ask 3-5 most relevant questions.

## Research Process

### Step 1: Initial Discovery with Google Search

Use Bright Data MCP's **mcp__bright-data:search_engine** to find initial information:

**Smart Search Strategies:**

```
For company LinkedIn profiles:
site:linkedin.com/company <company_name> OR <industry_keyword>

For contact LinkedIn profiles:
site:linkedin.com/in <person_name> <company_name> <job_title>

For company news and signals:
<company_name> (funding OR acquired OR launched OR hiring)

For technology stack:
site:stackshare.io <company_name> OR site:builtwith.com <company_name>

For company reviews/reputation:
<company_name> reviews OR <company_name> glassdoor

For industry research:
<industry> companies <location> <employee_size>
```

**Execute searches in parallel** when possible to gather comprehensive data quickly.

### Step 2: Deep Company Enrichment

Based on Step 1 findings, use appropriate Bright Data MCP tools:

#### LinkedIn Company Data
```
mcp__bright-data:web_data_linkedin_company_profile
- Company size, industry, location
- Employee count and growth trends
- Recent updates and posts
- Company description and specialties
```

#### Crunchbase Company Data
```
mcp__bright-data:web_data_crunchbase_company
- Funding history and investors
- Valuation and financial health signals
- Leadership team
- Technology categories
```

#### ZoomInfo Company Data
```
mcp__bright-data:web_data_zoominfo_company_profile
- Technographic data (tech stack)
- Contact information
- Revenue estimates
- Employee details
```

#### News and Market Intelligence
```
mcp__bright-data:web_data_reuter_news
- Recent news mentions
- Market positioning
- Industry trends
```

**Decision Logic**:
- If LinkedIn URL found → Always use web_data_linkedin_company_profile
- If Crunchbase URL found → Use web_data_crunchbase_company (especially for startups/tech)
- If available → Use web_data_zoominfo_company_profile for technographics
- For public companies → Check Reuters news for recent developments

### Step 3: Contact Intelligence

Once you've identified the company, find key decision-makers:

#### LinkedIn People Search
```
mcp__bright-data:web_data_linkedin_people_search
- Search for decision-makers by title
- Common titles: CEO, CTO, VP Sales, Director of Marketing, Head of Operations
```

#### LinkedIn Person Profile
```
mcp__bright-data:web_data_linkedin_person_profile
- Professional background and experience
- Education and skills
- Recent activity and posts
- Connections and mutual contacts (if visible)
```

#### Social Media Presence (when relevant)
```
mcp__bright-data:web_data_x_posts
- Thought leadership content
- Professional interests and priorities
- Communication style
```

**Prioritization**:
1. Economic buyer (budget authority)
2. Champion (internal advocate)
3. Influencers (technical/operational stakeholders)
4. End users (for bottom-up adoption plays)

### Step 4: Lead Qualification

Use the qualification script to score leads:

```bash
python scripts/lead_qualification.py --company-data company_data.json --icp-criteria icp_config.json
```

The script evaluates leads against custom ICP criteria including:
- **Firmographic fit** (industry, size, location, growth)
- **Technographic fit** (current tools, tech stack compatibility)
- **Behavioral signals** (hiring, funding, product launches)
- **Engagement potential** (social presence, content activity)

See [REFERENCE.md](REFERENCE.md) for detailed ICP framework and scoring methodology.

### Step 5: Outreach Strategy Development

Generate personalized outreach recommendations based on research:

1. **Pain Point Identification** - Match product value props to company challenges
2. **Personalization Hooks** - Find relevant news, posts, or company initiatives
3. **Messaging Angle** - Recommend approach (problem-solution, case study, insight-driven)
4. **Channel Selection** - Suggest best outreach channel based on contact behavior
5. **Timing Recommendations** - Identify optimal timing based on business events

See [OUTREACH.md](OUTREACH.md) for templates and examples.

## Batch Processing Workflow

For processing multiple leads from CSV/Excel files:

### Input File Format

Your CSV/Excel should include at minimum:
- `company_name` (required)
- `website` (optional but recommended)
- `linkedin_url` (optional)
- `contact_name` (optional)
- `contact_title` (optional)
- `industry` (optional)
- `notes` (optional)

**Example CSV:**
```csv
company_name,website,linkedin_url,contact_name,contact_title,industry
Acme Corp,acme.com,linkedin.com/company/acme,John Smith,VP Sales,SaaS
TechStart Inc,techstart.io,,Jane Doe,CEO,Technology
```

### Batch Processing Steps

1. **Load and Validate**
```bash
python scripts/batch_processor.py --input leads.csv --validate-only
```

2. **Enrich Leads** (processes all leads with intelligent tool selection)
```bash
python scripts/batch_processor.py --input leads.csv --output enriched_leads.json --parallel 5
```

Parameters:
- `--input`: Path to CSV/Excel file
- `--output`: Path for JSON output with enriched data
- `--parallel`: Number of concurrent API calls (default: 3, max: 10)
- `--icp-config`: Optional path to ICP criteria JSON file
- `--validate-only`: Check file format without processing

3. **Generate Excel Report**
```bash
python scripts/report_generator.py --input enriched_leads.json --output lead_report.xlsx --template summary
```

Parameters:
- `--input`: Path to enriched JSON data
- `--output`: Path for Excel report
- `--template`: Report template (summary, detailed, executive)
- `--top-n`: Number of top leads to highlight (default: 10)

The generated Excel report includes:
- **Summary Sheet**: Top-qualified leads with key metrics
- **All Leads Sheet**: Complete lead list with enrichment data
- **Qualification Sheet**: ICP scoring breakdown
- **Outreach Sheet**: Personalized messaging recommendations
- **Insights Sheet**: Patterns and trends analysis

## Error Handling and Edge Cases

### Missing Data
- If company website not found → Use LinkedIn company search
- If LinkedIn not available → Fall back to general web search + Crunchbase
- If no contact information → Provide guidance for LinkedIn Sales Navigator search

### API Rate Limits
- Implement exponential backoff for rate limit errors
- Batch processing automatically spaces requests
- Progress saved incrementally to allow resume after interruption

### Data Quality Issues
- Flag leads with low confidence scores (< 60%)
- Highlight missing critical data points
- Suggest manual verification steps when needed

## Integration with Bright Data MCP Tools

This skill is optimized to use Bright Data MCP tools efficiently:

### Primary Tools by Use Case

| Use Case | Primary Tool | Secondary Tool |
|----------|--------------|----------------|
| Company research | `web_data_linkedin_company_profile` | `web_data_crunchbase_company` |
| Contact research | `web_data_linkedin_person_profile` | `web_data_linkedin_people_search` |
| Market intelligence | `search_engine` (Google) | `web_data_reuter_news` |
| Tech stack | `web_data_zoominfo_company_profile` | `search_engine` |
| Social presence | `web_data_x_posts` | `web_data_linkedin_posts` |
| Reputation | `web_data_google_maps_reviews` | `search_engine` |

### Tool Selection Logic

```python
# Use this decision tree in scripts
if linkedin_company_url:
    use web_data_linkedin_company_profile

if company_is_startup or tech_company:
    use web_data_crunchbase_company

if need_tech_stack or contact_info:
    use web_data_zoominfo_company_profile

if need_decision_makers:
    use web_data_linkedin_people_search
    then web_data_linkedin_person_profile for top matches

if need_recent_signals:
    use search_engine with news queries
    optionally use web_data_reuter_news for public companies
```

## Best Practices

1. **Always start with minimal searches** - Use Google search to find URLs before calling specialized tools
2. **Parallel processing** - Fetch company and contact data simultaneously when possible
3. **Progressive enrichment** - Gather basic data first, then enrich high-scoring leads deeper
4. **Respect rate limits** - Space API calls appropriately in batch processing
5. **Validate data quality** - Cross-reference data points across multiple sources
6. **Document assumptions** - Flag inferred data vs. confirmed facts
7. **Privacy compliance** - Only gather publicly available information
8. **Human review** - Always recommend human verification for high-value leads

## Example: Complete Lead Research

**Input**: "Research Stripe as a potential lead for our API testing platform"

**Workflow**:

1. **Clarify Context** (if needed)
   - Ask about ICP criteria if not previously defined
   - Ask about specific contacts or departments to target

2. **Initial Search**
   ```
   mcp__bright-data:search_engine
   Query: "site:linkedin.com/company stripe"
   → Find LinkedIn company URL
   ```

3. **Company Enrichment**
   ```
   mcp__bright-data:web_data_linkedin_company_profile
   URL: linkedin.com/company/stripe
   → Get company size, industry, recent posts

   mcp__bright-data:web_data_crunchbase_company
   URL: crunchbase.com/organization/stripe
   → Get funding, valuation, investors
   ```

4. **Contact Research**
   ```
   mcp__bright-data:web_data_linkedin_people_search
   Search: "Head of Engineering" at Stripe
   → Identify key technical decision-makers

   mcp__bright-data:web_data_linkedin_person_profile
   → Enrich top 3 contacts with detailed profiles
   ```

5. **Market Intelligence**
   ```
   mcp__bright-data:search_engine
   Query: "Stripe API testing tools engineering blog"
   → Find technical content and pain points
   ```

6. **Qualification**
   - Company size: ✓ Enterprise (high fit)
   - Industry: ✓ Fintech/Payments (target vertical)
   - Tech stack: ✓ API-first company (perfect fit)
   - Growth signals: ✓ Expanding engineering team
   - **Overall Score: 92/100 (A-tier lead)**

7. **Outreach Strategy**
   - **Angle**: Technical credibility - reference Stripe's API-first approach
   - **Hook**: Recent engineering blog post about testing challenges
   - **Channel**: LinkedIn → Email follow-up
   - **Message**: Problem-solution focused on API reliability at scale
   - **CTA**: Offer case study from similar fintech company

8. **Output**
   - Comprehensive lead profile with all data points
   - Top 3 contacts with personalized messaging for each
   - Recommended outreach sequence (3-touch cadence)
   - Risk factors and objections to prepare for

## Progressive Disclosure

For complex topics, reference these additional files:

- **[REFERENCE.md](REFERENCE.md)** - ICP framework, qualification criteria, scoring methodology
- **[OUTREACH.md](OUTREACH.md)** - Message templates, channel strategies, cadence recommendations
- **README.md** - Setup instructions, configuration, troubleshooting

## Scripts Reference

### lead_qualification.py
Scores leads against ICP criteria with customizable weightings.

**Usage:**
```bash
python scripts/lead_qualification.py \
  --company-data company.json \
  --icp-criteria icp_config.json \
  --output scores.json
```

### batch_processor.py
Processes multiple leads with parallel API calls and progress tracking.

**Usage:**
```bash
python scripts/batch_processor.py \
  --input leads.csv \
  --output enriched.json \
  --parallel 5 \
  --icp-config icp.json
```

### report_generator.py
Creates professional Excel reports with formatting and charts.

**Usage:**
```bash
python scripts/report_generator.py \
  --input enriched.json \
  --output report.xlsx \
  --template detailed \
  --top-n 20
```

### lead_enrichment.py
Single-lead enrichment with intelligent tool selection.

**Usage:**
```bash
python scripts/lead_enrichment.py \
  --company-name "Acme Corp" \
  --website "acme.com" \
  --output acme_data.json
```

## Tips for Success

- **Quality over quantity**: Better to deeply research 10 high-fit leads than superficially research 100
- **Customize ICP criteria**: Spend time defining accurate qualification criteria upfront
- **Iterate on messaging**: Test different outreach angles and track what works
- **Track sources**: Always note where data came from for verification
- **Respect privacy**: Only use publicly available information ethically
- **Keep learning**: Update ICP criteria based on which leads convert

---

**Ready to start researching leads?** Provide a company name or upload a CSV file, and I'll begin the intelligent research process!
