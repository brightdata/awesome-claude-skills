# Spec-Driven Development - Visual Workflow

## Complete Process Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         USER INPUT                                      │
│  "I want to build [feature/project]"                                    │
└────────────────────────┬────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      PHASE 1: SPECIFY                                   │
│                   (User Intent + Research)                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Claude Interviews You:                                                 │
│  ├─ Who will use this?                                                  │
│  ├─ What problem does it solve?                                         │
│  ├─ What does success look like?                                        │
│  └─ Any constraints?                                                    │
│                                                                         │
│  Bright Data Research (Automatic):                                      │
│  ┌─────────────────────────────────────────────────────────┐           │
│  │ search_engine("similar features", "google")             │           │
│  │   → Find competitors and best practices                 │           │
│  │                                                         │           │
│  │ web_data_google_play_store(competitor_app_url)          │           │
│  │   → Extract user reviews and pain points               │           │
│  │                                                         │           │
│  │ scrape_as_markdown(official_docs_url)                   │           │
│  │   → Get documentation and patterns                     │           │
│  │                                                         │           │
│  │ web_data_github_repository_file(reference_repo)         │           │
│  │   → Study successful implementations                    │           │
│  └─────────────────────────────────────────────────────────┘           │
│                                                                         │
│  Output Generated:                                                      │
│  ┌──────────────────────────────┐                                      │
│  │  SPECIFICATION.md            │                                      │
│  ├──────────────────────────────┤                                      │
│  │ ✓ Executive Summary          │                                      │
│  │ ✓ Problem Statement          │                                      │
│  │ ✓ Competitive Analysis ←───────────── [Research Data]              │
│  │ ✓ User Journeys              │                                      │
│  │ ✓ Functional Requirements    │                                      │
│  │ ✓ Success Metrics            │                                      │
│  │ ✓ Research Notes ←───────────────────── [All Sources Cited]        │
│  └──────────────────────────────┘                                      │
│                                                                         │
└────────────────────────┬────────────────────────────────────────────────┘
                         │
                         ▼
                  ┌──────────────┐
                  │  VALIDATION  │
                  │  CHECKPOINT  │
                  └──────┬───────┘
                         │
           ┌─────────────┴─────────────┐
           │                           │
      ❌ Issues                    ✅ Approved
           │                           │
           │                           ▼
           │           ┌─────────────────────────────────────────────────────┐
           │           │            PHASE 2: PLAN                            │
           │           │        (Technical Architecture + Research)          │
           │           ├─────────────────────────────────────────────────────┤
           │           │                                                     │
           │           │  Claude Asks:                                       │
           │           │  ├─ What's your tech stack?                         │
           │           │  ├─ Any constraints (compliance, performance)?      │
           │           │  ├─ Integration requirements?                       │
           │           │  └─ Team capabilities?                              │
           │           │                                                     │
           │           │  Technical Research (Automatic):                    │
           │           │  ┌───────────────────────────────────────────┐     │
           │           │  │ scrape_batch([docs1, docs2, docs3])       │     │
           │           │  │   → Compare technology options            │     │
           │           │  │                                           │     │
           │           │  │ search_engine("architecture patterns")    │     │
           │           │  │   → Find proven approaches                │     │
           │           │  │                                           │     │
           │           │  │ web_data_crunchbase_company(competitor)   │     │
           │           │  │   → Learn from successful companies       │     │
           │           │  │                                           │     │
           │           │  │ web_data_github_repository_file(example)  │     │
           │           │  │   → Study reference implementations       │     │
           │           │  └───────────────────────────────────────────┘     │
           │           │                                                     │
           │           │  Output Generated:                                  │
           │           │  ┌──────────────────────────────┐                  │
           │           │  │  TECHNICAL_PLAN.md           │                  │
           │           │  ├──────────────────────────────┤                  │
           │           │  │ ✓ Architecture Overview      │                  │
           │           │  │ ✓ Tech Stack ←──────────────────── [Researched] │
           │           │  │ ✓ Alternatives Considered    │                  │
           │           │  │ ✓ Component Design           │                  │
           │           │  │ ✓ Security Architecture      │                  │
           │           │  │ ✓ Performance Targets        │                  │
           │           │  │ ✓ Deployment Strategy        │                  │
           │           │  │ ✓ Research Artifacts ←──────────── [All Cited]  │
           │           │  └──────────────────────────────┘                  │
           │           │                                                     │
           │           └────────────────────┬────────────────────────────────┘
           │                                │
           │                                ▼
           │                         ┌──────────────┐
           │                         │  VALIDATION  │
           │                         │  CHECKPOINT  │
           │                         └──────┬───────┘
           │                                │
           │              ┌─────────────────┴─────────────┐
           │              │                               │
           │         ❌ Issues                       ✅ Approved
           │              │                               │
           │              │                               ▼
           └──────────────┘       ┌─────────────────────────────────────────┐
                                  │         PHASE 3: TASKS                  │
                                  │      (Automated Breakdown)              │
                                  ├─────────────────────────────────────────┤
                                  │                                         │
                                  │  Script Execution:                      │
                                  │  ┌───────────────────────────────────┐ │
                                  │  │ python generate_tasks.py          │ │
                                  │  │   --spec SPECIFICATION.md         │ │
                                  │  │   --plan TECHNICAL_PLAN.md        │ │
                                  │  └───────────────────────────────────┘ │
                                  │                                         │
                                  │  Task Generation Process:               │
                                  │  ┌───────────────────────────────────┐ │
                                  │  │ 1. Extract requirements from spec │ │
                                  │  │ 2. Parse components from plan     │ │
                                  │  │ 3. Identify tech stack            │ │
                                  │  │ 4. Generate setup tasks           │ │
                                  │  │ 5. Create feature tasks           │ │
                                  │  │ 6. Add testing tasks              │ │
                                  │  │ 7. Include deployment tasks       │ │
                                  │  │ 8. Map dependencies               │ │
                                  │  │ 9. Estimate effort                │ │
                                  │  │ 10. Assign priorities             │ │
                                  │  └───────────────────────────────────┘ │
                                  │                                         │
                                  │  Output Generated:                      │
                                  │  ┌──────────────────────────────┐      │
                                  │  │  TASKS.md                    │      │
                                  │  ├──────────────────────────────┤      │
                                  │  │ Epic 1: Setup (4 tasks)      │      │
                                  │  │   ├─ 1.1 Init repo           │      │
                                  │  │   ├─ 1.2 Dev env             │      │
                                  │  │   ├─ 1.3 CI/CD               │      │
                                  │  │   └─ 1.4 Database            │      │
                                  │  │                              │      │
                                  │  │ Epic 2: Features (8 tasks)   │      │
                                  │  │   ├─ 2.1 Data model          │      │
                                  │  │   ├─ 2.2 Business logic      │      │
                                  │  │   ├─ 2.3 API endpoint        │      │
                                  │  │   └─ ...                     │      │
                                  │  │                              │      │
                                  │  │ Epic 3: Testing (2 tasks)    │      │
                                  │  │ Epic 4: Deploy (2 tasks)     │      │
                                  │  │                              │      │
                                  │  │ Total: 15-20 tasks           │      │
                                  │  │ Est: 30-40 hours             │      │
                                  │  └──────────────────────────────┘      │
                                  │                                         │
                                  └────────────────┬────────────────────────┘
                                                   │
                                                   ▼
                                            ┌──────────────┐
                                            │  VALIDATION  │
                                            │  CHECKPOINT  │
                                            └──────┬───────┘
                                                   │
                                 ┌─────────────────┴─────────────┐
                                 │                               │
                            ❌ Issues                       ✅ Approved
                                 │                               │
                                 │                               ▼
                                 │           ┌──────────────────────────────────┐
                                 │           │    PHASE 4: IMPLEMENT            │
                                 │           │   (Execute + Validate)           │
                                 │           ├──────────────────────────────────┤
                                 │           │                                  │
                                 │           │  Task Execution Loop:            │
                                 │           │  ┌────────────────────────────┐  │
                                 │           │  │ FOR each task in TASKS.md: │  │
                                 │           │  │                            │  │
                                 │           │  │ 1. Read task description   │  │
                                 │           │  │ 2. Check dependencies      │  │
                                 │           │  │ 3. Implement code          │  │
                                 │           │  │ 4. Write tests             │  │
                                 │           │  │ 5. Validate criteria       │  │
                                 │           │  │ 6. Mark complete           │  │
                                 │           │  │ 7. Update spec if needed   │  │
                                 │           │  │                            │  │
                                 │           │  │ NEXT task                  │  │
                                 │           │  └────────────────────────────┘  │
                                 │           │                                  │
                                 │           │  Progress Tracking:              │
                                 │           │  🔵 Not Started (10 tasks)       │
                                 │           │  🟡 In Progress (1 task)         │
                                 │           │  🟢 Complete (5 tasks)           │
                                 │           │                                  │
                                 │           │  Continuous Validation:          │
                                 │           │  ├─ Tests pass?                  │
                                 │           │  ├─ Coverage >80%?               │
                                 │           │  ├─ Acceptance criteria met?     │
                                 │           │  └─ Spec still accurate?         │
                                 │           │                                  │
                                 │           └──────────────────────────────────┘
                                 │                           │
                                 │                           ▼
                                 │                    ┌─────────────┐
                                 │                    │   DEPLOY    │
                                 │                    │  TO STAGING │
                                 │                    └──────┬──────┘
                                 │                           │
                                 │                           ▼
                                 │                    ┌─────────────┐
                                 │                    │  PRODUCTION │
                                 │                    │    READY    │
                                 │                    └─────────────┘
                                 │
                                 └──────────────────────────┐
                                                            │
                                                            ▼
                                                  [Iterate & Improve]
