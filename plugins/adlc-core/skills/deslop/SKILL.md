---
name: deslop
description: "Clean unnecessary material from the actual task diff while preserving behavior and safeguards."
---

Read [the ADLC contract](../../references/adlc-contract.md) first. Use the [Claude Code](../../guides/claude-code.md) or [Codex](../../guides/codex.md) guide for the actual host. Resolve nested skills by the relative links below from this package, not by a bare global name.

# Deslop

Perform narrow authorized cleanup of the actual task diff. Establish the real comparison base and include relevant staged/unstaged work; never assume `main` or claim only HEAD covers the task. Review-only requests get findings without edits.

Remove demonstrably unnecessary comments, duplication, type escapes or scaffolding that conflict with project conventions. Before removing defensive checks or exception handling, trace the real trust/invariant boundary and failure behavior; unusual-looking checks may be essential.

Preserve observable behavior, errors and security guarantees. Prefer explicit maintainable code over shorter code. Do not fix a behavioral bug or broaden cleanup unless task authority includes it. Review the final diff and renew affected checks, reusing valid evidence. Stop after the bounded cleanup and report significant changes and limits concisely.
