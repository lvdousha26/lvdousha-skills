---
name: code-review-assistant
description: Performs thorough code reviews checking for bugs, security issues, performance problems, and style inconsistencies. Provides actionable feedback with specific line references.
---

# Code Review Assistant

Perform thorough code reviews with actionable feedback.

## Review Checklist

When reviewing code, check for:

1. **Logic errors and edge cases** — null/undefined access, off-by-one, race conditions, incorrect assumptions
2. **Security vulnerabilities** — SQL injection, XSS, CSRF, hardcoded secrets, insecure dependencies, missing input validation
3. **Performance bottlenecks** — N+1 queries, unnecessary allocations, blocking operations, missing memoization
4. **Code style and readability** — naming clarity, function length, nesting depth, dead code
5. **Missing error handling** — try/catch gaps, unhandled promise rejections, missing error boundaries
6. **Test coverage gaps** — untested edge cases, missing integration tests, brittle assertions

## Output Format

```
[SEVERITY] file:line — Issue description
Suggestion: How to fix it
```

Severity levels:
- **[CRITICAL]** — Security vulnerability, data loss risk, production outage
- **[HIGH]** — Bug that affects correctness, broken feature
- **[MEDIUM]** — Performance issue, maintainability problem
- **[LOW]** — Style nit, minor improvement

## Process

1. Read all changed files thoroughly
2. Understand the intent of the changes
3. Report issues grouped by severity (critical first)
4. For each issue, explain WHY it's a problem and HOW to fix it
5. End with a summary: total issues found, overall assessment
