"""
<<<<<<<< HEAD:core/asgi.py
ASGI config for core project.
========
ASGI config for proxy project.
>>>>>>>> origin/develop:proxy/asgi.py

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<<< HEAD:core/asgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
========
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proxy.settings')
>>>>>>>> origin/develop:proxy/asgi.py

application = get_asgi_application()
