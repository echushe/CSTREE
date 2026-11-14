---
id: "databases"
type: "concept"
title: "Databases"
aliases: ["DBMS", "Database systems"]
domains: ["databases"]
branch: "databases"
---

# Databases

## What it is and why it matters

A database manages durable shared data and a system for querying and changing it. Choosing one requires understanding the data model, access patterns, consistency needs, and operational constraints.

## Mechanism

A database combines a logical model, query execution, storage structures, concurrency control, and recovery. A client-facing schema is distinct from physical indexes and files. Transactions define which combinations of changes and observations are allowed under failure and concurrency.

## Worked example

An order consists of a header and several line items. A transaction can commit all rows together or none. An index on customer and creation time can accelerate order history without changing the logical meaning of an order.

## Engineering implications

Start with invariants and queries rather than a product category. Consider migrations, backup restoration, connection limits, and failure behavior alongside query speed. Relational and nonrelational systems overlap in capabilities; a label alone does not specify transaction or scaling guarantees.

## Graph connections

- **requires:** [Data Structures and Algorithms](data-structures-and-algorithms.md)
- **contains:** [The Relational Model and SQL](relational-model-and-sql.md), [Data Modeling and Schema Evolution](data-modeling.md), [Indexes and Query Planning](indexes-and-query-planning.md), [Transactions and Isolation](transactions.md), [Database Storage and Recovery](storage-and-recovery.md), [Nonrelational Data Models](nosql.md)
- **related_to:** [Distributed Systems](distributed-systems.md)
- **supported_by:** [PostgreSQL Database Documentation](../references/postgresql-documentation.md), [A Relational Model of Data for Large Shared Data Banks](../papers/codd-1970-relational-model.md)
