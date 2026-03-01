# Cardinal Otunga School App - Public Access (PowerShell)
# This script runs the Django server for PUBLIC access

Write-Host ""
Write-Host "===================================================="  -ForegroundColor Cyan
Write-Host "  Cardinal Otunga School App - PUBLIC ACCESS"  -ForegroundColor Cyan
Write-Host "===================================================="  -ForegroundColor Cyan
Write-Host ""
Write-Host "Your app is now accessible to EVERYONE!" -ForegroundColor Green
Write-Host ""
Write-Host "Option 1: Local Network Only (same network)" -ForegroundColor Yellow
Write-Host "  Open: http://localhost:8000"
Write-Host "  From other computer on network: http://your-computer-name:8000"
Write-Host ""
Write-Host "Option 2: PUBLIC Internet Access (use ngrok)" -ForegroundColor Yellow
Write-Host "  1. Download ngrok from https://ngrok.com/download"
Write-Host "  2. In another terminal, run: ngrok http 8000"
Write-Host "  3. Share the public URL with anyone"
Write-Host ""
Write-Host "See PUBLIC-DEPLOYMENT.md for complete instructions!"
Write-Host ""

Set-Location -Path $PSScriptRoot
python manage.py runserver 0.0.0.0:8000

Read-Host "Press Enter to exit"
