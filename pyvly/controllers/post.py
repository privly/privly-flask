from Crypto.Random import random
from datetime import datetime, timedelta

from flask import Blueprint, request, current_app as app, jsonify, abort
from flask.ext.login import current_user as user
from flask_wtf.csrf import generate_csrf

from pyvly import helpers, database
from pyvly.models import Post

bp = Blueprint('post', __name__)

@bp.route('/user_account_data')
def user_account_data():
    """
    Get user's account data
    """
    return helpers.jsonify(dict(csrf=generate_csrf(),
                        burntAfter='2014-04-26T02:48:39+00:00',
                        canPost=True,
                        signedIn=False if user.is_anonymous() else True))

@bp.route('', methods=['GET'])
def get_posts():
    """
    Get all a user's posts
    """
    posts = []
    for post in user.posts:
        data = post.__json__()
        data['privly_URL'] = helpers.privly_URL(post)
        posts.append(data)

    return helpers.jsonify(posts)

@bp.route('/<int:id>', methods=['GET'])
@bp.route('/<int:id>.json', methods=['GET'])
def get_post(id):
    """
    Gets a single user's post
    """
    post = user.get_post(id)
    if not post:
        abort(403)
    return helpers.jsonify(post)

@bp.route('', methods=['POST'])
def create():
    """
    Create a post.
    """
    random_token = None
    if app.config['USE_RANDOM_TOKEN']:
        # Check if client defined a random token, if not generate one
        if 'random_token' in request.form:
            random_token = request.form['random_token']
        else:
            random_token = helpers.generate_token(
                app.config['RANDOM_TOKEN_LENGTH'])

    # Create burn after date based off client paramters or generate one
    today = datetime.today()
    if 'post[seconds_until_burn]' in request.form:
        burn_after = timedelta(seconds=int(request.form['post[seconds_until_burn]'])) + \
            today
    else:
        burn_after = timedelta(seconds=app.config['POST_LIFETIME_MAX']) + \
            today

    # Set the privly application, use "PlainPost" as default
    if 'post[privly_application]' in request.form:
        privly_application = request.form['post[privly_application]']
    else:
        privly_application = "PlainPost"

    # Create the Post
    post = Post(
        content=request.form['post[content]'],
        random_token=random_token,
        burn_after=burn_after,
        privly_application=privly_application,
        user=user
    )
    try:
        # Try to save
        post.save()
    except:
        pass

    # Create JSON response
    response = helpers.jsonify(status='created', location=post)
    response.headers['X-Privly-Url'] = helpers.privly_URL(post)
    return response

@bp.route('/<id>', methods=['PUT'])
def update(id):
    """
    Update a Post
    """

    # Load the post out of the database
    post = Post.get_user_post(user, id)

    if not post:
        abort(403)

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

    return helpers.jsonify(json=post)

@bp.route('/<int:id>', methods=['DELETE'])
def destroy(id):
    """
    Deletes a user's Post
    """
    post = Post.get(id)

    if not post:
        abort(403)

    post.delete()

    return helpers.jsonify(success=True)

@bp.route('/destroy_all', methods=['DELETE'])
def destroy_all():
    """
    Delete all user's Posts
    """
    for post in user.posts:
        post.delete(False)

    database.db_session.commit()

    return helpers.jsonify(success=True)


