#!/usr/bin/env python3
"""
gen_arsenal.py — re-runnable generator for the Cognis Arsenal full-kit index.

Pulls the LIVE repo list from github.com/cognis-digital, maps each repo to a
domain using the local tools tree (mirrors make_manifest.py), and emits:

  MANIFEST.json   every tool {name, domain, repo_url, desc, pip, pipx, git, docker}
  README.md       categorized arsenal index — domain sections, per-tool desc +
                  repo link + copy-paste install commands, hero, shields, the
                  Resources appendix, and bootstrap one-liners.

Stdlib only. Run anytime the repo count changes:  python gen_arsenal.py
"""
from __future__ import annotations
import collections, json, subprocess, sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parent
SRC = Path(r"C:\Users\user\Desktop\cognis-digital-v5\cognis-digital-v5")
GH = r"C:\Program Files\GitHub CLI\gh.exe"
ORG = "cognis-digital"
RAW = f"https://raw.githubusercontent.com/{ORG}/cognis-arsenal/master"

PRETTY = {
    "ai-agent": "AI Agents & LLMOps", "ai-security": "AI Security & Governance",
    "appsec": "Application Security", "bizdev": "Business Development",
    "blue-team": "Blue Team", "business": "Business Ops", "compliance": "Compliance & GRC",
    "data": "Data & Datasets", "defense": "Defense Tech", "dev-supply-chain": "Supply Chain Security",
    "devtools": "Developer Tools", "federal": "Federal & Compliance", "fintech": "FinTech",
    "healthcare": "Healthcare", "info-integrity": "Information Integrity", "iot": "IoT / OT",
    "network": "Network Security", "ops": "DevOps & Observability", "osint": "OSINT",
    "privacy": "Privacy", "red-team": "Red Team", "secops": "Security Operations",
    "tactical": "Tactical", "web3": "Web3",
}
ORDER = ["Flagship", "ai-security", "ai-agent", "blue-team", "red-team", "secops", "appsec",
         "osint", "federal", "compliance", "privacy", "network", "info-integrity",
         "dev-supply-chain", "devtools", "data", "ops", "business", "bizdev", "fintech",
         "healthcare", "iot", "web3", "defense", "tactical", "Defense & IC", "Meta / Suite",
         "Other / Resources", "Launcher"]


