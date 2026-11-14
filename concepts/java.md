---
id: "java"
type: "concept"
title: "Java"
aliases: ["JVM language"]
domains: ["languages"]
branch: "languages"
---

# Java

## What it is and why it matters

Java is a statically typed language commonly executed on the JVM. Its runtime and library ecosystem support long-lived services and portable application code.

## Mechanism

Classes and interfaces express nominal types; generics add parameterized abstractions. Java source typically compiles to bytecode, which a JVM interprets or JIT compiles. Managed objects are garbage collected. Exceptions and structured resource handling address different failure and lifetime concerns.

## Worked example

Putting the same object reference into two lists does not copy the object. Mutating the object through one reference is visible through the other. Copying a list changes the list container, but does not necessarily deep-copy its elements.

## Engineering implications

Understand `equals` and `hashCode` together before using objects as map keys. Close external resources with try-with-resources where applicable. Measure allocation, warmup, and GC behavior rather than equating bytecode execution with a fixed performance profile.

## Graph connections

- **requires:** [Type Systems](type-systems.md), [Programming Paradigms](programming-paradigms.md)
- **compares_with:** [C#](csharp.md), [Go](go.md)
- **uses:** [Runtimes and Program Execution](runtimes-and-execution.md)
- **supported_by:** [Language Specifications and Official Guides](../references/language-specifications.md)
