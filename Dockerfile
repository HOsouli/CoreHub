FROM python:3.12-slim

# تنظیم متغیرهای محیطی برای جلوگیری از بافر شدن و فایل‌های کش
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# نصب پیش‌نیازهای ضروری برای کار با دیتابیس در محیط لینوکسی داکر
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# ارتقای pip و نصب پکیج‌ها
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# کپی کردن کدهای پروژه
COPY . .
