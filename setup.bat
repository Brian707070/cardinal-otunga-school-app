@echo off
REM Cardinal Otunga School App Setup Script
REM This script sets up the Django application for Windows

echo.
echo ========================================
echo Cardinal Otunga School App Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo [2/4] Running database migrations...
python manage.py migrate
if errorlevel 1 (
    echo ERROR: Migration failed
    pause
    exit /b 1
)

echo [3/4] Creating superuser...
echo Please enter superuser details below:
python manage.py createsuperuser
if errorlevel 1 (
    echo WARNING: Superuser creation skipped
)

echo [4/4] Setup complete!
echo.
echo To start the development server, run:
echo   python manage.py runserver
echo.
echo Then visit:
echo   http://localhost:8000/admin/ (Admin panel)
echo   http://localhost:8000/api/ (API)
echo.
pause
