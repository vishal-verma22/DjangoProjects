"""
ASGI config for Document_Checker_Check_file_nme_type_size_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Document_Checker_Check_file_nme_type_size_project.settings')

application = get_asgi_application()
