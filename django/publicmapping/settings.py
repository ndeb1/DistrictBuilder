from ConfigParser import RawConfigParser

config = RawConfigParser()
config.read('/projects/publicmapping/local/settings.ini')

# Django settings for publicmapping project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    (config.get('publicmapping','ADMIN_USER'), 
     config.get('publicmapping','ADMIN_EMAIL')),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql_psycopg2'   # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = config.get('database','DATABASE_NAME')  # Or path to database file if using sqlite3.
DATABASE_USER = config.get('database', 'DATABASE_USER')  # Not used with sqlite3.
DATABASE_PASSWORD = config.get('database', 'DATABASE_PASSWORD')   # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/projects/publicmapping/trunk/django/publicmapping/site-media/'
SLD_ROOT = '/projects/publicmapping/trunk/sld/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/site-media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = config.get('publicmapping','SECRET_KEY')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

# configure cache, according to guidelines for configuring django's
# cache framework: http://docs.djangoproject.com/en/1.0/topics/cache
CACHE_BACKEND = 'locmem:///?timeout=3600&max_entries=400'
CACHE_MIDDLEWARE_SECONDS = 3600
CACHE_MIDDLEWARE_KEY_PREFIX = ''

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'publicmapping.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/projects/publicmapping/trunk/django/publicmapping/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.gis',
    'redistricting',
)

LOGIN_URL = '/'
MAP_SERVER = config.get('publicmapping', 'MAP_SERVER')
BASE_GEOLEVEL = 3
TEST_RUNNER = 'django.contrib.gis.tests.run_tests'
POSTGIS_TEMPLATE='template_postgis'
MAX_DISTRICTS = 18
PLAN_TEMPLATE = 'default'
DEFAULT_DISTRICT_DISPLAY = 'POPTOT' # can be subject id, name, or display
TEMP_DIR = config.get('publicmapping', 'TEMP_DIR')
