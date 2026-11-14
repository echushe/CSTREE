---
id: "lamport-1978-time-clocks"
type: "paper"
title: "Time, Clocks, and the Ordering of Events in a Distributed System"
authors: ["Leslie Lamport"]
year: 1978
venue: "Communications of the ACM"
selection: "distributed-ordering-foundation"
---

# Time, Clocks, and the Ordering of Events in a Distributed System

## Primary sources

- [Author-hosted paper](https://lamport.azurewebsites.net/pubs/time-clocks.pdf)

## Contribution and scope

Defines happens-before and logical clocks for ordering distributed events. A total order can extend the partial causal order, but a scalar timestamp comparison does not prove causality. The paper provides a foundation for protocol reasoning rather than clock synchronization accuracy guarantees.

## Reading route

Draw two process timelines, add sends and receives, and compute logical timestamps by hand. Identify concurrent events before considering the constructed total order.

## Graph connections

- **explains:** [Time and Ordering](../concepts/time-and-ordering.md), [Distributed Systems](../concepts/distributed-systems.md), [Formal Methods and Verification](../concepts/formal-methods.md)
