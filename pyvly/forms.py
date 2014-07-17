from flask_wtf.csrf import CsrfProtect
from wtforms import Form, TextField, PasswordField, validators

from pyvly.models import User


csrf = CsrfProtect()

class RegistrationForm(Form):
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')