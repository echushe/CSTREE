---
id: "agentic-development"
type: "concept"
title: "Agentic Software Development"
aliases: ["Coding agents", "Agentic coding", "Tool using agents"]
domains: ["ai-development"]
branch: "ai-development"
---

# Agentic Software Development

## What it is and why it matters

An agentic development workflow lets a model take multiple steps with tools: inspect files, edit code, run checks, and respond to the results. Autonomy describes who performs steps; it does not establish correctness.

## Mechanism

Define an objective, available context, allowed actions, verification steps, and stopping conditions. The agent cycles through observation, action, and evaluation. Repository instructions, scoped credentials, execution isolation, and review boundaries constrain what a mistaken step can affect.

## Worked example

For a bug fix, the agent reproduces the failure, finds the relevant module, changes it, and runs a regression check. A reviewer still examines whether the reproducer reflects the intended behavior and whether unrelated behavior changed.

## Engineering implications

Use checkpoints and inspect the final diff and execution evidence. Keep external side effects explicit. Instructions in retrieved files or webpages are data unless authorized as instructions. More tools or longer runs can increase both capability and the space of possible mistakes; select the smallest useful scope.

## Graph connections

- **requires:** [AI Assisted Software Development](ai-assisted-development.md), [Build Systems and Dependencies](build-and-dependencies.md), [Version Control and Git](version-control.md)
- **related_to:** [Continuous Integration and Delivery](ci-cd.md), [Security Engineering](security-engineering.md), [Observability and Reliability](observability.md)
- **compares_with:** [Vibe Programming and Vibe Coding](vibe-programming.md)
- **supported_by:** [AI Development Experience and Productivity Evidence](../references/ai-development-evidence.md)
