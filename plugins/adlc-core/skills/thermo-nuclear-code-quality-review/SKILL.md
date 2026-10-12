---
name: thermo-nuclear-code-quality-review
description: "Assess concrete structural maintainability concerns in a requested diff; distinguish defects from optional redesign."
disable-model-invocation: true
---

Read [the ADLC contract](../../references/adlc-contract.md) first. Use the [Claude Code](../../guides/claude-code.md) or [Codex](../../guides/codex.md) guide for the actual host. Resolve nested skills by the relative links below from this package, not by a bare global name.

# Thermo-nuclear code quality review

Use for explicitly requested deep structural review or a concrete maintainability concern. Establish the actual comparison base, acceptance diff, requirements, domain vocabulary and relevant surrounding code. Include in-scope uncommitted work. Review-only scope permits no edits.

Examine abstraction quality, branching/state complexity, canonical ownership, coupling, atomicity and type/error boundaries. Seek a smaller direct design when it removes concrete friction. Check callers and recovery behavior before recommending extraction, parallelism, new interfaces or removal of checks.

File length, repeated conditions, wrappers, casts and possible simplifications are investigation signals, not defects by themselves. Do not impose a 1,000-line limit, require speculative abstractions, treat every alternative as blocking, or infer architecture failure from size. Existing project conventions and actual consequences govern.

Report high-confidence actionable findings with trigger, impact, precise file/line and the smallest practical remedy. Label optional redesign and uncertain hypotheses explicitly. Prioritize correctness/security/data effects and documented requirement violations before concrete maintainability regressions. A recommendation to restructure must explain what improves and what could regress.

If no actionable finding exists, say so; do not manufacture work. Review supports acceptance but cannot prove runtime behavior. Stop once the requested assessment is supported; implementation or broader redesign requires actual authority.
