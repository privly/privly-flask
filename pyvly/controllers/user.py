from flask import Blueprint, redirect, url_for, request, abort
from flask.ext.login import login_user, logout_user, current_user as user, \
    login_required

from pyvly.forms import UserForm, csrf
from pyvly.helpers import jsonify
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
def sign_in():
    """Log the user into the server"""
    # Check for the correct form data to be submitted
    if 'user[password]' not in request.form \
        or 'user[email]' not in request.form:
        abort(400)

    # Get the user and check the password
    user = User.get_by_email(request.form['user[email]'])
    if user and user.check_password(request.form['user[password]']):
        # If the user and credentials are valid, log the user in
        login_user(user)
        return jsonify(success=True)

    # Something went wrong
    return jsonify(success=False, errors=['Login Failed'])


@bp.route('/sign_out', methods=['POST'])
@login_required
@csrf.exempt
def sign_out():
    """Log the user out"""
    logout_user()
    return jsonify(success=True)


@bp.route('/reset_password')
def reset_password():
    return "In progress"



