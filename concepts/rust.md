---
id: "rust"
type: "concept"
title: "Rust"
aliases: ["Borrow checker", "Rust language"]
domains: ["languages"]
branch: "languages"
---

# Rust

## What it is and why it matters

Rust uses ownership, borrowing, and static checking to support memory-safe systems programming without a mandatory tracing garbage collector.

## Mechanism

An owning value normally moves when transferred. Shared borrows permit reading; an exclusive mutable borrow permits mutation under the borrowing rules. Lifetimes describe valid relationships between references. `Option` and `Result` make absence and recoverable failure explicit. Unsafe code carries additional obligations that safe callers may depend on.

## Worked example

With `let a = String::from("hi"); let b = a;`, ownership moves to b and using a afterward is rejected. Borrowing with `let b = &a;` instead lets code read through b while a retains ownership.

## Engineering implications

Learning to model ownership often matters more than learning syntax. Reference counting, interior mutability, and async execution introduce further design choices. Rust prevents important classes of bugs in safe code; it does not prove business correctness or eliminate deadlocks and resource leaks.

## Graph connections

- **requires:** [Memory Management and Ownership](memory-management.md), [Type Systems](type-systems.md)
- **compares_with:** [C++](cpp.md), [C](c.md), [Go](go.md)
- **related_to:** [Synchronization and Concurrency Control](synchronization.md)
- **supported_by:** [Language Specifications and Official Guides](../references/language-specifications.md)
