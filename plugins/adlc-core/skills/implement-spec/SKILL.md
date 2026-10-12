---
name: implement-spec
description: "Coordinate implementation of a settled spec when its dependency graph benefits from it."
disable-model-invocation: true
---

Read [the ADLC contract](../../references/adlc-contract.md) first. Use the [Claude Code](../../guides/claude-code.md) or [Codex](../../guides/codex.md) guide for the actual host. Resolve nested skills by the relative links below from this package, not by a bare global name.

# Implement spec

Coordinate a settled specification and real dependency graph when it benefits from multiple implementers. If there is no useful graph, use [implement](../implement/SKILL.md) directly; do not create tickets or branches just to satisfy this workflow.

Read the spec, actual tracker, current Git state and acceptance requirements. Use [local tracker guidance](../../references/issue-tracker-local.md) only when needed. Establish bounded ownership, dependency order and integration checks. Parallelism is optional and requires supported host capabilities and independent file/worktree ownership; otherwise execute sequentially.

When worktrees are useful, inspect existing worktrees and source refs, preserve unrelated changes, and establish safe fixtures, ports and startup instructions. Do not reset checkouts onto a guessed base or copy secrets to make setup work. Missing tools leave that route unavailable. Share research in an accessible safe project note; do not store sensitive context in ephemeral private paths other workers cannot use.

Each implementer uses [implement](../implement/SKILL.md), with [tdd](../tdd/SKILL.md) only for appropriate behavior tests. Capture checks and limits for each piece. Integrate on the verified target within Git authority; inspect conflicts and rerun checks invalidated by integration. Do not infer integration success from isolated branch results.

Review the integrated actual diff with [code-review](../code-review/SKILL.md). Fix actionable in-scope findings, preserve optional suggestions separately, and stop repeating review when acceptance is supported. Ticket resolution, commits, PR creation/readiness, merges and cleanup each follow existing authority and actual completion rules. A local task does not authorize publication. Preserve review pauses. Remove only owned disposable material through the applicable recoverable-cleanup mechanism; never reset or remove user work.

Report integrated behavior, evidence and unresolved gaps. Tracker closure and a green branch do not establish intended-environment delivery. This skill adds no ongoing-operations or operational-handoff programme.
