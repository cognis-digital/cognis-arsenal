"""Tests for the cognis-arsenal installer + manifest."""
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

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


# ---------------------------------------------------------------------------
# Hardening tests — error paths, edge cases, bad input
# ---------------------------------------------------------------------------

class TestParseManifest(unittest.TestCase):
    """_parse_manifest raises ValueError on malformed input."""

    def test_invalid_json_raises(self):
        with self.assertRaises(ValueError) as ctx:
            install._parse_manifest("{not valid json", "test-source")
        self.assertIn("not valid JSON", str(ctx.exception))

    def test_non_object_raises(self):
        with self.assertRaises(ValueError) as ctx:
            install._parse_manifest("[1, 2, 3]", "test-source")
        self.assertIn("JSON object", str(ctx.exception))

    def test_missing_tools_key_raises(self):
        with self.assertRaises(ValueError) as ctx:
            install._parse_manifest('{"org": "x"}', "test-source")
        self.assertIn("'tools'", str(ctx.exception))

    def test_tools_not_object_raises(self):
        with self.assertRaises(ValueError) as ctx:
            install._parse_manifest('{"tools": [1, 2]}', "test-source")
        self.assertIn("'tools' must be a JSON object", str(ctx.exception))

    def test_valid_minimal_manifest_ok(self):
        data = install._parse_manifest('{"tools": {}}', "test-source")
        self.assertEqual(data["tools"], {})


class TestLoadManifestMissing(unittest.TestCase):
    """load_manifest raises OSError when the local file is unreadable."""

    def test_missing_local_file_falls_through_to_network(self):
        # When local MANIFEST.json does NOT exist, load_manifest tries the network.
        # We can't rely on network in tests, so we patch urlopen to raise an error
        # and verify a URLError is raised (not a crash/traceback).
        import urllib.error
        with patch("install.Path.is_file", return_value=False):
            with patch("urllib.request.urlopen",
                       side_effect=urllib.error.URLError("mock network error")):
                with self.assertRaises(urllib.error.URLError):
                    install.load_manifest()


class TestSelectEdgeCases(unittest.TestCase):
    """select() handles unusual inputs without raising."""

    def _minimal_manifest(self, extra_tools=None):
        tools = {
            "mytool": {
                "name": "mytool",
                "domain": "appsec",
                "domain_label": "Application Security",
            }
        }
        if extra_tools:
            tools.update(extra_tools)
        return {"tools": tools}

    def test_empty_target_returns_empty(self):
        m = self._minimal_manifest()
        self.assertEqual(install.select(m, ""), [])

    def test_whitespace_target_returns_empty(self):
        m = self._minimal_manifest()
        self.assertEqual(install.select(m, "   "), [])

    def test_missing_tools_key_returns_empty(self):
        self.assertEqual(install.select({}, "all"), [])

    def test_all_returns_every_tool(self):
        m = self._minimal_manifest()
        result = install.select(m, "all")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "mytool")

    def test_domain_label_match_case_insensitive(self):
        m = self._minimal_manifest()
        result = install.select(m, "APPLICATION SECURITY")
        self.assertEqual(len(result), 1)

    def test_malformed_tool_entry_skipped(self):
        # A non-dict value in tools should not blow up select()
        m = {"tools": {"bad": "not-a-dict", "good": {
            "name": "good", "domain": "appsec", "domain_label": "Application Security"
        }}}
        # Selecting "all" should return both (including the non-dict one) — select
        # doesn't filter, it just returns values. The install loop handles malformed entries.
        result = install.select(m, "all")
        self.assertEqual(len(result), 2)


class TestDoInstallEdgeCases(unittest.TestCase):
    """do_install() handles missing method keys and empty tool list."""

    def test_empty_tools_returns_2(self):
        rc = install.do_install([], "pip", dry_run=True)
        self.assertEqual(rc, 2)

    def test_tool_missing_method_key_skips_gracefully(self):
        # A tool entry that lacks the requested method key should not raise.
        # Ask for a method not in the dict -> skip, non-zero rc
        tool_no_docker = {"name": "nodockertool", "domain_label": "Test",
                          "pip": "pip install x", "pipx": "pipx install x", "git": "pip install x"}
        rc = install.do_install([tool_no_docker], "docker", dry_run=False)
        self.assertNotEqual(rc, 0)  # should report failure, not crash

    def test_dry_run_never_executes(self):
        tool = {"name": "mytool", "domain_label": "Test",
                "pip": "pip install cognis-mytool",
                "pipx": "pipx install x", "git": "pip install x",
                "docker": "docker run x"}
        # If dry_run, subprocess.run should never be called.
        with patch("subprocess.run") as mock_run:
            rc = install.do_install([tool], "pip", dry_run=True)
        mock_run.assert_not_called()
        self.assertEqual(rc, 0)

    def test_malformed_tool_dict_skipped(self):
        rc = install.do_install([{"no_name_key": True}], "pip", dry_run=True)
        self.assertEqual(rc, 1)


class TestDoSearchEdgeCases(unittest.TestCase):
    """do_search() validates empty query and handles empty manifest."""

    def _manifest(self):
        return load()

    def test_empty_query_returns_2(self):
        rc = install.do_search(self._manifest(), "")
        self.assertEqual(rc, 2)

    def test_whitespace_query_returns_2(self):
        rc = install.do_search(self._manifest(), "   ")
        self.assertEqual(rc, 2)

    def test_empty_tools_returns_1(self):
        rc = install.do_search({"tools": {}}, "anything")
        self.assertEqual(rc, 1)


class TestDoListEdgeCases(unittest.TestCase):
    """do_list() handles empty tools gracefully."""

    def test_empty_tools_returns_1(self):
        rc = install.do_list({"tools": {}, "total": 0})
        self.assertEqual(rc, 1)


class TestMainManifestError(unittest.TestCase):
    """main() surfaces manifest load errors as exit code 2 (no traceback)."""

    def test_manifest_load_error_exits_2_for_list(self):
        with patch("install.load_manifest", side_effect=ValueError("bad json")):
            rc = install.main(["list"])
        self.assertEqual(rc, 2)

    def test_manifest_load_error_exits_2_for_install(self):
        with patch("install.load_manifest", side_effect=OSError("no file")):
            rc = install.main(["install", "anything", "--dry-run"])
        self.assertEqual(rc, 2)

    def test_manifest_load_error_exits_2_for_bare_target(self):
        with patch("install.load_manifest", side_effect=ValueError("bad json")):
            rc = install.main(["sometool", "--dry-run"])
        self.assertEqual(rc, 2)

    def test_bad_method_exits_2(self):
        rc = install.main(["sometool", "--method", "ftp"])
        self.assertEqual(rc, 2)


if __name__ == "__main__":
    unittest.main()
