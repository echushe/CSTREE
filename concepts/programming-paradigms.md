---
id: "programming-paradigms"
type: "concept"
title: "Programming Paradigms"
aliases: ["OOP", "Functional programming", "Imperative programming", "Declarative programming"]
domains: ["languages"]
branch: "languages"
---

# Programming Paradigms

## What it is and why it matters

Paradigms organize the way a program expresses behavior. Imperative, object-oriented, functional, and declarative styles can coexist within one language or application.

## Mechanism

Imperative code updates state step by step. Object-oriented code groups state and behavior behind interfaces. Functional techniques emphasize function composition and controlled effects. Declarative code states a desired result while an engine chooses execution. These are design tools rather than exclusive categories.

## Worked example

To total paid invoices, an imperative loop updates an accumulator; a functional pipeline filters then folds; SQL expresses `SUM(amount)` with a predicate. Each can compute the same result while exposing different execution and mutation choices.

## Engineering implications

Use pure functions for calculations and explicit boundaries for I/O when that makes behavior easier to test. Objects can protect invariants, while simple functions may need less machinery. Avoid treating inheritance, immutability, or a pattern catalog as mandatory for every problem.

## Graph connections

- **requires:** [Programming Languages](programming-languages.md)
- **related_to:** [Software Design Principles](software-design.md), [Design Patterns](design-patterns.md), [The Relational Model and SQL](relational-model-and-sql.md)
- **supported_by:** [Language Specifications and Official Guides](../references/language-specifications.md), [Design Patterns Elements of Reusable Object-Oriented Software](../references/design-patterns-book.md)
