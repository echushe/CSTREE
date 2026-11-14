---
id: "runtimes-and-execution"
type: "concept"
title: "Runtimes and Program Execution"
aliases: ["JIT", "Bytecode", "VM", "ABI"]
domains: ["compilers"]
branch: "compilers"
---

# Runtimes and Program Execution

## What it is and why it matters

A runtime supplies services a program uses while executing: calling conventions, allocation, exception handling, scheduling, loading, or virtual-machine execution.

## Mechanism

Native programs still depend on operating-system and library services. Managed runtimes may interpret bytecode, JIT compile hot code, and collect garbage. Stack frames implement calls; closures preserve captured state beyond a single call when needed. An ABI defines binary-level interaction, distinct from a source API.

## Worked example

A function returning a closure over a counter needs that counter to remain alive after the outer function returns. A runtime can store captured state in an allocated environment rather than leaving it in an invalid stack frame.

## Engineering implications

Startup cost, warmup, allocation, GC pauses, and foreign calls affect latency differently. Distinguish language guarantees from implementation choices. Runtime scheduling does not remove data races, and garbage collection does not automatically close external resources.

## Graph connections

- **requires:** [Programming Languages](programming-languages.md), [Memory Management and Ownership](memory-management.md)
- **related_to:** [Compilers and Toolchains](compilers.md), [Processes and Threads](processes-and-threads.md), [I/O and Event Loops](io-and-event-loops.md), [Debugging and Profiling](debugging-and-profiling.md)
- **supported_by:** [Language Specifications and Official Guides](../references/language-specifications.md), [Operating Systems Three Easy Pieces](../references/operating-systems-book.md)
