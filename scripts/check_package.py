#!/usr/bin/env python3
"""Validate the public ADLC package without running hosts or network operations."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'plugins/adlc-core'
SELECTED = set('wayfinder domain-modeling grill-with-docs to-spec to-tickets implement implement-spec tdd systematic-debugging code-review simplify frontend-testing-debugging pr acquire-codebase-knowledge deslop post-implementation thermo-nuclear-code-quality-review'.split())
HELPERS = {'grilling', 'research', 'prototype', 'codebase-design'}
EXPLICIT_ONLY = {'wayfinder', 'grill-with-docs', 'to-spec', 'to-tickets', 'implement', 'implement-spec', 'thermo-nuclear-code-quality-review'}
REQUIRED = {
    'domain-modeling': ['ADR-FORMAT.md', 'GLOSSARY-FORMAT.md'],
    'prototype': ['UI.md', 'LOGIC.md'],
    'tdd': ['tests.md', 'mocking.md'],
    'codebase-design': ['DEEPENING.md', 'DESIGN-IT-TWICE.md'],
    'pr': ['CREDITS.md'],
    'systematic-debugging': ['root-cause-tracing.md', 'defense-in-depth.md', 'condition-based-waiting.md', 'condition-based-waiting-example.ts'],
    'acquire-codebase-knowledge': ['scripts/scan.py', 'references/inquiry-checkpoints.md', 'references/stack-detection.md'] + [f'assets/templates/{n}.md' for n in ('ARCHITECTURE', 'CONCERNS', 'CONVENTIONS', 'INTEGRATIONS', 'STACK', 'STRUCTURE', 'TESTING')],
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_links(path: Path):
    text = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
    for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', text):
        if not urlsplit(target).scheme:
            yield unquote(target.strip('<>'))


def anchors(path: Path) -> set[str]:
    found = set()
    counts = {}
    for line in path.read_text().splitlines():
        if not re.match(r'^#{1,6} ', line):
            continue
        title = re.sub(r'^#+\s+', '', line).strip().lower()
        title = re.sub(r'[^\w\- ]', '', title).replace(' ', '-')
        count = counts.get(title, 0)
        found.add(title + (f'-{count}' if count else ''))
        counts[title] = count + 1
    return found


def explicit_policy(path: Path) -> bool:
    """Accept the package's block policy with one actual false Boolean, not comments."""
    if not path.is_file():
        return False
    lines = [line.split('#', 1)[0].rstrip() for line in path.read_text().splitlines()]
    starts = [i for i, line in enumerate(lines) if line == 'policy:']
    if len(starts) != 1:
        return False
    values = []
    for line in lines[starts[0] + 1:]:
        if line and not line.startswith(' '):
            break
        match = re.fullmatch(r'  allow_implicit_invocation: (true|false)', line)
        if match:
            values.append(match.group(1))
        elif line.strip().startswith('allow_implicit_invocation:'):
            return False
    return values == ['false']


