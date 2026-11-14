---
id: "queues"
type: "concept"
title: "Queues and Deques"
aliases: ["FIFO", "Deque", "Ring buffer"]
domains: ["algorithms"]
branch: "algorithms"
---

# Queues and Deques

## What it is and why it matters

A queue removes items in first-in, first-out order. A deque supports insertion and removal at both ends. Both are basic tools for buffering and scheduling work.

## Mechanism

A circular buffer tracks head, tail, and size in fixed storage; enqueue and dequeue can be O(1). A linked queue needs both head and tail for O(1) end operations. A bounded queue must define what happens when full: block, reject, drop, or overwrite.

## Worked example

With capacity 3, enqueue A, B, C. Dequeue A, then enqueue D into the reused slot. The logical order is B, C, D even though the backing array wraps. Distinguishing full from empty requires a size counter or another explicit convention.

## Engineering implications

Avoid removing the first element of a dynamic array when that shifts all remaining elements. Bounded queues make overload visible. Thread safety, durable delivery, acknowledgments, and retries are additional guarantees; they do not follow from FIFO alone.

## Graph connections

- **requires:** [Arrays and Linked Lists](arrays-and-linked-lists.md)
- **used_by:** [Graphs and Graph Algorithms](graphs.md), [Messaging and Event Streams](messaging-and-streams.md), [I/O and Event Loops](io-and-event-loops.md)
- **related_to:** [Resilience and Idempotency](resilience-and-idempotency.md)
- **supported_by:** [Introduction to Algorithms](../references/algorithms-reference.md)
