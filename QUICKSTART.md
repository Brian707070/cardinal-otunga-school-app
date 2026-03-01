# Quick Start Guide

## For Windows Users

### Option 1: Using the Setup Script (Recommended)
1. Double-click `setup.bat`
2. Follow the prompts to create a superuser account
3. Once setup completes, run: `python manage.py runserver`
4. Visit http://localhost:8000/admin/

### Option 2: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

## For macOS/Linux Users

### Option 1: Using the Setup Script (Recommended)
```bash
chmod +x setup.sh
./setup.sh
```

### Option 2: Manual Setup
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

## Accessing the Application

Once the server is running:

- **Admin Panel**: http://localhost:8000/admin/
  - Login with the superuser credentials you created
  
- **API Root**: http://localhost:8000/api/
  - Browse all available API endpoints
  
- **API Endpoints**:
  - Students: http://localhost:8000/api/students/
  - Grades: http://localhost:8000/api/grades/
  - Announcements: http://localhost:8000/api/announcements/
  - Attendance: http://localhost:8000/api/attendance/
  - And many more...

## Common Commands

```bash
# Start development server
python manage.py runserver

# Create a new superuser
python manage.py createsuperuser

# Run migrations
python manage.py migrate

# Make migrations (if you modify models)
python manage.py makemigrations

# Access Django shell
python manage.py shell

# Backup database
python manage.py dumpdata > backup.json

# Restore database
python manage.py loaddata backup.json

# View all available commands
python manage.py help
```

## Troubleshooting

### Port 8000 Already in Use
```bash
python manage.py runserver 8001
```

### Database Errors
```bash
# Reset database (caution: deletes all data)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Module Not Found Error
```bash
# Make sure all dependencies are installed
pip install -r requirements.txt
```

## Default Admin Features

Once logged into the admin panel, you can:

- ✅ Register new students
- ✅ Add subjects and grades
- ✅ Record attendance
- ✅ Post announcements
- ✅ Manage school information
- ✅ View messages and feedback
- ✅ Generate reports

## Next Steps

1. Log in to the admin panel
2. Add your school information under "School Info"
3. Create subjects under "Subjects"
4. Start adding students
5. Record grades and attendance
6. Post announcements and events

For detailed documentation, see README.md
