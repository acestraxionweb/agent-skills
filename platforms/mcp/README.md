# MCP Platform Adapter

## Overview

This adapter enables **Agent Skills** to work with the [Model Context Protocol](https://modelcontextprotocol.io/) (MCP), allowing any MCP-compatible client to use the skills.

## What is MCP?

MCP is an open protocol that standardizes how AI applications connect to external data sources and tools. It provides a universal interface for:

- **Tools**: Functions the agent can call
- **Resources**: Data the agent can access
- **Prompts**: Pre-built prompt templates

## Setup

### 1. Install MCP Server

```bash
npm install -g agent-skills-mcp
# or
pip install agent-skills-mcp
```

### 2. Configure Your MCP Client

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "agent-skills": {
      "command": "agent-skills-mcp",
      "args": ["--config", "/path/to/config.yaml"],
      "env": {
        "NOTION_API_KEY": "your-notion-key",
        "GITHUB_TOKEN": "your-github-token"
      }
    }
  }
}
```

### 3. Available Tools

Each skill is exposed as an MCP tool:

| MCP Tool | Skill | Description |
|----------|-------|-------------|
| `notion_read_page` | notion | Read a Notion page |
| `notion_query_database` | notion | Query a Notion database |
| `github_search_repos` | github | Search GitHub repositories |
| `github_create_issue` | github | Create a GitHub issue |
| `memory_store` | memory | Store a memory |
| `memory_search` | memory | Search memories |
| `agent_builder_define` | agent-builder | Define a new agent |

## MCP Resources

Skills also expose resources for data access:

```
agent-skills://registry       → Skill registry data
agent-skills://skills/{name}  → Skill definition
agent-skills://config         → Current configuration
```

## Supported Clients

- ✅ Claude Desktop
- ✅ Cursor
- ✅ Windsurf
- ✅ Zed
- ✅ Cline
- ✅ Any MCP-compatible client