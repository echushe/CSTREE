---
id: "compilers"
type: "concept"
title: "Compilers and Toolchains"
aliases: ["Compiler pipeline", "Linker", "Toolchain"]
domains: ["compilers"]
branch: "compilers"
---

# Compilers and Toolchains

## What it is and why it matters

A compiler translates a program into another representation while preserving defined behavior. A toolchain also assembles, links, packages, and loads the result.

## Mechanism

A typical pipeline is source → tokens → syntax tree → name and type analysis → intermediate representation → optimization → target code. Some stages are combined or repeated. Ahead-of-time compilation happens before execution; JIT compilation happens during it. Transpilation and bytecode compilation are also forms of translation.

## Worked example

For `2 + 3 * 4`, the parser builds addition with multiplication as its right child. Constant folding can replace the expression with 14 when the language semantics permit it. A native backend emits machine instructions; a bytecode backend targets a virtual machine.

## Engineering implications

Separate source errors from linker errors, runtime faults, and package-resolution failures. Optimizations rely on language rules, including overflow and undefined behavior. Debug information maps transformed code back to source but cannot always preserve the appearance of every source variable.

## Graph connections

- **requires:** [Programming Languages](programming-languages.md), [Trees and Search Trees](trees.md)
- **contains:** [Parsing and Abstract Syntax Trees](parsing-and-asts.md), [Intermediate Representation and Optimization](intermediate-representation.md), [Runtimes and Program Execution](runtimes-and-execution.md)
- **uses:** [Hash Tables](hash-tables.md), [Type Systems](type-systems.md)
- **related_to:** [Build Systems and Dependencies](build-and-dependencies.md)
- **supported_by:** [LLVM Language Implementation Tutorial](../references/llvm-tutorial.md)
