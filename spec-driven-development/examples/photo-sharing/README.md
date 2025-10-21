# Example: Photo Sharing Feature

This example demonstrates the complete spec-driven development workflow for adding a photo sharing feature to a mobile app.

## Scenario

**User Request**: "Add photo sharing to my mobile app so users can upload and share photos with their friends"

**Context**: Existing app with user authentication, need to add photo upload, storage, and sharing capabilities.

## Workflow Demonstration

### Step 1: SPECIFY with Research

Claude used Bright Data MCP tools to research:

1. **Competitor Analysis**:
   ```python
   # Analyzed Instagram, Pinterest, and Snapchat
   BrightData:web_data_google_play_store(
       url="https://play.google.com/store/apps/details?id=com.instagram.android"
   )
   ```
   **Findings**: Users want instant upload, filters, and privacy controls

2. **User Pain Points**:
   ```python
   # Extracted from app reviews
   BrightData:web_data_google_play_store(
       url="https://play.google.com/store/apps/details?id=com.pinterest"
   )
   ```
   **Findings**: Slow uploads and confusing privacy settings are top complaints

3. **Technical Documentation**:
   ```python
   # Researched image upload best practices
   BrightData:search_engine(
       query="mobile photo upload best practices 2025",
       engine="google"
   )
   ```

**Output**: [SPECIFICATION.md](SPECIFICATION.md) - See the complete spec with research citations

**Validation**:
- Ran `python ../../scripts/validate_spec.py --spec SPECIFICATION.md`
- Score: 92/100
- All required sections present
- Research-backed requirements

### Step 2: PLAN with Technical Research

Claude researched technical approaches:

1. **Storage Solutions Comparison**:
   ```python
   # Compared AWS S3, Google Cloud Storage, Cloudflare R2
   BrightData:scrape_batch(
       urls=[
           "https://docs.aws.amazon.com/s3/",
           "https://cloud.google.com/storage/docs",
           "https://docs.cloudflare.com/r2/"
       ]
   )
   ```
   **Decision**: AWS S3 for maturity and SDKs

2. **Image Processing Libraries**:
   ```python
   # Researched Python image libraries
   BrightData:scrape_as_markdown(
       url="https://pillow.readthedocs.io/en/stable/"
   )
   ```
   **Decision**: Pillow for processing, validation

3. **Architecture Patterns**:
   ```python
   # Studied successful implementations
   BrightData:web_data_github_repository_file(
       url="https://github.com/encode/starlette/blob/master/docs/static-files.md"
   )
   ```
   **Decision**: Async upload with background processing

**Output**: [TECHNICAL_PLAN.md](TECHNICAL_PLAN.md) - Complete architecture with justified decisions

**Validation**:
- Architecture reviewed
- Technology choices backed by research
- Performance targets based on industry benchmarks

### Step 3: TASKS - Automated Breakdown

Claude ran:

```bash
python ../../scripts/generate_tasks.py \
  --spec SPECIFICATION.md \
  --plan TECHNICAL_PLAN.md \
  --output TASKS.md
```

**Output**: [TASKS.md](TASKS.md) - 15 concrete tasks, 32 estimated hours

**Task Highlights**:
- Task 1.1: Set up S3 bucket (1.5 hours)
- Task 2.3: Implement image validation (1 hour)
- Task 3.4: Create photo upload endpoint (3 hours)
- Task 4.2: Add privacy controls (2 hours)

### Step 4: IMPLEMENT - Execution

Claude worked through tasks sequentially:

1. **Setup** (Tasks 1.1-1.3): Infrastructure and storage
2. **Core Upload** (Tasks 2.1-2.4): Image processing and API
3. **Sharing** (Tasks 3.1-3.3): Friend sharing and permissions
4. **Testing** (Tasks 4.1-4.2): Coverage and E2E tests

**Result**: Feature implemented with 85% test coverage, deployed to staging

## Research Artifacts

### Research Report: Competitor Analysis

