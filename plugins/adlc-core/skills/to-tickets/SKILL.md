---
name: to-tickets
description: "Split agreed work into independently verifiable pieces when coordination helps."
disable-model-invocation: true
---

Read [the ADLC contract](../../references/adlc-contract.md) first. Use the [Claude Code](../../guides/claude-code.md) or [Codex](../../guides/codex.md) guide for the actual host. Resolve nested skills by the relative links below from this package, not by a bare global name.

# To tickets

Split a plan, spec or sufficient task conversation only when separately verifiable increments or coordination help. Reuse existing work and the project tracker, falling back to [local Markdown](../../references/issue-tracker-local.md) and [triage roles](../../references/triage-labels.md).

Read accepted behavior, current source and genuine dependencies. Each ticket states the outcome, acceptance/checks, scope and blockers. Prefer a usable path through the affected layers; do not invent a UI, schema, prefactor or layer merely to make a vertical slice. Refactor first only when a concrete dependency requires it and authority covers it.

For a broad mechanical migration that cannot remain correct per slice, consider expand, migrate callers, then contract with explicit integration verification. Do not remove the old route until callers and compatibility evidence support it.

Reuse an approved breakdown. Ask only if granularity or dependency choices materially affect behavior or coordination. Create one local file or authorized tracker issue per piece, then link blockers after identities exist. Mark ready only when sufficient context exists; preserve parent state and explicit task boundaries. External publication requires authority for that tracker/target.
