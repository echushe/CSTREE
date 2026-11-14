---
id: "architecture"
type: "concept"
title: "Software Architecture"
aliases: ["Modular monolith", "Microservices", "Ports and adapters", "ADR"]
domains: ["design"]
branch: "design"
---

# Software Architecture

## What it is and why it matters

Architecture establishes major boundaries, data ownership, communication, and deployment choices. Its value comes from meeting concrete quality requirements rather than adopting a fashionable shape.

## Mechanism

Layered and ports-and-adapters designs control dependencies. A modular monolith deploys together while preserving internal boundaries. Microservices separate deployments and often data ownership, introducing network and operational concerns. Event-driven designs decouple producers from consumers while making time and delivery semantics explicit.

## Worked example

An order application can keep catalog, checkout, and fulfillment in separate modules within one deployment. Extracting fulfillment as a service requires an API or event contract, independent failure handling, and a policy for order state when fulfillment is unavailable.

## Engineering implications

Write down latency, availability, security, and change constraints before comparing alternatives. Architecture decision records capture a decision, context, and consequences. Distribution adds partial failures and coordination cost; boundaries inside one process remain useful. Validate important assumptions with a small implementation or measurement.

## Graph connections

- **requires:** [Software Design Principles](software-design.md)
- **related_to:** [Distributed Systems](distributed-systems.md), [Data Modeling and Schema Evolution](data-modeling.md), [Observability and Reliability](observability.md), [Security Engineering](security-engineering.md)
- **supported_by:** [Software Engineering and Git Guides](../references/software-construction.md), [Site Reliability Engineering](../references/sre-book.md)
