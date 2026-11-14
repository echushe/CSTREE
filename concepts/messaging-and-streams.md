---
id: "messaging-and-streams"
type: "concept"
title: "Messaging and Event Streams"
aliases: ["Message queue", "Event streaming", "Pub/sub", "Delivery semantics"]
domains: ["distributed-systems"]
branch: "distributed-systems"
---

# Messaging and Event Streams

## What it is and why it matters

Messaging separates the time and location of producing work from consuming it. Queues often distribute tasks; retained logs support replay and independent consumer positions.

## Mechanism

Delivery guarantees depend on acknowledgment, persistence, retries, and consumer effects. At-most-once can lose work; at-least-once can redeliver. Exactly-once claims need a defined scope and transactional boundary. Ordering is commonly per partition or key rather than global. Backpressure and lag describe whether consumers can keep up.

## Worked example

A consumer updates a database, then crashes before acknowledging the message. The broker delivers it again. Recording a unique event ID in the same transaction as the effect can prevent applying that database change twice, with an explicit deduplication retention policy.

## Engineering implications

Define schema evolution, poison-message handling, retry delay, and replay safety. Avoid assuming a broker acknowledgment proves an external business effect. Decide who owns event meaning and whether an event states a fact or requests an action. Capacity planning must include retained backlog and recovery throughput.

## Graph connections

- **requires:** [Distributed Systems](distributed-systems.md), [Queues and Deques](queues.md)
- **related_to:** [Behavioral Design Patterns](behavioral-patterns.md), [Resilience and Idempotency](resilience-and-idempotency.md), [Distributed Transactions and Sagas](distributed-transactions.md), [Observability and Reliability](observability.md)
- **supported_by:** [Site Reliability Engineering](../references/sre-book.md)
