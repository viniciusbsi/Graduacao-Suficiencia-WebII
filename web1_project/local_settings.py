# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

DEBUG = False
# DEBUG = True

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['viniciusbsi.pythonanywhere.com']

# Make these unique, and don't share it with anybody.
SECRET_KEY = "o(*1ltt&=t_+%yvyk!#mk1f)rfx7z!z(9(@!4rtv7+#wvhadd@"
NEVERCACHE_KEY = "$f3_%g^4!^65#0-66ei(y0^igbfu3i%5nti2a_!c4p_&we%7g="

# DATABASES = {
#     "default": {
#         # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         # DB name or path to database file if using sqlite3.
#         "NAME": "nr2",
#         # Not used with sqlite3.
#         "USER": "nr2",
#         # Not used with sqlite3.
#         "PASSWORD": "nr2",
#         # Set to empty string for localhost. Not used with sqlite3.
#         "HOST": "localhost",
#         # Set to empty string for default. Not used with sqlite3.
#         "PORT": "5432",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
