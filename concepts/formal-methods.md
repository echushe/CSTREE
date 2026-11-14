---
id: "formal-methods"
type: "concept"
title: "Formal Methods and Verification"
aliases: ["Model checking", "Verification", "State machines", "Safety", "Liveness"]
domains: ["engineering"]
branch: "engineering"
---

# Formal Methods and Verification

## What it is and why it matters

Formal methods describe and analyze behavior with mathematical models. They are useful when subtle state interactions make examples alone insufficient.

## Mechanism

A specification can define states, allowed transitions, and invariants. Model checking explores modeled behaviors, often under finite bounds. Deductive verification proves obligations from assumptions. Type systems provide another form of static reasoning. Safety and liveness need different properties and environmental assumptions.

## Worked example

Model a two-slot buffer with enqueue and dequeue transitions. Check that size always lies between 0 and 2 and dequeued values follow enqueue order. A model that omits crashes cannot establish crash recovery behavior, even if every explored state passes.

## Engineering implications

Use small models to clarify protocols and counterexamples. State the abstraction and what is outside it. A proved model still needs a justified connection to the actual implementation. Combine formal reasoning with tests, review, and runtime evidence where each addresses a different uncertainty.

## Graph connections

- **requires:** [Discrete Mathematics for Software](discrete-mathematics.md), [Requirements and Specifications](requirements-and-specifications.md)
- **related_to:** [Type Systems](type-systems.md), [Software Testing](testing.md), [Synchronization and Concurrency Control](synchronization.md), [Replication and Consensus](replication-and-consensus.md)
- **supported_by:** [Introduction to Algorithms](../references/algorithms-reference.md), [Time, Clocks, and the Ordering of Events in a Distributed System](../papers/lamport-1978-time-clocks.md)
