from flask_wtf.csrf import CsrfProtect
from wtforms_alchemy import ModelForm

from pyvly.models import User


csrf = CsrfProtect()

class UserForm(ModelForm):
    class Meta:
        model = User