See [research/competitor-analysis.md](research/competitor-analysis.md)

**Key Findings**:
- Instagram's upload flow is the gold standard (3 taps)
- Users expect real-time upload progress
- Privacy defaults matter: "public" causes regret
- Image compression is critical for mobile

### Research Report: Image Storage Best Practices

See [research/storage-solutions.md](research/storage-solutions.md)

**Key Findings**:
- S3 signed URLs for security
- CDN for serving (CloudFront)
- Automatic thumbnail generation
- Metadata storage separate from blob

## Metrics & Validation

### Specification Validation

```bash
$ python ../../scripts/validate_spec.py --spec SPECIFICATION.md

✅ VALIDATION PASSED

📊 Completeness Score: 92/100

ℹ️  INFORMATION:
   • Found 8 functional requirements
   • Found 12 research sources
   • Out of Scope clearly defined

✅ Excellent! Specification is comprehensive.
```

### Task Generation

```bash
$ python ../../scripts/generate_tasks.py --spec SPECIFICATION.md --plan TECHNICAL_PLAN.md

🔍 Analyzing specification and technical plan...
✅ Found 8 requirements
✅ Found 5 components
✅ Tech stack: {'language': 'Python', 'framework': 'FastAPI', 'database': 'PostgreSQL', 'cache': 'Redis'}

📋 Generated 15 tasks (32.0 estimated hours)

✅ Tasks written to TASKS.md

🎉 Task generation complete!
```

## Lessons Learned

### What Worked Well

1. **Research-First Approach**: Understanding Instagram's UX before designing saved rework
2. **Bright Data Tools**: Scraped real app reviews to find actual pain points
3. **Small Tasks**: 2-hour tasks made progress trackable and reviewable
4. **Living Spec**: Updated spec when we discovered better approaches during implementation

### What We'd Improve

1. **More Social Media Research**: Could have analyzed TikTok for video sharing patterns
2. **Performance Testing**: Should have researched load testing earlier
3. **Mobile-Specific Research**: More iOS vs Android differences

### Bright Data Tools Used

| Tool | Use Case | Value |
|------|----------|-------|
| `web_data_google_play_store` | App reviews and ratings | Found top user complaints |
| `scrape_batch` | Compare multiple docs | Evaluated storage solutions |
| `search_engine` | Find best practices | Discovered image optimization guides |
| `web_data_github_repository_file` | Code examples | Found reference implementations |

## Timeline

| Phase | Duration | Output |
|-------|----------|--------|
| SPECIFY + Research | 3 hours | SPECIFICATION.md |
| PLAN + Technical Research | 2 hours | TECHNICAL_PLAN.md |
| TASKS Generation | 15 minutes | TASKS.md |
| IMPLEMENT | 5 days (32 hours) | Working feature |
| **Total** | **~1 week** | **Production-ready feature** |

## Files in This Example

- `README.md` - This file
- `SPECIFICATION.md` - User requirements with research
- `TECHNICAL_PLAN.md` - Architecture and technical decisions
- `TASKS.md` - Implementation breakdown (15 tasks)
- `research/competitor-analysis.md` - Bright Data research on competitors
- `research/storage-solutions.md` - Technical architecture research

## Try It Yourself

1. Read through [SPECIFICATION.md](SPECIFICATION.md) to see how research is integrated
2. Review [TECHNICAL_PLAN.md](TECHNICAL_PLAN.md) to see justified technical decisions
3. Check [TASKS.md](TASKS.md) for the implementation breakdown
4. Look at research reports to see how Bright Data findings are documented

## Next Steps

Use this example as a template for your own projects:

1. Copy the structure
2. Run the same Bright Data research patterns
3. Customize for your domain
4. Let Claude guide you through the workflow

---

**Want to build this yourself?**

In Claude Code, say:
```
I want to use spec-driven development to add photo sharing to my app
```

Claude will activate this skill and guide you through the same research-driven process!
