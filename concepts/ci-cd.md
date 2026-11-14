---
id: "ci-cd"
type: "concept"
title: "Continuous Integration and Delivery"
aliases: ["CI", "CD", "Canary release", "Deployment"]
domains: ["engineering"]
branch: "engineering"
---

# Continuous Integration and Delivery

## What it is and why it matters

Continuous integration checks changes together frequently. Continuous delivery keeps a version ready for release; continuous deployment automatically releases changes that pass the defined process.

## Mechanism

A pipeline builds an artifact, runs relevant checks, records provenance, and promotes it through environments. Reusing the same artifact avoids rebuilding different inputs for each stage. Feature flags, canary releases, health checks, and rollback or forward recovery limit release exposure.

## Worked example

Deploy a new version to a small portion of traffic and compare error rate and latency with a suitable baseline. If a database migration removed a column, rolling back only the application may fail; compatibility needs to be planned across both versions.

## Engineering implications

Keep checks informative and proportionate to failure impact. Protect credentials and artifact integrity. Distinguish a passed pipeline from verified production behavior. Release strategy must account for data changes, background workers, and old clients, not only replacing a web process.

## Graph connections

- **requires:** [Version Control and Git](version-control.md), [Build Systems and Dependencies](build-and-dependencies.md), [Software Testing](testing.md)
- **related_to:** [Observability and Reliability](observability.md), [Data Modeling and Schema Evolution](data-modeling.md), [Resilience and Idempotency](resilience-and-idempotency.md)
- **supported_by:** [Software Engineering and Git Guides](../references/software-construction.md), [Site Reliability Engineering](../references/sre-book.md)
