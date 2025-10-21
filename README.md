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


### Installation

#### 1: Clone the Repository

```bash
git clone https://github.com/yourusername/awesome-claude-skills.git
cd awesome-claude-skills
```

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

## 🤝 Contributing

We love contributions! Here's how you can help:

### Ways to Contribute

- 🐛 **Report Bugs** - Found an issue? [Open a bug report](https://github.com/yourusername/awesome-claude-skills/issues/new?template=bug_report.md)
- 💡 **Suggest Skills** - Have an idea? [Request a skill](https://github.com/yourusername/awesome-claude-skills/issues/new?template=skill_request.md)
- 📝 **Improve Docs** - Better docs = better skills
- 🔧 **Submit Skills** - Share your custom skills with the community

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
- [Example Skills Repository](https://github.com/anthropics/anthropic-cookbook)

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

---

<div align="center">


Made with ❤️ by the Claude Skills Community

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/awesome-claude-skills&type=Date)](https://star-history.com/#yourusername/awesome-claude-skills&Date)

</div>
