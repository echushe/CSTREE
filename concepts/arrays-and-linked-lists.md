---
id: "arrays-and-linked-lists"
type: "concept"
title: "Arrays and Linked Lists"
aliases: ["Array", "Vector", "Linked list"]
domains: ["algorithms"]
branch: "algorithms"
---

# Arrays and Linked Lists

## What it is and why it matters

Arrays store indexed elements contiguously; linked lists connect separately stored nodes. Their different memory layouts explain much of their practical performance.

## Mechanism

Array indexing is O(1). Inserting at an interior position shifts O(n) elements. A linked list inserts or removes in O(1) only when the necessary node and predecessor information are already available; finding a position is O(n). Dynamic arrays add capacity and resizing.

## Worked example

In `[10, 20, 30, 40]`, inserting 25 at index 2 shifts 30 and 40. In a singly linked list, insertion after a known node holding 20 updates two links. Finding that node still requires traversal unless another structure already points to it.

## Engineering implications

Prefer contiguous storage for sequential traversal and compactness. Lists add allocation and pointer overhead and usually have weaker cache locality. Iterator invalidation and reference stability are language and container specific. A list is not automatically faster because insertion is constant time.

## Graph connections

- **requires:** [Algorithm Analysis](algorithm-analysis.md)
- **used_by:** [Stacks](stacks.md), [Queues and Deques](queues.md), [Hash Tables](hash-tables.md)
- **related_to:** [Memory Management and Ownership](memory-management.md)
- **supported_by:** [Introduction to Algorithms](../references/algorithms-reference.md)
