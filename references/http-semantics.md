---
id: "http-semantics"
type: "reference"
title: "HTTP and Transport Specifications"
authors: ["IETF HTTP Working Group", "IETF TCP Maintenance and Minor Extensions Working Group"]
kind: "specification"
accessed: "2026-11-10"
---

# HTTP and Transport Specifications

## Primary sources

- [RFC 9110 HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [RFC 9111 HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111)
- [RFC 9293 Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293)

## Contribution and scope

RFC 9110 defines HTTP method and response semantics, RFC 9111 defines HTTP caching, and RFC 9293 specifies TCP. These separate application semantics from a transport byte stream. They do not specify every RPC framework or the business meaning of an idempotency key.

## Reading route

Read HTTP safe and idempotent method definitions together with retry behavior. Then compare a framed application protocol with TCP stream delivery. Return to the caching specification when implementing HTTP cache-control or validation.

## Graph connections

- **explains:** [Computer Networks](../concepts/computer-networks.md), [HTTP and Remote Procedure Calls](../concepts/http-and-rpc.md), [API Design and Contracts](../concepts/api-design.md), [Caching](../concepts/caching.md), [Resilience and Idempotency](../concepts/resilience-and-idempotency.md)
