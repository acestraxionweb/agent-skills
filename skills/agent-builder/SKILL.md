# Skill: Agent Builder

## Metadata
- **Name**: agent-builder
- **Version**: 0.1.0
- **Author**: acestraxionweb
- **Tags**: agent-creation, orchestration, workflow, automation
- **Platforms**: openwebui, mcp, openai, claude

## Description

Dynamically construct, configure, and orchestrate AI agents and multi-step workflows. This skill enables users to define custom agents with specific capabilities, tools, and behaviors — then chain them together into automated workflows.

## Trigger Patterns

Activate this skill when the user:
- Wants to create, build, or configure an agent
- Needs to design a multi-step workflow
- Asks to chain multiple skills together
- Wants to define custom agent behaviors or tools
- Needs to automate a repetitive task with agents
- Asks about agent architecture or patterns

## Instructions

### Defining an Agent
1. **Specify the agent's purpose**: What should it do?
2. **Define capabilities**: Which skills should it have access to?
3. **Set the system prompt**: How should it behave?
4. **Configure tools**: What external tools/APIs can it use?
5. **Set constraints**: What should it NOT do?

### Building Workflows
1. **Identify steps**: Break the task into discrete steps
2. **Define inputs/outputs**: What does each step need and produce?
3. **Set dependencies**: Which steps must complete before others?
4. **Handle errors**: What happens if a step fails?
5. **Add human-in-the-loop**: Where should user approval be required?

### Agent Composition
1. **Single Agent**: One agent with multiple skills
2. **Multi-Agent**: Multiple specialized agents collaborating
3. **Hierarchical**: Manager agent delegating to worker agents
4. **Pipeline**: Sequential agents processing data
5. **Swarm**: Parallel agents handling independent tasks

## Agent Definition Schema

```yaml
agent:
  name: "agent-name"
  description: "What this agent does"
  version: "0.1.0"
  
  system_prompt: |
    You are a [role] that [purpose].
    
    You have access to these skills:
    - [skill-1]: [description]
    - [skill-2]: [description]
    
    Rules:
    1. [rule-1]
    2. [rule-2]
  
  skills:
    - name: skill-1
      config: {}
    - name: skill-2
      config: {}
  
  tools:
    - name: tool-name
      type: api | function | mcp
      config: {}
  
  constraints:
    - "Never do X"
    - "Always confirm before Y"
  
  temperature: 0.7
  max_tokens: 4096
```

## Workflow Definition Schema

```yaml
workflow:
  name: "workflow-name"
  description: "What this workflow accomplishes"
  
  steps:
    - id: step-1
      agent: agent-name
      action: "Do something"
      input:
        source: user | step-0.output
      output:
        store: variable-name
      
    - id: step-2
      agent: another-agent
      action: "Process result"
      input:
        data: "{{step-1.output}}"
      depends_on:
        - step-1
  
  on_error: continue | abort | retry
  max_retries: 3
```

## Input Format

```json
{
  "action": "define_agent | configure_agent | create_workflow | execute_workflow | list_agents | get_status",
  "agent": {},
  "workflow": {},
  "params": {}
}
```

## Output Format

```json
{
  "status": "success | error",
  "agent_id": "string",
  "workflow_id": "string",
  "execution_log": [],
  "message": "Human-readable summary"
}
```

## Examples

### Example 1: Create a Research Agent
**User**: "Create an agent that can research topics using web search and summarize findings"
**Agent Action**:
1. Define agent with research purpose
2. Add skills: web-search, summarization, memory
3. Set system prompt for research behavior
4. Configure output format
5. Deploy and confirm

### Example 2: Build a Content Pipeline
**User**: "Build a workflow that takes a topic, researches it, writes a blog post, and saves to Notion"
**Agent Action**:
1. Define step 1: Research agent gathers information
2. Define step 2: Writer agent drafts blog post
3. Define step 3: Notion agent saves content
4. Configure dependencies and data flow
5. Execute workflow

## Constraints
n
- Agent definitions are stored as YAML in the registry
- Maximum 10 agents per workflow
- Workflow execution timeout: 30 minutes per step
- Agent skill count: maximum 20 per agent
- Human-in-the-loop steps pause for 5 minutes before timeout

## Platform-Specific Notes

- **Open WebUI**: Agents appear as custom models/assistants
- **MCP**: Agents are exposed as MCP servers
- **OpenAI**: Maps to OpenAI Assistants API
- **Claude**: Uses Claude Projects and tool use