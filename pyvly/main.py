import simplejson

from flask import Flask
from flask.ext.login import LoginManager
from flask_wtf.csrf import CsrfProtect

from pyvly.controllers import post, user
from pyvly.models import User

app = Flask(__name__)

app.config.from_object('config')

CsrfProtect(app)

login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return User.get(userid)


app.register_blueprint(post.bp, url_prefix='/posts')
app.register_blueprint(user.bp, url_prefix='/users')

class ExtensibleJSONEncoder(simplejson.JSONEncoder):
    """A JSON encoder that will check for a .__json__ method on objects."""
    def default(self, obj):
        if hasattr(obj, '__json__'):
            return obj.__json__()
        return super(ExtensibleJSONEncoder, self).default(obj)


app.json_encoder = ExtensibleJSONEncoder

