#!/usr/bin/env python3
"""
Lead Qualification Script

Scores leads against custom ICP (Ideal Customer Profile) criteria.
Supports configurable scoring weights and thresholds.
"""

import argparse
import json
import sys
from typing import Any


# Default ICP criteria with scoring weights
DEFAULT_ICP_CRITERIA = {
    "firmographic": {
        "weight": 0.35,
        "criteria": {
            "company_size": {
                "weight": 0.3,
                "ranges": {
                    "enterprise": {"min": 1000, "max": None, "score": 100},
                    "mid_market": {"min": 200, "max": 999, "score": 80},
                    "smb": {"min": 50, "max": 199, "score": 60},
                    "startup": {"min": 10, "max": 49, "score": 40},
                    "micro": {"min": 0, "max": 9, "score": 20},
                },
            },
            "revenue": {
                "weight": 0.25,
                "ranges": {
                    "large": {"min": 100_000_000, "max": None, "score": 100},
                    "medium": {"min": 10_000_000, "max": 99_999_999, "score": 80},
                    "small": {"min": 1_000_000, "max": 9_999_999, "score": 60},
                    "micro": {"min": 0, "max": 999_999, "score": 30},
                },
            },
            "industry_match": {
                "weight": 0.25,
                "target_industries": [
                    "Technology",
                    "SaaS",
                    "Software",
                    "Fintech",
                    "E-commerce",
                ],
                "score_match": 100,
                "score_adjacent": 60,
                "score_other": 20,
            },
            "geographic_match": {
                "weight": 0.2,
                "target_regions": ["North America", "Europe", "APAC"],
                "score_match": 100,
                "score_other": 50,
            },
        },
    },
    "technographic": {
        "weight": 0.25,
        "criteria": {
            "tech_stack_compatibility": {
                "weight": 0.5,
                "compatible_technologies": [
                    "AWS",
                    "Azure",
                    "GCP",
                    "Kubernetes",
                    "Docker",
                    "React",
                    "Python",
                    "Node.js",
                ],
                "score_per_match": 15,
                "max_score": 100,
            },
            "digital_maturity": {
                "weight": 0.5,
                "indicators": {
                    "has_api": 25,
                    "has_mobile_app": 20,
                    "cloud_infrastructure": 25,
                    "modern_tech_stack": 30,
                },
            },
        },
    },
    "behavioral": {
        "weight": 0.25,
        "criteria": {
            "growth_signals": {
                "weight": 0.4,
                "signals": {
                    "recent_funding": 30,
                    "hiring_actively": 25,
                    "product_launch": 20,
                    "market_expansion": 25,
                },
            },
            "buying_intent": {
                "weight": 0.35,
                "signals": {
                    "job_postings_relevant": 35,
                    "technology_investment": 30,
                    "competitive_switch": 20,
                    "pain_point_mentioned": 15,
                },
            },
            "engagement_potential": {
                "weight": 0.25,
                "signals": {
                    "active_social_media": 20,
                    "content_publishing": 30,
                    "event_participation": 25,
                    "thought_leadership": 25,
                },
            },
        },
    },
    "strategic": {
        "weight": 0.15,
        "criteria": {
            "deal_potential": {
                "weight": 0.5,
                "factors": {
                    "budget_signals": 30,
                    "decision_timeline": 25,
                    "authority_access": 25,
                    "economic_buyer_identified": 20,
                },
            },
            "competitive_position": {
                "weight": 0.5,
                "factors": {
                    "no_incumbent": 35,
                    "weak_incumbent": 25,
                    "switching_cost_low": 20,
                    "competitive_advantage": 20,
                },
            },
        },
    },
}


def score_company_size(employee_count: int, criteria: dict) -> float:
    """Score based on company size."""
    for range_name, range_data in criteria["ranges"].items():
        min_val = range_data["min"]
        max_val = range_data.get("max")

        if max_val is None:  # No upper limit
            if employee_count >= min_val:
                return range_data["score"]
        elif min_val <= employee_count <= max_val:
            return range_data["score"]

    return 0


