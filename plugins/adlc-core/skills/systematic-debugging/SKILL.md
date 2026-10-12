---
name: systematic-debugging
description: Investigate unexplained failures, regressions and unexpected behavior across the relevant code and runtime boundaries before making a supported fix.
---

# Systematic debugging

Read the [ADLC contract](../../references/adlc-contract.md) and the applicable [Claude Code](../../guides/claude-code.md) or [Codex](../../guides/codex.md) guide. This adapts the Superpowers investigation workflow; all required instruction support is bundled here.

## Establish what failed

Reuse the expected behavior, relevant prior evidence and current scope. In diagnose/review-only work, investigate and report without editing. A clear local error can need only a short investigation; a failure spanning UI, API, database or provider boundaries needs evidence from the boundaries involved.

Read the error and relevant stack frames, identify the actual checkout/artifact and environment, and compare recent changes. Reproduce only when safe and useful. Existing reliable evidence may be sufficient; do not repeatedly invoke paid or production operations to satisfy a reproduction loop. When reproduction is unavailable, state what was observed and what remains a hypothesis.

For multiple components, locate the first divergence between expected and observed behavior. Use the minimum allowlisted evidence: operation type, status/error code, correlation marker, timing, or whether a required setting is present. Do not dump environment variables, complete request/response bodies, credentials, customer records or browser storage. Prefer existing safe telemetry; temporary instrumentation requires edit authority and must not expose sensitive values. For example, compare a required configuration key's presence at two boundaries without printing its value or enumerating other keys.

Use [root-cause tracing](root-cause-tracing.md) when a bad value or unexpected side effect appears far from its origin. Compare a relevant working example and the actual owning implementation, including the assumptions that differ; broad analogous code is not proof of the cause.

## Test a hypothesis

State a concrete explanation and the evidence supporting it. Choose the smallest safe observation or experiment that could disprove it. Change one relevant variable at a time; do not stack speculative fixes. Read the result before choosing the next experiment.

For a timing failure, use [condition-based waiting](condition-based-waiting.md) to observe the required state with a deadline. A longer sleep, swallowed exception or unlimited retry does not establish the cause. If evidence contradicts the hypothesis, revise it. Repeated failed fixes call for reassessing the reproduction, environment and assumptions; they are not proof that the architecture is wrong. Escalate a concrete missing decision/access requirement or propose a bounded design investigation only when evidence supports it.

## Make the supported fix

When authorized, correct the identified cause with the smallest change that preserves intended behavior and security. Avoid unrelated cleanup. Add a meaningful regression check when the behavior warrants repeatable testing; use the bundled [Matt TDD workflow](../tdd/SKILL.md) for red/green work. Existing agreement about test boundaries counts. A reversible documentation or configuration correction may instead need a proportionate direct check, plus required repository checks.

If invalid input or unsafe side effects caused the defect, consult [defense in depth](defense-in-depth.md). Add checks at actual trust or invariant boundaries, not automatically at every function. Test relevant rejection and allowed behavior.

Verify the affected behavior in the relevant environment and renew checks affected by the fix. Reuse valid evidence elsewhere. Follow the shared contract's evidence and stopping rules; there is no external verification skill dependency. A mocked result, passing unit test and real provider result support different claims.

If the cause remains uncertain, report the strongest evidence, rejected hypotheses and the exact next observation needed. Mitigation can be appropriate within authority, but label it as mitigation and bound its retries/timeouts; do not declare the underlying defect resolved or add ongoing monitoring outside the task.

Finish with the cause or uncertainty, concrete change if any, checks and observed results, and material gaps. Preserve explicit review pauses and stop at the requested task boundary.