def live_repos():
    """Pull every repo from gh; fall back to cached repos.json on failure."""
    try:
        out = subprocess.run([GH, "repo", "list", ORG, "--limit", "400",
                              "--json", "name,description,url"],
                             capture_output=True, text=True, timeout=120)
        if out.returncode == 0 and out.stdout.strip():
            data = json.loads(out.stdout)
            (ROOT / "repos.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
            return data
    except Exception as e:
        print(f"[warn] gh failed ({e}); using cached repos.json", file=sys.stderr)
    return json.loads((ROOT / "repos.json").read_text(encoding="utf-8"))


def domain_map():
    """name(lower) -> domain, from the local source tree (mirrors make_manifest)."""
    dm = {}
    tools = SRC / "tools"
    if tools.is_dir():
        for dom in tools.iterdir():
            if dom.is_dir() and not dom.name.startswith("_"):
                for s in dom.iterdir():
                    if s.is_dir():
                        dm[s.name.lower()] = dom.name
    for sub, lab in [("_mil", "Defense & IC"), ("_meta", "Meta / Suite"),
                     ("_extra", "Flagship"), ("launcher", "Launcher")]:
        b = SRC / sub
        if b.is_dir():
            for s in b.iterdir():
                if s.is_dir() and s.name.lower() not in dm:
                    dm[s.name.lower()] = lab
    return dm


def recipes(name: str) -> dict:
    """Install-recipe strings for a single tool/repo."""
    git_url = f"https://github.com/{ORG}/{name}.git"
    return {
        "pip": f"pip install cognis-{name}",
        "pipx": f"pipx install git+{git_url}",
        "git": f"pip install git+{git_url}",
        "docker": f"docker run --rm ghcr.io/{ORG}/{name}:latest --help",
    }


def build_manifest():
    repos = {r["name"]: r for r in live_repos()}
    dm = domain_map()
    tools = {}
    for name, r in sorted(repos.items()):
        dom = dm.get(name.lower(), "Other / Resources")
        tools[name] = {
            "name": name,
            "domain": dom,
            "domain_label": PRETTY.get(dom, dom),
            "desc": (r.get("description") or "").strip(),
            "repo_url": r.get("url") or f"https://github.com/{ORG}/{name}",
            **recipes(name),
        }
    return tools


def write_manifest(tools: dict):
    payload = {
        "org": ORG,
        "raw_base": RAW,
        "total": len(tools),
        "sources_repo": f"https://github.com/{ORG}/cognis-sources",
        "tools": tools,
    }
    (ROOT / "MANIFEST.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload


def write_readme(tools: dict):
    groups = collections.defaultdict(list)
    for t in tools.values():
        groups[t["domain"]].append(t)
    total = len(tools)
    doms = [d for d in ORDER if d in groups] + [d for d in sorted(groups) if d not in ORDER]

    o = []
    a = o.append
    a("# Cognis Arsenal")
    a("")
    a("> **The single full-kit entry point to the entire [Cognis Neural Suite](https://github.com/cognis-digital).**")
    a("> Think *Hiren's BootCD PE*, but for the suite — every tool, one kit, multi-language installers.")
    a("")
    a(f"[![Tools](https://img.shields.io/badge/tools-{total}-2b6cb0.svg)](MANIFEST.json)")
    a(f"[![Domains](https://img.shields.io/badge/domains-{len(doms)}-6b46c1.svg)](#arsenal-index)")
    a("[![License: COCL 1.0](https://img.shields.io/badge/License-COCL%201.0-2b6cb0.svg)](LICENSE)")
    a(f"[![Suite](https://img.shields.io/badge/Cognis-Neural%20Suite-6b46c1.svg)](https://github.com/{ORG})")
    a("[![CI](https://github.com/cognis-digital/cognis-arsenal/actions/workflows/ci.yml/badge.svg)](https://github.com/cognis-digital/cognis-arsenal/actions)")
    a("")
    a(f"The Cognis Neural Suite is **{total} public, single-purpose, self-hostable, MCP-native tools** "
      f"across **{len(doms)} domains**. This repo is the one place to discover and install all of them — "
      "from one tool to an entire domain to the whole arsenal — using whatever package manager you already speak.")
    a("")
    # ---- recommended: guided wizard (TOP of the doc) ----
    a("## Get started — just run the wizard")
    a("")
    a("**New here? Don't memorize anything. Run the guided setup wizard:**")
    a("")
    a("```bash")
    a("python install.py setup")
    a("```")
    a("")
    a("It detects your OS and install backends (pip/pipx/git/docker), explains each step "
      "at your chosen depth, and lets you install the starter bundle, browse by domain, "
      "pick individual tools, or the whole suite — every command is shown and confirmed before it runs. "
      "Use `--dry-run` to preview without installing.")
    a("")
    a("One-line bootstrap (no checkout needed):")
    a("")
    a("```bash")
    a(f"curl -fsSL {RAW}/setup.sh | bash          # Linux / macOS")
    a("```")
    a("")
    a("```powershell")
    a(f"irm {RAW}/setup.ps1 | iex                 # Windows PowerShell")
    a("```")
    a("")
    a("After `pip install`, the same wizard is the `setup` subcommand:")
    a("")
    a("```bash")
    a("cognis-arsenal setup")
    a("```")
    a("")
    # ---- bootstrap one-liners ----
    a("## Bootstrap (one-liners)")
    a("")
    a("**Linux / macOS** — install a single tool (e.g. `mcpscan`):")
    a("")
    a("```bash")
    a(f"curl -fsSL {RAW}/install.sh | bash -s -- mcpscan")
    a("```")
    a("")
    a("**Windows PowerShell** — pull the installer and run it:")
    a("")
    a("```powershell")
    a(f"irm {RAW}/install.ps1 | iex")
    a("```")
    a("")
    a("**Cross-platform (Python)** — installs the `cognis-arsenal` console entry, then drives everything:")
    a("")
    a("```bash")
    a(f"pip install git+https://github.com/{ORG}/cognis-arsenal.git")
    a("cognis-arsenal list")
    a("cognis-arsenal search mcp")
    a("cognis-arsenal install mcpscan          # one tool")
    a("cognis-arsenal install ai-security       # a whole domain")
    a("cognis-arsenal install all --method pipx # the entire arsenal, via pipx")
    a("```")
    a("")
    # ---- usage ----
    a("## Installers")
    a("")
    a("Three installers, one `MANIFEST.json`. Each accepts a target of `<tool>`, `<domain>`, or `all`, "
      "plus `--method pip|pipx|git|docker`, and the `list` / `search` subcommands.")
    a("")
    a("| Platform | Installer | Example |")
    a("|---|---|---|")
    a("| Linux / macOS | `install.sh` | `./install.sh mcpscan --method pipx` |")
    a("| Windows | `install.ps1` | `.\\install.ps1 ai-security` |")
    a("| Any (Python) | `install.py` | `python install.py search osint` |")
    a("")
    a("```text")
    a("install.(sh|ps1|py) <tool|domain|all> [--method pip|pipx|git|docker]")
    a("install.(sh|ps1|py) list                  # list every tool + domain")
    a("install.(sh|ps1|py) search <query>        # match name/domain/description")
    a("```")
    a("")
    a("`pip` (default) installs the published `cognis-<tool>` package; `git` installs from source; "
      "`pipx` isolates each CLI; `docker` prints the container run command.")
    a("")
    # ---- arsenal index ----
    a("## Arsenal index")
    a("")
    a("_Per-domain counts:_ " + " · ".join(
        f"[{PRETTY.get(d, d)}](#{anchor(PRETTY.get(d, d))}) ({len(groups[d])})" for d in doms))
    a("")
    for d in doms:
        label = PRETTY.get(d, d)
        items = sorted(groups[d], key=lambda t: t["name"])
        a(f"### {label} ({len(items)})")
        a("")
        for t in items:
            desc = f" — {t['desc']}" if t["desc"] else ""
            a(f"- **[{t['name']}]({t['repo_url']})**{desc}")
            a(f"  ```bash")
            a(f"  cognis-arsenal install {t['name']}   # {t['pip']}")
            a(f"  ```")
        a("")
    # ---- resources appendix ----
    a("## Resources")
    a("")
    a(f"- **Suite hub:** [github.com/{ORG}](https://github.com/{ORG}) — all {total} repositories")
    a(f"- **Curated sources & datasets:** [github.com/{ORG}/cognis-sources](https://github.com/{ORG}/cognis-sources)")
    a(f"- **Machine-readable index:** [`MANIFEST.json`](MANIFEST.json)")
    a("- **Cognis.Studio:** [cognis.studio](https://cognis.studio) — agents call every tool over MCP")
    a("- **Cognis Digital:** [cognis.digital](https://cognis.digital)")
    a("")
    a("## License")
    a("")
    a("Source-available under the **Cognis Open Collaboration License (COCL) v1.0** — free for personal, "
      "internal-evaluation, research, and educational use; **commercial / production use requires a license** "
      "(licensing@cognis.digital). See [LICENSE](LICENSE).")
    a("")
    a("## About")
    a("")
    a("**[Cognis Digital](https://cognis.digital)** — Wyoming, USA · "
      "*Making Tomorrow Better Today: Advanced Cybersecurity, AI Innovation, and Blockchain Expertise.*")
    a("")
    (ROOT / "README.md").write_text("\n".join(o), encoding="utf-8")
    return total, len(doms)


def anchor(label: str) -> str:
    out = []
    for ch in label.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in " -":
            out.append("-")
    return "".join(out)


def main():
    tools = build_manifest()
    write_manifest(tools)
    total, ndoms = write_readme(tools)
    print(f"TOTAL tools: {total}  ·  domains: {ndoms}")
    print(f"wrote: {ROOT / 'MANIFEST.json'}")
    print(f"wrote: {ROOT / 'README.md'}")


if __name__ == "__main__":
    main()
