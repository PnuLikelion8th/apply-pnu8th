from .base import *
import json

# config_secret_production = json.loads(open(CONFIG_SECRET_PRODUCTION_FILE).read())

DEBUG = False 

ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'apply_pnu_project.wsgi'

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
