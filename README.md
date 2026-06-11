# Cognis Arsenal

> **The single full-kit entry point to the entire [Cognis Neural Suite](https://github.com/cognis-digital).**
> Think *Hiren's BootCD PE*, but for the suite — every tool, one kit, multi-language installers.

[![Tools](https://img.shields.io/badge/tools-287-2b6cb0.svg)](MANIFEST.json)
[![Domains](https://img.shields.io/badge/domains-28-6b46c1.svg)](#arsenal-index)
[![License: COCL 1.0](https://img.shields.io/badge/License-COCL%201.0-2b6cb0.svg)](LICENSE)
[![Suite](https://img.shields.io/badge/Cognis-Neural%20Suite-6b46c1.svg)](https://github.com/cognis-digital)
[![CI](https://github.com/cognis-digital/cognis-arsenal/actions/workflows/ci.yml/badge.svg)](https://github.com/cognis-digital/cognis-arsenal/actions)

The Cognis Neural Suite is **287 public, single-purpose, self-hostable, MCP-native tools** across **28 domains**. This repo is the one place to discover and install all of them — from one tool to an entire domain to the whole arsenal — using whatever package manager you already speak.

## Bootstrap (one-liners)

**Linux / macOS** — install a single tool (e.g. `mcpscan`):

```bash
curl -fsSL https://raw.githubusercontent.com/cognis-digital/cognis-arsenal/main/install.sh | bash -s -- mcpscan
```

**Windows PowerShell** — pull the installer and run it:

```powershell
irm https://raw.githubusercontent.com/cognis-digital/cognis-arsenal/main/install.ps1 | iex
```

**Cross-platform (Python)** — installs the `cognis-arsenal` console entry, then drives everything:

```bash
pip install git+https://github.com/cognis-digital/cognis-arsenal.git
cognis-arsenal list
cognis-arsenal search mcp
cognis-arsenal install mcpscan          # one tool
cognis-arsenal install ai-security       # a whole domain
cognis-arsenal install all --method pipx # the entire arsenal, via pipx
```

## Installers

Three installers, one `MANIFEST.json`. Each accepts a target of `<tool>`, `<domain>`, or `all`, plus `--method pip|pipx|git|docker`, and the `list` / `search` subcommands.

| Platform | Installer | Example |
|---|---|---|
| Linux / macOS | `install.sh` | `./install.sh mcpscan --method pipx` |
| Windows | `install.ps1` | `.\install.ps1 ai-security` |
| Any (Python) | `install.py` | `python install.py search osint` |

```text
install.(sh|ps1|py) <tool|domain|all> [--method pip|pipx|git|docker]
install.(sh|ps1|py) list                  # list every tool + domain
install.(sh|ps1|py) search <query>        # match name/domain/description
```

`pip` (default) installs the published `cognis-<tool>` package; `git` installs from source; `pipx` isolates each CLI; `docker` prints the container run command.

## Arsenal index

_Per-domain counts:_ [Flagship](#flagship) (19) · [AI Security & Governance](#ai-security--governance) (17) · [AI Agents & LLMOps](#ai-agents--llmops) (9) · [Blue Team](#blue-team) (6) · [Red Team](#red-team) (5) · [Security Operations](#security-operations) (30) · [Application Security](#application-security) (10) · [OSINT](#osint) (6) · [Federal & Compliance](#federal--compliance) (6) · [Compliance & GRC](#compliance--grc) (8) · [Privacy](#privacy) (7) · [Network Security](#network-security) (3) · [Information Integrity](#information-integrity) (4) · [Supply Chain Security](#supply-chain-security) (4) · [Developer Tools](#developer-tools) (10) · [Data & Datasets](#data--datasets) (8) · [DevOps & Observability](#devops--observability) (6) · [Business Ops](#business-ops) (10) · [Business Development](#business-development) (10) · [FinTech](#fintech) (10) · [Healthcare](#healthcare) (10) · [IoT / OT](#iot--ot) (10) · [Web3](#web3) (10) · [Defense Tech](#defense-tech) (15) · [Tactical](#tactical) (30) · [Defense & IC](#defense--ic) (12) · [Meta / Suite](#meta--suite) (3) · [Other / Resources](#other--resources) (9)

### Flagship (19)

- **[agentpassport](https://github.com/cognis-digital/agentpassport)** — Verifiable AI-agent identity + multi-hop delegation chains anchored to a human principal (the unsolved 2026 agent-auth gap)
  ```bash
  cognis-arsenal install agentpassport   # pip install cognis-agentpassport
  ```
- **[cloud-setups](https://github.com/cognis-digital/cloud-setups)** — Firebase, GCP, and Azure project setups â€” bootstrap, deploy, IaC, and emulators, merged and rebranded
  ```bash
  cognis-arsenal install cloud-setups   # pip install cognis-cloud-setups
  ```
- **[cognis-code](https://github.com/cognis-digital/cognis-code)** — Local uncensored AI coding suite â€” one endpoint wired into VS Code, JetBrains, Cursor, Zed, Neovim, opencode, and Aider
  ```bash
  cognis-arsenal install cognis-code   # pip install cognis-cognis-code
  ```
- **[cognis-devbox](https://github.com/cognis-digital/cognis-devbox)** — Custom dev OS image (Packer/KVM/Vagrant/cloud-init) with every language + cloud + AI tool preinstalled
  ```bash
  cognis-arsenal install cognis-devbox   # pip install cognis-cognis-devbox
  ```
- **[cognis-operations](https://github.com/cognis-digital/cognis-operations)** — How an agentic company runs â€” Cognis Digital's 4-layer operating model, org chart, agent registry, and governance
  ```bash
  cognis-arsenal install cognis-operations   # pip install cognis-cognis-operations
  ```
- **[cognis-sources](https://github.com/cognis-digital/cognis-sources)** — Curated index of 10k+ public technical & research links (privacy-filtered)
  ```bash
  cognis-arsenal install cognis-sources   # pip install cognis-cognis-sources
  ```
- **[compliance-atlas](https://github.com/cognis-digital/compliance-atlas)** — Condensed, cross-walked reference for SOC2, ISO 27001, NIST CSF/800-53/800-171, CMMC, GDPR, CCPA, HIPAA, PCI DSS, EU AI Act
  ```bash
  cognis-arsenal install compliance-atlas   # pip install cognis-compliance-atlas
  ```
- **[hermes](https://github.com/cognis-digital/hermes)** — Model-agnostic, portable long-term memory framework for AI agents (MCP-native)
  ```bash
  cognis-arsenal install hermes   # pip install cognis-hermes
  ```
- **[locateanything](https://github.com/cognis-digital/locateanything)** — Infer where a photo was taken using a local uncensored vision + reasoning model (OSINT/geoint, 100% local)
  ```bash
  cognis-arsenal install locateanything   # pip install cognis-locateanything
  ```
- **[mcpify](https://github.com/cognis-digital/mcpify)** — Turn any command-line tool into an MCP server â€” one line, zero boilerplate
  ```bash
  cognis-arsenal install mcpify   # pip install cognis-mcpify
  ```
- **[omni-install](https://github.com/cognis-digital/omni-install)** — One menu to install every language, cloud CLI, container, and AI tool â€” Linux/macOS/Windows
  ```bash
  cognis-arsenal install omni-install   # pip install cognis-omni-install
  ```
- **[privacyspoof](https://github.com/cognis-digital/privacyspoof)** — AdGuard/uBlock blocklists + UA/geo/cookie/session spoofing with a browser compatibility matrix
  ```bash
  cognis-arsenal install privacyspoof   # pip install cognis-privacyspoof
  ```
- **[quantumready](https://github.com/cognis-digital/quantumready)** — Post-quantum migration readiness scanner â€” find quantum-vulnerable crypto and map to NIST PQC (FIPS 203/204/205)
  ```bash
  cognis-arsenal install quantumready   # pip install cognis-quantumready
  ```
- **[repo-roast](https://github.com/cognis-digital/repo-roast)** — An AI roasts (and then constructively fixes) your repo â€” local, free, savage
  ```bash
  cognis-arsenal install repo-roast   # pip install cognis-repo-roast
  ```
- **[setup-scripts](https://github.com/cognis-digital/setup-scripts)** — Curated, idempotent Ubuntu/Debian setup scripts for popular dev & infra tools
  ```bash
  cognis-arsenal install setup-scripts   # pip install cognis-setup-scripts
  ```
- **[skills](https://github.com/cognis-digital/skills)** — Agent skill registry â€” portable skills for AI agents (MCP/Claude/ClawHub style)
  ```bash
  cognis-arsenal install skills   # pip install cognis-skills
  ```
- **[templates](https://github.com/cognis-digital/templates)** — Starter templates: Python CLI, MCP server, Dockerfile, CI, devcontainer, and more
  ```bash
  cognis-arsenal install templates   # pip install cognis-templates
  ```
- **[uncensored-fleet](https://github.com/cognis-digital/uncensored-fleet)** — Deploy a local multi-model LLM fleet (llama.cpp) with an agent harness, hermes memory, and a one-command CLI
  ```bash
  cognis-arsenal install uncensored-fleet   # pip install cognis-uncensored-fleet
  ```
- **[windows-toolkit](https://github.com/cognis-digital/windows-toolkit)** — Windows power-user starter kit â€” curated tools, 80+ shortcuts, one-command winget setup
  ```bash
  cognis-arsenal install windows-toolkit   # pip install cognis-windows-toolkit
  ```

### AI Security & Governance (17)

- **[adversa](https://github.com/cognis-digital/adversa)** — LLM red-team harness â€” OWASP LLM Top 10 + MITRE ATLAS attack packs
  ```bash
  cognis-arsenal install adversa   # pip install cognis-adversa
  ```
- **[aegis](https://github.com/cognis-digital/aegis)** — AI Agent Permission & Access Auditor â€” surfaces the lethal trifecta of credentials + injection + reach
  ```bash
  cognis-arsenal install aegis   # pip install cognis-aegis
  ```
- **[agentlog](https://github.com/cognis-digital/agentlog)** — Agentic workflow replay & audit with OTel GenAI semantic conventions
  ```bash
  cognis-arsenal install agentlog   # pip install cognis-agentlog
  ```
- **[agentmap](https://github.com/cognis-digital/agentmap)** — Discover and map agent-to-agent / MCP communications and flag shadow AI
  ```bash
  cognis-arsenal install agentmap   # pip install cognis-agentmap
  ```
- **[agenttax](https://github.com/cognis-digital/agenttax)** — Classify findings against Microsoft's AI-agent threat taxonomy with mitigations
  ```bash
  cognis-arsenal install agenttax   # pip install cognis-agenttax
  ```
- **[aicard](https://github.com/cognis-digital/aicard)** — Auto-generated NIST AI RMF / EU AI Act Annex IV model & system cards
  ```bash
  cognis-arsenal install aicard   # pip install cognis-aicard
  ```
- **[biascope](https://github.com/cognis-digital/biascope)** — Embedded bias probe suite â€” demographic / occupational / geographic
  ```bash
  cognis-arsenal install biascope   # pip install cognis-biascope
  ```
- **[guardpost](https://github.com/cognis-digital/guardpost)** — Runtime agent firewall â€” PII redaction, rate limits, policy enforcement
  ```bash
  cognis-arsenal install guardpost   # pip install cognis-guardpost
  ```
- **[hallumark](https://github.com/cognis-digital/hallumark)** — LLM hallucination & grounding auditor for RAG systems
  ```bash
  cognis-arsenal install hallumark   # pip install cognis-hallumark
  ```
- **[ledgermind](https://github.com/cognis-digital/ledgermind)** — Local LLM cost & token forensics proxy with anomaly detection
  ```bash
  cognis-arsenal install ledgermind   # pip install cognis-ledgermind
  ```
- **[mcpauth](https://github.com/cognis-digital/mcpauth)** — Drop-in token-auth gateway in front of unauthenticated MCP servers
  ```bash
  cognis-arsenal install mcpauth   # pip install cognis-mcpauth
  ```
- **[mcpharden](https://github.com/cognis-digital/mcpharden)** — MCP server hardening linter â€” capability declarations, transport, tool descriptions
  ```bash
  cognis-arsenal install mcpharden   # pip install cognis-mcpharden
  ```
- **[mcpscan](https://github.com/cognis-digital/mcpscan)** — Scan MCP servers for RCE/SSRF/no-auth/tool-poisoning vulnerabilities
  ```bash
  cognis-arsenal install mcpscan   # pip install cognis-mcpscan
  ```
- **[promptmirror](https://github.com/cognis-digital/promptmirror)** — Prompt-injection & indirect-injection scanner for any LLM context input
  ```bash
  cognis-arsenal install promptmirror   # pip install cognis-promptmirror
  ```
- **[ragshield](https://github.com/cognis-digital/ragshield)** — RAG corpus poisoning detector â€” embedding anomalies, backdoor triggers
  ```bash
  cognis-arsenal install ragshield   # pip install cognis-ragshield
  ```
- **[ssrfmcp](https://github.com/cognis-digital/ssrfmcp)** — Consent-based SSRF probe harness for MCP servers that fetch URLs
  ```bash
  cognis-arsenal install ssrfmcp   # pip install cognis-ssrfmcp
  ```
- **[trustgate](https://github.com/cognis-digital/trustgate)** — Detect symlink-hijack / one-click-RCE / unsafe-trust settings in AI coding-agent projects
  ```bash
  cognis-arsenal install trustgate   # pip install cognis-trustgate
  ```

### AI Agents & LLMOps (9)

- **[agentsmith](https://github.com/cognis-digital/agentsmith)** — Config-first scaffolding and orchestration for multi-agent workflows
  ```bash
  cognis-arsenal install agentsmith   # pip install cognis-agentsmith
  ```
- **[engram](https://github.com/cognis-digital/engram)** — Durable, model-agnostic long-term memory for AI agents â€” stdlib, SQLite, MCP-native
  ```bash
  cognis-arsenal install engram   # pip install cognis-engram
  ```
- **[evalbench](https://github.com/cognis-digital/evalbench)** — Offline LLM / agent eval harness with regression gates
  ```bash
  cognis-arsenal install evalbench   # pip install cognis-evalbench
  ```
- **[memorybank](https://github.com/cognis-digital/memorybank)** — Portable long-term memory store for agents, exposed over MCP
  ```bash
  cognis-arsenal install memorybank   # pip install cognis-memorybank
  ```
- **[modelroute](https://github.com/cognis-digital/modelroute)** — Local model router / proxy across Ollama, vLLM, and cloud with fallback
  ```bash
  cognis-arsenal install modelroute   # pip install cognis-modelroute
  ```
- **[promptpack](https://github.com/cognis-digital/promptpack)** — Versioned prompt / template registry with A/B and rollbacks
  ```bash
  cognis-arsenal install promptpack   # pip install cognis-promptpack
  ```
- **[ragkit](https://github.com/cognis-digital/ragkit)** — Batteries-included local RAG pipeline â€” ingest, index, serve
  ```bash
  cognis-arsenal install ragkit   # pip install cognis-ragkit
  ```
- **[skillhub](https://github.com/cognis-digital/skillhub)** — Local skill registry and installer for AI agents
  ```bash
  cognis-arsenal install skillhub   # pip install cognis-skillhub
  ```
- **[toolguard](https://github.com/cognis-digital/toolguard)** — Runtime allowlist and policy for agent tool-calls
  ```bash
  cognis-arsenal install toolguard   # pip install cognis-toolguard
  ```

### Blue Team (6)

- **[canarynet](https://github.com/cognis-digital/canarynet)** — Self-hosted canary token network â€” AWS keys, DNS, docs, web URLs
  ```bash
  cognis-arsenal install canarynet   # pip install cognis-canarynet
  ```
- **[edrgap](https://github.com/cognis-digital/edrgap)** — EDR coverage & bypass detector â€” reconciles MDM + EDR + AD inventories
  ```bash
  cognis-arsenal install edrgap   # pip install cognis-edrgap
  ```
- **[honeytrace](https://github.com/cognis-digital/honeytrace)** — Active-decoy network lure system â€” SSH, RDP, SMB, web honeypots
  ```bash
  cognis-arsenal install honeytrace   # pip install cognis-honeytrace
  ```
- **[phishforge](https://github.com/cognis-digital/phishforge)** — Open-source phishing simulation â€” campaigns, templates, training
  ```bash
  cognis-arsenal install phishforge   # pip install cognis-phishforge
  ```
- **[sbomgate](https://github.com/cognis-digital/sbomgate)** — Continuous SBOM diff & vulnerability watch with maintainer-change tracking
  ```bash
  cognis-arsenal install sbomgate   # pip install cognis-sbomgate
  ```
- **[sentrylog](https://github.com/cognis-digital/sentrylog)** — Single-file SIEM for small teams â€” Sigma rules + multi-source ingest
  ```bash
  cognis-arsenal install sentrylog   # pip install cognis-sentrylog
  ```

### Red Team (5)

- **[c2detect](https://github.com/cognis-digital/c2detect)** — C2 server fingerprinter â€” Cobalt Strike, Sliver, Mythic, Havoc, Brute Ratel
  ```bash
  cognis-arsenal install c2detect   # pip install cognis-c2detect
  ```
- **[crackq](https://github.com/cognis-digital/crackq)** — Self-hosted password cracking queue â€” multi-user hashcat with audit log
  ```bash
  cognis-arsenal install crackq   # pip install cognis-crackq
  ```
- **[payloadlab](https://github.com/cognis-digital/payloadlab)** — Static malicious payload analyzer â€” PE/ELF/LNK/macro/OneNote
  ```bash
  cognis-arsenal install payloadlab   # pip install cognis-payloadlab
  ```
- **[pwnreview](https://github.com/cognis-digital/pwnreview)** — Pentest report generator â€” YAML findings to CREST-grade PDF
  ```bash
  cognis-arsenal install pwnreview   # pip install cognis-pwnreview
  ```
- **[redpath](https://github.com/cognis-digital/redpath)** — Active Directory attack path mapper â€” minimum-cost paths + remediation priority
  ```bash
  cognis-arsenal install redpath   # pip install cognis-redpath
  ```

### Security Operations (30)

- **[apiseclint](https://github.com/cognis-digital/apiseclint)** — Lint OpenAPI specs for security gaps (authz, rate-limit, data exposure)
  ```bash
  cognis-arsenal install apiseclint   # pip install cognis-apiseclint
  ```
- **[asnmap](https://github.com/cognis-digital/asnmap)** — Map ASN/CIDR ownership & neighbors from whois/RIR exports
  ```bash
  cognis-arsenal install asnmap   # pip install cognis-asnmap
  ```
- **[browserforensics](https://github.com/cognis-digital/browserforensics)** — Analyze exported browser history/downloads for IOCs and exfil signs
  ```bash
  cognis-arsenal install browserforensics   # pip install cognis-browserforensics
  ```
- **[certsearch](https://github.com/cognis-digital/certsearch)** — Analyze Certificate-Transparency exports for subdomains & rogue issuance
  ```bash
  cognis-arsenal install certsearch   # pip install cognis-certsearch
  ```
- **[cipherdetect](https://github.com/cognis-digital/cipherdetect)** — Detect & crack classical ciphers (caesar/vigenere/xor) by scoring
  ```bash
  cognis-arsenal install cipherdetect   # pip install cognis-cipherdetect
  ```
- **[cookieaudit](https://github.com/cognis-digital/cookieaudit)** — Audit Set-Cookie flags (Secure/HttpOnly/SameSite) from a response dump
  ```bash
  cognis-arsenal install cookieaudit   # pip install cognis-cookieaudit
  ```
- **[cspm](https://github.com/cognis-digital/cspm)** — Cloud security posture from a config export (public buckets, open SGs, weak IAM)
  ```bash
  cognis-arsenal install cspm   # pip install cognis-cspm
  ```
- **[cyberbench](https://github.com/cognis-digital/cyberbench)** — Chainable encode/decode/transform pipeline (base64/hex/rot/xor/url/gzip)
  ```bash
  cognis-arsenal install cyberbench   # pip install cognis-cyberbench
  ```
- **[dmarcaudit](https://github.com/cognis-digital/dmarcaudit)** — SecOps tool â€” Cognis Neural Suite
  ```bash
  cognis-arsenal install dmarcaudit   # pip install cognis-dmarcaudit
  ```
- **[dockeraudit](https://github.com/cognis-digital/dockeraudit)** — Audit Dockerfiles + image configs for security smells
  ```bash
  cognis-arsenal install dockeraudit   # pip install cognis-dockeraudit
  ```
- **[entropyscan](https://github.com/cognis-digital/entropyscan)** — SecOps tool â€” Cognis Neural Suite
  ```bash
  cognis-arsenal install entropyscan   # pip install cognis-entropyscan
  ```
- **[evtxsift](https://github.com/cognis-digital/evtxsift)** — Find brute-force, persistence & lateral-movement signals in exported Windows event logs
  ```bash
  cognis-arsenal install evtxsift   # pip install cognis-evtxsift
  ```
- **[filecarve](https://github.com/cognis-digital/filecarve)** — SecOps tool â€” Cognis Neural Suite
  ```bash
  cognis-arsenal install filecarve   # pip install cognis-filecarve
  ```
- **[ghaudit](https://github.com/cognis-digital/ghaudit)** — Audit a GitHub org's security posture (branch rules, 2FA, secrets) from an export
  ```bash
  cognis-arsenal install ghaudit   # pip install cognis-ghaudit
  ```
- **[githubrecon](https://github.com/cognis-digital/githubrecon)** — Map a GitHub user/org footprint & leaked-secret surface from API exports
  ```bash
  cognis-arsenal install githubrecon   # pip install cognis-githubrecon
  ```
- **[graphqlmap](https://github.com/cognis-digital/graphqlmap)** — Analyze GraphQL introspection for risky fields, depth, and authz gaps
  ```bash
  cognis-arsenal install graphqlmap   # pip install cognis-graphqlmap
  ```
- **[iamlint](https://github.com/cognis-digital/iamlint)** — Lint cloud IAM policies (AWS/GCP/Azure JSON) for least-privilege violations
  ```bash
  cognis-arsenal install iamlint   # pip install cognis-iamlint
  ```
- **[iocrep](https://github.com/cognis-digital/iocrep)** — Score IOCs against offline reputation/allow lists with explainable verdicts
  ```bash
  cognis-arsenal install iocrep   # pip install cognis-iocrep
  ```
- **[k8saudit](https://github.com/cognis-digital/k8saudit)** — Audit Kubernetes manifests against CIS-style security rules
  ```bash
  cognis-arsenal install k8saudit   # pip install cognis-k8saudit
  ```
- **[magicid](https://github.com/cognis-digital/magicid)** — Identify true file types by magic bytes (beats extensions)
  ```bash
  cognis-arsenal install magicid   # pip install cognis-magicid
  ```
- **[memtriage](https://github.com/cognis-digital/memtriage)** — Triage memory-dump artifacts: strings, IOCs, suspicious processes from a dump export
  ```bash
  cognis-arsenal install memtriage   # pip install cognis-memtriage
  ```
- **[mftparse](https://github.com/cognis-digital/mftparse)** — Analyze an NTFS $MFT CSV for timestomping and suspicious file activity
  ```bash
  cognis-arsenal install mftparse   # pip install cognis-mftparse
  ```
- **[prefetchparse](https://github.com/cognis-digital/prefetchparse)** — Surface program-execution evidence from Windows Prefetch exports
  ```bash
  cognis-arsenal install prefetchparse   # pip install cognis-prefetchparse
  ```
- **[regexlab](https://github.com/cognis-digital/regexlab)** — Test, explain & benchmark regexes + a library of security patterns
  ```bash
  cognis-arsenal install regexlab   # pip install cognis-regexlab
  ```
- **[stixgen](https://github.com/cognis-digital/stixgen)** — Build STIX 2.1 bundles from a list of IOCs/observables
  ```bash
  cognis-arsenal install stixgen   # pip install cognis-stixgen
  ```
- **[tfscan](https://github.com/cognis-digital/tfscan)** — Scan Terraform plans/configs for misconfigurations
  ```bash
  cognis-arsenal install tfscan   # pip install cognis-tfscan
  ```
- **[timeliner](https://github.com/cognis-digital/timeliner)** — Build a forensic super-timeline by merging & normalizing log/artifact CSVs
  ```bash
  cognis-arsenal install timeliner   # pip install cognis-timeliner
  ```
- **[ttphunt](https://github.com/cognis-digital/ttphunt)** — Hunt MITRE ATT&CK techniques across logs with a rule pack
  ```bash
  cognis-arsenal install ttphunt   # pip install cognis-ttphunt
  ```
- **[waybackrecon](https://github.com/cognis-digital/waybackrecon)** — Mine archived URLs/params/endpoints from a Wayback/CDX export
  ```bash
  cognis-arsenal install waybackrecon   # pip install cognis-waybackrecon
  ```
- **[yaragen](https://github.com/cognis-digital/yaragen)** — Generate candidate YARA rules from sample files/strings
  ```bash
  cognis-arsenal install yaragen   # pip install cognis-yaragen
  ```

### Application Security (10)

- **[apkpeek](https://github.com/cognis-digital/apkpeek)** — One-command static triage of Android APK/AAB binaries: surfaces hardcoded secrets, exported components, dangerous permissions, and insecure manifest flags as a single SARIF report.
  ```bash
  cognis-arsenal install apkpeek   # pip install cognis-apkpeek
  ```
- **[binhunt](https://github.com/cognis-digital/binhunt)** — Game/desktop binary integrity scanner that fingerprints executables, detects common packers/obfuscators, and diffs against a known-good baseline to catch tampering.
  ```bash
  cognis-arsenal install binhunt   # pip install cognis-binhunt
  ```
- **[cheatsense](https://github.com/cognis-digital/cheatsense)** — Anti-cheat telemetry analyzer that ingests game session logs and flags statistically anomalous input/aim/movement signatures with explainable per-flag scoring.
  ```bash
  cognis-arsenal install cheatsense   # pip install cognis-cheatsense
  ```
- **[dastlite](https://github.com/cognis-digital/dastlite)** — A headless, config-as-code DAST runner that crawls an authenticated web/mobile-API surface and fires a curated active-scan ruleset, emitting deduplicated SARIF.
  ```bash
  cognis-arsenal install dastlite   # pip install cognis-dastlite
  ```
- **[deeplinkfuzz](https://github.com/cognis-digital/deeplinkfuzz)** — Fuzzes Android/iOS deep links, intents, and custom URL schemes against an emulator/device to surface unvalidated-redirect, injection, and component-hijack bugs.
  ```bash
  cognis-arsenal install deeplinkfuzz   # pip install cognis-deeplinkfuzz
  ```
- **[hookcraft](https://github.com/cognis-digital/hookcraft)** — Generates ready-to-run Frida instrumentation scripts from a YAML intent (e.g. 'bypass SSL pinning', 'dump crypto keys') and verifies they attach to a target process.
  ```bash
  cognis-arsenal install hookcraft   # pip install cognis-hookcraft
  ```
- **[ipasnitch](https://github.com/cognis-digital/ipasnitch)** — Static scanner for iOS .ipa bundles that flags ATS exceptions, missing entitlements hardening, embedded URLs/secrets, and weak Info.plist transport settings.
  ```bash
  cognis-arsenal install ipasnitch   # pip install cognis-ipasnitch
  ```
- **[pincheck](https://github.com/cognis-digital/pincheck)** — Validates that a mobile app's TLS pinning, certificate transparency, and network-security-config are actually enforced by replaying a MITM handshake against the built artifact.
  ```bash
  cognis-arsenal install pincheck   # pip install cognis-pincheck
  ```
- **[sbomx](https://github.com/cognis-digital/sbomx)** — Generates a CycloneDX SBOM for mobile apps by unpacking native libs and bundled SDKs, then matches components against known-vuln and tracker/privacy databases.
  ```bash
  cognis-arsenal install sbomx   # pip install cognis-sbomx
  ```
- **[semsift](https://github.com/cognis-digital/semsift)** — Lightweight semantic-aware SAST that runs curated taint rules over diffs only, so PRs get fast incremental SAST instead of whole-repo scan fatigue.
  ```bash
  cognis-arsenal install semsift   # pip install cognis-semsift
  ```

### OSINT (6)

- **[corpmap](https://github.com/cognis-digital/corpmap)** — Corporate structure & beneficial-ownership mapper
  ```bash
  cognis-arsenal install corpmap   # pip install cognis-corpmap
  ```
- **[cryptotrace](https://github.com/cognis-digital/cryptotrace)** — Free-tier blockchain investigator â€” ETH/BTC clustering + sanctions xref
  ```bash
  cognis-arsenal install cryptotrace   # pip install cognis-cryptotrace
  ```
- **[darkmirror](https://github.com/cognis-digital/darkmirror)** — Surface-web mirror of public Tor leak-site index for brand monitoring
  ```bash
  cognis-arsenal install darkmirror   # pip install cognis-darkmirror
  ```
- **[geolens](https://github.com/cognis-digital/geolens)** — Image geolocation toolkit â€” EXIF, sun-shadow, OCR, reverse-search
  ```bash
  cognis-arsenal install geolens   # pip install cognis-geolens
  ```
- **[maritimeint](https://github.com/cognis-digital/maritimeint)** — AIS vessel tracking & sanctions-evasion anomaly detection
  ```bash
  cognis-arsenal install maritimeint   # pip install cognis-maritimeint
  ```
- **[personagraph](https://github.com/cognis-digital/personagraph)** — Identity resolution dossier â€” username/email/phone cross-platform
  ```bash
  cognis-arsenal install personagraph   # pip install cognis-personagraph
  ```

### Federal & Compliance (6)

- **[checkpoint-ai](https://github.com/cognis-digital/checkpoint-ai)** — NIST AI RMF / EU AI Act / ISO 42001 self-assessment & SSP generator
  ```bash
  cognis-arsenal install checkpoint-ai   # pip install cognis-checkpoint-ai
  ```
- **[clearancepath](https://github.com/cognis-digital/clearancepath)** — Personnel clearance hygiene tracker â€” SF-86, SEAD-3/4, training currency
  ```bash
  cognis-arsenal install clearancepath   # pip install cognis-clearancepath
  ```
- **[cmmcmap](https://github.com/cognis-digital/cmmcmap)** — CMMC Level 2 practice mapper â€” stack-aware SSP skeleton generator
  ```bash
  cognis-arsenal install cmmcmap   # pip install cognis-cmmcmap
  ```
- **[fedramplens](https://github.com/cognis-digital/fedramplens)** — FedRAMP boundary visualizer & OSCAL-format SSP/POAM generator
  ```bash
  cognis-arsenal install fedramplens   # pip install cognis-fedramplens
  ```
- **[gsafinder](https://github.com/cognis-digital/gsafinder)** — GSA Schedule opportunity surveyor â€” SAM.gov + eBuy + FedConnect
  ```bash
  cognis-arsenal install gsafinder   # pip install cognis-gsafinder
  ```
- **[sbirscout](https://github.com/cognis-digital/sbirscout)** — SBIR/STTR topic discovery â€” DSIP + SBIR.gov + NIH digest with bid scoring
  ```bash
  cognis-arsenal install sbirscout   # pip install cognis-sbirscout
  ```

### Compliance & GRC (8)

- **[accessreview](https://github.com/cognis-digital/accessreview)** — Periodic user-access-review (UAR) campaign runner
  ```bash
  cognis-arsenal install accessreview   # pip install cognis-accessreview
  ```
- **[auditrail](https://github.com/cognis-digital/auditrail)** — Tamper-evident audit-log aggregator with hash-chained attestation
  ```bash
  cognis-arsenal install auditrail   # pip install cognis-auditrail
  ```
- **[dpiaforge](https://github.com/cognis-digital/dpiaforge)** — DPIA and EU AI Act impact-assessment generator
  ```bash
  cognis-arsenal install dpiaforge   # pip install cognis-dpiaforge
  ```
- **[frameworkmap](https://github.com/cognis-digital/frameworkmap)** — Crosswalk controls across NIST, ISO 27001, SOC 2, CMMC, PCI
  ```bash
  cognis-arsenal install frameworkmap   # pip install cognis-frameworkmap
  ```
- **[gdprkit](https://github.com/cognis-digital/gdprkit)** — GDPR/CCPA DSAR, RoPA, and cookie-consent toolkit
  ```bash
  cognis-arsenal install gdprkit   # pip install cognis-gdprkit
  ```
- **[policyforge](https://github.com/cognis-digital/policyforge)** — Auto-generate security policies from a short questionnaire
  ```bash
  cognis-arsenal install policyforge   # pip install cognis-policyforge
  ```
- **[soc2box](https://github.com/cognis-digital/soc2box)** — SOC 2 evidence collector and control tracker, self-hosted
  ```bash
  cognis-arsenal install soc2box   # pip install cognis-soc2box
  ```
- **[vendorvet](https://github.com/cognis-digital/vendorvet)** — Third-party / vendor risk questionnaires with SBOM cross-ref
  ```bash
  cognis-arsenal install vendorvet   # pip install cognis-vendorvet
  ```

### Privacy (7)

- **[breachwatch](https://github.com/cognis-digital/breachwatch)** — Personal breach aggregator â€” HIBP + DeHashed + stealer-log triage
  ```bash
  cognis-arsenal install breachwatch   # pip install cognis-breachwatch
  ```
- **[optout](https://github.com/cognis-digital/optout)** — Automated data-broker opt-out engine â€” top 50 brokers, CCPA/GDPR letters
  ```bash
  cognis-arsenal install optout   # pip install cognis-optout
  ```
- **[piicomb](https://github.com/cognis-digital/piicomb)** — Local PII discovery in your own files â€” SSN/CC/passport/DL/email/phone/DOB
  ```bash
  cognis-arsenal install piicomb   # pip install cognis-piicomb
  ```
- **[privacyshell](https://github.com/cognis-digital/privacyshell)** — Hardened browser profile generator â€” Firefox / LibreWolf / Brave
  ```bash
  cognis-arsenal install privacyshell   # pip install cognis-privacyshell
  ```
- **[recall](https://github.com/cognis-digital/recall)** — Privacy-first local RAG over personal data â€” encrypted, audit-logged
  ```bash
  cognis-arsenal install recall   # pip install cognis-recall
  ```
- **[trackblock](https://github.com/cognis-digital/trackblock)** — Family phone stalkerware audit â€” MVT-class iOS/Android forensics
  ```bash
  cognis-arsenal install trackblock   # pip install cognis-trackblock
  ```
- **[vaultmap](https://github.com/cognis-digital/vaultmap)** — Personal asset & account inventory â€” estate-planning-grade encrypted
  ```bash
  cognis-arsenal install vaultmap   # pip install cognis-vaultmap
  ```

### Network Security (3)

- **[certpatrol](https://github.com/cognis-digital/certpatrol)** — TLS cert lifecycle & rogue-issuance watch via Certificate Transparency
  ```bash
  cognis-arsenal install certpatrol   # pip install cognis-certpatrol
  ```
- **[dnsaudit](https://github.com/cognis-digital/dnsaudit)** — DNS posture & misconfiguration scanner â€” SPF/DKIM/DMARC/DNSSEC/CAA
  ```bash
  cognis-arsenal install dnsaudit   # pip install cognis-dnsaudit
  ```
- **[egresswatch](https://github.com/cognis-digital/egresswatch)** — Server-side outbound connection auditor â€” eBPF/Falco wrapper
  ```bash
  cognis-arsenal install egresswatch   # pip install cognis-egresswatch
  ```

### Information Integrity (4)

- **[claimtrace](https://github.com/cognis-digital/claimtrace)** — Misinformation provenance tracer â€” earliest-known appearance graph
  ```bash
  cognis-arsenal install claimtrace   # pip install cognis-claimtrace
  ```
- **[deepcheck](https://github.com/cognis-digital/deepcheck)** — Lightweight synthetic-media detector with C2PA validation
  ```bash
  cognis-arsenal install deepcheck   # pip install cognis-deepcheck
  ```
- **[electionlens](https://github.com/cognis-digital/electionlens)** — Influence-operations pattern monitor for election periods
  ```bash
  cognis-arsenal install electionlens   # pip install cognis-electionlens
  ```
- **[narrativediff](https://github.com/cognis-digital/narrativediff)** — News bias & framing diff across 50+ outlets per event
  ```bash
  cognis-arsenal install narrativediff   # pip install cognis-narrativediff
  ```

### Supply Chain Security (4)

- **[depgraph](https://github.com/cognis-digital/depgraph)** — Dependency risk visualizer â€” Scorecard + OSV + typosquat + maintainer signals
  ```bash
  cognis-arsenal install depgraph   # pip install cognis-depgraph
  ```
- **[ossaudit](https://github.com/cognis-digital/ossaudit)** — OSS license compliance auditor â€” AGPL contamination + NOTICE generation
  ```bash
  cognis-arsenal install ossaudit   # pip install cognis-ossaudit
  ```
- **[pipewatch-pro](https://github.com/cognis-digital/pipewatch-pro)** — CI/CD supply-chain auditor â€” GH Actions / GitLab CI / OWASP CI/CD Top 10
  ```bash
  cognis-arsenal install pipewatch-pro   # pip install cognis-pipewatch-pro
  ```
- **[secretsweep](https://github.com/cognis-digital/secretsweep)** — Repo secret scanner + auto-rotator across providers
  ```bash
  cognis-arsenal install secretsweep   # pip install cognis-secretsweep
  ```

### Developer Tools (10)

- **[apidiff](https://github.com/cognis-digital/apidiff)** — Breaking-change detector for OpenAPI / GraphQL across commits
  ```bash
  cognis-arsenal install apidiff   # pip install cognis-apidiff
  ```
- **[codeglance](https://github.com/cognis-digital/codeglance)** — Repo onboarding map â€” architecture + hotspots for humans and agents
  ```bash
  cognis-arsenal install codeglance   # pip install cognis-codeglance
  ```
- **[envdoctor](https://github.com/cognis-digital/envdoctor)** — .env validator, secret-presence and config-drift checker
  ```bash
  cognis-arsenal install envdoctor   # pip install cognis-envdoctor
  ```
- **[flakefinder](https://github.com/cognis-digital/flakefinder)** — Flaky-test detector from CI history with quarantine suggestions
  ```bash
  cognis-arsenal install flakefinder   # pip install cognis-flakefinder
  ```
- **[gitstory](https://github.com/cognis-digital/gitstory)** — Changelog and release notes from conventional commits
  ```bash
  cognis-arsenal install gitstory   # pip install cognis-gitstory
  ```
- **[licenselens](https://github.com/cognis-digital/licenselens)** — Dependency license + SBOM gate, developer-CLI first
  ```bash
  cognis-arsenal install licenselens   # pip install cognis-licenselens
  ```
- **[mcpforge](https://github.com/cognis-digital/mcpforge)** — Scaffold, test, and publish MCP servers in minutes
  ```bash
  cognis-arsenal install mcpforge   # pip install cognis-mcpforge
  ```
- **[promptlint](https://github.com/cognis-digital/promptlint)** — Lint, version, and test prompts as code with a CI gate
  ```bash
  cognis-arsenal install promptlint   # pip install cognis-promptlint
  ```
- **[shipcheck](https://github.com/cognis-digital/shipcheck)** — Dockerfile linter with image-size and CVE advisories
  ```bash
  cognis-arsenal install shipcheck   # pip install cognis-shipcheck
  ```
- **[tokenmeter](https://github.com/cognis-digital/tokenmeter)** — Token and cost counter / budgeter for LLM apps, CI-ready
  ```bash
  cognis-arsenal install tokenmeter   # pip install cognis-tokenmeter
  ```

### Data & Datasets (8)

- **[csvlens](https://github.com/cognis-digital/csvlens)** — Fast CLI for profiling and cleaning huge CSV / Parquet files
  ```bash
  cognis-arsenal install csvlens   # pip install cognis-csvlens
  ```
- **[datasetcard](https://github.com/cognis-digital/datasetcard)** — Auto Dataset Cards / datasheets with Croissant + provenance
  ```bash
  cognis-arsenal install datasetcard   # pip install cognis-datasetcard
  ```
- **[duckprobe](https://github.com/cognis-digital/duckprobe)** — Zero-setup data-quality checks on any file or warehouse via DuckDB
  ```bash
  cognis-arsenal install duckprobe   # pip install cognis-duckprobe
  ```
- **[embedaudit](https://github.com/cognis-digital/embedaudit)** — Embedding / vector-store drift and poisoning audit
  ```bash
  cognis-arsenal install embedaudit   # pip install cognis-embedaudit
  ```
- **[lineagemap](https://github.com/cognis-digital/lineagemap)** — Column-level lineage extracted from SQL and dbt
  ```bash
  cognis-arsenal install lineagemap   # pip install cognis-lineagemap
  ```
- **[piiscan](https://github.com/cognis-digital/piiscan)** — PII discovery across warehouses and lakes (data-side scanner)
  ```bash
  cognis-arsenal install piiscan   # pip install cognis-piiscan
  ```
- **[schemadrift](https://github.com/cognis-digital/schemadrift)** — Schema-change detector and data-contract tests
  ```bash
  cognis-arsenal install schemadrift   # pip install cognis-schemadrift
  ```
- **[seedforge](https://github.com/cognis-digital/seedforge)** — Synthetic test-data generator with referential integrity
  ```bash
  cognis-arsenal install seedforge   # pip install cognis-seedforge
  ```

### DevOps & Observability (6)

- **[alertmux](https://github.com/cognis-digital/alertmux)** — Alert dedup, correlation, and routing in front of Grafana / PagerDuty
  ```bash
  cognis-arsenal install alertmux   # pip install cognis-alertmux
  ```
- **[cloudbill](https://github.com/cognis-digital/cloudbill)** — Multi-cloud cost report, anomaly detection, and FOCUS export
  ```bash
  cognis-arsenal install cloudbill   # pip install cognis-cloudbill
  ```
- **[k8scost](https://github.com/cognis-digital/k8scost)** — Kubernetes cost and rightsizing advisor with no Prometheus dependency
  ```bash
  cognis-arsenal install k8scost   # pip install cognis-k8scost
  ```
- **[otelbox](https://github.com/cognis-digital/otelbox)** — One-command OpenTelemetry collector + dashboards bundle
  ```bash
  cognis-arsenal install otelbox   # pip install cognis-otelbox
  ```
- **[probesite](https://github.com/cognis-digital/probesite)** — Synthetic uptime and Playwright checks exported to Prometheus
  ```bash
  cognis-arsenal install probesite   # pip install cognis-probesite
  ```
- **[statuskit](https://github.com/cognis-digital/statuskit)** — Self-hosted status page with incident timeline and subscribers
  ```bash
  cognis-arsenal install statuskit   # pip install cognis-statuskit
  ```

### Business Ops (10)

- **[boardroom](https://github.com/cognis-digital/boardroom)** — Investor-update and KPI one-pager generator from your metrics
  ```bash
  cognis-arsenal install boardroom   # pip install cognis-boardroom
  ```
- **[churnlens](https://github.com/cognis-digital/churnlens)** — Self-hosted SaaS metrics â€” MRR, churn, LTV from Stripe or CSV
  ```bash
  cognis-arsenal install churnlens   # pip install cognis-churnlens
  ```
- **[invoctl](https://github.com/cognis-digital/invoctl)** — CLI invoicing + payment-link generator with PDF and a local ledger
  ```bash
  cognis-arsenal install invoctl   # pip install cognis-invoctl
  ```
- **[leadforge](https://github.com/cognis-digital/leadforge)** — Lightweight MCP-native CRM pipeline with email sequences
  ```bash
  cognis-arsenal install leadforge   # pip install cognis-leadforge
  ```
- **[meetingcost](https://github.com/cognis-digital/meetingcost)** — Compute the dollar cost of meetings from your calendar (.ics)
  ```bash
  cognis-arsenal install meetingcost   # pip install cognis-meetingcost
  ```
- **[orgchart](https://github.com/cognis-digital/orgchart)** — Org charts and headcount plans generated from CSV / HRIS export
  ```bash
  cognis-arsenal install orgchart   # pip install cognis-orgchart
  ```
- **[paywatch](https://github.com/cognis-digital/paywatch)** — Recurring-charge and subscription detector from bank/Plaid CSV
  ```bash
  cognis-arsenal install paywatch   # pip install cognis-paywatch
  ```
- **[quotecraft](https://github.com/cognis-digital/quotecraft)** — Proposal / quote / SOW generator â€” YAML to branded PDF
  ```bash
  cognis-arsenal install quotecraft   # pip install cognis-quotecraft
  ```
- **[runbookgen](https://github.com/cognis-digital/runbookgen)** — Incident runbook and SOP generator from templates
  ```bash
  cognis-arsenal install runbookgen   # pip install cognis-runbookgen
  ```
- **[seataudit](https://github.com/cognis-digital/seataudit)** — SaaS license, seat-usage and shadow-IT auditor
  ```bash
  cognis-arsenal install seataudit   # pip install cognis-seataudit
  ```

### Business Development (10)

- **[coldforge](https://github.com/cognis-digital/coldforge)** — Render personalized cold-outreach sequences from Markdown templates + a contacts CSV, with spam-score linting and per-send dry-run preview.
  ```bash
  cognis-arsenal install coldforge   # pip install cognis-coldforge
  ```
- **[crmsync](https://github.com/cognis-digital/crmsync)** — Bidirectional, idempotent sync of contacts/deals between a local SQLite source-of-truth and CRM APIs (HubSpot/Pipedrive/Salesforce) via one config.
  ```bash
  cognis-arsenal install crmsync   # pip install cognis-crmsync
  ```
- **[dealflow](https://github.com/cognis-digital/dealflow)** — Model your sales pipeline as a YAML state machine and compute conversion rates, stage velocity, and weighted forecast straight from CRM exports.
  ```bash
  cognis-arsenal install dealflow   # pip install cognis-dealflow
  ```
- **[dripcheck](https://github.com/cognis-digital/dripcheck)** — Lint email sequences and drip campaigns for deliverability: SPF/DKIM/DMARC, link health, unsubscribe presence, and CAN-SPAM/GDPR compliance.
  ```bash
  cognis-arsenal install dripcheck   # pip install cognis-dripcheck
  ```
- **[enrichr](https://github.com/cognis-digital/enrichr)** — Enrich a leads CSV with firmographics, tech stack, and contact validation from pluggable providers, caching results to avoid duplicate API spend.
  ```bash
  cognis-arsenal install enrichr   # pip install cognis-enrichr
  ```
- **[introbot](https://github.com/cognis-digital/introbot)** — Find warm-intro paths through your team's combined network graph and draft double-opt-in intro requests from a single contacts manifest.
  ```bash
  cognis-arsenal install introbot   # pip install cognis-introbot
  ```
- **[pactgen](https://github.com/cognis-digital/pactgen)** — Generate branded sales proposals and SOWs from a YAML scope file + pricing table into PDF/HTML, with a deterministic line-item math check.
  ```bash
  cognis-arsenal install pactgen   # pip install cognis-pactgen
  ```
- **[partnermap](https://github.com/cognis-digital/partnermap)** — Track partnership/channel agreements as YAML records and compute account overlap, co-sell coverage gaps, and renewal/expiry alerts.
  ```bash
  cognis-arsenal install partnermap   # pip install cognis-partnermap
  ```
- **[raisedeck](https://github.com/cognis-digital/raisedeck)** — Build and maintain an investor-update + data-room manifest from a metrics YAML, rendering monthly MRR/burn/runway updates with consistent KPIs.
  ```bash
  cognis-arsenal install raisedeck   # pip install cognis-raisedeck
  ```
- **[warmline](https://github.com/cognis-digital/warmline)** — Score and rank inbound/outbound leads from a YAML rulebook, emitting a ranked queue as JSON/CSV for your SDRs and CI gates.
  ```bash
  cognis-arsenal install warmline   # pip install cognis-warmline
  ```

### FinTech (10)

- **[chargeguard](https://github.com/cognis-digital/chargeguard)** — Monitors dispute/chargeback feeds, flags fraud-rate threshold breaches (VAMP/Visa), and drafts representment evidence packets.
  ```bash
  cognis-arsenal install chargeguard   # pip install cognis-chargeguard
  ```
- **[fraudlens](https://github.com/cognis-digital/fraudlens)** — Replays a stream of transactions against pluggable fraud rules and ML scorers, emitting precision/recall and alert volume from the terminal.
  ```bash
  cognis-arsenal install fraudlens   # pip install cognis-fraudlens
  ```
- **[iso20022](https://github.com/cognis-digital/iso20022)** — Validates, lints, and diffs ISO 20022 / pacs / camt payment messages and translates legacy MT into MX with schema-aware errors.
  ```bash
  cognis-arsenal install iso20022   # pip install cognis-iso20022
  ```
- **[ledgerproof](https://github.com/cognis-digital/ledgerproof)** — Verifies double-entry ledger integrity and tamper-evidence by checking balance invariants and hash-chained journal entries.
  ```bash
  cognis-arsenal install ledgerproof   # pip install cognis-ledgerproof
  ```
- **[obscan](https://github.com/cognis-digital/obscan)** — Conformance and security linter for Open Banking / FAPI APIs: validates OAuth flows, consent scopes, and PSD2 endpoints against the spec.
  ```bash
  cognis-arsenal install obscan   # pip install cognis-obscan
  ```
- **[panhound](https://github.com/cognis-digital/panhound)** — Scans code, logs, fixtures, and S3 buckets for leaked PANs (Luhn-validated card numbers) and CVVs before they hit prod.
  ```bash
  cognis-arsenal install panhound   # pip install cognis-panhound
  ```
- **[sanctscan](https://github.com/cognis-digital/sanctscan)** — Screens counterparties and transactions against OFAC/EU/UN sanctions lists with fuzzy name matching and explainable hit scoring.
  ```bash
  cognis-arsenal install sanctscan   # pip install cognis-sanctscan
  ```
- **[tokenvault](https://github.com/cognis-digital/tokenvault)** — Self-hostable PCI tokenization microservice and CLI that swaps PANs for format-preserving tokens and proves no raw card data persists.
  ```bash
  cognis-arsenal install tokenvault   # pip install cognis-tokenvault
  ```
- **[txgraph](https://github.com/cognis-digital/txgraph)** — Builds a transaction graph from ledger/account data and surfaces structuring, layering, and mule-network patterns for AML triage.
  ```bash
  cognis-arsenal install txgraph   # pip install cognis-txgraph
  ```
- **[webhookvty](https://github.com/cognis-digital/webhookvty)** — Verifies and replays signed payment webhooks (Stripe/Adyen/PayPal/Plaid) locally, catching signature, idempotency, and replay-attack bugs.
  ```bash
  cognis-arsenal install webhookvty   # pip install cognis-webhookvty
  ```

### Healthcare (10)

- **[baadiff](https://github.com/cognis-digital/baadiff)** — Scan a repo or infra manifest for HIPAA Security Rule gaps and produce a Business Associate readiness scorecard.
  ```bash
  cognis-arsenal install baadiff   # pip install cognis-baadiff
  ```
- **[codemap](https://github.com/cognis-digital/codemap)** — Translate and validate medical codes across ICD-10, SNOMED CT, LOINC, RxNorm, and CPT from the CLI.
  ```bash
  cognis-arsenal install codemap   # pip install cognis-codemap
  ```
- **[consentledger](https://github.com/cognis-digital/consentledger)** — Maintain a tamper-evident, hash-chained audit log of patient-data access and consent events.
  ```bash
  cognis-arsenal install consentledger   # pip install cognis-consentledger
  ```
- **[deidproof](https://github.com/cognis-digital/deidproof)** — Re-identification risk assessment that computes k-anonymity, l-diversity, and HIPAA Safe Harbor compliance on a dataset.
  ```bash
  cognis-arsenal install deidproof   # pip install cognis-deidproof
  ```
- **[dicomsweep](https://github.com/cognis-digital/dicomsweep)** — De-identify DICOM imaging studies per the DICOM PS3.15 Annex E profile, scrubbing tags and burned-in pixel text.
  ```bash
  cognis-arsenal install dicomsweep   # pip install cognis-dicomsweep
  ```
- **[fhirlint](https://github.com/cognis-digital/fhirlint)** — Validate FHIR R4/R5 resources and bundles against profiles (US Core, etc.) with precise, line-level error reporting.
  ```bash
  cognis-arsenal install fhirlint   # pip install cognis-fhirlint
  ```
- **[hl7tap](https://github.com/cognis-digital/hl7tap)** — Parse, pretty-print, diff, and replay HL7 v2 messages over MLLP from the terminal.
  ```bash
  cognis-arsenal install hl7tap   # pip install cognis-hl7tap
  ```
- **[phiscrub](https://github.com/cognis-digital/phiscrub)** — Stream-scan logs, CSVs, and free-text notes for PHI (names, MRNs, SSNs, dates, addresses) and redact or tokenize in place.
  ```bash
  cognis-arsenal install phiscrub   # pip install cognis-phiscrub
  ```
- **[synthcohort](https://github.com/cognis-digital/synthcohort)** — Generate statistically realistic synthetic patient cohorts (FHIR/CSV) from a schema spec for dev and testing.
  ```bash
  cognis-arsenal install synthcohort   # pip install cognis-synthcohort
  ```
- **[trialwatch](https://github.com/cognis-digital/trialwatch)** — Query, diff, and monitor ClinicalTrials.gov records, alerting on status, enrollment, or result changes.
  ```bash
  cognis-arsenal install trialwatch   # pip install cognis-trialwatch
  ```

### IoT / OT (10)

- **[blescope](https://github.com/cognis-digital/blescope)** — Sniff and decode BLE GATT traffic, fingerprint device profiles, and assert on insecure pairing/characteristics in CI against a capture.
  ```bash
  cognis-arsenal install blescope   # pip install cognis-blescope
  ```
- **[canzap](https://github.com/cognis-digital/canzap)** — Replay, fuzz, and assert on CAN bus traffic from a .pcap or SocketCAN interface with a tiny YAML DSL.
  ```bash
  cognis-arsenal install canzap   # pip install cognis-canzap
  ```
- **[fwxray](https://github.com/cognis-digital/fwxray)** — Diff two firmware images and surface exactly what changed: new binaries, flipped config flags, added certs, and shifted entropy regions.
  ```bash
  cognis-arsenal install fwxray   # pip install cognis-fwxray
  ```
- **[keyhunt](https://github.com/cognis-digital/keyhunt)** — Scan firmware blobs and filesystem dumps for hardcoded private keys, API tokens, default creds, and weak RSA/ECC material.
  ```bash
  cognis-arsenal install keyhunt   # pip install cognis-keyhunt
  ```
- **[modpot](https://github.com/cognis-digital/modpot)** — Spin up a high-interaction Modbus/DNP3 ICS honeypot that logs attacker register reads/writes as structured JSON.
  ```bash
  cognis-arsenal install modpot   # pip install cognis-modpot
  ```
- **[mqttspy](https://github.com/cognis-digital/mqttspy)** — Passively map an MQTT broker: enumerate topics, detect unauthenticated writes, spot PII/secrets in payloads, and emit a risk report.
  ```bash
  cognis-arsenal install mqttspy   # pip install cognis-mqttspy
  ```
- **[otaverify](https://github.com/cognis-digital/otaverify)** — Validate OTA update packages end-to-end: signature chains, rollback protection, anti-downgrade counters, and delta-patch integrity.
  ```bash
  cognis-arsenal install otaverify   # pip install cognis-otaverify
  ```
- **[rtosmap](https://github.com/cognis-digital/rtosmap)** — Statically map task structures, stack usage, and ISR call graphs in FreeRTOS/Zephyr firmware to flag stack overflows and priority-inversion risks.
  ```bash
  cognis-arsenal install rtosmap   # pip install cognis-rtosmap
  ```
- **[sbomb](https://github.com/cognis-digital/sbomb)** — Generate a CycloneDX SBOM directly from an unpacked firmware root filesystem and flag components with known CVEs and EOL kernels.
  ```bash
  cognis-arsenal install sbomb   # pip install cognis-sbomb
  ```
- **[uefiscan](https://github.com/cognis-digital/uefiscan)** — Audit UEFI firmware dumps for missing Secure Boot keys, unsigned modules, S3 boot-script vulns, and known SMM threats.
  ```bash
  cognis-arsenal install uefiscan   # pip install cognis-uefiscan
  ```

### Web3 (10)

- **[approvewarden](https://github.com/cognis-digital/approvewarden)** — Scans any wallet for dangerous ERC-20/721/1155 token approvals and infinite allowances, scoring drainer exposure and emitting revoke transactions.
  ```bash
  cognis-arsenal install approvewarden   # pip install cognis-approvewarden
  ```
- **[bytematch](https://github.com/cognis-digital/bytematch)** — Verifies that deployed on-chain bytecode matches a given source/Foundry build, detecting unverified or tampered proxies and implementations.
  ```bash
  cognis-arsenal install bytematch   # pip install cognis-bytematch
  ```
- **[forkfuzz](https://github.com/cognis-digital/forkfuzz)** — Mainnet-fork invariant fuzzer that replays your contract against live state and stateful sequences to break protocol invariants before deploy.
  ```bash
  cognis-arsenal install forkfuzz   # pip install cognis-forkfuzz
  ```
- **[gasprofiler](https://github.com/cognis-digital/gasprofiler)** — Per-opcode and per-function gas profiler that flags unbounded loops, DoS-prone patterns, and regressions against a committed baseline.
  ```bash
  cognis-arsenal install gasprofiler   # pip install cognis-gasprofiler
  ```
- **[mevscope](https://github.com/cognis-digital/mevscope)** — Replays a tx or address history to attribute sandwich, frontrun, and backrun MEV extraction with per-trade loss accounting.
  ```bash
  cognis-arsenal install mevscope   # pip install cognis-mevscope
  ```
- **[oraclewatch](https://github.com/cognis-digital/oraclewatch)** — Monitors price-oracle feeds for staleness, deviation, and manipulation exposure, simulating TWAP/spot attack profitability per pool.
  ```bash
  cognis-arsenal install oraclewatch   # pip install cognis-oraclewatch
  ```
- **[reentryx](https://github.com/cognis-digital/reentryx)** — Static + symbolic detector that flags reentrancy, cross-function, and read-only reentrancy paths in Solidity/Vyper with CI-gating SARIF output.
  ```bash
  cognis-arsenal install reentryx   # pip install cognis-reentryx
  ```
- **[rugradar](https://github.com/cognis-digital/rugradar)** — Token contract risk scanner detecting honeypots, hidden mint/blacklist functions, owner backdoors, and unlocked liquidity before you ape.
  ```bash
  cognis-arsenal install rugradar   # pip install cognis-rugradar
  ```
- **[sigsleuth](https://github.com/cognis-digital/sigsleuth)** — Decodes raw calldata and EIP-712 typed-data into human-readable intent, flagging blind-signing and malicious permit/Permit2 payloads.
  ```bash
  cognis-arsenal install sigsleuth   # pip install cognis-sigsleuth
  ```
- **[storagelens](https://github.com/cognis-digital/storagelens)** — Diffs and decodes contract storage layouts across proxy upgrades to catch storage-collision and uninitialized-slot bugs.
  ```bash
  cognis-arsenal install storagelens   # pip install cognis-storagelens
  ```

### Defense Tech (15)

- **[adsbwatch](https://github.com/cognis-digital/adsbwatch)** — Analyze an ADS-B feed/CSV for anomalies: callsign spoofing, squawk 7500/7600/7700, and unusual loiter patterns.
  ```bash
  cognis-arsenal install adsbwatch   # pip install cognis-adsbwatch
  ```
- **[basemap](https://github.com/cognis-digital/basemap)** — Build and query a structured catalog of installations/AOIs with distance, sector, and coverage queries.
  ```bash
  cognis-arsenal install basemap   # pip install cognis-basemap
  ```
- **[classguard](https://github.com/cognis-digital/classguard)** — Validate classification banner markings (CUI/CONFIDENTIAL/SECRET) in documents per portion-marking rules.
  ```bash
  cognis-arsenal install classguard   # pip install cognis-classguard
  ```
- **[convoyplan](https://github.com/cognis-digital/convoyplan)** — Defense logistics route/sustainment planner computing fuel, resupply windows, and chokepoint risk from a YAML plan.
  ```bash
  cognis-arsenal install convoyplan   # pip install cognis-convoyplan
  ```
- **[ewcorr](https://github.com/cognis-digital/ewcorr)** — Correlate electronic-warfare event logs by time/frequency/bearing to cluster emitters.
  ```bash
  cognis-arsenal install ewcorr   # pip install cognis-ewcorr
  ```
- **[geoaoi](https://github.com/cognis-digital/geoaoi)** — Area-of-interest geospatial helper: bounding boxes, geofence checks, and change-event diffs from coordinate logs.
  ```bash
  cognis-arsenal install geoaoi   # pip install cognis-geoaoi
  ```
- **[itarcheck](https://github.com/cognis-digital/itarcheck)** — Flags potential ITAR/EAR export-controlled terms and USML categories in code, datasheets, and docs.
  ```bash
  cognis-arsenal install itarcheck   # pip install cognis-itarcheck
  ```
- **[milstdlint](https://github.com/cognis-digital/milstdlint)** — Lint documents against MIL-STD / DoD formatting and classification-marking rules.
  ```bash
  cognis-arsenal install milstdlint   # pip install cognis-milstdlint
  ```
- **[natosymbol](https://github.com/cognis-digital/natosymbol)** — Generate and validate APP-6/MIL-STD-2525 symbol identification codes (SIDC).
  ```bash
  cognis-arsenal install natosymbol   # pip install cognis-natosymbol
  ```
- **[opsecscan](https://github.com/cognis-digital/opsecscan)** — Scan documents and file metadata for OPSEC leaks: geotags, author, GPS EXIF, unit identifiers.
  ```bash
  cognis-arsenal install opsecscan   # pip install cognis-opsecscan
  ```
- **[readiness](https://github.com/cognis-digital/readiness)** — Compute unit readiness (C-ratings style) from a personnel/equipment/training YAML and flag gaps.
  ```bash
  cognis-arsenal install readiness   # pip install cognis-readiness
  ```
- **[rfsurvey](https://github.com/cognis-digital/rfsurvey)** — Analyze RF spectrum-occupancy CSV/metadata for band usage, interference, and anomalies.
  ```bash
  cognis-arsenal install rfsurvey   # pip install cognis-rfsurvey
  ```
- **[sigmeta](https://github.com/cognis-digital/sigmeta)** — Parse and classify signal metadata (freq, modulation, bandwidth) into a normalized catalog.
  ```bash
  cognis-arsenal install sigmeta   # pip install cognis-sigmeta
  ```
- **[threatmodeler](https://github.com/cognis-digital/threatmodeler)** — Generate STRIDE threat models and attack trees from a YAML system spec.
  ```bash
  cognis-arsenal install threatmodeler   # pip install cognis-threatmodeler
  ```
- **[uaslog](https://github.com/cognis-digital/uaslog)** — Counter-UAS telemetry/log analyzer that flags drone-detection events, RF bands, and track anomalies.
  ```bash
  cognis-arsenal install uaslog   # pip install cognis-uaslog
  ```

### Tactical (30)

- **[attackmap](https://github.com/cognis-digital/attackmap)** — Map findings to MITRE ATT&CK techniques + coverage heatmap
  ```bash
  cognis-arsenal install attackmap   # pip install cognis-attackmap
  ```
- **[authmatrix](https://github.com/cognis-digital/authmatrix)** — Test an access-control matrix (role x endpoint) for IDOR/authz gaps
  ```bash
  cognis-arsenal install authmatrix   # pip install cognis-authmatrix
  ```
- **[cloudkeys](https://github.com/cognis-digital/cloudkeys)** — Find leaked cloud keys (AWS/GCP/Azure) + classify blast radius
  ```bash
  cognis-arsenal install cloudkeys   # pip install cognis-cloudkeys
  ```
- **[corsaudit](https://github.com/cognis-digital/corsaudit)** — Detect permissive/misconfigured CORS from headers or a config
  ```bash
  cognis-arsenal install corsaudit   # pip install cognis-corsaudit
  ```
- **[cspbuilder](https://github.com/cognis-digital/cspbuilder)** — Generate and audit a Content-Security-Policy from a page's resources
  ```bash
  cognis-arsenal install cspbuilder   # pip install cognis-cspbuilder
  ```
- **[dirsight](https://github.com/cognis-digital/dirsight)** — Analyze web content-discovery output (ffuf/gobuster) into ranked endpoints
  ```bash
  cognis-arsenal install dirsight   # pip install cognis-dirsight
  ```
- **[dnsrecon](https://github.com/cognis-digital/dnsrecon)** — Aggregate DNS recon (records, zone hints, takeover candidates)
  ```bash
  cognis-arsenal install dnsrecon   # pip install cognis-dnsrecon
  ```
- **[emailrecon](https://github.com/cognis-digital/emailrecon)** — Aggregate email OSINT (breach hints, MX, SPF/DMARC posture)
  ```bash
  cognis-arsenal install emailrecon   # pip install cognis-emailrecon
  ```
- **[exfilwatch](https://github.com/cognis-digital/exfilwatch)** — Detect DNS/HTTP exfiltration patterns (entropy, beaconing) in logs
  ```bash
  cognis-arsenal install exfilwatch   # pip install cognis-exfilwatch
  ```
- **[hashid](https://github.com/cognis-digital/hashid)** — Identify hash types and estimate crack cost/feasibility
  ```bash
  cognis-arsenal install hashid   # pip install cognis-hashid
  ```
- **[headerscan](https://github.com/cognis-digital/headerscan)** — Grade HTTP security headers (CSP/HSTS/XFO) A-F from a response dump
  ```bash
  cognis-arsenal install headerscan   # pip install cognis-headerscan
  ```
- **[honeyurl](https://github.com/cognis-digital/honeyurl)** — Generate canary URLs/tokens + a matcher for trip events
  ```bash
  cognis-arsenal install honeyurl   # pip install cognis-honeyurl
  ```
- **[iocextract](https://github.com/cognis-digital/iocextract)** — Extract & defang IOCs (IPs/domains/hashes/URLs) from any text
  ```bash
  cognis-arsenal install iocextract   # pip install cognis-iocextract
  ```
- **[jwtinspect](https://github.com/cognis-digital/jwtinspect)** — Decode JWTs and lint for alg=none, weak secrets, and missing claims
  ```bash
  cognis-arsenal install jwtinspect   # pip install cognis-jwtinspect
  ```
- **[logsift](https://github.com/cognis-digital/logsift)** — Detect brute-force, spray, and anomalous auth events in logs
  ```bash
  cognis-arsenal install logsift   # pip install cognis-logsift
  ```
- **[metascrub](https://github.com/cognis-digital/metascrub)** — Strip identifying metadata from docs/images before release
  ```bash
  cognis-arsenal install metascrub   # pip install cognis-metascrub
  ```
- **[nmapdiff](https://github.com/cognis-digital/nmapdiff)** — Diff two scans to surface new hosts/ports/services
  ```bash
  cognis-arsenal install nmapdiff   # pip install cognis-nmapdiff
  ```
- **[pcapsummary](https://github.com/cognis-digital/pcapsummary)** — Summarize flows/talkers/protocols from a pcap text export
  ```bash
  cognis-arsenal install pcapsummary   # pip install cognis-pcapsummary
  ```
- **[phishcheck](https://github.com/cognis-digital/phishcheck)** — Score URLs/emails for phishing signals (lookalike, auth, intent)
  ```bash
  cognis-arsenal install phishcheck   # pip install cognis-phishcheck
  ```
- **[portfan](https://github.com/cognis-digital/portfan)** — Summarize and diff nmap XML into prioritized, attackable findings
  ```bash
  cognis-arsenal install portfan   # pip install cognis-portfan
  ```
- **[ratecheck](https://github.com/cognis-digital/ratecheck)** — Probe API rate-limit/abuse resistance from a request spec
  ```bash
  cognis-arsenal install ratecheck   # pip install cognis-ratecheck
  ```
- **[reposecure](https://github.com/cognis-digital/reposecure)** — One-shot repo security posture grade (secrets/CI/branch rules/deps)
  ```bash
  cognis-arsenal install reposecure   # pip install cognis-reposecure
  ```
- **[s3sniff](https://github.com/cognis-digital/s3sniff)** — Flag risky cloud-bucket ACLs/policies from a listing or policy JSON
  ```bash
  cognis-arsenal install s3sniff   # pip install cognis-s3sniff
  ```
- **[sigmacheck](https://github.com/cognis-digital/sigmacheck)** — Lint and unit-test Sigma detection rules against sample events
  ```bash
  cognis-arsenal install sigmacheck   # pip install cognis-sigmacheck
  ```
- **[ssltriage](https://github.com/cognis-digital/ssltriage)** — Grade TLS config (protocols/ciphers/expiry) from openssl/sslyze output
  ```bash
  cognis-arsenal install ssltriage   # pip install cognis-ssltriage
  ```
- **[ssrfind](https://github.com/cognis-digital/ssrfind)** — Find SSRF-prone sinks and unvalidated URL fetches in code
  ```bash
  cognis-arsenal install ssrfind   # pip install cognis-ssrfind
  ```
- **[subhunt](https://github.com/cognis-digital/subhunt)** — Aggregate & dedupe subdomain enumeration from multiple sources
  ```bash
  cognis-arsenal install subhunt   # pip install cognis-subhunt
  ```
- **[tokenrotate](https://github.com/cognis-digital/tokenrotate)** — Plan + track secret rotation across providers from an inventory
  ```bash
  cognis-arsenal install tokenrotate   # pip install cognis-tokenrotate
  ```
- **[webrecon](https://github.com/cognis-digital/webrecon)** — Fingerprint web tech/CMS/frameworks from headers + body
  ```bash
  cognis-arsenal install webrecon   # pip install cognis-webrecon
  ```
- **[yararun](https://github.com/cognis-digital/yararun)** — Run simple YARA-style string/regex rules over a directory
  ```bash
  cognis-arsenal install yararun   # pip install cognis-yararun
  ```

### Defense & IC (12)

- **[airgap-pkg](https://github.com/cognis-digital/airgap-pkg)** — Self-contained installer for airgapped (SIPR/JWICS-style) environments
  ```bash
  cognis-arsenal install airgap-pkg   # pip install cognis-airgap-pkg
  ```
- **[classmark](https://github.com/cognis-digital/classmark)** — CAPCO-shape classification banner + portion marking library â€” placeholders only
  ```bash
  cognis-arsenal install classmark   # pip install cognis-classmark
  ```
- **[comint-osquery](https://github.com/cognis-digital/comint-osquery)** — DISA STIG-aligned osquery configs + RMF mapper
  ```bash
  cognis-arsenal install comint-osquery   # pip install cognis-comint-osquery
  ```
- **[convoy-or](https://github.com/cognis-digital/convoy-or)** — Military convoy routing w/ escort, dwell, threat-cost overlays
  ```bash
  cognis-arsenal install convoy-or   # pip install cognis-convoy-or
  ```
- **[geoaoi-pro](https://github.com/cognis-digital/geoaoi-pro)** — MIL-STD-2525 / APP-6 symbology + AOI helpers (QGIS-compatible)
  ```bash
  cognis-arsenal install geoaoi-pro   # pip install cognis-geoaoi-pro
  ```
- **[honeypot-mil](https://github.com/cognis-digital/honeypot-mil)** — Honeypot event enrichment + STIX/TAXII + CISA IOC export
  ```bash
  cognis-arsenal install honeypot-mil   # pip install cognis-honeypot-mil
  ```
- **[readiness-rms](https://github.com/cognis-digital/readiness-rms)** — Unit-readiness C-rating dashboard (C1-C4) â€” personnel, equipment, training
  ```bash
  cognis-arsenal install readiness-rms   # pip install cognis-readiness-rms
  ```
- **[redforge-c2](https://github.com/cognis-digital/redforge-c2)** — Authorized red-team engagement governance: scope enforcement, TPI, audit-log overlay
  ```bash
  cognis-arsenal install redforge-c2   # pip install cognis-redforge-c2
  ```
- **[rmf-package](https://github.com/cognis-digital/rmf-package)** — Auto-generate SSP / POAM / SAR (eMASS / Xacta import format)
  ```bash
  cognis-arsenal install rmf-package   # pip install cognis-rmf-package
  ```
- **[scifops](https://github.com/cognis-digital/scifops)** — SCIF/SAPF compliance helpers: badge audit, TPI, escort tracker
  ```bash
  cognis-arsenal install scifops   # pip install cognis-scifops
  ```
- **[sigsurvey-rf](https://github.com/cognis-digital/sigsurvey-rf)** — RF spectrum survey, NTIA/FCC-aware band-plan validator
  ```bash
  cognis-arsenal install sigsurvey-rf   # pip install cognis-sigsurvey-rf
  ```
- **[stigsentry](https://github.com/cognis-digital/stigsentry)** — DISA STIG checker + NIST 800-53 RMF mapper + POAM emitter
  ```bash
  cognis-arsenal install stigsentry   # pip install cognis-stigsentry
  ```

### Meta / Suite (3)

- **[awesome-cognis](https://github.com/cognis-digital/awesome-cognis)** — Awesome Cognis â€” curated list of the Cognis Neural Suite + upstream OSS
  ```bash
  cognis-arsenal install awesome-cognis   # pip install cognis-awesome-cognis
  ```
- **[cognis-digital](https://github.com/cognis-digital/cognis-digital)** — Config files for my GitHub profile.
  ```bash
  cognis-arsenal install cognis-digital   # pip install cognis-cognis-digital
  ```
- **[cognis-neural-suite](https://github.com/cognis-digital/cognis-neural-suite)** — Umbrella catalog of the Cognis Neural Suite (100+ tools)
  ```bash
  cognis-arsenal install cognis-neural-suite   # pip install cognis-cognis-neural-suite
  ```

### Other / Resources (9)

- **[TGC](https://github.com/cognis-digital/TGC)**
  ```bash
  cognis-arsenal install TGC   # pip install cognis-TGC
  ```
- **[assessment-tool](https://github.com/cognis-digital/assessment-tool)**
  ```bash
  cognis-arsenal install assessment-tool   # pip install cognis-assessment-tool
  ```
- **[cognis-workforce-tool](https://github.com/cognis-digital/cognis-workforce-tool)**
  ```bash
  cognis-arsenal install cognis-workforce-tool   # pip install cognis-cognis-workforce-tool
  ```
- **[f22-raptor-sim](https://github.com/cognis-digital/f22-raptor-sim)** — F-22 Raptor Combat Simulator â€” Operation Eastern Shield.
  ```bash
  cognis-arsenal install f22-raptor-sim   # pip install cognis-f22-raptor-sim
  ```
- **[fpv-strike-drone](https://github.com/cognis-digital/fpv-strike-drone)** — FPV Strike Drone â€” first-person drone flight & strike sim.
  ```bash
  cognis-arsenal install fpv-strike-drone   # pip install cognis-fpv-strike-drone
  ```
- **[golfgenie-ai](https://github.com/cognis-digital/golfgenie-ai)**
  ```bash
  cognis-arsenal install golfgenie-ai   # pip install cognis-golfgenie-ai
  ```
- **[operation-blackout](https://github.com/cognis-digital/operation-blackout)** — Operation Blackout â€” a fast browser FPS.
  ```bash
  cognis-arsenal install operation-blackout   # pip install cognis-operation-blackout
  ```
- **[service-tool](https://github.com/cognis-digital/service-tool)**
  ```bash
  cognis-arsenal install service-tool   # pip install cognis-service-tool
  ```
- **[value-widget](https://github.com/cognis-digital/value-widget)**
  ```bash
  cognis-arsenal install value-widget   # pip install cognis-value-widget
  ```

## Resources

- **Suite hub:** [github.com/cognis-digital](https://github.com/cognis-digital) — all 287 repositories
- **Curated sources & datasets:** [github.com/cognis-digital/cognis-sources](https://github.com/cognis-digital/cognis-sources)
- **Machine-readable index:** [`MANIFEST.json`](MANIFEST.json)
- **Cognis.Studio:** [cognis.studio](https://cognis.studio) — agents call every tool over MCP
- **Cognis Digital:** [cognis.digital](https://cognis.digital)

## License

Source-available under the **Cognis Open Collaboration License (COCL) v1.0** — free for personal, internal-evaluation, research, and educational use; **commercial / production use requires a license** (licensing@cognis.digital). See [LICENSE](LICENSE).

## About

**[Cognis Digital](https://cognis.digital)** — Wyoming, USA · *Making Tomorrow Better Today: Advanced Cybersecurity, AI Innovation, and Blockchain Expertise.*
