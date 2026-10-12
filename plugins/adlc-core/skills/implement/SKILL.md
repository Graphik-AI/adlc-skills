---
name: implement
description: "Implement a bounded task, spec or ticket with relevant checks and review."
disable-model-invocation: true
---

Read [the ADLC contract](../../references/adlc-contract.md) first. Use the [Claude Code](../../guides/claude-code.md) or [Codex](../../guides/codex.md) guide for the actual host. Resolve nested skills by the relative links below from this package, not by a bare global name.

# Implement

Carry out a clear bounded task, spec or ticket. A small well-specified change needs no separate spec or ticket graph.

1. Read scope, current source, Git state and project requirements. Preserve unrelated edits. Establish intended behavior, what must remain unchanged, acceptance criteria and the smallest relevant checks before substantive changes.
2. Implement the smallest correct solution. Use bundled [tdd](../tdd/SKILL.md) when repeatable behavioral regression checks are proportionate; reuse accepted seams. For reversible wording/layout changes use appropriate direct review/runtime evidence instead of manufacturing tests.
3. Run affected checks and mandatory repository checks. Investigate in-scope failures through [systematic-debugging](../systematic-debugging/SKILL.md). Reuse still-valid results; a full suite is required only when project rules or affected scope justify it. Explain mocks and unavailable runtime evidence.
4. Use [code-review](../code-review/SKILL.md) on the actual acceptance diff, including relevant uncommitted work. Fix actionable in-scope findings and renew invalidated checks. Do not fix unrelated issues or weaken behavior to pass tests.
5. Commit only when authorized, staging only in-scope changes. Report verified outcomes and limits. Local integration completion is separate from publication and intended-environment delivery.

Ask only about consequential unresolved decisions or authority that does not cover a proposed action. Continue independent work while dependent work is blocked; preserve explicit review pauses.
