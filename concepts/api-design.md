---
id: "api-design"
type: "concept"
title: "API Design and Contracts"
aliases: ["API contract", "Schema evolution", "Compatibility"]
domains: ["design"]
branch: "design"
---

# API Design and Contracts

## What it is and why it matters

An API specifies how a client requests behavior and what it may rely on. This applies to functions, libraries, services, and event schemas.

## Mechanism

Define inputs, outputs, invariants, errors, authorization, ownership, and compatibility. For remote APIs add timeouts, pagination, idempotency, and retry semantics. Separate transport representation from domain rules. Compatibility includes meaning as well as field names and types.

## Worked example

A paginated list API returns items and a continuation token. If concurrent inserts shift numbered pages, a client can miss or duplicate items. A cursor with a defined ordering and snapshot policy makes the contract clearer, but still needs explicit consistency semantics.

## Engineering implications

Validate at trust boundaries and avoid exposing internal storage details unnecessarily. Define how unknown fields, old clients, and repeated requests behave. A schema alone does not capture business invariants. Contract tests can check representative interactions across versions.

## Graph connections

- **requires:** [Type Systems](type-systems.md), [Software Design Principles](software-design.md)
- **related_to:** [HTTP and Remote Procedure Calls](http-and-rpc.md), [Software Testing](testing.md), [Resilience and Idempotency](resilience-and-idempotency.md), [Security Engineering](security-engineering.md)
- **supported_by:** [HTTP and Transport Specifications](../references/http-semantics.md), [Software Engineering and Git Guides](../references/software-construction.md)
