# takehome/tests/base.py


from flask_testing import TestCase

from takehome.server import app


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('takehome.server.config.DevelopmentConfig')
        return app
