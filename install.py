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
import argparse, json, shutil, subprocess, sys, urllib.request
from pathlib import Path

__version__ = "1.0.0"
RAW = "https://raw.githubusercontent.com/cognis-digital/cognis-arsenal/main/MANIFEST.json"
METHODS = ("pip", "pipx", "git", "docker")

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def load_manifest() -> dict:
    local = Path(__file__).resolve().parent / "MANIFEST.json"
    if local.is_file():
        return json.loads(local.read_text(encoding="utf-8"))
    with urllib.request.urlopen(RAW, timeout=30) as r:  # noqa: S310 (pinned suite URL)
        return json.loads(r.read().decode("utf-8"))


def select(manifest: dict, target: str) -> list[dict]:
    tools = manifest["tools"]
    t = target.strip()
    if t == "all":
        return list(tools.values())
    if t in tools:
        return [tools[t]]
    low = t.lower()
    by_dom = [v for v in tools.values()
              if v["domain"].lower() == low or v["domain_label"].lower() == low]
    return by_dom


def cmd_for(tool: dict, method: str) -> str:
    return tool[method]


def do_install(tools: list[dict], method: str, dry_run: bool) -> int:
    if not tools:
        print("No matching tool or domain. Try: cognis-arsenal list", file=sys.stderr)
        return 2
    rc = 0
    for t in tools:
        cmd = cmd_for(t, method)
        print(f"==> {t['name']} ({t['domain_label']}) :: {cmd}")
        if dry_run:
            continue
        if method == "docker":
            # docker recipe is a run command, not an install — just print it
            print("    (docker recipe — copy/paste to run)")
            continue
        exe = cmd.split()[0]
        if shutil.which(exe) is None:
            print(f"    [skip] '{exe}' not found on PATH", file=sys.stderr)
            rc = rc or 1
            continue
        res = subprocess.run(cmd, shell=True)
        if res.returncode != 0:
            print(f"    [fail] {t['name']} (exit {res.returncode})", file=sys.stderr)
            rc = rc or res.returncode
    return rc


def do_list(manifest: dict) -> int:
    tools = manifest["tools"]
    doms: dict[str, list[str]] = {}
    for v in tools.values():
        doms.setdefault(v["domain_label"], []).append(v["name"])
    print(f"Cognis Arsenal — {manifest['total']} tools across {len(doms)} domains\n")
    for label in sorted(doms):
        names = sorted(doms[label])
        print(f"{label} ({len(names)})")
        for n in names:
            print(f"  {n}")
        print()
    return 0


def do_search(manifest: dict, query: str) -> int:
    q = query.lower()
    hits = [v for v in manifest["tools"].values()
            if q in v["name"].lower()
            or q in v["domain"].lower()
            or q in v["domain_label"].lower()
            or q in (v.get("desc") or "").lower()]
    if not hits:
        print(f"No matches for '{query}'.")
        return 1
    print(f"{len(hits)} match(es) for '{query}':\n")
    for v in sorted(hits, key=lambda x: x["name"]):
        desc = f" — {v['desc']}" if v.get("desc") else ""
        print(f"  {v['name']}  [{v['domain_label']}]{desc}")
        print(f"    install: {v['pip']}")
    return 0


def do_setup(dry_run: bool = False) -> int:
    """Launch the guided setup wizard, pointed at this repo's MANIFEST.json."""
    here = Path(__file__).resolve().parent
    manifest = here / "MANIFEST.json"
    try:
        import setup_wizard  # local module, stdlib-only
    except Exception:
        # Ensure the repo dir is importable, then retry.
        if str(here) not in sys.path:
            sys.path.insert(0, str(here))
        import setup_wizard  # type: ignore
    mpath = str(manifest) if manifest.is_file() else None
    return setup_wizard.run(manifest_path=mpath, dry_run=dry_run)


SUBCOMMANDS = ("list", "search", "install", "setup")


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="cognis-arsenal",
                                description="Installer + index for the Cognis Neural Suite.")
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
                method = rest[i + 1]; i += 2; continue
            if rest[i] == "--dry-run":
                dry = True; i += 1; continue
            i += 1
        if method not in METHODS:
            print(f"--method must be one of {METHODS}", file=sys.stderr)
            return 2
        manifest = load_manifest()
        return do_install(select(manifest, target), method, dry)

    args = p.parse_args(argv)
    if args.cmd == "setup":
        return do_setup(getattr(args, "dry_run", False))
    manifest = load_manifest()
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
