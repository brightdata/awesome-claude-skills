# Spec-Driven Development with Research Intelligence

A comprehensive skill for Claude that implements **research-enhanced spec-driven development** using Bright Data's MCP tools to generate specifications grounded in real-world data, competitive analysis, and architectural best practices.

## Overview

Traditional "vibe-coding" often produces code that looks right but doesn't quite work. This skill takes a different approach: **start with a clear specification**, backed by research, then let that spec drive everything else.

### The Four-Phase Process

```
SPECIFY → PLAN → TASKS → IMPLEMENT
   ↓        ↓       ↓         ↓
Research  Tech   Break    Execute
+ User    Stack  Down     + Test
Intent    Choice Tasks    + Deploy
```

Each phase has **validation checkpoints** before moving forward.

## What Makes This Different?

Traditional spec-driven development writes specs in isolation. This skill uses **Bright Data MCP tools** to:

- **Research documentation** before choosing technologies
- **Analyze competitors** to understand what works (and what doesn't)
- **Extract user pain points** from reviews and forums
- **Find reference implementations** from successful projects
- **Validate architectural decisions** with real-world examples
- **Gather industry benchmarks** for performance targets

## Quick Start

### 1. Installation

This skill works with Claude Code and requires Bright Data MCP server.

```bash
# Navigate to your skills directory
cd custom_skills/spec-driven-development

# Install Python dependencies (for scripts)
pip install -r requirements.txt
```

### 2. Activate the Skill

When working on a new project or feature in Claude Code, say:

```
I want to use spec-driven development to build [your project]
```

Claude will automatically activate this skill and guide you through the process.

### 3. The Workflow

#### Phase 1: SPECIFY (with Research)

**You provide**: High-level description of what you're building

**Claude does**:
1. Asks clarifying questions about user intent
2. Uses Bright Data to research:
   - Similar products and features
   - User reviews to find pain points
   - Documentation for mentioned technologies
   - Real-world examples
3. Generates `SPECIFICATION.md` enriched with research

**Example Research Commands Claude Will Use**:
```python
# Find competitor approaches
BrightData:search_engine(
    query="best photo sharing apps features 2025",
    engine="google"
)

# Analyze user pain points
BrightData:web_data_google_play_store(
    url="https://play.google.com/store/apps/details?id=competitor.app"
)

# Extract architecture patterns
BrightData:web_data_github_repository_file(
    url="https://github.com/user/reference-project/blob/main/architecture.md"
)
```

**Validation**: Review spec for accuracy, gaps, and research-backed insights

#### Phase 2: PLAN (with Technical Research)

**You provide**: Technology preferences and constraints

**Claude does**:
1. Researches architectural patterns and best practices
2. Studies documentation for chosen technologies
3. Finds reference implementations
4. Generates `TECHNICAL_PLAN.md` with justified decisions

**Example Research Commands**:
```python
# Compare architecture patterns
BrightData:search_engine_batch(
    queries=[
        {"query": "microservices vs monolithic architecture 2025", "engine": "google"},
        {"query": "serverless architecture best practices", "engine": "google"}
    ]
)

# Get official documentation
BrightData:scrape_as_markdown(
    url="https://fastapi.tiangolo.com/deployment/concepts/"
)

# Study successful implementations
BrightData:web_data_crunchbase_company(
    url="https://www.crunchbase.com/organization/company-name"
)
```

**Validation**: Confirm technical approach and architectural decisions

#### Phase 3: TASKS (Automated Breakdown)

**Claude does**:
1. Runs `generate_tasks.py` to break down spec and plan
2. Creates concrete, testable tasks
3. Sequences tasks with dependencies
4. Generates `TASKS.md`

**You can also run manually**:
```bash
python scripts/generate_tasks.py \
  --spec SPECIFICATION.md \
  --plan TECHNICAL_PLAN.md \
  --output TASKS.md
```

**Validation**: Ensure tasks are small, clear, and testable

#### Phase 4: IMPLEMENT (Execution)

**Claude does**:
1. Works through tasks one-by-one
2. Validates against acceptance criteria
3. Updates spec/plan based on learnings
4. Creates focused, reviewable code changes

## Skill Features

### Automatic Research

Claude will proactively research:

| What | Bright Data Tools Used |
|------|------------------------|
| **Documentation** | `search_engine`, `scrape_as_markdown` |
| **Competitor Analysis** | `web_data_google_play_store`, `web_data_amazon_product` |
| **Code Examples** | `web_data_github_repository_file` |
| **User Feedback** | Product review tools, `web_data_reddit_posts` |
| **Company Intelligence** | `web_data_linkedin_company_profile`, `web_data_crunchbase_company` |
| **Architecture Patterns** | `scrape_batch` on multiple docs |

### Validation Scripts

**Validate Specification**:
```bash
python scripts/validate_spec.py --spec SPECIFICATION.md
```

Checks for:
- Required sections
- Measurable success metrics
- Clear acceptance criteria
- Research backing
- User journeys

**Generate Tasks**:
```bash
python scripts/generate_tasks.py \
  --spec SPECIFICATION.md \
  --plan TECHNICAL_PLAN.md
```

Produces:
- Small, testable tasks (<4 hours each)
- Clear acceptance criteria
- Dependency mapping
- Effort estimates

**Create Research Report**:
```bash
python scripts/research_report.py \
  --topic "microservices architecture" \
  --output research/microservices.md
```

Creates structured template for documenting research findings.

## Templates

All templates are fully populated with examples and guidance:

- **[SPECIFICATION_TEMPLATE.md](SPECIFICATION_TEMPLATE.md)** - User intent and requirements
- **[PLAN_TEMPLATE.md](PLAN_TEMPLATE.md)** - Technical architecture
- **[TASKS_TEMPLATE.md](TASKS_TEMPLATE.md)** - Implementation breakdown

## Example Usage Scenarios

### Scenario 1: Greenfield Project

```
User: "I want to build a task management app for remote teams"

Claude:
1. Researches existing task management tools (Asana, Trello, etc.)
2. Analyzes user reviews to find pain points
3. Studies collaboration features that work well
4. Generates SPECIFICATION.md with research-backed requirements
5. Proceeds through PLAN → TASKS → IMPLEMENT
```

### Scenario 2: New Feature

```
User: "Add real-time collaboration to my existing app"

Claude:
1. Researches real-time collaboration patterns
2. Studies WebSocket vs Server-Sent Events
3. Analyzes how Figma/Google Docs handle collaboration
4. Creates focused SPECIFICATION for just this feature
5. Integrates with existing architecture in TECHNICAL_PLAN
```

### Scenario 3: Legacy Modernization

```
User: "Migrate our monolith to microservices"

Claude:
1. Researches strangler fig pattern
2. Studies successful migration case studies
3. Analyzes current architecture
4. Creates phased SPECIFICATION
5. Generates migration PLAN with risk mitigation
```

## Research Patterns

### Pattern 1: Documentation Deep Dive

When user mentions a technology:

```python
# 1. Search for official docs
BrightData:search_engine(query="FastAPI official documentation", engine="google")

# 2. Scrape the docs
BrightData:scrape_as_markdown(url="https://fastapi.tiangolo.com/")

# 3. Incorporate into PLAN with proper citations
```

### Pattern 2: Competitive Intelligence

When building a feature similar to existing products:

```python
# 1. Find competitors
BrightData:search_engine(query="best photo sharing apps 2025", engine="google")

# 2. Analyze implementations
BrightData:web_data_google_play_store(url="...")
BrightData:web_data_apple_app_store(url="...")

# 3. Extract user pain points from reviews
# 4. Document in SPECIFICATION competitive analysis table
```

### Pattern 3: Architecture Research

When designing system architecture:

```python
# 1. Find reference implementations
BrightData:search_engine(query="Python microservices example GitHub", engine="google")

# 2. Study successful projects
BrightData:web_data_github_repository_file(url="...")

# 3. Extract patterns into TECHNICAL_PLAN
```

### Pattern 4: Batch Comparison

When comparing multiple approaches:

```python
# Research multiple architectures simultaneously
BrightData:scrape_batch(
    urls=[
        "https://docs.aws.amazon.com/lambda/",
        "https://cloud.google.com/functions/",
        "https://azure.microsoft.com/functions/"
    ]
)

# Create comparison table in TECHNICAL_PLAN
```

## Best Practices

### DO:

✅ **Research before specifying** - Use Bright Data to understand the problem space
✅ **Validate with real data** - Check reviews, docs, examples
✅ **Keep specs living** - Update as you learn
✅ **Break tasks small** - Each should be independently testable
✅ **Document research sources** - Link to scraped docs in spec
✅ **Iterate at each phase** - Don't skip validation checkpoints

### DON'T:

❌ **Skip research phase** - Don't guess when you can know
❌ **Write code before spec** - Resist the urge
❌ **Create mega-tasks** - Break down until each is <4 hours
❌ **Ignore user reviews** - They reveal real pain points
❌ **Copy blindly** - Understand WHY architectures work
❌ **Over-scrape** - Be targeted in your research

## Validation Checklists

### SPECIFY → PLAN Checklist

- [ ] User needs clearly articulated
- [ ] Research validates the problem exists
- [ ] Edge cases identified from real-world examples
- [ ] Success metrics defined
- [ ] Competitive analysis complete
- [ ] Run: `python scripts/validate_spec.py --spec SPECIFICATION.md`

### PLAN → TASKS Checklist

- [ ] Technology choices justified with research
- [ ] Architecture validated against best practices
- [ ] Integration points documented
- [ ] Performance targets researched
- [ ] Security considerations addressed

### TASKS → IMPLEMENT Checklist

- [ ] All tasks independently testable
- [ ] Dependencies properly sequenced
- [ ] Success criteria clear for each task
- [ ] Estimated complexity reasonable

## File Structure

```
spec-driven-development/
├── SKILL.md                      # Skill definition (Claude reads this)
├── README.md                     # This file
├── SPECIFICATION_TEMPLATE.md     # Template for user requirements
├── PLAN_TEMPLATE.md              # Template for technical architecture
├── TASKS_TEMPLATE.md             # Template for task breakdown
├── scripts/
│   ├── generate_tasks.py         # Auto-generate tasks from spec+plan
│   ├── validate_spec.py          # Validate specification completeness
│   └── research_report.py        # Template for research documentation
└── examples/
    └── photo-sharing/            # Complete example walkthrough
        ├── SPECIFICATION.md
        ├── TECHNICAL_PLAN.md
        ├── TASKS.md
        └── research/
            └── competitors.md
```

## Troubleshooting

### "The spec is too vague"
→ Use Bright Data to research similar implementations and enrich with concrete examples

### "I don't know what technology to choose"
→ Research multiple options with `scrape_batch`, compare in TECHNICAL_PLAN

### "Tasks are too large"
→ Run `generate_tasks.py` again or ask Claude to break down further

### "Implementation doesn't match spec"
→ Update spec based on learnings, regenerate tasks (specs are living documents!)

### "Research is taking too long"
→ Use `search_engine_batch` and `scrape_batch` for parallel research

## Integration with Development Workflow

### Git Workflow

```bash
# Start new feature with spec
git checkout -b feature/user-authentication

# Generate spec with Claude (uses this skill)
# Creates: SPECIFICATION.md, TECHNICAL_PLAN.md, TASKS.md

# Commit the specs
git add *.md
git commit -m "docs: add specification for user authentication"

# Implement tasks
# Claude works through TASKS.md

# Update specs as you learn
# Keep specs in sync with code
```

### CI/CD Integration

Add to your `.github/workflows/ci.yml`:

```yaml
- name: Validate Specification
  run: |
    python scripts/validate_spec.py --spec SPECIFICATION.md --strict
```

## Advanced Usage

### Custom Research Reports

Create detailed research documentation:

```bash
# Generate report template
python scripts/research_report.py \
  --topic "OAuth2 vs JWT authentication" \
  --output research/auth-comparison.md \
  --researcher "Your Name"

# Fill in with Bright Data research
# Link from SPECIFICATION.md
```

### Multi-Project Specs

For large projects, create separate specs per module:

```
project/
├── SPECIFICATION.md              # Overall project
├── modules/
│   ├── auth/
│   │   ├── SPECIFICATION.md      # Auth module spec
│   │   └── TECHNICAL_PLAN.md
│   └── api/
│       ├── SPECIFICATION.md
│       └── TECHNICAL_PLAN.md
```

### Iterative Refinement

Specs evolve:

```markdown
## Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-01-15 | Initial specification |
| 1.1 | 2025-01-20 | Added OAuth login after research |
| 2.0 | 2025-02-01 | Pivot to mobile-first based on user feedback |
```

## Resources

- **[Spec-Driven Development Guide](https://github.blog/engineering/developer-experience/spec-driven-development/)** - Original GitHub blog post
- **[Spec Kit](https://github.com/github/spec-kit)** - GitHub's official toolkit
- **[Bright Data MCP Documentation](https://brightdata.com/mcp)** - MCP tool reference

## Contributing

This skill is part of the awesome-claude-skills collection. To improve it:

1. Test the workflow on real projects
2. Share findings and edge cases
3. Suggest additional Bright Data research patterns
4. Contribute example projects

## License

See repository root LICENSE file.

---

## Quick Reference Card

### Phase Transitions

```
SPECIFY ──[validate_spec.py]──> PLAN ──[generate_tasks.py]──> TASKS ──> IMPLEMENT
```

### Key Commands

| Command | Purpose |
|---------|---------|
| `python scripts/validate_spec.py --spec SPECIFICATION.md` | Validate spec before PLAN |
| `python scripts/generate_tasks.py --spec SPECIFICATION.md --plan TECHNICAL_PLAN.md` | Generate tasks |
| `python scripts/research_report.py --topic "X" --output research/X.md` | Document research |

### Bright Data Quick Reference

| Use Case | Tool |
|----------|------|
| Search the web | `search_engine` |
| Get documentation | `scrape_as_markdown` |
| Batch scraping | `scrape_batch` |
| GitHub code | `web_data_github_repository_file` |
| App reviews | `web_data_google_play_store` |
| Company info | `web_data_linkedin_company_profile` |
| Competitor data | `web_data_crunchbase_company` |

---

**Ready to build better software through research-driven specifications?**

Start with: `"Claude, I want to use spec-driven development to build [your project]"`
