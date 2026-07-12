FROM python:3.12-slim

# Prevent Python from writing pyc files to disc and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies commonly needed by Django projects (adjust as needed)
RUN apt-get update \
	&& apt-get install -y --no-install-recommends build-essential libpq-dev \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
	&& pip install --no-cache-dir -r requirements.txt

COPY . .

# Collect static files (if project configured). Ignore failure if manage.py unavailable at build time.
RUN python manage.py collectstatic --noinput || true

# Default Django port
EXPOSE 8000

# Default command: start Django development server. For production, replace with gunicorn.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
