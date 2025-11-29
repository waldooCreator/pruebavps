#!/usr/bin/env bash
set -e

# Run migrations, collectstatic and start gunicorn
python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn webcalc.wsgi:application --bind 0.0.0.0:2000 --workers 3
