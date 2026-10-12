---
name: code-review
description: "Review the actual requested diff against requirements and repository standards, including in-scope uncommitted work."
---

Read [the ADLC contract](../../references/adlc-contract.md) first. Use the [Claude Code](../../guides/claude-code.md) or [Codex](../../guides/codex.md) guide for the actual host. Resolve nested skills by the relative links below from this package, not by a bare global name.

# Code review

Review the actual changes being accepted along two axes: requested behavior and repository standards. Neither a missing spec file nor a missing tracker erases requirements already established in the task.

## Establish coverage

Inspect Git status and the requested base/target. Resolve references before using them. Distinguish a direct comparison from a merge-base comparison; use the user's requested comparison and explain the chosen base. For a branch review include its committed diff, then staged/unstaged and relevant untracked files when they are part of acceptance. Read untracked files directly; `git diff` does not include them. Preserve unrelated changes and list material coverage gaps. An empty committed diff is not proof there is no work to review.

Read the task or supplied spec/ticket first, applicable AGENTS/project standards, affected callers and tests. Fetch tracker context only if relevant and available. Ask only when an ambiguous base or missing requirement materially changes the review.

## Assess and report

Check missing or unrequested behavior, compatibility, access/ownership boundaries, data integrity, failure handling and concrete maintainability effects. Use naming, duplication, state complexity, pass-through wrappers and indirection as investigation signals, not automatic violations. Project conventions take precedence over generic preferences. Skip formatting issues enforced by tooling.

A proportionate single reviewer can cover both axes. Independent reviewers are optional when the scope benefits and host capabilities/authority allow them; give each the same verified coverage and constraints. Do not require subagents or an external tracker to review a small change.

Report actionable findings by severity, with trigger, impact, precise file/line and relevant requirement. Distinguish confirmed defects, hypotheses, optional alternatives and missing evidence. If neither axis has findings, say so. Review is evidence about the diff; it cannot establish unexercised runtime behavior.

Review-only scope means no edits. During authorized implementation, fix in-scope defects and renew affected checks/review. Do not repeat the entire assessment merely because a workflow entered a new phase; stop when applicable acceptance requirements are supported and blockers resolved.
