---
id: "caching"
type: "concept"
title: "Caching"
aliases: ["Cache invalidation", "TTL", "LRU", "Cache stampede"]
domains: ["distributed-systems"]
branch: "distributed-systems"
---

# Caching

## What it is and why it matters

A cache stores reusable results closer to a consumer. It improves some accesses at the cost of memory, invalidation complexity, and potentially stale observations.

## Mechanism

Cache-aside checks a cache then loads a miss from the source. Write-through and write-behind move different work onto the write path. Eviction controls space; expiration controls a time-based reuse policy. Neither alone guarantees consistency. Keys must include every input that affects the result, including authorization scope when relevant.

## Worked example

If hits take 1 ms, misses 20 ms, and the hit rate is 90%, a simple serial model gives average lookup latency `0.9*1 + 0.1*20 = 2.9 ms`. Tail latency and concurrent misses can still be much worse. Many requests missing together can overload the source.

## Engineering implications

Bound size, define stale-data tolerance, and handle stampedes with appropriate request coalescing or refresh control. Invalidation can race with writes. Do not cache private data under a key shared across users. Measure hit rate together with source load and end-to-end latency.

## Graph connections

- **requires:** [Hash Tables](hash-tables.md), [Distributed Systems](distributed-systems.md)
- **related_to:** [Consistency Models and CAP](consistency-models.md), [HTTP and Remote Procedure Calls](http-and-rpc.md), [Performance Engineering](performance-engineering.md)
- **supported_by:** [Site Reliability Engineering](../references/sre-book.md), [HTTP and Transport Specifications](../references/http-semantics.md)
