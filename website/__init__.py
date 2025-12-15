"""
Application factory and core configuration.

Initializes the Flask app, database, blueprints, and Flask-Login
for session-based authentication.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# --------------------------
# Database configuration
# --------------------------
db = SQLAlchemy()
db_name = "registered_users"

# --------------------------
# Application
# --------------------------
""" create app """
def create_app():
    app = Flask(__name__)

    # application configuration
    app.config["SECRET_KEY"] = "choose_your_own_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{db_name}'

    # initialise database
    db.init_app(app)

    # register blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # import models and create tables
    from .models import User
    with app.app_context():
        db.create_all()

    # --------------------------
    # Login manager configuration
    # --------------------------
    login_manager = LoginManager()
    login_manager.login_view = "views.home"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        # load user by primary_key for session management
        return User.query.get(int(id))
    
    return app

