#!/usr/bin/env bash
# cognis-arsenal installer (Linux/macOS) — consumes MANIFEST.json.
#
# Usage:
#   ./install.sh <tool|domain|all> [--method pip|pipx|git|docker]
#   ./install.sh list
#   ./install.sh search <query>
#
# Bootstrap (one tool):
#   curl -fsSL https://raw.githubusercontent.com/cognis-digital/cognis-arsenal/main/install.sh | bash -s -- mcpscan
set -euo pipefail

ORG="cognis-digital"
RAW="https://raw.githubusercontent.com/${ORG}/cognis-arsenal/main/MANIFEST.json"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd || true)"

err() { printf '%s\n' "$*" >&2; }

# --- locate python (for JSON parsing) ---
PY=""
for c in python3 python; do
  if command -v "$c" >/dev/null 2>&1; then PY="$c"; break; fi
done
[ -n "$PY" ] || { err "Need python3 to read MANIFEST.json"; exit 1; }

# --- locate or fetch MANIFEST.json ---
MANIFEST=""
if [ -n "${SCRIPT_DIR:-}" ] && [ -f "${SCRIPT_DIR}/MANIFEST.json" ]; then
  MANIFEST="${SCRIPT_DIR}/MANIFEST.json"
else
  MANIFEST="$(mktemp)"
  if command -v curl >/dev/null 2>&1; then curl -fsSL "$RAW" -o "$MANIFEST"
  elif command -v wget >/dev/null 2>&1; then wget -qO "$MANIFEST" "$RAW"
  else err "Need curl or wget to fetch MANIFEST.json"; exit 1; fi
fi

usage() {
  cat <<EOF
cognis-arsenal installer
  install.sh <tool|domain|all> [--method pip|pipx|git|docker]
  install.sh list
  install.sh search <query>
EOF
}

[ $# -ge 1 ] || { usage; exit 0; }
SUB="$1"; shift || true

case "$SUB" in
  -h|--help) usage; exit 0 ;;
  list)
    "$PY" - "$MANIFEST" <<'PYEOF'
import json,sys
m=json.load(open(sys.argv[1],encoding="utf-8")); t=m["tools"]
d={}
for v in t.values(): d.setdefault(v["domain_label"],[]).append(v["name"])
print(f"Cognis Arsenal — {m['total']} tools across {len(d)} domains\n")
for lab in sorted(d):
    print(f"{lab} ({len(d[lab])})")
    for n in sorted(d[lab]): print(f"  {n}")
    print()
PYEOF
    exit 0 ;;
  search)
    [ $# -ge 1 ] || { err "search needs a query"; exit 2; }
    "$PY" - "$MANIFEST" "$1" <<'PYEOF'
import json,sys
m=json.load(open(sys.argv[1],encoding="utf-8")); q=sys.argv[2].lower()
h=[v for v in m["tools"].values() if q in v["name"].lower() or q in v["domain"].lower()
   or q in v["domain_label"].lower() or q in (v.get("desc") or "").lower()]
if not h: print(f"No matches for '{sys.argv[2]}'."); sys.exit(1)
print(f"{len(h)} match(es):\n")
for v in sorted(h,key=lambda x:x["name"]):
    dsc=f" — {v['desc']}" if v.get("desc") else ""
    print(f"  {v['name']}  [{v['domain_label']}]{dsc}")
    print(f"    install: {v['pip']}")
PYEOF
    exit $? ;;
esac

# --- install path: SUB is the target ---
TARGET="$SUB"
METHOD="pip"
while [ $# -gt 0 ]; do
  case "$1" in
    --method) METHOD="${2:-}"; shift 2 ;;
    *) shift ;;
  esac
done
case "$METHOD" in pip|pipx|git|docker) ;; *) err "--method must be pip|pipx|git|docker"; exit 2 ;; esac

# emit one shell command per selected tool
CMDS="$("$PY" - "$MANIFEST" "$TARGET" "$METHOD" <<'PYEOF'
import json,sys
m=json.load(open(sys.argv[1],encoding="utf-8")); target,method=sys.argv[2],sys.argv[3]
t=m["tools"]
if target=="all": sel=list(t.values())
elif target in t: sel=[t[target]]
else:
    low=target.lower()
    sel=[v for v in t.values() if v["domain"].lower()==low or v["domain_label"].lower()==low]
if not sel: sys.exit(3)
for v in sel: print(f"{v['name']}\t{v[method]}")
PYEOF
)" || { err "No matching tool or domain: $TARGET (try: install.sh list)"; exit 3; }

RC=0
while IFS=$'\t' read -r NAME CMD; do
  [ -n "$NAME" ] || continue
  printf '==> %s :: %s\n' "$NAME" "$CMD"
  if [ "$METHOD" = "docker" ]; then
    printf '    (docker recipe — copy/paste to run)\n'; continue
  fi
  EXE="${CMD%% *}"
  if ! command -v "$EXE" >/dev/null 2>&1; then
    err "    [skip] '$EXE' not on PATH"; RC=1; continue
  fi
  if ! sh -c "$CMD"; then err "    [fail] $NAME"; RC=1; fi
done <<< "$CMDS"
exit $RC