```

---

## Research Flow Detail

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    BRIGHT DATA RESEARCH PIPELINE                        │
└─────────────────────────────────────────────────────────────────────────┘

Input: User Intent + Context
   │
   ├──► STEP 1: Initial Discovery
   │    ┌────────────────────────────────────────┐
   │    │ search_engine(broad_query)             │
   │    │   → Get overview of problem space      │
   │    │   → Find key players                   │
   │    │   → Identify common solutions          │
   │    └────────────────────────────────────────┘
   │              │
   │              ▼
   ├──► STEP 2: Competitive Analysis
   │    ┌────────────────────────────────────────┐
   │    │ web_data_google_play_store(app1)       │
   │    │ web_data_apple_app_store(app2)         │
   │    │   → Extract features                   │
   │    │   → Read reviews (pain points)         │
   │    │   → Analyze ratings                    │
   │    └────────────────────────────────────────┘
   │              │
   │              ▼
   ├──► STEP 3: Documentation Deep Dive
   │    ┌────────────────────────────────────────┐
   │    │ scrape_batch([doc1, doc2, doc3])       │
   │    │   → Official documentation             │
   │    │   → Best practices guides              │
   │    │   → API references                     │
   │    └────────────────────────────────────────┘
   │              │
   │              ▼
   ├──► STEP 4: Code Examples
   │    ┌────────────────────────────────────────┐
   │    │ web_data_github_repository_file(repo)  │
   │    │   → Reference implementations          │
   │    │   → Architecture patterns              │
   │    │   → Code quality examples              │
   │    └────────────────────────────────────────┘
   │              │
   │              ▼
   ├──► STEP 5: Community Insights
   │    ┌────────────────────────────────────────┐
   │    │ web_data_reddit_posts(discussion)      │
   │    │ web_data_youtube_comments(tutorial)    │
   │    │   → Common pitfalls                    │
   │    │   → User preferences                   │
   │    │   → Emerging trends                    │
   │    └────────────────────────────────────────┘
   │              │
   │              ▼
   └──► SYNTHESIS
        ┌────────────────────────────────────────┐
        │ Aggregate all findings                 │
        │ Cross-reference sources                │
        │ Identify patterns                      │
        │ Generate recommendations               │
        │ Create competitive analysis table      │
        │ Document research in spec              │
        └────────────────────────────────────────┘
                     │
                     ▼
              [Research-Backed Spec]
```

