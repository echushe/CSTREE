---
id: "nosql"
type: "concept"
title: "Nonrelational Data Models"
aliases: ["NoSQL", "Document databases", "Key-value stores", "Graph databases"]
domains: ["databases"]
branch: "databases"
---

# Nonrelational Data Models

## What it is and why it matters

Nonrelational databases include key-value, document, wide-column, and graph models. They group together by contrast with relational systems, not by one shared consistency or transaction guarantee.

## Mechanism

A key-value model retrieves by key. Documents group nested fields. Wide-column models organize data around partition and clustering keys. Graph databases support relationship-oriented access. Model choice shapes query flexibility, locality, update boundaries, and how invariants are enforced.

## Worked example

A document containing an order and its line items makes one aggregate easy to read. A query across all line items by product may require an index or another representation. Duplicating product names inside orders also requires deciding whether they are historical snapshots or synchronized copies.

## Engineering implications

Start from access patterns and required invariants. Inspect the selected engine's transaction scope, consistency settings, indexing, and failure behavior. Schema flexibility still requires application contracts and migration handling. Relational engines may also support documents and graph-like queries.

## Graph connections

- **requires:** [Data Modeling and Schema Evolution](data-modeling.md)
- **compares_with:** [The Relational Model and SQL](relational-model-and-sql.md)
- **related_to:** [Partitioning and Sharding](partitioning-and-sharding.md), [Consistency Models and CAP](consistency-models.md)
- **supported_by:** [PostgreSQL Database Documentation](../references/postgresql-documentation.md), [Perspectives on the CAP Theorem](../papers/gilbert-lynch-2012-cap-perspectives.md)
