---
id: "partitioning-and-sharding"
type: "concept"
title: "Partitioning and Sharding"
aliases: ["Sharding", "Partition key", "Consistent hashing", "Hot partitions"]
domains: ["distributed-systems"]
branch: "distributed-systems"
---

# Partitioning and Sharding

## What it is and why it matters

Partitioning divides a dataset or workload; sharding distributes such partitions across nodes. It addresses capacity and locality separately from replication.

## Mechanism

Range partitioning preserves key locality but can create hot ranges. Hash partitioning spreads keys but complicates range scans. Consistent or rendezvous hashing can reduce remapping when membership changes. A partition key determines which operations are local and which require scatter, coordination, or duplicated data.

## Worked example

Sharding orders by customer keeps each customer's history local. A global query by product may need every shard. A single unusually busy customer can still overload one partition even when the total number of customers is evenly distributed.

## Engineering implications

Plan rebalancing, skew, cross-shard operations, and routing changes. Adding shards does not solve a hot key or a shared bottleneck automatically. Replicas of one shard improve redundancy; they are not additional disjoint partitions. Track per-partition metrics instead of only fleet averages.

## Graph connections

- **requires:** [Distributed Systems](distributed-systems.md), [Hash Tables](hash-tables.md), [Data Modeling and Schema Evolution](data-modeling.md)
- **related_to:** [Replication and Consensus](replication-and-consensus.md), [Indexes and Query Planning](indexes-and-query-planning.md), [Performance Engineering](performance-engineering.md)
- **supported_by:** [Site Reliability Engineering](../references/sre-book.md), [Perspectives on the CAP Theorem](../papers/gilbert-lynch-2012-cap-perspectives.md)