def score_revenue(revenue: float, criteria: dict) -> float:
    """Score based on annual revenue."""
    for range_name, range_data in criteria["ranges"].items():
        min_val = range_data["min"]
        max_val = range_data.get("max")

        if max_val is None:  # No upper limit
            if revenue >= min_val:
                return range_data["score"]
        elif min_val <= revenue <= max_val:
            return range_data["score"]

    return 0


def score_industry(industry: str, criteria: dict) -> float:
    """Score based on industry match."""
    industry_lower = industry.lower() if industry else ""
    target_industries_lower = [i.lower() for i in criteria["target_industries"]]

    # Exact match
    if industry_lower in target_industries_lower:
        return criteria["score_match"]

    # Partial match (adjacent industry)
    for target in target_industries_lower:
        if target in industry_lower or industry_lower in target:
            return criteria["score_adjacent"]

    return criteria["score_other"]


def score_geography(location: str, criteria: dict) -> float:
    """Score based on geographic location."""
    location_lower = location.lower() if location else ""
    target_regions_lower = [r.lower() for r in criteria["target_regions"]]

    for region in target_regions_lower:
        if region.lower() in location_lower:
            return criteria["score_match"]

    return criteria["score_other"]


def score_tech_stack(tech_list: list[str], criteria: dict) -> float:
    """Score based on technology stack compatibility."""
    if not tech_list:
        return 0

    compatible = criteria["compatible_technologies"]
    compatible_lower = [t.lower() for t in compatible]

    matches = sum(1 for tech in tech_list if tech.lower() in compatible_lower)
    score = min(matches * criteria["score_per_match"], criteria["max_score"])

    return score


def score_digital_maturity(company_data: dict, criteria: dict) -> float:
    """Score based on digital maturity indicators."""
    score = 0
    indicators = criteria["indicators"]

    if company_data.get("has_api"):
        score += indicators["has_api"]
    if company_data.get("has_mobile_app"):
        score += indicators["has_mobile_app"]
    if company_data.get("uses_cloud"):
        score += indicators["cloud_infrastructure"]
    if company_data.get("modern_stack"):
        score += indicators["modern_tech_stack"]

    return min(score, 100)


def score_growth_signals(signals_data: dict, criteria: dict) -> float:
    """Score based on growth signals."""
    score = 0
    signal_scores = criteria["signals"]

    for signal, points in signal_scores.items():
        if signals_data.get(signal):
            score += points

    return min(score, 100)


def score_buying_intent(intent_data: dict, criteria: dict) -> float:
    """Score based on buying intent signals."""
    score = 0
    signal_scores = criteria["signals"]

    for signal, points in signal_scores.items():
        if intent_data.get(signal):
            score += points

    return min(score, 100)


def score_engagement_potential(engagement_data: dict, criteria: dict) -> float:
    """Score based on engagement potential."""
    score = 0
    signal_scores = criteria["signals"]

    for signal, points in signal_scores.items():
        if engagement_data.get(signal):
            score += points

    return min(score, 100)


def score_deal_potential(deal_data: dict, criteria: dict) -> float:
    """Score based on deal potential factors."""
    score = 0
    factor_scores = criteria["factors"]

    for factor, points in factor_scores.items():
        if deal_data.get(factor):
            score += points

    return min(score, 100)


def score_competitive_position(competitive_data: dict, criteria: dict) -> float:
    """Score based on competitive position."""
    score = 0
    factor_scores = criteria["factors"]

    for factor, points in factor_scores.items():
        if competitive_data.get(factor):
            score += points

    return min(score, 100)


