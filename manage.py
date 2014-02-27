from flask.ext.script import Manager

from pyvly.helpers import create_user as cu
from pyvly.main import app

manager = Manager(app)

@manager.command
@manager.option('-e', '--email', required=True, help="User's email address")
@manager.option('-p', '--password', required=True, help="User's password")
def cerate_user(email, password):
    cu(email, password)


if __name__ == '__main__':
    manager.run()
