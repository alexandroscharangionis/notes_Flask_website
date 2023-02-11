from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"


# Initialize flask app, add secret key to config, add SQL relative path to config, register route blueprints and return app
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "12345"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    # Import blueprints with routes and register them to Flask app
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
