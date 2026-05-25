Add-Type -AssemblyName System.Drawing

$outputPath = Join-Path (Resolve-Path ".").Path "images\full_stack_ai_ml_mental_model_16_layers_science_math.png"

$width = 2600
$height = 1500
$bitmap = [System.Drawing.Bitmap]::new($width, $height)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

function New-Brush([int]$r, [int]$g, [int]$b, [int]$a = 255) {
    [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb($a, $r, $g, $b))
}

function Draw-RoundedRect(
    [System.Drawing.Graphics]$Graphics,
    [System.Drawing.RectangleF]$Rectangle,
    [float]$Radius,
    [System.Drawing.Brush]$Fill,
    [System.Drawing.Pen]$Pen
) {
    $path = [System.Drawing.Drawing2D.GraphicsPath]::new()
    $diameter = $Radius * 2
    $path.AddArc($Rectangle.X, $Rectangle.Y, $diameter, $diameter, 180, 90)
    $path.AddArc($Rectangle.Right - $diameter, $Rectangle.Y, $diameter, $diameter, 270, 90)
    $path.AddArc($Rectangle.Right - $diameter, $Rectangle.Bottom - $diameter, $diameter, $diameter, 0, 90)
    $path.AddArc($Rectangle.X, $Rectangle.Bottom - $diameter, $diameter, $diameter, 90, 90)
    $path.CloseFigure()
    $Graphics.FillPath($Fill, $path)
    $Graphics.DrawPath($Pen, $path)
    $path.Dispose()
}

function Draw-WrappedText(
    [System.Drawing.Graphics]$Graphics,
    [string]$Text,
    [System.Drawing.Font]$Font,
    [System.Drawing.Brush]$Brush,
    [float]$X,
    [float]$Y,
    [float]$Width,
    [float]$Height
) {
    $format = [System.Drawing.StringFormat]::new()
    $format.Alignment = [System.Drawing.StringAlignment]::Near
    $format.LineAlignment = [System.Drawing.StringAlignment]::Near
    $format.Trimming = [System.Drawing.StringTrimming]::EllipsisWord
    $rectangle = [System.Drawing.RectangleF]::new($X, $Y, $Width, $Height)
    $Graphics.DrawString($Text, $Font, $Brush, $rectangle, $format)
    $format.Dispose()
}

$layers = @(
    @{ N = "1"; C = @(30, 160, 255); T = "COMPUTING FOUNDATION"; S = "Discrete math; Boolean algebra; algorithms; information theory; architecture; semiconductor physics." },
    @{ N = "2"; C = @(70, 210, 105); T = "MATHEMATICS FOUNDATION"; S = "Linear algebra; calculus; probability; statistics; optimization; numerical analysis." },
    @{ N = "3"; C = @(170, 110, 255); T = "DATA FOUNDATION"; S = "Measurement theory; sampling; experimental design; statistics; database theory; signal processing." },
    @{ N = "4"; C = @(250, 225, 25); T = "CLASSICAL MACHINE LEARNING"; S = "Statistics; probability; optimization; decision theory; geometry; Bayesian inference." },
    @{ N = "5"; C = @(30, 220, 225); T = "DEEP LEARNING"; S = "Linear algebra; multivariable calculus; optimization; graph theory; dynamical systems." },
    @{ N = "6"; C = @(255, 160, 25); T = "NLP & LANGUAGE MODELING"; S = "Linguistics; formal language theory; probability; information theory; vector-space geometry." },
    @{ N = "7"; C = @(80, 220, 120); T = "TRANSFORMERS"; S = "Tensor algebra; linear algebra; optimization; graph theory; signal processing; information theory." },
    @{ N = "8"; C = @(185, 125, 255); T = "LARGE LANGUAGE MODELS"; S = "Statistical learning theory; probability; optimization; high-dimensional geometry; cognitive science." },
    @{ N = "9"; C = @(255, 225, 20); T = "EMBEDDINGS & VECTOR SEARCH"; S = "Vector spaces; metric geometry; topology; nearest-neighbor search; information retrieval." },
    @{ N = "10"; C = @(30, 220, 225); T = "RAG (RETRIEVAL-AUGMENTED GENERATION)"; S = "Information retrieval; ranking theory; graph theory; knowledge representation; statistics." },
    @{ N = "11"; C = @(255, 170, 30); T = "MULTIMODAL AI"; S = "Signal processing; computer vision; acoustics; geometry; statistics; human perception science." },
    @{ N = "12"; C = @(45, 170, 255); T = "TOOLS & INTEGRATIONS"; S = "Systems engineering; control theory; database theory; network science; reliability engineering." },
    @{ N = "13"; C = @(85, 220, 110); T = "AI AGENTS"; S = "Decision theory; reinforcement learning; planning; game theory; control theory; cognitive science." },
    @{ N = "14"; C = @(190, 115, 255); T = "AI APPLICATION ARCHITECTURE"; S = "Software engineering; distributed systems; queueing theory; security; human-computer interaction." },
    @{ N = "15"; C = @(255, 160, 25); T = "MLOPS / LLMOPS / GEN AIOPS"; S = "Statistics; experimental design; reliability engineering; observability; operations research." },
    @{ N = "16"; C = @(255, 65, 65); T = "RESPONSIBLE AI & GOVERNANCE"; S = "Ethics; law; risk science; causal inference; statistics; security science; sociology." }
)

