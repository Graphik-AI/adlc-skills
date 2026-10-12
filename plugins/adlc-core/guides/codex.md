# Codex

Install adlc-core from the public [adlc-skills repository](https://github.com/Graphik-AI/adlc-skills), then select its packaged skill in Codex CLI. Version 0.1.0 is a release candidate. The [verification record](../VERIFICATION.md) lists tested hosts and limits.

## Install from GitHub

The marketplace is public and uses HTTPS. Cloning it does not require a GitHub account, repository invitation, SSH key, or token. Your coding agent still needs its own login and project permissions.

Check the existing installation first:

```sh
codex --version
codex plugin --help
codex plugin list --json
codex plugin marketplace list --json
git ls-remote https://github.com/Graphik-AI/adlc-skills.git refs/heads/main
```

If adlc-core already uses the intended source, verify it below. Do not overwrite an installation from another source. Otherwise, install for cross-project use in your Codex configuration:

```sh
codex plugin marketplace add https://github.com/Graphik-AI/adlc-skills.git --ref main --json
codex plugin add adlc-core@vecton-adlc --json
```

## Switch an existing marketplace source

If `vecton-adlc` is registered from a different repository, record the old source and revision first. Remove only this plugin and marketplace, then run the GitHub install commands above. Preserve unrelated registrations and settings.

```sh
codex plugin remove adlc-core@vecton-adlc --json
codex plugin marketplace remove vecton-adlc --json
```

## Verify the installed source

Run these commands:

```sh
codex plugin marketplace list --json
codex plugin list --marketplace vecton-adlc --json
git -C ~/.codex/.tmp/marketplaces/vecton-adlc rev-parse HEAD
```

Confirm `adlc-core@vecton-adlc`, version `0.1.0`, `installed: true`, `enabled: true`, and the GitHub `marketplaceSource`. Git reports the fetched revision. The install result reports `installedPath`; the tested path is `~/.codex/plugins/cache/vecton-adlc/adlc-core/0.1.0`.

Start a fresh `codex` session. Use `/skills` or type `$` to inspect the adlc-core entries and compare the 21 names with the [catalog](../CATALOG.md). Use the picker to confirm discovery rather than counting files on disk. Codex CLI 0.160.1 has no `plugin details` command.

## Select the packaged implementation

Use `/skills` or type `$`, then select the adlc-core entry. Its name is `adlc-core:<name>`, such as `adlc-core:code-review`. If a global skill has the same short name, confirm the package path. An ambiguous `$code-review` does not identify the selected source.

Provide the task, requirements, permitted actions, acceptance criteria, and existing evidence. For a review, include the actual diff and comparison base. Respect explicit-only selection.

When a workflow names a helper file, read that exact package-relative `SKILL.md`. Do not substitute an unrelated global copy. Use question, delegation, and worktree capabilities only when the host provides them. Otherwise, use a permitted sequential route or report the missing capability. Preserve sandbox restrictions. The bundled Markdown tracker needs no external tracker API.

For browser work, use the authorized running app and the work profile required by your project. Report a missing profile instead of switching. The scanner needs Python 3.12 or later. Project checks need their own runtimes.

## Update and recovery

Record the fetched revision and installed version before updating. After reviewing the target source, refresh this marketplace and package:

```sh
codex plugin marketplace upgrade vecton-adlc --json
codex plugin add adlc-core@vecton-adlc --json
codex plugin list --marketplace vecton-adlc --json
```

Start a new session and verify the loaded path and version. `marketplace upgrade` refreshes a Git-backed snapshot. It does not update an already-running session and is unnecessary for a local folder.

For local recovery, use a separate clean checkout of the identified previous revision or retarget the local marketplace. Repeat installation and source verification. GitHub revision-pinned rollback and authenticated session reload have not been verified. See [host evidence](../VERIFICATION-HOSTS.md) before relying on either.

## Disable and uninstall

Codex CLI 0.160.1 has no `plugin disable` subcommand. To disable adlc-core, modify only its existing section in your `~/.codex/config.toml`:

```toml
[plugins."adlc-core@vecton-adlc"]
enabled = false
```

Preserve unrelated settings. Start a fresh session and confirm disablement with `codex plugin list --marketplace vecton-adlc --json`.

To uninstall the plugin, run:

```sh
codex plugin remove adlc-core@vecton-adlc --json
```

If no other installation needs the marketplace, remove its registration:

```sh
codex plugin marketplace remove vecton-adlc --json
```

Check `codex plugin list --json` and `codex plugin marketplace list --json`. Start a fresh session and confirm that adlc-core is absent from the picker.

## Local-checkout alternative

From an authorized checkout root, run:

```sh
codex plugin marketplace add "$PWD" --json
codex plugin add adlc-core@vecton-adlc --json
codex plugin list --marketplace vecton-adlc --json
```

This uses a local source. Project trust, authentication, and permitted actions still apply.

## Troubleshoot in order

Check network access, source, installation, enablement, and project trust. Restart a stale session. Check duplicate short names, support files, and the tools or authentication needed by the failing step.

Collect minimal redacted diagnostics. A selected skill does not prove that its workflow executed.

Sources: [plugin packaging and marketplaces](https://developers.openai.com/plugins/build/plugins), [skill selection and metadata](https://developers.openai.com/codex/skills), and the installed CLI help. Checked 12 October 2026. The verified CLI install route is separate from the documented desktop install flow.
