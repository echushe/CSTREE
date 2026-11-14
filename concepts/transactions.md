---
id: "transactions"
type: "concept"
title: "Transactions and Isolation"
aliases: ["ACID", "MVCC", "Isolation", "Serializability", "Write skew"]
domains: ["databases"]
branch: "databases"
---

# Transactions and Isolation

## What it is and why it matters

A transaction groups operations into a unit with defined failure and concurrency semantics. ACID names atomicity, consistency, isolation, and durability, but the actual guarantees need precise interpretation.

## Mechanism

Atomicity concerns all-or-nothing effects; durability concerns committed data surviving the promised failures. Consistency relies on declared constraints and correct transaction logic. Isolation controls allowed observations between transactions. Serializable execution is equivalent to some serial order; it does not by itself require real-time ordering. MVCC and locking are implementation techniques, not isolation levels.

## Worked example

Two on-call doctors each observe that the other is available, then each marks themselves unavailable. Snapshot-style isolation can allow both transactions and violate the at-least-one-doctor rule. Serializable handling can reject one transaction, requiring a retry of the whole decision.

## Engineering implications

State invariants and test concurrent histories. Defaults and similarly named isolation levels vary across engines. Handle deadlocks and serialization failures by retrying with a bounded policy. A database transaction does not automatically include an external payment or message publication.

## Graph connections

- **requires:** [The Relational Model and SQL](relational-model-and-sql.md)
- **related_to:** [Synchronization and Concurrency Control](synchronization.md), [Consistency Models and CAP](consistency-models.md), [Distributed Transactions and Sagas](distributed-transactions.md), [Database Storage and Recovery](storage-and-recovery.md)
- **supported_by:** [PostgreSQL Database Documentation](../references/postgresql-documentation.md)
