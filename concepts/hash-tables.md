---
id: "hash-tables"
type: "concept"
title: "Hash Tables"
aliases: ["Hash map", "Dictionary", "Hash set"]
domains: ["algorithms"]
branch: "algorithms"
---

# Hash Tables

## What it is and why it matters

A hash table implements fast key lookup by mapping a key through a hash function into a table. Dictionaries, sets, caches, and symbol tables commonly use it.

## Mechanism

Collisions require chaining or open addressing. The load factor is entries divided by buckets or slots. Expected O(1) lookup assumes suitable hashing and controlled load; worst-case lookup can be O(n). Equal keys must have equal hashes, but equal hashes do not prove key equality.

## Worked example

For a toy hash `h(k) = k mod 5`, keys 7 and 12 both map to bucket 2. Chaining stores both there and checks equality during lookup. Resizing requires redistributing entries because the mapping depends on table capacity.

## Engineering implications

Do not mutate a key in a way that changes its equality or hash while stored. Consider adversarial collision behavior for untrusted input. Iteration order is an implementation or language guarantee, not a property of hashing itself. Use a tree when ordered ranges are essential.

## Graph connections

- **requires:** [Arrays and Linked Lists](arrays-and-linked-lists.md)
- **compares_with:** [Trees and Search Trees](trees.md)
- **used_by:** [Caching](caching.md), [Compilers and Toolchains](compilers.md)
- **supported_by:** [Introduction to Algorithms](../references/algorithms-reference.md)
