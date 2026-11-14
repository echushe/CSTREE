---
id: "distributed-systems"
type: "concept"
title: "Distributed Systems"
aliases: ["Partial failure", "Safety and liveness"]
domains: ["distributed-systems"]
branch: "distributed-systems"
---

# Distributed Systems

## What it is and why it matters

A distributed system coordinates independent processes through communication. Its defining difficulty is partial failure: one participant or connection can fail while others continue.

## Mechanism

State assumptions about nodes, messages, clocks, and failures. Messages may be delayed, lost, duplicated, or delivered after a retry depending on the protocol. A timeout is suspicion, not proof of failure. Safety constrains what may happen; liveness concerns eventual progress under stated conditions.

## Worked example

Two services update order and inventory independently. If inventory succeeds but the order service loses the reply, the combined outcome is uncertain. Coordination, idempotent retry, or an explicit compensation protocol is needed to reach a defined business result.

## Engineering implications

Choose guarantees for specific operations rather than declaring an entire system strongly or eventually consistent. Include recovery, rolling changes, overload, and network partitions in the design. Distribution is useful for scale and isolation but also creates coordination obligations.

## Graph connections

- **requires:** [Computer Networks](computer-networks.md), [Processes and Threads](processes-and-threads.md)
- **contains:** [Consistency Models and CAP](consistency-models.md), [Replication and Consensus](replication-and-consensus.md), [Partitioning and Sharding](partitioning-and-sharding.md), [Messaging and Event Streams](messaging-and-streams.md), [Caching](caching.md), [Time and Ordering](time-and-ordering.md), [Resilience and Idempotency](resilience-and-idempotency.md), [Distributed Transactions and Sagas](distributed-transactions.md)
- **related_to:** [Software Architecture](architecture.md), [Observability and Reliability](observability.md)
- **supported_by:** [Time, Clocks, and the Ordering of Events in a Distributed System](../papers/lamport-1978-time-clocks.md), [Site Reliability Engineering](../references/sre-book.md)
