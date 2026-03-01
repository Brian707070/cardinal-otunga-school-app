@echo off
REM This script runs the Django server for PUBLIC access
REM The app will be accessible to EVERYONE over the internet (if using ngrok)
REM See PUBLIC-DEPLOYMENT.md for full instructions

echo.
echo ====================================================
echo   Cardinal Otunga School App - PUBLIC ACCESS
echo ====================================================
echo.
echo Your app is now accessible to EVERYONE!
echo.
echo Option 1: Local Network Only (same network)
echo   Open: http://localhost:8000
echo   From other computer on network: http://your-computer-name:8000
echo.
echo Option 2: PUBLIC Internet Access (use ngrok)
echo   1. Download ngrok from https://ngrok.com/download
echo   2. In another terminal, run: ngrok http 8000
echo   3. Share the public URL with anyone
echo.
echo See PUBLIC-DEPLOYMENT.md for more options!
echo.

cd /d "%~dp0"
python manage.py runserver 0.0.0.0:8000

pause
