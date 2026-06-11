#!/usr/bin/env bash
# Cognis Arsenal — guided setup bootstrap (Linux/macOS).
#
# Launches the guided wizard that walks you through installing the suite.
#
# Run locally:
#   ./setup.sh
# Or remotely (one line):
#   curl -fsSL https://raw.githubusercontent.com/cognis-digital/cognis-arsenal/master/setup.sh | bash
set -euo pipefail

ORG="cognis-digital"
RAW_BASE="https://raw.githubusercontent.com/${ORG}/cognis-arsenal/master"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd || true)"

# Locate python.
PY=""
for c in python3 python; do
  if command -v "$c" >/dev/null 2>&1; then PY="$c"; break; fi
done
[ -n "$PY" ] || { printf '%s\n' "Need python3 to run the setup wizard." >&2; exit 1; }

# Run from a local checkout if present; otherwise fetch the kit into a temp dir.
if [ -n "${SCRIPT_DIR:-}" ] && [ -f "${SCRIPT_DIR}/install.py" ]; then
  exec "$PY" "${SCRIPT_DIR}/install.py" setup "$@"
fi

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
fetch() {
  if command -v curl >/dev/null 2>&1; then curl -fsSL "$1" -o "$2"
  elif command -v wget >/dev/null 2>&1; then wget -qO "$2" "$1"
  else printf '%s\n' "Need curl or wget." >&2; exit 1; fi
}
fetch "${RAW_BASE}/install.py"      "${TMP}/install.py"
fetch "${RAW_BASE}/setup_wizard.py" "${TMP}/setup_wizard.py"
fetch "${RAW_BASE}/MANIFEST.json"   "${TMP}/MANIFEST.json"
exec "$PY" "${TMP}/install.py" setup "$@"
