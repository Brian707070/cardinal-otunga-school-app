# Cardinal Otunga School App - Complete Automated Setup
# This script handles everything: hosts file setup + server start
# IMPORTANT: Right-click this file (or run PowerShell as Admin) to execute

# Check for Administrator privileges
$isAdmin = ([Security.Principal.WindowsIdentity]::GetCurrent()).Groups -match "S-1-5-32-544"
if (-not $isAdmin) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "ERROR: Administrator privileges required!" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please run PowerShell as Administrator:" -ForegroundColor Yellow
    Write-Host "1. Press Windows Key + X" -ForegroundColor Yellow
    Write-Host "2. Select 'Windows PowerShell (Admin)'" -ForegroundColor Yellow
    Write-Host "3. Run: .\setup-and-run.ps1" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Cardinal Otunga School App Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Add to hosts file
Write-Host "Step 1: Configuring hosts file..." -ForegroundColor Yellow
$hostsPath = "$env:windir\System32\drivers\etc\hosts"
$hostEntry = "127.0.0.1       chibibyte.local"

$hostsContent = Get-Content $hostsPath -Raw
if ($hostsContent -notmatch [regex]::Escape("$hostEntry")) {
    Add-Content -Path $hostsPath -Value "`n$hostEntry" -Encoding UTF8
    Write-Host "[SUCCESS] ✓ Added chibibyte.local to hosts file" -ForegroundColor Green
} else {
    Write-Host "[INFO] ℹ chibibyte.local already configured" -ForegroundColor Green
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Step 2: Starting Django Server" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "✓ Server starting on: http://chibibyte.local/" -ForegroundColor Green
Write-Host ""
Write-Host "NEXT STEPS:" -ForegroundColor Cyan
Write-Host "1. Open your browser" -ForegroundColor White
Write-Host "2. Go to: http://chibibyte.local/" -ForegroundColor White
Write-Host ""
Write-Host "FOR OTHER DEVICES ON YOUR NETWORK:" -ForegroundColor Cyan
Write-Host "1. Find your PC's IP address:" -ForegroundColor White
Write-Host "   - Open Command Prompt and run: ipconfig" -ForegroundColor White
Write-Host "   - Look for IPv4 Address (e.g., 192.168.1.100)" -ForegroundColor White
Write-Host ""
Write-Host "2. On other devices, add to hosts file:" -ForegroundColor White
Write-Host "   Windows: C:\Windows\System32\drivers\etc\hosts" -ForegroundColor White
Write-Host "   Mac/Linux: /etc/hosts" -ForegroundColor White
Write-Host "   Add: 192.168.X.X  chibibyte.local" -ForegroundColor White
Write-Host ""
Write-Host "3. Access from any device: http://chibibyte.local/" -ForegroundColor White
Write-Host ""
Write-Host "To STOP server: Press Ctrl+C" -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Change to app directory
Set-Location $PSScriptRoot

# Start server
python manage.py runserver 0.0.0.0:80

Read-Host "Press Enter to exit"
