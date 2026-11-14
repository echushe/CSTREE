---
id: "build-and-dependencies"
type: "concept"
title: "Build Systems and Dependencies"
aliases: ["Build graph", "Dependency management", "Reproducible builds", "Lockfiles"]
domains: ["engineering"]
branch: "engineering"
---

# Build Systems and Dependencies

## What it is and why it matters

A build turns source and declared inputs into usable artifacts. Dependency management determines which external components and versions participate in that result.

## Mechanism

A build graph orders tasks by dependencies. Incremental builds reuse outputs only when relevant inputs are unchanged. Hermetic builds control environmental inputs; reproducible builds produce equivalent specified outputs from the same inputs. Lockfiles, checksums, toolchain versions, and generated code all affect repeatability.

## Worked example

If generated code depends on a schema, the build graph must include that schema edge. Omitting it can reuse stale output after a schema change even though compilation appears successful. A clean build may hide the missing incremental dependency.

## Engineering implications

Distinguish direct and transitive dependencies, build-time and runtime inputs, and package version constraints from resolved versions. Keep provenance and update policies explicit. A lockfile improves repeatability but does not establish that a dependency is correct or trustworthy.

## Graph connections

- **requires:** [Graphs and Graph Algorithms](graphs.md), [Compilers and Toolchains](compilers.md)
- **related_to:** [Version Control and Git](version-control.md), [Continuous Integration and Delivery](ci-cd.md), [Security Engineering](security-engineering.md)
- **supported_by:** [Software Engineering and Git Guides](../references/software-construction.md)
