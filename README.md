# CoreHub

CoreHub is a backend project built with Django for handling authentication and OTP-based login flows. It is designed with a clean and scalable architecture and can be extended for production use.

## Features

- OTP-based authentication
- Redis for caching and temporary token storage
- Celery for background tasks such as SMS sending
- Modular and maintainable Django app structure
- Ready for extension into a production-grade backend

## Tech Stack

- Python 3.10+
- Django
- Django REST Framework
- Redis
- Celery
- PostgreSQL (or another relational database)

## Project Structure

- `apps/` - application modules
- `core/` - project settings and configuration
- `services/` - reusable service layer logic
- `manage.py` - Django management entry point

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.10 or newer
- Redis
- PostgreSQL
- Git

## Environment Variables

This project uses environment variables for configuration.

Create a `.env` file based on `.env.example` and fill in the required values.

Example:
```env
SECRET_KEY=your_secret_key_here
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/dbname
REDIS_URL=redis://localhost:6379/0
SMS_API_KEY=your_sms_api_key_here
