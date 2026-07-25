# Open WebUI Platform Adapter

## Overview

This adapter enables **Agent Skills** to work within [Open WebUI](https://github.com/open-webui/open-webui), a self-hosted AI interface.

## Setup

### 1. Install Open WebUI

```bash
docker run -d -p 3000:8080 \
  -e OPENAI_API_BASE_URL=https://api.openai.com/v1 \
  -e OPENAI_API_KEY=your-key \
  --name open-webui \
  ghcr.io/open-webui/open-webui:main
```

### 2. Configure Skills

1. Go to **Admin Panel** → **Settings** → **Integrations**
2. Enable the skills you want to use
3. Configure API keys for each integration

### 3. Using Skills

Skills are available in any chat session. Simply describe what you want to do:

```
User: "Search my Notion for meeting notes from last week"
Agent: [Activates notion skill and retrieves results]
```

## Skill Registration

To register skills with Open WebUI:

1. Place skill YAML in the configured skills directory
2. Skills are auto-discovered on restart
3. Enable/disable via the Admin Panel

## Configuration

```yaml
# openwebui-config.yaml
skills:
  enabled:
    - notion
    - github
    - memory
    - agent-builder
  settings:
    notion:
      api_key: "${NOTION_API_KEY}"
    github:
      token: "${GITHUB_TOKEN}"
```

## Limitations

- Skills run within Open WebUI's execution sandbox
- External API calls require network access
- File operations limited to configured directories
- Memory persistence requires database configuration