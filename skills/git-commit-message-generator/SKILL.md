---
name: git-commit-message-generator
description: Automatically generates meaningful, conventional commit messages by analyzing staged changes. Follows the Conventional Commits specification with type prefixes like feat, fix, docs, refactor, etc.
---

# Git Commit Message Generator

Generate commit messages following the Conventional Commits specification.

## Format

```
<type>(<scope>): <subject>

<body>
```

## Types

- **feat**: new feature
- **fix**: bug fix
- **refactor**: code change that neither fixes a bug nor adds a feature
- **docs**: documentation only
- **test**: adding or correcting tests
- **chore**: build process, dependencies, CI
- **perf**: performance improvement
- **style**: formatting, semicolons, etc (not CSS)

## Rules

- Subject line: imperative mood, lowercase, no period, max 72 chars
- Body: explain WHY not WHAT (the diff shows what)
- If multiple logical changes, suggest splitting into separate commits
- Scope is optional but encouraged (e.g., feat(auth): add OAuth2 flow)
- For breaking changes: add `!` after type/scope (e.g., feat!: remove v1 API)

## Workflow

When asked to commit changes:
1. Run `git diff --staged` to analyze staged changes
2. Generate a commit message following the format above
3. Include bullet points for detailed changes in the body
4. Ask for confirmation before committing

When given a diff or description of changes, output ONLY the commit message. No explanation needed.
