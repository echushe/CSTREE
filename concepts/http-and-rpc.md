---
id: "http-and-rpc"
type: "concept"
title: "HTTP and Remote Procedure Calls"
aliases: ["HTTP", "RPC", "REST", "gRPC"]
domains: ["distributed-systems"]
branch: "distributed-systems"
---

# HTTP and Remote Procedure Calls

## What it is and why it matters

HTTP defines request and response semantics; RPC presents remote operations through a service interface. A remote call introduces latency, serialization, and uncertainty absent from a simple local function call.

## Mechanism

HTTP methods, status codes, headers, and representations carry meaning beyond the body format. Safe methods are intended to be read-only; idempotent methods have the same intended server effect when repeated. RPC frameworks add schemas, generated clients, and transport conventions, but application error and retry semantics still need design.

## Worked example

A client times out after submitting an order. The server may have committed it before the reply was lost. Repeating a POST without an application idempotency mechanism can create another order. An error at the client is not proof of no server-side effect.

## Engineering implications

Propagate deadlines, bound payloads, and distinguish transport failures from application rejection. HTTP idempotency concerns intended effects, not identical responses or absence of logs. Design pagination, versioning, authentication, and retry behavior as part of the API contract.

## Graph connections

- **requires:** [Computer Networks](computer-networks.md), [API Design and Contracts](api-design.md)
- **related_to:** [Resilience and Idempotency](resilience-and-idempotency.md), [Security Engineering](security-engineering.md), [Observability and Reliability](observability.md)
- **supported_by:** [HTTP and Transport Specifications](../references/http-semantics.md)
