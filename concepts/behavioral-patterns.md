---
id: "behavioral-patterns"
type: "concept"
title: "Behavioral Design Patterns"
aliases: ["Strategy", "State pattern", "Command", "Observer", "Iterator", "Visitor", "Mediator", "Memento", "Template Method", "Interpreter", "Chain of Responsibility"]
domains: ["design"]
branch: "design"
---

# Behavioral Design Patterns

## What it is and why it matters

Behavioral patterns allocate decisions, communication, traversal, and state transitions among collaborating parts of a program.

## Mechanism

- Strategy selects an algorithm; State changes behavior with an explicit state.
- Command represents an action; Chain of Responsibility passes a request among handlers.
- Observer notifies subscribers; Mediator coordinates collaborators.
- Iterator traverses a collection; Visitor adds operations across an object structure.
- Template Method fixes a skeleton with extension steps.
- Memento captures restorable state; Interpreter models a grammar and its evaluation.

## Worked example

An editor records insert and delete Commands for undo. Each command stores enough information to reverse its own change. Observer can notify the UI after a change, but it does not itself preserve the history required by undo.

## Engineering implications

Specify ordering, reentrancy, and failure behavior for callbacks and notifications. State can replace tangled conditionals when transitions are well defined. Visitor makes new operations easier but new element types harder. Prefer a simple function or switch when the variation is small.

## Graph connections

- **requires:** [Design Patterns](design-patterns.md)
- **related_to:** [Stacks](stacks.md), [Parsing and Abstract Syntax Trees](parsing-and-asts.md), [Messaging and Event Streams](messaging-and-streams.md)
- **supported_by:** [Design Patterns Elements of Reusable Object-Oriented Software](../references/design-patterns-book.md)
