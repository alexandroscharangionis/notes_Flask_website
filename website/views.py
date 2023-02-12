from flask import Blueprint, render_template
from flask_login import login_required, current_user


# Set up blueprint variable for Flask app (actual blueprint is called the same as the variable it's contained in)
views = Blueprint("views", __name__)


@views.route("/")
# Decorator that prevents accessing homepage unless logged in
@login_required
def home():
    return render_template("home.html")
