from flask import Flask

app = Flask(__name__)

class ExtensibleJSONEncoder(simplejson.JSONEncoder):
    """A JSON encoder that will check for a .__json__ method on objects."""
    def default(self, obj):
       if hasattr(obj, '__json__'):
          return obj.__json__()
    return super(ExtensibleJSONEncoder, self).default(obj)

app.json_encoder = ExtensibleJSONEncoder

