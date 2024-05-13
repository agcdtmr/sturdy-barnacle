#!/bin/sh

# Run django project, migrate the database
python manage.py migrate --no-input

# Collect static files needed for volume
# check by /admin page
python manage.py collectstatic --no-input

# Then instead of python manage.py runserver
gunicorn django-docker-gunicorn-nginx.wsgi:application --bind 0.0.0.0:8000
