---
id: "relational-model-and-sql"
type: "concept"
title: "The Relational Model and SQL"
aliases: ["SQL", "Relational algebra", "Joins", "Keys"]
domains: ["databases"]
branch: "databases"
---

# The Relational Model and SQL

## What it is and why it matters

The relational model describes data through relations and operations on them. SQL is a practical language for defining, querying, and updating relational data, with semantics that differ from pure set algebra.

## Mechanism

Selection filters tuples; projection chooses attributes; joins combine matching tuples. Keys identify rows and foreign keys constrain references. SQL commonly uses bag semantics, supports NULL, and requires an explicit `ORDER BY` when result order matters. NULL introduces three-valued logic in predicates.

## Worked example

Given customers `(1,Ada), (2,Lin)` and orders `(10,1), (11,1)`, an inner join on customer ID produces two rows for Ada and none for Lin. A left join preserves Lin with NULL order fields. `COUNT(*)` and `COUNT(order_id)` then count different things.

## Engineering implications

Use parameterized queries for values. Specify keys and constraints in the database when they protect shared invariants. Watch duplicate multiplication in joins and `NULL` comparisons: `x = NULL` is not the test for nullness. Treat query results as unordered unless ordering is requested.

## Graph connections

- **requires:** [Discrete Mathematics for Software](discrete-mathematics.md)
- **related_to:** [Data Modeling and Schema Evolution](data-modeling.md), [Indexes and Query Planning](indexes-and-query-planning.md), [Transactions and Isolation](transactions.md)
- **supported_by:** [A Relational Model of Data for Large Shared Data Banks](../papers/codd-1970-relational-model.md), [PostgreSQL Database Documentation](../references/postgresql-documentation.md)
