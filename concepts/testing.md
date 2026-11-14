---
id: "testing"
type: "concept"
title: "Software Testing"
aliases: ["Unit tests", "Integration tests", "Property-based testing", "Test oracle"]
domains: ["engineering"]
branch: "engineering"
---

# Software Testing

## What it is and why it matters

Testing runs an implementation against chosen expectations. A useful test detects a meaningful failure and gives enough information to diagnose it.

## Mechanism

Unit tests isolate a behavior; integration tests exercise boundaries; end-to-end tests cover a complete route. Property-based tests generate cases for an invariant. Differential tests compare independent implementations. An oracle determines the expected result. Coverage describes exercised code, not proof that all requirements are correct.

## Worked example

For a sorting function, check ordered output and preservation of the input multiset, including duplicates. Checking only order would allow an implementation that always returns an empty list. Add a case for stability only when stability is part of the contract.

## Engineering implications

Choose cases from requirements, boundaries, and past failures. Control clocks, randomness, and external dependencies where needed. Avoid overmocking implementation details or writing assertions that merely mirror the code. Concurrency, recovery, and performance need checks suited to their failure modes.

## Graph connections

- **requires:** [Requirements and Specifications](requirements-and-specifications.md), [Programming Languages](programming-languages.md)
- **related_to:** [Debugging and Profiling](debugging-and-profiling.md), [Continuous Integration and Delivery](ci-cd.md), [Formal Methods and Verification](formal-methods.md), [AI Assisted Software Development](ai-assisted-development.md)
- **supported_by:** [Software Engineering and Git Guides](../references/software-construction.md)
