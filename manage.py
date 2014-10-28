#!/usr/bin/env python
from flask.ext.script import Manager, Server

from pyvly import helpers, database, main, models


# Initialize the manager
manager = Manager(main.app)

manager.add_command('runserver', Server(host='0.0.0.0', port=3000))

@manager.option('-e', '--email', required=True, help="User's email address")
@manager.option('-p', '--password', required=True, help="User's password")
def create_user(email, password):
    """Creates a user in the database"""
    helpers.create_user(email, password)

@manager.command
def init_db():
    """Intializes the Database"""
    database.init_db()

@manager.command
def seed_db():
    users = ['admin', 'demostration', 'development']
    for name in users:
        user = models.User(name + '@priv.ly', 'password')
        user.save()


# Run the manager when called directly
if __name__ == '__main__':
    manager.run()
