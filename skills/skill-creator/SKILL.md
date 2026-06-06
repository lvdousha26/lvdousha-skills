---
name: skill-creator
description: Help users create new Claude Code skills with proper structure, frontmatter, and best practices. Use when user wants to build a custom skill.
---

# Skill Creator

## Overview
This skill helps you create new Claude Code skills from scratch. It guides you through the entire process: planning the skill's purpose, setting up the directory structure, writing the SKILL.md file with proper frontmatter, and following best practices.

## When to Use
- User asks to create a new skill
- User wants to build a custom slash command
- User mentions "skill", "skill template", or "skill generator"
- User wants to automate repetitive workflows

## Skill Creation Process

### Step 1: Gather Requirements
Ask the user the following questions:

1. **Purpose**: What should this skill do? What problem does it solve?
2. **Triggers**: When should Claude activate this skill? (e.g., "security review", "commit message", "API design")
3. **Target tasks**: What specific actions will the skill perform?
4. **Resources needed**: Scripts, templates, reference docs?

### Step 2: Design the Skill Structure

A skill has this minimal structure:
```
skill-name/
├── SKILL.md (required)
├── scripts/ (optional)
├── references/ (optional)
└── assets/ (optional)
```

### Step 3: Create the SKILL.md Template

Every SKILL.md must have:

**YAML Frontmatter (Required)**:
```yaml
---
name: skill_name_with_underscores
description: One clear sentence describing when to use this skill.
optional_field: value
---
```

**Content Sections**:
- Overview: What does this skill do?
- When to Use: When should Claude activate it?
- Instructions: Step-by-step guidance
- Examples: Good/bad examples (optional but recommended)

### Step 4: Generate Initial Files

Create the skill directory and SKILL.md with:
- A clear, specific description (crucial for triggering)
- Well-structured instructions
- Optional template files

### Step 5: Best Practices Checklist

Before finalizing, ensure:

- [ ] **Description is specific**: "Security review for Node.js apps" vs "Help with security"
- [ ] **SKILL.md under 500 lines**: Split long content into references/
- [ ] **Include examples**: Show Claude expected outputs
- [ ] **Define tool restrictions**: Use `allowed-tools` if needed
- [ ] **Test with real prompts**: Try using the skill immediately

## Skill Installation Locations

| Location | Scope | Command |
|----------|-------|---------|
| `~/.claude/skills/` | Global (all projects) | `mkdir -p ~/.claude/skills/skill-name` |
| `.claude/skills/` | Project only | `mkdir -p .claude/skills/skill-name` |

## Example: Creating a Code Review Skill

**User Input**: "I want a skill to review my code for security issues"

**Your Response**:
1. Ask: What languages/frameworks? Any specific security standards?
2. Create directory: `~/.claude/skills/code-reviewer/`
3. Generate SKILL.md with:
   - `name: code-reviewer`
   - `description: Review code for security vulnerabilities, performance issues, and best practice violations in [specific languages]`
   - Security checklist steps
   - Common vulnerability patterns
4. Test with: "Review this code for security issues"

## Frontmatter Field Reference

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Skill identifier (underscores, no spaces) |
| `description` | Yes | When to use this skill (critical for triggering) |
| `allowed-tools` | No | Restrict which tools the skill can use |
| `max-tokens` | No | Token budget for this skill |
| `examples` | No | Example prompts that should trigger |

## Common Pitfalls

**Don't**:
- Use vague descriptions like "Helps with code"
- Put everything in SKILL.md (use references/ for large content)
- Skip testing the skill
- Make skills too broad (one purpose per skill)

**Do**:
- Write specific, actionable descriptions
- Separate knowledge (references/) from instructions (SKILL.md)
- Test immediately after creation
- Keep skills focused on a single use case

## Quick Template for Users

If user wants a template, provide this:

```markdown
---
name: my_skill_name
description: What this skill does and when to trigger it.
---

# My Skill Name

## Overview
Brief description of what this skill accomplishes.

## When to Use
Trigger conditions for when Claude should activate this skill.

## Instructions
1. First step
2. Second step
3. Third step

## Examples
### Good Example
Expected output format

### Bad Example
What to avoid
```

## Troubleshooting

**Skill not triggering?**
- Check description is specific enough
- Verify skill is in correct directory
- Restart Claude Code session

**Skill too long?**
- Move background info to `references/`
- Move code templates to `assets/`
- Keep SKILL.md under 500 lines
