# Claude Platform Adapter

## Overview

This adapter enables **Agent Skills** to work with [Anthropic's Claude](https://www.anthropic.com/claude), allowing skills to be used as tools in Claude-powered agent systems.

## Setup

### 1. Install Dependencies

```bash
pip install anthropic agent-skills
```

### 2. Configure Skills for Claude

```python
import anthropic
from agent_skills import SkillRegistry

# Load skills
registry = SkillRegistry.from_file("registry.yaml")

# Create Anthropic client
client = anthropic.Anthropic()

# Get Claude-compatible tool definitions
tools = registry.to_claude_tools()

# Use with Claude
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    tools=tools,
    messages=[{"role": "user", "content": "Search GitHub for Python web frameworks"}]
)
```

### 3. Using Individual Skills

```python
from agent_skills import load_skill

# Load a specific skill
github_skill = load_skill("github")

# Get Claude-compatible tool definition
tool = github_skill.to_claude_tool()

# Use with Claude
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    tools=[tool],
    system=github_skill.system_prompt,
    messages=[{"role": "user", "content": "List open issues in my repo"}]
)
```

## Skill-to-Tool Mapping

| Skill | Claude Tool Name | Description |
|-------|------------------|-------------|
| notion | `notion_action` | Perform Notion operations |
| github | `github_action` | Perform GitHub operations |
| memory | `memory_action` | Manage agent memory |
| agent-builder | `agent_builder_action` | Build and orchestrate agents |

## Claude Projects Integration

For Claude Projects, skills can be added as project knowledge:

1. Create a Claude Project
2. Upload `SKILL.md` files as project knowledge
3. Claude will reference skill definitions in responses
4. Combine with tool use for full skill execution

## Environment Variables

```bash
export ANTHROPIC_API_KEY=your-anthropic-key
export NOTION_API_KEY=your-notion-key
export GITHUB_TOKEN=your-github-token
```

## Example: Skill Chain

```python
import anthropic
from agent_skills import load_skill

client = anthropic.Anthropic()

# Load multiple skills
notion = load_skill("notion")
github = load_skill("github")
memory = load_skill("memory")

# Combine tools
tools = [
    notion.to_claude_tool(),
    github.to_claude_tool(),
    memory.to_claude_tool(),
]

# Combined system prompt
system = "\n".join([
    notion.system_prompt,
    github.system_prompt,
    memory.system_prompt,
])

# Use all skills together
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    tools=tools,
    system=system,
    messages=[{"role": "user", 
               "content": "Remember that I prefer dark mode, then check my GitHub notifications"}]
)
```