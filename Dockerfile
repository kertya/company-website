# Базовий образ Python
FROM python:3.9-slim

# Встановлення залежностей для Postgres
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Робоча директорія
WORKDIR /app

# Копіювання та встановлення залежностей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіювання всіх файлів проекту
COPY . .

# Збір статичних файлів
RUN python manage.py collectstatic --noinput

# Команда для запуску
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "company_site.wsgi"]