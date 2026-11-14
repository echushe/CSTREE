---
id: "gilbert-lynch-2012-cap-perspectives"
type: "paper"
title: "Perspectives on the CAP Theorem"
authors: ["Seth Gilbert", "Nancy A. Lynch"]
year: 2012
venue: "Computer, IEEE"
selection: "cap-theorem-clarification"
---

# Perspectives on the CAP Theorem

## Primary sources

- [Author-hosted review](https://groups.csail.mit.edu/tds/papers/Gilbert/Brewer2.pdf)

## Contribution and scope

Reviews CAP, its formal setting, and practical implications. It is a 2012 perspective on the authors' earlier 2002 formalization, not the original theorem paper. It clarifies atomic consistency, availability, and unreliable communication; it is not a general product classification scheme.

## Reading route

Describe a partitioned read/write register and why both sides cannot always provide the latest value without communication. Keep formal availability separate from a production latency objective and compare weaker consistency requirements.

## Graph connections

- **explains:** [Consistency Models and CAP](../concepts/consistency-models.md), [Nonrelational Data Models](../concepts/nosql.md), [Partitioning and Sharding](../concepts/partitioning-and-sharding.md)
