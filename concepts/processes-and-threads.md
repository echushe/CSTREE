---
id: "processes-and-threads"
type: "concept"
title: "Processes and Threads"
aliases: ["Process", "Thread", "Scheduling", "Concurrency", "Parallelism"]
domains: ["operating-systems"]
branch: "operating-systems"
---

# Processes and Threads

## What it is and why it matters

A process provides an execution and resource boundary, usually including an address space. Threads within a process share much of that state while having their own execution state.

## Mechanism

Scheduling selects runnable work. A context switch saves and restores execution state. Concurrency means work can overlap in progress; parallelism means work executes simultaneously. Processes communicate through explicit mechanisms such as pipes, sockets, or shared memory. Runtime tasks need not correspond one-to-one with OS threads.

## Worked example

Two threads reading and writing one counter can lose increments if each reads 0 before either stores 1. Two processes normally do not share that ordinary heap variable at all; sharing requires an explicit communication or mapping mechanism.

## Engineering implications

Choose a concurrency model based on isolation, communication cost, and workload. Account for creation, cancellation, joining, and cleanup. More threads can increase contention or memory pressure. A blocked thread, runnable thread, and CPU-consuming thread require different debugging responses.

## Graph connections

- **requires:** [Operating Systems](operating-systems.md)
- **related_to:** [Synchronization and Concurrency Control](synchronization.md), [I/O and Event Loops](io-and-event-loops.md), [Distributed Systems](distributed-systems.md)
- **supported_by:** [Operating Systems Three Easy Pieces](../references/operating-systems-book.md)
