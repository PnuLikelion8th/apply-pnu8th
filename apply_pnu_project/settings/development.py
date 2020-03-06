from .base import *
import json


DEBUG = True

config_secret_develop = json.loads(open(CONFIG_SECRET_DEVELOP_FILE).read())

ALLOWED_HOSTS = ['*']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}