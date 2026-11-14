---
id: "sorting"
type: "concept"
title: "Sorting Algorithms"
aliases: ["Merge sort", "Quicksort", "Heapsort", "Stable sorting"]
domains: ["algorithms"]
branch: "algorithms"
---

# Sorting Algorithms

## What it is and why it matters

Sorting establishes an order that enables binary search, grouping, merge operations, and reproducible output. The right algorithm depends on data size, order, memory, and stability requirements.

## Mechanism

Merge sort has O(n log n) worst-case time and typically O(n) auxiliary array space. Quicksort has expected O(n log n) time with suitable pivot randomization, but O(n^2) worst case in its basic form. Heapsort is O(n log n) worst case. Insertion sort is O(n^2) worst case but useful for small or nearly sorted ranges. Comparison sorting has an Omega(n log n) worst-case lower bound; counting and radix methods use extra key assumptions.

## Worked example

For records `(2,A), (1,B), (2,C)`, a stable sort by the numeric key yields `(1,B), (2,A), (2,C)`. Stability preserves the relative order of A and C. Merge `[1,4]` and `[2,3]` by repeatedly taking the smaller front element to obtain `[1,2,3,4]`.

## Engineering implications

Define a consistent comparator and consider nulls, NaNs, locale, and tie-breakers. Standard library algorithms may be hybrids. External sorting uses runs and multiway merging when data exceeds memory. Benchmark the actual key extraction and comparison costs.

## Graph connections

- **requires:** [Algorithm Analysis](algorithm-analysis.md), [Arrays and Linked Lists](arrays-and-linked-lists.md)
- **uses:** [Heaps and Priority Queues](heaps.md), [Recursion and Backtracking](recursion-and-backtracking.md)
- **used_by:** [Indexes and Query Planning](indexes-and-query-planning.md)
- **supported_by:** [Introduction to Algorithms](../references/algorithms-reference.md)
