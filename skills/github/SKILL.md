# Skill: GitHub Operations

## Metadata
- **Name**: github
- **Version**: 0.1.0
- **Author**: acestraxionweb
- **Tags**: development, version-control, code-management, collaboration
- **Platforms**: openwebui, mcp, openai, claude

## Description

Manage GitHub repositories, issues, pull requests, branches, and code. This skill enables agents to perform common GitHub workflows including code review, issue triage, and repository management.

## Trigger Patterns

Activate this skill when the user:
- Mentions "GitHub" by name
- Asks to manage, create, or search repositories
- Wants to create or review pull requests
- Needs to work with issues (create, list, close)
- Wants to read or write code files in a repository
- References a GitHub URL or repository name

## Instructions

### Repository Operations
1. **Search**: Query GitHub for repositories by name, topic, or language
2. **Read**: Fetch repository metadata, README, file contents
3. **Create**: Initialize new repositories with configuration
4. **Clone/Fork**: Fork existing repositories for modification

### Issue Management
1. **List**: Browse issues with filters (label, state, assignee)
2. **Create**: File new issues with title, body, labels, and assignees
3. **Update**: Modify issue state, labels, or assignments
4. **Comment**: Add comments or updates to existing issues

### Pull Request Workflow
1. **Create**: Open PRs from branches with title and description
2. **Review**: Read PR diffs, file changes, and comments
3. **Merge**: Merge approved PRs with chosen strategy
4. **Comment**: Provide review feedback

### Code Operations
1. **Read Files**: Fetch file contents from any branch
2. **Create/Update Files**: Write or modify files via commits
3. **Browse Directory**: List files and folders in a path
4. **Branch Operations**: Create, list, and manage branches

## Input Format

```json
{
  "action": "search | create_repo | list_issues | create_issue | create_pr | read_file | commit_files | ...",
  "params": {},
  "repository": "owner/repo",
  "branch": "branch-name"
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

### Example 1: Search Repositories
**User**: "Find popular Python web scraping libraries on GitHub"
**Agent Action**:
1. Search GitHub for repos matching `python web scraping`
2. Sort by stars
3. Present top results with descriptions and links

### Example 2: Create an Issue
**User**: "Create an issue for the login bug in my-project"
**Agent Action**:
1. Create issue with title "Bug: Login not working"
2. Add description template
3. Apply "bug" label
4. Return issue link

### Example 3: Review a Pull Request
**User**: "Show me the changes in PR #42"
**Agent Action**:
1. Fetch PR #42 details and diff
2. Summarize changed files and key modifications
3. Present review summary

## Constraints

- Requires valid GitHub token with appropriate scopes
- API rate limit: 5,000 requests per hour (authenticated)
- File content limited to 1MB per file via API
- Branch names must follow Git naming conventions
- PR descriptions have a 65,536 character limit

## Platform-Specific Notes

- **Open WebUI**: Configure via `Settings > Integrations > GitHub`
- **MCP**: Use `github-mcp-server` adapter
- **OpenAI**: Set `GITHUB_TOKEN` environment variable
- **Claude**: Set `GITHUB_TOKEN` environment variable