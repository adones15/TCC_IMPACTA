"""
ASGI config for tcc_mercado project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see teste teste
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tcc_mercado.settings')

application = get_asgi_application()
