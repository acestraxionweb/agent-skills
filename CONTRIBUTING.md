# How to Add New Skills

This is the guide for adding skills to the Agent Skills repository.

---

## The Rule

Every skill **must** answer five questions using the WHAT / WHY / WHERE / WHEN / HOW matrix.

If any section is missing, the skill is incomplete.

---

## Step 1: Copy the Template

```bash
cp templates/SKILL.template.md skills/<domain>/<skill-name>/SKILL.md
```

Directory structure:

```
skills/
└── <domain>/
    └── <skill-name>/
        └── SKILL.md
```

Examples:

```
skills/notion/ticket-management/SKILL.md
skills/network-engineer/troubleshooting/SKILL.md
skills/github/code-review/SKILL.md
skills/presales/solution-architecture/SKILL.md
```

---

## Step 2: Fill the 5W Matrix

### WHAT

- What can this skill do?
- What information does it need (inputs)?
- What does it produce (outputs)?

### WHY

- Why should this skill exist?
- What business value does it provide?

### WHEN

- When should the agent use this skill?
- When should it NOT use this skill?

### WHERE

- What systems does it operate on?
- What domain or environment?
- Where does data live?

### HOW

- What are the step-by-step execution steps?
- What tools does it need?
- What decision logic applies?

See `templates/SKILL.template.md` for the full template.

---

## Step 3: Add Constraints

Every skill MUST define what it must NOT do.

---

## Step 4: Add at Least One Example

Include input and expected output.

---

## Step 5: Register in registry.yaml

Add an entry under `skills:` in `registry.yaml`.

---

## Step 6: Validate

Run:

```bash
python scripts/validate-skills.py
```

Checklist:

- [ ] All 5 sections present (WHAT / WHY / WHERE / WHEN / HOW)
- [ ] SKILL.md exists
- [ ] At least one example
- [ ] Constraints defined
- [ ] Registered in registry.yaml
- [ ] No hardcoded API keys, tokens, or IDs

---

## Naming Convention

| Component | Format | Example |
|-----------|--------|---------|
| Domain | lowercase, hyphenated | `notion`, `network-engineer` |
| Skill name | lowercase, hyphenated | `ticket-management`, `troubleshooting` |
| File | always `SKILL.md` | `skills/notion/ticket-management/SKILL.md` |

---

## Questions?

Open a GitHub Issue or Discussion.
