# Contributing to Agent Skills

Thank you for your interest in contributing! This guide will help you add new skills or improve existing ones.

## 🎯 Design Principles

1. **Portability**: Skills must work across multiple agent platforms
2. **No Hardcoding**: No database IDs, API keys, or environment-specific values
3. **Self-Contained**: Each skill directory should contain everything needed
4. **Machine-Readable**: All skills must be registered in `registry.yaml`

## 📝 Adding a New Skill

### Step 1: Create the Skill Directory

```bash
mkdir -p skills/your-skill-name/examples
touch skills/your-skill-name/SKILL.md
touch skills/your-skill-name/README.md
```

### Step 2: Write the SKILL.md

Use the template at [`templates/SKILL.template.md`](./templates/SKILL.template.md):

```bash
cp templates/SKILL.template.md skills/your-skill-name/SKILL.md
```

The `SKILL.md` is the **canonical source of truth** for the skill. It must include:

- **Name** and **description**
- **Trigger patterns** (when should the agent use this skill?)
- **Input/Output format**
- **Step-by-step instructions** for the agent
- **Examples** with expected behavior

### Step 3: Register in registry.yaml

Add your skill to [`registry.yaml`](./registry.yaml):

```yaml
skills:
  - name: your-skill-name
    description: "Short description of what this skill does"
    author: your-username
    version: 0.1.0
    tags: [category1, category2]
    platforms: [openwebui, mcp, openai, claude]
    skill_path: skills/your-skill-name/SKILL.md
```

### Step 4: Write a README.md

Add a human-readable README in your skill directory:

```markdown
# Your Skill Name

Brief description of the skill.

## What it does
...

## How to use
...
```

### Step 5: Add Examples (Optional)

Create example files in the `examples/` subdirectory:

```bash
touch skills/your-skill-name/examples/example-1.md
touch skills/your-skill-name/examples/example-2.md
```

## 📐 SKILL.md Format

Every SKILL.md should follow this structure:

```markdown
# Skill: [Name]

## Metadata
- **Name**: [skill-name]
- **Version**: [semver]
- **Author**: [your name/handle]
- **Tags**: [tag1, tag2]
- **Platforms**: [openwebui, mcp, openai, claude]

## Description
[What this skill does in 1-2 sentences]

## Trigger Patterns
[When should the agent activate this skill?]

## Instructions
[Step-by-step instructions for the agent]

## Input Format
[What does the agent need to receive?]

## Output Format
[What does the agent produce?]

## Examples
[Concrete examples with input/output]

## Constraints
[Any limitations or requirements]
```

## ✅ Quality Checklist

Before submitting a PR, ensure:

- [ ] `SKILL.md` follows the format above
- [ ] Skill is registered in `registry.yaml`
- [ ] No hardcoded IDs, API keys, or environment-specific values
- [ ] README.md is included and descriptive
- [ ] Examples are provided (recommended)
- [ ] Skill is platform-agnostic (or platform adapters are added)
- [ ] Markdown renders correctly

## 🔄 Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b skill/your-skill-name`
3. Add your skill following the steps above
4. Test that the skill description is clear and complete
5. Submit a pull request with:
   - A clear title: `feat: add [skill-name] skill`
   - A description of what the skill does
   - Which platforms it supports

## 🐛 Reporting Issues

- Use GitHub Issues for bugs or suggestions
- Include the skill name and version if applicable
- Provide clear steps to reproduce

## 📬 Questions?

Open a Discussion in the GitHub Discussions tab.

---

Thank you for making agents smarter! 🧠