def qualify_lead(company_data: dict, icp_criteria: dict = None) -> dict[str, Any]:
    """
    Calculate comprehensive lead qualification score.

    Args:
        company_data: Dictionary with company information
        icp_criteria: Custom ICP criteria (uses default if None)

    Returns:
        Dictionary with scores and qualification tier
    """
    if icp_criteria is None:
        icp_criteria = DEFAULT_ICP_CRITERIA

    scores = {
        "firmographic": {},
        "technographic": {},
        "behavioral": {},
        "strategic": {},
        "weighted_total": 0,
        "tier": "",
        "recommendation": "",
    }

    # 1. FIRMOGRAPHIC SCORING
    firm_criteria = icp_criteria["firmographic"]["criteria"]
    firm_weight = icp_criteria["firmographic"]["weight"]

    # Company size
    if company_data.get("employee_count"):
        size_score = score_company_size(
            company_data["employee_count"], firm_criteria["company_size"]
        )
        scores["firmographic"]["company_size"] = size_score
    else:
        scores["firmographic"]["company_size"] = 0

    # Revenue
    if company_data.get("revenue"):
        revenue_score = score_revenue(
            company_data["revenue"], firm_criteria["revenue"]
        )
        scores["firmographic"]["revenue"] = revenue_score
    else:
        scores["firmographic"]["revenue"] = 0

    # Industry
    if company_data.get("industry"):
        industry_score = score_industry(
            company_data["industry"], firm_criteria["industry_match"]
        )
        scores["firmographic"]["industry"] = industry_score
    else:
        scores["firmographic"]["industry"] = 0

    # Geography
    if company_data.get("location"):
        geo_score = score_geography(
            company_data["location"], firm_criteria["geographic_match"]
        )
        scores["firmographic"]["geography"] = geo_score
    else:
        scores["firmographic"]["geography"] = 0

    # Calculate weighted firmographic score
    firm_total = 0
    for criterion_name, criterion_data in firm_criteria.items():
        criterion_weight = criterion_data["weight"]
        criterion_score = scores["firmographic"].get(
            criterion_name.replace("_match", ""), 0
        )
        firm_total += criterion_score * criterion_weight

    scores["firmographic"]["total"] = firm_total
    scores["firmographic"]["weighted"] = firm_total * firm_weight

    # 2. TECHNOGRAPHIC SCORING
    tech_criteria = icp_criteria["technographic"]["criteria"]
    tech_weight = icp_criteria["technographic"]["weight"]

    # Tech stack compatibility
    tech_stack_score = score_tech_stack(
        company_data.get("technologies", []),
        tech_criteria["tech_stack_compatibility"],
    )
    scores["technographic"]["tech_stack"] = tech_stack_score

    # Digital maturity
    maturity_score = score_digital_maturity(
        company_data, tech_criteria["digital_maturity"]
    )
    scores["technographic"]["digital_maturity"] = maturity_score

    # Calculate weighted technographic score
    tech_total = (
        tech_stack_score * tech_criteria["tech_stack_compatibility"]["weight"]
        + maturity_score * tech_criteria["digital_maturity"]["weight"]
    )
    scores["technographic"]["total"] = tech_total
    scores["technographic"]["weighted"] = tech_total * tech_weight

    # 3. BEHAVIORAL SCORING
    behav_criteria = icp_criteria["behavioral"]["criteria"]
    behav_weight = icp_criteria["behavioral"]["weight"]

    # Growth signals
    growth_score = score_growth_signals(
        company_data.get("growth_signals", {}), behav_criteria["growth_signals"]
    )
    scores["behavioral"]["growth_signals"] = growth_score

    # Buying intent
    intent_score = score_buying_intent(
        company_data.get("buying_intent", {}), behav_criteria["buying_intent"]
    )
    scores["behavioral"]["buying_intent"] = intent_score

    # Engagement potential
    engagement_score = score_engagement_potential(
        company_data.get("engagement", {}), behav_criteria["engagement_potential"]
    )
    scores["behavioral"]["engagement"] = engagement_score

    # Calculate weighted behavioral score
    behav_total = (
        growth_score * behav_criteria["growth_signals"]["weight"]
        + intent_score * behav_criteria["buying_intent"]["weight"]
        + engagement_score * behav_criteria["engagement_potential"]["weight"]
    )
    scores["behavioral"]["total"] = behav_total
    scores["behavioral"]["weighted"] = behav_total * behav_weight

    # 4. STRATEGIC SCORING
    strat_criteria = icp_criteria["strategic"]["criteria"]
    strat_weight = icp_criteria["strategic"]["weight"]

    # Deal potential
    deal_score = score_deal_potential(
        company_data.get("deal_factors", {}), strat_criteria["deal_potential"]
    )
    scores["strategic"]["deal_potential"] = deal_score

    # Competitive position
    competitive_score = score_competitive_position(
        company_data.get("competitive", {}), strat_criteria["competitive_position"]
    )
    scores["strategic"]["competitive"] = competitive_score

    # Calculate weighted strategic score
    strat_total = (
        deal_score * strat_criteria["deal_potential"]["weight"]
        + competitive_score * strat_criteria["competitive_position"]["weight"]
    )
    scores["strategic"]["total"] = strat_total
    scores["strategic"]["weighted"] = strat_total * strat_weight

    # 5. CALCULATE OVERALL SCORE
    total_weighted = (
        scores["firmographic"]["weighted"]
        + scores["technographic"]["weighted"]
        + scores["behavioral"]["weighted"]
        + scores["strategic"]["weighted"]
    )

    scores["weighted_total"] = round(total_weighted, 2)

    # 6. ASSIGN TIER AND RECOMMENDATION
    if total_weighted >= 80:
        scores["tier"] = "A"
        scores["recommendation"] = (
            "High priority - Excellent fit. Pursue aggressively with personalized outreach."
        )
    elif total_weighted >= 60:
        scores["tier"] = "B"
        scores["recommendation"] = (
            "Good fit - Worth pursuing. Develop tailored messaging and multi-touch cadence."
        )
    elif total_weighted >= 40:
        scores["tier"] = "C"
        scores["recommendation"] = (
            "Moderate fit - Consider for nurture campaigns. Monitor for positive signals."
        )
    else:
        scores["tier"] = "D"
        scores["recommendation"] = (
            "Low priority - Poor fit. Deprioritize unless specific trigger events occur."
        )

    return scores


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(description="Qualify leads against ICP criteria")
    parser.add_argument(
        "--company-data",
        type=str,
        required=True,
        help="Path to JSON file with company data",
    )
    parser.add_argument(
        "--icp-criteria", type=str, help="Path to JSON file with custom ICP criteria"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="qualification_scores.json",
        help="Output file path (default: qualification_scores.json)",
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["json", "summary"],
        default="json",
        help="Output format (default: json)",
    )

    args = parser.parse_args()

    # Load company data
    try:
        with open(args.company_data) as f:
            company_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Company data file not found: {args.company_data}")
        return 1
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in company data file: {args.company_data}")
        return 1

    # Load ICP criteria if provided
    icp_criteria = None
    if args.icp_criteria:
        try:
            with open(args.icp_criteria) as f:
                icp_criteria = json.load(f)
        except FileNotFoundError:
            print(f"Error: ICP criteria file not found: {args.icp_criteria}")
            return 1
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in ICP criteria file: {args.icp_criteria}")
            return 1

    # Qualify the lead
    scores = qualify_lead(company_data, icp_criteria)

    # Output results
    if args.format == "json":
        output_data = {
            "company_name": company_data.get("company_name", "Unknown"),
            "qualification_date": "2025-10-18",  # In production, use datetime.now()
            "scores": scores,
        }

        with open(args.output, "w") as f:
            json.dump(output_data, f, indent=2)
        print(f"✓ Qualification scores saved to {args.output}")
    else:
        # Print summary to console
        print("\n" + "=" * 70)
        print("LEAD QUALIFICATION REPORT")
        print("=" * 70)

        print(f"\nCompany: {company_data.get('company_name', 'Unknown')}")
        print(f"Overall Score: {scores['weighted_total']}/100")
        print(f"Tier: {scores['tier']}")
        print(f"\nRecommendation: {scores['recommendation']}")

        print("\n--- Score Breakdown ---")
        print(
            f"Firmographic:   {scores['firmographic']['total']:.1f} (weighted: {scores['firmographic']['weighted']:.1f})"
        )
        print(
            f"Technographic:  {scores['technographic']['total']:.1f} (weighted: {scores['technographic']['weighted']:.1f})"
        )
        print(
            f"Behavioral:     {scores['behavioral']['total']:.1f} (weighted: {scores['behavioral']['weighted']:.1f})"
        )
        print(
            f"Strategic:      {scores['strategic']['total']:.1f} (weighted: {scores['strategic']['weighted']:.1f})"
        )

        print("\n" + "=" * 70 + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
