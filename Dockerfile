FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# install python deps
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /app/

# collect static files
ENV DJANGO_SETTINGS_MODULE=webcalc.settings
RUN python manage.py collectstatic --noinput || true

# make entrypoint executable
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
