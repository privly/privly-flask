from flask.ext.script import Manager

from pyvly import helpers, database, main

manager = Manager(main.app)


@manager.option('-e', '--email', required=True, help="User's email address")
@manager.option('-p', '--password', required=True, help="User's password")
def create_user(email, password):
    helpers.create_user(email, password)

@manager.command
def init_db():
    database.init_db()


if __name__ == '__main__':
    manager.run()
