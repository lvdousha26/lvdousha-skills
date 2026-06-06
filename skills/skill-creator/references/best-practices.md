# Skill Creation Best Practices

## Description Guidelines

The `description` field is the most critical part of your skill - it determines when Claude activates it.

### Good Descriptions
- "Review code for OWASP Top 10 security vulnerabilities in Python/Flask applications"
- "Generate commit messages following Conventional Commits specification"
- "Design REST API endpoints following OpenAPI 3.0 standards"

### Bad Descriptions
- "Help with code" (too vague)
- "Security review" (doesn't specify scope)
- "API design" (doesn't specify standards)

## Content Organization

### SKILL.md (Keep under 500 lines)
- Core instructions and workflows
- Step-by-step procedures
- Quick start guide
- What to do, not why

### references/ (Background knowledge)
- Domain explanations
- "Why" certain patterns exist
- Historical context
- Deep technical details

### assets/ (Reusable content)
- Code templates
- Config file examples
- Boilerplate text
- Schema definitions

### scripts/ (Executable tools)
- Python scripts for validation
- Bash scripts for automation
- Tools that Claude can execute

## Triggering Behavior

Claude uses LLM-based matching, not keywords. Your description should:
- Be specific about the task
- Mention the domain/context
- Indicate the output format
- Reference any standards or frameworks

## Tool Restrictions

Use `allowed-tools` to constrain skills:

```yaml
---
name: read-only-skill
description: Analyze code without making changes
allowed-tools:
  - Read
  - Grep
  - Glob
---
```

## Testing Your Skill

1. **Create the skill**
2. **Test immediately**: Try using it with a real prompt
3. **Refine**: Adjust based on what worked/didn't work
4. **Iterate**: Skills are living documents

## Common Patterns by Skill Type

### Code Generation Skills
- Include output format templates
- Specify language/framework conventions
- Provide validation checklist

### Analysis Skills
- Define analysis criteria
- Include reporting format
- Specify what to look for

### Automation Skills
- List execution steps clearly
- Include error handling
- Specify success criteria

### Documentation Skills
- Define documentation structure
- Include style guidelines
- Provide example outputs
