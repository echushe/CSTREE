---
id: "discrete-mathematics"
type: "concept"
title: "Discrete Mathematics for Software"
aliases: ["Logic", "Invariants", "Proof by induction"]
domains: ["algorithms"]
branch: "algorithms"
---

# Discrete Mathematics for Software

## What it is and why it matters

Discrete mathematics supplies the language for describing programs: sets, functions, relations, logic, counting, and proof. Invariants turn an intuition about code into a statement that can be checked.

## Mechanism

A loop invariant holds before the first iteration, is preserved by every iteration, and implies the required result at termination. Induction proves claims over recursive structure. A relation can be reflexive, symmetric, transitive, or a partial order; these distinctions matter in dependency graphs and event ordering.

## Worked example

To sum an array, keep `s = sum(a[0:i])` before iteration `i`. Initially `i = 0` and `s = 0`. Adding `a[i]` establishes the invariant for `i + 1`. At `i = n`, `s` is the sum of the entire array.

## Engineering implications

State preconditions such as sorted input or nonnegative weights before choosing an algorithm. Test boundary cases, then use an invariant to explain why all cases work. Proof and testing answer different questions: a proof depends on its model, while a test exercises an implementation.

## Graph connections

- **supported_by:** [Introduction to Algorithms](../references/algorithms-reference.md)
- **used_by:** [Algorithm Analysis](algorithm-analysis.md), [Graphs and Graph Algorithms](graphs.md), [Formal Methods and Verification](formal-methods.md)
