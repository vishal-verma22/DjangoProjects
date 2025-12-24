"""
WSGI config for Document_Checker_Check_file_nme_type_size_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Document_Checker_Check_file_nme_type_size_project.settings')

application = get_wsgi_application()
