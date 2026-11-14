---
id: "time-and-ordering"
type: "concept"
title: "Time and Ordering"
aliases: ["Lamport clock", "Vector clock", "Happens-before", "Logical clocks"]
domains: ["distributed-systems"]
branch: "distributed-systems"
---

# Time and Ordering

## What it is and why it matters

Distributed systems need to reason about event order without assuming every machine shares a perfect clock. Physical time, causal order, and a chosen total order solve different problems.

## Mechanism

Happens-before includes process-local order and send-before-receive, closed transitively. Lamport clocks increment locally and merge received timestamps with a maximum plus one. If a happens before b, then L(a) < L(b); the converse is false. Vector clocks can express causal relationships under their participant model. Monotonic clocks measure local durations.

## Worked example

Process A sends a message stamped 3. B has local clock 5, receives it, and sets its clock to `max(5,3)+1 = 6`. A concurrent event on C could also have timestamp 6. A process-ID tie-breaker can make a total order without proving the events were causally related.

## Engineering implications

Avoid using wall-clock order alone to prove causality. Clock correction can affect timestamps; use suitable monotonic duration APIs for local deadlines. Distributed leases require explicit timing assumptions. Define how conflict resolution uses timestamps and what happens when clocks disagree.

## Graph connections

- **requires:** [Distributed Systems](distributed-systems.md), [Discrete Mathematics for Software](discrete-mathematics.md)
- **related_to:** [Consistency Models and CAP](consistency-models.md), [Replication and Consensus](replication-and-consensus.md)
- **supported_by:** [Time, Clocks, and the Ordering of Events in a Distributed System](../papers/lamport-1978-time-clocks.md)
