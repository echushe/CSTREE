---
id: "version-control"
type: "concept"
title: "Version Control and Git"
aliases: ["Git", "Commits", "Branches", "Merge", "Rebase"]
domains: ["engineering"]
branch: "engineering"
---

# Version Control and Git

## What it is and why it matters

Version control records changes and supports collaboration, review, recovery, and comparison. Git represents history as commits connected through parent relationships.

## Mechanism

A commit records a tree and metadata; a branch is a movable reference. The working tree, staging area, and committed tree are different states. Merge combines histories; rebase recreates changes on another base. Revert records an inverse change without removing the original historical commit.

## Worked example

Two branches change separate functions and may merge automatically. If both edit the same behavior, resolving text conflicts is only the first step; the combined program still needs semantic review and appropriate checks.

## Engineering implications

Keep changes focused enough to review and record why they matter. Inspect the diff before committing. Coordinate before rewriting shared history. Ignoring a secret file does not remove a secret already recorded in history. Use history to locate regressions and understand prior decisions.

## Graph connections

- **requires:** [Graphs and Graph Algorithms](graphs.md)
- **related_to:** [Software Testing](testing.md), [Continuous Integration and Delivery](ci-cd.md), [Agentic Software Development](agentic-development.md)
- **supported_by:** [Software Engineering and Git Guides](../references/software-construction.md)
