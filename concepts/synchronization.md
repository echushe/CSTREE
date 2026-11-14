---
id: "synchronization"
type: "concept"
title: "Synchronization and Concurrency Control"
aliases: ["Mutex", "Semaphore", "Condition variable", "Data races", "Deadlock", "Atomics"]
domains: ["operating-systems"]
branch: "operating-systems"
---

# Synchronization and Concurrency Control

## What it is and why it matters

Synchronization coordinates concurrent access and ordering. It protects invariants across operations, not merely individual variables.

## Mechanism

Mutexes protect critical sections; condition variables wait for predicates; semaphores track permits. Atomics provide operations and ordering defined by a memory model. A data race is a specific language-level violation; a race condition is a broader timing-dependent correctness problem. Deadlock involves mutually blocked progress under resource dependencies.

## Worked example

To take an item from a shared queue, hold its mutex and wait in a loop while empty. Waiting releases the mutex and reacquires it before returning. Recheck the predicate because notifications and scheduling do not guarantee the queue still contains an item.

## Engineering implications

Document lock ownership and a consistent lock acquisition order. Avoid holding locks over slow external I/O. An atomic increment does not make a compound check-then-update invariant atomic. Lock-free algorithms need careful reclamation and memory-order reasoning; fewer locks do not automatically mean less complexity.

## Graph connections

- **requires:** [Processes and Threads](processes-and-threads.md), [Discrete Mathematics for Software](discrete-mathematics.md)
- **related_to:** [Transactions and Isolation](transactions.md), [Rust](rust.md), [Go](go.md), [Formal Methods and Verification](formal-methods.md)
- **supported_by:** [Operating Systems Three Easy Pieces](../references/operating-systems-book.md), [Language Specifications and Official Guides](../references/language-specifications.md)