---

## Validation Checkpoints Detail

```
┌────────────────────────────────────────────────────────────────┐
│               VALIDATION CHECKPOINT PROCESS                    │
└────────────────────────────────────────────────────────────────┘

At Each Phase Transition:
   │
   ├──► AUTOMATED CHECKS
   │    ┌──────────────────────────────────┐
   │    │ python validate_spec.py          │
   │    │                                  │
   │    │ Checks:                          │
   │    │ ✓ Required sections present      │
   │    │ ✓ Acceptance criteria defined    │
   │    │ ✓ Success metrics measurable     │
   │    │ ✓ Research sources cited         │
   │    │ ✓ User journeys complete         │
   │    │ ✓ Constraints documented         │
   │    │                                  │
   │    │ Score: 85/100                    │
   │    └──────────────────────────────────┘
   │              │
   │              ▼
   ├──► USER REVIEW
   │    ┌──────────────────────────────────┐
   │    │ Questions to Ask:                │
   │    │                                  │
   │    │ □ Does this match my intent?     │
   │    │ □ Are requirements complete?     │
   │    │ □ Any missing edge cases?        │
   │    │ □ Research sources credible?     │
   │    │ □ Success metrics right?         │
   │    │ □ Anything out of scope missing? │
   │    └──────────────────────────────────┘
   │              │
   │              ▼
   ├──► STAKEHOLDER APPROVAL
   │    ┌──────────────────────────────────┐
   │    │ Product: ☑ Approved              │
   │    │ Tech Lead: ☑ Approved            │
   │    │ Security: ☑ Approved             │
   │    │ QA: ☑ Approved                   │
   │    └──────────────────────────────────┘
   │              │
   │              ▼
   └──► DECISION
        ┌──────────┬──────────┐
        │ PASS     │ FAIL     │
        └────┬─────┴────┬─────┘
             │          │
             ▼          ▼
        [Continue]  [Iterate]
```

