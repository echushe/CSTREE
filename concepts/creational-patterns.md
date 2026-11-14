---
id: "creational-patterns"
type: "concept"
title: "Creational Design Patterns"
aliases: ["Factory Method", "Abstract Factory", "Builder", "Prototype", "Singleton"]
domains: ["design"]
branch: "design"
---

# Creational Design Patterns

## What it is and why it matters

Creational patterns control object construction so callers do not need every detail of concrete initialization.

## Mechanism

- Factory Method delegates construction through an overridable operation.
- Abstract Factory creates compatible families of objects.
- Builder separates staged construction from the resulting representation.
- Prototype creates from an existing instance under a defined copying policy.
- Singleton restricts an instance and supplies an access point, often introducing global state.

## Worked example

A report builder collects a title, sections, and output settings, then validates required fields at `build()`. An abstract factory could instead supply a matching renderer and font metrics for each output backend. These solve different construction problems.

## Engineering implications

Use ordinary constructors when creation is simple. Make partial states and validation explicit in a builder. Prototype requires a deliberate shallow or deep copy policy. Prefer explicit lifetime and dependency management over using Singleton merely for convenient access.

## Graph connections

- **requires:** [Design Patterns](design-patterns.md)
- **related_to:** [Memory Management and Ownership](memory-management.md), [Software Testing](testing.md)
- **supported_by:** [Design Patterns Elements of Reusable Object-Oriented Software](../references/design-patterns-book.md)
