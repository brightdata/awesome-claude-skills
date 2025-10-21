#!/usr/bin/env python3
"""
Specification Validator for Spec-Driven Development

This script validates that a SPECIFICATION.md contains all required sections
and follows best practices.

Usage:
    python validate_spec.py --spec SPECIFICATION.md
"""

import argparse
import re
from pathlib import Path
from typing import List, Tuple, Dict


class SpecValidator:
    """Validates specification documents for completeness and quality."""

    REQUIRED_SECTIONS = [
        'Executive Summary',
        'Problem Statement',
        'Solution Overview',
        'User Experience',
        'Functional Requirements',
        'Non-Functional Requirements',
        'Success Metrics',
        'Constraints & Assumptions'
    ]

    RECOMMENDED_SECTIONS = [
        'Out of Scope',
        'Research Notes',
        'Dependencies',
        'Timeline & Milestones',
        'Open Questions'
    ]

    def __init__(self, spec_path: str):
        self.spec_path = Path(spec_path)
        self.content = self._read_file()
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []

    def _read_file(self) -> str:
        """Read specification file."""
        if not self.spec_path.exists():
            raise FileNotFoundError(f"Specification not found: {self.spec_path}")
        return self.spec_path.read_text()

    def check_required_sections(self) -> None:
        """Verify all required sections are present."""
        for section in self.REQUIRED_SECTIONS:
            pattern = f"##\\s+{re.escape(section)}"
            if not re.search(pattern, self.content):
                self.errors.append(f"Missing required section: '{section}'")

    def check_recommended_sections(self) -> None:
        """Check for recommended but optional sections."""
        for section in self.RECOMMENDED_SECTIONS:
            pattern = f"##\\s+{re.escape(section)}"
            if not re.search(pattern, self.content):
                self.warnings.append(f"Missing recommended section: '{section}'")

    def check_functional_requirements(self) -> None:
        """Validate functional requirements section."""
        pattern = r'##\s+Functional Requirements(.*?)(?=##|\Z)'
        match = re.search(pattern, self.content, re.DOTALL)

        if not match:
            self.errors.append("No Functional Requirements section found")
            return

        section = match.group(1)

        # Check for P0 requirements
        if 'P0' not in section and 'Must Have' not in section:
            self.warnings.append("No P0/Must Have requirements identified")

        # Check for acceptance criteria
        if '[ ]' not in section and 'Acceptance Criteria' not in section:
            self.warnings.append("Functional requirements lack acceptance criteria")

        # Count requirements
        req_pattern = r'\d+\.\s+\*\*(.+?)\*\*'
        requirements = re.findall(req_pattern, section)

        if len(requirements) == 0:
            self.errors.append("No functional requirements listed")
        elif len(requirements) > 20:
            self.warnings.append(f"Large number of requirements ({len(requirements)}). Consider splitting into phases.")
        else:
            self.info.append(f"Found {len(requirements)} functional requirements")

    def check_success_metrics(self) -> None:
        """Validate success metrics are measurable."""
        pattern = r'##\s+Success Metrics(.*?)(?=##|\Z)'
        match = re.search(pattern, self.content, re.DOTALL)

        if not match:
            self.errors.append("No Success Metrics section found")
            return

        section = match.group(1)

        # Look for table with metrics
        if '|' not in section:
            self.warnings.append("Success metrics should be in a table format")

        # Check for specific measurement methods
        keywords = ['measure', 'track', 'metric', 'kpi', 'target']
        if not any(keyword in section.lower() for keyword in keywords):
            self.warnings.append("Success metrics lack clear measurement methods")

    def check_user_journeys(self) -> None:
        """Validate user experience section has journeys."""
        pattern = r'##\s+User Experience(.*?)(?=##|\Z)'
        match = re.search(pattern, self.content, re.DOTALL)

        if not match:
            self.errors.append("No User Experience section found")
            return

        section = match.group(1)

        # Look for journey structure
        if 'Journey' not in section and 'User Flow' not in section:
            self.warnings.append("User Experience section lacks defined user journeys")

        # Check for triggers and outcomes
        if 'Trigger' not in section:
            self.warnings.append("User journeys should define triggers")

        if 'Success' not in section and 'Outcome' not in section:
            self.warnings.append("User journeys should define success outcomes")

    def check_research_backing(self) -> None:
        """Check if specification is backed by research."""
        pattern = r'##\s+Research Notes(.*?)(?=##|\Z)'
        match = re.search(pattern, self.content, re.DOTALL)

        if not match:
            self.warnings.append("No Research Notes section found. Specs should be backed by research.")
            return

        section = match.group(1)

        # Look for links to research sources
        url_pattern = r'https?://[^\s)]+'
        urls = re.findall(url_pattern, section)

        if len(urls) == 0:
            self.warnings.append("Research Notes lacks source links")
        else:
            self.info.append(f"Found {len(urls)} research sources")

        # Check for specific research types
        research_types = {
            'Competitive': 'competitive',
            'User Feedback': 'review|feedback|user',
            'Documentation': 'documentation|docs',
            'Technical': 'github|stackoverflow|technical'
        }

        for research_type, pattern in research_types.items():
            if not re.search(pattern, section, re.IGNORECASE):
                self.info.append(f"Consider adding {research_type} research")

    def check_constraints(self) -> None:
        """Validate constraints and assumptions are defined."""
        pattern = r'##\s+Constraints & Assumptions(.*?)(?=##|\Z)'
        match = re.search(pattern, self.content, re.DOTALL)

        if not match:
            self.errors.append("No Constraints & Assumptions section found")
            return

        section = match.group(1)

        if 'constraint' not in section.lower():
            self.warnings.append("No specific constraints identified")

        if 'assumption' not in section.lower():
            self.warnings.append("No assumptions documented")

    def check_out_of_scope(self) -> None:
        """Verify out of scope items are explicitly defined."""
        pattern = r'##\s+Out of Scope(.*?)(?=##|\Z)'
        match = re.search(pattern, self.content, re.DOTALL)

        if match:
            section = match.group(1)
            if len(section.strip()) < 50:
                self.warnings.append("Out of Scope section is very brief. Be explicit about what's excluded.")
            else:
                self.info.append("Out of Scope clearly defined")

    def check_document_metadata(self) -> None:
        """Check for version, date, and status metadata."""
        required_metadata = ['Version', 'Date', 'Status']

        for meta in required_metadata:
            pattern = f"\\*\\*{meta}\\*\\*:"
            if not re.search(pattern, self.content):
                self.warnings.append(f"Missing document metadata: {meta}")

    def check_approval_section(self) -> None:
        """Check for review and approval tracking."""
        if 'Review & Approval' not in self.content:
            self.info.append("Consider adding a Review & Approval section for stakeholder sign-off")

    def calculate_completeness_score(self) -> int:
        """Calculate a completeness score (0-100)."""
        score = 100

        # Deduct points for errors
        score -= len(self.errors) * 10

        # Deduct points for warnings
        score -= len(self.warnings) * 3

        return max(0, min(100, score))

    def validate(self) -> Dict[str, any]:
        """Run all validation checks."""
        print(f"🔍 Validating {self.spec_path}...\n")

        self.check_document_metadata()
        self.check_required_sections()
        self.check_recommended_sections()
        self.check_functional_requirements()
        self.check_success_metrics()
        self.check_user_journeys()
        self.check_research_backing()
        self.check_constraints()
        self.check_out_of_scope()
        self.check_approval_section()

        score = self.calculate_completeness_score()

        return {
            'score': score,
            'errors': self.errors,
            'warnings': self.warnings,
            'info': self.info
        }

    def print_results(self, results: Dict[str, any]) -> None:
        """Print validation results in a readable format."""
        score = results['score']

        # Print errors
        if results['errors']:
            print("❌ ERRORS (Must Fix):")
            for error in results['errors']:
                print(f"   • {error}")
            print()

        # Print warnings
        if results['warnings']:
            print("⚠️  WARNINGS (Should Address):")
            for warning in results['warnings']:
                print(f"   • {warning}")
            print()

        # Print info
        if results['info']:
            print("ℹ️  INFORMATION:")
            for info in results['info']:
                print(f"   • {info}")
            print()

        # Print score
        print(f"📊 Completeness Score: {score}/100")

        if score >= 90:
            print("✅ Excellent! Specification is comprehensive.")
        elif score >= 75:
            print("✅ Good! Address warnings to improve further.")
        elif score >= 60:
            print("⚠️  Fair. Address errors and warnings before proceeding.")
        else:
            print("❌ Needs work. Significant improvements required.")

        print()

        # Overall result
        if results['errors']:
            print("❌ VALIDATION FAILED - Please fix errors before proceeding to PLAN phase.")
            return False
        else:
            print("✅ VALIDATION PASSED - Ready to proceed to PLAN phase!")
            return True


def main():
    parser = argparse.ArgumentParser(
        description='Validate specification document for completeness and quality'
    )
    parser.add_argument(
        '--spec',
        type=str,
        required=True,
        help='Path to SPECIFICATION.md'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Treat warnings as errors'
    )

    args = parser.parse_args()

    try:
        validator = SpecValidator(args.spec)
        results = validator.validate()
        passed = validator.print_results(results)

        # If strict mode, fail on warnings
        if args.strict and results['warnings']:
            print("\n⚠️  Strict mode: Failing due to warnings")
            return 1

        # Fail if errors exist
        if not passed:
            return 1

        return 0

    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1


if __name__ == '__main__':
    exit(main())
