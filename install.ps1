<#
.SYNOPSIS
  cognis-arsenal installer (Windows PowerShell) - consumes MANIFEST.json.

.DESCRIPTION
  Install Cognis Neural Suite tools by <tool|domain|all>, via pip|pipx|git|docker.
  Also supports 'list' and 'search <query>' subcommands.

.EXAMPLE
  .\install.ps1 mcpscan
  .\install.ps1 ai-security --method pipx
  .\install.ps1 all --method git
  .\install.ps1 list
  .\install.ps1 search mcp

.NOTES
  Bootstrap: irm https://raw.githubusercontent.com/cognis-digital/cognis-arsenal/main/install.ps1 | iex
#>
[CmdletBinding()]
param(
  [Parameter(Position = 0)][string]$Target,
  [Parameter(Position = 1)][string]$Query,
  [ValidateSet('pip', 'pipx', 'git', 'docker')][string]$Method = 'pip'
)

$ErrorActionPreference = 'Stop'
$Org = 'cognis-digital'
$Raw = "https://raw.githubusercontent.com/$Org/cognis-arsenal/main/MANIFEST.json"

function Get-Manifest {
  $local = Join-Path $PSScriptRoot 'MANIFEST.json'
  if (Test-Path $local) {
    return (Get-Content -Raw -Path $local -Encoding UTF8 | ConvertFrom-Json)
  }
  return (Invoke-RestMethod -Uri $Raw)
}

function Get-ToolList {
  param($Manifest)
  return $Manifest.tools.PSObject.Properties | ForEach-Object { $_.Value }
}

function Show-Usage {
  Write-Output "cognis-arsenal installer"
  Write-Output "  install.ps1 <tool|domain|all> [-Method pip|pipx|git|docker]"
  Write-Output "  install.ps1 list"
  Write-Output "  install.ps1 search <query>"
}

if (-not $Target -or $Target -eq '-h' -or $Target -eq '--help') {
  Show-Usage
  return
}

$manifest = Get-Manifest
$all = Get-ToolList -Manifest $manifest

switch ($Target) {
  'list' {
    $groups = $all | Group-Object -Property domain_label
    Write-Output ("Cognis Arsenal - {0} tools across {1} domains`n" -f $manifest.total, $groups.Count)
    foreach ($g in ($groups | Sort-Object Name)) {
      Write-Output ("{0} ({1})" -f $g.Name, $g.Count)
      foreach ($t in ($g.Group | Sort-Object name)) { Write-Output ("  {0}" -f $t.name) }
      Write-Output ''
    }
    return
  }
  'search' {
    if (-not $Query) { Write-Error 'search needs a query'; return }
    $q = $Query.ToLower()
    $hits = $all | Where-Object {
      $_.name.ToLower().Contains($q) -or $_.domain.ToLower().Contains($q) -or
      $_.domain_label.ToLower().Contains($q) -or
      ($_.desc -and $_.desc.ToLower().Contains($q))
    }
    if (-not $hits) { Write-Output "No matches for '$Query'."; return }
    Write-Output ("{0} match(es) for '{1}':`n" -f @($hits).Count, $Query)
    foreach ($t in ($hits | Sort-Object name)) {
      $d = if ($t.desc) { " - $($t.desc)" } else { '' }
      Write-Output ("  {0}  [{1}]{2}" -f $t.name, $t.domain_label, $d)
      Write-Output ("    install: {0}" -f $t.pip)
    }
    return
  }
}

# install path
$low = $Target.ToLower()
if ($Target -eq 'all') {
  $sel = $all
} elseif ($manifest.tools.PSObject.Properties.Name -contains $Target) {
  $sel = @($manifest.tools.$Target)
} else {
  $sel = $all | Where-Object { $_.domain.ToLower() -eq $low -or $_.domain_label.ToLower() -eq $low }
}

if (-not $sel -or @($sel).Count -eq 0) {
  Write-Error "No matching tool or domain: $Target (try: install.ps1 list)"
  return
}

$rc = 0
foreach ($t in $sel) {
  $cmd = $t.$Method
  Write-Output ("==> {0} ({1}) :: {2}" -f $t.name, $t.domain_label, $cmd)
  if ($Method -eq 'docker') { Write-Output '    (docker recipe - copy/paste to run)'; continue }
  $exe = ($cmd -split ' ')[0]
  if (-not (Get-Command $exe -ErrorAction SilentlyContinue)) {
    Write-Warning "    [skip] '$exe' not on PATH"; $rc = 1; continue
  }
  & cmd /c $cmd
  if ($LASTEXITCODE -ne 0) { Write-Warning "    [fail] $($t.name)"; $rc = 1 }
}
exit $rc
