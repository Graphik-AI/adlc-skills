"""Public scanner CLI checks using disposable synthetic repositories."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCANNER = Path(__file__).resolve().parents[1] / "plugins/adlc-core/skills/acquire-codebase-knowledge/scripts/scan.py"


class ScannerTests(unittest.TestCase):
    def setUp(self):
        # Retain fixtures for inspection; the host may trash these exact directories.
        self.fixture = Path(tempfile.mkdtemp(prefix="adlc-scanner-test-"))
        self.project = self.fixture / "project"
        self.project.mkdir()

    def write(self, path, text):
        target = self.project / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)
        return target

    def scan(self, *arguments, cwd=None, env=None):
        return subprocess.run(
            [sys.executable, str(SCANNER), *arguments], cwd=cwd or self.project,
            env=env, capture_output=True, text=True, timeout=20,
        )

    def git(self, *arguments):
        environment = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
        environment.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT="0")
        result = subprocess.run(
            ["git", "-c", "user.name=Synthetic", "-c", "user.email=synthetic@example.invalid",
             "-c", f"core.hooksPath={os.devnull}", "-c", "commit.gpgSign=false",
             "-c", "tag.gpgSign=false", "-c", "init.templateDir=", *arguments],
            cwd=self.project, env=environment, capture_output=True, text=True, timeout=5,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result

    def test_structure_survives_without_sensitive_contents(self):
        secret = "SYNTHETIC_VALUE_MUST_NOT_APPEAR_72"
        self.write("package.json", json.dumps({"scripts": {"start": secret}, "workspaces": ["packages/*"]}))
        self.write(".env.example", f"API_TOKEN={secret}\n# {secret}\nexport PORT=1234\n")
        self.write(".env", secret)
        self.write("src/main.py", f"# TODO {secret}\nprint('hello')\n")
        self.write(".github/workflows/check.yml", f"token: {secret}\n")
        self.write("Dockerfile", f"ENV TOKEN={secret}\n")
        result = self.scan()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn(secret, result.stdout + result.stderr)
        for expected in ("Found: package.json", "--- .env.example ---",
                         "src/main.py:1: TODO [text omitted]", "CI/CD: GitHub Actions", "Container: Docker found", "Python"):
            self.assertIn(expected, result.stdout)
        self.assertNotIn("1234", result.stdout)
        self.assertNotIn("API_TOKEN", result.stdout)
        self.assertNotIn("PORT", result.stdout)

    def test_multiline_template_payload_is_not_reported_as_a_variable(self):
        payload = "U1lOVEhFVElDX1NFQ1JFVA=="
        self.write(".env.example", f'CERT="-----BEGIN PRIVATE KEY-----\n{payload}\n-----END PRIVATE KEY-----"\n')
        result = self.scan()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("--- .env.example ---", result.stdout)
        for excluded in (payload, "CERT", "PRIVATE KEY"):
            self.assertNotIn(excluded, result.stdout + result.stderr)

    def test_symlink_files_and_directories_are_not_inspected(self):
        outside = self.fixture / "outside"
        outside.mkdir()
        (outside / "external.py").write_text("# TODO EXTERNAL_SENTINEL\n")
        (self.project / "src").symlink_to(outside, target_is_directory=True)
        (self.project / "package.json").symlink_to(outside / "external.py")
        result = self.scan()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("external.py", result.stdout)
        self.assertNotIn("EXTERNAL_SENTINEL", result.stdout)
        self.assertNotIn("Found: package.json", result.stdout)
        self.assertIn("Total files scanned: 0", result.stdout)

    def test_output_rejects_escape_symlink_and_overwrite(self):
        outside = self.fixture / "outside"
        outside.mkdir()
        (self.project / "link").symlink_to(outside, target_is_directory=True)
        existing = self.write("existing.txt", "KEEP THIS")
        for target in ("../escape.txt", str(outside / "escape.txt"), "link/escape.txt", "existing.txt"):
            with self.subTest(target=target):
                self.assertEqual(self.scan("--output", target).returncode, 1)
        self.assertEqual(existing.read_text(), "KEEP THIS")
        self.assertFalse((self.fixture / "escape.txt").exists())
        self.assertFalse((outside / "escape.txt").exists())
        result = self.scan("--output", "docs/scan.txt")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("SCAN COMPLETE", (self.project / "docs/scan.txt").read_text())

    def test_git_messages_and_caller_routing_are_excluded(self):
        self.git("init", "--quiet")
        self.write("src/main.py", "print('safe')\n")
        self.git("add", "src/main.py")
        self.git("commit", "--quiet", "-m", "SYNTHETIC_COMMIT_SECRET_99")
        environment = dict(os.environ, GIT_DIR=str(self.fixture / "missing"))
        result = self.scan(env=environment)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("SYNTHETIC_COMMIT_SECRET_99", result.stdout)
        self.assertIn("GIT COMMIT IDENTITIES", result.stdout)
        self.assertIn("   1 src/main.py", result.stdout)
        nested = self.project / "nested"
        nested.mkdir()
        nested_result = self.scan(cwd=nested)
        self.assertIn("Not a git repository", nested_result.stdout)
        self.assertNotIn("src/main.py", nested_result.stdout)

    def test_partial_clone_history_does_not_fetch_missing_objects(self):
        self.git("init", "--quiet")
        self.write("src/main.py", "print('safe')\n")
        self.git("add", "src/main.py")
        self.git("commit", "--quiet", "-m", "synthetic")
        origin = self.fixture / "origin.git"
        self.git("clone", "--bare", "--quiet", str(self.project), str(origin))
        tree = self.git("rev-parse", "HEAD^{tree}").stdout.strip()
        tree_object = self.project / ".git" / "objects" / tree[:2] / tree[2:]
        tree_object.rename(self.fixture / "saved-tree-object")
        self.git("config", "remote.origin.url", origin.as_uri())
        self.git("config", "remote.origin.promisor", "true")
        self.git("config", "remote.origin.partialclonefilter", "tree:0")
        self.git("config", "extensions.partialClone", "origin")
        # A local promisor remote makes a mistaken fetch observable without network access.
        self.git("config", "protocol.file.allow", "always")
        result = self.scan()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("History unavailable", result.stdout)
        self.assertFalse(tree_object.exists())
        self.assertFalse(list((self.project / ".git" / "objects" / "pack").glob("*.pack")))

    def test_terminal_controls_in_paths_are_escaped(self):
        self.write("unsafe\x1b[31m.py", "print('safe')\n")
        result = self.scan()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("\x1b", result.stdout)
        self.assertIn("\\x1b", result.stdout)


if __name__ == "__main__":
    unittest.main()
