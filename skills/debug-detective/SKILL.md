---
name: debug-detective
description: Systematically debugs issues by analyzing error messages, stack traces, and code flow. Forms hypotheses, isolates root causes via binary search through the call stack, and proposes verified fixes — not scatter-shot console.log statements.
---

# Debug Detective

Solve bugs like a detective — systematically gather evidence, form hypotheses, and methodically eliminate possibilities until the root cause is found.

## Investigation Protocol

When a bug is reported, follow these steps IN ORDER:

### Phase 1: Crime Scene Analysis
1. Get the exact error message and full stack trace
2. Find the minimal input that triggers the bug
3. Confirm: "I can reproduce this with: [steps]"

### Phase 2: Hypothesize
- List 3 possible causes, ranked by likelihood
- For each: what evidence would confirm or rule it out?

### Phase 3: Isolate (Binary Search)
- Check git blame on the failing line — when and why was it introduced?
- Find the last known-good state (commit/tag where this worked)
- Narrow the scope: is the bug in input, logic, or output?
- Add strategic logging only at decision points, not scatter-shot

### Phase 4: Root Cause Analysis
- Identify the exact line and condition that causes the failure
- Explain the chain of events: input → processing → failure
- Document WHY the current code is wrong

### Phase 5: The Fix
- Propose a minimal fix targeting the root cause
- Verify the fix against the original reproduction case
- Check for similar patterns elsewhere in the codebase

## Common Bug Patterns

- Null/undefined access — missing guards, async timing
- Type mismatches — implicit coercion, API contract changes
- Race conditions — missing await, shared mutable state
- State corruption — stale closures, incorrect dependency arrays
- Missing error handling — uncaught promises, swallowed exceptions

## Output Format

```
ROOT CAUSE: [one-line summary]

CHAIN OF EVENTS:
1. [step] → 2. [step] → 3. [failure]

FIX: [specific code change]

VERIFICATION: [how to confirm the fix works]

PREVENTION: [how to avoid this class of bug in the future]
```

Never propose a fix before completing the investigation. Evidence first, code second.
