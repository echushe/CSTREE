---
id: "programming-languages"
type: "concept"
title: "Programming Languages"
aliases: ["PL", "Language semantics"]
domains: ["languages"]
branch: "languages"
---

# Programming Languages

## What it is and why it matters

A programming language defines how programs express computation. A language, its implementation, its standard library, and its package ecosystem are related but distinct choices.

## Mechanism

Compare languages along independent axes: static or dynamic checking, value and reference semantics, resource ownership, error handling, concurrency, and runtime execution. Compiled and interpreted describe implementation techniques, not a strict division of all languages. Many implementations combine bytecode, interpretation, and JIT compilation.

## Worked example

The expression `a + b` may mean integer addition, string concatenation, or an overloaded operation depending on types and language rules. The same algorithm translated across languages can change overflow behavior, allocation cost, and failure modes.

## Engineering implications

Learn one language deeply, then compare another through concrete tasks: parse input, manage a resource, handle an error, and run concurrent work. Evaluate libraries, deployment targets, interoperability, and maintenance constraints alongside syntax.

## Graph connections

- **requires:** [Discrete Mathematics for Software](discrete-mathematics.md)
- **contains:** [Type Systems](type-systems.md), [Memory Management and Ownership](memory-management.md), [Programming Paradigms](programming-paradigms.md), [C](c.md), [C++](cpp.md), [Java](java.md), [Python](python.md), [C#](csharp.md), [Go](go.md), [Rust](rust.md), [JavaScript](javascript.md), [TypeScript](typescript.md)
- **related_to:** [Compilers and Toolchains](compilers.md)
- **supported_by:** [Language Specifications and Official Guides](../references/language-specifications.md)
