---
id: "heaps"
type: "concept"
title: "Heaps and Priority Queues"
aliases: ["Binary heap", "Priority queue"]
domains: ["algorithms"]
branch: "algorithms"
---

# Heaps and Priority Queues

## What it is and why it matters

A priority queue removes the most urgent item rather than the oldest. A binary heap is a compact tree-shaped implementation commonly stored in an array.

## Mechanism

In a min-heap, every parent is no greater than its children. With zero-based indexing, children of i are `2i + 1` and `2i + 2`. Peek is O(1); insert and remove-min are O(log n). Bottom-up heap construction is O(n). The structure is partially ordered, not globally sorted.

## Worked example

The array `[2, 5, 3, 9, 7]` is a min-heap. Removing 2 moves 7 to the root, then swaps it with 3, producing `[3, 5, 7, 9]`. The next minimum is available without sorting the whole array.

## Engineering implications

Useful for deadlines, top-k selection, and Dijkstra traversal. Updating priorities requires handles or a lazy-invalidation policy. Define tie-breaking if stable processing matters. The heap data structure is distinct from the heap memory region used for dynamic allocation.

## Graph connections

- **requires:** [Trees and Search Trees](trees.md), [Arrays and Linked Lists](arrays-and-linked-lists.md)
- **used_by:** [Graphs and Graph Algorithms](graphs.md), [Sorting Algorithms](sorting.md)
- **compares_with:** [Queues and Deques](queues.md)
- **supported_by:** [Introduction to Algorithms](../references/algorithms-reference.md)
