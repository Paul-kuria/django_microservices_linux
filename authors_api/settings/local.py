# #noqa tells linter to ignore line
from .base import * #noqa
from .base import env 

# SECURITY WARNING: keep the secret key used in production secret!
# Generate cryptographic secure random strings with 
# python -c "import secrets; print(secrets.token_urlsafe(38))"
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", 
    default="OvFfa7nPknplnqaw-VLH0CS9ObiIjFW8lPSMJGGiy1Lo0YPZrek"
    )

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"] # Will add domain of our server here.