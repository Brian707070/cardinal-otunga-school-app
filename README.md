# Cardinal Otunga School App

A comprehensive Django-based school management system for Cardinal Otunga National School Mosocho with features for student enrollment, academic performance tracking, attendance management, announcements, and parent-student communication.

## ⚡ Quick Setup (Automated)

**No manual configuration needed!** Just run one script:

```batch
# Windows: Right-click and "Run as Administrator"
setup-and-run.bat

# Then open browser to:
http://chibibyte.local/
```

Or use PowerShell:
```powershell
# Right-click and "Run with PowerShell"
setup-and-run.ps1
```

**Before starting?** Verify setup status:
```batch
verify-setup.bat
```

See **QUICK-START.md** for troubleshooting and detailed instructions.

---

## Features

- 📚 **Student Management**: Enrollment, registration, and student profiles
- 📊 **Grades & Performance**: Grade tracking, report cards, and academic performance analysis
- 📋 **Attendance**: Attendance tracking and attendance summaries
- 📢 **Announcements**: School announcements, news feeds, and event calendar
- 💬 **Communication**: Parent-student-teacher messaging and feedback system
- 🏫 **School Directory**: School information and directory
- 🔐 **Admin Dashboard**: Comprehensive Django admin panel
- 📱 **Mobile-Friendly**: Accessible from mobile browsers

## Technology Stack

- **Backend**: Django 4.2.7 + Django REST Framework
- **Database**: SQLite (development) / PostgreSQL (production)
- **Python**: 3.9+
- **API**: RESTful API with JSON responses
- **Optional**: Pillow (if you want to upload/validate images)

## Project Structure

```
cardinal-otunga-school-app/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── db.sqlite3               # SQLite database (created after migration)
│
├── school/                  # Main Django project
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── asgi.py
│   ├── wsgi.py
│
├── apps/                    # Django applications
│   ├── students/            # Student management
│   │   ├── models.py
│   │   ├── admin.py
│   │   └── ...
│   ├── grades/              # Academic grades
│   │   ├── models.py
│   │   ├── admin.py
│   │   └── ...
│   ├── attendance/          # Attendance tracking
│   │   ├── models.py
│   │   ├── admin.py
│   │   └── ...
│   ├── announcements/       # News and events
│   │   ├── models.py
│   │   ├── admin.py
│   │   └── ...
│   └── communication/       # Messaging and feedback
│       ├── models.py
│       ├── admin.py
│       └── ...
│
├── api/                     # REST API
│   ├── __init__.py
│   ├── serializers.py       # DRF serializers
│   ├── views.py             # API views
│   └── urls.py              # API routes
│
└── .github/
    └── copilot-instructions.md
```

## Installation & Setup

This repository now contains two versions of the application: a Django-based school system (original) and a newer Flask-based demo with YouTube and Bing features.

### 1. Clone the Repository
```bash
git clone <repository-url>
cd cardinal-otunga-school-app
```

### 2. Choose your stack
- To use **Django**, follow the original steps below.
- To try the **Flask** demo, see the "Flask version" section further down.

### 2. Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
# if you plan to upload images, also install Pillow:
# pip install Pillow
```

> Tip: To use a custom hostname like `chibibyte.local`, add an entry to your
> system's hosts file (`C:\Windows\System32\drivers\etc\hosts` on Windows) or
> configure mDNS/Bonjour so that the name resolves to the IP of the machine running the app.
### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

> Note: API endpoints do not require authentication or registration. Everyone can access data freely; only the Django admin panel still requires login to manage records.

### 6. Setup Hostname (Windows Hosts File)

To access the app as `chibibyte.local` instead of `localhost`, you need to add an entry to your Windows hosts file:

1. **Open Notepad as Administrator**
   - Right-click Notepad → Run as Administrator

2. **Open the hosts file:**
   - File → Open → Navigate to `C:\Windows\System32\drivers\etc\`
   - Select "All Files" filter if needed
   - Open `hosts`

3. **Add this line at the end of the file:**
   ```
   127.0.0.1 chibibyte.local
   ```

4. **Save and close**

### 7. Run Development Server
```bash
# Bind to all interfaces so others can connect
python manage.py runserver 0.0.0.0:8000
```

**Access Options:**
- **Via Hostname**: http://chibibyte.local:8000/ (after hosts file setup)
- **Via Localhost**: http://localhost:8000/
- **Admin Panel**: http://chibibyte.local:8000/admin/
- **API**: http://chibibyte.local:8000/api/

**For Network Access (Other Devices):**
- If accessing from another device via IP (e.g., `http://192.168.1.5:8000/`), the app will automatically redirect to `http://chibibyte.local:8000/`
- Ensure those devices have `chibibyte.local` configured in their hosts file or use mDNS

The application will be available at:
- **Main Site**: http://chibibyte.local:8000/
- **Admin Panel**: http://chibibyte.local:8000/admin/
- **API**: http://chibibyte.local:8000/api/

## API Endpoints (Django Only)


### Students
- `GET/POST /api/students/` - List/Create students
- `GET /api/students/{id}/` - Get student details
- `GET /api/students/by_admission/{admission_number}/` - Get student by admission number

### School Information
- `GET /api/school-info/` - Get school information

