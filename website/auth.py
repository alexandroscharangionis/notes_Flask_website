from flask import Blueprint

# Set up blueprint variable for Flask app (actual blueprint is called the same as the variable it's contained in)
auth = Blueprint("auth", __name__)
