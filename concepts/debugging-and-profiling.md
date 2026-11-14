---
id: "debugging-and-profiling"
type: "concept"
title: "Debugging and Profiling"
aliases: ["Debugger", "Profiler", "Flame graph", "Root cause analysis"]
domains: ["engineering"]
branch: "engineering"
---

# Debugging and Profiling

## What it is and why it matters

Debugging explains incorrect behavior; profiling measures where resources are spent. Both work best as hypothesis-driven investigation rather than speculative editing.

## Mechanism

Create a reproducible observation, reduce the relevant inputs, form a hypothesis, and choose a measurement that can distinguish explanations. Debuggers inspect state and execution; logs preserve events; profilers sample or instrument resource use. Wall time, CPU time, allocations, and lock waits answer different questions.

## Worked example

A request takes 2 seconds but uses 20 ms of CPU. Optimizing a CPU loop is unlikely to explain most of the delay. Trace dependency calls, queue wait, lock wait, and I/O; then check whether the suspected delay actually accounts for the observed duration.

## Engineering implications

Preserve evidence and change one useful variable at a time. Profiling can perturb timing, and samples need adequate duration. Verify a fix with the original failure and a focused regression check. A flame graph shows aggregated stacks, not necessarily a chronological sequence.

## Graph connections

- **requires:** [Programming Languages](programming-languages.md), [Algorithm Analysis](algorithm-analysis.md)
- **related_to:** [Observability and Reliability](observability.md), [Performance Engineering](performance-engineering.md), [Version Control and Git](version-control.md)
- **supported_by:** [Site Reliability Engineering](../references/sre-book.md), [Software Engineering and Git Guides](../references/software-construction.md)
