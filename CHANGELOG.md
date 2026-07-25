# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial repository structure
- README with project overview and quick start guide
- CONTRIBUTING guide for skill authors
- `registry.yaml` — machine-readable skill inventory
- Skill: `notion` — Notion integration for reading/writing pages and databases
- Skill: `github` — GitHub operations (repos, issues, PRs, code management)
- Skill: `memory` — Agent memory management (short-term, long-term, retrieval)
- Skill: `agent-builder` — Dynamic agent construction and orchestration
- Platform adapter: Open WebUI
- Platform adapter: MCP (Model Context Protocol)
- Platform adapter: OpenAI Agents
- Platform adapter: Claude
- Skill template (`templates/SKILL.template.md`)
- Agent template (`templates/agent.template.yaml`)

## [0.1.0] — 2026-07-25

### Added
- Repository initialized
- Core skill framework established
- Four foundational skills: notion, github, memory, agent-builder
- Four platform adapters: openwebui, mcp, openai, claude

[Unreleased]: https://github.com/acestraxionweb/agent-skills/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/acestraxionweb/agent-skills/releases/tag/v0.1.0