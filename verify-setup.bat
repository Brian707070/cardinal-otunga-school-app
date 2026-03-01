@echo off
REM Verify Cardinal Otunga School App Setup
REM No admin required - just checks if everything is configured

cls
echo.
echo ========================================
echo Cardinal Otunga School App - Setup Check
echo ========================================
echo.

REM Check if hosts file has the entry
echo Checking hosts file...
findstr /c:"127.0.0.1 chibibyte.local" %windir%\System32\drivers\etc\hosts >nul
if %errorLevel% equ 0 (
    echo [SUCCESS] ✓ chibibyte.local found in hosts file
) else (
    echo [WARNING] ✗ chibibyte.local NOT in hosts file
    echo           Run setup-and-run.bat to configure
)

echo.

REM Check if Python is installed
echo Checking Python installation...
python --version >nul 2>&1
if %errorLevel% equ 0 (
    echo [SUCCESS] ✓ Python is installed
    python --version
) else (
    echo [ERROR] ✗ Python not found - please install Python
)

echo.

REM Check if Django is installed
echo Checking Django installation...
python -c "import django; print(f'[SUCCESS] ✓ Django {django.get_version()} installed')" 2>nul
if %errorLevel% neq 0 (
    echo [ERROR] ✗ Django not found
    echo        Run: pip install -r requirements.txt
)

echo.

REM Check if database exists
echo Checking database...
if exist "db.sqlite3" (
    echo [SUCCESS] ✓ Database exists
) else (
    echo [WARNING] ✗ Database not found
    echo           Run: python manage.py migrate
)

echo.
echo ========================================
echo Setup Status Summary
echo ========================================
echo.
echo If all checks passed, run:
echo   setup-and-run.bat
echo.
echo and access:
echo   http://chibibyte.local/
echo.
pause
