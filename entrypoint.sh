#!/bin/sh
# Run database migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser --noinput

# Start the ASGI server
uvicorn  config.asgi:application --host 0.0.0.0 --port 8000
