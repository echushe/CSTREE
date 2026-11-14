---
id: "performance-engineering"
type: "concept"
title: "Performance Engineering"
aliases: ["Benchmarking", "Little's law", "Amdahl's law", "Latency", "Throughput"]
domains: ["engineering"]
branch: "engineering"
---

# Performance Engineering

## What it is and why it matters

Performance engineering connects resource use to user-facing goals under a defined workload. It uses models and measurements to locate the limiting factor before changing code.

## Mechanism

Specify throughput, latency distribution, capacity, and resource limits. In a stable system, Little's law gives average in-flight work `L = lambda * W`, using consistent units and boundaries. Amdahl's law bounds the benefit of accelerating only part of a workload. Queueing and contention often dominate near saturation.

## Worked example

At 100 requests per second and 0.2 seconds average residence time, the average in-flight count is 20. If residence time rises to 2 seconds at the same arrival rate, it becomes 200. A larger concurrency limit alone does not remove the underlying bottleneck.

## Engineering implications

Measure realistic data, warmup, error rates, and tail latency. Distinguish microbenchmark gains from end-to-end impact. Control load generation so a slowing service does not accidentally reduce offered load and hide overload. Change algorithms, access patterns, or coordination when measurements justify it.

## Graph connections

- **requires:** [Algorithm Analysis](algorithm-analysis.md), [Requirements and Specifications](requirements-and-specifications.md)
- **related_to:** [Debugging and Profiling](debugging-and-profiling.md), [Observability and Reliability](observability.md), [Caching](caching.md), [Indexes and Query Planning](indexes-and-query-planning.md)
- **supported_by:** [Site Reliability Engineering](../references/sre-book.md), [Introduction to Algorithms](../references/algorithms-reference.md)
