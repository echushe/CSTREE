---
id: "intermediate-representation"
type: "concept"
title: "Intermediate Representation and Optimization"
aliases: ["IR", "SSA", "Control-flow graph", "Compiler optimization"]
domains: ["compilers"]
branch: "compilers"
---

# Intermediate Representation and Optimization

## What it is and why it matters

An intermediate representation gives analyses and optimizations a common language between source syntax and machine instructions.

## Mechanism

A control-flow graph connects basic blocks. Data-flow analysis tracks facts such as live values or available expressions. Static single assignment gives each SSA value one definition; phi nodes merge values from predecessor paths. Code generation eventually selects instructions and assigns registers.

## Worked example

If one branch sets `x = 1` and another sets `x = 2`, SSA can name them `x1` and `x2`; the join defines `x3 = phi(x1, x2)`, selecting by the incoming edge. It does not compute an average or choose nondeterministically.

## Engineering implications

Optimization must preserve observable behavior under the target semantics. Reordering floating-point operations, memory access, or effects can change results. An IR verifier catches malformed representation, while differential or end-to-end tests check whether translation preserves behavior.

## Graph connections

- **requires:** [Compilers and Toolchains](compilers.md), [Graphs and Graph Algorithms](graphs.md)
- **related_to:** [Type Systems](type-systems.md), [Formal Methods and Verification](formal-methods.md), [Performance Engineering](performance-engineering.md)
- **supported_by:** [LLVM Language Implementation Tutorial](../references/llvm-tutorial.md)
