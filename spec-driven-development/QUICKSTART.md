# Quick Start Guide: Spec-Driven Development

Get started with research-enhanced spec-driven development in 5 minutes.

## What You'll Get

A structured process that uses **Bright Data research tools** to build better software:

```
Your Idea → Research → Spec → Plan → Tasks → Code
            ^^^^^^^^
         (The Secret Sauce)
```

## 30-Second Setup

1. Make sure Bright Data MCP is installed and configured in Claude Code
2. That's it! The skill activates automatically when you mention spec-driven development

## Your First Spec (5 Minutes)

### 1. Start a Conversation

In Claude Code, type:

```
I want to use spec-driven development to build a user authentication system
```

### 2. Claude Asks Questions

Claude will interview you about:
- Who will use this?
- What problem does it solve?
- What does success look like?

Answer naturally. Claude is gathering intent.

### 3. Claude Researches (Automatic)

While you wait, Claude uses Bright Data to:

```python
# Find best practices
BrightData:search_engine(
    query="authentication best practices 2025",
    engine="google"
)

# Study OAuth documentation
BrightData:scrape_as_markdown(
    url="https://oauth.net/2/"
)

# Analyze competitor approaches
BrightData:web_data_github_repository_file(
    url="https://github.com/auth0/node-auth0/blob/master/README.md"
)
```

**You don't need to do anything.** Claude handles all research automatically.

### 4. Review Specification

Claude generates `SPECIFICATION.md` with:
- ✅ Your requirements (from the interview)
- ✅ Competitive analysis (from research)
- ✅ User pain points (from reviews)
- ✅ Best practices (from documentation)
- ✅ Success metrics (from industry benchmarks)

**Your job**: Review and approve or request changes

### 5. Technical Plan

Claude asks about your tech stack:

```
User: "Use Python and PostgreSQL"

Claude: [Researches Python auth libraries, database security patterns]

Claude: "Here's your TECHNICAL_PLAN.md..."
```

**Your job**: Confirm the technical approach

### 6. Tasks Generated

Claude runs:
```bash
python scripts/generate_tasks.py
```

You get `TASKS.md` with 15-20 concrete tasks like:

```markdown
### Task 2.3: Implement Password Hashing

**Priority**: P0
**Estimated**: 45 minutes
**Dependencies**: Task 2.1

**Acceptance Criteria**:
- [ ] Uses bcrypt for hashing
- [ ] Salt is unique per password
- [ ] Unit tests written
- [ ] Test coverage >95%
```

### 7. Implementation

Claude works through tasks one-by-one, showing you progress:

```
✅ Task 1.1: Project setup - Done
✅ Task 1.2: Database configured - Done
🟡 Task 2.1: User model - In Progress...
```

## Real Example: 5-Minute Photo Upload Spec

Let's walk through a real example.

### Input (You Type This)

```
I need to add photo upload to my app. Users should be able to upload profile pictures.
```

### Claude's Research (Automatic)

```python
# 1. Find image upload best practices
BrightData:search_engine(query="image upload security best practices", engine="google")

# 2. Analyze how others do it
BrightData:web_data_github_repository_file(
    url="https://github.com/encode/starlette/blob/master/docs/static-files.md"
)

# 3. Check user pain points
BrightData:search_engine(query="image upload slow complaints", engine="google")
```

### Output (Generated in ~3 minutes)

**SPECIFICATION.md** includes:

```markdown
## Functional Requirements

### Must Have (P0)

1. **Image Upload**
   - Accept JPEG, PNG, WebP (research: most common formats)
   - Max 10MB (research: industry standard, balances quality and speed)
   - Validate dimensions <8000px (research: prevents DoS attacks)

   **Source**: OWASP file upload security guide [Link]

2. **Storage**
   - Store in S3 with signed URLs
   - Generate thumbnails automatically

   **Source**: AWS image handling best practices [Link]

## Competitive Analysis

| Competitor | Approach | Strength | Weakness |
|------------|----------|----------|----------|
| LinkedIn | Drag & drop | Intuitive | Slow for large files |
| Instagram | Instant upload | Fast feedback | Privacy confusion |

**Sources**: App reviews analysis via Bright Data
```

**TECHNICAL_PLAN.md** includes:

```markdown
## Technology Stack

| Component | Choice | Rationale | Research |
|-----------|--------|-----------|----------|
| Storage | AWS S3 | Industry standard, reliable | [S3 docs] |
| Processing | Pillow | Python-native, well-documented | [Pillow docs] |
| Validation | python-magic | Actual file type detection | [Security guide] |

**Alternatives Considered**:
- Google Cloud Storage: Rejected (cost for our scale)
- Local filesystem: Rejected (doesn't scale, backup complexity)

**Sources**: Cost comparison from AWS calculator, scaling analysis from [HackerNews thread]
```

### Time Breakdown

- Your input: 30 seconds
- Claude interview: 1 minute
- Claude research: 2 minutes (automatic, parallel)
- Your review: 1 minute
- **Total: ~5 minutes for a comprehensive spec**

