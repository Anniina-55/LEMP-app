# syntax=docker/dockerfile:1
FROM python:3.11-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ /app/
EXPOSE 8000
# Gunicorn: bind to all interfaces, 3 workers
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "app:app"]
