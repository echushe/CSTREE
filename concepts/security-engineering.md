---
id: "security-engineering"
type: "concept"
title: "Security Engineering"
aliases: ["Threat modeling", "Authentication", "Authorization", "Application security", "Least privilege"]
domains: ["engineering"]
branch: "engineering"
---

# Security Engineering

## What it is and why it matters

Security engineering protects system assets under an explicit threat model. It is part of design, implementation, delivery, and operation rather than a final inspection step.

## Mechanism

Identify assets, trust boundaries, adversary capabilities, and misuse cases. Authentication establishes identity; authorization decides permitted actions. Input validation, output encoding, parameterized queries, least privilege, secret handling, and dependency controls address different risks. Encryption does not replace authorization.

## Worked example

A logged-in user requesting `/orders/other-user-id` must still pass an ownership or policy check. Hiding that link in the UI is insufficient. A parameterized SQL query prevents value injection but also does not establish whether the user may read the selected row.

## Engineering implications

Use established libraries and protocols for cryptography and identity. Check permissions at every meaningful boundary and test rejection paths. Rotate exposed credentials and inspect affected access. Reference a specific standard version when turning broad goals into a verification checklist.

## Graph connections

- **requires:** [API Design and Contracts](api-design.md), [Requirements and Specifications](requirements-and-specifications.md)
- **related_to:** [Databases](databases.md), [Computer Networks](computer-networks.md), [Build Systems and Dependencies](build-and-dependencies.md), [AI Assisted Software Development](ai-assisted-development.md)
- **supported_by:** [OWASP Application Security Verification Standard](../references/security-guides.md)
