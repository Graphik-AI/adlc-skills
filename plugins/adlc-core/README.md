# adlc-core

Install the 21 ADLC skills from the public [adlc-skills marketplace](https://github.com/Graphik-AI/adlc-skills).
One shared skill tree serves Claude Code and Codex. The plugin is `adlc-core`,
the marketplace is `vecton-adlc`, and the package version is `0.1.0`.
No additional Vecton plugin is required.

Choose a workflow in the [catalog](CATALOG.md), then use the
[Claude Code guide](guides/claude-code.md) or [Codex guide](guides/codex.md).
The repository can be cloned anonymously over HTTPS. The host and your project
supply their own authentication, tools, runtimes, and permitted actions.
The [verification record](VERIFICATION.md) distinguishes tested behavior from
capabilities that remain unverified.

Provide the intended behavior, relevant source, constraints, permitted actions,
and observable acceptance. The [shared contract](references/adlc-contract.md)
defines proportionate workflow depth, evidence, and stopping conditions.
The package includes references, templates, a scanner, and a waiting example;
it has no hooks, telemetry, bundled MCP servers, or application services.

## Install

```sh
# Claude Code
claude plugin marketplace add https://github.com/Graphik-AI/adlc-skills.git --scope user --json
claude plugin install adlc-core@vecton-adlc --scope user --json

# Codex CLI
codex plugin marketplace add https://github.com/Graphik-AI/adlc-skills.git --ref main --json
codex plugin add adlc-core@vecton-adlc --json
```

If `vecton-adlc` already points to another source, use the host guide's source-switch
steps first. Restart the host and verify the installed source and 21 skill names.

## Acknowledgements

This package builds on Matt Pocock, Superpowers by Jesse Vincent, Cursor,
GitHub, Anthropic, and HumanLayer/Dex Horthy. See [source notices](NOTICES.md)
for their full license notices and [adaptations](ADAPTATIONS.md) for changes.
[Source identities and hashes](sync-sources.json) preserve the imported bytes.
Vecton original material is [MIT-licensed](notices/Vecton-MIT.txt); upstream
material retains its existing license and attribution.

## Sources and maintenance

The public `Graphik-AI/adlc-skills` repository is the installation source and
owner of package updates. The private ADLC project may retain a reviewed copy
for its documentation build; update that copy after reviewing public changes.

Edit the owning skill or support file, review upstream changes against the
recorded source, and preserve original hashes and upstream notices.
After reviewing changed bytes, run `python3 scripts/check_package.py --refresh-hashes`
from the repository root. Run `make check`, inspect the complete diff, and update
the changelog. Keep package version fields aligned when changing the version.
Record meaningful evidence in the existing verification files. An installation
or a version string does not prove every workflow executes or establish a tagged release.

Before updating an installation, record its source and revision. Marketplace
refresh, installed-content update, and session reload are separate steps; the
host guides describe update, removal, and recovery.
