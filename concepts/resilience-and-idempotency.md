---
id: "resilience-and-idempotency"
type: "concept"
title: "Resilience and Idempotency"
aliases: ["Retries", "Backpressure", "Circuit breaker", "Idempotency key", "Timeouts"]
domains: ["distributed-systems"]
branch: "distributed-systems"
---

# Resilience and Idempotency

## What it is and why it matters

Resilience keeps a service within defined behavior when dependencies slow down, fail, or overload. Idempotency makes deliberate retries compatible with one intended business effect.

## Mechanism

Use end-to-end deadlines, bounded retries, exponential backoff with jitter, concurrency limits, and load shedding where appropriate. Circuit breakers can stop repeated calls to a failing dependency. An idempotency key must bind to a request meaning and atomically coordinate effect and recorded outcome within a defined scope.

## Worked example

A client retries payment request key K after losing the reply. The server finds the prior completed result for K and returns it. If it instead performs the payment before separately recording K, a crash between those actions leaves a duplicate-effect window.

## Engineering implications

Retry only failures and operations whose semantics support retry. Layered retries multiply traffic: three attempts at each of three layers can yield 27 deepest calls. Define key retention, concurrent duplicate behavior, cancellation, and incompatible reuse of the same key.

## Graph connections

- **requires:** [Distributed Systems](distributed-systems.md), [Queues and Deques](queues.md)
- **related_to:** [HTTP and Remote Procedure Calls](http-and-rpc.md), [Transactions and Isolation](transactions.md), [Messaging and Event Streams](messaging-and-streams.md), [Observability and Reliability](observability.md)
- **supported_by:** [Site Reliability Engineering](../references/sre-book.md), [HTTP and Transport Specifications](../references/http-semantics.md)
