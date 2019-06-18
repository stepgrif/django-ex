import os

from django.conf import settings


engines = {
    'SQLITE': 'django.db.backends.sqlite3',
    'POSTGRESQL': 'django.db.backends.postgresql_psycopg2'
}


def config():
    # is engine is set, default sqlite
    engine = engines.get(os.getenv('DB_ENGINE').upper(), engines['SQLITE'])
    # schema name
    name = os.getenv('DB_NAME')
    # is schema name set
    if name is None:
        # sqlite is default
        name = os.path.join(settings.BASE_DIR, 'db.sqlite3')
    # map of values
    return {
        'ENGINE': engine,
        'NAME': name,
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
