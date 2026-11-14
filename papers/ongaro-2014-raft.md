---
id: "ongaro-2014-raft"
type: "paper"
title: "In Search of an Understandable Consensus Algorithm"
authors: ["Diego Ongaro", "John Ousterhout"]
year: 2014
venue: "USENIX Annual Technical Conference"
selection: "replicated-log-consensus-milestone"
---

# In Search of an Understandable Consensus Algorithm

## Primary sources

- [Author-hosted extended paper](https://raft.github.io/raft.pdf)
- [Raft authors project](https://raft.github.io/)

## Contribution and scope

Raft decomposes replicated-log consensus into election, replication, and safety. The linked text is the extended version associated with the 2014 USENIX ATC paper. Its failure model is not Byzantine, and its liveness depends on suitable communication and timing conditions.

## Reading route

Trace election terms and one log replication before studying leader changes. Explain why a majority is necessary but not sufficient without the log and commitment rules. Then examine membership and snapshots.

## Graph connections

- **explains:** [Replication and Consensus](../concepts/replication-and-consensus.md)
