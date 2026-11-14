---
id: "design-patterns"
type: "concept"
title: "Design Patterns"
aliases: ["GoF", "Gang of Four"]
domains: ["design"]
branch: "design"
---

# Design Patterns

## What it is and why it matters

A design pattern names a recurring design problem, the forces involved, and a reusable arrangement of responsibilities. Pattern names help discussion when the participants also understand the tradeoffs.

## Mechanism

The Gang of Four catalog groups 23 object-oriented patterns into creational, structural, and behavioral families. A pattern is not a library call or a required class diagram. A language feature such as a closure or algebraic data type can express the same intent with a different implementation.

## Worked example

A checkout service can accept a pricing function. Swapping a discount policy without rewriting checkout expresses Strategy. In a language with first-class functions, a callable may be enough; a hierarchy of strategy classes is optional.

## Engineering implications

Describe the problem before selecting a pattern. Compare the simplest direct implementation and explain what variation the pattern isolates. Singleton can hide global state and complicate tests. Patterns do not replace architectural decisions about data ownership, reliability, and deployment.

## Graph connections

- **requires:** [Programming Paradigms](programming-paradigms.md)
- **contains:** [Creational Design Patterns](creational-patterns.md), [Structural Design Patterns](structural-patterns.md), [Behavioral Design Patterns](behavioral-patterns.md)
- **related_to:** [Software Design Principles](software-design.md), [Software Architecture](architecture.md)
- **supported_by:** [Design Patterns Elements of Reusable Object-Oriented Software](../references/design-patterns-book.md)
