from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

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

    from .models import User, Note
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    # Redirects user to specified route if login is required:
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
