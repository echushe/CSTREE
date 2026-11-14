---
id: "javascript"
type: "concept"
title: "JavaScript"
aliases: ["JS", "ECMAScript"]
domains: ["languages"]
branch: "languages"
---

# JavaScript

## What it is and why it matters

JavaScript is a dynamically typed language standardized as ECMAScript. Browsers and server runtimes provide host APIs around the language core.

## Mechanism

Objects, closures, prototype-based delegation, and promises are central mechanisms. An event loop and task scheduling belong to the host integration; the ECMAScript specification defines language behavior and promise jobs. `await` suspends an async function, not the entire process.

## Worked example

After `const a = {count: 1}; const b = a; b.count = 2;`, `a.count` is 2. `const` prevents rebinding a; it does not freeze the object. Two concurrent async calls can still interleave updates across `await` boundaries.

## Engineering implications

Validate external data, understand coercion and equality rules, and handle promise rejection. CPU-intensive work can block an event loop; use a suitable worker or separate process when needed. Browser DOM APIs and Node APIs are not all part of ECMAScript.

## Graph connections

- **requires:** [Programming Languages](programming-languages.md)
- **extended_by:** [TypeScript](typescript.md)
- **related_to:** [I/O and Event Loops](io-and-event-loops.md), [HTTP and Remote Procedure Calls](http-and-rpc.md)
- **supported_by:** [Language Specifications and Official Guides](../references/language-specifications.md)
