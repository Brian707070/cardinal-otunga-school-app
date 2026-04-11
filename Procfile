release: python manage.py migrate --noinput
web: gunicorn --workers 3 --worker-class sync --timeout 60 --bind 0.0.0.0:10000 school.wsgi