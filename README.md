PyVly
=====

Privly Python Content Server

Installing Server
=================

## Prerequisites

- Python 2.X
- Pip
- Virtualenv

## Install

1. git clone --recursive https://github.com/privly/privly-flask.git
1. cd privly-flask
1. virtualenv env
1. source env/bin/activate
1. pip install -r requirements.txt
1. cp config.py.dist config.py
1. python managy.py init_db
1. python manage.py runserver

## Add a user

        python manage.py create_user -e user@example.com -p password

Running Tests
=============

From the projects root directory, run:

        nosetests



