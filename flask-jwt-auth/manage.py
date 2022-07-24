# manage.py


import os
import unittest
import coverage

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from takehome.server import application

application = Manager(application)

@application.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('takehome/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    application.run()
