from flask import Blueprint, render_template
from flask_login import login_required, current_user


# Set up blueprint variable for Flask app (actual blueprint is called the same as the variable it's contained in)
views = Blueprint("views", __name__)


@views.route("/")
# Decorator that prevents accessing homepage unless logged in
@login_required
def home():
    # 'user' arg references the current user via the current_user method inside the html template, so we can display some html elements only if user is signed-in
    return render_template("home.html", user=current_user)
