#!/usr/bin/env python3
"""
Lead Enrichment Script

Enriches a single lead with company and contact data using Bright Data MCP tools.
Implements intelligent tool selection based on available information.
"""

import argparse
import json
import sys
from typing import Any, Dict, List, Optional


def enrich_company(
    company_name: str,
    website: Optional[str] = None,
    linkedin_url: Optional[str] = None,
    industry: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Enrich company data using available information.

    This function provides a template for company enrichment logic.
    In practice, this would make calls to Bright Data MCP tools via the Claude API.

    Args:
        company_name: Company name
        website: Company website URL (optional)
        linkedin_url: LinkedIn company URL (optional)
        industry: Industry/vertical (optional)

    Returns:
        Dictionary with enriched company data
    """
    enriched_data = {
        "company_name": company_name,
        "website": website,
        "linkedin_url": linkedin_url,
        "industry": industry,
        "enrichment_status": "pending",
        "data_sources": [],
        "enriched_fields": {},
        "confidence_score": 0,
    }

    # Step 1: If we have LinkedIn URL, that's the best source
    if linkedin_url:
        enriched_data["data_sources"].append("linkedin_company_profile")
        enriched_data["recommended_mcp_tool"] = "web_data_linkedin_company_profile"
        enriched_data["confidence_score"] += 30

    # Step 2: If we have website, we can find LinkedIn/Crunchbase
    elif website:
        enriched_data["data_sources"].append("google_search")
        enriched_data["recommended_mcp_tool"] = "search_engine"
        enriched_data["search_query"] = (
            f'site:linkedin.com/company "{company_name}"'
        )
        enriched_data["confidence_score"] += 20

    # Step 3: Company name only - need broader search
    else:
        enriched_data["data_sources"].append("google_search")
        enriched_data["recommended_mcp_tool"] = "search_engine"
        if industry:
            enriched_data["search_query"] = (
                f'"{company_name}" {industry} company linkedin'
            )
        else:
            enriched_data["search_query"] = f'"{company_name}" company linkedin'
        enriched_data["confidence_score"] += 10

    # Add recommended secondary tools
    enriched_data["secondary_tools"] = []

    # For tech companies, Crunchbase is valuable
    if industry and any(
        tech in industry.lower()
        for tech in ["tech", "software", "saas", "startup", "ai", "data"]
    ):
        enriched_data["secondary_tools"].append("web_data_crunchbase_company")

    # ZoomInfo for contact info and tech stack
    enriched_data["secondary_tools"].append("web_data_zoominfo_company_profile")

    # News for recent signals
    enriched_data["secondary_tools"].append("web_data_reuter_news")

    enriched_data["enrichment_status"] = "ready"

    return enriched_data


def enrich_contact(
    contact_name: Optional[str] = None,
    contact_title: Optional[str] = None,
    company_name: Optional[str] = None,
    linkedin_url: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Enrich contact data using available information.

    Args:
        contact_name: Person's name (optional)
        contact_title: Job title (optional)
        company_name: Company they work for (optional)
        linkedin_url: LinkedIn profile URL (optional)

    Returns:
        Dictionary with enriched contact data
    """
    enriched_data = {
        "contact_name": contact_name,
        "contact_title": contact_title,
        "company_name": company_name,
        "linkedin_url": linkedin_url,
        "enrichment_status": "pending",
        "data_sources": [],
        "confidence_score": 0,
    }

    # Step 1: If we have LinkedIn profile URL, use it directly
    if linkedin_url:
        enriched_data["data_sources"].append("linkedin_person_profile")
        enriched_data["recommended_mcp_tool"] = "web_data_linkedin_person_profile"
        enriched_data["confidence_score"] = 90

    # Step 2: If we have name + company, search for profile
    elif contact_name and company_name:
        enriched_data["data_sources"].append("linkedin_people_search")
        enriched_data["recommended_mcp_tool"] = "web_data_linkedin_people_search"
        enriched_data["search_params"] = {
            "first_name": contact_name.split()[0] if contact_name else "",
            "last_name": " ".join(contact_name.split()[1:]) if contact_name else "",
            "company": company_name,
        }
        enriched_data["confidence_score"] = 70

    # Step 3: If we have title + company, search by role
    elif contact_title and company_name:
        enriched_data["data_sources"].append("google_search")
        enriched_data["recommended_mcp_tool"] = "search_engine"
        enriched_data["search_query"] = (
            f'site:linkedin.com/in "{contact_title}" "{company_name}"'
        )
        enriched_data["confidence_score"] = 50

    # Step 4: Title only - search for role at company
    elif contact_title:
        enriched_data["data_sources"].append("google_search")
        enriched_data["recommended_mcp_tool"] = "search_engine"
        if company_name:
            enriched_data["search_query"] = (
                f'"{contact_title}" "{company_name}" linkedin'
            )
        else:
            enriched_data["search_query"] = f'"{contact_title}" linkedin'
        enriched_data["confidence_score"] = 30

    # Add secondary enrichment opportunities
    enriched_data["secondary_tools"] = []

    # Check for social media presence
    if contact_name:
        enriched_data["secondary_tools"].append("web_data_x_posts")

    enriched_data["enrichment_status"] = "ready"

    return enriched_data


def generate_enrichment_plan(lead_data: dict[str, Any]) -> Dict[str, Any]:
    """
    Generate a complete enrichment plan for a lead.

    Args:
        lead_data: Dictionary with lead information

    Returns:
        Enrichment plan with recommended tools and sequence
    """
    company_name = lead_data.get("company_name")
    website = lead_data.get("website")
    linkedin_url = lead_data.get("linkedin_url")
    industry = lead_data.get("industry")
    contact_name = lead_data.get("contact_name")
    contact_title = lead_data.get("contact_title")

    plan = {
        "lead_id": lead_data.get("id", "unknown"),
        "company_enrichment": None,
        "contact_enrichment": None,
        "estimated_api_calls": 0,
        "priority": "standard",
    }

    # Enrich company data
    if company_name:
        plan["company_enrichment"] = enrich_company(
            company_name, website, linkedin_url, industry
        )
        plan["estimated_api_calls"] += len(
            plan["company_enrichment"]["data_sources"]
        )
        plan["estimated_api_calls"] += len(
            plan["company_enrichment"].get("secondary_tools", [])
        )

    # Enrich contact data
    if contact_name or contact_title:
        plan["contact_enrichment"] = enrich_contact(
            contact_name, contact_title, company_name, lead_data.get("contact_linkedin")
        )
        plan["estimated_api_calls"] += len(plan["contact_enrichment"]["data_sources"])

    # Determine priority based on data quality
    confidence_scores = []
    if plan["company_enrichment"]:
        confidence_scores.append(plan["company_enrichment"]["confidence_score"])
    if plan["contact_enrichment"]:
        confidence_scores.append(plan["contact_enrichment"]["confidence_score"])

    if confidence_scores:
        avg_confidence = sum(confidence_scores) / len(confidence_scores)
        if avg_confidence >= 70:
            plan["priority"] = "high"
        elif avg_confidence >= 40:
            plan["priority"] = "standard"
        else:
            plan["priority"] = "low"

    return plan


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Enrich lead data with company and contact information"
    )
    parser.add_argument(
        "--company-name", type=str, required=True, help="Company name"
    )
    parser.add_argument("--website", type=str, help="Company website URL")
    parser.add_argument("--linkedin-url", type=str, help="LinkedIn company URL")
    parser.add_argument("--industry", type=str, help="Industry or vertical")
    parser.add_argument("--contact-name", type=str, help="Contact person name")
    parser.add_argument("--contact-title", type=str, help="Contact job title")
    parser.add_argument(
        "--contact-linkedin", type=str, help="Contact LinkedIn profile URL"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="enrichment_plan.json",
        help="Output file path (default: enrichment_plan.json)",
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["json", "summary"],
        default="json",
        help="Output format (default: json)",
    )

    args = parser.parse_args()

    # Build lead data dictionary
    lead_data = {
        "company_name": args.company_name,
        "website": args.website,
        "linkedin_url": args.linkedin_url,
        "industry": args.industry,
        "contact_name": args.contact_name,
        "contact_title": args.contact_title,
        "contact_linkedin": args.contact_linkedin,
    }

    # Generate enrichment plan
    plan = generate_enrichment_plan(lead_data)

    # Output results
    if args.format == "json":
        with open(args.output, "w") as f:
            json.dump(plan, f, indent=2)
        print(f"✓ Enrichment plan saved to {args.output}")
    else:
        # Print summary to console
        print("\n" + "=" * 70)
        print("LEAD ENRICHMENT PLAN")
        print("=" * 70)

        print(f"\nLead: {args.company_name}")
        print(f"Priority: {plan['priority'].upper()}")
        print(f"Estimated API calls: {plan['estimated_api_calls']}")

        if plan["company_enrichment"]:
            print("\n--- Company Enrichment ---")
            ce = plan["company_enrichment"]
            print(f"Status: {ce['enrichment_status']}")
            print(f"Confidence: {ce['confidence_score']}%")
            print(f"Primary tool: {ce.get('recommended_mcp_tool', 'N/A')}")
            if ce.get("search_query"):
                print(f"Search query: {ce['search_query']}")
            if ce.get("secondary_tools"):
                print(f"Secondary tools: {', '.join(ce['secondary_tools'])}")

        if plan["contact_enrichment"]:
            print("\n--- Contact Enrichment ---")
            ce = plan["contact_enrichment"]
            print(f"Status: {ce['enrichment_status']}")
            print(f"Confidence: {ce['confidence_score']}%")
            print(f"Primary tool: {ce.get('recommended_mcp_tool', 'N/A')}")
            if ce.get("search_query"):
                print(f"Search query: {ce['search_query']}")
            if ce.get("search_params"):
                print(f"Search params: {ce['search_params']}")

        print("\n" + "=" * 70)
        print("\n💡 This plan can be executed by Claude using Bright Data MCP tools")
        print(
            "   Pass this to the Lead Research Assistant skill for automatic execution\n"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
