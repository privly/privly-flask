from flask import Blueprint, redirect, url_for, request, abort, jsonify
from flask.ext.login import login_user, logout_user, current_user as user, \
    login_required

from pyvly.forms import UserForm
from pyvly.models import User

bp = Blueprint('user', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def create_user():
    """Registration Page"""

    form = UserForm()
    if form.validate_on_submit():
        # Grab the password from the form
        data = form.data

        # Create the user
        helpers.create_user(data['email'], data['password'])

        return redirect(url_for("login"))

    return "register"


@bp.route('/confirm_account')
def verify():
    return "verify"


@bp.route('/sign_in', methods=['POST'])
def login():
    """Log the user into the server"""
    if 'user[password]' not in request.form \
        or 'user[email]' not in request.form:
        abort(400)

    user = User.get_by_email(request.form['user[email]'])

    if user and user.check_password(request.form['user[password]']):
        login_user(user)
        return jsonify(dict(success=True))

    return jsonify(dict(success=False, errors=['Login Failed']))


@bp.route('/sign_out')
@login_required
def logout():
    logout_user()
    return jsonify(dict(success=True))


@bp.route('/reset_password')
def reset_password():
    return "In progress"



