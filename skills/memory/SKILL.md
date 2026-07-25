# Skill: Agent Memory

## Metadata
- **Name**: memory
- **Version**: 0.1.0
- **Author**: acestraxionweb
- **Tags**: memory, context-management, knowledge-retrieval, persistence
- **Platforms**: openwebui, mcp, openai, claude

## Description

Manage agent memory systems including short-term conversation context, long-term knowledge storage, and semantic retrieval. This skill enables agents to remember user preferences, past interactions, and learned knowledge across sessions.

## Trigger Patterns

Activate this skill when the user:
- Says "remember this" or "don't forget"
- Asks "what do you remember about..."
- Needs to recall previous conversation context
- Wants to store or retrieve persistent information
- References past interactions or preferences
- Asks to clear or manage stored memories

## Instructions

### Storing Memories
1. **Identify the memory type**:
   - `fact` — Objective information (dates, names, specifications)
   - `preference` — User preferences (communication style, tools, etc.)
   - `context` — Conversational context for future reference
   - `instruction` — Rules or guidelines to follow
   - `episodic` — Past events or interactions

2. **Extract key information**:
   - Determine what to remember
   - Associate with relevant categories/tags
   - Set importance level (low, medium, high)
   - Optionally set expiration time

3. **Store the memory**:
   - Save to the configured memory store
   - Confirm storage with a summary

### Retrieving Memories
1. **Search by query**: Semantic search across all stored memories
2. **Filter by type**: Retrieve only specific memory types
3. **Filter by time**: Get memories from a specific time range
4. **Rank by relevance**: Return most relevant memories first

### Managing Memories
1. **List**: Browse all stored memories with filters
2. **Update**: Modify existing memories with new information
3. **Delete**: Remove outdated or incorrect memories
4. **Categorize**: Organize memories into collections or tags

## Memory Types

| Type | Description | TTL | Example |
|------|-------------|-----|---------|
| `fact` | Objective information | Long-term | "User's birthday is March 15" |
| `preference` | User preferences | Long-term | "Prefers dark mode" |
| `context` | Conversation context | Session-based | "Currently working on project X" |
| `instruction` | Rules/guidelines | Long-term | "Always respond in formal tone" |
| `episodic` | Past events | Medium-term | "Discussed pricing on July 10" |

## Input Format

```json
{
  "action": "store | retrieve | search | list | update | delete",
  "memory": {
    "type": "fact | preference | context | instruction | episodic",
    "content": "string",
    "tags": [],
    "importance": "low | medium | high",
    "ttl": "duration"
  },
  "query": "search term",
  "filters": {}
}
```

## Output Format

```json
{
  "status": "success | error",
  "memories": [],
  "count": 0,
  "message": "Human-readable summary"
}
```

## Examples

### Example 1: Store a Preference
**User**: "Remember that I prefer concise responses"
**Agent Action**:
1. Create memory of type `preference`
2. Content: "User prefers concise responses"
3. Importance: high
4. Store and confirm

### Example 2: Retrieve Facts
**User**: "What do you know about my project timeline?"
**Agent Action**:
1. Search memories for "project timeline"
2. Filter by type: fact, context
3. Return matching memories ranked by relevance
4. Summarize findings

### Example 3: List Recent Memories
**User**: "What have we discussed this week?"
**Agent Action**:
1. List memories from the past 7 days
2. Filter by type: episodic, context
3. Present chronological summary

## Constraints

- Memory storage depends on platform's memory backend (mem0, SQLite, etc.)
- Maximum memory size: 10KB per entry
- Semantic search requires embedding model support
- Default retention: 90 days for episodic, indefinite for facts/preferences
- Total memory limit: platform-dependent (typically 10,000 entries)

## Platform-Specific Notes

- **Open WebUI**: Uses built-in memory system
- **MCP**: Compatible with mem0-mcp-server
- **OpenAI**: Uses thread-based context + custom store
- **Claude**: Uses project knowledge + conversation context