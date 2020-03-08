from .base import *
import json

# config_secret_production = json.loads(open(CONFIG_SECRET_PRODUCTION_FILE).read())

DEBUG = False 

ALLOWED_HOSTS = ['pnu.likelion.org','.amazonaws.com','localhost']

WSGI_APPLICATION = 'apply_pnu_project.wsgi'

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())


DB_PW = config_secret_deploy['django']['db']['password']
DB_NAME = config_secret_deploy['django']['db']['name']
DB_USER = config_secret_deploy['django']['db']['user']
DB_HOST = config_secret_deploy['django']['db']['host']






# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
