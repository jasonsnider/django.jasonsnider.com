"""
WSGI config for jscom project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application
sys.path.append('/var/www/jasonsnider.com/django')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jscom.settings")

application = get_wsgi_application()
