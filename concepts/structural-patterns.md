---
id: "structural-patterns"
type: "concept"
title: "Structural Design Patterns"
aliases: ["Adapter", "Bridge", "Composite", "Decorator", "Facade", "Flyweight", "Proxy"]
domains: ["design"]
branch: "design"
---

# Structural Design Patterns

## What it is and why it matters

Structural patterns organize objects and interfaces so components can cooperate without every client depending on their internal representation.

## Mechanism

- Adapter translates an interface; Bridge separates independently varying abstraction and implementation.
- Composite treats leaves and groups uniformly.
- Decorator adds behavior around an object using a compatible interface.
- Facade exposes a simpler entry point to a subsystem.
- Flyweight shares suitable intrinsic state.
- Proxy controls access to another object.

## Worked example

A storage adapter translates `save(bytes)` into a vendor SDK call. A logging decorator wraps the same storage interface and records duration. A facade might offer one `publish_report()` operation that coordinates rendering and storage.

## Engineering implications

Wrapping can obscure error handling and make call chains difficult to trace. Remote proxies cannot make network failure behave exactly like a local call. Shared flyweight state should not accidentally include per-client mutable state. Keep wrappers transparent about ownership and failure semantics.

## Graph connections

- **requires:** [Design Patterns](design-patterns.md)
- **uses:** [Trees and Search Trees](trees.md)
- **related_to:** [API Design and Contracts](api-design.md), [HTTP and Remote Procedure Calls](http-and-rpc.md)
- **supported_by:** [Design Patterns Elements of Reusable Object-Oriented Software](../references/design-patterns-book.md)
