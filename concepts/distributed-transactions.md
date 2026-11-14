---
id: "distributed-transactions"
type: "concept"
title: "Distributed Transactions and Sagas"
aliases: ["2PC", "Two-phase commit", "Saga", "Transactional outbox"]
domains: ["distributed-systems"]
branch: "distributed-systems"
---

# Distributed Transactions and Sagas

## What it is and why it matters

Distributed transactions coordinate changes across participants. A saga instead arranges local transactions and compensating business actions when one atomic commit boundary is unavailable or undesirable.

## Mechanism

Two-phase commit asks participants to prepare, then records and distributes a commit or abort decision. Prepared participants can block while the decision is unavailable. Consensus can strengthen decision durability but does not turn atomic commitment into the same problem. A transactional outbox stores a publication intent with local data, then delivers it separately with deduplication.

## Worked example

An order transaction writes the order and an outbox row together. A relay publishes the row, then marks it delivered. A crash after publication but before marking can publish twice, so the consumer needs duplicate handling. A saga might reserve stock, charge payment, and compensate a failed workflow by releasing stock or issuing a refund.

## Engineering implications

Compensation is a new action, not erasure of history or perfect rollback. Define intermediate visible states, reconciliation, and manual recovery. Outbox delivery is not automatically exactly once. Choose a protocol around required invariants and participant capabilities.

## Graph connections

- **requires:** [Transactions and Isolation](transactions.md), [Distributed Systems](distributed-systems.md), [Messaging and Event Streams](messaging-and-streams.md)
- **related_to:** [Replication and Consensus](replication-and-consensus.md), [Resilience and Idempotency](resilience-and-idempotency.md), [Software Architecture](architecture.md)
- **supported_by:** [PostgreSQL Database Documentation](../references/postgresql-documentation.md), [Site Reliability Engineering](../references/sre-book.md)