### Subjects
- `GET /api/subjects/` - List all subjects

### Grades
- `GET /api/grades/` - List all grades (filter by student, subject, term, year)
- `GET /api/grades/by_student/?student_id={id}` - Get grades for specific student
- `GET /api/report-cards/` - Get report cards

### Attendance
- `GET/POST /api/attendance/` - List/Create attendance records
- `GET /api/attendance-summary/` - Get attendance summaries

### Announcements
- `GET /api/announcements/` - List announcements
- `GET /api/events/` - List events

### Communication
- `GET/POST /api/messages/` - List/Create messages (no login required)
- `GET /api/messages/inbox/` - Get received messages (public)
- `GET /api/messages/sent/` - Get sent messages (public)
- `GET/POST /api/conversations/` - List/Create conversations (public)
- `GET/POST /api/feedback/` - List/Create feedback (public)

## Usage Examples

### Get All Students
```bash
curl http://localhost:8000/api/students/
```

### Get Student by Admission Number
```bash
curl http://localhost:8000/api/students/by_admission/ADM001/
```

### Get Announcements
```bash
curl http://localhost:8000/api/announcements/
```

### Get Grades for Specific Student
```bash
curl "http://localhost:8000/api/grades/by_student/?student_id=1"
```

### Create a New Announcement
```bash
curl -X POST http://localhost:8000/api/announcements/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "School Notice",
    "content": "Important announcement...",
    "priority": "high",
    "category": "Academic"
  }'
```

## Django Admin Interface

Access the admin panel at `http://localhost:8000/admin/` with your superuser credentials.

In the admin panel, you can:
- Manage students and their information
- Record grades and create report cards
- Manage attendance records
- Post announcements and events
- Monitor messages and feedback

## Database Models

### Students App
- **Student**: Student information including personal, contact, and academic details
- **SchoolInfo**: School information and contact details

---

## Flask Version

The Flask implementation is a lightweight demo with minimal persistence (in-memory lists). It includes two extra features:

- **YouTube embed** on the home page (you can replace the `youtube_video_id` in `flask_app/app.py` with any video).
- **Bing search form**: a simple search box that displays mock results. You can hook it up to the Bing Search API by inserting your key in `app.py` and sending requests to `https://api.bing.microsoft.com/v7.0/search`.

### Running the Flask App

```bash
# install Flask dependencies
pip install Flask requests

# start the Flask server (it will redirect IP-based requests to chibibyte.local)
cd flask_app
python app.py
```

The app will be available at `http://localhost:5000/` by default. It has two routes:

- `/` – home page with YouTube video and search box
- `/students` – simple student list form

You can still run the original Django server as described earlier; the two apps are independent.

### Grades App
- **Subject**: School subjects
- **Grade**: Individual student grades
- **ReportCard**: Term-based report cards

### Attendance App
- **Attendance**: Daily attendance records
- **AttendanceSummary**: Attendance statistics per student per year

### Announcements App
- **Announcement**: School announcements and news
- **EventCalendar**: School events and calendar

### Communication App
- **Message**: Private messages between users
- **Conversation**: Group conversations/threads
- **ConversationMessage**: Messages within conversations
- **Feedback**: Parent feedback and complaints

## Configuration

### Django Settings (`school/settings.py`)
- **DEBUG**: Currently set to `True` for development
- **ALLOWED_HOSTS**: Set to `['*']` for development (restrict in production)
- **DATABASES**: SQLite for development (change to PostgreSQL in production)
- **INSTALLED_APPS**: All app modules are registered
- **CORS**: CORS is configured for localhost access

### For Production:
1. Change `SECRET_KEY` to a secure random string
2. Set `DEBUG = False`
3. Update `ALLOWED_HOSTS` with your domain
4. Configure PostgreSQL database
5. Set proper CORS origins
6. Use environment variables for sensitive data

## Development Server Commands

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver

# Create new app
python manage.py startapp app_name

# Collect static files (for production)
python manage.py collectstatic

# Create database backup
python manage.py dumpdata > backup.json

# Load database from backup
python manage.py loaddata backup.json
```

## Troubleshooting

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Database Errors
```bash
# Delete and recreate database
rm db.sqlite3
python manage.py migrate
```

### Missing Dependencies
```bash
pip install -r requirements.txt
```

## Security Considerations

- Always use a strong SECRET_KEY in production
- Set DEBUG = False in production
- Use HTTPS in production
- Configure proper CORS settings for your domain
- Use PostgreSQL instead of SQLite in production
- Implement proper authentication (JWT tokens recommended)
- Add rate limiting for API endpoints

## Future Enhancements

- Real-time notifications
- Mobile app (React Native/Flutter)
- Advanced analytics and reporting
- Parent payment portal
- Online assignment submission
- Video learning platform integration
- SMS and email notifications
- Advanced search and filtering

## Support & Contact

For issues or questions about this application, please contact Cardinal Otunga National School Mosocho.

## License

This project is developed for Cardinal Otunga National School Mosocho.

## Changelog

### Version 1.0.0 (Initial Release)
- Student management system
- Grade and performance tracking
- Attendance management
- Announcements and event calendar
- Communication and feedback system
- RESTful API
- Admin dashboard
