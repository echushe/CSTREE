---
id: "vibe-programming"
type: "concept"
title: "Vibe Programming and Vibe Coding"
aliases: ["Vibe coding", "Vibe programming"]
domains: ["ai-development"]
branch: "ai-development"
---

# Vibe Programming and Vibe Coding

## What it is and why it matters

Vibe programming, often called vibe coding, uses conversational feedback to steer AI-generated software. Here it denotes a workflow where acceptance is driven mainly by observed behavior and the author may not understand every generated change. The term is informal and usage varies.

## Mechanism

Describe a desired result, run a generated version, inspect what happens, and request another iteration. This makes the feedback loop accessible, but a convincing demo covers only the paths exercised. Karpathy's 2025 MenuGen account is a firsthand example of the gap between a quick prototype and operating a real application.

## Worked example

A generated to-do app appears to save an item. Refreshing reveals that the data was only in memory. Checking persistence, two simultaneous users, invalid input, and authorization exposes requirements absent from the initial visual feedback.

## Engineering implications

Treat observed success as a starting point for verification. Before depending on the result, inspect data handling, failures, dependencies, and deployment settings, and add checks from explicit requirements. AI assistance with understood and reviewed code fits the broader AI development workflow even when someone casually calls it vibe coding.

## Graph connections

- **requires:** [AI Assisted Software Development](ai-assisted-development.md)
- **compares_with:** [Agentic Software Development](agentic-development.md)
- **related_to:** [Debugging and Profiling](debugging-and-profiling.md), [API Design and Contracts](api-design.md)
- **supported_by:** [AI Development Experience and Productivity Evidence](../references/ai-development-evidence.md)
