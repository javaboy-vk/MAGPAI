Write-Host "==========================================="
Write-Host "MAGPAI Local AI Gateway – v1.0"
Write-Host "==========================================="

.\.venv\Scripts\uvicorn.exe apps.fastapi.local_ai_gateway_app:app --reload --host 127.0.0.1 --port 18081
