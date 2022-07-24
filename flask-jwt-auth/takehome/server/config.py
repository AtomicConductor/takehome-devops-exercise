# takehome/server/config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class DevelopmentConfig():
    """Development configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'APP_JWT_SECRET')
    DEBUG = True