---

## Task Dependency Graph Example

```
Epic 1: Setup
━━━━━━━━━━━━━

1.1 Init Repo
     │
     ▼
1.2 Dev Env ──────┐
     │            │
     ├────────────┼──► 1.3 CI/CD
     │            │
     ▼            │
1.4 Database ◄────┘


Epic 2: Features
━━━━━━━━━━━━━━━

1.4 (from above)
     │
     ▼
2.1 User Model
     │
     ├──► 2.2 Password Hashing
     │         │
     │         ▼
     │    2.3 Registration API
     │         │
     ▼         │
2.4 JWT Tokens │
     │         │
     └────┬────┘
          ▼
     2.5 Login API
          │
          ▼
     2.6 Auth Middleware


Epic 3: Testing
━━━━━━━━━━━━━━

2.6 (from above)
     │
     ├──► 4.1 Unit Tests (80% coverage)
     │         │
     │         ▼
     └────► 4.2 E2E Tests


Epic 4: Deploy
━━━━━━━━━━━━━

4.2 (from above)
     │
     ├──► 5.1 API Docs
     │
     └──► 5.2 Deploy Staging
              │
              ▼
         [Production]
```

---

## File Interaction Map

```
┌─────────────────────────────────────────────────────────────┐
│                    FILE ECOSYSTEM                           │
└─────────────────────────────────────────────────────────────┘

┌──────────────────┐
│   User Request   │
└────────┬─────────┘
         │
         ▼
┌─────────────────────────┐
│      SKILL.md           │◄──── Claude reads this
│  (Skill Definition)     │      Activates workflow
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ SPECIFICATION.md        │◄──── Generated from research
│  (User Requirements)    │      + User interview
└────────┬────────────────┘
         │
         │ Referenced by:
         ├──► validate_spec.py ──► Validation Report
         │
         └──► generate_tasks.py ──┐
                                  │
┌─────────────────────────┐       │
│ TECHNICAL_PLAN.md       │◄──────┤
│  (Architecture)         │       │ Both inputs
└────────┬────────────────┘       │
         │                        │
         │ Referenced by:         │
         └──► generate_tasks.py ◄─┘
                    │
                    ▼
         ┌─────────────────────┐
         │    TASKS.md         │◄──── Claude executes
         │ (Implementation)    │      Task by task
         └──────┬──────────────┘
                │
                ▼
         ┌─────────────────┐
         │  Working Code   │
         └─────────────────┘


Supporting Files:
━━━━━━━━━━━━━━━

research/
├── competitor-analysis.md  ◄──── research_report.py generates
├── tech-comparison.md
└── user-insights.md
         │
         └──► Referenced in SPECIFICATION.md
                       and TECHNICAL_PLAN.md


Templates:
━━━━━━━━━

SPECIFICATION_TEMPLATE.md ──► Used to generate ──► SPECIFICATION.md
PLAN_TEMPLATE.md ──────────► Used to generate ──► TECHNICAL_PLAN.md
TASKS_TEMPLATE.md ─────────► Used to generate ──► TASKS.md
```

---

## Time Flow Visualization

```
Traditional Approach:
━━━━━━━━━━━━━━━━━━━

[Think] ─► [Write Spec] ─► [Code] ─► [Debug] ─► [Rework] ─► [Done]
  2h         2h             8h        4h         6h         22h total
                                                  ▲
                                                  │
                                    "Oops, misunderstood requirements"


With This Skill:
━━━━━━━━━━━━━━━

[Input] ─► [Research] ─► [Spec] ─► [Plan] ─► [Tasks] ─► [Code] ─► [Done]
  1min      2min         1min      1min      auto       8h        ~8h total
                          │
                          └──► Research-backed, validated spec
                                No rework needed
```

---

## Parallel Research Execution

