param(
    [string]$VaultPath = "D:\DiavgeiaVault",
    [string]$TargetRelativePath = "Engineering\MAGPAI\Session1"
)

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$sourceRoot = Join-Path $repoRoot "diavgeia"
$sessionSource = Join-Path $sourceRoot "MAGPAI\Session1"
$imageSources = @(
    "magpie.avif"
    "full_stack_ai_ml_mental_model_16_layers_magpai_start.png"
    "magpai_from_question_to_insight.png"
) | ForEach-Object {
    Join-Path $repoRoot "images\$_"
}

if (-not (Test-Path -LiteralPath $VaultPath)) {
    throw "Vault path does not exist: $VaultPath"
}

if (-not (Test-Path -LiteralPath $sessionSource)) {
    throw "Session source path does not exist: $sessionSource"
}

$targetRoot = Join-Path $VaultPath $TargetRelativePath
$homeTarget = Join-Path $VaultPath "Engineering\MAGPAI"
$imageTarget = Join-Path $VaultPath "Attachments\Images\MAGPAI"

New-Item -ItemType Directory -Force -Path $targetRoot | Out-Null
New-Item -ItemType Directory -Force -Path $homeTarget | Out-Null
New-Item -ItemType Directory -Force -Path $imageTarget | Out-Null

$resolvedVault = (Resolve-Path -LiteralPath $VaultPath).Path
$resolvedTarget = (Resolve-Path -LiteralPath $targetRoot).Path
if (-not $resolvedTarget.StartsWith($resolvedVault, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "Refusing to clean target outside vault: $resolvedTarget"
}

Get-ChildItem -LiteralPath $targetRoot -File -Filter "*.md" | ForEach-Object {
    Remove-Item -LiteralPath $_.FullName -Force
}

$homeSource = Join-Path $sourceRoot "magpai-home-v1.0.md"
Copy-Item -LiteralPath $homeSource -Destination (Join-Path $homeTarget "MAGPAI - Home.md") -Force
Copy-Item -LiteralPath (Join-Path $sourceRoot "README.md") -Destination (Join-Path $homeTarget "MAGPAI - Diavgeia Export Notes.md") -Force

$staleFolderNote = Join-Path $homeTarget "MAGPAI.md"
if (Test-Path -LiteralPath $staleFolderNote) {
    Remove-Item -LiteralPath $staleFolderNote -Force
}

$imageSources | ForEach-Object {
    if (Test-Path -LiteralPath $_) {
        Copy-Item -LiteralPath $_ -Destination (Join-Path $imageTarget (Split-Path $_ -Leaf)) -Force
    }
}

Get-ChildItem -LiteralPath $sessionSource -File -Filter "*.md" | ForEach-Object {
    Copy-Item -LiteralPath $_.FullName -Destination (Join-Path $targetRoot $_.Name) -Force
}

$exportStamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss zzz"
$manifestPath = Join-Path $targetRoot "_MAGPAI Session 1 Export Manifest.md"

$manifest = @(
    "# MAGPAI Session 1 Export Manifest"
    ""
    "Exported: $exportStamp"
    "Source repository: $repoRoot"
    "Source folder: $sessionSource"
    "Vault target: $targetRoot"
    ""
    "## Exported Files"
    ""
)

Get-ChildItem -LiteralPath $sessionSource -File -Filter "*.md" |
    Sort-Object Name |
    ForEach-Object {
        $manifest += "- $($_.Name)"
    }

Set-Content -LiteralPath $manifestPath -Value $manifest -Encoding UTF8

Write-Host "Export complete."
Write-Host "Vault target: $targetRoot"
