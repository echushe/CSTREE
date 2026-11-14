---
id: "cpp"
type: "concept"
title: "C++"
aliases: ["C plus plus"]
domains: ["languages"]
branch: "languages"
---

# C++

## What it is and why it matters

C++ combines low-level control with value types, generic programming, and deterministic resource management. Good C++ design makes ownership visible through types.

## Mechanism

RAII binds resource release to object destruction. Containers and smart pointers encode common ownership policies; move semantics transfer resources without copying their contents. Templates support generic code. Virtual functions provide runtime dispatch when a polymorphic interface is needed.

## Worked example

A `std::vector<int> xs{1,2,3};` owns its storage and releases it automatically. A `std::unique_ptr<T>` expresses exclusive ownership. Moving that pointer transfers ownership; copying it is disallowed.

## Engineering implications

Prefer standard containers and explicit ownership over unmanaged owning pointers. Understand iterator invalidation, exceptions, and object lifetime before optimizing. Shared ownership adds coordination and can create cycles. C knowledge is useful context, but C++ can be learned directly through its own resource and value idioms.

## Graph connections

- **requires:** [Memory Management and Ownership](memory-management.md), [Type Systems](type-systems.md)
- **compares_with:** [C](c.md), [Rust](rust.md)
- **related_to:** [Design Patterns](design-patterns.md), [Compilers and Toolchains](compilers.md)
- **supported_by:** [Language Specifications and Official Guides](../references/language-specifications.md)
