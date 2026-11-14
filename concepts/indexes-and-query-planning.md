---
id: "indexes-and-query-planning"
type: "concept"
title: "Indexes and Query Planning"
aliases: ["B-tree index", "Query optimizer", "EXPLAIN", "Execution plan"]
domains: ["databases"]
branch: "databases"
---

# Indexes and Query Planning

## What it is and why it matters

Indexes trade storage and update work for faster access. A query planner chooses an execution plan using statistics and a cost model.

## Mechanism

B-tree indexes support ordered lookups and ranges; other structures serve different operators and data. Composite index order affects useful access paths. Planners choose scans, join orders, and join algorithms. Estimated cardinalities influence choices; `EXPLAIN` shows the plan, while an execution analysis adds actual observations.

## Worked example

For `WHERE customer_id = 7 ORDER BY created_at DESC LIMIT 20`, an index beginning with `(customer_id, created_at)` may locate the customer's rows in useful order. An index starting with an unrelated field may not provide that access path. Actual usefulness depends on the engine, statistics, and selectivity.

## Engineering implications

Inspect representative plans and row counts. More indexes increase write work and storage. An index does not guarantee use or eliminate table access. Execution analysis can run a modifying statement, so understand its effects before using it on live data. Keep predicates and data types aligned with usable index operators.

## Graph connections

- **requires:** [Trees and Search Trees](trees.md), [The Relational Model and SQL](relational-model-and-sql.md), [Algorithm Analysis](algorithm-analysis.md)
- **uses:** [Sorting Algorithms](sorting.md), [Hash Tables](hash-tables.md)
- **related_to:** [Performance Engineering](performance-engineering.md), [Database Storage and Recovery](storage-and-recovery.md)
- **supported_by:** [PostgreSQL Database Documentation](../references/postgresql-documentation.md)
