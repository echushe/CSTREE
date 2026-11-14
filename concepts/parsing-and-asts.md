---
id: "parsing-and-asts"
type: "concept"
title: "Parsing and Abstract Syntax Trees"
aliases: ["Parser", "Lexer", "AST", "Grammar"]
domains: ["compilers"]
branch: "compilers"
---

# Parsing and Abstract Syntax Trees

## What it is and why it matters

Parsing converts tokens into grammatical structure. An abstract syntax tree keeps the parts needed for later analysis while discarding punctuation or other concrete syntax details.

## Mechanism

Lexing recognizes token classes such as identifiers and numbers. Parsing applies grammar rules and operator precedence. Recursive descent often gives one routine per grammar rule; Pratt parsing is another useful expression technique. Name resolution and type checking are semantic stages after syntax has been recognized.

## Worked example

Tokens for `a + b * c` become `Add(Name(a), Multiply(Name(b), Name(c)))`. Parenthesizing `(a + b) * c` changes the AST to `Multiply(Add(Name(a), Name(b)), Name(c))`. The AST itself is not yet a computed value.

## Engineering implications

Preserve source spans for diagnostics and refactoring. Error recovery should avoid turning one malformed token into many misleading messages. Distinguish a syntax tree from a control-flow graph: conditional and loop execution introduce relationships absent from simple parent-child syntax.

## Graph connections

- **requires:** [Compilers and Toolchains](compilers.md), [Recursion and Backtracking](recursion-and-backtracking.md)
- **uses:** [Stacks](stacks.md), [Trees and Search Trees](trees.md)
- **related_to:** [Type Systems](type-systems.md), [Intermediate Representation and Optimization](intermediate-representation.md)
- **supported_by:** [LLVM Language Implementation Tutorial](../references/llvm-tutorial.md)
