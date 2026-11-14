---
id: "codd-1970-relational-model"
type: "paper"
title: "A Relational Model of Data for Large Shared Data Banks"
authors: ["E. F. Codd"]
year: 1970
venue: "Communications of the ACM"
selection: "relational-model-foundation"
---

# A Relational Model of Data for Large Shared Data Banks

## Primary sources

- [IBM Research publication record](https://research.ibm.com/publications/a-relational-model-of-data-for-large-shared-data-banks)

## Contribution and scope

A foundational relational-model paper that separates logical data from physical representation. It discusses relations, operations, and redundancy. Modern SQL adds behavior such as bags and NULL that should not be silently equated with the pure relational model.

## Reading route

Start with relations, keys, joins, and one update anomaly. Read the paper for data independence and logical representation, then compare those ideas with a concrete SQL engine.

## Graph connections

- **explains:** [The Relational Model and SQL](../concepts/relational-model-and-sql.md), [Data Modeling and Schema Evolution](../concepts/data-modeling.md), [Databases](../concepts/databases.md)
