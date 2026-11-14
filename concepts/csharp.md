---
id: "csharp"
type: "concept"
title: "C#"
aliases: ["C sharp", ".NET"]
domains: ["languages"]
branch: "languages"
---

# C#

## What it is and why it matters

C# is a statically typed language in the .NET ecosystem. It supports managed application development with object-oriented and functional features.

## Mechanism

Classes typically have reference semantics; structs have value semantics. Generics, interfaces, delegates, and pattern matching express reusable behavior. `async` and `await` compose asynchronous operations; they do not imply that each operation receives a dedicated thread. The runtime manages memory, while disposable resources need lifetime handling.

## Worked example

Copying a struct containing an integer copies the value. Copying a reference to a class shares the instance. If a struct contains a reference field, copying the struct also copies that reference, so its referenced object remains shared.

## Engineering implications

Use `using` or an appropriate asynchronous disposal form for disposable resources. Distinguish tasks from threads and avoid blocking on asynchronous operations in contexts where that can deadlock. Nullability annotations help analysis but do not replace input validation.

## Graph connections

- **requires:** [Type Systems](type-systems.md), [Programming Paradigms](programming-paradigms.md)
- **compares_with:** [Java](java.md), [TypeScript](typescript.md)
- **related_to:** [I/O and Event Loops](io-and-event-loops.md)
- **supported_by:** [Language Specifications and Official Guides](../references/language-specifications.md)
