from flask.ext.script import Manager

from pyvly import helpers
from pyvly.database import init_db as idb
from pyvly.main import app

manager = Manager(app)


@manager.option('-e', '--email', required=True, help="User's email address")
@manager.option('-p', '--password', required=True, help="User's password")
def create_user(email, password):
    helpers.create_user(email, password)

@manager.command
def init_db():
    idb()


if __name__ == '__main__':
    manager.run()
