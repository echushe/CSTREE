---
id: "storage-and-recovery"
type: "concept"
title: "Database Storage and Recovery"
aliases: ["WAL", "Write-ahead log", "LSM tree", "Recovery", "Buffer pool"]
domains: ["databases"]
branch: "databases"
---

# Database Storage and Recovery

## What it is and why it matters

Storage engines map logical data onto pages, indexes, and logs. Recovery restores a valid state after interruption, while backups address failures that the live system cannot repair by itself.

## Mechanism

A buffer pool caches pages. Write-ahead logging requires relevant log records to reach durable storage before corresponding changed data pages are written. Recovery can replay logged changes; exact undo and redo rules depend on the engine. Checkpoints limit recovery work. LSM-based engines organize writes through logs, memory tables, and compaction.

## Worked example

A committed change has durable WAL but its data page is still only in memory. After a crash, replay can restore that page's change from the log. If both the data volume and its only log copy are lost, replay alone cannot recover the database.

## Engineering implications

Match durability settings to the failure model. Replication, backup, and point-in-time recovery address different problems. Test restoration rather than only backup creation. Compaction, checkpoints, and cache misses can change latency. Do not assume a successful application write means every storage layer has persisted it.

## Graph connections

- **requires:** [Databases](databases.md), [Arrays and Linked Lists](arrays-and-linked-lists.md)
- **related_to:** [File Systems and Persistence](file-systems.md), [Virtual Memory](virtual-memory.md), [Replication and Consensus](replication-and-consensus.md), [Transactions and Isolation](transactions.md)
- **supported_by:** [PostgreSQL Database Documentation](../references/postgresql-documentation.md), [Operating Systems Three Easy Pieces](../references/operating-systems-book.md)
