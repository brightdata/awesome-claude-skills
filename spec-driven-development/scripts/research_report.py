#!/usr/bin/env python3
"""
Research Report Generator for Spec-Driven Development

This script provides a template for documenting research conducted using
Bright Data MCP tools during the specification phase.

Usage:
    python research_report.py --topic "microservices architecture" --output research/microservices.md
"""

import argparse
from pathlib import Path
from datetime import datetime


RESEARCH_TEMPLATE = """# Research Report: {topic}

**Date**: {date}
**Researcher**: {researcher}
**Purpose**: {purpose}

---

## Executive Summary

[2-3 sentences summarizing key findings from this research]

---

## Research Questions

1. [Question 1]
2. [Question 2]
3. [Question 3]

---

## Methodology

**Tools Used**:
- [ ] BrightData:search_engine - General web search
- [ ] BrightData:scrape_as_markdown - Documentation extraction
- [ ] BrightData:web_data_github_repository_file - Code examples
- [ ] BrightData:web_data_linkedin_company_profile - Company analysis
- [ ] Other: [Specify]

**Search Queries**:
1. `[query 1]` - [Purpose]
2. `[query 2]` - [Purpose]

**Sources Analyzed**:
- [Number] documentation pages
- [Number] GitHub repositories
- [Number] product reviews
- [Number] competitor sites

---

## Findings

### Finding 1: [Title]

**Source**: [URL or reference]

**Summary**:
[What you learned]

**Relevance to Project**:
[How this applies to our spec]

**Evidence**:
```
[Quote, code snippet, or data point]
```

**Actionable Insight**:
> [Specific recommendation for spec/plan]

---

### Finding 2: [Title]

[Repeat structure]

---

## Competitive Analysis

| Competitor | Approach | Strengths | Weaknesses | Key Takeaway |
|------------|----------|-----------|------------|--------------|
| [Name] | [How they solve it] | [What works] | [What doesn't] | [What to adopt/avoid] |

**Source**: [Link to BrightData research]

---

## Technical Patterns Identified

### Pattern 1: [Pattern Name]

**Description**:
[What is this pattern?]

**Used By**:
- [Company/Project 1]
- [Company/Project 2]

**Pros**:
- [Advantage 1]
- [Advantage 2]

**Cons**:
- [Disadvantage 1]

**Recommendation**:
[Should we use this? Why or why not?]

**Reference Implementation**:
[Link to GitHub repo or documentation]

---

## User Insights

### Pain Points Discovered

From reviews, forums, and social media:

1. **[Pain Point 1]**
   - **Source**: [Product reviews / Reddit / etc.]
   - **Frequency**: [How common is this complaint?]
   - **Impact**: [How does this affect users?]
   - **Our Response**: [How we'll avoid this]

2. **[Pain Point 2]**
   [Repeat]

### Desired Features

What users are asking for:

1. **[Feature Request 1]**
   - **Source**: [Where mentioned]
   - **Rationale**: [Why users want this]
   - **Priority for Us**: [High/Medium/Low]

---

## Technology Comparison

### Technology A vs Technology B vs Technology C

| Criteria | Tech A | Tech B | Tech C |
|----------|--------|--------|--------|
| Performance | [Benchmarks] | [Benchmarks] | [Benchmarks] |
| Learning Curve | [Assessment] | [Assessment] | [Assessment] |
| Community Size | [Metrics] | [Metrics] | [Metrics] |
| Documentation | [Quality rating] | [Quality rating] | [Quality rating] |
| Use Cases | [Best for...] | [Best for...] | [Best for...] |

**Recommendation**: [Which to choose and why]

**Sources**:
- [Link to comparison article]
- [Link to benchmarks]
- [Link to documentation]

---

## Best Practices Extracted

From official docs and successful implementations:

1. **[Best Practice 1]**
   - **Source**: [Documentation/Blog post]
   - **Rationale**: [Why this matters]
   - **Implementation**: [How to apply]

2. **[Best Practice 2]**
   [Repeat]

---

## Anti-Patterns to Avoid

Common mistakes identified in research:

1. **[Anti-Pattern 1]**
   - **Description**: [What not to do]
   - **Why It's Bad**: [Consequences]
   - **Source**: [Where we learned this]
   - **Alternative**: [Better approach]

---

## Data & Statistics

[Any quantitative findings]

- [Metric 1]: [Value] (Source: [Link])
- [Metric 2]: [Value] (Source: [Link])
- Market size: [Value]
- Growth rate: [Value]

---

## Open Questions

Questions we still need to answer:

1. **[Question 1]**
   - **Why It Matters**: [Importance]
   - **How to Answer**: [Further research needed]
   - **Deadline**: [When we need to know]

---

## Recommendations for Specification

Based on this research, we recommend:

1. **For SPECIFICATION.md**:
   - [ ] Include [finding X] in user journeys
   - [ ] Add [pain point Y] to "problems to solve"
   - [ ] Reference [competitor Z]'s approach in competitive analysis
   - [ ] Set success metric based on [industry benchmark]

2. **For TECHNICAL_PLAN.md**:
   - [ ] Adopt [technology/pattern A]
   - [ ] Avoid [anti-pattern B]
   - [ ] Follow [best practice C]
   - [ ] Architecture should account for [finding D]

---

## References

### Documentation
1. [Title] - [URL] - [Key takeaway]
2. [Title] - [URL] - [Key takeaway]

### Code Examples
1. [Repo name] - [URL] - [What we learned]
2. [Repo name] - [URL] - [What we learned]

### Articles & Blogs
1. [Title] - [URL] - [Summary]
2. [Title] - [URL] - [Summary]

### Product Reviews
1. [Product] - [URL] - [User sentiment]

### Social Media / Forums
1. [Discussion] - [URL] - [Insights]

---

## Appendix: Raw Data

### Search Results

**Query**: `[query string]`
**Engine**: Google
**Date**: {date}

Top 10 Results:
1. [Title] - [URL]
2. [Title] - [URL]
...

### Scraped Content

**URL**: [URL]
**Tool**: BrightData:scrape_as_markdown
**Date**: {date}

```markdown
[Excerpt of scraped content]
```

---

## Next Steps

1. [ ] Incorporate findings into SPECIFICATION.md
2. [ ] Update competitive analysis table
3. [ ] Add research sources to Research Notes section
4. [ ] Conduct follow-up research on open questions
5. [ ] Share report with stakeholders

---

**Report Status**: Draft | In Review | Final
**Last Updated**: {date}
"""


