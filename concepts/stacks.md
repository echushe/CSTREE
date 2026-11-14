---
id: "stacks"
type: "concept"
title: "Stacks"
aliases: ["LIFO"]
domains: ["algorithms"]
branch: "algorithms"
---

# Stacks

## What it is and why it matters

A stack is a last-in, first-out abstract data type. It models nested work: function calls, undo history, expression evaluation, and depth-first traversal.

## Mechanism

Expose `push`, `pop`, and `peek`. An array-backed stack appends and removes at its end, normally amortized O(1); a linked implementation changes the head in O(1). Handle underflow explicitly. A runtime call stack also stores activation records, return addresses, and local state.

## Worked example

For tokens `2 3 + 4 *`, push 2 and 3, pop both to compute 5, push 4, then compute 5 * 4 = 20. For noncommutative operators, the first popped item is the right operand.

## Engineering implications

Use an explicit stack when recursion depth may exceed runtime limits or when traversal state must be paused. Distinguish the stack abstract data type from a thread stack memory region. Persistent undo often needs commands or snapshots beyond the basic container.

## Graph connections

- **requires:** [Arrays and Linked Lists](arrays-and-linked-lists.md)
- **used_by:** [Recursion and Backtracking](recursion-and-backtracking.md), [Parsing and Abstract Syntax Trees](parsing-and-asts.md), [Graphs and Graph Algorithms](graphs.md)
- **related_to:** [Processes and Threads](processes-and-threads.md)
- **supported_by:** [Introduction to Algorithms](../references/algorithms-reference.md)
