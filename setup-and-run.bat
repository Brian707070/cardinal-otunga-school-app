@echo off
REM Complete Setup Script for Cardinal Otunga School App
REM This script requires Administrator privileges
REM Right-click and select "Run as administrator"

setlocal enabledelayedexpansion

REM Check for admin privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo.
    echo ========================================
    echo ERROR: This script requires Administrator privileges!
    echo ========================================
    echo.
    echo Please right-click this file and select "Run as administrator"
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Cardinal Otunga School App - Setup
echo ========================================
echo.

REM Step 1: Add to hosts file
echo Step 1: Adding chibibyte.local to hosts file...
findstr /c:"127.0.0.1 chibibyte.local" %windir%\System32\drivers\etc\hosts >nul
if %errorLevel% neq 0 (
    echo 127.0.0.1 chibibyte.local >> %windir%\System32\drivers\etc\hosts
    echo [SUCCESS] Added chibibyte.local to hosts file
) else (
    echo [INFO] chibibyte.local already in hosts file
)

echo.
echo ========================================
echo Step 2: Starting Django Server on Port 80
echo ========================================
echo.
echo Server starting on http://chibibyte.local/
echo.
echo Open your browser and visit:
echo   http://chibibyte.local/
echo.
echo To access from other devices on the same network:
echo   1. Find your computer's IP: ipconfig (look for IPv4 Address)
echo   2. On other devices, add to hosts file:
echo      192.168.X.X  chibibyte.local
echo   3. Access via: http://chibibyte.local/
echo.
echo Press Ctrl+C to stop the server
echo.
echo ========================================
echo.

REM Change to app directory
cd /d "%~dp0"

REM Start server on port 80
python manage.py runserver 0.0.0.0:80

pause
