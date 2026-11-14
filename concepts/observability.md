---
id: "observability"
type: "concept"
title: "Observability and Reliability"
aliases: ["Logs", "Metrics", "Tracing", "SLI", "SLO", "Error budget"]
domains: ["engineering"]
branch: "engineering"
---

# Observability and Reliability

## What it is and why it matters

Observability provides evidence for understanding system behavior from its outputs. Reliability connects that evidence to user-visible service expectations and recovery practices.

## Mechanism

Metrics aggregate measurements; logs record events; traces connect spans across a request. Service-level indicators measure behavior, while objectives set desired levels over a window. Error budgets connect allowed unreliability to operational choices. Correlation IDs and careful dimensions help join evidence without uncontrolled cardinality.

## Worked example

A 99.9% successful-request objective over one million eligible requests permits 1,000 failures under that definition. Counting only requests reaching one healthy server can hide failed requests upstream, so the measurement boundary matters.

## Engineering implications

Measure user-visible success and latency, then instrument dependencies and saturation for diagnosis. Percentiles cannot generally be averaged to obtain a global percentile. Avoid secrets and sensitive payloads in telemetry. Alert on actionable symptoms and practice incident response and restoration.

## Graph connections

- **requires:** [Requirements and Specifications](requirements-and-specifications.md)
- **related_to:** [Distributed Systems](distributed-systems.md), [Debugging and Profiling](debugging-and-profiling.md), [Continuous Integration and Delivery](ci-cd.md), [Performance Engineering](performance-engineering.md)
- **supported_by:** [Site Reliability Engineering](../references/sre-book.md)
