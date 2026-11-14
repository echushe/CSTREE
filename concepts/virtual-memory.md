---
id: "virtual-memory"
type: "concept"
title: "Virtual Memory"
aliases: ["Paging", "Page fault", "TLB", "Address space"]
domains: ["operating-systems"]
branch: "operating-systems"
---

# Virtual Memory

## What it is and why it matters

Virtual memory maps process-visible addresses onto physical storage and enforces access permissions. It supports isolation and flexible use of physical memory.

## Mechanism

Page tables translate virtual pages to frames; a TLB caches translations. A page fault transfers control to the kernel and can represent allocation, copy-on-write, a missing page, or an invalid access. Some faults need disk I/O and others do not. Virtual address size, resident memory, and committed backing are distinct measures.

## Worked example

With toy 4 KiB pages, virtual address 8197 has page number 2 and offset 5. If that page maps to frame 10, the physical byte address is `10 * 4096 + 5 = 40965`. The mapping need not preserve neighboring virtual-page adjacency.

## Engineering implications

Locality affects page and TLB behavior as well as CPU caches. Mapping a large file does not mean all its bytes are resident. Excessive working sets can cause paging and unstable latency. Memory leaks, retained objects, page-cache growth, and address-space exhaustion need different explanations.

## Graph connections

- **requires:** [Operating Systems](operating-systems.md)
- **related_to:** [Memory Management and Ownership](memory-management.md), [Database Storage and Recovery](storage-and-recovery.md), [Performance Engineering](performance-engineering.md)
- **supported_by:** [Operating Systems Three Easy Pieces](../references/operating-systems-book.md)
