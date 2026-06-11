<#
.SYNOPSIS
  Cognis Arsenal - guided setup bootstrap (Windows PowerShell).

.DESCRIPTION
  Launches the guided wizard that walks you through installing the suite.

.EXAMPLE
  .\setup.ps1
  irm https://raw.githubusercontent.com/cognis-digital/cognis-arsenal/master/setup.ps1 | iex
#>
[CmdletBinding()]
param([switch]$DryRun)

$ErrorActionPreference = 'Stop'
$Org = 'cognis-digital'
$RawBase = "https://raw.githubusercontent.com/$Org/cognis-arsenal/master"

# Locate python.
$py = $null
foreach ($c in 'python', 'python3', 'py') {
  if (Get-Command $c -ErrorAction SilentlyContinue) { $py = $c; break }
}
if (-not $py) { Write-Error 'Need Python to run the setup wizard.'; return }

$extra = @()
if ($DryRun) { $extra += '--dry-run' }

# Run from a local checkout if present; otherwise fetch the kit into a temp dir.
$local = if ($PSScriptRoot) { Join-Path $PSScriptRoot 'install.py' } else { $null }
if ($local -and (Test-Path $local)) {
  & $py $local setup @extra
  exit $LASTEXITCODE
}

$tmp = Join-Path ([System.IO.Path]::GetTempPath()) ("cognis-arsenal-" + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $tmp -Force | Out-Null
try {
  foreach ($f in 'install.py', 'setup_wizard.py', 'MANIFEST.json') {
    Invoke-WebRequest -Uri "$RawBase/$f" -OutFile (Join-Path $tmp $f) -UseBasicParsing
  }
  & $py (Join-Path $tmp 'install.py') setup @extra
  exit $LASTEXITCODE
}
finally {
  Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
}
