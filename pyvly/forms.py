from wtforms_alchemy import ModelForm

from pyvly.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
