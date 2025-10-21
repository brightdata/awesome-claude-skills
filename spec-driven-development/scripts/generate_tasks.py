#!/usr/bin/env python3
"""
Task Generator for Spec-Driven Development

This script analyzes a SPECIFICATION.md and TECHNICAL_PLAN.md to generate
a detailed TASKS.md breakdown with concrete, testable implementation tasks.

Usage:
    python generate_tasks.py --spec SPECIFICATION.md --plan TECHNICAL_PLAN.md --output TASKS.md
"""

import argparse
import re
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime


class TaskGenerator:
    def __init__(self, spec_path: str, plan_path: str):
        self.spec_path = Path(spec_path)
        self.plan_path = Path(plan_path)
        self.spec_content = self._read_file(self.spec_path)
        self.plan_content = self._read_file(self.plan_path)

    def _read_file(self, path: Path) -> str:
        """Read file contents."""
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        return path.read_text()

    def extract_requirements(self) -> List[str]:
        """Extract functional requirements from specification."""
        requirements = []

        # Look for "Functional Requirements" section
        pattern = r'##\s+Functional Requirements(.*?)(?=##|\Z)'
        match = re.search(pattern, self.spec_content, re.DOTALL)

        if match:
            section = match.group(1)
            # Extract P0, P1, P2 items
            req_pattern = r'\d+\.\s+\*\*(.+?)\*\*'
            requirements = re.findall(req_pattern, section)

        return requirements

    def extract_components(self) -> List[str]:
        """Extract system components from technical plan."""
        components = []

        # Look for "Component Design" section
        pattern = r'###\s+Component\s+\d+:\s+(.+?)\n'
        components = re.findall(pattern, self.plan_content)

        return components

    def extract_tech_stack(self) -> Dict[str, str]:
        """Extract technology stack decisions from plan."""
        stack = {
            'language': 'Python',  # Default
            'framework': 'FastAPI',
            'database': 'PostgreSQL',
            'cache': 'Redis'
        }

        # Try to extract from Technology Stack section
        pattern = r'\|\s+(\w+)\s+\|\s+\[([^\]]+)\]'
        matches = re.findall(pattern, self.plan_content)

        for component, tech in matches:
            component_lower = component.lower()
            if 'framework' in component_lower:
                stack['framework'] = tech.split(',')[0].strip()
            elif 'language' in component_lower:
                stack['language'] = tech.split(',')[0].strip()
            elif 'database' in component_lower or 'primary db' in component_lower:
                stack['database'] = tech.split(',')[0].strip()
            elif 'cache' in component_lower:
                stack['cache'] = tech.split(',')[0].strip()

        return stack

    def generate_setup_tasks(self, tech_stack: Dict[str, str]) -> List[Dict[str, Any]]:
        """Generate project setup and infrastructure tasks."""
        tasks = [
            {
                'id': '1.1',
                'name': 'Initialize Project Repository',
                'description': 'Set up the initial project repository with proper structure and CI/CD foundation.',
                'priority': 'P0',
                'estimated_hours': 0.5,
                'dependencies': [],
                'acceptance_criteria': [
                    'GitHub repository created with README',
                    f'.gitignore configured for {tech_stack["language"]}',
                    'Branch protection rules enabled on `main`',
                    'Initial project structure created',
                    'First commit pushed'
                ]
            },
            {
                'id': '1.2',
                'name': 'Set Up Development Environment',
                'description': 'Configure local development environment with dependencies and tools.',
                'priority': 'P0',
                'estimated_hours': 1.0,
                'dependencies': ['1.1'],
                'acceptance_criteria': [
                    f'{tech_stack["language"]} installed and verified',
                    'Virtual environment created',
                    'Dependencies file created',
                    'Development dependencies included (testing, linting)',
                    'Pre-commit hooks configured',
                    'Environment variables documented in `.env.example`'
                ]
            },
            {
                'id': '1.3',
                'name': 'Configure CI/CD Pipeline',
                'description': 'Set up automated testing and deployment workflow.',
                'priority': 'P0',
                'estimated_hours': 2.0,
                'dependencies': ['1.2'],
                'acceptance_criteria': [
                    'CI workflow file created',
                    'Pipeline runs on push and pull requests',
                    'Lint, type check, and test steps included',
                    'Docker image build step included',
                    'Security scan included',
                    'Status badge added to README'
                ]
            }
        ]

        # Add database setup if database is in stack
        if tech_stack.get('database'):
            tasks.append({
                'id': '1.4',
                'name': f'Set Up Database ({tech_stack["database"]})',
                'description': f'Configure {tech_stack["database"]} database for local development.',
                'priority': 'P0',
                'estimated_hours': 1.5,
                'dependencies': ['1.2'],
                'acceptance_criteria': [
                    'docker-compose.yml created with database service',
                    'Database initialized',
                    'Connection verified from application',
                    'Migration tool configured',
                    'Initial migration created',
                    'Seed data script created for development'
                ]
            })

        return tasks

    def generate_feature_tasks(self, requirements: List[str]) -> List[Dict[str, Any]]:
        """Generate implementation tasks for each feature requirement."""
        tasks = []
        base_id = 2

        for idx, req in enumerate(requirements[:3], 1):  # Limit to first 3 for demo
            # Create data model task
            tasks.append({
                'id': f'{base_id}.{idx * 3 - 2}',
                'name': f'Design {req} Data Model',
                'description': f'Create database schema and models for {req}.',
                'priority': 'P0',
                'estimated_hours': 1.0,
                'dependencies': ['1.4'],
                'acceptance_criteria': [
                    'Model class created with appropriate fields',
                    'Database migration generated',
                    'Migration applied to dev database',
                    'Constraints verified',
                    'Relationships configured'
                ]
            })

            # Create business logic task
            tasks.append({
                'id': f'{base_id}.{idx * 3 - 1}',
                'name': f'Implement {req} Business Logic',
                'description': f'Build core functionality for {req}.',
                'priority': 'P0',
                'estimated_hours': 2.0,
                'dependencies': [f'{base_id}.{idx * 3 - 2}'],
                'acceptance_criteria': [
                    'Core functions implemented',
                    'Input validation included',
                    'Error handling implemented',
                    'Unit tests written',
                    'Test coverage >80%'
                ]
            })

            # Create API endpoint task
            tasks.append({
                'id': f'{base_id}.{idx * 3}',
                'name': f'Create {req} API Endpoint',
                'description': f'Build REST API endpoint for {req}.',
                'priority': 'P0',
                'estimated_hours': 2.0,
                'dependencies': [f'{base_id}.{idx * 3 - 1}'],
                'acceptance_criteria': [
                    'Endpoint created with proper HTTP method',
                    'Request/response validation implemented',
                    'Authentication/authorization applied',
                    'Appropriate status codes returned',
                    'Integration test written',
                    'API documentation updated'
                ]
            })

        return tasks

    def generate_testing_tasks(self) -> List[Dict[str, Any]]:
        """Generate testing and QA tasks."""
        return [
            {
                'id': '4.1',
                'name': 'Achieve Target Test Coverage',
                'description': 'Write additional tests to reach 80% code coverage target.',
                'priority': 'P0',
                'estimated_hours': 4.0,
                'dependencies': ['*'],  # Depends on all implementation tasks
                'acceptance_criteria': [
                    'Coverage report generated',
                    'Overall coverage ≥80%',
                    'All critical paths covered',
                    'Edge cases tested',
                    'Coverage report uploaded to CI'
                ]
            },
            {
                'id': '4.2',
                'name': 'Write E2E Tests',
                'description': 'Create end-to-end tests for critical user journeys.',
                'priority': 'P1',
                'estimated_hours': 3.0,
                'dependencies': ['4.1'],
                'acceptance_criteria': [
                    'E2E test framework configured',
                    'Critical user journeys tested',
                    'Tests run against local environment',
                    'Screenshots captured on failure',
                    'Tests added to CI pipeline'
                ]
            }
        ]

    def generate_deployment_tasks(self) -> List[Dict[str, Any]]:
        """Generate documentation and deployment tasks."""
        return [
            {
                'id': '5.1',
                'name': 'Write API Documentation',
                'description': 'Generate interactive API documentation.',
                'priority': 'P1',
                'estimated_hours': 2.0,
                'dependencies': ['*'],  # Depends on all API tasks
                'acceptance_criteria': [
                    'Automatic docs enabled',
                    'All endpoints documented with descriptions',
                    'Request/response examples included',
                    'Error codes documented',
                    'Authentication flow explained',
                    'Interactive docs accessible'
                ]
            },
            {
                'id': '5.2',
                'name': 'Deploy to Staging Environment',
                'description': 'Deploy application to staging for QA testing.',
                'priority': 'P0',
                'estimated_hours': 4.0,
                'dependencies': ['4.2'],
                'acceptance_criteria': [
                    'Docker image built and pushed',
                    'Deployment manifests created',
                    'Environment variables configured',
                    'Database migration run',
                    'Health check responding',
                    'Application accessible via staging URL',
                    'Smoke tests pass'
                ]
            }
        ]

    def format_task(self, task: Dict[str, Any]) -> str:
        """Format a single task as markdown."""
        md = f"### Task {task['id']}: {task['name']}\n\n"
        md += f"**Status**: 🔵 Not Started\n"
        md += f"**Priority**: {task['priority']}\n"
        md += f"**Estimated Time**: {task['estimated_hours']} hours\n"
        md += f"**Dependencies**: {', '.join(task['dependencies']) if task['dependencies'] else 'None'}\n\n"
        md += f"**Description**:\n{task['description']}\n\n"
        md += "**Acceptance Criteria**:\n"
        for criteria in task['acceptance_criteria']:
            md += f"- [ ] {criteria}\n"
        md += "\n---\n\n"
        return md

    def generate(self, output_path: str) -> str:
        """Generate complete TASKS.md file."""
        print("🔍 Analyzing specification and technical plan...")

        # Extract information
        requirements = self.extract_requirements()
        components = self.extract_components()
        tech_stack = self.extract_tech_stack()

        print(f"✅ Found {len(requirements)} requirements")
        print(f"✅ Found {len(components)} components")
        print(f"✅ Tech stack: {tech_stack}")

        # Generate task groups
        setup_tasks = self.generate_setup_tasks(tech_stack)
        feature_tasks = self.generate_feature_tasks(requirements)
        testing_tasks = self.generate_testing_tasks()
        deployment_tasks = self.generate_deployment_tasks()

        all_tasks = setup_tasks + feature_tasks + testing_tasks + deployment_tasks
        total_hours = sum(t['estimated_hours'] for t in all_tasks)

        print(f"\n📋 Generated {len(all_tasks)} tasks ({total_hours} estimated hours)")

        # Build markdown
        output = f"""# Tasks: Implementation Breakdown

**Version**: 1.0
**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Based on**:
- [{self.spec_path.name}]({self.spec_path.name})
- [{self.plan_path.name}]({self.plan_path.name})

**Status Legend**: 🔵 Not Started | 🟡 In Progress | 🟢 Complete

---

## Summary

| Epic | Tasks | Est. Hours | Priority |
|------|-------|------------|----------|
| Epic 1: Setup | {len(setup_tasks)} | {sum(t['estimated_hours'] for t in setup_tasks):.1f} | P0 |
| Epic 2: Features | {len(feature_tasks)} | {sum(t['estimated_hours'] for t in feature_tasks):.1f} | P0 |
| Epic 3: Testing | {len(testing_tasks)} | {sum(t['estimated_hours'] for t in testing_tasks):.1f} | P0/P1 |
| Epic 4: Deployment | {len(deployment_tasks)} | {sum(t['estimated_hours'] for t in deployment_tasks):.1f} | P0/P1 |
| **Total** | **{len(all_tasks)}** | **{total_hours:.1f}** | |

**Estimated Timeline**: {total_hours / 40:.1f} weeks (assuming 40 hours/week, single engineer)

---

## Epic 1: Project Setup & Infrastructure

"""

        for task in setup_tasks:
            output += self.format_task(task)

        output += "\n## Epic 2: Feature Implementation\n\n"
        for task in feature_tasks:
            output += self.format_task(task)

        output += "\n## Epic 3: Testing & Quality Assurance\n\n"
        for task in testing_tasks:
            output += self.format_task(task)

        output += "\n## Epic 4: Documentation & Deployment\n\n"
        for task in deployment_tasks:
            output += self.format_task(task)

        output += """
---

## Notes

- Tasks can be parallelized where dependencies allow
- Estimated times are for implementation only (not including code review)
- Add 20-30% buffer for iteration
- Update this document as tasks are completed

---

**Next Step**: Assign tasks and begin Epic 1!
"""

        # Write output
        output_file = Path(output_path)
        output_file.write_text(output)
        print(f"\n✅ Tasks written to {output_path}")

        return output


def main():
    parser = argparse.ArgumentParser(
        description='Generate implementation tasks from specification and technical plan'
    )
    parser.add_argument(
        '--spec',
        type=str,
        required=True,
        help='Path to SPECIFICATION.md'
    )
    parser.add_argument(
        '--plan',
        type=str,
        required=True,
        help='Path to TECHNICAL_PLAN.md'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='TASKS.md',
        help='Output file path (default: TASKS.md)'
    )

    args = parser.parse_args()

    try:
        generator = TaskGenerator(args.spec, args.plan)
        generator.generate(args.output)
        print("\n🎉 Task generation complete!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1

    return 0


if __name__ == '__main__':
    exit(main())
