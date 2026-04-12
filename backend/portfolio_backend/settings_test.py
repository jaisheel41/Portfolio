"""
Test settings: SQLite in-memory database so CI/tests do not require Postgres/Supabase.
Import main settings after seeding minimal env vars for decouple.
"""

import os
from pathlib import Path

os.environ.setdefault("SECRET_KEY", "test-secret-key-not-for-production")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DB_NAME", "postgres")
os.environ.setdefault("DB_USER", "postgres")
os.environ.setdefault("DB_PASSWORD", "test")
os.environ.setdefault("DB_HOST", "localhost")
os.environ.setdefault("DB_PORT", "5432")
os.environ.setdefault("USE_SUPABASE_STORAGE", "False")

from portfolio_backend.settings import *  # noqa: E402, F403, F401
from portfolio_backend.settings import BASE_DIR  # noqa: E402

ALLOWED_HOSTS = ["testserver", "localhost", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

STATIC_ROOT = str(BASE_DIR / "test_staticfiles")
MEDIA_ROOT = str(BASE_DIR / "test_media")

Path(STATIC_ROOT).mkdir(parents=True, exist_ok=True)
Path(MEDIA_ROOT).mkdir(parents=True, exist_ok=True)
