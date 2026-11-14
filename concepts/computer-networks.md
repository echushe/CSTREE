---
id: "computer-networks"
type: "concept"
title: "Computer Networks"
aliases: ["TCP", "UDP", "IP", "DNS", "TLS"]
domains: ["distributed-systems"]
branch: "distributed-systems"
---

# Computer Networks

## What it is and why it matters

Networking connects programs across machines through layered protocols. Applications must account for latency, finite bandwidth, loss, and failures that cannot be observed directly.

## Mechanism

IP routes packets; TCP provides a reliable ordered byte stream between endpoints; UDP provides datagrams without that delivery guarantee. DNS resolves names through its own distributed system. TLS protects a channel under its trust and configuration assumptions. Application framing is still required over a byte stream.

## Worked example

Sending `hello` and then `world` over TCP does not guarantee two receive calls. A receiver may observe `helloworld` together or partial chunks. A length prefix or another framing protocol tells it where application messages begin and end.

## Engineering implications

Distinguish connection setup, name resolution, transport, encryption, and application work when diagnosing delay. Reliable transport does not prove that a remote business operation committed. Set deadlines and limits for buffers, message sizes, and concurrency.

## Graph connections

- **requires:** [Processes and Threads](processes-and-threads.md)
- **related_to:** [HTTP and Remote Procedure Calls](http-and-rpc.md), [Distributed Systems](distributed-systems.md), [I/O and Event Loops](io-and-event-loops.md), [Security Engineering](security-engineering.md)
- **supported_by:** [HTTP and Transport Specifications](../references/http-semantics.md)
