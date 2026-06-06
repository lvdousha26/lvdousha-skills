---
name: unit-test-generator
description: Generates comprehensive unit tests for functions and classes. Covers happy paths, edge cases, error conditions, and boundary values. Supports Jest, Pytest, JUnit, and other frameworks.
---

# Unit Test Generator

Generate comprehensive unit tests for functions and classes.

## Process

When generating tests:
1. Identify all code paths in the function/class
2. Create tests for normal inputs (happy path)
3. Test edge cases (empty, null, zero, negative)
4. Test boundary values (min, max, limits)
5. Test error conditions and exceptions
6. Mock external dependencies
7. Use descriptive test names

## Test Structure

```
describe("[function/module name]", () => {
  it("should [expected behavior] when [scenario]", () => {
    // Arrange — set up test data
    // Act — call the function
    // Assert — verify the result
  });
});
```

## Coverage Targets

- Happy path: primary use case works correctly
- Edge cases: empty/null/undefined inputs, extreme values
- Error paths: exceptions thrown, error responses returned
- Boundaries: min/max values, array limits, string lengths
- State: side effects, mutations, state transitions

## Naming Convention

`test_[function]_[scenario]_[expected_result]` (Pytest)
`it("should [behavior] when [condition]")` (Jest/Jasmine)
`test[Scenario]_Should[Expected]` (C# xUnit)

Auto-detect the testing framework from the project structure. Match existing test patterns and conventions.
