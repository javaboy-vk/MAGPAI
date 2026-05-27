param(
    [string]$CsvPath = "D:\DiavgeiaVault\Engineering\MAGPAI\Learning Path\learning_time_log.csv",
    [string]$DashboardPath = "D:\DiavgeiaVault\Engineering\MAGPAI\Learning Path\MAGPAI-Learning-Clock-Dashboard.md",
    [string]$ChartPath = "D:\DiavgeiaVault\Engineering\MAGPAI\Learning Path\MAGPAI-Learning-Time-Chart.svg"
)

$ErrorActionPreference = "Stop"

function Convert-DurationToSeconds([string]$value) {
    if ([string]::IsNullOrWhiteSpace($value)) { return 0 }
    $parts = $value.Split(':')
    if ($parts.Count -ne 3) { return 0 }
    return ([int]$parts[0] * 3600) + ([int]$parts[1] * 60) + [int]$parts[2]
}

function Convert-SecondsToHours([int]$seconds) {
    return [math]::Round($seconds / 3600, 2).ToString("0.00", [Globalization.CultureInfo]::InvariantCulture)
}

function Format-DateShort([string]$value) {
    if ([string]::IsNullOrWhiteSpace($value) -or $value.Trim().ToUpperInvariant() -eq "TOTAL") { return "N/A" }
    $parsed = [datetime]::MinValue
    if ([datetime]::TryParse($value, [ref]$parsed)) { return $parsed.ToString("MM-dd-yy") }
    return $value
}

function Escape-SvgText([string]$value) {
    return [Security.SecurityElement]::Escape($value)
}

function Add-SvgText(
    [System.Collections.Generic.List[string]]$Svg,
    [int]$X,
    [int]$Y,
    [string]$Text,
    [string]$Extra = ""
) {
    $Svg.Add("<text x=""$X"" y=""$Y"" $Extra>$(Escape-SvgText $Text)</text>")
}

function Add-SvgRect(
    [System.Collections.Generic.List[string]]$Svg,
    [int]$X,
    [int]$Y,
    [int]$Width,
    [int]$Height,
    [string]$Fill,
    [string]$Extra = ""
) {
    $Svg.Add("<rect x=""$X"" y=""$Y"" width=""$Width"" height=""$Height"" fill=""$Fill"" $Extra />")
}

if (-not (Test-Path -LiteralPath $CsvPath)) {
    throw "CSV path does not exist: $CsvPath"
}

$rows = Import-Csv -LiteralPath $CsvPath
$totalRow = $rows | Where-Object { $_.date.Trim().ToUpperInvariant() -eq "TOTAL" } | Select-Object -First 1
$sessionRows = @($rows | Where-Object { $_.date.Trim().ToUpperInvariant() -ne "TOTAL" })

if (-not $totalRow) {
    throw "No TOTAL row found in $CsvPath"
}

$categories = @(
    @{ Label = "Reading"; Field = "reading"; Meaning = "Book/chapter reading and review" },
    @{ Label = "Outlining"; Field = "outlining"; Meaning = "Creating or refining the learning outline" },
    @{ Label = "Memorizing"; Field = "memorizing"; Meaning = "Recall, review, spaced repetition, flashcards" },
    @{ Label = "Experimenting"; Field = "experimenting"; Meaning = "Code experiments in MAGPAI" },
    @{ Label = "Audiobook"; Field = "audiobook"; Meaning = "Listening to related audiobook material" },
    @{ Label = "Update Diavgeia"; Field = "update_diavgeia"; Meaning = "Documenting/refining the concept in Diavgeia" },
    @{ Label = "Promote stable concept"; Field = "promote_stable_concept"; Meaning = "Moving stable concepts into MAGPAI" }
)

$categoryValues = @(
    foreach ($category in $categories) {
        $time = $totalRow.($category.Field)
        $seconds = Convert-DurationToSeconds $time
        [pscustomobject]@{
            Label = $category.Label
            Time = $time
            Seconds = $seconds
            Hours = Convert-SecondsToHours $seconds
        }
    }
)

