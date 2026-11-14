---
id: "searching"
type: "concept"
title: "Searching and Binary Search"
aliases: ["Binary search", "Lower bound"]
domains: ["algorithms"]
branch: "algorithms"
---

# Searching and Binary Search

## What it is and why it matters

Searching finds an item or a boundary satisfying a condition. Binary search is useful whenever a predicate changes monotonically over an ordered range.

## Mechanism

Linear search is O(n) and needs no ordering. Binary search halves a search interval and takes O(log n) comparisons on random-access data. For lower-bound search, keep a half-open range `[lo, hi)` and discard the half that cannot contain the first value at least the target.

## Worked example

Find the first value at least 4 in `[1, 3, 3, 7, 9]`. Start lo=0, hi=5. Mid=2 holds 3, so lo=3. Mid=4 holds 9, so hi=4. Mid=3 holds 7, so hi=3. Return index 3; equality is not required.

## Engineering implications

Specify whether duplicates return any match, the first, or the insertion point. Test empty ranges and all-true/all-false predicates. Binary search over a linked list does not inherit the same access cost as an array. For fixed-width integer code, avoid overflowing the midpoint calculation.

## Graph connections

- **requires:** [Arrays and Linked Lists](arrays-and-linked-lists.md), [Discrete Mathematics for Software](discrete-mathematics.md)
- **related_to:** [Sorting Algorithms](sorting.md), [Trees and Search Trees](trees.md)
- **supported_by:** [Introduction to Algorithms](../references/algorithms-reference.md)
