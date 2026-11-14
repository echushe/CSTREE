---
id: "algorithm-analysis"
type: "concept"
title: "Algorithm Analysis"
aliases: ["Big O", "Complexity", "Amortized analysis"]
domains: ["algorithms"]
branch: "algorithms"
---

# Algorithm Analysis

## What it is and why it matters

Algorithm analysis describes how resource use grows with input size. It helps distinguish a constant-factor improvement from a change that remains useful at much larger scale.

## Mechanism

`O(g(n))` is an asymptotic upper bound; `Theta(g(n))` is a tight bound. State the case: worst, average under a distribution, or amortized across a sequence. Count time, auxiliary space, I/O, and allocations separately. Amortized cost does not mean every operation has that cost.

## Worked example

A dynamic array doubling capacity copies 1 + 2 + 4 + ... + 2^k elements over many appends. Before capacity exceeds `2n`, fewer than `2n` elements have been copied. Appending is therefore amortized O(1), although an individual resize takes O(n).

## Engineering implications

A linear scan can beat a pointer-heavy logarithmic structure on small data because of locality. Measure representative workloads after establishing the growth rate. Complexity statements should name their input variables: a graph traversal is O(V + E), not simply O(n).

## Graph connections

- **requires:** [Discrete Mathematics for Software](discrete-mathematics.md)
- **supported_by:** [Introduction to Algorithms](../references/algorithms-reference.md)
- **used_by:** [Sorting Algorithms](sorting.md), [Dynamic Programming](dynamic-programming.md), [Performance Engineering](performance-engineering.md)
