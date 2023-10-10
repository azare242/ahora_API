from decouple import config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
def get_db(db):
    if db == "SQLITE":
        return {
            'default': {
            'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db.sqlite3',
            }
    }
    elif db == "POSTGRES":
        return {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': config("POSTGRES_NAME"), 
                'USER': config("POSTGRES_USER"),
                'PASSWORD': config("POSTGRES_PASSWORD"), 
                'HOST': config("POSTGRES_HOST"),
                'PORT': config("POSTGRES_PORT", cast=int),
            }
        }
    elif db == "MYSQL":
        return {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': config('MYSQL_NAME'),
                'USER': config('MYSQL_USER'),
                'PASSWORD': config('MYSQL_PASSWORD'),
                'HOST': config('MYSQL_HOST'),
                'PORT': config('MYSQL_PORT', cast=int),
            }
        }

