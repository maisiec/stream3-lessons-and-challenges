from base import *



DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_HCC9iZGSlGKmuv8TeNWFIpaw')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_CrLLB7ikEuQLOlVD3zoRcxs7')

# Paypal Settings
SITE_URL = 'https://code-institute-social-staging1.herokuapp.com/'
PAYPAL_NOTIFY_URL = 'https://code-institute-social-staging1.herokuapp.com/'
PAYPAL_RECEIVER_EMAIL ='maaisiexx-facilitator@hotmail.co.uk'