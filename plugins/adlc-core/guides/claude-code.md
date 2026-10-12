# Claude Code

Install adlc-core from the public [adlc-skills repository](https://github.com/Graphik-AI/adlc-skills), then confirm the source before invoking a skill. Version 0.1.0 is a release candidate. The [verification record](../VERIFICATION.md) lists tested hosts and limits.

## Install from GitHub

The marketplace is public and uses HTTPS. Cloning it does not require a GitHub account, repository invitation, SSH key, or token. Your coding agent still needs its own login and project permissions.

Check the existing installation first:

```sh
claude --version
claude plugin list --json
claude plugin marketplace list --json
git ls-remote https://github.com/Graphik-AI/adlc-skills.git refs/heads/main
```

If adlc-core already uses the intended source, verify it below. Do not overwrite an installation from another source. Otherwise, install for cross-project use in your user configuration:

```sh
claude plugin marketplace add https://github.com/Graphik-AI/adlc-skills.git --scope user --json
claude plugin install adlc-core@vecton-adlc --scope user --json
```

## Switch an existing marketplace source

If `vecton-adlc` is registered from a different repository, record the old source and revision first. Remove only this plugin and marketplace, then run the GitHub install commands above. Preserve unrelated registrations and settings.

```sh
claude plugin uninstall adlc-core@vecton-adlc --scope user --json
claude plugin marketplace remove vecton-adlc --scope user --json
```

## Verify the installed source

Run these commands:

```sh
claude plugin marketplace list --json
claude plugin list --json
claude plugin details adlc-core@vecton-adlc
git -C ~/.claude/plugins/marketplaces/vecton-adlc rev-parse HEAD
```

Confirm `adlc-core@vecton-adlc`, version `0.1.0`, user scope, `enabled: true`, and the GitHub source. Compare the 21 skill names in `plugin details` with the [catalog](../CATALOG.md). Git reports the fetched revision.

The tested cache path is `~/.claude/plugins/cache/vecton-adlc/adlc-core/0.1.0`. Each skill is at `skills/<name>/SKILL.md`. Start a fresh session in an authorized project. Avoid loading another copy alongside it.

## Invoke and supply context

Invoke `/adlc-core:code-review` for a review. Use `/adlc-core:<name>` for another catalog entry. Provide the task, requirements, permitted actions, acceptance criteria, and existing evidence. For a review, include the actual comparison base, relevant staged and unstaged changes, and the review-only boundary.

Nested calls use `adlc-core:<name>` or the package-relative file named by the entry skill. Do not substitute a global skill with the same short name. Explicit-only helpers need explicit selection when the host restricts invocation. Report that restriction rather than bypassing it.

Project trust, authentication, and permitted tools still apply. Use available question, delegation, and worktree capabilities only when needed. A permitted sequential route is valid when delegation is unavailable. The bundled Markdown tracker needs no external tracker API.

For browser work, use the authorized running app and the work profile required by your project. Report a missing profile instead of switching. The scanner needs Python 3.12 or later. Project checks need their own runtimes.

## Update or return to a known version

Record the fetched revision and installed version before updating. After reviewing the target source, refresh this marketplace and package:

```sh
claude plugin marketplace update vecton-adlc
claude plugin update adlc-core@vecton-adlc --scope user
claude plugin list --json
```

Use `/reload-plugins` in an interactive session or start a new session. Verify the source and version again. Updating the marketplace does not update an already-running session by itself.

For local recovery, use a separate clean checkout of the identified previous revision or retarget the local marketplace. Repeat the update and verification steps. A version string does not pin Git `main`. GitHub revision-pinned rollback and authenticated session refresh have not been verified. See [host evidence](../VERIFICATION-HOSTS.md) before relying on either.

## Disable and uninstall

To disable the plugin, run:

```sh
claude plugin disable adlc-core@vecton-adlc --scope user --json
```

To uninstall it, run:

```sh
claude plugin uninstall adlc-core@vecton-adlc --scope user --json
```

If no other installation needs the marketplace, remove its registration:

```sh
claude plugin marketplace remove vecton-adlc --scope user --json
```

Check `claude plugin list --json` and `claude plugin marketplace list --json`. Start a fresh session and confirm that the removed installation is absent. Preserve unrelated settings and plugins.

## Local-checkout alternative

From an authorized checkout root, run:

```sh
claude plugin validate plugins/adlc-core --strict
claude plugin validate .claude-plugin/marketplace.json --strict
claude plugin marketplace add "$PWD"
claude plugin install adlc-core@vecton-adlc --scope user
```

For session-only loading, use `claude --plugin-dir ./plugins/adlc-core`. This loads `adlc-core@inline` without marketplace registration. Confirm that you selected the intended source.

## Diagnose missing or wrong skills

Check network access, source, installed version, enablement, and project trust. Restart a stale session. If names are duplicated, inspect the loaded path. Check the relevant support files and tool or authentication prerequisites.

Collect minimal redacted diagnostics. A discovered skill is available for selection. Its presence does not prove that its workflow ran.

Sources: [manifest rules](https://code.claude.com/docs/en/plugins/manifest-reference), [plugin commands](https://code.claude.com/docs/en/plugins/cli-reference), [loading and updates](https://code.claude.com/docs/en/plugins/loading), and [skill invocation](https://code.claude.com/docs/en/skills). Checked 12 October 2026.
