#!/usr/bin/env python
from distutils.core import setup

setup(name='django-actions',
    version='0.2',
    description='Provides mass actions for selected items like django admin actions',
    author='Nickolas Fox',
    author_email='lilfoxster@gmail.com',
    packages=[
        'django_actions',
        'django_actions.templatetags',
    ],
    package_data={
        'django_actions': [
            'templates/*.html',
            'templates/actions/*.html',
        ],
    }
)
