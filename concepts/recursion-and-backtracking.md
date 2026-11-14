---
id: "recursion-and-backtracking"
type: "concept"
title: "Recursion and Backtracking"
aliases: ["Divide and conquer", "Backtracking", "Recursion"]
domains: ["algorithms"]
branch: "algorithms"
---

# Recursion and Backtracking

## What it is and why it matters

Recursion solves a problem through smaller instances. Backtracking explores choices while undoing state when a partial solution cannot or need not be extended.

## Mechanism

A recursive function needs a base case and a measure that decreases toward it. Divide-and-conquer solves subproblems and combines results; backtracking explores a search tree. Maintain the invariant that shared state represents exactly the choices on the current path.

## Worked example

Enumerate subsets of `[A,B]`: choose or skip A, then choose or skip B, yielding `[]`, `[B]`, `[A]`, `[A,B]`. With n items there are `2^n` subsets; recursion does not remove that output cost. Restore a mutable path after each recursive call.

## Engineering implications

Watch call-stack depth and avoid accidentally sharing mutable results. Pruning needs a valid reason that excluded branches cannot contain a required answer. Memoization can replace repeated exploration when different paths reach the same subproblem.

## Graph connections

- **requires:** [Stacks](stacks.md), [Discrete Mathematics for Software](discrete-mathematics.md)
- **extended_by:** [Dynamic Programming](dynamic-programming.md)
- **used_by:** [Parsing and Abstract Syntax Trees](parsing-and-asts.md), [Trees and Search Trees](trees.md)
- **supported_by:** [Introduction to Algorithms](../references/algorithms-reference.md)
