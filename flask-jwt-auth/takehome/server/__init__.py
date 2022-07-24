# takehome/server/__init__.py

import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

app_settings = os.getenv(
    'APP_SETTINGS',
    'takehome.server.config.DevelopmentConfig'
)
application.config.from_object(app_settings)

from takehome.server.auth.views import auth_blueprint
application.register_blueprint(auth_blueprint)
