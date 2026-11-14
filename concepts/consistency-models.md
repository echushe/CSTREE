---
id: "consistency-models"
type: "concept"
title: "Consistency Models and CAP"
aliases: ["Linearizability", "Eventual consistency", "Causal consistency", "CAP"]
domains: ["distributed-systems"]
branch: "distributed-systems"
---

# Consistency Models and CAP

## What it is and why it matters

A consistency model specifies which observations are valid across operations and replicas. Name the model and operation scope rather than using consistency as a single yes-or-no property.

## Mechanism

Linearizability makes each operation appear to occur at one point between invocation and response, respecting real-time order. Serializability orders transactions without necessarily respecting real time. Causal consistency preserves causal relationships. Eventual consistency needs convergence conditions and does not alone provide a freshness bound. CAP concerns the impossibility of guaranteeing both atomic consistency and availability under partitions in its model.

## Worked example

After a completed write of x=1, a later linearizable read cannot return x=0. An eventually consistent replica might temporarily return 0. If a partition prevents coordination, a service preserving linearizability may have to withhold some responses instead of returning stale data as successful reads.

## Engineering implications

CAP is not a general instruction to pick any two features; partition tolerance describes the failure setting. Define session guarantees, staleness, and cross-key behavior separately. ACID consistency is about preserving application constraints, a different use of the same word.

## Graph connections

- **requires:** [Distributed Systems](distributed-systems.md), [Transactions and Isolation](transactions.md)
- **related_to:** [Time and Ordering](time-and-ordering.md), [Replication and Consensus](replication-and-consensus.md), [Caching](caching.md)
- **supported_by:** [Perspectives on the CAP Theorem](../papers/gilbert-lynch-2012-cap-perspectives.md), [PostgreSQL Database Documentation](../references/postgresql-documentation.md)
