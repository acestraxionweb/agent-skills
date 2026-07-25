# Agent Skills

Source of truth for agent skills, agents, and capability definitions.

Every skill follows the **WHAT / WHY / WHERE / WHEN / HOW** framework — turning each skill from a prompt file into a capability definition an agent can route to.

---

## Structure

```
agent-skills/
├── skills/           ← Canonical skill definitions
├── agents/           ← Agent configurations using skills
├── templates/        ← Templates for new skills and agents
├── registry.yaml     ← Machine-readable index
└── CONTRIBUTING.md   ← How to add new skills
```

---

## Skills

| Skill | Domain | Description |
|-------|--------|-------------|
| `notion/ticket-management` | Notion | Create, track, manage operational tasks |
| `notion/documentation` | Notion | MOP, SOP, KB, and technical documentation |
| `notion/knowledge-base` | Notion | Capture and retrieve reusable knowledge |
| `github/repo-management` | GitHub | Repository and code operations |
| `memory/context-management` | Memory | Persistent agent memory across sessions |

---

## Agents

Agents are configurations that combine skills into purpose-built assistants.

| Agent | Skills Used | Purpose |
|-------|-------------|---------|
| *(define as needed)* | | |

---

## Quick Start

**Use a skill:** Reference the `SKILL.md` in your agent system prompt or tool config.

**Add a skill:** Follow `CONTRIBUTING.md` — copy the template, fill the 5W matrix, submit.

---

## The 5W Framework

Every skill MUST answer five questions:

| Question | Purpose |
|----------|---------|
| **WHAT** | Can the agent do? Inputs, outputs, capabilities |
| **WHY** | Should this skill exist? Business value |
| **WHEN** | Should the agent activate it? Triggers and anti-triggers |
| **WHERE** | Does it operate? Systems, domains, environments |
| **HOW** | Does it execute? Steps, tools, decision logic |

This eliminates **skill ambiguity** — the agent knows exactly when to load a skill, what it can do, and when NOT to use it.

---

## Templates

- **New skill:** Copy `templates/SKILL.template.md` into `skills/<domain>/<skill-name>/SKILL.md`
- **New agent:** Copy `templates/agent.template.yaml` into `agents/<agent-name>.yaml`

---

## License

MIT.
