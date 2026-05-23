Write-Host "==========================================="
Write-Host "MAGPAI Clean Generated Files – v1.0"
Write-Host "==========================================="

Remove-Item -Recurse -Force site -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force build -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force dist -ErrorAction SilentlyContinue

Write-Host "Clean complete."
