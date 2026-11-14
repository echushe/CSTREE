---
id: "ai-assisted-development"
type: "concept"
title: "AI Assisted Software Development"
aliases: ["AI coding", "AI pair programming"]
domains: ["ai-development"]
branch: "ai-development"
---

# AI Assisted Software Development

## What it is and why it matters

AI assistance can generate, explain, transform, and review code. Its engineering value depends on whether the resulting change satisfies the intended behavior and remains maintainable.

## Mechanism

Use a loop of intent → relevant context → proposed change → inspection → independent execution checks. Supply concrete acceptance examples, repository conventions, and constraints. Evaluate the whole workflow, including waiting, review, correction, and later maintenance, rather than counting generated lines.

## Worked example

For a date parser, specify supported formats and invalid cases before generation. A check for `2024-02-29` should succeed; `2023-02-29` should fail. Tests derived from the specification are stronger evidence than tests that merely repeat the generated implementation's assumptions.

## Engineering implications

Read changed code and verify dependencies and APIs against current documentation. Keep tasks small enough to inspect. Benchmark productivity in the relevant setting: METR's early-2025 result and its 2026 methodology update do not establish one universal speedup or slowdown. Retain ordinary testing, review, and ownership.

## Graph connections

- **requires:** [Programming Languages](programming-languages.md), [Software Testing](testing.md), [Requirements and Specifications](requirements-and-specifications.md)
- **contains:** [Vibe Programming and Vibe Coding](vibe-programming.md), [Agentic Software Development](agentic-development.md)
- **related_to:** [Version Control and Git](version-control.md), [Security Engineering](security-engineering.md)
- **supported_by:** [AI Development Experience and Productivity Evidence](../references/ai-development-evidence.md)
