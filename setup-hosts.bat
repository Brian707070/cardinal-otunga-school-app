@echo off
REM This script adds chibibyte.local to your Windows hosts file
REM Right-click this file and select "Run as administrator"

echo Adding chibibyte.local to hosts file...

REM Check if already exists
findstr /c:"127.0.0.1 chibibyte.local" C:\Windows\System32\drivers\etc\hosts >nul
if %errorlevel%==0 (
    echo chibibyte.local is already in your hosts file.
    pause
    exit /b 0
)

REM Add the entry
echo 127.0.0.1 chibibyte.local >> C:\Windows\System32\drivers\etc\hosts

echo.
echo Success! Added chibibyte.local to your hosts file.
echo You can now access the app at: http://chibibyte.local:8000/
echo.
pause
