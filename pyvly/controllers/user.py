from flask import Blueprint, redirect, url_for

from pyvly.forms import UserForm

bp = Blueprint(__name__)


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


@bp.route('/login')
def login():
    return "login"


@bp.route('/logout')
@login_required
def logout():
    return 'logout'


@bp.route('/reset_password')
def reset_password():
    return "In progress"
