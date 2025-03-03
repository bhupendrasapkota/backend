import os

ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'development')

if ENVIRONMENT == 'production':
    from config.settings.production import *
else:
    from config.settings.development import *