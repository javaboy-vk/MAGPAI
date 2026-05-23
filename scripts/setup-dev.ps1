Write-Host "==========================================="
Write-Host "MAGPAI Development Setup – v1.0"
Write-Host "==========================================="

python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\pip.exe install -r requirements.txt

Write-Host "Setup complete."
