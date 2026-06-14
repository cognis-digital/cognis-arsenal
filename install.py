#!/usr/bin/env python3
"""
cognis-arsenal — cross-platform installer + index for the Cognis Neural Suite.

Consumes MANIFEST.json (next to this file, or downloaded from the suite) and
installs tools by name, by domain, or all of them, via pip / pipx / git / docker.

Usage:
  cognis-arsenal setup                                      # guided wizard (start here)
  cognis-arsenal <tool|domain|all> [--method pip|pipx|git|docker] [--dry-run]
  cognis-arsenal list
  cognis-arsenal search <query>
  cognis-arsenal --version

Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

__version__ = "1.0.0"
RAW = "https://raw.githubusercontent.com/cognis-digital/cognis-arsenal/main/MANIFEST.json"
METHODS = ("pip", "pipx", "git", "docker")

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


# ---------------------------------------------------------------------------
# Manifest loading
# ---------------------------------------------------------------------------

def _parse_manifest(text: str, source: str) -> dict:
    """Parse and validate a MANIFEST.json payload.

    Raises ValueError with a clear message on malformed or incomplete input.
    """
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"MANIFEST.json from {source!r} is not valid JSON: {exc}"
        ) from exc
    if not isinstance(data, dict):
        raise ValueError(
            f"MANIFEST.json from {source!r}: expected a JSON object at the top level"
        )
    if "tools" not in data:
        raise ValueError(
            f"MANIFEST.json from {source!r}: missing required key 'tools'"
        )
    if not isinstance(data["tools"], dict):
        raise ValueError(
            f"MANIFEST.json from {source!r}: 'tools' must be a JSON object"
        )
    return data


def load_manifest() -> dict:
    """Load MANIFEST.json from disk or fetch it from GitHub.

    Raises:
        OSError: local file could not be read.
        ValueError: JSON is malformed or missing required keys.
        urllib.error.URLError: network failure on remote fetch.
    """
    local = Path(__file__).resolve().parent / "MANIFEST.json"
    if local.is_file():
        try:
            text = local.read_text(encoding="utf-8")
        except OSError as exc:
            raise OSError(f"Cannot read {local}: {exc}") from exc
        return _parse_manifest(text, str(local))
    # No local copy — fetch from GitHub.
    try:
        with urllib.request.urlopen(RAW, timeout=30) as r:  # noqa: S310 (pinned suite URL)
            text = r.read().decode("utf-8")
    except urllib.error.URLError as exc:
        raise urllib.error.URLError(
            f"Could not fetch MANIFEST.json from {RAW!r}: {exc.reason}"
        ) from exc
    return _parse_manifest(text, RAW)


# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------

def select(manifest: dict, target: str) -> list[dict]:
    tools = manifest.get("tools", {})
    if not isinstance(tools, dict):
        return []
    t = target.strip()
    if not t:
        return []
    if t == "all":
        return list(tools.values())
    if t in tools:
        return [tools[t]]
    low = t.lower()
    by_dom = [
        v for v in tools.values()
        if isinstance(v, dict)
        and (
            v.get("domain", "").lower() == low
            or v.get("domain_label", "").lower() == low
        )
    ]
    return by_dom


def cmd_for(tool: dict, method: str) -> str:
    if method not in tool:
        raise KeyError(
            f"Tool {tool.get('name', '?')!r} has no install recipe for method {method!r}"
        )
    return tool[method]


def do_install(tools: list[dict], method: str, dry_run: bool) -> int:
    if not tools:
        print("No matching tool or domain. Try: cognis-arsenal list", file=sys.stderr)
        return 2
    rc = 0
    for t in tools:
        if not isinstance(t, dict) or not t.get("name"):
            print("[skip] malformed tool entry in manifest", file=sys.stderr)
            rc = rc or 1
            continue
        try:
            cmd = cmd_for(t, method)
        except KeyError as exc:
            print(f"    [skip] {exc}", file=sys.stderr)
            rc = rc or 1
            continue
        print(f"==> {t['name']} ({t.get('domain_label', '?')}) :: {cmd}")
        if dry_run:
            continue
        if method == "docker":
            # docker recipe is a run command, not an install — just print it
            print("    (docker recipe — copy/paste to run)")
            continue
        parts = cmd.split()
        if not parts:
            print(f"    [skip] empty install command for {t['name']!r}", file=sys.stderr)
            rc = rc or 1
            continue
        exe = parts[0]
        if shutil.which(exe) is None:
            print(f"    [skip] '{exe}' not found on PATH", file=sys.stderr)
            rc = rc or 1
            continue
        res = subprocess.run(cmd, shell=True)  # noqa: S602
        if res.returncode != 0:
            print(f"    [fail] {t['name']} (exit {res.returncode})", file=sys.stderr)
            rc = rc or res.returncode
    return rc


def do_list(manifest: dict) -> int:
    tools = manifest.get("tools", {})
    if not tools:
        print("No tools found in manifest.", file=sys.stderr)
        return 1
    doms: dict[str, list[str]] = {}
    for v in tools.values():
        if not isinstance(v, dict):
            continue
        doms.setdefault(v.get("domain_label", "Unknown"), []).append(v.get("name", "?"))
    total = manifest.get("total", len(tools))
    print(f"Cognis Arsenal — {total} tools across {len(doms)} domains\n")
    for label in sorted(doms):
        names = sorted(doms[label])
        print(f"{label} ({len(names)})")
        for n in names:
            print(f"  {n}")
        print()
    return 0


def do_search(manifest: dict, query: str) -> int:
    if not query or not query.strip():
        print("Search query cannot be empty.", file=sys.stderr)
        return 2
    q = query.lower()
    hits = [
        v for v in manifest.get("tools", {}).values()
        if isinstance(v, dict) and (
            q in v.get("name", "").lower()
            or q in v.get("domain", "").lower()
            or q in v.get("domain_label", "").lower()
            or q in (v.get("desc") or "").lower()
        )
    ]
    if not hits:
        print(f"No matches for '{query}'.")
        return 1
    print(f"{len(hits)} match(es) for '{query}':\n")
    for v in sorted(hits, key=lambda x: x.get("name", "")):
        desc = f" — {v['desc']}" if v.get("desc") else ""
        print(f"  {v.get('name', '?')}  [{v.get('domain_label', '?')}]{desc}")
        print(f"    install: {v.get('pip', '?')}")
    return 0


def do_setup(dry_run: bool = False) -> int:
    """Launch the guided setup wizard, pointed at this repo's MANIFEST.json."""
    here = Path(__file__).resolve().parent
    manifest = here / "MANIFEST.json"
    try:
        import setup_wizard  # local module, stdlib-only  # noqa: PLC0415
    except ImportError:
        # Ensure the repo dir is importable, then retry.
        if str(here) not in sys.path:
            sys.path.insert(0, str(here))
        try:
            import setup_wizard  # type: ignore  # noqa: PLC0415
        except ImportError as exc:
            print(f"error: cannot import setup_wizard: {exc}", file=sys.stderr)
            return 1
    mpath = str(manifest) if manifest.is_file() else None
    return setup_wizard.run(manifest_path=mpath, dry_run=dry_run)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

