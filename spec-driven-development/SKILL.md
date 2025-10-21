---
name: spec-driven-development
description: Generate comprehensive specifications for software projects using spec-driven development methodology. Leverages Bright Data MCP tools to research documentation, analyze competitor implementations, gather real-world examples, and enrich specs with architectural insights. Use when user requests specifications, technical plans, project specs, or architecture documentation.
---

# Spec-Driven Development with Research Intelligence

This skill implements a **research-enhanced spec-driven development process** that uses Bright Data's MCP tools to generate specifications grounded in real-world data, documentation research, and competitive analysis.

## When to Use This Skill

Use this skill when:
- User asks to create a specification or spec
- User mentions "spec-driven development" or "SDD"
- User wants to plan a new project or feature
- User needs architecture documentation
- User requests a technical plan
- User wants to research how competitors solve similar problems

## Core Principles

**Specification as Source of Truth**: The spec is a living, executable artifact that evolves with the project. It drives implementation, not the other way around.

**Research-Driven Clarity**: Before writing code, research how others solve similar problems. Use Bright Data tools to gather:
- Official documentation from technology providers
- Competitor implementations and patterns
- Real user reviews and pain points
- Industry best practices

**Progressive Refinement**: Start broad, then narrow with data. Each phase validates before moving forward.

## The Four-Phase Process

### Phase 1: SPECIFY (User Intent & Research)

**Goal**: Capture what you're building and why, enriched with research.

**Your Role**:
1. Interview the user about their intent
2. Use Bright Data MCP tools to research:
   - Similar products/features (competitive analysis)
   - User reviews to understand pain points
   - Documentation for technologies mentioned
   - Real-world examples

**Key Questions**:
- Who will use this?
- What problem does it solve?
- What outcomes matter?
- How will users interact with it?

**Research Tools to Use**:
- `BrightData:search_engine` - Find documentation, examples, tutorials
- `BrightData:scrape_as_markdown` - Extract full documentation pages
- `BrightData:web_data_github_repository_file` - Research open-source implementations
- `BrightData:web_data_linkedin_company_profile` - Understand competitor approaches
- Product-specific tools based on domain (e.g., `web_data_google_play_store` for mobile apps)

**Output**: `SPECIFICATION.md` - See [SPECIFICATION_TEMPLATE.md](SPECIFICATION_TEMPLATE.md)

**Validation Checkpoint**:
- Does the spec capture the actual user need?
- Are there gaps or edge cases identified from research?
- Have you validated assumptions with real-world data?

---

### Phase 2: PLAN (Technical Architecture & Stack Research)

**Goal**: Define HOW to build it, informed by best practices research.

**Your Role**:
1. Identify the technical stack and constraints
2. Research architectural patterns using Bright Data:
   - Official documentation for chosen technologies
   - Architecture examples from successful implementations
   - Integration patterns and best practices
   - Performance benchmarks from real deployments

**Key Inputs from User**:
- Technology stack preferences
- Constraints (compliance, performance, legacy systems)
- Integration requirements
- Team capabilities

**Research Tools to Use**:
- `BrightData:search_engine` - Find architecture guides, best practices
- `BrightData:scrape_as_markdown` - Extract technical documentation
- `BrightData:web_data_github_repository_file` - Study reference implementations
- `BrightData:web_data_crunchbase_company` - Research successful companies in space
- `BrightData:scrape_batch` - Gather multiple architecture docs at once

**Output**: `TECHNICAL_PLAN.md` - See [PLAN_TEMPLATE.md](PLAN_TEMPLATE.md)

**Validation Checkpoint**:
- Does the plan account for all constraints?
- Are architectural decisions backed by research?
- Can you generate multiple plan variations for comparison?

---

### Phase 3: TASKS (Breakdown & Prioritization)

**Goal**: Break specification and plan into actionable, testable tasks.

**Your Role**:
1. Decompose the plan into focused chunks
2. Each task should be:
   - Small enough to implement and test in isolation
   - Specific enough to validate completion
   - Sequenced to build incrementally

**Use**: `python scripts/generate_tasks.py` to create structured task breakdown

**Output**: `TASKS.md` - See [TASKS_TEMPLATE.md](TASKS_TEMPLATE.md)

**Validation Checkpoint**:
- Can each task be implemented independently?
- Is the success criterion clear?
- Are dependencies properly sequenced?

---

### Phase 4: IMPLEMENT (Execution with Validation)

**Goal**: Build the system task-by-task with continuous validation.

**Your Role**:
1. Tackle tasks one at a time (or in parallel where safe)
2. Validate each task against its success criteria
3. Update the spec/plan if you discover gaps

**Key Principle**: Review focused changes, not thousand-line dumps.

**Output**: Working code + tests

