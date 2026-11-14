---
id: "type-systems"
type: "concept"
title: "Type Systems"
aliases: ["Static typing", "Dynamic typing", "Generics", "Algebraic data types"]
domains: ["languages"]
branch: "languages"
---

# Type Systems

## What it is and why it matters

Types describe which values and operations can be combined. Static checks reject some invalid programs before execution; dynamic checks inspect values while the program runs.

## Mechanism

Nominal typing relates declared identities; structural typing relates shapes. Generics express reusable operations parameterized by types. Sum types represent alternatives, product types combine fields, and nullability adds an absence case. Type inference changes how types are written, not whether checking is static.

## Worked example

A result `Success(value) | Failure(error)` forces a caller to consider both alternatives in languages with exhaustive checking. A string containing `"42"` is still a string; converting it to an integer can fail and needs a defined policy.

## Engineering implications

Static types do not automatically validate network input or database rows. Casts, foreign interfaces, unchecked operations, and unsound features can weaken guarantees. Model domain states so invalid combinations are difficult to express, then validate external data at boundaries.

## Graph connections

- **requires:** [Programming Languages](programming-languages.md)
- **used_by:** [TypeScript](typescript.md), [Rust](rust.md), [Java](java.md), [C#](csharp.md), [Compilers and Toolchains](compilers.md)
- **related_to:** [API Design and Contracts](api-design.md), [Formal Methods and Verification](formal-methods.md)
- **supported_by:** [Language Specifications and Official Guides](../references/language-specifications.md)
