---
id: "trees"
type: "concept"
title: "Trees and Search Trees"
aliases: ["Binary search tree", "BST", "B-tree", "Trie"]
domains: ["algorithms"]
branch: "algorithms"
---

# Trees and Search Trees

## What it is and why it matters

Trees represent hierarchy using nodes and parent-child edges. Search trees add an ordering invariant so lookup can skip entire subtrees.

## Mechanism

A rooted tree has one root and one parent for each non-root node. A binary search tree places smaller keys on one side and larger keys on the other, with an explicit duplicate policy. Search costs O(h), where h is height: O(log n) when balanced, O(n) when skewed. B-trees use wider nodes suited to storage pages.

## Worked example

Insert 4, 2, 6, 1, 3 into a binary search tree. Searching for 3 visits 4, 2, 3. In-order traversal yields 1, 2, 3, 4, 6. Inserting already sorted keys into an unbalanced tree instead creates a chain.

## Engineering implications

Use balancing or a standard library ordered map when worst-case height matters. Tries organize keys by prefixes; they are not binary search trees. ASTs, directory trees, and indexes share tree structure but enforce different invariants.

## Graph connections

- **requires:** [Algorithm Analysis](algorithm-analysis.md)
- **related_to:** [Graphs and Graph Algorithms](graphs.md), [Parsing and Abstract Syntax Trees](parsing-and-asts.md), [File Systems and Persistence](file-systems.md)
- **used_by:** [Indexes and Query Planning](indexes-and-query-planning.md), [Heaps and Priority Queues](heaps.md)
- **supported_by:** [Introduction to Algorithms](../references/algorithms-reference.md)
