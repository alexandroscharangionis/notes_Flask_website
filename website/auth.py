from flask import Blueprint

# Set up blueprint variable for Flask app (actual blueprint is called the same as the variable it's contained in)
auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return "<p>Login</p>"


@auth.route("/logout")
def logout():
    return "<p>Logout</p>"


@auth.route("/sign-up")
def sign_up():
    return "<p>Sign up</p>"
