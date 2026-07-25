# Notion Skill for Agent Skills

A portable skill that enables AI agents to interact with Notion workspaces.

## What It Does

- **Read** Notion pages and databases
- **Create** new pages with structured content
- **Update** existing pages and their blocks
- **Search** across your entire Notion workspace
- **Query** databases with filters and sorting

## Setup

### 1. Create a Notion Integration

1. Go to [Notion My Integrations](https://www.notion.so/my-integrations)
2. Click **"New integration"**
3. Give it a name (e.g., "Agent Skills")
4. Select the workspace you want to connect
5. Copy the **Internal Integration Token**

### 2. Connect to Notion

1. Open any Notion page you want the agent to access
2. Click **`...`** menu → **"Add connections"**
3. Search for your integration name and select it
4. Repeat for each page/database the agent needs

### 3. Configure the Skill

Set the Notion API token in your platform:

| Platform | Configuration |
|----------|---------------|
| Open WebUI | Settings → Integrations → Notion → API Token |
| MCP | Set `NOTION_API_KEY` environment variable |
| OpenAI | Set `NOTION_API_KEY` environment variable |
| Claude | Set `NOTION_API_KEY` environment variable |

## Example Usage

```
User: "What's on my Notion project page?"
Agent: [Reads and presents page content]

User: "Add a new task to my project board"
Agent: [Creates a new database entry with provided details]

User: "Find all meeting notes from this week"
Agent: [Queries database with date filter and presents results]
```

## Supported Operations

| Operation | Description | Status |
|-----------|-------------|--------|
| `search` | Search across workspace | ✅ |
| `read_page` | Read page content | ✅ |
| `create_page` | Create new page | ✅ |
| `update_page` | Update existing page | ✅ |
| `query_database` | Query database with filters | ✅ |
| `create_database_entry` | Add entry to database | ✅ |
| `list_recent_pages` | List recently modified pages | ✅ |

## Permissions Required

- `Read content` — Read pages and databases
- `Insert content` — Create and update pages
- `Update content` — Modify existing content

---

See [`SKILL.md`](./SKILL.md) for the full skill definition.