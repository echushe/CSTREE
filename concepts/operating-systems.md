---
id: "operating-systems"
type: "concept"
title: "Operating Systems"
aliases: ["OS", "Kernel", "System calls"]
domains: ["operating-systems"]
branch: "operating-systems"
---

# Operating Systems

## What it is and why it matters

An operating system manages hardware resources and provides protected abstractions for programs. Its behavior explains scheduling, memory, files, and I/O observed by application code.

## Mechanism

User and kernel modes separate privileges. System calls request kernel services. The OS multiplexes processors, isolates address spaces, and exposes persistent storage and devices. Virtualization, concurrency, and persistence form a useful learning sequence.

## Worked example

A program requesting a file read crosses an OS interface. If data is cached, the request can complete without a device read. If not, the thread may wait while another runnable thread uses the CPU. Application-level duration includes more than the cost of a function call.

## Engineering implications

Differentiate CPU time from elapsed time and user memory from kernel buffers or caches. Resource limits and scheduling affect programs even when their algorithms are correct. Learn with small process, file, and memory experiments before tuning platform-specific settings.

## Graph connections

- **requires:** [Memory Management and Ownership](memory-management.md)
- **contains:** [Processes and Threads](processes-and-threads.md), [Synchronization and Concurrency Control](synchronization.md), [Virtual Memory](virtual-memory.md), [File Systems and Persistence](file-systems.md), [I/O and Event Loops](io-and-event-loops.md)
- **related_to:** [Computer Networks](computer-networks.md), [Runtimes and Program Execution](runtimes-and-execution.md)
- **supported_by:** [Operating Systems Three Easy Pieces](../references/operating-systems-book.md)
