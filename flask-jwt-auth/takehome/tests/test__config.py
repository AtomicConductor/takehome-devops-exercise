# takehome/tests/test_config.py


import unittest

from flask import current_app
from flask_testing import TestCase

from takehome.server import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('takehome.server.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['SECRET_KEY'] is 'APP_JWT_SECRET')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)

if __name__ == '__main__':
    unittest.main()