**Validation Checkpoint**:
- Does the implementation match the task requirements?
- Do tests validate the success criteria?
- Should the spec or plan be updated based on learnings?

---

## Bright Data Research Patterns

### Pattern 1: Documentation Research

When the user mentions a technology or framework:

```python
# 1. Search for official documentation
BrightData:search_engine(
    query="[technology] official documentation architecture guide",
    engine="google"
)

# 2. Extract the documentation pages
BrightData:scrape_as_markdown(
    url="https://docs.example.com/architecture"
)

# 3. Incorporate findings into PLAN
```

### Pattern 2: Competitive Analysis

When building a feature similar to existing products:

```python
# 1. Search for competitors
BrightData:search_engine(
    query="best [category] apps 2025",
    engine="google"
)

# 2. Analyze competitor implementations
BrightData:web_data_google_play_store(
    url="https://play.google.com/store/apps/details?id=competitor.app"
)

# 3. Read user reviews for pain points
BrightData:web_data_google_maps_reviews(
    url="https://maps.google.com/...",
    days_limit="30"
)

# 4. Document insights in SPECIFICATION
```

### Pattern 3: Architecture Examples

When designing system architecture:

```python
# 1. Find reference implementations
BrightData:search_engine(
    query="[framework] microservices architecture example github",
    engine="google"
)

# 2. Study successful implementations
BrightData:web_data_github_repository_file(
    url="https://github.com/user/repo/blob/main/architecture.md"
)

# 3. Extract patterns into TECHNICAL_PLAN
```

### Pattern 4: Batch Research

When you need to compare multiple approaches:

```python
# Research multiple architectures at once
BrightData:search_engine_batch(
    queries=[
        {"query": "monolithic vs microservices [domain]", "engine": "google"},
        {"query": "serverless architecture [domain]", "engine": "google"},
        {"query": "event-driven architecture [domain]", "engine": "google"}
    ]
)

# Or scrape multiple documentation pages
BrightData:scrape_batch(
    urls=[
        "https://docs.aws.com/lambda/",
        "https://cloud.google.com/functions/",
        "https://azure.microsoft.com/en-us/products/functions/"
    ]
)
```

### Pattern 5: Social Proof & Validation

When validating market assumptions:

```python
# LinkedIn company analysis
BrightData:web_data_linkedin_company_profile(
    url="https://linkedin.com/company/competitor"
)

# Product reviews
BrightData:web_data_amazon_product_reviews(
    url="https://amazon.com/dp/PRODUCT123"
)

# Social media sentiment
BrightData:web_data_reddit_posts(
    url="https://reddit.com/r/programming/comments/..."
)
```

---

## Complete Workflow Example

### Scenario: Building a Photo Sharing Feature

#### Step 1: SPECIFY with Research

**User Request**: "Add photo sharing to my app"

**Your Actions**:
1. Clarify intent through questions
2. Research existing photo sharing implementations:

```python
# Find popular photo sharing apps
BrightData:search_engine(
    query="best photo sharing apps 2025 features",
    engine="google"
)

# Analyze Instagram's approach
BrightData:web_data_instagram_profiles(
    url="https://instagram.com/popular_account"
)

# Check user pain points from app reviews
BrightData:web_data_google_play_store(
    url="https://play.google.com/store/apps/details?id=com.instagram.android"
)
```

3. Generate `SPECIFICATION.md` incorporating:
   - User journey (informed by research)
   - Key features (validated against competitors)
   - Pain points to avoid (from reviews)
   - Success metrics

#### Step 2: PLAN with Technical Research

**User Constraints**: "Use Python, must integrate with existing auth system"

**Your Actions**:
1. Research Python image processing libraries:

```python
BrightData:search_engine(
    query="python image upload best practices 2025",
    engine="google"
)

# Get official docs
BrightData:scrape_as_markdown(
    url="https://pillow.readthedocs.io/en/stable/"
)
```

2. Study storage solutions:

```python
BrightData:scrape_batch(
    urls=[
        "https://docs.aws.amazon.com/s3/",
        "https://cloud.google.com/storage/docs",
        "https://docs.cloudflare.com/r2/"
    ]
)
```

3. Generate `TECHNICAL_PLAN.md` with:
   - Architecture diagram
   - Technology choices (justified by research)
   - Integration points
   - Security considerations

#### Step 3: TASKS

Run task generator:
```bash
python scripts/generate_tasks.py --spec SPECIFICATION.md --plan TECHNICAL_PLAN.md
```

Produces `TASKS.md` with concrete, testable tasks.

#### Step 4: IMPLEMENT

Work through tasks one by one, validating against spec.

---

## Using the Scripts

### Generate Tasks
```bash
python scripts/generate_tasks.py \
  --spec SPECIFICATION.md \
  --plan TECHNICAL_PLAN.md \
  --output TASKS.md
```

