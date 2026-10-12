# ADLC Skills

21 practical skills for building software with AI coding agents, packaged as
`adlc-core` for Claude Code and Codex. Choose a workflow in the
[skill catalog](plugins/adlc-core/CATALOG.md) and use only what your task needs.

This package builds on **Matt Pocock**, **Superpowers by Jesse Vincent**,
**Cursor**, **GitHub**, **Anthropic**, and **HumanLayer / Dex Horthy**.
Their work, licenses, and source identities are documented in
[acknowledgements](UPSTREAMS.md) and retained inside the installed plugin.

## Install

The repository is public. Use HTTPS; no GitHub account, invitation, SSH key,
or GitHub token is required to clone it. Your coding agent needs its own login.

### Claude Code

```sh
claude plugin marketplace add https://github.com/Graphik-AI/adlc-skills.git --scope user --json
claude plugin install adlc-core@vecton-adlc --scope user --json
```

Invoke `/adlc-core:code-review`, or another name from the catalog.
The [Claude Code guide](plugins/adlc-core/guides/claude-code.md) covers
source verification, switching an existing marketplace, updates, and removal.

### Codex CLI

```sh
codex plugin marketplace add https://github.com/Graphik-AI/adlc-skills.git --ref main --json
codex plugin add adlc-core@vecton-adlc --json
```

Start a new Codex session. Use `/skills` or type `$` and select an
`adlc-core:<name>` entry. The [Codex guide](plugins/adlc-core/guides/codex.md)
covers source verification, switching an existing marketplace, updates, and removal.

The marketplace name is `vecton-adlc`; the plugin is `adlc-core`.
Changing the repository name does not change these installation selectors.

## What is included

The plugin contains 17 selected workflows and four conditional helpers,
with a shared contract, templates, a safe repository scanner, and a waiting example.
It has no hooks, automatic installers, telemetry, bundled MCP servers, or application services.
The host and your project supply their own tools, authentication, and runtimes.

See the [package README](plugins/adlc-core/README.md),
[catalog](plugins/adlc-core/CATALOG.md), and
[verification record](plugins/adlc-core/VERIFICATION.md).
Version `0.1.0` identifies the initial package; this repository has no numbered
GitHub release yet. Installation/discovery checks do not prove execution of every workflow.
The [ADLC documentation site](https://adlc.vecton.ai/) provides scenario playbooks.

## License and acknowledgements

Vecton original material is licensed under [MIT](LICENSE).
Imported material retains its own MIT or Apache-2.0 terms, copyright, notices,
and credits. See [acknowledgements](UPSTREAMS.md),
[full source notices](plugins/adlc-core/NOTICES.md), and
[the per-file source manifest](plugins/adlc-core/sync-sources.json).

## Maintain the package

This repository owns the installable package and marketplace catalogs.
Review upstream changes and preserve their source identities and original hashes.
After reviewing changed bytes, refresh packaged hashes and run the local checks:

```sh
python3 scripts/check_package.py --refresh-hashes
make check
```

Checks require Python 3.12+ and Node 22 with native TypeScript stripping.
They use synthetic local fixtures and no external services. Tests retain their
disposable temporary directories for inspection.
See [maintenance guidance](plugins/adlc-core/README.md#sources-and-maintenance)
and [security reporting](SECURITY.md).
