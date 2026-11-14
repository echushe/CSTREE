---
id: "graphs"
type: "concept"
title: "Graphs and Graph Algorithms"
aliases: ["BFS", "DFS", "DAG", "Topological sort", "Dijkstra"]
domains: ["algorithms"]
branch: "algorithms"
---

# Graphs and Graph Algorithms

## What it is and why it matters

A graph models relationships among entities: dependencies, routes, calls, ownership, or state transitions. It can be directed or undirected, weighted or unweighted.

## Mechanism

An adjacency list uses O(V + E) storage; a matrix uses O(V^2). BFS uses a queue and finds shortest paths by edge count in an unweighted graph. DFS uses recursion or a stack. Both take O(V + E) with adjacency lists. Topological sorting applies only to directed acyclic graphs. Dijkstra requires nonnegative edge weights.

## Worked example

For edges A→B, A→C, B→D, C→D, BFS from A assigns distances A=0, B=C=1, D=2. Either A,B,C,D or A,C,B,D is a valid topological order. Adding D→A creates a cycle and removes the possibility of such an order.

## Engineering implications

Mark visited nodes at a deliberate point to avoid duplicate work. Specify edge direction when modeling dependencies: this repository points `requires` from learner topic to prerequisite. Its full graph may contain cycles, while the prerequisite subgraph must not.

## Graph connections

- **requires:** [Algorithm Analysis](algorithm-analysis.md), [Queues and Deques](queues.md), [Stacks](stacks.md)
- **related_to:** [Heaps and Priority Queues](heaps.md), [Build Systems and Dependencies](build-and-dependencies.md), [Distributed Systems](distributed-systems.md)
- **supported_by:** [Introduction to Algorithms](../references/algorithms-reference.md)
