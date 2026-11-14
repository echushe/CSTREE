---
id: "dynamic-programming"
type: "concept"
title: "Dynamic Programming"
aliases: ["DP", "Memoization", "Tabulation"]
domains: ["algorithms"]
branch: "algorithms"
---

# Dynamic Programming

## What it is and why it matters

Dynamic programming reuses solutions to overlapping subproblems. The hard part is choosing a state that contains all information needed for future decisions.

## Mechanism

Define the state, recurrence, base cases, evaluation order, and reconstruction rule. Memoization evaluates states on demand; tabulation evaluates them in dependency order. Cost is roughly number of reachable states times transition work. Optimal substructure supports optimization recurrences; counting and feasibility problems also use DP.

## Worked example

For minimum coins with denominations `{1,3,4}`, let `dp[0]=0` and `dp[x]=1+min(dp[x-c])` over valid coins c. Values for amounts 1 through 6 are 1,2,1,1,2,2. At 6, taking 3+3 beats the greedy choice 4+1+1. Store a chosen coin to reconstruct the answer.

## Engineering implications

Do not omit state such as remaining capacity or a previous choice when it changes valid futures. Represent unreachable states safely. Rolling arrays save memory only when discarded states will never be needed again. Pseudo-polynomial algorithms depend on numeric magnitudes, not just their encoded bit length.

## Graph connections

- **requires:** [Recursion and Backtracking](recursion-and-backtracking.md), [Algorithm Analysis](algorithm-analysis.md)
- **compares_with:** [Greedy Algorithms](greedy-algorithms.md)
- **related_to:** [Graphs and Graph Algorithms](graphs.md)
- **supported_by:** [Some Applications of the Theory of Dynamic Programming—A Review](../papers/bellman-1954-dynamic-programming.md), [Introduction to Algorithms](../references/algorithms-reference.md)
