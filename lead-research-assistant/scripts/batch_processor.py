#!/usr/bin/env python3
"""
Batch Lead Processor

Processes multiple leads from CSV/Excel files with parallel enrichment and qualification.
Includes progress tracking, error handling, and resume capability.
"""

import argparse
import csv
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Optional

try:
    import pandas as pd

    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

from lead_enrichment import generate_enrichment_plan
from lead_qualification import qualify_lead


def load_leads_csv(file_path: str) -> list[dict[str, Any]]:
    """
    Load leads from CSV file.

    Args:
        file_path: Path to CSV file

    Returns:
        List of lead dictionaries
    """
    leads = []

    with open(file_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader):
            lead = {
                "id": f"lead_{idx + 1}",
                "company_name": row.get("company_name", "").strip(),
                "website": row.get("website", "").strip() or None,
                "linkedin_url": row.get("linkedin_url", "").strip() or None,
                "industry": row.get("industry", "").strip() or None,
                "contact_name": row.get("contact_name", "").strip() or None,
                "contact_title": row.get("contact_title", "").strip() or None,
                "contact_linkedin": row.get("contact_linkedin", "").strip() or None,
                "notes": row.get("notes", "").strip() or None,
            }

            # Only add if company name exists
            if lead["company_name"]:
                leads.append(lead)

    return leads


def load_leads_excel(file_path: str) -> list[dict[str, Any]]:
    """
    Load leads from Excel file using pandas.

    Args:
        file_path: Path to Excel file

    Returns:
        List of lead dictionaries
    """
    if not HAS_PANDAS:
        raise ImportError(
            "pandas is required to read Excel files. Install with: pip install pandas openpyxl"
        )

    df = pd.read_excel(file_path)

    # Rename columns to standard format if needed
    column_mapping = {
        "Company Name": "company_name",
        "Company": "company_name",
        "Website": "website",
        "URL": "website",
        "LinkedIn": "linkedin_url",
        "LinkedIn URL": "linkedin_url",
        "Industry": "industry",
        "Vertical": "industry",
        "Contact Name": "contact_name",
        "Name": "contact_name",
        "Contact Title": "contact_title",
        "Title": "contact_title",
        "Job Title": "contact_title",
        "Contact LinkedIn": "contact_linkedin",
        "Notes": "notes",
    }

    df = df.rename(columns=column_mapping)

    leads = []
    for idx, row in df.iterrows():
        lead = {
            "id": f"lead_{idx + 1}",
            "company_name": str(row.get("company_name", "")).strip(),
            "website": str(row.get("website", "")).strip() or None,
            "linkedin_url": str(row.get("linkedin_url", "")).strip() or None,
            "industry": str(row.get("industry", "")).strip() or None,
            "contact_name": str(row.get("contact_name", "")).strip() or None,
            "contact_title": str(row.get("contact_title", "")).strip() or None,
            "contact_linkedin": str(row.get("contact_linkedin", "")).strip() or None,
            "notes": str(row.get("notes", "")).strip() or None,
        }

        # Clean up 'nan' strings from pandas
        for key in lead:
            if lead[key] == "nan":
                lead[key] = None

        # Only add if company name exists
        if lead["company_name"] and lead["company_name"] != "nan":
            leads.append(lead)

    return leads


