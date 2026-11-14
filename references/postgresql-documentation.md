---
id: "postgresql-documentation"
type: "reference"
title: "PostgreSQL Database Documentation"
authors: ["The PostgreSQL Global Development Group"]
kind: "documentation"
accessed: "2026-11-10"
---

# PostgreSQL Database Documentation

## Primary sources

- [PostgreSQL 18 manual](https://www.postgresql.org/docs/18/index.html)
- [SQL tutorial](https://www.postgresql.org/docs/18/tutorial-sql.html)
- [Transaction isolation](https://www.postgresql.org/docs/18/transaction-iso.html)
- [Indexes](https://www.postgresql.org/docs/18/indexes.html)
- [Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
- [Write-ahead logging](https://www.postgresql.org/docs/18/wal-intro.html)
- [Two-phase transactions](https://www.postgresql.org/docs/18/two-phase.html)
- [JSON types](https://www.postgresql.org/docs/18/datatype-json.html)

## Contribution and scope

A concrete engine reference for SQL, constraints, indexes, query plans, isolation, WAL, prepared transactions, and JSON. Versioned links keep the teaching anchor explicit. PostgreSQL behavior illustrates database mechanisms; it does not define every other engine's guarantees or the entire NoSQL category.

## Reading route

Create a small schema with constraints. Compare query plans with and without a useful index. Use two sessions to observe isolation and retries. Read durability and backup contracts before experimenting with recovery.

## Graph connections

- **explains:** [Databases](../concepts/databases.md), [The Relational Model and SQL](../concepts/relational-model-and-sql.md), [Transactions and Isolation](../concepts/transactions.md), [Indexes and Query Planning](../concepts/indexes-and-query-planning.md), [Database Storage and Recovery](../concepts/storage-and-recovery.md), [Nonrelational Data Models](../concepts/nosql.md), [Distributed Transactions and Sagas](../concepts/distributed-transactions.md)