$maxSeconds = [Math]::Max(($categoryValues | Measure-Object -Property Seconds -Maximum).Maximum, 1)
$startDate = if ($sessionRows.Count -gt 0) { Format-DateShort $sessionRows[0].date } else { "N/A" }
$lastUpdate = if ($sessionRows.Count -gt 0) { Format-DateShort $sessionRows[-1].date } else { "N/A" }
$generated = Get-Date -Format "yyyy-MM-dd HH:mm:ss zzz"

$svg = New-Object System.Collections.Generic.List[string]
$svg.Add("<svg xmlns=""http://www.w3.org/2000/svg"" width=""760"" height=""360"" viewBox=""0 0 760 360"" role=""img"" aria-label=""MAGPAI learning time by category"">")
$svg.Add("<style>")
$svg.Add("text{font-family:Segoe UI,Arial,sans-serif;fill:#102a43}.category{font-size:11px}.hours{font-size:11px;fill:#52606d}.barLabel{font-size:12px;font-weight:700;fill:#ffffff}.metric{font-size:14px}.metricValue{font-size:14px;font-weight:700;fill:#1f4e79}")
$svg.Add("</style>")
Add-SvgRect $svg 1 1 758 322 "#f8fbff" "stroke=""#c8d7e8"" stroke-width=""1"" rx=""14"""

$chartTop = 28
$chartBottom = 220
$maxBarHeight = 190
$barWidth = 86
$slot = 96
$left = 23

for ($i = 0; $i -lt $categoryValues.Count; $i++) {
    $item = $categoryValues[$i]
    $barHeight = [Math]::Max([Math]::Round(($item.Seconds / $maxSeconds) * $maxBarHeight), 28)
    $x = $left + ($i * $slot)
    $y = $chartBottom - $barHeight

    Add-SvgRect $svg $x $y $barWidth $barHeight "#2f75b5" "rx=""6"""
    Add-SvgText $svg ($x + 20) ($y + 18) $item.Time "class=""barLabel"""

    if ($item.Label -eq "Promote stable concept") {
        Add-SvgText $svg ($x + 3) 243 "Promote stable" "class=""category"""
        Add-SvgText $svg ($x + 20) 258 "concept" "class=""category"""
    } else {
        Add-SvgText $svg ($x + 18) 243 $item.Label "class=""category"""
    }
    Add-SvgText $svg ($x + 31) 277 "$($item.Hours)h" "class=""hours"""
}

$svg.Add("<line x1=""23"" y1=""284"" x2=""713"" y2=""284"" stroke=""#8db3e2"" stroke-width=""1"" />")
Add-SvgText $svg 23 315 "Total time:" "class=""metric"""
Add-SvgText $svg 102 315 $totalRow.total "class=""metricValue"""
Add-SvgText $svg 205 315 "Total pages read:" "class=""metric"""
Add-SvgText $svg 333 315 $totalRow.pages_read "class=""metricValue"""
Add-SvgText $svg 430 315 "Start Date:" "class=""metric"""
Add-SvgText $svg 510 315 $startDate "class=""metricValue"""
Add-SvgText $svg 595 315 "Last Update:" "class=""metric"""
Add-SvgText $svg 685 315 $lastUpdate "class=""metricValue"""
$svg.Add("</svg>")
Set-Content -LiteralPath $ChartPath -Value $svg -Encoding UTF8

$lines = New-Object System.Collections.Generic.List[string]
$lines.Add("# MAGPAI Learning Time")
$lines.Add("")
$lines.Add("![[MAGPAI-Learning-Time-Chart.svg]]")
$lines.Add("")
$lines.Add("---")
$lines.Add("")
$lines.Add("###### Source")
$lines.Add("")
$lines.Add('`Engineering/MAGPAI/Learning Path/learning_time_log.csv`')
$lines.Add("")
$lines.Add("###### Categories")
$lines.Add("")
$lines.Add("| Category | Meaning |")
$lines.Add("|---|---|")
foreach ($category in $categories) {
    $lines.Add("| $($category.Label) | $($category.Meaning) |")
}
$lines.Add("")
$lines.Add("###### Rule")
$lines.Add("")
$lines.Add("Run the Learning Clock. The session is saved when the app closes.")
$lines.Add("")
$lines.Add("###### Generated")
$lines.Add("")
$lines.Add($generated)

Set-Content -LiteralPath $DashboardPath -Value $lines -Encoding UTF8
Write-Host "Updated dashboard: $DashboardPath"
Write-Host "Updated chart: $ChartPath"
