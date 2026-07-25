# 🧠 Agent Skills

A portable, platform-agnostic skill registry for AI agents. Skills are reusable capabilities that can be shared across different agent systems — from Open WebUI to MCP, OpenAI, Claude, and beyond.

## 🎯 What Are Agent Skills?

Agent Skills are modular, self-contained capability definitions that teach AI agents how to perform specific tasks. Each skill is defined in a standard `SKILL.md` format that can be:

- **Shared** across different agent platforms
- **Discovered** via the machine-readable `registry.yaml`
- **Extended** by anyone via pull request
- **Adapted** to specific platforms via adapter wrappers

## 📁 Repository Structure

```
agent-skills/
├── README.md              # This file
├── registry.yaml          # Machine-readable skill inventory
├── CONTRIBUTING.md        # How to add new skills
├── CHANGELOG.md           # Version history
│
├── skills/                # Canonical skill definitions
│   ├── notion/            # Notion integration skill
│   ├── github/            # GitHub operations skill
│   ├── memory/            # Agent memory management skill
│   └── agent-builder/     # Agent construction skill
│
├── platforms/             # Platform-specific adapters
│   ├── openwebui/         # Open WebUI adapter
│   ├── mcp/               # Model Context Protocol adapter
│   ├── openai/            # OpenAI agents adapter
│   └── claude/            # Claude agents adapter
│
└── templates/             # Templates for new skills
    ├── SKILL.template.md
    └── agent.template.yaml
```

## 🚀 Quick Start

### For Agent Users

1. Browse skills in the [`skills/`](./skills/) directory
2. Check [`registry.yaml`](./registry.yaml) for a machine-readable overview
3. Follow the platform-specific guides in [`platforms/`](./platforms/)

### For Skill Authors

1. Read [`CONTRIBUTING.md`](./CONTRIBUTING.md)
2. Use the template in [`templates/SKILL.template.md`](./templates/SKILL.template.md)
3. Submit a pull request!

## 📋 Skill Registry

The [`registry.yaml`](./registry.yaml) file provides a machine-readable inventory of all skills:

```bash
# Example: list all skills and their descriptions
python -c "import yaml; [print(f'{s[\"name\"]}: {s[\"description\"]}') for s in yaml.safe_load(open('registry.yaml'))['skills']]"
```

## 🌐 Platform Support

| Platform | Status | Adapter Location |
|----------|--------|------------------|
| Open WebUI | ✅ Supported | [`platforms/openwebui/`](./platforms/openwebui/) |
| MCP | ✅ Supported | [`platforms/mcp/`](./platforms/mcp/) |
| OpenAI Agents | ✅ Supported | [`platforms/openai/`](./platforms/openai/) |
| Claude | ✅ Supported | [`platforms/claude/`](./platforms/claude/) |
| Coding Agents | ✅ Native | Skills work directly |

## 📄 License

This project is open source. See the repository for license details.

---

**Built with ❤️ for the AI agent community**