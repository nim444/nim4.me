from .base import *
import configparser
from pathlib import Path

config = configparser.ConfigParser()
cdir = Path(__file__).parents[0]
secret_file: Path = cdir / '.secret'
if secret_file.exists():
    config.read(secret_file)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config.get('Secret', 'dbname'),
            'USER': config.get('Secret', 'dbuser'),
            'PASSWORD': config.get('Secret', 'dbpass'),
            'HOST': str(config.get('Secret', 'dbip')),
            'PORT': '5432',

        }
    }
    SECRET_KEY = config.get('Secret', 'secret')
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    SECRET_KEY = "Pre_Production_KEY"


DEBUG = False
ALLOWED_HOSTS = ['nim4.me','www.nim4.me',"*"]


