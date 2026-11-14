---
id: "memory-management"
type: "concept"
title: "Memory Management and Ownership"
aliases: ["Ownership", "RAII", "Garbage collection", "Lifetimes"]
domains: ["languages"]
branch: "languages"
---

# Memory Management and Ownership

## What it is and why it matters

Memory management controls object lifetime and resource access. The central questions are who owns a value, who may reference it, and when the storage can be reused.

## Mechanism

Automatic storage commonly follows call scope; dynamic allocation supports other lifetimes. Manual allocation pairs allocation with release. RAII couples resource release to object lifetime. Tracing garbage collection reclaims unreachable managed objects; reference counting reclaims when strong references reach zero but needs a policy for cycles. Ownership and borrowing can enforce lifetime rules statically.

## Worked example

Returning a pointer to a local C variable creates a dangling reference after the function returns. Returning an owning value or allocating with a clearly documented owner changes the lifetime. A garbage-collected object can still hold an open file that needs prompt closure.

## Engineering implications

Track non-memory resources such as files, sockets, and locks separately. Distinguish leaks, use-after-free, aliasing errors, and retained-but-reachable objects. Allocation rate and object layout affect performance even in managed languages.

## Graph connections

- **requires:** [Programming Languages](programming-languages.md)
- **related_to:** [Virtual Memory](virtual-memory.md), [C](c.md), [C++](cpp.md), [Rust](rust.md), [Runtimes and Program Execution](runtimes-and-execution.md)
- **supported_by:** [Language Specifications and Official Guides](../references/language-specifications.md), [Operating Systems Three Easy Pieces](../references/operating-systems-book.md)
