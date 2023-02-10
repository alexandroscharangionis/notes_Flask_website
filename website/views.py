from flask import Blueprint, render_template

# Set up blueprint variable for Flask app (actual blueprint is called the same as the variable it's contained in)
views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")
