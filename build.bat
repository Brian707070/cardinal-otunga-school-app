@echo off
REM Build script for deploying to Render.com
REM Run this locally before pushing to ensure everything works

echo.
echo ================================
echo Building for Render.com
echo ================================
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Run migrations
echo Running migrations...
python manage.py migrate

REM Collect static files
echo Collecting static files...
python manage.py collectstatic --noinput

REM Show completion message
echo.
echo Setup complete!
echo.
echo Next steps:
echo 1. git add .
echo 2. git commit -m "Ready for Render deployment"
echo 3. git push origin main
echo.
echo Then go to https://render.com and create a new web service
echo.

pause
