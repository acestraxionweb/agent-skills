# Skill: Notion Integration

## Metadata
- **Name**: notion
- **Version**: 0.1.0
- **Author**: acestraxionweb
- **Tags**: productivity, knowledge-base, documents, databases
- **Platforms**: openwebui, mcp, openai, claude

## Description

Read, create, update, and search Notion pages, databases, and blocks. This skill enables agents to interact with Notion workspaces as a knowledge base and documentation system.

## Trigger Patterns

Activate this skill when the user:
- Mentions "Notion" by name
- Asks to read, write, or search a Notion page
- Wants to query or modify a Notion database
- Needs to create or update documentation
- References a Notion URL or page ID

## Instructions

### Reading Pages
1. Identify the page reference (URL, page ID, or title search)
2. Use the Notion API to retrieve the page content
3. Parse blocks into readable format
4. Present the content to the user with proper formatting

### Writing Pages
1. Identify the target page or parent (page, database, or workspace)
2. Determine the content structure (headings, paragraphs, lists, code blocks)
3. Build the block array according to Notion's block schema
4. Create or update the page with the constructed blocks
5. Confirm success and provide the page link

### Querying Databases
1. Identify the database reference (URL, ID, or name)
2. Construct filters based on user criteria
3. Execute the query with appropriate sorting
4. Format results as a table or structured list
5. Offer follow-up actions (create entry, modify filter, etc.)

### Searching
1. Construct a search query from user intent
2. Search across pages, databases, and workspace
3. Rank results by relevance
4. Present top results with previews

## Input Format

```json
{
  "action": "read | create | update | search | query",
  "target": "page_id | database_id | search_term",
  "content": {},
  "filters": {},
  "options": {}
}
```

## Output Format

```json
{
  "status": "success | error",
  "data": {},
  "message": "Human-readable summary",
  "links": []
}
```

## Examples

### Example 1: Read a Page
**User**: "Read my Notion page about project roadmap"
**Agent Action**:
1. Search for page titled "project roadmap"
2. Retrieve page content
3. Present formatted content to user

### Example 2: Create a Page
**User**: "Create a meeting notes page for today's standup"
**Agent Action**:
1. Create page with title "Meeting Notes - [date] - Standup"
2. Add template blocks: attendees, agenda, notes, action items
3. Return page link

### Example 3: Query Database
**User**: "Show me all tasks with status 'In Progress' from my project board"
**Agent Action**:
1. Query project board database
2. Filter by status = "In Progress"
3. Return formatted task list

## Constraints

- Requires valid Notion API token (configured in platform settings)
- Notion API rate limits apply (3 requests per second)
- Database queries limited to 100 results per request
- File uploads must be under 5MB
- Rich text blocks have a maximum of 2000 characters

## Platform-Specific Notes

- **Open WebUI**: Configure via `Settings > Integrations > Notion`
- **MCP**: Use the `notion-mcp-server` adapter
- **OpenAI**: Pass Notion token via environment variable `NOTION_API_KEY`
- **Claude**: Supports direct Notion API calls via tool use