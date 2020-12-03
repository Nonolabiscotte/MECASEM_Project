"""
WSGI config for mecasem_report_manager_taskmanagement project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mecasem_report_manager_taskmanagement.settings')

application = get_wsgi_application()
