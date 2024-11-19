"""
ASGI config for hms project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application
from fastapi_app.main import app as fastapi_app
from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hms.settings')

# Get Django ASGI app
django_asgi_app = get_asgi_application()

# Add middleware for FastAPI
application = fastapi_app

# Mount Django ASGI app at a specific path (optional)
application.mount("/django", django_asgi_app)
