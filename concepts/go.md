---
id: "go"
type: "concept"
title: "Go"
aliases: ["Golang"]
domains: ["languages"]
branch: "languages"
---

# Go

## What it is and why it matters

Go combines static typing, garbage collection, and lightweight concurrent execution. Its language and standard tooling encourage straightforward service and systems code.

## Mechanism

Interfaces are satisfied implicitly by method sets. Goroutines run concurrently under a scheduler; channels communicate values and synchronization. Errors are commonly returned as values. Slices describe a segment of a backing array, so separate slice values can still share storage.

## Worked example

For `a := []int{1,2,3}; b := a[:2]`, assigning `b[0] = 9` changes `a[0]` too. Copying into a separately allocated slice avoids that alias. Appending may allocate a new backing array, so sharing must not be inferred from syntax alone.

## Engineering implications

Every goroutine needs a completion or cancellation story. Concurrent map access and shared mutable state require the appropriate coordination. Consult the language specification and current documentation for features such as generics; Effective Go explicitly does not cover all later language changes.

## Graph connections

- **requires:** [Type Systems](type-systems.md)
- **related_to:** [Synchronization and Concurrency Control](synchronization.md), [Processes and Threads](processes-and-threads.md)
- **compares_with:** [Java](java.md), [Rust](rust.md)
- **supported_by:** [Language Specifications and Official Guides](../references/language-specifications.md)
