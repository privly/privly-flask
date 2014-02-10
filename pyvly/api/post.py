from Crypto.Random import random
from datetime import datetime, timedelta

from flask import Blueprint, request, current_app as app, jsonify

from pyvly import helpers

bp = Blueprint(__name__)


@bp.route('/', methods=['POST'])
def create():
    """
    Create a post.
    """

    if app.config['USE_RANDOM_TOKEN']:
        # Check if client defined a random token, if not generate one
        if 'random_token' in request.form:
            random_token = request.form['random_token']
        else:
            random_token = helpers.generate_token(
                app.config['RANDOM_TOKEN_LENGTH'])

    # Create burn after date based off client paramters or generate one
    today = datetime.today()
    if 'seconds_until_burn' in request.form:
        burn_after = timedelta(seconds=request.form['seconds_until_burn']) + \
            today
    else:
        burn_after = timedelta(seconds=app.config['POST_LIFETIME_MAX']) + \
            today

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

    # Create JSON response
    response = jsonify(status='created', location=post)
    response.headers['X-Privly-Url'] = helpers.privly_URL(post)
    return response

@bp.route('/<id>', methods=['PUT'])
def update(id):
    # Load the post out of the database
    post = Post.get(id)

    # If the server is using random_tokens and it's provided, update
    if app.config['USE_RANDOM_TOKEN'] and 'random_token' in request.form:
        post.random_token = request.form['random_token']

    # If `seconds_until_burn` is sent, update the `burn_after` date
    if 'seconds_until_burn' in request.form:
        post.burn_after = datetime.today() + \
            timedelta(seconds=request.form['seconds_until_burn'])

    # If the `privly_application` string is sent, update the post
    if 'privly_application' in request.form:
       post.privly_application = request.form['privly_application']

    return jsonify(json=post)