### Validate Specification
```bash
python scripts/validate_spec.py --spec SPECIFICATION.md
```

### Research Report
```bash
python scripts/research_report.py \
  --topic "microservices architecture" \
  --output research/microservices.md
```

---

## Best Practices

### DO:
✅ **Research before specifying** - Use Bright Data to understand the problem space
✅ **Validate with real data** - Check user reviews, documentation, examples
✅ **Keep specs living** - Update as you learn
✅ **Break tasks small** - Each should be independently testable
✅ **Use batch operations** - When comparing multiple approaches
✅ **Document research sources** - Link to scraped docs in the spec
✅ **Iterate at each phase** - Don't move forward until validated

### DON'T:
❌ Skip research phase - Don't guess when you can know
❌ Write code before spec - Resist the urge to "just start coding"
❌ Create mega-tasks - Break down until each is <4 hours
❌ Ignore user reviews - They reveal real pain points
❌ Copy blindly - Understand WHY architectures work
❌ Over-scrape - Be targeted in your research
❌ Lock specs early - Embrace iteration

---

## MCP Tool Reference

### General Research
- `BrightData:search_engine` - Initial discovery
- `BrightData:scrape_as_markdown` - Documentation extraction
- `BrightData:scrape_batch` - Multiple docs at once
- `BrightData:search_engine_batch` - Parallel searches

### Code & Architecture
- `BrightData:web_data_github_repository_file` - Reference implementations
- `BrightData:web_data_linkedin_company_profile` - Company tech stacks

### Competitive Analysis
- `BrightData:web_data_google_play_store` - Mobile app analysis
- `BrightData:web_data_apple_app_store` - iOS app analysis
- `BrightData:web_data_amazon_product` - E-commerce features

### User Research
- Product review tools (Amazon, Google Play, Apple Store)
- `BrightData:web_data_reddit_posts` - Community discussions
- `BrightData:web_data_youtube_comments` - Video feedback

### Social & Business
- `BrightData:web_data_linkedin_*` - Professional insights
- `BrightData:web_data_crunchbase_company` - Funding & validation
- Social media tools for sentiment analysis

### Scraping Browser (Advanced)
For complex research requiring interaction:
- `BrightData:scraping_browser_navigate` - Navigate to pages
- `BrightData:scraping_browser_screenshot` - Capture UI patterns
- `BrightData:scraping_browser_get_text` - Extract dynamic content

---

## Validation Checklist

Before moving between phases:

**SPECIFY → PLAN**:
- [ ] User needs clearly articulated
- [ ] Research validates the problem exists
- [ ] Edge cases identified from real-world examples
- [ ] Success metrics defined
- [ ] Competitive analysis complete

**PLAN → TASKS**:
- [ ] Technology choices justified with research
- [ ] Architecture validated against best practices
- [ ] Integration points documented
- [ ] Performance targets researched
- [ ] Security considerations addressed

**TASKS → IMPLEMENT**:
- [ ] All tasks are independently testable
- [ ] Dependencies properly sequenced
- [ ] Success criteria clear for each task
- [ ] Estimated complexity reasonable

**IMPLEMENT → DONE**:
- [ ] All tasks completed
- [ ] Tests validate success criteria
- [ ] Documentation updated
- [ ] Spec reflects final implementation

---

## Troubleshooting

### "The spec is too vague"
→ Use Bright Data to research similar implementations and enrich with concrete examples

### "I don't know what technology to choose"
→ Research multiple options with `scrape_batch`, compare in TECHNICAL_PLAN

### "Tasks are too large"
→ Run `generate_tasks.py` again with `--granularity fine`

### "Implementation doesn't match spec"
→ Update spec based on learnings, regenerate tasks

### "Research is taking too long"
→ Use `search_engine_batch` and `scrape_batch` for parallel research

---

## Example Projects

See the `examples/` directory for complete walkthroughs:
- `examples/photo-sharing/` - Mobile feature with competitive analysis
- `examples/api-gateway/` - Microservices architecture research
- `examples/legacy-migration/` - Modernization with documentation mining

---

## Resources

- [Spec-Driven Development Guide](https://github.blog/engineering/developer-experience/spec-driven-development/)
- [Spec Kit Documentation](https://github.com/github/spec-kit)
- [Bright Data MCP Documentation](https://brightdata.com/mcp)

---

## Quick Start

1. **User asks to build something**
2. **Run**: Create `SPECIFICATION.md` with research
3. **Validate**: Review spec with user
4. **Run**: Create `TECHNICAL_PLAN.md` with architecture research
5. **Validate**: Confirm technical approach
6. **Run**: Generate `TASKS.md`
7. **Validate**: Verify task breakdown
8. **Implement**: Execute tasks with continuous validation

Remember: **Research → Specify → Plan → Task → Implement**

Each arrow is a validation checkpoint. Don't skip them.
