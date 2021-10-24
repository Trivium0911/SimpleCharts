import os
from dj_database_url import parse
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SimpleCharts.settings')

application = get_asgi_application()
