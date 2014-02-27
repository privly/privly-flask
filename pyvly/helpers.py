from Crypto.Random import random
from flask import current_app as app

from pyvly.database import db_session
from pyvly.models import User


def create_user(email, passwd):
    """
    Create user account
    """
    u = User(email=email,
             password=passwd,
             token=generate_token(64))
    db_session.add(u)
    db_session.commit()


def generate_token(length=32):
    """
    Generates a random token containing a-zA-Z0-9
    Crypto.Random may be a bad choice, consider switching to os.urandom:
    http://stackoverflow.com/a/20469525/263132
    """
    # Generate pool of possible characters
    pool = range(48, 57) + range(65, 90) + range(97, 122)
    # Create a string of random characters from the pool of size `length`
    return ''.join(chr(random.choice(pool)) for _ in range(length))


def privly_URL(post):
    """
    Return the URL for the Privly Application along with query parameters for
    the required access tokens. This should only be called for users who
    already have access to the content.
    """
    # The base tuple that contains the protocol and domain
    config = (app.config['REQUIRED_PROTOCOL'], app.config['LINK_DOMAIN_HOST'])

    # The data URL for accessing the Post data
    data_url = '%s://%s/posts/%s,json?random_token=%s' %
        (config + (post.id, post.random_token))

    # The Privly application url for injection
    return '%s://%s/apps/%s/show?%s&privlyDataURL=%s' %
        (config + (post.privly_application, post.url_parameters(), data_url))
