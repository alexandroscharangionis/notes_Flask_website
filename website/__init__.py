from flask import Flask


# Initialize flask app, add secret key to config and return app
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "12345"
    return app
