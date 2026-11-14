---
id: "python"
type: "concept"
title: "Python"
aliases: ["Python language"]
domains: ["languages"]
branch: "languages"
---

# Python

## What it is and why it matters

Python emphasizes readable syntax and a large library ecosystem. It is useful for automation, services, data work, and quickly testing an idea.

## Mechanism

Names bind to objects; assignment does not normally copy an object. Runtime checks enforce most operation compatibility. Type annotations support external checking but are not generally enforced by the runtime. The language has multiple implementations; CPython behavior should not be mistaken for the whole language definition.

## Worked example

After `a = [1]; b = a; b.append(2)`, both names refer to `[1,2]`. With `b = a.copy()`, appending to b leaves the original list alone, although nested mutable elements would still be shared by a shallow copy.

## Engineering implications

Use isolated environments and explicit dependency metadata. Profile hot paths before replacing code with native extensions. Concurrency and parallel execution depend on interpreter, build, libraries, and workload; a blanket statement about a global interpreter lock is insufficient.

## Graph connections

- **requires:** [Programming Languages](programming-languages.md)
- **related_to:** [Type Systems](type-systems.md), [Build Systems and Dependencies](build-and-dependencies.md), [AI Assisted Software Development](ai-assisted-development.md)
- **supported_by:** [Language Specifications and Official Guides](../references/language-specifications.md)