```
Sequential (Traditional):
━━━━━━━━━━━━━━━━━━━━━━━

Research Competitor 1  ───► 15 min
Research Competitor 2  ───► 15 min
Research Documentation ───► 20 min
Find Code Examples    ───► 20 min
Read User Reviews     ───► 15 min
                     Total: 85 minutes


Parallel (Bright Data):
━━━━━━━━━━━━━━━━━━━━━

Research Competitor 1  ┐
Research Competitor 2  ├───► All execute
Research Documentation ├───► simultaneously
Find Code Examples     ├───► via batch APIs
Read User Reviews      ┘
                     Total: ~2 minutes

Speedup: 42x faster!
```

---

## Success Metrics Dashboard (Conceptual)

```
┌────────────────────────────────────────────────────────┐
│         SPEC-DRIVEN DEVELOPMENT METRICS                │
├────────────────────────────────────────────────────────┤
│                                                        │
│  Time Savings:                                         │
│  ████████████████████████████████████░░░░░  95%       │
│                                                        │
│  Spec Completeness:                                    │
│  ██████████████████████████████████████░░  92/100     │
│                                                        │
│  Research Sources:                                     │
│  ████████████████████  15 sources cited               │
│                                                        │
│  Task Granularity:                                     │
│  ████████████████████  Avg 2.1 hrs/task               │
│                                                        │
│  Implementation Accuracy:                              │
│  ███████████████████████████████████████░  98%        │
│  (vs 65% without spec)                                 │
│                                                        │
│  Rework Required:                                      │
│  ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  5%          │
│  (vs 35% without spec)                                 │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## Integration Points

```
┌─────────────────────────────────────────────────────────┐
│            SPEC-DRIVEN SKILL INTEGRATIONS               │
└─────────────────────────────────────────────────────────┘

External Integrations:
━━━━━━━━━━━━━━━━━━━━

┌─────────────┐
│ Bright Data │◄──── All research operations
│ MCP Server  │      50+ scraping tools
└─────────────┘


Tool Integrations:
━━━━━━━━━━━━━━━

┌────────────┐
│    Git     │◄──── Version control for specs
└────────────┘

┌────────────┐
│   CI/CD    │◄──── Validate specs in pipeline
└────────────┘

┌────────────┐
│   VSCode   │◄──── Edit specs, view in IDE
└────────────┘


Team Integrations:
━━━━━━━━━━━━━━━

Product Team ──► Review SPECIFICATION.md
    │
Tech Team ────► Review TECHNICAL_PLAN.md
    │
QA Team ──────► Test against TASKS.md acceptance criteria
    │
All Teams ────► Track progress in TASKS.md
```

---

## Error Handling Flow

```
┌────────────────────────────────────────────┐
│         ERROR HANDLING & RECOVERY          │
└────────────────────────────────────────────┘

Error at SPECIFY Phase:
━━━━━━━━━━━━━━━━━━━━━

Validation Fails
     │
     ├──► Missing sections?
     │    └──► Claude auto-fills with research
     │
     ├──► Vague requirements?
     │    └──► Ask clarifying questions
     │
     └──► No research sources?
          └──► Run additional Bright Data queries


Error at PLAN Phase:
━━━━━━━━━━━━━━━━━━

Technology Conflicts?
     │
     ├──► Research alternatives
     │    └──► Compare with scrape_batch
     │
     └──► Update plan with justification


Error at TASKS Phase:
━━━━━━━━━━━━━━━━━━━

Tasks too large?
     │
     └──► Re-run generate_tasks.py
          └──► Auto-splits into smaller chunks


Error at IMPLEMENT Phase:
━━━━━━━━━━━━━━━━━━━━━━

Tests fail?
     │
     ├──► Check acceptance criteria
     │    └──► Fix implementation
     │
     └──► Update spec if requirements changed
```

---

## Quick Command Reference

```
┌─────────────────────────────────────────────────────┐
│           COMMAND CHEAT SHEET                       │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Activate Skill:                                    │
│  > "Use spec-driven development to build X"         │
│                                                     │
│  Validate Spec:                                     │
│  $ python scripts/validate_spec.py \                │
│      --spec SPECIFICATION.md                        │
│                                                     │
│  Generate Tasks:                                    │
│  $ python scripts/generate_tasks.py \               │
│      --spec SPECIFICATION.md \                      │
│      --plan TECHNICAL_PLAN.md                       │
│                                                     │
│  Create Research Report:                            │
│  $ python scripts/research_report.py \              │
│      --topic "Your Topic" \                         │
│      --output research/topic.md                     │
│                                                     │
│  View Skill Info:                                   │
│  Read SKILL.md (main definition)                    │
│  Read README.md (full documentation)                │
│  Read QUICKSTART.md (5-min guide)                   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

**This workflow transforms coding from guesswork to precision through research-driven specifications.**
