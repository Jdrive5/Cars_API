# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mk6+a7xz3m=uxoazb18!=ecivox7%o4c9!!jh9xy0+__qn+qws'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Elkton2009!' 
    }
}