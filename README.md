```markdown
# CoreHub

CoreHub is a robust backend system built with **Django**, specialized in secure **OTP-based authentication** and modular architecture.

## Features

- Secure OTP Auth
- Redis Caching
- Celery Background Tasks
- Modular Architecture
- RESTful API (DRF)

## 1. Environment Variables

Before running the project, you must configure your environment variables. Create a `.env` file in the root directory and use the following template:

```env
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=postgres://user:password@localhost:5432/dbname

# Redis & Celery
REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/1

# SMS Services
SMS_API_KEY=your_sms_api_key_here

## 2. Installation & Setup

### Clone & Enter
```bash
git clone https://github.com/HOsouli/CoreHub.git
cd CoreHub

````markdown
## 2. Installation & Setup

### Clone & Enter

```bash
git clone https://github.com/HOsouli/CoreHub.git
cd CoreHub
```

### Environment Setup

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install & Initialize

```bash
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

---

## 3. Running Background Workers

To handle asynchronous tasks like sending SMS, start the Celery worker:

```bash
# Start Worker
celery -A core worker -l info

# Start Beat (for scheduled tasks)
celery -A core beat -l info
```

---

## 4. Important Notes

- **Redis** must be running for OTP and Celery to function correctly.

- **Security:** The `.env` file is excluded from Git. Always update `.env.example` when adding new variables.

- **Dependencies:** Keep your `requirements.txt` updated:

```bash
pip freeze > requirements.txt
```

---

## 5. License

This project is currently for development and educational purposes.
````
