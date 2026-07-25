# OpenAI Agents Platform Adapter

## Overview

This adapter enables **Agent Skills** to work with [OpenAI's Agents SDK](https://github.com/openai/openai-agents-python), allowing skills to be used as tools in OpenAI-powered agent systems.

## Setup

### 1. Install the SDK

```bash
pip install openai-agents
```

### 2. Configure Skills

```python
from agent_skills import SkillRegistry
from openai_agents import Agent, Runner

# Load skills
registry = SkillRegistry.from_file("registry.yaml")

# Create an agent with skills
agent = Agent(
    name="assistant",
    instructions="You are a helpful assistant with access to these skills:
" + registry.describe_all(),
    tools=registry.to_openai_tools(),
)

# Run the agent
result = Runner.run_sync(agent, "Search GitHub for Python web frameworks")
print(result.final_output)
```

### 3. Using Individual Skills

```python
from agent_skills import load_skill

# Load a specific skill
notion_skill = load_skill("notion")

# Get OpenAI-compatible tool definition
tool = notion_skill.to_openai_tool()

# Use with any OpenAI agent
agent = Agent(
    name="notion-agent",
    instructions=notion_skill.system_prompt,
    tools=[tool],
)
```

## Skill-to-Tool Mapping

| Skill | OpenAI Tool Name | Description |
|-------|------------------|-------------|
| notion | `notion_action` | Perform Notion operations |
| github | `github_action` | Perform GitHub operations |
| memory | `memory_action` | Manage agent memory |
| agent-builder | `agent_builder_action` | Build and orchestrate agents |

## Environment Variables

```bash
export OPENAI_API_KEY=your-openai-key
export NOTION_API_KEY=your-notion-key
export GITHUB_TOKEN=your-github-token
```

## Example: Multi-Skill Agent

```python
from agent_skills import SkillRegistry
from openai_agents import Agent, Runner

registry = SkillRegistry.from_file("registry.yaml")

agent = Agent(
    name="multi-skill-agent",
    instructions="""You are a versatile assistant.
    You can manage Notion pages, work with GitHub,
    and remember user preferences.""",
    tools=registry.to_openai_tools(),
)

# The agent can now use any registered skill
result = Runner.run_sync(agent, 
    "Create a Notion page summarizing the open issues in my GitHub repo")
```