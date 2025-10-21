<div align="center">

<img src=assets/banner.jpg>


### A curated collection of powerful, production-ready skills for Claude

[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)

[Features](#-features) • [Skills](#-available-skills) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 📖 About

**Awesome Claude Skills** is a comprehensive collection of custom skills that supercharge Claude's capabilities across business workflows, data analysis, automation, and specialized domains. Each skill is production-ready, well-documented, and designed following Anthropic's best practices.

Skills extend Claude's expertise with:
- 🧠 **Specialized Knowledge** - Domain-specific expertise and methodologies
- 🔧 **Custom Workflows** - Multi-step processes and automation
- 📊 **Data Processing** - Scripts for batch operations and reporting
- 🎨 **Templates & Examples** - Ready-to-use patterns and references

## ✨ Features

<table>
<tr>
<td width="33.3%">

### Best Practices
- Follows Anthropic's skill authoring guidelines
- Progressive disclosure architecture
- Concise, token-optimized instructions
- Modular, maintainable structure

</td>
</tr>
<tr>
<td width="33.3%">

### Extensible
- Easy customization for your use case
- Compatible with MCP tools
- Works with Bright Data, GitHub, and more
- Composable with other skills

</td>
<td width="33.3%">

### Well-Documented
- Comprehensive README for each skill
- Usage examples and templates
- Troubleshooting guides
- API references

</td>
</tr>
</table>

## 🎯 Available Skills

### 🔍 Lead Research Assistant

<img src="https://img.shields.io/badge/Status-Stable-success?style=flat-square" alt="Stable"> <img src="https://img.shields.io/badge/Category-Sales%20%26%20Marketing-blue?style=flat-square" alt="Sales & Marketing"> <img src="https://img.shields.io/badge/MCP-Bright%20Data-orange?style=flat-square" alt="Bright Data">

**Identify, qualify, and engage high-potential leads with intelligent web research and systematic analysis.**

<details>
<summary><b>📋 Features & Capabilities</b></summary>

#### Core Capabilities
- 🌐 **Intelligent Discovery** - Find leads using smart Google queries + LinkedIn/Crunchbase/ZoomInfo
- 📊 **Custom Qualification** - Score leads against your ICP with 4-dimensional framework
- 👥 **Contact Intelligence** - Identify decision-makers and build relationship maps
- ✉️ **Outreach Strategy** - Generate personalized messaging with 50+ templates
- 📈 **Batch Processing** - Process hundreds of leads from CSV/Excel files
- 📑 **Excel Reporting** - Professional reports with charts and recommendations

#### Use Cases
- **Outbound Prospecting** - Build targeted lead lists from minimal criteria
- **Inbound Qualification** - Score and prioritize incoming leads
- **Market Research** - Analyze TAM and competitive landscape
- **Account-Based Marketing** - Deep research on strategic accounts

#### Tech Stack
- **Bright Data MCP Tools** - LinkedIn, Crunchbase, ZoomInfo, Google Search
- **Python Scripts** - Batch processing, qualification engine, report generation
- **Excel Output** - openpyxl for professional formatting

</details>

<details>
<summary><b>🚀 Quick Start Example</b></summary>

```
Research "Stripe" as a potential lead for our API testing platform.
We target fintech companies with 200-1000 employees.
```

**Claude will:**
1. Ask clarifying questions about your ICP
2. Search LinkedIn, Crunchbase, and ZoomInfo
3. Qualify the lead (A/B/C/D tier)
4. Provide personalized outreach strategy

**For batch processing:**
```
Process leads.csv and generate an Excel report with top 20 qualified leads
```

</details>

[📖 View Documentation](custom_skills/lead-research-assistant/) | [⬇️ Download Skill](custom_skills/lead-research-assistant/)

---

### 🏗️ Skill Builder *(Coming Soon)*

<img src="https://img.shields.io/badge/Status-In%20Development-yellow?style=flat-square" alt="In Development"> <img src="https://img.shields.io/badge/Category-Development-purple?style=flat-square" alt="Development">

**Build high-quality custom Claude skills with guided workflows and best practice templates.**

- 📝 Interactive skill scaffolding
- ✅ Validation and quality checks
- 📚 Template library for common patterns
- 🎯 Best practice guidance

---

## 🚀 Quick Start

### Prerequisites

1. **Claude with Skills Support**
   - Claude Code (desktop app)
   - Claude API with Skills beta access

2. **Optional: Bright Data MCP** (for Lead Research Assistant)
   ```bash
   # Install Bright Data MCP server
   npm install -g @brightdata/mcp-server
   ```

### Installation

#### Option 1: Clone the Repository

```bash
git clone https://github.com/yourusername/awesome-claude-skills.git
cd awesome-claude-skills
```

#### Option 2: Download Individual Skills

Download the skill folder you need from [`custom_skills/`](custom_skills/) directory.

### Using Skills with Claude

#### In Claude Code (Desktop App)

1. Open Claude Code Settings
2. Navigate to Skills section
3. Click "Add Skill" → "From Folder"
4. Select the skill directory (e.g., `custom_skills/lead-research-assistant`)
5. Skill is now available in all conversations!

#### Via Claude API

```python
from anthropic import Anthropic
from anthropic.lib import files_from_dir

client = Anthropic(api_key="your-api-key")

# Upload skill
skill = client.beta.skills.create(
    display_title="Lead Research Assistant",
    files=files_from_dir("custom_skills/lead-research-assistant")
)

# Use in conversation
response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4096,
    container={
        "skills": [{
            "type": "custom",
            "skill_id": skill.id,
            "version": "latest"
        }]
    },
    messages=[{
        "role": "user",
        "content": "Research Anthropic as a potential lead"
    }]
)
```

## 📚 Documentation

### For Users

- **[Skills Overview](docs/SKILLS_OVERVIEW.md)** - Understand how skills work
- **[Installation Guide](docs/INSTALLATION.md)** - Detailed setup instructions
- **[Usage Examples](docs/EXAMPLES.md)** - Real-world use cases
- **[Troubleshooting](docs/TROUBLESHOOTING.md)** - Common issues and solutions

### For Developers

- **[Creating Skills](docs/CREATING_SKILLS.md)** - Build your own skills
- **[Best Practices](docs/BEST_PRACTICES.md)** - Anthropic's authoring guidelines
- **[API Reference](docs/API_REFERENCE.md)** - Skills API documentation
- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute

## 🗂️ Repository Structure

```
awesome-claude-skills/
├── custom_skills/                 # 📁 All custom skills
│   ├── lead-research-assistant/   # 🔍 Lead research & qualification
│   │   ├── SKILL.md              # Main skill instructions
│   │   ├── REFERENCE.md          # ICP framework & criteria
│   │   ├── OUTREACH.md           # Message templates
│   │   ├── README.md             # Skill documentation
│   │   ├── scripts/              # Python automation scripts
│   │   └── sample_leads.csv      # Example data
│   └── skill-builder/            # 🏗️ Skill creation assistant
├── docs/                          # 📚 General documentation
├── examples/                      # 💡 Usage examples
└── README.md                      # You are here!
```

## 🎯 Skill Categories

### 📊 Business & Analytics
- [x] **Lead Research Assistant** - Sales prospecting and qualification

### 🛠️ Development Tools
- [ ] **Skill Builder** - Create custom skills (coming soon)

### 📝 Content & Writing
- [ ] **Content Strategy Generator** (planned)
- [ ] **SEO Optimizer** (planned)

### 🔬 Data & Research
- [ ] **Competitive Intelligence** (planned)
- [ ] **Market Analysis** (planned)

### 🎨 Design & Creative
- [ ] **Brand Guidelines Enforcer** (planned)

*Want to see a specific skill?* [Open an issue](https://github.com/yourusername/awesome-claude-skills/issues/new) with your request!

## 🤝 Contributing

We love contributions! Here's how you can help:

### Ways to Contribute

- 🐛 **Report Bugs** - Found an issue? [Open a bug report](https://github.com/yourusername/awesome-claude-skills/issues/new?template=bug_report.md)
- 💡 **Suggest Skills** - Have an idea? [Request a skill](https://github.com/yourusername/awesome-claude-skills/issues/new?template=skill_request.md)
- 📝 **Improve Docs** - Better docs = better skills
- 🔧 **Submit Skills** - Share your custom skills with the community

### Contribution Guidelines

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-skill`)
3. **Follow** our [skill authoring guidelines](docs/BEST_PRACTICES.md)
4. **Test** thoroughly with multiple scenarios
5. **Document** everything (README, examples, troubleshooting)
6. **Commit** your changes (`git commit -m 'Add amazing skill'`)
7. **Push** to the branch (`git push origin feature/amazing-skill`)
8. **Open** a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📋 Skill Quality Standards

All skills in this repository meet these standards:

- ✅ **Well-Documented** - Comprehensive README, usage examples, troubleshooting
- ✅ **Production-Ready** - Tested, error handling, edge cases covered
- ✅ **Best Practices** - Follows Anthropic's skill authoring guidelines
- ✅ **Maintainable** - Clear structure, commented code, version control
- ✅ **User-Friendly** - Clear instructions, helpful error messages
- ✅ **Token-Efficient** - Concise instructions, progressive disclosure

## 🎓 Learning Resources

### Official Documentation
- [Claude Skills Documentation](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview)
- [Skills Best Practices](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/best-practices)
- [Skills API Reference](https://docs.anthropic.com/en/api/skills-guide)

### Community Resources
- [Skills Engineering Blog](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Example Skills Repository](https://github.com/anthropics/anthropic-cookbook)
- [Claude Developer Discord](https://discord.gg/anthropic)

### Tutorials
- [Creating Your First Skill](docs/tutorials/FIRST_SKILL.md)
- [Advanced Skill Patterns](docs/tutorials/ADVANCED_PATTERNS.md)
- [Debugging Skills](docs/tutorials/DEBUGGING.md)

## 💬 Community & Support

- 💭 **Discussions** - [GitHub Discussions](https://github.com/yourusername/awesome-claude-skills/discussions)
- 🐛 **Issues** - [Bug Reports & Feature Requests](https://github.com/yourusername/awesome-claude-skills/issues)
- 📧 **Contact** - [Email Us](mailto:your.email@example.com)
- 🐦 **Twitter** - [@YourHandle](https://twitter.com/yourhandle)

## 📊 Statistics

<div align="center">

| Metric | Count |
|--------|-------|
| 🎯 Total Skills | 2 (1 stable, 1 in development) |
| 📝 Lines of Documentation | 5,000+ |
| 🔧 Python Scripts | 8 |
| 📚 Templates | 50+ |
| ⭐ GitHub Stars | ![Stars](https://img.shields.io/github/stars/yourusername/awesome-claude-skills?style=social) |
| 🍴 Forks | ![Forks](https://img.shields.io/github/forks/yourusername/awesome-claude-skills?style=social) |

</div>

## 🗺️ Roadmap

### Q1 2025
- [x] Lead Research Assistant v1.0
- [ ] Skill Builder v1.0
- [ ] Documentation site
- [ ] Video tutorials

### Q2 2025
- [ ] 5+ new skills in various categories
- [ ] Claude Code extension
- [ ] Community skill marketplace
- [ ] Skill composition framework

### Q3 2025
- [ ] Enterprise skill library
- [ ] Skill analytics and metrics
- [ ] Multi-language support
- [ ] Advanced MCP integrations

[View Full Roadmap](docs/ROADMAP.md)

## 🏆 Hall of Fame

### Top Contributors

<!-- Update with actual contributors -->
<a href="https://github.com/yourusername/awesome-claude-skills/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yourusername/awesome-claude-skills" />
</a>

### Featured Community Skills

*Submit your skill to be featured here!*

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License - Copyright (c) 2025 Awesome Claude Skills Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
[...]
```

## 🙏 Acknowledgments

- **Anthropic** - For creating Claude and the Skills framework
- **Bright Data** - For powerful MCP web scraping tools
- **Contributors** - Everyone who has contributed skills and improvements
- **Community** - For feedback, bug reports, and feature requests

## ⚡ Quick Links

<div align="center">

[![Documentation](https://img.shields.io/badge/📚-Documentation-blue?style=for-the-badge)](docs/)
[![Examples](https://img.shields.io/badge/💡-Examples-green?style=for-the-badge)](examples/)
[![API Reference](https://img.shields.io/badge/🔧-API%20Reference-orange?style=for-the-badge)](docs/API_REFERENCE.md)
[![Discord](https://img.shields.io/badge/💬-Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/yourserver)

</div>

---

<div align="center">

**[⬆ Back to Top](#-awesome-claude-skills)**

Made with ❤️ by the Claude Skills Community

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/awesome-claude-skills&type=Date)](https://star-history.com/#yourusername/awesome-claude-skills&Date)

</div>