$background = [System.Drawing.Drawing2D.LinearGradientBrush]::new(
    [System.Drawing.Rectangle]::new(0, 0, $width, $height),
    [System.Drawing.Color]::FromArgb(4, 9, 18),
    [System.Drawing.Color]::FromArgb(10, 18, 34),
    90
)
$graphics.FillRectangle($background, 0, 0, $width, $height)

$white = New-Brush 245 248 255
$muted = New-Brush 218 226 238
$dim = New-Brush 165 176 194
$yellow = New-Brush 255 220 20

$titleFont = [System.Drawing.Font]::new("Segoe UI", 44, [System.Drawing.FontStyle]::Bold)
$bridgeFont = [System.Drawing.Font]::new("Segoe UI", 32, [System.Drawing.FontStyle]::Bold)
$layerFont = [System.Drawing.Font]::new("Segoe UI", 22, [System.Drawing.FontStyle]::Bold)
$scienceFont = [System.Drawing.Font]::new("Segoe UI", 26, [System.Drawing.FontStyle]::Regular)
$numberFont = [System.Drawing.Font]::new("Segoe UI", 27, [System.Drawing.FontStyle]::Bold)

$xNumber = 55
$xLayer = 175
$xScience = 850
$graphics.DrawString("AI / ML layers", $titleFont, $yellow, $xLayer, 28)
$graphics.DrawString("based on:", $bridgeFont, $dim, 645, 40)
$graphics.DrawString("Math & Sciences", $titleFont, $white, 910, 28)
$rowY = 140
$rowHeight = 73
$rowGap = 9

foreach ($layer in $layers) {
    $color = $layer.C
    $pen = [System.Drawing.Pen]::new([System.Drawing.Color]::FromArgb($color[0], $color[1], $color[2]), 2)
    $fill = New-Brush $color[0] $color[1] $color[2] 22
    $layerBrush = New-Brush $color[0] $color[1] $color[2]

    Draw-RoundedRect $graphics ([System.Drawing.RectangleF]::new(44, $rowY, $width - 88, $rowHeight)) 12 $fill $pen
    Draw-RoundedRect $graphics ([System.Drawing.RectangleF]::new($xNumber, $rowY + 9, 88, 55)) 10 (New-Brush $color[0] $color[1] $color[2] 55) $pen

    $numberX = if ($layer.N.Length -eq 1) { $xNumber + 30 } else { $xNumber + 19 }
    $graphics.DrawString($layer.N, $numberFont, $layerBrush, $numberX, $rowY + 12)
    $graphics.DrawString($layer.T, $layerFont, $layerBrush, $xLayer, $rowY + 19)
    Draw-WrappedText $graphics $layer.S $scienceFont $white $xScience ($rowY + 12) 1705 52

    $rowY += $rowHeight + $rowGap
}

$bitmap.Save($outputPath, [System.Drawing.Imaging.ImageFormat]::Png)

$graphics.Dispose()
$bitmap.Dispose()
$background.Dispose()

Write-Host "Created $outputPath"
