Write-Host "==========================================="
Write-Host "MAGPAI Chatbot Demo - v0.1"
Write-Host "==========================================="

$env:PYTHONPATH = Join-Path (Resolve-Path ".") "src"

if ($args.Count -eq 0) {
    .\.venv\Scripts\python.exe -m magpai.chatbot
} else {
    .\.venv\Scripts\python.exe -m magpai.chatbot @args
}
