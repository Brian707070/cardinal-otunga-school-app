#!/bin/bash

# Cardinal Otunga School App Setup Script
# This script sets up the Django application for macOS/Linux

echo ""
echo "========================================"
echo "Cardinal Otunga School App Setup"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.9+ first"
    exit 1
fi

echo "Python version: $(python3 --version)"
echo ""

# Create virtual environment
echo "[1/5] Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "[2/5] Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

# Run migrations
echo "[3/5] Running database migrations..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "ERROR: Migration failed"
    exit 1
fi

# Create superuser
echo "[4/5] Creating superuser..."
echo "Please enter superuser details below:"
python manage.py createsuperuser

# Create necessary directories
echo "[5/5] Creating necessary directories..."
mkdir -p media
mkdir -p staticfiles

echo ""
echo "Setup complete!"
echo ""
echo "To start the development server, run:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "Then visit:"
echo "  http://localhost:8000/admin/ (Admin panel)"
echo "  http://localhost:8000/api/ (API)"
echo ""
