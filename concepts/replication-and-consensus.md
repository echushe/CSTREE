---
id: "replication-and-consensus"
type: "concept"
title: "Replication and Consensus"
aliases: ["Raft", "Paxos", "Quorums", "Replicated state machine"]
domains: ["distributed-systems"]
branch: "distributed-systems"
---

# Replication and Consensus

## What it is and why it matters

Replication maintains copies of data or computation. Consensus coordinates agreement, often on an ordered log used by a replicated state machine.

## Mechanism

Leader-based replication orders changes through a leader; asynchronous followers can lag. Raft separates leader election, log replication, and safety rules. Majority quorums overlap, but correctness also depends on terms, log matching, and commitment rules. Consensus safety can survive delays; progress depends on communication and timing conditions.

## Worked example

In a five-node Raft cluster, a majority is three. If two nodes are unavailable, the remaining three can potentially elect and make progress when communication and timing permit. A two-node minority cannot commit new entries merely by choosing its own leader.

## Engineering implications

Consensus is not Byzantine fault tolerance unless the protocol says so. Read consistency, membership changes, snapshots, and recovery need explicit treatment. Majority arithmetic alone is not a complete protocol. Replication does not protect against every accidental deletion or replace independent backups.

## Graph connections

- **requires:** [Distributed Systems](distributed-systems.md), [Time and Ordering](time-and-ordering.md)
- **related_to:** [Consistency Models and CAP](consistency-models.md), [Database Storage and Recovery](storage-and-recovery.md), [Distributed Transactions and Sagas](distributed-transactions.md)
- **supported_by:** [In Search of an Understandable Consensus Algorithm](../papers/ongaro-2014-raft.md)
