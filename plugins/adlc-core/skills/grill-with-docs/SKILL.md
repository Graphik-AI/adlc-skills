---
name: grill-with-docs
description: "Resolve consequential choices using focused grilling and useful domain documentation."
disable-model-invocation: true
---

Read [the ADLC contract](../../references/adlc-contract.md) first. Use the [Claude Code](../../guides/claude-code.md) or [Codex](../../guides/codex.md) guide for the actual host. Resolve nested skills by the relative links below from this package, not by a bare global name.

# Grill with docs

Use [grilling](../grilling/SKILL.md) for the consequential unresolved decision and [domain-modeling](../domain-modeling/SKILL.md) where meanings, glossary terms or a non-obvious tradeoff need recording. Read both from this package before composition. Inspect known facts yourself; reuse valid decisions and do not restart an interview merely to run the wrapper.

Work within the task's actual tracker and scope; the [local convention](../../references/issue-tracker-local.md) is sufficient when no tracker exists. Leave product choices to the developer. Save useful reasons and unresolved questions in existing context. Create a glossary entry only when a term settles and an ADR only when the tradeoff warrants one. A clear task needs no new artifacts.
