DATABASES = {
    'pubsub': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pubsub',
        'USER': 'ezoji',
        'PASSWORD': '1qaz!QAZ',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    },

}

def get_db():

    return DATABASES