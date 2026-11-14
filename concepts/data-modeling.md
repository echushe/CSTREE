---
id: "data-modeling"
type: "concept"
title: "Data Modeling and Schema Evolution"
aliases: ["Normalization", "Schema migration", "Domain modeling"]
domains: ["databases"]
branch: "databases"
---

# Data Modeling and Schema Evolution

## What it is and why it matters

Data modeling turns domain facts and invariants into stored structures. Schema evolution changes those structures while keeping existing data and clients usable.

## Mechanism

Identify entities, keys, relationships, cardinality, and constraints. Functional dependencies guide normalization and expose update anomalies. Denormalization stores redundant facts to support specific reads and creates a synchronization obligation. Migrations need a sequence compatible with running application versions.

## Worked example

Storing a customer address on every order may be deliberate: an order often needs the shipping address used at purchase, not the customer's latest address. Separating current customer details from an immutable order snapshot preserves both meanings.

## Engineering implications

Name the fact being stored and its time semantics. For a required new field, first add a compatible nullable field, deploy writers, backfill with a defined rule, then enforce the constraint when readers and data are ready. Backfills need batching, observability, and a restart policy.

## Graph connections

- **requires:** [The Relational Model and SQL](relational-model-and-sql.md)
- **related_to:** [API Design and Contracts](api-design.md), [Software Architecture](architecture.md), [Transactions and Isolation](transactions.md)
- **supported_by:** [A Relational Model of Data for Large Shared Data Banks](../papers/codd-1970-relational-model.md), [PostgreSQL Database Documentation](../references/postgresql-documentation.md)
