# Host verification

## Historical behavior evidence

Earlier bounded local checks exercised review-only staged/unstaged diffs,
implementation/debugging, local tracker composition, research, a logic prototype,
and the scanner/templates. These checks establish those cases only.
Previous GitHub-backed installation/discovery passed on Claude Code 2.1.294
and Codex CLI/app-server 0.160.1. Those historical checks used another source;
the public repository's installation checks are recorded separately below.

## Public repository checks — 12 October 2026

Tested Claude Code **2.1.296** and Codex CLI/app-server **0.162.0** against
public repository revision `6f84040c7a08b458fed21f9626cd0de764a0e2b5`.

Both hosts registered `https://github.com/Graphik-AI/adlc-skills.git`, installed
`adlc-core@vecton-adlc` **0.1.0**, and reported it enabled. Claude's native
`plugin details` returned exactly 21 skills. Codex's fresh app-server
`skills/list` returned exactly 21 enabled `adlc-core:` skills from the installed
package with no errors. Both fetched marketplace revisions matched the revision
above, and installed skill/support bytes matched this public package.

Checks used separate temporary host configuration directories. Git credential
helpers and interactive authentication were disabled; no GitHub or coding-agent
credentials were copied into those directories. A separate anonymous HTTPS clone
also succeeded. Global Codex/Claude settings and plugin-registration files
remained byte-for-byte unchanged. No model-session skill execution was requested.

These results establish public installation, source identity, and discovery.
They do not repeat or expand the historical workflow-behavior trials.

## Limits

Execution of every skill, authenticated session reload after package updates,
revision-pinned rollback, desktop/IDE/cloud/remote operation, and real browser
workflow execution are not established by the public repository installation checks.
The scanner needs Python 3.12+. The waiting example needs Node with native
TypeScript stripping. The host and project supply other tools and permissions.
