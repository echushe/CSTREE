---
id: "file-systems"
type: "concept"
title: "File Systems and Persistence"
aliases: ["Files", "Directories", "fsync", "Crash consistency"]
domains: ["operating-systems"]
branch: "operating-systems"
---

# File Systems and Persistence

## What it is and why it matters

A file system maps names and file operations onto persistent storage. Its namespace and crash behavior are part of an application's correctness model.

## Mechanism

Directories map names to file identities; open handles access files independently of many namespace operations. Buffers and caches decouple a write call from device persistence. Journaling or copy-on-write can help recover file-system structure, but application-level multi-file consistency still requires a protocol.

## Worked example

To replace a configuration file, an application can write a temporary file and rename it into place. Atomic namespace replacement and crash durability are different guarantees. A robust protocol may also need flushing the file and its parent directory under the specific OS and file-system contract.

## Engineering implications

Distinguish atomic operations, durable operations, permissions, and backup protection. Handle short writes and I/O errors. File locks and rename behavior differ across platforms and network file systems. Use a database when application invariants require more transactional behavior than a few file operations can safely supply.

## Graph connections

- **requires:** [Operating Systems](operating-systems.md)
- **related_to:** [Database Storage and Recovery](storage-and-recovery.md), [Security Engineering](security-engineering.md)
- **supported_by:** [Operating Systems Three Easy Pieces](../references/operating-systems-book.md)
