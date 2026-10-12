"""Exercise package validation against concrete damaged candidate copies."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('check_package', SOURCE / 'scripts/check_package.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class PackageValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        # Retain disposable copies for inspection; never mutate the real candidate.
        self.root = Path(tempfile.mkdtemp(prefix='adlc-package-test-'))
        for rel in ('plugins/adlc-core', '.claude-plugin', '.agents'):
            shutil.copytree(SOURCE / rel, self.root / rel)
        for rel in ('AGENTS.md', 'README.md', 'UPSTREAMS.md', 'SECURITY.md', 'LICENSE'):
            shutil.copy2(SOURCE / rel, self.root / rel)
        self.old_root, self.old_package = checker.ROOT, checker.PACKAGE
        checker.ROOT = self.root
        checker.PACKAGE = self.root / 'plugins/adlc-core'

    def tearDown(self) -> None:
        checker.ROOT, checker.PACKAGE = self.old_root, self.old_package

    def test_accepts_current_candidate(self) -> None:
        self.assertEqual(checker.validate(), [])

    def test_rejects_changed_bytes_without_reviewed_hash(self) -> None:
        path = checker.PACKAGE / 'skills/tdd/tests.md'
        path.write_text(path.read_text() + '\nUnreviewed change.\n')
        self.assertTrue(any('Packaged hash mismatch: skills/tdd/tests.md' in e for e in checker.validate()))

    def test_rejects_version_mismatch(self) -> None:
        path = checker.PACKAGE / '.codex-plugin/plugin.json'
        data = json.loads(path.read_text())
        data['version'] = '9.0.0'
        path.write_text(json.dumps(data))
        self.assertTrue(any('identity/version mismatch' in e for e in checker.validate()))

    def test_rejects_escaping_support_reference(self) -> None:
        path = checker.PACKAGE / 'skills/implement/SKILL.md'
        path.write_text(path.read_text() + '\n[External required support](../../../../GLOSSARY.md)\n')
        self.assertTrue(any('Package link escapes' in e for e in checker.validate()))

    def test_rejects_missing_explicit_only_policy(self) -> None:
        path = checker.PACKAGE / 'skills/implement/agents/openai.yaml'
        path.write_text('interface:\n  display_name: "Implement"\n')
        self.assertTrue(any('implement: missing Codex explicit-only policy' in e for e in checker.validate()))

    def test_rejects_commented_false_with_active_true_policy(self) -> None:
        path = checker.PACKAGE / 'skills/implement/agents/openai.yaml'
        path.write_text('# allow_implicit_invocation: false\npolicy:\n  allow_implicit_invocation: true\n')
        checker.refresh_hashes()
        self.assertTrue(any('implement: missing Codex explicit-only policy' in e for e in checker.validate()))

    def test_rejects_path_segment_as_immutable_commit(self) -> None:
        path = checker.PACKAGE / 'sync-sources.json'
        data = json.loads(path.read_text())
        next(r for r in data['files'] if r['path'] == 'notices/Cursor-MIT.txt')['revision'] = 'cursor-team-kit'
        path.write_text(json.dumps(data))
        self.assertTrue(any('Invalid immutable commit identity: notices/Cursor-MIT.txt' in e for e in checker.validate()))


if __name__ == '__main__':
    unittest.main()
