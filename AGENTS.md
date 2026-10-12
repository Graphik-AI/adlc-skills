# Repository purpose

This public repository owns the installable `adlc-core` skill package for
Claude Code and Codex and the `vecton-adlc` marketplace catalogs.
Start with README.md, plugins/adlc-core/CATALOG.md, and the owning skill.

## Maintenance

Preserve the 21 selected skill names, host manifests, relative support links,
upstream notices, credits, immutable original hashes, and source qualifications.
Do not overwrite adapted files from a global installation. Review source updates
before running `python3 scripts/check_package.py --refresh-hashes`.
Run `make check` after implementation, manifest, helper, or package changes.
Python 3.12+ and Node 22 with native TypeScript stripping are required; checks
use synthetic local fixtures and no external services.

Keep checks proportional to the affected behavior. Installation/discovery is
separate from workflow execution, and a package version is separate from a tagged release.
Document material verification limits. Use the appropriate authorized browser
profile for real UI work; unavailable access does not authorize a substitute.

## Publication boundary

Do not add private project records, developer research, transcripts, survey
responses, credentials, local-machine paths, deployment secrets, or customer data.
Preserve unrelated user changes and stage only files in scope.
Vecton original material is MIT-licensed; upstream material keeps its own terms.
Do not add agent authorship or co-authorship to commits.
Use recoverable deletion through `/usr/bin/trash`; never use `rm`.
