#!/bin/sh

python manage.py collectstatic --no-input
python manage.py makemigrations 
python manage.py migrate
gunicorn zabuiki.wsgi:application --workers 1 --bind 0.0.0.0:8000