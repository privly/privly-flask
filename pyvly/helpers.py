import urllib

from Crypto.Random import random
from flask import current_app as app, json, request


from pyvly.database import db_session
from pyvly.models import User


def create_user(email, password):
    """Create user account"""
    user = User(email=email,
                password=password,
                token=generate_token(64))
    user.save()
    return user

# Generate a _POOL of ASCII char-codes for a-z A-Z 0-9
_POOL = range(48, 57) + range(65, 90) + range(97, 122)

def generate_token(length=32):
    """
    Generates a random token containing a-z A-Z 0-9 of size `length`
    Crypto.Random may be a bad choice, consider switching to os.urandom:
    http://stackoverflow.com/a/20469525/263132
    """
    return ''.join(chr(random.choice(_POOL)) for _ in range(length))


def privly_URL(post):
    """
    Return the URL for the Privly Application along with query parameters for
    the required access tokens. This should only be called for users who
    already have access to the content.
    """
    # The base tuple that contains the protocol and domain
    config = (app.config['REQUIRED_PROTOCOL'], app.config['LINK_DOMAIN_HOST'])

    # The data URL for accessing the Post data
    data_url = '%s://%s/posts/%s?random_token=%s' %\
        (config + (post.random_id, post.random_token))

    inject_params = post.url_parameters()
    inject_params['privlyDataURL'] = data_url
    # The Privly application url for injection
    return '%s://%s/apps/%s/show?%s' %\
        (config + (post.privly_application, urllib.urlencode(inject_params)))

def jsonify(*args, **kwargs):
    'Improved json response factory'
    indent = None
    data = args[0] if args else dict(kwargs)
   
    if app.config['JSONIFY_PRETTYPRINT_REGULAR'] \
       and not request.is_xhr:
        indent = 2
    return app.response_class(json.dumps(data,
        indent=indent),
        mimetype='application/json')