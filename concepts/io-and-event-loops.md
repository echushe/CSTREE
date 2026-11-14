---
id: "io-and-event-loops"
type: "concept"
title: "I/O and Event Loops"
aliases: ["Async I/O", "Event loop", "Nonblocking I/O", "Futures"]
domains: ["operating-systems"]
branch: "operating-systems"
---

# I/O and Event Loops

## What it is and why it matters

I/O models determine how a program waits for external work without wasting execution resources. Event loops coordinate many in-flight operations with relatively few threads.

## Mechanism

Blocking I/O waits in the calling execution context. Nonblocking I/O returns when it cannot proceed. Readiness notification says an operation may make progress; completion notification reports a completed operation. Async functions and futures expose suspension and resumption above these mechanisms.

## Worked example

A server starts a network request, suspends its handler, and processes another request. When bytes arrive, the first handler resumes. A CPU-heavy loop that never yields on the event-loop thread delays both handlers even though the network operations are asynchronous.

## Engineering implications

Track cancellation, timeouts, bounded concurrency, and resource cleanup. Async execution does not eliminate shared-state races or imply parallel CPU execution. Apply backpressure so outstanding operations cannot grow without bound. Separate file, network, and CPU behavior when interpreting a runtime's async APIs.

## Graph connections

- **requires:** [Processes and Threads](processes-and-threads.md), [Queues and Deques](queues.md)
- **related_to:** [JavaScript](javascript.md), [C#](csharp.md), [Computer Networks](computer-networks.md), [Resilience and Idempotency](resilience-and-idempotency.md)
- **supported_by:** [Operating Systems Three Easy Pieces](../references/operating-systems-book.md), [Language Specifications and Official Guides](../references/language-specifications.md)
