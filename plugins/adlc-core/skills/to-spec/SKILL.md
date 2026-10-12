---
name: to-spec
description: "Synthesize agreed work into a proportionate implementation-ready specification."
disable-model-invocation: true
---

Read [the ADLC contract](../../references/adlc-contract.md) first. Use the [Claude Code](../../guides/claude-code.md) or [Codex](../../guides/codex.md) guide for the actual host. Resolve nested skills by the relative links below from this package, not by a bare global name.

# To spec

Synthesize agreed behavior into a concise implementation-ready spec; this is not a new interview. Reuse an adequate existing spec. Read the task, applicable project instructions, exact affected sources, glossary/ADRs and acceptance evidence needs.

Use the existing tracker, or [local Markdown](../../references/issue-tracker-local.md). Include the problem/result, intended behavior and exclusions, consequential decisions, dependencies, files/interfaces where concrete locations help implementation, and observable acceptance/checks. User stories are optional; do not pad the spec to a template.

Choose checks at existing public boundaries. Reuse agreed seams and independently derived expected results. Ask only about consequential unresolved choices; mark dependent work blocked instead of filling gaps with plausible policy. Save within authorized scope and label readiness accurately using the project's vocabulary or [triage mapping](../../references/triage-labels.md). Existing approval to implement counts. Writing a spec does not authorize external publication or an unrequested implementation.
