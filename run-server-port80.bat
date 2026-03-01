@echo off
REM This script runs the Django server on port 80 (requires Administrator)
REM Right-click and select "Run as administrator"

echo.
echo Starting Cardinal Otunga School App on chibibyte.local (Port 80)
echo.
echo Notice: This requires Administrator privileges
echo Open a new browser tab and navigate to: http://chibibyte.local
echo.

cd /d "%~dp0"
python manage.py runserver 0.0.0.0:80

pause
