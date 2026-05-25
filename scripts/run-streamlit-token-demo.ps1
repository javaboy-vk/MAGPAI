Write-Host "==========================================="
Write-Host "MAGPAI Token Visualizer – v1.0"
Write-Host "==========================================="

$env:PYTHONPATH = Join-Path (Resolve-Path ".") "src"
.\.venv\Scripts\streamlit.exe run src/magpai/tokenization/token_streamlit_app.py
