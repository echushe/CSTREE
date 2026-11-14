---
id: "typescript"
type: "concept"
title: "TypeScript"
aliases: ["TS"]
domains: ["languages"]
branch: "languages"
---

# TypeScript

## What it is and why it matters

TypeScript adds static type analysis to JavaScript development. It helps express contracts while using JavaScript runtime semantics.

## Mechanism

Structural typing, unions, control-flow narrowing, and generics describe JavaScript values. Type annotations and interfaces are normally erased during emission. A type assertion tells the checker what to assume; it does not inspect or transform the runtime value.

## Worked example

Declaring `type User = {id: number}` does not make a network response a valid User. An input such as `{"id":"wrong"}` still needs runtime parsing and validation. Narrowing an `unknown` value after actual checks supplies a meaningful boundary.

## Engineering implications

Enable suitable strict checking and keep `any` and assertions deliberate. Check build configuration, module resolution, and runtime targets together. Tests and boundary validation complement static analysis. Language changes and compiler options should be checked against the official handbook and release documentation.

## Graph connections

- **requires:** [JavaScript](javascript.md), [Type Systems](type-systems.md)
- **related_to:** [API Design and Contracts](api-design.md), [Software Testing](testing.md), [Compilers and Toolchains](compilers.md)
- **supported_by:** [Language Specifications and Official Guides](../references/language-specifications.md)
