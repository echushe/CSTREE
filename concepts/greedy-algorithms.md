---
id: "greedy-algorithms"
type: "concept"
title: "Greedy Algorithms"
aliases: ["Greedy choice", "Exchange argument"]
domains: ["algorithms"]
branch: "algorithms"
---

# Greedy Algorithms

## What it is and why it matters

A greedy algorithm commits to a locally attractive choice without revisiting it. It is powerful when an exchange argument or another proof connects that local rule to a global optimum.

## Mechanism

Specify the objective, feasible choices, and selection rule. Prove that some optimal solution can begin with the greedy choice, then reduce to the remaining problem. Sorting often exposes the rule. A plausible heuristic is not an optimal greedy algorithm until the necessary property is established.

## Worked example

To maximize the number of nonoverlapping intervals, choose the earliest finishing compatible interval. For `[0,3), [1,2), [2,4)`, earliest finish selects `[1,2)` and `[2,4)` for two intervals; choosing earliest start instead yields only `[0,3)`.

## Engineering implications

Try small counterexamples before investing in an implementation. Coin change fails for arbitrary denominations, while interval scheduling has an exchange proof. Weighted interval scheduling needs a different approach, commonly dynamic programming.

## Graph connections

- **requires:** [Algorithm Analysis](algorithm-analysis.md), [Discrete Mathematics for Software](discrete-mathematics.md)
- **compares_with:** [Dynamic Programming](dynamic-programming.md)
- **uses:** [Sorting Algorithms](sorting.md), [Heaps and Priority Queues](heaps.md)
- **supported_by:** [Introduction to Algorithms](../references/algorithms-reference.md)
