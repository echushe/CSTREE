---
id: "software-design"
type: "concept"
title: "Software Design Principles"
aliases: ["SOLID", "Encapsulation", "Cohesion", "Coupling", "Dependency inversion"]
domains: ["design"]
branch: "design"
---

# Software Design Principles

## What it is and why it matters

Software design chooses boundaries that make behavior understandable and change manageable. Good boundaries hide decisions likely to vary and keep related rules together.

## Mechanism

Cohesion measures how closely a module's responsibilities fit; coupling describes dependencies among modules. Encapsulation protects invariants behind operations. Dependency inversion lets policy depend on an abstraction instead of a particular infrastructure implementation. SOLID is a set of design heuristics, not a mechanical score.

## Worked example

An invoice calculator taking prices and tax rules can be a pure function. An application service loads data and calls it. Keeping SQL and email delivery outside the calculation lets the same rules run in tests, an HTTP endpoint, or a batch job.

## Engineering implications

Choose abstractions around concrete variation or protected invariants. Excessive interfaces and layers add navigation cost without guaranteeing flexibility. Refactor when a repeated change reveals a missing boundary. Document why a boundary exists and what dependencies may cross it.

## Graph connections

- **requires:** [Programming Paradigms](programming-paradigms.md)
- **contains:** [Design Patterns](design-patterns.md), [Software Architecture](architecture.md), [API Design and Contracts](api-design.md)
- **related_to:** [Software Testing](testing.md), [Requirements and Specifications](requirements-and-specifications.md)
- **supported_by:** [Design Patterns Elements of Reusable Object-Oriented Software](../references/design-patterns-book.md), [Software Engineering and Git Guides](../references/software-construction.md)
