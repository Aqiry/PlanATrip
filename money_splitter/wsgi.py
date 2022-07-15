"""
WSGI config for money_splitter project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'money_splitter.settings')

application = get_wsgi_application()


# beautifulsoup4==4.9.0
# certifi==2020.6.20
# cffi==1.14.0
# chardet==3.0.4
# defusedxml==0.6.0
# Django==3.0.5
# django-allauth==0.42.0
# django-bootstrap3==12.1.0
# django-bootstrap4==1.1.1
# django-braces==1.14.0
# django-polymorphic==2.1.2
# django-responsive==0.3.0
# idna==2.10
# oauthlib==3.1.0
# Pillow==7.1.1
# psycopg2==2.8.5
# pycparser==2.20
# python-dateutil==2.8.1
# python3-openid==3.2.0
# pytz==2019.3
# requests==2.24.0
# requests-oauthlib==1.3.0
# six==1.14.0
# soupsieve==2.0
# sqlparse==0.3.1
# text-unidecode==1.3
# urllib3==1.25.9