def validate_leads(leads: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Validate lead data quality.

    Args:
        leads: List of lead dictionaries

    Returns:
        Validation report
    """
    report = {
        "total_leads": len(leads),
        "valid_leads": 0,
        "issues": [],
        "data_quality": {},
    }

    has_website = 0
    has_linkedin = 0
    has_industry = 0
    has_contact = 0

    for lead in leads:
        is_valid = True

        # Check required field
        if not lead.get("company_name"):
            report["issues"].append(
                f"Lead {lead.get('id', 'unknown')}: Missing company name"
            )
            is_valid = False

        # Track data completeness
        if lead.get("website"):
            has_website += 1
        if lead.get("linkedin_url"):
            has_linkedin += 1
        if lead.get("industry"):
            has_industry += 1
        if lead.get("contact_name") or lead.get("contact_title"):
            has_contact += 1

        if is_valid:
            report["valid_leads"] += 1

    # Calculate data quality percentages
    total = len(leads)
    report["data_quality"] = {
        "has_website": f"{(has_website / total * 100):.1f}%",
        "has_linkedin": f"{(has_linkedin / total * 100):.1f}%",
        "has_industry": f"{(has_industry / total * 100):.1f}%",
        "has_contact_info": f"{(has_contact / total * 100):.1f}%",
    }

    return report


def process_single_lead(
    lead: dict[str, Any], icp_criteria: Optional[dict] = None
) -> dict[str, Any]:
    """
    Process a single lead: generate enrichment plan and qualify.

    Args:
        lead: Lead data dictionary
        icp_criteria: Optional ICP criteria for qualification

    Returns:
        Processed lead with enrichment plan and scores
    """
    result = lead.copy()

    try:
        # Generate enrichment plan
        enrichment_plan = generate_enrichment_plan(lead)
        result["enrichment_plan"] = enrichment_plan

        # Simulate enriched data for qualification
        # In production, this would call actual Bright Data MCP tools
        mock_enriched_data = {
            "company_name": lead["company_name"],
            "employee_count": 150,  # Mock data
            "revenue": 5_000_000,  # Mock data
            "industry": lead.get("industry", "Technology"),
            "location": "North America",
            "technologies": ["AWS", "React", "Python"],
            "has_api": True,
            "uses_cloud": True,
            "growth_signals": {"hiring_actively": True, "recent_funding": False},
            "buying_intent": {"job_postings_relevant": True},
            "engagement": {"active_social_media": True},
            "deal_factors": {"authority_access": True},
            "competitive": {"weak_incumbent": True},
        }

        # Qualify the lead
        scores = qualify_lead(mock_enriched_data, icp_criteria)
        result["qualification"] = scores

        result["status"] = "success"
        result["processed_at"] = time.strftime("%Y-%m-%d %H:%M:%S")

    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)
        result["processed_at"] = time.strftime("%Y-%m-%d %H:%M:%S")

    return result


def process_batch(
    leads: list[dict[str, Any]],
    parallel: int = 3,
    icp_criteria: Optional[dict] = None,
    progress_file: Optional[str] = None,
) -> list[dict[str, Any]]:
    """
    Process multiple leads with parallel execution.

    Args:
        leads: List of lead dictionaries
        parallel: Number of parallel workers
        icp_criteria: Optional ICP criteria
        progress_file: Optional file to save progress

    Returns:
        List of processed leads
    """
    results = []
    total = len(leads)

    print(f"\n🚀 Processing {total} leads with {parallel} parallel workers...")
    print("=" * 70)

    with ThreadPoolExecutor(max_workers=parallel) as executor:
        # Submit all tasks
        future_to_lead = {
            executor.submit(process_single_lead, lead, icp_criteria): lead
            for lead in leads
        }

        # Process completed tasks
        completed = 0
        for future in as_completed(future_to_lead):
            completed += 1
            result = future.result()
            results.append(result)

            # Show progress
            status_icon = "✓" if result["status"] == "success" else "✗"
            tier = result.get("qualification", {}).get("tier", "?")
            score = result.get("qualification", {}).get("weighted_total", 0)

            print(
                f"{status_icon} [{completed}/{total}] {result['company_name'][:40]:40} | Tier {tier} | Score: {score:.1f}"
            )

            # Save progress incrementally if requested
            if progress_file and completed % 10 == 0:
                with open(progress_file, "w") as f:
                    json.dump(results, f, indent=2)
                print(f"   💾 Progress saved ({completed}/{total} complete)")

    print("=" * 70)
    print(f"✅ Batch processing complete: {completed}/{total} leads processed\n")

    return results


def generate_summary(results: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Generate summary statistics from processed leads.

    Args:
        results: List of processed lead results

    Returns:
        Summary dictionary
    """
    summary = {
        "total_processed": len(results),
        "successful": 0,
        "errors": 0,
        "tier_distribution": {"A": 0, "B": 0, "C": 0, "D": 0},
        "avg_score": 0,
        "top_leads": [],
    }

    scores = []

    for result in results:
        if result["status"] == "success":
            summary["successful"] += 1

            qual = result.get("qualification", {})
            tier = qual.get("tier", "D")
            score = qual.get("weighted_total", 0)

            summary["tier_distribution"][tier] += 1
            scores.append(score)

        else:
            summary["errors"] += 1

    # Calculate average score
    if scores:
        summary["avg_score"] = round(sum(scores) / len(scores), 2)

    # Get top 10 leads
    successful_results = [r for r in results if r["status"] == "success"]
    sorted_results = sorted(
        successful_results,
        key=lambda x: x.get("qualification", {}).get("weighted_total", 0),
        reverse=True,
    )

    summary["top_leads"] = [
        {
            "company_name": r["company_name"],
            "tier": r["qualification"]["tier"],
            "score": r["qualification"]["weighted_total"],
        }
        for r in sorted_results[:10]
    ]

    return summary


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Process multiple leads from CSV/Excel files"
    )
    parser.add_argument(
        "--input", type=str, required=True, help="Path to input CSV or Excel file"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="enriched_leads.json",
        help="Output JSON file path (default: enriched_leads.json)",
    )
    parser.add_argument(
        "--icp-config", type=str, help="Path to ICP criteria JSON file"
    )
    parser.add_argument(
        "--parallel",
        type=int,
        default=3,
        help="Number of parallel workers (default: 3, max: 10)",
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Only validate input file without processing",
    )
    parser.add_argument(
        "--progress-file",
        type=str,
        help="Save progress incrementally to this file",
    )

    args = parser.parse_args()

    # Validate parallel workers
    if args.parallel < 1 or args.parallel > 10:
        print("Error: --parallel must be between 1 and 10")
        return 1

    # Load leads
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {args.input}")
        return 1

    print(f"📁 Loading leads from {args.input}...")

    try:
        if input_path.suffix.lower() == ".csv":
            leads = load_leads_csv(args.input)
        elif input_path.suffix.lower() in [".xlsx", ".xls"]:
            leads = load_leads_excel(args.input)
        else:
            print(
                f"Error: Unsupported file format: {input_path.suffix}. Use .csv or .xlsx"
            )
            return 1
    except Exception as e:
        print(f"Error loading file: {e}")
        return 1

    print(f"✓ Loaded {len(leads)} leads")

    # Validate leads
    validation = validate_leads(leads)

    print("\n📊 Data Quality Report:")
    print(f"   Total leads: {validation['total_leads']}")
    print(f"   Valid leads: {validation['valid_leads']}")
    print(
        f"   With website: {validation['data_quality']['has_website']}"
    )
    print(
        f"   With LinkedIn: {validation['data_quality']['has_linkedin']}"
    )
    print(
        f"   With industry: {validation['data_quality']['has_industry']}"
    )
    print(
        f"   With contact info: {validation['data_quality']['has_contact_info']}"
    )

    if validation["issues"]:
        print(f"\n⚠️  Found {len(validation['issues'])} validation issues:")
        for issue in validation["issues"][:5]:  # Show first 5
            print(f"   - {issue}")
        if len(validation["issues"]) > 5:
            print(f"   ... and {len(validation['issues']) - 5} more")

    if args.validate_only:
        print("\n✓ Validation complete (no processing performed)")
        return 0

    # Load ICP criteria if provided
    icp_criteria = None
    if args.icp_config:
        try:
            with open(args.icp_config) as f:
                icp_criteria = json.load(f)
            print(f"✓ Loaded custom ICP criteria from {args.icp_config}")
        except Exception as e:
            print(f"Warning: Could not load ICP config: {e}")
            print("Using default ICP criteria")

    # Process leads
    results = process_batch(
        leads, args.parallel, icp_criteria, args.progress_file
    )

    # Generate summary
    summary = generate_summary(results)

    print("📈 Processing Summary:")
    print(f"   Successful: {summary['successful']}/{summary['total_processed']}")
    print(f"   Errors: {summary['errors']}")
    print(f"   Average score: {summary['avg_score']:.1f}")
    print("\n   Tier Distribution:")
    print(f"      A-tier: {summary['tier_distribution']['A']} leads")
    print(f"      B-tier: {summary['tier_distribution']['B']} leads")
    print(f"      C-tier: {summary['tier_distribution']['C']} leads")
    print(f"      D-tier: {summary['tier_distribution']['D']} leads")

    if summary["top_leads"]:
        print("\n   🏆 Top 10 Leads:")
        for i, lead in enumerate(summary["top_leads"], 1):
            print(
                f"      {i}. {lead['company_name'][:35]:35} | Tier {lead['tier']} | {lead['score']:.1f}"
            )

    # Save results
    output_data = {"summary": summary, "leads": results, "metadata": {"input_file": args.input, "processed_at": time.strftime("%Y-%m-%d %H:%M:%S"), "total_leads": len(leads), "parallel_workers": args.parallel}}

    with open(args.output, "w") as f:
        json.dump(output_data, f, indent=2)

    print(f"\n✅ Results saved to {args.output}")
    print(
        f"💡 Next step: Generate Excel report with: python scripts/report_generator.py --input {args.output}\n"
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
