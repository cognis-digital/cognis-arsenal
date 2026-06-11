"""Tests for the cognis-arsenal installer + manifest."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import install  # noqa: E402


def load():
    return json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8"))


class TestManifest(unittest.TestCase):
    def test_manifest_exists_and_sized(self):
        m = load()
        self.assertEqual(m["total"], len(m["tools"]))
        self.assertGreaterEqual(m["total"], 250)  # ~287 repos

    def test_every_tool_has_recipes(self):
        m = load()
        for name, t in m["tools"].items():
            for key in ("name", "domain", "domain_label", "repo_url",
                        "pip", "pipx", "git", "docker"):
                self.assertIn(key, t, f"{name} missing {key}")
            self.assertEqual(t["name"], name)
            self.assertTrue(t["repo_url"].startswith("https://github.com/cognis-digital/"))
            self.assertTrue(t["pip"].startswith("pip install cognis-"))

    def test_sources_appendix_link(self):
        m = load()
        self.assertIn("cognis-sources", m["sources_repo"])


class TestSelect(unittest.TestCase):
    def setUp(self):
        self.m = load()

    def test_select_all(self):
        self.assertEqual(len(install.select(self.m, "all")), self.m["total"])

    def test_select_by_name(self):
        sel = install.select(self.m, "mcpharden")
        self.assertEqual(len(sel), 1)
        self.assertEqual(sel[0]["name"], "mcpharden")

    def test_select_by_domain(self):
        sel = install.select(self.m, "ai-security")
        self.assertTrue(len(sel) >= 1)
        self.assertTrue(all(t["domain"] == "ai-security" for t in sel))

    def test_select_unknown(self):
        self.assertEqual(install.select(self.m, "nope-not-real"), [])


class TestCLI(unittest.TestCase):
    def test_list_exit0(self):
        self.assertEqual(install.main(["list"]), 0)

    def test_search_hit(self):
        self.assertEqual(install.main(["search", "mcp"]), 0)

    def test_search_miss(self):
        self.assertEqual(install.main(["search", "zzz-no-such-thing"]), 1)

    def test_install_dry_run(self):
        self.assertEqual(install.main(["install", "mcpharden", "--dry-run"]), 0)

    def test_bare_target_dry_run(self):
        self.assertEqual(install.main(["mcpharden", "--dry-run"]), 0)


if __name__ == "__main__":
    unittest.main()
