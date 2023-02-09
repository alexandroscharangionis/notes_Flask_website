from flask import Flask


# Initialize flask app, add secret key to config and return app
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "12345"

    # Import blueprints with routes and register them to Flask app
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
