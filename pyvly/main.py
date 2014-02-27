import simplejson
from flask import Flask


from pyvly.api import post


app = Flask(__name__)


app.register_blueprint(post.bp, url_prefix='/posts')

class ExtensibleJSONEncoder(simplejson.JSONEncoder):
    """A JSON encoder that will check for a .__json__ method on objects."""
    def default(self, obj):
        if hasattr(obj, '__json__'):
            return obj.__json__()
        return super(ExtensibleJSONEncoder, self).default(obj)


app.json_encoder = ExtensibleJSONEncoder