Compare to traditional approach:
- Manual research: 2-3 hours
- Writing spec: 1-2 hours
- **Total: 3-5 hours**

**You save 95% of the time** and get better research coverage.

## Validation Commands

### Check Your Spec

```bash
python scripts/validate_spec.py --spec SPECIFICATION.md
```

Output:
```
🔍 Validating SPECIFICATION.md...

✅ All required sections present
ℹ️  Found 6 functional requirements
ℹ️  Found 8 research sources

📊 Completeness Score: 88/100
✅ Good! Address warnings to improve further.
```

### Generate Tasks

```bash
python scripts/generate_tasks.py \
  --spec SPECIFICATION.md \
  --plan TECHNICAL_PLAN.md
```

Output:
```
📋 Generated 12 tasks (24.0 estimated hours)
✅ Tasks written to TASKS.md
```

## Common Workflows

### Workflow 1: New Feature

```
You: "Add real-time notifications to my app"
Claude: [Researches WebSocket vs SSE, analyzes Firebase, studies socket.io docs]
Claude: "Here's your spec with researched recommendations..."
You: "Looks good, proceed"
Claude: [Generates plan and tasks]
```

### Workflow 2: Whole Project

```
You: "Build a recipe sharing platform"
Claude: "Let me research similar platforms..."
Claude: [Analyzes AllRecipes, Pinterest, gets user pain points from reviews]
Claude: "Found 3 key differentiators from research. Here's the spec..."
You: "Perfect, let's build it"
Claude: [Creates comprehensive plan and task breakdown]
```

### Workflow 3: Architecture Decision

```
You: "Should I use microservices or a monolith?"
Claude: "Let me research your specific context..."
Claude: [Studies team size, scale requirements, successful patterns]
Claude: "Based on research, monolith-first. Here's why..."
[Generates spec with architectural decision record]
```

## Bright Data Research Patterns

### Pattern: Competitor Analysis

When building features similar to existing products:

```python
# Automatic (Claude does this)
BrightData:web_data_google_play_store(url="competitor-app")
BrightData:web_data_amazon_product_reviews(url="competitor-product")

# Result: Pain points and feature gaps in your spec
```

### Pattern: Documentation Research

When using specific technologies:

```python
# Automatic
BrightData:scrape_as_markdown(url="https://official-docs.com")

# Result: Best practices and gotchas in your technical plan
```

### Pattern: Code Examples

When designing architecture:

```python
# Automatic
BrightData:web_data_github_repository_file(url="reference-implementation")

# Result: Proven patterns in your technical plan
```

## Tips for Success

### 1. Be Specific in Your Initial Request

❌ **Vague**: "Build an app"
✅ **Specific**: "Build a task management app for remote engineering teams with async communication"

**Why**: Specific requests enable targeted research

### 2. Mention Your Constraints Early

Good inputs:
- "Using Python and PostgreSQL" (tech constraints)
- "Must be HIPAA compliant" (regulatory constraints)
- "Launch in 2 weeks" (time constraints)
- "Team of 2 junior engineers" (skill constraints)

**Why**: Claude can research solutions that fit YOUR constraints

### 3. Trust the Research

Claude cites sources. Follow the links. You'll see:
- Official documentation
- Real user reviews
- Successful implementations
- Industry benchmarks

**Why**: Decisions are data-driven, not guesswork

### 4. Iterate the Spec

Specs are living documents. When you learn something new:

```
You: "I just learned our users hate email verification. Update the spec."
Claude: [Researches alternatives: SMS, magic links, OAuth]
Claude: "Updated spec with passwordless options based on research..."
```

### 5. Use Validation Checkpoints

Don't skip phases:
- ✅ Validate spec before plan
- ✅ Validate plan before tasks
- ✅ Validate tasks before coding

**Why**: Catching issues early is 10x cheaper than late

## Troubleshooting

### "Claude didn't research anything"

**Fix**: Explicitly mention research:
```
"Use spec-driven development WITH research to build..."
```

### "Research sources seem irrelevant"

**Fix**: Guide Claude:
```
"Focus research on [specific area], particularly [specific aspect]"
```

### "Too much research, taking too long"

**Fix**: Be more directive:
```
"Quick spec, minimal research, I know what I want"
```

### "Spec is too technical"

**Fix**: Remind Claude of the phase:
```
"We're in SPECIFY phase - focus on user intent, not implementation"
```

## Next Steps

### Option 1: Read Full Documentation
- [README.md](README.md) - Complete guide
- [SKILL.md](SKILL.md) - Detailed skill description

### Option 2: See an Example
- [examples/photo-sharing/](examples/photo-sharing/) - Full walkthrough

### Option 3: Jump In
```
In Claude Code, type:
"I want to use spec-driven development to build [your idea]"
```

## The Secret

Most coding agents are glorified autocomplete. They guess what you want.

This skill **researches** what you actually need, **documents** the findings, then **builds** exactly that.

Research → Spec → Plan → Tasks → Code

That's the difference between "code that looks right" and "code that IS right."

---

**Ready?** Open Claude Code and try:

```
I want to use spec-driven development to build a [your feature/project]
```

Claude will handle the rest.
