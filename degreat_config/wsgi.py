"""
WSGI config for DE-GREAT WELD ENTERPRISES
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'degreat_config.settings')

application = get_wsgi_application()
