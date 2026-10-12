---
name: wayfinder
description: "Coordinate unresolved decisions across sessions using a map, dependencies and claims."
disable-model-invocation: true
---

Read [the ADLC contract](../../references/adlc-contract.md) first. Use the [Claude Code](../../guides/claude-code.md) or [Codex](../../guides/codex.md) guide for the actual host. Resolve nested skills by the relative links below from this package, not by a bare global name.

# Wayfinder

Use a map when unresolved decisions span sessions or depend on one another. A single bounded question can go directly to [grill-with-docs](../grill-with-docs/SKILL.md). Track decisions, not implementation or delivery success.

Use the existing project tracker; otherwise read the bundled [local tracker convention](../../references/issue-tracker-local.md) and [triage mapping](../../references/triage-labels.md). No global setup installer is needed.

## Chart or resume

1. Establish the destination, constraints, existing decisions and excluded work. Reuse settled answers. Ask only consequential unresolved questions through [grilling](../grilling/SKILL.md); use [domain-modeling](../domain-modeling/SKILL.md) only for unclear meanings or useful decision records.
2. Keep a map with Destination, Notes, Decisions so far (linked gists), Not yet specified and Out of scope. Precise questions become separate tickets; vague questions remain notes. Do not create a mandatory spec or course from a small task.
3. Give each ticket a type, status, dependencies and claim. Research establishes facts through [research](../research/SKILL.md); prototype tests a question through [prototype](../prototype/SKILL.md); grilling requires the human's answer; task denotes bounded work needed before a decision. Capabilities and actions remain conditional on scope.
4. Verify dependencies are resolved, claim the selected open ticket before work, then investigate. Other independent work can continue. Refer to tickets by title, with links. A subagent can investigate facts when useful and supported; it cannot supply the human's decision.
5. Record the answer and evidence in the ticket, resolve only when supported, release the claim, and add a short linked gist to the map. For incomplete work preserve the exact missing evidence and release the claim at closeout. Keep scope exclusions separate from resolved answers.

Charting does not itself authorize implementation. Continue into execution only when the task authorizes it; preserve explicit stop conditions. There is no universal one-ticket-per-session limit: respect the user's bounded objective and actual dependencies. Commit or publish tracker updates only within applicable authority.
