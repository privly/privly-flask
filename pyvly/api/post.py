from Crypto.Random import random
from datetime import datetime, timedelta

from flask import Blueprint, request, current_app as app


bp = Blueprint(__name__)

def generate_token(length=32):
    """
    Generates a random token containing a-zA-Z0-9
    Crypto.Random may be a bad choice, consider switching to os.urandom:
    http://stackoverflow.com/a/20469525/263132
    """
    pool = range(48, 57) + range(65, 90) + range(97, 122)
    return ''.join(chr(random.choice(pool)) for _ in range(length))


@bp.route('/', methods=['POST'])
def create():
    """
    Create a post.
    """

    # Check if client defined a random token, if not generate one
    if 'random_token' in request.form:
        random_token = request.form['random_token']
    else:
        random_token = generate_token(app.config['RANDOM_TOKEN_LENGTH']

    # Create burn after date based off client paramters or generate one
    today = datetime.today()
    if 'seconds_until_burn' in request.form:
        burn_after = timedelta(seconds=request.form['seconds_until_burn']) + \
            today
    else:
        burn_after = timedelta(seconds=app.config['POST_LIFETIME_MAX'])

    # Set the privly application, use "PlainPost" as default
    if 'privly_application' in request.form:
        privly_application = request.form['privly_application']
    else:
        privly_application = "PlainPost"

    # Create the Post
    post = Post(
        random_token=random_token,
        burn_after=burn_after,
        privly_application=privly_application
    )
    try:
        # Try to save

        post.save()
    except:
        pass