SUBCOMMANDS = ("list", "search", "install", "setup")


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="cognis-arsenal",
        description="Installer + index for the Cognis Neural Suite.",
    )
    p.add_argument("--version", action="version", version=f"cognis-arsenal {__version__}")
    sub = p.add_subparsers(dest="cmd")
    ss = sub.add_parser("setup", help="launch the guided setup wizard (recommended)")
    ss.add_argument("--dry-run", action="store_true")
    sub.add_parser("list", help="list every tool, grouped by domain")
    sp = sub.add_parser("search", help="search tools by name/domain/description")
    sp.add_argument("query")
    si = sub.add_parser("install", help="install <tool|domain|all>")
    si.add_argument("target")
    si.add_argument("--method", choices=METHODS, default="pip")
    si.add_argument("--dry-run", action="store_true")
    return p


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    p = _build_parser()

    # Empty / help / version go straight through argparse.
    if not argv:
        p.print_help()
        return 0
    if argv[0] in ("-h", "--help", "--version"):
        p.parse_args(argv)
        return 0

    # Bare-target form (no explicit subcommand): cognis-arsenal mcpscan [--method ...] [--dry-run]
    if argv[0] not in SUBCOMMANDS:
        target = argv[0]
        method, dry = "pip", False
        rest, i = argv[1:], 0
        while i < len(rest):
            if rest[i] == "--method" and i + 1 < len(rest):
                method = rest[i + 1]
                i += 2
                continue
            if rest[i] == "--dry-run":
                dry = True
                i += 1
                continue
            i += 1
        if method not in METHODS:
            print(f"--method must be one of {METHODS}", file=sys.stderr)
            return 2
        try:
            manifest = load_manifest()
        except (OSError, ValueError, urllib.error.URLError) as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
        return do_install(select(manifest, target), method, dry)

    args = p.parse_args(argv)
    if args.cmd == "setup":
        return do_setup(getattr(args, "dry_run", False))

    try:
        manifest = load_manifest()
    except (OSError, ValueError, urllib.error.URLError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.cmd == "list":
        return do_list(manifest)
    if args.cmd == "search":
        return do_search(manifest, args.query)
    if args.cmd == "install":
        return do_install(select(manifest, args.target), args.method, args.dry_run)
    p.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
