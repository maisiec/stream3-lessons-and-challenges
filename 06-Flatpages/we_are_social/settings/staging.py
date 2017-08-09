from base import *
import dj_database_url



DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Update database configuration with $DATABASE_URL.


# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}


# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_HCC9iZGSlGKmuv8TeNWFIpaw')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_CrLLB7ikEuQLOlVD3zoRcxs7')

# Paypal Settings
SITE_URL = 'https://code-institute-social-staging1.herokuapp.com'
PAYPAL_NOTIFY_URL = 'http://a47f1d9c.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL ='maaisiexx-facilitator@hotmail.co.uk'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'