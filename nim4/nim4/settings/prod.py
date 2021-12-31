from .base import *
import configparser
from pathlib import Path

config = configparser.ConfigParser()
cdir = Path(__file__).parents[0]
secret_file: Path = cdir / '.secret'
config.read(secret_file)


SECRET_KEY = config.get('Secret','secret')
DEBUG = False
ALLOWED_HOSTS = ['nim4.me','www.nim4.me',"*"]

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
