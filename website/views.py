from flask import Blueprint

# Set up blueprint variable for Flask app (actual blueprint is called the same as the variable it's contained in)
views = Blueprint("views", __name__)
