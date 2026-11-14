---
id: "c"
type: "concept"
title: "C"
aliases: ["C language"]
domains: ["languages"]
branch: "languages"
---

# C

## What it is and why it matters

C exposes pointers, object representations, and explicit resource management. It is useful for learning systems interfaces and the obligations that higher-level runtimes often handle.

## Mechanism

Programs use functions, structs, arrays, and pointers. Array bounds and allocated lifetimes require explicit care. Compilation usually produces object files that a linker combines. Undefined behavior places no requirements on execution; it is different from implementation-defined behavior documented by an implementation.

## Worked example

For `int a[3] = {10,20,30};`, `a[1]` is 20. Accessing `a[3]` is out of bounds. A pointer plus a length can describe a buffer, but the function must still enforce the length contract.

## Engineering implications

Use warnings, sanitizers, and narrow ownership rules. Check allocation and I/O errors, integer conversions, and buffer lengths. N1570 is a public C11 committee draft used here for enduring fundamentals; it is not a statement of the latest C standard.

## Graph connections

- **requires:** [Memory Management and Ownership](memory-management.md)
- **compares_with:** [C++](cpp.md), [Rust](rust.md)
- **related_to:** [Operating Systems](operating-systems.md), [Compilers and Toolchains](compilers.md)
- **supported_by:** [Language Specifications and Official Guides](../references/language-specifications.md)
