# Quick Start: Creating Your First Skill

## Method 1: Let Claude Help You

Just say something like:
> "Help me create a skill for [your task]"

Claude will guide you through the process and create the skill for you.

## Method 2: Manual Creation

### 1. Create Directory
```bash
# Global skill (all projects)
mkdir -p ~/.claude/skills/your-skill-name

# Project skill (this project only)
mkdir -p .claude/skills/your-skill-name
```

### 2. Create SKILL.md
Copy the template from `templates/skill-template.md` and customize it.

### 3. Use Your Skill
Restart Claude Code, then type:
> `/your-skill-name`

## Example Skills You Can Create

- `commit-message` - Generate conventional commits
- `code-review` - Review code for issues
- `api-design` - Design REST APIs
- `test-generator` - Generate unit tests
- `docs-generator` - Create documentation

## Need Help?
Just ask: "Create a skill for [your purpose]"
