# Cardinal Otunga School App - Render.com Deployment Guide

## What is Render.com?
Render.com is a modern cloud platform similar to Heroku. It's free, simple, and automatically deploys from GitHub.

## Step-by-Step Deployment

### 1. Push Your Code to GitHub
If you haven't already:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/cardinal-otunga-school-app
git push -u origin main
```

### 2. Create a Render.com Account
- Go to https://render.com
- Sign up with GitHub (easiest option)
- Authorize Render to access your GitHub repositories

### 3. Create New Web Service
1. Click **New +** → **Web Service**
2. Select your `cardinal-otunga-school-app` repository
3. Configure:
   - **Name**: `cardinal-otunga-app` (or any name)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn school.wsgi`
   - **Plan**: Free (or upgrade for better performance)

### 4. Create PostgreSQL Database
1. Click **New +** → **PostgreSQL**
2. Configure:
   - **Name**: `cardinal-otunga-db`
   - **Plan**: Free
   - Copy the `DATABASE_URL` (you'll need it)

### 5. Set Environment Variables
In your web service, go to **Environment** tab and add:

```
DEBUG=False
SECRET_KEY=your-long-random-secret-key-here
USE_POSTGRES=True
DATABASE_URL=postgresql://user:password@host:5432/dbname
```

Get `DATABASE_URL` from your PostgreSQL service details.

### 6. Deploy
- Click **Create Web Service**
- Render will automatically:
  - Install dependencies from requirements.txt
  - Run migrations (via Procfile)
  - Collect static files
  - Deploy your app

Your app URL will be something like: `https://cardinal-otunga-app.onrender.com`

---

## After Deployment

### Create Admin Account
```bash
# Via Render dashboard, go to Shell tab and run:
python manage.py createsuperuser
```

Then access admin at: `https://your-app-name.onrender.com/admin`

### View Logs
Go to **Logs** tab in Render dashboard to see what's happening.

### Custom Domain
In **Settings** tab:
1. Click **Add Custom Domain**
2. Add your domain (e.g., `school.example.com`)
3. Update DNS records as shown

---

## Troubleshooting

### "ModuleNotFoundError" after deployment
- Check that ALL dependencies are in `requirements.txt`
- Run: `pip freeze > requirements.txt`
- Push and redeploy

### Static files not loading (CSS/images)
- Run manually: `python manage.py collectstatic`
- Check `STATIC_ROOT` setting in `settings.py`

### Database errors
- Verify `DATABASE_URL` is correct
- Check database is running in Render dashboard
- Run migrations: Dashboard Shell → `python manage.py migrate`

### App keeps crashing
- Check Logs tab for errors
- Run locally first: `python manage.py runserver`
- Test with `DEBUG=False` locally first

---

## Key Files for Render
- ✅ `Procfile` - Tells Render how to run your app
- ✅ `requirements.txt` - Python dependencies
- ✅ `render.yaml` - (Optional) Complete infrastructure as code
- ✅ `school/settings.py` - Django configuration with env variables

---

## Free vs Paid Plans
| Feature | Free | Paid |
|---------|------|------|
| Web Service | ✅ | ✅ |
| Database | ✅ | ✅ |
| Auto Sleep | Yes (after 15 min inactivity) | No |
| Performance | Good | Better |
| Cost | $0 | Starting $7/month |

**Note**: Free services sleep after 15 minutes of inactivity. Paid plans run 24/7.

---

## One-Click Deploy Button (Optional)
Add this to your README.md for users to deploy in one click:

```markdown
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/YOUR-USERNAME/cardinal-otunga-school-app)
```

---

## Questions?
- Render Docs: https://render.com/docs
- Django Deployment: https://docs.djangoproject.com/en/4.2/howto/deployment/
- Email: support@render.com