def generate_research_report(topic: str, output_path: str, researcher: str = "Claude", purpose: str = ""):
    """Generate a research report template."""

    if not purpose:
        purpose = f"Gather information about {topic} to inform specification and technical planning"

    content = RESEARCH_TEMPLATE.format(
        topic=topic.title(),
        date=datetime.now().strftime('%Y-%m-%d'),
        researcher=researcher,
        purpose=purpose
    )

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(content)

    print(f"✅ Research report template created: {output_path}")
    print(f"\n📝 Next steps:")
    print(f"   1. Use Bright Data MCP tools to conduct research")
    print(f"   2. Fill in findings as you discover them")
    print(f"   3. Reference this report in your SPECIFICATION.md")
    print(f"\n💡 Example MCP tool usage:")
    print(f'   BrightData:search_engine(query="{topic}", engine="google")')
    print(f"   BrightData:scrape_as_markdown(url=\"https://docs.example.com\")")
    print(f"\n🔗 When complete, link this report in SPECIFICATION.md Research Notes section")


def main():
    parser = argparse.ArgumentParser(
        description='Generate research report template for spec-driven development'
    )
    parser.add_argument(
        '--topic',
        type=str,
        required=True,
        help='Research topic (e.g., "microservices architecture")'
    )
    parser.add_argument(
        '--output',
        type=str,
        required=True,
        help='Output file path (e.g., research/microservices.md)'
    )
    parser.add_argument(
        '--researcher',
        type=str,
        default='Claude',
        help='Name of researcher (default: Claude)'
    )
    parser.add_argument(
        '--purpose',
        type=str,
        default='',
        help='Purpose of research (optional)'
    )

    args = parser.parse_args()

    try:
        generate_research_report(args.topic, args.output, args.researcher, args.purpose)
        return 0
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1


if __name__ == '__main__':
    exit(main())