def validate() -> list[str]:
    errors = []
    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)
    entries = {p.parent.name: p for p in (PACKAGE / 'skills').glob('*/SKILL.md')}
    require(set(entries) == SELECTED | HELPERS, 'Inventory must contain exactly the selected 17 plus four helpers')
    for name, path in entries.items():
        body = path.read_text()
        require(re.search(rf'^name: {re.escape(name)}$', body, re.M) is not None, f'{name}: frontmatter name mismatch')
        require(body.startswith('---\n') and '\ndescription:' in body, f'{name}: missing frontmatter')
        require('../../references/adlc-contract.md' in body, f'{name}: shared contract not loaded')
        policy = path.parent / 'agents/openai.yaml'
        if name in EXPLICIT_ONLY:
            frontmatter = body.split('---', 2)[1]
            require(re.search(r'^disable-model-invocation: true$', frontmatter, re.M) is not None, f'{name}: missing Claude explicit-only policy')
            require(explicit_policy(policy), f'{name}: missing Codex explicit-only policy')
        for support in REQUIRED.get(name, []):
            require((path.parent / support).is_file(), f'{name}: missing {support}')
    manifest = json.loads((PACKAGE / 'sync-sources.json').read_text())
    version = manifest['version']
    for host in ('.claude-plugin', '.codex-plugin'):
        data = json.loads((PACKAGE / host / 'plugin.json').read_text())
        require(data['name'] == 'adlc-core' and data['version'] == version, f'{host}: identity/version mismatch')
        require(data.get('skills') == './skills/', f'{host}: wrong skill root')
    claude = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
    codex = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text())
    require(claude['name'] == codex['name'] == 'vecton-adlc', 'Marketplace identities differ')
    for data in (claude, codex):
        require(len(data['plugins']) == 1, 'Unexpected marketplace inventory')
        plugin = data['plugins'][0]
        require(plugin['name'] == 'adlc-core', 'Wrong marketplace plugin')
        source = plugin['source']
        target = source['path'] if isinstance(source, dict) else source
        require(target == './plugins/adlc-core', 'Marketplace source is not portable local package')
    require(claude['plugins'][0]['version'] == version, 'Claude catalog version differs')
    require(f'## {version} ' in (PACKAGE / 'CHANGELOG.md').read_text(), 'Changelog version missing')
    records = manifest['files']
    seen = set()
    for record in records:
        rel = record['path']
        path = PACKAGE / rel
        require(rel not in seen, f'Duplicate provenance record: {rel}')
        seen.add(rel)
        require(path.resolve().is_relative_to(PACKAGE.resolve()), f'Escaping source record: {rel}')
        require(path.is_file() and not path.is_symlink(), f'Missing/linked recorded file: {rel}')
        if not path.is_file():
            continue
        require(record.get('packaged_sha256') == digest(path), f'Packaged hash mismatch: {rel}')
        require(bool(record.get('source') and record.get('revision') and record.get('author') and record.get('adaptation')), f'Incomplete provenance: {rel}')
        if record.get('revision_kind') == 'immutable-upstream-commit':
            require(bool(re.fullmatch('[0-9a-f]{40}', record['revision'])), f'Invalid immutable commit identity: {rel}')
        require(bool(re.fullmatch('[0-9a-f]{64}', record.get('original_sha256') or '')) or record.get('origin') == 'original', f'Missing original hash: {rel}')
        require((PACKAGE / record['notice']).is_file(), f'Missing notice: {rel}')
        for dependency in record.get('dependencies', []):
            require((PACKAGE / dependency).is_file(), f'Missing dependency {dependency}: {rel}')
        if rel.startswith('notices/') and rel.endswith('.txt'):
            require(record['original_sha256'] == digest(path), f'Upstream notice modified: {rel}')
    actual = {p.relative_to(PACKAGE).as_posix() for p in PACKAGE.rglob('*') if p.is_file() and p.name != 'sync-sources.json'}
    require(seen == actual, f'Provenance inventory mismatch; unrecorded={sorted(actual-seen)}, missing={sorted(seen-actual)}')
    md_files = list(PACKAGE.rglob('*.md'))
    md_files += list(ROOT.glob('*.md'))
    for path in md_files:
        for target in local_links(path):
            ref, _, anchor = target.partition('#')
            dest = (path.parent / ref).resolve() if ref else path.resolve()
            if path.is_relative_to(PACKAGE):
                require(dest.is_relative_to(PACKAGE.resolve()), f'Package link escapes: {path.relative_to(ROOT)} -> {target}')
            require(dest.exists(), f'Broken link: {path.relative_to(ROOT)} -> {target}')
            if dest.is_file() and anchor and dest.suffix == '.md':
                require(anchor in anchors(dest), f'Broken anchor: {path.relative_to(ROOT)} -> {target}')
    for path in PACKAGE.rglob('*'):
        require(not path.is_symlink(), f'Package symlink: {path}')
        if not path.is_file() or path.suffix not in {'.md', '.yaml', '.json', '.py', '.ts'} or path.name == 'sync-sources.json':
            continue
        body = path.read_text()
        require('/Users/' not in body and '/home/' not in body, f'Machine-local path: {path.relative_to(PACKAGE)}')
        if path.is_relative_to(PACKAGE / 'skills'):
            require('superpowers:' not in body and '/setup-matt-pocock-skills' not in body, f'Hidden skill dependency: {path.relative_to(PACKAGE)}')
    return errors


def refresh_hashes() -> None:
    path = PACKAGE / 'sync-sources.json'
    data = json.loads(path.read_text())
    for record in data['files']:
        packaged = PACKAGE / record['path']
        record['packaged_sha256'] = digest(packaged)
    path.write_text(json.dumps(data, indent=2) + '\n')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh-hashes', action='store_true', help='Refresh only packaged hashes after reviewing changes; original hashes remain immutable')
    args = parser.parse_args()
    if args.refresh_hashes:
        refresh_hashes()
    errors = validate()
    if errors:
        print('\n'.join(errors))
        return 1
    print('ADLC checks passed: 21 skills, manifests/catalogs, dependency/support closure, links, source records, hashes and notices')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
